# Integrity audit: run 2026-11-11

Integrity auditor (stage 4, final gate), 2026-11-11. I did not write any earlier stage.

**This is an in-project AI audit, not peer review.** The reviewer, fact-checker, note-writer and
this auditor are all AI agents. Agents that check other agents can share the same blind spots,
for example the same model-mediated reading of a PDF (WebFetch returns a model's extraction, not
the raw text). An agreement between stages is therefore weaker evidence than an independent
human reading of the primary source.

## Scope and method

Inputs read in full: `brief.md`, `claims.md`, `factcheck.md`, `notes.md`; project files
`reports/finalists.md`, `reports/cost_supply.md`, `reports/sensitivity.md`,
`reports/study_results.md`, `pipeline/finalists.py`, `pipeline/cost_supply.py`, and
`data/calphad/study_results.csv`. I read the CSV to test correction 8's premise that every alloy
contains W, Ta, Nb and V.

I checked every sentence of `notes.md`: the Summary, Q1-Q5 (literature, comparison and next-step
bullets), the Q5 table, all 12 rows of "Corrections to the project", "Checked and not a
correction", Open leads, Open questions and References. That is about 170 prose sentences, 4 table
rows, 12 correction rows and 27 reference entries.
- Literature sentences: each tag traced to `claims.md` and its `factcheck.md` verdict. All 46 tags
  resolve, all are SUPPORTED or PARTIAL, and the five PARTIAL claims (C2, C3, C14, C18, C46) appear
  only in the fact-checker's corrected wording.
- Project sentences: every number traced to the cited project file. The Thermo-Calc values
  (1691/1482/787/1734 MPa), measured values (1246/1058/1530/1525 MPa), errors (+445/+424/-743/+209),
  ρ = -0.20, the 163 MPa finalist span, the Scheil ranges (600-844, 623-732, 785-844, 600 °C), the
  sensitivity slopes (-18 °C [-19, -17]; +9 °C [+6, +12]), V 5.7-12.1 at.%, 11.42-14.93 g/cm³,
  2371-2822 °C, 572-795 MPa, 0.3 % density error, $40/kg Nb, SR 1.31-2.50, 12 non-dominated / 8
  non-finalists, $278.22 → $351/kg W, and $380/mtu and $51/kg all match exactly.
- Correction-table line numbers: all checked against the files as they stand. Every cited line
  (finalists.md l. 13, 18, 41, 47, 48, 64; finalists.py l. 30, 44, 45, 119-120, 187-188;
  cost_supply.md l. 15, 17, 19, 35, 65; cost_supply.py l. 14, 57, 61-62, 74, 145-147, 181-183,
  215-219) contains the quoted current wording.

## Defects found and fixed in notes.md (28 defects, 25 edits; defects 4/5, 17/18 and 22/23 each share one edit)

All fixes delete or weaken text. Where a sentence was reworded, the new wording uses only content
already in the cited claim or project file.

1. Summary: "whose published validation covers only the Mo-Ta binary". C7 covers only the help
   pages read and explicitly does not claim that no other validation exists. Weakened to "whose
   validation, in the help pages read, covers only the Mo-Ta binary".
2. Summary: "Two of the project's validation inputs need fixing". NbTaVW needs a verification
   flag, not a fix. Weakened to "need attention".
3. Summary: "In W-Mo-Ta-Nb-V castings ... V and Nb to interdendritic regions [C10, C11, C12]". This
   generalised from three alloys, and C12 says Nb stays near bulk in MoNbTaV, which contradicts
   the cited statement. Narrowed to "In as-cast W-Nb-Mo-Ta-V ... [C11]".
4. Summary: "the USGS prices and shares in cost_supply.md check out [P1, P2]". This was wider than
   the support: P1 and P2 cover only Nb and V, and the W, Mo and Ta shares and the W and Mo prices
   were not checked. Narrowed to "the Nb and V USGS prices and producer shares".
5. Summary: "the ferroniobium conversion is already handled correctly". This was untagged and
   overstated, because the 0.65 grade is unverified. Weakened to "already treats the price as
   gross weight [P2]".
