# ScoutRecon — round-90, claim C (coverage) — base-surface re-derivation and entry boundary

Seat: ScoutRecon-7 · 2026-11-04 · milestone r90-v1 · lane kotodama
Frozen predicate read first: `reports/round-90/claims.json` (unamended, base `6b0b86e4`).
Read-only reconnaissance: no lane file written, no git/jj mutation, no subagent dispatch.
Scratch `/fast/scratch/hyaku/kotodama-r90/ScoutRecon/` (base tree materialized with
`git archive`, never `git worktree`), deleted before yield.

Two headline results:

1. **The frozen surface claim is right and the pasted command is wrong.** `claims.json`
   C.surface lists six owner files including `carthage.md:1`; the seat's case-sensitive
   heading grep reproduces only five. `carthage.md:1` carries a capitalized **`Votive`**.
   The `-i` run reproduces all seven heading lines over six files, i.e. the frozen list.
2. **The hardest collision is not one of the six files in the frozen list.** It is
   `corpus/knowledge/civilizations/arabia-pre-islamic.md`: `:58` already prints the word
   `petitionary inscription`, and §Safaitic `:141-148` already carries a real worked
   petition-inscription grammar with two verbatim excerpts (AMSI 71, ZEGA 1). The new
   entry's "votive inscription grammar" leg must route through that section.

---

## 1. Base surface re-derived at `6b0b86e45ae902331aca75863db380f2991458c4`

### 1.1 Headings naming the surface — as pasted (case-sensitive)

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -nE \
    '^#{1,6} .*\b(prayer|petition|votive|supplicat)' \
    6b0b86e45ae902331aca75863db380f2991458c4 -- corpus/knowledge
