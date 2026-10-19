- Seat: K01 | scout | claim C | date 2026-10-19 | baseline 4a7aede

# K01 — coverage census at HEAD, thinnest-partition gap analysis, entry shape contract

Three deliverables for claim C: (1) the per-partition census at HEAD, measured by
command; (2) the gap analysis for the two thinnest partitions — which
culture-material / myth-symbol domains the existing index leaves unnamed, with the
evidence per candidate; (3) the entry shape contract, read off three exemplar
entries in full, so C01..C10 can draft entries that land clean on the first pass.

Everything below is measured at `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
(`git rev-parse HEAD`, 2026-10-19) unless a line says otherwise. No file outside
`reports/round-35/scout/` was written by this seat. The gap candidates in §2 are
**triage evidence for P01 and the C-authors to select from**, not a declaration:
declaring a gap is the planner's/authors' act, per the round-19 registry precedent
(`reports/round-19/gaps.md:7-11`).

## 1. Per-partition census at HEAD

### 1.1 Counts — the claim's before-state, reproduced

Command (run 2026-10-19 from the lane root):

```
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
```

Output:

| partition | files |
|---|---|
| linguistics | 21 |
| myth-symbol | 19 |
| culture-material | 18 |
| synthesis | 29 |
| verification | 20 |
| civilizations | 94 |
| **total** (`ls corpus/knowledge/*/*.md | wc -l`) | **201** |

This reproduces the claim's declared before-state exactly (`reports/round-35/claims.json`,
claim C `before.partition_counts` = "linguistics 21 / myth-symbol 19 / culture-material
18 / synthesis 29 / verification 20 / civilizations 94 = 201 files"). The after-state
claim C targets is therefore culture-material 24, myth-symbol 23, total 211.

### 1.2 Independent cross-check — the inventory tool

```
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
```

→ `"totals": {"files": 201, ..., "lines": 36395, ...}`; caveat block carries
`"marker_absence_is_not_verification": true` and
`"classification_is_heuristic_needs_review": true` — a second counting method
agrees with the census on 201, and a third agrees on the line total:

| method | result |
|---|---|
| `ls corpus/knowledge/*/*.md \| wc -l` | 201 |
| `tools/source-audit-inventory.py --summary` → `totals.files` | 201 |
| sum of per-file line counts (script `.scratch/k01/census.py`, `len(txt.splitlines())`) | 36395 = `totals.lines` |

### 1.3 Partition detail (lines, section bands, header fields)

Measured by `.scratch/k01/census.py` + `.scratch/k01/frontmatter.py` (scratch, not
durable; the numbers below are the durable record). "Header block" = the lines
before the file's first `## ` heading.

| partition | files | total lines | lines min/median/max | `##` sections min/mean/max | `topic` | `sources` | `couples` | `verified-at` | `recheck` | `- source:` (singular) | `- gap:` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| linguistics | 21 | 3992 | 111 / 162 / 436 | 6 / — / 14 | 21 | 21 | 21 | 21 | 21 | 3 | 0 |
| myth-symbol | 19 | 2760 | 103 / 136 / 218 | 7 / 10.7 / 14 | 19 | 19 | 19 | 19 | 19 | **19** | 1 |
| culture-material | 18 | 2557 | 103 / 149 / 177 | 7 / 10.2 / 14 | 18 | 18 | 18 | 18 | 18 | **0** | 1 |
| synthesis | 29 | 5248 | 75 / 200 / 231 | 6 / — / 14 | 29 | 29 | 29 | 29 | 29 | 29 | 0 |
| verification | 20 | 3462 | 80 / 197 / 252 | 6 / — / 13 | 20 | 20 | 20 | 20* | 20* | 8 | 0 |
| civilizations | 94 | 18376 | 164 / 196 / 231 | 9 / — / 17 | 94 | 94 | 94 | 94 | 94 | 75 | 0 |

\* In `verification/`, three entries carry `verified-at`/`recheck` **below their first
`## ` heading** rather than in the header block — the only header-block deviations in
the corpus (measured; the six rows are `verification/citation-format-and-source-registry.md:16,17`,
`verification/myth-consistency-gate.md:10,11`,
`verification/provenance-audit-ledger-format.md:10,11`). Every one of the 201 files
does carry all five core fields somewhere in the file.

