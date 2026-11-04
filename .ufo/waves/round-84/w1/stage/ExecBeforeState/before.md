# ExecBeforeState — red-before receipts for round-84 claims D and O

Wave `kotodama-r84-v1`, milestone `r84-v1`. Measured 2026-11-04T13:34:49Z to 2026-11-04T13:34:51Z UTC.
Base revision `81499ee45b5751d388fefc78583810878de01ecd`; dispatch freeze `3ca2cf288fb593618e0559ea86a36e2dd3110eb8`; lane tip `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` at the start and `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` at the end of the run.
Every base-state claim reads the base tree; the worktree is never the source of a base number.

Machine-readable numbers: `before.json` (same directory). Per-entry stdout/stderr/rc:
`receipts/<id>.stdout`, `.stderr`, `.rc` with `receipts/index.tsv` carrying the normalised command.

`$LANE` = lane repository root, `$STAGE` = this stage directory. No absolute scratch path is cited.

## 0. Provenance of this measurement

Every base-state number below is read from the base tree with `git show` / `git ls-tree` /
`git grep <rev>`, never from the working tree. Worktree-literal readings are labelled `W`/`SW`
and are only a cross-check. `$LANE` is the lane repository root; `$STAGE` is the wave's
`stage/ExecBeforeState` directory. Commands are printed in normalised form.

### P0

```
$ (cd $LANE) git rev-parse HEAD
```

```text
7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2
```

exit 0

### P0b

```
$ (cd $LANE) date -u +%Y-%m-%dT%H:%M:%SZ
```

```text
2026-11-04T13:34:49Z
```

exit 0

### P0c

```
$ (cd $LANE) git log --oneline -3
```

```text
7e6ee2f8 round-84: freeze revision r2 — SOUNDLAW_ERROR shape marker accepts the label constant (fixture-proven, pre-dispatch)
e160a72e round-84: freeze revision r1 — entry section headings aligned to the house shape (pre-dispatch, no claim artifact)
3ca2cf28 round-84: freeze claims, counters and counter library before any claim artifact
```

exit 0

### P0d

```
$ (cd $LANE) git rev-parse HEAD
```

```text
7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2
```

exit 0

### P0e

```
$ (cd $LANE) date -u +%Y-%m-%dT%H:%M:%SZ
```

```text
2026-11-04T13:34:51Z
```

exit 0

### P1

```
$ (cd $LANE) git status --porcelain | wc -l
```

```text
4
```

exit 0

### P1b

```
$ (cd $LANE) git status --porcelain
```

```text
 M reports/round-84/counter-revisions.md
?? .ufo/waves/round-84/
?? corpus/lessons/round-84.md
?? reports/round-84/telemetry/
```

exit 0

### P1c

```
$ (cd $LANE) git rev-list --count 3ca2cf288fb593618e0559ea86a36e2dd3110eb8..HEAD
```

```text
2
```

exit 0

### P2

```
$ (cd $LANE) git status --porcelain -- tools examples corpus SKILL.md reports/round-84 | wc -l
```

```text
3
```

exit 0

### P3

```
$ (cd $LANE) git rev-parse 81499ee45b5751d388fefc78583810878de01ecd
```

```text
81499ee45b5751d388fefc78583810878de01ecd
```

exit 0

### P4

```
$ (cd $LANE) git rev-parse 3ca2cf288fb593618e0559ea86a36e2dd3110eb8
```

```text
3ca2cf288fb593618e0559ea86a36e2dd3110eb8
```

exit 0

### P5

```
$ (cd $LANE) git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:reports/round-84/claims.json
```

_(stdout empty)_

stderr:

```text
fatal: path 'reports/round-84/claims.json' exists on disk, but not in '81499ee45b5751d388fefc78583810878de01ecd'
```

exit 128

### P5b

```
$ (cd $LANE) git rev-parse e160a72e4adf1620e09f812b913d4ece0fcd5243
```

```text
e160a72e4adf1620e09f812b913d4ece0fcd5243
```

exit 0

### P5c

```
$ (cd $LANE) git rev-parse 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2
```

```text
7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2
```

exit 0

### P6

```
$ (cd $LANE) git merge-base --is-ancestor 81499ee45b5751d388fefc78583810878de01ecd HEAD
```

_(stdout empty)_

exit 0

### P7

```
$ (cd $LANE) git merge-base --is-ancestor 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 HEAD
```

_(stdout empty)_

exit 0

### P8

```
$ (cd $LANE) git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- tools examples
```

_(stdout empty)_

exit 0

### P9

```
$ (cd $LANE) git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- SKILL.md
```

_(stdout empty)_

exit 0

## 1. Claim D — knowledge-file census at base

Expected 257 files, all `.md`. `D1d` proves base..HEAD moved no byte under `corpus/knowledge`,
so the base reading and the worktree reading coincide (`D1e`).

### D1a

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep -c "\.md$"
```

```text
257
```

exit 0

### D1b

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
257
```

exit 0

### D1c

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep "\.md$" | cut -d/ -f3 | sort | uniq -c | sort -k2
```

```text
     95 civilizations
     42 culture-material
     32 linguistics
     35 myth-symbol
     29 synthesis
     24 verification
```

exit 0

### D1d

```
$ (cd $LANE) git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- corpus/knowledge
```

_(stdout empty)_

exit 0

### D1e

```
$ (cd $LANE) find $LANE/corpus/knowledge -type f -name "*.md" | wc -l
```

```text
257
```

exit 0

## 2. Claim D — registry-row census at base

`D2a` is the seat's census grammar `^ {0,3}\| *S[0-9]{3,}`. `D2b` is the frozen counter's
`ROW_LINE` (accept-d84.py:39), `D2c` calls the counter's own `knowledge_files` / `registry_rows`
helpers (accept-d84.py:49,52) so the count is not a reimplementation, and `B1` re-runs the
counter's whole `before()` body. `D2e` = 839 = 837 data rows + header + separator.

### D2a

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "^ {0,3}\| *S[0-9]{3,}"
```

```text
837
```

exit 0

