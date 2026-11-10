#!/usr/bin/env python3
"""
study_results.py - Summary of the Thermo-Calc (TCHEA6 v6.1) study of W-Mo-Ta-Nb-V alloys.

Reads data/calphad/calphad_vs_ml.csv (all alloys with a complete 500-3000 C sweep), adds
rule-of-mixtures density and the Random Forest yield-strength estimate at 1000 C, finds
the single-phase alloys that no other single-phase alloy beats on both solidus and
density, and reports leave-one-out accuracy of the Gaussian-process surrogates.

Writes study_results.md and data/calphad/study_results.csv. Usage: python -m pipeline.study_results
"""
from __future__ import annotations

import contextlib
import io
from pathlib import Path

import numpy as np
import pandas as pd

from pipeline import active_learning as al
from pipeline import hea_model as hm
from pipeline import study_design as sd
from pipeline import paths as P

ELS = al.ELS
YS_T = sd.YS_T


def main():
    d = pd.read_csv(P.COMPARISON)
    X = d[ELS].to_numpy() / 100

    from pymatgen.core import Element
    M = np.array([float(Element(e).atomic_mass) for e in ELS])
    V = M / np.array([float(Element(e).density_of_solid) / 1000 for e in ELS])
    d["density_gcc"] = (X @ M) / (X @ V)
    with contextlib.redirect_stdout(io.StringIO()):
        F = hm.compute_features_general([ELS] * len(d), [list(r) for r in X])
    ysm = sd.strength_model(0)
    d[f"YS_{YS_T}C_MPa"] = ysm.predict(
        np.column_stack([F[hm.FEATURES].to_numpy(), d["density_gcc"], np.full(len(d), YS_T)]))
    d["single_phase_500C"] = d["split_C"] <= 500.0 + 1e-6

    s = d[d["single_phase_500C"]].copy()
    m = d[~d["single_phase_500C"]]
    front = s.iloc[sd.pareto(np.column_stack([s["solidus_C"], -s["density_gcc"]]))]
    front = front.sort_values("solidus_C", ascending=False)

    cv_split = al.loo(X, d["split_C"].to_numpy(), 0)
    cv_sol = al.loo(X, d["solidus_C"].to_numpy(), 0)
    d.to_csv(P.CALPHAD / "study_results.csv", index=False)

    def row(r):
        comp = " ".join(f"{e}{r[e]:.1f}" for e in ELS)
        return (f"| {r['alloy']} | {comp} | {r['solidus_C']:.0f} | {r['density_gcc']:.2f} | "
                f"{r[f'YS_{YS_T}C_MPa']:.0f} |")

    top = s.sort_values("solidus_C", ascending=False).head(10)
    L = ["# Thermo-Calc study of W-Mo-Ta-Nb-V alloys: results\n",
         f"{len(d)} alloys with complete equilibrium sweeps (500–3000 °C) computed in Thermo-Calc "
         "with the TCHEA6 (v6.1) database, summarised by `study_results.py`. All values are "
         "calculated, not measured.\n",
         "## Headline numbers\n",
         f"- **{len(s)} of {len(d)}** alloys are single-phase BCC from 500 °C up to the solidus; "
         f"the rest split into two BCC phases below {d.loc[~d['single_phase_500C'], 'split_C'].max():.0f} °C. "
         "This fraction reflects how alloys were chosen (later rounds targeted single-phase "
         "regions), not how common single-phase alloys are in the system.",
         f"- Highest solidus of a single-phase alloy: **{s['solidus_C'].max():.0f} °C** "
         f"({s.loc[s['solidus_C'].idxmax(), 'alloy']}).",
         f"- Lowest density of a single-phase alloy: **{s['density_gcc'].min():.2f} g/cm³** "
         f"({s.loc[s['density_gcc'].idxmin(), 'alloy']}).",
         f"- Surrogate accuracy (Gaussian process, leave-one-out over all {len(d)}): solidus "
         f"mean abs. error **{cv_sol['mae']:.0f} °C** (ρ {cv_sol['rho']:.2f}); split temperature "
         f"**{cv_split['mae']:.0f} °C** (ρ {cv_split['rho']:.2f}). Guessing the mean would give "
         f"{cv_sol['mae_base']:.0f} and {cv_split['mae_base']:.0f} °C.\n",
         "## Best trade-offs: melting point vs density\n",
         "Single-phase alloys that no other single-phase alloy beats on both solidus (higher) "
         "and density (lower). Moving down the table trades melting point for lower density. "
         "Mole percent.\n",
         f"| Alloy | Composition (at.%) | Solidus (°C) | Density (g/cm³) | YS {YS_T} °C, est. (MPa) |",
         "|---|---|---:|---:|---:|"]
    L += [row(r) for _, r in front.iterrows()]
    L += ["", "## Ten highest-melting single-phase alloys\n",
          f"| Alloy | Composition (at.%) | Solidus (°C) | Density (g/cm³) | YS {YS_T} °C, est. (MPa) |",
          "|---|---|---:|---:|---:|"]
    L += [row(r) for _, r in top.iterrows()]
    L += ["", "## What the study shows\n",
          "- Within this system, high solidus and single-phase stability go together with "
          f"low V and higher W and Ta: single-phase alloys average {s['V'].mean():.1f} % V, "
          f"{s['Mo'].mean():.1f} % Mo, {s['W'].mean():.1f} % W and {s['Ta'].mean():.1f} % Ta, "
          f"against {m['V'].mean():.1f}, {m['Mo'].mean():.1f}, {m['W'].mean():.1f} and "
          f"{m['Ta'].mean():.1f} % for the alloys that split (at {m['split_C'].min():.0f}–"
          f"{m['split_C'].max():.0f} °C). This is a pattern in these calculations, not a tested rule.",
          "- The Gaussian-process surrogate trained only on Thermo-Calc results predicts new "
          "alloys within a few tens of °C; the cross-family ML classifier (trained on "
          "experimental data from many systems) ranks alloys within this system only weakly "
          "(see `calphad_vs_ml.md`).",
          "",
          "## Limits\n",
          "- **Equilibrium calculations only.** TCHEA6 predictions for these compositions have "
          "not been checked against experiments here; real alloys may contain phases or "
          "segregation that equilibrium does not show (see the Scheil results in "
          "`calphad_results.md`).",
          f"- **Strength is a rough estimate.** The yield-strength column comes from a model whose "
          "error on unseen alloy families is about 200 MPa (`properties_results.md`); "
          "differences smaller than that are not meaningful.",
          "- **Density** is a rule-of-mixtures estimate (median error 0.3 % on measured alloys).",
          "- **Not assessed:** ductility, oxidation resistance, creep, processability.",
          "- Ten alloys (R2-*m, R3-*) were calculated at compositions other than planned because of "
          "input errors; they are included at the compositions actually calculated "
          "(`calphad_extra_points.csv`, `calphad_round3_points.csv`).\n",
          "Full table: `data/calphad/study_results.csv`.\n"]
    (P.REPORTS / "study_results.md").write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