6b0b86e4…:corpus/knowledge/civilizations/tibet.md:92:## 5. Symbolic systems and prayer-wheel mantra economies
6b0b86e4…:corpus/knowledge/myth-symbol/direction-symbolism.md:129:## 8. Orientation of prayer and institutions
6b0b86e4…:corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:1:# Sacred topography and pilgrimage — the place register: holy-site typology, the route as rite, votive economy, and the shrine institution
6b0b86e4…:corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:74:## 5. The votive economy — the object, the receipt, the token
6b0b86e4…:corpus/knowledge/synthesis/religion-language-co-evolution.md:1:# Religion–language co-evolution: sacred registers, prayer languages, and priestly closure
# rc=0, 5 lines
```

### 1.2 Same command, case-insensitive

```
$ git grep -niE '^#{1,6} .*\b(prayer|petition|votive|supplicat)' 6b0b86e4 -- corpus/knowledge
…civilizations/carthage.md:1:# Carthage — Punic Language, Votive Cult, and Maritime Culture
…civilizations/tibet.md:92:## 5. Symbolic systems and prayer-wheel mantra economies
…myth-symbol/direction-symbolism.md:129:## 8. Orientation of prayer and institutions
…myth-symbol/sacred-topography-pilgrimage.md:1:# Sacred topography and pilgrimage — …votive economy, and the shrine institution
…myth-symbol/sacred-topography-pilgrimage.md:74:## 5. The votive economy — the object, the receipt, the token
…synthesis/religion-language-co-evolution.md:1:# Religion–language co-evolution: sacred registers, prayer languages, and priestly closure
…synthesis/religion-language-co-evolution.md:64:## 5. Prayer languages: model events and permissions
# 7 lines over 6 files
```

Note the seventh line: `religion-language-co-evolution.md:64` carries capital `Prayer`, so
**the case-sensitive command misses two of the seven matching lines** (`carthage.md:1`,
`religion-language-co-evolution.md:64`) and one of the six owner files.

### 1.3 Filename owners and body files

```
$ git ls-tree -r --name-only 6b0b86e4 corpus/knowledge | grep -cE '(prayer|petition|votive|supplicat)'
0
$ git grep -lciE '\b(prayer|petition|votive|supplicat)' 6b0b86e4 -- corpus/knowledge | wc -l
88
```

### 1.4 Bounded vs unbounded term census (matching lines, whole partition)

```
prayer           files=60   matching-lines=131
petition         files=35   matching-lines=75      (unbounded 'petition': 91 files)
petitionary      files=1    matching-lines=1
votive           files=15   matching-lines=52
supplicat        files=2    matching-lines=2
invocation       files=32   matching-lines=49
'prayer language' files=1   matching-lines=5
optative         files=0    matching-lines=0
precative        files=0    matching-lines=0
mood             files=25   (bounded, body)
```

### 1.5 Does `reports/round-90/base-surface.txt` agree?

**Partly — it agrees with the pasted command and disagrees with `claims.json`.**

| item | base-surface.txt | my re-derivation | verdict |
|---|---|---|---|
| filename owners | 0 | 0 | agree |
| heading lines, case-sensitive | 5 (same 5) | 5 | agree |
| body files | 88 | 88 | agree |
| files total / linguistics | 261 / 34 | 261 / 34 | agree |
| registry rows / last id | 865 / S941 | 865 / S941 | agree |
| owner file list vs `claims.json` | omits `carthage.md:1` | `-i` run shows it | **base-surface.txt is short one owner** |

`base-surface.txt` is internally honest — it pastes the command it ran — but the command
it ran is case-sensitive, so the record under-counts the owner set that `claims.json`
declares. Both `claims.json` (six files) and the `-i` measurement are correct.

**Recommendation to L1:** when the round-90 lesson or report restates the surface, run the
heading grep with `-i` and record 7 lines / 6 files, or add one line to `base-surface.txt`
naming `carthage.md:1` as a case-only miss. Do not amend `claims.json` (frozen).

### 1.6 Patterns that false-match

| pattern | false match | evidence |
|---|---|---|
| unbounded `petition` | **`competition`** | 91 files unbounded vs 35 word-bounded; 32 files contain `competition`. Heading-level false positives: `culture-material/garment-lexicon-crosslinguistic.md:1` ("Generic–Specific **Competition**") and `:56` ("## 5. Generic vs specific competition") |
| case-sensitive `\bvotive` | misses capitalized `Votive` | `carthage.md:1` |
| case-sensitive `\bprayer` | misses `Prayer` | `religion-language-co-evolution.md:64` |
| bare `supplicat` | 2 hits, both are `supplicant/supplication` in non-petition senses | `civilizations/tibet.md:70` ("Local supplication appears in early ritual"), `myth-symbol/guest-right-hospitality-law.md:71` ("the suppliant's formula states the jurisdiction") — neither owns prayer formulae |
| `\bprayer\b`-style word boundary on `prayer-wheel` | still matches `prayer` (prefix of a compound) | `tibet.md:92` — a wheel-economy section, not a prayer-language section |

`petitionary` exists exactly once in the whole partition:
`civilizations/arabia-pre-islamic.md:58` — `distinguish local conversation, public
genealogical identification, **petitionary inscription**, heightened ode, and ritual
utterance`. This is the single pre-existing use of the entry's own head noun.

---

## 2. Entries already holding part of this ground — boundary the new entry must not cross

Line ranges are inclusive and stop one line before the next heading.

### 2.1 `corpus/knowledge/civilizations/tibet.md` — §5, lines 92–115

> `## 5. Symbolic systems and prayer-wheel mantra economies`

Covers: Avalokiteśvara + *oṃ maṇi padme hūṃ* coupling; prayer wheel vs Dharma-wheel vs
mandala vs rosary vs prayer flag; *g.yung drung* semantics; prescribed rotation direction;
"mantra economy" as an analytical framework (production, circulation, authorization,
attribution); a 7-row **object/economy** table (text, motion, merit attribution, intention,
patronage, technology, distribution); evidence limit (emic equivalences); dating limit.

