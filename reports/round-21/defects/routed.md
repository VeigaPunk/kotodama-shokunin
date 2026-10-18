# Round 21 O17–O18 — findings routed to round 22

- **Axis:** O / operability.
- **Prepared:** 2026-10-18, from the round-17 through round-20 defect sweeps, reviews, and later bounded controls/recounts available in this checkout.
- **Scope:** routing record only. No round-8–20 artifact is corrected here; this file does not admit, promote, or re-grade any round. Every owner below is a round-22 role; the dispatcher must name the seat before work starts. LOG/SCORECARD integration remains with the parent.
- **Queue snapshot:** `date -u +%Y-%m-%dT%H:%M:%SZ && git rev-parse HEAD && git status --porcelain -- reports/round-17 reports/round-18 reports/round-19 reports/round-20 reports/round-21 && if test -e reports/round-21/defects/routed.md; then printf 'TARGET_EXISTS\n'; exit 1; else printf 'TARGET_ABSENT\n'; fi` ran at `2026-10-18T14:22:00Z`, HEAD `8115eaaeb57c9dce157fe291337cb52dd914c6cf`. The status showed no changes under rounds 17–20 and pre-existing untracked R21 artifacts/directories; the final check printed `TARGET_ABSENT` before creation. Those parallel R21 artifacts are not edited by this router.

## Open items — round 22

### R17-SWEEP-O01 — closure records use the declaration revision as baseline

**Status:** Open; historical metadata correction only. The filed R17 claims and receipt name baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; `LOG.md` and `SCORECARD.md` call `9b49a4a` the baseline, although `git show -s --format='%H %s' 9b49a4a` identifies it as the R17 claims declaration (comparison recorded 2026-10-18; `reports/round-21/defects/sweep-r17.md` §O01).

**Round-22 owner:** integrator / closure-record scribe. Add a dated correction in a new authorized integration record; do not rewrite LOG, SCORECARD, claims, or receipt. **Closure control:** compare the declared baseline in claims/receipt with the corrected record and resolve both revisions with `git show -s`.

### R17-CURRENT-RECOUNT-DISCREPANCY — current-tree C/D/O readings differ from filed receipt

**Status:** Open; current-tree observations do not alter R17's historical receipt or verdict. In disposable clone HEAD `8115eaa…`, `python3 reports/round-17/run-validation.py` (2026-10-18) exited 1. The C recount reports recorded attempt/fix/fragment counts `5/7/16` versus current `0/0/0`; D reports `examples/culture-d2/expected-holds.json` changed from SHA `a5dc26d5…` to `7b9439c4…`, two adapter builds exit 2 and an adapter pin mismatch. O also changes from pass to fail on the same pinned D2/D3 byte mismatch. The same R17 frozen replay reproduces 5/5. See `reports/round-21/recount/r17-1.md`–`r17-4.md` for the commands and row-level boundary; the replay result is not a correction to the receipt.

**Round-22 owner:** R17 recount/integration owner, with D2/D3 adapter and pin owners for the technical discrepancy. Attribute the changed counts and pins in a new isolated recount disposition; preserve the filed receipt. **Closure control:** run the full validator only in a disposable clone with `TMPDIR` under `.scratch`, compare each filed/current metric and pin, record the exit and exact command/date, and confirm no protected source receipt was written.

### R17-D33-F1 — phonology prose contradicts its coda data

**Status:** Open component consistency finding. `examples/culture-d4/components/02-phonology.yml:30` says “codas limited to four consonants,” while its coda list and phonotactics record specify eight (`:83-91`, `:118-120`). `reports/round-17/reviews/review-1.md` §3 F1 records the component/data cross-read and proposed control (2026-10-18, 09:45–09:52Z).

**Round-22 owner:** D06 / phonology component owner. Reconcile the prose with the delivered data in a new authorized component revision. **Closure control:** re-derive the coda declaration and confirm either the stale four-consonant phrase is removed or the data and witnesses consistently implement the chosen limit.

### R17-D33-F2 — lexicon `coverage_notes` are stale

