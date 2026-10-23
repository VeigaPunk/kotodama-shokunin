# CriticClaims — round 62, wave 1

Review of the declaration at `f0173481047a93c46798f90b68d71d4f169d2642`. Advisory findings only: no admission decision, candidate edits, counter execution, or alternative runtime invocation.

## Axes and evidence boundary

- **Depth:** source-scoped factual detail, not a lexical score or registry-row count.
- **Operability:** a newly runnable row re-opener and its stated behavior.
- **Calibration:** declared scope, measured evidence, lowest-axis reasoning, and honest distinctions between a leg survivor and a whole-predicate survivor.
- **Coverage, freshness, adjacency:** boundary checks; no expansion, resumed freshness claim, or cross-domain ownership follows from these predicates.

I read `claims.json` and the round-61 closure §7 first, then the frozen counters, manifest, relevant fleet/canonical rules, source rows, and prior closure precedents. Bounded `sha256sum` matched the supplied counters:

```text
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
```

No control was run by this seat; consequently this report claims neither CONTROL-MET nor a new PASS receipt. Static predicted behavior below is marked **[INFERENCE]**. An existing peer receipt is explicitly attributed, not presented as my run.

## Ranked findings and smallest pre-data corrections

### 1. High — D can satisfy its wording legs while reversing the source's meaning

**Counterexample.** In an otherwise passing D fixture, replace only lines 74 and 75 with:

```text
- A caption denies heels originated in Western Asia for horseback riding. (S665)
- BBC denies the earliest evidence we have of someone wearing heels is a Persian bowl. (S666)
```

These assert denials the quotes do not carry. **[INFERENCE, hand-derived, not executed]** For line 74 the content count is 8, shared words/LCS are 5, required LCS is 4, and the longest copied run is 4 words. For line 75 the corresponding values are 8, 7, 4, and 10. Each retains the required id and caption/hedge token, avoids defect marks and the banned old wording, and changes no row, line count, new-id set, or other acceptance input. Thus these substitutions preserve a passing whole predicate conditional on an otherwise passing fixture, without performing those two semantic repairs.

**Evidence.** `accept-d.py:175-186,247-263` checks tokens and lexical overlap/order, not entailment; `:49-50` expressly relegates support beyond shared words to review-only. Fixed row quotes are in `corpus/SOURCES.md:620-621`.

There is also exercised local evidence: `.ufo/waves/round-62/w1/CtlDJunkTokens.md:39-48,149-170` records `five-content-minimum`, including `- caption heel European invention Western. (S665)` and `- BBC we have earliest evidence someone quasar wearing. (S666)`. The frozen counter prints PASS for SET, ONEID, NOMARK, OPEN, HEDGE, CAPTION, APPEND, LINK, COPY, ACCESS and LINT. It prints FAIL for SOLE, ROWS and LOCATE, ending FAIL/exit 1. **This is a demonstrated target-leg survivor, NOT a demonstrated full-control survivor.** Its exact fixture is `/fast/scratch/hyaku/kotodama-r62/CtlDJunkTokens/junk-fixtures.json`.

**Impacted axes.** Depth and quality, with calibration harmed if lexical PASS is described as verified source support.

**Smallest safe correction.** Do not increase an overlap threshold or ban `denies`: neither fixes entailment. Before candidate/data evaluation, require a bounded source-support review of the exact four line bytes, with the evidence bound to their hashes, if D is to prove substantive repair. Otherwise keep the current mechanical/review-only distinction explicit and do not describe the frozen counter as proving “ONLY what the quote carries.” QUALITY 11 permits review-only clauses; it does not turn their weaker stand-ins into support evidence. A post-data strengthening cannot retroactively rescue the declared claim.

### 2. High — D can recycle a tier-C source as a nominally new A/B authority; capture identity is unchecked

**Counterexample.** **[INFERENCE; not scored]** Append S693 by re-registering the existing S687 Theoi URL and its genuine Hermes quote, changing the tier cell to A or B, and adding a purported Wayback URL after the live URL. Repoint line 93 to S693 with sufficient quote overlap. This avoids acquiring a stronger source while satisfying the nominal new-id/tier/Hermes checks, conditional on live location. An unrelated or nonexistent capture is immaterial if the live URL locates first.

**Evidence.** The old C row and quote are `corpus/SOURCES.md:642`. `accept-d.py:199-225` checks the tier string for line 93 and URL substring/order for new rows; it never compares new live URLs with base registry URLs or checks that a capture embeds the same page. `:271-280` passes all URLs to a locator which stops on the first location (`reports/round-61/reopen-quote.py:195-216`). ACCESS checks recorded access-bypass markers, not publisher authority or capture identity (`tools/check-source-access.py:47-91`). The assignment explicitly forbids reusing an existing registry URL and requires a same-page `id_` capture.

