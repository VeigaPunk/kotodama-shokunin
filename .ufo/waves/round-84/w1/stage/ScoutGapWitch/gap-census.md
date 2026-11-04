# Claim-D absence census — witchcraft / sorcery as an accusation institution

Seat: ScoutGapWitch · milestone r84-v1 · lane `kotodama-shokunin`
Before-state revision: `81499ee45b5751d388fefc78583810878de01ecd`
Frozen claims/counters revision: `3ca2cf288fb593618e0559ea86a36e2dd3110eb8`
Access date: 2026-11-04. Read-only recon; no canon recommendation.

The worktree at census time was byte-identical to the base for `corpus/knowledge`:
`git diff --stat 81499ee4 -- corpus/knowledge` printed nothing and
`git status --porcelain corpus/knowledge` printed nothing. Every sweep below reads the
base tree explicitly, so a concurrent writer cannot move the before-state.

Commands were run from the lane root (`kotodama-shokunin`). No network access was used.

---

## 1. Commands and raw output

### A. Filename sweep (owning basenames)

```
$ git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge \
    | grep -iE 'witch|witches|witchcraft|sorcer|sorcery|malefic'
(no output)
rc=1
```

```
$ git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge \
    | grep -c '\.md$'
257
```

Result: **0 owning basenames**; 257 knowledge files at base (target file absent —
`grep -i 'accusation-institution'` over the same listing printed nothing, rc=1).

### B. Matter-of-subject scan (topic lines)

```
$ git grep -nE '^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
(no output)
rc=1
```

Widened topic scan (stems `witch|sorcer|malefic|venefic|strig`, case-insensitive):

```
$ git grep -nE '^- topic: .{0,200}(witch|sorcer|malefic|venefic|strig)' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:3:- topic: The naked-eye sky as the worldbuilder's highest-yield symbolic system — sun/moon deity gender assignments across cultures (no universal pattern; aspect-switching), the planet-as-god interpretatio chain (Babylonian → Greek/Roman → Germanic/Chinese/Indian/Maya), constellation vs asterism as a naming problem, the Pleiades as the most calendrically overloaded object worldwide, Milky Way figure typology, eclipse-omen systems and their rituals and archives, the mechanics by which celestial cycles anchor calendars and festivals; with a calibration section on discredited celestial-myth schools
rc=0   (the single hit is the substring "aspect-switching", not the surface)
```

Result: **0 files whose `- topic:` line is about the surface.** The one widened hit is a
false positive of the stem `witch` inside `switching`.

### C. Word-boundary occurrence census (the assigned pattern)

```
$ git grep -niE '\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
```

19 lines, 11 files. Verbatim (receipt file `census-exact.tsv` in this directory):

