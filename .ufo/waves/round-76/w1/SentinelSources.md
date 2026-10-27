# SentinelSources — round 76 / wave 1 — attack on the candidate sources and the staged package

Seat: `SentinelSources` (leaf; no subagents, no background jobs, no labrat probe used).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base revision: `98c486bdb4650ba5b8e651d332910e8ee60ad121`.
Package under attack (read-only): `/home/vgpnk/Projects/shokuknow/merge/kotodama/`.
Date of every fetch below: **2026-10-27**. Scratch: `/fast/scratch/hyaku/kotodama-r76/SentinelSources` (deleted on exit; receipts copied into `w1/stage/SentinelSources/receipts/`).
One User-Agent used for every recorded fetch, unless a row says otherwise:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` (referred to below as `<UA>`).

Scope: (1) are the planned source URLs public ordinary-means pages; (2) credential material in the staged package; (3) is plain GET on the Chinese standards portal a terms-of-use breach the lane must record. Plus whatever the attack turned up on the way: duplicate documents, false "live page withdrawn" provenance, a Before leg that does not hold, and kill-rule exposure in all four staged entries.

Verdict in one line: **no access-control bypass, no credential leak, no private host, no tracking token — but three things in the DRAFT claim C would fail their own declared kill rule if frozen as written (entry d's provenance, the S896/S897 duplicate, the `-- corpus` Before leg), and every staged entry carries campaign ids and package-side pointers that resolve nowhere in the lane.**

---

## F1 — HIGH — entry `d` is not the standard's clause text; it is the drafter's 解读材料 (provenance defect, and it trips the tier-C rule)

**What the staged file claims.** `knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md:1-6` and its body:

```
# Amendment — the standard's clause, not the drafter's reading of it
source: S916 — https://www.xingzuobaike.com/huangli/wannianli/d165803.html — the 原文 section, 编排规则 clause (4) — fetched 2026-10-23
...
- topic: the standard's own clause text: the 编排规则 (1)–(5) ...
- **§N The clause, quoted** — from S916: rule (4) in the standard's own words ...
```

**Measured.** The page's content is the official 5-page interpretation PDF, line for line. I fetched both and compared.

```
$ curl -sS -A '<UA>' --max-time 60 -o jiedu.pdf -w 'jiedu code=%{http_code} size=%{size_download} ctype=%{content_type}\n' \
    'http://www.pmo.cas.cn/xwdt2019/kpdt2019/202203/P020240201504886119982.pdf'
jiedu code=200 size=108132 ctype=application/pdf
$ file jiedu.pdf
jiedu.pdf: PDF document, version 1.5, 5 page(s) (zip deflate encoded)
$ pdftotext -layout jiedu.pdf jiedu.txt   # chars=8735
```

Sentence probes (normalised whitespace, containment):

```
pdf=True web=True :: 本标准首次明确了农历计算的模型、精度以及编排规则和表述方法
pdf=True web=True :: 本标准主要技术内容包括两部分
pdf=True web=True :: 农历的编排规则明确了农历的年、月、日的确定方法以及排序方法
pdf=True web=True :: 公开发行的农历日历应注明资料来源
pdf=True web=True :: 对农历颁行要求的内容如下
```

Line containment over the mirror page's content lines (nav/promo/footer excluded):

```
content lines=27 in_pdf=21 not_in_pdf=6
--- NOT in PDF (first 6):
  * 国家标准《农历的编算和颁行》GB/T 33661-2017 原文及解读材料
  * 此文件原载：https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296
  * 2026年日历：2026丙午马年日历全年表，2026年阴历阳历对照表
  * 2027年节气表：2027年二十四节气日期及时间表（含公历和农历）
  * 2027年日历：2027丁未羊年日历全年表，2027年阴历阳历对照表
  * 易学董老师：2026年10月27日 每日通胜+今日生肖红黑榜
