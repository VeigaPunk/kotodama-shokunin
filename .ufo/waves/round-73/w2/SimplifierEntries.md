# SimplifierEntries — round 73 / wave 2 (FALSIFY, hyaku run 7)

Seat: LEAF simplifier. Target: the two landed entries of claim C,
`corpus/knowledge/linguistics/conlang-scholarship.md` and
`…conlang-scholarship.amend-2026-10-23.md`.

**Revision note.** My item names the landed revision `0316b8883b4f8d44b8efd720140e7f52f734a102`.
While this seat ran, the lane advanced to **`7aa8f9903a0b3dc935a8c14a11d5a5a26c956190`**
("wave-2 falsify repairs — entry content fixes (per-sentence fact-check) …"), which rewrote both
entries. I re-fetched, re-read and re-measured everything at `7aa8f99`; **every number and every
line anchor below is at `7aa8f99`**. Section "What the repair already fixed" lists what I found
at `0316b88` that no longer holds, so it is not re-litigated. The lane then advanced twice more
(to `c1b5b47`); `git diff --stat 7aa8f99 c1b5b47 -- corpus/knowledge/ corpus/SOURCES.md` is empty,
so the anchors and the measured cut remain valid at current HEAD.

Lane working tree untouched: the only modified tracked path in the lane is this report
(`git status --porcelain` → ` M .ufo/waves/round-73/w2/SimplifierEntries.md`, my own file, tracked
by the wave-2 repair commit). Every byte-changing experiment ran in a throwaway clone.

## Verdict

- **495 words of 3,957 (12.5%) do not earn their place for a worldbuilder**: base entry
  2,106 → 1,830 (−276, −13.1%), amendment 1,851 → 1,632 (−219, −11.8%).
- **All 11 claim-C legs stay PASS on the cut bytes** — measured at `7aa8f99`, not assumed.
- **Three couplings/statements are still wrong at HEAD** (F1–F3, MAJOR): one self-contradicting
  sentence in the amendment, and two `couples:` pointers that name a section which does not
  hold the material. None is read by a leg.
- Nothing here is a claim-leg failure, so nothing is a `kill_rule` trigger.

## Method and environment

```
D=$(mktemp -d) && git -C "$D" init -q
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
git -C "$D" rev-parse --show-toplevel   -> /tmp/tmp.XO43287mUC   (== $D)
# after the lane moved:
git -C "$D/lane" fetch -q origin && git -C "$D/lane" checkout -q --detach 7aa8f9903a0b3dc935a8c14a11d5a5a26c956190
git -C "$D/lane" diff --stat 0316b88 7aa8f99 -- reports/round-73/accept-c.py tools/   -> (empty; same counter)
```

Counter runs, both from the clone (`--fleet-root /home/vgpnk/Projects/shokunin` supplies only the
census script path; the CENSUS leg materializes `<lands>`, so the fleet tree is read, never written):

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 7aa8f9903a0b3dc935a8c14a11d5a5a26c956190 \
      --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-73: PASS legs=11/11                       # baseline at HEAD

# cut bytes committed in the clone only: 0b50562f42369727046997e86d788782e91f1839 (parent 7aa8f99)
$ python3 -B reports/round-73/accept-c.py --root . --lands 0b50562f42369727046997e86d788782e91f1839 \
      --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK
ACCEPT-C-73: PASS legs=11/11                       # cut bytes
```

Cited-line check (the lane's own tool) on the cut pair and on the landed pair:

```
$ python3 -B tools/check-cited-lines.py /tmp/SimplifierEntries/cut2/base.md /tmp/SimplifierEntries/cut2/amend.md
CITED-LINES: 0 finding(s) in 2 file(s)        exit=0
$ python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/conlang-scholarship.md \
      corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
