# Research brief: run 2026-11-13

Project: computational screening of W-Mo-Ta-Nb-V refractory high-entropy alloys
(repo hea-alloy-property-pipeline). This run checks the new physics-based strength model.
Read `reports/strength_model.md`, `pipeline/strength_model.py` and `reports/finalists.md`
for context. Earlier runs (`run-2026-11-09/`, `run-2026-11-11/`) are already done; reuse
their findings where relevant (e.g. run-2026-11-11 C1, C3 on Maresca-Curtin) and do not
repeat them except where a question below needs it.

Google Scholar (scholar.google.com) may be used for searching, alongside other sources.

## Questions

- **Q1. The reduced Maresca-Curtin model as implemented.** Check the equations and
  constants in `pipeline/strength_model.py` against Maresca & Curtin, Acta Mater. 182
  (2020) 235-249 (doi:10.1016/j.actamat.2019.10.015; arXiv:1901.02100): the prefactors
  0.040 and 2.00, the line-tension coefficient α = 1/12, the reference strain rate
  10^4 s^-1, the Taylor factor 3.067, the low/high-temperature forms and the switch at
  τ_y/τ_y0 = 0.5, the rule-of-mixtures recipe for μ and ν, and Vegard's-law misfit
  volumes. Have later papers by the same group (or others applying the reduced model)
  changed any constant (e.g. a different α), the elastic-constant recipe, or the
  switching rule? Do they report room-temperature predictions for MoNbTaW, WMoTaNbV,
  NbTaVW or MoNbTaV that we can compare with our 922, 1411, 1425 and 1317 MPa?
- **Q2. Elemental inputs.** Room-temperature BCC lattice parameters and single-crystal
  elastic constants (C11, C12, C44) of W, Mo, Ta, Nb and V from primary or standard
  handbook sources (e.g. Simmons & Wang; Featherston & Neighbours; Bolef; Katahara et al.).
  Compare with the values in `pipeline/strength_model.py` (`LATTICE_A`, `ELASTIC`).
- **Q3. Validation data.** Verify NbTaVW room-temperature compressive yield strength
  1530 MPa against its primary source (Yao et al., Mater. Sci. Eng. A 674 (2016),
  doi:10.1016/j.msea.2016.07.102): value, processing state, test method, strain rate.
  If the full text cannot be opened, say exactly what is missing.
- **Q4. High temperature and limits.** How do predictions of the Maresca-Curtin edge
  model (full or reduced) compare with measured yield strength of MoNbTaW and WMoTaNbV at
  1000-1600 °C? Does the literature say whether edge or screw dislocations control strength
  at room temperature in these alloys, and what that means for room-temperature
  predictions from the edge model?

## Project statements to check

- P1. `reports/strength_model.md`: "The paper reports its predictions fall below
  experiment at high temperature (the 900–1300 K plateau is not reproduced)."
- P2. `reports/strength_model.md`: "DFT gives a much lower C44 for equiatomic MoNbTaVW"
  (Table 2 of the paper, DFT row: a = 3.192 Å, C11 338, C12 164, C44 51 GPa; DFT misfit
  volumes Mo -0.824, Nb 1.848, Ta 1.882, V -2.380, W -0.526 Å^3), as used in
  `tests/test_strength_model.py`.
- P3. `tests/test_strength_model.py`: the paper reports energy barriers of 2.2-2.5 eV for
  MoNbTaW / MoNbTaVW.
- P4. `README.md`: "V has the largest misfit volume of the five elements" (via
  run-2026-11-11 notes).

## Paywalled sources

If a source that matters cannot be opened, list it in a final section "Needs Sean
(university access)" with full citation, DOI, the exact table/figure/value needed, and
whether it is IMPERATIVE (a project number or conclusion depends on it and no open source
covers it) or OPTIONAL. Only IMPERATIVE items will be requested.
