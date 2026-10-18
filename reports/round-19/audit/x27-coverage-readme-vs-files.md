# X27 — coverage audit: `corpus/README.md` index vs on-disk files (round 19)

- round 19 (operator loop 2 of 3, build round 3 of 4; 64 workers on
  `hyper/deepseek-v4-flash`) · seat **X27** (SCRIBE X26..X28 — coverage auditor,
  README vs files) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X26..X28: spot-check auditors (>=6 new entries
  re-derived), coverage auditor (README vs files), lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  baseline revision `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: NON-CANON engineering evidence. This audit admits nothing and certifies
  no round.
- writes: **this file** and its siblings `x26-spotcheck-entries.md`,
  `x28-lessons-audit.md`, plus the read-only tooling and receipts under
  `reports/round-19/audit/`. No `corpus/` byte is edited by this seat. No commit,
  no push.
- measurement window: 2026-10-18T11:32Z (pre-wave baseline) → live re-reads at
  11:35Z–11:4xZ. The wave was live throughout; every reading names its stamp.

## 0. Verdict at a glance

| # | reading (stamp) | class |
|---|---|---|
| 1 | **pre-wave** (`e571894`/HEAD `169c616`, 11:32Z): 6/6 partitions clean — 189 index rows vs 189 disk files, 0 missing, 0 ghosts | **CLEAN** |
| 2 | **mid-wave** (11:38Z): 4/6 clean — verification 20 disk vs 15 rows, synthesis 28 disk vs 24 rows (9 unindexed new entries) | **DIRTY (expected mid-wave)** |
| 3 | **post-reconciliation** (11:41Z): 6/6 clean — **199 index rows vs 199 disk files**, 0 missing, 0 ghosts; `revision:` bumped `1.3` → `1.4` ("Round-19 index refresh") | **CLEAN** |
| 4 | the round-19 revision note and the ten new rows are present; partition counts 19/19/18/29/20/94 | measured |

## 1. Method

Read-only tool `reports/round-19/audit/coverage-audit.py` (stdlib only):

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-19/audit/coverage-audit.py            # per-partition summary
python3 reports/round-19/audit/coverage-audit.py --json     # receipt (receipt-coverage.json)
python3 reports/round-19/audit/coverage-audit.py --selftest # in-memory controls
```

The tool parses the README's `## <partition>/ (N)` section headers and the
`- \`name.md\` — description` index rows under each, then compares the row set
to the `.md` files actually present under `corpus/knowledge/<partition>/`. It
reports, per partition: the declared header count, the row count, duplicates,
files missing from the index, index-only "ghosts", and both deltas. Selftest:
4/4 checks green (section parse, declared count, row extraction, non-row
ignoring).

This audit answers the *index↔files* question only. It does not verify that an
indexed description matches its file's content, and it does not re-measure the
`to-verify` marker counts (`tools/source-audit-inventory.py` owns that).

## 2. Pre-wave baseline (11:32Z, baseline `e571894` / HEAD `169c616`)

```
linguistics      clean declared=19 rows=19 disk=19 missing=0 ghosts=0
myth-symbol      clean declared=19 rows=19 disk=19 missing=0 ghosts=0
culture-material clean declared=18 rows=18 disk=18 missing=0 ghosts=0
synthesis        clean declared=24 rows=24 disk=24 missing=0 ghosts=0
verification     clean declared=15 rows=15 disk=15 missing=0 ghosts=0
civilizations    clean declared=94 rows=94 disk=94 missing=0 ghosts=0
TOTAL rows=189 disk=189 clean=6/6
```

README `revision:` reads `1.3 — Round-10 index refresh …` at both `e571894` and
HEAD `169c616` (`git show e571894:corpus/README.md` vs live — identical). The
index was fully reconciled **before** the round-19 wave; the two thin partitions
that claim C expands held exactly 15 (verification) and 24 (synthesis) rows.

## 3. Mid-wave reading (11:38Z)

Nine new entries had landed (5 verification + 4 synthesis) with no README edit:

```
synthesis        DIRTY declared=24 rows=24 disk=28 missing=4 ghosts=0
    missing: era-material-scoped-reconciliation.md, generated-artifact-lifecycle.md,
             hold-set-contract-in-brief.md, typed-label-routing-workflow.md
verification     DIRTY declared=15 rows=15 disk=20 missing=5 ghosts=0
    missing: gate-battery-surface-verification.md, generated-artifact-roundtrip-verification.md,
             label-channel-routing-verification.md, pre-declared-hold-set-reconciliation.md,
             two-reader-interop-agreement.md
TOTAL rows=189 disk=198 clean=4/6
```

This is the **expected intermediate state** for an append-only wave: authors land
files, and the index reconciliation is a single later write. The state is
reported here because a coverage audit must not read a mid-wave snapshot as a
defect — the question is whether the reconciliation lands before round close.

## 4. Reconciliation requirement (what a clean close needs)

Claim C's `counting_command` (`reports/round-19/run-validation.py`, `measure_c`
§C3) requires, at close:

1. `corpus/README.md` changed vs the baseline revision (not merely "present");
2. its `revision:` string bumped past `1.3`;
3. every new entry's filename indexed in the README;
4. the `## verification/ (N)` and `## synthesis/ (N)` header counts equal the
   live file counts; and
5. a round-19 revision note in the README prose.

The auditor's `coverage-audit.py` re-measures (3) and (4) directly and (2)
via the `revision:` line; a clean `6/6` reading after the reconciliation is the
independent control that the index and the files agree.

## 5. Post-reconciliation reading (11:41Z)

The reconciliation landed while this audit was running. Final state:

```
linguistics      clean declared=19 rows=19 disk=19 missing=0 ghosts=0
myth-symbol      clean declared=19 rows=19 disk=19 missing=0 ghosts=0
culture-material clean declared=18 rows=18 disk=18 missing=0 ghosts=0
synthesis        clean declared=29 rows=29 disk=29 missing=0 ghosts=0
verification     clean declared=20 rows=20 disk=20 missing=0 ghosts=0
civilizations    clean declared=94 rows=94 disk=94 missing=0 ghosts=0
TOTAL rows=199 disk=199 clean=6/6
```

`revision:` reads `1.4 — Round-19 index refresh: the thin partitions gained ten
new entries (verification 5, synthesis 5, landed 2026-10-18 …) and every row is
re-measured against the files it indexes (199 rows, 0 missing, 0 topic
mismatches; partition counts 19/19/18/29/20/94)`. Every one of claim C's five
reconciliation conditions (§4) is satisfied, verified independently by this
audit's `coverage-audit.py`:

1. README changed vs baseline — yes (`git diff corpus/README.md` non-empty);
2. `revision:` bumped `1.3` → `1.4` — yes;
3. all ten new entries indexed — yes (0 missing in both thin partitions);
4. `## verification/ (20)` and `## synthesis/ (29)` equal the live counts — yes;
5. a round-19 revision note present — yes (`corpus/README.md` §Known gaps /
   revision header).

**Timing note:** the `revision:` string was bumped roughly two minutes *after*
the row/count edits landed (rows clean at 11:39:30Z with `revision: 1.3`; bumped
to `1.4` at 11:41:06Z). A validator run inside that window would have failed the
C3 "revision was not bumped" leg while the index itself was already clean — a
reminder that the reconciliation is a multi-write act, not atomic.

## 6. Limits

- Structural comparison only: the tool checks that the index names the files and
  that the counts agree. It does not audit the row descriptions, the
  `Known gaps (frontier)` section, or the `to-verify` inventory.
- Counts are point-in-time (2026-10-18) and are re-measured, never inherited,
  before being quoted. A mid-wave DIRTY reading is a snapshot, not a verdict.
- The README's round-19 note repeats the pre-change battery statement ("the D4
  gate family is outside the battery's seven-name constant"). See the sibling
  `x26-spotcheck-entries.md` finding X26-1 context and the round-19 lesson: the
  same-round O change registers nine gates, so that sentence is a point-in-time
  reading, not a current one.