```
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
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/binding-speech-complex.md:164:**5.2 Counter-curse and defense.** Every real curse ecology has defenses, and the defenses are the more interesting half: the *voces magicae* and "barbarous names" whose force is held to lie in the sound rather than the sense (Betz 1986) — a defense that requires knowing the name's *original* form; amulets, apotropaic writing, and threshold deposits (Gager 1992); the counter-curse that returns the imprecation to its sender; and, at the institutional level, **the prohibition**: Qur'an 2:102 and 5:90 place sorcery and divining arrows outside the permitted, which converts the whole channel from a technology into a sin (and the corpus's `./divination-omen-systems.md` §11 calibrates the modern misuse of that material). A culture that criminalizes cursing has not …
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/color-symbolism.md:22:| Turner's Ndembu triad (1967) | Ndembu ritual organizes on white (goodness/health/fertility/continuity), red (blood/transition/mediation), black (sorcery/bad death/disease) | Generates polarity *systems*; red as mediator between light/dark poles | A single-culture study; universalizing the triad was the classic overreach of later readers — Turner himself argues Ndembu-specific and answers Turnbull's critique in the same volume (§11) |
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/divination-omen-systems.md:13:  - Evans-Pritchard (1937), *Witchcraft, Oracles and Magic among the Azande*, Oxford UP — the *benge* poison oracle, the second-oracle check, the taboo list, arbitration use; Winch (1964), "Understanding a Primitive Society," *American Philosophical Quarterly* 1(4):307–324; Wilson, ed. (1970), *Rationality*, Blackwell
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/divination-omen-systems.md:112:| What did I do wrong | Ifa; Azande witchcraft diagnosis | a prescription (offer X) | generates the offering economy and the confession scene |
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/myth-folktale-genres.md:54:| 300–749 | Tales of magic (Märchen proper; Propp's corpus) | ATU 300 The Dragon-Slayer; 313 The Magic Flight; 325 The Sorcerer's Apprentice; 330 The Smith and the Devil; 410 Sleeping Beauty; 425C Beauty and the Beast; 440 The Frog King; 480 The Kind and the Unkind Girls; 500 The Name of the Supernatural Helper (Rumpelstiltskin); 510A Cinderella; 510B Donkeyskin / Cap o' Rushes; 545B The Cat as Helper (Puss in Boots); 709 Snow White; 720 The Juniper Tree |
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/myth-ritual-theories.md:12:  - Malinowski (1922), Argonauts of the Western Pacific, and (1926), Myth in Primitive Psychology, Kegan Paul (myth as "social charter"; Trobriand garden magic and Kula); Radcliffe-Brown (1922), The Andaman Islanders, Cambridge UP; Kluckhohn (1944), Navaho Witchcraft, Peabody Museum Papers; Malinowski (1926), Crime and Custom in Savage Society (his own counter to the universal Oedipus)
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/myth-ritual-theories.md:53:- Core claim: myth is not bad science or degraded ritual but a hard-working **social warrant** — it justifies institutions by narrating their origin as precedent. Trobriand material: garden-magic origin stories license land tenure and chiefly rank; Kula myths license exchange partnerships; the charter names names, places, and precedence. Malinowski: "the myth is to the savage what, to a fully believing Christian, is the Biblical tale of Creation" (Myth in Primitive Psychology, 1926 — the register is his; quote with care). Radcliffe-Brown (1922) is the adjacent "myth expresses social structure" line; Kluckhohn (1944) runs it on witchcraft ideology. Bascom's…
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:28:  - **The Ndembu color triad**: white/red/black, each spreading through the whole ritual vocabulary — white mudyi milk = motherhood, matriliny, goodness; red = blood, hunting, womanhood; black = sorcery, badness (Turner 1966).
```

Per-file distribution: amulets 6; binding-speech 2; divination 2; myth-ritual-theories 2;
mongol 1; yoruba 1; hair-grooming 1; animal-symbolism 1; color-symbolism 1;
myth-folktale-genres 1; symbolism-synthesis-method 1.

**Role of every line** (manual classification, one role per line):