### D2b

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "^ {0,3}\| *S[0-9]{3,} *\|"
```

```text
837
```

exit 0

### D2c

```
$ (cd $LANE) python3 -B $STAGE/probe_counter.py $LANE 81499ee45b5751d388fefc78583810878de01ecd
```

```text
KNOWLEDGE_FILES_ACCEPT_D84=257
KNOWLEDGE_NONDOTMD=0
REGISTRY_LINES_MATCHED=837
REGISTRY_ROWS_11CELL=837
REGISTRY_ROWS_MALFORMED=0
ROW_LINE_SOURCE='^ {0,3}\\| *S\\d{3,} *\\|'
OWNED_BASENAMES_CLAIM_RE=none
```

exit 0

### D2d

```
$ (cd $LANE) git diff --stat 81499ee45b5751d388fefc78583810878de01ecd HEAD -- corpus/SOURCES.md
```

_(stdout empty)_

exit 0

### D2e

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "^ *\|"
```

```text
839
```

exit 0

### D2f

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -oE "^ {0,3}\| *S[0-9]{3,}" | grep -oE "S[0-9]+" | sort -V | tail -1
```

```text
S913
```

exit 0

### D2g

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -oE "^ {0,3}\| *S[0-9]{3,}" | grep -oE "S[0-9]+" | sort | uniq -d | wc -l
```

```text
0
```

exit 0

### D2h

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -oE "^ {0,3}\| *S[0-9]{3,}" | grep -oE "S[0-9]+" | sort -V | head -1
```

```text
S001
```

exit 0

### S9

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -E "^ {0,3}\| *S913" | awk -F"|" "{print NF-2}"
```

```text
11
```

exit 0

## 3. Claim D — the four absences (ScoutGapWitch's brief, re-run)

Sweep 1 filename; sweep 2 matter-of-subject; sweep 3 word-boundary occurrence census;
sweep 4 `- gap filled:` lines naming the surface. Controls follow in section 7.

### D3a

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep -icE "witch|witches|witchcraft|sorcer|sorcery|malefic"
```

```text
0
```

exit 1

### D3b

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | grep -iE "witch|witches|witchcraft|sorcer|sorcery|malefic"
```

_(stdout empty)_

exit 1

### D3c

```
$ (cd $LANE) git grep -lE "^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge
```

_(stdout empty)_

exit 1

### D3d

```
$ (cd $LANE) git grep -lE "^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
0
```

exit 0

### D3e

```
$ (cd $LANE) git grep -niE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge
```

```text
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/civilizations/mongol.md:193:- Rubruck is a medieval Franciscan traveler, not a colonial field ethnographer; nevertheless missionary polemic, European categories, interpreter errors, and unequal access shape his report. “Idol,” “devil,” and “witchcraft” are his judgments, not neutral translations.
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/civilizations/yoruba.md:122:- “Mothers” is not simply a generic fertility goddess category. Translate àjẹ́ and related spiritual powers carefully; “witch” can import a demonizing European category rather than explain the local relation.
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/culture-material/hair-grooming-codes.md:39:- Nineteenth-century physicians feared plica polonica, matted hair thought to be the effect of a spell cast by witch or a punishment from God, and believed cutting it would kill the patient (S854)
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4:- gap filled: at the claim base no file under `corpus/knowledge` owns protective objects as a system. Filename sweep `git ls-tree -r --name-only d4795abd corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` → 0; `evil eye`, `nazar`, `mezuz`, `omamori`, `ofuda`, `phylacter` and `witch mark` occur in 0 files (`.ufo/waves/round-59/build/ConnectInLaneAmulets59.md` §1). Partial owners hold single links of the chain (danger, carrier, material, surface, deposition); §2 routes each one-way.
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:39:- A museum leaflet adopts the dictionary sense: an amulet is anything worn about the person as a charm preventative against evil, mischief, disease or witchcraft, and a charm can also be a spell or incantation believed to have a magical power (S644). **B**
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:72:- Correspondence: in the Welsh witch-bottle practice the bottle symbolised the witch's bladder, so the sharp objects sealed in it were believed to cause her pain (S622). **C**
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:102:- Carved into the fabric: witches' marks were a common form of ritual protection in which symbols or patterns were carved into the stonework or woodwork of historic buildings (S621). **B**
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:104:- Sealed vessel: in the witch-bottle practice the bottle symbolised the witch's bladder, and the sharp objects sealed inside it were believed to cause her pain (S622). **C**
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:158:- "Like produces like" as a law: correspondence logic appears in one practice here (the witch bottle) and is reported as a belief; do not promote sympathetic magic to a universal mechanism (contested framework; see `myth-symbol/comparative-frameworks.md`).
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/animal-symbolism.md:9:  - Douglas (1966) Purity and Danger, Routledge; Leach (1964) "Anthropological Aspects of Language: Animal Categories and Verbal Abuse", in Lenneberg ed., New Directions in the Study of Language, MIT Press; Harris (1974) Cows, Pigs, Wars and Witches, Random House and (1985) Good to Eat, Basic; Simoons (1961; 2nd ed. 1994) Eat Not This Flesh, U Wisconsin Press; Evans-Pritchard (1940) The Nuer, Oxford UP; Fortes (1959) Oedipus and Job in West African Religion, Cambridge UP; Evans (1906) The Criminal Prosecution and Capital Punishment of Animals, Hein
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/binding-speech-complex.md:26:  - Qur'an 5:89 (the *kaffāra*, the graded expiation for a broken oath), 2:102 (Hārūt and Mārūt — sorcery taught in Babylon), 89:1 (the oath-opening genre), and 113–114 (the two "protection" sūras); already a corpus source at `../myth-symbol/divination-omen-systems.md` (Qur'an 3:44, 37:141, 5:90).
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/binding-speech-complex.md:164:**5.2 Counter-curse and defense.** Every real curse ecology has defenses, and the defenses are the more interesting half: the *voces magicae* and "barbarous names" whose force is held to lie in the sound rather than the sense (Betz 1986) — a defense that requires knowing the name's *original* form; amulets, apotropaic writing, and threshold deposits (Gager 1992); the counter-curse that returns the imprecation to its sender; and, at the institutional level, **the prohibition**: Qur'an 2:102 and 5:90 place sorcery and divining arrows outside the permitted, which converts the whole channel from a technology into a sin (and the corpus's `./divination-omen-systems.md` §11 calibrates the modern misuse of that material). A culture that criminalizes cursing has not removed the channel; it has made every curse an *accusation*, which is a legal plot.
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/color-symbolism.md:22:| Turner's Ndembu triad (1967) | Ndembu ritual organizes on white (goodness/health/fertility/continuity), red (blood/transition/mediation), black (sorcery/bad death/disease) | Generates polarity *systems*; red as mediator between light/dark poles | A single-culture study; universalizing the triad was the classic overreach of later readers — Turner himself argues Ndembu-specific and answers Turnbull's critique in the same volume (§11) |
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/divination-omen-systems.md:13:  - Evans-Pritchard (1937), *Witchcraft, Oracles and Magic among the Azande*, Oxford UP — the *benge* poison oracle, the second-oracle check, the taboo list, arbitration use; Winch (1964), "Understanding a Primitive Society," *American Philosophical Quarterly* 1(4):307–324; Wilson, ed. (1970), *Rationality*, Blackwell
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/divination-omen-systems.md:112:| What did I do wrong | Ifa; Azande witchcraft diagnosis | a prescription (offer X) | generates the offering economy and the confession scene |
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/myth-folktale-genres.md:54:| 300–749 | Tales of magic (Märchen proper; Propp's corpus) | ATU 300 The Dragon-Slayer; 313 The Magic Flight; 325 The Sorcerer's Apprentice; 330 The Smith and the Devil; 410 Sleeping Beauty; 425C Beauty and the Beast; 440 The Frog King; 480 The Kind and the Unkind Girls; 500 The Name of the Supernatural Helper (Rumpelstiltskin); 510A Cinderella; 510B Donkeyskin / Cap o' Rushes; 545B The Cat as Helper (Puss in Boots); 709 Snow White; 720 The Juniper Tree |
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/myth-ritual-theories.md:12:  - Malinowski (1922), Argonauts of the Western Pacific, and (1926), Myth in Primitive Psychology, Kegan Paul (myth as "social charter"; Trobriand garden magic and Kula); Radcliffe-Brown (1922), The Andaman Islanders, Cambridge UP; Kluckhohn (1944), Navaho Witchcraft, Peabody Museum Papers; Malinowski (1926), Crime and Custom in Savage Society (his own counter to the universal Oedipus)
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/myth-ritual-theories.md:53:- Core claim: myth is not bad science or degraded ritual but a hard-working **social warrant** — it justifies institutions by narrating their origin as precedent. Trobriand material: garden-magic origin stories license land tenure and chiefly rank; Kula myths license exchange partnerships; the charter names names, places, and precedence. Malinowski: "the myth is to the savage what, to a fully believing Christian, is the Biblical tale of Creation" (Myth in Primitive Psychology, 1926 — the register is his; quote with care). Radcliffe-Brown (1922) is the adjacent "myth expresses social structure" line; Kluckhohn (1944) runs it on witchcraft ideology. Bascom's four functions (validation, education, conformity, entertainment) are the tidy descendant (cross-ref comparative-frameworks §1).
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:28:  - **The Ndembu color triad**: white/red/black, each spreading through the whole ritual vocabulary — white mudyi milk = motherhood, matriliny, goodness; red = blood, hunting, womanhood; black = sorcery, badness (Turner 1966).
```

