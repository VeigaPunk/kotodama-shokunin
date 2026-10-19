# K04 — independent gap verification: fresh absence sweep at the 223 total

- Seat: `K04` (scout, claim **C**, second gap scout independent of K02)
- Out path: `reports/round-44/scout/K04-gap-verify.md`
- Baseline: `git rev-parse HEAD` → `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (declared baseline `c9f4eaa`, `reports/round-44/claims.json:7`)
- Observation time: 2026-10-19T17:22:20Z (UTC)
- Working tree at observation: `git status --porcelain` → `?? reports/round-44/` only; no corpus byte touched by this seat.
- Mission (verbatim, `reports/round-44/targets.json` seat `K04`): *"Second gap scout (independent of K02): run your own fresh absence sweep at 223 and either confirm K02's named gap is unowned or name a different unowned gap; corroborate the one-owner-per-topic precondition before any landing."*

**Result in one line:** the wave has no K02 output yet (`reports/round-44/scout/` was empty at write time), so this seat names its own independently verified gap: the **dream / vision / trance altered-state complex**, proposed path `corpus/knowledge/myth-symbol/dream-vision-trance.md`. It is absent at `c9f4eaa`, no entry's `- topic:` line owns the complex (2 adjacent hits, both explained below), the slug collides with no corpus filename, and it sorts between `divination-omen-systems.md` and `eschatology-world-end-systems.md`. Total 223 → 224; myth-symbol 26 → 27.

---

## 1. Baseline measurement (all commands run from the lane root)

```
$ git rev-parse HEAD
c9f4eaa707b6e977ff6e1616463e91f4b8afea5d

$ find corpus/knowledge -name '*.md' | wc -l
223

