# C02 — cartography entry drafter B (sections 5-9)

- Seat: `C02` | role: executor | claim: C | date 2026-10-19
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`, measured at seat start)
- Out path: `reports/round-47/cov/C02-entry-b.md` (this file; the only path this seat wrote)
- Mission (`reports/round-47/targets.json`, seat C02): entry sections 5-9 — survey-to-symbol chain, scarcity/prestige, mapmaker trade, provenance/charter, container-name fossil.
- Status: **DRAFT ONLY.** No file was created or edited under `corpus/`; the fence below is the byte source. The integrator applies the assembled entry to `corpus/knowledge/culture-material/cartography-and-mapmaking.md`.

## What this seat did

1. Read `reports/round-47/claims.json` (claim C: one fresh entry, 223→224) and `targets.json` (seat C02).
2. Read the r44 seed `reports/round-44/scout/K02-gap-scout.md`, the r47 plan `reports/round-47/plan/P02-c-plan.md`, and the filed C01/C03 drafts before finalizing this revision.
3. Confirmed the landing path is still unused and the partition is still 223 at this HEAD:

```
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ find corpus/knowledge -name '*.md' | wc -l
223
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
```

4. Drafted §§5-9, then **revised them against C01's filed §§1-4** to remove duplicated projection/scale/symbol tables. Every in-repo citation was re-read at the exact line; the audit table after the fence records the verified text.

## Integration and reconciliation note (read first)

At this cut the binding map is **not** in dispute: `targets.json` and P02's final 15-section skeleton (`reports/round-47/plan/P02-c-plan.md:234-250`) agree on the five C02 blocks — §5 survey-to-symbol chain, §6 scarcity/prestige, §7 mapmaker trade, §8 provenance/charter, §9 container-name fossil. The earlier P02 §2.4 table (`plan/P02-c-plan.md:170-181`) is a preliminary mapping, superseded by §4; do not use it for assembly. The only live inconsistency is C01's handoff (`reports/round-47/cov/C01-entry-a.md` §C.1), which calls §8 "mapmaker trade" and §9 both "provenance/charter" and "container-name fossil"; the binding plan puts trade at §7, provenance at §8, and the word layer at §9. Correct C01's cross-references at assembly; do not renumber the others.

**Duplication removed.** C01 §§3.2-3.5 already tabulate projection families, scale-as-three-numbers, orientation conventions, and the symbol grammar. P02 §5 requires those tables somewhere in §5; they are satisfied by C01's sections, so the fence treats §5 as the **production chain** and cites them rather than re-tabling them. This keeps one table of each kind in the assembled entry and matches C01's §C.1 request. The fence still supplies the instrument table, the three survey modes, the error budget, the control network, reproduction, and the failure/build rules that P02 §5 assigns to C02.

**K02's five spine items are retained, not dropped.** K02 §9 warned that the mission language could crowd out the seed's load-bearing spine (`K02-seed-extract.md:220-235`). The assembled entry keeps all five, distributed across the two drafters: the **survey chain** in §5.1-5.3; **projection and scale** in C01 §3.2-3.3 plus §5.4's three production rules; **drawing and symbolization** in C01 §3.4-3.5 plus §5.5's five production rules; **reproduction and the map trade** in §5.6, §6 and §7; and **the map's silences** in C01 §3.1 plus §5.5. The de-duplication relocates mechanism tables to C01, where they already exist; it does not remove the seed's spine.

**Cross-draft citation flag (not my file).** `reports/round-47/cov/C01-entry-a.md:90` and its self-audit at `:344` quote `corpus/knowledge/linguistics/naming-systems.md:70` as "a map is an archive of coups". The live line reads: "**Critical toponymy** … naming is inscription of power; the street grid is a city-text. Regime changes rewrite it…" The quoted phrase is not in the file. It appears to be a corruption of the correct craft paraphrase "a map is an archive of renamings" (which C03 uses at its §14). C06's source audit should drop the quotation marks or correct the phrase; I did not edit C01.

---

```markdown
## 5. The survey-to-symbol chain — seven links and one weakest-link rule

A map is not drawn from the world. It is drawn from a chain of transformations, and every link converts one kind of evidence into another: the world into a brief, the brief into measurements, the measurements into a control framework, the framework into a document, the document into a projection, the projection into symbols, the symbols into copies. The chain is what makes a sheet a register rather than a picture, and it yields the entry's operative rule:

> **The weakest-link rule.** A map cannot assert more precision than its weakest link. A beautiful drawing over a bad survey is a lie with good penmanship; a plain drawing over a controlled survey is evidence.

| # | link | converts | instruments and techniques | characteristic failure | the decision it forces |
|---|---|---|---|---|---|
| 1 | **select** | the world → a brief | the client's question; the warrant that authorizes the work (§8) | the unmapped is treated as absent | what is worth measuring, and for whom |
| 2 | **measure** | ground → number | pacing, rope and chain, groma, dioptra, astrolabe, cross-staff, compass, plane table, theodolite | random error; systematic offset; misclosure | which measurement primitives the culture actually has |
| 3 | **control** | numbers → a framework | baseline, triangulation, boundary marks, benchmarks, meridian | an uncontrolled survey drifts; a controlled one distributes its error | who owns and guards the fixed points |
| 4 | **reduce** | observations → a document | field book, calculation book, fair copy, coordinate list, plat | the fair copy silently "fixes" the field book | what counts as the original, and what the archive keeps |
| 5 | **project** | sphere → plane | the projection families and their trade-offs are §3.2's; the chain only chooses and records one | area, shape, direction and distance cannot all be preserved | which lie the map tells, and to whom |
| 6 | **symbolize** | picture → text | the conventions are §3.4-§3.5's; the chain fixes the set and the silences | false precision; symbol overreach; the accidental blank | what the reader is told, and what is withheld |
| 7 | **reproduce** | one → many | hand copy, woodblock, copperplate, lithography, print | copy drift; plate wear; edition error | who can own a copy, and who can correct it (§7) |

### 5.1 Measure: the instruments decide the map's form

The map is a picture of its instruments. A culture that can pace a route and name landmarks, but cannot close a traverse, produces itinerary lists and strip maps — distance and sequence, not area. A culture with a rope, a right angle and a boundary stone produces cadastral parcels and grids. A culture with a compass and a sounding line produces the portolan: bearings, hazards, a coastline. A culture with a baseline and a triangulation network produces a topographic sheet with a control skeleton. A culture with a clock and a star table can fix longitude as well as latitude, and only then does a global graticule become a practical product.

