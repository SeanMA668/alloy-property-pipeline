# Sources supplied by Sean (university / browser access)

## S1. Yao et al., NbTaV-(Ti, W) refractory high-entropy alloys

Accepted manuscript, OSTI 1482331 (https://www.osti.gov/servlets/purl/1482331), of
H.W. Yao, J.W. Qiao, M.C. Gao, J.A. Hawk, S.G. Ma, H.F. Zhou, Y. Zhang, "NbTaV-(Ti, W)
refractory high-entropy alloys: experiments and modeling", Mater. Sci. Eng. A 674 (2016),
doi:10.1016/j.msea.2016.07.102. PDF downloaded by Sean on 2026-11-13; text extracted with
pdftotext and read directly (full text, read-directly). The accepted manuscript may differ
in small ways from the published version.

- S1a. Section 2: alloys arc-melted from pure metals (≥ 99.9 wt.%), remelted at least seven
  times; compression specimens EDM-cut **from the cast ingots** (no heat treatment is
  described); cylinders 3 mm diameter × 6 mm height; MTS 809, room temperature, nominal
  strain rate **5 × 10⁻⁴ s⁻¹**.
- S1b. Section 3.4: σ0.2 is "the stress at ε = 0.2%", read from the **true** stress-strain
  curves at 298 K. NbTaVW plastic fracture strain 12 %.
- S1c. Table 2: NbTaVW σ0.2 = **1530 MPa** (experimental; 351 MPa estimated by rule of
  mixtures). Hv 4830 ± 29 MPa. Lattice parameter 3.2186 Å measured (3.2172 Å estimated).
- S1d. Table 3: NbTaVW bulk composition by EDX (Caver), at.%: **Nb 28.50, Ta 29.65,
  V 20.67, W 21.18**, not equiatomic. W enriches dendrite arms (K = 2.22), V the
  interdendritic regions (K = 0.52).

Project check (computed in this session with `pipeline/strength_model.py`, not from the
paper): Maresca–Curtin gives 1425 MPa at the nominal composition (296 K, 10⁻³ s⁻¹) and
1265 MPa at the EDX composition and the paper's 298 K, 5 × 10⁻⁴ s⁻¹.