$ for d in corpus/knowledge/*/; do printf '%s=%s ' "$(basename $d)" "$(find $d -name '*.md' | wc -l)"; done
civilizations=94 culture-material=25 linguistics=25 myth-symbol=26 synthesis=29 verification=24

$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0

$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge | head
  "totals": { "files": 223, ... }
```

The index is green at 223 and the pinned README digest is `7c788a1d…ef31cdcd`. The live partition matches the claim C `before` (223 total) exactly.

---

## 2. Method — two tests, then the collision/sort checks

Adopted from the r42 gap-scout method (`reports/round-42/scout/K02-myth-gaps.md:96-105`) so the result is comparable to prior sweeps, but every number below was re-measured at `c9f4eaa`, not carried:

1. **Demand sweep** — regex over the full text of all 223 entries, counting distinct files. High demand means the corpus *uses* the domain.
2. **Topic-ownership test** — the same regex over each entry's single `- topic:` line. A hit means some entry *names the domain as its subject*. A candidate is a gap signal when demand is high and relevant topic-owners are zero, or the owners are adjacent by-product only.
3. **Heading test** — `^#{1,4} ` headings matching the domain, to catch an entry that owns the domain in a section without naming it in the topic line.
4. **Slug/collision test** — `find corpus/knowledge -iname '*<term>*'` and a `LC_ALL=C sort` insertion check against the live partition listing.

No prior-round absence claim is used as a premise. The r43 defect is the reason: the r43 C claim asserted the lithic slot was "named but unbuilt" while `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` already existed at its close commit (`reports/round-43/scout/K02-landing-scout.md:190-206`; `reports/round-43/review/R01-review.md:400`, R01-43-12). Every ownership statement here is a command run at `c9f4eaa`.

---

## 3. Candidate table (223 entries, measured at `c9f4eaa`)

Clean regexes with word boundaries; `demand` = distinct files whose body matches; `owners` = distinct files whose `- topic:` line matches.

| candidate | demand /223 | topic-owners | relevant owners? | verdict |
|---|---:|---:|---|---|
| **dream / vision / trance** (`dream(s|ing|er|t)`, `trance`, `ecsta*`, `shaman*`, `incubat*`, `vision quest`, `visionary`) | **52** | **2** | `myth-symbol/divination-omen-systems.md` owns the *reading technology* (dream-oracle row 12); `civilizations/mongol.md` is a civilization base carrying "shamanic vocabulary" | **unowned system — recommended** |
| gesture / sign / whistle / drum speech (`gesture*`, `sign language`, `signed language`, `whistl*`, `drum speech/language/talk`, `kinesic*`) | 45 | **0** | — | genuine gap, but in-corpus source shelf is thin (see §7) |
| metallurgy process (`metallurg*`, `smelt*`, `forge*`, `alloy*`, `ore(s)`, `casting`, `blacksmith*`) | 42 | 1 | `divination-omen-systems.md` — false positive: "casting lots", not metal casting | partly owned by `craft-artisan-lexicon.md` (material-grading bank, tools, marks); overlap risk |
| monster / terato (`monster(s)`, `monstrous`, `terato*`, `ogre(s)`) | 13 | **0** | — | thin demand; `dragon`/`chaoskampf` already rows in `hero-journey-variants.md` and `creation-myths-taxonomy.md` |
| games / sport (`game(s)`, `sport(s)`, `athletic*`, `toy(s)`, `gambling`, `board/ball game(s)`) | 40 | 1 | `transport-mobility-lexicon.md` — incidental ("game trail" sense); not an owner | genuine gap, but no in-corpus shelf (Huizinga 0 files, Caillois 0, Parlett 0) |
| sacrifice / offering | 92 | 3 | `ritual-liminality.md` **owns sacrifice typology** (explicit in `divination-omen-systems.md:154`: "sacrifice typology, calendrical rites") | owned — do not propose |
| marriage / alliance | 78 | 5 | all five are by-product mentions (`furniture-interior-lexicon.md`, `ritual-garments.md`, `sumptuary-law-rank-display.md`, `kinship-terminology.md`, `sacred-kingship-mythic-charter.md`) | possible gap, thin in-corpus shelf; rank behind the two above |

The recommended candidate is the only one that combines (a) high demand, (b) zero owners of the *system*, and (c) a substantial shelf of works already registered in the corpus (§4.5). That combination is what the admission bar in `corpus/QUALITY.md:3-23` rewards.

---

## 4. The named gap — dream, vision and trance

### 4.1 Topic-ownership test, term by term (all 223 entries)

Command pattern:

```
grep -rilE -- '^- topic:.*\b<term>' corpus/knowledge/*/*.md
```

| term | topic-owner files | reading |
|---|---:|---|
| `dream` / `dreams` / `dreaming` / `dreamer` | **1** — `myth-symbol/divination-omen-systems.md` | one of fourteen divination technique rows, not the experience |
| `trance` | **0** | unowned |
| `ecsta*` (ecstasy / ecstatic) | **0** | unowned |
| `vision quest` / `visionary` | **0** | unowned |
| `incubation` | **1** — `divination-omen-systems.md` | the incubation *technique*, not the state or its institution |
| `shaman*` | **1** — `civilizations/mongol.md` | civilization base; topic line says "Heaven/earth and shamanic vocabulary" (`mongol.md:3`), i.e. lexical data |
| `possession(s)` / `possessed` | 47 raw, **3** strict phrases | raw hits are dominated by "inalienable possessions" (ownership sense), e.g. `culture-material/material-culture-inference-method.md:9`; strict phrases (`spirit possession`, `oracular possession`, `possessed by`, …) occur in `myth-symbol/divination-omen-systems.md`, `civilizations/burma.md`, `civilizations/ryukyu.md` — all adjacent, none owning the complex |

The two owners are adjacent, and both say so themselves:

- `myth-symbol/divination-omen-systems.md:1` — the H1 names "dreams" only as one of the reading technologies ("lots, bones, livers, birds, day-counts, dreams, and the institutions that license them").
- `divination-omen-systems.md:3` — the topic line places "dream-oracles and incubation" as **one row** in a fourteen-row technique typology.
- `divination-omen-systems.md:56` — "an *open* code (any dream, any utterance) needs a strong interpretive office to hold it together": divination owns what a dream *means when read*, not who dreams, how the state is induced, who is licensed to enter it, or how the culture polices it.
- `divination-omen-systems.md:64` — *divinatio naturalis* is "frenzy, dreams, oracular possession" **as a sign source** on the natural/artificial design axis.
- `divination-omen-systems.md:89` — technique row 12 is "Dream-oracle & incubation"; `:126` lists the dream-sanctuary as an institution that serves the reading.
- `divination-omen-systems.md:147-158` — §8 "Boundary — what this entry does not own" enumerates sky omens, direction codes, tale indexes, sacrifice typology, name magic, and civilization bases. It claims neither the altered state nor its specialist.
- `civilizations/mongol.md:3` — "Heaven/earth and shamanic vocabulary" is lexical/civilization reference, not a system entry.

### 4.2 Heading test

```
grep -rniE '^#{1,4} .*(dream|trance|ecsta|shaman|incubat|vision quest|altered state)' corpus/knowledge
```

Two hits, both adjacent:

- `myth-symbol/divination-omen-systems.md:1` — H1, dreams as a reading technology (above).
- `civilizations/australia-aboriginal.md:36` — "## Dreaming, Tjukurpa and ancestral law-language coupling". This is the Australian ancestral Dreaming (a cosmological law-time), **not** the dream/vision/trance state complex; the new entry must name this boundary explicitly so the two are not conflated.

No entry has a section heading that owns dream experience, trance induction, ecstatic practice, the visionary career, or possession as a system.

### 4.3 Demand evidence (the corpus uses the domain widely)

From the same 223-file pass:

| term set | distinct files |
|---|---:|
| `dream(s/ing/er/t)` | 25 |
| `shaman*` | 28 |
| `vision quest` / `visionary` / `visions` | 14 |
| `ecsta*` | 5 |
| `trance(s)` | 4 |
| `incubat*` | 2 |
| **union (any of the above)** | **52** |

The mentions are by-product, which is the point: the corpus refers to dream-culture, shamanic practice, and ecstatic experience inside divination, animal symbolism, ritual liminality, cosmology, and civilization bases, but no file owns the machinery. This is the same "everyone couples to it, nobody owns it" shape that `plant-symbolism.md:3` used to justify its own landing and that r42's R1 used for the lithic register (now landed as `mineral-stone-symbolism.md`).

### 4.4 Nearest neighbours and the boundary the entry must keep

| neighbour | what it owns (cite) | what the new entry owns instead |
|---|---|---|
| `myth-symbol/divination-omen-systems.md` | the reading technology: question → technique → closed sign space → licensed reader → prescription (`:3`, `:56`, `:64`, `:89`, `:126`, §8 `:147-158`) | the **state and its induction**: dream/vision/trance/possession as experience, the techniques that produce it, and the institutions that license the person who enters it |
| `myth-symbol/ritual-liminality.md` | rite-of-passage grammar, communitas, sacrifice typology, permanent liminal specialist *slot* (`:5-6`, `:39-40`, `:111`) | the **visionary career and its training**, not the liminal phase grammar; the shaman is one occupant of that file's slot and the new entry supplies the occupation's internal machinery |
| `myth-symbol/animal-symbolism.md` | spirit helpers and the shaman's assisting animals (`:8`, `:53`); Harner calibration (`:57`) | the human practice, not the fauna register; the new entry uses spirit-helpers as one component and does not restate the animal code |
| `culture-material/music-instrument-lexicon.md` | the drum as material culture and tone-language encoding (`:96-100`) | the drum as *induction technology* inside a ritual sequence, not the instrument's classification |
| `linguistics/politeness-taboo-euphemism.md`, `linguistics/register-strata-attestation.md` | the marked register and attestation law | the **possession/visionary register** as one output of the state, coupled not restated |
| `myth-symbol/death-afterlife-eschatology.md` | death doctrine and the unquiet dead as a status | the vision of the dead as one vision type, not the afterlife system |
| `verification/myth-consistency-gate.md:34`, `verification/real-world-inspiration-boundaries.md:2,97` | the restricted-knowledge rule and the screening procedure | the new entry must mark access boundaries and invent in-world designs rather than reconstruct living possession rites |

### 4.5 Source shelf already in the corpus (no fabricated bibliography required)

All locators below were re-read live at `c9f4eaa`; they are the same shelf r42's R2 identified (`reports/round-42/scout/K02-myth-gaps.md:216-260`), still unlanded:

- `myth-symbol/animal-symbolism.md:8` — Eliade (1951; trans. Trask 1964), *Shamanism: Archaic Techniques of Ecstasy*, Pantheon; Harner (1980), *The Way of the Shaman*, Harper & Row (calibration note at `:57`: core-cluster neo-shamanism, a modern book-transmitted practice — fine as fiction, wrong as ethnography).
- `myth-symbol/divination-omen-systems.md:12` — Artemidorus, *Oneirocritica* (2nd c. CE; trans. White 1975); Gardiner (1935), *Hieratic Papyri in the British Museum* 3rd series (Papyrus Chester Beatty III); Oppenheim (1956), "The Interpretation of Dreams in the Ancient Near East", *TAPS* 46(3).
- `myth-symbol/divination-omen-systems.md:186` — Dodds (1951), *The Greeks and the Irrational* ch. 4, with its mid-century evolutionism already labelled; the same calibration is carried at `myth-symbol/sacred-topography-pilgrimage.md:114`.
- `myth-symbol/ritual-liminality.md:5-6` — van Gennep (1909), *Les rites de passage*; Turner (1967), *The Forest of Symbols*; Turner (1969), *The Ritual Process*; Turner (1974), *Dramas, Fields, and Metaphors*; Turner & Turner (1978), *Image and Pilgrimage in Christian Culture*.
- `myth-symbol/ritual-liminality.md:40,111` — permanent liminality as an institution, with "shaman" named as a permanent specialist slot (this is the neighbour claim, not an ownership claim).
- `culture-material/music-instrument-lexicon.md:100` — the talking drum as the lane's tone-language coupling (induction-adjacent material).
- `myth-symbol/cosmology-cosmography.md:5` — Eliade (1949/1957), the sacred/profane and eternal-return frame.
- `verification/myth-consistency-gate.md:34` — "Do not expose restricted ritual knowledge to fill a table"; `verification/real-world-inspiration-boundaries.md:97` — restricted initiation knowledge must not be reproduced or reconstructed.

**Known shelf risk (must be recorded, not hidden):** the obvious modern specialist bibliography is **not** registered anywhere in the corpus — measured at `c9f4eaa`: `Bourguignon` 0 files, `Winkelman` 0, `Lambek` 0, `Csordas` 0, `Vitebsky` 0 (`Schieffelin` 1, incidental). A drafter cannot fetch these (no network at seat time); the entry must either build on the in-corpus shelf above or mark the modern items `(to-verify)` inline per `corpus/QUALITY.md:3-8`. This is the reason r42 ranked R2 below R1, and it remains the entry's main authoring risk; it does **not** affect the ownership verdict.

### 4.6 Why this is not a carried r43 premise

- r42's K02 proposed R2 at `reports/round-42/scout/K02-myth-gaps.md:216-260`; the r42 landing set was the other three (lithic, purity, sacred topography), recorded in `corpus/README.md:5-14` (revision 2.4: myth-symbol 23 → 26).
- At `c9f4eaa` the proposed filename does not exist: `ls corpus/knowledge/myth-symbol/dream-vision-trance.md` → "No such file or directory".
- The absence is re-measured here at the 223 total, not inferred from r42 or r43. The r43 lithic failure was the opposite case: the topic's file *was* present (`mineral-stone-symbolism.md`, r42 landing), which is exactly what a fresh sweep catches.

---

## 5. Landing preconditions verified against the live partition

1. **Proposed path is free.** `find corpus/knowledge -type f | grep -iE 'dream|trance|vision|ecsta|shaman|incubat'` → no output. No existing entry, in any partition, has one of these in its filename.
2. **Sort position.** `{ find corpus/knowledge/myth-symbol -name '*.md' -printf '%f\n'; echo dream-vision-trance.md; } | LC_ALL=C sort` places it at line 11:
   ```
   10  divination-omen-systems.md
   11  dream-vision-trance.md
   12  eschatology-world-end-systems.md
   ```
3. **Partition delta.** `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 26; landing one entry → 27. `find corpus/knowledge -name '*.md' | wc -l` → 223; → 224.
4. **README delta the integrator will owe (C02's job, stated here for the arithmetic).** `## myth-symbol/ (26)` at `corpus/README.md:205` → `(27)`; `Total knowledge entries: 223.` at `corpus/README.md:544` → `224`; footer vector `25/26/25/29/24/94` → `25/27/25/29/24/94`; new row text must be the entry's own `- topic:` text byte-equal and inserted in filename order between the `divination-omen-systems.md` and `eschatology-world-end-systems.md` rows.
5. **One-owner-per-topic precondition.** No topic line owns the complex (§4.1); the two adjacent owners each state the boundary they keep (§4.4). The entry must add a boundary table naming divination, ritual-liminality, animal-symbolism, music-instrument, death-afterlife, and the Australian Dreaming, so the "no duplication" review check (`divination-omen-systems.md:173`, DR-DIV-03) stays green.
6. **No overwrite.** The landing creates one new file and edits no existing entry; the only other file changed is `corpus/README.md` (one section header, one totals line, one footer vector, one new row, one revision block). The integrator applies it; no seat stages under `corpus/`.

Entry-contract fields the drafter must carry, as measured on the most recent myth-symbol landing (`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`): `- gap filled:` at `:3`, `- topic:` at `:5`, `- sources:` at `:7`, `- couples:` at `:11`, `- source:` at `:13`, `- verified-at:` at `:15`, `- recheck:` at `:17`, `- scope:` at `:19`. The README row is byte-equal to the `- topic:` line (rev-2.0/2.1/2.3 convention, `corpus/README.md:33-42`).

---

## 6. Corroboration of K02 (or divergence)

At write time (`2026-10-19T17:22:20Z`) `ls -la reports/round-44/scout/` returned an empty directory — **K02's fragment had not landed**, so this seat cannot literally confirm K02's named gap. This file is the independent measurement K02's gap will be compared against.

Procedure for the integrator once K02 lands (substitute K02's candidate terms/slug):

```
# 1. total must still be 223 (no landing happened in parallel)
find corpus/knowledge -name '*.md' | wc -l

# 2. topic-owner test: 0 relevant owners required
grep -rilE -- '^- topic:.*\b(<term1>|<term2>|...)' corpus/knowledge/*/*.md

# 3. heading test: no section owns the candidate
grep -rniE '^#{1,4} .*(<term1>|<term2>)' corpus/knowledge

# 4. slug/collision test: empty required
find corpus/knowledge -type f -iname '*<slug-fragment>*'

# 5. sort position against the live partition
{ find corpus/knowledge/<partition> -name '*.md' -printf '%f\n'; echo <proposed-slug>.md; } | LC_ALL=C sort | grep -n -B1 -A1 '<proposed-slug>.md'
```

- If K02 named **the same** gap: this file is the corroboration; §4.1–4.6 supply the ownership and shelf evidence.
- If K02 named **a different** gap: both are candidates; the integrator should prefer the one whose topic-owners are zero *after explaining every hit* and whose source shelf is in-corpus. Claim C is +1 only — do not land both. This file's §3 table already records the alternates' weaknesses.
- If K02's gap proves **owned** on this sweep (the r43 failure mode): this file's candidate stands as the fallback, with the §4 evidence.

---

## 7. Alternates, ranked (if the integrator rejects the recommendation)

1. **Gesture / sign / whistle / drum speech** — demand 45/223, **0 topic-owners**, filename free. The corpus already carries the channel inside other entries: `linguistics/phonetics-phonology.md:75,197,310` (whistled registers), `linguistics/orality-formulaic-language.md:114,124` (talking drums; Carrington 1949 registered at `:24`), `linguistics/sound-symbolism.md:19,121`, `culture-material/music-instrument-lexicon.md:100`. **Weakness:** the specialist shelf is not in-corpus — measured `Kendon` 0, `McNeill` 0, `Stokoe` 0, `Klima` 0, `Bellugi` 0, `Umiker-Sebeok` 0 (`Sebeok` 3, incidental). An entry would depend on the Carrington/whistled-speech anchors and heavy `(to-verify)` marking. Rank 2.
2. **Metallurgy process** (ore → smelt → alloy → cast) — demand 42/223, no real topic owner (the single hit is "casting lots" in divination). **Weakness:** `culture-material/craft-artisan-lexicon.md:3` already owns tool names, material-grading vocabularies (tamahagane, karat, fineness) and workshop organization; `myth-symbol/mineral-stone-symbolism.md` owns the symbolic register; the process entry would need a sharp boundary and would still overlap the material-culture category. Shelf partly in-corpus (`pantheon-archetypes.md:20` Eliade *The Forge and the Crucible*, McNaughton; `material-culture-inference-method.md:7,52,66` Leroi-Gourhan, Lemonnier, Lechtman, Pfaffenberger). Rank 3.
3. **Monster / terato** — demand only 13/223, 0 strict topic-owners. `Watkins (1995) How to Kill a Dragon` is registered four times (`hero-journey-variants.md:11`, `pantheon-archetypes.md:8`, `binding-speech-complex.md:12`, `naming-systems.md:18`), but the domain is thin and already covered as rows inside `hero-journey-variants.md:11-13` and `creation-myths-taxonomy.md`. Rank 4.
4. **Games / sport** — demand 40/223, no real owner, but the shelf is absent (`Huizinga` 0, `Caillois` 0, `Parlett` 0; `Murray` 4 files, ambiguous author match). Do not propose without a source route. Rank 5.

---

## 8. Limits / to-verify

- **K02 unavailable.** This seat could not read K02's named gap (empty `scout/` at write time); §6 defines the comparison procedure. No claim is made about K02's content.
- **Demand is a heuristic.** A regex count measures mentions, not scholarly treatment. It is used only to establish that the corpus *uses* the domain; the ownership verdict rests on the topic-line/heading tests, which are exhaustive over the 223 files.
- **Shelf risk is real.** The modern specialist literature for dream/trance (Bourguignon, Winkelman, Lambek, Csordas, Vitebsky) is unregistered. The entry must be built from the in-corpus shelf in §4.5 and mark anything unretrieved `(to-verify)`; an authoring seat must not invent bibliographic detail.
- **Australian Dreaming boundary.** `civilizations/australia-aboriginal.md:36` uses "Dreaming" in the ancestral-law sense. The new entry must explicitly distinguish the two or the review will read it as a collision.
- **No landing authority.** This seat proposes a path and verifies its absence; it does not draft the entry, stage corpus bytes, or edit README. C01/C03/C04/C05 and the integrator own those steps.
- **No external verification.** No network was used; every citation above is an in-repo locator re-read at `c9f4eaa`. Anything not in the repo stays `to-verify`.

---

## 9. Command log (this seat, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

| command | output |
|---|---|
| `git rev-parse HEAD` | `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` |
| `git status --porcelain` | `?? reports/round-44/` only |
| `find corpus/knowledge -name '*.md' \| wc -l` | `223` |
| per-partition `find` | `civilizations=94 culture-material=25 linguistics=25 myth-symbol=26 synthesis=29 verification=24` |
| `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, `totals_ok True`, `footer_ok True`, exit 0, `readme_sha256 7c788a1d…ef31cdcd` |
| `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 223` |
| `ls corpus/knowledge/myth-symbol/dream-vision-trance.md` | `No such file or directory` |
| `find corpus/knowledge -type f \| grep -iE 'dream\|trance\|vision\|ecsta\|shaman\|incubat'` | no output |
| `grep -rilE -- '^- topic:.*\bdream' corpus/knowledge/*/*.md` | `corpus/knowledge/myth-symbol/divination-omen-systems.md` (1) |
| `grep -rilE -- '^- topic:.*\btrance\b' corpus/knowledge/*/*.md` | no output (0) |
| `grep -rilE -- '^- topic:.*\becsta' corpus/knowledge/*/*.md` | no output (0) |
| `grep -rilE -- '^- topic:.*\bvision quest\|\bvisionary' corpus/knowledge/*/*.md` | no output (0) |
| `grep -rilE -- '^- topic:.*\bshaman' corpus/knowledge/*/*.md` | `corpus/knowledge/civilizations/mongol.md` (1) |
| heading sweep `grep -rniE '^#{1,4} .*(dream\|trance\|ecsta\|shaman\|incubat\|vision quest\|altered state)' corpus/knowledge` | 2 hits: `divination-omen-systems.md:1`, `australia-aboriginal.md:36` |
| Python demand sweep over 223 files (regexes in §3) | dream/vision/trance `52`; gesture/sign/whistle `45`; metallurgy `42`; games `40`; sacrifice `92`; marriage `78`; monster `13` |
| `{ find corpus/knowledge/myth-symbol -name '*.md' -printf '%f\n'; echo dream-vision-trance.md; } \| LC_ALL=C sort \| grep -n -B1 -A1 dream-vision-trance.md` | `10 divination-omen-systems.md` / `11 dream-vision-trance.md` / `12 eschatology-world-end-systems.md` |
| `ls corpus/knowledge/myth-symbol/*.md \| wc -l` | `26` |
| `ls -la reports/round-44/scout/` | empty at write time |

**Non-actions:** no corpus staging, no `reports/round-*/run-validation.py` execution, no filed-byte edit, no git commit/push, no network, no `.scratch` artifact left behind.
