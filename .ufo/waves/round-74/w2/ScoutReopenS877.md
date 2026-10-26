# ScoutReopenS877 — independent re-open of lane row S877 (round 74 wave 2)

Seat: ScoutReopenS877 (leaf, read-only). Lane main at fetch: `1d7add3f7b9eaf6f3349c56c36f6d06325d74236`; operative freeze F3 `00c408a0…`; claim C lands `c4bf61a8…`.
All reads were `git show main:<path>` or fetches into `/tmp/ScoutReopenS877/`. Nothing in the lane or fleet was written except this file.
I did not run the counters: the assignment is the S877 attack, not the counters.

## Verdict (one line)
The Gate admit of S877 survives: the quote is on the page, the bytes and hash are unchanged, and tier B is right. The attack finds defects in the landed entry `worldbuilding-setting-practice.md` (four S877-cited sentences plus the table/coupling lines that lean on them) and in two statements in the Gate notes. There are 0 BLOCKERs, 1 HIGH (scope), 3 MEDIUM, 6 LOW.

## 1. Re-fetch (required lines)

```
$ curl -sS -L --compressed --connect-timeout 20 --max-time 90 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -o conlangs.pdf -D headers.txt -w "%{http_code} %{url_effective} %{size_download}\n" http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
200 http://www.philol.msu.ru/~sidorova/files/conlangs.pdf 1055723
(date -u: Mon 26 Oct 2026 02:00:34 UTC = 2026-10-25 23:00 America/Sao_Paulo)
Last-Modified: Sun, 15 Jul 2007 15:26:48 GMT   ETag: "3890039-101beb-f8fe9e00"   Content-Type: application/pdf
$ sha256sum conlangs.pdf
e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9  conlangs.pdf
```
- UA: the browser-shaped Chrome/130 string above. No wall, 1 attempt.
- `pdfinfo`: Pages 185, Producer "Acrobat Distiller 5.0…", CreationDate 2007-07-15, File size 1055723 bytes.
- Hash equality: **YES**, the live bytes equal the evidence file (`bytes: 1055723`, `sha256: e512a20d…595a9`), the row anchor (HTTP 200, 1055723 bytes) and the entry source line. Nothing moved. The server `ETag` and `Last-Modified` are the 2007 values, so the file is static.
- Wayback carrier in the row:
  - `curl -A <same UA> "https://web.archive.org/web/20260208005339id_/https://www.philol.msu.ru/~sidorova/files/conlangs.pdf"` → `200 … 1055723`, sha256 `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9`. This is byte-identical to live.
  - The CDX probe is `…/cdx/search/cdx?url=philol.msu.ru/~sidorova/files/conlangs.pdf&output=txt`. It returns the 20260208005339 row (`https://www.philol.msu.ru/…`, 200, digest `3WWHFZNWQ…`, length 866237).
  - Positive control `url=example.com&limit=1` → `com,example)/ 20020120142510 …`.
  - The capture's embedded original is `https://www.…` while the live URL is `http://www.…`; both normalise to the same urlkey, so it is the same page (QUALITY 18 shape).

## 2. Gate quote
- Text extraction: `pdftotext -enc UTF-8 conlangs.pdf out.txt`, **no `-layout`** (poppler 26.08.0): 494888 chars, 186 form-feed-split pages (the last is empty).
- Quote «Язык – главный инструмент построения вымышленных миров» (7 tokens, 54 chars, en dash U+2013 as on the page):
  - Verbatim in the raw extract: **NO**. A line break falls between «главный» and «инструмент» (`…эскапизма. Язык – главный⏎инструмент построения…`). The evidence file records the same: `quote-found-verbatim: no`.
  - After whitespace fold: **YES**, exactly 1 occurrence in the whole book (`ft.count == 1`).
  - Location: PDF page 7 = **printed p. 7**. The page-number offset is 0: the printed number is extracted on p. 4 (`…индиви4`), p. 5, p. 6 (top), p. 9, p. 35, p. 139 and p. 140, so pp. 35/36/139/140 map 1:1. The p. 7 footer does not extract in plain mode; the TOC says Предисловие starts p. 4.
  - Context: the paragraph at the end of the preface, after «…проявление эскапизма.».
  - With `-layout` (a cross-check only) the same words read `Язык – главный⏎инструмент построения…`, also split by a line break.
