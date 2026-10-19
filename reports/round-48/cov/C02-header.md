# C02 — cartography entry header drafter (right-sized)

- Seat: `C02` | role: executor | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`baseline_commit: "a01405d"`).
- Out path: `reports/round-48/cov/C02-header.md` (this file).
- Mission: the head block only — H1, `- topic:`, `- gap filled:`, `- sources:`, `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:` — as a fenced block the integrator lifts verbatim. Body sections are other seats' work.

**Result in one line:** a 23-line head block is drafted on a freshly measured 223-entry tree at `a01405d`: 0 filename owners, 0 topic-line owners, slug unused, sort position free; every one of the 23 `path:line` assertions re-checked mechanically and all 19 `couples:` targets resolve. It carries the r47 fixes that belong to the header — B2 (the gap count is now reproducible: `cartograph` = 2 files / **2** lines), B3 (the `naming-systems.md:70` quote is used verbatim, with no "correction"), B4 (the craft ladder cites `:54-65`, not `:44`), and B8 (the cosmography `:27` "how the world is drawn (maps)" sentence is dispositioned, so the one-owner claim is not overstated).

---

## 1. Live state measured at `a01405d` (not carried from r44 or r47)

All commands run 2026-10-19 from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

### 1.1 Census and sweep

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
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
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

The partition is unchanged from r47's baseline except for the commit itself; the README digest is the same `7c788a1d…` (the duplicate-H1 defect the Ca claim fixes is still live).

### 1.2 Ownership probes — fresh, with the exact counts r47 got wrong

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ for t in cartograph mapmaking portolan cadastr graticule theodolite 'survey map' 'compass rose' 'mappa mundi'; do
    printf '%-14s files=%s lines=%s\n' "$t" \
      "$(grep -rli "$t" corpus/knowledge/ | wc -l)" "$(grep -rni "$t" corpus/knowledge/ | wc -l)"; done