**Status:** Open bookkeeping finding. `examples/culture-d4/components/04-lexicon.yml:198-201` does not match its delivered record counts/routes; review-1 F2's 2026-10-18 census reports 49 declared versus 54 records and a route split of root 44 versus root 43 plus one lexicalized item (the audit's `grep`/recount; see `reports/round-17/reviews/review-1.md` §3 F2).

**Round-22 owner:** D07 / lexicon component owner. Recompute the maps from the delivered records; keep the data and note in agreement. **Closure control:** independently recount fields and routes from the component and compare each declared map with that recount; preserve the command and date in the new record.

### R17-D33-F3 — myth component points to a nonexistent register component

**Status:** Open stale-reference finding. `examples/culture-d4/components/06-myth.yml:19` assigns sayings/oath formulas to “the register component”; the delivered 12-component registry has no such component. Evidence and the record-level registry cross-read are in `reports/round-17/reviews/review-1.md` §3 F3 (2026-10-18).

**Round-22 owner:** D11 / myth component owner, with the integrator confirming the landed owner. Name the real owner or remove the unsupported reference in a new authorized revision. **Closure control:** resolve every named component against the delivered registry.

### R17-D33-F4 — two office/rank terms are undeclared

**Status:** Open vocabulary finding. The review identifies `broker` in `09-costumes.yml` and `weigh-master` in `07-symbolism.yml` as terms absent from the declared rank/office vocabulary; the reviewer’s source scan is recorded in `reports/round-17/reviews/review-1.md` §3 F4 (2026-10-18).

**Round-22 owner:** D14 / costume-rank vocabulary owner, with the symbolism owner if needed. Declare the offices or replace them with owned terms; do not make a canon decision. **Closure control:** rerun `grep -rn "broker\|weigh-master" examples/culture-d4/components/*.yml` and show each remaining use resolves to a declared term.

### R17-D34-F5 — natural-class allophony still needs a finite expansion or disposition

**Status:** Open. The phonology gate retains `A-CLASS REVIEW` for `s → z / V _ V`; the gate requires finite contextual expansion, and the review says the reviewer’s run retained the finding. See `reports/round-17/reviews/review-2.md` §§1.1, 2 F5 (2026-10-18, 09:45–09:52Z).

**Round-22 owner:** D06 / phonology owner. Supply a finite rule expansion or a named design disposition; do not treat the unrelated coda prose correction as closure. **Closure control:** run the phonology gate over the settled packet and show the `A-CLASS` finding is either removed by finite rules or explicitly dispositioned.

### R17-D36-F7 — competing D4 hold-set declarations lack a parent disposition

**Status:** Open design/contract choice. R17 review-4 records the delivered registry/brief set as 6 holds / 0 notes / 0 fails and the separate weigh-court fragment as 17 / 1 / 0. R18's extraction records 15 emitted holds + 1 note against the 6/0/0 declaration; the later R20 projection still emits 15/1. The source readings and extraction commands are dated 2026-10-18 (`reports/round-17/reviews/review-4.md` F7; `reports/round-18/d4/holds.md` §§0, 3–5; `reports/round-20/wart/review.md` §2 M5). No parent choice between the competing pre-implementation declarations is evidenced.

**Round-22 owner:** parent / D4 contract-design owner. Record which declaration is authoritative and how the emitted set is governed; do not infer authority from whichever projection was used later. **Closure control:** a new contract disposition names the controlling declaration and subsequent equality test; old reviews, declarations, and receipts remain unchanged.

### R17-ASSEMBLER-F-O-2 — weigh-court and furnace-league designs remain unadjudicated

**Status:** Open design disposition. The R17 assembler integration says the delivered components use the furnace-league FIRE/MARK family while `design-brief.md` describes weigh-court COUNT×QUOTE; its flexible merge behavior records the divergence but does not decide it (`reports/round-17/assembler/impl.md` §4 F-O-2; `integration.md` §5, 2026-10-18). Later use of the furnace-league tree is not itself evidence of a parent adjudication.

**Round-22 owner:** integrator / D4 design owner. Record the selected design or explicitly retain both as distinct alternatives and define the active contract. **Closure control:** compare the dated disposition with the delivered component registry and packet keys; no canon ruling is implied.

### R17-D37-F8 — runner clearance detector is negation-blind

