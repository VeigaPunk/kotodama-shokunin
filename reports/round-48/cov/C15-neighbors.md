# C15 — neighbor-disposition verification (claim C)

- Seat: `C15` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`)
- Out path: `reports/round-48/cov/C15-neighbors.md` (this file)
- Non-author statement: I drafted no cartography bytes, in r47 or r48. Every judgement below is from filed bytes plus commands I ran at the baseline. I wrote only this file, and nothing under `corpus/`.

**One-line verdict.** All seven of K02's named neighbours are **dispositioned and extended, not restated**, in the r47 boundary table, and I found **no scope bleed** into any neighbour's owned territory. Six of the seven rows are clean as written. The seventh — cosmography — has **one blocking omission**: the row cites the T-O disclaimers at `:71`/`:102` but not the competing definition at `cosmology-cosmography.md:27` ("how the world is drawn (maps)"), so the entry's "no entry owns the made map" claim reads as an over-claim against the neighbour's own text (R03's B8, independently confirmed at live HEAD). One drain on the boundary vocabulary (`C02:70`) and three small over-promises are logged as P3. **For r48: the draft fails C15 if the cosmography row again omits `:27`.**

---

## 1. What existed to verify at my write cut

```
$ ls reports/round-48/
claims.json  targets.json  telemetry/
```

No r48 draft bytes exist yet. The only filed cartography bytes are r47's four fragments (`reports/round-47/cov/C01-entry-a.md`, `C02-entry-b.md`, `C03-entry-c.md`, `C04-entry-header.md`). This seat therefore does two things:

1. **Audits the r47 boundary table** — the reference implementation of the disposition duty — against the live corpus, row by row, including a restatement/bleed scan of the body.
2. **Files the binding 7-row spec** (§6) that the r48 draft must carry, so the r48 draft's own C15 check is decidable without re-deriving the neighbour registry from K02.

The audit is valid at r48 HEAD because **the corpus did not change** between the r47 draft baseline `6e9a30d` and our baseline `a01405d`:

```
$ git diff --name-only 6e9a30d..a01405d -- corpus/ | wc -l
0
$ git diff --stat 6e9a30d..a01405d -- corpus/ tools/ | tail -2
 tools/harness/claims-freshness.py | 2717 +++++++++++++++++++++