exit 0

### D3f

```
$ (cd $LANE) git grep -niE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
19
```

exit 0

### D3g

```
$ (cd $LANE) git grep -liE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
11
```

exit 0

### D3h

```
$ (cd $LANE) git grep -nE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge
```

```text
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4:- gap filled: at the claim base no file under `corpus/knowledge` owns protective objects as a system. Filename sweep `git ls-tree -r --name-only d4795abd corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` → 0; `evil eye`, `nazar`, `mezuz`, `omamori`, `ofuda`, `phylacter` and `witch mark` occur in 0 files (`.ufo/waves/round-59/build/ConnectInLaneAmulets59.md` §1). Partial owners hold single links of the chain (danger, carrier, material, surface, deposition); §2 routes each one-way.
```

exit 0

### D3i

```
$ (cd $LANE) git grep -nE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
1
```

exit 0

### D3j

```
$ (cd $LANE) git grep -c "^- topic:" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
257
```

exit 0

### D3k

```
$ (cd $LANE) git grep -c "^- gap filled:" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
60
```

exit 0

### D3l

```
$ (cd $LANE) git grep -liE "witch|witchcraft|sorcer|malefic" 81499ee45b5751d388fefc78583810878de01ecd -- corpus reports | wc -l
```

```text
148
```

exit 0

### D3m

```
$ (cd $LANE) git grep -liE "witch|witchcraft|sorcer|malefic" 81499ee45b5751d388fefc78583810878de01ecd -- corpus reports
```

```text
81499ee45b5751d388fefc78583810878de01ecd:corpus/README.md
81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/civilizations/ancestral-puebloan.md
... (148 lines total; full list in receipts/D3m.stdout)
```

exit 0

## 4. Claim D — the same four sweeps in the working tree (brief-literal form)

Cross-check only: `corpus/knowledge` is byte-identical at base, at the freeze and in the
worktree, so these reproduce section 3 exactly.

### W1

```
$ (cd $LANE) find corpus/knowledge -name "*.md" | grep -icE "witch|witches|witchcraft|sorcer|sorcery|malefic"
```

```text
0
```

exit 1

### W2

```
$ (cd $LANE) grep -rlE "^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)" corpus/knowledge | wc -l
```

```text
0
```

exit 0

### W3

```
$ (cd $LANE) grep -rniE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" corpus/knowledge | wc -l
```

```text
19
```

exit 0

### W3b

```
$ (cd $LANE) grep -rliE "\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b" corpus/knowledge | wc -l
```

```text
11
```

exit 0

### W4

```
$ (cd $LANE) grep -rnE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" corpus/knowledge | wc -l
```

```text
1
```

exit 0

## 5. Claim D — entry path absent, and the S914-S917 row space

`D4a` exits 128 (the path does not exist at base); `D4c` confirms it is absent in the
worktree too. `D4b` gives the 35-file sibling partition. `S7`/`S8`/`S9` show S913 is the
last registered id and its row has 11 cells; `S1`-`S6` show the id space above it is empty.

### D4a

```
$ (cd $LANE) git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md
```

_(stdout empty)_

stderr:

```text
fatal: path 'corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md' does not exist in '81499ee45b5751d388fefc78583810878de01ecd'
```

exit 128

### D4b

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge/myth-symbol | wc -l
```

```text
35
```

exit 0

### D4c

```
$ (cd $LANE) test -e $LANE/corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md
```

_(stdout empty)_

exit 1

### D4d

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge/myth-symbol
```

