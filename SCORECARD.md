# kotodama-shokunin — SCORECARD

Axes: depth, coverage, operability, freshness, calibration, adjacency
(fleet `AXES.md`). Rounds 1–4 retain their historical records, including
rejected rounds 2 and 4. Rounds 5 and 6 have author-side admission tables
below; each final report lands after its work commit. The OpenCode Go
supplement is additional work, not one of the three authorized Z.ai Flash
rounds. No fleet closure, promotion or retrospective schedule-compliance
repair is claimed.

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

## Axes — round 6 final integration (2026-10-17)

Baseline: `030c3928de74ed514853bc1f7490e0f8bb4d451f`. The original F claim
and thresholds in `reports/round-6/claims.json` are unchanged. One actual
Flash MAX batch returned 16/16; its three same-identity review continuations
are not additional swarms. Parent reconciliation is separate from the
frozen raw ledgers at `104aa54c737d79c5df1382f65d578b61cbf831f2`.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | unchanged | Same executable culture tasks and twenty D2 findings; five bounded source-to-system rows added, not a new whole-culture demonstration | `python3 reports/round-6/run-validation.py`; `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | Prior acceptance green in a disposable copy; `SKILL.md` round-6 table |
| coverage | unchanged | 179 → 179 knowledge entries, same six partitions 16/16/16/24/13/94; twelve existing entries audited, not twelve newly verified civilizations | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`; `python3 reports/round-6/run-validation.py` | `validation.json` inventory; civilization partition remains 92 bases plus two source maps |
| operability | unchanged | Old code/examples byte-identical; round-local acceptance and nine count-boundary negative controls added without claiming a new general gate | `python3 reports/round-6/run-validation.py` | Seven legacy gate selftests pass; both round-3 manifests 7/7; craft 10/10 domain + 18/18 CLI; previous acceptance true |
| freshness | improved (claim F) | Zero round-6 rows/checks → 24 fixed rows / twelve entries, twenty distinct eligible main passages / eleven entries, five parent source checks / four entries | `python3 reports/round-6/run-validation.py` | F true; unchanged 24-row / ≥6-passage / ≥4-entry / ≥3-parent thresholds; normalized key list and receipts in `validation.json` |
| calibration | improved (unclaimed observation) | Raw 24 supported / 18 whole / six partial preserved → nine scoped-support / eleven partial-support / four unresolved; archive pin, page-9 locator and two main mediator-kind corrections recorded apart | `python3 reports/round-6/run-validation.py` | `parent-reconciliation.json`, `parent-source-spotchecks.json`; five parent checks are not twenty independent whole confirmations |
| adjacency | unchanged | Same province and handoff boundary; no lore receipt, cultural clearance, canon or promotion | `python3 reports/round-6/run-validation.py`; `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | Prior acceptance and preserved handoff example; `SHONEN.md` remains author-asserted |

Author-side admission: F verifies and no tested axis is harmed. The
acceptance command checks recorded relevance, schema, count boundaries,
preserved history and actual regressions; it is not a historical-truth or
cultural-authenticity oracle. Tertiary mains and optional corroborations do
not enter the twenty-passage count. Fifteen older round-5 residuals remain
unresolved; round 6 still has eleven partial and four unresolved questions.

The historical checkpoint state is preserved in `checkpoint.json`,
`checkpoint-validation.json`, the first 96 lesson lines and the first 142
filed report lines. `check-checkpoint.py` is unmodified and applies to the
checkpoint tree, not the later legitimate append-only entry errata. The
final report outcome appends after the carrying work commit and lands last.

## Round 7 declared — no result claimed yet (2026-10-17)

Baseline `30caac66a2a382f1c46ba31f0c3c93da62d0762c`.
`reports/round-7/claims.json` declares two distinct measurable moves:

| claim / axis | before → required after | counting command |
|---|---|---|
| F / freshness, historically lowest non-retired | Zero round-7 records → five fixed live rule checks, ≥3 distinct substantive passages across ≥3 reference entries and ≥2 parent re-fetches | `python3 reports/round-7/run-validation.py` |
| O / operability, capability acquisition | No D3 profile → deterministic NON-CANON two-era culture packet, 20 lexemes, 6 replayed names, 2 attributed variants, 4 costume/scene cases, 5 scoped source bridges; actual positive/≥12 domain-negative/≥4 malformed CLI controls, isolated selftest and frozen tamper rejection | `python3 reports/round-7/run-validation.py`; `python3 tools/assemble-culture-d3.py --check`; `python3 tools/check-evidence-coupling.py --selftest` |

The live-source check and D3 capability are independently verifiable. No
axis verdict or new capability is admitted at declaration. Old D1/D2,
source uncertainty and round-6 evidence remain unchanged; D3 is not an
implicit repair of D2. Dispatch is exactly one 16-worker Flash MAX batch.

## Axes — round 14 (2026-10-17), admitted (integrate round)

Baseline `a7bc9e9`; one 32-worker `openai-codex/gpt-6.1-sol` (max effort)
batch (27/32 completed; 5 scribe seats failed — consolidation completed by the
integrator). Acceptance: `python3 reports/round-14/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | 8 routed items open → 8/8 dispositioned in routed-resolution.json: 3 applied-with-control (battery roots: default run exit 0 / 7/7 gates / 29/29 controls; tracker verifier pointer appended with byte-identical rows; status-conflict single-status entry), 5 resolved-by-documentation with controls; filed bytes of rounds 8-12 untouched | `python3 reports/round-14/run-validation.py` | `reports/round-14/routed-resolution.json`, fix-*.md, verify-*.md, regression.md |
| depth | improved (claim D, capability `receipt-guard`) | Unmitigated clobber root cause → `tools/harness/receipt_guard.py`: overwrites of committed validation.json refused unless REFRESH_RECEIPTS=1 (exit 3, named diagnostic); selftest both modes; retro-tests prove it catches the r8/r9 clobber pattern; rounds 8-11 runners untouched | `python3 tools/harness/receipt_guard.py --selftest` | `reports/round-14/guard/` |
| calibration | improved (claim C) | No loop view → loop-1 retrospective: 4 admitted / 1 rejected / 1 operator-skipped; claim flags 14 passed / 1 failed (filed harness decisions, not recertification); round-11 denominators explicit (147/189 = 0.778; 147/192 = 0.7656; both < 0.95); freshness-threshold question restated for the operator | `reports/round-14/loop1-retrospective.md` | retrospective + audits + retro-consistency.md |

Admission: O/D/C verify, no axis harmed. Integrator acts: routed-resolution.json
authored; SCORECARD/LOG drafts landed; 5 failed scribe seats' coverage folded.

## Axes — round 15 (2026-10-17), admitted (GLM round 1 of 2)

Baseline `c60b17c`; one 16-worker `zai-coding-plan/glm-5.3-flash-low` (zai MAX
effort) batch (12/16 completed; O02 builder seat timed out — its role was
covered by the landed validator suite + deterministic packet build; 2h wave).
Acceptance: `python3 reports/round-15/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | Handoff packet semantically rejected (round 12) → v2 lands: 16/16 + 20/20 shape, 15/15 claims with uncertainty {status,basis} (8 supported / 5 partial / 2 unresolved, zero boilerplate per audit), 50/50 claim-to-record links resolving, D2 aggregate dissolved into 34 atomic edges; contract-audit re-run = pass-with-named-gaps (bilateral read + L0 digest remain lore-owned); validators (19/19, 31/31 selftests) + frozen expected.json + freeze/verify tool durable | `python3 reports/round-15/run-validation.py` | `reports/round-15/handoff/` (v2-design, packet-v2-05 twins, contract-v2-audit, frozen.md, reviewers) |
| depth | improved (claim D) | No uncertainty-typing craft knowledge → SKILL.md gains the claim-uncertainty decision table (supported/partial/unresolved + basis grammar + verification-partition crosswalk) + 13 error-pattern rows; 17/17 rule rows cited; enum drift-checked vs the landed packet | `python3 reports/round-15/run-validation.py` | `reports/round-15/knowledge/` drafts + SKILL.md subsection |
| calibration | improved (unclaimed observation) | Three reviewer findings (L-anchor link bypass, unchecked edge source, lexeme link-coverage gap) routed to round 16 with recipes, not absorbed | — | `reports/round-15/handoff/review-{9,10}.md` |
| coverage / freshness / adjacency | unchanged | Freshness axis-moves still paused; fleet root has one pre-existing stray (baseline-analyze.txt, flagged not ours); filed rounds 8-14 byte-preserved (651 files checked) | — | `reports/round-15/scope.md` |

Admission: O/D verify, no axis harmed. Routed to round 16: reviewer findings
F9-1/F9-2/F10-1; packet canonical rename note; lore-owned items (bilateral
read, L0 digest) stay open.

## Axes — round 16 (2026-10-18), admitted (GLM round 2 of 2 — loop 1 complete)

Baseline `0ce7714`; one 16-worker `zai-coding-plan/glm-5.3-flash-low` (zai MAX
effort) batch (16/16 completed). Acceptance:
`python3 reports/round-16/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | 94-entry civ partition unmapped → civ-map.json 94/94 receipted (82 current / 12 stale-documented, named reasons, 0 unreceipted); auditor independently re-derived + 20 spot-checks + all 12 stale reasons re-verified; 2 map defects (dangling evidence paths, missing row dates/reasons) found by the auditor and fixed by the integrator | `python3 reports/round-16/run-validation.py` | `reports/round-16/civ-map.json`, `civ/` shard receipts, `map-audit.md` |
| operability | improved (claim O) | Three routed reviewer findings → all fixed with controls: edge-source validation (selftests 31→38, aggregate rejected E-SOURCE-UNKNOWN); L-anchor collision closed (dangling #L99 rejected, real ids resolve); link coverage 33 orphans → 0 via keyed packet-v2-07 (83/83 links; gate 16/16 + 20/20; frozen baseline re-frozen with the landed recipe after the verify seat pinned a canonicalization divergence) | `python3 reports/round-16/run-validation.py` | `reports/round-16/fixes/`, `verify.md`, `handoff/packet-v2-07.*` |
| calibration | improved (unclaimed observation) | Auditor filed 7 findings incl. 2 map defects + a validator routing conflict; verify seat caught the freeze-recipe divergence; all dispositioned with evidence, none absorbed | — | `civ/map-audit.md`, `verify.md` |
| depth / freshness / adjacency | unchanged | Freshness pause respected (C07 rows: zero live fetches, in-repo verification only); filed rounds 8-15 byte-preserved | — | `reports/round-16/scope.md` |

Admission: C/O verify, no axis harmed. Integrator acts: map repoint + row
annotation (3 defect classes); v2-07 baseline re-frozen; validation rerun on
the settled tree. Loop 1 is complete: rounds 8-16 (r13 operator-skipped).

## Axes — round 17 (2026-10-18), NOT admitted (claim D failed as declared)

Baseline `9b49a4a`; one 64-worker `opencode-go/deepseek-v4.1-flash` batch
(loop 2 build 1; 30/64 completed — route capacity; integration by the
orchestrator). Acceptance: `python3 reports/round-17/run-validation.py`:
C PASS, O PASS, D FAIL.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C verified) | 12 round-16 stale-documented civ entries -> 7 fixed with live content-verified replacements + 5 attempts documented; verifiers re-ran evidence; map-patch proposed | `python3 reports/round-17/run-validation.py` | `reports/round-17/civ/` (12 fixer + 4 verifier fragments + map-patch.json) |
| operability | improved (claim O verified, capability `assemble-culture-d4`) | No D4 assembler -> `tools/assemble-culture-d4.py` durable: 81/81 selftest controls, --check byte-identical regeneration; integrator eras-shape fix (flat tag list + era_records, documented normalization) after the projector contract was discovered | `python3 tools/assemble-culture-d4.py --selftest` | `reports/round-17/assembler/`, packet regenerated twice byte-identical (e7ecd204…) |
| depth | unchanged (claim D failed as declared) | D4 tree complete (12 components, deterministic packet) and the typed projection runs (74 labels / 15 holds / 0 fails emitted) — but the round-11 `typed-pipeline-gate` L1 leg pins assemble-d2 output bytes and structurally cannot consume a D4 packet; "gate findings == D4 hold set" not executable this round; generalization + re-pin cascade routed to round 18 | `python3 reports/round-17/run-validation.py` | gate L1 output; `reports/round-17/d4/` design docs incl. the fork record |
| calibration | improved (unclaimed observation) | Design fork recorded (three D4 concepts across doc seats; delivered tree rules); the gate's D2-boundary discovered and documented rather than worked around | — | D01 §13 fork analysis |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | `reports/round-17/scope.md` |