```

The only delta in range touching `corpus/` or `tools/` is the freshness gate; no knowledge entry moved. Every `path:line` reading below was taken live at `a01405d`, not copied from r47.

### 1.1 The registry — and a seed count-word defect

`reports/round-44/scout/K02-gap-scout.md:183` reads:

> The new entry must **couple to, not restate**, these **five**:

but the table it introduces runs **seven** rows, `K02-gap-scout.md:187-193`:

| # | Neighbour named by K02 | K02 line |
|---|---|---|
| 1 | `myth-symbol/cosmology-cosmography.md` | `:187` |
| 2 | `myth-symbol/sacred-topography-pilgrimage.md` | `:188` |
| 3 | `myth-symbol/direction-symbolism.md` | `:189` |
| 4 | `culture-material/architecture-settlement-lexicon.md` | `:190` |
| 5 | `culture-material/writing-media-surface-economy.md` | `:191` |
| 6 | `civilizations/mesoamerica-primary-sources.md` | `:192` |
| 7 | `culture-material/transport-mobility-lexicon.md` | `:193` |

**F0 (P3, seed-side; I cannot edit filed bytes).** "these five" against seven rows is the same defect class r47 failed on — an unverified count word next to a longer list. The correct registry is the **seven rows**; any r48 fragment that dispositions "five neighbours" has silently dropped two. The r47 draft's table in fact carries **eight** rows (the seven plus `linguistics/naming-systems.md` at `C01-entry-a.md:103`), which is a superset — not a defect.

---

## 2. Live anchor re-read — all seven resolve exactly

Commands: `sed -n '<n>p' corpus/knowledge/<file>` at `a01405d`. Quotes below are from the live lines; where I trim, the cut is marked `…`.

| # | Neighbour | Anchor | Live text (trimmed) | Exact? |
|---|---|---|---|---|
| 1 | cosmology-cosmography | `:71` | `| Medieval Christian: T-O | east at top, Jerusalem center, three continents split by the T of waters | churches face east; Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, not survey maps (§10) | Isidore, Etymologiae 14 |` | yes |
| 1 | cosmology-cosmography | `:102` | "…T-O diagrams are symbolic devices, not cartographic claims. Disc cosmologies are emic models, not geometry failures…" | yes |
| 1 | cosmology-cosmography | `:27` | "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." | yes — **omitted by the draft row** |
| 1 | cosmology-cosmography | `:133` | "Toponyms are cosmographic claims… A fictional map is a set of etymological arguments — hand the derivation table to naming-systems." | yes |
| 2 | sacred-topography-pilgrimage | `:5` | "…sacred-geography mapping (a culture's holy sites as a diagram: radial, quartered, linear-corridor, or archipelago)…" | yes |
| 2 | sacred-topography-pilgrimage | `:69` | "**The three route types.** (a) **Fixed itinerary** … (b) **Votive ramble** … (c) **Circuit / circumambulation**…" | yes |
| 3 | direction-symbolism | `:51` | "**The compass trap**: an abstract north requires deciding *which* north — true or magnetic — and their difference (declination) is latitude- and era-dependent." | yes |
| 4 | architecture-settlement-lexicon | `:95` | "…surveyed with the **groma**… The grid is cadastral: a state that *measures land* builds this city." | yes |
| 5 | writing-media-surface-economy | `:3` | "…the seven surface families (clay and wax; stone and metal; papyrus and parchment; palm leaf, bark and cloth; bamboo and silk; paper; and the incidental surfaces…)" | yes |
| 6 | mesoamerica-primary-sources | `:58` | "| Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) | Cloth maps/migration-conquest accounts | … Originals often lost; the copy chain is the evidence — record which copy you cite… |" | yes |
| 7 | transport-mobility-lexicon | `:28` | "**Craft rule**: a route is only real if someone maintains it. … If your fictional road has no maintenance clause, it is a description, not an institution." | yes |
| 7 | transport-mobility-lexicon | `:117` | "| DR-TR-02 | Require a maintenance clause (labor obligation, calendar rite, or tax) for every named route and bridge | … | adopted — no route ships without its upkeep rule |" | yes |
| + | naming-systems (8th, bonus) | `:70` | "Every renaming is datable; a map is an archive of coups." | yes |

**12 of 12 anchors exact. Zero miscites.** This is the point r47's B3/B4 failed on; the r47 boundary table and body do not repeat it, and the r48 draft must not reintroduce it by re-typing these lines from memory.

I also verified the couples targets resolve as relative paths from the entry's directory `corpus/knowledge/culture-material/`:

```
OK ../myth-symbol/cosmology-cosmography.md 155
OK ../myth-symbol/sacred-topography-pilgrimage.md 181
OK ../myth-symbol/direction-symbolism.md 202
OK architecture-settlement-lexicon.md 149
OK writing-media-surface-economy.md 201
OK transport-mobility-lexicon.md 129
OK ../civilizations/mesoamerica-primary-sources.md 176
```

---

## 3. Per-neighbour disposition verdict

The duty has three legs: **dispositioned** (the row names what the neighbour owns, with a resolving citation), **extended** (the row says what *this* entry takes instead — a different object, not a summary), **no bleed** (the body does not re-teach the neighbour's owned content). I checked the third leg by keyword sweep over the three body fragments, then read every non-table hit.

| # | Neighbour | Row (r47) | Owns / takes split | Extended? | Restatement or bleed in body | Verdict |
|---|---|---|---|---|---|---|
| 1 | cosmology-cosmography | `C01:96` | five world-model axes + T-O symbolic + toponyms (`:71,:102,:133`) → "the measured sheet", contrast case | yes | five-axis terms (`five-axis`, `world-shape`, `layer-count`, `age-doctrine`) appear **once**, inside the row that disclaims them; `cosmogram` appears only in that row's disclaimer and in the cosmographic-form row, which cites the neighbour as the owner (`C01:247`). **But** `:27` unhandled — see F1 | **PASS-with-blocking-fix (F1)** |
| 2 | sacred-topography-pilgrimage | `C01:97` | holy-site typology, route-as-rite, route types (`:5,:69`), votive economy, shrine | yes — "representation of a route on a sheet" (itinerary, souvenir sheet, badge-map) | `hierophany` = 0 hits; `votive ramble` = 0 outside the row/audit table; route types are cited as map *content*, never re-typed. Living-practice routing at `C03:177,215` | **PASS** |
| 3 | direction-symbolism | `C01:98` | direction register, cardinal coinage, compass trap `:51`, circumambulation → sheet convention (which north, rose, arrow, graticule) | yes | `circumambulation`/`cardinal` appear only in the boundary row; the compass trap is re-stated **in the map's terms** at `C01:197` ("A map that does not say which north it uses is not wrong — it is under-specified") with the `:51` citation. That is an extension, not a restatement | **PASS** |
| 4 | architecture-settlement-lexicon | `C01:99` | city-plan lexicon, castrum grid, groma sentence `:95`, precinct → land survey as a production step | yes | `C02:70` **repeats `cardo` × `decumanus`** while drawing the survey case; one sentence, cited. The row promises "does not restate the settlement or precinct vocabulary". No typology, no precinct rite — a vocabulary gloss only — see F2 | **PASS-with-note (F2)** |
| 5 | writing-media-surface-economy | `C01:100` | seven surface families, cost ladder `:3` → map-specific media and reproduction in use/trade terms | yes | Body cites the cost curve at `C02:115` with range `:64-78`; I re-read it: `:64` is the `## 4. The cost ladder` heading, `:77` is the register law, `:78` the two-way error — the range is **accurate**, and the body paraphrases in map terms rather than re-tabling the five rungs. The ur-medium table (`C02:385-395`) is a map-word fossil table, not a surface-economy restatement; no preparation-chain text is reproduced | **PASS** |
| 6 | mesoamerica-primary-sources | `C01:101` | lienzo / cartographic-history source class + provenance `:58` → the genre as a map form and legal document | yes | The manuscript inventory is not reproduced; the form row (`C01:249`) cites `:58` and adds "nothing European scale conventions can read directly; it is a legal document first". `C03:177` adds a living-practice restriction that is *stricter* than the neighbour, not a restatement. Scope line omits it — see F3 | **PASS-with-note (F3)** |
| 7 | transport-mobility-lexicon | `C01:102` | routes, maintenance institution `:28`, DR-TR-02 `:117` → representation of a route on a sheet | yes | The maintenance rule is quoted once and *applied* at `C03:221` ("a mapped route without a maintenance clause is a description") — the neighbour's own distinction, cited, not re-derived. No mobility-layer system, no vehicle vocabulary | **PASS** |