Shape facts that bind the new entries:

- **The header block is universal.** `# H1 title` then the `- field:` bullet block,
  before the first `## ` heading, in all 201 entries.
- **`- source:` (singular) is partition convention, not corpus law**: myth-symbol
  19/19 and synthesis 29/29 carry it; **culture-material 0/18 does not**. So a new
  myth-symbol entry owes six header fields (five core + `- source:`); a new
  culture-material entry owes five.
- **Section band for the two thin partitions is 7–14 `##` sections**, mean ≈ 10.
- **Line band**: culture-material 103–177, myth-symbol 103–218. A draft materially
  shorter than ~100 lines is out of band for these partitions.

### 1.4 README index reconciliation (the state C11 must move)

Measured 2026-10-19 by parsing `corpus/README.md` section headers and row bullets
against the live file set:

| section (README line) | header count | index rows | live files | missing rows | ghost rows |
|---|---|---|---|---|---|
| `## linguistics/` (`corpus/README.md:123`) | 21 | 21 | 21 | 0 | 0 |
| `## myth-symbol/` (`:147`) | 19 | 19 | 19 | 0 | 0 |
| `## culture-material/` (`:169`) | 18 | 18 | 18 | 0 | 0 |
| `## synthesis/` (`:190`) | 29 | 29 | 29 | 0 | 0 |
| `## verification/` (`:222`) | 20 | 20 | 20 | 0 | 0 |
| `## civilizations/` (`:245`) | 94 | 94 | 94 | 0 | 0 |

Totals line `Total knowledge entries: 201.` at `corpus/README.md:469`; counts footer
`(total 201 files; directory totals 21/19/18/29/20/94)` at `:471-473`. The index is
clean at HEAD — **C11's job is the delta, not a repair** (24 / 23 / 211 and the
footer vector `21/23/24/29/20/94`).

Two reconciliation rules C11 inherits, both stated in the README itself:

1. **Row text is byte-equal to the entry's own `- topic:` text.** `corpus/README.md:6-8`
   (revision 1.9 note): "its row was added in filename order with the entry's own
   `- topic:` text byte-equal". The round-20 sweep exists because ten round-19 rows
   were filed as condensed paraphrases instead (`corpus/README.md:447-450`,
   `:490-493`) — a paraphrase row is a defect even when it is accurate.
2. **Rows are added in filename order within their section**, and a superseded
   reading is preserved as a dated record rather than edited away (`:475-480`).

### 1.5 How the two thin partitions declare a gap today

| form | where it lives | entries using it |
|---|---|---|
| `- gap:` header field | header block, before `- topic:` | `culture-material/transport-mobility-lexicon.md:3`, `myth-symbol/plant-symbolism.md:3` |
| in-body gap section | `## 1.` of the entry | `culture-material/vessel-container-lexicon.md:9-24`, `myth-symbol/divination-omen-systems.md:30-32`, `myth-symbol/direction-symbolism.md:194-196`, `myth-symbol/plant-symbolism.md:13` |

Two of the five gap-filling entries in these partitions carry **both** forms
(plant-symbolism: header `:3` + §1 `:13`; transport-mobility: header `:3` only,
its §1 at `:24` is the frame, not a gap statement).

**Constraint from the r10 acceptance run** (`reports/round-10/coverage/audit-filler.md:105-112`):
the runner's gap check accepted only (a) a `gap …:` clause with *filled / addressed /
served*
or a bare colon, or (b) a heading containing "gap" — and it **false-failed**
`plant-symbolism.md` because the gap was named in prose under a heading that did not
contain the word "gap" (`audit-filler.md:104-115`). Draft rule for C01..C10: put the
gap in the header as `- gap: <domain> absent from <partition> … — this entry fills it`
(which satisfies both a bare colon and "filled"), and repeat it as a `## 1.` section
whose **heading contains the word "gap"** (the vessel-container `## 1. The gap this
entry fills — …` form). That is belt-and-braces against both readings.

