# S712 — wimple / veil source note

## Outcome

Partial source work only; **not a verified S712 row**. The Britannica article is a relevant Tier B candidate, and its body quote is located on the live page. The selected Wayback URL visibly contains the same body sentence in the `read` extraction, but the required base locator returned `quote-absent` for that capture. Other locator attempts on its available captures returned `URLError`; direct `curl` could not connect to `web.archive.org:443`. As the assignment makes the base locator authoritative, I do not report capture location as passing and the row must not be integrated as verified without resolving this.

## Source, quote, and candidate artifacts

Opened by ordinary `read`:
- Live: `https://www.britannica.com/topic/wimple`
- CDX query: `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.britannica.com%2Ftopic%2Fwimple&output=json&limit=-5&filter=statuscode%3A200`
- CDX showed same-page captures dated 20250126045834, 20250313004627, 20250418020140, 20250622032622, and 20260211225215, all with original `https://www.britannica.com/topic/wimple` and status 200. Selected capture: `https://web.archive.org/web/20260211225215id_/https://www.britannica.com/topic/wimple`.
- The live and selected-capture page reads both display this article-body sentence (not a caption, alt text, or title): “The wimple, usually made of fine white linen or silk, framed the face and covered the neck.” It is 17 normalized words.
- Search of `corpus/SOURCES.md` for the exact live URL returned **No matches found**. ScribeRowS713 acknowledged avoiding this exact URL. I did not establish uniqueness against every other scribe's eventual choice.

Candidate row (draft only; capture locator failed):
> | S712 | Britannica Editors, “Wimple,” *Encyclopaedia Britannica* (page date not shown) — https://www.britannica.com/topic/wimple ; capture https://web.archive.org/web/20260211225215id_/https://www.britannica.com/topic/wimple | docs | B | the medieval European women's wimple as a head-and-neck covering, its face framing, and its material | Article body, second paragraph: “The wimple, usually made of fine white linen or silk, framed the face and covered the neck” | the wimple's linen-or-silk material and its face-framing and neck coverage | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |

Candidate entry bullet (one S-id; content words and quote-word order are supported; seven consecutive copied words, within the 12-word maximum):
> - Medieval women wore linen and silk wimples that framed the face and covered the neck. (S712)

Gate-ready line:
> - S712 | https://www.britannica.com/topic/wimple | 2026-10-23 | "The wimple, usually made of fine white linen or silk, framed the face and covered the neck"

## Locator evidence and gates

Required live-page command:
```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.britannica.com/topic/wimple' 'The wimple, usually made of fine white linen or silk, framed the face and covered the neck'
```
Full stdout: `LOCATED https://www.britannica.com/topic/wimple`. The tool response did not print a numeric exit code; the locator docstring specifies exit 0 for `LOCATED`.

Required selected-capture command:
```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260211225215id_/https://www.britannica.com/topic/wimple' 'The wimple, usually made of fine white linen or silk, framed the face and covered the neck'
```
Full stdout: `NOT_LOCATED https://web.archive.org/web/20260211225215id_/https://www.britannica.com/topic/wimple quote-absent`; exit 1.

Additional ordinary locator attempts (exact commands are recorded in the scratch evidence file): capture 20250126045834, 20250313004627, 20250418020140, and 20250622032622; the 202602 capture without `id_`; and the 202602 `id_` URL with an `http` origin. Each printed `NOT_LOCATED <attempted URL> URLError` and exited 1. The `http`-origin check was diagnostic only, not a candidate row URL. The `curl` diagnostic printed `curl: (7) Failed to connect to web.archive.org:443 after 179 ms: Could not connect to server`, then `HTTP 000; final=https://web.archive.org/web/20260211225215id_/https://www.britannica.com/topic/wimple`; exit 7. No challenge bypass was attempted. Full CDX output, exact commands, and all locator outputs are in `locator-outputs.md` below.

Verdict: live quote leg PASS; archive quote leg **not confirmed / FAIL for this candidate**. A read-tool extraction showing the quote does not override the base locator result. No ACCEPT-C counter, LIVE subset gate, independent review, or claim-level gate was run by this leaf seat. No counter receipt or acceptance verdict is claimed.

## Touched surfaces and scope

- Wrote this single report in the lane repo. No product source, `corpus/SOURCES.md`, knowledge entry, counter, or review artifact was edited.
- No tools installed or updated.
- Claim O repair/review, counters, and integration are out of scope for this source seat.

## Scratch artifacts

All candidate artifacts and raw locator evidence are under `/fast/scratch/hyaku/kotodama-r63/ScribeRowS712/`:
- `row.md` — draft registry line, explicitly marked unverified
- `entry-bullet.md` — candidate entry bullet
- `gate-line.md` — candidate Gate line
- `locator-outputs.md` — CDX output, locator commands and outcomes, and rejection notes
- `source-search.txt` — exact-URL registry search result

The row is intentionally reported as a candidate only: the selected capture's prescribed locator did not locate the quote.