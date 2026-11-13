#!/usr/bin/env python3
"""
mlip_volumes.py - Alloy atomic volumes from a universal machine-learned interatomic potential.

Relaxes random BCC supercells (4x4x4 conventional = 128 atoms, one random configuration
each; volume and atom positions relaxed, cell kept cubic) with MACE-MPA-0 (medium) and
writes the atomic volume per composition to data/mlip/alloy_volumes.csv. Compositions: the
five pure elements, the four validation alloys, the five finalists, and random compositions
across W-Mo-Ta-Nb-V. `pipeline/strength_model.py` uses the table to test Vegard's law, which
the strength model relies on for misfit volumes.

Needs `pip install mace-torch` (not in requirements.txt; the table is committed so the rest
of the pipeline and the tests run without it). About 1 min per composition on 2 CPU cores.
Usage: python -m pipeline.mlip_volumes [--random 26] [--seed 0]
"""
from __future__ import annotations

import argparse
import csv
import time
import warnings

import numpy as np

from pipeline import paths as P

warnings.filterwarnings("ignore")
ELEMENTS = ["W", "Mo", "Ta", "Nb", "V"]
OUT = P.DATA / "mlip" / "alloy_volumes.csv"
MODEL = "medium-mpa-0"


def compositions(n_random: int, seed: int):
    from pipeline import strength_model as S
    rows = [(e, {e: 100.0}) for e in ELEMENTS]
    rows += [(a, c) for a, c, *_ in S.MEASURED]
    rows += list(S.finalist_compositions().items())
    rng = np.random.default_rng(seed)
    for i in range(n_random):
        f = rng.dirichlet(np.ones(5))
        if i % 3 == 0:                      # some quaternaries, like the validation alloys
            f[rng.integers(5)] = 0.0
            f /= f.sum()
        rows.append((f"rand{i:02d}", dict(zip(ELEMENTS, 100 * f))))
    return rows


def random_cell(comp: dict, n_rep: int, rng):
    from ase.build import bulk
    v_guess = {"W": 15.86, "Mo": 15.58, "Ta": 18.06, "Nb": 17.98, "V": 13.83}
    f = np.array([comp.get(e, 0.0) for e in ELEMENTS], float)
    f /= f.sum()
    a0 = (2 * f @ np.array([v_guess[e] for e in ELEMENTS])) ** (1 / 3)
    at = bulk("W", "bcc", a=a0, cubic=True).repeat((n_rep,) * 3)
    n = len(at)
    counts = np.floor(f * n).astype(int)
    for i in np.argsort(-(f * n - counts))[: n - counts.sum()]:
        counts[i] += 1
    syms = sum(([e] * c for e, c in zip(ELEMENTS, counts)), [])
    rng.shuffle(syms)
    at.set_chemical_symbols(syms)
    return at, counts


def relaxed_volume(at, calc) -> float:
    from ase.filters import FrechetCellFilter
    from ase.optimize import FIRE
    at.calc = calc
    FIRE(FrechetCellFilter(at, hydrostatic_strain=True), logfile=None).run(fmax=5e-3, steps=400)
    return at.get_volume() / len(at)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--random", type=int, default=26)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    from mace.calculators import mace_mp
    calc = mace_mp(model=MODEL, default_dtype="float32", device="cpu")
    done = set()
    if OUT.exists():
        with open(OUT) as fh:
            done = {r["name"] for r in csv.DictReader(fh)}
    rng = np.random.default_rng(args.seed + 1)
    new = not OUT.exists()
    with open(OUT, "a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["name", *ELEMENTS, "n_atoms", "volume_A3", "model"])
        for name, comp in compositions(args.random, args.seed):
            if name in done:
                continue
            n_rep = 1 if len([e for e in ELEMENTS if comp.get(e, 0) > 0]) == 1 else 4
            at, counts = random_cell(comp, n_rep, rng)
            t = time.time()
            v = relaxed_volume(at, calc)
            frac = 100 * counts / counts.sum()
            w.writerow([name, *[f"{x:.4f}" for x in frac], len(at), f"{v:.5f}", MODEL])
            fh.flush()
            print(f"{name:8s} V={v:.4f} A^3/atom  ({time.time() - t:.0f} s)", flush=True)


if __name__ == "__main__":
    main()
