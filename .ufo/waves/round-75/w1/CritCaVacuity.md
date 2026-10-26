# CritCaVacuity — round 75, Ca draft review

## Findings

### F1 — L75-08 is unobservable from the specified lane-base clone

**Evidence.** I cloned the lane repo, checked out base `f556d1049fe651d3d63975600b13acd9fb686f15`, and ran the exact `observe_cmd`. `git cat-file -e 3a7401609325341eb3fe0efd42d0eec29d06be3c` in that clone fails; the observation prints `fatal: unable to parse object` and exits 128. The same fleet-pin revision is not a lane-repo object. L75-08 also gives `stated_at` as an absolute path under the fleet root, not a lane-base path. The claim's LEDGER requires each observation to be observable in the base clone and says `stated_text` is found at `stated_at` in the BASE tree.

**Fix.** Make this an explicitly fleet-scoped pair: provide a pinned fleet path/revision/hash and run both observation and statement lookup against that pinned fleet repository (or materialize the fleet pin into a separate read-only clone). Do not treat the lane clone as containing fleet objects. Bind this exception in the frozen grammar and counter.

### F2 — L75-07 contradicts the DRAFT's ban on absence-observation pairs

**Evidence.** At base, the exact command `git grep -c 're-pointed read path' f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/QUALITY.md` returns no output, exit 1. Round-74's `run_observe` normalizes this exact `git grep -c` zero-match shape to token `0`, and its LEDGER rejects a zero base count when `expected_after` is positive. L75-07 expects `1`; its own `why` says the text is absent at base and appended later. This directly conflicts with both the ledger status (“an absence-observation pair is never kept”) and Ca's no-absence LEDGER rule. With the supplied `parse` `:([0-9]+)$`, the normalized zero token also fails to parse, so the pair is unobservable under the round-74 parser.

**Fix.** Drop/replace L75-07 with a genuinely observable, nonzero-at-base measure that can be corrected without an absence-to-presence transition; otherwise explicitly revise the no-absence rule and define a non-circular, parseable zero-count grammar. Do not merely waive this pair by id.

### F3 — several “red” pairs compare unlike quantities, and two are unobservable under the inherited parser

**Evidence.** I ran the draft commands at base. L75-04 observes one `FOOTER_RE.search` occurrence; L75-05 and L75-06 each observe a grep count of 1 for the filed sentence; their `stated_parse` extracts prose, not that count. Thus their inequality is guaranteed by token type (prose versus integer), not evidence that the stated assertion is false. L75-10's `ls` output contains 44 `.md` names, but its parse `\.md$` has no capture group and extracts only `.md` under round-74 `observed_token` semantics; it does not observe 44. It also lacks the revision operand required by the ANNOTATE rule that “count pairs measure at the pinned base revision.” L75-11's exact grep has zero matches; with its `:([0-9]+)$` parse it likewise cannot parse the round-74 normalized zero token. L75-09 is a meaningful mismatch: the committed receipt line ends `min-pairs gate FAI`, while `stated_text` says `...FAIL`.

