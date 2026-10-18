# X45 — lessons-index pointer and prose audit (round 25)

- round 25 (operator: loop 3 of 3, build round 1 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-25/claims.json`) · seat
  **X45** (SCRIBE X45 — lessons audit) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X45: lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  claims `baseline_revision` `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` (round-24
  admit), HEAD `f74fc94` (round-25 declaration).
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies no
  round, blesses no lesson, and grants no promotion.
- writes: **this file**, its read-only tool
  `reports/round-25/audit/x45-lessons-pointer-audit.py` and the receipt
  `reports/round-25/audit/x45-lessons-pointer-receipt.json`. **No
  `corpus/lessons/**` byte was written or edited by this seat** — in particular
  `corpus/lessons/README.md` is another seat's deliverable and this seat did not
  touch it. No filed round-8–24 artifact, tool or gate was edited. No commit, no
  push.
- measurement window: 2026-10-18T17:26:27Z–17:38:36Z UTC. The wave was live
  throughout; `corpus/lessons/README.md` moved through **at least eight
  revisions** inside this window (see §C-2) and `corpus/lessons/round-25.md`
  through several more. Every reading below is bound to the digest named beside
  it.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | `corpus/lessons/README.md` did **not** exist at this seat's first read (17:26:27Z); it landed from a sibling C seat at 17:27:23Z local and was rewritten eight times inside the window | measured (before-control) |
| 2 | the index's §2 table is structurally correct: **26 rows for 26 files**, no orphan, no ghost, no duplicate; the C seat's own tool (`c31-lessons-index-audit.py`) reads its four structural checks green | measured |
| 3 | **two disposition pointers name paths that do not exist** — `reports/round-4-audit` and `reports/round-4-triage` on the `round-4-sol-fixes-and-audits.md` row; the real directories are `corpus/lessons/round-4-audit` / `corpus/lessons/round-4-triage` | **finding X45-1** |
| 4 | **two disposition pointers are stale** — the `round-12.md` and `round-21.md` rows say "no `validation.json`", but both receipts are on disk and both read `acceptance_checks_passed: true` | **finding X45-2** |
| 5 | the index's §4 arithmetic self-corrected inside the window and now matches the measurement (49 queue rows, 23 of 26 rows carrying a question) | measured (cleared) |
| 6 | every open-question id a §2 row claims to carry exists as a §4 queue row and vice versa (49↔49, zero orphans both directions) | measured |
| 7 | the C seat's own tool is **red at this stamp** on a pin-drift class the C seat cannot avoid: `round-25.md` is still being written, so its row's `bytes`/`lines`/`sha8` cannot be stable | measured (live-wave fact) |

## 1. Method

The sibling C seat's tool answers four structural questions: rows==files, owners
resolve, formats documented, pins re-derived. It deliberately does **not** read
the index's `disposition pointer` column, and it does not compare the index's
prose counts against the live partition. This seat audits those two surfaces, so
that the two tools together cover the index rather than duplicating each other.

Read-only tool `reports/round-25/audit/x45-lessons-pointer-audit.py` (stdlib
only; opens no file for writing — the receipt is the caller's stdout redirect),
run from the lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py --selftest  # 15/15, exit 0
python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py             # pointer + prose checks
python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py --json      # receipt
```

| id | question | green means |
|---|---|---|
| X45-P1 | pointers resolve | every path a disposition pointer names exists on disk, **unless** the pointer's own prose declares the path was never filed (`not filed`, `no validation.json`, `not round-numbered`) |
| X45-P2 | prose counts == measurement | every `N of M` ratio in §2/§4 that is about the partition equals the live file/row count |
| X45-P3 | queue cross-consistency | every id a §2 row claims to carry has a §4 row, and every §4 row is claimed by some §2 row |

The P1 "declared absent" exemption is the whole point of the check: an index
whose pointer says "`reports/round-1` not filed; record is `LOG.md`" is honest,
and a checker that red-lined it would punish the disclosure. The exemption is
keyed to the pointer's own words, so a pointer that silently names a
non-existent path is still caught.

## 2. Before-control (the red state)

`corpus/lessons/README.md` did not exist at this seat's first read
(2026-10-18T17:26:27Z): `ls corpus/lessons/*.md | wc -l` returned **24** and the
directory held no index. That is the claim's before-state, measured. The file
appeared at 17:27:23Z local (21368 B), landed by a sibling C seat claiming
`R25-C31..C34` with its own tool at
`reports/round-25/audit/c31-lessons-index-audit.py`.

## 3. After-state (2026-10-18T17:38:36Z, `x45-lessons-pointer-receipt.json`)

```
index:        corpus/lessons/README.md
sha256:       ee2a15dff30e7edf352c4c87dd525f5fe414ad511931bf5caeb6fece0d172154
lesson files: 26
index rows:   26
queue rows:   49
carry rows:   23
  FAIL P1_pointers_resolve
  PASS P2_prose_counts
  PASS P3_queue_cross_consistency
findings:     1
  X45-P1 unresolved-pointer: [('round-4-sol-fixes-and-audits.md','reports/round-4-audit', ...),
                              ('round-4-sol-fixes-and-audits.md','reports/round-4-triage', ...)]
```

The digest `ee2a15df…` was stable across three reads spanning ~75 s at the
window's end. A consumer must re-measure: the partition and the index are both
live-wave surfaces.

## 4. Findings

### X45-1 — two disposition pointers name paths that do not exist (finding)

The `corpus/lessons/round-4-sol-fixes-and-audits.md` row carries the
disposition pointer

```
`reports/round-4-audit`, `reports/round-4-triage`
```

Neither path exists:

```
$ ls -d reports/round-4-audit reports/round-4-triage
ls: cannot access 'reports/round-4-audit': No such file or directory
ls: cannot access 'reports/round-4-triage': No such file or directory
$ ls -d corpus/lessons/round-4-audit corpus/lessons/round-4-triage
corpus/lessons/round-4-audit  corpus/lessons/round-4-triage
```

The round-4 audit and triage material lives under `corpus/lessons/`, not under
`reports/`. `git log --all --diff-filter=A --name-only | grep -c '^reports/round-4'`
returns **0** — no `reports/round-4*` path has ever been filed in this repo, so
this is not a rename that broke a pointer; the pointer names a location that
never existed. The same row's own §4 entry for Q-04-4 names the **correct** path
(`corpus/lessons/round-4-audit`), so the index already knows the right answer
one section later.

**Why the sibling tool does not catch this.** `c31-lessons-index-audit.py` checks
the pin columns, the owner column, the format class and the row↔file relation.
It never parses the `disposition pointer` cell, so a pointer can name any string
at all and all five of its checks stay green. That is a coverage gap between the
two tools, not a defect in either — this seat's P1 exists to close it.

**Control (executed).** A mutant of the index in `.scratch/x45/README.fixed.md`
with only those two tokens rewritten to `corpus/lessons/round-4-audit` /
`corpus/lessons/round-4-triage` drives this tool green on all three checks
(`P1 True, P2 True, P3 True`, findings 0) while leaving the live file untouched.
The check is therefore sensitive to exactly the named defect and to nothing else.

### X45-2 — two disposition pointers are stale against receipts now on disk (finding, informational)

The index says:

| row | pointer text | measured now |
|---|---|---|
| `round-12.md` | `` `reports/round-12` (no `validation.json`; provisional, no admission) `` | `reports/round-12/validation.json` exists, `acceptance_checks_passed: true`, baseline `a3f6fcef…` |
| `round-21.md` | `` `reports/round-21` (no `validation.json` at the lesson's stamp) `` | `reports/round-21/validation.json` exists, `acceptance_checks_passed: true`, baseline `35b6797b…` |

Both statements were **true at the lesson's own stamp** — `round-12.md:7` says
its final listing found no `validation.json`, and `round-21.md`'s recheck line
tells the reader to read the runner's receipt "only after it appears". The
round-12 receipt is dated 2026-10-17T20:36:46Z and the round-21 receipt
2026-10-18T11:36:51Z, both **after** their lessons were written, and `LOG.md`
records both rounds as admitted (`LOG.md:3031`, `LOG.md:3286`).

So this is not an error of fact; it is an index that quotes a *point-in-time
absence* as if it were the current state. The honest reading of the
`round-12.md` row today is "the lesson is provisional; the round was admitted
later and the receipt now exists". The row for `round-21.md` is closer to
correct because it names its stamp, but a reader who stops at the pointer column
will still conclude no receipt exists.

This finding is **informational**, not a red: my tool exempts both pointers
under the "declared absent" rule and does not fail on them. It is recorded
because the index's own §5 note ("A lesson is not a verdict … points each row at
a *disposition pointer*, not at a verdict") sets an expectation that the pointer
is the place to learn the round's disposition, and for these two rounds the
pointer currently points at a superseded state.

### X45-3 — the index's §4 arithmetic self-corrected inside the window (measured, cleared)

At 17:27:45Z the §4 block read "Rows: **48**. Distinct lessons contributing: 22
of 24" while its own table already held 49 rows; at 17:29:18Z it read "49 … 23
of 24". At the final revision (`ee2a15df…`) it reads:

```
Rows: **49**. Of the 26 index rows, **23 carry at least one question**;
```

This seat independently measured **49** queue rows and **23 of 26** rows
carrying a question (`README.md` self-row, `round-1-gates-and-triage.md` and
`round-25.md` carry none). The statement now matches. P2 is green. The drift
that existed mid-window is recorded because the sibling C seat's own C-2 finding
(`reports/round-25/lessons/C25-C30.md`) measured the same class, and because a
consumer reading the index at the 17:27:45Z digest would have been misled.

## 5. Independent cross-checks (positive controls on the live file)

- **Rows ↔ files.** 26 §2 rows naming a `.md` file, 26 files in
  `corpus/lessons/`; orphan set empty, ghost set empty. Matches the sibling
  tool's C31 and the sibling census tool's `lesson_files: 26`.
- **Queue ↔ carried ids.** Expanding every range cell in §2 (`Q-02-1..4`,
  `Q-04-1..4`, `Q-11-1..3`, `Q-12-1..3`, `Q-18-1..3`, `Q-20-1..4`, `Q-22-1..3`,
  `Q-23-1..3`) yields **49** ids; the §4 table holds **49** rows; the two sets
  are equal with **zero** orphans in either direction. This is a stronger
  relation than either tool checks alone — it proves the "open-questions
  carried" column and the queue are the same population.
- **Owner resolution.** Under this seat's parser (which splits on unescaped
  pipes, as the C seat's own fixed tool does): 49/49 owners resolve — **37**
  to a live path, **12** to a role token (`parent` 9, `operator` 3). The one
  row that a naive `split("|")` mis-parses is `Q-20-3`, whose question cell
  contains an escaped pipe (`--profile v2\|v3`); parsed correctly its owner is
  `` `tools/exercise-handoff-e2e.py` ``, a live path.
- **Contract-line column.** All 26 rows' `N/4` cells match a re-derivation from
  each file's first 14 lines (rounds 1–4 at 0/4, round 16 at 3/4, loop-era files
  at 3/4 or 4/4). No mismatch.
- **The two continuity pins** named by earlier rounds still reproduce: round-19
  `0c975cf1…` and round-23 `b567a60a…`.

## 6. What this seat did not do

- It did not write, edit or overwrite `corpus/lessons/README.md`. Two sibling C
  seats and this seat all read the same path; only the C seats write it. The
  `README.md` row inside the index (`bytes=0 lines=0 sha8=self-referential`) is
  the C seat's own self-row and is exempt from my P1 by construction (it names
  no path).
- It did not run `reports/round-25/run-validation.py`: that runner writes
  `reports/round-25/validation.json`, which is outside this seat's assigned
  paths (round-14 established that a counting command can itself be a writer).
  The C-leg regexes were therefore simulated **in memory** against the index
  bytes: `LESSONS_ROW_RE` parses 26/26 rows with no orphan or phantom, all three
  `CENSUS_FORMATS` appear, the open-question section is found with 51
  pipe-prefixed lines in it, a counting command is present, and the runner's
  `declared_count` regex matches no `total … files` phrase at all (so its
  declared-count check is vacuous on this text). That last point is recorded as
  an observation, not a claim: the runner may score the index differently than
  this simulation, and the runner's receipt is the authority.
- It did not re-execute any lesson's census commands, re-verify any lesson's
  domain claims, or adjudicate prose correctness.

## 7. Limits

- P1's "declared absent" exemption is keyed to a small phrase set (`not filed`,
  `no validation.json`, `not round-numbered`). A pointer that names an absent
  path in different words would be reported as unresolved even if the index
  intended it as a known-absent pointer; the check errs toward red, which is the
  safe direction for an audit.
- P2 only fires on `N of M` ratios whose denominator equals the live file count
  or row count. A prose count written as a bare number ("Rows: 49") is not
  checked by P2 — the sibling tool's `C34b_prose_arithmetic` covers that shape,
  and the two checks are complementary rather than overlapping.
- The partition is a live-wave surface. `corpus/lessons/round-25.md` was written
  throughout this window and `corpus/lessons/README.md` was rewritten eight
  times; the digest `ee2a15df…` is a point-in-time reading. Any later re-read is
  a new measurement, and a lesson landing after this stamp adds a row rather than
  changing one.
- This audit admits nothing. Claim C's admission belongs to the assigned runner
  (`python3 reports/round-25/run-validation.py`) and the round auditor.

## 8. Dated observations

### 2026-10-18T17:26:27Z — opening read: the index does not exist

`ls corpus/lessons/*.md | wc -l` → 24; `ls corpus/lessons/` held no `README.md`.
`git rev-parse HEAD` → `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.

### 2026-10-18T17:27:23Z–17:38:36Z — the index lands and is rewritten eight times

| stamp (local) | bytes | sha256 (first 16) |
|---|---|---|
| 17:27:23 | 21368 | — |
| 17:28:15 | 21443 | — |
| 17:29:06 | 22065 | `c1af089541a6c8f6` |
| 17:30 | 22260 | `b1a994027a601b09` |
| 17:31 | 22806 | — |
| 17:32 | 23954 | `6a5160e2c2c02c5f` |
| 17:35 | 24480 | `05adf044fc2d0a9c` |
| 17:36 | 24630 | `ca64b246f883a359` |
| 17:36–17:38 | 25081 | **`ee2a15dff30e7edf`** (stable ≥3 min) |

Inside the same window `corpus/lessons/round-25.md` landed and then grew
(26897 B → 38296 B → 37555 B across three reads), and two sibling audit
fragments (`x47-argot-negatives`, `x48-v3-supersession`) landed in this
directory.

### 2026-10-18T17:38:36Z — the sibling C tool is red on a live-wave pin

`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` at this stamp
exits **1** with

```
FAIL C34_pins_rederived
findings:      1
  C34-1 pin-drift: [('round-25.md', 'bytes', '26897', 37555),
                    ('round-25.md', 'lines', '150', 205),
                    ('round-25.md', 'sha8', 'feccf068', '3b84ecf9')]
```

This is the C seat's own tool red-lining the index's own round-25 row: the row
pinned `round-25.md` at one revision and the lesson kept being written. It is a
**live-wave fact, not a defect in the index's design** — the index's §5 note
says exactly this ("a lesson landing after this stamp adds a row rather than
changing one"), and the remedy is a re-pin of that one row at close, not a
change to the check. Recorded here because the C seat's own md file
(`reports/round-25/audit/c31-lessons-index-audit.md`) claims "findings: 0" at
its 17:2xZ stamp; at the later stamp the same tool reads 1. A consumer must
re-run the tool rather than quote either receipt.

SHA-256 of the bytes of this file **before this paragraph**, measured
2026-10-18T17:38:36Z:
`707d92f1b15982378a6cd93001f18a6818e3a8d37fc86c762dc364bacb277db1`
(16582 bytes, 297 lines). Any later edit supersedes it and a consumer must
re-measure rather than inherit.
