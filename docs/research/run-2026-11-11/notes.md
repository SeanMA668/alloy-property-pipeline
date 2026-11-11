# Literature notes: run 2026-11-11

Literature notes produced by AI agents (reviewer, fact-checker, note-writer, integrity auditor). Not peer review.

Inputs: `brief.md`, `claims.md` (46 claims), `factcheck.md` (41 SUPPORTED, 5 PARTIAL; project statements P1, P2, P6 SUPPORTED and P3, P4, P5 PARTIAL), and the project files `reports/finalists.md`, `reports/cost_supply.md`, `reports/sensitivity.md`, `reports/study_results.md`, `pipeline/cost_supply.py`, `pipeline/finalists.py`. Tags such as [C4] point to `claims.md` and its verdict in `factcheck.md`. Tags such as [P4] point to the project-statement checks in `factcheck.md`. PARTIAL claims (C2, C3, C14, C18, C46) appear here only in the fact-checker's corrected wording.

## Summary

The literature has a mechanistic explanation for why V-containing alloys in this family are strong: V has the largest misfit volume of the five elements [C1]. Thermo-Calc's yield-strength model, by contrast, is a Walbrühl-type model whose validation, in the help pages read, covers only the Mo-Ta binary [C6, C7]. So its failure to rank our four validation alloys (Spearman ρ = -0.20, n = 4) (finalists.md) is not surprising. Two of the project's validation inputs need attention. MoNbTaV was tested as-cast, not annealed [C13, P4]. The NbTaVW value of 1530 MPa, which carries the largest model error (-743 MPa) (finalists.md), could not be checked against its primary source [P4]. In as-cast W-Nb-Mo-Ta-V, measured segregation sends W to dendrite cores and V and Nb to interdendritic regions [C11]. That direction is consistent with the project's calculated link between V content and freezing range (finalists.md), but no checked source measures how long these alloys take to homogenise. For cost and supply, the Nb and V USGS prices and producer shares in `cost_supply.md` check out [P1, P2], and the ferroniobium conversion already treats the price as gross weight [P2]. The EU criticality rule, however, is two-part (SR and EI), not SR alone [P3]. One published comparison places equiatomic Nb-Mo-Ta-W and V-Nb-Mo-Ta-W above Inconel 718 in strength above 800 °C [C37]. No checked paper compares them directly with C-103, TZM or Ta-10W, so those points on the Ashby chart have to come from data sheets [C42, C43, C44].

## Q1. Strength models for this family

**What the literature says.**
- Maresca and Curtin's edge-dislocation theory explains why the V-containing alloy is stronger than MoNbTaW: V has the largest misfit volume of the constituents, so it is the most potent strengthener [C1]. The same paper also points to pairing small and large atoms (such as V with Ta) and to stiff elements such as W [C1].
- With no adjustable parameters, that theory agrees very well with measured 296 K yield strengths for the Mo-Nb-Ta-V-W alloys tested up to then. The text does not name the plotted alloys or give numbers. The figure caption cites Yao et al.'s NbTaV-(Ti,W) paper among its experimental sources [C3].
- The theory underpredicts measured MoNbTaV, which the authors still consider reasonable. They attribute part of the gap to dendritic segregation and give composition-dependent strength differences of 158 MPa and 78 MPa. Which regions those numbers compare must be confirmed against the PDF before use [C2].
- For as-cast MoNbTaV, a Labusch-type solid-solution model predicted about 1.5 GPa, close to the measured value of about 1.5 GPa [C4]. The authors say the properties do not follow a simple rule of mixtures. They suggest solid-solution strengthening may matter more than expected and that the fine as-cast grain size may also contribute [C5].
- In NbTaV-(Ti,W) alloys, measured yield strengths were about 3.5-4.4 times the rule-of-mixture estimates [C8]. The abstract that was read gives no NbTaVW strength [C8].
- Senkov et al. found as-cast W-Nb-Mo-Ta-V harder than W-Nb-Mo-Ta (5250 vs 4455 MPa Vickers) and attribute this probably to a finer grain structure. This is a different explanation from misfit volume [C9].
- Thermo-Calc's Yield Strength Property Model implements the Walbrühl et al. (2017) solid-solution model. The help pages that were read do not mention Labusch, Varvenne or Maresca-Curtin models [C6]. Those pages show validation only for the Mo-Ta binary, and no W-Mo-Ta-Nb-V alloy appears [C7].

