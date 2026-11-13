#!/usr/bin/env python3
"""
mlip_strength.py - Does Vegard's law hold for these alloys? Test with an ML potential.

The Maresca-Curtin strength model depends on the solute misfit volumes dV_n, which
`strength_model.py` takes from Vegard's law (a linear mix of pure-element volumes). Here
the alloy volumes computed with a universal machine-learned interatomic potential
(MACE-MPA-0, `mlip_volumes.py`, data/mlip/alloy_volumes.csv) are used to:

  1. measure how far the computed alloy volumes deviate from Vegard's law;
  2. fit V(c) = sum V_n c_n + sum_{n<m} W_nm c_n c_m and take the apparent (partial) atomic
     volumes at each alloy composition, i.e. the misfit volumes the alloy actually has;
  3. correct the experimental-Vegard misfit volumes by the MLIP's non-Vegard part only,
     dV_n = dV_n(exp. Vegard) + [dV_n(MLIP alloy) - dV_n(MLIP Vegard)], so the potential's
     own error in pure-element lattice parameters cancels;
  4. rerun the strength validation and finalist ranking with the corrected misfits.

Elastic constants are not taken from the MLIP: its pure-element C44 values for Nb, V and Ta
are far from experiment (see the report), so rule-of-mixtures experimental values stay.

Writes reports/mlip_strength.md. Usage: python -m pipeline.mlip_strength
"""
from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from pipeline import paths as P
from pipeline import strength_model as S

ELS = S.ELEMENTS
CSV = P.DATA / "mlip" / "alloy_volumes.csv"
PAIRS = list(combinations(range(5), 2))

# Pure-element elastic constants from MACE-MPA-0 (medium) at 0 K, strain-stress method
# (+-0.5 % strains, relaxed ions), computed 2026-11-13; GPa, (C11, C12, C44).
MLIP_ELASTIC = {"W": (588.7, 256.5, 142.3), "Mo": (518.4, 201.1, 85.0),
                "Ta": (244.2, 183.3, 38.2), "Nb": (236.4, 119.5, -17.5),
                "V": (271.1, 141.5, 6.4)}


# Measured room-temperature lattice parameters (A) of the validation alloys, as checked in
# earlier research runs: (composition, [values], source).
MEASURED_A = [
    ("MoNbTaW", {"W": 25, "Mo": 25, "Ta": 25, "Nb": 25}, [3.2134, 3.220],
     "run-2026-11-11 C21 (X-ray), run-2026-11-09 C2 (neutron)"),
    ("WMoTaNbV", {e: 20 for e in ELS}, [3.1832, 3.185],
     "run-2026-11-11 C21, run-2026-11-09 C2"),
    ("NbTaVW (as tested)", {"Nb": 28.50, "Ta": 29.65, "V": 20.67, "W": 21.18}, [3.2186],
     "Yao et al. 2016 Table 2 (run-2026-11-13 sean-sources S1c)"),
    ("MoNbTaV", {"W": 0, "Mo": 25, "Ta": 25, "Nb": 25, "V": 25}, [3.2036, 3.208],
     "Yao et al., Entropy 2016, Section 3.1 / abstract (run-2026-11-11 D4)"),
]


def load() -> pd.DataFrame:
    d = pd.read_csv(CSV)
    d[ELS] = d[ELS] / 100.0
    return d


def design(C: np.ndarray) -> np.ndarray:
    return np.hstack([C, np.column_stack([C[:, i] * C[:, j] for i, j in PAIRS])])


def fit(d: pd.DataFrame) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(design(d[ELS].to_numpy()), d["volume_A3"].to_numpy(), rcond=None)
    return coef


def volume(coef, c: np.ndarray) -> float:
    return float((design(c[None, :]) @ coef)[0])


def apparent_misfits(coef, c: np.ndarray) -> np.ndarray:
    """dV_n = V_n^app - V_bar, with V_n^app the partial atomic volume (d(N V)/dN_n)."""
    lin, W = coef[:5], coef[5:]
    grad = lin.copy()
    for k, (i, j) in enumerate(PAIRS):
        grad[i] += W[k] * c[j]
        grad[j] += W[k] * c[i]
    v = volume(coef, c)
    v_app = v + grad - c @ grad
    return v_app - v


def pure_volumes(d: pd.DataFrame) -> np.ndarray:
    return np.array([d.loc[d["name"] == e, "volume_A3"].iloc[0] for e in ELS])


def corrected_misfits(coef, vpure, c: np.ndarray) -> np.ndarray:
    exp_v = S.atomic_volumes()
    exp_dv = exp_v - c @ exp_v
    mlip_vegard = vpure - c @ vpure
    return exp_dv + (apparent_misfits(coef, c) - mlip_vegard)