Round status: REJECTED on D (unverifiable-as-declared; boundary + recipe
recorded); C/O verify; no axis harmed. Routed to round 18: typed-gate
assembler-identity generalization (re-pin cascade: round-11 frozen manifest,
round-9 baselines, round-16 v2-07 expected.json helper pins); D4 gate run +
expected-holds + frozen manifest once the gate accepts D4.

## Axes — round 18 (2026-10-18), admitted (build 2 of 4 — repairs round 17)

Baseline `c66ac3c`; one 64-worker `opencode-go-2/deepseek-v4.1-flash` batch
(19/64 completed; the gate generalization design + re-pin seats landed; the
D4-adapter seat never delivered — built by the integrator as
`tools/assemble-d4-typed.py`, text-transform architecture after the serializer
round-trip corruption was diagnosed: regex backslashes, booleans, nulls).
Acceptance: `python3 reports/round-18/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | Typed gate D2-bound -> generalized: declared-assembler identity (packet-declared pin; D4 profile), default D2 path byte-identical (16/16 legs pre/post); re-pin cascade green (round-18 repin-d2 manifest 11/11 reproduced; round-9 baseline pins; v2-07 helper pins); L2 D4-family accounting landed with the before/after digest table | `python3 reports/round-18/run-validation.py` | `reports/round-18/gate/`, `repin/` |
| depth | improved (claim D) | D4 never gate-verified -> generalized gate runs D4 19/19 legs: findings exactly == the 15-hold + 1-note expected set; routing consistency (12 rows: 6 garment + 6 slot, owed slots named once); channel differential exactly the 6 PHON-INVENTORY artifacts removed, zero additions; round-18 frozen manifest replays green; D2 verdict identical to round-11 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `reports/round-18/d4/`, `tools/gates/frozen/round-18/` |
| coverage | improved (claim C) | Round-16 map pre-fix -> round-18 revision applies the round-17 patch (transitions with fix-evidence pointers; attempt rows annotated; counting command reproduces 94; round-16 map untouched) | `python3 reports/round-18/run-validation.py` | `reports/round-18/civ-map-r18.json` |
| calibration | improved (unclaimed observation) | Round-17 rejection root-caused to a discovered architectural boundary, repaired with a documented recipe; the serializer round-trip corruption class recorded (D4 first culture with derivations) | — | this section; gate design §11 |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | `reports/round-18/scope.md` |

Admission: O/D/C verify, no axis harmed. The round-17 D-rejection stands on
record; its artifacts are now fully verified. Capabilities addendum:
`assemble-d4-typed` (D4 typed-packet adapter, text-transform architecture).

## Axes — round 19 (2026-10-18), admitted (build 3 of 4 — hyper provider)

Baseline `169c616`; one 64-worker `hyper/deepseek-v4.1-flash` batch (17/64
completed — hyper route is slow; integrator-authored validation after the
scribe seat failed). Acceptance:
`python3 reports/round-19/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D) | D4 craft uncodified -> SKILL.md gains two subsections (slot-label routing: one row per translated label, owed slot named once on the slot's row; derivation-replay discipline: machine-readable pattern/output pairs + the round-trip corruption class); 3 analyst + 2 reviewer fragments; reviews' pre-repair red measurements superseded with errata; Defects A/B corrected | `python3 reports/round-19/run-validation.py` | `reports/round-19/knowledge/` |
| coverage | improved (claim C) | verification 15 / synthesis 24 -> 20 / 29 (10 new sourced entries, integrator-audited zero defects: gap-named, frontmatter-complete, decision-record carrying) | `python3 reports/round-19/run-validation.py` | `git status` new entries + audit |
| operability | improved (claim O) | D4 gates outside the battery -> registered (9 registered: 7 executed + 2 D4 duty-2 baseline-inspected — mirror cannot host peer-dependent gates, mode documented); committed expected.json baselines for both D4 gates (17 valid baseline rows); battery selftest 35/35 | `python3 tools/check-gate-battery.py` | `reports/round-19/battery/`, `baselines/` |
| calibration | improved (unclaimed observation) | Review blockers traced to pre-repair states and dispositioned with errata, not re-rolled; the projector era-alias leg's D2-component dependency for D4 packets documented and routed | — | review errata; routed wart |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | `reports/round-19/adjacency.md` |

Admission: D/C/O verify, no axis harmed. Integrator acts: errata + SKILL
landings; adapter selftest repaired (12/12: mirror faithfulness + named-once
fixture); availability record closed.

## Axes — round 20 (2026-10-18), admitted (build 4 of 4 — loop 2 builds complete)

Baseline `122086b`; one 64-worker `opencode-go/deepseek-v4.1-flash` batch
(20/64 completed; heavy integration seats landed). Acceptance:
`python3 reports/round-20/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D) | Handoff e2e v2 (D2+D3) -> v3 adds D4: 27 claims (16 supported / 7 partial / 4 unresolved), D4-CL01..12 with uncertainty + 102/102 resolving links; gate 16/16 + 20/20; v2 subset equality preserved; frozen v3 baseline + tamper control | `python3 reports/round-20/run-validation.py` | `reports/round-20/handoff/` (design, claims-map, packet-v3-13, audit-v3) |
| operability | improved (claim O) | Projector era-alias wart closed: per-family alias resolution (D4 documented skip; D2 byte-identical — selftest 50/50, gate 13/13 stdout sha unchanged); adapter selftest 12/12 WITHOUT the foreign examples tree; repin cascade updated as new rows; all regressions green | `python3 tools/d2-typed-labels.py --selftest` | `reports/round-20/wart/`, `repin/` |
| coverage | improved (claim C) | README unreconciled since rounds 10/19 -> command-carried reconciliation (civ 94 / ling 20 / myth 19 / culture 18 / synth 29 / verif 20); index rows == files; known-gaps refreshed against rounds 17-20 content | `python3 reports/round-20/run-validation.py` | `reports/round-20/readme/` |
| calibration | improved (unclaimed observation) | Design seats executed documented flip rules when the wart fix landed mid-wave (basis re-grounded with the negative-control leg named as owed); fragment-index collision (X19/X20 vs X24) recorded for integrator disposition | — | design.md §4; fragment indexes |
| freshness / adjacency | unchanged | Pause in force (operator ruling still pending at L0); ledger snapshot taken for the loop-2 verify round; scope clean | — | `reports/round-20/ledger-snapshot.md` |

Admission: D/O/C verify, no axis harmed. Loop 2 builds complete (rounds 17-20;
one rejection r17 later repaired by r18). Next: round 21 verify (luna).

## Axes — round 21 (2026-10-18), admitted (loop 2 verify round)

Baseline `8115eaa`; one 64-worker `openai-codex/gpt-6-luna-max` verify batch
(20/64; integrator coverage completion for failed scribe seats — 18 ledger
rows added and normalized to the licensed disposition schema). Acceptance:
`python3 reports/round-21/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim C) | Rounds 17-20 unrecounted -> full recount ledger (45+ unique commands; 100% match or dispositioned); r18 repair independently reproduced (19/19, D2 byte-identical, replay 11/11); dispositions name every mismatch class incl. one filed-figure defect (r20 linguistics count) and the 102-vs-105 link drift (mtime tie-break, non-hermetic) | `python3 reports/round-21/run-validation.py` | `reports/round-21/recount/` (16 receipts, ledger.json, dispositions.md, audit.md) |
| operability | improved (claim O) | No loop-2 defect queue -> consolidated 23-entry ledger across rounds 17-20 (conformance/process/bookkeeping classes); bounded fixes demonstrated; everything larger routed to round 22 with owners; regressions green (battery, craft, all typed/assembly selftests, replay selftest) | `python3 reports/round-21/run-validation.py` | `reports/round-21/defects/` (sweeps, fixes, routed.md, regression.md, ledger.json) |
| adjacency | improved (claim A) | Per-round posture -> consolidated audit: handoff v3 contract re-verified (16/16 + 20/20 + 27 claims 16/7/4 + 105/105 links current pair); one filed D2->D4 fixture bleed in the typed projection (routed, not absorbed); v3 edge-payload loss (declared_in) documented; PROVINCE accurate; zero unfiled bleed | `python3 reports/round-21/run-validation.py` | `reports/round-21/adjacency/` |
| depth / coverage / freshness | unchanged | Audit round; pause in force | — | — |

