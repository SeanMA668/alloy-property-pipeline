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
- Repo polish: package layout, README with figures, 26 tests, GitHub Actions CI.

## Finalists
| Alloy | Mo | Ta | Nb | V | W | Solidus (°C) | Density (g/cm³) |
|---|---:|---:|---:|---:|---:|---:|---:|
| R5-1 | 21.4 | 28.8 | 8.4 | 6.4 | 35.0 | 2822 | 14.93 |
| R5-2 | 23.8 | 16.6 | 18.9 | 5.7 | 35.0 | 2760 | 13.92 |
| R5-13 | 29.3 | 10.0 | 22.9 | 5.9 | 31.9 | 2707 | 13.12 |
| R5-4 | 17.2 | 24.4 | 35.0 | 12.1 | 11.3 | 2499 | 11.85 |

## Waiting on Sean (Thermo-Calc / Granta)
1. **Yield Strength property model**, Single, 25 °C, for WMoTaNbV, MoNbTaW, NbTaVW, MoNbTaV
   (files `ys_5`, `ys_L1`, `ys_L2`, `ys_L3`). Measured values to compare (MPEA dataset, cast,
   25 °C): 1246, 1058 (996), 1530, 1525 (annealed) MPa. If the model passes, run it for the
   finalists (Batch mode).
2. **Rerun L3 (MoNbTaV, no W, Mo balance)** from 2000 to 3000 °C: the sweep stopped at
   2276 °C before melting, so its solidus is missing.
3. **Scheil for T6** (cheapest single-phase alloy): mole %, Mo 26.9, Ta 5.5, Nb 30.2,
   V 5.2, W balance (32.2); save as `hea_T6_scheil.csv/.png`, °C axis.
4. **Granta EduPack table**: density, melting point, yield strength for W, Mo, Ta, Nb, TZM,
   C-103, Ta-10W, Inconel 718, a single-crystal Ni superalloy (e.g. CMSX-4).
5. Later: **set D** (one round with W and Ta allowed up to ~45 %; generate with
   `study_design.py` after raising the cap) and **set C** (composition tolerance, try the
   Property Model "Uncertainty" type on one finalist first). Phase Diagram isopleth through
   R5-1 (V from 0 to 30 %) for a poster figure.

## Still to do (Claude, no Thermo-Calc needed)
- Verify the V price and Nb/V producer shares against the USGS chapter PDFs (read from
  secondary summaries; see `reports/cost_supply.md`, Limits).
- Decide whether T6 should join the finalists now that cost is an objective (after its
  Scheil run, item 3 above).
- Optional: lattice parameters/elastic constants from an ML interatomic potential feeding a
  published physics-based strength model.
- Browser dashboard (GitHub Pages, greys out compositions far from data), Ashby chart with
  Granta data, final report, poster in Figma, resume bullets.

## Thermo-Calc rules that caused errors before
- **Mole percent and Celsius** every time; the Property Model Calculator defaults to Mass
  percent and Kelvin (round 2 was entered in mass % by mistake).
- Thermo-Calc's composition fields are in the order **Mo, Ta, Nb, V, with W as balance**.
  Give tables in that order (round 3 was shifted one element over).
- Sweep 500–3000 °C; export CSV + PNG with the axis in °C; name files `hea_<ID>.csv/.png`
  (Scheil: `hea_<ID>_scheil`). Plots for #1–#5, T1–T9, R2-*m may still have kelvin axes.
- No HEA mobility database (MOBHEA), so Homogenization/Diffusion cannot be used.
- Never commit the Materials Project API key; pass it only as `MP_API_KEY`.

## Branches
- `main`: merged through PR #7 (ml-depth).
- `cost-sensitivity`: sensitivity report, cost and supply-risk objectives (PR open).
