# ScribeEntryBase — round 73 wave 1 — base entry draft for claim C

Seat: ScribeEntryBase (leaf). Date: 2026-10-25. Item: draft the base entry
`corpus/knowledge/linguistics/conlang-scholarship.md` from the staged
`merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md`, to the lane bar
(`corpus/QUALITY.md` criteria 1–21) and the lane entry format, citing only tentative ids S876 and
S877 and deleting the staged clause that names a "conference paper (S728)".

Artifact written (the only repo path this seat touched):
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/w1/drafts/conlang-scholarship.md`
— 105 lines, 13,231 bytes, nine sections (§1 calibration key, §2 method, §3 taxonomy, §4 volume
rule, §5 fictional-vs-auxiliary contracts, §6 description-first and authored history, §7 three
languages that left the page, §8 status in the field, §9 handoff). Four decision tables; every
cited line carries exactly one S-id; no table row carries an id.

Scratch: `/tmp/ScribeEntryBase/` (`ojs-7099.html`, `conlangs.pdf`, `conlangs.txt`, `flat.txt`).

## 1. Fetches — commands, raw outputs, UA

One browser-shaped User-Agent was used for both fetches and is recorded here verbatim:
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
$ curl -sS -L --max-time 90 -A '<UA above>' -o /tmp/ScribeEntryBase/ojs-7099.html \
    -w 'HTTP %{http_code} -> %{url_effective} bytes=%{size_download}\n' \
    'https://ojs.unito.it/index.php/ricognizioni/article/view/7099'
HTTP 200 -> https://ojs.unito.it/index.php/ricognizioni/article/view/7099 bytes=30289
```
```
$ curl -sS -L --max-time 90 -A '<UA above>' -o /tmp/ScribeEntryBase/conlangs.pdf \
    -w 'HTTP %{http_code} -> %{url_effective} bytes=%{size_download} type=%{content_type}\n' \
    'http://www.philol.msu.ru/~sidorova/files/conlangs.pdf'
HTTP 200 -> http://www.philol.msu.ru/~sidorova/files/conlangs.pdf bytes=1055723 type=application/pdf
```
No wall, no redirect off the cited URL, no challenge. Text extraction: `pdftotext -layout conlangs.pdf
conlangs.txt` → 9,603 lines; `pdfinfo` reports Title `verstka`, Author `G4`, QuarkXPress 4.11 /
Distiller 5.0, 2007-07-15 (i.e. the PDF is a print layout of the 2006 book, not a scan).
Quoted spans were re-found in the text after flattening line breaks (`tr '\n' ' ' | tr -s ' '`).

## 2. What each cited sentence rests on (locator map for the Gate)

S876 — Enguehard, `https://ojs.unito.it/index.php/ricognizioni/article/view/7099`; abstract
paragraph at page-source line 267 of the served page, under `<h2 class="label">Abstract</h2>`:
- "the construction of languages by students allows them to better grasp the reality of linguistic
  analysis" — 16 words, abstract sentence 1.
- "the same ones that lead most linguists to marginalize constructed languages from research" — 13
  words, abstract sentence 2.
- keywords "Constructed languages, Linguistic Analysis, Linguistics Teaching, Method-Oriented
  Teaching" — `citation_keywords` meta fields on the same page.

S877 — Сидорова & Шувалова 2006, the book PDF; page numbers are the PDF's own printed page markers
(`pdftotext -layout` emits `Page N` between leaves; each quote below was re-found in the flattened
text at the line noted):
- typology (auxlangs / artlangs 2.1 with 2.1.1–2.1.2 / personal 2.2 / языки-наброски) — p. 11–12,
  text lines 474–500.
- no terminological unity among linguists and conlangers — p. 10, line 433.
- "Язык выступает здесь как объект и инструмент познания" (8 words) — p. 11, line 506.
- competing classifications (Rosenfelder; Harrison after Couturat/Leau; Capuzzo; HKU letter+SVO
  index) — pp. 12–16, lines 535–770.
