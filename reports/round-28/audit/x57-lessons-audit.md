# X57 — lessons audit (round 28)

- round 28 (operator: loop 3 of 3, build round 4 of 4 — the last build round;
  64 workers on `devin/deepseek-v4-1-flash-high` per `reports/round-28/claims.json`)
  · seat **X57** (SCRIBE X57 — lessons audit) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X57: lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  claims `baseline_revision` `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (the
  round-27 admit), lane HEAD `69cecbc7dcf575a29f29660ecac470e05260fd86`
  ("round-28: declare claims D/O/C", 2026-10-18T17:10:20−03:00 = 20:10:20Z).
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies no
  round, blesses no lesson and grants no promotion.
- writes: **this file**, the read-only tool `reports/round-28/audit/x57-lessons-audit.py`,
  and the receipts `x57-lessons-receipt.json` / `x57-lessons-selftest.json` /
  `x57-lessons-live.txt`. **No `corpus/lessons/**` byte was written or edited by
  this seat** — the filed `corpus/lessons/README.md` was read only and its Git
  blob is still `a31870556c733498243b56697896504a2fb3679a`, the declared
  `README_BASELINE_BLOB`. No filed round-8–27 artifact, tool or gate was edited;
  the round-27 predecessor tool is executed, never rewritten. No commit, no push.
- measurement window: 2026-10-18T20:11:44Z–20:18:25Z UTC (every stamp from
  `date -u --iso-8601=seconds`). `reports/round-28/` held 3 files
  (`claims.json`, `targets.json`, `scribe/x56-census.py`) when this seat opened
  and 31 files at its close — the wave produced the round-28 runner
  (`run-validation.py`) and `validation.json` inside this window, and the runner
  moved again under this seat's own readings (`a130f368…` → `0a215dc4…`, §3
  X57-G6). `corpus/lessons/`
  was stable at 28 `*.md` for the whole window (no `round-28.md` lesson exists
  yet), and the four surfaces this audit binds to (§2) did not move.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the filed index `corpus/lessons/README.md` is byte-stable at sha256 `ec7469dadf87df3e…` (29 059 B / 346 lines), blob `a3187055…` = the declared baseline — **two rounds have now run without touching it** | measured |
| 2 | the partition is **28** `*.md` files; the filed index carries **26** rows — two orphans, `round-26.md` and `round-27.md` | measured |
| 3 | the newest revision is still `reports/round-26/zzz-lessons-index-revision-4.md` (sha256 `1c4623ec…`, 27 rows); **no round-27 or round-28 revision exists** | measured |
| 4 | the newest revision omits `round-27.md` — it was written before that lesson landed, and the round-27 audit itself recorded that "a further revision is owed" | **finding X57-A2** |
| 5 | the revision's own `round-26.md` pin is still stale: it reads `bytes=46745 lines=190 sha8=cf7461fe`; the live file is **60 054 B / 222 lines / `cae06660`** | **finding X57-B2 / X57-G2** |
| 6 | the filed index's row-level cell for `round-25.md` still says "this round's own O/D/C claims are pending"; `reports/round-25/validation.json` reads `acceptance_checks_passed: true` | **finding X57-G3** |
| 7 | the filed index states `files: 26`; the partition is 28 — **both** index surfaces' prose arithmetic is now stale | **finding X57-F1** |
| 8 | **new this round:** the round-27 lesson cites `reports/round-27/audit/x57-lessons-audit.py --selftest` → **37/37** as a control; the live tool now reads **34/37**, exit 1, because three of its controls pin the pre-round-27 partition | **finding X57-G5** |
| 9 | **new this round:** the ledger has **dropped off the acceptance surface**. The round-25 and round-26 runners each grade it (43 and 34 `lessons` references, `README_BASELINE_BLOB`, the queue and its dispositions); the round-27 and round-28 runners contain **zero** references to `corpus/lessons` | **finding X57-G6** |
| 10 | the six `X63-G1` instances the round-26 auditor filed **all reproduce** on today's bytes | measured (peer, reproduced) |
| 11 | **disposition coverage is green**: 49 filed queue ids, 49 §4 rows, zero missing / extra / duplicate, every class in `{fixed, carried}`, every owner resolves | measured |
| 12 | all four peer auditors are reachable and their exit codes are recorded: `c31` selftest 0 / live 1, `x45` 0 / 1, `x63` **1** / 1, `r27x57` **1** / 1 | measured (peer, reproduced) |
| 13 | this seat's own auditor reads **52/52 controls, exit 0**, and **14/22 live checks green with 8 findings** | measured |

**One line:** the lessons ledger has been **frozen for two rounds** while the
partition grew by one — and the reason is now measured, not inferred: the round
runner **stopped grading the ledger after round 26**, so two rounds of drift
accumulated with no acceptance surface to catch them. Two new findings are filed
on top of round 27's five: a filed *lesson's* own control claim contradicted by
the bytes it cites (G5), and the dropped acceptance surface itself (G6).

## 1. Method

Read-only tool `reports/round-28/audit/x57-lessons-audit.py` (stdlib only; opens
no file for writing — the receipt is the caller's stdout redirect), run from the
lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/x57-lessons-audit.py --selftest   # 52/52, exit 0
python3 -B reports/round-28/audit/x57-lessons-audit.py              # findings, exit 1
python3 -B reports/round-28/audit/x57-lessons-audit.py --json       # receipt
```

**Why a new file rather than an edit of the round-27 tool.** The round-27 tool is
a filed artifact of round 27 and is read-only (lane rule: corrections are new
files). It is also, by its own design, *not re-runnable*: three of its 37 controls
assert the partition is 27 files and that the filed orphan set is exactly
`['round-26.md']`, so the partition move reds its selftest. This successor keeps
its probe set and generalizes the two things that broke:

- **revision resolution.** Round 27 hard-coded `reports/round-26/zzz-lessons-index-revision-4.md`.
  This tool resolves the newest revision the way the round-26 runner does
  (`find_readme_revisions()`, sorted by `(queue_ids, rows)`) but globs
  `reports/*/zzz-lessons-index-revision-*.md` — so a revision filed under
  `reports/round-28/` would be found here and is **not** found by the round-26
  runner, which globs `reports/round-26` only.
- **partition-pinned controls.** Every control that asserted 27 now asserts the
  measured 28, and the round-27 tool's own red selftest is itself a recorded
  reading (§3, X57-G5) rather than something smoothed over.

| id | question | green means |
|---|---|---|
| A1 | filed row/file set | every `.md` file has exactly one row, every row names a file, no duplicate |
| A2 | revision row/file set | same, on the newest revision |
| A3 | partition census | the partition equals the 28 measured at this stamp |
| B1 | filed pins | each row's `bytes`/`lines`/`sha8` equals the live bytes (self-row exempt) |
| B2 | revision pins | same, on the newest revision |
| B3 | shape cells | each row's `format` and `contract` cell equals a live re-derivation, on both surfaces |
| D | pointers | every backticked path resolves (brace groups expanded first), unless the cell declares the path absent |
| E / E2 | queue ↔ carried ids, owners | every carried id has a queue row and vice versa; every owner is a live path, `operator` or `parent` |
| F | prose arithmetic | **both** surfaces' stated row and file counts equal the measurement |
| G1 | the six X63-G1 instances | they reproduce exactly (the positive control for the staleness probes) |
| G2 | revision-level staleness | no cell of the newest revision is contradicted by today's bytes |
| G3 | row-level staleness | no filed §2 row's own `pending` cell is contradicted by a live receipt |
| G4 | lesson source resolvability | every repo path the newest lesson's `source:` line names resolves |
| G5 | **lesson control claims** | every `<tool> --selftest n/n` figure the newest lesson states still holds when the tool is run |
| G6 | **acceptance-surface coverage** | the round's own counting command still grades the lessons ledger |
| H | round-13 row | the skipped-round row says why no lesson file exists |
| I | disposition coverage | every filed queue id has exactly one §4 row with a usable class, owner, reason and next touch |
| J | cross-tool reproduction | the four auditors run and their exit codes are recorded |

**What this tool adds over its round-27 predecessor, named rather than assumed.**
`G4`, `G5` and `G6` are new. G4 is a resolvability probe over the *newest lesson's
own `source:` line* — 32 backticked tokens, several of them brace groups — and is
green. G5 is a probe on a lesson's own control citation: a lesson cites a tool's
selftest count as evidence that the tool was green when the lesson was written,
and the lesson is filed bytes that a later write cannot repair. Round 27's own
lesson does exactly that, and the figure it cites is now false. That is the
"control fixture pinned to a moving partition" class — the class this audit and
its two predecessors have each filed one level up — reproduced **inside a filed
lesson**. G6 steps outside the lessons tree entirely and asks the structural
question the other probes cannot: *is this ledger still on any acceptance
surface?* It reads the four loop-era round runners and reports whether each one
names `corpus/lessons`. Two do; the two that matter now do not (§3, X57-G6).

The four auditors were re-executed at this stamp as the cross-check:

| tool | selftest | live | finding |
|---|---|---|---|
| `reports/round-25/audit/c31-lessons-index-audit.py` | 28/28, exit 0 | exit 1 | `C31-1 unindexed-file: ['round-26.md', 'round-27.md']`; `C34-2 prose-arithmetic-drift` |
| `reports/round-25/audit/x45-lessons-pointer-audit.py` | 15/15, exit 0 | exit 1 | `X45-P1 unresolved-pointer` on the round-4 cell the C35 seat corrected (the standing X63-D2 cross-tool disagreement) |
| `reports/round-26/audit/x63-lessons-audit.py` | **exit 1** (three controls pin the pre-round-26 partition of 26) | exit 1 | `X63-A1`, `X63-F1`, `X63-G1` |
| `reports/round-27/audit/x57-lessons-audit.py` | **exit 1** (34/37; three controls pin the pre-round-27 partition of 27) | exit 1 | the same six findings as round 27 plus `X57-A2` |

Both red selftests are the same class and neither is a defect in the tool *as
written*: `x63`'s controls assert `len(files) == 26`, `r27x57`'s assert
`len(files) == 27`, and each was true at its own stamp. This seat records both
and takes no position on whether either filed tool should be re-pinned (that is
the parent's disposition). It is the reason this round's tool is a new file.

## 2. After-state (2026-10-18T20:18:24Z, `x57-lessons-receipt.json`)

```
filed index:      corpus/lessons/README.md
  sha256:         ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c
  blob:           a31870556c733498243b56697896504a2fb3679a  (= declared baseline)
  rows:           26
