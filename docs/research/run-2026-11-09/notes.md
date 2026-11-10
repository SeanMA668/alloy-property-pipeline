# Research notes: run 2026-11-09

Literature notes produced by AI agents (reviewer, fact-checker, note-writer, integrity auditor). Not peer review.

Tags [C#] and [P#] refer to `claims.md` and `factcheck.md`. PARTIAL claims (C28, C29, C41, P1-P3) appear in the fact-checker's corrected wording.

## Summary

In one study, WMoTaNb and WMoTaNbV were single-phase BCC as cast and after an 18-19 h anneal at 1400 °C [C1]. The only long low-temperature anneal found (5 weeks at 500 °C) was on V-free MoNbTaW [C3]; none was found for WMoTaNbV, for which our Thermo-Calc runs predict a second BCC phase below about 664 °C (calphad_results.md). Simulations predict chemical ordering [C4-C6], not TCHEA's split into two disordered BCC phases. No checked source compares CALPHAD phase-stability predictions (solidus/liquidus, phase separation, ordering) with experiment for these alloys, and none reports our Ta/Nb-rich, Mo-lean candidates. The VEC rule was built to separate FCC from BCC [P6], consistent with our finding that VEC does not track the split temperature (calphad_vs_ml.md). The 1246 and 2612 MPa strengths come from two different processing routes [C35, C37].

Terms: **A2** is disordered BCC (calphad_results.md). **Scheil** calculations assume no diffusion in the solid during freezing, giving worst-case segregation (coring) in a casting (calphad_results.md).

## Q1. Phase stability after long anneals

**Literature.** Arc-melted WMoTaNb and WMoTaNbV were single-phase disordered BCC by neutron diffraction both as cast and after annealing at 1400 °C, with an anneal time given as 18 or 19 h in different parts of the paper [C1]. MoNbTaW homogenised at 1800 °C for 4 days and then aged at 500 °C for 5 weeks showed only BCC in synchrotron XRD, with no superlattice peaks [C3]. MoNbTaVW films stayed BCC up to 1500 °C [C8]. In other refractory HEA families, 100 h anneals caused decomposition starting near 500 °C [C10].

Simulations predict ordering instead. For MoNbTaW, an A2 to B2 transition is predicted at 1280 K (Monte Carlo) or 1654 K (mean field), driven by Mo-Ta bonding [C5]; an EAM-based study puts a chemical ordering transition (B2-type Mo-Ta ordering) near 700 K [C4]. For VNbMoTaW, a first-principles analysis finds a V-dominated B32-like instability at 742 K (559 K, B2-like, for NbMoTaW), likely overestimates [C6]; the authors judge the simulated low-temperature multiphase state unlikely to be seen experimentally, while short-range order may be observable after suitable heat treatment [C7].

**Comparison with our results.** TCHEA predicts that equiatomic WMoTaNbV splits into two disordered BCC phases below about 664 °C (28 % second phase at 500 °C), and reports no B2 or intermetallic in any run (calphad_results.md). The 1400 °C anneals are above our split temperature, and the 500 °C aging was on the V-free quaternary, so neither tests it.

**Next step.** A long 500-650 °C anneal of equiatomic WMoTaNbV, checked for both superlattice peaks and a second BCC phase, would test both predictions.

## Q2. CALPHAD vs experiment in this system

**Literature.** TCHEA3 fully assessed 294 binaries and 136 ternaries, about 5 % of the possible ternaries [C12]. Gorsse and Senkov conclude that extrapolating from binaries alone is acceptable only where there are no binary miscibility gaps and few intermetallics; their tests were on non-refractory systems at 800 °C [C13]. A Pandat-based screen made no experimental comparison for NbMoTaW or NbMoTaVW and notes that no higher-order alloy had full ternary assessment [C14]. With TCHEA v2.1, liquidus values were 3138 K (MoNbTaW) and 2976 K (MoNbTaWV), close to rule-of-mixtures estimates; no measured liquidus existed for comparison [C16]. Scheil calculations with TCHEA4 matched the observed casting segregation in NbTaTiW and MoNbTaTi [C18]. As-cast WMoTaNb and WMoTaNbV had dendritic structures with segregation, dendrite arms about 20-30 µm thick [C19].

**Comparison with our results.** Our TCHEA liquidus for equiatomic WMoTaNbV is 2665 °C (calphad_results.md), versus 2976 K (about 2703 °C) with v2.1 [C16]. Our Scheil freezing ranges of 844 and 803 °C for #1 and #3 (calphad_results.md) predict strong coring; the observed dendritic segregation [C19] is in the equiatomic alloys, not in #1 or #3, so it does not test these predictions.

**Next step.** Record our TCHEA version; treat the split as an untested database extrapolation.

## Q3. Non-equiatomic compositions

**Literature.** In thin-film libraries spanning non-equiatomic VNbMoTaW compositions, a single BCC phase formed with comparable hardness, and replacing Mo with Nb was the most effective way to raise ductility [C23]. DFT screening of 70 compositions found Mo and W raise moduli and V raises ductility indicators [C24]. As-cast NbTaTiVW was single BCC with 1420 MPa yield strength and 20 % fracture strain [C25].

**Comparison with our results.** Our Mo-lean candidates #1 and #3 have rule-of-mixtures densities of 12.90 and 12.58 g/cm³ versus 12.36 g/cm³ for the equiatomic control by the same calculation (properties_results.md); none of these is a measurement. The thin-film Nb-for-Mo result [C23] does not test our compositions.

**Next step.** Making #1 or #3 is the only direct test.

## Q4. Machine learning for phase prediction

**Literature.** The VEC < 6.87 rule for BCC was derived from Al-containing 3d-metal alloys and separates FCC from BCC [P6]. In a 2436-alloy dataset of 3d-metal quinaries, VEC was the most important feature and BCC and B2 were lumped into one class [C27]. Its ANN scored 81.8 % on 66 external alloys versus 89.1 % in cross-validation [C28]. A classifier for Al-containing refractory HEAs predicted single-BCC test alloys correctly but misclassified three multi-phase ones, blamed on scarce mixed-phase training data [C29]. Ordering in NbMoTaW depends on specific pair preferences, and in VNbMoTaW on second-neighbour V-W pairs [C30].

**Comparison with our results.** VEC has the largest importance in our classifier (0.385; results.md) but ρ = +0.01 with the TCHEA split temperature, and the classifier reaches only ρ = -0.43 (p = 0.12) (calphad_vs_ml.md). This fits a rule built for cross-family FCC/BCC separation [P6, C27]. A model fitted to 14 TCHEA results reproduces the TCHEA split temperature with leave-one-out ρ = 0.82 (active_learning.md); this is agreement with CALPHAD, not with experiment.

**Next step.** Continue the in-system active-learning loop (active_learning.md).

## Q5. Strength

**Literature.** Arc-melted WMoTaNb annealed at 1400 °C yielded at 1058 MPa at 23 °C and 548 MPa at 1000 °C [C34]. WMoTaNbV yielded at 1246 MPa at 23 °C, 842 MPa at 1000 °C and 477 MPa at 1600 °C [C35]. WNbMoTaV made by mechanical alloying and spark plasma sintering reached 2612 MPa with 8.8 % failure strain, with oxide inclusions in a fine-grained BCC matrix [C37]; the authors credit grain-boundary, solid-solution and oxide (Orowan) strengthening [C38]. A parameter-free solute-strengthening theory matches room-temperature strengths but underpredicts at high temperature [C40]; its authors list O and N impurities, dendritic microstructure (158 MPa stronger dendrites in MoNbTaV) and about 50 MPa of Hall-Petch strengthening for 80-200 µm grains as factors that can raise measured strength above the intrinsic prediction [C41].

**Comparison with our results.** In our held-out check (properties_results.md), the measured WMoTaNbV values at 23-1600 °C and the WMoTaNb values at 600-1600 °C match the arc-melted series [C34, C35]; the WMoTaNb room-temperature entries (996 MPa at 23 °C; 996, 1058, 1217 MPa at 25 °C) include values not from that series. The 1246 and 2612 MPa room-temperature entries are two processing routes [C35, C37], not repeat tests of one material; the model predicted 1379 MPa for both (properties_results.md).

**Next step.** Add processing route as a feature, or restrict strength training to arc-melted material.

## Corrections to the project

- **P1** (calphad_results.md cites "Senkov et al. 2010"). Corrected: Senkov et al., Intermetallics 18 (2010) 1758-1765: near-equiatomic W-Nb-Mo-Ta and W-Nb-Mo-Ta-V (arc-melted, as cast) are single-phase BCC. Measured density of the as-cast near-equiatomic quaternary was 13.75 g/cm³.
- **P2** (results.md, "Widom et al., JOM 2013"). Corrected: Huhn & Widom, "Prediction of A2 to B2 phase transition in the high-entropy alloy Mo-Nb-Ta-W", JOM 65 (2013) 1772-1779, DOI 10.1007/s11837-013-0772-3.
- **P3** (results.md, "Laves formation in V-Ta (V₂Ta)"). Corrected: the Ta-V binary has a Laves phase (C15 at intermediate temperatures, C14 at high temperatures; Pavlů et al., Calphad 35 (2011) 103); the V2Ta stoichiometry is not verified.
- **P5** (results.md, δ ≤ 6.6 %, Ω ≥ 1.1). UNREACHABLE: original not read; a citing source agrees. Mark unverified.
- **Density of MoNbTaW.** 13.64 g/cm³ is our rule-of-mixtures value and 13.60 g/cm³ is the measured value recorded in our training data (properties_results.md, "13.64 vs 13.60"; the dataset row cites DOI 10.1016/j.actamat.2019.06.032, not opened). 13.75 g/cm³ is the value Senkov et al. 2010 measured for their near-equiatomic as-cast alloy [P1]. Shaikh et al. list 13.64 as experimental [C17], apparently swapped with the rule-of-mixtures value (factcheck.md, C17); do not cite 13.64 as measured.

## Open leads (not verified)

- C11: A2+A2 splitting below 1000 °C in Hf-Nb-Ta-Ti-V-Zr (analogue of the TCHEA split).
- C21: a third-generation Mo-Nb-Ta-W database (A2 + B2 only at very low T).
- C22, C31, C32, C33: CALPHAD vs empirical parameters; limits of δ, Ω and VEC.
- C26: VxNbMoTa single BCC down to 350 °C.

## Open questions

- Any bulk WMoTaNbV annealed for hundreds of hours at 500-700 °C?
- Which TCHEA version did we use, and are the W-Mo-Ta-Nb-V ternaries assessed?
- Sources of the 996 and 1217 MPa WMoTaNb values (properties_results.md)?
- Does Borg et al.'s 630 [P7] count entries or compositions?

## References

- Senkov, Wilks, Scott, Miracle, Intermetallics 19 (2011) 698-706, DOI 10.1016/j.intermet.2011.01.004 (read as preprint https://apps.dtic.mil/sti/pdfs/ADA550865.pdf). [C1, C19, C34, C35]
- Senkov, Wilks, Miracle, Chuang, Liaw, Intermetallics 18 (2010) 1758-1765 (read as DTIC preprint ADA550824). [P1]
- Bajpai et al., arXiv:2103.07951, https://arxiv.org/pdf/2103.07951. [C3, C4]
- Huhn, Widom, JOM 65 (2013) 1772-1779, DOI 10.1007/s11837-013-0772-3; arXiv:1306.5043. [C5, P2]
- Woodgate, Staunton, Phys. Rev. Materials 7, 013801 (2023), DOI 10.1103/PhysRevMaterials.7.013801; arXiv:2211.09911. [C6, C7, C30]
- Xia, Franz, Coatings 10 (2020) 941, DOI 10.3390/coatings10100941. [C8]
- Dai et al., J. Mater. Sci. Technol. 122 (2022) 243-254, DOI 10.1016/j.jmst.2021.12.057. [C10]
- Gorsse, Senkov, Entropy 20 (2018) 899, DOI 10.3390/e20120899. [C12, C13]
- Senkov, Miller, Miracle, Woodward, CALPHAD 50 (2015) 32-48, DOI 10.1016/j.calphad.2015.04.009. [C14]
- Shaikh et al., Intermetallics 127 (2020) 106926, https://home.iitm.ac.in/satyesh/papers/2020-calphad.pdf. [C16]
- Puerling et al., report NSC-614-4990 (2023), https://www.osti.gov/servlets/purl/1989196. [C18]
- Yao et al., Mater. Sci. Eng. A 674 (2016) 203-211, DOI 10.1016/j.msea.2016.07.102. [C25]
- Tuhser et al., J. Mater. Res. Technol. 35 (2025), DOI 10.1016/j.jmrt.2025.02.011. [C23]
- Zheng, Wang, Entropy 20 (2018) 965, DOI 10.3390/e20120965. [C24]
- Wang, Zhong, Zhao, J. Alloys Compd. 915 (2022) 165173, DOI 10.1016/j.jallcom.2022.165173. [C27, C28]
- Sreenidhi Iyengar et al., arXiv:2503.21146, https://arxiv.org/pdf/2503.21146. [C29]
- Kang et al., Mater. Sci. Eng. A 712 (2018) 616-624, DOI 10.1016/j.msea.2017.12.021. [C37, C38]
- Maresca, Curtin, arXiv:1901.02100, https://arxiv.org/pdf/1901.02100. [C40, C41]
- Guo, Ng, Lu, Liu, J. Appl. Phys. 109 (2011) 103505, https://core.ac.uk/download/61022332.pdf. [P6]
- Pavlů et al., Calphad 35 (2011) 103-108, DOI 10.1016/j.calphad.2010.12.002. [P3]
- Borg et al., Sci. Data 7 (2020) 430, DOI 10.1038/s41597-020-00768-9. [P7]
