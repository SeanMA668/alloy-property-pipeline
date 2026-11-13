import json
import shutil
import subprocess

import pytest

from pipeline import paths as P

SITE = P.ROOT / "site"


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
def test_browser_models_match_python():
    """The dashboard's JavaScript must reproduce the Python surrogate, strength and density."""
    js = f"""
    const m = require({json.dumps(str(SITE / 'model.js'))});
    const d = require({json.dumps(str(SITE / 'data.json'))});
    m.setData(d);
    console.log(JSON.stringify(d.check.map(f => {{ const r = m.predict(f);
      return [r.sol.mu - f.solidus, r.ys25 - f.ys25, r.rho - f.density]; }})));
    """
    out = json.loads(subprocess.check_output(["node", "-e", js], text=True))
    for d_sol, d_ys, d_rho in out:
        assert abs(d_sol) < 0.5 and abs(d_ys) < 0.5 and abs(d_rho) < 1e-3


def test_data_file_is_current():
    d = json.loads((SITE / "data.json").read_text())
    assert len(d["alloys"]) == 50 and len(d["X"]) == 50
