# Research brief: run 2026-11-09

Project: computational screening of W-Mo-Ta-Nb-V refractory high-entropy alloys
(repo hea-alloy-property-pipeline). Read `results.md`, `calphad_results.md`,
`calphad_vs_ml.md` and `properties_results.md` for context.

## Questions

- **Q1. Phase stability after long anneals.** What do experiments report for WMoTaNb,
  WMoTaNbV and nearby compositions after long heat treatments (e.g. hundreds of hours at
  600-1400 C)? Any decomposition, B2 ordering, or second BCC phase? Our Thermo-Calc
  (TCHEA) runs predict a second disordered BCC phase below ~664 C for equiatomic
  WMoTaNbV.
- **Q2. CALPHAD vs experiment in this system.** Published comparisons of CALPHAD
  predictions (TCHEA or other databases) with experiment for W-Mo-Ta-Nb-V alloys:
  solidus/liquidus, low-temperature phase separation, ordering.
- **Q3. Non-equiatomic compositions.** Experimental reports on Ta- and Nb-rich,
  Mo-lean W-Mo-Ta-Nb-V alloys (close to W23 Mo7 Ta25.5 Nb25 V19 or W15 Mo15.6 Ta29
  Nb25.7 V14.6): phases, strength, ductility, density.
- **Q4. Machine learning for phase prediction.** Known limits of empirical parameters
  (VEC, delta, mixing enthalpy, Omega) and ML classifiers for predicting phase stability
  within all-BCC refractory systems. Our finding: VEC does not track the CALPHAD split
  temperature within this system.
- **Q5. Strength.** Measured compressive yield strength of WMoTaNb and WMoTaNbV at room
  temperature and 1000-1600 C, and explanations for large scatter between studies (our
  training data list 1246 and 2612 MPa for WMoTaNbV at room temperature).

## Project statements to check

These appear in the repo and were written from memory; the fact-checker must verify them.

- P1. Senkov et al., Intermetallics 18 (2010) 1758: equiatomic WMoTaNb and WMoTaNbV are
  single-phase BCC as cast.
- P2. Widom et al., JOM (2013): first-principles prediction of B2 ordering in Mo-Nb-Ta-W.
- P3. The V-Ta binary has a Laves phase (V2Ta).
- P4. Takeuchi & Inoue, Mater. Trans. 46 (2005) 2817: binary mixing enthalpies
  W-Ta -7, W-Nb -8, Mo-Ta -5, Mo-Nb -6 kJ/mol; W-Mo, Mo-V, Ta-Nb 0; W-V, Ta-V, Nb-V -1.
- P5. Yang & Zhang, Mater. Chem. Phys. 132 (2012) 233: solid-solution criteria
  Omega >= 1.1 and delta <= 6.6 %.
- P6. Guo et al., J. Appl. Phys. 109 (2011) 103505: VEC < 6.87 favours BCC.
- P7. Borg et al., Sci. Data 7, 430 (2020): the MPEA dataset used for training (630
  alloys; observed phases).
