# Fact-check: run 2026-11-11

Fact-checker, 2026-11-11. I re-opened every cited source myself with WebFetch, which returns a
model-extracted reading of the page, not the raw text. "read-directly" means the relevant passage of
the full text, full preprint, full report or data sheet was in what loaded. "abstract-only" means
only an abstract or abstract-level record loaded. I did not rely on the quotes in `claims.md`.

Notes on what counts as the source:
- Senkov et al. Intermetallics 19 (2011) 698-706: I could not open the published article. A library
  record (bvbvf1.bib-bvb.de, Primo) confirms the bibliographic data: O.N. Senkov, G.B. Wilks,
  J.M. Scott, D.B. Miracle, Intermetallics 19(5) 698-706 (2011), doi:10.1016/j.intermet.2011.01.004.
  The numbers were checked against the same authors' preprint AFRL-RX-WP-TP-2011-4289 (DTIC
  ADA550865, July 2011), which has the same title. The preprint says it was submitted to J. Alloys
  Compd., not Intermetallics. So the published text may differ from the preprint.
- AFRL-RX-WP-TP-2011-4295 (DTIC ADA550824): the report documentation page carries an unrelated
  title ("The Duality of Fracture Behavior in a Ca-Based Bulk-Metallic Glass"). The paper body is
  "Refractory High-Entropy Alloys" by Senkov, Miracle, Wilks, Chuang and Liaw, as cited.

Reviewer flags D1-D6, resolved where I could:
- D1 (470 vs 477 MPa at 1600 C): confirmed. The 4289 text says "862 to 470 MPa" and Table 3 gives
  477 MPa. Atli & Karaman Table 1 gives 477 MPa (cites Senkov 2011). Not resolvable from the sources.
- D2 (19 h vs 18 h): confirmed. Section 2 says 19 h; Section 3.2.1 and the Fig. 4 caption say 18 h.
- D3 (Mo in W-Nb-Mo-Ta dendrites): confirmed. Table 4 gives Mo -1.7 at.% in dendrite arms and the
  Results text agrees ("depleted with Nb and Mo"). The Conclusions say "enriched with W and Mo".
  Table 4 and the Results text agree with each other, so the Conclusions sentence is the odd one out.
- D4 (3.2036 vs 3.208 A): confirmed. The body gives 3.2036 A and the abstract gives 3.208 A.
- D5 (MoNbTaV "annealed"): resolved against the project. Yao et al. report arc melting with at least
  seven remelts and no anneal or homogenisation of MoNbTaV, and call the tested material as-cast.
  The only anneal in the paper is Senkov's MoNbTaW comparison sample (1400 C, 19 h). The 1525 MPa
  number is in the paper: Table 1 lists sigma0.2 = "333/1525" MPa (calculated/experimental) for
  MoNbTaV, in the second half of the page (characters 100000-193754), which the reviewer did not
  read. The number is right; the "annealed" label is wrong.
