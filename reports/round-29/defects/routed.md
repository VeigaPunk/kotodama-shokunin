# Round 29 — unresolved R25–R28 routes to R30 (O17–O18)

- **Audit date:** 2026-10-18.
- **Purpose:** route non-fixed findings to a named R30 owner and a verifiable closure control. This is an engineering handoff, not a canon, source-merits, or round-acceptance decision.
- **Preservation:** keep filed rounds 8–28 and the append-only `reports/round-29/defects/ledger.json` unchanged. R30 should record any status changes in a successor artifact, not rewrite these records.

## Ledger status and disposition rule

On 2026-10-18, `python3 -c 'import json,sys,collections; d=json.load(open(sys.argv[1])); c=collections.Counter(x["status"] for x in d["entries"]); print(dict(sorted(c.items()))); print("open IDs:", ", ".join(x["id"] for x in d["entries"] if x["status"] == "open")); print("observation IDs:", ", ".join(x["id"] for x in d["entries"] if x["status"] == "observation"))' reports/round-29/defects/ledger.json` returned `closed=3, observation=3, open=16, superseded=2`. Every open ID is routed below. `R25-ARGOT-REGISTER-RELATION-ABSENT` has new, narrow closure evidence on the present packet; it remains historically open in the ledger until R30 records that scoped closure in a successor. Do not read an exit-zero result on a different leg as closure for any other argot or law finding.

## Typed pipeline

### `R25-TYPED-ROUTING-HOLD-LAUNDERING` — route to the owner of `tools/gates/typed-pipeline-gate.py`

On 2026-10-18, each of `python3 tools/gates/typed-pipeline-gate.py .scratch/r29-routing-typed/culture-d4/single-null-hold.yml` and the same command with `single-missing-hold.yml` exited `0` at `17/17` legs even though one moved row had, respectively, a null `hold` or no `hold` key. These are separate bypasses. Add a separate negative control for each shape; both must refuse or report the hold-set mismatch. Retain the valid-null and clean-packet controls. Evidence: `ledger.json` entry and sources at `reports/round-25/audit/o18-gate-input-adversarial.md:195-218` and `reports/round-25/scribe/x46-gate-input-cold-rerun.md:163-170`.

### `R25-TYPED-INPUT-REFUSAL-TRACEBACKS` — route to the owner of `tools/gates/typed-pipeline-gate.py`

On 2026-10-18, `python3 tools/gates/typed-pipeline-gate.py .scratch/r29-routing-typed/culture-d4/missing-source.yml` exited `1` with an uncaught `FileNotFoundError` traceback; the same command on `source-less-missing-record.yml` exited `1` with `KeyError: 'record'`. Guard source reads and semantic row access. R30 closure requires end-to-end malformed-input fixtures for both shapes, each producing the documented exit `2`, a named could-not-evaluate refusal, and no traceback. Evidence: `ledger.json`; historical probe sources at `reports/round-25/audit/o18-gate-input-adversarial.md:152-193` and `reports/round-25/scribe/x46-gate-input-cold-rerun.md:235-258`.

## Argot and register-stratum checks

### `R25-ARGOT-REGISTER-RELATION-ABSENT` — route to the R30 register-stratum / argot owner; narrow closure candidate

On 2026-10-18, `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` returned `records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`, exit `0`; `python3 tools/assemble-culture-d4.py --check` reported byte-identical assembly. The former empty-derived-pair gap is no longer present in these bytes. R30 should verify that the eight packet pairs are the declared relation and record closure of this ID in a successor ledger, keeping the older empty-domain readings as history. This is only the relation-presence disposition; it does not close the identity, typing, borrowing, operation-detection, or diphthong routes below. Source trail: `ledger.json` and `reports/round-25/audit/x47-argot-negatives.md:171-176,202-234`.

### `R26-ARGOT-DERIVATION-IDENTITY-AND-PAIR-SCOPE` — route to the owner of `tools/gates/argot-derivation-gate.py`

On 2026-10-18, the current gate exited `0` on the `.scratch/r29-routing-argot/` dangling-base, self-derived, and out-of-inventory probes; the half-pair probe omitted the pair from `derived_pairs` instead of reporting it. Resolve each base to a packet record, reject identity derivations unless the declared operation allows them, and hold malformed half-pairs rather than dropping them. R30 closure needs named negative controls for all three attack classes plus a valid declared-pair positive control. Evidence and earlier probes: `ledger.json`; `reports/round-26/argot/D21-adversarial-replay.md:115-138,140-171,173-197,258-276`.

