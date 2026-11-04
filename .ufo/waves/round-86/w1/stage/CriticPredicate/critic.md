# CriticPredicate — r86-v1

Axes: **depth + operability**. Freshness pause unchanged. This is lane-local criticism, not admission, external spot-check, planner-role exception adjudication, or a native-judge verdict.

## Scope and evidence

Reviewed the exact assigned freeze `16c267832746e1cb98fb42a56180f8d1d12dc18b`, base `1e6b10a02b93a981b012987c51399d278fe37fa9`, frozen `reports/round-86/measure86.py` and `claims.json`, protocol Gate standard, and QUALITY 7/9/11/19/23/26/28.

Frozen counter SHA256: `15cf54126850d7f16acaec1cc22174a4a6319107752c7b9ee6028473158f19fe`.
Frozen claims SHA256: `051f57130785a4b50a3294466a13c385122f36c55df7292d536e1e69ba322634`.
Observed both working copies equal those frozen bytes. The preserved exact counter copy is `measure86.frozen.py` in this stage.

Bounded foreground probes used the unchanged counter functions with **only Git transport replaced**: assigned real freeze/base blobs, synthetic lands overlays, synthetic ancestry/tree responses. Candidate tools and the real frozen lint ran as actual isolated subprocesses. The synthetic `aaaa…` revision and `bbbb…` tree in receipts are deliberately model inputs, **not real commits, live CLI measurements, provenance proof, or criterion-19 receipts**. No Git mutation or counter selftest was run; the latter creates commits. No network, installs, background jobs, production edits, or other runtime adjudication.

Receipts under `.ufo/waves/round-86/w1/stage/CriticPredicate/`:
- `probe.py`: reproducible bounded overlay harness (includes the subsequent single-leg lint control).
- `probe.txt`: original observed seven overlay cases and two direct candidate invocations.
- `lint-control.txt`: separately observed additional single-leg lint control.
- `frozen-inventory.txt`, `frozen-counter-selftest.txt`: freeze inventory and existing receipt.
- `frozen-pre-dispatch-controls.json`, `frozen-separability-pre-dispatch.txt`: preserved Git missing-path diagnostics, **not JSON/control receipts**.

## F1 — operability survives without reading HTML or running any selftests

**Counterexample, executed:** an eight-line candidate never opens `--html`, emits `SELFTEST: PASS (12 checks)` without checking anything, always prints `ordinal=2`, and returns green only when the quote is not literal `absent` and `--expect` is 2. Its registry is only `paragraph-locator tools/check-paragraph-locator.py`, without a Gate row.

Observed `O-nonreader-fake-selftest-and-bare-registry`: exit 0, `ACCEPT-O-86: PASS legs=8/8`. The same candidate directly returned exit 0 for both an unreadable HTML path and an HTML file containing `needle` in two article paragraphs. Those violate the frozen required exit 2 for malformed input and exit 1 for ambiguous containment. Its Iron output never prints the quote, also required by claims.json:20.

**Evidence:** measure86.py:92-105 trusts a candidate-reported selftest tally and uses only known positive ordinal 2 cases, one negative expected ordinal 1, and literal absent quote. `HELDOUT` checks exit status but no finding-id or paragraph identity. Its HTML includes a figure-caption distractor, but no independent case isolates caption-only/nav-only matches, ambiguous article containment, malformed input, traceback handling on malformed input, a varying positive ordinal, or printed Iron quote. Registry line 110 is two substring checks. These are mechanical interface promises, not all covered by the review-only article/caption-scope clause.

**Impacted axes:** operability directly; calibration if its eight green legs are represented as full capability verification. Gate standard selftest/registry and QUALITY 11 are the relevant boundaries. This is not the QUALITY-28 mistake of running an unpinned judge: the new locator is the **graded candidate**, so pinning it to the freeze would prevent capability acquisition. The defect is candidate self-attestation plus insufficient independent observations.

**Smallest safe correction:** keep the predicate frozen and preserve its limited verdict. Independently demonstrate every omitted mechanical promise using frozen/declared external fixtures and observable finding IDs; verify the actual Gate registry fields, not token presence. Additional independent checks cannot retroactively supply missing pre-dispatch clause controls. A corrected future declaration needs varying ordinals/HTML-derived outcomes, ambiguity, exclusions, malformed input, quote output, and green-first differential controls. Never relabel the present frozen eight-leg green as proof of those missing clauses.

## F2 — eight pipe characters pass “six design decisions”

**Counterexample, executed:** starting from a 7,638-byte structurally passing dossier fixture, replace only the decision-table block with eight lines containing a single `|` each. The result is 7,606 bytes and has no table cells or six decisions.

Observed `D-eight-pipes-not-six-decisions`: exit 0, `LEG PASS DECISIONS table-lines=8`, `ACCEPT-D-86: PASS legs=7/7`.

**Evidence:** measure86.py:71-73 counts lines beginning `|`; it neither checks a header/separator nor six data rows with content. This is a mechanical nearest-miss for the table form, distinct from the explicitly review-only truth of source support. Twelve repeated `S924/S925/S926 fixture` bullets likewise pass ANCHORS and the frozen citation-shape lint; that shows only counts and single-ID line shape, not twelve attested facts. The fixture's initial green is **structural**, not a legitimate all-semantic-clauses green control.

**Impacted axes:** depth; QUALITY 11 forbids promoting a weaker form stand-in into semantic verification.

