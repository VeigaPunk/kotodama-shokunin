# Surface map — claim C (ideophones and mimetic vocabulary)

Seat: ScoutSurface · Lane: kotodama · Round 92 · Date: 2026-11-05
Base commit: `21350361500aa000b90f91082bf9d7295a9c24cd`
Freeze commit: `066b9728fc64e78735769c4740d05c1000d31a3b`

All commands run with `cwd = /home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Committed bytes are read via `git show` / `git ls-tree` against the base commit, never
from the working tree. Scratch: `/fast/scratch/hyaku/kotodama-r92/ScoutSurface/`
(base tree materialized at `base-tree/` by `git archive <base> | tar -x` for byte-level
grepping only; it is scratch, not citable evidence).

---

## 0. Base and freeze identity

```
$ git log -1 --format='%H %ad %s' --date=iso 21350361500aa000b90f91082bf9d7295a9c24cd
21350361500aa000b90f91082bf9d7295a9c24cd 2026-11-05 09:25:38 -0300 round-91 verifier spot-check (integrator, hyaku): non-author admit/reject

$ git log -1 --format='%H %ad %s' --date=iso 066b9728fc64e78735769c4740d05c1000d31a3b
066b9728fc64e78735769c4740d05c1000d31a3b 2026-11-05 09:25:38 -0300 round-92: freeze - grader v3 (routed r91 survivors), counter, mutants, controls, evidence S957-S960

$ git diff --stat 21350361500aa000b90f91082bf9d7295a9c24cd 066b9728fc64e78735769c4740d05c1000d31a3b -- corpus/
(no output; rc=0)
```

**Finding.** `corpus/` is byte-identical between base and freeze. The freeze adds only
`reports/round-92/` artifacts. Therefore every base measurement below is also the freeze
measurement.

---

## 1. Filename owners of the three regex classes → expect 0

```
$ git ls-tree -r --name-only 21350361500aa000b90f91082bf9d7295a9c24cd corpus/knowledge \
    | grep -icE '(ideophone|mimetic|onomatopoe)'
0
rc=1   (grep exits 1 on no match; the count printed is 0)
```

Same command over the whole `corpus/` tree (not just `corpus/knowledge`):

```
$ git ls-tree -r --name-only 21350361500aa000b90f91082bf9d7295a9c24cd corpus \
    | grep -icE '(ideophone|mimetic|onomatopoe)'
0
```

Same command at the **freeze** commit (confirms the freeze did not land the entry):

```
$ git ls-tree -r --name-only 066b9728fc64e78735769c4740d05c1000d31a3b corpus/knowledge \
    | grep -icE '(ideophone|mimetic|onomatopoe)'
0
```

**Finding.** 0 filename owners at base and at freeze, over `corpus/knowledge` and over
the whole `corpus/` tree. No dedicated entry file for ideophones, mimetics or
onomatopoeia exists.

Direct object-existence probe (the "surface unmoved" command named in claims.json
`C.surface`):

```
$ git show 21350361500aa000b90f91082bf9d7295a9c24cd:corpus/knowledge/linguistics/ideophones-mimetics.md
fatal: path 'corpus/knowledge/linguistics/ideophones-mimetics.md' does not exist in '21350361500aa000b90f91082bf9d7295a9c24cd'
rc=128

$ git show 066b9728fc64e78735769c4740d05c1000d31a3b:corpus/knowledge/linguistics/ideophones-mimetics.md
fatal: path 'corpus/knowledge/linguistics/ideophones-mimetics.md' does not exist in '066b9728fc64e78735769c4740d05c1000d31a3b'
rc=128
```

---

## 2. Linguistics partition count → expect 36

```
$ git ls-tree -r --name-only 21350361500aa000b90f91082bf9d7295a9c24cd corpus/knowledge/linguistics | wc -l
36
rc=0
```

At freeze: `git ls-tree -r --name-only 066b9728fc64e78735769c4740d05c1000d31a3b corpus/knowledge/linguistics | wc -l` → `36`.

The 36 filenames at base (numbered):

```
 1 color-terminology.md
 2 conlang-methodology.md
 3 conlang-scholarship.amend-2026-10-23.md
 4 conlang-scholarship.md
 5 dialect-register-consistency.md
 6 evidentiality-epistemic-marking.md
 7 gesture-co-speech-pointing.md
 8 historical-linguistics.md
 9 kinship-terminology.md