```

So: **21 of 27 content lines are verbatim in the official 解读材料 PDF; the other 6 are the page title, a provenance line, and four site promos.** There is no separate 原文 section in the served artefact — `原文` occurs exactly twice on the page, both in the title (`grep -c '原文'` → `2`: line 1 `<title>`, line 19 `<h1>`). Normative-clause markers are absent:

```
$ grep -cE '规范性引用文件|术语和定义|^\s*[0-9]+\s+范围|^\s*5\.[0-9]' body-895.html.txt
0
```

And the `(1)–(5)` list the entry wants to quote sits **inside the interpretation's `§标准主要内容` 第 1 条**, introduced by the drafter's own words `本标准沿用规则如下：` — the numbered items `1. 农历的编排规则… 2. 农历日期编排… 3. 农历的表示方法… 4. 对农历颁行要求的内容如下：` are the interpretation's section numbers, not GB/T clause numbers.

**Exploit path (how this becomes a false lane claim).** Land `d` as staged → the corpus asserts *"the standard's own clause text … quoted as the standard states it rather than as the drafter explains it"* → the lane's own quality rule (tier-C only, never factual authority) is inverted: a tier-C third-party mirror of the drafter's **interpretation** is cited as the **standard's normative wording**. Nothing in the artefact can support that: a reproduction of the interpretation cannot establish the standard's clause text even where it quotes the rules.

**Second, independent trip.** Claim C's declared after-state says *"no tier-C row is the sole support of an admitted entry"*. Entry `d` has exactly **one** source and it is tier C (`SOURCES.append.md` S916: `| ... | spec | C |`). Admitting `d` as staged breaks that leg of the claim with no ambiguity — no gate judgement needed.

**Smallest remediation.**
- (a) Preferred: drop entry `d` from the admitted set. `n >= 2` still holds from `a`, `b`, `c`; `k` loses its tier-C row.
- (b) If the lane wants the interpretation: re-point `d` to the **official** carrier (the pmo.cas.cn 5-page PDF the campaign already cites as S860, `docs | A`), rewrite `d`'s topic/scope to "the drafting observatory's interpretation of the standard", add its registry row, and never describe it as the standard's clause text. Caveat the lane must record if it takes (b): that PDF is served over **plain http** (`http://www.pmo.cas.cn/...`), i.e. no TLS.
- Either way: do not cite the mirror as clause text, and if the mirror is kept for any purpose, its tier stays C and it is never a sole support.

---

## F2 — HIGH — S896 and S897 are ONE document; `k` is over-counted by one

**Planned.** DRAFT claim C row plan: `S896 = openstd newGbInfo Wayback capture (S932)`, `S897 = openstd showGb page (S938)` — two registry rows.

**Measured.** Four URL spellings, one record page.

```
$ curl -sS -I -L -A '<UA>' 'https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296'
HTTP/1.1 302
Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter
HTTP/1.1 200
Content-Language: zh
final=https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter redirects=1
```

```
type=online   run1 code=200 size=24144 final=.../newGbInfo?hcno=...&refer=outter
type=online   run2 code=200 size=24144 ...
type=download run1 code=200 size=24144 ...
type=download run2 code=200 size=24144 ...
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-download-1.html
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-download-2.html
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-online-1.html
e866bfd61a16f4c4fcdc1fc3a16bdf89  route-online-2.html
```

And the `gb` (not `std`) spelling named by the mirror page's own provenance line also collapses:

```
--- https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296
code=200 size=24144 ctype=text/html;charset=utf-8 final=https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296
--- https://openstd.samr.gov.cn/bzgk/gb/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296
code=200 size=24144 ... final=https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter
```

So `/bzgk/std/newGbInfo`, `/bzgk/std/showGb?type=online`, `/bzgk/std/showGb?type=download`, `/bzgk/gb/newGbInfo`, `/bzgk/gb/showGb` all resolve to the **same** 24 144-byte registry record. This independently confirms entry `b`'s qualitative claim that the "download" button is the catalogue page again — and it falsifies the plan's assumption that `showGb` is a second document.

**Impact.** Claim C's after-state is defined as `k = number of distinct documents …, one row per document`. Two rows for one document breaks the claim's own definition, and the claim's kill rule lists *"a row appended as staged"* — a second row for the same document is that failure in substance.

