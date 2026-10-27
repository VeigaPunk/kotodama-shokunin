# Amendment — what a calendar standard's announcement fixes, and an era table that carries its own start years

- source: S896 — https://news.gmw.cn/2017-05/23/content_24559485.htm — 光明日报 2017-05-23, 01版, 「农历编算有了国家标准 春节端午等假期与其密切相关」, byline 陈海波; P1–P5 are the five article-body paragraphs in document order, P1 = byline-and-release paragraph; a same-page Wayback capture exists at timestamp 20170523024955 (status 200) — fetched 2026-10-27 (HTTP 200, 25,250 B decompressed, sha256 670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1)
- source: S895 — https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 — 全国标准信息公共服务平台, the GB/T 33661-2017 record; read live and from Internet Archive capture https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 (memento 2026-04-24T03:10:27Z); locators are the page's field labels 标准号, 中文标准名称, 英文标准名称, 标准状态, 发布日期, 实施日期, 中国标准分类号（CCS）, 国际标准分类号（ICS）, 主管部门, 归口部门, 发布单位, 备注, plus the online-preview notice — fetched 2026-10-27 (live HTTP 200, 24,144 B decompressed, sha256 80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9; capture HTTP 200, 24,174 B decompressed, sha256 f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e)
- source: S894 — https://www.digital.archives.go.jp/search — 国立公文書館デジタルアーカイブ, 詳細検索, the 元号選択 modal; read live and from the Internet Archive capture https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search (memento 2026-04-22T14:50:52Z); locators are the modal's three tabs (和暦元号, 中国元号, 朝鮮元号) and its table columns 元号名称 / 開始西暦年 — fetched 2026-10-27 (live HTTP 200, 311,308 B, sha256 204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8; capture HTTP 200, 307,700 B, sha256 c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0)
- verified-at: 2026-10-27
- recheck: 180d — re-open the three live URLs and re-locate every cited span at its named locator. The Gate quotes are in `reports/round-76/evidence/`; additional era-table boundaries are rechecked against the committed full-page S894 live/capture files under `.ufo/waves/round-76/w1/stage/ExecCensusRows/window/`. The same-page archive captures are alternate carriers, not evidence that these pages require a browser. If a span stops locating in its declared carrier, the affected row is unverifiable rather than the claim softened.

- ground: at base 98c486bdb4650ba5b8e651d332910e8ee60ad121 the knowledge corpus held no row for this standard — `git grep -l -E 'GB/T 33661' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge` exits 1 with no output — and the base entry `culture-material/calendar-festival-systems.md` carries intercalation strategy and the politics of the leap (§2) without either the announced rules of a modern state standard or an era table with start years.
- topic: what a promulgated calendar standard's announcement fixes — its anchoring rule, its computation model and precision, what a published calendar must carry, and who drafted it — what the registry's own record does and does not carry, and one archived era-name table whose rows are a name plus a start year across three era systems.
- gap filled: the base entry says which leap strategies exist and who owns them; it does not say what a modern state's calendar standard actually fixes, and it holds no citable era table. This amendment adds both from the opened sources, and records the one rule a reader would most expect — how the leap month is chosen — as absent from every page read here.
- sources: the three rows above — one tier-B state-press report of a regulator's release, one tier-A registry record of the standard itself, and one tier-A archive page whose table the sections below transcribe. The standard's own clause text is not read by this amendment.
- couples: `culture-material/calendar-festival-systems.md` (the base this amends); `culture-material/timekeeping-instruments.md` (the instruments the anchor rule presupposes); `culture-material/era-periodization-models.md` (era-name craft and 元号法; this file adds only the form name + start year); `linguistics/naming-systems.md` (era coining and the label-versus-self-designation problem); `synthesis/worldbible-integration-contract.md` (the canon handoff this file stops at).
- scope: an amendment to the calendar entry. It records one standard's announced rules, one registry identity record, one era table, and the checks that follow; it decides no world's calendar and makes no rights or attribution ruling. It also declines the staged file's Barthes/Marrone codes comparison, which is narrative-theory material belonging to `myth-symbol/narrative-structure-frameworks.md` and is off-theme here (flagged to the round).

## §1 The announcement fixes four things, and only one of them is an anchor

The report is the state press's account of a batch release, and it states the batch plainly: 「国家标准委22日发布了《农历的编算和颁行》等334项国家标准」 (loc. P1) (S896). Its own framing of the change is institutional rather than astronomical: 「这次标准的制定首次将农历编算和颁行纳入国家标准化管理体系」 (loc. P1) (S896).

The anchoring rule is one sentence with two clauses, and both clauses matter: 「规定了朔日为农历月的第一个农历日，包含冬至在内的农历月为农历十一月」 (loc. P4) (S896). The first clause fixes day 1 of every lunar month to the day of the new moon; the second fixes month number 11 to the lunar month that contains the winter solstice. Everything else in a lunisolar calendar follows from those two choices, which is why the standard can be stated so briefly.

