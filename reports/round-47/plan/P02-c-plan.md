# P02 — C-claim plan: the cartography entry's structure

- Seat: P02 | role: planner | claim: C | round 47 (loop 2, opening build)
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`, 2026-10-19)
- Out path: `reports/round-47/plan/P02-c-plan.md` (this file only; no corpus bytes written)
- Mission: the cartography entry's structure — header fields, section skeleton, the boundary table against all seven K02-named neighbours, the calibration bank, and the source shelf with `(to-verify)` markers.
- Claim contract: `reports/round-47/claims.json:22-34`; seat mission: `reports/round-47/targets.json:17`.

**Result in one line:** the entry is a 15-section culture-material register entry built on one master claim (a map is an argument about space, not a picture of it), with a canonical single-line `- topic:` fixed here so C04's head block and C09's README row cannot drift, a seven-row boundary table that cites the live disclaimer at `cosmology-cosmography.md:71/:102`, an eight-row calibration bank, and a tiered shelf whose every external item is `(to-verify)` because this lane has no network.

---

## 1. Measured baseline and freshness (this seat, not asserted)

All commands run from the lane root on 2026-10-19 with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
```

Partition census at the baseline:

| partition | files |
|---|---:|
| civilizations | 94 |
| culture-material | **25** |
| linguistics | 25 |
| myth-symbol | 26 |
| synthesis | 29 |
| verification | 24 |
| **total** | **223** |

Sort position, measured (`ls corpus/knowledge/culture-material/ | grep -nE 'calendar|costume'`): `calendar-festival-systems.md` at position 5, `costume-semiotics.md` at position 6. The new slug sorts between them.

### 1.1 Ownership sweep — broad hits, zero owners

The broad topic-line test (`grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/`) returns **11 hits in 11 files**. Every hit is metaphor, verb, statistical "survey", or a handoff, exactly as K02 §3.3 dispositioned them at r44:

| file | what the hit is |
|---|---|
| `linguistics/sound-symbolism.md` | "map" as a conceptual schema |
| `linguistics/dialect-register-consistency.md` | a dialect map as a lect inventory |
| `linguistics/sacred-registers-liturgical-language.md` | "map" as a verb |
| `myth-symbol/number-symbolism.md` | "survey" in the statistical sense |
| `myth-symbol/purity-pollution-boundary-systems.md` | "boundary map" as the entry's master metaphor |
| `myth-symbol/sacred-topography-pilgrimage.md` | sacred-geography mapping as a diagram — the nearest neighbour |
| `culture-material/ritual-garments.md` | an "atonement map" metaphor |
| `synthesis/dialect-faction-map-workflow.md` | "map" as a verb |
| `civilizations/finnic-sami.md` | "identity map" metaphor |
| `civilizations/mesoamerica-primary-sources.md` | "reference map" metaphor |
| `civilizations/africa-primary-sources.md` | "source map" metaphor |

The **strict** topic-owner test (`cartograph|mapmak|portolan|cadastr`) returns **0**. The filename test returns **0**. The target slug is unused.

### 1.2 Demand, measured honestly

The tight demand pattern K02 used (`cartograph|mapmak|portolan|cadastr|mappae|mappa mundi|surveyor|theodolit|compass rose|graticule|hereford mappa|lienzos?|stick chart|star chart|world map|map of|maps of|drawn map`) still returns **29 files / 35 lines** at `6e9a30d`. The genuine cartographic footprint remains the seven files K02 §3.4 tabulated, each hit a by-product or an explicit handoff (the line count is not re-asserted here: a raw regex over the same vocabulary returns false positives from bibliography titles in `direction-symbolism.md` and `mineral-stone-symbolism.md`, so the manual disposition governs). The load-bearing disclaimer is live:

- `myth-symbol/cosmology-cosmography.md:71` — T-O diagrams are "symbolic, not survey maps".
- `myth-symbol/cosmology-cosmography.md:102` — they are "not cartographic claims".
- `culture-material/architecture-settlement-lexicon.md:95` — the Roman castrum grid is "surveyed with the groma" and "the grid is cadastral" (one sentence; the built plan is that entry's object, not the survey chain).
- `civilizations/mesoamerica-primary-sources.md:58` — lienzos and cartographic histories are one row in a manuscript inventory (that entry owns provenance, not map production).
- `myth-symbol/direction-symbolism.md:51` — the true-vs-magnetic "compass trap" (orientation register, not the map convention).
- `culture-material/transport-mobility-lexicon.md:28` — "a route is only real if someone maintains it" (route institution, not route representation).
- `civilizations/japan-medieval-sengoku.md:157` — a warning not to read an Edo cadastral map as a Sengoku map (periodization caution).

The remaining 22 files in the broad pattern are the metaphor class above. **Low raw demand is stated, not hidden:** this is a structurally named but unbuilt register, not a high-demand omission.

### 1.3 Prior-round status — the "carried" question, answered precisely

The claim's phrase "NOT a carried topic" needs a definition that survives the r43/r44 failure class. This plan uses:

> A candidate is **carried** when a round *other than the round that supplied this claim's seed* has already named it in a gap registry, scout recommendation, or drafted landing. The seed round itself naming the candidate is not carriage; it is provenance.

Evidence at `6e9a30d`:

- `reports/round-44/scout/K02-gap-scout.md:85` selects cartography as the fresh candidate after screening the carried set.
- `reports/round-44/scout/K02-gap-scout.md:378-388` records that the r44 C landing candidate actually drafted was **dream/vision/trance**, which was carried from r42 (`reports/round-42/scout/K02-myth-gaps.md:216`), and that r44 landed neither.
- `reports/round-44/cov/C01-entry-draft.md:1` confirms the r44 entry draft was `myth-symbol/dream-vision-trance.md`, not cartography.
- A global `reports/` grep for `cartograph|mapmak|portolan|cadastr|mappa|stick chart|world map` now returns the r44 seed and its integration discussion (K02, C05, C06, S01, R01, R02, X01, A01) plus pre-existing by-product copies under `reports/supplement-opencode-1/scratch/` and one inherited-bibliography line at `reports/round-42/cov/C04-entry-4.md`. **No other round has proposed cartography; no cartography entry draft exists.**
- The r44 round filed `validation.json` with C unverified and the corpus total stayed 223.

Therefore the freshness statement for the `- gap filled:` field must say: *the only prior proposal is `reports/round-44/scout/K02-gap-scout.md`, which is this claim's seed; no other round proposed it; no cartography entry was drafted or landed; the live 223 tree has zero owners.* It must **not** say "no prior proposal anywhere", because that sentence is false and would be the same stale-premise defect the claim is repairing.

**Correction to `P01-plan.md` §4.2 F0:** its gate wording "a global `reports/` proposal grep showing no prior cartography proposal" is over-strict and unachievable given the claim's own seed. The operative check is the four-part one above. K01's recheck should report the r44 seed explicitly and prove that no *other* round proposed it. This is a plan-level correction, not a criticism of K01's mission.

### 1.4 README state at the baseline

| anchor | live bytes |
|---|---|
| `corpus/README.md:234` | `## culture-material/ (25)` |
| `corpus/README.md:240-241` | calendar row, then costume row |
| `corpus/README.md:544` | `Total knowledge entries: 223.` |
| `corpus/README.md:546-548` | `Counts checked 2026-10-19 from the repo root:` / inventory command / `(total 223 files; directory totals 25/26/25/29/24/94).` |
| `corpus/README.md:10-11` | `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**.` — this sums to **217**, not 223; myth-symbol is understated (23 instead of 26), culture-material is overstated (26 instead of 25), and synthesis is understated (25 instead of 29) |

Additional observed anomaly, **report-only, not in this round's scope:** `corpus/README.md:1` and `:3` both carry the H1 `# kotodama-shokunin corpus index` (a duplicated title). The claim sanctions only the prose-vector repair; this plan does not absorb the duplicate-title fix. C09 should report it and leave it untouched unless the integrator rules otherwise.

---

## 2. The entry contract the draft must satisfy

### 2.1 Head block — field order and consumers

The established culture-material shape (checked against `timekeeping-instruments.md:1-9`, `mineral-stone-symbolism.md:1-11`, `writing-media-surface-economy.md:1-9`, `furniture-interior-lexicon.md:1-15`) is:

| order | field | required by | consumer |
|---:|---|---|---|
| 1 | H1 title | convention | reader; not parsed |
| 2 | `- topic:` | `tools/gates/provenance-audit.py:75` (`FIELD_NAMES`), README sweep | `reports/round-28/readme/sweep.py:74-81` parses it; the README row must equal the space-joined text |
| 3 | `- gap filled:` | claim C (`claims.json:28`), house convention | C05 freshness, C07 contract audit |
| 4 | `- sources:` | provenance gate; `QUALITY.md` item 1 | C06/C12 shelf audit |
| 5 | `- source:` | house convention | C06 audit of what was actually checked |
| 6 | `- couples:` | provenance gate; `QUALITY.md` item 3 | C13 couples resolver, A02 ownership |
| 7 | `- verified-at:` | house convention | C05/C07; the "no reading-laundering" rule |
| 8 | `- recheck:` | house convention | reader |
| 9 | `- scope:` | house convention; `QUALITY.md` item 5 | A01 scope verifier |

Rules:

1. `- topic:` is **one physical line**. `TOPIC_RE` stops at the next top-level `- <word>:` field, and `topic_of()` strips and space-joins continuation lines. A single line removes the join-fragility; the README row must be byte-equal to the parsed text.
2. Do not put a blank line between `- topic:` and the next field; `TOPIC_RE` tolerates it but the house shape does not.
3. `- sources:` may be a blank field followed by an indented bullet list (the writing-media/mineral-stone style). The provenance gate treats a placeholder-only value as empty; a real list passes.
4. `- couples:` must name real files and say what each owns. A token that does not resolve at HEAD fails C13.
5. `- verified-at:` must name the checks actually run this round and the checks not run (no external fetch). A template date is a defect.
6. The body must contain the word `calibrat*` and a real calibration section; the gate reports `missing-calibration` only when the vocabulary is absent, so passing the gate is necessary but not sufficient.

### 2.2 Body conventions

- Numbered `## N.` sections, in the order of §4 below.
- Every section ends in a **design lever** or a **decision row** (`corpus/QUALITY.md:16-17`: usable tables, typology, worked example; no essays).
- Every real-world factual claim carries a source or an inline `(to-verify)`. No external work is described as inspected.
- No canon: the entry decides nothing about any world; it ends at the handoff (`QUALITY.md:18-20`).
- No restatement of a neighbour's owned content; cite by `path:line` and state the boundary.
- Correction discipline: future corrections are new sections or a new entry, never rewrites (the partition's stated rule, e.g. `mineral-stone-symbolism.md:15`).

### 2.3 Length and split budget

Comparable entries at HEAD: `timekeeping-instruments.md` 140 lines, `furniture-interior-lexicon.md` 143, `mineral-stone-symbolism.md` ~200, `writing-media-surface-economy.md` 201. This entry has more tables and a 12-row decision record; target **260-320 lines total**, split:

| block | owner | target lines |
|---|---|---:|
| head block | C04 | 45-60 |
| §1-§4 | C01 | 80-95 |
| §5-§9 | C02 | 85-100 |
| §10-§15 | C03 | 80-95 |

Anything above 340 lines is bloat for this register; anything below 230 is thin for a 15-section entry with a worked example. C11 should flag a total outside that band rather than silently accepting it.

### 2.4 The nine-topic content spine, mapped onto the 15 sections

K02 §4.3 proposed a ten-item spine (question → form typology → survey chain → projection/scale → symbolization → reproduction/trade → silences → calibration → build order → decision record + example). The round's seat allocation (`targets.json:21-23`) splits the body into 15 sections. The mapping is:

| K02 spine item | this entry's section |
|---|---|
| question | §2 (the map's question and the register test) |
| form typology | §2 item 4 (the eight-form table) |
| survey chain | §5 items 1-5 (chain, instruments, modes, error budget, control) |
| projection/scale | §5 items 6-7 (projection families, scale) |
| symbolization | §5 item 8 (the symbol grammar) and §3 (the semiotics of the six mechanisms) |
| reproduction/trade | §4 (surface/reproduction classes) + §6 (scarcity) + §7 (the trade) |
| silences | §3 (omission as a mechanism) and §11 (the worked example's blank) |
| calibration | §12 |
| build order | §10 |
| decision record + example | §11 (example) + §13 (decision record) |

Nothing from the K02 spine is dropped; the addition is §9 (provenance/charter and the container-name fossil), which the seat allocation requires and which K02 placed implicitly under "trade" and "the map as legal instrument".

---

## 3. Canonical head block (candidate for C04)

C04 owns the bytes. This is the structural candidate; C04 may tighten prose, but **the `- topic:` string below is canonical** — C09 pastes its parsed text into the README row, and any change must propagate to C09 before the sweep.

```markdown
# Cartography and mapmaking — the made map as an instrument and a claim: the survey → projection → drawing → reproduction chain, the map-form typology, the map's silences, and the authority warrant

- topic: the made map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative, and the four choices that constitute it (what is measured, what is preserved, what is drawn, who may copy and read it); the map-form typology by the question each answers (itinerary/strip, cadastral/land register, chorographic/regional, portolan/nautical, celestial/star chart, cosmographic/world diagram, thematic, and the cartographic history/lienzo); the survey instruments and their error budget (pacing, rope and chain, groma, dioptra, astrolabe, compass, cross-staff, plane table, theodolite, triangulation); projection and scale as claims (equirectangular, stereographic, Mercator, polar azimuthal, local plane; what each preserves and distorts; the scale bar and the smallest drawn unit); the symbol grammar (orientation and which north, compass rose, scale bar, legend, boundary line, blank, monster and vignette) and the map as a text to be read; the map's silences and its use as a legal/territorial instrument (treaty map, cadastral register, tithe map, the replaced toponym); the reproduction economics (manuscript, woodblock, copperplate, lithography, the atlas, state monopoly and pirate copy) and the mapmaker trade (surveyor, draughtsman, engraver, printer, instrument maker; guild, office, patronage, maker's mark); provenance and authority (charter, warrant, forgery, the copy chain) and the word layer that fossilizes the object (map, chart, atlas, portolan, legend, scale); a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory, one-way diffusion); a build order, a twelve-row decision record, and one NON-CANON worked irrigation-cadastral example. Reference knowledge and method only; canon decisions belong to lore-shokunin.

- gap filled: the corpus owns space as cosmology (`corpus/knowledge/myth-symbol/cosmology-cosmography.md`), space as sacred route (`corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md`), space as orientation code (`corpus/knowledge/myth-symbol/direction-symbolism.md`), the built plan (`corpus/knowledge/culture-material/architecture-settlement-lexicon.md`), and the surfaces a map might be drawn on (`corpus/knowledge/culture-material/writing-media-surface-economy.md`) — but it owns the made map nowhere. The partition's nearest file disclaims the register: `cosmology-cosmography.md:71` calls T-O diagrams "symbolic, not survey maps" and `:102` says they are "not cartographic claims". Fresh absence sweep 2026-10-19 at lane HEAD `6e9a30d` (`git rev-parse HEAD`): total **223**, culture-material **25**; `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → No such file; filename owners (`find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*'`) → **0**; strict topic owners (`grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/`) → **0**; the broad 11-hit topic sweep is all metaphor/verb/handoff, dispositioned in §1; tight demand → **29 files / 35 lines**, of which the genuine cartographic footprint is **7 files / 9 lines**, every line a by-product or an explicit handoff. Prior-round status: the only proposal is `reports/round-44/scout/K02-gap-scout.md` (this claim's seed); no other round proposed cartography, no cartography entry draft exists, and r44 landed neither candidate (total stayed 223).
```

The `- gap filled:` line above is a **candidate**, not filed evidence. C04 must re-run the commands at the landing HEAD and update the counts and date; C05 independently re-derives them. If the landing HEAD is still `6e9a30d` and the tree is still 223, the counts stand as written.

### 3.1 `- sources:` candidate

```markdown
- sources:
  - In-corpus anchors (each re-read by C06 at the landing HEAD; the entry cites, and does not restate, the owning entry): `corpus/knowledge/myth-symbol/cosmology-cosmography.md:6` (Smith 1987 and Wheatley 1971 registrations; the critique inherited, not re-derived), `:41-42` (Wheatley's ceremonial-city thesis and J. Z. Smith's built-expression test), `:68` (the ceque system as a radial diagram), `:71` and `:102` (the T-O "symbolic, not survey maps / not cartographic" disclaimer — the entry's charter citation), `:75` (the geometry menu); `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5` (the place-register topic), `:57` (sacred-geography diagram geometries), `:69` (the three route types), `:124` (route-type build step), `:132` (the NON-CANON river-delta example this entry deliberately does not reuse); `corpus/knowledge/myth-symbol/direction-symbolism.md:51` (the true-vs-magnetic compass trap), `:112` (tawaf circuits), `:125` (grave orientation and procession routes), `:132` (qibla); `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` (castrum grid, groma, cadastral claim), `:101` (instrument + founding rite + claim word); `corpus/knowledge/culture-material/writing-media-surface-economy.md:3` (the seven surface families and the cost ladder — cited, not restated); `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:28` (the [LIEN] record), `:58` (lienzos as a source class); `corpus/knowledge/culture-material/transport-mobility-lexicon.md:28` (the maintenance rule), `:35` (Qhapaq Ñan), `:117` (DR-TR-02); `corpus/knowledge/culture-material/timekeeping-instruments.md:50` (longitude at sea as one cell of a timekeeping table); `corpus/knowledge/civilizations/polynesia-navigation.md:52` (horizon compass vs steering-star sequence vs latitude clue), `:63` (the Kāpeʻa row); `corpus/knowledge/civilizations/japan-medieval-sengoku.md:157` (the Edo-cadastral-map caution); `corpus/knowledge/linguistics/naming-systems.md:70` (critical toponymy: a map is an archive of renamings); `corpus/knowledge/verification/real-world-inspiration-boundaries.md:2` and its recheck at `:6` (restricted/sacred material), `corpus/knowledge/verification/myth-consistency-gate.md:34` (the access-boundary rule), `corpus/knowledge/verification/to-verify-triage-protocol.md:15` (what `(to-verify)` means).
  - Inherited bibliography — standard works, **not fetched or page-checked this round (no network at this seat)**; author/year/title are confident, editions/volumes/page ranges are `(to-verify)`:
    - Survey and projection: Ptolemy, *Geography*, trans. Berggren & Jones (2000), Princeton UP; Dilke (1971), *The Roman Land Surveyors*, David & Charles; Snyder (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395; Campbell (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *The History of Cartography*, vol. 1 (page range `to-verify`).
    - History and reference: Harley & Woodward (eds.), *The History of Cartography*, 6 vols. in 7, University of Chicago Press, 1987–2022; Harley (1989), "Deconstructing the Map," *Cartographica* 26(2): 1–20; Wood (1992; 2nd ed. 2010), *The Power of Maps*, Guilford; Monmonier (1991; 3rd ed. 2018), *How to Lie with Maps*, University of Chicago Press; Jacob (French 1992; Eng. trans. 2006), *The Sovereign Map*, University of Chicago Press; Pickles (2004), *A History of Spaces*, Routledge; Buisseret (ed.) (1992), *Monarchs, Ministers, and Maps*, University of Chicago Press; Edson (2007), *The World Map, 1300–1492*, Johns Hopkins UP; Kain & Baigent (1992), *The Cadastral Map in the Service of the State*, University of Chicago Press.
    - Non-European and colonial: Mundy (1996), *The Mapping of New Spain*, University of Chicago Press; Boone (2000), *Stories in Red and Black*, University of Texas Press; al-Idrisi, *Nuzhat al-mushtāq* (1154; edition/translation `to-verify`); Needham (1959), *Science and Civilisation in China*, vol. 3, CUP (registered in-corpus at `cosmology-cosmography.md:6`); the *Tabula Peutingeriana* and the *Antonine Itinerary* (editions `to-verify`); Ortelius, *Theatrum Orbis Terrarum* (1570) and Mercator's atlas (editions `to-verify`).
  - No external work in this list was consulted, fetched, or page-checked this round. The list is a shelf, not a set of receipts; every claim that depends on a page carries `(to-verify)` in place.
```

### 3.2 `- source:`, `- verified-at:`, `- recheck:`, `- scope:` candidates

```markdown
- source: the lane-side authority is the in-corpus `path:line` anchor list above, each re-read at lane HEAD `6e9a30d` on 2026-10-19, plus the absence-sweep commands recorded in `- gap filled:`; the charter citation is `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` and `:102`. The external works are cited as literature for the mechanisms they document, never blended into a claim about any real community; **no external source was fetched or resolved this round** (no network at this seat), so every bibliographic detail the author could not check against a held copy or a lane citation carries an inline `(to-verify)`, listed together in §14. The typology, the survey-to-sheet chain, the projection table, the symbol grammar, the decision rows and the worked example are lane-authored organization built on those citations.

- verified-at: 2026-10-19 — written this round at lane HEAD `6e9a30d` (`git rev-parse HEAD` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`, equal to the declared baseline at `reports/round-47/claims.json:7`). Measured at write time with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: partition census `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**; the absence sweep in `- gap filled:` (filename owners 0, strict topic owners 0, broad hits 11 all dispositioned, tight demand 29 files / 35 lines with 7 files / 9 lines genuine); the target slug absent. Every in-repo `path:line` anchor cited in this entry was re-read live in this pass and each cited line re-checked against the file (count recorded in §15); **not done this round:** no external source was fetched or resolved, no page-level check of Ptolemy, Dilke, Snyder, Campbell, Harley, Woodward, Wood, Monmonier, Jacob, Pickles, Buisseret, Edson, Kain & Baigent, Mundy, Boone, al-Idrisi, Needham, the Peutinger Table, Ortelius or Mercator was performed, and no real tradition's restricted map was inspected. Every claim whose accuracy depends on those page-level checks carries an inline `(to-verify)` below.

- recheck: before printing any date of a map, instrument, survey or edition (Hereford c. 1300, the Peutinger Table, Ortelius 1570, the Mercator atlas), any precision or scale figure, any price/cost figure, any etymology (*map*, *chart*, *atlas*, *portolan*, *legend*, *scale*, *cartography*), any claim that a culture "first" made a map or that cartography diffused one-way, any treaty/cadastral/tithe map as settled law, any projection ranked as "correct", any reading of a real tradition's restricted or sacred map, or any inference from a map's silence to a real absence. Re-run §12 on the then-current evidence before any of these becomes load-bearing in a world bible.

- scope: reference knowledge and craft method for the culture-material partition only. This entry decides nothing about any world, names no canon fact, makes no promotion or clearance verdict, and ends at the handoff (§15). Every `(to-verify)` item is a backlog row, not an assertion. Restricted real-world material is screened by `corpus/knowledge/verification/real-world-inspiration-boundaries.md`, not here.
```

### 3.3 `- couples:` candidate

```markdown
- couples: `corpus/knowledge/myth-symbol/cosmology-cosmography.md` (owns the five world-model axes and the T-O symbolic disclaimer at `:71,:102`; this entry owns the survey map and cites the disclaimer as its charter, without restating the five-axis typology), `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` (owns the holy-site typology and the route-as-rite at `:5,:69`; this entry owns how a route is measured and drawn, and cites the route types as map content without re-owning pilgrimage), `corpus/knowledge/myth-symbol/direction-symbolism.md` (owns orientation frames and the compass trap at `:51`; this entry owns the map convention — orientation choice, compass rose, north arrow — and cites `:51` without restating the direction register), `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` (owns the city-plan lexicon and the castrum/groma sentence at `:95`; this entry owns land survey as a map-production step and does not restate the settlement vocabulary), `corpus/knowledge/culture-material/writing-media-surface-economy.md` (owns the seven surface families and the cost ladder at `:3`; this entry owns map-specific media and reproduction and cites the surface economy), `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` (owns the lienzo source class and its provenance at `:28,:58`; this entry cites the genre as a map-form exemplar and does not restate the manuscript inventory), `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (owns routes and the maintenance institution at `:28,:35,:117`; this entry owns the representation of routes and cites DR-TR-02), `corpus/knowledge/culture-material/timekeeping-instruments.md` (longitude at sea is one cell of its table at `:50`; a marine chart is a timekeeping instrument's customer, not its replacement), `corpus/knowledge/culture-material/trade-economy-lexicon.md` (market, measure and money words; a map's price and its legal function join that ladder), `corpus/knowledge/culture-material/craft-artisan-lexicon.md` (guild ladders, Meisterstück and maker's marks at its §4; the surveyor/engraver/printer is a signed trade), `corpus/knowledge/culture-material/calendar-festival-systems.md` (a dated map needs an era; the map's date is a calendar artifact), `corpus/knowledge/culture-material/material-culture-inference-method.md` (the ladder tags and formation processes this entry's survival notes use), `corpus/knowledge/linguistics/naming-systems.md` (toponymy and critical toponymy at `:70`; a map is an archive of renamings), `corpus/knowledge/linguistics/writing-systems.md` (labels, legends and the script a map carries), `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` (the map/chart/atlas word field as a semantic field), `corpus/knowledge/linguistics/historical-linguistics.md` and `corpus/knowledge/linguistics/language-contact.md` (map-word loan strata date contact), `corpus/knowledge/civilizations/polynesia-navigation.md` (horizon compass and steering-star sequence at `:52,:63`; navigation is that entry's, the chart is this entry's), `corpus/knowledge/civilizations/japan-medieval-sengoku.md` (the Edo-cadastral-map caution at `:157`), `corpus/knowledge/verification/real-world-inspiration-boundaries.md` (restricted/sacred maps; its recheck at `:6`), `corpus/knowledge/verification/myth-consistency-gate.md` (the access-boundary rule at `:34`), `corpus/knowledge/verification/to-verify-triage-protocol.md` (every `(to-verify)` mark routes through that procedure); handoff target: lore-shokunin world bible — reference knowledge, tables and method only; canon decisions are theirs (lane rule, `AGENTS.md`).
```

C13 must resolve every token. All paths above exist at `6e9a30d` (this seat checked the seven neighbours; the secondary couples are existing entries listed by `ls`/`grep` and must be re-resolved by C13 before landing). The `handoff target:` clause is prose, not a path token; the resolver's tokenization must not treat `lore-shokunin` as a file.

---

## 4. The 15-section body skeleton

The allocation is binding from `targets.json:21-23`: C01 drafts §1-4, C02 drafts §5-9, C03 drafts §10-15. Each section ends in a design lever or a decision row. Section numbers are fixed so the three drafts stitch without renumbering.

| § | heading (working) | owner | K02 spine item | target lines |
|---:|---|---|---|---:|
| 1 | What this entry owns, and where the seven siblings stop | C01 | frame | 18-22 |
| 2 | The property that makes a map a register | C01 | question + form typology | 22-28 |
| 3 | The map-meaning mechanisms | C01 | silences (conceptual) | 18-22 |
| 4 | Material and trade classes | C01 | reproduction/trade (classes) | 20-26 |
| 5 | The survey-to-symbol chain | C02 | survey + projection/scale + symbolization | 30-38 |
| 6 | Scarcity and prestige — the economics of the rare sheet | C02 | reproduction/trade (scarcity) | 14-18 |
| 7 | The mapmaker trade | C02 | reproduction/trade (people) | 16-20 |
| 8 | Provenance and charter — who warrants the map | C02 | the map as legal instrument | 16-20 |
| 9 | The container-name fossil — the word layer | C02 | (K02's word layer, promoted) | 14-18 |
| 10 | Build order | C03 | build order | 14-18 |
| 11 | Worked micro-example (NON-CANON) | C03 | worked example | 22-28 |
| 12 | Calibration bank | C03 | calibration | 20-26 |
| 13 | Decision record | C03 | decision record | 16-20 |
| 14 | Recheck triggers | C03 | (head field, expanded) | 8-12 |
| 15 | Scope and handoff | C03 | handoff | 10-14 |

### §1 — What this entry owns, and where the seven siblings stop (C01)

Required:

- The master claim in one sentence: *a map is an argument about space, not a picture of it; its authority comes from the survey chain behind it and its politics from what it omits.*
- The **seven-row boundary table** from plan §5, embedded in the entry's §1 verbatim or in the same row order.
- A "why it is load-bearing for fiction" paragraph with three scene types: the border dispute that turns on a line's thickness; the pilot who trusts a chart whose survey never left the coast; the tax map whose blank is the temple's exemption.
- A one-sentence disposition of the 11 broad topic-line hits (metaphor, verb, statistical survey, or handoff) so the `- gap filled:` promise "dispositioned in §1" is true; the full 11-row table stays in the drafting fragment, not the entry.
- The method statement: reference and craft method only; no canon; handoff at §15.

Must not restate: the cosmography five-axis typology, the pilgrimage route typology, the direction register, the settlement lexicon, the seven writing surfaces, the Mesoamerican provenance table, or the transport four layers. Cite each by its live line and state the split.

Ends with: a **design lever** — "if two siblings both seem to own the object, the map is the sheet, not the space."

### §2 — The property that makes a map a register (C01)

Required:

1. **The four constitutive choices.** A map is the output of four load-bearing choices: **what is measured** (survey precision and warrant), **what is preserved** (projection and scale), **what is drawn** (selection and symbolization), and **who may copy and read it** (reproduction and access). Fix all four or the object is decoration.
2. **The register test** (four questions a "map" must answer):
   - *Warrant*: who measured it, by what authority, and when?
   - *Selection*: what is omitted, and who benefits from the omission?
   - *Projection*: what is distorted, and what property was chosen to preserve?
   - *Address*: who can read it, and who is excluded by language, literacy, secrecy or scale?
   A sheet that answers none of the four is a picture; one that answers one is a diagram; one that answers all four is a map.
3. **The object-boundary table:** map vs picture vs diagram vs itinerary vs cosmogram vs mental map vs GIS layer. Columns: object / what it asserts / what it lacks / who uses it / failure mode. This is where "map" stops being a metaphor.
4. **The map-form typology table** — the entry's central typology. Columns: form / the question it answers / typical reader / survey precision required / typical medium / signature failure. Rows:
   - itinerary / strip map — "how do I get there?" — traveller — linear distance and stations — roll or strip — route drawn, space omitted.
   - cadastral / land register — "who owns what, and what is owed?" — tax office, court — parcel boundary, area — register or sheet — boundary precision exceeds survey.
   - chorographic / regional — "what is where in this province?" — administrator, educated reader — selected features — printed sheet — decorative selection mistaken for inventory.
   - portolan / nautical — "what course and what hazards?" — pilot — coastline, bearings, soundings — chart on vellum/cloth — magnetic drift and copy drift.
   - celestial / star chart — "what is above, and when?" — astronomer, astrologer, navigator — angular position — chart or globe — precession/epoch mismatch.
   - cosmographic / world diagram — "what is the world's shape and order?" — priest, scholar — none (symbolic) — manuscript diagram — symbolic diagram read as survey (the T-O trap).
   - thematic — "what pattern matters?" — reformer, official, merchant — chosen variable — printed sheet — the variable's collection bias.
   - cartographic history / lienzo — "what is our claim and our journey?" — lineage, court, community — event/route sequence — cloth or codex — legal document read as neutral picture.

   The row "cosmographic" cites `cosmology-cosmography.md:71/:102` and explicitly says the T-O diagram is the *contrast case*, not the survey map.
5. A **design lever**: the form follows the question, not the era. A culture can have a precise cadastral map and no portolan, or a beautiful cosmogram and no survey.

Must not restate: the world-model axes (`cosmology-cosmography.md:2`); the route types (`sacred-topography-pilgrimage.md:69`); the direction frames (`direction-symbolism.md:3`).

### §3 — The map-meaning mechanisms (C01)

Required:

- A six-row table: **selection, projection, scale, orientation, symbolization, omission/silence** — each with *what it asserts*, *a real exemplar*, *the failure mode*, and *where §5 gives the technical treatment*. §3 is the semiotics; §5 is the production chain. State the split explicitly so the two sections do not duplicate.
- **The blank as a mechanism.** Four kinds of blank: unknown (no survey), forbidden (restricted), depopulated (political), reserved (legal exemption). Each is a different claim; the entry must not let one stand for another. The empty interior of a map is often the most informative mark on it.
- **Centre and periphery.** Where the map puts the reader's polity, the sacred centre, the sea, the "barbarian" edge; the map's frame as a claim.
- **Monster and vignette.** The decorative register as a warrant of eyewitness authority and as a place-holder for the unknown; use sparingly and date it.
- **The map as a text to be read.** Reading order (title/cartouche → orientation → scale → legend → content → margin), and the rule that an unlabelled map is read with the reader's own assumptions.
- A **design lever**: for every map a character uses, write one sentence naming what the map argues; if the sentence is "it shows the land", the map is scenery.

Must not restate: the direction register's compass trap (`direction-symbolism.md:51`); the writing-surface cost ladder (`writing-media-surface-economy.md:3`); the route-as-rite (`sacred-topography-pilgrimage.md:69`).

### §4 — Material and trade classes (C01)

Required:

1. **Surface classes table** — at least: parchment/vellum, paper, cloth, wall/plaster, palm leaf, woodblock matrix, copperplate matrix. Columns: surface / preparation chain / tool / ink / unit of text-or-image / cost driver / survival. The map-specific point: a map's surface is chosen for *correction* and *copying*, not only for writing.
2. **Reproduction classes table** — manuscript (one master, hand copies), woodblock (carve once, print many), copperplate (engrave once, reprint with wear), lithography (draw on stone, print), and the modern print. Columns: edition size / cost per copy / fidelity across copies / who can own one / signature failure (plate wear, copy drift, pirate edition).
3. **The atlas as a product and as a state project.** The bound collection changes the map's unit from sheet to book; the atlas's order is an argument (world → nation → province). Cite the Ortelius/Mercator shelf with `(to-verify)`.
4. **Legal/territorial classes** (names only; §8 explains the warrant): treaty map, cadastral register, tithe map, boundary map, colonial survey, the map as court exhibit.
5. **Trade classes** (names only; §7 details the people): court surveyor, itinerant chart-seller, engraver-publisher, instrument maker, colourer, map librarian.
6. **The cost ladder and the access filter.** Cost per copy, literacy, secrecy and scale together decide who sees the map. A map can be cheap to print and still restricted by law; a map can be expensive and public.
7. A **design lever**: pick the reproduction class before the map's politics — manuscript maps produce secrecy and copy-drift plots; printed maps produce editions, piracy and public argument.

Must not restate: the seven writing-surface families (`writing-media-surface-economy.md:3`); the textile or craft trade ladders (`craft-artisan-lexicon.md` §4); the trade-economy measure→money ladder (`trade-economy-lexicon.md`).

### §5 — The survey-to-symbol chain (C02)

This is the entry's technical spine and its longest section. Required:

1. **The chain diagram** (as a numbered list, not an image): question → survey → control network → projection → scale → drawing → symbol set → reproduction → use. Each arrow is a lossy transform; state what is lost at each.
2. **Instrument table.** Rows: pacing, rope and chain, groma, dioptra, astrolabe, compass, cross-staff, plane table, theodolite, triangulation. Columns: what it measures (distance / angle / position), precision class, typical error, what it cannot do, archaeological trace. Real anchors: the Roman *groma* (`architecture-settlement-lexicon.md:95`; Dilke `to-verify`), the plane table and theodolite (Snyder/Ptolemy shelf `to-verify`), the compass and the true-vs-magnetic distinction (`direction-symbolism.md:51`).
3. **Three survey modes:** linear (itinerary: distance and station), angular (triangulation: baseline + angles), positional (coordinates: latitude/longitude or grid). A map's form follows its survey mode; a portolan is linear/angular, a cadastral is positional/local, a cosmogram is neither.
4. **The error budget.** Closure error, scale error, orientation error, drafting error, reproduction error. The rule: errors compound; a map cannot show finer than its survey can measure at its scale, and a copy cannot be more accurate than its master.
5. **The control network.** Baseline, stations, monuments, benchmarks; the difference between a survey that closes and one that merely stops. The control network is the map's invisible warrant.
6. **Projection family table.** Rows: equirectangular, stereographic, Mercator, polar azimuthal, local plane. Columns: what it preserves (angle / area / distance / direction / none), what it distorts, typical use, signature failure. The rule: **no projection is neutral; choose the property to preserve and name the distortion.** Cite Snyder `(to-verify)`.
7. **Scale.** Representative fraction, scale bar, the smallest drawn unit; scale as a political decision (what is worth showing at this scale); the legend of the omitted. A map at 1:5,000 can show a terrace; a map at 1:5,000,000 cannot show a village.
8. **Symbolization.** Orientation (east/top, south/top, Mecca-centred, route-up, river-up), compass rose, north arrow, scale bar, legend, boundary line, blank, monster, vignette. The symbol grammar table: symbol / what it encodes / how it can lie / who can read it.
9. A **design lever**: choose the survey mode and the projection before drawing a single symbol; the rest of the map is downstream.

Must not restate: the castrum/city-plan lexicon (`architecture-settlement-lexicon.md:95`); the direction register (`direction-symbolism.md:51`); the timekeeping instrument families (`timekeeping-instruments.md:18-31`) — the survey instrument is a different instrument class, and the entry says so.

### §6 — Scarcity and prestige (C02)

Required:

- **The scarcity ladder:** unique manuscript → a few hand copies → printed edition → mass map. What each rung costs, who can own it, and what social relation it creates.
- **Prestige uses:** the map room, the gift map, the royal survey, the chart under lock, the captured chart, the map as an heirloom and as proof of a claim.
- **Restricted maps:** state secret, guild secret, pilot's chart, cadastral privacy, sacred/ritual map. Each has a different enforcement mechanism and a different failure mode.
- **The map as treasure and as evidence.** A map can be both; the plot is in the conflict.
- A **design lever**: scarcity is a design choice, not a default; decide who is excluded and what they do about it.

Must not restate: the `craft-artisan-lexicon` guild ladders; the `sumptuary-law-rank-display` assayability test (a map is not a dress, but the same "who may display" logic applies; cite, do not restate); the `trade-economy-lexicon` price ladder.

### §7 — The mapmaker trade (C02)

Required:

- **The workshop-chain table:** surveyor → draughtsman → engraver → printer → colourer → seller. Columns: skill / tools / pay / guild or office / signature or mark / failure mode. Not every culture has every role; the table is a menu.
- **Training and organization:** apprentice → journeyman → master; court office vs market workshop; hereditary atelier; the state survey office; the church scriptorium as a map workshop. Cite `craft-artisan-lexicon.md` §4 for the guild ladder, not restated.
- **The maker's mark and the signed map.** Why a map is signed; what a signature warrants; how a false signature is detected; the copy chain as provenance.
- **Patronage and employment.** Who pays for the survey, who owns the resulting map, and what the surveyor is allowed to publish. The patron's question is the map's first selection filter.
- A **design lever**: the trade's place in the workshop ladder predicts the map's politics — a court office produces official silence, a market workshop produces commercial noise.

Must not restate: the guild ladder and maker's-mark typology in `craft-artisan-lexicon.md` §4; the writing-media scriptorium economics; the trade-economy wage ladder.

### §8 — Provenance and charter (C02)

Required:

- **The authority warrant.** Four questions displayed in the cartouche: who made it, for whom, by what warrant, dated when. The cartouche is the map's title deed.
- **Charter and legal instrument table:** treaty map, cadastral register, tithe map, boundary map, colonial survey, court exhibit. Columns: who warrants it / what it claims / who can contest it / what happens when it is wrong.
- **Forgery and authentication.** Copy chain, anachronism, paper/ink/plate evidence, the altered copy; the map as a document that can be forged like a deed.
- **Colonial and living-tradition flags.** A survey map can be an instrument of dispossession; a sacred map can be restricted. Route every real-world case through `verification/real-world-inspiration-boundaries.md:2/:6` and `myth-consistency-gate.md:34`; do not fill restricted knowledge.
- A **design lever**: the warrant is part of the map; a map without a warrant is a rumor with a drawing.

Must not restate: the Mesoamerican provenance table (`mesoamerica-primary-sources.md:58`); the cosmography T-O disclaimer; the pilgrimage site typology.

### §9 — The container-name fossil (C02)

Required:

- **The word-layer table:** *map* (< Latin *mappa* "cloth/napkin"), *chart* (< Latin *carta* "paper"), *atlas* (< Atlas, the bound collection's frontispiece), *portolan* (< Italian *portolano*, a pilot book), *legend*, *scale*, *cartography*, *plan*, *plot*. Columns: word / source / what format it fossilizes / what it now means / the drift.
- **The container logic.** The word often names the *format* (sheet, book, roll, cloth) before it names the *content*; a culture that writes on cloth may call its maps "cloths", and the word survives the medium. This is a design lever for fictional lexicons.
- **Genre names as institutions.** "Atlas", "portolan", "itinerary", "cadastral register" are not neutral labels; each implies a format, a reader and a use.
- **Toponymy.** The replaced name, the dual name, the name taboo; a map is an archive of renamings (`naming-systems.md:70`). The entry owns the *map's* naming layer, not the general onomastic system.
- A **design lever**: choose the format and the word follows; or choose the word and it implies the format. Either way, do not let a modern generic word ("map") stand unexamined in a pre-modern culture.

Must not restate: the general toponymy in `naming-systems.md`; the writing-systems history; the language-contact loanword method.

### §10 — Build order (C03)

Nine steps, each with a deliverable and a failure mode:

1. Fix the question and the reader. *Deliverable:* one sentence. *Failure:* a map that answers every question answers none.
2. Fix the survey warrant and precision. *Deliverable:* who measured, by what instrument, to what error. *Failure:* a map finer than its survey.
3. Fix the control network. *Deliverable:* baseline, stations, closure rule. *Failure:* a survey that stops rather than closes.
4. Fix projection and scale. *Deliverable:* what is preserved, what is distorted, the smallest drawn unit. *Failure:* a projection chosen by habit.
5. Fix orientation and which north. *Deliverable:* the frame's up and the reason. *Failure:* a north arrow with no north.
6. Fix the symbol set and legend. *Deliverable:* the grammar and who can read it. *Failure:* symbols that only the author can decode.
7. Fix the medium and reproduction. *Deliverable:* master, copies, copy chain. *Failure:* a unique map with no provenance.
8. Decide the silences. *Deliverable:* what is omitted and why. *Failure:* an accidental blank read as ignorance.
9. Write the authority warrant and run the calibration audit. *Deliverable:* cartouche + §12 pass. *Failure:* a map that cannot say who made it.

Ends with: a **decision row** (DR-MAP-01 and DR-MAP-12 are the bookends).

### §11 — Worked micro-example (NON-CANON) (C03)

Use the **highland-valley irrigation cadastral map**, not the river-delta example at `sacred-topography-pilgrimage.md:132`. The deliberate difference: the sacred-topography example demonstrates a *shrine and route*; this one demonstrates a *map whose blank is a legal exemption*. The setting is a working label, every element is a design option, and the fragment must say so in its first and last sentence.

Required elements:

| element | the example's choice | what it demonstrates |
|---|---|---|
| question | "who holds water, and what is owed?" | the question fixes the cadastral form |
| survey | rope-and-sight chain along terrace walls; baseline on the main channel; no triangulation beyond the valley | survey precision limits the sheet |
| control | three stone benchmarks at channel junctions; closure by walking the loop | the control network is invisible but load-bearing |
| projection | local plane; no graticule; scale 1:5,000 | a local map can refuse the sphere |
| orientation | upstream at top; a flow arrow instead of a compass rose | orientation is a claim, not a convention |
| symbols | channels double lines; parcel boundaries dashed; temple land a blank with a hatched border | the symbol grammar encodes law |
| silence | the temple's exempt parcels are blank; the downstream hamlet is omitted because it pays no water tax | the blank is the most political mark |
| reproduction | parchment master; two cloth copies for the water court; one copy altered | the copy chain is a plot engine |
| warrant | a charter naming the surveyor, the water court, the year; the cartouche | authority is displayed, not assumed |
| dispute | the altered copy moves a boundary by one terrace | the map is an argument, and the argument is actionable |

Add a four-row table: **what the map shows / what it omits / what it claims / who can read it.** End with an explicit NON-CANON sentence and a boundary statement: this decides nothing about any world.

### §12 — Calibration bank (C03)

Eight rows minimum; each row has *claim / status / why / anchor / design consequence*. Status vocabulary is exactly `mainstream | contested | discredited | overclaim | category error`; no row may be unmarked.

| # | claim | status | why | anchor | design consequence |
|---:|---|---|---|---|---|
| 1 | "A map is a neutral, objective picture of space." | discredited | selection, projection, orientation and omission are constitutive; there is no view from nowhere | Harley 1989; Wood 1992; Monmonier (`to-verify`); §3 | every map must name its argument |
| 2 | "Medieval people believed the earth was flat; T-O maps prove it." | discredited | sphericity was standard learned opinion; T-O diagrams are symbolic, not survey maps | `cosmology-cosmography.md:102`; Russell 1991 (`to-verify`) | do not use a T-O diagram as evidence of flat-earth belief |
| 3 | "Portolan charts are photographically accurate." | overclaim | they are practical sailing charts with their own conventions, distortions and copy drift | Campbell 1987 (`to-verify` for page range) | use a portolan as a practical instrument, not a geodetic survey |
| 4 | "Indigenous maps are childlike or merely mental." | discredited | lienzos and cartographic histories are precise legal/territorial documents with their own conventions | `mesoamerica-primary-sources.md:58`; Mundy 1996; Boone 2000 (`to-verify`) | treat a lienzo as a legal document and a genre, not a failed modern map |
| 5 | "The map is the territory." | category error | a representation is not the thing; use it as a design lever, not a metaphysics | §3; Wood 1992 (`to-verify`) | the gap between map and ground is the plot |
| 6 | "Cartography diffused one-way from Europe." | contested | Chinese, Islamic, Mesoamerican and Polynesian traditions are independent or parallel; the diffusion story is uneven and often retrofitted | Needham 1959; al-Idrisi 1154; Mundy 1996 (`to-verify`) | allow multiple origins; do not stage a single "invention" |
| 7 | "Pre-modern maps are failed modern maps" (the primitive-map fallacy). | discredited | each map answers its own question with its own conventions; judging it by modern accuracy is a category error | Wood 1992; Jacob 1992/2006 (`to-verify`); §2 | judge a map by its question, not by a modern projection |
| 8 | "Mercator is simply wrong; one true projection exists." | overclaim | every projection preserves some properties and distorts others; Mercator serves navigation at the cost of area | Snyder 1987 (`to-verify`); §5 | choose the projection by the property the map must preserve |

**Living-practice flags** (a subsection, not a table row): restricted/sacred maps (songlines, ritual geography, initiation knowledge), colonial survey and cadastral maps of living peoples, and contested border maps. Rule: do not fill restricted knowledge to complete a table; mark an access boundary and choose a less extractive comparison (`verification/myth-consistency-gate.md:34`; `verification/real-world-inspiration-boundaries.md:2/:6`). A fictional map may borrow a *mechanism* (the blank, the restricted copy, the ritual orientation), not a community's specific restricted content.

### §13 — Decision record (C03)

Twelve rows, IDs `DR-MAP-01`..`DR-MAP-12` (the prefix is unused in the corpus: `grep -rn 'DR-MAP' corpus/knowledge/ | wc -l` → 0, measured this seat). Columns: ID / decision / reason / failure mode if skipped / section.

| ID | decision | reason | failure if skipped | § |
|---|---|---|---|---|
| DR-MAP-01 | Fix the question and the reader before the form | the question selects the form; form-first produces decoration | a beautiful map that answers nothing | §2, §10 |
| DR-MAP-02 | Declare the survey warrant and its precision; never draw finer than the survey | the sheet's authority is the chain behind it | a map that looks precise and is not | §5, §8 |
| DR-MAP-03 | Choose the control network and the closure rule | a survey that does not close cannot be checked | an error that propagates silently | §5 |
| DR-MAP-04 | Choose the projection and state what it preserves/distorts | no projection is neutral | a map read as if it had no distortion | §5 |
| DR-MAP-05 | Fix orientation and which north (true/magnetic/ritual) | orientation is a claim; the compass trap is real | the priests' north and the pilots' north disagree on the sheet | §5, §8 |
| DR-MAP-06 | Fix scale and the smallest drawn unit | scale decides what can be shown and what must be omitted | a village drawn at a scale that cannot hold it | §5 |
| DR-MAP-07 | Fix the symbol set and the legend's reader | a symbol only the author can read is not a map | an illegible or private code | §3, §5 |
| DR-MAP-08 | Decide the silences and who may notice them | omission is a constitutive act | an accidental blank read as ignorance | §3, §11 |
| DR-MAP-09 | Fix the medium and the reproduction chain | the copy chain is the map's provenance | a unique sheet with no authentication | §4, §6 |
| DR-MAP-10 | Write the authority warrant (maker, patron, date, charter) | a map without a warrant is a rumor with a drawing | an unattributable sheet, useless in court | §8 |
| DR-MAP-11 | Assign custody and access (public, archive, secret) | access is the map's politics | a secret map treated as public, or vice versa | §6, §8 |
| DR-MAP-12 | Run the calibration audit and mark every `(to-verify)` | the entry's external shelf is unverified this round | a page-level claim shipped as settled | §12, §14 |

Each row must cite its section; C03 must not add rows with no section anchor.

### §14 — Recheck triggers (C03)

A short numbered list, mirroring the head `- recheck:` field but expanded with the entry's specific traps:

1. Before printing any date (Hereford c. 1300, the Peutinger Table, Ortelius 1570, the Mercator atlas) or any map's "first" claim.
2. Before any precision, scale, distance or cost figure.
3. Before any etymology (*map*, *chart*, *atlas*, *portolan*, *legend*, *scale*, *cartography*).
4. Before any claim that a culture "invented" the map or that cartography diffused one-way.
5. Before treating a treaty/cadastral/tithe map as settled law or as a neutral record.
6. Before ranking a projection as "correct" or "wrong".
7. Before using a real tradition's restricted or sacred map; route through the verification entries.
8. Before inferring a real absence from a map's silence.

### §15 — Scope and handoff (C03)

Required:

- What the entry supplies: the register test, the map-form typology, the survey-to-symbol chain, the projection table, the symbol grammar, the material/reproduction classes, the scarcity ladder, the trade roles, the warrant table, the word layer, the calibration bank, the twelve decision rows, the build order, and the NON-CANON example.
- What it does not supply: any canon decision, any world bible fact, any clearance or promotion verdict, any permission to use restricted real-world material.
- Handoff target: lore-shokunin world bible — comparative data, tables and terminology candidates only; which map is canon, who owns it and what it claims is theirs to decide.
- Correction discipline: corrections are new sections or a new entry, never rewrites; every `(to-verify)` is a backlog row, not an assertion.

---

## 5. Boundary table — all seven K02-named neighbours

This table is the entry's §1 table. It must use the live line numbers below (re-read at `6e9a30d`), not K02's r44 line numbers where they differ. Every row has the same three-part shape: *it owns / this entry owns / does not restate*.

| # | neighbour | what it owns (live citation) | what this entry owns instead | does not restate |
|---:|---|---|---|---|
| 1 | `corpus/knowledge/myth-symbol/cosmology-cosmography.md` | the five world-model axes (`:2`); the T-O row and its disclaimer "symbolic, not survey maps" (`:71`); the flat-earth calibration "not cartographic claims" (`:102`); the geometry menu (`:75`); the J. Z. Smith built-expression test (`:42`) | the **survey map**: the measured, projected, reproduced sheet; cites the T-O disclaimer as its charter | the five-axis typology; the axis-mundi vehicle table; the flat-earth calibration; the geometry menu |
| 2 | `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` | the holy-site typology (`:5`); sacred-geography diagram geometries (`:57`); the three route types, fixed itinerary / votive ramble / circuit (`:69`); the build step (`:124`); the river-delta NON-CANON example (`:132`) | **how a route is measured and drawn**; cites the route types as content a map can carry | the site typology; the route-as-rite grammar; the votive economy; the river-delta example (deliberately not reused) |
| 3 | `corpus/knowledge/myth-symbol/direction-symbolism.md` | orientation frames; the true-vs-magnetic compass trap (`:51`); tawaf circuits (`:112`); grave orientation and procession routes (`:125`); qibla (`:132`) | the **map convention**: orientation choice, compass rose, north arrow, frame-up | the direction register; the direction-word etymology bank; the orientation typology |
| 4 | `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` | the city-plan lexicon; the Roman castrum grid, the groma sentence and "the grid is cadastral" (`:95`); the instrument + founding rite + claim word lever (`:101`) | **land survey as a map-production step**; cites `:95` and does not absorb the settlement vocabulary | the house/roof/threshold lexicon; the planning lexica; the castrum row's building content |
| 5 | `corpus/knowledge/culture-material/writing-media-surface-economy.md` | the seven surface families and the cost ladder (`:3`); the survivor's ledger; the medium as a legal instrument | **map-specific media and reproduction**: parchment/paper/cloth/copperplate; manuscript vs print; the atlas; plate wear and copy drift | the seven-family inventory; the three-price model; the archive commitment |
| 6 | `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` | the lienzo/cartographic-history source class and its provenance (`:28`, `:58`); the manuscript inventory | the **genre** as a map-form exemplar; cites the source class | the manuscript inventory; the provenance table; the copy-chain facts for the specific lienzos |
| 7 | `corpus/knowledge/culture-material/transport-mobility-lexicon.md` | routes and the maintenance institution (`:28`); the Qhapaq Ñan case (`:35`); DR-TR-02's maintenance clause (`:117`) | the **representation** of routes on a sheet; cites the maintenance rule | the four-layer mobility system; vehicle/draft vocabulary; the route institution itself |

Secondary couples (not in the seven-row boundary table, but in `- couples:`): `timekeeping-instruments.md:50` (longitude at sea), `trade-economy-lexicon.md`, `craft-artisan-lexicon.md` §4, `calendar-festival-systems.md`, `material-culture-inference-method.md`, `naming-systems.md:70`, `writing-systems.md`, `semantic-fields-lexicon-building.md`, `historical-linguistics.md`, `language-contact.md`, `polynesia-navigation.md:52,:63`, `japan-medieval-sengoku.md:157`, `real-world-inspiration-boundaries.md:2,:6`, `myth-consistency-gate.md:34`, `to-verify-triage-protocol.md:15`.

Boundary test for C08: no row may say "this entry owns" something already named in the neighbour's `- topic:` line. If a row's "owns" clause can be found in the neighbour's topic, the row is wrong and the drafter must narrow it.

---

## 6. Calibration bank — status vocabulary and the living-practice rule

The bank is §12 of the entry. Three rules bind it:

1. **Every row carries a status from the fixed vocabulary** (`mainstream | contested | discredited | overclaim | category error`) and a one-clause reason. "Some say" is not a status.
2. **No row is a straw man.** The discredited claims are the ones a worldbuilder is likely to repeat (neutral map, flat-earth T-O, primitive map, map=territory); the contested one (one-way diffusion) is genuinely contested, not settled in the other direction.
3. **Living-practice flags are separate from epistemic status.** A restricted map is not "discredited"; it is *restricted*. The entry must not use the calibration vocabulary to license extraction. The access rule is `myth-consistency-gate.md:34`.

C07's contract audit checks: at least the eight rows; every status in vocabulary; the living-practice subsection present; no external source presented as inspected; the `(to-verify)` count is honest.

---

## 7. Source shelf — tiers and audit obligations

The head block carries the shelf; this section states what each tier may claim.

| tier | contents | allowed claim | audit |
|---|---|---|---|
| **A — in-corpus anchors** | the `path:line` list in §3.1 | "re-read at the landing HEAD"; may be cited as the lane's authority | C06 re-resolves every path and line; a line that moved is a FAIL until re-cited |
| **B — inherited bibliography** | the standard works in §3.1 | author/year/title only; editions, volumes, page ranges are `(to-verify)` | C06/C12 check that every item carries `(to-verify)` and that no item is described as read, fetched, inspected or page-checked |
| **C — internal method/verification** | `real-world-inspiration-boundaries.md`, `myth-consistency-gate.md`, `to-verify-triage-protocol.md`, `material-culture-inference-method.md` | method and policy only; no historical fact | C07 checks the access-boundary rule is applied |

Specific obligations:

- The **charter citation** is `cosmology-cosmography.md:71` and `:102`. C06 must re-read both lines and quote them accurately; the entry may quote the phrases "symbolic, not survey maps" and "not cartographic claims".
- The **Smith/Wheatley/Needham registrations** are at `cosmology-cosmography.md:6`; the entry reuses them by path and does not re-register them as new sources.
- Every Tier B item that is not an in-corpus registration is `(to-verify)` for edition/page. The entry must not say "Harley argues..." as if a page was read; it says "Harley's argument, as the standard statement of the map-as-claim position (`to-verify`)".
- The shelf is **not** a bibliography dump: every item must be tied to a section that uses it, or removed. C12's check is "does each external item support a named claim, and is it marked?" not "is the list long?".
- No URL is required for the standard works; the corpus convention is author/year/title/edition (`to-verify`). A URL may be added only if it was fetched; none was.

---

## 8. Worked example — acceptance checklist for C14

C14 (non-author) judges the §11 example against this list; a FAIL on any line holds the landing until C03 repairs.

| check | pass condition |
|---|---|
| declared invented | first and last sentence say NON-CANON / working label; no real culture named as the example's parent |
| internal consistency | survey precision, scale, smallest drawn unit and what the map shows agree (no 1:5,000 map with a 1:50,000 omission rationale) |
| method exercised | all nine build steps visible: question, warrant, control, projection, orientation, symbols, medium, silence, authority |
| not a clone | does not reuse `sacred-topography-pilgrimage.md:132`'s river-delta shrine; the difference is stated |
| silence is load-bearing | the blank has a legal reason and a consequence, not decoration |
| authority is displayed | the cartouche/warrant is described and dated |
| no canon | the example decides nothing; it is a drill, not a world fact |
| length | 22-28 lines; a table plus prose, not an essay |

---

## 9. README revision 2.5 — exact landing arithmetic (C09)

C09 owns the draft; the integrator applies. The byte targets at `6e9a30d`:

| anchor | current | after |
|---|---|---|
| `corpus/README.md:5` | `revision: 2.4 — ...` | insert a new `revision: 2.5 — Round-47 culture-material expansion (2026-10-19): ...` block **above** it, naming the entry, the audits, `## culture-material/` 25 → **26**, totals 223 → **224**, vector `25/26/25/29/24/94 → 25/26/26/29/24/94`, and the sweep re-measure |
| `corpus/README.md:10-11` | `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**.` (sums 217) | `the vector 25/23/25/29/24/94 → **25/26/25/29/24/94**.` (sums 223) **plus** one correction sentence: "The rev-2.4 prose vector printed here originally read 25/23/26/25/24/94 (sum 217); corrected here to the measured pair." Do not delete the rev-2.4 block |
| `corpus/README.md:234` | `## culture-material/ (25)` | `## culture-material/ (26)` |
| between `:240` and `:241` | calendar row, then costume row | insert `- \`cartography-and-mapmaking.md\` — <canonical topic text>` in filename order |
| `corpus/README.md:544` | `Total knowledge entries: 223.` | `Total knowledge entries: 224.` |
| `corpus/README.md:546-548` | `Counts checked 2026-10-19 ...` / inventory command / `(total 223 files; directory totals 25/26/25/29/24/94).` | keep the date and command; change to `(total 224 files; directory totals 25/26/26/29/24/94).` |

Rules:

1. **Byte equality.** The row text after `` — `` must equal `topic_of()`'s output for the entry: the `- topic:` content stripped, continuation lines space-joined. The canonical string in §3 is a single physical line, so the row is a straight paste. No double spaces, no trailing space, no smart-quote substitution.
2. **Order of application.** Apply the README edits bottom-up (footer → totals → row → section header → revision block) or recompute anchors after each insertion; the new revision block shifts every later line.
3. **The rev-2.4 repair is a forward correction of a live index**, explicitly sanctioned by `claims.json:28` and the non-goal at `claims.json:64`; it is not an edit to a filed round.
4. **Do not touch** the duplicate H1 at `:1/:3`; report it as an observed anomaly. Do not "tidy" other rows.
5. **Expected sweep output after landing:** `parts` with `culture-material: 26`; `rows 224 files 224`; `missing_from_index 0 []`; `topic_mismatch 0 []`; `orphan_rows 0 []`; `header_drift {}`; `totals_line 224 totals_ok True`; footer `{"date": "2026-10-19", "total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}`; `footer_findings []`; exit 0. The README sha changes; C10 records the staged sha and V01 compares it to the live post-landing sha.

The vector arithmetic is independently checkable: `sum([25,26,25,29,24,94]) == 223` and `sum([25,26,26,29,24,94]) == 224`. C09 must print both sums in its fragment.

---

## 10. Verification plan — commands, expected outputs, and what each gate can and cannot see

### 10.1 Pre-landing (draft tree)

| gate | command | expected | what it does not prove |
|---|---|---|---|
| freshness | `test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md`; `find ... -iname '*cartograph*' ... \| wc -l`; `grep -rniE '^- topic:.*(cartograph\|mapmak\|portolan\|cadastr)' corpus/knowledge/ \| wc -l` | path absent; 0 filename owners; 0 strict topic owners | that the topic is not carried (K01's report handles the prior-round leg) |
| source audit | every backticked path resolved at HEAD; every cited line re-read | 100% resolve; no line drift | that the external shelf was page-checked (it was not) |
| contract audit | `python3 tools/gates/provenance-audit.py <entry>` | exit 0; no `FINDING`; `INFO to-verify-count` expected | content quality; the gate cannot judge whether a status is warranted |
| boundary | seven-row table present; each "owns" clause agrees with the neighbour's `- topic:` | 7/7 | that no second owner exists corpus-wide (A02/V01 grep) |
| couples | resolver over the `- couples:` line | every token resolves; no dangling path | that the coupling is meaningful |
| example | C14 checklist §8 | 8/8 | that the example is good fiction (it is a drill) |

### 10.2 Staged 224-tree sweep (C10), without writing in-tree

`sweep.py`'s CLI has no `--root`; `root_override` is a function argument (`reports/round-28/readme/sweep.py:119-122`). The safe staged method:

```bash
mkdir -p .scratch/r47-sweep
rm -rf .scratch/r47-sweep/corpus                # idempotent: never nest a second copy
cp -a corpus .scratch/r47-sweep/corpus          # disposable copy
# apply the draft entry + README rev 2.5 to .scratch/r47-sweep/corpus only
python3 -B - <<'PY'
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("sweep", "reports/round-28/readme/sweep.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
readme = pathlib.Path(".scratch/r47-sweep/corpus/README.md").read_text(encoding="utf-8")
r = m.sweep(readme, root_override=".scratch/r47-sweep/corpus/knowledge")
print(m.render(r)); raise SystemExit(0 if r["ok"] else 1)
PY
```

Expected: `rows 224 files 224`, `missing_from_index 0 []`, `topic_mismatch 0 []`, `orphan_rows 0 []`, `header_drift {}`, `totals_line 224 totals_ok True`, `footer_findings []`, exit 0. The lane's own selftest is separately green: `python3 -B reports/round-28/readme/sweep.py --selftest` → `selftest: 12/12 checks passed`.

This copy-based method is *not* an exception to the in-tree rule: it writes only under `.scratch`, and it never invokes a round runner. The ABSOLUTE rule forbids `reports/round-*/run-validation.py` in-tree; `claims.json`'s counting command that names `reports/round-47/run-validation.py` is the integrator's acceptance runner, not a seat command. Seats use the direct commands above.

### 10.3 Post-landing (V01)

```
find corpus/knowledge -name '*.md' | wc -l                 # 224
ls corpus/knowledge/culture-material/*.md | wc -l          # 26
python3 -B reports/round-28/readme/sweep.py                # rows 224 files 224; exit 0
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l   # exactly 1
git status --porcelain -- corpus/                          # A entry + M README only
```

Post-landing ownership: exactly one `- topic:` owner (the new entry); no other entry's topic may name cartography/mapmaking; `git status` must show no `M` on an existing entry and no second corpus file.

---

## 11. Risks, tripwires, and open items

| # | risk | evidence | mitigation / abort rule |
|---:|---|---|---|
| 1 | **"Carried topic" misreading.** A checker applies "no prior proposal anywhere" and rejects the claim because r44 K02 proposed cartography. | `reports/round-44/scout/K02-gap-scout.md:85`; `claims.json:26` names r44 K02 as the seed | use the definition in §1.3; K01 reports the seed explicitly and proves no *other* round proposed it; do not reject the claim on the seed |
| 2 | **Adjacency collision with cosmography.** A reviewer says the T-O row already owns maps. | `cosmology-cosmography.md:71` and `:102` explicitly disclaim survey maps | quote both lines in §1 and §2; C08 checks the boundary table; A02 checks one-owner |
| 3 | **Sacred-topography clone.** The worked example repeats the river-delta shrine. | `sacred-topography-pilgrimage.md:132` | use the highland-valley irrigation cadastral example; C14 checks the difference |
| 4 | **Low demand read as manufactured +1.** | tight demand 29/35 broad, 7/9 genuine | state the low demand honestly in `- gap filled:` and §1; frame it as a structurally named but unbuilt register, the r42 lithic precedent |
| 5 | **Source laundering.** An external work is described as read. | no network this round | every Tier B item `(to-verify)`; C06/C12 audit; no page quote |
| 6 | **README byte drift.** C04 changes the topic line after C09 cuts the row. | sweep compares exact text (`sweep.py:136-148`) | one canonical topic string in §3; C09 waits for C04's final line; C10 re-runs the staged sweep after any change |
| 7 | **Revision-block line shift.** C09 edits the top block first and then uses stale line numbers. | revision at `:5`; anchors at `:234,:544` | apply bottom-up or recompute; the plan's anchors are baseline anchors, not immutable |
| 8 | **Duplicate H1.** `corpus/README.md:1` and `:3` both carry the title. | observed this seat | report only; do not fix in this landing; the claim does not sanction it |
| 9 | **Census conflation with O.** O measures a 223-denominator census; C lands 224. | `reports/round-44/scout/K02-gap-scout.md:301-316` (K02 §5) | record C's +1 as a separate post-census delta; do not re-run O's census over 224 and present it as the same measurement |
| 10 | **Decision-row ID collision.** | `grep -rn 'DR-MAP' corpus/knowledge/ \| wc -l` → 0 | use `DR-MAP-01..12`; if a later seat adds a row, re-grep |
| 11 | **Over-length entry.** 15 sections plus tables can bloat. | comparable entries 140-201 lines | 260-320 line band; C11 flags outside; cut prose, not tables |
| 12 | **Restricted-material extraction.** A real sacred map is used as a design template. | `real-world-inspiration-boundaries.md:2,:6`; `myth-consistency-gate.md:34` | living-practice flags in §12; borrow mechanisms, not restricted content |

Open items (all `to-verify`, none blocking the plan):

- The exact page range for Campbell 1987 and the editions of al-Idrisi, the Peutinger Table, the Antonine Itinerary, Ortelius and Mercator are unverified; C04/C06 keep them `(to-verify)`.
- The claim's `counting_commands` names `python3 reports/round-47/run-validation.py`; the shared rules forbid running round runners in-tree. The integrator runs it; seats use the direct commands. This is a contract-execution note, not a defect in the claim.
- P01 §4.2 F0's "no prior proposal" wording needs the §1.3 correction at integration; otherwise K01's gate will fail on a true fact.

---

## 12. Handoff map (what each seat should take from this plan)

| seat | what to take | what not to do |
|---|---|---|
| **K01** | §1.3's four-part freshness statement; the r44-seed nuance; the exact commands in §10.1 | do not report "no prior proposal anywhere" |
| **K02** | the seed extract should confirm the slug, master claim, seven neighbours and the tiered shelf against §3-§7; current line numbers are in §5 | do not re-cite r44 line numbers if they moved |
| **C01** | §1-§4 skeleton; the seven-row boundary table; the map-form typology; the master claim | do not restate cosmography/pilgrimage/direction/architecture |
| **C02** | §5-§9 skeleton; the survey-to-symbol chain; the projection and symbol tables; the trade/warrant/word layers | do not duplicate §3's semiotics; §3 points forward to §5 |
| **C03** | §10-§15 skeleton; the build order; the highland-valley example; the eight-row calibration bank; `DR-MAP-01..12`; the recheck list | do not reuse the river-delta example; do not add decision rows without a section anchor |
| **C04** | the canonical head block in §3; the field order and the one-line topic rule | do not change the topic string after C09 cuts the row |
| **C05** | the four-part freshness statement; the target path and sort position; the "A not M" check | do not treat the r44 seed as carriage |
| **C06** | the Tier A anchors and the `(to-verify)` rule; the charter citation | do not let a Tier B item be described as read |
| **C07** | the QUALITY clause map: provenance, calibration, coupling, usability, canon hygiene | do not pass on the provenance gate alone |
| **C08** | the seven-row boundary table; the "owns clause vs neighbour topic" test | do not accept a row that restates the neighbour |
| **C09** | §9's byte targets; the canonical topic string; the rev-2.4 repair | do not delete the rev-2.4 block; do not touch the duplicate H1 |
| **C10** | §10.2's staged `.scratch` method; the expected sweep lines | do not run a round runner in-tree |
| **C11** | the evidence-chain checklist; the length band; the "no missing seat" rule | do not summarize a draft as landed |
| **C12** | the shelf tiers; the "each item tied to a claim" rule | do not reward a long bibliography |
| **C13** | the full `- couples:` candidate in §3.3; every token must resolve | do not treat `lore-shokunin` as a path |
| **C14** | §8's eight-check list | do not accept a decorative example |
| **W02** | target path, byte source = the assembled fenced entry, apply order (entry then README), sha pin | do not stage under `corpus/` |
| **R03 / X04** | the honest low-demand statement and the register test; judge method, not length | do not demand high demand for a structurally named gap |
| **A02** | the seven-row boundary and the one-owner grep | do not accept a second owner |
| **V01** | §10.3 post-landing commands | do not run before the integrator applies |

---

## 13. Cross-claim interfaces

- **O (freshness gate):** the C claim's `before` is expressible as typed probes and is a useful negative control: `count_eq(total, 223)`, `path_absent(corpus/knowledge/culture-material/cartography-and-mapmaking.md)`, `topic_owner_absent(cartograph|mapmak|portolan|cadastr)` → 0, `grep_absent(prior proposals excluding the r44 seed)`. If O's tool is pointed at `reports/round-47/claims.json`, it should report C **FRESH** at `6e9a30d`; this is a cross-check, not a substitute for K01/C05's human sweep.
- **Ca (calibration):** the loop-1 stale-premises defect is the reason C's `- gap filled:` must carry measured commands, not a bare "no owner". Ca's queue-successor should cite `claims.json:26` and this plan's §1.3.
- **Census ordering:** O's 223-denominator measurement and C's 224 landing are two measurements. Record C's +1 as a post-census delta; do not silently re-run O's census over 224 and present the numbers as the same measurement (`reports/round-44/scout/K02-gap-scout.md:301-316`, K02 §5).
- **README:** C's landing is the only corpus delta; O's tool and Ca's successor are non-corpus. The integrator applies C's entry and README in one change; no other seat writes under `corpus/`.

---

## 14. Self-audit — what this seat measured, what it did not

Measured this seat at `6e9a30d`:

- `git rev-parse HEAD`; `git status --porcelain`; total 223; culture-material 25; six-partition census; target path absent; filename owners 0; strict topic owners 0; broad topic hits 11; tight demand 29 files / 35 lines; sort position 5/6; README anchors `:5`, `:10-11`, `:234`, `:240-241`, `:544`, `:546-548`; `DR-MAP` collision 0; the seven neighbour paths resolve; the cited lines re-read: `cosmology-cosmography.md:6,41,42,68,71,75,102`; `sacred-topography-pilgrimage.md:5,57,69,124,132`; `direction-symbolism.md:51,112,125,132`; `architecture-settlement-lexicon.md:95,101`; `writing-media-surface-economy.md:3`; `mesoamerica-primary-sources.md:28,58`; `transport-mobility-lexicon.md:28,35,117`; `timekeeping-instruments.md:50`; `polynesia-navigation.md:52,63`; `japan-medieval-sengoku.md:157`; `naming-systems.md:70`; `real-world-inspiration-boundaries.md:2,6`; `myth-consistency-gate.md:34`; `to-verify-triage-protocol.md:15`.
- The r44 seed and its round status: `reports/round-44/scout/K02-gap-scout.md:85,378-388`; `reports/round-44/cov/C01-entry-draft.md:1`; the r44 `validation.json` existence; the global reports grep.

Not done this seat:

- No external source was fetched, resolved or page-checked (no network).
- No corpus byte was written; this file is the only write.
- No round runner was executed; no `reports/round-47/run-validation.py` was touched.
- The full per-line disposition of the 29-file demand set was not re-typed; it is carried from K02 §3.4 and spot-checked at the load-bearing lines above. C06 must re-read any line the draft actually cites.
- The secondary couples paths (`trade-economy-lexicon.md`, `craft-artisan-lexicon.md`, `calendar-festival-systems.md`, `material-culture-inference-method.md`, `writing-systems.md`, `semantic-fields-lexicon-building.md`, `historical-linguistics.md`, `language-contact.md`) were listed from the live partition, not each re-opened; C13 resolves them before landing.
- The duplicate H1 at `README.md:1/:3` is reported, not repaired.

## Owed

- **C04:** fill the head block from §3, re-run the gap sweep at the landing HEAD, and keep the canonical topic string byte-stable.
- **C05:** independently re-derive §1's four-part freshness statement and report the r44 seed explicitly.
- **C06:** re-read every Tier A anchor; keep every Tier B item `(to-verify)`.
- **C08:** apply the "owns clause vs neighbour topic" test to all seven rows.
- **C09:** apply §9 bottom-up, paste the canonical topic byte-equal, and print the two vector sums.
- **C10:** run the staged `.scratch` sweep and record the staged README sha.
- **Integrator:** apply the entry and README in one change; run the round runner outside the seat; file the post-landing V01.
- **P01 correction:** replace F0's "no prior proposal" gate with §1.3's four-part check at integration.

---

## Appendix — command transcript (trimmed, this seat)

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
No such file or directory
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ | wc -l
11
$ python3 - <<'PY'  # tight demand
... TIGHT DEMAND: files=29 lines=35
PY
$ ls corpus/knowledge/culture-material/ | grep -nE 'calendar|costume'
5:calendar-festival-systems.md
6:costume-semiotics.md
$ grep -n '## culture-material/\|Total knowledge entries\|Counts checked' corpus/README.md
234:## culture-material/ (25)
544:Total knowledge entries: 223.
546:Counts checked 2026-10-19 from the repo root:
$ grep -rn 'DR-MAP' corpus/knowledge/ | wc -l
0
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; totals 223; footer 25/26/25/29/24/94; exit 0
```

The sweep run above is the baseline measurement, not the post-landing state; C10's staged run is the acceptance measurement.
