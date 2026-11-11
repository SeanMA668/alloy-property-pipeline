"""Composition perturbation, sensitivity signs, and the cost / supply-risk calculation."""
import numpy as np
import pandas as pd
import pytest

from pipeline import cost_supply as cs
from pipeline import sensitivity as sens

ELS = sens.ELS


def test_perturb_adds_one_percent_and_keeps_ratios():
    X = np.array([[0.20, 0.20, 0.20, 0.20, 0.20], [0.35, 0.214, 0.288, 0.084, 0.064]])
    for j in range(5):
        Z = sens.perturb(X, j)
        assert np.allclose(Z.sum(axis=1), 1)
        assert np.allclose(Z[:, j] - X[:, j], 0.01)
        others = [k for k in range(5) if k != j]
        ratio = lambda A: A[:, others] / A[:, others].sum(axis=1, keepdims=True)
        assert np.allclose(ratio(Z), ratio(X))


def test_ols_recovers_a_known_linear_mixture():
    # y = sum b_k x_k exactly; the +1 at.% change is then b_j - weighted mean of the others
    rng = np.random.default_rng(0)
    X = rng.dirichlet(np.ones(5), size=40)
    b = np.array([3400.0, 2600.0, 3000.0, 2500.0, 1900.0])
    got = sens.ols_sensitivity(X, X @ b)
    for j, e in enumerate(ELS):
        expect = ((sens.perturb(X, j) - X) @ b).mean()
        assert got[e] == pytest.approx(expect, abs=1e-6)


@pytest.fixture(scope="module")
def result():
    return sens.run()


def test_solidus_signs_follow_melting_points(result):
    # Guards against a sign error in the perturbation (W melts highest, V lowest).
    s = result["solidus"].set_index("element")["mean"]
    assert s["W"] > 0 and s["Ta"] > 0 and s["V"] < 0
    assert s["W"] > s["V"]


def test_split_sensitivity_uses_only_alloys_above_the_floor(result):
    assert result["n_split"] + result["n_single"] == 50
    assert result["split_range"][0] > sens.FLOOR_C


def test_pure_element_costs_its_own_price():
    for e in ELS:
        row = pd.DataFrame([{k: (100.0 if k == e else 0.0) for k in ELS}])
        assert cs.alloy_metrics(row)["cost_2025"].iloc[0] == pytest.approx(cs.PRICE_2025[e][0])
        assert cs.alloy_metrics(row)["sr_eu"].iloc[0] == pytest.approx(cs.SUPPLY[e][0])


def test_price_conversions():
    assert cs.PRICE_2025["W"][0] == pytest.approx(380 / 7.93)
    assert cs.TA_IN_TA2O5 == pytest.approx(0.819, abs=1e-3)
    assert cs.V_IN_V2O5 == pytest.approx(0.560, abs=1e-3)


def test_pareto_mask():
    df = pd.DataFrame({"a": [3, 2, 1, 3], "b": [1, 1, 0, 2]})   # maximise a, minimise b
    assert list(cs.pareto(df, ["a"], ["b"])) == [True, False, True, False]
