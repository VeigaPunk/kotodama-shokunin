# ExecToolControls — controls receipt, draft `tools/check-sources-recheck.py`

- tool: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py`
- tool sha256: `95e67c16f466c0f1b2e34faf9681063b4af68024feb3a3ec4d0efd3b740ba219` (mtime 1793791532.4054022)
- as-of 2026-11-04, window 90: edge +90 = 2027-02-02, +91 = 2027-02-03 — python3 -c "date(2026,11,4)+timedelta(days=90)"
- python 3.14.8; runner: /fast/scratch/hyaku/kotodama-r82/ExecToolControls/runner.py

## 00-selftest — --selftest runs >= 8 checks, prints SELFTEST: PASS (<n> checks)
- expected exit 0; verdict **pass**
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --selftest`
- raw stdout:
```
SELFTEST: PASS (13 checks)
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; selftest line format=ok; selftest >= 8 checks=ok

## 01-empty-registry — header-only registry -> all zero, exit 0
- expected exit 0; verdict **pass**
- fixture `fx01_empty.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx01_empty.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 0 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok

## 02-due-exactly-on-asof — recheck ISO == as-of -> due +1
- expected exit 0; verdict **pass**
- fixture `fx02_due_on_asof.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S201 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2026-11-04 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx02_due_on_asof.md --as-of 2026-11-04`
- raw stdout:
```
DUE S201 2026-11-04
RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok
- note: line ORDER differs from contract prose order: tool prints DUE lines first, summary last; contract text pins membership only; tool's own selftest expects DUE-first

## 02b-nnd-lands-on-asof — opened 2026-11-01 + 3d == as-of -> due +1 (NNd conversion)
- expected exit 0; verdict **pass**
- fixture `fx02b_nnd_due.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S202 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-11-01 | 3d | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx02b_nnd_due.md --as-of 2026-11-04`
- raw stdout:
```
DUE S202 2026-11-04
RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok
- note: line ORDER differs from contract prose order: tool prints DUE lines first, summary last; contract text pins membership only; tool's own selftest expects DUE-first

## 03-due-at-window-edge — due_date == as-of+window(90) -> upcoming +1 (inclusive edge)
- expected exit 0; verdict **pass**
- fixture `fx03_upcoming_edge.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S203 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2027-02-02 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx03_upcoming_edge.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok

## 03b-window-89-flag — same fixture with --window 89 -> edge drops out (window flag honoured)
- expected exit 0; verdict **pass**
- fixture `fx03_upcoming_edge.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S203 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2027-02-02 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx03_upcoming_edge.md --as-of 2026-11-04 --window 89`
- raw stdout:
```
RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok

## 04-beyond-window — due_date == as-of+window+1 -> neither due nor upcoming
- expected exit 0; verdict **pass**
- fixture `fx04_beyond_window.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S204 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2027-02-03 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx04_beyond_window.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok

## 05-on-release — on-release -> exempt cadence counted, not due
- expected exit 0; verdict **pass**
- fixture `fx05_on_release.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S205 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | on-release | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx05_on_release.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-QUEUE: 0 due / 0 upcoming / 1 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok

## 06-12-cell-row — 12-cell row -> exit 2, RECHECK-ERROR, no traceback
- expected exit 2; verdict **pass**
- fixture `fx06_12_cell_row.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S206 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 90d | — | EXTRA |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx06_12_cell_row.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-ERROR line 9: row has 12 cells, expected 11
```
- raw stderr:
```
(empty)
```
- exit code: 2
- checks: exit code=ok; no traceback=ok; RECHECK-ERROR printed=ok

## 07-recheck-soon — recheck 'soon' unparseable -> exit 2, RECHECK-ERROR, no traceback
- expected exit 2; verdict **pass**
- fixture `fx07_recheck_soon.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S207 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | soon | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx07_recheck_soon.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-ERROR row S207: unparseable recheck cadence 'soon'
```
- raw stderr:
```
(empty)
```
- exit code: 2
- checks: exit code=ok; no traceback=ok; RECHECK-ERROR printed=ok

## 08-opened-invalid-iso — opened 2026-13-40 -> exit 2, RECHECK-ERROR, no traceback
- expected exit 2; verdict **pass**
- fixture `fx08_bad_opened.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S208 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-13-40 | 90d | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx08_bad_opened.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-ERROR row S208: opened '2026-13-40' is not a real calendar date
```
- raw stderr:
```
(empty)
```
- exit code: 2
- checks: exit code=ok; no traceback=ok; RECHECK-ERROR printed=ok