| role | count | lines |
|---|---|---|
| bibliographic title in a source list | 5 | animal-symbolism:9, binding-speech:26, divination:13, myth-folktale-genres:54, myth-ritual-theories:12 |
| translation / source-criticism caution | 2 | mongol:193, yoruba:122 |
| passing exemplar or table cell | 5 | hair-grooming:39, color-symbolism:22, divination:112, myth-ritual-theories:53, symbolism-synthesis-method:28 |
| artifact name (witch bottle / witches' marks) | 4 | amulets:72, amulets:102, amulets:104, amulets:158 |
| dictionary definition of a neighbouring word | 1 | amulets:39 |
| absence probe inside a `- gap filled:` line | 1 | amulets:4 |
| prohibition clause (sorcery as sin) | 1 | binding-speech:164 |

No line defines, tabulates, or owns the accusation institution.

**Widened lexeme check** (the assigned pattern is blind to `witchery` and `sorceress`):

```
$ P='\b(witch[a-z]*|bewitch[a-z]*|sorcer[a-z]*|malefic[a-z]*|venefic[a-z]*|strig(a|ae|oi|e)\b|incubus|succubus)'
$ git grep -niE "$P" 81499ee4 -- 'corpus/knowledge' | wc -l
22
$ git grep -liE "$P" 81499ee4 -- 'corpus/knowledge' | wc -l
13
```

Three lines are added over the assigned pattern; all three are likewise passing:

| added line | token | role |
|---|---|---|
| `civilizations/kongo-kingdom.md:45` | `sorceress` | source-criticism: “Gallo calls Kimpa Vita a possessed sorceress: weigh it as testimony against her” — hostile-witness caution, not an institution |
| `myth-symbol/monsters-hybrid-beings.md:119` | `witchery` | restricted-knowledge note: publish the rule, withhold the content (Diné witchery named as a restricted kind of talk) |
| `myth-symbol/monsters-hybrid-beings.md:122` | `witchery` | same: Denetdale quoted, “We don't talk about witchery” — the norm is recorded, never the content |

Widened total: **22 lines / 13 files**, still 0 owning topic lines.

### D. `- gap filled:` lines naming the surface

```
$ git grep -niE '^\- gap filled:.*(witch|sorcer|malefic)' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4:- gap filled: at the claim base no file under `corpus/knowledge` owns protective objects as a system. Filename sweep `git ls-tree -r --name-only d4795abd corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` → 0; `evil eye`, `nazar`, `mezuz`, `omamori`, `ofuda`, `phylacter` and `witch mark` occur in 0 files (`.ufo/waves/round-59/build/ConnectInLaneAmulets59.md` §1). Partial owners hold single links of the chain (danger, carrier, material, surface, deposition); §2 routes each one-way.
rc=0
```

```
$ git grep -nE '^- gap filled:' 81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge' | wc -l
60
```

Measured: **1** of 60 `- gap filled:` lines contains a surface token, and it is an
**absence probe** (`witch mark` occurs in 0 files) inside the amulets entry — not an
ownership claim. **0** lines claim the surface as the entry's own gap.

A wider probe over accusation-chain vocabulary (`accus|inquisit|ordeal|confess|slander|defam|witch|sorcer|malefic`)
returns 2 lines, both absence probes: amulets:4 (above) and
`myth-symbol/ordeal-judicial-proof-rituals.md:4` (the ordeal entry's own 0-owner sweep;
it mentions `ordeal`, not the surface).

### E. Outside `corpus/knowledge` (context, same pattern)

```
$ git grep -niE '\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus' ':!corpus/knowledge' \
  | sed -E 's/^([0-9a-f]+):([^:]+):([0-9]+):.*/\1:\2:\3/' | awk -F: '{print $2}' | sort | uniq -c
      1 corpus/lessons/round-55.md
      3 corpus/lessons/round-59.md
      1 corpus/lessons/round-68.md
      7 corpus/SOURCES.md
```

The 7 S-id rows are S019 (ISEBEL belief-legend search), S332 and S333 (Motif-Index
volumes), S621 (*Witches' Marks*, Provan Hall), S622 (*Witch-bottles and healing
charms*, Museum Wales), S644 (Pitt Rivers amulets leaflet), S854 (plica polonica
article). None is a source row for an accusation institution. Six of the seven are
already cited by entries (amulets: S621, S622, S644; hair-grooming: S854;
monsters-hybrid-beings: S332, S333); S019 (ISEBEL) is the only uncited row.
`corpus/README.md` contains **0** real surface tokens: the only substring hit in its
index rows is `aspect-switching`.

---

## 2. Before-state counts

| measure | value |
|---|---|
| knowledge files at base | 257 |
| knowledge files if claim D lands | 258 |
| myth-symbol files at base | 35 |
| myth-symbol index rows in `corpus/README.md` | 32 |
| myth-symbol files without an index row | 3 |
| owning basenames (filename sweep) | 0 |
| owning `- topic:` lines | 0 |
| assigned-pattern lines / files | 19 / 11 |
| widened-lexeme lines / files | 22 / 13 |
| `- gap filled:` lines total | 60 |
| `- gap filled:` lines with a surface token | 1 (absence probe) |
| `- gap filled:` lines claiming the surface | 0 |
| surface lines outside `corpus/knowledge` | 12 (7 SOURCES + 5 lessons) |

The three unindexed myth-symbol files are exactly the three newest:
`guest-right-hospitality-law.md` (verified-at 2026-11-04),
`marriage-alliance-bridewealth.md` (2026-11-04), and
`ordeal-judicial-proof-rituals.md` (2026-11-01). The README's newest own count
(`corpus/README.md:834`) reads “Total knowledge entries: 253” and its myth-symbol
heading (`:376`) reads `(32)`; the live tree holds 257 and 35. The landing of a 258th
file widens that pre-existing drift by one; no byte of `corpus/README.md` is touched by
this census.

---

## 3. Machine-readable summary table (file, owner, lines)

| file | owner | lines |
|---|---|---|
| corpus/knowledge/civilizations/mongol.md | Mongol reference base (script, sacred lexicon, deel, yam, naming) | 193 |
| corpus/knowledge/civilizations/yoruba.md | Yoruba reference base (language, òrìṣà, oríkì, àṣẹ, Gelede, Ifá) | 122 |
| corpus/knowledge/culture-material/hair-grooming-codes.md | hair and grooming as a material register | 39 |
| corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md | protective objects as a system | 4, 39, 72, 102, 104, 158 |
| corpus/knowledge/myth-symbol/animal-symbolism.md | fauna as symbolic substrate | 9 |
| corpus/knowledge/myth-symbol/binding-speech-complex.md | oath / curse / blessing / name-power as one machinery | 26, 164 |
| corpus/knowledge/myth-symbol/color-symbolism.md | colour as an enforceable code | 22 |
| corpus/knowledge/myth-symbol/divination-omen-systems.md | divination as a symbolic technology | 13, 112 |
| corpus/knowledge/myth-symbol/myth-folktale-genres.md | narrative classification (Bascom, ATU, Motif) | 54 |
| corpus/knowledge/myth-symbol/myth-ritual-theories.md | classical theories of myth | 12, 53 |
| corpus/knowledge/myth-symbol/symbolism-synthesis-method.md | the five-register symbol-generation method | 28 |
| corpus/knowledge/civilizations/kongo-kingdom.md | Kongo reference base (source shelf, language, Antonians) | 45 |
| corpus/knowledge/myth-symbol/monsters-hybrid-beings.md | monsters as a cultural category; restricted beings | 119, 122 |

Last two rows are the widened-lexeme additions (`sorceress`, `witchery`).

---

## 4. Partial-owner map, one-way

Notation: “chain” = the six elements of the frozen claim (vocabulary set, accusation
grammar, proof technology, confession, slander law, social functions). No file below
answers any complete chain element; each answers an adjacent surface only.

### 4.1 `civilizations/mongol.md` — line 193

- **Owns:** the Mongol reference base — Uyghur-derived writing, the Secret History's
  registers, Heaven/earth/ancestor lexicon (§83), symbolic system (§107), deel and dress
  entitlement (§121), yam (§143), naming (§170).
- **Does not answer:** the chain. Its one mention is a source-criticism caveat —
  Rubruck's words “Idol”, “devil”, “witchcraft” are “his judgments, not neutral
  translations”. It supplies a warning about European category import and nothing about
  accusation procedure. It owns none of amulets, divination, binding speech, colour,
  funerary or purity; those stay in their specialist files.

### 4.2 `civilizations/yoruba.md` — line 122

- **Owns:** Yoruba reference base — sound-to-object bridge (§27), drum speech (§41),
  òrìṣà ecology (§60), oríkì (§78), àṣẹ (§95), symbolic relations (§109), Gelede (§120),
  dress (§138), era staging (§146), naming (§159), Ifá registers (§168).
- **Does not answer:** the chain. Line 122 is a translation caution: “Translate àjẹ́ and
  related spiritual powers carefully; ‘witch’ can import a demonizing European
  category”. The file explicitly *refuses* the equation the accusation institution
  needs to analyse. It does not own divination in general (Ifá is a bounded register
  here; the technique typology is `divination-omen-systems.md`), nor amulets, binding
  speech, colour, funerary or purity.

### 4.3 `culture-material/hair-grooming-codes.md` — line 39

- **Owns:** hair and grooming as a register — state control (§7), faith grooming (§16),
  wig and hair trades (§27), hair politics (§35), tapu/rank (§41), boundaries (§46).
- **Does not answer:** the chain. Line 39 records plica polonica as “the effect of a
  spell cast by witch or a punishment from God” — a medical belief with an offstage
  agent; no accuser, no procedure, no proof. It owns none of the six neighbour surfaces.

### 4.4 `myth-symbol/amulets-talismans-apotropaic-marks.md` — lines 4, 39, 72, 102, 104, 158

- **Owns:** protective objects as a system — word field (§3), danger table (§4),
  mechanism (§5), material/form (§6), placement (§7), written protection (§8), makers
  (§9), life cycle (§10), build order (§11), calibration bank (§12).
- **Does not answer:** the chain. Uses of the surface: line 4 is an absence probe
  (`witch mark` 0 files); line 39 quotes a dictionary sense (“preventative against …
  witchcraft”); lines 72/104 are the witch-bottle mechanism; line 102 is **witches'
  marks as apotropaic scratches on buildings**; line 158 is a calibration flag against
  promoting sympathetic magic.
- **Homonym trap, observed:** “witches' marks” at line 102 are building marks that
  *repel* harm, not the bodily “witch's mark” sought as evidence. The same English words
  name two different objects; this file owns only the first.
- **Neighbour routing it already declares:** §2 rows point `binding-speech-complex.md`
  §5.2 one-way for the spoken curse (line 22) and `purity-pollution-boundary-systems.md`
  §4 for contamination carriers (line 24); §8 points back at line 121. It owns amulets;
  it does not own divination, binding speech, colour (it points to `color-symbolism.md`
  §6 at line 26), funerary or purity.

### 4.5 `myth-symbol/animal-symbolism.md` — line 9

- **Owns:** fauna as symbolic substrate — mechanism typology (§3), guardians (§4), food
  law (§5), zodiac (§6), heraldry (§7), serpent (§8), biogeography (§9), kotodama hooks
  (§10).
- **Does not answer:** the chain. The line is a bibliography row; the surface occurs only
  inside the title *Cows, Pigs, Wars and Witches*. Owns none of the six neighbour
  surfaces (it cites Douglas for purity but does not own purity).

### 4.6 `myth-symbol/binding-speech-complex.md` — lines 26, 164

- **Owns:** the oath, curse, blessing and name-power as one machinery — master channel
  table (§3), oath (§4), curse physics and counter-curse (§5), blessing (§6), name-power
  (§7), enforcement ledger (§8), release (§9).
- **Does not answer:** the chain. Line 26 is a source-list item (Qur'an 2:102, “sorcery
  taught in Babylon”); line 164 is the **prohibition** clause — Qur'an 2:102/5:90 place
  sorcery and divining arrows “outside the permitted”, converting a technology into a
  sin. That is a legal-theological verdict on the practice, not a procedure for
  accusing, trying, proving or confessing a person. §5.1 routes scapegoat/substitute to
  `ritual-liminality.md` §4 one-way. Owns binding speech; not amulets (§5.2 points
  there), not divination (§11 pointer), not colour, funerary or purity.

### 4.7 `myth-symbol/color-symbolism.md` — line 22

- **Owns:** colour as an enforceable code — calibration rule (§1), framework table (§2),
  five-colour family (§3), white (§4), black/white dualism (§5), red (§6), yellow (§7),
  blue/green (§8), purple (§9), scarcity and enforcement (§10), calibration flags (§11).
- **Does not answer:** the chain. Line 22 is one cell of Turner's Ndembu triad table:
  black = “sorcery/bad death/disease”, flagged as a single-culture study. “Sorcery” is a
  valence gloss in a colour system, not an accusation category. Owns colour; not
  amulets, divination, binding speech, funerary or purity (lexicon side is
  `linguistics/color-terminology.md`).

### 4.8 `myth-symbol/divination-omen-systems.md` — lines 13, 112

- **Owns:** divination as a symbolic technology — core frame (§2), fourteen-family
  technique typology (§3), interpretive engine (§4), institutions and reading licences
  (§5), omen archives (§6), word-omen channel (§7), explicit boundary (§8).
- **Does not answer:** the chain, but it is the closest neighbour to the *diagnosis*
  moment. Line 112 (“What did I do wrong” → Ifa; Azande witchcraft diagnosis →
  prescription → “generates the offering economy and the confession scene”) owns the
  oracle's naming of an offence and the prescription; it does not own denunciation,
  prosecution, proof, confession-as-evidence, slander law or social functions.
  Line 13 is the Evans-Pritchard bibliography row.
- **Declared boundary:** §8 points sacrifice typology to `ritual-liminality.md` §4/§5
  (line 154) and name taboo/name magic to `../linguistics/naming-systems.md` (line 155).
  Owns divination; not amulets, binding speech, colour, funerary or purity.

### 4.9 `myth-symbol/myth-folktale-genres.md` — line 54

- **Owns:** the narrative classification spine — Bascom's four forms (§1), Motif-Index
  and ATU (§2–§3), myth as charter (§4), genre strata (§5), euhemerism (§6),
  calibration (§7), house genre rules (§8).
- **Does not answer:** the chain. Line 54 lists ATU 325 *The Sorcerer's Apprentice* as a
  tale type; a sorcerer in a Märchen is a character slot, not an accused person. Owns
  none of the six neighbour surfaces.

### 4.10 `myth-symbol/myth-ritual-theories.md` — lines 12, 53

- **Owns:** classical theories of myth and their scholarly status — myth-ritual school
  (§2), euhemerism (§3), allegory/nature-myth (§4), functionalism (§5), structuralism
  (§6, pointer), depth psychology (§7), feminist/goddess line (§8), Dumézil (§9), master
  table (§10), theories as in-world positions (§11).
- **Does not answer:** the chain. Line 12 is a bibliography row (Kluckhohn 1944,
  *Navaho Witchcraft*); line 53 is functionalism's one-line use of it (“Kluckhohn (1944)
  runs it on witchcraft ideology”) — a *why-does-the-ideology-persist* argument, not a
  procedure, proof technology, confession, slander law or typology of accusations.
  Owns none of the six neighbour surfaces.

