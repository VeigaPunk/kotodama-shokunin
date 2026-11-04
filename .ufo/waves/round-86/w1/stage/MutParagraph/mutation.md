# MutParagraph — one reversible mutation probe

Axes: **depth + operability**. Freshness pause unchanged. Seat evidence only; no external admission or planner exception adjudication.

## Mutant and expected detector

Copied ExecParagraph/check-paragraph-locator.py to own scratch. One smallest behavior-bearing mutation, candidate line 63: `c.endswith('caption')` → `c == 'caption'`. This plausibly narrows caption detection while leaving explicit `thumbcaption`, `figure` and `figcaption` exclusions intact.

Expected detector: exclude a paragraph inside `<div class="image-caption">` rather than treating it as an article paragraph. Exact fixture:

```html
<div class="mw-parser-output"><div class="image-caption"><p>needle</p></div><p>opening</p><p>needle</p></div>
```

Invocation: `python3 -B locator.py --html generic-caption.html --quote needle --expect 2`.

## Actual outputs and verdict

| Phase | Direct cases meeting expectation | Generic caption output | Frozen O mechanism overlay |
|---|---:|---|---|
| Pristine | 10/10 | exit 0: `PARAGRAPH: PASS ordinal=2 expect=2 quote='needle'` | exit 0, `ACCEPT-O-86: PASS legs=8/8` |
| Mutated | 9/10 | exit 1: `PARAGRAPH: FAIL ambiguous matches=2 quote='needle'` | exit 0, `ACCEPT-O-86: PASS legs=8/8` |
| Restored | 10/10 | exit 0: `PARAGRAPH: PASS ordinal=2 expect=2 quote='needle'` | exit 0, `ACCEPT-O-86: PASS legs=8/8` |

**Killed by independent generic-caption detector; survived frozen O's tested behavioral mechanism and candidate's 28-check selftest.** Baseline and restoration were clean before drawing this conclusion. This is a coverage finding, not a demonstrated defect in pristine candidate and not permission to revise the frozen predicate.

Remaining direct case exit codes were identical across all phases:

- nav 0; figure/figcaption 0; extra paragraphs outside root 0.
- multiple sibling roots 2 and nested roots 2: `PARAGRAPH_ERROR: expected one .mw-parser-output article, found 2`.
- nested inline tags, entities and Unicode 0, with `quote='café naïve & wise tail'`, ordinal 2.
- absent span 1: `PARAGRAPH: FAIL absent matches=0 quote='missing'`.
- duplicate containing paragraphs 1: `PARAGRAPH: FAIL ambiguous matches=2 quote='needle'`.
- repeated span within one paragraph 0, ordinal 1: unique containing paragraph is the contract, not unique occurrence.

All driver subprocess exits were 0; no stderr in those driver runs. Raw per-case stdout/stderr, inputs, expected exits and observed exits are retained in pristine.json, mutated.json, restored.json and receipt.json.

## Frozen-counter boundary

No Git fixtures, index writes or commits. The actual unchanged measure86.py was imported with only `git`/`blob` read transport overlaid in memory. Frozen config and Iron HTML were real bytes; candidate executions were real isolated subprocesses. Synthetic metadata, BEFORE absence and registry text were transport fixtures, **not evidence of genuine lands/ancestry, actual registry state, or accepted O**. The eight-leg PASS is therefore explicitly a mechanism-level observation, never production acceptance. Counter's own --selftest was not run because it mutates Git fixtures.

In all three phases: candidate `SELFTEST: PASS (28 checks)`, HELDOUT PASS, real Iron expect 1 exited 1 with ordinal 2, expect 2 exited 0 with ordinal 2, retaining the full frozen quote in output. No full repository tests/build/lint/formatter runs.

## Restoration evidence

SHA-256 candidate original/scratch-restored/source-after:
`85c8c70f7959e4e4059b1421f06337ecfa898a0cf30a43364e63c2a98e43a61f`

Mutated scratch bytes:
`63408210156bab36439f3acaa6f2c3c0a33d23c2dfef4dd65af7f4fef8504d3f`

Frozen counter before/after:
`15cf54126850d7f16acaec1cc22174a4a6319107752c7b9ee6028473158f19fe`

Exact restoration is recorded true in receipt.json. Only own scratch candidate was mutated; sibling candidate and frozen counter untouched. Probe scripts are retained as evidence; scratch directory removed before handoff. No tools installed or updated.

## Evaluation

Accuracy 4/5: observed outputs/hashes preserved; counter metadata is synthetic and explicitly limited. Completeness 4/5: all assigned HTML case categories covered with one mutant, not exhaustive HTML parsing. Clarity 4/5: distinguishes independent kill from counter survival; raw logs are longer. Actionability 4/5: exact fixture exposes missing caption-suffix selftest coverage; frozen target unchanged. Conciseness 4/5: duplicate raw phase receipts retained for audit. Overall 4.0/5. Improvement: future non-frozen behavioral suites can retain the generic-caption fixture. User agreement depends on respecting mechanism versus acceptance distinction.