### `R26-ARGOT-LABEL-TYPING-AND-REGISTER-SCOPE` — route to the owner of `tools/gates/argot-derivation-gate.py`

On 2026-10-18, the current gate exited `0` for both `.scratch/r27-d19/C1-full-gloss-on-register-slot.yml` and `.scratch/r27-d19/C2-full-prose-register.yml`; the same full-gloss fixture was rejected by `tools/d2-typed-labels.py` with `D2L-NATIVE`. Apply the label-typing table before arithmetic replay and keep gloss, native-form, borrowed-strata, and argot-register channels distinct. Closure requires the same-byte projector comparison and paired typed-label / argot-gate controls that reject prose in a form slot without rejecting valid register forms. Evidence: `ledger.json`; `reports/round-26/argot/D22-label-typing-crosscheck.md:40-96,98-160,190-207` and `reports/round-27/argot/D19-label-typing-crosscheck.md:129-155,157-176`.

### `R26-ARGOT-BORROW-REPLAY-OVERPERMISSIVE` — observation remeasured; route to the owner of `tools/gates/argot-derivation-gate.py`

On 2026-10-18, `python3 .scratch/r26-d21/probeE.py` showed the E3 arbitrary-substitution borrow probe still exits `0`, while its E3b mismatch control exits `1`. Keep this as a newly actionable R30 route, not as a claim that the historical observation was always open. Require donor-side correspondence and recipient-inventory legality; add explicit oversubstitution and mismatch negatives, plus a valid borrow positive. R30 should update status only in a successor ledger. Evidence: `ledger.json` and `reports/round-26/argot/D23-overmatch.md:87-121,173-188,190-200`.

### `R26-ARGOT-PROSE-OPERATION-DETECTOR` — observation remeasured; route to the owner of `tools/gates/argot-derivation-gate.py`

On 2026-10-18, `python3 .scratch/r26-d21/probeB.py` reproduced three prose-triggered `D4L-ARGOT-COVERAGE` holds and three synonym controls that remained clean. Replace unanchored prose-substring detection with typed operation declarations. Closure requires paired declarations/prose variants proving that only the typed field controls coverage; update the observation in a successor ledger after that result. Evidence: `ledger.json` and `reports/round-26/argot/D23-overmatch.md:36-85,183-200`.

### `R27-HEAD2-DIPHTHONG-VERDICT-INVERSION` — route to the owner of `tools/gates/argot-derivation-gate.py`

On 2026-10-18, `python3 -B tools/gates/argot-derivation-gate.py .scratch/r27-d18/diph-design-correct.yml` exited `1` for design-correct `tumhai`, while the paired gate-reading fixture exited `0` for `tumha`. Correct syllabification against the packet's declared diphthongs and design algorithm; retain this opposite-reading pair as the closure oracle. Do not count the earlier cluster-only change as closure. Evidence: `ledger.json`; `reports/round-27/argot/D18-mis-syllabified-form.md:147-201,212-226` and `reports/round-27/argot/D20-gap-closure-record.md:98-160,164-169`.

### R25-O20 argot battery / hold-oracle gap — non-ledger route to the R30 validation-battery owner

`tools/check-gate-battery.py:116-134` registers the structural gates and D4 typed-label/assembly adapters, but not the argot or law gate. The typed pipeline's `L3b-argot` leg and dedicated argot runner commands exist, so this is specifically a battery/hold-oracle integration gap, not absence of all argot tests. R30 should register argot in the standard battery or document a dedicated equivalent with an expected-verdict and negative-control oracle. Define what an argot expected-hold row means before adding `D4L-ARGOT-*` rows to `examples/culture-d4/expected-holds.json`. Evidence: `reports/round-29/defects/sweep-r25.md:16-20` and `reports/round-25/audit/o20-argot-leg-review.md:111-136,178-200` (measurements dated 2026-10-18).

## Register-law gate and packet

### `R28-LAW-FORCE-OVERMATCH` — route to the owner of `tools/gates/register-law-gate.py`

