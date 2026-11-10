# Claims: run 2026-11-09 (literature-reviewer)

Written by the literature-reviewer agent, 2026-11-09. Each claim records how its source
was read. Pages were opened with WebFetch, which returns a model-extracted reading of the
page, not the raw text. "read-directly" means the relevant passage of the full text (or
full preprint) was in what loaded. `search-summary` claims are leads, not findings: they
come only from a search-engine or Consensus abstract snippet.

Bibliographic note (disagreement between sources): the AFRL preprint of Senkov, Wilks,
Scott & Miracle (DTIC ADA550865) says it was submitted to *J. Alloys Compd.*, but
Maresca & Curtin (arXiv:1901.02100) cite the same data as Intermetallics 19, 698-706
(2011). I did not open the published Intermetallics version. Numbers below are from the
preprint.

---

## Q1. Phase stability after long anneals

### C1
Claim: Equiatomic Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 were single-phase disordered BCC by neutron diffraction, both as cast and after annealing at 1400 C.
Answers: Q1 (also bears on P1)
Access: read-directly
Source: O.N. Senkov, G.B. Wilks, J.M. Scott, D.B. Miracle, "Mechanical Properties of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 Refractory High-Entropy Alloys", AFRL-RX-WP-TP-2011-4289 (preprint, July 2011), https://apps.dtic.mil/sti/pdfs/ADA550865.pdf
Where: Abstract; Section 3.2.1 (neutron diffraction, NIST BT1)
Evidence: BCC structure "remained stable after exposure to 1400 °C"
Not claimed: anneals of hundreds of hours; anything below 1400 C; anything about P1's 2010 paper itself. The anneal time is given as 19 h in Section 2 and 18 h in Section 3.2.1 / Fig. 4, so the preprint is inconsistent. No diffraction is shown after the 1600 C tests.

### C2
Claim: The lattice parameter did not change measurably on annealing: 3.220 A for NbMoTaW (as cast and annealed), and 3.185 A as cast vs 3.187 A annealed for VNbMoTaW.
Answers: Q1
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C1)
Where: Section 3.2.1
Evidence: a = 3.185 Å as-cast; a = 3.187 Å annealed (VNbMoTaW)
Not claimed: that no nanoscale decomposition or short-range order occurred; diffraction resolution not assessed.

### C3
Claim: Equiatomic MoNbTaW homogenised at 1800 C for 4 days, and samples then aged at 500 C (773 K) for 5 weeks, showed only a BCC average structure in synchrotron XRD, with no superlattice reflections.
Answers: Q1
Access: read-directly
Source: V. Bajpai, S. Maiti, S. Mishra, B. Rai, "Temperature dependent phase stability of Mo-Nb-Ta-W refractory high-entropy alloys", arXiv:2103.07951 (2021, preprint; journal not stated on the page), https://arxiv.org/pdf/2103.07951
Where: Section 2 (Experiments); Section 4.3 (Structure Evaluation)
Evidence: "no superlattice Bragg reflections peak observed"
Not claimed: anything about V-containing alloys; whether order forms below 773 K (the aging temperature is above the simulated ~700 K transition, so the experiment does not test it directly).

### C4
Claim: EAM-based hybrid MC/MD simulations of MoNbTaW put the chemical ordering transition near 700 K, with B2-type next-neighbour ordering of Mo-Ta pairs and clustering tendency of Nb-W.
Answers: Q1
Access: read-directly
Source: Bajpai et al., arXiv:2103.07951 (as C3)
Where: Abstract; Section 4.2
Evidence: "The ordering transition temperature is close to 700 K"
Not claimed: macroscopic phase separation (not predicted); experimental confirmation below 773 K.

### C5
Claim: First-principles-based modelling of MoNbTaW predicts an A2 to B2 order-disorder transition at 1280 K (Monte Carlo) or 1654 K (mean field), driven by strong Mo-Ta bonding, with further low-temperature transitions likely ending in segregation into binary phases.
Answers: Q1 (also bears on P2)
Access: read-directly
Source: W.P. Huhn, M. Widom, "Prediction of A2 to B2 Phase Transition in the High Entropy Alloy MoNbTaW", arXiv:1306.5043v1 (21 June 2013), PDF via figshare: https://figshare.com/articles/journal_contribution/Prediction_of_A2_to_B2_Phase_Transition_in_the_High_Entropy_Alloy_MoNbTaW/6507926/1/files/11972051.pdf
Where: Abstract; Section V; Section III (zero-K phases MoTa.oA12, NbW.cF16, TaW2.tI6, Mo3Nb4.hR7)
Evidence: "Our Monte Carlo simulations predict TC = 1280K"
Not claimed: experimental observation of B2; the published journal version (the preprint names no journal, so the JOM 2013 venue in P2 was not checked here); anything about V.

