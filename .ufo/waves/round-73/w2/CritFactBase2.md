# CritFactBase2 — wave 2 FALSIFY: `conlang-scholarship.md` §5–§9 against S877

Lane revision attacked: `0316b8883b4f8d44b8efd720140e7f52f734a102` (read-only; lane tree not mutated, no clone needed — every experiment here is a read of a `/tmp` download). Downloads: `/tmp/CritFactBase2/` (`S877.pdf`, `S877_curlua.pdf`, `plain.txt`, `layout.txt`, `L.txt`, `P.txt`). Tools installed: none (`pdftotext` 26.08.0 / poppler was already present). No pacman.

## VERDICT: no fabrication in §5–§9 — 0 BLOCKER, 2 MAJOR, 3 MINOR

Every sentence with an `(S877)` cite in §5–§8 (15 cites) and every table row (3 rows, ~20 named facts) is **supported by the opened book at the printed page shown below**. All nine quoted spans (six double-quoted, three guillemet) are **verbatim** in the source, including the English `«impoverishments of the natural languages»`, which I expected to be a translated pseudo-quote and is not. All named persons (Tolkien, Okrand, Watson, Yaguello, Schnapp, Higley, Henning, Jakobson) and all numbers (почти двух десятков, 1 500, 773, 20 000, 1992, 1985/1991, 28 July 2005, 1999) check out at the page named.

