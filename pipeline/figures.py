#!/usr/bin/env python3
"""
figures.py - Figures for the README, made from the Thermo-Calc study data.

  reports/figures/melting_vs_density.png
      every calculated alloy, solidus vs density, single-phase vs two-phase, with the
      single-phase alloys no other single-phase alloy beats on both axes connected.
  reports/figures/prediction_by_round.png
      prospective check of the Gaussian-process surrogate: for each round, the model is
      fitted only on earlier rounds and predicts that round's alloys before they are used.

Run after study_results.py. Usage: python -m pipeline.figures
"""
from __future__ import annotations

import warnings

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pipeline import active_learning as al
from pipeline import paths as P
from pipeline import study_design as sd

warnings.filterwarnings("ignore")

# Reference palette (dataviz skill, light mode): categorical slots 1-2, text and surface tokens.
BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1", "#fcfcfb"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": MUTED,
    "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
    "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
})


def round_of(alloy: str) -> int:
    """Round 1 = initial candidates (#1-#5) and test points T1-T9; R<k>-... = round k."""
    return int(alloy[1]) if alloy.startswith("R") else 1


def melting_vs_density(d: pd.DataFrame, out):
    s, m = d[d["single_phase_500C"]], d[~d["single_phase_500C"]]
    front = s.iloc[sd.pareto(np.column_stack([s["solidus_C"], -s["density_gcc"]]))]
    front = front.sort_values("density_gcc")

    fig, ax = plt.subplots(figsize=(7.2, 4.6), dpi=200)
    ax.scatter(m["density_gcc"], m["solidus_C"], s=46, marker="X", color=ORANGE,
               edgecolor=SURFACE, linewidth=1.2, label=f"Splits into two BCC phases ({len(m)})", zorder=3)
    ax.scatter(s["density_gcc"], s["solidus_C"], s=46, marker="o", color=BLUE,
               edgecolor=SURFACE, linewidth=1.2, label=f"Single-phase BCC, 500 °C to melting ({len(s)})", zorder=4)
    ax.plot(front["density_gcc"], front["solidus_C"], color=BLUE, linewidth=1.5, alpha=0.55,
            zorder=2, label="Best trade-off (no alloy beats it on both)")

    # label positions (absolute, in data units) chosen to sit in empty space
    for name, tx, ty, ha in [("R5-1", 13.55, 2830, "right"), ("R5-13", 11.6, 2770, "right"),
                             ("R5-4", 10.9, 2590, "right")]:
        r = d[d["alloy"] == name].iloc[0]
        ax.annotate(f"{name}\n{r['solidus_C']:.0f} °C, {r['density_gcc']:.2f} g/cm³",
                    (r["density_gcc"], r["solidus_C"]), xytext=(tx, ty), ha=ha, va="center",
                    fontsize=8, color=INK2,
                    arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8, shrinkB=4))

    ax.set_xlabel("Density, rule of mixtures (g/cm³)")
    ax.set_ylabel("Solidus, Thermo-Calc TCHEA6 (°C)")
    ax.set_title(f"{len(d)} W-Mo-Ta-Nb-V alloys calculated in Thermo-Calc",
                 loc="left", color=INK, fontsize=11.5, fontweight="bold")
    ax.legend(loc="lower right", frameon=False, fontsize=8.5, labelcolor=INK2)
    fig.tight_layout()
    fig.savefig(out)
    plt.close(fig)


def prediction_by_round(d: pd.DataFrame, out):
    rows = []
    for k in sorted(set(d["round"])) [1:]:
        tr, te = d[d["round"] < k], d[d["round"] == k]
        X, Xt = tr[al.ELS].to_numpy() / 100, te[al.ELS].to_numpy() / 100
        for t, label in [("solidus_C", "Solidus"), ("split_C", "Split temperature")]:
            pred = al.gp(0).fit(X, tr[t].to_numpy()).predict(Xt)
            rows.append({"round": k, "target": label, "n_train": len(tr), "n_test": len(te),
                         "model": np.abs(pred - te[t].to_numpy()).mean(),
                         "baseline": np.abs(tr[t].mean() - te[t].to_numpy()).mean()})
    r = pd.DataFrame(rows)
    r.to_csv(P.CALPHAD / "prediction_by_round.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.6), dpi=200, sharey=True)
    w = 0.38
    for ax, target in zip(axes, ["Solidus", "Split temperature"]):
        q = r[r["target"] == target].reset_index(drop=True)
        x = np.arange(len(q))
        ax.bar(x - w / 2 - 0.01, q["model"], w, color=BLUE, label="GP model (earlier rounds only)")
        ax.bar(x + w / 2 + 0.01, q["baseline"], w, color=MUTED, alpha=0.55, label="Guess the average")
        for xi, v in zip(x, q["model"]):
            ax.text(xi - w / 2, v + 4, f"{v:.0f}", ha="center", va="bottom", fontsize=8, color=INK)
        ax.set_xticks(x, [f"Round {k}\n{a}→{b}" for k, a, b in zip(q["round"], q["n_train"], q["n_test"])],
                      fontsize=8)
        ax.set_title(target, loc="left", color=INK, fontsize=10, fontweight="bold")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("Mean absolute error (°C)")
    axes[0].legend(loc="upper left", frameon=False, fontsize=8, labelcolor=INK2)
    fig.suptitle("Predicting each Thermo-Calc round before running it", x=0.02, ha="left",
                 color=INK, fontsize=11.5, fontweight="bold")
    fig.text(0.02, -0.02, "Under each round: alloys the model was trained on → new alloys predicted.",
             fontsize=8, color=INK2)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return r


def main():
    P.FIGURES.mkdir(parents=True, exist_ok=True)
    d = pd.read_csv(P.CALPHAD / "study_results.csv")
    d["round"] = d["alloy"].map(round_of)
    melting_vs_density(d, P.FIGURES / "melting_vs_density.png")
    r = prediction_by_round(d, P.FIGURES / "prediction_by_round.png")
    print(r.round(1).to_string(index=False))


if __name__ == "__main__":
    main()