6. Summary: "Published comparisons place W-Mo-Ta-Nb-V alloys above Inconel 718". C37 is one paper
   on two equiatomic alloys. Narrowed to "One published comparison places equiatomic Nb-Mo-Ta-W and
   V-Nb-Mo-Ta-W ...".
7. Q1 comparison: "validated only on Mo-Ta [C6, C7]". Same overreach as #1; weakened to
   "validation shown only for Mo-Ta in the pages read".
8. Q1 comparison: "The other three measured values check out, and all four are as-cast [P4]". The
   NbTaVW primary source was never read, so its as-cast status rests on the dataset label
   (finalists.md "NbTaVW (cast)"), not on verification. Weakened to say this.
9. Q1 comparison: "because all four validation measurements are as-cast [P4]". Same issue as #8;
   weakened to "the three verified validation measurements are as-cast and NbTaVW is recorded as
   cast".
10. Q1 comparison: "The literature gives no reason to expect ..." Narrowed to "The sources
    checked give no reason ...".
11. Q1 next step: "is *the* published model with a stated agreement". C4 also reports agreement
    for a Labusch-type model on MoNbTaV. Weakened to "a published model".
12. Q2 comparison: "Mobility databases may overpredict how fast segregation in W- and Ta-containing
    alloys decays [C18]". This generalised from one database and two analogue alloys. Narrowed to
    the C18 finding.
13. Q2 next step: "results should be treated as a lower bound on time". This inference went beyond
    C18. Weakened to "may underestimate the time needed".
14. Q3 literature: the W-Ta-Cr-V ODTT result [C26] read as if it were an observation. It is a
    modelling result, and the sentence now says "first-principles-based modelling associates ...".
15. Q3 comparison: "V ... raises high-temperature strength [C22]". This generalised from one
    equiatomic pair. Narrowed to "the V-containing alloy of the equiatomic pair kept higher
    high-temperature strength".
16. Q3 comparison: "This agrees with the exact theory-measurement match for W-Nb-Mo-Ta-V [C21]".
    This was cherry-picked: the other alloy in C21 differs (13.64 vs 13.75 g/cm³), and the basis of
    Senkov's "calculated" density is not established. Deleted.
17. Q3 comparison: "Low V is therefore not expected to cost room-temperature compressive
    ductility ... because neither of the equiatomic pair showed any [C23]". This contradicted the
    source, since C23 reports 2.1 % and 1.7 % plastic strain, and it generalised from one pair.
    Deleted.
18. Q3 comparison: "[C24] has not been tested in W-containing alloys". This was an absolute claim
    of absence. Weakened to "is not tested in W-containing alloys by any checked source".
19. Q3 next step: "the only test available for the slopes". Weakened to "the check the project
    has planned for the slopes".
20. **Q4 comparison, the garbled sentence**: "and Mo meets neither condition's SR part [P3]".
    Against P3, Mo has SR 0.8 (< 1.0, so it fails) and EI 6.7 (≥ 2.8, so it passes). It fails the
    SR condition only. I replaced the clause with P3's corrected wording: "Mo (SR 0.8) does not
    qualify [P3]". The element-by-element conclusion still holds, because I confirmed from
    `data/calphad/study_results.csv` that all 50 alloys contain W (≥ 3.8), Ta (≥ 5.1), Nb (≥ 5.4)
    and V (≥ 5.1 at.%).
21. Q4 comparison: "metal-versus-raw-material data ... are the tantalum trade quotes [C34, C35]".
    C35's form is not stated, so it is not a metal quote. Narrowed to C34, with C35 noted as of
    unstated form.
22. Q4 comparison: "the closest published study". This was an untagged judgement; replaced with
    "Mulukutla et al.".
23. Q4 comparison: "the literature neither supports nor rejects it". Narrowed to "the checked
    literature".
24. Q5 comparison: "Measured literature points exist only at other temperatures". This is false
    as worded, because C38 has Inconel 718 at 982 °C and the C39 finding notes 130 MPa at 1000 °C.
    Weakened to "The measured literature points listed here are at other temperatures".
