#!/usr/bin/env python3
"""
select_calphad_points.py - Pick W-Mo-Ta-Nb-V compositions for a Thermo-Calc check of the
ML phase model ("closing the loop").

The five alloys already run (calphad_results.md) sit mostly at high predicted P(BCC).
To test whether the model's ranking means anything, new points must also cover the
middle and the bottom of its range. This script bins the 10,000 screened compositions
by predicted P(BCC) (low / mid / high thirds), then within each bin picks points that
are far apart in composition (farthest-point sampling) and far from the five alloys
already calculated. Compositions are rounded to 0.1 at.% with W as balance, exactly
as they would be typed into Thermo-Calc.

Writes calphad_test_points.csv. Usage: python select_calphad_points.py [--per-bin 3]
"""
from __future__ import annotations

import argparse
import contextlib
import io

import numpy as np
import pandas as pd

import hea_model as hm
from hea_properties import CANDIDATES

ELS = hm.ELEMENTS  # W, Mo, Ta, Nb, V


def farthest_points(X: np.ndarray, fixed: np.ndarray, k: int) -> list[int]:
    chosen = []
    ref = fixed.copy()
    for _ in range(k):
        d = np.min(np.linalg.norm(X[:, None, :] - ref[None, :, :], axis=2), axis=1)
        i = int(np.argmax(d))
        chosen.append(i)
        ref = np.vstack([ref, X[i]])
    return chosen


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-bin", type=int, default=3)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="calphad_test_points.csv")
    args = ap.parse_args(argv)

    with contextlib.redirect_stdout(io.StringIO()):
        df, _ = hm.main(["--seed", str(args.seed), "--out", "/dev/null"])
    df = df[~df["is_equiatomic"]].reset_index(drop=True)
    done = np.array([[c[e] for e in ELS] for c in CANDIDATES.values()])

    q = df["p_bcc"].quantile([1 / 3, 2 / 3]).to_numpy()
    bins = {"low": df["p_bcc"] < q[0], "mid": df["p_bcc"].between(q[0], q[1]),
            "high": df["p_bcc"] > q[1]}
    picks = []
    for name, mask in bins.items():
        sub = df[mask].reset_index(drop=True)
        if name == "low":
            # Always include the single lowest-ranked composition: the sharpest test.
            first = int(sub["p_bcc"].idxmin())
            ref = np.vstack([done, sub[ELS].to_numpy()[first]])
            idx = [first] + farthest_points(sub[ELS].to_numpy(), ref, args.per_bin - 1)
        else:
            idx = farthest_points(sub[ELS].to_numpy(), done, args.per_bin)
        for i in idx:
            r = sub.iloc[i]
            row = {"bin": name, "p_bcc": round(float(r["p_bcc"]), 3)}
            pct = {e: round(100 * float(r[e]), 1) for e in ["Mo", "Ta", "Nb", "V"]}
            pct["W"] = round(100 - sum(pct.values()), 1)
            row.update({e: pct[e] for e in ELS})
            picks.append(row)
            done = np.vstack([done, sub[ELS].to_numpy()[i]])

    out = pd.DataFrame(picks).sort_values("p_bcc", ascending=False).reset_index(drop=True)
    out.insert(0, "id", [f"T{i + 1}" for i in range(len(out))])
    out.to_csv(args.out, index=False)
    print(out.to_string(index=False))
    print(f"\nP(BCC) bin edges: {q[0]:.3f}, {q[1]:.3f}")


if __name__ == "__main__":
    main()
