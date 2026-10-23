# S700 — turban / dastar source report

## Status

**Draft candidate only; not admissible yet.** The selected page provides an in-body quote and the live locator passes. Static reads of Wayback replays also display the quote, but the required base locator did not verify a capture (one `quote-absent`, then `URLError` results); CDX requests were unavailable. Do not count this row or the C LIVE leg as verified until the archive locator succeeds and capture provenance is closed.

## Proposed artifacts

Registry row (11 columns):

```text
| S700 | Identity, Sikh Coalition (page date not shown) - https://www.sikhcoalition.org/about-sikhs/identity/ ; capture https://web.archive.org/web/20261010081315id_/https://www.sikhcoalition.org/about-sikhs/identity/ | docs | A | Sikh Coalition's published framing of the Sikh turban's identity and public ethical meaning; not a cross-tradition history | Identity page, paragraph 3, sentence 2: "the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people." | The Sikh Coalition reports that Sikh Gurus adopted the South Asian royal turban to assert sovereignty and equality; it frames wearing one as a public commitment to service, compassion and honesty. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

Entry bullet:

```text
- The Sikh Coalition says Sikh Gurus adopted the turban as a public assertion of sovereignty and equality for all people (S700)
```

Gate line:

```text
- S700 | https://www.sikhcoalition.org/about-sikhs/identity/ | 2026-10-23 | "the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people."
```

The anchor is 17 normalized words. The proposed clause has at least five content words and shares `sovereignty`, `equality`, `people` in quote order; its longest copied run is below 12 words. Source URL uniqueness search on `corpus/SOURCES.md` for `sikhcoalition\.org` returned **No matches found**.

## Evidence and gates

The live static read of Sikh Coalition's Identity page showed the paragraph-3 sentence: “The turban was historically worn by royalty in South Asia, and the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.” The selected quote is a verbatim substring of that body text, not a caption, alt text or title. Page date is not shown. The scoped A-tier designation is for the Coalition's own published account, not a general history of turbans.

Required live locator command:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.sikhcoalition.org/about-sikhs/identity/' 'the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.'; echo exit=$?
```

Full output:

```text
LOCATED https://www.sikhcoalition.org/about-sikhs/identity/
exit=0
```

CDX lookup attempts for the Sikh Coalition page returned HTTP 429. The ordinary curl attempt was:

```text
curl -sS -L 'https://web.archive.org/cdx/search/cdx?url=www.sikhcoalition.org%2Fabout-sikhs%2Fidentity%2F&output=json&filter=statuscode%3A200&fl=timestamp,original,statuscode&limit=5'
```

Output: `curl: (7) Failed to connect to web.archive.org:443 after 189 ms: Could not connect to server`; exit 7. `read` attempts at the same CDX endpoint (including simplified/non-www, minimal, and date-filtered queries) reported `Failed to fetch URL (HTTP 429)`.

As a fallback discovery—not a successful CDX response—the ordinary archive calendar read at `https://web.archive.org/__wb/calendarcaptures/2?url=https%3A%2F%2Fwww.sikhcoalition.org%2Fabout-sikhs%2Fidentity%2F&date=2026&groupby=day` returned:

```json
{"items":[[107,301,2],[223,200,1],[505,503,4],[926,200,1],[1010,200,1]]}
```

Date-based `id_` replay reads resolved to `20260223105441`, `20260926063946`, and `20261010081315`; each displayed the same Sikh Coalition Identity page, with the selected quote in body text and the embedded original URL matching the live URL. The proposed row uses the latest replay, `https://web.archive.org/web/20261010081315id_/https://www.sikhcoalition.org/about-sikhs/identity/`.

**Capture locator is not passed.** Full locator command outputs:

1. Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260223105441id_/https://www.sikhcoalition.org/about-sikhs/identity/' 'the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.'; echo exit=$?`

```text
NOT_LOCATED https://web.archive.org/web/20260223105441id_/https://www.sikhcoalition.org/about-sikhs/identity/ quote-absent
exit=1
```

2. Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260223105441id_/https://www.sikhcoalition.org/about-sikhs/identity/' 'Perhaps the most visible aspect of the Sikh identity is the turban, which can be worn by men and women alike.'; echo exit=$?`

```text
NOT_LOCATED https://web.archive.org/web/20260223105441id_/https://www.sikhcoalition.org/about-sikhs/identity/ URLError
exit=1
```

3. Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260223105441id_/https://www.sikhcoalition.org/about-sikhs/identity/' 'The turban was historically worn by royalty in South Asia'; echo exit=$?`

```text
NOT_LOCATED https://web.archive.org/web/20260223105441id_/https://www.sikhcoalition.org/about-sikhs/identity/ URLError
exit=1
```

4. Command: `timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20261010081315id_/https://www.sikhcoalition.org/about-sikhs/identity/' 'the Gurus adopted this practice as a way of asserting the sovereignty and equality of all people.'; echo exit=$?`

```text
NOT_LOCATED https://web.archive.org/web/20261010081315id_/https://www.sikhcoalition.org/about-sikhs/identity/ URLError
exit=1
```

**Conflict for the canonical judge:** static `read` replays display the quote in the captured page body; the required base locator did not verify any capture. Preserve the failure; do not upgrade the read output into a locator pass.

Explored but not used: `https://www.iranicaonline.org/articles/dastar-turban` → HTTP 404; `https://www.vam.ac.uk/articles/turbans` → HTTP 404; `https://www.vam.ac.uk/articles/the-sikh-turban` → HTTP 404; `https://www.britannica.com/topic/turban/additional-info#history` → HTTP 403; `https://www.sikhcoalition.org/blog/2017/what-is-a-turban/` → HTTP 404. Britannica's generic turban article opened but was not selected for this Sikh-identity subtopic.

## Touched surfaces and scope

- Lane-repository write: this report only: `.ufo/waves/round-63/w1/ScribeRowS700.md`.
- Scratch artifacts: `/fast/scratch/hyaku/kotodama-r63/ScribeRowS700/registry-row.txt`, `entry-bullet.txt`, `gate-line.txt`, and `locator-outputs.md`.
- No product registry or knowledge-entry edits; no code changes, counter runs, acceptance verdicts, `tools/reopen-row.py` execution, git/jj writes, installs, or O/review work. The L1 integration owner must decide whether to retry the capture verification or choose another source before landing this row.