## 2. Thinnest-partition gap analysis

### 2.1 What the existing index already names

culture-material (18): adornment-body-codes, architecture-settlement-lexicon,
calendar-festival-systems, costume-semiotics, craft-artisan-lexicon,
cuisine-food-lexicon, dress-through-eras, era-periodization-models,
garment-lexicon-crosslinguistic, material-culture-inference-method,
music-instrument-lexicon, ritual-garments, sumptuary-law-rank-display,
textile-technology, trade-economy-lexicon, transport-mobility-lexicon,
vessel-container-lexicon, warrior-material-culture.

myth-symbol (19): animal-symbolism, celestial-symbolism-calendars, color-symbolism,
comparative-frameworks, cosmology-cosmography, creation-myths-taxonomy,
direction-symbolism, divination-omen-systems, flood-traditions,
hero-journey-variants, motif-index-usage, myth-folktale-genres, myth-ritual-theories,
number-symbolism, pantheon-archetypes, plant-symbolism, ritual-liminality,
symbolism-synthesis-method, trickster.

Adjacency is already dense: the cross-partition pointer sweep (script, 2026-10-19,
regex over all 201 entries + `corpus/README.md` + `SKILL.md`) found **108 distinct
in-corpus path references and exactly one that does not resolve**
(`linguistics/phonology-sanity.md`, referenced from
`synthesis/typed-label-routing-workflow.md` and
`verification/label-channel-routing-verification.md` — a **linguistics** defect, not
this claim's partitions, and a finding worth a `to-verify` row of its own; the
plausible target `verification/phonology-sanity-gate.md` exists, but the pointed-at
path does not). Consequence for claim C: **new entries must not create a second
dangling pointer**; every path a draft cites should be resolved by `grep` before
filing.

### 2.2 The ownership test (method, and its limits)

Method, run 2026-10-19 at HEAD (script `.scratch/k01/owner-test.py`):

1. **Mention sweep** — regex the candidate's keywords over the full text of all 201
   entries; count distinct files mentioning it.
2. **Topic-ownership test** — regex the same keywords over each entry's single
   `- topic:` line; a hit means some entry *names* that domain as its subject.
3. A candidate is a **gap signal** when mentions are many and topic-owners are zero
   (or the owners are civilization entries only, i.e. the institution is present in
   the corpus but no method entry owns the system).

Precedent for this method is the corpus's own: `vessel-container-lexicon.md:11`
sweeps keywords across the committed partition and tabulates hits-per-file to show
the domain was absent, and `divination-omen-systems.md:42` uses the
"`grep -rl … civilizations/ | wc -l` → 14 — institution present, system unowned"
form.

**Limits, stated rather than hidden:** the sweep is lexical triage, not proof of
absence — a domain can be substantively treated inside an entry without the keyword
appearing in its `- topic:` line, and a keyword can hit a passing mention. The
corpus's own inventory tool carries the same warning
(`classification_is_heuristic_needs_review: true`,
`marker_absence_is_not_verification: true`). Each candidate below therefore carries
the first-hit citation so a selector can read the actual treatment before claiming
the gap; **a C-author must re-run the sweep on the final keyword set and record its
own counts in the entry's gap section** (the r10 entries did exactly this).

### 2.3 culture-material candidate gaps (ranked)

`mentions` = files (of 201) whose text matches; `topic-owners` = entries naming the
domain in their `- topic:` line; `owners` names them.