### C6
Claim: A first-principles linear-response (concentration-wave) analysis gives a chemical-ordering instability at 742 K for VNbMoTaW, of B32-like type dominated by V, and at 559 K for NbMoTaW, of B2-like type; the authors call these mean-field values likely overestimates.
Answers: Q1
Access: read-directly
Source: C.D. Woodgate, J.B. Staunton, "Short-range order and compositional phase stability in refractory high-entropy alloys via first-principles theory and atomistic modeling: NbMoTa, NbMoTaW, and VNbMoTaW", Physical Review Materials (2022) (venue and year from the Consensus record); arXiv:2211.09911v2, https://arxiv.org/pdf/2211.09911v2
Where: Table II; Section III.B
Evidence: VNbMoTaW T_us = 742 K, B32-like, k = {1/2,1/2,1/2}
Not claimed: a disordered-BCC miscibility gap of the kind TCHEA predicts (this is an ordering instability, not an A2+A2 split); experimental confirmation.

### C7
Claim: Monte Carlo simulations with the fitted pair model show multiphase behaviour in VNbMoTaW at low temperature (B32-like V-W regions plus B2-like patches), which the authors judge unlikely to be seen experimentally, while short-range order may be observable after suitable heat treatment.
Answers: Q1
Access: read-directly
Source: Woodgate & Staunton, arXiv:2211.09911v2 (as C6)
Where: Section III.D, Figs. 4-5; Section IV
Evidence: "is unlikely to be experimentally observable"
Not claimed: a transition temperature for the multiphase state; a V-rich disordered BCC phase (not described explicitly).