Model and precision are given as one requirement, not two: the times of new moon and of the solar terms 「必须按国际天文学规范中关于天体位置计算所规定的模型来计算，精度应达到1秒」 (loc. P4) (S896). The report states the tolerance as 「1秒」 without saying whether the second is a second of time or of arc; this entry does not resolve that and keeps the page's own word (to-verify).

What a published calendar must carry is a third, separate requirement: 「要求公开发行的日历产品必须包含公历和农历的日期对照以及二十四节气」 (loc. P5) (S896). The date correspondence and the twenty-four solar terms are the minimum content, and the same sentence requires conformity with 「标准规定的编排规则、计算模型和精度及表示方法」 (loc. P5) (S896).

The drafter is named as an institute, not a ministry: 「国标由国内唯一的历书编算机构，中国科学院紫金山天文台起草编制」 (loc. P5) (S896). That sentence is the only place in the three rows where computational authority is attributed to a body that computes, rather than one that regulates.

The report also states the problem the release was meant to answer, and it states it as a public-experience failure rather than an error bound: 「如2013年的端午和冬至都分别有不同的日期版本，引起了公众困惑和使用混乱」 (loc. P2) (S896). Its account of the cause is that publication was open to anyone with printing capacity: 「任何有印刷资质的单位和个人都可以公开自行编制或复制农历日历」 (loc. P3) (S896).

**What the page does not state.** The report never uses the word 闰 (it occurs zero times in the served article and in its extracted text), so the leap-month *selection* rule is not on this page. What the page gives is the month-11 anchor; that a leap month is the one left over when the anchor is satisfied is a derivation this entry marks (to-verify) against the standard's clause text, which no row read here contains. A writer modelling a calendar standard should state the anchor and mark the derived rule, because the two are different strengths of claim.

## §2 The registry record carries identity, and says so

The record identifies the document completely enough to cite it without the press: 标准号 GB/T 33661-2017, 中文标准名称 「农历的编算和颁行」, 英文标准名称 "Calculation and promulgation of the Chinese calendar", 标准状态 现行 (loc. field 标准号 through 标准状态) (S895). Two dates are printed and they are not the same date: 发布日期 2017-05-12 and 实施日期 2017-09-01 (loc. fields 发布日期, 实施日期) (S895). The classification fields list 中国标准分类号（CCS）A46 and 国际标准分类号（ICS）07.040 (loc. fields CCS, ICS) (S895); this entry records the printed codes without inferring their taxonomy or institutional meaning.

Custody is two-layered and both layers sit in the same academy: 主管部门 中国科学院 and 归口部门 中国科学院, with 发布单位 「中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会」 (loc. fields 主管部门, 归口部门, 发布单位) (S895). The registry therefore places stewardship in the academy while the press places drafting in one of its observatories — the two rows name different links of one chain, and neither alone gives the whole chain.

The record also limits itself, in its own words. Its full-text notice tells the re-opener to reopen the page in a modern browser to continue 「标准全文预览」 (loc. preview notice) (S895), so this page is an identity carrier and not a clause carrier. The 备注 field is present with no text in it (loc. field 备注) (S895), so nothing in the record qualifies the dates above.

One date needs care, because two carriers print two dates. The registry's 发布日期 field reads 2017-05-12 (loc. field 发布日期) (S895), and that is the date the record itself puts on publication.

The press, for its part, reports the release on the 22nd: 「国家标准委22日发布」 (loc. P1) (S896). Both statements are carried here and they are not reconciled. A worldbuilder copying an "announced on" date for an invented standard should decide which event the date marks — signature, registration or press release — because a real registry distinguishes them.

## §3 An era table: a name, a start year, and whose naming it is

The archive's advanced-search page carries the era list as a selector rather than as an article: a modal headed 元号選択 with three tabs — 和暦元号, 中国元号, 朝鮮元号 — and, under each tab, a table whose columns are 元号名称 and 開始西暦年 (loc. 元号選択 modal, tab headers and table head) (S894).

The 和暦 tab holds 248 data rows. Its head is the five modern eras with their start years in the archive's own column: 令和 2019, 平成 1989, 昭和 1926, 大正 1912, 明治 1868 (loc. 和暦元号 tab, first five rows) (S894). The list does not stop at the modern set: it runs back past 慶応 1865 and 元治 1864 to 白雉 650 and 大化 645 (loc. 和暦元号 tab, last two rows) (S894).

The other two tabs show that the instrument is comparative by design. 中国元号 holds 94 rows, beginning 康徳 1934, 大同 1932, 民国 1912 and 清宣統 1909 and running back to 金天輔 1117 and 金収国 1115 (loc. 中国元号 tab, first and last rows) (S894). 朝鮮元号 holds 8 rows from 朝鮮乾隆 1736 to 朝鮮永楽 1403 (loc. 朝鮮元号 tab, first and last rows) (S894).

Both the live page and its capture carry the same 248 和暦 rows in the same order, and both carry `<select>` options with the matching era-name/start-year pairs (明治 1868, 大正 1912, 昭和 1926, 平成 1989, 令和 2019) (loc. live and capture, 和暦 rows and option list) (S894). This is a cross-carrier check, not a capture-only feature. Second, the page does not describe itself as a 詔勅 or 勅令 database: those strings occur zero times in the live page and zero times in the capture, so the carrier is this archive's search selector, not the document series a staged draft named (loc. page and capture, whole document) (S894).

