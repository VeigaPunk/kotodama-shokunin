# ScoutDocS896 — recon + attack on staged S932 (openstd newGbInfo, Wayback 2026-04-24), planned lane row S896

Seat scratch: `/fast/scratch/hyaku/kotodama-r76/ScoutDocS896/` (deleted at exit; receipts copied to `.ufo/waves/round-76/w1/stage/ScoutDocS896/`). All times of fetch 2026-10-27.

## Verdict: ADMIT the row (tier A, scope = the registry record's own field cells only); the staged entry's §N+1 MUST drop or hedge 4 statements (list below). Live-page claim in the staged row is FALSE.

## 1. Staged material read

`grep -nE '^ {0,3}\|[[:space:]]*S9[0-9][0-9]' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` -> S932 at append line 80 (file line 33 in the filtered list). Staged row says: *"the live record page no longer serves this text; the archived capture does"*, kind docs, tier A, anchor "the 标准信息表 field rows 标准号 / 主管部门", teaches: *"the registry records this standard as GB/T 33661-2017 with 中国科学院 as its 主管部门 — the drafting institution — so a fictional calendar … inherits an authorship chain that runs through the National Astronomical Observatory, not a ministry"*.
Staged entry: `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` (7571 bytes), §N+1 cites S932 (entry line 39).

## 2. Fetches (command, raw output)

```
U='https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'
B='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
curl -sS -L -A "$B"           -D h-browser.txt -o browser.bin -w 'status=%{http_code} bytes=%{size_download} url=%{url_effective}\n' "$U"
curl -sS -L -A 'curl/8.10.1'  -D h-curl.txt    -o curl.bin    -w '…' "$U"
sha256sum browser.bin curl.bin
```
| request | UA | status | bytes (wire) | sha256 (wire) |
|---|---|---|---|---|
| Wayback `…20260424031027id_/…` | browser-shaped (Chrome/130) | 200 | 8075 | `870bd7ad3fcec3745d33766da94ef877877b71b23a5ba9564d9b2aeba5343634` |
| same URL | `curl/8.10.1` | 200 | 8075 | `870bd7ad3fcec3745d33766da94ef877877b71b23a5ba9564d9b2aeba5343634` (identical) |

Headers (browser run): `HTTP/2 200`, `content-type: text/html;charset=utf-8`, `content-encoding: gzip`, `memento-datetime: Fri, 24 Apr 2026 03:10:27 GMT`, `x-archive-orig-date: Fri, 24 Apr 2026 03:10:28 GMT`, `x-archive-orig-content-language: zh`. No challenge/captcha/login: plain GET, nothing bypassed.
Decode: `file browser.bin` -> gzip, original size mod 2^32 24174; `gunzip -c browser.bin > page.html` -> `wc -c` **24174** bytes, sha256 **`f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e`**. Charset: `grep -io 'charset[^"; ]*' page.html` -> `charset=utf-8` (header also utf-8); decoded as UTF-8, no GB18030 needed. (Plain `curl` without `--compressed` stores the gzip bytes; the sha above of the wire bytes is the gz, the HTML sha is the gunzipped.)
The page is server-rendered HTML (JSP, JSESSIONID origin cookie): the field table IS in a plain GET; no JavaScript is needed for it. What JS gates is only the full-text viewer: the page text carries `在线预览提示 … 当前浏览器暂不支持标准全文在线预览服务` and buttons `在线预览 / 下载标准 / 实施信息反馈` — the clause text is not in the page.

Rendered text (scripts/styles/tags stripped, whole 800-char document text) is saved in the window; key lines: `标准号：GB/T 33661-2017`; `中文标准名称：农历的编算和颁行`; `英文标准名称：Calculation and promulgation of the Chinese calendar`; `标准状态： 现行`; `中国标准分类号（CCS） A46`; `国际标准分类号（ICS） 07.040`; `发布日期 2017-05-12`; `实施日期 2017-09-01`; `主管部门 中国科学院`; `归口部门 中国科学院`; `发布单位 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会`; `备注` (empty cell). Also a stale 2022 maintenance banner ("2022年10月28日17点…系统暂时停止访问服务").

### Live URL (attack on "the live record page no longer serves this text")
```
O='https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'
curl -sS -L --max-time 40 -A "$B"          -o live.bin -w 'LIVE status=… bytes=…' "$O"
curl -sS -L --max-time 40 -A 'curl/8.10.1' -o live.bin …
```
- browser UA: `HTTP/1.1 200`, `Content-Type: text/html;charset=utf-8`, bytes **24144**, sha256 `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9`
- curl UA: `HTTP/1.1 200`, bytes **24058**, sha256 `f2297660c13f635bd137d73a7fab6fec90f40c92508cb5f2a125f183a2c21a5c` (per-request byte differences = session/html noise; both UAs served the page)
- Text-stripped live page vs capture text: `diff <(sed 's/^ *//' text.txt) <(sed 's/^ *//' live-text.txt)` -> only the 3 lines of the 2022 maintenance banner differ (present in capture, absent live); every field row is identical. => **the live page DOES serve the same field table to a plain client today.** The staged sentence "the live record page no longer serves this text" is contradicted (observed 2026-10-27). Live-text sha256 `010f6acf3bf703b4a5fea2934b800a0abba761bb5f79bd2df03f55d8068a93b3` (stage/live-text.txt).