def strength_with_misfits(comp: dict, dV: np.ndarray, T_K=296.0, rate=1e-3) -> float:
    c = S._fractions(comp)
    d = S.descriptors(comp)
    misfit = float(c @ dV ** 2)
    pf = (1 + d["nu"]) / (1 - d["nu"])
    x = misfit / d["b_A"] ** 6
    tau0 = 0.040 * S.ALPHA ** (-1 / 3) * d["mu_GPa"] * pf ** (4 / 3) * x ** (2 / 3) * 1e3
    de = 2.00 * S.ALPHA ** (1 / 3) * d["mu_GPa"] * d["b_A"] ** 3 * pf ** (2 / 3) * x ** (1 / 3) * S.GPA_A3_TO_EV
    s = S.K_B * T_K / de * np.log(S.EPS0 / rate)
    low = 1 - s ** (2 / 3)
    return float(S.TAYLOR * tau0 * (low if low > 0.5 else np.exp(-s / 0.55)))


def loo_fit_error(d: pd.DataFrame) -> float:
    """Leave-one-out error of the quadratic volume fit on the alloys (not pure elements)."""
    errs = []
    for i in d.index[d[ELS].gt(0).sum(axis=1) > 1]:
        coef = fit(d.drop(index=i))
        errs.append(volume(coef, d.loc[i, ELS].to_numpy(float)) - d.loc[i, "volume_A3"])
    return float(np.sqrt(np.mean(np.square(errs))))


