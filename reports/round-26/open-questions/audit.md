# R26-C47..C50 — audit of the open-question dispositions

- round 26 (operator: loop 3 of 3, build round 2 of 4). Seat **C**,
  claims `R26-C47..C50` (open-question auditors x4); owner: L2 worker,
  kotodama-shokunin lane.
- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- canon: **NON-CANON engineering evidence.** This audit admits nothing,
  certifies no round and grants no promotion.
- writes: `audit-dispositions.py`, `audit.json`, `audit.md` in this
  directory, plus gitignored scratch under `.scratch/r26-c47/`. No filed
  artifact of rounds 8-25 was edited; no disposer fragment was edited.
  No commit, no push.

## 0. Verdict at a glance

| reading | value |
|---|---|
| queue rows in the filed README | 49 |
| rows dispositioned by C41-C46 | 49 |
| disposer fragments landed at this stamp | C41, C42, C43, C44, C45, C46 |
| disposer fragments pending | none |
| evidence commands re-run | 49 |
| **findings** | **0** |

## 1. Checks

| id | result | detail |
|---|---|---|
| `A1_every_queue_row_dispositioned` | PASS | 49 queue rows; 0 undispositioned |
| `A2_class_in_vocabulary` | PASS | 0 row(s) outside the vocabulary |
| `A3_fixed_rows_cite_evidence` | PASS | 0 fixed row(s) with no evidence command |
| `A4_carried_rows_complete` | PASS | 0 carried row(s) missing owner/reason/next-touch |
| `A5_evidence_commands_rerun` | PASS | 49 fence(s) re-run; 0 diverged |
| `A5b_stamp_drift_attributed` | PASS | 2 fence(s) diverged; the D4 read set has 1 file(s) moved off the round-25 baseline (examples/culture-d4/expected-holds.json); 0 unattributed |
| `A6_declared_block_counts` | PASS | 0 fragment(s) disagree with the declared partition |
| `A7_revision_carries_dispositions` | PASS | reports/round-26/zzz-lessons-index-revision-3.md: 49 ids named; 0 queue rows absent |
| `A8_revision_class_agrees` | PASS | 0 row(s) whose class family differs between the revision and the disposer fragment |

## 2. Class histogram over the audited rows

| class | rows |
|---|---|
| `carried` | 17 |
| `closed-by-supersession` | 0 |
| `fixed-with-evidence` | 32 |
| `routed` | 0 |
| `standing-rule` | 0 |

## 3. The sibling lessons-index revision

- path: `reports/round-26/zzz-lessons-index-revision-3.md` — discovered, not hard-coded (the file's
  name and directory are not fixed by any contract; it landed at the
  round-26 root as `zzz-lessons-index-revision-3.md`)
  A **new file** — the filed `corpus/lessons/README.md` blob is
  unchanged at `a31870556c733498243b56697896504a2fb3679a`
- queue ids named in it: **49** of 49
- queue rows absent: **0**
- rows whose class family differs from the disposer fragment: **0**

## 4. Stamp drift — a live wave, disclosed not absorbed

2 fence(s) re-ran to a different exit than
the fragment claims, because a peer seat moved the D4 read set
**during this audit's own window**. The disposer fragments measured
the bytes as they stood at their stamp; this audit measured later
bytes. Neither reading is wrong, and the divergence is a fact about
the live wave, not a defect in any disposition.

| row | fence | re-run exit | fragment claimed |
|---|---|---|---|
| `Q-02-4` | `python3 -B tools/exercise-handoff-e2e.py --profile v3` | 1 | [0] |
| `Q-20-3` | `python3 -B tools/exercise-handoff-e2e.py --profile v2` | 1 | [0] |

Attribution is measured, not inferred: the audit hashes the D4
read-set files against their round-25 filed baseline digests, and
only counts drift as attributable when those bytes have in fact
moved (A5b).

## 5. Counting command

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-26/open-questions/audit-dispositions.py        # audit + write
python3 -B reports/round-26/open-questions/audit-dispositions.py --json # receipt
```

