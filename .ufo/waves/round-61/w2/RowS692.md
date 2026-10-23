# Row S692 — one-row one-clause review: dictionary.com/browse/sabot

Reviewer: KotodamaR61.RowS692 (leaf, review-only). Measured revision efbee29cd8c0872a4fb89db34c489d4a9960916c. 2026-10-23 UTC.

## Fetch record (ordinary means only: curl, no browser)

- Live `https://www.dictionary.com/browse/sabot`: **HTTP 200**, final URL unchanged, 83,361 bytes decoded (20,144 on the wire, gzip). Plain curl, browser User-Agent. Real content served (title `SABOT Definition & Meaning | Dictionary.com`); the strings `challenge-platform`/`captcha` present are head script boilerplate, not an interstitial — no challenge was met or passed.
- Archive: `archive.org/wayback/available` rate-limited me with **429 Too Many Requests** (disclosed; not a page failure). The CDX API answered: 200-status captures `20250314122924` and `20251203233222`. Fetched `https://web.archive.org/web/20251203233222/...` — **HTTP 200**, 44,848 bytes. So an archive capture works.
- No tools installed (none needed).

## (1) QUOTE — verbatim check

Row quote: "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc."

- Live page: exact string present twice in raw HTML — offset 19665 (the `<meta name="description">` copy) and offset **32828, the visible body**: a `<p class="txt-variant-label-short">` whose text content is the definition, sitting in the American entry's definition sequence directly after "sabots plural" and before the second definition "a shoe with a thick wooden sole and sides and a top of coarse leather." That is entry body text, not navigation and not a caption fragment.
- Archive capture 2025-12-03: same string verbatim in the body flow inside a `<span>`, same position after "plural sabots". Independent corroboration.

Carrier text (≥10 consecutive words, page body): "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc." (26 words).

## (2) CLAUSE — coverage check

Clause: "A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, and Belgium."

| Clause part | Page | Carried? |
|---|---|---|
| hollowed shoe made from one wooden block | "a shoe made of a single block of wood hollowed out" | yes (pure reorder; "single"→"one", "wood"→"wooden", no content change) |
| worn especially by farmers and workers | "worn especially by farmers and workers" | yes, verbatim |
| in the Netherlands, France, and Belgium | "in the Netherlands, France, Belgium, **etc.**" | **no** — hedge removed |

Sole defect, named exactly: the page's country list is **open-ended** ("Belgium, etc." = and elsewhere); the clause **drops the "etc." hedge and closes the list** ("France, and Belgium"), presenting a non-exhaustive enumeration as a closed one. Per the row criterion ("a hedge removed" is an addition-class defect) this part is unsupported. No other text on the page repairs it: the country words each occur exactly once (Belgium ×1, Netherlands ×1, France ×1), all inside that one "etc." list; the second and third definitions (thick wooden sole; military disk/base ring) mention no countries. Everything else in the clause is carried, and no date, cause, comparison, or universal is added.

## Findings by severity

- **NOT-SUPPORTED (clause, hedge removal)** — "etc." dropped and list closed with "and"; source is "Netherlands, France, Belgium, etc." Evidence: live body offset 32828, saturated single occurrence of the list on the page.
- **INFO** — quote is genuine verbatim body text (LOCATED), live and archived.

## Residual risk / verification gaps

- Single live fetch at 2026-10-23; Dictionary.com serves definitions server-side, but a JS re-render could in principle differ from the fetched HTML (unlikely; archive capture shows the same body flow).
- Wayback availability API 429 — capture existence established via CDX instead; the 2025-03-14 capture was not fetched (the 2025-12-03 one sufficed).

QUOTE S692 LOCATED
CLAUSE S692 NOT-SUPPORTED