**Smallest remediation.** One row for the openstd record. Put the live `newGbInfo` address as the row's primary address, the 2026-04-24 capture as the dated fallback, and record the `showGb`/`gb` spellings **inside that row as 302 aliases** (this preserves entry `b`'s negative result without a phantom document). Then `k = 4` for the four entries `a`–`d`: NAJ `search` page, openstd record, gmw 2017 report, and (only if F1(b) is taken) the pmo.cas.cn PDF — or 3 if `d` is dropped and the openstd row stands alone. The DRAFT already licenses this ("Scouts may change this plan … where two URLs are one document").

---

## F3 — MEDIUM — S932's "live record page no longer serves this text" is false today, and entry `b`'s byte-count/md5 is not reproducible

**Measured (live record, 2026-10-27).**

```
$ curl -sS -A '<UA>' --max-time 30 -o body-896orig.html -w 'S896orig %{http_code} %{size_download}\n' \
    'https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'
S896orig 200 24144
```

All field rows are server-rendered in that response:

```
 标准号：GB/T 33661-2017
 中文标准名称： 农历的编算和颁行
 英文标准名称：Calculation and promulgation of the Chinese calendar
 标准状态： 现行
 中国标准分类号（CCS） A46
 国际标准分类号（ICS） 07.040
 发布日期 2017-05-12
 实施日期 2017-09-01
 主管部门 中国科学院
 归口部门 中国科学院
 发布单位 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会
```

(receipt: `receipts/openstd-record-fields-2026-10-27.txt`, 24 lines.)

The campaign row S932's marshalling text says *"the live record page no longer serves this text; the archived capture does"*. **That is not what the live page does today** — 200, 24 144 bytes, eleven field rows, no cookie jar, no JS. The capture is a *fallback*, not the only carrier. The staged entry `a` then attributes the field set to "capture of 2026-04-24" when the live page serves it.

Second half: entry `b` states *"Fetching both routes returns **byte-identical** responses — 24148 bytes each, md5 `9791d9dc0f17384eeab4ff4791eed437`"*. Today:

```
type=online   run1 code=200 size=24144 ...
type=download run1 code=200 size=24144 ...
md5 e866bfd61a16f4c4fcdc1fc3a16bdf89  (all four fetches)
```

`24148` vs `24144` and a different md5. The *qualitative* claim ("the download route is the catalogue page again") holds and I confirmed it; the *numbers* are a snapshot of a server-rendered page and are not a stable window — a gate quote that includes them cannot be relocated by re-fetch.

**Impact.** A row whose address is annotated "withdrawn" invites the executor to cite a capture when a live ordinary fetch works, and a byte/md5 window that drifts fails the gate's own "quote located inside a committed evidence window" check on the next recheck.

**Smallest remediation.** (i) Row: live `newGbInfo` primary, capture dated fallback, and state the observed date of each. (ii) Entry `b`: keep "both routes return the same catalogue page", drop the byte count and md5, or bind them explicitly to the dated capture (`id_` fetch) rather than to the live page.

---

## F4 — HIGH — claim C's declared `Before:` command does not hold (it prints files, exit 0)

**Claim text.** *"Before: `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` each print nothing (exit 1)."*

