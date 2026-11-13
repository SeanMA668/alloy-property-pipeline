# Literature notes: run 2026-11-13

Literature notes produced by AI agents (reviewer, fact-checker, note-writer, integrity auditor). Not peer review.

Inputs: `brief.md`, `claims.md` (44 claims), `factcheck.md` (40 SUPPORTED, 4 PARTIAL: C15, C17, C24, C33; project statements P1 and P3 SUPPORTED, P2 and P4 PARTIAL), and the project files `reports/strength_model.md`, `pipeline/strength_model.py`, `tests/test_strength_model.py`, `reports/finalists.md` and `README.md`. Tags such as [C4] point to `claims.md` and its verdict in `factcheck.md`. Tags such as [P2] point to the project-statement checks in `factcheck.md`. "factcheck D5" and similar point to the fact-checker's resolution of the reviewer's discrepancy list. PARTIAL claims appear here only in the fact-checker's corrected wording. Every Maresca-Curtin finding below was checked against the arXiv v3 preprint (13 Jun 2019), not the published Acta Materialia article, which neither agent could open.

## Summary

The constants and equations in `pipeline/strength_model.py` all match the arXiv v3 preprint of Maresca and Curtin: prefactors 0.040 and 2.00, α = 1/12, a reference strain rate of 10⁴ s⁻¹, M = 3.067, rule-of-mixtures elastic constants and Vegard misfit volumes [C1-C7]. The code also includes the 1/3 in the bulk modulus, which the preprint leaves out but the group's own numbers use (factcheck D4). One point is still open and it matters. The preprint has two temperature forms with a switch at τy/τy0 = 0.5 [C5]. Later papers, two of them co-authored by Curtin, credit the published paper with a single exponential form that has a 0.91 exponent [C15; factcheck D1]; Baruffi et al. use that form without a reference [C18]. No checked source gives the four validation predictions (922, 1411, 1425, 1317 MPa) under the single form, so this stays the first item for university access. On inputs, the code's Ta elastic constants match the Featherston and Neighbours 0 K values, but the code labels them as room-temperature values [C22; factcheck side-by-side]. Its Ta and Nb lattice parameters also do not match the X-ray values that were found (25 °C for Ta; temperature not shown for Nb) [C26, C28]. The nearest published room-temperature predictions, from Yin et al., are 954 MPa for MoNbTaW and 1347 MPa for MoNbTaWV [C12]. Ours are 922 and 1411 MPa (strength_model.md). The NbTaVW value of 1530 MPa is still confirmed only through a secondary compilation, which gives neither the processing state nor the strain rate [C30]. On mechanism, the authors say the edge model agrees well with experiment even at low temperature, where edge and screw strengths may be comparable [C37]. One later study of annealed VNbMoTaW found edge and screw segments present almost equally, edge and screw models giving similar strengths, and screw-type kink migration controlling the rate at room temperature [C40]. So an edge-only model that matches a room-temperature measurement does not by itself show that edge glide is the controlling mechanism.

## Q1. The reduced Maresca-Curtin model as implemented

**What the literature says.**
- In the arXiv v3 preprint, the reduced model gives τy0 and ΔEb as power laws in μ̄, (1+ν̄)/(1-ν̄) and Σ cn ΔVn²/b̄⁶, with prefactors 0.040 and 2.00 and α to the powers -1/3 and +1/3 [C1]. These prefactors were fitted to the full theory. They reproduce most high-strength, high-temperature full-model results within 5 %, and the whole full-model set with a standard deviation of about 10 % [C8].
- The main analysis uses α = 1/12. Appendix A tests 1/16, 1/12 and 1/8 and reports that room-temperature predictions are rather sensitive to α, while predictions over 296-1900 K are quite insensitive [C2].
- The reference strain rate is 10⁴ s⁻¹. The experimental comparisons use 10⁻³ s⁻¹ for one set of data and 5·10⁻⁴ s⁻¹ for two others [C3].
- The Taylor factor is M = 3.067 [C4]. Two later papers from the group print 3.06 [C11, C18], which the fact-checker treats as rounding (factcheck D3).
- The preprint gives two temperature forms: a 2/3-power law for τy/τy0 > 0.5 and an exponential with a 1/0.55 factor for τy/τy0 < 0.5. The exponent 0.91 does not appear anywhere in v3 [C5].
- Alloy elastic constants are rule-of-mixtures averages, with μ̄ = √[½C̄44(C̄11-C̄12)] and the standard isotropic ν̄ [C6]. The preprint prints the bulk modulus without the 1/3 [C6]. Yin et al. include it [C11], and Yin's tabulated μ and ν can only be reproduced with it (factcheck D4).
- Misfit volumes follow Vegard's law from experimental elemental atomic volumes [C7]. The preprint does not say which elemental elastic-constant set feeds its experimental-alloy predictions [C7; factcheck D5].
- Later work by the same group:
  - Yin, Maresca and Curtin use the same prefactors, α = 0.0833, M = 3.06, ε̇0 = 10⁴ s⁻¹, 300 K and 10⁻³ s⁻¹, rule-of-mixtures Cij with B = (C11+2C12)/3, and Vegard misfits [C11]. As extracted, their strength equation is the 2/3-power form only, with no exponential branch (factcheck, C11 finding).
  - Kubilay et al. use 0.040, 2.00, α = 1/12 and M = 3.067 [C14]. They write that, to cover the full temperature range, the published Acta paper proposed a single exponential form with exponent 0.91. The extraction does not settle whether the 1/0.55 factor sits inside or outside the bracket raised to 0.91 [C15].
  - Lee et al. keep α = 1/12 and the two forms with the switch at 0.5, citing the Acta paper [C17]. They obtain alloy-specific coefficients from the full theory (Aσ 0.0437, AE 2.02 for NbTaTiV; 0.0344, 1.93 for CrMoNbV) and state that across BCC HEAs these fall in Aσ = 0.040 ± 0.004 and AE = 2.00 ± 0.2. Nothing is fitted to experiment [C17].
  - Baruffi et al. keep the prefactors but use α = 1/6, M = 3.06 and a single ad hoc exponential with exponent 0.91 and no switch [C18].
  - Xiao et al. used the reduced model with rule-of-mixtures and Vegard inputs on Nb-Mo-Ta-W films, and only as a relative proxy, because predicted strength did not scale directly with measured hardness [C19].
