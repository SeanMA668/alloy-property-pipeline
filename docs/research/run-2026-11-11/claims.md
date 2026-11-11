# Claims: run 2026-11-11 (literature-reviewer)

Written by the literature-reviewer agent, 2026-11-11. Each claim records how its source
was read. Pages were opened with WebFetch, which returns a model-extracted reading of the
page, not the raw text; quotes below are as returned by that reading. "read-directly"
means the relevant passage of the full text (or full preprint / full data sheet) was in
what loaded. `abstract-only` means only the abstract or an abstract-level record loaded.
`search-summary` claims are leads, not findings. No claim in this file is a judgement of
the project's own results.

Scope: the brief asks not to repeat run-2026-11-09. Where a claim restates something
already recorded there, the entry says so (e.g. "see run-2026-11-09 C40").

Disagreements and inconsistencies noticed while reading (recorded, not resolved):

- D1. Senkov et al. AFRL-RX-WP-TP-2011-4289 gives the 1600 C yield strength of
  V20Nb20Mo20Ta20W20 as 470 MPa in the Section 3.1.3 text but 477 MPa in Table 3
  (run-2026-11-09 C35); Atli & Karaman (2023) Table 1 lists 477 MPa.
- D2. The same preprint gives the 1400 C anneal as 19 h (Section 2) and 18 h
  (Section 3.2.1, Fig. 4) (already noted in run-2026-11-09 C1).
- D3. Senkov et al. AFRL-RX-WP-TP-2011-4295 (as-cast W-Nb-Mo-Ta): Table 4 shows Mo
  depleted in dendrite arms, but the Conclusions say dendrite arms were enriched with
  W and Mo.
- D4. Yao et al. (Entropy 2016) give the MoNbTaV lattice parameter as 3.2036 A in
  Section 3.1 and 3.208 A in the abstract.
- D5. The project's validation table (`reports/finalists.md`) labels MoNbTaV
  (doi:10.3390/e18050189) as "annealed". The paper itself, as read here, reports no
  anneal or homogenisation of MoNbTaV and tests it as cast (see C13). Recorded for the
  fact-checker; not resolved here.
- D6. P5 says Senkov et al. "homogenised" WMoTaNb and WMoTaNbV at 1400 C. The 2011
  preprint calls the treatment "annealed" and does not state its purpose (see C14).
  Recorded for the fact-checker.

---

## Q1. Strength models for this family

### C1
Claim: Maresca and Curtin attribute the higher strength of the V-containing alloy (MoNbTaVW vs MoNbTaW) to V having the largest misfit volume of the constituents, making it the most potent strengthener in their edge-dislocation theory.
Answers: Q1 (also Q3)
Access: read-directly
Source: F. Maresca, W.A. Curtin, "Mechanistic Origin of High Strength in Refractory BCC High Entropy Alloys up to 1900K", arXiv:1901.02100v3 (2019), https://arxiv.org/pdf/1901.02100 (published Acta Mater. 182 (2020) 235 per ADS/LAMMPS search listings; published version not opened)
Where: Section 4; Section 1; Section 6
Evidence: "V has the largest misfit volume and so is the most potent strengthener"
Not claimed: any prediction for NbTaVW specifically; a numerical V-content dependence; that misfit volume is the only factor (Section 6 also cites combining small and large elements, e.g. V and Ta, and stiff elements such as W).

### C2
Claim: In the same paper the edge-dislocation theory underpredicts the measured strength of MoNbTaV, and the authors estimate that cast dendritic regions are 158 MPa stronger and interdendritic regions 78 MPa weaker than the average composition.
Answers: Q1, Q2
Access: read-directly
Source: Maresca & Curtin, arXiv:1901.02100v3 (as C1)
Where: Appendix B; Fig. 5
Evidence: theory "underpredicts the measured strength" (MoNbTaV)
Not claimed: the size of the underprediction in MPa (no numbers given in the text; values are only in Fig. 5); partly repeats run-2026-11-09 C41.

### C3
Claim: Maresca and Curtin report very good parameter-free agreement with measured room-temperature yield strength for MoNbTaW and MoNbTaVW, and show NbTaV-(Ti,W) experimental data in the same comparison figure without a stated agreement or numbers in the text.
Answers: Q1
Access: read-directly
Source: Maresca & Curtin, arXiv:1901.02100v3 (as C1)
Where: Fig. 5 and Section 4
Evidence: "very good agreement" at 296 K, no adjustable parameters
Not claimed: numerical predicted-vs-measured values or errors (figures only); an NbTaVW-specific error. Repeats the substance of run-2026-11-09 C40 for Q1 context.

### C4
Claim: For as-cast MoNbTaV, a Labusch-type solid-solution strengthening model predicted a yield strength of about 1.5 GPa, close to the measured value of about 1.5 GPa.
Answers: Q1
Access: read-directly
Source: H. Yao, J.-W. Qiao, M.C. Gao, J.A. Hawk, S.-G. Ma, H. Zhou, "MoNbTaV Medium-Entropy Alloy", Entropy 18(5), 189 (2016), DOI 10.3390/e18050189, https://mdpi.com/1099-4300/18/5/189
Where: Sections 3.3 and 4.3; Fig. 7a
Evidence: "yield stress ... of MoNbTaV is 1.5 GPa"
Not claimed: the 1525 MPa value used in the project (the text read gives 1.5 GPa); model parameters; applicability to W-containing alloys. Only the first 100000 of 193754 characters of the page were read.

### C5
Claim: Yao et al. state that MoNbTaV properties do not follow a simple rule of mixtures and that solid-solution strengthening may play a larger role than expected, and they suggest a finer as-cast grain size (versus homogenised MoNbTaW) may also contribute.
Answers: Q1
Access: read-directly
Source: Yao et al., Entropy 18, 189 (2016) (as C4)
Where: Section 3.3
Evidence: properties "do not obey the simple ROM"
Not claimed: that grain size was measured or tested as a cause (presented as a possibility).

