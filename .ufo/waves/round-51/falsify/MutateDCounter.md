# MutateDCounter — mutation test of claim D's measurement

## Item attacked

Claim **D** (axis: depth) in `reports/round-51/claims.json:13-30`: the pastoralism entry's
section-2 one-owner boundary table grows 11 → 15 data rows, each naming one distinct in-corpus
neighbour by a resolving `path:line` anchor, with the ownership cell supported by the anchored
line. Declared counter: `python3 -B reports/round-51/boundary-count.py`, required output
`rows=15 resolved=15 distinct=15` (exit 0).

The attack is on the **measurement**, not on the prose: one mutation at a time to the landed
entry's four new rows (lines 44–47) and to the counter's own input, then the declared counter
re-run. A mutant is *killed* when the counter's printed line differs from
`rows=15 resolved=15 distinct=15` or its exit code is non-zero.

## Lane moved under the test — read this first

The integrator landed two commits **while this battery was running**:

```
e6b6629  round-51: claim D falsify fixes - row cells trimmed to their anchors, lead sentence
          qualified, section-10 herd-side taboo sentence, couples and anchor list updated
364eeff  round-51: claim C falsify fixes - cells re-scoped to what their sources say, …
```

`e6b6629` rewrites the four new rows' ownership cells and the §2 lead sentence. **The entire
battery was therefore re-run from scratch against the post-fix bytes**, and the report's tables
below are the post-fix results. The pre-fix run is kept as the record of what was found and
what has since been repaired.

| | pre-fix bytes | post-fix bytes (current) |
|---|---|---|
| Commit | `9feb69e` | `364eeff` (D fixed by `e6b6629`) |
| Entry SHA-256 | `5c2e09d04652920ae5c8d2f64c175b871b5b98b3cf7a0327ccfe063390c019d0` | `dfd84ee1b56c7599a46e43c43b664a7d9b807fa61846af68d893232df196fd4c` |
| Counter SHA-256 | `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2` | `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2` (unchanged) |
| Counter reading | `rows=15 resolved=15 distinct=15` exit 0 | `rows=15 resolved=15 distinct=15` exit 0 |

**The mutation verdict set is identical on both byte sets** — every killed and every surviving
mutant keeps the same verdict, the same printed line and the same exit code. Only the
prose-level reading of two ownership cells changed. That is itself the result: the integrator's
fix was a **text** fix to the ownership cells (F6 below), and it left the **instrument**
untouched, so every instrument-level gap this seat found is still open.

## Setup and isolation

