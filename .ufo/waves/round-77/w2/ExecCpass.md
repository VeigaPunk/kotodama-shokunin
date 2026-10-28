# ExecCpass — ACCEPT-C-77 selftest + clean/do-nothing controls, run in isolation (round 77, wave 2)

Seat: `ExecCpass` (leaf executor, attack-only). Assignment: run the adapted claim-C
counter's `--selftest` and its clean / do-nothing controls **as staged source in an
isolated scratch copy**, inspect the counter's own receipts, and report the exact
command, exit code and whether all frozen legs are distinct. No production write.

**Verdict: GREEN for the named item.** Reproduced `SELFTEST: 37/37` (exit 0) from the
staged bytes, clean control `PASS legs=13/13` (exit 0), do-nothing landing
`FAIL legs=3/13` (exit 1), do-nothing-at-base refused `FAIL legs=0/13` (exit 2).
Both graded receipts print exactly **13** `LEG` lines with **13 distinct** names,
equal to the generated list; the frozen list (W1 skeleton and the draft prose) is
the same 13 names, no duplicate. One residual harness gap found (F1 below).

Source of truth (read-only, lane `kotodama-shokunin`):

- staged counter: `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py`
  142196 B, sha256 `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4`
  — identical to the hash `ExecAdaptC.md` reports.
- `git -C <lane> cat-file -e 211f9526:.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py`
  → exit **128** ("exists on disk, but not in '211f9526…'"); same at `HEAD`
  (`211f9526800906e0c585d878d265c37e5e090c15`). The "committed staged source" is
  therefore the on-disk staged bytes, which are **not yet tracked**; the counter
  self-reports its own sha256 in every receipt, so a later commit must keep this
  exact hash or the receipts go stale.
- no `reports/round-77/claims.json` exists yet (`reports/round-77/` holds only
  `telemetry/`), so no L1-frozen `legs[]` is present to grade against; the frozen
  lists available are the W1 skeleton and the draft prose (both compared below).

Environment: Python 3.14.8, git 2.56.0. No installs; `pacman` not run.

## Isolation

Scratch: `/fast/scratch/hyaku/kotodama-r77/ExecCpass` (never `/tmp`; deleted before
yield). The staged counter was copied there and the copy's sha256 re-checked:

```
$ cp .ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py /fast/scratch/hyaku/kotodama-r77/ExecCpass/counter/accept-c.py
$ sha256sum <staged> <copy>
5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4  …/w1/stage/ExecAdaptC/accept-c.py
5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4  /fast/scratch/hyaku/kotodama-r77/ExecCpass/counter/accept-c.py
```

All graded bytes come from fixtures the counter itself builds with `git init`
under `case_dir/lane`; `_st_build` asserts `rev-parse --show-toplevel` equals that
dir (observed: no assertion fired). `--selftest` creates
`$HYAKU_SCRATCH/kotodama-r77/selftest/<mkdtemp>` and removes it in `finally`
(the dir was empty afterwards). `grep -c '/tmp' accept-c.py` → **0** (exit 1).

## Exact commands and exits

### 1. Selftest (the named run)

```
$ cd /fast/scratch/hyaku/kotodama-r77/ExecCpass/counter
$ HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r77/ExecCpass \
  PYTHONDONTWRITEBYTECODE=1 python3 -B accept-c.py --selftest
...
SELFTEST: 37/37
$ echo $?
0
```
Raw: `w2/stage/ExecCpass/selftest.out` (37 `CASE` lines, final line
`SELFTEST: 37/37`; the shell exit code above is the measured one). A second
identical run gave the same result (`selftest-rerun.out`).

### 2. Clean and do-nothing controls (raw receipts from the counter)

Driver imports the **scratch copy** and calls the counter's own
`_st_build`/`_st_run` — the same fixture path `--selftest` uses — then prints the
counter's raw stdout, the raw `LEG`-line count, the distinct-name count, the
failing set and the verdict:

