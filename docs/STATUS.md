# Project status and handoff (2026-11-11)

Read this first when resuming work in a new session. Repo:
`SeanMA668/hea-alloy-property-pipeline`; see `README.md` for what the project is.

## Done
- **Study:** 50 alloys calculated in Thermo-Calc 2026a (TCHEA6 v6.1), 28 single-phase BCC
  from 500 °C to melting; summary in `reports/study_results.md`.
- **Surrogate:** Gaussian processes on composition (`pipeline/active_learning.py`);
  leave-one-out solidus error 10 °C, split temperature 26 °C.
- **Search benchmark** (`reports/search_benchmark.md`): on a Thermo-Calc-trained stand-in,
  model-guided search finds the best alloy in 8–10 calculations; random search needs ~550.
- **Validation** (`reports/finalists.md`): Thermo-Calc agrees with experiments for all four
  W-Mo-Ta-Nb-V alloys with reported phases (MoNbTaW, NbTaVW, MoNbTaV, WMoTaNbV).
- **Scheil:** finalists freeze over 623–732 °C (Scheil) vs 785–844 °C for earlier candidates.
- **Sensitivity** (`reports/sensitivity.md`): +1 at.% (taken proportionally from the
  others) changes solidus by W +8, Ta +5, Mo 0, Nb −4, V −18 °C (28 single-phase alloys)
  and split temperature by V +9, Mo +8, Nb −4, W −7, Ta −8 °C (22 alloys that split above
  500 °C). Supersedes the first-pass numbers, which used a different perturbation.
- **Cost and supply risk** (`reports/cost_supply.md`): USGS MCS 2026 prices (2025 avg) and
  EU CRM 2023 supply-risk scores. Finalists cost $71–108/kg raw material at 2025 prices;
  with W at the Oct 2026 APT price, $160–239/kg and R5-4 becomes the cheapest. T6
  ($60/kg, 2688 °C, 12.70 g/cm³) is the cheapest single-phase alloy and on the
  solidus/density/cost trade-off front.
- **Strength model check** (`reports/finalists.md` §3): Thermo-Calc's Yield Strength model
  (Simplified, 1400 °C, solid-solution only) fails validation: rank order vs the four
  measured alloys is wrong (ρ = −0.20); NbTaVW predicted 787 vs 1530 MPa measured; the
  others are 209–445 MPa high. Finalists span only 1528–1691 MPa, so it cannot rank them.
- **Research run 2026-11-11** (4 agents, SIGN-OFF: PASS): MoNbTaV validation data is
  as-cast, not annealed; all checked strengths are as-cast, so the 1400 °C anneal input
  matches none; EU criticality needs SR ≥ 1.0 and EI ≥ 2.8; Nb and V prices verified.
- **T6 Scheil:** 600 °C range, narrowest of all; liquid + BCC only. **L3** solidus 2281 °C,
  liquidus 2463 °C. **Isopleth through R5-1** (`data/calphad/hea_R5-1_isopleth.png`):
  single-phase to 500 °C up to ~11 % V (W balance); solidus at 6.4 % V matches the sweep.
- Repo polish: package layout, README with figures, 27 tests, GitHub Actions CI.

## Finalists
| Alloy | Mo | Ta | Nb | V | W | Solidus (°C) | Density (g/cm³) |
|---|---:|---:|---:|---:|---:|---:|---:|
| R5-1 | 21.4 | 28.8 | 8.4 | 6.4 | 35.0 | 2822 | 14.93 |
| R5-2 | 23.8 | 16.6 | 18.9 | 5.7 | 35.0 | 2760 | 13.92 |
| R5-13 | 29.3 | 10.0 | 22.9 | 5.9 | 31.9 | 2707 | 13.12 |
| R5-4 | 17.2 | 24.4 | 35.0 | 12.1 | 11.3 | 2499 | 11.85 |

## Waiting on Sean (Thermo-Calc / Granta)
1. **Granta EduPack table** (Level 3 or Aerospace): density, melting point/solidus, room-T
   yield strength, max service temperature, price, for W, Mo, Ta, Nb, TZM, C-103, Ta-10W,
   Inconel 718, CMSX-4. Export Table view to CSV/Excel.
2. Optional: confirm `ys_L2` (NbTaVW) had solid-solution strengthening ticked; if it was
   off, rerun. The conclusion holds either way (the other three already vary by 236 MPa).
3. Later: **set D** (one round with W and Ta allowed up to ~45 %; generate with
   `study_design.py` after raising the cap) and **set C** (composition tolerance, try the
   Property Model "Uncertainty" type on R5-1 first).

## Still to do (Claude, no Thermo-Calc needed)
- Find the full text of Yao et al., MSEA 674 (doi:10.1016/j.msea.2016.07.102) to verify
  NbTaVW 1530 MPa; the largest strength-model error rests on it.
- Next research run leads (`docs/research/run-2026-11-11/audit.md`): USGS Niobium
  footnote may cite the 65 % Nb ferroniobium grade; check the W and Mo USGS figures.
- Decide whether T6 joins the finalists (cheapest, narrowest Scheil range, solidus 2688 °C).
- Optional: lattice parameters/elastic constants from an ML interatomic potential feeding a
  published physics-based strength model.
- Browser dashboard (GitHub Pages, greys out compositions far from data), Ashby chart with
  Granta data, final report, poster in Figma, resume bullets.

## Thermo-Calc rules that caused errors before
- **Mole percent and Celsius** every time; the Property Model Calculator defaults to Mass
  percent and Kelvin (round 2 was entered in mass % by mistake).
- Thermo-Calc's composition fields are in the order **Mo, Ta, Nb, V, with W as balance**.
  Give tables in that order (round 3 was shifted one element over).
- The **Property Model Calculator uses Mo as balance**, with fields W, Ta, Nb, V. Type the W
  value in the W box and check the greyed Mo value (the first finalist YS runs had W and Mo
  swapped).
- Sweep 500–3000 °C; export CSV + PNG with the axis in °C; name files `hea_<ID>.csv/.png`
  (Scheil: `hea_<ID>_scheil`). Plots for #1–#5, T1–T9, R2-*m may still have kelvin axes.
- No HEA mobility database (MOBHEA), so Homogenization/Diffusion cannot be used.
- Never commit the Materials Project API key; pass it only as `MP_API_KEY`.

## Branches
- `main`: merged through PR #10 (README).
- `research-run-2026-11-11`: research run 2 and its corrections (PR #11 open).