| Item | Value |
|---|---|
| Private clone | `/fast/scratch/hyaku/kotodama-r51a3-falsify/MutateDCounter` (`git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin …`) |
| Clone HEAD (final) | `364eeff` |
| `realpath` check | `/fast/scratch/hyaku/kotodama-r51a3-falsify/MutateDCounter` — no symlink into the lane |
| Entry under test | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` |
| Counter under test | `reports/round-51/boundary-count.py` |
| Lane entry SHA-256 | `dfd84ee1b56c7599a46e43c43b664a7d9b807fa61846af68d893232df196fd4c` (byte-identical to the clone) |
| Lane counter SHA-256 | `fb1d5c89d2ed3ea32a699692901fa24fed28020f5a930fc7198e2b62f1b14cc2` (byte-identical to the clone) |

Every mutation was applied to the clone copy only, then the exact pristine bytes were restored
and re-verified by SHA-256 after each run. **All 50 mutation runs report `restore_ok=True`.**
The final lane tree shows `git status --porcelain` → `?? .ufo/waves/round-51/` (this report)
plus the integrator's own in-flight `corpus/SOURCES.md` and C-entry edits, which this seat did
not touch. No file in the lane was edited, created or deleted other than this report; no git
add/commit/stash/checkout was run in the lane; no `jj` command was run anywhere.

Harness scripts left in the clone (not the lane) for reproducibility:
`mutate_harness.py` (M01–M14), `mutate_harness2.py` (X01–X13), `mutate_harness3.py` (Y01–Y08),
`mutate_harness4.py` (Z01–Z12), `mutate_harness5.py` (W01–W03 + base/landed row diff),
`probe_structure.py` (per-row anchor shape), `probe_repair.py` / `probe_repair2.py` (repair
re-test).

**Method note, stated because it changed numbers.** Two harnesses were once run concurrently
against the same clone file, and the two processes raced on the entry bytes. The affected run
is discarded and every battery in this report was re-run **sequentially** against the post-fix
bytes; the sequential results are the ones tabulated. The discarded run had produced
inconsistent "killed" verdicts (e.g. X01/X07/X08 flipping to survived, X09/X11 flipping to
killed) that no single mutation could produce; the sequential run reproduces the pre-fix
verdicts exactly, which confirms the diagnosis.

## Baseline and control runs (post-fix bytes)

```
$ python3 -B reports/round-51/boundary-count.py            # clone
rows=15 resolved=15 distinct=15
exit 0
$ python3 -B reports/round-51/boundary-count.py            # lane, read-only
rows=15 resolved=15 distinct=15
exit 0
```

Base tree `bff83ba` (entry restored from the base blob, counter unchanged):

```
$ git show bff83ba:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md > entry; python3 -B reports/round-51/boundary-count.py
rows=11 resolved=11 distinct=11
exit 0
```

Both ends of the declared before/after hold: 11/11/11 at base, 15/15/15 now. Entry restored
to `dfd84ee1…` immediately after.

**Detector semantics established by probing (important for reading the tables below).**
`boundary-count.py` computes `resolved` as *rows whose every anchor token resolves* and
`distinct` as *distinct resolved targets across all rows*; it returns exit 0 when
`rows == resolved == distinct`, and it prints the numbers regardless. Two consequences:
(a) a **dropped** row prints `rows=14 resolved=14 distinct=14` and **exits 0** — the exit code
alone does not detect a missing row; only the printed line does (confirmed separately:
`--entry /tmp/row14.md` → `rows=14 resolved=14 distinct=14`, exit 0);
(b) the acceptance command in `reports/round-51/separability-manifest.json:16` is
`test "$(python3 -B …)" = 'rows=15 resolved=15 distinct=15'` — a **string** comparison on
stdout, so the printed line is the operative gate, not the exit code. That is the correct
choice, and it is why the mutants below are judged on the printed line.

## Mutation battery 1 — the four new rows and the counter's input (M01–M14)

Each mutation starts from the full pristine entry. Printed line and exit code as returned by
the declared counter.

| ID | Exact mutation | Printed line | Exit | Verdict |
|---|---|---|---|---|
| M01 | drop row 44 (`ritual-liminality.md:63`) from the table | `rows=14 resolved=14 distinct=14` | 0 | **killed** (printed line) |
| M02 | drop row 47 (`numerals-and-measures.md:101`) from the table | `rows=14 resolved=14 distinct=14` | 0 | **killed** (printed line) |
| M03 | row 47 → `ritual-liminality.md:70` (duplicate of row 44's file) | `rows=15 resolved=15 distinct=14` | 1 | **killed** |
| M04 | row 44 → `ritual-liminality.md:1400` (file has 136 lines) | `rows=15 resolved=14 distinct=14` | 1 | **killed** |
| M05 | row 45 anchor loses its backticks | `rows=15 resolved=14 distinct=14` | 1 | **killed** |
| M06 | row 47 → `linguistics/` (knowledge **directory**) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| M07 | row 47 → `civilizations/` (directory already used by row 11) | `rows=15 resolved=15 distinct=14` | 1 | **killed** |
| M08 | row 44 → `` `ritual-liminality.md:63` and `fire-fuel-light.md:37` `` (second neighbour already named by row 8) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| M09 | row 44 → `` `ritual-liminality.md:63` and `calibration-registry.md:35` `` (second, otherwise unused neighbour) | `rows=15 resolved=15 distinct=16` | 1 | **killed** |
| M10 | row 44 → `ritual-liminality.md` (line number stripped, still backticked) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| M11 | row 47 → `linguistics/sign-languages-manual-modality.md:101` (the round's claim-C entry) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| M12 | §5 seam sentence (line 93) `numerals-and-measures.md:101` → `trade-economy-lexicon.md:69` | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| M13 | §10 Shepherd-king row anchor → `fire-fuel-light.md:37` | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| M14 | §2 lead sentence (line 29) deleted | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |

## Mutation battery 2 — anchor-resolution and counter-internal probes (X01–X13, Y01–Y08)

| ID | Exact mutation | Printed line | Exit | Verdict |
|---|---|---|---|---|
| X01 | row 47 → `does-not-exist.md:12` | `rows=15 resolved=14 distinct=14` | 1 | killed |
| X02 | row 47 → `corpus/SOURCES.md:5` (outside `corpus/knowledge`) | `rows=15 resolved=14 distinct=14` | 1 | killed |
| X03 | row 47 → `pastoralism-animal-husbandry.md:47` (**self**-citation) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| X04 | row 44 **cell 2** gains `fire-fuel-light.md:37` (counter reads cell 1 only) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| X05 | row 44 **cell 2** gains `celestial-symbolism-calendars.md:28` | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| X06 | row 47 anchor spelled `linguistics/numerals-and-measures.md:101` (path form) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** (benign — same file) |
| X07 | row 47 anchor `myth-symbol/../linguistics/numerals-and-measures.md:101` (traversal) | `rows=15 resolved=14 distinct=14` | 1 | killed |
| X08 | row 44 → `ritual-liminality.md:0` | `rows=15 resolved=14 distinct=14` | 1 | killed |
| X09 | row 44 → `ritual-liminality.md:60-66` (line **range**) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** (benign — range is legal) |
| X10 | row 44 one backtick holding `ritual-liminality.md:63,celestial-symbolism-calendars.md:28` | `rows=15 resolved=14 distinct=14` | 1 | killed |
| X11 | §5 seam sentence (line 93) gains a second anchor | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| X12 | §10 Shepherd-king row deleted | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| X13 | a 16th §2 row added naming `ritual-liminality.md:70` | `rows=16 resolved=16 distinct=15` | 1 | killed |
| Y01 | row 44 **ownership cell** names `death-afterlife-eschatology.md:20` (unused file) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Y02 | the four new rows moved into §3 (before `## 3.`) | `rows=17 resolved=15 distinct=15` | 1 | killed |
| Y03 | a second `## 2. One-owner boundary` heading inserted before §1 | `rows=0 resolved=0 distinct=0` | 0 | **SURVIVED** (printed line differs → killed by the acceptance string) |
| Y04 | row 44 → `ritual-liminality.md:1` (real file, title line, semantically wrong) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Y05 | row 44 → `ritual-liminality.md:2` (real file, blank line) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Y06 | counter mutated to always print `rows=15 resolved=15 distinct=15` | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** (self-certification) |
| Y07 | counter mutated to hard-wire exit 0 | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Y08 | counter mutated to ignore directory anchors (first attempt, 8-space indent — **did not apply**, no behavioural change) | `rows=15 resolved=15 distinct=15` | 0 | n/a — see Z10 |

