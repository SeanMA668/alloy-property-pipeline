# Integrity audit: run 2026-11-09 (integrity-auditor)

Written by the integrity-auditor agent, 2026-11-09. I did not write brief.md, claims.md,
factcheck.md or notes.md. **This is an in-project AI audit, not peer review.** The
reviewer, fact-checker, note-writer and auditor are all AI agents; agents checking agents
can share blind spots (for example, all stages read sources through WebFetch, which returns
a model-extracted reading, not raw text).

## Scope

- Sentences checked: 77 sentence units in notes.md (Summary through Open questions,
  including bullets), plus the 23 reference entries.
- Literature sentences traced to claim tags and their verdicts in factcheck.md. All tags
  used in the body are SUPPORTED, or PARTIAL in the corrected wording (C28, C29, C41,
  P1-P3). LEAD-ONLY claims (C11, C21, C22, C26, C31-C33) appear only under "Open leads
  (not verified)"; P5 (UNREACHABLE) is marked unverified.
- Project sentences traced to results.md, calphad_results.md, calphad_vs_ml.md,
  properties_results.md, active_learning.md; density and strength rows also traced to
  data/MPEA_dataset.csv and hea_properties.py.

Project numbers confirmed exactly: VEC importance 0.385 (results.md); split below about
664 °C, 28 % at 500 °C, liquidus 2665 °C, Scheil freezing ranges 844 / 803 °C, no B2 or
intermetallic (calphad_results.md); ρ = -0.43, p = 0.12, VEC ρ = +0.01 (calphad_vs_ml.md);
leave-one-out ρ = 0.82 on 14 TCHEA results (active_learning.md); densities 12.90 / 12.58 /
12.36 and held-out strengths, predicted 1379 MPa at 25 °C (properties_results.md).
2976 K = 2702.85 °C, so "about 2703 °C" is correct.

## Density conflict, MoNbTaW (resolved in notes)

| Value (g/cm³) | What it is | Source |
|---|---|---|
| 13.75 ± 0.028 | measured (He pycnometry), as cast, near-equiatomic W27.3 Nb22.7 Mo25.6 Ta24.4 | Senkov et al. 2010, DTIC ADA550824 (re-opened, read-directly) |
| 13.64 | rule of mixtures, ours (`hea_properties.py`, `rho_mix`); Senkov 2010 also calculates 13.64 | properties_results.md; ADA550824 |
| 13.64 | listed as "experimental" by Shaikh et al. Table 2 (with ROM 13.75), citing Senkov 2010: apparently swapped | Shaikh et al. PDF (re-opened, read-directly) |
| 13.60 | measured value recorded in our training data (MPEA row citing DOI 10.1016/j.actamat.2019.06.032) | properties_results.md "13.64 vs 13.60"; data/MPEA_dataset.csv. Original paper not opened. |

The code prints `rho_mix` first, then `Exp. Density`, so in properties_results.md 13.64 is
computed and 13.60 is measured. For WMoTaNbV: our ROM 12.36, training-data measured 12.29,
Senkov 2010 measured 12.36 (near-equiatomic, ROM 12.36).

## Defects found and fixed in notes.md

All fixes delete or weaken; the only additions are attributions to project files already
cited or to existing claim tags.

1. Summary: "WMoTaNb and WMoTaNbV are single-phase BCC ... [C1]" generalised one study and
   one processing state. Weakened to "In one study ... after an 18-19 h anneal at 1400 °C".
2. Summary: "no checked source held them for long times at 500-700 °C" was contradicted by
   C3 (MoNbTaW aged 5 weeks at 500 °C). Restricted to WMoTaNbV, with C3 stated.
3. Summary: "Simulations predict chemical ordering there [C5, C6]" placed ordering at
   500-700 °C; the predicted temperatures (559-1654 K) do not match. "there" deleted;
   tag widened to C4-C6.
4. Summary: "No checked source tests CALPHAD against experiment for these alloys" was too
   broad (C17 compares TCHEA and measured densities). Narrowed to phase-stability
   predictions.
5. Summary: "scatter reflects two processing routes" (causal) weakened to "come from two
   different processing routes".
6. Terms: untagged definitions of B2, B32 and CALPHAD (from general knowledge, no source)
   deleted. A2 and Scheil kept, traced to calphad_results.md.
7. Q1: C4 was described as an "A2 to B2 transition near 700 K"; C4 says a chemical
   ordering transition with B2-type Mo-Ta ordering. Reworded to the claim.
8. Q1: "the authors think only short-range order may be observable" overstated C7.
   Replaced with C7's wording.
9. Q2: Scheil coring predicted for #1 and #3 was called "consistent with the observed
   dendrites" [C19], which were in the equiatomic alloys. Now states it does not test the
   prediction.
10. Q3: "predicted densities" did not say they are rule-of-mixtures values, and the control's
    12.36 could be read as measured. Labelled as rule of mixtures, not measurements;
    "favours Mo-lean alloys" deleted.
