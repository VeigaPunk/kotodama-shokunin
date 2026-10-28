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
| sources registry | Keep a curated, append-only registry of opened sources — tier scoped per claim, anchored to a revision, rejections kept with reason and flip, study paths and a search log — and census it with the fleet contract's seven commands | `corpus/SOURCES.md` (43 rows: A 34 / B 3 / C 6; mined 20 / queued 19 / rejected 4); `corpus/lessons/round-49.md` `## Gate`; `python3 reports/round-49/run-validation.py` S leg, measured at `8c78e6b` | round 49 |
| gate-line shape checker | Reports a lesson Gate row whose first quoted span repeats its locator (`doubled-locator`), whose Grounds is a proper prefix of the registry `teaches` cell (`truncated-grounds`), and quotes hidden by a hard wrap, guillemets, an ellipsis between spans or a `- * ` row; word rule stays a whitespace split | `python3 -B tools/check-gate-quotes.py <lesson.md>`; `--selftest` (24/24); `python3 -B reports/round-55/accept-o.py` exit 1 at `f4015e7`, exit 0 at `454a2dc` | round 55 |
| gate-line character-reference checks | Reports, once per row, a lesson Gate row carrying an HTML character reference (numeric, or an HTML5 named reference ending in `;`) as `html-entity`; applies the quote and Grounds rules to the decoded row; answers a lesson that is not valid UTF-8 with exit 2 and a `GATE_QUOTES_ERROR` line, no traceback | `python3 -B tools/check-gate-quotes.py <lesson.md>`; `--selftest` (38/38 at `7576fd4`); `python3 -B reports/round-56/accept-o.py` exit 1 at `b4b7db9`, exit 0 at `7576fd4` | round 56 |
| gate-line reference grammar with a mutation-killing selftest | Reports numeric character references with or without `;` (named only with `;`; invalid code points decode to U+FFFD) as `html-entity`, decoded once; its in-process selftest fails under double decoding, stop-at-first-unreadable-file and a renamed `html-entity` label, and passes under neutral patches | `python3 -B tools/check-gate-quotes.py --selftest` (52/52 at `43f1e781`); `python3 -B reports/round-57/accept-o.py` ACCEPT-O-57 FAIL at `13226c18`, PASS at `43f1e781`; controls `reports/round-57/telemetry/controls-o.txt` | round 57 |
| clause-scoping lint for cited lines | Reports every knowledge line carrying two or more distinct S-ids (`MULTI-ID`) and every table row carrying an S-id (`TABLE-ID`), with the summary `CITED-LINES: <k> finding(s) in <m> file(s)`, exit 1/0, and exit 2 with `CITED_LINES_ERROR` on no path, a missing path or invalid UTF-8; 603 findings on the base corpus, 0 on the footwear entry | `python3 -B tools/check-cited-lines.py <path>`; `python3 -B reports/round-61/accept-o.py` ACCEPT-O-61 FAIL at revision 0 `106df397` (no tool), PASS at `efbee29c` | round 61 |
| bounded row re-opener with archived fallback and caption verdict | Re-opens SOURCES rows: up to 3 attempts per URL on transient results (429, 5xx, timeout, connection error), more passes only after a transient failure (default 3 passes, 60 s apart), tries listed captures after the live URL and stops at the first body match; separates LOCATED body text from CAPTION_ONLY (figcaption, caption/thumbnail/gallery class or id, alt/title/aria-label/content/data-* attributes), ABSENT, UNREACHABLE and REFUSED (private hosts); one ROW line per argument, `REOPEN: k/m located`, exit 0/1/2 | `python3 -B tools/reopen-row.py [--registry PATH] [--passes N] [--gap S] S###…`; `--selftest` (32 checks); `python3 -B reports/round-62/accept-o.py` ACCEPT-O-62 FAIL at `9143fc44` (no tool), PASS at `a2c5caa5` | round 62 |
| row-fragment checker | Checks round-65 row fragments for 11-cell shape, tier/status/opened/used-by, quote length, teaches-cell character bound, capture/live URL normalization and cross-row URL duplicates; selftest and 26-file scan pass with 0 findings | `python3 -B tools/check-row-fragments.py --selftest`; `python3 -B tools/check-row-fragments.py` | round 65 |

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

## Axes — round 40 (2026-10-19), ADMITTED (regimen 2, loop 1 position 8)

