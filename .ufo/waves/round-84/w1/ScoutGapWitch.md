# ScoutGapWitch — claim-D absence census (round 84, w1)

Milestone `r84-v1`. Read-only recon at the base revision `81499ee45b5751d388fefc78583810878de01ecd`
(frozen claims `3ca2cf28`). No file outside this seat's stage directory and this report was
written; no canon recommendation; no git/jj mutation.

**Verdict — before-state CONFIRMED.** At base, no knowledge file owns witchcraft/sorcery as an
accusation institution:

- **0** owning basenames in 257 knowledge files (filename sweep, rc=1).
- **0** owning `- topic:` lines (assigned scan and widened scan, rc=1 each).
- **19** occurrence lines in **11** files under the assigned pattern; every one is a passing
  attribute (bibliography title, translation/source caution, table cell, artifact name, one
  dictionary gloss, one absence probe, one prohibition clause) — none defines or tabulates the
  institution.
- **1** of 60 `- gap filled:` lines contains a surface token and it is an **absence probe**
  (`witch mark` occurs in 0 files), so **0** lines claim the surface as an owned gap.
- **22** lines in **13** files under a widened lexeme scan (adds `witchery`, `sorceress`), all
  likewise passing — the absence is not an artefact of the assigned pattern.
- The 17-bullet frontier names the surface **0** times and **no named row is advanced** by this
  entry.

## Axes (godspeed)

1. **Absence-proof strength** — base-pinned tree reads, exact pattern + widened lexeme control +
   gap-filled scan, every hit opened in context.
2. **Owner-map completeness** — all 11 mentioning files mapped one-way, plus 6 non-mentioning
   chain neighbours (proof, purity, liminality, funerary, death, law).
3. **Frontier honesty** — all 17 frontier bullets inventoried; advance/leave-open stated without
   inventing a row.
4. **Artifact parseability** — pipe table `(file, owner, lines)` in the census; `gap-census.json`
   validated with `python3 -m json.tool`; no absolute paths anywhere.

---

## 1. Before-state: commands and raw output

Run from the lane root (`kotodama-shokunin`). Worktree was byte-identical to base for
`corpus/knowledge` when checked: `git diff --stat 81499ee4 -- corpus/knowledge` and
`git status --porcelain corpus/knowledge` both printed nothing.

### A. Filename sweep

```
$ git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge \
    | grep -iE 'witch|witches|witchcraft|sorcer|sorcery|malefic'
(no output)
rc=1

$ git ls-tree -r --name-only 81499ee45b5751d388fefc78583810878de01ecd -- corpus/knowledge \
    | grep -c '\.md$'
257
```

`git ls-tree … | grep -i 'accusation-institution'` also printed nothing (rc=1): the target
basename is absent at base.

### B. Matter-of-subject scan

```
$ git grep -nE '^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
(no output)
rc=1
```

Widened topic scan (`witch|sorcer|malefic|venefic|strig`, up to 200 chars after
`- topic: `):

```
$ git grep -nE '^- topic: .{0,200}(witch|sorcer|malefic|venefic|strig)' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:3:- topic: The naked-eye sky as the worldbuilder's highest-yield symbolic system — sun/moon deity gender assignments across cultures (no universal pattern; aspect-switching), the planet-as-god interpretatio chain (Babylonian → Greek/Roman → Germanic/Chinese/Indian/Maya), constellation vs asterism as a naming problem, the Pleiades as the most calendrically overloaded object worldwide, Milky Way figure typology, eclipse-omen systems and their rituals and archives, the mechanics by which celestial cycles anchor calendars and festivals; with a calibration section on discredited celestial-myth schools
rc=0   (the single hit is the substring "aspect-switching", not the surface)
```

**0 real topic owners.**

### C. Word-boundary occurrence census (assigned pattern)

```
$ git grep -niE '\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
```

19 lines / 11 files. Per-file distribution: amulets 6; binding-speech 2; divination 2;
myth-ritual-theories 2; mongol 1; yoruba 1; hair-grooming 1; animal-symbolism 1;
color-symbolism 1; myth-folktale-genres 1; symbolism-synthesis-method 1. Verbatim block in
§6; receipt `.ufo/waves/round-84/w1/stage/ScoutGapWitch/census-exact.tsv`.

Role census (one role per line):