- D6 (Senkov "homogenised"): resolved, with a further finding. Section 2 of the 4289 preprint
  applies the 1400 C / 19 h anneal only to the neutron-diffraction samples ("as-cast and annealed
  (1400°C for 19 hours) conditions"). The compression specimens were "electric-discharged machined
  from the cast buttons", and no heat treatment of them is described. So the 1058 and 1246 MPa
  room-temperature yield strengths are as-cast values. The paper gives no stated purpose for the
  anneal; Section 3.2.1 uses it to show the BCC phase "is stable upon heating at least up to
  1400°C". No compositional measurement after the anneal is reported. One secondary source,
  Yao et al. (Entropy 2016), calls this MoNbTaW "the homogenized MoNbTaW alloy". That is Yao's
  wording, not Senkov's.

New inconsistency found: the 4289 preprint gives the room-temperature failure of Nb25Mo25Ta25W25
as "failed by splitting at εp = 2.1%" in the text, but the extraction reported a fracture strain of
2.6 % in Table 2. I have not checked the table image.

---

## Claims

### C1 - SUPPORTED
Checked: arXiv:1901.02100v3 (Maresca & Curtin, revised 13 June 2019), full PDF; Section 4 paragraph on Fig. 5, Section 6. Access: read-directly.
Finding: Section 4 says "the alloy with V is comparatively stronger because V has the largest misfit volume and so is the most potent strengthener". Section 6 also cites combinations of small and large elements (V and Ta) and stiff elements (W), as the claim's "Not claimed" notes. I did not open the published Acta Mater. version.

### C2 - PARTIAL
Checked: arXiv:1901.02100v3, Appendix B (read twice, asking specifically for the region pairing). Access: read-directly.
Finding: The theory does underpredict MoNbTaV ("may explain why the theory underpredicts the measured strength in MoNbTaV, although the predictions remain quite reasonable"). The extraction gave the numbers paired differently from the claim: "the dendritic region is 158 MPa stronger than the interdendritic composition, and 78 MPa weaker than the average composition". The claim instead says dendritic is 158 MPa stronger and interdendritic 78 MPa weaker than the average. My reading is model-mediated, so check the PDF before using either number.
Corrected claim: Maresca and Curtin's theory underpredicts the measured strength of MoNbTaV, which they consider still "quite reasonable". Appendix B attributes part of the gap to dendritic segregation and gives composition-dependent strength differences of 158 MPa and 78 MPa. The pairing as read here is: dendritic 158 MPa stronger than interdendritic; the pairing must be confirmed against the PDF before the numbers are used.

### C3 - PARTIAL
Checked: arXiv:1901.02100v3, Fig. 5 caption and Section 4 paragraph. Access: read-directly.
Finding: The text reports "very good agreement between predictions for the Mo-Nb-Ta-V-W alloys studied experimentally to date at T=296K", with no adjustable parameters. In that passage it does not name MoNbTaW or MoNbTaVW individually. The Fig. 5 caption cites the NbTaV-(Ti,W) paper (Ref. [3]) only as a source of the experimental strain rate. The text does not say which alloys are plotted, so "shows NbTaV-(Ti,W) data in the same figure" cannot be confirmed from the text.
Corrected claim: Maresca and Curtin report very good, parameter-free agreement with measured 296 K yield strengths for "the Mo-Nb-Ta-V-W alloys studied experimentally to date" (Fig. 5). The Fig. 5 caption cites Yao et al.'s NbTaV-(Ti,W) paper among its experimental sources, but the text does not identify the plotted alloys or give numbers.

### C4 - SUPPORTED
Checked: Yao et al., Entropy 18(5) 189 (2016), doi:10.3390/e18050189, mdpi.com page; both halves read (0-100000 and 100000-193754). Access: read-directly.
Finding: The abstract says "a simple model on solid solution strengthening predicts a yield strength of approximately 1.5 GPa". The model is explicitly "the classical Labush [sic] approach". The measured value is 1.5 GPa in Section 3.3 and 1525 MPa in Table 1. The material is as-cast. There is no "Section 4.3" heading; the model is in Section 4.

### C5 - SUPPORTED
Checked: Yao et al. (as C4), Section 3.3. Access: read-directly.
Finding: Section 3.3 says the properties "do not obey the simple ROM" and that "aspects of solid solution strengthening (SSS) may play a more dominant role". It suggests the "much refined grain sizes in the as-cast state" compared with "the homogenized MoNbTaW alloy [22]" may contribute. This is presented as a possibility.

### C6 - SUPPORTED
Checked: Thermo-Calc help, "About the Yield Strength Property Model" (2025b URL), solid solution strengthening section. Access: read-directly.
Finding: The page says "The model by Walbrühl et al. [2017Wal] is implemented". The result is "normalized with respect to the sum of all mole fractions for FCC, BCC, and HCP", and one option uses equilibrium phase fractions and compositions. Labusch, Varvenne, Maresca and Curtin do not appear on the page. The page itself states no version number.

### C7 - SUPPORTED
Checked: the TCHEA yield-strength validation page and the PM_G_06 example page. Access: read-directly.
Finding: Both pages show only the Mo-Ta BCC binary. The validation page compares against [2017Wal]. PM_G_06 uses TCHEA and compares against Stephens & Witzke 1972 data at 300 K and 411 K. No W-Mo-Ta-Nb-V alloy appears.

### C8 - SUPPORTED
Checked: opact.sdu.edu.tr Summon record for Yao et al., MSEA 674 (2016) 203-211, doi:10.1016/j.msea.2016.07.102 (authors H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang confirmed). Access: abstract-only (truncated summary).
Finding: The record gives yield strengths about 3.5-4.4 times the rule-of-mixture estimates, and NbTaTiVW at 1420 MPa with 20 % fracture strain. It gives no NbTaVW yield strength.

### C9 - SUPPORTED
Checked: DTIC ADA550824 (AFRL-RX-WP-TP-2011-4295), full preprint. Access: read-directly.
Finding: Hv is 4455 and 5250 MPa, rule-of-mixture values are 1841 and 1596 MPa, and the paper says "The higher microhardness in Alloy2 is probably due to a finer grain structure". The alloys were studied "in the as-cast condition".

### C10 - SUPPORTED
Checked: ADA550824, Table 1, Table 4, Results text, Conclusions. Access: read-directly.
Finding: The measured composition is 27.3W-22.7Nb-25.6Mo-24.4Ta. Dendrite arm minus average is W +3.9, Nb -2.5, Mo -1.7, Ta +0.3. The Conclusions contradict this on Mo (D3), as the claim notes.

### C11 - SUPPORTED
Checked: ADA550824, Table 1 and Table 5. Access: read-directly.
Finding: The measured composition is 21.1W-20.6Nb-21.7Mo-15.6Ta-21.0V. Dendrite: W +4.7, Ta +1.1, V -4.0, Nb -1.7. Interdendritic: V +6.3, Nb +2.6, W -7.3. Mo is near zero (-0.2 / +0.4) and interdendritic Ta is -2.0; neither is mentioned in the claim.

### C12 - SUPPORTED
Checked: Yao et al. (as C4), Section 3.1. Access: read-directly.
Finding: Section 3.1 says "The dendrite arms are enriched with Ta and Mo, while the interdendritic regions are enriched strongly with V", and Nb "deviates little from the bulk concentration".

### C13 - SUPPORTED
Checked: Yao et al. (as C4), Section 2, Section 3.3, Conclusions, Table 1 (full page). Access: read-directly.
Finding: Processing was arc melting and at least seven remelts; no anneal is reported. The tested material is called as-cast. High-temperature homogenisation and temperature-dependent testing are "beyond the scope of the present study".

### C14 - PARTIAL
Checked: DTIC ADA550865 (AFRL-RX-WP-TP-2011-4289), Section 2, Section 3.2.1, Fig. 4 caption, Section 3.2.4; asked specifically about post-anneal composition. Access: read-directly.
Finding: The 1400 C / 19 h (18 h in Section 3.2.1 and Fig. 4) anneal, the "annealed" wording, the lack of a stated purpose, and the lack of any post-anneal segregation measurement are all confirmed. The claim omits that the anneal was applied only to the neutron-diffraction samples. The compression specimens were machined from the cast buttons. Section 3.2.1 uses the annealed samples to show phase stability up to 1400 C.
Corrected claim: Senkov et al. annealed neutron-diffraction samples of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 at 1400 C for 19 h (18 h in Section 3.2.1 and Fig. 4) and use them to show that the BCC phase is stable up to 1400 C. They state no other purpose and report no compositional measurement after the anneal. The compression specimens were machined from the as-cast buttons and were not annealed.

### C15 - SUPPORTED
Checked: ADA550865, Section 3.2.4. Access: read-directly.
Finding: Section 3.2.4 says "Even dynamic recrystallization was not able to remove the compositional inhomogeneity", referring to samples deformed at 1400 C.

### C16 - SUPPORTED
Checked: arXiv:2103.07951 (Bajpai, Maiti, Mishra, Rai), Experiments section. Access: read-directly.
Finding: The paper says "annealed in 1800°C first for homogenization annealing for 4 days", followed by 500 C for 5 weeks. The anneal atmosphere is not stated (Ar only for arc melting), and no post-anneal homogeneity check is reported.

### C17 - SUPPORTED
Checked: OSTI 1989196 (Puerling et al., NSC-614-4990, 01/2023), Table 2 and text. Access: read-directly.
Finding: The experimental core/interdendritic values are W 27.2/9.1, Ta 24.5/14.1, Ti 26.0/52.3 and Nb 22.3/24.3 at.%. The sentence "dendrite cores are Mo, Ta, and W-rich, while the interdendritic regions are Nb and Ti-rich" is confirmed.

### C18 - PARTIAL
Checked: OSTI 1989196, heat-treatment text and Tables 4-5. Access: read-directly.
Finding: The heat treatment is confirmed: "heat treated under vacuum at 1673K for 35 h in an attempt to achieve homogenization". After it, NbTaTiW core/interdendritic was Ta 27.9/23.9 and W 29.1/23.5, and MoNbTaTi Ta was 33.5/25.5. DICTRA with MOBHEA2 "predicts faster diffusion" than observed. The authors present the Ta-diffusivity explanation as a hypothesis, not a firm attribution. "Near-complete homogenisation" was not confirmed in the wording I read.
Corrected claim: After 35 h at 1673 K under vacuum, NbTaTiW and MoNbTaTi still showed residual segregation (Ta, and W in NbTaTiW, remained core-enriched). DICTRA with MOBHEA2 predicted faster homogenisation than observed, and the authors hypothesise that this is due to the Ta diffusivity in the mobility database.

### C19 - SUPPORTED
Checked: arXiv:2306.05711 (Duan et al.; MSEA 871 (2023) 144923), Section 3.1, Table 1. Access: read-directly.
Finding: The 1400 C / 12 h anneal with furnace cooling "did not result in chemical homogeneity". The subsequent 1000 C / 12 h anneal with quenching "did not homogenize the RHEA either". HPT produced chemical homogeneity. Zr is 8.8 vs 43.8 at.%. Only the second step was quenched.

### C20 - SUPPORTED
Checked: par.nsf.gov 10178918 (Lee et al., Acta Mater. 160 (2018) 158-172), Section 3.2. Access: read-directly.
Finding: Section 3.2 says "The dendrite is enriched in Nb and Ta, while Ti and V are more preferentially distributed in the interdendritic region".

### C21 - SUPPORTED
Checked: ADA550824, Table 2. Access: read-directly.
Finding: Calculated/experimental density is 13.64/13.75 (Alloy 1) and 12.36/12.36 g/cm3 (Alloy 2). Measured lattice parameters are 3.2134 and 3.1832 A.

### C22 - SUPPORTED
Checked: ADA550865, Section 3.1.3 and Table 3. Access: read-directly.
Finding: The text gives "decreases from 862 to 470 MPa" for the V alloy and "561 to 405 MPa" for the V-free alloy. Table 3 gives 477 MPa at 1600 C (D1).

### C23 - SUPPORTED
Checked: ADA550865, Sections 3.1.1-3.1.2. Access: read-directly.
Finding: The text says "failed by splitting at εp = 2.1%" (Nb25Mo25Ta25W25) and "failed at εp = 1.7% by splitting" (V20Nb20Mo20Ta20W20). Table 2 may list 2.6 % fracture strain for the former (see the new inconsistency above).

### C24 - SUPPORTED
Checked: pure.bit.edu.cn record, Wang, Ma, Xu, Cheng, MSEA 808, 140848 (2021), doi:10.1016/j.msea.2021.140848. Access: abstract-only.
Finding: The abstract says "both the yield strength and ductility of VxNbMoTa are greatly improved when increasing the V concentration". It attributes this to solid-solution strengthening, grain refinement and fewer grain-boundary impurities and brittle compounds. Higher-V alloys show weaker strain hardening at 800 and 1000 C.

### C25 - SUPPORTED
Checked: mdpi.com Coatings 15(2) 120 (2025), doi:10.3390/coatings15020120, Introduction (first 100000 of 162914 characters). Access: read-directly.
Finding: The Introduction says "while the addition of vanadium enhanced the high-temperature strength, it sacrificed the alloy's plasticity and toughness" [18], where [18] is Senkov et al., Intermetallics 2011. This is a secondary statement.

### C26 - SUPPORTED
Checked: UKAEA PDF of Sun et al., Acta Mater. 299 (2025) 121435, Section 3.3 and Conclusions. Access: read-directly.
Finding: The paper says "a high concentration of V is generally associated with lower ODTTs" and that the system "phase separates in domains rich in CrV and WTa at low temperatures".

### C27 - SUPPORTED
Checked: arXiv:2409.15391v1 HTML, Sections 2.1, 2.3 and Table 1 (first 100000 of 146464 characters). Access: read-directly.
Finding: The index has "four groups with twelve indicators at the elemental level" and the alloy value is a weighted mean. The system is Mo-Nb-Ti-V-W, and the other objectives are yield strength, ductility (Pugh ratio and Cauchy pressure), thermal conductivity and density.

### C28 - SUPPORTED
Checked: arXiv:2409.15391v1 (as C27). Access: read-directly.
Finding: The paper says "the average yield strength is very similar across all scenarios". Cost is not an objective and appears only in a post-hoc plot "based on pure elemental raw material price". The paper says "cost tends to be a lagging indicator".

### C29 - SUPPORTED
Checked: arXiv:2601.00852v1 (Nominé, ..., Cvelbar, Zavašnik). Access: read-directly.
Finding: The paper assesses 30,201 equimolar HEAs using HHI, ESG, companionability/by-product dependence, production, reserves, and CO2/energy footprint. The resilient shortlist is "approximately 5%" (1,556 HEAs). Prices are not used, production data come from USGS MCS 2022, and no date is stated.

### C30 - SUPPORTED
Checked: USGS MCS 2026 Vanadium PDF, salient statistics, footnote 6, narrative. Access: read-directly.
Finding: The V2O5 price row reads 8.17 9.29 7.50 5.44 5.02 $/lb. Footnote 6: "Chinese annual average V2O5 prices (98% V2O5 content)". The narrative gives ferrovanadium (78-82 % V) at $14.14/lb in 2025. The 2025 values are estimates.

### C31 - SUPPORTED
Checked: USGS MCS 2026 Vanadium, mine production table and page units line. Access: read-directly.
Finding: China produced 82,000 and the world 110,000 (rounded) in 2025e. The units line reads "(Data in metric tons, vanadium content, unless otherwise specified)". "(thousand metric tons)" applies to reserves only.

### C32 - SUPPORTED
Checked: USGS MCS 2026 Niobium PDF, salient statistics, footnote 5, production table. Access: read-directly.
Finding: Ferroniobium unit value is $26/kg in 2025. Footnote 5 defines it as the "weighted average unit value of gross weight of U.S. ferroniobium trade". Brazil produced 104,000 t and the world 112,000 t (Nb content, 2025e), and the text gives Brazil "approximately 93%".

### C33 - SUPPORTED
Checked: USGS MCS 2026 Tantalum PDF. Access: read-directly.
Finding: Tantalite is 158 196 170 167 180 $/kg Ta2O5 content (2025e; source Asian Metal). The chapter gives no tantalum metal price.

### C34 - SUPPORTED
Checked: SMM article, 27 Feb 2026. Access: read-directly.
Finding: The article gives "China landed price reaching $160–165 per pound", 99.5 % oxide at 3,900 yuan/kg, 99.95 % ingot at 5,500 yuan/kg, and offers up to 6,000 yuan/kg. The ore grade and basis are not stated.

### C35 - SUPPORTED
Checked: IMARC page, 18 Feb 2026. Access: read-directly.
Finding: USA Q4 2025 is USD 502/kg, +5.46 % QoQ. No product form or purity is given for the US price.

### C36 - SUPPORTED
Checked: arXiv:2602.07293 (Nahin, Pustelnik, Dong, Zakia, Zhang). Access: read-directly.
Finding: A design criterion reads: "Presumed density and cost of the alloy were lower than those for C-103, which is 8.85 g/cm3 and $500/kg". No source is given for $500/kg.

### C37 - SUPPORTED
Checked: ADA550865, Section 3.1.3. Access: read-directly.
Finding: The paper says "much higher than that of Haynes 230 at all studied temperatures" and "higher than that of Inconel 718 at temperatures above 800°C".

### C38 - SUPPORTED
Checked: ADA550865, Section 3.1.3. Access: read-directly.
Finding: Inconel 718 YS "exceeds 1000 MPa at temperatures up to 650°C", "rapidly decreases to 138 MPa" at 982 C, and "melting occurs at ~1210°C". Haynes 230 is "~255-275 MPa, in the temperature range from 540°C to 870°C".

### C39 - SUPPORTED
Checked: Frontiers, Atli & Karaman (2023), doi:10.3389/ftmal.2023.1135826, Table 1 and caption, Section 3.1.1 (first 100000 of 105163 characters). Access: read-directly.
Finding: Inconel 718 is 8.22 g/cm3 with 105 MPa at 1200 C. CMSX-4 is 8.70 g/cm3 with 420 MPa at 1094 C and 146 MPa at 1204 C. The caption calls these "Tensile properties", and the RHEAs were tested in compression. Section 3.1.1 also cites 130 MPa at 1000 C for Inconel 718.

### C40 - SUPPORTED
Checked: Atli & Karaman Table 1. Access: read-directly.
Finding: MoNbTaW is 13.64 g/cm3 with 506/421/405 MPa. MoNbTaVW is 12.35 g/cm3 with 735/656/477 MPa (1200/1400/1600 C). Testing was in compression at 0.001 s-1, and the values are cited to Senkov et al. 2011.

### C41 - SUPPORTED
Checked: Atli & Karaman Section 3.1.3. Access: read-directly.
Finding: The review says MoNbTaW and MoNbTaVW "do not possess SYS values as high as the medium-density RHEAs due to their relatively high densities".

### C42 - SUPPORTED
Checked: Materion DS-AM-622 (dated 6.21.2024). Access: read-directly.
Finding: The sheet gives 8.850 g/cm3, 2350 C, and 0.2 % YS of 38 ksi (262 MPa) at 25 C and 16 ksi (110 MPa) at 1093 C. Values are labelled "Typical" and "for reference purposes only".

### C43 - SUPPORTED
Checked: ATI Ta-10W data sheet (dated 5/13/13; "v5" appears only in the URL). Access: read-directly.
Finding: The sheet gives 16.9 g/cm3 and 3035 C. Recrystallized sheet YS is 70,000-89,000 psi (RT), 22,300-28,300 (2600 F), 10,500-12,300 (3000 F) and 9,400 (3500 F). Stress-relieved sheet is 55,100 psi (2000 F) and 34,700 psi (2400 F). Values are typical.

### C44 - SUPPORTED
Checked: Wieland Duro TZM data sheet. Access: read-directly.
Finding: The sheet gives density 10.2 g/cm3 and "Yield strength N/mm² 750–900" (reference values, no temperature or condition). Elevated-temperature data are only a tensile-strength graph (stress-relieved and recrystallized sheet, 273-2073 K). No numeric melting point is given.

### C45 - SUPPORTED
Checked: arXiv:1710.06983 (Singh et al.). Access: read-directly.
Finding: The paper says "Typical refractory high-entropy alloys exhibit a yield strength of 500-700 MPa at 1200°C, surpassing Ni-based superalloys". TZM is compared only on Young's modulus versus temperature (Fig. 6c).

### C46 - PARTIAL
Checked: Springer PDF, Senkov, Woodward, Miracle, JOM 66(10) 2030-2042 (2014), doi:10.1007/s11837-014-1066-0. Access: abstract-only.
Finding: The abstract gives densities of 6.9-9.1 g/cm3 and σ0.2 of 1280-2035 MPa, but does not state the test temperature for that range. It says "some" of the alloys show considerably improved high-temperature strengths relative to advanced Ni-based superalloys, not all six.
Corrected claim: Six Al-containing refractory HEAs had densities of 6.9-9.1 g/cm3 and compressive yield strengths of 1280-2035 MPa (test temperature not stated in the abstract; presumably room temperature). Some of them are described as having considerably improved high-temperature strength relative to advanced Ni-based superalloys.

---

## Project statements

### P1 - SUPPORTED
Checked: USGS MCS 2026 Vanadium PDF (as C30-C31). Access: read-directly.
Finding: The 2025 average Chinese V2O5 (98 % V2O5) price is $5.02/lb. China mine production was 82,000 t of a world total of 110,000 t (V content). The 2025 values are USGS estimates ("2025e").

### P2 - SUPPORTED
Checked: USGS MCS 2026 Niobium PDF (as C32). Access: read-directly.
Finding: Ferroniobium is $26/kg and Brazil produced 104,000 t of 112,000 t (Nb content, 2025e). The text gives "approximately 93%". The $26/kg is a gross-weight unit value of U.S. ferroniobium trade, not a per-kg-Nb price. Any per-kg-Nb cost conversion in `reports/cost_supply.md` must account for this.

### P3 - PARTIAL
Checked: "Study on the Critical Raw Materials for the EU 2023 - Final Report" (Grohol & Veeh, DG GROW; Publications Office, catalogue ET-07-23-116-EN-N). I read a copy hosted at cde.ual.es, characters 0-300000 of 412943. The ec.europa.eu docsroom link redirects to a host that is not on this session's allowlist, so I could not open the official copy. Access: read-directly (third-party mirror of the official PDF).
Finding: The overview table gives SR of W 1.2, Mo 0.8, Ta 1.3, Nb 4.4 and V 2.3, which all match. EI is W 8.7, Mo 6.7, Ta 4.8, Nb 6.5 and V 3.9. The criticality threshold is two-part: "SR ≥ 1.0 and EI ≥ 2.8", and both must be met. The project statement gives only the SR half.
Corrected claim: EU CRM 2023: supply risk W 1.2, Mo 0.8, Ta 1.3, Nb 4.4, V 2.3 (EI 8.7, 6.7, 4.8, 6.5, 3.9). A raw material is critical only if SR ≥ 1.0 and EI ≥ 2.8; Mo does not qualify (SR 0.8).

### P4 - PARTIAL
Checked: ADA550865 (4289 preprint) Section 2 and room-temperature results. Bibliographic record for Intermetallics 19(5) 698-706, doi:10.1016/j.intermet.2011.01.004 (bvbvf1.bib-bvb.de). Yao et al. Entropy 18, 189, full page including Table 1. opact.sdu.edu.tr abstract record for doi:10.1016/j.msea.2016.07.102. encyclopedia.pub entry 21029 (secondary). Access: read-directly for Senkov (preprint) and Yao Entropy; abstract-only for MSEA 674, plus one secondary source.
Finding:
- MoNbTaW 1058 MPa and WMoTaNbV 1246 MPa match the preprint. The DOI and journal details match the library record. Both specimens were machined from as-cast buttons. I did not open the published Intermetallics text.
- MoNbTaV 1525 MPa matches Yao et al. Table 1 (experimental σ0.2; text "1.5 GPa"). The "annealed" label is wrong: the alloy was tested as-cast, and the paper reports no anneal (D5).
- I could not confirm NbTaVW 1530 MPa from the primary source. The MSEA 674 abstract gives no NbTaVW value, and the full text could not be found. The only support is a secondary encyclopedia.pub entry: "NbTaTiVW and NbTaVW show yield strengths of 1420 MPa and 1530 MPa with fracture strains of 20% and 12%", cited to Yao et al. That is not verification.
Corrected claim: Measured room-temperature compressive yield strengths, all as-cast: MoNbTaW 1058 MPa and WMoTaNbV 1246 MPa (Senkov et al., Intermetallics 19 (2011) 698, doi:10.1016/j.intermet.2011.01.004; values checked against the AFRL preprint); MoNbTaV 1525 MPa, as-cast (doi:10.3390/e18050189, Table 1); NbTaVW 1530 MPa (doi:10.1016/j.msea.2016.07.102), not verified against the primary source, secondary citation only.

### P5 - PARTIAL
Checked: ADA550865 Section 2, Section 3.2.1, Fig. 4 caption, Section 3.2.4. Intermetallics abstract via library record ("stable ... after exposure to 1400°C"). Access: read-directly (preprint); published version abstract-only.
Finding: Senkov et al. did heat-treat both alloys at 1400 C, but they call it an anneal, not homogenisation. It was 19 h (18 h elsewhere) and was applied to the neutron-diffraction samples to show phase stability. No compositional check after it is reported, and Section 3.2.4 says inhomogeneity persisted even after 1400 C deformation. The project's reason for using 1400 C does not follow from the source: the yield strengths the Thermo-Calc runs are validated against (1058 and 1246 MPa) were measured on as-cast specimens, not on 1400 C-annealed material. Yao et al. (2016) do call Senkov's MoNbTaW "homogenized", but that is a secondary description.
Corrected claim: Senkov et al. annealed neutron-diffraction samples of cast WMoTaNb and WMoTaNbV at 1400 C for 19 h (18 h in Section 3.2.1) and found the BCC phase stable. They did not call this homogenisation or show that segregation was removed. Their room-temperature yield strengths were measured on as-cast specimens.

### P6 - SUPPORTED
Checked: Canadian Mining Journal, "Western tungsten prices nearly quadruple China's: report", 4 Nov 2026, CMJ Staff, reporting MetalMiner's "Tungsten Resilience White Paper". Access: read-directly (CMJ article; I did not open the MetalMiner white paper).
Finding: The article says Rotterdam APT "traded at $278.22 per kg in October" (2026). The basis is $/kg as written; the article does not say whether this is per kg APT or per kg WO3. The figure is a trade-press report of a MetalMiner number.

---

## Verdict counts

Claims (46):
- SUPPORTED: 41
- PARTIAL: 5 (C2, C3, C14, C18, C46)
- UNSUPPORTED: 0
- UNREACHABLE: 0
- LEAD-ONLY: 0 (no claim had a search-summary access label)

Abstract-only verdicts: C8, C24, C46.

Project statements (6):
- SUPPORTED: 3 (P1, P2, P6)
- PARTIAL: 3 (P3, P4, P5)
- UNSUPPORTED: 0
- UNREACHABLE: 0 as whole statements. One part of P4 (NbTaVW 1530 MPa) could not be verified against the primary source.
- LEAD-ONLY: 0
