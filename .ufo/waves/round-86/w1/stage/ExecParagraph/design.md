# Paragraph locator: round 86 staged implementation

Axes: depth + operability; this seat changes only operability. Freshness remains paused. This is lane implementation evidence, not external admission or adjudication of the planner-role prohibition.

## Integration

Copy `check-paragraph-locator.py` to `tools/check-paragraph-locator.py`. The frozen registry leg additionally requires L1's SKILL.md registration containing both that path and `paragraph-locator`; this seat deliberately does not edit production files.

```
python3 -B tools/check-paragraph-locator.py --html PATH --quote TEXT --expect N
python3 -B tools/check-paragraph-locator.py --selftest --work EXISTING_DIRECTORY
```

0 means the unique containing paragraph has the expected one-based ordinal; 1 means absent/ambiguous containing paragraphs or ordinal mismatch; 2 means `PARAGRAPH_ERROR:` on stderr without traceback. The verdict prints the normalized quote and actual ordinal whenever unique, including mismatch. A quote repeated within one paragraph still has exactly one containing paragraph.

## Extraction decisions

- Stdlib HTMLParser decodes entities once. An ancestry stack scopes extraction to exactly one `.mw-parser-output` root; missing/multiple roots are unevaluable, not an arbitrary first-root selection.
- Only nonempty `p` elements count. Inline text chunks concatenate before Unicode whitespace folding (`' '.join(text.split())`); inline markup does not manufacture spaces inside words. `br` supplies a whitespace boundary. Quote whitespace folds identically. Search is a case-sensitive literal substring, not a regex, first occurrence locator, or cross-paragraph span.
- Ancestor flags exclude figure/figcaption/caption, navigation, aside/header/footer, script/style/template/noscript, explicit hidden elements, navigation/banner/contentinfo roles, and named MediaWiki/Wikisource navigation/export/caption classes. Excluded descendants contribute neither ordinals nor inline text.
- `ws-noexport` is important structurally: Iron's See-also/disclaimer paragraph lives there. It is not article prose and must not shift the quoted varieties paragraph to raw ordinal 3. The `prp-pages-output` content remains included. There is no Iron-text special case.
- Void tags do not change ancestry; matched closes unwind ancestry; common block starts implicitly close an open paragraph, supporting omitted `</p>`. This is not a full HTML5 DOM/browser/CSS implementation; arbitrary malformed nesting or externally styled navigation requires review.
- CLI modes are exclusive. Positive decimal expected ordinals, nonblank quotes, strict UTF-8, readable input and existing selftest work directory are required. No fetching, shell calls, git operations, repository discovery or normal-mode writes occur.
- Selftest creates one temporary sandbox under `--work` and a separate child cwd/HTML fixture for each subprocess. Children use `-B`, bounded timeouts and the same public CLI. Temporary files are removed even on failure. No fixture Git repositories or commits are created.

## Observed bounded evidence

`selftest.json`: exit 0, `SELFTEST: PASS (29 checks)`. Initial `selftest-initial.json` preserves the earlier 28-check pass. The added image-caption suffix regression addresses MutParagraph's independently discovered selftest coverage gap; extraction code is unchanged. Checks cover ordinal pass/fail, absent/ambiguous quotes, nested markup/entities/Unicode, whitespace and line breaks, figure/navigation/caption/disclaimer exclusion, out-of-article paragraphs, script/style, empty/implicitly closed paragraphs, cross-paragraph refusal, one-paragraph repeated spans, missing/multiple article roots, malformed UTF-8, four invalid expected ordinals, empty quote, missing args/input/work, nonexistent work, and mixed modes.

`Iron.frozen.html` is copied verbatim by read-only `git -C ... show 16c267832746e1cb98fb42a56180f8d1d12dc18b:reports/round-86/evidence/Iron.html`. SHA-256: `afbf036349ffb87745dc44595726e554dbe83c17e0d3f6eef2976c9970548ed1`.

`iron-red.json`: exit 1, `PARAGRAPH: FAIL ordinal=2 expect=1 quote='giving origin to the three important varieties: cast iron, steel, wrought iron.'`

`iron-green.json`: exit 0, `PARAGRAPH: PASS ordinal=2 expect=2 quote='giving origin to the three important varieties: cast iron, steel, wrought iron.'`

Receipts retain exact argv, return code, stdout and stderr. No frozen counter selftest or gate, builds, lint, formatter, production checks, network or installs were run. Python is the existing system executable. LSP definitions/references/refactors were unavailable: no LSP tool is mounted in this seat; this is a new standalone file and no existing symbols are renamed.

## Limitations and review boundary

The class/tag/role policy is explicit, not computed CSS or a semantic guarantee for every publisher. Empty paragraphs do not count. Multiple parser roots produce exit 2. An existing but empty article yields an absent-quote exit 1. Semantic article-scope review and L1 post-integration gates remain necessary. Claims/counter are untouched; planner-role exception is not claimed adjudicated.