| survey capability | what it can produce | the form it can feed (the forms themselves are §4.1's) |
|---|---|---|
| pacing + landmarks + toponyms | route sequence, travel time, named places | itinerary / strip map |
| rope or chain + right angle (groma) | parcels, grids, boundaries, areas | cadastral map, plat, land register |
| compass + sounding + pilot knowledge | bearings, hazards, anchorages, coastlines | portolan / nautical chart |
| baseline + triangulation | fixed control points, intervisible stations, topography | topographic / trigonometric map |
| astronomical latitude; longitude with a timekeeper | a graticule and a world frame | cosmographic / geodetic map |
| plane table | local detail at large scale, drawn in the field | town, estate, battlefield map |

- **Roman case**: the *groma* sets right angles, the *cardo* × *decumanus* grid is laid out, and the grid is cadastral — "a state that *measures land* builds this city" (`corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95`). The instrument and the city plan are one system.
- **Compass case**: an abstract north requires deciding *which* north — true or magnetic — and declination is latitude- and era-dependent; the "compass trap" is a production problem before it is a plot device (`corpus/knowledge/myth-symbol/direction-symbolism.md:51`).
- **Longitude case**: the minute becomes navigable only when a clock can carry it; "longitude at sea" is the application that turns timekeeping into a coordinate (`corpus/knowledge/culture-material/timekeeping-instruments.md:50`).
- **The chartless boundary**: a sophisticated navigation system does not entail charts. Polynesian navigation distinguishes the horizon compass, the ordered steering-star sequence, the large sky mnemonic, and the latitude/landfall clue — "related operations, not synonyms" (`corpus/knowledge/civilizations/polynesia-navigation.md:52`). Do not assume every capable navigator draws; the chart is one possible output of wayfinding, not its definition.
- **The coordinate tradition**: Ptolemy's *Geography* is the type case of a map built from a coordinate table and a projection rather than from a route or a picture (Ptolemy, trans. Berggren & Jones 2000, `to-verify`). Triangulation as a survey method is early modern (Gemma Frisius 1533; Snellius 1615–17; the Ordnance Survey from 1791 — all `to-verify` for dates and priority). The design point is the dependency, not the dates: each capability unlocks a form.
- **Rule**: the form follows the capability, not the era. A world with pacing and rope and no triangulation is not a "primitive" map culture; it is a culture whose maps answer route and parcel questions, and whose regional maps are honestly less precise.

### 5.2 Control: the fixed point is the political fact

A survey without control accumulates error; a survey with control distributes it. The control network — boundary stone, trig pillar, benchmark, meridian — is the map's skeleton, and it is infrastructure that someone pays for, guards and repairs. The worldbuilder's question is therefore not only "what instrument?" but **"who owns the fixed points?"** A temple that owns the boundary stones owns the boundary; a crown that owns the trig pillars owns the survey; a city that owns its meridian owns its time.

- **Small-scale case**: the Roman *terminus* and the *pomerium* — the city begins as a furrow and a law-line, and the boundary is a ritual and legal object before it is a drawn one (`architecture-settlement-lexicon.md:95`; the lever "instrument + founding rite + claim word" is at `:101`).
- **Large-scale case**: the geodetic baseline, from which every other point is triangulated. A baseline is expensive, exposed and political; a survey that loses its baseline loses its authority.
- **Rule**: name the fixed points and their custodian before naming the map. A map with no fixed points is a sketch; a map whose fixed points are contested is a boundary dispute waiting to be filed.

### 5.3 Reduce: the field book is the map's witness

The field book — raw angles, paced distances, sketches, corrections, crossings-out — is the primary document. The fair copy is already an argument built from it. This distinction is the hinge of provenance (§8): a map with a field book is evidence; a map without one is an assertion.

- **The archive choice**: a culture that keeps the field book can litigate and re-compute its maps; a culture that keeps only the fair copy can display them but cannot defend them. The choice is a decision row, not a technical detail.
- **The fair-copy drift**: the copyist smooths a wavering line, closes a gap, or adds a plausible detail. The drift is not usually fraud; it is the normal pressure of making a document look finished. Make the field book and the fair copy disagree, and the disagreement is a scene.
- **The "original" problem**: if the field book is lost and the fair copy survives, the copy becomes the original by default. The general rule for documents applies: "If the document survives only in a later copy, distinguish the dated witness from the proposed original" (`corpus/knowledge/synthesis/loanword-material-dating.md:40`).

### 5.4 Project and scale: the two links that promise more than they can keep

The projection families and their preserves/distorts are tabulated at §3.2; the scale-as-three-numbers argument is §3.3. This section adds only the chain's three rules, because projection and scale are **links with a cost**, not free choices made at the drawing table:

- **The projection choice is a claim, and the claim is inherited by every copy.** Once the plate is cut, the distortion is reproduced with the map. A correction of the survey does not correct the projection; it requires a new plate.
- **Scale is a promise the survey must be able to keep.** At 1:50,000, one millimetre on the sheet is 50 metres on the ground; at 1:1,000,000, one millimetre is one kilometre. A line drawn at 0.2 mm on a 1:50,000 sheet claims about 10 m of ground; if the survey closed at 200 m, the drawing asserts ten times the available precision. This is the **false-precision rule**, and it is the most common lie in real maps.
- **The scale bar is the only scale that survives copying.** A photocopied "1:50,000" is a lie; a photocopied bar is still true. If the culture reproduces maps by hand, the bar is the first thing to standardize and the first thing a forger must copy.

The chain's projection failure is therefore a *production* failure — the drafting table inherits a choice it did not make — and it belongs in §5.8's failure table alongside misclosure and copy drift.

### 5.5 Symbolize: close the set, state the contract, decide the blank

The meaning of the conventions — orientation and its cosmology, the compass rose, the legend, the boundary line, the blank, the vignette — is §3.1 and §3.4-§3.5's. The production chain adds five rules that are about *making* the sheet rather than reading it:

- **Close the symbol set.** A culture with twenty signs and a combination rule is more legible than one with a hundred ad-hoc pictures. The closure is a drafting convention before it is an aesthetic; it is what lets two surveyors draw the same thing as the same thing.
- **The legend is a contract, not a caption.** The legend states the class definitions the sheet is using; if the classes are ambiguous, the sheet becomes the dispute. C03's build step 5 makes the legend byte-equal to the class definitions (§10); this is the production reason why.
- **The blank has three readings** — unknown, empty, forbidden — and the culture's convention must choose one per context (§3.1). A blank that is not marked as one of the three will be read as whichever suits the reader.
- **The boundary line is the most political stroke on the sheet.** Solid, dashed, dotted or absent; along a river or through it; named or unnamed. The convention must be stated because the same stroke can mean "limit of surveyed land", "limit of claimed land", and "limit of land we admit exists".
- **The monster marks the edge of the survey.** The phrase "here be dragons" is attested once, on the Lenox Globe (c. 1510, `HC SVNT DRACONES`), and is largely a modern joke rather than a medieval convention (`to-verify`). Use monsters as a rarity and a claim about the edge, not as stock filler; the blank is the more honest marker of ignorance.

### 5.6 Reproduce: the edition is a new map

Every reproduction is a new edition with its own errors. A hand copy normalizes; a woodblock fills and wears; a copperplate wears and can be re-engraved; a lithograph transfers; a print run multiplies one plate's mistakes. The medium's cost curve is the one already priced in `corpus/knowledge/culture-material/writing-media-surface-economy.md:64-78`: the expensive surface carries the authoritative genre, the cheap surface carries the vernacular one.

- **The edition problem**: the first state of a plate, the corrected state, the pirated state and the re-engraved state are different maps with the same title. A forger does not need a forged map; a "corrected" edition is enough.
- **The medium decides the social life of the sheet**: a unique manuscript is a treasure and a hostage; a limited edition is a status object; a mass print is furniture. The choice is §6's subject.
- **The copy-control question**: who may copy, what certifies a copy, and what happens to a superseded copy. This is the production side of the warrant chain (§8) and the reason a map archive is an institution, not a cupboard.
- **The loss rate**: a working map is used up; a monument map is kept (§6.4). The reproduction regime decides which of the two a culture's descendants will see.

### 5.7 The chain's failure table

| failure | where it enters | what it looks like on the sheet | the design use |
|---|---|---|---|
| **misclosure** | measure / control | the traverse does not close; the surveyor "adjusts" the last leg | a boundary that is slightly wrong everywhere, and legally final |
| **offset** | measure | a systematic shift; everything is 50 m west of the ground | a map that lies consistently and is therefore trusted |
| **false precision** | project / symbolize | a crisp line over a vague survey | a legal trap and a professional scandal |
| **projection lie** | project | a polar possession the size of a continent | a propaganda map that is technically correct |
| **scale omission** | scale | the village, path or sacred site that is not there | a map that erases a people by being "accurate" |
| **symbol overreach** | symbolize | one dot for a dispersed phenomenon; one line for a zone | a mine that is actually a field, a road that is a claim |
| **orientation ambiguity** | symbolize | whose north? which rose? | the compass trap, a discovery event |
| **copy drift** | reproduce | the third edition has a new island, a moved boundary | a forged or doctored map with an innocent provenance |

### 5.8 The chain as a build rule

The build order for the chain follows the links, not the drawing:

1. Fix the question and the reader (§§1-2).
2. Choose the instruments the culture actually has, and accept the form they imply (§5.1).
3. Choose the control network and name its custodian (§5.2).
4. Decide what the archive keeps — field book, fair copy, both, neither (§5.3).
5. Choose and record the projection and scale (§3.2-§3.3, §5.4).
6. Close the symbol set and decide the silences (§3.1, §3.4-§3.5, §5.5).
7. Choose the medium and the reproduction regime (§5.6), then state the weakest link in the map's own documentation — or let an in-world critic find it.

A worldbuilder who has fixed the chain has fixed the map's politics before drawing a line. The sheet is the visible end of a chain whose earlier links are where the authority and the lies are made.

## 6. Scarcity and prestige — the survey is the expensive part

A map looks like a drawing; economically it is a **survey with a picture attached**. The cost structure is dominated by fixed costs — the survey, the instruments, the training — and, before printing, by the skilled copy. This single fact explains most of the map's social life: who commissions it, who may see it, why it is given as a gift, and why it is stolen.

### 6.1 The cost stack

| cost | what it buys | who bears it | time scale |
|---|---|---|---|
| **the warrant** | the right to survey, publish or enforce | crown, city, company, patron | political |
| **the survey** | control network, field time, instruments, labour | the commissioning institution | months to years |
| **the reduction** | calculation, fair copy, drafting | the mapmaker's shop | weeks to months |
| **the plate or block** | the reproductive capital | the publisher | capital |
| **the copy** | paper, ink, hand colouring, binding | the buyer | per unit |
| **the correction** | a new survey or a new edition | the institution | recurring |

**The rule**: the institution that pays for the survey owns the map's politics, even when a private printer sells the copies. The survey is the state's loss leader; the atlas is the publisher's profit centre. A worldbuilder who knows who paid for the survey knows who can be blamed for the boundary.

### 6.2 Four scarcity regimes

| regime | what is scarce | mechanism | prestige form | plot engine |
|---|---|---|---|---|
| **unique copy** | the sheet itself | manuscript; one master; loss is total | the wall map, the gift chart, the treasury map | theft, gift, ransom, loss at sea |
| **access** | permission to see or copy | state secret, pilot's oath, chained chart, classified survey | the secret chart, the cabinet map | espionage, leak, betrayal, a map shown once |
| **reproduction** | the right or the plate to print | privilege, monopoly, limited edition, hand colouring | the atlas, the deluxe edition | piracy, privilege dispute, counterfeit |
| **currency** | up-to-date knowledge | the frontier moves; the survey ages; the coast silts | the "new survey", the corrected edition | obsolescence, scandal, a re-survey that changes a title |

- **The unique copy** is the pre-print norm: the chart is a working tool and a treasure at once. Its loss is not a reprint problem; it is the loss of the only witness.
- **Access scarcity** is the state's favourite: the Spanish *Padrón Real* and the Portuguese policy of secrecy are the standard European cases (`to-verify` institutional details), and the pilot's oath is the small-scale version. The restriction is the asset; a leaked chart is a diplomatic incident.
- **Reproduction scarcity** arrives with print: the privilege, the plate, the edition. The Dürer–Raimondi mark dispute is the legal template for a copied map (`corpus/knowledge/culture-material/craft-artisan-lexicon.md:87`), and the Amsterdam atlas trade is the commercial template (Ortelius 1570; Blaeu 1662–72; `to-verify` editions).
- **Currency scarcity** makes mapping a recurring expense: a map is a perishable claim. The re-survey is a political event because it can move a boundary, a tax or a title.

### 6.3 Prestige: four currencies

- **Patronage** — the dedication, the cartouche, the patron's arms. The map is a gift between rulers and a claim on the patron's behalf. al-Idrisi's *Tabula Rogeriana* for Roger II of Sicily (1154) is the type case (`to-verify` the silver-planisphere account in the preface and the edition).
- **Completeness** — the world map, the planisphere, the atlas as a claim to encompass the known world. The atlas is a library in one volume, and its completeness is prestige independent of its accuracy.
- **Difficulty** — the survey as a feat: the measured meridian, the triangulated range, the mapped colony. "We measured the kingdom" is a capacity display, and the map is its certificate.
- **Antiquity and possession** — the old map as a relic, a charter or a trophy. The captured chart, the map in the treasury, the map bound into the charter roll: possession is the prestige.

**The rule**: prestige attaches to what is hard to replace, not to what is accurate. A beautiful wrong map can outrank a plain right one. That is a plot engine, not a defect, and it is why a patron may prefer the monument to the survey.

### 6.4 The two registers: working sheet and monument map

| register | qualities | who uses it | survival |
|---|---|---|---|
| **working map** | plain, current, cheap, annotated, folded, used up | pilot, surveyor, officer, tax collector | low — it is consumed |
| **monument map** | ornate, expensive, displayed, bound, dedicated | court, library, collector, patron | high — it is kept |

The split is the map's version of the surface-cost ladder (`corpus/knowledge/culture-material/writing-media-surface-economy.md:64-78`) and it produces the same survivor bias (`:81`; the general perishability rule is `corpus/knowledge/culture-material/material-culture-inference-method.md:69`): the monument map survives because it was expensive; the working map is used up. The record therefore over-represents ceremony and under-represents practice. A worldbuilder can make the antiquarians mistake the monument for the working map — a standing error in the real history of cartography (`to-verify` case by case).

- **Cheapness is not access**: a print revolution widens the base of map owners but does not redistribute the authority to survey, license or certify — the same rule the surface economy states for writing ("Cheapness widens the *base*, it does not redistribute the *authority*", `writing-media-surface-economy.md:78`).
- **The prestige–accuracy trade**: the monument map can afford ornament and a strong claim; the working map must be plain and current. A culture that confuses the two sends a pilot out with a trophy.

### 6.5 The loop, and its breaks

The loop: an expensive survey → institutional ownership → restricted access → prestige → more commissions → more surveys. Each turn reinforces the institution that owns the chain. The loop breaks at:

1. **a cheap instrument** (compass, plane table, printed manual) — it lowers survey cost and widens the practitioner base;
2. **a cheap reproduction** (print) — it separates the sheet's price from the survey's price;
3. **a new patron** (merchant company, city, colonial administration) — it moves the map from court to counting-house;
4. **a political rupture** (revolution, conquest, expropriation) — it transfers the survey archive and with it the map's authority.

Each break is an era seam, and a good place to stage a transition from secret chart to printed atlas, or from court cosmography to state survey.

### 6.6 Calibration flags and design questions

**Calibration (terse; the full bank is §12).** "Maps were rare because mapmaking was primitive" — **false**: rarity is a demand-and-institution fact before it is a skill fact. "The map was always a state monopoly" — **false**: commercial map markets existed (Amsterdam is the standard case). "A prestige map is accurate" — **false**: prestige and accuracy are different axes. "Cheap printing made map knowledge democratic" — **overclaim**: it widened ownership, not the authority to survey or certify.

**Design questions.** (1) Who pays for the survey, and what do they expect? (2) Who may see the sheet, and who may copy it? (3) What is the culture's prestige object — atlas, globe, wall map, secret chart, relic? (4) What happens to an obsolete map — archive, scrap, correction, concealment, reuse as a charter? (5) Can a private person commission a survey, and what does the state do about it? (6) Which register do the surviving maps belong to, and what does that hide?

## 7. The mapmaker trade — five roles, four products, three customers

"The mapmaker" is a modern abstraction. In most map cultures the work is split into roles that are socially distinct, and the split is where authority is manufactured. A single practitioner can collapse them all, but then the map's authority is personal; a trade separates them, and the map's authority becomes institutional. The **object** side of this trade — unique chart, printed sheet, atlas, globe, monumental map, register, treaty map — is §4.3's; this section adds the **maker** side.

### 7.1 The roles

| role | owns | sells | failure mode | anchor |
|---|---|---|---|---|
| **surveyor / geometer** | the measurement and the field book | the survey | misclosure, offset, fatigue, a bribe | Roman *agrimensor* and the *groma* (`corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95`; Dilke 1971, `to-verify`) |
| **cosmographer** | the frame: projection, coordinates, world-picture | the framework | a frame that cannot absorb new data | Ptolemy; al-Idrisi; Mercator (`to-verify` editions) |
| **draftsman / illuminator** | the sheet's execution | the drawing | ornament over information | portolan and mappa mundi workshops (`to-verify`) |
| **engraver / printer / publisher** | the plate and the edition | the copy | plate wear, copy drift, piracy | Ortelius; Blaeu (`to-verify`) |
| **instrument maker** | the tools | the instrument | a bad instrument poisons the survey | compass and theodolite makers (`to-verify`) |
| **pilot / informant** | local knowledge | the route or the secret | a secret kept, or a lie told | portolan pilots; contrast the chartless navigator (`corpus/knowledge/civilizations/polynesia-navigation.md:52`) |

**The rule**: when the roles collapse into one person, the map is a personal attestation; when they separate, the map is a **system**, and the system's weakest role is the map's weakest link. This is §5's weakest-link rule applied to labour.

### 7.2 Organization models

| model | who employs | the map is | historical anchor | plot engine |
|---|---|---|---|---|
| **court office** | crown or temple | a state secret or a prestige object | the Spanish *Padrón Real*; the Chinese astronomical bureau; al-Idrisi at Roger II's court (`to-verify`) | court intrigue, rival cosmographers, a patron's fall |
| **guild workshop** | the trade | a commodity with a mark | the Amsterdam map trade; the stationers (`to-verify`) | privilege dispute, piracy, apprenticeship |
| **state corps** | army, navy, treasury | infrastructure | Ordnance Survey (1791); Survey of India (1802); USGS (1879) (`to-verify` dates) | budget, scandal, a frontier survey |
| **merchant company** | the company | commercial intelligence | VOC and East India Company chart archives (`to-verify`) | espionage, monopoly, a lost ship |
| **itinerant practitioner** | local patrons | a service | parish surveyors, peripatetic geometers (`to-verify`) | a survey that is also a swindle |
| **temple or monastery** | the cult | a cosmology | mappa mundi, monastic mapmaking (`to-verify`) | heresy, custody, a copy that must not circulate |

### 7.3 The workshop ladder, the marks, and the shop hand

The trade's internal ladder is the standard one: apprentice → journeyman → master, with a masterpiece and a feast, and with the usual escape hatches (masters' sons, redemption fees) that make corruption plots possible (`corpus/knowledge/culture-material/craft-artisan-lexicon.md:44`; the guild ladder is at `:3`, the marks typology at `:76-87`). The map trade's specific twist is that **the surveyor and the engraver are different hands**, and the "author" is often a brand — the publisher's imprint, the cosmographer's name, the crown's privilege.