**Measured, verbatim.**

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -l -E 'GB/T 33661' 98c486b -- corpus
98c486b:corpus/lessons/round-68.md
98c486b:corpus/lessons/round-69.md
exit=0
$ git -C ... grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus
98c486b:corpus/lessons/round-68.md
exit=0
```

The same two patterns **do** print nothing when scoped to the knowledge tree:

```
$ git -C ... grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge
exit=1
$ git -C ... grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus/knowledge
exit=1
```

**Impact.** As written, the claim's own do-nothing control falsifies it before any data arrives: the lane *does* mention both tokens at base (in lessons). Freezing it leaves an assertion the L1 can only satisfy by pretending the grep is narrower than it is — the exact "stated token differs from observed token" class this round is meant to catch.

**Smallest remediation.** Re-scope the Before command to the tree the claim actually asserts about:
`git grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge` → nothing (exit 1); same for `digital\.archives\.go\.jp`. Optionally add the honest C-score line: the tokens exist in `corpus/lessons/round-68.md`, `round-69.md`, so the novelty claim is "the knowledge tree does not hold it", not "the lane never mentioned it".

---

## F5 — MEDIUM/HIGH — every staged entry carries campaign ids and package-side pointers that resolve nowhere in the lane

Tokens present in the four staged files (`grep -oE 'S[0-9]{3}' | sort -u`):

```
calendar-festival-systems.amend-2026-10-24.md        S750 S777 S807 S919 S921 S932 S935 S937
calendar-festival-systems.amend-2026-10-24-r10.md    S938
calendar-festival-systems.amend-2026-10-23c.md       S718 S719 S916
era-periodization-models.amend-2026-10-23b.md        S757 S908
```

The DRAFT's re-pointing table covers only S937→S898, S935→S894, S932→S896, S938→S897, S919→S892, S921→S885, S916→S895, S908→S894. **Unmapped: `S750`, `S777`, `S807` (entry a), `S757` (entry c), `S718`, `S719` (entry d).** Two of those are collision traps, not merely unmapped:

```
$ git -C ... show 98c486b:corpus/SOURCES.md | grep -E '^\| S71[89] '
| S718 | Farran et al., 2016, "Cross-Cultural Register Differences in Infant-Directed Speech: An Initial Study", PLOS ONE ...
| S719 | Alejandrina Cristia, 2013. Input to Language: The Phonetics and Perception of Infant-Directed Speech. ...
```

So a blind "re-point by id" on entry `d` would cite **infant-directed-speech** rows for a Chinese calendar standard — precisely the failure mode the campaign-namespace collision guard exists to prevent.

Second exposure: the `recheck:` and `ground:` lines name package-side documents that exist in neither tree:

```
$ find /home/vgpnk/Projects/shokuknow/merge/kotodama -name 'SOURCES-PROPOSED*' | wc -l
0
$ git -C <lane> ls-tree -r --name-only 98c486b | grep -c 'SOURCES-PROPOSED'
0
$ git -C <lane> ls-tree -r --name-only 98c486b | grep -c 'CANNOT-ANSWER'
0
```

Every entry's `recheck:` says "re-run the row recheck command in round N's `SOURCES-PROPOSED.md`" and every `ground:` cites "round 8's CANNOT-ANSWER §2" / "round 6's …". None of those files is in the lane or the package.

**Impact.** Claim C's kill rule names two of these explicitly: *"a row appended as staged"* and *"a cited campaign-namespace id"*. Landing any entry unchanged trips at least one; landing entry `d` with the id mapping applied mechanically trips the collision guard as well.

**Smallest remediation.** In the landing text: (i) replace every campaign id with the lane id **by document** (or delete the superseded passage that carries it — entry `a`'s second section is explicitly "Superseded passage … retained as the dated record"); (ii) never map `S718`/`S719` by number; (iii) make `recheck:` a self-contained command that runs in the lane, and `ground:` a lane path, because the round-N package files are not in the repo.

---

## F6 — LOW/MEDIUM — the NAJ evidence is a JS modal of 350 buttons, not form "options" (the row's own address is sound)

**Claim.** S908/DRAFT: *"詳細検索フォーム「元号名称／開始西暦年」options"*.

**Measured.** It is a modal picker with server-rendered buttons plus hidden inputs:

```
<input type="hidden" id="date-gengo-1-from" class="dateEField" name="date_e_from_era" value=""
<button type="button" class="archive-finder-form-container__date-gengo-bt cmn-button"
<button type="button" class="gengo-modal__tab is-current" data-gengo-type-target="wa"
<button type="button" class="gengo-modal__select-button" data-gengo-label="令和" data-eracode="248" data-yyyy="2019"
<button type="button" class="gengo-modal__select-button" data-gengo-label="平成" data-eracode="247" data-yyyy="1989"
<button type="button" class="gengo-modal__select-button" data-gengo-label="昭和" data-eracode="246" data-yyyy="1926"
id="date-gengo-1-from" / id="date-gengo-1-to" / id="gengo-modal"
data-eracode count = 350 ; 開始西暦 count = 3 ; 元号名称 <th> = 3
```

Live vs the 2026-04-22 capture — the values are identical, which is what makes the "one row, two addresses" plan for S894 sound:

```
$ md5sum naj-era-buttons-live.txt naj-era-buttons-cap2026-04-22.txt
cc88460841fee4655e7633b8bb9ea2a8   (350 lines)
cc88460841fee4655e7633b8bb9ea2a8   (350 lines)
branch tabs: 1 cho / 1 chu / 1 wa   (both)
```

The entry's five named values are exactly as stated: `明治 1868`, `大正 1912`, `昭和 1926`, `平成 1989`, `令和 2019`; the table runs to `文治 1185` (present in both live and capture).

**Impact.** Low, but it is the kind of wording a gate quote has to land on: a quote of "the 詳細検索フォーム … options" is not locatable (there is no `<select>`), while the button list is. Also worth recording: the table is readable by plain GET only because it is server-rendered inside the modal markup — it is not a JS-only fetch.

**Smallest remediation.** Say what is there: "the 詳細検索 form's 元号 picker (`#gengo-modal`), whose 350 buttons each carry `data-gengo-label`/`data-eracode`/`data-yyyy`, in the initial HTML (plain GET, HTTP 200)". Values and dates as measured are correct and need no change.

