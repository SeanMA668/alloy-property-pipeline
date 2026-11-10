# Fact-check: run 2026-11-09 (fact-checker)

Written by the fact-checker agent, 2026-11-09. I did not write claims.md. Every source
below was opened by me with WebFetch, which returns a model-extracted reading of the page
rather than raw text; "read-directly" means the relevant passage of the full text loaded,
"abstract-only" means only an abstract or catalogue record loaded. Direct download with
curl was refused by the proxy (403) for all hosts, so no PDF was read as raw text.

## Bibliographic conflict: Senkov, Wilks, Scott & Miracle (2011)

Resolved. The AFRL preprint (DTIC ADA550865, AFRL-RX-WP-TP-2011-4289, July 2011) says it
was "submitted to the Journal of Alloys and Compounds", but it was published as
**Intermetallics 19(5) (2011) 698-706, DOI 10.1016/j.intermet.2011.01.004** (library
record bvbvf1.bib-bvb.de, cdi_proquest_miscellaneous_864436470; ISC record
manuscript.isc.ac/Inventory/10/1505012.htm gives Intermetallics 2011, pp. 698-706;
Maresca & Curtin arXiv:1901.02100v3 cite the same). The J. Alloys Compd. note is the
submission target only. The same pattern holds for P1: its AFRL preprint (ADA550824) also
says "submitted to J. Alloys Compd." but appeared in Intermetallics 18 (2010) 1758-1765.
Cite the Intermetallics versions; numbers in C1, C2, C19, C34-C36 were checked against the
preprint only (I did not open the published version).

---

## Q1

### C1 - SUPPORTED
Checked: DTIC ADA550865 preprint, full text (abstract, Sections 2, 3.2.1, Conclusions). read-directly.
Finding: Both alloys single-phase disordered BCC by neutron diffraction, as cast and after 1400 C; abstract says BCC "remained stable after exposure to 1400 °C". Anneal time is 19 h (Section 2) vs 18 h (3.2.1, Fig. 4), as the reviewer noted.

### C2 - SUPPORTED
Checked: ADA550865, Section 3.2.1. read-directly.
Finding: a = 3.220 A for NbMoTaW as cast and annealed; 3.185 A as cast vs 3.187 A annealed for VNbMoTaW.

### C3 - SUPPORTED
Checked: arXiv:2103.07951 full text (Sections 2, 4.3). read-directly.
Finding: Homogenised 1800 C / 4 days, aged 773 K / 5 weeks; synchrotron powder XRD (SLS, PSI) showed only random BCC, no superlattice peaks. Note: only angles up to 40 deg 2-theta were analysed. No journal named in the preprint.

### C4 - SUPPORTED
Checked: arXiv:2103.07951, abstract and Section 4.2. read-directly.
Finding: EAM hybrid MC/MD; ordering/SRO changes appear below about 700 K; Mo-Ta strong next-neighbour (B2-type) ordering; Nb-W least ordered and tending to segregate into patches at 100-300 K.

### C5 - SUPPORTED
Checked: figshare PDF of arXiv:1306.5043v1 (full text); also the JOM abstract page (Springer PDF link) and ADS record. read-directly (preprint); abstract-only (journal).
Finding: Tc = 1280 K (MC) and 1654 K (mean field), Mo-Ta bonding drives it, zero-K phases MoTa.oA12, NbW.cF16, TaW2.tI6, Mo3Nb4.hR7, further low-T transitions "likely ending with phase segregation into binary phases". The published JOM abstract gives no numeric Tc, so the numbers are from the preprint.

### C6 - SUPPORTED
Checked: arXiv:2211.09911v2 full text (Table II, Sec. III.B). read-directly.
Finding: VNbMoTaW 742 K, k = {1/2,1/2,1/2}, B32-like, V-dominated polarisation; NbMoTaW 559 K, B2-like; authors call mean-field values "expected to be overestimates". Bibliographic correction: search results list it as Phys. Rev. Materials 7, 013801 (2023) (DOI 10.1103/PhysRevMaterials.7.013801, ADS 2023PhRvM...7a3801W), not 2022; journal page not opened.

### C7 - SUPPORTED
Checked: arXiv:2211.09911v2, Sec. III.D and Conclusions. read-directly.
Finding: Low-T MC shows B32-like V-W regions and B2-like patches; this state "is unlikely to be experimentally observable"; SRO "may be experimentally observable given suitable heat treatment".

