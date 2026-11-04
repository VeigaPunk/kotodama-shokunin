# ReviewerRefetch — round 89 w1, claim F independent re-fetch

Seat: ReviewerRefetch (reviewer). Axis: freshness. Milestone r89-v1.
I tested this hypothesis: "each of the 16 claim-F population rows is still supported at its live surface on 2026-11-04". I did not read any other seat's stage.

## Method
- Client: python3 `urllib.request` with UA `kotodama-r89-refetch`. curl was not used. The row URL was fetched first. On 403/429/5xx the client fell back to `https://web.archive.org/web/2026/<url>`. All fetches happened on 2026-11-04 between about 19:07 and 19:09 local time (-03:00).
- Text extraction: HTML went through `html.parser` with script and style dropped. Block tags became newlines and lines were stripped. PDFs went through `pdftotext -layout`. JSON was kept verbatim. Each capture is the full page text, not an excerpt.
- Quote checks used measure89's own `contains` and `quote_ok` functions (`quote_max_words` 25, `quote_min_chars` 20).
- Receipts: `stage/ReviewerRefetch/independent.json` records, per id: url, status, fetched_at, sha256 of the saved .txt, raw_sha256, attempts, verdict, quote, contains and why.

## Per-row verdicts
| id | surface fetched | status | verdict |
|---|---|---|---|
| S009 | cals.info/statistics/ | 200 | SUPPORTED (1323 conlangs / 127 natlangs / 145 features / 97.9% WALS) |
| S012 | arxiv abs 2508.06094 | 200 | SUPPORTED; the page is now **v4** (revised 17 Apr 2026), while the registry locator says "v1" |
| S020 | arxiv abs 2603.19283 | 200 | SUPPORTED (2,670 / 200 / 58,450; 0.85 F1) |
| S021 | arxiv abs 2606.17350 | 200 | SUPPORTED; the page is now **v2** (revised 2 Sep 2026) |
| S031 | PLOS pone.0287101 | 200 | SUPPORTED (50 of 63, 79%; 36 of 41 intentional) |
| S032 | doi → linkinghub → ScienceDirect | redirect stub / 400 / 403; Wayback 2026 = redirect only / 403 | **UNREACHABLE** |
| S033 | PLOS pone.0309543 | 200 | SUPPORTED |
| S084 | signwriting.org | 200 | SUPPORTED ("Sign Languages are written languages!") |
| S104 | glottolog lsfi1234 | 200 | SUPPORTED for existence and naming; FSL/ASL children are drawn by a JS tree that is not in the static HTML (ASL-under-LSFic is confirmed in the S105 capture) |
| S105 | glottolog amer1248.json | 200 | SUPPORTED (classification: Sign Language > L1 > LSFic > ASLic > American Sign) |
| S106 | glottolog bsli1234 | 200 | SUPPORTED |
| S107 | glottolog banz1243.json | 200 | SUPPORTED (newick: Auslanic, BSL, NZSL under BANZSL) |
| S142 | row Wayback URL returned a 200 HTML frame with no PDF text; fetched the live publisher PDF (200) and the Wayback `id_` raw PDF (200) | 200 | SUPPORTED; the two PDFs are byte-identical (raw sha256 ddb27350…) |
| S157 | UNESCO 00172 | 200 | SUPPORTED (2009 4.COM; Biomes: Mountains) |
| S163 | UNESCO 00658 | 200 | SUPPORTED (2017 12.COM, Urgent Safeguarding) |
| S875 | bunka.go.jp heritages search | 200 | SUPPORTED (時代 ladder, 分野 options, 材質・構造・技法 rows) |

Result: 15 SUPPORTED, 0 NOT-SUPPORTED, 1 UNREACHABLE.

