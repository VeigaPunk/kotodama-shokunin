# E01 — cartography entry: boundary table (claim C)

- Seat: `E01` | role: executor (boundary-table author) | claim: **C** (coverage)
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/cov/E01-boundary.md` (this file)
- Non-author statement: I wrote no other round-48 fragment and touched no corpus byte. Every ruling below is read from the live tree at `a01405d`; every cited line is quoted from `sed -n '<n>p'` output reproduced in §6.
- Deliverable: one integration-ready fenced block — the entry's **§1.2 boundary table**, its four rules of use, and the three non-collision notes — plus the mandatory gap sentence that closes r47's **B8** (cosmography's `:27` competing sentence).

**One-line judgment.** All seven K02 seed neighbours are **adjacent, not collisions**: each owns an *input* or an *output* of the map-production chain, and none owns the surveyed→projected→drawn→reproduced sheet. The seed's seven rows are correct; I add **six** rows the seed missed (four of them are r47's **P2-7**), and I rule **two** candidates out of the table as non-collisions (`divination-omen-systems.md`, `polynesia-navigation.md`) with evidence. No row claims a second owner. The single wording risk is `cosmology-cosmography.md:27`, and it is fixed by the sentence in §3.

---

## 1. What this fragment is, and where it goes

The entry's body opens with a one-owner claim. The boundary table is the proof of that claim: for each neighbour it states what the neighbour owns (with a live `file:line`), what this entry owns *instead*, and the ruling. It belongs immediately after the entry's opening ownership paragraph — suggested **§1.2**, "Boundary — what each neighbour keeps". C01/C02 own the final section numbering; this fragment asserts no cross-reference number except that suggestion (so r47's B5/B6 class cannot recur here).

The table is deliberately a **division of labour**, not a disclaimer list. "X does not cover maps" is weak; "X owns the route institution and this entry owns the route's representation" is a rule a drafter can act on. That distinction is the point of the fragment.

Length: **15 lines** of table (13 rows) + **7 lines** of rules + **4 lines** of non-collision notes + the 4-line gap sentence = **~30 body lines**. Against the partition's 103–221-line band (max 221, `wc -l corpus/knowledge/culture-material/*.md | sort -n`), that is a deliberate, small share of the ≤~250-line discipline, not a second over-build.

---

## 2. Integration-ready fenced block

```markdown
### 1.2 Boundary — what each neighbour keeps

The corpus owns every *input* of a map and every *use* of one; it owns no made sheet. The rule the table applies: **whoever owns the input owns its vocabulary, whoever owns the output owns its document.** No row below is a collision; each is a handoff with a stated seam.

| Neighbour | Owns (verified at HEAD) | This entry owns instead | Ruling |
|---|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | world models (five axes) and the T-O diagram as symbolic, "not survey maps" (`:71`, `:102`); cosmography as "how the world is drawn (maps)" (`:27`); toponyms handed to naming-systems (`:133`) | the sheet as a production object: surveyed, projected, drawn, reproduced | adjacent — the gap sentence names `:27` and splits world-picture from sheet |
| `myth-symbol/sacred-topography-pilgrimage.md` | the holy-site typology and sacred geography "as a diagram" (`:5`); the three route types (`:69`); route selection in its build order (`:124`) | how a route is measured and drawn — the itinerary line, the strip map | adjacent — route *type* stays theirs, route *representation* is ours |
| `myth-symbol/direction-symbolism.md` | the orientation register and frames of reference (`:21`); the true-vs-magnetic compass trap (`:51`); maps named as a *use* of the relative frame (`:48`) | the map convention: which north the sheet declares, the compass rose, the graticule | adjacent — `:51` decides *which* north; this entry decides what the sheet does once it is decided |
| `culture-material/architecture-settlement-lexicon.md` | built-environment lexicon; the castrum grid "surveyed with the groma" (`:95`); instrument + founding rite + claim word (`:101`) | land survey as a production step, and the cadastral *document* (the sheet, not the city) | adjacent — architecture owns the built plan; this entry owns the drawn document |
| `culture-material/writing-media-surface-economy.md` | the seven surface families, cost ladder and survivor's ledger (`:3`, `:48`, `:73`, `:78`); zero map mentions in the file | map media and reproduction: skin, cloth, paper; manuscript vs print; copperplate; the atlas; the copy chain | adjacent — cite the ladder, do not re-price surfaces |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo / cartographic-history source class; "the copy chain is the evidence" (`:58`) | the map *form* a lienzo instantiates; the genre as a form class | adjacent — source provenance and custody stay theirs |
| `culture-material/transport-mobility-lexicon.md` | the route as institution and its maintenance clause (`:28`); the Qhapaq Ñan (`:35`); DR-TR-02 (`:117`) | the representation of a route on a sheet | adjacent — never re-derive upkeep |
| `culture-material/agrarian-field-system-lexicon.md` | the PARCEL and CLAIM institutions and their words — "field names, boundary words, tenure words, land measures" (`:42`, `:45`) | the drawn cadastral sheet | adjacent — the sharpest under-claim risk: `cadastral` appears at `architecture-settlement-lexicon.md:95` and `japan-medieval-sengoku.md:157`, but no entry owns the document |
| `culture-material/craft-artisan-lexicon.md` | the workshop as speech community; the apprentice→journeyman→master ladder (`:54-65`); attribution conflict as a legal genre (`:88`) | the mapmaker's workshop as a trade class and the surveyor as an office | adjacent — cite the ladder at `:54-65`, never `:44` (that line is the steel-grading row) |
| `culture-material/trade-economy-lexicon.md` | measure, coin and contract vocabulary; measures from body, substance, action, container (`:17`); split-object authentication — tally stock/foil, *symbolon*, chirograph (`:92`, `:121`) | the measures *fixed onto* the sheet, and the map as a legal instrument at that boundary | adjacent — metrology and the split-object rule stay theirs |
| `myth-symbol/celestial-symbolism-calendars.md` | the sky as symbol system; the Polynesian sidereal compass as a "celestial *language of direction*" (`:84`) | the star chart *as a map form*, admitted only under this entry's five-condition test | adjacent — and the sidereal compass is not a chart (`polynesia-navigation.md:60`) |
| `myth-symbol/sacred-kingship-mythic-charter.md` | the eight legitimation channels; the charter as four questions (`:44`); "the regalia as found title-deed" (`:70`) | the map's documentary warrant: who attests the sheet, who may copy it | adjacent — cite legitimation, do not restate it |
| `linguistics/naming-systems.md` | toponymy (`:40`); "Every renaming is datable; a map is an archive of coups" (`:70`); royal-name taboo (`:97`) | the toponym *layer* of the sheet | adjacent — quote `:70` verbatim |

**Four rules of use.**

1. **Input/output rule.** A row may claim only the input or the output of the chain. Whoever owns the input owns its vocabulary; whoever owns the output owns its document.
2. **Anchor rule.** Every "owns" cell carries a live `file:line`. A row with no anchor is deleted, not softened.
3. **No-restatement rule.** The `- couples:` line names these files once; the table states the seam; the body cites. No neighbour's content is re-taught here.
4. **Division rule.** Adjacency is written as a division of labour, never as a disclaimer. If a row needs the phrase "does not cover", it has not found the seam yet.

**Ruled out of the table (non-collisions, with evidence).**

- `myth-symbol/divination-omen-systems.md` — owns sign-reading; it contains **no cartographic material**. Its two `map` hits are verbs ("The code maps to twelve prescriptions", §9 worked design example; "maps directly onto that gate's symbol-ledger row", §13 coupling notes). No row is owed.
- `civilizations/polynesia-navigation.md` — owns navigation, and its own table rules the star compass "A mental bearing framework, not a chart showing the canoe's absolute position" (`:60`). It reinforces this entry's non-claim rather than competing with it.
- `civilizations/japan-medieval-sengoku.md:157` — the "a neat Edo cadastral map must not be treated as a direct Sengoku map" caution is *evidence* that a map is dated as an object, not an ownership claim.
```

---

## 3. The mandatory gap sentence (r47 B8 fix)

This sentence is part of the fragment's handoff even though it sits in the entry's opening paragraph, because the boundary table cannot carry the whole load: the table says cosmography is adjacent, the sentence says *why* against cosmography's own definition.

```markdown
**The gap.** Cosmography owns the world-picture: `cosmology-cosmography.md:27` defines it as "the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked … and built", and `:71`/`:102` then rule the T-O diagram "symbolic, not survey maps". This entry takes the other half of that sentence — the sheet as a production object. Cosmography answers *what the drawing claims about the world*; this entry answers *how the drawing was made, who may copy it, and what it is silent about*. A corpus that owns both halves can tell a cosmogram from a survey; a corpus that owns only the first cannot.
```

Why this is the correct fix rather than an over-claim: the two entries answer different questions about the same paper. `:27` is a definition of cosmography's *subject* (the world-drawn claim), not an assertion of the survey chain, the projection arithmetic, the reproduction economics, or the map's legal warrant — none of which appear in `cosmology-cosmography.md` (155 lines; `grep -niE 'survey|cadastr|portolan|graticule'` → only `:71`, `:116`, both by-product mentions).

---

## 4. Ruling summary — seven seed rows, six added, two excluded

| # | Neighbour | Verdict | Basis |
|---|---|---|---|
| 1 | `myth-symbol/cosmology-cosmography.md` | adjacent (wording risk fixed) | `:27` competing definition; `:71`/`:102` explicit disclaimer |
| 2 | `myth-symbol/sacred-topography-pilgrimage.md` | adjacent | `:5` "as a diagram"; `:69` route types; `:124` route selection |
| 3 | `myth-symbol/direction-symbolism.md` | adjacent | `:51` compass trap; `:48` maps as a frame *use* |
| 4 | `culture-material/architecture-settlement-lexicon.md` | adjacent | `:95` groma + "the grid is cadastral"; `:101` instrument+rite+claim word |
| 5 | `culture-material/writing-media-surface-economy.md` | adjacent | `:3` seven families; `:78` cheapness widens the base; 0 map mentions |
| 6 | `civilizations/mesoamerica-primary-sources.md` | adjacent | `:58` lienzos; "the copy chain is the evidence" |
| 7 | `culture-material/transport-mobility-lexicon.md` | adjacent | `:28` maintenance rule; `:117` DR-TR-02 |
| 8 | `culture-material/agrarian-field-system-lexicon.md` | **added** — adjacent | `:42` PARCEL, `:45` CLAIM; owns tenure *words*, not the sheet |
| 9 | `culture-material/craft-artisan-lexicon.md` | **added** (r47 P2-7) | ladder `:54-65`; attribution `:88`; B4 says `:44` is wrong |
| 10 | `culture-material/trade-economy-lexicon.md` | **added** (r47 P2-7) | measures `:17`; split-object authentication `:92`, `:121` |
| 11 | `myth-symbol/celestial-symbolism-calendars.md` | **added** (r47 P2-7) | `:84` sidereal compass as direction language |
| 12 | `myth-symbol/sacred-kingship-mythic-charter.md` | **added** (r47 P2-7) | `:44` charter as four questions; `:70` regalia as title-deed |
| 13 | `linguistics/naming-systems.md` | **added** | `:40` toponymy; `:70` archive-of-coups; `:97` taboo |
| — | `myth-symbol/divination-omen-systems.md` | **excluded** — non-collision | 0 cartographic content; both `map` hits are verbs |
| — | `civilizations/polynesia-navigation.md` | **excluded** — non-collision | `:60` "not a chart" |

**Six added rows, two exclusions:** the seed's seven plus six = thirteen rows; the two excluded candidates are notes, not rows. If C05's length check bites, the documented cut order is **11 → 12 → 10** (fold each into one "also adjacent" sentence), and the rows that may never be cut are **1–9 and 13** — row 8 because it is the real under-claim risk, row 9 because r47's B4 miscite lives exactly there, row 13 because it carries the only verbatim quote.

### 4.1 Reconciliation with K01's spec table

K01's spec table (`reports/round-48/scout/K01-rightsized-spec.md:213-231`) is 13 rows = 12 real neighbours + divination. This fragment differs in four deliberate ways; each is traceable, and C01 should apply *this* table, not K01's, where they differ:

- **`agrarian-field-system-lexicon.md` added (13th real neighbour).** K01's table omits it. C07 independently files the omission as **U1, blocking** (`reports/round-48/cov/C07-boundary.md` §Verdict: "K01's 13-row tabl[e]" fails the agrarian row). Row 8 closes it with `:42`/`:45`. This is the only *substantive* divergence.
- **Divination demoted from row to note.** K01 gives it a row anchored at `:3` (its topic line). A row in this table asserts an ownership seam; divination has none, so the honest form is the negative note, with the two verb-only `map` hits as evidence. If C01 prefers K01's shape, promote the note to a row without changing its content.
- **`polynesia-navigation.md` added as a second note.** K01 does not name it; `:60`'s "not a chart" is the strongest single piece of evidence that navigation and cartography are separate registers.
- **Anchors extended, not replaced.** Row 10 now cites `:92`/`:121` (split-object authentication) beside `:17` (measures); row 12 cites `:70` (regalia as found title-deed) beside `:44` (charter as four questions). Both K01 seams were re-read live this pass (transcript §6.3) and are load-bearing for the map-as-instrument argument.

Row count after reconciliation: **13 real neighbours + 2 notes = 15 table lines + 2 note lines**, still inside the fragment's ~30-line budget.

---

## 5. Defect avoidance against r47 R03 B1–B9

| r47 defect | Status in this fragment |
|---|---|
| **B1** arithmetic (200 m = 20× not 10×) | No ratio arithmetic is offered. The numbers here are measured line counts and grep counts, each reproduced in §6. |
| **B2** unreproducible gap count | The gap count is stated as `grep -rni 'cartograph' corpus/knowledge/` → **2 files / 2 lines**, listed by path. `:71` is cited as the "Mappa Mundi / survey maps" disclaimer, *not* counted as a `cartograph` hit. |
| **B3** false quote accusation | `naming-systems.md:70` is quoted verbatim as "Every renaming is datable; a map is an archive of coups." No correction is proposed; the line is real. |
| **B4** mis-cited workshop ladder | Row 9 cites `craft-artisan-lexicon.md:54-65` (header `:54`, systems `:56-63`, rule `:65`) and adds the explicit negative: `:44` is the Steel (Japan) grading row. |
| **B5/B6** wrong section cross-refs | This fragment asserts no internal section number except the suggested placement "§1.2"; no other § target is claimed. The drafter numbers the section. |
| **B7** worked-example inconsistency | Not in scope; this fragment contains no worked example. |
| **B8** "owns no made map" vs cosmography `:27` | Fixed by the §3 sentence, which cites `:27` alongside `:71`/`:102` and splits the two subjects. |
| **B9** "5 of 8 forms" table | Not in scope; no form table here. |
| **P2-7** four missing boundary rows | Closed: rows 8–13 add six, including craft, trade-economy, celestial and sacred-kingship. |

**One-owner verdict.** The new entry lands as **A** (new file, slug free) and creates **no second owner**: every neighbour's ownership is quoted live, and the sheet (survey → projection → symbolization → reproduction) is claimed by none of the 223 entries — the topic-line sweep for `cartograph|mapmak|portolan|cadastr|survey map|mappa` returns **0**, and the filename sweep returns **0** (§6.2).

---

## 6. Verification transcript (baseline `a01405d`, 2026-10-19)

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

### 6.1 Baseline and partition

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ wc -l corpus/knowledge/culture-material/*.md | sort -n | tail -4
   179 .../agrarian-field-system-lexicon.md
   201 .../writing-media-surface-economy.md
   221 .../funerary-material-culture.md
  3756 total
```

Partition band: min 103, max 221 (25 files). The fragment's ~30 body lines sit inside the ≤~250 discipline.

### 6.2 Ownership sweep (no second owner)

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' -o -iname '*survey*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '.../cartography-and-mapmaking.md': No such file or directory
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|survey map|mappa)' corpus/knowledge/ | wc -l
0
$ grep -rni 'cartograph' corpus/knowledge/ | cut -c1-140
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:- Calibration: "everyone before Columbus believed in a flat earth" is a 19th-centu
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:| Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahua
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l   # files
2
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l   # lines
2
```

`cadastral` body mentions (no owner): `architecture-settlement-lexicon.md:95`, `japan-medieval-sengoku.md:157`.

### 6.3 Every "owns" anchor, quoted live

| Anchor | Live text (excerpt, `sed -n '<n>p'`) |
|---|---|
| `cosmology-cosmography.md:27` | "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." |
| `cosmology-cosmography.md:71` | "Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, not survey maps (§10)" |
| `cosmology-cosmography.md:102` | "…T-O diagrams are symbolic devices, not cartographic claims." |
| `cosmology-cosmography.md:133` | "A fictional map is a set of etymological arguments — hand the derivation table to naming-systems." |
| `sacred-topography-pilgrimage.md:5` | "…sacred-geography mapping (a culture's holy sites as a diagram: radial, quartered, linear-corridor, or archipelago)…" |
| `sacred-topography-pilgrimage.md:69` | "**The three route types.** (a) **Fixed itinerary** … (b) **Votive ramble** … (c) **Circuit / circumambulation**…" |
| `sacred-topography-pilgrimage.md:124` | "**Pick the route type** (§4: fixed itinerary, votive ramble, or circuit) and lay the stages." |
| `direction-symbolism.md:21` | "The direction register is the culture's mapping from a **small closed set of orientations**…" |
| `direction-symbolism.md:48` | "\| Relative (body) \| … \| written directions, letters, maps, instructions to absent readers \|" |
| `direction-symbolism.md:51` | "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic…" |
| `architecture-settlement-lexicon.md:95` | "…surveyed with the **groma** … The grid is cadastral: a state that *measures land* builds this city." |
| `architecture-settlement-lexicon.md:101` | "…give every planner culture an **instrument + founding rite + claim word**…" |
| `writing-media-surface-economy.md:3` | "…the seven surface families (clay and wax; stone and metal; papyrus and parchment; palm leaf, bark and cloth; bamboo and silk; paper; and the incidental surfaces…" |
| `writing-media-surface-economy.md:48` | "\| **palm leaf / bark / cloth** \| … \|" |
| `writing-media-surface-economy.md:73` | "\| 3 \| papyrus (coarse), paper (early), cloth \| the office and the merchant \| the account, the contract, the register, the ledger \|" |
| `writing-media-surface-economy.md:78` | "Cheapness widens the *base*, it does not redistribute the *authority*." |
| `mesoamerica-primary-sources.md:58` | "\| Lienzos and cartographic histories … \| Cloth maps/migration-conquest accounts \| … \| Originals often lost; the copy chain is the evidence…" |
| `transport-mobility-lexicon.md:28` | "**Craft rule**: a route is only real if someone maintains it." |
| `transport-mobility-lexicon.md:35` | "**Inca Qhapaq Ñan**: ~40,000 km … *tambos* at day intervals; *qullqas* for storage…" |
| `transport-mobility-lexicon.md:117` | "\| DR-TR-02 \| Require a maintenance clause … \|" |
| `agrarian-field-system-lexicon.md:42` | "\| PARCEL \| who holds the ground, by what right, owing what \| field names, boundary words, tenure words, land measures \|" |
| `agrarian-field-system-lexicon.md:45` | "\| CLAIM \| who takes a share of the harvest, and how it is enforced \| tithe/rent/tax words, storage words, status words (free/owing) \|" |
| `craft-artisan-lexicon.md:54` | "\| System \| Apprentice \| Journeyman \| Master \| Entry rite / mechanism \|" |
| `craft-artisan-lexicon.md:56` | "\| Germanic guild \| Lehrling (learner) \| **Geselle** … \| Meister \| the **Meisterstück** … \|" |
| `craft-artisan-lexicon.md:65` | "Design rule: pick a rung system and then break it deliberately…" |
| `craft-artisan-lexicon.md:44` | "\| Steel (Japan) \| **tamahagane** 玉鋼 …" — **steel grading, not the ladder** (r47 B4 confirmed) |
| `trade-economy-lexicon.md:17` | "Four natural sources…: **the body**, **the substance measured**…, **the action**…, and **the container/counting technology**…" |
| `trade-economy-lexicon.md:92` | "\| stock \| Exchequer tallies really were split into matching *stock* and *foil* halves (Clanchy 1993; Jenkinson 1924; OED s.v. *stock*…) \|" |
| `trade-economy-lexicon.md:121` | "**Split-object authentication** (named heuristic: the teeth of the contract): Greek *symbolon* … English chirograph and *indenture* … The cut object *is* the contract." |
| `celestial-symbolism-calendars.md:84` | "…the Polynesian **sidereal compass** … is a fully realized celestial *language of direction*…" |
| `sacred-kingship-mythic-charter.md:44` | "A mythic charter of rule is a story that answers four questions a polity cannot leave open…" |
| `sacred-kingship-mythic-charter.md:70` | "\| 8 \| **the regalia as found title-deed** \| title inheres in *objects*… \|" |
| `naming-systems.md:40` | "Onomastics splits by what is named: **anthroponymy** … **toponymy** …" |
| `naming-systems.md:70` | "Every renaming is datable; a map is an archive of coups." (verbatim — r47 B3 confirmed as a false accusation) |
| `naming-systems.md:97` | "\| Korea (Joseon) \| royal personal name avoided (국휘)… \|" |
| `divination-omen-systems.md` `map` hits | "The code maps to twelve prescriptions" (§9); "maps directly onto that gate's symbol-ledger row" (§13) — both verbs, 0 cartographic content |
| `polynesia-navigation.md:60` | "\| Horizon houses \| Thompson's Hawaiian star compass \| A mental bearing framework, not a chart showing the canoe's absolute position. \|" |
| `japan-medieval-sengoku.md:157` | "…a neat Edo cadastral map must not be treated as a direct Sengoku map." |

### 6.4 Couples-target existence (15/15)

```
$ for p in myth-symbol/cosmology-cosmography.md myth-symbol/sacred-topography-pilgrimage.md \
    myth-symbol/direction-symbolism.md culture-material/architecture-settlement-lexicon.md \
    culture-material/writing-media-surface-economy.md civilizations/mesoamerica-primary-sources.md \
    culture-material/transport-mobility-lexicon.md culture-material/agrarian-field-system-lexicon.md \
    culture-material/craft-artisan-lexicon.md culture-material/trade-economy-lexicon.md \
    myth-symbol/celestial-symbolism-calendars.md myth-symbol/sacred-kingship-mythic-charter.md \
    myth-symbol/divination-omen-systems.md civilizations/polynesia-navigation.md \
    linguistics/naming-systems.md; do test -f corpus/knowledge/$p && echo "OK $p" || echo "MISSING $p"; done
OK (15 lines, no MISSING)
```

Every row's target resolves as a file. Line counts for the neighbours (all read this pass): cosmology 155, sacred-topography 181, direction 202, architecture 149, writing-media 201, mesoamerica 176, transport 129, agrarian 179, craft 154, trade 166, celestial 175, sacred-kingship 203, divination 218, polynesia 210, naming 136.

### 6.5 Counts used in the fragment

```
writing-media map count: 0
divination map count: 2      # both the verb "maps", see 6.3
transport map count: 2       # a URL line and "source map" metaphor; no ownership
agrarian map count: 5        # "source map", "inheritance with a map", "underground-water map"; no ownership
```

No figure in this fragment is carried from r47 or the r44 seed; each was re-measured.

---

## 7. Handoff notes

- **To C01/C02 (entry/header drafters).** Insert §2's fenced block after the opening ownership paragraph; insert §3's gap sentence in the opening. Add the 13 filenames to `- couples:` once each (the table does not substitute for the field). Keep row 9's anchor at `:54-65`.
- **To C05 (length + contract).** The fragment is ~30 body lines. If the draft exceeds the discipline, apply the §4 cut order; rows 1–9 and 13 are load-bearing.
- **To C07 (boundary verifier).** The checks I expect: each "owns" cell resolves; no row claims a second owner; `divination` appears only as a non-collision note; `cosmology:27` is named in the gap sentence; `craft:44` does not appear as the ladder.
- **To A02 (one-owner, post-landing).** Cross-check the `- couples:` tokens against the neighbour entries; all 15 files named in this fragment (13 rows + 2 notes) exist at this baseline.
- **Open item (coordination, not evidence).** The section number "§1.2" is a placement suggestion. If C01's skeleton numbers the ownership section differently, C05/C07 should check the final number rather than cite this fragment's suggestion — that is the B5-class trap.

*Unknowns: none for in-corpus claims. No external source is cited in this fragment, so no `(to-verify)` marks are owed here; the entry's external shelf is C02/C08's surface.*