**How it compares with our results.**
- Thermo-Calc (Simplified mode, 1400 °C annealing temperature, solid solution only) predicted 1691, 1482, 787 and 1734 MPa for WMoTaNbV, MoNbTaW, NbTaVW and MoNbTaV, against measured 1246, 1058, 1530 and 1525 MPa. The resulting errors are +445, +424, -743 and +209 MPa (finalists.md). The rank correlation is ρ = -0.20 (finalists.md).
- The literature's explanation for strong V alloys is misfit-volume strengthening [C1]. Thermo-Calc's model is a different formulation, with validation shown only for Mo-Ta in the pages read [C6, C7]. Nothing checked here shows that it captures V's misfit effect, so its low NbTaVW value is consistent with a model mismatch, but no source tests that.
- The -743 MPa NbTaVW error depends on the 1530 MPa value, which the fact-checker could confirm only through a secondary source [P4]. The other three measured values check out and are as-cast; NbTaVW is recorded as cast (finalists.md), but its primary source was not read [P4].
- The project's caveat that strength depends on "cast vs annealed" processing (finalists.md) does not apply as worded, because the three verified validation measurements are as-cast and NbTaVW is recorded as cast [P4]. The model's 1400 °C annealing input does not match the tested condition of any of them [P5].
- The finalists' Thermo-Calc values span 163 MPa (finalists.md), and the project's own estimator has about 200 MPa error (study_results.md). The sources checked give no reason to expect the Thermo-Calc model to do better on this family [C7].

**What it means for the next step.**
- Before using the NbTaVW point, obtain the full text of Yao et al. MSEA 674 (doi:10.1016/j.msea.2016.07.102) and confirm the 1530 MPa value [P4].
- A Maresca-Curtin-type estimate is a published model with a stated agreement for Mo-Nb-Ta-V-W alloys at room temperature [C3]. It would be a better candidate tie-breaker for the finalists than Thermo-Calc's model. Numerical accuracy for this family cannot be quoted from the sources read [C3].
- Treat V-related strength gains as possibly partly grain-size effects in as-cast material [C5, C9].

## Q2. Casting segregation and homogenisation

**What the literature says.**
- In as-cast W-Nb-Mo-Ta, dendrite arms were enriched in W (+3.9 at.%) and depleted in Nb (-2.5) and Mo (-1.7), with Ta nearly unsegregated (+0.3) [C10].
- In as-cast W-Nb-Mo-Ta-V, dendrite arms were enriched in W (+4.7) and Ta (+1.1) and depleted in V (-4.0) and Nb (-1.7). Interdendritic regions were enriched in V (+6.3) and Nb (+2.6) and depleted in W (-7.3) [C11].
- In as-cast MoNbTaV, Ta and Mo enrich the dendrite arms, V strongly enriches the interdendritic regions, and Nb stays near the bulk value [C12]. Analogue alloys show the same pattern, with V and Ti going interdendritic in NbTaTiV [C20] and W and Ta enriching cores in NbTaTiW [C17].
- Homogenisation data for this family are thin:
  - Senkov et al. annealed neutron-diffraction samples of the equiatomic quaternary and quinary alloys at 1400 °C for 19 h (18 h elsewhere in the paper) to show BCC stability. They report no composition after the anneal, and their compression specimens were as-cast [C14].
  - Compositional inhomogeneity persisted even after compression at 1400 °C with dynamic recrystallisation [C15].
  - MoNbTaW has been annealed at 1800 °C for 4 days for homogenisation, but no homogeneity check was reported [C16].
  - Yao et al. did not homogenise MoNbTaV and say homogenisation was beyond their scope [C13].
- In W-containing analogues (NbTaTiW, MoNbTaTi), 35 h at 1673 K under vacuum left residual segregation, with Ta and W still core-enriched in NbTaTiW. DICTRA with MOBHEA2 predicted faster homogenisation than observed, and the authors hypothesise that this comes from the Ta diffusivity in the mobility database [C18].
- In MoNbTaTiVZr, 1400 °C for 12 h and then 1000 °C for 12 h did not homogenise the alloy, while high-pressure torsion did [C19].

**How it compares with our results.**
- The project's Scheil ranges are 600-844 °C overall: 623-732 °C for the finalists, 785-844 °C for the earlier candidates and equiatomic WMoTaNbV, and 600 °C for T6 (finalists.md). The project notes that the lower-V finalists have narrower ranges, which it calls an observation, not a tested rule (finalists.md).
- The measured partitioning of V and Nb to interdendritic regions and W to cores [C11, C12] fits a picture in which V widens the freezing range. The reports read here do not give Scheil partitioning per element, so this is a consistency of direction only, not a test.
- No checked source compares measured freezing ranges with Scheil for these alloys (claims.md, Q2 status).
- The project's report says that "typical high-temperature anneals happen above" the 664-791 °C split temperatures (finalists.md). That is true for the treatments found (1400 °C [C14], 1800 °C [C16]), but none of them was shown to remove segregation [C14, C16]. In two W- or Ta-containing analogues, DICTRA with MOBHEA2 predicted faster homogenisation than observed [C18].