Admission: C/O/A verify, no axis harmed. Loop 2 is complete (rounds 17-21).
Routed to round 22 (with owners): edge declared_in restoration, mtime
tie-break hermeticity, the D4 fixture bleed, the r17 clone-snapshot question,
the alias malformed-tag coercion, baseline-binding drift class.

## Axes — round 22 (2026-10-18), NOT admitted (claim D failed as declared)

Baseline `cd9c8e4`; one 32-worker `openai-codex/gpt-6.1-sol` (max effort)
integrate batch (9 completed, 6 aborted mid-flight by operator interrupt —
among them the D-claim implementation seats D04-D08). Acceptance: O and C
verify; D does not (the bleed fix was designed but never implemented).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O verified) | Six round-21 routed items dispositioned in routed-resolution.json: declared_in restored (34/34 exact equality, truncation removed, packet 3.1.1, new frozen revisions); deterministic content-based tie-break (23/23 controls; the PLACEHOLDER_RE wording false positive routed to r25, not weakened); alias coercion fails closed (132/132 projector selftest; paired before/after); r17 scanner mechanism reproduced (.scratch path filter); r18 supersession documented as a named row; baseline-binding new-pin discipline codified. Regressions: battery/craft/adapter/d4-gate/d2-gate/handoff-v3/handoff-v2/projector all exit 0 | `python3 reports/round-22/run-validation.py` (parent-assembled) | `reports/round-22/fixes/`, `routed-resolution.json` |
| calibration | improved (claim C verified) | reports/round-22/loop2-retrospective.md: loop 2 = 4 admissions / 1 rejection; 14 passing / 1 failing claim flags; the r17/r18 arc assessed honestly — the executable repair is real but R17's 6-hold/0-note contract vs the reconciled 15/1 shows the original contract was not unchanged; 23 defect entries classified exactly once; auditors verified numbers and pointers (C08 PASS; strict C07 unblocked by the resolution JSON) | `reports/round-22/loop2-retrospective.md` | retrospective + audits |
| depth | unchanged (claim D failed as declared) | The D4 fixture-bleed FIX was analyzed and designed (exact census: 24 rank-provenance fields + 3 quarantine citations + 14 short refs; injection point at the projector's unconditional D2 build_payload; family-clean design with paired controls) but the implementation seats were aborted before landing — no source fix this round | `reports/round-22/bleed/` | analysis.md + design.md only |
| freshness / adjacency / coverage | unchanged | Pause in force; scope verified clean at recorded observations (1,018 protected paths) | — | `reports/round-22/scope.md` |

Round status: REJECTED on D (impl aborted; design + controls route to round
25 with the implementation seats' recipe). O/C verify; no axis harmed.
Loop-2 retrospective stands as the loop's calibration record.

## Axes — round 23 (2026-10-18), admitted (loop 2, GLM round 1 of 2)

Baseline `0e81d9d` (preservation leg; the adjudicated r22 straggler was
resolved inside the round — regression.md restored to baseline bytes, the
completed O12 report living on as regression-completed.md). One 16-worker
`zai-coding-plan/glm-5.3-flash-low` (MAX effort) batch (17/17 completed).
Acceptance: `python3 reports/round-23/run-validation.py` exits 0 (run in an
isolated copy per the receipt-guard; close-time refresh under
REFRESH_RECEIPTS=1).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | Two r22 tails closed: PLACEHOLDER_RE false positive dispositioned via the preferred route (D4-CL08 basis reworded in the uncertainty grammar — 'foreign-path-stability control' — packet re-pinned as new revision declared-in-r3; no rule weakened; wording-check 28/28 + 17/17); all six combined-source successor pins landed (D2 live expected-holds to projector 2819f687 with supersedes history; round-23 frozen repin-d2 generation replaying 11/11; v2 successor + stale-refusal control; D4 profile/frozen rows re-verified) | `python3 reports/round-23/run-validation.py` | `reports/round-23/wording/`, `pins/` |
| depth | improved (claim D) | Family-clean projection rule drafted (rule statement, unconditional-build_payload injection-point warning, 7 paired controls mapped to landed selftest lines, r25 commitment) and landed into SKILL.md; every row cited | `python3 reports/round-23/run-validation.py` | `reports/round-23/rule/skill-draft.md` + SKILL.md |
| calibration | improved (unclaimed observation) | LOG append-only correction: round 22's 'never implemented' wording mis-described the tree — the family-clean implementation IS present at 0e81d9d (verified by two independent round-23 seats); the r22 ledger row stands with the correction pointer | — | LOG.md correction entry |
| coverage / freshness / adjacency | unchanged | Pause in force; scope clean at recorded observations | — | `reports/round-23/scope.md` |

Admission: O/D verify, no axis harmed. SHONEN-box evidence survey prepared for
round 24's promotion review (`reports/round-23/shonen-survey.md`).

## Axes — round 24 (2026-10-18), admitted (loop 2 GLM round 2 — promotion-review round)

Baseline `8fbcee9`; one 16-worker `zai-coding-plan/glm-5.3-flash-low` (MAX
effort) batch (16/16 completed). Acceptance:
`python3 reports/round-24/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim C) | SHONEN boxes never non-author-verified -> promotion-review dossier: boxes 1-4 each verified-with-conditions by 10+ named non-author reviewers (swarm seats that authored none of the lane's artifacts); per-box verdicts + 18 traced conditions; the promotion DECISION stays operator-owned | `python3 reports/round-24/run-validation.py` | `reports/round-24/promotion-review.md` |
| operability | improved (claim O) | Cold-run never tested -> 4 fresh-context seats execute the SKILL.md surface (~80 invocations): every documented steady state reproduces (163/163, 7/7 pinned replay, 19/19 D4); 7 breaks/conditions found and dispositioned (7 wording-level SKILL.md fixes landed with controls; 7 named box-3 conditions) | `python3 reports/round-24/run-validation.py` | `reports/round-24/cold-run*.md` |
| depth | improved (claim D) | No SKILL.md staleness audit ever -> adversarial audit: every executable claim re-run green; 8 stale spots fixed with controls/dated errata (line-drifts, inverted battery row, superseded passenger measurement, unresolvable anchors, corpus pointers, stray fences); 123-row per-row disposition table; zero silent staleness | `python3 reports/round-24/run-validation.py` | `reports/round-24/skill-audit.md` + audit fragments |
| coverage / freshness / adjacency | unchanged | Pause in force; scope clean | — | — |

Admission: C/O/D verify, no axis harmed. LOOP 2 IS COMPLETE (rounds 17-24).
The promotion dossier stands for the operator's decision. Loop 3 (rounds
25-32) runs the DeepSeek builds on the devin provider per operator directive.

## Axes — round 25 (2026-10-18), admitted (loop 3 build 1 of 4 — devin provider)

Baseline `f74fc94`; one 64-worker `devin/deepseek-v4-1-flash-high` batch
(operator provider test; 26/64 completed, 31-min wave — the devin route is
slower per-worker than opencode-go but carried the heavy seats). Acceptance:
`python3 reports/round-25/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | Two round-24 hazards closed: (a) the typed-pipeline gate now refuses derived-packet input with named input-class diagnostics (typed-declared-source / typed-unresolvable / typed-stale-source / typed-rebuilt / typed-unfaithful-rebuild, exit 2) plus the owed_slot nullish guard — the false red (14/16 with 8 manufactured DERIV-REPLAYs) is root-caused to a lossy yaml_lines rebuild and eliminated; source-packet entry still 19/19 byte-identical. (b) v3 claim prose corrected to the family-clean present state across 4 revisions (8 stale assertions; D4-CL05/06/07/09) and re-pinned as declared-in-r4. Regressions green; pin cascade as new rows | `python3 reports/round-25/run-validation.py` | `reports/round-25/gate-input/`, `v3-supersession/` |
| depth | improved (claim D, capability `argot-derivation-check`) | The round-17 forecast delivered as an executable leg: derivation replay for register-scoped forms (pattern/output discipline per SKILL); D4L-ARGOT-DERV finding class; negatives real and closed; the delivered-vs-forecast delta named honestly — the register-form domain in the delivered D4 packet is EMPTY (the register class was design-forecast, never built into components), so the leg stands ready over an empty domain, recorded as such | `python3 reports/round-25/run-validation.py` | `reports/round-25/argot/` |
| coverage | improved (claim C) | corpus/lessons/README.md reconciled: every round file 1-24 censused (format class, open questions carried, disposition pointer); the open-question queue extracted with owners; counting command-carried | `python3 reports/round-25/run-validation.py` | `reports/round-25/lessons/` |
| calibration | improved (unclaimed observation) | A transient mid-round gate breakage (~90s, KeyError owed_slot_of) documented with its window; the availability record captures the devin route's first regimen numbers | — | `reports/round-25/gate-input/design.md` §8; availability.json |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | — |

Admission: O/D/C verify, no axis harmed. Devin provider test: viable for
regimen use (slower per-worker; heavy seats landed). Remainders named by the
shard auditors: the r4 twin gap, the empty argot domain, two sibling pin tails.

## Axes — round 26 (2026-10-18), admitted (loop 3 build 2 of 4 — devin)

Baseline `1ad491a`; one 64-worker `devin/deepseek-v4-1-flash-high` batch
(24/64 completed). Acceptance: `python3 reports/round-26/run-validation.py`
exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D, capability `register-stratum`) | The round-17 register forecast CLOSED: the `stamp` attestation register lands in the delivered furnace-league tree — 8 verified register forms (tuum/kit/lom/nees/huum/mees/reek/saam) with the discovered axis-to-operation rule (mark->reverse, fire->lengthen), era E1 scoped, derivation replay clean (8 derived pairs, 0 violations over 170 records); typed labels classify the register forms; named gaps recorded (head2 empty proper domain, syllabify disagreement on 15/62, register law needs a future component — additive landing) | `python3 reports/round-26/run-validation.py` | `reports/round-26/register/` (design measured on the delivered tree) |
| operability | improved (claim O) | Three round-25 remainders dispositioned: the register landing's 6-file read-set change re-pinned through the sanctioned chain — v3 default baseline moved to declared-in-r5 (self-referential tool-pin subtlety: freeze must follow the re-point edit); the pin-repoint checker green 17/17 (stale rows replay red, new rows green, filed rows untouched); the r4 checker superseded-and-recorded with its tails resolved by the pin checker + r5 freeze | `python3 reports/round-26/run-validation.py` | `reports/round-26/remainders/` |
| coverage | improved (claim C) | The round-25 open-question queue 100% dispositioned (fixed-with-evidence or carried with owner + reason + next touch); lessons README new revision | `python3 reports/round-26/run-validation.py` | `reports/round-26/open-questions/` |
| calibration | improved (unclaimed observation) | X64's cold re-run verdict ("not landed") was a stale-snapshot misread — three independent measurements by the integrator confirmed the stratum in the packet and components; the fragment stands as honest-but-superseded | — | this section; packet greps |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | — |

Admission: D/O/C verify, no axis harmed. Devin route: second viable sample.

## Axes — round 27 (2026-10-18), admitted (loop 3 build 3 of 4 — devin)

Baseline `b95fca1`; one 64-worker `devin/deepseek-v4-1-flash-high` batch
(24/64 completed). Acceptance: `python3 reports/round-27/run-validation.py`
exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D, capability `register-law`) | The register law lands: component 13 + the `register_law` packet block (RGL-01..05 — charge, attested oath, naming-of-a-lot, guest's charge; speakers, forces, record consequences) via a decisive A/B (route A beside `registers`: 0 new holds vs route B's 4); the syllabify disagreement fixed (one maximal-onset algorithm; selftest 21->27; all forms re-verified); named findings: RL-1 (no law replay leg yet), RL-3 (all 8 register forms are material-presence; the 5 legal abstractions refuse reverse — the register cannot spell its own law's vocabulary, a recorded craft constraint), RL-4 (orthography packet_keys gap: OR-01..03/LI-01..03/EN-01..02 never reach the packet — routed) | `python3 reports/round-27/run-validation.py` | `reports/round-27/law/` |
| operability | improved (claim O) | The D4 pin sweep: every frozen manifest/baseline/expected-holds/replay row pinning D4 surfaces re-verified against the amended packet; drifted rows re-pinned as new rows; battery 9/9, all replays green; sweep auditors independently verified the inventory | `python3 reports/round-27/run-validation.py` | `reports/round-27/pinsweep/` |
| coverage | improved (claim C) | corpus/knowledge/linguistics/register-strata-attestation.md: sourced, gap-named, decision-record carrying, 32 locators resolving; README reconciled; five false-green/self-defect classes found and fixed in the audit instruments themselves | `python3 reports/round-27/run-validation.py` | `reports/round-27/entry/` |
| calibration | improved (unclaimed observation) | The A/B measurement culture (route chosen by measured holds, not taste); instrument self-defects caught by their own auditors | — | law/design.md §5 |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | — |

Admission: D/O/C verify, no axis harmed. Routed: the law replay leg (RL-1),
the orthography packet_keys gap (RL-4), the register-lexicon ceiling (RL-3 —
a design constraint, not a defect).

## Axes — round 28 (2026-10-18), admitted (loop 3 build 4 of 4 — builds complete)

Baseline `69cecbc`; one 64-worker `devin/deepseek-v4-1-flash-high` batch
(24/64 completed). Acceptance: `python3 reports/round-28/run-validation.py`
exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D, capability `register-law-replay`) | The law gains a replay leg (tools/gates/register-law-gate.py): six D4L-LAW-* classes over four resolutions (speaker by exact token with polarity in kind — the substring trap where 'stamp-holder only' would grant master/delegate is designed out; force vocabulary; consequence vs roll/rank; register by names); RL-4 fixed (8 records now reach the packet; four-site pin cascade); the leg immediately earned its keep — 4 real D4L-LAW-DANGLING findings on the clean packet (every design_row names registers records QREG-05..08 that do not exist; the design's own defect surfaced, priced for round 30) | `python3 reports/round-28/run-validation.py` | `reports/round-28/law/` |
| operability | improved (claim O) | The final build-round sweep: all frozen/baseline/replay surfaces re-verified against the amended packet; drifted rows re-pinned as new rows; battery 9/9; all replays green | `python3 reports/round-28/run-validation.py` | `reports/round-28/sweep/` |
| coverage | improved (claim C) | The RL-3 ceiling recorded in the register-strata entry (append-only amendment) + the register-lexicon-ceilings knowledge entry (sourced, gap-named); README reconciled; entry audits clean (one one-line fix routed) | `python3 reports/round-28/run-validation.py` | `reports/round-28/ceiling/` |
| calibration | improved (unclaimed observation) | The leg's calibration honesty: it reports 6 findings on the clean packet and says why (4 real dangles + 2 saturated classes); controls inert on two classes reported as such — a leg reporting 0 would have hidden both | — | law/design.md calibration section |
| freshness / adjacency | unchanged | Pause in force; scope clean | — | — |

Admission: D/O/C verify, no axis harmed. LOOP 3 BUILDS COMPLETE (rounds
25-28, all on the devin provider). Routed to round 30: the QREG-05..08
dangling-register fix, the battery registration of the law gate, X63-F2.

## Axes — round 29 (2026-10-18), admitted (loop 3 verify round)

Baseline `e923d6e`; one 64-worker `openai-codex/gpt-6-luna-max` verify batch
(17/64 completed; integrator dispositions + the R27 full-sweep reproduction
completed post-wave). Acceptance: `python3 reports/round-29/run-validation.py`
exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim C) | Rounds 25-28 recounted: the register landing independently reproduced (8 forms; 170 records at admission; revision boundaries documented 175/183); the law calibration reconciled (designed 6 vs delivered 4 — the design's own scoping of consequence checks to binding acts; dispositioned, not re-rolled); the R27 full sweep reproduced post-wave (41 findings at the current tree vs 31 at admission — a revision boundary); the devin availability leg documented could-not-evaluate (wave-time telemetry lost with .scratch cleanup; durable records stand; round-30 telemetry-durability fix routed) | `python3 reports/round-29/run-validation.py` | `reports/round-29/recount/` |
| operability | improved (claim O) | Consolidated 24-entry loop-3 defect queue; bounded fixes with controls; everything routed to round 30 (QREG-05..08 dangles, law-gate battery registration, X63-F2, telemetry durability); the r28-sweep TMPDIR precondition fixed in the validator; regressions green | `python3 reports/round-29/run-validation.py` | `reports/round-29/defects/` |
| adjacency | improved (claim A) | Register/law bleed check clean (speech-act framework verified in-world by design); PROVINCE byte-identical; the ceilings-entry evidence defect filed (baseline-false absence claim, non-bleed); zero unfiled bleed | `python3 reports/round-29/run-validation.py` | `reports/round-29/adjacency/` |
| depth / coverage / freshness | unchanged | Audit round; pause in force | — | — |

Admission: C/O/A verify, no axis harmed. Routed to round 30 with owners: the
QREG-05..08 dangling-register fix, the law-gate battery registration, X63-F2,
the register-law selftest speaker-tamper tail, telemetry durability.

## Axes — round 30 (2026-10-18), admitted (loop 3 integrate round)

Baseline `44145d5`; one 32-worker `openai-codex/gpt-6.1-sol` (max effort)
integrate batch (19/32 completed; the orchestrator executed the seats'
explicit parent-action list). Acceptance:
`python3 reports/round-30/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | Five round-29 routed items resolved: QREG-05..08 land (law gate clean 4->0 findings; 7/7 linkage controls); the speaker candidate lands (selftest 29/33->45/45; law-block tamper verified -> named D4L-LAW-SPEAKER); the register-law gate registered in the battery (10/10; r30-post baseline under the standard mirrored layout); X63-F2 append-only amendment; the telemetry durability convention lands in AGENTS.md + a demonstrated round-30 telemetry dir. Regressions green (the v3 default chain re-pointed to declared-in-r6 after diagnosing the profile-row baseline drift) | `python3 reports/round-30/run-validation.py` | `reports/round-30/fixes/`, `routed-resolution.json` |
| calibration | improved (claim C) | reports/round-30/loop3-retrospective.md: the register program assessed end-to-end (forecast -> leg -> stratum -> law -> replay); three-loop regimen summary (18 admissions / 3 rejections / 1 skip through r29); the freshness-threshold question restated with full-regimen data + a concrete recommendation (settled-tree >=95% raw replay, all preregistered rows in the denominator, build-change accounting) | `python3 reports/round-30/run-validation.py` | retrospective + audits |
| depth | improved (claim D) | SKILL.md gains the unified Register-craft subsection (17,829 chars; stratum discipline + law discipline + composition with label typing and the typed pipeline; every row cited); the round-24 box-1 condition CLOSED — post-landing survey 28/28 named executables resolve, digest-pinned | `python3 reports/round-30/run-validation.py` | `reports/round-30/craft/` |
| coverage / freshness / adjacency | unchanged | Pause in force; scope clean at recorded observations | — | — |

Admission: O/C/D verify, no axis harmed. LOOP 3 integration complete.
Routed to rounds 31-32: nothing blocking; the freshness-threshold ruling
remains the operator's.

## Axes — round 31 (2026-10-18), admitted (loop 3 GLM round 1 of 2 — regimen close-out)

Baseline `e8d2d0d`; one 16-worker `zai-coding-plan/glm-5.3-flash-low` (MAX
effort) close-out batch (12/16 + late scribes; orchestrator landings: the
jin'i-ryu rule, the five closing snapshots, the validator reconciliations).
Acceptance: `python3 reports/round-31/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim C) | No single closure artifact -> closure-ledger.json: 32/32 lane rounds audited, zero missing; 22/22 filed reports commit-ancestor-valid; two honest findings (r23's missing Landed-changes heading; r13's documented operator-skip); two independent auditors, 13 rows re-verified, zero mismatches | `python3 reports/round-31/run-validation.py` | `reports/round-31/closure-ledger.json` + C04/C05 |
| operability | improved (claim O) | Piecemeal sweep -> the final green sweep: 50/50 capability rows exit 0, 13 filed-red historical controls at their codes, battery 10/10, the r31-post frozen generation replaying 4/4 (the r28-post supersession gap closed), all 50 recorded commands re-executed green | `python3 reports/round-31/run-validation.py` | `reports/round-31/final-sweep.md` + sweep/ |
| depth | improved (claim D — the jin'i-ryu self-improvement round) | The gate's required round: given the telemetry (5/5 availability records open-at-seat-close, 0 finalized; the r29 restate hazard), the lane proposed and landed ONE falsifiable improvement to its own operating files — the telemetry finalization-closure rule (AGENTS.md 'Close what you open' + SKILL.md checklist audit + five retroactive closing snapshots, append-only, digest-pinned) with a three-leg falsification condition recorded in LOG.md | `python3 reports/round-31/run-validation.py` | `reports/round-31/jinii/` + LOG.md gate entry |
| coverage / freshness / adjacency | unchanged | Pause in force; scope clean | — | — |

Admission: C/O/D verify, no axis harmed. Operator amendments 5-6 recorded
(Grok reaffirmed-skipped; sol->luna preference for future regimens). ONE ROUND
REMAINS: round 32 — the regimen's close.

## Axes — round 32 (2026-10-18), admitted (THE REGIMEN'S FINAL ROUND)

Baseline `4d50050`; one 16-worker `zai-coding-plan/glm-5.3-flash-low` (MAX
effort) final batch (12/16; late scribes landed before integration).
Acceptance: `python3 reports/round-32/run-validation.py` exits 0 — C/O/D PASS
(receipt at `reports/round-32/validation.json`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim C) | No end-to-end criterion certification -> completion-audit.md + completion-ledger.json: the completion criterion verified through round 31 — 24/24 rounds closed (20 admitted incl. r23 with its carried heading finding; 3 rejections r11/r17/r22 on record; r13 operator-skipped); 73 commit citations all ancestors of HEAD; rounds 1-7 retro re-confirmed; r32 by-construction; two independent auditors green; findings F-C32-1/F-C32-2 carried un-repaired | `python3 reports/round-32/run-validation.py` | `reports/round-32/completion-audit.md` + C04/C05 |
| operability | improved (claim O) | The r31 sweep predated r32 -> the r32 final sweep: the 50-command matrix + the r32 harness selftest, 51/51 green x3 passes, 13 filed-red controls at codes, battery 10/10, replays r17 5/5 + r31-post 4/4; sweep auditors: 128 independent re-executions, zero findings | `python3 reports/round-32/run-validation.py` | `reports/round-32/final-sweep.md` + sweep/ + audit files |
| depth | improved (claim D) | The dossier predated the Register-craft landing -> final-dossier.md: box 1's inventory condition CLOSED (28/28 at the current SKILL bytes); boxes 2-4 restated with r24 verdicts + loop-3 evidence; the full capability inventory (every SCORECARD capability with its demonstrated command); the operator's four decision materials — the dossier claims no promotion, it IS the decision's evidence | `python3 reports/round-32/run-validation.py` | `reports/round-32/final-dossier.md` + d11-d13 |
| coverage / freshness / adjacency | unchanged | Pause in force to the end; final scope watch clean (1,870 tracked paths) | — | `reports/round-32/scope.md` |

Admission: C/O/D verify, no axis harmed. THE REGIMEN IS COMPLETE: lane rounds
8-32 (25 rounds: 21 admitted, 3 rejected, 1 operator-skipped) + rounds 1-7
retroactive closure. Routed debt recorded for the operator: the falsifier
audit's filename mismatch (substance 5/5), 7 unindexed lessons, 12 standing
open items in the dossier, the promotion + freshness decisions.

## Axes — round 8 (2026-10-17), admitted

Baseline `cf338a713060f274269cdacb18cdc0085bb06aeb`; one 64-worker
`opencode-go/deepseek-v4.1-flash` batch (loop 1, build 1 of 4). Acceptance:
`python3 reports/round-8/run-validation.py` exits 0
(`reports/round-8/validation.json`, `reports/round-8/rerun.json`).
Owner action during integration: D2 packet regenerated to re-pin the
reader sha after the legitimate costume-gate repair — drift was caused by
in-round O repairs, not by the D tool.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D, capability `d2-typed-labels`) | No typed-label handling → `tools/d2-typed-labels.py` with five kinds, kind-by-declaration, borrow-ledger checks; selftest 39/39; D2 packet regenerates byte-identical; SKILL.md gains the label-typing decision table + 15 error-pattern rows with cited sources | `python3 tools/d2-typed-labels.py --selftest`; `python3 tools/assemble-d2.py --check` | `reports/round-8/depth/*`, `validation.json` claims.D |
| coverage | unchanged | 179 knowledge entries, same six partitions; metadata frontmatter repaired, no entries added or removed | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `reports/round-8/metadata/m0*.md` (11 shard fragments) |
| operability | improved (claim O) | Harness mis-rejected duplicate-parent-receipt controls → `tools/harness/r8_checks.py` fix with regression controls; 20 legacy defects inventoried, 10 isolated negative controls; battery 10/10 + craft 10/10 domain + 18/18 CLI controls green; round-3 manifests reproduce 7/7 isolated | `python3 tools/check-gate-battery.py --selftest`; `python3 reports/round-8/run-validation.py` | `reports/round-8/operability/*`, `battery-rerun.json` |
| freshness | improved (claim F, lowest non-retired) | 15 residual round-6 rows with no round-8 receipts → 15/15 receipts with fresh retrievals (215 distinct substantive passage keys per harness count), raw 15× supported split conservatively to 11 partial-support / 4 unresolved with basis text; passage support separated from whole-claim support by enforced controls; documented access failures carried | `python3 reports/round-8/run-validation.py` | `reports/round-8/freshness/R8-F*-receipt.{json,md}`, `reconciliation.json`, `audit.md` |
| calibration | improved (unclaimed observation) | Raw worker labels (15× "supported") preserved apart from reconciled dispositions; named access failures recorded per receipt (e.g. R8-F01: 6 documented failures); limits handed forward explicitly | `python3 reports/round-8/run-validation.py`; read `reconciliation.json` notes | 15 rows with raw/reconciled fields; `freshness/audit.md` spot-checks |
| adjacency | unchanged | No cross-domain bleed: handoff contract untouched by D work, PROVINCE still accurate, no out-of-lane writes (git-scope check); contract-digest drift vs lore's open r93 ratification escalated to L0, not absorbed | `git status` scope read; `reports/round-8/adjacency.md` | `adjacency.md`; fleet `.ufo/l0-questions.md` append |