### C6
Claim: Thermo-Calc's Yield Strength Property Model implements the Walbrühl et al. (2017) solid-solution strengthening model, evaluated from equilibrium phase fractions and compositions, normalised over FCC, BCC and HCP; the help pages read do not mention Labusch, Varvenne or Maresca-Curtin models.
Answers: Q1
Access: read-directly
Source: Thermo-Calc Software, "About the Yield Strength Property Model", Thermo-Calc 2025b online help, https://help.thermocalc.com/2025b/content/property_models-gen/yieldstrength-about.htm
Where: Solid solution strengthening section
Evidence: Walbrühl et al. [2017Wal] model "is implemented"
Not claimed: the Simplified-mode details (on a separate page, not opened); the 2026a version used by the project (2025b help was read); the Walbrühl 2017 paper itself (not opened).

### C7
Claim: The Thermo-Calc help pages read show the yield-strength model validated against experiment only for the Mo-Ta binary (against Walbrühl 2017 data and, in example PM_G_06 with TCHEA, against 1972 data at 300 and 411 K); no W-Mo-Ta-Nb-V alloy appears.
Answers: Q1
Access: read-directly
Source: Thermo-Calc Software, "Yield Strength" (TCHEA validation example), https://help.thermocalc.com/2025b/content/databases/tchea/valid_examples/tchea_validex_yieldstrength.htm; and "PM_G_06: Yield Strength HEA", https://help.thermocalc.com/2025b/content/examples/propmodels-gen/pm_g_06_yield_strength_hea.htm
Where: Figure 1 captions on both pages
Evidence: "Total yield strength of the Mo-Ta BCC binary alloy"
Not claimed: that no other validation exists (only these two pages were read; the TCHEA Examples Collection PDF was not opened); any accuracy figure (none stated).

### C8
Claim: In NbTaV-(Ti,W) alloys, measured yield strengths were about 3.5-4.4 times rule-of-mixture estimates, and NbTaTiVW reached 1420 MPa with 20 % fracture strain.
Answers: Q1 (also Q3)
Access: abstract-only
Source: H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang, "NbTaV-(Ti,W) refractory high-entropy alloys: Experiments and modeling", Mater. Sci. Eng. A 674 (2016) 203-211, DOI 10.1016/j.msea.2016.07.102 (abstract via https://opact.sdu.edu.tr/vufind/SummonRecord/FETCH-LOGICAL-c540t-aa8133d9efb0fa421a079ac242f3a191bb5e2277601d5d333c095cfad931e15c3)
Where: Abstract
Evidence: "about 3 (and 3.5–4.4) times that those estimated from the rule of mixture"
Not claimed: the 1530 MPa NbTaVW value in P4 (the abstract does not give an NbTaVW strength; not verified here); any mechanistic explanation (none in the abstract). See also run-2026-11-09 C25.

### C9
Claim: In as-cast W-Nb-Mo-Ta and W-Nb-Mo-Ta-V, Vickers hardness was 4455 MPa and 5250 MPa respectively, against rule-of-mixture values of 1841 and 1596 MPa, and the authors attribute the higher hardness of the V alloy probably to a finer grain structure.
Answers: Q1, Q3
Access: read-directly
Source: O.N. Senkov, D.B. Miracle, G.B. Wilks, C.P. Chuang, P.K. Liaw, "Refractory High-Entropy Alloys", AFRL-RX-WP-TP-2011-4295 (preprint, July 2011; submitted to J. Alloys Compd. per the preprint), https://apps.dtic.mil/sti/pdfs/ADA550824.pdf
Where: Table 3; Results
Evidence: "The higher microhardness in Alloy2 is probably due to a finer grain structure"
Not claimed: grain-size measurements; yield strength; the published journal version (not opened; possibly the Intermetallics 18 (2010) 1758 paper but not checked).

**Q1 status: partly answered.** Among sources that loaded: a published mechanistic explanation for strong V-containing alloys exists (V has the largest misfit volume, C1), the Maresca-Curtin theory agrees with MoNbTaW/MoNbTaVW at room temperature but underpredicts MoNbTaV (C2-C3), a Labusch-type model matched as-cast MoNbTaV (C4), and Thermo-Calc's model is Walbrühl-based with only Mo-Ta validation shown (C6-C7). I found no published numerical test of any model against NbTaVW, and could not open a source giving the 1530 MPa NbTaVW value. Senkov et al. give a competing grain-size explanation for V-alloy hardness (C9).

---

## Q2. Casting segregation and homogenisation

### C10
Claim: In as-cast W-Nb-Mo-Ta (measured 27.3W-22.7Nb-25.6Mo-24.4Ta at.%), dendrite arms were enriched in W (+3.9 at.%) and depleted in Nb (-2.5) and Mo (-1.7) relative to the average, with Ta nearly unsegregated (+0.3).
Answers: Q2
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4295 (as C9)
Where: Table 4; Results (Microstructure)
Evidence: "the dendrite arms are enriched with W and depleted with Nb and Mo"
Not claimed: a consistent statement about Mo (the Conclusions say dendrites were enriched in Mo; see D3); any heat-treated condition (as-cast only).

### C11
Claim: In as-cast W-Nb-Mo-Ta-V (measured 21.1W-20.6Nb-21.7Mo-15.6Ta-21.0V at.%), dendrite arms were enriched in W (+4.7) and Ta (+1.1) and depleted in V (-4.0) and Nb (-1.7), while interdendritic regions were enriched in V (+6.3) and Nb (+2.6) and depleted in W (-7.3).
Answers: Q2, Q3
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4295 (as C9)
Where: Table 5
Evidence: Alloy 2 Cidr − Caver: V +6.3, W −7.3
Not claimed: homogenisation behaviour (none was performed in this preprint); the measured composition is not equiatomic (Ta 15.6 at.%).

### C12
Claim: In as-cast MoNbTaV the dendrite arms are enriched in Ta and Mo and the interdendritic regions strongly enriched in V, with Nb close to the bulk value.
Answers: Q2, Q3
Access: read-directly
Source: Yao et al., Entropy 18, 189 (2016) (as C4)
Where: Section 3.1; Table 2; Figs. 3-4
Evidence: "interdendritic regions are enriched strongly with V"
Not claimed: numerical compositions (Table 2 values were not legible in the extracted text).

### C13
Claim: Yao et al. performed no homogenisation of MoNbTaV, tested it as cast, and state that proper homogenisation is needed before high-temperature evaluation but is beyond the scope of their study.
Answers: Q2 (bears on P4 and D5)
Access: read-directly
Source: Yao et al., Entropy 18, 189 (2016) (as C4)
Where: Section 2; Section 3.3
Evidence: homogenization "beyond the scope of the present study"
Not claimed: that no other MoNbTaV report used an anneal.

### C14
Claim: Senkov et al. heat-treated arc-melted Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 at 1400 C for 19 h (18 h elsewhere in the same paper), call this an anneal, do not state its purpose, and do not report whether dendritic segregation remained afterwards.
Answers: Q2 (bears on P5 and D6)
Access: read-directly
Source: O.N. Senkov, G.B. Wilks, J.M. Scott, D.B. Miracle, "Mechanical Properties of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 Refractory High-Entropy Alloys", AFRL-RX-WP-TP-2011-4289 (preprint, July 2011), https://apps.dtic.mil/sti/pdfs/ADA550865.pdf
Where: Section 2; Sections 3.2.1-3.2.2
Evidence: "annealed (1400°C for 19 hours)"
Not claimed: atmosphere or cooling (not stated); the published Intermetallics 19 (2011) 698 version (not opened).

### C15
Claim: The same preprint reports that compositional inhomogeneity persisted after compression at 1400 C, which the authors say even dynamic recrystallization could not remove.
Answers: Q2
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C14)
Where: Section 3.2.4
Evidence: "Even dynamic recrystallization was not able to remove the compositional inhomogeneity"
Not claimed: segregation magnitude after the 1400 C anneal itself.

