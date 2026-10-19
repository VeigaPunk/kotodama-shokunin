# C01 — entry draft, claim C: `myth-symbol/dream-vision-trance.md`

- Seat: **C01**, role executor, claim **C** (`reports/round-44/targets.json:29`).
- Round 44, loop 1; baseline `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (`reports/round-44/claims.json:7`).
- Out path: `reports/round-44/cov/C01-entry-draft.md` (this file only).
- Writes: this file only. **No `corpus/**` byte is staged or edited.** The entry below is a fenced DRAFT for integrator application.
- Canon: **NON-CANON** engineering evidence. This seat drafts; it admits nothing, certifies no round, and decides nothing about any world.
- Scout reconciliation: K02's `scout/K02-gap-scout.md` was **not on disk** at this seat's write time. The claim-C gap this draft serves is the one named by the independent claim-C scout **K04** (`reports/round-44/scout/K04-gap-verify.md:10`, §4, §5), whose sweep and landing preconditions are re-measured independently below. If K02 lands a different gap, this draft is a **spare**, not the claim's landing; the integrator must choose one gap, not land both (`K04-gap-verify.md:211`).

## 1. Fresh absence sweep at HEAD `c9f4eaa`

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
c9f4eaa707b6e977ff6e1616463e91f4b8afea5d

$ find corpus/knowledge -name '*.md' | wc -l
223

$ for d in corpus/knowledge/*/; do printf '%s=%s ' "$(basename $d)" "$(find $d -name '*.md' | wc -l)"; done
civilizations=94 culture-material=25 linguistics=25 myth-symbol=26 synthesis=29 verification=24
```

### 1.1 Topic-ownership test (the single `- topic:` line of every entry)

| term | command | topic-owner files | disposition |
|---|---|---|---|
| `dream` | `grep -rilE -- '^- topic:.*\bdream' corpus/knowledge/*/*.md` | **1** | `myth-symbol/divination-omen-systems.md` — technique row 12, "dream-oracle & incubation" (`:89`), not the state |
| `trance` | `grep -rilE -- '^- topic:.*\btrance' ...` | **0** | unowned |
| `ecsta*` | `grep -rilE -- '^- topic:.*\becsta' ...` | **0** | unowned |
| `vision quest` / `visionary` | `grep -rilE -- '^- topic:.*(\bvision quest\b\|\bvisionary\b)' ...` | **0** | unowned after the grouping fix; an ungrouped alternation produced two false positives in a `- sources:` line and is not counted |
| `shaman*` | `grep -rilE -- '^- topic:.*\bshaman' ...` | **1** | `civilizations/mongol.md:3` — "shamanic vocabulary", a civilization base, not a system |
| `incubat*` | `grep -rilE -- '^- topic:.*\bincubat' ...` | **1** | `divination-omen-systems.md` — the incubation *technique*, not the state or its institution |

### 1.2 Heading test — no entry owns the complex in a section

```
$ grep -rniE -- '^#{1,4} .*(dream|trance|ecsta|shaman|incubat|vision quest|altered state)' corpus/knowledge/*/*.md
corpus/knowledge/myth-symbol/divination-omen-systems.md:1:# Divination & omen-reading systems — ... dreams ...
corpus/knowledge/civilizations/australia-aboriginal.md:36:## Dreaming, Tjukurpa and ancestral law-language coupling
```

Both hits are adjacent, not owners: `divination-omen-systems.md:1` names dreams as one sign source; `australia-aboriginal.md:36-40` is the ancestral Dreaming/Tjukurpa (law-time), **not** ordinary sleep dreams — the draft names this boundary explicitly in §1 and §9.

### 1.3 Demand is by-product

| pattern | distinct files |
|---|---:|
| `\bdream(s\|ing\|er\|t)?\b` | 25 |
| `\bshaman[a-z]*\b` | 28 |
| `\bvision quest\b\|\bvisionary\b\|\bvisions?\b` | 14 |
| `\becsta[a-z]*\b` | 5 |
| `\btrance(s)?\b` | 4 |
| `\bincubat[a-z]*\b` | 2 |
| **union** (`grep -rilE` over the six patterns) | **61** |

K04's independent Python pass measured **52** for a slightly narrower union (`K04-gap-verify.md:63`); the difference is regex scope, not ownership. Either number shows the corpus *uses* the domain; the ownership verdict rests on §1.1–1.2, which are exhaustive over the 223 files.

### 1.4 Filename and sort checks

```
$ find corpus/knowledge -type f | grep -iE 'dream|trance|vision|ecsta|shaman|incubat'
(no output)

$ { find corpus/knowledge/myth-symbol -name '*.md' -printf '%f\n'; echo dream-vision-trance.md; } | LC_ALL=C sort | grep -n -B1 -A1 'dream-vision-trance.md'
10-divination-omen-systems.md
11:dream-vision-trance.md
12-eschatology-world-end-systems.md
```

The proposed slug is unused in every partition and sorts at position 11 of `myth-symbol/`.

### 1.5 Boundary against the nearest owners (measured, not asserted)

| neighbour | what it owns (cited) | what this entry owns instead |
|---|---|---|
| `myth-symbol/divination-omen-systems.md` | the reading technology: question → technique → closed sign space → licensed reader → prescription (`:52-56`); the natural/artificial etic axis (`:64`); technique row 12 (`:89`); the dream-sanctuary institution (`:126`); its own §8 boundary (`:147-158`) | the **state and its induction**, the **visionary career**, and the **institutions that license the entrant** — not what a dream means once read |
| `myth-symbol/ritual-liminality.md` | the rite-of-passage grammar, liminality/communitas (`:39-40`), and the permanent-liminal specialist *slot* that names "shaman" (`:111`) | the occupation's internal machinery — call, training, ordeal, licensure, practice, failure — not the phase grammar that stages it |
| `myth-symbol/animal-symbolism.md` | spirit helpers and assisting animals (`:53`), Harner's calibration (`:57`) | the human practice; spirit helpers are one component here, never a re-table of the fauna register |
| `culture-material/music-instrument-lexicon.md` | the drum as material culture and as tone-language encoding (`:96-100`) | the drum as **induction technology** inside a ritual sequence, not the instrument's classification |
| `myth-symbol/death-afterlife-eschatology.md` | death doctrine, survival types, the unquiet dead (`:3`) | a vision of the dead as **one vision type**, not the afterlife system |
| `linguistics/sacred-registers-liturgical-language.md` | the sacred register system, its competences and event rules (`:3`, `:26-40`, `:101`) | the **visionary/possession register** as one output of the state; the register's own machinery is cited, not restated |
| `linguistics/register-strata-attestation.md` | the attestation register and the register law — who may speak, with what force, with what record consequence (`:3`, `:40`) | the state-side licensing that precedes the register law; the law itself is cited, not restated |
| `civilizations/australia-aboriginal.md` | the ancestral Dreaming/Tjukurpa as law-time (`:36-40`) | ordinary sleep dreams and their institutions; §1 and §9 state the distinction explicitly |

## 2. Landing check

- **Target path:** `corpus/knowledge/myth-symbol/dream-vision-trance.md`.
- **Partition delta:** `myth-symbol/` 26 → **27**; corpus total 223 → **224**.
- **Overwrite:** none. The file does not exist at `c9f4eaa` (§1.4); no existing entry is edited. The only other file the integrator changes is `corpus/README.md` (C02's job).
- **One owner per topic:** the only topic-line hits are an adjacent technique row and a civilization base (§1.1), both explained; no second owner.
- **Sort position:** between `divination-omen-systems.md` and `eschatology-world-end-systems.md` (§1.4).

## 3. README handoff (C02 applies; this seat does not edit README)

C02's rev-2.5 edit must, for this entry:

1. Add a row in `## myth-symbol/ (26)` → `(27)` at `corpus/README.md:205`, in filename order between the `divination-omen-systems.md` and `eschatology-world-end-systems.md` rows. The row text must be the entry's own `- topic:` text **byte-equal**, continuations space-joined (the sweep's `topic_of` rule, `reports/round-28/readme/sweep.py`; `corpus/README.md:95-101`).
2. Move `Total knowledge entries: 223.` at `corpus/README.md:544` → **224**.
3. Move the counts footer at `corpus/README.md:546-549` from `(total 223 files; directory totals 25/26/25/29/24/94)` to `(total 224 files; directory totals 25/27/25/29/24/94)`.
4. Note the pre-existing rev-2.4 prose-vector defect only if C02 touches that prose; this seat does not repair filed bytes (`reports/round-44/targets.json:6`).

