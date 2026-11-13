# Physics-based strength model (Maresca–Curtin)

Reduced analytic edge-dislocation model of Maresca & Curtin, *Acta Mater.* 182 (2020) 235–249 (doi:10.1016/j.actamat.2019.10.015). Inputs are elemental only: Vegard's-law atomic volumes from room-temperature lattice parameters and rule-of-mixtures elastic constants. Nothing is fitted to alloy data. Room temperature (296 K), strain rate 10⁻³ s⁻¹, Taylor factor 3.067. Code: `pipeline/strength_model.py`.

## 1. Validation against measured strengths

![Predicted vs measured](figures/strength_parity.png)

| Alloy | Measured (MPa) | Maresca–Curtin (MPa) | Error | Thermo-Calc (MPa) | Error |
|---|---:|---:|---:|---:|---:|
| WMoTaNbV | 1246 | 1411 | +165 | 1691 | +445 |
| MoNbTaW | 1058 | 922 | -136 | 1482 | +424 |
| NbTaVW | 1530 | 1425 | -105 | 787 | -743 |
| MoNbTaV | 1525 | 1317 | -208 | 1734 | +209 |

Spearman rank correlation with measured (n = 4): Maresca–Curtin ρ = 0.80, Thermo-Calc ρ = -0.20. Mean absolute error: Maresca–Curtin 153 MPa, Thermo-Calc 455 MPa.

With n = 4, ρ = 0.80 means one adjacent pair is swapped (WMoTaNbV and MoNbTaV); it is not statistically significant on its own. The clearer result is the error: every Maresca–Curtin prediction is within about 210 MPa, and NbTaVW, which Thermo-Calc misses by 743 MPa, comes out close.

**Sensitivity to the regime switch.** At room temperature these alloys sit near τ/τ₀ = 0.5, where the paper switches between its low- and high-temperature forms and the two differ by about 5 %. Switching where the forms cross instead (`switch="continuous"`) gives WMoTaNbV 1497, MoNbTaW 978, NbTaVW 1512, MoNbTaV 1396 MPa (mean absolute error 120 MPa, ρ = 0.80). The tables use the paper's rule.

Thermo-Calc values were rerun on 2026-11-13 (Advanced mode, 1000 °C anneal, solid-solution strengthening on) and reproduced the earlier Simplified/1400 °C values to within 1 MPa, so the NbTaVW result is not a settings error.

## 2. Finalists

| Alloy | V (at.%) | μ (GPa) | ΔE_b (eV) | 25 °C | 1000 °C | 1300 °C | Thermo-Calc 25 °C |
|---|---:|---:|---:|---:|---:|---:|---:|
| R5-1 | 6.4 | 111 | 3.00 | 1227 | 573 | 445 | 1556 |
| R5-2 | 5.7 | 109 | 2.91 | 1169 | 533 | 411 | 1636 |
| R5-13 | 5.9 | 109 | 2.87 | 1149 | 517 | 397 | 1691 |
| T6 | 5.2 | 105 | 2.80 | 1113 | 491 | 374 | 1649 |
| R5-4 | 12.1 | 78 | 2.49 | 1087 | 428 | 315 | 1528 |

**Reading.** At 25 °C the finalists span 140 MPa, less than the model's 153 MPa mean error on the validation alloys, so room-temperature strength still cannot separate them with confidence. The order is the same at every temperature: R5-1 is strongest and R5-4 weakest, 445 vs 315 MPa at 1300 °C. R5-4 has the most V (the strongest misfit solute) but the least W, and its lower shear modulus and energy barrier outweigh the extra misfit. The high-temperature values are not validated here: the paper's own predictions fall below experiment at high temperature, so treat them as a ranking, not as design numbers.

## Caveats

- Four validation alloys, all equiatomic and as-cast; NbTaVW's 1530 MPa is not yet verified against its primary source.
- Edge dislocations only. The paper finds edge glide controls strength at moderate to high temperature; at room temperature screw dislocations may also contribute.
- The paper reports its predictions fall below experiment at high temperature (the 900–1300 K plateau is not reproduced), so absolute high-temperature values are likely low; rankings are the intended use.
- Rule-of-mixtures elastic constants ignore alloying effects (DFT gives a much lower C44 for equiatomic MoNbTaVW). Elemental inputs are handbook values not yet checked against primary sources.
