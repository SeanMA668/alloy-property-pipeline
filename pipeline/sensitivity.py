#!/usr/bin/env python3
"""
sensitivity.py - How much does +1 at.% of each element move the solidus and the split
temperature?

Uses the Gaussian-process surrogates from active_learning.py, fitted on all 50 Thermo-Calc
results. "+1 at.% of element e" means: add 0.01 mole fraction of e and remove it from the
other four in proportion to their amounts, so their ratios stay fixed.

  - Solidus: averaged over the 28 alloys that stay single-phase BCC down to 500 C (the
    region the design is aimed at).
  - Split temperature: averaged only over the 22 alloys whose split is ABOVE 500 C. In the
    other 28 the calculated split is "500 or lower" (the sweep starts at 500 C), so the
    model surface there is flat by construction and its slope means nothing. The 22 split
    alloys sit on the two-phase side, close to the phase boundary the design must avoid.

Uncertainty: 400 joint posterior draws of each GP at x and x + 1 at.%; the change is taken
draw by draw, so the shared uncertainty cancels. Reported as mean and 90 % interval of the
average change. Cross-check: an ordinary least-squares fit on the raw Thermo-Calc values of
the same alloys (no GP), expressed with the same perturbation.

Writes reports/sensitivity.md and data/calphad/sensitivity.csv.
Usage: python -m pipeline.sensitivity
"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning

from pipeline import paths as P
from pipeline.active_learning import ELS, gp

STEP = 0.01      # +1 at.%
N_DRAWS = 400
FLOOR_C = 500.0  # start of the Thermo-Calc sweeps


def perturb(X: np.ndarray, j: int, step: float = STEP) -> np.ndarray:
    """Add `step` mole fraction of element j, taken from the others in proportion."""
    X = np.asarray(X, float)
    xj = X[:, [j]]
    out = X * (1 - xj - step) / (1 - xj)
    out[:, j] = X[:, j] + step
    return out


def gp_sensitivity(model, X: np.ndarray, seed: int = 0) -> pd.DataFrame:
    """Mean change (and 90 % interval) of the model prediction for +1 at.% of each element,
    averaged over the rows of X, from joint posterior draws."""
    rows = []
    for j, e in enumerate(ELS):
        Z = np.vstack([X, perturb(X, j)])
        draws = model.sample_y(Z, n_samples=N_DRAWS, random_state=seed)  # (2n, draws)
        n = len(X)
        delta = (draws[n:] - draws[:n]).mean(axis=0)                    # per draw
        mu = model.predict(Z)
        rows.append({"element": e, "mean": float((mu[n:] - mu[:n]).mean()),
                     "lo": float(np.percentile(delta, 5)), "hi": float(np.percentile(delta, 95)),
                     "min_alloy": float((mu[n:] - mu[:n]).min()),
                     "max_alloy": float((mu[n:] - mu[:n]).max())})
    return pd.DataFrame(rows)


def ols_sensitivity(X: np.ndarray, y: np.ndarray) -> dict[str, float]:
    """Linear fit y = sum_k b_k x_k (mixture model, no intercept) and the change it gives
    for the same +1 at.% perturbation, averaged over X."""
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return {e: float(((perturb(X, j) - X) @ b).mean()) for j, e in enumerate(ELS)}


def run(seed: int = 0) -> dict:
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    d = pd.read_csv(P.COMPARISON)
    X = d[ELS].to_numpy() / 100
    split, sol = d["split_C"].to_numpy(), d["solidus_C"].to_numpy()
    single = split <= FLOOR_C + 1e-6
    m_sol, m_split = gp(seed).fit(X, sol), gp(seed).fit(X, split)
    s_sol = gp_sensitivity(m_sol, X[single], seed)
    s_split = gp_sensitivity(m_split, X[~single], seed)
    s_sol["ols"] = s_sol["element"].map(ols_sensitivity(X[single], sol[single]))
    s_split["ols"] = s_split["element"].map(ols_sensitivity(X[~single], split[~single]))
    return {"solidus": s_sol, "split": s_split, "n_single": int(single.sum()),
            "n_split": int((~single).sum()), "split_range": (split[~single].min(), split[~single].max())}


def _c(x: float) -> str:
    """Signed whole degrees without a '-0'."""
    r = round(x) + 0
    return "0" if r == 0 else f"{r:+d}"


def _table(s: pd.DataFrame) -> list[str]:
    L = ["| +1 at.% of | Change (°C), GP | 90 % interval | Range across alloys | Linear fit on raw data |",
         "|---|---:|---:|---:|---:|"]
    for _, r in s.sort_values("mean", ascending=False).iterrows():
        L.append(f"| {r['element']} | {_c(r['mean'])} | {_c(r['lo'])} to {_c(r['hi'])} | "
                 f"{_c(r['min_alloy'])} to {_c(r['max_alloy'])} | {_c(r['ols'])} |")
    return L


def main():
    r = run()
    sol, spl = r["solidus"], r["split"]
    out = pd.concat([sol.assign(target="solidus"), spl.assign(target="split")])
    out.to_csv(P.CALPHAD / "sensitivity.csv", index=False)

    v_sol = sol.set_index("element")["mean"]
    v_spl = spl.set_index("element")["mean"]
    L = ["# Composition sensitivity\n",
         "How much one extra at.% of each element moves the solidus and the temperature at which "
         "the alloy splits into two BCC phases. Generated by `pipeline/sensitivity.py` from the "
         "Gaussian-process surrogates fitted on all 50 Thermo-Calc (TCHEA6 v6.1) results.\n",
         "**Perturbation.** +1 at.% of one element, removed from the other four in proportion to "
         "their amounts. Intervals are 90 % ranges of the average change over 400 joint "
         "posterior draws of the GP. The last column repeats the calculation with a plain "
         "linear fit to the same Thermo-Calc values, as a check that the GP is not inventing "
         "the trend.\n",
         f"## Solidus ({r['n_single']} alloys that stay single-phase to 500 °C)\n",
         *_table(sol), "",
         f"**Reading:** W ({_c(v_sol['W'])} °C) and Ta ({_c(v_sol['Ta'])} °C) raise the solidus, "
         f"V lowers it most ({_c(v_sol['V'])} °C), and Mo ({_c(v_sol['Mo'])} °C) and Nb "
         f"({_c(v_sol['Nb'])} °C) matter little. The order follows the pure-element melting "
         "points (W 3422, Ta 3017, Mo 2623, Nb 2477, V 1910 °C): swapping in an element that "
         "melts above the alloy's own solidus raises it.\n",
         f"## Split temperature ({r['n_split']} alloys that split above 500 °C, "
         f"{r['split_range'][0]:.0f}–{r['split_range'][1]:.0f} °C)\n",
         "Only these alloys are used. The other 28 have a calculated split of \"500 °C or "
         "lower\" because the sweeps start at 500 °C, so the surrogate is flat there and its "
         "slope would average toward zero. The 22 split alloys lie on the two-phase side of the "
         "boundary, which is where a composition change decides whether an alloy passes.\n",
         *_table(spl), "",
         "Positive means the alloy splits at a *higher* temperature, i.e. moves toward failing "
         "the single-phase goal.\n",
         "**Reading:** "]
    order = v_spl.sort_values()
    helps = [e for e in order.index if order[e] < 0]
    hurts = [e for e in order.index[::-1] if order[e] > 0]
    sig = spl.set_index("element")
    def fmt(e):
        robust = sig.loc[e, "lo"] * sig.loc[e, "hi"] > 0
        return f"{e} ({_c(v_spl[e])} °C{'' if robust else ', interval spans zero'})"
    join = lambda xs: ", ".join(xs[:-1]) + " and " + xs[-1] if len(xs) > 1 else xs[0]
    L[-1] += ("adding " + join([fmt(e) for e in hurts]) + " raises the split temperature; "
              "adding " + join([fmt(e) for e in helps]) + " lowers it.")
    L += ["",
          "## What this means for the design\n",
          f"- **V hurts both goals:** it lowers the solidus ({_c(v_sol['V'])} °C) and raises the "
          f"split ({_c(v_spl['V'])} °C). This is the slope behind the pattern in the README "
          "(single-phase alloys average 9.6 at.% V, split alloys 23.1 %). The finalists keep V "
          "at 5.7–12.1 at.%.",
          f"- **Mo** barely moves the solidus ({_c(v_sol['Mo'])} °C) but raises the split "
          f"({_c(v_spl['Mo'])} °C), so it is the second element to limit near the boundary.",
          f"- **W and Ta help both goals** (solidus {_c(v_sol['W'])} / {_c(v_sol['Ta'])} °C, "
          f"split {_c(v_spl['W'])} / {_c(v_spl['Ta'])} °C) but are the densest elements "
          "(19.3 and 16.7 g/cm³), so they trade directly against weight; see `study_results.md`.",
          f"- **Nb** lowers the solidus a little ({_c(v_sol['Nb'])} °C) and the split a little "
          f"({_c(v_spl['Nb'])} °C) and is light (8.6 g/cm³), consistent with the lightest "
          "finalist, R5-4, being the Nb-rich one.",
          "- These are local slopes, averaged over the alloys listed. They are not additive "
          "rules: the range column shows the same +1 at.% can do noticeably different things "
          "in different parts of composition space.\n",
          "## Limits\n",
          "- Surrogate slopes of a 50-point model, not Thermo-Calc calculations at perturbed "
          "compositions. A direct check would be Thermo-Calc runs at ±2 at.% around one "
          "finalist (planned as set C in the project status).",
          "- The split temperature is censored at 500 °C, so nothing here says how far "
          "below 500 °C the single-phase alloys stay single-phase.",
          "- Equilibrium only; the split is unlikely to occur at low temperature in practice "
          "because diffusion is slow (see `finalists.md`).\n"]
    text = "\n".join(L)
    (P.REPORTS / "sensitivity.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
