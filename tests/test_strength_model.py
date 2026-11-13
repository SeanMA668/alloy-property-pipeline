import numpy as np
import pytest

from pipeline import strength_model as S

EQUI5 = {e: 20 for e in S.ELEMENTS}


def test_misfit_volumes_close_to_paper_dft():
    # Maresca & Curtin (2020) Table 2, DFT misfit volumes (A^3) for equiatomic MoNbTaVW.
    dft = {"Mo": -0.824, "Nb": 1.848, "Ta": 1.882, "V": -2.380, "W": -0.526}
    V = S.atomic_volumes()
    vegard = dict(zip(S.ELEMENTS, V - V.mean()))
    for e, ref in dft.items():
        assert vegard[e] == pytest.approx(ref, abs=0.25)


def test_barrier_in_paper_range():
    # Paper reports barriers of 2.2-2.5 eV for MoNbTaW / MoNbTaVW; rule-of-mixtures C44 is
    # stiffer than DFT, so allow some margin above.
    for comp in (EQUI5, {"W": 25, "Mo": 25, "Ta": 25, "Nb": 25}):
        _, de = S.zero_temperature(comp)
        assert 2.0 < de < 3.2


def test_strength_falls_with_temperature_and_is_continuous():
    T = np.linspace(100, 2000, 200)
    s = np.array([S.yield_strength(EQUI5, t, switch="continuous") for t in T])
    assert np.all(np.diff(s) < 0)
    assert np.max(np.abs(np.diff(s))) < 40   # no jump at the low/high-T switch
    # The paper's rule has a known ~5 % upward step at tau/tau0 = 0.5, and nothing else.
    p = np.array([S.yield_strength(EQUI5, t) for t in T])
    assert np.sum(np.diff(p) > 0) == 1


def test_pure_element_has_no_misfit_strength():
    assert S.zero_temperature({"W": 100})[0] == pytest.approx(0.0, abs=1e-9)


def test_validation_beats_thermocalc():
    v = S.validation_table()
    assert v["mc_error"].abs().mean() < v["tc_error"].abs().mean()