revision candidates:
  reports/round-26/zzz-lessons-index-revision-3.md
  reports/round-26/zzz-lessons-index-revision-4.md
newest revision:  reports/round-26/zzz-lessons-index-revision-4.md
  sha256:         1c4623ec2e26954853da75af9783190aa573a291a426ab3a3cf574945016f9b9
  rows:           27
lesson files:     28        queue rows: 49
  PASS A3_partition_census            FAIL A1_filed_rows_eq_files
  PASS B1_filed_pins_rederived        FAIL A2_revision_rows_eq_files
  PASS B3_shape_cells_rederived       FAIL B2_revision_pins_rederived
  PASS D_pointers_resolve             FAIL F_prose_arithmetic
  PASS E_queue_cross_consistency      FAIL G2_revision_cells_clean
  PASS E2_owners_resolve              FAIL G3_row_level_cells_clean
  PASS G1_x63_instances_reproduce     FAIL G5_lesson_selftest_claims_hold
  PASS G4_lesson_source_tokens_resolve FAIL G6_runner_still_grades_the_ledger
  PASS H_round13_row_self_describes   PASS I_disposition_coverage
  PASS J_c31 / J_x45 / J_x63 / J_r27x57
checks:           14 / 22 green
findings:         8
  X57-A1  X57-A2  X57-B2  X57-F1  X57-G2  X57-G3  X57-G5  X57-G6
