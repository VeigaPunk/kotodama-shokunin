# B2ReviewRowS722 — falsification review of inherited draft

Draft: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS722/row.txt` (read-only; not edited)

## HTTP results (verbatim, 2026-10-23)

- Live: `HTTP 200 https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/` (198771 bytes)
- Capture: `CAPTURE HTTP 200 https://web.archive.org/web/20250410073702id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/` (195142 bytes)
- Wayback API after one 429 + 20s backoff: `{"closest": {"status": "200", "timestamp": "20250410073702", "url": "http://web.archive.org/web/20250410073702/https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/"}}` — capture original matches live URL.
- Lane locator: `python3 -B reports/round-61/reopen-quote.py '<url>' '<quote>'` → `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/`

## Verdict table

| field | draft value | verified? | evidence (verbatim) | required fix |
|---|---|---|---|---|
| row shape | 11 cells; mined; 2026-10-23; 180d; used-by = entry path | YES | conforms to ROWS leg | none |
| live URL | https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/ | YES | `HTTP 200 https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/` | none |
| capture | web.archive.org/web/20250410073702id_/…PMC5182137/ | YES | `CAPTURE HTTP 200`; API `timestamp=20250410073702`, same original | none |
| anchor quote | "emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning" | YES | verbatim+contiguous in body `<p id="P35">`: `…This emerging view emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning, as well as ecological factors…`; 17 normalised words; body text not caption/nav | none |
| anchor locator | "Section A Continuous Vocabulary Spurt, paragraph 35" | YES | nearest preceding heading `A Continuous Vocabulary Spurt`; quote in `<p id="P35">` | none |
| citation authors | Samuelson and McMurray | YES | `citation_author`: Larissa L Samuelson; Bob McMurray | none |
| citation year | 2016 | YES | page's own citation: `Wiley Interdiscip Rev Cogn Sci. 2016 Dec 1;8(1-2):10.1002/wcs.1421.` | none |
| citation title | "What does it take to learn a word?" | YES | `citation_title="What does it take to learn a word?"` | none |
| citation journal/vol/issue | Wiley Interdisciplinary Reviews: Cognitive Science 8(1–2) | YES | `citation_journal_title`/`volume=8`/`issue=1-2` | none |
| tier B | B for scoped topic | YES | WIREs review = expert survey (strong secondary); primary record for fast mapping/vocabulary spurt lies in cited originals — B is the correct ceiling, A would overreach | none |
| BULLET | "Novelty, attention, statistical learning, and competition shape how toddlers build vocabulary (S722)" | YES | RESTATE simulation with counter's regex/STOPWORDS: 9 content words; in-order hits novelty→attention→statistical→learning→competition = 5; novel words {shape,toddlers,build,vocabulary}; longest copied run 4 ≤12; no invented number, no overreach beyond what the quote establishes | none |

VERDICT: CLEAN — quote verbatim in body, locator LOCATED, citation and 2016/8(1–2) match page metadata, tier B correct, BULLET satisfies all RESTATE legs.
