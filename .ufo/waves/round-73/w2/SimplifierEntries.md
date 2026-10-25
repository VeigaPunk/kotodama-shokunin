# SimplifierEntries — round 73 / wave 2 (FALSIFY, hyaku run 7)

Seat: LEAF simplifier. Target: the two landed entries of claim C at lane revision
`0316b8883b4f8d44b8efd720140e7f52f734a102`
(`corpus/knowledge/linguistics/conlang-scholarship.md`,
`corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md`).
Lane working tree untouched (`git -C kotodama-shokunin rev-parse HEAD` = `0316b88…`,
`git status --porcelain` shows only pre-existing untracked wave files). Every
byte-changing experiment ran in a throwaway clone.

## Verdict

- **417 words of 3,549 (11.7%) do not earn their place for a worldbuilder** and can go
  without breaking a single claim-C leg: base entry 1,986 → 1,748 words (−238, −12.0%),
  amendment 1,563 → 1,384 (−179, −11.4%).
- **All 11 claim-C legs stay PASS on the cut bytes** — measured, not assumed (below).
- **Two admitted statements are false** (F1, F2) and **four couplings point at the wrong
  section** (F3–F6). None of these is read by any leg; the claim survives *as declared*
  while the sentences must not stand.
- Nothing here is a claim-leg failure, so nothing is a `kill_rule` trigger. By this seat's
  rubric ("a claim leg **or an admitted statement** is wrong") F1/F2 are BLOCKER-severity
  defects of the admitted artefacts.

## Method and environment

```
D=$(mktemp -d) && git -C "$D" init -q
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
git -C "$D" rev-parse --show-toplevel   -> /tmp/tmp.XO43287mUC   (== $D)
```

Baseline and cut runs of the declared counter, both from the clone
(`--fleet-root /home/vgpnk/Projects/shokunin` supplies only the census script path; the
leg materializes `<lands>`, so the fleet tree is read, never written):

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 \
      --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK
ACCEPT-C-73: PASS legs=11/11

# cut bytes committed in the clone only: 485c67761b6cb49da1bed06b79406cb02cd8afef (parent 0316b88…)
$ python3 -B reports/round-73/accept-c.py --root . --lands 485c67761b6cb49da1bed06b79406cb02cd8afef \
      --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-73: PASS legs=11/11
```

Cited-line check, on the cut pair and on the landed pair, with the lane's own tool:

```
$ python3 -B tools/check-cited-lines.py /tmp/SimplifierEntries/cut/base.md /tmp/SimplifierEntries/cut/amend.md
CITED-LINES: 0 finding(s) in 2 file(s)        exit=0
$ python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/conlang-scholarship.md \
      corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
CITED-LINES: 0 finding(s) in 2 file(s)        exit=0
```

ENTRIES floor (counter `_min_entry_words` at base = 478 words): cut bodies are
**base 1,380 / amend 949** words after the header block — both far above the floor.
Registry `used-by` is derived from the `- source:` header lines only; **no source line is
touched**, so S876/S877 → base and S878/S879/S880 → amend are unchanged (ROWS PASS on the
cut revision proves it).

Fetch log (all to `/tmp/SimplifierEntries/`, plain `curl/8.7.1`, no wall hit, no browser
UA needed, no challenge passed):

| row | URL | status | bytes | sha256 |
|---|---|---|---|---|
| S876 | `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` | 200 | 30,289 | `e7260b49…19369c` |
| S877 | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1,055,723 | `e512a20d…a595a9` |
| S878 | `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` | 200 | 959,171 | `9f745dda…ed07c` |
| S879 | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` | 200 | 97,656 | `0b6969e5…d709bc` |
| S880 | `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` | 200 | 193,610 | `26dbcf2c…a0d535` |

Text extracted with the system `pdftotext -layout`; no tool was installed or upgraded.

## Keep / cut per section (word counts measured in `/tmp/SimplifierEntries/cut/`)

Section counts split on `^## `; totals are `wc -w` on the whole file (the split drops blank
separators, hence the small difference).