Y08 is reported honestly as a **no-op**: the patch string used 8-space indentation while the
source at `reports/round-51/boundary-count.py:46-47` uses 4, so the replacement never matched
and the counter was byte-unchanged. Z10 repeats it correctly.

## Mutation battery 3 — section structure, base-vs-landed drift, and counter internals (Z01–Z12, W01–W03)

| ID | Exact mutation | Printed line | Exit | Verdict |
|---|---|---|---|---|
| Z01 | existing row 33's neighbour → `calendar-festival-systems.md:20` (valid, unused file) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z02 | existing row 33's anchor line numbers → `:60,:80` (same file) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z03 | existing row 35 (cuisine) → `calendar-festival-systems.md:20` | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z04 | row 44 → `` `ritual-liminality.md:63` and `ritual-liminality.md:70` `` (same file, two lines) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z05 | row 45 → `symbolism-synthesis-method.md:40` (real line, different rule) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z06 | row 46 → `celestial-symbolism-calendars.md:86` (real line, different section) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z07 | row 47 → `numerals-and-measures.md:60` (real line, different content) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z08 | row 47 → `sign-languages-manual-modality.md:101` (C entry, basename form) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z09 | entry body cites `corpus/lessons/round-51.md` | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** |
| Z10 | counter mutated to ignore directory anchors (**corrected 4-space patch**) | `rows=15 resolved=14 distinct=14` | 1 | killed → proves the counter *does* rely on the pre-existing `civilizations/` directory row to reach `resolved=15` |
| Z11 | counter mutated to drop the distinct-set check (`return 0 if len(data) == resolved else 1`) | `rows=15 resolved=15 distinct=15` | 0 | **SURVIVED** (the distinct set is not independently enforced by the exit code) |
| Z12 | counter mutated to count the table header as a data row | `rows=17 resolved=15 distinct=15` | 1 | killed |
| W01 | the four new rows moved **after** the `## 3.` heading (so they leave §2) | `rows=11 resolved=11 distinct=11` | 0 | **SURVIVED** (printed line differs → killed by the acceptance string) |
| W02 | §2 heading renamed to `## 2. One-owner boundaries` | *(no stdout)* stderr `BOUNDARY_INPUT_ERROR list.index(x): x not in list` | 2 | killed |
| W03 | the four new rows appended into §10's table | `rows=11 resolved=11 distinct=11` | 0 | **SURVIVED** (printed line differs → killed by the acceptance string) |

**Base-vs-landed §2 table diff (direct check, not via the counter).** Base `bff83ba` has 11 data
rows, landed has 15. Ten base rows are byte-identical in the landed table. One base row is
**not** byte-identical:

```
base:   | `sacred-kingship-mythic-charter.md:65` | the shepherd-king office | the herd ledger that office audits (§10) |
landed: | `sacred-kingship-mythic-charter.md:65` | the shepherd-king office: the ruler as the gods' shepherd, audited by omens and the gods | the herd ledger the shepherd image presupposes (§10); the office and its audit stay there |
```

The **anchor is unchanged** (`sacred-kingship-mythic-charter.md:65` in both), so the neighbour is
kept; only the ownership and boundary cells were rewritten to align with §10. The claim's
sentence "The existing 11 rows keep their neighbours" is therefore satisfied on the anchor,
which is what the counter measures. This is stated as a fact, not scored as a defect.

## Structural probe of the landed table (what the counter can and cannot see)

`probe_structure.py` re-uses the counter's own tokeniser over the landed §2 table
(post-fix bytes):

```
data rows: 15
row  1 (line 33) tokens=1 FILE+LINE  `agrarian-field-system-lexicon.md:56,:62`
row  2 (line 34) tokens=1 FILE+LINE  `hunting-foraging-subsistence.md:36,:116`
row  3 (line 35) tokens=1 FILE+LINE  `cuisine-food-lexicon.md:67,:81,:152`
row  4 (line 36) tokens=1 FILE+LINE  `transport-mobility-lexicon.md:92,:95`
row  5 (line 37) tokens=1 FILE+LINE  `trade-economy-lexicon.md:69`
row  6 (line 38) tokens=1 FILE+LINE  `textile-technology.md:22,:27`
row  7 (line 39) tokens=1 FILE+LINE  `semantic-fields-lexicon-building.md:70,:105`
row  8 (line 40) tokens=1 FILE+LINE  `fire-fuel-light.md:37`
row  9 (line 41) tokens=1 FILE+LINE  `animal-symbolism.md:73,:110`
row 10 (line 42) tokens=1 FILE+LINE  `sacred-kingship-mythic-charter.md:65`
row 11 (line 43) tokens=1 DIRECTORY   `civilizations/`
row 12 (line 44) tokens=1 FILE+LINE  `ritual-liminality.md:63`
row 13 (line 45) tokens=1 FILE+LINE  `symbolism-synthesis-method.md:69`
row 14 (line 46) tokens=1 FILE+LINE  `celestial-symbolism-calendars.md:28`
row 15 (line 47) tokens=1 FILE+LINE  `numerals-and-measures.md:101`

distinct targets: 15
```

Every landed row carries **exactly one** anchor token and exactly one resolved target. The four
new rows (12–15) each carry a `file.md:N` anchor with a line number. Row 11's directory anchor
is pre-existing from base and is outside the four new rows.

## Are the four new rows' ownership cells supported by their anchored lines?

Read directly (not via the counter), on the **post-fix** bytes:

| Row | Anchor | Anchored line says | Ownership cell claims (post-fix) | Supported? |
|---|---|---|---|---|
| 44 | `ritual-liminality.md:63` | `\| calendrical / maintenance \| feed the machine that keeps time \| AztecENOITE rites, Tlacaxipehualiztli gladiatorial sacrifice …; Vedic agnihotra daily milk oblation; aśvamedha year-long royal horse rite (Staal 1983) \| the calendar-owning priesthood's budget \|` | "sacrifice typology, including calendrical rites that consume herd products (the Vedic milk oblation, the royal horse rite)" | **Yes** — both named examples (Vedic milk oblation, royal horse rite) are on line 63 |
| 45 | `symbolism-synthesis-method.md:69` | `- **Prey apologetics**: … An animal taboo implies a rite; write both or neither.` | "the register rule that an animal taboo implies a rite (\"write both or neither\")" | **Yes (repaired)** — the pre-fix cell added "and the symbol grammar that enforces it", a phrase that appears **nowhere** in `symbolism-synthesis-method.md` (`grep -c "symbol grammar"` → 0). `e6b6629` dropped that clause and quoted the rule's own words ("write both or neither"), which *are* on line 69. |
| 46 | `celestial-symbolism-calendars.md:28` | `- Three constraints … (2) **subsistence** — farmers anchor on heliacal risings, sailors on star paths, pastoralists on milky/river figures; (3) **economy of omens** …` | "its design rule that subsistence selects sky figures (it assigns pastoralists milky or river figures)" | **Yes (repaired)** — the pre-fix cell added "and the star calendar", a phrase that appears **nowhere** in `celestial-symbolism-calendars.md` (`grep -c "star calendar"` → 0; the calendar star is §5 at `:86`, the calendar lever at `:29`). `e6b6629` dropped that clause. |
| 47 | `numerals-and-measures.md:101` | `… This entry owns only the *words* — mensural classifiers, counting units (*pair*, *head of cattle*, *dozen*, *score*) …` | "counting words: counting units such as \"head of cattle\", and mensural classifiers" | **Yes** — "head of cattle" and "mensural classifiers" are both on line 101 |

