# Registry grammar census — kotodama base c285b2a (round 82, w1)

Seat: **ScoutRegistry**. Date: 2026-11-04. Scope: the grammar that claim O's
`tools/check-sources-recheck.py` must parse at the round base. Read-only; nothing under the
lane or the fleet root was written.

## 0. Provenance

The census runs on the base blob, extracted once to scratch and never edited:

```text
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md | wc -l
960
[exit 0]
```

```text
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md | sha256sum
2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263  -
[exit 0]
```

```text
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD
c285b2afb19d4b64320e18df1f55e426bf2d0b0c
[exit 0]
```

The lane's working tree is byte-identical to the base blob (so a round-start run against
`corpus/SOURCES.md` and a run against the base blob are the same input):

```text
$ sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263  /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
[exit 0]
```

Extraction command used for every later probe:

```text
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md > SOURCES.base.md
$ sha256sum SOURCES.base.md
2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263  SOURCES.base.md
```

## 1. Row census

Rows matching the contract pattern `^\s{0,3}\|\s*S\d{3,}\s*\|` — **827 rows**, all of them at column 0:

```text
$ grep -cE "^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|" /fast/scratch/hyaku/kotodama-r82/ScoutRegistry/SOURCES.base.md
827
[exit 0]
```

```text
$ grep -cE "^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|" /fast/scratch/hyaku/kotodama-r82/ScoutRegistry/SOURCES.base.md
827
[exit 0]
```

```text
$ grep -cE "^[[:space:]]+\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|" /fast/scratch/hyaku/kotodama-r82/ScoutRegistry/SOURCES.base.md
0
[exit 1]
```

**Reading.** 827 rows match at 0–3 leading spaces; 827 match at column 0 exactly; **0 rows
carry any leading whitespace**. The indentation tolerance the contract requires (0–3 spaces)
is therefore *unexercised by real lane data* — see §7. `grep -c` exiting 1 on the zero-match
indented sweep is expected (no match, not an error).

Row band: lines 30–859 of the 960-line file, i.e. the `## Registry` section (heading line 26,
header row line 28, separator line 29):

```text
$ grep -nE "^ {0,3}#{1,6} " /fast/scratch/hyaku/kotodama-r82/ScoutRegistry/SOURCES.base.md
1:# SOURCES — where kotodama learns
26:## Registry
860:## Paths
897:## Search log
911:## Leads (unopened)
[exit 0]
```

Only lines 28 and 29 outside the row band begin with `|`, so the fleet checker's E12
(row-shaped source outside `## Registry`) cannot fire on this file:

```text
$ grep -nE '^ {0,3}\|' SOURCES.base.md | grep -vE '\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' | head -10
28:| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
29:|---|---|---|---|---|---|---|---|---|---|---|
```

File hygiene (a parser need not handle tabs or CRLF here):

```text
$ printf "tabs=%s crlf=%s trailsp=%s\n" "$(grep -cP "\t" SOURCES.base.md)" "$(grep -c $'\r' SOURCES.base.md)" "$(grep -cE " +$" SOURCES.base.md)"
tabs=0 crlf=0 trailsp=0
[exit 0]
```

## 2. Column census

One-off parser (`census.py`, reproduced in this stage directory): split the row body on `|`,
strip each cell, count.

```text
$ python3 census.py
rows: 827
first line: 30 last line: 859
cell-count distribution: {11: 827}
rows with cell count != 11: [] count 0
duplicate ids: {}
opened histogram: {'2026-10-19': 47, '2026-10-21': 23, '2026-10-22': 395, '2026-10-23': 210, '2026-10-24': 108, '2026-10-25': 25, '2026-10-27': 12, '2026-10-30': 1, '2026-10-31': 3, '2026-11-01': 3}
recheck histogram: {'180d': 249, '2027-10-22': 42, '2027-10-23': 112, '365d': 392, '90d': 18, 'on-release': 14}
opened not ISO: []
recheck not NNd/ISO/on-release: []
status histogram: {'mined': 732, 'queued': 58, 'rejected': 37}
id min/max: 1 903 distinct: 827 expected span: 903
missing ids in span: [455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474] 76
[exit 0]
```

**Cell count.** Distribution is `{11: 827}` — every single row has exactly 11 cells, none
has 12, none has 10. No row is malformed at base, so claim O's *error path* (exit 2,
`RECHECK-ERROR <detail>`, no traceback) is never triggered by real lane data: it can only be
proven by `--selftest` or by a synthetic registry.

**`opened` column.** 10 distinct values, every one a real ISO date (each parsed by
`datetime.date.fromisoformat`, which rejects impossible days like 2026-02-30):

