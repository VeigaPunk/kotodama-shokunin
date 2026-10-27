# ScoutDocS898 — recon + attack on staged S937 (gmw.cn 2017-05-23, GB/T 33661) → planned lane row S898

Verdict: **ADMIT (hedged)** — the page is plain server-rendered HTML, opened by ordinary means, and carries every
*rule* sentence the staged entry attributes to S937. It does NOT carry three things the entry sentence/row attach to it
(see §4). Tier: **B** for the rules (not A). Flip: see §9.

Scratch: `/fast/scratch/hyaku/kotodama-r76/ScoutDocS898/` (deleted at exit after receipts copied). All receipts below
are under `.ufo/waves/round-76/w1/stage/ScoutDocS898/`.

## 1. Fetches (every request bound to its UA)

Commands (run 2026-10-27 ~21:33Z, cwd = scratch):

```
U='https://news.gmw.cn/2017-05/23/content_24559485.htm'
BUA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
curl -sS -L -A "$BUA"          -D b.h -o b.bin -w 'browser: %{http_code} %{size_download} %{url_effective}\n' $U
curl -sS -L -A 'curl/8.10.1'   -D c.h -o c.bin -w 'curl: %{http_code} %{size_download} %{url_effective}\n' $U
sha256sum b.bin c.bin
```

Raw output:

```
browser: 200 8076 https://news.gmw.cn/2017-05/23/content_24559485.htm
curl: 200 8076 https://news.gmw.cn/2017-05/23/content_24559485.htm
c46174515531be8754b98767d7e489bab08f09fcea72f262f9bced0f44959b86  b.bin
c46174515531be8754b98767d7e489bab08f09fcea72f262f9bced0f44959b86  c.bin
HTTP/1.1 200 OK ... Content-Type: text/html ... Content-Encoding: gzip ... Server: nginx
b.bin: gzip compressed data ... original size modulo 2^32 25250
```

| request | UA | HTTP | wire bytes | sha256 (wire) | redirects |
|---|---|---|---|---|---|
| 1 | browser-shaped Chrome/130 | 200 | 8076 | c4617451…959b86 | none (url_effective = request URL) |
| 2 | `curl/8.10.1` | 200 | 8076 | c4617451…959b86 | none |

Identical for both UAs; no bot challenge, no captcha, no login. **The server sends gzip even without
`Accept-Encoding`**, so a bare `curl` writes gzip bytes (the registry row's `--compressed` caveat is correct and
must stay). Decoded with `--compressed`:

```
curl -sS -L --compressed -A 'curl/8.10.1' -o c2.html -w '... %{http_code} %{size_download}\n' $U
curl --compressed: 200 8076
670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1  c2.html   (cmp c2.html page.html -> same)
```

Decoded document: 25250 bytes, sha256 `670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1`
(saved `stage/ScoutDocS898/live-page.html`). Charset: `<meta ... charset=utf-8>` (3 matches by
`grep -io 'charset=[a-z0-9-]*'`), file starts with a UTF-8 BOM; decoded `utf-8-sig`, no GB18030 fallback needed.
Fold used for comparison only: NFKC + whitespace removal (the page uses U+3000 ideographic-space paragraph indents).

Row recheck command, re-run: `curl -fsSL --compressed '<URL>' | grep -c '精度应达到1秒'` → `1`;
same command without `--compressed` → `0` (gzip bytes). Row recheck is valid as written.

**Not JavaScript-rendered, not a search form.** A plain GET returns the whole article in `<div id="contentMain">`
(lines 132–138 of the decoded HTML): headline, dateline, five body paragraphs, print-edition line. No table is
claimed for S937 and none is present; the "claimed" content is running prose.

Archived capture of the SAME page (for the source cell, QUALITY 18):

```
curl -sS -L --compressed --retry 3 --retry-all-errors -A "$BUA" -o w.html -w 'wayback id_: %{http_code} %{size_download} %{url_effective}\n' \
  'https://web.archive.org/web/20170523024955id_/http://news.gmw.cn/2017-05/23/content_24559485.htm'
wayback id_: 200 9687 https://web.archive.org/web/20170523024955id_/http://news.gmw.cn/2017-05/23/content_24559485.htm
1a187ee42651e1d0a582e75638a4b4c853a3daa0c321e34ec073b899986801f5  w.html
```

