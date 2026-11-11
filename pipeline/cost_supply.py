#!/usr/bin/env python3
"""
cost_supply.py - Raw-material cost and supply-risk objectives for the 50 calculated alloys.

Every number below is dated and sourced. Prices are for the traded raw material (ore
concentrate, oxide or ferroalloy), converted to US$ per kg of contained element. They are
NOT prices of the high-purity metals an alloy would be melted from, which cost several
times more; use the result as a raw-material index to compare alloys, not as a part cost.

Per alloy (mole % -> mass fractions):
  cost_2025      $/kg alloy at 2025 annual-average prices (USGS MCS 2026)
  cost_W2026     same, with W at the October 2026 European APT price (2026 export-control spike)
  cost_per_L     cost_2025 x density: cost of a fixed volume, the fairer basis for a part
  sr_eu          mass-weighted EU supply-risk score (EU CRM study 2023). A raw material is
                 critical only if SR >= 1.0 AND economic importance EI >= 2.8; the rule
                 applies to raw materials, not to alloys.
  w_cost_share   fraction of cost_2025 coming from tungsten

Writes data/calphad/cost_supply.csv and reports/cost_supply.md.
Usage: python -m pipeline.cost_supply
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pipeline import paths as P
from pipeline.composition import mole_to_mass

ELS = ["W", "Mo", "Ta", "Nb", "V"]

# Molar masses used only for oxide -> element conversions (g/mol).
_M = {"Ta": 180.948, "V": 50.942, "O": 15.999}
TA_IN_TA2O5 = 2 * _M["Ta"] / (2 * _M["Ta"] + 5 * _M["O"])   # 0.819
V_IN_V2O5 = 2 * _M["V"] / (2 * _M["V"] + 5 * _M["O"])       # 0.560
KG_W_PER_MTU = 7.93          # 1 metric ton unit of WO3 = 10 kg WO3 = 7.93 kg W (USGS)
NB_IN_FENB = 0.65            # ASSUMPTION: standard ferroniobium grade (~65 % Nb)
LB_PER_KG = 2.20462

USGS = "USGS Mineral Commodity Summaries 2026 (Feb 2026), doi:10.3133/mcs2026"
EU = ("European Commission, Study on the Critical Raw Materials for the EU 2023, "
      "Final Report (Grohol & Veeh), assessment-results table")

# element: (price $/kg element, how it was derived, source)
PRICE_2025 = {
    "W":  (380 / KG_W_PER_MTU,
           "$380 per mtu WO3, concentrate, Rotterdam, 2025 avg (est.); ÷ 7.93 kg W/mtu",
           f"{USGS}, Tungsten"),
    "Mo": (51.0,
           "$51/kg, U.S. molybdic oxide (57 % Mo), 2025 avg; taken as per kg Mo contained",
           f"{USGS}, Molybdenum"),
    "Ta": (180 / TA_IN_TA2O5,
           "$180/kg Ta2O5 in tantalite, 2025 avg (est.); ÷ 0.819 kg Ta per kg Ta2O5",
           f"{USGS}, Tantalum"),
    "Nb": (26 / NB_IN_FENB,
           "$26/kg ferroniobium (gross weight), 2025 unit value; ÷ 0.65 Nb (assumed grade)",
           f"{USGS}, Niobium"),
    "V":  (5.02 * LB_PER_KG / (0.98 * V_IN_V2O5),
           "$5.02/lb V2O5 (98 %), China, 2025 avg (est.); ÷ (0.98 × 0.560 kg V per kg V2O5)",
           f"{USGS}, Vanadium"),
}
# Scenario: tungsten during the 2026 Chinese export controls.
W_2026 = (278.22 / (KG_W_PER_MTU / 10),
          "$278.22/kg, APT, Rotterdam warehouse, October 2026; the source does not state the "
          "basis, assumed per kg WO3 (≈ $2,782 per mtu); ÷ 0.793",
          "MetalMiner study reported in Canadian Mining Journal, 'Western tungsten prices "
          "nearly quadruple China's' (2026; data through October 2026)")

# element: (EU 2023 supply risk SR, largest producer and share of 2025 world mine output)
SUPPLY = {
    "W":  (1.2, "China 79 % (67 of 85 kt)"),
    "Mo": (0.8, "China 37 % (97 of 260 kt)"),
    "Ta": (1.3, "Congo (Kinshasa) 52 % (1.3 of 2.5 kt)"),
    "Nb": (4.4, "Brazil ~93 % (104 of 112 kt)"),
    "V":  (2.3, "China ~75 % (82 of 110 kt)"),
}
# EU 2023 economic importance EI (same study, assessment-results table)
EI = {"W": 8.7, "Mo": 6.7, "Ta": 4.8, "Nb": 6.5, "V": 3.9}
# EU rule: a raw material is critical if SR >= 1.0 AND EI >= 2.8.
SR_THRESHOLD, EI_THRESHOLD = 1.0, 2.8


def prices(w_price: float | None = None) -> np.ndarray:
    p = np.array([PRICE_2025[e][0] for e in ELS])
    if w_price is not None:
        p[ELS.index("W")] = w_price
    return p


def alloy_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add cost and supply-risk columns to a table with W, Mo, Ta, Nb, V in mole %."""
    wt = mole_to_mass(df[ELS].to_numpy(float), ELS)          # mass fractions
    p25, p26 = prices(), prices(W_2026[0])
    sr = np.array([SUPPLY[e][0] for e in ELS])
    out = df.copy()
    out["cost_2025"] = wt @ p25
    out["cost_W2026"] = wt @ p26
    out["w_cost_share"] = wt[:, 0] * p25[0] / out["cost_2025"]
    out["sr_eu"] = wt @ sr
    if "density_gcc" in out:
        out["cost_per_L"] = out["cost_2025"] * out["density_gcc"]   # $/kg × kg/L
    return out