## 09-missing-registry-file — missing --registry path -> exit 2, RECHECK-ERROR (not an uncaught exception)
- expected exit 2; verdict **pass**
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/does-not-exist.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-ERROR registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/does-not-exist.md: No such file or directory
```
- raw stderr:
```
(empty)
```
- exit code: 2
- checks: exit code=ok; no traceback=ok; RECHECK-ERROR printed=ok

## 10-population-modularity — base + neutral row -> due/upcoming/on-release unchanged, rows +1
- expected exit 0; verdict **pass**
- fixture `fx10_base_plus_neutral.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S201 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2026-11-04 | — |
| S210 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2099-01-01 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx10_base_plus_neutral.md --as-of 2026-11-04`
- raw stdout:
```
DUE S201 2026-11-04
RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 2 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok
- note: line ORDER differs from contract prose order: tool prints DUE lines first, summary last; contract text pins membership only; tool's own selftest expects DUE-first

## 11-indented-row — 2-space indented row parsed (census grammar allows 0-3 leading spaces)
- expected exit 0; verdict **pass**
- fixture `fx11_indented_neutral.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S201 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2026-11-04 | — |
  | S210 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2099-01-01 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx11_indented_neutral.md --as-of 2026-11-04`
- raw stdout:
```
DUE S201 2026-11-04
RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 2 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok
- note: line ORDER differs from contract prose order: tool prints DUE lines first, summary last; contract text pins membership only; tool's own selftest expects DUE-first

## 11b-4space-row-ignored — observation: 4-space indented row is outside the 0-3 grammar -> silently ignored
- expected exit 0; verdict **pass**
- fixture `fx11b_4space_neutral.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S201 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2026-11-04 | — |
    | S210 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 2099-01-01 | — |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx11b_4space_neutral.md --as-of 2026-11-04`
- raw stdout:
```
DUE S201 2026-11-04
RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows
```
- raw stderr:
```
(empty)
```
- exit code: 0
- checks: exit code=ok; no traceback=ok; exactly one summary line=ok; stdout lines exact, order-insensitive (contract pins membership, not order)=ok
- note: line ORDER differs from contract prose order: tool prints DUE lines first, summary last; contract text pins membership only; tool's own selftest expects DUE-first

## 12-pipe-in-usedby — used-by with embedded pipe -> 12 cells -> grammar forbids; expect exit 2 RECHECK-ERROR
- expected exit 2; verdict **pass**
- fixture `fx12_pipe_in_usedby.md`:
```
# SOURCES — controls fixture

prose preamble; tool must scope to the Registry section.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S212 | Fixture Source — https://example.org/fx | dataset | A | controls stress scope | anchor p1 para | teaches text for controls | queued | 2026-01-01 | 90d | corpus/a.md|corpus/b.md |
```
- command: `/usr/bin/python3 /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py --registry /fast/scratch/hyaku/kotodama-r82/ExecToolControls/fx/fx12_pipe_in_usedby.md --as-of 2026-11-04`
- raw stdout:
```
RECHECK-ERROR line 9: row has 12 cells, expected 11
```
- raw stderr:
```
(empty)
```
- exit code: 2
- checks: exit code=ok; no traceback=ok; RECHECK-ERROR printed=ok

## Observations (behavior, not failures)
- Output order: `DUE` lines precede the `RECHECK-QUEUE` summary; the contract pins line membership only (cases 02/02b/10/11), and the tool's own selftest expects DUE-first. No action needed unless the L1 wants to pin order.
- Row matching is `^\s{0,3}\|\s*S\d{3,}\s*\|` applied to EVERY line of the file (not scoped to `## Registry`). Harmless for the real corpus: sweep of base c285b2af and worktree found S-id pipe rows only as registry rows (base 827 / worktree 831 rows, all 11 cells, all flush-left).
- Real-corpus cadence vocabulary (worktree): on-release 14, NNd 663, ISO 154 — no other form occurs; case 07's `soon` cannot arise today but correctly exits 2.
- 4-space (or deeper) indented S-rows are silently skipped by ROW_RE (case 11b) — outside the 0-3 grammar, ignored not errored.
- `used-by` with an embedded pipe widens the cell count to 12 and is rejected exit 2 (case 12). The real registry forbids it: zero non-11-cell rows in base and worktree sweeps — python3 sweep over git show c285b2af…:corpus/SOURCES.md and worktree copy.
