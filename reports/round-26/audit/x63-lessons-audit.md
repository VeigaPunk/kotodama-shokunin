# X63 — lessons audit (round 26)

- round 26 (operator: loop 3 of 3, build round 2 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-26/claims.json`) · seat
  **X63** (SCRIBE X63 — lessons audit) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X63: lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  claims `baseline_revision` `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` (round-25
  admit), HEAD `1ad491a` (round-26 declaration).
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies no
  round, blesses no lesson, and grants no promotion.
- writes: **this file**, its read-only tool
  `reports/round-26/audit/x63-lessons-audit.py` and the receipt
  `reports/round-26/audit/x63-lessons-receipt.json`. **No `corpus/lessons/**`
  byte was written or edited by this seat** — in particular
  `corpus/lessons/README.md` is the round-25 C seat's deliverable and this seat
  read it only. No filed round-8–25 artifact, tool or gate was edited. No
  commit, no push.
- measurement window: 2026-10-18T18:00:42Z–18:04:42Z UTC. The wave was live
  throughout; `corpus/lessons/README.md` was stable at
  `sha256 ec7469dadf87df3e…` (29 059 B / 346 lines) for the whole window, so
  every reading below binds to one digest.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the partition is **26 `.md` files**, the index carries **26 rows** — zero orphan, zero phantom, zero duplicate | measured |
| 2 | **all 25 pinned rows re-derive exactly** on the live bytes (bytes, lines, sha8); the 26th is the index's own self-row, exempt by construction | measured |
| 3 | **25/25 format cells and 25/25 contract cells re-derive**; the live histogram is gate-keeper 14 / fragment-index 5 / plain 6 / index 1 | measured |
| 4 | **49 queue rows, 49 carried ids, zero orphans in either direction**; every owner resolves (37 path, 12 role token) | measured |
| 5 | every §2 disposition pointer resolves, **or its own cell declares the path was never filed** (4 such rows, all honest) | measured |
| 6 | **six queue/index readings were true at the index's stamp and are contradicted by today's bytes** — the round-12 and round-21 pointers, Q-04-1's status, and Q-23-1..3's status | **finding X63-G1** |
| 7 | the round-25 X45 pointer tool now reads **red** on the round-4 cell the C35 seat corrected — a cross-tool disagreement, not an index defect | **finding X63-D2** |
| 8 | the index has **no row for round 24**, and its own §2 prose names the omission as a dossier rather than a missing row | measured |

## 1. Method

Read-only tool `reports/round-26/audit/x63-lessons-audit.py` (stdlib only; opens
no file for writing — the receipt is the caller's stdout redirect), run from the
lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-26/audit/x63-lessons-audit.py --selftest   # 20/20, exit 0
python3 -B reports/round-26/audit/x63-lessons-audit.py              # findings
python3 -B reports/round-26/audit/x63-lessons-audit.py --json       # receipt
```

| id | question | green means |
|---|---|---|
| A | row/file set | every `.md` file has exactly one row, every row names a file, no duplicate |
| B | pins | each row's `bytes`/`lines`/`sha8` equals the live bytes (self-row exempt) |
| B2 | shape cells | each row's `format` and `contract` cell equals a live re-derivation |
| D | pointers | every backticked path in a disposition pointer resolves, **unless** the pointer's own cell declares the path absent |
| E | queue cross-consistency | every id §2 claims to carry has a queue row, and every queue row is claimed |
| E2 | owners | every queue owner is a live path, `operator`, or `parent` |
| F | prose arithmetic | the index's stated row/file counts equal the measurement |
| G | staleness | no cell asserts a state that today's bytes contradict |
| H | round-13 row | the skipped-round row says why no lesson file exists |

**Relation to the two round-25 auditors, named rather than assumed.** The C31
tool (`reports/round-25/audit/c31-lessons-index-audit.py`) checks the row/file
set, owner resolution, documented formats and pin re-derivation; the X45 tool
(`reports/round-25/audit/x45-lessons-pointer-audit.py`) checks the pointer
column and the prose counts. This tool re-runs the union of those surfaces on
the current bytes and adds **G**, the staleness probe, which neither performs.
Both round-25 tools were re-executed at this stamp as the cross-check: C31 is
**green, findings 0** (28/28 selftest); X45 is **red, 1 finding** on the
round-4 pointer (15/15 selftest) — see X63-D2.

## 2. After-state (2026-10-18T18:06:53Z, `x63-lessons-receipt.json`)

```
index:        corpus/lessons/README.md
sha256:       ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c
bytes/lines:  29059 / 346
lesson files: 26      index rows: 26      queue rows: 49
  PASS A_rows_eq_files            PASS E2_owners_resolve
  PASS B_pins_rederived           PASS F_prose_arithmetic
  PASS B2_shape_cells_rederived   FAIL G_no_stale_readings
  PASS D_pointers_resolve         PASS H_round13_row_self_describes
  PASS E_queue_cross_consistency
findings:     1  (X63-G1, six instances)
```

Every reading above is a point-in-time measurement of the bytes at
`ec7469dadf87df3e…`. The index is a round-25 artifact and the round-25 runner
owns its acceptance; this audit admits nothing.

## 3. Findings

### X63-G1 — six index readings were true at the stamp and are false now (finding)

The index was written and last revised on 2026-10-18 at 17:48Z UTC, **before**
the round-25 close commit `fc13cd2` landed at 14:58:37 local (17:58:37Z). Its
queue and its §2 pointer column therefore describe a state that the close
commit then changed. Six cells, each measured now:

| # | surface | the cell says | measured now |
|---|---|---|---|
| 1 | `round-12.md` §2 pointer | `reports/round-12` (no `validation.json`; provisional, no admission) | `reports/round-12/validation.json` exists, `acceptance_checks_passed: true`, baseline `a3f6fcef…` |
| 2 | `round-21.md` §2 pointer | `reports/round-21` (no `validation.json` at the lesson's stamp) | `reports/round-21/validation.json` exists, `acceptance_checks_passed: true`, baseline `35b6797b…` |
| 3 | `Q-04-1` status | `D4L-ARGOT-DERIV` is **absent** from `tools/gates/typed-pipeline-gate.py`; the leg is **not delivered** | the id occurs at `typed-pipeline-gate.py:536` in the admitted commit `fc13cd2`, and the sibling gate `tools/gates/argot-derivation-gate.py` (840 lines) ships `op_head2` / `op_reverse` |
| 4–6 | `Q-23-1`, `Q-23-2`, `Q-23-3` status | **in flight round 25** (claim O) | round 25 is admitted; `reports/round-25/validation.json` exists with `acceptance_checks_passed: true` |

**Row 3 is read precisely.** The status cell makes two statements and only the
first is contradicted by a byte-level measurement: the id is **not** absent
(`grep -c D4L-ARGOT-DERIV tools/gates/typed-pipeline-gate.py` → 1 at `:536`),
while "the leg is not delivered" is a **judgment about capability** that the
round-25 D seat's own `reports/round-25/argot/delta.md` argues at length (the
delivered packet has no register-scoped forms, so the leg has an empty domain).
This seat measures the id's presence and takes **no position** on whether the
capability is delivered — that question is round-26 claim D's, not this audit's.
The stale part is the factual "is absent" clause; the judgment clause is left
standing.

**Why this is not a defect in the index's design.** Each statement was true of
the bytes that existed when it was written, and the index says so for itself
("Gate-shape readings bind to a stamp … any later re-read of this index is a new
measurement"). Rows 1–2 are the class the round-25 X45 seat already recorded as
finding X45-2 and deliberately left unrepaired, and row 3 is the class the C31
seat recorded as C31-F4 (an in-flight claim must not be upgraded to delivered).
What is new here is that **round 25 closed**, which moves the whole
`in flight round 25` block into the stale set at once — the round-23 commitments
Q-23-1..3 have no disposition in the index at all.

**Control (executed, in-memory).** The G probe is a two-line predicate:
it fires when a cell declares `no \`validation.json\`` and the receipt exists,
and stays silent when the same text is scanned with `receipt_present=False`
(selftest controls `G fires when the receipt exists`,
`G stays silent when the receipt is absent`). A third control asserts the live
run actually reads the argot id out of the gate source (`G reads the argot id in
the live gate`). The probe is therefore sensitive to the named contradiction and
to nothing else; it does not fire on the five *declared-absent* tokens the index
carries in four §2 rows, because those name paths that genuinely never existed
(§4, pointer bullet).

**Disposition owner.** The index is a round-25 deliverable, so the correction is
a **new revision block** appended by whoever owns the index next (claim C's
`reports/round-26/open-questions/` disposition surface), not an edit by this
seat. This audit records the six instances with their commands so that
disposition has a measured target.

### X63-D2 — the round-25 X45 tool now reds the C35-corrected round-4 pointer (finding, informational)

Re-executed at this stamp, `reports/round-25/audit/x45-lessons-pointer-audit.py`
exits **1** with:

```
FAIL P1_pointers_resolve
findings: 1
  X45-P1 unresolved-pointer: [('round-4-sol-fixes-and-audits.md', 'reports/round-4*',
    '`corpus/lessons/round-4-audit/` (16 reports), `corpus/lessons/round-4-triage/`;
     **no `reports/round-4*` exists** (C35 correction)')]
```

The cell is **correct**: the round-25 C35 seat replaced a dead pointer
(`reports/round-4-audit`, which never existed) with the two live directories and
stated the absence of `reports/round-4*` explicitly. X45's exemption set is
`NOT_FILED_RE = not filed|no \`validation\.json\`|not round-numbered`
(`x45-lessons-pointer-audit.py:44`), which does not cover the "**no `X` exists**"
phrasing, so a *declared* absence reads as an unresolved pointer.

This is the case X45's own limits section predicted: "a pointer that names an
absent path in different words would be reported as unresolved even if the index
intended it as a known-absent pointer; the check errs toward red, which is the
safe direction for an audit." It is recorded here as a **cross-tool coverage
difference, not an index defect**: this seat's D check exempts the cell
(`DECLARED_ABSENT_RE` matches `no \`reports/round-4*\` exists`) and X45's does
not. A consumer must not read X45's red as a live broken link without reading
the cell.

## 4. Independent cross-checks (positive controls on the live file)

- **Rows ↔ files.** 26 §2 rows naming a `.md` file, 26 files in
  `corpus/lessons/`; orphan set empty, phantom set empty, duplicate set empty.
  Matches the C31 tool's `C31_index_rows_eq_files` and the round-25 census
  tool's `lesson_files: 26`.
- **Pins.** All 25 pinned rows re-derive byte-equal on `bytes`, `lines` and
  `sha8`. The two loop-era lessons that carry a prior filed auditor pin still
  reproduce it exactly — round-19 `0c975cf1…` and round-23 `b567a60a…` — which
  is the continuity control across rounds 19 → 20 → 23 → 25 → 26.
- **Shape cells.** **25/25** format cells and **25/25** contract cells match a
  live re-derivation — the format cell against the exact-`## Gate`-heading
  classifier, the contract cell against a live count of
  `source:`/`verified-at:`/`recheck:`/`scope:` lines in the file's first 14
  lines. The index's own self-row is exempt from both, on the same
  `sha8=self-referential` key that exempts it from the pin check. The histogram
  the 25 checked rows produce (gate-keeper 14 / fragment-index 5 / plain 6) is
  the round-25 C31 histogram over the filed lessons.
- **Queue.** 49 rows, 49 ids, 49 carried ids; the two sets are equal with zero
  orphans in either direction. Owners: 37 resolve to a live path, 12 are role
  tokens (`parent` 9, `operator` 3). The escaped-pipe row `Q-20-3`
  (`--profile v2\|v3`) parses correctly under the unescaped-pipe split and its
  owner `tools/exercise-handoff-e2e.py` resolves.
- **Pointers.** Every backticked path in the §2 disposition column resolves
  except **five tokens across four rows**, and each of them sits inside a cell
  that declares the path was never filed: `reports/round-1`, `reports/round-2`,
  `reports/round-3` each in a "not filed" clause, and `.ufo/l0-questions.md`
  named as the fleet-root carrier outside this repo (the round-2 cell carries
  two of the five). A sweep that red-lined them would be reading a negative
  statement as a broken link. The remaining four rows the tool reports as
  "declared absent" include the round-4 cell, whose `no \`reports/round-4*\`
  exists` wording this seat's D check exempts and the round-25 X45 check does
  not (X63-D2).
- **Subdirectory table.** §5's nine-row evidence table re-measured: 42, 43, 1,
  16, 2, 10, 12, 5, 15 files — 146 total, all nine counts exact. 172 files
  under `corpus/lessons/` recursively = 26 `.md` + 146 evidence files.
- **Prose arithmetic.** The index states `Rows: **49**` and `Rows: 26. Files:
  26.`; the measurement is 49 data rows and 26 files, so F is green. The
  round-25 runner counts **51** rows in the same block because its own
  convention counts every pipe-prefixed line (header + separator + 49 data
  rows); the two readings differ by the table's frame and both are recorded
  rather than reconciled by this seat.

## 5. What this seat did not do

- It did not write, edit or overwrite `corpus/lessons/README.md`, and it did not
  create a new revision of it. The claim-C disposition surface
  (`reports/round-26/open-questions/`) belongs to another seat; this audit
  supplies the measured targets for X63-G1 and stops there.
- It did not run `reports/round-25/run-validation.py` or
  `reports/round-26/run-validation.py`: a counting command can itself be a
  writer (round-14 established this), and those receipts are outside this seat's
  assigned paths. The runner's `measure_lessons()` convention was simulated
  **in memory** to explain the 49-vs-51 count difference, not to score the
  index.
- It did not re-execute any lesson's census commands, re-verify any lesson's
  domain claims, or adjudicate prose correctness.
- It did not touch `corpus/lessons/round-*.md` or any filed round-8–25
  artifact. The one finding whose remedy is a write (X63-G1) is routed, not
  applied.

## 6. Limits

- The staleness probe (G) is keyed to three literal shapes: `no \`validation.json\``
  in a pointer cell, `D4L-ARGOT-DERIV` + `absent` in a status cell, and
  `in flight round 25` in a status cell. A cell that states a superseded fact in
  different words is not caught. The probe errs toward silence, so a green G is
  "no instance of these three shapes", not "the index is current".
- G's remedy is a new revision of a round-25 artifact. Until that lands, the
  index continues to describe the pre-close state, and a consumer who reads the
  queue as of the index's stamp is reading history correctly; a consumer who
  reads it as of today is reading six stale cells.
- The partition is a live-wave surface. The digest `ec7469dadf87df3e…` is a
  point-in-time reading; a lesson landing after this stamp adds a row rather
  than changing one. Any later re-read is a new measurement.
- This audit admits nothing. The round-26 claims' admission belongs to the
  assigned runner (`python3 reports/round-26/run-validation.py`) and the round
  auditor.

## 7. Dated observations

### 2026-10-18T18:00:42Z — opening read

`corpus/lessons/README.md` → `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`,
29 059 B, 346 lines; `git status --porcelain` empty; `HEAD` = `1ad491a`;
`reports/round-26/` holds only `claims.json` and `targets.json`.

### 2026-10-18T18:04:42Z — settled reading and the two sibling tools re-executed

| tool | exit | result |
|---|---|---|
| `x63-lessons-audit.py --selftest` | 0 | 20/20 controls PASS |
| `x63-lessons-audit.py` | 1 | 8 PASS, `G_no_stale_readings` FAIL, 1 finding (X63-G1, six instances) |
| `c31-lessons-index-audit.py --selftest` | 0 | 28/28 PASS |
| `c31-lessons-index-audit.py` | 0 | findings 0 (all six checks PASS) |
| `x45-lessons-pointer-audit.py --selftest` | 0 | 15/15 PASS |
| `x45-lessons-pointer-audit.py` | 1 | 1 finding (X63-D2: the round-4 cell, declared-absent in other words) |

SHA-256 of the bytes of this file **before this paragraph** (16636 bytes, 271
lines), measured 2026-10-18T18:07Z:
`bc383618d31f1699183b0f852fe13f98e08d93793847232445cab50eb393ad48`.
A consumer must re-measure; any later edit supersedes it.