```text
corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
corpus/knowledge/myth-symbol/animal-symbolism.md
corpus/knowledge/myth-symbol/binding-speech-complex.md
corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md
corpus/knowledge/myth-symbol/color-symbolism.md
corpus/knowledge/myth-symbol/comparative-frameworks.md
corpus/knowledge/myth-symbol/cosmology-cosmography.md
corpus/knowledge/myth-symbol/creation-myths-taxonomy.md
corpus/knowledge/myth-symbol/death-afterlife-eschatology.md
corpus/knowledge/myth-symbol/direction-symbolism.md
corpus/knowledge/myth-symbol/divination-omen-systems.md
corpus/knowledge/myth-symbol/eschatology-world-end-systems.md
corpus/knowledge/myth-symbol/flood-traditions.md
corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md
corpus/knowledge/myth-symbol/hero-journey-variants.md
corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
corpus/knowledge/myth-symbol/monsters-hybrid-beings.md
corpus/knowledge/myth-symbol/motif-index-usage.md
corpus/knowledge/myth-symbol/myth-folktale-genres.md
corpus/knowledge/myth-symbol/myth-ritual-theories.md
corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md
corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md
corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
corpus/knowledge/myth-symbol/number-symbolism.md
corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md
corpus/knowledge/myth-symbol/pantheon-archetypes.md
corpus/knowledge/myth-symbol/plant-symbolism.md
corpus/knowledge/myth-symbol/purity-pollution-boundary-systems.md
corpus/knowledge/myth-symbol/ritual-liminality.md
corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md
corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md
corpus/knowledge/myth-symbol/symbolism-synthesis-method.md
corpus/knowledge/myth-symbol/trickster.md
```

exit 0

### S1

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S914 |"
```

```text
0
```

exit 1

### S2

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S915 |"
```

```text
0
```

exit 1

### S3

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S916 |"
```

```text
0
```

exit 1

### S4

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "| S917 |"
```

```text
0
```

exit 1

### S5

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "\| S91[4-7] \|"
```

```text
0
```

exit 1

### S6

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -cE "S91[4-9]|S9[2-9][0-9]"
```

```text
0
```

exit 1

### S7

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -c "S913"
```

```text
1
```

exit 0

### S8

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:corpus/SOURCES.md | grep -E "^ {0,3}\| *S913"
```

```text
| S913 | James George Frazer, *The Golden Bough: A Study of Magic and Religion* (1922 abridged edition) — Project Gutenberg eBook #3623, https://www.gutenberg.org/cache/epub/3623/pg3623.txt — as served 2026-11-04 (HTTP 200 under both the plain and the browser-shaped UA, 2331343 bytes, sha256 065d433f4ce2be211a4eecf538fd2d9dbf04bab9651e78abcb8450c15e875304); same-page Wayback capture 2026-08-14 (https://web.archive.org/web/20260814122123id_/https://www.gutenberg.org/cache/epub/3623/pg3623.txt, status 200, 2331343 decoded bytes, byte-identical to live) — capture record reports/round-82/evidence/reject-golden-bough.txt | book | C | the magic-to-religion-to-science stage law as the work states it, offered and refused as a load-bearing framework | chapter III, "Sympathetic Magic", the passage that makes magic a false science — locator only, no quote: the refusal rests on framework status, never on unquotability, and the located span is recorded in reports/round-82/evidence/reject-golden-bough.txt | supersedes S908 — REJECTED: the unilinear magic-to-religion-to-science stage law is the Frazerian evolutionism QUALITY criterion 2 bars from load-bearing use, and S908 filed that refusal under a lowercase teaches that the contract does not spell as REJECTED:, with no superseding row to carry the flip; flip: re-open only for a chapter-scoped admission filed tier C with framework-discredited written into the row scope, or for a modern critical historiography that carries the chapter without the stage law | rejected | 2026-11-04 | 365d | — |
```

exit 0

### SW1

```
$ (cd $LANE) grep -c "| S914 |" corpus/SOURCES.md
```

```text
0
```

exit 1

### SW2

```
$ (cd $LANE) grep -c "| S915 |" corpus/SOURCES.md
```

```text
0
```

exit 1

### SW3

```
$ (cd $LANE) grep -c "| S916 |" corpus/SOURCES.md
```

```text
0
```

exit 1

### SW4

```
$ (cd $LANE) grep -c "| S917 |" corpus/SOURCES.md
```

```text
0
```

exit 1

### SW5

```
$ (cd $LANE) grep -cE "\| S91[4-7] \|" corpus/SOURCES.md
```

```text
0
```

exit 1

## 6. Claim O — tool, marker and example absence at base

`O1a`/`O1b` are the frozen name sweep (0). `O1g`-`O1j` are content-level context: at base
10 tool files and 11 example files mention sound laws in phonology prose, but none applies
one; neither the tool nor the `SOUNDLAWS` marker exists. `O2b`/`O2c` show the marker exists
only at the freeze, in the two round-84 report files. `O3a`/`O3c` show `examples/sound-laws`
is absent; `O3f` shows the only neighbouring tool (`check-craft-exercise.py`) is present.

### O1a

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools examples | grep -ciE "sound.?law|soundchange"
```

```text
0
```

exit 1

### O1b

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools examples | grep -iE "sound.?law|soundchange"
```

_(stdout empty)_

exit 1

### O1c

```
$ (cd $LANE) git grep -liE "sound.?law|soundchange" 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- reports | wc -l
```

```text
56
```

exit 0

### O1d

```
$ (cd $LANE) git grep -liE "sound.?law|soundchange" 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- reports
```

```text
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-10/drift/shard-05.md
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-10/validation.json
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-11/depth/review-23.md
... (56 lines total; full list in receipts/O1d.stdout)
```

exit 0

### O1e

```
$ (cd $LANE) git grep -li "sound" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
162
```

exit 0

