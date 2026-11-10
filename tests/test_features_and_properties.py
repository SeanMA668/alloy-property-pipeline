"""Feature code, density and composition conversions against known values."""
import numpy as np
import pandas as pd
import pytest

from pipeline import hea_model as hm
from pipeline import paths as P
from pipeline.composition import mass_to_mole, mole_to_mass
from pipeline.hea_properties import density
from pipeline.study_design import pareto

ELS = ["W", "Mo", "Ta", "Nb", "V"]


def test_feature_self_check():
    """Miedema pair table matches matminer; dH_mix, VEC, dS_mix match published equiatomic values."""
    hm.self_check(hm.load_element_data())


def test_density_pure_tungsten():
    assert density(["W"], [1.0]) == pytest.approx(19.25, abs=0.01)


def test_density_equiatomic_wmotanbv():
    # rule-of-mixtures value reported in properties_results.md; measured 12.29 g/cm3
    assert density(ELS, [0.2] * 5) == pytest.approx(12.36, abs=0.01)


def test_mass_mole_round_trip():
    x = np.array([0.236, 0.140, 0.320, 0.155, 0.149])
    assert np.allclose(mass_to_mole(mole_to_mass(x, ELS), ELS), x / x.sum())


def test_mass_to_mole_reproduces_round2_diagnosis():
    """R2 values typed as mass % correspond to the compositions recorded as R2-*m."""
    planned = pd.read_csv(P.ROUNDS / "calphad_round2_points.csv").set_index("id")
    actual = pd.read_csv(P.ROUNDS / "calphad_extra_points.csv").set_index("id")
    for rid in planned.index:
        got = 100 * mass_to_mole(planned.loc[rid, ELS].to_numpy(float), ELS)
        assert np.allclose(got, actual.loc[rid + "m", ELS].to_numpy(float), atol=0.02), rid


def test_pareto():
    obj = np.array([[3, 1], [2, 2], [1, 3], [1, 1], [2, 1]])   # maximise both
    assert sorted(pareto(obj)) == [0, 1, 2]
