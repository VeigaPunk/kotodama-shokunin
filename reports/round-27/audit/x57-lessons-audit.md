# X57 — lessons audit (round 27)

- round 27 (operator: loop 3 of 3, build round 3 of 4; 64 workers on
  `devin/deepseek-v4-1-flash-high` per `reports/round-27/claims.json`) · seat
  **X57** (SCRIBE X57 — lessons audit) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X57: lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  claims `baseline_revision` `4f09c990d4c17f23b5e2cda0871f81db875635fc` (round-26
  admit), HEAD `b95fca1` (round-27 declaration, 2026-10-18T16:12−03:00).
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies no
  round, blesses no lesson, and grants no promotion.
- writes: **this file**, its read-only tool
  `reports/round-27/audit/x57-lessons-audit.py` (36 947 B) and the two receipts
  `x57-lessons-receipt.json` / `x57-lessons-selftest.json`. **No
  `corpus/lessons/**` byte was written or edited by this seat** — the filed
  `corpus/lessons/README.md` was read only, and its Git blob is still
  `a31870556c733498243b56697896504a2fb3679a`, the round-26 runner's declared
  `README_BASELINE_BLOB`. No filed round-8–26 artifact, tool or gate was edited.
  No commit, no push.
- measurement window: 2026-10-18T19:12:09Z–19:15:44Z UTC, every stamp from
  `date -u --iso-8601=seconds`. The wave was live throughout: `reports/round-27/`
  grew from 3 files to 13 during this seat's reads, and `corpus/lessons/` was
  stable at 27 `*.md` for the whole window (no `round-27.md` lesson exists yet).

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the filed index `corpus/lessons/README.md` is byte-stable at sha256 `ec7469dadf87df3e…` (29 059 B / 346 lines) and blob `a3187055…` = the declared baseline | measured |
| 2 | the partition is **27** `*.md` files; the filed index carries **26** rows — one orphan, `round-26.md` (the round-26 gate-keeper lesson, committed at `4f09c99` 19:10Z, after the index's 17:48Z stamp) | measured |
| 3 | the **newest revision** `reports/round-26/zzz-lessons-index-revision-4.md` is the one the round-26 runner grades (`find_readme_revisions()[-1]` over two candidates); it carries **27 rows**, zero orphan, zero phantom | measured |
| 4 | the filed index's **25 pinned rows all re-derive** on the live bytes; the 26th is its own self-row, exempt by construction | measured |
| 5 | **the newest revision is itself stale on one row**: its `round-26.md` pin reads `bytes=46745 lines=190 sha8=cf7461fe`; the live file is **60 054 B / 222 lines / `cae06660`** | **finding X57-B2 / X57-G2** |
| 6 | the filed index's row-level cell for `round-25.md` still says **"this round's own O/D/C claims are pending"**; `reports/round-25/validation.json` exists and reads `acceptance_checks_passed: true` | **finding X57-G3** |
| 7 | the revision's §4 `Q-18-3` disposition names **"next touch round 26"**; round 26 closed at `4f09c99` and `reports/round-26/validation.json` reads `true` | **finding X57-G2** |
| 8 | the six `X63-G1` instances the round-26 auditor filed **all reproduce** on today's bytes (2 defect-class pointers, `Q-04-1`'s "absent" clause, `Q-23-1..3`'s "in flight round 25") | measured (peer, reproduced) |
| 9 | **disposition coverage is green**: 49 filed queue ids, 49 §4 rows, zero missing / extra / duplicate, every class in `{fixed, carried}`, every owner resolves, every `carried` row carries a reason and a next-touch round | measured |
| 10 | the filed index's prose arithmetic is stale in one cell: it states `files: 26` while the partition is 27 | **finding X57-F1** |
| 11 | all three peer lessons auditors are reachable and their exit codes are recorded: C31 `1` (2 findings), X45 `1` (1 finding), X63 `1` (3 findings) | measured (peer, reproduced) |
| 12 | this seat's own auditor reads **37/37 controls, exit 0**, and **12/17 live checks green with 5 findings** | measured |

## 1. Method

Read-only tool `reports/round-27/audit/x57-lessons-audit.py` (stdlib only; opens
no file for writing — the receipt is the caller's stdout redirect), run from the
lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest   # 37/37, exit 0
python3 -B reports/round-27/audit/x57-lessons-audit.py              # findings, exit 1
python3 -B reports/round-27/audit/x57-lessons-audit.py --json       # receipt
```

| id | question | green means |
|---|---|---|
| A1 | filed row/file set | every `.md` file has exactly one row, every row names a file, no duplicate |
| A2 | revision row/file set | same, on the newest revision |
| B1 | filed pins | each row's `bytes`/`lines`/`sha8` equals the live bytes (self-row exempt) |
| B2 | revision pins | same, on the newest revision |
| B3 | shape cells | each row's `format` and `contract` cell equals a live re-derivation, on both surfaces |
| D | pointers | every backticked path in a disposition pointer resolves, unless the cell declares the path absent |
| E / E2 | queue ↔ carried ids, owners | every carried id has a queue row and vice versa; every owner is a live path, `operator` or `parent` |
| F | prose arithmetic | the index's stated row and file counts equal the measurement |
| G1 | the six X63-G1 instances | they reproduce exactly (the positive control for the staleness probe) |
| G2 | **revision-level staleness** | no cell of the newest revision is contradicted by today's bytes |
| G3 | **row-level staleness** | no filed §2 row's own `pending` cell is contradicted by a live receipt |
| H | round-13 row | the skipped-round row says why no lesson file exists |
| I | **disposition coverage** | every filed queue id has exactly one §4 row with a usable class, owner, reason and next touch |
| J | cross-tool reproduction | the three peer auditors run and their exit codes are recorded |

**What this tool adds over the round-26 X63 auditor, named rather than assumed.**
X63 audits the **filed** index only; this tool audits **both** surfaces — the
filed index *and* the newest revision, which is what the round-26 runner grades.
That difference is what surfaces X57-B2/G2: the revision's own pins were correct
at its 18:23Z stamp and were invalidated 47 minutes later by the round-26 close
commit, and no round-26 probe re-read them. X63's `G` probe covers the six
filed-index instances; this tool keeps that as its positive control (G1) and adds
G2 (revision cells) and G3 (row-level cells). `I` is new: X63 checked the
**filed** queue's internal consistency, not whether every queue id has a usable
**disposition** row in the revision.

The three peer auditors were re-executed at this stamp as the cross-check:

| tool | selftest | live | finding |
|---|---|---|---|
| `reports/round-25/audit/c31-lessons-index-audit.py` | 28/28, exit 0 | exit 1 | `C31-1 unindexed-file: ['round-26.md']`; `C34-2 prose-arithmetic-drift` |
| `reports/round-25/audit/x45-lessons-pointer-audit.py` | 15/15, exit 0 | exit 1 | `X45-P1 unresolved-pointer` on the round-4 cell the C35 seat corrected (the standing X63-D2 cross-tool disagreement) |
| `reports/round-26/audit/x63-lessons-audit.py` | exit 1 (3 controls pin the pre-round-26 partition of 26 files) | exit 1 | `X63-A1`, `X63-F1`, `X63-G1` |

The X63 selftest red is **not** a defect in X63: three of its 20 controls assert
`len(files) == 26` and `A`/`F` green on the live bytes, which was true when it
was written and is false now that `round-26.md` exists. It is the same class of
staleness this audit reports one level up — a **control fixture pinned to a
moving partition**. This seat records it and takes no position on whether the
round-26 tool should be re-pinned (that is the parent's disposition).

## 2. After-state (2026-10-18T19:15:44Z, `x57-lessons-receipt.json`)

```
filed index:      corpus/lessons/README.md
  sha256:         ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c
  blob:           a31870556c733498243b56697896504a2fb3679a  (= declared baseline)
  rows:           26
newest revision:  reports/round-26/zzz-lessons-index-revision-4.md
  sha256:         1c4623ec2e26954853da75af9783190aa573a291a426ab3a3cf574945016f9b9
  rows:           27
lesson files:     27        queue rows: 49
  PASS A2_revision_rows_eq_files      PASS G1_x63_instances_reproduce
  PASS B1_filed_pins_rederived        FAIL G2_revision_cells_clean
  PASS B3_shape_cells_rederived       FAIL G3_row_level_cells_clean
  PASS D_pointers_resolve             PASS H_round13_row_self_describes
  PASS E_queue_cross_consistency      PASS I_disposition_coverage
  PASS E2_owners_resolve              PASS J1..J3 peer tools reproduce
  FAIL A1_filed_rows_eq_files         FAIL B2_revision_pins_rederived
  FAIL F_prose_arithmetic
findings:         5
  X57-A1  X57-B2  X57-F1  X57-G2  X57-G3
```

Every reading binds to the digests above. The partition is a live-wave surface:
a `corpus/lessons/round-27.md` landing after this stamp adds a row rather than
changing one, and would re-red A1/A2/F here and C31/X63 above.

## 3. Findings

### X57-B2 / X57-G2 — the newest revision's own pin is stale (finding)

The revision `zzz-lessons-index-revision-4.md` re-derived every pin from the live
bytes at its own stamp (18:23Z local 15:23−03:00, mtime
`2026-10-18 15:23:14−03:00`). The round-26 close commit `4f09c99`
(2026-10-18T16:10:02−03:00 = 19:10:02Z) then **amended `corpus/lessons/round-26.md`
from 46 745 B / 190 lines to 60 054 B / 222 lines**, and no later probe re-read
the revision:

| surface | the cell says | measured now |
|---|---|---|
| rev-4 §1 row `round-26.md` | `bytes=46745 lines=190 sha8=cf7461fe` | 60 054 B / 222 lines / `cae06660` |
| rev-4 §1 row `round-25.md` | "round-25 claims pending, not carried" | `reports/round-25/validation.json` exists, `acceptance_checks_passed: true` |
| rev-4 §1 row `round-26.md` | "its claims are pending, not carried" | `reports/round-26/validation.json` exists, `acceptance_checks_passed: true` |
| rev-4 §4 disposition `Q-18-3` | next touch **round 26** | round 26 closed at `4f09c99`; its receipt reads `true` |

Commands (run 2026-10-18 from the lane root):

```sh
stat -c '%y' corpus/lessons/round-26.md          # 2026-10-18 15:29:15 -0300
git show 4f09c99:corpus/lessons/round-26.md | wc -c    # 60054
git log --format='%h %cI %s' -- corpus/lessons/round-26.md
python3 -c "import json;print(json.load(open('reports/round-26/validation.json'))['acceptance_checks_passed'])"
```

**Class: honest-at-stamp, superseded** — the same class the revision itself
assigned to four of the six `X63-G1` instances. Every cell was true of the bytes
that existed at its stamp; the close commit moved the bytes. The successor
readings are:

- `round-26.md` → **60 054 B / 222 lines / `cae06660`** (the filed bytes at
  `4f09c99`; `git show 4f09c99:corpus/lessons/round-26.md | sha256sum` reproduces
  the digest).
- `round-25.md` / `round-26.md` §1 rows → **their rounds closed**;
  `reports/round-25/validation.json` and `reports/round-26/validation.json` both
  read `acceptance_checks_passed: true`. Whether their commitments are
  *satisfied* is each round's own claim verdict, not this audit's.
- `Q-18-3` §4 → **next touch round 26 has closed**; whether the register engine
  path Q-18-3 asks for is delivered is round-26/27 claim D's question, not this
  audit's.

### X57-G3 — the filed index's row-level `pending` cell is stale (finding)

Same class, on the filed surface, at a depth X63's `G` probe does not reach. X63
probes the **disposition-pointer** and **queue-status** columns; the §2 row cell
"— (this round's own O/D/C claims are pending, not carried)" for `round-25.md`
is in neither. It was true when the index was written (rev 2, 17:47Z) and the
round-25 admit landed at 17:58:37Z.

### X57-A1 / X57-F1 — the filed index is one row behind the partition (known, not new)

The partition moved when `corpus/lessons/round-26.md` landed at 15:29:15−03:00
and was committed by `4f09c99`; the filed index's 26 rows and its stated
`files: 26` were correct at its own 17:48Z stamp. This is exactly the state
revision 4 §0 already names and its isolated-clone control demonstrates
(`C31-1 unindexed-file: ['round-26.md']`), and it is the parent-owned question
revision 4 §5 lists as "not dispositioned here": whether to land a revision
block **inside** the filed `corpus/lessons/README.md`. This seat measures it and
does not decide it. No correction is filed: a filed byte is read-only, and the
successor reading already exists in revision 4 §1 (27 rows, `round-26.md`
pinned).

## 4. What is green

- **Filed pins (B1):** 25/25 pinned rows re-derive exactly on the live bytes.
- **Shape cells (B3):** every `format` and `contract` cell of both surfaces
  re-derives; the live histogram over the 27 files is gate-keeper 15 /
  fragment-index 5 / plain 6 / index 1, and the filed 26-row index's histogram
  is the same minus the round-26 lesson (gate-keeper 14).
- **Pointers (D):** every disposition pointer resolves, or its own cell declares
  the path was never filed (4 such rows, all honest).
- **Queue (E/E2):** 49 queue rows, 49 carried ids, zero orphans in either
  direction; all 49 owners resolve (37 path, 12 role token).
- **Disposition coverage (I):** 49 queue ids ↔ 49 §4 disposition rows; zero
  missing, extra or duplicate; classes `{fixed: 32, carried: 17}`, all in
  vocabulary; every owner resolves; every `carried` row carries `reason:` and a
  next-touch round. **This is the round-26 disposition ledger's own claim,
  re-verified here on today's bytes and not inherited from revision 4's prose.**
- **G1:** the six `X63-G1` instances reproduce, which is the positive control
  that makes the G2/G3 probes mean something.

## 5. Controls

`--selftest` is **37 in-memory controls, exit 0**. One surface per control:

- **positive controls (live readings):** partition 27; filed rows 26; revision
  rows 27; filed pins clean; revision pins drift on exactly `round-26.md`; filed
  orphan exactly `round-26.md`; revision orphan empty; filed queue 49; the six
  G1 instances reproduce under their exact six names.
- **negative controls (a probe must stay silent):** G1 silent when the
  claimed-absent receipt is absent; G3 silent when the round's receipt is absent;
  G2 §4 silent on a revision whose whole next-touch column names only round 99;
  D exempts a declared-absent pointer; E2 accepts `operator`/`parent` as role
  tokens and fires on a fabricated path owner.
- **mutation controls (a probe must fire):** A1 fires on a deleted filed row;
  B2 fires on a falsified revision pin; D fires on an undeclared dead pointer;
  E fires on a dropped queue row; F fires on drifted prose; I fires on a dropped
  disposition row and on an out-of-vocabulary class.
- **cross-tool controls:** J records all three peers with a live exit code, and
  the round-26 auditor's own selftest state (red, because its controls pin the
  pre-round-26 partition) is recorded rather than smoothed over.

Two controls were repaired during this seat's run rather than shipped vacuous:
the G2 negative control originally asserted silence against the live revision
(which is *not* silent, so it passed for the wrong reason), and the G2 §4 control
mutated a row that was not in the disposition section at all. Both now mutate
the right surface and are counted.

## 6. Boundary record

- **Writes:** this file, `reports/round-27/audit/x57-lessons-audit.py`,
  `x57-lessons-receipt.json`, `x57-lessons-selftest.json`. **No
  `corpus/lessons/**` byte was written or edited**; no filed round-8–26 artifact,
  tool or gate was edited; no historical round validator was run against the live
  tree. No commit, no push.
- **Known limit:** this audit is a point-in-time measurement of the digests in
  §2. The partition and the round-26 revision are both live-wave surfaces; a
  later write invalidates §0/§2 without making any row here wrong. The revision's
  §4 dispositions are re-checked for **shape** (class, owner, reason, next touch)
  and for the four staleness instances named above; this seat does **not** re-run
  every one of the 49 evidence probes the C41–C46 seats authored.
- **Not dispositioned here (parent-owned):** whether to land a revision block
  inside the filed `corpus/lessons/README.md`; whether to re-pin the round-26 X63
  auditor's partition-pinned controls; the round-19 path collision (Q-19-1); and
  the standing cross-tool disagreement X63-D2 (the round-25 X45 pointer tool
  reading red on the round-4 cell the C35 seat corrected).
- **Handoff to the round-27 C seat:** if a `corpus/lessons/round-27.md` lesson
  lands, the row set this audit measured (27 files) becomes 28 and a further
  revision is owed; the successor readings in §3 are the ones to carry, not the
  filed index's stale cells.

X57 lessons audit (2026-10-18, round 27). Re-pins and corrections land as new
rows or new files, never as an in-place rewrite of a filed byte.