```

The partition is a live-wave surface: a `corpus/lessons/round-28.md` landing
after this stamp adds a row rather than changing one, and would re-red A1/A2/F
here and C31/X63 above. A revision filed under `reports/round-28/` would change
which file §2's revision block describes and would be picked up by this tool's
`newest_revision()`.

## 3. Findings

### X57-G6 — the lessons ledger has dropped off the acceptance surface (finding, new this round)

The single most consequential reading in this round is structural, and it is why
the other findings were allowed to accumulate.

| round runner | sha256 (16) | `lessons` refs | `corpus/lessons` refs | `README_BASELINE_BLOB` | grades the ledger |
|---|---|---|---|---|---|
| `reports/round-25/run-validation.py` | `d19435251dccb738` | 43 | 9 | no | **yes** |
| `reports/round-26/run-validation.py` | `73297683d552b167` | 34 | 7 | yes | **yes** |
| `reports/round-27/run-validation.py` | `36b597068d59a881` | **0** | **0** | no | **no** |
| `reports/round-28/run-validation.py` | **moved ≥5×** inside this window (`a130f36877494060` → `0a215dc4…` → `50a735b5…` → `6f8db1d2…` → `c398bdc4…`) | **0** in every revision | **0** in every revision | no | **no** |

Command (run 2026-10-18 from the lane root, re-derived by the tool's own G6 probe):

```sh
for r in 25 26 27 28; do
  printf "round-%s: %s\n" $r "$(grep -c -i 'lessons' reports/round-$r/run-validation.py)"