The exact `- topic:` text to copy is inside the fence below (the `- topic:` line is a single line; do not wrap it in the README row).

## 4. Draft entry — integrator applies exactly this fenced block

````markdown
# Dream, vision and trance — the altered-state complex: induction, the visionary career, the dream economy, and the institutions that license entrance

- gap filled: the partition owns the **reading technology** of dreams — a dream-oracle row inside a fourteen-row divination typology (`corpus/knowledge/myth-symbol/divination-omen-systems.md:1,:3,:89,:126,:147-158`) — and it owns the **rite grammar** that stages a permanent liminal specialist (`corpus/knowledge/myth-symbol/ritual-liminality.md:39-40,:111`), but no entry owns the altered state itself: how a culture recognizes it, induces it, licenses the person who enters it, interprets it, and converts it into social action. Measured absence sweep 2026-10-19 at lane HEAD `c9f4eaa` from the lane root over `corpus/knowledge/*/*.md` (total **223**; myth-symbol **26**). Topic-owner test (`grep -rilE -- '^- topic:.*<term>'`): `\bdream` → **1** (`divination-omen-systems.md`, technique row 12), `\btrance` → **0**, `\becsta` → **0**, `(\bvision quest\b|\bvisionary\b)` → **0**, `\bshaman` → **1** (`civilizations/mongol.md:3`, "shamanic vocabulary" in a civilization base), `\bincubat` → **1** (`divination-omen-systems.md`, the incubation technique). Heading test (`grep -rniE '^#{1,4} .*(dream|trance|ecsta|shaman|incubat|vision quest|altered state)'`) → **2**, both adjacent: `divination-omen-systems.md:1` (dreams as a sign source) and `civilizations/australia-aboriginal.md:36` (the ancestral Dreaming/Tjukurpa, explicitly not sleep dreams). Filename test (`find corpus/knowledge -type f | grep -iE 'dream|trance|vision|ecsta|shaman|incubat'`) → **0**. Demand is by-product: this seat's union regex over the 223 files → **61 distinct files** (`dream*` 25, `shaman*` 28, `vision quest/visionary/visions` 14, `ecsta*` 5, `trance*` 4, `incubat*` 2); K04's independent pass → **52** (`reports/round-44/scout/K04-gap-verify.md:63`); the difference is regex scope, not ownership. The gap is re-measured at `c9f4eaa`, not carried: r42's scout ranked this complex (`reports/round-42/scout/K02-myth-gaps.md:216-260`) but it was not landed, and the file is absent at HEAD.

- topic: the dream/vision/trance complex of a fictional culture as a designed system — the state typology (ordinary dream, significant or "big" dream, waking vision, trance, possession, ecstatic flight, incubation dream, deathbed vision, lucid dream) treated as **etic coordinates rather than a ladder**; the induction technologies (sleep and incubation, sleep deprivation, fasting, sensory deprivation, rhythmic drumming and dance, ordeal and pain, plant helpers, isolation, hyperventilation, meditation, temperature) with the mechanism claim separated from the cultural meaning; the visionary career (call, training, ordeal, licensure, practice, failure, retirement) as distinct from the rite-of-passage grammar that stages it; the institutions that license and police entrance (dream-sanctuary, dream-reader, shaman, prophet, possession cult, dream-sharing council, state dream office, dream-book archive, secret society); the **dream economy** — who may dream, who may tell, who may interpret, who may act, and who profits; the visionary register as one output of the state; the evidence and ethics rules for using living traditions without extraction; a build protocol; a NON-CANON worked example; and a calibration shelf. Reference method only; canon decisions belong to lore-shokunin.

- sources:
  - In-corpus anchors (resolve on disk at baseline `c9f4eaa`; every cited line re-read in this seat, transcript in the `## 5. Self-audit` section of `reports/round-44/cov/C01-entry-draft.md`): `corpus/knowledge/myth-symbol/divination-omen-systems.md:3` (the topic: dreams as one row in a fourteen-row technique typology), `:52-56` (the five slots; an *open* dream code needs an interpretive office), `:64` (Cicero's natural/artificial etic axis, with the label requirement), `:89` (technique row 12, dream-oracle and incubation), `:126` (the dream-sanctuary institution), `:147-158` (§8 boundary: what that entry does not own), `:12` (Artemidorus, Gardiner, Oppenheim — the dream-book shelf), `:186` (Dodds' dream evolutionism, labelled); `corpus/knowledge/myth-symbol/ritual-liminality.md:5-6` (van Gennep and Turner shelf), `:39-40` (liminality and communitas), `:111` (the permanent-liminal specialist slot that names "shaman"), `:112` (ritual language as performative); `corpus/knowledge/myth-symbol/animal-symbolism.md:8` (Eliade 1951 and Harner 1980 registration), `:53` (spirit helpers and their holders), `:57` (Harner calibration: core-cluster neo-shamanism, fine as fiction, wrong as ethnography); `corpus/knowledge/culture-material/music-instrument-lexicon.md:96` (the shaman's drum as steed and cosmos), `:98` (instruments that speak), `:100` (the talking drum as the lane's tone-language coupling); `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md:3` (the death-doctrine topic; the vision of the dead is one vision type, not that system); `corpus/knowledge/civilizations/australia-aboriginal.md:36-40` (Dreaming/Tjukurpa as ancestral law-time, explicitly not ordinary sleep dreams); `corpus/knowledge/myth-symbol/cosmology-cosmography.md:5` (Eliade's sacred/profane and eternal-return vocabulary, with its calibration); `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md:3` (the sacred-register topic), `:26-40` (§1 boundary table), `:101` (recitation norms and chant); `corpus/knowledge/linguistics/register-strata-attestation.md:3` (attestation register and register law), `:40` (the register/law object table); `corpus/knowledge/linguistics/linguistic-anthropology.md:9` (the SPEAKING grid's speech-event unit), `:13` (the eight components); `corpus/knowledge/linguistics/semantics-pragmatics.md:88-94` (speech acts and the commissive class); `corpus/knowledge/verification/myth-consistency-gate.md:34` ("Do not expose restricted ritual knowledge to fill a table"); `corpus/knowledge/verification/real-world-inspiration-boundaries.md:91-97` (the sacred-material red lines, including restricted initiation knowledge); `corpus/QUALITY.md:3-23` (the admission bar).
  - External shelf registered in-corpus (each item is carried by the entry named; **not re-fetched in this seat** — no network at this run — so every item below is `(to-verify)` for direct reading, edition and page): Eliade (1951; trans. Trask 1964), *Shamanism: Archaic Techniques of Ecstasy*, Pantheon — registered at `animal-symbolism.md:8` and `cosmology-cosmography.md:5`; Harner (1980), *The Way of the Shaman*, Harper & Row — registered at `animal-symbolism.md:8`, with the calibration at `:57`; Artemidorus, *Oneirocritica* (2nd c. CE; trans. White 1975) — registered at `divination-omen-systems.md:12`; Gardiner (1935), *Hieratic Papyri in the British Museum*, 3rd series (Papyrus Chester Beatty III) — registered at `divination-omen-systems.md:12`; Oppenheim (1956), "The Interpretation of Dreams in the Ancient Near East," *Transactions of the American Philosophical Society* 46(3) — registered at `divination-omen-systems.md:12`; Dodds (1951), *The Greeks and the Irrational*, ch. 4 — registered at `divination-omen-systems.md:186`, with its evolutionism labelled; van Gennep (1909), *Les rites de passage*; Turner (1967), *The Forest of Symbols*; Turner (1969), *The Ritual Process*; Turner (1974), *Dramas, Fields, and Metaphors*; Turner & Turner (1978), *Image and Pilgrimage in Christian Culture* — registered at `ritual-liminality.md:5-6`.
  - External shelf **not registered in-corpus** (measured at `c9f4eaa`: `Bourguignon` **0** files, `Winkelman` **0**, `Lambek` **0**, `Csordas` **0**, `Vitebsky` **0**, `Kehoe` **0**, `Hamayon` **0**): Bourguignon (1973), *Religion, Altered States of Consciousness, and Social Change*; Winkelman (2000), *Shamanism: The Neural Ecology of Consciousness and Healing*; Lambek (1993), *Knowledge and Practice in Mayotte*; Csordas (1994), *The Sacred Self*; Vitebsky (1995), *The Shaman*; Kehoe (2000), *Shamans and Religion*; Hamayon's work on Siberian shamanism. **Every one is `(to-verify)`** — no edition, page or claim from these is asserted in this entry; they are named as the reader's route to the specialist literature, not as inspected support. The entry is built from the in-corpus shelf above.
  - In-repo authority: `corpus/QUALITY.md:3-23`; `corpus/knowledge/synthesis/coupling-model.md:3` (the master method into which this system fits); `corpus/knowledge/synthesis/worldbible-integration-contract.md:2` (the handoff contract); `corpus/knowledge/verification/real-world-inspiration-boundaries.md:91-97` and `corpus/knowledge/verification/myth-consistency-gate.md:34` (the access boundaries this entry obeys).