| # | candidate | mentions | topic-owners | first-hit citation (evidence the corpus uses it) | why it is a system gap |
|---|---|---|---|---|---|
| CM-1 | **agriculture / subsistence system** — field, plough, irrigation, fallow/rotation, crop calendar, land tenure | 21 | **0** | `civilizations/amazigh-berber.md:146`; `civilizations/bali.md:14`; `civilizations/carthage.md:63` | the partition owns food (`cuisine-food-lexicon.md`) and the civil calendar (`calendar-festival-systems.md`) but no entry owns *farming itself* — tools, water, rotation, tenancy. Demand is broad (21 files) and the two nearest neighbours explicitly stop at the table and the decree |
| CM-2 | **pastoralism / animal husbandry** — herd species, transhumance, fodder, breeding, herd law | 23 | **0** | `civilizations/dine-navajo.md:75`; `civilizations/finnic-sami.md:140`; `civilizations/inca.md:128` | transport owns the draft animal as a *vehicle power source* (`transport-mobility-lexicon.md:64-70`); nothing owns the herd as an economy. Couples to cuisine (dairy/meat), textile (wool), trade (livestock markets) |
| CM-3 | **mining, quarrying, and the extractive chain** — ore, shaft, quarry, fuel, water-lifting, the mining settlement | 17 | **0** | `civilizations/aksum-ethiopia.md:121`; `civilizations/ancestral-puebloan.md:17`; `civilizations/china-song.md:83` | `craft-artisan-lexicon.md` owns the *workshop* and `warrior-material-culture.md` the *weapon*, but the chain that feeds both (extraction, charcoal, drainage) is unowned |
| CM-4 | **medicine, healing, and the body's material repair** — physician's kit, pharmacy, plague response, midwifery | 13 | **0** | `civilizations/fon-dahomey.md:56`; `civilizations/mamluk.md:37`; `myth-symbol/divination-omen-systems.md:126` | `adornment-body-codes.md` owns the *inscribed* body; no entry owns the treated body, its instruments, materia medica, or its institutions |
| CM-5 | **lighting, fuel, and domestic utilities** — lamp, candle, firewood/charcoal economy, hearth fuel, water supply | 11 | **0** | `civilizations/etruria.md:65`; `civilizations/muisca.md:70`; `culture-material/material-culture-inference-method.md:66` | fuel is the quiet constraint on every other material system (kilns, dyeing, smelting, cooking) and appears only as a passing row in the inference method's substrate inventory |
| CM-6 | **funerary and mortuary material culture** — coffin, ossuary, urn, grave goods, cemetery as institution | 40 | 4 (none owns the material side: `vessel-container-lexicon.md` as an extension, `myth-symbol/ritual-liminality.md` as rites, `civilizations/etruria.md`, `civilizations/thrace-dacia.md`) | `civilizations/akan.md:151`; `civilizations/carthage.md:19`; `civilizations/chimu.md:65` | the *rite* is owned (ritual-liminality) and the *urn* is an extension row in vessel-container (`:38`), but no entry owns the mortuary assemblage and its production |
| CM-7 | warfare logistics, siege, and the camp | 17 | 0 | `civilizations/aegean-minoan-mycenaean.md:41`; `civilizations/persia-achaemenid.md:3` | `warrior-material-culture.md` owns the fighting body and its identification systems; supply, siege works and encampment are unowned |
| CM-8 | intoxicants and drug material culture | 19 | 0 | `civilizations/greece-classical.md:73`; `civilizations/ottoman.md:151` | cuisine owns the meal and fermentation as heritage (`cuisine-food-lexicon.md:3,43,176`); the regulated substance (cultivation, trade, ritual, prohibition) is unowned |
| CM-9 | bathing, sanitation, and water infrastructure | **0** | 0 | — (no keyword hit in any of the 201 entries) | a genuinely empty domain: nothing to build on in-corpus, so an entry here would need its whole source shelf from outside. Lowest-yield candidate for a 10-entry wave; listed for completeness |

### 2.4 myth-symbol candidate gaps (ranked)

