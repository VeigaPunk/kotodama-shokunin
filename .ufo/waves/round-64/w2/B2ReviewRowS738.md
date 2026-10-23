# B2ReviewRowS738 — falsification review of inherited draft row S738

**VERDICT: FIX-REQUIRED** — the anchor cell's first double-quoted span is the section heading `CONCEPTUALIZATION OF THE FAMILY, NONHETERONORMATIVE MASCULINITY AND ETHNICITY`, not the body quote. `anchor_quote()` (accept-c.py + reopen-quote.py `row_target`) takes the FIRST `"…"` match, so as drafted: RESTATE fails (`in_order=0`, simulated against the frozen counter logic) and LIVE leg `--row S738` vouches for a *heading* — anchors may not come from headings. All other fields verified clean.

## HTTP results (verbatim)

- Live: `HTTP 200 https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf` — 793,536 B, PDF 1.7, 21 pp (plain curl GET, no challenge).
- Capture: `HTTP 200 https://web.archive.org/web/20250720191758id_/https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf` — 795,846 B.
- Wayback availability API: `timestamp=20250720191758`, `original` == live URL — capture link consistent.

## Locator runs

- Body quote → `LOCATED https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf`
- Section name as quote → `LOCATED` (heading is locatable; the defect hides from LIVE but breaks RESTATE).

## Required fixes

1. **Reorder the anchor cell** so the quote is the first/only double-quoted span and the section name is unquoted, e.g.:
   `section CONCEPTUALIZATION OF THE FAMILY, NONHETERONORMATIVE MASCULINITY AND ETHNICITY, paragraph introducing Excerpt 4.2: "as a result of the experts’ advice, they prioritized the children’s well-being and accommodated to their needs linguistically"`
2. **Fix the locator phrase**: the quote is in the paragraph *introducing Excerpt 4.2* ("In Excerpt 4.2, Błażej explains how as a result of the experts’ advice, they prioritized the children’s well-being and accommodated to their needs linguistically."), not "the paragraph following Excerpt 4.1".

## Verified clean

- Quote: verbatim, contiguous, normalised 20 words, narrative body text (not caption/heading/nav). Found at normalised offset 30339 in pdftotext extraction.
- Citation: eprints record — "Kozminska, Kinga and Zhu, H. (2021) Making a family… In: Wright, L. and Higgins, C. (eds.) Diversifying Family Language Policy. Contemporary Studies in Linguistics. London, UK: Bloomsbury Publishing, pp. 55-79. ISBN 9781350189904." — authors, year, title, book, series, publisher, pages all match.
- Tier A for scope "the one studied transnational LGBTQ+ adoptive family's expert-informed caregiver-child language choices": the chapter is the original study of that family by its own researchers — primary for exactly that scope.
- kind `book`, status `mined`, opened `2026-10-23`, recheck `180d`, 11 cells, used-by = entry path: all conform.
- BULLET: "Expert guidance prioritized children’s well-being and accommodated their needs linguistically during adoptive language socialization (S738)" — asserts only what the quote grounds (expert advice → prioritised well-being + linguistic accommodation), no invented numbers. RESTATE sim vs the real quote: content=13, in_order=7, novel words={adoptive,during,expert,guidance,language,socialization}, copy_run=6 → would PASS once the anchor is fixed.

## Counter blind spot noted

ROWS only checks the extracted string's word count (heading passes at 8 words); RESTATE is the catching leg here. Reviewer evidence and tools: full per-field verdict table at `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS738/review.md`; fetched PDFs + extracted text in the same scratch dir. No installs needed (`curl`, `pdftotext`, system python3).
