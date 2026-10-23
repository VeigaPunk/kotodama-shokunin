# Round 63 — S694 pileus / liberty cap

## Finding and proposed behavior

Selected Princeton University Library’s curated numismatic exhibit, “Liberty’s Cap: The Origins of a Numismatic Symbol,” as the tier-A institutional source. It directly describes the Roman enfranchisement rite and the pileus as a public sign of freedom. The live and archived page both contain the body-text anchor quote; both canonical locator checks ultimately returned `LOCATED`.

### Draft artifacts for L1

Registry row (11 columns):

```text
| S694 | “Liberty’s Cap: The Origins of a Numismatic Symbol,” Princeton University Library, n.d. — https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html ; capture https://web.archive.org/web/20251206173833id_/https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html | docs | A | Roman Republican manumission ritual and the pileus as a public sign of freedom in numismatic imagery | opening explanatory paragraph after the H1, Roman Republic enfranchisement sentence: "given a pileus to wear as a public sign of his freedom" | Princeton University Library describes a pileus being given to a Roman slave at enfranchisement as a public sign of freedom and traces the cap’s later liberty imagery. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

Entry bullet:

```text
- A Roman slave received the pileus as a public emblem of freedom (S694)
```

Gate line:

```text
- S694 | https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html | 2026-10-23 | "given a pileus to wear as a public sign of his freedom"
```

The quote has 12 normalized words. Its body-text location is the opening explanatory paragraph after the H1. The entry clause has 7 content words; `pileus`, `public`, and `freedom` occur in that quote in order, with no more than 3 consecutive copied words. The page has no publication date shown; the row uses `n.d.`.

## Provenance and gates

- Ordinary fetch command: `curl -L --max-time 30 -A 'Mozilla/5.0' -D /fast/scratch/hyaku/kotodama-r63/KotodamaR63.ScribeRowS694/princeton.headers -o /fast/scratch/hyaku/kotodama-r63/KotodamaR63.ScribeRowS694/princeton.html -w 'http_code=%{http_code} final_url=%{url_effective} bytes=%{size_download}\n' 'https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html'` → `http_code=200 final_url=https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html bytes=41039`. The page HTML shows the Princeton University Library logo and footer; the quoted sentence is in its explanatory body paragraph.
- CDX was read from `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fstatic-prod.lib.princeton.edu%2Fcapping-liberty%2Fcase%2F6%2Findex.html&output=json&limit=-5&filter=statuscode%3A200`. It returned three HTTP-200 captures, each with original URL exactly equal to the live URL: `20241011190201`, `20250516135250`, `20251206173833`. The newest capture was selected. The static `read` view of its `id_` page contains the same quoted sentence in the same body paragraph.
- Exact reuse check: `grep` on `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` for `static-prod\.lib\.princeton\.edu/capping-liberty/case/6/index\.html` → `No matches found`.
- Live locator command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html' 'given a pileus to wear as a public sign of his freedom'` → `LOCATED https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html`; exit 0.
- Capture locator command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20251206173833id_/https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html' 'given a pileus to wear as a public sign of his freedom'`. First run → `NOT_LOCATED https://web.archive.org/web/20251206173833id_/https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html URLError`, exit 1. Retrying that same command after the transient error → `LOCATED https://web.archive.org/web/20251206173833id_/https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html`, exit 0. Both locator checks therefore have a final `LOCATED` result; the initial transient is retained here.

### Rejected candidate

Britannica’s `https://www.britannica.com/topic/pileus-hat` was not selected: an ordinary curl returned HTTP 403 with `cf-mitigated: challenge`. CDX lists five captures and a static-reader view of the newest capture contains a body-text quote, but the base locator returned `NOT_LOCATED` on the live URL (`HTTPError`) and on the newest capture (`quote-absent`); two earlier capture attempts returned `HTTPError`. I therefore did not claim the challenge was successfully routed around or use that candidate. The Princeton live and capture locators both passed.

## Touched surfaces, gates, and limits

- Lane write: this requested report only, `.ufo/waves/round-63/w1/ScribeRowS694.md`. No registry row, entry, README, or product code was changed.
- Scratch artifacts: `/fast/scratch/hyaku/kotodama-r63/KotodamaR63.ScribeRowS694/S694-selected.md` contains the three draft artifacts and locator evidence. `/fast/scratch/hyaku/kotodama-r63/KotodamaR63.ScribeRowS694/ScribeRowS694.md` retains the Britannica candidate investigation.
- `accept-c.py`, the overall `LIVE` leg, blind source-support review, and all other S694–S717 rows were not run or judged by this seat. This report is row-level source evidence, not an `ACCEPT-C-63` receipt.
- No tools were installed; no Git or jj write command was run. The O/reopen-row repair and review gate are out of scope for this seat.