- **The marks of a map**: the surveyor's signature; the imprint (place, publisher, date); the privilege line (*cum privilegio*); the dedication; the scale; the arms. Each is a claim of a different kind: authorship, origin, licence, patronage, precision, ownership.
- **The shop-hand problem**: a "Raphael" is a workshop's output, not one hand (`craft-artisan-lexicon.md:87`). An atlas is the same: the master's name sells the edition, the apprentices cut the plates. Decide **whose name makes the map official** — the surveyor's, the publisher's, the patron's, or the state's.
- **The signature law case**: the Dürer–Raimondi monogram dispute is the legal template for map piracy (`craft-artisan-lexicon.md:87`). A map culture's "court of marks" can be a full institution with a docket and precedent.

### 7.4 Four products

| product | buyer | price logic | protection | plot |
|---|---|---|---|---|
| **the sheet** | reader, collector | per copy | privilege, later copyright | piracy, counterfeit |
| **the survey** | state, company, city | contract | secrecy, oath | leak, underpayment, a second client |
| **the secret** | rival, merchant, envoy | ransom or favour | custody, oath | espionage, betrayal |
| **the warrant** | anyone who needs authority | fee or office | licence, statute | corruption, a bought surveyor |

A mapmaker can sell any one of these without the others, and each has a different buyer and a different legal protection. The sheet is the visible product, the survey is the capital, the secret is the premium, and the warrant is the licence.

