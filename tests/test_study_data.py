"""Integrity of the Thermo-Calc study data and a regression guard on the surrogate."""
import numpy as np
import pandas as pd
import pytest

from pipeline import active_learning as al
from pipeline import paths as P

ELS = al.ELS


@pytest.fixture(scope="module")
def study():
    return pd.read_csv(P.COMPARISON)


def test_fifty_unique_alloys(study):
    assert len(study) == 50
    assert study["alloy"].is_unique


def test_compositions_sum_to_100(study):
    assert np.allclose(study[ELS].sum(axis=1), 100, atol=0.2)


def test_every_alloy_has_an_export(study):
    for a in study["alloy"]:
        stem = f"hea_{a.lstrip('#')}" + ("_" if a.startswith("#") else ".")
        assert any(p.name.startswith(stem) for p in P.CALPHAD.glob("hea_*.csv")), a


def test_temperatures_physical(study):
    assert (study["solidus_C"].between(2000, 3000)).all()
    assert (study["split_C"] >= 500).all() and (study["split_C"] < study["solidus_C"]).all()


def test_surrogate_leave_one_out(study):
    """GP must stay far better than guessing the mean (MAE 10 C vs 154 C when written)."""
    X = study[ELS].to_numpy() / 100
    cv = al.loo(X, study["solidus_C"].to_numpy(), 0)
    assert cv["mae"] < 25
    assert cv["mae"] < 0.25 * cv["mae_base"]
