# Integrity audit: run 2026-11-13

Integrity auditor (stage 4, final gate), 2026-11-13. I did not write any earlier stage.

**This is an in-project AI audit, not peer review.** The reviewer, fact-checker, note-writer and
this auditor are all AI agents. Agents that check other agents can share the same blind spots,
for example the same model-mediated reading of a PDF (WebFetch returns a model's extraction, not
the raw text). An agreement between stages is therefore weaker evidence than an independent
human reading of the primary source. The one exception in this run is the Yao et al. manuscript,
which I read as page images of the PDF the project owner downloaded, not through WebFetch.

## Scope and method

Inputs read in full: `brief.md`, `claims.md`, `factcheck.md`, `notes.md`, `sean-sources.md`;
project files `reports/strength_model.md`, `pipeline/strength_model.py`,
`tests/test_strength_model.py`, `README.md`, `reports/finalists.md`; and lines 1-70 of
`docs/research/run-2026-11-11/notes.md` (to check the line numbers in correction #6). I also read
all 31 pages of the Yao et al. accepted manuscript PDF (`/mnt/user-data/uploads/95b801e2-1482331.pdf`)
as page images.

I checked every sentence of `notes.md`: the Summary, Q1-Q4 (literature, comparison and next-step
bullets), the Q2 table, all 10 rows of "Corrections to the project", "Checked and not a
correction", Open leads, Open questions, References and Needs Sean. That is about 175 prose
sentences or bullets, 5 table rows, 10 correction rows, 16 reference entries and 7 Needs Sean
items.
- **Literature sentences.** Each tag traced to `claims.md` and its `factcheck.md` verdict. All tags
  resolve to SUPPORTED or PARTIAL claims. The four PARTIAL claims (C15, C17, C24, C33) appear only
  in the fact-checker's corrected wording. The "factcheck Dn / Pn / side-by-side" references
  resolve to the cited passages.
- **Project sentences.** Every number traced to the cited project file:
  - validation predictions 1411/922/1425/1317, measured values 1246/1058/1530/1525, errors
    +165/-136/-105/-208, MAE 153, ρ = 0.80;
  - continuous variant 1497/978/1512/1396, MAE 120;
  - finalists 573/533/517/491/428 (1000 °C) and 445/411/397/374/315 (1300 °C);
  - code constants (`ALPHA`, `EPS0`, `TAYLOR`, `LATTICE_A`, `ELASTIC`, `B = (c11+2c12)/3`, switch
    `low if low > 0.5 else high`);
  - the test's 2.0-3.2 eV band and the DFT misfit volumes.

  All match.
- **Correction-table line numbers.** Every cited line contains the quoted current wording:
  - strength_model.py l. 5, 11-12, 19, 20-21, 36-38, 43, 112-114, 163-164, 182-189, 206-207,
    212-215, 219-221;
  - strength_model.md l. 3, 20, 34, 38, 39, 41;
  - test l. 10, 19-20, 31;
  - README l. 16-17, 95-96, 131-135;
  - run-2026-11-11 notes l. 9, 63.

  For row 3, l. 11-12 of the docstring hold the equations rather than the phrase "paper's rule",
  but they are the right place for the "(arXiv v3)" label. For row 4, README l. 131-135 has no
  edge-only sentence; the row correctly says to add one.

## Defects found and fixed in notes.md (19 defects, 16 edits)

All fixes delete or weaken text. Where a sentence was reworded, the new wording uses only content
already in `claims.md`, `factcheck.md` or the cited project file.

1. **Summary: "Several later papers by the same group credit the published paper ... [C15, C18]".**
   C18 (Baruffi) uses the 0.91 form as an "ad-hoc form" with no reference (factcheck D1; I
   confirmed this myself). Reworded to "Later papers, two of them co-authored by Curtin, credit the
   published paper ... [C15; factcheck D1]; Baruffi et al. use that form without a reference
   [C18]".
2. **Summary: "Our alloys sit close to that switch at room temperature (strength_model.md)".**
   Deleted. The report does say this, but its own numbers contradict it (see "Project-file issues
   found by the audit", A1). The claim is kept in Q1, attributed to the report (#10).
3. **Summary: "No source gives ... and nobody has computed them".** An absolute claim of absence.
   Weakened to "No checked source gives ...", and "nobody has computed them" was deleted.
4. **Summary and Q2: the code's Ta Cij "equal" the F&N 0 K values.** 266.0/158.0/87.4 against
   266.32/158.16/87.36 is a match to within 0.4 GPa, not equality at the printed precision. Changed
   to "match" (2 places).
5. **Summary: "Ta and Nb lattice parameters ... do not match the 25 °C X-ray values".** The Nb
   value (COD, C28) has no stated temperature. Reworded to "(25 °C for Ta; temperature not shown
   for Nb)".
6. **Summary: "the authors argue that edge dislocations can control strength even at low
   temperature [C37]".** This was stronger than C37, which says only that the edge *model* agrees
   with experiment at low T, "where edge and screw strengths may be comparable". C36 says "especially
   at high temperatures". Weakened to C37's content.
7. **Summary, Q4 and correction #4: Tsuru et al. found "equal numbers" / "equal" edge and screw
   segments.** The source says "present almost equally" and gives no counts (I confirmed this).
   Weakened in 3 places.
8. **Q1: "Outside the group, Xiao et al."** This was untagged; C19 does not establish that
   affiliation. Deleted "Outside the group,".
9. **Q1 comparison with Yin et al.: "They use 0 K Featherston and Neighbours constants for W, Mo
   and Ta (factcheck D5)".** D5 is about Kubilay et al.'s tabulated inputs, and Yin et al. do not
   tabulate their Cij (C13, "Not claimed"). Reworded to attribute the 0 K inputs to the Curtin
   group's tabulated set (Kubilay) and to say that Yin et al. do not tabulate theirs.
10. **Q1 temperature-law bullet: "At room temperature our alloys sit near τ/τ0 = 0.5".**
    Attributed to the report ("The report states that ..."). See A1.
11. **Q1 temperature-law bullet: "switching where the two v3 forms cross gives ...".** Attributed
    to the report ("which the report describes as switching where the two v3 forms cross"). See A2.
12. **Q1 temperature-law bullet: "the single 0.91-exponent form that later papers attribute to
    the published article [C15, C18]".** Same issue as #1. The tag was changed to
    [C15; factcheck D1].
13. **Q1 temperature-law bullet: "not ... found in any source".** Narrowed to "any checked source".
14. **Q2: "The code's source for these, Simmons and Wang according to the Curtin group's citation
    ...".** No stage established the code's source; the code says only "Standard handbook values".
    Reworded so that S&W is identified only as the Curtin group's citation [C13].
15. **Q2: "the V misfit, which is the largest term for V-containing alloys (factcheck P4)".** This
    overgeneralised. P4 says V is largest only for the equiatomic and near-equiatomic alloys and
    the finalists, and that Nb or Ta would overtake it in strongly V-rich alloys. Narrowed to "for
    the alloys studied here".
16. **Q3: "a compression test giving 1530 MPa at 12 % strain".** This was a misreading of C30. The
    12 is the ε (ductility) column, not the strain at which 1530 MPa was reached; Yao et al. confirm
    12 % is the plastic fracture strain. Reworded to "a compression test, 1530 MPa, and a strain of
    12 %".
17. **Q4 and "Checked and not a correction": "agrees fairly well ... overall [C32]".** "Overall"
    is not in the source, which says "with the measured high temperature behavior". Removed in 2
    places.
18. **Q4: "The 922 MPa (MoNbTaW) and 1317 MPa (MoNbTaV) predictions, the two V-free validation
    alloys".** This was a factual error, because MoNbTaV contains V. Narrowed to MoNbTaW, the only
    V-free validation alloy, with "no checked source".
19. **Needs Sean item 1: "the regime switch is at the alloys' room-temperature operating point".**
    Attributed to the report (see A1). The section header ("unchanged") was updated to say the
    audit weakened one phrase and to point to "Superseded by sean-sources.md" below.

## Overreach scan

I searched for "first", "novel", "proves", "confirms", "always", generalisation from one alloy or
one processing state, and model predictions treated as experiment.
- "Novel", "proves" and "always" do not occur.
- "First" occurs only as an ordinal ("the first item for university access").
- "Confirmed" is used only of sources and checks, for example "confirmed only through a secondary
  compilation".
- Generalisations were fixed: #15 (V misfit) and #18 (V-free).
- Prediction versus observation is handled correctly throughout: edge control of MoNbTaW and
  MoNbTaVW is labelled a prediction [C39], and the Tsuru edge and screw numbers are labelled model
  values.
- Tsuru's annealed, coarse-grained specimens are explicitly not transferred to the project's
  as-cast data (Q4).

## Sources re-opened by the auditor

| Source | Access | Confirms |
|---|---|---|
| Yao et al., accepted manuscript OSTI 1482331, local PDF supplied by the project owner (all 31 pages, read as page images) | read-directly (full text; accepted manuscript, published MSEA version not seen) | every item of `sean-sources.md` S1a-S1d (see below); C31 |
| Maresca & Curtin, arXiv:1901.02100 PDF (v3) | read-directly via WebFetch (preprint; published Acta version not opened) | C1-C6, C8, C9, C10, C32, C37, C44; no 0.91 anywhere; B printed without 1/3 |
| Kubilay et al. 2021, EPFL PDF | read-directly via WebFetch | C14, C15 (attribution to ref. 8 = Acta 182; my reading also puts 1/0.55 inside the bracket), C16, C35 |
| Yin et al. 2020, RUG publisher PDF | read-directly via WebFetch | C11, C12 (954/1058, 1347/1246, a, μ, ν, 300 K, 10⁻³ s⁻¹), C13, C42 |
| Featherston & Neighbours 1963, CORE PDF | read-directly via WebFetch (unit exponent garbled) | C20, C21, C22; 0 K rows (factcheck D5) |
| Gorsse et al. 2018, PDF | read-directly via WebFetch | C30 (NbTaVW row, ref. [76]), C34 (all eight HT values) |
| Tsuru et al. 2024, Springer page | read-directly via WebFetch (characters 0-100000 of 136022) | C40 (1242/1210 MPa, 25-30 %, ~2000 °C 48 h, 496 µm, 1 × 10⁻⁴ s⁻¹, Rao et al. edge model) |
| Lee et al. 2021, NSF PAR accepted manuscript | read-directly via WebFetch | C17 corrected wording (coefficients from full theory, no fitting), C39 |
| Baruffi et al. 2022, RUG PDF | read-directly via WebFetch | C18, C29, C43; "ad-hoc form" without reference |
| Bolef 1961, OSTI record 4110197 | abstract-only via WebFetch | C24 corrected wording (Nb c12 "13." truncated) |
| Gong & Dal Corso, arXiv:2406.16634v1 | read-directly via WebFetch | C25 |
| NBS Circular 539 Vol. I | read-directly via WebFetch (characters 0-100000) | C26 |
| AMCSD vanadium (rruff.info) | read-directly via WebFetch | C27 |
| COD 1539041 | read-directly via WebFetch | C28 (no temperature) |

Not re-opened by me (I relied on the fact-checker): Xiao et al. 2023 (C19), Pozuelo & Marian 2022
(C41), the opact.sdu.edu.tr Yao abstract record (C31; superseded by the full text), and Winkens
et al. 2023, arXiv:2502.11369 and Wang et al. 2026 (factcheck D1 only; not reviewer claims). One
side observation from my MC-v3 reading: Section 4 gives the plateau as 900-1300 K, while
Appendix C gives 800-1100 K. P1 quotes Section 4 correctly. This is a lead, not added to the notes.

## Verification of sean-sources.md against the PDF

The PDF title page reads "NbTaV-(Ti, W) Refractory High-entropy Alloys: Experiments and
Modeling", H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang. The pages
print no journal, volume or DOI. The link to MSEA 674 (2016) and doi:10.1016/j.msea.2016.07.102
therefore rests on the OSTI record (which I could not fetch) and the project owner's note. The
title and author list match that citation.

| Statement | Verdict | Where in the PDF |
|---|---|---|
| S1a: arc-melted from pure metals ≥ 99.9 wt.% | SUPPORTED | Section 2, p. 3 ("weight percentage purity ≥ 99.9%"; vacuum arc melting, Ti-gettered Ar) |
| S1a: remelted at least seven times | SUPPORTED | p. 4 |
| S1a: compression specimens EDM-cut from the cast ingots | SUPPORTED | p. 4 ("electric-discharged machined from the cast ingots") |
| S1a: no heat treatment is described | SUPPORTED | Nothing in any of the 31 pages describes an anneal or homogenisation. Fig. 3 caption: "as-solidified"; Fig. 5 caption and Conclusions: "as-cast" |
| S1a: cylinders 3 mm × 6 mm; MTS 809; room temperature; nominal 5 × 10⁻⁴ s⁻¹ | SUPPORTED | p. 4 |
| S1b: σ0.2 "the stress at ε = 0.2%", from true stress-strain curves at 298 K | SUPPORTED as a quotation of Section 3.4 (p. 7), with three caveats S1b omits: (i) the Fig. 6 caption (p. 17) says "Compressive **engineering** stress-strain curves", while the plot axes and text say true; (ii) the Fig. 6 panel says T = **296 K**, the text 298 K; (iii) the printed definition is stress at ε = 0.2 %, not a 0.2 % offset. In my reading of Fig. 6, the NbTaVW curve is still in its elastic rise at 0.2 % total strain and reaches about 1500 MPa only at roughly 1-1.5 %. The printed definition therefore cannot be literal, and 1530 MPa is probably an offset-type yield, but the paper does not say so |
| S1b: NbTaVW plastic fracture strain 12 % | SUPPORTED | p. 7 |
| S1c: Table 2 NbTaVW σ0.2 = 1530 MPa exp., 351 MPa est. by ROM | SUPPORTED | p. 30, "351/1530" (Est/Exp). The table note says the estimates use the EDX bulk compositions |
| S1c: Hv 4830 ± 29 MPa | SUPPORTED | p. 30, "1491/4830±29" (Est/Exp) |
| S1c: a = 3.2186 Å measured, 3.2172 Å estimated | SUPPORTED | p. 30 "3.2172/3.2186"; Section 3.2 p. 5 |
| S1d: Table 3 Caver Nb 28.50, Ta 29.65, V 20.67, W 21.18 at.% | SUPPORTED | p. 31. Table 3 calls it "estimated bulk composition"; EDX per the Table 2 note and EDS per Section 2 |
| S1d: W enriches dendrite arms (K = 2.22), V interdendritic (K = 0.52) | SUPPORTED | p. 31 (K = Cdr/Cidr); Section 3.3 p. 6-7 |
| "Project check": 1425 MPa at nominal composition | SUPPORTED by `reports/strength_model.md` l. 13 | — |
| "Project check": 1265 MPa at EDX composition, 298 K, 5 × 10⁻⁴ s⁻¹ | NOT VERIFIED. This is a session computation; I have no code execution in this audit. It is correctly labelled in `sean-sources.md` as not from the paper | — |

One further connection: the S1d composition is identical, to the digit, to the "Nb-Ta-V-W
28.5-29.65-20.67-21.18" row of MC-v3 Table 2 [C10]. Maresca and Curtin's experimental NbTaVW is
therefore Yao et al.'s EDX bulk composition.

## Superseded by sean-sources.md

These statements in `notes.md` were correct on the evidence the earlier stages had. They are now
out of date. Per the deletion-only rule, I have not added the new facts to `notes.md`. Apply the
corrections from here.

**Literature (from the PDF, verified above):**
1. **Summary**: "The NbTaVW value of 1530 MPa is still confirmed only through a secondary
   compilation, which gives neither the processing state nor the strain rate [C30]." Now
   superseded: the primary (Yao et al. Table 2) gives σ0.2 = 1530 MPa. The material was tested
   as-cast (EDM from arc-melted ingots, no heat treatment described) at room temperature (298 K in
   the text, 296 K on Fig. 6) and a nominal 5 × 10⁻⁴ s⁻¹.
2. **Q3, Gorsse bullet**: "whether it is the yield strength or the maximum stress is an inference
   [C30; factcheck D9]". Resolved: the primary lists 1530 as σ0.2 ("yielding strength"). D9 is
   closed. Whether σ0.2 is an offset yield remains open (see caveat iii above).
3. **Q3, "Still missing" list**:
   - value as printed: 1530 MPa, Table 2;
   - 0.2 % offset: the paper defines σ0.2 as "the stress at ε = 0.2%" on true curves, and offset
     is not stated (partly open);
   - specimen condition: as-cast;
   - strain rate: 5 × 10⁻⁴ s⁻¹;
   - specimen size: 3 mm × 6 mm;
   - measured composition: Nb 28.50, Ta 29.65, V 20.67, W 21.18 at.%.
4. **Q3 comparison**: "recorded as cast and marked as not verified ... It does not confirm the
   as-cast state or that the value is a yield strength [C30]". The as-cast state and σ0.2 are now
   confirmed by the primary.
5. **Q3 comparison**: "The NbTaVW strain rate is unknown [C30, C31]". It is 5 × 10⁻⁴ s⁻¹, so the
   report's 10⁻³ s⁻¹ (strength_model.md l. 3) does not apply to NbTaVW.
6. **Q3 literature, C10 bullet**: the non-equiatomic MC-v3 NbTaVW composition is Yao et al.'s
   Table 3 bulk composition.
7. **Q3 next steps**: "Try [the OSTI manuscript] before asking for library access" is done. "Once
   the paper is read, record the measured composition, condition and strain rate in `MEASURED`"
   can now be done for NbTaVW.
8. **Corrections #10** (the whole corrected-wording cell, including "The primary (Yao et al. 2016)
   has not been read"). Superseded; replacement under "Corrections the project should apply"
   below.
9. **Open leads**: the Yao et al. OSTI lead ("whether it holds the full text is not confirmed")
   is resolved: it does.
10. **Open questions**: "What strain rate applies to each of the four measurements, and is 1530 MPa
    a yield strength or a maximum stress" is answered for NbTaVW (5 × 10⁻⁴ s⁻¹; σ0.2). It is still
    open for the other three in this run's notes.
11. **References**: Yao et al. "(abstract only) [C31]" should become "accepted manuscript OSTI
    1482331, full text".
12. **Needs Sean item 2 (Yao, IMPERATIVE)** is resolved and no longer needed. Remaining OPTIONAL
    point: whether the published MSEA version differs from the accepted manuscript in Table 2 or
    Section 2.

**Session computations (not literature claims; not verified by this audit):**
13. **Q3 comparison / Open questions**: "How much our predictions would change at those
    compositions has not been computed." For NbTaVW, the owner's session reports 1265 MPa at the
    EDX composition, 298 K and 5 × 10⁻⁴ s⁻¹ (`sean-sources.md`), against 1425 MPa at nominal. This
    is a session computation, not a literature claim, and I did not reproduce it. Put it in a
    project file (e.g. the report) before citing it.
14. **Needs Sean item 1 (Maresca-Curtin Acta 182)**: mark it as **no longer imperative for
    conclusions**. The project owner's session computed that the single-exponential (0.91) law
    changes the four validation predictions by only +7 to +37 MPa, with unchanged ranking. This is
    a session computation, not a literature claim, and I could not rerun the code.
    - **Plausibility check (auditor arithmetic, not code execution).** The report's continuous and
      paper-rule values differ by a factor of 1.060-1.061 for all four alloys. That puts
      s = (kT/ΔEb) ln(ε̇0/ε̇) ≈ 0.15 and τ/τ0 ≈ 0.72 on the 2/3-power branch. At s = 0.15, the 0.91
      form gives +0.8 % (1/0.55 outside the bracket) to +2.6 % (inside), or about +7 to +36 MPa on
      922-1425 MPa. That is consistent with the session figure, and the near-uniform factor
      preserves ranking. The session note does not say which bracket placement it used; my
      arithmetic suggests the stated range spans both.
    - The item stays useful (OPTIONAL) for labelling the equations correctly (correction #3) and
      for the finalist high-temperature values.
    - Statements in `notes.md` that this supersedes:
      - Summary: "so this stays the first item for university access";
      - the Q1 bold sentence "How the four validation predictions would change under the single
        form has not been computed by the project ...";
      - Q1 next step "Do not change the switch rule until the published equations are read";
      - the corresponding bold sentence inside correction #3's wording;
      - Open questions, first bullet ("D1, the most important"; the validation part is answered by
        the session, the finalist part is not).

## Project-file issues found by the audit (auditor arithmetic; confirm by running the code)

- **A1. "At room temperature these alloys sit near τ/τ₀ = 0.5"** (`reports/strength_model.md`
  l. 20; generator l. 182-184; related wording in the `yield_strength` docstring l. 112-113 and
  test l. 31). The report's own numbers say otherwise. For R5-4 (ΔEb = 2.49 eV), s at 25 °C is
  0.166, which gives τ/τ0 = 0.698 on the 2/3-power branch. Taking the 1000 °C and 1300 °C values on
  the exponential branch then reproduces the report's 428 and 315 MPa from its 1087 MPa (my
  arithmetic gives 428.5 and 316). R5-1 likewise reproduces 573 MPa. For the validation alloys,
  the uniform 6.0-6.1 % continuous/paper ratio implies τ/τ0 ≈ 0.72, not 0.5. The switch at 0.5 is
  then reached only at about 700 K. Consequence: the room-temperature validation values do not sit
  at the regime switch; they depend on which law is used, not on where the switch is.
- **A2. `switch="continuous"` is not "switching where the forms cross"** (`yield_strength`
  docstring l. 114; report l. 20; generator l. 184). For 0 < s ≤ 1, exp(-s/0.55) exceeds
  1 - s^(2/3) everywhere. I checked s = 0.01, 0.15, 0.35, 0.5, 0.8 and 1.0, and as s → 0 the s^(2/3)
  term dominates. So max(low, high) is the exponential form (Eq. 12) at every temperature, and the
  forms never cross. The "~0.53 crossing" in the docstring is incorrect. Relabel the variant as
  "v3 Eq. 12 throughout".

## Corrections the project should apply

From `notes.md` (as fixed by this audit): #1-#9 as written, with #4 now reading "edge and screw
segments present almost equally". The bold "not computed" sentence in #3 is superseded (item 14
above). Replace it once the session numbers are recorded in a project file.