- The evidence file's window (line 33, 4098 chars, 7558 UTF-8 bytes) contains the quote at fold offset 2019. That matches `before=2019`, and `4098−2019−54 = 2025` matches `after=2025`. `sha256(window line)` = `f63d6485cfb7e55036c7f20db66d725a36fcd753e535ad51db7a0d1600570a27`, which **equals** the recorded `window-sha256`, and `window-bytes: 7558` matches. The window starts «вления в них могут появляться…», which is p. 6 text. The stored line is long, so some viewers truncate it with «…»; the line itself is intact.
- Evidence counters I could not reproduce: `extract: 494887 chars` (mine: 494888 from stdout and from file) and `visible-chars: 492810` (mine: 492870 after NFKC fold and whitespace collapse, 492869 stripped, 425943 non-space). This is poppler-version or definition noise; the quote, window sha and offsets are unaffected. LOW (F9).

## 3. Row S877 against the page (corpus/SOURCES.md:832 at main; cells 0–10)

| cell | content | verdict |
|---|---|---|
| source | Сидорова, Шувалова, «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 2006, 184 с., ISBN 5-98789-005-5, complete typeset text of the monograph | PDF p. 2 carries exactly that imprint, `С 34 Интернет-лингвистика: вымышленные языки. М., «1989.ру», 2006, с.184` and `ISBN 5-98789-005-5` ✔. The PDF has 185 pages; the last is only the number «185», and p. 184 is the colophon. The scope cell says "185-page", the entry says "184-page"; both are defensible. |
| kind / tier | book / **B** | **AGREE with B** (see Tier). |
| scope | "Tier B for the book's own framing: classification of artificial languages (конланги), the vocabulary separating вымышленные языки from вспомогательные… Tolkien, Klingon, D'ni… survey of the literature" | In scope: p. 10–12 classification and terminology, pp. 22–26 Tolkien/Klingon/D'ni, pp. 27–29 survey ✔. **Not in scope: world-building, the language–world link, the science-fiction premise rule, the communication function (see F1).** |
| anchor | Глава 1, printed p. 10 «Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.» | Span is on printed p. 10 ✔. **But it is Harrison's FAQ quoted by the book** (see F5). |
| teaches | Russian scholarly frame; class system; "volume rule"; dated survey | volume rule p. 12–13 ✔; survey ✔. |
| used-by | `…conlang-scholarship.md, …worldbuilding-setting-practice.md` | `git diff` of the row, base f7104cb vs main: only cell 10 changed, `conlang-scholarship.md` → `…, …worldbuilding-setting-practice.md`. All 10 other cells are byte-identical, and the row has 11 cells ✔. Row sha at main = c4bf61a = `f7eba3a7…3695`. |
| opened / recheck / status | 2026-10-25 / 180d / mined | consistent with the Gate. |

Tier verdict: **agree B, not A.** It is a monograph from a small press (ISBN prefix 5-98789), not peer-reviewed, author-hosted, and its taxonomy is one of several it surveys (p. 11 "мы принимаем следующую типологию"; p. 12 "Есть и другие способы классификации"). All of that is stated in the row, and B is the right call. Tier scope matters, though: B is granted for the scope cell, not globally (SOURCES.md header: "Tiers are scoped to the row's `scope`, never global") — see F1.

Gate row (corpus/lessons/round-74.md `## Gate`, lines 16–18): URL ✔, access date 2026-10-25 ✔ (the evidence `fetched: 2026-10-26T01:09:09Z` is 22:09 local, America/Sao_Paulo), bytes/sha ✔, locator "p.7 (PDF page 7)" ✔, verdict admitted ✔. Two prose statements in the Gate notes are false (F4).

## 4. Pages 7, 35, 36, 139, 140 against the entry's locators
Entry `corpus/knowledge/culture-material/worldbuilding-setting-practice.md`, source line 3: "cited here at printed pages 7, 35, 36, 139 and 140". Every S877-cited sentence:

| entry line | sentence (≤25 tokens quoted) | page | carried? |
|---|---|---|---|
| 36 | "Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и социальных реалий" (15 tokens) | p. 7 | **YES**, verbatim after fold; translation OK. |
| 38 | "ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации" | p. 139, item 14 | Quote YES, verbatim. The gloss "a constructed language is normally not a means of communication" is wider than the page (F2). |
| 42 | "связь между лингвоконструированием и моделированием миров неразрывна" + "an author may run from world to language or from language to world" | p. 35 | **YES**: «Вы можете идти и другим путем: от языка к вымышленному миру … (от языка к вымышленному миру или наоборот) связь … неразрывна». |
| 44 | "некое научное или не совсем научное допущение" … "builds around it the picture of the world that would follow if the premise held" | p. 36 | Quote YES; paraphrase of «далее строит вокруг него ту картину мира, которая, по его мнению, сложится при существовании данного допущения» OK, but "states the rule" is not carried (F3). |
| p. 140 | none | p. 140 | **No sentence in the entry uses p. 140**, although the source line lists it (F6). |

