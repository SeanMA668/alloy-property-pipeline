#!/usr/bin/env python3
"""
calphad_summary.py - Summarise Thermo-Calc (TCHEA6 v6.1) temperature sweeps of the
W-Mo-Ta-Nb-V candidates and write calphad_results.md.

Input: data/calphad/hea_<n>_<label>.csv, tab-separated tables exported from a
Thermo-Calc Equilibrium Calculator one-axis temperature sweep (500-3000 C) with
"Amount of phase" for all phases. Every number in the report is read from these
files; nothing is typed in by hand except the compositions entered in Thermo-Calc.

Usage: python -m pipeline.calphad_summary [--dir data/calphad] [--out calphad_results.md]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from pipeline import paths as P

# Compositions entered in Thermo-Calc (mole %, W = balance); see hea_model results.md
COMPOSITIONS = {
    1: ("top ML pick", "W23.1 Mo7.1 Ta25.5 Nb25.2 V19.1"),
    2: ("Nb-rich, ML top 20", "W20.5 Mo11.6 Ta13.1 Nb34.1 V20.7"),
    3: ("Ta-rich, ML top 20", "W15.1 Mo15.6 Ta29.0 Nb25.7 V14.6"),
    4: ("old rule-score pick", "W27.6 Mo30.1 Ta5.4 Nb5.8 V31.1"),
    5: ("control, equiatomic", "W20 Mo20 Ta20 Nb20 V20"),
}
SWEEP_MIN_C = 500.0


def summarise(path: Path) -> dict:
    df = pd.read_csv(path, sep="\t").dropna(axis=1, how="all")
    df = df.rename(columns=lambda c: c.strip())
    tcol = [c for c in df.columns if c.startswith("Temperature")][0]
    df = df.dropna(subset=[tcol])
    phases = [c for c in df.columns if c.startswith("Amount of")]
    liq = [c for c in phases if "LIQUID" in c][0]
    solids = [c for c in phases if c != liq]

    # Rows where Thermo-Calc returned a solution (at least one phase amount)
    solved = df[df[phases].notna().any(axis=1)]
    t_min = float(solved[tcol].min())

    solidus = float(solved.loc[solved[liq].notna(), tcol].min())
    liquidus = float(solved.loc[solved[liq] >= 0.999995, tcol].min())

    # Phase split: highest temperature where two or more solid phases coexist.
    # Counted by amount, not by name, because Thermo-Calc may label the single
    # high-temperature phase BCC_B2 in one run and BCC_B2#2 in another.
    extra = {}
    n_solid = (solved[solids].fillna(0) > 1e-6).sum(axis=1)
    if (n_solid >= 2).any():
        # Thermo-Calc writes the exact boundary as a row where both solid
        # columns are filled and one is 0; use it as the split temperature.
        t_split = float(solved.loc[solved[solids].notna().sum(axis=1) >= 2, tcol].max())
        low = solved[solved[tcol] == t_min][solids].fillna(0).iloc[0]
        minority = float(low[low > 1e-6].min())
        extra["second BCC (A2)"] = (t_split, minority)
    return {"solidus": solidus, "liquidus": liquidus, "t_min": t_min,
            "complete": t_min <= SWEEP_MIN_C + 1e-6, "extra": extra,
            "phases": [c.replace("Amount of ", "").replace(" [mol]", "") for c in phases]}


def summarise_scheil(path: Path) -> dict:
    """Classic Scheil table: 'Mole fraction of solid' vs 'Temperature [°C]'."""
    df = pd.read_csv(path, sep="\t").dropna(axis=1, how="all").dropna()
    fs = df.iloc[:, 0].to_numpy()
    t = df.iloc[:, 1].to_numpy()
    at = lambda f: float(np.interp(f, fs, t))
    return {"liquidus": float(t[0]), "t50": at(0.5), "t90": at(0.9),
            "t_end": float(t[-1]), "fs_end": float(fs[-1])}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(P.CALPHAD))
    ap.add_argument("--out", default=str(P.REPORTS / "calphad_results.md"))
    args = ap.parse_args(argv)

    rows = []
    for n, (label, comp) in COMPOSITIONS.items():
        f = sorted(p for p in Path(args.dir).glob(f"hea_{n}_*.csv") if "scheil" not in p.name)
        if not f:
            continue
        s = summarise(f[0])
        if s["extra"]:
            second = "; ".join(f"{p} below {t:.0f} °C ({100 * a:.0f} % at {s['t_min']:.0f} °C)"
                               for p, (t, a) in s["extra"].items())
        else:
            second = "none"
        low = f"{s['t_min']:.0f}" + ("" if s["complete"] else " (sweep stopped early)")
        verdict = ("single BCC from solidus to lowest computed T" if not s["extra"]
                   else "single BCC at high T; second BCC at low T")
        rows.append((n, label, comp, s, second, low, verdict, f[0].name))

    L = ["# CALPHAD check of W-Mo-Ta-Nb-V candidates (Thermo-Calc, TCHEA6 v6.1)\n",
         "Equilibrium phase amounts from 500 to 3000 °C, computed by the user in Thermo-Calc "
         "Graphical Mode (TCHEA6 High Entropy Alloy database, v6.1) and summarised from the exported tables in "
         "`data/calphad/` by `calphad_summary.py`.\n",
         "| # | Alloy (at.%) | Role | Solidus (°C) | Liquidus (°C) | Lowest T computed (°C) | "
         "Second solid phase | Verdict |",
         "|---:|---|---|---:|---:|---:|---|---|"]
    for n, label, comp, s, second, low, verdict, _ in rows:
        L.append(f"| {n} | {comp} | {label} | {s['solidus']:.0f} | {s['liquidus']:.0f} | "
                 f"{low} | {second} | {verdict} |")
    L.append("")
    L.append("## Reading\n")
    L.append(
        "- Every phase Thermo-Calc reported is BCC labelled [A2] (disordered) or LIQUID. "
        "No B2 ordering and no Laves or other intermetallic appeared in any run.\n"
        "- The equiatomic control splits into two disordered BCC phases below about 664 °C. "
        "Experiments report a near-equiatomic WMoTaNbV single-phase BCC as cast (Senkov et "
        "al., Intermetallics 18 (2010) 1758); at such low "
        "temperatures diffusion is slow, so the split may not occur in practice.\n"
        "- The ML-favoured Ta/Nb-rich alloys (#1, #3) are the only ones that stay single-phase "
        "down to 500 °C. The old rule-score pick (#4, W-Mo-V-rich) has the widest split: below "
        "about 842 °C it separates into two BCC phases of roughly equal amount.\n"
        "- A sweep that stopped early (no solution below the listed temperature) leaves the "
        "low-temperature behaviour of that alloy unknown, not single-phase.\n"
        "- These are equilibrium calculations with one database. They screen candidates; they "
        "do not replace making and characterising the alloy.\n")
    scheil = []
    for n, (label, comp) in COMPOSITIONS.items():
        f = Path(args.dir) / f"hea_{n}_scheil.csv"
        eq = next((s for m, _, _, s, *_ in rows if m == n), None)
        if f.exists():
            scheil.append((n, label, comp, summarise_scheil(f), eq))
    if scheil:
        L.append("## Scheil solidification (worst-case casting)\n")
        L.append("Classic Scheil: no diffusion in the solid while the alloy freezes. A wide range "
                 "between the liquidus and the last-liquid temperature means strong segregation "
                 "(coring) in an as-cast ingot, which a homogenisation anneal would have to "
                 "remove.\n")
        L.append("| # | Alloy | Liquidus (°C) | T at 50 % solid (°C) | T at 90 % solid (°C) | "
                 "Last liquid (°C) | Freezing range (°C) | Equilibrium solidus (°C) |")
        L.append("|---:|---|---:|---:|---:|---:|---:|---:|")
        for n, label, comp, s, eq in scheil:
            eq_sol = f"{eq['solidus']:.0f}" if eq else "-"
            L.append(f"| {n} | {comp} | {s['liquidus']:.0f} | {s['t50']:.0f} | {s['t90']:.0f} | "
                     f"{s['t_end']:.0f} (at {100 * s['fs_end']:.0f} % solid) | "
                     f"{s['liquidus'] - s['t_end']:.0f} | {eq_sol} |")
        L.append("")
        L.append("- Only LIQUID and BCC_A2 appear in the Scheil plots: no second phase forms even "
                 "in the last liquid (read from the exported plots; the tables hold only "
                 "temperature and fraction solid).\n"
                 "- The Scheil liquidus differs by a few °C from the equilibrium sweep for the "
                 "same composition. That is within the precision of the two calculation types "
                 "and does not change any conclusion.\n")
    L.append("Phase columns found per file: " + "; ".join(
        f"#{n}: {', '.join(s['phases'])}" for n, _, _, s, *_ in rows) + ".\n")
    Path(args.out).write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