| # | candidate | mentions | topic-owners | first-hit citation | why it is a system gap |
|---|---|---|---|---|---|
| MS-1 | **afterlife, underworld, and eschatology** — destination topologies, judgement, ancestor/afterlife interfaces, mourning eschatology | 39 | 2, both civilization entries (`civilizations/china-han.md:2`, `civilizations/tibet.md:2`) — **zero in myth-symbol** | `civilizations/ainu.md:16`; `civilizations/egypt-ancient.md:38` | the partition owns cosmogony (`creation-myths-taxonomy.md`), the flood (`flood-traditions.md`) and the rite of death (`ritual-liminality.md`) but never the *destination* — the strongest single gap in this partition |
| MS-2 | **purity, pollution, and the unclean** — category violation as moral code, purification technologies, purity policing | 42 | 1 (`myth-symbol/color-symbolism.md` — owns color's purity valence, not the code system) | `civilizations/ainu.md:174`; `civilizations/balts.md:35`; `civilizations/china-tang.md:121` | Douglas's *Purity and Danger* is cited inside `cuisine-food-lexicon.md` and `animal-symbolism.md` as a borrowed tool; the system itself is unowned, and it is the coupling layer between taboo, dress, and law |
| MS-3 | **spirit, demon, and other-than-human taxonomy** — classes of spirit, demonology, possession, exorcism | 40 | 1 (`civilizations/arabia-pre-islamic.md` — jinn, as a civilization base) | `civilizations/algonquian.md:4`; `civilizations/balts.md:69`; `civilizations/china-tang.md:112` | `animal-symbolism.md:3,34` owns other-than-human *animals*; no entry owns the spirit class system that most pantheons sit inside |
| MS-4 | **pilgrimage and sacred geography** — route as rite, shrine networks, festival geography, sacred precinct law | 28 | 2, both civilization entries (`civilizations/arabia-pre-islamic.md:2`, `civilizations/zapotec-mixtec.md:2`) — **zero in myth-symbol** | `civilizations/celts.md:182`; `civilizations/greece-classical.md:70` | direction-symbolism owns orientation and `architecture-settlement-lexicon.md` the precinct, but the *journey* as a religious institution is unowned; couples directly to `transport-mobility-lexicon.md` (routes) |
| MS-5 | **sacred kingship and sovereignty ritual** | 15 | 0 | `civilizations/benin.md:1`; `civilizations/byzantium.md:63`; `civilizations/persia-achaemenid.md:1` | the office that fuses myth and law; `pantheon-archetypes.md` owns divine *roles*, `ritual-garments.md` the vestment, `sumptuary-law-rank-display.md` the display — no entry owns the doctrine |
| MS-6 | **dream, vision, and trance** | 26 | 1 (`myth-symbol/divination-omen-systems.md` — owns the *reading technology*, not the experience) | `civilizations/ancestral-puebloan.md:82`; `civilizations/finnic-sami.md:118` | divination's §8 boundary explicitly routes dream-oracles to incubation but does not own dream/vision as a system |
| MS-7 | ancestor veneration and the lineage dead | 9 | 0 | `civilizations/benin.md:67`; `civilizations/korea-joseon.md:18`; `civilizations/yoruba.md:200` | thin but structurally load-bearing: it is the bridge from MS-1 (afterlife) to ritual practice, and nine files already assume it |
| MS-8 | apocalypse, millenarianism, and end-time movements | 8 | 0 | `myth-symbol/cosmology-cosmography.md:51`; `myth-symbol/comparative-frameworks.md:19` | thin; the end-of-world *doctrine* is touched by cosmography's age-doctrine axis and the Aztec Five Suns, never owned |
| MS-9 | iconography and visual-composition grammar | 68 | 1 (`civilizations/mississippian.md`) | `civilizations/akan.md:90`; `civilizations/amazigh-berber.md:91`; `civilizations/chimu.md:85` | high mention count but the demand is mostly descriptive ("their iconography shows…") and much of it is *etic* label work; a method entry would need a source shelf this lane has not yet built. Rank below the seven above |

### 2.5 Recommended allocation for claim C (6 + 4)

Claim C needs **+6 culture-material** and **+4 myth-symbol**. On the evidence above,
the six culture-material domains with the strongest demand-to-ownership gap are
CM-1…CM-6, and the four myth-symbol domains are MS-1…MS-4:

| slot | partition | candidate | proposed slug (planner/author may re-slug; register it) |
|---|---|---|---|
| C01–C06 | culture-material | agriculture/subsistence · pastoralism/husbandry · mining+extraction · medicine/healing · lighting/fuel+water utilities · funerary material culture | `agriculture-subsistence-systems`, `pastoralism-husbandry-lexicon`, `extractive-industry-lexicon`, `medicine-healing-material`, `fuel-lighting-water-utilities`, `funerary-material-culture` |
| C07–C10 | myth-symbol | afterlife/eschatology · purity-pollution codes · spirit/demon taxonomy · pilgrimage/sacred geography | `afterlife-eschatology-symbolism`, `purity-pollution-codes`, `spirit-demon-taxonomy`, `pilgrimage-sacred-geography` |

Collision discipline to copy from round 19 (`reports/round-19/gaps.md:4-6`): the first
author to claim a gap writes the row (slug → gap → partition → seat) into a registry
before drafting; a later author finding a collision appends `-b` to the slug and says
so in the entry's gap line. Six culture-material + four myth-symbol drafts, each
naming a *different* row, is what keeps the wave from producing six variants of one
entry.

## 3. Entry shape contract (three exemplars read in full)

Exemplars read end-to-end at HEAD:
`culture-material/transport-mobility-lexicon.md` (129 lines, 11 sections),
`culture-material/vessel-container-lexicon.md` (175 lines, 12 sections),
`myth-symbol/plant-symbolism.md` (197 lines, 13 sections). Cross-checked against the
newest corpus entry, `linguistics/register-lexicon-ceilings.md` (317 lines, 12
sections, round 28), which is the current shape after the round-28 landing.

### 3.1 Header block — field by field

Order as filed (culture-material / myth-symbol form):

```
# <Title> — <subtitle naming the payload>          # H1, one line
- gap: <domain> absent from <partition> (… ) — this entry fills it     # only when filling a declared gap
- topic: <one paragraph, the whole entry in miniature>
- sources:
  - <author (year) Title, edition/venue>            # bulleted sub-list; URLs carry "(fetched YYYY-MM-DD)"
  - <in-corpus path citations, if used>
- couples: <sibling file> (division of labour); … ; handoff target: lore-shokunin receives <X> only — <Y> is theirs (lane rule)
- source: <locator summary>                          # myth-symbol only (19/19); culture-material carries none (0/18)
- verified-at: <date> — <what was re-checked live today; what was NOT re-consulted; access failures (e.g. HTTP 429)>
- recheck: before <specific use>, re-open <named source/section>; treat <claim> as <status>
```

Measured detail:

- `- topic:` is **one long line**, and it is the byte-source of the README row
  (`corpus/README.md:6-8`; §1.4 rule 1 above). Writing the topic line last, then
  pasting it into the README, is the round-28 practice.
- `- sources:` is a nested bullet list (`  - `), not a single line — see
  `transport-mobility-lexicon.md:5-19` (11 sub-bullets, each with fetched dates) and
  `animal-symbolism.md:3-9`.
- `- verified-at:` is a **prose record, not a date**: it names each item re-checked
  live, the tool used, the items *not* re-consulted, and any access failure
  (`vessel-container-lexicon.md:6`; `transport-mobility-lexicon.md:21`;
  `plant-symbolism.md:8`).
- `- recheck:` names the *trigger*, not the date: "before putting any load figure …
  into a world bible as fact, re-open the cited page and the underlying study"
  (`transport-mobility-lexicon.md:22`); `plant-symbolism.md:9` names the three
  specific re-runs.
- `- couples:` ends with the **handoff target** sentence naming lore-shokunin and
  disclaiming canon (`transport-mobility-lexicon.md:20` last clause;
  `plant-symbolism.md:6`).

### 3.2 Body skeleton (the sections every exemplar carries)

| slot | function | exemplar |
|---|---|---|
| §1 | gap statement **or** core frame; for gap-filling entries the heading contains "gap" | `vessel-container-lexicon.md:9`; `plant-symbolism.md:11`; `transport-mobility-lexicon.md:24` |
| middle §§ | typology tables → attested exemplars per row → the design lever each row implies | `vessel-container-lexicon.md:27,42,58,75,81,100`; `plant-symbolism.md:22,34,56,85` |
| calibration section | contested / discredited / invented / apocryphal items with the source that settles the status | `vessel-container-lexicon.md:123`; `plant-symbolism.md:177`; `transport-mobility-lexicon.md:100` |
| decision record | table, stable ids, evidence per row | §3.3 below |
| build order / procedure | numbered steps a worldbuilder executes | `vessel-container-lexicon.md:156`; `plant-symbolism.md:151` |
| handoff note | recipient, what the entry supplies, open questions, known limits | `transport-mobility-lexicon.md:124`; `vessel-container-lexicon.md:171`; `plant-symbolism.md:193` |

Conventions observed inside the body:

- **NON-CANON worked examples are labelled inline and disposable.** Either a
  decision-record fixture ("Worked fixture only: the *record format* is the
  deliverable; the culture below is disposable and is never world-bible canon",
  `plant-symbolism.md:164`) or an explicitly-flagged micro-example
  ("**Worked micro-example (NON-CANON — a demonstration, not a world decision).**",
  `vessel-container-lexicon.md:169`).
- **`(to-verify)` is inline and pointed**, with the reason: "(the 17th-century French
  vinaigrette precedent … reported, not adjudicated)" (`transport-mobility-lexicon.md:86`);
  "(OED s.v. celadon … not re-consulted this round — **to-verify**)"
  (`vessel-container-lexicon.md:128`).
