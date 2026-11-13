#!/usr/bin/env python3
"""
dashboard.py - Data for the browser dashboard (site/index.html, served by GitHub Pages).

Exports everything the page needs to predict a composition client-side, with no server:
  - the two Gaussian-process surrogates (solidus and two-BCC split temperature) fitted on
    the 50 Thermo-Calc results: training compositions, kernel hyperparameters, alpha,
    Cholesky factor, y normalisation, and the leave-one-out calibration of the uncertainty;
  - elemental inputs of the Maresca-Curtin strength model and of rule-of-mixtures density;
  - the 50 calculated alloys, the finalists, and reference predictions for a JS self-check.

Usage: python -m pipeline.dashboard   (writes site/data.json)
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd
from pymatgen.core import Element

from pipeline import active_learning as al
from pipeline import paths as P
from pipeline import strength_model as S
from pipeline.hea_properties import density

OUT = P.ROOT / "site" / "data.json"
SEED = 0


def export_gp(X, y):
    cv = al.loo(X, y, SEED)
    m = al.gp(SEED).fit(X, y)
    k = m.kernel_
    return {
        "const": float(k.k1.k1.constant_value),
        "length": [float(v) for v in np.atleast_1d(k.k1.k2.length_scale)],
        "noise": float(k.k2.noise_level),
        "alpha": m.alpha_.ravel().tolist(),
        "L": m.L_.tolist(),
        "y_mean": float(m._y_train_mean), "y_std": float(m._y_train_std),
        "calib": cv["calib"], "loo_mae": cv["mae"],
    }, m


def main():
    d = pd.read_csv(P.COMPARISON)
    st = pd.read_csv(P.CALPHAD / "study_results.csv").set_index("alloy")
    X = d[al.ELS].to_numpy() / 100
    g_sol, m_sol = export_gp(X, d["solidus_C"].to_numpy())
    g_split, m_split = export_gp(X, d["split_C"].to_numpy())
    alloys = []
    for _, r in d.iterrows():
        alloys.append({"id": r.alloy, **{e: float(r[e]) for e in al.ELS},
                       "solidus": float(r.solidus_C), "split": float(r.split_C),
                       "single": bool(st.loc[r.alloy, "single_phase_500C"]) if r.alloy in st.index else bool(r.single_to_500),
                       "density": float(density(al.ELS, r[al.ELS].to_numpy() / 100))})
    check = []
    for a, comp in S.finalist_compositions().items():
        x = np.array([[comp[e] / 100 for e in al.ELS]])
        check.append({"id": a, **comp,
                      "solidus": float(m_sol.predict(x)[0]), "split": float(m_split.predict(x)[0]),
                      "ys25": S.yield_strength(comp, 298.15), "ys1300": S.yield_strength(comp, 1573.15),
                      "density": float(density(al.ELS, x[0]))})
    data = {
        "elements": al.ELS,
        "X": X.tolist(), "gp_solidus": g_sol, "gp_split": g_split,
        "split_goal": al.SPLIT_GOAL,
        "strength": {"lattice_A": S.LATTICE_A, "elastic_GPa": S.ELASTIC, "alpha": S.ALPHA,
                     "taylor": S.TAYLOR, "eps0": S.EPS0, "strain_rate": 1e-3},
        "mass": {e: float(Element(e).atomic_mass) for e in al.ELS},
        "rho": {e: float(Element(e).density_of_solid) / 1000 for e in al.ELS},
        "alloys": alloys, "finalists": S.FINALISTS + [], "check": check,
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")))
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} kB); LOO MAE solidus "
          f"{g_sol['loo_mae']:.0f} C, split {g_split['loo_mae']:.0f} C")


if __name__ == "__main__":
    main()