**What it means for the next step.**
- Do not assume a homogenisation schedule from the literature; none has been verified for W-Mo-Ta-Nb(-V) [C14, C16].
- If DICTRA homogenisation runs are planned, the MOBHEA2 caveat applies [C18], and the results may underestimate the time needed.
- Report per-element Scheil partitioning for the finalists so that it can be compared directly with the dendrite and interdendritic differences in [C10] and [C11].

## Q3. Effect of vanadium

**What the literature says.**
- Measured density fell from 13.75 g/cm³ for as-cast W-Nb-Mo-Ta to 12.36 g/cm³ for as-cast W-Nb-Mo-Ta-V, and the V alloy's measured value equalled its theoretical value [C21].
- Between 600 and 1600 °C, the V-containing equiatomic alloy kept a higher yield strength than NbMoTaW. The text gives drops from 862 to 470 MPa for the V alloy and from 561 to 405 MPa for the V-free alloy [C22]; Table 3 gives 477 MPa at 1600 °C [C22]. V gives the largest misfit volume of the five elements [C1] and higher hardness in the as-cast quinary [C9].
- Both equiatomic alloys split in room-temperature compression, at 2.1 % (V-free) and 1.7 % (V-containing) plastic strain, so V did not bring compressive ductility in this pair [C23]. A 2025 paper, citing Senkov et al., says V addition raised high-temperature strength at the cost of plasticity and toughness [C25].
- In W-free VxNbMoTa, more V improved both room-temperature yield strength and ductility (abstract only) [C24].
- In the analogue system W-Ta-Cr-V, first-principles-based modelling associates higher V with lower order-disorder transition temperatures [C26].
- No checked source varies V content within W-Mo-Ta-Nb-V or gives a measured solidus or a per-at.% V slope (claims.md, Q3 status).

**How it compares with our results.**
- From the surrogate, +1 at.% V lowers the solidus by 18 °C (90 % interval -19 to -17 °C) and raises the two-BCC split temperature by 9 °C (+6 to +12 °C) (sensitivity.md). Neither slope can be checked against measurement with the sources read.
- The project concludes that V "hurts both goals" (sensitivity.md). The literature adds the other side: V is the strongest solid-solution strengthener in the misfit-volume picture [C1], and the V-containing alloy of the equiatomic pair kept higher high-temperature strength [C22]. V also lowers density [C21], which the project's composition objective already captures through rule-of-mixtures density (study_results.md).
- The project's density estimate is rule-of-mixtures with a median error of 0.3 % (study_results.md).
- The finalists keep V at 5.7-12.1 at.% (sensitivity.md). The ductility gain with V reported for W-free VxNbMoTa [C24] is not tested in W-containing alloys by any checked source.

**What it means for the next step.**
- The strength trade-off for V should be stated in `sensitivity.md` alongside the solidus and split slopes [C1, C22].
- A measured V-series in W-Mo-Ta-Nb-V remains an open gap. The planned ±2 at.% Thermo-Calc check (sensitivity.md) is the check the project has planned for the slopes.

## Q4. Cost and critical raw materials in alloy design

**What the literature says.**
- Supply risk has been used as a design objective in Mo-Nb-Ti-V-W refractory alloys. Mulukutla et al. used an element-level index of twelve indicators as one objective in batch Bayesian optimisation [C27]. Average yield strength stayed very similar across scenarios, raw-material cost was only compared after the fact, and the authors call cost a lagging indicator of supply risk [C28].
- Nominé et al. screened 30,201 equimolar HEAs on supply concentration, ESG, by-product dependence, production, reserves and footprint, without prices, and kept about 5 % as a resilient shortlist [C29].
- One Nb-alloy design study used C-103's density (8.85 g/cm³) and cost ($500/kg) as the benchmark to undercut [C36].
- USGS MCS 2026 prices and production:
  - Vanadium: Chinese 98 % V2O5 averaged $5.02/lb in 2025 and ferrovanadium $14.14/lb [C30]. China produced 82,000 t of a world total of about 110,000 t (V content, 2025 estimates) [C31, P1].
  - Niobium: ferroniobium had a 2025 unit value of $26/kg, and Brazil produced 104,000 t of 112,000 t [C32]. The $26/kg is a gross-weight unit value of U.S. ferroniobium trade, not a per-kg-Nb price [P2].
  - Tantalum: tantalite averaged $180/kg of Ta2O5 content in 2025, and the chapter gives no metal price [C33].
