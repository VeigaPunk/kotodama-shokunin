# ScoutFrontier — round 90 w2, coverage + adjacency frontier recon

## Axes and scope

Frozen O = operability; frozen C = coverage. This seat reads only: it does not regrade either
claim, does not re-verify, re-date or repair any registry row, and proposes no freshness claim
(freshness is PAUSED under open L0 `kotodama | round-11` and `round-89`). Production, siblings and
the fleet repo were read-only; the only writes are this report and this seat's stage
`.ufo/waves/round-90/w2/stage/ScoutFrontier/` (two transcripts: `base-surface-transcript.txt`,
`frontier-greps.txt`). No subagent dispatched (leaf seat). No tool installed or updated — nothing
was needed; tools used, all pre-existing: `git 2.56.0` (read-only: `git show`, `git grep`,
`git ls-tree`, `git archive` to a scratch dir, `git diff`, `git log`), `python3 3.14.8`,
`curl 8.23.0` (WALS chapter titles + SIL glossary term pages only), `grep (pi-uu-grep) 0.2.0`.
`jj 0.45.1` was invoked read-only for a description and produced nothing; no jj or git write of any
kind was run. No pacman call.

Base `6b0b86e45ae902331aca75863db380f2991458c4`; lands `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761`;
lane HEAD at measurement `3f56892f29e46cce90996bd126ca3a2e7c7658e7`; freeze
`d0b6f2a7f9cc36272682749a9b047b739406f0c8`. Scratch `/fast/scratch/hyaku/kotodama-r90/ScoutFrontier/`
(extracted base tree, WALS/SIL fetches, a planted index-drift fixture).

---

## 1. Verdict on the base-surface statement of the round-90 entry

**Substance holds; two spellings of the count do not, and the count word is wrong in the frozen
claim. No seat may amend the frozen claim, so this is a report-only observation.**

### 1a. What the base actually carries (measured)

```
$ cd /fast/scratch/hyaku/kotodama-r90/ScoutFrontier/base/corpus/knowledge
$ find . -name '*.md' | grep -Ei '\b(prayer|petition|votive|supplicat)'
   -> 0 filename owners
$ grep -rEin '^#{1,6} .*\b(prayer|petition|votive|supplicat)' . | sort
./civilizations/carthage.md:1:# Carthage — Punic Language, Votive Cult, and Maritime Culture
./civilizations/tibet.md:92:## 5. Symbolic systems and prayer-wheel mantra economies
./myth-symbol/direction-symbolism.md:129:## 8. Orientation of prayer and institutions
./myth-symbol/sacred-topography-pilgrimage.md:1:# Sacred topography and pilgrimage — ... votive economy, ...
./myth-symbol/sacred-topography-pilgrimage.md:74:## 5. The votive economy — the object, the receipt, the token
./synthesis/religion-language-co-evolution.md:1:# Religion–language co-evolution: sacred registers, prayer languages, ...
./synthesis/religion-language-co-evolution.md:64:## 5. Prayer languages: model events and permissions
   -> 7 heading locations in 5 files
```

The same set via git, case-insensitively, at the base commit:

```
$ git grep -niE "^#{1,6} .*\b(prayer|petition|votive|supplicat)" 6b0b86e4 -- corpus/knowledge
   -> 7 lines in 5 files (identical set)
```

Case-sensitive, the same grep prints only 5 lines in 4 files — `carthage.md:1` ("Votive Cult") and
`religion-language-co-evolution.md:64` ("Prayer languages") are capitalised and are missed. That is
the only spelling difference; the file set is the same.

### 1b. The frozen claim's enumeration is right; its count word is not

`reports/round-90/claims.json` `C.surface` enumerates exactly
`carthage.md:1, tibet.md:92, sacred-topography-pilgrimage.md:1 and :74, direction-symbolism.md:129,
religion-language-co-evolution.md:1 and :64` — seven heading locations in **five** files — and calls
them "**six entries**". No measured quantity equals six:

| quantity | measured at base |
|---|---|
| filename owners | 0 |
| files with a heading carrying the surface | **5** |
| heading locations carrying the surface | **7** |
| files matching the looser substring grep (adds `garment-lexicon-crosslinguistic.md` on the substring inside *competition*) | 6 |
| files mentioning the surface anywhere in the body | 88 |

`corpus/README.md` (Round 90 block) repeats "sub-sections of six entries". The landed lesson
`corpus/lessons/round-90.md` says "nine lines in five entries" and names both `competition` false
positives — the lesson's count is the correct one for the command it prints (substring, all heading
levels, case-insensitive: 9 lines / 6 files, of which 5 files topical). Because `claims.json` is
frozen at `d0b6f2a7`, no seat may amend it; the divergence is recorded here for the integrator only.

### 1c. The committed receipt under-reports the headings the claim enumerates

