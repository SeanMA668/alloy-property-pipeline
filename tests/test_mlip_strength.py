import numpy as np
import pandas as pd

from pipeline import mlip_strength as M


def _synthetic(W=None, n=40, seed=0):
    rng = np.random.default_rng(seed)
    V = np.array([15.9, 15.6, 18.1, 18.0, 13.8])
    C = np.vstack([np.eye(5), rng.dirichlet(np.ones(5), n)])
    vol = C @ V
    if W is not None:
        vol = vol + sum(w * C[:, i] * C[:, j] for w, (i, j) in zip(W, M.PAIRS))
    d = pd.DataFrame(C, columns=M.ELS)
    d["name"] = M.ELS + [f"r{k}" for k in range(n)]
    d["volume_A3"] = vol
    return d, V


def test_vegard_data_gives_vegard_misfits():
    d, V = _synthetic()
    coef = M.fit(d)
    c = np.full(5, 0.2)
    assert np.allclose(M.apparent_misfits(coef, c), V - c @ V, atol=1e-8)
    # no non-Vegard part -> corrected misfits equal the experimental Vegard ones
    exp_v = M.S.atomic_volumes()
    assert np.allclose(M.corrected_misfits(coef, M.pure_volumes(d), c), exp_v - c @ exp_v, atol=1e-8)


def test_partial_volumes_sum_to_alloy_volume():
    d, _ = _synthetic(W=np.linspace(-1, 1, 10))
    coef = M.fit(d)
    c = np.array([0.3, 0.2, 0.2, 0.2, 0.1])
    assert abs(c @ M.apparent_misfits(coef, c)) < 1e-9   # misfits average to zero