| opened | rows |
|---|---|
| 2026-10-19 | 47 |
| 2026-10-21 | 23 |
| 2026-10-22 | 395 |
| 2026-10-23 | 210 |
| 2026-10-24 | 108 |
| 2026-10-25 | 25 |
| 2026-10-27 | 12 |
| 2026-10-30 | 1 |
| 2026-10-31 | 3 |
| 2026-11-01 | 3 |

**`recheck` column.** 6 distinct values, all inside the contract's three forms
(`NNd` → opened+N days, ISO date → itself, `on-release` → exempt):

| recheck | form | rows |
|---|---|---|
| 90d | opened+90 | 18 |
| 180d | opened+180 | 249 |
| 365d | opened+365 | 392 |
| 2027-10-22 | ISO | 42 |
| 2027-10-23 | ISO | 112 |
| on-release | exempt | 14 |

`NNd` (659) + ISO (154) + `on-release` (14) = 827. Rows whose `opened` is not ISO: **none**.
Rows whose `recheck` is not `NNd`/ISO/`on-release`: **none**.

Status histogram (irrelevant to the queue but useful when reading a diff): mined 732,
queued 58, rejected 37.

## 3. Duplicate-id and duplicate-URL traps

**Duplicate ids: none.** 827 rows carry 827 distinct ids. Ids span S001–S903, and 76 numbers
in that span are unused (S455–S474 among others) — the registry has holes, so an
implementation that assumes contiguous ids or derives `rows` from `max(id) - min(id) + 1`
reports 903 instead of 827. `rows` must be the parsed-row count.

```text
$ python3 duprec.py
rows: 827
distinct ids: 827 duplicate ids: {}
normalized duplicate-URL groups: 43
  same-scope (supersede/correction pairs, NOT W04): 15
   same-scope: aras.org ['S029', 'S047']
   same-scope: doi.org/10.1017/CBO9781139176132 ['S034', 'S044']
   same-scope: routledge.com/Stone-Age-Economics/Sahlins/p/book/9781138702615 ['S038', 'S045']
   same-scope: press.princeton.edu/books/paperback/9780691084428/foraging-theory ['S039', 'S046']
   same-scope: ich.unesco.org/doc/src/36234-EN.doc ['S159', 'S574']
   same-scope: archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt ['S359', 'S481']
   same-scope: journals.openedition.org/assr/pdf/2480 ['S385', 'S484']
   same-scope: metmuseum.org/art/collection/search/312342 ['S396', 'S487']
   same-scope: metmuseum.org/art/collection/search/318318 ['S399', 'S488']
   same-scope: journals.flvc.org/athanor/article/view/126740`, ['S407', 'S489']
   same-scope: archive.org/download/completeguidetoh00foxduoft/completeguidetoh00foxduoft_djvu.txt ['S413', 'S560']
   same-scope: courtofthelordlyon.scot/blazoning.htm ['S421', 'S562']
   same-scope: heraldikk.no/PDF/GODE%20R%C3%85D%20OM%20NYE%20KOMMUNEV%C3%85PEN.pdf ['S445', 'S567']
   same-scope: britannica.com/topic/Tuareg ['S701', 'S858']
   same-scope: penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf ['S753', 'S776']
  cross-scope (== W04 lines): 28
[exit 0]
```

**URL duplicates are 43 groups, and only 28 of them are W04.** The fleet census flags a
duplicate only when the row's `scope` also differs; the other 15 groups are the lane's
deliberate `supersedes` / correction pairs (same URL, same scope, e.g. S029→S047, S034→S044,
S038→S045, S039→S046). 15 + 28 = 43, which reconciles exactly with the census count below.
For claim O this matters only as a non-goal: the recheck auditor must not dedupe or collapse
rows by URL, or it would drop 15 rows from `rows` and from the cadence computation.

## 4. Round-start fleet census (as instructed)

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	W04	S358 duplicate url ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 across scopes
kotodama	W04	S482 duplicate url periodicos.ufpb.br/index.php/srh/article/view/13999/7921 across scopes
kotodama	W04	S483 duplicate url web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 across scopes
kotodama	W04	S485 duplicate url revistas.usp.br/sankofa/article/view/187402 across scopes
kotodama	W04	S490 duplicate url glottolog.org/resource/languoid/id/kiko1235.json across scopes
kotodama	W04	S561 duplicate url archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt across scopes
kotodama	W04	S564 duplicate url en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm across scopes
kotodama	W04	S565 duplicate url ag.colorado.gov/brands/about-brands across scopes
kotodama	W04	S566 duplicate url collections.vam.ac.uk/item/O1053476 across scopes
kotodama	W04	S569 duplicate url www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm across scopes
kotodama	W04	S570 duplicate url www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf across scopes
kotodama	W04	S571 duplicate url www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf across scopes
kotodama	W04	S572 duplicate url www.icphs2007.de/conference/Papers/1286/1286.pdf across scopes
kotodama	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	W04	S830 duplicate url collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals across scopes
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
[exit 0]
```