CITED-LINES: 0 finding(s) in 2 file(s)        exit=0
```

ENTRIES floor (`_min_entry_words` at base = 478): cut bodies are **base 1,423 / amend 1,097**
words after the header block — both far above the floor. Registry `used-by` derives from the
`- source:` header lines only; **no source line is touched**, so S876/S877 → base and
S878/S879/S880 → amend are unchanged (ROWS PASS on the cut revision proves it).

Fetch log (all into `/tmp/SimplifierEntries/`, plain `curl/8.7.1`; no wall met, no browser UA
needed, no challenge passed, no captcha solved):

| row | URL | status | bytes | sha256 |
|---|---|---|---|---|
| S876 | `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` | 200 | 30,289 | `e7260b49…19369c` |
| S877 | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1,055,723 | `e512a20d…a595a9` |
| S878 | `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` | 200 | 959,171 | `9f745dda…ed07c` |
| S879 | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` | 200 | 97,656 | `0b6969e5…d709bc` |
| S879 PDF | `…/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf` | 200 | 630,227 | `cc9a91c5…c0643f` |
| S880 | `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` | 200 | 193,610 | `26dbcf2c…a0d535` |

Text extracted with the system `pdftotext` (both `-layout` and plain). **No tool was installed or
upgraded**; nothing was fetched from the fleet root or the lane root.

## Keep / cut per section (word counts measured in `/tmp/SimplifierEntries/cut2/`)

Section counts split on `^## `; totals are `wc -w` over the whole file.

| file | section | before | after | delta | verdict |
|---|---|---|---|---|---|
| base | (header) | 407 | 407 | 0 | KEEP all 11 fields (ENTRIES leg) |
| base | §1 Calibration key | 205 | 194 | −11 | KEEP the table (QUALITY 2 device); cut the reader-instruction clause |
| base | §2 Construction as a teaching method | 174 | 115 | −59 | CUT keywords note + abstract-limit duplicate |
| base | §3 A taxonomy | 313 | 261 | −52 | CUT the competing-classifications bibliography |
| base | §4 How much language | 130 | 111 | −19 | CUT the praise sentence and the dangling `naming-systems` imperative |
| base | §5 Different contracts | 167 | 221 | +54 | KEEP all; three-axes prose → 3-row table; absorbs Higley from §8 |
| base | §6 Description is the language | 200 | 200 | 0 | KEEP whole — every line carries a lever |
| base | §7 Three languages | 261 | 241 | −20 | CUT the Tolkien-father historiography |
| base | §8 Status in the field | 168 | 0 | −168 | CUT section; keep only Higley (moved to §5) |
| base | §9 Coupling to the world bible | 72 | 72 | 0 | KEEP (QUALITY 3/5 handoff) |
| **base total** | | **2,106** | **1,830** | **−276** | |
| amend | (header) | 544 | 535 | −9 | KEEP all fields; cut one clause in `- ground:` |
| amend | §1 the scale | 335 | 296 | −39 | CUT the abstract-method sentence |
| amend | §2 typologies | 447 | 346 | −101 | CUT the авторскими note, the "article's own subject" meta; compress the restatement; repair the table sentence |
| amend | §3 classroom study | 239 | 202 | −37 | CUT the duplicate novelty quote |
| amend | §4 what the lane does | 167 | 167 | 0 | KEEP whole — four design consequences |
| amend | §5 provenance limits | 114 | 81 | −33 | CUT the duplicated semester line and the closing process note |
| **amend total** | | **1,851** | **1,632** | **−219** | |

## Findings at HEAD (`7aa8f99`)

### F1 — MAJOR — amendment line 53: a sentence that contradicts itself about its own source

Landed: *"The table's Peterson column names nine classes; the prose bullet-list gives six and
adds parody languages (instance: Yesqur) plus a mention of gesture- and graphic-symbol-based
constructed languages, which the article counts as an advantage of the taxonomy; **only the three
category names are table-only** (S879, printed pp. 30, 32–33)."*