Programmatic check of all 4 Cyrillic quotes in the entry: each found, `[7] [139] [35] [36]`, 1 page each.

Sentences citing S877 that the page does NOT (fully) carry — see F2, F3 and F7:
- Line 32 (§1): "a constructed language is its world's subject rather than a means of talk". The page says ВЯ is «предметом, темой коммуникации» — the subject/topic of communication, around which communicative situations form (p. 139). It does not say the language is its world's subject.
- Lines 44–46 and table line 52: the premise as a rule and "where to start".
- Line 40: "not to a need for talk — the same volume rule".
- Line 261: "the atmosphere function of a world's language sets how deep the language file goes".

## 5. Entries using S877 inside its scope?
Two landed entries cite S877:
(a) `linguistics/conlang-scholarship.md` (round 73, the row's original consumer);
(b) `culture-material/worldbuilding-setting-practice.md` (round 74, the new used-by). There is no other file in `corpus/` that carries the id S877 apart from the lessons, SOURCES.md and the accept scripts.

### (a) conlang-scholarship.md: all S877 sentences checked against the page
I verified every sentence and quote, and the page cites match:
- §3: p. 10 "ни у ученых-лингвистов, ни в среде конлангеров нет терминологического единства…", p. 11 numbering 1 / 2.1 / 2.1.1 / 2.1.2 / 2.2 and языки-наброски; Rosenfelder p. 12; Harrison, Kuznetsov, Couturat and Leau pp. 13–14; Capuzzo p. 15; the HKU page p. 16; Klingon as a possible living language p. 12.
- §4: Henning volume rule, pp. 12–13, table rows ✔.
- §5: pp. 16–17, 19–21 ✔, with «не «должны», а «могут»» on p. 19, the manifesto point on pp. 19–20, and Jakobson on p. 21.
- §6: pp. 6 and 22 ✔.
- §7: Tolkien p. 23 ✔, Klingon pp. 24–25 ✔ (OVS, no tense/gender/adjectives, own script, 1992 KLI, ISSN 1061-2327), D'ni p. 26 ✔ («Ричардом А. Ватсоном»), pp. 26–27 ✔.
- §8: pp. 11, 27–29 ✔; counters p. 5 (≈1 500, ≈20 000 in 1999) and p. 8 (773 languages, 28 July 2005) ✔.
- Its source line says "preface pp. 4–7, ch. 1 pp. 8–34"; its row-scope sentence ("S877's row is scoped to the book's framing and chapter structure; the opened artefact is the whole book, so the body cites printed pages") is honest.

Defects there: F8 (Tolkien count) and F10 (locator-less cites), both LOW.
Scope: §6 (the description-first discipline; p. 6 and the p. 22 authored-history mechanics) is chapter-1 framing, borderline against the scope cell but defensible as "the book's own framing". No finding.

### (b) worldbuilding-setting-practice.md: scope breach, F1 (HIGH)
The row's scope is classification / vocabulary / special status of three languages / literature survey. The new entry uses S877 for four claims about **how worlds are built** (the language as the chief instrument of world-building, the world–language link, the SF premise, the communication function) and calls the monograph "tier B" for them (line 11: "the monograph is tier B and supplies what a constructed world is"). The rows are append-only (only `status`, `recheck`, `used-by` change in place), so the scope cell cannot be widened; the lesson's in-place edit changed only `used-by`. "Tiers are scoped to the row's `scope`." The landed entry therefore cites a tier-B row for claims outside its recorded scope.

## FINDINGS

### F1 — HIGH — worldbuilding-setting-practice.md cites S877 outside the row's scope cell
- Evidence: row cell 4 (command `git -C … show main:corpus/SOURCES.md | sed -n 832p`) lists "classification of artificial languages…, the vocabulary separating вымышленные языки from вспомогательные… special status of Tolkien's languages, Klingon and D'ni, … survey of the literature". The entry's S877 cites are lines 36, 38, 42 and 44 (pp. 7, 139, 35, 36) and the table at lines 48–52. `grep -n 'S877' wsp.md` shows the line 3 source line pairing "the passages where the book treats world-building as the context of conlang-making".
- The lesson (`round-74.md` lines 90–98) logs only the used-by change; it does not widen or justify the scope.
- Fix: either a new supersede/amend row (`teaches` opens "supersedes S0NN —" under the append-only rule) scoping pp. 7/35/36/139–140 as the book's world-building framing, or have the entry state in its `sources:` line that these cites sit outside the S877 scope cell and carry them as an explicitly out-of-scope tier-B reading. Without that, QUALITY's tier-scope rule is not met by the entry.

### F2 — MEDIUM — "a constructed language … not a means of communication" overgeneralises ВЯ (p. 139)
- Entry lines 32 and 38: "a constructed language is normally not a means of communication but its subject and topic (S877)", "a constructed language is its world's subject rather than a means of talk".
- Page p. 139: «ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации, то есть вокруг него формируется особый набор коммуникативных ситуаций». ВЯ = вымышленный язык (p. 11 class 2; auxlangs, class 1, are excluded and "служить в качестве международных искусственных языков").
- p. 140 contrasts: «конланги, сконструированные для фантастических миров, от искусственных языков типа эсперанто, идо, ложбана и др., призванных обслуживать коммуникацию между людьми». For a constructed language in general (auxlangs, class 1) the sentence is false.
- "its world's subject" is not on the page; the subject is *of communication*.
- Fix: write "a fictional language (ВЯ)", and drop "its world's" or say "the subject of communication around it".

### F3 — MEDIUM — the "premise" is promoted to "the rule" / "strongest single design rule" and contradicted by other lines of the entry
- Page p. 36: «Особенность научной фантастики состоит в том, что автор предлагает читателю некое научное или не совсем научное допущение и далее строит вокруг него ту картину мира, которая, по его мнению, сложится…». This describes a genre feature (with Urban cited), not a rule for builders; «по его мнению» is dropped.
- Entry line 44 "states the rule"; line 46 "it is the strongest single design rule in this entry: the first artefact is a one-sentence premise, and everything else is derived from it"; table line 52 "where to start | [scholarly source:] a premise, then the world picture it implies".
- The same book on p. 35 says the direction is free («Вы можете идти и другим путем: от языка к вымышленному миру» … «как бы ни двигался создатель ВЯ (от языка к вымышленному миру или наоборот)»), and the entry itself says so at line 42 ("The direction of construction is free"). Line 23 says the monograph "prescribes no authoring order". Table line 53 ("order… not addressed") is consistent with line 23 but not with line 52.
- "one-sentence" is not on the page.
- Fix: label line 46 and table row 52 as the entry's inference ("the book describes SF authors starting from a premise; it prescribes no start"), or delete "where to start" from the scholarly column.

### F4 — MEDIUM — two false statements in the round-74 Gate notes (corpus/lessons/round-74.md lines 26 and 174, R74-M7)
- Claim: "The located sentence is 108 characters and 15 whitespace tokens … the full sentence stays on the evidence file's `quote:` line."
- Observed, from the PDF page 7 extract: the 108-char / 15-token span ends at «реалий,» and is a clause. The sentence runs to «…на сконструированных языках).» and measures **285 chars / 37 tokens**.
- `reports/round-74/evidence/S877.txt` line 31 (`quote:`) is the 54-char head clause. The 108-char text is in no `quote:` line; it appears only in the `locator:` line, with «…».
- R74-M7's resolution wording rests on the false measurement: "the located S877 sentence is 15 tokens but 108 characters".
- The Gate cell and the evidence file are internally consistent (54 chars, 7 tokens); only the prose is wrong.
- Fix: say "108-character clause, 285-character sentence"; either put the 108-char clause on the evidence file or delete "full sentence stays on the evidence file's quote: line".

