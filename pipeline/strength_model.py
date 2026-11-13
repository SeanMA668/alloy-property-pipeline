#!/usr/bin/env python3
"""
strength_model.py - Physics-based yield strength from the Maresca-Curtin edge-dislocation model.

Reduced analytic model of Maresca & Curtin, Acta Mater. 182 (2020) 235-249
(doi:10.1016/j.actamat.2019.10.015; arXiv:1901.02100, Section 5):

    tau_y0 = 0.040 a^(-1/3) mu [(1+nu)/(1-nu)]^(4/3) [sum c_n dV_n^2 / b^6]^(2/3)
    dE_b   = 2.00  a^( 1/3) mu b^3 [(1+nu)/(1-nu)]^(2/3) [sum c_n dV_n^2 / b^6]^(1/3)

    tau_y(T) = tau_y0 [1 - ((kT/dE_b) ln(e0/e))^(2/3)]          if tau_y/tau_y0 > 0.5
             = tau_y0 exp(-(1/0.55)(kT/dE_b) ln(e0/e))           otherwise
    sigma_y  = 3.067 tau_y   (Taylor factor)

with line-tension coefficient a = 1/12, reference strain rate e0 = 1e4 /s, alloy elastic
constants by rule of mixtures (mu = sqrt(C44 (C11-C12)/2), B = (C11+2 C12)/3 ... see
`elastic_averages`), and misfit volumes dV_n = V_n - V_alloy from Vegard's law.

Inputs here are elemental room-temperature values (no fitting to any alloy data). The model
covers edge dislocations only; the paper finds edge glide controls strength from moderate
to high temperature in these alloys.

Writes reports/strength_model.md and reports/figures/strength_parity.png.
Usage: python -m pipeline.strength_model
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from pipeline import paths as P

ELEMENTS = ["W", "Mo", "Ta", "Nb", "V"]

# Room-temperature BCC lattice parameters (Angstrom) and single-crystal elastic constants
# (GPa, C11, C12, C44). Standard handbook values; not yet checked against a primary source
# in this repo.
LATTICE_A = {"W": 3.1652, "Mo": 3.1470, "Ta": 3.3029, "Nb": 3.3004, "V": 3.0240}
ELASTIC = {
    "W":  (523.3, 204.5, 160.7),
    "Mo": (465.0, 163.0, 109.0),
    "Ta": (266.0, 158.0, 87.4),
    "Nb": (246.5, 134.5, 28.7),
    "V":  (231.0, 120.0, 43.2),
}

ALPHA = 1.0 / 12.0       # line tension coefficient used in the paper's main analysis
TAYLOR = 3.067
EPS0 = 1.0e4             # reference strain rate, 1/s
K_B = 8.617333262e-5     # eV/K
GPA_A3_TO_EV = 1.0e9 * 1.0e-30 / 1.602176634e-19   # GPa * A^3 -> eV

# Measured room-temperature compression yield strengths (MPa), same as reports/finalists.md.
MEASURED = [  # alloy, composition (at.%), measured MPa, Thermo-Calc MPa, note
    ("WMoTaNbV", {"W": 20, "Mo": 20, "Ta": 20, "Nb": 20, "V": 20}, 1246, 1691, "cast"),
    ("MoNbTaW",  {"W": 25, "Mo": 25, "Ta": 25, "Nb": 25, "V": 0}, 1058, 1482, "cast; 996 in a second report"),
    ("NbTaVW",   {"W": 25, "Mo": 0, "Ta": 25, "Nb": 25, "V": 25}, 1530, 787, "cast; not verified against primary source"),
    ("MoNbTaV",  {"W": 0, "Mo": 25, "Ta": 25, "Nb": 25, "V": 25}, 1525, 1734, "cast"),
]
FINALISTS = ["R5-1", "R5-2", "R5-13", "R5-4", "T6"]
TC_FINALISTS = {"R5-1": 1556, "R5-2": 1636, "R5-13": 1691, "R5-4": 1528, "T6": 1649}


def _fractions(comp: dict) -> np.ndarray:
    c = np.array([float(comp.get(e, 0.0)) for e in ELEMENTS])
    return c / c.sum()


def atomic_volumes() -> np.ndarray:
    """Elemental atomic volumes, A^3 (two atoms per BCC cell)."""
    return np.array([LATTICE_A[e] ** 3 / 2.0 for e in ELEMENTS])


def elastic_averages(c: np.ndarray) -> tuple[float, float]:
    """Rule-of-mixtures alloy shear modulus (GPa) and Poisson ratio, as in the paper."""
    C = np.array([ELASTIC[e] for e in ELEMENTS])
    c11, c12, c44 = c @ C
    mu = np.sqrt(0.5 * c44 * (c11 - c12))
    B = (c11 + 2.0 * c12) / 3.0
    nu = (3.0 * B - 2.0 * mu) / (2.0 * (3.0 * B + mu))
    return float(mu), float(nu)


def descriptors(comp: dict) -> dict:
    c = _fractions(comp)
    V = atomic_volumes()
    v_bar = float(c @ V)
    dV = V - v_bar
    a = (2.0 * v_bar) ** (1.0 / 3.0)
    b = np.sqrt(3.0) / 2.0 * a
    mu, nu = elastic_averages(c)
    misfit = float(c @ dV**2)
    return {"a_A": a, "b_A": b, "mu_GPa": mu, "nu": nu, "sum_c_dV2": misfit,
            "delta_V_rms": np.sqrt(misfit)}


def zero_temperature(comp: dict) -> tuple[float, float]:
    """tau_y0 (MPa) and energy barrier dE_b (eV)."""
    d = descriptors(comp)
    pf = (1.0 + d["nu"]) / (1.0 - d["nu"])
    x = d["sum_c_dV2"] / d["b_A"] ** 6
    tau0 = 0.040 * ALPHA ** (-1 / 3) * d["mu_GPa"] * pf ** (4 / 3) * x ** (2 / 3) * 1e3
    de = 2.00 * ALPHA ** (1 / 3) * d["mu_GPa"] * d["b_A"] ** 3 * pf ** (2 / 3) * x ** (1 / 3) * GPA_A3_TO_EV
    return float(tau0), float(de)


def yield_strength(comp: dict, T_K: float = 296.0, strain_rate: float = 1e-3,
                   switch: str = "paper") -> float:
    """Yield strength sigma_y (MPa) at temperature T and strain rate.

    switch="paper" uses the paper's rule (low-T form while tau/tau0 > 0.5). The two forms
    differ by ~5 % there (0.500 vs 0.526), so strength jumps upward with temperature.
    switch="continuous" takes the larger form, i.e. switches where they cross (~0.53).
    """
    tau0, de = zero_temperature(comp)
    s = K_B * T_K / de * np.log(EPS0 / strain_rate)
    low = 1.0 - s ** (2 / 3)
    high = np.exp(-s / 0.55)
    if switch == "continuous":
        ratio = max(low, high)
    else:
        ratio = low if low > 0.5 else high
    return float(TAYLOR * tau0 * ratio)


def finalist_compositions() -> dict:
    d = pd.read_csv(P.CALPHAD / "study_results.csv").set_index("alloy")
    return {a: d.loc[a, ELEMENTS].to_dict() for a in FINALISTS}


def validation_table() -> pd.DataFrame:
    rows = []
    for alloy, comp, meas, tc, note in MEASURED:
        mc = yield_strength(comp)
        rows.append({"alloy": alloy, "measured": meas, "maresca_curtin": mc,
                     "mc_continuous": yield_strength(comp, switch="continuous"), "thermocalc": tc,
                     "mc_error": mc - meas, "tc_error": tc - meas, "note": note})
    return pd.DataFrame(rows)


def finalist_table(temps_C=(25, 1000, 1300)) -> pd.DataFrame:
    rows = []
    for alloy, comp in finalist_compositions().items():
        d = descriptors(comp)
        tau0, de = zero_temperature(comp)
        r = {"alloy": alloy, "V_pct": comp["V"], "mu_GPa": d["mu_GPa"], "dE_b_eV": de,
             "thermocalc_25C": TC_FINALISTS[alloy]}
        for t in temps_C:
            r[f"mc_{t}C"] = yield_strength(comp, T_K=t + 273.15)
        rows.append(r)
    return pd.DataFrame(rows)


def report() -> str:
    v = validation_table()
    f = finalist_table()
    rho_mc = spearmanr(v["measured"], v["maresca_curtin"]).correlation
    rho_tc = spearmanr(v["measured"], v["thermocalc"]).correlation
    mae_mc = v["mc_error"].abs().mean()
    mae_tc = v["tc_error"].abs().mean()
    L = ["# Physics-based strength model (Maresca–Curtin)", "",
         "Reduced analytic edge-dislocation model of Maresca & Curtin, *Acta Mater.* 182 (2020) "
         "235–249 (doi:10.1016/j.actamat.2019.10.015). Inputs are elemental only: Vegard's-law "
         "atomic volumes from room-temperature lattice parameters and rule-of-mixtures elastic "
         "constants. Nothing is fitted to alloy data. Room temperature (296 K), strain rate "
         "10⁻³ s⁻¹, Taylor factor 3.067. Code: `pipeline/strength_model.py`.", "",
         "## 1. Validation against measured strengths", "",
         "![Predicted vs measured](figures/strength_parity.png)", "",
         "| Alloy | Measured (MPa) | Maresca–Curtin (MPa) | Error | Thermo-Calc (MPa) | Error |",
         "|---|---:|---:|---:|---:|---:|"]
    for _, r in v.iterrows():
        L.append(f"| {r.alloy} | {r.measured:.0f} | {r.maresca_curtin:.0f} | {r.mc_error:+.0f} "
                 f"| {r.thermocalc:.0f} | {r.tc_error:+.0f} |")
    L += ["", f"Spearman rank correlation with measured (n = 4): Maresca–Curtin ρ = {rho_mc:.2f}, "
          f"Thermo-Calc ρ = {rho_tc:.2f}. Mean absolute error: Maresca–Curtin {mae_mc:.0f} MPa, "
          f"Thermo-Calc {mae_tc:.0f} MPa.", "",
          "With n = 4, ρ = 0.80 means one adjacent pair is swapped (WMoTaNbV and MoNbTaV); it is "
          "not statistically significant on its own. The clearer result is the error: every "
          "Maresca–Curtin prediction is within about 210 MPa, and NbTaVW, which Thermo-Calc "
          "misses by 743 MPa, comes out close.", "",
          "**Sensitivity to the regime switch.** At room temperature these alloys sit near "
          "τ/τ₀ = 0.5, where the paper switches between its low- and high-temperature forms "
          "and the two differ by about 5 %. Switching where the forms cross instead "
          "(`switch=\"continuous\"`) gives "
          + ", ".join(f"{r.alloy} {r.mc_continuous:.0f}" for _, r in v.iterrows())
          + f" MPa (mean absolute error {(v['mc_continuous']-v['measured']).abs().mean():.0f} MPa, "
          f"ρ = {spearmanr(v['measured'], v['mc_continuous']).correlation:.2f}). The tables use "
          "the paper's rule.", "",
          "Thermo-Calc values were rerun on 2026-11-13 (Advanced mode, 1000 °C anneal, "
          "solid-solution strengthening on) and reproduced the earlier Simplified/1400 °C values "
          "to within 1 MPa, so the NbTaVW result is not a settings error.", "",
          "## 2. Finalists", "",
          "| Alloy | V (at.%) | μ (GPa) | ΔE_b (eV) | 25 °C | 1000 °C | 1300 °C | Thermo-Calc 25 °C |",
          "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for _, r in f.sort_values("mc_25C", ascending=False).iterrows():
        L.append(f"| {r.alloy} | {r.V_pct:.1f} | {r.mu_GPa:.0f} | {r.dE_b_eV:.2f} | {r.mc_25C:.0f} "
                 f"| {r.mc_1000C:.0f} | {r.mc_1300C:.0f} | {r.thermocalc_25C:.0f} |")
    lo, hi = f["mc_25C"].min(), f["mc_25C"].max()
    best = f.sort_values("mc_1300C").iloc[-1]
    worst = f.sort_values("mc_1300C").iloc[0]
    L += ["", f"**Reading.** At 25 °C the finalists span {hi - lo:.0f} MPa, less than the "
          f"model's {mae_mc:.0f} MPa mean error on the validation alloys, so room-temperature "
          "strength still cannot separate them with confidence. The order is the same at every "
          f"temperature: {best.alloy} is strongest and {worst.alloy} weakest, "
          f"{best.mc_1300C:.0f} vs {worst.mc_1300C:.0f} MPa at 1300 °C. R5-4 has the most V "
          "(the strongest misfit solute) but the least W, and its lower shear modulus and "
          "energy barrier outweigh the extra misfit. The high-temperature values are not "
          "validated here: the paper's own predictions fall below experiment at high "
          "temperature, so treat them as a ranking, not as design numbers."]
    L += ["", "## Caveats", "",
          "- Four validation alloys, all equiatomic and as-cast; NbTaVW's 1530 MPa is not yet "
          "verified against its primary source.",
          "- Edge dislocations only. The paper finds edge glide controls strength at moderate "
          "to high temperature; at room temperature screw dislocations may also contribute.",
          "- The paper reports its predictions fall below experiment at high temperature "
          "(the 900–1300 K plateau is not reproduced), so absolute high-temperature values "
          "are likely low; rankings are the intended use.",
          "- Rule-of-mixtures elastic constants ignore alloying effects (DFT gives a much lower "
          "C44 for equiatomic MoNbTaVW). Elemental inputs are handbook values not yet checked "
          "against primary sources.", ""]
    return "\n".join(L)


def parity_figure(out=None):
    """Predicted vs measured yield strength for both models."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from pipeline.figures import BLUE, ORANGE, INK, INK2, MUTED  # also sets rcParams

    out = out or P.FIGURES / "strength_parity.png"
    v = validation_table()
    fig, ax = plt.subplots(figsize=(6.2, 5.4), dpi=160)
    lim = (600, 1900)
    ax.plot(lim, lim, color=MUTED, lw=1, ls="--", zorder=1)
    ax.fill_between(lim, [x - 200 for x in lim], [x + 200 for x in lim], color=MUTED,
                    alpha=0.12, lw=0, label="±200 MPa")
    for col, c, lab in [("thermocalc", ORANGE, "Thermo-Calc Yield Strength model"),
                        ("maresca_curtin", BLUE, "Maresca–Curtin (elemental inputs only)")]:
        ax.scatter(v["measured"], v[col], s=70, color=c, edgecolor="white", lw=1.2, zorder=3,
                   label=lab)
    for _, r in v.iterrows():
        left = r.alloy == "MoNbTaV"     # sits on top of NbTaVW; label it on the other side
        for y in (r.thermocalc, r.maresca_curtin):
            ax.annotate(r.alloy, (r.measured, y), xytext=(-8 if left else 8, 0),
                        textcoords="offset points", ha="right" if left else "left",
                        va="center", fontsize=7.5, color=INK2)
        ax.plot([r.measured] * 2, [r.thermocalc, r.maresca_curtin], color=MUTED, lw=0.8,
                zorder=2)
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xlabel("Measured yield strength, room temperature (MPa)")
    ax.set_ylabel("Predicted (MPa)")
    ax.set_title("Strength models vs four measured W-Mo-Ta-Nb-V alloys", loc="left",
                 color=INK, fontsize=11, fontweight="bold")
    ax.legend(loc="lower right", frameon=False, fontsize=8, labelcolor=INK2)
    fig.text(0.01, 0.005, "Measured: as-cast compression tests (MPEA dataset). NbTaVW value "
             "not yet verified against its primary source.", fontsize=6.8, color=MUTED)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(out)
    plt.close(fig)


if __name__ == "__main__":
    parity_figure()
    text = report()
    (P.REPORTS / "strength_model.md").write_text(text)
    print(text)