`reports/round-90/base-surface.txt` §"headings naming the surface (word-bounded)" prints the
**case-sensitive** `git grep -nE` result — 5 lines in 4 files — and therefore omits
`carthage.md:1` and `religion-language-co-evolution.md:64`, the two capitalised hits that the frozen
claim does enumerate. Every other number in that receipt reproduces exactly against my
independent recount: filename owners 0; body-mention file count 88 (with `\b`, case-insensitive);
the per-file top-10 body counts 16 / 14 / 12 / 11 / 8 / 8 / 8 / 7 / 6 / 6; partition counts
`knowledge files total: 261`, `linguistics: 34`; registry `865` rows, last id `S941`. So the receipt
is internally consistent and matches the claim's *file list*; only its heading *list* is two lines
short because of case sensitivity.

One more method note on the frozen text: `C.surface` describes the measurement as
"`git show 6b0b86e4:corpus/knowledge` + word-boundary grep". `git show <rev>:corpus/knowledge`
prints a **tree listing** (directory names), not file bodies, so grepping that output cannot yield
heading hits; the receipt's `git grep -nE ... <rev> -- corpus/knowledge` is the form that works.
The substantive results are unaffected — all of them reproduce.

### 1d. The rest of the base-state claim reproduces

| frozen claim | measured |
|---|---|
| "no knowledge filename carries prayer\|petition\|votive\|supplicat (0 owners)" | 0 ✓ |
| "the linguistics partition holds 34 files" (at base) | 34 ✓ |
| "registry 865 rows" (at base) | 865 rows, last id `S941` ✓ |
| "no dedicated entry exists" | no file named for any of the four terms; the only filename owner at HEAD is the new entry itself ✓ |
| unmoved-test `git show <lands>:corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` fails | rc=128 at base ✓, rc=0 at lands ✓ |
| "S942–S948 opened this round; S949 is a retained rejection" | S942–S948 status `mined`, used-by the new entry; S949 `rejected`, used-by the lesson ✓ (8 rows appended, 865 → 873, zero cell changes to older rows) |

### 1e. One adjacency gap inside the entry itself

The entry carries `- topic: - sources: - verified-at: - recheck: - couples:` but **no `- gap filled:`
line**, and it names none of the five base partial owners:

```
$ grep -cE 'carthage|tibet\.md|sacred-topography|direction-symbolism|religion-language' \
    corpus/knowledge/linguistics/petitionary-and-votive-formulae.md
0
```

14 of the 35 linguistics entries carry `- gap filled:`, including the immediate round-89 sibling
`evidentiality-epistemic-marking.md`, whose `gap filled:` states its base state in the entry's own
header. The frozen claim's `C.header_keys` are only `topic/sources/verified-at/recheck`, so the
entry passes its contract — but the base-surface fact therefore lives entirely outside the entry
(in claims.json, the lesson and the README), and a reader of the entry alone cannot see what was
absent before. Worth carrying into the next round's entry template.

Scope note (checked, not assumed): `tools/harness/claims-freshness.py` is the one lane tool that
consumes `- gap filled:` — its topic-owner probe defaults to `fields = ["h1", "topic", "gap
filled"]` — but it is a *freshness*-axis harness and is **not** invoked by
`reports/round-90/measure90.py` (grep for `claims-freshness|freshness` in measure90.py: no hits).
Freshness is PAUSED, so the missing line is not a C failure and this is not a repair proposal; it
is recorded because a future freshness run that probes this topic owner would read that field.

The entry's `- couples:` line
likewise points at `myth-symbol` and `culture-material` by partition only, without naming
`sacred-registers-liturgical-language.md` (whose §5 event table already carries a "Private petition"
row) or `myth-symbol/binding-speech-complex.md` (oath / curse / blessing / name-power), the two
nearest neighbours of the register it builds.

---

## 2. Coverage-map honesty: does README list the new entry with the right counts, and does any
other partition disagree with the tree?

**Yes on both counts, with one stale *dated* block and one in-place heading edit that the
freeze-pinned checker actually requires.**

### 2a. The new entry's row and counts are correct

```
$ python3 -B tools/check-corpus-index.py --root .
CORPUS-INDEX: OK files=262 rows=262 findings=0        (exit 0)
```

```
$ python3 -B tools/check-corpus-index.py --root . --json   (footer_live)
"total": 262, "dir_totals": [35,36,43,29,24,95],
"order": [linguistics, myth-symbol, culture-material, synthesis, verification, civilizations]
```

Independently counted in the tree: `linguistics=35 myth-symbol=36 culture-material=43
synthesis=29 verification=24 civilizations=95`, total **262** — identical to the live footer and to
the README's Round-90 block ("Total knowledge entries: 262 … directory totals 35/36/43/29/24/95").
`## linguistics/ (35)` was moved 34 → 35 by the landing commit, and the row's text is **byte-equal**
to the entry's own `- topic:` line (checked programmatically: `entry topic == readme row` → True).
The row sits in filename order between `orality-formulaic-language.md` and
`phonetics-phonology.md`.