### F5 — LOW — the row's anchor span is a quotation of Rick Harrison's FAQ, not the authors' own sentence
- Page p. 10 (extract): «…ряд терминологических обозначений. Языки, используемые в художественных произведениях, называют вымышленными или фикциональными. Те, которые сконструированы для обеспечения международной коммуникации, называются … Царство искусственных языков также включает …»1 (http://www.rickharrison.com/language/faq.txt)». The footnote 1 on the same page gives the English original: "Those used in works of fiction are called imaginary languages or fictional languages."
- The row anchor presents it as the book's span. The scope cell's "vocabulary separating вымышленные языки from вспомогательные" is partly Harrison's list as quoted by the book.
- It is true to the page ("the book carries it"), but a re-checker should know whose voice it is. The Gate's p. 7 quote is the authors' own voice.
- Fix: a note in the next recheck: "p. 10 span is Harrison via fn. 1"; no row edit is possible without a supersede row.

### F6 — LOW — entry source line claims p. 140 and uses it nowhere
- Entry line 3: "cited here at printed pages 7, 35, 36, 139 and 140"; no S877 sentence has the p. 140 content. The p. 140 text (world history written «с обратным отсчетом», conlangs as an exercise for linguists, the Tolkien-style `Тезаурус полной луны` quotes) is nowhere in the entry (`grep -n -i 'histor\|140'` hits only unrelated lines 66, 67, 95).
- Also: no sentence in the entry carries a page; the pages sit only on the source line. Round 73's lesson recorded "page per cite" for conlang-scholarship.md (R73 lesson line 162); the new entry did not apply it.
- Fix: drop 140 from the source line, or add the p. 140 claim; add "(S877 p. N)" to the four sentences.

### F7 — LOW — cross-reference lines lean on S877 without the cite and attribute things to conlang-scholarship.md that it does not contain
- Line 40: "a world's language layer is sized to what the world must carry, not to a need for talk — the same volume rule `linguistics/conlang-scholarship.md` records". The volume rule there (Henning, p. 12–13) ties size to **use**, and the third row says real communication or literature needs "far more". "Not to a need for talk" is the entry's gloss, and partly inverts the table.
- Line 261: "the atmosphere function of a world's language sets how deep the language file goes". `grep -n -i atmosph cs.md` finds nothing. The only "atmosphere" in the book is Capuzzo's class 2.3 «Фикциональные (для создания атмосферы вымышленного мира…)» on p. 16, which is not cited by page in the entry.
- Fix: cite p. 16, or delete the "atmosphere function" attribution.

### F8 — LOW — mistranslation, "nearly two dozen" for «почти двух десятков»
- conlang-scholarship.md §7 table: Tolkien "credited by the book («считается») with nearly two dozen languages".
- Page p. 23: «Считается, что Толкин был творцом почти двух десятков языков» — "almost twenty"; a dozen is двенадцать.
- Fix: "nearly twenty".

### F9 — LOW — two evidence-file counters not reproducible (see §2)
- `extract: 494887 chars` against 494888 here; `visible-chars: 492810` against 492870 / 492869 / 425943 under my three definitions. The quote, window sha256, window bytes and offsets all reproduce exactly, so this is a definition gap, not a content gap.
- Fix: state the definition of `visible-chars` in the evidence grammar.

### F10 — LOW — conlang-scholarship.md carries locator-less S877 cites in §3/§4/§7
- Lines 38, 49, 51, 55 and 64 cite "(S877)" with no page. All of those claims are on pp. 10–13 (§3/§4) and the `p. 11` numbering is only on the table header. The §7 page line (Tolkien p. 23; Klingon pp. 24–25; D'ni p. 26) was added after R73.
- Fix: add "p. 10–12" / "pp. 12–13" to §3 and §4.

### Smaller, unfiled
- The HKU page in conlang-scholarship.md §3 ("a composite letter-plus-SVO index from a University of Hong Kong page"): the book prints only the URL `http://web.hku.hk/~antonioc/conLang/class.htm`; "University of Hong Kong" is an inference from the domain (the token "Hong Kong" appears nowhere in the text). The description of the index (a priori/a posteriori scale, classes А/В/С/Z, plus an SVO word-order tag) matches p. 16 ✔.

## Attacks that FAILED (the claim survived)
1. Quote not on the page: it is there (printed p. 7; 1 occurrence; 54 chars / 7 tokens; after whitespace fold).
2. The page moved since the Gate: it did not. Same sha256, same 1055723 bytes, same 2007 ETag; the Wayback carrier 20260208005339 is byte-identical and its CDX row is present (positive control run).
3. The evidence file's window is wrong or forged: sha256, byte count and offsets all reproduce from the Gate's own extractor definition.
4. The row's in-place change is wider than `used-by`: only cell 10 differs (`git show` of base vs main row; 11 cells both).
5. Printed-page offset is off (p. 7 vs PDF page, pp. 35, 36, 139, 140): offset 0, confirmed from printed numbers on adjacent pages.
6. All 4 quotations in the new entry and all 9 in conlang-scholarship.md are on the cited pages (programmatic check, whitespace-folded).
7. S877 is mis-tiered B: B is right (see §3).
8. conlang-scholarship.md carries claims the page lacks: apart from F8, the §3–§8 sentences are carried on their cited pages (§5 above).

## Commands (reproduction)
```
D=/tmp/ScoutReopenS877; cd $D
pdftotext -enc UTF-8 conlangs.pdf out2.txt        # plain mode
python3 - <<'E'   # fold + locate
import re;t=open('out2.txt',encoding='utf8').read();P=t.split('\f')
q="Язык – главный инструмент построения вымышленных миров"
print([n+1 for n,p in enumerate(P) if re.sub(r'\s+',' ',q) in re.sub(r'\s+',' ',p)])   # -> [7]
E
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show main:corpus/SOURCES.md | sed -n 832p
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show main:reports/round-74/evidence/S877.txt
```
Tools: no installs (pdftotext 26.08.0 and curl were already present).
