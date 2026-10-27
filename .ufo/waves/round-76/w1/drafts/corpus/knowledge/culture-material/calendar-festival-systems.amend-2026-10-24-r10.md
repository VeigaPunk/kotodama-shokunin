# Amendment — what the authoritative copy serves when asked, and the two gates between its page and the standard's text

- source: S897 — https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296 — 全国标准信息公共服务平台 (footer: 主办 国家市场监督管理总局国家标准技术审评中心), the 标准信息表 for GB/T 33661-2017 and the route family its own controls call: the catalogue page `/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` (the referer-less redirect target), the 在线预览 target (`type=online`), and the 全文下载 target (`type=download`); locators C1–C9 are defined in §1–§3 — fetched 2026-10-27 (browser-shaped UA, plain GET; catalogue HTTP 302→200, 24,144 B, sha256 80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9; viewer 200, 89,039 B zh / 89,002 B en; download modal 200, 7,606 B)
- verified-at: 2026-10-27
- recheck: 90d — repeat the four requests named on the source line (referer-less `type=online`, referer-less `type=download`, referer'd `type=online`, referer'd `type=download`) and re-locate C1–C9; the negative sweep in §3 must again return 0 for every probe word. The fetch line for each row — URL, User-Agent, HTTP status, bytes, sha256 — is stored with this wave's gate notes.
- ground: at base 98c486bdb4650ba5b8e651d332910e8ee60ad121 the lane has no knowledge file and no registry row for this instrument — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -l -E 'GB/T 33661' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge` prints nothing, `git show 98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md | grep -c '33661'` = 0, and the same `grep -c` for `openstd` = 0. Two lesson files do mention it — `corpus/lessons/round-68.md:111` lists the page as present and adoptable, and `corpus/lessons/round-69.md:39,111` records a package row for it — which is the lane saying it knew of the page and had not adopted it. The calendar entry names a Chinese lunisolar calendar among its exemplars but carries no standards-level record of one, so the lane can describe the calendar and cannot yet cite the instrument that fixes it.
- topic: what the registry's own pages state about this standard, what each of the page's two buttons actually serves when a request carries the navigation a browser would send, and which of those bytes a citation may carry.
- gap filled: the lane's calendar entry models lunisolar intercalation and festival placement without any promulgated instrument behind the model. This amendment adds the instrument's public record — name, status, dates, classification, issuing bodies — and the measured boundary of that record: the catalogue prints fields and no clauses, the reading route serves raster page tiles, and the file route stands behind a four-character verification code. It records the boundary so a later round stops trying endpoints and either quotes the record or names the text as unread.
- sources: the one row above, tier A for the registry's own record of the standard and its own page mechanics. The standard's normative clause text is not among these sources and is named as unread below; nothing here paraphrases a clause.
- couples: `culture-material/calendar-festival-systems.md` (the lunisolar and festival machinery this amendment supplies an instrument record for), `culture-material/timekeeping-instruments.md` (the observatory-side instruments whose output a promulgated calendar fixes), `culture-material/era-periodization-models.md` (the dating vocabulary a standard's promulgation date enters as a fact rather than an era claim).
- scope: an amendment to the calendar entry. It records the registry's fields for GB/T 33661-2017, the measured behaviour of the page's two routes, and a short decision table for what a worldbuilder may cite from them. It decides no fictional world's calendar, makes no rights, licence or attribution ruling, and ends before the lore handoff. It refuses: any clause text, any claim about what the standard requires, any inference from page-tile count to printed pagination, and any treatment of the registry record as evidence about the standard's substance.

## 1. The catalogue page: fields a citation can carry

The catalogue page prints one 标准信息表 for this standard, and every field below is read from that table (C1, S897):

| field | value as printed |
|---|---|
| 标准号 | GB/T 33661-2017 |
| 中文标准名称 | 农历的编算和颁行 |
| 英文标准名称 | Calculation and promulgation of the Chinese calendar |
| 标准状态 | 现行 |
| 发布日期 | 2017-05-12 |
| 实施日期 | 2017-09-01 |
| 中国标准分类号（CCS） | A46 |
| 国际标准分类号（ICS） | 07.040 |
| 主管部门 | 中国科学院 |
| 归口部门 | 中国科学院 |
| 发布单位 | 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会 |

The 备注 row is present and empty (C1, S897). The calibration this entry rests on: 现行 is the registry's own status field for a national standard, and that is `mainstream` in the only sense used here — a promulgated instrument recorded as currently in effect. Nothing in the table states a rule, and the entry never upgrades the table into one (S897).

The catalogue page also prints an 在线预览提示 modal: 「当前浏览器暂不支持标准全文在线预览服务，请使用现代浏览器（Chrome、Firefox、Opera、Microsoft Edge、360安全浏览器、搜狗浏览器、猎豹浏览器、傲游浏览器等）重新打开当前页面继续进行标准全文预览。」 (C2, S897). Read on its own, that sentence looks like the registry's explanation for why the text is not on the page. §3 shows why it is not: the page's own script no longer reaches it.

## 2. What the two buttons serve: the measured route family

A request that carries no navigation header is redirected before it can reach either route. A referer-less GET of the 在线预览 URL answers 302 with `Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter`, and so does the 全文下载 URL (C3, S897). Both therefore land on the same catalogue page, and that page is byte-stable: 24,144 bytes, sha256 80b4c781…, identical across two consecutive fetches and a third sending `Accept-Language: zh-CN` (C4, S897).

That identity is a property of the redirect, not of the routes. When the request carries the Referer a browser would send from the catalogue page — the page's own buttons call `window.open('/bzgk/std/showGb?type=…&hcno=…&request_locale=…')` — the two routes separate (C5, S897):

- `type=online` answers 200 with the viewer page, 89,039 bytes with `request_locale=zh` and 89,002 bytes without it; the two differ in the title and toolbar strings, and two zh responses fetched with different session cookies differ in exactly one line, the analytics object `var data = {'hcno':'…','time':totalTime,'rate':rate};`, whose token changes between requests — so the viewer page is not byte-stable at all (C5, S897).
- `type=download` answers 200 with a 7,606-byte 全文下载 modal headed 「GB/T 33661-2017 全文下载」, carrying a four-character 验证码 input, an image element whose source the page sets to `gc?_<timestamp>`, and a `checkCode()` that POSTs `{verifyCode: …}` to `verifyCode` and reloads on success — no file is served to a client that has not passed that challenge (C6, S897).

A prior draft of this amendment compared the two routes without the navigation header and read the identity as proof that the download button serves the catalogue page and no file. The measurement above does not support that reading: the identity belongs to the redirect, and the captcha — not a repeat of the catalogue — is what stands between a navigated request and the file.

## 3. Why the reading page carries no sentences

The viewer page for this standard is titled 在线预览|GB/T 33661-2017 and holds 12 `<div class="page">` elements, ids 0–11, each 2315×3274 px, with `var page = 12;` in its script (C7, S897). The text of those pages is not in the HTML: each div carries an opaque `bg` token and the script fetches the image with `request.open('get', 'viewGbImg?fileName='+bg, true)`, then paints it as a background image. The page even instructs the reader about the display: 「请保持鼠标在当前窗口以获取清晰标准文本。」 (C8, S897).

A sweep of the served viewer HTML for the standard's own vocabulary returns zero occurrences of each probe word — 范围 0, 术语 0, 编算 0, 农历 0, 历法 0, 朔 0, 节气 0, 紫金山 0 (C8, S897). This is the mechanical reason the reading route cannot supply a sentence: it is a raster reader, and the sentences are painted from the page images, not carried as text in the served page.

The 在线预览提示 modal's explanation is dead code. The click handler for 在线预览 carries `//if(supported) {` and `//} else {` — both commented out — so the handler calls `showGb(el.attr('data-value'),'online')` unconditionally and never shows the modal that blames the browser (C9, S897). The consequence is exact and worth stating plainly: a browser-shaped request does not fail for lack of browser support; it gets the viewer, and the viewer's ceiling is 12 raster tiles plus a captcha-gated file. A citation of this standard's content must therefore come from a document that carries text, not from this page, and no page image was downloaded here.

