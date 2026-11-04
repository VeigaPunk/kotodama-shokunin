# ExecParagraph — r86-v1

Axes: depth + operability; scoped implementation adds the operability paragraph locator. Inherited freshness pause unchanged. Lane evidence only; no external admission or planner-prohibition exception adjudication.

## Files created

Under `.ufo/waves/round-86/w1/stage/ExecParagraph/`:
- `check-paragraph-locator.py` — complete stdlib CLI candidate for L1 integration as `tools/check-paragraph-locator.py`.
- `design.md` — extraction policy, CLI, integration, exact observations and limitations.
- `Iron.frozen.html` — frozen Git blob capture, SHA-256 `afbf036349ffb87745dc44595726e554dbe83c17e0d3f6eef2976c9970548ed1`.
- `selftest.json`, `selftest-initial.json`, `iron-red.json`, `iron-green.json` — exact argv/exit/stdout/stderr receipts.

This report is the only write outside that unique stage root. Production files, claims, frozen counter, Git/index and external state untouched. No installs or network.

## Behavior

Finds exactly one nonempty containing paragraph under one `.mw-parser-output`; inline/entity decoding and Unicode whitespace folding; excludes figures/captions/navigation/hidden and ws-noexport subtrees. Unique mismatch prints actual ordinal with exit 1; match exit 0. Absent/ambiguous containing paragraphs exit 1. Missing article, multiple roots, invalid UTF-8, invalid CLI/input exit 2 with `PARAGRAPH_ERROR` and no traceback. Normal mode reads only; selftest writes temporary fixtures only below existing --work, with each public CLI child isolated in its own cwd and -B.

## Assigned observed probes

- `--selftest --work /fast/scratch/hyaku/kotodama-r86/ExecParagraph`: exit 0, `SELFTEST: PASS (29 checks)`. Earlier 28-check pass retained in `selftest-initial.json`; added image-caption suffix regression after MutParagraph reported a surviving selftest mutation. Extraction implementation unchanged.
- Frozen Iron quote with `--expect 1`: exit 1; `PARAGRAPH: FAIL ordinal=2 expect=1 quote='giving origin to the three important varieties: cast iron, steel, wrought iron.'`
- Same frozen capture/quote with `--expect 2`: exit 0; `PARAGRAPH: PASS ordinal=2 expect=2 quote='giving origin to the three important varieties: cast iron, steel, wrought iron.'`

Both red and green retain empty stderr. Selftest and capture receipts were copied into stage; exclusive scratch was then removed. No builds/lint/formatters/counter gates run; parent owns post-integration checks. No test claims beyond these observed outputs.

## Retained risks and blockers

No implementation blocker. HTMLParser plus explicit exclusion classes is not a full HTML5/CSS/semantic DOM; arbitrary malformed markup or unrecognized publisher navigation remains a review boundary. Multiple parser roots are refused rather than choosing one. Repeated text inside one paragraph is intentionally one containing paragraph. Local input is trusted: normal-mode read_text is unbounded and does not reject FIFO/device paths, so those could block; not exercised and no network capability exists. SentinelScope-20 independently reported 14 matching probes and this static FIFO limitation; that is peer evidence, not an additional self-run claim.

No LSP tool is mounted, so supported symbol lookup/refactoring is unavailable rather than presumed absent from an empty response. New standalone module changes no existing symbols. L1 must copy candidate to production and add the frozen SKILL.md registry reference, then own integration gates/review. Frozen files remain unchanged; no commits.

Report: .ufo/waves/round-86/w1/ExecParagraph.md