### C16
Claim: Equiatomic MoNbTaW was given a homogenisation anneal at 1800 C for 4 days, but the paper reports no chemical-homogeneity check of the result.
Answers: Q2
Access: read-directly
Source: V. Bajpai, S. Maiti, S. Mishra, B. Rai, "Temperature dependent phase stability of Mo-Nb-Ta-W refractory high-entropy alloys", arXiv:2103.07951, https://arxiv.org/pdf/2103.07951
Where: Section 2 (Experiments)
Evidence: "annealed in 1800°C first for homogenization annealing for 4 days"
Not claimed: that 1800 C / 4 days achieved homogeneity; atmosphere (not stated). See run-2026-11-09 C3.

### C17
Claim: In as-cast NbTaTiW, dendrite cores were enriched in W (27.2 vs 9.1 at.%) and Ta (24.5 vs 14.1) and interdendritic regions in Ti (52.3 vs 26.0), with Nb similar in both.
Answers: Q2 (analogue alloy, no V)
Access: read-directly
Source: R. Puerling, A. Miklas, F.G. Coury, N.R. Philips, P. Mason, N.E. Peterson, A. Deal, J. Klemm-Toole, A.J. Clarke, "Thermodynamics and Kinetics of Refractory Multi-Principal Element Alloys: An Experimental and Modeling Comparison", report NSC-614-4990 (01/2023), https://www.osti.gov/servlets/purl/1989196
Where: p. 5; Table 2
Evidence: "dendrite cores are Mo, Ta, and W-rich ... interdendritic regions are Nb and Ti-rich"
Not claimed: V-containing alloys. The model-extracted table reading lists the core value first; not cross-checked against the PDF image.

### C18
Claim: After 35 h at 1673 K under vacuum, NbTaTiW and MoNbTaTi still showed residual segregation (Ta and W remained core-enriched), whereas DICTRA with MOBHEA2 predicted near-complete homogenisation; the authors attribute the gap mainly to a too-high Ta diffusivity in the mobility database.
Answers: Q2 (analogue alloys)
Access: read-directly
Source: Puerling et al., NSC-614-4990 (as C17)
Where: pp. 3-7; Fig. 1(b), Fig. 2; Tables 4-5
Evidence: NbTaTiW after treatment: core Ta 27.9, W 29.1 vs 23.9, 23.5 interdendritic
Not claimed: the time needed for full homogenisation; any W-Mo-Ta-Nb-V alloy. Extends run-2026-11-09 C18 (abstract-level) with the body text.

### C19
Claim: Annealing as-solidified MoNbTaTiVZr at 1400 C for 12 h, then 1000 C for 12 h with quenching, did not homogenise its Zr segregation, whereas high-pressure torsion did.
Answers: Q2 (analogue alloy)
Access: read-directly
Source: C. Duan, A. Kostka, X. Li, Z. Peng, P. Kutlesa, R. Pippan, E. Werner, "Deformation-induced homogenization of the multi-phase senary high-entropy alloy MoNbTaTiVZr processed by high-pressure torsion", Mater. Sci. Eng. A 871, 144923 (2023); arXiv:2306.05711, https://www.arxiv.org/pdf/2306.05711
Where: Section 3.1; Table 1; Section 4.2
Evidence: "did not homogenize the RHEA either"
Not claimed: anything about W-containing alloys; the Zr-driven segregation here (Zr 8.8 vs 43.8 at.%) has no analogue in W-Mo-Ta-Nb-V.

### C20
Claim: In as-cast NbTaTiV the dendrites are enriched in Nb and Ta while Ti and V are found preferentially in interdendritic regions.
Answers: Q2 (analogue alloy), Q3
Access: read-directly
Source: C. Lee, G. Song, M.C. Gao, R. Feng, P. Chen, J. Brechtl, Y. Chen, K. An, W. Guo, J.D. Poplawsky, S. Li, A.T. Samaei, W. Chen, A. Hu, H. Choo, P.K. Liaw, "Lattice distortion in a strong and ductile refractory high-entropy alloy", Acta Mater. 160 (2018) 158-172, https://par.nsf.gov/servlets/purl/10178918
Where: Section 3.2
Evidence: "Ti and V are more preferentially distributed in the interdendritic region"
Not claimed: W- or Mo-containing alloys; homogenisation.