| file | section | before | after | delta | verdict |
|---|---|---|---|---|---|
| base | (header) | 364 | 368 | +4 | KEEP all 11 fields (ENTRIES leg); one sentence of §1's closing line cut |
| base | §1 Calibration key | 205 | 194 | −11 | KEEP table (QUALITY 2 compliance device); cut the reader-instruction clause |
| base | §2 Construction as a teaching method | 163 | 115 | −48 | CUT two sentences (keywords list; abstract-limit duplicate) |
| base | §3 A taxonomy | 305 | 261 | −44 | CUT one sentence (competing-classification bibliography, false attribution) |
| base | §4 How much language | 130 | 111 | −19 | CUT two (vacuous praise; dangling `naming-systems` imperative) |
| base | §5 Different contracts | 158 | 213 | +55 | KEEP all; three-axes prose → 3-row table; absorbs Higley from §8 |
| base | §6 Description is the language | 192 | 192 | 0 | KEEP whole (every line carries a lever) |
| base | §7 Three languages | 232 | 214 | −18 | CUT one (Tolkien-father historiography) |
| base | §8 Status in the field | 156 | 0 | −156 | CUT section; keep only Higley (moved to §5) |
| base | §9 Coupling to the world bible | 72 | 72 | 0 | KEEP (QUALITY 3/5 handoff) |
| **base total** | | **1,986** | **1,748** | **−238** | |
| amend | (header) | 435 | 435 | 0 | KEEP all fields; cut one clause inside `- ground:` |
| amend | §1 the scale | 308 | 269 | −39 | CUT the abstract-method sentence |
| amend | §2 typologies | 366 | 283 | −83 | CUT the Шувалова restatement (cross-entry duplicate), the meta sentence; RENAME heading |
| amend | §3 classroom study | 204 | 167 | −37 | CUT the duplicate novelty quote |
| amend | §4 what the lane does | 154 | 154 | 0 | KEEP whole (four design consequences) |
| amend | §5 provenance limits | 91 | 71 | −20 | CUT the duplicated semester line |
| **amend total** | | **1,563** | **1,384** | **−179** | |

## Findings

### F1 — BLOCKER — amendment §2, line 50: a false statement about the source's prose

Landed sentence: *"The comparison table's Peterson column carries three categories the
article's prose does not list — parody, sign and graphic languages — so the taxonomy's full
extent is a table entry, not an argued class (S879)."*

The prose **does** list all three, in the same section that enumerates Peterson's six
groups:

```
$ python3 - <<'PY'   # tags stripped from /tmp/SimplifierEntries/s879.html into txt
for p in ('Питерсон предлагает выделять языки жестовые','можно отнести к группе пародийных языков'):
    print(p,'->','да' if p in txt else 'нет')
PY
Питерсон предлагает выделять языки жестовые -> да
можно отнести к группе пародийных языков -> да
```

Verbatim (S879, comparison section, after the six-group list): «Помимо таких языков,
Питерсон предлагает выделять языки жестовые (sign languages or manual languages) и
графические (graphic languages)» and «разработанный лингвистом Уильямом Спруэллом язык
Yesqur можно отнести к группе пародийных языков (parody languages or jokelangs)». The
comparison table (Таблица 1) does carry them — but so does the prose, so the inference
("not an argued class") is false.

**Exact cut:** delete line 50 entire. It is a calibration hedge whose only content is the
false claim; the entry loses nothing else.

### F2 — BLOCKER — amendment §2 heading, line 34: "Three Russian-language typologies"

Only **two** of the three compared typologies are Russian-language:

```
$ python3 - <<'PY'   # strip tags from /tmp/SimplifierEntries/s879.html, then:
i=txt.find('Материалом исследования'); print(txt[i:i+200])
PY
Материалом исследования являются классификации конструированных языков Д. Питерсона ,
О. Н. Шуваловой и М. Ю. Сидоровой, А. Ч. Пиперски. При проведении исследования были …
```