- **Boundaries are routed, not absorbed**: `direction-symbolism.md:202` routes four
  neighbour topics out by name; `divination-omen-systems.md:147` carries a whole
  `## 8. Boundary — what this entry does not own` section. A new entry adjacent to an
  existing one owes the same section or clause.

### 3.3 Decision-record pattern

Three shapes are in use; all carry **stable per-entry ids** and **an evidence column**:

| entry | table columns | id form |
|---|---|---|
| `transport-mobility-lexicon.md:114-122` | ID \| Decision \| Trigger / condition \| Evidence \| Status | `DR-TR-01`…`DR-TR-07` |
| `vessel-container-lexicon.md:141-154` | ID \| Decision \| Why \| Rejected alternative \| Evidence | `DR-1`…`DR-12` |
| `plant-symbolism.md:166-174` | # \| Decision \| Options considered \| Chosen (fixture) \| Evidence rule applied \| Falsifier / recheck trigger | `D1`…`D6` |

Shared rules across all three: every row names the evidence (a corpus path with line
numbers, or a cited source); the row states what is *rejected* or what would falsify
it; ids are stable so later rounds can amend a row without rewriting the file
(`vessel-container-lexicon.md:139` says exactly this). `plant-symbolism.md:175` adds
the record rule worth copying: "every row names the evidence rule it applies, so a
later reader can re-run the decision instead of trusting it."