def report() -> str:
    d = load()
    coef = fit(d)
    vpure = pure_volumes(d)
    exp_v = S.atomic_volumes()
    alloys = d[d[ELS].gt(0).sum(axis=1) > 1].copy()
    alloys["vegard"] = alloys[ELS].to_numpy() @ vpure
    alloys["dev_pct"] = 100 * (alloys["volume_A3"] / alloys["vegard"] - 1)

    L = ["# Testing Vegard's law with a machine-learned interatomic potential", "",
         "Generated by `pipeline/mlip_strength.py` from `data/mlip/alloy_volumes.csv` "
         "(`pipeline/mlip_volumes.py`). Potential: MACE-MPA-0, medium (a universal "
         "machine-learned interatomic potential trained on DFT data). Each alloy is one "
         "random 128-atom BCC supercell with volume and atom positions relaxed at 0 K. "
         f"{len(alloys)} alloys and the 5 pure elements.", "",
         "## 1. Pure elements: what the potential gets right and wrong", "",
         "| Element | a, MLIP (Å) | a, experiment (Å) | C11 / C12 / C44, MLIP (GPa) | C11 / C12 / C44, experiment (GPa) |",
         "|---|---:|---:|---|---|"]
    for k, e in enumerate(ELS):
        a_m = (2 * vpure[k]) ** (1 / 3)
        L.append(f"| {e} | {a_m:.3f} | {S.LATTICE_A[e]:.4f} | "
                 f"{' / '.join(f'{v:.0f}' for v in MLIP_ELASTIC[e])} | "
                 f"{' / '.join(f'{v:.0f}' for v in S.ELASTIC[e])} |")
    L += ["", "Lattice parameters are within about 1 % (V is 1.5 % too small). Elastic "
          "constants are close for W and Mo but far off for the shear constant C44 of Ta, "
          "Nb and V (Nb's is negative, i.e. mechanically unstable). Plain DFT is known to "
          "have trouble with C44 of Nb and V, and this potential is trained on DFT data. "
          "So the strength model keeps experimental elastic constants, and the potential "
          "is used only for volumes, where it is reliable and where the model assumes "
          "Vegard's law.", "",
          "## 2. How far from Vegard's law?", "",
          f"Alloy volume vs the linear mix of the potential's own pure-element volumes: "
          f"mean deviation {alloys['dev_pct'].mean():+.2f} %, range "
          f"{alloys['dev_pct'].min():+.2f} to {alloys['dev_pct'].max():+.2f} % over "
          f"{len(alloys)} alloys. A quadratic fit V(c) = Σ Vₙcₙ + Σ Wₙₘcₙcₘ reproduces "
          f"held-out alloys to {loo_fit_error(d):.3f} Å³/atom (leave-one-out RMS).", "",
          "Pair terms of the fit (Å³/atom; negative = the pair packs tighter than Vegard):", "",
          "| Pair | W (Å³) |", "|---|---:|"]
    for k, (i, j) in enumerate(PAIRS):
        L.append(f"| {ELS[i]}–{ELS[j]} | {coef[5 + k]:+.2f} |")

    L += ["", "### Check against measured lattice parameters", "",
          "Vegard's law with experimental elemental lattice parameters, and the same with the "
          "potential's non-Vegard correction applied (a × (V_MLIP / V_MLIP,Vegard)^(1/3)):", "",
          "| Alloy | Measured a (Å) | Vegard (Å) | Vegard + MLIP correction (Å) | Source |",
          "|---|---|---:|---:|---|"]
    err_v, err_c = [], []
    for name, comp, vals, src in MEASURED_A:
        c = S._fractions(comp)
        a_v = (2 * c @ exp_v) ** (1 / 3)
        a_c = a_v * (volume(coef, c) / (c @ vpure)) ** (1 / 3)
        m = float(np.mean(vals))
        err_v.append(a_v - m); err_c.append(a_c - m)
        L.append(f"| {name} | {' / '.join(f'{x:.4f}' for x in vals)} | {a_v:.4f} | {a_c:.4f} | {src} |")
    L += ["", f"Mean signed error against the measured values: Vegard {np.mean(err_v):+.4f} Å "
          f"(mean |error| {np.mean(np.abs(err_v)):.4f} Å), corrected {np.mean(err_c):+.4f} Å "
          f"(mean |error| {np.mean(np.abs(err_c)):.4f} Å). The measured values themselves differ "
          "by up to 0.007 Å between studies of the same alloy."]
    L += ["", "## 3. Misfit volumes and strength", "",
          "Corrected misfit volumes keep the experimental Vegard values and add only the "
          "potential's non-Vegard part (its alloy partial volumes minus its own Vegard "
          "misfits), so the potential's errors in pure-element lattice parameters cancel.", "",
          "| Alloy | ΔV_V Vegard → corrected (Å³) | Measured (MPa) | Vegard model (MPa) | Corrected (MPa) |",
          "|---|---|---:|---:|---:|"]
    rows = []
    for alloy, comp, meas, *_ in S.MEASURED:
        c = S._fractions(comp)
        dv_exp = exp_v - c @ exp_v
        dv_cor = corrected_misfits(coef, vpure, c)
        y0, y1 = S.yield_strength(comp), strength_with_misfits(comp, dv_cor)
        rows.append((alloy, meas, y0, y1))
        iv = ELS.index("V")
        vtxt = f"{dv_exp[iv]:+.2f} → {dv_cor[iv]:+.2f}" if c[iv] > 0 else "no V"
        L.append(f"| {alloy} | {vtxt} | {meas} | {y0:.0f} | {y1:.0f} |")
    r = pd.DataFrame(rows, columns=["alloy", "meas", "veg", "cor"])
    mae0 = (r.veg - r.meas).abs().mean()
    mae1 = (r.cor - r.meas).abs().mean()
    rho1 = spearmanr(r.meas, r.cor).correlation
    L += ["", f"Mean absolute error: Vegard {mae0:.0f} MPa, corrected {mae1:.0f} MPa; "
          f"rank correlation with measured, corrected: ρ = {rho1:.2f} (n = 4).", "",
          "| Finalist | Vegard 25 °C (MPa) | Corrected 25 °C | Vegard 1300 °C | Corrected 1300 °C |",
          "|---|---:|---:|---:|---:|"]
    fin = []
    for a, comp in S.finalist_compositions().items():
        c = S._fractions(comp)
        dv = corrected_misfits(coef, vpure, c)
        v = (S.yield_strength(comp, 298.15), strength_with_misfits(comp, dv, 298.15),
             S.yield_strength(comp, 1573.15), strength_with_misfits(comp, dv, 1573.15))
        fin.append((a, *v))
        L.append(f"| {a} | " + " | ".join(f"{x:.0f}" for x in v) + " |")
    f = pd.DataFrame(fin, columns=["alloy", "v25", "c25", "v1300", "c1300"])
    same = list(f.sort_values("v1300").alloy) == list(f.sort_values("c1300").alloy)
    dv_pct = 100 * (r.cor / r.veg - 1)
    better = np.mean(np.abs(err_c)) < np.mean(np.abs(err_v)) - 0.001
    L += ["", f"Finalist ranking at 1300 °C {'unchanged' if same else 'changes'} with the "
          "corrected misfits.", "",
          "## Reading", "",
          "The potential finds that adding V expands these alloys more than Vegard's law "
          "predicts (every pair term with V is positive), so V behaves as a larger atom in the "
          "alloy and its misfit volume shrinks by about a fifth. Because the model's strength "
          "scales with misfit volume to the 4/3 power, the corrected strengths fall and the validation error grows from "
          f"{mae0:.0f} to {mae1:.0f} MPa. The measured lattice parameters do not settle "
          "which is right: " + ("the correction moves them closer to experiment"
          if better else "Vegard's law fits them as well as or better than the corrected "
          "values") + ", and the scatter between studies is as large as the difference. "
          "The project keeps Vegard misfit volumes, as the published model does. Two findings "
          "stand: the strength predictions are sensitive to V's effective size in the alloy "
          f"(in the three V-containing validation alloys the corrected strength is "
          f"{-dv_pct[r.alloy != 'MoNbTaW'].max():.0f}–{-dv_pct[r.alloy != 'MoNbTaW'].min():.0f} % lower), and the finalist "
          "ranking does not depend on that choice.", "",
          "## Caveats", "",
          "- One random configuration per alloy (no special quasirandom structures, no "
          "averaging over configurations); 0 K volumes, no thermal expansion.",
          "- The potential is trained on DFT data and inherits its errors; using only its "
          "deviation from Vegard's law reduces, but does not remove, that dependence.",
          "- The quadratic fit is valid inside the sampled composition range. The potential's "
          "pure V is 1.5 % too small, so its description of V, the element that matters most "
          "here, is the least certain.",
          "- Measured lattice parameters exist for only four alloys, and studies of the same "
          "alloy differ by up to 0.007 Å.", ""]
    return "\n".join(L)


if __name__ == "__main__":
    text = report()
    (P.REPORTS / "mlip_strength.md").write_text(text)
    print(text)