### 2b. No partition disagrees with the tree

All six live headings equal their measured file counts (35/36/43/29/24/95) and the checker reports
`declared == files == rows` for every partition. Note for readers: the heading counts *partition
files*, while the rows are distributed between the canonical `## <partition>/` sections and appended
supplemental blocks — 33 rows sit inside `## linguistics/` (35) because
`conlang-scholarship.md` + `conlang-scholarship.amend-2026-10-23.md` live in the "Round 73
additions" block; likewise 32 in `## myth-symbol/` (36) and 41 in `## culture-material/` (43). The
freeze-pinned checker resolves supplemental rows by design (its own docstring: "selects the last
matching footer and resolves supplemental rows") and returns clean. This is lane convention, not a
defect, but it is the one place a reader can mis-count the tree from the README prose alone.

### 2c. The in-place heading edit was mandatory, and the checker proves it

The landing commit rewrote `## linguistics/ (34)` → `(35)` in place, against the older README
convention that partition headings "stay as filed (append-only: an in-place heading edit would be a
rewrite)". Round 85 already moved to in-place heading correction, and the freeze-pinned checker
*requires* it. Planted control on a scratch copy:

```
# copied corpus/ + tools/ to scratch, then edited the heading 35 -> 34
$ python3 -B idx/tools/check-corpus-index.py --root idx
CORPUS-INDEX: FINDINGS files=262 rows=262 findings=1 ids=HEADER_DRIFT   (exit 1)
$ python3 -B tools/check-corpus-index.py --root .        # real tree
CORPUS-INDEX: OK files=262 rows=262 findings=0                          (exit 0)
```

So the edit was required, not a rewrite of a dated record, and the dated blocks were left untouched.

### 2d. One stale dated block (pre-existing, not introduced by round 90)

The "Round 85 index reconciliation" block's own prose says "the two live partition headings are
corrected to 36 myth-symbol and **42** culture-material files", its footer says "total **258** files;
directory totals 32/36/**42**/29/24/95", and its "Total knowledge entries: 258" — but that same
commit (`76ff0707`) wrote the heading `## culture-material/ (43)`, and the tree at that commit held
**259** files with culture-material = **43** (measured by `git ls-tree -r --name-only 76ff0707
corpus/knowledge`). The round-85 block is off by one on both the total and culture-material, and its
prose contradicts its own heading. The round-90 live footer is correct, and the checker only reads
the last dated footer, so this does not affect any grade. It is a dated record and must not be
edited in place; it is reported, not repaired.

---

## 3. Ranked frontier for the next linguistics partition move

Measured over the whole 262-file tree at HEAD. Each candidate shows zero filename owners and zero
topic-line owners, so the lane does not hold the surface at all.

### F1 (highest) — Negation, standard negation and negative concord

```
$ cd corpus/knowledge
$ find . -name '*.md' | grep -Ei '(negat|concord)'
   -> 0 filename owners
$ grep -rnE '^- topic:.*\b(negation|negative concord|multiple negation|standard negation)\b' . | wc -l
   -> 0 topic-line owners
$ grep -rlEi 'negative concord|multiple negation|double negation' --include='*.md' . | wc -l
   -> 0 files anywhere in the corpus
```

All five topic-line "negat" hits are false friends of a different sense: *carnival polarity*
(calendar-festival-systems), *negative strata* (taboo-strata-lifecycle, channel silence),
*negative control* (label-channel-routing-verification, worked-example-verification), *polarity*
(purity-pollution-boundary-systems). Nothing owns grammatical negation.

Sources verified live for a next entry: WALS ch 112 *Negative Morphemes*, 113 *Symmetric and
Asymmetric Standard Negation*, 114 *Subtypes of Asymmetric Standard Negation*, 115 *Negative
Indefinite Pronouns and Predicate Negation*; SIL glossary `/term/negation` → 200 with a Definition.
None of WALS 112–115 is in the registry (it holds only ch 71, 72, 73, 77, 78).

Adjacency: the entry that just landed makes the negative system its own decision cell — §3 crosses
verb shape with **negation strategy** for the prohibitive (S944, four values over 496 languages),
and §7 requires "the negation in the prohibition is or is not the declarative negator — one cell".
The closest neighbour the partition still does not own.

### F2 — Tense and aspect (TAM)

