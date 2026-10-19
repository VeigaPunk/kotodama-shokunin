# C08 — boundary audit: cartography entry vs the live partition

- Seat: C08 | role: verifier | claim: C | date: 2026-10-19
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (measured in this seat, `git rev-parse HEAD`)
- Audited bytes (current revision at rewrite time; sha256 pinned in this seat):
  - `reports/round-47/cov/C01-entry-a.md` — `a02031a4fdb5d083a4f136fef964e93bf1418aaa69dcb5e141e2b8c59844ca35` (sections 1–4)
  - `reports/round-47/cov/C02-entry-b.md` — `85085d24190e445558ea02e72b6b8f842bac520a495754151fd3308cbfe8d5a2` (sections 5–9)
  - `reports/round-47/cov/C03-entry-c.md` — `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5` (sections 10–15)
  - `reports/round-47/cov/C04-entry-header.md` — `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0` (head block)
- Out path: `reports/round-47/cov/C08-boundary.md` (this file)

**Verdict in one paragraph.** No second owner exists and none is created by the draft. The corpus has 0 cartography filename owners, 0 `- topic:` owners, and 29 files / 35 tight body hits that are all metaphor, verb, source-title, data handoff, or an explicit disclaimer; the proposed slug is unused and the entry lands as `A`, not `M`. The C01 §1.1 boundary table correctly dispositions all seven K02-named neighbours plus `naming-systems`: cosmology keeps the world model and the T-O symbolic diagram (not survey maps), sacred topography keeps the place register and route grammar, direction keeps the orientation register, architecture keeps the city-plan lexicon, writing media keeps the surface economy, Mesoamerica keeps the lienzo source class, transport keeps the route institution, and naming keeps toponymy. C02's secondary boundary notes (`C02:464-481`) extend the surface to craft-artisan, vessel-container, sacred-kingship and japan-sengoku, and those divisions are correct. **Divination is not a collision**: it owns the sign-reading technology, its §8 boundary table names no cartography, and the draft contains zero divinatory material. Two adjacencies remain absent from **both** boundary surfaces — **trade-economy-lexicon** (the legal-instrument/metrology edge) and **celestial-symbolism-calendars** (the star-chart form) — and one citation is wrong and asserted as "real": C02 anchors the guild ladder at `craft-artisan-lexicon.md:44`, which is the steel-grading row; the ladder is `:56-63`. The earlier cosmographic-row wording defect is resolved in the current revision (`C01:247`). These are P1 table-completeness and citation defects, not ownership collisions; §4 gives exact fixes and §6 the pass/fail checklist for the assembled entry.

---

## 1. Ownership test at HEAD `6e9a30d` (measured, not carried)

Commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

### 1.1 Census

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

The partition matches the claim's `before` (223; culture-material 25) and the C04 head block's `verified-at` line. `reports/round-44/cov/C05-collision.md:97-146` had already cleared this exact path as a collision test at r44; that is a collision clearance, not a gap proposal, so it does not make the topic carried.

