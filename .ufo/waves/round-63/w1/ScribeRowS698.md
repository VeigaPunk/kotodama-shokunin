# ScribeRowS698 — S698 source report (round 63, w1)

Date: 2026-10-23. Scope: S698, crown as regalia. This is a source-and-wording report for the L1; it is not a lane integration or ACCEPT-C-63 result.

## Artifacts

Proposed registry row (11 columns):

```text
| S698 | Collins English Dictionary — Complete & Unabridged, HarperCollins Publishers, 2012 Digital Edition (served by Dictionary.com; British noun sense 1) — https://www.dictionary.com/browse/crown ; capture https://web.archive.org/web/20260412094355id_/https://www.dictionary.com/browse/crown | docs | A | lexical definition of crown as sovereign headgear and materials (British noun sense) | British noun sense 1: "an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones" | Collins defines a crown as sovereign ornamental headwear and describes gold and precious-stone materials | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

Proposed entry bullet:

```text
- A crown symbolizes sovereignty in gold and precious stones. (S698)
```

Gate line:

```text
- S698 | https://www.dictionary.com/browse/crown | 2026-10-23 | "an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones"
```

The Collins British noun sense 1 quote is 13 normalized words and appears as body definition text (not a caption, alt text, title, or meta description). Tier A is scoped to the dictionary's own lexicographic definition, not broader historical or cross-cultural practice. The entry clause has six content words; four appear in quote order (sovereignty, gold, precious, stones); the longest exact copied run is two words (“precious stones”).

## Evidence and commands

- Ordinary `read` opened the live Dictionary.com page and the selected `id_` archive page. The live and archived page bodies display the Collins British entry and the exact definition quote. The page attribution identifies Collins English Dictionary — Complete & Unabridged, 2012 Digital Edition, and HarperCollins.
- CDX request read: `http://web.archive.org/cdx/search/cdx?url=www.dictionary.com/browse/crown&output=json&limit=-5&filter=statuscode%3A200`. It returned five status-200 captures, each with `original` exactly `https://www.dictionary.com/browse/crown`: 20240407171410, 20240419000931, 20250610184908, 20260212065754, 20260412094355. The selected `id_` capture is the latest in that result set and embeds the same original URL as the live page.
- URL reuse check: exact URL `https://www.dictionary.com/browse/crown` searched in `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` → `No matches found`.
- Final live locator, run from the lane root with `timeout 300`:
  - Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.dictionary.com/browse/crown' 'an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones'`
  - Full stdout: `LOCATED https://www.dictionary.com/browse/crown`; exit 0.
- Final capture locator, run from the lane root with `timeout 300`:
  - Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260412094355id_/https://www.dictionary.com/browse/crown' 'an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones'`
  - Full stdout: `NOT_LOCATED https://web.archive.org/web/20260412094355id_/https://www.dictionary.com/browse/crown HTTPError`; exit 1. This is not a quote-absence result. The independent reviewer reports HTTP 429 Too Many Requests from the archive locator request; the capture body was nevertheless fetched and verified by ordinary means.
- Independent review report: `.ufo/waves/round-63/w1/RevRowS698.md`, lines 15–16, 28–36, 39–48, records `VERDICT: SUPPORTED` (with capture-transport caveat), live locator `LOCATED`, a direct 81,772-byte capture fetch containing the Collins quote once in the body definition, the same-page Collins citation, and the locator's archive 429. Reviewer reports one plain `curl/8.5.0` capture request returned status 200 (13,803 bytes); no cryptographic digest was supplied.
- Access difference: my ordinary default-curl GET command `curl -sS -L -o /dev/null -w 'HTTP %{http_code}\n' 'https://www.dictionary.com/browse/crown'` printed `HTTP 403`; the prescribed locator's ordinary fixed desktop User-Agent located the live quote. The independent reviewer reports their ordinary curl fetch of the live page was HTTP 200. This is recorded as a method-specific access difference; no browser, login, challenge-solving, or challenge bypass was used.

Additional exploratory locator outcomes, kept separate from the final quote:

- The American Dictionary.com sense quote `any of various types of headgear worn by a monarch as a symbol of sovereignty, often made of precious metal and ornamented with valuable gems.` located on live (`LOCATED https://www.dictionary.com/browse/crown`, exit 0); its archive probes did not pass (HTTPS `URLError`, HTTP `quote-absent` for the selected capture; older 2024/2026-02 capture probes returned `URLError` or `HTTPError`). This quote was not selected; the Collins British quote is narrower and the final reviewer verified it.
- Alternate Historic Royal Palaces page `https://www.hrp.org.uk/tower-of-london/history-and-stories/the-crown-jewels/`: the materials quote locator returned `NOT_LOCATED https://www.hrp.org.uk/tower-of-london/history-and-stories/the-crown-jewels/ HTTPError`, exit 1; the `20261017093616id_` capture locator returned `NOT_LOCATED … URLError`, exit 1. Page/capture body text was readable, but this candidate was not selected because the final live Dictionary.com quote locates.

## Rejected candidates

- Britannica `https://www.britannica.com/topic/crown-regalia` and `/topic/crown-headgear`: ordinary reads returned HTTP 404; the queried CDX results were empty.
- Britannica `https://www.britannica.com/topic/crown`: ordinary read returned HTTP 403 and the queried CDX result was empty. `https://www.britannica.com/art/crown-headgear` returned HTTP 404.
- Met Heilbrunn `https://www.metmuseum.org/toah/hd/croi/hd_croi.htm`: ordinary read returned HTTP 429; its CDX request also returned HTTP 429.
- Royal Collection Trust trail URL `https://www.rct.uk/collection/themes/trails/the-crowns-of-the-royal-collection` and object URL `https://www.rct.uk/collection/31700/the-imperial-state-crown`: ordinary reads returned HTTP 404; CDX for the object URL returned HTTP 429.
- An initial plain `curl -sS` CDX request for the HRP page was automatically moved to a background job by the tool after an incoming-message interrupt; it completed with HTTP 429 before the cancellation attempt reported the job already completed. No job remained running. A subsequent ordinary `read` CDX request returned five status-200 captures for that page.

## Gates, touched surfaces, and limits

- S698 source, URL uniqueness, body quote, quote length, and entry-line thresholds were manually checked; live locator passed. Independent blind-support verdict is `SUPPORTED` as recorded in the reviewer artifact above.
- Capture quote is verified in the archive body by `read` and the independent reviewer, but the canonical locator-on-capture did not pass during this window because archive.org returned HTTP 429. Mark this `met-not-passed` for the locator-on-capture check (transport limitation, not quote absence); do not report it as a locator pass. The reviewer notes the frozen C LIVE subset uses the live URL and that the live locator passes for S698. No `reports/round-63/accept-c.py` run was performed, so no `ACCEPT-C-63` verdict is claimed.
- Touched surfaces: this requested report and scratch note `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS698/S698.md` only. No registry or knowledge-entry file, product code, judge, or counter was changed.
- Out of scope / not performed: O repair or review gate; S694–S717 integration; counter/control runs; build, tests, lint, commit, push, publish, or deploy; package installs (none).