### O1f

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools examples | wc -l
```

```text
430
```

exit 0

### O1g

```
$ (cd $LANE) git grep -liE "sound.?law|soundchange" 81499ee45b5751d388fefc78583810878de01ecd -- tools | wc -l
```

```text
10
```

exit 0

### O1h

```
$ (cd $LANE) git grep -liE "sound.?law|soundchange" 81499ee45b5751d388fefc78583810878de01ecd -- tools examples
```

```text
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d2/components/01-brief.yml
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d2/components/06-pantheon.yml
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d2/components/15-pragmatics.yml
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d2/reviews/01-brief.md
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d3/handoff.md
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d3/packet.gates.yml
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d3/packet.json
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d4/components/01-brief.yml
81499ee45b5751d388fefc78583810878de01ecd:examples/culture-d4/components/02-phonology.yml
81499ee45b5751d388fefc78583810878de01ecd:examples/handoff-packet.sample.md
81499ee45b5751d388fefc78583810878de01ecd:examples/handoff-packet.sample.yml
81499ee45b5751d388fefc78583810878de01ecd:tools/assemble-culture-d3.py
81499ee45b5751d388fefc78583810878de01ecd:tools/exercise-handoff-e2e.py
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/expected/d4-assembly-check-gate/r19-pre/examples/culture-d4/components/01-brief.yml
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/expected/d4-assembly-check-gate/r19-pre/examples/culture-d4/components/02-phonology.yml
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/frozen/handoff-packet-check/r18-post/packet.md
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/frozen/handoff-packet-check/r9-pre/packet.md
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/frozen/provenance-audit/r18-post/inputs/corpus/knowledge/verification/verification-method-overview.md
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/frozen/provenance-audit/r9-pre/inputs/corpus/knowledge/verification/verification-method-overview.md
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/frozen/round-22/d4-repin/inputs/examples/culture-d4/components/01-brief.yml
81499ee45b5751d388fefc78583810878de01ecd:tools/gates/frozen/round-22/d4-repin/inputs/examples/culture-d4/components/02-phonology.yml
```

exit 0

### O1i

```
$ (cd $LANE) git grep -liE "sound.?law" 81499ee45b5751d388fefc78583810878de01ecd -- examples | wc -l
```

```text
11
```

exit 0

### O1j

```
$ (cd $LANE) git grep -liE "sound.?law|soundchange" 81499ee45b5751d388fefc78583810878de01ecd -- reports | wc -l
```

```text
54
```

exit 0

### O2a

```
$ (cd $LANE) git grep -c SOUNDLAWS 81499ee45b5751d388fefc78583810878de01ecd -- tools examples reports
```

_(stdout empty)_

exit 1

### O2b

```
$ (cd $LANE) git grep -c SOUNDLAWS 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- tools examples reports
```

```text
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/accept-o84.py:3
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/claims.json:3
```

exit 0

### O2c

```
$ (cd $LANE) git grep -l SOUNDLAWS 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 -- tools examples reports
```

```text
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/accept-o84.py
3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/claims.json
```

exit 0

### O2d

```
$ (cd $LANE) git grep -c SOUNDLAW_ERROR 81499ee45b5751d388fefc78583810878de01ecd -- tools examples reports
```

_(stdout empty)_

exit 1

### O3a

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- examples/sound-laws | wc -l
```

```text
0
```

exit 0

### O3b

```
$ (cd $LANE) git ls-tree --name-only 81499ee45b5751d388fefc78583810878de01ecd:examples
```

```text
culture-d2
culture-d3
culture-d4
handoff-packet.sample.md
handoff-packet.sample.yml
supplement-opencode-1
```

exit 0

### O3c

```
$ (cd $LANE) git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:examples/sound-laws
```

_(stdout empty)_

stderr:

```text
fatal: path 'examples/sound-laws' does not exist in '81499ee45b5751d388fefc78583810878de01ecd'
```

exit 128

### O3d

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- examples | wc -l
```

```text
68
```

exit 0

### O3e

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- examples | cut -d/ -f2 | sort -u
```

```text
culture-d2
culture-d3
culture-d4
handoff-packet.sample.md
handoff-packet.sample.yml
supplement-opencode-1
```

exit 0

### O3f

```
$ (cd $LANE) git cat-file -e 81499ee45b5751d388fefc78583810878de01ecd:tools/check-craft-exercise.py
```

_(stdout empty)_

exit 0

### O4c

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools | wc -l
```

```text
362
```

exit 0

### O4d

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- reports | grep -cE "^reports/round-[^/]+/accept-[^/]+\.py$"
```

```text
61
```

exit 0

### O4e

```
$ (cd $LANE) git show 81499ee45b5751d388fefc78583810878de01ecd:SKILL.md | grep -cE "^ {0,3}\|"
```

```text
246
```

exit 0