### C8
Claim: Cathodic-arc MoNbTaVW thin films kept their BCC solid-solution phase on vacuum annealing up to 1500 C.
Answers: Q1
Access: abstract-only
Source: A. Xia, R. Franz, "Thermal stability of MoNbTaVW high entropy alloy thin films", Coatings 10(10), 941 (2020), DOI 10.3390/coatings10100941 (abstract via https://pure.unileoben.ac.at/en/publications/thermal-stability-of-monbtavw-high-entropy-alloy-thin-films/)
Where: Abstract
Evidence: BCC phase "is stable up to 1500 ◦ C"
Not claimed: anneal durations; bulk behaviour; behaviour at 600-700 C over long times; what happens above 1500 C.

### C9
Claim: TiNbMoTaW kept a single BCC structure after annealing at 1200 C for 24 h.
Answers: Q1
Access: search-summary
Source: Z.D. Han et al., "Effect of Ti additions on mechanical properties of NbMoTaW and VNbMoTaW refractory high entropy alloys", Intermetallics 84 (2017) 153-157, DOI 10.1016/j.intermet.2017.01.007 (statement from Consensus abstract snippet; the XJTU abstract page I opened gave the bibliography)
Where: Abstract (snippet)
Evidence: single BCC "even after annealing at 1200 °C for 24 h" (snippet)
Not claimed: Ti-free alloys; long anneals.

### C10
Claim: In other BCC refractory HEAs (HfNbTaTiZr, NbTaTiZr, HfNbTiZr, NbTiZr), 100 h anneals at intermediate temperatures caused decomposition into multiple phases starting near 500 C, with re-entry into the single-phase field at 900 to above 1300 C depending on alloy.
Answers: Q1 (analogue system, not W-Mo-Ta-Nb-V)
Access: search-summary
Source: P. Cao et al., "Microstructural stability and aging behavior of refractory high entropy alloys at intermediate temperatures", J. Mater. Sci. Technol. (2022) (Consensus record)
Where: Abstract (snippet)
Evidence: "start to decompose into multiple phases at around 500 °C" (snippet)
Not claimed: anything about W-Mo-Ta-Nb-V; included only as a lead showing that long anneals have revealed low-T decomposition in other RHEA families.

### C11
Claim: In Hf-Nb-Ta-Ti-V-Zr alloys the single BCC solid solution is reported stable only above 1000 C, separating at lower temperature into disordered BCC phases of slightly different composition, while rapid cooling retains a metastable single phase.
Answers: Q1 (analogue system)
Access: search-summary
Source: T. Vlasák et al., "Thermal Stability of Microstructure of High-Entropy Alloys Based on Refractory Metals Hf, Nb, Ta, Ti, V, and Zr", Metals (2022) (Consensus record)
Where: Abstract (snippet)
Evidence: "phase separation into disordered bcc phases" (snippet)
Not claimed: anything about W-Mo-Ta-Nb-V; included as an experimental example of an A2+A2 split of the kind TCHEA predicts here.

**Q1 status: partly answered.** Bulk experiments that loaded cover short anneals only (1400 C, 18-19 h, WMoTaNb and WMoTaNbV; 1800 C 4 days plus 500 C 5 weeks, WMoTaNb only), and none showed a second phase or superlattice peaks. I found no bulk WMoTaNbV anneal of hundreds of hours at 600-1400 C among the sources that loaded. Computations predict B2-type (WMoTaNb) or B32-type (WMoTaNbV) ordering below about 560-1650 K depending on method; none of the opened sources predicts or observes a disordered A2+A2 split for WMoTaNbV.

---

## Q2. CALPHAD vs experiment in this system

### C12
Claim: Thermo-Calc's TCHEA3 database had 294 binary and 136 ternary systems assessed over the full composition and temperature range, which the authors put at about 5 % of the possible ternaries.
Answers: Q2
Access: read-directly
Source: S. Gorsse, O.N. Senkov, "About the Reliability of CALPHAD Predictions in Multicomponent Systems", Entropy 20(12), 899 (2018), DOI 10.3390/e20120899, https://pmc.ncbi.nlm.nih.gov/articles/PMC7512484
Where: Introduction; Section 2; Conclusions
Evidence: fully assessed ternaries "about 5%"
Not claimed: which W-Mo-Ta-Nb-V ternaries are assessed in TCHEA (not stated); anything about TCHEA versions later than 3.

### C13
Claim: Gorsse and Senkov conclude that extrapolating from binaries alone is acceptable only where there are no binary miscibility gaps and few or no intermetallics, and that results from lower-credibility databases may be questionable; their test systems were not refractory and all calculations were at 800 C.
Answers: Q2
Access: read-directly
Source: Gorsse & Senkov, Entropy 20, 899 (2018) (as C12)
Where: Section 4; Conclusions; Section 3
Evidence: "lower credibility databases may be questionable"
Not claimed: any test on W, Mo, Ta, Nb or V systems or on low-temperature miscibility gaps.

### C14
Claim: A high-throughput CALPHAD screen of equiatomic multi-principal-element alloys (Pandat 2013 databases) did not compare its predictions with experiment for NbMoTaW, NbMoTaVW or other W-containing refractory alloys, and notes that no higher-order alloy had full ternary assessment.
Answers: Q2
Access: read-directly
Source: O.N. Senkov, J.D. Miller, D.B. Miracle, C. Woodward, "Accelerated exploration of multi-principal element alloys for structural applications", CALPHAD 50 (2015) 32-48, AFRL-RX-WP-JA-2015-0202, https://apps.dtic.mil/sti/pdfs/ADA627998.pdf
Where: Section 2.2.1; Section 3.1.3; Section 4.1
Evidence: "none of the higher order alloys have full ternary assessment"
Not claimed: anything about TCHEA. Validation counts are inconsistent in the paper (65 alloys in Section 2.2.1, "over 50" in Section 4.1).

### C15
Claim: In the same screen, the PanSol database predicted a BCC + BCC mixture at 600 C for equiatomic AlCrMoNbVW.
Answers: Q2
Access: read-directly
Source: Senkov et al., CALPHAD 50 (2015) (as C14)
Where: Table 15
Evidence: AlCrMoNbVW: Tm 1915 °C; BCC + BCC at 600 °C
Not claimed: experimental confirmation; relevance to the Al- and Cr-free W-Mo-Ta-Nb-V system beyond showing that low-T BCC splits appear in CALPHAD output for V-bearing refractory alloys.

### C16
Claim: With TCHEA v2.1, the computed liquidus is 3138 K for MoNbTaW and 2976 K for MoNbTaWV, close to rule-of-mixtures melting points of 3158 K and 2963 K.
Answers: Q2
Access: read-directly
Source: S.M. Shaikh, V.S. Hariharan, S.K. Yadav, B.S. Murty, "CALPHAD and rule-of-mixtures: A comparative study for refractory high entropy alloys", Intermetallics 127, 106926 (2020), https://home.iitm.ac.in/satyesh/papers/2020-calphad.pdf
Where: Section 3.1
Evidence: MoNbTaWV MP-ROM = 2963 K, MP-TC = 2976 K
Not claimed: comparison with a measured solidus or liquidus (none is given); solidus values (not reported).

### C17
Claim: The same study lists measured densities of 13.64 g/cm3 (MoNbTaW) and 12.36 g/cm3 (MoNbTaWV), against TCHEA values of 13.8 and 12.44 g/cm3.
Answers: Q2 (also Q3 density context)
Access: read-directly
Source: Shaikh et al., Intermetallics 127, 106926 (2020) (as C16)
Where: Table 2
Evidence: MoNbTaWV experimental 12.36, ROM 12.36, CALPHAD 12.44 g/cm³
Not claimed: the original source of the experimental values (cited as their ref. [9], not opened).

### C18
Claim: For equimolar NbTaTiW and MoNbTaTi, Scheil calculations with TCHEA4 predicted the observed solidification segregation accurately, and DICTRA (MOBHEA2) captured general homogenisation trends at 1673 K.
Answers: Q2 (analogue alloys)
Access: read-directly
Source: R. Puerling, A. Miklas, F.G. Coury, N.R. Philips, P. Mason, N.E. Peterson, A. Deal, J. Klemm-Toole, A.J. Clarke, "Thermodynamics and Kinetics of Refractory Multi-Principal Element Alloys: An Experimental and Modeling Comparison", report NSC-614-4990 (01/2023), https://www.osti.gov/servlets/purl/1989196
Where: Abstract
Evidence: "Scheil calculations accurately predict the observed solidification segregation"
Not claimed: anything about V-containing alloys, solidus values, or low-temperature phase separation.

### C19
Claim: As-cast WMoTaNb and WMoTaNbV showed dendritic microstructures with uneven Z-contrast from constitutional segregation, dendrite arms about 20-30 um thick.
Answers: Q2 (bears on Scheil coring prediction); Q1
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C1)
Where: Section 3.2.2, Figure 5
Evidence: dendrite arm thickness about 20-30 µm
Not claimed: measured compositions of dendrite cores vs interdendrites; comparison with any CALPHAD calculation.

