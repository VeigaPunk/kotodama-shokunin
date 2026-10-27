# REFUSAL — candidate d is not installable: the page carries no 原文, and no A/B row carries the clause

status: REFUSED 2026-10-27 (ScribeEntryD). This file is a gate record, not a knowledge entry: it must NOT be installed under `corpus/knowledge/`. The staged body it answers is `merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md`.

source: S895 — https://www.xingzuobaike.com/huangli/wannianli/d165803.html — the 星座百科网 page titled 「国家标准《农历的编算和颁行》GB/T 33661-2017 原文及解读材料」, body running from the heading 标准制定背景 through the block 对农历颁行要求的内容; opened 2026-10-27 (HTTP 200, 33,179 B, sha256 830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e)
source: S896 — https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 — the 标准信息表 field rows of the national standards registry record; opened 2026-10-27 (HTTP 200, 24,144 B after content decoding, sha256 80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9). The row's bound capture `web.archive.org/web/20260424031027id_/…` did not open from this host: curl exit 7 on four attempts.
source: S898 — https://news.gmw.cn/2017-05/23/content_24559485.htm — the article body, the five paragraphs that follow the dateline 光明日报北京5月22日电（记者陈海波）; opened 2026-10-27 (HTTP 200, 25,250 B, sha256 670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1)
verified-at: 2026-10-27
recheck: 180d — re-open the three URLs and re-locate every span at the locator named beside it; re-run the preview probe `curl -sS -D - -o /dev/null 'https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296'` and confirm it still answers 302 to the record page rather than serving the standard's text.
ground: the lane at 98c486b holds no row for this standard and no knowledge file that prints its rules. `git grep -l -E '33661' 98c486b -- corpus` returns only `corpus/lessons/round-68.md` and `corpus/lessons/round-69.md`; `git grep -l -E '农历的编算' 98c486b -- corpus` and `git grep -l -E '紫金山' 98c486b -- corpus` each print nothing (exit 1). The gap the staged entry names is real; the carrier it names does not fill it.

- topic: the normative clause text of GB/T 33661-2017《农历的编算和颁行》 — the compilation rules, the calculation model and its precision, the representation methods, and the promulgation duties — as a standard's own text rather than a summary of it.
- gap filled: none. This record fills no gap and adds no entry. It states why the candidate cannot be installed and what would install it.
- sources: the three rows above, all opened 2026-10-27 by a plain request under the browser-shaped UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, with no challenge met or passed, no paywall, no login, and no archive fallback available on this host for the registry row.
- S895 is tier C: a reproduction, and it is quoted here only as what that reproduction says.
- S896 is the registry's identity record: tier A for identity, dates and custodianship, and nothing else.
- S898 is tier A for what the state press reported on the day of promulgation, and for nothing wider.
- couples: `culture-material/calendar-festival-systems.md` only. The staged entry's other two couples targets do not exist at base — `git cat-file -e 98c486b:corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23.md` and `git cat-file -e 98c486b:corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md` both fail.
- scope: a refusal of one candidate entry. It asserts nothing about any calendar's rules, decides no world's canon, makes no rights or attribution ruling on the reproduction, and stops at the lore handoff. It records what three pages carry, and what a worldbuilder may therefore write down today.

## §1 The verdict, and the three located reasons

The staged entry's whole value is one sentence — that the lane can now quote *the standard's own clause text* instead of the drafter's explanation of it. Three checks defeat that sentence, and each is a located fact about bytes I fetched today, not a judgement about the reproduction's quality.

**R1 — the page has no 原文 block.** The title promises 原文及解读材料, but the body is entirely 解读-shaped. Its section headings are 标准制定背景, 标准制定意义 and 标准主要内容; the last of these runs four numbered items, and it is the first of them that carries the five rules. A sweep of the served text for the structural headings any Chinese standard's text carries returns zero for each: 前言 0, 范围 0, 规范性引用文件 0, 术语和定义 0. The string 原文 occurs twice and both occurrences are in the page's own title and heading lines, neither in the body. So the page does not print the standard's normative text; it prints an explanation *about* the standard, which is the very class of carrier the entry said it would replace. [INFERENCE from the heading shape and the first-person drafting voice at 「本标准沿用规则如下」: the body reproduces a 解读/编制说明-type document. The inference is why the entry's premise fails even before the tier test.]

**R2 — every load-bearing sentence of the staged body is tier-C only.** The staged body has two sections: the clause text with the leap-month rule and the four representation rules, and the promulgation duties. Run them against the two A/B candidates and the result is uniform: the state press carries two of the five rules and part of the promulgation duty, and carries nothing of the leap rule or the naming methods. The registry record carries no rule at all.

**R3 — the entry would double-count, not add.** Even the half that an A/B row does carry is already claimed elsewhere in this round: the staged candidate a carries the same announcement material from the same document. A narrowed candidate d would restate candidate a's first section and nothing more.

## §2 The test, sentence by sentence

The admission rule for this seat: the entry may be admitted only if it also rests on an A/B row for every load-bearing sentence. The table sets out the result. No row of it carries a source id; the citations follow it, one per line.