25. Q5 comparison: "both point the same way: ... the W-rich finalists will compare less well
    [C41]". This was stronger than C41, which is about the review's alloys, not ours. Weakened to
    "may compare less well, as the review notes for high-density RHEAs".
26. Correction 5 (corrected wording): "All four measured strengths are from as-cast specimens".
    Same issue as #8; weakened to say three are confirmed as-cast and NbTaVW is recorded as cast
    (primary source not checked).
27. Correction 12 (corrected wording): "The W and Mo figures have not been independently
    re-checked". As a statement about this run's evidence it is true: claims.md says the USGS
    Tungsten and Molybdenum chapters were not opened, and no P-statement covers them. But the
    replacement silently dropped Ta and the project's own provenance statement. Reworded, using
    only the existing cost_supply.md text and C33, to: "The W, Mo and Ta figures were read from the
    USGS chapters by the project; of these, only the Ta price was re-checked in run-2026-11-11."
    Support column now C30-C33.

28. Open leads: "Only a secondary encyclopedia.pub entry gives the value". This was an absolute
    claim of absence. Weakened to "The only source found for the value is a secondary
    encyclopedia.pub entry".

## The "Corrections to the project" section

All 12 rows are supported after the fixes above:
- **#1-3 MoNbTaV relabel (annealed → as-cast).** Supported by C13, P4 and factcheck D5. I
  re-opened Yao et al. (Entropy 18, 189) myself. It describes vacuum arc melting with at least
  seven remelts and no anneal or homogenisation, calls the tested material as-cast, and says
  homogenisation is "beyond the scope of the present study". Table 1 gives σ0.2 = 333/1525 MPa
  (calc/exp). Line numbers match.
- **#4 NbTaVW 1530 MPa verification flag.** Supported by P4. The fact-checker had only the MSEA
  674 abstract (no NbTaVW value) and a secondary encyclopedia.pub entry. I did not obtain the full
  text either, so the flag is correct and must stay.
- **#5 caveat rewording.** Supported by P4, P5 and C14 after fix #26.
- **#6 1400 °C rationale.** Supported by P5, C14 and C15. I re-opened the AFRL-RX-WP-TP-2011-4289
  preprint (DTIC ADA550865). The 1400 °C / 19 h anneal (18 h in Section 3.2.1 and Fig. 4) applied
  to the neutron-diffraction material. Compression specimens were "electric-discharged machined
  from the cast buttons". Section 3.2.4 says "Even dynamic recrystallization was not able to
  remove the compositional inhomogeneity". So "homogenised" is not Senkov's wording, and 1400 °C
  does not correspond to the tested condition. One caveat stays open: the row targets "the repo
  text giving the reason for the 1400 °C setting", which was not among the files read. The notes
  already say so. The project must locate that text before applying the correction.
- **#7-9 EU threshold.** Supported by P3. I re-read the same third-party mirror (cde.ual.es) as
  the fact-checker. Both thresholds (SR ≥ 1.0 and EI ≥ 2.8) must be met, and SR/EI are W
  1.2/8.7, Mo 0.8/6.7, Ta 1.3/4.8, Nb 4.4/6.5, V 2.3/3.9. All match. I could not open the
  official EC copy either. #8's premise ("every alloy here contains W, Ta, Nb and V") is confirmed
  from the CSV.
- **#10 tungsten basis.** Supported by P6. I re-opened the CMJ article (4 Nov 2026). It says
  Rotterdam APT "traded at $278.22 per kg in October" and does not state a WO3 basis.
- **#11 V "(est.)".** Supported by P1 and C30. I re-opened the USGS Vanadium chapter, which labels
  the 2025 column "2025e".
- **#12 Limits wording.** Supported after fix #27. Within this pipeline the W and Mo USGS figures
  ($380/mtu, $51/kg, and the W and Mo producer shares) remain unchecked, and the Ta producer
  share (Congo 52 %) is also unchecked.

## Sources re-opened by the auditor (all via WebFetch, model-mediated reading)

