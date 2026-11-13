#!/usr/bin/env python3
"""
finalists.py - Validation against experiments and solidification of the finalists.

  1. Validation: Thermo-Calc (TCHEA6 v6.1) phase predictions for the four W-Mo-Ta-Nb-V
     alloys with experimentally reported phases in the MPEA dataset (Borg et al. 2020).
  2. Solidification: equilibrium vs Scheil freezing ranges for the finalists and the
     cost-oriented candidate T6, compared with the earlier candidates #1, #3 and
     equiatomic WMoTaNbV (#5).
  3. Strength: Thermo-Calc's Yield Strength property model checked against the measured
     room-temperature yield strengths of the four validation alloys, then applied to the
     finalists.

Writes reports/finalists.md. Usage: python -m pipeline.finalists
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pipeline import paths as P
from pipeline.calphad_summary import summarise, summarise_scheil

# Experimental phase reports in data/MPEA_dataset.csv for alloys made only of W, Mo, Ta, Nb, V
# (all equiatomic). Processing as recorded in the dataset; anneal temperatures are not recorded.
VALIDATION = [
    # id,  alloy,       Thermo-Calc file, experiment (dataset), processing, reference DOI
    ("L1", "MoNbTaW",   "hea_L1.csv",          "BCC", "cast; powder", "10.1016/j.intermet.2011.01.004"),
    ("L2", "NbTaVW",    "hea_L2.csv",          "BCC", "cast",         "10.1016/j.msea.2016.07.102"),
    # MoNbTaV: the MPEA dataset labels it "annealed", but the source (Yao et al., Entropy
    # 2016) reports no anneal; tested as cast (docs/research/run-2026-11-11, P4/C13).
    ("L3", "MoNbTaV",   "hea_L3.csv",          "BCC", "as-cast",      "10.3390/e18050189"),
    ("#5", "WMoTaNbV",  "hea_5_control.csv",   "BCC", "cast; powder", "10.1016/j.intermet.2011.01.004"),
]
SCHEIL = [("R5-1", "R5-1"), ("R5-2", "R5-2"), ("R5-13", "R5-13"), ("R5-4", "R5-4"),
          ("T6", "T6"), ("#1", "1"), ("#3", "3"), ("#5", "5")]
EARLIER = {"#1", "#3", "#5"}

# Yield Strength property model (Thermo-Calc 2026a, TCHEA6): Simplified mode, annealing
# temperature 1400 C, solid-solution strengthening only, Single calculation, mole percent.
# Measured values: MPEA dataset (Borg et al. 2020), compression, 25 C. All four are confirmed
# as-cast in the primary sources (NbTaVW in docs/research/run-2026-11-13). None was annealed at 1400 C, so that input matches
# none of the specimens.
YS_DIR = P.CALPHAD / "yield_strength"
YS_MEASURED = [  # id, alloy, measured MPa, note
    ("5", "WMoTaNbV", 1246, "cast"),
    ("L1", "MoNbTaW", 1058, "cast; 996 in a second report"),
    ("L2", "NbTaVW", 1530, "as-cast; checked in Yao et al. 2016 Table 2"),
    ("L3", "MoNbTaV", 1525, "cast"),
]
YS_FINALISTS = ["R5-1", "R5-2", "R5-13", "R5-4", "T6"]
FS_END = 0.99   # Scheil runs stop at 99 % solid


def validation_rows():
    rows = []
    for vid, name, f, exp, proc, doi in VALIDATION:
        path = next(iter(sorted(P.CALPHAD.glob(f))), None) or next(iter(sorted(P.CALPHAD.glob(f"hea_{vid.lstrip('#')}_*.csv"))))
        s = summarise(path)
        split = s["extra"].get("second BCC (A2)", (None,))[0]
        tc = ("single BCC 500 °C → melting" if split is None
              else f"single BCC above {split:.0f} °C; two BCC below")
        agrees = "yes" if split is None else f"yes, if processed above {split:.0f} °C"
        rows.append({"id": vid, "alloy": name, "experiment": exp, "processing": proc,
                     "thermocalc": tc, "split_C": split,
                     "solidus_C": s["solidus"] if s["melted"] else np.nan,
                     "agrees": agrees, "doi": doi, "complete": s["complete"]})
    return pd.DataFrame(rows)


def scheil_rows():
    eq = pd.read_csv(P.CALPHAD / "study_results.csv").set_index("alloy")
    rows = []
    for alloy, stem in SCHEIL:
        sc = summarise_scheil(P.CALPHAD / f"hea_{stem}_scheil.csv")
        r = eq.loc[alloy]
        rows.append({"alloy": alloy, "V_at": r["V"], "liquidus_C": sc["liquidus"],
                     "solidus_eq_C": r["solidus_C"], "eq_range_C": sc["liquidus"] - r["solidus_C"],
                     "scheil_end_C": sc["t_end"], "scheil_range_C": sc["liquidus"] - sc["t_end"],
                     "fs_end": sc["fs_end"], "finalist": alloy.startswith("R5")})
    return pd.DataFrame(rows)


def read_ys(stem: str) -> float:
    """Total yield strength (MPa) from a Property Model export (tab-separated)."""
    d = pd.read_csv(YS_DIR / f"ys_{stem}.csv", sep="\t")
    return float(d.iloc[0, 0])


def ys_rows():
    rows = [{"alloy": a, "measured": m, "note": n, "calc": read_ys(i)}
            for i, a, m, n in YS_MEASURED]
    v = pd.DataFrame(rows)
    v["error"] = v["calc"] - v["measured"]
    f = pd.DataFrame([{"alloy": a, "calc": read_ys(a)} for a in YS_FINALISTS])
    return v, f


def main():
    v, s = validation_rows(), scheil_rows()
    fin, ref = s[s["finalist"]], s[s["alloy"].isin(EARLIER)]
    L = ["# Finalists: validation and solidification\n",
         "Thermo-Calc 2026a, TCHEA6 v6.1. Generated by `pipeline/finalists.py`.\n",
         "## 1. Does Thermo-Calc agree with experiments for this alloy family?\n",
         "The MPEA dataset (Borg et al. 2020) contains experimental phase reports for four "
         "alloys made only of these elements. All four are reported as single-phase BCC.\n",
         "| Alloy | Experiment (processing) | Thermo-Calc TCHEA6 | Consistent? | Reference |",
         "|---|---|---|---|---|"]
    for _, r in v.iterrows():
        L.append(f"| {r['alloy']} | {r['experiment']} ({r['processing']}) | {r['thermocalc']} | "
                 f"{r['agrees']} | doi:{r['doi']} |")
    L += ["",
          "**Reading:** Thermo-Calc never contradicts the experiments. For MoNbTaW and NbTaVW it "
          "predicts single-phase BCC at every temperature. For WMoTaNbV and MoNbTaV it predicts "
          "a split into two BCC phases only below "
          f"{v['split_C'].min():.0f}–{v['split_C'].max():.0f} °C. Casting and typical "
          "high-temperature anneals happen above that, and diffusion in these alloys is slow at "
          "such low temperatures, so the experiments would not be expected to see the split. "
          "This test therefore confirms the high-temperature phase predictions; it cannot confirm "
          "or rule out the predicted low-temperature split, which would need long anneals below "
          "about 800 °C.\n",
          "Caveats: only four alloys, all equiatomic and all single-phase in experiment, so the "
          "test cannot show whether Thermo-Calc correctly predicts a *failure*. MoNbTaV is "
          "labelled \"annealed\" in the MPEA dataset, but its source (Yao et al., Entropy "
          "2016) reports no anneal: it was tested as cast, so the dataset label is wrong "
          "(`docs/research/run-2026-11-11`).",
          ]
    if v["solidus_C"].isna().any():
        miss = ", ".join(v.loc[v["solidus_C"].isna(), "alloy"])
        L.append(f"The {miss} sweep stopped before melting, so its solidus is not available yet "
                 "(the phase result below that temperature is unaffected).")
    L += ["", "## 2. How much do the finalists segregate when cast?\n",
          "Equilibrium freezing assumes the solid stays fully mixed; Scheil assumes no diffusion "
          "in the solid, the worst case for a casting. A wider Scheil range means more "
          "segregation and a harder alloy to homogenise. Scheil runs end at "
          f"{100 * FS_END:.0f} % solid.\n",
          "| Alloy | V (at.%) | Liquidus (°C) | Equilibrium range (°C) | Scheil range to 99 % solid (°C) |",
          "|---|---:|---:|---:|---:|"]
    for _, r in s.iterrows():
        tag = (" (finalist)" if r["finalist"] else
               " (cost candidate)" if r["alloy"] == "T6" else "")
        L.append(f"| {r['alloy']}{tag} | {r['V_at']:.1f} | {r['liquidus_C']:.0f} | "
                 f"{r['eq_range_C']:.0f} | {r['scheil_range_C']:.0f} |")
    L += ["", f"**Reading:** the finalists freeze over {fin['scheil_range_C'].min():.0f}–"
          f"{fin['scheil_range_C'].max():.0f} °C under Scheil, against "
          f"{ref['scheil_range_C'].min():.0f}–{ref['scheil_range_C'].max():.0f} °C for the earlier "
          f"candidates and equiatomic WMoTaNbV; equilibrium ranges are "
          f"{fin['eq_range_C'].min():.0f}–{fin['eq_range_C'].max():.0f} °C against "
          f"{ref['eq_range_C'].min():.0f}–{ref['eq_range_C'].max():.0f} °C. So the search that "
          "favoured high melting point also produced alloys that should segregate less. The "
          "finalists are also lower in V, which is consistent with V widening the freezing range "
          "in these calculations; this is an observation across seven alloys, not a tested rule. "
          "In the five Scheil runs added for this report (finalists and #5), the "
          "Thermo-Calc plots show only liquid + BCC; no other phase forms during "
          "solidification.\n"]
    t6 = s.set_index("alloy").loc["T6"]
    L.append(f"T6, the cheapest single-phase alloy (`cost_supply.md`), has the narrowest Scheil "
             f"range calculated so far ({t6['scheil_range_C']:.0f} °C) and also forms only "
             "liquid + BCC, which strengthens the case for adding it to the finalists.\n")

    yv, yf = ys_rows()
    from scipy.stats import spearmanr
    rho = spearmanr(yv["measured"], yv["calc"]).statistic
    no_l2 = yv[yv["alloy"] != "NbTaVW"]
    L += ["## 3. Can Thermo-Calc's strength model rank the finalists?\n",
          "Yield Strength property model, Simplified mode, annealing temperature 1400 °C, "
          "solid-solution strengthening only (no grain-boundary or precipitation terms). "
          "Measured values are room-temperature compression tests from the MPEA dataset.\n",
          "| Alloy | Measured (MPa) | Thermo-Calc (MPa) | Error (MPa) |",
          "|---|---:|---:|---:|"]
    for _, r in yv.iterrows():
        L.append(f"| {r['alloy']} ({r['note']}) | {r['measured']:.0f} | {r['calc']:.0f} | "
                 f"{r['error']:+.0f} |")
    L += ["",
          f"**Reading: it fails this test.** The rank order does not match (Spearman ρ = "
          f"{rho:.2f}, n = 4). NbTaVW, the strongest alloy in experiments, is predicted the "
          f"weakest, {abs(yv.set_index('alloy').loc['NbTaVW', 'error']):.0f} MPa low. Without "
          f"it the model overestimates every alloy, but by {no_l2['error'].min():.0f}–"
          f"{no_l2['error'].max():.0f} MPa, a spread of "
          f"{no_l2['error'].max() - no_l2['error'].min():.0f} MPa that no single correction "
          "removes.\n",
          "Thermo-Calc's values for the finalists, for the record:\n",
          "| Alloy | Thermo-Calc yield strength (MPa) |", "|---|---:|"]
    for _, r in yf.iterrows():
        L.append(f"| {r['alloy']} | {r['calc']:.0f} |")
    spread = yf["calc"].max() - yf["calc"].min()
    L += ["",
          f"They span only {spread:.0f} MPa, less than the {no_l2['error'].max() - no_l2['error'].min():.0f} "
          "MPa variation in the model's error even on the three alloys it gets in the right "
          "order. So these numbers cannot separate the finalists, and the project keeps its "
          "own strength estimate (`properties_results.md`, about 200 MPa error) as a "
          "tie-breaker only. Strength remains the least certain property in this study.\n",
          "A physics-based replacement (Maresca–Curtin edge-dislocation model, elemental inputs "
          "only) does much better on the same four alloys: see `strength_model.md`.\n",
          "Caveats: four alloys, calculated at nominal equiatomic compositions. All four "
          "measured strengths are confirmed as-cast in their primary sources; the NbTaVW value "
          "(1530 MPa) was checked in run-2026-11-13, which also found the tested NbTaVW ingot "
          "was not equiatomic (Nb 28.5, Ta 29.7, V 20.7, W 21.2 at.% by EDX). The "
"1400 °C annealing temperature used in the model matches none of the specimens. "
          "Measured strengths also depend on processing and test method, which the model "
          "does not represent (`docs/research/run-2026-11-11`).\n"]
    (P.REPORTS / "finalists.md").write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
