# Research pipeline (literature review with checks)

Four Claude Code agents, defined in `.claude/agents/`, run in order. Each is a separate
agent and never checks its own work.

| Stage | Agent | Reads | Writes |
|---|---|---|---|
| 1 | `literature-reviewer` | `brief.md` | `claims.md`: every claim with source, location and how it was read (read-directly / abstract-only / search-summary), plus a log of searches and blocked sources |
| 2 | `fact-checker` | `brief.md`, `claims.md` | `factcheck.md`: re-opens each source; SUPPORTED / PARTIAL / UNSUPPORTED / UNREACHABLE / LEAD-ONLY, plus checks of the project's own literature statements |
| 3 | `note-writer` | the above + project result files | `notes.md`: uses only SUPPORTED claims (PARTIAL in corrected wording) |
| 4 | `integrity-auditor` | everything | traces every sentence, fixes `notes.md` by deletion only, re-opens key sources, writes `audit.md` ending `SIGN-OFF: PASS` or `FAIL` |

Notes without `SIGN-OFF: PASS` are not used. All of this is an in-project AI review, not
peer review; agents checking agents can share blind spots, and sources that would not
load are listed, not counted as support.

## Running a new round

1. Create `docs/research/run-YYYY-MM-DD/brief.md` with numbered questions and any
   project statements to check (copy the format of `run-2026-11-09/brief.md`).
2. In Claude Code, from the repo root, ask: "Run the research pipeline on
   docs/research/run-YYYY-MM-DD: literature-reviewer, then fact-checker, then
   note-writer, then integrity-auditor."
3. Apply the "Corrections to the project" section of `notes.md` to the code and reports.

## Runs

- `run-2026-11-09/`: phase stability after anneals, CALPHAD vs experiment, Ta/Nb-rich
  compositions, ML limits, strength scatter. SIGN-OFF: PASS (15 defects fixed by the
  auditor).
- `run-2026-11-11/`: strength models, casting segregation, effect of V, cost and critical
  raw materials, comparison with existing refractory alloys; checks of the cost and
  validation inputs. SIGN-OFF: PASS (28 defects fixed by the auditor). Its 12 corrections
  are applied in `pipeline/finalists.py` and `pipeline/cost_supply.py`.
- `run-2026-11-13/`: check of the Maresca–Curtin strength model (equations, constants,
  elemental inputs, temperature law, edge vs screw at room temperature) and of the NbTaVW
  validation value, using the Yao et al. accepted manuscript supplied by the project owner
  (`sean-sources.md`). SIGN-OFF: PASS (19 defects fixed by the auditor). Corrections applied
  in `pipeline/strength_model.py`, `pipeline/finalists.py` and `README.md`; the published
  temperature law remains unresolved but changes no conclusion.
