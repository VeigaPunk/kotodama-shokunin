# kotodama-shokunin — SCORECARD

Axes: depth, coverage, operability, freshness, calibration, adjacency
(fleet `AXES.md`). Rounds 1–4 retain their historical records, including
rejected rounds 2 and 4. Round 5's author-side admission is recorded below;
its report lands after the work commit. The OpenCode Go supplement is
additional work, not one of the three authorized Z.ai Flash rounds. No fleet
closure, promotion or retrospective schedule-compliance repair is claimed.

The old 0–10 estimates had no reproducible mapping from evidence to score.
They remain historical in Git, not new numeric claims. This table records
per-axis verdicts and checkable observations instead; defining a calibrated
numeric rubric remains an explicit protocol-conformance gap. Freshness is
historically the lowest non-retired axis, not a newly computed scalar.
A raw file or marker count is not a quality score.

## Axes — round 5 (2026-10-17)

Measured baseline: `1ccb2b7119039d8026ad1d004f20427623838b94`. Claims F/O and
their unchanged thresholds are in `reports/round-5/flash-claims.json`.
Delivered-tree commands, exact tested code hashes and results are persisted
in `reports/round-5/validation.json`; `reports/round-5/kotodama.md`, filed
last, binds these measurements to the carrying work commit. Source readings
and reviews remain author-side evidence; parent re-fetches are separately
recorded, not independent promotion verification.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | unchanged | Same nine-derivation NON-CANON exercise and D2 packet; five source-use distinctions added to SKILL without claiming a new end-to-end culture task | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json`; `python3 reports/round-5/run-validation.py` | Positive example exit 0; D2 still 20 findings; `reports/round-5/validation.json` |
| coverage | unchanged | 179 → 179 knowledge entries across six partitions; civilization partition remains 92 bases + two source maps, not 94 verified civilizations | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 179 files; partition totals 16/16/16/24/13/94; `corpus/README.md` |
| operability | improved (claim O) | No standalone battery → seven copied-tree gate selftests pass; six traceback/exit-1 malformed cases → six stable exit-2 diagnostics; battery 10/10 controls and craft 10/10 domain + 18/18 CLI controls pass; both round-3 manifests reproduce 7/7 | `python3 reports/round-5/run-validation.py`; `python3 tools/check-gate-battery.py --selftest`; `python3 tools/check-craft-exercise.py --selftest` | F/O acceptance true, previous acceptance preserved; `reports/round-5/validation.json`, `battery-mutation.json` |
| freshness | improved (claim F) | Zero round-5 follow-ups → 20 original unresolved questions followed up in 22 raw rows, 17 retrieved rows and five parent checks; conservative reconciliation is five scoped supported / 15 unresolved, not 13 confirmed whole claims | `python3 reports/round-5/run-validation.py` | Declared ≥10/≥3/≥3 thresholds pass; `corpus/lessons/round-5-sources/`, `reports/round-5/parent-reconciliation.json`, `parent-source-spotchecks.json` |
| calibration | improved (unclaimed observation) | Raw worker labels 13 supported / eight unresolved / one contradicted are separated from 20 original-question dispositions (five scoped support / 15 residuals); schema, harness and runtime-review defects retained and corrected, not hidden | `python3 reports/round-5/run-validation.py`; `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | 22 rows / 20 IDs; 592 raw marker-bearing lines, 598 raw occurrences; `integration-attempts.json` and reconciliation |
| adjacency | unchanged | Same handoff envelope: 16 fields and 20 glossary entries, exit 0; no lore receipt, cultural clearance or canon decision | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md`; `python3 reports/round-5/run-validation.py` | Previous acceptance rerun in an isolated copy; `reports/round-5/validation.json` |

Admission: both measurable claims verify and no tested axis is harmed.
This does not prove arbitrary malformed-schema safety, cultural authenticity
or untested behavior. Full protocol conformance and promotion remain open.

## Capabilities

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| structural domain checks | Phonology, lexicon, myth, costume, naming and provenance verdicts on their supplied inputs; coverage limitations retained | `tools/gates/*.py --selftest`, seven isolated legacy selftests | round 1 (handoff round 2) |
| reproducible culture assembly | Source-hash-pinned D2 packet and positive/negative assembly controls | `python3 tools/assemble-d2.py --selftest`; `--check` | round 3; selftest supplement-opencode-1 |
| frozen verdict replay | Validate snapshot/gate/output digests before re-executing pinned inputs; expected red remains red | `python3 tools/replay-frozen.py --selftest`; actual round-3 replay | supplement-opencode-1 |
| uncertainty inventory | Deterministic lines/occurrences/marker inventory with heuristic labels, never scholarship certification | `python3 tools/source-audit-inventory.py --selftest`; `--json --summary` | supplement-opencode-1 |
| historical source rechecks | Per-claim retrieved passages, access limits, contradictions and unresolved outcomes | 13 supplemental ledgers / 148 audits; round-5 follow-up of 20 original questions with separate parent reconciliation | supplement-opencode-1; extended round 5 |
| contrastive craft exercise | Distinguish sound law, register-limited name avoidance and borrowed garment strata across two eras | `python3 tools/check-craft-exercise.py --selftest`; `examples/supplement-opencode-1/sound-change-vs-taboo.json` | supplement-opencode-1 |
| corpus apparatus audit | Inspect declared metadata and ledger scope without equating it to factual truth | `corpus/lessons/round-4-audit/` (16 reports), supplemental reviews | round 4 |
| isolated gate battery | Standalone copied-tree seven-gate runner; stable failure versus could-not-evaluate mapping, byte/path preservation checks and ten controls | `python3 tools/check-gate-battery.py`; `--selftest`; `reports/round-5/battery-mutation.json` | round 5 |
| bounded typed craft CLI | Six original malformed controls and reviewed nested/argument cases return exit 2 without tracebacks; genuine findings still exit 1 | `python3 tools/check-craft-exercise.py --selftest` (10 domain + 18 CLI); actual calls in `reports/round-5/validation.json` | round 5 |

## Planned

- Round 5 used one actual 16-worker Z.ai Flash batch (16 completed). Pending
  rounds 6–7 each use one more 16-worker batch through native alias
  `zai-coding-plan/glm-5.3-flash-low` (legacy name, documented MAX thinking).
  This follows the explicit operator amendment, not a silent substitution.
- Pending rounds 8–9 use OpenCode Go DeepSeek v4.1 Flash, 32–64 workers per
  round. The operator explicitly replaced Alibaba token-plan with OpenCode.
- Round 10 is the requested Grok 4.7 xhigh fast 128-worker wave, AFTER the
  DeepSeek rounds. This supersedes the older goal draft's round-8 ordering,
  not its exact-model requirement. Use the native route or the host's Grok
  CLI if necessary and available; no silent model or provider substitution.
- Freshness follow-up: 15 original questions retain residual uncertainty.
  Prioritize primary passages for compound/edition-specific claims, not
  another catalogue match. Keep passage support separate from whole claims.
- D2 needs typed translated-label/native-form handling, scoped era/material
  reconciliation and an executable rank-rule adapter. A green partial
  schema check is not whole-culture verification.
- Fix legacy parser/regex and fixture-rewriting defects documented in
  supplemental reviews 26 and 29; add isolated negative controls. The new
  battery does not repair five old assert-based/fixture-writing selftests.
- Corpus metadata (`source`, `verified-at`, `recheck`), per-gate
  `expected.json` baseline layout, and a reproducible numeric axis rubric
  remain conformance debts. Historical round-4 dispatch provenance remains
  incomplete (31 returns, no durable original request); do not fabricate it.

## Round 5 routing history

The earlier request for native non-flash `zai-coding-plan/glm-5.3` was
rejected by the host before launch, not by an observed provider rate limit.
`reports/round-5/availability-attempt-1.json` still records 16 requested,
zero launched, zero completed. It earns no completed-round credit.

After explicit authorization, `reports/round-5/dispatch.json` records one
executed Flash batch, 16/16 completed, plus continuations of existing worker
identities. Reproduce both counts with:
`python3 -c 'import json; a=json.load(open("reports/round-5/availability-attempt-1.json")); d=json.load(open("reports/round-5/dispatch.json")); print(a["requested_workers"],a["launched_workers"],a["completed_workers"]); print(d["workers"],d["completed"],d["actual_executed_batches_after_authorization"])'`.
There were two native request attempts and only one executed batch. Saved
request binding is in `native-request-binding.json`; simultaneous runtime
concurrency and upstream wire-model identity were not independently echoed.
The old availability report remains historical, not a current blocker.

## Saturation and retired axes

No retirement. Legacy saturation line 8 and stagnation window 3 remain
historical policy; the nudge is not invoked without calibrated scores.