- calibration: **mainstream** — sleep and dreaming are panhuman; cultures pattern what counts as a significant dream and what is done with it; dream incubation is documented in several independent traditions (Egyptian dream book, Assyrian incubation, Greek Asclepieia; `divination-omen-systems.md:12,:89`); Eliade's *documentary* range across Siberian and American shamanic techniques is usable even where his universal theory is not; Turner's liminality is a productive heuristic, not a law. **Contested** — Eliade's "archaic techniques of ecstasy" as a universal core; the shaman/priest/medium typology; "altered state" as one thing rather than a family; the neurophysiological mapping of trance; the therapeutic efficacy of trance; the possession/shamanism binary; the cross-cultural stability of "vision quest." **Discredited or refused** — Lévy-Bruhl's "primitive mentality" and any prelogical/pre-rational framing; shamanism as mental illness; dream prophecy as a natural law; the pharmacological reduction ("the plant explains the religion"); the Jungian universal-archetype reading; and the conflation of the Australian ancestral Dreaming/Tjukurpa with ordinary sleep dreams (`australia-aboriginal.md:36-40`). The corpus's own calibrations are carried, not re-derived: Harner's core-shamanism is a modern, book-transmitted practice — "fine as a fictional religion; wrong as ethnographic description" (`animal-symbolism.md:57`); Dodds' developmental sequence (objective → symbolic dreams) is mid-century evolutionism — "use the material, label the frame" (`divination-omen-systems.md:186`; repeated at `sacred-topography-pilgrimage.md:114`). The six-component model, the dream-economy table and the career sequence are **lane-authored craft organization**, not a published standard.

- couples: `corpus/knowledge/myth-symbol/divination-omen-systems.md` (owns the reading technology — question, technique, sign space, licensed reader, prescription — `:52-56`, and the dream-oracle/incubation row `:89`, the sanctuary institution `:126`; this entry owns the state, its induction, the entrant's career and the licensing institution, and hands the *reading* of a dream to that file rather than re-tabling it); `corpus/knowledge/myth-symbol/ritual-liminality.md` (owns the rite-of-passage grammar and the permanent-liminal specialist slot `:39-40,:111`; this entry fills the occupation's internal sequence — call, training, ordeal, licensure, practice, failure — and does not restate the phase grammar); `corpus/knowledge/myth-symbol/animal-symbolism.md` (owns spirit helpers and assisting animals `:53`, and the Harner calibration `:57`; a helper is one component of a visionary career here, never a re-table of the fauna register); `corpus/knowledge/culture-material/music-instrument-lexicon.md` (owns the drum as material culture and tone-language encoding `:96-100`; this entry owns the drum as an induction technology inside a sequence — tempo, duration, participation — not the instrument's classification); `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md` (owns death doctrine, survival types and the unquiet dead `:3`; a vision of the dead is one vision type here, not an afterlife system); `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md` (owns the sacred register, its competences and event-typed rules `:3,:26-40,:101`; the visionary register is one output of the state, and its liturgical cousin is cited, not restated); `corpus/knowledge/linguistics/register-strata-attestation.md` (owns the attestation register and the register law `:3,:40`; this entry owns the state-side licence that precedes the law, and the law itself stays there); `corpus/knowledge/myth-symbol/binding-speech-complex.md` (owns efficacious speech — oath, curse, blessing and name-power as one machinery `:39,:85`; a spirit's command is a register output here, and its binding force stays there); `corpus/knowledge/linguistics/linguistic-anthropology.md` (owns the SPEAKING grid and the speech-event inventory `:9,:13`; this entry fills the internal architecture of one event type — the vision event — rather than re-listing the grid); `corpus/knowledge/linguistics/semantics-pragmatics.md` (owns speech acts and implicature `:88-94`; possession speech and spirit narration are analysed here as register outputs, with the speech-act machinery cited); `corpus/knowledge/civilizations/australia-aboriginal.md` (owns the ancestral Dreaming/Tjukurpa `:36-40`; this entry explicitly excludes it from the sleep-dream complex); `corpus/knowledge/synthesis/coupling-model.md` (the master method; this entry is one system inside it); `corpus/knowledge/synthesis/worldbible-integration-contract.md` (the handoff contract); `corpus/knowledge/verification/real-world-inspiration-boundaries.md` and `corpus/knowledge/verification/myth-consistency-gate.md` (the access boundaries).

- source: the measured authority for the gap statement is the absence sweep recorded in `- gap filled:` (commands and counts, run 2026-10-19 at HEAD `c9f4eaa`); the method authority is the in-corpus sibling set named in `- couples:` — the entry recombines the corpus's own registered instruments (the divination frame, the liminality grammar, the spirit-helper shelf, the drum/register coupling) and adds nothing sourced anew. **No external source was fetched or resolved this run** (no network at this seat), so every bibliographic detail the author could not check against a held copy or a lane citation carries an inline `(to-verify)`; the unregistered specialist shelf is named as a route, not as support. The six-component model, the state typology, the career sequence, the dream-economy rights table and the worked fixture are lane-authored organization built on those citations.

- verified-at: 2026-10-19 — written this round at lane HEAD `c9f4eaa` (`git rev-parse HEAD` → `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`, equal to the declared baseline at `reports/round-44/claims.json:7`). Measured at write time with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: corpus total **223**; `myth-symbol/` **26**; the absence sweep and the topic/heading/filename/sort checks are recorded in `- gap filled:` and §1 above, each with its command and count. Every in-repo `path:line` anchor cited in this entry was re-read live in this pass and each cited line number re-checked against the file (transcript in the `## 5. Self-audit` section of `reports/round-44/cov/C01-entry-draft.md`). **Not done this round:** no external source was fetched or resolved (no network), so all literature legs are `(to-verify)`; no real tradition's rite, restricted detail or community practice was reconstructed; and the §12 fixture is disposable and decides nothing about any world.

- recheck: before any dream/vision/trance assignment becomes load-bearing in a world bible — re-run §3's state-recognition table against the scene in question and check that the state is socially recognized rather than merely experienced; re-read `corpus/knowledge/myth-symbol/divination-omen-systems.md:52-56,:89,:126,:147-158` before letting a dream-reading office double as the induction institution (the two are separable and often are separate); re-read `corpus/knowledge/myth-symbol/ritual-liminality.md:39-40,:111` before treating a visionary career as a rite of passage (the career outlasts the rite); re-open `corpus/knowledge/myth-symbol/animal-symbolism.md:57` before using Harner's "power animal" as ethnography; re-open `corpus/knowledge/myth-symbol/divination-omen-systems.md:186` before quoting Dodds' developmental sequence; re-read `corpus/knowledge/verification/real-world-inspiration-boundaries.md:91-97` and `corpus/knowledge/verification/myth-consistency-gate.md:34` before adapting any living tradition's restricted material; and re-open `corpus/knowledge/civilizations/australia-aboriginal.md:36-40` before using the word "Dreaming" for a sleep state. Corrections to this entry are new sections or a new entry, never rewrites.

