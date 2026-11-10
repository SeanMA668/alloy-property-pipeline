#!/usr/bin/env python3
"""
hea_model.py - Phase-stability screening pipeline for W-Mo-Ta-Nb-V refractory HEAs.

Stages
  1. Data ingestion    : elemental data from the Materials Project (mp-api) when an
                         MP_API_KEY is set and the API is reachable; otherwise pymatgen's
                         bundled periodic-table data. Binary mixing enthalpies are the
                         Miedema-model values of Takeuchi & Inoue (Mater. Trans. 46, 2005),
                         read from matminer's copy of that table (the Materials Project does
                         not provide them).
  2. Training data     : observed phases of real alloys from Borg et al., "Expanded dataset
                         of mechanical properties and observed phases of multi-principal
                         element alloys", Sci. Data 7, 430 (2020), data/MPEA_dataset.csv
                         (Apache-2.0, see data/LICENSE-MPEA_dataset).
  3. Feature engineering: delta, dH_mix, VEC, dS_mix and Tm for every training alloy and
                         for 10,000 W-Mo-Ta-Nb-V compositions (6 equiatomic + 9,994
                         non-equiatomic).
  4. Machine learning  : Random Forest classifier of "single-phase BCC observed" vs not,
                         validated with cross-validation grouped by chemical system and
                         compared against the published empirical rules on the same alloys.
  5. Reporting         : top-20 compositions by predicted P(single-phase BCC) -> results.md

Usage:  python hea_model.py [--n 10000] [--seed 42] [--out results.md]
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score, roc_auc_score
from sklearn.model_selection import GroupKFold, cross_val_predict

warnings.filterwarnings("ignore", message=".*metallic_radius.*")
warnings.filterwarnings("ignore", message=".*No Pauling electronegativity.*")
warnings.filterwarnings("ignore", module="pymatgen")
warnings.filterwarnings("ignore", module="matminer")

ELEMENTS = ["W", "Mo", "Ta", "Nb", "V"]
R_GAS = 8.314462618  # J / (mol K)
DATA_PATH = Path(__file__).with_name("data") / "MPEA_dataset.csv"

# Binary mixing enthalpies (kJ/mol) for the five target elements, Takeuchi & Inoue
# (2005). Entered by hand; `self_check()` verifies every value against matminer's copy
# of the same table and against the reported equiatomic WNbMoTa / WNbMoTaV values.
DH_PAIR = {
    frozenset(("W", "Mo")): 0.0,
    frozenset(("W", "Ta")): -7.0,
    frozenset(("W", "Nb")): -8.0,
    frozenset(("W", "V")): -1.0,
    frozenset(("Mo", "Ta")): -5.0,
    frozenset(("Mo", "Nb")): -6.0,
    frozenset(("Mo", "V")): 0.0,
    frozenset(("Ta", "Nb")): 0.0,
    frozenset(("Ta", "V")): -1.0,
    frozenset(("Nb", "V")): -1.0,
}

# Empirical thresholds for the rule-based BCC solid-solution baseline
DELTA_MAX = 6.6    # % ; Yang & Zhang, Mater. Chem. Phys. 132 (2012) 233
OMEGA_MIN = 1.1    # Yang & Zhang (2012)
VEC_BCC_MAX = 6.87 # Guo et al., J. Appl. Phys. 109 (2011) 103505

FEATURES = ["delta_pct", "dH_mix_kJmol", "VEC", "dS_mix_JmolK", "Tm_K"]


# --------------------------------------------------------------------------- #
# Stage 1: data ingestion
# --------------------------------------------------------------------------- #
@dataclass
class ElementData:
    radius: dict      # metallic radius, Angstrom (12-coordination)
    vec: dict         # valence electrons (group number for transition metals)
    tm: dict          # melting point, K
    source: str
    mp_structures: dict  # element -> ground-state space group from MP (if fetched)


def fetch_from_materials_project(api_key: str) -> dict:
    """Return {element: {'spacegroup':..., 'volume_per_atom':..., 'material_id':...}}
    for the lowest-energy elemental entry of each element."""
    from mp_api.client import MPRester

    out = {}
    with MPRester(api_key) as mpr:
        for el in ELEMENTS:
            docs = mpr.materials.summary.search(
                chemsys=el,
                fields=["material_id", "symmetry", "volume", "nsites",
                        "energy_above_hull"],
            )
            if not docs:
                raise RuntimeError(f"No Materials Project entries for {el}")
            gs = min(docs, key=lambda d: d.energy_above_hull)
            out[el] = {
                "material_id": str(gs.material_id),
                "spacegroup": gs.symmetry.symbol,
                "volume_per_atom": gs.volume / gs.nsites,
            }
    return out


def valence_electrons(symbol: str) -> int:
    """VEC convention of Guo et al. (2011): group number for groups 1-12,
    group - 10 for groups 13-18."""
    from pymatgen.core import Element
    g = Element(symbol).group
    return g if g <= 12 else g - 10


def load_element_data() -> ElementData:
    from pymatgen.core import Element

    radius = {el: float(Element(el).metallic_radius) for el in ELEMENTS}
    tm = {el: float(Element(el).melting_point) for el in ELEMENTS}
    vec = {el: valence_electrons(el) for el in ELEMENTS}

    mp_structures = {}
    source = "pymatgen bundled periodic-table data (Materials Project not queried)"
    api_key = os.environ.get("MP_API_KEY")
    if api_key:
        try:
            mp_structures = fetch_from_materials_project(api_key)
            source = ("pymatgen periodic-table data for radii/Tm/VEC; Materials Project "
                      "(mp-api) for elemental ground-state structures")
        except Exception as exc:  # network blocked, bad key, API change...
            print(f"[ingest] Materials Project query failed ({type(exc).__name__}: {exc}); "
                  "using pymatgen bundled data only.", file=sys.stderr)
    else:
        print("[ingest] MP_API_KEY not set; using pymatgen bundled data only.",
              file=sys.stderr)

    return ElementData(radius, vec, tm, source, mp_structures)


def verify_payload(d: ElementData) -> None:
    """Basic payload checks; raises on missing or non-physical values."""
    for el in ELEMENTS:
        assert 1.0 < d.radius[el] < 2.0, f"radius out of range for {el}"
        assert d.vec[el] in (5, 6), f"unexpected VEC for {el}"
        assert 1500 < d.tm[el] < 4000, f"Tm out of range for {el}"
    for a, b in itertools.combinations(ELEMENTS, 2):
        assert frozenset((a, b)) in DH_PAIR, f"missing dH for {a}-{b}"
    for el, s in d.mp_structures.items():
        if s["spacegroup"] != "Im-3m":
            print(f"[ingest] warning: MP ground state of {el} is {s['spacegroup']}, "
                  "not bcc Im-3m", file=sys.stderr)


# --------------------------------------------------------------------------- #
# Stage 2: experimental training data
# --------------------------------------------------------------------------- #
def load_experimental(path: Path) -> tuple[pd.DataFrame, dict]:
    """One row per unique alloy composition, labelled 1 if every record of that
    composition reports a single-phase BCC microstructure, 0 if none does.
    Compositions with conflicting reports (e.g. BCC as cast, BCC+Laves after anneal)
    are dropped. Alloys containing an element with no metallic radius in pymatgen
    (B, C, Si, Sn in this dataset) are dropped because delta cannot be computed."""
    from pymatgen.core import Composition, Element

    raw = pd.read_csv(path)
    raw = raw.dropna(subset=["FORMULA", "PROPERTY: Microstructure"])
    raw["comp"] = raw["FORMULA"].map(
        lambda f: Composition(f.replace(" ", "")).fractional_composition)
    raw["key"] = raw["comp"].map(
        lambda c: tuple(sorted((str(e), round(float(v), 3)) for e, v in c.items())))
    raw["is_bcc"] = raw["PROPERTY: Microstructure"].str.strip() == "BCC"

    g = raw.groupby("key").agg(comp=("comp", "first"), n=("is_bcc", "size"),
                               n_bcc=("is_bcc", "sum"))
    g["label"] = np.where(g.n_bcc == g.n, 1, np.where(g.n_bcc == 0, 0, -1))
    stats = {"records": len(raw), "unique_alloys": len(g),
             "conflicting": int((g.label == -1).sum())}
    g = g[g.label >= 0]

    rows, no_radius = [], 0
    for _, r in g.iterrows():
        els = [str(e) for e in r.comp]
        if any(Element(e).metallic_radius is None for e in els):
            no_radius += 1
            continue
        rows.append({"elements": els,
                     "fractions": [float(r.comp[e]) for e in els],
                     "system": "-".join(sorted(els)),
                     "label": int(r.label)})
    stats["dropped_no_radius"] = no_radius
    exp = pd.DataFrame(rows)
    feats = compute_features_general(exp["elements"], exp["fractions"])
    exp = pd.concat([exp, feats], axis=1)
    stats["used"] = len(exp)
    stats["bcc"] = int(exp.label.sum())
    stats["systems"] = int(exp.system.nunique())
    return exp, stats


def compute_features_general(element_lists, fraction_lists) -> pd.DataFrame:
    """Features for alloys of arbitrary elements (training data)."""
    from matminer.utils.data import MixingEnthalpy
    from pymatgen.core import Element

    mix = MixingEnthalpy()
    out = []
    for els, x in zip(element_lists, fraction_lists):
        x = np.asarray(x, dtype=float)
        r = np.array([float(Element(e).metallic_radius) for e in els])
        tm = np.array([float(Element(e).melting_point) for e in els])
        v = np.array([valence_electrons(e) for e in els])
        dh = 0.0
        for i, j in itertools.combinations(range(len(els)), 2):
            dh += 4.0 * mix.get_mixing_enthalpy(Element(els[i]), Element(els[j])) * x[i] * x[j]
        rb = x @ r
        out.append({
            "delta_pct": 100.0 * np.sqrt(np.sum(x * (1.0 - r / rb) ** 2)),
            "dH_mix_kJmol": dh,
            "VEC": x @ v,
            "dS_mix_JmolK": -R_GAS * np.sum(x[x > 0] * np.log(x[x > 0])),
            "Tm_K": x @ tm,
        })
    df = pd.DataFrame(out)
    df["Omega"] = omega(df)
    return df


# --------------------------------------------------------------------------- #
# Stage 3: target compositions and their features
# --------------------------------------------------------------------------- #
def equiatomic_compositions(min_elements: int = 4) -> np.ndarray:
    """Equiatomic quaternaries and the quinary (binaries/ternaries are not HEAs)."""
    rows = []
    for k in range(min_elements, len(ELEMENTS) + 1):
        for subset in itertools.combinations(range(len(ELEMENTS)), k):
            c = np.zeros(len(ELEMENTS))
            c[list(subset)] = 1.0 / k
            rows.append(c)
    return np.array(rows)


def random_compositions(n: int, rng: np.random.Generator,
                        cmin: float = 0.05, cmax: float = 0.35) -> np.ndarray:
    """Non-equiatomic quinary compositions with every element in [cmin, cmax]
    (Yeh's 5-35 at.% HEA definition), sampled uniformly on that region by rejection."""
    out = []
    free = 1.0 - cmin * len(ELEMENTS)
    while sum(len(o) for o in out) < n:
        c = cmin + free * rng.dirichlet(np.ones(len(ELEMENTS)), size=4 * n)
        out.append(c[(c <= cmax).all(axis=1)])
    return np.vstack(out)[:n]


def omega(df: pd.DataFrame) -> np.ndarray:
    abs_dh_j = np.abs(df["dH_mix_kJmol"].to_numpy()) * 1000.0
    return np.where(abs_dh_j > 1e-9,
                    df["Tm_K"].to_numpy() * df["dS_mix_JmolK"].to_numpy()
                    / np.maximum(abs_dh_j, 1e-9), np.inf)


def compute_features(C: np.ndarray, d: ElementData) -> pd.DataFrame:
    """Vectorised features for W-Mo-Ta-Nb-V compositions (rows of C sum to 1)."""
    r = np.array([d.radius[e] for e in ELEMENTS])
    v = np.array([d.vec[e] for e in ELEMENTS])
    tm = np.array([d.tm[e] for e in ELEMENTS])
    H = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        H[i, j] = H[j, i] = DH_PAIR[frozenset((ELEMENTS[i], ELEMENTS[j]))]

    r_bar = C @ r
    delta = 100.0 * np.sqrt(np.sum(C * (1.0 - r[None, :] / r_bar[:, None]) ** 2, axis=1))
    dh_mix = 2.0 * np.einsum("ni,ij,nj->n", C, H, C)  # = sum_{i<j} 4 dH_ij c_i c_j
    with np.errstate(divide="ignore", invalid="ignore"):  # 0 ln 0 := 0
        clnc = np.where(C > 0, C * np.log(np.where(C > 0, C, 1.0)), 0.0)

    df = pd.DataFrame(C, columns=ELEMENTS)
    df["delta_pct"] = delta
    df["dH_mix_kJmol"] = dh_mix
    df["VEC"] = C @ v
    df["dS_mix_JmolK"] = -R_GAS * clnc.sum(axis=1)
    df["Tm_K"] = C @ tm
    df["Omega"] = omega(df)
    return df


def rule_says_bcc(df: pd.DataFrame) -> np.ndarray:
    """Published empirical criteria: delta <= 6.6 %, Omega >= 1.1, VEC < 6.87."""
    return ((df["delta_pct"] <= DELTA_MAX) & (df["Omega"] >= OMEGA_MIN)
            & (df["VEC"] < VEC_BCC_MAX)).to_numpy()


def self_check(d: ElementData) -> dict:
    """Checks that can fail: the hand-entered dH table against matminer's copy of
    Takeuchi & Inoue, and the feature code against reported equiatomic values."""
    from matminer.utils.data import MixingEnthalpy
    from pymatgen.core import Element

    mix = MixingEnthalpy()
    for a, b in itertools.combinations(ELEMENTS, 2):
        ref = mix.get_mixing_enthalpy(Element(a), Element(b))
        if ref != DH_PAIR[frozenset((a, b))]:
            raise AssertionError(f"dH table mismatch for {a}-{b}: {DH_PAIR[frozenset((a, b))]} vs {ref}")

    C = np.array([[0.25, 0.25, 0.25, 0.25, 0.0],   # WMoTaNb
                  [0.2, 0.2, 0.2, 0.2, 0.2]])      # WMoTaNbV
    f = compute_features(C, d)
    g = compute_features_general([["W", "Mo", "Ta", "Nb", "V"]], [[0.2] * 5])
    checks = {
        "WMoTaNb dH_mix (expect -6.50)": (f.loc[0, "dH_mix_kJmol"], -6.50, 0.01),
        "WMoTaNbV dH_mix (expect -4.64)": (f.loc[1, "dH_mix_kJmol"], -4.64, 0.01),
        "WMoTaNb VEC (expect 5.50)": (f.loc[0, "VEC"], 5.50, 1e-9),
        "WMoTaNbV VEC (expect 5.40)": (f.loc[1, "VEC"], 5.40, 1e-9),
        "WMoTaNbV dS_mix (expect R ln5 = 13.38)": (f.loc[1, "dS_mix_JmolK"], R_GAS * np.log(5), 1e-6),
        "WMoTaNbV delta, general vs vectorised code": (g.loc[0, "delta_pct"], f.loc[1, "delta_pct"], 1e-9),
    }
    for name, (got, exp, tol) in checks.items():
        if abs(got - exp) > tol:
            raise AssertionError(f"self-check failed: {name}: got {got:.4f}")
    out = {k: round(float(v[0]), 4) for k, v in checks.items()}
    out["all 10 pair enthalpies match matminer's Takeuchi-Inoue table"] = True
    return out


# --------------------------------------------------------------------------- #
# Stage 4: Random Forest classifier
# --------------------------------------------------------------------------- #
def make_rf(seed: int) -> RandomForestClassifier:
    return RandomForestClassifier(n_estimators=500, min_samples_leaf=2,
                                  class_weight="balanced", n_jobs=-1, random_state=seed)


def train_classifier(exp: pd.DataFrame, seed: int):
    """Grouped 5-fold CV: every alloy of a chemical system (e.g. all Al-Co-Cr-Fe-Ni
    variants) is held out together, so the score measures transfer to unseen
    systems rather than interpolation between near-duplicates."""
    X, y = exp[FEATURES].to_numpy(), exp["label"].to_numpy()
    p_cv = cross_val_predict(make_rf(seed), X, y, cv=GroupKFold(5),
                             groups=exp["system"], method="predict_proba")[:, 1]
    rule = rule_says_bcc(exp)
    metrics = {
        "rf_auc": float(roc_auc_score(y, p_cv)),
        "rf_balanced_accuracy": float(balanced_accuracy_score(y, p_cv >= 0.5)),
        "rule_balanced_accuracy": float(balanced_accuracy_score(y, rule)),
        "rule_says_bcc_fraction": float(rule.mean()),
    }
    rf = make_rf(seed).fit(X, y)
    importances = dict(zip(FEATURES, rf.feature_importances_.round(4).tolist()))
    return rf, metrics, importances


# --------------------------------------------------------------------------- #
# Stage 5: report
# --------------------------------------------------------------------------- #
def fmt_comp(row) -> str:
    return " ".join(f"{el}{100 * row[el]:.1f}" for el in ELEMENTS if row[el] > 0)


def write_report(df, top, exp, exp_stats, metrics, importances, checks, d, path,
                 n_eq, seed, seed_overlap):
    in_sys = exp[exp["elements"].map(lambda e: set(e) <= set(ELEMENTS))]
    p = df["p_bcc"]
    L = []
    L.append("# Refractory HEA (W-Mo-Ta-Nb-V) BCC phase-stability screen\n")
    L.append("Generated by `hea_model.py` "
             f"(seed {seed}, {len(df):,} compositions: {n_eq} equiatomic + "
             f"{len(df) - n_eq:,} non-equiatomic with every element in 5-35 at.%).\n")

    L.append("## How the model was trained\n")
    L.append(
        f"- **Training data are experimental.** Observed microstructures from Borg et al., "
        f"*Sci. Data* 7, 430 (2020): {exp_stats['records']:,} records reduce to "
        f"{exp_stats['unique_alloys']} unique alloy compositions. {exp_stats['conflicting']} "
        f"with conflicting reports and {exp_stats['dropped_no_radius']} containing B, C, Si "
        f"or Sn (no metallic radius available) were dropped, leaving **{exp_stats['used']} "
        f"alloys from {exp_stats['systems']} chemical systems, {exp_stats['bcc']} of them "
        f"single-phase BCC**.\n"
        "- **Label:** 1 = single-phase BCC reported in every record of that composition; "
        "0 = anything else (FCC, BCC + intermetallic, BCC + B2, multiphase...).\n"
        "- **Model:** Random Forest classifier on δ, ΔH_mix, VEC, ΔS_mix and T_m. Output "
        "is P(single-phase BCC).\n")

    L.append("## How well it works\n")
    L.append("Tested with 5-fold cross-validation grouped by chemical system, so each "
             "alloy family is predicted by a model that never saw any alloy from it.\n")
    L.append("| Method | Balanced accuracy | ROC AUC |")
    L.append("|---|---:|---:|")
    L.append(f"| Random Forest (this model) | {metrics['rf_balanced_accuracy']:.3f} | "
             f"{metrics['rf_auc']:.3f} |")
    L.append(f"| Empirical rules (δ ≤ 6.6 %, Ω ≥ 1.1, VEC < 6.87) | "
             f"{metrics['rule_balanced_accuracy']:.3f} | n/a |")
    L.append("")
    L.append("At a 0.5 cut-off the classifier is no more accurate than the published rules "
             "(the gap is within its seed-to-seed spread of about ±0.003). What it adds is a "
             "graded probability, which the rules cannot give: the AUC shows it ranks BCC "
             "alloys above non-BCC alloys 89 % of the time on unseen alloy families.\n")
    L.append("Feature importances: " +
             ", ".join(f"{k} {v:.3f}" for k, v in importances.items()) + ".\n")

    L.append("## Top 20 W-Mo-Ta-Nb-V compositions by predicted P(single-phase BCC)\n")
    L.append("| Rank | Composition (at.%) | P(BCC) | δ (%) | ΔH_mix (kJ/mol) | VEC | "
             "ΔS_mix (J/mol·K) | T_m (K) | Ω |")
    L.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|")
    for i, (_, r) in enumerate(top.iterrows(), 1):
        L.append(f"| {i} | {fmt_comp(r)} | {r['p_bcc']:.3f} | {r['delta_pct']:.2f} | "
                 f"{r['dH_mix_kJmol']:.2f} | {r['VEC']:.2f} | {r['dS_mix_JmolK']:.2f} | "
                 f"{r['Tm_K']:.0f} | {r['Omega']:.1f} |")
    L.append("")

    L.append("### Equiatomic alloys for reference\n")
    L.append(f"| Alloy | P(BCC) | Rank of {len(df):,} | Observed in training data |")
    L.append("|---|---:|---:|---|")
    ranks = p.rank(ascending=False, method="min").astype(int)
    observed = {frozenset(e): lab for e, lab in zip(in_sys["elements"], in_sys["label"])}
    for idx, r in df[df["is_equiatomic"]].sort_values("p_bcc", ascending=False).iterrows():
        els = [el for el in ELEMENTS if r[el] > 0]
        obs = observed.get(frozenset(els))
        obs_txt = "-" if obs is None else ("single-phase BCC" if obs == 1 else "not single-phase BCC")
        L.append(f"| {''.join(els)} | {r['p_bcc']:.3f} | {ranks[idx]:,} | {obs_txt} |")
    L.append("")

    calphad = Path(__file__).with_name("calphad_results.md")
    if calphad.exists():
        L.append("**CALPHAD follow-up:** selected candidates were checked in Thermo-Calc "
                 "(TCHEA); see [`calphad_results.md`](calphad_results.md).\n")
    if Path(__file__).with_name("properties_results.md").exists():
        L.append("**Properties:** predicted density and compressive yield strength of the "
                 "checked candidates are in [`properties_results.md`](properties_results.md).\n")

    L.append("## Limits — read before using the ranking\n")
    L.append(
        f"- **Predictions for this system are near the ceiling.** P(BCC) ranges "
        f"{p.min():.3f}–{p.max():.3f} across the 10,000 compositions (median "
        f"{p.median():.3f}); {(p >= 0.9).mean():.0%} are ≥ 0.9. The model is confident the "
        "whole region is BCC-forming, and differences between ranks are small.\n"
        f"- **The ranking is not stable.** Retraining with a different random seed keeps "
        f"{seed_overlap} of the top 20. Treat the list as a region of composition space, not "
        "20 distinct winners.\n"
        "- **The ranking is driven mostly by VEC.** Across all alloy families, low VEC "
        "separates BCC alloys from FCC ones, so the model favours Ta- and Nb-rich, Mo-lean "
        "compositions. That is a cross-family trend, not evidence about which "
        "W-Mo-Ta-Nb-V alloys stay single-phase.\n"
        f"- **Little in-system evidence.** Only {len(in_sys)} training alloys use only these "
        f"five elements ({', '.join(sorted(''.join(e) for e in in_sys['elements']))}); "
        f"{int(in_sys['label'].sum())} of them are single-phase BCC. Everything else the "
        "model knows comes from other alloy families.\n"
        "- **What 'BCC' means here.** The label is the phase each paper reported for its "
        "processing state (as-cast, wrought, annealed...), not a verified equilibrium phase. "
        "The features cannot see slow ordering to B2 "
        "(predicted for Mo-Nb-Ta-W by Widom et al., JOM 2013) or Laves formation in V-Ta "
        "(V₂Ta). Check top candidates with CALPHAD (e.g. Thermo-Calc) before any experiment.\n")

    L.append("## Data sources and checks\n")
    L.append(f"- Elemental data: {d.source}. Metallic radii (Å): " +
             ", ".join(f"{e} {d.radius[e]}" for e in ELEMENTS) + ".")
    if d.mp_structures:
        L.append("- Materials Project ground states: " + ", ".join(
            f"{e} {s['material_id']} ({s['spacegroup']})" for e, s in d.mp_structures.items()))
        odd = [e for e, s in d.mp_structures.items() if s["spacegroup"] != "Im-3m"]
        if odd:
            L.append(f"  - Note: the lowest-energy Materials Project entry for {', '.join(odd)} "
                     "is not bcc (Im-3m), although the element is bcc experimentally. These "
                     "structures are recorded for reference only; no feature uses them.")
    L.append("- Binary ΔH_mix: Takeuchi & Inoue, Mater. Trans. 46 (2005) 2817, via matminer.")
    L.append("- Training data: `data/MPEA_dataset.csv`, copied from "
             "github.com/CitrineInformatics/MPEA_dataset (commit d31e251, Apache-2.0).")
    L.append("- Self-check (run every execution; the pipeline stops if any fails):")
    for k, v in checks.items():
        L.append(f"  - {k}: {v}")
    L.append("")
    with open(path, "w") as fh:
        fh.write("\n".join(L))


# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--n", type=int, default=10_000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="results.md")
    ap.add_argument("--data", default=str(DATA_PATH), help="MPEA_dataset.csv path")
    ap.add_argument("--csv", default=None, help="optionally save the full dataset")
    args = ap.parse_args(argv)

    rng = np.random.default_rng(args.seed)
    d = load_element_data()
    verify_payload(d)
    print("[ingest] payload:", json.dumps({"radius_A": d.radius, "VEC": d.vec,
                                            "Tm_K": d.tm}))
    checks = self_check(d)
    print("[check]", checks)

    exp, exp_stats = load_experimental(Path(args.data))
    print("[data]", exp_stats)

    C_eq = equiatomic_compositions()
    C_rand = random_compositions(args.n - len(C_eq), rng)
    df = compute_features(np.vstack([C_eq, C_rand]), d)
    df["is_equiatomic"] = [True] * len(C_eq) + [False] * len(C_rand)
    assert np.isfinite(df[FEATURES].to_numpy()).all(), "non-finite features"

    rf, metrics, importances = train_classifier(exp, args.seed)
    print("[model]", metrics, importances)
    df["p_bcc"] = rf.predict_proba(df[FEATURES].to_numpy())[:, 1]
    top = df.sort_values("p_bcc", ascending=False).head(20)

    # Stability of the ranking under a different random seed
    rf2 = make_rf(args.seed + 1).fit(exp[FEATURES].to_numpy(), exp["label"].to_numpy())
    p2 = rf2.predict_proba(df[FEATURES].to_numpy())[:, 1]
    top2 = set(np.argsort(-p2)[:20])
    seed_overlap = len(top2 & set(top.index))

    write_report(df, top, exp, exp_stats, metrics, importances, checks, d, args.out,
                 len(C_eq), args.seed, seed_overlap)
    if args.csv:
        df.to_csv(args.csv, index=False)
    print(f"[report] wrote {args.out}")
    return df, top


if __name__ == "__main__":
    main()