**Fix.** Freeze a typed pair contract: each statement token and observation must represent the same quantity/domain, and the counter must reject structurally mismatched types rather than count any inequality as “red.” For count observations, use a parse that captures the count including zero, and pin the relevant revision. Replace L75-04/05/06 with observations that establish the asserted false proposition (not a count of the assertion's own wording); fix or replace L75-10/11 accordingly. Keep L75-09's explicit truncated-token comparison.

### F4 — REPAIR's observation revision and expected value are not coherently specified for the combined tree

**Evidence.** L75-01's exact base observation returns 808, and claim C's frozen row set adds eight `S885`–`S892` rows. Therefore the same `^. S[0-9]{3}` measure at a tree containing both landings is 816, not L75-01's `expected_after: "808"`. Yet L75-07 can only reach its stated expected value 1 if its observation sees the newly appended QUALITY text; its argv pins the old base revision, where the count remains zero. The REPAIR sentence says “truth observed in a clone at <lands>” but does not say whether the counter substitutes `<lands>` for base revisions; the ledger status/ANNOTATE rule separately says observations are pinned to base. COMBINED reruns Ca at the both-landed tip, so this ambiguity is material, not cosmetic.

**Fix.** Specify separate, explicit base-observation and lands-observation operands/semantics in the pair schema and counter. For a combined grading tree, set L75-01's repaired statement/expected observation to the actual combined registry total (816, given the eight frozen rows), and ensure the repair is evaluated at that same both-landed tree. Replace L75-07 as in F2. Bind `expected_after` to the parsed lands observation and state this in REPAIR and COMBINED.

### F5 — ANNOTATE can accept a token-substring re-derivation, so NOSTUB is not substantive evidence

**Evidence.** The Ca claim says the re-derivation “returns the observed token.” In the round-74 reference implementation, `leg_annotate` applies `token_in(out_text, obs)`, i.e. boundary-matched containment in raw command output, rather than parsing and requiring equality to the observed token. `leg_nostub` only requires the row to contain id, old token, new token, and the command; it rejects a small placeholder list but does not validate that the command computes the same typed measure. A permitted `cat`/`grep` command can print a file containing the expected token as incidental text alongside unrelated output and satisfy containment without returning that token as the command's result. This matters especially for pairs whose “observed” token is a count but whose stated token is prose.

**Fix.** Parse re-derivation output with the pair's declared result parser and require exact token equality; require old token != new token; bind the re-derivation to the same pinned source/revision as the observation. Reject extra/ambiguous matches rather than accepting containment.

### F6 — R1 exemption must compare changed cell positions, not merely a line's changed span

**Counterexample bytes.** Consider an 11-cell SOURCES row (field labels illustrative):

`| S123 | https://x.example | title | author | 2020 | mined | 2026-10-20 | teaches: foo | used-by: a.md | note | tag |`

A landing changes it to:

`| S123 | https://x.example | title | author | 2020 | mined | 2026-10-20 | teaches: foo; cite new finding | used-by: a.md, b.md | note | tag |`

Adding `b.md` in `used-by` can be legitimate under the stated rule-2 exemption, but changing `teaches` is not. A line-level implementation that sees an exempt used-by change and exempts the whole changed row would pass this substantive teaches edit. The DRAFT requires the exemption to apply only to rule-2 cells, but does not specify the positional cell-diff algorithm or exact shape validation needed to enforce that boundary.

**Fix.** Parse base and landing row into exactly 11 positional cells, validate the same row identity and delimiter/escape shape, compute every changed cell index, and allow the exemption only if the complete changed-index set is a subset of `{status, recheck, used-by}`. Reject a malformed or ambiguous row; do not grant exemption because any one changed span intersects an allowed cell. The committed R1EXEMPT negative fixture should include simultaneous teaches + used-by edits, not only a teaches-only edit.

### F7 — the sweep receipts mentioned for L75-04 are not revision-bound by a named leg

**Evidence.** L75-04's `why` says the repair lands with `sweep-red-before.txt` and `sweep-green-after.txt`, and that the counter reruns them. None of the twelve listed legs names or checks those receipts. STAMP binds the counter receipt at `<lands>`; RECEIPTS binds the round-74 accept-ca receipt. Neither text binds the sweep receipts to a materialized tree containing the repaired sweep code. Consequently the DRAFT's listed criteria do not prevent a green-after receipt produced from some other revision/tree from being committed as evidence.

**Fix.** Add a leg that materializes exact base and lands revisions, reruns the sweep at each, checks expected exit/output, and binds each receipt's stamped/evaluated/measured revision and tree hash to those exact trees. Or remove the receipt assertion from L75-04's rationale and rely solely on a counter-executed lands check explicitly specified in REPAIR.

### F8 — COMBINED is not inherently circular, but its same-tree/revision contract needs the F4 correction

**Evidence.** As written, COMBINED asks the Ca counter to run at the lane tip with both landings; it does not require recursively invoking the C counter, so it can be independently checkable. However, it rechecks REPAIR at a tree containing C's eight appended rows, which changes L75-01's observed count from 808 to 816. That creates the concrete incompatibility in F4 unless the statement and expected measure are defined for the combined tree. The claim does not specify whether the combined receipt is produced by one counter pass at the combined tip or by grading separate tips and then circularly using one result as input to the other.

**Fix.** Define one materialized combined revision, run `accept-ca-75` exactly once against it, and bind `measures-ca-head.txt` stamped/evaluated/measured/tree headers to that revision. Keep C acceptance independent; do not use C's PASS as Ca's input. Resolve the L75-01 measure at that same tip as in F4.

## Base command results

Commands ran in my disposable clone checked out at the frozen base. Strict result: L75-01 (808 vs stated 412), L75-02 (32 vs 30), L75-03 (40 vs 36), L75-04 (1 vs prose), L75-05 (1 vs prose), L75-06 (1 vs prose), L75-09 (`FAI` vs `FAIL`), and L75-10 (44 `.md` filenames vs stated 43) produce unequal values only under a permissive/mismatched-token interpretation; L75-07 and L75-11 produce zero matches, but their `:([0-9]+)$` parse misses the normalized zero under the round-74 counter; L75-08 exits 128 because the pinned fleet commit is absent from the lane clone. Thus I cannot certify “every pair red and observable”: at least L75-07, L75-08, and L75-11 are unobservable under the referenced parser, and L75-04/05/06/10 are not meaningful same-domain comparisons. The round-75 counter does not yet exist in the lane worktree, so these are findings against the DRAFT and the referenced round-74 implementation, not a claim that an unseen round-75 implementation has been run.

## Evidence provenance

- Draft files read: `reports/round-75/claims.json`, `reports/round-75/ledger.json`.
- Reference: `reports/round-74/accept-ca.py`; mutation history: `.ufo/waves/round-74/w2/MutLedgerCa.md`.
- Base clone under `/fast/scratch/hyaku/kotodama-r75/CritCaVacuity/`; no lane/fleet files or git state modified. No tools installed.