(first two attempts: `curl: (7) Failed to connect to web.archive.org:443` — transient; succeeded on retry 3 of the
second invocation.) UA: browser-shaped, HTTP/2 200. Article text extracted from the 2017 capture and from the live
page are **identical after NFKC+whitespace fold** (`True 722 722`, a python compare of both `contentMain` bodies), and
both contain `精度应达到1秒` and `紫金山天文台起草编制`. So the live page has not drifted since the day-of capture
(capture is 2017-05-23 02:49:55Z, i.e. ~49 minutes after the page's own 02:00 stamp).

## 2. Evidence window

The whole article is 722 characters, < 4096, so the window is the **whole document** (title + source line +
body): `stage/ScoutDocS898/window.txt` — 809 characters, 2286 bytes,
`sha256 057004261dd927bd99ce171a50fad42dd0747b2dba53a0ecfc26f4d4e0f5b9f1`
(`wc -c` = 2286; `sha256sum window.txt` line above). Companion raw receipts in the same dir:
`live-page.html` (670850ea…), `wayback-20170523024955-id_.html` (1a187ee4…), `article_clean.txt` (b31fa71f…).
Body text is built from `<div id="contentMain">` with HTML comments/tags removed; the stored text is not folded.

## 3. Located quote(s)

Primary (carries the compilation rule), located in `window.txt` by NFKC+whitespace fold, exactly 1 hit:

> 规定了朔日为农历月的第一个农历日，包含冬至在内的农历月为农历十一月

- 33 characters (≤80), 99 UTF-8 bytes; token count: 1 whitespace-delimited token (Chinese, no spaces). A word
  segmenter was not run, so the ≤25-word bound is unmeasured; the character count (33) is the measured bound.
- Location: body paragraph 4 of 5 (the paragraph beginning 此次发布的《农历的编算和颁行》), char offset 574 (0-based)
  in `window.txt`, 560 in the folded text. Hits: 1.

Second quote (precision + model), 36 characters, offset 640 in `window.txt` (626 folded), 1 hit, same paragraph:

> 必须按国际天文学规范中关于天体位置计算所规定的模型来计算，精度应达到1秒

Third (drafter), paragraph 5: `国标由国内唯一的历书编算机构，中国科学院紫金山天文台起草编制。` (folded offset 763 for the tail
`紫金山天文台起草编制`, 1 hit).

Per-span fold hit counts (python, folded body): `精度应达到1秒` 1; `朔日为农历月的第一个农历日` 1;
`包含冬至在内的农历月为农历十一月` 1; `紫金山天文台起草编制` 1;
`公开发行的日历产品必须包含公历和农历的日期对照以及二十四节气` 1;
`符合标准规定的编排规则、计算模型和精度及表示方法` 1; `国际天文学标准` **0**.

## 4. Sentence-by-sentence: staged entry vs page

Entry file: `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` (7571 bytes). Rows cited S937: the `source:` line 4 and §N.

| # | staged sentence (S937-attributed) | status | located span |
|---|---|---|---|
| 1 | "the compilation rules fix **how** a lunar date is determined and ordered" | carried | `编排规则明确了农历年月日的确定方法以及排序方法` |
| 2 | "the new-moon day is the first day of the lunar month" | carried | `规定了朔日为农历月的第一个农历日` |
| 3 | "the lunar month containing the winter solstice is the eleventh" | carried | `包含冬至在内的农历月为农历十一月` |
| 4 | "the times of the new moon and the solar terms are computed under the models prescribed by the international astronomy standards" | carried, wording-shifted | page: `朔和节气时刻……必须按国际天文学规范中关于天体位置计算所规定的模型来计算`. `规范` = norms/specifications; "international astronomy standards" is the entry's rendering; the page's literal string `国际天文学标准` is absent (0 hits). Say "international astronomical norms/specifications". Also the page says the models are those *for celestial-position calculation* specifically |
| 5 | "to an accuracy of **1 second**" | carried | `精度应达到1秒` |
| 6 | "a publicly issued calendar must carry the solar–lunar date correspondence and the twenty-four solar terms, conforming to the standard's rules, model, precision and presentation" | carried | `要求公开发行的日历产品必须包含公历和农历的日期对照以及二十四节气，符合标准规定的编排规则、计算模型和精度及表示方法` |
| 7 | "The report also names the drafter: 中国科学院紫金山天文台" | carried | `中国科学院紫金山天文台起草编制` |
| 8 | "the observatory, not a ministry" (row `teaches`, entry §N) | **not carried / paraphrase-beyond-source** — editorial contrast; the page says only that it is `国内唯一的历书编算机构` (the country's only almanac-compiling institution), a fact the entry omits | drop the contrast or attribute it to the lane |
| 9 | entry heading "as announced **on the day it was promulgated**" (and row scope: "as the state press reported it on the day it was promulgated") | **not carried, and in tension with S932 in the same entry** — the page says `国家标准委22日发布了《农历的编算和颁行》等334项国家标准` (SAC announced 22 May 2017, as part of a batch of 334); §N+1 of the same entry cites S932 for `发布日期 2017-05-12`. The page proves a report dated 22/23 May, not the standard's issue date | hedge to "as reported 2017-05-23 (dateline 22 May) in the batch announcement of 334 standards"; do not call it the promulgation day |
| 10 | row `scope`: "the report is the authoritative record of the promulgation" | **not carried** — a newspaper report of a SAC announcement, not the SAC notice/registry record | drop; the registry record (S932) is the authority for issue/implementation dates |
| 11 | §N+1 "promulgation chain runs through the National Astronomical Observatory" | not from S937 (S932-sourced); note the S937 page says 紫金山天文台 (Purple Mountain Observatory) drafted — not the National Astronomical Observatory. Verify S932's 主管部门/归口 reading separately; do not let the S937 sentence conflate the two bodies | outside S937 scope; flagged only |

Sentences the entry must **drop or hedge** for S937: #8 (drop or lane-attribute), #9 (hedge date framing), #10 (drop),
#4 (reword to `规范`/"norms"), and the row's "Tier A" (§7). Everything else (#1–3, 5–7) is carried.

Additional page content the entry does not use but that bounds the claim: the page reports the standard
"首次明确了农历的编排规则、计算模型和精度等" (first time specified) and frames the aim as ending inconsistent
printed calendars (e.g. `2013年的端午和冬至都分别有不同的日期版本`). These are the report's own framing, not clause text —
the entry already correctly says clause text is unread.

## 5. Wayback CDX probe of the canonical URL (QUALITY 21/24)

Probed with the browser-shaped UA, `curl -sS -A "$BUA" -G --data-urlencode "url=<U>" --data-urlencode output=json --data-urlencode limit=5 https://web.archive.org/cdx/search/cdx`:

| probed URL | result |
|---|---|
| `news.gmw.cn/2017-05/23/content_24559485.htm` | HTTP 200, 258 bytes: one row, `20170523024955`, `http://news.gmw.cn/2017-05/23/content_24559485.htm`, text/html, 200, digest `IHP5SRJMWRHJIGMLJVZ4LWLYYUS37MLD`, length 9236 |
| `https://news.gmw.cn/2017-05/23/content_24559485.htm` | same single row (CDX is scheme-normalised) |
| `news.gmw.cn/2017-05/23/content_24559485.htm*` (prefix) | same single row |
| **positive control** `en.wikipedia.org/wiki/Main_Page` | HTTP 200, 872 bytes, 5 rows (2003-12-02 … 2004-02-24, up to limit 5) — the probe method returns captures when they exist |

Availability API: `https://archive.org/wayback/available?url=news.gmw.cn/2017-05/23/content_24559485.htm` →
`{"archived_snapshots":{"closest":{"status":"200","available":true,"url":"http://web.archive.org/web/20170523024955/http://news.gmw.cn/2017-05/23/content_24559485.htm","timestamp":"20170523024955"}}}`.
Result: exactly **one** capture exists (2017-05-23 02:49:55Z); it is the id_ raw form fetched in §1 and is content-equal
to the live page. Both the live URL and the capture are usable, so the row can carry both (the page is still live,
so unlike S932/S935 there is no "live page no longer serves" caveat).

## 6. PROPOSED lane registry row (11 columns, no pipe inside any cell; verified by `python3` split count below)

```
| S898 | 光明日报 (Guangming Daily), 《农历编算有了国家标准 春节端午等假期与其密切相关》, 北京5月22日电 (记者陈海波), 光明网 2017-05-23, 《光明日报》2017-05-23 01版 — https://news.gmw.cn/2017-05/23/content_24559485.htm ; archived capture of the SAME page: https://web.archive.org/web/20170523024955id_/http://news.gmw.cn/2017-05/23/content_24559485.htm — page as served 2026-10-27 (HTTP 200, 8076 bytes gzip on the wire / 25250 decoded, sha256 670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1; plain GET, same bytes for a browser-shaped and a curl UA; the server gzips even without Accept-Encoding, so use --compressed) | docs | B | what the state press reported on 2017-05-23 about the technical content of GB/T 33661-2017《农历的编算和颁行》 (compilation rules, computation precision, issuance requirement, drafting body) as part of the SAC's 22 May announcement of 334 standards — a news report of the standard, not its clause text and not the registry record, so not an authority for issue or implementation dates | body paragraphs 4 and 5 (编排规则明确了…, 精度应达到1秒, 要求公开发行的日历产品必须包含…, 中国科学院紫金山天文台起草编制) | the report states that the standard fixes the new-moon day as the first day of the lunar month and the month containing the winter solstice as the eleventh, requires new-moon and solar-term times to be computed by the models of the international astronomical norms to 1 second, requires published calendars to carry the solar-lunar date correspondence and the twenty-four solar terms, and was drafted by 中国科学院紫金山天文台, which the report calls the country's only almanac-compiling institution; the report does not give the standard's clause numbers or its issue date | mined | 2026-10-27 | 180d | corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md |
```

Verification (run, §10): the row has 11 cells, 0 stray pipes. `recheck` is `180d`; the staged campaign row's
runnable recheck command (`curl -fsSL --compressed … | grep -c '精度应达到1秒'` → 1) was re-run in §1 and still holds.

## 7. Tier — B, not A

Reason: lane `corpus/SOURCES.md` lines 14–19 define A as "primary or authoritative for that scope (spec, official
docs, … maintainer statement…)" and B as "strong secondary". The page is a newspaper report of the SAC announcement;
the primary/authoritative carriers for GB/T 33661-2017 are the standard itself and the SAC/openstd registry record
(S932/S938). The report is strong secondary for the rules (state organ, same-day, unambiguous, content-equal across
nine years of captures) but it does not itself state clause text, clause numbers or the issue date, and its date
framing (`22日发布`) disagrees with the registry's `发布日期 2017-05-12` that §N+1 cites. Scoped A would only hold for
the narrow scope "what Guangming Daily printed", a claim no knowledge sentence needs. Not community, not a
reproduction (it is the original publisher's own page), so B rather than C. Consequence for the claim "no tier-C row is
the sole support": B is unaffected. The staged row's "authoritative record of the promulgation" wording must go.

## 8. Other notes / checks not done

- Word/token count of the ≤25-word bound: **unrun** (no Chinese tokenizer installed; none installed for this task).
  Characters 33 / 36 as counted in python.
- Not opened: the standard's clause text (not needed; the entry already declares it unread), the SAC notice that
  names the 334 standards (would be the primary carrier of the batch date; not searched).
- `<meta name="author" content="石佳">` differs from the byline `记者陈海波` (editor vs reporter); cite the byline as
  printed in the body, as the row does.
- No tools installed or upgraded.

## 9. Verdict and flip

**ADMIT** the S898 row at tier B (used-by the S937-citing entry `…/calendar-festival-systems.amend-2026-10-24.md`),
conditional on the entry's S937-attributed text carrying the §4 edits (#4 reword, #8 drop/lane-attribute, #9 hedge,
#10 drop). **Flip to REFUSE/hold** if the entry (a) keeps "on the day it was promulgated" or "authoritative record"
while also citing S932's 2017-05-12 issue date, or (b) keeps the row at tier A. **Flip to UNVERIFIABLE** only if the
live page and the 2017 capture both stop serving (neither is true on 2026-10-27).

## 10. Pipes check (run)

```
python3: lines starting '| S898 |' in this file -> 1; split on '|' (strip outer pipes) -> 11 cells
cell lengths [6, 579, 6, 3, 376, 80, 564, 7, 12, 6, 81]   (id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by)
```