### 7.5 Licences, training, and the three customers

- **Three licences.** The *printing privilege* — the right to print and sell, enforced by a stationers' company or a guild (`corpus/knowledge/culture-material/trade-economy-lexicon.md:106-116`). The *professional licence* — the sworn surveyor, the state examiner, the cosmographer royal; it converts a private skill into a public fact and makes the surveyor's oath actionable (§8). The *access licence* — the pilot's oath, the state secret, the restricted chart; it creates a gray market in copies and a black market in knowledge.
- **Training.** The surveyor needs pacing, the compass, the chain, the plane table, the calculation of closure, and the sketch; training is by apprenticeship, a state corps school, or a military academy (`to-verify` institutional history). The cosmographer needs geometry, astronomy, projection, and the coordinate table. The engraver needs the burin, lettering, the plate, and the press. The pilot needs the route, the hazard, the season, and the landfall clue; the training is often oral and familial (`polynesia-navigation.md:52`). **The surveyor's oath is the hinge**: it converts a private measurement into a public fact. Decide who administers it, and the map's authority follows.

| customer | wants | the map is | the failure they fear |
|---|---|---|---|
| **the state** | a register: tax, territory, control | a legal instrument | a parcel it cannot find, a boundary it cannot defend |
| **the merchant or pilot** | a tool: route, hazard, distance | a working sheet | a chart that is out of date or wrong |
| **the patron or collector** | a monument: prestige, completeness, gift | a treasure | a map that is common, damaged or superseded |