**Score: 7/7 dispositioned, 7/7 extended, 0 bleed.** None of the seven rows is a summary of the neighbour; each names a different object (the sheet, not the register) and each bound is stated as an exclusion. The only substantive failure is the *completeness* of row 1 against its own neighbour's text.

### 3.1 Blast-radius check — does the entry pull any neighbour's topic into itself?

| Test | Result |
|---|---|
| Does the body define cosmology/cosmography terms? | no — no `axis` typology, no world-shape, no age-doctrine outside the disclaiming row |
| Does it type the route grammar? | no — `fixed itinerary` appears as a *map form* with the citation to `:69`; the rite grammar (separation/liminality/incorporation) is absent |
| Does it coin direction words or cardinal sets? | no |
| Does it re-describe the castrum founding rite? | no — `sulcus primigenius` / `pomerium` appear nowhere |
| Does it re-table the seven surface families or their preparation chains? | no — one cost-curve citation; the medium table is map-word etymology |
| Does it inventory Mesoamerican manuscripts? | no — three genre exemplars named once, as exemplars |
| Does it re-own route maintenance? | no — cites `:28`/DR-TR-02 and applies the rule to map claims |

The one-owner statement (`C01:105`) states the composition rule explicitly — the map owns the *slot grammar*, never a component register. That is the right architecture for a register-of-registers entry, and it is what keeps seven neighbours adjacent instead of absorbed.

---

## 4. Findings

### F1 — BLOCKING: the cosmography row omits the competing definition at `:27`