### C20
Claim: In NbTaTiV and NbTaTiVW, the observed elemental segregation qualitatively matched CALPHAD predictions.
Answers: Q2
Access: abstract-only
Source: H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang, "NbTaV-(Ti,W) refractory high-entropy alloys: Experiments and modeling", Mater. Sci. Eng. A 674 (2016) 203-211, DOI 10.1016/j.msea.2016.07.102
Where: Abstract
Evidence: segregation "qualitatively" matches CALPHAD (paraphrase of abstract)
Not claimed: database used; any quantitative comparison; Mo-containing alloys.

### C21
Claim: A third-generation CALPHAD database for Mo-Nb-Ta-W reportedly predicts a wide single-A2 field, with A2 + B2 regions only at very low temperatures, and was checked against an as-cast equiatomic MoNbTaW.
Answers: Q2
Access: search-summary
Source: E. Zhang et al., "On phase stability of Mo-Nb-Ta-W refractory high entropy alloys", Int. J. Refract. Met. Hard Mater. (2022) (Consensus record; paper not opened)
Where: Abstract (snippet)
Evidence: "A2 + B2 phase regions exist at very low temperatures" (snippet)
Not claimed: transition temperatures; V; agreement with TCHEA.

### C22
Claim: A refractory-HEA design study reports CALPHAD as more effective than empirical parameters at predicting HEA formation, with segregation in two as-cast alloys qualitatively matching CALPHAD.
Answers: Q2, Q4
Access: search-summary
Source: M.C. Gao et al., "Design of Refractory High-Entropy Alloys", JOM (2015) (Consensus record; not opened)
Where: Abstract (snippet)
Evidence: CALPHAD "is more effective in predicting HEA formation than empirical parameters" (snippet)
Not claimed: W-Mo-Ta-Nb-V-specific comparisons (the verified alloys were HfMoNbTaTiVZr and HfMoNbTaTiVWZr).

**Q2 status: partly answered.** Among the sources that loaded, I found no direct comparison of CALPHAD (TCHEA or another database) with a measured solidus/liquidus, low-temperature phase separation, or ordering for WMoTaNb or WMoTaNbV. What loaded: database-coverage limits (C12-C14), TCHEA liquidus vs rule of mixtures (C16), and Scheil segregation validated on analogue alloys (C18, C20). The Mo-Nb-Ta-W third-generation database (C21) is a lead only.

---

## Q3. Non-equiatomic compositions

