# CALPHAD check of W-Mo-Ta-Nb-V candidates (Thermo-Calc, TCHEA)

Equilibrium phase amounts from 500 to 3000 °C, computed by the user in Thermo-Calc Graphical Mode (TCHEA database) and summarised from the exported tables in `data/calphad/` by `calphad_summary.py`.

| # | Alloy (at.%) | Role | Solidus (°C) | Liquidus (°C) | Lowest T computed (°C) | Second solid phase | Verdict |
|---:|---|---|---:|---:|---:|---|---|
| 1 | W23.1 Mo7.1 Ta25.5 Nb25.2 V19.1 | top ML pick | 2474 | 2707 | 500 | none | single BCC from solidus to lowest computed T |
| 2 | W20.5 Mo11.6 Ta13.1 Nb34.1 V20.7 | Nb-rich, ML top 20 | 2377 | 2601 | 500 | second BCC (A2) below 573 °C (31 % at 500 °C) | single BCC at high T; second BCC at low T |
| 3 | W15.1 Mo15.6 Ta29.0 Nb25.7 V14.6 | Ta-rich, ML top 20 | 2521 | 2691 | 500 | none | single BCC from solidus to lowest computed T |
| 4 | W27.6 Mo30.1 Ta5.4 Nb5.8 V31.1 | old rule-score pick | 2417 | 2647 | 500 | second BCC (A2) below 842 °C (44 % at 500 °C) | single BCC at high T; second BCC at low T |
| 5 | W20 Mo20 Ta20 Nb20 V20 | control, equiatomic | 2457 | 2665 | 500 | second BCC (A2) below 664 °C (28 % at 500 °C) | single BCC at high T; second BCC at low T |

## Reading

- Every phase Thermo-Calc reported is BCC labelled [A2] (disordered) or LIQUID. No B2 ordering and no Laves or other intermetallic appeared in any run.
- The equiatomic control splits into two disordered BCC phases below about 664 °C. Experiments report it single-phase BCC as cast (Senkov et al. 2010); at such low temperatures diffusion is slow, so the split may not occur in practice.
- The ML-favoured Ta/Nb-rich alloys (#1, #3) are the only ones that stay single-phase down to 500 °C. The old rule-score pick (#4, W-Mo-V-rich) has the widest split: below about 842 °C it separates into two BCC phases of roughly equal amount.
- A sweep that stopped early (no solution below the listed temperature) leaves the low-temperature behaviour of that alloy unknown, not single-phase.
- These are equilibrium calculations with one database. They screen candidates; they do not replace making and characterising the alloy.

Phase columns found per file: #1: BCC_B2, LIQUID; #2: BCC_B2, BCC_B2#2, LIQUID; #3: BCC_B2, LIQUID; #4: BCC_B2, BCC_B2#2, LIQUID; #5: BCC_B2, BCC_B2#2, LIQUID.