On 2026-10-18, `for f in .scratch/r29-routing-law-correct/{force-inverted,force-negated,consequence-empty,consequence-negative,speaker-bare,kind-unknown}.yml; do python3 tools/gates/register-law-gate.py "$f"; done` left the clean packet's four QREG dangling HOLDs unchanged for the first five mutations, with `force_failures=0` and `consequence_failures=0`; the unknown-kind control added `D4L-LAW-KIND`, producing five findings. Declare a machine-readable force vocabulary and validate value membership, class, polarity, and qualifiers as related fields. Closure requires positive-force and inversion/negation/fabricated-value controls that change the finding set appropriately; do not infer the vocabulary from the values being checked. See `ledger.json` and `reports/round-28/argot/D18-force-overmatch.md:69-136,211-258,285-296,385-440`.

### `R28-LAW-CONSEQUENCE-AND-SPEAKER-BLINDNESS` — route to the owner of `tools/gates/register-law-gate.py`

The same 2026-10-18 mutation batch left the four clean-packet QREG HOLDs unchanged for blank and polarity-inverted consequences and a tokenless bogus speaker class. Validate consequence presence and polarity, and explicitly declare and resolve speaker classes. Closure requires tokenless speaker and consequence-negation controls; keep a token-bearing speaker control only as a distinct case, not a substitute. Evidence: `ledger.json` and `reports/round-28/argot/D17-law-bypass.md:240-282,418-459,485-501,579-615`.

### `R28-LAW-REGISTER-ROW-ASSEMBLY-VALIDATION` — route to the owner of `tools/assemble-culture-d4.py`

The current assembler's `RECORD_FIELDS` at `tools/assemble-culture-d4.py:109-126` has no `register_law` field list. Add law-row validation and a mirror-based negative control that strips a law-row ID and refuses assembly; retain the lexicon missing-ID contrast and deterministic-assembly check. Evidence: `ledger.json` and `reports/round-28/scribe/x54-law-negatives-spotcheck.md:164-198`.

### `R28-LAW-DANGLING-DESIGN-ROW-REFERENCES` — route to the R30 register-law packet/design owner

On 2026-10-18, `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` emitted four `D4L-LAW-DANGLING` HOLDs for absent design rows `QREG-05` through `QREG-08`. Deliver the cited rows or correct those citations in an authorized successor. Preserve the gate's calibrated dangling-HOLD behavior: these clean-packet HOLDs are not themselves a gate regression. Evidence: `ledger.json`; `reports/round-28/argot/D17-law-bypass.md:89-99,579-602` and `reports/round-28/scribe/x58-d4-chain-cold-rerun.md:315-342`.

### `R28-LAW-GATE-ABSENT-FROM-REGRESSION-LABELS` — route to the R30 validation-runner / gate-battery owner

`tools/check-gate-battery.py:116-134` does not register `register-law-gate.py`. Add a standard-battery leg with the clean baseline explicitly expecting the four QREG dangling HOLDs, plus tamper-delta controls for force, consequence, speaker, and kind. Do not hide the expected clean HOLDs by omitting the gate or mark the calibrated four-HOLD baseline as a clean zero-finding run. R30 must also disposition the separate R29 six-versus-four calibration wording before claiming that the law gate's requested calibration is met. Evidence: `ledger.json` and `reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md:20-30,307-323`.

## Replay, runners, and sweep inventory

### `R28-FROZEN-REPLAY-USES-LIVE-TREE` — route to the owner of `tools/replay-frozen.py`

On 2026-10-18, `TMPDIR=/var/tmp/r28o39 python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv` was measured at 20:12Z and 20:26Z. At the first stamp two distinct pinned D4 inputs emitted one identical output digest and exited `2`; at the second their output digests diverged, but both still mismatched against live-tree assembly bytes. The two exit-`2` refusals were classified as `replay_mismatch/status=mismatch`, not `could-not-evaluate`. R30 closure requires an isolated mirror containing the full pinned read set and dependencies, distinct pinned-input controls that cannot collapse to one live-tree output, and a separate `could-not-evaluate` result for input-class refusals. Keep refusal and mismatch distinct; do not rerun old writers against filed artifacts in the live lane. Evidence: `ledger.json` and `reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md:104-220`.

### `R28-VALIDATION-CLAUSE-OMITS-FROZEN-MANIFEST-REPLAY` — route to the R30 validation-runner owner