**Q2 status: partly answered.** For W-Mo-Ta-Nb-V alloys themselves, measured as-cast segregation loaded for W-Nb-Mo-Ta, W-Nb-Mo-Ta-V and MoNbTaV: W (and Ta, Mo in MoNbTaV) enrich dendrite cores, V and Nb enrich interdendritic regions (C10-C12); analogues agree on V and Ti going interdendritic (C17, C20). On homogenisation, I found no paper among those that loaded that measures residual segregation after a heat treatment of a W-Mo-Ta-Nb(-V) alloy. The treatments found are 1400 C / 18-19 h (purpose not stated, C14) and 1800 C / 4 days (outcome not checked, C16); 1673 K / 35 h left residual segregation in W-containing analogues (C18). No source that loaded compared measured freezing ranges with Scheil for these alloys.

---

## Q3. Effect of vanadium

### C21
Claim: Measured density was 13.75 g/cm3 for as-cast W-Nb-Mo-Ta and 12.36 g/cm3 for as-cast W-Nb-Mo-Ta-V (theoretical 13.64 and 12.36), with lattice parameters 3.2134 and 3.1832 A.
Answers: Q3
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4295 (as C9)
Where: Tables 2-3
Evidence: density 13.75 ± 0.028 vs 12.36 ± 0.011 g/cm³
Not claimed: a per-at.% V density slope; the alloys are not exactly equiatomic (see C11). Compare run-2026-11-09 C17 (13.64 / 12.36 g/cm3 via Shaikh et al.).

### C22
Claim: Between 600 and 1600 C, the V-containing equiatomic alloy kept a higher yield strength than NbMoTaW, with the text giving falls from 862 to 470 MPa (V alloy) and 561 to 405 MPa (V-free alloy).
Answers: Q3, Q5
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C14)
Where: Section 3.1.3; Fig. 3
Evidence: "from 862 to 470 MPa" (V alloy); Table 3 gives 477 MPa at 1600 C
Not claimed: one consistent 1600 C value (see D1). Full temperature series: run-2026-11-09 C34-C35.

### C23
Claim: Both equiatomic alloys failed by splitting in room-temperature compression, Nb25Mo25Ta25W25 at 2.1 % and V20Nb20Mo20Ta20W20 at 1.7 % plastic strain, so adding V did not give room-temperature compressive ductility in this pair.
Answers: Q3
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C14)
Where: Sections 3.1.1 and 3.1.2
Evidence: "failed at εp = 1.7% by splitting" (V alloy); "failed by splitting at εp = 2.1%"
Not claimed: tensile ductility; behaviour at other V contents. Repeats run-2026-11-09 C36 (re-read this run).