Admission: F/O/D all verify and no axis is harmed. Exploratory content:
none declared. Limits: receipts are current-constraint rechecks, not new
historical certifications; the 4 unresolved rows stay open; the D tool's
holds are representation discipline, not clearance.

Capabilities addendum (round 8):

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| d2-typed-labels | Types D2 records across five kinds by declaration; enforces holds (TL-01/TL-02), borrow-ledger clock checks (B4), channel separation; emits typed projection | `python3 tools/d2-typed-labels.py --selftest`; `examples/culture-d2/typed-labels.d2.yml` | round 8 |

## Axes — round 9 (2026-10-17), admitted

Baseline `a7bb205`; one 64-worker `opencode-go-2/deepseek-v4.1-flash` batch
(loop 1, build 2 of 4). Acceptance: `python3 reports/round-9/run-validation.py`
exits 0 after two orchestrator integration acts (neither a work defect):
reconciliation rows normalized to the declared flat `raw_label` contract, and
the D3 `expected.json` freeze refreshed for three pins — all three drifts are
round-8's legitimate committed changes (two gate repairs, one contract
frontmatter repair) that round 8 re-pinned for D2 but not D3.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D, capability `culture-d3-acceptance`) | D3 capability unadmitted (round 7 closed failed) → `assemble-culture-d3.py --check` byte-identical, `check-evidence-coupling.py --selftest` green, frozen replay exit 0 / 0 findings after legitimate re-pin; contract cross-check + 2 adversarial reviews filed | `python3 tools/assemble-culture-d3.py --check`; `python3 reports/round-9/run-validation.py` | `reports/round-9/d3/*` |
| coverage | unchanged | 179 knowledge entries, same partitions; metadata verify sweep re-audited all frontmatter post-round-8 | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `reports/round-9/metadata/v0*.md` + audit.md |
| operability | improved (claim O) | 0 of 7 structural gates with committed drift-pin baselines → 7/7 with expected.json baselines (both `tools/gates/expected/` and `tools/gates/frozen/<gate>/r9-pre/` layouts), battery extension validates tampered → could-not-evaluate, audit confirms zero gate behavior changes | `python3 tools/check-gate-battery.py --selftest`; `python3 reports/round-9/run-validation.py` | `reports/round-9/baselines/*`, battery extension |
| freshness | improved (claim F, lowest non-retired) | 4 residuals unresolved after round 8 → 4/4 partial-support with 12 escalated-strategy receipts (primary/museum, scholarly fulltext, alternate angle) + 3 verifier reports + spot-check audit; raw labels preserved apart | `python3 reports/round-9/run-validation.py` | `reports/round-9/freshness/*` |
| calibration | improved (unclaimed observation) | Reconciliation carries flat raw label next to reconciled disposition with basis; 12+ named access failures documented per receipt; deeper-limit receipts name what remains unread | read `reports/round-9/freshness/reconciliation.json` | verification chain V01–V03 + audit.md |
| adjacency | unchanged (with conformance defect) | Two out-of-lane writes occurred (fleet-root `reports/round-9/metadata/v09-myth.md`, fleet-root junk PDF) and were swept/remediated by the orchestrator; scope defect recorded, X03 check missed it; L0 contract-digest question still open | `reports/round-9/adjacency.md` | fleet round notes; remediated in commit |

