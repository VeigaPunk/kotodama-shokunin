# K02 — cartography seed extraction and the culture-material entry contract

- Seat: K02 | role: scout | claim: C | date 2026-10-19
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`; `git status --porcelain` → only `?? reports/round-47/`
- Out path: `reports/round-47/scout/K02-seed-extract.md` (this file)
- Mission: read `reports/round-44/scout/K02-gap-scout.md`'s cartography seed; extract its recommended slug, section outline, master claim, boundary table, and tiered source shelf; report the entry contract requirements for a culture-material entry.

**Result in one line:** the r44 K02 seed is sound and still true at this round's baseline — the target path is absent, the topic has 0 filename and 0 topic-line owners, and the live census is 223 total / 25 culture-material. Recommended landing: `corpus/knowledge/culture-material/cartography-and-mapmaking.md`, culture-material 25 → 26, total 223 → 224. The seed's ten-section skeleton is the authoritative outline; **the r47 executor missions (C01–C03) do not match it** — see §9, a real integration defect that must be reconciled before drafting.

---

## 1. Baseline measured at write time (not carried from r44)

All commands run from the lane root on 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|mappa|survey map)' corpus/knowledge/ | wc -l
0
$ grep -rniE '(cartograph|mapmaking|portolan|cadastr|mappa)' reports/round-45 reports/round-46 --include='*.md' --include='*.json' | wc -l
0
```

- Partition split measured by `ls … | wc -l`: civilizations 94, culture-material 25, linguistics 25, myth-symbol 26, synthesis 29, verification 24 (sum 223). The seed's r44 reading (`K02-gap-scout.md:12-31`) is unchanged at this HEAD.
- Sort position, simulated by sorting the directory with the new name inserted: index 5 (0-based) — `calendar-festival-systems.md` → **`cartography-and-mapmaking.md`** → `costume-semiotics.md`. This is the same slot the seed claimed (`K02-gap-scout.md:219`), and the same one a byte-sorted README section requires.
- No r45/r46 report proposes cartography; the r44 non-carriage evidence (`K02-gap-scout.md:195-209`) remains the freshness record. K01 owns the independent landing-time re-check; my §1 is the seed-extraction cross-check, not a substitute for K01.

## 2. Recommended landing (extracted, `K02-gap-scout.md:211-227`)

| Field | Seed recommendation | Live check at 6e9a30d |
|---|---|---|
| Partition | `culture-material/` — a made object system with a production chain and a vocabulary, not a workflow (`:213-223`) | partition exists, 25 files |
| Filename | `cartography-and-mapmaking.md` | absent (A, not M); slug unused |
| Sort position | between `calendar-festival-systems.md` and `costume-semiotics.md` | confirmed at insertion index 5 |
| Count effect | culture-material 25 → **26**; total 223 → **224** | live 25 / 223 |
| README | revision 2.5 with one new row, section header 25 → 26, totals 223 → 224, footer `25/26/25/29/24/94` → `25/26/26/29/24/94` | live rev 2.4; anchors in §8 |

The partition rationale is explicit in the seed and should be preserved in the entry's boundary section: `culture-material` over `synthesis` (the map is an object and a trade, not a workflow), over `myth-symbol` (symbolic space is already owned by cosmography, sacred topography and direction; the missing object is the instrument and the sheet), and over `linguistics` (toponymy and legend grammar couple to `corpus/knowledge/linguistics/naming-systems.md` but are not the system).

## 3. Master claim (verbatim, `K02-gap-scout.md:230-232`)

> *a map is an argument about space, not a picture of it — its authority comes from the survey chain behind it, and its politics from what it omits.*

The seed decomposes the map into four load-bearing choices, which the entry should use as its spine:

1. **what is measured** — survey precision;
2. **what is preserved** — projection and scale;
3. **what is drawn** — selection and symbolization;
4. **who may copy and read it** — reproduction and access.

The second sentence of the claim fixes the typology's logic: *the form follows the question, not the era* — itinerary for the traveller, cadastral for the tax office, portolan for the pilot, cosmographic for the temple, thematic for the reformer. This is the anti-progress-ladder rule and must survive drafting: a map-form table sorted by century would be the exact defect the claim rules out.