**Status:** Open runner defect; the D4 wording workaround does not fix the detector. `reports/round-17/run-validation.py:131` matches `accepted by lore` without accounting for negation. Review-5 demonstrates that “not accepted by lore-shokunin” matches while “no lore acceptance is claimed or implied” does not (`reports/round-17/reviews/review-5.md` §2 F8, 2026-10-18 09:57Z).

**Round-22 owner:** R17 validation-runner maintainer. Add a positive and a negative disclaimer fixture. **Closure control:** the natural negated phrase must not trigger `clearance/acceptance claim found`, while a genuine “accepted by lore-shokunin” claim still does; run the runner selftest in an isolated fixture and retain both outputs.

### R18-SWEEP-O04 — R18 admission records mislabel the baseline

**Status:** Open metadata correction; R18's green receipt is not overturned. Claims and receipt declare baseline `3dd3754207032cb81f5fb3e202fe85cf79211339`; LOG/SHONEN instead label `c66ac3c` (the R18 declaration) as baseline. `git show -s --format='%H %s' c66ac3c 3dd3754` distinguishes the two revisions (2026-10-18; `reports/round-21/defects/sweep-r18.md` §O04).

**Round-22 owner:** integrator / closure-record scribe. Add a dated correction in a new authorized record, preserving LOG and SHONEN. **Closure control:** compare claims/receipt and corrected admission record, and resolve both revisions with `git show -s`.

### R18-GATE-F1 — packet-controlled assembler path is loaded as code

**Status:** Open security/bypass finding; no hostile probe is authorized in the live tree. R18 review-4 shows that `candidate_path` accepts absolute/parent-traversal paths and `load_peer` uses `runpy.run_path`; a packet can name an assembler that the gate executes and that can self-attest. Probes were repeated at two gate revisions on 2026-10-18 10:36Z and 10:42Z (`reports/round-18/gate/reviews.md` §2 F1; current code locations were re-read at `typed-pipeline-gate.py:169-171, 203-209`).

**Round-22 owner:** typed-gate security/maintainer. Bind executable peers to trusted, lane-contained code and reject untrusted paths before load. **Closure control:** isolated negative fixtures for absolute and `..` paths prove no marker code executes and the gate fails closed; include a trusted-path positive control.

### R18-GATE-F2 — alias collision silently overrides the declared assembler

**Status:** Open configuration ambiguity. R18 review-4 demonstrates that `assembly.generator` can override `typed_pipeline.assembler` by iteration order rather than rejecting a conflict (`declared_paths` and alias resolution; review probes 2026-10-18 10:36Z/10:42Z; `reports/round-18/gate/reviews.md` §2 F2; current code `typed-pipeline-gate.py:248-259`).

**Round-22 owner:** typed-gate configuration maintainer. Deduplicate by canonical key and fail closed or emit an explicit conflict result. **Closure control:** isolated conflicting-alias fixture must be rejected; identical declarations and the default D2 path must remain deterministic.

### R18-GATE-F3 — identity leg can be skipped through packet-selected serializer

**Status:** Open bypass/contract ambiguity. Review-4 found `identity_requested` can be false when the resolved assembler equals the D2 serializer, leaving no gate-level assembler identity check; the exemption is selected through packet configuration (`reports/round-18/gate/reviews.md` §2 F3; current code `typed-pipeline-gate.py:476-477`; probes 2026-10-18 10:42Z).

**Round-22 owner:** typed-gate maintainer. Run identity verification on every generalized pipeline or expose any exemption as an explicit, justified result that cannot be chosen by the packet. **Closure control:** a tampered isolated packet cannot bypass identity verification; normal D2 and D4 positive controls still pass.

### R18-GATE-F4 — generalized expected-hold path is packet-controlled

**Status:** Open expected-set trust-boundary finding. Review-4's scratch probes show a packet or flag can supply an internally consistent expected set, making the expected-hold equality leg self-selected (`reports/round-18/gate/reviews.md` §2 F4; probes 2026-10-18 10:36Z/10:42Z; current config resolution at `typed-pipeline-gate.py:502+`).