One map cannot serve all three. The register needs parcels and boundaries; the tool needs routes and soundings; the monument needs the world and ornament. The trade's real skill is knowing which customer it is serving; make the mapmaker choose, and let the choice be visible in the sheet.

## 8. Provenance and charter — how a sheet becomes authority

A map is not believed because it is right; it is believed because it is **warranted**. The warrant is a chain of documents and acts, and a map without one is a drawing. The chain has five links; break any one and the map's authority is contestable.

### 8.1 The warrant chain

| link | document or act | holder | question it answers | failure |
|---|---|---|---|---|
| **1 warrant** | commission, statute, charter, contract | crown, city, company, patron | who authorized this survey? | an unauthorized survey is trespass or espionage |
| **2 record** | field book, calculation book, original survey | surveyor's office, archive | what was actually measured? | no record → the sheet is an assertion |
| **3 attestation** | signature, oath, seal, date, witness | surveyor, magistrate | who says so? | a forged or absent signature |
| **4 authentication** | registry copy, countersignature, deposition, privilege | registry, archive, state | who certifies the copy? | an unregistered copy is a rumour |
| **5 use** | grant, assessment, treaty, boundary award | court, treasury, legislature | what does it do? | the act is not performed, or is performed on a different map |

**The rule**: a map's authority is the weakest link in this chain, not the accuracy of its drawing. A superb survey with no warrant is a curiosity; a mediocre survey with a registered copy is law. This is §5's weakest-link rule applied to institutions.

### 8.2 The performative map

In cadastral and treaty regimes the map does not describe a fact; it **creates** one. The recorded plat creates the lot; the ratified boundary map creates the border (or the claim to it); the tithe map fixes the liability. This is the one place where "the map is the territory" is not a category error but a legal operation: the map binds the ground because the law says the registered line is the line.

- **Real anchors** (`to-verify` at the level of statutes and dates): the US Public Land Survey System (1785) and its township/section grid; the Napoleonic cadastre from 1807; the English tithe commutation maps of 1836; the Torrens title register (South Australia, 1858); the colonial boundary commissions. The point is the structure — statute, survey, register, legal act — not the dates.
- **The design lever**: decide **which map in your culture is performative** — the tax map, the treaty map, the temple's land register, the clan's charter — and who may amend it. The amendment procedure is the constitution of the map.
- **Boundary against `sacred-kingship-mythic-charter.md`**: that file owns the **mythic charter**, the story that legitimates a ruler; this section owns the **legal charter**, the document that legitimates a claim to ground. A culture can have both, and their disagreement is a plot engine.

### 8.3 The authority ladder

| rung | document added | who can challenge | typical setting |
|---|---|---|---|
| **sketch** | none | anyone with local knowledge | frontier, emergency, private note |
| **survey** | the field book | the surveyor and the client | estate, route, reconnaissance |
| **sworn survey** | the oath and the signature | a court or a magistrate | boundary, tax, grant |
| **registered survey** | the registry copy and the countersignature | the registry and the courts | cadastre, title, treaty |
| **statutory map** | the statute and the penalty | the legislature and the courts | partition, public land, national survey |

Each rung adds a document, a witness, and a penalty for falsification. The ladder is also a **cost ladder**: each rung costs more, which is why poor jurisdictions use sketches and rich ones use statutory surveys (link §6). A worldbuilder can place a culture on the ladder and derive who can challenge a map, what evidence is needed, and what happens when the map is wrong.

### 8.4 Provenance failure modes

