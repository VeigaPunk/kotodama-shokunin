# S713 cloche-hat source research — scoped report

## Behavior
No product behavior or lane corpus file was changed. This seat produced a candidate source, quote, row, entry bullet, and Gate line as scratch drafts only. The candidate is **not accepted** under the row rules because the required Wayback locator did not confirm the quote.

## Gates and evidence

Assignment context reviewed read-only: `reports/round-63/claims.json`, the docstrings of `reports/round-63/accept-o.py` and `reports/round-63/accept-c.py`, and section 5 of `corpus/lessons/round-62-verifier-spotcheck.md`. Claim C's frozen predicate is `ACCEPT-C-63: every leg of reports/round-63/accept-c.py prints PASS.` This seat did not run the C counter; no counter verdict is claimed.

Candidate live source, opened via the ordinary read tool:
- `https://fashionhistory.fitnyc.edu/1920-1929/` — “1920-1929”, Fashion History Timeline; Karina Reddy; published 2018-05-11; updated 2020-08-18.
- Body location: Womenswear, paragraph beginning “Though this was one of the more popular styles”. The quote is in running prose, not a caption, alt text, or title.
- Quote: “the brimless cloche hats that were popular during the twenties” (10 normalised words).

Live locator command:
`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://fashionhistory.fitnyc.edu/1920-1929/' 'the brimless cloche hats that were popular during the twenties'`

Live locator stdout: `LOCATED https://fashionhistory.fitnyc.edu/1920-1929/` (the shell tool completed successfully and emitted no explicit zero-exit line).

Archive discovery/locator findings:
- The prescribed CDX query `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Ffashionhistory.fitnyc.edu%2F1920-1929%2F&output=json&limit=-5&filter=statuscode%3A200` failed via the read tool with HTTP 429. A reduced-fields CDX query, the Wayback availability API, and timemap JSON also returned HTTP 429.
- Ordinary curl retry: `curl -sS --max-time 30 -A 'Mozilla/5.0' -D - 'https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Ffashionhistory.fitnyc.edu%2F1920-1929%2F&output=json&limit=-5&filter=statuscode%3A200'` → `curl: (7) Failed to connect to web.archive.org:443 after 189 ms: Could not connect to server`; exit 7.
- A timestamped ordinary replay request for `https://web.archive.org/web/20200818000000id_/https://fashionhistory.fitnyc.edu/1920-1929/` returned the actual id_ capture URL `https://web.archive.org/web/20200828090928id_/https://fashionhistory.fitnyc.edu/1920-1929/`. The read tool returned the page, its canonical original URL, and the same body quote.
- Required locator command on that id_ URL, run twice:
`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20200828090928id_/https://fashionhistory.fitnyc.edu/1920-1929/' 'the brimless cloche hats that were popular during the twenties'`
- Both attempts stdout: `NOT_LOCATED https://web.archive.org/web/20200828090928id_/https://fashionhistory.fitnyc.edu/1920-1929/ URLError`; both exited 1. Therefore the read tool displayed the archived quote, but the required locator did not confirm it. Do not ingest these drafts without a successful archive locator. The archive lookup also did not satisfy the requested successful CDX step.

Rejected alternatives and outcomes:
- `https://www.britannica.com/art/cloche` resolved to `https://www.britannica.com/topic/cloche`, a horticulture article about plant covers, not headgear.
- `https://www.vam.ac.uk/articles/an-introduction-to-1920s-fashion` returned HTTP 404.
- `https://www.britannica.com/topic/cloche-hat` returned HTTP 404.

## Draft artifacts — not eligible for ingestion yet

Registry row:
`| S713 | Karina Reddy, “1920-1929”, Fashion History Timeline, Fashion Institute of Technology, published 2018-05-11; updated 2020-08-18 — https://fashionhistory.fitnyc.edu/1920-1929/ ; capture https://web.archive.org/web/20200828090928id_/https://fashionhistory.fitnyc.edu/1920-1929/ | docs | B | 1920s cloche hats as brimless women’s fashion accessories | Womenswear, paragraph beginning “Though this was one of the more popular styles”: “the brimless cloche hats that were popular during the twenties” | brimless cloche hats remained popular accessories throughout the twenties | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

Entry bullet:
`- Brimless cloche hats remained popular accessories throughout the twenties (S713)`

Gate line:
`- S713 | https://fashionhistory.fitnyc.edu/1920-1929/ | 2026-10-23 | "the brimless cloche hats that were popular during the twenties"`

The bullet has one S-id, eight qualifying content words, at least three in quote order, and no more than three consecutive copied words. The quote is 10 normalized words. The row is a draft only because archive location failed.

## Touched surfaces and out of scope

- Lane repository: only this required report file was written. No product, registry, entry, counter, or other lane file was modified.
- Scratch drafts/evidence are under `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS713/`.
- Did not run `reports/round-63/accept-c.py`, `tools/reopen-row.py`, or any O/C counter; did not use git/jj write commands; installed no tools.

## Artifact paths

- Report: `.ufo/waves/round-63/w1/ScribeRowS713.md`
- Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS713/source-evidence.md`
- Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS713/row-S713.md`
- Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS713/entry-bullet-S713.md`
- Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS713/gate-S713.md`
- Scratch: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS713/decision-S713.md`