**Round-22 owner:** typed-gate security/contract maintainer. Bind the expected set to a trusted digest/registry or refuse packet-selected paths outside the authorized family. **Closure control:** isolated negative fixtures cannot substitute a scratch expected set; the trusted expected file is positively loaded and the full comparison remains bidirectional.

### R18-D4-MISSING-PACKET-TRACEBACK — missing D4 input exits with an uncaught traceback

**Status:** Open error-contract defect pending a final-revision control. `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/absent.yml` produced `FileNotFoundError`, exit 1, traceback; the same path shape on D2 and family-less inputs returned exit 2 without traceback. The defect reproduced in an isolated mirror; the report explicitly required retesting the final revision (`reports/round-18/d4/gate-runs-3.md` §3, `gate-runs-4.md` §§2, 5; dated 2026-10-18).

**Round-22 owner:** typed-gate CLI/error-handling owner. Convert the missing D4 input to a stable fail-closed diagnostic with documented exit 2. **Closure control:** run the negative case in an isolated mirror and assert exit 2, named missing path, no traceback; include D2 and family-less controls.

### R18-ORIGINAL-FROZEN-REPLAY — superseded D4 row has no successor disposition

**Status:** Open; leave the historical manifest unchanged. In an isolated scratch replay on 2026-10-18 10:50:16−03:00, `python3 tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv --json` exited 1 with 1/2 rows reproduced; the D4 projection row was `replay_mismatch`, recorded projection `a59990bb…` versus current `cbcf997f…` (`reports/round-21/defects/regression.md` §Frozen replay measurements; `reports/round-21/defects/fix-16.md`; precursor `reports/round-20/regression.md` F-O15-1). The R18 `repin-d2` successor replays 11/11, but does not supersede this D4 row.

**Round-22 owner:** frozen-replay owner. Add a new frozen generation for the changed D4 projection or a named supersession record with fresh digest and replay evidence. **Closure control:** replay the successor in isolation and preserve `tools/gates/frozen/round-18/MANIFEST.tsv` byte-for-byte.

### R19-SWEEP-O06 — R19 receipt binds to the declaration, not the declared baseline

**Status:** Open metadata/receipt reconciliation; the filed acceptance-true value is not reinterpreted here. `claims.json` declares R18 admit `e5718945a1ab0a0c3db955338d2cae77d68fd348`; `validation.json`, LOG and SHONEN use `169c616` (R19 declaration). The dated revision comparison is `git show -s --format='%H %s' e571894 169c616` (`reports/round-21/defects/sweep-r19.md` §O06, 2026-10-18).

**Round-22 owner:** integrator / validation-receipt owner. Reconcile via a new authorized record or isolated remeasurement; do not rewrite the R19 receipt or infer a new acceptance outcome. **Closure control:** corrected baseline binding and any new measurement are tied to the exact claims baseline and dated command.

### R19-SCRIBE-SEAT-FAILURE — recurrence prevention for close-time fallback is missing

**Status:** Open process control; the bounded fallback itself is documented. R19 `validation.json` says “integrator-authored harness (scribe seat failed); all measurements re-run at close,” records the runner command and acceptance true; the cause of the assigned seat failure remains `to-verify` (`reports/round-21/defects/fix-10.md`, 2026-10-18).

**Round-22 owner:** operator / integrator. Define a named failure trigger, fallback owner, and retained handoff receipt; do not infer the R19 cause or replace its receipt. **Closure control:** an isolated dispatch/close rehearsal demonstrates the trigger and records the assigned seat, fallback, and exact close command.

### R19-LESSON-PATH-COLLISION — parent disposition for the D4 lesson path is outstanding

**Status:** Open integration choice; preserve both extant artifacts. R19-D08 and X21 shared `corpus/lessons/round-19.md`; the survey occupies that path while the D4 lesson fragment remains `reports/round-19/integration/d4-lessons-entry.md`. The collision and unchosen destinations are recorded in `reports/round-19/integration/fragment-ledger.md` §3 and `reports/round-21/defects/fix-11.md` (R20 census in `reports/round-20/audit/x24-lessons-audit.md` §§1, 3, 2026-10-18).

**Round-22 owner:** parent / integrator. Choose append-with-authorship, a distinct path, or drop, and record the pointer. This router selects no canonical lesson location and writes no corpus content. **Closure control:** the chosen pointer resolves and the integration record preserves authorship and the parent decision.