### C23
Claim: Across a broad range of non-equiatomic VNbMoTaW compositions (thin-film fragmentation of VNbMoTaW, VNb2TaW, VNbMoTa2, V2NbTaW, V2NbMoTa), a single-phase BCC solid solution formed with comparable hardness, and replacing Mo with Nb was the most effective way to raise ductility.
Answers: Q3
Access: abstract-only
Source: T.B.N. Tuhser, I.S. Winter, D. Chrzan, T.J. Balk, "Enhancing intrinsic ductility in VNbMoTaW high entropy alloy: A combinatorial investigation with experimental evaluation of theoretical predictions", J. Mater. Res. Technol. 35 (2025), DOI 10.1016/j.jmrt.2025.02.011 (abstract via https://uknowledge.uky.edu/cme_facpub/123)
Where: Abstract
Evidence: "The replacement of Mo with Nb emerged as the most effective strategy"
Not claimed: numerical hardness, crack-onset strain or density; bulk compression data; the project's specific compositions (W23 Mo7 Ta25.5 Nb25 V19, W15 Mo15.6 Ta29 Nb25.7 V14.6).

### C24
Claim: DFT elastic-constant screening of 70 V-Mo-Nb-Ta-W compositions found that more Mo + W raises the moduli, V improves Pugh-criterion ductility indicators, and Nb and Ta have small effects; all 70 structures were mechanically stable.
Answers: Q3
Access: read-directly
Source: S. Zheng, S. Wang, "First-Principles Design of Refractory High Entropy Alloy VMoNbTaW", Entropy (2018), https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7512564/
Where: Results and conclusions
Evidence: "Element W is brittle and has high density"
Not claimed: experimental ductility (Pugh heuristics only; the paper states no VMoNbTaW experimental data existed for validation); phase stability.

### C25
Claim: As-cast NbTaTiVW was single-phase BCC with compressive yield strength 1420 MPa and fracture strain 20 %.
Answers: Q3 (Mo-free, Ti-containing neighbour)
Access: abstract-only
Source: Yao et al., Mater. Sci. Eng. A 674 (2016) 203-211 (as C20)
Where: Abstract
Evidence: "1420MPa with fracture strain of 20%"
Not claimed: Ti-free alloys; high-temperature strength; density.

### C26
Claim: VxNbMoTa alloys (V 0-25 at.%) are reported single-phase BCC from the solidus down to 350 C, with equimolar VNbMoTa giving 811 MPa yield strength at 1000 C and room-temperature fracture strain above 25 %.
Answers: Q3 (W-free neighbour); Q5
Access: search-summary
Source: M. Wang et al., "Designing VxNbMoTa refractory high-entropy alloys with improved properties for high-temperature applications", Scripta Materialia (2021) (Consensus record; not opened)
Where: Abstract (snippet)
Evidence: "yield strength of 811 MPa at 1000°C" (snippet)
Not claimed: W-containing alloys; how "phase stability down to 350 C" was established (anneal times unknown).

**Q3 status: partly answered.** I found no experimental report on Ta-/Nb-rich, Mo-lean W-Mo-Ta-Nb-V bulk alloys near the two named compositions among the sources that loaded. Nearby evidence: single BCC across varied VNbMoTaW thin-film compositions with better ductility when Nb replaces Mo (C23, abstract only), DFT trends (C24), and Ti- or W-free neighbours (C25, C26). The only densities found are for the equiatomic alloys (C17).

---

## Q4. Machine learning for phase prediction

### C27
Claim: In a 2436-alloy experimental dataset of Al-Co-Cr-Cu-Fe-Mn-Ni quinaries, VEC was the most important feature for separating BCC/B2 from FCC (thresholds VEC < 6.87 and > 9.16); the classes lumped BCC and B2 together.
Answers: Q4 (bears on P6)
Access: abstract-only
Source: C. Wang, W. Zhong, J.-C. Zhao, "Insights on phase formation from thermodynamic calculations and machine learning of 2436 experimentally measured high entropy alloys", J. Alloys Compd. 915, 165173 (2022), DOI 10.1016/j.jallcom.2022.165173, https://par.nsf.gov/biblio/10485156-insights-phase-formation-from-thermodynamic-calculations-machine-learning-experimentally-measured-high-entropy-alloys
Where: Abstract
Evidence: "VEC < 6.87 and VEC > 9.16"
Not claimed: anything about refractory alloys (none in the dataset); that VEC separates phases within an all-BCC system; the origin of the 6.87 threshold (P6, Guo et al. 2011, not opened).

### C28
Claim: In the same work the trained ANN predicted 66 external experimental solid-solution alloys with 81.8 % accuracy, below its roughly 89-93 % cross-validation accuracy.
Answers: Q4
Access: abstract-only
Source: Wang, Zhong, Zhao, J. Alloys Compd. 915, 165173 (2022) (as C27)
Where: Abstract
Evidence: 81.8% accuracy on 66 experimental SS alloys
Not claimed: performance on refractory systems.

### C29
Claim: An ML classifier for Al-containing refractory HEAs (Couzinié et al. data) predicted all 42 single-BCC alloys correctly but misclassified BCC+BCC and BCC+B2 alloys, which the authors attribute to scarce data (2 BCC+BCC and 13 BCC+B2 entries).
Answers: Q4
Access: read-directly
Source: M. Sreenidhi Iyengar, M.K. Anirudh, P.H. Anantha Desik, M.P. Phaniraj, "Composition based machine learning to predict phases & strength of refractory high entropy alloys", arXiv:2503.21146, https://arxiv.org/pdf/2503.21146
Where: Results (Table 4 discussion); dataset description
Evidence: "fewer data with similar phases in the database"
Not claimed: anything about VEC, delta, enthalpy or Omega (not used as features); W-Mo-Ta-Nb-V alloys. Reported accuracy metrics are internally inconsistent (accuracy labelled R²).

### C30
Claim: For NbMoTaW, the first-principles analysis finds that isoelectronic pairs (Mo-W, Nb-Ta) are disfavoured as nearest neighbours and pairs differing in valence (Nb-W, Mo-Ta, Nb-Mo, Ta-W) are favoured, while in VNbMoTaW second-neighbour V-W pairs drive B32-like order.
Answers: Q4 (mechanism context for why an average descriptor like VEC may not capture within-BCC instability); Q1
Access: read-directly
Source: Woodgate & Staunton, arXiv:2211.09911v2 (as C6)
Where: Section III.D
Evidence: second-nearest-neighbour V-W pairs "highly favoured" (paraphrased reading)
Not claimed: any statement by the authors about VEC or ML descriptors; that this explains the project's VEC finding.

### C31
Claim: delta and Omega were found inaccurate when applied to a large group of refractory HEAs, though useful within specific subsystems, and hardness correlated poorly with atomic size and modulus mismatch in single-phase BCC RHEAs.
Answers: Q4
Access: search-summary
Source: F. Coury et al., "Phase equilibria, mechanical properties and design of quaternary refractory high entropy alloys", Materials & Design 155 (2018) (Consensus abstract; the OSTI record https://www.osti.gov/pages/biblio/1513301 loaded metadata only)
Where: Abstract (snippet)
Evidence: δ and Ω "shown to be inaccurate" for a large group (snippet)
Not claimed: W-Mo-Ta-Nb-V-specific results.

### C32
Claim: A 2026 study of seven previously reported single-BCC RHEAs reports that composition criteria predict single-phase BCC reliably but not which alloy is strongest; of ten descriptors only mixing enthalpy ranked strength, and NbMoTaW was second weakest of six.
Answers: Q4, Q5
Access: search-summary
Source: L.-C. Zhuo et al., "Correlating Ten Composition-, Lattice- and Microstructure-Derived Descriptors with Compressive Yield Strength in Previously Reported Single-Phase BCC Refractory High-Entropy Alloys", Crystals (2026) (Consensus record; not opened)
Where: Abstract (snippet)
Evidence: "NbMoTaW, is second weakest of six" (snippet)
Not claimed: anything verified; n = 6, and the authors' own corrected q = 0.167 is not significant.

### C33
Claim: A high-throughput CALPHAD revisit of the VEC rule in Al-Co-Cr-Fe-Ni states that the rule has limitations, finding more than 90 % BCC for 5.7 <= VEC <= 7.2 and 100 % FCC for VEC >= 8.4.
Answers: Q4
Access: search-summary
Source: S. Yang et al., "Revisit the VEC rule in high entropy alloys (HEAs) with high-throughput CALPHAD approach...", Acta Materialia (2020) (Consensus record; not opened)
Where: Abstract (snippet)
Evidence: ">90% compositions ... BCC structures when 5.7≤VEC≤7.2" (snippet)
Not claimed: refractory systems; within-BCC discrimination.

**Q4 status: partly answered.** The sources that loaded show that VEC thresholds come from, and are tested on, FCC-vs-BCC separation in 3d-transition-metal datasets that lump BCC with B2 (C27), and that classifiers misclassify BCC+BCC and BCC+B2 alloys for lack of data (C29). I found no source that tests VEC, delta, enthalpy or Omega against phase-separation or ordering temperatures within an all-BCC refractory system. C31-C33 are leads only.

---

## Q5. Strength

### C34
Claim: Arc-melted Nb25Mo25Ta25W25 annealed at 1400 C had compressive yield strengths of 1058 MPa at 23 C, 561 (600 C), 552 (800 C), 548 (1000 C), 506 (1200 C), 421 (1400 C) and 405 MPa (1600 C).
Answers: Q5
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C1)
Where: Table 2
Evidence: 1058 MPa at 23 °C; 405 MPa at 1600 °C
Not claimed: the 996 and 1217 MPa room-temperature values in the project's training data (sources not found here).

### C35
Claim: Arc-melted V20Nb20Mo20Ta20W20 annealed at 1400 C had compressive yield strengths of 1246 MPa at 23 C, 862 (600 C), 846 (800 C), 842 (1000 C), 735 (1200 C), 656 (1400 C) and 477 MPa (1600 C).
Answers: Q5
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C1)
Where: Table 3
Evidence: 1246 MPa at 23 °C; 477 MPa at 1600 °C
Not claimed: values for other processing routes.