Replacing #10 (from the verified PDF):
- `reports/strength_model.md` Caveats l. 38 and generator l. 212-213: replace "NbTaVW's 1530 MPa is
  not yet verified against its primary source" with: "NbTaVW 1530 MPa is σ0.2 from Yao et al.,
  MSEA 674 (2016), Table 2 (accepted manuscript, OSTI 1482331): as-cast (EDM-cut from arc-melted
  ingots, no heat treatment described), room temperature, nominal 5 × 10⁻⁴ s⁻¹, 3 × 6 mm
  cylinders. The paper defines σ0.2 as 'the stress at ε = 0.2%' and does not state an offset. The
  measured composition (Nb 28.50, Ta 29.65, V 20.67, W 21.18 at.%) is not equiatomic."
- The same caveat bullet's "all equiatomic": the validation *compositions used* are equiatomic,
  but the NbTaVW specimen (and MoNbTaV per MC-v3 Table 2 [C10]) was not. Same fix needed in README
  l. 132 ("four equiatomic, as-cast alloys") and `reports/finalists.md` l. 66 ("all equiatomic").
- `reports/strength_model.md` l. 3 / generator l. 166-167: "strain rate 10⁻³ s⁻¹" is the model
  setting. Note that the NbTaVW test was at 5 × 10⁻⁴ s⁻¹.