### R19-AVAILABILITY-COMPLETION — completion count is not evidenced

**Status:** Open evidence gap, not a provider failure. `reports/round-19/availability.json` leaves `completed_workers: null`; its own note says the seat could not observe completion. A read-only JSON check on 2026-10-18T14:11:07Z found no `completed_workers` key in `reports/round-19/validation.json`, despite the close receipt existing. The original availability record says the route dispatched and work landed; none of this proves worker completion count.

**Round-22 owner:** dispatcher / availability-record integrator. Obtain an authorized dispatch/completion record if one exists, or explicitly retain `to-verify`; do not fill the field from requested/launched counts. **Closure control:** a source record supports any populated count and is cross-linked, or the field remains explicitly unknown with the acceptance receipt separately cited.

### R19-X26-1 — two corpus `couples:` pointers target a missing path

**Status:** Open path correction. R19 C11 and C16 entries point to `corpus/knowledge/linguistics/phonology-sanity.md`; the path is absent while `phonetics-phonology.md` exists. Both reviewers independently report the same issue (`reports/round-19/entries/review-C11.md` §5 R19C21-F1 and `review-C16.md` §5 R19C26-F1); the R21 adjacency ledger repeats it at `reports/round-21/adjacency/ledger.json:114` (path check dated 2026-10-18).

**Round-22 owner:** corpus-entry integration owner. Produce a new dated correction/pointer for both entries; do not edit either historical review in this router. **Closure control:** resolve each corrected `couples:` target from its source directory and retain a `test -f`/link-check result.

### R19-C24-F1 — battery-surface entry still carries a superseded measurement

**Status:** Open documentation correction; the battery operation itself is now green. The R19 review recorded an in-flight `pass 8 / unevaluable 1 / exit 2 / 9/9` result at 11:38Z, and marked the entry’s prior `pass 7` and “D4 outside battery” statements stale (`reports/round-19/entries/review-C14.md` §§2, 5 F1). Later controls show `python3 tools/check-gate-battery.py` exit 0, pass 7, unevaluable 0, baseline coverage 9/9 on 2026-10-18 10:50:15−03:00 (`reports/round-21/defects/regression.md`, “Battery and craft”); `reports/round-20/readme/reconcile.md` §§4–5 also dates the D4 coverage correction. The open item is the old knowledge-entry wording, not a current battery failure.

**Round-22 owner:** corpus-entry integrator with the battery maintainer. Add a new dated correction/qualification that distinguishes the seven selftests from nine baseline-covered gates. **Closure control:** re-run the battery and independently inspect the entry’s coverage statement; retain the green command output without rewriting the round-19 review.

### R19-C24-F2 — battery entry’s quoted absence sweep is false

**Status:** Open wording correction. The quoted `grep -rln "check-gate-battery\|gate battery\|battery_exit" corpus/knowledge/` returned a pre-existing `verification-independence-anti-circularity.md`, not zero files (`reports/round-19/entries/review-C14.md` §3, 2026-10-18 11:40Z). The actual scope gap may remain; the literal absence claim does not.

**Round-22 owner:** corpus-entry integrator. Replace the false absence claim with a scoped, dated qualification in a new authorized record. **Closure control:** rerun the cited search and state the scope distinction; do not use the scope gap as evidence for literal absence.

### R19-C27-F1 — generated-artifact entry’s quoted absence sweep is false

**Status:** Open wording correction. The quoted `grep -rln "generated artifact\|never hand-edit\|rebuild" corpus/knowledge/synthesis/` matched `loanword-material-dating.md` on “rebuilding” (review at 2026-10-18 11:40Z; `reports/round-19/entries/review-C17.md` §§3, 5 F1).

**Round-22 owner:** corpus-entry integrator. Narrow the search claim to the actual intended phrase/word boundary or document the hit. **Closure control:** rerun the exact revised search with date and output, preserving the stated scope gap separately.

### R19-C28-F1 — disposition-workflow entry’s quoted absence sweep is false