**Boundary:** tibet owns the *text-bearing object* and its merit economy. The new entry
must not re-teach the wheel, the mantra economy, or merit attribution. It may cite `:92` for
"the prayer object is a separate institution from the prayer utterance" and take only the
utterance side.

### 2.2 `corpus/knowledge/myth-symbol/direction-symbolism.md` — §8, lines 129–140

> `## 8. Orientation of prayer and institutions`

Covers: qibla (Qur'an 2:144, al-Bīrūnī); the Jewish nested ladder (Berakhot 30a); *ad
orientem*; Chinese south-facing rule; Bali *kaja*; the Etruscan *templum*; and the design
rule "sacred orientation is the most dateable direction fact — write a reorientation as an
event with an institution to enforce it".

**Boundary:** direction owns the *bearing* of prayer. The new entry must not re-derive any
orientation rule and must not restate the reorientation-as-event rule; it cites `:129-140`
as the address-vector's spatial half.

### 2.3 `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` — header 1–14, §5 74–80

> `# Sacred topography and pilgrimage — the place register: holy-site typology, the route as rite, votive economy, and the shrine institution`
> `## 5. The votive economy — the object, the receipt, the token`

§5 covers: three objects (votive deposit / inscribed receipt / token) each with its
institution; "the archive is the byproduct" (Asclepieia, `divination-omen-systems.md:135`);
badges-as-archaeology; the economy around the site (`arabia-pre-islamic.md:120,:122`);
"a sanctuary's wealth is evidence of a later economy, not of its ancient sanctity".

**Boundary:** this entry owns the **deposited object, the receipt as an object, and the
token economy**. The new entry owns the **text of the receipt** — the grammar of the
inscription — not the object's deposition, manufacture, or market. It must cite `:74-80`
for the receipt-as-object and add only the inscription's syntax. It must not re-teach the
archive-byproduct rule.

### 2.4 `corpus/knowledge/synthesis/religion-language-co-evolution.md` — header 1–9, §5 64–78

> `# Religion–language co-evolution: sacred registers, prayer languages, and priestly closure`
> `## 5. Prayer languages: model events and permissions`

§5 covers a 6-row **event × language-policy** table (canonical recitation, sermon, **private
petition**, hymn, naming/initiation, translation) and the rule "never derive an entire
community's private prayer practice from its formal liturgy"; the five competences
(recitation accuracy, reading, comprehension, composition, authorization).

**Boundary:** this synthesis owns the **event-typed policy question and the competence
split** — *which language may be used for which event, by whom*. The new entry must not
re-tabulate events against language policy. It owns the complementary object: **what the
petition sentence itself is made of** (vocative, mood, condition, vow). Cite `:64-78`.

### 2.5 `corpus/knowledge/civilizations/carthage.md` — header 1–9, §4 66–82

> `# Carthage — Punic Language, Votive Cult, and Maritime Culture`
> `## 4. Cult core and the limits of reconstructed mythology`

§4 covers: Tanit `tnt pn bʿl` / Baal Hammon `bʿl ḥmn` as dedication recipients; the
dedication segments `lrbt ltnt pn bʿl` and `wlʾdn lbʿl ḥmn`; **`ndr`, vow, and "he heard
his voice" formulae connect petition, named dedication, and expected response**; Baal as a
title; no Tanit=Astarte merge; method transfer "construct a cult around recipients,
epithets, vow verbs, authorized personnel, and material offerings".

**Boundary:** this is the **single most dangerous collision** for the "conditional vow"
leg. Carthage already states the `ndr` vow ↔ named dedication ↔ "he heard his voice"
circuit as a Punic worked case. The new entry must **cite `:74-79`** and must not restate
the Punic formulae, the recipient pairing, or the method-transfer line. What the new entry
may add: the *general* vow grammar (apodosis form, the deferred-payment slot, the
witness/inscription requirement) as a cross-cultural design instrument, with Carthage as
one of its anchors.

### 2.6 Additional owner the frozen surface list does **not** contain (highest risk)

#### `corpus/knowledge/civilizations/arabia-pre-islamic.md` — §"Language family, scripts, and registers" 52–60; §Safaitic 141–148

> `## Language family, scripts, and registers`
> `## Safaitic: compact models of social and sacred speech`

`:58` — `distinguish local conversation, public genealogical identification, petitionary
inscription, heightened ode, and ritual utterance.`
`:142` — `The basalt-desert inscriptions commonly combine **l- genealogy → w- narrative →
w-/f- prayer or curse**.`
`:143` — AMSI 71: `l bny bn bny bn nẓr w ḏbḥ f h lt slm` (author + paternal chain,
sacrifice, invocation to Allāt for security).
`:144` — ZEGA 1 (lineage, cult stone, petition).
`:145` — lexical coupling `slm` security, `qbll` reunion, `rwḥ` relief, `ḏbḥ` sacrifice.
`:148` — `DESIGN: let ordinary economic activities motivate petitions… Formulaic language
can be compact and personal without being mechanically identical.`

**Boundary:** this entry already owns **a complete petition-inscription formula with its
slot sequence and two verbatim excerpts**. The new entry must cite `:141-148` as its
worked real-world case for inscription grammar and must not re-quote AMSI 71 / ZEGA 1,
must not restate the `l- → w- → w-/f-` chain as its own finding, and must not re-teach the
"economic motive for petition" design rule. Its legitimate addition: the *cross-linguistic
generalisation* of those slots (vocative address → predicate of need → condition → promised
counter-gift → self-identification/witness), which `arabia` states for one corpus only.

#### Two further owners, both in the linguistics partition

`corpus/knowledge/linguistics/sacred-registers-liturgical-language.md` §1 (26–40), §4 (73–85), §5 (86–100):
its §1 boundary table already assigns **"the special-language survey signature (archaism,
formula, parallelism, performative force)" to `linguistic-anthropology.md` §5.1**, and §4
owns "why liturgy freezes: mechanism per layer". §5's event table already contains a
**"Private petition | intent suffices | none in H | disfavored free words"** row.