### Later capture (to show the page is stable)
`curl -sS -L --compressed -A "$B" 'https://web.archive.org/web/20260710164431id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'` -> `status=200 bytes=8223` (gz wire; decoded size not re-measured), sha256 of the decoded file `8f23f891996f09ff0238c730931f9c6eb21cd029fca83be9ecca0d6611cf23fc`; `grep -c 中国科学院` -> 2; `现行` and `主管部门` present (lines 468, 537).

## 3. Quote location (NFKC + whitespace-folded; folding in comparison only)

Method: python `unicodedata.normalize('NFKC')` + `re.sub(r'\s+',' ')` applied to both page text and quote; `F.find(q)`.

| quote (stored form) | folded chars | whitespace tokens | idx in folded page text | result |
|---|---|---|---|---|
| **`主管部门 中国科学院 归口部门 中国科学院`** (primary quote) | **21** (<=80) | **4** (<=25 words) | 333 | located (in `window.txt` TEXT VIEW and as `<div class="title">主管部门</div><div class="content">中国科学院</div><div class="title">归口部门</div><div class="content">中国科学院</div>`) |
| `标准号：GB/T 33661-2017` | 19 | 2 | 141 | located |
| `标准状态： 现行` | 8 | 2 | 238 | located |
| `发布日期 2017-05-12 实施日期 2017-09-01` | 31 | 4 | 301 | located |
| `中国标准分类号(CCS) A46 国际标准分类号(ICS) 07.040` (full-width parens folded) | 36 | 4 | 264 | located |
| `发布单位 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会` | 37 | 2 | 355 | located |

Absence sweep over the folded page text (`w in F`): `标准信息表` False; `紫金山` False; `天文台` False; `国家天文台` False; `起草` False; `AQSIQ` False; `SAC` False; `Observatory` False; `1秒` False; `农历的编算和颁行` True.

## 4. Sentence-by-sentence verdict on the staged entry's S932 citations

| staged sentence (entry §N+1 / row teaches) | verdict | located span / why |
|---|---|---|
| "the registry records 标准号 GB/T 33661-2017" | **carried** | `标准号：GB/T 33661-2017` idx 141 |
| "标准状态 现行" | **carried** | idx 238 |
| "发布日期 2017-05-12, 实施日期 2017-09-01" | **carried** | idx 301 |
| "CCS A46, ICS 07.040" | **carried** | idx 264 |
| "主管部门 and 归口部门 both 中国科学院" | **carried** | idx 333 (the primary quote) |
| "发布单位 the AQSIQ and SAC" | **carried as full names; abbreviations are the entry's gloss** — page has 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会; `AQSIQ`/`SAC` absent. Keep the Chinese names, drop or mark the abbreviations as gloss. |
| row: "中国科学院 as its 主管部门 — **the drafting institution**" | **paraphrase-beyond-source** — 主管部门 = competent/supervising department; the page has no 起草 (drafter) field. Drop or hedge ("supervising department"). |
| "the promulgation chain runs through the National Astronomical Observatory" | **not carried** — `天文台`/`紫金山`/`国家天文台` absent; the page names 中国科学院 (the Academy), not any observatory; and 主管部门 is not the promulgation chain (发布单位 is AQSIQ + SAC). The 紫金山天文台 drafter claim belongs to S937 (gmw), not S932. Drop from S932 attribution. |
| "a fictional calendar modelled on this standard inherits an authorship chain that starts in an observatory" / row "not a ministry" | **not carried (inference/design advice)** — also tension: 发布单位 is two state bodies (a ministry-level administration + SAC). Drop or label as the lane's own inference. |
| source line "the 标准信息表 field rows" | **label not carried** — `标准信息表` absent; fields are in an unlabelled table + div rows. Rename "the 标准号 / 主管部门 field rows of the record page". |
| row: "the live record page no longer serves this text; the archived capture does" / "withdrawn original" | **false (observed 2026-10-27)** — live URL returns 200 with identical fields; original is not withdrawn. Rewrite: live URL serves the record; Wayback capture is the dated witness. |
| row: "registry … does not serve [clause text] to a plain client" | **carried** (viewer text `当前浏览器暂不支持标准全文在线预览服务`, no clause text in page) |

## 5. Wayback CDX probes (QUALITY 21/24)

All with the browser UA, `web.archive.org/cdx/search/cdx`. (Some connections to web.archive.org failed intermittently with `curl: (7) Failed to connect` — treated as unrun for those attempts, retried with a loop; results below are the successful retries.)
- Canonical: `…cdx?url=openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&output=txt&fl=timestamp,statuscode,digest,length` ->
  ```
  20260424031027 200 PPTOMTSAPKBSVWIDPLD4GQBGD65ML5U3 9022
  20260508002954 - PPTOMTSAPKBSVWIDPLD4GQBGD65ML5U3 720
  20260710164431 200 N76CP7ELHZHOICS2FOQ7KYQPCFNM6DKZ 7885
  ```
  3 captures; the 20260424031027 capture (200) is the staged one; the 20260508 row is a revisit (status `-`, same digest).