- scope: reference method and lane policy for the myth-symbol partition. This entry decides nothing about any world — no state is real by virtue of this file, no rite is authorized, no specialist is licensed, no tradition is reconstructed — and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff (§13). Restricted real-world material is screened by `corpus/knowledge/verification/real-world-inspiration-boundaries.md`, not here.

## 1. What this entry owns, and the boundary it keeps

The altered-state complex is the **state-side** machinery that every dream-oracle, every shaman story, and every possession scene presupposes and none of the neighbouring entries owns. The boundary is stated once, then used throughout:

| Surface | Owner (read, not restated) | What this entry adds |
|---|---|---|
| Reading a dream as a sign | `divination-omen-systems.md` §2–§3 (`:52-56`, `:89`) | who dreams, how the state is induced, who is licensed to enter it, and what the community does before and after reading |
| Rite-of-passage grammar; liminal specialist slot | `ritual-liminality.md` §2, §6 (`:39-40`, `:111`) | the occupation's internal career: call, training, ordeal, licensure, practice, failure, retirement |
| Spirit helpers and assisting animals | `animal-symbolism.md` §4 (`:53`, `:57`) | the human practice that recruits a helper; the fauna code stays there |
| Drum as material culture; tone-language encoding | `music-instrument-lexicon.md` §7 (`:96-100`) | the drum as induction technology inside a sequence — tempo, duration, participation |
| Death doctrine and the unquiet dead | `death-afterlife-eschatology.md` (`:3`) | a vision of the dead as one vision type, not the afterlife system |
| Binding speech — oath, curse, blessing, name-power | `binding-speech-complex.md` §1, §3 (`:39`, `:85`) | the state that produces the utterance and the institution that licenses the speaker; a spirit's command is analysed here as a register output, its binding force stays there |
| Sacred register and liturgical language | `sacred-registers-liturgical-language.md` (`:3`, `:26-40`, `:101`) | the visionary/possession register as one output of the state |
| Attestation register and register law | `register-strata-attestation.md` (`:3`, `:40`) | the state-side licence that precedes the register law |
| Speech events and the SPEAKING grid | `linguistic-anthropology.md` §1 (`:9`, `:13`) | the internal architecture of one event type — the vision event |
| The ancestral Dreaming/Tjukurpa | `civilizations/australia-aboriginal.md` (`:36-40`) | ordinary sleep dreams; the two are explicitly separated in §9 |

**The one-sentence boundary:** the neighbours own what a sign *means* and what a rite *does*; this entry owns how a person *gets into the state*, who is allowed to, who pays for it, and what the community does with the person afterwards.

**The master claim, stated once: an altered state is a social institution before it is a private experience.** A culture's dream/vision/trance complex is the arrangement of who enters, how, with what warrant, who interprets, and what the community does with the result. A state without an institution is a symptom; an institution without a state is a theater. The design object is therefore not "the shaman" and not "the dream" but the **six-slot arrangement** in §2.

## 2. The six designable components

| # | component | design question | what it fixes | failure if absent | in-corpus handle |
|---|---|---|---|---|---|
| C1 | **STATE** | which state is recognized, and by what public cues? | the vocabulary and the recognition test | every unusual experience becomes a plot device | `divination-omen-systems.md:52-56` (sign-space discipline); `ritual-liminality.md:39-40` (liminal cues) |
| C2 | **INDUCTION** | how is it entered, at what cost, and who controls the technique? | the technology, the duration, the risk | the state is asserted rather than produced | `music-instrument-lexicon.md:96-100` (drum); `divination-omen-systems.md:89` (incubation) |
| C3 | **ENTRANT** | who may enter, with what warrant, and who is excluded? | the licence, the selection, the disqualification | a universal priesthood of anyone | `ritual-liminality.md:111` (the specialist slot); `register-strata-attestation.md:3` (licensed speech) |
| C4 | **INTERPRETER** | who reads the state, with what code, and who may disagree? | the interpretive office and its archive | the dream means whatever the plot needs | `divination-omen-systems.md:52-56` (reader slot); `:126` (sanctuary) |
| C5 | **UPTAKE** | what does the community do — decide, heal, crown, exile, or nothing? | the output and its consequences | the vision is private decoration | `divination-omen-systems.md:56` (prescription, not prediction) |
| C6 | **INSTITUTION** | which office, sanctuary, guild or court licenses and polices the whole arrangement? | the durable structure and its economy | a charisma with no succession | `divination-omen-systems.md:126`; `ritual-liminality.md:111` |

- **The six-of-six rule.** A rhetoric of the state missing any one slot is a style, not an institution. A "shaman" with no induction is a costume; a dream with no interpreter is a mood; an interpreter with no uptake is a critic; an institution with no state is a church.
- **The separation rule.** The slots are independently designable. The same culture can have a dream-sanctuary (C6) staffed by a reader (C4) who never enters trance (C1/C2), and a separate trance circle (C1/C2) with no reading office (C4). Real systems often separate them; fiction collapses them at its peril.
- **The cost rule.** Every slot has a cost, and the cost is where the politics lives: the entrant's training years, the sanctuary's land, the interpreter's fee, the uptake's risk, the institution's orthodoxy. A slot with no cost is a slot with no story.

## 3. State typology — etic coordinates, not a ladder

These are **etic** labels for design comparison, not emic categories and not stages. A culture may have three of them, merge two, or name one that this table does not. The table is a checklist of questions, not a taxonomy to impose.

| etic state | recognition cues (designable) | agency attributed | communication | typical uptake | caution |
|---|---|---|---|---|---|
| **ordinary dream** | sleep mentation, casual recall | passive | recounted or ignored | little or none | not every dream is a sign; the culture decides which are |
| **significant / "big" dream** | vividness, repetition, occasion, consensus | passive; sometimes a sender | shared, often in a fixed form | interpretation, action, archive | the "big dream" label is a social achievement, not a physiological type |
| **waking vision** | perceived while awake; sensory claim | passive | reported, often to a specialist | interpretation, warning, legitimation | cannot be externally verified; the institution supplies the warrant |
| **trance** | narrowed attention, altered responsiveness, posture, breathing | reduced | later report or none | ritual action, healing, performance | "trance" is a family, not one state; do not equate it with sleep |
| **possession** | voice change, third-person speech, amnesia or claimed amnesia | external (a spirit/other) | the spirit speaks through the entrant | diagnosis, negotiation, exorcism, cult | etic category; some traditions distinguish it sharply from journeying |
| **ecstatic flight** | journey narrative, soul-loss or soul-travel claim | the practitioner | first-person journey report | retrieval, healing, cosmography | Eliade's construct; not a universal core |
| **incubation dream** | sleep in a sacred place for a purpose | passive; a sender expected | the dream is told to the sanctuary staff | healing, oracle, votive | documented in specific traditions, not a general template |
| **deathbed vision** | reported at dying, often by witnesses | passive | witness report | comfort, prognosis, inheritance | interpretation is contested; do not make it a law |
| **lucid dream** | awareness within the dream; claimed control | the dreamer | report, sometimes trained | practice, play, therapy | cross-cultural evidence is uneven; not a universal attainment |

- **The no-ladder rule.** The table is ordered for exposition, not for evolution. A culture can have possession without trance, incubation without a dream-book, or a big-dream institution with no induction technology at all.
- **The recognition rule.** A state is socially real when the culture has a **public cue** and a **licensed recognizer**. A state that only the experiencer can identify is a private claim; a state that only an outsider can identify is a colonial diagnosis.
- **The translation rule.** Do not translate an emic term by an etic label without a note. "Dream," "vision," "trance," "possession," and "shaman" are all loanwords with histories; the entry uses them as design coordinates, never as claims about what a real tradition believes.

## 4. Induction technologies — mechanism claims separated from cultural meanings