`corpus/knowledge/linguistics/linguistic-anthropology.md` §5.1 (93–103):
`Structural signature: archaism + formula + parallelism + performative force, often with
deliberate incomprehensibility` — with Fox 1988 *To Speak in Pairs*, Sherzer 1983, Kuipers
1990, Tambiah 1968, Staal 1979.

`corpus/knowledge/linguistics/semantics-pragmatics.md` §5 (84–112), table at 88–95:
`| directives | order, request | petition registers; who may direct whom |` and
`| commissives | promise, vow | oath formulae with self-curse clauses |`.

**Boundary (these three together):** the new entry's legs "prayer-register archaism and
parallelism" and "petition mood" are **already owned at the level of classification**.
- archaism + parallelism: owned by `linguistic-anthropology.md §5.1` and routed by
  `sacred-registers-liturgical-language.md §1`. The new entry may cite both and must add
  only what they do not hold: **the sentence-level form of archaism inside a petition**
  (fossil mood endings, the archaic vocative particle, the preterite-as-precative), not the
  register-level signature again.
- petition mood: `semantics-pragmatics.md §5` owns the Searle class map. The new entry must
  not re-teach directive/commissive classification; it owns the **mood-marking inventory**
  (imperative / optative / precative / jussive / subjunctive-in-vow) — which is genuinely
  absent (`optative` 0 files, `precative` 0 files at base).

---

## 3. Internal cross-links the new entry must cite

Repo-relative paths (from the lane root; the entry's own header uses paths relative to
`corpus/knowledge/`, per the house convention in `carthage.md:3` and
`religion-language-co-evolution.md:3`). Section names as they must appear.

