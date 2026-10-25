# CritFactBase1 — §1–§4 of `conlang-scholarship.md` against its two sources (wave 2, FALSIFY)

- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Attacked bytes: `corpus/knowledge/linguistics/conlang-scholarship.md` at **0316b8883b4f8d44b8efd720140e7f52f734a102** (`git show 0316b88:… | sha256sum` = `5584ecc094d530c3f8ecdefc48a87a6510cfae1936cd4478c08b7ffa434af202` = worktree file, verified).
- Scope of this seat: **§1–§4 only** (lines 15–65), plus the provenance header (lines 3–13) because every §1–§4 sentence is scoped by it.
- Method: both sources fetched live and read in full at the level §1–§4 use; every cited span located in the extracted text with its **printed page** (this PDF's printed page number equals its PDF page index — verified: page 11 footer reads `11`, page 12 footer `12`); every quoted string compared character-for-character; every number re-derived.
- **VERDICT: §1–§4 HOLD.** No BLOCKER, no MAJOR. Five MINOR defects, all in wording/locator/provenance, none touching a claim leg (C's ENTRIES/ROWS/GATE/EVIDENCE legs are untouched by anything below). The strongest attack I could build — that the book says something other than the entry's taxonomy, volume rule, or terminology claim — **fails**: the source matches the entry almost word for word.

## Fetches (every request: UA, status, bytes, sha256)

`UA-B` = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; `UA-C` = `curl/8.7.1`. Local curl is 8.23.0; `-A curl/8.7.1` sends that UA.

| URL | UA | status | bytes | sha256 |
|---|---|---|---|---|
| https://ojs.unito.it/index.php/ricognizioni/article/view/7099 | UA-B | 200 | 30289 | e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c |
| same | UA-C | 200 | 30289 | e7260b49…9369c (same) |
| http://www.philol.msu.ru/~sidorova/files/conlangs.pdf (`-L`) | UA-B | 200 | 1055723 | e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9 |
| https://ojs.unito.it/index.php/ricognizioni/about/editorialPolicies | UA-B | 404 | 22 | — (path guess) |
| https://ojs.unito.it/index.php/ricognizioni/about | UA-B | 200 | 26501 | — (peer-review check only) |

Both S876 and S877 sha256/bytes equal the committed captures `reports/round-73/evidence/S876.txt` and `S877.txt`. No UA gating in either direction on S876. Downloads in `/tmp/CritFactBase1/` only (`s876.html`, `s876-plain.html`, `s877.pdf`, `s877.txt` = `pdftotext -layout`, `s877-nolayout.txt` = plain, `about.html`, `about2.html`). Nothing written outside this report.

```
$ pdfinfo s877.pdf | grep -E 'Pages|File size|Title'
Title:           verstka
Pages:           185
File size:       1055723
```
The book's own imprint (p. 2) says `2006, с.184`, so "the whole 184-page book" is the book's own page count; the PDF carries one extra blank page numbered 185 (p. 185 = `185` only). Not a defect — recorded because a rechecker running `pdfinfo` will see 185.

## Per-sentence table (§1–§4)

`L` = line in `conlang-scholarship.md`. Page numbers are printed pages of S877; S876 spans are given by the served page's source line.

| L | claim | source span | verdict |
|---|---|---|---|
| 3 | S876 = abstract under "Abstract" heading, page-source line 267, plus `citation_keywords` | `s876.html:267` = `<p>In this article, I show from my own experience…`; keywords meta present | SUPPORTED (exact) |
| 3 | 30,289 bytes, HTTP 200, no wall | live fetch, both UAs, identical bytes/sha | SUPPORTED |
| 4 | S877 = whole book, 1,055,723 bytes, title page/аннотация/Оглавление/preface pp. 4–7/ch. 1 pp. 8–34 | p. 1 title, p. 2 imprint+annotation, p. 3 Оглавление (`Предисловие … 4`, `Глава 1 … 8`, `Глава 2 … 35`), p. 4–7 preface | SUPPORTED (ch. 1 = 8–34 confirmed by Глава 2 starting p. 35) |
| 4 | "text read with `pdftotext -layout`" | committed capture says `extract: pdftotext -enc UTF-8 S877.pdf -` | **MISMATCH — F4** |
| 6 | recheck: "re-run `pdftotext -layout` and re-find the quote" | in `-layout` the Gate quote is hyphen-split | **not mechanically reproducible — F4** |
| 7 | `conlang-methodology.md` cites Rosenfelder, Peterson, Okrent, Higley, WALS, PHOIBLE, APiCS | that file line 4 names all seven | SUPPORTED |
| 7 | "the 799-row registry carries no row naming a constructed-language research venue (`grep -c … = 0`)" | base: 799 rows / 0 hits; **lands: 804 rows / 2 hits** | **stale at lands — F1** |
| 8 | "one peer-reviewed article and one Russian-language monograph" | journal about page: "peer-reviewed journal"; book has ISBN 5-98789-005-5, М.: «1989.ру» | SUPPORTED (peer-review support is on a page not named in the entry; see adjacent) |
| 10 | both rows tier B as the register scopes them | SOURCES.md rows S876/S877 both `B` | SUPPORTED |
| 19 | Enguehard = single author's position, not field consensus; abstract carries no curriculum/cohort/count | `s876.html:267` (two "I show" sentences, no numbers) | SUPPORTED |
| 20 | book records that neither linguists nor conlangers agree on class names; adopts one of several classifications | p. 10: «ни у ученых-лингвистов, ни в среде конлангеров нет терминологического единства в том, что касается обозначения классов искусственных языков»; p. 11: «Для целей нашей работы мы принимаем следующую типологию» | SUPPORTED (exact) |
| 21 | Henning = conlanger-community organiser's scheme, reported not tested | p. 12 «Идеолог движения конлангеров в Интернете Дж. Хеннинг»; p. 28 «Создатель одного из основных Интернет-ресурсов … conlang.com»; no test of the rule anywhere | SUPPORTED |
| 22 | Yaguello = contested/hostile; book notes it selects the strangest cases | p. 27–28 «Ягелло настаивает на патологическом характере лингвоконструирования»; p. 28 «она специально выбирает наиболее странные фигуры» | SUPPORTED |
| 23 | Schnapp's "impoverishment" thesis; Higley argues against it in the same survey | p. 28 «(для него ВЯ – это «impoverishments of the natural languages»)»; p. 29 «Возражая Шнаппу …» | SUPPORTED (entry's singular "impoverishment" is a label; the book's term is plural) |
| 24 | Higley = contested, published, venue not named by the book (to-verify) | p. 29 names the article title only; **the bibliography pp. 176–181 has no `[Higley 2000]` entry at all** | SUPPORTED, (to-verify) is honest and if anything understated |
| 30 | quote "the construction of languages by students allows them to better grasp the reality of linguistic analysis" | `s876.html:267`, verbatim | SUPPORTED (16 words) |
| 31 | quote "the same ones that lead most linguists to marginalize constructed languages from research" | `s876.html:267`, verbatim | SUPPORTED |
| 32 | "The article's keywords name the frame it works in: Constructed languages, Linguistic Analysis, Linguistics Teaching, Method-Oriented Teaching" | served keywords are **ten** items: Constructed languages, Phonology, Diachronic linguistics, Natural Languages, Natlang, Linguistic Analysis, Constructed Languages, Conlangs, Linguistics Teaching, Method-Oriented Teaching | **PARTIAL — F2** (4 of 10, no ellipsis; drops Phonology and Diachronic linguistics) |
| 33 | abstract carries no curriculum/cohort/outcome; abstract is the whole opened artefact | `s876.html:267`; the PDF galley was not opened (declared) | SUPPORTED (honest scope) |
| 38 | book adopts one of several classifications and says neither linguists nor conlangers share class terminology | p. 10 + p. 11 (as L20) | SUPPORTED (exact) |
| 40 | table header "Class, in the book's numbering (pp. 11–12)" | `1.`, `2.1.`, `2.1.1.`, `2.1.2.`, `2.2.` all occur on **p. 11 only**; p. 12 contains no class number | **locator over-range — F5** |
| 42 | 1. Auxlangs = Esperanto, Ido, Lojban | p. 11 «эсперанто, идо, ложбан и др.» | SUPPORTED |
| 43 | 2.1 Artlangs = fiction, film, games | p. 11 «придуманные авторами литературных и кинематографических произведений, а также компьютерных игр» | SUPPORTED |
| 44 | 2.1.1 = left their fictional world: Tolkien, Klingon, D'ni | p. 11 «языки Толкина, клингон …, язык D'ni из мира компьютерной игры «Myst»» | SUPPORTED |
| 45 | 2.1.2 = function or are only mentioned inside the work | p. 11 ««функционирующие» или просто упоминающиеся только в пределах соответствующего художественного произведения» | SUPPORTED |
| 46 | 2.2 = personal/авторские, own pleasure, Internet as primary habitat | p. 11 «для собственного удовольствия» … «Основной средой бытования авторских языков является Интернет» | SUPPORTED |
| 47 | 2.2 germinal case = языки-наброски: never leave the germinal stage, not tied to a world, or partly revise natural languages | p. 11 «Проекты, не выходящие из зародышевой стадии и не связанные с созданием вымышленного мира, а также попытки частичной ревизии естественных языков принято именовать «языками-набросками»» | SUPPORTED (book reports customary usage; entry's "the book calls" is a small voice shift, not a misquote) |
| 49 | book's own subject is 2.2, not the artlangs beside it | p. 6 «основным предметом нашего исследования являются персональные, или авторские, вымышленные языки»; p. 11 «Такие фантастические языки рассматриваются нами попутно» | SUPPORTED |
| 50 | competing classifications: Rosenfelder (structure/purpose); a priori vs a posteriori "(Harrison, after Couturat and Leau)"; Capuzzo (potential use/users); HKU letter+SVO index | p. 12 Rosenfelder; p. 13–14 the a priori/a posteriori tradition (Couturat/Leau) is inside a **quoted Kuznetsov** passage about auxiliary languages, and Harrison is introduced separately as developing that opposition; p. 15 Capuzzo; p. 16 `web.hku.hk` composite index | **PARTIAL — F3** (Harrison↔Couturat/Leau link is the entry's synthesis) |
| 51 | boundaries shift; Klingon and Tolkien's Elvish left fiction; book asks whether Klingon counts as a living natural language | p. 11–12 «границы между классами ВЯ могут смещаться … как это произошло, например, с клингоном и с эльфийскими языками … не следует ли приравнять клингон … к живым естественным языкам» | SUPPORTED |
| 55 | Henning's volume rule: size/detail of lexicon and grammar follow from what the language is for | p. 12 «В зависимости от того, будет ли язык-модель использоваться как жаргон, как «язык имен собственных» (naming language), язык для общения или язык литературы, для него потребуется разный объем и степень детализации словаря и грамматики» | SUPPORTED (exact) |
| 60 | jargon = a few words + plural rules, «вкус другой культуры» | p. 12 «достаточно горсточки слов, передающих «вкус другой культуры», и правил образования множественного числа» | SUPPORTED |
| 61 | naming language = no special grammar | p. 12–13 «Для «языка имен собственных» … тоже не требуется особой грамматики» | SUPPORTED |
| 62 | real communication / literature = far more | p. 13 «нужно гораздо большее» | SUPPORTED |
| 64 | "Read that rule against `linguistics/naming-systems.md` (S877)" | coupling reference; the rule is S877's | SUPPORTED (no source claim) |

## Findings

### F1 — MINOR: the ground line's command does not reproduce at the landed revision, and the entry's own rows falsify its present tense

L7 reads "the 799-row registry carries no row naming a constructed-language research venue (`grep -c 'ojs.unito.it\|philol.msu.ru' corpus/SOURCES.md` = 0, run 2026-10-25)". The command has no revision qualifier, so a reader runs it at lands and gets the opposite of the printed value — because S876/S877 themselves put those hosts in the registry.

```
$ grep -c 'ojs.unito.it\|philol.msu.ru' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
2
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
804
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 8841ad3b896a0227674fa0725b818c999118046f:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
799
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 8841ad3b896a0227674fa0725b818c999118046f:corpus/SOURCES.md | grep -c 'ojs.unito.it\|philol.msu.ru'
0
```

Claim-C's GROUND leg is **not** falsified: it reads `reports/round-73/telemetry/gap-sweep.txt`, which pins `git show 8841ad3b…` in its own section [7]. The defect is confined to the entry's wording.
**Smallest safe correction:** `… and at base 8841ad3b… the 799-row registry carried no row naming a constructed-language research venue (git show 8841ad3b…:corpus/SOURCES.md | grep -c … = 0)`.

### F2 — MINOR: the keyword list is truncated from ten items to four with no ellipsis

L32 says "The article's keywords name the frame it works in: Constructed languages, Linguistic Analysis, Linguistics Teaching, Method-Oriented Teaching". The served metadata carries ten, including two that cut against the teaching-only frame:

```
$ grep -o 'Constructed languages,[^<]*' /tmp/CritFactBase1/s876.html | tr -s ' \t' ' '
Constructed languages, Phonology, Diachronic linguistics, Natural Languages, Natlang, Linguistic Analysis, Constructed Languages, Conlangs, Linguistics Teaching, Method-Oriented Teaching
$ grep -c '<meta name="citation_keywords"' /tmp/CritFactBase1/s876.html
10
```
Dropped: Phonology, Diachronic linguistics, Natural Languages, Natlang, Conlangs, and a duplicate "Constructed Languages". The four listed are genuine and in order, so the sentence is not false — it is selective in a way that overstates a teaching/method frame for a phonology-and-diachrony article.
**Smallest safe correction:** `The article's keywords include Constructed languages, Linguistic Analysis, Linguistics Teaching, Method-Oriented Teaching (among ten, with Phonology and Diachronic linguistics leading) (S876).`

### F3 — MINOR: "(Harrison, after Couturat and Leau)" is the entry's synthesis, not the book's report

L50 attributes the a priori/a posteriori split to "Harrison, after Couturat and Leau". In the book the Couturat/Leau genealogy occurs **inside a block quotation from S. N. Kuznetsov about international auxiliary languages**, and Harrison is introduced in a separate sentence as merely developing the opposition:

```
p.13: «… С. Н. Кузнецов в статье … формулирует это разграничение относительно вспомогательных языков …: «По традиции, восходящей к работам Г. Мока, но еще больше к знаменитым трудам Л. Кутюра и Л. Ло, все МИЯ распределяются на два класса …»»
p.14: «Интерес представляет и классификация Ричарда Харрисона, также детально разрабатывающего противопоставление априорности/апостериорности в конлангах»
```
Reproduce: `python3 /tmp/CritFactBase1/find.py "Кутюра" "Харрисона"` (helper kept in `/tmp/CritFactBase1/find.py`, prints the printed page for each hit). The book never links Harrison to Couturat/Leau; the entry's parenthetical compresses a chain across two different sources and one quoted third party.
**Smallest safe correction:** `a priori versus a posteriori (Harrison, developing a distinction the book traces, via Kuznetsov, to Couturat and Leau)`.

### F4 — MINOR: the header names `pdftotext -layout`, but the committed capture used plain mode, and the prescribed recheck returns 0 in `-layout`

L4 says "text read with `pdftotext -layout`"; L6 tells the rechecker to "re-run `pdftotext -layout` and re-find the quote". The committed capture `reports/round-73/evidence/S877.txt` records `extract: pdftotext -enc UTF-8 S877.pdf -` (no `-layout`). The Gate quote is only contiguous in plain mode — in `-layout` the line break hyphenates it:

```
$ pdftotext -layout -enc UTF-8 s877.pdf - | grep -n 'используемые в художественных произведениях'
443:          обозначений. Языки, используемые в художественных произведениях, на-
$ pdftotext -layout -enc UTF-8 s877.pdf - | grep -c 'называют вымышленными или фикциональными'
0
$ pdftotext -enc UTF-8 s877.pdf - | grep -c 'называют вымышленными или фикциональными'
1
```
(Whitespace-normalised search also returns 0 under `-layout`, because the hyphen survives normalisation as `на- зывают`.) Consequence: the EVIDENCE leg still passes (the capture's own extract line is plain and the quote is verbatim there), but a rechecker following the entry's instruction mechanically concludes the quote is gone. All §1–§4 quotes are hyphen-free and survive `-layout` intact (`вкус другой культуры`, `языки-наброски`, and the §5–§8 strings likewise), so nothing in the body is affected.
**Smallest safe correction:** name the mode actually used in the capture: "text read with `pdftotext -enc UTF-8`", and in the recheck say "re-extract with `pdftotext -enc UTF-8` (plain mode de-hyphenates; `-layout` splits `на-зывают`)".

### F5 — MINOR: the class-number locator over-ranges by one page

L40 says "in the book's numbering (pp. 11–12)". Every class number is on p. 11; p. 12 carries none.

```
$ python3 -c "import re;t=open('/tmp/CritFactBase1/s877.txt',encoding='utf-8').read().split('\f');[print('p.%d:'%(i+1), re.findall(r'\b(?:2\.1\.1|2\.1\.2|2\.1|2\.2|1)\.', t[i])) for i in (9,10,11,12)]"
p.10: []
p.11: ['1.', '2.1.', '2.1.1.', '2.1.2.', '2.2.']
p.12: []
p.13: []
```
**Smallest safe correction:** `(p. 11)`.

### Trivial, no severity
L23 writes `"impoverishment"` (singular); the book's term is `«impoverishments of the natural languages»` (p. 28). It is a label, not a quotation of a single word; flagging it only so a later recheck does not treat it as a misquote.

## What I verified and that holds (the attack that failed)

These were my strongest hypotheses; each is dead:

1. **"The book does not actually say the terminology is contested, or that it adopts a classification."** Dead: p. 10 and p. 11 carry both sentences nearly verbatim (§3 L38, §1 L20).
2. **"The class table is invented or renumbered."** Dead: the five numbers and all six row descriptions are p. 11 verbatim, including `языки-наброски` and the D'ni/Myst attribution.
3. **"Henning's volume rule is the authors' own, or overstated."** Dead: p. 12 attributes it to Henning's 1995 conlang.com article and states exactly the three-row threshold the entry tabulates (jargon / naming language / communication-or-literature).
4. **"The §1 Higley (to-verify) mark is a dodge."** Dead — it is honest and understated: the bibliography (pp. 176–181) contains **no** Higley entry, so the book gives no venue at all. `grep -n 'Higley' s877.txt` returns only body hits (pp. 29, 74, 113).
5. **"The abstract quotes are paraphrased."** Dead: both are verbatim on served line 267, 16 and 13 words.
6. **"The 'abstract is the whole opened artefact' line is dishonest."** Dead: the entry declares it, the row's tier reason matches, and §1's status is derived from it.
7. **"The book is a booklet, not a monograph / the PDF is not the whole book."** Dead: 185-page PDF, 1,055,723 B, ISBN on p. 2, Оглавление with six chapters and three appendices, ch. 1 = pp. 8–34 as the header says.

Adjacent, out of assigned scope, checked anyway because they are cheap: §8's three dated counters are exact — p. 5 «около 20 000 членов» (1999) and «около 1 500 конлангов»; p. 8 «773 … (по состоянию на 28 июля 2005 года)»; and §8's «исчисляются единицами» (p. 27) and the Higley/Schnapp/Yaguello attributions (pp. 27–29) are faithful. The entry's "peer-reviewed article" (L8) is true — the journal's about page says "peer-reviewed journal" and "double blind peer review" — but that page is not named in the entry's source line and no capture records it; `ScoutReopenS876` MINOR-2 already filed that provenance gap at row level, and I confirm it here at entry level.

## What I could NOT check

- **The article's PDF galley** (the "Downloads PDF" link on the S876 page): not opened, so I cannot say whether it carries a curriculum, cohort or count. The entry declares the abstract as the whole opened artefact, so this is a limit of the entry's scope, not a defect I can disprove.
- **Whether this article was individually peer-reviewed** (as opposed to the journal being peer-reviewed): the about page states journal-level double-blind review but does not say which sections are reviewed; the article sits in section CrOCEVIA.
- **The S877 Wayback capture** (`web.archive.org/web/20260208005339id_/…`): not fetched; I relied on the live URL, which served 200 with the same sha256 as the committed capture.
- **The Klingon grammatical description against Okrand's own grammar** — that is §7's own `(to-verify)`, outside my §1–§4 assignment; I did not open Okrand.
- **§5–§8 as a whole** — outside assignment. I read the pages they cite (pp. 19–29) while chasing §1–§4 and spot-checked the numbers, but I did not sentence-map those sections.
- **The book's chapters 2–6** beyond the pages §1–§4 (and my adjacent spot-checks) cite: I grepped the full 185-page extract but did not read every page.
- **Any counter run or selftest** — none executed; this seat attacked bytes, not legs.

## Tooling

No installs, no upgrades, no `pacman` (paused host-wide). Tools used were already present: `curl 8.23.0`, `pdftotext`/`pdfinfo` (poppler), `python3`, `git` (read-only against the lane). No subagents, no background jobs; all experiments read-only, downloads confined to `/tmp/CritFactBase1/`.
