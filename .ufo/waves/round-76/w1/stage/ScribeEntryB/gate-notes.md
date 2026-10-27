# Gate notes — candidate b, ScribeEntryB (round 76, wave 1)

Seat: ScribeEntryB. Target: `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24-r10.md`.
Lane id cited: **S897** (planned: openstd showGb route family). Campaign id S938 is not cited anywhere in the
draft. Access date for every record below: **2026-10-27**. Scratch: `/fast/scratch/hyaku/kotodama-r76/ScribeEntryB/`
(deleted after receipts copied here).

## Fetch log (each UA bound to the response it produced — QUALITY 22)

UA-A = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` (browser-shaped)

| # | request | headers | result | bytes | hash |
|---|---|---|---|---|---|
| F1 | GET `/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296` | UA-A, no Referer, no cookie | 302, `Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter` | 0 | — |
| F2 | GET same as F1 with `type=download` | UA-A, no Referer, no cookie | 302, same `Location` | 0 | — |
| F3 | GET the F1 redirect target, following `-L` | UA-A | 200 `text/html;charset=utf-8` | 24,144 | sha256 `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9`, md5 `e866bfd61a16f4c4fcdc1fc3a16bdf89` |
| F4 | GET F1 target again, same command | UA-A | 200 | 24,144 | identical bytes (`cmp` → IDENTICAL) |
| F5 | GET F1 target with `Accept-Language: zh-CN,zh;q=0.9` | UA-A | 200 | 24,144 | identical bytes |
| F6 | GET `/bzgk/std/showGb?type=online&hcno=…&request_locale=zh` | UA-A, `Referer: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…&refer=outter` | 200 `text/html;charset=UTF-8` | 89,039 | sha256 `f32c3f4714af9cb20232468d75600940ab795b62e7449c2ad186b525b811ecb9` |
| F7 | GET `/bzgk/std/showGb?type=online&hcno=…` (no locale) | UA-A, same Referer | 200 | 89,002 | sha256 `f15dedfc8c367488fc1372b66773bdd24dd22c374a7d141dcff3521d8ec6c0b7` |
| F8 | GET `/bzgk/std/showGb?type=download&hcno=…&request_locale=zh` | UA-A, same Referer | 200 `text/html;charset=utf-8` | 7,606 | sha256 `124ebe19cbe016efcce983a2fb5f34b44304ec110a40482f73b1a5f16e7e3d99` |
| F9 | GET F1 (no `type`) | UA-A, no Referer, no cookie | 302 to `newGbInfo` (catalogue) | — | — |
| F10 | GET F6 target with session cookie jar (`JSESSIONID`) + same Referer | UA-A | 200, zh | 89,039 | differs from F6 in exactly one line (analytics `hcno` token) |

Evidence windows (committed with this seat): `.ufo/waves/round-76/w1/stage/ScribeEntryB/evidence/S897-catalogue.html`, `S897-viewer-zh.html`, `S897-viewer-en.html`, `S897-download-zh.html`, and the F1/F6/F8 response headers as `S897-f1-headers.txt`, `S897-f6-headers.txt`, `S897-f8-headers.txt`. Hashes above were computed on those copies.

Commands (verbatim shape; one route shown, the others differ only in the query string):

```
curl -sS -D head.txt -o body.html -A "$UA-A" \
  'https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296'
curl -sS -o body.html -w '%{http_code} %{size_download} %{content_type}\n' -A "$UA-A" \
  -e 'https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter' \
  'https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296&request_locale=zh'
```

## Source records — one per cited route, each ADMIT/REFUSE

### G1 — catalogue page (F3/F4/F5)

- URL: `https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` (redirect target of the source-line URL)
- status/bytes/UA: HTTP 200, 24,144 B, UA-A (F3); byte-identical repeat (F4) and with `Accept-Language` (F5).
- located quote: 「农历的编算和颁行」 — 8 chars — 中文标准名称 row, line 446 of the served HTML.
- verdict: **ADMIT** for the bibliographic fields only (标准号, both names, 现行, 2017-05-12, 2017-09-01, A46, 07.040, 中国科学院 ×2, the two 发布单位). Flip: if any field changes on re-fetch, refresh the field and keep the citation; never paraphrase a field that changed.

### G2 — catalogue 在线预览提示 modal (F3)

- URL: as G1.
- status/bytes/UA: as G1.
- located quote: 「当前浏览器暂不支持标准全文在线预览服务」 — 22 chars — modal `#myModal`, line 588; the same string is in the i18n map at line 69.
- verdict: **ADMIT** that the string exists; **REFUSE** the reading that it explains the page. Flip: the string is dead code — the `if(supported)` guard at lines 114–119 is commented out, so the modal is never shown and the button opens the viewer unconditionally. The entry states this correction.