- Published room-temperature predictions found:
  - Yin et al. predict 954 MPa for MoNbTaW (measured ≈1058) and 1347 MPa for MoNbTaWV (measured ≈1246) at 300 K and 10⁻³ s⁻¹, with a = 3.228 / 3.192 Å, μ = 103 / 92 GPa and ν = 0.31 / 0.32 [C12].
  - No checked source gives a prediction for NbTaVW or MoNbTaV [C12].
- The Curtin group's elemental inputs:
  - W, Mo and Ta elastic constants equal the Featherston and Neighbours 0 K rows, not their 300 K rows [C14, C20, C22, C25; factcheck D5].
  - Nb and V elastic constants have no identified source (factcheck D5).
  - The V atomic volume of 14.020 Å³ [C13] matches a = 3.038 Å as listed by Baruffi et al. [C29] (factcheck D6).

**How it compares with our results.**
- The code matches the preprint on every item the brief lists:
  - prefactors 0.040 and 2.00;
  - `ALPHA = 1/12`;
  - `EPS0 = 1.0e4`;
  - `TAYLOR = 3.067`;
  - the two forms with `low if low > 0.5 else high`;
  - μ = √(0.5·C44·(C11-C12)) and B = (C11+2C12)/3;
  - misfits V_n - V̄ (strength_model.py).
  On B, the code follows the group's practice rather than the preprint's printed formula, which is correct (factcheck D4).
- Our room-temperature predictions are WMoTaNbV 1411, MoNbTaW 922, NbTaVW 1425 and MoNbTaV 1317 MPa. Against the measured values (1246, 1058, 1530, 1525 MPa), the errors are +165, -136, -105 and -208 MPa, with a mean absolute error of 153 MPa and ρ = 0.80 (strength_model.md).
- For the two alloys Yin et al. also predict, ours are 922 MPa against their 954 MPa for MoNbTaW, and 1411 MPa against their 1347 MPa for the quinary [C12] (strength_model.md). Both studies compare with the same measured values, ≈1058 and ≈1246 MPa [C12]. The two calculations differ in their inputs. The Curtin group's tabulated elemental inputs (Kubilay et al.) are 0 K Featherston and Neighbours constants for W, Mo and Ta (factcheck D5); Yin et al. do not tabulate theirs [C13]. Yin et al. use a V volume corresponding to a = 3.038 Å (factcheck D6). They use M = 3.06 [C11], and as extracted their strength equation is the 2/3-power form only (factcheck, C11 finding). How much each difference contributes has not been worked out.
- **Temperature law (open item, D1).** The report states that at room temperature our alloys sit near τ/τ0 = 0.5, where the v3 forms switch and differ by about 5 % (strength_model.md). The project already reports one alternative, `switch="continuous"`, which the report describes as switching where the two v3 forms cross: WMoTaNbV 1497, MoNbTaW 978, NbTaVW 1512 and MoNbTaV 1396 MPa (mean absolute error 120 MPa, ρ = 0.80) (strength_model.md). That alternative is not the single 0.91-exponent form that later papers attribute to the published article [C15; factcheck D1]. **How the four validation predictions would change under the single form has not been computed by the project or found in any checked source.** The answer also depends on the unresolved bracket placement. The fact-checker estimates the two readings differ by about 5 % in the exponent: (1/0.55)^0.91 = 1.72 against 1/0.55 = 1.82 (factcheck D1).
- α: the code uses 1/12, the value in the preprint's main analysis [C2]. Later work by the same group also uses 1/6 [C18]. Since the preprint reports that room-temperature predictions are rather sensitive to α [C2], and all four validation points are at room temperature (strength_model.md), the choice of α matters most exactly where the project validates.

