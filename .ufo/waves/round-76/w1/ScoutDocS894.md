# ScoutDocS894 — National Archives of Japan 詳細検索 (planned lane row S894; entries c and a)

Verdict: **ADMIT** (scoped), with sentence-level drops for entry a and hedges for entry c. Receipts: `.ufo/waves/round-76/w1/stage/ScoutDocS894/` (window.txt, 4 header files, cdx-canonical.txt). Scratch `/fast/scratch/hyaku/kotodama-r76/ScoutDocS894/` (deleted at exit). No installs.

## 1. Fetches (every request, UA bound to its response)

Commands (run in the scratch dir; `B` = browser-shaped UA from the assignment; plain UA string set explicitly as `curl/8.10.1`):

```
curl -sS -L -A "$UA" -D live-$n.hdr -o live-$n.html -w "live $n status=%{http_code} bytes=%{size_download} url=%{url_effective}\n" https://www.digital.archives.go.jp/search
curl -sS -L -A "$UA" -D wb-$n.hdr   -o wb-$n.html   -w "wb $n status=%{http_code} bytes=%{size_download} url=%{url_effective}\n" "https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search"
```

Raw output:

```
live browser status=200 bytes=311308 url=https://www.digital.archives.go.jp/search
204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8  live-browser.html
wb browser status=200 bytes=307700 url=https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search
c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0  wb-browser.html
live curl status=200 bytes=311308 url=https://www.digital.archives.go.jp/search
204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8  live-curl.html
wb curl status=200 bytes=307700 url=https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search
c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0  wb-curl.html
```

| request | UA | status | bytes | sha256 |
|---|---|---|---|---|
| live | Mozilla/5.0 (X11; Linux x86_64) … Chrome/130.0 Safari/537.36 | 200 | 311308 | 204b7188…763ea8 |
| live | curl/8.10.1 | 200 | 311308 | 204b7188…763ea8 (same bytes) |
| Wayback 20260422145052id_ | browser UA | 200 | 307700 | c015e1dc…8a13e0 |
| Wayback 20260422145052id_ | curl/8.10.1 | 200 | 307700 | c015e1dc…8a13e0 (same bytes) |

Headers (saved, sha256: live-browser 7536fb89…, live-curl 01c4d1b5…, wb-browser 4841d49a…, wb-curl b50da73f…): live `HTTP/2 200`, `content-type: text/html;charset=UTF-8`, `server: Apache`, via CloudFront (`x-cache: Miss from cloudfront`); Wayback `memento-datetime: Wed, 22 Apr 2026 14:50:52 GMT`, `x-archive-src: CC-MAIN-2026-17-…warc.gz`, `link: <https://www.digital.archives.go.jp/search>; rel="original"` — the capture is of the SAME URL. No bot challenge, captcha, login or geo gate met on either UA (cookie set only: AWSALB/JSESSIONID). Charset: `file` → "HTML document, Unicode text, UTF-8"; header says UTF-8; decoded UTF-8, no GB18030 question (Japanese page). Folding: NFKC+whitespace in comparison only; stored window is unfolded.

The live bytes (311308, prefix sha 204b7188…) equal the round-68 hand-check record for the same URL (`git show 98c486b:.ufo/waves/round-68/assimilation/quarantine-handcheck.json` lines 214-225: `"status": "200 311308 text/html;charset=UTF-8 …", "sha256": "204b7188493573f8", "bytes": 311308`) — page byte-stable across rounds.

## 2. What a plain GET returns (not JS-rendered for this text)

Title: `grep -o '<title>[^<]*</title>'` → `<title>詳細検索 | 国立公文書館デジタルアーカイブ</title>`. It IS a search form, but the era table is **static HTML inside the served bytes**: a hidden modal `<div id="gengo-modal" class="gengo-modal is-hidden">` with heading `元号選択`, three tabs 和暦元号 / 中国元号 / 朝鮮元号, each a `<table class="gengo-modal__table">` with `<th>元号名称</th><th>開始西暦年</th>` and `<td>` rows each carrying a button `data-gengo-label="文治" data-eracode="107" data-yyyy="1185"`. The modal opens from the form row 年月日(元号) (hidden input `date_e_from_era`, button `元号選択`). A separate `<select name="date_e_to">` carries only five options (明治 1868, 大正 1912, 昭和 1926, 平成 1989, 令和 2019). No JavaScript execution needed; the table IS in the plain-GET text.