| role | count | lines |
|---|---|---|
| bibliographic title in a source list | 5 | animal-symbolism:9, binding-speech:26, divination:13, myth-folktale-genres:54, myth-ritual-theories:12 |
| translation / source-criticism caution | 2 | mongol:193, yoruba:122 |
| passing exemplar or table cell | 5 | hair-grooming:39, color-symbolism:22, divination:112, myth-ritual-theories:53, symbolism-synthesis-method:28 |
| artifact name (witch bottle / witches' marks) | 4 | amulets:72, 102, 104, 158 |
| dictionary definition of a neighbouring word | 1 | amulets:39 |
| absence probe inside `- gap filled:` | 1 | amulets:4 |
| prohibition clause (sorcery as sin) | 1 | binding-speech:164 |

**Widened lexeme control** (the assigned pattern is blind to `witchery` and `sorceress`):

```
$ P='\b(witch[a-z]*|bewitch[a-z]*|sorcer[a-z]*|malefic[a-z]*|venefic[a-z]*|strig(a|ae|oi|e)\b|incubus|succubus)'
$ git grep -niE "$P" 81499ee4 -- 'corpus/knowledge' | wc -l
22
$ git grep -liE "$P" 81499ee4 -- 'corpus/knowledge' | wc -l
13
```

The 3 added lines are all passing: `civilizations/kongo-kingdom.md:45` (`sorceress` in a
source-criticism note — “Gallo calls Kimpa Vita a possessed sorceress: weigh it as testimony
against her”); `myth-symbol/monsters-hybrid-beings.md:119` and `:122` (`witchery` in the
restricted-beings section — publish the rule, withhold the content; Denetdale: “We don't talk
about witchery”). A naive substring scan is rejected: it adds `switch`/`aspect-switching`,
`strigil`, and `code-switching` false positives.

### D. `- gap filled:` lines

```
$ git grep -niE '^\- gap filled:.*(witch|sorcer|malefic)' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge'
81499ee45b5751d388fefc78583810878de01ecd:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:4:- gap filled: at the claim base no file under `corpus/knowledge` owns protective objects as a system. Filename sweep `git ls-tree -r --name-only d4795abd corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` → 0; `evil eye`, `nazar`, `mezuz`, `omamori`, `ofuda`, `phylacter` and `witch mark` occur in 0 files (`.ufo/waves/round-59/build/ConnectInLaneAmulets59.md` §1). Partial owners hold single links of the chain (danger, carrier, material, surface, deposition); §2 routes each one-way.
rc=0

$ git grep -nE '^- gap filled:' 81499ee45b5751d388fefc78583810878de01ecd -- 'corpus/knowledge' | wc -l
60
```

Measured: 1 token line of 60, and it is an absence probe, not ownership → **0** ownership
claims. A wider accusation-chain probe (`accus|inquisit|ordeal|confess|slander|defam|witch|sorcer|malefic`)
returns 2 lines, both absence probes (amulets:4 and
`myth-symbol/ordeal-judicial-proof-rituals.md:4`).

### E. Outside `corpus/knowledge` (context only)

```
$ git grep -niE '\b(witch|witches|witchcraft|sorcerer|sorcery|malefic)\b' \
    81499ee45b5751d388fefc78583810878de01ecd -- 'corpus' ':!corpus/knowledge' \
  | sed -E 's/^([0-9a-f]+):([^:]+):([0-9]+):.*/\1:\2:\3/' | awk -F: '{print $2}' | sort | uniq -c
      1 corpus/lessons/round-55.md
      3 corpus/lessons/round-59.md
      1 corpus/lessons/round-68.md
      7 corpus/SOURCES.md
```

The 7 S-id rows: S019 (ISEBEL), S332/S333 (Motif-Index), S621 (*Witches' Marks*, Provan Hall),
S622 (*Witch-bottles and healing charms*, Museum Wales), S644 (Pitt Rivers amulets leaflet),
S854 (plica polonica). None is an accusation-institution source row. Six of the seven are
already cited by entries (amulets: S621, S622, S644; hair-grooming: S854; monsters-hybrid-beings:
S332, S333); S019 (ISEBEL) is the only uncited row. `corpus/README.md` has **0** real surface
tokens (its only substring hit is `aspect-switching`).

---

## 2. Partial-owner map (one-way)

Machine-readable summary `(file, owner, lines)`:

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
| corpus/knowledge/myth-symbol/symbolism-synthesis-method.md | five-register symbol-generation method | 28 |
| corpus/knowledge/civilizations/kongo-kingdom.md | Kongo reference base (source shelf, language, Antonians) | 45 |
| corpus/knowledge/myth-symbol/monsters-hybrid-beings.md | monsters as a cultural category; restricted beings | 119, 122 |

(The last two are the widened-lexeme additions.)

### What each does not answer

All 13 files fail the six chain elements (vocabulary set, accusation grammar, proof technology,
confession, slander law, social functions). Per file, the nearest thing it owns:

- **mongol.md:193** — a source-criticism caveat: Rubruck's “Idol”, “devil”, “witchcraft” are “his
  judgments, not neutral translations”. Owns the Mongol reference base; no procedure, no proof,
  no law.
- **yoruba.md:122** — a translation caution: “Translate àjẹ́ … carefully; ‘witch’ can import a
  demonizing European category”. The file refuses the very equation the institution analyses; it
  does not own divination in general (Ifá is a bounded register here).
- **hair-grooming-codes.md:39** — plica polonica as “the effect of a spell cast by witch or a
  punishment from God”: an offstage agent in a medical belief; no accuser, no proof.
- **amulets-talismans-apotropaic-marks.md** — owns protective objects (§3–§12). Line 4 is an
  absence probe; 39 a dictionary gloss; 72/104 the witch-bottle mechanism; 102 **witches' marks as
  apotropaic scratches on buildings**; 158 a calibration flag. *Homonym trap:* those building
  marks repel harm; they are not the bodily “witch's mark” sought as evidence. §2 already routes
  curse speech to binding-speech §5.2 (line 22) and contamination carriers to purity §4
  (line 24).
- **animal-symbolism.md:9** — bibliography title only (*Cows, Pigs, Wars and Witches*).
- **binding-speech-complex.md:26,164** — owns oath/curse/blessing/name-power and the
  **prohibition** (Qur'an 2:102/5:90 put sorcery “outside the permitted”, a sin not a procedure).
  Line 26 is a source-list item; §5.1 routes scapegoat/substitute to ritual-liminality §4.
- **color-symbolism.md:22** — one Ndembu triad cell, “black = sorcery/bad death/disease”, flagged
  single-culture; a valence gloss, not an accusation category.
- **divination-omen-systems.md:13,112** — owns the oracle's **diagnosis** slot: “What did I do
  wrong” → Azande witchcraft diagnosis → prescription → “generates … the confession scene”.
  Line 13 is the Evans-Pritchard bibliography row. §8 excludes sacrifice (ritual-liminality §4/§5,
  line 154) and name magic (naming-systems, line 155).
- **myth-folktale-genres.md:54** — ATU 325 *The Sorcerer's Apprentice* in a tale-type table; a
  character slot, not an accused person.
- **myth-ritual-theories.md:12,53** — Kluckhohn 1944 bibliography; functionalism “runs it on
  witchcraft ideology” — a why-persists argument, not a procedure or a typology of accusations.
- **symbolism-synthesis-method.md:28** — Ndembu triad as a closed-system exemplar; “sorcery” is a
  colour valence.
- **kongo-kingdom.md:45** — hostile-witness caution: Gallo's “possessed sorceress” label is
  testimony against Kimpa Vita, to be weighed, not repeated.
- **monsters-hybrid-beings.md:119,122** — restricted circulation norm: “publish the rule,
  withhold the content”; Diné witchery is named as restricted talk with its speaker recorded.

### Chain-element coverage

| element | general owner | what is actually answered | unowned |
|---|---|---|---|
| vocabulary set | none | that “witch” imports a European category (mongol, yoruba); hostile reporters use it as a judgment (kongo) | emic term set, register strata, gender/age/status distribution, translation traps |
| accusation grammar | none | oracle diagnosis → prescription (divination:112) | who may accuse, suspicion → denunciation → trial, the answer, political timing |
| proof technology | `myth-symbol/ordeal-judicial-proof-rituals.md` (general) | oath → compurgation → ordeal → battle, ordeal menu, inspection grammar, administrator's economy (`:12–18`); purity:105 owns ordeal as a discharge | witch-specific proofs (swimming, bodily mark/pricking, spectral evidence, torture as proof manqué); the ordeal file has 0 witch/sorcer tokens |
| confession | none | confession as purification discharge, “itself a speech act” (purity:104); confession scene as narrative consequence (divination:112); Varuṇa confession in a source list (binding:26) | confession as evidence, torture–confession, formula/uptake, retraction |
| slander law | none | Hammurabi §161 marriage remedy (marriage:88); lashon hara (ritual-garments:57); a one-line coupling (creation-myths:104) | counter-suit for false accusation, price of imputation, defamation vs heresy, standing |
| social functions | none | charter/why-persists (myth-ritual:53); piacular “institution that decides who is the pollution” (ritual-liminality:57); five attribution regimes (purity:65–79) | envy, scapegoat, purge, accusation as resource, political economy and demography |

Coverage: **1/6** elements has a general (non-witch) owner; **0/6** has a witch-specific owner.

### Neighbour-surface owners named in the seat spec

| surface | owner |
|---|---|
| amulets | `myth-symbol/amulets-talismans-apotropaic-marks.md` |
| divination | `myth-symbol/divination-omen-systems.md` |
| binding speech | `myth-symbol/binding-speech-complex.md` |
| colour symbolism | `myth-symbol/color-symbolism.md` |
| funerary | `culture-material/funerary-material-culture.md`; `myth-symbol/death-afterlife-eschatology.md` |
| purity | `myth-symbol/purity-pollution-boundary-systems.md` |

Two non-mentioning neighbours also own chain ground: `myth-symbol/ordeal-judicial-proof-rituals.md`
(proof ladder, §1 at `:12–18`) and `myth-symbol/ritual-liminality.md` (`:57`, piacular row).

---

## 3. Frontier extraction (`corpus/README.md` `## Known gaps (frontier)`, lines 609–788)

17 bullets at lines 611, 622, 635, 643, 646, 657, 671, 676, 690, 694, 696, 714, 735, 736,
737, 738, 739. **0 mention the surface.** Four bear on ritual-institution work:

| line | subject | bearing |
|---|---|---|
| 676 | round-10 thin-partition entries; myth-symbol 3 | partition precedent only (historical) |
| 694 | cultural permission, real-language name screening, lore receipt, independent promotion review outside the evidence | the surface touches living traditions (àjẹ́, Diné witchery, Azande diagnosis) and hostile testimony (Gallo) — this row governs that material and stays open |
| 736 | round-66 scent/perfume register; incense-adjacent neighbours | adjacent ritual material only |
| 737 | round-67 medicine-healing; partial scopes include “`myth-symbol/` apotropaic purity scopes” | the entry consumes amulets + purity one-way; the partial-scope statement stays partial |

**Advances:** none of the 17 named rows. No frontier bullet records a witchcraft/sorcery/
accusation content gap, so the entry cannot close or advance a named row; it repeats the
unnamed-gap thin-partition pattern of bullets 735/736/737/739 and moves the myth-symbol
partition from 35 to 36 files.

**Leaves open:** all 17, in particular 611/622/671 (rounds 5–7 evidence residuals), 643
(header conformance), 646/657 (D2/D3), 737 (partial apotropaic/purity scopes), 694 (permission
and name screening). Housekeeping drift also stays open: the newest footer
(`corpus/README.md:834`) says 253 entries while the tree holds 257 at base (258 after landing);
the myth-symbol heading (`:376`) says 32 while the partition holds 35 (36 after landing). The
three unindexed myth-symbol files are exactly `guest-right-hospitality-law.md` (2026-11-04),
`marriage-alliance-bridewealth.md` (2026-11-04) and `ordeal-judicial-proof-rituals.md`
(2026-11-01). The README footer/heading drift is pre-existing and untouched by this seat.

---

## 4. Confidence and remaining unknowns

- **Certain at base:** 0 owning basenames (0/257), 0 owning topic lines (assigned and widened),
  target basename absent, 19/11 and 22/13 counts, 1/60 gap-filled token line (an absence probe).
- **High, reading-based:** the role classification of all 22 widened hits (every line opened in
  context) and the “does not answer” judgments in §2.
- **Method limit:** Markdown prose has no semantic index in this lane; no LSP server applies, so
  grep is the literal fallback. No non-English or binary knowledge files exist to scan.
- **Stated as claims, not measurements:** 258 is the claim's arithmetic (257 + 1); this census
  measured 257 and the absent basename.
- **Open questions left to other seats:** whether the D entry disambiguates the two `witch's
  mark` objects (building apotropaion vs bodily evidence); whether a future frontier row records
  this gap; whether S621/S622 wording supports the bodily-mark distinction (not opened here —
  source reading is outside this seat's scope).

---

## 5. Artifacts

Repo-relative, all under the seat stage:

- `.ufo/waves/round-84/w1/stage/ScoutGapWitch/gap-census.md` — full census, commands, raw output,
  partial-owner map, frontier table.
- `.ufo/waves/round-84/w1/stage/ScoutGapWitch/gap-census.json` — exact counts (validated with
  `python3 -m json.tool`).
- `.ufo/waves/round-84/w1/stage/ScoutGapWitch/census-exact.tsv` — the 19 verbatim lines.

Scratch directory was removed; nothing was left behind. The receipt above was written
directly under the stage path (the scratch intermediate was a duplicate and was deleted).

---

## 6. Appendix — verbatim 19-line census

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