**Status:** Open wording correction. The quoted synthesis search for `disposition|finding severity|design debt` matched `worldbible-integration-contract.md` and `naming-canon-workflow.md` (review at 2026-10-18 11:40Z; `reports/round-19/entries/review-C20.md` §§3, 5 F1). The missing design-workflow gap is distinct from the false zero-hit claim.

**Round-22 owner:** corpus-entry integrator. Correct the search scope/claim in a new authorized record. **Closure control:** rerun the exact scoped search and retain its matches; do not turn a distinction about workflow scope into a claim that no lexical matches exist.

### R20-SWEEP-O07 — R20 closure records mislabel the baseline

**Status:** Open metadata correction; the R20 admitted verdict is not overturned. Claims and receipt name baseline `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`; LOG/SHONEN name `122086b`, which `git show -s --format='%H %s' 122086b caf1beac` identifies as R20 declaration versus R19 admit (2026-10-18; `reports/round-21/defects/sweep-r20.md` §O07).

**Round-22 owner:** integrator / closure-record scribe. Add a dated correction in a new authorized integration record; preserve LOG/SHONEN history. **Closure control:** compare declared baseline with claims/receipt and resolve both revisions with `git show -s`.

### R20-HISTORICAL-RECEIPT-REWRITE — add a prevention control for live historical reruns

**Status:** Open process safeguard; the transient changes are documented as restored, not current mutations. R20 evidence records R5/R7/R9 validation receipts modified during live historical-validator runs; R5 and R7 were outside R20's declared 8–19 freeze, while the R9 receipt temporarily flipped acceptance true→false and was restored by 13:03:17Z. Later R20/R21 read-only comparisons found the currently committed protected range unchanged; that does not undo the incident. See `reports/round-20/adjacency.md` §§74–99, `reports/round-20/regression.md` F-O15-2, and `reports/round-21/defects/sweep-r20.md` §O08 (2026-10-18).

**Round-22 owner:** operator / integrator. Require historical validators that write receipts to run only in disposable clones, snapshot protected hashes before/after, and file any correction append-only. **Closure control:** a controlled isolated rerun plus before/after hashes demonstrates no live protected receipt mutation; do not restore or regenerate earlier-round paths as part of this routing.

### R20-CONTRACT-AUDIT-RECOUNT — current isolated R20 check fails while filed receipt is green

**Status:** Open; cause unresolved. `python3 reports/round-20/run-validation.py --check` in the isolated R21 recount clone (2026-10-18T13:50:01Z) exited 1: C/O passed, D failed because the selected contract-audit artifact was classified `fail`, while the filed R20 receipt records acceptance true. The selected census reproduced 27 rows and statuses 16/7/4; that is a separate passing reading (`reports/round-21/recount/r20-1.md`, `r20-3.md`).

**Round-22 owner:** R20 contract-audit / integration owner. Reconcile the selected audit artifact and filed evidence without rewriting historical files or guessing the cause. **Closure control:** reproduce in an isolated clone, identify the exact audit path and failing verdict, and record a bounded disposition with command/date; separately preserve the filed receipt.

### R20-HANDOFF-LINK-COUNT — build-16 packet count differs from later link replay

**Status:** Open bookkeeping discrepancy; do not silently replace either reading. Independent `packet_links.py --packet reports/round-20/handoff/twin.json` and `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` each reported 105/105 at 2026-10-18T13:51:02Z; filed `packet-v3-16.md` §validation records 102/102 at 13:14:00Z (`reports/round-21/recount/r20-2.md`). Later final packet/twin controls are separately closed below; this item concerns the named build-16 receipt.

**Round-22 owner:** handoff packet / integration owner. Explain whether the 3-link difference is a build-version distinction or a receipt error in a new append-only record. **Closure control:** cross-read the exact packet build and machine twin, rerun both link readers, and bind the disposition to packet/twin hashes and timestamps.

### R20-FRAGMENT-INDEX-COLLISION — canonical index pointer is undecided

**Status:** Open parent decision; both snapshots remain intact. `reports/round-20/fragment-index.md` and `fragment-index-x24.md` coexist. X24's inventory control reported indexed 72 / observed 72, no unindexed paths at 2026-10-18T13:28:33Z, but explicitly did not decide authority (`reports/round-21/defects/fix-12.md`).