### 3.4 Source-pointer style

- **In-corpus pointers are backticked relative paths, with line numbers when the
  claim is specific**: `` `material-culture-inference-method.md:67` ``,
  `` `corpus/knowledge/civilizations/polynesia-navigation.md:23,37,53,60` ``
  (`transport-mobility-lexicon.md:19`). Both relative and root-relative forms occur;
  a draft should use the form its sibling file uses.
- **Books**: `Author (year) *Title*, Publisher` (`animal-symbolism.md:4-9`).
- **Articles**: `Author (year) "Title", *Journal* vol(issue):pages`.
- **Web**: `[Label](URL) (fetched YYYY-MM-DD)` — the fetch date is mandatory in the
  sources block (`transport-mobility-lexicon.md:6-18`).
- **Tertiary relays are declared as such**: "Wikipedia is a tertiary relay — the
  underlying works … were not read first-hand here"
  (`transport-mobility-lexicon.md:21`), and the same line lists the works not read.
- **Emic/etic marking** is part of the pointer discipline: which names are in-world
  words and which are modern scholarly labels (`vessel-container-lexicon.md:55,151`).

### 3.5 Canon boundary

Every exemplar ends with the same three-part statement: what the entry supplies, who
receives it (`lore-shokunin`, via `synthesis/worldbible-integration-contract.md`),
and which questions remain the recipient's
(`transport-mobility-lexicon.md:126-129`; `plant-symbolism.md:193-197`;
`vessel-container-lexicon.md:171-175`). `plant-symbolism.md:196` adds the handoff
shape rule — every "ancient" claim in a handoff must carry either a source or the
word *invented*.

### 3.6 Current-shape cross-check (round 28 entry)

`linguistics/register-lexicon-ceilings.md` shows two shape moves that post-date the
round-10 exemplars and are worth carrying into new drafts:

- a **`## 10. Limits of this entry`** section naming the entry's own thin spots
  (`:250`), which the round-10 exemplars carry only as a closing bullet; and
- an **appended `## 12. Errata (round 33): … re-measured`** section rather than an
  in-place edit (`:291`), i.e. corrections are appended and dated.

Both are optional for claim C, but an author who expects later re-measurement should
leave room for them.

## 4. Limits of this census

- Keyword sweeps are lexical triage (§2.2 limits); every candidate row carries the
  first-hit citation so the gap claim can be re-checked before it is declared.
- The census counts files and header fields; it does not certify the *quality* of
  any existing entry, and a passing structural gate is not a truth claim
  (`corpus/QUALITY.md`; `corpus/README.md:12-13` "Non-canon examples and passing
  structural gates do not certify historical truth").
- Nothing here is canon, promotion, or clearance; the partition counts are
  measurements at `4a7aede` and will be stale the moment claim C's entries land.

## Owed: none

K01 owes no sibling fragment: this census is an *input* to
`reports/round-35/plan/P01-c-plan.md` and to the C01..C10 authors, not a consumer of
them. At scout time `reports/round-35/` contained only `claims.json`, `targets.json`
and `telemetry/` (`ls reports/round-35/`), so no dependency fragment existed to read.

## Citations

Commands (all run 2026-10-19 from the lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`, at `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`):

- `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21 / 19 / 18 / 29 / 20 / 94
- `ls corpus/knowledge/*/*.md | wc -l` → 201
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 201`, `totals.lines 36395`
- `.scratch/k01/census.py`, `.scratch/k01/frontmatter.py` → §1.3 table (per-file line counts, section counts, header-field presence)
- `for p in …; do grep -l '^- source:' corpus/knowledge/$p/*.md | wc -l; done` → linguistics 3/21, myth-symbol 19/19, culture-material 0/18, synthesis 29/29, verification 8/20, civilizations 75/94
- `grep -c '^- gap:' corpus/knowledge/*/*.md` → 1 hit each in `culture-material/transport-mobility-lexicon.md` and `myth-symbol/plant-symbolism.md`
- header-block deviation script → the six rows in `verification/{citation-format-and-source-registry,myth-consistency-gate,provenance-audit-ledger-format}.md`
- README reconciliation script (headers/rows vs live files) → 0 missing, 0 ghost rows in every section
- `.scratch/k01/gapsweep.py`, `.scratch/k01/owner-test.py` → §2.3/§2.4 mention and topic-owner counts
- cross-partition pointer sweep script → 108 distinct refs, 1 dangling (`linguistics/phonology-sanity.md`)

Repo files:

- `reports/round-35/claims.json` — claim C before/after, thresholds
- `reports/round-35/targets.json` — K01 mission; shared_rules
- `corpus/README.md:6-8, 15-16, 123, 147, 169, 190, 222, 245, 447-450, 469, 471-473, 475-480, 490-493`
- `corpus/QUALITY.md` (five admission criteria)
- `corpus/knowledge/culture-material/transport-mobility-lexicon.md:3,5-22,24,114-129`
- `corpus/knowledge/culture-material/vessel-container-lexicon.md:9-24,27,38,55,123,137-154,156,169,171-175`
- `corpus/knowledge/myth-symbol/plant-symbolism.md:3,11-13,164,166-175,177,193-197`
- `corpus/knowledge/myth-symbol/divination-omen-systems.md:30-32,42,147`
- `corpus/knowledge/myth-symbol/direction-symbolism.md:194-196,202`
- `corpus/knowledge/myth-symbol/animal-symbolism.md:3-9,34,61,66`
- `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:3,16-17,23,125`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:250,291`
- `corpus/knowledge/culture-material/material-culture-inference-method.md:66-67,92`
- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:3,6,43,86,131,176`
- `reports/round-10/coverage/audit-filler.md:62-78,104-119` (gap-check regexes and the plant-symbolism false-fail)
- `reports/round-19/gaps.md:7-11` (gap-registry + collision-log precedent)
- `SKILL.md:536-551` (corpus map)