- Trade press (SMM, February 2026) quoted 99.95 % tantalum ingot at 5,500 yuan/kg and 99.5 % oxide at 3,900 yuan/kg [C34]. IMARC gives a US tantalum price of $502/kg for Q4 2025 with no form or purity stated [C35].
- The EU CRM 2023 supply-risk scores are W 1.2, Mo 0.8, Ta 1.3, Nb 4.4 and V 2.3, with economic importance (EI) 8.7, 6.7, 4.8, 6.5 and 3.9. A material is critical only if SR ≥ 1.0 and EI ≥ 2.8 [P3].
- Rotterdam APT traded at $278.22/kg in October 2026 per a trade-press report of MetalMiner. The article does not say whether this is per kg of APT or per kg of WO3 [P6].

**How it compares with our results.**
- **Ferroniobium.** The project derives Nb at $40/kg from $26/kg ferroniobium, treated as gross weight and divided by an assumed 0.65 Nb grade (cost_supply.md; `NB_IN_FENB = 0.65` in `pipeline/cost_supply.py`). This matches the fact-check's finding that $26/kg is gross weight [P2], so **it is not a correction**. The 0.65 grade itself is not confirmed by any checked source; the reviewer did not read it from USGS [C32]. It stays a flagged assumption, as the project already says (cost_supply.md).
- **Vanadium.** The project's V input ($5.02/lb V2O5, 98 %, China; China 82 of 110 kt) (cost_supply.md) matches the USGS chapter [C30, C31, P1]. The 2025 figure is a USGS estimate [P1], which the project does not mark, although it does mark W and Ta as "(est.)" (cost_supply.md).
- **Tantalum.** The project's $180/kg Ta2O5 input (cost_supply.md) matches USGS [C33].
- **Verification status.** The project's Limits section says the Nb price, V price and Nb and V producer shares came from search excerpts or secondary summaries and should be checked (cost_supply.md). They have now been checked against the USGS chapters [P1, P2].
- **EU threshold.** The project treats SR ≥ 1.0 alone as the EU criticality threshold and compares mass-weighted alloy scores (1.31-2.50) with it (cost_supply.md). The EU rule is two-part and applies to raw materials, not alloys [P3]. The project's conclusion that every alloy contains critical raw materials still holds element by element, because W, Ta, Nb and V each meet both criteria; Mo (SR 0.8) does not qualify [P3]. The reasoning given in the report does not support it, though.
- **Tungsten scenario.** The project converts $278.22/kg as if it were per kg WO3 ("≈ $2,782 per mtu WO3", ÷ 0.793) to get $351/kg W (cost_supply.md). The source does not state this basis [P6].
- **Metal mark-up.** The project's statement that arc-melting-grade metal costs "several times more" (cost_supply.md) has no checked source for W, Mo, Nb or V. The only metal-versus-raw-material data found are the SMM tantalum quotes [C34]; the IMARC figure does not state its form [C35]. Their units and bases differ, and they were not converted into a ratio.
- **Cost as an objective.** The project's three-objective trade-off (solidus, density, 2025 cost; 12 non-dominated alloys, 8 not finalists) (cost_supply.md) goes further than Mulukutla et al., who kept cost out of the optimisation [C28]. This is a design choice; the checked literature neither supports nor rejects it.

**What it means for the next step.**
- Apply the threshold and tungsten-basis fixes listed under "Corrections to the project".
- Open the USGS Tungsten and Molybdenum chapters, which were not read this run (claims.md), to verify the $380/mtu and $51/kg inputs.
- If cost is to stand for the price of a part, find a checked source for high-purity metal prices. Otherwise keep the existing "raw-material index" framing (cost_supply.md).

## Q5. Comparison with existing refractory alloys

**What the literature says.**
- Senkov et al. report that equiatomic Nb-Mo-Ta-W and V-Nb-Mo-Ta-W are much stronger than Haynes 230 at all temperatures studied and stronger than Inconel 718 above 800 °C [C37]. In that paper, Inconel 718 exceeds 1000 MPa up to 650 °C, falls to 138 MPa at 982 °C and melts at about 1210 °C [C38].
- A 2023 review tabulates the following [C39, C40]:

  | Alloy | Density (g/cm³) | Yield strength | Test mode |
  |---|---:|---|---|
  | Inconel 718 | 8.22 | 105 MPa at 1200 °C | tension |
  | CMSX-4 | 8.70 | 420 MPa at 1094 °C, 146 MPa at 1204 °C | tension |
  | MoNbTaW | 13.64 | 506 / 421 / 405 MPa at 1200 / 1400 / 1600 °C | compression |
  | MoNbTaVW | 12.35 | 735 / 656 / 477 MPa at 1200 / 1400 / 1600 °C | compression |