Other declared entry requirements also lack corresponding ROWS checks: quote maximum 25 words, body-text rather than caption, title/publisher/date, anchor location, recheck `180d`, and A/B for any optional new line-74 row. SOLE enforces A/B only for line 93. Body location and substantive support are disclosed review-only; the others should not be assumed covered by ROWS.

**Impacted axes.** Depth, source provenance and calibration. Relabeling an old C authority as A is not a harmless quality tradeoff.

**Smallest safe correction.** Before data, compare new live URLs with base registry URLs; validate exact Wayback host, capture shape and embedded live-page identity; check the required new-row fields. Retain a claim-scoped authority/body review rather than trusting a tier letter. A capture listing is not evidence that both availability routes were exercised.

### 3. High — O's DEFAULT leg accepts the wrong default exit and cannot establish the promised retry schedule

**Counterexample.** **[INFERENCE; not scored here]** A tool that behaves correctly for explicit flags but returns exit 0 after printing the expected default DEAD row still satisfies DEFAULT. So does one that issues nine DEAD requests without three 60-second-separated passes, then delays until the permitted wall-time interval. Both skip a specifically promised default behavior while leaving the other runs unchanged.

**Evidence.** `accept-o.py:364-371` captures `code4`, but DEFAULT uses only parsed row, wall time 100–600 seconds and total hits 9. It neither checks `code4 == 1` nor the default summary, nor timestamps/spacing of requests. EXIT (`:338-348`) checks different, explicit `--passes 3 --gap 0` invocations. The tool contract promises exit 1 for a non-LOCATED row and three passes with gap 60 (`:22-40`).

Two further cheap omissions are accepted by the current checks:

- A tool may print `url=-` for every match: `parse()` (`:240-246`) discards the captured URL entirely.
- A tool may require `--registry` and omit its default `corpus/SOURCES.md` behavior: all valid, private, default-retry and error invocations supply `--registry` (`:311,346,359,368,375-380`). The DEFAULT leg tests retry defaults, not the registry default.

**Impacted axes.** Operability and calibration. These are checks missing for already stated behavior, not requests for additional product scope.

**Smallest safe correction.** Before data, check default exit and summary; record server timestamps and test the promised schedule with an appropriate scheduling tolerance; retain and compare verdict URLs; add one copied-tree call with a real `corpus/SOURCES.md` and no `--registry`. Keep the default-registry test distinct from retry defaults. I requested existing control evidence from CtlODefault; no published result was available during this review, so none is claimed.

### 4. High, fixable harness defect — the declared separability base cannot run either acceptance command

**Counterexample/evidence.** The manifest uses base `d42ffb89` and overlays only D's two corpus paths or O's tool (`separability-manifest.json:3-33`). Its REC unit does not own the counters either (`:35-48`). Bounded read-only `git ls-tree` over that base returned the old locator and three existing checkers, **no `reports/round-62` files**. The same query at `f0173481` returned both counters, claims, manifest and declaration telemetry. The separability tool really materializes the declared base and overlays only each unit's lands (`tools/check-claim-separability.py:527-595,647-704`), rather than borrowing the current worktree's counter.

**[INFERENCE]** Once the product lands exist, both dynamic legs therefore fail because their acceptance script is absent; no other declared unit restores it. This is an instrument-baseline omission, not evidence that D depends on O. The dry-run's earlier absent-O-land error (`telemetry/declaration-dry-run.txt:31-33`) stopped before exposing this later problem.

**Impacted axes.** Operability of verification and calibration of separability evidence.

**Smallest safe correction.** Set the manifest's counterfactual base to the committed, pre-product instrument revision `f0173481047a93c46798f90b68d71d4f169d2642`, while retaining D's historical content-comparison BASE `d42ffb89`. Explain the two baselines. Do not put a shared counter in both claims' lands or add a false dependency on REC merely to make it appear in the sandbox.

**Direct answer on imports.** D imports only the old `reports/round-61/reopen-quote.py`, then invokes existing access/citation checkers (`accept-d.py:150-152,287-290`); it does **not** invoke O's new tool. O copies only `tools/reopen-row.py` and generates its own random local registry/server; it does **not** consume D's rows or repaired entry. Product-level separability is credible by static reading. The proposed QUALITY text's future use of O is policy/documentation, not an existing D counter import; do not silently turn it into one.

### 5. Medium — the lowest-axis note gives a reasonable work priority, not proof of the lowest-axis obligation

**Counterexample/evidence.** `claims.json:109` selects D because depth has not been admitted since round 59. Time since an admitted move is not a score comparison. `SCORECARD.md:11-16` says freshness remains historically lowest and that there is no calibrated numeric rubric. `:933-936` says no retirement and no saturation nudge without calibrated scores. The round-11 question is still present at fleet `.ufo/l0-questions.md:47`; it pauses freshness claims, not formally retires the axis. A capability also entered in round 61 (`SCORECARD.md:58`), so the stated stagnation-window condition cannot simply be presumed.