### C36
Claim: Both alloys were brittle in room-temperature compression, failing by splitting with quasi-cleavage fracture at about 2 % (NbMoTaW) and 1.7 % (VNbMoTaW) strain; the authors place the DBTT above room temperature.
Answers: Q5 (also Q3 ductility)
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C1)
Where: Sections 3.1.1, 3.1.2; Tables 2-3
Evidence: VNbMoTaW "failed by splitting at εp = 1.7%"
Not claimed: one consistent NbMoTaW strain value (the text gives 2.1 %, Table 2 1.5 % peak and 2.6 % fracture, and the Conclusions about 2 %).

### C37
Claim: Equiatomic WNbMoTaV made by 6 h mechanical alloying and spark plasma sintering at 1500 C reached a room-temperature compressive yield strength of 2612 MPa with 8.8 % failure strain, in a fine-grained single BCC matrix containing a small amount of oxide inclusions.
Answers: Q5
Access: abstract-only
Source: B. Kang, J. Lee, H.J. Ryu, S.H. Hong, "Ultra-high strength WNbMoTaV high-entropy alloys with fine grain structure fabricated by powder metallurgical process", Mater. Sci. Eng. A 712 (2018) 616-624, DOI 10.1016/j.msea.2017.12.021 (abstract via https://koasas.kaist.ac.kr/handle/10203/240572?mode=full)
Where: Abstract
Evidence: 2612 MPa; failure strain 8.8%
Not claimed: oxygen content, oxide fraction or exact grain size (not in what loaded).

### C38
Claim: Kang et al. attribute the high strength to grain-boundary strengthening, substitutional and interstitial solid-solution strengthening, and Orowan strengthening by oxide inclusions.
Answers: Q5 (scatter explanation)
Access: abstract-only
Source: Kang et al., Mater. Sci. Eng. A 712 (2018) 616-624 (as C37)
Where: Abstract
Evidence: paraphrase of abstract (no direct quote recorded)
Not claimed: the relative size of each contribution.

### C39
Claim: Mechanically alloyed and SPS-consolidated NbMoTaWVTi reached 2709 MPa room-temperature compressive yield strength, with 1.35 um grains, 0.86 wt% oxygen in the milled powder and TiO particles at 16.1 vol%.
Answers: Q5 (Ti-containing neighbour; processing effect)
Access: read-directly
Source: Y. Long, K. Su, J. Zhang, X. Liang, H. Peng, X. Li, "Enhanced Strength of a Mechanical Alloyed NbMoTaWVTi Refractory High Entropy Alloy", Materials 11(5), 669 (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC5978046
Where: Results; Section 3.1; Conclusions
Evidence: yield strength 2709 MPa, fracture strain 11.4%
Not claimed: a Ti-free alloy. TiO particle size differs between Section 3.1 (0.64 um) and Conclusions (0.46 um).

### C40
Claim: An edge-dislocation solute-strengthening theory with no fitted parameters agrees with the measured room-temperature strengths of MoNbTaW and MoNbTaVW but predicts lower values than measured at high temperature, where experiments show a plateau the theory does not reproduce.
Answers: Q5
Access: read-directly
Source: F. Maresca, W.A. Curtin, "Mechanistic Origin of High Strength in Refractory BCC High Entropy Alloys up to 1900K", arXiv:1901.02100v3 (13 Jun 2019), https://arxiv.org/pdf/1901.02100 (published Acta Mater. 182 (2020) 235 per ADS search result, not opened)
Where: Fig. 1 caption; Fig. 5 text; main text
Evidence: "plateau in yield strength in the range 900K–1300K not predicted"
Not claimed: one plateau range (Appendix C gives 800-1100 K); tabulated values (figures only).

### C41
Claim: Maresca and Curtin list O and N impurities, cast dendritic microstructure (a dendrite/interdendrite strength difference of order 100 MPa in MoNbTaV) and a Hall-Petch contribution of about 50 MPa for 80-200 um grains as factors that can move measured strength away from the intrinsic value.
Answers: Q5 (scatter explanation)
Access: read-directly
Source: Maresca & Curtin, arXiv:1901.02100v3 (as C40)
Where: Appendix B; discussion
Evidence: dendritic region "158 MPa stronger" than interdendritic (MoNbTaV)
Not claimed: a quantitative account of the 1246 vs 2612 MPa difference, which the paper does not address.

### C42
Claim: TiNbMoTaW and TiVNbMoTaW reach about 586 and 659 MPa at 1200 C, and Ti addition raised room-temperature yield strength and compressive plasticity relative to NbMoTaW and VNbMoTaW.
Answers: Q5
Access: abstract-only
Source: Han et al., Intermetallics 84 (2017) 153-157 (as C9), abstract via https://scholar.xjtu.edu.cn/zh/publications/effect-of-ti-additions-on-mechanical-properties-of-nbmotaw-and-vn/
Where: Abstract
Evidence: "∼586 and ∼659 MPa at 1200 °C"
Not claimed: the paper's own NbMoTaW / VNbMoTaW baseline values (not in the abstract).

**Q5 status: partly answered.** The full Senkov et al. temperature series for arc-melted, 1400 C-annealed WMoTaNb and WMoTaNbV loaded (C34-C35), and it matches the project's training values for those rows. The 2612 MPa value for WMoTaNbV traces to a mechanically alloyed and SPS-sintered, fine-grained, oxide-containing material (C37-C38), so the 1246 vs 2612 MPa gap compares different processing routes, not repeat measurements of one material. Sources for the 996 and 1217 MPa WMoTaNb values were not found. Mechanistic explanations of scatter (C41) are qualitative.

---

## Search log

```
Query: "NbMoTaW high entropy alloy long-term annealing phase stability decomposition hours"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: arXiv:2103.07951 (Bajpai et al.)
Blocked: none
Stopped: no

Query: "Senkov Wilks Scott Miracle "Mechanical properties of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 refractory high entropy alloys""  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: DTIC ADA550865 (Senkov et al. 2011 preprint); DTIC ADA550822 (Senkov et al., TaNbHfZrTi preprint - not about this system; only cites 13.8 / 12.4 g/cm3 densities and Hv 4.5 / 5.3 GPa for the two alloys from its refs 3-4, not recorded as claims)
Blocked: none
Stopped: no

Query: "WNbMoTaV high-entropy alloy powder metallurgy fine grain ultrahigh compressive yield strength 2612 MPa"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: KAIST KOASAS record (Kang et al. 2018 abstract)
Blocked: doi.org/10.3390/ma15155416 -> mdpi.com/1996-1944/15/15/5416 (WMoTaNb powder metallurgy, Materials 2022): URL not on allowlist
Stopped: no

Query: "MoNbTaVW refractory high entropy alloy aging heat treatment second phase precipitation B2 ordering experiment"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: figshare PDF of arXiv:1306.5043 (Huhn & Widom); par.nsf.gov/servlets/purl/10553141 (irrelevant: AlMoNb2Ti2-B alloy, not recorded)
Blocked: ar5iv.labs.arxiv.org/html/1306.5043 (not on allowlist; got the same paper via figshare)
Stopped: no

Query: ""NbMoTaWV" OR "WMoTaNbV" OR "MoNbTaVW" annealed long time phase stability single BCC retained 1000 h experiment"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: pure.unileoben.ac.at (Xia & Franz 2020 abstract); arXiv:2008.11671 (Maresca et al., NbTaTiV/CrMoNbV, no W-Mo-Ta-Nb-V phase data; not recorded)
Blocked: none
Stopped: no

Query: "phase stability of NbMoTaW and NbMoTaWV refractory high entropy alloys after long-term annealing, decomposition or ordering"  Tool: Consensus search (page_size 20)  Date: 2026-11-09
Opened: (search results only; Woodgate opened via next query)
Blocked: none
Stopped: no

Query: "Woodgate Staunton arXiv short-range order compositional phase stability NbMoTa NbMoTaW VNbMoTaW"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: arXiv:2211.09911v2
Blocked: none
Stopped: no

Query: "Senkov Miller Miracle Woodward "Accelerated exploration of multi-principal element alloys with solid solution phases" Nature Communications CALPHAD"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: DTIC ADA627998 (turned out to be the CALPHAD 50 (2015) companion paper, not the Nat. Commun. paper)
Blocked: PMC4366518 (Nat. Commun. 2015): URL not on allowlist
Stopped: no

Query: "NbMoTaW measured solidus liquidus temperature compared Thermo-Calc TCHEA prediction refractory high entropy alloy"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: home.iitm.ac.in 2020-calphad.pdf (Shaikh et al.); OSTI 1989196 (Puerling et al.)
Blocked: none
Stopped: no

Query: "Gorsse Senkov "About the reliability of CALPHAD predictions in multicomponent systems" Entropy 2018"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: PMC7512484
Blocked: none
Stopped: no

Query: "non-equiatomic W-Mo-Ta-Nb-V refractory high entropy alloy varying Mo content microstructure compressive properties ductility"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: PMC7512564 (Zheng & Wang); UKnowledge cme_facpub/123 (Tuhser et al. abstract); scholar.xjtu.edu.cn (Zhang et al. 2023, LPBF M0/M10/M20 - compositions not given in abstract, not recorded)
Blocked: none
Stopped: no

Query: "TaNbVW OR "NbTaVW" refractory high entropy alloy microstructure compressive yield strength density single BCC"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: opact.sdu.edu.tr record (Yao et al. 2016 abstract); jmst.org (Wu et al. 2022, CxHf0.25NbTaW0.5 - not in system, not recorded); PMC5978046 (Long et al. 2018)
Blocked: none
Stopped: no

Query: "limitations empirical parameters VEC delta Omega predicting phase formation refractory high entropy alloys machine learning classifier misclassification BCC"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: arXiv:2503.21146 (Iyengar et al.); par.nsf.gov biblio 10485156 (Wang, Zhong, Zhao abstract)
Blocked: none
Stopped: no

Query: "empirical criteria atomic size difference mixing enthalpy VEC fail to distinguish single-phase BCC from BCC+B2 or phase-separated BCC in refractory high entropy alloys"  Tool: Consensus search (page_size 15)  Date: 2026-11-09
Opened: (search results only)
Blocked: none
Stopped: no

Query: "Coury Kaufman Clarke "Phase equilibria, mechanical properties and design of quaternary refractory high entropy alloys" Materials & Design 2018"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: OSTI 1513301 (metadata only, no abstract or text)
Blocked: PMC6247412 (Couzinié et al., RHEA mechanical-property data compilation, Data in Brief 2018): URL not on allowlist
Stopped: no

Query: "Han Chen Liaw "Effect of Ti additions on mechanical properties of NbMoTaW and VNbMoTaW refractory high entropy alloys" yield strength"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: scholar.xjtu.edu.cn (Han et al. 2017 abstract)
Blocked: idr-sdlib.iitbhu.ac.in bitstream (loaded empty repository shell, no content)
Stopped: no

Query: "Maresca Curtin "Mechanistic origin of high strength in refractory BCC high entropy alloys up to 1900K" arXiv MoNbTaW"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: arXiv:1901.02100
Blocked: none
Stopped: no

Query: "Zou Maiti Steurer Spolenak "Ultrastrong ductile and stable high-entropy alloys at small scales" Nature Communications NbMoTaW"  Tool: WebSearch (standard)  Date: 2026-11-09
Opened: none
Blocked: PMC4510962 (Zou et al. 2015): reCAPTCHA interstitial
Stopped: yes (tool-call budget reached)
```

Not opened (leads from Consensus, recorded as search-summary only): Zhang et al. 2022
IJRMHM (Mo-Nb-Ta-W CALPHAD); Wang et al. 2021 Scripta (VxNbMoTa); Cao et al. 2022 JMST;
Vlasák et al. 2022 Metals; Gao et al. 2015 JOM; Coury et al. 2018 Mater. Des.; Zhuo et al.
2026 Crystals; Yang et al. 2020 Acta Mater.; Wan et al. 2021 (WTaMoNbTi, not recorded).
Not opened at all: Senkov et al., Intermetallics 18 (2010) 1758 (P1), Takeuchi & Inoue
(P4), Yang & Zhang (P5), Guo et al. (P6), Borg et al. (P7).