### C24
Claim: In VxNbMoTa alloys, raising V content improved room-temperature yield strength and ductility, attributed to solid-solution strengthening, grain refinement and fewer grain-boundary impurities, while at 800 and 1000 C higher-V alloys showed weaker strain hardening.
Answers: Q3 (W-free neighbour)
Access: abstract-only
Source: M. Wang, Z.L. Ma, Z.Q. Xu, X.W. Cheng, "Effects of vanadium concentration on mechanical properties of VxNbMoTa refractory high-entropy alloys", Mater. Sci. Eng. A 808, 140848 (2021), DOI 10.1016/j.msea.2021.140848 (abstract record via https://pure.bit.edu.cn/en/publications/effects-of-vanadium-concentration-on-mechanical-properties-of-vsu/)
Where: Abstract
Evidence: yield strength "greatly improved when increasing the V concentration"
Not claimed: the x values, phases or numerical strengths (not on the page); W-containing alloys.

### C25
Claim: A 2025 TixNbMoTaW paper states, citing Senkov et al., that vanadium addition raised high-temperature strength but sacrificed plasticity and toughness.
Answers: Q3
Access: read-directly
Source: R. Zhao, Y. Cao, J. He, J. Chen, S. Liu, Z. Yang, J. Lin, C. Chang, "Microstructure and Mechanical Properties of TixNbMoTaW Refractory High-Entropy Alloy for Bolt Coating Applications", Coatings 15(2), 120 (2025), DOI 10.3390/coatings15020120, https://www.mdpi.com/2079-6412/15/2/120
Where: Introduction
Evidence: "it sacrificed the alloy's plasticity and toughness"
Not claimed: primary evidence (a secondary statement in an introduction); only the first 100000 of 162914 characters were read.

### C26
Claim: In W-Ta-Cr-V, first-principles-based modelling finds higher V concentration associated with lower order-disorder transition temperatures, with low-temperature phase separation into Cr-V-rich and W-Ta-rich domains.
Answers: Q3 (analogue system)
Access: read-directly
Source: B. Sun, M. Fedorov, J. Wrobel, D. Nguyen-Manh, C. Hatler, M. Vigil, D.J. Thoma, O. El-Atwani, E. Martinez, "Thermodynamic assessment of the quaternary WTaCrV refractory high entropy alloy as a means to guide experimental approaches", Acta Mater. 299 (2025) 121435, https://scientific-publications.ukaea.uk/wp-content/uploads/A2E98271-CDC1-484B-80F4-D403440D7190.PDF
Where: Section 3.3; Conclusions
Evidence: "a high concentration of V is generally associated with lower ODTTs"
Not claimed: anything about Mo- or Nb-containing alloys; a disordered A2+A2 split of the TCHEA kind. Contrast run-2026-11-09 C6, where V drives B32-like ordering in VNbMoTaW.

**Q3 status: partly answered.** For W-Mo-Ta-Nb-V itself, the evidence that loaded compares equiatomic alloys with and without V only: V lowers density (C21), raises hardness and high-temperature strength (C9, C22, C1), and both alloys are brittle in room-temperature compression (C23). No study varying V content within W-Mo-Ta-Nb-V loaded; the V-series found is W-free (C24, abstract only). On melting point, the only values found are the TCHEA-vs-rule-of-mixtures liquidus pair in run-2026-11-09 C16; no measured solidus or per-at.% V slope loaded. Phase-stability effects of V in loaded sources are ordering-type (run-2026-11-09 C6) or from an analogue system (C26).

---

## Q4. Cost and critical raw materials in alloy design

### C27
Claim: Mulukutla et al. used an element-level supply-risk index (twelve indicators in four groups, alloy value as a weighted mean) as one objective in multi-objective batch Bayesian optimisation of Mo-Nb-Ti-V-W refractory alloys, alongside yield strength, ductility, thermal conductivity and density.
Answers: Q4
Access: read-directly
Source: M. Mulukutla, R. Robinson, D. Khatamsaz, B. Vela, N. Vu, R. Arróyave, "Supply Risk-Aware Alloy Discovery and Design", arXiv:2409.15391v1 (2024), https://arxiv.org/html/2409.15391v1
Where: Sections 2.1, 2.3; Table 1
Evidence: "twelve indicators at the elemental level"
Not claimed: use of the EU CRM scores (the index is their own framework; SR data partly from 2015); Ta in the system.

### C28
Claim: In that study, adding supply risk as an objective left average yield strength very similar across scenarios, raw-material cost was only compared afterwards (not optimised), and the authors call cost a lagging indicator of supply-chain risk.
Answers: Q4
Access: read-directly
Source: Mulukutla et al., arXiv:2409.15391v1 (as C27)
Where: Sections 3-4; Fig. 11
Evidence: cost "tends to be a lagging indicator"
Not claimed: element prices or their source (in a supplementary Table S4, not opened).

### C29
Claim: Nominé et al. screened 30,201 predicted equimolar HEAs on supply concentration (HHI), ESG risk, by-product dependence, production and reserves, and CO2/energy footprint, and report a resilient shortlist of about 5 % of alloys, without using prices.
Answers: Q4
Access: read-directly
Source: A. Nominé et al. (with J. Zavašnik, U. Cvelbar), "The hidden sustainability bottleneck in high-entropy alloy design", arXiv:2601.00852v1, https://arxiv.org/pdf/2601.00852v1
Where: Abstract; Methods; Fig. 3
Evidence: "identify a resilient shortlist" (~5 % of HEAs)
Not claimed: year of publication (not stated on the page); results for W-Mo-Ta-Nb-V alloys; use of EU CRM supply-risk scores (USGS MCS 2022 used for production data).

### C30
Claim: USGS reports the average vanadium pentoxide price as $5.02 per pound in 2025 (down from $5.44 in 2024) and the ferrovanadium (78-82 % V) price as $14.14 per pound in 2025.
Answers: Q4 (bears on P1)
Access: read-directly
Source: U.S. Geological Survey, Mineral Commodity Summaries 2026, Vanadium, https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-vanadium.pdf
Where: Salient statistics table (Price row); narrative text
Evidence: "8.17 9.29 7.50 5.44 5.02" ($/lb V2O5, 2021-2025)
Not claimed: that the V2O5 price is China-specific (the extract did not show the footnote 6 text); any vanadium metal price (none in the chapter).

### C31
Claim: USGS estimates 2025 vanadium mine production at 82,000 for China out of a rounded world total of 110,000.
Answers: Q4 (bears on P1)
Access: read-directly
Source: USGS MCS 2026, Vanadium (as C30)
Where: World Mine Production and Reserves table
Evidence: "China e84,000 82,000"; "World total (rounded) 118,000 110,000"
Not claimed: the unit (not labelled for this column in the extract; not read here).

### C32
Claim: USGS gives the 2025 average unit value of ferroniobium as $26 per kilogram, and 2025 Brazil mine production of 104,000 out of a rounded world total of 112,000.
Answers: Q4 (bears on P2)
Access: read-directly
Source: USGS MCS 2026, Niobium (Columbium), https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-niobium.pdf
Where: Salient statistics; World Mine Production table
Evidence: "ferroniobium, dollars per kilogram5 21 25 25 26 26"
Not claimed: the Nb grade of ferroniobium or whether $/kg is gross weight (footnote 5 not read); any niobium metal price (none in the chapter).

### C33
Claim: USGS gives the 2025 annual average tantalite price as $180 per kilogram of Ta2O5 content, and the chapter gives no price for tantalum metal.
Answers: Q4
Access: read-directly
Source: USGS MCS 2026, Tantalum, https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-tantalum.pdf
Where: Salient statistics (Price row)
Evidence: "158 196 170 167 180" ($/kg Ta2O5, 2021-2025)
Not claimed: metal prices.

### C34
Claim: A Shanghai Metals Market report of February 2026 quotes, in one article, tantalum ore at $160-165 per pound (China landed/CIF), 99.5 % tantalum oxide at 3,900 yuan/kg and 99.95 % tantalum ingot at 5,500 yuan/kg (some offers 6,000).
Answers: Q4
Access: read-directly
Source: Shanghai Metals Market (SMM), "Supply Contraction Drives Up Tantalum Ore Prices, Smelting Cost Increases Face Short-Term Obstacles [SMM Analysis]", 27 Feb 2026, https://news.metal.com/newscontent/103781654-Supply-Contraction-Drives-Up-Tantalum-Ore-Prices-Smelting-Cost-Increases-Face-Short-Term-Obstacles-SMM-Analysis
Where: Article body (price statements)
Evidence: tantalum ingot 99.95%: 5,500 yuan/kg
Not claimed: the ore grade or whether the ore price is per lb of Ta2O5 (not stated in what loaded); an ingot-to-concentrate ratio (units and bases differ; not computed here); trade press, not peer-reviewed.

### C35
Claim: IMARC Group reports a US tantalum price of $502/kg for Q4 2025 without specifying product form or purity.
Answers: Q4
Access: read-directly
Source: IMARC Group, "US Tantalum Prices Hold at USD 502/KG Amid Stable Industrial Demand", 18 Feb 2026, https://www.imarcgroup.com/news/tantalum-price-index
Where: Regional table; "Tantalum Price Trend Q4 2025"
Evidence: USD 502/KG (USA, Q4 2025)
Not claimed: that this is a metal price (form not stated); methodology; the headline ("Hold") conflicts with the body (+5.46 % QoQ).

### C36
Claim: A Nb-based alloy design study used C-103's density (8.85 g/cm3) and cost ($500/kg) as the benchmark that its new alloy had to undercut.
Answers: Q4, Q5
Access: read-directly
Source: A.M. Nahin, J. Pustelnik, J. Dong, T. Zakia, M. Zhang, "A Low-Cost, Strong, and Ductile Single-Phase Nb-Based Refractory Complex Concentrated Alloy", arXiv:2602.07293, https://arxiv.org/pdf/2602.07293
Where: Introduction (design criteria)
Evidence: C-103 "8.85 g/cm3and $500/kg"
Not claimed: the source or year of the $500/kg figure; W-Mo-Ta-Nb-V alloys.

**Q4 status: partly answered.** Published uses of supply risk in refractory/HEA design loaded (C27-C29), and cost appears as a benchmark in one alloy-design paper (C36). USGS 2025 concentrate/oxide/ferroalloy prices loaded for V, Nb and Ta (C30-C33); none of these chapters gives a metal price. The only metal-vs-raw-material comparison found is a trade-press tantalum quote (C34); no high-purity (arc-melting grade) price for W, Mo, Nb or V loaded (SMM vanadium metal and V2O5 pages require a login). I did not open the USGS tungsten or molybdenum chapters this run.

---

## Q5. Comparison with existing refractory alloys

### C37
Claim: Senkov et al. report that the yield strengths of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 are much higher than Haynes 230 at all temperatures studied and higher than Inconel 718 above 800 C.
Answers: Q5
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C14)
Where: Section 3.1.3; Fig. 3
Evidence: "higher than that of Inconel 718 at temperatures above 800°C"
Not claimed: an exact crossover temperature; that the comparison is like-for-like (HEA compression vs superalloy literature data).