Питерсон is an American linguist (the article itself: «американским лингвистом Дэвидом
Питерсоном»), and the amendment's own §2 line 42 calls his taxonomy a podcast-delivered
practitioner framework. **Exact fix (heading only):** `## 2. Two Russian-language typologies,
Peterson's, and one reviewer's comparison`.

### F3 — MAJOR — base header line 11 and §4 line 64: coupling to a section that does not exist

`- couples:` names ``linguistics/naming-systems.md`` *(§4's naming-language volume rule)*,
and §4 ends with *"Read that rule against `linguistics/naming-systems.md` (S877)."*

```
$ grep -n '^## ' corpus/knowledge/linguistics/naming-systems.md
73:## 4. Theonymy: names of gods
```

§4 is theonymy. naming-systems.md holds no volume rule: the only "how many" hits are about
how many names one person holds —

```
$ grep -n 'how many' corpus/knowledge/linguistics/naming-systems.md
41:… Systems differ mainly in **how many names a person holds, who assigns them, and when they change** …
116:6. **Life-stage schedule** — how many names does one person hold at birth, majority, office, marriage, death? …
```

The imperative therefore has no target, and the parenthetical misdescribes the coupled file.
**Exact cut:** delete line 64; rewrite the parenthetical to the section that does couple —
`(the name lexicon a conlang's naming layer feeds)` — or drop the parenthetical (the
`couples:` field stays non-empty either way).

### F4 — MAJOR — base header line 11: `historical-linguistics.md (§6's authored history)`

```
$ grep -n '^## ' corpus/knowledge/linguistics/historical-linguistics.md
143:## 6. Dating language stages
175:## 7. Constructing proto-languages and daughter languages
```

The authored-history material the entry's §6 describes (write a family's history backwards or
forwards, ordered law lists, strata) is §7. **Exact fix:** `(§7's constructed family)`.

### F5 — MAJOR — amendment header line 13: the methodology stage pointer

`conlang-methodology.md` *(the craft pipeline whose Stage 1–2 choices the scale argument bears
on)*. Stage 1 is the phoneme inventory, Stage 2 phonotactics:

```
$ grep -n '^## Stage' corpus/knowledge/linguistics/conlang-methodology.md
24:## Stage 0 — the culture brief is a spec, not flavor
38:## Stage 1 — phoneme inventory
45:## Stage 2 — phonotactics
52:## Stage 3 — morphology sketch
76:## Stage 4 — syntax skeleton
82:## Stage 5 — 300-word core lexicon
90:## Stage 6 — pragmatics layer
$ grep -n 'Derivation-first' corpus/knowledge/linguistics/conlang-methodology.md
86:- Derivation-first vs coin-first: if the language has deep history, derive the lexicon from proto-roots through the numbered sound-change law list, mechanically … If it must ship fast for scenes, coin directly and back-derive later
```

The a priori/a posteriori scale bears on **Stage 5's** derivation-first/coin-first choice, not
on inventory or phonotactics. **Exact fix:** `(the Stage 5 derivation-first/coin-first
choice the scale argument bears on)`.

### F6 — MAJOR — base §3 line 50: mis-attributed lineage ("Harrison, after Couturat and Leau")

The book gives the Couturat/Leau lineage to **Kuznetsov's** formulation about international
auxiliary languages, and describes Harrison's classification separately:

```
$ sed -n '596,598p' book.txt          # Kuznetsov, on МИЯ
  образом: «По традиции, восходящей к работам Г. Мока, но еще больше к
  знаменитым трудам Л. Кутюра и Л. Ло, все МИЯ распределяются на два
  класса в зависимости от наличия/отсутствия их материального соответ-
$ awk 'NR>=645 && NR<=700' book.txt | grep -c "Кутюра\|Ло,"     # Harrison's block
0
```

The sentence also earns nothing for a worldbuilder: four classification schemes named without
one criterion or consequence (QUALITY 4, "No essays"). **Exact cut:** delete line 50 entire —
the cut removes the mis-attribution and the bibliography in one line.

### F7 — MINOR — amendment `- ground:` line 9: a promise the file breaks