### 4.11 `myth-symbol/symbolism-synthesis-method.md` — line 28

- **Owns:** the five-register generation method — grammar definition (§1), framework
  table (§2), steps 0–8 (§3), register notes (§4), consistency rules (§5), change rules
  (§6), audit checklist (§7), calibration (§8), worked example (§9), handoff (§10).
- **Does not answer:** the chain. Line 28 is the Ndembu triad used as an exemplar of a
  closed system (“black = sorcery, badness”). Owns method; not colour as content, not
  amulets, divination, binding speech, funerary or purity.

### 4.12 Widened-lexeme additions (same classification)

- `civilizations/kongo-kingdom.md:45` — source shelf row: “Gallo calls Kimpa Vita a
  possessed sorceress: weigh it as testimony against her”. Owns the Kongo reference
  base and this hostile-witness caution; no procedure, no proof, no law.
- `myth-symbol/monsters-hybrid-beings.md:119,122` — restricted-beings section: “publish
  the rule, withhold the content”; Diné witchery is named as a restricted kind of talk,
  with Denetdale as the speaker of the norm. Owns monster category and circulation
  ethics; no institution.

---

## 5. Chain-element coverage (six elements, one row each)

| chain element | nearest owner(s) | what that owner actually answers | what remains unowned |
|---|---|---|---|
| vocabulary set | no owner; cautions at `mongol.md:193`, `yoruba.md:122`; bibliographic Evans-Pritchard (`divination:13`) and Kluckhohn (`myth-ritual:12`) | that “witch” imports a demonizing European category; that hostile reporters use the word as a judgment | the emic term set, its register stratification (learned maleficium vs popular sortilege), the gender/age/status distribution of the label, the translation traps in a named language |
| accusation grammar | no owner; nearest `divination-omen-systems.md:112` (diagnosis → prescription) | how an oracle names an offence and prescribes an offering; that the diagnosis “generates … the confession scene” | who may accuse, at what stage (suspicion, denunciation, formal libel), the accused's answer, the political timing of a prosecution, the relation of accusation to feud and to lordship |
| proof technology | `myth-symbol/ordeal-judicial-proof-rituals.md` (general); `purity-pollution-boundary-systems.md:105` (ordeal as a pollution discharge) | the proof ladder oath → compurgation → ordeal → battle, the ordeal menu, the inspection grammar, the administrator's economy, the decay markers (`ordeal:3`, §1 at `:12–18`, §2 six decisions) | any witch-specific proof: swimming, bodily mark and pricking, spectral evidence, torture as proof manqué; the ordeal file contains **0** witch/sorcer tokens and its §1 boundary names only oath, divination, liminality, liturgy, periodization |
| confession | no owner; partial `purity:104` (confession/declaration as a purification discharge, “the confession is itself a speech act”), `divination:112` (confession scene as a consequence), `binding:26` (Varuṇa confession in a source list) | that confession can discharge pollution and needs “an audience and an authority”; that a divination prescription produces a confession scene | confession as evidence: its evidentiary weight, the torture–confession relation, formula and uptake, the retraction rule, confession as a public theatre |
| slander law | no owner; passing `marriage-alliance-bridewealth.md:88` (Hammurabi §161: a slandering third party cannot acquire the bride — a marriage remedy), `ritual-garments.md:57` (lashon hara), `creation-myths-taxonomy.md:104` (blasphemy/defamation listed as cosmic crimes, not built), `bathing-and-body-hygiene.md:96` (rhetorical “slander”) | a marriage remedy for a slanderer; a garment symbolism for lashon hara; a one-line coupling note | the counter-suit for false accusation, the price of a false imputation against a person vs against a craft, the difference between defamation and heresy, who may sue |
| social functions | no owner; partial `myth-ritual-theories.md:53` (functionalism/Kluckhohn), `ritual-liminality.md:57` (piacular sacrifice — “the institution that decides who is the pollution”), `purity-pollution-boundary-systems.md:65–79` (five attribution regimes; “a system where every pollution has a culprit is a system with a courtroom”), `purity:111` (enforcement, economy, profession) | why an ideology persists (charter); who is declared pollution and by which regime; the purification economy | envy, scapegoating, purge, accusation as a resource, the political economy and demography of accusations, the difference between village and state prosecution |