```
$ find . -name '*.md' | grep -Ei '(tense|aspect|perfective)'
   -> 0 filename owners
$ grep -rnE '^- topic:.*\b(tense|aspect|perfective)\b' .
   -> 4 topic-line hits, all false friends or partial:
      myth-symbol/celestial-symbolism-calendars.md:3   ("aspect-switching" = sun/moon gender)
      myth-symbol/eschatology-world-end-systems.md:3     ("present-tense institutions")
      myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md:9 ("present-tense" discourse)
      verification/index-sweep-verification.md:3         ("present-tense claim")
```

Inside the linguistics partition, tense/aspect survives only as sub-lines of other entries:
`syntax-typology.md:45` (aspect split), `:80` (evidential × tense), `:90`, `:106`;
`morphological-typology.md:48` (ablaut as tense/mood carrier), `:52` (tone carries TAM), `:77`.
No entry owns TAM as a designed system. Sources verified live: WALS ch 65 *Perfective/Imperfective
Aspect*, 66 *The Past Tense*, 67 *The Future Tense*, 68 *The Perfect*, 69 *Position of Tense-Aspect
Affixes*. Adjacency: the landed entry is a *mood* typology with no temporal system attached, and
`synthesis/era-language-staging.md` stages a language across eras without one.

### F3 — Interrogatives and question formation

```
$ find . -name '*.md' | grep -Ei '(interrogat|question)'
   -> 0 filename owners
$ grep -rnE '^- topic:.*\b(interrogative|polar question|question particle|wh-question)\b' . | wc -l
   -> 0 topic-line owners
$ grep -rlEi '\b(interrogative|polar question|question particle)\b' --include='*.md' .
   -> 3 of 262 files: civilizations/igbo.md,
                      linguistics/evidentiality-epistemic-marking.md,
                      synthesis/multi-culture-creole-workshop.md
```

The four topic-line "question" hits are false friends (*which questions* in timekeeping, binding
speech, divination, header conformance). Sources verified live: WALS ch 92 *Position of Polar
Question Particles*, 93 *Position of Interrogative Phrases in Content Questions*, 116 *Polar
Questions*; SIL `/term/question` → 200 with a Definition (question as a directive illocution).
Adjacency: the landed entry defines petition as the illocution "asking a power for something" and
solves the addressee slot; the interrogative is the sibling illocution whose particle/periphrasis
decision mirrors the entry's own precative-particle row (§3, "the negative of a command is a
paradigm of its own").

### F4 (runner-up, not in the top three) — Information structure, topic–focus, anaphora

```
$ find . -name '*.md' | grep -Ei '(anaphor|coreferen|information-struct|topic-focus|deixis)'
   -> 0 filename owners
$ grep -rnE '^- topic:.*\b(anaphor|coreferen|information structure|topic.focus|deixis)\b' . | wc -l
   -> 1 (semantics-pragmatics.md, one clause)
$ grep -rlEi '\b(anaphor|coreferen|information structure|topic.focus)\b' --include='*.md' .
   -> 3 of 262 files: synthesis/conlang-blueprint-template.md:79-80 (a template slot),
                      linguistics/syntax-typology.md:84 (one line), civilizations/ryukyu.md:52 (one row)
```

Sources verified live: SIL `/term/anaphora` → 200 with a Definition, `/term/deixis` → 200;
WALS ch 41/42 (demonstratives). Ranked fourth only because the two source families are thinner
than F1–F3's, and because the blueprint template already carries a topic/focus slot the partition
has not filled.

---

## 4. What is left unresolved

- Whether the frozen `claims.json` "six entries" count word should be re-stated is an integrator
  decision, not a seat's: the file is frozen at `d0b6f2a7` and no seat may amend it. My measurement
  says five topical files / seven heading locations at base, and the lesson already says five.
- The round-85 dated block's off-by-one (§2d) is a dated record; it must not be edited in place and
  is reported for a future reconcile.
- The `- gap filled:` absence in the round-90 entry (§1e) is a template observation for the next
  round; the entry as landed satisfies its frozen `C.header_keys`.
- Freshness is out of scope and untouched: no row was re-verified, re-dated or repaired, and no
  freshness claim is proposed.

## Commands actually run (all read-only, all observed output quoted above)

```
git rev-parse / git log / git show / git grep / git ls-tree / git diff / git archive   # read-only
python3 -B tools/check-corpus-index.py --root .            # exit 0
python3 -B tools/check-corpus-index.py --root . --json     # footer_live 262 / 35-36-43-29-24-95
python3 -B tools/check-readme-revisions.py                 # findings 0, warnings 1 (routed residual)
curl -sS -L https://wals.info/chapter/{41,42,65..69,92,93,112..116}   # titles only
curl -sS -L https://glossary.sil.org/term/{negation,anaphora,deixis,question,...}  # status + Definition
```

Full transcripts: `.ufo/waves/round-90/w2/stage/ScoutFrontier/base-surface-transcript.txt` and
`.ufo/waves/round-90/w2/stage/ScoutFrontier/frontier-greps.txt`.