The first half is right — I verified the nine classes from the printed table (two shared:
auxlangs, artlangs; seven distinct: personal, secret, fictional, engineered, parody, sign,
graphic). The last clause is false: the prose gives the English category names in parentheses.

```
$ python3 - <<'PY'   # tags stripped from /tmp/SimplifierEntries/s879.html
for p in ('parody languages or jokelangs','sign languages or manual languages','graphic languages'):
    print('%-34s -> %s' % (p, 'present in prose' if p in txt else 'absent'))
PY
parody languages or jokelangs      -> present in prose
sign languages or manual languages -> present in prose
graphic languages                  -> present in prose
```

The printed text (`pdftotext -layout s879.pdf`, pp. 30–31) reads «… можно отнести к группе
пародийных языков (parody languages or jokelangs)» and «Питерсон предлагает выделять языки
жестовые (sign languages or manual languages) и графические (graphic languages)». So the
qualifier must go, and with it the "table-only" inference.

**Exact cut:** replace the clause `; only the three category names are table-only` with
`; the printed table and the prose therefore agree on the categories, and differ only in that
the prose adds examples`. (My cut file already applies a shorter variant of this.)

### F2 — MAJOR — base line 11: `historical-linguistics.md (§6's authored history)`

```
$ grep -n '^## ' corpus/knowledge/linguistics/historical-linguistics.md
143:## 6. Dating language stages
175:## 7. Constructing proto-languages and daughter languages
```

§6 is relative chronology and dating; the authored-history procedure the base §6 describes
(write a family's history backwards or forwards, ordered law lists, strata) is §7.
**Exact fix:** `(§7's constructed family)`.

### F3 — MAJOR — amendment line 16: the methodology stage pointer

`conlang-methodology.md` *(the craft pipeline whose Stage 1–2 choices the scale argument bears
on)*:

```
$ grep -n '^## Stage' corpus/knowledge/linguistics/conlang-methodology.md
38:## Stage 1 — phoneme inventory
45:## Stage 2 — phonotactics
82:## Stage 5 — 300-word core lexicon
$ grep -n 'Derivation-first' corpus/knowledge/linguistics/conlang-methodology.md
86:- Derivation-first vs coin-first: if the language has deep history, derive the lexicon from
    proto-roots … If it must ship fast for scenes, coin directly and back-derive later
```

The a priori / a posteriori scale bears on Stage 5's derivation-first/coin-first choice, not on
inventory or phonotactics. **Exact fix:** `(the Stage 5 derivation-first/coin-first choice the
scale argument bears on)`.

### F4 — MINOR — amendment line 12: a promise §2 breaks

*"This amendment adds those three documents; it does not restate the base's topic, gap, or
§2–§5."* §2 line 39 restates the base §3 classes (now compressed and flagged as a second voice,
but restated). **Exact cut:** `; it does not restate the base's topic, gap, or §2–§5` — the field
stays present and non-placeholder (ENTRIES leg unaffected).

### F5 — MINOR — the same receipt twice inside the amendment (lines 71 and 91)

Both say the token "semester-long" is absent from S880's nine pages. Line 71 carries the command,
so **cut line 91** and start line 93 at "The term «автоконланги»…" (which also retires the
now-wrong "Two staged elements").

### F6 — MINOR — amendment line 95: a process note with no content

*"This amendment appends to `linguistics/conlang-scholarship.md`; the base points here through its
`couples:` line."* The coupling is already stated twice in the two entries' `- couples:` lines.
**Exact cut:** delete line 95.

### F7 — MINOR — duplication, measured

- base:33 ↔ §1 row 19 — the same "no curriculum, cohort or count" calibration, twice.
- base §8 lines 99–101 ↔ §1 rows 22–24 — the same three frameworks' statuses, twice.
- amend:41 ↔ base §3 row 46 — «авторские языки» stated twice (base's row already reads
  "2.2 Personal, or авторские, languages").
- amend:67 — the "claimed novelty" quote is the S880 registry anchor quote verbatim.

