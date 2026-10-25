# CritEntryAmendFinal — attack on `conlang-scholarship.amend-2026-10-23.md`

Seat: critic, round 73 wave 2 (FALSIFY), leaf. Target bytes:
`corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` at lane revision
`0316b8883b4f8d44b8efd720140e7f52f734a102` (clean worktree for tracked files; `git status` showed
only untracked `.ufo/waves/round-73/w2*`). Frozen claims read first:
`reports/round-73/claims.json` (freeze `af65165`). I mutated nothing; every experiment ran in
`/tmp/CritEntryAmendFinal/`; no repo write except this file.

**The lane moved under this seat.** While I worked, a repair commit `7aa8f99` rewrote the amendment
along the lines of this seat's findings (it also committed an earlier state of this report) and HEAD
advanced to `c1b5b47`. Findings F1–F16 below are stated against the assigned revision `0316b88`; the
section **Disposition at the revisions that superseded the target** re-checks each one against
`c1b5b47`. One finding, **F17**, was made after the repair and is **open at `c1b5b47`**: the
Sowers-Wills "no capture" ruling is false — two status-200 captures of the canonical article page
carry the study's own abstract, which says "a semester-long language construction project".

## Verdict

**Verdict on the assigned revision `0316b88`: NEEDS-CUTS — but not cuts alone.** Two BLOCKERs are
false statements in an admitted entry (L50 and L11). L50 is cuttable. L11 is **not**: `gap filled` is
one of the nine mandatory header fields of claim C's ENTRIES leg (`reports/round-73/claims.json`,
claim C leg ENTRIES), so the false clause has to be *replaced*, not deleted. If this wave may only cut
lines, the entry is **REFUSE** on QUALITY 1 (a false provenance statement) and QUALITY 2 (two
uncalibrated framework entries).

**Verdict at the repaired HEAD `c1b5b47`: still NEEDS-CUTS, and one BLOCKER remains open.** The repair
closed F2–F7 and F9–F13 and F15 (see Disposition). Open: **F17** (BLOCKER for claim C's REJECTS leg,
MAJOR for the entry — the Sowers-Wills no-capture ruling is false), **F8** (Piperski uncalibrated),
and the wording residues of F1 and F14.

| # | Sev | Line | Finding |
|---|---|---|---|
| F1 | BLOCKER | 50 | "three categories the article's prose does not list" — the prose lists all three, with examples |
| F2 | BLOCKER | 11 | "It could not say what any taxonomy contains" — the base's §3 is exactly a table of the taxonomy's contents |
| F3 | MAJOR | 36, 38 | restates the base's §3 taxonomy (5/5 class labels shared) while L9 claims it does not |
| F4 | MAJOR | 56 | "Location limit … (to-verify)" — the page is measured (printed 31–32 / PDF 4–5) and the same round's row and evidence assert p. 32 |
| F5 | MAJOR | 3, 28 | S878 locators off by one page: conclusion is p. 465 (not 464), section heading p. 458 (not 457), conclusion range 465–466 |
| F6 | MAJOR | 84, 12 | the 429 provenance claim names no DOI/URL and points at "this round's fetch log", which does not exist |
| F7 | MAJOR | 7 | "the three commands and their 2026-10-25 outputs stand in the round-73 gate record" — no such commands exist in any committed gate record |
| F8 | MAJOR | 40 (and 36–38) | QUALITY 2: Piperski's three-way split and the Шувалова/Сидорова restatement carry no status; Piperski is calibrated nowhere in `corpus/knowledge/` |
| F9 | MAJOR | 66 | "the only description of its format" is contradicted by the entry's own L62 ("The course design") and L64 |
| F10 | MINOR | 22 | "His ruling" upgrades the source's "it may be argued that this division should be seen as a scale" |
| F11 | MINOR | 34 | heading "Three Russian-language typologies" — Peterson's is an English-language podcast taxonomy; the entry's own L10 says "Russian- and English-language" |
| F12 | MINOR | 24, 26 | "the Star Wars films" (source: "the Star Wars universe"); "no formal description" drops "or consistency"; CNL list drops Simple/Special English without "e.g." |
| F13 | MINOR | 66 | "project-based" does not re-locate in the declared extraction (`projectbased`) |
| F14 | MINOR | 74 | "every taxonomy … sorts on purpose before it sorts on form" — Piperski's first group is a thought/function criterion; the article never says any taxonomy sorts on form |
| F15 | MINOR | — | "amendment appends to the base" is one-way: the base carries no pointer to the amendment (the heritage precedent does) |
| F16 | MINOR (cross-land) | 4 | the third support S879 is live-only and its row names no capture URL, so the entry's `recheck:` re-opens a page with no durable carrier |
| F17 | BLOCKER (claim C) / MAJOR (this entry) | 70, 84 (target); 15, 73, 87 (HEAD) | the Sowers-Wills "no capture" ruling is false — two status-200 captures of the canonical article page carry the study's own abstract, which says "a semester-long language construction project" |