## 4. Section outline (extracted, `K02-gap-scout.md:234-247`)

The seed's ten sections, each required to end in a design lever or a decision row (`corpus/QUALITY.md:15-17`). Reproduced here as the binding skeleton for the drafters.

| # | Section | Content the seed assigns | Terminating artifact |
|---|---|---|---|
| 1 | The map's question | what the map is for: navigation, taxation, ownership, pilgrimage, cosmology, war, memory, propaganda; the question fixes the form | design lever: fix the question before the form |
| 2 | Map-form typology | itinerary/strip; cadastral/land register; chorographic/regional; portolan/nautical; celestial/star chart; cosmographic/world diagram; thematic; the cartographic history/lienzo; one real exemplar per form | typology table |
| 3 | The survey chain | pacing, rope and chain, groma, dioptra, astrolabe, compass, cross-staff, plane table, theodolite, triangulation; line vs angle vs position; error budget; control network | rule: a map shows only what the survey can measure at its scale |
| 4 | Projection and scale | sphere-on-plane; equirectangular, stereographic, Mercator, polar azimuthal, local plane; what each preserves and distorts; scale as a political decision; the legend of the omitted | comparison table + decision row |
| 5 | Drawing and symbolization | orientation (east/top, south/top, Mecca-centred, route-up), compass rose, scale bar, legend, boundary, blank, monster, vignette; the map as a text to be read | symbol-grammar table |
| 6 | Reproduction and the map trade | manuscript vs woodblock vs copperplate vs lithography; cost per copy; the atlas as a commercial product; state monopoly, pirate copy; the map as a legal instrument (treaty map, cadastral register, tithe map) | cost/reproduction table |
| 7 | The map's silences | the unnamed village, the path that is not a road, the omitted sacred site, the replaced toponym; the blank as a licence; Harley/Wood on the map as a claim | silence inventory + decision row |
| 8 | Calibration bank | six rows, §7 below | labelled table (mainstream / contested / discredited) |
| 9 | Build order | (1) question and reader; (2) survey precision; (3) projection/scale; (4) orientation; (5) symbol set and legend; (6) medium and reproduction; (7) silences; (8) authority claim (who made it, for whom, by what warrant); (9) calibration audit | numbered build order |
| 10 | Decision record + NON-CANON worked example | e.g. a river-delta culture's tax map: rope-and-groma survey, cadastral parcels, the blank where temple land is exempt, orientation to the river's flow, a cloth copy, the dispute it settles | `DR-CM-01..` rows + declared-invented example |

**What the entry must NOT do** (seed, same section): restate the cosmography five-axis typology; restate the pilgrimage route types; restate the direction register; restate the city-plan lexicon; restate the seven writing surfaces; restate the Mesoamerican provenance table; become a general history of cartography with no decision surface.

## 5. Boundary table — seven neighbours, live-verified

The seed's table is at `K02-gap-scout.md:181-193`. I re-read every cited line at HEAD 6e9a30d; the quotations below are the live text, not the seed's paraphrase.

| Neighbour | What it owns, with live evidence | The new entry's boundary |
|---|---|---|
| `corpus/knowledge/myth-symbol/cosmology-cosmography.md` | the five world-model axes; the T-O diagram as a symbolic device. `:71` (T-O row): "T-O diagrams are symbolic, not survey maps (§10)"; `:102`: "T-O diagrams are symbolic devices, not cartographic" | owns the **survey map** — measured, projected, reproduced sheet. Cites the T-O row as the contrast case; does not restate the world-model typology or the flat-earth calibration |
| `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` | the holy-site typology and the route-as-rite. `:5` topic line: "the place register of a fictional culture's symbolic grammar — the holy-site typology … the route as rite" | owns **how the route is measured and drawn**; uses the route types as map content; does not re-own pilgrimage |
| `corpus/knowledge/myth-symbol/direction-symbolism.md` | orientation frames and the true-vs-magnetic compass trap. `:51`: "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic … (declination)" | owns the **map convention** (orientation choice, compass rose, north arrow); cites `:51`; does not restate the direction register |
| `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` | the city-plan lexicon and the Roman survey step. `:95`: castrum grid "surveyed with the **groma** … The grid is **cadastral**" | owns **land survey as a map-production step**; cites `:95`; does not restate settlement vocabulary |
| `corpus/knowledge/culture-material/writing-media-surface-economy.md` | the seven surface families and the cost ladder. `:3` topic line: "the surface economy of inscription … the seven surface families" | owns **map-specific media and reproduction** (parchment/paper/cloth/copperplate; manuscript vs print; the atlas); cites the surface economy, does not restate it |
| `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` | the lienzo / cartographic-history **source class** and provenance. `:58`: "Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) … Cloth maps/migration-conquest accounts" | cites the genre; does not restate the manuscript inventory or its provenance table |
| `corpus/knowledge/culture-material/transport-mobility-lexicon.md` | routes, maintenance and the mobility system. `:28`: "a route is only real if someone maintains it"; `:117` (DR-TR-02): require a maintenance clause for every named route | owns the **representation** of routes; cites the maintenance rule; does not re-own route engineering |