---

## F7 — INFO — ordinary-means and terms-of-use record for each host (the explicit question on openstd)

Headers-only sweep for every planned and already-held address (`curl -sS -I -L -A '<UA>'`), raw receipts in `receipts/`:

| key | status | final URL | host | note |
|---|---|---|---|---|
| S894 live | 200 | `https://www.digital.archives.go.jp/search` | www.digital.archives.go.jp | 311 308 B, `Content-Language: ja`; 0 redirects |
| S894 capture | 200 | `…/web/20260422145052id_/https://www.digital.archives.go.jp/search` | web.archive.org | 307 700 B; `memento-datetime: Wed, 22 Apr 2026 14:50:52 GMT` |
| S895 | 200 | `https://www.xingzuobaike.com/huangli/wannianli/d165803.html` | www.xingzuobaike.com | 33 179 B; openresty/CDN cache, 0 redirects |
| S896 capture | 200 | `…/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` | web.archive.org | body gzip, 24 174 B decoded |
| S896 original (live) | 200 | same `newGbInfo` URL | openstd.samr.gov.cn | 24 144 B, field rows served |
| S897 (`showGb?type=online`) | 200 after **1** redirect | `…/bzgk/std/newGbInfo?hcno=…&refer=outter` | openstd.samr.gov.cn (**same authority**) | 302 `Location:` then 200 |
| S898 | 200 | `https://news.gmw.cn/2017-05/23/content_24559485.htm` | news.gmw.cn | 8 076 B, gzip |
| S892 held (Marrone PDF) | 200 | `…if_/https://iris.unipa.it/retrieve/…2014%20marrone%20age%20dor---2.pdf` | web.archive.org | `application/pdf`, 763 802 B |
| S885 held (Barthes/Persée) | 200 | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` | www.persee.fr | 111 487 B |

Flags, each with its sweep:

- **Tracking query strings: none.** Sweep over the nine URLs for `utm_*|gclid|fbclid|msclkid|yclid|ref=|referrer=|source=|spm=|sessionid|token=|sid=|phpsessid` printed nothing for every row. `hcno=` is the registry's document handle (removing it loses the record); `refer=outter` is **added by the server** on the 302, not by us.
- **Private/internal hosts: none.** `getent hosts` on the six hosts returned public addresses only (`18.161.205.x`, `111.203.12.48`, `120.52.95.237`, `2407:2440:2d::c`, `140.77.166.118`, `207.241.237.3`); the same sweep for `//localhost|//127.0.0.1|//10.|//192.168.|//172.(16-31).|.internal|169.254` matched nothing.
- **Redirect cross-authority hops: one, and it stays inside the authority.** `showGb` → `newGbInfo` is `openstd.samr.gov.cn` → `openstd.samr.gov.cn`. No redirect to a login, a captcha, or another host anywhere in the set.
- **Cookie/JS challenge: none, on either UA.** Same nine URLs fetched with the browser UA and with `curl/8.5.0`, no cookie jar: every combination 200.