cartograph     files=2 lines=2
mapmaking      files=0 lines=0
portolan       files=0 lines=0
cadastr        files=2 lines=2
graticule      files=0 lines=0
theodolite     files=0 lines=0
survey map     files=1 lines=1
compass rose   files=1 lines=1
mappa mundi    files=1 lines=1
```

The exact hit lines:

```
$ grep -rni 'cartograph' corpus/knowledge/
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:… T-O diagrams are symbolic devices, not cartographic claims …
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:| Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) | …
$ grep -rni 'cadastr' corpus/knowledge/
corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95:… The grid is cadastral: a state that *measures land* builds this city.
corpus/knowledge/civilizations/japan-medieval-sengoku.md:157:… a neat Edo cadastral map must not be treated as a direct Sengoku map.
$ grep -rni 'survey map' corpus/knowledge/
corpus/knowledge/myth-symbol/cosmology-cosmography.md:71:… T-O diagrams are symbolic, not survey maps (§10) …
$ grep -rni 'compass rose' corpus/knowledge/
corpus/knowledge/myth-symbol/direction-symbolism.md:26:… In-world, a direction code is expressed as ritual regulation, omen lore, house rules, and processional custom — never as a compass rose with a legend.
```

**The r47 B2 defect, corrected.** r47's head block claimed "2 files / 3 lines" for `cartograph` and counted `:71` as a `cartograph` hit. `:71` does **not** contain the token `cartograph` (it says "Mappa Mundi" and "survey maps"), and `grep -rli` counts files, not lines. This block states **2 files / 2 lines** (`:102`, `mesoamerica:58`) and keeps `:71` separate as the `survey map` disclaimer. No count in the block is asserted without the command that produced it.

### 1.3 Freshness, not carriage

- The only prior proposal is the originating scout `reports/round-44/scout/K02-gap-scout.md`; its §3.6 checked `round-19/gaps.md`, `round-35/scout/K01`, `round-39/scout/K01`, `round-40/scout/K03`, `round-42/scout/K02`, the r36–r43 scouts and the lane docs, and found no cartography row.
- `reports/round-44/validation.json:9` records: "the fresh gap (cartography, K02) has no entry body. No corpus delta; coverage holds at 223." The topic was scouted and **not landed** — not carried.
- `reports/round-45/` does not exist; `grep -rliE 'cartograph|mapmaking|portolan' reports/round-46/` → **0** files.
- The r48 freshness gate re-confirmed the claim FRESH at declaration (`reports/round-48/claims.json:21-24`; result mirrored in `reports/round-48/telemetry/dispatch-declared.json` under `freshness_gate_first_live_use`). The gate guards topic ownership, not entry quality — the over-build class is the Ca claim's business, not this block's.

### 1.4 Collision and sort position

- Slug unused; no entry's `- topic:` names mapmaking. Landing is an **A**, not an M.
- README culture-material rows are filename-ordered: `…calendar-festival-systems.md`, `costume-semiotics.md…`, so `cartography-and-mapmaking.md` inserts between them (confirmed with `ls corpus/knowledge/culture-material/*.md | sed -n '5,7p'`).
- Nearest neighbour: `myth-symbol/sacred-topography-pilgrimage.md:5` (the place register and the sacred-geography diagram). It is coupled, not duplicated.

---

## 2. The head block (fenced — integrator lifts verbatim)

Target path: `corpus/knowledge/culture-material/cartography-and-mapmaking.md`.
Everything below is the entire head block (all bytes above the first `## ` body section). `- topic:` is the r44 K02 §4.2 seed **verbatim** (`reports/round-44/scout/K02-gap-scout.md`, the fenced `text` block; one physical line, sha256 of the seed line `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a`) — the README row must copy it byte-for-byte.

````markdown
# Cartography and mapmaking — the map as an argument about space: the survey chain, projection and scale, symbol grammar, reproduction, and the map's silences

- topic: the map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative; the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo); projection and scale as claims about what matters; the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank); the reproduction economics (manuscript, woodblock, copperplate, the atlas); the map's silences and its use as a legal/territorial instrument; a build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)
- gap filled: the corpus owns the world-picture, the sacred route, the orientation code and the built plan, and owns no made map. The boundary is the partition's own: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` defines cosmography as "the projected, inhabited version: how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)" — cosmography owns that world-drawn content; `:71` distinguishes the T-O diagram from "survey maps"; `:102` calls T-O diagrams "not cartographic"; `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5` owns "sacred-geography mapping … as a diagram" and the route types; `corpus/knowledge/myth-symbol/direction-symbolism.md:51` owns the orientation register and the true-vs-magnetic "compass trap"; `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` owns the castrum grid and names the groma as the survey step. This entry owns the surveyed, projected, reproduced sheet as production — the chain from measured ground to an authoritative copy — and restates none of those registers. Fresh absence sweep, run 2026-10-19 from the lane root at HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (223 files; partitions 94/25/25/26/29/24): filename probe `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l` → **0**; slug `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → **No such file**; topic-owner probe `grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l` → **0** (the one wider-probe hit, `itinerar` in `sacred-topography-pilgrimage.md:5`, is a route type, not map production); term counts `mapmaking` 0, `portolan` 0, `graticule` 0, `theodolite` 0, `cartograph` **2 files / 2 lines** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`), `cadastr` **2 files / 2 lines** (`architecture-settlement-lexicon.md:95`, `japan-medieval-sengoku.md:157`), `survey map` 1 line (`cosmology-cosmography.md:71`, the disclaimer). Demand is honestly low: this is a named-but-unbuilt register, not a high-demand omission. **Not carried:** the only prior proposal is `reports/round-44/scout/K02-gap-scout.md` (its §3.6 checked every prior registry); `reports/round-44/validation.json:9` records "the fresh gap (cartography, K02) has no entry body. No corpus delta"; `reports/round-45/` is absent and `reports/round-46/` has 0 cartography hits. The topic was re-confirmed FRESH by the r48 freshness gate at declaration (`reports/round-48/claims.json:21-24`).
- sources:
  - In-corpus anchors (repo-relative `path:line`, each re-read at HEAD `a01405d` on 2026-10-19; sha256 pinned for the eleven load-bearing files):
    - `corpus/knowledge/myth-symbol/cosmology-cosmography.md` (sha256 `165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e`): `:27` "how the world is drawn (maps)" — the competing-definition sentence this entry must disposition; `:71` the T-O row, "symbolic, not survey maps"; `:102` "not cartographic". The world-model typology is **not** restated.
    - `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` (sha256 `241113b5a1259b04de889ebc458736ab8860e015b9afa9f74479bcc8bc165459`): `:5` "sacred-geography mapping … as a diagram" — the place register and route types, cited as map *content*, not re-owned.
    - `corpus/knowledge/myth-symbol/direction-symbolism.md` (sha256 `5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426`): `:51` the "compass trap" (true vs magnetic north, declination); `:26` in-world direction codes are "never … a compass rose with a legend" — the sheet's compass rose is designer tooling, and this entry cites the register rather than restating it.
    - `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` (sha256 `9af04e751206c32bc1ca38a73ef16a27a3e2e4a696454dd1bb5e22ed27bada9f`): `:95` the castrum grid "surveyed with the groma", "the grid is cadastral". The settlement vocabulary stays there; this entry owns land survey as a production step.
    - `corpus/knowledge/culture-material/writing-media-surface-economy.md` (sha256 `f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601`): `:3` the seven surface families. This entry owns map-specific media and reproduction (parchment, paper, cloth, copperplate; manuscript vs print; the atlas) and cites the economy rather than restating it.
    - `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (sha256 `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70`): `:28` "a route is only real if someone maintains it". This entry owns the *representation* of a route, not the route institution.
    - `corpus/knowledge/culture-material/craft-artisan-lexicon.md` (sha256 `fd678d82fcc5134f5c5c0a65b15106b35cabe67bfd935d45df4fa16524f30288`): the workshop ladder at `:54-65` (`:54` the header; `:56-63` the systems; `:65` the design rule) — **not `:44`**, which is the steel-grading row (the r47 B4 miscite). `:3` is the topic-line summary only.
    - `corpus/knowledge/culture-material/trade-economy-lexicon.md` (sha256 `760a9df61364916b69e91c4d7f21ee4bff6bf138af6643f585afdcb10f05f277`): `:92` the Exchequer tally's stock/foil split; `:121` split-object authentication (`symbolon`, chirograph). The boundary case for the map as a legal instrument.
    - `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` (sha256 `d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530`): `:58` the lienzo / cartographic-history source class. Cited as a genre; the manuscript inventory is not restated.
    - `corpus/knowledge/linguistics/naming-systems.md` (sha256 `d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d`): `:70` "Every renaming is datable; a map is an archive of coups" — quoted **verbatim**; it is not paraphrased and no "correction" is owed (the r47 B3 false accusation is not repeated).
    - `corpus/knowledge/verification/calibration-registry.md` (sha256 `cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c`): `:50` the CAL-03 row; `:78-88` the strong-Whorf section. The calibration posture for a "maps determine thought" claim.
  - External standard shelf — **not consulted this round** (no network at seat time); author/year/title/publisher at book level, every edition, volume and page locator `(to-verify)`; no unread work is presented as inspected: Harley & Woodward (eds.), *The History of Cartography* (University of Chicago Press, 1987–) `(to-verify)`; Harley (1989), "Deconstructing the Map," *Cartographica* 26(2):1–20 `(to-verify)`; Wood (1992; 2nd ed. 2010), *The Power of Maps* (Guilford) `(to-verify)`; Monmonier (1991; 3rd ed. 2018), *How to Lie with Maps* (University of Chicago Press) `(to-verify)`; Jacob (French 1992; Eng. trans. 2006), *The Sovereign Map* (University of Chicago Press) `(to-verify)`; Ptolemy, *Geography*, trans. Berggren & Jones (2000, Princeton University Press) `(to-verify)`; Campbell (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *The History of Cartography* vol. 1 `(to-verify)`; Kain & Baigent (1992), *The Cadastral Map in the Service of the State* (University of Chicago Press) `(to-verify)`; Snyder (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395 `(to-verify)`; Dilke (1971), *The Roman Land Surveyors* (David & Charles) `(to-verify)`.
- couples: myth-symbol — `../myth-symbol/cosmology-cosmography.md` (owns the world model and the world-drawn/cosmogram content — `:27,:71,:102`; this entry owns the surveyed sheet and cites the disclaimer as its charter); myth-symbol — `../myth-symbol/sacred-topography-pilgrimage.md` (owns the holy-site typology and route-as-rite — `:5`; this entry owns how a route is measured and drawn); myth-symbol — `../myth-symbol/direction-symbolism.md` (owns the orientation register and the compass trap — `:51`; this entry owns the map convention: orientation choice, compass rose, north arrow); culture-material — `architecture-settlement-lexicon.md` (owns the built plan and the groma sentence — `:95`; this entry owns land survey as a map-production step); culture-material — `writing-media-surface-economy.md` (owns the surface families and cost ladder — `:3`; this entry owns map-specific media and reproduction); culture-material — `transport-mobility-lexicon.md` (owns route institutions and the maintenance rule — `:28`; this entry owns the representation of a route); culture-material — `craft-artisan-lexicon.md` (owns the workshop register and the ladder — `:54-65`; the mapmaker's shop is a craft case in those terms); culture-material — `trade-economy-lexicon.md` (owns measures, weights, contract vocabulary and split-object authentication — `:92,:121`; this entry owns the map as a legal/territorial instrument); culture-material — `timekeeping-instruments.md` (owns the instrument families, including `:50` longitude at sea; this entry owns the coordinate problem the map inherits); culture-material — `material-culture-inference-method.md` (owns the perishability constraint `:69` and the anti-determinism guard `:76`; applied here to map survival and to "the map caused the state"); culture-material — `vessel-container-lexicon.md` (owns containers as documents and chronometers — `:115`; the map roll and archive chest are storage, cited at the boundary); linguistics — `../linguistics/naming-systems.md` (owns toponymy — `:70`; the map's place-names are that file's assignment, not this entry's); civilizations — `../civilizations/mesoamerica-primary-sources.md` (owns the lienzo source class — `:58`; cited as genre, inventory not restated); civilizations — `../civilizations/japan-medieval-sengoku.md` (owns the Edo-cadastral periodization caution — `:157`); civilizations — `../civilizations/polynesia-navigation.md` (owns horizon compass and steering-star operations — `:52`; navigation is explicitly not a chart); verification — `../verification/calibration-registry.md` (owns the calibration posture — `:50` CAL-03; a "maps determine thought" claim is braked with the same test); verification — `../verification/real-world-inspiration-boundaries.md` and `../verification/myth-consistency-gate.md` (own the restricted-knowledge boundary; every living tradition's restricted map or songline is routed there before any table is filled); synthesis — `../synthesis/worldbible-integration-contract.md` (handoff target; this entry records nothing in canon).
- source: lane-side authority is the in-corpus `path:line` anchor list above (each re-read at HEAD `a01405d`, 2026-10-19) plus the absence-sweep commands recorded in `- gap filled:`; the external frameworks are the shelf above, **none fetched or inspected this run** (no network at seat time), so every edition, volume and page locator carries `(to-verify)` — the shelf supports mechanisms, never a claim about any fictional world. The four-choice spine (what is measured / what is preserved / what is drawn / who may copy and read), the form typology, the symbol grammar and the build order are this lane's design method assembled from those sources.
- verified-at: 2026-10-19 — draft written at HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`; equal to `reports/round-48/claims.json` `baseline_commit` `a01405d`). Measured with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**; `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}, totals_line 223, footer `25/26/25/29/24/94`, exit 0; `corpus/README.md` sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`. Every in-corpus `path:line` in this head block was checked mechanically in this seat: **23/23** needle-in-line assertions passed over 22 distinct anchors, and **19/19** `- couples:` targets resolve relative to `corpus/knowledge/culture-material/`. The slug is unused; the README sort position is between `calendar-festival-systems.md` (5th) and `costume-semiotics.md` (6th). **Not claimed:** any portolan accuracy figure, any projection-distortion value, any print-run or price, any survival percentage, any external edition, volume or page.
- recheck: before any map, survey or territorial claim becomes load-bearing — re-read `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102` before repeating any flat-earth/T-O calibration and `:71` before letting a symbolic diagram stand in for a survey map; re-read `:27` before claiming cosmography does not own "how the world is drawn"; re-read `corpus/knowledge/myth-symbol/direction-symbolism.md:51` (and `:26`, which denies the compass rose as an emic direction code) before fixing true north, magnetic north or an east-at-top convention; re-read `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` before treating a castrum grid as a survey (the grid is a plan; the groma is the chain); re-read `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58` before citing a lienzo as evidence of a cartographic practice; re-read `corpus/knowledge/culture-material/material-culture-inference-method.md:69` before treating a surviving map as evidence of its own importance (parchment and vellum survive; cloth and bark do not); re-read `corpus/knowledge/culture-material/transport-mobility-lexicon.md:28` before drawing a route no institution maintains; and route every living tradition's restricted map or songline through `corpus/knowledge/verification/real-world-inspiration-boundaries.md:6` and `corpus/knowledge/verification/myth-consistency-gate.md:34` before filling any table. Corrections to this entry are a new section or a new entry, never a rewrite.
- scope: reference method and lane policy for the culture-material partition. This entry owns the map as a made instrument and a claim — the survey chain, projection and scale, symbolization, reproduction, and the map's silences. It does not own the world model or the cosmogram (`../myth-symbol/cosmology-cosmography.md`), the holy-site typology and route-as-rite (`../myth-symbol/sacred-topography-pilgrimage.md`), the direction register (`../myth-symbol/direction-symbolism.md`), the settlement vocabulary (`architecture-settlement-lexicon.md`), the writing-surface economy (`writing-media-surface-economy.md`), the vehicle-and-road system (`transport-mobility-lexicon.md`), or toponymy (`../linguistics/naming-systems.md`). It decides nothing about any world — no border, charter or survey is authorized by this file — and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff.
````

---

## 3. Right-sizing and defect map

### 3.1 Length

The fenced block is **23 lines** (measured in §4.3). The partition's header length ranges 7–42 lines (`funerary-material-culture.md` 42, `writing-media-surface-economy.md` 34, median ~11), so this is inside the house band and leaves ~227 lines of the ≤~250 budget for the body seats. r47's header was the same field set but carried a 49-line external shelf and a 21-token couples essay; this block keeps the shelf at 2 lines and the couples line at 1 physical line.

### 3.2 r47 R03 defects this block must not reproduce

| Defect (R03) | Where it applied | This block's behaviour | Evidence |
|---|---|---|---|
| **B1** arithmetic (200 m = 20× not 10×) | body (`C02:98` r47) | no arithmetic claim in the header; the only numbers are measured counts | §1.2 |
| **B2** unreproducible count "2 files / 3 lines" | header `- gap filled:` | corrected to **2 files / 2 lines**, `:71` reclassified as the `survey map` disclaimer | §1.2 |
| **B3** false accusation against `naming-systems.md:70` | r47 C02, not the header | quote used verbatim; no "correction" proposed | `grep -n 'archive of coups'` → `70:` |
| **B4** ladder cited at `:44` | r47 body + audit | header cites `:54-65`; `:44` explicitly labelled the steel-grading row | §1.2, §4.2 |
| **B5/B6** wrong section cross-refs | body | the header makes no `§N` references at all | block text |
| **B7** worked-example rule stated three ways | body | out of scope here; flagged for the body/C14 seats | — |
| **B8** "owns no made map" overstated vs `cosmography:27` | header `- gap filled:` | the `:27` sentence is quoted and dispositioned: cosmography owns the world-drawn content; this entry owns production | §1.2 |
| **B9** 5-of-8 form table | body | out of scope here; flagged for the body/C05 seats | — |
| **P2-2** "six" anchors when nine were pinned | header | this block does not state an anchor count in prose except via the measured `verified-at:` field ("23/23 assertions … 22 distinct anchors") | §4.2 |

### 3.3 Field-order and convention note

The field order follows the mission and the recent culture-material precedent (`timekeeping-instruments.md:3-11`, `writing-media-surface-economy.md:3-11`): `topic, gap filled, sources, couples, source, verified-at, recheck, scope`. There is **no** `- calibration:` field: the three newest culture-material entries carry the calibration bank in the body, and the mission's field list is the eight above. `gap filled`, `source` and `scope` are newer than most of the partition (present in 3, 6 and 3 of 25 entries respectively); including them is deliberate, not drift.

---

## 4. Verification transcript

### 4.1 Census/sweep

See §1.1. `exit=0`; `rows 223 files 223`; footer `25/26/25/29/24/94`.

### 4.2 Anchor assertions (23 checks over 22 anchors, 0 failures)

```
OK   cosmology-cosmography.md:27    "how the world is drawn (maps)"
OK   cosmology-cosmography.md:71    "symbolic, not survey maps"
OK   cosmology-cosmography.md:102   "not cartographic"
OK   sacred-topography-pilgrimage.md:5  "sacred-geography mapping"
OK   direction-symbolism.md:51      "compass trap"
OK   architecture-settlement-lexicon.md:95  "groma"
OK   architecture-settlement-lexicon.md:95  "cadastral"
OK   writing-media-surface-economy.md:3     "seven surface families"
OK   transport-mobility-lexicon.md:28       "a route is only real if someone maintains it"
OK   mesoamerica-primary-sources.md:58      "Lienzos and cartographic histories"
OK   naming-systems.md:70                   "a map is an archive of coups"
OK   craft-artisan-lexicon.md:54            "Apprentice"
OK   craft-artisan-lexicon.md:65            "Design rule"
OK   trade-economy-lexicon.md:92            "stock"
OK   trade-economy-lexicon.md:121           "Split-object authentication"
OK   calibration-registry.md:50             "CAL-03"
OK   calibration-registry.md:78             "CAL-03"
OK   timekeeping-instruments.md:50          "longitude at sea"
OK   vessel-container-lexicon.md:115        "document"
OK   material-culture-inference-method.md:69 "perishab"
OK   material-culture-inference-method.md:76 "deterministic trap"
OK   japan-medieval-sengoku.md:157          "Edo cadastral map"
OK   polynesia-navigation.md:52             "horizon compass"
FAILURES 0
```

Additional line checks used in `- recheck:`: `direction-symbolism.md:26` contains "never as a compass rose with a legend"; `real-world-inspiration-boundaries.md:6` is the reuse-permission recheck; `myth-consistency-gate.md:34` is "Do not expose restricted ritual knowledge to fill a table." All three confirmed by `sed -n`.

### 4.3 Couples resolution (19/19)

All resolve relative to `corpus/knowledge/culture-material/`:

```
../myth-symbol/cosmology-cosmography.md            OK
../myth-symbol/sacred-topography-pilgrimage.md     OK
../myth-symbol/direction-symbolism.md              OK
architecture-settlement-lexicon.md                 OK
writing-media-surface-economy.md                   OK
transport-mobility-lexicon.md                      OK
craft-artisan-lexicon.md                           OK
trade-economy-lexicon.md                           OK
timekeeping-instruments.md                         OK
material-culture-inference-method.md               OK
vessel-container-lexicon.md                        OK
../linguistics/naming-systems.md                   OK
../civilizations/mesoamerica-primary-sources.md    OK
../civilizations/japan-medieval-sengoku.md         OK
../civilizations/polynesia-navigation.md           OK
../verification/calibration-registry.md            OK
../verification/real-world-inspiration-boundaries.md  OK
../verification/myth-consistency-gate.md           OK
```

`synthesis/worldbible-integration-contract.md` (the handoff target named in `- couples:`) resolves the same way — `corpus/knowledge/culture-material/../synthesis/worldbible-integration-contract.md` exists — so the count is **19/19**.

### 4.4 Fenced-block line count

```
$ python3 - <<'PY'
import re, pathlib
t = pathlib.Path('reports/round-48/cov/C02-header.md').read_text()
blocks = re.findall(r'````markdown\n(.*?)\n````', t, re.S)
print(len(blocks), [len(b.splitlines()) for b in blocks])
PY
1 [23]
```

### 4.5 README defect flagged, not touched

`grep -c '^# kotodama-shokunin corpus index' corpus/README.md` → **2** (lines 1 and 3); `corpus/README.md` sha256 `7c788a1d…`; the rev-2.4 prose vector at `:11` sums **217** (not 223). Both belong to claim **Ca**; this block only predicts the post-landing culture-material count 25 → 26 and does not edit the index.

---

## 5. Integration contract

1. **Target:** `corpus/knowledge/culture-material/cartography-and-mapmaking.md` — an **A** (the path does not exist at `a01405d`). Re-check the live tree at apply time; if another seat landed the slug first, stop and report the collision rather than overwrite.
2. **Bytes:** lift the fenced block in §2 as the first bytes of the file; body sections start at the first `## `. Do not reflow: `- topic:` is one physical line (the sweep's `TOPIC_RE` stops at the next `- word` line), and each field is one physical line.
3. **README rev 2.5 (other seats):** new row between `calendar-festival-systems.md` and `costume-semiotics.md`; row text is the `- topic:` value **byte-for-byte**; `## culture-material/ (25)` → `(26)`; totals 223 → 224; footer vector `25/26/25/29/24/94` → `25/26/26/29/24/94`; repair the rev-2.4 prose vector (sums 217) in the same edit.
4. **Post-landing prediction (not measured here):** total 224; culture-material 26; sweep `rows 224 files 224`; the entry ≤ ~250 lines including this 23-line head.
5. **No corpus write by this seat.** Nothing under `corpus/`, `tools/`, `LOG.md` or `README` was touched or staged.

---

## 6. Write surface and limits

**Write surface:** this file only — `reports/round-48/cov/C02-header.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed. `git status --porcelain` at the write cut showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.

**Not verified by this seat:** the body sections (other seats); any external edition, volume or page (no network); the assembled entry's total line count (body seats); the README edit and staged sweep (C10/C11); the Ca claim's duplicate-heading fix and over-build disposition (Ca seats). The gate result is cited from `reports/round-48/claims.json:21-24` and `telemetry/dispatch-declared.json`; the gate's overlay file itself is not filed under `reports/round-48/`, so a replay of the exact gate invocation is `to-verify` for O01/O04, not claimed here.

**One remaining judgement call for the integrator:** `- couples:` names `../synthesis/worldbible-integration-contract.md` as the handoff target and `real-world-inspiration-boundaries.md` / `myth-consistency-gate.md` as restriction routes; these are boundary citations, not content the entry restates. If the body seats drop the restricted-material route, remove those two tokens rather than leaving a dangling promise.