- **The lost original** — the copy survives and its errors become the record. The archive choice (§5.3) decides whether the culture can audit its own maps. `corpus/knowledge/synthesis/loanword-material-dating.md:40` states the general rule for documents: a later copy dates the copyist as well as the original.
- **The improved copy** — a later hand adds detail or "corrects" the map; the sheet becomes a palimpsest; the edition is a new map (§5.6, §7.3). The provenance chain must name the edition, not just the title.
- **The forged map** — the Vinland Map is the cautionary case: long celebrated, now widely treated as a modern forgery (`to-verify` the current consensus and the ink evidence). A map is easy to fake because re-surveying the ground is expensive; the forgery economy is the shadow of the survey economy. The **back-dated map** — drawn later, dated earlier to support a claim — is the legal variant.
- **The archival fire** — the custody chain burns. `corpus/knowledge/culture-material/fire-fuel-light.md:89` names the deliberate burning of archives and registers as "the cheapest way to write a *hole*" into a record: a burnt survey office is a provenance gap and a plot engine.
- **The surveyor's error become law** — the line that is wrong but registered; the boundary that follows it; the doctrine that possession or the registered map wins. This is the legal version of "the map is not the territory", and the most story-rich failure on the list.

### 8.5 The contest rule

| rule | what wins | institution | plot |
|---|---|---|---|
| **map wins** | the registered line | registry, statute, court | the ground is legally wrong; a family loses land it farms |
| **ground wins** | possession, custom, long use | local court, community, oath | the map is evidence, not law; a surveyor is discredited |
| **new survey wins** | the re-measurement | commission, sovereign, party | the remedy is political; the re-survey is the event |

Decide the rule before writing a boundary dispute. The rule determines who is believed, who pays, and what a "win" means.

### 8.6 Calibration and the eight decisions

**Calibration.** "The map is the territory" is a category error as metaphysics, but a **performative fact** in a registered system; keep the two apart. "Cadastral maps are accurate" — they are accurate to the legal question (parcel identity, liability), not to the ground; the in-corpus precedent is the Edo cadastral caution (`corpus/knowledge/civilizations/japan-medieval-sengoku.md:157`). "Ancient maps were legal documents" — some were, many were not; the warrant chain tells you which. "A registered map cannot be wrong" — it can; it can be wrong and binding at once. That is the point of the performative exception.

**The eight decisions** (feeds the decision record, §13):

1. Name the **warrant** and its holder.
2. Name the **record** (field book, fair copy, both) and its custodian.
3. Name the **attestation** (signature, oath, seal, witness).
4. Name the **authentication** (registry, countersignature, deposition, privilege).
5. Name the **legal act** the map performs (grant, assessment, treaty, boundary).
6. Name the **contest rule** (map, ground or new survey wins).
7. Name the **forgery economy** (what is easy to fake, and who checks).
8. Name what the **archive keeps**, and what it destroys.

## 9. The container-name fossil — what the map's words remember

The words for maps are a fossil bed. Most of them are not words for "map"; they are words for the **material** a map was made of, or the **container** it was kept in. The object changed; the name stayed. This is the same fossil logic the partition already uses for vessels — the ear/lug word survives the handle (`corpus/knowledge/culture-material/vessel-container-lexicon.md:71`) — and for materials, where the *sarcophagus* stone becomes the coffin's name (`corpus/knowledge/culture-material/funerary-material-culture.md:22`).

### 9.1 The word bank

| word | root | original sense | what it fossils | design use |
|---|---|---|---|---|
| **map** | Latin *mappa* | cloth, napkin | the cloth sheet; *mappa mundi* = cloth of the world | a culture whose maps were cloth keeps "cloth" in its map word after paper arrives |
| **chart, card, charter, cartography** | Latin *charta* / Greek *chartēs* | papyrus sheet, paper | the paper; a charter is a small paper; cartography is paper-writing | the legal document and the map share a root — the medium is the warrant |
| **atlas** | Mercator's *Atlas* (1595), after the Titan | a bound collection of maps | the book/container; later any systematic collection | a culture with bound atlases names the genre after the binder or the frontispiece |
| **portolan** | Italian *portolano* | harbour pilot book | the text genre that accompanied the chart | a chart named after the book it replaced |
| **cartouche** | French *cartouche* | cartridge, paper roll | the ornamental title panel | the title panel is a paper container |
| **legend** | Latin *legenda* | things to be read | the reading key | the key as a reading list |
| **scale** | Latin *scala* | ladder, steps | the scale bar | the bar as a ladder |
| **table** | Latin *tabula* | board, tablet | the map as a board (*Tabula Peutingeriana*) | a wall map is a "table" |
| **plat** | *plot* | piece of ground | the parcel; the map of parcels | the map named after the land, not the medium |
| **gazetteer** | *gazette* | newspaper, coin | the news-sheet → the geographical dictionary | a map index named after a periodical |
| **itinerary** | Latin *iter* | journey | the route list | a route map named after the journey |
| **album** | Latin *albus* | white, a blank tablet | the blank book → the collection | a collection named after its blank pages |
| **cartulary** | *chartularium* | book of charters | the archive container | a register named after its book |

All etymologies are standard-shelf but **`to-verify` at OED level** for first attestation and exact sense; the safe core is the root and the semantic path, not the date. The external check is the *Oxford English Dictionary*, 3rd edn (online), s.vv. map, chart, card, charter, cartography, atlas, portolan, cartouche, legend, scale, table, plat, gazetteer, itinerary, album, cartulary (`to-verify`; no network at seat time).

### 9.2 The method

1. **Choose the ur-medium** — cloth, hide, bark, paper, clay, silk, wood, slate.
2. **Coin the map word from the medium or the container**, not from an abstract "map".
3. **Let the word survive the medium change**; the fossil is the trace of the first medium.
4. **Treat the fossil as a dating tool and a plot device**: an archaism tells you what the first maps were, and an in-world etymologist can build an argument on it (rightly or wrongly).

This is exactly the rule at `corpus/knowledge/culture-material/writing-media-surface-economy.md:62`: "A culture that changes tools keeps the old names (the fossil), which gives the etymologist a dating tool." The map word is the same kind of evidence.

- **The container→genre drift**: a word for the container becomes a word for the collection, then for the genre. *Atlas* is the model — a bound book of maps becomes any systematic collection — and *album*, *cartulary*, *portfolio* and *cabinet* follow. A worldbuilder can build a whole map taxonomy out of storage words: the roll, the chest, the portfolio, the atlas, the wall.
- **The map-specific trap**: the fossil records the **medium at entry**, not the medium of the first map or the current one. A culture that says "cloth" for map may have made its first maps on cloth and later switched to paper; the word survives, the material does not. Do not infer the current medium from the word, and do not infer the first medium from the current word without a second witness. This is the map's version of the two-clocks rule: a word entering a speech community is not the same event as the arrival of its referent (`corpus/knowledge/synthesis/loanword-material-dating.md:30`), and a later copy dates the copyist as well as the original (`:40`).