**All four new rows now pass the support check.** The two over-claiming cells found on the
pre-fix bytes were repaired by the integrator's own `e6b6629` before this seat's re-run; the
repair text is recorded in the "Findings" section below as F6 (now closed).

## What the proposed repair closes and what it does not

The build-wave seat `ExecBoundaryCounterControls.md` proposed a two-line repair to
`reports/round-51/boundary-count.py`: require a line number in `FILE_ANCHOR`, and require
`len(set(hits)) == 1` per row. I applied that exact patch to a copy of the counter inside the
clone and re-ran the survivors against it.

```
pristine under CURRENT counter:   rows=15 resolved=15 distinct=15  exit 0
pristine under REPAIRED counter:  rows=15 resolved=15 distinct=15  exit 0
base entry under REPAIRED counter: rows=11 resolved=11 distinct=11 exit 0  (repair preserves the base reading)
```

| Survivor | Current counter | Repaired counter |
|---|---|---|
| M08 second neighbour already named elsewhere | survived | **killed** (`rows=15 resolved=14 distinct=15`, exit 1) |
| M10 line number stripped | survived | **killed** (`rows=15 resolved=14 distinct=14`, exit 1) |
| M06 new row anchored to a directory | survived | **still survives** |
| Z04 same file twice at two lines | survived | **still survives** (both anchors resolve to one target, so `len(set(hits)) == 1` holds) |
| X03 self-citation | survived | **still survives** |
| M11 / Z08 naming the C entry | survived | **still survives** |
| M12 / M14 body and lead-sentence edits | survived | **still survives** (counter never reads them) |

The repair is correct and closes the two false positives the round lesson already records
(`corpus/lessons/round-51.md:107`), but it does not close directory anchors (M06), same-file
double anchors (Z04), or self-citation (X03). Those three need separate handling; none of them
is present in the landed rows.

## Findings

**F1 — medium — the counter accepts a knowledge *directory* as a row's neighbour, so a new row
can be "resolved" without naming a neighbour file.**
`reports/round-51/boundary-count.py:46-47` resolves any token ending in `/` against the
directory index, and the distinct set counts it as a target. Mutant **M06** (row 47 →
`` `linguistics/` ``) prints `rows=15 resolved=15 distinct=15`, exit 0. The claim's wording
("one distinct in-corpus neighbour by a backticked path:line anchor") is stricter than the
counter's grammar. The proposed repair does not close it. As the rows stand, no new row uses a
directory, so this is a **measurement weakness, not a live defect** — but it means the counter
cannot be used as evidence that the four new rows name *files*. Smallest fix: require a
`file.md:N` shape for rows other than the pre-existing group row, or make a directory token
count toward `resolved` only when it is the single known group row.

**F2 — medium — the counter does not enforce the "one neighbour per row" rule, and the proposed
repair does not close every instance.**
Mutants **M08** (second neighbour already named elsewhere) and **Z04** (same file twice) both
print `rows=15 resolved=15 distinct=15`, exit 0. M08 is closed by the proposed repair; Z04 is
not, because both anchors resolve to one target and `len(set(hits)) == 1` still holds. Smallest
fix: extend the repair with a per-row check that the row's token count is exactly one for
non-group rows.

**F3 — medium — a row may cite the entry itself as its own neighbour.**
Mutant **X03** (row 47 → `` `pastoralism-animal-husbandry.md:47` ``) prints
`rows=15 resolved=15 distinct=15`, exit 0. The counter resolves the entry's own path from the
same knowledge index it scans. Not present in the landed rows. Smallest fix: exclude the entry
under test from the resolution index.

**F4 — medium — a new row may name the round's own claim-C entry and the counter will not
object.**
Mutants **M11** (full path) and **Z08** (basename) both print `rows=15 resolved=15 distinct=15`,
exit 0. The claim's `must_not_cite` list names the C entry, and the counter has no knowledge of
it. This is caught one level up — the separability checker does flag it (see below) — so the
overall gate holds, but the counter alone would not. Smallest fix: none needed in the counter if
the separability leg remains mandatory; otherwise add a C-entry exclusion.