The defects that do exist are in the entry's **verification apparatus**, not its content: the header names an extraction method that contradicts the evidence receipt and cannot re-find 7 of the 28 anchors, and 15 of 15 §5–§8 cites carry no page locator, so the header's own recheck instruction cannot be executed for this body. Neither defect makes a frozen claim leg false (the legs require a Gate locator for the row's anchor quote, which S877 has at p. 10), so I do not raise a BLOCKER.

## Fetch record (this seat, live, 2026-10-25)

| request | UA | status | bytes | sha256 |
|---|---|---|---|---|
| GET `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | 200 | 1 055 723 | `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` |
| same | `curl/8.7.1` | 200 | 1 055 723 | `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` |

`cmp S877.pdf S877_curlua.pdf` → `identical-bytes`. No UA gate either way; bytes equal the evidence capture's sha256. `pdfinfo`: 185 pages, `Title: verstka`. PDF page index = printed folio for the body (checked for pp. 5, 6, 8, 11, 16, 17, 19–29), so the pages below are printed pages.

## Per-sentence table (§5–§9)

| line | claim | source span (verbatim, ≤25 w) | printed p. | verdict |
|---|---|---|---|---|
| 69 | three-axis contrast auxlang/fictional | "стремиться к охвату как можно большего числа пользователей" / "отражать в своей семантике окружающую нас действительность, а также образ мыслей людей Земли" / "требование равной структурной простоты"; "не претендуют на широкий круг пользователей" / "призваны передавать картину мира, принципиально отличную от привычной нам" / "не связаны требованиями структурной простоты" | 16–17 (aux side), 19–20 (fictional side) | SUPPORTED |
| 70 | modality quote | "Эти языки и их создатели не «должны», а «могут»." | 19 | SUPPORTED (verbatim) |
| 71 | memorandum/manifesto unacceptable; how-to offers options | "В сообществе создателей ВЯ неприемлем такой жанр, как меморандум или манифест"; "не поставить лингвоконструкторов в жесткие рамки, а предложить им набор возможностей" | 19–20 | SUPPORTED |
| 72 | poetic function (Jakobson) is the leading principle | "ведущим началом при конструировании вымышленных языков является поэтическая функция языка, по Р.О. Якобсону" | 21 | SUPPORTED |
| 76 | "первичность описания языка" | "первичность описания языка по отношению к языку как таковому. Пока автор ВЯ не напишет в грамматике…" | 6 | SUPPORTED |
| 77 | project vs grammatical description | "описывают то, что уже существует, проектирование подразумевает создание объекта" | 6 | SUPPORTED (verbatim) |
| 78 | discontinuous, deliberate change | "прерывистый, «скачкообразный» процесс, заключающийся в сознательном внесении изменений автором или пользователями языка (с санкции автора)"; "снятие фонотактических ограничений или добавление морфонологического процесса"; "чтобы разнообразить его, украсить" | 22 | SUPPORTED |
| 79 | history written backwards/forwards; resources rewritten | "может идти от первоначальной системы как в прошлое … так и в будущее"; "восстанавливая древние стадии развития языка, якобы предшествовавшие первоначально придуманной системе"; "эти «наличные ресурсы» можно в любой момент изменить, отредактировать" | 22 | SUPPORTED |
| 80 | design consequence | — (entry's inference, no cite) | — | n/a |
| 86 | Tolkien row | "Считается, что Толкин был творцом почти двух десятков языков своего фантастического мира — Арды"; "имеется обширный корпус поэтических произведений … молитва «Отче наш»"; "От других языков Арды нам известны горсточки … имен и зачатки грамматики" | 23 | SUPPORTED (hedge dropped — F5) |
| 87 | Klingon row | "создан доктором лингвистики Марком Окрандом на основе исчезнувших языков американских индейцев … с установкой на максимальное отличие от языков Земли"; "структурой предложения OVS"; "В клингоне нет категории времени, нет рода, нет прилагательных; в нем оригинальная система письма"; "С 1992 года в США существует Институт клингонского языка"; "ISSN 1061-2327"; "По клингону защищен ряд диссертаций"; "созданы словари, учебники, пособия" | 24–25 | SUPPORTED (no inline cite — F3) |
| 88 | D'ni row | "создан для серии компьютерных игр «Myst» сотрудником компьютерной фирмы Cyan Worlds Ричардом А. Ватсоном"; "принимают допущение, что язык уже существует в готовом виде, однако открывается им по частям"; "Под руководством самого создателя языка Ватсона … разгадывая лингвистические загадки" | 26 | SUPPORTED (no inline cite — F3) |
| 90 | why D'ni stands apart | "Особое место D'ni обусловлено не исключительной популярностью «Мист» … а тем статусом, который авторы серии придали языковому компоненту" | 26–27 | SUPPORTED |
| 91 | Tolkien as "father" though conlangs predate him | "известны и до Дж. Р. Толкина, «отцом» движения энтузиастов-языкотворцев все-таки следует считать его" | 22–23 | SUPPORTED |
| 92 | Klingon grammar not re-checked | entry's own `(to-verify)` hedge | — | honest, n/a |
| 96 | "исчисляются единицами"; large auxlang literature | "работы, серьезно трактующие проблему вымышленных языков, исчисляются единицами"; "Лингвистическая литература, посвященная вспомогательным языкам, весьма обширна" | 27; 11 | SUPPORTED |
| 97 | Yaguello 1985 / Eng. 1991, pathology, dilettantes | "В 1985 г. … М. Ягелло (M. Yaguello) выпустила книгу под названием «Лингвистические лунатики» (английский перевод — «Lunatic Lovers of Language…», 1991)"; "называя их «дилетантами…»"; "настаивает на патологическом характере лингвоконструирования" | 27–28 | SUPPORTED |
| 98 | Schnapp: "philologists of imagined worlds" + "impoverishments" | "он называет конлангеров «филологами воображаемых миров»"; "для него ВЯ – это «impoverishments of the natural languages»" | 28 | SUPPORTED (verbatim, incl. the English phrase) |
| 99 | Higley: models/artefacts, sailboat, translation possible | "конланги – это действительно модели, артефакты … Никто не плавает на модели парусника. Никто не думает и не говорит на конланге, хотя с конланга и на конланг можно переводить" | 29 | SUPPORTED |
| 100 | 1 500 / 773 / 20 000 counters | "около 1 500 конлангов"; "773 … по состоянию на 28 июля 2005 года"; "в США подобное объединение в 1999 году насчитывало около 20 000 членов" | 5; 8; 5 | SUPPORTED (dated-premise defect — F4) |
| 103–105 | §9 coupling | — (no S877 cite) | — | n/a |

Quote-fidelity census — all quoted spans in §5–§9, checked character-for-character against `pdftotext -enc UTF-8` output with whitespace collapsed: `FOUND` × 9, `ABSENT` × 0 (`Эти языки … «могут».`, `первичность описания языка`, `описывают то, что уже существует, проектирование подразумевает создание объекта`, `исчисляются единицами`, `impoverishments of the natural languages`, `конланги – это действительно модели, артефакты`, `должны`, `могут`, `филологами воображаемых миров`).

## Findings

### F1 — MAJOR. The header's extraction method contradicts the evidence receipt and cannot re-find 7 of 28 §5–§8 anchors.

`conlang-scholarship.md:4` declares the text was "read with `pdftotext -layout`"; `reports/round-73/evidence/S877.txt` records `extract: pdftotext -enc UTF-8 S877.pdf -`. Both are landed bytes at `<lands>`, so one of them is false. It matters because `conlang-scholarship.md:6` instructs the 180-day recheck to "re-run `pdftotext -layout` and re-find the quote": under `-layout`, 7 anchors in §5–§8 are unreachable, because `-layout` keeps the book's end-of-line hyphenation (`как та-\nковому`, `«скачкообраз-\nный»`, `По клин-\nгону`, `язык уже суще-\nствует`, `весьма обшир-\nна`, `университе-\nта`) and, once, interleaves the running folio inside the phrase (`…«отцом»` / `22` / `движения энтузиастов…`). Every one of the 28 anchors is findable in the receipt's mode.

```
$ cd /tmp/CritFactBase2 && pdftotext -layout -enc UTF-8 S877.pdf layout.txt \
  && pdftotext -enc UTF-8 S877.pdf plain.txt && python3 - <<'PY'
import re
def norm(s):
    s=re.sub(r'verstka\s*\n\s*\d+/\d+/\d+\s*\n\s*[\d:]+\s*[AP]M\s*\n\s*Page \d+','',s)
    return re.sub(r'\s+',' ',s)
L=norm(open('layout.txt',encoding='utf-8').read()); P=norm(open('plain.txt',encoding='utf-8').read())
A=[('S5 axes','Вымышленные языки, в отличие от вспомогательных'),
   ('S5 modality','Эти языки и их создатели не «должны», а «могут».'),
   ('S5 manifesto','неприемлем такой жанр, как меморандум или манифест'),
   ('S5 poetic','поэтическая функция языка, по Р.О. Якобсону'),
   ('S6 первичность','первичность описания языка по отношению к языку как таковому'),
   ('S6 project','описывают то, что уже существует, проектирование подразумевает создание объекта'),
   ('S6 change','прерывистый, «скачкообразный» процесс'),
   ('S6 backwards','может идти от первоначальной системы как в прошлое'),
   ('S7 2dozen','творцом почти двух десятков языков'),
   ('S7 prayer','молитва «Отче наш»'),
   ('S7 klingon','структурой предложения OVS'),
   ('S7 KLI','С 1992 года в США существует Институт клингонского языка'),
   ('S7 ISSN','ISSN 1061-2327'),
   ('S7 diss','По клингону защищен ряд диссертаций'),
   ('S7 Watson','Ричардом А. Ватсоном'),
   ('S7 dni-assume','язык уже существует в готовом виде'),
   ('S7 dni-why','Особое место D’ni обусловлено не исключительной популярностью'),
   ('S7 father','«отцом» движения энтузиастов-языкотворцев все-таки следует считать его'),
   ('S8 units','исчисляются единицами'),
   ('S8 large-lit','Лингвистическая литература, посвященная вспомогательным языкам, весьма обширна'),
   ('S8 yaguello','В 1985 г. профессор английского отделения Парижского университета'),
   ('S8 schnapp','филологами воображаемых'),
   ('S8 impoverish','impoverishments of the natural languages'),
   ('S8 higley','конланги – это действительно модели, артефакты'),
   ('S8 sailboat','Никто не плавает на модели парусника'),
   ('S8 1500','около 1 500 конлангов'),
   ('S8 773','773 представленных в мировой сети языка'),
   ('S8 20000','насчитывало около 20 000 членов')]
print(f"{'anchor':16} {'-layout':8} {'plain':6}")
fails=[]
for k,q in A:
    a,b=q in L,q in P
    print(f'{k:16} {str(a):8} {str(b):6}')
    if not a: fails.append(k)
print('layout-unfindable:',len(fails),fails)
PY
anchor           -layout  plain
S5 axes          True     True
S5 modality      True     True
S5 manifesto     True     True
S5 poetic        True     True
S6 первичность   False    True
S6 project       True     True
S6 change        False    True
S6 backwards     True     True
S7 2dozen        True     True
S7 prayer        True     True
S7 klingon       True     True
S7 KLI           True     True
S7 ISSN          True     True
S7 diss          False    True
S7 Watson        True     True
S7 dni-assume    False    True
S7 dni-why       True     True
S7 father        False    True
S8 units         True     True
S8 large-lit     False    True
S8 yaguello      False    True
S8 schnapp       True     True
S8 impoverish    True     True
S8 higley        True     True
S8 sailboat      True     True
S8 1500          True     True
S8 773           True     True
S8 20000         True     True
layout-unfindable: 7 ['S6 первичность', 'S6 change', 'S7 diss', 'S7 dni-assume', 'S7 father', 'S8 large-lit', 'S8 yaguello']
```

Mechanism, from the raw `-layout` text (`grep -n 'скачкообр\|обширн\|весьма' layout.txt`):

```
1082:          ющийся в коммуникации между людьми, а как прерывистый, «скачкообраз-
 475:          ская литература, посвященная вспомогательным языкам, весьма обшир-
```

**Smallest safe correction:** change `conlang-scholarship.md:4` to name the mode the receipt actually used — "text read with `pdftotext -enc UTF-8`" — and in `:6` replace "re-run `pdftotext -layout` and re-find the quote on the printed page number given" with the mode plus a de-hyphenation step (or drop the mode from the recheck line and keep only "re-find the quoted span with whitespace collapsed and end-of-line hyphens joined"). Do not restate the claim: the quotes are all correct; only the recipe is wrong.

### F2 — MAJOR. 15 of 15 §5–§8 cites carry no page locator, so the header's own recheck clause is unexecutable for this body.

`:6` says the recheck is to "re-locate each quoted span at the page or section its sentence names". §5–§8 name no page and no section: the only page locators in the whole entry are the header's scope line and §3's table header.

```
$ cd kotodama-shokunin && grep -n 'p\{1,2\}\. [0-9]' corpus/knowledge/linguistics/conlang-scholarship.md
4:- source: S877 — … preface pp. 4–7, ch. 1 pp. 8–34 — … text read with `pdftotext -layout`
40:| Class, in the book's numbering (pp. 11–12) | What the book means | Design question it forces |
$ awk 'NR>=67 && NR<=101' corpus/knowledge/linguistics/conlang-scholarship.md | grep -c '(S877)'
15
$ awk 'NR>=67 && NR<=101' corpus/knowledge/linguistics/conlang-scholarship.md | grep -n 'p\.'
$ echo exit=$?
exit=1
```

So a rechecker has 15 cites, 6 quoted spans and no page for any of them; the printed pages exist and are cheap to state (19, 19–20, 21, 6, 6, 22, 22, 23, 24–25, 26, 26–27, 22–23, 27, 27–28, 28, 29, 5/8/5 — see the table above).

**Smallest safe correction:** append the printed page to each `(S877)` in §5–§8, e.g. `(S877 p. 19)`. Nothing else changes; the claims are already true at those pages.

### F3 — MINOR. The §7 table's three rows carry no inline `(S877)`, and they hold the entry's densest cluster of named-person/number facts.

Lines 86–88 assert ~20 checkable facts (Tolkien, Okrand, Watson; "nearly two dozen"; 1992; OVS; no tense/gender/adjectives; script; ISSN; dictionaries; dissertations; corpus; Lord's Prayer; "handfuls of names"; the D'ni assumption and decipherment) and carry no source id; every other §5–§8 sentence carries one. All of them are true at pp. 23–26 (table above), so this is a provenance hole, not a truth defect — but it is the block where a fabrication would have been cheapest to hide and hardest to catch.

```
$ sed -n '84,88p' corpus/knowledge/linguistics/conlang-scholarship.md | grep -c '(S877)'
0
$ echo exit=$?
exit=1
```

**Smallest safe correction:** add `(S877 pp. 23–26)` to the section lead-in line above the table, or a page column.

### F4 — MINOR. "The book's counters are dated" is true of two of the three counters.

Line 100 opens "The book's counters are dated and are not reused as current figures here". The 773 counter is dated (28 July 2005, p. 8) and the 20 000 counter is dated (1999, p. 5), but the 1 500 langmaker counter carries no date anywhere in the book: p. 5 reads "Список конструированных языков (конлангов) … langmaker.com – включает около 1 500 конлангов (см. Приложение 1)", and Приложение 1 (p. 142) is a bare alphabetical list with no as-of date.

```
$ grep -n 'около 1 500 конлангов' /tmp/CritFactBase2/plain.txt
171:подобное объединение в 1999 году насчитывало около 20 000 членов). Список конструированных языков (конлангов) на одном из самых авторитетных источников – langmaker.com – включает около 1 500 конлангов (см.
$ sed -n '5992,5997p' /tmp/CritFactBase2/plain.txt
Приложение 1
Списки конлангов
1А. Список конлангов на сайте langmaker.com
A

B
```

The undated figure is the one a later reader is most likely to reuse as current — exactly what the sentence exists to prevent.

**Smallest safe correction:** "Two of the book's counters are dated" or "the book's counters are dated or undated as follows: 1 500 (undated) …".

### F5 — MINOR. The two-dozen count drops the book's own hedge.

Line 86 states "nearly two dozen languages" flatly; p. 23 hedges it: "**Считается, что** Толкин был творцом почти двух десятков языков своего фантастического мира — Арды." The book does not assert the count, it reports a received view; the book's own enumeration on the same page runs to ~17 entries. For a named number this is the difference between "the book records" and "the book vouches".

```
$ python3 -c "p=open('/tmp/CritFactBase2/plain.txt',encoding='utf-8').read().split(chr(12))[22];i=p.find('двух десятков');print(repr(p[i-90:i+40]))"
'иастов-языкотворцев все-таки следует считать его. Считается, что Толкин был творцом почти двух десятков языков своего фантастическ'
```

**Smallest safe correction:** "Tolkien, by the book's report 'almost two dozen' languages for his legendarium".

## Checked and clean (no finding)

- §5's three axes are the book's own three-item lists on both sides (pp. 16–17 auxlangs а/б/в; pp. 19–20 fictional а/б/в) — not a synthesis that invents a frame.
- §6's description-first property is correctly **scoped to personal/authorial languages**, which is exactly the book's scope: p. 6 contrasts them with "языки Толкина, фантастические языки кино и компьютерных игр". The following paragraph's "such a language" narrows a general ВЯ claim (p. 22, "Развитие первых") to a subset — a safe narrowing, since p. 6 concedes Esperanto and Tolkien's languages can change in use.
- §8's whole section is honestly framed as the monograph's report ("as the 2006 monograph reports it"), so the second-hand chain (book → Schnapp / Higley / Yaguello) is not a false provenance.
- The `(to-verify)` hedge on line 92 is accurate: the book gives the Klingon grammar at p. 24 but the entry never claims to have checked Okrand's own grammar.
- All six `couples:` targets and the §9 handoff path exist at `<lands>` (`corpus/knowledge/linguistics/{conlang-methodology,naming-systems,phonetics-phonology,historical-linguistics,writing-systems}.md`, `corpus/knowledge/synthesis/worldbible-integration-contract.md`).
- The amendment file does not restate S877, so there is no cross-document contradiction to test (`grep -n 'source:' …amend-2026-10-23.md` → S878, S879, S880 only).

## What I could NOT check

- **The book's own claims against the world.** §8 is scoped to the monograph's report and so is my check. I did not verify that Yaguello's French original is 1984 (the book says 1985), that HolQeD's ISSN 1061-2327 is registered, that the KLI was founded in 1992, or that langmaker's list ever held ~1,500 entries — all of these are reports the entry correctly attributes to S877, and checking them would be a different claim.
- **Which extraction mode the drafter actually used.** Unknowable from landed bytes: the entry says `-layout`, the receipt says `-enc UTF-8`. I proved the consequence (7 anchors unreproducible under the declared mode), not the history.
- **The other entry's §1–§4 body** (lines 15–66), including §3's "pp. 11–12" class-numbering cite — outside this seat's item.
- **The counter, ledger, receipts and the §7/§8 rows' tier language** — other seats' items; I read `claims.json` only to establish that no frozen leg depends on per-sentence locators.
