# CritFactAmend2 — round 73, wave 2 (FALSIFY / hyaku run 7)

Seat: critic. Item: attack
`corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` §2–§5 against S879
(cyberleninka, Kostyukhin 2023) and S880 (sanders.phonologist.org, Anderson/Grant/Sanders).

Lane revision under attack: `0316b8883b4f8d44b8efd720140e7f52f734a102` (lands), base
`8841ad3b896a0227674fa0725b818c999118046f`. `git rev-parse HEAD` = lands, and
`git diff 0316b888 -- corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md`
is empty — the bytes attacked are the landed bytes. Date of every probe below: 2026-10-25.

Method: re-fetch both sources with recorded UA/status/bytes/sha256, extract the text, then read
every §2–§5 sentence that carries an (S879)/(S880) tag against the extracted span. Every finding
carries the command whose output I paste. Files live in `/tmp/CritFactAmend2/`; nothing was
written outside this report.

---

## 0. Fetch log (every request this seat made)

| # | URL | User-Agent | status | bytes | sha256 | final URL |
|---|---|---|---|---|---|---|
| 1 | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | 200 | 97656 | `23878cbca934e8aa0e8069ef93711960d61e8ebc51dfcb75033112dd62f9dddd` | same |
| 2 | same | `curl/8.7.1` | 200 | 97588 | `cd9e5630ca31cfdf2a5ebe0748148f2cb9ca767422358a1f7f8c6623194264a0` | same |
| 3 | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf` | browser-shaped (as #1) | 200 | 630227 | `cc9a91c5149ada2868fc94f93c39e61c62812466c8414ddff5643dd254c0643f` | same |
| 4 | same `/pdf` | `curl/8.7.1` | 200 | 630227 | `cc9a91c5149ada2868fc94f93c39e61c62812466c8414ddff5643dd254c0643f` (byte-identical to #3) | same |
| 5 | `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` | browser-shaped | 200 | 193610 | `26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535` | same |
| 6 | `https://doi.org/10.1017/cnj.2024.21` (`-L`) | browser-shaped | **429** | 1302 | — | `https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article` |
| 7 | same DOI | `curl/8.7.1` | **429** | 1302 | — | same |
| 8 | `https://api.crossref.org/works/10.1017/cnj.2024.21` | browser-shaped | 200 | 6670 | `6183ca31ddcdd34ec18c53197539eb63eaf18440ba6ef2ab43b2cd4e125d2492` | same |
| 9 | `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` | browser-shaped | 200 | 959171 | `9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c` | same |

No browser automation, no challenge solved, no captcha touched (QUALITY 10). No pacman, no tool
installed — `curl`, `pdftotext`, `pdfinfo`, `python3` sufficed.

Two calibration facts from the log itself:

* S880 re-fetches **byte-identical** to the committed capture (`26dbcf2c…` = `evidence/S880.txt`
  sha256), so every S880 claim below is checked against the exact captured bytes.
* S879's HTML does **not** reproduce its capture: `evidence/S879.txt` records 97622 B /
  `709e186b…`; my two fetches are 97656 B and 97588 B with two different hashes. The page is
  dynamic. The `/pdf` endpoint, by contrast, is byte-stable (identical sha across two UAs and two
  fetches) — see F3.

Text extraction used the same normalisation the capture declares (`html tags stripped, entities
unescaped (python3 re/html)`; `pdftotext -enc UTF-8`).

---

## 1. Findings

### F1 — **BLOCKER** — §2, "three categories the article's prose does not list — parody, sign and graphic languages" is false for all three, and the conclusion drawn from it is contradicted

Sentence under attack:

> "The comparison table's Peterson column carries three categories the article's prose does not
> list — parody, sign and graphic languages — so the taxonomy's full extent is a table entry, not
> an argued class (S879)."