def pareto(df: pd.DataFrame, maximise: list[str], minimise: list[str]) -> np.ndarray:
    """Boolean mask of rows not dominated on the given objectives."""
    V = np.hstack([-df[maximise].to_numpy(float), df[minimise].to_numpy(float)])
    keep = np.ones(len(V), bool)
    for i in range(len(V)):
        dom = (V <= V[i]).all(axis=1) & (V < V[i]).any(axis=1)
        keep[i] = not dom.any()
    return keep


FINALISTS = ["R5-1", "R5-2", "R5-13", "R5-4"]


def main():
    d = alloy_metrics(pd.read_csv(P.CALPHAD / "study_results.csv"))
    sp = d[d["single_phase_500C"]].copy()
    sp["pareto3"] = pareto(sp, ["solidus_C"], ["density_gcc", "cost_2025"])
    d = d.merge(sp[["alloy", "pareto3"]], on="alloy", how="left")
    cols = ["alloy", *ELS, "solidus_C", "density_gcc", "single_phase_500C", "cost_2025",
            "cost_W2026", "cost_per_L", "w_cost_share", "sr_eu", "pareto3"]
    d[cols].to_csv(P.CALPHAD / "cost_supply.csv", index=False)

    eq = alloy_metrics(pd.DataFrame([{e: 20.0 for e in ELS}]))
    fin = d.set_index("alloy").loc[FINALISTS]
    lo, hi = sp["cost_2025"].min(), sp["cost_2025"].max()
    r26 = sp["cost_W2026"] / sp["cost_2025"]

    L = ["# Cost and supply risk\n",
         "Raw-material cost and supply-risk scores for the 50 calculated alloys. Generated by "
         "`pipeline/cost_supply.py`; per-alloy values in `data/calphad/cost_supply.csv`.\n",
         "**Read this first.** Prices are for traded raw materials (concentrate, oxide or "
         "ferroalloy), converted to $ per kg of contained element. High-purity metal for "
         "arc melting costs several times more, and the mark-up differs by element. So these "
         "numbers rank alloys by the cost of what is in them; they are not the price of a "
         "part.\n",
         "## Inputs\n",
         "| Element | $/kg element (2025) | Derived from | EU supply risk (2023) | EU economic importance | Largest producer, 2025 |",
         "|---|---:|---|---:|---:|---|"]
    for e in ELS:
        L.append(f"| {e} | {PRICE_2025[e][0]:.0f} | {PRICE_2025[e][1]} | {SUPPLY[e][0]:.1f} | "
                 f"{EI[e]:.1f} | {SUPPLY[e][1]} |")
    L += ["",
          f"Tungsten scenario: {W_2026[1]} → **${W_2026[0]:.0f}/kg W**, "
          f"{W_2026[0] / PRICE_2025['W'][0]:.1f}× the 2025 figure. This is a refined "
          "intermediate rather than concentrate, so it overstates the like-for-like change "
          "somewhat, but it is the price a European buyer faced in late 2026.\n",
          f"EU rule: a raw material is critical if its supply risk is at least {SR_THRESHOLD:.1f} "
          f"**and** its economic importance at least {EI_THRESHOLD:.1f}. W, Ta, Nb and V meet "
          "both; Mo (SR 0.8) does not qualify. The score reflects risk to EU supply; it is "
          "used here as a general, citable indicator.\n",
          "## Finalists\n",
          "| Alloy | Solidus (°C) | Density (g/cm³) | $/kg (2025) | $/kg (W at Oct 2026) | "
          "$/L (2025) | W share of cost | EU supply risk |",
          "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for a, r in fin.iterrows():
        L.append(f"| {a} | {r['solidus_C']:.0f} | {r['density_gcc']:.2f} | {r['cost_2025']:.0f} | "
                 f"{r['cost_W2026']:.0f} | {r['cost_per_L']:.0f} | {100 * r['w_cost_share']:.0f} % | "
                 f"{r['sr_eu']:.2f} |")
    e0 = eq.iloc[0]
    L.append(f"| *equiatomic WMoTaNbV* | – | – | {e0['cost_2025']:.0f} | {e0['cost_W2026']:.0f} | – | "
             f"{100 * e0['w_cost_share']:.0f} % | {e0['sr_eu']:.2f} |")

    cheapest = sp.loc[sp["cost_2025"].idxmin()]
    r_ta = float(np.corrcoef(sp["cost_2025"], sp["Ta"])[0, 1])
    f25, f26, fL = fin["cost_2025"], fin["cost_W2026"], fin["cost_per_L"]
    L += ["",
          "## What it shows\n",
          f"- **Tantalum sets the cost at 2025 prices.** At ${PRICE_2025['Ta'][0]:.0f}/kg it is "
          f"{PRICE_2025['Ta'][0] / PRICE_2025['Mo'][0]:.0f}–{PRICE_2025['Ta'][0] / PRICE_2025['V'][0]:.0f}× "
          f"the other elements. Across the single-phase alloys (${lo:.0f}–{hi:.0f}/kg), Ta content "
          f"alone explains {100 * r_ta ** 2:.0f} % of the variation in cost. R5-13 (10 % Ta) is "
          f"the cheapest finalist (${f25['R5-13']:.0f}/kg); R5-1 and R5-4 (24–29 % Ta) are the "
          f"most expensive (${f25['R5-1']:.0f}/kg).",
          f"- **The 2026 tungsten spike reverses the order.** With W at the October 2026 price, "
          f"single-phase alloys cost {r26.min():.1f}–{r26.max():.1f}× more. The three W-rich "
          f"finalists (32–35 % W) rise to ${f26[['R5-1', 'R5-2', 'R5-13']].min():.0f}–"
          f"{f26[['R5-1', 'R5-2', 'R5-13']].max():.0f}/kg, while R5-4 (11 % W) rises only to "
          f"${f26['R5-4']:.0f}/kg and becomes the cheapest finalist. No finalist is cheapest "
          "under both price sets.",
          f"- **Supply risk is driven by Nb and V.** Nb has the highest EU score (4.4; about "
          f"93 % of mine output is Brazilian) and V the second (2.3). R5-4, the lightest "
          f"finalist, is also the most Nb-rich and has the highest score of the four "
          f"({fin['sr_eu'].max():.2f}); R5-1 has the lowest ({fin['sr_eu'].min():.2f}). The "
          f"mass-weighted scores of the 50 alloys span {d['sr_eu'].min():.2f}–"
          f"{d['sr_eu'].max():.2f}. The EU threshold applies to raw materials, not alloys; "
          "what matters is that every one of the 50 alloys contains W, Ta, Nb and V, all "
          "EU-critical, so no composition in this family avoids critical raw materials.",
          f"- **Per volume the spread widens.** Dense W-Ta alloys cost more per kg *and* need "
          f"more kg for the same part: the finalists differ {f25.max() / f25.min():.2f}× per kg "
          f"but {fL.max() / fL.min():.2f}× per litre. Use $/L for a fixed component size.",
          f"- **A cost-oriented candidate outside the finalists:** {cheapest['alloy']} "
          f"(W{cheapest['W']:.1f} Mo{cheapest['Mo']:.1f} Ta{cheapest['Ta']:.1f} "
          f"Nb{cheapest['Nb']:.1f} V{cheapest['V']:.1f}) is the cheapest single-phase alloy "
          f"(${cheapest['cost_2025']:.0f}/kg) with a {cheapest['solidus_C']:.0f} °C solidus and "
          f"{cheapest['density_gcc']:.2f} g/cm³, close to R5-13 on both. Its cost depends heavily "
          f"on tungsten ({100 * cheapest['w_cost_share']:.0f} % of its 2025 cost), so it shares "
          "the W price exposure.",
          "",
          "## Trade-off among the 28 single-phase alloys\n",
          "Alloys not beaten on all three of solidus (higher), density (lower) and 2025 "
          "raw-material cost (lower):\n",
          "| Alloy | Solidus (°C) | Density (g/cm³) | $/kg (2025) | Ta (at.%) | Finalist? |",
          "|---|---:|---:|---:|---:|---|"]
    for _, r in sp[sp["pareto3"]].sort_values("solidus_C", ascending=False).iterrows():
        L.append(f"| {r['alloy']} | {r['solidus_C']:.0f} | {r['density_gcc']:.2f} | "
                 f"{r['cost_2025']:.0f} | {r['Ta']:.1f} | {'yes' if r['alloy'] in FINALISTS else ''} |")
    L += ["",
          f"{int((~sp.loc[sp['pareto3'], 'alloy'].isin(FINALISTS)).sum())} of these "
          f"{int(sp['pareto3'].sum())} are not finalists: the finalists were chosen before cost "
          "was an objective. Adding cost mainly promotes low-Ta alloys such as T6 and R5-11.\n",
          "## Limits\n",
          "- One year of prices. Tungsten moved several-fold within 2026, and Ta and V prices "
          "have swung by tens of percent in past years (USGS five-year tables), so treat any "
          "ranking that depends on a few dollars per kg as unsettled.",
          "- The Nb price assumes a 65 % Nb ferroniobium grade; the Mo price is taken as per "
          "kg of contained Mo. Both are stated in the code so they can be changed.",
          "- No processing cost. Melting, homogenising and machining a refractory alloy usually "
          "cost more than its raw material; that is not modelled here.",
          "- The Nb and V prices and producer shares were checked against the USGS chapters "
          "in research run 2026-11-11. The W, Mo and Ta figures were read from the USGS "
          "chapters by the project; of these, only the Ta price was re-checked in that run "
          "(`docs/research/run-2026-11-11`).\n",
          "## Sources\n",
          f"- {USGS}: chapters Tungsten, Molybdenum, Tantalum, Niobium (Columbium), Vanadium. "
          "https://pubs.usgs.gov/periodicals/mcs2026/",
          f"- {W_2026[2]}.",
          f"- {EU}. https://ec.europa.eu/docsroom/documents/54114\n"]
    text = "\n".join(L)
    (P.REPORTS / "cost_supply.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