Parse (Python regex over the served HTML, rows = `<tr>` cells, both pages):

```
rows identical live vs wb: True
wa  : 248 data rows + header; first 令和 2019, 平成 1989, 昭和 1926, 大正 1912, 明治 1868, 慶応 1865, 元治 1864 …; last 朱鳥 686, 白雉 650, 大化 645
chu : 94 data rows (康徳 1934 … 金収国 1115)
cho : 8 data rows (朝鮮乾隆 1736 … 朝鮮永楽 1403)
令和 2019 / 平成 1989 / 昭和 1926 / 大正 1912 / 明治 1868 / 慶応 1865 / 文治 1185 / 大化 645 : all True against the staged values
sentinel counts (raw, live and wb alike): 元号名称 = 3, 開始西暦年 = 3 (grep -c lines: 3 and 3); 詔勅 = 0, 勅令 = 0, 勅書 = 0; 文治 = 3, 1185 = 2
```

## 3. Located quote

- Quote (NFKC + whitespace folded, button label 「選択」 between cells removed in the comparison; cell text read in table order): `元号名称 開始西暦年 令和 2019 平成 1989 昭和 1926 大正 1912 明治 1868` — **50 characters, 12 whitespace tokens** (≤80 chars, ≤25 words). This is exactly span 1 of the lane's own round-68 quarantine record (`quarantine-handcheck.json` S825 spans[0]).
- Without removing the button label, the contiguous rendering is `元号名称 開始西暦年 令和 2019 選択 平成 1989 選択 昭和 1926` — 40 characters, 10 tokens.
- Location: live HTML, character offset 106247 (first `元号名称`, 和暦元号 tab, `thead` of `table.gengo-modal__table` inside `#gengo-modal`); offset 237900 (中国元号); 288656 (朝鮮元号). In `stage/ScoutDocS894/window.txt` the heading begins at offset 2043 (one token per line there; folded match `fold(window).replace(' 選択','').find(q)` → 2043, `True`).
- Window: `window.txt` — 6015 characters, sha256 `2260bb9f9f55497258016c6505ea4d19319c4b5bd9597dc542bda6b6a3caa680` (`sha256sum`). Tags-stripped visible text from form row 年月日(元号) to end of the 朝鮮元号 table, whole 和暦 table included. (The window is derived text; the byte-level parent is the 311308-byte live GET.)
- Span 2 of the staged S908/S825 pair, `元号名称／開始西暦年` (full-width slash): **NOT in the page**: `'元号名称／開始西暦年' in raw: False; NFKC-fold: False; '元号名称/開始西暦年' folded: False`. The page has two separate `<th>` cells; the slash-joined heading is the campaign's own composite label (round-68 handcheck: `"found": null` for that span). Do not quote it.

## 4. Staged sentences vs the page

Entry c (`era-periodization-models.amend-2026-10-23b.md`, S908):

