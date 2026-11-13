# Claims: run 2026-11-13 (literature-reviewer)

Written by the literature-reviewer agent, 2026-11-13. Each claim records how its source
was read. Pages were opened with WebFetch, which returns a model-extracted reading of the
page, not the raw text. Quotes below are as returned by that reading. Equations taken from
PDF extractions are often garbled (brackets, exponents, "/3" factors); where that matters
the entry says so. `read-directly` means the relevant passage of the full text (full
preprint, full open-access article, full data table) was in what loaded. `abstract-only`
means only an abstract-level record loaded. `search-summary` claims are leads, not
findings. No claim in this file judges the project's own results. Where a comparison with
the project's code is given, it is a side-by-side of numbers only, and any unit conversion
or arithmetic done by the reviewer is labelled "reviewer arithmetic".

Scope: run-2026-11-11 C1-C3 (Maresca-Curtin: V as strongest misfit solute; MoNbTaV
underpredicted; "very good agreement" at room temperature) and C8 (Yao et al. MSEA 2016
abstract) are reused, not repeated, except where a question here needs the detail.

Main source for Q1 and Q4: F. Maresca, W.A. Curtin, arXiv:1901.02100v3 (13 Jun 2019),
read in full on ar5iv (https://ar5iv.labs.arxiv.org/html/1901.02100, 209487 characters,
read in three parts at offsets 0, 100000, 180000/200000) and cross-checked on the arXiv PDF
(https://arxiv.org/pdf/1901.02100, version marker "arXiv:1901.02100v3 [cond-mat.mtrl-sci]
13 Jun 2019"). The published Acta Mater. 182 (2020) 235-249 version was NOT opened (paywall).
Below this is cited as "MC-v3".

## Disagreements and inconsistencies noticed (recorded, not resolved)

- D1. **Temperature form.** MC-v3 gives two forms, Eq. 11 for τy/τy0 > 0.5 and Eq. 12
  for τy/τy0 < 0.5 (C5); Lee et al. 2021 also use two forms switching at 0.5 (C17).
  Kubilay et al. 2021 (C15) and Baruffi et al. 2022 (C18) instead use one formula,
  τy = τy0 exp{-(1/0.55)[(kT/ΔEb) ln(ε̇0/ε̇)]^0.91}, and Kubilay et al. attribute it to
  "Maresca et al." ref. 8, which is the published Acta Mater. 182 (2020) paper. MC-v3 does
  not contain the exponent 0.91. Possibly the published version differs from v3; not
  checked (published version paywalled; see "Needs Sean").
- D2. **Line-tension coefficient.** α = 1/12 in MC-v3, Yin 2020 (0.0833), Kubilay 2021
  and Lee 2021; α = 1/6 in Baruffi 2022 ("slightly larger ... but gives better overall
  predictions of strength vs. temperature").
- D3. **Taylor factor.** 3.067 in MC-v3 and Kubilay 2021; 3.06 in Yin 2020 and Baruffi
  2022.
- D4. **Bulk modulus.** MC-v3 prints B̄ = (C̄11 + 2C̄12) without the factor 1/3 (both the
  ar5iv and the PDF extraction; Sections 3 and 5). Kubilay 2021 and Baruffi 2022 extractions
  also show no 1/3. Yin 2020 Table 3 footnote h gives B = (C11 + 2C12)/3. The ν formula
  ν = (3B - 2μ)/[2(3B + μ)] is the standard isotropic one, which assumes the 1/3. Not
  resolved: it may be a typesetting omission or an extraction artefact.
- D5. **Which elemental elastic constants feed the rule of mixtures.** MC-v3 Section 4 says
  the ROM estimate uses "the EAM values of the elements". MC-v3 Table 2's "Vegard/ROM" rows
  equal (reviewer arithmetic) the ROM of the elemental values in Kubilay 2021 Table 2
  (equiatomic MoNbTaVW: 346.8, 157.72, 90.49 GPa vs printed 346.8, 157.7, 90.5; MoNbTaW:
  375.4, 167.31, 101.62 vs printed 375.5, 167.3, 101.6). The Kubilay Mo values (450.02,
  172.92, 125.03 GPa) equal the Featherston & Neighbours 0 K Mo values as tabulated by Gong &
  Dal Corso (4500.2, 1729.2, 1250.3 kbar; C25), not their 300 K values (C21). So at least
  for Mo the Curtin-group inputs are not room-temperature values. Not resolved for W, Ta,
  Nb, V (their 0 K values were not found in an open source).
- D6. **Elemental volumes for V.** Yin 2020 Table 2 gives V 14.020 Å³ "from the experimental
  lattice constants of the elements" (citing Simmons & Wang), and Baruffi 2022 Table I gives
  a(V) = 3.038 Å; this corresponds to a = 3.038 Å (reviewer arithmetic). X-ray values at
  25 °C in AMCSD are 3.0236-3.0241 Å (C27). The two differ by about 0.014 Å; not resolved.
- D7. **MC-v3 Table 2 quinary Vegard misfits.** The equiatomic MoNbTaVW Vegard row (Mo
  -0.628, Nb 1.713, Ta 1.877, V -2.484, W -0.478 Å³) could not be reproduced by the reviewer
  from the Yin/Kubilay elemental volumes (gives -0.734, 1.694, 1.727, -2.238, -0.451),
  whereas the MoNbTaW row (-1.293, 1.135, 1.168, -1.010) is reproduced exactly and the
  quinary a_bcc (3.192 Å) is reproduced (reviewer arithmetic). Not resolved.
- D8. **Title.** The arXiv v3 PDF and ar5iv show "Mechanistic Origin of High Strength in
  Refractory BCC High Entropy Alloys up to 1900K"; the arXiv abstract page shows the current
  title as "Mechanistic origin of high retained strength in refractory BCC high entropy
  alloys up to 1900K". The project cites the published Acta Mater. 182 article.
- D9. **Gorsse et al. NbTaVW row.** The row has one strength value (1530) and no σmax; the
  extracted reading places it in the σy column but flags the row as ambiguous (C30).

---

## Q1. The reduced Maresca-Curtin model as implemented

### C1
Claim: The reduced analytic model gives τy0 = 0.040 α^(-1/3) μ̄ [(1+ν̄)/(1-ν̄)]^(4/3) [Σ cn ΔVn²/b̄⁶]^(2/3) and ΔEb = 2.00 α^(1/3) μ̄ b̄³ [(1+ν̄)/(1-ν̄)]^(2/3) [Σ cn ΔVn²/b̄⁶]^(1/3).
Answers: Q1
Access: read-directly
Source: F. Maresca, W.A. Curtin, "Mechanistic Origin of High Strength in Refractory BCC High Entropy Alloys up to 1900K", arXiv:1901.02100v3 (2019), https://ar5iv.labs.arxiv.org/html/1901.02100 and https://arxiv.org/pdf/1901.02100 (published as Acta Mater. 182 (2020) 235-249, doi:10.1016/j.actamat.2019.10.015; published version not opened)
Where: Section 5 (reduced model equations)
Evidence: "τy0 = 0.040α" ... "∆Eb = 2.00α" (PDF extraction; α^(-1/3), α^(1/3) per ar5iv)
Not claimed: that the published version has the same prefactors (not opened); the full-model fits in Eqs. 15-16 use different prefactors (0.051 and 0.274 with factors f^τ, f^ΔE).

### C2
Claim: The main text uses line-tension coefficient α = 1/12 (Γ = αμb²); Appendix A tests α = 1/16, 1/12 and 1/8 and states that room-temperature predictions are rather sensitive to α while 296-1900 K predictions are quite insensitive.
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 2; Appendix A; Fig. 9
Evidence: "the values α=1/16,1/12,1/8 that span the expected range"; "Results in the main text use α=1/12"
Not claimed: the size of the room-temperature sensitivity in MPa (figure only).

### C3
Claim: The reference strain rate is ε̇0 = 10⁴ s⁻¹, and experimental comparisons use ε̇ = 10⁻³ s⁻¹ (Ref. [3]) and 5·10⁻⁴ s⁻¹ (Refs. [4], [5]).
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 3 (after Eq. 10); Section 4 / Fig. 5 caption
Evidence: "estimated as ε̇_0=10^4 s-1"
Not claimed: which strain rate belongs to which alloy in Fig. 5 beyond the reference numbers.

### C4
Claim: Uniaxial yield stress of an untextured BCC polycrystal controlled by edge glide is taken as σy = Mτy with M = 3.067.
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 4, before Fig. 5
Evidence: "computed as σy = Mτy (M=3.067)"
Not claimed: that later papers use the same value (see D3).

### C5
Claim: MC-v3 gives two temperature/strain-rate forms: τy = τy0[1 - ((kT/ΔEb) ln(ε̇0/ε̇))^(2/3)] for low T / high stress (τy/τy0 > 0.5), and τy = τy0 exp[-(1/0.55)(kT/ΔEb) ln(ε̇0/ε̇)] for τy/τy0 < 0.5; the exponent 0.91 does not appear in v3.
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 3, Eqs. 11-12
Evidence: "holds for low temperatures and high stress (τy/τy0 > 0.5)"; "For higher temperatures/lower stress (τy/τy0 < 0.5)"
Not claimed: what the published Acta version prints (see D1, C15); any statement in v3 about a discontinuity at the switch.

### C6
Claim: Alloy elastic constants are rule-of-mixtures averages C̄ij = Σ cn Cij, with μ̄ = √[½ C̄44 (C̄11 - C̄12)] and ν̄ = (3B̄ - 2μ̄)/[2(3B̄ + μ̄)]; the bulk modulus is printed as B̄ = (C̄11 + 2C̄12) without a 1/3.
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 3 (after Fig. 4) and Section 5
Evidence: "the bulk modulus as B¯ = (C¯11 + 2C¯12)"
Not claimed: that the missing 1/3 is intended (see D4).

### C7
Claim: MC-v3 says its ROM elastic estimate uses the EAM values of the elements and that misfit volumes use Vegard's law based on experimental atomic volumes of the elements.
Answers: Q1, Q2
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 4 (before Table 2); Section 6 summary
Evidence: "using the EAM values of the elements yields good agreement with the atomistic values"; "Vegard's law based on the experimental atomic volumes"
Not claimed: which elemental values (or sources) are used in the Section 5 reduced-model predictions; Section 5 says only that moduli are "computed as before" (see D5).

### C8
Claim: The reduced formulas were fitted to reproduce most high-strength/high-temperature full-model results within 5 %, and differ from the whole full-model dataset with a standard deviation of about 10 % for both strength and barrier.
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 5
Evidence: "within 5% accuracy"; "standard deviation of ∼10%"
Not claimed: accuracy against experiment.

### C9
Claim: MC-v3 Table 2 lists for equiatomic MoNbTaVW a DFT row (a 3.192, ΔV Mo -0.824, Nb 1.848, Ta 1.882, V -2.380, W -0.526, C11 338, C12 164, C44 51) and a Vegard/ROM row (a 3.192, ΔV -0.628, 1.713, 1.877, -2.484, -0.478, C11 346.8, C12 157.7, C44 90.5), and for equiatomic MoNbTaW a DFT row (3.237; -1.251, 1.153, 1.132, -1.034; 374, 163, 64) and a Vegard/ROM row (3.228; -1.293, 1.135, 1.168, -1.010; 375.5, 167.3, 101.6).
Answers: Q1, Q2 (also P2, P4)
Access: read-directly
Source: MC-v3 (as C1)
Where: Table 2 (caption: DFT data "kindly provided by Dr. B. Yin")
Evidence: DFT row "3.192, −0.824, 1.848, 1.882, −2.380, −0.526, 338, 164, 51"
Not claimed: units (not printed in the extraction; Å, Å³, GPa implied by magnitude). Column order of ΔV is Mo, Nb, Ta, V, W. EAM rows also exist; the text says the EAM C44 "is actually better than the DFT value".

### C10
Claim: MC-v3 Table 2 also gives Vegard/ROM and EAM rows (no DFT rows) at the measured compositions of the experimental alloys, e.g. Mo-Nb-Ta-V 24.9-25.8-26.6-22.7 (Vegard/ROM a 3.205; C11 300.8, C12 146.6, C44 72.8) and Nb-Ta-V-W 28.5-29.65-20.67-21.18 (a 3.22; ΔV Nb 1.258, Ta 1.29, V -2.675, W -1.171; C11 310.3, C12 152.5, C44 78.2).
Answers: Q1
Access: read-directly
Source: MC-v3 (as C1)
Where: Table 2
Evidence: "0-28.5-29.65-20.67-21.18 (nominal Nb-Ta-V-W)"
Not claimed: that these compositions are equiatomic (they are not; the project's validation uses equiatomic compositions); composition column order is Mo-Nb-Ta-V-W as shown in the extraction, whose labels were partly garbled.

### C11
Claim: Yin, Maresca and Curtin (2020) use the same reduced bcc model with (A_t, A_E) = (0.040, 2.00), α = 0.0833, Taylor factor 3.06, ε̇0 = 10⁴ s⁻¹, T = 300 K and ε̇ = 10⁻³ s⁻¹, ROM elemental Cij with Bacon-Scattergood μ = √[C44(C11 - C12)/2] and B = (C11 + 2C12)/3, and Vegard's-law misfit volumes.
Answers: Q1
Access: read-directly
Source: B. Yin, F. Maresca, W.A. Curtin, "Vanadium is an optimal element for strengthening in both fcc and bcc high-entropy alloys", Acta Mater. 188 (2020) 486-491, doi:10.1016/j.actamat.2020.01.062, publisher PDF at https://research.rug.nl/files/136414836/1_s2.0_S1359645420300884_main.pdf
Where: Section 2, Eqs. 1-3; Table 3 and footnote h
Evidence: footnote h: "The anisotropic elastic constants Cij of the alloy is estimated by applying "rule-of-mixtures""
Not claimed: the temperature-dependence form used for Table 3 (not stated in what loaded); the formulas in footnote h were partly garbled in extraction.

### C12
Claim: Yin et al. predict room-temperature (300 K, 10⁻³ s⁻¹) yield strengths of 954 MPa for MoNbTaW (measured ≈1058) and 1347 MPa for MoNbTaWV (measured ≈1246), with a = 3.228 / 3.192 Å, μ = 103 / 92 GPa and ν = 0.31 / 0.32.
Answers: Q1
Access: read-directly
Source: Yin et al. 2020 (as C11)
Where: Table 3
Evidence: "MoNbTaW: 954 vs. ≈1058"; "MoNbTaWV ... 1347 vs. ≈1246"
Not claimed: predictions for NbTaVW or MoNbTaV (not in Table 3); the experimental values are from Couzinié et al. Data in Brief 21 (2018) (ref. [33]), not newly measured.

### C13
Claim: Yin et al. Table 2 gives bcc apparent atomic volumes V 14.020, Mo 15.524, W 15.807, Nb 17.952, Ta 17.985 Å³, stated to be from the experimental lattice constants of the elements (footnote: Simmons & Wang handbook, 1971).
Answers: Q1, Q2
Access: read-directly
Source: Yin et al. 2020 (as C11)
Where: Table 2 and caption; ref. [29] G. Simmons, H. Wang, Single Crystal Elastic Constants and Calculated Aggregate Properties: A Handbook, MIT Press, 1971
Evidence: "Other values are from the experimental lattice constants of the elements."
Not claimed: the measurement temperature of those lattice constants; the elemental Cij used (not tabulated in Yin et al.).

### C14
Claim: Kubilay et al. (2021) apply the reduced theory (prefactors 0.040 and 2.00, α = 1/12, M = 3.067, μ = √[C44(C11 - C12)/2], ROM of elemental values, Vegard's law) with tabulated elemental inputs W 15.807 Å³ / 532.55, 204.95, 163.13 GPa; Mo 15.524 / 450.02, 172.92, 125.03; Ta 17.985 / 266.32, 158.16, 87.36; Nb 17.952 / 252.7, 133.2, 30.97; V 14.020 / 232.4, 119.36, 45.95.
Answers: Q1, Q2
Access: read-directly
Source: R.E. Kubilay, A. Ghafarollahi, F. Maresca, W.A. Curtin, "High energy barriers for edge dislocation motion in body-centered cubic high entropy alloys", npj Comput. Mater. 7, 112 (2021), doi:10.1038/s41524-021-00577-7, https://infoscience.epfl.ch/record/287520/files/s41524-021-00577-7.pdf
Where: "Application to real alloys", Eqs. 7-8; Table 2 ("Single-element properties used in the reduced edge theory predictions")
Evidence: "M= 3.067 is the Taylor factor for an untextured BCC polycrystal deforming by edge dislocation motion"
Not claimed: a source or temperature for the volumes and elastic constants (Table 2 cites sources only for vacancy energies); see D5.

### C15
Claim: Kubilay et al. state that "to cover the full range of temperatures, Maresca et al. [ref. 8 = Acta Mater. 182 (2020)] proposed" a single form τy = τy0 exp{-(1/0.55)[(kT/ΔEb) ln(ε̇0/ε̇)]^0.91}, after noting the 2/3-power form holds only for τy/τy0 > 0.5.
Answers: Q1
Access: read-directly
Source: Kubilay et al. 2021 (as C14)
Where: Eq. 7 and the sentences before it; reference list entry 8
Evidence: "To cover the full range of temperatures, Maresca et al.8 proposed the approximate form"
Not claimed: the exact bracket placement (the raw PDF extraction is garbled; the reading above places the 0.91 exponent on the whole bracket); that the published Acta paper indeed contains this form (not opened; MC-v3 does not, D1).

### C16
Claim: For MoNbTaW (EAM-based full theory) Kubilay et al. report τy0 = 422 MPa from theory, 410 MPa from NEB and 470 MPa from direct atomistic simulation.
Answers: Q1
Access: read-directly
Source: Kubilay et al. 2021 (as C14)
Where: Results, Table 1
Evidence: theory 422, NEB 410, atomistic 470 MPa (as returned)
Not claimed: anything about the reduced model with experimental elemental inputs; these are 0 K shear stresses for an interatomic-potential alloy.

### C17
Claim: Lee et al. (2021) use the reduced Maresca-Curtin edge model with α = 1/12, ε̇0 = 10⁴ s⁻¹, ROM elastic constants, Vegard misfits and two temperature forms switching at σy/σy0 = 0.5, and report fitted coefficients Aσ = 0.0437, AE = 2.02 (NbTaTiV) and 0.0344, 1.93 (CrMoNbV), with averages over BCC HEAs of Aσ = 0.040 ± 0.004 and AE = 2.00 ± 0.2.
Answers: Q1
Access: read-directly
Source: C. Lee, F. Maresca, R. Feng, et al. (incl. P.K. Liaw, W.A. Curtin), "Strength can be controlled by edge dislocations in refractory high-entropy alloys", Nat. Commun. 12, 5474 (2021), doi:10.1038/s41467-021-25807-w, accepted manuscript https://par.nsf.gov/servlets/purl/10343625
Where: Eqs. 2-5 and surrounding text
Evidence: "Aσ = 0.040 ± 0.004 and AE = 2.00 ± 0.2"
Not claimed: a Taylor factor (not mentioned in what loaded); any W-Mo-Ta-Nb-V prediction.

### C18
Claim: Baruffi, Maresca and Curtin (2022) use the edge model with prefactors 0.040 and 2.00 but α = 1/6, Taylor factor 3.06, a single "ad-hoc" exponential temperature form with exponent 0.91 (no switch), and ROM elastic constants converted with the Bacon-Scattergood relations.
Answers: Q1
Access: read-directly
Source: C. Baruffi, F. Maresca, W.A. Curtin, "Screw vs. edge dislocation strengthening in body-centered-cubic high entropy alloys and implications for guided alloy design", MRS Commun. 12 (2022) 1111-1118, doi:10.1557/s43579-022-00278-2, https://pure.rug.nl/ws/files/274719702/s43579_022_00278_2.pdf
Where: Edge strengthening theory, Eqs. 6-11, p. 1113-1114
Evidence: "α = 1/6 that is slightly larger than that used by Maresca et al."; "3.06 is the Taylor factor"
Not claimed: predictions for any W-Mo-Ta-Nb-V alloy (none in the paper; studied systems are W-Ta, Ta-Nb-V, Ta-Hf-W, Nb-Hf-W-Ta-Zr, Nb-Ti, Nb-Ti-Mo); equations were partly garbled in extraction.

### C19
Claim: Xiao et al. (2023) used the reduced Maresca-Curtin model with ROM and Vegard's-law inputs on an Nb-Mo-Ta-W thin-film library and state that the predicted yield strength is not directly proportional to measured hardness, using it as a relative proxy.
Answers: Q1
Access: read-directly
Source: B. Xiao, Y. Lysogorskiy, A. Savan, et al., "Correlations of Composition, Structure, and Hardness in the High-Entropy Alloy System Nb-Mo-Ta-W", High Entropy Alloys & Materials 1 (2023) 110-119, doi:10.1007/s44210-022-00007-3
Where: Materials and Methods; Results ("Analysis of Mechanical Strength and Its Optimization")
Evidence: "The reduced Maresca–Curtin solid solution model ... was used."
Not claimed: any numerical prediction for the four validation alloys; constants (not stated in the text).

**Q1 status: partly answered.** The constants and forms in `pipeline/strength_model.py` (0.040, 2.00, α = 1/12, ε̇0 = 10⁴ s⁻¹, M = 3.067, two forms with switch at 0.5, ROM with μ = √[C44(C11-C12)/2], Vegard misfits) all appear in MC-v3 (C1-C7). Later papers from the same group vary α (1/6, C18), the Taylor factor (3.06, C11, C18), the temperature form (single exponential with exponent 0.91, C15, C18, attributed to the published Acta paper) and show alloy-specific prefactors scattering around 0.040/2.00 (C17). Room-temperature predictions found: MoNbTaW 954 MPa and MoNbTaWV 1347 MPa (Yin et al., C12); none found for NbTaVW or MoNbTaV. The published Acta version, which may differ from v3 in the temperature form (D1), was not opened.

---

## Q2. Elemental inputs

### C20
Claim: Featherston and Neighbours measured W at 300 K as C11 5.2327, C12 2.0453, C44 1.6072 (units printed garbled; consistent with 10¹² dyn cm⁻²), with B = 3.1078.
Answers: Q2
Access: read-directly
Source: F.H. Featherston, J.R. Neighbours, "Elastic Constants of Tantalum, Tungsten, and Molybdenum", Phys. Rev. 130 (1963) 1324, open copy (Naval Postgraduate School, Calhoun) https://core.ac.uk/download/81223136.pdf
Where: Table III, 300 K row
Evidence: C11 "5.2327", C12 "2.0453", C44 "1.6072"
Not claimed: units beyond the garbled caption (10¹² dyn cm⁻² = 100 GPa would give 523.27, 204.53, 160.72 GPa, reviewer arithmetic); the C12 header was garbled and reconstructed from column arithmetic.

### C21
Claim: Featherston and Neighbours measured Mo at 300 K as C11 4.4077, C12 1.7243, C44 1.2165 (same units), and note their Mo values differ substantially from Bolef and de Klerk's, attributing this to specimen-specific factors.
Answers: Q2
Access: read-directly
Source: Featherston & Neighbours 1963 (as C20)
Where: Table IV, 300 K row; Table V and discussion
Evidence: C11 "4.4077", C12 "1.7243", C44 "1.2165"
Not claimed: which Mo data set is more reliable.

### C22
Claim: Featherston and Neighbours measured Ta at 300 K as C11 2.6091, C12 1.5743, C44 0.8182 (same units).
Answers: Q2
Access: read-directly
Source: Featherston & Neighbours 1963 (as C20)
Where: Table II, 300 K row
Evidence: "2.6091", "1.5743", "0.8182"
Not claimed: the first-column header was missing in the extraction (identified as C11 by column arithmetic).

### C23
Claim: Featherston and Neighbours' room-temperature comparison table lists Bolef and de Klerk (1962) values C44 = 1.604, ½(C11-C12) = 1.598, B = 3.083 for W and 1.068, 1.510, 2.683 for Mo, and Bolef (1961) 0.825, 0.53, 1.96 for Ta.
Answers: Q2
Access: read-directly
Source: Featherston & Neighbours 1963 (as C20)
Where: Table V
Evidence: Mo, Bolef & de Klerk: "1.068 | 1.510 | 2.683"
Not claimed: C11 and C12 directly (only C44, C′, B are tabulated; column headers inferred by the reading).

### C24
Claim: Bolef measured at 27 °C, in 10¹¹ dyn cm⁻², V: c11 22.8, c12 11.9, c44 4.26; Nb: 24.6, 13, 2.87; Ta: 26.7, 16.1, 8.25.
Answers: Q2
Access: abstract-only
Source: D.I. Bolef, "Elastic Constants of Single Crystals of the bcc Transition Elements V, Nb, and Ta", J. Appl. Phys. 32 (1961) 100 (citation per Featherston & Neighbours Table V; OSTI record shows journal and volume only), https://www.osti.gov/biblio/4110197-elastic-constants-single-crystals-bcc-transition-elements-nb-ta
Where: OSTI abstract
Evidence: V "22.8 | 11.9 | 4.26" (10¹¹ dyn/cm², 27 °C)
Not claimed: uncertainties, specimen purity (full text not opened; DOI not seen).

### C25
Claim: Gong and Dal Corso tabulate experimental Mo elastic constants: Dickinson & Armstrong (273.15 K) 4637, 1578, 1092 kbar; Bolef & de Klerk (300 K) 4696, 1676, 1068; Katahara, Manghnani & Fisher (300 K) 4648, 1616, 1089; and Featherston & Neighbours at 0 K 4500.2, 1729.2, 1250.3.
Answers: Q2
Access: read-directly
Source: X. Gong, A. Dal Corso, "Ab initio quasi-harmonic thermoelasticity of molybdenum at high temperature and pressure", arXiv:2406.16634v1 (2024), https://arxiv.org/html/2406.16634v1
Where: Table II
Evidence: "Expt. 18 | 300 | 4648 | 1616 | 1089" (Katahara et al., J. Phys. F 9, 773 (1979))
Not claimed: that these are copied correctly from the primaries (secondary compilation; primaries not opened). 1 kbar = 0.1 GPa (Katahara 300 K = 464.8, 161.6, 108.9 GPa, reviewer arithmetic).

### C26
Claim: NBS Circular 539 gives powder-diffraction lattice constants a0 = 3.1648 Å for W, 3.1472 Å for Mo and 3.3058 Å for Ta at 25 °C (table headers say 26 °C).
Answers: Q2
Access: read-directly
Source: H.E. Swanson, E. Tatge, Standard X-ray Diffraction Powder Patterns, Vol. I, NBS Circular 539 (1953), https://nvlpubs.nist.gov/nistpubs/Legacy/circ/nbscircular539v1.pdf
Where: Tables 13 (W, p. 28), 8 (Mo, p. 20-21), 14 (Ta, p. 30)
Evidence: W "3.1648", Mo "3.1472", Ta "3.3058"
Not claimed: Nb or V (not in Vol. I; only the first 100000 of 275192 characters were read, but the three entries were found there).

### C27
Claim: The American Mineralogist Crystal Structure Database lists bcc V with a = 3.0241 Å at 25 °C (James and Straumanis 1960), 3.0236 Å (Straumanis 1959), 3.0240 Å (Wyckoff 1963) and 3.04 Å (Hull 1922).
Answers: Q2
Access: read-directly
Source: AMCSD vanadium entries, https://rruff.info/AMS/minerals/Vanadium (primary: W.J. James, M.E. Straumanis, J. Electrochem. Soc. 107 (1960) 69, "Lattice parameter and expansion coefficient of vanadium")
Where: database entries 1-4
Evidence: "a = 3.0241 Å ... Sample: at T = 25C"
Not claimed: the primary paper itself (not opened); purity of the samples.

### C28
Claim: The Crystallography Open Database entry 1539041 gives Nb a = 3.3063 Å from Roberge (1975), a paper on the Nb lattice parameter between 4.2 and 300 K.
Answers: Q2
Access: read-directly
Source: COD 1539041, https://www.crystallography.net/cod/1539041.html (primary: R. Roberge, "Lattice parameter of niobium between 4.2 and 300 K", J. Less-Common Met. 40 (1975) 161-164)
Where: database entry
Evidence: "3.3063 Å"
Not claimed: the temperature of this specific entry (not shown on the page); the primary paper (not opened).

### C29
Claim: Baruffi et al. Table I (elemental properties stated to follow Lee et al.) lists a / C11 / C12 / C44 as W 3.162 Å / 533 / 205 / 163 GPa; Mo 3.1437 / 450 / 173 / 125; Ta 3.301 / 266 / 158 / 87; Nb 3.299 / 253 / 133 / 31; V 3.038 / 232 / 119 / 46.
Answers: Q2
Access: read-directly
Source: Baruffi et al. 2022 (as C18)
Where: Table I, p. 1113
Evidence: V "3.038 | 232 | 119 | 46"
Not claimed: primary sources or temperature for these values (none given in the table); these are secondary values used by the modelling group.

Side-by-side (numbers only, no verdict). Code = `pipeline/strength_model.py`. F&N 300 K converted at 10¹² dyn cm⁻² = 100 GPa and Bolef at 10¹¹ dyn cm⁻² = 10 GPa (reviewer arithmetic).

| | Code a (Å) | Open source a (Å) | Code C11/C12/C44 (GPa) | Room-T measured C11/C12/C44 (GPa) | Curtin-group inputs (C14) |
|---|---|---|---|---|---|
| W | 3.1652 | 3.1648 (C26) | 523.3/204.5/160.7 | 523.3/204.5/160.7 (F&N 300 K, C20) | 532.55/204.95/163.13 |
| Mo | 3.1470 | 3.1472 (C26) | 465.0/163.0/109.0 | 440.8/172.4/121.7 (F&N, C21); 464.8/161.6/108.9 (Katahara, C25); 469.6/167.6/106.8 (Bolef & de Klerk, C25) | 450.02/172.92/125.03 (= F&N 0 K, D5) |
| Ta | 3.3029 | 3.3058 (C26) | 266.0/158.0/87.4 | 260.9/157.4/81.8 (F&N, C22); 267/161/82.5 (Bolef, C24) | 266.32/158.16/87.36 |
| Nb | 3.3004 | 3.3063 (C28, T not shown) | 246.5/134.5/28.7 | 246/130/28.7 (Bolef, C24) | 252.7/133.2/30.97 |
| V | 3.0240 | 3.0241 at 25 °C (C27) | 231.0/120.0/43.2 | 228/119/42.6 (Bolef, C24) | 232.4/119.36/45.95 |

**Q2 status: partly answered.** Room-temperature primary values were read for W, Mo, Ta (Featherston & Neighbours, full text), V, Nb, Ta (Bolef 1961, abstract only) and Mo from three more measurements via a secondary table. Lattice parameters at about 25 °C were found for W, Mo, Ta (NBS) and V (AMCSD); for Nb only a COD entry with no stated temperature. Simmons & Wang, Katahara et al. and Bolef & de Klerk full texts were not opened. Measured Mo constants disagree between experiments by up to about 30 GPa in C11 (C21, C25).

---

## Q3. Validation data: NbTaVW 1530 MPa

### C30
Claim: Gorsse et al.'s database lists NbTaVW as BCC, HV 492, compression test, 1530 MPa, strain 12 %, citing Yao et al. MSEA 674 (2016) 203-211, alongside MoNbTaW 1058 MPa, MoNbTaVW 1246 MPa (Senkov et al. 2011) and MoNbTaV 1525 MPa (Yao et al. Entropy 2016).
Answers: Q3
Access: read-directly
Source: S. Gorsse, M.H. Nguyen, O.N. Senkov, D.B. Miracle, "Database on the mechanical properties of high entropy alloys and complex concentrated alloys", Data in Brief 21 (2018) 2664-2678, doi:10.1016/j.dib.2018.11.111, PDF https://rcastoragev2.blob.core.windows.net/cd112831df1624214e875d7df7715d66/PMC6290247.pdf
Where: Table 1 (room temperature), ref. [76]
Evidence: "NbTaVW | 76 | BCC | (12.9) | 492 | C | 1530 | – | 12"
Not claimed: processing state or strain rate (the table gives neither); that 1530 is unambiguously σy rather than σmax (D9). Secondary compilation, not the primary.

### C31
Claim: The Yao et al. (MSEA 2016) abstract states that a single BCC solid solution phase was confirmed in the as-cast ingots of the NbTaV-(Ti,W) alloys.
Answers: Q3
Access: abstract-only
Source: H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang, "NbTaV-(Ti,W) refractory high-entropy alloys: Experiments and modeling", Mater. Sci. Eng. A 674 (2016) 203-211, doi:10.1016/j.msea.2016.07.102, abstract via https://opact.sdu.edu.tr/vufind/SummonRecord/FETCH-LOGICAL-c540t-aa8133d9efb0fa421a079ac242f3a191bb5e2277601d5d333c095cfad931e15c3
Where: Abstract (truncated in the record)
Evidence: "a single body-centered cubic solid solution phase was experimentally confirmed in the as-cast ingots"
Not claimed: that the mechanical tests were on as-cast material; any NbTaVW strength, test method or strain rate (not in the visible abstract). See also run-2026-11-11 C8.

**Q3 status: partly answered.** An open secondary compilation lists NbTaVW at 1530 MPa in compression and attributes it to Yao et al. (C30). Missing because the primary full text could not be opened: the value as printed in the primary (table or figure), whether it is the 0.2 % offset yield, the specimen condition actually tested (the abstract mentions as-cast ingots only for phase identification), the strain rate and specimen geometry. A web page (alloyfyi.com) listing "1530.0 MPa, CAST" with no reference was seen but not recorded as a claim.

---

## Q4. High temperature and limits

### C32
Claim: Maresca and Curtin state that their predictions for MoNbTaW and MoNbTaVW at high temperature are lower than experiments, that the measured plateau in yield strength between 900 K and 1300 K is not predicted, and yet that edge strengthening agrees fairly well with the measured high-temperature behaviour.
Answers: Q4 (also P1)
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 4 (comparison with Fig. 1 data); Appendix C cited for a possible plateau explanation
Evidence: "The predictions are lower than experiments."; "a plateau in yield strength in the range 900K–1300K not predicted by the theory"
Not claimed: the size of the underprediction in MPa (Fig. 1 only, not read as numbers); the paper lists omitted contributions (Hall-Petch ≈50 MPa, solute-solute interactions, cast microstructure, impurities).

### C33
Claim: MC-v3 Fig. 1 compares predictions (solid lines) with experiments (open symbols, ref. [3]) for BCC HEAs at 800-1900 K; the text identifies the experimental HEAs as MoNbTaW and MoNbTaVW.
Answers: Q4
Access: read-directly
Source: MC-v3 (as C1)
Where: Fig. 1 caption; Section 1
Evidence: "Yield strength of BCC high entropy alloys and Ni-based superalloys at high temperatures 800-1900K."
Not claimed: any number (figure values not extracted).

### C34
Claim: Gorsse et al. list measured compressive yield stresses of MoNbTaW as 548, 506, 421 and 405 MPa and of MoNbTaVW as 842, 735, 656 and 477 MPa at 1000, 1200, 1400 and 1600 °C.
Answers: Q4
Access: read-directly
Source: Gorsse et al. 2018 (as C30)
Where: Table 2, ref. [73] (Senkov, Wilks, Scott, Miracle, Intermetallics 19 (2011) 698-706)
Evidence: MoNbTaVW "1600 °C, 477 MPa"
Not claimed: model predictions at these temperatures. Secondary; run-2026-11-11 D1 notes the 1600 °C V-alloy value appears as 470 (text) and 477 (table) in the Senkov preprint.

### C35
Claim: Kubilay et al. compare reduced-theory predictions with experiments at 0, 1000 and 1200 °C for the MoNbTaW(Ti)(V) family and say quantitative agreement is not as good as for the Hf-containing family, but that the theory captures the strengthening from V and these alloys continue to follow the theory trend up to 1200 °C.
Answers: Q4
Access: read-directly
Source: Kubilay et al. 2021 (as C14)
Where: "Application to real alloys"; Fig. 7b
Evidence: "the quantitative agreement is not as good"; "continue to agree with the theory trend"
Not claimed: numbers (figure only); the temperature form used here is the single 0.91-exponent form (C15), not the two-form switch.

### C36
Claim: Maresca and Curtin argue that, unlike pure BCC metals and dilute alloys whose low-temperature strength is controlled by screw dislocations, BCC HEAs can be controlled by edge dislocations, especially at high temperatures, with edge dominance emerging at moderate temperatures.
Answers: Q4
Access: read-directly
Source: MC-v3 (as C1)
Where: Abstract; Section 1
Evidence: "Edge dominance emerges at moderate temperatures and accurately predicts the high-temperature behavior"
Not claimed: that edge glide controls room-temperature strength.

### C37
Claim: For MoNbTaW at 296 K the edge theory predicts an activation volume of 36b³, which the authors note is in the range of other BCC alloys controlled by screw motion, and they say that even at low T, where edge and screw strengths may be comparable, the edge model agrees well with experiment.
Answers: Q4
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 4
Evidence: "we predict V=36b^3, which happens to be in the range of other BCC alloys controlled by screw motion"
Not claimed: a screw-strength calculation for these alloys (none in this paper).

### C38
Claim: MC-v3 states that at high temperature screw-dislocation strength is dominated by jog pinning, which thermal vacancies defeat, so edge versus screw control may explain differences among BCC HEAs.
Answers: Q4
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 7
Evidence: "the high-temperature strength of the screw dislocation is dominated by pinning due to jogs"
Not claimed: a quantitative transition temperature.

### C39
Claim: In room-temperature-deformed NbTaTiV and CrMoNbV, TEM found predominantly edge dislocations (58 of 77 and 23 of 41), and the authors state that MoNbTaW and MoNbTaVW "have been predicted to be controlled by edge dislocations".
Answers: Q4
Access: read-directly
Source: Lee et al. 2021 (as C17)
Where: Results (TEM and neutron diffraction); Discussion
Evidence: "predominantly of edge character (58 of 77, or 75%)"
Not claimed: any observation on MoNbTaW or MoNbTaVW themselves (prediction cited, not measured).

### C40
Claim: In equiatomic VNbMoTaW deformed at room temperature, screw and edge segments were present almost equally; a screw model gave 1242 MPa and an edge model (Rao et al. formulation) 1210 MPa, both about 25-30 % below the measured yield strength, and the authors conclude kink migration (a screw mechanism) is rate-controlling at room temperature.
Answers: Q4
Access: read-directly
Source: T. Tsuru, S. Han, S. Matsuura, Z. Chen, K. Kishida, I. Iobzenko, S.I. Rao, C. Woodward, E.P. George, ..., H. Inui, "Intrinsic factors responsible for brittle versus ductile nature of refractory high-entropy alloys", Nat. Commun. 15, 1706 (2024), doi:10.1038/s41467-024-45639-8, https://link.springer.com/article/10.1038/s41467-024-45639-8
Where: Results ("Deformation behaviors at room temperature and 77 K"; "Yield strength modeling"); Discussion; Methods (processing)
Evidence: "screw and edge dislocation segments are present almost equally here regardless of the operative slip plane"
Not claimed: that the edge model is the reduced Maresca-Curtin model (it is attributed to Rao et al.); the measured value (figure only); applicability to as-cast material (specimens were annealed at about 2000 °C for 48 h, grain size 496 µm, tested at 1 × 10⁻⁴ s⁻¹). Only the first 100000 of 136023 characters were read; the second part held references only.

### C41
Claim: In equiatomic NbMoTaW micropillars tested at room temperature, HRTEM showed edge dislocations in several grains, and the authors relate the governing mechanism to Peierls-type activation of edge or screw dislocations.
Answers: Q4
Access: read-directly
Source: M. Pozuelo, J. Marian, "Microscale deformation controlled by compositional fluctuations in equiatomic Nb-Mo-Ta-W alloys", Mater. Sci. Eng. A 856 (2022) 143892, doi:10.1016/j.msea.2022.143892, accepted manuscript https://par.nsf.gov/servlets/purl/10362786
Where: Sections 3.3 and 4.2; Fig. 7
Evidence: "the governing mechanism is related to a Peierls type activation of edge or screw dislocations"
Not claimed: that edge dislocations control bulk yield strength; micropillar results may not transfer to bulk.

### C42
Claim: Yin et al. suggest that the underprediction of V-free alloys may reflect a change from edge-controlled strength (with V) to screw-controlled strength (without V) in some alloys.
Answers: Q4
Access: read-directly
Source: Yin et al. 2020 (as C11)
Where: Section 3.2
Evidence: "change from control of the alloy strength by edge dislocations (with V) to screw dislocations (without V) in some alloys"
Not claimed: a demonstration; it is offered as a possible explanation.

### C43
Claim: Baruffi et al. state that no theories capture the approximate plateau in yield strength versus temperature at intermediate temperatures, and classify Ta42Nb40V18 as edge-controlled with the edge theory in good agreement with experiment though slightly low at high temperature.
Answers: Q4
Access: read-directly
Source: Baruffi et al. 2022 (as C18)
Where: p. 1114-1115; Table II; Fig. 2(a)
Evidence: "the edge theory is in good agreement with experiments, although slightly low at high temperature"
Not claimed: anything about MoNbTaW, MoNbTaVW, NbTaVW or MoNbTaV (not studied).

**Q4 status: partly answered.** Maresca and Curtin report their predictions for MoNbTaW and MoNbTaVW fall below experiment at high temperature and miss the 900-1300 K plateau (C32), but say agreement is "fairly well" overall; Kubilay et al. find weaker quantitative agreement for this family up to 1200 °C (C35). Predicted MPa values at 1000-1600 °C are only in figures and were not extracted; measured values are in C34. On room-temperature control, sources disagree: the Curtin group argues edge control is possible even at low T (C36, C37, C39), while Tsuru et al. find equal edge and screw segments, similar edge and screw strengths and screw-type kink migration as rate-controlling in annealed VNbMoTaW (C40); Yin et al. suggest V-free alloys may be screw-controlled (C42). No source read states what this means quantitatively for room-temperature predictions of the edge model.

---

## Project statements

- **P1** (predictions below experiment at high T; 900-1300 K plateau not reproduced): matches C32 in substance. The same paragraph also says edge strengthening "agrees fairly well" with high-temperature behaviour. The statement concerns MoNbTaW and MoNbTaVW in MC-v3 (C33).
- **P2** (DFT row of Table 2): the values quoted in the brief match MC-v3 Table 2 (C9) as read: a 3.192, C11 338, C12 164, C44 51; ΔV Mo -0.824, Nb 1.848, Ta 1.882, V -2.380, W -0.526. Vegard/ROM C44 for the same alloy is 90.5 (C9). Units not printed in the extraction.
- **P3** (barriers 2.2-2.5 eV for MoNbTaW / MoNbTaVW): see C44.
- **P4** (V has the largest misfit volume of the five): MC-v3 Table 2 DFT row has |ΔV_V| = 2.380, the largest of the five (C9); run-2026-11-11 C1 quotes "V has the largest misfit volume". Yin et al. note Cr is smaller than V among bcc elements (C13 context, Section 3.2), which does not affect the five-element statement.

### C44
Claim: Maresca and Curtin give zero-stress energy barriers ΔEb = 2.2 eV and 2.5 eV for the MoNbTaW and MoNbTaVW alloys, and ΔEb ≈ 1.9-2.5 eV for the alloys simulated in Section 3.
Answers: P3 (also Q1)
Access: read-directly
Source: MC-v3 (as C1)
Where: Section 4 (paragraph on strength retention); Section 3
Evidence: "ΔE_b=2.2 eV, 2.5 eV"
Not claimed: an explicit mapping of each value to one alloy (the text lists them in the order MoNbTaW, MoNbTaVW but does not pair them explicitly, as read); that these come from the reduced model with ROM/Vegard inputs (the inputs behind these values were not identified in what loaded).

---

## Search log

```
Query: (direct fetch) ar5iv.labs.arxiv.org/html/1901.02100, offsets 0, 100000, 180000, 200000  Tool: WebFetch  Date: 2026-11-13
Opened: full ar5iv page (209487 characters) across four reads
Blocked: none (each read covered at most 100000 characters; parts read separately)
Stopped: no

Query: (direct fetch) arxiv.org/abs/1901.02100 and arxiv.org/pdf/1901.02100  Tool: WebFetch  Date: 2026-11-13
Opened: abstract page (version history, DOI); v3 PDF (equations, M, B)
Blocked: none
Stopped: no

Query: "Yin Maresca Curtin "Vanadium is an optimal element for strengthening" high entropy alloys arXiv"  Tool: WebSearch  Date: 2026-11-13
Opened: infoscience.epfl.ch/record/277447 (record; preprint file link not given); research.rug.nl publication page; research.rug.nl publisher PDF (read three times)
Blocked: none
Stopped: no

Query: "Baruffi Maresca Curtin "Screw vs. edge dislocation strengthening in body-centered-cubic high entropy alloys" arXiv"  Tool: WebSearch  Date: 2026-11-13
Opened: pure.rug.nl s43579_022_00278_2.pdf (read twice)
Blocked: none
Stopped: no

Query: "Hu Sundar Ogata Qi "Screening of generalized stacking fault energies, surface energies and intrinsic ductile potency" OR "solid solution strengthening" refractory high entropy alloys Maresca Curtin model DFT elastic constants MoNbTaW prediction"  Tool: WebSearch  Date: 2026-11-13
Opened: none (results not on point)
Blocked: none
Stopped: no

Query: "MoNbTaW dislocation character TEM room temperature compression screw dislocations edge dislocations refractory high entropy alloy"  Tool: WebSearch  Date: 2026-11-13
Opened: none from this list directly (par.nsf.gov 10343625 opened under next query)
Blocked: none
Stopped: no

Query: "Lee Maresca Feng Curtin Liaw "Strength can be controlled by edge dislocations in refractory high-entropy alloys" Nature Communications"  Tool: WebSearch  Date: 2026-11-13
Opened: par.nsf.gov/servlets/purl/10343625 (Lee et al. 2021 accepted manuscript)
Blocked: pmc.ncbi.nlm.nih.gov not tried (blocked in run-2026-11-11)
Stopped: no

Query: "NbMoTaW dislocations deformed room temperature TEM "screw" character high-entropy alloy micropillar OR compression Couzinié OR Zou"  Tool: WebSearch  Date: 2026-11-13
Opened: link.springer.com s41467-024-45639-8 (Tsuru et al. 2024; 0-100000 and 100000-136023 characters; Methods not in either part as returned); par.nsf.gov/servlets/purl/10362786 (Pozuelo & Marian 2022)
Blocked: Tsuru et al. Methods section (edge-model constants) not in the extracted text
Stopped: no

Query: "Maresca Curtin edge model predicted yield strength MoNbTaW high temperature 1200 °C 1400 °C 1600 °C comparison Senkov experiment underestimate"  Tool: WebSearch  Date: 2026-11-13
Opened: infoscience.epfl.ch s41524-021-00577-7.pdf (Kubilay et al. 2021; read four times)
Blocked: aminer.org record "Solid solution strengthening of the body-centered cubic refractory complex concentrated alloy, MoNbTaW" (site metadata only, no paper content)
Stopped: no

Query: "Maresca Curtin "Theory of screw dislocation strengthening in random BCC alloys from dilute to" arXiv"  Tool: WebSearch  Date: 2026-11-13
Opened: none (records only; not needed after Lee/Tsuru)
Blocked: none
Stopped: no

Query: "Kubilay Ghafarollahi Maresca Curtin "High energy barriers for edge dislocation motion" arXiv"  Tool: WebSearch  Date: 2026-11-13
Opened: none new (already read the open publisher PDF)
Blocked: none
Stopped: no

Query: "single crystal elastic constants tungsten molybdenum room temperature Featherston Neighbours Bolef de Klerk C11 C12 C44 pdf"  Tool: WebSearch  Date: 2026-11-13
Opened: core.ac.uk/download/81223136.pdf (Featherston & Neighbours 1963, read twice); osti.gov/biblio/4718167 (record, no numbers); next.sciencegate.app 10.1063/1.1728952 (Bolef & de Klerk record, no abstract or numbers)
Blocked: Bolef & de Klerk full text (not found open)
Stopped: no

Query: "elastic constants vanadium niobium tantalum single crystal ultrasonic room temperature C11 C12 C44 Bolef 1961 Katahara Manghnani Fisher"  Tool: WebSearch  Date: 2026-11-13
Opened: osti.gov/biblio/4110197 (Bolef 1961, abstract)
Blocked: full text of Bolef 1961; Katahara et al. 1979 (not found open)
Stopped: no

Query: "molybdenum single crystal elastic constants room temperature C11 4.65 OR 465 GPa C12 1.63 OR 163 C44 1.09 OR 109 ultrasonic"  Tool: WebSearch  Date: 2026-11-13
Opened: scilit.com record for Dickinson & Armstrong 1967 (abstract, no absolute values); arxiv.org/html/2406.16634v1 (Gong & Dal Corso, read twice)
Blocked: Dickinson & Armstrong full text
Stopped: no

Query: "room temperature lattice parameter vanadium bcc 3.024 OR 3.0274 OR 3.030 Å X-ray precision measurement high purity"  Tool: WebSearch  Date: 2026-11-13
Opened: rruff.info/AMS/minerals/Vanadium; crystallography.io/structure/9012770 (empty page, no data)
Blocked: rruff.info/AMS/minerals/Tantalum, /Tungsten, /Molybdenum, /Niobium (constructed URLs, not on session allowlist)
Stopped: no

Query: "rruff American Mineralogist Crystal Structure Database tungsten OR molybdenum OR tantalum OR niobium native element cell parameter"  Tool: WebSearch  Date: 2026-11-13
Opened: none
Blocked: rruff.geo.arizona.edu/AMS/minerals/Tantalum (robots_disallowed)
Stopped: no

Query: "precision lattice parameters tungsten molybdenum tantalum niobium 25 °C Straumanis X-ray 3.1652 3.1470 3.3058 3.3004"  Tool: WebSearch  Date: 2026-11-13
Opened: nvlpubs.nist.gov nbscircular539v1.pdf (first 100000 of 275192 characters)
Blocked: none
Stopped: no

Query: "niobium lattice parameter room temperature 3.3004 Å precision X-ray high purity niobium bcc"  Tool: WebSearch  Date: 2026-11-13
Opened: crystallography.net/cod/1539041.html
Blocked: none
Stopped: no

Query: (direct fetch) scholar.google.com/scholar?q="NbTaV-(Ti,W) refractory high-entropy alloys: Experiments and modeling"  Tool: WebFetch  Date: 2026-11-13
Opened: none
Blocked: constructed Google Scholar URL not on session allowlist
Stopped: no

Query: "NbTaV-(Ti,W) refractory high-entropy alloys experiments and modeling"  Tool: WebSearch (allowed_domains scholar.google.com)  Date: 2026-11-13
Opened: none (results were author profile pages only)
Blocked: none
Stopped: no

Query: ""NbTaV-(Ti,W)" refractory high-entropy alloys experiments and modeling Yao Qiao Gao Hawk osti.gov full text"  Tool: WebSearch  Date: 2026-11-13
Opened: none new
Blocked: no full text found
Stopped: no

Query: "osti.gov NbTaV Ti W refractory high entropy alloys experiments modeling NETL 2016 Materials Science Engineering A 674"  Tool: WebSearch  Date: 2026-11-13
Opened: none
Blocked: no OSTI full text found
Stopped: no

Query: "NbTaVW yield strength 1530 MPa compressive as-cast"  Tool: WebSearch  Date: 2026-11-13
Opened: alloyfyi.com mpea-nb1-ta1-v1-w1 (no reference, self-contradictory description; not recorded as a claim); pdf.arxiv.org 2008.11671 (Maresca et al. preprint of Lee et al.; no NbTaVW value)
Blocked: none
Stopped: no

Query: "Couzinié Senkov Miracle Dirras "Comprehensive data compilation on the mechanical properties of refractory high-entropy alloys" Data in Brief 2018"  Tool: WebSearch  Date: 2026-11-13
Opened: doaj.org record (no link)
Blocked: ncbi.nlm.nih.gov/pmc PMC6247412 (302 redirect to pmc.ncbi.nlm.nih.gov, which returned a reCAPTCHA page)
Stopped: no

Query: "sciencedirect "Comprehensive data compilation on the mechanical properties of refractory high-entropy alloys" S2352340918313143 OR 10.1016/j.dib.2018.10.071"  Tool: WebSearch  Date: 2026-11-13
Opened: oskar-bordeaux.fr handle 153253 (record, no PDF)
Blocked: no open copy of Couzinié et al. found
Stopped: no

Query: "hal.science "Database on the mechanical properties of high entropy alloys and complex concentrated alloys" Gorsse pdf"  Tool: WebSearch  Date: 2026-11-13
Opened: rcastoragev2.blob.core.windows.net PMC6290247.pdf (Gorsse et al. 2018)
Blocked: none
Stopped: no

Query: ""NbTaV-(Ti,W)" refractory high-entropy alloys sciencedirect abstract arc melted strain rate compression"  Tool: WebSearch  Date: 2026-11-13
Opened: opact.sdu.edu.tr record (abstract, truncated)
Blocked: primary full text not found
Stopped: no

Query: "reduced Maresca-Curtin model predicted yield strength NbTaVW OR MoNbTaV OR "NbMoTaV" room temperature comparison experiment high-throughput refractory alloys"  Tool: WebSearch  Date: 2026-11-13
Opened: link.springer.com s44210-022-00007-3 (Xiao et al. 2023); archive.materialscloud.org fcafh-h1367 (dataset record only)
Blocked: dataset files (842 MiB .mat) not opened
Stopped: yes (enough coverage for the brief; remaining gaps need paywalled sources)
```

Not opened (leads only, no claims made from them): published Acta Mater. 182 (2020)
235-249 version of Maresca & Curtin; Maresca & Curtin, "Theory of screw dislocation
strengthening in random BCC alloys from dilute to 'High-Entropy' alloys", Acta Mater. 182
(2020) 144 (records only); Materials Cloud dataset materialscloud:2021.65 (10 million
predicted strengths at 1300 K, may include W-Mo-Ta-Nb-V compositions); arXiv:2511.16057
(high-throughput RHEA exploration, title only); Couzinié et al. Data in Brief 21 (2018)
1622-1641; Simmons & Wang (1971) handbook; Tsuru et al. 2024 Methods and Supplementary
Information.

---

## Needs Sean (university access)

1. **IMPERATIVE.** F. Maresca, W.A. Curtin, "Mechanistic origin of high strength in
   refractory BCC high entropy alloys up to 1900K", Acta Materialia 182 (2020) 235-249,
   doi:10.1016/j.actamat.2019.10.015.
   Needed: (a) the temperature/strain-rate equations as published (the equivalents of
   arXiv v3 Eqs. 11-12): is it two forms with a switch at τy/τy0 = 0.5, or a single
   exp{-(1/0.55)[(kT/ΔEb) ln(ε̇0/ε̇)]^0.91} form, and if both, which is used for the
   predictions in Section 5 and Figs. 1 and 5; (b) the Section 5 reduced-model equations
   (prefactors 0.040 and 2.00, α); (c) the bulk modulus expression (with or without 1/3);
   (d) the Taylor factor; (e) Table 2 equiatomic MoNbTaVW Vegard/ROM row.
   Why imperative: the project's switch rule and its 922/1411/1425/1317 MPa depend on (a),
   open sources disagree (D1: arXiv v3 and Lee 2021 use the switch; Kubilay 2021 and
   Baruffi 2022 use the single 0.91 form and Kubilay attributes it to this paper), and no
   open copy of the published version was found.

2. **IMPERATIVE.** H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang,
   "NbTaV-(Ti,W) refractory high-entropy alloys: Experiments and modeling", Materials
   Science and Engineering A 674 (2016) 203-211, doi:10.1016/j.msea.2016.07.102.
   Needed: the NbTaVW room-temperature compressive yield strength as printed (table and/or
   stress-strain figure), whether it is the 0.2 % offset yield, the specimen condition
   tested (as-cast or heat-treated), strain rate, specimen size, and the measured
   composition. Why imperative: 1530 MPa is one of the project's four validation points and
   enters the reported errors; the only open source (Gorsse et al. 2018, C30) gives the
   value but not condition or strain rate, and the brief (Q3) asks for these explicitly.

3. OPTIONAL. D.I. Bolef, J. de Klerk, "Elastic Constants of Single-Crystal Mo and W between
   77° and 500°K", J. Appl. Phys. 33 (1962) 2311-2314, doi:10.1063/1.1728952. Needed: 300 K
   C11, C12, C44 for Mo and W. Open secondary values exist (C23, C25).

4. OPTIONAL. K.W. Katahara, M.H. Manghnani, E.S. Fisher, J. Phys. F: Met. Phys. 9 (1979)
   773 (citation as printed in Gong & Dal Corso ref. 18; title and DOI not seen).
   Needed: 300 K C11, C12, C44 of pure Mo, Nb, Ta, W. Mo covered by C25.

5. OPTIONAL. D.I. Bolef, "Elastic Constants of Single Crystals of the bcc Transition
   Elements V, Nb, and Ta", J. Appl. Phys. 32 (1961) 100 (DOI not seen). Needed: full table
   with uncertainties; abstract values already read (C24).

6. OPTIONAL. G. Simmons, H. Wang, Single Crystal Elastic Constants and Calculated Aggregate
   Properties: A Handbook, MIT Press (1971). Needed: recommended room-temperature C11, C12,
   C44 and lattice constants for W, Mo, Ta, Nb, V (the handbook the Curtin group cites for
   atomic volumes, C13).

7. OPTIONAL. R. Roberge, "Lattice parameter of niobium between 4.2 and 300 K", J.
   Less-Common Met. 40 (1975) 161-164 (DOI not seen). Needed: Nb lattice parameter at
   293-300 K (only an undated COD value was read, C28).