### C38
Claim: In the same paper Inconel 718 is described as exceeding 1000 MPa up to 650 C, falling to 138 MPa at 982 C, and melting at about 1210 C, with Haynes 230 about 255-275 MPa from 540 to 870 C.
Answers: Q5
Access: read-directly
Source: Senkov et al., AFRL-RX-WP-TP-2011-4289 (as C14)
Where: Section 3.1.3
Evidence: Inconel 718 YS "rapidly decreases to 138 MPa" at 982 C
Not claimed: primary superalloy data (the paper cites data sheets, not opened).

### C39
Claim: A 2023 review tabulates Ni superalloy tensile data of 8.22 g/cm3 and 105 MPa at 1200 C for Inconel 718, and 8.70 g/cm3 with 420 MPa at 1094 C and 146 MPa at 1204 C for CMSX-4, noting these are tensile while the RHEA values are compressive.
Answers: Q5
Access: read-directly
Source: K.C. Atli, I. Karaman, "A short review on the ultra-high temperature mechanical properties of refractory high entropy alloys", Frontiers in Metals and Alloys 2 (2023), DOI 10.3389/ftmal.2023.1135826, https://www.frontiersin.org/articles/10.3389/ftmal.2023.1135826
Where: Table 1 and caption; Section 3.1
Evidence: CMSX-4: 8.70 g·cm⁻³, 420 MPa at 1,094°C
Not claimed: consistency within the review (Section 3.1.1 cites Inconel 718 at 130 MPa at 1000 C, not in Table 1); C-103 or Ta-10W (not mentioned). First 100000 of 105163 characters read.

### C40
Claim: The same review lists MoNbTaW at 13.64 g/cm3 with 506, 421 and 405 MPa at 1200, 1400 and 1600 C, and MoNbTaVW at 12.35 g/cm3 with 735, 656 and 477 MPa at the same temperatures (compression, 0.001 s-1).
Answers: Q5, Q3
Access: read-directly
Source: Atli & Karaman (2023) (as C39)
Where: Table 1
Evidence: MoNbTaVW 12.35 g·cm⁻³; 735 MPa at 1,200°C
Not claimed: independent data (values trace to Senkov et al.; see D1 for 470 vs 477 MPa).

### C41
Claim: The review notes that high-density RHEAs do not reach the specific yield strength of medium-density RHEAs because of their high densities.
Answers: Q5
Access: read-directly
Source: Atli & Karaman (2023) (as C39)
Where: Section 3.1.3
Evidence: "due to their relatively high densities"
Not claimed: a ranking of specific alloys by the reviewers.

### C42
Claim: Materion's C-103 data sheet gives typical values of 8.850 g/cm3 density, 2350 C melting point, and 0.2 % yield strength of 262 MPa at 25 C and 110 MPa at 1093 C.
Answers: Q5
Access: read-directly
Source: Materion Corporation, "Niobium C-103 Bar and Rod Data Sheet", DS-AM-622 (2024), https://hkvxni.files.cmp.optimizely.com/download/assets/Niobium+C-103+Bar+and+Rod+Data+Sheet/8aef8eca300b11ef899fe60a55c50f3d
Where: Physical and mechanical property tables
Evidence: 2000˚F (1093˚C): "16 (110)" ksi (MPa)
Not claimed: minimum/design values (sheet says reference only); test mode (not stated in what loaded); the exact date (footer rendered as "6 .2 1.2024").

### C43
Claim: ATI's Ta-10W data sheet gives 16.9 g/cm3 density, 3035 C melting point, and recrystallized-sheet yield strengths of 70,000-89,000 psi at room temperature, 22,300-28,300 psi at 2600 F, 10,500-12,300 psi at 3000 F and 9,400 psi at 3500 F.
Answers: Q5
Access: read-directly
Source: ATI (Allegheny Technologies), "ATI Ta-10W" technical data sheet, v5, dated 5/13/13, https://www.atimaterials.com/Products/Documents/datasheets/niobium-hafnium-tantalum-vanadium/tantalum/ati_Ta10W_v5.pdf
Where: Tables 2-4
Evidence: "5495°F, 3035ºC"; RT YS "70,000–89,000" psi
Not claimed: values in MPa (not converted here); minimum values (sheet says typical only); stress-relieved values (55,100 psi at 2000 F; 34,700 psi at 2400 F) are a different condition.

### C44
Claim: Wieland's TZM data sheet lists density 10.2 g/cm3 and a reference yield strength of 750-900 N/mm2 without stating test temperature, and gives elevated-temperature data only as a tensile-strength graph whose values did not come through in the extraction.
Answers: Q5
Access: read-directly
Source: Wieland Duro GmbH, "TZM" product data sheet (TZM_EX_EN.pdf, undated), https://www.wieland.com/da/content/download/12678/file/TZM_EX_EN.pdf
Where: Property table; tensile strength vs temperature graph
Evidence: "Yield strength N/mm² 750–900"
Not claimed: melting point (not stated); high-temperature yield strength; condition of the 750-900 value.