### O4f

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- tools | grep -cE "^tools/[^/]+\.py$"
```

```text
30
```

exit 0

### O4h

```
$ (cd $LANE) git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- reports | grep -cE "^reports/round-84/"
```

```text
0
```

exit 1

## 7. Claim O — gate registry at base and at the lane tip

`O4g` is the base reading and matches claim O's `before` sentence exactly. `O4a` is the
lane tip (`P0`), materialised from committed bytes so a concurrent write cannot skew it;
`O4b` is the live worktree and is byte-identical (`gate_worktree_equals_materialised_tip`).
The two tip MISSING lines are exactly the two round-84 counters, which have no SKILL.md row yet.

### O4g

```
$ (cd $STAGE/base) python3 -B tools/check-gate-registry.py --root .
```

```text
GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead
GATE-REGISTRY-INFO: 25 tools without a row
```

exit 0

### O4a

```
$ (cd $STAGE/head) python3 -B tools/check-gate-registry.py --root .
```

```text
GATE-REGISTRY: 2 missing / 74 registered / 63 instruments / 0 dead
MISSING reports/round-84/accept-d84.py
MISSING reports/round-84/accept-o84.py
GATE-REGISTRY-INFO: 25 tools without a row
```

exit 1

### O4b

```
$ (cd $LANE) python3 -B tools/check-gate-registry.py --root .
```

```text
GATE-REGISTRY: 2 missing / 74 registered / 63 instruments / 0 dead
MISSING reports/round-84/accept-d84.py
MISSING reports/round-84/accept-o84.py
GATE-REGISTRY-INFO: 25 tools without a row
```

exit 1

## 8. The frozen BEFORE legs, recomputed with the counters' own helpers

`B1` imports `reports/round-84/accept-d84.py` at the tip and replays its `before()` body
(lines 106-127) plus `accept-o84.py`'s `before()` body (lines 104-109) against the base tree.
Both legs are green before any claim artifact exists: that is the red-before the counters need.

### B1

```
$ (cd $LANE) python3 -B $STAGE/probe_before_legs.py $LANE 81499ee45b5751d388fefc78583810878de01ecd
```

```text
D_BEFORE_OK=True
D_entry_at_base=False
D_knowledge_files=257 frozen=257
D_registry_rows_11cell=837 frozen=837
D_owned_basenames=none
D_surface_re='(?i)\\b(witch|witches|witchcraft|sorcer[a-z]*|malefic[a-z]*)\\b'
O_BEFORE_OK=True
O_tool_at_base=False
O_example_files=0
O_marker_files=0 
O_shape_markers=['SOUNDLAW_ERROR:', '--selftest', 'def main(']
```

exit 0

## 9. Instrument validity

A zero from a dead instrument is worthless, so each absence has a positive control or a
regex-semantics probe. `V1`/`V2` prove `\b` is a real word boundary in this grep; `V3` shows
57 knowledge files contain the substring `switch`, which an unanchored `witch` pattern would
wrongly match; `V4` shows the scout's gap-filled pattern matches inside longer words;
`V5`-`V7` show the single gap-filled hit survives a word-boundary variant, so only a reading
of the line (not a stricter regex) separates it from an ownership claim.

### V1

```
$ (cd $STAGE) printf "%s\n" sandwich switch bewitched | grep -cE "\bwitch\b"
```

```text
0
```

exit 1

### V2

```
$ (cd $STAGE) printf "%s\n" "a witch" "witches" | grep -cE "\bwitch\b"
```

```text
1
```

exit 0

### V3

```
$ (cd $LANE) git grep -c "switch" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
57
```

exit 0

### V4

```
$ (cd $LANE) printf "%s\n" "witch mark" "witchcraft" "sorcery" | grep -cE "(witch|witchcraft|sorcer|sorcery|malefic)"
```

```text
3
```

exit 0

### V5

```
$ (cd $LANE) git grep -cE "^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge
```

```text
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:1
```

exit 0

### V6

```
$ (cd $LANE) git grep -nE "^- gap filled:.*\b(witch|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge
```

```text
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4:- gap filled: at the claim base no file under `corpus/knowledge` owns protective objects as a system. Filename sweep `git ls-tree -r --name-only d4795abd corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` → 0; `evil eye`, `nazar`, `mezuz`, `omamori`, `ofuda`, `phylacter` and `witch mark` occur in 0 files (`.ufo/waves/round-59/build/ConnectInLaneAmulets59.md` §1). Partial owners hold single links of the chain (danger, carrier, material, surface, deposition); §2 routes each one-way.
```

exit 0

### V7

```
$ (cd $LANE) git grep -nE "^- gap filled:.*\b(witch|witchcraft|sorcerer|sorcery|malefic)\b" 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge | wc -l
```

```text
1
```

exit 0

## 10. Freeze revisions and contract-versus-counter

The dispatch names `3ca2cf28` as the freeze; the lane has since advanced it twice, before
dispatch (`X17`), and the tip is `7e6ee2f8` (`P0`). `X4`/`X5` show claim D's two graded
headings changed between them; `X6` shows claim O's `SOUNDLAWS` marker lost its colon;
`X8`/`X7` show the new `semantics` and `min_trace_columns` fields are read by nothing in the
counter. `X2` shows the counter executes `--selftest` while the frozen tool contract's
canonical spelling is `selftest`.

### X4

```
$ (cd $LANE) git show 3ca2cf288fb593618e0559ea86a36e2dd3110eb8:reports/round-84/claims.json | grep -n "decision_heading\|\"anchors_heading\""
```

```text
23:    "decision_heading": "## 2. The decision table",
25:    "anchors_heading": "## 4. Attested anchors",
```

exit 0

### X5

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "decision_heading\|\"anchors_heading\""
```

```text
23:    "decision_heading": "## 2. Six design decisions",
25:    "anchors_heading": "## 3. Attested anchors",
```

exit 0

### X6

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "\"shape_markers\"" -A 4
```

```text
102:    "shape_markers": [
103-     "SOUNDLAW_ERROR",
104-     "--selftest",
105-     "def main("
106-    ],
```

exit 0

### X1

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -c "\-\-selftest"
```

```text
2
```

stderr:

```text
grep: warning: stray \ before -
```

exit 0

### X2

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | grep -n "\"--selftest\""
```

```text
117:        rc, out, err = C.run_py(os.path.join(tree, tool), ["--selftest"], cwd=tree)
```

exit 0

### X3

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | grep -n "SOUNDLAW_ERROR"
```

```text
18:  NEGATIVE    three malformed inputs each exit 2 with a SOUNDLAW_ERROR label and
176:            if rc != 2 or "SOUNDLAW_ERROR:" not in err or "Traceback" in err:
```

exit 0

### X7

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | grep -c "min_trace_columns\|semantics"
```

```text
0
```

exit 1

### X8

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "min_trace_columns\|\"semantics\""
```

```text
100:    "semantics": "A segment is one whitespace-delimited token in the input TSV and in a rule field. A rule's `from` is exactly one segment; `to` is zero or more segments written space-separated ('' deletes). `pre`/`post` are segment lists; '#' is allowed only as the first element of `pre` (the word start) or the last element of `post` (the word end). Rules apply in file order; each rule is one left-to-right non-overlapping pass over the current word. A trace line is `gloss<TAB>index<TAB>rule<TAB>word-before<TAB>word-after`, index the matched position before the change, words space-joined segments.",
101:    "min_trace_columns": 5,
```

exit 0

### X9

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-d84.py | grep -n "SID = \|ROW_LINE = \|LINT_SUMMARY = "
```

```text
38:SID = re.compile(r"\bS\d{3,}\b")
39:ROW_LINE = re.compile(r"^ {0,3}\| *S\d{3,} *\|")
40:LINT_SUMMARY = re.compile(r"^CITED-LINES: (\d+) finding")
```

exit 0

### X10

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-d84.py | sed -n "163,180p"
```

```text
            if len(found) != 1 or found[0] in bad:
                bad.append(line[:60])
                continue
            bullets += 1
            ids.add(found[0])
        ok = (len(bad) == 0 and bullets >= block["min_anchors"] and len(ids) >= block["min_distinct_ids"])
        return ok, "bullets=%d/%d ids=%d/%d malformed=%d" % (
            bullets, block["min_anchors"], len(ids), block["min_distinct_ids"], len(bad))

    def lint():
        rc, out, err = C.run_py(os.path.join(tree, block["cited_lines_tool"]), [entry], cwd=tree)
        hit = C.one_line(out, LINT_SUMMARY.pattern)
        if hit is None:
            return False, "no CITED-LINES summary: %r" % ((out or err).strip()[:160])
        k = int(re.match(LINT_SUMMARY.pattern, hit).group(1))
        return (rc == 0 and k == 0, "rc=%d findings=%d line=%r" % (rc, k, hit[:80]))

    def rows_leg():
```

