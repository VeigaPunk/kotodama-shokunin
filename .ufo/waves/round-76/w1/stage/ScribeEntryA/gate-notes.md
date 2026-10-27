# Gate notes — ScribeEntryA, round 76 wave 1, target candidate a

Seat: `ScribeEntryA`. Draft under test: `drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`.
Access date for every row below: **2026-10-27**. Scratch: `/fast/scratch/hyaku/kotodama-r76/ScribeEntryA/` (deleted on exit; receipts copied to this stage dir).
User-Agent for every request below, verbatim: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.

## Row S898 — the 2017 report

- URL: https://news.gmw.cn/2017-05/23/content_24559485.htm
- Carrier: 光明日报 2017-05-23, 01版, 「农历编算有了国家标准 春节端午等假期与其密切相关」, byline 陈海波.
- Fetch: `curl -sS -L --compressed --max-time 60 -A "<UA above>"` → HTTP/1.1 200, 8,076 B on the wire, **25,250 B decompressed** (server sent gzip without an `Accept-Encoding` request; the first fetch without `--compressed` returned the gzip stream, which is why the first byte count read 8,076). `Content-Type: text/html`.
- sha256 (decompressed body): `670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1`.
- Located quote (24 chars, one line): 「规定了朔日为农历月的第一个农历日，包含冬至在内的农历月为农历十一月」 — **location: article body paragraph 4** (P1 = the byline-and-release paragraph; paragraph index counted over the served page's non-empty `<p>` elements in document order).
- Same-page capture, for durability (criterion 18): CDX `url=news.gmw.cn/2017-05/23/content_24559485.htm&filter=statuscode:200` → `20170523024955 … 200 … IHP5SRJMWRHJIGMLJVZ4LWLYYUS37MLD`. The capture is of the same path, so the live URL and the capture name one document.
- Verdict: **ADMIT**. Reason: the page is the state press's own report of the release, reached by a plain request, and it carries the anchoring rule, the model-and-precision sentence, the publication requirement, the drafter and the motive, each in a locatable paragraph. Flip to REFUSE if the rule sentences are not in P4–P5 of a re-opened copy (they were in this one), or if the page is reached only through a challenge (it was not: no challenge, no login, no paywall).

## Row S896 — the registry record

- Live URL: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296
- Read from: https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 (memento-datetime `Fri, 24 Apr 2026 03:10:27 GMT`; the capture's `Link: rel="original"` normalises to the live URL verbatim, query string included).
- Fetch: capture HTTP/2 200, 8,075 B on the wire, **24,174 B decompressed**, sha256 `f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e`. The live URL was also fetched on 2026-10-27: HTTP/1.1 200, 7,334 B, and it printed the same `标准号`/`GB/T 33661` fields.
- Located quote (18 chars): 「标准号：GB/T 33661-2017」 — **location: the record's first field row**.
- Auxiliary fields read off the same page (each used in the draft with the same id): 中文标准名称 农历的编算和颁行; 英文标准名称 Calculation and promulgation of the Chinese calendar; 标准状态 现行; 发布/实施日期 2017-05-12 / 2017-09-01; CCS A46; ICS 07.040; 主管部门 中国科学院; 归口部门 中国科学院; 发布单位 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会; 备注 present with an **empty** content cell (`grep -c 备注` = 1, the following `div.content` is blank).
- Limit recorded, not smoothed: the record's own preview notice reads 「当前浏览器暂不支持标准全文在线预览服务，请使用现代浏览器…」, i.e. the page offers identity fields and points a full-text reader elsewhere. No clause text exists in this window.
- Verdict: **ADMIT**. Reason: official registry, plain copy, same-page capture, and every field quoted is a labelled cell on the page. Flip to REFUSE if the capture's embedded original stops normalising to the live URL, or if a re-opener finds the 发布日期 cell reading a different date (it read 2017-05-12 on both the capture and the live page on 2026-10-27).

## Row S894 — the archive era table

- Live URL: https://www.digital.archives.go.jp/search (page title 「詳細検索 | 国立公文書館デジタルアーカイブ」)
- Read from: same page live **and** https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search (memento-datetime `Wed, 22 Apr 2026 14:50:52 GMT`).
- Fetch: live HTTP/1.1 200, 311,308 B, sha256 `204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8`; capture HTTP/2 200, 307,700 B, sha256 `c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0`.
- Located quote (19 chars, a table head plus its first row): 「元号名称 開始西暦年 令和 2019」 — **location: the `#gengo-modal` 元号選択 modal, 和暦元号 tab, table head and first data row**; the same modal's tabs are 和暦元号 / 中国元号 / 朝鮮元号.
- Counted, both artifacts, same script: 和暦元号 **248** data rows (head 令和 2019, 平成 1989, 昭和 1926, 大正 1912, 明治 1868; tail 白雉 650, 大化 645); 中国元号 **94** rows (head 康徳 1934, 大同 1932, 民国 1912, 清宣統 1909; tail 金天輔 1117, 金収国 1115); 朝鮮元号 **8** rows (朝鮮乾隆 1736 … 朝鮮永楽 1403). The capture additionally carries a `<select>` whose options repeat the mapping as `data-yyyy` attributes (明治 1868 … 令和 2019).
- Negative, located on both artifacts: `grep -o 詔勅 | wc -l` = **0**, `勅令` = **0**, `勅書` = **0** in the live page and in the capture. The staged text's description of this table as the 詔勅・勅令・勅書 database is therefore **not the page's own framing**; the carrier is the archive's advanced-search era selector. The draft says the selector and drops the staged phrase.
- Verdict: **ADMIT**, with the correction above. Reason: tier-A national archive, both a live copy and a same-page capture, and the table is machine-countable in both artifacts with identical row counts. Flip to REFUSE if the modal's table head or the five modern-era rows stop locating, or if the 詔勅-family strings are found on a re-opened page (they were absent on 2026-10-27).

## The three sentences this seat REFUSES

1. **The leap-month rule.** The report never uses 闰: `grep -o 闰` on the served page = **0** and on its extracted text = **0**; 冬至 occurs twice, 朔 twice, always in the anchor and model sentences. So no page read here states **how** the leap month is selected. The staged text's "leap-month rule" sentence is refused; the draft keeps the month-11 anchor and marks the derived selection rule `(to-verify)`.
2. **The 詔勅・勅令・勅書 database** as the carrier of the era table — refused on the located zero counts above; replaced by the archive's own framing.
3. **The Barthes/Marrone "codes/levels" comparison** staged in the same file — refused as off-theme for a calendar amendment: it is narrative theory, it belongs to `myth-symbol/narrative-structure-frameworks.md`, and neither campaign id (S919/S921 → lane S892/S885) was opened for this entry. It is not cited, and the draft's `- scope:` line says so.

**Plainly:** the staged text as delivered should be **REFUSED** for sentences 1–2 (the first overreaches the page, the second misnames it) and sentence 3 should be cut as off-theme; the draft staged here refuses all three and is admissible on rows S898, S896 and S894.

## Id hazard noticed while gating (not used, reported to the round)

The staged file's older section cites `S750`, `S776`, `S777`, `S807` as if they were this standard's rows. At base `98c486b` those ids are other documents (S750 = Culin 1907; S776 = Pearson 2016; S807 = a 2021 anatomy paper), and `git show 98c486b:corpus/SOURCES.md | grep -c 33661` = 0. No lane-id-looking citation from the staged text is carried into the draft; all three rows are cited by document.

## Commands used for the checks in this file

```
sha256sum s898b.html s896b.html s894live.html s894w.html
python3 -  # extract <p>/<td> text, count rows per gengo tab, count 詔勅/勅令/勅書
grep -o '闰' s898b.html | wc -l              # 0
grep -o '閏' s898.txt | wc -l                # 0
grep -o '詔勅' s894live.html | wc -l          # 0   (same for s894w.html)
curl "https://web.archive.org/cdx/search/cdx?url=news.gmw.cn/2017-05/23/content_24559485.htm&output=json&limit=5&filter=statuscode:200"
python3 -B tools/check-cited-lines.py <draft>  # CITED-LINES: 0 finding(s) in 1 file(s), exit 0
```
