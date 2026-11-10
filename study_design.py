#!/usr/bin/env python3
"""
study_design.py - Design the next Thermo-Calc batch around three goals at once.

Goals, for W-Mo-Ta-Nb-V alloys that stay single-phase BCC (split < 550 C) and have
solidus >= 2450 C, as predicted by the Gaussian processes fitted on the Thermo-Calc
(TCHEA6 v6.1) results collected so far:
  1. high solidus            (GP on Thermo-Calc results)
  2. low density              (rule of mixtures, hea_properties.density)
  3. high yield strength      (Random Forest of hea_properties, at 1000 C)

The batch is spread along the Pareto front of these three (no pick is beaten on all three
by another feasible composition), plus a few "explore" points where the split model is
least certain. Writes calphad_round<N>_points.csv and study_design.md.

Usage: python study_design.py [--batch 16] [--explore 3] [--target 50] [--seed 0]
"""
from __future__ import annotations

import argparse
import contextlib
import io
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

import active_learning as al
import hea_model as hm
import hea_properties as hp

HERE = Path(__file__).parent
ELS = al.ELS
P_MIN = 0.9          # required calibrated P(split < 550 C)
YS_T = 1000          # test temperature for the strength goal (C)


def pareto(obj: np.ndarray) -> np.ndarray:
    """Indices of non-dominated rows; every column is to be maximised."""
    keep = np.ones(len(obj), bool)
    for i in range(len(obj)):
        if keep[i]:
            dom = (obj >= obj[i]).all(1) & (obj > obj[i]).any(1)
            if dom.any():
                keep[i] = False
    return np.where(keep)[0]