- The same review notes that these high-density alloys fall short of medium-density alloys on specific yield strength [C41].
- Data sheets give typical values:
  - C-103: 8.850 g/cm³, melting point 2350 °C, 0.2 % yield strength 262 MPa at 25 °C and 110 MPa at 1093 °C [C42].
  - Ta-10W: 16.9 g/cm³, melting point 3035 °C. Recrystallised-sheet yield strength is 70,000-89,000 psi at room temperature, 22,300-28,300 psi at 2600 °F, 10,500-12,300 psi at 3000 °F and 9,400 psi at 3500 °F [C43].
  - TZM: 10.2 g/cm³ and 750-900 N/mm² yield strength with no temperature or condition stated. The sheet gives no high-temperature yield strength and no melting point [C44].
- One paper states, as a secondary claim, that typical refractory HEAs reach 500-700 MPa at 1200 °C, above Ni superalloys [C45].
- Some Al-containing refractory HEAs (6.9-9.1 g/cm³) are described as having considerably better high-temperature strength than advanced Ni superalloys [C46].
- No checked paper compares W-Mo-Ta-Nb-V alloys directly with C-103, TZM or Ta-10W (claims.md, Q5 status).

**How it compares with our results.**
- The single-phase Pareto alloys span 11.42-14.93 g/cm³ and 2371-2822 °C calculated solidus (study_results.md). That places them between TZM (10.2 g/cm³) [C44] and Ta-10W (16.9 g/cm³) [C43] in density. Their solidus lies above C-103's melting point (2350 °C) [C42] and below Ta-10W's (3035 °C) [C43]. Our values are calculated solidus temperatures and the data-sheet values are melting points, so the two are not the same quantity.
- The project's estimated 1000 °C yield strengths for those alloys are 572-795 MPa, with about 200 MPa model error (study_results.md). The measured literature points listed here are at other temperatures (C-103 at 1093 °C [C42]; Inconel 718 and CMSX-4 at 1094-1204 °C [C39]; MoNbTaW and MoNbTaVW from 1200 °C up [C40]), so a 1000 °C comparison mixes estimate and measurement.
- On a per-density basis the W-rich finalists may compare less well, as the review notes for high-density RHEAs [C41].

**What it means for the next step (Ashby chart).**
- Plot the comparison alloys at their source temperatures. Mark tension versus compression [C39] and typical (non-design) data-sheet values [C42, C43]. Convert the Ta-10W psi and °F values explicitly in the plotting code [C43].
- Leave TZM off the strength axis until a checked high-temperature yield value is found [C44].
- Use MoNbTaVW and MoNbTaW from the review [C40] as the measured HEA anchor points next to the project's estimates.

## Corrections to the project

Each row below is a concrete fix with its supporting claim or fact-check id. Line numbers refer to the files as read on 2026-11-11.