```
S894-live | browser | 200|311308|text/html;charset=UTF-8     S894-live | curl | 200|311308|...
S894-cap  | browser | 200|307700|...                          S894-cap  | curl | 200|307700|...
S895      | browser | 200|33179|...                          S895      | curl | 200|33179|...
S896-cap  | browser | 200|8075|...                           S896-cap  | curl | 200|8075|...
S896-orig | browser | 200|24144|...                          S896-orig | curl | 200|24057|...
S897      | browser | 200|24144|...                          S897      | curl | 200|24057|...
S898      | browser | 200|8076|...                          S898      | curl | 200|8076|...
S892-held | browser | 200|763802|application/pdf              S892-held | curl | 200|763802|application/pdf
S885-held | browser | 200|111487|...                          S885-held | curl | 200|111480|...
```

  The two 87/7-byte deltas are explained, not mysterious — openstd echoes the UA into one JS variable and nothing else:

```
340c340
< var userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
---
> var userAgent = 'curl/8.5.0';
record-field block md5 (browser vs curl): c609e73c5018dd7cbdb42094f2ac8775 == c609e73c5018dd7cbdb42094f2ac8775
```

- **Cookies that are issued but not required:** persee sets `JSESSIONID`, `COOKIE_SUPPORT`, `GUEST_LANGUAGE_ID`; NAJ sets `AWSALB`/`AWSALBCORS`/`JSESSIONID`/`amladConsumerLang`; openstd sets `JSESSIONID=…; Path=/bzgk`. All are CMS/load-balancer cookies, none is an auth token, and every fetch above was made with **no cookie jar** and still got the content.
- **Access-control: no bypass, and the one 403 is already recorded honestly.** The direct publisher URL that lane S892's row calls "withdrawn" answers exactly as recorded:

```
$ curl -sS -o /dev/null -A '<UA>' -w 'code=%{http_code} final=%{url_effective} size=%{size_download}\n' \
    'https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf'
code=403 final=... size=5867
```
  Using the Internet Archive capture of the same deposit is an ordinary public copy, not a bypass — the block was **met and not passed**, and S892 says so.

### The specific question: is plain GET on `openstd.samr.gov.cn` fine, or does it breach a terms-of-use line the lane must record?

**It is fine by plain GET; nothing is accepted, nothing is bypassed, and no click-through or login exists.** What the page itself says, in full:

```
$ grep -oE '[^<>]{0,80}(声明|版权|版权所有|免责|使用条款|服务条款|隐私|转载|禁止)[^<>]{0,80}' body-896orig.html
版权所有 侵权必究
$ sed -n '605,625p' body-896orig.html | sed -e 's/<[^>]*>/ /g' ...
 版权所有 侵权必究
 主管：国家市场监督管理总局 国家标准化管理委员会
 主办：国家市场监督管理总局国家标准技术审评中心
 技术支持：北京中标赛宇科技有限公司
 支持电话：010-82261056
 备案号： 京ICP备18022388号-1
$ grep -oE 'href="[^"]*"[^>]*>[^<]{0,30}(声明|协议|帮助|须知|通知)[^<]{0,30}' body-896orig.html
(no output)
$ curl -sS -A '<UA>' 'https://openstd.samr.gov.cn/robots.txt'
HTTP Status 404 – Not Found  (code=404)
```

So: a **copyright reservation** (`版权所有 侵权必究` = "all rights reserved, infringement prosecuted"), a sponsor/operator line, an ICP filing number — and **no** user agreement, no terms page, no robots.txt. The only gating present is technical, and it gates the *standard's full text*, not the record: the `在线预览` modal says 「当前浏览器暂不支持标准全文在线预览服务，请使用现代浏览器…」, and I measured that the `type=online` and `type=download` routes return the catalogue page anyway (F2), so there is nothing behind the gate to take.

**Three lines the lane must record (smallest set, each evidenced above):**
1. `版权所有 侵权必究` — and the lane therefore quotes **short spans** of the record (field rows), never whole pages.
2. The full-text viewer is JS-gated; the lane does not drive it, does not hunt a PDF/image endpoint, and records the negative result (both route types return the record page, md5 `e866bfd6…`, 24 144 B, 2026-10-27).
3. openstd publishes **no robots.txt** — the lane's recheck is a single page fetch, and it says so rather than implying a granted crawl policy.

