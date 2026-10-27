# ScribeEntryD — gate notes, candidate d

**Verdict: REFUSE candidate d.** `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md` must not be installed. The draft at `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md` is a refusal record, not an entry, and is marked so on its first line.

Access date for every source below: **2026-10-27**. Every request was a plain `curl` with the browser-shaped User-Agent `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. No challenge was met or passed; no paywall, login, geo block or automation was used. Scratch: `/fast/scratch/hyaku/kotodama-r76/ScribeEntryD/` (deleted after receipts were copied to `stage/ScribeEntryD/`).

## S895 — xingzuobaike reproduction

- URL: `https://www.xingzuobaike.com/huangli/wannianli/d165803.html`
- Opened 2026-10-27, plain GET, HTTP **200**, **33,179 B**, `text/html; charset=utf-8`, sha256 `830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e`. Title: 「国家标准《农历的编算和颁行》GB/T 33661-2017 原文及解读材料 - 星座百科网」. Byline on the page: 老黄历网 2026-01-26 10:40:03.
- Located quote (18 chars, 7 words): 「公开发行的农历日历应注明资料来源」 — the first clause of the block that follows 标准主要内容 item 4 (the page's 对农历颁行要求的内容 block; served-text line 52 of my extraction).
- Second located quote (10 chars): 「本标准沿用规则如下」 — inside 标准主要内容, item 1, introducing the five numbered rules (served-text line 39).
- Third located quote (26 chars): 「取其中最先出现的一个不包含中气的农历月为农历闰月」 — inside 标准主要内容, item 1, rule (4) (served-text line 43).
- Locator scheme used in the draft and above: the page's own section headings (标准制定背景 / 标准制定意义 / 标准主要内容 / 对农历颁行要求的内容) plus the Arabic-numbered items inside 标准主要内容. Served-text line numbers are given only as a second handle; the extraction strips `<script>`/`<style>`, replaces block tags with newlines, unwraps the rest and drops empty lines, so the numbering is an artifact of that one pass and the headings are the stable locator.
- **REFUSE.** Reason, located: the page's title promises 原文及解读材料 but the body carries no 原文 structure — a sweep of the served text returns 0 for 前言, 0 for 范围, 0 for 规范性引用文件 and 0 for 术语和定义, and the string 原文 occurs twice, both in the title lines, neither in the body. What it carries is a 解读-shaped explanation whose 编排规则 are introduced in the drafting voice (「本标准沿用规则如下」), not as clause numbers. [INFERENCE from the heading shape and that first-person voice: the page reproduces a 解读/编制说明-type document, i.e. the same carrier class the lane already holds and the staged entry promised to replace.] Second located reason: the page's own provenance pointer contradicts its title — its last line prints 「此文件原载：https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296」, and that address, opened the same day, carries no 原文 at all (see S896 below).
- Flip: an A-tier carrier of the standard's normative text — the registry's full-text preview served to a plain client, or a ministry/academy reprint — printing the same clause. Then the reproduction becomes corroboration rather than the only carrier.

## S896 — openstd registry record (row bound to the Wayback capture)

- Row URL as planned: `https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`
- The bound capture **did not open from this host**: four attempts, each `curl: (7) Failed to connect to web.archive.org:443 … Could not connect to server`, HTTP `000`, 0 bytes. `https://web.archive.org/` itself answers the same on a direct HEAD. No archive fallback reachable; `timetravel.mementoweb.org` does not resolve here (`curl: (6) Could not resolve host`).
- The live document at the same `hcno` **did** open: `https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`, HTTP **200**, **24,144 B** after content decoding, `text/html;charset=utf-8`, sha256 `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9`, title 「国家标准|GB/T 33661-2017」.
- Located quote (18 chars): 「当前浏览器暂不支持标准全文在线预览服务」 — the 在线预览提示 notice on the record page (served-text line 37 of my extraction).
- Located field quote (11 chars): 「标准号：GB/T 33661-2017」 — first row of the 标准信息表 (served-text line 12). Further fields read off the same table: 标准状态 现行; CCS A46; ICS 07.040; 发布日期 2017-05-12; 实施日期 2017-09-01; 主管部门 and 归口部门 中国科学院; 发布单位 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会.
- **REFUSE as bound, ADMIT as document.** Reason: the URL the row binds does not open today, and the document it names carries identity, dates and custodianship only — no clause text of any kind (48 extracted lines, none of them a rule). As an A-tier carrier for the entry's load-bearing sentences it therefore carries none of them.
- Flip: re-point the row to the live `newGbInfo` URL and re-check the capture later; that makes the row usable for identity, dates and custodian, still not for the clause text.
- Collision note for the id map: `showGb?type=online&hcno=…` answers **302** with `Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…&refer=outter`, and `showGb?type=download&hcno=…` answers the same 302; the `/bzgk/gb/` variants 301 into `/bzgk/std/`.
- So the planned S897 (showGb) resolves to **one document** with the newGbInfo record — the plan's two registry rows are one page, which the by-document map should record.

## S898 — gmw.cn / 光明日报 report

- URL: `https://news.gmw.cn/2017-05/23/content_24559485.htm`
- Opened 2026-10-27, plain GET with `--compressed`, HTTP **200**, **25,250 B** after content decoding, `text/html`, sha256 `670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1`. Title: 「农历编算有了国家标准 春节端午等假期与其密切相关」; page credit 来源：光明网-《光明日报》, 「《光明日报》（ 2017年05月23日 01版）」, 记者陈海波.
- Located quote (14 chars): 「朔日为农历月的第一个农历日」 — article paragraph 4 (the paragraph beginning 此次发布的《农历的编算和颁行》), mid-sentence.
- Second located quote (17 chars): 「包含冬至在内的农历月为农历十一月」 — same paragraph 4.
- Third located quote (7 chars): 「精度应达到1秒」 — same paragraph 4 (the served text prints no space before 1).
- Fourth located quote (22 chars): 「必须包含公历和农历的日期对照以及二十四节气」 — article paragraph 5 (the paragraph beginning 这次国标对农历的颁行也提出规定).
- Fifth located quote (15 chars): 「中国科学院紫金山天文台起草编制」 — same paragraph 5.
- Locator scheme: P1–P5 are the five article paragraphs after the dateline 「光明日报北京5月22日电（记者陈海波）」; P4 is the paragraph beginning 此次发布的, P5 the paragraph beginning 这次国标.
- **ADMIT.** Reason: a state-press report of the promulgation, carrying the compilation rules it names, the model and 1-second precision, the publication duty, and the drafter. It is tier A for what the press reported that day, and for nothing wider.
- Negative sweep run on the same served bytes (all counts 0): 闰, 置闰, 干支, 生肖, 中气, 资料, 北京时间. So this page carries **none** of the leap rule, **none** of the naming methods, **none** of the source-labelling duty, and **not** the Beijing-time rule.
- Flip: not needed for the sentences it carries. If a later round finds an A-tier carrier for the leap rule and the naming methods, the entry can be re-filed and this row supports the half it already supports.

## Why the entry is refused — the admission test, run

The seat's rule: admit only if every load-bearing sentence also rests on an A/B row. The staged body's load-bearing sentences are the clause text (five compilation rules, four representation rules) and the promulgation duties (two of them).

- Rule (2) and rule (3), the model, the precision, and the solar–lunar/24-term duty: carried by S898, claimed holds.
- Rule (1), rule (4), rule (5), all four representation rules, and the source-labelling duty: carried by S895 alone.
- The S898 sweep is zero for every token that would carry them.
- S896 carries none of them: it is a metadata record with a preview control that will not serve the text.

So not every load-bearing sentence rests on an A/B row. **Refused.** A tier-C-only clause text would also be the sole support of the entry, which the claim's own kill rule forbids.

Two further defects found on the staged file, reported rather than repaired:

- Two of its three `couples:` targets do not exist at base. `git cat-file -e 98c486b:corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23.md` fails, and `git cat-file -e 98c486b:corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md` fails. Only `calendar-festival-systems.md` resolves.
- Its `gap filled:` bullet calls S718 the standard's registry record; at base that number is a row for an infant-directed-speech paper, not a registry record.
- The same bullet calls S719 the drafter's interpretation; at base that number is a row for a different infant-directed-speech paper.
- Lane S718 is a row for an infant-directed-speech paper (`corpus/SOURCES.md:673`), not a registry record.
- Lane S719 is a row for a different infant-directed-speech paper (`corpus/SOURCES.md:674`), not an interpretation of the standard. So the numbers there are campaign ids, not lane ids - the same id-space collision the round's collision guard exists for.

## Counters and checks run on the draft

- `python3 -B tools/check-cited-lines.py` on the draft: `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 (after one repair: the `- sources:` bullet originally carried three ids on one line and was split into three lines, one id each).
- Body length from `## §1`: 1,600 words (floor is 478).
- Table rows carrying an id: 0.