**Smallest safe correction:** in this wave manually inspect the six substantive decisions and located anchor support, separately from the frozen leg result; preserve this survivor. In a properly predeclared later predicate, parse nonempty table cells and exactly distinguish header/separator/data rows, with this near-miss as a red control. Do not revise the frozen threshold after data. D is already correctly framed as deepening inherited proverb/riddle knowledge, not first acquisition; absent dedicated path is not absence of genre knowledge.

## F3 — duplicate source identities are silently accepted

**Counterexample, executed:** duplicate all three source rows, leaving every checked value unchanged. `D-duplicate-source-id-shadowing` exits 0, `ACCEPT-D-86: PASS legs=7/7`.

**Evidence:** measure86.py:37-43 stores rows in a dictionary by ID; the final duplicate silently overwrites an earlier row. Lines 78-80 validate only that surviving representation. Registry identity uniqueness therefore is not verified. The tested case is identical duplicates; an adversarial conflicting duplicate is a code-derived risk, not a separately executed observation.

**Impacted axes:** depth/source provenance, and calibration if ROWS is called full registry validity. CORPUS forbids ID reuse; source identity is review-only in the frozen declaration, so this is an exposed review obligation, not proof that the dossier's actual rows are wrong.

**Smallest safe correction:** independently check S924–S926 occur once each and their opened sources support their quotes; do not infer this from ROWS. Future registry parsing should refuse duplicate IDs before building its mapping.

## What the controls actually verify

- `D-config-mutation-control`: exit 1, only FROZENCFG fails, all other six legs pass. Lands config cannot shrink the frozen minimum. This is a clean **mechanical** differential control.
- `D-single-leg-frozen-lint-control`: add a multi-ID prose line outside ANCHORS and supply a constant-print lint at lands. Exit 1, only LINT fails, all other six legs pass. The real lint is read from the freeze and its digest compared with the frozen constant (lines 81-85). QUALITY-28 authority pinning works for this tested replacement. The earlier related test in `probe.txt` also failed ANCHORS and is not claimed as single-leg evidence.
- `O-registry-control`: remove only both registry tokens from the otherwise eight-leg-passing stub. Exit 1, only REGISTRY fails. This proves **token presence**, not a conformant Gate row.
- D shape fixture plus only its entry/registry overlay and O stub plus only its tool/SKILL overlay each pass independently. This supports the narrow mechanical absence of a D↔O dependency in this counter; it is not the required full separability check over the eventual production lands.

## Criteria and protocol coverage limits

| Standard | What evidence establishes / limitation |
|---|---|
| Gate standard | Counter declares exits 0/1/2 and has a committed selftest receipt. Its selftest runs only D CLI scenarios, not O. O candidate self-reported tally and token-only registry do not establish isolated checks or required registry fields. Native judge authority remains separate. |
| QUALITY 7 | Frozen claim path sets are disjoint in the counter. The displayed separability manifest assigns D S924–S926; O exports PARAGRAPH_ERROR. The actual manifest/check receipts are not in the assigned freeze inventory, so these overlays do not establish production separability. |
| QUALITY 9 | Working pre-dispatch controls record base refusal and freeze absent-land failures. Frozen claims.json contains prose and leg names, not the complete per-command declaration/receipt bijection. No bidirectional argv audit was executed. Preserve the distinction between an observed run and this missing proof. |
| QUALITY 11 | F1/F2 are survivors; frozen selftest is only eight D scenarios (clean, five easy mutations, freeze, base), without per-clause nearest-miss controls. No O scenarios exist in that selftest. Metadata presence, decision semantics, and registry shape are not clause-complete merely because the leg list matches. |
| QUALITY 19 | Code uses lands committed blobs and emits matching revision/tree headers; no worktree grading is apparent. Our transport overlay does NOT test real ancestry, carrier-parentage, receipt existence at lands, or true stamped-tree equality. No such claims are made. |
| QUALITY 23 | Exact freeze contains counter-selftest.txt with `COUNTER-SELFTEST: PASS (8 checks; clean green first)` and `exit=0`, but no counter digest in that receipt. Freeze inventory lacks pre-dispatch-controls.json; its absence is independently preserved. Working receipts show freeze D fail 3/7 and O fail 2/8, not all legs evaluated successfully. No counter revision was made by this seat. |
| QUALITY 26 | Code loads constants with freeze:claims.json, requires full IDs and first-parent ancestry, checks frozen leg inventory, and rejects config differences. Our executed config overlay tests that last property only. Freeze lacks do-nothing/pre-dispatch control receipts and separability files; the existing selftest alone is not evidence all required controls were committed at freeze. External assigned freeze pin remains necessary; we did not test a junk freeze. |
| QUALITY 28 | D lint pin resists a lands stub in the single-leg control. There is no corresponding authority-pin conclusion for the new O candidate: independent behavior must be observed, not trusted from its selftest banner. |

## Disposition boundary

These are fixable implementation/evidence defects and explicit proof limitations, not authorization to alter frozen predicates. A supplementary demonstration can narrow uncertainty about the delivered artifacts but cannot rewrite pre-dispatch history or turn an output count into full behavioral proof. Treating structural greens as semantic acquisition, or omitting unverified clauses to claim no harm, would change the declared task rather than answer this review. No axis verdict, admission decision, planner exception, or external-review status is issued here.