| # | File (location) | Current wording | Corrected wording | Support |
|---|---|---|---|---|
| 1 | `reports/finalists.md` §1 table, MoNbTaV row (l. 13); generated from `pipeline/finalists.py` `VALIDATION` (l. 30) | "BCC (annealed)" / processing `"annealed"` | "BCC (as-cast)" / `"as-cast"`; add a code comment that the primary source overrides the MPEA dataset label | P4, C13, factcheck D5 |
| 2 | `reports/finalists.md` §3 table, MoNbTaV row (l. 48); `pipeline/finalists.py` `YS_MEASURED` (l. 45) | "MoNbTaV (annealed)" / note `"annealed"` | "MoNbTaV (cast)" / note `"cast"` | P4, C13 |
| 3 | `reports/finalists.md` §1 caveats (l. 18); `pipeline/finalists.py` (l. 119-120) | "The anneal temperature for MoNbTaV is not recorded in the dataset." | "The MoNbTaV source reports no anneal; the alloy was tested as-cast (the dataset's 'annealed' label is wrong)." | P4, C13 |
| 4 | `reports/finalists.md` §3, NbTaVW row (l. 47); `pipeline/finalists.py` `YS_MEASURED` (l. 44) | "NbTaVW (cast) \| 1530" | Keep the value but add a note: "1530 MPa not verified against the primary source (secondary citation only)". The "Reading" paragraph should state that the -743 MPa error rests on this unverified value | P4 |
| 5 | `reports/finalists.md` §3 caveats (l. 64); `pipeline/finalists.py` (l. 187-188) | "measured strengths depend on processing (cast vs annealed) and test, which the model does not represent." | "The MoNbTaW, WMoTaNbV and MoNbTaV strengths are from as-cast specimens, and NbTaVW is recorded as cast (primary source not checked); the model was run with a 1400 °C annealing temperature, which matches none of them." | P4, P5, C14 |
| 6 | `reports/finalists.md` §3 intro (l. 41) and the repo text giving the reason for the 1400 °C setting (P5; that text was not in the files read for this run) | "annealing temperature 1400 °C" (justified elsewhere as: Senkov et al. homogenised cast WMoTaNb and WMoTaNbV at 1400 °C) | "Senkov et al. annealed neutron-diffraction samples at 1400 °C for 19 h (18 h elsewhere in the paper) to show BCC stability. They did not call it homogenisation or show segregation was removed, and their yield strengths are from as-cast specimens." | P5, C14, C15 |
| 7 | `reports/cost_supply.md` (l. 19); `pipeline/cost_supply.py` (l. 145-147) | "EU supply risk: 1.0 or higher counts as high (the EU criticality threshold). Mo (0.8) is the only one of the five below it." | "EU CRM 2023 classes a raw material as critical only if SR ≥ 1.0 and EI ≥ 2.8 (EI: W 8.7, Mo 6.7, Ta 4.8, Nb 6.5, V 3.9). W, Ta, Nb and V meet both; Mo (SR 0.8) does not." | P3 |
| 8 | `reports/cost_supply.md` (l. 35); `pipeline/cost_supply.py` (l. 181-183) | "Every one of the 50 alloys scores 1.31–2.50, above the EU threshold of 1.0: no composition in this family avoids critical raw materials." | "Every one of the 50 alloys scores 1.31–2.50 (mass-weighted SR). The EU threshold applies to raw materials, not alloys; every alloy here contains W, Ta, Nb and V, all of which are EU-critical." | P3 |
| 9 | `pipeline/cost_supply.py` docstring (l. 14) and `SR_THRESHOLD` comment (l. 74) | "(EU CRM study 2023; >= 1.0 = high)" / "EU criticality threshold for supply risk" | "(EU CRM 2023; critical if SR >= 1.0 AND EI >= 2.8)"; add an `EI` value per element to `SUPPLY` | P3 |
| 10 | `reports/cost_supply.md` (l. 17); `pipeline/cost_supply.py` `W_2026` (l. 61-62) | "$278.22/kg (≈ $2,782 per mtu WO3), APT ... ÷ 0.793" | "$278.22/kg APT, Rotterdam, October 2026 (Canadian Mining Journal, 4 Nov 2026, reporting MetalMiner). Basis not stated by the source; **assumed** per kg WO3 for the ÷ 0.793 conversion." | P6 |
| 11 | `reports/cost_supply.md` Inputs, V row (l. 15); `pipeline/cost_supply.py` (l. 57) | "$5.02/lb V2O5 (98 %), China, 2025 avg" | "$5.02/lb V2O5 (98 %), China, 2025 avg (est.)" to match the W and Ta rows | P1, C30 |
| 12 | `reports/cost_supply.md` Limits (l. 65); `pipeline/cost_supply.py` (l. 215-219) | "...the Nb price from a search excerpt of the USGS Niobium chapter; the V price and the Nb and V producer shares from secondary summaries ... Check them against the chapters before citing externally." | "The Nb and V prices and producer shares were checked against the USGS MCS 2026 Niobium and Vanadium chapters (fact-check, run-2026-11-11). The W, Mo and Ta figures were read from the USGS chapters by the project; of these, only the Ta price was re-checked in run-2026-11-11." | P1, P2, C30-C33 |

**Checked and not a correction.** The ferroniobium conversion in `pipeline/cost_supply.py` (`26 / NB_IN_FENB`, `NB_IN_FENB = 0.65`) treats $26/kg as gross weight. That is consistent with the fact-check, which defines the USGS figure as a gross-weight unit value [P2]. The 0.65 grade is still an unverified assumption [C32], and the code and report already label it as one (cost_supply.md).

## Open leads

None of these are findings.
- Walbrühl et al. (2017), the paper behind Thermo-Calc's model; the Thermo-Calc Simplified-mode help page; and the TCHEA Examples Collection PDF. None was opened (claims.md, C6, C7).
- Yao et al., MSEA 674 (2016) full text, the primary source for NbTaVW 1530 MPa. The only source found for the value is a secondary encyclopedia.pub entry (factcheck.md, P4).
- Wang et al. 2021 Scripta Mater. on VxNbMoTa (claims.md, not opened). The Wang et al. MSEA 808 result was read from the abstract only [C24].
- USGS MCS 2026 Tungsten and Molybdenum chapters (claims.md, not opened this run).
- The official EC copy of the EU CRM 2023 study. The fact-checker read a third-party mirror (factcheck.md, P3).
- The MetalMiner "Tungsten Resilience White Paper" (factcheck.md, P6; not opened).
- A catalogue entry for a two-phase NbMoTaWV paper (eld.bl.uk) and an OSTI record "Lattice-Distortion-Enhanced Yield Strength in a Refractory High-Entropy Alloy" (Adv. Mater. 32(49)). Only metadata loaded for these (claims.md search log).