**Round-22 owner:** parent / integrator. Select or generate the canonical pointer only after the final artifact set settles. **Closure control:** the chosen index resolves to the settled inventory and the parent’s canonical choice is explicit; do not delete or rewrite the peer-owned snapshots.

### R20-MALFORMED-ALIAS-FAIL-OPEN — non-string era-alias value becomes confirmed

**Status:** Open projector validation defect; full CLI refusal remains unverified. `packet_alias_rows()` stringifies each tag and labels the row confirmed (`tools/d2-typed-labels.py:2486-2492`). The R21 direct helper probe with `era_aliases: {"era-9": [1, 2]}` produced alias `"[1, 2]"` and `status: confirmed` on 2026-10-18; see the exact command in `reports/round-21/defects/fix-14.md`. This did not exercise the full packet/CLI path.

**Round-22 owner:** `tools/d2-typed-labels.py` projector owner. Reject non-string or grammar-invalid tags before projection and add a named negative control. **Closure control:** run a full isolated packet/CLI negative fixture proving the malformed value cannot be emitted as confirmed; retain a valid-alias positive control and the command/date.

### R20-KEEP-DEAD-CLI — `--keep DIR` is parsed but not honored

**Status:** Open interface defect. R20 interop records `--keep` as parsed but never passed to the run (`reports/round-20/handoff/interop.md` §4, 2026-10-18). The current source has the parser declaration at `tools/exercise-handoff-e2e.py:4407`; the R21 source/AST review found no `keep` attribute use. Do not treat argument recognition as persistence behavior.

**Round-22 owner:** handoff CLI owner. Either implement keeping the isolated packet directory at the requested destination or remove/clarify the option in the supported contract. **Closure control:** an isolated end-to-end invocation with a temporary target proves the expected files are retained there, or a revised help/contract and negative test prove the unsupported option is rejected.

### R20-D4-ASSEMBLY-SELFTEST — selftest duty for the D4 assembly gate is unresolved

**Status:** Open contract/control question, distinct from the closed battery unevaluable defect. R20 reconciliation records that `d4-assembly-check-gate.py --selftest` returns exit 2 because the gate has no `--selftest`; R21 regression confirms the CLI is `[PACKET]`, while the ordinary packet check is green and battery reports 7 selftests plus 9/9 baseline coverage (`reports/round-20/readme/reconcile.md` §§4–5, 2026-10-18; `reports/round-21/defects/regression.md`, “Typed / assembly selftests” and “Battery and craft,” 10:50:15–10:50:16−03:00).

**Round-22 owner:** D4 gate owner with battery/contract integrator. Implement a meaningful selftest or explicitly disposition the selftest duty and name its substitute control. **Closure control:** either a positive/negative selftest passes under its declared interface, or a dated contract disposition demonstrates which test covers the duty; do not reopen the separate green battery result.

## Needs current-state check / pointer

- **R17-ROUTE-CAPACITY — actual attendance remains `to-verify`.** The R17 declaration mismatch (64 declared vs 60 target seats) is closed at declaration level by R18's balanced 64-seat allocation (20+28+10+6); the read-only arithmetic command is in `reports/round-21/defects/fix-09.md` (2026-10-18). It does not prove R17 dispatch or attendance. **Round-22 owner:** operator/dispatcher; consult an authorized dispatch log if one exists, otherwise retain `to-verify`. Do not infer staffing from claims/targets.
- **R18-FINAL-REPORT-POINTER / R19-FINAL-REPORT-POINTER / R20-FINAL-REPORT-POINTER.** The dated repo-only sweeps found no lane-local authorized final report for R18, found R19 still represented by an explicitly non-final draft, and found R20's draft explicitly non-final (`reports/round-21/defects/sweep-r18.md` O03, `sweep-r19.md` O05, `sweep-r20.md` O07; 2026-10-18). External filing was not inspected. **Round-22 owner:** integrator; request or record the authorized external pointer. Do not state that no external report exists without checking through an authorized route.
- **R20-LEDGER-SNAPSHOT-F1 — R9 runner current state requires isolated verification.** R20's ledger snapshot records `python3 reports/round-9/run-validation.py` exit 1 because no `expected.json` baseline for the typed-pipeline gate was found under the named roots; the clean-HEAD mirror produced the same output (`reports/round-20/ledger-snapshot.md` §3 F1, 2026-10-18 13:08–13:10Z). This is an R20-reported R9 runner issue, not evidence of a new R17–R20 receipt failure. **Round-22 owner:** historical-runner/recheck owner. Recheck only in a disposable clone with `TMPDIR=$PWD/.scratch`, because the runner writes its receipt; preserve the live tree and record whether the issue remains or has a later authorized disposition.