**F5 — low — the counter does not read anything outside the §2 table's first cell.**
Mutants **M12** (the §5 numerals seam sentence pointed at an unrelated file), **M14** (the §2
lead sentence deleted), **X11**, **X12**, **X04/X05/Y01** (anchors in the ownership and boundary
cells) all survive. The claim's own falsifier is "any other printed value" plus a review
finding about the anchored line — so body development and ownership-cell wording are review
responsibilities, not counter properties. This is a scope statement, not a defect. Note that
`e6b6629` changed the lead sentence and added a §10 sentence: the counter reads neither, so it
reports 15/15/15 either way.

**F6 — medium (pre-fix) → CLOSED by `e6b6629` — the counter cannot see whether an anchored line
supports its ownership cell, and two ownership cells over-claimed relative to their anchor.**
Mutants **Y04/Y05/Z05/Z06/Z07** (real file, wrong line; real file, blank line) survive, so the
counter is blind to support. On the **pre-fix** bytes, row 45 claimed "and the symbol grammar
that enforces it" (phrase absent from `symbolism-synthesis-method.md`) and row 46 claimed "and
the star calendar" (phrase absent from `celestial-symbolism-calendars.md`). The integrator's
`e6b6629` trimmed both cells to what their anchors say, and the re-run confirms all four rows
now pass. **No live defect remains.** The standing gap is only that the counter cannot detect
this class of defect by itself: the same support error reintroduced in future would pass at
15/15/15. Smallest fix for the standing gap: none in the counter without a semantic check;
this is a review responsibility, as the claim's falsifier already states.

**F7 — low — the counter is self-certifying.**
Mutants **Y06** (counter always prints the required string) and **Y07** (counter hard-wires exit
0) both "pass". The declared acceptance string in `reports/round-51/separability-manifest.json:16`
compares the counter's own output against a constant, so a corrupted counter would satisfy it.
The lane's `reports/round-51/calibration/ruler.py` and `oracle.json` (landed in `5ab3634`,
which `git diff --stat bff83ba 5ab3634` confirms touches only those two paths under
`reports/round-51/calibration/`, no path either claim lands or measures) are the only
independent check available; I did not read that directory (held prior-attempt material per the
lane bounds) and did not exercise the ruler. Smallest fix: none required for D; noted so the
integrator knows the counter's own output is not self-validating.

**F8 — low — the counter's exit code alone does not detect a missing or misplaced row.**
A dropped row prints `rows=14 resolved=14 distinct=14` and exits **0**; an empty §2 prints
`rows=0 resolved=0 distinct=0` and exits **0** (verified with `--entry /tmp/emptyprobe/empty.md`).
The declared acceptance is a stdout string comparison, so the real gate is correct — but any
future consumer that checks only the exit code would miss a dropped row. Smallest fix: none;
recorded as a usage constraint.

**F10 — medium — D's declared acceptance argv is absent from the pre-dispatch receipt, and it
cannot be run pre-dispatch anyway.**
QUALITY criterion 9 (`corpus/QUALITY.md:35`) requires every declared acceptance command to
appear in the pre-dispatch receipt and every receipt command to match a declaration verbatim.
The lane's own final receipt check (`reports/round-51/telemetry/final-measures.txt`, last line)
already reports `MISSING_FROM_RECEIPT ['D', 'C']`. Confirmed here: D's acceptance script is

```
sh -c test "$(python3 -B reports/round-51/boundary-count.py)" = 'rows=15 resolved=15 distinct=15'
```

and that **whole string does not appear in** `reports/round-51/telemetry/declaration-dry-run.txt`;
the receipt runs only the bare `python3 -B reports/round-51/boundary-count.py` and prints
`rows=11 resolved=11 distinct=11`. The receipt contains no "before"/"after"/"expected" naming
and no `rows=15` or `227` string at all. Criterion 9 explicitly allows the pre-landing form
("an after-value comparison failing with the before value printed"), but the receipt does not
use that form either. A second, deeper point: the acceptance argv **cannot** be run
pre-dispatch at all — evaluated against the declaration tree (entry restored to the base
11-row blob), it exits **1**, because the string comparison against `rows=15 resolved=15
distinct=15` fails by construction at declaration time. So this is not a missing receipt line
that could simply be pasted in; the declared command is only meaningful post-landing. Smallest
fix: amend the D acceptance to a form that is runnable on both trees (for example a script that
prints the measured value and a separate post-landing assertion), or amend the receipt to
carry the before-value comparison in criterion 9's named form, and record in the receipt why the
after-value string test is deferred.

**F9 — informational — the four new rows are not independent of each other under the counter.**
Rows 12–15 each name a distinct file in a distinct corpus partition (`myth-symbol/` ×3,
`linguistics/` ×1), so the "distinct=15" figure is not an artefact of one file being reused.
Basenames in `corpus/knowledge` are unique (`find … -printf '%f\n' | sort | uniq -d` → empty),
so no anchor is ambiguous.

