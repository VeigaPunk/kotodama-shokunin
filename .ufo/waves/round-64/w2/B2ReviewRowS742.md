# B2ReviewRowS742 — falsification review of wave-1 draft S742

VERDICT: FIX-REQUIRED — anchor cell's curly-quoted heading `“Morning Meeting Greetings”` is extracted by the counter's `QUOTE_RE` before the real ASCII quote (3 normalised words vs required 8–25 → ROWS `quote_words=3`), and the drafted quote alone is 26 words (>25). All other fields verify clean.

## HTTP results (verbatim)

- Live: `curl -sL --max-time 90 'https://files.eric.ed.gov/fulltext/EJ1271032.pdf'` → `200`, `application/pdf`, 810771 bytes.
- Archive: `curl -sL --max-time 120 'https://web.archive.org/web/20250403232101id_/https://files.eric.ed.gov/fulltext/EJ1271032.pdf'` → `200`, `application/pdf`, 810771 bytes — byte-identical to live (`cmp -s`).
- Lane locator (argv mode, drafted quote): first line `LOCATED https://files.eric.ed.gov/fulltext/EJ1271032.pdf`.

## Findings

1. **ROWS failure (anchor extraction).** Anchor cell: `p. 48, “Morning Meeting Greetings”: "Rachele took time … ritual"`. `QUOTE_RE = r'"([^"]+)"|“([^“”]+)”'` hits the curly-quoted heading first → extracts `Morning Meeting Greetings` (3 words; counter requires 8–25). Same failure in `reopen-quote.py row_target` → `--row S742` would print `NOT_LOCATED quote under 8 words` (S742 is not in the LIVE subset, but ROWS fails anyway). Fix: remove/unquote the lead-in heading so the ASCII quote is the first quoted string in the cell.
2. **ROWS failure (quote length).** The drafted quote alone normalises to 26 words (`another’s` → `another` + `s`); cap is 25. Fix: trim one word — e.g. end at `…name with eye contact)` (25 words).
3. **Quote content verified.** Located verbatim, contiguous, in p. 48 body prose under the "Morning Meeting Greetings" section (not heading/caption/nav): "Rachele took time and provided explicit instruction so that every greeting included three components: acknowledgement (usually the saying of another’s name with eye contact), ritual …".
4. **Citation verified.** Title page: "Classroom Greetings: More than a Simple Hello" by Lauren K. Shields-Lysiak, Maureen P. Boyd, John P. Iorio Jr., Christopher R. Vasquez; header "Iranian Journal of Language Teaching Research 8(3), (Oct., 2020) 41-56". Authors, year, journal, volume(issue), pages all match.
5. **Tier A justified** for the scoped claim (primary single-classroom case study on explicitly taught greeting routines).
6. **BULLET RESTATE.** Simulated on the row as filed: in-order hits = 0 (<3) because the row-quote is the heading. With the anchor fixed to the Rachele quote: content=9, in_order=4, novel words present, copy_run=2 — passes. Clause is hedged ("can make"), no invented numbers; supported by quote and surrounding text (greeting "created a connection", builds community/belonging).
7. **Inherited `VERIFY: LOCATED` line is misleading**: reproduces only in argv-quote mode, not in the `--row` registry mode the counter uses.

Full table: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS742/review.md`.
