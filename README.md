# Refractory high-entropy alloy discovery: ML + Thermo-Calc active learning

[![tests](https://github.com/SeanMA668/hea-alloy-property-pipeline/actions/workflows/tests.yml/badge.svg)](https://github.com/SeanMA668/hea-alloy-property-pipeline/actions/workflows/tests.yml)

A Python pipeline that searches the W-Mo-Ta-Nb-V alloy family for compositions that stay
**single-phase BCC** from 500 °C to melting. A machine-learning screen picks candidates,
Thermo-Calc (TCHEA6 v6.1) calculates them, and a Gaussian-process surrogate trained on
those results chooses the next batch.

**Result:** over five rounds, **50 alloys** were calculated and **28** were single-phase
BCC up to the solidus, the highest melting at **2822 °C**. Fitted only on earlier
rounds, the surrogate predicted each new round's solidus to within **8–28 °C** on
average, where guessing the average would miss by 148–241 °C. Thermo-Calc's phase
predictions agree with all four alloys in this family that have experimentally reported
phases, and the finalists are predicted to segregate less on casting than earlier
candidates.

![Solidus vs density for the 50 calculated alloys](reports/figures/melting_vs_density.png)

## How it works

```mermaid
flowchart LR
    A[Materials Project + pymatgen<br/>elemental data] --> B[Features<br/>δ, ΔHmix, VEC, ΔSmix, Tm]
    C[MPEA dataset<br/>1,545 experimental entries] --> D[Random Forest<br/>P single-phase BCC]
    B --> D
    D --> E[Candidate<br/>compositions]
    E --> F[Thermo-Calc TCHEA6<br/>500–3000 °C sweeps]
    F --> G[Gaussian-process surrogate<br/>solidus + split temperature]
    G --> H[Next batch: best trade-offs<br/>melting point · density · strength]
    H --> F
```

1. **Screen** (`pipeline/hea_model.py`): computes atomic-size mismatch δ, mixing
   enthalpy ΔHmix (Miedema pair values, checked against matminer), VEC, ΔSmix and Tm for
   10,000 random compositions, and trains a Random Forest on the MPEA experimental dataset
   (Borg et al., *Sci. Data* 2020) to estimate P(single-phase BCC).
2. **Calculate** (done by hand in Thermo-Calc Graphical Mode): equilibrium phase amounts
   from 500 to 3000 °C for each proposed composition, exported to `data/calphad/`.
3. **Learn and propose** (`pipeline/active_learning.py`, `pipeline/study_design.py`):
   Gaussian processes on composition predict the solidus and the temperature where the
   alloy splits into two BCC phases. Their uncertainty is calibrated by leave-one-out.
   The next batch spreads along the trade-off between melting point, density and
   predicted strength, plus a few "explore" points where the model is least sure.
4. **Report** (`pipeline/study_results.py`, `pipeline/figures.py`): writes
   [`reports/study_results.md`](reports/study_results.md) and the figures here.

## What the loop achieved

![Prospective prediction error per round](reports/figures/prediction_by_round.png)

Each bar is a genuine forecast: the model saw only earlier rounds. The error does not
fall steadily, because later rounds deliberately probed new regions; what holds is that
it stays roughly 3–20× smaller than the no-model baseline.

| | Solidus (°C) | Density (g/cm³) | Raw material, 2025 ($/kg) | Scheil freezing range (°C) | Composition (at.%) |
|---|---:|---:|---:|---:|---|
| Highest melting (R5-1) | 2822 | 14.93 | 108 | 672 | W35.0 Mo21.4 Ta28.8 Nb8.4 V6.4 |
| Balanced (R5-13) | 2707 | 13.12 | 71 | 623 | W31.9 Mo29.3 Ta10.0 Nb22.9 V5.9 |
| Lightest above 2450 °C (R5-4) | 2499 | 11.85 | 108 | 732 | W11.3 Mo17.2 Ta24.4 Nb35.0 V12.1 |
| Cheapest (T6) | 2688 | 12.70 | 60 | 600 | W32.2 Mo26.9 Ta5.5 Nb30.2 V5.2 |

A smaller Scheil range means less segregation in a casting. Full list:
[`reports/study_results.md`](reports/study_results.md); validation, solidification and
strength checks: [`reports/finalists.md`](reports/finalists.md).

## How they compare with existing high-temperature metals

![Melting point vs density, with EduPack reference materials](reports/figures/ashby_melting_density.png)

Against Ansys Granta EduPack data for pure refractory metals, refractory alloys (TZM,
C-103, Ta-10W) and Ni superalloys, four of the five candidates are calculated to sit in a
gap: hotter than Mo alloys (about 2615 °C) and lighter than Ta alloys (16.5–16.9 g/cm³).
Their calculated solidus is 1160–1560 °C above Inconel 718's melting range, at 1.4–1.8×
its density. The lightest finalist, R5-4, is beaten by Mo and TZM on these two axes alone.
Details and caveats: [`reports/ashby.md`](reports/ashby.md).

## Findings worth knowing

- **Thermo-Calc agrees with experiments on phases.** All four W-Mo-Ta-Nb-V alloys with
  reported phases (MoNbTaW, NbTaVW, MoNbTaV, WMoTaNbV) are single-phase BCC in experiments,
  and TCHEA6 predicts single-phase BCC for all of them at casting and annealing
  temperatures. It predicts a split into two BCC phases below 664–791 °C for the two
  V-and-Mo alloys, which those experiments could not have seen. Four equiatomic alloys
  cannot show whether it predicts a *failure* correctly.
- **The finalists should segregate less.** Under Scheil (no diffusion in the solid) they
  freeze over 600–732 °C, against 785–844 °C for earlier candidates and equiatomic
  WMoTaNbV. Only liquid and BCC form.
- **Thermo-Calc's strength model fails validation.** Against the four measured
  room-temperature yield strengths, its ranking is wrong (Spearman ρ = −0.20): NbTaVW is
  predicted at 787 MPa against 1530 MPa measured (that measured value is not yet verified
  against its primary paper), and the others are 209–445 MPa too high.
  The finalists' predicted values span only 163 MPa, so the model cannot rank them.

- **The cross-family ML classifier ties the textbook rules.** Under cross-validation
  grouped by chemical system, the Random Forest and the empirical δ/Ω/VEC rules both reach
  balanced accuracy 0.812 (AUC 0.89 for the forest). Within W-Mo-Ta-Nb-V its ranking
  agrees only weakly with Thermo-Calc (Spearman ρ = −0.37 against split temperature,
  n = 50). That is why the loop switched to a surrogate trained on Thermo-Calc itself.
- **The surrogate caught data-entry errors.** Two batches came back hundreds of degrees
  off prediction in one direction. Testing alternatives showed one batch was entered as
  mass % instead of mole %, and another was shifted one element over; both were confirmed
  and the runs kept at the compositions actually calculated (`data/rounds/`).
- **Composition pattern.** Single-phase alloys average 9.6 at.% V against 23.1 % for those
  that split, and contain more W and Ta. This is a pattern in these calculations, not a
  tested rule. The surrogate's slopes agree: +1 at.% V lowers the solidus by 18 °C and
  raises the split temperature by 9 °C ([`reports/sensitivity.md`](reports/sensitivity.md)).
  The phase diagram through the highest-melting alloy shows the same thing directly:
  with W as balance, it stays single-phase down to 500 °C only up to about 11 % V.

  <img src="data/calphad/hea_R5-1_isopleth.png" alt="Isopleth through R5-1, V 0-30 mol%" width="560">
- **Cost and supply risk.** At 2025 raw-material prices, Ta content explains 98 % of the
  cost spread between single-phase alloys; at the October 2026 tungsten price the
  low-W finalist becomes the cheapest. Every alloy in the family contains four
  EU-critical raw materials (W, Ta, Nb, V) ([`reports/cost_supply.md`](reports/cost_supply.md)).

## Limitations

- **Calculated, not measured.** Every result is a TCHEA6 calculation. The phase
  predictions agree with the four experimental alloys above, but none of the finalists
  has been made.
- **Strength is the weakest property.** The project's own model has a 202 MPa error on
  unseen alloy families, larger than the differences between candidates, so it only
  breaks ties; Thermo-Calc's model failed the validation above.
- **Cost** uses 2025 raw-material prices (ore, oxide, ferroalloy), not high-purity metal,
  and tungsten's price moved several-fold during 2026.
- **Density** is a rule-of-mixtures estimate (median error 0.3 % on 31 measured alloys).
- **Not assessed:** ductility, oxidation, creep, processing.
- **Selection bias:** 28 of 50 single-phase reflects targeted sampling, not how common
  single-phase alloys are in the system.

## Reproduce

```bash
git clone https://github.com/SeanMA668/hea-alloy-property-pipeline.git
cd hea-alloy-property-pipeline
pip install -r requirements.txt

export MP_API_KEY=...            # optional; adds Materials Project structures to the report
python -m pipeline.hea_model     # screen + classifier        -> reports/results.md
python -m pipeline.hea_properties # density + strength         -> reports/properties_results.md
python -m pipeline.calphad_vs_ml # collect Thermo-Calc runs    -> data/calphad/calphad_vs_ml.csv
python -m pipeline.study_results # study summary              -> reports/study_results.md
python -m pipeline.figures       # README figures             -> reports/figures/
python -m pipeline.sensitivity   # composition sensitivity    -> reports/sensitivity.md
python -m pipeline.cost_supply   # cost + supply risk         -> reports/cost_supply.md
python -m pipeline.finalists     # validation, Scheil, strength -> reports/finalists.md
python -m pipeline.ashby         # EduPack comparison chart -> reports/ashby.md
pytest                           # tests
```

To run another round: `python -m pipeline.study_design --batch 8` writes the next
compositions to `data/rounds/`. Calculate them in Thermo-Calc (mole %, W as balance,
500–3000 °C), save the tables as `data/calphad/hea_<ID>.csv`, then rerun the last three
commands. Thermo-Calc and the TCHEA6 database need their own licence.

## Repository layout

```
pipeline/   all code; run as python -m pipeline.<script>
data/       MPEA dataset, Thermo-Calc exports (data/calphad/), batch files (data/rounds/)
reports/    generated reports and figures
tests/      pytest suite (runs without Thermo-Calc or an API key)
docs/       literature notes, fact-checked by a multi-agent review (docs/research/)
```

## Credits

Built by [SeanMA668](https://github.com/SeanMA668). Code was written with an AI coding assistant (Claude);
the Thermo-Calc calculations, study design decisions and review are mine. Training data:
Borg et al., "Expanded dataset of mechanical properties and observed phases of
multi-principal element alloys", *Sci. Data* 7, 430 (2020), Apache-2.0
(`data/LICENSE-MPEA_dataset`).