## Cross-checks that ran alongside (post-fix bytes)

```
$ python3 -B reports/round-51/boundary-count.py            # lane, read-only
rows=15 resolved=15 distinct=15          exit 0
$ find corpus/knowledge -name '*.md' | wc -l
227
$ python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit 0
```

**D's own forbidden-reference clauses, checked directly against the landed entry (post-fix):**

```
$ grep -oE '\bS0[7-9][0-9]\b|\bS[1-9][0-9][0-9]\b' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
(no output)   # D cites S048–S069 only; no S-id from S071 up
$ grep -n 'sign-languages-manual-modality' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
(no output)   # D does not name the C entry
$ grep -nE 'round-51|corpus/lessons' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
(no output)   # D does not cite the round lesson
```

**F4 cross-checked at the separability level.** With row 47 mutated to name the C entry, the
separability checker does catch the dependency (both spellings):

```
basename form  → SEPARABILITY_DEPENDENCY D->C via acceptance … fails on base+D.lands (rc=1) …  exit 1
full-path form → SEPARABILITY_DEPENDENCY D->C via acceptance … fails on base+D.lands (rc=1) …  exit 1
```

**F6's S-id clause cross-checked at the export level.** With row 44's ownership cell mentioning
`S071`, the separability checker flags it:

```
SEPARABILITY_DEPENDENCY D->C via export '\bS(07[1-9]|0[89]\d|[1-9]\d\d)\b' matched
  corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:44
exit 1
```

**F10 cross-checked against the lane's own receipts.** The lane's
`reports/round-51/telemetry/final-measures.txt` already carries the last line

```
receipt coverage (QUALITY criterion 9 two-way check): declared manifest acceptance argvs present in reports/round-51/telemetry/declaration-dry-run.txt?
MISSING_FROM_RECEIPT ['D', 'C']
```

This seat independently confirmed the D half and additionally showed that D's acceptance argv
**exits 1 when evaluated on the declaration tree**, so it is not runnable pre-dispatch in any
form. The receipt's own `rows=11 resolved=11 distinct=11` line is the before value and is
present; the after-value comparison that criterion 9 names as the acceptable pre-landing form is
not.

## Sources opened

None. This seat tested a local measurement instrument against local bytes; it opened no external
URL, consulted no source row, and made no access-date claim. Every quoted corpus line above was
read from the lane clone on 2026-10-22 and is cited by `path:line`.

## Unrun checks

- The lane's `reports/round-51/calibration/ruler.py` and `oracle.json` were not read or run
  (that directory is held prior-attempt material under this seat's bounds).
- No external source row (S048–S069, S071–S124) was opened; the tier and scope of the four
  new rows' anchors were assessed only against the in-corpus lines they point at.
- No ownership-correctness audit of the four rows' neighbours against the neighbouring entries'
  own boundaries — this seat tested whether the *measurement* can detect a broken row, not
  whether the seams are right.
- No repair to `reports/round-51/boundary-count.py` was landed; the proposed patch was applied
  to a scratch copy inside the clone only, and that copy was deleted afterwards.
- The build wave's own control set was not re-run (it is author-lane material); the two
  false positives it records were independently reproduced here as M08 and M10.
- The pre-fix and post-fix byte sets were each measured in full, but only the **post-fix** set
  is tabulated above; the pre-fix set differs solely in the four ownership cells and the lead
  sentence.

## Verdict

**HOLDS-WITH-FIXES** for claim D's measurement: the **claim's own bytes hold**, but its
**declared acceptance command** does not (F10).

**The claim holds.** The declared count is met and reproducible on the current bytes:
`rows=15 resolved=15 distinct=15`, exit 0, from both the lane (read-only) and a private clone,
against a base that reads `rows=11 resolved=11 distinct=11`. The separability leg reports 0
findings, and D's three forbidden-reference clauses (no C entry, no S-id from S071 up, no round
lesson) hold on the landed bytes, verified directly and by the separability export leg. The
four new rows each carry exactly one `file.md:N` anchor naming a distinct file in a distinct
partition, and each ownership cell is now supported by its anchored line — the two that
over-claimed were repaired by the integrator's `e6b6629` before this seat's re-run.

