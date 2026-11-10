"""Composition unit conversions (used to diagnose Thermo-Calc entries made in the wrong unit)."""
from __future__ import annotations

import numpy as np


def atomic_masses(elements) -> np.ndarray:
    from pymatgen.core import Element
    return np.array([float(Element(e).atomic_mass) for e in elements])


def mass_to_mole(fractions, elements) -> np.ndarray:
    """Mass fractions (any scale) -> mole fractions summing to 1."""
    w = np.asarray(fractions, dtype=float) / atomic_masses(elements)
    return w / w.sum(axis=-1, keepdims=True)


def mole_to_mass(fractions, elements) -> np.ndarray:
    """Mole fractions (any scale) -> mass fractions summing to 1."""
    m = np.asarray(fractions, dtype=float) * atomic_masses(elements)
    return m / m.sum(axis=-1, keepdims=True)
