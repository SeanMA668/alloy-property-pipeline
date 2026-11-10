# Thermo-Calc study of W-Mo-Ta-Nb-V alloys: results

50 alloys with complete equilibrium sweeps (500–3000 °C) computed in Thermo-Calc with the TCHEA6 (v6.1) database, summarised by `study_results.py`. All values are calculated, not measured.

## Headline numbers

- **28 of 50** alloys are single-phase BCC from 500 °C up to the solidus; the rest split into two BCC phases below 925 °C. This fraction reflects how alloys were chosen (later rounds targeted single-phase regions), not how common single-phase alloys are in the system.
- Highest solidus of a single-phase alloy: **2822 °C** (R5-1).
- Lowest density of a single-phase alloy: **11.42 g/cm³** (R2-5m).
- Surrogate accuracy (Gaussian process, leave-one-out over all 50): solidus mean abs. error **10 °C** (ρ 0.99); split temperature **26 °C** (ρ 0.85). Guessing the mean would give 154 and 113 °C.

## Best trade-offs: melting point vs density

Single-phase alloys that no other single-phase alloy beats on both solidus (higher) and density (lower). Moving down the table trades melting point for lower density. Mole percent.

| Alloy | Composition (at.%) | Solidus (°C) | Density (g/cm³) | YS 1000 °C, est. (MPa) |
|---|---|---:|---:|---:|
| R5-1 | W35.0 Mo21.4 Ta28.8 Nb8.4 V6.4 | 2822 | 14.93 | 574 |
| R5-10 | W34.4 Mo17.4 Ta24.7 Nb16.7 V6.8 | 2774 | 14.40 | 633 |
| R5-2 | W35.0 Mo23.8 Ta16.6 Nb18.9 V5.7 | 2760 | 13.92 | 574 |
| R5-11 | W34.8 Mo18.3 Ta15.4 Nb26.2 V5.3 | 2742 | 13.66 | 573 |
| R5-9 | W28.0 Mo12.6 Ta23.0 Nb31.3 V5.1 | 2719 | 13.46 | 574 |
| R5-13 | W31.9 Mo29.3 Ta10.0 Nb22.9 V5.9 | 2707 | 13.12 | 574 |
| T6 | W32.2 Mo26.9 Ta5.5 Nb30.2 V5.2 | 2688 | 12.70 | 572 |
| R2-2 | W20.9 Mo17.8 Ta21.9 Nb30.9 V8.5 | 2614 | 12.70 | 763 |
| R2-3 | W6.7 Mo15.7 Ta34.9 Nb31.0 V11.7 | 2529 | 12.24 | 721 |
| R5-4 | W11.3 Mo17.2 Ta24.4 Nb35.0 V12.1 | 2499 | 11.85 | 795 |
| R2-5m | W21.5 Mo7.9 Ta10.4 Nb40.8 V19.4 | 2371 | 11.42 | 720 |

## Ten highest-melting single-phase alloys

| Alloy | Composition (at.%) | Solidus (°C) | Density (g/cm³) | YS 1000 °C, est. (MPa) |
|---|---|---:|---:|---:|
| R5-1 | W35.0 Mo21.4 Ta28.8 Nb8.4 V6.4 | 2822 | 14.93 | 574 |
| R5-10 | W34.4 Mo17.4 Ta24.7 Nb16.7 V6.8 | 2774 | 14.40 | 633 |
| R5-6 | W32.0 Mo11.5 Ta32.5 Nb15.4 V8.6 | 2765 | 14.67 | 704 |
| R5-2 | W35.0 Mo23.8 Ta16.6 Nb18.9 V5.7 | 2760 | 13.92 | 574 |
| R5-11 | W34.8 Mo18.3 Ta15.4 Nb26.2 V5.3 | 2742 | 13.66 | 573 |
| R5-5 | W25.6 Mo21.8 Ta34.8 Nb8.7 V9.1 | 2742 | 14.42 | 704 |
| R5-8 | W25.6 Mo23.5 Ta26.9 Nb18.4 V5.6 | 2739 | 13.79 | 633 |
| R5-9 | W28.0 Mo12.6 Ta23.0 Nb31.3 V5.1 | 2719 | 13.46 | 574 |
| R5-13 | W31.9 Mo29.3 Ta10.0 Nb22.9 V5.9 | 2707 | 13.12 | 574 |
| R5-12 | W25.4 Mo10.5 Ta33.6 Nb21.6 V8.9 | 2705 | 14.02 | 706 |

## What the study shows

- Within this system, high solidus and single-phase stability go together with low V and higher W and Ta: single-phase alloys average 9.6 % V, 16.5 % Mo, 25.2 % W and 24.6 % Ta, against 23.1, 23.1, 16.0 and 16.0 % for the alloys that split (at 545–925 °C). This is a pattern in these calculations, not a tested rule.
- The Gaussian-process surrogate trained only on Thermo-Calc results predicts new alloys within a few tens of °C; the cross-family ML classifier (trained on experimental data from many systems) ranks alloys within this system only weakly (see `calphad_vs_ml.md`).

## Limits

- **Equilibrium calculations only.** TCHEA6 predictions for these compositions have not been checked against experiments here; real alloys may contain phases or segregation that equilibrium does not show (see the Scheil results in `calphad_results.md`).
- **Strength is a rough estimate.** The yield-strength column comes from a model whose error on unseen alloy families is about 200 MPa (`properties_results.md`); differences smaller than that are not meaningful.
- **Density** is a rule-of-mixtures estimate (median error 0.3 % on measured alloys).
- **Not assessed:** ductility, oxidation resistance, creep, processability.
- Ten alloys (R2-*m, R3-*) were calculated at compositions other than planned because of input errors; they are included at the compositions actually calculated (`calphad_extra_points.csv`, `calphad_round3_points.csv`).

Full table: `data/calphad/study_results.csv`.