- auxiliary vs fictional on three axes — pp. 16–20, lines 740–945.
- "Эти языки и их создатели не «должны», а «могут»." (9 words) — p. 19, line 948.
- no manifesto/memorandum genre; how-to literature offers options — p. 19–20, lines 943–960.
- poetic function (Jakobson) — p. 21, lines 1012–1018.
- "первичность описания языка" (5 words; the printed phrase runs on "…по отношению к языку как
  таковому", which pdftotext splits as "тако-вому") — p. 6, line 232.
- "описывают то, что уже существует, проектирование подразумевает создание объекта" (9 words) —
  p. 6, lines 247–250.
- discontinuous, author-sanctioned change; history written backwards or forwards; resources may be
  rewritten — pp. 21–22, lines 1063–1115.
- Tolkien (~two dozen languages; Quenya/Sindarin corpora incl. the Lord's Prayer; others names and
  grammar fragments) — pp. 22–24, lines 1119–1200.
- Klingon (Okrand, extinct Native American languages, maximal difference from Earth's languages, OVS,
  no tense/gender/adjectives, own script; KLI 1992; journal with ISSN; dissertations) — pp. 24–26,
  lines 1212–1290.
- D'ni (Watson for Cyan/Myst; the fiction of a complete language revealed in pieces; creator-led
  decipherment; the book's own explanation of its standing) — pp. 26–27, lines 1295–1340.
- "исчисляются единицами" (2 words) — p. 27, line 1353.
- Yaguello, Schnapp («филологами воображаемых миров», "impoverishments of the natural languages"),
  Henning, Higley ("конланги – это действительно модели, артефакты"; the model-sailboat passage) —
  pp. 27–29, lines 1355–1475.
- Henning's volume rule (jargon «вкус другой культуры» / naming language / communication) —
  pp. 12–13, lines 560–575.
- dated counters (langmaker ~1,500; conlang.com 773 as of 28 July 2005; ~20,000 members in 1999) —
  pp. 5 and 8, lines 180–200 and 330–350.

## 3. Gates exercised (only what was actually run)

```
$ python3 -B tools/check-cited-lines.py .ufo/waves/round-73/w1/drafts/conlang-scholarship.md
CITED-LINES: 0 finding(s) in 1 file(s)          # exit 0
$ wc -l .ufo/waves/round-73/w1/drafts/conlang-scholarship.md
105
$ grep -c 'S728\|S769\|S806\|S881\|S882\|S892\|S893\|S901' <draft>
0
$ grep -o 'S[0-9]\{3\}' <draft> | sort | uniq -c
      5 S876
     24 S877
$ grep -cE '^ *\| ?S[0-9]{3} ' corpus/SOURCES.md
799                                            # registry ends at S875
$ grep -c 'ojs.unito.it\|philol.msu.ru' corpus/SOURCES.md
0
$ for p in linguistics/conlang-methodology.md linguistics/naming-systems.md \
    linguistics/phonetics-phonology.md linguistics/historical-linguistics.md \
    linguistics/writing-systems.md synthesis/worldbible-integration-contract.md; do
    [ -f "corpus/knowledge/$p" ] && echo "OK $p"; done
OK (all six; every path named in the `- couples:` line exists)
```
Quote discipline: each of the ten quoted spans was re-found in the source text (`grep -c -F` → 1 in
the flattened book text, or 2 in the article HTML where the abstract appears both as metadata and as
body), and each is ≤25 words by `wc -w`: 16, 13, 3, 3, 9, 5, 9, 2, 5, 6. Two candidate quotes were
dropped because `pdftotext` hyphenates them across lines and the full span would not re-locate
("…языку как тако-вому", "…серьезно трак-тующие…"); the first is now quoted only up to
"первичность описания языка" with the rest paraphrased, and the second is quoted as
"исчисляются единицами" alone.

Not run (so not claimed): the round's accept-c counter, the Gate-record leg of `corpus/lessons/round-73.md`
(no lesson file exists yet), any registry-row check, and any landing. This draft is not the landed
entry and has not been through a second reader.

## 4. Findings — staged text vs the opened sources (for freeze; nothing decided here)

F1. **The staged row's artefact description is falsified.** Staged S882 calls the PDF a "series
announcement booklet with the book's contents". The opened file is the whole 184-page book
(1,055,723 bytes; title page, аннотация, Оглавление, preface pp. 4–7, ch. 1 pp. 8–34 with full body
text, bibliography to p. 176). Consequence for the freeze: the S877 row's `scope` cell ("the framing
and chapter structure of the … book this booklet announces") understates the opened artefact, and the
tier question reopens — a book is primary for its own taxonomy, where an announcement booklet is not
(QUALITY 6). I cite S877 as tier B because that is the register's current scope and I do not decide
row scope; the entry's `- sources:` line states that the opened artefact is the whole book.

F2. **The staged `ground:` line cites a file that exists nowhere.** "round 1's CANNOT-ANSWER §4"
resolves in neither the lane (`find . -name 'CANNOT-ANSWER*'` outside .git/.ufo → nothing) nor the
staged package (`find merge/kotodama -iname '*CANNOT*'` → nothing). Replaced with an executed check
(799-row registry, 0 rows for either URL).

F3. **The staged `recheck:` line cites a campaign file.** "the two row recheck commands in round 2's
`SOURCES-PROPOSED.md` (S881 -> 2, S882 -> 2)" — the file is not in the lane and the "-> 2" cells are
campaign-internal counters. Replaced with a self-contained re-locate instruction.

F4. **Two staged coupling paths do not exist in the lane**: `linguistics/phonology-systems.md` and
`culture-material/worldbuilding-setting-practice.md` (both MISSING; the lane has
`linguistics/phonetics-phonology.md` and no `worldbuilding-setting-practice.md` anywhere under
`corpus/knowledge/`). Replaced with six paths that exist and fit.

F5. **"вымышленные языки as a third kind" is wrong against the book's own numbering.** The book's
typology (p. 11) makes auxlangs class 1 and вымышленные языки class 2 (2.1 artlangs, 2.1.1–2.1.2,
2.2 personal). The entry uses the book's numbering instead.

F6. **The staged §2 phrase "produces analysable data" is not in the abstract.** The abstract says
students "better grasp the reality of linguistic analysis"; the word "data" occurs only about
exercises on natural-language data. The entry quotes the abstract and does not carry the paraphrase.

F7. **Klingon's grammar is second-hand in S877.** OVS / no tense / no gender / no adjectives / own
script are the book's report of Okrand's language; the entry marks them (to-verify) against Okrand's
own grammar.

F8. The S876 row's staged keywords are a 4-token subset of the live 10; the entry names only the four
that frame the argument, which is accurate but not exhaustive.

## 5. Every staged sentence cut, and why

| Staged text (verbatim) | Disposition | Why |
|---|---|---|
| `source: S881 — … — Abstract — fetched 2026-10-23` | rewritten as S876, fetched 2026-10-25, locator "abstract paragraph … page-source line 267" | id re-pointed by document; "Abstract" alone does not locate a span; the date is this seat's fetch |
| `source: S882 — … — аннотация + Оглавление — fetched 2026-10-23` | rewritten as S877, fetched 2026-10-25, scope "the whole 184-page book … preface pp. 4–7, ch. 1 pp. 8–34" | id re-pointed by document; locator widened to what was actually opened (F1) |
| `verified-at: 2026-10-23` | → `2026-10-25` | this seat re-opened both sources |
| `recheck: 180d — re-run the two row recheck commands in round 2's SOURCES-PROPOSED.md (S881 -> 2, S882 -> 2) (ran 2026-10-23)` | cut | cites an absent campaign file and campaign counters (F3) |
| `ground: round 1's CANNOT-ANSWER §4 — the lane's conlang sources were craft manuals and typological datasets, with no constructed-language research venue as a row.` | cut | the cited file exists in neither tree (F2); replaced by an executed registry check |
| `Round 1 added a conference paper (S728) because no venue could be reached.` | cut | campaign id naming an unrelated lane document (S728 = Qaqet child-directed speech); the assignment's explicit deletion, and claim C's REPOINTED leg |
| `This entry establishes that peer-reviewed venues exist, and that the literature is not English-only.` | cut | overstates two sources (one article, one 2006 monograph); replaced by the concrete "one peer-reviewed article and one Russian-language monograph … read in the original language" |
| `the peer-reviewed argument that conlang construction is a method that yields analysable linguistic data rather than decoration` (topic line) | cut | not the abstract's claim (F6) |
| `… the taxonomy of artificial languages and the vocabulary that separates вымышленные языки from auxiliary languages` | rewritten | the book's own term is not "vocabulary that separates"; the entry says "its separation of вымышленные языки from auxiliary languages" |
| `` `linguistics/phonology-systems.md` `` (couples) | cut | path does not exist in the lane (F4); `linguistics/phonetics-phonology.md` named instead |
| `` `culture-material/worldbuilding-setting-practice.md` (the practitioner side of the same question) `` (couples) | cut | path does not exist in the lane (F4) |
| `**§1 Calibration key** — what a peer-reviewed conlang article and a scholarly book announcement can each carry.` | cut, replaced by §1 status table | "book announcement" is falsified (F1); criterion 2 wants a status per framework, which a sentence cannot carry |
| `**§2 Conlangs as method** — from S881: construction as a teaching instrument that produces analysable data, and the asymmetry between how linguists teach and how they research.` | kept as §2, re-worded | the asymmetry is in the abstract; "produces analysable data" is not (F6) |
| `**§3 A taxonomy of artificial languages** — from S882: конланги, auxiliary languages, and вымышленные языки as a third kind; why the distinction matters for a fictional world that merely *has* languages.` | kept as §3 table, "third kind" cut | false to the book's numbering (F5); the decision-table form replaces the sentence |
| `**§4 Status within the field** — Tolkien, Klingon and D'ni as specially classed conlangs, and the survey literature behind them.` | split into §7 (the three languages) and §8 (status in the field) | one section holding both became an essay, failing criterion 4 |
| `**§5 Coupling to the world bible** — what to hand to lore-shokunin.` | kept as §9, expanded | the handoff must name the contract and the split of duties (criterion 5) |
| `### Proposed body` and the numbered list framing, and the closing `---` | cut | draft scaffolding from the staged package, not entry content |

Kept without change in substance: the title, the `- topic:` subject, the two-source structure
(one English, one Russian, both read in the original language), the `- scope:` sentence (extended
with "rules on no real-world attribution"), and the naming-systems coupling.

## 6. Out of scope / handoffs

- The registry rows S876/S877, their tier and scope cells, the renumber map, `reports/round-73/*`,
  `claims.json`, `corpus/lessons/round-73.md` and the companion amendment entry
  (`conlang-scholarship.amend-2026-10-23.md`, ids S878/S879/S880) belong to other seats.
- F1 is a freeze question (row scope/tier for S877), not a scribe decision.
- Landing the draft at `corpus/knowledge/linguistics/conlang-scholarship.md` is the executor's step;
  this file is a draft under `.ufo/waves/round-73/w1/drafts/`.
- Checks a landing round should run that this seat did not: the accept-c counter, the Gate-record leg,
  and a second-reader provenance pass.

## 7. Tooling

Nothing installed. `pdftotext`/`pdfinfo` 26.08.0 (Poppler) were already on the host and were used
read-only. No pacman, no uv/npx/cargo, no git writes; no writes outside the draft path and
`/tmp/ScribeEntryBase/`.