| Source | Access | Confirms |
|---|---|---|
| Yao et al., Entropy 18, 189 (mdpi.com), both halves | read-directly | C4, C5, C12, C13, P4 (MoNbTaV 1525 MPa, as-cast, no anneal) |
| Senkov et al., AFRL-RX-WP-TP-2011-4289 (DTIC ADA550865) | read-directly (preprint; published Intermetallics text not opened) | C14, C15, C22, C23, C37, C38, P4 (1058, 1246 MPa, as-cast), P5 |
| Senkov et al., AFRL-RX-WP-TP-2011-4295 (DTIC ADA550824) | read-directly | C9, C10, C11, C21 (all numbers match) |
| Maresca & Curtin, arXiv:1901.02100 | read-directly | C1, C3; C2 pairing as the fact-checker read it (158 MPa dendritic vs interdendritic; 78 MPa dendritic vs average) |
| Thermo-Calc TCHEA yield-strength validation page (2025b) | read-directly | C7 (Mo-Ta only; no W-Mo-Ta-Nb-V) |
| USGS MCS 2026 Vanadium | read-directly | C30, C31, P1 |
| USGS MCS 2026 Niobium | read-directly | C32, P2 (gross-weight footnote 5; 104 of 112 kt; ~93 %) |
| USGS MCS 2026 Tantalum | read-directly | C33 |
| EU CRM 2023 final report, cde.ual.es mirror | read-directly (third-party mirror; official EC copy not opened) | P3 |
| Canadian Mining Journal, 4 Nov 2026 (canadianminingjournal.com/?p=1003791730) | read-directly (MetalMiner white paper not opened) | P6 |
| Atli & Karaman 2023 (Frontiers) | read-directly (first 100000 of 105163 characters) | C39, C40, C41 |
| Materion C-103 data sheet | read-directly | C42 |
| ATI Ta-10W data sheet | read-directly | C43 |
| Wieland TZM data sheet | read-directly | C44 |

Not re-opened by me (relied on the fact-checker): C6 "About" page, PM_G_06 page, C8 abstract,
C16-C20, C24-C29, C34-C36, C45, C46.

## Could not verify

- NbTaVW 1530 MPa and its processing state (Yao et al., MSEA 674, full text not found by any
  stage). Flagged in the notes and in correction #4. This is an open gap, not an unsupported
  statement.
- The official EC copy of the EU CRM 2023 study. Only the mirror was read.
- The published Intermetallics 19 (2011) text. Only the AFRL preprint was read, and it says it was
  submitted to J. Alloys Compd.
- The repo location of the 1400 °C rationale (correction #6).

## Leads for the next run (not added to notes.md, because the auditor does not add facts)

- My reading of Yao et al. (Entropy 2016) suggests the "333 MPa" in Table 1 is the
  rule-of-mixtures σ0.2, and the Labusch-type solid-solution term (~1.21 GPa) is added to it to
  give ~1.5 GPa. If confirmed against the PDF, this resolves the first Open question.
- My reading of the USGS Niobium chapter shows footnote 1 assuming "65% niobium content in
  ferroniobium" for trade estimates. That is an assumption, not a measured grade, but it is a
  citable basis for the project's `NB_IN_FENB = 0.65`. A fact-checker should confirm it.
- My reading of Senkov 4289 gives the V20Nb20Mo20Ta20W20 failure strain as "about 1 %" in the
  Conclusions (1.7 % in the text). This is a further internal inconsistency like the 2.1/2.6 %
  one.

## Overreach scan

I searched for "first", "novel", "proves", "confirms", "always", generalisation from one alloy
or one processing state, and CALPHAD/ML treated as experiment. None of "first", "novel",
"proves" or "always" occurs. "confirm" appears only as a to-do ("confirm the 1530 MPa value").
The generalisations from one alloy or one pair were fixed (#3, #6, #12, #15, #17). The modelling
result read as observation was fixed (#14). Project values are marked as calculated or surrogate
values throughout (Q3 "From the surrogate"; Q5 "calculated solidus" vs "melting points";
"estimate and measurement").

## Result

All 28 defects found were fixed by deletion or weakening. No unsupported statement remains in
`notes.md`. The items I could not verify are stated as unverified in the notes, not asserted.

SIGN-OFF: PASS
