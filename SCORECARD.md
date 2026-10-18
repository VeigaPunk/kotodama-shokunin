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

## Planned

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
