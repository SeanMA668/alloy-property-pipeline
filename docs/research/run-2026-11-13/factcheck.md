# Fact-check: run 2026-11-13

Fact-checker, 2026-11-13. I re-opened every cited source myself with WebFetch. WebFetch returns a
model-extracted reading of the page, not the raw text. "read-directly" means the relevant passage
of the full text, full preprint, full open-access article or full data table was in what loaded.
"abstract-only" means only an abstract or abstract-level record loaded. I did not rely on the
quotes in `claims.md`. Equations read from PDFs are reconstructions from garbled extractions
(brackets, exponents, "/3" factors); where that matters the entry says so.

Notes on what counts as the source:
- Maresca & Curtin. Bibliographic data confirmed from two repository records (EPFL Infoscience
  handle 20.500.14299/166619; University of Groningen research portal): F. Maresca, W.A. Curtin,
  "Mechanistic origin of high strength in refractory BCC high entropy alloys up to 1900K", Acta
  Materialia 182 (2020) 235-249, doi:10.1016/j.actamat.2019.10.015 (online 15 Oct 2019). The RUG
  copy is the publisher version, listed as an embargoed document ("Request copy" only). The EPFL
  record has no attached file. I found no open accepted manuscript. Every check below was made
  against arXiv:1901.02100v3 (13 Jun 2019): ar5iv HTML, all of its 209487 characters read in three
  parts, plus the arXiv PDF for equations and specific sentences. Below this is "MC-v3". Any
  verdict on MC-v3 is a verdict on the preprint, not on the published article.
- arXiv v1 and v2 could not be checked. The v1 PDF URL was not on the session allowlist. The v2
  URL returned only the abstract page (v2 dated 2019-01-14).