| # | link | why the entry needs it | the exact surface it must cite, not restate |
|---|---|---|---|
| 1 | `corpus/knowledge/linguistics/naming-systems.md` §4 Theonymy (73–79), §6 Name taboo and name magic (87–108) | vocative address names a deity; epithets are the address form; name taboo is the kotodama core | transparent/opaque theonyms, cult epithets (Athena Polias), the bìhuì table — cite only |
| 2 | `corpus/knowledge/synthesis/deity-name-derivation-pipeline.md` §4 Epithet systems (69–88), §6 Name taboo (110–131) | the pipeline that produces the name the vocative calls | epithet = grammar + jurisdiction; "specify the forbidden act" |
| 3 | `corpus/knowledge/myth-symbol/pantheon-archetypes.md` §1 (30–35), §7 Build protocol (102–) | who may be addressed, and with what role-set | functional-map premise |
| 4 | `corpus/knowledge/myth-symbol/ritual-liminality.md` §4 Sacrifice (51–69), **votive row `:58`** | the offering is the vow's payment; `:58` is the lane's only votive-offering typology row | `votive │ pay a vow │ Greek anathemata; Roman vota; ex-voto plaques │ contract-law with the divine` |
| 5 | `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` §5 (74–80) | the inscribed receipt as an object; the votive economy | deposit/receipt/token triad; archive-as-byproduct |
| 6 | `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` `:27` | the coupling row already declares the shrine→talisman handoff | its own boundary table row |
| 7 | `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md` §1 (26–40), §4 (73–85), §5 (86–100) | the sacred register the prayer is spoken in; the "private petition" event row | the boundary table + fossilization mechanics + event-typed rules |
| 8 | `corpus/knowledge/linguistics/linguistic-anthropology.md` §5.1 (93–103) | archaism/formula/parallelism signature — the declared owner | cite as owner; add only sentence-level form |
| 9 | `corpus/knowledge/linguistics/semantics-pragmatics.md` §5 (84–112) | speech-act classes: directives→petition, commissives→vow | the Searle table |
| 10 | `corpus/knowledge/linguistics/morphological-typology.md` §4 Morphological processes (40–56), §11 Application protocol (110–) | **mood marking** is morphology: fusion vs agglutination decides whether a mood is a suffix, a particle or a stem change | process catalog; the "write one full paradigm" rule `:116` |
| 11 | `corpus/knowledge/linguistics/syntax-typology.md` §1 (9–33), §3 (51–66) | vocative position, verb-final petition clauses, embedding of the condition | word-order companions; embedding |
| 12 | `corpus/knowledge/linguistics/orality-formulaic-language.md` §1 (30–37), §3 (56–63) | prayer formulae are formulaic composition; parallelism is the same engine as epic couplets | Parry–Lord engine; epithet/praise-name lexicon |
| 13 | `corpus/knowledge/linguistics/historical-linguistics.md` §5 The grammaticalization cycle (107–142) | the optative→subjunctive→conditional drift is a grammaticalization case | the cycle |
| 14 | `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` §2 Honorific systems (55–70) | address form to a superior deity; deferential vocative | honorific-as-grammar |
| 15 | `corpus/knowledge/synthesis/religion-language-co-evolution.md` §5 (64–78) | event-typed policy for private petition | its event table |
| 16 | `corpus/knowledge/civilizations/carthage.md` §4 (66–82) | `ndr` vow + "he heard his voice" worked case | cite, do not re-quote |
| 17 | `corpus/knowledge/civilizations/arabia-pre-islamic.md` §Safaitic (141–148) | the compact inscription formula, verbatim | cite, do not re-quote AMSI 71 / ZEGA 1 |
| 18 | `corpus/knowledge/civilizations/tibet.md` §5 (92–115) | prayer-object vs prayer-utterance split | cite |
| 19 | `corpus/knowledge/myth-symbol/direction-symbolism.md` §8 (129–140) | the address's bearing | cite |
| 20 | `corpus/knowledge/synthesis/worldbible-integration-contract.md` §3 Ownership decision table (36–48), §4 Handoff envelope (49–71) | **worldbible handoff contract**: the entry must end at a handoff, and must declare which fields the bible receives | the envelope's required fields |
| 21 | `corpus/knowledge/verification/myth-consistency-gate.md:34` and `verification/real-world-inspiration-boundaries.md` §(2,6) | restricted-ritual-knowledge gate — mandatory for living-tradition prayer material | the gate sentence |
| 22 | `corpus/knowledge/verification/to-verify-triage-protocol.md:15` | every unopened literature leg must be routed | the triage rule |