| technique | mechanism claim (etic) | evidence status | access boundary | design hook |
|---|---|---|---|---|
| **sleep / incubation** | sleep in a designated place, with expectation and ritual frame | documented in Egyptian, Assyrian and Greek incubation (`divination-omen-systems.md:12,:89`) | do not reproduce a living sanctuary's restricted procedure | the sanctuary as hospital, court, and archive |
| **sleep deprivation** | cumulative sleep loss alters perception and suggestibility | mainstream physiology; cultural use variable | none beyond ordinary fatigue risk | the vigil as a test; the watch that produces a vision |
| **fasting** | metabolic stress and altered attention | mainstream physiology; ritual meaning variable | medical risk in a real practice; fiction should name the cost | the fast as an offering and as a political weapon |
| **sensory deprivation** | reduced input can produce imagery and disorientation | laboratory evidence; cultural framing variable | confinement can harm; do not present as a safe technique | the dark cell, the cave, the hood |
| **rhythmic drumming / dance** | rhythmic entrainment can facilitate trance in some participants | mixed; not sufficient or necessary; do not claim a "trance frequency" | living ceremonial repertoires are restricted | tempo, duration, participation, and the drummer's licence |
| **ordeal / pain** | stress, exhaustion and pain alter attention and arousal | mainstream physiology; ritual use documented | do not describe self-harm or torture as a recipe | the ordeal as licensure; the scar as credential |
| **plant helpers** | pharmacological action alters perception and affect | real pharmacology; cultural meaning is not derived from it | **restricted**: do not reproduce ceremonies, doses, or preparation | the plant as a person, a gift, a debt, or a prohibited route |
| **isolation** | solitude and darkness alter attention and mood | mainstream; cultural use variable | confinement risk | the solitary vigil; the exile's vision |
| **hyperventilation** | blood-gas changes produce dizziness and altered sensation | physiological; dangerous if prolonged | do not present as a safe method | the breath as a technique with a named cost |
| **meditation** | trained attention can produce altered states | mainstream; traditions differ | living traditions' instructions are not reproduced | the trained state vs the spontaneous one |
| **temperature** | heat/cold stress alters cognition and arousal | physiological; cultural use variable | real risk | the sweat lodge analogue, the cold vigil |

- **The anti-reduction rule.** A mechanism claim explains *how the body can enter the state*; it never explains *why the culture values it*. "The drum changes brainwaves" is not a theory of the drum's meaning, and "the plant contains a compound" is not a theory of the plant's personhood.
- **The access rule.** Plant helpers, ordeal, and living ceremonial techniques are the most extractive surface in this entry. Use published scholarship at the level of the reported institution; do not write a recipe, a dose, or a reconstructed rite (`verification/real-world-inspiration-boundaries.md:91-97`; `verification/myth-consistency-gate.md:34`).
- **The cost rule.** Every induction has a cost — time, pain, risk, money, purity, social standing. A cost-free induction is a magic button; a cost-free *vision* is a plot convenience.

## 5. The visionary career — the occupation, not the rite

`ritual-liminality.md:111` names "shaman" as one occupant of the permanent-liminal specialist slot. This table fills the occupation that occupies the slot; it does not restate the rite grammar.

| stage | actors | tests / markers | failure mode | design hook |
|---|---|---|---|---|
| **call** | the candidate, a recurring dream/illness/vision, the community | the experience is recognized by an existing specialist | an unrecognized call becomes madness or fraud | the call that arrives before the training; the call that is refused |
| **selection** | family, guild, sanctuary, court, self | heredity, aptitude, patronage, election, purchase | a candidate with no patron | the office that runs in a lineage vs the office that recruits |
| **training** | master, peers, ancestors/spirits | memorized repertoire, apprenticeship, supervised practice | training that teaches technique but not judgement | the training ledger: what is drilled, what is tested, what is secret |
| **ordeal** | the candidate, the master, the community | isolation, fasting, pain, vigil, public performance | an ordeal that kills or breaks the candidate (name the cost) | the ordeal as licensure, not as entertainment |
| **licensure** | the guild, sanctuary, court, congregation | examination, sponsor, public recognition, fee | a licence that cannot be refused or lost | the licence document, the badge, the seating order |
| **practice** | the practitioner, clients, patients, patrons | success, failure, competition, reputation | the practitioner who cannot say "no" | fees, referrals, rivals, malpractice |
| **failure** | the practitioner, the community, the institution | a failed cure, a false vision, a scandal | the failure that is hidden vs the failure that is tried | the malpractice trial; the rival's accusation |
| **retirement / succession** | the practitioner, heirs, the institution | age, illness, loss of clients, death | no successor; the office dies with the person | the retirement scene; the unteachable technique |

- **The career-over-rite rule.** A rite of passage has a beginning, a liminal middle and an end; a career has a beginning, a middle, an end, and a **reputation** that outlasts all three. Do not model a forty-year practice as one initiation.
- **The competence rule.** Separate the competences: inducing the state, reading the state, performing the cure, managing the client, managing the institution. A single character who has all five is a monopoly; a culture with five separate offices is a politics.
- **The failure rule.** A career with no failure mode is a fantasy of competence. Name what happens when the vision is wrong, the cure fails, the client dies, or the successor is absent.

## 6. Institutions that license and police entrance

| institution | who enters | who interprets | who acts | who pays | failure mode |
|---|---|---|---|---|---|
| **dream-sanctuary** | pilgrims, patients, the sick, the wealthy | sanctuary staff; dream-book | the sanctuary, the patient, the sponsor | votive offerings, fees, land | the sanctuary becomes a hospital, a court, or a racket |
| **dream-reader** | clients with a dream | the reader, alone or with a panel | the client, the reader's patron | fee per reading | the reader's code outlives its questions |
| **shaman** | the called, the trained, the licensed | the shaman, sometimes a second reader | the shaman, the client, the community | gifts, fees, retainer, reputation | the charismatic who cannot be succeeded |
| **prophet** | the called; often outside the guild | the prophet, a following, a text | the prophet, the ruler, the movement | donations, patronage, tribute | the prophecy that becomes a rival government |
| **possession cult** | the possessed, the medium, the congregation | the cult's senior medium or priest | the spirit, the medium, the cult | dues, offerings, performances | the spirit's demands outrun the cult's finances |
| **dream-sharing council** | any adult with a dream | the council, by rules | the council, the chief, the assembly | communal labor, no fee | the council becomes a conformity machine |
| **state dream office** | the ruler's dreamers, the court | the court's reader | the ruler, the bureau | the treasury | the ruler's dream is the only one that counts |
| **dream-book archive** | scribes, readers, initiates | the archive's custodians | the reader, the court | the archive's endowment | custody becomes power; the text is unreadable |
| **secret society** | the initiated | the senior members | the society, the client | initiation fees, dues | the secret is empty, or the society is a front |

- **The institution-is-not-the-state rule.** A dream-sanctuary can exist without a trance technology; a possession cult can exist without a dream-book; a state dream office can exist without either. The six slots are independently combinable, and the combinations are the design space.
- **The archive rule.** Custody of the dream-book is a political office. Who may consult, who may copy, who may translate, and who may burn it are separate rights; design them separately (`divination-omen-systems.md:126`; `register-strata-attestation.md:40`).
- **The second-reader rule.** A single-reader institution has no error correction. A two-reader rule (appeal, cross-check, rival school) is the cheapest way to make dream knowledge contestable — and to generate factions (`divination-omen-systems.md:52-56`).

## 7. The dream economy — who owns the dream

The lane-authored table below is the entry's distinctive contribution. It separates five rights that fiction usually collapses into one.

| right | question | typical holder | can it be sold? | can it be withheld? | conflict seed |
|---|---|---|---|---|---|
| **the dream** | who owns the experience? | the dreamer, the sender, the community | rarely; sometimes the dream is a gift | the dreamer may refuse to tell | a dreamer who sells a dream the community owns |
| **the telling** | who may narrate it? | the dreamer, a designated rememberer, a performer | yes, as performance or testimony | yes, by taboo or fear | a professional rememberer vs the dreamer's family |
| **the interpretation** | who may say what it means? | the reader, the archive, the guild | yes, by fee or patronage | yes, by esoteric restriction | rival readings; a client who shops for a reading |
| **the action** | who may act on it? | the council, the ruler, the patient, the guild | no; action is political | yes, by veto or delay | a ruler who acts on a private dream |
| **the archive** | who may keep and consult the record? | the sanctuary, the state, the guild, the family | sometimes, as a commodity | yes, by custody | a archive that holds a rival's dream |