Observed coverage count: **1 of 6** chain elements has a general (non-witch) owner —
proof technology, in `ordeal-judicial-proof-rituals.md`. **0 of 6** has a witch-specific
owner.

---

## 6. Neighbour-surface owners (the six surfaces named in the seat spec)

| surface | owning file | exact scope boundary it declares |
|---|---|---|
| amulets | `myth-symbol/amulets-talismans-apotropaic-marks.md` | protective objects and marks (§2 table); it points curse speech to binding-speech §5.2 and carriers to purity §4 |
| divination | `myth-symbol/divination-omen-systems.md` | question → technique → sign → reader → prescription; §8 excludes sacrifice, names, sky, tale indexing |
| binding speech | `myth-symbol/binding-speech-complex.md` | oath, curse, blessing, name-power; §8 enforcement ledger; §5.1 points scapegoat to ritual-liminality §4 |
| colour symbolism | `myth-symbol/color-symbolism.md` | colour code as term × carrier × practice × authority × enforcement; lexicon in `linguistics/color-terminology.md` |
| funerary | `culture-material/funerary-material-culture.md`; `myth-symbol/death-afterlife-eschatology.md` | disposal/assemblage/monument/word (`funerary:4`); death doctrine and judgment machines (`death:4`) |
| purity | `myth-symbol/purity-pollution-boundary-systems.md` | seven polarity axes, anomaly engine, four carriers, five attribution regimes, discharge ledger, enforcement (§1–§14); confession row at `:104`, ordeal row at `:105` |

