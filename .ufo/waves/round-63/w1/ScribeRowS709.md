# ScribeRowS709 — Round 63

## Result

Prepared the S709 registry row, one entry bullet, and Gate line for L1 integration. The selected source is the Birmingham Museum of Art's primary collection record, **Hat (kufi)**. It identifies the object as probably Yoruba, from Ogbomosho, Nigeria, dated 1967, and records a purchase from the hat-maker. The cited quote is the visible `Provenance` body field, not image caption/alt/title text or a search snippet.

The evidence supports this one catalogued object's identity and provenance only. It does **not** establish general kufi use for prayer or formal dress; the drafted entry wording is limited to the record.

## S709 artifacts

Registry row:

```text
| S709 | Hat (kufi), Birmingham Museum of Art, 1967 object record (page modified 2026-05-20) - https://www.artsbma.org/collection/hat-kufi/ ; capture https://web.archive.org/web/20230330120744id_/https://www.artsbma.org/collection/hat-kufi/. | docs | A | catalogue identification and provenance of one kufi recorded in Ogbomosho, Nigeria; not a general usage claim | Provenance, "Purchased by the donor and her husband from the hat-maker in 1967 in Ogbomosho, Nigeria" | the museum records a 1967 purchase from the Ogbomosho hat-maker and lists the kufi as probably Yoruba (AFI.427.2010) | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

Entry bullet:

```text
- The museum records a kufi's purchase from the hat-maker in 1967 in Ogbomosho, Nigeria (S709)
```

Gate line:

```text
- S709 | https://www.artsbma.org/collection/hat-kufi/ | 2026-10-23 | "Purchased by the donor and her husband from the hat-maker in 1967 in Ogbomosho, Nigeria"
```

Manual shape check: the quote normalizes to 16 words (within 8–25). The entry clause has at least five content words of four or more letters; `maker`, `1967`, `Ogbomosho`, `Nigeria` appear in quote order, with a nine-word copied sequence at most (under the 12-word cap); it contains one S-id. The row follows the 11-column pattern, uses the required status/opened/recheck/used-by values, and lists the live URL followed by an `id_` capture whose CDX original URL is exactly the live URL.

## Locator evidence and gates

CDX query used through the read tool:

`https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.artsbma.org%2Fcollection%2Fhat-kufi%2F&output=json&limit=-5&filter=statuscode%3A200`

It returned (timestamp | original | status):

```text
20210927015728 | https://www.artsbma.org/collection/hat-kufi/ | 200
20220122002254 | https://www.artsbma.org/collection/hat-kufi/ | 200
20220812003507 | https://www.artsbma.org/collection/hat-kufi/ | 200
20230330120744 | https://www.artsbma.org/collection/hat-kufi/ | 200
20240619015814 | https://www.artsbma.org/collection/hat-kufi/ | 200
```

The live page and selected 20230330120744 capture were opened by ordinary read. Both display the quoted provenance text. The exact locator command and full output for the live URL:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.artsbma.org/collection/hat-kufi/' 'Purchased by the donor and her husband from the hat-maker in 1967 in Ogbomosho, Nigeria'; echo exit=$?
LOCATED https://www.artsbma.org/collection/hat-kufi/
exit=0
```

Selected same-page capture:

```text
timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20230330120744id_/https://www.artsbma.org/collection/hat-kufi/' 'Purchased by the donor and her husband from the hat-maker in 1967 in Ogbomosho, Nigeria'; echo exit=$?
LOCATED https://web.archive.org/web/20230330120744id_/https://www.artsbma.org/collection/hat-kufi/
exit=0
```

A later CDX-listed capture (20240619015814) also displayed the quote when opened, but its locator returned `NOT_LOCATED ... HTTPError` (exit 1); the earlier capture above was used after its locator passed.

URL reuse checks: grep of `corpus/SOURCES.md` for `artsbma.org/collection/hat-kufi` returned no matches; grep of the current `.ufo/waves/round-63/w1` reports returned no matches.

## Rejected candidates and limits

- `https://www.britannica.com/topic/kufi` — ordinary read returned HTTP 404; no quote used.
- `https://collections.rom.on.ca/objects/464022/cap-kufi` — ordinary read returned HTTP 403; no quote or row used.
- Smithsonian National Portrait Gallery page `https://npg.si.edu/about-us/press-release/portrait-yarrow-mamout-on-view-national-portrait-gallery-0` — ordinary read returned HTTP 403. A Wayback capture opened with read and displayed a relevant body quote, so this is recorded as **met-not-passed** for the source-access exception; it was not selected because the live and capture locator attempts returned HTTPError rather than LOCATED. A later archive capture also displayed the quote, but its locator likewise returned HTTPError. The first CDX read returned HTTP 429; a plain `curl` attempt failed to connect (HTTP 000, exit 7). No challenge was bypassed.
- The 20240619015814 Birmingham capture above — quote visible by read, but locator HTTPError; replaced by the CDX-listed 20230330120744 capture, which locates.

The complete failed-candidate commands and outputs, CDX query details, and selected page notes are preserved in the scratch `locators.txt` artifact listed below.

## Gates, touched surfaces, and out of scope

- **S709 source gate:** live locator PASS; selected capture locator PASS; page/capture original URL match; current registry and wave-report uniqueness searches found no existing use. Manual row/entry constraints checked above.
- **ACCEPT-C-63 predicate and all other counter/review gates:** not run or judged by this seat. These row materials are not an acceptance receipt.
- **Touched lane surface:** this report only, `.ufo/waves/round-63/w1/ScribeRowS709.md`. The registry and knowledge entry were not edited; L1 integrates the row and bullet.
- No product-code changes, git/jj writes, commit, push, deployment, installs, or tool updates. No browser or challenge bypass used.

## Artifact paths

Scratch directory: `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS709/`

- `row.txt`
- `entry.txt`
- `gate.txt`
- `locators.txt`
- `summary.txt`

Report path: `.ufo/waves/round-63/w1/ScribeRowS709.md`