## Open questions

- Fact-check D5 reports that Yao et al.'s Table 1 lists a calculated σ0.2 of 333 MPa for MoNbTaV. The abstract says a simple model predicts about 1.5 GPa [C4]. What the 333 MPa figure is has not been resolved (factcheck.md).
- Which regions Maresca and Curtin's 158 MPa and 78 MPa figures compare needs checking against the PDF [C2].
- What does the "annealing temperature" input do in Thermo-Calc's Simplified yield-strength mode? The page describing it was not opened (claims.md, C6).
- The Nb grade of USGS ferroniobium (the project assumes 0.65) and whether the USGS V2O5 price is per lb of product or of contained V2O5 (the project divides by 0.98) are not established by any checked source.
- What is the mark-up of arc-melting-grade W, Mo, Nb and V over concentrate, oxide or ferroalloy prices? No checked source found one.
- How long does homogenisation take for W-Mo-Ta-Nb(-V)? No checked source measured residual segregation after a heat treatment of these alloys.
- What are TZM's yield strength at temperature and its melting point? The checked data sheet gives neither [C44].
- Unresolved internal inconsistencies in the sources: 470 vs 477 MPa at 1600 °C (D1); 19 vs 18 h anneal (D2); Mo in W-Nb-Mo-Ta dendrites, where Table 4 and the Results text say depleted and the Conclusions say enriched (D3); 2.1 % vs possibly 2.6 % failure strain for Nb25Mo25Ta25W25 (factcheck.md).

## References