*"This amendment adds those three documents; it does not restate the base's topic, gap, or
§2–§5."* §2 lines 36–38 restate the base §3 table class by class (1. Auxlangs / 2.1 Artlangs /
2.1.1 Tolkien-Klingon-Myst / 2.1.2 Arëndron / 2.2 Personal, авторские). **Exact cut:** delete
`; it does not restate the base's topic, gap, or §2–§5` (keep "This amendment adds those three
documents."). The header field stays present and non-placeholder (ENTRIES leg unaffected).

### F8 — MINOR — one receipt recorded twice inside the amendment (§3 line 68 and §5 line 88)

Both sentences say the token "semester-long" is absent from S880's nine pages. The §3 copy
carries the command, so **cut line 88** and start line 90 at "The term «автоконланги»…"
(which also removes the now-wrong "Two staged elements").

### F9 — MINOR — cross-entry and intra-entry duplication

- Amendment §2 lines 36–38 ↔ base §3 table: the same taxonomy twice in one claim's two
  entries. Keep the base table (it is S877's own numbering with design questions); reduce the
  amendment to a one-sentence pointer.
- Base §2 line 33 ↔ §1 row 19 ("the opened abstract carries no curriculum, cohort or count"):
  same calibration, twice.
- Base §8 lines 97–99 ↔ §1 rows 22–24: the same three frameworks' statuses, twice.

## The cut list (anchored to landed line numbers at `0316b88…`)

`CL` = check-cited-lines, `UB` = registry used-by, `LEG` = claim-C leg.

| # | file:line | exact cut | CL | UB | LEG | QUALITY |
|---|---|---|---|---|---|---|
| 1 | base:11 | replace two parentheticals: `(§4's naming-language volume rule)` → `(the name lexicon a conlang's naming layer feeds)`; `(§6's authored history)` → `(§7's constructed family)` | no (no id) | no (`source:` lines untouched) | none | 3 improved |
| 2 | base:26 | delete 2nd sentence "The sources' own words appear below, each with its row's id." | no | no | none | 1 unaffected (calibration sentence kept) |
| 3 | base:32 | delete "The article's keywords name the frame it works in: Constructed languages, Linguistic Analysis, Linguistics Teaching, Method-Oriented Teaching (S876)." — a selective subset (the page also carries Phonology, Diachronic linguistics, Natlang, Conlangs) restated from metadata; no consequence | no | no | none | 1/4 improved |
| 4 | base:33 | delete "What the abstract does not carry is a curriculum, a cohort or a measured outcome; treat the argument as a position, because the abstract is the whole opened artefact (S876)." — duplicates §1 row 19 | no | no | none | 2 still satisfied by §1 |
| 5 | base:50 | delete entire sentence (bibliography + false Harrison/Couturat lineage) | no | no | none | 1 improved (F6) |
| 6 | base:56 | delete "Of the classifications it surveys, this one transfers most directly to a build." — praise with no criterion; §4's design-consequence line already says it | no | no | none | 4 improved |
| 7 | base:64 | delete "Read that rule against `linguistics/naming-systems.md` (S877)." — dangling, and the target has no such rule | no | no | none | 3 improved (F3) |
| 8 | base:69 | replace the three-axes prose with a lead line + 3-row table (`body of users` / `world picture` / `simplicity`), S877 kept in the lead, **no S-id inside any table row** | no (verified 0 findings) | no | none | 4 improved |
| 9 | base:91 | delete "It treats Tolkien as the movement's father even while noting that constructed languages in fiction predate him (S877)." — historiography, no lever | no | no | none | 4 improved |
| 10 | base:94–100 | delete §8 heading and lines 96, 97, 98, 100; **move** line 99 (Higley, "конланги – это действительно модели, артефакты") into §5 as its last line | no | no | none | 4 improved; 2 still satisfied by §1 rows 22–24, which keep the statuses and reasons |
| 11 | amend:9 | delete `; it does not restate the base's topic, gap, or §2–§5` | no | no | none | header field intact |
| 12 | amend:18 | delete "Novikov's article states its method in the abstract: … — 24 words, Abstract, p. 455 (S878)." — the quote is already the S878 registry anchor cell and the Gate line; "24 words" is an audit count | no | no | none | 1 unaffected (other S878 lines carry the quotes) |
| 13 | amend:34 | heading → "Two Russian-language typologies, Peterson's, and one reviewer's comparison" | no | no | none | 1 improved (F2) |
| 14 | amend:36+38 | delete both paragraphs; insert one line: "The first Russian typology this article compares is Шувалова and Сидорова's (2006), whose classes the base entry's §3 table already reports from the book itself (S879)." | no | no | none | 4 improved; `- topic:` still true (Piperski + Peterson + comparison remain) |
| 15 | amend:50 | delete entire sentence (F1) | no | no | none | 1/2 improved |
| 16 | amend:52 | delete "The article's own subject is Peterson's classification … not the reverse (S879)." — meta about the article; S879's registry row already scopes it as "one review article reporting another author's classification" | no | no | none | 6 unaffected (row carries the scope) |
| 17 | amend:64 | delete the "claimed novelty" sentence — it is the S880 registry anchor quote verbatim, and §4 bullet 4 already carries its operative content | no | no | none | 1/4 improved |
| 18 | amend:88 | delete; adjust line 90's lead-in ("Two staged elements…" goes with it) | no | no | none | 1 unaffected |

Nothing in the list touches a `- source:` line, a `- topic:` line, or a table row carrying an
S-id; that is why CL, UB and all 11 legs stay green (measured).

## Examined and kept, with the proof

- **base:49** "The book's own subject is class 2.2" — verified, not trivia: `book.txt`: «Именно
  они [авторские языки] и служат предметом нашего дальнейшего рассмотрения.» It scopes §6:
  the description-first rule is stated for personal languages, not for Tolkien-style artlangs.
- **base:92** the Klingon (to-verify) line — provenance, QUALITY 1.
- **base §1 rows 19–24** — the QUALITY 2 compliance device; the reasons are information, the
  table is not an essay.
- **base §6 whole** — every sentence is a lever (description precedes language; discontinuous
  authored change; history written backwards; the grammar file is canon).
- **base §7 table's "Transferable lever" column** — each row converts a fact into a decision.
- **amend §1 lines 22–26** (the scale, Halley's split, the zonal languages, the 68-language
  range) — verified against S878; each carries a lever §4 uses. Note: the zonal-language fact
  (Križanić's Common Slavonic) is the one lever with no consequence anywhere in either entry —
  a gap, not a cut.
- **amend:28** the conclusion quote — a cut candidate on length alone, kept because it is the
  only place the article's own generalization extends the move beyond the a priori case to
  "auxiliary and artistic".
- **amend:30–32** calibration and the Eurocentrism hypothesis-test — QUALITY 2, and §4 bullet 3
  uses the latter.
- **amend:56** the cyberleninka location limit — QUALITY 1; I hit the same limitation
  (no page markers in the served HTML).
- **amend §3 lines 60–62, 66** and **§4 all four bullets** — the only content the S880 row
  supports; §4 is the amendment's whole point.

## What I could NOT check

- **S879's printed page numbers** (pp. 28–34): the cyberleninka HTML has no page markers. The
  entry's own (to-verify) is correct and stays.
- **The Sowers-Wills article itself**: not fetched (the amendment records HTTP 429 to both UAs
  on 2026-10-25; I did not re-probe it, so its reachability today is unverified by me).
- **Whether the cuts preserve the entries' downstream use**: no lane document cites a section
  of either entry (`grep -rn 'conlang-scholarship' --include=*.md .` outside the entries shows
  only README topic lines, the lesson, the registry rows and the claim), and README's index
  rows are the `- topic:` text verbatim, which no cut touches — but I did not test any
  consumer beyond that grep.
- **Whether the four cuts are stylistically right** is a judgment I can defend from QUALITY 4,
  not a measurement.