Two further non-mentioning neighbours matter to the chain and are named here because they
own ground the new entry would otherwise duplicate:

| file | owns | chain-adjacent line |
|---|---|---|
| `myth-symbol/ordeal-judicial-proof-rituals.md` | the proof ladder and ordeal system | §1 at `:12–18`; six decisions §2 |
| `myth-symbol/ritual-liminality.md` | rite structure, sacrifice typology, substitution | `:57` piacular row: “the institution that decides who is the pollution” |

---

## 7. Frontier extraction (`corpus/README.md` `## Known gaps (frontier)`, lines 609–788)

### 7.1 Inventory — 17 bullets

| line | subject (one line) | bears on ritual institutions? | names the surface? |
|---|---|---|---|
| 611 | round-5 per-claim rechecks on five civilization entries; 15 residuals open | no | no |
| 622 | round-6 fixed questions; 9 scoped / 11 partial / 4 unresolved | no | no |
| 635 | replay-frozen gates; 17 `expected.json` pins | no | no |
| 643 | most historical entries lack the full fleet header | no | no |
| 646 | D2 typed native-form/translated-label needs | no | no |
| 657 | D3 culture packet; round-7 acceptance recorded false | no | no |
| 671 | five round-7 live constraint rechecks | no | no |
| 676 | round-10 ten thin-partition entries (myth-symbol 3); historical precedent | marginal (partition precedent) | no |
| 690 | earlier round-local acceptance scripts keep strict path whitelists | no | no |
| 694 | cultural permission, real-language name screening, lore receipt, independent promotion review — outside the evidence | **yes** (governs living-tradition material) | no |
| 696 | round-19 ten thin-partition entries (verification 5, synthesis 5) | no | no |
| 714 | round-20 index reconciliation and its open list | no | no |
| 735 | round-64 language-socialization entry; 0 filename / 0 topic owners before | marginal (thin-partition precedent) | no |
| 736 | round-66 scent/perfume register; incense-adjacent neighbours | **yes** (ritual material adjacent) | no |
| 737 | round-67 medicine-healing register; partial scopes include “`myth-symbol/` apotropaic purity scopes” | **yes** (apotropaic/purity scopes stay partial) | no |
| 738 | round-65 games/sport register | no | no |
| 739 | round-74 worldbuilding-setting practice + amendment | no | no |

