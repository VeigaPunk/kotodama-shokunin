# ScoutSidorovaWorldview — staged S882 (Sidorova & Shuvalova 2006) vs the worldbuilding base entry, round 74 w1

Seat: ScoutSidorovaWorldview (leaf; godspeed). Date 2026-10-25. Lane base f7104cbc. Nothing written outside this file and /tmp/ScoutSidorovaWorldview/.
Tooling: nothing installed; pdftotext/pdfinfo (poppler, /usr/bin) already present; curl; python3 (string checks only). Pacman untouched.

## 1. Fetch
- GET http://www.philol.msu.ru/~sidorova/files/conlangs.pdf, UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` -> HTTP 200, 1055723 bytes, saved /tmp/ScoutSidorovaWorldview/conlangs.pdf.
- sha256 e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9 — identical to `reports/round-73/evidence/S877.txt` line 7 and to the lane row's 1055723 B. `pdfinfo`: 185 pages, QuarkXPress 4.11, created 2007-07-15.
- Extracted with `pdftotext -layout` (/tmp/ScoutSidorovaWorldview/c.txt) and per page with `pdftotext -f N -l N`. PDF page N = printed page N (printed number and page-header "Page N" agree; the row's "printed p. 10" matches). Quotes below were each confirmed as a substring of the single named page after joining end-of-line hyphenation and collapsing whitespace (python check, all True).

## 2. What the staged base entry actually cites S882 for
The staged base file (`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/worldbuilding-setting-practice.md`, 26 lines) is a header plus a *Proposed body* outline, not prose. Every S882 occurrence:
| # | staged location | wording | verdict |
|---|---|---|---|
| 1 | line 4 `source:` | `S882 — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf — аннотация — fetched 2026-10-23` | URL carried (byte-equal to S877's URL). Locator «аннотация» is carried only loosely: the annotation is the unheaded publisher blurb on the imprint page (PDF p.2), not a section named «аннотация»; the staged row's "series announcement booklet" description is obsolete — the URL now serves the full 185-page text (S877). Re-locate as «imprint page (PDF p.2), unheaded annotation». The date 2026-10-23 is the campaign fetch; lane date is 2026-10-25. |
| 2 | line 8 `recheck:` | `S882 -> 2` | Staged-namespace id. Must be repointed/dropped (REPOINTED leg); S877 recheck is `180d` already. |
| 3 | line 9 `ground:` | "pairs it with a tier-B scholarly row" | **carried** — S877 is tier B (monograph, not peer-reviewed, per row). |
| 4 | line 11 `topic:` | "against the scholarly framing of what constructing a world means" | **paraphrase-beyond-source** — the book frames constructing *languages* (and, as a motive, *worlds*) among conlang hobbyists; it has no framing of "what constructing a world means" as a setting-specification method. Only the annotation's question «Что побуждает … к языковому конструированию и созданию вымышленных миров?» touches it, and as a question, not a framing. |
| 5 | line 13 `sources:` | "S882, a tier-B row, states the scholarly framing that the practitioner guides elaborate" | **paraphrase-beyond-source** — the tier is right; "states the scholarly framing that [S883/S884] elaborate" is not: S877's scope (cell 4) is classification of artificial languages, not setting-note practice. Safe rewrite: S877 *describes* world-building courses/guides as the context of conlang making (p.35) and *models* the SF author's premise-to-world step (p.36). |
| 6 | line 20 body §2 heading | «§2 Worldview as rule-set — from S882» | heading **not carried** — the book never uses "worldview"/"rule-set" for a setting's rule system. Whole-PDF keyword scan of «мировоззрен-» (per page, 8 pages): p.5 «мировоззренческих … проблем» (an outlook problem, in B2), p.12 (Jakobson, language shapes мировоззрение), pp.44–45 (language-and-outlook citation), p.137 (creators' мировоззрение shown in their languages), p.141 (мировоззрения inherited by a project), pp.156–157 (religion of a fictional people, appendix). None is a world's rule system. "Rule-set" comes from the Chinese S729/S895 side, not S882 `[INFERENCE]`. |
| 7 | line 20 body §2 sub-claim a | "linguistic construction as modelling of other realities" | **carried** — annotation p.2 + Предисловие p.4–5 (quotes A1, B2, B3 below). Caveat: A1 is a question listing the options (игра / опыт моделирования иных реальностей / решение проблем общения) — it records the authors' framing alternatives, not an asserted finding; p.36 and p.139 assert it. |
| 8 | line 20 body §2 sub-claim b | "what a constructed world is assumed to be" | **partly carried / vague** — p.20 (a вымышленный язык must convey a картина мира принципиально отличная, else the world is uninteresting), p.36 (author posits a допущение and builds the world-picture it implies = модель реальности), p.139–140 (worlds are not static, have history; their language history must be логично связана with world history). None says the world is "assumed" to be a rule-set. Rewrite the sub-claim to one of these three, each with its page. |
Staged entry citations of S882 beyond the above: none (the 2026-10-23 amendment cites S899/S900/S895 only, no S882).

## 3. Carried / not carried / paraphrase-beyond — summary
- CARRIED: tier-B pairing (#3); conlang construction as modelling of other realities (#7, annotation p.2, Предисловие p.4–5, p.36, p.42); world-building as context of conlang-making (p.7, p.35, p.139).
- PARAPHRASE-BEYOND-SOURCE: «scholarly framing of what constructing a world means» (#4); «states the framing the practitioner guides elaborate» (#5); «what a constructed world is assumed to be» (#8) unless pinned to p.20/p.36/p.139–140.
- NOT CARRIED: the heading «Worldview as rule-set» (#6) — no wording in the book; a premise->consequences chain is present only for science fiction (p.36), and it is the author's description of SF, not of setting notes; any claim that S882 supports "rule-set" is the staged entry's inference `[INFERENCE]`.
- Also not carried by S877: anything on settings notes, build order, single-source discipline, the four layers or five elements (those are S883/S884 only).

## 4. Proposed located quotes (verbatim, <=25 words; PDF page = printed page; wc -w / characters of the Cyrillic string)
| id | location | quote | w | ch | supports |
|---|---|---|---|---|---|
| A1 | p.2 imprint annotation | «игрой, опытом моделирования иных реальностей, попыткой решения внешних по отношению к компьютерной действительности проблем общения» | 15 | 131 | #7 modelling of other realities (question form) |
| A2 | p.2 | «Что побуждает наших современников к языковому конструированию и созданию вымышленных миров?» | 11 | 91 | #4 world-creation as motive |
| B2 | p.5 Предисловие | «служит инструментом познания мира, решения важных мировоззренческих, культурологических и психологических проблем» | 11 | 113 | #7 (the `-layout` extract breaks `культурологи-/ческих`; plain extract does not) |
| B3 | p.4 Предисловие | «ограниченный план, родившийся в голове одного человека» | 7 | 54 | the invented language/world as one author's bounded model |
| C1 | p.7 (before Глава 1, which starts p.8 per Оглавление) | «Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и социальных реалий» | 15 | 108 | world-building context |
| D1 | p.20 Гл.1 | «призваны передавать картину мира, принципиально отличную от привычной нам, иначе вымышленный мир будет неинтересен» | 14 | 114 | #8 |
| E1 | p.35 Гл.2 opening | «если вы хотите построить свой собственный мир, вы можете, например, записаться на дистанционные курсы World Builders» | 16 | 116 | practitioner guides exist (replaces claim #5) |
| E2 | p.36 Гл.2 | «автор предлагает читателю некое научное или не совсем научное допущение и далее строит вокруг него ту картину мира» | 18 | 114 | premise -> world chain, SF only (#8, nearest to "rule-set") |
| E3 | p.36 | «писатель строит несколько иную модель реальности, научной, технологической, культурной, социальной» | 10 | 98 | #7 |
| F1 | p.140 | «должны быть логично связаны с историей мира» | 7 | 43 | #8 consistency of world history |
| F2 | p.139 | «Без контактов между вымышленными народами, а главное – без общего языка, ничего не выйдет.» | 14 | 90 | world needs a common language (optional) |
Оглавление (p.3) supports only the book's own coverage: Гл.2 «Вымышленные языки в мире – фантастическом, реальном и виртуальном» (p.35); «Общегуманитарные проблемы, связанные с конструированием языков» (p.40); «Языковое конструирование как форма игровой деятельности и проявление языкового творчества» (p.44). It names no worldview/setting-specification topic.
Locator note: A1/A2 sit on the imprint page (PDF p.2) and carry no «аннотация» heading, so cite as "p.2, unheaded publisher annotation". C1's heading was not read; cite only as "p.7".
Hyphenation: every quote above was also checked as a verbatim substring of the plain `pdftotext -f N -l N` output of its page after only collapsing whitespace (no de-hyphenation) — all 11 True — so the gate comparison needs no hyphen-joining; the `-layout` extract does break B2 as `культурологи-/ческих`, so extract without `-layout`.

## 5. S877 row — verbatim at lane worktree and at base (md5 of line 832 identical in both: 0186be0415bb375c4a0affeb29292ab2)
```
| S877 | М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 2006, 184 с., ISBN 5-98789-005-5 — complete typeset text of the monograph, author-hosted at МГУ — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf ; https://web.archive.org/web/20260208005339id_/https://www.philol.msu.ru/~sidorova/files/conlangs.pdf . | book | B | Tier B for the book's own framing: the classification of artificial languages (конланги), the vocabulary separating вымышленные языки from вспомогательные языки and from natural languages, the special status of Tolkien's languages, Klingon and D'ni, and the survey of the literature on imaginary languages. The full 185-page typeset text was opened (not an announcement booklet), but it is a monograph, not a peer-reviewed article, and its taxonomy is one classification among several it surveys | Глава 1 «Классификация искусственных языков (конлангов)», printed p. 10: «Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.» — PDF as served 2026-10-25 (HTTP 200, 1055723 bytes) and capture 20260208005339 (same bytes), both carrying the span | Supplies the Russian-language scholarly frame for constructed languages: a class system that separates fictional languages from auxiliary ones, a volume rule for how much language a world needs, and a dated literature survey | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.md |
```
Cells (split on `|`): id S877; kind book; tier B; status `mined`; opened `2026-10-25`; recheck `180d`; used-by (cell 10) = `corpus/knowledge/linguistics/conlang-scholarship.md` (one path, 51 chars).

## 6. May S877's used-by gain the base entry path in place?
Yes, with conditions.
- Rule: SOURCES.md preamble (lines 7–9): "Append-only: only `status`, `recheck` and `used-by` change in place, each change logged old→new in a round lesson". Adding a path to `used-by` is exactly the permitted in-place change; row id, source URL, tier, scope, anchor, teaches, opened stay untouched.
- Proposed new cell, old -> new, to be logged in `corpus/lessons/round-74.md` (one line, old and new strings verbatim):
  old: `corpus/knowledge/linguistics/conlang-scholarship.md`
  new: `corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md` (the exact separator convention used by other multi-path used-by cells in the registry must be copied — e.g. a row with two paths — before the edit; I did not enumerate it).
  Should the amendment (`worldbuilding-setting-practice.amend-2026-10-23.md`) be admitted as its own entry, it adds no S877 citation (it cites S899/S900/S895 only), so it is NOT added to S877.
- Condition 1 (REPOINTED/USED-BY legs): the added path is valid only if the admitted base entry really carries a `source: S877` line (repointed from `S882`), with the URL verbatim and a located page; the claims.json ROWS leg demands "used-by exactly the admitted entries whose source: lines cite it", so the edit must be dropped if the repoint is dropped.
- Condition 2 (scope): S877's `scope` cell says the row is tier B for the classification/vocabulary of artificial languages. Using it for the worldbuilding entry is outside that scope for any claim except "conlang making is modelling / world-building context" (#7, #8-pinned). The in-place used-by edit does not widen the scope cell (it may not change); the entry's wording must stay inside the scope, so rewrite claims #4, #5, #6 first (§2) — otherwise the used-by edit records a citation the source does not carry (the R73-M8 attribution failure class: lesson round-73.md line 115).
- Condition 3: the row's `anchor` cell (printed p. 10 quote) is for the classification claim; a new claim here needs its own located quote in the round-74 `## Gate` (use §4), not a reuse of the S877 anchor.
- Rule 2 does not require a re-fetch: byte-identical (sha256 above); the round-74 Gate/evidence entry for the *claim* should still record this fetch (UA, 200, 1055723 B, sha256).

## 7. Gaps / unrun
- Wayback capture was not re-probed (not asked; row already carries id_ capture 20260208005339, which the round-73 lesson reports as same bytes).
- I did not run the claims.json counter or any census; I did not read the full text of the book — only the TOC, annotation, Предисловие, the passages listed and keyword greps («мир», «моделирован», «мировоззрен», «правил»).