### C8 - SUPPORTED
Checked: pure.unileoben.ac.at record for Xia & Franz, Coatings 10(10) 941 (2020), DOI 10.3390/coatings10100941. abstract-only.
Finding: Cathodic-arc films, vacuum annealed up to 1600 C, BCC "is stable up to 1500 °C". No durations given.

### C9 - SUPPORTED
Checked: scholar.xjtu.edu.cn record of Han et al., Intermetallics 84 (2017) 153-157, DOI 10.1016/j.intermet.2017.01.007 (I opened it; the reviewer's label was search-summary). abstract-only.
Finding: TiNbMoTaW single BCC and "could sustain the phase structure even after annealing at 1200 °C for 24 h".

### C10 - SUPPORTED
Checked: jmst.org abstract page, J. Mater. Sci. Technol. 122 (2022) 243-254, DOI 10.1016/j.jmst.2021.12.057 (opened by me; reviewer label was search-summary). abstract-only.
Finding: Four alloys, 100 h anneals, all start decomposing near 500 C; single phase regained at about 900 (HfNbTiZr), 1000 (NbTiZr), 1100 (HfNbTaTiZr) and above 1300 C (NbTaTiZr). Bibliographic correction: first author is Meng Dai (Dai, Cao, Huang, ... Lu), not "P. Cao et al.".

### C11 - LEAD-ONLY
Checked: not opened. Vlasák et al., Metals (2022) is on MDPI, which is blocked here.
Finding: Remains a search-summary lead.

## Q2

### C12 - SUPPORTED
Checked: PMC7512484 full text (Gorsse & Senkov, Entropy 20(12) 899, 2018, DOI 10.3390/e20120899). read-directly.
Finding: TCHEA3: 26 elements, 294 binaries and 136 ternaries fully assessed, out of 2600 possible ternaries ("about 5%").

### C13 - SUPPORTED
Checked: PMC7512484, Sections 3-4 and Conclusions. read-directly.
Finding: Binary-only extrapolation acceptable only without binary miscibility gaps and with few or no intermetallics; lower-credibility results "may be questionable"; test systems Co-Cr-Fe-Ni, Co-Cu-Fe-Ni, Al-Co-Ni-Ti, all at 800 C.

### C14 - SUPPORTED
Checked: DTIC ADA627998 (CALPHAD 50 (2015) 32-48, DOI 10.1016/j.calphad.2015.04.009), full text. read-directly.
Finding: Pandat 8.1 with 2013 databases; no experimental comparison for NbMoTaW or NbMoTaVW; "none of the higher order alloys have full ternary assessment". Location correction: that sentence and the 65-alloy count are in Section 3.1.1, not 2.2.1; Section 4.1 says "over 50".

### C15 - SUPPORTED
Checked: ADA627998, Table 15. read-directly.
Finding: AlCrMoNbVW, PanSol, Tm 1915 C, BCC + BCC at 600 C.

### C16 - SUPPORTED
Checked: home.iitm.ac.in PDF of Shaikh et al., Intermetallics 127, 106926 (2020), Section 3.1. read-directly.
Finding: TCHEA v2.1 liquidus 3138 K (MoNbTaW) and 2976 K (MoNbTaWV) vs ROM 3158 K and 2963 K. The paper states no experimental liquidus exists for RHEAs.

### C17 - SUPPORTED
Checked: Shaikh et al., Table 2. read-directly.
Finding: The source does list 13.64 / 12.36 (exp.) and 13.8 / 12.44 (CALPHAD), citing Senkov 2010. Caution: Senkov 2010 itself reports a measured 13.75 g/cm3 for the quaternary (see P1), about 0.8 % above its rule-of-mixtures value; Shaikh's Table 2 appears to swap the experimental (13.75) and ROM (about 13.64) values for MoNbTaW. Do not use 13.64 as a measured density.

### C18 - SUPPORTED
Checked: OSTI 1989196 report (abstract and main text). read-directly.
Finding: NbTaTiW and MoNbTaTi; TCHEA4 + MOBHEA2; Scheil "accurately predict the observed solidification segregation"; DICTRA "predicts general trends". The 1673 K (35 h) condition is in the main text, not the abstract.

### C19 - SUPPORTED
Checked: ADA550865, Section 3.2.2. read-directly.
Finding: Dendritic structure, dendrite arm thickness "~ 20-30 µm" in both alloys.

### C20 - SUPPORTED
Checked: opact.sdu.edu.tr catalogue record of Yao et al., MSEA 674 (2016) 203-211, DOI 10.1016/j.msea.2016.07.102. abstract-only (abstract partly truncated).
Finding: "The observed elemental segregation in each alloy qualitatively agrees with CALPHAD prediction."

### C21 - LEAD-ONLY
Checked: tried aminer.org (homepage shell only) and bohrium (redirect, not followed). Not opened.
Finding: Remains a lead.

### C22 - LEAD-ONLY
Checked: not attempted (budget).
Finding: Remains a lead.

## Q3

### C23 - SUPPORTED
Checked: uknowledge.uky.edu/cme_facpub/123 (Tuhser et al., JMRT 35 (2025), DOI 10.1016/j.jmrt.2025.02.011). abstract-only.
Finding: Broad single-BCC space, "comparable hardness", Mo-to-Nb replacement most effective in thin film and bulk tests; fragmentation set VNbMoTaW, VNb2TaW, VNbMoTa2, V2NbTaW, V2NbMoTa.

### C24 - SUPPORTED
Checked: PMC7512564 full text (Zheng & Wang, Entropy 20(12) 965, 2018, DOI 10.3390/e20120965). read-directly.
Finding: 70 compositions; Mo + W raise moduli; V raises B/G and Poisson ratio; Nb and Ta small effects; all mechanically stable; no experimental VMoNbTaW data. Note: all B/G values in Table 3 exceed 2, so the Pugh-ductility reading is relative only.

### C25 - SUPPORTED
Checked: opact.sdu.edu.tr record (as C20). abstract-only.
Finding: As-cast ingots single BCC; NbTaTiVW yield 1420 MPa, fracture strain 20 %.

### C26 - LEAD-ONLY
Checked: peeref.com record returned a login page. Not opened.
Finding: Remains a lead.

## Q4

### C27 - SUPPORTED
Checked: par.nsf.gov record of Wang, Zhong, Zhao, J. Alloys Compd. 915, 165173 (2022). abstract-only.
Finding: 2436 Al-Co-Cr-Cu-Fe-Mn-Ni quinaries; VEC most important; single BCC/B2 at VEC < 6.87, single FCC at VEC > 9.16; BCC and B2 form one class.

### C28 - PARTIAL
Checked: par.nsf.gov record (as C27). abstract-only.
Finding: External test 81.8 % on 66 SS alloys is right, but the abstract gives a single cross-validation accuracy of 89.1 % (three-class); "roughly 89-93 %" is not in what loaded.
Corrected claim: The trained ANN predicted 66 external experimental solid-solution alloys with 81.8 % accuracy, against 89.1 % cross-validation accuracy for the BCC/B2, BCC/B2+FCC and FCC classes.

### C29 - PARTIAL
Checked: arXiv:2503.21146 full text. read-directly.
Finding: The 42 is the count of database compositions "that had BCC phase", not shown to be single-BCC; the misclassifications are of new test alloys (Table 4, nos. 7, 8, 10), all labelled BCC+BCC in Table 4 although the text says BCC+BCC and BCC+B2. Reason given: "fewer data with similar phases in the database" (2 BCC+BCC, 13 BCC+B2 entries). The data are Al-containing RHEAs from Couzinié et al.; features are composition and processing only.
Corrected claim: A composition-based classifier for Al-containing RHEAs (Couzinié et al. data) predicted the single-BCC test alloys correctly but misclassified three multi-phase test alloys, which the authors attribute to scarce mixed-phase training data (2 BCC+BCC and 13 BCC+B2 entries).

### C30 - SUPPORTED
Checked: arXiv:2211.09911v2, Sec. III.D. read-directly.
Finding: Mo-W and Nb-Ta "disfavored as nearest neighbours"; Nb-W, Mo-Ta, Nb-Mo, Ta-W favoured; second-neighbour V-W "highly favored".

### C31 - LEAD-ONLY
Checked: not opened (reviewer's OSTI record had metadata only; I did not retry).
Finding: Remains a lead.

### C32 - LEAD-ONLY
Checked: not attempted (Crystals is MDPI, blocked).
Finding: Remains a lead.

### C33 - LEAD-ONLY
Checked: not attempted (budget).
Finding: Remains a lead.

## Q5

### C34 - SUPPORTED
Checked: ADA550865, Table 2. read-directly.
Finding: Yield 1058, 561, 552, 548, 506, 421, 405 MPa at 23-1600 C, matching the claim.

### C35 - SUPPORTED
Checked: ADA550865, Table 3. read-directly.
Finding: Yield 1246, 862, 846, 842, 735, 656, 477 MPa at 23-1600 C, matching the claim.

### C36 - SUPPORTED
Checked: ADA550865, abstract, Sections 3.1.1, 3.1.2, 3.2.3, Conclusions (second targeted read). read-directly.
Finding: Both failed "by splitting" with "Brittle quasi-cleavage fracture"; DBTT "above room temperature". Strain values are inconsistent in the source: NbMoTaW 2.1 % (text), 2.6 % (Table 2 footnote), about 2 % (Conclusions); VNbMoTaW 1.7 % (text, Table 3) but "about 1%" in Conclusions.

### C37 - SUPPORTED
Checked: koasas.kaist.ac.kr record of Kang et al., MSEA 712 (2018) 616-624, DOI 10.1016/j.msea.2017.12.021. abstract-only.
Finding: 6 h MA, SPS 1500-1700 C, 2612 MPa and 8.8 % for the 1500 C sample, homogeneous BCC matrix with a small amount of oxide inclusions.

### C38 - SUPPORTED
Checked: koasas record (as C37). abstract-only.
Finding: Grain-boundary, substitutional and interstitial solid-solution, and Orowan (oxide) strengthening named.

### C39 - SUPPORTED
Checked: PMC5978046 full text (Long et al., Materials 11(5) 669, 2018, DOI 10.3390/ma11050669). read-directly.
Finding: 2709 MPa, 11.4 %, 1.35 um grains, 0.86 wt% O after 40 h milling, TiO 16.1 vol%; TiO size 0.64 um (Sec. 3.1) vs 0.46 um (Conclusions).

### C40 - SUPPORTED
Checked: arXiv:1901.02100v3 full text. read-directly.
Finding: "no adjustable parameters"; good RT agreement; predictions "lower than experiments" at high T; plateau 900-1300 K "not predicted by the theory" (Appendix C gives 800-1100 K).

### C41 - PARTIAL
Checked: arXiv:1901.02100v3, Appendix B. read-directly.
Finding: Factors listed are right, but the MoNbTaV dendrite-interdendrite difference is given as 158 MPa (dendrite also 78 MPa weaker than the average composition), not "of order 100 MPa"; the Hall-Petch estimate of about 50 MPa is for 80-200 um as-cast grains.
Corrected claim: Maresca and Curtin list O and N impurities, cast dendritic microstructure (dendritic regions 158 MPa stronger than interdendritic regions in MoNbTaV) and a Hall-Petch contribution of about 50 MPa for 80-200 um grains as factors that can raise measured strength above the intrinsic prediction.

### C42 - SUPPORTED
Checked: scholar.xjtu.edu.cn record (as C9). abstract-only.
Finding: About 586 and 659 MPa at 1200 C; Ti "significantly" enhances RT yield strength and compressive plastic strain. Baseline values not in abstract.

---

## Project statements

### P1 - PARTIAL
Checked: DTIC ADA550824 (AFRL-RX-WP-TP-2011-4295, preprint of the same paper) full text; ISC record manuscript.isc.ac/Inventory/10/1504786.htm (Intermetallics 2010, pp. 1758-1765, authors Senkov, Wilks, Miracle, Chuang, Liaw). read-directly (preprint).
Finding: Both alloys single-phase BCC in the as-cast condition (synchrotron XRD); no anneal. But they were near-equiatomic, not equiatomic: measured at.% W27.3 Nb22.7 Mo25.6 Ta24.4 and W21.1 Nb20.6 Mo21.7 Ta15.6 V21.0. Missing reflections in the quaternary were tentatively attributed to possible ordering. Densities 13.75 and 12.36 g/cm3; a = 3.2134 and 3.1832 A; HV 4455 and 5250 MPa.
Corrected claim: Senkov et al., Intermetallics 18 (2010) 1758-1765: near-equiatomic W-Nb-Mo-Ta and W-Nb-Mo-Ta-V (arc-melted, as cast) are single-phase BCC.

### P2 - PARTIAL
Checked: Springer abstract page (s11837-013-0772-3) and ADS 2013JOM....65l1772H; preprint arXiv:1306.5043v1 (as C5). abstract-only (journal), read-directly (preprint).
Finding: The content is right (first-principles effective Hamiltonian predicts B2 ordering, Mo-Ta driven), but the first author is Huhn, not Widom.
Corrected claim: Huhn & Widom, "Prediction of A2 to B2 phase transition in the high-entropy alloy Mo-Nb-Ta-W", JOM 65 (2013) 1772-1779, DOI 10.1007/s11837-013-0772-3.

### P3 - PARTIAL
Checked: NIST materialsdata record of Pavlů et al., "Ta-V thermodynamic modeling of Laves phases", Calphad 35(1) (2011) 103-108, DOI 10.1016/j.calphad.2010.12.002. abstract-only. (PMC8950179, a 2022 third-generation Ta-V assessment, was not on the allowlist.)
Finding: Ta-V has Laves phases: C15 "most stable ... at intermediate temperatures", C14 at 0 K and high temperature. The stoichiometry (TaV2 / V2Ta) is not stated in what loaded.
Corrected claim: The Ta-V binary has a Laves phase (C15 at intermediate temperatures, C14 at high temperatures; Pavlů et al., Calphad 35 (2011) 103); the V2Ta stoichiometry is not verified here.

### P4 - SUPPORTED
Checked: matminer 0.10.1, matminer.utils.data.MixingEnthalpy (data file MiedemaLiquidDeltaHf.tsv; docstring cites Takeuchi & Inoue, Mater. Trans. 46, 2817-2829 (2005)), read with python3. repository. The original paper was not opened; HEACalculator (arXiv:2606.19661) confirms the citation details.
Finding: All ten pairs match: W-Ta -7, W-Nb -8, Mo-Ta -5, Mo-Nb -6, W-Mo 0, Mo-V 0, Ta-Nb 0, W-V -1, Ta-V -1, Nb-V -1 kJ/mol. This is a check against matminer's copy of the table, not against the paper.

### P5 - UNREACHABLE
Checked: tried bohrium.com (WAF challenge), scinapse/peeref (captcha/login); original not opened. A secondary source, HEACalculator (Sarıtürk, Kalay, Arróyave, arXiv:2606.19661, read-directly), states the criterion Ω ≥ 1.1 and δ ≤ 6.6 % and cites Yang & Zhang, Mater. Chem. Phys. 132 (2012) 233-238, DOI 10.1016/j.matchemphys.2011.11.021.
Finding: Consistent with P5 per a citing source, but the original was not read; not a pass.

### P6 - SUPPORTED
Checked: core.ac.uk/download/61022332.pdf (Guo, Ng, Lu, Liu, J. Appl. Phys. 109, 103505 (2011)) full text. read-directly.
Finding: Conclusions: bcc stable at "lower VEC (< 6.87)"; mixed fcc+bcc for 6.87 <= VEC < 8; fcc for VEC >= 8 (inequality signs garbled in the extracted text, read from context). Note the rule was built on Al-containing 3d-metal systems (AlxCoCrCuFeNi etc.) and separates FCC from BCC; it says nothing about stability within all-BCC alloys.

### P7 - SUPPORTED
Checked: oskar-bordeaux.fr record of Borg et al., Sci. Data 7, 430 (2020), DOI 10.1038/s41597-020-00768-9 (nature.com not on allowlist). abstract-only.
Finding: Mechanical properties for "630 multi-principal element alloys", with microstructure/observed phases recorded. The record does not say whether 630 counts entries or distinct compositions.

---

## Verdict counts

Claims C1-C42: SUPPORTED 32, PARTIAL 3 (C28, C29, C41), UNSUPPORTED 0, UNREACHABLE 0, LEAD-ONLY 7 (C11, C21, C22, C26, C31, C32, C33).

Project statements P1-P7: SUPPORTED 3 (P4 repository, P6, P7), PARTIAL 3 (P1, P2, P3), UNSUPPORTED 0, UNREACHABLE 1 (P5).

Bibliographic corrections outside the verdicts: Senkov et al. 2011 is Intermetallics 19(5) 698-706; C6 is Phys. Rev. Materials 7, 013801 (2023); C10 first author is Meng Dai; C17's 13.64 g/cm3 "measured" density conflicts with Senkov 2010 (13.75).