done
# round-25: 43   round-26: 34   round-27: 0   round-28: 0
```

**The round-28 runner moved five times inside this seat's own window** —
`a130f368…` (95 895 B) at 20:15Z → `0a215dc4…` (101 508 B) at 20:17Z →
`50a735b5…` → `6f8db1d2…` (103 311 B) → `c398bdc4…` at 20:18Z — which is the
round-27 lesson's own "a moving tree is not one revision" class reproduced one
level down, on the runner rather than on the artifact. **The G6 reading is stable
across all five revisions: zero `corpus/lessons` references in every one.** That
stability is the point — a coverage reading that held across five rewrites is a
property of the round, not of a particular byte. A consumer must still bind G6 to
a runner sha256, which is why the receipt records one.

Round 25 built the index and graded it; round 26 built the revision, pinned the
filed blob against `README_BASELINE_BLOB`, re-derived the pins and dispositioned
the queue. Round 27's and round 28's runners do none of that — `corpus/lessons`
does not appear in either file at all, so a lesson row that goes stale, a revision
that omits a lesson, or a queue id with no disposition cannot fail either round.

**This is the mechanism, not just the symptom.** It explains, without any appeal
to neglect, why two consecutive rounds left the ledger untouched while the
partition grew by one: from round 27 onward there was no command in the round's
own `counting_command` that could red on it. Round 28's claim O asks that "every
frozen/baseline/replay surface re-verified" — the ledger is no longer on that
list, and this audit measures that it is not.

**Class: coverage regression, not a defect in any delivered artifact.** No filed
byte is wrong because of it; the ledger simply stopped being graded. It is also
the class the round-28 C claim does *not* cover: claim C is scoped to
`corpus/knowledge/linguistics` and `corpus/README.md`, not to `corpus/lessons`.

**Not dispositioned here (parent-owned):** whether the lessons index belongs on
the round runner at all, and if so whether the owed revision (§X57-A2) must land
before the ledger can be graded again. This seat measures the coverage gap and
files it; it does not decide the ledger's governance.

### X57-G5 — a filed lesson's own control claim is contradicted by the bytes it cites (finding, new this round)

The round-27 lesson states, in its own controls section
(`corpus/lessons/round-27.md:199`):

> `x61 --selftest` 21/21; `readme/sweep --selftest` 9/9; **`x57 --selftest` 37/37**

and again at line 121, listing the regressions it ran green. The tool was 37/37
at the lesson's own 19:28Z stamp. It is not now:

| surface | the cell says | measured now |
|---|---|---|
| `corpus/lessons/round-27.md:199` | `x57 --selftest` **37/37** | **34/37**, exit 1 |
| `corpus/lessons/round-27.md:121` | the same tool, listed green | the same, red |

Command and control (run 2026-10-18 from the lane root):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest   # exit 1, 34/37
```

The three red controls are exactly the partition-pinned ones:

```
FAIL partition is 27 md files                     | observed: 28
FAIL filed orphan is exactly round-26.md          | observed: ['round-26.md', 'round-27.md']
FAIL revision has no orphan                       | observed: ['round-27.md']
```