## Resolved or not routed as open

- **R17 worker/seat arithmetic — declaration-level closure only.** R18 claims/targets declare 64 and allocate 64 seats; R21 fix-09's dated Python arithmetic control confirms the declarations reconcile. Actual R17 dispatch/attendance stays in the check section above.
- **R17 missing D4 typed chain and original R17 frozen replay.** R17 review-4's missing typed inputs were later supplied for R18; R21 recount records the current R17 frozen manifest at 5/5. R17's filed rejection remains historical and is not retroactively changed (`reports/round-21/defects/ledger.json` R17-HISTORICAL-D-REJECTION and R17-CURRENT-RECOUNT-DISCREPANCY; recount 2026-10-18).
- **R19 D4 adapter selftest failure / foreign-tree mirror wart.** R19's selftest failure (4/11) and foreign-tree copy are bounded closed by final R20 controls and independent R21 readings: adapter selftest 12/12, no D2 tree in the D4 mirror, `foreign_tree_copy_in_adapter: false` (`reports/round-21/defects/ledger.json` R19-ADAPTER-SELFTEST / R19-MIRROR-FAITHFULNESS-WART; R21 regression/recount, 2026-10-18). The separate malformed-alias defect above is not closed by those controls.
- **R19 battery unevaluable defect.** The R19 battery contract failure is closed by R20/R21 green battery runs (pass 7, unevaluable 0; 9/9 baseline coverage, commands and dates in `reports/round-20/regression.md` and `reports/round-21/defects/regression.md`). The stale R19 corpus entry correction remains open above.
- **R20 intermediate runner-receipt binding.** Final `reports/round-20/validation.json` runner digest matches the current runner; R21 fix-15 records the dated SHA/stat control. This closes the final-receipt binding concern, not measurement correctness.
- **R20 F-INT-1 packet/twin divergence at intermediate builds.** The later R21 v3 end-to-end control reports 27 claims, statuses 16/7/4 and 105/105 links, with final `packet.md` and twin hashes matching their expected pins (`reports/round-21/adjacency/ledger.json` checks at 2026-10-18T13:49:39Z–13:56:40Z). This closes the final packet/twin mismatch only; the separate build-16 102-vs-105 receipt discrepancy remains routed above.
- **R20 linguistics declared-vs-live count.** The 20-vs-19 delta is explicitly documented in the README and R20 claim passed with that qualification; the R21 recount found no unexplained discrepancy (`reports/round-21/recount/r20-4.md`, counting command 2026-10-18T13:51:05Z). Monitor wording in future coverage claims; no separate defect route.
- **Expected historical replay refusals.** Round-11's old frozen row is an expected superseded digest; R21's isolated regression copied its ignored `run.log` before the final run and reproduced the documented refusal, while the R18 and R20 successor re-pins replayed 11/11. Do not route or rewrite the old manifest (`reports/round-21/defects/regression.md` §§5–6, 2026-10-18 10:50:50−03:00).

## Exclusions and boundaries

- The new R21 adjacency finding `A21-D4-XF-01` is outside this R17–R20 operability route and remains with its separate adjacency/projector disposition; this file does not make a canon or semantic decision about it (`reports/round-21/adjacency/ledger.json`, finding dated 2026-10-18).
- R20's informational/stale X24 path references are historical context, not current defects. R17's old D4 rejection and all prior receipts remain immutable; no promotion or acceptance is inferred.
- No external report absence is asserted; see the pointer requests above. No R22 fix is claimed by this router.

**Routing result:** the open findings and verification requests above are handed to round-22 roles. This record routes work only; no finding is represented as repaired or promoted here.
