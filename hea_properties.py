#!/usr/bin/env python3
"""
hea_properties.py - Density and compressive yield strength of W-Mo-Ta-Nb-V candidates.

  Density  : rule of mixtures (alloy mass / sum of elemental molar volumes), checked
             against every measured density in the training data.
  Strength : Random Forest regression of compressive yield strength on observed
             single-phase BCC alloys (Borg et al., Sci. Data 2020), with test
             temperature as a feature. Validated by cross-validation grouped by
             chemical system, plus a held-out check on the two measured alloys from
             this exact system (WMoTaNb and WMoTaNbV).
  Hardness : evaluated the same way and reported, but not used: it does not beat a
             mean-value baseline by enough to rank candidates.

Writes properties_results.md.  Usage: python hea_properties.py [--seed 42]
"""
from __future__ import annotations

import argparse
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold, cross_val_predict

import hea_model as hm

warnings.filterwarnings("ignore")

DATA = Path(__file__).with_name("data") / "MPEA_dataset.csv"
TEMPS_C = [25, 600, 1000, 1200]

# Candidates checked in Thermo-Calc (see calphad_results.md), mole fractions
CANDIDATES = {
    "#1 top ML pick": {"W": 0.231, "Mo": 0.071, "Ta": 0.255, "Nb": 0.252, "V": 0.191},
    "#2 Nb-rich": {"W": 0.205, "Mo": 0.116, "Ta": 0.131, "Nb": 0.341, "V": 0.207},
    "#3 Ta-rich": {"W": 0.151, "Mo": 0.156, "Ta": 0.290, "Nb": 0.257, "V": 0.146},
    "#4 old rule pick": {"W": 0.276, "Mo": 0.301, "Ta": 0.054, "Nb": 0.058, "V": 0.311},
    "#5 WMoTaNbV (control)": {"W": 0.2, "Mo": 0.2, "Ta": 0.2, "Nb": 0.2, "V": 0.2},
}


def col(df, s):
    return [c for c in df.columns if s in c][0]


def density(els, fracs) -> float:
    """g/cm^3: mass per mole over volume per mole of the pure elements."""
    from pymatgen.core import Element
    mass = sum(x * float(Element(e).atomic_mass) for e, x in zip(els, fracs))
    vol = sum(x * float(Element(e).atomic_mass) / (float(Element(e).density_of_solid) / 1000)
              for e, x in zip(els, fracs))
    return mass / vol


def load(path: Path) -> pd.DataFrame:
    from pymatgen.core import Composition, Element
    df = pd.read_csv(path).dropna(subset=["FORMULA"])
    df["comp"] = df["FORMULA"].map(lambda f: Composition(f.replace(" ", "")).fractional_composition)
    df["els"] = df["comp"].map(lambda c: [str(e) for e in c])
    df["fracs"] = df["comp"].map(lambda c: [float(c[e]) for e in c])
    df = df[df["els"].map(lambda es: all(Element(e).metallic_radius is not None for e in es))].copy()
    feats = hm.compute_features_general(df["els"], df["fracs"])
    feats.index = df.index
    df = pd.concat([df, feats], axis=1)
    df["system"] = df["els"].map(lambda e: "-".join(sorted(e)))
    df["rho_mix"] = [density(e, x) for e, x in zip(df["els"], df["fracs"])]
    return df