### C45
Claim: Singh et al. state, citing the literature, that typical refractory HEAs have yield strengths of 500-700 MPa at 1200 C, surpassing Ni-based superalloys, and compare their alloys with commercial TZM only on Young's modulus versus temperature.
Answers: Q5
Access: read-directly
Source: P. Singh, A. Sharma, A.V. Smirnov, M.S. Diallo, P.K. Ray, G. Balasubramanian, D.D. Johnson, "Design of high-strength refractory complex solid-solution alloys", arXiv:1710.06983, https://arxiv.org/pdf/1710.06983
Where: Introduction; Fig. 6(c)
Evidence: "500-700 MPa at 1200°C, surpassing Ni-based superalloys"
Not claimed: primary data (secondary statement); TZM yield strength.

### C46
Claim: Six Al-containing refractory HEAs (Mo/Ta/Hf with Nb, V, Zr, Ti, Al) had densities of 6.9-9.1 g/cm3 and room-temperature compressive yield strengths of 1280-2035 MPa, and are described as considerably stronger at high temperature than advanced Ni-based superalloys.
Answers: Q5 (context; not W-Mo-Ta-Nb-V)
Access: abstract-only
Source: O.N. Senkov, C. Woodward, D.B. Miracle, "Microstructure and Properties of Aluminum-Containing Refractory High-Entropy Alloys", JOM 66(10) (2014) 2030-2042, DOI 10.1007/s11837-014-1066-0, https://link.springer.com/content/pdf/10.1007/s11837-014-1066-0.pdf
Where: Abstract
Evidence: "considerably improved high temperature strengths relative to advanced Ni-based superalloys"
Not claimed: which superalloys or numbers (body paywalled).

**Q5 status: partly answered.** Published comparisons of W-Mo-Ta-Nb-V HEAs with Ni superalloys loaded (C37-C40), with tabulated densities and 1200-1600 C strengths for MoNbTaW and MoNbTaVW. I found no published paper among those that loaded that compares W-Mo-Ta-Nb-V HEAs directly with C-103, TZM or Ta-10W; for those alloys I recorded manufacturer data sheets (C42-C44), which give typical values, use different test conditions and units, and for TZM lack a high-temperature yield strength. CMSX-4 density and strength come from one review (C39).

---

## Search log