**The fix that is still needed is F10.** D's declared acceptance argv
(`sh -c test "$(python3 -B reports/round-51/boundary-count.py)" = 'rows=15 resolved=15 distinct=15'`)
does not appear in the pre-dispatch receipt, and — measured here — **cannot be run
pre-dispatch**: evaluated on the declaration tree it exits 1, because a string comparison
against the after-value necessarily fails at declaration time. QUALITY criterion 9 asks for the
after-value comparison "failing with the before value printed"; the receipt prints the before
value from the bare counting command but not in that named form. The lane's own
`reports/round-51/telemetry/final-measures.txt` already flags `MISSING_FROM_RECEIPT ['D','C']`.
Smallest fix: amend the receipt to carry the before-value comparison in criterion 9's form and
state why the after-value string test is deferred, or amend the acceptance to a form runnable
on both trees. This is a records-and-declaration fix, not an entry fix.

**Two standing caveats on the instrument**, neither affecting the claim's count and neither
present in the landed rows. `reports/round-51/boundary-count.py` is a row-counting and
anchor-resolution check, and four classes of one-owner violation pass it at 15/15/15 exit 0 — a
directory anchor (M06), a second neighbour in one row (M08), the same file twice (Z04), and a
self-citation (X03). The build wave's proposed repair closes M08 and M10 but not M06, Z04 or
X03. The claim's own falsifier already routes anchored-line support to non-author review, so
the counter need not carry it; but anyone who treats "15/15/15" as proof of the one-owner
property would be over-reading it.

If the integrator wants the counter's verdict to be evidence for the claim's *wording* rather
than only for its *count*, the counter needs three more conditions (file-anchored rows only,
one target per row, no self-reference) beyond the proposed repair. That is a separate change to
a frozen instrument and is the integrator's call, not this seat's.

**Survivor ledger — every survivor, and which could hide a defect in the landed rows as they
stand now.** 50 mutation runs were executed against the post-fix bytes (49 effective mutants
plus one no-op patch, Y08, reported above). 20 were killed and 30 survived the current counter;
of the 30 survivors, 26 are entry mutations and 4 are counter self-mutations. Every one of them:

| Survivor | Could it hide a defect in the **landed** rows as they stand? |
|---|---|
| M06 directory anchor | **No** — all four new rows are `file.md:N`; probe_structure confirms `kinds=['FILE+LINE']` for rows 12–15. But it means the counter cannot *prove* that. |
| M08 second neighbour | **No** — every landed row carries exactly one anchor token (probe: `tokens=1` for all 15 rows). |
| Z04 same file twice | **No** — same evidence. |
| X03 self-citation | **No** — no landed row names the entry itself. |
| M10 line number stripped | **No** — all 15 landed rows carry a line number except the pre-existing group row 11. |
| M11 / Z08 naming the C entry | **No** — verified absent in the landed bytes; caught by the separability leg when introduced. |
| Z09 citing the round lesson | **No** — verified absent in the landed bytes. |
| M12 / M13 / X11 / X12 body and lead-sentence edits | **No** — the landed body was read line by line and is consistent with its anchors. But the counter reads none of it, so it is review-only territory. |
| M14 lead sentence removed | **No** — the lead sentence is present at line 29, and `e6b6629` qualified it to name the `civilizations/` group row exception. The counter reads it never. |
| X04 / X05 / Y01 anchors outside cell 1 | **No** — the landed rows' ownership and boundary cells carry no backticked file anchors. |
| W01 / W03 structure moves | **No** — the landed §2 table holds 15 rows under the exact `## 2. One-owner boundary` heading. (Y03 is listed as killed above: the duplicate heading makes the counter print `rows=0 resolved=0 distinct=0`, which differs from the required string.) |
| Z01 / Z02 / Z03 existing-row drift | **No** — the base-vs-landed diff shows ten base rows byte-identical and the eleventh keeping its anchor. |
| Y04 / Y05 / Z05 / Z06 / Z07 wrong-but-real line | **No** — all four new rows were re-read against their anchors after the fix and all four now match. This is the class that **did** hide two real defects on the pre-fix bytes (F6), and the fix was textual, so the same blind spot remains open for future edits. |
| Y06 / Y07 / Z11 counter self-mutation | **No** — the counter is unchanged since the declaration commit `1f97472`; `git log --oneline -- reports/round-51/boundary-count.py` shows that commit alone. |
| X06 / X09 benign variants | **No** — a path spelling and a line range are both legal and resolve to the intended file. |
| Y08 no-op patch | Not a mutant — the patch string did not match the source (8-space vs 4-space indent), so the counter was byte-unchanged. Reported for completeness; Z10 repeats it correctly. |

**Bottom line for the integrator:** no mutation found a defect in the landed D rows as they
stand now. The live findings are F10 (D's declared acceptance command is not receipted and is
not runnable pre-dispatch) and the standing instrument caveats F1/F2/F3, which affect what
"15/15/15" can be used to prove but not whether it is true.