Precedent for the entry's own `couples:` line: `evidentiality-epistemic-marking.md:8`
(round-89) lists exactly this shape — `linguistics/… §N (what it holds — not repeated
here)`.

---

## 4. Coverage accounting at base `6b0b86e4`

```
$ git ls-tree -r --name-only 6b0b86e4 corpus/knowledge | grep -c '\.md$'
261
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do
    git ls-tree -r --name-only 6b0b86e4 corpus/knowledge/$p | grep -c '\.md$'; done
linguistics: 34
myth-symbol: 36
culture-material: 43
synthesis: 29
verification: 24
civilizations: 95          (sum = 261)
```

`corpus/README.md` partition lines (base, 937 lines):

```
344:## linguistics/ (34)
378:## myth-symbol/ (36)
412:## culture-material/ (43)
455:## synthesis/ (29)
487:## verification/ (24)
513:## civilizations/ (95)
```

Footer:

```
Total knowledge entries: 261.

Counts checked 2026-11-04 from the repo root:
`python3 -B tools/check-corpus-index.py --root .`
(total 261 files; directory totals 34/36/43/29/24/95).
```

Registry — `corpus/SOURCES.md` (the registry is SOURCES.md, not a separate file):

```
$ git show 6b0b86e4:corpus/SOURCES.md | grep -cE '^\| *S[0-9]+'
865
$ … | grep -oE 'S[0-9]{3,4}' | sort -u | tail -5
S937 S938 S939 S940 S941
$ … | grep -cE '\| 2026-11-04 \|'      # rows already opened on the round's date
38
```

### 4.1 Index tool at base — clean

Materialized the base tree with `git archive` into scratch (no worktree, no mutation) and ran
the freeze-pinned checker:

```
$ git archive 6b0b86e4 corpus tools | tar -x -C $S/base
$ cd $S/base && python3 -B tools/check-corpus-index.py --root .
CORPUS-INDEX: OK files=261 rows=261 findings=0
EXIT=0
```

### 4.2 Five README surfaces must move together (measured from the tool's source)

`tools/check-corpus-index.py` raises, per partition: `MISSING_ROW`, `GHOST_ROW`,
`DUPLICATE_ROW`, `TOPIC_MISMATCH` (row text must be **byte-equal** to the entry's `- topic:`
field after whitespace folding), `HEADER_DRIFT` (`declared != len(disk)`), plus
`TOTALS_ABSENT`/`TOTALS_DRIFT`, `FOOTER_ABSENT`/`FOOTER_MALFORMED`/`FOOTER_TOTAL`/
`FOOTER_DIR_TOTALS` (`footer dir_totals` compared against `[len(files[p]) for p in PARTS]`,
PARTS order `linguistics, myth-symbol, culture-material, synthesis, verification,
civilizations`).

So one new linguistics entry requires **five** edits to `README.md`:
1. `## linguistics/ (34)` → `(35)`
2. a new row in that span, **in filename order** — `petitionary-and-votive-formulae.md`
   sorts between `orality-formulaic-language.md` and `phonetics-phonology.md`
3. the totals line `Total knowledge entries: 261` → `262`
4. the footer `(total 261 files; …)` → `262`
5. the footer vector `34/36/43/29/24/95` → `35/36/43/29/24/95`

### 4.3 Trap: the linguistics section already under-lists by 2

Section header declares 34 and 34 files exist, but the span carries only **32** `- \`x.md\``
rows:

```
$ comm -23 <(ls-tree linguistics filenames | sort) <(README rows 344-377 | sort)
conlang-scholarship.amend-2026-10-23.md
conlang-scholarship.md
$ comm -13 …
(empty)
```