On 2026-10-18, `python3 reports/round-28/run-validation.py --check` showed that the replay clause checks handoff/selftest labels but never enumerates frozen-manifest replay; the sweep recorded 11 of 12 manifest generations as nonzero. Make the runner enumerate the manifest generations it claims to cover and report refusal, mismatch, and reproduced verdicts separately. Closure requires a battery fixture in which a nonzero manifest replay makes the claimed all-replays clause fail. This is independent of the replay implementation route above. Evidence: `ledger.json` and `reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md:184-220,307-323`.

### `R28-ACCEPTANCE-CLONE-LIVE-SYNC` — route to the R30 acceptance-runner owner

On 2026-10-18, `python3 .scratch/r28-o33-o36-regression/f0-control.py` reproduced the effect of running `python3 reports/round-28/run-validation.py --check` inside an in-lane clone: three HEAD-probe files changed to live bytes. Prevent clone discovery from resolving back to the live lane, or disable sync in snapshot-only phases. Closure requires an isolated-clone run and before/after hashes for every probe file, all unchanged. Keep the existing exclusion until this control passes; do not test by running the historical sync against filed artifacts in the live lane. Evidence: `ledger.json` and `reports/round-28/regression.md:52-87,112-124`.

### `R28-CHECK-MODE-WRITES-RECEIPT` — route to the owners of the R27/R28 `run-gate-tests.py` runners

On 2026-10-18 at 17:13:19Z, `python3 reports/round-27/gate-tests/run-gate-tests.py --check` rewrote its filed receipt; the receipt was restored and hash-checked equal to HEAD. The R28 source inspection on 2026-10-18 confirmed the same unconditional receipt write in its runner. Make check mode read-only. Closure requires invoking it only in an isolated clone and comparing receipt hashes before and after; do not rerun either writer in the live lane. Evidence: `ledger.json` and `reports/round-28/regression.md:89-110,305-314`.

### `R28-SWEEP-LIVE-COUPLED-ADMISSION-AND-PIN-KEY-COVERAGE` — route to the R30 sweep-inventory owner

The dated R28 adjudication still found family-G admission coupled to live lineage and family-J discovery limited to a fixed pin-map vocabulary. Admit family-G hold sets by their own `packet_sha256` against recorded D4 lineage and report drift rather than silently skipping; discover family-J maps beyond a fixed set of key names. Closure requires a drifted-packet control and a map stored under an otherwise unseen key. This subsumes, but does not erase, R27-O05: on 2026-10-18 `python3 reports/round-27/audit/o37-sweep-inventory-audit.py` was recorded first at 26 surfaces / 9 swept / 17 missed and later at 29 surfaces / 24 missed; those are distinct historical snapshots, not a current defect count. R27-O06's replay red is likewise snapshot-specific and is not a second live failure: on 2026-10-18 at 19:26Z `python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` reported `2 mismatch, 0 reproduced`, while the later R27 receipt differed. Route any future snapshot-stability control through the replay owner; do not rewrite either R27 artifact. Evidence: `ledger.json`; the R27 snapshot findings are summarized at `reports/round-29/defects/sweep-r27.md:10-24`, with R28 sources at `reports/round-28/audit/o38-sweep-inventory-adjudication.md:87-145,147-170,199-223`.

## Other non-ledger routes and bounded historical dispositions

### R26-O03 — snapshot stability; historical, not a current red

On 2026-10-18, `python3 tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-26/remainders/v3-baseline-r26/expected.json` was green at 18:16Z, then red at 18:19:16Z with `E2E-DIGEST: 6 read-set file(s) changed` after a concurrent D4 write at 18:18:32Z (`reports/round-29/defects/sweep-r26.md:10-14`). Route a future snapshot-stability control to the R30 handoff/validation owner: freeze or hash the entire read set and reject an invalidated result. Do not repair the old row or present the later filed green receipt as proof that no in-flight invalidation occurred.

### R26-O04 and `R26-R4-CHECKER-UNEVALUATED` — claim language and valid verdicts

The R26 claim says “r4 checker green,” while the final runner marks r4 superseded/not graded and requires the r5 pin-repoint checker (`reports/round-29/defects/sweep-r26.md:16-24`; `ledger.json`). Route future claim wording to the R30 R26-claim/acceptance owner: name the r5 successor and state r4's supersession, rather than revive the old checker. Retain `R26-R4-CHECKER-UNEVALUATED` as a historical runner-design observation: a required check is satisfied only by a valid passed verdict, never a receipt without one. Do not rewrite the R26 receipt or resurrect the r4 checker against r5 pins.