### 1.2 Filename and slug ownership

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' -o -iname '*atlas*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '.../cartography-and-mapmaking.md': No such file or directory
$ grep -rniE '^#{1,4} .*(cartograph|mapmaking|portolan|cadastr|atlas|survey map|star chart|world map)' corpus/knowledge/
corpus/knowledge/linguistics/language-shift-obsolescence-revival.md:73:### 2.2 UNESCO (2003) / Atlas (2010): nine factors and six degrees
```

The single heading hit is the title of a UNESCO publication, not a map entry. **0 filename owners, 0 section-heading owners.**

### 1.3 Topic-line ownership

A narrow cartography-vocabulary topic probe returns **0**:

```
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|mappa|survey map|world map|atlas of)' corpus/knowledge/
0 owners
```

A deliberately wider probe (`map|chart|survey|topograph|itinerar|diagram|cosmogram|plan`) returns 13 topic lines. Every one is a metaphor, a verb, a register term, or an adjacent object — listed here so no hit is silently dropped:

| Entry:line | Matched term | Disposition |
|---|---|---|
| `civilizations/africa-primary-sources.md:2` | map | "a bounded **source map**" — metaphor for a source inventory |
| `civilizations/finnic-sami.md:3` | map | "gákti as an **identity map**" — metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | map | "a reference **map** for the four Mesoamerican bases" — metaphor; the entry owns the lienzo *source class* at `:58` |
| `culture-material/ritual-garments.md:3` | map | "the b.Arakhin 16a **atonement map**" — metaphor |
| `linguistics/dialect-register-consistency.md:3` | map | "a built **dialect map**" — a lect inventory, not a sheet |
| `linguistics/sacred-registers-liturgical-language.md:3` | map | "how ritual events **map** to the competences" — verb |
| `linguistics/sound-symbolism.md:3` | map | "the three-way **map** (arbitrariness / iconicity / systematicity)" — conceptual schema |
| `myth-symbol/direction-symbolism.md:3` | cosmogram | "the Mexica **cosmogram**" — a direction-register partition, owned there; not a survey sheet |
| `myth-symbol/number-symbolism.md:3` | survey | "a variance **survey**" — statistics, not land |
| `myth-symbol/plant-symbolism.md:4` | diagram | the flora register's own typology diagram — not cartography |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | map | "purity is … a **boundary map**" — the entry's master metaphor |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | diagram, itinerar | **nearest neighbour** — "sacred-geography **mapping** … as a diagram"; owns the place register and the route, not the survey-to-sheet chain (§2.4) |
| `synthesis/dialect-faction-map-workflow.md:2` | map | "**Map** dialect features … onto travel networks" — verb |

**Zero topic-line owners of cartography.**

### 1.4 Tight body sweep — 29 files / 35 lines, all dispositioned

```
$ # pattern: cartograph|mapmak|portolan|cadastr|mappae|mappa mundi|surveyor|theodolit|
  #          compass rose|graticule|hereford mappa|lienzos?|stick chart|star chart|
  #          world map|map of|maps of|drawn map
