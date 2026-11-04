# ExecCraftLedger — round 86 / w1

## Scope and axes

Depth + operability. Delivered six authored NON-CANON exercise records and an independent, read-only Python checker in this seat's unique stage directory. This deepens handling of genres already covered in `corpus/knowledge/linguistics/orality-formulaic-language.md` §§6–7; it does not claim new genre acquisition or satisfy the frozen D/O acceptance legs by itself.

Read `claims.json` and `measure86.py` from freeze `16c267832746e1cb98fb42a56180f8d1d12dc18b` using read-only `git -C ... show`; also read the current carriers and round source map. Frozen predicate/counter unchanged and never executed. No Git/JJ/index mutations, commits, delegation, background work, external substrates, source-registry writes or production edits.

## Files delivered

Relative to the lane root:

- `.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json`
- `.ufo/waves/round-86/w1/stage/ExecCraftLedger/check-craft.py`
- `.ufo/waves/round-86/w1/stage/ExecCraftLedger/probe-receipts.json`
- This exclusive report.

## Entry-scribe artifact interface

`craft.json` is a UTF-8 JSON object, `schema_version: 1`, `status: NON-CANON`, axes and explicit hypothetical-material boundary, plus exactly six `records`. Stable IDs `R86-CRAFT-01` through `R86-CRAFT-06` map respectively to:

1. Attestation versus origin: earliest surviving packet witness is not first utterance.
2. Borrowed proverb: donor/recipient witnesses and an explicit transfer-direction basis; ultimate origin remains unknown.
3. Literary saying becoming proverbial: authored composition, situated uptake and anthology collection have separate dates.
4. Ambiguous riddle: two candidate solutions retain clue support and strain; no selected answer.
5. Editor conjecture: transmitted gap and attributed emendation remain separate; the conjecture cannot establish its preferred solution.
6. Translated wording: source/target text and witness dates, translator and free-rendering method remain separate.

Each record contains `id`, `case`, `genre`, `sense`, `composition_status`, `wording`, and four top-level clock objects named `attestation`, `origin`, `collection`, `design`. Every clock requires `value` (ISO date or explicit null), nonempty `reason`, and `scope`. Historical clocks are `synthetic`; only the real exercise-authorship `design` clock is `real`. A null design date is refused. Origins are deliberately unknown except the explicitly stipulated literary composition. Historical date ordering applies within the invented packet, never across synthetic and real scopes.

Case-specific objects are `borrowing`, `literary`, `solutions`, `editorial`, `translation`. Each `exercise` supplies `prompt`, `expected`, `refusal` and evidence-triggered `flip`. These are worked teaching cases, not source rows, historical quotations or canon proposals. No S924–S928 IDs are consumed. English wording for invented languages is authored demonstration text, not evidence of a real language.

Entry scribe may refer to the stable exercise IDs and distinctions above. Do not promote their hypothetical dates, people, texts, expected answers or invented histories into the sourced dossier or source registry. The dossier's evidence must remain independently sourced. L1 alone chooses any production destination; the checker defaults to sibling `craft.json`, so retain the pair together or pass an explicit ledger path.

Usage from any directory:

```text
python3 -B /absolute/path/to/check-craft.py /absolute/path/to/craft.json
```

Exit 0 = structural contract satisfied; 1 = ledger contract refused; 2 = input/JSON/CLI error. Default argument is sibling `craft.json`, independent of process cwd. Duplicate JSON keys are rejected. The checker imports no ledger code, writes nothing and invokes no subprocess, Git or network. Successful output explicitly says structure only, not source verification.

## Exact observed bounded evidence

Only the assigned craft-checker subprocess probes were run, with Python 3.14.8. No builds, lint, formatters, repository tests or acceptance-counter runs.

Observed order:

```text
01-red-null-without-reason: exit=1
CRAFT: FAIL record 1: reason: nonempty text required
02-green-complete-ledger: exit=0
CRAFT: PASS (6 NON-CANON records; structure only, not source verification)
```

Twenty real subprocess observations matched their expected exit and diagnostic marker. Subsequent refusals cover duplicate IDs, CANON status, origin overclaim, donor/recipient clock conflation, premature literary uptake, selecting an ambiguous answer, conjecture promoted to witness text, translation backdating, absent clock/case, wrong composition status, missing candidate strain, invalid date, incorrect clock scope, nonstring case, malformed JSON and duplicate keys. The twentieth invocation demonstrates default sibling lookup while cwd is the seat scratch directory. No observed stdout/stderr contained a traceback.

`probe-receipts.json` preserves each complete input (including all failing mutations), argv, cwd, expected/observed exit, required marker, exact stdout/stderr, match boolean, runtime and SHA-256 of both implementation artifacts. The first red input was never used to alter the staged green ledger. Scratch `/fast/scratch/hyaku/kotodama-r86/ExecCraftLedger` was created exclusively for these probes and removed after receipts were retained. Receipt argv still names removed scratch fixtures; reconstruct them from each stored `input` if reproducing.

## Limitations and authority

- This checker validates this six-case exercise contract, not historical truth, source support, first attestation worldwide, unique riddle solutions or canon admission. Free-form reasons and evidence descriptions still require human reading.
- No public URLs were independently reopened because this seat authored synthetic exercises rather than source rows. The source map was read for scope only; no source-verification claim is made.
- LSP tooling is not exposed in this seat's available tools; no existing symbol definition/reference/refactor claim is made. All implementation files are new and local to this stage.
- No installs or updates; existing Python 3.14.8 was used. Host pacman pause and PATH-write prohibition preserved.
- Inherited freshness pause remains unchanged. The stated L1 planner-role validator prohibition remains unresolved; no exception or external admission is claimed.
- No blockers for this scoped deliverable. Main owns integration and post-integration checks. If integrated, main can rerun the explicit checker command; frozen D/O gates remain separate and require their own committed production artifacts.

## Deliverable self-review (not an admission judgment)

Accuracy 4/5: actual subprocess outputs are retained, but historical support is intentionally outside this synthetic ledger. Completeness 4/5: six requested cases and four clocks are present; free-form reasoning remains review-only. Clarity 4/5: explicit synthetic/real scopes prevent date conflation, but consumers must retain the top-level boundary. Actionability 4/5: sibling-default CLI and reconstructable receipts are supplied; integration destination belongs to L1. Conciseness 4/5: six worked cases are self-contained, though their repeated clock explanations increase size. Overall 4.0/5. Highest-value downstream improvements are preserving the boundary on excerpt and separately reviewing sourced entry claims; neither is a checker admission claim. A reader should agree this is a scoped exercise implementation rather than evidence of historical discovery.

Report: .ufo/waves/round-86/w1/ExecCraftLedger.md