Other hosts' stated terms, for completeness:
- **NAJ** — `robots.txt` 200, `User-agent: *`, `Crawl-delay: 30`, `Disallow: /contentDownload/*`. The `/search` page is allowed; the lane's 180-day recheck must therefore space NAJ requests **≥ 30 s** apart. The page also shows a cookie-consent banner (`…クッキー（Cookie）の取得と利用に同意をお願いいたします。`); content is served regardless, and we did not accept anything.
- **gmw.cn** — `robots.txt` 200, 55 921 B, 1 264 `Disallow` lines whose shapes are 1 260 exact `/YYYY-MM/DD/content_NNN.htm` (2023–2024) and 4 `/*2013 … /*2016`; **no** rule matches `/2017-05/23/content_24559485.htm` (`grep -nE '2017'` → no hits; `grep -nE '24559485'` → no hits; no catch-all `Disallow: /`). Footer: `光明网版权所有`.
- **xingzuobaike** — `robots.txt` → 404 (its own "未找到页面"). Footer: `Copyright © 2026 Xingzuobaike.com All Rights Reserved`, and the page carries a rights-reserved document, so the same short-span rule applies. Third-party hosts the page references: only its own CDN/static and `www.huangli123.net`.
- **persee** — 200 without cookies; sets CMS cookies only.

---

## F8 — INFO/privacy — two analytics beacons exist on the pages and are **not** triggered by the lane's fetch

```
$ grep -n 'hm.baidu' body-896orig.html | cut -c1-120
652:  hm.src  =  "https://hm.baidu.com/hm.js?50758913e6f0dfc9deacbfebce3637e4";
$ grep -c 'hm\.baidu\.com' body-896orig.html
1
```

openstd's record page embeds a Baidu analytics tag. NAJ embeds Google Tag Manager, in two different shapes — the live page carries the `gtm.js` loader at line 62, the 2026-04-22 capture carries a `gtag/js?id=G-RE0R6DLCWW` tag at line 53 (both pages also carry consent-mode defaults):

```
--- live:     62:  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
--- capture:  53:  <script async src="https://www.googletagmanager.com/gtag/js?id=G-RE0R6DLCWW"></script>
--- counts:   live  googletagmanager=1 gtag/js=0  |  capture googletagmanager=1 gtag/js=1  |  hm.baidu=0 both
```

A plain `curl` executes neither, so the lane's fetches make no third-party request and leak nothing. The Baidu value is the site's **site id**, not a secret; it is not credential material and must not be quoted into the registry. External hosts referenced by the openstd record page are all PRC government/registry hosts (`std.samr.gov.cn`, `www.samr.gov.cn`, `www.sac.gov.cn`, `ncse.ac.cn`, `bszs.conac.cn`, `beian.miit.gov.cn`) — no ad network.

---

## F9 — PASS list (each with the sweep that produced it)