Two more seed dispositions that are **not** collisions and should be recorded as such in the draft's boundary section: `civilizations/japan-medieval-sengoku.md:157` (a periodization caution about Edo cadastral maps, not a cartographic treatment) and `civilizations/polynesia-navigation.md:52-74` (navigation operations explicitly distinguished from a chart). `culture-material/timekeeping-instruments.md:50` ("longitude at sea") is one table cell in a timekeeping entry.

## 6. Tiered source shelf (extracted, `K02-gap-scout.md:249-286`)

**No external work below was fetched, opened, or page-checked at seat time** (no network this round). Author/year/title are the seed's confident bibliographic level; every edition, volume and page range is `(to-verify)` at authoring, and every direct quotation must carry that mark inline (`corpus/QUALITY.md:5-8`).

### 6.1 Tier A — already registered in-corpus (reuse, cite by path:line)

| Source | In-corpus registration |
|---|---|
| Smith (1987), *To Take Place*; Wheatley (1971), *The Pivot of the Four Quarters* | `cosmology-cosmography.md` `- sources:` block (critique of universal-centre claims) |
| Needham (1959), *Science and Civilisation in China*, vol. 3 | `cosmology-cosmography.md` `- sources:` (gaitian/huntian/xuanye; Kaogongji) |
| Horowitz (1998), *Mesopotamian Cosmic Geography* (BM 92687) | `cosmology-cosmography.md` `- sources:` |
| Russell (1991), *Inventing the Flat Earth* | `cosmology-cosmography.md:102` |
| Egeria, *Itinerarium*; Petrarch, *Itinerarium*; Ibn Jubayr, *Riḥla*; Ibn Baṭṭūṭa, *Riḥla* | `sacred-topography-pilgrimage.md:167-168` (editions already `to-verify` there) |
| Rykwert (1976); Kostof (1991); Steinhardt (1990) | `architecture-settlement-lexicon.md:95-97` |
| The [LIEN] lienzo record (UFM Quauhquechollan) and the cartographic-history row | `mesoamerica-primary-sources.md:28,58` |
| Navigation sources (horizon compass, star sequence, latitude) | `polynesia-navigation.md:52-74` |
| Surface-economy sources (media, cost, reproduction) | `writing-media-surface-economy.md:3` and its `- sources:` block |

### 6.2 Tier B — the thirteen named external works