What is **sound**: the citation lint passes (0 findings, exit 0), all three `couples:` paths exist,
§4 is method and decides no canon, the quotes at L18/L28/L44/L60/L62/L64/L90 are verbatim and within
the 25-word cap, "semester-long" really is absent (`grep -ci semester` → 0), "автоконланги" really
is absent (0) while «авторскими языками» is present (1), the case-mangled served heading at L4 is
verbatim in the served HTML, the S879 capture-shell claim in the row is consistent with the lesson,
and the three S-ids each sit alone on their lines.

## Probes (fetch hygiene)

All requests: browser-shaped UA
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
and, for the one walled page, plain `curl/8.7.1`; `automation: none`, curl 8.23.0,
pdftotext/pdfinfo 26.08.0, downloads in `/tmp/CritEntryAmendFinal/`. The three primary sources and the
archive requests answered 200 under the browser UA. The one wall met is the live Cambridge page: 429,
1,302 B under both UAs (`<title>429 Too many automated requests from this network.</title>`), so the
live page is genuinely refused and the archived copy is the ordinary route (QUALITY 10), not a bypass.
No challenge was solved, no browser automation was used, no install was made, pacman not run.

| request | status | bytes | hash |
|---|---|---|---|
| `journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` | 200 | 959,171 | sha256 `9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c` (identical to `reports/round-73/evidence/S878.txt`) |
| `sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` | 200 | 193,610 | sha256 `26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535` (identical to evidence S880) |
| `cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` | 200 | 97,656 | sha256 `6f1def00ebc3e2873ffe90440905f719c00ca5b96637334c258b8c9ee137cfff` (evidence recorded 97,622 B / `709e186b…`: 34 B live drift, no span affected) |
| `cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf` | 200 | 630,227 | sha256 `cc9a91c5149ada2868fc94f93c39e61c62812466c8414ddff5643dd254c0643f`, 7 pages (matches the 630,227 B publisher PDF recorded by `ScoutS893`) |
| `doi.org/10.1017/cnj.2024.21` | 302 | 0 | redirects to `https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article` |
| Wayback CDX exact on the canonical article page (F17) | 200 | 1,104 | sha256 `98036ca3b90ee266bba67e6830e3f42cbc289abbe06fa32c33f786c868b6b371`; two status-200 captures |
| `web.archive.org/web/20241106195515id_/<canonical article page>` | 200 | 1,030,239 | sha256 `dc061a30bae1c2e207a0494fb6cdbfd1c94b51498c690d78aa26babdd1c35a7e` |
| live canonical article page (browser UA) | 429 | 1,302 | matches the Gate row's live reading |
| live canonical article page (`curl/8.7.1`) | 429 | 1,302 | `<title>429 Too many automated requests from this network.</title>` — wall persists under both UAs |
| live identifier page `.../product/identifier/S0008413124000215/type/journal_article` (browser UA) | 429 | — | same wall; no redirect served |

The PDF leg matters: it is the layout that carries printed page numbers, and the round's own scout
recorded fetching it. The amendment's "the cyberleninka text is served as extracted HTML with no page
markers" is true of the HTML and false as a reason for `(to-verify)` — see F4.

---

## F1 — BLOCKER — line 50: the prose does list all three categories

Claim (L50): *"The comparison table's Peterson column carries three categories the article's prose
does not list — parody, sign and graphic languages — so the taxonomy's full extent is a table entry,
not an argued class (S879)."*

The prose lists all three, on printed p. 30 (PDF p. 3), with examples:

```
$ cd /tmp/CritEntryAmendFinal
$ for p in 3 6; do echo "-- pdf page $p --"; pdftotext -enc UTF-8 -f $p -l $p S879.pdf - \
    | grep -n -E "пародийных|жестовые|графические|jokelangs|sign languages|graphic Languages"; done
-- pdf page 3 --
57:Yešqūr3 можно отнести к группе пародийных языков (parody languages or jokelangs), поскольку он
64:Помимо таких языков, Питерсон предлагает выделять языки жестовые (sign languages or manual
65:languages) и графические (graphic languages), т. е.
-- pdf page 6 --
51:(jokelangs), sign languages
```

PDF p. 3 is printed p. 30 (page map below, F4). So: parody is in the prose with its example
(Yešqūr, "в высшей степени бюрократизированный язык"); sign and graphic are in the prose as groups
Peterson "предлагает выделять", with the rikchik example in the next sentence. The sentence is false
under every reading of "prose" — the three appear outside the six-category bullet list, but the
sentence says the *prose* does not list them, and it draws the further inference that they are "not
an argued class", which the prose's own Yešqūr and rikchik discussion contradicts.