- Other places that say the NbTaVW value is unverified:
  - `pipeline/strength_model.py` `MEASURED` note l. 58 ("cast; not verified against primary
    source");
  - the parity-figure footnote l. 259-260;
  - `README.md` l. 99-100;
  - `reports/finalists.md` l. 47 and l. 66 ("its paper has not been read ... rests on that
    unverified value").

  Update all of them. `docs/research/run-2026-11-11/` is a closed run; do not edit it.
- If the session's 1265 MPa (EDX composition, 298 K, 5 × 10⁻⁴ s⁻¹) is adopted, report it next to
  1425 MPa, labelled as a project computation.

New from the audit: A1 and A2 above (confirm by running the code before rewording).

## Could not verify

- The published Acta Mater. 182 version of Maresca & Curtin (temperature law, bracket placement).
  No stage opened it. It is now OPTIONAL for conclusions on the basis of the session computation.
- The session computations (+7 to +37 MPa; 1265 MPa). The auditor has no code execution. My
  arithmetic is consistent with the first; I did not attempt the second.
- Whether the OSTI 1482331 PDF matches the published MSEA version. The PDF carries no journal or
  DOI. The OSTI record could not be fetched by any agent (`robots_disallowed`).
- Whether Yao et al.'s σ0.2 is a 0.2 % offset yield (see caveat iii).
- Bolef's exact Nb C12 and the temperature of the COD Nb lattice parameter. Both are already
  flagged in the notes.

## Memory and instructions

Nothing in the run files, the PDF or memory asked me to do anything outside this task.

## Result

All 19 defects found were fixed by deletion or weakening. No unsupported statement remains in
`notes.md`. Statements made out of date by `sean-sources.md` and the session computation are
listed above under "Superseded by sean-sources.md". They were supported by the evidence the
earlier stages had, and they must be updated from this list before the notes are cited for
NbTaVW. The items I could not verify are stated as unverified, not asserted.

SIGN-OFF: PASS