exit 0

### X11

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/counterlib.py | sed -n "138,156p"
```

```text
def claim_span(root, base, lands, own_paths):
    """Return (first_claim_commit, parent) for the commits in base..lands that touch an own path.

    A claim may need a corrected lands (a second commit that fixes its own artifact);
    separability is then judged over the claim's own commits from the first one that
    touches its paths, and foreign paths must be byte-identical at that commit's parent
    and at lands.
    """
    own = [p.rstrip("/") for p in own_paths]
    for c in gout(root, "rev-list", "--reverse", "%s..%s" % (base, lands)).split():
        touched = changed_paths(root, c + "^", c)
        if any(any(t == p or t.startswith(p + "/") for p in own) for t in touched):
            return c, gout(root, "rev-parse", c + "^").strip()
    raise RuntimeError("no commit touching a claim path in %s..%s" % (base, lands))


def blob_sha(root, rev, path):
    r = run(root, "rev-parse", "%s:%s" % (rev, path))
    return r.stdout.decode().strip() if r.returncode == 0 else None
```

exit 0

### X12

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-d84.py | sed -n "204,222p"
```

```text
    def separable():
        other = set()
        for c in cfg["claims"]:
            if c["id"] == CLAIM_ID:
                continue
            for v in c.values():
                if isinstance(v, dict) and v.get("own_paths"):
                    other.update(v["own_paths"])
        unique = [p for p in block["own_paths"] if p not in other]
        parent = C.claim_span(root, base, lands, unique)[1]
        cumulative = C.changed_paths(root, base, lands)
        own_missing = [p for p in unique if not any(c == p or c.startswith(p) for c in cumulative)]
        foreign = [p for p in block["foreign_paths"] if C.blob_sha(root, parent, p) != C.blob_sha(root, lands, p)]
        return (not own_missing and not foreign,
                "span_parent=%s own_missing=%s foreign_moved=%s" % (parent[:8], own_missing or "none", foreign or "none"))

    g.grade("FROZENCFG", frozen)
    g.grade("BEFORE", before)
    g.grade("ENTRY", entry_leg)
```

exit 0

### X13

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/accept-o84.py | sed -n "197,215p"
```

```text
    def separable():
        other = set()
        for c in cfg["claims"]:
            if c["id"] == CLAIM_ID:
                continue
            for v in c.values():
                if isinstance(v, dict) and v.get("own_paths"):
                    other.update(v["own_paths"])
        unique = [p for p in block["own_paths"] if p not in other]
        parent = C.claim_span(root, base, lands, unique)[1]
        cumulative = C.changed_paths(root, base, lands)
        own_missing = [p for p in unique if not any(c == p or c.startswith(p) for c in cumulative)]
        foreign = [p for p in block["foreign_paths"] if C.blob_sha(root, parent, p) != C.blob_sha(root, lands, p)]
        return (not own_missing and not foreign,
                "span_parent=%s own_missing=%s foreign_moved=%s" % (parent[:8], own_missing or "none", foreign or "none"))

    g.grade("FROZENCFG", frozen)
    g.grade("BEFORE", before)
    g.grade("TOOL", tool_leg)
```

exit 0

### X14

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "min_selftest_checks\|min_changes\|min_rules_fired\|min_decision_rows\|min_anchors"
```

```text
24:    "min_decision_rows": 6,
26:    "min_anchors": 20,
92:    "min_selftest_checks": 20,
95:    "min_changes": 12,
96:    "min_rules_fired": 6,
```

exit 0

### X15

```
$ (cd $LANE) git show 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2:reports/round-84/claims.json | grep -n "\"own_paths\"" -A 3
```

```text
50:    "own_paths": [
51-     "corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md",
52-     "corpus/SOURCES.md"
53-    ],
--
117:    "own_paths": [
118-     "tools/apply-sound-laws.py",
119-     "examples/sound-laws/",
120-     "SKILL.md"
```

exit 0

### X16

```
$ (cd $LANE) git diff --stat 3ca2cf288fb593618e0559ea86a36e2dd3110eb8 7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2 -- reports/round-84
```

```text
 reports/round-84/claims.json          | 10 +++++----
 reports/round-84/counter-revisions.md | 41 +++++++++++++++++++++++++++++++++++
 2 files changed, 47 insertions(+), 4 deletions(-)
```

exit 0

### X17

```
$ (cd $LANE) git log --oneline 3ca2cf288fb593618e0559ea86a36e2dd3110eb8..7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2
```

```text
7e6ee2f8 round-84: freeze revision r2 — SOUNDLAW_ERROR shape marker accepts the label constant (fixture-proven, pre-dispatch)
e160a72e round-84: freeze revision r1 — entry section headings aligned to the house shape (pre-dispatch, no claim artifact)
```

exit 0

## 11. Expectations versus measured

| id | expectation | expected | measured | verdict |
|---|---|---|---|---|
| D1a | knowledge .md files at base = 257 | `257` | `257` | MATCH |
| D2a | registry rows under the seat census grammar = 837 | `837` | `837` | MATCH |
| D3a | filename sweep owning basenames = 0 | `0` | `0` | MATCH |
| D3d | matter-of-subject files = 0 | `0` | `0` | MATCH |
| D3f | word-boundary census lines = 19 (claim prose) | `19` | `19` | MATCH |
| D3g | word-boundary census files = 10 (claim prose) | `10` | `11` | DIVERGE |
| D3i | gap-filled lines naming the surface = 0 (scout brief) | `0` | `1` | DIVERGE |
| D4a | entry absent at base (git cat-file rc = 128) | `128` | `128` | MATCH |
| S5 | rows S914-S917 at base = 0 | `0` | `0` | MATCH |
| O1a | tool/example sound-law name hits = 0 | `0` | `0` | MATCH |
| O2a | SOUNDLAWS line count at base = 0 lines (empty stdout) | `0` | `0` | MATCH |
| O3a | examples/sound-laws files at base = 0 | `0` | `0` | MATCH |
| O4g | gate at base = 0 missing / 74 registered / 61 instruments / 0 dead | `GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead` | `GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead` | MATCH |
| O4g | gate info at base = 25 tools without a row | `GATE-REGISTRY-INFO: 25 tools without a row` | `GATE-REGISTRY-INFO: 25 tools without a row` | MATCH |
| P0c | lane tip at measurement = freeze r2 | `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` | `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` | MATCH |