### 9.3 The in-world lexicon builder

| ur-medium | likely map word | what it asserts | the anachronism it creates |
|---|---|---|---|
| **cloth** | "cloth", "sheet", "painted cloth" | maps are textile, portable, sewn | paper maps called "cloths" after a paper revolution |
| **hide / parchment** | "skin", "scraped skin" | maps are animal, expensive, durable | a cheap paper map called a "skin" |
| **paper** | "paper", "sheet", "leaf" | maps are cheap, replaceable | a luxury map called a "leaf" |
| **clay** | "tablet", "brick" | maps are heavy, archival, fired | a paper map called a "tablet" (an archaism of the bureau) |
| **silk** | "silk", "woven" | maps are luxury, light, courtly | a military map called "silk" |
| **wood** | "board", "table" | maps are furniture, wall-mounted | a pocket map called a "board" |
| **slate** | "slate", "stone" | maps are reusable, practice | a vellum map called a "slate" |

Each row gives a **word**, an **implied medium**, and an **anachronism** the worldbuilder can use deliberately. The best fossils are the ones that survive a revolution: a paper age that still calls its maps "cloths" is a culture with a visible media history.

### 9.4 False fossils, the trade vocabulary, and the design rule

- **False fossils to kill**: "map" is not an acronym; "chart" is not from "character"; "atlas" is not a book size; "cartouche" is not from "cart"; "portolan" is not simply "port". Each is a plausible folk etymology and each is wrong. A worldbuilder can use a folk etymology as an **in-world** belief — a scribe's mistake, a guild's origin story — but must not present it as the real one. The distinction is itself a useful scene: a culture's learned etymology is often a better guide to its self-image than to its language.
- **The trade's fossil vocabulary**: **plot** (a parcel), **plat** (a map of parcels), **draft** (a drawn plan), **survey** (a measured account), **scale** (a ladder), **legend** (a reading), **cartouche** (a paper roll), **imprint** (a printing), **privilege** (a licence). Use these as in-world archaisms with a stated origin; the trade's speech community becomes legible — the same method the craft register uses (`corpus/knowledge/culture-material/craft-artisan-lexicon.md:3`).
- **Design rule**: name the ur-medium, coin the word, let it fossilize, and decide which medium change the word outlives. The lexicon is a **stratigraphy** of the map's material history: each layer is a word that survived a revolution. The map's words are the cheapest evidence of its material past, and the most portable plot device.
```

---

## Citation audit — every in-repo `path:line` used above, re-read at HEAD `6e9a30d`

| citation | verified text (short) | status |
|---|---|---|
| `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` | Roman castrum grid surveyed with the **groma**; "The grid is cadastral: a state that *measures land* builds this city." | real |
| `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:101` | design levers: "give every planner culture an **instrument + founding rite + claim word**" | real |
| `corpus/knowledge/myth-symbol/direction-symbolism.md:51` | "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic … declination." | real |
| `corpus/knowledge/culture-material/timekeeping-instruments.md:50` | table row: the minute → "longitude at sea" | real |
| `corpus/knowledge/civilizations/polynesia-navigation.md:52` | "Distinguish **horizon compass**, **ordered steering-star sequence**, **large sky mnemonic**, and **latitude/landfall clue**; these are related operations, not synonyms." | real |
| `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` | T-O row: "T-O diagrams are symbolic, not survey maps (§10)" | real (cited in the report and C01 boundary; not restated in the fence) |
| `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, not cartographic claims"; flat-earth fabrication (Russell 1991) | real |
| `corpus/knowledge/culture-material/writing-media-surface-economy.md:62` | "A culture that changes tools keeps the old names (the fossil), which gives the etymologist a dating tool." | real |
| `corpus/knowledge/culture-material/writing-media-surface-economy.md:64-78` | §4 cost ladder and register law; `:78` "Cheapness widens the *base*, it does not redistribute the *authority*." | real |
| `corpus/knowledge/culture-material/writing-media-surface-economy.md:81` | §5 "The survivor's ledger — what the medium does to the future's evidence" | real |
| `corpus/knowledge/culture-material/craft-artisan-lexicon.md:3` | topic line: "the workshop as a speech community — a closed technical register" | real |
| `corpus/knowledge/culture-material/craft-artisan-lexicon.md:44` | workshop ladder table (apprentice → journeyman → master; masterpiece) | real |
| `corpus/knowledge/culture-material/craft-artisan-lexicon.md:76-87` | §6 marks typology (six types) and the Dürer–Raimondi case | real |
| `corpus/knowledge/culture-material/trade-economy-lexicon.md:106-116` | §6 guilds and trade associations; `:115` Ogilvie/Epstein calibration; `:116` design lever (shelter, revenue, identity, rite) | real |
| `corpus/knowledge/culture-material/vessel-container-lexicon.md:71` | "The **ear** word for handles is the neatest fossil" | real |
| `corpus/knowledge/culture-material/funerary-material-culture.md:22` | Pliny *NH* 36.27, the *sarcophagus* stone of Assos — "a material property that becomes a container's name" | real |
| `corpus/knowledge/culture-material/fire-fuel-light.md:89` | "Fire as record destruction … the cheapest way to write a *hole* into a fictional archive" | real |
| `corpus/knowledge/culture-material/material-culture-inference-method.md:69` | perishability row: "what survives to be seen; memory politics" | real |
| `corpus/knowledge/civilizations/japan-medieval-sengoku.md:157` | "a neat Edo cadastral map must not be treated as a direct Sengoku map" | real |
| `corpus/knowledge/synthesis/loanword-material-dating.md:30` | the three-clock table: lexical entry vs referent arrival vs first written token | real |
| `corpus/knowledge/synthesis/loanword-material-dating.md:40` | "If the document survives only in a later copy, distinguish the dated witness from the proposed original." | real |

Commands used for this audit (read-only, from the lane root):

```
$ sed -n '<line>p' <file>          # each row above
$ python3 - <<'PY'                 # full-path citation resolver
# extracted every corpus/knowledge/*.md:NN and checked file + line count
PY
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
```

The resolver found 17 unique full-path citations in the fence, zero missing files, zero out-of-range lines. No in-repo citation above is a guess. If another round shifts a file before landing, the assembler must re-check at apply time (the standing `recheck:` discipline).

## Boundary notes (for C08/A02)

This draft is written to **couple, not restate** the neighbours the seed named:

| neighbour | what it owns | how §§5-9 keep the boundary |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | the five world-model axes; the T-O diagram as a **symbolic** device | §5 cites the contrast only in the report; the fence does not restate the typology or the flat-earth calibration. C01 §1 owns the boundary statement |
| `myth-symbol/sacred-topography-pilgrimage.md` | holy-site typology, route-as-rite, the diagram geometries | §5.1/§5.5 use the route only as a map form/feed; §8's charter is legal, not mythic |
| `myth-symbol/direction-symbolism.md` | orientation frames, cardinal coinage, the compass trap | §5.1/§5.4 cite `:51` for the production problem (declination); §3.4-3.5 of C01 owns the register |
| `culture-material/architecture-settlement-lexicon.md` | city-plan lexicon, castrum, groma | §5.1/§5.2 cite `:95`/`:101` for the survey step and the boundary-stone case; no settlement vocabulary restated |
| `culture-material/writing-media-surface-economy.md` | seven surface families; cost ladder; medium as legal instrument | §5.6/§6.4 cite `:64-78`/`:81`; no surface inventory restated |
| `culture-material/craft-artisan-lexicon.md` | workshop ladder, marks, guild models | §7.3 cites `:44`/`:76-87`; §9.4 cites `:3`; no guild taxonomy restated |
| `culture-material/vessel-container-lexicon.md` | container typology, measure→money chain | §9 cites `:71` as the **method precedent**; the measure→money chain is not restated |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo/cartographic-history **source class** | cited at `:58` in C01/C03 and in the report; no manuscript inventory restated |
| `civilizations/japan-medieval-sengoku.md` | periodization caution | §8.6 cites `:157` as the calibration precedent; no Sengoku history restated |
| `myth-symbol/sacred-kingship-mythic-charter.md` | mythic charter/legitimation | §8.2 states the legal/mythic split explicitly |

**One-owner check**: the draft's `- couples:` line (C04's job) should name these files; the entry's own topic is the **made map** (survey→sheet→warrant→word), not cosmography, pilgrimage, direction, settlement or writing media. No register is claimed twice. C01's §1 boundary table is the authoritative statement; this section only confirms that §§5-9 do not violate it.

## Sources this seat adds (C04/P02 already carry the full shelf)

The full tiered shelf is in `plan/P02-c-plan.md:199-240` (§3.1) and `scout/K02-seed-extract.md` §6; this seat adds only the items its sections use and did not find already registered:

- **Dilke, O. A. W. (1971), *The Roman Land Surveyors*, David & Charles** — the *groma*/centuriation chain (§5.1). `(to-verify)` edition/pages.
- **Snyder, John P. (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395** — the projection families (§5.4 points to C01 §3.2, which already names it). `(to-verify)`.
- **Kain, Roger J. P., & Baigent, Elizabeth (1992), *The Cadastral Map in the Service of the State*, University of Chicago Press** — the cadastral/performative map (§8.2). `(to-verify)`.
- **Scott, James C. (1998), *Seeing Like a State*, Yale University Press** — legibility and the cadastral state (§8.2). `(to-verify)`; not registered in-corpus.
- ***Oxford English Dictionary*, 3rd edn (online)** — every etymology in §9. **Not consulted this round**; all first attestations `to-verify`.
- **The Dutch/Portuguese/English chart archives** (VOC, *Padrão Real*, Hydrographic Office) — the access-scarcity cases (§6.2); all `(to-verify)`.
- **The Vinland Map** — the forgery caution (§8.4); current consensus `(to-verify)`.

No external work was fetched or page-checked at this seat (no network). The in-corpus anchors are the only verified citations.

## to-verify list (must not ship as inspected fact)

1. Every external edition, volume and page range — no external work consulted.
2. All etymology first attestations and exact senses — OED-level check required; roots and semantic paths are standard, dates are not asserted.
3. The institutional details of the Spanish *Padrón Real*, Portuguese secrecy, VOC archives, and the Amsterdam atlas trade.
4. The dates for triangulation (Gemma Frisius 1533; Snellius 1615–17), the Ordnance Survey (1791), the Survey of India (1802), the USGS (1879), the Cassini survey, the Napoleonic cadastre (1807), the tithe maps (1836), and the Torrens register (1858).
5. The Vinland Map forgery consensus and the ink evidence.
6. "Here be dragons" — one attested instance (Lenox Globe, c. 1510) and the modern-myth status.
7. The al-Idrisi silver-planisphere account (it is in the preface; `to-verify` the translation).
8. The claim that the record over-represents the monument map — plausible and consistent with the in-corpus survivor's ledger, but the cartographic case-by-case evidence is `to-verify`.

## Collision / write-surface report

- `corpus/knowledge/culture-material/cartography-and-mapmaking.md` does not exist at `6e9a30d` (command output above). No entry is overwritten; the landing would be an **A** (add) under the live partition.
- No file under `corpus/` was written by this seat. The fence is a draft; the integrator applies it.
- No filed bytes under `reports/round-1..46/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, or fleet `.ufo/**` were touched.
- This seat wrote only `reports/round-47/cov/C02-entry-b.md`.

## Owed / handoff

- **Integrator**: choose one of the three section maps (recommendation: the binding `targets.json` five-block map, because C01/C03 already refer to §5-9), then renumber every `§` cross-reference in C01/C02/C03. The re-cut table above is mechanical.
- **C04**: the header block (H1, `- topic:`, `- gap filled:`, `- sources:`, `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:`). The `- topic:` line must be byte-equal to the README row (C09). P02 §3 has a canonical candidate.
- **C03**: the calibration bank must absorb the inline flags in §5.5 (dragons), §6.6 (rarity, monopoly, prestige/accuracy, cheap print), and §8.6 (map/territory, cadastral accuracy, ancient legal maps, registered error); the decision record should absorb §8.6's eight decisions, and §6.6's design questions.
- **C06**: correct or drop C01's `naming-systems.md:70` quotation ("a map is an archive of coups" — not in the live line; the correct paraphrase is "a map is an archive of renamings").
- **C08/A02**: the boundary table above is the draft's claim; an independent verifier should re-check `cosmology-cosmography.md:71/:102` and `sacred-topography-pilgrimage.md:5/:57` against the final assembled text.
- **C13**: the eventual `- couples:` line should include at least `myth-symbol/cosmology-cosmography.md`, `myth-symbol/sacred-topography-pilgrimage.md`, `myth-symbol/direction-symbolism.md`, `culture-material/architecture-settlement-lexicon.md`, `culture-material/writing-media-surface-economy.md`, `culture-material/craft-artisan-lexicon.md`, `culture-material/trade-economy-lexicon.md`, `culture-material/vessel-container-lexicon.md`, `synthesis/loanword-material-dating.md`, and the handoff target. All of these resolve at HEAD.