10 language-contact.md
11 language-shift-obsolescence-revival.md
12 language-socialization-and-acquisition.md
13 linguistic-anthropology.md
14 morphological-typology.md
15 naming-systems.md
16 numerals-and-measures.md
17 orality-formulaic-language.md
18 petitionary-and-votive-formulae.md
19 phonetics-phonology.md
20 politeness-taboo-euphemism.md
21 proverbs-riddles-attestation-solutions.md
22 register-lexicon-ceilings.md
23 register-strata-attestation.md
24 sacred-registers-liturgical-language.md
25 secret-and-ludic-languages.md
26 semantic-fields-lexicon-building.md
27 semantics-pragmatics.md
28 sign-languages-manual-modality.md
29 sociolinguistics-registers.md
30 sound-symbolism.md
31 speech-surrogates-whistled-drummed.md
32 syntax-typology.md
33 taboo-strata-lifecycle.md
34 toponymy-place-names.md
35 translation-protocol-fidelity.md
36 writing-systems.md
```

**Finding.** 36 files at base and at freeze. The partition holds no
ideophone/mimetic/onomatopoeia file. Landing `ideophones-mimetics.md` moves the
partition to **37**, and the `## linguistics/ (N)` README header to 37 (see §5).

---

## 3. Nearest owners — where ideophone-adjacent material lives

### 3a. `corpus/knowledge/linguistics/sound-symbolism.md` (28980 bytes, 155 lines)

Read at base via `git show <base>:corpus/knowledge/linguistics/sound-symbolism.md`.

H2 line map:

```
 21 ## 1. The gap this entry fills — and the three-way map
 42 ## 2. The cross-linguistic bias evidence, calibrated
 74 ## 3. Bouba/kiki — the most robust single effect, with its calibration
 82 ## 4. The frequency code — voice-level symbolism (Ohala 1994)
 88 ## 5. Phonesthemes — systematicity you can plant and police
 99 ## 6. Ideophones — the depictive class (the biggest lever for a mimetic-rich culture)
113 ## 7. Where the coupling pays out (cross-file hooks)
126 ## 8. Calibration shelf (keep this section with any excerpt)
140 ## 9. Decision record (author)
150 ## 10. Handoff notes (lore-shokunin, sibling files)
```

Ideophone-adjacent material, by line:

| line | material |
|---|---|
| 1 | H1 title `# Sound Symbolism — Iconicity, Ideophones, and the Sound–Meaning Interface` — the only H1 in `corpus/knowledge` matching any of the six topic phrases |
| 3 | `- topic:` line already names "ideophones as a depictive word class (Dingemanse 2012, 2018; Japanese mimetics)" and "an ideophone-register design procedure" |
| 11 | source list: Dingemanse 2012 (ideophones, *Language and Linguistics Compass*), Dingemanse 2015 (ideophones and reduplication), Dingemanse 2018 (*Glossa*) |
| 15 | source list: Hamano 1998 *The Sound-Symbolic System of Japanese*; Kita 1997 "Two-dimensional semantic analysis of Japanese mimetics" |
| 18 | `- recheck:` line: "before citing ideophone morphosyntax" |
| 23 | §1 "Gap filled: no committed linguistics entry owned sound symbolism" |
| 27 | §1 bullet: "imitative: onomatopoeia proper (a word copying a sound)" — the onomatopoeia sub-type |
| 38 | §1 table row: `\| mimetic/ideophone stratum \| iconic + conventionalized \| narrative performance, song, insult, praise (→ §6) \|` — the only table row in the partition naming mimetic/ideophone |
| 99 | §6 H2: `## 6. Ideophones — the depictive class (the biggest lever for a mimetic-rich culture)` — the only H2 in `corpus/knowledge` matching any of the six phrases |
| 101 | §6 "What they are (Dingemanse 2012, author-version retrieved)" — depictive word class definition |
| 102 | §6 "Grammar profile (Dingemanse & Akita 2017, title/venue to-verify)" — inverse relation between expressiveness and grammatical integration |
| 103 | §6 "Reduplication as grammar (Dingemanse 2015)" |
| 104 | §6 "Japanese mimetics (Hamano 1998; Kita 1997)" — giongo 擬音語 / gitaigo 擬態語 |
| 105–110 | §6 "Ideophone register design procedure" — 5 steps (Fields / Shapes / Slots / Register politics / Orthography) |
| 111 | §6 "Diachrony" |
| 143, 146–148 | §9 decision record D2/D5/D6/D7 — D7 ships "the ideophone register procedure and phonestheme-bank protocol as the usability deliverable" |
| 153 | §10 pre-canonization recheck list mentions the ideophone to-verify marks |