**Impacted axes.** Calibration and round-level lowest-axis conformance; not a reason to invent new scalar scores or declare saturation.

**Smallest safe correction.** State the exact limitation: freshness is the known lowest and blocked; D is chosen to close routed quality defects, not because a next-lowest ranking was established. A ranking/waiver remains for the canonical judge/operator, not an inference from “last admitted.” Keep the existing L0 question and the conformance gap visible. Changing the note alone does not manufacture satisfaction of AXES.md:33-38,66-73.

### 6. Medium, interpretation issue rather than a demonstrated regression — “never admitted” is not an express rewrite exemption

**Evidence in both directions.** Fleet and canonical CORPUS.md:53-60 say “Corrections are new entries, never rewrites,” with an explanation about aggregator/author collisions. They state no exemption for rejected knowledge. However, the round-61 closure §7 item 1 expressly routes these exact line repairs “in a new commit,” including caption re-scoping. Round-59 closure §2 D and §6 also accept paired knowledge substitutions as depth repairs. The round-59 closure `:117` distinguishes retained product from admission and requires a new pre-data freeze for admission; QUALITY 14 protects an object through adjudication, not against all future rounds.

**Counterexample to overclaiming.** Four in-place repairs can leave the entire footwear entry unadmitted: D checks four lines, not the original 41-row coverage predicate or the earlier S671 miss. Conversely, amending the round-61 receipt/lesson/closure to pretend the old entry passed would rewrite history, not repair product.

**Impacted axes.** Calibration, provenance and quality.

**Smallest safe correction.** Cite the bounded, new-commit repair route and preserve all round-61 filed verdicts and source-row facts. Do not justify it solely with “never admitted,” and do not claim whole-entry admission from D. The broad CORPUS wording versus the narrower lane-repair precedent is an interpretation for the canonical judge, not a categorical violation proved by this critic. If the judge applies the broad rule to lane knowledge corrections too, an append-only correction entry or an explicit authorized exception is needed before changing the predicate; silently rewriting the rule is not a fix.

## Axis fit and universal-clause answers

- **D:** defensible as a small depth move **if** the four source-scoped assertions really improve. AXES.md:11 explicitly includes cited verifiable detail, and LEARNING.md:34,86-89 maps stronger/re-verified knowledge to the quality trend and its depth/freshness/operability axes. The round-59 verified paired-fix precedent is especially strong contrary evidence to calling all repairs mere record work. LOG/SCORECARD errata alone would be quality-of-records, not depth; a LINK re-score alone would not establish depth either. Do not claim coverage: no new knowledge surface is declared or tested.
- **O:** a genuine operability capability surface is available. The prior row locator already existed (`reports/round-61/reopen-quote.py` supports `--row`), so the actual novelty is a durable independent lane tool with caption separation and configurable bounded passes, not invention of quote location. A runnable implementation of those deltas is not merely a re-score. A new pathname or fixture-only shortcut is insufficient.
- **Universals:** D enumerates its four line positions and its finite cited-new-row set; O enumerates 18 classes twice plus one closed-port row, 37 requested IDs, and ORDER rejects missing/duplicate parsed IDs. Thus the explicit “each/every” over those bounded sets is not inherently oversized. Neither predicate supports universal real-world source support, arbitrary HTML/network behavior, or “no harm anywhere.” O's literal-loopback privacy test is not exhaustive evidence about all resolved host/address cases in its broader contract. Keep review-only live behavior and this finite fixture scope explicit.
- **Frozen predicate identity:** both predicates use the advertised final labels and conjunction of legs; no multi-predicate substitution is needed to explain the findings. Any correction belongs before candidate/data measurement, with controls committed. A miss under the original first-run rule must remain a miss.

## One small provenance trap to prevent during integration

Removing the entry's only S687 citation but leaving its current `mined` / footwear `used-by` pairing records a citation that no longer exists. Search found S687 in knowledge only at the to-be-replaced line 93; the already-existing `corpus/lessons/round-61.md:84,118` really cites it. D's APPEND permits changing only S687's used-by cell. The smallest separable repair is to point that cell to the existing round-61 lesson and log old→new, not to erase the C row, inflate its tier, leave a false used-by, or depend on newly landed REC text. SOURCES contract `:103-108,116-118` supplies the semantics.

## Verification and limits

No candidate, counter, test suite, locator or live fetch was executed by this critic. Observed commands were bounded read-only tree listings and counter hashes; all completed, with no background process started. No tools were installed or updated. The only lane write is this report; the created scratch directory is `/fast/scratch/hyaku/kotodama-r62/CriticClaims/`.

The strongest exercised counterexample available to this review is the peer's lexical-leg survivor, whose **whole predicate failed**. The D whole-pass and O shortcut constructions above remain static inferences, not fabricated receipts. The canonical judge must distinguish these fixable counter/harness gaps from an actual quality trade or a retroactive change of predicate; this report does not admit or reject either claim.