### R27-O05/O06 and R28-O07/O08 — distinct scope and replay lessons

R27-O05 is carried by `R28-SWEEP-LIVE-COUPLED-ADMISSION-AND-PIN-KEY-COVERAGE` above; its old inventory counts are not a current inventory result. R27-O06 is a snapshot-specific replay finding, not a claim that the later acceptance receipt is red. R28-O07 and R28-O08 remain separate live routes above: the runner omission (`R28-VALIDATION-CLAUSE-OMITS-FROZEN-MANIFEST-REPLAY`) is distinct from the replay tool reading the live tree (`R28-FROZEN-REPLAY-USES-LIVE-TREE`).

### X63-F2 — route to the R30 corpus-entry author for `register-lexicon-ceilings.md`

X63-F2 is an authoring defect, not a sibling landing: `sound-symbolism.md:106` already contained “which semantic fields” at baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`. The 2026-10-18 audit's `git grep -n -i "which semantic fields" 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede -- corpus/knowledge/linguistics/sound-symbolism.md` records that pre-existing hit. In a new authorized entry, remove the false absence sweep or qualify it to say the phrase occurs in `sound-symbolism.md` in the ideophone sense. Do not edit the filed R28 entry. X63-F1, X63-F3, and X63-F4 are classified in the same audit as sibling-landings, not authoring defects; preserve those classifications instead of routing them for repair. Evidence: `reports/round-28/audit/x63-entry-source-resolvability.md:133-179`.

### Fresh v3 renderer claim drift — route to the R30 claims-map / handoff-renderer owner

On 2026-10-18, `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze "$TMPDIR/r29-fresh-v3-recheck"` exited `0` with packet hash `a20ae059aa7cac9e28345d1a80a4dae3fa302117e26b5b1405f05b38d12f0001`. The fresh render's D4-CL05/06 and OQ-V3-05 still state the prior values: `74` labels, `16` findings with `15` hold-or-fail, `15` holds plus `1` note, and `13` unresolved rank items. On 2026-10-18, `python3 -c 'import json; p=json.load(open("examples/culture-d4/typed-labels.d4.yml")); e=json.load(open("examples/culture-d4/expected-holds.json")); c=p["coverage"]; print("labels=%d findings_total=%d findings_hold_or_fail=%d rank_unresolved=%d" % (c["typed_labels"], c["findings_total"], c["findings_hold_or_fail"], c["rank_rules_unresolved_items"])); print("expected=%s" % e["counts"])'` returned `labels=82 findings_total=12 findings_hold_or_fail=12 rank_unresolved=0` and `expected={'hold': 12, 'note': 0, 'fail': 0}`. The projection check `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` exited `0` on 2026-10-18. Refresh the claims-map source and renderer from measured projection fields; add a regression that compares rendered claims and unresolved-question text to the live projection. Keep this separate from the already-corrected append-only R25/R26 handoff revisions. Sources: `reports/round-20/handoff/claims-map.md`, `tools/exercise-handoff-e2e.py`, and the 2026-10-18 fresh render in `.scratch/r29-fresh-v3-recheck/`.

## Historical entries not reopened

The R29 ledger's `closed` entries remain bounded closures: `R25-TYPED-PIPELINE-MANUFACTURED-RED`, `R25-TRANSIENT-GATE-SELFTEST-REDS`, and `R25-ARGOT-REVERSE-ENGINE-LIMIT`. Its `superseded` entries remain historical: `R25-V3-STALE-PROSE-SUPERSESSION` was superseded by append-only successors, and `R25-FROZEN-GATE-PIN-UNCOMMITTED` by later committed generations. The ledger census command and date are recorded above. Do not revive intermediate reds or rewrite filed receipts. The `R26-R4-CHECKER-UNEVALUATED` observation is retained only as the valid-verdict lesson above; the r4 checker itself is superseded.

FILES: reports/round-29/defects/routed.md | SUMMARY: routes every open R25–R28 ledger item and the remaining audit findings to R30 with named owners, scoped evidence, and closure controls.