- **Evidence.** `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` (live, verified): "**Cosmography** = the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)."
- The draft's row (`C01:96`) and gap sentence (`C01:90`, `C04:115`) cite only `:71`/`:102`/`:133` — the *disclaimers* — and then assert "**No entry owns the made map**". A strict one-owner reading answers: `:27` says cosmography owns "how the world is drawn (maps)."
- This is R03's B8, re-confirmed independently at the r48 baseline. It is a **boundary** defect, not an ownership collision: the correct reading is that `:27` owns the **cosmogram / world-picture**, while the surveyed, projected, reproduced sheet is a different object. But the entry must *say* that, or the row under-claims its neighbour's text and the gap sentence over-claims.
- **Fix (mandatory for r48; exact wording supplied in §6).** Add to the row, the `- couples:` token for cosmography, and the `- gap filled:` sentence:

  > Cosmography owns the world-picture and the drawn cosmogram (`cosmology-cosmography.md:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as a production object.

### F2 — P3: `C02:70` repeats the settlement vocabulary the row promises not to restate

- `C02:70` reads: "the *groma* sets right angles, the *cardo* × *decumanus* grid is laid out, and the grid is cadastral…". `cardo`/`decumanus` are `architecture-settlement-lexicon.md`'s owned terms. The row (`C01:99`) says "does not restate the settlement or precinct vocabulary".
- Not a bleed — one cited sentence, no typology, no founding rite — but the promise is stronger than the bytes. **Fix:** either trim `C02:70` to "the groma sets the right angle and the castrum plan is the cadastral case (`:95`)", or soften the row to "does not restate the settlement typology or the founding rite; the axis names recur once as a survey illustration".

### F3 — P3: the `- scope:` negative list omits the Mesoamerican source class

- `C04:162` lists seven exclusions: world model, holy-site typology/route, direction register, settlement vocabulary, writing-surface economy, vehicle-and-road system, toponymy. **`mesoamerica-primary-sources.md` is absent**, although the entry uses the lienzo genre as a map form and the `couples:` line names it (`C04:159`).
- The `- scope:` field is the line a reader trusts for one-owner; an omission there is where a later entry would grow a second claim. **Fix:** add "the lienzo / cartographic-history source class (`../civilizations/mesoamerica-primary-sources.md`)" to the exclusion list.

### F4 — P3: the calibration bank re-argues the flat-earth ruling the row says it will not restate

- `C03:161` (calibration row 2) repeats the ruling in full: "A 19th-century fabrication; sphericity was standard ancient and medieval learning; T-O diagrams are symbolic devices, not survey maps." The row (`C01:96`) says the entry "does not restate … the flat-earth calibration".
- The calibration row **must exist** — a cartography entry that never names the T-O misreading would be worse. The defect is the *promise*, not the row. **Fix:** keep the row and cut the re-argument to a pointer ("per `cosmology-cosmography.md:102`: the flat-earth proof-reading is a 19th-century fabrication"), or reword the boundary promise to "cites the ruling at `:102` and re-argues none of it".

### F5 — P3: the gap sentence accounts for five of the seven

- `C01:90` names the corpus's owned space as: world model, sacred route, orientation, built plan, maintained route, name. Missing from the prose: **writing-media-surface-economy** and **mesoamerica-primary-sources** (both present in the table).
- Not a bleed; it weakens the gap argument, since the entry's own thesis is "the corpus owns every production system but the map" and the surface economy is the medium component of that chain. **Fix:** add "as surface economy (`culture-material/writing-media-surface-economy.md:3`)" to the sentence; the Mesoamerican genre can stay in the table only.

---

## 5. What I could not evaluate

- **The r48 draft itself.** No bytes exist at my write cut; this seat's per-row verdicts apply to the r47 reference, and §6 is the spec the r48 draft will be judged against. A later C15/C07 read must re-run §3's sweep on the r48 fences.
- **Any external source.** No network at seat time; the seven neighbours are all in-corpus and needed no external check. I read no shelf item.
- **Whether the r48 lander will use the same eight-row table.** If the r48 draft shrinks to a five-row table (following K02's "these five" count word), rows 6–7 would be missing and this seat would fail it.

---

## 6. Binding 7-row spec for the r48 draft (fenced — integrator/drafter may lift)

````markdown
| Neighbour | What it owns (verified anchor) | What this entry takes — and must not restate |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | the world model and the drawn cosmogram: the five world-model axes; T-O diagrams as symbolic, not survey (`:71`, `:102`); the definition that cosmography is "how the world is drawn (maps), named, walked, and built" (`:27`); toponyms as cosmographic claims (`:133`) | the **contrast case**: cosmography owns the world-picture and the cosmogram (`:27`, `:71`, `:102`); this entry owns the **surveyed, projected, reproduced sheet as production**. Cite the disclaimers; do not restate the five axes, the cosmogram typology, or the flat-earth ruling |
| `myth-symbol/sacred-topography-pilgrimage.md` | the place register: holy-site typology, six properties, route-as-rite, the three route types (`:5`, `:69`), votive economy, shrine institution | the **representation** of a route on a sheet and the map as a pilgrimage document (itinerary, souvenir sheet, badge-map). The site typology and route grammar stay there; route types are cited as map *content* |
| `myth-symbol/direction-symbolism.md` | the orientation register: direction frames, cardinal coinage, circumambulation, the true-vs-magnetic "compass trap" (`:51`) | the **sheet convention**: which way is up, the compass rose, the north arrow, the graticule, the declaration of which north. Cite `:51` for the under-specification problem; do not re-own the direction register |
| `culture-material/architecture-settlement-lexicon.md` | the city-plan lexicon, the Roman castrum grid and the groma sentence (`:95`), the founding rite and precinct | **land survey as a map-production step** and the plan as a cadastral object. Cite `:95`; do not restate the settlement typology or the founding rite (an axis-name gloss is at most one cited clause) |
| `culture-material/writing-media-surface-economy.md` | the seven surface families and their preparation chains; the cost ladder (`:3`, `:64-78`) | the **map-specific media choice and reproduction economics** (vellum, cloth, paper, copperplate; manuscript vs print; the atlas) as a use class and trade class. Cite the cost curve; do not re-table the seven families or their preparation chains |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo / cartographic-history **source class** and its provenance rules (`:58`) | the **genre as a map form** and its legal-document status. The manuscript inventory and the copy-chain provenance rule stay there; restricted living-tradition material routes through `../verification/real-world-inspiration-boundaries.md` |
| `culture-material/transport-mobility-lexicon.md` | routes and the maintenance institution (`:28`), DR-TR-02 (`:117`), the mobility layers | **how a route is drawn** — the line, the stage, the toll, the impassable season. Cite the maintenance rule; do not re-own transport or the upkeep institution |
````

**Scope-line addition (F3), one clause:** `…the vehicle-and-road system (`transport-mobility-lexicon.md`), the lienzo / cartographic-history source class (`../civilizations/mesoamerica-primary-sources.md`), or toponymy (`../linguistics/naming-systems.md`).`

**Row-1 sentence (F1), to add verbatim:** `Cosmography owns the world-picture and the drawn cosmogram (`cosmology-cosmography.md:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production.`

---

## 7. Acceptance checklist for the r48 draft

Run before any r48 C15/C07 verdict; each line is decidable.

1. **Registry count.** `grep -c "^| " <boundary table>` ≥ 7 and the seven K02 names are all present (`grep -o` each basename). A five-row table fails.
2. **Anchor re-read.** For each anchor in §2, `sed -n '<n>p'` still yields the quoted content at the apply-time HEAD. Any miss is a B4-class miscite.
3. **`:27` sentence present.** `grep -c 'cosmology-cosmography.md:27' <fence>` ≥ 1, and the sentence states the cosmogram/sheet split, not just a cite.
4. **Extend, don't restate.** For each neighbour, the row contains a "this entry owns/takes" clause naming a **different object**. A row that only summarises the neighbour fails.
5. **Bleed sweep.** `grep -ciE 'hierophany|votive ramble|sulcus|pomerium|cardo|decumanus|world-shape|age-doctrine|layer-count' <body>` — every hit must be inside a boundary row/recheck line or a single cited illustration; re-read each.
6. **Scope completeness.** The `- scope:` exclusion list names all seven neighbours, including mesoamerica.

---

## 8. Commands and write surface

All commands from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git diff --name-only 6e9a30d..a01405d -- corpus/ | wc -l
0
$ ls reports/round-48/
claims.json  targets.json  telemetry/
$ sed -n '27p;71p;102p;133p' corpus/knowledge/myth-symbol/cosmology-cosmography.md      # 4/4 quoted verbatim
$ sed -n '5p;69p' corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md          # 2/2
$ sed -n '51p' corpus/knowledge/myth-symbol/direction-symbolism.md                       # 1/1
$ sed -n '95p' corpus/knowledge/culture-material/architecture-settlement-lexicon.md      # 1/1
$ sed -n '3p;64,78p' corpus/knowledge/culture-material/writing-media-surface-economy.md  # cost ladder at :64-78
$ sed -n '58p' corpus/knowledge/civilizations/mesoamerica-primary-sources.md             # 1/1
$ sed -n '28p;117p' corpus/knowledge/culture-material/transport-mobility-lexicon.md      # 2/2
$ sed -n '70p' corpus/knowledge/linguistics/naming-systems.md                            # 1/1 (8th row)
$ grep -n 'these five' reports/round-44/scout/K02-gap-scout.md
183:The new entry must **couple to, not restate**, these five:
# rows at :187-193 = 7
$ grep -n '^| Neighbour' reports/round-47/cov/C01-entry-a.md
94:| Neighbour | What it owns (cited) | What this entry takes, and what it must not restate |
# data rows :96-103 = 8 (7 K02 neighbours + naming-systems)
$ grep -n '^- scope:' reports/round-47/cov/C04-entry-header.md
162:- scope: … seven exclusions; mesoamerica absent
```

**Anchor tally:** 13 of 13 in-corpus `path:line` assertions re-read live at `a01405d` and exact (12 neighbour anchors + the naming-systems bonus row); 7 of 7 couples paths resolve relative to `corpus/knowledge/culture-material/`.

**Write surface:** this file only — `reports/round-48/cov/C15-neighbors.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
