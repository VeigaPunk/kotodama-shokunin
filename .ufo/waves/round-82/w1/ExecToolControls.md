# ExecToolControls — controls receipt, r82-v1 (claim O: `tools/check-sources-recheck.py`)

## Verdict

**DRAFT HOLDS under all 16 controls** — `{'pass': 16, 'FAIL': 0, 'unrun': 0}` against the current draft bytes
`sha256 95e67c16f466c0f1b2e34faf9681063b4af68024feb3a3ec4d0efd3b740ba219` (mtime 2026-11-04 08:25:32 -0300, 14259 B).
- `16/16 — RECHECK_TOOL=…drafts/tools/check-sources-recheck.py python3 /fast/scratch/hyaku/kotodama-r82/ExecToolControls/runner.py` → `ran {'pass': 16, 'FAIL': 0, 'unrun': 0}`
- Contract arithmetic cross-check: `as-of 2026-11-04 +90 = 2027-02-02 ; +91 = 2027-02-03 ; opened 2026-11-01 +3d = 2026-11-04 — python3 datetime sweep`.

No tool installs this seat (none needed; pacman paused per host ruling). No lane, fleet, corpus, or tool file was written by me; the only lane writes are the four receipt paths listed below.

## Files written (absolute)

1. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecToolControls/controls.md` — full human receipt: per case, fixture content, exact command, raw stdout/stderr, exit code, per-check verdicts, observations.
2. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecToolControls/controls.json` — machine-readable twin (same content, structured).
3. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecToolControls/fixtures/` — 13 fixture registries (fx01…fx12, contents also inlined in controls.md).
4. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecToolControls/runner.py` — the harness itself (deterministic; regenerates fixtures, binds tool sha256+mtime into the JSON meta).
5. This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ExecToolControls.md`.

## Case results (fixture → command → raw output → exit)

All runs: `python3 <draft> [--registry <fixture>] --as-of 2026-11-04`, TMPDIR pinned to `/fast/scratch/hyaku/kotodama-r82/ExecToolControls/tmp`, cwd scratch. Full raw text in controls.md.

| # | case | raw stdout (abridged where noted) | exit |
|---|------|-----------------------------------|------|
| 00 | `--selftest` | `SELFTEST: PASS (13 checks)` | 0 |
| 01 | empty registry (header+separator only) | `RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 0 rows` | 0 |
| 02 | recheck ISO `2026-11-04` == as-of | `DUE S201 2026-11-04` + `RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows` | 0 |
| 02b | `opened 2026-11-01`, recheck `3d` (NNd lands on as-of) | same counts, `DUE S202 2026-11-04` — NNd conversion correct | 0 |
| 03 | recheck ISO `2027-02-02` == as-of+90 | `RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 1 rows` (edge inclusive) | 0 |
| 03b | same fixture, `--window 89` | `RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows` (flag honoured) | 0 |
| 04 | recheck ISO `2027-02-03` == as-of+91 | `RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows` | 0 |
| 05 | `on-release` | `RECHECK-QUEUE: 0 due / 0 upcoming / 1 on-release / 1 rows` | 0 |
| 06 | 12-cell row | `RECHECK-ERROR line 9: row has 12 cells, expected 11` | 2 |
| 07 | recheck `soon` | `RECHECK-ERROR row S207: unparseable recheck cadence 'soon'` | 2 |
| 08 | opened `2026-13-40` | `RECHECK-ERROR row S208: opened '2026-13-40' is not a real calendar date` | 2 |
| 09 | missing `--registry` file | `RECHECK-ERROR registry …/fx/does-not-exist.md: No such file or directory` | 2 |
| 10 | base(1 due) + neutral row | due/upcoming/on-release unchanged, rows 1→2: `RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 2 rows` + `DUE S201 2026-11-04` | 0 |
| 11 | case 10 with `  | S210 | …` (2-space indent) | identical to case 10 — indented row parsed (0–3 leading spaces grammar) | 0 |
| 11b | case 10 with 4-space indent | `… / 1 rows` — 4-space row silently ignored (outside grammar; observation) | 0 |
| 12 | used-by `corpus/a.md\|corpus/b.md` | `RECHECK-ERROR line 9: row has 12 cells, expected 11` | 2 |

Every error case: single `RECHECK-ERROR` line on stdout, empty stderr, no traceback (checked per case: `"Traceback (most recent call last)" not in stdout+stderr`).

## Case 12 sweep — the registry forbids embedded pipes (evidence)

`python3` sweep over `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md` and the worktree copy:

- `base rows: 827 leading: {0: 827} non-11-cell rows: [] recheck vocab: {'on-release': 14, 'NNd': 659, 'ISO': 154}`
- `worktree rows: 831 leading: {0: 831} non-11-cell rows: [] recheck vocab: {'on-release': 14, 'NNd': 663, 'ISO': 154}`

Zero rows anywhere deviate from 11 cells → no real row carries a pipe inside `used-by` (or any cell); the pipe-in-used-by shape is grammar-forbidden, and case 12 shows the tool rejects it exit 2 anyway. Cadence vocabulary in the wild is exactly the three contract forms; `soon` (case 07) cannot arise today but is correctly rejected.

## Cross-seat reconciliation (ExecEvidence)

ExecEvidence reported `--selftest` exiting 1 with a fixture bug in selftest check 4 (`row(…)[:-1] + " extra |"` gluing `extra` into cell 11 → 11 cells → no error). Re-verified against current bytes:

- `sha256sum <draft>` → `95e67c16f466c0f1…`; `stat` → mtime `2026-11-04 08:25:32`, 14259 B (one byte more than the 14258 B file present at 08:20).
- `grep -n 'extra |' <draft>` → `253:                              [row("S911", "2026-01-01", "30d")[:-1] + "| extra |"])` — the pipe fix is in.
- `TMPDIR=… python3 <draft> --selftest` → `SELFTEST: PASS (13 checks)`, `exit=0`.

Conclusion: the defect was real for the pre-08:25:32 revision only; the author's one-char fix has landed and my controls ran entirely against the fixed bytes (receipt sha bound in controls.json meta). ExecEvidence's independent probes (12-cell, 10-cell, `fortnight` → exit 2; real-corpus tallies `0/18/14/827` and `813/0/14/827` matching the tool) corroborate my cases 06/07 and the population behavior on the real registry.

## Observations (behavior, not failures)

1. **Output order**: `DUE` lines print *before* the `RECHECK-QUEUE` summary. The contract pins line membership, not order, and the tool's own selftest expects DUE-first. No action needed unless the L1 wants order pinned.
2. **Row matching is file-wide**: `ROW_RE = ^\s{0,3}\|\s*S\d{3,}\s*\|` applies to every line, not just the `## Registry` section. Harmless today (sweep above: S-id pipe lines exist only as registry rows), worth knowing if prose ever quotes a row-shaped line.
3. **4-space+ indented S-rows are silently skipped** (case 11b) — ignored, not errored; consistent with the 0–3-space census grammar.
4. **Harness transparency**: my first harness version mis-applied two checks (summary-line check on `--selftest`; summary-first line order). Both were harness bugs, not tool bugs; corrected, receipts regenerated in full. A trailing-newline artifact in the order-note condition was also fixed before the definitive run.

## Risks / blockers

- None blocking. The draft is fit for the L1 freeze from a controls standpoint; freeze should re-pin sha256 at install time (the file changed once mid-round already).
- Scratch `/fast/scratch/hyaku/kotodama-r82/ExecToolControls/` removed before yield; receipts copied to stage first.