The design lesson is the label problem. A row of this table is three fields — name, start year, system — and the third field is not decoration: the 中国元号 tab prefixes names it did not coin (清宣統, 金天輔), and it files 民国 1912 beside 康徳 1934, so the tab is one archive's finding aid across several naming regimes. An era table is usable exactly to the extent that it says whose label each name is.

## §4 Calibration

**The standard's identity, status, dates and custody — mainstream.** The registry record is the official carrier for exactly these fields, and nothing read here disputes them (S895).

**The standard's rules as announced — mainstream as an announcement, unread as a clause.** The state press reports a regulator's release and states the rule in the regulator's own vocabulary (S896); the standard's clause text is not in any window opened here, so every rule sentence is carried at the strength "as announced", never "as enacted". Where this entry needs the exact normative wording, it marks (to-verify).

**"The standard ended calendar inconsistency" — not claimed, and not claimable from these rows.** The report describes the prior inconsistency as a problem and the release as a remedy in prospect; it reports no measurement after 2017, and no page read here measures one (S896).

**An era table as an instrument — mainstream; its labels, one archive's.** The table is a plain finding aid in a national archive, and its five modern-era start years are the ones a re-opener can count off the page (S894). Its Chinese and Korean tabs are the archive's own filing of other states' era names, so the table is mainstream for the form (name + start year + system) and is not a chronology of any state (S894).

**The Barthes/Marrone codes comparison — dropped, and flagged.** The staged file carried a second passage comparing narrative "codes" and "levels". It is not a coupling this calendar entry can carry: it is narrative theory, its own lane entry already holds it, and the staged text's two campaign ids were never opened for this amendment. It is removed here and reported to the round rather than cited.

## §5 What a worldbuilder does with this

**Checklist, in order.**

1. Fix the anchor before the arithmetic. Name which astronomical event fixes which month number; a calendar standard that starts with month lengths has started in the wrong place.
2. State the model and the tolerance in one sentence, and name who computes it. A tolerance without a computing body is a wish.
3. List what a published calendar must print. The minimum set is the correspondence between the two reckonings plus the term table; anything else the authority wants printed is a separate rule.
4. Write the custody chain as separate links — regulator, custodian, computing institute — because a real chain names different bodies at each link, and a world's chain will be read as a political map.
5. For eras, record three fields per row: name, start year, and the system the name belongs to. Where a name is not the era's own, say so.
6. When a rule matters to the plot, cite the page that states it; if only the anchor is stated, mark the derived rule (to-verify) and let a later round find the clause.

**Decision table — what the announcement fixes, and what the authority still decides.**

| the design question | what the announced rule fixes | what the authority still decides |
|---|---|---|
| which lunar month is month 11 | the month containing the winter solstice | how the solstice instant is computed and rounded |
| which day is day 1 | the day of the new moon | the time zone and the cut-off that turn an instant into a day |
| how close is close enough | a stated precision, computed under a named model | which model, and the observing data behind it |
| what a printed calendar carries | date correspondence and the solar-term table | layout, presentation and any additional content |
| which month is the leap month | nothing stated on these pages | the selection rule itself, which a clause text must supply |
| how eras are named | nothing — a separate instrument | the naming authority, the label and its start year |

**Decision table — what the note must record when a world adopts such a standard.**

| field | required when | why |
|---|---|---|
| anchor rule | any lunisolar calendar in play | it is the only rule the other rules derive from |
| model and tolerance | any calendar claimed to be computable | an announcement states both, and the pair is the claim |
| publication minimum | any in-world printed calendar | it is what makes the calendar a public instrument |
| custody chain | any calendar with a state behind it | it locates the politics without inventing it |
| era rows, three fields | any era-naming system | a name without a start year and a system cannot be checked |

**Worked example, no canon decided.** A world's almanac office is asked why its festival dates moved. The note it writes is not a history of the reform: it states the anchor (the month holding the solstice is the eleventh), the model and the second-level tolerance, the two columns a published almanac must print, and the three offices that signed. The era table, if the world has one, is a separate instrument with its own authority — and the festival complaint is answered by the anchor, not by the era names.

## §6 What this amendment does not establish, and the handoff

- No clause text. Every rule statement here is the announcement's, and the standard's own wording stays unread; the leap-month selection rule is explicitly absent from all three pages.
- No measurement of the reform. The report's 2013 example is the problem's evidence, not the remedy's effect; no page read here counts divergent calendars before or after.
- No ruling on the 1-second tolerance: the page does not say whether the second is of time or of arc, and this entry leaves the word as the page prints it (to-verify).
- No rights, licence or attribution ruling about any standard, archive or table, and no canon: nothing here says what any fictional world's calendar holds.
- The era table is recorded as an instrument and its labels as the archive's; the table is not offered as a chronology, and no state's era sequence is asserted from it.
- Handoff: a calendar standard, an era table and the custody chain behind them are world-bible records, which `synthesis/worldbible-integration-contract.md` hands to lore; this entry ends at that handoff and records no canon.