def rf(seed):
    return RandomForestRegressor(n_estimators=500, min_samples_leaf=2, n_jobs=-1, random_state=seed)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="properties_results.md")
    args = ap.parse_args(argv)

    df = load(DATA)
    YS, HV, T = col(df, "YS (MPa)"), col(df, "HV"), col(df, "Test temperature")
    TT, MS, ED = col(df, "Type of test"), col(df, "Microstructure"), col(df, "Exp. Density")
    in_sys = df["system"].isin(["Mo-Nb-Ta-V-W", "Mo-Nb-Ta-W"])

    # ---- density check ------------------------------------------------------
    d = df[df[ED].notna()].drop_duplicates("FORMULA")
    derr = 100 * (d["rho_mix"] - d[ED]) / d[ED]
    d_sys = d[d["system"].isin(["Mo-Nb-Ta-V-W", "Mo-Nb-Ta-W"])]

    # ---- yield strength ---------------------------------------------------
    feats = hm.FEATURES + ["rho_mix", T]
    s = df[df[YS].notna() & (df[TT] == "C") & (df[MS].str.strip() == "BCC") & df[T].notna()].copy()
    X, y, g = s[feats].to_numpy(), s[YS].to_numpy(), s["system"].to_numpy()
    p = cross_val_predict(rf(args.seed), X, y, cv=GroupKFold(5), groups=g)
    ys_metrics = {"n": len(s), "systems": s["system"].nunique(),
                  "r2": r2_score(y, p), "mae": mean_absolute_error(y, p),
                  "mae_base": float(np.abs(y - y.mean()).mean())}
    s["pred_cv"] = p
    held = (s[s["system"].isin(["Mo-Nb-Ta-V-W", "Mo-Nb-Ta-W"])]
            .groupby(["system", T]).agg(measured=(YS, lambda v: ", ".join(f"{x:.0f}" for x in sorted(set(v)))),
                                         predicted=("pred_cv", "mean")).reset_index())
    ys_model = rf(args.seed).fit(X, y)

    # ---- hardness (evaluated, not used) -----------------------------------
    hv = df[df[HV].notna() & df[T].fillna(25).between(15, 30) & (df[MS].str.strip() == "BCC")]
    hv = hv.groupby("FORMULA").agg({**{f: "first" for f in hm.FEATURES + ["rho_mix", "system"]}, HV: "mean"})
    phv = cross_val_predict(rf(args.seed), hv[hm.FEATURES + ["rho_mix"]].to_numpy(), hv[HV].to_numpy(),
                            cv=GroupKFold(5), groups=hv["system"].to_numpy())
    hv_metrics = {"n": len(hv), "r2": r2_score(hv[HV], phv), "mae": mean_absolute_error(hv[HV], phv),
                  "mae_base": float(np.abs(hv[HV] - hv[HV].mean()).mean())}

    # ---- candidates ---------------------------------------------------------
    rows = []
    for name, comp in CANDIDATES.items():
        els, fr = list(comp), list(comp.values())
        f = hm.compute_features_general([els], [fr]).iloc[0]
        rho = density(els, fr)
        row = {"name": name, "rho": rho}
        for t in TEMPS_C:
            x = np.array([[*(f[k] for k in hm.FEATURES), rho, t]])
            trees = np.array([tr.predict(x)[0] for tr in ys_model.estimators_])
            row[t] = (float(trees.mean()), float(np.percentile(trees, 10)), float(np.percentile(trees, 90)))
        rows.append(row)

    # ---- report -------------------------------------------------------------
    L = ["# Density and strength of W-Mo-Ta-Nb-V candidates\n",
         "Generated by `hea_properties.py`. Training data: Borg et al., *Sci. Data* 7, 430 (2020).\n",
         "## Predicted properties\n",
         "Compressive yield strength in MPa, as-reported processing (mostly as-cast). Each cell is "
         "the forest mean, with the 10–90 % spread of the individual trees in brackets. The spread "
         "shows model disagreement only; the real error is larger (next section).\n",
         "| Alloy | Density (g/cm³) | YS 25 °C | YS 600 °C | YS 1000 °C | YS 1200 °C | "
         "Specific YS at 1000 °C (MPa·cm³/g) |",
         "|---|---:|---:|---:|---:|---:|---:|"]
    for r in rows:
        cells = [f"{r[t][0]:.0f} [{r[t][1]:.0f}–{r[t][2]:.0f}]" for t in TEMPS_C]
        L.append(f"| {r['name']} | {r['rho']:.2f} | " + " | ".join(cells)
                 + f" | {r[1000][0] / r['rho']:.0f} |")
    L.append("")
    L.append("## How far to trust it\n")
    L.append(f"- **Yield strength:** {ys_metrics['n']} compression tests on single-phase BCC alloys "
             f"from {ys_metrics['systems']} chemical systems. Cross-validation grouped by system: "
             f"R² {ys_metrics['r2']:.2f}, mean absolute error **{ys_metrics['mae']:.0f} MPa** "
             f"(predicting the average every time: {ys_metrics['mae_base']:.0f} MPa). Differences "
             f"between candidates smaller than about {ys_metrics['mae']:.0f} MPa are not meaningful.")
    L.append("- **Held-out check on this system.** Each value below was predicted by a model that "
             "never saw any alloy from that system:\n")
    L.append("| System | Test T (°C) | Measured YS (MPa) | Predicted YS (MPa) |")
    L.append("|---|---:|---|---:|")
    for _, r in held.iterrows():
        L.append(f"| {r['system']} | {r[T]:.0f} | {r['measured']} | {r['predicted']:.0f} |")
    L.append("")
    # Does the held-out model rank WMoTaNbV above WMoTaNb at each tested temperature?
    pair = ["Mo-Nb-Ta-V-W", "Mo-Nb-Ta-W"]
    meas = s.groupby(["system", T])[YS].median().unstack(0)[pair]
    pred = s.groupby(["system", T])["pred_cv"].mean().unstack(0)[pair]
    both = meas.dropna().index
    right = [t for t in both if (pred.loc[t, "Mo-Nb-Ta-V-W"] > pred.loc[t, "Mo-Nb-Ta-W"])
             == (meas.loc[t, "Mo-Nb-Ta-V-W"] > meas.loc[t, "Mo-Nb-Ta-W"])]
    wrong = [t for t in both if t not in right]
    L.append(f"  Measured, WMoTaNbV is stronger than WMoTaNb at every temperature. The model "
             f"ranks them correctly at {', '.join(f'{t:.0f}' for t in right)} °C"
             + (f" and in the wrong order at {', '.join(f'{t:.0f}' for t in wrong)} °C"
                if wrong else "")
             + ", and it narrows the measured gap. The same WMoTaNbV alloy is reported at "
             "1246 and 2612 MPa at room temperature by different studies: measured strength "
             "depends strongly on processing and testing.")
    L.append("- **Reading the candidate table:** #1, #2, #3 and the control are predicted within "
             "a few tens of MPa of each other above 600 °C, well inside the model error, so the "
             "model cannot separate them on strength. #4 is predicted about 240 MPa weaker at "
             "1000 °C, which is just above the error. Small non-monotonic steps with temperature "
             "(e.g. 600 vs 1000 °C) are noise from the forest, not physics.")
    L.append(f"- **Density:** rule of mixtures vs {len(d)} measured densities: median error "
             f"{derr.abs().median():.1f} %; for this system "
             + ", ".join(f"{r['FORMULA'].replace(' ', '')} {r['rho_mix']:.2f} vs {r[ED]:.2f} g/cm³"
                         for _, r in d_sys.iterrows())
             + ". The largest errors (over 40 %) are Zn- and Ag-containing alloys, not relevant here.")
    L.append(f"- **Hardness was not usable:** {hv_metrics['n']} room-temperature BCC alloys, grouped "
             f"cross-validation R² {hv_metrics['r2']:.2f}, error {hv_metrics['mae']:.0f} HV vs "
             f"{hv_metrics['mae_base']:.0f} HV for the average. It is not reported for the candidates.")
    L.append("- **Not modelled:** ductility, oxidation resistance, creep. Refractory alloys of this "
             "family are known to be brittle at room temperature; strength alone does not make a "
             "usable alloy.\n")
    Path(args.out).write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
