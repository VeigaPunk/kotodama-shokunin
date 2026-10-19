- Seat: X01 | critic | cross | date 2026-10-19 | baseline da68a6d

# X01 — trade hunter: D/O/C collisions and axis-harm pathways

Method: every finding below is from live bytes at `da68a6d` read in this seat
(`git rev-parse HEAD` = da68a6d705e41f369f21e8607bfaab5b54077f84; the only
untracked path is `reports/round-34/`). No fragment directory had landed when
this seat read them (`ls reports/round-34/{scout,plan,cross,depth,op,calib,review,scribe}`
→ all empty), so the collision analysis is measured, not synthesized from
peers. Two of the three legs named in every claim's `counting_commands`
(`python3 reports/round-34/run-validation.py`) name a file the round contract
says does not exist yet and that no seat may execute in-tree — see T-6.

## 0. Verified before-state (claim premises)

| premise | claim says | measured | citation |
|---|---|---|---|
| renderer default pair pins r6 | claims.json D.before | `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"`, `V3_FROZEN_DIR_DEFAULT = "…/declared-in-r6"` | tools/exercise-handoff-e2e.py:1933-1934 |
| old pair is shape-green | claims.json D (D13 control) | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0: `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` | command run this seat; matches reports/round-30/handoff/declared-in-r6/freeze.txt:2 |
| old pair is semantically stale | claims.json D `stale_numbers` | packet.md:148 (typed_labels 74 / native-form 56 / findings_total 16 / hold-or-fail 15); :149 (hold 15, note 1); :150 and :152 (conflicts 4, quarantine handles 3, 13 unresolved rank items); :307 (OQ-V3-05 same text) | cited lines; live values below |
| live D4 numbers | claims.json D.after | `examples/culture-d4/typed-labels.d4.yml:29-48`: typed_labels 82, labels_by_kind native-form 64 / translated-label 12 / borrowed-strata 6, findings_total 12, findings_hold_or_fail 12, label_findings_fail 0, conflicts 0, rank_rules_unresolved_items 0, rank_quarantine_handles 0, reconciliation_records 6 | file:lines |
| live hold set | claims.json D.after | `examples/culture-d4/expected-holds.json` counts `{"hold":12,"note":0,"fail":0}`; active_pin_generation `round-30-qreg-records`; packet_sha256 aac91246…, projection c23b0ab5…, projector 2819f687… | python3 json read this seat |
| manifest rows already agree with live | claims.json D.self_contradiction | packet.md:68 A-30 reads "82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12 findings, 0 unresolved rank items"; :69 A-31 reads "12 holds / 0 note / 0 fail" | cited lines |
| SKILL digest as claim C states | claims.json C.before | `sha256sum SKILL.md` → f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b, 732 lines | command output |
| box-1 surface | claims.json C.after | `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, `named 28 / resolvable 28 / unnamed_in_skill []`, skill_sha256 f9bd07c2… (r30 filed receipt was 28/28 at 83b0a78a…) | command output; reports/round-30/craft/box1-landed-survey.json |

## 1. Collision matrix

| surface | claim D | claim O | claim C | verdict |
|---|---|---|---|---|
| `tools/exercise-handoff-e2e.py` | EDITS (defaults + prose sources, drafted) | none | none (SKILL.md:448 only describes it) | single-writer; D owns it |
| `reports/round-20/handoff/claims-map.md` | would *want* to edit (source of the stale figures) | none | none | FILED — must not be edited (round rules item 2) → **T-1** |
| `tools/harness/receipt_guard_adoption.py` | none | NEW FILE (drafted) | none | no overlap with D/C |
| `reports/round-34/handoff/declared-in-r7/**` | NEW | none | none | D only |
| `reports/round-30/handoff/declared-in-r6/**` | read-only (superseded generation) | none | none | filed, stays byte-frozen |
| `reports/round-34/craft/box1-resurvey-durable.json` | none | none | NEW | C only |
| `SKILL.md` | none required (no `declared-in-*` pin inside SKILL.md; only :448 names the tool's `--baseline` semantics) | none | digest-pinned at f9bd07c2… | **C's pin freezes SKILL.md bytes for the round — see T-4** |
| `LOG.md` / `SCORECARD.md` | new rows only (SCORECARD:400 records the r30 re-point to declared-in-r6) | new row (adoption-gap debt) | none | parent-applied bookkeeping |
| filed round runners | unchanged (grep: no `reports/round-*/run-validation.py` references `V3_BASELINE_DEFAULT` or `declared-in-r6`) | scanned read-only | none | **no adoption-class change from D's re-pin** — X00's D-vs-O question answered: none |

## 2. Trade findings

### T-1 — depth: the stale figures have two sources the D edit list does not name (blocking for D's threshold)

The r6 packet is the renderer's own render (file digest of packet.md is exactly
freeze.txt's `packet_sha256` 6ced88ad… == expected.json `packet_sha256`), so a
shape-green r7 pair must be the renderer's output. That output's stale text is
not authored in the packet; it is:

1. **carried verbatim from a FILED file.** `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"` (tools/exercise-handoff-e2e.py:184), parsed by `v3_parse_claims_map` (:2289-2320, "the twelve D4 rows as filed") and consumed at :3511; the source string "typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15" is live at reports/round-20/handoff/claims-map.md:104 and flows to packet.md:148. There is **no override**: :184 is a module constant with no CLI flag and no environment reader (`grep "claims.map|claims_map|environ\["` finds only the constant, its docstring, the read-set entry :1957, and the prose copies :2566, :2881, :2934).
2. **hardcoded in the renderer's string table.** OQ-V3-05's stale text is source bytes at tools/exercise-handoff-e2e.py:3526-3527 ("twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts") and is the only other stale prose constant in the tool (grep for the six stale tokens: only :3526-3527).

Consequence: D10's mission ("the exact new-row edits for tools/exercise-handoff-e2e.py:1933-1934 and every other pinning surface") and the D02/D05 route (render via `--freeze`) cannot reach "zero stale figures" by moving the two default lines. Two compliant routes exist, both edits to the shared tool:
 - **(a) prescribed**: repoint :184 to a NEW in-repo map file landed under `reports/round-34/handoff/declared-in-r7/` (new bytes, no filed edit), reword :3526-3527 to the live state, keep the two default lines + the CLAIMS_MAP prose copies (:2566, :2881, :2934) consistent, and add the new map to the read set (:1957) so the freeze re-measures its digest.
 - **(b) rejected alone**: a round-25-style supersession builder. `reports/round-25/v3-supersession/build-revision.py` is the precedent (parent pinned by `PARENT_SHA256`, per-row `count(old)==1` replacements, OQ-V3-05 handled as a passenger line), and its own NOTE states it is "a claim-prose revision, not a renderer build" whose "frozen validators stay byte-identical". That is exactly why it cannot serve here: the v3 run compares the *fresh render* against expected.json's `field_digests` (tools/exercise-handoff-e2e.py:4084-4086 writes expected.json from the same assembly the run re-renders), so a builder-only r7 packet would mismatch the renderer's render. Route (b) is admissible as *evidence*, not as the frozen pair.

Axis at risk: **depth** (the claim's substance). If unmitigated, the r7 pair would be green with the same stale figures — the precise false-green class D13 is chartered to falsify — and the honest verdict would be "unchanged", leaving the round's lowest non-retired axis unworked.

Also for D13: the negative control must be run against the **rendered** packet bytes, not a hand-written draft; today's measured control is available already (old pair exit 0 over stale prose, §0).

### T-2 — calibration + operability: the re-pin re-points a moving default that filed runners invoke bare

`--profile v3` with no `--baseline` resolves through :1933-1934. Filed runners and receipts invoke exactly that bare form: reports/round-21/run-validation.py:622, reports/round-22/run-validation.py:71, reports/round-23/run-validation.py:130, reports/round-24/run-validation.py:174; reports/round-20/run-validation.py:58 and reports/round-11/run-validation.py:144 name the tool as the exercise. After the default moves, an isolated replay of those filed runners measures declared-in-r7 instead of the generation they recorded (r30 receipt: packet 6ced88ad…; r22-era receipt: a97a0f0a…, reports/round-24/box2-d4.md:35). Two harm modes: (i) a green-for-the-wrong-generation pass — the failure SKILL.md:448 warns against ("instead of silently blessing stale prose/pins"); (ii) historical packet digests no longer reproducible from the recorded bare command.

Mitigation, which D10's new-row block must carry: the explicit replay form `--baseline reports/round-30/handoff/declared-in-r6/expected.json` for those filed rounds, and a SCORECARD r34 row (precedent SCORECARD:400) naming the old→new default so the move is a recorded supersession, not a silent one.

### T-3 — operability: an intermediate red window and a hard landing dependency

`v3_freeze` writes `expected.json`, `packet.md`, `twin.json`, `run.log`, `freeze.txt` into the target dir (tools/exercise-handoff-e2e.py:4077-4127) and the run path refuses a missing baseline with `BaselineError("frozen baseline not found: … (write one with --profile v3 --freeze DIR)")` (:3774). Therefore:
 - if the prose sources change (T-1) while the defaults still point at r6, the default run compares a new render against r6's frozen `field_digests` → **the default profile goes red until r7 lands**;
 - if the defaults move before `reports/round-34/handoff/declared-in-r7/expected.json` exists, every default invocation dies with BaselineError.

Landing constraint: new map + prose edits + default move + `--freeze reports/round-34/handoff/declared-in-r7` land as one atomic edit set, and `--profile v3 --quiet` must be green before any other round leg runs. Round-26 recorded the same class ("freeze must follow the re-point edit", SCORECARD:330). Pre-edit landing check measured here: `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` exit 0 (tamper controls green), so a regression after the edit is attributable to the edit.

### T-4 — calibration: claim C's digest pin freezes SKILL.md for the whole round

Claim C binds `reports/round-34/craft/box1-resurvey-durable.json` to SKILL.md f9bd07c2… (measured at HEAD, §0). SKILL.md carries no `declared-in-*` pin (grep: only :448 mentions the tool), so D's re-pin needs no SKILL edit — but any SKILL.md edit landed later in the wave (for D, O, or housekeeping) silently invalidates C's receipt and box-1 reading. Constraint: **no SKILL.md edits in round 34**, or C's receipt is re-derived at close and the digest in claims.json C.before is superseded as a new row. A09 R3/R5 (SKILL sha256 receipts, line anchors) are satisfied by this same held-still condition; A09 R4's contingency ("named_in_skill may move off 28", reports/round-33/adj/A09-pins.md:110) did **not** trigger: measured 28/28 at the new digest.

### T-5 — operability: claim O's inventory denominator is time-dependent

The inventory walks `reports/round-*/run-validation.py`; the round's own runner (S04's spec) and every later round's runner change the denominator. If the integrator lands `reports/round-34/run-validation.py` before running the landed tool, the tool's list differs from O04's predicted inventory (which cannot contain r34) and O07's row-for-row parity check fails for a benign reason. Mitigation: the inventory JSON names its scan stamp, the scanned paths, and any explicit exclusion with a reason (AGENTS.md telemetry discipline: owner + observation window; `null`/`could-not-evaluate` over inferred values). No D×O collision otherwise: no filed runner pins the v3 default (grep empty, §1).

Live anchors for O's taxonomy, so no class needs inventing: adopted pattern — reports/round-32/run-validation.py:1103 `runpy.run_path("tools/harness/receipt_guard.py")`; in-place writers — reports/round-5/run-validation.py:194, reports/round-6/run-validation.py:336, reports/round-7/run-validation.py:1171 (`(HERE / "validation.json").write_text(…)`), reports/round-26/run-validation.py:90 (`OUTPUT = f"{ROUND_DIR}/validation.json"`, with a no-write flag at :1871).

### T-6 — honesty: all three claims' third counting command cannot run in this round's wave

`python3 reports/round-34/run-validation.py` appears in claims.json D/O/C `counting_commands`, but the file does not exist (`ls reports/round-34/` → claims.json, targets.json, telemetry only) and shared rule 4 forbids executing any round runner in-tree (F-C13-1). No seat may report that leg as verified during the wave; it is a close-time measurement in an isolated `git archive` copy, and until then it must be recorded `could-not-evaluate`/owed, never as a pass.

### T-7 — honesty/adjacency: the OQ and ledger rewrites must not read as a resolution

Live D4 reports `rank_rules_unresolved_items 0` and `rank_quarantine_handles 0` (typed-labels.d4.yml:44-45); the round-25 NOTE attributes the rank-row removal to the round-22 family-clean repair (reports/round-25/v3-supersession/build-revision.py NOTE lines). The rewritten OQ-V3-05 / D4-CL09 rows must therefore say: D4 now carries **zero D2L-RANK rows of its own** (12 holds, all D2L-FORM-UNRESOLVED, 0 notes, 0 fails), while the D2-side residuals moved by the r22 repair are D2's, not resolved by this packet. A rewrite that drops the old "(13 rank items, 3 quarantine, 4 conflicts)" without naming where they went reads as a silent resolution — an adjacency-facing claim the lane does not own (canon/closure is operator/lore-owned). D2's current residual counts were not measured by this seat → `to-verify`.

## 3. Axis-harm verdicts (conditional on landed bytes)

| axis | harm pathway | status at this read |
|---|---|---|
| depth | T-1: green-but-stale r7 would make D's depth move nominal | open — depends on the integrator extending the drafted edit set |
| operability | T-2/T-3 moving default; T-5 inventory denominator | open, all mitigable by naming rows/atomic landing |
| calibration | T-2 silent blessing; T-4 SKILL freeze; T-6 unverifiable third leg | open — must be recorded as owed, not passed |
| coverage | none: no claim touches corpus partitions | unchanged |
| freshness | pause in force; no live fetch in D/O/C | unchanged |
| adjacency | T-7: OQ rewrite touching residuals the lane does not own | open — wording constraint named |

Cross-seat consistency: the peer critic seat agrees on T-6 —
`reports/round-34/cross/X02-conformance.md:229` independently states the round-34
runner is "authored and run in its isolated copy"; X02 does not treat
`claims-map.md` or the renderer defaults as an edit surface, so T-1 is carried
by this fragment alone and the integrator should route it to the D block.

No pathway found that harms an axis *if* the mitigations above land; none of the
three claims is blocked outright by a collision. The single blocking-class item
is T-1 for claim D's own threshold.

## Owed

- `reports/round-34/scout/K02-repin-census.md` — absent at this seat's reads
  (`ls reports/round-34/scout` → empty). My §1 surface list is my own grep
  (`grep -rn declared-in-r6` over the tree, excluding `.scratch` and `.git`);
  the integrator must diff it against K02 and add any surface K02 finds that I
  did not (e.g. frozen manifests under `tools/gates/frozen/**` and
  `reports/round-*` reproduced copies — my grep found none referencing
  `exercise-handoff-e2e` or the r6 dir).
- `reports/round-34/cross/X00-connector.md` — absent at this seat's reads; the
  D×O adoption-class question I answered in §1 should be cross-checked against
  X00's matrix, and any X00 row without a counterpart here must be answered
  explicitly.
- D2-side residual counts for T-7 (`to-verify`): the D2 typed-labels coverage
  block's current conflicts/quarantine/rank-item figures were not read here.

## Citations

- `reports/round-34/claims.json` (D/SKILL premises, counting_commands); `reports/round-34/targets.json` (seat X01 mission, shared_rules); `REGIMEN.md:52-58`.
- `git rev-parse HEAD` → da68a6d705e41f369f21e8607bfaab5b54077f84; `git status --porcelain` → only `?? reports/round-34/`.
- `tools/exercise-handoff-e2e.py:184,1933-1934,1957,2289-2320,2566,2881,2934,3511,3526-3527,3774,4077-4127,4084-4086`.
- `reports/round-30/handoff/declared-in-r6/{packet.md:68-69,148-152,307, freeze.txt, expected.json, twin.json, run.log}`; `sha256sum` packet.md = 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb.
- `reports/round-20/handoff/claims-map.md:97,104`; `git log --oneline --follow -- reports/round-20/handoff/claims-map.md` → 35b6797 (r20 admission only).
- `reports/round-25/v3-supersession/build-revision.py:34,43,71-77` + NOTE text.
- `examples/culture-d4/typed-labels.d4.yml:29-48`; `examples/culture-d4/expected-holds.json` (counts, active_pin_generation, digests).
- `SKILL.md:448`; `sha256sum SKILL.md` → f9bd07c2…; `SCORECARD.md:330,400`; `LOG.md:3428`; `README.md` (grep for declared-in/baseline → no match).
- `reports/round-33/adj/A09-pins.md:107-114,116`; `reports/round-30/craft/box1-survey.py` and `box1-landed-survey.json`.
- Filed runner lines cited in T-2/T-5: `reports/round-{11:144,20:58,21:622,22:71,23:130,24:174}/run-validation.py`; `reports/round-{5:194,6:336,7:1171,26:90,1871,32:1103}/run-validation.py`.
- Commands run (all read-only; no round runner executed): `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, packet_sha256=6ced88ad…; `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0; `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, 28/28 at f9bd07c2…; `grep -rn "declared-in-r6"` tree sweep; `git diff --stat -- reports/round-2 reports/round-4 reports/round-5 reports/round-6 reports/round-30` → empty (the e2e run left filed bytes untouched).