Smallest safe correction: cut L50. Nothing else in §2 depends on it (L52 and §4 do not use it).

## F2 — BLOCKER — line 11: the base does say what a taxonomy contains

Claim (L11): *"the base could say a taxonomy of artificial languages exists and that peer-reviewed
venues exist. It could not say what any taxonomy contains, how the taxonomies compare, or what a
construction exercise actually consisted of."*

The base's §3 is a six-row table of the taxonomy's contents, plus a survey of four competing
classifications with their criteria:

```
$ sed -n '/^## §3/,/^## §4/p' corpus/knowledge/linguistics/conlang-scholarship.md | sed -n '1,12p'
## §3 A taxonomy to file a world's languages into
The book adopts one classification out of several it surveys, and states that neither linguists nor
conlangers share a terminology for the classes (S877).
| Class, in the book's numbering (pp. 11–12) | What the book means | Design question it forces |
| 1. Auxlangs | international auxiliary languages: Esperanto, Ido, Lojban | ... |
| 2.1 Artlangs | languages invented by authors of fiction, film and games | ... |
| 2.1.1 | artlangs that left their fictional world: Tolkien's, Klingon, D'ni | ... |
| 2.1.2 | artlangs that function, or are only mentioned, inside the work | ... |
| 2.2 Personal, or авторские, languages | invented by individuals or groups for their own pleasure ... | ... |
$ grep -n "It reports several competing classifications" corpus/knowledge/linguistics/conlang-scholarship.md
50:It reports several competing classifications, with their criteria, without adopting them: structure
and purpose (Rosenfelder), a priori versus a posteriori (Harrison, after Couturat and Leau), potential
use and potential users (Capuzzo), and a composite letter-plus-SVO index ... (S877).
```