| sentence | verdict | span |
|---|---|---|
| "the National Archives of Japan's detailed-search form carries an era-name table mapping 令和 (2019), 平成 (1989), 昭和 (1926), 大正 (1912), 明治 (1868), 慶応 (1865) … 文治 (1185) and onward to the earliest names" | **carried** (和暦 table to 大化 645; the page also carries 中国元号 94 and 朝鮮元号 8 rows the entry does not mention) | rows above |
| "so that a catalogue search can be bounded by era" | **paraphrase-beyond-source (mild)**: the page offers 元号選択 as a date-range helper on 年月日(元号) (`date_e_from_era`) but states no purpose; hedge: "offers an era picker for date fields" | form row 年月日(元号) |
| "how an archive actually dates what it holds, as distinct from how a library classifies" / "an institution that bounds a search by era name and year is showing how a period vocabulary is actually used" (S908 row teaches) | **not carried**: page is a form widget with no statement about how holdings are dated; the form also has a Gregorian 西暦 date type; hedge as inference | — |
| "the archive's own search instrument / tier A for its era-name table as applied in its catalogue" | carried only as "a table the archive's search form lists"; "applied in its catalogue" not shown | — |
| `§N+1 Four period axes…` (library ladder / museum periods / heritage ladder) | not from this page (out of S908's scope; other rows) | — |
| S908 recheck `grep -c '元号名称' -> 3` | **reproduces** (3 on live) | — |

Entry a (`calendar-festival-systems.amend-2026-10-24.md`, S935 §N+2):

| sentence | verdict |
|---|---|
| "the national archives' own **詔勅・勅令・勅書 database** lists each era name with its start year" (source line, `sources:` paragraph, S935 row descriptor "the 詔勅・勅令・勅書 database") | **NOT CARRIED, drop**: `詔勅`, `勅令`, `勅書` each count 0 in both the live and the 2026-04-22 bytes; the page is 国立公文書館デジタルアーカイブ 詳細検索 across all holdings |
| "lists each era name with its start year — 明治 1868, 大正 1912, 昭和 1926, 平成 1989, 令和 2019" | **carried** (also in the `date_e_to` select) |
| "a culture adopting an era-name system has a citable precedent for the *form* (name + start year)" | carried as form of the table (name + start year); the "precedent" framing is the entry's own inference |
| "and for where the naming authority sits" (and S935 "the archive is the authoritative source for its own holdings"/"naming authority") | **NOT CARRIED, drop or hedge**: the page names no authority for era names; it is a picker |
| S935 row: "**the live search page no longer serves this text; the archived capture does**" | **FALSE as of today**: live GET 2026-10-27 returns it (3 × 元号名称). Drop the sentence and the "withdrawn original" wording; same document, one row |
| S935 recheck "`grep -c '開始西暦年'` -> 1 (ran 2026-10-24…)" | **does not reproduce**: `grep -c` over the Wayback bytes = 3 (and 3 on live). Fix to `-> 3` |
| §N+2 "so the lane has an era-name table it can check" | carried |

Sentences to drop/hedge: (a) "詔勅・勅令・勅書 database" everywhere (entry a front matter, `sources:`, §N+2, S935 row); (b) "where the naming authority sits"; (c) "live page no longer serves"; (d) S935 recheck count 1→3; (e) c: "dates what it holds", "applied in its catalogue", "bounded by era" → hedge to "offers an era picker for date fields"; (f) never quote `元号名称／開始西暦年`.

## 5. Wayback CDX probe (QUALITY 21/24)

Commands, probed URLs and raw output (`curl -sS -A "$B" 'https://web.archive.org/cdx/search/cdx?url=…&output=txt&fl=…'`; an earlier try returned `curl: (7) Failed to connect to web.archive.org:443` for 3 of 5 requests — transient, retried with 3s sleep and answered):

Canonical `url=digital.archives.go.jp/search` (13 captures, status 200 bytes=739):
```
20120602150945 404 …  20260302155700 404 …  20260304154446 301 …  20260304164243 404 …
20260325054802 403 …  20260422145052 200 DZ2PGRHTWUTPSMWFQZANJJWH2STP2UI4 31794
20260526044439 403 …  20260629040938 403 …  20260712052824 200 EP5IHEYTCOW4RKDQ5NUB3ICFOP4VDL5O 32004
20260806161727 403 …  20260908142230 403 …  20261003150501 200 2DF5KEX4EAGRBRZUSZDPIE3OOIV7ESO7 31917
20261014075835 403 …
```
(full raw in `stage/ScoutDocS894/cdx-canonical.txt`, sha256 5f0dfce3…767ccd). Variant `www.digital.archives.go.jp/search&limit=3`: `20120602150945 404 …/search/`, `20260302155700 404`, `20260304154446 301`. `https://archive.org/wayback/available?url=digital.archives.go.jp/search` → `{"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20261003150501/…"}}`.
Positive control `url=example.com&limit=3` → `20020120142510 200 http://example.com:80/` etc. (status 200, 134 bytes): CDX answers for a URL known to have captures, so the canonical result is a real positive, not an endpoint failure. Three 200 captures exist (2026-04-22, 2026-07-12, 2026-10-03); the 2026-04-22 one is the capture the staged row cites and I fetched; 7 of 13 captures are 403/404 crawls — direct fetches today got 200 on both UAs, so no gate was met. The 2026-04-22 capture's era rows equal live's (`rows identical: True`).

## 6. Prior-art flags for the L1 (draft-claim attack)

1. **CLAIMS-DRAFT "Before" check is false at base**: `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` prints `98c486b:corpus/lessons/round-68.md` (exit 0). Line 112 reads "S825 (digital.archives.go.jp/search is a portal landing, not the table page)" — the lane refused this page in round 68 as "not the table page"; the round-71 hand-check (`git show 98c486b:.ufo/waves/round-71/w1/ScoutQuarantineFetch3.md` line 7) later found the table PRESENT. Today's evidence: the table is in the plain GET; the round-68 refusal reason does not reproduce. The Before command must be changed (e.g. `… -- corpus/SOURCES.md corpus/knowledge`, which prints 0 matches in SOURCES.md: `git show 98c486b:corpus/SOURCES.md | grep -c 'archives.go.jp'` → `0`) or the claim must say "corpus holds only a refusal note".
2. Lane registry is `corpus/SOURCES.md` (not top-level): header at line 28 `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`, 817 rows, last id S893 (`grep -cE '^\| S[0-9]+ '` → 817; `tail -1` of ids → S893).
3. Two campaign ids S908 and S935 are ONE document (same URL; capture is the same page) → one lane row S894, as the CLAIMS-DRAFT plans.

## 7. PROPOSED lane registry row (11 columns, no pipe in any cell)

```
| S894 | 国立公文書館デジタルアーカイブ 詳細検索 (National Archives of Japan, digital archive detailed search form; era-picker modal 元号選択) - https://www.digital.archives.go.jp/search ; capture of the same page: https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search | docs | A | Tier A for **which era names and start years the National Archives of Japan's own search form offers for its 年月日(元号) date filter**: the 和暦元号 list (248 names, 令和 2019 to 大化 645) plus 中国元号 (94) and 朝鮮元号 (8). Tier A does **not** extend to how the archive dates holdings, to any statement that the archive is the naming authority for era names, or to the 詔勅・勅令・勅書 database (the page does not mention it) | modal #gengo-modal, tables headed 元号名称 and 開始西暦年 (rows 令和 2019, 平成 1989, 昭和 1926, 大正 1912, 明治 1868, 慶応 1865, 文治 1185, 大化 645); served in a plain GET, no JavaScript needed; live 2026-10-27 and the 2026-04-22 capture carry identical rows | That a national archive's search form pairs each era name with a western start year (name + start year) and offers the pick as a date-range helper, with the Japanese list running to 645 and separate Chinese and Korean era lists; a citable precedent for the form of an era-name table, not a statement of who names eras | mined | 2026-10-27 | 180d - `curl -fsSL -o s.html 'https://www.digital.archives.go.jp/search'` then `grep -c '元号名称' s.html` -> 3 (ran 2026-10-27; live and the 2026-04-22 capture both 3) | corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md, corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md |
```
Check: cells separated by exactly 11 pipes boundaries; the recheck cell contains no pipe (two-step command instead of a pipeline).

## 8. Tier

**A**, scoped as above: an institution's own web instrument publishing its own list (primary for "what the archive's form offers"); not community, not a reproduction. Reason for the scope limit: the page is a UI picker, so it is primary only for its own list; it asserts nothing about era authority or dating practice. S935's tier-A wording "authoritative source for its own holdings" is not shown on the page and should be dropped.

## 9. Verdict

**ADMIT** the document as one row S894 (live URL + the 2026-04-22 capture of the same page). Entry c can admit with the hedges in §4; entry a's §N+2 can admit only after dropping "詔勅・勅令・勅書 database", "naming authority" and "live page no longer serves"; with those sentences kept the entry would carry claims the page does not make (flip to REFUSE for entry a if the source line `詔勅・勅令・勅書` is kept). If the live page later stops serving the modal, the capture 20260422145052 remains and the row stays admissible on the capture. Unrun: no fetch of the 2026-07-12/2026-10-03 captures' era rows (only the 2026-04-22 capture was fetched).
