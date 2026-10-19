- Seat: Ca06 | executor | claim Ca | date 2026-10-19 | baseline 57c8409

# Ca06 — recount-ledger draft

**Status: could-not-assemble.** The mission requires assembling the Ca01–Ca05 recounts into one row per command. All five named input fragments were absent when checked, so this fragment does not emit an empty or partially populated ledger that could be mistaken for a completed r37 recount.

The prior `reports/round-36/calib/recount-ledger.json` is historical input only: it identifies itself as a round-36 ledger, has 17 distinct-command rows covering rounds 33–35, and distinguishes those rows from its 21 table rows. Its observations are not represented as round-37 reruns. The round-36 validation also records a rejected round on D while Ca passed; neither fact supplies Ca01–Ca05's required r37 observed results.

## Owed

- `reports/round-37/calib/Ca01-r33.md` — missing; needed to assemble round-33 recount rows.
- `reports/round-37/calib/Ca02-r34.md` — missing; needed to assemble round-34 recount rows.
- `reports/round-37/calib/Ca03-r35.md` — missing; needed to assemble round-35 recount rows.
- `reports/round-37/calib/Ca04-r36.md` — missing; needed to assemble round-36 recount rows, including the rejection receipt.
- `reports/round-37/calib/Ca05-cross-cutting.md` — missing; needed to assemble recurring cross-cutting command rows.

## Citations

- `reports/round-37/targets.json:19-24` — Ca01–Ca05 output paths and Ca06 assembly mission/schema.
- `reports/round-37/claims.json:13-18` — recount claim, required coverage, and disposition threshold.
- `reports/round-36/calib/recount-ledger.json:2-15,51-64` — provenance, prior-round scope, row-count convention, and historical observation method.
- Command-output evidence: after `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin` and `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, a read-only Python `Path.is_file()` check returned `MISSING` for each of the five paths listed under `## Owed`.
