"""Repository locations used by every pipeline script."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MPEA = DATA / "MPEA_dataset.csv"        # Borg et al., Sci. Data 7, 430 (2020)
CALPHAD = DATA / "calphad"              # Thermo-Calc exports: hea_<ID>.csv / .png
ROUNDS = DATA / "rounds"                # compositions sent to Thermo-Calc, one file per round
COMPARISON = CALPHAD / "calphad_vs_ml.csv"
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"
