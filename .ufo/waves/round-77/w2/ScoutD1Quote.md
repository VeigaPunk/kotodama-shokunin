# ScoutD1Quote — round 77 / wave 2 — independent reopen + quote-cell fit on D1 (staged S897 → lane S897)

Seat: `ScoutD1Quote` (leaf; no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base: `211f9526800906e0c585d878d265c37e5e090c15`.
Item under attack (dispatch.json): *"Independently reopen D1 ordinary live and archive, bind plain/browser UA separately, locate the exact admission quote and section, compare 2021 post date with article publication metadata, and test whether S897 anchor quote fits the row cell word/char limits."*
Named W1 artifact: `w1/SentinelSources.md` F1 (and the W1 fix it landed in CLAIMS-DRAFT line 14, now reading "Live plain UA HTTP 403 / 162-byte WAF page; browser-shaped UA HTTP 200 / 143252-byte article. Do not claim both UAs were blocked.").
All probes dated **2026-10-27** (UTC Date headers `02:17–02:20 GMT`). Scratch `/fast/scratch/hyaku/kotodama-r77/ScoutD1Quote`, deleted on exit; receipts copied to `w2/stage/ScoutD1Quote/`.

UA strings, bound per request:
- `plain` = `curl/8.23.0` (`curl --version` → `curl 8.23.0 (x86_64-pc-linux-gnu) libcurl/8.23.0 OpenSSL/3.6.5 ...`)
- `browser` = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

**Verdict: claim-C D1 line as amended stands — live browser-UA 200 / plain-UA 403 reproduced verbatim at this seat's probe time; the staged admission quote is verbatim in both live and capture; every surfaced date token agrees on 2021-03-16. Two findings: (F1, LOW) the section label `引言` is functional, not literal — the string occurs 0 times in the page; (F2, INFO) the staged Gate quote is 59 chars / 1 whitespace token, inside both counter caps (≤25 tokens AND ≤80 chars) — but CJK quotes only ever bind on the char cap.**

---

## 1. Reopen — ordinary live, UA split (raw)

```
$ curl -s -D d1-live-plain.hdr -o d1-live-plain.body -A 'curl/8.23.0' --max-time 40 -w '...' 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
plain   code=403 bytes=162 type=text/html effective=http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml redirects=0
$ curl -s -D d1-live-browser.hdr -o d1-live-browser.body -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' --max-time 40 -w '...' 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
browser code=200 bytes=143252 type=text/html effective=http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml redirects=0
```

Plain-UA 403 page is the 162-byte nginx default (`<center><h1>403 Forbidden</h1>` + `Server: nginx` + `Set-Cookie: SF_cookie_1=12669420` — WAF cookie). Browser-UA 200 sets the same `SF_cookie_1` cookie (`15292879`) but serves the article; `X-Frame-Options: SAMEORIGIN`. `%{url_effective}` == requested URL, `redirects=0`, no canonical elsewhere → **no redirect/canonical chase; the page is the target**.

`https://` variant dead under **both** UAs — `code=000 err=Connection timed out after 2000x milliseconds`. `http://` is the only live route.

## 2. Reopen — same-page Wayback capture + CDX (raw)

```
$ curl -s -D d1-cap-plain.hdr -o d1-cap-plain.body -A 'curl/8.23.0' --max-time 60 -w '...' 'https://web.archive.org/web/20240111092427id_/http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
plain   cap code=200 bytes=143457 type=text/html ... redirects=0
$ curl -s -D d1-cap-browser.hdr -o d1-cap-browser.body -A 'Mozilla/5.0 (X11; Linux x86_64) ...' --max-time 60 -w '...' '...same URL...'
browser cap code=200 bytes=143457 type=text/html ... redirects=0
$ sha256sum d1-cap-plain.body d1-cap-browser.body
68c6ed377334199f5372fff16192be71a46e5ffbb6eee71611c3535bae42bf35  d1-cap-plain.body
68c6ed377334199f5372fff16192be71a46e5ffbb6eee71611c3535bae42bf35  d1-cap-browser.body

$ curl -s -A 'Mozilla/5.0 ...' 'http://web.archive.org/cdx/search/cdx?url=lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml&output=json&matchType=exact&filter=statuscode:200'
cdx code=200 bytes=295
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["cn,cssn,lishisuo)/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml","20240111092427","http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml","text/html","200","MRIGYUAH7BQACKUKQCJ5BNS64GWDTXGA","41417"]]
```

Capture `20240111092427` is the **only** status-200 capture of the exact URL — byte-identical under both UAs (no UA-gating at the archive). Matches W1 ScoutCDXPositive exactly.

## 3. Exact admission quote + section location (raw)

Staged S897 Gate quote (from `SOURCES-PROPOSED.md` round-4, `## Gate — S897`):
`「在現代社會中，姓、名共同構成一項人群標記符號。但姓與名實際是有區分的。名的使用要早于姓，兩者組合是一種後起的文化習慣。」— 引言`

```
$ grep -c '<quote>' d1-live-browser.body     → 1
$ grep -c '<quote>' d1-cap-plain.body        → 1
$ grep -n '<quote>' d1-cap-plain.body | cut -d: -f1   → 1404  (raw HTML line)
# tag-stripped text offsets:
live    → quote at text line 242; headings: 一、單名與雙名 L295, 二、漢代南方人名的變化與單名問題 L654, 三、晉宋之際上層雙名的興起及其意義 L1037, 四、結語 L1528
capture → quote at text line 241; same four headings at L294/L653/L1036/L1527
```

The quote sits in the front-matter block before the first numbered section (`一、單名與雙名`), exactly where the `anchor`/`— 引言` label points. Offsets drift by 1 line between live and capture (Wayback injects nothing under `id_`; the 205-byte delta is template-level, not content).

**F1 — LOW (locator precision, not a kill):** the literal string `引言` occurs **0** times in both raw bodies (`grep -c '引言' → 0`, raw and stripped). The page prints no introductory heading — the opening block is unlabeled; the byline (`发布日期：…`) leads directly into paragraph 1. The row's `— 引言` names a *functional* position ("the introductory paragraphs before section 一"), not a printed section title. This matches how prior admitted rows label unlabeled front matter, and the locator is still uniquely resolvable (the quote itself is present 1×, before the sole 一、 heading). Report it as precision debt, not falsification: if the r77 Gate format requires the section label to appear verbatim in the document, the cell should read `— introductory paragraphs before 一、單名與雙名`.

## 4. Post date vs publication metadata (raw)

Three independent surfaces, all `2021-03-16`:

```
$ grep -n '2021-03-16' d1-live-browser.body
50:  <meta name="publishdate" content="2021-03-16">
1387: <div class="riqi">发布日期：2021-03-16 原文刊于： </div>
$ grep -o '202[0-9]-[0-9][0-9]-[0-9][0-9]' d1-live-browser.body | sort | uniq -c
      2 2021-03-16        (no other dates in body)
$ grep -o 'contentid[^>]*' d1-live-browser.body
contentid" content="5318560"        → matches URL token t20210316_5318560
URL path year-month: /202103/t20210316_5318560  → 2021-03-16, contentid 5318560
```

- `<meta name="publishdate" content="2021-03-16">` (machine metadata), visible byline `发布日期：2021-03-16`, URL `t20210316_5318560` — all three agree; the `原文刊于：` (original venue) field is **blank** both live and in the capture, so no earlier-print date contradicts the post date. Staged row/claim date `2021-03-16` is the article's own metadata, not just the URL slug.
- Other meta: `publishedtype=1`, `catalogs=122968`, `author=zhuangxx` (a staff handle, NOT the scholar's name — the scholar 魏斌 appears only in `<title>`/`<h2 class="title1">` and byline-less body). No `og:`/`article:` OpenGraph tags.

## 5. Quote vs row-cell limits (raw)

Counter caps: `MAX_QUOTE_TOKENS = 25`, `MAX_QUOTE_CHARS = 80` — identical in base `reports/round-76/accept-c.py:251-252` (base-read via `git show 211f95…:reports/round-76/accept-c.py`) and W1 counter draft `w1/stage/ExecAdaptC/accept-c.py:186-187`; `quote_ok` = `≤25 whitespace tokens AND ≤80 chars` (both files). `QUOTE_RE` includes the `「…」` bracket class, so the staged `「…」` span is a matchable span.

```
quote raw                                    chars= 59 whitespace_tokens= 1 bytes_utf8=177
gate-line span as QUOTE_RE matches (「…」 interior)   chars= 59 tokens= 1
full gate line ('- quote: 「…」— 引言')      chars= 74 tokens= 4
```

**F2 — INFO (fit verified, with a caveat for the counter):** the S897 anchor quote passes `quote_ok` on both axes (59 ≤ 80 chars; 1 ≤ 25 tokens). The binding leg for any CJK quote is the **character** cap — CJK has no whitespace, so the token leg is vacuous (every CJK sentence counts as 1 token regardless of length). Cross-check: the r76-regression noted in W1 SentinelSources F4 (S903's 124-char English quote) fails the char cap while passing tokens; S897 has no such issue. Note the utf-8 byte length is 177 — if any leg ever measured bytes instead of `len(str)` chars it would fail; observed code uses `len(span)` on the str, correct.

## Findings vs the named item

| seat question | measured | verdict |
|---|---|---|
| reopen D1 ordinary live, plain vs browser UA bound | plain 403/162B WAF page ×1 probe; browser 200/143252B article ×1 probe; both reps consistent with W1's ×2 | **CONFIRMED — UA filter, not a wall** |
| reopen archive (same-page capture + CDX) | capture 200/143457B both UAs, sha256-identical; CDX exact: exactly 1 capture, `20240111092427`, digest `MRIGY…` | **CONFIRMED** |
| locate exact admission quote + section | quote 1× in live + 1× in capture; front matter before 一、單名與雙名 | **CONFIRMED**; section label `引言` is functional — literal string absent (F1) |
| 2021 post date vs article metadata | meta publishdate, visible 发布日期, URL slug all `2021-03-16`; `原文刊于：` empty | **CONFIRMED — no date conflict** |
| S897 anchor quote vs row cell limits | 59 chars / 1 token vs ≤80/≤25 | **PASSES both caps** (F2); char cap is the only binding leg for CJK |

**Net attack result:** no falsifier lands on the D1 adoption path as drafted. The amended D1 line in CLAIMS-DRAFT ("Do not claim both UAs were blocked") is accurate at this seat's probe time. Residual precision debt is F1 (`引言` label) — informational unless the Gate format requires verbatim section names.

## Tooling

No installs; `curl 8.23.0`, `python3`, `grep`, `sha256sum`, `git` already present. Pacman not invoked (paused). No fixture git repos created (none needed — all reads were `git show <base>` / network fetches).

## Receipts (`w2/stage/ScoutD1Quote/`)

```
live-plain.log      live-browser.log     https-probe.log    live-headers.log
capture-fetch.log   cdx.log              quote-locate.log   date-meta.log
date-context.log    quote-caps.log       final-verify.log
d1-live-plain.{hdr,body}  d1-live-browser.{hdr,body}  d1-cap-plain.{hdr,body}  d1-cap-browser.{hdr,body}
cdx-d1.out  cdx.hdr  d1-live-browser.body.txt  d1-cap-plain.body.txt
```

Report: `.ufo/waves/round-77/w2/ScoutD1Quote.md`