Divergences and their exact reading:

- `D3g`: the frozen claim's prose says the term set occurs "19 times across 10 files"; the tree
  gives 19 lines across **11** files. Nothing the counter grades depends on the file count
  (`B1` passes), but the prose is off by one and should not be quoted as a measured constant.
- `D3i`: the scout brief's literal test (`grep -nE '^- gap filled:.*(witch|witchcraft|sorcer|sorcery|malefic)'`)
  returns **1** line, not 0. The line is
  `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4`, whose subject is
  amulets; it quotes `witch mark` inside a sweep ledger that reports the term occurs in 0
  files. Ownership claims: 0. The brief's command-level "= 0" is therefore false as an
  instrument reading while the frozen claim's wording ("no `- gap filled:` owner for the
  surface") remains true.

## 12. Calibration findings

Each finding names the measurements that carry it; none changes a base number.

### F1 (D) The scout brief's `- gap filled:` test is 1 at base, not 0

Kind: brief divergence, not a claim divergence.

Measured: 1 line: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4 (D3h, D3i, V5).

Reading: The line's subject is protective objects; the surface appears as the quoted search term `witch mark` inside a sweep ledger that reports the term occurs in 0 files. A word-boundary variant still matches it (V6, V7), so only reading the line separates it from an ownership claim.

Impact: Any later checker that asserts the brief's literal `= 0` fails on green bytes. The frozen claim's wording ('no `- gap filled:` owner for the surface') is still true: ownership claims = 0.

### F2 (D) The word-boundary census is 19 lines across 11 files; the frozen prose says 10 files

Kind: prose divergence.

Measured: 19 lines, 11 files (D3e, D3f, D3g; worktree cross-check W3/W3b identical).

Reading: The 11th file is myth-symbol/animal-symbolism.md:9, a bibliography line carrying the book title 'Cows, Pigs, Wars and Witches'.

Impact: Not counter-graded: the BEFORE leg reads 257 files, 837 rows, entry absence and owning basenames only. Do not quote 10 as a measured constant.

### F3 (O) Claim O's registry sentence is a base reading; the lane tip already reads 2 missing / 63 instruments

Kind: base-versus-tip reading.

Measured: base: `GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead` and `GATE-REGISTRY-INFO: 25 tools without a row`, rc 0 (O4g). tip 7e6ee2f8: `2 missing / 74 registered / 63 instruments / 0 dead`, rc 1, the two MISSING paths being reports/round-84/accept-d84.py and accept-o84.py (O4a, O4b)..

Reading: The two round-84 counters are instruments at the tip but carry no SKILL.md row yet, so the instrument floor in the claim's `after` (i >= 63) is already met and the deficits are the two rows plus registered 74 -> >= 77.

Impact: A seat that re-reads the instrument set at the tip expecting 61 measures 63. Use the base revision for 61 and the tip for 63.

### F4 (O) The counter invokes `--selftest`; the frozen tool contract's canonical spelling is `selftest`

Kind: contract versus counter.

Measured: accept-o84.py:117 runs `["--selftest"]`; claims.json shape_markers require the literal `--selftest` in the tool bytes (X6); the junk stub also keys on `--selftest` (accept-o84.py:258). The seat-level tool contract prints `selftest` and the bench spec writes `--selftest` (alias `selftest`).

Reading: A tool implementing only the `selftest` spelling fails SELFTEST and TOOL. A tool implementing both passes; the literal `--selftest` must appear in the source bytes even if only as an alias.

Impact: The builder must accept both spellings and keep the literal in the file.

### F5 (D+O) The dispatch names freeze r0; the lane tip is freeze r2 and two graded constants moved

Kind: revision drift, pre-dispatch.

Measured: r0 3ca2cf28 -> r1 e160a72e -> r2 7e6ee2f8 (X17). Claims.json changed: claim D's decision_heading `## 2. The decision table` -> `## 2. Six design decisions` and anchors_heading `## 4. Attested anchors` -> `## 3. Attested anchors` (X4, X5); claim O's shape marker `SOUNDLAW_ERROR:` -> `SOUNDLAW_ERROR` (X6) and new `semantics` and `min_trace_columns` fields (X8) that no counter line reads (X7).

Reading: The dispatch/context text and the seat spec disagree on claim D's two headings; the seat spec matches the tip. An entry written to the r0 headings fails DECISIONS/ANCHORS under an r1/r2 freeze and vice versa. FROZENCFG requires the lands claims.json to equal the freeze bytes.

Impact: Graders must be told which freeze hex is in force; the two heading pairs are not interchangeable.

### F6 (D+O) SEPARABLE forces all of claim O's bytes to land strictly before claim D's first commit

Kind: landing-order constraint, code-derived.

Measured: counterlib.py:138-152 `claim_span` returns the first commit in base..lands touching a claim's own paths plus that commit's parent; accept-d84.py:216 and accept-o84.py:209 compare blob_sha(parent, foreign_path) with blob_sha(lands, foreign_path), and counterlib.py:154-156 returns None for a path absent at the revision.

Reading: If D lands first or in the same commit as O, D's foreign paths (tool, examples dir, SKILL.md) exist at lands and are absent (or differ) at D's first-claim parent, so D's SEPARABLE leg fails. O first, D second passes both legs: O's foreign paths (entry, SOURCES) are absent at the freeze and unchanged at lands.

Impact: Land order is a graded constraint, not a convenience; a single combined commit fails both legs.

## 13. Reproducibility

`method/` holds normalised copies of the three drivers and of the three helpers, with the
scratch root replaced by `${STAGE:?}`, the lane root by `${LANE:?}`, and the tip
materialisation revision pinned to the measured tip. Executed in a fresh `$STAGE` with
`STAGE` and `LANE` set, they reproduce **111 of 120** entries byte-for-byte; the nine
excluded entries are the nine that read the clock, the lane HEAD or the live worktree
(`P0`, `P0b`, `P0c`, `P0d`, `P0e`, `P1`, `P1b`, `P1c`, `O4b`). The comparison is recorded in
`receipts/repro-check.txt`; the rule is `receipts/index.tsv`.

## 14. What this does not measure

- It does not grade the entry or the tool (that is the counters' job at lands).
- It does not measure source availability for S914-S917 (that is ScoutSourcesWitch).
- It does not read uncommitted bytes as a base state; `P1b` records the working-tree dirt seen
  during the run so a later reader can tell what was in flight.
