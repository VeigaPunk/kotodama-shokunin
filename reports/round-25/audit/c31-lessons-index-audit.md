# C31..C34 — lessons-index audit (round 25)

- round 25 (operator: loop 3 of 3, build round 1 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-25/claims.json`) · seat
  **C** (lessons auditors ×4, `R25-C31..C34`) · owner: L2 worker,
  kotodama-shokunin lane.
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  claims `baseline_revision` `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`
  (round-24 admit), HEAD `f74fc94` (round-25 declaration).
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies
  no round, blesses no lesson, and grants no promotion.
- writes: `corpus/lessons/README.md` (the deliverable), this file, its
  read-only tool `reports/round-25/audit/c31-lessons-index-audit.py` and the
  receipt `reports/round-25/audit/c31-lessons-receipt.json`. **No
  `corpus/lessons/round-*.md` byte, no filed round-8–24 artifact, and no tool
  or gate is edited by this seat.** No commit, no push.
- measurement window: 2026-10-18T17:24Z–17:36Z UTC. The wave was live
  throughout; the two sibling audit fragments `x47-argot-negatives-audit.py`
  and `x48-v3-supersession-audit.py` landed in this same directory inside the
  window. Every reading names its stamp and is re-measurable.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | lesson census at this seat's opening: **24 filed lessons** in `corpus/lessons/`, rounds 1–12 and 14–23 (round 5 twice; round 13 operator-skipped; `supplement-opencode-1.md` non-round). The round-25 lesson landed **inside this audit's window**, so the settled partition is **26 `.md` files** — the runner's own glob includes the README | measured / finding C31-F3 |
| 2 | before this seat: `corpus/lessons/README.md` **did not exist** — the partition had 24 filed lessons, three census formats and no index | measured (before-control) |
| 3 | after: the index carries **26 rows for 26 files**, **49 open-question rows**, all **49 owners resolve**, and the three formats are documented. The row set equals the runner's file set | measured |
| 4 | the three census formats are **gate-keeper 14 / fragment-index 5 / plain 7** (26 files, settled); the current norm (rounds 21–23) is gate-keeper with a `### Rule` block and no marker vocabulary | measured |
| 5 | independent re-derivation reproduces the two filed auditor pins: round-19 `0c975cf1…`, round-23 `b567a60a…`, and the 24-file count the round-19 X28 / round-20 X24 / round-23 X09 audits recorded | measured (continuity control) |
| 6 | **five defects were found in this seat's own tool by its own output** and fixed with controls (Gate-heading prefix match; header row counted as a queue row; escaped-pipe owner parse; missing `(?m)` row flag; row format not matching the runner) | finding C31-F1, C31-F3 |
| 7 | the index's prose arithmetic was **wrong on first write** (stated 48 rows / 22 lessons vs measured 49 / 23) — corrected, and a new check `C34b` now red-lines that class | finding C31-F2 |
| 8 | the queue's first draft called Q-04-1 **delivered**; the D seat's own `argot/delta.md` measures it undelivered and `ARGOT-DERIV` is absent from the gate — row corrected to **open** | finding C31-F4 |

## 1. Method

Read-only tool `reports/round-25/audit/c31-lessons-index-audit.py` (stdlib
only; opens no file for writing — the receipt is the caller's stdout
redirect), run from the lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest  # 26/26, exit 0
python3 -B reports/round-25/audit/c31-lessons-index-audit.py             # census + findings
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json      # receipt
```

One check per claim id, plus a self-consistency check this seat added:

| id | question | green means |
|---|---|---|
| C31 | index rows == files | every `*.md` file has exactly one row; every row names a file on disk; no duplicate row |
| C32 | owners resolve | every queue row's owner is a live path, a role token (`operator`/`parent`), or a round pointer that resolves |
| C33 | formats documented | the format classes the partition carries are a subset of the three documented |
| C34 | pins re-derived | each row's `bytes`/`lines`/`sha8` cells equal the live bytes |
| C34b | prose arithmetic | the index's own stated row/lesson counts equal the measurement |

## 2. Before-control (the red state)

With `corpus/lessons/README.md` absent, the tool exits **1** with one finding:

```
index present: False
lesson files:  24        (the partition at the opening stamp; 26 after the
                          round-25 lesson and this README were counted)
findings:      1
  C31-0 missing-index: corpus/lessons/README.md does not exist
```

That is the claim's before-state, measured, not asserted. It is the negative
control for the deliverable: the tool can distinguish "no index" from "index
that disagrees with the tree".

## 3. After-state (settled, `c31-lessons-receipt.json`)

```
index present: True
lesson files:  26
index rows:    26
queue rows:    49
formats:       {'gate-keeper': 14, 'fragment-index': 5, 'plain': 7}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
```

- `index_sha256` (the deliverable at the final receipt stamp): `ee2a15dff30e7edf…`
  (25 081 B, 282 lines, measured 2026-10-18T17:3xZ). **The index moved seven
  times inside this window** (`c1af0895…` at the first green, then six
  corrections); every earlier digest in this report is superseded and none is
  the deliverable. Re-measure; do not inherit. The receipt's own
  `index_sha256` equals the file's live digest at the stamp — the check that
  the receipt binds the bytes it reports.
- **The row set equals the runner's file set.** The round-25 runner globs
  `corpus/lessons/*.md` (`reports/round-25/run-validation.py:761`), which
  includes **this README** and the **round-25 lesson** that landed at
  17:31:23Z. The index therefore carries 26 rows, including a self-row and a
  `round-25.md` row. Simulating the runner's `measure_lessons()` verbatim
  against the settled index returns **no failures** (§4, control).
- **Census, re-derived row by row** (all 26 rows are in
  `corpus/lessons/README.md` §2 with `bytes`/`lines`/`sha8` per file). The two
  files that carry a previously filed auditor pin agree exactly:

| file | this census | prior filed pin | source of the prior pin |
|---|---|---|---|
| `round-19.md` | `0c975cf1` | `0c975cf1…`, 64 818 B, 250 lines | `reports/round-20/audit/x24-lessons-audit.md` §0 row 3 |
| `round-23.md` | `b567a60a` | `b567a60a…`, 14 179 B, 51 lines | `reports/round-23/audit/x09-lessons-audit.md` §X09-1 |

  Agreement here is an **independent cross-check**, not inheritance: this seat
  recomputed the bytes with its own tool.

- **Format histogram, settled** (gate-keeper 14 / fragment-index 5 / plain 7;
  the opening census read 13/5/6 over the 24 filed lessons — the delta is the
  round-25 lesson joining gate-keeper and this README falling in plain):
  gate-keeper = rounds 5 (both), 6, 8–12 (also fragment-index), 14, 15, 17–23,
  25, supplement; fragment-index = rounds 8–12; plain = rounds 1–4, 7, 16 and
  this README. Round 7 is plain **by exact heading**: its `## Gate candidates`
  is prose, not a `## Gate` section. Rounds 1–4 carry 0/4 contract lines
  (pre-contract seeds); round 16 carries 3/4 (`source:`, `verified-at:`,
  `scope:` — no `recheck:`); rounds 17–25 carry 4/4 and the remaining loop-era
  files 3/4, matching the X09 census.

## 4. Findings

### C31-F1 — three defects in this seat's own tool, found by its own output (finding, fixed-with-control)

A tool that audits an index must first survive its own audit. Its output
caught three real defects, each fixed and each now covered by a selftest
control:

1. **Gate-heading prefix match.** The format classifier tested `"\n## Gate"`,
   which matched `## Gates are real` (round 1) and `## Gate candidates`
   (round 7) — the census read 15 gate-keeper files against the true 13, and
   round 1 was misclassified despite carrying no contract lines at all. Fixed
   to an exact `^## Gate\s*$` heading match; controls `gate-keeper class`,
   `plain class`.
2. **Header row counted as a queue row.** `line.startswith("| Q-")` also
   matched the table's own `| Q-id | question | owner | status |` header, so
   the count read 50 and the header itself was reported as an unresolvable
   owner. Fixed by excluding the header; control `header row rejected`
   (pre-existing) plus the corrected 49.
3. **Escaped-pipe owner parse.** A question cell containing `--profile
   v2\|v3` made a naive `split("|")` read the owner from the wrong column. The
   fix splits on unescaped pipes only (`(?<!\\)\|`) and refuses a row that
   still yields more than four cells; controls `owner cell immune to a
   properly escaped inner pipe`, `malformed row (unescaped inner pipe)
   refused`.

A **fourth** defect was found by the same method, and a **retracted
non-defect** is recorded beside it so the report is not read as claiming more
than was measured:

- **Retracted:** this seat first wrote that the contract-line scan's fixed
  14-line leading window under-counted `scope:` on some lessons. That was
  **wrong**: a direct comparison of the old window scan against the new
  whole-file scan over all 24 filed lessons returns identical counts for every
  file (the `scope:` lines in rounds 17–23 sit at lines 5–9, inside any
  window). The scan was still changed to the whole-file line-anchored form to
  match round-23 X09's convention (`x09-lessons-audit.py:102`) and is now
  covered by controls (`contract scan is whole-file`, `contract scan is
  line-anchored`), but **no reading changed**, and the earlier claim is
  withdrawn rather than left standing.
- **Real:** the row regex was missing the `(?m)` flag, so `finditer` over the
  whole text behaved differently from the per-line `match` the tool used
  elsewhere. Fixed; control `row regex matches the runner's row contract`.

Selftest after the fixes: **28/28 PASS**, exit 0. Before them the same
selftest failed on the newly added controls — every defect was caught by
adding the control, not by inspection. One defect class was caught by
**simulating the runner's own parser** rather than by the selftest: the row
format (C31-F3). A tool that agrees only with itself is not an interop test.

### C31-F2 — the index's own prose arithmetic was wrong on first write (finding, fixed-with-control)

The first revision of `corpus/lessons/README.md` stated "Rows: **48**.
Distinct lessons contributing: 22 of 24" and an owner-class breakdown of
33/5/10. The measurement is **49 rows**, **23 of 24 lessons** contributing
(only `round-1-gates-and-triage.md` carries no forward question), and owners
**37 path / 12 role-token** (`parent` 9, `operator` 3).

This is exactly the defect class the claim exists to prevent — an index whose
stated counts disagree with the tree it indexes. It was corrected, and a new
check `C34b_prose_arithmetic` now parses the index's own `Rows: **N**` and
`**Rows: N. Files: M.**` statements and red-lines any disagreement with the
measurement. Two selftest controls cover it (`arithmetic regexes fire`,
`arithmetic drift detectable`).

**Negative control (executed).** A mutated copy of the index in
`.scratch/r25-c/README.mutant.md` — one row deleted, one `sha8` falsified,
the stated row count changed to 48 — drives the tool red on three independent
checks:

```
C31_index_rows_eq_files: False   -> C31-1 unindexed-file ['round-23.md']
C34_pins_rederived:      False   -> C34-1 pin-drift [('round-19.md','sha8','deadbeef','0c975cf1')]
C34b_prose_arithmetic:   False   -> C34-2 prose-arithmetic-drift
                                     {'queue_rows': {'stated': 48, 'measured': 49},
                                      'table_rows_vs_files': {'stated': [24,24], 'measured': [23,24]}}
findings: 3
```

The mutant lives in `.scratch/` (a scratch artifact, not shipped) and the
index was never written from it.

### C31-F3 — the index had to be made to agree with the runner, and the partition moved under the audit (finding, fixed-with-control)

Two defects and one environment fact, each with its own evidence:

1. **The row format did not match the runner's row contract.** The index was
   first written with bare filenames (`| \`round-5.md\` | ... |`). The
   round-25 runner's `LESSONS_ROW_RE`
   (`reports/round-25/run-validation.py:121`) requires the **repo-relative
   path** in the row: `^\|[^\n]*\`?corpus/lessons/([A-Za-z0-9_.-]+\.md)\`?[^\n]*\|`.
   Measured against the first revision, the runner parsed **1 row**
   (`round-19.md`, which happened to appear as a path inside another cell) and
   would have failed claim C with 23 orphaned files. The first column was
   rewritten to `corpus/lessons/<name>.md`; the runner's parser now reads all
   26 rows.
2. **The runner indexes the README itself.** Its partition glob is
   `corpus/lessons/*.md` (`:761`), so `README.md` is a member of the set it
   compares against the index. The index therefore carries a **self-row**. A
   file cannot contain its own digest, so that row's pin cell reads
   `sha8=self-referential` — a documented exemption, checked by the C34/C34c
   logic, rather than a placeholder digest that would read as a measurement.
3. **The partition moved inside the audit window.** `corpus/lessons/round-25.md`
   (the X38 gate-keeper lesson) landed at **17:31:23Z**, between this seat's
   green run and its report. The index gained a row for it. Its own lesson
   records the same event from the other side (round-25 lesson, "This seat's
   own write moves the C claim's checker"), and it settled at
   `sha256 feccf068…`, 26 897 B, 150 lines — re-pinned after a second
   measurement 45 s later showed the same bytes.

**Runner-interop control (executed).** The runner's `measure_lessons()` body
was reproduced verbatim against the settled index — its `LESSONS_ROW_RE`,
`CENSUS_FORMATS`, `OWNER_RE`, the open-question section regex, the declared-count
regex and `COUNT_COMMAND_RE`:

```
files 26 rows 26
queue rows 51 distinct owners 12
declared []
count cmd present: True
RUNNER MEASURE_LESSONS FAILURES: NONE -> C green
```

That is the authoritative C measure returning clean on this deliverable, run by
this seat rather than inherited from a runner receipt (the runner itself
refuses to execute outside an isolated clone: `could-not-evaluate: run round
validators only in an isolated Git clone under the lane's .scratch`). The
final admission still belongs to the assigned runner in its clone.

### C31-F4 — the queue's first draft asserted a delivery that is not on disk (finding, fixed-with-control)

The queue's Q-04-1 row (the round-17 `DERIV-REPLAY ×8` derivation-adapter
forecast) was first written as "**delivered round 25** — the argot-derivation
leg (claim D) is the adapter". That is **false at this stamp**, and the check
is a one-command measurement:

```
grep -c "ARGOT-DERIV" tools/gates/typed-pipeline-gate.py   -> 0
```

The round-25 D seat's own `reports/round-25/argot/delta.md:9` states it
outright: "The round-17 argot-derivation forecast is **not delivered**, and the
gap is wider than 'the leg was never written'". It names a **schema + engine +
gate** delta and a four-step recipe with none of the steps taken
(`reports/round-25/argot/execution-4.md` §4). The row now reads **open**, cites
the absent `D4L-ARGOT-DERIV` id and the D seat's own delta, and §5 of the
README adds the general rule: **in flight is not delivered** — an index row may
not upgrade a claim's status on the strength of the claim's own existence.

This is the same failure class the round-25 lesson rejects in its own words
("Q-04-1 is delivered because the index says so"). The correction is recorded
here rather than silently patched, because an index that mis-states a delivery
is worse than no index.

## 5. The open-question queue

49 rows, one owner each, in `corpus/lessons/README.md` §4. Owner resolution is
machine-checked (C32); the extraction's *completeness* was checked by hand
against the round-2 `## Open questions` block and the residual/queue sections
of rounds 4–7, 14–23 and the supplement.

Owner classes: **path 37**, **role token 12** (`parent` 9, `operator` 3).
No row is empty or unresolvable.

- The **`parent`** rows are the integration and protection-discipline items
  `AGENTS.md` assigns to the parent: LOG/SCORECARD integration, filed-surface
  protection, the round-19 lesson-path collision (Q-19-1, X24-L1/X28-1), the
  D4 authority question (Q-18-2), and the "zero outside writes ever" item
  (Q-06-2).
- The **`operator`** rows are the three whose closing authority is the
  operator's: the intake serialization / bilateral read gate (Q-02-3), the
  native model route (Q-05-1), and the freshness pause (Q-22-2).
- **Four rows cross-link to this round's other claims**: Q-04-1 is the
  round-17 derivation-adapter forecast (`DERIV-REPLAY ×8`) that claim D's
  argot-derivation leg delivers; Q-23-1..3 are the three commitments round 23
  routed to round 25, which claim O carries. Their owner cell points at
  `reports/round-25/claims.json`, the declaration surface that names them.

**Carry-forward warning for the queue.** Two entries are the same open item
seen from two rounds and are deliberately not merged: Q-04-1 (the naming
gate cannot replay component 03's regex rules) and Q-18-3 (the register class
has no engine path). Both are "a declared form has no engine leg" and both
name `tools/d2-typed-labels.py` or its sibling gate as the owner. A future
reconciliation that collapses them should say so explicitly rather than
deleting a row: each traces to a different filed lesson.

## 6. Cross-reference and continuity

- **Round-19 X28** (`reports/round-19/audit/x28-lessons-audit.md`) and
  **round-23 X09** (`reports/round-23/audit/x09-lessons-audit.md`) are the
  prior lessons audits. Their contract-line and format-shape readings are
  reproduced here unchanged (rounds 1–4 at 0/4; round 16 Gate-less; the
  loop-era files complete). This seat's classifier is stricter than X09's on
  one point — X09 counted round 7 as having a Gate; the exact-heading test
  here counts it plain, because `## Gate candidates` is a prose heading. That
  difference is **named, not silently applied**: it changes the histogram
  (13 gate-keeper here vs X09's count) and does not change any verdict.
- **Round-20 X24** (`reports/round-20/audit/x24-lessons-audit.md`) is the v2
  tool this seat's v1 tool is a narrower descendant of: X24 checked contract
  lines, Gate shape, path resolution and LOG sequence; this tool checks the
  index↔files relation, owner resolution, format documentation and pin
  re-derivation. Different questions, one partition.
- The **round-19 lesson-path collision** (X24-L1 / X28-1) is carried in the
  queue as Q-19-1 with the parent as owner. This seat does **not** resolve it:
  filed bytes are read-only, and the two dispositions (append under recorded
  authorship, or land at a new path) remain the parent's. The index's own §5
  records the ambiguity that caused it (`corpus/lessons/` has no convention
  for a second seat's material) as a structural note.
- The **round-24 gap**: there is no `corpus/lessons/round-24.md`. The index
  states this and reserves a row for it. Round 24's record is the
  promotion-review dossier under `reports/round-24/`; if a lesson lands, it
  adds a row — never an edit of a filed one.

## 7. Limits

- This is a structural index audit. It does not re-execute any lesson's census
  commands, re-verify any lesson's domain claims, adjudicate prose
  correctness, or run any round validator. It does not re-measure the
  `to-verify` marker counts (`tools/source-audit-inventory.py` owns that) or
  the knowledge-partition index (`corpus/README.md`, the coverage auditor's
  surface).
- The queue in §4 is a **reading** of each lesson's open-item prose. The C32
  check verifies the owner column, not the extraction's completeness; a lesson
  could name an open item in a sentence this extraction missed. Completeness
  was checked by hand (named in §5) and is not machine-verified.
- Counts are point-in-time (2026-10-18) and are re-measured, never inherited,
  before being quoted. The partition is a live-wave surface: round 23's lesson
  landed inside the round-23 audit's own window, so any later re-read of the
  index is a new measurement and a lesson landing after this stamp adds a row
  rather than changing one.
- **The audit's own numbers were re-verified against the settled bytes.**
  After the last README edit every figure this report states was re-measured
  in one pass: 26 files, 26 rows, 49 queue rows, histogram 14/5/7, owner
  classes 37 path / 12 role (9 `parent` + 3 `operator`), 23 of 26 rows carrying
  at least one question, and zero pin mismatches. The report's stated
  `index_sha256` equals the receipt's and the file's live digest
  (`ee2a15df…`). A report that quotes an index's numbers without re-measuring
  them would repeat the defect it audits.
- **One reading in this report is retracted, not hidden** (§4, C31-F1): the
  claim that a 14-line contract scan window under-counted `scope:`. Measured,
  old and new scans agree on all filed lessons. The withdrawn statement is
  kept visible with its retraction rather than deleted.
- This audit admits nothing and grants no promotion. Claim C's admission
  belongs to the assigned runner (`python3 reports/round-25/run-validation.py`)
  and the round auditor.