Admission: F/O/D all verify, no axis harmed. Conformance defects recorded:
(1) two out-of-lane worker writes, remediated by orchestrator sweep;
(2) `/tmp` inode exhaustion (100%) hit ≥5 shards — workers adapted with
in-lane scratch; operator cleanup decision pending (L0).

Capabilities addendum (round 9):

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| culture-d3-acceptance | D3 packet regenerates byte-identical; evidence-coupling green; frozen expectation replays clean | `python3 tools/assemble-culture-d3.py --check`; `reports/round-9/d3/replay.md` | round 9 |

## Axes — round 10 (2026-10-17), admitted

Baseline `eb348f3`; one 64-worker `opencode-go/deepseek-v4.1-flash` batch
(attempt 4 — keys -3/-4/-5 returned 402 insufficient funds, recorded in
`reports/round-10/availability-attempt-{1,2,3}.json`; 61/64 workers completed,
3 downstream scribes late-landed before integration). Acceptance:
`python3 reports/round-10/run-validation.py` exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | 179 entries, thin partitions unexpanded → 189 entries: linguistics 16→19, myth-symbol 16→19, culture-material 16→18, verification 13→15; each new entry gap-named, frontmatter-complete, decision-record carrying, source-resolving; README index reconciled | `python3 reports/round-10/run-validation.py` | `reports/round-10/coverage/*` (10 authors, 10 reviewers, 4 auditors) |
| freshness | improved (claim F, lowest non-retired) | No drift ledger → 192-row ledger, 36/36 cited commands covered; stale items fixed-with-evidence or documented; every ledger row command-carried with output hashes | `python3 reports/round-10/run-validation.py` | `reports/round-10/drift/ledger.json` + 14 shard fragments |
| operability | improved (claim O) | 24 open adversarial findings (rounds 8-9) → 24/24 dispositioned: 18 fixed-with-control, 5 wont-fix documented, 1 wrong; verifiers re-ran controls; battery selftest green | `python3 reports/round-10/run-validation.py` | `reports/round-10/findings-tracker.json` + verify fragments |
| depth | unchanged | No depth claim this round; D3 selftest 85/85 re-verified via ledger | — | ledger row SKILL.md:264 |
| calibration | improved (unclaimed observation) | Integrator caught and reverted a worker rewrite of filed round bytes (`reports/round-9/validation.json`, `reports/round-8/run-validation.py`); staleness documented instead of back-patched; 14 ledger rows re-measured at integration | git log of the two artifacts | conformance defect below |
| adjacency | unchanged | Fleet root verified clean this round; PROVINCE accurate | `reports/round-10/adjacency.md` | X02 fragment |