**Class: honest-at-stamp, superseded** — and, unlike the six `X63-G1` instances,
**unrepairable**, because the lesson is filed bytes. Round 27's own X57 audit
already stated the successor reading for its partition count ("the row set this
audit measured (27 files) becomes 28 and a further revision is owed"); what was
not anticipated is that the *lesson's own control citation* would be the thing
that went stale.

The three other selftest figures the lesson cites **still hold**, which is the
negative control that makes this probe mean something: `argot-derivation-gate.py`
27/27 (exit 0), `readme/sweep.py` 9/9 (exit 0), `x61-pin-sweep.py` 21/21
(exit 0). The probe fires on the one claim that moved, not on the four that
did not. Note also that `x59-register-law-negatives.py --controls` (8/8 caught)
is cited by the lesson and is correctly **not** counted by this probe: `x59`
takes `--controls`, not `--selftest`.

### X57-A2 — the newest revision omits `round-27.md` (finding, new this round)

`reports/round-26/zzz-lessons-index-revision-4.md` carries 27 rows for what is
now a 28-file partition. `round-27.md` (54 972 B / 203 lines / `f15e285b`,
gate-keeper, committed by `6c0ac44`) has **no row on either surface**.

Round 27's X57 audit predicted exactly this and named it as the successor's to
carry (`reports/round-27/audit/x57-lessons-audit.md` §6: "if a
`corpus/lessons/round-27.md` lesson lands, the row set this audit measured
(27 files) becomes 28 and a further revision is owed"). It landed at 16:30:29−03:00,
**before** the round-27 admit commit `6c0ac44` at 17:09:19−03:00, and no
revision followed. Round 28 has now run its whole build round without one either.

**Consequence for the round-26 runner.** `find_readme_revisions()`
(`reports/round-26/run-validation.py:1357-1372`) globs `reports/round-26` only
and takes the last candidate by `(queue_ids, rows)`. It still resolves rev-4, and
it still fails on it: `orphans` is non-empty, so its `"the new revision omits N
lesson file(s)"` branch fires. That runner was not executed here against the live
tree (no round-28 tree to grade it against); the reading is from its source and
from this tool's equivalent computation.

### X57-B2 / X57-G2 — the newest revision's own pin is still stale (finding, carried)

Unchanged from round 27 — no revision has been filed since, so the reading stands:

| surface | the cell says | measured now |
|---|---|---|
| rev-4 §1 row `round-26.md` | `bytes=46745 lines=190 sha8=cf7461fe` | 60 054 B / 222 lines / `cae06660` |
| rev-4 §1 row `round-25.md` | "round-25 claims pending, not carried" | `reports/round-25/validation.json` exists, `acceptance_checks_passed: true` |
| rev-4 §1 row `round-26.md` | "its claims are pending, not carried" | `reports/round-26/validation.json` exists, `acceptance_checks_passed: true` |
| rev-4 §4 disposition `Q-18-3` | next touch **round 26** | round 26 closed at `4f09c99`; its receipt reads `true` |

**Class: honest-at-stamp, superseded.** Every cell was true of the bytes that
existed at the revision's 18:23Z stamp; the round-26 close commit `4f09c99`
(19:10:02Z) amended `round-26.md` from 46 745 B / 190 lines to 60 054 B / 222
lines. Note the asymmetry this round adds: the revision's `round-25.md` pin
(`bytes=38520 lines=205 sha8=08f0337e`) **still re-derives**, and so does every
other pinned row except `round-26.md` — B1 on the filed index is 25/25 green.
The drift is one row, and it is the row the close commit moved.

### X57-G3 — the filed index's row-level `pending` cell is stale (finding, carried)

Same class, same row, same bytes as round 27: the filed §2 cell for `round-25.md`
reads "— (this round's own O/D/C claims are pending, not carried)". It was true
when the index was written (rev 2, 17:47Z); the round-25 admit landed at
17:58:37Z. `X63`'s `G` probe does not reach this cell (it probes the disposition
pointer and queue-status columns), which is why this tool keeps G3.

### X57-A1 / X57-F1 — both index surfaces are behind the partition (known, widened)

- **Filed index (A1/F1):** 26 rows and `files: 26` against a 28-file partition.
  Orphans are `['round-26.md', 'round-27.md']`. Correct at its own 17:48Z stamp;
  two lesson files have landed since.
- **Newest revision (A2/F1):** 27 rows and `Rows: 27. Files: 27.` against 28.
  Orphan is `['round-27.md']`. Correct at its own 15:23−03:00 stamp.

F1 fires on **both** surfaces this round, where round 27's F fired on the filed
index only. No correction is filed: a filed byte is read-only, and the successor
reading (28 rows) does not yet exist anywhere — it is the revision both this
audit and round 27's handoff say is owed.

## 4. What is green

- **Filed pins (B1):** 25/25 pinned rows re-derive exactly on the live bytes; the
  26th is the self-row, exempt by construction.
- **Shape cells (B3):** every `format` and `contract` cell of both surfaces
  re-derives. The live histogram over the 28 files is **gate-keeper 16 /
  fragment-index 5 / plain 6 / index 1**; the revision's own stated histogram
  (gate-keeper 15 + fragment-index 5 + plain 6 = 26 lesson files + self-row = 27)
  is correct *as of its partition* and is off by exactly the one gate-keeper
  lesson that landed after it.
- **Pointers (D):** every disposition pointer resolves, or its own cell declares
  the path was never filed (5 such token rows across 4 lesson rows, all honest). This round the probe also
  brace-expands group tokens such as `reports/round-27/law/{design,rules,review}.md`
  and `reports/round-27/scribe/{…}` before testing them, so a shorthand is not
  mistaken for a path; the count of unresolved pointers is still **0** on both
  surfaces.
- **Queue (E/E2):** 49 queue rows, 49 carried ids, zero orphans in either
  direction; all 49 owners resolve (37 path, 12 role token).
- **Disposition coverage (I):** 49 queue ids ↔ 49 §4 disposition rows; zero
  missing, extra or duplicate; classes `{fixed: 32, carried: 17}`, all in
  vocabulary; every owner resolves; every `carried` row carries `reason:` and a
  next-touch round. Re-verified here on today's bytes, not inherited from rev-4's
  prose — and unchanged from round 27, which is itself the reading: the
  disposition ledger was correct and nothing has disturbed it.
- **Lesson source resolvability (G4):** all 32 backticked repo paths on the
  round-27 lesson's `source:` line resolve, brace groups included. The lesson is
  a good pointer file.
- **G1:** the six `X63-G1` instances reproduce under their exact six names, which
  is the positive control that makes the G2/G3/G5 probes mean something.

**What is notably *not* green, and why that is the round's reading:** the ledger
is measured here by an auditor the round did not name, because the round's own
counting command no longer reads it at all (X57-G6). Everything green above is
green *on this seat's instrument*; none of it is green on `reports/round-28/run-validation.py`.

## 5. Controls

`--selftest` is **52 in-memory controls, exit 0**. One surface per control:

- **positive controls (live readings):** partition 28; filed rows 26; revision
  rows 27; filed pins clean; revision pins drift on exactly `round-26.md`; filed
  orphans exactly `['round-26.md', 'round-27.md']`; revision orphan exactly
  `['round-27.md']`; filed queue 49; the six G1 instances reproduce under their
  exact six names; the round-27 lesson classifies as gate-keeper; the round-27
  lesson is the newest; G4 green on it; G6 reads all four loop-era runners and
  records rounds 25–26 as grading the ledger.
- **negative controls (a probe must stay silent):** G1 silent when the
  claimed-absent receipt is absent; G3 silent when the round's receipt is absent;
  G2 §4 silent on a revision whose whole next-touch column names only round 99;
  D exempts a declared-absent pointer; E2 accepts `operator`/`parent` as role
  tokens and fires on a fabricated path owner; **G5 counts a claim that still
  holds as not-stale** (the three other selftest figures the round-27 lesson
  cites), which is what separates a staleness probe from a probe that reds
  everything; G6 stays silent on a fabricated runner body that does not name
  `corpus/lessons`.
- **mutation controls (a probe must fire):** A1 fires on a deleted filed row;
  A2 fires on a revision that omits a lesson file; B2 fires on a falsified
  revision pin; D fires on an undeclared dead pointer; E fires on a dropped queue
  row; F fires on drifted prose; I fires on a dropped disposition row and on an
  out-of-vocabulary class; G4 fires on a fabricated dead source token and
  brace-expands a group token correctly; G5 finds the round-27 lesson's stale
  claim and records the measured figure; G6 fires on a runner body that names
  `corpus/lessons`.
- **cross-tool controls:** J records all four peers with a live exit code, and
  both peers' own red selftest states (`x63` pinned to 26, `r27x57` pinned to 27)
  are recorded rather than smoothed over.

Two probe defects were repaired during this seat's run rather than shipped
vacuous, and both were caught by their own controls rather than by inspection:
the G5 attribution first read `--selftest` as sitting *outside* the backtick span
and attributed `tools/check-gate-battery.py` and `readme/sweep.py` to figures that
belong to other tools, and its observed-figure parser first accepted only the
JSON spelling `"passed": n` and not the `selftest: n/n checks passed` spelling
that three of the four cited tools actually print. Both now parse the two
spellings the lesson uses, and the repaired probe reports the three holding
claims as holding.

The tool was also run repeatedly at this stamp. Its readings are **deterministic
across every re-run on the lessons surfaces** — the same 8 findings, the same 14/22
checks, the same digests — and the only field that moved between runs was
`runner_coverage.runners['reports/round-28/run-validation.py'].sha256`, because
the wave was rewriting that runner underneath this seat (§3, X57-G6). That is the
control that separates the two: a probe whose *findings* are stable while the
byte it reads is moving is measuring the tree, and the `observed_at_utc` plus the
runner sha256 are the two fields a consumer must not compare across runs.

## 6. Boundary record

- **Writes:** this file, `reports/round-28/audit/x57-lessons-audit.py`,
  `x57-lessons-receipt.json`, `x57-lessons-selftest.json`, `x57-lessons-live.txt`.
  Every scratch artifact lives under `.scratch/x57r28/` (gitignored) with
  `export TMPDIR=$PWD/.scratch` before each scratch-writing command. **No
  `corpus/lessons/**` byte was written or edited**; no filed round-8–27 artifact,
  tool or gate was edited; the round-27 predecessor tool was executed, never
  rewritten; no historical round validator was run against the live tree. No
  commit, no push.
- **Known limit:** this audit is a point-in-time measurement of the digests in
  §2. The partition and both index surfaces are live-wave surfaces; a later write
  invalidates §0/§2 without making any row here wrong. The revision's §4
  dispositions are re-checked for **shape** (class, owner, reason, next touch) and
  for the four staleness instances named above; this seat does **not** re-run
  every one of the 49 evidence probes the C41–C46 seats authored. G5 executes
  four tools; a tool that hangs would hit the probe's 240-second timeout and be
  recorded with `observed: null` rather than silently passing.
- **Not dispositioned here (parent-owned):** **whether the lessons ledger belongs
  on the round runner at all (X57-G6)**; whether to land the owed revision (now
  two rounds behind, with one further lesson file to add); whether to land a
  revision block **inside** the filed `corpus/lessons/README.md`; whether to
  re-pin the round-26 `x63` and round-27 `x57` auditors' partition-pinned
  controls, or to accept that a filed tool's selftest is a stamp-bound reading;
  the round-19 path collision (Q-19-1); and the standing cross-tool disagreement
  X63-D2 (the round-25 X45 pointer tool reading red on the round-4 cell the C35
  seat corrected).
- **Handoff to the round-28 C seat / parent.** If a `corpus/lessons/round-28.md`
  lesson lands, the partition becomes 29 and the owed revision grows by a row
  again; if the owed revision is filed, this tool picks it up automatically
  (§1) provided it is named `zzz-lessons-index-revision-*.md` under some
  `reports/round-*/` directory. The successor readings in §3 are the ones to
  carry, not the filed index's or rev-4's stale cells. **Two new classes for the
  parent's attention:** (i) a lesson's own `--selftest n/n` citation is a control
  that a later write can falsify, and filing the lesson freezes the falsified
  figure in place — round 27's lesson is the first instance; and (ii) the ledger
  is no longer graded by the round's own counting command, so unless it is put
  back on that surface (or a standing lessons auditor is named in the runner),
  the drift this audit measures will keep accumulating unwatched.

X57 lessons audit (2026-10-18, round 28). Re-pins and corrections land as new
rows or new files, never as an in-place rewrite of a filed byte.