**Honest boundary for the new entry.** `sound-symbolism.md` is not merely adjacent —
it already holds a **§6 "Ideophones — the depictive class"** section (lines 99–111)
with a class definition, a grammar profile, the Japanese mimetics system, and a
5-step ideophone-register design procedure, plus the Dingemanse 2012/2015/2018,
Hamano 1998 and Kita 1997 citations (lines 11, 15), and its §1 topic line already
advertises "an ideophone-register design procedure" (line 3). Its own D7 (line 147)
calls that procedure "the usability deliverable".

Consequence for the new entry's boundary statement: the entry may claim the
**typological word-class framing, the Cushitic/Ethiosemitic grammar, the sensory
semantics, the acquisition/processing material, and a full design procedure**; it
**cannot** claim the ideophone design procedure as new, nor the Dingemanse/Hamano/
Kita typology as newly sourced — all of those are already held in `sound-symbolism.md`
§6 and its sources block. The claims.json `C.bounds` text already anticipates this
("Does not absorb … the sound-symbolism material already held in sound-symbolism.md
(named as the adjacent owner)").

The one h2 in `corpus/knowledge` matching a topic phrase — `sound-symbolism.md:99` —
is therefore a **material overlap**, not just a mention: the new entry's TOPIC leg
counts phrase anchors in the *new* entry's own headings/table, but a reviewer comparing
the two files will see two "ideophone design procedure" blocks. This is the single
sharpest honesty risk on the surface.

### 3b. `corpus/knowledge/linguistics/register-lexicon-ceilings.md` (36139 bytes, 317 lines)

Read at base via `git show <base>:corpus/knowledge/linguistics/register-lexicon-ceilings.md`.

H2 line map:

```
 22 ## 1. The ceiling, stated as one sentence
 39 ## 2. Why it is a ceiling and not a gap that more coinage closes
 58 ## 3. Measuring the ceiling: the procedure
 81 ## 4. The measurement, worked: the D4 stamp register
151 ## 5. The three dispositions
176 ## 6. The real-world analogues, and what they do and do not show
191 ## 7. Design procedure (build order)
211 ## 8. Decision record — the rules this entry adopts
227 ## 9. Calibration: what is mainstream, what is contested
250 ## 10. Limits of this entry
274 ## 11. Canon boundary and handoff
291 ## 12. Errata (round 33): the absence sweeps in the head block, re-measured
```

Ideophone-adjacent material — **only two lines, both inside §12 Errata**:

| line | material |
|---|---|
| 303 | §12 table row: `` \| `which semantic fields` \| 3 \| `sound-symbolism.md:106`; `register-strata-attestation.md` §13; this entry \| **one pre-existing hit** \| `` |
| 306 | "…fields** carry ideophones\") existed at the round-28 baseline commit `6c0ac448`" |
| 315 | "…corpus, in `sound-symbolism.md`, in the ideophone sense — a different sense from this entry's ceiling sense." |

**Correction to the claims.json `C.surface` wording.** claims.json says
`register-lexicon-ceilings.md` carries a "**mimetic** mention". It does not:

```
$ grep -n -i 'mimetic' corpus/knowledge/linguistics/register-lexicon-ceilings.md
(no output; rc=1)
```

The word "mimetic" has **0** occurrences in that file. Its two occurrences are the
word "**ideophone**" (lines 306, 315), and both are *back-references to
`sound-symbolism.md`* inside a round-33 errata that corrects a false absence sweep
(`X63-F2`). So the real near-owner structure is:

- `sound-symbolism.md` — the substantive owner (22 of the 26 corpus-wide `ideophone`
  occurrences inside `corpus/knowledge`; 28 occurrences corpus-wide including
  `corpus/README.md`);
- `register-lexicon-ceilings.md` — a *mention-only* file, and its two mentions point
  **back at** `sound-symbolism.md`, i.e. it corroborates `sound-symbolism.md` as the
  owner rather than competing with it.

This does not change the claim's conclusion (no dedicated entry owner exists), but the
entry's "gap filled" line must not say "mimetic mention in register-lexicon-ceilings.md"
— that statement would be false on the committed bytes.

### 3c. Third and fourth owners (not named in claims.json `C.surface`)

```
$ grep -rn -i -E '^#{2,3} .*(ideophone|mimetic|onomatopoeia|depictive|expressive|sound-symbol)' corpus/knowledge/
corpus/knowledge/linguistics/sound-symbolism.md:99:## 6. Ideophones — the depictive class …
```

Only one h2/h3 in the whole partition. But table cells also carry the phrases, and two
other linguistics files own the **expressives** sense:

```
corpus/knowledge/linguistics/register-strata-attestation.md:69:| expressives | expresses a state of mind | etiquette; almost no institutional machinery | mourning formulas, thanks, curses |
corpus/knowledge/linguistics/semantics-pragmatics.md:95:| expressives | thank, condole, envy | mourning etiquette; envy taboos |
```

These are the **Searle speech-act class "expressives"**, not ideophone expressiveness —
a different sense. The new entry's `expressive` phrase anchor must be disambiguated
from them explicitly, or a reviewer will read a collision that is not there.

Two synthesis-level neighbours (also not in claims.json `C.surface`):

```
corpus/knowledge/synthesis/myth-to-language-derivation.md:32:| Ideophone / sound imitation | Depictive lexical behavior or imitation of a perceived sound, requiring its own analysis | Chant recruits a conventional sound of splashing | An ideophone is not automatically a sacred word, phonestheme, or divine name |
corpus/knowledge/synthesis/myth-to-language-derivation.md   (also holds 'depictive' and 'sound-symbolic')
corpus/knowledge/myth-symbol/ritual-liminality.md:130  ('mimetic' = Girard's mimetic theory — a third, unrelated sense)
corpus/knowledge/culture-material/music-instrument-lexicon.md:59  ('onomatopoeia' — instrument naming)
```

`myth-to-language-derivation.md:32` is the corpus's existing **classification row** for
ideophones, in a synthesis file (not a linguistics partition file). It already asserts
"An ideophone is not automatically a sacred word, phonestheme, or divine name". A new
entry must place itself relative to that row rather than silently re-derive it.

---

## 4. The six topic phrases in the base corpus — grep counts and files

Phrase list from claims.json `C.topic_phrases`:
`ideophone; mimetic; onomatopoeia; depictive; expressive; sound-symbolic`

### 4a. Whole-corpus file list, case-insensitive, per phrase (`git grep -l -i` at base)

| phrase | files holding it (base) |
|---|---|
| `ideophone` | `corpus/knowledge/linguistics/sound-symbolism.md`; `corpus/knowledge/linguistics/register-lexicon-ceilings.md`; `corpus/knowledge/synthesis/myth-to-language-derivation.md` |
| `mimetic` | `corpus/knowledge/linguistics/sound-symbolism.md`; `corpus/knowledge/myth-symbol/ritual-liminality.md`; `corpus/SOURCES.md` (S863 dance-movement row) |
| `onomatopoeia` | `corpus/knowledge/linguistics/sound-symbolism.md`; `corpus/knowledge/culture-material/music-instrument-lexicon.md` |
| `depictive` | `corpus/knowledge/linguistics/sound-symbolism.md`; `corpus/knowledge/synthesis/myth-to-language-derivation.md` |
| `expressive` | 12 files: `corpus/SOURCES.md`; `corpus/knowledge/civilizations/{akan,hawaii,igbo}.md`; `corpus/knowledge/culture-material/{adornment-body-codes,dance-performance-movement-codes}.md`; `corpus/knowledge/linguistics/{register-strata-attestation,semantics-pragmatics,sound-symbolism}.md`; `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`; `corpus/knowledge/synthesis/{dialect-faction-map-workflow,multi-culture-creole-workshop}.md`; `corpus/lessons/round-5.md`; `corpus/lessons/round-5-sources/13.json` |
| `sound-symbolic` | `corpus/knowledge/linguistics/sound-symbolism.md`; `corpus/knowledge/synthesis/myth-to-language-derivation.md` |

`corpus/README.md` holds one line naming any of the six: line 372, the
`sound-symbolism.md` row. `corpus/lessons/` holds one: `round-5.md` (a round-5
question row, `expressive`).

### 4b. Word-bounded occurrence counts over `corpus/knowledge` (base tree)

```
$ for p in ideophone mimetic onomatopoeia depictive expressive sound-symbolic; do \
    n=$(grep -rIioE "\b$p" corpus/knowledge/ | wc -l); f=$(grep -rIilE "\b$p" corpus/knowledge/ | wc -l); \
    echo "$p: occurrences=$n files=$f"; done
ideophone: occurrences=26 files=3
mimetic: occurrences=11 files=2
onomatopoeia: occurrences=2 files=2
depictive: occurrences=5 files=2
expressive: occurrences=15 files=11
sound-symbolic: occurrences=6 files=2
```

(`mimetic` files=2 inside `corpus/knowledge`; `corpus/SOURCES.md` adds a third file
corpus-wide. `expressive` is the only broadly-distributed phrase — it is ordinary
English, which is why its use as a *sub-topic phrase anchor* carries no
distinctiveness weight on its own.)

### 4c. Dedicated-entry owner check → none

Three independent tests, all negative:

1. **Filename owners**: 0 (§1 above), across `corpus/` and at base and freeze.
2. **H1 owners**: a scan of the H1 of every file under `corpus/knowledge` at base
   matched exactly one file — `corpus/knowledge/linguistics/sound-symbolism.md`
   (`# Sound Symbolism — Iconicity, Ideophones, and the Sound–Meaning Interface`),
   whose owning topic is sound symbolism / iconicity, **not** the ideophone word
   class, and whose `- topic:` line (line 3) frames the entry as "how sound and
   meaning couple non-arbitrarily".
3. **H2/H3 owners**: exactly one heading in the whole partition — `sound-symbolism.md:99`
   `## 6. Ideophones — the depictive class …` — a *section* inside a file owned by a
   different topic (sound symbolism), not a dedicated entry.

**Conclusion.** No dedicated-entry owner exists for ideophones / mimetic vocabulary /
onomatopoeia at base. The topic exists as (a) one section of `sound-symbolism.md`
(§6), (b) one classification row of `synthesis/myth-to-language-derivation.md` (:32),
and (c) scattered mentions in 3+2+2+2+11+2 files. The claim-C coverage gap is real.

### 4d. What the grader's TOPIC leg will actually count

From the freeze-pinned `tools/check-advance-evidence.py` (lines 482–498): the six
phrases are split on `;`, and the phrase anchors are searched **only in the new
entry's own h2 headings and table cells** (`anchor_text = norm(heads) + table rows`),
not in the base corpus. `hit_heads` = headings containing a phrase; `hit_rows` = table
rows containing a phrase; `span = len(hit_heads) + (1 if hit_rows else 0)`.

With `min_topic_phrases = 4` and `min_anchor_span = 3`, the new entry needs **at least
4 of the 6 phrases present in its headings/table, spread across at least 3 distinct
heading/table surfaces**. The base-corpus counts in §4a/§4b are a *surface-map* fact
(what already exists), not a grader input — but they tell the entry author which
phrases are already semantically loaded elsewhere (`expressive` in the Searle sense;
`mimetic` in the Girard sense) and should be disambiguated in the entry text.

---

## 5. `corpus/README.md` at base

```
$ git show 21350361500aa000b90f91082bf9d7295a9c24cd:corpus/README.md
```

### 5a. Linguistics partition row

- Header at **line 344**: `## linguistics/ (36)`
- Rows at **lines 345–378**: **34** `- \`file.md\` — topic` rows inside that section
  (first `color-terminology.md`, last `writing-systems.md`).
- **2 files of the partition have no row inside the `## linguistics/` section**: they are
  listed as *supplemental* rows further down the file, under
  `## Round 73 additions (appended 2026-10-25, hyaku run 7)` at **lines 797–798**:
  `conlang-scholarship.md` and `conlang-scholarship.amend-2026-10-23.md`.
  The index tool attributes those to `linguistics` by ownership.

Verified set difference (README rows in the section vs the tree's filenames):

```
in tree, not listed in README:  conlang-scholarship.amend-2026-10-23.md
                                conlang-scholarship.md
in README, not in tree:         (none)
```

And the index tool's own accounting (run on the materialized base tree):

```
$ python3 -B tools/check-corpus-index.py --root <base-tree>
CORPUS-INDEX: OK files=263 rows=263 findings=0
rc=0
```

with per-part rows:

```
linguistics:    declared=36  files=36  rows=36
myth-symbol:    declared=36  files=36  rows=36
culture-material: declared=43 files=43 rows=43
synthesis:      declared=29  files=29  rows=29
verification:   declared=24  files=24  rows=24
civilizations:  declared=95  files=95  rows=95
```

and the supplemental-ownership list confirming the two conlang-scholarship files are
assigned to `linguistics`:

```
{'filename': 'conlang-scholarship.md', 'owners': ['linguistics']}
{'filename': 'conlang-scholarship.amend-2026-10-23.md', 'owners': ['linguistics']}
```

**So the honest statement of the partition row count is: 36 rows for 36 files — 34 of
them inside the `## linguistics/` section and 2 supplemental rows owned by
`linguistics`.** A naive `grep -c` of the section body alone returns 34 and undercounts
by 2; the tool's own parser returns 36.

### 5b. Is an ideophone entry listed? → No

```
$ grep -c 'ideophones-mimetics' corpus/README.md   (at base)
0
```

```
$ grep -n -i -E 'ideophone|mimetic|depictive|sound-symbolic|onomatopoe' corpus/README.md
372:- `sound-symbolism.md` — how sound and meaning couple non-arbitrarily, … ideophones as a depictive word class (Dingemanse 2012, 2018; Japanese mimetics); plus decision tables, an ideophone-register design pr…
```

Exactly **one** README line mentions any of the six phrases — the `sound-symbolism.md`
row at line 372. No dedicated ideophone entry row exists.

### 5c. Totals and footer at base (what a landing must move)

```
line 759:  Total knowledge entries: 243.        (historical block)
line 974:  Total knowledge entries: 263.        ← live totals line (TOTALS_RE takes the last match)
line 976:  Counts checked 2026-11-05 from the repo root:
line 978:  (total 263 files; directory totals 36/36/43/29/24/95).
```

The live footer is the last `Counts checked` block: date `2026-11-05`, total `263`,
directory totals `36/36/43/29/24/95` in PARTS order
(`linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`).
The header at line 344 is `## linguistics/ (36)`.

A round-92 landing therefore has to move **four** README numbers together or the
index tool fails with `HEADER_DRIFT` / `TOTALS_DRIFT` / `FOOTER_TOTAL` /
`FOOTER_DIR_TOTALS`:

| item | base | lands |
|---|---|---|
| `## linguistics/ (N)` header (line 344) | 36 | 37 |
| `Total knowledge entries:` (line 974) | 263 | 264 |
| footer total (line 978) | 263 | 264 |
| footer directory totals | 36/36/43/29/24/95 | 37/36/43/29/24/95 |
| new `- \`ideophones-mimetics.md\` — <topic>` row | absent | present, topic text verbatim from the entry's `- topic:` line |

The tool compares the README row's topic string to the entry's `- topic:` field
character-for-character (`TOPIC_RE` capture vs row topic, `TOPIC_MISMATCH` on
difference) — the row text must be the entry's topic verbatim, as the historical
revision blocks say ("with the entry's `- topic:` text verbatim").

---

## 6. Registry and lesson state at base (context for the C legs)

```
$ git show <base>:corpus/SOURCES.md | grep -c -E '^ {0,3}\| *S[0-9]+'
880
$ git show <base>:corpus/SOURCES.md | grep -o -E 'S[0-9]{3,}' | sort -u | tail -3
S954
S955
S956
```

880 rows, last id `S956` — matching claims.json `C.before`. The four round-92 sources
`S957`–`S960` are therefore new ids; `C.new_ids_min = 3` is satisfiable.

```
$ git ls-tree -r --name-only <base> corpus/lessons/ | grep -E 'round-(8[5-9]|9[0-9])\.md'
corpus/lessons/round-85.md … corpus/lessons/round-91.md
```

`corpus/lessons/round-91.md` exists at base (it is the `--base-lesson` for the
APPENDONLY leg). `corpus/lessons/round-92.md` **does not exist at base or freeze** —
it must be created by the landing (measure92.py reads it as `--lesson` at lands).

Freeze evidence (all four at the freeze commit, `reports/round-92/evidence/`):

```
S957.pdf  S957.txt   URL typologyatcrossroads.unibo.it/article/view/19369   http 200
S958.pdf  S958.txt   URL typologyatcrossroads.unibo.it/article/view/16393   http 200
S959.pdf  S959.txt   URL typologyatcrossroads.unibo.it/article/view/16466   http 200
S960.html            URL frontiersin.org/articles/10.3389/flang.2026.1785036 http 200
manifest.json
```

Manifest quotes are exactly on-topic for the claim:
S957 "whether or not ideophones make up a clear-cut word class in different languages";
S958 "do they constitute a word class on their own, or should they be subsumed under
another word class"; S959 "complex predicates consisting of an invariant coverb followed
by an inflecting light verb, most commonly the verb alä 'say'".

---

## 7. Summary of the numbers

| # | measure | command | value at base | value at freeze |
|---|---|---|---|---|
| 1 | filename owners `(ideophone\|mimetic\|onomatopoe)` in `corpus/knowledge` | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -icE …` | **0** (rc=1) | **0** |
| 1b | same over whole `corpus/` | same, `corpus` | **0** | — |
| 2 | linguistics partition file count | `git ls-tree -r --name-only <rev> corpus/knowledge/linguistics \| wc -l` | **36** | **36** |
| 3a | nearest owner 1 | `corpus/knowledge/linguistics/sound-symbolism.md` | 155 lines / 28980 bytes; ideophone material at **lines 1, 3, 11, 15, 18, 23, 27, 38, 99–111, 143, 146–148, 153** | — |
| 3b | nearest owner 2 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` | 317 lines / 36139 bytes; ideophone material at **lines 303, 306, 315** only; **0 `mimetic`** | — |
| 4 | six-phrase presence | `git grep -l -i` per phrase | see §4a/§4b | — |
| 4c | dedicated-entry owner | filename + H1 + H2/H3 scans | **none** | — |
| 5a | README linguistics row count | index-tool parser on base tree | declared **36**, files **36**, rows **36** (34 in-section + 2 supplemental owned) | — |
| 5b | README lists an ideophone entry? | `grep -c 'ideophones-mimetics' corpus/README.md` | **0** (absent) | — |
| 5c | README live totals / footer | line 974 / 976 / 978 | `263`; `2026-11-05`; `263 files; 36/36/43/29/24/95` | — |
| 6 | registry rows / last id | `git show <base>:corpus/SOURCES.md` | **880** rows, last id **S956** | — |
| — | index tool on base tree | `python3 -B tools/check-corpus-index.py --root <base-tree>` | `CORPUS-INDEX: OK files=263 rows=263 findings=0`, **rc=0** | — |
| — | entry path at base / freeze | `git show <rev>:corpus/knowledge/linguistics/ideophones-mimetics.md` | **rc=128**, does not exist | **rc=128**, does not exist |

## 8. What could not be measured

- The **lands** surface (the state after the entry lands) does not exist yet — the entry
  is the L1's to integrate. No lands-side numbers are claimed here.
- `corpus/lessons/round-92.md` does not exist at base or freeze, so no gate-line
  measurement was possible for it.
- Whether the 2 supplemental `conlang-scholarship*` rows stay supplemental or are
  folded back into the `## linguistics/` section at lands is an L1 integration
  decision; either form passes the index tool (ownership resolution), but the row
  count must still land at 37 for the partition.

## 9. Tooling

No tools were installed or upgraded for this seat: the work was `git` plumbing plus
the lane's own `python3` (`git archive`/`tar` for the byte-level base tree, and
`tools/check-corpus-index.py` from the lane itself). Nothing was written outside
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-92/w1/stage/ScoutSurface/`
and the seat's report trailer; no git mutation of any kind was performed (read-only
`git log`/`ls-tree`/`show`/`archive`/`diff` only).