Baseline `fd55e1f`; one 24-seat `zai-coding-plan/glm-5.3-flash` batch, 24/24.
Acceptance: `python3 reports/round-40/run-validation.py` exits 0 (receipt
sha256 `8b7b4508…`; the runner is the O12 relative-ROOT cure with non-null
`runner_sha256` — the N7 receipt-fidelity cure).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | linguistics 21 → 25, total 216 → 220: K01-r39's routed gaps G2-G4 landed; audits 4/4 PASS pre-landing (C05 + C07 independent); README rev 2.3 sweep-green 220==220 | census + sweep | `corpus/knowledge/linguistics/`; `cov/C05-audit.md` |
| calibration | improved (claim Ca) | r37-aged 24-row queue → 38-row owner-complete defect-queue-v2 (r38/r39 findings folded; the reviewers' five mandated rows + locator + ruling applied; 72.7% sample match) | `python3 reports/round-40/run-validation.py` | `op/defect-queue-v2.json` |
| adjacency | improved (claim A) | no consolidated r37-40 pass → every surface verdict-filed; PROVINCE byte-accurate; contested routed | `python3 reports/round-40/run-validation.py` | `adj/A03-verify-assembly.md` |
| depth / operability / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Named: the queue-v2 completeness catch (folded); N7 cured in this runner;
F-A02-1 routed (packet surface); the r39-runner root-regression finding
(O12 streak r34-r39, cured here); K02's fold cross-check carried to r41.

## Axes — round 41 (2026-10-19), ADMITTED (regimen 2, loop 1 position 9)

Baseline `456674d`; one 32-seat `openai-codex/gpt-6-luna-max` batch, 32/32 in
~7 min. Acceptance: `python3 reports/round-41/run-validation.py` exits 0
(receipt sha256 `1d3735d9…`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | no runner template/checker -> both durable; the 7-runner census classifies the r34-r39 streak per-runner (r39 mechanically caught duplicating r38's findings); r40 conformant as the reference | `python3 -B tools/harness/round_runner_conformance.py --selftest/--json` | `templates/round-runner-template.py`; `op/runner-census.json` |
| calibration | improved (claim Ca) | N3: multiple presumed stale live pins -> one self-marking historical hit (SKILL.md:383), ruled; N7 + r39-runner-root-regression re-classed fixed-with-evidence | `python3 reports/round-41/run-validation.py` | `calib/pin-supersession.json`; the queue update |
| depth / coverage / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Named: the seven-vs-eight census scope (r33 = precedent, streak = r34-r39);
the trap-output ambiguity; Ca02's optional SKILL delta carried.

## Axes — round 42 (2026-10-19), NOT ADMITTED on C (loop 1, position 10)

Baseline `ac47c78`; one 32-seat `devin/deepseek-v4-1-flash-high` batch (31/32 +
C05 completion). Rejection receipt: `python3 reports/round-42/run-validation.py`
exit 1 by design (`reports/round-42/validation.json`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | the wrapped couples field read as empty -> read whole (4/4 targets, successor extractor durable at tools/harness/, selftest green); the corrected census (223 entries / 2730 refs); the r39 policy truncation corrected by the full successor document | extractor --selftest; `python3 reports/round-42/run-validation.py` | `tools/harness/couples-reference-extractor.py`; `op/couples-extractor-census.json` |
| coverage | unchanged (claim C FAILED as declared) | myth-symbol 23 -> 26 (not 27), total 220 -> 223 (not 224): C01/C04 collided on the lithic register; C04 lands, C01 routed as the named spare; two existing entries momentarily overwritten by stale paths, restored byte-exact from HEAD; audits 4/4 PASS-with-defects | census + sweep | `cov/C05-audit.md`; `cov/C01-mineral-spare.md` |
| depth / calibration / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Round status: REJECTED on C (the r36 precedent). Named: the collision ruling;
the overwrite-restore incident (caught by census arithmetic); the r39
truncation (corrected append-only); K01's D1b/D1c/D1d finding family filed to
the queue's successor.

## Axes — round 43 (2026-10-19), NOT ADMITTED on O+C (loop 1, position 11)

Baseline `7ceff59`; scheduled `zai-coding-plan/glm-5.3-flash-low`, operator-
redirected to `opencode-go/deepseek-v4.1-flash` after three pre-completion
interruptions (a named deviation). One 32-seat batch, 16/32 filed. Rejection
receipt: `python3 reports/round-43/run-validation.py` exit 1 by design
(`reports/round-43/validation.json`, `rejected-honest-stop`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | unchanged (claim O FAILED as declared) | durable green resolver already exists at HEAD (`couples-reference-extractor.py` 8/8, census 223/2730); minting the claim-named `basename-couples-resolver.py` would fork the parser — the `before` was false. Residual hardening (blank-line terminator, ambiguous control, four-class census, disposition leg) is real but un-landed → could-not-evaluate / unprovable-but-better | `python3 tools/harness/couples-reference-extractor.py --selftest/--census`; `python3 reports/round-43/run-validation.py` | `scout/K01-resolver-scout.md`; `op/O09-scribe.md` (515-line verified successor draft, 27/27) |
| coverage | unchanged (claim C BLOCKED by collision) | lithic slot already owned by `mineral-stone-symbolism.md` (r42 C04); landing the C01 spare overwrites or duplicates → no corpus delta. myth-symbol 26, total 223, README stays rev 2.4 | census + `python3 -B reports/round-28/readme/sweep.py` | `cov/C06-collision.md`; `review/R01-review.md` §3 |
| calibration | improved (claim Ca) | four carried r38/r39 rows each reach a class with citation, zero dropped (19 findings / 22+ legs); filed with independent-verifier Ca02's measured amendments (D-3 recorded, R01-13 fixed at r40, R01-4 r39 citation) — no filed byte edited, all successor records | `python3 reports/round-43/run-validation.py` | `calib/dispositions-r38-r39.json`; `calib/defect-queue-v2-successor-r43.json` |
| depth / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Round status: REJECTED on O+C (honest stop; the second consecutive such).
Named: the stale-premises process defect (claims not re-measured at baseline
before dispatch — R01-43-12); the claims.json digest drift from three provider
redirects (re-pinned in `telemetry/availability-close-43.json`); the O09
verified successor draft carried to a future hardening round; the C01 spare
retired as superseded. Absent seats O01/O08/R02 recorded could-not-evaluate.

## Axes — round 44 (2026-10-19), NOT ADMITTED on C+Ca (loop 1, position 12; O improved)

Baseline `c9f4eaa`; scheduled `antigravity/gemini-3.8-flash`, operator-redirected to
`opencode-go/deepseek-v4.1-flash` after the antigravity lane aborted twice with zero
seat output ('skip the gemini and argon rounds'). One 32-seat batch, 14/32 filed —
18 seats failed on an opencode-go `reasoning_content` API error (provider defect).
Rejection receipt: `python3 reports/round-44/run-validation.py` exit 1 by design.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O) | no four-class census authority → `tools/harness/basename-couples-resolver.py` landed byte-exact (sha `43ce341f…`, the r43 O09 successor): 27/27 selftest, four-class census 2556+166+0+7=2729 +1 glob, 50 fallback mappings + 7 reasoned unresolved rows, 0-diff parity with the r42 witness (demoted-by-record, bytes `d8d23a26…` untouched); fixes blank-line over-capture + ambiguous/indented-prose/glob-precedence controls | `python3 tools/harness/basename-couples-resolver.py --selftest/--census` | `op/O02-verify.md`; `calib/couples-census-r44.json`; `op/O07-parity.md`; `op/instrument-of-record.md` |
| coverage | unchanged (claim C BLOCKED) | the only drafted gap candidate (dream/vision/trance) was already named at `reports/round-42/scout/K02-myth-gaps.md:216` (same slug) — 'not carried' fails under the strict reading; the fresh gap (cartography, K02) has no entry body. No landing; total 223, README rev 2.4 | census + `python3 -B reports/round-28/readme/sweep.py` | `scout/K02-gap-scout.md`; `review/R01-review.md` §3 |
| calibration | unprovable-but-better (claim Ca) | R01-43-12 stale-premises defect confirmed; scratch prototype flags r43 O/C stale + Ca fresh (exit 2 + REFUSE) but no durable gate exists and its selftest is red (17/19); all three Ca seats failed | — | `review/R01-review.md` §4; `cross/X01-trades.md` |
| depth / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Round status: NOT ADMITTED on C+Ca (O improved and landed — recorded without
averaging the C/Ca shortfalls into an accept). Named: the carried-candidate
collision (dream = r42 R2, the r43 defect class one level up); the 'not carried'
clause ruled strict per R01-44-09; the antigravity-lane outage deviation; the
opencode-go `reasoning_content` provider defect (18 failed seats).

## Axes — round 46 (2026-10-19), ADMITTED (loop 1, position 14 — git-hygiene audit)

Baseline `1dfb87f`; scheduled `devin/swe-2` (8-seat read-only audit). Run as an
integrator mechanical git census + a Devin-CLI swe-2 non-author reviewer. Acceptance
receipt: `python3 reports/round-46/run-validation.py` exit 0
(`reports/round-46/validation.json`, `admitted`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| adjacency | improved (claim A) | lane<->fleet boundary never audited → 14/14 loop-1 commits carry the lane identity; zero lane→fleet or fleet→lane writes; zero pushes/merges (lane ahead of origin = operator's pending push, local-first holds) | `git log --format='%an <%ae>'`; `git -C ../.. log --name-only -- kotodama-shokunin/{corpus,tools,reports}` | `audit/A01-commit-chain.md`; `audit/A02-boundary` (integrator census) |
| operability | improved (claim O) | append-only + receipt integrity never audited across the loop → zero post-landing edits except r40's two recorded supersessions (REFRESH_RECEIPTS + r41 defect-queue amendment, sha-pinned); all 12 validation.json present + committed + parse | `git log --diff-filter=MD -- reports/round-<N>`; `ls reports/round-<N>/validation.json` | `audit/O01-append-only.md`; `audit/O02-receipts` |
| calibration | improved (claim Ca) | MANIFEST fidelity never audited → all 12 loop-1 rows reconcile row-for-row to the lane receipts across both ledger schemas (8 admitted / 2 rejected / 2 honest-stop); zero discrepancies | parse `MANIFEST.json` + each `validation.json` | `audit/Ca01-manifest.md` |
| depth / coverage / freshness | unchanged | Read-only audit; freshness paused; no corpus delta | — | — |

Round status: ADMITTED — all three audit claims verify and no axis is harmed.
Named: the r40 supersession edits (recorded, sha-pinned); the two MANIFEST
ledger schemas (closure rows + per-lane rows); the swe-2 reviewer dispatched
as a successor artifact.

## Axes — round 47 (2026-10-19), NOT ADMITTED on C; O+Ca improved (loop 2, position 1)

Baseline `6e9a30d`; `opencode-go/deepseek-v4.1-flash` 64 seats — key-1 batch (50/64
filed) + operator-directed key-6 refire of the 14 missing seats (64/64 total).
Rejection receipt: `python3 reports/round-47/run-validation.py` exit 1 by design.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | unchanged (claim C BLOCKED) | verified-fresh cartography gap (0 owners) but the assembled entry is 790 lines vs live partition max 221 with 9 blocking defects (arithmetic, false source-accusation, mis-anchored cites, worked-example FAIL). Not landing-ready; repeats the r42/r44 collision if forced. total 223, README rev 2.4 | census + `python3 -B reports/round-28/readme/sweep.py` | `scout/K01-gap-recheck.md`; `review/R03-c-content.md` |
| operability | improved (claim O) | the R01-43-12 stale-premises defect closed: `tools/harness/claims-freshness.py` landed durable — selftest 62/62 (registry 43 + seam 19), r43 regression (O STALE 2/2, C STALE, Ca FRESH, exit 1 + REFUSE), negative control green (r47 3 FRESH, exit 0), anti-theater verified | `python3 tools/harness/claims-freshness.py --selftest` + `--claims … --checks …` | `tools/harness/claims-freshness.py`; `calib/r43-checks.json`; `calib/r47-checks.json`; `op/W01-landing-spec.md` |
| calibration | improved (claim Ca) | loop-1 defect reconciliation filed (3 defect rows + 2 provider amendments) with integrator corrections (zai-sentence fix, Ca05 re-pin); successor records only, parent sha-pinned | `python3 reports/round-47/run-validation.py` | `calib/queue-successor-r47.json` |
| depth / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Round status: NOT ADMITTED on C; O+Ca improved and landed (recorded without
averaging the C shortfall into an accept). Named: the coverage-over-build
defect (790-line entry, 3.6× partition max — the stale-premises class one level
up, now a build-quality miss); the freshness gate as the durable cure for
R01-43-12; the key-1/key-6 split dispatch.

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

## Axes — round 48 (2026-10-19), ADMITTED (loop 2, position 2)

Baseline `a01405d`; `opencode-go/deepseek-v4.1-flash` 64 seats (key-2 round-robin),
clean single-batch 64/64. Claims C + Ca (O dropped at declaration — the freshness
gate's first live use flagged its candidate premise stale). Acceptance receipt:
`python3 reports/round-48/run-validation.py` exit 0.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | verified-fresh cartography gap (0 owners, gate-confirmed at declaration) → `corpus/knowledge/culture-material/cartography-and-mapmaking.md` landed: 239 lines (C02 head + C01 body with R03's D1/D3/P2 fixes), 1 H1/14 H2/0 H3, inside ≤250 tolerance; nine r47 B-defects absent on assembled bytes; total 223 → 224, culture-material 25 → 26, sweep `rows 224 files 224`, topic_mismatch 0 | `python3 -B reports/round-28/readme/sweep.py`; `wc -l corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `cov/C01-entry.md`; `cov/C02-header.md`; `review/R03-c-content.md`; `cross/X03-overbuild.md` |
| calibration | improved (claim Ca) | live README duplicate H1 (lines 1/3, grep 2) → removed (grep 1) as a recorded act; the r47 over-build defect class → `calib/queue-successor-r48.json` fixed-with-evidence (parent `defect-queue-v2.json` sha-pinned, not edited); the sweep's heading blind-spot → `tools/check-readme-heading.py` (selftest 8/8, green on fixed README); rev-2.4 transposed prose vector repaired | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md`; `python3 -B tools/check-readme-heading.py`; `python3 -B tools/check-readme-heading.py --selftest` | `calib/Ca01-readme-fix.md`; `calib/Ca02-overbuild.md`; `calib/Ca05-heading-control.md`; `calib/queue-successor-r48.json` |
| operability | unchanged | Not claimed; the freshness gate (r47 deliverable) ran its first live use at declaration and dropped the stale O candidate — recorded as a gate success, not a round claim | `python3 tools/harness/claims-freshness.py --selftest` | `claims.json`; `telemetry/dispatch-declared.json` |
| depth / adjacency / freshness | unchanged | Not claimed; freshness paused; no axis harmed | — | — |

Round status: ADMITTED — both claims verify on the landed bytes and no axis is
harmed. Named: the D1 register-test/form-typology contradiction (resolved by
admitting the star chart + the cosmogram as a doctrinal-correspondence boundary
form); the residual `revision: 2.0` duplicate-header note (X01, not a blocker);
in-flight seat audits ran on non-final bytes — the integrator re-verified on the
assembled landed bytes (sweep + heading control + run-validation).

## Axes — round 49 (2026-10-19), ADMITTED by runner, pending non-author verification (loop 2, position 3; kaika wave 2)

Baseline `c42d675` (differs from the declared `78f77a6` only in round-49 framing files:
`git diff --name-only 78f77a6 c42d675 -- corpus tools SKILL.md` prints nothing).
Measured commit **`8c78e6b`** (work commits `c6a174d` + `8c78e6b`), replayed in a fresh
clone: `python3 reports/round-49/run-validation.py` → `verdict: admitted`, exit 0
(`reports/round-49/validation.json`). Dispatch: the declared 64-seat opencode-go key-3
batch had 402'd; this round ran one batched 11-seat L2 swarm (planner, connector, scout,
4 executors, scribe, reviewer, critic) plus 2 replacement executor seats after a provider
rate limit. Claims C/Ca declared in `claims.json`; S declared in
`claims-addendum-kaika.json` (kaika campaign slot).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | hunting/foraging production register unowned (0 filename owners; 2 partial topic owners — `algonquian.md:3` regional round, `semantic-fields-lexicon-building.md:3` lexicon field — the declared "0 true topic owners" was narrowed, critic finding) → `culture-material/hunting-foraging-subsistence.md` landed: 205 lines, 1 H1, 0 H3, 1 `- topic:`, 8-field head in order, 12 opened external rows + 53 in-corpus anchors; total 224 → 225, culture-material 26 → 27; sweep `rows 225 files 225`, topic_mismatch 0; no existing entry modified | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l`; `python3 -B reports/round-28/readme/sweep.py`; `python3 reports/round-49/run-validation.py` | `validation.json` claims.C; R49Reviewer PASS, R49Critic survives-with-conditions (`reports/round-49/integration/README.md`) |
| calibration | improved (claim Ca) | dangling `revision: 2.0` stub (README:55, introduced `57c8409`) → deleted, `grep -c '^revision: 2\.0' corpus/README.md` 2 → 1; class control `tools/check-readme-revisions.py` (dup/stub/order legs, selftest 11/11) exits 1 on base bytes, 0 now; the headless rev-1.9 body is a routed residual (`REVISION-ORPHAN` warning only) | `grep -c '^revision: 2\.0' corpus/README.md`; `python3 -B tools/check-readme-revisions.py --selftest`; `python3 -B tools/check-readme-heading.py` | `reports/round-49/integration/Ca-evidence.md`; `validation.json` claims.Ca |
| depth | improved (claim S, capability `sources registry`) | `corpus/SOURCES.md` absent, 0 rows → 43 opened rows (A 34 / B 3 / C 6; mined 20 / queued 19 / rejected 4), all seven contract census commands clean (malformed 0, no dup ids, no enum/tier-inflation, no missing used-by); `## Paths` 15 sequences, `## Search log` 3 notes, `## Leads (unopened)`; every row's URL/date/≤25-word quote in `corpus/lessons/round-49.md` `## Gate` | the seven census commands of `SOURCES-CONTRACT-v1.md`; `python3 reports/round-49/run-validation.py` | `validation.json` claims.S; Critic re-opened all 13 of S031–S043 |
| operability | unchanged, not harmed | `reports/round-25/audit/c31-lessons-index-audit.py` would have gone red on the new lesson (C31 unindexed + C34b drift) → lessons README revision 4 indexes it, `findings: 0`, selftest 28/28 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | `corpus/lessons/README.md` revision 4 |
| freshness / adjacency | unchanged | not claimed; freshness pause in force; connector found 0 sibling owners of the register (fleet-wide `topic:` sweep) | — | — |

Separability (recorded, not gating): `c_without_s` passed (every cited row id carries an
inline URL in the entry's `- source:` line); `s_without_c` passed (census clean with the
entry path removed from every `used-by`). Coupling named: 12 S rows list the entry as
`used-by`; the entry points to `corpus/SOURCES.md` at its shelf and recheck lines.
Non-author verification of the three verdicts is the orchestrator's (§6.6).

## Axes — round 50 (2026-10-21), NOT ADMITTED as declared: C and O improved, Ca one acceptance leg unmet (hyaku phase 2, first jj-colocated kotodama round)

Baseline `4ad2683`. Build wave landed at `1c779e4`; post-falsify fixes landed at
**`c8865c7`**, with final entry-only corrections at **`1923bfe`** (measured commit).
Receipt: `python3 -B reports/round-50/run-validation.py --tree <clone of 1923bfe> --base-tree <clone of 4ad2683>` → `acceptance_passed: true`, exit 0
(`reports/round-50/validation.json`). The runner's own acceptance passes for all three
claims, but Ca's declared leg "run on `reports/round-50/claims.json` exits 0" exits **2**
(`SEPARABILITY_INPUT_ERROR manifest is missing base, schema`); the runner measured the
substitute `separability/r50-manifest.json`, whose 0 findings depend on path spelling
(lesson R50-M6). The frozen claim is reported unmet, not redefined. Waves: build 73 seats
(ChousaR27R2), falsify 66 seats (validated payload dispatched unchanged by the replacement
L1 after the host crash); round total 139.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C) | pastoralism/husbandry register unowned (0 filename owners, 0 word-bounded topic owners) → `culture-material/pastoralism-animal-husbandry.md` (204 lines, 1 H1, 0 H3, one `- topic:`, 22 opened rows S048–S069 cited); total 225 → 226, culture-material 27 → 28; sweep rows 226 files 226, topic_mismatch 0; falsify-wave calibration/anchor repairs landed in `c8865c7` | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l`; `python3 -B reports/round-28/readme/sweep.py` | `validation.json` claims.C; `.ufo/waves/round-50/falsify/Review*`, `Reopen*` |
| operability | improved (claim O) | jj-colocation probe (v3: landed sha must equal the origin/main tip and the guard must refuse) false negatives 3/3 on base tools → 0/3 on `c8865c7` tools; false positives 0/4 both; receipt_guard selftest 45 → 71 controls (71/71), check-readme-revisions 11 → 15 (15/15); post-falsify: symref-outside-namespace fails closed, jj `refs/jj/root` HEAD handled, readme-revisions discovery bounded | `python3 -B reports/round-50/jj-colocation-probe.py --tools-root <tree>`; `python3 -B tools/harness/receipt_guard.py --selftest`; `python3 -B tools/check-readme-revisions.py --selftest` | `reports/round-50/telemetry/jj-probe-v1.txt`, `-v2.txt`, `-v3.txt`; `validation.json` claims.O |
| calibration | not verified as declared (claim Ca) | round-49 inseparable pair detected 0/1 → 1/1 (`check-claim-separability.py` on `r49-fixture.json` exits 1 naming C→S; selftest 56/56; QUALITY criterion 7 grounded in the r49 spot-check) — **but** the declared self-application leg on `claims.json` exits 2, and the substitute manifest's 0 hides a real C→REC (Gate-in-lesson) coupling | `python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json`; `... reports/round-50/claims.json` | `validation.json` claims.Ca; falsify CriticR50Manifest, ReviewSepTool, ScoutCaCount, ReviewCriterion7 |
| depth / adjacency / freshness | unchanged | not claimed; freshness pause (L0 round-11) in force; no axis harmed — lessons-index audit 3 findings at base → 0 after revision 5 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | `corpus/lessons/README.md` revision 5 |

Frontier step (not a claim): `corpus/SOURCES.md` 47 → 70 rows (A 34 → 51, B 6 → 12, C 7);
census `scripts/sources-census.sh validate kotodama` exit 0 at start and end. Non-author
verification of these verdicts is the hyaku closure's.


## Axes — round 51 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 3, attempt 3)

Claim base `bff83ba`; declaration `1f97472`; D landed `35f0d49`, falsify fixes `e6b6629`; C landed `da31d3c`, falsify fixes `364eeff`; records `9feb69e` and the closing records commit. Receipts: `reports/round-51/telemetry/declaration-dry-run.txt` (before), `reports/round-51/telemetry/final-measures.txt` (after, measured on `364eeff` plus uncommitted records). Waves: build 36 seats, falsify 41 seats; round total 77 (`.ufo/waves/round-51/`).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| depth | improved, bounded (claim D, repair-first) | pastoralism §2 boundary table `rows=11 resolved=11 distinct=11` → `rows=15 resolved=15 distinct=15`, exit 0; repairs only the row-count leg of the round-50 routed debt 2. Disclosed: the inherited `civilizations/` row is a directory, so 14 of 15 rows carry a `path:line` anchor; falsify seats failed two new rows as first landed, fixed in `e6b6629` | `python3 -B reports/round-51/boundary-count.py` | `.ufo/waves/round-51/falsify/ReviewDRow*.md`, `RerunDCounter.md`, `CriticDRepairScope.md` |
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 226 → 227; linguistics 25 → 26; sweep exit 0, footer total 227; every cited S-id resolves with the entry in `used-by`; sign languages and manual communication had 0 filename and 0 topic-line owners at base | `find corpus/knowledge -name '*.md' \| wc -l`; `python3 -B reports/round-28/readme/sweep.py` | `corpus/knowledge/linguistics/sign-languages-manual-modality.md`; falsify `RerunCCount.md`, `ReviewCSec*.md`, `Reopen*.md` |
| calibration | not claimed; recorded | separability self-application on the round-51 manifest: 0 findings, exit 0 at `9feb69e` and `364eeff`; QUALITY criteria 8 and 9 (9 supersedes 8 after the falsify wave showed 8 was one-directional) | `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` | `corpus/lessons/round-51.md` R51-M1, R51-M5 |
| operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 70 → 131 rows (S071–S122 mined, S123–S125 and S127–S131 queued, S126 mined); census exit 0 at start and end. Non-author verification is the hyaku closure's.

Correction (appended in round 53, 2026-10-22; round-52 closure, routed defect 3, `corpus/lessons/round-52-verifier-spotcheck.md:138-140`). The frontier line above was filed in the round-51 records commit `10f433c`, the same commit that flipped S081 `mined` → `queued` (`corpus/lessons/round-51.md:127`), and it was not updated to match. At the round-51 tip `2b956d7` the split for S071–S131 is 52 mined and 9 queued: S071–S122 except S081, plus S126, are mined; S081, S123–S125 and S127–S131 are queued. Re-measure: `git show 2b956d7:corpus/SOURCES.md | awk -F'|' '/^\| S(07[1-9]|0[89][0-9]|1[0-2][0-9]|13[01]) /{s=$9; gsub(/ /,"",s); c[s]++} END{for(k in c) print k, c[k]}'`. The line above stays as filed; `SHONEN.md:8` carries the corrected split since `9ae5af9`.

## Axes — round 52 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 3, attempt 1)

Prerequisite `147cfde` (QUALITY criterion 10, `tools/check-source-access.py`, S094 rejected via S132, S133); declaration `d9f73c8`; D landed `dea5ece`, wording fixes `5b7ecfb`; C landed `7cee23b`; records in the closing records commit. Receipts: `reports/round-52/telemetry/declaration-dry-run.txt` (before), `reports/round-52/telemetry/final-measures.txt` (after). Wave: one build wave of 35 seats (`.ufo/waves/round-52/`); no falsify wave (seat gate timeouts, then Main's freeze).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| depth | improved, bounded (claim D, repair-first) | sign-language entry lines citing S094: 5 → 0, exit 0; the movement and orientation pairs re-sourced to S096 (NAME/SHORT, CHAIR/NAME), the passive-hand set to S097 (seven shapes, Type-3 signs); the unverifiable 1974 set marked `(to-verify)` | `awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md` | `.ufo/waves/round-52/build/ReviewDLines.md` (5 of 5 lines PASS), `CriticClaimD.md` (two wording fixes landed in `5b7ecfb`) |
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 227 → 228; linguistics 26 → 27; C acceptance exit 0 (49 cited S-ids, all S134 or above, each with the entry in `used-by`); the sweep run on its own exits 0 with 228 rows vs 228 files | `find corpus/knowledge -name '*.md' \| wc -l`; `python3 -B reports/round-28/readme/sweep.py` | `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`; `reports/round-52/telemetry/final-measures.txt`. Disclosed: the acceptance argv's sweep leg is weaker than the statement (R52-M3) |
| calibration | not claimed; recorded | QUALITY criterion 10 added from the round-51 outside disagreement; SHONEN lines 6 and 8 corrected after a seat found 2 mismatches with observed state (`ReviewShonenScorecard.md` M1, M2) | `python3 -B tools/check-source-access.py` | `corpus/lessons/round-52.md` R52-M1 to R52-M3 |
| operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 131 → 183 rows (S132 rejected, S133 queued, S134–S183 opened this round with S178 rejected); census exit 0 at start and end. Non-author verification is the hyaku closure's.


## Axes — round 53 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 3, attempt 1)

Prerequisite `9ae5af9` (S184 registers the UNESCO 00172 nomination file and entry line 104 cites it; S185 and S186 supersede S145's locator and S157's access note; SHONEN line 8); claim instruments `a9cf95f`; declaration `60f1d2a`; D landed `374ae5a`; C landed `47ec825`, falsify fixes `e0f9505`; records in the closing records commit. Receipts: `reports/round-53/telemetry/declaration-dry-run.txt` (before), `reports/round-53/telemetry/final-measures.txt` (after, with per-clause red controls). Waves: build 39 seats, falsify 32 seats (5 died at spawn with "No model selected"); round total 71 (`.ufo/waves/round-53/`).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| depth | improved, bounded (claim D, repair-first) | speech-surrogates entry: `d-count.py` OPEN 18 → 0, SID_BAD 0 → 0 (10 draft-id fragments, 2 wrong-row citations, 6 over-read phrases routed by the round-52 closure); line count and cited S-id set kept (`clauses.py` D1, D2). Disclosed: the routed "primitive peoples" item was itself wrong (R53-M3) | `python3 -B reports/round-53/d-count.py` | `.ufo/waves/round-53/build/ReviewDS*.md`, `ReviewDWrongRows.md`; falsify `ReviewDLines*.md` |
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 228 → 229; linguistics 27 → 28; `accept-c.py` exit 0 (README sweep exit 0, rows 229 files 229, missing 0; 51 cited S-ids, all S187 or above, mined, used-by the entry). Disclosed: "one new entry" and the topic are checked only by the record script `clauses.py`, not by the declared commands (R53-M2; the claim-sizing class for the third round running) | `find corpus/knowledge -name '*.md' \| wc -l`; `python3 -B reports/round-53/accept-c.py` | `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`; falsify `CriticLearningClaim.md`, `CriticCRestatement.md`, `CriticCClaimSizing.md` |
| calibration | not claimed; recorded | SHONEN line 8 and the round-51 frontier line corrected (appended note); QUALITY criterion 11 added from R52-M3 and R53-M2; `tools/check-draft-ids.py` (11 findings at the round-52 tip, 0 now) | `python3 -B tools/check-draft-ids.py` | `corpus/lessons/round-53.md` mistakes R53-M1 to R53-M3 |
| operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 183 → 238 rows (S184–S238 opened this round; S233 retired as a duplicate of S219); census exit 0 at start and end. Non-author verification is the hyaku closure's.


## Axes — round 54 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 3, attempt 2)

Prerequisite `d761ee8` (attempt 1: round-53 routed fixes; not a claim); claim instruments `4b2299b`, revised `260c68d` (claim base); declaration `7fa37fb` (one claim); attempt-2 dispatch records `5757c45`; C landed `6a658ca`, falsify fixes `58b2fae`; records in the closing records commit. Receipts: `reports/round-54/telemetry/declaration-dry-run.txt` (before), `reports/round-54/telemetry/criterion11-controls.txt` (13/13, replayed byte-identical by ExecControlsReplay), `reports/round-54/telemetry/final-measures.txt` (after).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 229 → 230; culture-material 28 → 29; `accept-c.py` exit 1 (SET, SWEEP, FLOOR FAIL) → exit 0, seven legs PASS (rows 230 files 230, missing 0; 46 cited S-ids, all S239 or above, one row each, mined, used-by the entry; ACCESS exit 0). Gap at base: 0 filename owners, 1 topic-line owner (`civilizations/siam-thai.md`); the build-wave critic found section-level owners in civilization entries (igbo, haudenosaunee, hopi, yoruba, fon-dahomey, siam-thai), which §2 points to one-way. Disclosed: the topic, sentence support and one-way pointing are review-only clauses | `python3 -B reports/round-54/accept-c.py` | `corpus/knowledge/culture-material/masks-masquerade.md`; `.ufo/waves/round-54/residual/` |
| depth / calibration | not claimed; recorded | prerequisite `d761ee8` repaired gesture and speech-surrogates lines (one locator over-corrected, see the lesson); `tools/check-gate-quotes.py` added (R54-M1): round-53 lesson 12 findings, round-54 lesson 0 | `python3 -B tools/check-gate-quotes.py corpus/lessons/round-54.md` | `corpus/lessons/round-54.md#mistakes` |
| operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 238 → 284 rows (S239–S284 opened this round, all mined; statuses 194/34/10 → 240/34/10); census exit 0 at start (`reports/round-54/telemetry/census-start-a2.txt`) and end. Non-author verification is the hyaku closure's.

## Axes — round 55 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 1)

Instruments `d44309a`, revised after the two pre-dispatch critics at `f4015e7` (claim base); declaration `8eda954`; routed fixes (not claims) `b9c44a2`, `81178c8`, `d52c9df`; O landed `454a2dc`; C landed `eb0a331`; records in the closing records commit. Receipts: `reports/round-55/telemetry/declaration-dry-run.txt` (before), `reports/round-55/telemetry/criterion11-controls.txt` (C 14/14), `reports/round-55/telemetry/criterion11-controls-o.txt` (O 16/16), `reports/round-55/telemetry/final-measures.txt` (after). Waves: build 51 seats, falsify 33 seats (`.ufo/waves/round-55/`).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 230 → 231; myth-symbol 26 → 27; `accept-c.py` exit 1 (SET, SWEEP, FLOOR FAIL) → exit 0, seven legs PASS (rows 231 files 231, missing 0; 73 cited S-ids, all S285 or above, one row each, mined, used-by the entry; ACCESS exit 0). Gap at base: 0 filename owners; partial owners pointed to one-way in §2. Disclosed: topic, sentence support, one-way pointing and the lore handoff are review-only clauses | `python3 -B reports/round-55/accept-c.py` | `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md`; `.ufo/waves/round-55/falsify/` |
| operability | improved (claim O, capability `gate-line shape checker`) | `accept-o.py` exit 1 (DOUBLED count 0, TRUNC count 0, EXIT and ESCAPE FAIL) → exit 0, eight legs PASS (exactly the 13 doubled and 17 truncated round-54 rows the closure routed; S901, S902, S904, S905 on the round-54 adversarial fixture; round-53 findings unchanged; selftest 24/24). Disclosed: KEEP53 reads only `words=` lines and the set legs ignore line numbers (`.ufo/waves/round-55/build/CriticClaimO.md`) | `python3 -B reports/round-55/accept-o.py` | `tools/check-gate-quotes.py` at `454a2dc`; `.ufo/waves/round-55/build/ExecGateShapes.md` |
| calibration | not claimed; recorded | round-54 closure routed defects 1-4 dispositioned (errata for 17 grounds and 13 locators, S358 supersedes S256's tier, S248/S254/S275 anchors, four of five escape classes); gesture line 68, speech-surrogates line 79, divination line 72 corrected; mistakes R55-M1 to R55-M4 | `python3 -B tools/check-gate-quotes.py corpus/lessons/round-54.md` | `corpus/lessons/round-55.md` |
| depth / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 284 → 358 rows (S285–S357 opened this round and cited by C; S358 supersedes S256, queued); statuses 240/34/10 → 313/35/10; census exit 0 at start (`reports/round-55/telemetry/census-start.txt`) and end. Non-author verification is the hyaku closure's.

## Axes — round 56 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 1)

Instruments `052f145`, revised after the two pre-dispatch critics at `045f458` (claim base); declaration `b4b7db9`; pre-dispatch receipts `456f5ad` (each names the revision it measured); O landed `7576fd4`; C landed `767040e`; records in the closing records commit. Receipts: `reports/round-56/telemetry/declaration-dry-run.txt` (before, measured-revision `b4b7db9`), `criterion11-controls.txt` (C 18/18), `criterion11-controls-o.txt` (O 23/23), `final-measures.txt` (after, names its revision). Waves: build 46 seats, falsify 37 seats (`.ufo/waves/round-56/`).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 231 → 232; civilizations 94 → 95; `accept-c.py` exit 1 (SET, SWEEP, FLOOR FAIL) → exit 0, seven legs PASS at `767040e` (rows 232 files 232, missing 0; 54 cited S-ids, all in C's block S359-S418 (S359-S412 used), one row each, mined, used-by the entry; ACCESS exit 0). Gap at base: 0 filename owners, one passing mention. Disclosed: topic, sentence support and the lore handoff are review-only clauses; the falsify wave's row slices are listed in the lesson | `python3 -B reports/round-56/accept-c.py` | `corpus/knowledge/civilizations/kongo-kingdom.md`; `.ufo/waves/round-56/falsify/` |
| operability | improved (claim O, capability `gate-line character-reference checks`) | `accept-o.py` exit 1 (ENTITY count 0, EXIT, DECODE FAIL, BADUTF8 exit 1 with traceback) at `b4b7db9` → exit 0, eight legs PASS at `7576fd4` (exactly the 16 round-55 entity rows, once each; ten fixture findings plus a run-time moved copy; rounds 49-54 output unchanged; invalid UTF-8 exit 2; selftest 38/38). Disclosed: the acceptance cannot tell a faithful decoder from an S-id-keyed shortcut (R56-M3); the falsify mutants left double decoding and stop-at-first-bad-file alive | `python3 -B reports/round-56/accept-o.py` | `tools/check-gate-quotes.py` at `7576fd4`; `.ufo/waves/round-56/build/ExecGateEntity.md` |
| calibration | not claimed; recorded | round-55 closure routed defects 1-6 dispositioned (lesson intake table); QUALITY criterion 7 amended (exact export block); S292, S293, S309 registry cells corrected; mistakes R56-M1 to R56-M4 | `python3 -B tools/check-gate-quotes.py corpus/lessons/round-55.md` (16 html-entity findings) | `corpus/lessons/round-56.md` |
| depth / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Correction rows for round 55 (routed defect 2 of `corpus/lessons/round-55-verifier-spotcheck.md`; the filed rows are not edited):

| corrected row | correction | re-run command |
|---|---|---|
| round-55 calibration row ("mistakes R55-M1 to R55-M4") | the round-55 lesson carries six mistakes, R55-M1 to R55-M6 | `grep -c '^\| R55-M' corpus/lessons/round-55.md` → 6 |
| round-55 capability row and operability row ("selftest 24/24") | 24/24 is the selftest at `454a2dc` only; 12/12 at `f4015e7`; 27/27 at `173cab6` and at the round-55 tip `2935c47` | `git show <rev>:tools/check-gate-quotes.py > /tmp/t.py && python3 -B /tmp/t.py --selftest` in a scratch copy (`.ufo/waves/round-56/build/ScribeScorecardNits.md`: 3 of 12 round-55 cells mismatched) |

Frontier step (not a claim): `corpus/SOURCES.md` 358 → 412 rows (S359-S412 opened this round and cited by C; S413-S418 of C's block unassigned); statuses 313/35/10 → 367/35/10; census exit 0 at start (`reports/round-56/telemetry/census-start.txt`) and end. Non-author verification is the hyaku closure's.

## Axes — round 57 (2026-10-22), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 1)

Instruments `6f08c494`, revised after the two pre-dispatch critics and before any data at `0314aa98` (claim base); declaration `13226c18` (dry-run `286288f4`, measured-revision named); O landed `43f1e781`; C landed `78d83b5e`; records in the closing records commit. Pre-data control receipts: `reports/round-57/telemetry/controls-o.txt` (16/16 as expected, including the round-56 S-id cheat and the critic's green), `controls-c.txt` (7/7: base, four sourceless or reflected stubs, a copied-rows stub). Waves: pre-dispatch 2, build 50, residual 8 (`.ufo/waves/round-57/`).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | improved (claim C, learning claim, sourced claim) | knowledge files 232 → 233; myth-symbol 27 → 28; ACCEPT-C-57 FAIL (SET, SWEEP, FLOOR, LOCATE) at `13226c18` → PASS at `78d83b5e`, nine legs (42 cited S-ids S413-S454, one row each, mined, used-by the entry; LOCATE 40/42 live, need 34; FRESH no reused registry URL; ACCESS exit 0). Surface: frontier → core, a heraldry/identity-mark topic with 0 filename owners (`git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ciE 'herald\|emblem\|kamon\|tamga\|insign'` 0 → 1). Shortcut defeated: the sourceless stub passes the eight other legs and fails LOCATE (controls-c). Review-only: topic, sentence support, one-way pointing, lore handoff | `python3 -B reports/round-57/accept-c.py` | `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`; `.ufo/waves/round-57/build/` |
| operability | improved (claim O, capability `gate-line reference grammar with a mutation-killing selftest`) | ACCEPT-O-57 FAIL (GEN 5/5 and REAL 3/3 failing on bare numeric references; MUTANTS three survivors) at `13226c18` → PASS at `43f1e781`, seven legs (selftest 38/38 → 52/52). Surface: the checker's reference grammar and its selftest's kill set. Shortcuts defeated before data: S-id keyed, short-list, any-ampersand, file-hash selftest, seed replay, generator-text keyed, function-identity selftest | `python3 -B reports/round-57/accept-o.py` | `tools/check-gate-quotes.py` at `43f1e781`; `.ufo/waves/round-57/build/ExecGateBareNumeric.md` |
| calibration | not claimed; recorded | round-56 closure routed defects 1-7 dispositioned (lesson intake); QUALITY criterion 10 amended (third-party scans); superseding rows S481-S491; errata for koon1244 and R56-M3; mistakes R57-M1 to R57-M3 | `grep -c '^\| R57-M' corpus/lessons/round-57.md` | `corpus/lessons/round-57.md` |
| depth / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; no axis harmed by an observed check | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 412 → 465 rows (S413-S454 opened this round and cited by C; S481-S491 superseding rows, queued); census exit 0 at start (`reports/round-57/telemetry/census-start.txt`) and end. Non-author verification is the hyaku closure's.



## Axes — round 58 (2026-10-23), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 2)

Instruments `91fb8fd9`, revised five times before any data seat (`a43f5336`, `c42121f4`, `edecdc90`, `1a07344e`, claim base `80f48c2c`) because pre-data controls met each earlier counter; control receipts `97577f6c` (`reports/round-58/telemetry/controls-c.txt`: 123 fixtures, 0 pass); pre-data dry-run `adc28834`; C landed `ddc17f4a`; support verdicts `a7e47abd`; records `e27c8a67`, `45bb7e1a`.

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | NOT VERIFIED as declared (claim C, learning claim, sourced claim) | knowledge files 233 → 234; linguistics 28 → 29; 44 rows S500-S543 cited, mined, used-by the entry; 13 of 15 legs PASS on every final run, SUPPORT 44/44 SUPPORTED by six non-author reviewer seats; but ACCEPT-C-58 printed FAIL on 4 of 4 live final runs (`a7e47abd` once, `e27c8a67` twice, `45bb7e1a` once), each time on one fetch-class error at an Australian government host (S510 `environment.nt.gov.au` BOILER, S511 `www.land.vic.gov.au` BOILER/TOPIC) while the same rows pass when checked alone; the frozen LOCATE/BOILER/TOPIC legs allow no slack, so the miss stands. Separability also finds C's acceptance needs `.ufo/waves/round-58/support/`, a path C's declared lands omit | `python3 -B reports/round-58/accept-c.py` | `reports/round-58/telemetry/final-measures.txt`; `corpus/lessons/round-58.md` |
| calibration | not claimed; recorded | round-57 closure defects 1-6 dispositioned (lesson intake); QUALITY criterion 12 (re-test stated rejection grounds); superseding rows S560-S562, S564-S574; S575 re-sources heraldry :41; S576 registers CODH bukan; errata for round-57.md:92 and :119; mistakes R58-M1 to R58-M6 | `grep -c '^| R58-M' corpus/lessons/round-58.md` | `corpus/lessons/round-58.md` |
| depth / operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; the kongo-kingdom and speech-surrogates fixes were re-verified but not applied (carried) | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 465 → 525 rows (S500-S543 opened this round and cited by C; S560-S562, S564-S576 records rows); census exit 0 at the base (run late on a base clone) and at the end after the kind-enum correction (`reports/round-58/telemetry/census-*.txt`).


## Axes — round 59 (2026-10-23), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 1)

Instruments `39c9ce8a` (revision 0), declaration `1b80ee41`, revision 1 and freeze `d4795abd` after an 8-seat pre-data control wave (one control met revision 0; `reports/round-59/telemetry/controls-c.txt`), claim base set `ff802cc3`; D landed `b2b2bde9`; packet-key hash `f7375cec`; C landed `4abfb63d`. Final receipt `reports/round-59/telemetry/final-measures.txt` (measured revision `4abfb63d`).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | author: PASS on the landed revision, with a disclosed post-review removal (claim C, learning claim, sourced claim) | knowledge files 234 → 235; myth-symbol 28 → 29; ACCEPT-C-59 FAIL at `ff802cc3` → PASS at `4abfb63d`, 15 legs (43 cited rows S600-S647, 40 hosts; SUPPORT: 8/8 seats qualified, 24/24 planted blocks rejected). The as-reviewed entry citing 47 rows printed FAIL on SUPPORT only (4 rows each rejected by one reviewer); those 4 rows were filed `rejected` and their lines removed after the verdicts. The operator rules whether that removal is admissible curation or a post-data narrowing. Surface: frontier → core, protective objects (`git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ciE 'amulet\|talism\|apotrop'` 0 → 1) | `python3 -B reports/round-59/accept-c.py` | `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md`; `reports/round-59/telemetry/as-reviewed-c.txt` |
| depth | improved (claim D) | ACCEPT-D-59 FAIL (14 old strings, old ids 16/2/3/2/4) at `ff802cc3` → PASS at `b2b2bde9` (first run) and at `4abfb63d`: kongo-kingdom.md carries the 14 frozen fixes (third carry closed), speech-surrogates cites S570-S574 | `python3 -B reports/round-59/accept-d.py` | `reports/round-59/telemetry/final-measures-d.txt`, `final-measures.txt` |
| calibration | not claimed; recorded | round-58 closure defects 1-8 dispositioned (lesson intake); errata for revision count, freeze wording, control count, separability; QUALITY criterion 13 | `grep -c '^| R59-M' corpus/lessons/round-59.md` | `corpus/lessons/round-59.md` |
| operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question | — | — |

Correction rows for round 58 (filed rows not edited): the round-58 instrument was revised six times before data, not five (`31cf8b6` added TOPIC); its "123 fixtures, 0 pass" holds only as a whole-predicate count — 18 failed only SUPPORT, 17 of them for a missing registry (`corpus/lessons/round-59.md` Errata).

Frontier step (not a claim): `corpus/SOURCES.md` 525 → 573 rows (S600-S647 opened this round; 43 mined, 1 queued, 4 rejected); census exit 0 at start (`reports/round-59/telemetry/census-start.txt`) and end.

Correction rows for round 59 (recorded in round 60; routed defects 1-3 of `corpus/lessons/round-59-verifier-spotcheck.md`; filed round-59 rows not edited):

| corrected row | correction | evidence |
|---|---|---|
| round-59 coverage (`ACCEPT-C-59`, author-side PASS) | **MISSED** on the as-reviewed 47-row object: 14 legs PASS, SUPPORT FAIL on S602, S616, S623, S643; the four propositions were deleted 12 s after the FAIL receipt; run 2 at `84b931a5` printed FAIL (legs lost to `tail -3`). The narrowed object is not the judged object. | `reports/round-59/telemetry/as-reviewed-c.txt`; `reports/round-59/telemetry/final-measures.txt` run 2; spot-check §2 |
| round-59 separability `C->REC via acceptance` | a live-fetch re-run artifact, not a dependency (no REC land read by `accept-c.py`; C passed alone at `4abfb63d`) | spot-check §2 and §5 item 3 |


## Axes — round 60 (2026-10-23), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 3)

Instruments revision 0 `b60e6d4e` … revision 9 `a56b04fc` (revisions 5-9 in attempt 3, each before any data seat, forced by the pre-data control waves `.ufo/waves/round-60/w1-a3/` and `.ufo/waves/round-60/resid-a3/`); claim-D build `1cd9db7c`; freeze `47f27bd0`; support verdicts and final measure in the closing commit.

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| depth | **MISSED** (claim D, sourced claim, S648-S651) | ACCEPT-D-60 FAIL at the claim base `b9faed93` (SET, LINES, ROWS, PINNED, JUDGED, SUPPORT) → FAIL at the measured revision: SET, LINES, OLDWORD, ROWS, PINNED, JUDGED PASS; SUPPORT FAIL (14 NOT-SUPPORTED on mapped ids, 13/24 seats qualified). Surface moved but not admitted: four round-59 propositions restored in source-scoped wording, 19 base lines narrowed; the judged entry stays as built (no post-verdict change). | `python3 -B reports/round-60/accept-d.py` | `reports/round-60/telemetry/final-measure.txt`, `before-measure.txt`; `corpus/lessons/round-60.md` |
| calibration | not claimed; recorded | round-59 corrections (C MISSED, separability artifact), round-59 errata, QUALITY criterion 14, mistakes R60-M1..M7 | `grep -c '^| R60-M' corpus/lessons/round-60.md` | `corpus/lessons/round-60.md` |
| coverage / operability / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question | — | — |

Frontier step (not a claim): `corpus/SOURCES.md` 573 → 577 rows (S648-S651 opened this round, mined); census exit 0 at start (`reports/round-60/telemetry/census-start.txt`) and end (`census-end.txt`).


## Axes — round 61 (2026-10-23), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 1)

Instruments revision 0 `106df397` (dry-run `78ad4b17`); revision 1 and freeze `2f4f8a40`, forced by the 36-seat pre-data control wave (`.ufo/waves/round-61/w1/`; re-score receipts `reports/round-61/telemetry/controls-c-rescore.txt`, `controls-o-rescore.txt`); O landed `675d59af`; C landed `efbee29c` (measured revision). Receipt: `reports/round-61/telemetry/final-measures.txt` (the first and sole authoritative claim-measurement runs; the declared separability check later re-ran both acceptances in temporary copies as a dependency check, `reports/round-61/telemetry/separability.txt`). Observed before-values come from the revision-0 dry run `106df397` (`reports/round-61/telemetry/declaration-dry-run.txt`); the revision-1 absent-land FAILs at the freeze are inferred, not separately run (CriticFreezeC F6).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| coverage | **MISSED** (claim C, sourced claim, S652-S692) | ACCEPT-C-61 FAIL before landing (observed at revision 0 `106df397`: SET, SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE) → FAIL at `efbee29c` on LOCATE alone: 13 of 14 legs PASS, 41 cited rows, 40 located; S671's live URL answers 403 and its only capture erred at 09:58Z. Surface moved but not admitted: knowledge files 235 → 236 (`git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ciE 'footwear\|shoe\|sandal'` 0 → 1). Nothing amended after the receipt | `python3 -B reports/round-61/accept-c.py` | `corpus/knowledge/culture-material/footwear-codes-terminology.md`; `corpus/lessons/round-61.md` R61-M4 |
| operability | improved (claim O, capability `clause-scoping lint for cited lines`) | ACCEPT-O-61 FAIL before landing (observed at revision 0: tool absent, all six legs) → PASS at `efbee29c`, six legs (GEN 92/92 on a random tree, REAL 603/603 on the base corpus including amulets line 95 `S612,S613`, ERR exit 2 ×3). Surface: a new lane tool. Review-only: the tool's own selftest (26/26) | `python3 -B reports/round-61/accept-o.py` | `tools/check-cited-lines.py` at `675d59af`; `.ufo/waves/round-61/w1/ExecLintTool.md` |
| calibration | not claimed; recorded | round-60 corrections (void breakdown, X60, pypdf seven seats, missing Gate heading, revision 5, R60-M6 lines 69/95/120, S646 = SupportB60 P01); QUALITY criterion 15; mistakes R61-M1..M6 | `grep -c '^| R61-M' corpus/lessons/round-61.md` | `corpus/lessons/round-61.md` |
| depth / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; ConnectSiblings found no sibling owner of footwear or a cited-line lint | — | `.ufo/waves/round-61/w1/ConnectSiblings.md` |

Correction rows for round 60 (recorded in round 61; routed defects of `corpus/lessons/round-60-verifier-spotcheck.md` §5; filed round-60 rows and report not edited):

| corrected row | correction | evidence |
|---|---|---|
| round-60 report structure and controls | no `## Gate` heading (Gate content under `## SHONEN`, lines 55/57); line 46's "five pre-data controls" is three met controls (CtlNarrowA3, CtlKeyedLabelA3, MutEvidenceA3) plus RescoreConfineA3's evasion; revision 5 was forced by the L1's review (`revision_note_5`), not a control receipt | `.ufo/reports/round-60/kotodama.md` lines 10, 46, 48-59 |
| round-60 depth row ("13/24 seats qualified") and R60-M7 | the 11 unqualified seats are 5 `bash-cwd-outside-sandbox` (A, P, Q, R, V), 4 `deny:chr(` (D, F, L, W), 1 `kotodama` (S), 1 bare X2 with no verdicts (U); SupportX60 was qualified and counted | `reports/round-60/telemetry/final-measure.txt`; `grep -c '^VERDICT ' .ufo/waves/round-60/support/SupportU60.md` → 0 |
| round-60 install record | `pypdf==5.4.0` via `uv run --with` in seven seats: RescoreMechA3, MutEvidenceA3, CtlNarrowA3, CtlGenericA3, CtlKeyedLabelA3, AuditA3R15, CtlRubberStampA3 | `.ufo/waves/round-60/w1-a3/AuditA3R15.md:95`, `CtlRubberStampA3.md:149` and the five lines named in the lesson |
| R60-M6 | the S612 packet joined entry lines 69, 95 and 120 | `reports/round-60/build-packets.py:50-52`; `.ufo/waves/round-60/support/packet-SupportD60.md` P05 |
| registry teaches cells | S646 joins S601, S608, S614, S624, S636, S640, S641 as superseding-row candidates; its finding is SupportB60 P01 (P07 is PLANTED) | `.ufo/waves/round-60/support/planted-key.json`; `SupportB60.md` |

Frontier step (not a claim): `corpus/SOURCES.md` 577 → 618 rows (S652-S692 opened this round, mined, used-by the footwear entry); census exit 0 at start (`reports/round-61/telemetry/census-start.txt`) and end (`census-end.txt`).

## Axes — round 62 (2026-10-23), author-side verdicts, pending non-author closure (hyaku phase 4, attempt 1)

Instruments revision 0 `f0173481`; revision 1 `e6a61e82`, forced before any data by the 37-seat pre-data control wave (`.ufo/waves/round-62/w1/`; re-score receipts `reports/round-62/telemetry/controls-rescore.txt`, LOCATE paired control `locate-control.txt`); freeze `9143fc44`; O landed `e605603c`; D landed `a2c5caa5` (measured revision). Receipt: `reports/round-62/telemetry/final-measures.txt` (first and sole authoritative runs, 12:05-12:08Z).

| axis | verdict | before → after / observation | re-run command | evidence |
|---|---|---|---|---|
| depth | author: PASS (claim D, sourced claim, S693) | ACCEPT-D-62 FAIL at the freeze `9143fc44` (SET, OPEN, HEDGE, CAPTION, SOLE, ROWS, LOCATE; `declaration-dry-run-rev1.txt`) → PASS at `a2c5caa5`, 16 legs: footwear lines 63 (open list), 74 (caption named), 75 (hedge and attribution), 93 (talaria on tier-B S693 instead of tier-C S687) repaired in place; S693 located live on pass 1. Surface: the four routed lines (`git show <rev>:corpus/knowledge/culture-material/footwear-codes-terminology.md \| sed -n '63p;74p;75p;93p'`). Review-only: support beyond shared words | `python3 -B reports/round-62/accept-d.py` | `corpus/lessons/round-62.md`; `.ufo/waves/round-62/resid/` |
| operability | author: PASS (claim O, capability `bounded row re-opener with archived fallback and caption verdict`) | ACCEPT-O-62 FAIL at `9143fc44` (no tool, all nine legs) → PASS at `a2c5caa5`: GEN 53/53 rows, ORDER with repeated ids, BOUND with no unlisted request, EXIT incl. default registry, PRIV, DEFAULT (9 requests, bursts [3,3,3], gaps 60/60 s, 150 s), ERR. Surface: a new lane tool (`test -f tools/reopen-row.py` false at `d42ffb89`). Post-measure review (outside the predicate): HIGH redirect-to-private SSRF and a ValueError traceback on malformed URLs, routed to round 63 | `python3 -B reports/round-62/accept-o.py` | `tools/reopen-row.py` at `e605603c`; `.ufo/waves/round-62/w1/ExecReopenTool.md` |
| calibration | not claimed; recorded | round-61 closure defects 1-5 dispositioned (lesson intake); QUALITY criterion 16; mistakes R62-M1..M5 | `grep -c '^| R62-M' corpus/lessons/round-62.md` | `corpus/lessons/round-62.md` |
| coverage / freshness / adjacency | unchanged | freshness stays paused by the open round-11 L0 question; ConnectSiblings: nearest prior art `chousa-shokunin/tools/quote-reopen.py` (no archive fallback, no caption verdict), no sibling owns footwear or talaria | — | `.ufo/waves/round-62/w1/ConnectSiblings.md` |

Correction rows for round 61 (recorded in round 62; routed defect 3 of `corpus/lessons/round-61-verifier-spotcheck.md`; filed rows not edited):

| corrected row | correction | evidence |
|---|---|---|
| round-61 calibration row ("mistakes R61-M1..M6") | the round-61 lesson records seven mistakes, R61-M1..M7 | `corpus/lessons/round-61.md:108-114` |

Frontier step (not a claim): `corpus/SOURCES.md` 618 → 619 rows (S693 opened this round, mined, used-by the footwear entry; S687 used-by → `—`); census exit 0 at start (`reports/round-62/telemetry/census-start.txt`) and end (`census-end.txt`).

Safety hold (appended after filing, Main directive 2026-10-23): the round-62 capability `bounded row re-opener with archived fallback and caption verdict` (`tools/reopen-row.py`) is unsuitable for use pending a defensive repair of redirect validation and malformed-URL handling plus an independent review. Do not run it on live URLs or against private/local services. The filed rows above are unchanged. See `corpus/lessons/round-62.md` `## Safety hold`.

## Axes — round 63 (2026-10-23, hyaku run 5 attempt 1, L1 KotodamaR63), admission pending non-author closure

Baseline `65b393e`; freeze `80d53ff`; one v2 wave 69 seats + residual 6; round total 75.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O, capability repair under hold) | r62 tool followed cross-authority redirects to private hosts and trace-backed on malformed URLs (closure HIGH) → repaired tool `0d965ccb` at `dd81fd29`: frozen counter ACCEPT-O-63 rev0 FAIL at base (all 9 artifact legs) → PASS at the measured tip; review gate RevToolA/B/C + RevHoldLift `VERDICT: NO-OPEN-HIGH-MED`; hold lifted per QUALITY | `python3 -B reports/round-63/accept-o.py` | `reports/round-63/telemetry/final-measures-o.txt`; `.ufo/waves/round-63/w1/RevTool{A,B,C}.md` |
| coverage | improved (claim C, sourced) | 0 filename owners of the headgear register (partial owners cited one-way in the entry §6) → `headgear-head-covering-codes.md` (51 lines, 24 cited bullets) + rows S694-S717 (A 14 / B 10); corpus 236 → 237 entries, culture-material 30 → 31; sweep rows 237 files 237 topic_mismatch 0; ACCEPT-C-63 FAIL at base (FILE/ROWS/APPEND/NOHARM/SWEEP/LIVE) → PASS at the measured tip | `python3 -B reports/round-63/accept-c.py` | `corpus/lessons/round-63.md` `## Gate`; `reports/round-63/telemetry/row-verify.txt` |
| calibration | not claimed; recorded | seven pre-data counter revisions, each committed with its forcing control receipt; CtlCJunkRow homograph/subset residuals and MutToolNeutral drip residual disclosed, not prettified | `grep -c 'revision ' reports/round-63/claims.json` | `.ufo/waves/round-63/w1/Ctl*.md`, `Mut*.md`, `RevCounter*.md` |
| depth / freshness / adjacency | unchanged | freshness pause in force (round-11 L0); ConnectSiblings: nearest prior art `chousa-shokunin/tools/quote-reopen.py`; no sibling owns the headgear register | — | routed-defect records in LOG |

### Round-63 corrections (appended 2026-10-23 in round 64, claim Ca)

| item | correction |
|---|---|
| tier histogram (round-63 closure defect 3) | the coverage row above says "A 14 / B 10"; the frozen census over S694-S717 prints **A=13 B=11** — S702 is tier B (`docs`). Re-derive: `git show ff30a205c8d23b35f1ac533740121a955a9fda96:corpus/SOURCES.md \| awk -F'\|' '/^\|[[:space:]]*S(69[4-9]\|7[01][0-9])[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for (k in n) printf "%s=%d ", k, n[k]; print ""}'` → `A=13 B=11`. |
| dead evidence pointer (defect 2) | the operability row above now cites `reports/round-63/telemetry/final-measures-o.txt`; the claim-C receipt is `reports/round-63/telemetry/final-measures-c.txt`. Both exist at `ff30a20` (`test -f`). The round-63 receipt → measured revision map is `reports/round-63/telemetry/revisions.txt` (defect 8). |
| numeric nits (defect 9) | round-63 landed **47** seat reports under `.ufo/waves/round-63/w1/` (the round-63 report says 45); the census **W04** warning covers **27** duplicate-URL rows (`scripts/sources-census.sh validate … \| grep -c W04` → 27), not S650/S651; the ACCEPT-O-63 dry run lists **9** FAIL legs (GEN/ORDER/BOUND/REDIRECT/MALFORMED/GZIP/TRUNC/TIMEOUT/REVIEW), not 6. Measurements re-run in round 64 at `ff30a20`. |
| separability (defect 10) | the round-63 re-run printed `SEPARABILITY: 2 findings` with `exit=1` (`reports/round-63/telemetry/rev-separability.txt`); the dependency class is a **record dependency** — the acceptance counters are REC lands, so each unit's `accept-*.py` is carried by the records unit, never an inter-claim dependency. Round-64 LOG entry records it. |

## Axes — round 64 (2026-10-23/24, hyaku run 5, L1 kotodama-r64; launch 5 after attempts 1–4 died to orchestrator failures)

Baseline `ff30a205`; declaration + instruments `097c21d`; measured at the claim-C land `95c9194ef938e1338b2af894086a46e8b8677ee2` (parent `6f3e0b24`). Two v1 waves (32+32) + one 6-seat residual repair call; round total 70 seats + L1 integration; dead seat: CriticRevC (provider policy refusal; scope absorbed by RevVerifyC). Acceptance: `python3 -B reports/round-64/accept-{c,o,ca}.py --root .` all print every leg PASS, exit 0 (receipts `reports/round-64/telemetry/final-measures-{c,o,ca}.txt`).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, sourced) | 0 filename owners / 0 topic-line owners of language socialization & acquisition → new entry `linguistics/language-socialization-and-acquisition.md` (81 lines, 26 cited bullets) + 26 mined rows S718-S743 (A 14 / B 12) + six disposition rows S744-S749 (3 rejected + 3 queued candidates) curating the round-63 routed defect 7; corpus 237 → 238 entries, linguistics 29 → 30, registry 643 → 675 (S687 mined → queued, logged old→new); blind-support ring: all 26 SUPPORTED after repairs (S719 re-hedged, S729 re-sourced to Neer et al. 2025 after the duplicate-of-S718 finding, S739 re-anchored to Results, S735/S728/S742 bounded, S722 locator fixed, S721/S726/S737 tier-honest B); ACCEPT-C-64 FAIL at base (dry-run-c.txt) → PASS 11/11 at `95c9194e` | `python3 -B reports/round-64/accept-c.py --root .` | `final-measures-c.txt`; `corpus/lessons/round-64.md` `## Gate` (32 rows); `res/ResVerifyRows.md`; sweep exit 0 (`reports/round-28/readme/sweep.py`) |
| operability | improved (claim O, counter hardening) | round-63 counter had no EDGE_/DRIP legs (grep exit 1) and a fail-open `--only` → frozen counter rev5 pins seven redirect-edge properties + DRIP, fail-closed `--only` (unknown selector exit 2), m5 isolation check; unchanged tool passes 23/23 incl. MUT (10 mutants kill their pinned legs; m5 exactly, isolation-verified); rev4 byte state shipped an uncompilable m5 — caught by three independent rebuilds, red receipt preserved, repaired pre-data as rev5; ACCEPT-O-64 PASS at `95c9194e`, tool byte-equal to base | `python3 -B reports/round-64/accept-o.py --root .` | `final-measures-o.txt` (+ `-rev3`/`-rev4` red/`-rev5` named variants); `w2/RevVerifyO2.md`; mutants/ sources |
| calibration | improved (claim Ca, bookkeeping + corrections) | round-63 closure routed defects 1,2,3,4,8,9,10 unresolved → all repaired and verified leg-by-leg (canonical log entry; dead pointers fixed; A=13 B=11 histogram; r62 items 5–7 dispositions; revisions.txt written then provenance-corrected in place; 47/27/9 numeric nits; record-dependency separability named); ACCEPT-CA-64 PASS 7/7 at `95c9194e`; revisions.txt prose overstatements corrected with evidence; claims.json C statement patched (disposition rows) | `python3 -B reports/round-64/accept-ca.py --root .` | `final-measures-ca.txt`; `w2/ReviewerCa.md`, `w2/CaReceipts.md`; `reports/round-63/telemetry/revisions.txt` |
| depth / freshness / adjacency | unchanged | freshness pause in force (round-11 L0); no new derivations or craft tables; adjacency: ConnectorOverlap ×2 — topic stays in-lane, lore handoff one-way, nearest prior art `chousa-shokunin/tools/quote-reopen.py` | — | `w1/ConnectorOverlap.md`, `w2/OverlapRe.md` |

Admission: C/O/Ca verify at `95c9194e`; no axis harmed (sweep + NOHARM diff = exactly the new file; filed rounds 51–63 rows append-only). Not claimed: counter gaming surfaces scored post-hoc (teaches-copy near-miss, Ca global-token legs, NITS denial-prose, O filtered-mode partial greens, mutant exclusivity beyond m5) — routed to round 65, listed in LOG; exploratory-claim count 0.

Frontier step: registry 643 → 675 rows; census exit 0 at start (`census-start.txt`, `census-wave1.txt`) and end (`census-end.txt`); mined rows S718-S743 used-by the entry; S687 flipped mined → queued (old → new logged in `corpus/lessons/round-64.md`); six disposition rows advance the round-63 reject curation; lesson `corpus/lessons/round-64.md` carries `## Gate` (32 rows + disposition evidence) and `## Mistakes` (R64-M1..M19).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

### Round-63 corrections (appended 2026-10-23 in round 64, claim Ca) — superseded pointer
See the round-63 corrections table above (carried into this round's Ca claim and verified at `95c9194e`).

## Axes — round 65 (2026-10-24, hyaku run 5, attempt 1 after stale-claim reset; L1 kotodama-r65-2)

Baseline `17c32302`; declaration + instruments `f107e849`; one v2 wave of 64 items validated under policy v2 and rendered to `.ufo/waves/round-65/taskcall-prepared-unissued.json`, but this attempt has no dispatch event in the parent log. The inherited `w1/` directory contains 54 `.md` seat artifacts; 10 spec item names have no report, and no last-error text is retained. Role mix in the prepared payload: 14 reviewers + 9 critics + 6 mutation-testers = 29/64 attack roles (45.3% ≥25%); the L1 holds the canonical planner seat. The 8 missing row fragments were opened by the L1; round-65 total is 0 dispatched L2 seats + L1 integration (the inherited files are not counted as this attempt's seats).

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, sourced; author-side counter PASS, review-only not independently closed) | 0 word-bounded filename owners at base; a topic-line keyword sweep finds two partial hits (musical contests, wheeled toys), not whole-register owners (`w1/RevClaimC.md`); the new entry now points one-way to four substantive partial owners. → `corpus/knowledge/culture-material/games-play-sport-contests.md` (126 lines, 26 cited bullets) + 26 mined rows S750-S775 (tier A 8 / B 18) + README reconciliation; corpus 238 → 239, culture-material 31 → 32; registry 675 → 701; ACCEPT-C-65 PASS 10/10 at `3b1b5a67`; LIVE subset 6/6 | `python3 -B reports/round-65/accept-c.py --root .` | `reports/round-65/telemetry/final-measures-c.txt`; lesson `## Gate`; sweep receipt |
| operability | improved (claim O, counter hardening + capability `row-fragment checker`) | Round-64 counter-gaming surfaces routed to this round → full ACCEPT-O-65 PASS 26/26 at `3b1b5a67`; FULL re-executes unfiltered (23/23), MUT kills all 10 pinned behaviors, MUTEX exact table matches the committed sweep with no traceback, FRAG selftest + 26-file scan reports 0 findings. An earlier same-bytes full run failed MUTEX with three tracebacks; a later full run passed and both are preserved (`accept-o-full-initial.txt`, `final-measures-o.txt`). Tool `tools/reopen-row.py` remains byte-equal to base. | `python3 -B reports/round-65/accept-o.py --root .` | `reports/round-65/telemetry/final-measures-o.txt`; `exactness-sweep-o65.txt`; `accept-o-full-initial.txt` |
| calibration | improved (claim Ca, records) | Round-64 spot-check defects R1-R7 unresolved → all dispositioned in A: final-measures-ca.txt re-stamped to `8bab271c` with tree `0ec0e50e`, original bytes preserved (R1); revisions.txt named correction (R2); w1/ReviewerCa.md actual path named (R3); claims.json statement_correction keeps predicate byte-unchanged (R4); control-o revision-3 binding named (R5); lesson R64-M12 status corrected (R6); round-64 entry verified-at corrected (R7); QUALITY criterion 17 added. R1-R7, CRITERION, QUOTES pass at A; RECEIPTS is pre-records red, then passes at B after the three A-stamped receipts land. | `python3 -B reports/round-65/accept-ca.py --root .` | `reports/round-65/telemetry/final-measures-ca.txt`; `accept-ca` post-record output in round report; `.ufo/waves/round-64/w2/LessonFinal.md` |
| depth / freshness / adjacency | unchanged | freshness pause in force (round-11 L0); no new derivations; ConnectorOverlap ×2: topic stays in-lane, lore handoff one-way, nearest prior art `chousa-shokunin/tools/quote-reopen.py`; S771 carries an explicit interested-source caveat | — | `w1/ConnectorSiblings.md`; entry calibration section |

Author-side: C and O full counters pass at lands A; Ca's R1-R7/CRITERION/QUOTES pass at A and its RECEIPTS leg passes on the post-record re-run at B. No observed axis harm; C's topic-line matches are partial scopes, disclosed above; non-author closure is still required. `check-claim-separability.py` timed out after 600 seconds, so causal separability remains unverified and round admission is not claimed. Freshness remains paused under the round-11 L0 ruling; no calibrated numeric scores (stagnation nudge not invoked). Exploratory claims: 0.

### Round-64 corrections (appended 2026-10-24 in round 65, claim Ca)

| item | correction |
|---|---|
| Correction (round 65, R1) | The round-64 Ca row's `95c9194e` attribution is superseded: `final-measures-ca.txt` is re-stamped to measured revision `8bab271c691c6b1006da95316a24ae1958ec01e2`, with tree `0ec0e50ea828ca6d8e20298f72af49414692e9e4`. The original seven-leg output remains preserved verbatim in the receipt. |
| Correction (round 65, R3) | The round-64 SCORECARD Ca row's `w2/ReviewerCa.md` citation is wrong; actual path: `.ufo/waves/round-64/w1/ReviewerCa.md`. The filed report's `w2/ReviewerCa.md` citation is the erratum target, corrected by the round-65 report erratum. |

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

### Round-65 correction (receipt parent)

| item | correction |
|---|---|
| ACCEPT-CA-65 post-record verdict | The preceding text anticipated a receipt PASS, but the actual run at records tip `3e85a610` printed `RECEIPTS FAIL lands=53a60275`: the receipts name `3b1b5a67`, while the immediate parent is `53a60275` after the prepared-wave commit. Ca's R1-R7/CRITERION/QUOTES legs pass, but the claim is **not verified as declared**. Exact output: `reports/round-65/telemetry/accept-ca-post-records-fail.txt`. |

## Axes — round 66 (2026-10-24, hyaku run 5, L1 KotodamaR66)

Baseline `94209e8f`; lands `65fe8572`; records `4589ebdd` (direct child of lands). One v2 wave of 64 seats in a single task call; 63 seats returned reports named in `reports/round-66/telemetry/seat-evidence.txt`; ScoutRow01 died on a provider error and rows S777/S778 were never produced, so the claim statement was shrunk pre-data to S779-S800 (22 rows) and the gap is named in `corpus/lessons/round-66.md`. Axis verdicts below are the non-author spot-check's (`corpus/lessons/round-66-verifier-spotcheck.md` §6: coverage improved, operability improved, calibration unprovable, depth/freshness/adjacency unchanged), re-read against the committed receipts.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, sourced; ACCEPT-C-66 PASS 12/12 declared legs at lands; non-author spot-check re-opened the S779 and S795 admits and the S795-draft reject — all agreed) | Scent/perfume/aromatics/incense register unowned at base (0 word-bounded filename owners) → `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` (52 lines, 1 H1 / 6 H2, topic line verbatim in the README row) + 22 new mined rows S779-S800 (tier A/B, opened 2026-10-24, used-by the entry, cited exactly once) + the S776 supersession repair; registry 701 → 724 rows (+23 net, re-derived by `^\| S[0-9]{3} ` row count at `94209e8f` and `65fe8572`), corpus 239 → 240 entries, culture-material 32 → 33; 22-row SET complete and unique, 21 hosts, link and capture legs clean | `python3 -B reports/round-66/accept-c.py` inside a materialized clone at `65fe8572` | `reports/round-66/telemetry/final-measures-c.txt`; `corpus/lessons/round-66-verifier-spotcheck.md` §3 re-open table |
| operability | improved (claim O, counter hardening: R65-D4 bound) | Round-65's routed defect (separability checker timed out at 600s) → `tools/check-claim-separability.py` gains `--jobs`/`--budget`/`--max-runs`/`--static-only` + honest-partial (exit 2, `SEPARABILITY_PARTIAL`, `SEPARABILITY_UNRESOLVED`); ACCEPT-O-66 PASS 9/9 declared legs at lands (receipt prints 10 lines incl. the REVISION pre-leg): selftest 63/63, diff 428 lines, option surface present, bounded/static/max-runs exit 2 without asserting `<base>`, `--jobs 1` == `--jobs 4` findings, 4/4 mutants killed, fixture wall 6.2s. The round-66 manifest runs to a complete verdict: `SEPARABILITY: 8 findings`, units=4, ordered_pairs=12, acceptance_runs=9, skipped=0, exit 1 | `python3 -B reports/round-66/accept-o.py` inside a materialized clone at `65fe8572` | `reports/round-66/telemetry/final-measures-o.txt`; `reports/round-66/telemetry/separability-real.txt` |
| calibration | unprovable (claim Ca, records — the frozen counter's committed verdict is FAIL) | Round-65 routed defects D1-D4 → dispositions are real on their own bytes: D1 PASS (S753 live 200 pdf + fresh capture 20261024111013, games entry cites S776 ×1 / S753 ×0), D3 PASS (63 named seat reports present, dead=1, min 8), D4 PASS (complete separability verdict, runs=9 skipped=0), CRITERION PASS (QUALITY criterion 18 grounds anchor resolvability), QUOTES PASS (0 findings, 25 gate ids). But **D2 FAIL** — `no_carrier` for all three `final-measures-*.txt`: the receipts were stamped at lands `65fe8572` and run before the records commit existed, so `git log -1 main -- <receipt>` found no carrier and the committed bytes end `ACCEPT-CA-66: FAIL`. That is the R66-D3 receipt-sequencing artifact; the re-derivation holds post-records (carrier `4589ebdd`, parent `65fe8572`, tree `f0681e6e`) but the frozen verdict stands | `python3 -B reports/round-66/accept-ca.py` inside a materialized clone at `65fe8572` (reproduces the committed FAIL) | `reports/round-66/telemetry/final-measures-ca.txt`; `corpus/lessons/round-66-verifier-spotcheck.md` §2 re-derivation |
| depth / freshness / adjacency | unchanged | Freshness pause in force (round-11 L0); no new derivations. The wave's adjacency artifact keeps the lore handoff one-way through the existing `kotodama-lore-adjacency` 1.0.0 contract (no cross-lane mirror), and the entry's register stays in-lane; the false-owner trap (49 literal hits) is recorded and refused. Depth unchanged: the entry assembles already-mined sources, no new synthesis. The spot-check's §6 verdicts are depth unchanged, freshness unchanged, adjacency unchanged. | — | `w1/ConnectorSiblings.md`; `w1/RevLoreHandoff.md`; `corpus/lessons/round-66-verifier-spotcheck.md` §6 |

Admission: **not admitted** — the non-author spot-check returned `lanes.kotodama = ok; admitted = false; verdict = rejected-honest-stop` (`corpus/lessons/round-66-verifier-spotcheck.md` §6). Coverage and operability verify by their own counters at lands; calibration is unprovable as declared because the frozen Ca receipt's committed verdict is FAIL (D2 `no_carrier`), even though the repeated predicate holds at tip. No observed axis harm: sweep exit 0 and the NOHARM diff is exactly the two declared culture-material files; the census E12/E11 defects and the missing LOG/SCORECARD rows are conformance gaps routed as R66-D2/D4, not falsified knowledge. Freshness remains paused under the round-11 L0 ruling; no calibrated numeric scores (stagnation nudge not invoked).

### Round-66 receipt correction (appended in round 67)

| item | correction |
|---|---|
| ACCEPT-CA-66 verdict | the fleet report `.ufo/reports/round-66/kotodama.md` (fleet root) states "Verdict: ACCEPT-CA-66 PASS (`final-measures-ca.txt`, stamped revision = lands rev per criterion 17)" and "D2 PASS (receipts parented on the lands commit)". The committed receipt at `reports/round-66/telemetry/final-measures-ca.txt` prints `D2 FAIL bad=['reports/round-66/telemetry/final-measures-c.txt:no_carrier', '…-o.txt:no_carrier', '…-ca.txt:no_carrier']` and `ACCEPT-CA-66: FAIL`. The receipt is the record of record; the report line is superseded. |
| Registry arithmetic | The round-66 wave item's coverage summary "+22 rows 701→724" does not add up (701+22=723). Re-derived counts are 701 rows at base `94209e8f` and 724 at lands `65fe8572`/records `4589ebdd` — a +23 net: the 22 new mined rows S779-S800 plus the S776 supersession repair row. |

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Axes — round 67 (2026-10-24, hyaku run 5, L1 KotodamaR67)

Lands `c58eb84b` (claim C) / A_ca (claim Ca); records B; base `ad5b52b0`. Instruments frozen pre-data at `b78f8b8e`/`c5f09921` (accept-ca rev1 sha `5382ffed`); receipts run inside a materialized clone at the lands revision (QUALITY 19 protocol).

| axis | move | verdict | evidence |
|------|------|---------|----------|
| coverage | improved | PASS — medicine/healing register 0 -> owned: `medicine-healing-codes.md` + 24 rows S805-S828, HOSTS=13 | `reports/round-67/telemetry/final-measures-c.txt` (14 legs all PASS at lands) |
| operability | improved | PASS — new capability `tools/check-receipt-seq.py` (lands evaluation, topo, 14/14 selftest) | `reports/round-67/telemetry/final-measures-o.txt` (9 legs all PASS) |
| calibration | improved | PASS — all five R66-D dispositions landed; sequencing protocol enforced by frozen SEQ/QUOTES legs | `reports/round-67/telemetry/final-measures-ca.txt` |
| depth | unchanged | — | — |
| freshness | unchanged | — | — |
| adjacency | unchanged | — | — |

## Axes — round 68 (2026-10-24, hyaku run 6, L1 kotodama-r68 attempt 3 — resumed round)

Round 68 claims: coverage (C) · operability (O) · calibration (Ca). Verdicts below are author-side; the non-author hyaku closure rules admission.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, sourced) | hair/grooming register 0 word-bounded filename owners at base `99fae308` → `corpus/knowledge/culture-material/hair-grooming-codes.md` (57 lines, 24 cited bullets) + 24 mined rows S833-S856; corpus 241 → 242, culture-material 34 → 35, registry 756 → 780 at A_c; ACCEPT-C-68 PASS 12/12 legs in a materialized clone at `44c9cc28` | `python3 -B reports/round-68/accept-c.py --root <clone@A_c> --lands 44c9cc2863fed952bb3a2b04149c2ac279338c3b` | `reports/round-68/telemetry/final-measures-c.txt`; `corpus/lessons/round-68.md` Gate |
| operability | not verified as declared (claim O — FAILED on the frozen EXEC fixture; surface moved) | 34 pending supersedes chains at base → 0 at A_c; `tools/check-supersession-settlement.py` (selftest 7/7) + 82-row dedup ledger (0 findings) land; ACCEPT-O-68 9/10 legs PASS at A_c but EXEC FAIL is structurally unreachable — the frozen fixture never creates `corpus/knowledge/a.md`, so `missing_paths=1` at fixture lands in every recorded run (T0 dry-run, attempt-2 probe, A_c). Counter frozen post-data, not edited | `python3 -B reports/round-68/accept-o.py --root <clone@A_c> --lands 44c9cc2863fed952bb3a2b04149c2ac279338c3b --declaration cb2f8cafa76e84fa698fe5366f353968ba902047` | `reports/round-68/telemetry/final-measures-o.txt`; R68-M1 |
| calibration | improved (claim Ca, records) | R67-D1: 26 frozen scratch paths (incl. 172 MiB fabric-c) deleted with telemetry; R67-D2: ledger ruling for every flagged/chain id, census W04 URL multiset stable at base 28, first-class rejects S857/S858 (both 403-verified); receipt-sequencing protocol re-proven (SEQ/FIXTURES legs; receipts stamped==evaluated in materialized clones) | `python3 -B reports/round-68/accept-ca.py --root <clone@A_ca> --lands <A_ca>` | `reports/round-68/telemetry/final-measures-ca.txt` (records-2); `sweep-d1.txt`; `census-end.txt` |
| depth / freshness / adjacency | unchanged | no new derivations; freshness pause (round-11 L0) in force; adjacency: re-points stay inside the 7 frozen EDITABLE_ENTRIES + the new entry; connector duty folded into L1 verification (no sibling owns the hair register: word-bounded sweep at base; r66 connector prior art stands) | — | DIFFSET leg; lesson quarantine section |

Round shape: one v2 wave 64 seats (dispatched attempt 1, single task call, policy v2, 37/64 attack roles: 23 reviewer + 11 critic + 3 mutation-tester; 15 scout + 6 scribe + 3 executor + 1 connector + 1 sentinel + 1 revenger; the L1 holds the canonical planner seat); ~50 seats dead to the provider rate wall, none replaced, wave not re-dispatched; residual verification as L1 work (no batched dispatch surface on the Kimi seat). Round total: 64 dispatched + L1 integration.

## Axes — round 69 (2026-10-24, hyaku run 6, L1 kotodama-r69 attempt 1 — repair-first after round 68 was rejected)

Round 69 claims: O2 (operability, capability acquisition) · Ca2 (calibration, records) · D2 (depth, the lane's lowest owned axis). Verdicts below are author-side; the non-author hyaku closure rules admission. The round-68 counters are not amended: both new counters carry a `R68FROZEN` leg re-deriving the three round-68 counters' sha256 against their own receipts.

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| operability | improved (claim O2, capability acquisition) | no lane-shaped settlement fixture harness at base `793f7974` → `tools/check-settlement-fixture.py` (three cases: green / negative / pending; the negative case is the missing-used-by class round 68 never exercised); ACCEPT-O-69 PASS 7/7 at the measured revision (STAMP, TOOL, FIXTURE, NEGCASE, LANE, NEGPROBE, R68FROZEN); the lane's own registry still settles pending=0 missing_paths=0 | `python3 -B reports/round-69/accept-o.py --root .` | `reports/round-69/telemetry/final-measures-o.txt`; `reports/round-69/telemetry/controls-rev1.txt` (GREEN 7/7, DO-NOTHING 5/7 FAIL as required, SPOOF 6/7 FAIL as required) |
| calibration | improved (claim Ca2, records) | 5 unannotated mismatches between the filed self-assessment and the committed round-68 receipts over the 5 declared (class, surface) pairs → 0 unannotated (4 live mismatches remain: the frozen round-68 filed texts, each closed by an appended correction row); ACCEPT-CA-69 PASS 8/8; R68FROZEN proves the crashed round-68 counter is byte-identical to its receipt's sha256 | `python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin` | `reports/round-69/telemetry/final-measures-ca.txt`; `reports/round-69/corrections-r68.md`; `corpus/lessons/round-69.md` `## Corrections` |
| depth | improved (claim D2, sourced) | SKILL.md had no registry-correction-chain decision table at base (depth last moved at round 62) → `### Registry correction chains` with the five chain states (pending / settled-active / settled-retired / settled-closed / settled-split), each row carrying row shape, writer's next action, a named error signature and an evidence pointer; the five signatures also listed under `## Error patterns`; the table cites the new registry row S859 (own-work, tier A, opened 2026-10-24); ACCEPT-D-69 PASS 8/8 | `python3 -B reports/round-69/accept-d.py --root .` | `reports/round-69/telemetry/final-measures-d.txt`; `corpus/knowledge` — n/a (depth surface is SKILL.md); `corpus/lessons/round-69.md` `## Gate` |
| coverage / freshness / adjacency | unchanged | coverage is not claimed: round 68 already improved it (S833-S856 admitted) and that work is not repeated as a new claim; freshness stays paused under the open round-11 L0 ruling; adjacency: the connector duty found no sibling owner of a registry-correction-chain surface, and the new table stays in-lane (`.ufo/waves/round-69/w1/ScoutAdj.md`) | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (not re-run this round) | `.ufo/waves/round-69/w1/ScoutAdj.md` |

Frontier step (not a claim): `corpus/SOURCES.md` 782 → 783 rows (S859 opened, mined, used-by `SKILL.md` and `corpus/lessons/round-69.md`); census exit 0 at start (`reports/round-69/telemetry/census-start.txt`) and end (`census-end.txt`); lesson `corpus/lessons/round-69.md` carries `## Gate` (S859), `## Mistakes` (R69-M1..R69-M6 plus the backfilled R68-M9), `## Corrections` and `## Quarantine`.

Round shape: one v1 wave of 32 seats (policy v1, band 32-64; 26/32 attack roles = 81.3%), one dispatch call, 1201 s wall, parent alive until settlement; 21 reports returned, 11 dead seats (9 × `provider.rate_limit: 429`, 2 × 1200 s timeout), none replaced (`.ufo/waves/round-69/w1/settle.tsv`).

### Round-69 corrections to the filed round-68 self-assessment (append-only; the filed round-68 bytes are not rewritten)

| corrected row | correction | re-derivation command |
|---|---|---|
| round-68 operability row and round-68 LOG entry and the filed fleet report: `ACCEPT-O-68 9/10 legs PASS` | the committed round-68 receipt prints **9 legs: 8 PASS and 1 FAIL (EXEC)** — not 9 of 10 | `grep -cE '^[A-Z0-9_]+ (PASS\|FAIL) ' reports/round-68/telemetry/final-measures-o.txt` → 9; the same grep with `PASS` → 8 |
| round-68 report pointer `## Mistakes R68-M1..M8 (+M9 in LOG)` and `Ca fails as declared (R68-M9)` | no R68-M9 row existed; the crash itself is real (`NameError: name 'git_bytes' is not defined`, `accept-ca.py:224`). The row is backfilled in `corpus/lessons/round-69.md` `## Mistakes` and named in the `LOG.md` round-69 entry, so the filed pointer now resolves. The crashed counter is NOT amended | `grep -c 'R68-M9' LOG.md corpus/lessons/round-68.md corpus/lessons/round-69.md` → 3 (0 before this round) |
| round-68 calibration row: `\| calibration \| improved (claim Ca, records) \|` | the committed round-68 calibration receipt carries a `NameError` traceback and never prints `ACCEPT-CA-68: PASS` — the claim did not verify as declared | `grep -c 'ACCEPT-CA-68: PASS' reports/round-68/telemetry/final-measures-ca.txt` → 0 |

Stale-lane: respawn-per-round driver; no other mission of this lane is open at round-69 close.

### Round-69 attempt-2 residual verification (2026-10-25) — verdicts, routed defects, corrections

Attempt 1's records above stand as filed; this block appends what seven residual seats found
attacking the landed measures at `9e82c7b` (all seven returned, none died; evidence
`.ufo/waves/round-69/w2-verify/*.md`). Nothing above is rewritten; the one in-place exception —
the ScoutAdj pointer repair in the round-69 coverage/freshness/adjacency row, disclosed in the
round-69 corrections table (POINTER class) — is recorded there, and the record corrections this
attempt appends live in `corpus/lessons/round-69.md` `## Corrections (round 69 attempt 2)` and its
`## Quarantine` addendum.

| claim | frozen predicate re-run (fresh clone) | residual finding | attempt-2 verdict |
|---|---|---|---|
| O2 | `ACCEPT-O-69: PASS legs=7/7`, body byte-identical to the receipt | NEGPROBE adjudicates a constant (a one-token spoof still passes), 4 of 9 mutations survive, both STAMP legs compare a file to itself under `--root .` (R69-M8..M10) | **verified on its frozen predicate**; capability partial, defects routed to round 70 |
| Ca2 | `ACCEPT-CA-69: PASS legs=8/8`, `live=4 unannotated=0` | the frozen `kill_rule` fires on the 4 live pairs, and the declared after-state requires rewriting frozen round-68 bytes (R69-M7); five stub correction rows also pass | **FAILED AS DECLARED** — calibration stays unprovable; no axis harmed |
| D2 | `ACCEPT-D-69: PASS legs=8/8` before and after the repair | five table statements contradicted the code, EVIDENCE checks path existence only, the do-nothing selftest became non-reproducible post-data (R69-M11, R69-M12) | **verified on its frozen predicate after a content repair**; `reports/round-69/telemetry/final-measures-d-attempt2.txt` |

Round admission: the claim cap admits a round only when every claim verifies, and Ca2 does not.
Author-side verdict: **not admitted as declared**; the non-author closure/operator rules. Round
shape: inherited attempt-1 v1 wave (32 seats, 26 attack roles) plus one residual `task` call of 7
seats (reviewer 2, critic 3, mutation-tester 1, scout 1) = 39 seats, ≤128, no dead seats. Item-10
adoption stays CLOSED; the id-collision guard is proved for the first time at
`.ufo/waves/round-69/assimilation/guard-proof/`. The lesson now carries R68-M9 plus
R69-M1..R69-M15; the frontier-step line above names only R69-M1..R69-M6, which is the attempt-1
count.

## Corrections — round 70 (2026-10-25, hyaku run 6, L1 kotodama-r70)

Appended per the append-only correction convention; the superseded texts above stand as filed.
Full per-defect dispositions: `reports/round-70/corrections-r69.md`.

| item | correction |
|---|---|
| D2 attributions | Landed-changes first-commit hashes: `tools/check-settlement-fixture.py` = `6a98d7d`; `reports/round-69/corrections-r68.md` = `e86ed3e`; the round-70 fleet report uses them |
| D3 claims.json wording | the round-69 claims.json frozen fields are unchanged at `6a98d7d`, `52b92a6`, `ef75509`; wave metadata and `counter_revisions` were appended at `52b92a6` — the round-70 report says exactly that |
| D4 round-69 calibration | marking round-69 calibration unprovable: the Ca2 claim failed as declared (`FAILED AS DECLARED` at :1360; `claims.json` Ca2 `kill_rule` fires on the 4 live pairs, R69-M7); the `improved` row at :1331 is superseded by this row |
| D9 dead pointer | `.ufo/waves/round-69/assimilation/guard-proof/note.txt` line 4 cited R69-M10; the S859 lane-package collision is mistake R69-M13; pointer fixed in place |
| D10 O2 receipt | O2's current measurement is `reports/round-69/telemetry/final-measures-o-attempt2.txt` (stamped `975e8f2`); `final-measures-o.txt` remains the attempt-1 receipt |

### Round-70 trend-correction row (appended 2026-10-25 in round 71, V70-4)

The filed round-70 fleet report (`.ufo/reports/round-70/kotodama.md`) graded
`expansion: improved` and `discernment: improved`. Per LEARNING.md observables
these do not fire: no admitted knowledge entry on uncovered ground (expansion,
CORPUS.md rule 4) and no gate decision/new lesson-grounded QUALITY criterion
(discernment). This row marks the round-70 trend-correction. Correct verdicts for round 70: expansion `unchanged`, quality
`unchanged`, discernment `unchanged` (wave-1 seat CritTrendObservables). The
filed report bytes are untouched; this row is the correction record.

## Axes — round 72 (2026-10-25, hyaku run 6, L1 kotodama-r72; repair-first + first shokuknow adoption), admitted author-side

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| calibration | improved (claim Ca, records) | 8 routed defects K71-1..K71-8 un-landed at base `b60c7b1` (QUALITY 20 worktree-only; 7 w2 files uncommitted; in-place id-map edit without old→new record; fleet report :57/:61 stale; tally 10/6/5 vs 10/7/4; wave-2 41 vs 40; counter-sha mis-pairing; falsified Capoeira reject reason; no criterion 21) → all eight landed append-only with old→new records; ACCEPT-CA-72 PASS legs=12/12 at the measured revision | `python3 -B reports/round-72/accept-ca.py --root . --lands <lands>` | `reports/round-72/telemetry/measures-ca.txt`; `corpus/lessons/round-71.md` `## Corrections (round 72)`; `reports/round-71/telemetry/measures-ca-restamp-64da9e14.txt` |
| coverage | improved (claim C, assimilation-sourced) | 0 heritage-taxonomy files and 0 ihchina/bunka registry rows at base (797-row registry, gap sweep re-run 2026-10-25) → 2 admitted entries (`heritage-taxonomy-models.md` + `.amend-2026-10-24-r13.md`) citing mined rows S874/S875 re-pointed by document from staged S863/S867/S967; registry 797 → 799; ACCEPT-C-72 PASS legs=10/10 | `python3 -B reports/round-72/accept-c.py --root . --lands <lands>` | `reports/round-72/telemetry/measures-c.txt`; `corpus/lessons/round-72.md` `## Gate`; `.ufo/waves/round-72/assimilation/validate-receipt.txt` |
| depth / quality / operability / freshness / adjacency | unchanged | no existing entry re-verified or deepened (C is net-new ground, not depth); QUALITY 20 was authored round 71 (its commit in round 72 is calibration, never quality — criterion 20); no new runnable tool (counters are receipts, not lane capabilities); freshness stays paused under the open round-11 L0 ruling; adjacency: connector scan found the heritage-taxonomy surface in-lane and uncontested (lore assigns culture-material design models to kotodama by path) | census + counters above (not re-scored) | `.ufo/waves/round-72/w1/ConnectorSiblings.md` |

Frontier step (not a claim): `corpus/SOURCES.md` 797 → 799 rows (S874, S875 opened and mined this round); census exit 0 at start (`reports/round-72/telemetry/census-start.txt`) and end (`census-end.txt`); lesson `corpus/lessons/round-72.md` carries `## Gate` (2 admits + 2 refuses with reason+flip), `## Mistakes` (in-place-edit class), `## Quarantine` (F-1/F-2) and `## Corrections` (pre-data freeze corrections). Claim C is the sourced claim: rows S874/S875.

Round shape: one v1 wave of 32 seats (policy v1, band 32-64; 16/32 attack roles = 50%), one batched dispatch, no wave 2 (operator wrap-up — no new waves; residual attack items are recorded in the report instead of a second wave). Item-10 adoption: two heritage-taxonomy entries admitted (first adoption round); staged REFUSED set not adopted; `considerthese/` absent.

## Corrections — round 73

Append-only record (hyaku run 7, L1 KotodamaR73). Claim Ca ledger `reports/round-73/ledger.json` (frozen with `reports/round-73/claims.json` at af65165). Counter: `python3 -B reports/round-73/accept-ca.py --root . --lands <lands> --fleet-root /home/vgpnk/Projects/shokunin`. The filed lines named below stand as filed; each ANNOTATE row carries id, old token, new token and the re-derivation command.

| id | old token (as filed) | new token (observed) | re-derivation command | note |
|---|---|---|---|---|
| L01 | 243 | 245 | git ls-tree -r --name-only 8841ad3b896a0227674fa0725b818c999118046f corpus/knowledge (count the .md paths) -> 245 | `corpus/README.md:732` `Total knowledge entries: 243.` — 243 was written at 498db73 and not reconciled after round 72 added two culture-material files; measured at the pinned base revision so landing claim C (+2 files, README footer line `Total knowledge entries: 247.` carried by claim C) cannot move it. The filed README line stays as filed; this row and the later appended footer line supersede it. |
| L02 | 36 | 38 | git ls-tree -r --name-only 8841ad3b896a0227674fa0725b818c999118046f corpus/knowledge/culture-material (count the .md paths) -> 38 | `corpus/README.md:407` heading `## culture-material/ (36)` — the directory held 38 `.md` files at the pinned base (the two round-72 heritage-taxonomy entries were never counted). Heading not rewritten (append-only discipline); this row is the correction record. |
| L03 | 243 | 245 | git ls-tree -r --name-only 8841ad3b896a0227674fa0725b818c999118046f corpus/knowledge (count the .md paths) -> 245; python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge | `corpus/README.md:736` counts-checked line `(total 243 files; directory totals 30/29/36/29/24/95)` — same 243 → 245 drift as L01 and 36 → 38 as L02, at the same pinned base. |
| L06 | PASS | FAIL | grep -ho 'ACCEPT-CA-72: [A-Z]*' reports/round-72/telemetry/measures-ca.txt | `SCORECARD.md:1401` says `ACCEPT-CA-72 PASS legs=12/12 at the measured revision`; the committed round-72 receipt `reports/round-72/telemetry/measures-ca.txt` reads `ACCEPT-CA-72: FAIL legs=12/12` (REPORTCORR/REPORTLAST — the fleet report had not yet landed at the stamp). The filed row was therefore wrong as filed. Round 73 appends `reports/round-73/telemetry/measures-ca72-rerun.txt`: the same counter (sha256 `f080c240…`) re-run in a materialized clone at its own stamped revision `21ad3088` prints `ACCEPT-CA-72: PASS legs=12/12`, so the verdict is true at that revision only after the report landed — it never repairs the filed row, which stays annotated. |
| L07 | F1-F9 | F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE | python3 -c "import json;print(', '.join(c['id'] for c in json.load(open('reports/round-72/claims.json'))['pre_data_corrections']))" | `LOG.md:4280` says `pre-data corrections F1-F9 + SCOUT-LIVE documented there`; `reports/round-72/claims.json` `pre_data_corrections` holds eight ids (F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE) — there is no F7 entry. Filed text not rewritten; the range token overstated the set by one slot. |

REPAIR pairs (statement now equals the truth, observed by the counter at `<lands>`): L04 `SHONEN.md:6` `:468` → `:505` (Error patterns) and L05 `:522` → `:564` (Checklist), repaired in place in SHONEN.md (not an append-only file) with the old values named in the line itself; L08 `SKILL.md` §Gates and probes — registry last row `accept-o-69` → `accept-ca-73` after seven rows were inserted (accept-c-71, accept-ca-71, accept-d-71, accept-c-72, accept-ca-72, accept-c-73, accept-ca-73). The round-70 pair has no counter bytes in git (only receipts at 453676a2): it is explained here, not registered. Defect R1: `.ufo/waves/round-72/w1/ScoutMergeScan.md` and `ScribeLesson.md` are tracked from the Ca landing commit on (TRACKED leg).

Measured side finding (not a ledger pair): `python3 -B reports/round-72/accept-c.py --selftest` prints `SELFTEST: 10/11` and exits 1 at the round-73 base (`--- clean fixture: expected PASS 10/10, got exit=1`); the round-72 report and SCORECARD cite the counter's `--selftest` mode without a receipt of it. Recorded in `corpus/lessons/round-73.md` `## Mistakes`; the round-72 counter is not amended.


## Axes — round 73 (2026-10-25, hyaku run 7, L1 KotodamaR73), author-side verdicts, pending non-author closure

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, assimilation-sourced) | 0 `*conlang-scholarship*` files and 0 rows naming the five source hosts at base `8841ad3` (799-row registry) → 2 admitted files citing mined rows S876-S880 (804 rows); ACCEPT-C-73 PASS legs=11/11 | `python3 -B reports/round-73/accept-c.py --root . --lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0` | `reports/round-73/telemetry/controls-c.txt`, `selftest-r3.txt`; `corpus/lessons/round-73.md` `## Gate` |
| calibration | improved (claim Ca, records) | 8 of 8 ledger pairs red at base, 2 seat reports untracked → 3 REPAIR pairs green, 5 ANNOTATE pairs annotated, both files tracked; ACCEPT-CA-73 PASS legs=9/9 (counter r3) | `python3 -B reports/round-73/accept-ca.py --root . --lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0 --fleet-root /home/vgpnk/Projects/shokunin` | `reports/round-73/ledger.json`, `counter-revisions.md`, `telemetry/controls-ca*.txt` |
| depth / operability / freshness / adjacency | unchanged | no existing entry deepened; freshness paused under the open round-11 L0 ruling | — | `corpus/lessons/round-73.md` |

Wave-2 found content defects in the admitted entries (all repaired, old→new in the lesson Corrections) and counter survivors (not repaired; frozen predicates stand). Round shape: wave 1 = 37 seats, wave 2 = 33 seats, total 70 (policy v1, band 32-64 each). Stale-lane: none.

## Corrections — round 74

Append-only record (hyaku run 7, L1 KotodamaR74). Claim Ca ledger `reports/round-74/ledger.json` (frozen with `reports/round-74/claims.json`). Counter: `python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin`. The filed lines named below stand as filed; each row carries id, old token, new token and the re-derivation command, which the counter re-runs.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| LC-01 | 412 | 804 | git grep -c -E '^. S[0-9]{3}' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
| LC-02 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbce186bc2e1522abf0cfd619cc834628bb -- reports/round-73/telemetry/selftest-r3.txt |
| LC-03 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbce186bc2e1522abf0cfd619cc834628bb -- reports/round-73/telemetry/selftest-r3.txt |
| LC-06 | 243 | 247 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/*/*.md' |
| LC-07 | 243 | 247 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/*/*.md' |
| LC-08 | 30 | 32 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f7104cbce186bc2e1522abf0cfd619cc834628bb -- 'corpus/knowledge/linguistics/*.md' |
| LC-11 | 23443 | 97656 | git grep -h -o -E 'decompress.*23443.*[0-9]+ bytes' f7104cbce186bc2e1522abf0cfd619cc834628bb -- .ufo/waves/round-73/w2/ScoutReopenS879.md |
| LC-12 | no | two | git grep -h -o -E 'HAS two status-200 Wayback captures' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/lessons/round-73.md |
| LC-15 | 776 | 724 | git grep -c -E '^. S[0-9]{3}' 65fe8572822ef83f1750593af77daddf34a1e337 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
| LC-16 | reachable | present | git grep -h -o -E 'wall (present) \("Client Challenge"\)' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/lessons/round-73.md |
| LC-17 | 752 | 728 | git grep -c -E '^. S[0-9]{3}' c5f099211e1d6c095e7c59edbd05c0043b4b95fc f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |
| LC-18 | 753 | 701 | git grep -c -E '^. S[0-9]{3}' 94209e8f80969dbac48d56c5d0e2e623635b8616 f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/SOURCES.md |

## Axes — round 74 (2026-10-25, hyaku run 7, L1 KotodamaR74), author-side verdicts, pending non-author closure

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, assimilation-sourced; author-side) | 0 `*worldbuilding-setting*` files, 247 knowledge files and 804 registry rows with 0 rows naming litmemo/tuduku/chinawriter at base `f7104cb` → 2 admitted entries whose `source:` lines cite S877 and S881-S884, 249 knowledge files and 808 registry rows at lands `c4bf61a`; ACCEPT-C-74 PASS legs=13/13 | `python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin` | `reports/round-74/telemetry/measures-c.txt`, `junk-c.txt`, `selftest-c.txt`, `census-start.txt`, `census-end.txt`; `corpus/lessons/round-74.md` `## Gate` |
| calibration | improved (claim Ca, records; author-side) | 13 of 13 ledger pairs red at base, six round-73 w2 files unlanded and no `ACCEPT-C-73: PASS` / `ACCEPT-CA-73: PASS` line in the base telemetry → 1 REPAIR pair green (`LC-09` `94`→`95`), 12 ANNOTATE rows, six files tracked at identical blob ids, both round-73 counters re-executed at `2d1cd914` (`ACCEPT-C-73: PASS legs=11/11`, `ACCEPT-CA-73: PASS legs=9/9`); ACCEPT-CA-74 PASS legs=11/11 | `python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin` | `reports/round-74/ledger.json`, `telemetry/measures-ca.txt`, `accept-c-73-at-lands.txt`, `accept-ca-73-at-lands.txt`, `junk-ca.txt`, `selftest-ca.txt` |
| depth / operability / freshness / adjacency | unchanged | no existing entry deepened; freshness paused under the open round-11 L0 row (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47`), no waiver claimed | — | `corpus/lessons/round-74.md`; `reports/round-74/claims.json` `axes_note` |

Round shape: wave 1 = 42 seats (12 scout / 10 executor / 6 scribe / 6 critic / 3 reviewer / 2 connector / 1 mutation-tester / 1 sentinel / 1 simplifier), wave 2 = 44 seats (critic 9 / reviewer 8 / executor 8 / scout 6 / mutation-tester 6 / connector 2 / scribe 2 / simplifier 1 / revenger 1 / sentinel 1), total 86 (policy v1, band 32-64 each). Wave-1 dead seats: none (42/42 report files present at `.ufo/waves/round-74/w1/`). Stale-lane: none.

Wave-2 outcome folded in (author-side): claim C holds at `c4bf61a` (PASS legs=13/13) and claim Ca at its own landing `5e4796c` (PASS legs=11/11); Ca is NOT green at a tree carrying both landings (APPENDONLY: claim C's in-place `used-by` change on the reused row is outside Ca's REPAIR lines — frozen-claims conflict, not amended). Admission is reported, not asserted: the operator and the non-author closure rule on whether Ca measured at its own landing satisfies the claim. Calibration is `improved` only for the declared ledger pairs; the wave-2 record sweep found further mismatches in the round's own new bytes (two HIGH repaired: SKILL pin, QUALITY 25; the rest routed). Trend verdicts: expansion improved (one ground; base + amendment), quality unchanged (own-entry repairs are calibration work, QUALITY 20), discernment unchanged (no outside spot-check of this round yet). Exploratory claims: 0.


## Corrections — round 75

Append-only record (hyaku run 10, L1 kotodama round 75). Claim Ca ledger `reports/round-75/ledger.json`, frozen
with `reports/round-75/claims.json`. Counter: `python3 -B reports/round-75/accept-ca.py --root . --lands <lands>
--freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin`. The filed lines named below stand as filed; each
row carries the pair id, the base stated token, the observed token and the pair's own re-derivation command,
which the counter re-runs with the pair's parser and requires to return the observed token.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| L75-04 | 249 | 247 | git grep -c -E '^- `[^`]+\.md` —' f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/README.md |
| L75-08 | absent | present | git grep -c '非凡特性来自最初造物主' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S883.txt |
| L75-09 | absent | present | git grep -c '这个我肯定考虑过' f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-74/evidence/S884.txt |
| L75-10 | 43 | 44 | git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- ':(glob).ufo/waves/round-74/w2/*.md' |

Notes. Each cell holds the ledger's own token, not a paraphrase: the old token is the pair's `stated_parse`
capture at the pinned base, the new token is what the pair's `observe_cmd` returns there.

- `corpus/README.md:813` (pair L75-04) states `Total knowledge entries: 249.` while the index rows above it
  number 247 at the pinned base; the filed footer line stands and claim C carries its own later footer.
- `corpus/lessons/round-74.md:37` and `:38` (pairs L75-08 and L75-09) say each staged row's quoted span was
  absent from the page it was bound to, while each own span occurs once in that page's round-74 capture and the
  mispairing belongs to the register rows the lesson names.
- `LOG.md:4318` (pair L75-10) says `43 of 44 report files present at filing`; the frozen base carries 44 report
  files in that wave-2 directory, the three `drafts/*.md` files being outside it.
- The remaining six ledger pairs are REPAIR pairs and carry no row here: their statements move to the observed
  truth in the files they name.

The row commands are the ledger's `rederive` strings verbatim. Four ledger observations (pairs L75-04, L75-05,
L75-06 and L75-07) embed a backtick or a pipe inside an `-E` pattern, which the counter's observe guard refuses;
the freeze must carry the guard-clean re-cut named in `.ufo/waves/round-75/w2/ScribeScorecardFinal.md`, and if
it does, cell four of the matching row takes the re-cut string. The token cells do not change.

## Axes — round 75 (2026-10-27, hyaku run 10, kotodama), author-side verdicts, pending non-author closure

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| coverage | improved (claim C, assimilation-sourced) | at base f556d104: 0 knowledge files named `*narrative*`, 808 registry rows, 249 knowledge `.md` files → 3 admitted `corpus/knowledge/myth-symbol/narrative-structure-frameworks*` files (252 `.md` files), 817 registry rows (S885-S893, one row per document); ACCEPT-C-75 PASS legs=13/13 | `python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2535c2c06c51627dc2736c40183847cae1 --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14` | `reports/round-75/telemetry/controls-c.txt`, `junk-c.txt`, `selftest-c.txt`, `census-start.txt`, `census-end.txt`; `corpus/lessons/round-75.md` `## Gate` |
| calibration | improved (claim Ca, records) | at base f556d104: 10 ledger pairs (6 REPAIR, 4 ANNOTATE), every stated token unequal to the observed one — all 10 measured red at the pinned base (the four pairs whose `-E` pattern holds a backtick or an escaped pipe are read as pattern operands, the argv never shell-parsed — claims LEDGER wording, pre-data edit W2-F5) → 6 REPAIR statements equal the truth observed at the Ca lands, 4 rows under `## Corrections — round 75` carrying id + old token + new token + the re-derivation command, zero removed lines in the APPENDONLY set; ACCEPT-CA-75 PASS legs=12/12 | `python3 -B reports/round-75/accept-ca.py --root . --lands 012e8d3c8b92f47c734f735d58d118d574fe6a14 --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 --fleet-root /home/vgpnk/Projects/shokunin --combined 4f5e3b2535c2c06c51627dc2736c40183847cae1` (run in a clone whose local main is pinned to the Ca landing) | `reports/round-75/ledger.json`, `reports/round-75/telemetry/controls-ca.txt`, `junk-ca.txt`, `measures-ca.txt` (its COMBINED leg ran with --combined), `accept-ca-74-at-lands.txt`; `corpus/lessons/round-75.md` |

Round shape: wave 1 = 42 seats (attempt 1), wave 2 = 34 seats (build + attack, pre-freeze), wave 3 = 36 falsify seats; round total 112. Non-author closure pending.
## Corrections — round 76

Append-only record (hyaku run 10, kotodama round 76). Claim Ca ledger `reports/round-76/ledger.json` has 20 unique pairs (19 ANNOTATE, 1 REPAIR), frozen with `reports/round-76/claims.json`. Measured at Ca-lands `a43ed807ea38b5fc5a7875a839d576cea73aba7c`, freeze `df0f0309d61e5485bb17035d3f8791b1e6a11d40`, combined C-lands `722e69ff6361aadf148cb46acbf6ac8fd147f59a`: `python3 -B reports/round-76/accept-ca.py --root . --lands a43ed807ea38b5fc5a7875a839d576cea73aba7c --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin --combined 722e69ff6361aadf148cb46acbf6ac8fd147f59a --main a43ed807ea38b5fc5a7875a839d576cea73aba7c --work /fast/scratch/hyaku/kotodama-r76/final-ca-counter`.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| L76-01 | absent | present | git grep -c -E '^' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/claims.json |
| L76-02 | DRAFT | FINAL | git grep -o -E '"status": "[A-Z]+' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/claims.json |
| L76-03 | fails | blob | git cat-file -t 98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/claims.json |
| L76-04 | fails | blob | git cat-file -t 98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/accept-c.py |
| L76-05 | 6862 | 30920 | git ls-tree -l 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.md |
| L76-06 | excerpt | whole-document | git grep -o -E '^window-scope: [a-z-]+' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S891.txt |
| L76-07 | amend-2026-10-23 | amend-2026-10-23b | git grep -o -E '^\| S891 \|.*' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/SOURCES.md |
| L76-08 | 10 | 3266 | git grep -o -E '^window: chars=[0-9]+ min=[0-9]+ pad=[0-9]+ before=[0-9]+' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S888.txt |
| L76-10 | 4097 | 4096 | git grep -h -E '^window: chars=' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S888.txt |
| L76-11 | 111486 | 109588 | git grep -h -E '^bytes: ' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S885.txt |
| L76-12 | 118776 | 116878 | git grep -h -E '^bytes: ' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S887.txt |
| L76-13 | 111487 | 109588 | git grep -h -E '^bytes: ' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S885.txt |
| L76-14 | .ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md | corpus/SOURCES.md | git grep -l -F -e 'Innombrables sont les récits du monde.' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/SOURCES.md |
| L76-15 | marrone%20age% | marrone%20age%20dor---2.pdf | git grep -h -o -E 'marrone%20age%[^ ]*' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md |
| L76-17 | 5933 | 24166 | git ls-tree -l 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md |
| L76-18 | 2514 | 23049 | git ls-tree -l 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md |
| L76-19 | 284 | 2020 | git grep -h -E '^window: chars=' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S892.txt |
| L76-20 | 2bcdd019 | 20b571d7 | git grep -h -o -E '^sha256: [0-9a-f]{8}' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S885.txt |
| L76-21 | fbf48ad2 | e0560649 | git grep -h -o -E '^sha256: [0-9a-f]{8}' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S887.txt |

The table is a verbatim projection of the 19 ANNOTATE pairs, not an assertion that the frozen Ca counter accepts them. L76-13 names a knowledge path outside the frozen append-only allowlist; L76-19's stated token cannot be found at the claimed lesson line. L76-16 is the single REPAIR: `SKILL.md:707` now distinguishes the receipt's pre-freeze digest `fa5060b91bdb…` from the committed counter digest `315c5f3f27fd…`.

Erratum (W2, `ExecScorecardConsistency.md`): the table preserves the 19 old/new token pairs, but its re-derivation-command cells for L76-19/20/21 are not byte-identical to the frozen ledger and are not executable under the frozen parser. The earlier phrase “verbatim projection” was too broad; `measures-ca.txt` records the ANNOTATE/NOSTUB failures.


## Axes — round 76 (2026-10-27, hyaku run 10, kotodama), author-side verdicts

**Coverage / claim C — failed as declared; no score delta.** Base 98c486b: 252 knowledge files, 817 registry rows. C lands 722e69f: 253 files, 820 rows (S894-S896). The frozen counter reports FAIL legs=11/13; ROWS and COLLCHECK are red. Counting command:

```sh
for rev in 98c486bdb4650ba5b8e651d332910e8ee60ad121 722e69ff6361aadf148cb46acbf6ac8fd147f59a; do
  printf '%s knowledge=' "$rev"
  git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only "$rev" corpus/knowledge | grep -c '\.md$'
  printf '%s rows=' "$rev"
  git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show "$rev:corpus/SOURCES.md" | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
done
```

Observed output: `98c486b… knowledge=252 rows=817`; `722e69f… knowledge=253 rows=820`. Acceptance command: `python3 -B reports/round-76/accept-c.py --root . --lands 722e69ff6361aadf148cb46acbf6ac8fd147f59a --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin --work /fast/scratch/hyaku/kotodama-r76/final-c-counter`. Evidence: `reports/round-76/telemetry/measures-c.txt`, the calendar amendment and its Gate.

**Calibration / claim Ca — failed as declared; no score delta.** The frozen ledger has 20 pairs (19 ANNOTATE / 1 REPAIR); the counter reports FAIL legs=5/12. L76-13 and L76-19 fail LEDGER, with additional REPAIR, ANNOTATE, NOSTUB, R1EXEMPT, SEPARABLE, and COMBINED failures. Acceptance command: `python3 -B reports/round-76/accept-ca.py --root . --lands a43ed807ea38b5fc5a7875a839d576cea73aba7c --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin --combined 722e69ff6361aadf148cb46acbf6ac8fd147f59a --main a43ed807ea38b5fc5a7875a839d576cea73aba7c --work /fast/scratch/hyaku/kotodama-r76/final-ca-counter`. Evidence: `reports/round-76/telemetry/measures-ca.txt`, `reports/round-76/ledger.json`, and the Corrections table above.

Neither frozen acceptance counter passes. The source additions and ledger annotations remain recorded with their failure boundaries explicit; neither axis score is advanced.

W2 evidence follow-up: `reports/round-76/evidence/S894.txt`, `S895.txt`, and `S896.txt` were regenerated with the frozen round-76 capture tool and its anchor-binding self-check; all three printed `VERIFY OK` and `CAPTURE OK` (`reports/round-76/telemetry/capture-evidence-recapture.txt`). C was re-measured at `3c2893bf87f5247e8d2d7af59d1ec1e11895647b`: `ACCEPT-C-76: FAIL legs=11/13`, still only ROWS and COLLCHECK red (`reports/round-76/telemetry/measures-c-final.txt`). No score delta.

Final Gate-reviewed C remeasurement at `cb4f6c6a550b3233f3c12a266e72dee6f4bc126b`: `ACCEPT-C-76: FAIL legs=11/13`; ROWS and COLLCHECK remain the only red legs after the S895 locator correction and non-author spot-check. Receipt: `reports/round-76/telemetry/measures-c-final.txt`. No score delta.

Final counter restamp after the census/lesson integration at `b857eed56674738fe95f49b298f5ec555f1e6f6b`: `ACCEPT-C-76: FAIL legs=11/13`, with ROWS and COLLCHECK still the only red legs (`reports/round-76/telemetry/measures-c-final-c6.txt`). Counts remain 252→253 knowledge files and 817→820 registry rows; no score delta.

Final W2-integrated restamp at `b40113eb3961bce44fba6b066ce6a656f0e16fec`: `ACCEPT-C-76: FAIL legs=11/13`; ROWS and COLLCHECK remain the only red legs (`reports/round-76/telemetry/measures-c-final-c7.txt`). The integration and quarantine/lesson corrections did not change the frozen claim verdict; no score delta.

Final post-WAVE-DONE restamp at `c792ea50f1cfba2b56c16a0f5102b2877fd2eefd`: `ACCEPT-C-76: FAIL legs=11/13`, still ROWS and COLLCHECK only (`reports/round-76/telemetry/measures-c-final-c792.txt`). W2 evidence corrections and count receipts did not alter the frozen result; no score delta.

Final lane-tip measurement at `c28ea2194ae6d0c874c011d3b1b59409a20bd422`: `ACCEPT-C-76: FAIL legs=11/13`, still ROWS and COLLCHECK only (`reports/round-76/telemetry/measures-c-final-c28ea.txt`). The pushed tip adds only evidence/close records after the C7 data; no score delta.

## Round 78 — honest stop (2026-10-27)

No claim survived pre-data scoping; no axis score delta is recorded. Freshness is historically the lowest non-retired axis but its move remains paused by the open round-11 L0 question; the SCORECARD carries no saturation evidence to invoke the stagnation nudge. No source or knowledge entry was opened/added for a claim. The missing 64-seat swarm floor is a conformance defect; no wave was padded without a real claim.