- Yao et al., MSEA 674 (2016). An OSTI accepted manuscript exists (search result "1 NbTaV-(Ti, W)
  Refractory High-entropy Alloys: Experiments and Modeling", https://www.osti.gov/servlets/purl/1482331;
  record https://www.osti.gov/pages/biblio/1482331). Both URLs failed for me with
  `robots_disallowed`, so I could not read them. academia.edu and Semantic Scholar copies also
  failed (client_error). A person using a normal browser can probably open the OSTI copy without
  university access. I have not confirmed that it holds the full text.

---

## Reviewer discrepancies D1-D9

- **D1 (temperature law): not resolved. The open evidence now leans towards the published
  version differing from v3.** Confirmed: MC-v3 Eqs. 11-12 are the two forms (2/3-power for
  τy/τy0 > 0.5; exp[-(1/0.55)(kT/ΔEb) ln(ε̇0/ε̇)] for τy/τy0 < 0.5). The arXiv PDF has no 0.91
  (the only "0.91" string is the start of "0.914" in Table 2). Several later papers attribute a
  single exp form with exponent 0.91 to the Acta paper. Two of them have Curtin, and one also
  Maresca, as co-author:
  - Kubilay, Ghafarollahi, Maresca, Curtin 2021 (Eq. 7, ref. 8 = Acta 182).
  - Winkens et al., Commun. Mater. 4, 26 (2023), co-authored by Curtin (Eq. 14, "ad hoc form",
    cites Acta 182).
  - arXiv:2502.11369 (Eq. 14, ref. [18] = Acta 182).
  - Wang, ..., Rao, Mater. Des. 261 (2026) 115368 (Eq. 5, refs. [15] = Acta 182 and [17] = Rao 2021).
  Baruffi et al. 2022 use the same form without a separate reference. Against this, Lee et al. 2021
  (Maresca and Curtin co-authors) use the two forms with the switch at σy/σy0 = 0.5 and cite only
  the Acta paper (ref. 23) for them. Yin et al. 2020 (Eq. 2) print only the 2/3-power form.
  So both laws are attributed to the published paper by the same group. The published paper may
  contain both: the two forms plus an interpolating 0.91 form, perhaps added in revision after
  v3. That is a plausible guess, not a finding.
  A second problem, also unresolved, is where the bracket goes in the 0.91 form. My reading of the
  Kubilay PDF puts 1/0.55 inside the bracket raised to 0.91. Winkens, arXiv:2502.11369 and Wang
  et al. put it outside. (1/0.55)^0.91 = 1.72 against 1.82 (my arithmetic), so the exponent
  differs by about 5 %.
  Status: IMPERATIVE in "Needs Sean", narrowed to the temperature law only.
- **D2 (α): confirmed. Not a contradiction but a spread across papers.** α = 1/12 in MC-v3
  (Section 3 "we use the value α=1/12 here"; Appendix A "Results in the main text use α=1/12"),
  Yin 2020 (0.0833 bcc), Kubilay 2021 and Lee 2021. α = 1/6 in Baruffi 2022 ("slightly larger
  than that used by Maresca et al." but "gives better overall predictions of strength vs.
  temperature"). New: α = 1/8 in Winkens et al. 2023 (Curtin co-author). MC-v3 Appendix A says
  room-temperature predictions are "rather sensitive" to α, and 296-1900 K predictions are "quite
  insensitive". The project's 1/12 matches the paper's main analysis. Later work by the same group
  uses 1/12, 1/8 and 1/6.
- **D3 (Taylor factor): resolved as rounding.** M = 3.067 in MC-v3 and Kubilay 2021. "3.06" in Yin
  2020, Baruffi 2022 and Winkens 2023. The difference is 0.2 %. Lee 2021 gives no Taylor factor.
- **D4 (bulk modulus 1/3): resolved for practice; the printed form is still unverified.** MC-v3
  prints B̄ = (C̄11 + 2C̄12) with no 1/3 in Section 3 and Section 5 (both ar5iv and PDF). Kubilay
  2021 and Baruffi 2022 extractions also show no 1/3. Yin 2020 footnote h, Lee 2021 and Winkens
  2023 give (C11 + 2C12)/3. Yin's numbers show the group's calculations use the 1/3. Here is my
  arithmetic, using ROM of the Kubilay elemental values:
  - MoNbTaW: C̄ = 375.4/167.3/101.6 GPa gives μ = 102.8 GPa. ν = 0.310 with the 1/3, and 0.431
    without it. Yin Table 3 gives μ 103, ν 0.31.
  - MoNbTaVW: C̄ = 346.8/157.7/90.5 gives μ = 92.5. ν = 0.316 with the 1/3, and 0.433 without.
    Yin gives μ 92, ν 0.32.
  The missing 1/3 in MC-v3 is therefore a typesetting omission (or extraction loss), not the
  method, and the code's `B = (c11 + 2c12)/3` matches what the group computes. Whether the
  published Acta text prints the 1/3 no longer matters to any project number. I removed it from
  the imperative request.
- **D5 (which elemental Cij): further resolved.** I read Featherston & Neighbours (1963) Tables II-IV
  myself. The Kubilay 2021 Table 2 values for three elements equal the F&N **0 K** rows:
  - W: 532.55/204.95/163.13 = F&N 0 K 5.3255/2.0495/1.6313.
  - Mo: 450.02/172.92/125.03 = F&N 0 K 4.5002/1.7292/1.2503.
  - Ta: 266.32/158.16/87.36 = F&N 0 K 2.6632/1.5816/0.8736.
  The F&N unit exponent is illegible in my extraction too; 100 GPa per unit fits the magnitudes.
  So for W, Mo and Ta the Curtin-group inputs are 0 K values, not room-temperature values. Nb
  (252.7/133.2/30.97) and V (232.4/119.36/45.95) remain unattributed; I found no open source for
  them. Note also that MC-v3 Section 4 says only that alloy moduli "are computed as before". The
  "EAM values of the elements" sentence refers to the ROM-vs-atomistic comparison. MC-v3 itself
  does not say which elemental set feeds the experimental-alloy predictions.
- **D6 (V volume): confirmed, not resolved.** Yin Table 2 gives V 14.020 Å³ "from the experimental
  lattice constants" (Simmons & Wang). That corresponds to a = 3.0381 Å; Baruffi Table I gives
  3.038 Å. AMCSD gives 3.0236-3.0241 Å (James & Straumanis 1960 at 25 °C: 3.0241 Å). The other
  Curtin-group volumes correspond to W 3.1620, Mo 3.1430, Nb 3.2998 and Ta 3.3018 Å (all my
  arithmetic). These are 0.003-0.004 Å below the NBS 25 °C values for W, Mo and Ta, and 0.014 Å
  above for V. The source of the group's V value is unknown.
- **D7 (MC-v3 Table 2 quinary Vegard row): confirmed, with more detail.** My Table 2 reading is
  the same as the reviewer's. My arithmetic with the Yin/Kubilay volumes:
  - Equiatomic MoNbTaVW: ΔV = Mo -0.734, Nb +1.694, Ta +1.727, V -2.238, W -0.451. Printed:
    -0.628, 1.713, 1.877, -2.484, -0.478. The printed set still sums to zero. a = 3.1915 Å matches
    the printed 3.192.
  - The measured-composition MoNbTaVW row (21.7Mo-20.6Nb-15.6Ta-21V-21.1W) reproduces: Mo
    -0.628, Nb 1.800, Ta 1.833, V -2.132, W -0.345 against printed -0.628, 1.8, 1.833, -2.132,
    -0.348, with a = 3.184 against 3.185. Its Mo value is identical to the equiatomic row's Mo
    value.
  - The MoNbTaV measured row reproduces (Mo -0.940, Nb 1.488, Ta 1.521, V -2.444).
  - The NbTaVW measured row reproduces for Nb, Ta and V (1.257, 1.290, -2.675) but not for W:
    -0.888 computed against -1.171 printed. The printed row does not sum to zero (Σ c·ΔV = -0.06).
  So MC-v3 Table 2 has internal inconsistencies in at least two rows. They may be corrected in
  the published version. No project number uses these Vegard rows; the test compares against
  the DFT row.
- **D8 (title): resolved.** The published title, confirmed by the Infoscience and RUG records, is
  "Mechanistic origin of high strength in refractory BCC high entropy alloys up to 1900K". The
  arXiv abstract page now shows "...high retained strength...". The v3 PDF shows the published
  wording in title case. The project cites the Acta article, so it should use the published title.
- **D9 (Gorsse NbTaVW column): not resolved.** In my reading too, 1530 sits in the σy column by
  position: one stress value, then ε = 12, then "(208)". The table does not mark empty cells, so
  this is an inference. Only the primary source can settle it.

---

## Claims

### C1 - SUPPORTED
Checked: MC-v3 ar5iv (characters 100000-200000, Section 5) and arXiv PDF. Access: read-directly (preprint).
Finding: Section 5 gives τy0 = 0.040 α^(-1/3) μ̄ ((1+ν̄)/(1-ν̄))^(4/3) [Σ cn ΔVn²/b̄⁶]^(2/3) and ΔEb = 2.00 α^(1/3) μ̄ b̄³ ((1+ν̄)/(1-ν̄))^(2/3) [Σ cn ΔVn²/b̄⁶]^(1/3). The same prefactors appear in Kubilay 2021, Yin 2020, Baruffi 2022 and Winkens 2023. I did not open the published version.

### C2 - SUPPORTED
Checked: MC-v3 ar5iv Section 3 and Appendix A (characters 200000-209487); arXiv PDF Appendix A. Access: read-directly.
Finding: Section 3: "we use the value α=1/12 here", with Γ = αμb². Appendix A: "α=1/16,1/12,1/8 that span the expected range"; "Results in the main text use α=1/12"; RT predictions are "rather sensitive"; 296-1900 K predictions are "quite insensitive".

### C3 - SUPPORTED
Checked: MC-v3 ar5iv Section 2/3 (characters 0-100000) and Section 4. Access: read-directly.
Finding: "ε̇0=10^4 s-1 ([26])". Experimental comparisons use "ε̇=10⁻³, Ref. [3], and ε̇=5·10⁻⁴, Refs. [4],[5]".

### C4 - SUPPORTED
Checked: arXiv PDF, Section 4. Access: read-directly.
Finding: "The uniaxial yield stress in an untextured BCC polycrystal controlled by edge dislocation glide is computed as σy = Mτy (M=3.067)."

### C5 - SUPPORTED
Checked: MC-v3 ar5iv Eqs. 11-12 and arXiv PDF. Access: read-directly.
Finding: Two forms with the stated conditions ("holds for low temperatures and high stress (τy/τy0 > 0.5)"; "For higher temperatures/lower stress (τy/τy0 < 0.5)"). No 0.91 exponent anywhere in v3. The PDF extraction does not fully settle the bracket around 1/0.55 in Eq. 12; ar5iv gives exp(-(1/0.55)(kT/ΔEb) ln(ε̇0/ε̇)).

### C6 - SUPPORTED
Checked: MC-v3 ar5iv Section 3 and Section 5; arXiv PDF. Access: read-directly.
Finding: μ̄ = √(½C̄44(C̄11-C̄12)), ν̄ = (3B̄-2μ)/(2(3B̄+μ)), B̄ = (C̄11+2C̄12) with no 1/3, in both places. The Section 5 restatement of μ̄ is garbled in ar5iv. See D4: the group's numbers use the 1/3.

### C7 - SUPPORTED
Checked: MC-v3 ar5iv (characters 100000-200000). Access: read-directly.
Finding: "A rule-of-mixtures (ROM) estimate C̄ij=∑n cn Cij using the EAM values of the elements yields good agreement"; "we use Vegard's law based on the experimental atomic volumes of the alloy elements". The "computed as before" sentence is in Section 4 in my reading of the PDF, not Section 5. It does not identify the elemental set used for the experimental alloys (D5).

### C8 - SUPPORTED
Checked: MC-v3 ar5iv Section 5. Access: read-directly.
Finding: "fitted to reproduce most high-strength/high-temperature data within 5% accuracy"; "standard deviation of ∼10% for both strength and energy barrier".

### C9 - SUPPORTED
Checked: MC-v3 ar5iv Table 2; arXiv PDF Table 2 caption. Access: read-directly.
Finding: All four rows match the claim to the digit. The caption confirms that the DFT data were "kindly provided by Dr. B. Yin [39]". The PDF has "The EAM value for C44 is actually better than the DFT value, which is known to be underestimated in BCC metals [36]" (relevant to P2). Units are not printed in my extraction either.

### C10 - SUPPORTED
Checked: MC-v3 ar5iv Table 2. Access: read-directly.
Finding: MoNbTaV (24.9-25.8-26.6-22.7) Vegard/ROM a 3.205, C 300.8/146.6/72.8; NbTaVW (28.5-29.65-20.67-21.18) a 3.22, ΔV Nb 1.258, Ta 1.29, V -2.675, W -1.171, C 310.3/152.5/78.2, all as claimed. My arithmetic (D7): the printed W misfit in the NbTaVW row is not consistent with the other entries (-0.888 expected). The ROM C11 of the MoNbTaV row reproduces (300.84).

### C11 - SUPPORTED
Checked: Yin, Maresca, Curtin, Acta Mater. 188 (2020) 486-491, doi:10.1016/j.actamat.2020.01.062, RUG publisher PDF. Access: read-directly.
Finding: (A_t, A_E) = (0.040, 2.00) for bcc; α "0.0833 (bcc)"; "3.06 is the Taylor factor"; ε̇0 = 10⁴ s⁻¹; Table 3 at 300 K and 10⁻³ s⁻¹; footnote h gives ROM, μ = √(C44(C11-C12)/2), B = (C11+2C12)/3. Additional point: Yin's Eq. 2 as extracted is the 2/3-power form only (σy = 3.06 τy0[1-(...)^(2/3)]), with no exponential branch or switch (relevant to D1).

### C12 - SUPPORTED
Checked: Yin et al. Table 3. Access: read-directly.
Finding: MoNbTaW: a 3.228, μ 103, ν 0.31, predicted 954 against ≈1058. MoNbTaWV: a 3.192, μ 92, ν 0.32, predicted 1347 against ≈1246. There are no NbTaVW or MoNbTaV predictions.

### C13 - SUPPORTED
Checked: Yin et al. Table 2 and caption, ref. [29]. Access: read-directly.
Finding: V 14.020, Mo 15.524, W 15.807, Nb 17.952, Ta 17.985 Å³; "Other values are from the experimental lattice constants of the elements"; footnote cites Simmons & Wang (MIT Press, 1971).

### C14 - SUPPORTED
Checked: Kubilay et al., npj Comput. Mater. 7, 112 (2021), doi:10.1038/s41524-021-00577-7, EPFL Infoscience PDF. Access: read-directly.
Finding: Prefactors 0.040/2.00, α = 1/12, M = 3.067 ("Taylor factor for an untextured BCC polycrystal"), μ = √[C44(C11-C12)/2], and the Table 2 values all match the claim. Table 2 gives no source or temperature for the volumes or Cij. The W, Mo and Ta values equal the F&N 0 K rows (D5).

### C15 - PARTIAL
Checked: Kubilay et al. PDF, text before Eq. 7, Eq. 7, ref. 8 (read twice; asked specifically about bracket placement). Access: read-directly.
Finding: The attribution is confirmed: "This equation holds for low temperatures and/or high stresses (τy/τy0 > 0.5)8"; "To cover the full range of temperatures, Maresca et al.8 proposed the approximate form"; ref. 8 = Acta Mater. 182, 235-249 (2020). But my reading of the garbled glyphs puts the 1/0.55 factor inside the bracket raised to 0.91. The claim's formula has it outside. The two differ by about 5 % in the exponent.
Corrected claim: Kubilay et al. state that "to cover the full range of temperatures, Maresca et al. [ref. 8 = Acta Mater. 182 (2020)] proposed" a single form τy = τy0 exp{-[(1/0.55)(kT/ΔEb) ln(ε̇0/ε̇)]^0.91} or τy0 exp{-(1/0.55)[(kT/ΔEb) ln(ε̇0/ε̇)]^0.91}. The extraction does not settle whether 1/0.55 is inside or outside the bracket raised to 0.91. Winkens et al. 2023 and arXiv:2502.11369 print it outside.

### C16 - SUPPORTED
Checked: Kubilay et al. Table 1. Access: read-directly.
Finding: MoNbTaW τy0: theory 422, NEB 410, direct atomistic (MS) 470 MPa.

### C17 - PARTIAL
Checked: Lee et al., Nat. Commun. 12, 5474 (2021), doi:10.1038/s41467-021-25807-w, NSF PAR accepted manuscript (read twice). Access: read-directly.
Finding: α = 1/12, ε̇0, ROM elemental C11/C12/C44, Vegard's law, Eqs. 2-3 with the switch at σy/σy0 = 0.5 (ref. 23 = Acta 182), and the averages Aσ = 0.040 ± 0.004 and AE = 2.00 ± 0.2 are all confirmed. In my reading, the alloy values (NbTaTiV 0.0437/2.02; CrMoNbV 0.0344/1.93) are obtained from the full theory for each alloy. The paper stresses the theory has no fitting parameters. "Fitted" is therefore misleading if read as fitted to experiment. There is no Taylor factor or σ/τ conversion.
Corrected claim: Lee et al. (2021) use the reduced Maresca-Curtin edge model (α = 1/12, ε̇0 = 10⁴ s⁻¹, ROM elastic constants, Vegard misfits, two temperature forms switching at σy/σy0 = 0.5, citing Acta Mater. 182). They report alloy-specific coefficients from the full theory, Aσ = 0.0437, AE = 2.02 (NbTaTiV) and 0.0344, 1.93 (CrMoNbV), and state that across BCC HEAs these fall in Aσ = 0.040 ± 0.004, AE = 2.00 ± 0.2. Nothing is fitted to experiment.

### C18 - SUPPORTED
Checked: Baruffi, Maresca, Curtin, MRS Commun. 12 (2022) 1111-1118, doi:10.1557/s43579-022-00278-2, RUG PDF. Access: read-directly.
Finding: Prefactors 0.040/2.00; "α = 1/6 that is slightly larger than that used by Maresca et al."; "3.06 is the Taylor factor"; single "ad-hoc form" with 0.91 exponent, no switch, no separate reference; Bacon-Scattergood relations. Equations are garbled in extraction. No W-Mo-Ta-Nb-V alloy is in the 14-alloy Table II.

### C19 - SUPPORTED
Checked: Xiao et al., High Entropy Alloys & Materials 1 (2023) 110-119, doi:10.1007/s44210-022-00007-3, Springer page. Access: read-directly.
Finding: "The reduced Maresca–Curtin solid solution model ... was used"; "rule of mixtures and Vegard's law"; "the predicted yield strength is not directly proportional to the experimentally measured hardness"; predictions are used as "proxy properties". The paper states no α or Taylor factor. Misfit volumes are also attributed to their ref. [21].

### C20 - SUPPORTED
Checked: Featherston & Neighbours, Phys. Rev. 130, 1324 (1963), CORE/Calhoun PDF, Tables II-V. Access: read-directly.
Finding: W 300 K: C11 5.2327, C12 2.0453, C44 1.6072, B 3.1078. The unit exponent is illegible in my extraction too. The 0 K row is 5.3255/2.0495/1.6313 (D5).

### C21 - SUPPORTED
Checked: F&N Table IV and discussion. Access: read-directly.
Finding: Mo 300 K: 4.4077/1.7243/1.2165. The authors consider the Mo differences from Bolef & de Klerk "real and that they depend on physical differences between the specimens", "particularly in light of the agreement on tungsten".

### C22 - SUPPORTED
Checked: F&N Table II. Access: read-directly.
Finding: Ta 300 K: 2.6091/1.5743/0.8182. The 0 K row is 2.6632/1.5816/0.8736.

### C23 - SUPPORTED
Checked: F&N Table V. Access: read-directly.
Finding: W (Bolef & de Klerk) 1.604/1.598/3.083; Mo 1.068/1.510/2.683; Ta (Bolef 1961) 0.825/0.53/1.96. Column labels and row mapping are partly inferred in my extraction too.

### C24 - PARTIAL
Checked: OSTI record 4110197. Access: abstract-only.
Finding: At 27 °C, in 10¹¹ dyn/cm²: V 22.8/11.9/4.26; Ta 26.7/16.1/8.25; Nb c11 24.6, c44 2.87. My reading of the Nb c12 is "13." with the last digit uncertain; it may be 13.x, not 13. The OSTI record lists no authors, pages or DOI. Authorship and the 1961 date come from F&N's citation, and the OSTI receipt date is 31 Dec 1961.
Corrected claim: The OSTI abstract of "Elastic constants of single crystals of the bcc transition elements V, Nb, and Ta" (J. Appl. Phys. 32; cited by F&N as Bolef 1961) gives at 27 °C, in 10¹¹ dyn cm⁻², V 22.8/11.9/4.26 and Ta 26.7/16.1/8.25. For Nb it gives c11 24.6 and c44 2.87; c12 shows as "13." and may be truncated (13 to 13.9).

### C25 - SUPPORTED
Checked: Gong & Dal Corso, arXiv:2406.16634v1, Table II and references. Access: read-directly.
Finding: Dickinson & Armstrong 273.15 K 4637/1578/1092; Bolef & de Klerk 300 K 4696/1676/1068; Katahara et al. 300 K 4648/1616/1089; F&N 0 K 4500.2/1729.2/1250.3 kbar. The table also lists 0 K extrapolations, not mentioned in the claim. This is a secondary compilation.

### C26 - SUPPORTED
Checked: NBS Circular 539 Vol. I (characters 0-100000 of 275192). Access: read-directly.
Finding: W 3.1648, Mo 3.1472, Ta 3.3058 Å at 25 °C; the pattern tables (Tables 13, 8, 14) are at 26 °C.

### C27 - SUPPORTED
Checked: AMCSD (rruff.info) Vanadium page. Access: read-directly.
Finding: Wyckoff 1963 3.0240; Straumanis 1959 3.0236; James & Straumanis 1960 3.0241 Å at 25 °C; Hull 1922 3.04 Å.

### C28 - SUPPORTED
Checked: COD 1539041. Access: read-directly.
Finding: Nb a = 3.3063 Å; Roberge, J. Less-Common Met. 40 (1975) 161-164. No temperature is shown for the entry.

### C29 - SUPPORTED
Checked: Baruffi et al. Table I. Access: read-directly.
Finding: The values match the claim. The caption gives sources only for vacancy, interstitial and kink energies, and the text says the elemental properties "are those given in Lee et al.".

### C30 - SUPPORTED
Checked: Gorsse et al., Data in Brief 21 (2018) 2664-2678, doi:10.1016/j.dib.2018.11.111, PDF. Access: read-directly.
Finding: "NbTaVW [76] BCC (12.9) 492 C 1530 12 (208)"; [76] = Yao et al. MSEA 674 (2016) 203-211. Also MoNbTaW 1058, MoNbTaVW 1246 ([73] Senkov 2011) and MoNbTaV 1525 ([72] Yao, Entropy 2016). The σy column placement is inferred (D9). No processing state or strain rate is given.

### C31 - SUPPORTED
Checked: opact.sdu.edu.tr Summon record (truncated abstract). Access: abstract-only.
Finding: Bibliographic data confirmed. "a single body-centered cubic solid solution phase was experimentally confirmed in the as-cast ingots". The visible abstract has no NbTaVW value, strain rate or test method.

### C32 - SUPPORTED
Checked: MC-v3 ar5iv Section 4. Access: read-directly.
Finding: "The predictions are lower than experiments."; "The experiments show a plateau in yield strength in the range 900K–1300K not predicted by the theory."; "the edge strengthening agrees fairly well with the measured high temperature behavior".

### C33 - PARTIAL
Checked: arXiv PDF Fig. 1 caption and Section 1. Access: read-directly.
Finding: The caption reads "Yield strength of BCC high entropy alloys and Ni-based superalloys at high temperatures 800-1900K ... Open symbols indicate experiments [2] and solid lines indicate predictions." The experiments are cited as ref. [2], not ref. [3]. Section 1 names "nominal compositions MoNbTaW and MoNbTaVW", citing [1, 2]. The figure also includes Ni-based superalloys.
Corrected claim: MC-v3 Fig. 1 compares predictions (solid lines) with experiments (open symbols, ref. [2]) for BCC HEAs, alongside Ni-based superalloys, at 800-1900 K. Section 1 identifies the HEAs as MoNbTaW and MoNbTaVW (refs. [1, 2]).

### C34 - SUPPORTED
Checked: Gorsse et al. Table 2. Access: read-directly.
Finding: MoNbTaW 548/506/421/405 MPa and MoNbTaVW 842/735/656/477 MPa at 1000/1200/1400/1600 °C, ref. [73]. The alloy-to-row mapping is by group heading. This is a secondary compilation.

### C35 - SUPPORTED
Checked: Kubilay et al. Fig. 7 caption and text. Access: read-directly.
Finding: The caption says "Yield strength theory predictions vs experiments at 0, 1000, and 1200 °C", with panel b for the MoNbTaW(Ti)(V) family. The text says "While the quantitative agreement is not as good, the theory captures the notable strengthening due to the addition of V in both alloys" and the Mo-Nb-Ta-Ti-V-W alloys "continue to agree with the theory trend". The paper also says the Ti strengthening of MoNbTaTiW "is not captured".

### C36 - SUPPORTED
Checked: arXiv PDF abstract and Section 1. Access: read-directly.
Finding: Abstract: "Unlike pure BCC metals and dilute alloys that are controlled by screw dislocation motion at low temperatures"; "can be controlled by edge dislocations, and especially at high temperatures". Section 1: "Edge dominance emerges at moderate temperatures".

### C37 - SUPPORTED
Checked: MC-v3 ar5iv and PDF, Section 4. Access: read-directly.
Finding: "V=36b³" for MoNbTaW at 296 K, "in the range of other BCC alloys controlled by screw motion"; "even at low T in the region where edge and screw strengths may be comparable, the edge model provides good agreement with experiments".

### C38 - SUPPORTED
Checked: arXiv PDF Section 7. Access: read-directly.
Finding: "the high-temperature strength of the screw dislocation is dominated by pinning due to jogs"; "Jog strengthening is defeated at high temperatures by thermal vacancies".

### C39 - SUPPORTED
Checked: Lee et al. accepted manuscript. Access: read-directly.
Finding: At 293 K: NbTaTiV 58 of 77 (75 %) edge and CrMoNbV 23 of 41 (56 %). MoNbTaW and MoNbTaVW "have been predicted to be controlled by edge dislocations". That is a prediction, not an observation.

### C40 - SUPPORTED
Checked: Tsuru et al., Nat. Commun. 15, 1706 (2024), doi:10.1038/s41467-024-45639-8, Springer page (characters 0-100000 of 136022; author list truncated with "…" on the page). Access: read-directly.
Finding: "screw and edge dislocation segments are present almost equally here regardless of the operative slip plane". Screw model 1242 MPa, edge model 1210 MPa (Rao et al. 2021), "approximately 25–30% lower" than measured. "kink migration is the rate-controlling step at room temperature in VNbTaMoW". Anneal at ~2000 °C (estimated) for 48 h, grain size 496 µm, 1 × 10⁻⁴ s⁻¹.

### C41 - SUPPORTED
Checked: Pozuelo & Marian, MSEA 856 (2022) 143892, NSF PAR accepted manuscript. Access: read-directly.
Finding: Section 3.3: "Edge dislocations are profusely observed in several of the other grains as well". Section 4.2: "the governing mechanism is related to a Peierls type activation of edge or screw dislocations". Section 4.2 also says edge dislocations are seen "before, during and after deformation".

### C42 - SUPPORTED
Checked: Yin et al. Section 3.2. Access: read-directly.
Finding: "One possible explanation is that there is a change from control of the alloy strength by edge dislocations (with V) to screw dislocations (without V) in some alloys."

### C43 - SUPPORTED
Checked: Baruffi et al. pp. 1114-1115, Table II. Access: read-directly.
Finding: No theories "capture the approximate plateau in yield strength versus temperature at intermediate temperatures". Ta42Nb40V18 is edge-controlled, and "the edge theory is in good agreement with experiments, although slightly low at high temperature".

### C44 - SUPPORTED
Checked: MC-v3 ar5iv Sections 3 and 4. Access: read-directly.
Finding: Section 4 (the experimental MoNbTaW and MoNbTaVW): "large zero-stress energy barriers (ΔE_b=2.2 eV, 2.5 eV)". Section 3 (simulated alloys): "ΔE_b≈1.9−2.5 eV". The text lists the two values without an explicit pairing to each alloy.

---

## Project statements

### P1 - SUPPORTED
Checked: MC-v3 Section 4 and Fig. 1 caption (as C32, C33). Access: read-directly (preprint; published version not opened).
Finding: The preprint says "The predictions are lower than experiments" and that the 900-1300 K plateau is "not predicted by the theory", for MoNbTaW and MoNbTaVW in Fig. 1. The same paragraph says edge strengthening "agrees fairly well" with high-temperature behaviour. If the published version changed the temperature law (D1), the published Fig. 1 curves may differ from v3.

### P2 - PARTIAL
Checked: MC-v3 Table 2 and Section 3 (as C9). Access: read-directly.
Finding: Every number quoted for the DFT row is correct (a 3.192; C11 338, C12 164, C44 51; ΔV Mo -0.824, Nb 1.848, Ta 1.882, V -2.380, W -0.526), and the ROM C44 is 90.5. DFT does give a much lower C44. But the report presents this as an alloying effect that ROM ignores. MC-v3 instead says "The EAM value for C44 is actually better than the DFT value, which is known to be underestimated in BCC metals [36]". The paper's own reading is that DFT C44 is too low, not that ROM is too high.
Corrected claim: "Rule-of-mixtures elastic constants ignore alloying effects. For equiatomic MoNbTaVW, DFT gives C44 = 51 GPa against 90.5 GPa from ROM (Maresca & Curtin Table 2, arXiv v3), but the authors note that DFT is known to underestimate C44 in BCC metals and consider the EAM value more reliable." The DFT misfit volumes in `tests/test_strength_model.py` match the table.

### P3 - SUPPORTED
Checked: MC-v3 Section 4 (as C44). Access: read-directly.
Finding: "(ΔE_b=2.2 eV, 2.5 eV)" for the experimental MoNbTaW and MoNbTaVW. MC-v3 does not say which inputs (DFT, Vegard/ROM or EAM) produced these barriers, so the test's comparison with ROM-input barriers is approximate. The test comment says so.

### P4 - PARTIAL
Checked: MC-v3 Section 4 (run-2026-11-11 C1 sentence, re-read in this run's PDF reading), Table 2 (all rows), my Vegard arithmetic. Access: read-directly.
Finding: The exact sentence is not in `README.md`. The nearest project text is `reports/strength_model.md`, "V (the strongest misfit solute)". The paper says V "has the largest misfit volume" in the context of MoNbTaVW against MoNbTaW. |ΔV_V| is the largest in every V-containing row of Table 2. A misfit volume is relative to the alloy's average volume, so it is not a fixed property of the element. With the Yin/Kubilay volumes, V's misfit is the largest for equiatomic and near-equiatomic alloys and for all five finalists (e.g. R5-4: V -2.80, Ta +1.16 Å³, my arithmetic). In strongly V-rich alloys Nb or Ta would overtake it (my arithmetic, not from a source).
Corrected claim: "In the W-Mo-Ta-Nb-V alloys studied (equiatomic and near-equiatomic, and our finalists), V has the largest-magnitude misfit volume (Maresca & Curtin; Table 2), because it is the smallest atom."

---

## Side-by-side check of the reviewer's Q2 table (numbers only, no verdict on the project)

I re-derived the open-source columns from my own readings. They match the reviewer's table. Two
observations:
- Code Ta (266.0/158.0/87.4) matches the F&N **0 K** row (266.32/158.16/87.36), not the F&N
  300 K row (260.9/157.4/81.8) or Bolef 27 °C (267/161/82.5). C44 differs by 5.6 GPa from both
  room-temperature measurements. The code comment says "Room-temperature".
- Code W equals F&N 300 K. Code Mo is close to Katahara et al. 300 K (464.8/161.6/108.9). Code
  Nb and V are close to Bolef 27 °C (Nb C12 uncertain, C24). Code lattice parameters: W, Mo and V
  agree with 25 °C X-ray values to within 0.0004 Å. Ta (3.3029 against NBS 3.3058) and Nb (3.3004
  against COD 3.3063, temperature unknown) do not. The Simmons & Wang source of these values was
  not opened.

---

## Needs Sean (university access)

1. **IMPERATIVE (narrowed).** F. Maresca, W.A. Curtin, "Mechanistic origin of high strength in
   refractory BCC high entropy alloys up to 1900K", Acta Materialia 182 (2020) 235-249,
   doi:10.1016/j.actamat.2019.10.015. No open published or accepted version found: the EPFL
   record has no file and the RUG publisher copy is embargoed.
   Needed: the temperature/strain-rate equation(s) as printed (equivalents of arXiv v3 Eqs.
   11-12):
   - two forms switching at τy/τy0 = 0.5, a single exp form with exponent 0.91, or both;
   - if the 0.91 form is there, whether 1/0.55 is inside or outside the bracket raised to 0.91;
   - which form is used for Fig. 1, Fig. 5 and the Section 5 reduced-model predictions.
   Why imperative: the code's switch rule and the 922/1411/1425/1317 MPa depend on it. Open
   sources attribute both laws to this paper (D1), and the regime switch is at the alloys'
   room-temperature operating point (`reports/strength_model.md`).
   No longer needed from this item:
   - (b) prefactors and α: these agree across v3, Kubilay and Yin.
   - (c) bulk modulus 1/3: settled by Yin's μ/ν arithmetic, D4.
   - (d) Taylor factor: 3.067 confirmed in v3 and Kubilay.
   - (e) Table 2 quinary Vegard row: OPTIONAL, since no project number uses it (D7).

2. **IMPERATIVE, but probably no university access needed.** H.W. Yao, J.W. Qiao, M.C. Gao, J.A.
   Hawk, S.G. Ma, H.F. Zhou, Y. Zhang, "NbTaV-(Ti,W) refractory high-entropy alloys: Experiments
   and modeling", Materials Science and Engineering A 674 (2016) 203-211,
   doi:10.1016/j.msea.2016.07.102. An OSTI accepted manuscript appears to exist at
   https://www.osti.gov/servlets/purl/1482331 (record https://www.osti.gov/pages/biblio/1482331).
   I could not open it because the site blocks automated fetching (`robots_disallowed`). Please
   try it in a browser first, and use library access only if that fails.
   Needed:
   - the NbTaVW room-temperature compressive yield strength as printed (table and/or figure),
     and whether it is the 0.2 % offset yield (D9);
   - the specimen condition tested (as-cast or heat-treated);
   - strain rate, specimen size and measured composition.
   Why imperative: 1530 MPa is a validation point. Only a secondary compilation (Gorsse, C30)
   gives it, and that gives neither condition nor strain rate.

3. OPTIONAL. D.I. Bolef, J. de Klerk, "Elastic Constants of Single-Crystal Mo and W between 77°
   and 500°K", J. Appl. Phys. 33 (1962) 2311, doi:10.1063/1.1728952. 300 K Cij for Mo and W.
   Secondary values are open (C23, C25).
4. OPTIONAL. K.W. Katahara, M.H. Manghnani, E.S. Fisher, J. Phys. F: Met. Phys. 9 (1979) 773.
   300 K Cij of Mo, Nb, Ta, W. Mo is covered by C25.
5. OPTIONAL (slightly raised priority). D.I. Bolef, "Elastic Constants of Single Crystals of the
   bcc Transition Elements V, Nb, and Ta", J. Appl. Phys. 32 (1961) 100. Needed: the Nb C12
   exact value (C24 shows "13."), plus uncertainties.
6. OPTIONAL. G. Simmons, H. Wang, Single Crystal Elastic Constants and Calculated Aggregate
   Properties: A Handbook, MIT Press (1971). Recommended RT Cij and lattice constants for W, Mo,
   Ta, Nb, V. This would also identify the source of the Curtin group's V volume (D6) and the
   code's Ta, Nb values.
7. OPTIONAL. R. Roberge, "Lattice parameter of niobium between 4.2 and 300 K", J. Less-Common
   Met. 40 (1975) 161-164. Nb a at 293-300 K.

---

## Search and fetch log (this check)

- arxiv.org/abs/1901.02100 (title, versions, DOI); ar5iv 1901.02100 at offsets 0, 100000,
  200000; arxiv.org/pdf/1901.02100 (three targeted reads).
- arxiv.org/pdf/1901.02100v1: not on session allowlist. arxiv.org/pdf/1901.02100v2: abstract
  only.
- WebSearch for an Infoscience copy of the Acta paper: infoscience.epfl.ch record (no file);
  research.rug.nl (publisher version embargoed).
- WebSearch for the "0.91"/"0.55" temperature law. Opened arXiv:2502.11369 and nature.com
  s43246-023-00353-8 (Winkens et al. 2023; characters 0-100000 of 131151). tandfonline
  10.1080/14686996.2022.2129444 failed (client_error).
- Second WebSearch on the 0.91 form: escholarship qt0f66h7kr (Wang et al. 2026);
  materialscloud record 1507 (Baruffi dataset, no equations).
- Infoscience Kubilay PDF (two reads); RUG Yin PDF; NSF PAR Lee (two reads); RUG Baruffi PDF;
  Springer Xiao 2023; Springer Tsuru 2024 (characters 0-100000 of 136022); NSF PAR Pozuelo &
  Marian.
- CORE F&N 1963; OSTI 4110197 (Bolef); arXiv 2406.16634v1; NBS Circular 539 (0-100000);
  rruff Vanadium; COD 1539041; Gorsse PDF; opact.sdu.edu.tr Yao record.
- WebSearch "NbTaV-(Ti,W) refractory high-entropy alloys": OSTI purl 1482331 and OSTI pages
  1482331 (robots_disallowed); academia.edu and semanticscholar (client_error). Second
  WebSearch for the NbTaVW 1530 MPa primary: nothing new. Google Scholar not used.

---

## Verdict counts

Claims (44):
- SUPPORTED: 40
- PARTIAL: 4 (C15, C17, C24, C33)
- UNSUPPORTED: 0
- UNREACHABLE: 0
- LEAD-ONLY: 0 (no claim had a search-summary access label)

Abstract-only verdicts: C24, C31. All MC-v3 verdicts (C1-C10, C32, C33, C36-C38, C44) are
against the arXiv v3 preprint; the published Acta version was not opened.

Project statements (4):
- SUPPORTED: 2 (P1, P3)
- PARTIAL: 2 (P2, P4)
- UNSUPPORTED: 0
- UNREACHABLE: 0
- LEAD-ONLY: 0