```
$ cd /fast/scratch/hyaku/kotodama-r77/ExecCpass
$ PYTHONDONTWRITEBYTECODE=1 python3 -B drive.py
GENERATED_LEGS 13 13 unique
LEGS_ORDER ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX

=== CASE clean exit 0
LEG_LINES 13 DISTINCT 13 SETS_EQUAL True
FAILING -
VERDICT ACCEPT-C-77: PASS legs=13/13

=== CASE lands-eq-freeze exit 1
LEG_LINES 13 DISTINCT 13 SETS_EQUAL True
FAILING CITEDLINES,COLLCHECK,ENTRIES,EVIDENCE,GATE,GROUND,INDEX,REJECTS,REPOINTED,ROWS
VERDICT ACCEPT-C-77: FAIL legs=3/13

=== CASE lands-eq-base exit 2
LEG_LINES 0 DISTINCT 0 SETS_EQUAL False
VERDICT ACCEPT-C-77: FAIL legs=0/13 (refused: lands … is the frozen claim base … (the do-nothing control: no data landed))
STDERR REFUSED: lands … is the frozen claim base … (the do-nothing control: no data landed)
```
Raw: `controls-driver.out`, `receipt-clean.txt`,
`receipt-do-nothing-lands-eq-freeze.txt`, `receipt-do-nothing-lands-eq-base.txt`.

Do-nothing legs, verbatim from `receipt-do-nothing-lands-eq-freeze.txt`:
`ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES` → **FAIL**;
`CENSUS SCRATCHMIRROR FROZENCFG` → **PASS**; verdict `ACCEPT-C-77: FAIL legs=3/13`.
The three survivors are the structural legs satisfied by the frozen commit itself
(census-start receipt, staged-id mirror, frozen config), so the landing data legs
are the ones that redden — a do-nothing **landing does not pass**.

### 3. Leg distinctness (three independent readings)

| reading | command | result |
|---|---|---|
| generated table | `python3 -B accept-c.py --emit-legs` (exit 0) | 13 names, JSON list, no duplicate (`emit-legs.json`) |
| W1 skeleton frozen `legs[]` | parsed `.ufo/waves/round-77/w1/stage/ExecAdaptC/claims-C.skeleton.json` | 13, 13 unique, `== generated: True` |
| draft prose | regex over `CLAIMS-DRAFT.md` "lineage legs … (13 unique)" | 13, 13 unique, `== generated: True` |
| graded receipts | raw `LEG` lines counted in clean + do-nothing runs | 13 lines, 13 distinct, set `== generated: True` |

Order is stable: `ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES
CENSUS SCRATCHMIRROR COLLCHECK FROZENCFG INDEX`, exactly one `INDEX`.

### 4. Frozen-list acceptance vs refusal (independent of `--selftest`'s summary)

Fresh fixture, mutated `reports/round-77/claims.json` at a new commit; `git -C`
always explicit and `rev-parse --show-toplevel` asserted equal to the fixture.

```
$ PYTHONDONTWRITEBYTECODE=1 python3 -B legcount2.py
CASE frozen-equal-graded    exit=0 leg-lines=13 fails=-   verdict: PASS legs=13/13
CASE frozen-dup             exit=2 leg-lines=0  verdict: FAIL legs=0/13 (refused: LEGCOUNT: … repeats the leg name(s) INDEX …)
CASE frozen-reorder         exit=2 leg-lines=0  verdict: FAIL legs=0/13 (refused: LEGCOUNT: … lists 13 legs (ROWS,ENTRIES,…) …)
CASE frozen-extra (+STAMP)  exit=2 leg-lines=0  verdict: FAIL legs=0/13 (refused: LEGCOUNT: … lists 14 legs …)
CASE frozen-missing (-INDEX) exit=2 leg-lines=0 verdict: FAIL legs=0/13 (refused: LEGCOUNT: … lists 12 legs …)
```
`legcount3.py` adds the stale-freeze shape (freeze moved after landing):
`CASE frozen-equal-stale-freeze exit=1 fails=EVIDENCE verdict: FAIL legs=12/13`
— i.e. the EVIDENCE stamp really is checked against `--freeze`; a merely-renumbered
freeze cannot ride a stale capture. `legkey.py` deletes the `legs` key entirely:
`exit=2 leg-lines=0`, `FAIL legs=0/13 (refused: claim C at freeze lacks legs)`.
Raw: `legcount-accept-refuse.out`, `legcount-stale-freeze.out`,
`legcount-absent-legs.out`.

### 5. Every leg is exercised red somewhere