## Where the hypothesis fails
- **S032**: the row's live surface does not show the teaching, so the hypothesis fails for this row.
  - What happened: the DOI's HTTP 200 is a "Redirecting" JS stub (`S032.txt`, 11 bytes of text). ScienceDirect returns 400 on `/pii/` and 403 on `/abs/pii/`. Wayback 2026 of the DOI only has the 20261019 capture of the linkinghub 301. Wayback of the ScienceDirect URLs returns 403.
  - Off-surface support: the Crossref API (`S032.crossref.txt`) does support the title-level teaches cell. My quote "Female foragers sometimes hunt, yet gendered divisions of labor are real" passes `contains` against that file. But Crossref is not one of the row's URLs, so under the frozen `url_ok` it cannot back a recheck. Its fetched_at is approximate (file mtime 19:08). I did not log the exact second.
  - L1 action: if an executor's S032 capture contains article content and claims the doi URL or a Wayback capture of it, treat it as suspect. Neither surface served content to me.

## Findings for L1
1. **S142, url_ok vs. what actually serves the PDF.** The frozen `measure89.url_ok` accepts only the exact row URL `https://web.archive.org/web/20250331081615/https://historicbrass.org/…/HBSJ_2008_JL01_002_Cheney.pdf`, or a web.archive.org URL that ends with that exact string.
   - I checked this directly: `url_ok` is False both for the direct publisher URL and for the `20250331081615id_/` raw-PDF URL.
   - With a plain client, the accepted URL returns the Wayback toolbar HTML and none of the paper's text.
   - So an executor S142 capture whose url passes `url_ok` and whose text contains a paper quote was either fetched through a renderer or iframe-follower, or relabelled. Ask what client they used and compare against my `S142.txt` / `S142.wayback.txt` (identical text sha256 e3e679be…).
   - This is a weakness in the frozen counter's design, reported here and not amended.
2. **S142 registry locator is not verbatim.** The locator reads "The style of notation used **by** these hunting signals…". The PDF reads "used **for** these hunting signals appears to be unique to this source". Anyone quoting the locator as written will fail `contains`.
3. **S012 and S021 version drift.** The arXiv pages are now v4 and v2. Their abstracts still support the teaches cells. A LOCATED line should cite the current version rather than "v1".
4. **S104 static HTML.** The page alone does not show the "FSL and ASL classify under it" half of the summary cell. The teaches cell (existence and naming) is supported.
5. **S009 markup.** Percentages are split by markup ("97" / ".9%"). Normalised text still contains "97 9 of all features are from WALS". Quotes with "97.9%" as one token will still match, because the normaliser turns "." into a space.

## How to cross-check
`python3 -c "import sys;sys.path.insert(0,'reports/round-89');import measure89 as m;print(m.contains(open('.ufo/waves/round-89/w1/stage/ReviewerRefetch/<id>.txt').read(), QUOTE))"`

Run this for each executor quote. A False result against a SUPPORTED row of mine means the quote is not on the surface as I fetched it. That is the F-forged-capture defence. Small layout differences are possible for PDFs (`-layout` hyphenation and ligatures such as "ﬁ", which NFKC normalises) and for JS-built pages.

## Commands and results
- `python3 fetch.py` (16 ids): rc=0, every response 200. The S032 200 was a redirect stub and the S142 200 was a Wayback frame.
- S032 and S142 alternative probes (urllib): rc=0. Statuses as listed above.
- S142 PDF capture plus `pdftotext`: rc=0. `cmp` shows the live PDF and the Wayback id_ PDF are identical.
- `python3 build.py` (writes independent.json, checks every quote with `measure89.contains` and `quote_ok`): rc=0, no failed quotes.
- `url_ok` probe for S142 and S032 against base 42816d25 SOURCES.md: rc=0. Output is as stated in finding 1.
- Scratch dir `/fast/scratch/hyaku/kotodama-r89/ReviewerRefetch` removed with `rm -rf` before yield.
- No tools were installed or upgraded. No git or jj mutations, commits or production-file edits.

## Paths written
- `.ufo/waves/round-89/w1/stage/ReviewerRefetch/{S009,S012,S020,S021,S031,S032,S033,S084,S104,S105,S106,S107,S142,S157,S163,S875}.txt`, `S142.wayback.txt`, `S032.crossref.txt`, `independent.json`
- `.ufo/waves/round-89/w1/ReviewerRefetch.md`

## Residual risk
- I fetched once per row. Content that changes by geography or bot detection could differ for other clients.
- The JS-built pages (CALS, Glottolog tree) only expose what is in their static HTML.