```
Query: "Maresca Curtin edge dislocation model prediction NbTaVW yield strength vanadium misfit volume"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: none from this query at the time (arXiv:1901.02100 opened after the later Maresca query)
Blocked: none
Stopped: no

Query: "Thermo-Calc property model yield strength solid solution strengthening high entropy alloys validation documentation"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: help.thermocalc.com TCHEA yield-strength validation example; "About the Yield Strength Property Model"; PM_G_06 example
Blocked: none (TCHEA_Examples_Collection.pdf not attempted)
Stopped: no

Query: "NbMoTaW as-cast dendrite interdendritic segregation EDS W Ta enriched dendrite Nb interdendritic homogenization"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: OSTI 1989196 (Puerling et al.)
Blocked: none
Stopped: no

Query: ""MoNbTaV" refractory high-entropy alloy Entropy 2016 18 189 microstructure mechanical properties"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: mdpi.com/1099-4300/18/5/189 (Yao et al.; first 100000 of 193754 characters)
Blocked: none
Stopped: no

Query: "NbTaVW refractory high entropy alloy yield strength 1530 MPa vanadium strengthening lattice distortion"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: OSTI 1706235 ("Lattice-Distortion-Enhanced Yield Strength in a Refractory High-Entropy Alloy", Adv. Mater. 32(49); metadata only, no authors, alloy or abstract; not recorded as a claim)
Blocked: none
Stopped: no

Query: "Senkov Wilks Miracle Chuang Liaw refractory high-entropy alloys Intermetallics 2010 NbMoTaW dendrite composition homogenization 1400 C 19 h"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: DTIC ADA550824 (Senkov et al., AFRL-RX-WP-TP-2011-4295); DTIC ADA550865 (Senkov et al., AFRL-RX-WP-TP-2011-4289; read three times: heat treatment, superalloy comparison, RT failure strains)
Blocked: none
Stopped: no

Query: "Yao Qiao Gao Hawk "NbTaV-(Ti,W) refractory high-entropy alloys: Experiments and modeling" pdf"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: opact.sdu.edu.tr record (abstract)
Blocked: no full text found
Stopped: no

Query: "Maresca Curtin "Mechanistic origin of high strength in refractory BCC high entropy alloys" Acta Materialia 182 2020 235 NbTaV"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: arXiv:1901.02100
Blocked: none
Stopped: no

Query: ""NbTaVW" yield strength as-cast compression Yao 2016 osti OR nsf full text"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: par.nsf.gov/servlets/purl/10178918 (Lee et al. 2018, NbTaTiV)
Blocked: no NbTaVW full text found
Stopped: no

Query: "vanadium content effect VxNbMoTaW refractory high entropy alloy yield strength ductility density phase"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: pure.bit.edu.cn record (Wang et al. 2021, abstract)
Blocked: none
Stopped: no

Query: "MoNbTaW refractory high entropy alloy homogenization heat treatment elemental segregation eliminated temperature hours dendritic as-cast"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: arXiv:2306.05711 (Duan et al.)
Blocked: aminer.cn record for "Influence of thermomechanical processing on microstructure and mechanical properties of MoNbTaW" (loaded a generic landing page with no paper content)
Stopped: no

Query: ""NbMoTaWV" OR "WMoTaNbV" OR "VNbMoTaW" homogenized annealed "1600 °C" OR "1800 °C" OR "2000 °C" segregation dendrite arc-melted"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: none new (results were sources already opened or opened under the next query)
Blocked: none
Stopped: no

Query: "Bajpai Maiti arXiv 2103.07951 MoNbTaW homogenized 1800 C four days"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: arXiv:2103.07951; par.nsf.gov/servlets/purl/10420388 (same Puerling et al. report as OSTI 1989196)
Blocked: none
Stopped: no

Query: "MoNbTaWVx OR "NbMoTaWVx" high-entropy alloy effect of V addition microstructure compressive properties"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: none (no W-Mo-Ta-Nb-V V-series in the results; eld.bl.uk catalogue entry for a two-phase NbMoTaWV paper not opened)
Blocked: none
Stopped: no

Query: "Effect of vanadium on phase stability W-Mo-Ta-Nb-V high entropy alloy first-principles CALPHAD miscibility gap V-rich"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: UKAEA PDF (Sun et al. 2025, WTaCrV)
Blocked: resolver.caltech.edu record (V-Nb, V-Ta, Nb-Ta phase equilibria) redirected to authors.library.caltech.edu; redirect not followed
Stopped: no

Query: ""Vx" NbMoTaW refractory high-entropy alloy vanadium content x=0 0.25 0.5 0.75 1 hardness yield strength"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: mdpi.com/2079-6412/15/2/120 (Zhao et al. 2025; first 100000 of 162914 characters); pub.mdi.ruhr-uni-bochum.de 42133.pdf (Xiao et al. 2022, Nb-Mo-Ta-W thin films, no V; not recorded)
Blocked: peeref.com/works/21813498 (login page only)
Stopped: no

Query: ""Designing VxNbMoTa refractory high-entropy alloys with improved properties for high-temperature applications" Scripta Materialia"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: next.sciencegate.app record (title only, no abstract)
Blocked: peeref.com/works/21539500 (login page); ncbi PMC5848905 redirected to pmc.ncbi.nlm.nih.gov, which is not on the session allowlist
Stopped: no

Query: "high-entropy alloy design raw material cost supply risk criticality metric screening refractory"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: arXiv:2409.15391v1 (full page in two parts); arXiv:2601.00852v1
Blocked: none
Stopped: no

Query: "price high purity tantalum niobium vanadium metal 99.9% per kg compared to ferroniobium V2O5 concentrate"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: cdn.asianmetal.com May 2025 Ta/Nb market report (direction of price moves only; not recorded)
Blocked: price figures subscription-only
Stopped: no

Query: "USGS Mineral Commodity Summaries 2026 vanadium pdf"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: pubs.usgs.gov mcs2026-vanadium.pdf
Blocked: none
Stopped: no

Query: "USGS Mineral Commodity Summaries 2026 niobium ferroniobium unit value pdf"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: pubs.usgs.gov mcs2026-niobium.pdf; mcs2026-tantalum.pdf
Blocked: none
Stopped: no

Query: "high-purity metal price premium over ore concentrate tantalum niobium vanadium tungsten molybdenum $/kg arc melting cost refractory alloys"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: ibm.gov.in ASP Metals June 2026 extract (prices derived from USGS MCS, form unspecified; not recorded); USGS "Metal Prices in the United States Through 1998" via UNT web archive (only first 100000 of 500000 characters read; the Nb, Ta, V, W, Mo chapters were not reached; not recorded)
Blocked: none
Stopped: no

Query: "tantalum metal ingot price 2025 per kg vs tantalite concentrate price Ta2O5"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: imarcgroup.com tantalum price index; news.metal.com SMM tantalum article
Blocked: none
Stopped: no

Query: "refractory high entropy alloys compared with Ni-based superalloys Inconel 718 Haynes 230 yield strength vs temperature density specific strength Senkov"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: link.springer.com JOM 2014 PDF (Senkov, Woodward, Miracle; abstract and front matter only); frontiersin.org Atli & Karaman 2023 (read twice; first 100000 of 105163 characters)
Blocked: springerlink.bibliotecabuap.elogim.com JMR 2018 invited review (jmr.2018.153) redirected to an institutional login page; body of the JOM 2014 paper paywalled
Stopped: no

Query: "refractory high-entropy alloys comparison C-103 TZM Ta-10W yield strength density high temperature"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: arXiv:2602.07293 (Nahin et al.)
Blocked: none
Stopped: no

Query: ""C-103" "TZM" "Ta-10W" refractory alloys density melting point yield strength 1200 °C table"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: Materion C-103 data sheet (hkvxni.files.cmp.optimizely.com)
Blocked: none
Stopped: no

Query: "NASA refractory metal alloys C-103 Ta-10W TZM properties comparison report pdf high temperature strength"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: NTRS 20205003679 (Mireles et al., AM C103; RT tensile only, wrought values in a figure not readable; not recorded); NTRS TM-20260007378 (Brizes et al. 2026, list of Nb alloys, no properties; not recorded)
Blocked: none
Stopped: no

Query: "refractory complex concentrated alloys benchmark against commercial refractory alloys C-103 TZM T-111 Ta-10W yield strength 1200 °C comparison figure"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: arXiv:1710.06983 (Singh et al.)
Blocked: none
Stopped: no

Query: "vanadium metal 99.5% price yuan/kg SMM vanadium pentoxide ferrovanadium 2026"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: metal.com price pages 202404120005 (99.5 % powdered vanadium) and 202110220002 (98 % flake V2O5)
Blocked: both price pages show values only after login or subscription
Stopped: no

Query: "Ta-10W tantalum tungsten alloy data sheet density melting point yield strength elevated temperature"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: atimaterials.com ATI Ta-10W data sheet
Blocked: none
Stopped: no

Query: "TZM molybdenum alloy data sheet density melting point yield strength 1000 °C 1200 °C"  Tool: WebSearch (standard)  Date: 2026-11-11
Opened: wieland.com TZM data sheet
Blocked: none
Stopped: yes (tool-call budget for this run reached; Q3 V-series in W-Mo-Ta-Nb-V, high-purity W/Mo/Nb/V metal prices and TZM high-temperature yield strength remain open)
```

Not opened this run (leads only, no claims made from them): Walbrühl et al. 2017 (Thermo-Calc's
SSS model paper); Thermo-Calc TCHEA Examples Collection PDF; Wang et al. 2021 Scripta Mater.
(VxNbMoTa, see run-2026-11-09 C26); USGS MCS 2026 Tungsten and Molybdenum chapters; EU CRM 2023
study (P3); MetalMiner / Canadian Mining Journal (P6); full text of Yao et al. MSEA 674 (2016)
(source of the NbTaVW value in P4).
