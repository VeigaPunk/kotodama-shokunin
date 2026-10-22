# ReviewRowsS320S323S356 — round-55 spot-check §5 item 4 (non-author row re-open)

Round 56, 2026-10-22. Scope: rows S320, S323, S356 (`corpus/SOURCES.md:349,352,385`), their Gate lines (`corpus/lessons/round-55.md:104,107,140`), their citing sentences (`corpus/knowledge/myth-symbol/monsters-hybrid-beings.md:80,86,180`), and the S320 HTML-entity question. All three rows are the ones spot-check §5 item 4 named as never re-opened by a non-author.

Method: every source re-opened this session by plain curl, ordinary means only, no installs (used existing curl, pdftotext/pdftoppm/poppler, tesseract, qpdf). Scratch: /fast/scratch/hyaku/kotodama-r56/ReviewRowsS320S323S356/.

## S320 — VERDICT: row clean; the `&#124;` cells are the registry's pipe escape, not a defect. No fix.

Re-open: https://www.gutenberg.org/cache/epub/73533/pg73533.txt — direct plain request, HTTP 200, `text/plain`, 977,828 bytes and 24,314 newline-terminated lines, both exactly as the row records (SOURCES.md:349).

- All 15 anchor quotes verified verbatim (joined across printed line breaks, runs of spaces collapsed; no word dropped). Whitespace-split word counts 7–21, all ≤ 25.
- Locators pinned: Völuspá 40 first two lines at pg73533.txt:1016-1017; Völuspá 39 last two lines :1013-1014 (the quote takes the first half-lines of the stanza's last two printed lines and trailing-omits the refrain "would you know yet more?" — locator stays accurate); Völuspá 44 second line :1037; Voluspo note 39 "Dread Biter" :1479-1481; Voluspo note 40 (Skoll and Hati, eclipse-myth) :1493-1498; Grimnismol note 39 Ironwood :4421-4426 under the GRIMNISMOL header :3742. The Ironwood note really is the note to Grimnismol 39 and ends "cf. Voluspo, 40", so the entry's dual locator "(S320, Völuspá 40; note to Grimnismol 39)" (monsters-hybrid-beings.md:80) is exactly right, and the sentence attributes the conjecture to Bellows, satisfying the cell's own tier note that his editorial judgements stay his statements. General Introduction and Völuspá Introductory Note quotes all present in their sections.
- The entity call: the row's quotes cell carries four `&#124;` occurrences, each escaping a literal `|` of Bellows's printed caesura inside the SOURCES.md Markdown table row, where a raw pipe would split the cell. The same escape convention appears elsewhere in the file (e.g. S332's query string `action=query&prop=revisions&#124;proofread`, SOURCES.md:361), and the Gate bullet, which is not a table, carries the decoded `|` (round-55.md:104). Verdict: required pipe escaping, consistent with house convention; no old -> new.
- Tier A stands: public-domain primary translation, authoritative for the poem's English wording and for what Bellows's notes say; the in-cell caveat is present.

## S323 — VERDICT: row and Gate line clean. No fix.

Re-open: https://www.getty.edu/art/exhibitions/bestiary/ (HTTP 200, `text/html`, 43,714 bytes) and https://www.getty.edu/art/exhibitions/bestiary/downloads/beasts_checklist.pdf (HTTP 200, `application/pdf`, 5,595,978 bytes — byte count matches the row exactly; 24 pages per qpdf, as the row states).

- Both exhibition-page anchors verbatim in the opening paragraph, with typographic “escaped” (12 and 15 words): "a popular type of medieval book describing the beasts of the world" and "they often “escaped” from manuscripts to inhabit other art works made during the medieval period".
- Checklist anchors exact: "Legendary Peoples, 1277 or after" on PDF p. 2 of 24 as checklist nos. 5–6 (Ms. Ludwig XV 4, fols. 117v and 118, acc. 83.MR.174.117v/.118); "23. Unknown German artist / Lion Aquamanile (Water Vessel), about 1250" on PDF p. 5 of 24, with "Los Angeles County Museum of Art, Gift of Varya and…" confirming the row's LACMA attribution.
- Citing sentence carried (monsters-hybrid-beings.md:86). Tier A stands (holding museum's own page and official checklist; curatorial-copy caveat present).
- Note: pdftotext emits a benign "Expected the optional content group list" warning on this PDF; extraction is unaffected. Not a row defect.
- Gate line round-55.md:107 verbatim against the registry, 12 words. No old -> new.

## S356 — VERDICT: row clean; Gate line has one defect (HTML entities where the registry has decoded marks). One fix.

Re-open: https://web.archive.org/web/20260914204030id_/https://files.commons.gc.cuny.edu/wp-content/blogs.dir/20578/files/2022/05/FYW-Sample-Reading-B.pdf — HTTP 200, `application/pdf`, 2,941,677 bytes, exactly the row's recorded capture and size. The direct CUNY URL re-probed today with a plain request answers HTTP 403 (`text/html`): the row's "challenge met, not passed" route note is accurate; the Wayback capture is an ordinary public copy. The PDF is a 12-leaf scan of facing pages with no text layer, as the row states; I OCRed at 200 dpi and read the page scans.

- All four anchors verified. Thesis III (p. 7) and Thesis V (p. 12) match OCR verbatim (16 and 21 words); the III quote sits on the right-hand page of the spread headed 6/7 and the V quote on the left-hand page of the spread headed 12/13, confirming both locators. Thesis I (p. 4) and Thesis VI (p. 18) match after dehyphenating printed line breaks ("etymo-logically", "fan- tastic"); both passages visually confirmed on the scans under running heads "4 Jeffrey Jerome Cohen" and "18 Jeffrey Jerome Cohen" (17 and 21 words). The registry cell uses decoded typographic marks, correct.
- Citing sentence carried (monsters-hybrid-beings.md:180, Theses I, III, V). Tier A stands (author's own chapter; the cell's scope caveat — no bestiary, no non-European material — is accurate).
- DEFECT — `corpus/lessons/round-55.md:140`: the Gate quote leaks four numeric character references where the registry cell has decoded marks; one of the "HTML entities in 16 Gate lines" defects recorded at round-55.md:241. Exact fix (decode `&#8220;`/`&#8221;` to the registry's marks):
  - old: `"the monstrum is etymologically &#8220;that which reveals,&#8221; &#8220;that which warns,&#8221; a glyph that seeks a hierophant."`
  - new: `"the monstrum is etymologically “that which reveals,” “that which warns,” a glyph that seeks a hierophant."`

## Summary

| row | re-open | anchors | ≤25 words | locators | tier | citing sentence | verdict |
|---|---|---|---|---|---|---|---|
| S320 | HTTP 200, bytes match | 15/15 verbatim | yes (max 21) | all confirmed | A ok | carried (:80) | clean; `&#124;` = pipe escape, no fix |
| S323 | HTTP 200 x2, bytes match | 4/4 verbatim | yes (max 15) | all confirmed | A ok | carried (:86) | clean, no fix |
| S356 | Wayback 200, bytes match; CUNY still 403 | 4/4 verbatim (dehyphenation) | yes (max 21) | pp. 4, 7, 12, 18 all pinned | A ok | carried (:180) | row clean; Gate line :140 entity leak, one fix above |

## Residual risk and unrun checks

- S320's five General Introduction / Introductory Note quotes were confirmed present verbatim in the whole-file join; their section attribution follows Bellows's layout, line numbers not pinned individually.
- S356 Thesis III/V wording was matched by OCR of a half-page crop rather than a visual read of those two pages; pp. 4 and 18 were visually read. No mismatch found.
- No prior content hash is recorded in the rows, so identity rests on URL, content type and exact byte-count match, not sha256.
- I applied no fixes (verdict-only seat): the S356 Gate-line decode is left to the L1's integration hand.