TIGHT files=29 lines=35
```

By class (35/35 lines accounted for; the four classes are exhaustive for this hit set):

| Class | Files:lines | Why it is not an owner |
|---|---|---|
| **Metaphor / verb** (23 lines) | `ancestral-puebloan:39`, `bali:189`, `china-qing:26`, `china-shang-zhou:37`, `japan-medieval-sengoku:99`, `nazca:105`, `persia-achaemenid:58`, `persia-sasanian:9,:105`, `zapotec-mixtec:158`, `zimbabwe-shona:20`, `agrarian-field-system-lexicon:94`, `bathing-and-body-hygiene:67`, `cuisine-food-lexicon:94`, `ritual-garments:22`, `politeness-taboo-euphemism:73`, `syntax-typology:89`, `animal-symbolism:75`, `myth-folktale-genres:76`, `number-symbolism:106`, `pantheon-archetypes:30`, `phonology-sanity-gate:28`, `verification-method-overview:204` | "map of languages / labor / sects / value nodes", "smell map", "feature map", "Map of every V token" (a dict), etc. No produced sheet, no survey, no map trade |
| **Explicit disclaimer** (3 lines) | `myth-symbol/cosmology-cosmography.md:71,:102`; `myth-symbol/direction-symbolism.md:26` | Cosmology says T-O diagrams are "symbolic, not survey maps" / "not cartographic claims"; direction says an in-world code is "never as a compass rose with a legend". These are the two partition files *disclaiming* the register this entry lands |
| **Data / handoff** (7 lines) | `civilizations/mesoamerica-primary-sources.md:28,:42,:46,:58`; `civilizations/japan-medieval-sengoku.md:157`; `culture-material/architecture-settlement-lexicon.md:95`; `civilizations/khmer-angkor.md:17` | Lienzo source class and provenance; Edo cadastral periodization caution; the Roman groma/cadastral sentence; a source title ("archaeological map") — each a handoff, not an ownership of map production |
| **Work title / bibliography** (2 lines) | `civilizations/finnic-sami.md:185` ("A Linguistic Map of Prehistoric Northern Europe"); `myth-symbol/mineral-stone-symbolism.md:9` (*Mappae Clavicula*, a recipe book) | Title false positives on `map` / `Mappae` |

All 35 lines were also read in context; none describes a survey, projection, drawing, reproduction or map-trade system as its subject. The tight count is reproducible and matches the r44 K02 scout's `files=29 lines=35` (`reports/round-44/scout/K02-gap-scout.md`, §3.4).

**No second owner at HEAD. The gap is still unowned at landing.**

---

## 2. Boundary surfaces — what the draft has, and what it misses

The draft has **two** boundary surfaces:

1. **Authoritative:** C01 §1.1 (`reports/round-47/cov/C01-entry-a.md:92-103`, 8 rows).
2. **Secondary:** C02's "Boundary notes (for C08/A02)" (`reports/round-47/cov/C02-entry-b.md:464-481`, 10 rows), which explicitly says "C01's §1 boundary table is the authoritative statement; this section only confirms that §§5-9 do not violate it" (`:481`).

The head block's `- couples:` (`C04-entry-header.md:159`) and scope line (`:162`), and C03 §15's boundary reminders (`C03-entry-c.md:249`), are supporting surfaces.

### 2.1 Authoritative table (C01 §1.1) — all seven K02 neighbours pass

| Neighbour | Owned object (draft's citation) | Draft clause | Audit |
|---|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | world-model axes; T-O as symbolic device (`:71,:102`); toponyms (`:133`) | "contrast case … owns the measured sheet; does not restate the five axes, the flat-earth calibration, or the cosmogram typology" (`C01:96`) | **PASS** — see §2.4 |
| `myth-symbol/sacred-topography-pilgrimage.md` | holy-site typology, route-as-rite, three route types (`:5,:69`) | representation of a route; the route grammar/site typology stay there (`C01:97`) | **PASS** — add `:57,:96,:98` (P2-2) |
| `myth-symbol/direction-symbolism.md` | orientation register, compass trap (`:51`) | sheet convention (rose, north arrow, graticule); does not re-own the register (`C01:98`) | **PASS** — add `:26` (P2-3) |
| `culture-material/architecture-settlement-lexicon.md` | city-plan lexicon, castrum grid, groma (`:95`) | land survey as map-production step; no settlement vocabulary restatement (`C01:99`) | **PASS** |
| `culture-material/writing-media-surface-economy.md` | seven surface families, cost ladder (`:3`) | map-specific media/reproduction; no surface-family restatement (`C01:100`) | **PASS** |
| `civilizations/mesoamerica-primary-sources.md` | lienzo/cartographic-history source class (`:58`) | the genre as a map form; no manuscript-inventory restatement (`C01:101`) | **PASS** |
| `culture-material/transport-mobility-lexicon.md` | route and maintenance institution (`:28`), DR-TR-02 (`:117`) | how a route is drawn; no transport re-ownership (`C01:102`) | **PASS** |
| `linguistics/naming-systems.md` | toponymy, critical toponymy (`:40,:70,:97`) | toponym layer of the sheet; name derivation/taboo stay there (`C01:103`) | **PASS** — add `:118,:136` (P2-4) |

### 2.2 Secondary notes (C02) — craft, vessel and sacred-kingship are covered there

C02's boundary notes disposition ten neighbours (`:470-479`). The additions beyond the C01 table are:

| Neighbour | C02 note | Audit |
|---|---|---|
| `culture-material/craft-artisan-lexicon.md` | "§7.3 cites `:44`/`:76-87`; §9.4 cites `:3`; no guild taxonomy restated" (`:475`) | **Clause correct, anchor wrong** — `:44` is not the ladder (P1-2) |
| `culture-material/vessel-container-lexicon.md` | "§9 cites `:71` as the **method precedent**; the measure→money chain is not restated" (`:476`) | **PASS** — §9 applies the fossil method to map words, not vessel words |
| `myth-symbol/sacred-kingship-mythic-charter.md` | "§8.2 states the legal/mythic split explicitly" (`:479`) | **PASS** — but the row is only in the secondary surface; promote it (P2-1) |
| `civilizations/japan-medieval-sengoku.md` | "§8.6 cites `:157` as the calibration precedent" (`:478`) | **PASS** — screen |

Still absent from **both** surfaces: `trade-economy-lexicon.md` and `myth-symbol/celestial-symbolism-calendars.md` (P1-3, P1-4).

### 2.3 Divination — **NOT a collision**

Evidence, measured:

- `myth-symbol/divination-omen-systems.md:3` — the topic is the question → technique → closed sign space → licensed reader → prescription system, with a fourteen-row technique typology. **No cartography, mapmaking, survey, projection, or map-trade term.**
- Its own §8 boundary table (`:147-159`) names seven neighbours — celestial omens, cosmology, motif index, ritual liminality, naming, the myth-consistency gate, civilization bases — and **does not name cartography**, for the same reason: a reading is not a made sheet.
- The only `map` in the file is the verb in the worked example: "the code **maps** to twelve prescriptions" (`:163`). A precise grep for `divinat|geomanc|\bomen` across the four fragments returns **0**.
- The nearest conceptual overlap is geomancy (`ʿilm al-raml`, `:189`) and feng-shui siting, but those are *reading technologies*: the divination entry owns the sign code and the licensed reader, architecture owns the siting/plan, and cartography owns the sheet. If a later revision adds "a map used as a divination instrument", the sentence belongs to divination's §8 (`:147-159`); it must not be presented as map production.

**Ruling: not a second owner, not a collision, no entry clause strictly required** (the draft contains no divinatory material). A one-line non-collision note is optional (P3-1).

### 2.4 Cosmology — **T-O is symbolic; the survey sheet is unowned**

The claim's named boundary is correct and measured at three lines:

- `cosmology-cosmography.md:27` — cosmography is "the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage)". This is the definition that could be read as owning maps; read with the next two lines, it owns the *world model's* drawn form.
- `:71` — "Hereford Mappa Mundi c. 1300; T-O diagrams are **symbolic, not survey maps** (§10)".
- `:102` — "T-O diagrams are symbolic devices, **not cartographic** claims".

C01 §1.1 `:96` quotes the disclaimer and disclaims the five axes, the flat-earth calibration and the cosmogram typology. That is the correct division. The earlier §4.1 wording ("cosmography owns this form") has been **replaced** in the current revision: `C01:247` now says "anything measured — it makes no survey claim; the form belongs to `cosmology-cosmography.md` and is cited here as the contrast case, never restated". The entry does not restate the world-model content; C03 §10 (`:103`) uses the form only as a production row ("a projection statement and a doctrinal warrant … it is not a survey map"). **Resolved**; the residual P3-2 asks for "content/typology belongs" rather than "form belongs", which is a wording precision, not an ownership defect.

---

## 3. Second-owner test, corpus-wide

| Test | Result | Evidence |
|---|---|---|
| Filename owner | 0 | §1.2 |
| `- topic:` owner | 0 narrow; 13 wide hits all non-owners | §1.3 |
| Section-heading owner | 0 | §1.2 |
| Tight body vocabulary | 29 files / 35 lines, all by-product or disclaimer | §1.4 |
| Proposed slug unused | yes | `ls` → No such file |
| Entry lands as `A` | yes | path absent; C05-freshness §7 reached the same result (`C05-freshness.md:160`) |
| Sort position | between `calendar-festival-systems.md` (5) and `costume-semiotics.md` (6) | `ls corpus/knowledge/culture-material/` (1–12 listing) |
| Second owner created by draft | no | every dispositioned neighbour keeps its object; the remaining defects are omissions (trade, celestial) and a wrong anchor (craft), not absorption |
| Carried topic | no | r44 K02 §3.6; r44 collision clearance `C05-collision.md:97-146`; zero prior proposals in `reports/round-*/` outside the r44 seed chain |

**No collision to report.** The entry does not overwrite, absorb, or duplicate any existing topic. The defects below are table-completeness and citation defects, which the integrator should fix before the C landing because the boundary table is the entry's one-owner evidence.

---

## 4. Findings — exact locations and fixes

### P1 (must fix before assembly; the boundary table is the one-owner evidence)

**P1-1 — RESOLVED: cosmographic row.** The prior wording "cosmography owns this form" is gone. Current `C01:247` reads "anything measured — it makes no survey claim; the form belongs to `cosmology-cosmography.md` and is cited here as the contrast case, never restated". No action required for ownership; see P3-2 for a wording polish.

**P1-2 — craft ladder citation is wrong, and the draft's own citation audit certifies it as real.**
`reports/round-47/cov/C02-entry-b.md:267` anchors the standard apprentice → journeyman → master ladder at `corpus/knowledge/culture-material/craft-artisan-lexicon.md:44`. Line `:44` is the steel material-grading row (`tamahagane`, `kawagane`/`shingane`, `hada` …), not the ladder. The ladder is at `:56-63` (Germanic, London, Ottoman, Persianate, Chinese, Japanese, Indian, non-guild rows) and the overview is the topic line `:3`; the marks typology is `:76-87` (heading at `:76`). The error is repeated and certified in three more places:
- `C02:440` — citation audit table: "`:44` | workshop ladder table (apprentice → journeyman → master; masterpiece) | **real**". This is false; `:44` is grading.
- `C02:475` — boundary notes repeat "§7.3 cites `:44`/`:76-87`".
- `C04:127` and `C04:159` — the head block says craft "owns … the material-grading vocabulary — `:44`" and calls it the workshop register; `:44` supports the grading half only.
Fix: cite `:3,:56-63` for the ladder, keep `:44` only for material grading, keep `:76-87` for marks. The boundary clause itself is correct; the anchor is not.

**P1-3 — no trade-economy row in either boundary surface.**
C01 §3.6 (`C01:209-214`) and C02 §8.2 (`C02:313-319`) develop the map as a legal/territorial instrument; the head block cites `trade-economy-lexicon.md:92,:121` (Exchequer stock/foil, split-object authentication) in couples (`C04:159`), but neither the authoritative C01 table nor C02's boundary notes mention trade. Add a row: *trade owns measures and their sacred standardization, money-words, contract/debt vocabulary and split-object authentication (`:3,:49,:92,:121`); this entry owns the map as a legal/territorial instrument and the scale bar's declared unit, not metrology.* Without the row, the entry's "the map is a legal instrument" section has no declared metrology boundary.

**P1-4 — no celestial-symbolism row, although the draft owns a star-chart form.**
C01 §2.1 includes a `star chart` row (`C01:132`: "map of a non-terrestrial referent — the test is ground-indexed, not earth-indexed"), §4.1 includes a `Celestial / star chart` form (`C01:246`), and C02 §5.4 uses star charts as a stereographic case (`C02:101`). `myth-symbol/celestial-symbolism-calendars.md` owns constellations/asterisms (`:70`), the planet-as-god chain (`:53`), and the sky-as-calendar machinery (`:136`), but is cited **nowhere** in the four fragments (grep for the path: 0). Add a row: *celestial symbolism owns the sky objects, constellation naming, planet-god identities and calendar mechanics (`:70,:136`); this entry owns the star chart as a produced document and does not restate the sky typology.* This is the one genuinely unmarked adjacency introduced by the draft's own form typology.

### P2 (should fix; strengthens the strongest textual overlaps and the single-surface rule)

**P2-1 — promote craft and sacred-kingship rows to the authoritative table.**
C02's boundary notes cover craft (`:475`) and sacred-kingship (`:479`), but C01 §1.1 is declared authoritative (`C02:481`) and omits both. Add the two rows there (and add sacred-kingship to the head block's couples line, which currently omits it). This is a consistency fix, not a new ownership claim.

**P2-2 — pilgrimage anchors.** `C01:97` cites `:5,:69`. Add `:57` ("Once the sites are named, they form a map"), `:96` ("Sacred geography as a diagram — and the era drift of a holy map") and `:98` ("The map is a claim"). These are the literal textual overlaps; the clause is right, the anchors are under-specified. The draft's `C01`–`C03` never develop the three route types or the six drift mechanisms — checked: no `fixed itinerary / votive ramble / circuit` definition outside citations (only `C01:97` and the anchor table at `C01:336`), and no `revelation/translation/conquest/reform/neglect/invention` list.

**P2-3 — direction anchor.** `C01:98` cites `:51` (compass trap). Add `:26`: direction's standing rule says an in-world direction code is "never as a compass rose with a legend" — that is the disclaimer that licenses this entry's ownership of the rose/north arrow as **map convention**, not emic direction code.

**P2-4 — naming anchors.** `C01:103` cites `:40,:70,:97`. Add `:118` (toponym layer: "stratify the map") and `:136` ("the map's official names are canon decisions owned by lore-shokunin") — both are map-adjacent and confirm naming owns the names, not the sheet.

**P2-5 — vessel citation mismatch.** The couples line cites `vessel-container-lexicon.md:115` (containers as documents/chronometers), while C02 §9's fossil argument uses `:71` (the ear/lug container-name fossil; `C02:368`) and C02's boundary note correctly cites `:71` (`:476`). Add `:71` to the couples surface and a screen row: *vessel owns container-name families and the container-as-document/chronometer case; this entry owns map-word fossils and map storage as a boundary use, not container vocabulary.* No restatement: §9 applies the fossil logic to **map** words (mappa, charta, atlas, portolan, cartouche), not to vessel words.

**P2-6 — polynesia anchor.** `C02:92` correctly cites `:52` for the chartless boundary; the stick-chart row at `C01:133` marks it a boundary case but cites no owner. Add `:60` ("A mental bearing framework, not a chart showing the canoe's absolute position") and a screen row: navigation owns the operations; this entry owns the chart as a document; the Marshallese stick chart is a boundary case with living-practice flags routed to `verification/real-world-inspiration-boundaries.md:6` (C03 §12 already does this at `C03:215`).

**P2-7 — screened, no table row required.** `timekeeping-instruments.md:50` (longitude), `material-culture-inference-method.md:69,:76` (survival/anti-determinism), `writing-systems.md:117,:149,:156` (media bias), `japan-medieval-sengoku.md:157` (periodization caution) are all cited in couples and used as handoffs; none is at restatement risk. The table may list them in a "cited, not at risk" footnote.

### P3 (record only)

**P3-1 — divination.** Not a collision; the draft contains no divinatory material. If the integrator wants the mission's named non-collision visible in the entry, add one sentence to §1.1: *"Divination (`divination-omen-systems.md`) owns the sign-reading technology; a map used as a divination instrument is a reading, not map production."* No table row is required.

**P3-2 — cosmographic wording polish.** `C01:247` says "the form belongs to `cosmology-cosmography.md`". Prefer "the **content and world-model typology** belong to cosmology; this entry owns only the sheet's production as a contrast case". The current wording is conservative and creates no second owner; the polish prevents a later reader from thinking the form itself is out of scope while the entry's §4.1 and build order include it.

**P3-3 — heading sweep.** The only `Atlas` heading in the corpus is `linguistics/language-shift-obsolescence-revival.md:73`, a UNESCO publication title. No action.

---

## 5. Required boundary rows (fenced; integrator/C11 may merge into C01 §1.1)

P1 rows are required; P2 rows are recommended to keep one authoritative surface; the last row is the optional non-collision note. Paths are relative to `corpus/knowledge/culture-material/` for culture-material files; the rest carry the partition prefix.

````markdown
| `culture-material/trade-economy-lexicon.md` | measures and their sacred standardization (`:3,:49`), contract vocabulary and split-object authentication (`:92,:121`) | the map as a **legal/territorial instrument** and the scale bar's declared unit. Metrology and contract grammar stay there |
| `myth-symbol/celestial-symbolism-calendars.md` | constellations and asterisms (`:70`), planet-as-god identities (`:53`), the sky-as-calendar machinery (`:136`) | the **star chart as a produced document** (observation, projection, print). The sky typology and calendar mechanics stay there |
| `culture-material/craft-artisan-lexicon.md` | the workshop register, seven guild/workshop systems, the apprentice→journeyman→master ladder (`:3,:56-63`), the six-type mark taxonomy (`:76-87`) | the **map trade's** roles, products, customers and licensing. This entry cites the ladder and the mark types and does not restate them (`:44` is the material-grading row, not the ladder) |
| `myth-symbol/sacred-kingship-mythic-charter.md` | the **mythic charter** of rule and the royal register (`:3`) | the **legal charter** — the document that legitimates a claim to ground; the two charters' disagreement is a plot engine |
| `myth-symbol/divination-omen-systems.md` | the sign-reading technology: question → technique → closed sign space → licensed reader (`:3`; boundary at `:147-159`) | **no object taken** — a map used as a divination instrument is a reading, not map production; the draft contains no divinatory material (non-collision note) |
````

---

## 6. Pass/fail checklist for the assembled entry

Run on the assembled `corpus/knowledge/culture-material/cartography-and-mapmaking.md` before it is filed. Each clause is pass/fail; a fail is a boundary defect, not a style note.

| # | Clause | Pass condition | Test |
|---|---|---|---|
| B1 | K02 seven-neighbour set | each of `cosmology-cosmography`, `sacred-topography-pilgrimage`, `direction-symbolism`, `architecture-settlement-lexicon`, `writing-media-surface-economy`, `mesoamerica-primary-sources`, `transport-mobility-lexicon` appears with an "owns / does not restate" clause | `grep -c '<name>' ENTRY` ≥ 1 for each; read the row |
| B2 | Cosmology | quotes `:71`/`:102`; no restatement of the five axes, world-shape table or flat-earth calibration; the cosmographic row says **content vs production** (P3-2) | `grep -nE 'five (independent )?(design )?axes\|layer-count\|world-shape\|age-doctrine' ENTRY` → only inside a "does not restate" clause |
| B3 | Sacred topography | cites `:5` and at least one of `:57,:96,:98`; no route-type or drift-mechanism restatement | `grep -nE 'fixed itinerary\|votive ramble\|circuit / circumambulation' ENTRY` → cited as content, not defined |
| B4 | Direction | cites `:51` and `:26`; compass rose is a map convention, not the emic direction code | `grep -nE 'Levinson\|intrinsic/relative/absolute\|wuxing.*direction' ENTRY` → absent |
| B5 | Architecture | cites `:95`; no castrum/cardo/decumanus or settlement-vocabulary restatement | `grep -nE 'castrum\|cardo\|decumanus' ENTRY` → only as a citation |
| B6 | Writing media | cites `:3`; no seven-surface-family list | `grep -nE 'seven surface families\|clay and wax\|papyrus and parchment' ENTRY` → only inside a citation |
| B7 | Transport | any named route carries the maintenance citation `:28,:117`; no route/vehicle typology | `grep -nE 'DR-TR-02\|maintenance clause' ENTRY` → present where routes are drawn |
| B8 | Mesoamerica | lienzo cited to `:58`; no provenance inventory restatement | `grep -nE 'Quauhquechollan\|Tlaxcala\|Coixtlahuaca' ENTRY` → only in the exemplar cell |
| B9 | Naming | cites `:70` and one of `:118,:136`; no toponym derivation pipeline restatement | `grep -nE 'substrate names\|commendatory layer\|name taboo' ENTRY` → absent |
| B10 | Craft | cites `:3,:56-63` for the ladder and `:76-87` for marks; **not** `:44` for the ladder; no ladder restatement | `grep -nE 'apprentice.*journeyman.*master' ENTRY` → followed by the craft citation |
| B11 | Trade | cites `:3`/`:49` for measures and `:92`/`:121` for split-object; no metrology history | `grep -nE 'talent\|shekel\|metre\|standardization' ENTRY` → only as a citation |
| B12 | Celestial | cites `:70`/`:136`; no constellation/planet/calendar typology restatement | `grep -nE 'constellation\|Pleiades\|planet-as-god\|Milky Way' ENTRY` → only as a citation |
| B13 | Sacred kingship | the mythic/legal charter division is present with `:3` | `grep -nE 'mythic charter\|legal charter' ENTRY` → present |
| B14 | Divination | no collision; if any divinatory material appears, it cites `:147-159` | `grep -nE 'divinat\|geomanc\|omen' ENTRY` → 0, or a citation |
| B15 | No second owner | 0 filename/topic owners at landing; entry is `A`; no existing file overwritten | re-run §1.2–§1.4 (`find`/`grep`/`ls`) on the post-landing tree; `git status --porcelain` shows one new file + README only |
| B16 | Single boundary surface | C01 §1.1 and C02's boundary notes agree on every neighbour; no row exists only in the secondary surface | `diff` the neighbour sets from the two tables; every name in one appears in the other or in the couples line |

Re-run command template (from the lane root, with a staged entry path in `$ENTRY`):

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
ENTRY=corpus/knowledge/culture-material/cartography-and-mapmaking.md
for n in cosmology-cosmography sacred-topography-pilgrimage direction-symbolism \
         architecture-settlement-lexicon writing-media-surface-economy \
         mesoamerica-primary-sources transport-mobility-lexicon naming-systems \
         craft-artisan-lexicon trade-economy-lexicon celestial-symbolism-calendars \
         sacred-kingship-mythic-charter divination-omen-systems; do
  printf '%-40s %s\n' "$n" "$(grep -c "$n" "$ENTRY")"; done
find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' | wc -l
grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
```