Admission: C/F/O verify, no axis harmed. Conformance defects recorded:
(1) one stale-fixer rewrote filed round-8/round-9 receipt bytes — reverted by
the integrator, staleness documented in the drift ledger instead;
(2) 3 workers failed late (scribe seats) and late-landed — no round defect;
(3) model availability: opencode-go keys -3/-4/-5 unprovisioned (402),
rotation now keys 1/2 only.

## Axes — round 11 (2026-10-17), NOT admitted (claim F failed as declared)

Baseline `e3ef171`; one 64-worker `opencode-go-2/deepseek-v4.1-flash` batch
(loop 1, build 4 of 4; 54/64 completed, 10 seats failed late — scribe-class
seats, no core-claim seat lost). Acceptance:
`python3 reports/round-11/run-validation.py`: D PASS, O PASS, F FAIL
(stability 0.778 < declared 0.95).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D verified) | Typed projection standalone; GAR labels on legacy sound channel → typed pipeline wired (new derived typed packet + typed-pipeline gate, five gate scripts untouched); e2e findings exactly == expected hold set (15: 10 D2L-FORM-UNRESOLVED, 2 D2L-NATIVE, 3 D2L-RANK); differential proves 10/10 PHON-INVENTORY artifacts gone; negatives (channel smuggle, silent form-drop, hold laundering) each caught | `python3 reports/round-11/run-validation.py` | `reports/round-11/depth/` (design, integration, tests, negs, reviews) |
| operability | improved (claim O verified) | No e2e handoff exercise → `tools/exercise-handoff-e2e.py` assembles a packet from live D2/D3 artifacts; 16/16 fields + 20/20 glossary entries; handoff-packet-check green in isolation; frozen expected.json baseline with tamper control | `python3 reports/round-11/run-validation.py` | `reports/round-11/handoff/` |
| freshness | unchanged (claim F failed as declared) | Recheck covered 192/192 ledger rows; 147 stable (0.778 < 0.95); all 45 drifts dispositioned with named causes (dominant: round-10/11 legitimate changes; environmental path embedding; 3 transcription defects incl. truncated ledger row 187); zero undispositioned drift | `python3 reports/round-11/run-validation.py` | `reports/round-11/recheck/` |
| coverage | unchanged | 189 entries; no coverage claim this round | — | — |
| calibration | improved (unclaimed observation) | Failed threshold reported, not gamed; transcription defects dispositioned; receipt schema defects repaired by integrator re-measurement | — | this section; `recheck/summary.json` |
| adjacency | unchanged | Fleet root clean; PROVINCE accurate; five gate scripts deliberately untouched (replay-frozen pin integrity) | `reports/round-11/adjacency.md` | X02 |

Round status: REJECTED — F misses its declared threshold; D/O verify; no axis
harmed. Freshness axis progression halts pending operator threshold
recalibration (queued at L0: a quiet-tree 95% assumption cannot hold across
build rounds that legitimately change the tree). Round-12 verify will audit
this round's evidence independently.

## Axes — round 12 (2026-10-17), admitted (verify round)

Baseline `69d0c21`; one 64-worker `openai-codex/gpt-6-luna-max` verify batch
auditing rounds 8-11 (25/64 completed — route capacity; coverage completed by
integrator re-measurement, 61 commands re-run, rows normalized to the licensed
disposition schema). Acceptance: `python3 reports/round-12/run-validation.py`
exits 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim C) | Rounds 8-11 unrecounted → 89-row recount ledger: 12 exact matches, 16 worker dispositions, 61 integrator coverage rows; round-11 rejection numbers independently reproduced, including the ratio correction (147/192 = 0.7656; 0.778 = 147/189 — both recorded) | `python3 reports/round-12/run-validation.py` | `reports/round-12/recount/` (16 receipts, ledger.json, dispositions.md, audit.md) |
| operability | improved (claim O) | No consolidated defect queue → 15-entry ledger: 7 fixed-with-control bounded (incl. rounds 8+9 filed-receipt clobber restored byte-exact from e1694ba/9dc18ec), 8 routed to round 14 with owner notes; regressions green | `python3 reports/round-12/run-validation.py` | `reports/round-12/defects/` (sweeps, fixes, routed.md, regression.md) |
| adjacency | improved (claim A) | Per-round posture → consolidated audit: 10 new entries PASS (3 boundary-sensitive: report existing legal facts, no lane rulings); PROVINCE accurate; handoff packet REJECTED on semantics — shape passes (16/16, 20/20) but claim-ledger uncertainty dimension + bilateral acknowledgment missing; zero unfiled bleed | `python3 reports/round-12/run-validation.py` | `reports/round-12/adjacency/` (entries, contract, province, ledger.json) |
| depth | unchanged | Audit round; no depth claim | — | — |
| coverage | unchanged | 189 entries confirmed by recount | — | recount r10-3 |
| freshness | unchanged (axis-move claims still paused) | Audit surfaced the filed-receipt clobber root cause (ledger commands that are round-runners); fix routed to round 14 | — | defects ledger FRR-12a/b |