## 4. What a worldbuilder can and cannot take

What the registry can and cannot answer, row by row — every locator in this table is the page field or script named in §1–§3 (S897).

| what the design asks | what the registry can answer | what it cannot, and the fallback |
|---|---|---|
| what is the instrument called, and is it current? | yes: both names, 现行, 2017-05-12 and 2017-09-01, CCS A46 / ICS 07.040 (C1) | — |
| who promulgated it and who administers it? | yes: 中国科学院 for both 主管 and 归口, and the two 发布单位 as printed (C1) | — |
| what does it actually require? | no: no clause text on the catalogue or the viewer (C8) | the normative sentences; name the text as unread in the world bible |
| how long is it, for a page citation? | only a tile count: 12 viewer tiles (C7) | printed folios; do not cite a page number from the viewer (to-verify) |
| may I quote a rule from the registry? | no: the page carries fields and images, not rules (C8) | quote a document that carries text, and cite that document |
| can I obtain the file? | only past a four-character 验证码 (C6) | automated retrieval; do not script the challenge |

Read as a rule for design, this entry's own formulation: when a fictional calendar is modelled on a promulgated standard, the citable chain is the promulgation record plus a text-bearing edition of the standard. The registry certifies the instrument's existence, name, status and dates; it does not certify a rule, and a world bible that lists it under "sources for the calendar's rules" is citing the wrong artefact.

Worked example, hypothetical and canon-free: a world's festival calendar is said to follow a promulgated standard. The citable sentence is "the world's calendar is modelled on an instrument promulgated on a given date and recorded as in force", with the registry record behind it; the sentence "the instrument requires a leap month every third year" needs the text, not the record, and must stay out of the bible until that text is read.

## 5. What this amendment does not establish, and the handoff

- No clause text was read, quoted or paraphrased. Every claim above is about the registry's pages and their bytes; none is about the standard's requirements (S897).
- The tile count is not a pagination. The viewer shows 12 tiles; whether they map one-to-one to printed folios is untested here and is marked (to-verify) wherever it matters.
- The access account is narrow and stated as such: the requests carried the Referer the page's own buttons use; the download modal's 验证码 was not attempted or solved, and no page image was downloaded. A challenge met and routed around is not claimed — none was passed.
- Calibration: the instrument's in-force status is `mainstream` (a national standard the registry records as 现行); the reading of the referer-less byte identity as "the download serves no file" is `discredited` by the separated routes in §2; the design table in §4 is this entry's own construction and carries no calibration weight.
- Handoff: what a world's calendar is, and which instrument it cites, are canon decisions for the world bible and lore; this entry stops at the record and the boundary, and makes no rights, licence or attribution ruling.

---