| # | Work (as the seed gives it) | Use in the entry | Status |
|---|---|---|---|
| 1 | Harley, J. B., & Woodward, David (eds.), *The History of Cartography*, 6 vols. in 7, University of Chicago Press, 1987–2022 | standard reference; vol. 1 (1987) portolan and medieval; vol. 3 (2007) European Renaissance | `(to-verify)` volumes/pages |
| 2 | Harley, J. B. (1989), "Deconstructing the Map," *Cartographica* 26(2): 1–20 | the map-as-claim argument (§7 silences; calibration row 1) | `(to-verify)` pages |
| 3 | Wood, Denis (1992; 2nd ed. 2010), *The Power of Maps*, Guilford Press | the map as an argument; selection and omission | `(to-verify)` edition |
| 4 | Monmonier, Mark (1991; 3rd ed. 2018), *How to Lie with Maps*, University of Chicago Press | symbolization and deliberate distortion | `(to-verify)` edition |
| 5 | Jacob, Christian (French 1992; Eng. trans. 2006), *The Sovereign Map*, University of Chicago Press | the map as a sovereign instrument; long-run theoretical frame | `(to-verify)` translator/pages |
| 6 | Ptolemy, *Geography*, trans. Berggren & Jones (2000), Princeton University Press | the projection/coordinate tradition (§4) | `(to-verify)` book/chapter locators |
| 7 | Campbell, Tony (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *The History of Cartography*, vol. 1 | portolan accuracy calibration (§8 row 3) | page range `(to-verify)` |
| 8 | Kain, Roger J. P., & Baigent, Elizabeth (1992), *The Cadastral Map in the Service of the State*, University of Chicago Press | cadastral form; the tax office's map | `(to-verify)` pages |
| 9 | Mundy, Barbara E. (1996), *The Mapping of New Spain*, University of Chicago Press | indigenous cartography / lienzos as legal documents | `(to-verify)` pages |
| 10 | Boone, Elizabeth Hill (2000), *Stories in Red and Black*, University of Texas Press | pictorial histories and the lienzo genre | `(to-verify)` pages |
| 11 | Pickles, John (2004), *A History of Spaces*, Routledge | cartographic reason and the geo-coded world | `(to-verify)` pages |
| 12 | Snyder, John P. (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395 | projection families and their distortions (§4 table) | `(to-verify)` section numbers |
| 13 | Dilke, O. A. W. (1971), *The Roman Land Surveyors*, David & Charles | the groma/centuriation chain (§3) | `(to-verify)` pages |

The seed's shelf also names three works beyond the thirteen and they should not be silently dropped: Edson (2007), *The World Map, 1300–1492*, Johns Hopkins UP; Buisseret (ed.) (1992), *Monarchs, Ministers, and Maps*, University of Chicago Press; al-Idrisi, *Nuzhat al-mushtāq* (1154), edition/translation `(to-verify)`. Primary-text shelf, all editions `(to-verify)`: the *Tabula Peutingeriana* and the *Antonine Itinerary*; Ortelius, *Theatrum Orbis Terrarum* (1570); Mercator's atlas.

## 7. Calibration bank (extracted, `K02-gap-scout.md:288-298`)

The entry must flag each row with a status label (`corpus/QUALITY.md:9-12`). Six rows:

| Claim | Status | Why (as seeded) |
|---|---|---|
| "A map is a neutral, objective picture of space" | **discredited** | selection, projection, orientation and omission are constitutive (Harley 1989; Wood 1992) |
| "Medieval people believed the earth was flat; T-O maps prove it" | **discredited** | sphericity was standard; T-O diagrams are symbolic, not survey maps — verified live at `cosmology-cosmography.md:102`; Russell 1991 |
| "Portolan charts are photographically accurate" | **overclaim** | practical sailing charts with their own distortions and conventions (Campbell; page-level `to-verify`) |
| "Indigenous maps are childlike or merely mental" | **discredited** | lienzos and cartographic histories are precise legal/territorial documents (Mundy 1996; Boone 2000) |
| "The map is the territory" | **category error** | a representation, not the thing; a design lever, not a metaphysics |
| "Cartography diffused one-way from Europe" | **contested** | Chinese, Islamic, Mesoamerican and Polynesian traditions are independent or parallel (Needham; al-Idrisi; Mundy) |

## 8. Entry contract for a culture-material entry

This is the executable contract, assembled from the gates and the live house style rather than from memory. It has three layers: **gate-hard** (a landing that misses these fails an executable check), **round-audit** (the r19/r35 audit shape), and **house style** (observed in the most recent landings; a reviewer expects it, the gate does not enforce it).

### 8.1 Gate-hard fields

| Contract leg | Requirement | Executable source |
|---|---|---|
| `- topic:` | present, non-empty; the README row text must equal it **byte-for-byte** after the row marker. Continuation lines are space-joined on both sides, so line wraps are free but wording is not | `tools/gates/provenance-audit.py:75` (FIELD_NAMES), `reports/round-28/readme/sweep.py:61` (`TOPIC_RE`), `:74-83` (`topic_of`), `:136-147` (mismatch class `REWRITE`) |
| `- sources:` | present and non-placeholder; at least one source bullet carrying a locator (year, backticked repo path, URL, or sha) | `provenance-audit.py:75`, finding list `:99-104`; `reports/round-19/audit/entry-audit.py:49-72` (`source_locators`), `:125-134` (`quality_bar`) |
| `- couples:` | present and non-empty; every backticked `.md` target resolves against the entry's directory, the lane root, or `corpus/knowledge/` | `provenance-audit.py:75`; `entry-audit.py:74-97` (`couples_targets`), unresolved list is a fail |
| Calibration vocabulary | at least one calibration word/shape anywhere (heading, table column, bold label, labelled line) | `provenance-audit.py:99-104`, `:268-281` (`calibration_apparatus`) |
| `verified-at` + `recheck`/`source` | the audit tail check: `verified-at` present **and** (`recheck` or `source`) present | `entry-audit.py:108` |
| Gap named | a frontmatter gap field, an inline gap clause, or a body heading naming the gap | `entry-audit.py:26` (`GAP_RE`), `:120` |
| Decision record | a `decision record`/`decision table` heading or a `DR-XX-NN` id | `entry-audit.py:27` (`DECISION_RE`), `:121` |

Note on the live partition: seven older culture-material entries omit `couples` (e.g. `calendar-festival-systems.md`, `cuisine-food-lexicon.md`, `era-periodization-models.md`), so the gate is applied at landing, not retroactively. The new entry must satisfy the full triple; "the neighbours predate the gate" is not a licence.

### 8.2 Head-block shape (house style; `timekeeping-instruments.md:1-9` is the fullest exemplar)

```
# <Title> — <subtitle naming the system and its parts>

- topic: <one paragraph; README row must be byte-equal>
- gap filled: <measured absence sweep: command, date, HEAD, counts; every near-miss dispositioned>
- sources: <Tier A in-corpus by path:line; Tier B external with editions to-verify>
- source: <the measured authority for the gap statement; state the no-network limit>
- couples: <each target with a parenthetical boundary; handoff target>
- verified-at: <ISO date> — <HEAD>; what was checked and what was not
- recheck: <the triggers that would change the entry>
- scope: reference knowledge and craft method only; no canon; ends at the handoff
```

Field census across the 25 live culture-material entries (first 14 lines each): `topic` and `sources` are universal; `couples` is 18/25; `verified-at` 15/25; `recheck` 12/25; a gap field appears as either `- gap filled:` (4) or `- gap:` (5); `- source:` and `- scope:` appear in the recent full-profile entries. The round-audit shape requires the gate-hard triple **plus** the tail; the remaining fields are the house profile and should be carried.

### 8.3 Body contract (QUALITY.md, 5 clauses)

| Clause | Requirement | `corpus/QUALITY.md` |
|---|---|---|
| Provenance | every factual claim sourced; unverifiable claims inline `(to-verify)`; invented sources are a conformance defect | `:5-8` |
| Calibration | every framework entry states mainstream / contested / discredited with reason; pop-mythography flagged on first use | `:9-12` |
| Coupling | `- couples:` names the systems/files connected; an entry that couples nothing must say so | `:13-15` |
| Usability | decision tables, typology tables, checklists, worked examples; no essays | `:16-17` |
| Canon hygiene | no entry decides what is true in any world; ends at the handoff | `:18-20` |

Observed body conventions in the recent landings, which the draft should match: a §1 that states **what the entry owns and where siblings stop**; numbered sections that each end in a design lever or decision row; a calibration bank with status labels; a `DR-<TAG>-NN` decision record; a numbered build order; a **NON-CANON** worked micro-example declared invented; a final handoff section naming lore-shokunin and the open `(to-verify)` items. The tag for this entry should be new and unique — `CM` collides with no live culture-material tag seen in the partition scan; the seed's example rows `DR-CM-01..` are the intended form (`K02-gap-scout.md:245`).

### 8.4 README revision 2.5 — exact anchors and arithmetic

Live `corpus/README.md` at HEAD (575 lines):

| Line | Current bytes | Required change |
|---|---|---|
| `:5` | `revision: 2.4 — Round-42 myth-symbol expansion …` | a new revision 2.5 block above it naming the r47 cartography landing and the re-measurement |
| `:11` | "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**" | **pre-existing defect**: this vector sums to **217**, not 223; repair to the correct pre-landing `25/26/25/29/24/94` (sums 223) and the post-landing `25/26/26/29/24/94` (sums 224) |
| `:234` | `## culture-material/ (25)` | `## culture-material/ (26)` |
| `:240-241` | `calendar-festival-systems.md` row, then `costume-semiotics.md` row | insert the new row between them, in filename order |
| `:544` | `Total knowledge entries: 223.` | `Total knowledge entries: 224.` |
| `:548` | `(total 223 files; directory totals 25/26/25/29/24/94)` | `(total 224 files; directory totals 25/26/26/29/24/94)` |

Arithmetic checked by command: `25+23+26+25+24+94 = 217`; `25+26+25+29+24+94 = 223`; `25+26+26+29+24+94 = 224`.

The sweep's acceptance legs (`reports/round-28/readme/sweep.py:136-210`) are stricter than the totals line alone: **rows == files** per section, 0 missing, 0 ghosts, 0 duplicate rows, 0 topic mismatches, declared section header count == file count, totals line == total files, and the footer's date/command/total/directory vector all agree. The footer directory order is `PARTS` order — linguistics, myth-symbol, culture-material, synthesis, verification, civilizations — which is why the live footer reads `25/26/25/29/24/94` and the post-landing must read `25/26/26/29/24/94`.

### 8.5 Partition landing rules

- The landing is a **new file** (`A`), never a modification of an existing entry; the only other corpus delta is `corpus/README.md`. The seed's collision check (`K02-gap-scout.md:347-351`) is the template: enumerate the partition, confirm the slug unused, confirm the sort slot, confirm no second owner.
- One topic, one owner: the boundary table in §5 is the ownership statement, not decoration. The two explicit disclaimers in cosmography (`:71`, `:102`) are the load-bearing proof that the survey-map register is unowned.
- The entry is drafted under `corpus/` **only as a fenced block in the seat's out path**; the integrator applies it (round rule; `targets.json` shared_rules). No seat stages under `corpus/`.

## 9. Integration defect: the r47 executor missions describe a different entry

The round's C executor missions are:

- `targets.json:21` (C01): "sections 1-4: frame + **the property that makes a map a register** + **the map-meaning mechanisms** + **material/trade classes**";
- `targets.json:22` (C02): "sections 5-9: the survey-to-symbol chain + **scarcity/prestige** + **the mapmaker trade** + **provenance/charter** + **the container-name fossil**";
- `targets.json:23` (C03): "sections 10-15: build order + worked micro-example + calibration bank + decision record + recheck + scope".

Those phrases are the **r42 lithic-register skeleton**, not the cartography seed. The exact wording appears in `reports/round-42/cov/C01-entry-1.md:53` ("the property that makes stone a register at all … the four stone-meaning mechanisms (material property → metaphor, provenance → charter, scarcity → rank, and the container-name fossil) … the eight material classes"), with the container-name fossil defined at `:44` and `:138`. The cartography seed has **no** "container-name fossil", no "material/trade classes", and a **ten**-section outline, not fifteen.

**State at my write cut (measured, not predicted).** C01 did not copy the skeleton literally; it adapted it to cartography — `cov/C01-entry-a.md` §1 frame/boundary, §2 "what makes a map a register — the five-condition test" (`:109`), §3 "the map-meaning mechanisms — six decisions before a line is drawn" (`:152`), §4 "material and trade classes — the map-object typology" (`:232`). C03 likewise maps its §10–15 onto the seed's build order, worked example, calibration bank and decision record (`cov/C03-entry-c.md:73,107,154,189`), adding §14 recheck and §15 scope. C03's own header warns that its § numbers are an assumption tied to the target text and must be reconciled at assembly (`C03-entry-c.md:10`). C02 had not filed at my cut.

So the defect is **not** "lithic filler has landed"; it is a **fifteen-section adaptation of a ten-section seed whose §5–9 mission still names the lithic content**. The assembly check is concrete: confirm that C02's §5–9 actually contains (a) the survey chain, (b) projection and scale, (c) drawing and symbolization, (d) reproduction and the map trade, and (e) the map's silences — the five sections the seed makes load-bearing (`K02-gap-scout.md:234-247`). If the literal mission list ("scarcity/prestige, mapmaker trade, provenance/charter, container-name fossil") crowds those five out, the assembled entry will lose the seed's spine and fail its own "what the entry must NOT do" list. **Recommendation:** the reviewer/planner re-cut C02's brief against the seed before assembly; if the fifteen-section shape is kept, seed §3–5 maps to C02 §5–7 and seed §6–7 to C02 §8–9. This is my recommendation, not a filed decision; the integrator owns it.

A second, smaller mismatch: the seed's §4.3 lists ten sections while C03's mission assigns "sections 10-15" and names "recheck + scope" as body sections — in the house style those are **head-block fields**, not sections (`timekeeping-instruments.md:6-9`). C03 drafted them as §14/§15; at assembly they should collapse into the head block rather than survive as duplicate body sections.

## 10. Risks and handoff

1. **Low raw demand, stated honestly.** The seed measures 29 files / 35 lines with the broad pattern, but only 7 files / 9 lines of genuine cartographic vocabulary, several of them disclaimers (`K02-gap-scout.md:138-179`). The gap is a *named-but-unbuilt register*, the same shape as the r42 lithic gap; the draft's `- gap filled:` must say so rather than inflate the count. This is the r43 lesson applied.
2. **Adjacency is the main collision risk and it is answerable.** `cosmology-cosmography.md:71/:102` — verified live — is the single most load-bearing citation: the partition explicitly disclaims survey maps. Quote it; do not restate the five-axis typology.
3. **Sources.** No external work was fetched or page-checked at seat time. Tier B is record-level only; every page, volume, edition and quotation carries `(to-verify)`. The draft must not present an unread work as inspected.
4. **Counts.** The landing arithmetic is 223 → 224 and culture-material 25 → 26; the README footer vector must be `25/26/26/29/24/94`. The rev-2.4 prose vector's 217 sum is a pre-existing defect, repaired forward in 2.5, not a rewrite of a closed round's filed bytes.
5. **For K01/C05:** re-run the ownership sweep at the landing HEAD; my §1 is a cross-check at 6e9a30d, and freshness must be re-verified at the commit the integrator actually lands on.

## Owed

- none for this seat. The extraction is complete; the only `to-verify` items are the Tier B editions/pages and the Campbell page range, which belong to the drafters/auditor. The executor-mission mismatch in §9 is reported to the integrator/planner, not absorbed.

## Citations

- Seed: `reports/round-44/scout/K02-gap-scout.md` — §1 baseline `:12-31`, claim `:93-95`, filename test `:97-112`, topic test `:116-136`, demand `:138-179`, boundaries `:181-193`, non-carriage `:195-209`, recommendation `:211-227`, topic seed `:224-228`, master claim/outline `:230-247`, shelf `:249-286`, calibration `:288-298`, README anchors `:301-318`.
- Contract: `corpus/QUALITY.md:3-23`; `tools/gates/provenance-audit.py:75,99-104,268-281`; `reports/round-19/audit/entry-audit.py:25-27,49-72,74-97,99-135`; `reports/round-28/readme/sweep.py:61-64,74-83,136-210`.
- House style: `corpus/knowledge/culture-material/timekeeping-instruments.md:1-9`; `corpus/knowledge/culture-material/furniture-interior-lexicon.md:1-9`; `corpus/knowledge/culture-material/bathing-and-body-hygiene.md:1-10`.
- Boundary lines re-read live at 6e9a30d: `myth-symbol/cosmology-cosmography.md:71,102`; `myth-symbol/sacred-topography-pilgrimage.md:5`; `myth-symbol/direction-symbolism.md:51`; `culture-material/architecture-settlement-lexicon.md:95`; `culture-material/writing-media-surface-economy.md:3`; `civilizations/mesoamerica-primary-sources.md:58`; `culture-material/transport-mobility-lexicon.md:28,117`.
- Mismatch evidence: `reports/round-47/targets.json:21-23`; `reports/round-42/cov/C01-entry-1.md:44,53,138`.