Exit status and the code histogram of that output:

```text
$ awk -F"\t" "{print \$2}" <validate output> | sort | uniq -c
      1 ok
      4 W01
     28 W04
[exit 0]
```

Tail (last three lines of the same run):

```text
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

**Answer to the question asked: 28 W04 duplicate-URL warnings for this lane, exit 0, final
line `ok`.** The 4 W01 lines are pre-existing tier-C-mined notes, not this round's business.

## 5. Date boundaries

```text
$ python3 dates.py
earliest opened: 2026-10-19 latest opened: 2026-11-01
as-of 2026-11-04 window 90: due=0 upcoming=18 on-release=14 rows=827
as-of 2027-11-01 window 90: due=813 upcoming=0 on-release=14 rows=827
rows with due_date == 2026-11-04: 0 []
rows with due_date == 2027-11-01: 0 []
distinct due dates: 18
   2027-01-17 7
   2027-01-20 8
   2027-01-22 1
   2027-01-23 2
   2027-04-17 7
   2027-04-20 1
  ...
   2027-04-30 3
   2027-10-19 24
   2027-10-21 23
   2027-10-22 381
   2027-10-23 112
   2027-10-24 6
[exit 0]
```

```text
$ python3 boundary.py   # (boundary probe over the base blob)
NNd rows=659  ISO-recheck rows=154  on-release rows=14  total=827
fleet cadence-line total = NNd + on-release = 673
fleet overdue total at 2027-11-01 = NNd + ISO = 813

as-of / window=90 / due / upcoming / on-release / rows
2026-10-19  0  7  14  827
2026-11-04  0  18  14  827
2027-01-16  0  18  14  827
2027-01-17  7  18  14  827
2027-02-02  18  249  14  827
2027-02-03  18  249  14  827
2027-10-22  695  118  14  827
2027-10-24  813  0  14  827
2027-11-01  813  0  14  827

strict '<' implementation at as-of 2027-01-17: due=0 upcoming=18
rows due exactly on 2026-11-04: 0
rows due exactly on 2027-11-01: 0
distance of latest in-window due date from the 2026-11-04+90d edge: 10 days
[exit 0]
```

**Earliest / latest `opened`:** 2026-10-19 / 2026-11-01.

**Rows due exactly on the two probe dates: 0 and 0.** No row lands on 2026-11-04 and none on
2027-11-01, so neither date can distinguish `<=` from `<` at the *as-of* edge by itself. The
date that does exercise `due_date <= as-of` in real data is **2027-01-17**: 7 rows fall due
exactly there, and an as-of 2027-01-17 run must count them as **due=7** (a `<` implementation
prints due=0 — see the strict-`<` line in the probe above).

**Window edge is not exercised either.** At as-of 2026-11-04 the window closes on 2027-02-02;
the latest in-window due date is 2027-01-23, **10 days inside the edge**. As-of 2027-02-02 and
2027-02-03 both print `18 / 249`, identical, because no row falls due on either date. So the
inclusive upper bound (`due_date <= as-of + window`) cannot be proven from lane data; it must
be built synthetically in `--selftest`.

### 5.1 Independent cross-check: the fleet's own `overdue` mode

My one-off parser is not the only computation of these numbers. `sources-census.sh overdue`
computes the same due-date rule (`due = opened + N days` for `NNd`, ISO dates as themselves,
symbolic cadences exempt) and it must agree with §5 row for row:

```text
$ S=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
$ $S overdue --root /home/vgpnk/Projects/shokunin kotodama --today 2026-11-04 > o1.out 2>&1; echo exit=$?
exit=0
$ awk -F"\t" '{print $2}' o1.out | sort | uniq -c
    673 cadence
$ $S overdue --root /home/vgpnk/Projects/shokunin kotodama --today 2027-11-01 > o2.out 2>&1; echo exit=$?
exit=1
$ awk -F"\t" '{print $2}' o2.out | sort | uniq -c
    673 cadence
    813 overdue