Count: **17 bullets; 0 name the surface; 4 bear on ritual-institution work**
(676, 694, 736, 737).

### 7.2 Which frontier row does this entry advance?

**None of the 17 by name.** No frontier bullet records a witchcraft/sorcery/accusation
content gap, so the D entry cannot close or advance a named row. What it does is repeat
the *unnamed-gap* landing pattern that bullets 735/736/737/739 describe for other
themes (0 filename owners, 0 topic-line owners, partial one-way owners remain), and it
extends the myth-symbol partition from 35 to 36 files. Whether that pattern deserves a
new frontier row is not this seat's call; the census above is the evidence such a row
would need.

### 7.3 Touched but not closed

- **`corpus/README.md:737` (round 67, medicine-healing).** The bullet's partial-scope
  list names “`myth-symbol/` apotropaic purity scopes”. The D entry consumes the
  apotropaic object (`amulets…`) and the purity apparatus (`purity…`) one-way; it adds a
  consumer of those scopes, it does not close the round-67 partial-scope statement.
- **`corpus/README.md:694` (cultural permission / name screening / lore receipt /
  independent promotion review).** The D surface is exactly the kind that touches living
  traditions (àjẹ́, Diné witchery, Azande diagnosis) and hostile historical testimony
  (Gallo on Kimpa Vita). The existing corpus already marks these as cautions; the
  frontier row remains outside the current evidence and is not advanced by any entry.