**What it means for the next step.**
- Do not change the switch rule until the published equations are read (Needs Sean, item 1). After that, compute the four validation predictions under whichever form the published paper uses, and under both bracket placements if it is the 0.91 form, then report them next to the current table.
- Label the current equations as the arXiv v3 forms in the report and the code (Corrections 3).
- Optionally, report the four predictions with α = 1/6 alongside the 1/12 values, as a sensitivity check [C2, C18].

## Q2. Elemental inputs

**What the literature says.**
- Featherston and Neighbours' 300 K single-crystal constants, converted at an assumed 100 GPa per printed unit, are as follows. The unit exponent is illegible in the extraction, and the conversion is reviewer arithmetic.
  - W: 523.27 / 204.53 / 160.72 GPa [C20].
  - Mo: 440.77 / 172.43 / 121.65 GPa [C21].
  - Ta: 260.91 / 157.43 / 81.82 GPa [C22].
- Their 0 K rows are:
  - W: 532.55 / 204.95 / 163.13 GPa [C20; factcheck D5].
  - Ta: 266.32 / 158.16 / 87.36 GPa [C22].
  - Mo: 450.02 / 172.92 / 125.03 GPa (via Gong and Dal Corso) [C25].
- Measured Mo constants differ between experiments.
  - The 300 K values of Katahara et al. (464.8 / 161.6 / 108.9 GPa) and of Bolef and de Klerk (469.6 / 167.6 / 106.8 GPa) both come via a secondary table [C25].
  - Featherston and Neighbours consider the difference real and specimen-dependent [C21].
- The OSTI abstract of Bolef's paper gives values at 27 °C, in 10¹¹ dyn cm⁻² (10 GPa per unit, reviewer arithmetic):
  - V: 22.8 / 11.9 / 4.26.
  - Ta: 26.7 / 16.1 / 8.25.
  - Nb: c11 24.6 and c44 2.87. The Nb c12 shows as "13." and may be truncated, anywhere from 13 to 13.9 [C24].
- Lattice parameters near room temperature:
  - W 3.1648, Mo 3.1472 and Ta 3.3058 Å at 25 °C [C26].
  - V 3.0241 Å at 25 °C, with three other entries at 3.0236-3.04 Å [C27].
  - Nb 3.3063 Å, from a study covering 4.2-300 K. The temperature of this particular entry is not shown [C28].

**How it compares with our results.** Code values are from `LATTICE_A` and `ELASTIC` (strength_model.py). The code comment labels all of them as room-temperature handbook values (strength_model.py).

| | Code a (Å) | Open source a (Å) | Code C11/C12/C44 (GPa) | Room-T measured (GPa) | 0 K (GPa) |
|---|---|---|---|---|---|
| W | 3.1652 | 3.1648, 25 °C [C26] | 523.3/204.5/160.7 | 523.3/204.5/160.7 F&N 300 K [C20] | 532.55/204.95/163.13 [C20; factcheck D5] |
| Mo | 3.1470 | 3.1472, 25 °C [C26] | 465.0/163.0/109.0 | 464.8/161.6/108.9 Katahara; 469.6/167.6/106.8 Bolef & de Klerk [C25]; 440.8/172.4/121.7 F&N [C21] | 450.02/172.92/125.03 [C25] |
| Ta | **3.3029** | 3.3058, 25 °C [C26] | **266.0/158.0/87.4** | 260.9/157.4/81.8 F&N [C22]; 267/161/82.5 Bolef [C24] | **266.32/158.16/87.36** [C22] |
| Nb | **3.3004** | 3.3063, temperature not shown [C28] | 246.5/134.5/28.7 | 246/130-139/28.7 Bolef [C24] | not found |
| V | 3.0240 | 3.0241, 25 °C [C27] | 231.0/120.0/43.2 | 228/119/42.6 Bolef [C24] | not found |

- **Ta elastic constants are 0 K values labelled as room temperature.** The code's Ta values match the Featherston and Neighbours 0 K row, not their 300 K row or Bolef's 27 °C values. C44 is 87.4 GPa in the code, against 81.8 and 82.5 GPa in the two room-temperature measurements [C22, C24; factcheck side-by-side]. Ta is the only element in the code that the fact-check identified this way. W matches the 300 K row exactly [C20]. Mo is close to the Katahara 300 K values [C25]. Nb and V are close to Bolef's 27 °C values [C24]. (The Curtin group's own inputs use 0 K values for W and Mo as well, but our code does not [C14; factcheck D5].)
- **Lattice parameters.** W, Mo and V agree with the 25 °C X-ray values to within 0.0004 Å [C26, C27; factcheck side-by-side]. Ta (3.3029 against 3.3058 Å) [C26] and Nb (3.3004 against 3.3063 Å, temperature unknown) [C28] do not. The code gives only "standard handbook values" as its source (strength_model.py). Simmons and Wang, which the Curtin group cites for its volumes [C13], was not opened.
- Our V lattice parameter (3.0240 Å) matches the 25 °C X-ray value [C27]. The Curtin group's V volume corresponds to 3.038 Å [C13, C29; factcheck D6]. That difference feeds straight into the V misfit, which is the largest term for the alloys studied here (factcheck P4).

