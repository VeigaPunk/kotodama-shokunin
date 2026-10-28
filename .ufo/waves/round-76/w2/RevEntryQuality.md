# RevEntryQuality — round-76 W2 — landed calendar-festival amendment review

Seat: RevEntryQuality (reviewer, leaf — no subagents). Date: 2026-10-27.
Revisions used (all reads via `git show` against pinned commits, not the mutable worktree):

- base `98c486bdb4650ba5b8e651d332910e8ee60ad121`
- frozen C/Ca configuration `df0f0309d61e5485bb17035d3f8791b1e6a11d40`
- **landing under review `788bd566cb613e946fcaf03ec5c26368ba11d956`** ("round-76: add sourced calendar standard amendment", parent of C landing `722e69ff…`); the calendar amendment is the file `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` (109 lines; line numbers below are its numbering at this commit)
- Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c` (SCORECARD/SKILL only; no entry bytes)

Method: span-by-span verification of the amendment against the committed evidence windows (`reports/round-76/evidence/S894.txt`, `S895.txt`, `S896.txt` at the landing; window = line 35 of each) and the committed w1 full-page captures (`.ufo/waves/round-76/w1/stage/ExecCensusRows/window/…`), matching whitespace-folded per each window's own `normalise:` rule. No live fetch was made by this seat; no builds/tests/linters run; no files outside this report were written. Tooling: **no installs or upgrades performed** (read-only wave; nothing to record under the tooling directive). Scratch `/fast/scratch/hyaku/kotodama-r76/RevEntryQuality-2` was used for extracted blobs and removed before yielding.

## Verdict

**Accept the entry as landed, with one substantive correction owed (F1) and four minor locator/wording defects (M1–M4).** Every evidence-bearing quote, field value, count, and digest in the amendment verifies against committed bytes; tier use is correct and correctly scoped; topic fit, gap, couples, and the dropped-passage handling all check out. The one factual overreach is an interpretive sentence about the classification codes, not any quoted datum.

## Findings

### F1 — MEDIUM · factual overreach: the CCS/ICS gloss inverts what the codes mean

`calendar-festival-systems.amend-2026-10-24.md:34`:

> "The classification fields place it **outside astronomy proper** — 中国标准分类号（CCS）A46 and 国际标准分类号（ICS）07.040 (loc. fields CCS, ICS) (S895) — which is itself the institutional point: a calendar is filed as a standard for general use, not as an almanac."

The quoted field **values** are correct (S895.txt window line: `中国标准分类号（CCS） A46 国际标准分类号（ICS） 07.040`, each ×1; also present ×1 in the committed live fetch `w1/stage/ExecCensusRows/window/S896-openstd.newGbInfo-live-2026-10-27.html`). But the interpretive sentence built on them is backwards:

- ICS 07.040 is ISO's "**Astronomy. Geodesy. Geography**" class (https://www.iso.org/ics/07.040.html) — i.e., it files the standard *inside* astronomy.
- CCS/中标分类 A46 is 天文学 (astronomy; Chinese registry detail pages for GB/T 33661-2017 give `中标分类 A46 天文学`, e.g. std.samr.gov.cn gbDetailed records surfaced by web search).

So both fields place the standard **in** astronomy, and the drawn "institutional point" (general-use standard, not almanac) is unsupported by — indeed contradicted by — the cited fields. The page itself prints only the codes; the gloss is the entry's own inference presented as if it followed from the record. Contained damage: no other section or decision table repeats the claim, and §2's sourced sentences around it are accurate — but this sentence should not survive the entry's own 180d recheck standard.

### M1 — MINOR · S895 locator enumeration under-covers the locators §2 actually uses

The S895 source line (`:4`) declares "locators are the record's own field labels — 标准号, 标准状态, 发布日期, 实施日期, 主管部门, 归口部门, 发布单位, 备注". §2 then cites "loc. field 标准号 through 标准状态" (a range crossing the un-enumerated 中文标准名称/英文标准名称 labels), "loc. fields CCS, ICS" (`:34`; un-enumerated labels), and "loc. preview notice" (`:38`; not a field label at all). The spans all locate in the committed window (中文标准名称：农历的编算和颁行, 英文标准名称：Calculation and promulgation of the Chinese calendar, CCS A46, ICS 07.040, 在线预览提示…标准全文预览 notice — all ×1 in S895.txt), and SOURCES.md:850's scope cell ("identity, status, dates, classification and custodial fields only") already authorizes the use — the defect is the amendment's own locator declaration, not the evidence.

### M2 — MINOR · S896 declares a P6 the article does not have

`:3` declares "locators P1–P6 are the article body's paragraphs in document order". The served article body (S896.txt whole-document extract, 1,487 visible chars) has **five** body paragraphs: P1 byline-and-release (光明日报北京5月22日电（记者陈海波）国家标准委22日…), P2 (…2013年的端午和冬至…使用混乱。), P3 (…任何有印刷资质的单位和个人…), P4 (此次发布的…精度应达到1秒。), P5 (这次国标对农历的颁行…起草编制。); what follows is the page marker 《光明日报》（2017年05月23日 01版） and an editor credit, not a sixth body paragraph. P6 is declared but phantom and unused. All used locators P1–P5 verified (see ledger).

### M3 — MINOR · "additionally a `<select>`" implies a capture/live difference that does not exist

`:52` says the capture "carries the same 248 和暦 rows in the same order, **and additionally** a `<select>` whose options repeat the mapping as attributes (明治 1868, 大正 1912, 昭和 1926, 平成 1989, 令和 2019)". Measured: live and capture each carry the same 7 `<select>` blocks, including two era dropdowns whose options carry exactly those attribute pairs (`value="244" data-yyyy="1868"` 明治 … `value="248" data-yyyy="2019"` 令和; `data-yyyy="1868"` occurs ×3 in each carrier). The select is not capture-exclusive. The check's conclusion is unaffected — the capture does corroborate the table, and the last option's `value="248"` for 令和 itself corroborates the 248-row count — but the contrast drawn ("additionally") is factually wrong about which carrier distinguishes itself.

### M4 — MINOR · recheck parenthetical mischaracterizes S894 as browser-gated

`:7` says "(the capture is the carrier for any page that gates its tables behind a browser)". For S894 this is false descriptively: the era tables are server-rendered in the plain-client HTML — the curl-fetched live page (311,308 B) contains all 350 table rows, as does the capture. The genuinely browser-gated surface is S895's 在线预览 notice (verified in the S895 window). Read as a conditional ("if a page gates its tables, use the capture") the clause is harmless; read as a description of these carriers it is wrong for S894.

### I1 — INFO · evidence-window coverage: §3's tail spans live in w1 captures, not the three named evidence files

S894.txt stores an **excerpt** window (4,103 chars of a 6,815-char extract) covering the modal, the three tab names, the table columns, and the **first five** 和暦 rows only — 大化 645, 白雉 650, and every 中国元号/朝鮮元号 boundary row are outside it (measured ×0). Those spans are verifiable only against the committed w1 full-page captures (`S894-digital.archives.go.jp-live-2026-10-27.html`, `S894-digital.archives.go.jp-capture-20260422145052.html`). I verified all of them there (see ledger); nothing is ungrounded, but the recheck sentence "each span below occurred exactly once in its window on 2026-10-27" (`:7`) is loose about which committed artifact carries which span. A future re-opener limited to the three evidence files could not re-locate the §3 tail spans.

## Verified-true ledger (checked, holds)

1. **All nine S896 quoted spans occur exactly once** in the whole-document window (S896.txt:35, whitespace-folded): `国家标准委22日发布了《农历的编算和颁行》等334项国家标准`, `这次标准的制定首次将农历编算和颁行纳入国家标准化管理体系` (P1); `如2013年的端午和冬至都分别有不同的日期版本…` (P2); `任何有印刷资质的单位和个人都可以公开自行编制或复制农历日历` (P3); `规定了朔日为农历月的第一个农历日，包含冬至在内的农历月为农历十一月`, `必须按国际天文学规范中关于天体位置计算所规定的模型来计算，精度应达到1秒` (P4); `要求公开发行的日历产品必须包含公历和农历的日期对照以及二十四节气`, `标准规定的编排规则、计算模型和精度及表示方法`, `国标由国内唯一的历书编算机构，中国科学院紫金山天文台起草编制` (P5). 闰 occurs **0** times in the whole extract — `:30`'s "occurs zero times" and the decision-table/§6 "nothing stated" leap-month rows (`:87`, `:104`) hold. The 1秒 unit ambiguity is real (page prints 1秒 with no unit) — `:22`/`:106` honest.
2. **All S895 field values ×1** in S895.txt:35: 标准号：GB/T 33661-2017; 中文/英文标准名称; 标准状态 现行; 发布日期 2017-05-12; 实施日期 2017-09-01; CCS A46; ICS 07.040; 主管部门 中国科学院 and 归口部门 中国科学院 (中国科学院 ×2, matching `:36`'s "both layers"); 发布单位 中华人民共和国国家质量监督检验检疫总局、中国国家标准化管理委员会; 备注 present with no content (`:38` holds); 标准全文预览 browser notice ×1. The two-date tension (registry 2017-05-12 vs press 22日) is carried unreconciled exactly as the two windows print it (`:40-42`).
3. **Digest/size fidelity**: S894 live 311,308 B sha256 204b7188…, capture 307,700 B sha256 c015e1dc…; S895 capture 24,174 B sha256 f04feb…; S896 25,250 B sha256 670850ea… — all match `:3-5`, and all four carriers are committed (evidence files + w1 captures). The `:4` parenthetical "the live page answered HTTP 200 with the same fields on the same date" is supported by the committed live openstd fetch (24,144 B, all twelve field strings present).
4. **Era-table numbers exact in both carriers**: 和暦 **248** rows (令和 2019 first; …; 慶応 1865, 元治 1864; 白雉 650, 大化 645 last two), 中国元号 **94** (康徳 1934, 大同 1932, 民国 1912, 清宣統 1909 first; 金天輔 1117, 金収国 1115 last), 朝鮮元号 **8** (朝鮮乾隆 1736 → 朝鮮永楽 1403), strict descending order; 248+94+8 = 350 numeric row tokens measured, matching `:48-50`. 詔勅 = 0 and 勅令 = 0 in live **and** capture — `:52`'s refusal of the staged "詔勅・勅令・勅書 database" description is verified, and the staged draft is demonstrably wrong on this point.
5. **Tier use correct**: SOURCES.md:849-851 at the landing = S894 dataset/A (scope: the archive's own comparison instrument), S895 docs/A (identity/status/dates/classification/custodial only, not clause text), S896 docs/B (state-press report, not normative wording) — matching fleet `CORPUS.md:93-97` definitions (A = primary/authoritative for the scope; B = strong secondary). The amendment's `:12` labels ("one tier-B state-press report… one tier-A registry record… one tier-A archive page") match, and `:60` carries every rule sentence "as announced, never as enacted" — the right epistemic strength for a B row. Notably the landed entry **corrects** the staged draft, which claimed "one tier A for the state press's promulgation report" (`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`, read-only source copy).
6. **Topic fit and gap real**: ground re-derived — `git grep -l -E 'GB/T 33661' 98c486b… -- corpus/knowledge` exits 1 with no output; base `culture-material/calendar-festival-systems.md` §2 is titled "Lunisolar intercalation: four strategies and the politics of the leap" (line 36 at base), matching `:9` exactly; base §8 mentions eras only as unsourced prose examples (Minguo 1912, Reiwa 2019 inside a speech-act list) — no era *table*, so "no citable era table" holds precisely because of "citable". All five couples targets exist at the landing. README row added with a description matching `:10`'s topic sentence; counts culture-material 40→41 and total 252→253 appended per convention; lesson Paths order S896→S895→S894 (SOURCES.md:854) matches the amendment's §1→§2→§3 structure; census-end receipt exits 0 with only pre-existing W04/W01 warnings (none touching S894–S896).
7. **Dropped-passage honesty**: the staged file indeed carried a second, superseded passage citing S919 (Marrone PDF) and S921 (Persee 1966) on codes/levels; the landed `:14`/`:66` drops it and the justification verifies — the lane entry `corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` holds the material (Marrone ×1, S892 ×10, levels ×27, reformulation ×3 at the landing), and S919/S921 were not opened for this amendment (rows appended are exactly S894–S896; 817→820 per lesson `:90`).
8. **Provenance trio** (source:/verified-at:/recheck:) present and first, recheck `180d` is a legal cadence, anchors are locator-bearing, not bare homepages (fleet CORPUS.md:105-106, 163-166). Claim-C context (df0f030 draft, marked pre-data/not frozen) maps candidate a to this exact path and the S908/S935→S894, S932/S938→S895, S937→S896 renumbering — consistent with lesson `:66` and the landed citations.

## Residual risk and verification gaps

- F1's correction and M1–M4's wording fixes are **not** made here (falsification seat; frozen text). None of them undermines the claim-C legs already measured by the counter seats; F1 is an entry-prose defect, not an evidence defect.
- All verification is against committed bytes at pinned revisions; no independent re-fetch was performed (out of seat scope). If the live pages drift before the 180d recheck, the amendment's own recheck rule (`:7`) — not this review — governs.
- External context for F1 (ISO 07.040 title; CCS A46 = 天文学) comes from web sources (iso.org; std.samr.gov.cn detail pages), not from lane evidence; the lane's own windows print only the codes.
- The capture/live text extracts differ trivially (whitespace/selected-state); the 350 row tokens, boundary rows, and select attributes are identical, so no cross-carrier claim is affected.