`legcov.py` reads `_ST_CASES` (35 cases; the receipt's 37 = 35 + 2 leg-table
cases) and maps expected failing sets → per-leg red coverage. `never-red: []`.
Thinnest: `CENSUS` red in 1 case (`census-red`); `REJECTS` 2; `GATE` 3 but never
as the sole failing leg (couples with `EVIDENCE` in J2/alias cases). Raw:
`leg-red-coverage.out`.

## Reproducibility

Two consecutive `--selftest` runs differ **only** in the random fixture commit sha
printed inside the `lands-eq-base` refusal line (342-byte diff,
`selftest-determinism.diff`). My run against W1's `selftest-receipt.txt` differs
**only** in that same sha (`selftest-vs-w1.diff`); all other 36 `CASE` lines and
`SELFTEST: 37/37` are byte-identical.

## No production write

Read-only lane snapshot (file size + mtime, `.git` pruned) taken immediately
before and after the runs: 15833 → 15838 entries. The entire diff is five files
written by a **sibling** seat in its own stage dir —
`.ufo/waves/round-77/w2/stage/ExecCapEvidence/{capture.log,claims-rehearsal.json,
measure-s898.log,measure-s898.py,S898-candidate.txt}`. No lane production file
(`LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `corpus/**`, `reports/**`),
no git/jj/index state, no sibling lane was touched by this seat. Raw:
`lane-snapshot-before.txt`, `lane-snapshot-after.txt`, `lane-snapshot-diff.txt`.

My only lane writes: this report and `w2/stage/ExecCpass/**`.

## Findings

- **F1 (real, small) — the selftest cannot see a duplicated `LEG` line.**
  `_st_run` collects legs into a dict keyed by name (`legs[name] = PASS|FAIL`), so
  a leg that printed twice would collapse, and the verdict's `legs=13/13` count
  comes from the `LEGS` table (`run_legs` returns `len(results)`), not from the
  printed lines. On the clean and do-nothing receipts the raw-line check shows 13
  lines / 13 distinct, so this is not a live defect — but a leg function emitting a
  second `LEG` line (or a duplicated name in `LEGS`) would pass unnoticed. Cheap
  fix: assert in `_st_run`/`run_selftest` that `len(leg_lines) == len(LEGS)` and
  `len(set(names)) == len(names)`.
- **F2 — thin red coverage on two legs.** `CENSUS` has one red case; `GATE` is
  never the sole failing leg. Coverage is non-zero for all 13 (`never-red: []`),
  so this is a margin note, not a failure.
- **F3 — the staged counter is untracked** (absent at base and at `HEAD`); its
  receipts stamp `# counter sha256 (self)`. If L1 commits a modified counter, W1's
  `selftest-receipt.txt` no longer describes the committed bytes.
- **F4 — `claims-C.skeleton.json` self-declares `"status": "frozen"`** while
  nothing is installed under `reports/round-77/`. Nothing in this seat's run read
  it as config; flagging only so the freeze installs the real file rather than
  treating the stage copy as installed.
- The clean fixture is synthetic (`S004/S005`, rows 3→5, 2→3 knowledge files), so
  `PASS legs=13/13` proves the control logic and the do-nothing discrimination,
  **not** the real claim.

## Unrun (explicit)

- No graded run against a real round-77 `<freeze>`/`<lands>`: neither exists
  (`reports/round-77/` holds only `telemetry/`).
- No `/tmp`/symlink audit of the counter beyond the `grep -c '/tmp'` → 0 result;
  that is `ExecTmpAudit2`'s seat.
- No claim-C content grading (entry/rows/Gate/evidence) — `RevCounterC`,
  `MutCrows`, `Crit*` seats; this seat only ran the harness and its controls.

## Wave-2 stage artifacts

`.ufo/waves/round-77/w2/stage/ExecCpass/`: `selftest.out`, `selftest-rerun.out`,
`selftest-determinism.diff`, `selftest-vs-w1.diff`, `controls-driver.out`,
`receipt-clean.txt`, `receipt-do-nothing-lands-eq-freeze.txt`,
`receipt-do-nothing-lands-eq-base.txt`, `leg-red-coverage.out`,
`legcount-accept-refuse.out`, `legcount-stale-freeze.out`,
`legcount-absent-legs.out`, `emit-legs.json`, `counter-copy.sha256`,
`lane-snapshot-before.txt`, `lane-snapshot-after.txt`, `lane-snapshot-diff.txt`.

Scratch `/fast/scratch/hyaku/kotodama-r77/ExecCpass` deleted after staging.