**What it means for the next step.**
- Replace the Ta elastic constants with a room-temperature set, either Featherston and Neighbours 300 K [C22] or Bolef 27 °C [C24], or else label them as 0 K. Then rerun the validation and finalist tables. The effect on 922/1411/1425/1317 MPa has not been computed (Corrections 1).
- Record the source of each element's value in the code comment, and flag the Ta and Nb lattice parameters as unmatched (Corrections 2).

## Q3. Validation data: NbTaVW 1530 MPa

**What the literature says.**
- Gorsse et al.'s open database lists NbTaVW with:
  - phase BCC and hardness HV 492;
  - a compression test, 1530 MPa, and a strain of 12 %;
  - Yao et al., MSEA 674 (2016) 203-211, as the source [C30].
  The table gives no processing state and no strain rate. 1530 sits in the yield-strength column by position, but the table does not mark empty cells, so whether it is the yield strength or the maximum stress is an inference [C30; factcheck D9].
- The visible part of Yao et al.'s abstract says a single BCC phase was confirmed in the as-cast ingots of the NbTaV-(Ti,W) alloys. It gives no NbTaVW strength, test method or strain rate [C31].
- Maresca and Curtin's Table 2 lists the experimental NbTaVW at a non-equiatomic composition (Nb 28.5, Ta 29.65, V 20.67, W 21.18) and the experimental MoNbTaV at Mo 24.9, Nb 25.8, Ta 26.6, V 22.7 [C10].
- **Still missing** because the primary full text was not opened:
  - the value as printed;
  - whether it is the 0.2 % offset yield;
  - the specimen condition tested;
  - the strain rate;
  - the specimen size;
  - the measured composition (claims.md Q3 status; factcheck Needs Sean item 2).

**How it compares with our results.**
- The project uses 1530 MPa for equiatomic NbTaVW, recorded as cast and marked as not verified against the primary source (strength_model.py; strength_model.md). The secondary listing agrees on the number and on compression testing [C30]. It does not confirm the as-cast state or that the value is a yield strength [C30].
- Our validation uses equiatomic compositions (strength_model.py). For NbTaVW and MoNbTaV, the compositions Maresca and Curtin list for the experimental alloys are not equiatomic [C10]. How much our predictions would change at those compositions has not been computed.
- The report assumes 10⁻³ s⁻¹ for all four alloys (strength_model.md). Maresca and Curtin's comparisons used 10⁻³ or 5·10⁻⁴ s⁻¹, depending on the data source [C3]. The NbTaVW strain rate is unknown [C30, C31].

**What it means for the next step.**
- The fact-checker found an OSTI accepted manuscript of Yao et al. that blocks automated fetching but may open in a normal browser (factcheck Needs Sean item 2). Try that before asking for library access.
- Once the paper is read, record the measured composition, condition and strain rate in `MEASURED`. Consider predicting at the measured compositions [C10].

## Q4. High temperature and limits

**What the literature says.**
- In the preprint, Maresca and Curtin state that their high-temperature predictions for MoNbTaW and MoNbTaVW fall below experiment, and that the measured plateau between 900 and 1300 K is not predicted. They also say edge strengthening agrees fairly well with the measured high-temperature behaviour [C32].
- Their Fig. 1 compares predictions with experiments (ref. [2]) for these HEAs and for Ni-based superalloys at 800-1900 K. The predicted values are in the figure only and were not extracted [C33].
- Measured compressive yield stresses, from a secondary compilation:
  - MoNbTaW: 548, 506, 421 and 405 MPa.
  - MoNbTaVW: 842, 735, 656 and 477 MPa.
  - Both at 1000, 1200, 1400 and 1600 °C [C34].
