#!/usr/bin/env python3
"""
hea_model.py - Phase-stability screening pipeline for W-Mo-Ta-Nb-V refractory HEAs.

Stages
  1. Data ingestion   : elemental data from the Materials Project (mp-api) when an
                        MP_API_KEY is set and the API is reachable; otherwise pymatgen's
                        bundled periodic-table data. Binary mixing enthalpies come from
                        the Miedema-model table of Takeuchi & Inoue (Mater. Trans. 46, 2005),
                        which the Materials Project does not provide.
  2. Feature engineering: 10,000 compositions (6 equiatomic + 9,994 non-equiatomic),
                        computing delta, dH_mix, VEC, dS_mix, Tm, Omega.
  3. Machine learning : Random Forest regression of a rule-based BCC solid-solution
                        stability score (see `stability_score`). IMPORTANT: no experimental
                        phase labels are used. The target is built from published empirical
                        criteria, so the RF is a surrogate of those criteria, not a model
                        validated against experiments.
  4. Reporting        : top-20 compositions by out-of-fold predicted score -> results.md

Usage:  python hea_model.py [--n 10000] [--seed 42] [--out results.md]
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_predict, train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

ELEMENTS = ["W", "Mo", "Ta", "Nb", "V"]
R_GAS = 8.314462618  # J / (mol K)

# Binary mixing enthalpies (kJ/mol) at equiatomic composition, Miedema model,
# Takeuchi & Inoue, Mater. Trans. 46 (2005) 2817. These values were entered by hand
# and are cross-checked in `self_check()` against the widely reported equiatomic
# values for WNbMoTa (-6.5 kJ/mol) and WNbMoTaV (-4.64 kJ/mol).
DH_PAIR = {
    frozenset(("W", "Mo")): 0.0,
    frozenset(("W", "Ta")): -7.0,
    frozenset(("W", "Nb")): -8.0,
    frozenset(("W", "V")): -1.0,
    frozenset(("Mo", "Ta")): -5.0,
    frozenset(("Mo", "Nb")): -6.0,
    frozenset(("Mo", "V")): 0.0,
    frozenset(("Ta", "Nb")): 0.0,
    frozenset(("Ta", "V")): -1.0,
    frozenset(("Nb", "V")): -1.0,
}

# Empirical thresholds used for the BCC solid-solution criteria
DELTA_MAX = 6.6    # % ; Yang & Zhang, Mater. Chem. Phys. 132 (2012) 233
OMEGA_MIN = 1.1    # Yang & Zhang (2012)
VEC_BCC_MAX = 6.87 # Guo et al., J. Appl. Phys. 109 (2011) 103505


# --------------------------------------------------------------------------- #
# Stage 1: data ingestion
# --------------------------------------------------------------------------- #
@dataclass
class ElementData:
    radius: dict      # metallic radius, Angstrom (12-coordination)
    vec: dict         # valence electrons (group number for transition metals)
    tm: dict          # melting point, K
    source: str
    mp_structures: dict  # element -> ground-state space group from MP (if fetched)


def fetch_from_materials_project(api_key: str) -> dict:
    """Return {element: {'spacegroup':..., 'volume_per_atom':..., 'material_id':...}}
    for the lowest-energy elemental entry of each element."""
    from mp_api.client import MPRester

    out = {}
    with MPRester(api_key) as mpr:
        for el in ELEMENTS:
            docs = mpr.materials.summary.search(
                chemsys=el,
                fields=["material_id", "symmetry", "volume", "nsites",
                        "energy_above_hull"],
            )
            if not docs:
                raise RuntimeError(f"No Materials Project entries for {el}")
            gs = min(docs, key=lambda d: d.energy_above_hull)
            out[el] = {
                "material_id": str(gs.material_id),
                "spacegroup": gs.symmetry.symbol,
                "volume_per_atom": gs.volume / gs.nsites,
            }
    return out


def load_element_data() -> ElementData:
    from pymatgen.core import Element

    radius = {el: float(Element(el).metallic_radius) for el in ELEMENTS}
    tm = {el: float(Element(el).melting_point) for el in ELEMENTS}
    vec = {el: int(Element(el).group) for el in ELEMENTS}  # groups 5 / 6

    mp_structures = {}
    source = "pymatgen bundled periodic-table data (Materials Project not queried)"
    api_key = os.environ.get("MP_API_KEY")
    if api_key:
        try:
            mp_structures = fetch_from_materials_project(api_key)
            source = ("pymatgen periodic-table data for radii/Tm/VEC; Materials Project "
                      "(mp-api) for elemental ground-state structures")
        except Exception as exc:  # network blocked, bad key, API change...
            print(f"[ingest] Materials Project query failed ({type(exc).__name__}: {exc}); "
                  "using pymatgen bundled data only.", file=sys.stderr)
    else:
        print("[ingest] MP_API_KEY not set; using pymatgen bundled data only.",
              file=sys.stderr)

    return ElementData(radius, vec, tm, source, mp_structures)


def verify_payload(d: ElementData) -> None:
    """Basic payload checks; raises on missing or non-physical values."""
    for el in ELEMENTS:
        assert 1.0 < d.radius[el] < 2.0, f"radius out of range for {el}"
        assert d.vec[el] in (5, 6), f"unexpected VEC for {el}"
        assert 1500 < d.tm[el] < 4000, f"Tm out of range for {el}"
    for a, b in itertools.combinations(ELEMENTS, 2):
        assert frozenset((a, b)) in DH_PAIR, f"missing dH for {a}-{b}"
    for el, s in d.mp_structures.items():
        if s["spacegroup"] != "Im-3m":
            print(f"[ingest] warning: MP ground state of {el} is {s['spacegroup']}, "
                  "not bcc Im-3m", file=sys.stderr)


# --------------------------------------------------------------------------- #
# Stage 2: compositions and thermodynamic features
# --------------------------------------------------------------------------- #
def equiatomic_compositions(min_elements: int = 4) -> np.ndarray:
    """Equiatomic quaternaries and the quinary. Binaries/ternaries are excluded:
    they are not HEAs, and as a handful of isolated points they sit outside the
    distribution the RF is trained on."""
    rows = []
    for k in range(min_elements, len(ELEMENTS) + 1):
        for subset in itertools.combinations(range(len(ELEMENTS)), k):
            c = np.zeros(len(ELEMENTS))
            c[list(subset)] = 1.0 / k
            rows.append(c)
    return np.array(rows)


def random_compositions(n: int, rng: np.random.Generator,
                        cmin: float = 0.05, cmax: float = 0.35) -> np.ndarray:
    """Non-equiatomic quinary compositions with every element in [cmin, cmax]
    (Yeh's 5-35 at.% HEA definition), sampled uniformly on that simplex region
    by rejection."""
    out = []
    free = 1.0 - cmin * len(ELEMENTS)
    while sum(len(o) for o in out) < n:
        c = cmin + free * rng.dirichlet(np.ones(len(ELEMENTS)), size=4 * n)
        out.append(c[(c <= cmax).all(axis=1)])
    return np.vstack(out)[:n]


def compute_features(C: np.ndarray, d: ElementData) -> pd.DataFrame:
    r = np.array([d.radius[e] for e in ELEMENTS])
    v = np.array([d.vec[e] for e in ELEMENTS])
    tm = np.array([d.tm[e] for e in ELEMENTS])
    H = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        H[i, j] = H[j, i] = DH_PAIR[frozenset((ELEMENTS[i], ELEMENTS[j]))]

    r_bar = C @ r
    delta = 100.0 * np.sqrt(np.sum(C * (1.0 - r[None, :] / r_bar[:, None]) ** 2, axis=1))
    # dH_mix = sum_{i<j} 4 dH_ij c_i c_j  (= 2 * c^T H c with zero diagonal)
    dh_mix = 2.0 * np.einsum("ni,ij,nj->n", C, H, C)
    vec = C @ v
    # dS_mix = -R sum c ln c, with 0 ln 0 := 0 (avoids log(0) math-domain errors)
    with np.errstate(divide="ignore", invalid="ignore"):
        clnc = np.where(C > 0, C * np.log(np.where(C > 0, C, 1.0)), 0.0)
    ds_mix = -R_GAS * clnc.sum(axis=1)
    tm_mix = C @ tm
    # Omega = Tm dS / |dH| ; cap where |dH| -> 0 (ideal-solution limit)
    abs_dh_j = np.abs(dh_mix) * 1000.0
    omega = np.where(abs_dh_j > 1e-9, tm_mix * ds_mix / np.maximum(abs_dh_j, 1e-9), np.inf)

    df = pd.DataFrame(C, columns=ELEMENTS)
    df["delta_pct"] = delta
    df["dH_mix_kJmol"] = dh_mix
    df["VEC"] = vec
    df["dS_mix_JmolK"] = ds_mix
    df["Tm_K"] = tm_mix
    df["Omega"] = omega
    return df


def bcc_ss_criteria(df: pd.DataFrame) -> pd.Series:
    """True when all three empirical criteria for a BCC solid solution hold."""
    return (df["delta_pct"] <= DELTA_MAX) & (df["Omega"] >= OMEGA_MIN) & \
           (df["VEC"] < VEC_BCC_MAX)


def stability_score(df: pd.DataFrame) -> np.ndarray:
    """Rule-based BCC solid-solution stability score (dimensionless, higher = more
    favourable). Equal-weight mean of three normalised margins:
        size     : 1 - delta / 6.6
        entropy  : log10(Omega / 1.1) / 2, clipped to [-1, 1] (Omega >= 110 saturates)
        electron : (6.87 - VEC) / 6.87
    The weights and normalisations are a design choice of this pipeline, not a
    published model."""
    m_size = 1.0 - df["delta_pct"].to_numpy() / DELTA_MAX
    om = np.minimum(df["Omega"].to_numpy(), 1e6)
    m_omega = np.clip(np.log10(om / OMEGA_MIN) / 2.0, -1.0, 1.0)
    m_vec = (VEC_BCC_MAX - df["VEC"].to_numpy()) / VEC_BCC_MAX
    return (m_size + m_omega + m_vec) / 3.0


def self_check(d: ElementData) -> dict:
    """Reproduce reported equiatomic values. Fails loudly if the feature code or
    the hand-entered dH table disagree with them."""
    C = np.array([[0.25, 0.25, 0.25, 0.25, 0.0],   # WMoTaNb
                  [0.2, 0.2, 0.2, 0.2, 0.2]])      # WMoTaNbV
    f = compute_features(C, d)
    checks = {
        "WMoTaNb dH_mix (expect -6.50)": (f.loc[0, "dH_mix_kJmol"], -6.50, 0.01),
        "WMoTaNbV dH_mix (expect -4.64)": (f.loc[1, "dH_mix_kJmol"], -4.64, 0.01),
        "WMoTaNb VEC (expect 5.50)": (f.loc[0, "VEC"], 5.50, 1e-9),
        "WMoTaNbV VEC (expect 5.40)": (f.loc[1, "VEC"], 5.40, 1e-9),
        "WMoTaNbV dS_mix (expect R ln5 = 13.38)": (f.loc[1, "dS_mix_JmolK"], R_GAS * np.log(5), 1e-6),
    }
    for name, (got, exp, tol) in checks.items():
        if abs(got - exp) > tol:
            raise AssertionError(f"self-check failed: {name}: got {got:.4f}")
    return {k: round(float(v[0]), 4) for k, v in checks.items()} | {
        "WMoTaNb delta_pct": round(float(f.loc[0, "delta_pct"]), 3),
        "WMoTaNbV delta_pct": round(float(f.loc[1, "delta_pct"]), 3),
    }


# --------------------------------------------------------------------------- #
# Stage 3: Random Forest
# --------------------------------------------------------------------------- #
FEATURES = ["delta_pct", "dH_mix_kJmol", "VEC", "dS_mix_JmolK", "Tm_K"]


def train_model(df: pd.DataFrame, seed: int):
    X = df[FEATURES].to_numpy()
    y = df["score_target"].to_numpy()
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=seed)
    rf = RandomForestRegressor(n_estimators=300, min_samples_leaf=2,
                               n_jobs=-1, random_state=seed)
    rf.fit(X_tr, y_tr)
    pred_te = rf.predict(X_te)
    metrics = {
        "holdout_R2": float(r2_score(y_te, pred_te)),
        "holdout_MAE": float(mean_absolute_error(y_te, pred_te)),
        "n_train": int(len(y_tr)), "n_test": int(len(y_te)),
    }
    # Out-of-fold predictions for every composition (used for ranking, so no
    # composition is ranked by a model that saw its own label)
    oof = cross_val_predict(
        RandomForestRegressor(n_estimators=300, min_samples_leaf=2,
                              n_jobs=-1, random_state=seed),
        X, y, cv=KFold(5, shuffle=True, random_state=seed), n_jobs=1)
    metrics["oof_R2"] = float(r2_score(y, oof))
    importances = dict(zip(FEATURES, rf.feature_importances_.round(4).tolist()))
    return rf, oof, metrics, importances


# --------------------------------------------------------------------------- #
# Stage 4: report
# --------------------------------------------------------------------------- #
def fmt_comp(row) -> str:
    parts = [f"{el}{100 * row[el]:.1f}" for el in ELEMENTS if row[el] > 0]
    return " ".join(parts)


def write_report(df, top, metrics, importances, checks, d, path, n_eq, seed):
    lines = []
    lines.append("# Refractory HEA (W-Mo-Ta-Nb-V) BCC stability screen\n")
    lines.append("Generated by `hea_model.py` "
                 f"(seed {seed}, {len(df):,} compositions: {n_eq} equiatomic + "
                 f"{len(df) - n_eq:,} non-equiatomic with every element in 5-35 at.%).\n")
    lines.append("## What this ranking is, and is not\n")
    lines.append(
        "- **The target is not experimental.** No measured phase data were used. "
        "Each composition gets a rule-based score built from three published empirical "
        "criteria for BCC solid solutions: atomic size mismatch δ ≤ 6.6 % and "
        "Ω ≥ 1.1 (Yang & Zhang 2012), and VEC < 6.87 (Guo et al. 2011). The score is "
        "the equal-weight mean of the three normalised margins; that weighting is a "
        "choice made for this pipeline.\n"
        "- **The Random Forest is a surrogate of that score.** Its high R² shows it "
        "reproduces the formula from the features, not that it predicts real phase "
        "formation.\n"
        f"- **Every sampled composition passes all three criteria** "
        f"({int(df['bcc_criteria_pass'].sum()):,} of {len(df):,}). All five elements "
        "are BCC and the system has small size mismatch, so the empirical rules cannot "
        "separate good from bad here; the ranking only orders compositions by how far "
        "inside the thresholds they sit.\n"
        "- **Known failure modes the rules ignore:** chemical ordering to B2 predicted "
        "from first principles in Mo-Nb-Ta-W (Widom et al., JOM 2013), and Laves phases "
        "in the V-Ta binary (V2Ta). Low-δ, near-zero-ΔH compositions ranked highly here "
        "should be checked with CALPHAD (e.g. Thermo-Calc) before any experiment.\n"
        "- **The top of the list is boundary-driven.** Ta and Nb form the most negative "
        "pair enthalpies with W and Mo, so the score pushes both toward the 5 at.% "
        "sampling floor. Widening the bounds would move the optimum, so read the top 20 "
        "as 'W-Mo-V-rich, lean in Ta and Nb', not as specific optimal compositions.\n"
        "- **Equiatomic WMoTaNb and WMoTaNbV rank low here, yet both have been reported "
        "as single-phase BCC after arc melting (Senkov et al., Intermetallics 2010).** "
        "A low score therefore does not mean a composition will fail to form BCC.\n")

    lines.append("## Top 20 compositions (ranked by out-of-fold RF prediction)\n")
    lines.append("| Rank | Composition (at.%) | δ (%) | ΔH_mix (kJ/mol) | VEC | "
                 "ΔS_mix (J/mol·K) | T_m (K) | Ω | Rule score | RF predicted score |")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for i, (_, r) in enumerate(top.iterrows(), 1):
        om = "inf" if not np.isfinite(r["Omega"]) else f"{r['Omega']:.1f}"
        lines.append(
            f"| {i} | {fmt_comp(r)} | {r['delta_pct']:.2f} | {r['dH_mix_kJmol']:.2f} | "
            f"{r['VEC']:.2f} | {r['dS_mix_JmolK']:.2f} | {r['Tm_K']:.0f} | {om} | "
            f"{r['score_target']:.4f} | {r['score_pred_oof']:.4f} |")
    lines.append("")

    lines.append("### Equiatomic alloys for reference\n")
    lines.append("| Alloy | δ (%) | ΔH_mix (kJ/mol) | VEC | Ω | RF predicted score | Rank of "
                 f"{len(df):,} |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    ranks = df["score_pred_oof"].rank(ascending=False, method="min").astype(int)
    for idx, r in df[df["is_equiatomic"]].sort_values("score_pred_oof",
                                                       ascending=False).iterrows():
        name = "".join(el for el in ELEMENTS if r[el] > 0)
        lines.append(f"| {name} | {r['delta_pct']:.2f} | {r['dH_mix_kJmol']:.2f} | "
                     f"{r['VEC']:.2f} | {r['Omega']:.1f} | {r['score_pred_oof']:.4f} | "
                     f"{ranks[idx]:,} |")
    lines.append("")

    lines.append("## Model diagnostics\n")
    lines.append(f"- Hold-out R² (20 % test split): {metrics['holdout_R2']:.4f}; "
                 f"MAE {metrics['holdout_MAE']:.4f}")
    lines.append(f"- 5-fold out-of-fold R² over all {len(df):,} compositions: "
                 f"{metrics['oof_R2']:.4f}")
    lines.append("- Feature importances (impurity-based): " +
                 ", ".join(f"{k} {v:.3f}" for k, v in importances.items()))
    lines.append(f"- Feature ranges over the dataset: δ {df['delta_pct'].min():.2f}–"
                 f"{df['delta_pct'].max():.2f} %, ΔH_mix {df['dH_mix_kJmol'].min():.2f}–"
                 f"{df['dH_mix_kJmol'].max():.2f} kJ/mol, VEC {df['VEC'].min():.2f}–"
                 f"{df['VEC'].max():.2f}\n")

    lines.append("## Data sources and checks\n")
    lines.append(f"- Elemental data: {d.source}. Metallic radii (Å): " +
                 ", ".join(f"{e} {d.radius[e]}" for e in ELEMENTS) + ".")
    if d.mp_structures:
        lines.append("- Materials Project ground states: " + ", ".join(
            f"{e} {s['material_id']} ({s['spacegroup']})" for e, s in d.mp_structures.items()))
    lines.append("- Binary ΔH_mix: Miedema values of Takeuchi & Inoue, Mater. Trans. 46 "
                 "(2005) 2817, entered by hand in `DH_PAIR`.")
    lines.append("- Self-check (run every execution; the pipeline stops if any fails):")
    for k, v in checks.items():
        lines.append(f"  - {k}: {v}")
    lines.append("")
    with open(path, "w") as fh:
        fh.write("\n".join(lines))


# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--n", type=int, default=10_000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="results.md")
    ap.add_argument("--csv", default=None, help="optionally save the full dataset")
    args = ap.parse_args(argv)

    rng = np.random.default_rng(args.seed)
    d = load_element_data()
    verify_payload(d)
    print("[ingest] payload:", json.dumps({"radius_A": d.radius, "VEC": d.vec,
                                            "Tm_K": d.tm}, indent=None))
    checks = self_check(d)
    print("[check]", checks)

    C_eq = equiatomic_compositions()
    C_rand = random_compositions(args.n - len(C_eq), rng)
    df = compute_features(np.vstack([C_eq, C_rand]), d)
    df["is_equiatomic"] = [True] * len(C_eq) + [False] * len(C_rand)
    df["bcc_criteria_pass"] = bcc_ss_criteria(df)
    df["score_target"] = stability_score(df)
    assert np.isfinite(df[FEATURES + ["score_target"]].to_numpy()).all(), "non-finite features"

    rf, oof, metrics, importances = train_model(df, args.seed)
    df["score_pred_oof"] = oof
    print("[model]", metrics, importances)

    top = df.sort_values("score_pred_oof", ascending=False).head(20)
    write_report(df, top, metrics, importances, checks, d, args.out, len(C_eq), args.seed)
    if args.csv:
        df.to_csv(args.csv, index=False)
    print(f"[report] wrote {args.out}")
    return df, top


if __name__ == "__main__":
    main()
