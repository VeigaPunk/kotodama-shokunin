# ScoutSurface — round 87, w1

Axes: operability; attribution accuracy; bounded read-only scope. Confidence: high for frozen source comparison, no runtime verdict.

## Observed findings

Frozen contract and counter were opened at `2a3b5643899c3520867ae930593cafef6ef19cad`: `reports/round-87/claims.json` and `reports/round-87/measure87.py`. The claim is one O capability, exactly 12/12 through `--packet PATH --json`, explicitly finite structural discrimination, not truth, quotation support, authenticity, canon, or arbitrary substitute rejection. The counter loads the six-record packet from BASE, not mutable staging. Its `cases()` names three positive cases, eight structural negatives, and invalid JSON; `evaluate()` checks expected exit plus required finding ID, or records=6/findings=[] for positives. It does not establish semantic validity. No battery was run by this seat.

Exact production path absence at BASE `83846a22ee1e9da7aa52ac505ccebf4455169247` is confirmed by `git cat-file -e BASE:tools/check-attestation-packet.py`: exit 128, path-does-not-exist diagnostic. This proves path absence, not absence of prior capability elsewhere.

**The old stage checker already implements all eight enumerated domain-check categories, not merely record completeness.** Immutable BASE body `.ufo/waves/round-86/w1/stage/ExecCraftLedger/check-craft.py` was opened. Numbered pointers below refer to that body, also displayed through the read tool:

| r87 contract category | Existing r86 implementation |
|---|---|
| RECORD_ID: nonempty/unique | `fields()`/`record_check()` lines 42–44, 60; `validate()` lines 149–159 |
| CLOCK_MISSING: four clocks | `CLOCKS` line 24; `object_at()` lines 36–39; loop lines 65–67 |
| CLOCK_REASON: nonblank reason | loop line 68 via `fields()` |
| CLOCK_DATE: valid canonical date | `iso_date()` lines 47–54; loop lines 71–72 |
| RECORD_FIELD: sense/wording/genre/composition status | lines 60–64 (genre/status constrained more tightly by case) |
| SOLUTION_CONFLICT: unresolved cannot select | lines 102–106 |
| EDITORIAL_CONFLICT: conjecture not silently promoted | lines 116–125 |
| TRANSLATION_CLOCK: target not backdated | lines 128–134; existing requirement `source < target == attestation` is stricter than merely rejecting attestation before translation date |

The inherited CLI is already executable Python with positional ledger/default craft.json; `main()` lines 173–188 returns 0/1/2, uses `CRAFT_ERROR`, and emits human-readable fail/pass, not the r87 structured finding interface. `no_duplicate_keys()` lines 164–170 also already rejects duplicate JSON keys. Other inherited checks include six-case coverage, NON-CANON status, clock scopes, borrowing dates, literary uptake and editorial dates. These are historical facts, not a demand to enlarge r87 scope.

## Distinguishing acquisition from inheritance

[INFERENCE grounded in the bodies] Defensible novelty is the production location and public named-option/JSON contract, stable machine-readable finding IDs, and its isolated selftest interface—not newly discovered unresolved-solution/editorial/translation relationships. The frozen bounds phrase “newly enumerated integrity relationships” can mean newly enumerated in this round; it must not be repeated as newly implemented domain capability relative to r86. No false first-completeness or first-integrity-checking assertion is supported.

Nearest match from file-structure-first discovery is the r86 stage checker itself. Existing production `tools/check-cited-records.py` is instead a cited-record byte/path audit (`scan()`, `summary()`, CLI description at line 177), not this packet validator. Targeted literal search located frozen counter caller `TOOL`/`evaluate()` and claim CLI; no production candidate body was present in the scoped glob at observation time. A concurrent candidate may subsequently appear. LSP was unavailable (`xd://lsp`: no such tool); these are direct body/literal observations, not semantic-reference completeness claims.

## Surface absence and limits

With hidden paths included and gitignore disabled, lane `**/considerthese*` and `**/ConsiderThese*` matched nothing. Fleet direct-child `*considerthese*` also matched nothing and explicit fleet `considerthese/**` was missing. This is bounded path absence, not a claim about other machines or installed tools. External shokuknow merge/menu reading was unnecessary; adoption is none.

This author-side scout supplies bounded data-walk evidence for L1 canonical planning. It grants no admission and no formal L2 planner-policy exception; the unresolved L2 conflict remains disclosed. Existing sources/counter history and frozen claims were untouched. Runtime success, final production candidate contents, and end-to-end 12/12 remain unobserved by this seat and belong to explicitly authorized integration/checking seats.

Receipts: `.ufo/waves/round-87/w1/stage/ScoutSurface/receipts.md`. Exclusive scratch created, receipt retained in stage, then scratch removed. No installs/updates, external sources, tests, production changes, Git mutations, or delegation.

Report: .ufo/waves/round-87/w1/ScoutSurface.md