- Kubilay et al. compare reduced-theory predictions with experiments at 0, 1000 and 1200 °C. For the MoNbTaW(Ti)(V) family, quantitative agreement is weaker than for the Hf-containing family. The theory still captures the strengthening from V and follows the measured trend up to 1200 °C [C35]. Their calculation uses the single 0.91-exponent form [C15].
- Baruffi et al. state that no theory captures the intermediate-temperature plateau [C43].
- **Edge or screw at room temperature.**
  - Maresca and Curtin argue that, unlike pure BCC metals, BCC HEAs can be edge-controlled, especially at high temperature, with edge dominance emerging at moderate temperatures [C36]. For MoNbTaW at 296 K they predict an activation volume of 36b³. They note this is in the range of screw-controlled BCC alloys, but say the edge model still agrees well at low temperature [C37]. At high temperature, screw strength depends on jog pinning, which thermal vacancies defeat [C38].
  - Lee et al. observed mostly edge dislocations after room-temperature deformation of NbTaTiV (58 of 77) and CrMoNbV (23 of 41). For MoNbTaW and MoNbTaVW they cite only a prediction of edge control, not an observation [C39].
  - **Tsuru et al. (2024)** studied equiatomic VNbMoTaW deformed at room temperature [C40]:
    - the specimens were annealed at about 2000 °C for 48 h, had a 496 µm grain size and were tested at 1 × 10⁻⁴ s⁻¹;
    - screw and edge segments were present almost equally;
    - a screw model gave 1242 MPa and an edge model (Rao et al.'s formulation, not the reduced Maresca-Curtin model) gave 1210 MPa, both about 25-30 % below the measured yield strength;
    - the authors conclude that kink migration, a screw mechanism, controls the rate at room temperature.
  - In room-temperature NbMoTaW micropillars, edge dislocations were seen in several grains, and the authors link the governing mechanism to Peierls-type activation of edge or screw dislocations [C41].
  - Yin et al. suggest that underprediction of V-free alloys may reflect a change from edge control (with V) to screw control (without V) [C42].
  - No checked source states what this means quantitatively for room-temperature predictions from the edge model (claims.md Q4 status).

**How it compares with our results.**
- The project does not report Maresca-Curtin predictions for MoNbTaW or WMoTaNbV at 1000-1600 °C (strength_model.md). A direct comparison with the measured values [C34] is therefore not possible from the project files.
- The project's high-temperature numbers are for the finalists only. At 1000 °C they are R5-1 573, R5-2 533, R5-13 517, T6 491 and R5-4 428 MPa. At 1300 °C they are 445, 411, 397, 374 and 315 MPa. The report treats them as a ranking, not as design numbers (strength_model.md). That framing fits the reported underprediction and the missed plateau [C32, C43].
- These high-temperature values come from the exponential branch, where the v3 form and the single 0.91 form differ (strength_model.py; [C5, C15]). They are as exposed to the D1 question as the room-temperature values.
- The project's caveat says edge glide controls strength at moderate to high temperature and that screw dislocations "may also contribute" at room temperature (strength_model.md). The literature says more than that:
  - in annealed VNbMoTaW, edge and screw models give similar strengths and screw-type kink migration controls the rate [C40];
  - edge control of MoNbTaW and MoNbTaVW is a prediction, not an observation [C39];
  - V-free alloys may be screw-controlled [C42].
  The 922 MPa prediction for MoNbTaW, the only V-free validation alloy, is below measurement (strength_model.md). That direction is consistent with Yin et al.'s suggestion, but no checked source tests it for this alloy [C42].
- Tsuru et al.'s specimens (annealed, coarse-grained, 1 × 10⁻⁴ s⁻¹) [C40] differ from the project's as-cast validation data (strength_model.md), so their 25-30 % gap does not transfer directly to our numbers.

**What it means for the next step.**
- Run the model for MoNbTaW and WMoTaNbV at 1000, 1200, 1400 and 1600 °C and set the results against [C34]. Do this after D1 is resolved, because the high-temperature branch depends on it.
- Rewrite the edge-only caveat as in Corrections 4. Agreement of the edge model with a room-temperature measurement does not establish edge control [C40].

## Corrections to the project

Line numbers refer to the files as read on 2026-11-13. No file other than this one was edited. Where `reports/strength_model.md` is generated, the same text must be changed in `pipeline/strength_model.py` `report()`.

| # | File (location) | Current wording | Corrected wording | Support |
|---|---|---|---|---|
| 1 | `pipeline/strength_model.py` `ELASTIC`, Ta (l. 43); comment (l. 36-38); docstring (l. 19) | `"Ta": (266.0, 158.0, 87.4)` under "Room-temperature ... single-crystal elastic constants"; "Inputs here are elemental room-temperature values" | Either replace with a room-temperature set (Featherston & Neighbours 300 K 260.9/157.4/81.8 GPa, or Bolef 27 °C 267/161/82.5 GPa) and rerun, or keep and label: "Ta: Featherston & Neighbours (1963) 0 K values, not room temperature." The docstring should then say "room-temperature values except Ta Cij (0 K)" or drop the exception after replacement. Rerun effect on 922/1411/1425/1317 MPa not computed | C22, C24; factcheck D5 and side-by-side |
| 2 | `pipeline/strength_model.py` comment (l. 36-38); `reports/strength_model.md` Caveats (l. 41) and generator (l. 220-221) | "Standard handbook values; not yet checked against a primary source in this repo." / "Elemental inputs are handbook values not yet checked against primary sources." | Give a source per element: "W Cij = Featherston & Neighbours 300 K; Mo close to Katahara et al. 300 K (via Gong & Dal Corso); Nb, V close to Bolef 27 °C (Nb C12 uncertain, 13-13.9 ×10¹¹ dyn cm⁻²); Ta = F&N 0 K (see #1). Lattice parameters: W, Mo, V within 0.0004 Å of 25 °C X-ray values; Ta 3.3029 vs 3.3058 Å (NBS, 25 °C) and Nb 3.3004 vs 3.3063 Å (temperature not stated) unmatched." | C20, C24, C25, C26, C27, C28; factcheck side-by-side |
| 3 | `reports/strength_model.md` §1 "Sensitivity to the regime switch" (l. 20); `pipeline/strength_model.py` docstring (l. 11-12), `yield_strength` docstring (l. 112-114), generator (l. 182-189); `tests/test_strength_model.py` (l. 31) | "where the paper switches between its low- and high-temperature forms ... The tables use the paper's rule." / "uses the paper's rule" / "The paper's rule has a known ~5 % upward step" | "arXiv v3 (Eqs. 11-12) uses two forms with a switch at τ/τ0 = 0.5, and the tables use that rule. Later papers by the same group attribute to the published Acta paper a single form, τy0·exp{-(1/0.55)[(kT/ΔEb) ln(ε̇0/ε̇)]^0.91} (bracket placement of 1/0.55 uncertain). Which law the published paper uses is unresolved. **The four validation predictions under the single form have not been computed.** The 'continuous' variant above is not that form." Add "(arXiv v3)" to the test comment | C5, C15, C17, C18; factcheck D1 |
| 4 | `reports/strength_model.md` Caveats (l. 39); generator (l. 214-215); `pipeline/strength_model.py` docstring (l. 20-21); `README.md` Limitations (l. 131-135) | "Edge dislocations only. The paper finds edge glide controls strength at moderate to high temperature; at room temperature screw dislocations may also contribute." | "Edge dislocations only. Maresca & Curtin argue edge glide can control strength from moderate to high temperature and agrees with room-temperature data, but edge control of MoNbTaW and MoNbTaVW is predicted, not observed. In annealed VNbMoTaW at room temperature, Tsuru et al. (2024) found edge and screw segments present almost equally, similar edge (1210 MPa) and screw (1242 MPa) model strengths, both 25-30 % below measurement, and screw kink migration as rate-controlling. Room-temperature agreement of this edge model therefore does not show that edge glide controls strength." Add one sentence to the README limitation | C36, C37, C39, C40, C42 |
| 5 | `reports/strength_model.md` Caveats (l. 41); generator (l. 219-220); `tests/test_strength_model.py` comment (l. 19-20) | "Rule-of-mixtures elastic constants ignore alloying effects (DFT gives a much lower C44 for equiatomic MoNbTaVW)." / "rule-of-mixtures C44 is stiffer than DFT" | "Rule-of-mixtures elastic constants ignore alloying effects. For equiatomic MoNbTaVW, DFT gives C44 = 51 GPa against 90.5 GPa from ROM (Maresca & Curtin Table 2, arXiv v3), but the authors note that DFT is known to underestimate C44 in BCC metals and consider the EAM value more reliable." Test comment: "ROM C44 is higher than the DFT value, which the authors regard as too low." | P2, C9 |
| 6 | `reports/strength_model.md` §2 Reading (l. 34); generator (l. 206-207). The P4 sentence is **not in `README.md`** (factcheck P4); the closest wording is in `docs/research/run-2026-11-11/notes.md` (l. 9, l. 63), which this run does not edit | "R5-4 has the most V (the strongest misfit solute)" / "V has the largest misfit volume of the five elements" | "In the W-Mo-Ta-Nb-V alloys studied (equiatomic and near-equiatomic, and our finalists), V has the largest-magnitude misfit volume (Maresca & Curtin, Table 2), because it is the smallest atom." A misfit volume is relative to the alloy average, not a fixed property of the element. In strongly V-rich alloys Nb or Ta would overtake it (fact-checker arithmetic, no source) | P4, C9 |
| 7 | `reports/strength_model.md` (l. 3); `pipeline/strength_model.py` docstring (l. 5) and generator (l. 163-164) | "Maresca & Curtin, *Acta Mater.* 182 (2020) 235–249" (no title) | Add the published title: F. Maresca, W.A. Curtin, "Mechanistic origin of high strength in refractory BCC high entropy alloys up to 1900K", Acta Mater. 182 (2020) 235-249, doi:10.1016/j.actamat.2019.10.015. Do not use the current arXiv abstract-page title ("...high retained strength..."). Note that the equations were checked against arXiv:1901.02100v3 | factcheck D8 |
| 8 | `tests/test_strength_model.py` (l. 10) | "Maresca & Curtin (2020) Table 2, DFT misfit volumes" | "Maresca & Curtin, arXiv:1901.02100v3 Table 2, DFT row (published version not checked)". The numbers themselves are correct | C9, P2 |
| 9 | `README.md` (l. 16-17, l. 95-96); `reports/strength_model.md` (l. 3) | "a physics-based model with no fitted parameters" / "with nothing fitted" / "Nothing is fitted to alloy data." | "nothing fitted to measured data (the reduced model's prefactors were fitted to the full theory; Maresca & Curtin report about 10 % scatter)" | C8, C17 |
| 10 | `reports/strength_model.md` Caveats (l. 38); generator (l. 212-213) | "NbTaVW's 1530 MPa is not yet verified against its primary source." | "NbTaVW's 1530 MPa is listed in compression by an open secondary compilation (Gorsse et al. 2018), which gives no processing state or strain rate and does not mark whether it is σy. The primary (Yao et al. 2016) has not been read. Our validation compositions are equiatomic; the experimental NbTaVW and MoNbTaV were not." | C10, C30, C31; factcheck D9 |

**Checked and not a correction.**
- Prefactors 0.040 and 2.00, α = 1/12, ε̇0 = 10⁴ s⁻¹ and M = 3.067 all match the preprint [C1, C2, C3, C4]. The 3.06 in later papers is rounding (factcheck D3).
- `B = (c11 + 2c12)/3` in `elastic_averages` is correct even though the preprint prints no 1/3. The group's own μ and ν values require it [C6, C11; factcheck D4].
- The DFT misfit volumes, a and C44 quoted in the test and the brief match MC-v3 Table 2 to the digit [C9, P2]. The test compares against the DFT row, so the internal inconsistencies in the preprint's Vegard rows do not affect it (factcheck D7).
- P1: the report's statement that predictions fall below experiment at high temperature and miss the 900-1300 K plateau is supported [C32, P1]. One optional addition: the same paragraph says edge strengthening agrees fairly well with the measured high-temperature behaviour [C32]. If the published version changed the temperature law, its Fig. 1 may differ (factcheck P1).
- P3: the test's 2.2-2.5 eV range for MoNbTaW / MoNbTaVW is supported [C44, P3]. The preprint does not say which inputs produced those barriers, so the comparison with rule-of-mixtures barriers is approximate. The test's wide 2.0-3.2 eV band already allows for that (factcheck P3).
- W elastic constants, and the W, Mo and V lattice parameters, match room-temperature measurements [C20, C26, C27]. Our V lattice parameter is closer to the 25 °C X-ray value than the Curtin group's [C27; factcheck D6].

## Open leads

None of these are findings.
- The published Acta Mater. 182 (2020) 235-249 article: the temperature law, Fig. 1 and Fig. 5 (factcheck Needs Sean item 1).
- Yao et al. MSEA 674 (2016) accepted manuscript at https://www.osti.gov/servlets/purl/1482331. It blocked automated fetching, and whether it holds the full text is not confirmed (factcheck).
- Winkens et al., Commun. Mater. 4, 26 (2023), Curtin co-author. The fact-checker reports α = 1/8 and the 0.91 form credited to the Acta paper, with 1/0.55 outside the bracket. Not a reviewer claim (factcheck D1, D2).
- arXiv:2502.11369 and Wang et al., Mater. Des. 261 (2026) 115368. Both use the 0.91 form and cite the Acta paper (factcheck D1); neither is a reviewer claim.
- arXiv:1901.02100 v1 and v2, not checked (factcheck).
- Maresca & Curtin, screw-dislocation theory, Acta Mater. 182 (2020) 144 (records only); the Materials Cloud dataset materialscloud:2021.65 (predicted strengths at 1300 K); arXiv:2511.16057 (title only) (claims.md).
- Tsuru et al. 2024 Methods and Supplementary Information, for the edge-model constants and the measured value (claims.md C40).
- Kubilay et al. Fig. 7b and Maresca & Curtin Fig. 1 predicted values, which are in the figures only [C33, C35].
- Couzinié et al., Data in Brief 21 (2018) 1622-1641; Simmons & Wang (1971) handbook (claims.md).
- An unreferenced web page listing NbTaVW at 1530 MPa cast was seen by the reviewer and deliberately not recorded as a claim (claims.md Q3 status).

## Open questions

- **D1, the most important.** Which temperature law does the published paper use? What are the four validation predictions (and the finalist values) under the single 0.91 form, for both bracket placements? Neither the project nor any source gives these numbers.
- What does the preprint's statement that room-temperature predictions are rather sensitive to α, while 296-1900 K predictions are quite insensitive, mean in MPa? The two statements overlap at 296 K, and the size of the effect is shown only in a figure [C2].
- Why do our MoNbTaW and quinary predictions (922 and 1411 MPa) differ from Yin et al.'s (954 and 1347 MPa) [C12] (strength_model.md)? Candidate causes are the 0 K elemental inputs, the V volume, M = 3.06 and the 2/3-power-only form. None has been tested.
- How much would the predictions change at the measured, non-equiatomic compositions of the experimental NbTaVW and MoNbTaV [C10]?
- What strain rate applies to each of the four measurements, and is 1530 MPa a yield strength or a maximum stress [C3, C30]?
- Where do the Curtin group's Nb and V elastic constants and its V volume come from (factcheck D5, D6)? What is the exact Bolef Nb C12 [C24]? What is Nb's lattice parameter at 293-300 K [C28]?
- Do MoNbTaW, NbTaVW and MoNbTaV deform by edge or screw control at room temperature in the as-cast state? No checked source observed this for these alloys [C39, C40, C42].
- MC-v3 Table 2 has internal inconsistencies in its quinary Vegard row and the NbTaVW W misfit. Were these corrected in the published version (factcheck D7)? No project number depends on them.

## References

- Maresca, F., Curtin, W.A. Mechanistic origin of high strength in refractory BCC high entropy alloys up to 1900K. Acta Mater. 182 (2020) 235-249, doi:10.1016/j.actamat.2019.10.015 (published version not opened); read as arXiv:1901.02100v3, https://arxiv.org/pdf/1901.02100 and https://ar5iv.labs.arxiv.org/html/1901.02100 [C1-C10, C32, C33, C36, C37, C38, C44, P1-P4]
- Yin, B., Maresca, F., Curtin, W.A. Vanadium is an optimal element for strengthening in both fcc and bcc high-entropy alloys. Acta Mater. 188 (2020) 486-491. doi:10.1016/j.actamat.2020.01.062 ; https://research.rug.nl/files/136414836/1_s2.0_S1359645420300884_main.pdf [C11, C12, C13, C42]
- Kubilay, R.E., Ghafarollahi, A., Maresca, F., Curtin, W.A. High energy barriers for edge dislocation motion in body-centered cubic high entropy alloys. npj Comput. Mater. 7, 112 (2021). doi:10.1038/s41524-021-00577-7 ; https://infoscience.epfl.ch/record/287520/files/s41524-021-00577-7.pdf [C14, C15, C35]
- Lee, C., Maresca, F., Feng, R., et al. Strength can be controlled by edge dislocations in refractory high-entropy alloys. Nat. Commun. 12, 5474 (2021). doi:10.1038/s41467-021-25807-w ; https://par.nsf.gov/servlets/purl/10343625 [C17, C39]
- Baruffi, C., Maresca, F., Curtin, W.A. Screw vs. edge dislocation strengthening in body-centered-cubic high entropy alloys and implications for guided alloy design. MRS Commun. 12 (2022) 1111-1118. doi:10.1557/s43579-022-00278-2 ; https://pure.rug.nl/ws/files/274719702/s43579_022_00278_2.pdf [C18, C29, C43]
- Xiao, B., Lysogorskiy, Y., Savan, A., et al. Correlations of composition, structure, and hardness in the high-entropy alloy system Nb-Mo-Ta-W. High Entropy Alloys & Materials 1 (2023) 110-119. doi:10.1007/s44210-022-00007-3 [C19]
- Featherston, F.H., Neighbours, J.R. Elastic constants of tantalum, tungsten, and molybdenum. Phys. Rev. 130 (1963) 1324. https://core.ac.uk/download/81223136.pdf [C20, C21, C22]
- Bolef, D.I. Elastic constants of single crystals of the bcc transition elements V, Nb, and Ta. J. Appl. Phys. 32 (1961) 100 (abstract only). https://www.osti.gov/biblio/4110197-elastic-constants-single-crystals-bcc-transition-elements-nb-ta [C24]
- Gong, X., Dal Corso, A. Ab initio quasi-harmonic thermoelasticity of molybdenum at high temperature and pressure. arXiv:2406.16634v1 (2024). https://arxiv.org/html/2406.16634v1 [C25]
- Swanson, H.E., Tatge, E. Standard X-ray diffraction powder patterns, Vol. I. NBS Circular 539 (1953). https://nvlpubs.nist.gov/nistpubs/Legacy/circ/nbscircular539v1.pdf [C26]
- American Mineralogist Crystal Structure Database, vanadium entries. https://rruff.info/AMS/minerals/Vanadium [C27]
- Crystallography Open Database entry 1539041 (Nb; Roberge, J. Less-Common Met. 40 (1975) 161-164). https://www.crystallography.net/cod/1539041.html [C28]
- Gorsse, S., Nguyen, M.H., Senkov, O.N., Miracle, D.B. Database on the mechanical properties of high entropy alloys and complex concentrated alloys. Data in Brief 21 (2018) 2664-2678. doi:10.1016/j.dib.2018.11.111 [C30, C34]
- Yao, H.W., Qiao, J.W., Gao, M.C., Hawk, J.A., Ma, S.G., Zhou, H.F., Zhang, Y. NbTaV-(Ti,W) refractory high-entropy alloys: experiments and modeling. Mater. Sci. Eng. A 674 (2016) 203-211. doi:10.1016/j.msea.2016.07.102 (abstract only) [C31]
- Tsuru, T., Han, S., Matsuura, S., et al. Intrinsic factors responsible for brittle versus ductile nature of refractory high-entropy alloys. Nat. Commun. 15, 1706 (2024). doi:10.1038/s41467-024-45639-8 [C40]
- Pozuelo, M., Marian, J. Microscale deformation controlled by compositional fluctuations in equiatomic Nb-Mo-Ta-W alloys. Mater. Sci. Eng. A 856 (2022) 143892. doi:10.1016/j.msea.2022.143892 ; https://par.nsf.gov/servlets/purl/10362786 [C41]

## Needs Sean (university access)

As left by the fact-checker (`factcheck.md`), unchanged except for one phrase in item 1 weakened by the integrity audit (`audit.md`). Items 1 and 2 are affected by `sean-sources.md` and a session computation; see `audit.md`, "Superseded by sean-sources.md".

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
   sources attribute both laws to this paper (D1), and the report places the regime switch at
   the alloys' room-temperature operating point (`reports/strength_model.md`).
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
