# Round 8 — residual source recheck, harness repair, typed-label D2 build (2026-10-17)

source: reports/round-8/claims.json; reports/round-8/targets.json; reports/round-8/** worker fragments (indexed below); reports/round-8/validation.json (freshest acceptance receipt); reports/round-7/validation.json (carried defect)
verified-at: 2026-10-17 (gate-keeper survey window closed 20:29 UTC; acceptance receipt re-run 20:29:44 UTC on a still-unsettled tree; admission and spot-check pending)
recheck: `python3 reports/round-8/run-validation.py` (declared counting command for F/O/D, authored by shard R8-O15); re-list fragments with `find reports/round-8 -type f | sort`

Gate-keeper skeleton (scribe X01), opened before the round-8 fragments landed
and closed after a 15-minute fragment survey. It indexes the fragments that
landed and records the declared gate candidates with bounded reasons. Nothing
is admitted on declaration alone: the admitted/rejected rows below cite the
fragment and acceptance evidence actually read during the survey window, and
every admission stays marked spot-check pending until the parent's acceptance
run on the settled tree and an independent re-run land.

## Fragment index

Survey commands (2026-10-17 UTC): `find reports/round-8 -type f | wc -l` and
`find reports/round-8 -type f | sort`; a background poller sampled the tree
every 30 s for 30 ticks, 20:14:27–20:29:27 (log kept outside the repo,
`/tmp/r8-poll.log`, not shipped).

- 20:13:27 UTC (first tick): 2 files — `reports/round-8/claims.json`,
  `reports/round-8/targets.json`; zero worker fragments at that moment.
- 20:29:48 UTC (survey close): **141 files** — freshness 32, operability 59,
  depth 34, metadata 11, top-level 4 (`claims.json`, `targets.json`,
  `run-validation.py`, `validation.json`), plus one `__pycache__` artifact.
- The poller observed 159 distinct paths across the window; the gap to the
  141 present at close is transient scratch paths (e.g. `depth/.shard-parser.*.py`)
  that appeared and were removed. The index records presence at close.

| fragment surface | shard range | claim | state at close |
|---|---|---|---|
| `freshness/` — 15 `R8-F*-receipt.json` + 15 `.md` companions + `audit.md` + `reconciliation.json` (32 files) | R8-F01..F15 | F | landed, all 15 ids |
| `operability/` — `defect-inventory.json`, `battery-rerun.json`, `o01-diagnosis.md`, `o02-fix.md`, `neg-controls/` (9 dirs at close: `neg-04`, `neg-05`, `neg-07`–`neg-13`; `neg-06` landed 20:30:08, after close; 59 files) | R8-O01..O16 | O | landed |
| `depth/` — `design-spec.md`, `shard-parser.md`, `shard-rank.md`, `shard-era-material.md`, `test-{boundary,consistency,determinism,replay,selftest}.md`, `skill-table-draft.md`, `docs.md`, `findings-17.md`, `scribe.md`, `neg/` (34 files) | R8-D01..D20 | D | landed |
| `metadata/` — `m01`–`m11` (11 files) | metadata sweep (12 assigned) | (metadata) | 11 of 12 landed |
| `run-validation.py` (first seen 20:19:27), `validation.json` (re-run 20:29:44) | R8-O15/O16 | F/O/D acceptance | runner landed; `rerun.json` absent |

First-seen rows (first poll tick at which the path appeared; 2026-10-17 UTC):
`neg-04/neg-04-control.py` 20:14:57 (first worker fragment) ·
`operability/battery-rerun.json` 20:15:27 · `depth/docs.md`, `depth/findings-17.md`
20:15:57 · `depth/shard-parser.md`, `operability/o01-diagnosis.md` 20:16:27 ·
`operability/o02-fix.md`, first F receipt (`R8-F09-receipt.json`) 20:16:57 ·
`depth/skill-table-draft.md` 20:17:57 · `depth/design-spec.md`, `depth/scribe.md`
20:18:57 · `reports/round-8/run-validation.py` 20:19:27 · `reports/round-8/validation.json`
(first acceptance run) 20:19:57 · `operability/defect-inventory.json` 20:20:27 ·
`depth/shard-rank.md` 20:20:57 · `depth/shard-era-material.md` 20:22:27 ·
`depth/neg/` packets 20:23:57–20:28:57 · `freshness/reconciliation.json`
20:25:08 (mtime) · `depth/test-boundary.md`, `depth/test-consistency.md` 20:26:57.

Fragments landing after 20:29:48 UTC are not indexed here; re-run the survey
commands above. Fragment presence is not acceptance: a landed file is an
input to `run-validation.py`, not a verdict. The tree was still being written
at close (`tools/d2-typed-labels.py` mtime 20:28:35, `reports/round-8/run-validation.py`
20:27:27, `git status` 177 modified + 10 untracked paths), so every receipt
quoted below is a snapshot of an unsettled tree.

## Gate

Candidates are the three claims declared before dispatch in
`reports/round-8/claims.json` (operator regimen: loop 1 of 3, build round
1 of 4; requested model `opencode-go/deepseek-v4.1-flash`, 64 workers).
Each candidate below quotes its declared `after_required` threshold; no
scalar rubric is invented.

- **F / freshness** (declared lowest axis). The 15 residual round-6
  reconciliation rows (11 partial-support, 4 unresolved) must each carry a
  round-8 receipt under `reports/round-8/freshness/`: a fresh
  retrieved-passage record (source URL, accessed-at date, quoted passage
  with named location, support scope) or a documented access failure with
  attempted command and status; >=8 of the 15 must show a retrieved
  substantive passage; passage support stays separate from whole-claim
  support; raw worker labels are preserved apart from reconciled
  dispositions in `reports/round-8/freshness/reconciliation.json`.
  Counting command: `python3 reports/round-8/run-validation.py`.
- **O / operability**. The round-7 acceptance harness must accept
  `duplicate-parent-receipt-does-not-inflate` (reports/round-7/validation.json
  F error: "wrong rejection for duplicate-parent-receipt-does-not-inflate:
  parent check identity collision") while still rejecting genuine
  parent-check identity collisions; each legacy selftest/parser defect from
  supplemental reviews 26/29 (`reports/supplement-opencode-1/26-parser-controls.md`
  D1–D9; `reports/supplement-opencode-1/29-local-boundaries.md` F1–F3) is
  repaired or explicitly quarantined with a documented reason; every repaired
  defect ships an isolated negative control demonstrating fail-before/pass-after;
  `python3 tools/check-gate-battery.py --selftest` and
  `python3 tools/check-craft-exercise.py --selftest` stay green.
- **D / depth** (capability `d2-typed-labels`). A single new tool
  `tools/d2-typed-labels.py` implements the typed-label schema, scoped
  era/material reconciliation and the rank-rule adapter; `--selftest`
  passes with positive and malformed-input controls; the D2 example packet
  regenerates deterministically and replays frozen
  (`python3 tools/replay-frozen.py`) without digest drift; SKILL.md gains
  the label-typing decision table with cited sources; the capability row
  enters SCORECARD only on demonstrated run.

### Survey verdict at close (2026-10-17 20:29:48 UTC)

Freshest filed acceptance receipt: `reports/round-8/validation.json`, re-run
20:29:44 UTC, file sha256 `863e397af8e70135…`, runner `reports/round-8/run-validation.py`
sha256 prefix `d07bf890fc926b94`; `missing_dependencies: []`.

- F: `passed: true`, 0 failures; 15 declared ids, zero mirrored duplicates,
  and its own negative controls (missing-receipt, identity-collision,
  benign-mirror-dedup, passage-leg-separation) recorded as rejecting.
- O: `passed: true`, 0 failures; `battery_rerun` shows both legacy tools
  re-executed live at exit 0 with stdout hashes reproduced
  (`stdout-hash-reproduced` for both `check-gate-battery` and
  `check-craft-exercise`).
- D: `passed: false`, 7 failures (listed below).
- Overall `acceptance_checks_passed: false`.

**Admitted at this survey close: none yet.** Reasons: (1) the round verdict
is false while D is red; (2) the tree was still being written during and
after the window — `tools/d2-typed-labels.py` and `reports/round-8/run-validation.py`
were both modified within two minutes of the last receipt, and the file
count kept rising after the poller stopped, so the receipt is a snapshot of
an unsettled tree; (3) the independent re-run receipt (`reports/round-8/rerun.json`,
shard R8-O16) has not landed. F and O currently read green in that receipt;
that is recorded as observed evidence, not admitted, because admission
requires the parent's acceptance on the settled tree plus the independent
re-run.

Rejected at this survey close (each names the observed evidence):

- **D as currently delivered**: `tools/d2-typed-labels.py --selftest` exits 1
  with a traceback, does not report malformed-input controls, and reports
  failing controls `[('0', '1')]`; `tools/assemble-d2.py --check` exits 1
  because the packet's `reader_sha256` pin `29a9361c7b96…` no longer matches
  the live `tools/gates/costume-era-consistency-gate.py` (`e6bffd7020c0…`) —
  an O-repair side effect on a D input pin, owner action named in the
  receipt; no frozen manifest exists for the D2 packet; and SCORECARD
  carries the `d2-typed-labels` row although the selftest did not pass.
- **SCORECARD row before a demonstrated run** — observed in the wild as D
  failure 7, exactly the shortcut the candidate list rejects.
- **Mid-flight receipts as completion**: the first acceptance run (20:19:57)
  failed F on 7 then-missing receipts and on passage/whole-claim field
  separation in the early receipts (F01/F06/F07 shapes), and O on the
  then-missing `defect-inventory.json`; those conditions were repaired only
  later in the window. Receipts must be judged on the settled tree, not at
  first landing.
- **`battery-rerun.json` alone as the O green leg**: the receipt
  self-declares "pre-repair" (its hash is expected to go stale once O
  repairs edit the tools), so it cannot by itself carry O; the acceptance
  runner re-executes both batteries on the delivered tree, and that live
  re-execution is what the 20:29:44 O pass records.
- **Reusing a round-6 ledger's already-cited passage as a "fresh" round-8
  receipt** — F requires a fresh retrieved-passage record; a recycled
  citation is not a receipt.
- **Counting a documented access failure toward the >=8 substantive-passage
  threshold** — a failure receipt is legitimate but cannot be a retrieved
  passage.
- **Promoting passage-level support to whole-claim or whole-culture
  confirmation** — F keeps passage support separate from whole-claim support
  (the acceptance receipt states this separation is checked structurally,
  not adjudicated for label correctness).
- **Erasing or relabelling raw worker labels instead of preserving them
  beside reconciled dispositions** — F requires both surfaces.
- **"Fixing" the identity-collision defect by weakening the rejection so
  genuine collisions pass** — O requires the genuine-collision rejection to
  survive; the round-8 F-harness negative controls keep the
  identity-collision rejection visible alongside the benign-mirror dedup.
- **Counting a quarantined defect as repaired, or a repair without its
  fail-before/pass-after negative control** — O requires one or the other
  with evidence; nine `neg-controls/` directories were present at close
  (ten by 20:30:08), and whether each is repair-plus-control or a documented
  quarantine is the parent's audit item.
- **Claiming "no digest drift" without an actual `replay-frozen.py` run** —
  the claim is the run's recorded output, not a forecast; no D2 frozen
  manifest exists yet, so no D replay claim is possible at close.
- **Treating fragment file presence or a fragment's self-report as
  acceptance** — fragments are inputs to `run-validation.py`; admission
  requires the parent's run and independent re-run.

Spot-check status: **pending**. No parent acceptance on a settled tree, no
independent re-run (`rerun.json`), and no parent source re-fetch receipt for
the round-8 F receipts has landed in this window. Historical receipts and
frozen evidence must not be rewritten; `reports/round-7/` filed artifacts
are read-only and the O repair belongs to round-8-owned harness code
(`tools/harness/r8_checks.py`). The round's own counting command and the
freshness receipts' access limits remain the authoritative evidence once the
tree settles; this lesson records the gate-keeper's bounded survey only.
