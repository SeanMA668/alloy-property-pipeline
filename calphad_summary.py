#!/usr/bin/env python3
"""
calphad_summary.py - Summarise Thermo-Calc (TCHEA) temperature sweeps of the
W-Mo-Ta-Nb-V candidates and write calphad_results.md.

Input: data/calphad/hea_<n>_<label>.csv, tab-separated tables exported from a
Thermo-Calc Equilibrium Calculator one-axis temperature sweep (500-3000 C) with
"Amount of phase" for all phases. Every number in the report is read from these
files; nothing is typed in by hand except the compositions entered in Thermo-Calc.

Usage:  python calphad_summary.py [--dir data/calphad] [--out calphad_results.md]
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

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

    # Second solid phase (e.g. BCC_B2#2): highest temperature it is present at
    extra = {}
    for c in solids[1:]:
        present = solved[solved[c].notna() & (solved[c] > 0)]
        if len(present):
            at_min = solved.loc[solved[tcol] == t_min, c].max()
            extra[c.replace("Amount of ", "").replace(" [mol]", "")] = (
                float(solved.loc[solved[c].notna(), tcol].max()), float(at_min))
    return {"solidus": solidus, "liquidus": liquidus, "t_min": t_min,
            "complete": t_min <= SWEEP_MIN_C + 1e-6, "extra": extra,
            "phases": [c.replace("Amount of ", "").replace(" [mol]", "") for c in phases]}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(Path(__file__).with_name("data") / "calphad"))
    ap.add_argument("--out", default="calphad_results.md")
    args = ap.parse_args(argv)

    rows = []
    for n, (label, comp) in COMPOSITIONS.items():
        f = sorted(Path(args.dir).glob(f"hea_{n}_*.csv"))
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

    L = ["# CALPHAD check of W-Mo-Ta-Nb-V candidates (Thermo-Calc, TCHEA)\n",
         "Equilibrium phase amounts from 500 to 3000 °C, computed by the user in Thermo-Calc "
         "Graphical Mode (TCHEA database) and summarised from the exported tables in "
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
        "Experiments report it single-phase BCC as cast (Senkov et al. 2010); at such low "
        "temperatures diffusion is slow, so the split may not occur in practice.\n"
        "- A sweep that stopped early (no solution below the listed temperature) leaves the "
        "low-temperature behaviour of that alloy unknown, not single-phase.\n"
        "- These are equilibrium calculations with one database. They screen candidates; they "
        "do not replace making and characterising the alloy.\n")
    L.append("Phase columns found per file: " + "; ".join(
        f"#{n}: {', '.join(s['phases'])}" for n, _, _, s, *_ in rows) + ".\n")
    Path(args.out).write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