Admission: C/O/A verify, no axis harmed. Key audit findings: (1) filed receipt
integrity broke for rounds 8+9 (restored; root cause routed); (2) handoff
semantics rejected — routes to round 13/14; (3) round-11 ratio-documentation
defect corrected in records. Conformance defects carried to round 14:
battery baseline roots, audit-count erratum, tracker verifier pointer,
draft-status reconciliations.

## Axes — round 33 (2026-10-19), ADMITTED (regimen 2, loop 1 build 1 of 3)

Baseline `139e3b662900557afe54f632b468619593dc9fcb`; one 64-worker
`opencode-go/deepseek-v4.1-flash` batch (key 1 of the round-robin; observed
64/64 completed — `reports/round-33/telemetry/observed-dispatch.json`).
Acceptance: `python3 reports/round-33/run-validation.py` exits 0
(`reports/round-33/validation.json`, receipt sha256 `93b28f36…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | c31 audit exit 1 (33 files vs 26 rows; findings `C31-1` + `C34-2`) → exit 0 (33/33/78, findings 0); README revision-3 bytes byte-equal the seats' verified reconstruction `f752e1d7…`; the round-32 falsifier debt (F-X16-3): `SKILL.md` one-liner false-fired 5 rows → content-keyed re-key prints 0 rows live + 11/11 isolated controls | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`; `python3 reports/round-33/run-validation.py` | `reports/round-33/op/lessons-reconciliation-receipt.json`; `op/O05-falsifier-disposition.md`; `validation.json` |
| calibration | improved (claim C) | No ledger, dossier items open → `calib/open-items-ledger.json` 12/12 rows dispositioned (OI-04/05/06/12 `fixed-with-evidence` with integrator-applied drafts + green controls: d2-typed-labels 163/163, box1-survey 28/28, packet_uncertainty 19/19; 8 carried with owner+reason+next-touch); the numeral "12" is reconstructed, not quoted — caveat carried (F-C15-1) | `python3 reports/round-33/run-validation.py` | `calib/open-items-ledger.json`; `calib/C13-consistency.md`; `calib/C14-fix-drafts.md` |
| adjacency | improved (claim A — lowest non-paused axis) | No consolidated audit since r29 → `adj/audit-assembled.md`: A01–A14 verdicts filed (green / named-finding with owner); handoff gate live re-run 16/16 + 20/20 + findings 0; scope watch clean at close (2655 tracked, protected roots 0 rows); zero unfiled bleed; contested items restated routed-not-absorbed | `python3 reports/round-33/run-validation.py` | `adj/audit-assembled.md`; `validation.json` |
| depth / coverage / freshness | unchanged | Freshness pause in force (operator ruling pending since r11); depth/coverage not claimed this round; no axis harmed | — | `claims.json` non_goals |

Admission: O/C/A verify and no axis is harmed. Findings on record: **F-C13-1**
(r5/r6/r7 receipts written in-tree 03:53:25Z–03:55:27Z and restored byte-exact;
guard-adoption gap; incident recorded in LOG.md); **F-C13-4** (membership
ruling: K03's twelve canonical; box-4 readings 3a/3b/3c out-of-set);
**F-C15-1** (the "12" is a reconstructed numeral). Supersessions recorded as
new rows: r26 runner README blob pin and r25 receipt `input_sha256` (revision-3
bytes); SKILL.md digest `79fe91d3…` → `f9bd07c2…`; AGENTS.md drafting residue
excised (42 → 40 lines). No new domain capability this round
(bookkeeping/instrument round). Operator directive recorded: outlined batch
counts per round (concurrency); integrator seats recorded in telemetry.

## Axes — round 34 (2026-10-19), ADMITTED (regimen 2, loop 1 build 2 of 3)

Baseline `da68a6d` (short id; expands to `da68a6d705e41f369f21e8607bfaab5b54077f84`);
one batch on `opencode-go-2/deepseek-v4.1-flash` (key 2 of the round-robin):
63 seats authored/dispatched/completed — the declared `seat_count: 64` vs 63
rows is recorded as the named CO4 deviation (digest-pinned, not edited).
Acceptance: `python3 reports/round-34/run-validation.py` exits 0
(`reports/round-34/validation.json`, receipt sha256 `ba2fa4dc…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D) | A02-H1 closed: the v3 default pair was shape-green but semantically stale (renderer verbatim-carried the 12 D4 claim rows from filed round-20 + a hard-coded OQ literal) → `declared-in-r7` built from live bytes (successor claims-map + six renderer edits); every D4/OQ figure equals a measured live value (d4_stale_audit CLEAN); gate 16/16 + 20/20 + 0; links 105/105; claims 27 (16/7/4); e2e exit 0, packet `45f57132…` == freeze.txt; r6 row refuses replay (exit 1, KeyError mechanism — named R34-N1) | `python3 reports/round-34/run-validation.py`; `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | `reports/round-34/handoff/declared-in-r7/`, `handoff/repin.json`, `validation.json` |
| operability | improved (claim O, capability `receipt-guard-adoption-audit`) | No adoption inventory (the F-C13-1 gap uninstrumented) → `tools/harness/receipt_guard_adoption.py` durable (selftest green) + inventory of all 29 filed runners: 18 guarded-refresh / 11 unguarded-in-place (r5-r12, r19, r21, r29), routing receipt covers every unguarded runner with the isolated-copy protocol; zero in-tree runner execution (r5/r6/r7 receipts == HEAD); r26 correction errata filed (it is guard-adopted) | `python3 tools/harness/receipt_guard_adoption.py --selftest`; `python3 reports/round-34/run-validation.py` | `op/adoption-inventory.json`; `op/O05-routing.md`; LOG.md errata |
| calibration | improved (claim C) | Box-1 evidence current only as console output at the old digest → durable receipt 28/28 at `f9bd07c2…` + A09 anchor reissue table built from the citation census (seven live stale cites re-issued as superseded readings; C09-F2 phantom-row guard); zero filed-row edits | `python3 -B reports/round-30/craft/box1-survey.py`; `python3 reports/round-34/run-validation.py` | `craft/box1-resurvey-durable.json`; `craft/anchor-reissue.md` |
| coverage / freshness / adjacency | unchanged | Freshness pause in force; coverage/adjacency not claimed; no axis harmed | — | `claims.json` non_goals |

Admission: D/O/C verify and no axis is harmed. Findings on record: **R34-N1**
(r6-row refusal surfaces as an unhandled KeyError, not E2E-DIGEST — routed to
renderer hardening); the **CO4 seat-count deviation** (64 declared vs 63
authored/dispatched — recorded, not edited); two seats (D17, X00) never landed —
coverage folded by siblings, recorded in `missing_dependencies`. Supersessions
as new rows: renderer default pair r6→r7, CLAIMS_MAP r20→r7 successor; the
filed r2..r6 packet rows and round-20 map stay byte-identical.

## Axes — round 35 (2026-10-19), ADMITTED (regimen 2, loop 1 build 3 of 3)

Baseline `4a7aede` (expands to `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`);
declared 64 workers on `opencode-go-3`, **observed route opencode-go key 1** —
keys 3/4/5 returned 402 insufficient funds (three recorded attempts, zero
launched; `telemetry/availability-attempt-{1,2,3}.json`); the batch completed
64/64 on the live-key fallback. Acceptance:
`python3 reports/round-35/run-validation.py` exits 0
(`reports/round-35/validation.json`, receipt sha256 `328e97b3…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | 201 entries (CM 18 / MS 19) → 211 (CM 24 / MS 23): ten sourced entries landed after the mid-wave allocation reconciliation (swap chain recorded); README revision 2.0 sweep-green (211 rows == 211 files); 10/10 entries audited by three independent seat auditors; C04's timekeeping alternate routed as a named spare | partition census; `python3 -B reports/round-28/readme/sweep.py`; `python3 reports/round-35/run-validation.py` | `corpus/knowledge/{culture-material,myth-symbol}/`; `cov/C13/C14/C17` audits; `validation.json` |
| operability | improved (claim O) | R34-N1 closed: superseded-row replay = unhandled KeyError → exit 1 `E2E-READSET` naming `reports/round-20/handoff/claims-map.md` (no traceback); m13a/m13b/m14a/m14b green; E2E-DIGEST/E2E-BASELINE paths preserved; r7 chain exit 0, packet `45f57132…` — zero freeze bytes moved | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`; `--profile v3 --selftest` | `op/O01/O02` drafts + applied bytes; `validation.json` |
| adjacency | improved (claim A) | No consolidated r33/34-surface audit → 13-surface assembled audit: zero unfiled bleed, PROVINCE accurate at HEAD (`c53782a`), findings F1-F13 owner-assigned; contested items routed-not-absorbed | `python3 reports/round-35/run-validation.py` | `adj/audit-assembled.md` |
| depth / freshness | unchanged | Freshness pause in force; depth not claimed; no axis harmed | — | `claims.json` non_goals |

Admission: C/O/A verify and no axis is harmed. Named records: the **route
deviation** (opencode-go-3 → key 1; key census 1-2 live, 3-5 dry); the
**allocation reconciliation** (P01 swap-rule swap chain, C03's placement);
the **timekeeping spare**; the integration repair (bad first control insertion
reverted and re-applied).

## Axes — round 36 (2026-10-19), NOT ADMITTED on D (loop 1, position 4)

Baseline `ce103bf`; declared hyper 32w -> observed devin fallback (hyper 402
out-of-credits; declared fallback) 32/32. Rejection receipt: `python3
reports/round-36/run-validation.py` exit 1 by design (`reports/round-36/validation.json`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | unchanged (claim D FAILED as declared) | Premise falsified: the register-form domain was already closed by r26/r27 (argot derived_pairs=8, law findings=0) — nothing landed under the failed claim; residue routed with K01's recipe | `reports/round-36/run-validation.py` (D leg carries the evidence) | `scout/K01-register-scout.md`; `validation.json` |
| coverage | improved (claim C) | 211 -> 212 (CM 24 -> 25): the routed timekeeping spare landed; README rev 2.1 sweep-green; named defects filed; rev-2.0 order repair | census + `python3 -B reports/round-28/readme/sweep.py` | `corpus/knowledge/culture-material/timekeeping-instruments.md`; `cov/` audits |
| calibration | improved (claim Ca) | No cross-round recount -> 17-row ledger: 15 match / 2 dispositioned mismatch | `reports/round-36/run-validation.py` | `calib/recount-ledger.json` |
| operability / freshness / adjacency | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Round status: REJECTED on D per the honest-stop rule (rounds 11/17/22
precedent). Named: the route deviation, the conformance incident (in-tree r35
runner execution, restored), the README prediction-vs-delivery nuance.

## Axes — round 37 (2026-10-19), ADMITTED (regimen 2, loop 1 position 5 — verify round)

Baseline `57c8409`; one 64-worker `openai-codex/gpt-6-luna-max` batch, 64/64
completed. Acceptance: `python3 reports/round-37/run-validation.py` exits 0
(receipt sha256 `616c1c14…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim Ca) | No cross-round recount of r33-36 → 34-row verify ledger: 25 match / 5 named mismatch (all legitimate later-tree or environmental deltas) / 4 could-not-reproduce (the O12 isolation hazard); two independent samplers | `python3 reports/round-37/run-validation.py` | `calib/recount-ledger.json`; Ca07/Ca08 |
| operability | improved (claim O) | Defects scattered across four rounds → 24-row dispositioned queue (fixed-with-evidence or carried-with-owner); new findings: A01 roster defect, contract-digest lore drift, O10 runner-sha256 null, O12 isolation hazard, basename-couples policy | `python3 reports/round-37/run-validation.py` | `op/defect-queue.json` |
| adjacency | improved (claim A) | The freeze-drift question adjudicated: 13-register-law.yml missing from the r7 read set = a roster defect (not a skip); pair re-renders faithfully; 334/334 couples resolve, zero bleed; r36 rejection preserved | `python3 reports/round-37/run-validation.py` | `adj/A01-freeze-adjudication.md`; A02/A06/A08 |
| depth / coverage / freshness | unchanged | Not claimed (verify round); no axis harmed | — | — |

Integration repairs recorded against the integrator: the round-35 README apply
left two `__E3_PLACEHOLDER__` lines (removed; sweep re-green — the r35
prediction-vs-delivery nuance's root cause); the r36 receipt's
`runner_sha256: null` (carried as O10; filed bytes never edited).

## Planned

- Round 36 REJECTED on D (C/Ca verified). Next: round 37 — loop 1 position 5,
  one 64-worker verify batch on `openai-codex/gpt-6-luna-max` auditing rounds
  33-36 (REGIMEN.md).
## Planned

- Round 35 ADMITTED — loop 1's opencode-go build trio is complete (r33-r35).
  Next: round 36 — loop 1 position 4, one batch of 32-64 workers on
  `hyper/deepseek-v4.1-flash` with the declared devin fallback
  (`devin/deepseek-v4-1-flash-high`) if hyper is exhausted (REGIMEN.md).
- Round 34 ADMITTED (see its table above).
- Rounds 8-10 + round 12 (verify) admitted; round 11 REJECTED (F threshold).
  Next: round 13, loop 1 expand round — 128 workers on `xai-oauth/grok-4.7-fast`.
  Candidate claims: D4 culture packet (typed pipeline on a fresh build),
  civilizations-partition recheck wave, handoff packet v2 closing the round-12
  semantic reject (uncertainty dimension + claim-to-record links). Freshness
  axis-move claims remain paused pending operator ruling.
- Operator regimen 2026-10-17, amended 3× same day (supersedes the older
  rounds 8–10 mapping; recorded in LOG.md): 3 loops × 8 rounds. Per loop:
  4 build (64w deepseek-v4.1-flash; opencode-go keys 1/2, **round 19 on the
  hyper provider**), 1 verify (64w `openai-codex/gpt-6-luna-max`), 1 integrate
  (32w `openai-codex/gpt-6.1-sol` max effort), 2 GLM rounds (16w
  `zai-coding-plan/glm-5.3-flash-low` = zai MAX thinking effort).
  **Loop-3 DeepSeek builds (rounds 25-28) run on the devin provider**
  (`devin/deepseek-v4-1-flash-high`) per operator directive 2026-10-18 —
  a provider test replacing the opencode-go/hyper lanes for those rounds.
  Amendments 5-6 (operator 2026-10-18): (5) the 128-worker xai-grok expand
  rounds remain SKIPPED (reaffirmed — none exist in the amended regimen);
  (6) where the regimen names a sol-max integrate round, luna max is the
  operator's preferred substitute — recorded for future regimens; the three
  integrate rounds of this regimen (r14/r22/r30) already ran on gpt-6.1-sol
  per the prior spec and closed rounds are never re-dispatched.
  **Expand (Grok) rounds cancelled by operator.** Lane rounds: loop 1 = 8–16
  (r13 operator-skipped), loop 2 = 17–24, loop 3 = 25–32 (24 dispatched +
  r13 skipped). Round-13 claims deferred: handoff-v2 + civ-map -> GLM rounds
  15–16; D4 -> a loop-2 build round. Original mapping:
  4 build rounds (one 64-worker swarm each, `opencode-go/deepseek-v4.1-flash`,
  rotating opencode-go key lanes), 1 verify round (64 workers,
  `openai-codex/gpt-6-luna-max`), 1 expand round (128 workers,
  `xai-oauth/grok-4.7-fast`), 1 integrate round (32 workers,
  `openai-codex/gpt-6.1-sol`, max effort). Lane rounds 1–6 closed
  retroactively and round 7 closed `failed` in MANIFEST.json rounds[]
  (no fleet report landed; never re-dispatch round 7).
- Round 8 declared (loop 1, build 1 of 4): claims F/O/D on
  freshness/operability/depth — F: follow up the 15 residual round-6
  reconciliation rows (11 partial-support, 4 unresolved) with fresh
  retrieved-passage receipts; O: repair the round-7 validation parent-check
  identity-collision defect plus the legacy selftest/parser debts from
  supplemental reviews 26/29, with isolated negative controls; D:
  `d2-typed-labels` capability (typed translated-label/native-form handling,
  scoped era/material reconciliation, executable rank-rule adapter).
  Declarations in `reports/round-8/claims.json`; shard assignments in
  `reports/round-8/targets.json`.
- Debts folded into rounds 9–28: corpus metadata conformance
  (`source`/`verified-at`/`recheck`), per-gate `expected.json` baselines,
  reproducible numeric axis rubric. Historical round-4 dispatch provenance
  remains incomplete (31 returns, no durable original request); do not
  fabricate it.

## Axes — round 38 (2026-10-19), ADMITTED (regimen 2, loop 1 position 6)

Baseline `9bccc9b`; declared grok-4.7-fast 32w → observed devin fallback
(grok 403 out-of-credits; named deviation) 32/32 across an interrupted dispatch
plus its 10-seat completion. Acceptance: `python3
reports/round-38/run-validation.py` exits 0 (receipt sha256 `88db61bf…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D) | r36 register residue landed: F-6 counters (derived_forms=8/derived_ok=8 live; corrected derived_failures formula; argot selftest 35) + the RL-8 era leg on the argot host emitting D4L-ARGOT-ERA (39/39 controls; planted-probe pipeline visibility; typed pipeline 20/20) | argot/law gates; typed pipeline; `python3 reports/round-38/run-validation.py` | `tools/gates/argot-derivation-gate.py` (sha 10c88433…); round-38 depth fragments |
| operability | improved (claim O) | the r7 read-set omission invisible → a named `manifest-roster` row on the r7 class (guard patch sha e5812751…; m15a/m15b controls; r7 chain exit 0, packet 45f57132… byte-identical); naming-not-detection recorded as the limit | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | round-38 op fragments (O01/O02/O03/O08) |
| coverage / calibration / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Named: the grok→devin route deviation; the interrupted-batch completion; the
0-byte O07 fragment; the RL-8 host decision (argot, per X01 T1 — the law-gate
host's battery pin cascade declined); the guard's row-blindness + O03's G5
four-row finding filed to the defect queue's successor.

## Axes — round 39 (2026-10-19), ADMITTED (regimen 2, loop 1 position 7)

Baseline `dfb0719`; one 16-seat `zai-coding-plan/glm-5.3-flash` batch as
declared (C05 concurrency-failed, re-dispatched; 16/16). Acceptance:
`python3 reports/round-39/run-validation.py` exits 0 (receipt sha256
`0fefcd56…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | verification 20 → 24, total 212 → 216: four sourced entries (worked-example, index-sweep, contact-strata gate, append-only-record), each audited pre-landing 4/4 PASS by C05; README rev 2.2 sweep-green 216==216 | census + `python3 -B reports/round-28/readme/sweep.py` | `corpus/knowledge/verification/`; `cov/C05-audit.md` |
| calibration | improved (claim Ca) | 4 could-not-reproduce recount rows → reproduced-under-protocol (the isolation-replay protocol: bwrap mount-namespace replay at close commit; Ca02 verified, successor ledger filed); the basename-couples fallback documented as policy | `python3 reports/round-39/run-validation.py` | `calib/isolation-replay-protocol.md`; `calib/recount-ledger-successor.json`; `calib/basename-couples-policy.md` |
| depth / operability / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Named: the C05 completion re-dispatch; the stray C03 staging file (removed,
digest-proven); K01's gaps G2-G4 routed; Ca04's two one-sentence defects;
R01-1's replay-mechanism ruling recorded in the successor ledger.

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