### G3 — viewer page (F6/F7/F10)

- URL: `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296`
- status/bytes/UA: HTTP 200, 89,039 B zh / 89,002 B en, UA-A, Referer as above (F6/F7).
- located quotes: 「在线预览|GB/T 33661-2017」 (title, line 14); 「请保持鼠标在当前窗口以获取清晰标准文本。」 (21 chars, 阅读提示 modal, line 1278); `var page = 12;` (line 1368) with 12 `<div id="0".."11" class="page">` elements (lines 170–~1200); `request.open('get', 'viewGbImg?fileName='+bg, true);` (line 1463).
- negative sweep on this body (command in draft §3/report): 范围 0, 术语 0, 编算 0, 农历 0, 历法 0, 朔 0, 节气 0, 紫金山 0.
- verdict: **ADMIT** for the mechanical claims (raster tiles, no clause text in the HTML, page count 12 tiles). **REFUSE** any page-image download or OCR of the standard's sentences in this seat; the article's substance stayed unread. Flip: if a lane-approved, terms-compliant text-bearing edition arrives, cite that edition instead of this page.

### G4 — download modal + captcha (F8)

- URL: `https://openstd.samr.gov.cn/bzgk/std/showGb?type=download&hcno=E107EA4DE9725EDF819F33C60A44B296`
- status/bytes/UA: HTTP 200, 7,606 B, UA-A, Referer as above.
- located quotes: 「GB/T 33661-2017 全文下载」 (modal title); `id="verifyCode" maxlength="4" placeholder="验证码"` (line 209); `url:'verifyCode'` POST inside `checkCode()` (line ~3290); 「本系统所提供的电子文本仅供参考，请以正式标准出版物为准。」 (29 chars, disclaimer).
- verdict: **ADMIT** that a four-character 验证码 stands between the request and the file. **REFUSE** to submit or solve it; no captcha was attempted, so nothing behind it is claimed. Flip: nothing to flip — if a later round passes the captcha it must say so and its evidence is a fresh record, not this one.

## Staged-text checks (candidate b as handed over)

| staged statement | test | outcome |
|---|---|---|
| "both routes return byte-identical responses — 24148 bytes each, md5 `9791d9dc0f17384eeab4ff4791eed437`" | F1/F2/F3; two repeats + one Accept-Language variant | **does not reproduce**: the no-navigation pair is identical at **24,144 B**, md5 `e866bfd61a16f4c4fcdc1fc3a16bdf89`, sha256 `80b4c781…`. A 24,148-byte response did not appear under any of the four variants tried. The number is stale or from another route; the draft does not carry it. |
| "the download route is the catalogue page again, not a file" | F8 with the page's own Referer | **refuted as stated**: the navigated download route serves a 7,606-B 全文下载 captcha modal. The identity belongs to the 302 redirect, not to the route. |
| "the registry states in its own words why the text is not on the page: 当前浏览器暂不支持…" | catalogue script lines 110–119 | **overread**: the string exists, but its guard is commented out and the button always opens the viewer. |
| "no non-browser channel reaches the standard's text" | F6 | **too wide**: a request with the page's Referer reaches the viewer; the viewer is images, not text. The draft narrows the claim to the served HTML and states the raster limit. |
| "24148 bytes each" as a recheck anchor | recheck command is now the four-request matrix, not a byte count | **replaced**: the viewer body is not byte-stable (F6 vs F10 differ in the analytics token line), so the recheck must re-locate spans, not compare hashes. |

## Verdict on the entry

**ADMIT, reduced and corrected** — the entry is carried only by what the pages state about themselves and by
measured route behaviour. No clause text, no captcha passed, no page image downloaded, no campaign id cited.
If the L1 prefers a hard refusal, the honest alternative is to refuse candidate b entirely: what it can add
over the record is a boundary note, not the standard's substance. The boundary note is, however, fully
sourced and decision-usable (§4), so the draft is submitted as an amendment rather than a refusal.

Residual limits: (1) the three URLs are one controller/hcno family; if the registry counts one row per URL the
row needs three locators, not three rows; (2) printed folios are untested — the draft marks that (to-verify);
(3) no independent copy of this page exists in the wave's evidence directory yet; the fetch lines above are
the record.