The checker still reports `OK` because those two files are resolved as **supplemental rows**
appearing elsewhere in README (`parse_readme` collects `ROW_RE` matches outside every
partition span and appends them to the single partition that owns the filename). Consequence
for the new entry: it must be listed **inside** the `## linguistics/` span; a supplemental
row elsewhere would pass the checker but is not the house pattern and would put the row out
of the section a reader scans. Do not "fix" the two scholarship files — that is a base-row
change and is outside this round's append-only leg.

### 4.4 Registry append-only rule and the reserved id block

`corpus/SOURCES.md:9-13` fixes the contract: `Append-only: only status, recheck and used-by
change in place`. Reserved this round: **S942 S943 S944 S945 S946 S947 S948 S949**, with
**S949 the lesson's reject row**. Round-89's precedent shape for the lesson gate lines
(`corpus/lessons/round-89.md:59-84`):

```
- **S936 admit A/mined.** https://wals.info/chapter/77 — accessed 2026-11-04 — section 1
  Defining the values, closing sentence before section 2: “…” Grounds: …
- **S941 reject C/rejected.** http://www.glottopedia.org/index.php/Evidentiality — accessed
  2026-11-04 — Definition, first sentence: “…” Grounds: unreferenced stub …
```

`corpus/lessons/round-90.md` **does not exist at base** (`git ls-tree corpus/lessons`
returns only `round-89.md` and `round-89-verifier-spotcheck.md`), while `claims.json`
names it as `C.lesson` and each new row must carry "a lesson gate line". L1 creates it.

### 4.5 Where the registry rows must point

Round-89's new rows carry the entry in `used-by` and the entry's header carries the ids in
`sources:` (`evidentiality-epistemic-marking.md:3` → `S936 … S940`). Claim C's NEWIDS leg
requires the reverse too: the entry must **cite** the new ids. Cite them in `- sources:`
and in the §"Sources (opened 2026-11-04)" block that round-89 established
(`evidentiality-epistemic-marking.md:189`).

---

## 5. Facts vs inference vs remaining unknowns

**Observed (command + output above):** all counts, all line ranges, all quoted headings,
the `-i`/case discrepancy, the `competition` false match, the `petitionary` single hit, the
zero counts for `optative`/`precative`, the 32-vs-34 README row shortfall, the base index
`OK 261/261`, the five README surfaces, the SOURCES.md append-only sentence, the absence of
`corpus/lessons/round-90.md`.

**Inference (marked, not verified):**
- `[INFERENCE]` The five README edits in §4.2 are the complete set — derived by reading the
  checker's finding classes, not by running it over a fixture with a new entry.
- `[INFERENCE]` "petition mood" is genuinely uncovered: `optative` and `precative` are 0 at
  base, and the `mood` hits are morphological-typology/paradigm contexts, not petition
  contexts. A full read of all 25 `mood` files was not done; only `morphological-typology.md`
  §4/§11 and `semantics-pragmatics.md` §5 were read.
- `[INFERENCE]` `arabia-pre-islamic.md` §Safaitic is the closest existing treatment of
  votive inscription grammar; no other file was found with a slot-sequence formula.

**Remaining unknowns (not resolved by this seat, outside its question):**
- Whether any registry row already covers a petition/vow/prayer-formula source (the 865-row
  `teaches` column was not searched for `vow|prayer|petition|dedication`); a duplicate-source
  collision at S942–S949 would only surface there.
- Whether `reports/round-90/evidence/manifest.json` and `reports/round-90/evidence/` exist
  (they do not at base — `reports/round-90/` holds `base-surface.txt`, `census-start.txt`,
  `claims.json`, `controls/`, `counter-revisions.md`, `measure90.py`, `mutants.py`,
  `mutation-score.*`); capture layout is L1's to create.
- The `-i` correction to `base-surface.txt` is a production file: I did not touch it.

**Tooling:** no install or upgrade was needed or performed; `git`, `python3`, `curl` only.