| Staged sentence | A/B carrier that would have to hold it | Result |
|---|---|---|
| Rule (1): Beijing time is the standard time | none — the press report does not state it | fails |
| Rule (2): the new-moon day is the first day of the lunar month | the press report states it in the compilation-rules paragraph | holds |
| Rule (3): the lunar month containing the winter solstice is the eleventh month | the press report states it in the same paragraph | holds |
| Rule (4): with 13 months between two eleventh months, the first month lacking a 中气 is the leap month | none — the press report never uses 闰 or 置闰 | fails |
| Rule (5): the second month after the eleventh, not counting a leap month, begins the year | none | fails |
| The representation rules: gan-zhi and zodiac years, numbered months with the 闰 prefix, numbered and gan-zhi days, the combined date label | none — the press report never uses 干支 or 生肖 | fails |
| Calculation model per the international astronomical standards | the press report states the model requirement | holds |
| Precision to 1 second | the press report states 1 秒 | holds |
| A published calendar must carry the solar–lunar correspondence and the twenty-four solar terms | the press report states both | holds |
| A published calendar must state its data source | none — the press report never uses 资料 | fails |
| The drafter is 中国科学院紫金山天文台 | the press report names the observatory | holds |

The sweep behind the negative column, run on the served press page:

- The string 闰 does not occur on the page (count 0), and neither does 置闰 — so the leap-month rule is not carried by the only A/B carrier that states any rule (S898).
- The strings 干支 and 生肖 do not occur on the page (count 0 each), so none of the representation rules is carried there (S898).
- The string 资料 does not occur on the page (count 0), so the source-labelling duty rests on the reproduction alone (S898).
- The string 北京时间 does not occur on the page (count 0), so rule (1) rests on the reproduction alone (S898).
- The registry record carries the standard's number, both titles, its status, its classification codes, its publication and implementation dates, its custodians and issuing bodies — and no clause text of any kind (S896).
- The registry's own preview control does not serve the text to a plain client: the online-preview call answers 302 with `Location: …/newGbInfo?hcno=…&refer=outter`, and the record page prints 当前浏览器暂不支持标准全文在线预览服务 (S896).
- The reproduction's own provenance pointer contradicts its title: it ends 此文件原载 with the same registry address, and that address carries no 原文 (S895).
- The reproduction's 编排规则 numbering is the drafting voice, not a clause number: the rules are introduced inside 标准主要内容 as 本标准沿用规则如下 (S895).

## §3 What a worldbuilder may take today

The refusal is not a shrug: three of the eleven staged statements are citable at tier A, and they are the ones that matter most for modelling a calendar *as an institution*.

| Question a worldbuilder asks | What may be written today | Warrant |
|---|---|---|
| Who fixes the first day of a lunar month? | The new-moon day is day one, by rule | A (press) |
| Which month is the anchor month? | The month containing the winter solstice is the eleventh | A (press) |
| How exact must the arithmetic be? | Model per the international astronomical standards; precision 1 second | A (press) |
| What must a published calendar carry? | Solar–lunar correspondence and the twenty-four solar terms | A (press) |
| Who may be named as the drafting body? | 中国科学院紫金山天文台, with 中国科学院 as custodian | A (press, registry) |
| What are the standard's dates and status? | Published 2017-05-12, in force 2017-09-01, status 现行 | A (registry) |
| How is a leap month chosen? | Design freely; the rule is a lead, not a quotable clause | C (reproduction) |
| How are years, months and days named? | Design freely; the naming methods are a lead | C (reproduction) |

A checklist for anyone who wants to put "the standard says" into a lore note:

1. Quote the rule only if the sentence you are writing is on the rows above marked A; otherwise write "one reproduction states" and date it.
2. Never print a clause number as the standard's own unless you have the standard's text: a heading like 编排规则 inside an explanation is not a clause.
3. When a reproduction names an original, open that original and check the claim: here the pointer led to a record page with no text.
4. Prefer the institution to the clause: a calendar published by an academy is a different worldbuilding object from a calendar computed by priests, and the A rows carry the institution.
5. Treat the 1-second precision as a design constraint with teeth: it is what forces a calendar standard to name a model and an ephemeris, not just a rule set.

## §4 Calibration

The standard itself is `mainstream` in the only sense that matters here: it is a live national standard, status 现行, in force since 2017-09-01, and no source I opened disputes it. What is `contested` is the reproduction's standing as a carrier of the standard's text: it presents itself as the 原文, its own pointer leads to a page that carries no 原文, and no A/B carrier I opened repeats its leap rule or its naming methods. Nothing here is `discredited`: the rules the reproduction prints are consistent with what the press reports where the two overlap, and I found no conflicting version of any of them. The calibration claim, then, is narrow and exact: the *rules as announced* are mainstream and citable; the *clause text* is a contested attribution and is not citable at all.

## §5 The flip

Three conditions, any one of which would make a successor entry installable without weakening this refusal:

- The registry serves the standard's full text to a plain client, and the served text prints the compilation rules, the representation methods and the promulgation duties as numbered clauses. The probe that decides it is in the `recheck:` line above; today it answers 302 to the record page.
- A second A-tier carrier reproduces the leap rule and the naming methods — an academy page, a ministry announcement, or a standards-service reprint — so that no load-bearing sentence rests on the reproduction.
- The entry is re-scoped to the rules as announced, and it then cites the press row for every load-bearing sentence, keeps every reproduction-only sentence out, and is filed against the announcement material rather than as a new entry beside it.

Until one of those holds, the honest disposition is this record. A refusal with a located reason costs the round nothing it did not already lack; an entry that calls a 解读 a 原文 would cost it the distinction the standard exists to make.