### F8 — MINOR — vacuous and dangling lines in the base

- line 56 *"Of the classifications it surveys, this one transfers most directly to a build."* —
  a ranking with no criterion; §4's design-consequence line already does the work.
- line 64 *"Read that rule against `linguistics/naming-systems.md` (S877)."* — an imperative with
  no content; the repair re-pointed the `couples:` parenthetical correctly, so the sentence is now
  merely empty rather than false.
- line 32 — the keywords note (now honest: "four of the ten the page lists") is an audit fact
  about the page, not a design input.
- line 50 — four competing classifications named with no criterion and no consequence
  (QUALITY 4, "No essays"). The repair corrected the attribution (verified: the book traces the
  a priori/a posteriori tradition to Couturat and Leau **via Kuznetsov**, and describes Harrison's
  classification separately), so this is now purely a length cut.
- line 93 — "It treats Tolkien as the movement's father …" — historiography with no lever.

## The cut list (line numbers at `7aa8f99`)

`CL` = check-cited-lines, `UB` = registry used-by, `LEG` = claim-C leg.

| # | file:line | exact cut | CL | UB | LEG | QUALITY |
|---|---|---|---|---|---|---|
| 1 | base:11 | `(§6's authored history)` → `(§7's constructed family)` | no | no | none | 3 improved (F2) |
| 2 | base:26 | delete the 2nd sentence "The sources' own words appear below, each with its row's id." | no | no | none | 1 unaffected (calibration sentence kept) |
| 3 | base:32 | delete the keywords sentence — a page-audit note, no consequence | no | no | none | 1/4 improved |
| 4 | base:33 | delete the sentence; §1 row 19 carries the same calibration | no | no | none | 2 still satisfied by §1 |
| 5 | base:50 | delete the competing-classifications sentence | no | no | none | 4 improved |
| 6 | base:56 | delete "Of the classifications it surveys, this one transfers most directly to a build." | no | no | none | 4 improved |
| 7 | base:64 | delete "Read that rule against `linguistics/naming-systems.md` (S877)." | no | no | none | 3 unaffected (couples line keeps the link) |
| 8 | base:69 | replace the three-axes prose with a lead line + 3-row table (`body of users` / `world picture` / `simplicity`); S877 stays in the lead, **no S-id in any table row** | no (verified 0 findings) | no | none | 4 improved |
| 9 | base:93 | delete the Tolkien-father sentence | no | no | none | 4 improved |
| 10 | base:96–102 | delete the §8 heading and lines 98, 99, 100, 102; **move** line 101 (Higley, "конланги – это действительно модели, артефакты") to the end of §5 | no | no | none | 4 improved; 2 still satisfied by §1 rows 22–24 |
| 11 | amend:12 | delete `; it does not restate the base's topic, gap, or §2–§5` | no | no | none | header intact (F4) |
| 12 | amend:16 | `Stage 1–2` → `Stage 5 derivation-first/coin-first` | no | no | none | 3 improved (F3) |
| 13 | amend:21 | delete the "states its method in the abstract … 24 words" sentence — the quote is the S878 registry anchor cell and the Gate line; "24 words" is an audit count | no | no | none | 1 unaffected |
| 14 | amend:39 | compress: keep "the review restates them without adding members" + the Э'П/D'ni rendering discrepancy; drop the class-by-class enumeration (it is base §3's table) | no | no | none | 4 improved |
| 15 | amend:41 | delete the авторскими note (base §3 row 46 already carries the term) | no | no | none | 1 unaffected |
| 16 | amend:53 | replace the false final clause (F1) | no | no | none | 1 improved |
| 17 | amend:55 | delete "The article's own subject is Peterson's classification … not the reverse" — the S879 registry row already scopes the article | no | no | none | 6 unaffected (row carries the scope) |
| 18 | amend:67 | delete the "claimed novelty" sentence — registry anchor quote verbatim; §4 bullet 4 carries its operative content | no | no | none | 1/4 improved |
| 19 | amend:91 | delete; start line 93 at "The term «автоконланги»…" | no | no | none | 1 unaffected |
| 20 | amend:95 | delete the closing process note | no | no | none | 4 improved |

Nothing in the list touches a `- source:` line, a `- topic:` line, or a table row carrying an
S-id; that is why CL, UB and all 11 legs stay green (measured at `0b50562`).

## What the repair already fixed (checked at `7aa8f99`, not re-raised)

- **Heading** was "Three Russian-language typologies" — only two are Russian (Шувалова/Сидорова,
  Piperski); Peterson is «американским лингвистом» in the article itself. Now reads "Three
  typologies in a Russian-language review" — correct.
- **Harrison/Couturat attribution** was "(Harrison, after Couturat and Leau)"; the book credits
  the lineage to Kuznetsov's auxlang formulation. Now reworded correctly.
- **`naming-systems.md` couples pointer** was "(§4's naming-language volume rule)" while §4 is
  theonymy; now "the names file this entry's §4 naming-language row bears on" — correct.
- **S879 page locations**: the earlier text carried a (to-verify) for the pages; the repair cites
  pp. 31–32 for items 1–2.2 and p. 33 for the table. I confirmed from the fetched PDF that item
  2.2 and Таблица 1 fall on the pages the footers bracket (32 and 33); the exact p.30/p.31 split
  of the bullet list I could not pin from the layout text.
- **"nine classes"** in the Peterson column — correct: 2 shared (auxlangs, artlangs) + 7 distinct.

## Examined and kept, with the proof

- **base:49** "The book's own subject is class 2.2" — `book.txt`: «Именно они [авторские языки] и
  служат предметом нашего дальнейшего рассмотрения.» It scopes §6: description-first is stated
  for personal languages, not for Tolkien-style artlangs.
- **base:90** the page list for the three §7 rows and **base:94** the Klingon (to-verify) line —
  locators and provenance (QUALITY 1/12).
- **base §1 rows 19–24** — the QUALITY 2 compliance device; a table, not an essay.
- **base §6 whole** — every sentence is a lever (description precedes language; discontinuous
  authored change; history written backwards; the grammar file is canon).
- **base §7's "Transferable lever" column** — each row converts a fact into a decision.
- **amend §1 lines 23–35** (the hedged scale, Halley's split, the zonal languages, the 68-language
  range, the conclusion quote, calibration, Eurocentrism) — verified against S878; the scale and
  Eurocentrism are used by §4. The zonal-language fact (Križanić's Common Slavonic) is the one
  lever with no consequence anywhere in either entry — a gap, not a cut.
- **amend:51** the calibration of the ranking (podcast form, the Rhiemeier objection) — QUALITY 2,
  and the only place the article's own hedge is recorded.
- **amend:59** the location line — replaces the old (to-verify); QUALITY 1.
- **amend §3 lines 63–65, 69** and **§4 all four bullets** — the only content the S880 row
  supports; §4 is the amendment's whole point.

## What I could NOT check

- **The exact p.30 / p.31 boundary** of S879's Peterson bullet list: `pdftotext -layout` prints
  footers for pp. 29, 31 and 33 only, so I can bound the passage (pp. 30–31) but not split it.
- **The Sowers-Wills article itself**: not fetched. The amendment records HTTP 429 to both UAs on
  2026-10-25; I did not re-probe, so its reachability today is unverified by me.
- **Whether any downstream consumer reads a section of either entry**: no lane document cites one
  (`grep -rn 'conlang-scholarship'` outside the entries returns README topic lines, the lesson,
  the registry rows, the claim and the counter), and README's index rows are the `- topic:` text
  verbatim, which no cut touches — but I tested no consumer beyond that grep.
- **Whether the cuts are the right stylistic call** is a judgment defensible from QUALITY 4, not a
  measurement.