- **The scarcity rule.** Dream knowledge is scarce when the state is rare, the reader is licensed, or the archive is closed. A world with universal dreaming and universal interpretation has no dream economy — which may be the point (a democratic dream culture), but say so.
- **The fraud rule.** Every dream economy has a fraud surface: the false dreamer, the bribed reader, the forged archive, the client who invents a dream to justify an action. Design the detection procedure, not just the fraud.
- **The secrecy rule.** Secrecy is not the same as rarity. A dream can be common and its interpretation secret; a technique can be rare and its results public. Track the two separately.
- **The political rule.** The most dangerous right is **action**: a dream that can command a war, a marriage, a execution, or a land transfer is a constitutional instrument. Give it a procedure, a counter-power, and a failure case.

## 8. The visionary register — one output of the state

The state produces marked speech, but the register is not the state. This table names the register features a visionary complex can generate; the register's own system is owned by `sacred-registers-liturgical-language.md` and `register-strata-attestation.md`, and the speech-act machinery by `semantics-pragmatics.md:88-94`.

| feature | state | social function | failure mode | coupled owner |
|---|---|---|---|---|
| **trance voice** | trance | marks the threshold; separates the practitioner from ordinary speakers | unintelligibility that the community cannot evaluate | `sacred-registers-liturgical-language.md:101` (recitation/chant) |
| **spirit speech** | possession | authorizes the message by relocating the speaker | the spirit sounds exactly like the officiant | `register-strata-attestation.md:3` (licensed speech) |
| **archaic formulae** | trance / possession | borrows the authority of antiquity | incomprehension; the formula becomes a password | `sacred-registers-liturgical-language.md:26-40` (the register's competences) |
| **glossolalia / invented language** | ecstasy / possession | marks the unlearnable and the unteachable | no interpreter; the performance is empty | `semantics-pragmatics.md:88-94` (speech acts) |
| **first-person spirit narration** | possession | lets the spirit testify in its own voice | the narrator's interests leak into the spirit's | `register-strata-attestation.md:40` (register law) |
| **silence / refusal** | vision / trance | withholds; makes the absence meaningful | reads as failure or as defiance | `linguistic-anthropology.md:9` (the speech event) |
| **command voice** | prophecy | turns a vision into an imperative | tyranny; the command outruns the institution | `register-strata-attestation.md:40` (force and consequence) |

- **The efficacy/authority split.** A spirit's command can be both a register output (this entry) and a binding act (`binding-speech-complex.md:39,:85`). Keep the two ledgers separate: the register explains who may speak and how; the binding ledger explains what the word holds and who executes it.
- **The register-is-earned rule.** A marked voice is credible only where the institution has already licensed the speaker. A stranger who enters trance in a foreign village is not automatically a visionary; the licence is the institution's, not the state's.
- **The comprehension rule.** A register can be efficacious without being understood (`sacred-registers-liturgical-language.md:26-40`), but a *vision* that nobody can interpret is not yet social knowledge. Separate the performance's efficacy from its interpretability.
- **The translation rule.** Spirit speech and glossolalia are the hardest surfaces to render in a fictional text. Decide whether the reader sees the gloss, the effect on listeners, or both; do not let the narrator translate by fiat.

## 9. Evidence and ethics — using real traditions without extraction

The entry's examples are design coordinates, not ethnographic verdicts. Six rules govern the use of real material:

1. **Use published scholarship at the level of the reported institution.** Cite the registering entry and its source; do not reconstruct a rite from fragments (`verification/real-world-inspiration-boundaries.md:91-97`).
2. **Do not reproduce restricted detail.** "Do not expose restricted ritual knowledge to fill a table. Mark an access boundary and choose a less extractive comparison" (`verification/myth-consistency-gate.md:34`).
3. **Do not universalize "shaman."** The word is Siberian-derived and has a history; Eliade's comparative construct is a design language, not a finding (`animal-symbolism.md:57`; `cosmology-cosmography.md:5`).
4. **Do not reduce the state to its mechanism.** Drumming, fasting, and plants are techniques, not explanations (`§4`).
5. **Do not conflate the ancestral Dreaming with sleep dreams.** `australia-aboriginal.md:36-40` is law-time; this entry is the sleep/vision/trance complex, and the two must be named separately in any world bible.
6. **Do not turn a living tradition into a faction.** A fictional cult may borrow the *institutional question* (who licenses, who pays, who dissents); it must not borrow a community's names, rites, or restricted knowledge.

| evidence trap | symptom | test | repair |
|---|---|---|---|
| **the exotic shaman** | a wise outsider with universal powers | does the figure have a training path, a fee, a failure, and a rival? | give the figure an institution and a politics |
| **the drug shortcut** | the plant explains the religion | is the plant's meaning derivable from its pharmacology alone? | separate mechanism from cultural framing |
| **the primitive mentality** | the culture is pre-rational, so anything goes | does the culture have error correction, sceptics, and procedure? | give it a second reader and a fraud trial |
| **the colonial gaze** | the specialist is described only from outside | whose terms name the state, the office, the fee? | add an emic vocabulary and a practitioner's account |
| **the one-informant culture** | one practitioner stands for a whole tradition | are there regional, generational, or factional variants? | add a rival school or a dissenting lineage |
| **the decontextualized technique** | a drum, fast, or plant is lifted without its sequence | what precedes, follows, and pays for the technique? | restore the sequence and the cost |
| **the Dreaming conflation** | "Dreaming" is used for ordinary dreams | does the culture distinguish law-time from sleep? | name the two separately (`australia-aboriginal.md:36-40`) |
| **the possession/shamanism collapse** | every altered state is called shamanism | is the agency external or the practitioner's? | separate possession from journeying, or say the culture merges them |

## 10. Failure modes

| failure | symptom | test | repair |
|---|---|---|---|
| **the exotic shaman** | a mysterious outsider with no training, fee, or failure | can the character be refused, paid, or sued? | build the career (§5) and the institution (§6) |
| **the drug shortcut** | the substance explains the vision and the culture | what does the culture say the plant *is*? | separate mechanism from meaning (§4) |
| **the chosen-one career** | the call is the whole story; training is skipped | what did the practitioner sacrifice, and who trained them? | stage the training and the ordeal (§5) |
| **the prophecy that always lands** | every dream comes true | what happens when a dream is wrong? | design the failure and the false-dream trial (§7) |
| **the dream as plot explanation** | a dream arrives to tell the protagonist what to do | could the information arrive another way? | make the dream cost something, or cut it |
| **possession as costume** | the spirit voice is a special effect | who interprets the spirit, and who can contradict it? | give the possession an institution and a politics (§6, §8) |
| **the extractive copy** | a real tradition's rite is reproduced in detail | is the detail necessary, and is it restricted? | replace it with an invented institution (`§9`) |
| **the universal Dreaming** | "Dreaming" means any dream or any myth | does the culture distinguish law-time from sleep? | separate the two (`australia-aboriginal.md:36-40`) |
| **the state without an institution** | everyone has visions; no one is licensed | who says which vision counts? | add a recognizer and an uptake rule (§2) |
| **the institution without a state** | an office exists, but no one enters the state | what does the office actually do? | add the induction and the recognition cue (§3, §4) |

## 11. Build protocol

1. **Choose the state inventory.** List the states the culture recognizes (not the etic table, the emic names), and for each write the public cue and the licensed recognizer. Test: can a stranger tell a big dream from an ordinary one?
2. **Choose the induction.** Pick one to three techniques from §4, name the cost of each, and decide who controls the technique. Test: what happens if the technique fails?
3. **Choose the entrant.** Decide who may enter (heredity, call, training, purchase, election) and who is excluded. Test: can the licence be lost? What does an unauthorized entrant risk?
4. **Choose the interpreter.** Decide who reads the state, with what code, and whether a second reader exists. Test: what happens when two readers disagree?
5. **Choose the uptake.** Decide what the community does with the result: decide, heal, crown, exile, archive, or nothing. Test: what is the worst thing a vision can authorize?
6. **Build the institution.** Name the office, the sanctuary, the guild, or the court; give it a fee, a budget, a rival, and a succession rule. Test: who pays, and who profits?
7. **Build the dream economy.** Allocate the five rights in §7, and name the fraud surface and the detection procedure. Test: who can be bribed, and who can refuse?
8. **Design the register.** Pick two or three features from §8 and decide what they mark. Test: can an outsider fake the register? What gives it away?
9. **Design the counter-case.** Add a sceptic, a rival school, a false dreamer, or a failed cure. Test: does the institution have an error-correction procedure?
10. **Test with a scene.** Write one scene in which a dream/vision/trance is told, interpreted, and acted on (or refused). Cut any element that does not change a decision, a relationship, or a cost. Hand off the brief, not the canon.

## 12. Worked NON-CANON fixture — the Orrun dream complex

**Declared invented.** The Orrun are a highland herding culture invented for this exercise; no real tradition is described, and nothing here decides any world. The fixture is disposable.

**The six slots.**

| slot | Orrun design |
|---|---|
| **STATE** | four emic states: *the ordinary dream* (ignored), *the deep dream* (incubation at the spring), *the shaking* (trance by dance and drum), *the rider* (possession by a lineage spirit) |
| **INDUCTION** | deep dream: sleep one night at the Vash spring after a day's fast; shaking: communal dance with a hand-drum, led by a dream-keeper, until the dancer loses ordinary speech; rider: an inherited spirit arrives during a fever or a vigil, and is recognized by the lineage's dream-keeper |
| **ENTRANT** | any adult may incubate; the shaking is led by licensed dream-keepers; the rider is called by illness and must be accepted by the lineage; children and outsiders are excluded from the shaking |
| **INTERPRETER** | the dream-keeper reads the deep dream from a notched-stick archive; the rider's spirit speaks in its own voice and is cross-examined by a second dream-keeper; the council hears both |
| **UPTAKE** | herding routes, water disputes, healing, and succession; a deep dream can call a council, but only the council can bind the clan |
| **INSTITUTION** | the Vash spring sanctuary, the dream-keepers' lineage (hereditary, with adopted apprentices), the council of herd-heads, and the notched-stick archive |

**The career.** A dream-keeper is called by a recurring dream of a white ram, trains for three years, spends one night alone at the spring in late winter (the ordeal), is recognized by the council, practices for life, and retires when the dreams stop. A dream-keeper who gives a false reading can be tried by the council; the penalty is loss of the archive key, not death. The office is hereditary in principle and adoptive in practice, which is the clan's standing political quarrel.

**The dream economy.** The dreamer owns the dream; the dream-keeper owns its interpretation; the council owns action; the archive owns the record; telling is public at the spring but a dream told outside the spring is not admissible. A client may buy a reading but not an action. A dream-keeper may refuse a reading; a council may refuse a dream.

**A worked scene (NON-CANON).** A dry summer. A herder, Nera, dreams of a white ram walking east through a gap in the ridge. The dream-keeper reads it as a route sign and calls the council. A rival dream-keeper reads the same dream as a warning against the eastern gap, because the ram is the lineage's spirit and the east is the lineage's burial ground. The council sends a scout, who finds water in the east gap but also a rival clan's herds. The council decides to send an embassy, not a migration. The scene's outcome is political, not evidential: the dream did not prove the water; it started a procedure that produced a scout, a negotiation, and a new boundary.

**What the fixture demonstrates.** The state is recognized by a public cue; the induction has a cost; the entrant is licensed; the interpreter is contestable; the uptake is institutional; the economy has rights, refusal, and fraud; the register (the ram as metonym, the spirit's first-person voice, the council's silence before the vote) is an output, not a decoration. The fixture decides nothing about any world.

## 13. Calibration bank

| claim | status | reason | use |
|---|---|---|---|
| sleep and dreaming are panhuman | **mainstream** | ordinary physiology; cultural elaboration varies | the baseline, not the explanation |
| cultures pattern significant dreams and their uptake | **mainstream** | comparative ethnography; the "big dream" is a social achievement | design the recognition and the uptake |
| dream incubation is a documented institution | **mainstream** | Egyptian dream book, Assyrian incubation, Greek Asclepieia (`divination-omen-systems.md:12,:89`) | one induction model among several |
| Eliade's "archaic techniques of ecstasy" is a universal core | **contested** | comparative construct; criticized for decontextualizing and universalizing | use the documentation, not the universal claim |
| the shaman/priest/medium typology is a clean partition | **contested** | etic categories overlap in practice | use as a design axis, not a census |
| "altered state" is one thing | **contested** | a family of states with different phenomenology and physiology | design several states, not one slider |
| neurophysiology explains trance's cultural meaning | **contested** | correlates do not supply meanings | mechanism claims stay in §4 |
| trance is therapeutically efficacious | **contested** | outcome studies vary by tradition, diagnosis, and context | do not promise a cure; design the claim and the failure |
| possession and shamanism are opposites | **contested** | traditions merge, separate, or alternate them | ask who acts: the spirit or the practitioner |
| Lévy-Bruhl's "primitive mentality" | **discredited** | colonial-era prelogical framing | refused; do not use |
| shamanism is mental illness | **discredited** | diagnostic imperialism; no reliable cross-cultural basis | refused |
| dreams are naturally prophetic | **refused** | a truth claim no evidence supports | treat prophecy as an institutional claim, not a law |
| the plant explains the religion | **refused** | pharmacological reduction | separate mechanism from meaning |
| the Jungian shaman archetype is ethnography | **discredited as ethnography** | universalizing psychology, not comparative data | fiction may use it; do not cite it as evidence |
| "Dreaming" means ordinary dreams | **discredited conflation** | the ancestral Dreaming/Tjukurpa is law-time (`australia-aboriginal.md:36-40`) | name the two separately |
| Harner's core-shamanism is ethnographic | **discredited as ethnography** | modern, book-transmitted practice (`animal-symbolism.md:57`) | fine as fiction; label it |

## 14. Decision record

| ID | decision | basis | status |
|---|---|---|---|
| DR-DVT-01 | Claim the **state/institution complex**, not the dream-reading technology | `divination-omen-systems.md:52-56,:89,:147-158` owns the reading; the sweep finds no system owner | adopted; §1 boundary |
| DR-DVT-02 | Treat state labels as **etic coordinates, not a ladder** | comparative categories overlap; the emic vocabulary is the culture's | adopted; §3 |
| DR-DVT-03 | Separate mechanism claims from cultural meanings | §4's anti-reduction rule; the corpus's calibration discipline | adopted; §4 |
| DR-DVT-04 | Use living traditions only through published scholarship; no recipe or reconstructed rite | `real-world-inspiration-boundaries.md:91-97`; `myth-consistency-gate.md:34` | adopted; §9 |
| DR-DVT-05 | Distinguish the ancestral Dreaming/Tjukurpa from sleep dreams | `australia-aboriginal.md:36-40` | adopted; §1, §9 |
| DR-DVT-06 | Treat "shaman" as a historically situated, Siberian-derived term; no universal | `animal-symbolism.md:57`; `cosmology-cosmography.md:5` | adopted; §9 |
| DR-DVT-07 | Keep the visionary career distinct from the rite-of-passage grammar | `ritual-liminality.md:39-40,:111` owns the grammar and the slot | adopted; §5 |
| DR-DVT-08 | Present the dream economy as **lane-authored craft**, not a universal institution | no published standard for the five-rights table; it is a design instrument | adopted; §7 |
| DR-DVT-09 | Keep sacred-register, register-law and speech-act machinery in their owning entries | `sacred-registers-liturgical-language.md:3,:26-40`; `register-strata-attestation.md:3,:40`; `semantics-pragmatics.md:88-94` | adopted; §8 |
| DR-DVT-10 | Name the unregistered specialist shelf as a route, never as inspected support | measured 0 files for Bourguignon, Winkelman, Lambek, Csordas, Vitebsky, Kehoe, Hamayon | adopted; sources block |
| DR-DVT-11 | End at the handoff; decide no world, authorize no rite, reconstruct no tradition | `corpus/QUALITY.md:5`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:2` | adopted; §15 |

## 15. Canon boundary and handoff

This entry is a **method and reference** file for the myth-symbol partition. It does not say that any world has a dream-sanctuary, a shaman, a possession cult, or a vision quest; it says how such an institution can be designed, what it must answer, and where its neighbours' surfaces begin. It does not adjudicate any real tradition's practice, and it does not authorize the reproduction of restricted knowledge. Canon recording, consistency verification, and any world-bible decision belong to lore-shokunin; the handoff runs through `corpus/knowledge/synthesis/worldbible-integration-contract.md:2`. Restricted real-world material is screened by `corpus/knowledge/verification/real-world-inspiration-boundaries.md`, not here. Corrections to this entry are new sections or a new entry, never rewrites.
````

## 5. Self-audit (this seat)

### 5.1 Citation resolution

A read-only script extracted every `path:line` and `path:a-b` reference from this file and checked (a) the path exists at `c9f4eaa`, and (b) every line number is in range. Result:

```
distinct existing paths: 24
distinct line citations: 141 mechanically extracted (plus the detached `:N` refs checked in §5.2)
missing paths (expected: the proposed target only): ['corpus/knowledge/myth-symbol/dream-vision-trance.md']
out-of-range lines: []
```

The proposed target is correctly absent (that is the landing precondition); every other cited path exists and every cited line is in range. The 24 existing paths are the 18 corpus knowledge files, `corpus/QUALITY.md`, `corpus/README.md`, `reports/round-28/readme/sweep.py`, `reports/round-42/scout/K02-myth-gaps.md`, `reports/round-44/scout/K04-gap-verify.md`, and the two round-44 contract files. The per-path line counts are:

| path | cited lines |
|---|---:|
| `corpus/QUALITY.md` | 21 |
| `corpus/README.md` | 13 |
| `corpus/knowledge/civilizations/australia-aboriginal.md` | 5 |
| `corpus/knowledge/culture-material/music-instrument-lexicon.md` | 1 |
| `corpus/knowledge/linguistics/linguistic-anthropology.md` | 1 |
| `corpus/knowledge/linguistics/register-strata-attestation.md` | 1 |
| `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md` | 1 |
| `corpus/knowledge/linguistics/semantics-pragmatics.md` | 7 |
| `corpus/knowledge/myth-symbol/animal-symbolism.md` | 2 |
| `corpus/knowledge/myth-symbol/binding-speech-complex.md` | 2 (detached `:39,:85`) |
| `corpus/knowledge/myth-symbol/cosmology-cosmography.md` | 1 |
| `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md` | 1 |
| `corpus/knowledge/myth-symbol/divination-omen-systems.md` | 22 |
| `corpus/knowledge/myth-symbol/ritual-liminality.md` | 5 |
| `corpus/knowledge/synthesis/coupling-model.md` | 1 |
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | 1 |
| `corpus/knowledge/verification/myth-consistency-gate.md` | 1 |
| `corpus/knowledge/verification/real-world-inspiration-boundaries.md` | 7 |

The remaining paths carry single line refs: `reports/round-28/readme/sweep.py` (no line; the `topic_of` rule), `reports/round-42/scout/K02-myth-gaps.md:216-260` (544 lines total), `reports/round-44/scout/K04-gap-verify.md:10,:63` (259 lines total), `reports/round-44/claims.json:7` (70 lines), `reports/round-44/targets.json:6,:29` (46 lines), and this file's own self-reference.

### 5.2 Spot-checks of the load-bearing anchors

| anchor | line content checked | verdict |
|---|---|---|
| `divination-omen-systems.md:52-56` | the five-slot frame; `:56` says an *open* code needs a strong interpretive office | matches |
| `divination-omen-systems.md:64` | Cicero's natural/artificial pair as an etic design axis | matches |
| `divination-omen-systems.md:89` | technique row 12, "Dream-oracle & incubation" | matches |
| `divination-omen-systems.md:126` | the dream-sanctuary institution row | matches |
| `divination-omen-systems.md:147-158` | §8 boundary table; claims neither the state nor its specialist | matches |
| `ritual-liminality.md:39-40` | liminality and communitas | matches |
| `ritual-liminality.md:111` | permanent liminal specialists, "shaman" named as a slot | matches |
| `animal-symbolism.md:53` | spirit helpers and their holders | matches |
| `animal-symbolism.md:57` | Harner's core-shamanism calibration | matches |
| `binding-speech-complex.md:39,:85` | §1 boundary (efficacious speech, not suasion) and §3 master channel table | matches |
| `music-instrument-lexicon.md:96,:98,:100` | drum as steed/cosmos; instruments that speak; talking drum | matches |
| `australia-aboriginal.md:36-40` | Dreaming/Tjukurpa as ancestral law-time, not sleep dreams | matches |
| `sacred-registers-liturgical-language.md:26-40` | §1 boundary table (six neighbouring surfaces) | matches |
| `semantics-pragmatics.md:88-94` | speech acts and the five-class table (commissives at `:94`) | matches |
| `real-world-inspiration-boundaries.md:91-97` | sacred-material red lines, including restricted initiation knowledge | matches |
| `myth-consistency-gate.md:34` | the restricted-knowledge rule quoted in §9 | matches |

### 5.3 Mechanical integrity

```
$ grep -c '^````' reports/round-44/cov/C01-entry-draft.md
2                      # one opening fence, one closing fence
$ grep -c '^- topic:' reports/round-44/cov/C01-entry-draft.md
1                      # the entry has exactly one topic line (length 1295 chars incl. prefix)
$ git status --porcelain
?? reports/round-44/   # no corpus/, tools/, README, LOG, or filed-round byte touched by this seat
```

The draft is a single fenced `markdown` block (`## 4`); sections `## 1`–`## 15` inside it are the entry body. The out file's own `## 1`–`## 5` are the seat report, outside the fence.

### 5.4 What this seat did **not** verify

- **No external source was fetched or resolved** (no network at this seat). Every external bibliographic item is either registered in-corpus (and carries the registering entry's own limits) or marked `(to-verify)`; the unregistered specialist shelf (Bourguignon, Winkelman, Lambek, Csordas, Vitebsky, Kehoe, Hamayon) is named as a reader's route, not as inspected support.
- **No real tradition was reconstructed.** The only concrete examples are the in-corpus citations and the invented Orrun fixture (§12), which is declared NON-CANON and decides nothing.
- **K02 had not landed** at this seat's write time. The draft follows K04's independent, scout-verified gap (`K04-gap-verify.md:10`, §4–§5). If K02 names a different gap, the integrator must choose one; this draft is then a spare, and the rhetoric candidate noted below is a second spare.
- **The README row is not applied** and the `total 223 → 224` arithmetic is stated for C02, not executed by this seat.

### 5.5 Alternate candidate considered (not drafted)

Before K04 landed, this seat independently swept **rhetoric / persuasion** as a possible gap: at `c9f4eaa`, `\brhetoric` occurs in **44** files / **65** occurrences, `\bpersuas*` in **3**, `\borator*` in **7**, with **0** topic-line owners, **2** civilization-specific section headers (`olmec.md:125` persuasive portraiture; `parthia.md:78` outsider rhetoric), no filename collision, and **0** prior-scout hits. It is a real unowned surface, but this draft follows K04's scout-verified gap because (a) K04 is the claim-C scout output on disk, (b) the dream/trance complex has an in-corpus source shelf (Eliade, Harner, Artemidorus, Gardiner, Oppenheim, Dodds, van Gennep, Turner) while the rhetoric shelf is mostly unregistered, and (c) claim C is +1 only. The rhetoric sweep is recorded here as a spare, not as the landing.

### 5.6 Handoff summary

- **Draft path:** `reports/round-44/cov/C01-entry-draft.md` (this file), single fenced block at `## 4`.
- **Proposed landing:** `corpus/knowledge/myth-symbol/dream-vision-trance.md`; myth-symbol 26 → 27; total 223 → 224.
- **Integrator must:** apply the fenced block byte-for-byte; let C02 add the README row in filename order with the `- topic:` text byte-equal; run the r28 sweep (`224 == 224`); and reconcile K02 vs K04 before landing.
- **No filed byte was edited; no corpus byte was staged; no runner was executed; no commit/push/install/network.**
