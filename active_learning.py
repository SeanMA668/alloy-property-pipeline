#!/usr/bin/env python3
"""
active_learning.py - Pick the next W-Mo-Ta-Nb-V compositions to run in Thermo-Calc.

Fits two Gaussian-process models directly on the Thermo-Calc results collected so far
(data/calphad/calphad_vs_ml.csv, written by calphad_vs_ml.py):
  - split temperature (highest T with two BCC phases; 500 C = single phase to 500 C)
  - equilibrium solidus
Inputs are the five mole fractions. Each model is checked by leave-one-out before use.

Then it scores a fresh pool of compositions (every element 5-35 at.%) and proposes a
batch: mostly "exploit" points, most likely to stay single-phase (split < 550 C) with a
high solidus, spread apart in composition, plus one "explore" point where the split
model is least certain. Writes calphad_round<N>_points.csv and active_learning.md.

Loop: run calphad_vs_ml.py -> active_learning.py -> run the batch in Thermo-Calc ->
save hea_R<N>-<k>.csv files in data/calphad/ -> repeat.

Usage: python active_learning.py [--batch 5] [--seed 0]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm, spearmanr
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel
from sklearn.model_selection import LeaveOneOut

HERE = Path(__file__).parent
ELS = ["W", "Mo", "Ta", "Nb", "V"]
SPLIT_GOAL = 550.0      # want the split below this (C)
SOLIDUS_MIN = 2450.0    # and a solidus at least this high (C)


def gp(seed):
    k = (ConstantKernel(1.0) * RBF(length_scale=[0.2] * len(ELS), length_scale_bounds=(0.02, 5))
         + WhiteKernel(0.1, (1e-4, 1)))
    return GaussianProcessRegressor(k, normalize_y=True, n_restarts_optimizer=5, random_state=seed)


def loo(X, y, seed):
    """Leave-one-out predictions. 'calib' rescales the model's own uncertainty so that
    held-out errors are, on average, one standard deviation (GPs fitted on a handful
    of points are usually overconfident)."""
    p, s = np.zeros(len(y)), np.zeros(len(y))
    for tr, te in LeaveOneOut().split(X):
        mu, sd = gp(seed).fit(X[tr], y[tr]).predict(X[te], return_std=True)
        p[te], s[te] = mu, sd
    calib = float(np.sqrt(np.mean(((p - y) / np.maximum(s, 1e-6)) ** 2)))
    return {"rho": float(spearmanr(p, y).statistic), "mae": float(np.abs(p - y).mean()),
            "mae_base": float(np.abs(y - y.mean()).mean()), "calib": max(calib, 1.0)}


def pool(n, rng, cmin=0.05, cmax=0.35):
    out = []
    while sum(len(o) for o in out) < n:
        c = cmin + (1 - cmin * len(ELS)) * rng.dirichlet(np.ones(len(ELS)), size=4 * n)
        out.append(c[(c <= cmax).all(axis=1)])
    return np.vstack(out)[:n]


def farthest(Xc, ref, k):
    idx = []
    for _ in range(k):
        dmin = np.min(np.linalg.norm(Xc[:, None] - ref[None], axis=2), axis=1)
        i = int(np.argmax(dmin))
        idx.append(i)
        ref = np.vstack([ref, Xc[i]])
    return idx


def next_round() -> int:
    nums = [int(m.group(1)) for p in HERE.glob("calphad_round*_points.csv")
            if (m := re.search(r"round(\d+)_", p.name))]
    return max(nums, default=1) + 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=5)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args(argv)
    rng = np.random.default_rng(args.seed)

    d = pd.read_csv(HERE / "data" / "calphad" / "calphad_vs_ml.csv")
    X = d[ELS].to_numpy() / 100
    y_split, y_sol = d["split_C"].to_numpy(), d["solidus_C"].to_numpy()
    cv_split, cv_sol = loo(X, y_split, args.seed), loo(X, y_sol, args.seed)
    m_split = gp(args.seed).fit(X, y_split)
    m_sol = gp(args.seed).fit(X, y_sol)

    P = pool(20000, rng)
    mu, sd = m_split.predict(P, return_std=True)
    sd = sd * cv_split["calib"]  # calibrated to leave-one-out errors
    sol = m_sol.predict(P)
    p_good = norm.cdf((SPLIT_GOAL - mu) / np.maximum(sd, 1e-6))
    feasible = sol >= SOLIDUS_MIN

    # Exploit: highest P(split < goal) among feasible, spread out in composition
    order = np.argsort(-np.where(feasible, p_good, -1))
    top = order[:400]
    pick = [top[i] for i in farthest(P[top], X, args.batch - 1)]
    # Explore: most uncertain feasible point, away from data and picks
    unc = np.argsort(-np.where(feasible, sd, -1))[:400]
    pick += [unc[farthest(P[unc], np.vstack([X, P[pick]]), 1)[0]]]

    rnd = next_round()
    rows = []
    for k, i in enumerate(pick, 1):
        pct = {e: round(100 * P[i, j], 1) for j, e in enumerate(ELS) if e != "W"}
        pct["W"] = round(100 - sum(pct.values()), 1)
        rows.append({"id": f"R{rnd}-{k}", "role": "explore" if k == len(pick) else "exploit",
                     **{e: pct[e] for e in ELS},
                     "pred_split_C": round(float(mu[i])), "split_sd_C": round(float(sd[i])),
                     "p_split_below_goal": round(float(p_good[i]), 2),
                     "pred_solidus_C": round(float(sol[i]))})
    batch = pd.DataFrame(rows)
    out_csv = HERE / f"calphad_round{rnd}_points.csv"
    batch.to_csv(out_csv, index=False)

    L = [f"# Active learning, round {rnd}\n",
         f"Models fitted on {len(d)} Thermo-Calc results (`data/calphad/calphad_vs_ml.csv`). "
         "Generated by `active_learning.py`.\n",
         "## How well the models predict (leave-one-out)\n",
         "| Target | Spearman ρ | Mean abs. error (°C) | Error of always guessing the mean (°C) |",
         "|---|---:|---:|---:|",
         f"| Split temperature | {cv_split['rho']:.2f} | {cv_split['mae']:.0f} | {cv_split['mae_base']:.0f} |",
         f"| Solidus | {cv_sol['rho']:.2f} | {cv_sol['mae']:.0f} | {cv_sol['mae_base']:.0f} |",
         "",
         f"The split model's raw uncertainty was {cv_split['calib']:.1f}× too narrow on held-out "
         "alloys, so all ± values and probabilities below are widened by that factor.\n",
         f"For comparison, the cross-family ML model's P(BCC) reaches |ρ| = 0.43 on the split "
         "temperature for the same alloys (`calphad_vs_ml.md`). With so few points these errors "
         "are rough; they will tighten as rounds are added.\n",
         f"## Next batch to run (`{out_csv.name}`)\n",
         f"Goal: split below {SPLIT_GOAL:.0f} °C and solidus at least {SOLIDUS_MIN:.0f} °C. "
         "Mole percent, W as balance. Save results as `hea_<ID>.csv` / `.png` in `data/calphad/`.\n",
         "| ID | Role | Mo | Ta | Nb | V | W (balance) | Predicted split (°C) | ± | "
         f"P(split < {SPLIT_GOAL:.0f}) | Predicted solidus (°C) |",
         "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in rows:
        L.append(f"| {r['id']} | {r['role']} | {r['Mo']} | {r['Ta']} | {r['Nb']} | {r['V']} | "
                 f"{r['W']} | {r['pred_split_C']} | {r['split_sd_C']} | "
                 f"{r['p_split_below_goal']:.2f} | {r['pred_solidus_C']} |")
    L.append("")
    L.append("Treat the probabilities as a ranking, not literal odds: they assume the model's "
             "smooth shape is right, which 14 points cannot confirm. Exploit picks sit near "
             "alloys already known to be single-phase, which is why they look certain.\n")
    L.append("Split predictions below 500 °C mean 'single-phase over the whole calculated range'; "
             "the training data cannot resolve anything lower.\n")
    (HERE / "active_learning.md").write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
