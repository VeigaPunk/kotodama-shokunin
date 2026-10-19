# R04 — non-author review of the O freshness gate: real probes, no instrument

- Seat: `R04` | role reviewer (non-author) | claim **O** | round 47, loop 2
- Out path: `reports/round-47/review/R04-gate.md` (this seat's only write)
- Review cut: 2026-10-19T18:30Z (UTC); HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`
- Mission (`reports/round-47/targets.json`, id `R04`): "does the tool genuinely implement the R01-43-12 contract (typed probes, baseline-eval, polarity, exit codes) or just look like it? Judge operability depth."
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.
- Boundary: no filed byte edited, no corpus staging, no `reports/round-*/run-validation.py`, no git commit/push/install/network. My assembly and drivers live only under `.scratch/r04/`. I did not author any O fragment; O01–O06, O09, O10, O12, O13 were read as evidence.
- Cut integrity: re-checked against the full `reports/round-47/` listing at 18:32Z (the refire wave was in flight). `op/O07`, `O08`, `O11`, `O14`, `O15`, `W01`, `V02` and `tools/harness/claims-freshness.py` were still absent; `O01–O06`, `O09`, `O10`, `O12`, `O13` are the whole O set in scope. New non-O fragments (A03, Ca07, C02, C12, X01, R03, R05, S01) do not assert a landed tool or a successful assembly.

## 0. Verdict

**The measurement layer is genuine; the instrument is not.** The three fenced parts (O01 core, O02 probe registry, O03 decision algebra) each do real work and their unit suites are green where they exist. But the deliverable `tools/harness/claims-freshness.py` is absent, and the parts **do not compose** under the assembly contract O01 states. Two of the four required demonstrations cannot even be parsed by the implemented registry, and the one executable assembly path produces a **false green**.

| question | measured answer |
|---|---|
| Do the typed probes exist and measure? | **Yes.** 7 kinds, 43/43 registry selftest; count 223, path absent/present, sha256, topic ownership all measured correctly at `7ceff59` (§3.1). |
| Is evaluation baseline-only (never worktree)? | **Yes at the core.** `Baseline` has only commit inputs; measured 223 at `7ceff59`; the r43 Ca artifact is absent there (§3.1). No CLI exists to expose it. |
| Is polarity declared, not inferred? | **Yes at the validator.** Missing/mistyped `expect` is rejected; boolean vs integer is type-strict (`O02:580,602`). |
| Does a contradiction yield STALE? | **Yes in O03, no across the seam.** O02 emits `mismatch`; O03 recognises only `CONTRADICTED`, so its own documented adapter downgrades a contradiction to `could-not-evaluate` / exit 3. A 3-line remap fixes it (§3.3). |
| Does the durable tool exist with a green selftest? | **No.** `ls` and the claim's own counting command both fail; plain concatenation is a `SyntaxError`; after the minimal syntax fix, **every** invocation prints the registry selftest and exits 0 without reading claims (§3.2). |
| Do the filed demos run through these parts? | **No.** O05's r43 overlay: 5 of 6 checks rejected as malformed. O06's negative control: 9 of 9 rejected. There is no `--checks` overlay loader in any part (§3.4). |
| Could the machinery produce the required verdicts? | **Yes, if checks are rewritten natively and a status adapter is added.** Measured O STALE, C STALE, Ca FRESH, exit 1 (§3.5). That is capability, not delivery. |

**Axis judgment: operability is not improved by this round at this cut.** The defect R01-43-12 remains live. Nothing landed, so no axis is harmed; but an integrator who applies "plain concatenation" would land a tool that exits 0 on stale claims — strictly worse than no tool. The O claim's thresholds (`reports/round-47/claims.json:47`) are unmet on every clause that requires a durable artifact.

This is not theater in the sense of fabricated measurement: the probes really measure and O02's renamed-tool control (S7) really finds behavior by behavior. It is **unintegrated parts reported through three different scratch evaluators** (O05's K03 evaluator, O06's compat harnesses and O08 oracle, O03's transcribed `ClauseResult` fixtures). O12 said the chain was open at 18:10Z; this review confirms that at the seam level with measured runs rather than by reading the fragments.

## 1. What claim O requires

From `reports/round-47/claims.json:37-47`:

- durable `tools/harness/claims-freshness.py`;
- re-derive each `before` at `baseline_commit` (git plumbing, not the worktree);
- typed per-clause probes with declared polarity, from the closed set named at `:39`;
- STALE when any declared clause contradicts; non-zero exit on stale;
- green selftest; r43 O+C stale / Ca fresh; a fresh claim not flagged; anti-theater mutation still flags; a filed demonstration at `reports/round-47/calib/`; `could-not-evaluate != green`.

The defect is R01-43-12 (`reports/round-43/review/R01-review.md:400`). The six-part contract is `reports/round-44/review/R01-review.md:243-250`; the normative overlay schema is K03 `reports/round-47/scout/K03-gate-spec.md:130-152`.

## 2. Method

I extracted the three fenced bodies byte-for-byte and pinned them:

| part | extraction | lines | sha256 | matches published |
|---|---|---|---|---|
| O01 core | `reports/round-47/op/O01-tool-core.md:161-793` | 633 | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` | yes (`O01:14`) |
| O02 registry | `reports/round-47/op/O02-probe-registry.md:255-1221` | 967 | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` | yes (`O02:1224`) |
| O03 verdict | `reports/round-47/op/O03-verdict-contract.md:87-573` | 487 | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` | yes (`O03:84`) |

Drivers under `.scratch/r04/`: `seam_test.py` (schema acceptance), `probe_measure*.py` (native probes at `7ceff59`), `verdict_seam.py` (O02→O03), `o04_dropin.py` (O04 seam), `native_r43.py` (native r43 check set). They import the parts read-only and never write the repo. All reads of baseline bytes go through O01's `Baseline` (git plumbing).

## 3. Measurements

### 3.1 The measurement layer works

`python3 -B .scratch/r04/p2.py`:

```
PROBE-REGISTRY SELFTEST: 43/43
exit=0
```

Native probes through O01's `Baseline(".", "7ceff59")`, 3229 tracked files:

```
count_eq   corpus/knowledge/*/*.md                    expect=223  measured=223   holds
path_absent tools/harness/basename-couples-resolver.py expect=True measured=True  holds
path_present tools/harness/couples-reference-extractor.py expect=True measured=True holds
sha256_eq  tools/harness/couples-reference-extractor.py expect=d8d23a26… measured=d8d23a26… holds
topic_owner_absent myth-symbol:lithic expect=False measured=False holds
  1 owner(s): corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
grep_absent  xyzzy-no-such-token expect=True measured=True holds
```

The capability probe also genuinely executes baseline blobs, not literal names: with a fixture containing the live wrapped field, the extractor passes and is found (`measured=True`, `1/1 candidate(s) pass`); with an incomplete fixture it fails (`measured=False`). That is real behavioral measurement, and O02's S7 control (`renamed tool`) is a credible unit-level anti-theater test.

**One dangerous edge, measured.** A candidate that *executes and exits non-zero* is treated as "no capability" (`O02:687`, `O02:819`, `O02:877`; only timeouts/exec errors reach `could-not-evaluate`). With an incomplete fixture the extractor crashed at its live-corpus read and the probe returned measured `False`. For an absence claim (`expect:false`), that measured `False` **holds** — a present capability would be laundered as absent by an author's incomplete fixture. The r43 O check is exactly an absence claim. This is not exercised by O02's selftest, whose candidates exit cleanly.

### 3.2 Assembly fails, then yields a false green

O01 states the contract: "The assembly is plain concatenation; nothing in part 2/3 needs to edit these bytes" (`O01:23`). Measured, with `cat p1 p2 p3`:

```
$ python3 -B .scratch/r04/assembled.py --selftest
  File ".../assembled.py", line 694
    from __future__ import annotations
SyntaxError: from __future__ imports must occur at the beginning of the file
exit=1
```

Both O02 and O03 carry `from __future__ import annotations` mid-file (`O02:315`, which lands at assembled line 694; `O03:108`). After removing the duplicate future imports — the minimal syntax fix — the result is worse:

```
$ python3 -B .scratch/r04/assembled3.py --selftest   → PROBE-REGISTRY SELFTEST: 43/43; exit 0
$ python3 -B .scratch/r04/assembled3.py --claims reports/round-43/claims.json
                                                      → PROBE-REGISTRY SELFTEST: 43/43; exit 0
$ python3 -B .scratch/r04/assembled3.py --help        → PROBE-REGISTRY SELFTEST: 43/43; exit 0
```

Cause: O02 ends with `if __name__ == "__main__": sys.exit(selftest_registry())` (`O02:1220-1221`), and no part defines `main()` or `argparse` (grep: zero hits in all three). O01's own limits concede "No CLI yet" (`O01:798`) and O03 says the main "should look like this" (`O03:683`) — a sketch, not a deliverable. The assembled file ignores `--claims` entirely and exits 0: the claim's own counting command would report success while evaluating nothing. `could-not-evaluate != green` is violated by the only executable assembly.

The claim's first counting command, at the durable path:

```
$ python3 tools/harness/claims-freshness.py --selftest
python3: can't open file '.../tools/harness/claims-freshness.py': [Errno 2] No such file or directory
exit=2
```

### 3.3 The O02→O03 status vocabulary does not match

O02 emits `"holds" | "mismatch" | "could-not-evaluate"` (`O02:687`). O03's clause statuses are `("HOLDS", "CONTRADICTED", "NOT_EVALUATED")` (`O03:138`), and anything else is downgraded (`O03:184`). Feeding a real O02 mismatch through O03's documented adapter (`O03:685-701`):

```
p2 result: {'probe_kind': 'capability_present', 'expect': False, 'measured': True, 'status': 'mismatch'}
judge_claim(raw p2 result) -> could-not-evaluate | counts {'holds': 0, 'contradicted': 0, 'not_evaluated': 1}
  not_evaluated: ["evaluator-contract-violation: status 'MISMATCH' is not one of HOLDS/CONTRADICTED/NOT_EVALUATED"]
judge_claim(remapped mismatch→CONTRADICTED) -> stale
build_report(raw) exit_code = 3, run_verdict = could-not-evaluate
```

A one-line remap is enough, but it is not in any fragment, and O03's adapter section says to pass results straight through. As filed, the gate would answer `could-not-evaluate`/exit 3 for the r43 O stale premise — non-zero, but the wrong state, and a false acquittal of the claim's "flags O STALE" threshold.

### 3.4 The filed demos are malformed under the implemented registry

**O05 r43 overlay** (`reports/round-47/op/O05-r43-demo.md:127-152`), run through O02's `validate_check` with the r43 `before` strings:

| check | result |
|---|---|
| O[0] capability_present `{capability, scope}` | `CheckError: capability_present target has unknown key(s): capability, scope` |
| O[1] same | rejected, same reason |
| C[0] count_eq `expect: true` | `CheckError: count_eq expect must be a JSON integer, got True` |
| C[1] topic_owner_absent `{topics, partition, fields}` | `CheckError: target has unknown key(s): partition, topics` |
| C[2] count_eq `expect: true` | rejected, same reason |
| Ca[0] path_absent | **accepted** |

5 of 6 rejected. This is not a fixture typo: O05 follows the K03 overlay schema, where `expect` is a JSON boolean and the value lives in `target` (`K03:147`), while O02's in-file schema puts the typed value in `expect` (`O02:602`). Both are defensible; they are not the same contract, and the demos were run on yet another evaluator (`O05:261` says explicitly "NOT the durable tool"). O05 also requires a `--checks` overlay path (`O05:253`); grep for `overlay|claims_sha256|--checks` finds no loader in O01/O02/O03.

**O06 negative control** (`reports/round-47/op/O06-negative-control.md:79-178`): 9 of 9 checks rejected — `path_absent/count_eq/topic_owner_absent target must be an object` (O06 uses `target` strings and `path::regex`), plus three clauses that are not verbatim substrings of the `before` they are bound to. O06 itself records that it ran against the r44 prototype and O08's oracle, "neither reads the canonical fixture's r47 vocabulary" (`O06:323-326`). So the negative control, as filed, cannot be run by the tool the round is building.

Three check dialects are in play: K03/O05 (v1 overlay, boolean `expect`), O02 (in-file `before_checks`, typed `expect`), O06 (string targets and `path::regex`). No part implements K03's overlay or its named `couples_census` capability; O02 implements only the behavioral form. The flagship r43 O demo depends on the one form that does not exist in code.

### 3.5 O04's selftest is not a drop-in

O04's seam (`reports/round-47/op/O04-selftest.md:190-194`) requires `CAPABILITIES`, `SchemaError`, `FixtureBaseline`, `evaluate_claim`, and a different `evaluate_check` contract. Against the actual parts:

```
CAPABILITIES: MISSING
SchemaError: MISSING
FixtureBaseline: MISSING
evaluate_claim: MISSING
evaluate_check: present (different signature/return)
selftest raised NameError : name 'evaluate_claim' is not defined
```

The 46-control suite has never run against O01–O03; its green run is against `.scratch/o04/ref_gate.py` (`O04:499-506`), a different implementation. O04 also says "8 kinds" while the claim and O02 have 7 (`O04:190` vs `O02` S10b) — a minor but real count inconsistency.

### 3.6 What the parts *can* do when wired natively

To separate "broken machinery" from "missing integration", I wrote r43 checks in O02's native schema and added the 3-line status map:

```
O stale  {'holds': 0, 'contradicted': 1, 'not_evaluated': 0}  [('capability_present', True)]
C stale  {'holds': 2, 'contradicted': 1, 'not_evaluated': 0}  [('topic_owner_absent', False)]
Ca fresh {'holds': 1, 'contradicted': 0, 'not_evaluated': 0}
report verdict/exit: stale 1
```

This is the required positive regression — reached with the real probes at the real baseline, not with transcribed values. The missing pieces are mechanical: a CLI, an overlay loader or fixture rewrite, a status map, and a decision about the capability schema. The parts are worth integrating; the claim is not met until they are.

## 4. Per-contract disposition

| R01-43-12 element | status | evidence |
|---|---|---|
| typed per-clause probes | **implemented** | 7 kinds, 43/43 (`O02` selftest); native runs §3.1 |
| baseline-only evaluation | **implemented in core, unexposed** | `Baseline` commit-only; 223 at `7ceff59`; no CLI |
| declared polarity | **implemented, but two encodings** | `O02:580,602`; K03 `:147` vs O02 typed `expect`; O05 vs O06 disagree |
| contradiction ⇒ STALE | **decision layer yes, seam no** | §3.3: raw = CNE/exit 3; remap = stale/exit 1 |
| exit non-zero on stale | **algebra yes, binary no** | `O03` exit map; assembled binary exits 0 on `--claims` |
| durable tool + green selftest | **absent** | `ls`; `python3 tools/harness/…` exit 2 |
| r43 O+C stale / Ca fresh | **not as filed; reachable natively** | §3.4, §3.6 |
| negative control not flagged | **not as filed** | 9/9 rejected §3.4 |
| anti-theater mutation | **unit-level only; O07 absent** | S7 renamed tool passes; fixture-incompleteness false-negative §3.1 |
| filed demonstration at `calib/` | **absent** | file listing |
| could-not-evaluate ≠ green | **algebra yes; assembly violates** | §3.2: any argument exits 0 |

## 5. Defects the integrator must fix before applying

D1 (blocker) — remove duplicate `from __future__ import annotations` from O02/O03 or place one at the head of the assembled file. Plain concatenation does not parse.
D2 (blocker) — remove O02's `__main__` guard (`O02:1220-1221`) and write the CLI: `--claims`, `--checks`, `--json`, `--selftest`, `--no-exec`; exit codes per O03.
D3 (blocker) — add the status map `holds→HOLDS`, `mismatch→CONTRADICTED`, `could-not-evaluate→NOT_EVALUATED` at the seam.
D4 (blocker) — choose one check schema. If K03/O05: implement the overlay loader (`claims_sha256`, `baseline_commit` equality, unknown ids malformed) and a named/AST capability registry. If O02: rewrite O05 and O06 fixtures into native typed checks; they are currently unusable and must not be filed as demos.
D5 (high) — O04's control set must be adapted to the actual symbols (`FixtureBaseline`, `evaluate_claim`, `evaluate_check` return type) or the suite re-authored; its 46/46 claim is not about this code.
D6 (high) — capability probe: distinguish "candidate ran and failed its behavioral contract" from "no candidate". For absence claims an incomplete fixture currently yields a false hold. Either treat any candidate crash as `could-not-evaluate`, or require the fixture to be derived from baseline bytes and document it.
D7 (medium) — reconcile the probe-kind count (claim/K03/O02: 7; O04: 8) and the header-field spelling (`O02` uses `h1`, K03/O05 use `H1`).
D8 (medium) — O02's `_result` has no `reason` for `mismatch`; O03 expects one only for NOT_EVALUATED, so this is cosmetic, but the human renderer should print measured vs expected for each contradiction (it does when rows are remapped).

## 6. What I could not evaluate

- Whether O01's core passes its own scratch suite: I did not run `.scratch/o01/check_core.py`; no durable transcript is filed. The core behaved correctly on every path I exercised.
- Whether O03's 33/33 suite corresponds to the fenced bytes: I ran the block's functions directly, not the scratch driver; the digest matches, so the bytes are the tested ones.
- The actual O05/O06 evaluator runs: I did not re-run `.scratch/o05/*` or `.scratch/o06/*`; I measured their fixtures against the registry, which is the integration question. Their own transcripts remain their evidence, and both label themselves non-durable.
- O07 (anti-theater artifact), O08, O11, O14, O15, W01, V02 are absent at this cut; their questions are unowned, not passed.

## 7. Handoff

**To the integrator:** do not apply the concatenation as-is. The claim's `after_required` is unmet until D1–D4 are fixed and the six commands of `O12:6.3` run against `tools/harness/claims-freshness.py`. The strongest existing assets are O02's registry (43/43, genuinely behavioral), O01's commit-only `Baseline`, O03's decision algebra (33/33, correct exit semantics), and O05/O06's expected verdict tables — the fixtures need translation, not the expectations.

**To O08/V02:** the two checks that discriminate a real gate from a green-looking one are (a) `--claims reports/round-43/claims.json --checks <overlay>` must print O STALE, C STALE, Ca FRESH and exit 1 (not 0, not 3), and (b) `--claims` on a claim with no checks must exit 3, never 0. The assembled binary as drafted fails both by exiting 0 on the registry selftest.

**To the scribe/parent:** operability is **not improved** this round. Record the O chain as `could-not-evaluate` for the durable link; do not credit the reference-evaluator runs as the deliverable. The Ca row `r43-stale-premises` must stay `routed-with-owner` until the tool passes the two checks above. No axis is harmed because nothing landed; the latent risk is applying the false-green assembly.

## Appendix — commands run (abridged)

```
python3 -B .scratch/r04/p2.py                              # 43/43, exit 0
python3 -B .scratch/r04/assembled.py --selftest            # SyntaxError, exit 1
python3 -B .scratch/r04/assembled3.py --claims …           # 43/43, exit 0 (false green)
python3 -B .scratch/r04/seam_test.py                       # O05 5/6 rejected; O06 9/9 rejected
python3 -B .scratch/r04/verdict_seam.py                    # raw CNE/exit 3; remap STALE
python3 -B .scratch/r04/o04_dropin.py                      # NameError: evaluate_claim
python3 -B .scratch/r04/probe_measure2.py                  # count/path/sha/topic correct
python3 -B .scratch/r04/native_r43.py                      # O stale, C stale, Ca fresh, exit 1
python3 tools/harness/claims-freshness.py --selftest       # No such file, exit 2
sha256sum reports/round-47/op/O01-tool-core.md …           # fragment digests (see §2)
```

No filed byte edited; `git status --porcelain` shows only `?? reports/round-46/review/` and `?? reports/round-47/`.