- Positive control: `…cdx?url=example.com&output=txt&fl=timestamp,statuscode&limit=3` -> `20020120142510 200 / 20020328012821 200 / 20020524041628 200` (probe path works).
- Negative control (URL that should have none): `…cdx?url=openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=ZZZZZZZZZZ&output=txt&limit=3` -> empty, exit 0 (probe distinguishes presence from absence).
- Availability API: `https://archive.org/wayback/available?url=openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4D…&timestamp=20260424` -> `{"closest":{"status":"200","available":true,"url":"http://web.archive.org/web/20260424031027/https://openstd.samr.gov.cn/…","timestamp":"20260424031027"}}`.
- Neighbour probe (S938 territory, FYI): `cdx?url=openstd.samr.gov.cn/bzgk/std/showGb*&output=txt&fl=original,timestamp,statuscode&limit=5` returned captures of OTHER standards' showGb pages (302/-); it did not answer whether the 33661 showGb page is captured. Not examined further.

## 6. PROPOSED lane registry row (11 columns, no pipe inside a cell)

```
| S896 | 国家标准全文公开系统 / 全国标准信息公共服务平台 (openstd.samr.gov.cn; 主管 国家市场监督管理总局 国家标准化管理委员会) — the registry record page (标准号 GB/T 33661-2017, 农历的编算和颁行): live https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 ; archived capture of the SAME page, 2026-04-24: https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 | docs | A | Tier A for the official registry's own statement of the standard's identity, status, dates, classification and the named 主管部门 / 归口部门 / 发布单位 — what the national standards registry records about its own holding; NOT the clause text (the full-text viewer is not in the page), NOT who drafted the standard (the page has no drafter field), NOT any observatory | the field cells of the record page — the 标准号 / 标准状态 / 发布日期 / 实施日期 / 主管部门 / 归口部门 / 发布单位 rows; quoted span 主管部门 中国科学院 归口部门 中国科学院 | That the registry records this standard as GB/T 33661-2017 (现行; issued 2017-05-12; in force 2017-09-01; CCS A46; ICS 07.040) with 中国科学院 as both 主管部门 and 归口部门 and 中华人民共和国国家质量监督检验检疫总局 plus 中国国家标准化管理委员会 as 发布单位 — and nothing about the drafting body or the clause rules | mined | 2026-10-27 | 180d | corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md |
```
Recheck command (for the row/entry): `curl -fsSL -A '<browser UA>' 'https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296' | grep -c '中国科学院'` -> expected 2 (not run in this form; the capture grep gave the matching count on the decoded capture; live-text diff run as above). Pipe check: the row contains `|` only as the 11 cell separators (12 pipe characters including trailing); verify with the lane census.

## 7. Tier

**A**: operator of the registry is 国家市场监督管理总局 / SAC (主管/主办 stated in page footer text `主管：国家市场监督管理总局 国家标准化管理委员会`); the record is the registry's own statement about its own holding; not community, not a reproduction. Scope limit written into the row: identity/status/dates/department fields only. It is NOT tier A for drafting authorship or clause text.

## 8. Window

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ScoutDocS896/window.txt` — 6680 bytes, sha256 `55ddfece62e5a4e080edca5014cb70266e9182ff4f81718505eb761fa2284500` (= full decoded text view of the whole capture + 4651-char raw HTML of the field table region from `<table … class="mk1"` to the modal; the quote's cells are inside it). Also stage: `capture-decoded.html` (24174 B, sha `f04feb47…1e0e`), `live-text.txt` (sha `010f6acf…93b3`).
`sha256sum` output: window `55ddfece…4500`, capture-decoded `f04feb47…1e0e`, live-text `010f6acf…93b3`.

## 9. Verdict

**ADMIT** (row S896, tier A, mined, scope limited as above) — the quoted span and 5 of the entry's field sentences are carried verbatim by a plain-GET, ordinary-source capture whose CDX presence is confirmed against a working positive and negative control.
Required edits to the staged entry before admission: (1) drop "drafting institution" and "National Astronomical Observatory / observatory authorship chain" from the S932 attribution (page does not carry them; they rest on S937 for 紫金山天文台, and 主管部门 ≠ drafter); (2) drop or mark as inference the "promulgation chain runs through…" and "fictional calendar inherits an authorship chain" sentences; (3) keep AQSIQ/SAC only as gloss of the Chinese 发布单位 names; (4) rename "标准信息表" (not on the page); (5) correct the staged row text claiming the live page no longer serves it.
Flip to REFUSE if: the entry keeps the observatory/drafting sentences attributed to S932; or the row is admitted with a scope broader than the field cells. Flip to UNVERIFIABLE if: the Wayback capture stops resolving AND the live record no longer carries the 主管部门 fields (not the case at 2026-10-27).

Unrun: no GB18030 re-decode (page declares and decodes as utf-8); S938 showGb page not probed beyond the neighbour CDX query; decoded size of the 20260710 capture not measured.
Installs: none.