Expected: every name ≥ 1 in the boundary/couples surface; filename/topic owners 0 before the landing; 1 after (the new file itself).

---

## 7. Limits and provenance

- The audited bytes are the **fenced draft fragments** C01–C04 at the sha256 values above, not an assembled corpus entry. The fragments were revised by their authors during this audit; the values above are the current revision, and all line references in this report were re-checked against it. An earlier revision had different bytes and a different §4.1 cosmographic wording; that finding is recorded as resolved in P1-1 rather than silently dropped. All `path:line` citations were spot-checked against HEAD `6e9a30d` in this seat; only the citations named in §4 failed or under-specified.
- No external source was fetched (no network); Tier B works remain `(to-verify)` and are outside this seat's boundary remit (C06/C12).
- The ownership counts in §1 are measured at HEAD `6e9a30d` on 2026-10-19, not copied from the r44 scout. The tight count (29/35) reproduces K02's; the wide topic count (13) differs from K02's 11 because this probe includes `cosmogram`, `diagram` and `plan`; every extra hit is dispositioned in §1.3.
- C05-freshness explicitly defers the boundary adjudication to this seat (`reports/round-47/cov/C05-freshness.md:302`); §2–§6 answer that deferral.
- This seat wrote only this file. No corpus file, no filed round, no instrument was modified. The fenced rows in §5 are integration material, not a staging under `corpus/`.