| check | result | command |
|---|---|---|
| credential material in the four candidates | **none** — no output, `EXIT=1` | `grep -rniE 'password|token=|secret|op://|api[_-]?key|session' <4 candidate files>` |
| credential material across the 5-file set (4 candidates + `SOURCES.append.md`) | **one line, false positive**: the word `bearer` in ordinary English — `names act on how others perceive their bearer), 自我信息加工取向 (self-information-processing` | same grep; per-pattern counts: `JSESSIONID 0`, `AWSALB 0`, `cookie 0`, `authorization 0`, `bearer 1`, `basic <b64> 0`, `password 0`, `secret 0`, `op:// 0`, `api[_-]?key 0`, `session 0` |
| absolute local paths in staged files | none (`exit=1`) | `grep -rnoE '/(home|fast|tmp|Users)/[A-Za-z0-9._/-]+' <4 files>` |
| plaintext `http://` URLs in the staged files | none (`exit=1`) | `grep -rnoE 'http://[^ )>,]+' <4 files>` |
| knowledge `.md` baseline | **252** (claim's baseline correct) | `git -C <lane> ls-tree -r --name-only 98c486b corpus/knowledge \| grep -c '\.md$'` |
| registry baseline | **817** rows, last id **S893** (claim correct) | `git -C <lane> show 98c486b:corpus/SOURCES.md \| grep -cE '^\| S[0-9]{3}'` and `… \| grep -oE '^\| S[0-9]{3}' \| tail -5` |
| registry holds none of the new hosts | `33661 → 0`, `openstd.samr.gov.cn → 0`, `digital.archives.go.jp → 0`, `xingzuobaike → 0`, `news.gmw.cn → 0`, `pmo.cas.cn → 0`; held: `persee.fr → S885,S886,S887`, `iris.unipa.it → 1` | `git -C <lane> show 98c486b:corpus/SOURCES.md \| grep -cE '<pattern>'` |
| four target filenames absent at base | `0` each | `git -C <lane> ls-tree -r --name-only 98c486b corpus/knowledge/culture-material/<file> \| wc -l` |
| `S894`–`S898` rows already in registry | `0` | `git -C <lane> show 98c486b:corpus/SOURCES.md \| grep -cE '^\| S89[4-8] '` |
| already-held mappings are by document, not by number | **correct**: lane `S885` row already cites the Persée per-page service including `…_T1_0006_0000` (campaign S921 = p. 6); lane `S892` row already cites the Marrone PDF via the 2025-11-11 capture and records the direct 403 | `git -C <lane> show 98c486b:corpus/SOURCES.md \| grep -E '^\| S88[5] \|'` / `^\| S892 \|` |

---

## Unrun / out of scope (reported as unrun, not as passed)

- I did not attempt the standard's full-text viewer, its download endpoint beyond confirming the 302, or any licence/copy-of-record route: out of ordinary means and nothing measurable was behind the gate (F2).
- I did not verify the standard's normative wording against any copy — that is the claim's open CANNOT-ANSWER, unchanged by this seat.
- I did not evaluate claims C's counter implementation, the Ca ledger, or any round-75 machinery: not my surface.
- Several fetch attempts to `web.archive.org` failed with `curl: (7) Failed to connect … Could not connect to server` during this run (four, for the NAJ capture, before a `--http1.1` retry returned 200/307 700 B; one, for the openstd capture, before a plain retry returned 200). The successes are what the ledger records; the failures mean no archive receipt should be regenerated once and trusted without a retry loop.

---

## Receipts (written under `.ufo/waves/round-76/w1/stage/SentinelSources/`)

```
receipts/S885-held.txt … S898.txt        9 raw response-header dumps (one per URL in the sweep)
receipts/openstd-record-fields-2026-10-27.txt   24 lines — the record page's field rows as text
receipts/naj-era-buttons-live.txt               350 lines — data-gengo-label/data-eracode/data-yyyy
receipts/naj-era-buttons-cap2026-04-22.txt      350 lines — identical md5 cc88460841fee4655e7633b8bb9ea2a8
receipts/naj-era-branch-tabs.txt                 wa / chu / cho
receipts/FETCH-LEDGER.md                        status/URL table, body sha256s, route md5s, UA deltas,
                                                containment measurement, live-vs-capture md5s, iris 403
```

Body `sha256` (recorded so a re-fetch is comparable; the bodies themselves are **not** copied into the repo, because three of them are rights-reserved text):

```
80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9  body-896orig.html        (openstd record, live)
f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e  body-896cap.dec.html     (openstd record, 2026-04-24 capture, decompressed)
830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e  body-895.html            (xingzuobaike mirror)
670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1  body-898.html            (gmw 2017 report)
204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8  body-894live.html        (NAJ search)
c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0  body-894cap.raw          (NAJ search, 2026-04-22 capture)
813bdb125fa9f43a3003994ba42dc2549fbd778043de5f460b164f5125f28832  jiedu.pdf                (pmo.cas.cn 解读材料, 5 pp.)
```

## Tooling

No tool was installed or upgraded for this seat; no package manager was invoked (pacman is paused host-wide and was not touched). `curl`, `pdftotext`, `python3`, `sha256sum`, `md5sum` were already present (`/usr/bin/pdftotext`).
