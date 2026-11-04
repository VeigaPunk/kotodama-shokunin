# ExecTool — round 82 / wave 1 — claim O artifact (recheck-cadence auditor)

**Verdict: PASS.** The claim-O tool is built to the frozen contract at
`.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py`, its 13-check
selftest passes, both required real-registry audits ran clean, and the
2027-11-01 output (813 DUE lines + summary) was cross-validated byte-for-byte
against an independent second implementation. No installs were needed
(python3 stdlib only).

## Files written (absolute paths)

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py` — the claim-O artifact (install target `tools/check-sources-recheck.py`; I did NOT touch `tools/`).
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecTool/` — receipts: `check-sources-recheck.py` (copy of final draft), `selftest.out`, `selftest.rc`, `audit-2026-11-04.out`, `audit-2026-11-04.rc`, `audit-2027-11-01.out`, `audit-2027-11-01.rc`.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ExecTool.md` — this report.

## Behavior implemented

- argparse: `--registry PATH` (default `corpus/SOURCES.md` relative to CWD; the tool never assumes a repo root), `--as-of YYYY-MM-DD` (required unless `--selftest`), `--window N` (int, default 90), `--selftest`.
- Row grammar: `^\s{0,3}\|\s*S\d{3,}\s*\|`; outer pipes stripped; row split on `|`; exactly 11 cells required (header of the real registry: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`; cells 0/8/9 drive the audit). Any other count → error.
- Cadence semantics: `on-release` → exempt (never due); `NNd` → opened + N days; ISO date → itself. Unparseable `opened` or cadence → error.
- Output: `DUE <id> <iso-date>` per due row in file order, then exactly one `RECHECK-QUEUE: <due> due / <upcoming> upcoming / <on-release> on-release / <rows> rows` (due = due_date <= as-of; upcoming = as-of < due_date <= as-of + window).
- Errors: exit 2, single `RECHECK-ERROR <detail>` line on stdout, no traceback (covers missing/unreadable registry, bad `--as-of`, wrong cell counts, unparseable cells; argparse failures are funneled through a custom parser to the same shape).
- `--selftest`: 13 checks, fixtures built under `tempfile.mkdtemp` (honours TMPDIR; verified by running with `TMPDIR=/fast/scratch/hyaku/kotodama-r82/ExecTool`). Includes every contract-required case: clean mixed registry (NNd/ISO/on-release + due exactly == as-of), window boundary inside (due == as-of+window → upcoming) and outside (window 89 → not counted), 12-cell row → exit 2 labelled, short-row count → exit 2 labelled, unparseable cadence → exit 2 labelled, unparseable opened → exit 2 labelled, missing file → exit 2 labelled, directory-as-registry → exit 2 labelled, bad `--as-of` → exit 2 labelled, missing `--as-of` → exit 2 labelled, population check (non-due append leaves due/upcoming unchanged), leading-space row (2 spaces) + default window.

## Evidence (commands + raw output)

### Selftest (13/13 PASS)

Command: `TMPDIR=/fast/scratch/hyaku/kotodama-r82/ExecTool python3 .ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --selftest` (cwd = scratch dir), rc 0, stderr empty. Raw stdout:

```
SELFTEST: PASS (13 checks)
```

13 checks — command above, raw output line `SELFTEST: PASS (13 checks)`.
Selftest coverage was itself exercised: the first run reported `SELFTEST: FAIL 12-cell row: rc=0 stdout='DUE S911 2026-01-31\nRECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows\n'` — my fixture had appended text inside the last cell instead of adding a pipe, so the row was genuinely 11 cells; fixing the fixture to 12 cells turned the same check green. That is the selftest catching a bad fixture, not a tool miss.

### Real-registry audit, as-of 2026-11-04

Command: `python3 .ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --as-of 2026-11-04 --window 90` (cwd = `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, so the default `corpus/SOURCES.md` resolved against CWD), rc 0, stderr empty. Raw stdout (1 line, no DUE lines since due=0):

```
RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 832 rows
```

### Real-registry audit, as-of 2027-11-01

Command: `python3 .ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --as-of 2027-11-01 --window 90` (cwd = lane root), rc 0, stderr empty, 814 stdout lines — 813 `DUE` lines + summary. Summary line (raw):

```
RECHECK-QUEUE: 813 due / 5 upcoming / 14 on-release / 832 rows
```

814 lines — `wc -l < audit-2027-11-01.out` (from the capture command in Evidence block). First DUE line and last DUE line, raw:

```
DUE S005 2027-04-17
DUE S903 2027-04-30
```

(Verified by reading the staged `audit-2027-11-01.out` lines 1 and 813 directly.)

### Independent cross-validation

A second, independently written implementation (same row grammar and cadence rules, in a throwaway python snippet over `corpus/SOURCES.md` bytes) produced an expected output list for 2027-11-01 and compared against the tool's full stdout:

```
expected lines: 814 actual lines: 814
IDENTICAL: True
```

The 2026-11-04 prediction matched as well (due=0, upcoming=18, exempt=14, rows=832), and both error paths were exercised by the selftest table above (each asserts rc 2, single RECHECK-ERROR stdout line, no 'Traceback' in either stream).

### Registry shape (basis for the audits)

- 832 rows in the current worktree registry — `open('/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md')` parsed with the census grammar in the validation snippet (raw: `rows now: 832`).
- 827 rows at lane base c285b2afb19d4b64320e18df1f55e426bf2d0b0c — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md` parsed the same way (raw: `registry rows: 827`, `cell-count histogram: {11: 827}`; max id S903).
- The +5 delta appeared during this wave: the current registry's max ids are `['S901','S902','S903','S904','S905','S906','S907','S908']` (raw from the same snippet) — sibling seats' new rows; all five carry `365d` (vocab moved `365d: 392 → 397`), opened 2026-11-04, hence upcoming (not due) at 2027-11-01. The tool reads bytes at run time, so its counts reflect whatever the registry holds when the L1 runs it.
- recheck vocabulary at validation time — raw `recheck vocab: {'365d': 397, '180d': 249, '2027-10-23': 112, '2027-10-22': 42, '90d': 18, 'on-release': 14}`; every `opened` cell is ISO (`bad opened cells: [] count: 0`), so the real registry contains no error rows.
- Buckets at 2027-11-01: 818 non-exempt rows = 813 due + 5 upcoming; the 5 upcoming are exactly the five wave-added `365d` rows (due 2027-11-04, inside the 90-day horizon), so all pre-wave dated rows are due. Arithmetic from the vocab above: 397 + 249 + 18 + 154 = 818 = 832 − 14 on-release.

## Installs

None. Tool is python3 stdlib only (`argparse datetime os re shutil subprocess sys tempfile`); no pacman (paused), no pip, no npm. python3 already present.

## Risks / notes

- The registry is a live file this wave; `rows` and bucket counts will drift if more rows land before the L1 installs the tool. Affects any auditor equally; not a tool defect.
- Argparse help/usage errors are folded into the `RECHECK-ERROR argument: ...` shape so exit-2-no-traceback holds for argument problems too; `--help` still prints normal help and exits 0.
- The selftest spawns the tool as a subprocess (`sys.executable`, script abspath) from the TMPDIR fixture root — no network, no writes outside its own mkdtemp (removed in `finally`).

## Blockers

None.