```

(The two id-set files below were built from `o2.out` with
`awk -F'\t' '$2=="overdue"{split($3,a," "); print a[1]}' | sort -u` and the same for
`cadence`.)

```text
$ awk -F"\t" '$2=="overdue"{split($3,a," "); print a[1]}' o2.out | sort -u | wc -l
813
$ awk -F"\t" '$2=="cadence"{split($3,a," "); print a[1]}' o2.out | sort -u | wc -l
673
$ comm -23 od.ids cd.ids | wc -l   # overdue-only ids = ISO-dated rows
154
$ comm -13 od.ids cd.ids | wc -l   # cadence-only ids = on-release rows
14
$ comm -12 od.ids cd.ids | wc -l   # ids in both = NNd rows past due
659
$ awk -F"\t" '$2=="overdue"' o2.out | head -2
kotodama	overdue	S033 288d recheck=90d opened=2026-10-19
kotodama	overdue	S032 288d recheck=90d opened=2026-10-19
$ awk -F"\t" '$2=="cadence"' o2.out | head -2
kotodama	cadence	S001 recheck=on-release opened=2026-10-19
kotodama	cadence	S002 recheck=on-release opened=2026-10-19
```

**Agreement is exact.** At 2027-11-01 the fleet's `overdue` id set is 813 = 154 ISO-dated
rows + 659 `NNd` rows past due, and the only ids it never judges are the 14 `on-release`
rows — identical to my parser's `due=813 / on-release=14`. At 2026-11-04 it reports **zero**
overdue rows (exit 0), identical to my parser's `due=0`. Two independent implementations
produce the same base numbers, which is why §6's target line can be stated as a hard
expectation rather than a guess.

Two shape differences between the two tools, so nobody confuses them: the fleet census prints
a `cadence` line for every `NNd` and `on-release` row regardless of due date (673 lines) and
nothing at all for future-dated ISO rows until they fall due, whereas claim O's tool must
print *one* summary line and only the `DUE` lines; and the fleet census exits 1 when rows are
overdue (2027-11-01) while claim O's contract names exit 2 only for malformed input, leaving a
clean-but-overdue run at exit 0.

## 6. Target output for the new tool at this base

With the contract's own semantics (`due = due_date <= as-of`; `upcoming = as-of < due_date <=
as-of + window`; `on-release` exempt; `rows = rows parsed`), the base registry must produce,
verbatim:

```text
$ python3 tools/check-sources-recheck.py --as-of 2026-11-04
RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows
```

— one line, no `DUE` lines (there are zero due rows), and

```text
$ python3 tools/check-sources-recheck.py --as-of 2027-11-01
RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows
DUE S009 2027-01-17
DUE S012 2027-01-17
... (813 DUE lines total)
```

The 18 upcoming rows at 2026-11-04, for a spot check:

```text
DUE-DATE 2027-01-17: S009 S012 S020 S021 S031 S032 S033   (7)
DUE-DATE 2027-01-20: S084 S104 S105 S106 S107 S142 S157 S163  (8)
DUE-DATE 2027-01-22: S859                               (1)
DUE-DATE 2027-01-23: S860 S875                           (2)
```

**The three buckets do not sum to `rows` at 2026-11-04** (0 + 18 + 14 = 32, not 827): the
remaining 795 rows are past the window and belong to no bucket. That is the contract as
written — `rows` is the parsed-row count, not the sum. An implementer who "fixes" the
arithmetic by adding a fourth "later" bucket, or by making `upcoming` mean "everything not
due", breaks the contract. The selftest should pin one case where
`due + upcoming + on-release < rows` so the distinction survives refactors.

### 6.1 Decisions the contract leaves open (pin them in the tool, then in `--selftest`)

1. **Line order.** The contract sentence names the summary line first and the `DUE` lines
   second ("prints exactly one summary line …, plus one `DUE <id> <iso-date>` line per due
   row"), so summary-first is the defensible reading and a checker will most likely read only
   the first line. Pin that order with a selftest that has ≥ 1 due row.
2. **`DUE` line order among themselves.** Unspecified. Registry (file) order is the only
   deterministic choice that does not require inventing a sort key; `S009` before `S012`
   before `S020` in §6's spot check is file order, not lexical accident.
3. **No status filter.** Rejected and queued rows carry cadences exactly like mined rows — at
   base, 58 queued and 37 rejected rows are in the 827, 25 of those rejects are `365d`, and
   none of them is due at 2026-11-04. Filtering to `status == mined` would print `rows: 732`
   and silently under-report later rounds.
4. **`--as-of` default.** The contract gives defaults for `--registry` and `--window` only.
   Today **in UTC** is the only defensible default (the fleet census's own selftest asserts
   `UTC-date-in-Sao-Paulo`, i.e. the fleet convention is UTC, not local). Document it in
   `--help`; the report and every acceptance run should still pass `--as-of` explicitly, so a
   date rollover cannot change a recorded receipt.
5. **`--registry` relative path.** `corpus/SOURCES.md` is cwd-relative as written; run from
   `tools/` and it is not found. Contract-literal (cwd) is fine, but the selftest must never
   depend on cwd — use temp files with explicit `--registry`.
6. **Exit code for a clean-but-overdue run.** The contract names exit 2 only for malformed
   input, so a run with due rows must still exit 0. (The fleet census exits 1 on overdue —
   do not copy that here.)

## 7. What real data does NOT exercise (mandatory selftest coverage)

Derived from the numbers above; every item is a check the `--selftest` (≥ 8 checks, printing
`SELFTEST: PASS (<n> checks)`) must build synthetically, because the 827 real rows cannot
distinguish a correct implementation from a wrong one:

1. **Indented rows.** Zero rows carry leading whitespace. Must test 0, 1, 2, 3 spaces parse
   and (per the fleet parser's documented rule, "4 or more spaces are indented code and
   ignored") that 4 spaces does not. The contract text only promises 0–3; the 4-space case is
   a decision the tool must make and the report should record.
2. **Malformed row → exit 2.** No real row has ≠ 11 cells. Must test one 10-cell and one
   12-cell row, asserting exit 2, stdout `RECHECK-ERROR <detail>`, and *no traceback* (empty
   stderr, or at minimum no `Traceback (most recent call last)`).
3. **Unparseable cadence → exit 2.** Every real value is valid. Must test e.g. `90 days`,
   `90D`, `2027-13-01`, `never`, `""`.
4. **`due_date == as-of` counts as due.** Real data can test it only at as-of 2027-01-17
   (7 rows); the selftest should assert it on a 1-row fixture so the boundary is explicit.
5. **`due_date == as-of + window` counts as upcoming (inclusive).** No real row is within 10
   days of the edge.
6. **`on-release` never enters due/upcoming**, even when `opened` is far in the past (the 14
   real rows are all recent; a 2020-opened `on-release` row would be the sharp case).
7. **ISO recheck in the past** (e.g. `2020-01-01` with `opened 2019-01-01`) is due at once —
   no real row has an ISO recheck earlier than its opened date plus cadence; all 154 ISO rows
   are future-dated 2027-10-22/23.
8. **Month/leap-year arithmetic.** `opened + NNd` must be calendar arithmetic on real dates,
   not 30-day months: 2026-10-19 + 90 = 2027-01-17 (crosses the year boundary and the short
   months); a leap case (e.g. 2027-12-01 + 90 = 2028-02-29) is unobtainable from lane data.
9. **Empty registry / no rows**: real file always has 827; the tool must decide and pin
   whether `0 due / 0 upcoming / 0 on-release / 0 rows` exits 0 or 2.
10. **`--window 0`**: nothing is upcoming by definition; pin it.

## 8. Post-round delta the L1 can use at the freeze

If claim D appends S904–S906 (and S907 as a `rejected` row, matching how S028/S043/S047 are
kept), the registry becomes 831 rows. All four are opened 2026-11-04, so with a 90d/180d/365d
cadence their due dates are 2027-02-02 / 2027-05-03 / 2027-11-04. A 90d row lands exactly on
the 2026-11-04 window edge (2027-02-02), and `due_date == as-of + window` is **upcoming**, not
due; the other cadences are past the edge entirely. Therefore no new row can raise `due`, and
the post-round run at as-of 2026-11-04 must print:

```text
RECHECK-QUEUE: 0 due / <18 or 18+N> upcoming / <14 or 14+M> on-release / 831 rows
```

where N is the number of new rows given a cadence ≤ 90d (a 90d row lands exactly on the window
edge and is *upcoming*, so N counts it) and M the number of new rows marked `on-release`. Any
other shape — especially `due > 0`, or `rows` ≠ 831 — means the parser dropped, duplicated or
mis-dated a row. This is the cheapest end-to-end check available at the freeze.

## 9. Reproduction

Scripts used (copied into this stage directory, dependency-free Python 3, no network):
`census.py` (§2), `dates.py` (§5), `boundary.py` (§5), `duprec.py` (§3). Raw transcripts in
`raw/` (`01`–`17`). Scratch dir `/fast/scratch/hyaku/kotodama-r82/ScoutRegistry/` is removed
after the stage copy; the base blob is recoverable at any time with the `git show` in §0.
