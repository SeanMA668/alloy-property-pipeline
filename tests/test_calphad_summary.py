"""Parsing of Thermo-Calc exports: solidus, liquidus, split temperature, incomplete sweeps."""
import numpy as np
import pandas as pd
import pytest

from pipeline import paths as P
from pipeline.calphad_summary import summarise

T = "Temperature [°C]"


def write(tmp_path, rows, cols):
    df = pd.DataFrame(rows, columns=[T] + [f"Amount of {c} [mol]" for c in cols])
    f = tmp_path / "sweep.csv"
    df.to_csv(f, sep="\t", index=False, na_rep="")
    return f


def test_single_phase(tmp_path):
    rows = [[t, 1.0, np.nan] for t in range(500, 2600, 100)]
    rows += [[2600.0, 1.0, 0.0], [2650.0, 0.5, 0.5], [2700.0, 0.0, 1.0], [2800.0, np.nan, 1.0]]
    s = summarise(write(tmp_path, rows, ["BCC_B2", "LIQUID"]))
    assert s["solidus"] == 2600.0
    assert s["liquidus"] == 2700.0
    assert s["complete"] and s["extra"] == {}


def test_split_detected_at_boundary_row(tmp_path):
    rows = [[500.0, 0.7, 0.3, np.nan], [600.0, 0.9, 0.1, np.nan], [612.5, 1.0, 0.0, np.nan],
            [700.0, 1.0, np.nan, np.nan], [2500.0, 1.0, np.nan, 0.0], [2600.0, np.nan, np.nan, 1.0]]
    s = summarise(write(tmp_path, rows, ["BCC_B2", "BCC_B2#2", "LIQUID"]))
    t_split, minority = s["extra"]["second BCC (A2)"]
    assert t_split == 612.5
    assert minority == pytest.approx(0.3)


def test_split_found_when_labels_swap(tmp_path):
    """Thermo-Calc may call the single high-T phase BCC_B2#2; counting phases must still work."""
    rows = [[500.0, 0.4, 0.6, np.nan], [650.0, 0.0, 1.0, np.nan], [700.0, np.nan, 1.0, np.nan],
            [2500.0, np.nan, 1.0, 0.0], [2600.0, np.nan, np.nan, 1.0]]
    s = summarise(write(tmp_path, rows, ["BCC_B2", "BCC_B2#2", "LIQUID"]))
    assert s["extra"]["second BCC (A2)"][0] == 650.0
    assert s["solidus"] == 2500.0


def test_incomplete_sweep_flagged(tmp_path):
    rows = [[500.0, np.nan, np.nan], [800.0, 1.0, np.nan], [2500.0, 1.0, 0.0], [2600.0, np.nan, 1.0]]
    s = summarise(write(tmp_path, rows, ["BCC_B2", "LIQUID"]))
    assert not s["complete"]


@pytest.mark.parametrize("alloy, solidus, split", [
    ("R4-1", 2677.75225, None),          # single-phase
    ("R3-1", 2342.07369, 839.86398),     # splits
    ("R4-5", 2496.38002, 667.95163),     # brief third BCC label near the split
])
def test_real_exports(alloy, solidus, split):
    s = summarise(P.CALPHAD / f"hea_{alloy}.csv")
    assert s["solidus"] == pytest.approx(solidus)
    got = s["extra"].get("second BCC (A2)", (None,))[0]
    assert got == (pytest.approx(split) if split else None)