def strength_model(seed: int):
    with contextlib.redirect_stdout(io.StringIO()):
        df = hp.load(hp.DATA)
    YS, T, TT, MS = (hp.col(df, s) for s in ("YS (MPa)", "Test temperature", "Type of test", "Microstructure"))
    s = df[df[YS].notna() & (df[TT] == "C") & (df[MS].str.strip() == "BCC") & df[T].notna()]
    feats = hm.FEATURES + ["rho_mix", T]
    return hp.rf(seed).fit(s[feats].to_numpy(), s[YS].to_numpy())


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--explore", type=int, default=3)
    ap.add_argument("--target", type=int, default=50)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args(argv)
    rng = np.random.default_rng(a.seed)

    d = pd.read_csv(HERE / "data" / "calphad" / "calphad_vs_ml.csv")
    X = d[ELS].to_numpy() / 100
    cv_split = al.loo(X, d["split_C"].to_numpy(), a.seed)
    cv_sol = al.loo(X, d["solidus_C"].to_numpy(), a.seed)
    m_split = al.gp(a.seed).fit(X, d["split_C"].to_numpy())
    m_sol = al.gp(a.seed).fit(X, d["solidus_C"].to_numpy())

    P = al.pool(20000, rng)
    mu, sd = m_split.predict(P, return_std=True)
    sd = sd * cv_split["calib"]
    sol = m_sol.predict(P)
    p_good = norm.cdf((al.SPLIT_GOAL - mu) / np.maximum(sd, 1e-6))
    feas = np.where((p_good >= P_MIN) & (sol >= al.SOLIDUS_MIN))[0]

    # density and strength for feasible compositions
    from pymatgen.core import Element
    M = np.array([float(Element(e).atomic_mass) for e in ELS])
    V = M / np.array([float(Element(e).density_of_solid) / 1000 for e in ELS])
    rho = (P @ M) / (P @ V)
    Pf = P[feas]
    with contextlib.redirect_stdout(io.StringIO()):
        F = hm.compute_features_general([ELS] * len(Pf), [list(r) for r in Pf])
    ysm = strength_model(a.seed)
    Xs = np.column_stack([F[hm.FEATURES].to_numpy(), rho[feas], np.full(len(Pf), YS_T)])
    ys = np.full(len(P), np.nan)
    ys[feas] = ysm.predict(Xs)

    # Pareto front on (solidus up, density down, strength up), spread out
    front = feas[pareto(np.column_stack([sol[feas], -rho[feas], ys[feas]]))]
    n_exp = a.batch - a.explore
    picks = [front[i] for i in al.farthest(P[front], X, min(n_exp, len(front)))]
    unc = np.where(sol >= al.SOLIDUS_MIN)[0]
    unc = unc[np.argsort(-sd[unc])][:400]
    picks += [unc[i] for i in al.farthest(P[unc], np.vstack([X, P[picks]]), a.explore)]

    old = HERE / f"calphad_round{al.next_round() - 1}_points.csv"
    rnd = al.next_round()
    if old.exists() and not list((HERE / "data" / "calphad").glob(f"hea_R{rnd - 1}-*.csv")):
        rnd -= 1   # previous round file was never run: replace it
    rows = []
    for k, i in enumerate(picks, 1):
        pct = {e: round(100 * P[i, j], 1) for j, e in enumerate(ELS) if e != "W"}
        pct["W"] = round(100 - sum(pct.values()), 1)
        rows.append({"id": f"R{rnd}-{k}", "role": "explore" if k > n_exp else "pareto",
                     **{e: pct[e] for e in ELS},
                     "pred_split_C": round(float(mu[i])), "split_sd_C": round(float(sd[i])),
                     "p_split_below_goal": round(float(p_good[i]), 2),
                     "pred_solidus_C": round(float(sol[i])),
                     "density_gcc": round(float(rho[i]), 2),
                     f"pred_YS_{YS_T}C_MPa": None if np.isnan(ys[i]) else round(float(ys[i]))})
    b = pd.DataFrame(rows)
    out = HERE / f"calphad_round{rnd}_points.csv"
    b.to_csv(out, index=False)

    yf = ys[feas]
    L = [f"# Study design, round {rnd}: toward {a.target} Thermo-Calc alloys\n",
         f"{len(d)} Thermo-Calc results so far (TCHEA6 v6.1); this batch adds {len(b)}, "
         f"for {len(d) + len(b)}. Generated by `study_design.py`.\n",
         "## Goals\n",
         f"Keep only compositions predicted single-phase BCC (calibrated P(split < "
         f"{al.SPLIT_GOAL:.0f} °C) ≥ {P_MIN}) with solidus ≥ {al.SOLIDUS_MIN:.0f} °C: "
         f"{len(feas)} of {len(P)} random compositions qualify. Among those, the "
         f"{len(front)} on the Pareto front of **solidus (higher)**, **density (lower)** and "
         f"**yield strength at {YS_T} °C (higher)** are candidates; {n_exp} spread-out ones "
         f"are picked, plus {a.explore} explore points where the split model is least certain.\n",
         "## Model accuracy (leave-one-out on Thermo-Calc results)\n",
         f"- Split temperature: mean abs. error {cv_split['mae']:.0f} °C; solidus: "
         f"{cv_sol['mae']:.0f} °C.",
         "- Density: rule of mixtures, median error 0.3 % on measured alloys (`properties_results.md`).",
         f"- **Strength is the weak goal.** Across the qualifying compositions the predicted YS "
         f"at {YS_T} °C ranges {np.nanmin(yf):.0f}–{np.nanmax(yf):.0f} MPa "
         f"(middle 80 %: {np.nanpercentile(yf, 10):.0f}–{np.nanpercentile(yf, 90):.0f}), while the "
         "model's error on unseen alloy families is about 200 MPa. It can flag large "
         "differences only; treat the strength column as a tie-breaker.\n",
         f"## Batch to run (`{out.name}`)\n",
         "Mole percent, W as balance; columns in Thermo-Calc's field order. Same 500–3000 °C "
         "sweep. Save as `hea_<ID>.csv` / `.png` in `data/calphad/`.\n",
         "| ID | Role | Mo | Ta | Nb | V | W (bal.) | Split (°C) | P(single) | Solidus (°C) | "
         f"Density (g/cm³) | YS {YS_T} °C (MPa) |",
         "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for _, r in b.iterrows():
        yv = r[f"pred_YS_{YS_T}C_MPa"]
        L.append(f"| {r['id']} | {r['role']} | {r['Mo']} | {r['Ta']} | {r['Nb']} | {r['V']} | "
                 f"{r['W']} | {r['pred_split_C']} ± {r['split_sd_C']} | {r['p_split_below_goal']:.2f} | "
                 f"{r['pred_solidus_C']} | {r['density_gcc']} | "
                 f"{'—' if pd.isna(yv) else int(yv)} |")
    L += ["", "Split predictions below 500 °C mean single-phase over the whole calculated range. "
          "Explore points are chosen to teach the model, not because they are expected to pass; "
          "their strength is not predicted (they fail the single-phase screen).\n"]
    (HERE / "study_design.md").write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