Reproducing commands and output (text extracted from fetch #1):

```
$ grep -o 'разработанный лингвистом Уильямом Спруэллом язык Yesqur[^.]*\.' s879.txt | cut -c1-250
разработанный лингвистом Уильямом Спруэллом язык Yesqur3 можно отнести к группе пародийных языков (parody languages or jokelangs), поскольку он представ
```

```
$ grep -o 'Данную классификацию также выгодно отличает[^.]*жестов' s879.txt | cut -c1-260
Данную классификацию также выгодно отличает от других классификаций упоминание в ней конструированных языков, создаваемых на основе жестов
```

(the sentence continues after a page break / footnote intrusion in the served text with
`или графических символов`: pdf page 5 = printed p. 32 carries `Данную классификацию также
выгодно отличает … на основе жестов`, and pdf page 6 = printed p. 33 opens with
`или графических символов. Несмотря на имеющиеся достоинства, рассматриваемая классификация`
— `pdftotext -enc UTF-8 -f 6 -l 6 cl_pdf_Mozil.bin - | sed -n 2p`).

* **parody** is named in the prose, with an instance and a rationale, in the Peterson-classification
  section (printed p. 30): `… язык Yesqur … можно отнести к группе пародийных языков (parody
  languages or jokelangs)`.
* **sign** and **graphic** are named in the prose **of the comparison section itself**
  (printed pp. 32–33), and the prose does not merely list them — it argues them as an **advantage**
  of Peterson's taxonomy (`выгодно отличает от других классификаций`). So "not an argued class"
  is exactly backwards for these two.
* Only the three *English category labels* (`parody Languages (jokeLangs)`, `sign Languages
  (manual Languages)`, `graphic Languages`, table, printed p. 33) are table-only. The charitable
  reading ("the six-bullet list does not carry them as top-level bullets") does not save the
  sentence: it says "the article's prose does not list", and it draws a conclusion
  ("the taxonomy's full extent is a table entry, not an argued class") that the two quoted prose
  spans falsify.

Smallest safe correction: replace with — "The table's Peterson column names nine classes; the
prose bullet-list gives six and adds parody languages (instance: Yesqur) plus a mention of
gesture- and graphic-symbol-based constructed languages, which the article counts as an advantage
of the taxonomy. Only the three category *names* are table-only (S879, printed pp. 30, 32–33)."

Minor locator note inside the same sentence: the table is `Таблица 1 СРАВНИТЕЛЬНЫЙ АНАЛИЗ
КЛАССИФИКАЦИЙ`, printed p. 33, under the `заключение` heading — not inside the comparison
section. `pdftotext -f 6 -l 6 cl_pdf_Mozil.bin - | grep -n 'Таблица 1'` → `25:Таблица 1`.

---

### F2 — **BLOCKER** — §3 and §5 declare the study's own text unopened and its duration unknown; the study's own deposited abstract was opened this round (and is live now) and says "semester-long"

Sentences under attack:

* §3: "Whether the study itself reports a semester-long curriculum … stays (to-verify): both need
  the article's own text, which was not opened this round."
* §5: "The publisher's abstract of the study was not opened … Section §3 therefore rests on a
  companion article's account of the study, not on the study itself (S880)."

Reproducing command and output (fetch #8, HTTP 200, 6670 B):

```
$ python3 -c "
import json,re,html
t=html.unescape(re.sub(r'<[^>]+>','',json.load(open('cr_cnj.json'))['message']['abstract']))
i=t.find('semester-long'); print(repr(t[i-70:i+80]))"
's courses sometimes struggle with phonology, active engagement with a semester-long language construction project endowed these students with the prac'
```

The full deposited abstract (145 words) also says `This paper reflects on a project-based
curriculum employing constructed languages to teach linguistics, with a focus on phonology. In a
special topics linguistics course, nine students were led through the construction of a language.`

This is not a discovery I am adding late: the lane's **own committed w1 seat report** records the
same payload, same round, and quotes the abstract's first sentence as its located quote —

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r 0316b888 --name-only -- .ufo/waves/round-73/w1/RevSowersAccess.md
.ufo/waves/round-73/w1/RevSowersAccess.md
$ sed -n '30,31p' .ufo/waves/round-73/w1/RevSowersAccess.md
| https://api.crossref.org/works/10.1017/cnj.2024.21 (UA-B) | 200 | 6670 | YES — `abstract` field, full text |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1017/cnj.2024.21?fields=title,abstract,venue,year,externalIds (UA-B) | 200 | 3658 | YES — `abstract` field identical span |
```

and it states there: "Located quote (18 words … verbatim from the Crossref `abstract` field,
first sentence): *This paper reflects on a project-based curriculum employing constructed
languages to teach linguistics, with a focus on phonology.*"

So the landed entry contradicts evidence committed in the same revision, and the "semester-long"
element the amendment cut as unsupported **is** supported by the study's own abstract. What is
true is narrower: the token is absent from **S880** (0 hits, verified — see cleared checks) and the
**publisher page** 429s (verified — see §5 row below).

Smallest safe correction: keep the DOI-429 fact; replace the two provenance sentences with —
"The Cambridge page answered HTTP 429 to both a browser-shaped and a plain client
on 2026-10-25 (its OA PDF likewise 429'd in wave 1); the study's deposited abstract was opened this round from Crossref (200, 6670 B)
and Semantic Scholar (200, 3658 B), and it reports 'a semester-long language construction project'
in 'a special topics linguistics course'. The companion article (S880) carries no duration token,
which is why §3's quotes carry none; the study's own full text remains unopened."

---

### F3 — **MAJOR** — §2 "Location limit … is (to-verify)" is a false limit: the site serves a byte-stable PDF and the page is printed p. 32

Sentence under attack:

> "Location limit: the cyberleninka text is served as extracted HTML with no page markers, so the
> page for items 1–2.2 within the article's pp. 28–34 is (to-verify); the section heading and item
> numbers locate the passage (S879)."

Reproducing commands and output (fetches #3/#4):

```
$ curl -sS -o cl_pdf_Mozil.bin -w 'status=%{http_code} bytes=%{size_download} type=%{content_type}\n' \
    -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
    'https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf'
status=200 bytes=630227 type=application/pdf
$ pdfinfo cl_pdf_Mozil.bin | grep -i pages
Pages:           7
$ pdftotext -enc UTF-8 -f 5 -l 5 cl_pdf_Mozil.bin - | grep -c '2\.2\. Personal languages'
1
$ pdftotext -enc UTF-8 -f 5 -l 5 cl_pdf_Mozil.bin - | sed '/^$/d' | tail -2
32
Vestnik of MSLU. Humanities. Issue 2 (870) / 2023
```

PDF p. 5 of 7 within printed pp. 28–34 (the article's own citation line reads `С. 28-34`,
`s879.txt:82`) ⇒ **item 2.2 is on printed p. 32**. The first clause of the sentence is true (the
HTML carries no page markers); the conclusion is false, and it contradicts the lane's own Gate row
and evidence capture, which assert `item 2.2 (PDF p. 5 = printed p. 32)` — those are **right** and
the amendment is **wrong**.

Why it matters beyond pedantry: the `/pdf` endpoint is byte-stable (`cc9a91c5…` across two UAs and
two fetches), while the HTML is not (my two fetches differ by 68 B and by sha, and neither
reproduces the capture's `709e186b…`). The row's anchor currently rests on the unstable artefact
when a stable one on the same host carries the same span.

Smallest safe correction: delete the limit; state "item 2.2 sits on printed p. 32 (PDF p. 5 of 7;
`…/pdf`, HTTP 200, 630227 B, sha256 cc9a91c5…, byte-stable across two fetches)", and point the
row's anchor at the PDF.

---

### F4 — **MAJOR** — §4 "every taxonomy the review article compares sorts on purpose before it sorts on form" is not in S879, and S879's own table contradicts the "before it sorts on form" half

Sentence under attack:

> "Classify a world's constructed language by the purpose it serves in that world first, then by
> structure: every taxonomy the review article compares sorts on purpose before it sorts on form
> (S879)."

Reproducing commands and output:

```
$ grep -c 'цели создания' cl_pdf.txt
1
$ grep -o 'В зависимости от цели создания[^:]*:' cl_pdf.txt
В зависимости от цели создания он предлагает выделять следующие типы конлангов
```

Purpose-of-creation is stated **once**, and only for Peterson. For the other two typologies the
article gives no sorting criterion at all; its only cross-taxonomy generalisations are about
*shared categories*, not about an ordering of criteria — `все исследователи выделяют в отдельную
группу вспомогательные языки` and `во всех трех классификациях присутствует категория
художественных языков`. The comparison dimensions in the article's table are `Используемые
категории` / `Охват` / `Степень систематизации материала` — nothing about purpose-before-form.
And Peterson's own column carries `sign Languages (manual Languages)` and `graphic Languages`,
which are **modality/form** classes, so "sorts on purpose before it sorts on form" is contradicted
by the same taxonomy it is predicated on.

Smallest safe correction: "each of the three typologies uses purpose-defined top-level classes
(auxlang / artlang / logical), and Peterson's additionally carries two modality classes (sign,
graphic) — so purpose comes first in all three, and form appears at all only in Peterson's
(S879)."

---

### F5 — **MAJOR** — §2's Peterson sentence omits the article's own caveat that the six-way purpose split may be an erroneous impression

Sentence under attack:

> "Peterson's taxonomy, delivered as a 2015 podcast episode, sorts by purpose of creation into
> personal, secret or stealthlang, auxiliary, fictional, artistic, and engineered languages …"

The six classes and all six instance groups are verbatim supported (see cleared checks). What the
entry omits is the article's immediately following caveat, in the same section, printed p. 33:

```
$ python3 -c "
import re;t=re.sub(r'\s+',' ',open('s879.txt',encoding='utf-8').read())
print(re.search(r'может сложиться ошибочное впечатление.*?артлангов',t).group(0))"
может сложиться ошибочное впечатление, что Питерсон распределяет по отдельным группам персональные языки и вымышленные языки, хотя в действительности, как отмечает на своем вебсайте конлангер Йорг Римайер, они входят в более крупную категорию артлангов
```

So the source flags the personal/fictional split as a possibly **erroneous impression** (per Jörg
Rhiemeier, both fall inside artlangs). The entry presents it as settled and then builds §4's
"classify by purpose first" rule on it. This is an omission, not a misquote — but it makes an
admitted statement stronger than its source.

Smallest safe correction: append "— a split the article itself says may be an erroneous
impression: per Rhiemeier, personal and fictional languages fall inside artlangs (S879, p. 33)."

---

### F6 — **MAJOR** — the amend's `recheck:` promise ("re-locate its quoted span … one grep per row") is not met for S879: the recorded recheck greps a different sentence

Sentence under attack (entry header):

> "recheck: 180d — re-open each of the three rows above and re-locate its quoted span (one grep
> per row, each prints 1; the three commands and their 2026-10-25 outputs stand in the round-73
> gate record …)"

The S879 row's quoted span (Gate + `evidence/S879.txt`) is `2.2. Personal languages Это личные,
или персональные, языки, т. е. вымышленные языки, проектируемые отдельными энтузиастами
лингвоконструирования`. The recorded recheck command (`.ufo/waves/round-73/w1/ScoutS893.md:103`)
is a grep for a **different** sentence:

```
$ grep -c '2\.2\. Personal languages' s879.txt
1
$ grep -c 'Шувалова и М. Ю. Сидорова предлагают следующую классификацию' s879.txt
1
$ python3 -c "print('Шувалова и М. Ю. Сидорова предлагают следующую классификацию'.find('2.2. Personal languages')!=-1)"
False
```

Both print 1 today, so the letter of "each prints 1" holds — but the recheck would still pass
with the anchor quote deleted, which is exactly what a 180-day recheck is for. (S880 and S878 are
fine: `pdftotext … | grep -c 'multi-part, creative project'` → 1, and the S878 token → 1, with
`s878.pdf` byte-identical to `evidence/S878.txt`, sha `9f745dda…`.)

Smallest safe correction: change S879's recheck token to a substring of the anchor quote
(e.g. `grep -c '2.2. Personal languages'`) — it prints 1 today on both the HTML and the PDF.

---

### F7 — **MINOR** — §3 puts the 16-word quote on p. 5; it is on p. 4

```
$ pdftotext -enc UTF-8 -f 4 -l 4 s880.pdf - | tr '\n' ' ' | grep -c 'Sara Sowers-Wills assesses'
1
$ pdftotext -enc UTF-8 -f 5 -l 5 s880.pdf - | tr '\n' ' ' | grep -c 'Sara Sowers-Wills assesses'
0
```

The sentence is in §3 ("3. These papers" starts on p. 4 — `pdftotext -f 4 -l 4 s880.pdf - |
sed -n 1,2p` → `4` / `3. These papers`), so the section is right and the page is wrong. The other
two quotes are on p. 5 as claimed (`… -f 5 -l 5 … | grep -c 'One innovation of this work'` → 1).
Smallest correction: `§3, p. 4` for that one quote.

### F8 — **MINOR** — §3's "the only description of its format the companion article gives" is contradicted by the sentence the entry itself quotes two lines earlier

```
$ python3 -c "
import re;t=re.sub(r'\s+',' ',open('s880.txt',encoding='utf-8').read())
print(re.search(r'In the course, examples.*?typology\.',t).group(0))"
In the course, examples of phonological systems in natural languages and constructed languages were presented along with instruction in language universals and typology.
```

That is a second description of how the course ran, in the same paragraph. Smallest correction:
"the only description of its *mode*" (active learning / project-based), or drop the universal.

### F9 — **MINOR** — two different agents for the same act: §2 "the same authors propose «авторскими языками»" vs §5 "the review article … proposes «авторскими языками»"

```
$ python3 -c "
import re;t=re.sub(r'\s+',' ',open('s879.txt',encoding='utf-8').read())
print(re.search(r'Их исследователи предлагают[^.]*\.',t).group(0))"
Их исследователи предлагают также обозначать «авторскими языками».
```

The source's agent is "их исследователи" (the researchers of these languages) — neither "the same
authors" (Шувалова/Сидорова) nor "the article". The article's own table does put `авторские языки`
inside the Шувалова/Сидорова column, so §2's reading is defensible; §5's is not, and the two
cannot both stand. Smallest correction: one attribution in both places — "the article reports that
researchers of these languages propose «авторскими языками», and its table carries the label in the
Шувалова/Сидорова column (S879)".

### F10 — **MINOR** — "rather than a published taxonomy" is not in S879, which cites Peterson's 2015 book for the classification's content

```
$ grep -c 'Peterson, 2015; Питерсон, 2018' s879.txt
2
```

The article's claim is narrower: the classification is presented *orally, in podcast format*, and
consists of recommendations to beginning conlangers. Whether a published version exists is not
stated. Smallest correction: "delivered orally as a 2015 podcast episode; the article cites
Peterson's 2015 book elsewhere but does not say the taxonomy is published there".

### F11 — **MINOR** — "which the article attributes to its oral podcast form" drops the source's "отчасти" (partly)

```
$ python3 -c "
import re;t=re.sub(r'\s+',' ',open('s879.txt',encoding='utf-8').read())
print(re.search(r'она уступает по уровню систематизации.*?подкаста\.',t).group(0))"
она уступает по уровню систематизации материала типологиям российских лингвистов, что отчасти объясняется способом ее представления: Питер-сон знакомит слушателей со своей классификацией устно в формате подкаста.
```

Smallest correction: "which the article says is *partly* explained by its oral podcast form".

### F12 — **MINOR** — §2's gloss of 2.1.2 ("languages that exist only inside the work") drops "functioning or merely mentioned"

```
$ python3 -c "
import re;t=re.sub(r'\s+',' ',open('s879.txt',encoding='utf-8').read())
print(re.search(r'2\.1\.2\. Языки[^К]*',t).group(0))"
2.1.2. Языки, «функционирующие» или просто упоминающиеся только в пределах соответствующего художественного произведения
```

The criterion is functional/mention status, not existence. Smallest correction: "languages that
function, or are merely mentioned, only inside the work (Arëndron)".

---

## 2. Per-sentence table — every §2–§5 sentence carrying an (S879)/(S880) tag

Legend: **SPAN** = the source span was located and says what the entry says; **FALSE**,
**UNSUPPORTED**, **OVERSTATED**, **MISATTRIBUTED** as named; severity in brackets.

| # | Sentence (abridged) | Cite | Verdict | Basis |
|---|---|---|---|---|
| §2.1 | Шувалова/Сидорова divide in two; 2.1 Artlangs → 2.1.1 (Tolkien, Klingon, Э'П/Myst) / 2.1.2 (Arëndron) | S879 | **SPAN** (2.1.2 gloss lossy — [MINOR] F12) | items `1.`, `2.`, `2.1Artlangs`, `2.1.1.`, `2.1.2.`, `2.2.` all present verbatim; instances verbatim; printed pp. 31–32 |
| §2.2 | 2.2 "Personal languages" …; "the same authors propose «авторскими языками»" | S879 | quote **SPAN**; agent **MISATTRIBUTED** [MINOR] F9 | `Их исследователи предлагают…`; table carries the label in the Шувалова/Сидорова column |
| §2.3 | Piperski (2017) three-way split (loglan, lojban / auxlangs / artlangs) | S879 | **SPAN** | `языки философские, или логические … (логла-на или ложбана)`, `международные вспомогательные языки (ауксланги)`, `художественные языки, или артланги` |
| §2.4 | Peterson 2015 podcast; six purpose classes; Vorlin / Awolang / Esperanto,Novial / Quenya,Sindarin,Klingon,Verdurian / Okuna / ro,Ithkuil | S879 | **SPAN** for the six and every instance; **OVERSTATED** by omission [MAJOR] F5 | `В 2015 году … первый эпизод подкаста … «Типы конлангов»`; `В зависимости от цели создания`; six bullets with exactly those instances |
| §2.5 | verdict quote "Наиболее детализированной …", 10 tokens, in the differences paragraph | S879 | **SPAN** | verbatim; 10 tokens; paragraph starts `Следующее различие … в степени детализации` |
| §2.6 | most detailed yet systematizes worse, attributed to the podcast form | S879 | **SPAN**; **OVERSTATED** by dropping "отчасти" [MINOR] F11 | `уступает по уровню систематизации … отчасти объясняется … подкаста`; table `Низкая` vs `Высокая`/`Высокая` |
| §2.7 | Calibration: one author's comparison, not a field consensus; "rather than a published taxonomy" | S879 | first clause **SPAN** (hedge); second **OVERSTATED** [MINOR] F10 | article cites `[Peterson, 2015; Питерсон, 2018]` twice |
| §2.8 | table's Peterson column carries three categories the prose does not list — parody, sign, graphic | S879 | **FALSE** [**BLOCKER**] F1 | prose: `группе пародийных языков (parody languages or jokelangs)` (p. 30); `упоминание … на основе жестов` + `или графических символов`, argued as an advantage (pp. 32–33) |
| §2.9 | the article's subject is Peterson's classification and its advantages over the Russian typologies | S879 | **SPAN** | abstract: `… предложенной … Дэвидом Питерсоном, и ее преимуществ по отношению к другим типологиям … отечественными лингвистами` |
| §2.10 | footnote: Lojban's auxlang placement disputable; Piperski puts it in the philosophical/logical group | S879 | **SPAN** | `Отнесение языка ложбан к группе вспомогательных языков представляется дискуссионным…` |
| §2.11 | Location limit: no page markers, so the page is (to-verify) | S879 | first clause **SPAN**; conclusion **FALSE** [MAJOR] F3 | `/pdf` → 200, 630227 B, byte-stable; PDF p. 5 of 7 = printed p. 32 |
| §3.1 | 16-word description, "§3, p. 5" | S880 | quote/count/section **SPAN**; page **FALSE** [MINOR] F7 | on p. 4, not p. 5 |
| §3.2 | 23-word course-design quote, same section and page | S880 | **SPAN** | verbatim (23 words) on p. 5 |
| §3.3 | 25-word novelty quote, same section and page | S880 | **SPAN** | verbatim (25 words) on p. 5; matches the Gate quote byte-for-byte |
| §3.4 | "an active learning approach in a project-based phonology course" + "the only description of its format" | S880 | quote **SPAN** (de-hyphenated line break); universal **OVERSTATED** [MINOR] F8 | PDF word boxes `project-` (end of line) + `based` (next line); a second format description follows in the same paragraph |
| §3.5 | "semester-long" occurs zero times in its nine pages | S880 | **SPAN** | `pdfinfo` → `Pages: 9`; `grep -ci semester` → 0 |
| §3.6 | "Whether the study itself reports a semester-long curriculum … was not opened this round" | S880 | **FALSE** [**BLOCKER**] F2 | Crossref abstract (200, 6670 B) contains `a semester-long language construction project`; lane's own `RevSowersAccess.md:30-31` records the same payload |
| §4.1 | "every taxonomy the review article compares sorts on purpose before it sorts on form" | S879 | **UNSUPPORTED** [MAJOR] F4 | `цели создания` occurs once, for Peterson only; table carries modality classes (sign, graphic) |
| §4.2 | a priori / a posteriori scale rather than a label | S878 | **not checked** — outside this seat's item (§1/§4 S878 material) | — |
| §4.3 | expect Eurocentrism as a default | S878 | **not checked** — outside item | — |
| §4.4 | classroom evidence supports "assesses a student's command of phonological concepts … nothing here compares it with lectures" | S880 | **SPAN** | `assesses students' command of concepts in phonology`; `lecture` occurs once in the whole PDF, in a reference title (`Lecturers' perceptions…`) |
| §5.1 | DOI answered HTTP 429 to both a browser-shaped and a plain client | (fetch log) | **VERIFIED by re-measure** | #6 and #7: 429, 1302 B, both UAs, final URL cambridge.org/core/product/identifier/S0008413124000215/type/journal_article |
| §5.2 | "The publisher's abstract of the study was not opened" | (fetch log) | **FALSE** in substance [**BLOCKER**] F2 | the publisher-deposited abstract is served by Crossref (200, 6670 B) and S2 (200, 3658 B) and was read this round |
| §5.3 | "§3 therefore rests on a companion article's account … not on the study itself" | S880 | **FALSE** [**BLOCKER**] F2 | as §5.2 |
| §5.4 | "semester-long" absent from the companion article's nine pages | S880 | **SPAN** | 0 hits / 9 pages |
| §5.5 | «автоконланги» absent; the article "proposes «авторскими языками»" | S879 | absence **SPAN**; agent **MISATTRIBUTED** [MINOR] F9 | `автоконланг` → 0 hits; `авторскими языками` → 1 hit, agent `Их исследователи` |
| header | recheck: "one grep per row, each prints 1 … re-locate its quoted span" | all three | **FALSE for S879** [MAJOR] F6 | recheck token does not contain the anchor quote |

---

## 3. Checks that held (so the report is not only negatives)

* Shuvalova/Sidorova numbering `1` / `2` / `2.1` / `2.1.1` / `2.1.2` / `2.2` — all verbatim, in
  order, printed pp. 31–32 (`grep -c '1. Auxlangs. Вспомогательные языки'` → 1 on both HTML and
  PDF; `2.2. Personal languages` → 1).
* `Arëndron` — verbatim (`К ним вполне можно отнести язык Arëndron Майкла Рептона.`).
* Piperski's three-way split — verbatim, including the loglan/lojban examples.
* Peterson's six classes **and all six instance groups** — verbatim, in the article's order
  (Vorlin; Awolang; эсперанто/новиаль; квенья, синдарин, клингонский, вердурианский; Okuna;
  ро и ифкуиль).
* The "Наиболее детализированной …" quote — verbatim and exactly 10 tokens.
* "systematizes worse than the Russian typologies" — supported in prose **and** in the table
  (`Степень систематизации материала`: `Низкая` for Peterson vs `Высокая` for both Russian
  typologies).
* Lojban footnote — verbatim.
* "the article's own subject is Peterson's classification" — verbatim in the abstract.
* The 16/23/25-word quotes are verbatim in the S880 capture and count 16/23/25 words
  (`python3` word counts over the whitespace-collapsed text).
* `project-based` is a faithful de-hyphenation, not a misquote: PDF word boxes give `project-`
  ending one line (y=183.108) and `based` starting the next (y=199.384).
* "semester-long" → 0 hits in S880's 9 pages; "nine pages" correct.
* The three recheck greps print 1 today (S879 HTML 1, S880 `multi-part, creative project` 1,
  S878 `by analyzing various types of languages based on their lexical` 1), and `s878.pdf` is
  byte-identical to its capture (`9f745dda…`), as is `s880.pdf` (`26dbcf2c…`).
* The header's "served heading … case-mangled by the site's text layer" — correct: the HTML has
  `сОпОсТАВЛЕНИЕ КЛАссИФИКАцИИ …`, the PDF has `Сопоставление классификации`.
* The article's page range `28–34` — correct (`Для цитирования: … 2023. Вып. 2 (870). С. 28-34`).
* "nothing here compares it with lectures" (S880) — correct.
* «автоконланги» absent (0), «авторскими языками» present (1).
* §5's DOI-429 claim — re-measured, still 429/1302 B under both UAs.

---

## 4. What I could NOT check

* **§1 and the S878-tagged sentences of §4** (a priori/a posteriori scale, Eurocentrism) — outside
  my item; I did not audit them. I fetched S878 only to run its recheck grep.
* **The Sowers-Wills article's full text.** The DOI-resolved Cambridge page 429s under both UAs
  (measured here); its OA PDF 429'd in wave 1 (`RevSowersAccess.md`). I read only its deposited
  abstract (Crossref). Whether the full article argues anything
  about lectures remains unverified — but the abstract already answers the "semester-long" half of
  §3's (to-verify), which is what F2 rests on.
* **Whether Peterson's 2015 book contains the taxonomy** — I did not open it; F10 is limited to what
  S879 states.
* **Whether «авторскими языками» is Шувалова/Сидорова's own coinage** — S879 only reports a
  proposal by "их исследователи"; the primary book (S877) was not re-read for this point.
* **Claim Ca material** (ledger, SCORECARD corrections, SHONEN/SKILL edits) — outside my item.
* **The other ~30 w1/w2 seat reports** — I read only the four that bear on S879/S880/S878
  (`ScoutS893`, `ScoutS901`, `ScoutS892`, `RevSowersAccess`).
* **Byte-reproducibility of the S879 HTML capture** — my two fetches differ from each other and
  from `evidence/S879.txt`; I cannot say which response the capture saw. The PDF, however,
  reproduces exactly.
* **The exact word-count convention** for "10 tokens" in §2.5 — I counted whitespace tokens; the
  Gate's convention is `wc -w`. Both give 10 here.

---

## 5. Impacted axes and the smallest safe correction set

* **Coverage (claim C)** — not moved: all five rows still exist and every cited span I checked is
  present in its source. F1/F2/F5/F8 are content defects inside an admitted entry, not row
  defects. F3 and F6 do touch provenance: the S879 anchor should move to the byte-stable PDF, and
  its 180d recheck should target the anchor quote.
* **Calibration** — F2 is the one that matters: the round's own w1 evidence (`RevSowersAccess`)
  disproves a provenance limit the landed entry still declares. Any later round that inherits
  "the study was not opened" will re-derive a limit that no longer exists.
* **The single smallest safe correction** (one edit, if only one is taken): **F2** — replace the
  two "not opened" sentences with the measured state (DOI 429; deposited abstract read via
  Crossref/S2; "semester-long language construction project" is the study's own words). It is the
  only finding where the entry states a fact the lane's own committed evidence contradicts.
* **Second smallest**: **F1** — the parody/sign/graphic sentence, which is false in all three
  clauses and draws a conclusion its own source reverses.

Verdict from this seat: **2 BLOCKER, 4 MAJOR, 6 MINOR**. The entry cannot be called faithful to
S879/S880 until F1 and F2 are repaired; F3, F4, F5 and F6 should be repaired in the same pass
because each is one sentence and each is provable from the commands above.
