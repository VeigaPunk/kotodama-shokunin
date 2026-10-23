# ScribeRowS708 — Round 63 evidence

**Status: candidate only; archive-locator confirmation failed.** The live page and both opened Wayback captures visibly contain the quote in article body text, but the required base locator returned `NOT_LOCATED` for each tested capture. Do not count this row as fully source-confirmed or integrate it without resolving that gate.

## Behavior and draft artifacts

Opened the Cooper Hewitt, Smithsonian Design Museum article “Yoruba Complete,” by Susan Brown (published June 25, 2015; the page identifies her as Associate Curator in the Textiles Department). The article body says: “Re-tying the wrap each time allows a woman to keep up with fashion, create appropriate wraps for different social occasions, and express her personal aesthetic.” It directly supports occasion-specific styling and personal aesthetic; it does not establish rank/status, so the clause is intentionally limited to the supported aspect.

Draft registry row (11 columns):

```text
| S708 | Yoruba Complete, Susan Brown, Cooper Hewitt, Smithsonian Design Museum, June 25, 2015 — https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ ; capture https://web.archive.org/web/20260605232422id_/https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ | docs | A | Cooper Hewitt curator's account of Yoruba gèlè styling for social occasions and personal aesthetic | Article body, sentence on retying for social occasions: "create appropriate wraps for different social occasions, and express her personal aesthetic." | The curator says retying lets women create occasion-appropriate gèlè wraps and express personal aesthetic. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

The anchor quote is 12 normalized words. The proposed clause has at least five content words and shares `create appropriate wraps social occasions express personal aesthetic` in quote order; its longest copied run is four words. It carries exactly one S-id.

Draft entry bullet:

```text
- Yoruba women create appropriate wraps for social occasions and express personal aesthetic through each wearing (S708)
```

Gate-ready line:

```text
- S708 | https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ | 2026-10-23 | "create appropriate wraps for different social occasions, and express her personal aesthetic."
```

## Gates and exact evidence

- **Live locator:** from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, ran `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.cooperhewitt.org/2015/06/25/yoruba-complete/' 'create appropriate wraps for different social occasions, and express her personal aesthetic.'` → stdout `LOCATED https://www.cooperhewitt.org/2015/06/25/yoruba-complete/`; exit 0.
- **CDX:** read `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.cooperhewitt.org%2F2015%2F06%2F25%2Fyoruba-complete%2F&output=json&limit=-5&filter=statuscode%3A200`. It returned captures `20250713022728`, `20251028012346`, `20251117223507`, `20260312202334`, `20260605232422`; all five entries named the live page as `original`.
- **Capture body:** `read` opened the `20260605232422id_` and `20260312202334id_` captures of the same URL; each showed the quote in article body text, not a caption. Ordinary `curl` of the `20260605232422id_` capture returned HTTP 200, 109204 bytes. These are not substitutes for the required locator.
- **Locator on capture `20260605232422id_`:** ran the same locator command with that capture URL three times. Each invocation printed exactly `NOT_LOCATED https://web.archive.org/web/20260605232422id_/https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ URLError`; each exited 1.
- **Locator on capture `20260312202334id_`:** `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260312202334id_/https://www.cooperhewitt.org/2015/06/25/yoruba-complete/' 'create appropriate wraps for different social occasions, and express her personal aesthetic.'` → stdout `NOT_LOCATED https://web.archive.org/web/20260312202334id_/https://www.cooperhewitt.org/2015/06/25/yoruba-complete/ URLError`; exit 1.
- **Network diagnostic only:** a plain `urllib.request.urlopen` diagnostic for the `20260605232422id_` capture returned `HTTPError 429: 'Too Many Requests'` and exited 1. No challenge or access control was bypassed.
- **Duplicate check:** `functions.grep` searched `corpus/SOURCES.md` for `https?://www\.cooperhewitt\.org/2015/06/25/yoruba-complete/` → “No matches found.”

Locator outputs are also recorded with commands in `/fast/scratch/hyaku/kotodama-r63/ScribeRowS708/S708-locator-output.md`; the three draft lines are in `/fast/scratch/hyaku/kotodama-r63/ScribeRowS708/S708-artifacts.md`.

## Touched surfaces, limits, and scope

- This report is the only file this seat wrote under the lane repo. No registry, entry, README, product code, or counter was changed. Scratch artifacts are under `/fast/scratch/hyaku/kotodama-r63/ScribeRowS708/`.
- The first diagnostic `curl` wrote its downloaded body to `/tmp/kotodama-s708-capture.html`; that temporary file was removed with `rm -f` before this report. No tool was installed or updated.
- `ACCEPT-C-63` was not run: this seat supplied one unintegrated row draft, not the complete measured entry/24-row object. No claim verdict is made. S708 is not in the frozen LIVE subset (S694, S698, S702, S706, S710, S714); that does not waive the requested per-source check.
- Claim O, `tools/reopen-row.py`, the O counter, the independent review gate, the remaining C rows, full entry assembly, README/sweep, and full C counter are out of scope for this seat. The held `tools/reopen-row.py` was not run.

## Findings and known limit

The candidate is textually well supported for occasion and personal-aesthetic wording, and the live locator passed. The base locator did not confirm either tested capture despite both capture bodies being visible through ordinary reads; its failure is `URLError`, and the separate urllib diagnostic returned 429. Therefore this seat cannot certify the required live-and-capture locator condition. Treat the row and gate line above as drafts, not a passed sourced row. No installation, counter, integration, or independent-review evidence is claimed.