(cells and line tails elided for width; the elisions are marked "…". The full §3 table has six class
rows and each "What the book means" cell is filled; the survey line ends "… from a University of Hong
Kong page (S877).")

"It could not say what **any** taxonomy contains" is falsified by the base's own table. The other two
clauses are true (the base compares no taxonomies and reports no construction exercise). The gap the
amendment actually fills is narrower: *a comparison's verdict between taxonomies*, *the a priori/a
posteriori scale argument*, and *one course's design as a companion article reports it*.

Smallest safe correction: replace the second sentence of L11 with the true, narrower gap — e.g.
"the base reports one taxonomy's contents and four classifications' criteria, but compares none of
them, records no scale argument, and reports no construction exercise." A cut is not available:
`gap filled` is a mandatory header field (claim C, ENTRIES leg).

## F3 — MAJOR — lines 36 and 38 restate the base's §3

The header says (L9) "it does not restate the base's topic, gap, or §2–§5". §2's first two
paragraphs re-present base §3's taxonomy, class by class:

```
$ for k in "1. Auxlangs" "2.1 Artlangs" "2.1.1" "2.1.2" "2.2"; do
    printf "%s base=%s amend=%s\n" "$k" \
      "$(grep -c -F "$k" corpus/knowledge/linguistics/conlang-scholarship.md)" \
      "$(grep -c -F "$k" corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md)"; done
1. Auxlangs base=1 amend=1
2.1 Artlangs base=1 amend=1
2.1.1 base=1 amend=1
2.1.2 base=1 amend=1
2.2 base=3 amend=3
```

5/5 class labels shared; the same two examples (Tolkien, Klingon) in 2.1.1; the same "Personal /
авторские" cell in 2.2. The only new elements are the Э'П/Myst example and Arëndron, plus the review
article's wording. The new content of §2 is the *comparison* (L40–L56), not the taxonomy.

Smallest safe correction: compress L36/L38 to one sentence that names what the review adds (Э'П,
Arëndron, the авторские naming as the review quotes it) and points at base §3 for the classes; or
amend L9/L14 so they no longer claim non-restatement.

## F4 — MAJOR — line 56: the `(to-verify)` page is measured, and the row asserts it

Claim (L56): *"the cyberleninka text is served as extracted HTML with no page markers, so the page for
items 1–2.2 within the article's pp. 28–34 is (to-verify)"*.

The publisher PDF has printed page numbers and was fetched by this round (`ScoutS893`: "630 227 bytes
PDF"):

```
$ for p in $(seq 1 7); do printf "pdf p%s printed %s %s\n" "$p" \
    "$(pdftotext -enc UTF-8 -f $p -l $p S879.pdf - | grep -xE '[0-9]{2}' | tail -1)" \
    "$(pdftotext -enc UTF-8 -f $p -l $p S879.pdf - | grep -oE '1\. Auxlangs|2\.2\. Personal languages' | tr '\n' ' ')"; done
pdf p1 printed 28 
pdf p2 printed 29 
pdf p3 printed 30 
pdf p4 printed 31 1. Auxlangs 
pdf p5 printed 32 2.2. Personal languages 
pdf p6 printed 33 
pdf p7 printed 34 
```

Items 1–2.2 sit on printed pp. 31–32 = PDF pp. 4–5. The registry row and the evidence capture this
same round landed assert exactly that:

```
$ grep -n "printed p. 32" corpus/SOURCES.md reports/round-73/evidence/S879.txt corpus/lessons/round-73.md
corpus/SOURCES.md:834: ... item 2.2 (PDF p. 5 = printed p. 32) ...
reports/round-73/evidence/S879.txt:9: locator: comparison section ..., item 2.2 (printed p. 32)
corpus/lessons/round-73.md:21: ... item 2.2 (PDF p. 5 = printed p. 32) ...
```

So the entry marks `(to-verify)` what the round measured three times. The charitable reading ("if you
only have the HTML") does not survive the sentence's own conclusion, and the entry's `- source:` line
(L4) names only the HTML, so the PDF URL a re-opener needs is not in the entry either.

Smallest safe correction: cut the `(to-verify)` clause; write "items 1–2.2 = printed pp. 31–32 (PDF
pp. 4–5)"; add the `/pdf` URL to the S879 source line or to the row's anchor so "PDF p. 5" resolves.

## F5 — MAJOR — lines 3 and 28: S878 page locators are off by one

```
$ for p in 1 4 11 12; do printf "pdf p%s printed %s %s\n" "$p" \
    "$(pdftotext -enc UTF-8 -f $p -l $p S878.pdf - | grep -xE '[0-9]{3}' | tail -1)" \
    "$(pdftotext -enc UTF-8 -f $p -l $p S878.pdf - | grep -oE 'Correlation between types|Conclusion|challenge the integrity|the author examines the existing classifications' | tr '\n' ' ')"; done
pdf p1 printed 455 the author examines the existing classifications 
pdf p4 printed 458 Correlation between types 
pdf p11 printed 465 Conclusion challenge the integrity 
pdf p12 printed 466 
```

- L28: `"challenge the integrity of the seemingly well-established dichotomies ..." — 18 words,
  Conclusion, p. 464 (S878)` → the sentence is on **p. 465**.
- L3: `§"Correlation between types ...", pp. 457–459` → the heading is on **p. 458**; the cited spans
  are pp. 458–459; p. 457 carries nothing the entry uses.
- L3: `Conclusion, pp. 464–465` → the Conclusion runs **465–466**.

The 18-word count and the abstract locator (p. 455, 24 words) are correct.

Smallest safe correction: `p. 465`; `pp. 458–459`; `pp. 465–466`.

## F6 — MAJOR — lines 84 and 12: the 429 claim has no resolvable source

```
$ find reports/round-73 -iname '*fetch*' | wc -l
0
$ grep -c "10\.1017\|doi\.org" corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
0
$ grep -rn "fetch log" --include='*.md' --include='*.json' --include='*.txt' . | grep -v '^./.ufo' | cut -c1-200
./corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md:84:The publisher's abstract of the study was not opened: its DOI answered HTTP 429 to both a browser-shaped and a plain client on
```

(the line continues past the 200-char cut; its tail is "(this round's fetch log, not a source row).")

The claim "its DOI answered HTTP 429 to both a browser-shaped and a plain client" is consistent with
the lesson Gate row (`corpus/lessons/round-73.md:47`, which names `https://doi.org/10.1017/cnj.2024.21`,
1302 B under each UA, `automation: none`), but the entry names neither the DOI nor the artifact that
carries the record. "this round's fetch log" is not a file that exists anywhere in the lane. Under
QUALITY 1 the claim is not checkable from the entry.

Smallest safe correction: name the DOI and point at `corpus/lessons/round-73.md:47` (the S894 row),
or drop the pointer clause. (The Gate row itself does not record the 429's attempts/gaps as QUALITY 22
asks; that is a claim-C Gate defect, not this entry's.)

## F7 — MAJOR — line 7: the recheck's receipt claim is false

Claim (L7): *"one grep per row, each prints 1; the three commands and their 2026-10-25 outputs stand
in the round-73 gate record"*.

```
$ grep -c "grep -" corpus/lessons/round-73.md
1
$ grep -n "grep -" corpus/lessons/round-73.md | cut -c1-90
117:Sweep for further mistakes in rounds 70–72 lessons: `grep -c '^| .* | none |' corpus
$ grep -c "grep" reports/round-73/evidence/*.txt | tr '\n' ' '
reports/round-73/evidence/S876.txt:0 reports/round-73/evidence/S877.txt:0 reports/round-73/evidence/S878.txt:0 reports/round-73/evidence/S879.txt:0 reports/round-73/evidence/S880.txt:0 
```

(the single lesson hit is line 117's unrelated sweep command, not a recheck command.)

The committed Gate section carries a table (URL, date, quote, locator, evidence file, verdict) and
the evidence captures carry `quote-found-verbatim: yes` — no commands, no outputs. The three commands
exist only in untracked wave-1 seat reports (`.ufo/waves/round-73/w1/ScoutS892.md:94`,
`ScoutS893.md:101`, `ScoutS901.md:49`), which are not "the round-73 gate record" and are not
committed. The lesson's own note (`corpus/lessons/round-73.md:90`) says this prose was moved out of
the row *into the entry*, so the entry is now the only carrier of a pointer that resolves to nothing.

Smallest safe correction: replace the clause with the artifact that does exist ("the recheck greps
and their outputs are in the wave-1 scout reports `ScoutS892/893/901`") or drop it.

## F8 — MAJOR — QUALITY 2: two framework entries carry no status

```
$ grep -c "^Calibration:" corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
2
$ grep -rln "Пиперски\|Piperski" corpus/knowledge/
corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
```

(one file only: Piperski is calibrated nowhere in `corpus/knowledge/`.)

Two `Calibration:` lines cover Novikov's scale reading (L30) and the comparison/Peterson (L48).
Uncalibrated framework entries: Piperski's three-way split (L40, repeated at L54) and the
Шувалова/Сидорова taxonomy (L36–L38). The Шувалова/Сидорова status does exist in base §1, but the
amendment does not point to it; Piperski's exists nowhere in the corpus. The asymmetry is the tell:
the entry calibrates Peterson's podcast taxonomy as "a practitioner framework … rather than a
published taxonomy" (L48) but says nothing about the source of Piperski's split, which the review
article cites as a trade book — `Пиперски А. Ч. Конструирование языков: От эсперанто до
дотракийского. М.: Альпина нон-фикшн, 2017` (S879, reference 10; the article itself calls it "Более
традиционный способ классификации"). QUALITY 2 requires the status and the reason for every
framework entry.

Smallest safe correction: add one status clause to L40 (e.g. "a trade-book taxonomy reported by the
review, not a peer-reviewed classification") and one to L36 ("status as base §1: published descriptive
taxonomy, terminology contested").

## F9 — MAJOR — line 66: "the only description of its format" is contradicted by L62 and L64

The companion article gives three descriptions of the course in the same section and page:
"examines the use of constructed languages as **an active learning approach in a project-based
phonology course**"; "**In the course, examples of phonological systems in natural languages and
constructed languages were presented along with instruction in language universals and typology**";
"a **multi-part, creative project** can be part of a course even at the introductory level"
(`reports/round-73/evidence/S880.txt`, context window; all three are quoted by the entry itself at
L62 and L64). L62 labels the second one "The course design". So L66's "which is the only description
of its format the companion article gives" is false against the entry's own two preceding sentences.

Smallest safe correction: cut the trailing clause ("which is the only description …"), or narrow it
to "the only description of its *pedagogical format*" and say what the other two describe.

## F10 — MINOR — line 22: "His ruling" overstates a hedge

```
$ pdftotext -enc UTF-8 -f 4 -l 4 S878.pdf - | grep -n "it may be argued"
35:it may be argued that this division should be seen as a scale rather than a binary
```

The source sentence is impersonal and hedged ("However, it may be argued that this division should be
seen as a scale rather than a binary system since all a priori languages are bound to be influenced by
their creator's linguistic worldview"). The entry's "His ruling on it" turns a proposal into a
verdict, and contradicts the entry's own L30 ("a contested refinement, not a replacement"). The quote
itself is verbatim; only the framing overstates.

Smallest safe correction: "He argues it:" or "The article proposes:".

## F11 — MINOR — line 34: the section heading mislabels the third taxonomy

`## 2. Three Russian-language typologies, and one reviewer's comparison` — the section's third
taxonomy is Peterson's, delivered on a YouTube podcast in English ("В 2015 году Д. Питерсон
опубликовал на своем YouTube-канале первый эпизод подкаста «Искусство создания языков»", S879
printed pp. 29–30, the sentence spanning the page break). The entry's own topic line (L10) correctly says "purpose-first typologies in
Russian- and English-language scholarship".

Smallest safe correction: "## 2. Three typologies in a Russian-language review".

## F12 — MINOR — lines 24 and 26: source drift on the examples

- L26 "the Star Wars films use 68 languages" — source: "the Star Wars universe features 68 languages,
  yet none of them have any formal description or consistency" (S878, printed p. 459). "films"
  narrows "universe"; the dropped "or consistency" narrows the negative.
- L24 "the controlled natural languages — Basic English, Globish, E-Prime" — the source's CNL
  examples are "Simple English, Basic English, Special English, Globish, etc.", with E-Prime named
  separately as a "thinking device". The three-item list reads as exhaustive without "e.g.".

Smallest safe correction: "universe"; "e.g. Basic English, Globish, E-Prime".

## F13 — MINOR — line 66: the hyphenated quote does not re-locate in the declared extraction

```
$ grep -c "projectbased" S880.txt
1
$ grep -c "project-based" S880.txt
0
```

The PDF sets "project-\nbased" across a line break; `pdftotext` (the extraction the evidence file
declares) yields `projectbased`. A re-opener running the declared extraction will not find the quoted
string as printed.

Smallest safe correction: quote the extract's form or mark the line-break hyphen.

## F14 — MINOR — line 74: "every taxonomy … sorts on purpose before it sorts on form"

Piperski's first group is not a purpose class: "– языки философские, или логические (энджланги):
данная категория выделяется в тесной связи с гипотезой лингвистической относительности" (S879
printed p. 32), with loglan/lojban as instances. The article never says any of the three taxonomies
sorts on form. The method line's premise is therefore an overgeneralization of the article's
Peterson-specific "В зависимости от цели создания".

Smallest safe correction: "the taxonomies the review compares sort on purpose or function, not on
structure".

## F15 — MINOR — the append is one-way

```
$ grep -c "amend" corpus/knowledge/linguistics/conlang-scholarship.md
0
$ grep -n "amend" corpus/knowledge/culture-material/heritage-taxonomy-models.md
76:four to five (S874, and see `heritage-taxonomy-models.amend-2026-10-24-r13.md`).
```

The amendment names the base; the base names nothing. The lane's own precedent for an amendment
(the heritage entry) carries the pointer in the canonical entry's body. So "an amendment to the
conlang-scholarship entry" (L14) is true of intent but not of the landed relationship: a reader of
the base never learns the amendment exists (only `corpus/README.md:771` lists it).

Smallest safe correction: add the pointer to the base (one line, or the `couples:` line).

## F16 — MINOR (cross-land) — the third support has no durable carrier

The row S879 (`corpus/SOURCES.md:834`) is live-only: "the one Wayback capture (20261025222414, made
this round) is a 23443-byte shell that does not carry the span and is not an anchor", and it names no
capture URL; `grep -rn 20261025222414` finds the id only in the row, the lesson and `claims.json`, never
a URL. QUALITY 16 asks each row to list its live URL **followed by an archived capture of that same
page**; QUALITY 18 permits a live-only row only when the live URL serves the quote (it does). The two
criteria collide here and the round resolved it toward 18. For this entry the consequence is narrow:
its `recheck:` tells a future re-opener to re-open a page whose only carrier is live.

Smallest safe correction (claim C's, not the entry's): record the capture URL in the row's durability
cell with its shell status, so the "no working capture" ruling is reproducible.

## F17 — BLOCKER for claim C / MAJOR for this entry: the Sowers-Wills "no capture" ruling is false

This is the finding that outlives the repair commit (see Disposition below). The round refused the
Sowers-Wills article (staged S894) on a durability ground that its own Quarantine row contradicts and
that my probe falsifies.

The DOI resolves to Cambridge's identifier page; the archive's replay of that identifier URL resolves
to the canonical article page (same title and author), which is what CDX captured twice:

```
$ curl -sS -o /dev/null -w 'doi status=%{http_code} redirect=%{redirect_url}\n' -A "<browser UA>" https://doi.org/10.1017/cnj.2024.21
doi status=302 redirect=https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article
```

CDX exact query on that canonical page (the QUALITY 21 duty: follow the live URL's own canonical /
redirect target and query THAT slug):

```
$ curl -sS -A "<browser UA>" "https://web.archive.org/cdx/search/cdx?url=https://www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59&output=json&filter=statuscode:200"
[["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
 ["org,cambridge)/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649f8bedbf579512088f614eb2794b59","20241106195515",...,"text/html","200","PHYINBAF4UFJYGIVRKM4FAW772BN5X47","139256"],
 ["...649f8bed...","20241107004043",...,"text/html","200","QE7UHKBANTDZ55WDAIZUDZ5O5MYXESKH","139614"]]
```

(the `original` field is elided as `...` in both rows — it is the same canonical URL given in the
query; `statuscode` 200, `mimetype` text/html, distinct digests and lengths are as printed.)

Replay of the first capture (`id_`), browser UA, `automation: none`:

```
status=200 bytes=1030239 final=https://web.archive.org/web/20241106195515id_/https://www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59
sha256 dc061a30bae1c2e207a0494fb6cdbfd1c94b51498c690d78aa26babdd1c35a7e
```

(The replay of the second timestamp redirects to the first; CDX still lists two distinct captures.)

Body text of the captured page (head/scripts stripped, tags removed — body, not a meta attribute):

```
Abstract This paper reflects on a project-based curriculum employing constructed languages to teach
linguistics, with a focus on phonology. In a special topics linguistics course, nine students were led
through the construction of a language. ... active engagement with a semester-long language construction
project endowed these students with the practical motivation to understand (1) what phonology is, (2)
how phonological rules work, and (3) why rules surface in the first place. ...
... Initially, 10 students enrolled in the course, one of whom withdrew early on. Among the nine
students who completed the course ...
... Phonology from the Inside Out: Constructed Language as a Pedagogical Tool / Published online by
Cambridge University Press: 30 October 2024 / Sara Sowers-Wills
```

The live canonical page is indeed walled under both UAs — the Gate's live reading is correct:

```
live canonical (browser UA)   status=429 bytes=1302
live canonical (curl/8.7.1)   status=429 bytes=1302  <title>429 Too many automated requests from this network.</title>
```

But the lane already knew this, in the same lesson file:

```
$ sed -n '101p' corpus/lessons/round-73.md
| S812 doi.org/10.1017/cnj.2024.21 | S894 | PRESENT in the Crossref abstract record and in two
status-200 Wayback captures of the canonical article page (20241106195515, 20241107004043); live
publisher page HTTP 429 | verifiable, not fabrication; the row is not adopted (outside the declared set) |
```

against the Gate row's:

```
$ sed -n '47p' corpus/lessons/round-73.md
| ... | S894 | status: ... the 429 is a rate limit read per QUALITY 16, not UA-gating; no Wayback
capture of the same page (CDX 0 for the DOI, the cambridge identifier URL and the slug prefix); ...
```

Two committed rulings on the same DOI, one of them false. My probe confirms the Quarantine side: the
Gate's CDX probes named the DOI, the `product/identifier/` page and the slug prefix — none of them the
canonical `/core/journals/.../article/.../649F8BED...` page, which is what the DOI's redirect chain
lands on and what the archive captured twice with status 200.

Why it matters, in order:

1. **Claim C's REJECTS leg.** S894 is named as refused on an unreachability ground that is false.
   Under QUALITY 18 the row was adoptable (live URL = the canonical page; capture = 20241106195515,
   status 200; anchor = the abstract's body text), and QUALITY 10 says an ordinary archive copy is not
   a bypass. The refusal may still stand on the round's own F1 ground ("outside the declared set"),
   but not on "no capture".
2. **This entry's §5.** Target L84 presents the 429 as the reason the publisher's abstract "was not
   opened". The 429 is real, but it is not the operative constraint: an ordinary capture carries the
   abstract and the article body.
3. **This entry's §3.** Target L70 marks "semester-long" and "what it claims the project teaches that
   lectures do not" as `(to-verify)` because "both need the article's own text, which was not opened
   this round". The captured abstract answers the first outright ("a semester-long language construction
   project") and the second in the same sentence (concepts "to that attained in a traditional
   introductory course"). So the entry's `(to-verify)` is resolvable now, by ordinary means.
4. **The "useful negative" framing.** L88 says "Two staged elements were dropped rather than repaired.
   The 'semester-long' duration is absent from the companion article's nine pages (S880)." The token is
   absent from the *companion*; it is present in the *study's own* abstract. Dropping it was not
   required by the evidence, only by the companion's scope.

Smallest safe correction: (a) correct the lesson Gate row's no-capture clause to name the canonical
URL and the two captures (QUALITY 21), and restate the reject on the declared-set ground; (b) in the
entry, either adopt the row and cite the study's own abstract for the semester-long project and the
nine-student cohort, or state plainly that the abstract is reachable through the 2024-11-06 capture and
that this round chose not to adopt it — and stop presenting the 429 as the reason.

---

## Disposition at the revisions that superseded the target (for the main agent)

The lane moved while this seat ran. My assignment named `0316b88`; by the time I finished, HEAD was
`c1b5b47`, and a repair commit `7aa8f99` ("wave-2 falsify repairs — entry content fixes (per-sentence
fact-check) …") had landed that rewrote the amendment along the lines of this seat's findings and
committed an earlier state of this report. I re-checked the repaired bytes (`git show
c1b5b47:corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md`) so the main agent is not
left chasing closed items. **Findings against the assigned revision `0316b88` remain the record below;
this table is the disposition at `c1b5b47`.**

| finding | at `c1b5b47` | evidence |
|---|---|---|
| F2 gap filled | **closed** | L14 now reads "It reports one monograph's taxonomy but could not say how a later review restates and compares taxonomies, …" |
| F3 restatement | **closed** | L39 now points to base §3 ("Шувалова and Сидорова's classes are in the base (§3)") |
| F4 location | **closed** | L59 now gives printed pp. 31–32 (PDF pp. 4–5) and the `/pdf` URL |
| F5 S878 pages | **closed** | header now `pp. 458–460` / `pp. 465–466`; L31 `p. 465` |
| F6 429 provenance | **closed** | L15 now names `https://api.crossref.org/works/10.1017/cnj.2024.21` and the lesson Gate |
| F7 recheck | **closed** | L8–L11 now carry the three commands inline, each printing 1 on the bytes I hold |
| F9 "only description" | **closed** | L69 now says "the companion article's one-line characterization of the course's mode" |
| F10 "His ruling" | **closed** | L25 now "He argues, hedged as 'it may be argued that'" |
| F11 heading | **closed** | L37 "Three typologies in a Russian-language review" |
| F12 universe / e.g. | **closed** | L29 "Star Wars universe … none with any formal description or consistency"; L27 "e.g. Basic English, …" |
| F13 hyphen | **closed** | L69 notes "the PDF text breaks the hyphenated word across a line" |
| F15 one-way append | **closed** | base `couples:` now names the amendment (base L11); amendment adds a closing line |
| F1 table-only claim | **open (wording)** | L53: "the prose bullet-list gives six and adds parody languages (instance: Yesqur) plus a mention of gesture- and graphic-symbol-based constructed languages …; only the three category names are table-only". The first half says the prose names two of them; "table-only" then contradicts it. The prose gives all three names (printed p. 30). Reword to "only the table lists all nine as one enumerated set" |
| F8 calibration | **open** | L43 Piperski still has no status; the Шувалова/Сидорова status is reachable only via the pointer to base §3, while the status itself sits in base §1 |
| F14 purpose claim | **open (wording)** | L77 "purpose-defined top-level classes (auxlang, artlang, logical)" — the logical class is tied to the linguistic-relativity hypothesis (S879 p. 32), not to purpose |
| F17 Sowers-Wills capture | **open, and worse at HEAD** | the repaired §5 (L87) and sources line (L15) still present the 429 as the reason; the canonical-page capture (F17) is not mentioned, and the Gate row's no-capture clause is still false |

The two items that need bytes, not wording, are F17 (a Gate-row correction, plus a decision on whether
to adopt the row) and F8 (a status clause for Piperski). The rest is sentence-level.

---

## What I could NOT check

- **Whether the round itself fetched the Crossref abstract record.** The Gate row says it is
  "reachable"; the entry says the publisher's abstract "was not opened". No fetch log exists to settle
  it. What I did establish is that the study's own abstract is reachable by ordinary means (F17);
  whether the round touched the Crossref record specifically remains unverified.
- **The register row S812's own anchor quote against the capture.** The Quarantine table's "S812" is a
  register-namespace id; the lane's `SOURCES.md` S812 is a different document (Galen), so I could not
  compare the register's quote with the captured body. I verified only that the captured canonical page
  is the article and carries its abstract.
- **The S879 Save-Page-Now capture's body** (`20261025222414`): I did not probe it, so the row's
  "23443-byte shell that does not carry the span" is accepted as reported, not re-measured.
- **QUALITY 7 separability**: no round-73 separability manifest exists (`ls reports/round-73/*manifest*`
  → none; no `separability-manifest-v1` anywhere under `reports/` or `.ufo/waves/round-73/`), so the
  criterion's declared check could not be run at all this round. By inspection the amendment cites only
  claim C's own rows (S878–S880) and names no Ca-exported path, so separability holds on the bytes I read.
- **QUALITY 13/16 retry budgets and paired controls** for the round's live-fetch legs: I audited only
  the amendment's own claims, not the round's declared budget and its two controls.
- **The full S878 argument beyond the cited spans and their immediate context** (I read the abstract,
  §Correlation, the Eurocentrism section and the conclusion; not the whole 13 pages line by line).
- **S876/S877 base anchors and the archive captures** of S878/S880: out of scope for this seat and not
  re-opened.
- **The round counters** (`accept-c.py`, `accept-ca.py`): not my target, not run.

## Axis impact

Claim **C** (coverage/assimilation): the entry's *sourced content* survives; its *provenance frame*
does not. F1 and F2 are false statements in an admitted entry, F4/F5/F6/F7 are locator/pointer
defects, F3 falsifies the entry's own non-restatement claim, F8 is an admission-bar failure
(QUALITY 2). The smallest safe repair is local (three lines changed, four locators fixed, two status
clauses added) — no new sources, no new rows, no new fetch.

**F17 is different in kind and is the one item that moves an axis.** It falsifies claim C's
durability ground for refusing S894 (QUALITY 21: the canonical slug was never queried) and it shows
that the study's own abstract — with the "semester-long" duration the entry marks `(to-verify)` — was
reachable by ordinary means this round. The choice is the round's: correct the Gate row and keep the
refusal on the declared-set ground, or adopt the row and let the entry cite the primary. Either way
the amendment's §5 must stop presenting the 429 as the reason. Claim **Ca** is untouched by this seat.
