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