---

## Appendix — command transcript (trimmed)

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' \
      -o -iname '*cadastr*' -o -iname '*atlas*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
No such file or directory
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|mappa|survey map|world map|atlas of)' corpus/knowledge/
0 owners
$ # tight body sweep
TIGHT files=29 lines=35
$ # topic-line wide probe
13 hits, table §1.3
$ # per-line anchors checked in this seat (examples)
corpus/knowledge/myth-symbol/cosmology-cosmography.md:71  "symbolic, not survey maps"
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102 "not cartographic"
corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:57  "they form a map"
corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:96  "Sacred geography as a diagram"
corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:98  "The map is a claim"
corpus/knowledge/myth-symbol/direction-symbolism.md:26  "never as a compass rose with a legend"
corpus/knowledge/myth-symbol/direction-symbolism.md:51  "compass trap"
corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95  "surveyed with the groma ... cadastral"
corpus/knowledge/culture-material/writing-media-surface-economy.md:3   seven surface families
corpus/knowledge/culture-material/transport-mobility-lexicon.md:28,:117  route maintenance
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58  lienzos / cartographic histories
corpus/knowledge/linguistics/naming-systems.md:70  "a map is an archive of coups"
corpus/knowledge/culture-material/craft-artisan-lexicon.md:44  steel grading (NOT the ladder)
corpus/knowledge/culture-material/craft-artisan-lexicon.md:56-63  guild ladder rows
corpus/knowledge/myth-symbol/divination-omen-systems.md:147-159  §8 boundary; no cartography row
corpus/knowledge/myth-symbol/divination-omen-systems.md:163  "the code maps to twelve prescriptions" (verb)
$ # current draft shas (rewrite-time revision)
a02031a4... C01-entry-a.md
85085d24... C02-entry-b.md
4b699e06... C03-entry-c.md
cb5a7489... C04-entry-header.md
```

**Bottom line for the integrator:** land the C entry; it creates no second owner and divination is clean. Before filing the C evidence chain: add the two missing P1 rows (trade, celestial) to the authoritative C01 §1.1 table; fix the `craft-artisan:44` ladder anchor in C02 §7.3, C02's citation audit (`:440`), C02's boundary notes (`:475`) and C04 (`:127`, `:159`); and promote the craft and sacred-kingship rows from C02's secondary notes into C01's authoritative table so there is one boundary surface. Then re-run B1–B16 on the assembled entry. The two strongest textual overlaps — cosmology's "drawn (maps)" definition at `:27` and sacred topography's "holy map" section at `:96-98` — are already correctly disclaimed; adding the P2 anchors makes the disclaimers checkable rather than asserted.