### 7.4 Leaves open

All 17 rows remain open, in particular: the rounds 5–7 evidence residuals (611, 622,
671), the header-conformance question (643), the D2/D3 items (646, 657), the round-67
partial apotropaic/purity scopes (737), and the standing permission/name-screening row
(694). Separately, the file-count drift is open housekeeping rather than a frontier row:
the newest footer (`corpus/README.md:834`) says 253 while the tree holds 257 at base
(258 after landing), and the myth-symbol heading (`:376`) says 32 while the partition
holds 35 (36 after landing).

---

## 8. Limits and confidence

- **Method.** All sweeps are read-only `git grep` / `git ls-tree` at the base revision;
  Markdown prose has no semantic index in this lane, so the census is literal text plus
  manual role reading of every hit (all 22 widened lines were opened in context). No LSP
  server applies to `.md`; this is recorded as the fallback condition, not as semantic
  proof.
- **Pattern sensitivity, measured.** The assigned pattern (`\bwitch\b` etc.) misses
  `witchery` and `sorceress`; the widened stem set adds 3 lines / 2 files, all passing.
  A naive substring search adds false positives (`switch`, `strigil`) and was rejected.
- **Counts that are claims, not measurements.** 258 is the claim's arithmetic
  (257 + 1); this census measured 257 and the absence of the target basename at base.
- **Concurrent writes.** The census reads the base tree, so later worktree changes cannot
  invalidate it. The worktree was clean for `corpus/knowledge` when checked.
- **Confidence.** Owning-basename absence: certain at base (0/257). Owning topic-line
  absence: certain for the literal pattern; high for the widened set (every hit read).
  Partial-owner map: high for the cited lines; the “does not answer” judgments are
  reading-based, not machine-checked.