11. Q4: "while in-system ordering depends on particular atom pairs [C30]" implied C30
    explains our VEC result (C30 "Not claimed": that it explains the project's finding;
    TCHEA's split is A2+A2, not ordering). Deleted. The ρ = 0.82 sentence now says
    leave-one-out and that it is agreement with CALPHAD, not experiment.
12. Q5: C41 sentence "reasons measured strength exceeds the intrinsic value" weakened to the
    corrected wording "factors that can raise measured strength above the intrinsic
    prediction".
13. Q5: "The measured values in our held-out check match the arc-melted series" was false
    for WMoTaNb at room temperature (996 MPa at 23 °C; 996, 1058, 1217 at 25 °C). Restricted
    to the rows that match.
14. Corrections: the "Also" bullet called 13.64 g/cm³ the "measured" value in
    properties_results.md; there it is our rule-of-mixtures value. Rewritten as in the
    table above.
15. Corrections P1: "Measured density of the quaternary was 13.75" now says as-cast,
    near-equiatomic.

No "first", "novel", "proves" or "confirms" remains. No sentence treats a CALPHAD or ML
output as an experimental result after fixes 9-11.

## Sources re-opened by the auditor (WebFetch, 2026-11-09)

| Source | Access | Confirmed |
|---|---|---|
| Senkov et al. 2011 preprint, DTIC ADA550865 | read-directly | 1400 °C anneal 19 h (Sec. 2) vs 18 h (3.2.1/Fig. 4); single BCC by neutron diffraction as cast and annealed; a = 3.220, 3.185/3.187 Å; Tables 2-3 yield strengths all match C34-C35; dendrite arms 20-30 µm; vacuum arc melting. Note: Conclusions give 470 MPa at 1600 °C vs 477 in Table 3 (notes use the table value). |
| Senkov et al. 2010 preprint, DTIC ADA550824 | read-directly | Compositions W27.3 Nb22.7 Mo25.6 Ta24.4 and W21.1 Nb20.6 Mo21.7 Ta15.6 V21.0; densities 13.75 and 12.36 measured, 13.64 and 12.36 calculated; as cast, single BCC. |
| Shaikh et al. 2020 PDF (home.iitm.ac.in) | read-directly | TCHEA v2.1; liquidus 3138 / 2976 K vs ROM 3158 / 2963 K; no experimental liquidus; Table 2 MoNbTaW exp. 13.64, ROM 13.75, CALPHAD 13.8 (swap). |
| Kang et al. 2018 (KAIST record) | abstract-only | 6 h MA, SPS 1500-1700 °C, 2612 MPa, 8.8 %, BCC with oxide inclusions, four strengthening mechanisms. |
| Bajpai et al., arXiv:2103.07951 | read-directly | 1800 °C 4 days; 500 °C (773 K) 5 weeks; synchrotron XRD, no superlattice peaks; ~700 K EAM MC/MD; Mo-Ta B2-type. |
| Huhn & Widom, arXiv:1306.5043 (figshare) | read-directly | Tc 1280 K (MC), 1654 K (mean field); Mo-Ta driven. |
| Woodgate & Staunton, arXiv:2211.09911v2 | read-directly | 742 K B32-like (V), 559 K B2-like; overestimates; multiphase state unlikely observable; SRO may be observable; pair preferences. |
| Maresca & Curtin, arXiv:1901.02100 | read-directly | no adjustable parameters; RT agreement; underprediction and plateau at high T; 158 MPa; ~50 MPa Hall-Petch for 80-200 µm; O, N. |
| Gorsse & Senkov, PMC7512484 | read-directly | 294 binaries, 136 ternaries, about 5 %; extrapolation conditions; test systems at 800 °C. |
| Wang, Zhong, Zhao (par.nsf.gov) | abstract-only | 2436 alloys; VEC < 6.87 / > 9.16; BCC/B2 one class; ANN CV 89.1 %; 81.8 % on 66 alloys. |
| Xia & Franz (pure.unileoben.ac.at) | abstract-only | cathodic arc films, vacuum anneals to 1600 °C, BCC stable to 1500 °C. |
| Dai et al. 2022 (jmst.org) | abstract-only | 100 h anneals, decomposition from ~500 °C, re-entry 900 / 1000 / 1100 / >1300 °C. |
| Guo et al. 2011 (core.ac.uk) | read-directly | bcc at VEC < 6.87; derived from Al-containing 3d-metal series. |
| Iyengar et al., arXiv:2503.21146 | read-directly | Couzinié data, Al-containing; 2 BCC+BCC, 13 BCC+B2; test alloys 7, 8, 10 misclassified; single-BCC correct. |
| Tuhser et al. (uknowledge.uky.edu) | abstract-only | single BCC, comparable hardness, Mo-to-Nb most effective. |
| Zheng & Wang, PMC7512564 | read-directly | 70 compositions; Mo+W raise moduli; V raises B/G, ν; Nb, Ta small; all stable. |
| Puerling et al., OSTI 1989196 | read-directly | NbTaTiW, MoNbTaTi; TCHEA4/MOBHEA2; Scheil accurate; 1673 K, 35 h. |

## Not re-opened / not verified

- Yao et al. 2016 (C25, 1420 MPa, 20 %): catalogue URL not recorded in full by earlier
  stages; not re-opened. Relies on the fact-checker's abstract-only check.
- Huhn & Widom JOM journal version, Woodgate & Staunton PRM journal page, Senkov 2011
  Intermetallics published version: not opened (preprints only).
- Pavlů et al. (P3), Borg et al. (P7), matminer table (P4): not re-opened.
- MDPI-hosted sources (Vlasák C11, Zhuo C32, Xia & Franz full text) and blocked PMC/ar5iv
  pages: not re-opened.
- The paper behind the training-data density 13.60 / 12.29 g/cm³ (DOI
  10.1016/j.actamat.2019.06.032): not opened.

## Notes for the main session (not changed in notes.md)

- Open question "Sources of the 996 and 1217 MPa WMoTaNb values" can be partly answered from
  data/MPEA_dataset.csv: 996 MPa rows cite DOIs 10.1016/j.msea.2017.12.004 (cast) and
  10.1016/j.actamat.2019.06.032; 1217 MPa cites 10.1007/s10853-019-03567-9 (powder). None
  opened.
- The raw TCHEA exports name phase columns BCC_B2 / BCC_B2#2 while calphad_results.md says
  every phase is labelled [A2]; the notes copy calphad_results.md. Worth confirming that the
  column names are only the database's model name.

SIGN-OFF: PASS