- Maresca, F., Curtin, W.A. Mechanistic origin of high strength in refractory BCC high entropy alloys up to 1900K. arXiv:1901.02100v3 (2019); published Acta Mater. 182 (2020) 235 (published version not opened). https://arxiv.org/pdf/1901.02100 [C1, C2, C3]
- Yao, H., Qiao, J.-W., Gao, M.C., Hawk, J.A., Ma, S.-G., Zhou, H. MoNbTaV medium-entropy alloy. Entropy 18(5), 189 (2016). doi:10.3390/e18050189 [C4, C5, C12, C13, P4]
- Thermo-Calc Software. About the Yield Strength Property Model (2025b help). https://help.thermocalc.com/2025b/content/property_models-gen/yieldstrength-about.htm [C6]
- Thermo-Calc Software. Yield Strength (TCHEA validation example); PM_G_06: Yield Strength HEA. https://help.thermocalc.com/2025b/content/databases/tchea/valid_examples/tchea_validex_yieldstrength.htm ; https://help.thermocalc.com/2025b/content/examples/propmodels-gen/pm_g_06_yield_strength_hea.htm [C7]
- Yao, H.W., Qiao, J.W., Gao, M.C., Hawk, J.A., Ma, S.G., Zhou, H.F., Zhang, Y. NbTaV-(Ti,W) refractory high-entropy alloys: experiments and modeling. Mater. Sci. Eng. A 674 (2016) 203-211. doi:10.1016/j.msea.2016.07.102 (abstract only) [C8, P4]
- Senkov, O.N., Miracle, D.B., Wilks, G.B., Chuang, C.P., Liaw, P.K. Refractory high-entropy alloys. AFRL-RX-WP-TP-2011-4295 (preprint, 2011). https://apps.dtic.mil/sti/pdfs/ADA550824.pdf [C9, C10, C11, C21]
- Senkov, O.N., Wilks, G.B., Scott, J.M., Miracle, D.B. Mechanical properties of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20 refractory high-entropy alloys. AFRL-RX-WP-TP-2011-4289 (preprint, 2011), https://apps.dtic.mil/sti/pdfs/ADA550865.pdf ; published Intermetallics 19 (2011) 698-706, doi:10.1016/j.intermet.2011.01.004 (published text not opened) [C14, C15, C22, C23, C37, C38, P4, P5]
- Bajpai, V., Maiti, S., Mishra, S., Rai, B. Temperature dependent phase stability of Mo-Nb-Ta-W refractory high-entropy alloys. arXiv:2103.07951. https://arxiv.org/pdf/2103.07951 [C16]
- Puerling, R., et al. Thermodynamics and kinetics of refractory multi-principal element alloys: an experimental and modeling comparison. NSC-614-4990 (2023). https://www.osti.gov/servlets/purl/1989196 [C17, C18]
- Duan, C., et al. Deformation-induced homogenization of the multi-phase senary high-entropy alloy MoNbTaTiVZr processed by high-pressure torsion. Mater. Sci. Eng. A 871, 144923 (2023); arXiv:2306.05711. https://www.arxiv.org/pdf/2306.05711 [C19]
- Lee, C., et al. Lattice distortion in a strong and ductile refractory high-entropy alloy. Acta Mater. 160 (2018) 158-172. https://par.nsf.gov/servlets/purl/10178918 [C20]
- Wang, M., Ma, Z.L., Xu, Z.Q., Cheng, X.W. Effects of vanadium concentration on mechanical properties of VxNbMoTa refractory high-entropy alloys. Mater. Sci. Eng. A 808, 140848 (2021). doi:10.1016/j.msea.2021.140848 (abstract only) [C24]
- Zhao, R., et al. Microstructure and mechanical properties of TixNbMoTaW refractory high-entropy alloy for bolt coating applications. Coatings 15(2), 120 (2025). doi:10.3390/coatings15020120 [C25]
- Sun, B., et al. Thermodynamic assessment of the quaternary WTaCrV refractory high entropy alloy as a means to guide experimental approaches. Acta Mater. 299 (2025) 121435. https://scientific-publications.ukaea.uk/wp-content/uploads/A2E98271-CDC1-484B-80F4-D403440D7190.PDF [C26]
- Mulukutla, M., et al. Supply risk-aware alloy discovery and design. arXiv:2409.15391v1 (2024). https://arxiv.org/html/2409.15391v1 [C27, C28]
- Nominé, A., et al. The hidden sustainability bottleneck in high-entropy alloy design. arXiv:2601.00852v1. https://arxiv.org/pdf/2601.00852v1 [C29]
- U.S. Geological Survey. Mineral Commodity Summaries 2026: Vanadium; Niobium (Columbium); Tantalum. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-vanadium.pdf ; https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-niobium.pdf ; https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-tantalum.pdf [C30, C31, C32, C33, P1, P2]
- Shanghai Metals Market. Supply contraction drives up tantalum ore prices... (27 Feb 2026). https://news.metal.com/newscontent/103781654-Supply-Contraction-Drives-Up-Tantalum-Ore-Prices-Smelting-Cost-Increases-Face-Short-Term-Obstacles-SMM-Analysis [C34]
- IMARC Group. US tantalum prices hold at USD 502/kg amid stable industrial demand (18 Feb 2026). https://www.imarcgroup.com/news/tantalum-price-index [C35]
- Nahin, A.M., et al. A low-cost, strong, and ductile single-phase Nb-based refractory complex concentrated alloy. arXiv:2602.07293. https://arxiv.org/pdf/2602.07293 [C36]
- Atli, K.C., Karaman, I. A short review on the ultra-high temperature mechanical properties of refractory high entropy alloys. Front. Met. Alloys 2 (2023). doi:10.3389/ftmal.2023.1135826 [C39, C40, C41]
- Materion. Niobium C-103 bar and rod data sheet, DS-AM-622 (2024). https://hkvxni.files.cmp.optimizely.com/download/assets/Niobium+C-103+Bar+and+Rod+Data+Sheet/8aef8eca300b11ef899fe60a55c50f3d [C42]
- ATI. ATI Ta-10W technical data sheet (5/13/13). https://www.atimaterials.com/Products/Documents/datasheets/niobium-hafnium-tantalum-vanadium/tantalum/ati_Ta10W_v5.pdf [C43]
- Wieland Duro. TZM product data sheet. https://www.wieland.com/da/content/download/12678/file/TZM_EX_EN.pdf [C44]
- Singh, P., et al. Design of high-strength refractory complex solid-solution alloys. arXiv:1710.06983. https://arxiv.org/pdf/1710.06983 [C45]
- Senkov, O.N., Woodward, C., Miracle, D.B. Microstructure and properties of aluminum-containing refractory high-entropy alloys. JOM 66(10) (2014) 2030-2042. doi:10.1007/s11837-014-1066-0 (abstract only) [C46]
- European Commission (Grohol, M., Veeh, C.). Study on the Critical Raw Materials for the EU 2023, Final Report. https://ec.europa.eu/docsroom/documents/54114 (fact-checker read a third-party mirror of this PDF) [P3]
- Canadian Mining Journal. Western tungsten prices nearly quadruple China's: report (4 Nov 2026), reporting MetalMiner. URL not recorded in factcheck.md [P6]
