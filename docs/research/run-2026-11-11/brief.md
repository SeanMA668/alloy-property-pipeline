# Research brief: run 2026-11-11

Project: computational screening of W-Mo-Ta-Nb-V refractory high-entropy alloys
(repo hea-alloy-property-pipeline). Read `reports/finalists.md`, `reports/cost_supply.md`,
`reports/sensitivity.md` and `reports/study_results.md` for context. The previous run
(`run-2026-11-09/`) covered phase stability, CALPHAD vs experiment, Ta/Nb-rich
compositions, ML limits and strength scatter; do not repeat it except where a question
below needs it.

## Questions

- **Q1. Strength models for this family.** How accurate are published models of
  solid-solution strengthening for refractory BCC high-entropy alloys (e.g. Maresca-Curtin
  edge-dislocation model, Labusch/Varvenne-type models, Thermo-Calc's Yield Strength
  property model) against measured yield strength of W-Mo-Ta-Nb-V alloys? Our Thermo-Calc
  run (Simplified mode, solid solution only) predicted NbTaVW at 787 MPa against 1530 MPa
  measured, and overestimated WMoTaNbV, MoNbTaW and MoNbTaV by 209-445 MPa. Is there a
  published explanation for why V-containing alloys such as NbTaVW are so strong?
- **Q2. Casting segregation and homogenisation.** What do experiments report on dendritic
  segregation in as-cast W-Mo-Ta-Nb-V alloys (which elements enrich dendrite cores vs
  interdendritic regions) and on the time and temperature needed to homogenise them? Our
  Scheil calculations predict freezing ranges of 600-844 C.
- **Q3. Effect of vanadium.** Experimental or computational reports on how V content
  changes phase stability, melting point, strength, ductility and density in W-Mo-Ta-Nb-V
  alloys. Our surrogate finds +1 at.% V lowers the solidus by 18 C and raises the
  two-BCC split temperature by 9 C.
- **Q4. Cost and critical raw materials in alloy design.** Published uses of raw-material
  cost or supply-risk metrics in high-entropy or refractory alloy design, and how the
  price of high-purity metal (arc-melting grade) compares with concentrate/oxide/ferroalloy
  prices for W, Mo, Ta, Nb and V.
- **Q5. Comparison with existing refractory alloys.** Published comparisons of refractory
  high-entropy alloys with TZM, C-103, Ta-10W and Ni-based superalloys (e.g. Inconel 718,
  CMSX-4) on density, melting point and high-temperature yield strength, to frame the
  planned Ashby chart.

## Project statements to check

These are in the repo; the fact-checker must verify them against the primary sources.

- P1. USGS Mineral Commodity Summaries 2026, Vanadium: China V2O5 (98 %) average price
  $5.02/lb in 2025; China about 82 kt of about 110 kt world mine production in 2025.
- P2. USGS Mineral Commodity Summaries 2026, Niobium: ferroniobium unit value $26/kg in
  2025; Brazil about 104 kt, about 93 % of world mine production in 2025.
- P3. European Commission, Study on the Critical Raw Materials for the EU 2023: supply
  risk W 1.2, Mo 0.8, Ta 1.3, Nb 4.4, V 2.3; criticality threshold SR >= 1.0.
- P4. Measured room-temperature compressive yield strengths used for validation:
  MoNbTaW 1058 MPa and WMoTaNbV 1246 MPa (Senkov et al., Intermetallics 19 (2011) 698,
  doi:10.1016/j.intermet.2011.01.004); NbTaVW 1530 MPa (doi:10.1016/j.msea.2016.07.102);
  MoNbTaV 1525 MPa, annealed (doi:10.3390/e18050189).
- P5. Senkov et al. homogenised cast WMoTaNb and WMoTaNbV at 1400 C (the reason the
  Thermo-Calc yield-strength runs used a 1400 C annealing temperature).
- P6. Canadian Mining Journal / MetalMiner (2026): Rotterdam APT $278.22/kg in October
  2026.
