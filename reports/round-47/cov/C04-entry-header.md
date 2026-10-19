# C04 — cartography entry header drafter

- Seat: `C04` | role: executor | claim: **C** (coverage) | round 47, loop 2
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-47/claims.json:7`
- Out path: `reports/round-47/cov/C04-entry-header.md` (this file)
- Mission: draft the **full head block** for the proposed entry — H1, `- topic:`, `- gap filled:` (fresh sweep evidence), `- sources:` (tiered shelf, `to-verify`), `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:` — as a fenced block the integrator can lift.
- Deliverable location: §2 below. §1 is the measured state the block cites; §3 is the integration contract; §4 is the self-audit.

**Result in one line:** the head block is drafted on a **live** 223-entry tree — zero filename owners, zero topic-line owners, slug unused, sort position between `calendar-festival-systems.md` and `costume-semiotics.md`; no collision to report. The block is byte-ready except for the four parts owned by other seats (body sections, README row, source audit, contract audit).

---

## 1. Measured state at HEAD `6e9a30d` (not carried from r44)

Commands run 2026-10-19 from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

### 1.1 Census

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
linguistics      25
myth-symbol      26
culture-material 25
synthesis        29
verification     24
civilizations    94
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ... "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

### 1.2 Ownership probes (the gap is still unowned at r47)

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ grep -rli 'mapmaking' corpus/knowledge/ | wc -l          # 0
$ grep -rli 'portolan'  corpus/knowledge/ | wc -l          # 0
$ grep -rli 'graticule' corpus/knowledge/ | wc -l          # 0
$ grep -rli 'theodolite' corpus/knowledge/ | wc -l         # 0
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l         # 2 files / 3 lines
$ grep -rli 'cadastr'   corpus/knowledge/ | wc -l          # 2 files
```

The three `cartograph` lines are by-product or disclaimer, not ownership:
`myth-symbol/cosmology-cosmography.md:71` (T-O diagrams "symbolic, not survey maps"),
same file `:102` ("not cartographic"), and
`civilizations/mesoamerica-primary-sources.md:58` (lienzos as a *source class*).
The two `cadastr` files are `architecture-settlement-lexicon.md:95` (the castrum grid;
one sentence names the groma) and `japan-medieval-sengoku.md:157` (a periodization caution
against reading an Edo cadastral map back into the Sengoku period).

**The one loose topic hit, reported rather than hidden:** widening the topic probe with
`itinerar` returns **1** hit — `myth-symbol/sacred-topography-pilgrimage.md:5`, inside
"the fixed itinerary vs the votive ramble". That is a *route type* owned by the place
register, not map production; it is the nearest neighbour the block couples to, and it
does not own the survey-to-sheet chain. A broad demand probe over 20 patterns
(`cartograph|mapmak|portolan|cadastr|mappa mundi|surveyor|theodolit|compass rose|graticule|world map|drawn map|map of|maps of`)
measures **28 files / 31 lines**, every genuine hit a by-product of another system.

### 1.3 Freshness, not carriage

- The only pre-r47 proposal is the originating scout `reports/round-44/scout/K02-gap-scout.md`
  (its §3.6 checked `round-19/gaps.md`, `round-35/scout/K01`, `round-39/scout/K01`,
  `round-40/scout/K03`, `round-42/scout/K02`, the r36–r43 scouts, and the root lane docs).
- `reports/round-44/validation.json:9` records the round's own outcome:
  "the fresh gap (cartography, K02) has no entry body. No corpus delta" — the topic was
  scouted fresh at r44 and **not landed**, not carried from an earlier registry.
- Grep across all filed reports: every `cartograph|mapmaking|portolan` hit outside K02 is
  either r44's own wave citing K02 (C05/C06/A01/X01/R01/R02/S01) or frozen scratch copies
  of `mesoamerica-primary-sources.md` under `reports/supplement-opencode-1/`. `reports/round-46/`
  has **0** hits; `reports/round-45/` does not exist.
- A collision check at the live partition: the slug is unused, and no other entry's `- topic:`
  names mapmaking. **No collision to report.**

### 1.4 The README defect the rev-2.5 edit must repair

`corpus/README.md:11` (rev 2.4 prose) reads "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**".
That vector sums **217**, not 223; the live footer (`:548`, sweep-measured) is the correct
`25/26/25/29/24/94` = 223. This block does not touch the README (no corpus writes by seats);
the defect is flagged for the integrator/C09, and the post-landing vector is
`25/26/26/29/24/94` = **224** (culture-material 25 → 26).

---

## 2. The head block (fenced — integrator lifts verbatim)

Target path: `corpus/knowledge/culture-material/cartography-and-mapmaking.md`.
The fenced block is the **entire head block** (everything above the first `## ` body section).
`- topic:` is byte-equal to the K02-r44 seed and is the single source of truth for the README
row description (C09 must copy it byte-for-byte).

````markdown
# Cartography and mapmaking — the map as an instrument and a claim: the survey-to-reproduction chain, projection and scale, the symbol grammar, and the map's silences

- topic: the map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative; the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo); projection and scale as claims about what matters; the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank); the reproduction economics (manuscript, woodblock, copperplate, the atlas); the map's silences and its use as a legal/territorial instrument; a build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)
- gap filled: the corpus owns space as cosmology, space as sacred route, space as orientation code and space as built plan — and owns no made map. The partition's own disclaimer is this entry's charter: `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` distinguishes the T-O diagram from "survey maps" and `:102` says T-O diagrams are "not cartographic"; `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:5` owns "sacred-geography mapping … as a diagram" (the place register and the route); `corpus/knowledge/myth-symbol/direction-symbolism.md:51` owns the orientation register and the true-vs-magnetic "compass trap"; `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` owns the castrum grid and names the groma as the survey step. What none owns is the survey → projection → drawing → reproduction chain that turns measured ground into an authoritative sheet. Fresh absence sweep 2026-10-19 at r47 HEAD `6e9a30d` from the lane root over `corpus/knowledge/` (223 files; partitions 25/26/25/29/24/94): filename probe `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l` → **0**; slug probe `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → **No such file**; topic-owner probe `grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l` → **0** (the one loose hit under the wider probe is `itinerar` inside sacred-topography's "fixed itinerary vs the votive ramble" — a route type, not map production); `grep -rli 'mapmaking' corpus/knowledge/ | wc -l` → **0**; `grep -rli 'portolan' …` → **0**; `grep -rli 'graticule' …` → **0**; `grep -rli 'theodolite' …` → **0**; `grep -rli 'cartograph' …` → **2 files / 3 lines**, all by-product or disclaimer (`cosmology-cosmography.md:71,:102`; `civilizations/mesoamerica-primary-sources.md:58`, lienzos as a source class); `grep -rli 'cadastr' …` → **2 files** (`architecture-settlement-lexicon.md:95`; `civilizations/japan-medieval-sengoku.md:157`, a periodization caution); a broad-vocabulary demand probe (20 patterns incl. `compass rose`, `world map`, `drawn map`) measures **28 files / 31 lines**, every genuine hit a by-product of another system. **Not carried:** the only pre-r47 proposal is the originating scout `reports/round-44/scout/K02-gap-scout.md` (its §3.6 checked every prior registry and found none), and `reports/round-44/validation.json:9` records "the fresh gap (cartography, K02) has no entry body. No corpus delta"; rounds 45–46 carry zero cartography mentions (`reports/round-45/` absent; `reports/round-46/` grep → 0). The nearest neighbour is `sacred-topography-pilgrimage.md:5`'s diagram of holy sites — this entry cites it and does not restate the place register.
- sources:
  - In-corpus anchors (repo-relative `path:line`, each re-read at HEAD `6e9a30d` on 2026-10-19; sha256 pinned for the six load-bearing anchors):
    - `corpus/knowledge/myth-symbol/cosmology-cosmography.md` (sha256 `165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e`): `:71` the T-O row — "symbolic, not survey maps"; `:102` the flat-earth calibration — "not cartographic". The charter citation; the five-axis world-model typology is **not** restated.
    - `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` (sha256 `241113b5a1259b04de889ebc458736ab8860e015b9afa9f74479bcc8bc165459`): `:5` "sacred-geography mapping … as a diagram: radial, quartered, linear-corridor, or archipelago" — the place register and the three route types, cited as map *content*, not re-owned.
    - `corpus/knowledge/myth-symbol/direction-symbolism.md` (sha256 `5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426`): `:51` the "compass trap" — true vs magnetic north and declination. This entry owns the map *convention* (orientation choice, compass rose, north arrow) and cites the register.
    - `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` (sha256 `9af04e751206c32bc1ca38a73ef16a27a3e2e4a696454dd1bb5e22ed27bada9f`): `:95` the Roman castrum grid "surveyed with the groma"; the grid is "cadastral". This entry owns land survey as a map-production step; the settlement lexicon stays there.
    - `corpus/knowledge/culture-material/writing-media-surface-economy.md` (sha256 `f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601`): `:3` the seven surface families and the cost ladder. This entry owns map-specific media and reproduction (parchment/paper/cloth/copperplate; manuscript vs print; the atlas) and cites the surface economy rather than restating it.
    - `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (sha256 `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70`): `:28` "a route is only real if someone maintains it"; `:117` the maintenance-clause decision row. This entry owns the *representation* of routes and cites the maintenance rule.
    - `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` (sha256 `d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530`): `:58` the lienzo / cartographic-history genre and its provenance. Cited as a source class; the manuscript inventory is not restated.
    - `corpus/knowledge/culture-material/timekeeping-instruments.md` (sha256 `9805c0b854334ed396119476b6278cc4f58eb1014a0b06eb6bba561def05f0a6`): `:50` "longitude at sea" as the minute's application — the measurement side of the map's coordinate problem.
    - `corpus/knowledge/culture-material/material-culture-inference-method.md`: `:69` the perishability constraint (what survives to be seen); `:76` the anti-determinism guard. Both applied to map survival and to the "the map caused the state" reading; neither restated.
    - `corpus/knowledge/culture-material/craft-artisan-lexicon.md`: `:44` the material-grading vocabulary (the workshop register). The mapmaker's workshop and tool names are a craft case in that file's terms.
    - `corpus/knowledge/culture-material/trade-economy-lexicon.md`: `:92` and `:121` — the Exchequer tally's stock/foil split and split-object authentication. The boundary case for the map as a legal instrument (a copied sheet authenticates by seal and counterpart, not by cutting).
    - `corpus/knowledge/culture-material/vessel-container-lexicon.md`: `:115` containers as documents and chronometers — the map case, roll and archive chest as storage, cited at the boundary.
    - `corpus/knowledge/linguistics/naming-systems.md`: toponymy as a name system; the map's place-names are that file's assignment, not this entry's.
    - `corpus/knowledge/linguistics/writing-systems.md`: `:117` media bias (what survives), `:149` media-blind design, `:156` build step 2 (medium and tool from economy). The script side; this entry takes only the map's medium and reproduction.
    - `corpus/knowledge/civilizations/japan-medieval-sengoku.md`: `:157` — an Edo cadastral map is not a Sengoku map. Cited as the periodization caution for any map read as a direct window.
    - `corpus/knowledge/civilizations/polynesia-navigation.md`: `:52` horizon compass, steering-star sequence, sky mnemonic and latitude/landfall clue distinguished — navigation operations, not charts; cited to keep the boundary.
    - `corpus/knowledge/verification/calibration-registry.md` (sha256 `cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c`): `:78–88` CAL-03 (strong Whorf rejected; "weak relativity is always defensible" too broad) — the calibration posture borrowed for the "maps determine thought" claim.
    - `corpus/knowledge/verification/real-world-inspiration-boundaries.md`: `:6` the recheck line for restricted real-world material; every living tradition's restricted map or songline is routed here before any table is filled.
    - `corpus/knowledge/verification/myth-consistency-gate.md`: `:34` "do not expose restricted ritual knowledge to fill a table" — the access boundary applied to secret/sacred maps.
    - `corpus/knowledge/synthesis/worldbible-integration-contract.md`: the handoff target; this entry ends at the handoff and records nothing in canon.
    - `corpus/knowledge/synthesis/era-material-scoped-reconciliation.md`: era and material stages are separate clocks — a map's style date is not its survey date.
  - External standard shelf — **not consulted this round** (no network at seat time); author/year/title/publisher stated at book level, every edition, volume and page locator `(to-verify)`; no unread work is presented as inspected:
    - Harley, J. B., & Woodward, David (eds.), *The History of Cartography*, University of Chicago Press, 1987– — the standard reference; volume/book count and the volume covering portolan charts `(to-verify)`.
    - Harley, J. B. (1989), "Deconstructing the Map," *Cartographica* 26(2): 1–20 `(to-verify)` — the map-as-claim argument.
    - Wood, Denis (1992; 2nd ed. 2010), *The Power of Maps*, Guilford Press `(to-verify)`.
    - Monmonier, Mark (1991; 3rd ed. 2018), *How to Lie with Maps*, University of Chicago Press `(to-verify)`.
    - Jacob, Christian (French 1992; Eng. trans. 2006), *The Sovereign Map*, University of Chicago Press `(to-verify)`.
    - Ptolemy, *Geography*, trans. J. Lennart Berggren & Alexander Jones (2000), Princeton University Press `(to-verify)` — the projection/coordinate tradition.
    - Campbell, Tony (1987), "Portolan Charts from the Late Thirteenth Century to 1500," in *The History of Cartography* vol. 1 `(to-verify)` — page range and volume `(to-verify)`.
    - Edson, Evelyn (2007), *The World Map, 1300–1492*, Johns Hopkins University Press `(to-verify)`.
    - Kain, Roger J. P., & Baigent, Elizabeth (1992), *The Cadastral Map in the Service of the State*, University of Chicago Press `(to-verify)`.
    - Mundy, Barbara E. (1996), *The Mapping of New Spain*, University of Chicago Press `(to-verify)`.
    - Boone, Elizabeth Hill (2000), *Stories in Red and Black*, University of Texas Press `(to-verify)`.
    - Pickles, John (2004), *A History of Spaces*, Routledge `(to-verify)`.
    - Buisseret, David (ed.) (1992), *Monarchs, Ministers, and Maps*, University of Chicago Press `(to-verify)`.
    - Snyder, John P. (1987), *Map Projections: A Working Manual*, USGS Professional Paper 1395 `(to-verify)` — projection families and their distortions.
    - Dilke, O. A. W. (1971), *The Roman Land Surveyors*, David & Charles `(to-verify)` — the groma and centuriation chain.
    - al-Idrisi, *Nuzhat al-mushtāq fī ikhtirāq al-āfāq* (1154) — edition/translation `(to-verify)`.
    - *Tabula Peutingeriana* and the *Antonine Itinerary* — editions `(to-verify)`; the strip-itinerary form's surviving witnesses.
    - Ortelius, *Theatrum Orbis Terrarum* (1570), and Mercator's atlas — editions `(to-verify)`; the commercial atlas as a reproduction form.
- source: the lane-side authority is the in-corpus `path:line` anchor list above, each re-read at r47 HEAD `6e9a30d` on 2026-10-19, plus the absence-sweep commands recorded in `- gap filled:`; the charter citation is `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71,:102`. The external frameworks are the Tier B shelf above — Harley & Woodward, Harley 1989, Wood, Monmonier, Jacob, Ptolemy (Berggren & Jones), Campbell, Edson, Kain & Baigent, Mundy, Boone, Pickles, Buisseret, Snyder, Dilke, al-Idrisi, the *Tabula Peutingeriana*, Ortelius — **none fetched or inspected this run** (no network at seat time), so every edition/volume/page locator carries `(to-verify)`; the shelf supports mechanisms, never a claim about any fictional world. The map-form typology, the four-choice spine (what is measured / what is preserved / what is drawn / who may copy and read), the symbol grammar and the build order are this lane's design method assembled from those sources.
- couples: myth-symbol — `../myth-symbol/cosmology-cosmography.md` (owns the five-axis world model and the T-O symbolic diagram — `:71,:102`; this entry owns the measured, projected sheet and cites the disclaimer as its charter, not the typology); myth-symbol — `../myth-symbol/sacred-topography-pilgrimage.md` (owns the holy-site typology, the route as rite and the sacred-geography diagram — `:5`; this entry owns how a route is surveyed and drawn and cites the route types as map content); myth-symbol — `../myth-symbol/direction-symbolism.md` (owns the orientation register and the true-vs-magnetic compass trap — `:51`; this entry owns the map convention: orientation choice, compass rose, north arrow); culture-material — `architecture-settlement-lexicon.md` (owns the built plan, the castrum grid and the groma sentence — `:95`; this entry owns land survey as a map-production step and does not restate the settlement vocabulary); culture-material — `writing-media-surface-economy.md` (owns the seven surface families and the cost ladder — `:3`; this entry owns map-specific media and reproduction — parchment, paper, cloth, copperplate, manuscript vs print, the atlas); culture-material — `transport-mobility-lexicon.md` (owns routes, vehicles and the maintenance rule — `:28,:117`; this entry owns the representation of a route and cites the maintenance rule); culture-material — `timekeeping-instruments.md` (owns the instrument families and the minute's applications — `:50` longitude at sea; this entry owns the coordinate problem the map inherits, not the instruments); culture-material — `material-culture-inference-method.md` (owns the inference ladder, the perishability constraint and the anti-determinism guard — `:69,:76`; this entry applies them to map survival and to "the map caused the state"); culture-material — `craft-artisan-lexicon.md` (owns the workshop register and the material-grading vocabulary — `:44`; the mapmaker's workshop is a craft case in that file's terms); culture-material — `trade-economy-lexicon.md` (owns measures, weights and contract vocabulary — `:92,:121`; this entry owns the map as a legal/territorial instrument at the boundary with split-object authentication); culture-material — `vessel-container-lexicon.md` (owns containers as documents and chronometers — `:115`; the map case, roll and archive chest are storage, cited at the boundary); linguistics — `../linguistics/naming-systems.md` (owns toponymy; the map's place-names are that file's assignment, not this entry's); linguistics — `../linguistics/writing-systems.md` (owns script typology and media bias — `:117,:149,:156`; this entry takes only the map's medium and reproduction, not the script side); civilizations — `../civilizations/mesoamerica-primary-sources.md` (owns the lienzo/cartographic-history source class and its provenance — `:58`; this entry cites the genre and does not restate the manuscript inventory); civilizations — `../civilizations/polynesia-navigation.md` (owns horizon compass, steering-star sequence, sky mnemonic and landfall clue — `:52`; navigation operations are distinguished from charts and are not re-owned here); civilizations — `../civilizations/japan-medieval-sengoku.md` (owns the periodization caution that an Edo cadastral map is not a Sengoku map — `:157`; this entry cites it as the rule for reading any map as a window); verification — `../verification/calibration-registry.md` (owns the calibration posture — `:78–88` CAL-03; a "map determines thought" claim is braked with the same test); verification — `../verification/real-world-inspiration-boundaries.md` and `../verification/myth-consistency-gate.md` (own the restricted-knowledge boundary — `:6` and `:34`; every living tradition's restricted map or songline is routed there before any table is filled); synthesis — `../synthesis/worldbible-integration-contract.md` (the handoff target; this entry records nothing in canon); synthesis — `../synthesis/era-material-scoped-reconciliation.md` (era and material stages are separate clocks — a map's style date is not its survey date).
- verified-at: 2026-10-19 — written at r47 HEAD `6e9a30d` (`git rev-parse HEAD` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`, equal to `reports/round-47/claims.json:7`). Measured with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: `find corpus/knowledge -name '*.md' | wc -l` → **223**; `ls corpus/knowledge/culture-material/*.md | wc -l` → **25**; `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}, totals_line 223, footer `25/26/25/29/24/94`, exit 0; the proposed slug is unused and the sort position is between `calendar-festival-systems.md` (5th) and `costume-semiotics.md` (6th). Every in-repo `path:line` anchor in this head block was checked mechanically in this seat: 23/23 needle-in-line assertions passed and 21/21 couples paths resolve relative to `corpus/knowledge/culture-material/` (re-runnable instrument `.scratch/c04/anchors.py`, transcript in this seat fragment). `corpus/README.md` sha256 at write time `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`; its rev-2.4 prose vector sums **217**, not 223 — a defect for the integrator's rev-2.5 edit, not repaired in the corpus by this seat. **No external source was fetched or inspected**: every Tier B item is `(to-verify)` for edition, volume and page. **Not claimed:** any portolan accuracy figure, any projection-distortion table value, any print-run or price number, any survival percentage.
- recheck: before any map, survey or territorial claim becomes load-bearing in a world bible — re-run the form typology against the map's question (a cadastral map and a portolan answer different questions); re-read `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102` before repeating any flat-earth/T-O calibration and `:71` before letting a symbolic diagram stand in for a survey map; re-read `corpus/knowledge/myth-symbol/direction-symbolism.md:51` before fixing true north, magnetic north or an east-at-top convention; re-read `corpus/knowledge/culture-material/architecture-settlement-lexicon.md:95` before treating a castrum grid as a survey (the grid is a plan; the groma is the chain); re-read `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58` before citing a lienzo as evidence of a cartographic practice; re-read `corpus/knowledge/culture-material/material-culture-inference-method.md:69` before treating a surviving map as evidence of its own importance (parchment and vellum survive; cloth and bark do not); re-read `corpus/knowledge/culture-material/transport-mobility-lexicon.md:28,:117` before drawing a route no institution maintains; and route every living tradition's restricted map or songline through `corpus/knowledge/verification/real-world-inspiration-boundaries.md:6` and `corpus/knowledge/verification/myth-consistency-gate.md:34` before filling any table. Corrections to this entry are new sections or a new entry, never rewrites.
- scope: reference method and lane policy for the culture-material partition. This entry owns the map as a made instrument and a claim — the survey chain, projection and scale, symbolization, reproduction, and the map's silences. It does not own the world model or the T-O symbolic diagram (`../myth-symbol/cosmology-cosmography.md`), the holy-site typology and route-as-rite (`../myth-symbol/sacred-topography-pilgrimage.md`), the direction register (`../myth-symbol/direction-symbolism.md`), the settlement vocabulary (`architecture-settlement-lexicon.md`), the writing-surface economy (`writing-media-surface-economy.md`), the vehicle-and-road system (`transport-mobility-lexicon.md`), or toponymy (`../linguistics/naming-systems.md`). It decides nothing about any world — no border, no charter and no survey is authorized by this file — and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff. Restricted real-world material is screened by `../verification/real-world-inspiration-boundaries.md`, not here.
````

### 2.1 Field-by-field rationale (for the integrator, not part of the entry)

| field | why it is worded this way | evidence |
|---|---|---|
| H1 | names the object and the four-part spine so the body's sections have a stated thesis | K02 §4.3 master claim |
| `- topic:` | **byte-equal to `reports/round-44/scout/K02-gap-scout.md:227`**; the sweep compares README row text to this field (`reports/round-28/readme/sweep.py:61,74-75,139-140`), so C09 must copy it verbatim | `diff` in §4.1 |
| `- gap filled:` | carries the live r47 counts, the r44 outcome line, and the one loose `itinerar` hit; a "no owner" claim without counts is the r43 defect | §1.2–1.3 |
| `- sources:` | Tier A is `path:line`-anchored and sha-pinned; Tier B is book-level only with every edition/page `(to-verify)` — no unread work is presented as inspected | §4.2 |
| field order | deliberately the measured 8-field culture-material convention — `topic, gap filled, sources, source, couples, verified-at, recheck, scope` — as in `timekeeping-instruments.md:3-10` and `bathing-and-body-hygiene.md:3-10`; **no `- calibration:` field**, because the newest entries keep the bank in the body (C07-47 F5) and this seat's mission lists eight fields. The six statuses live in C03's calibration bank; the header's `- recheck:` keeps the discredited readings visible. | `timekeeping-instruments.md:3-10`; `reports/round-47/cov/C07-contract-audit.md` F5 |
| `- couples:` | 21 tokens, each resolving relative to `corpus/knowledge/culture-material/`; each names what the neighbour owns and what this entry owns instead | §4.3 |
| `- source:` | separates lane-side authority (in-corpus anchors) from external framework (shelf), and states the no-network limit | — |
| `- verified-at:` | measured counts, anchor checks, README digest, and an explicit "not claimed" list | §4.1–4.3 |
| `- recheck:` | seven re-entry points keyed to file:line, plus the restricted-knowledge route | — |
| `- scope:` | the one-owner boundary in prose, mirroring the `couples:` boundaries; no canon, no verdict | `corpus/QUALITY.md:18-20`; `PROVINCE.md:16-19` |

---

## 3. Integration contract (what the integrator must do with this block)

1. **Target path:** `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (A, not M — the path does not exist at `6e9a30d`; verified in §1.2). If any later seat lands that path first, this block must be re-checked against the live tree before applying; do not overwrite.
2. **Apply order:** the fenced block's head is the first bytes of the file; the body sections drafted by C01/C02/C03 start at the first `## ` heading. The head block must not be reflowed — the `- topic:` line is one physical line and must stay one line (`sweep.py`'s `TOPIC_RE` stops at the next `- word` line; a hard wrap would truncate the topic).
3. **README rev 2.5 (C09):** the new row is inserted between `calendar-festival-systems.md` and `costume-semiotics.md`, in the form ``- `cartography-and-mapmaking.md` — <topic text>`` where `<topic text>` is the `- topic:` value **byte-for-byte**. Header `## culture-material/ (25)` → `(26)`; totals 223 → 224; footer vector `25/26/25/29/24/94` → `25/26/26/29/24/94`; repair the rev-2.4 prose vector at `corpus/README.md:11` (sums 217) in the same edit.
4. **No corpus write by this seat.** This file is the draft; nothing under `corpus/` was staged, touched or created.
5. **Collision status: none.** Zero filename owners, zero topic-line owners, slug unused, sort position free. The nearest neighbour `sacred-topography-pilgrimage.md:5` is coupled, not duplicated; the cosmology T-O disclaimer is cited, not absorbed.

### 3.1 Predicted post-landing state (for C10's staged sweep, not measured here)

| anchor | now | after |
|---|---|---|
| `find corpus/knowledge -name '*.md' \| wc -l` | 223 | 224 |
| `ls corpus/knowledge/culture-material/*.md \| wc -l` | 25 | 26 |
| README `## culture-material/ (N)` | 25 | 26 |
| README totals line | 223 | 224 |
| README footer vector | 25/26/25/29/24/94 | 25/26/26/29/24/94 |
| sweep | rows 223 files 223 | rows 224 files 224, exit 0 |

These are predictions, not measurements; C10 stages the tree in `.scratch` to measure them.

---

## 4. Self-audit

### 4.1 Topic byte-equality with the r44 seed

```
$ python3 - <<'PY'
import re
seed = open('reports/round-44/scout/K02-gap-scout.md', encoding='utf-8').read().splitlines()[226]
mine = [l for l in open('reports/round-47/cov/C04-entry-header.md', encoding='utf-8').read().splitlines() if l.startswith('- topic: the map as an instrument')]
print('seed_len', len(seed), 'mine_len', len(mine[0]) if mine else None)
print('byte_equal', seed == mine[0] if mine else False)
PY
seed_len 775 mine_len 775
byte_equal True
```

(Line 227 of the seed is the `- topic:` line; the local index is 226.)

### 4.2 Anchor check (the instrument, re-runnable)

`.scratch/c04/anchors.py` asserts a needle substring on each cited line and resolves every
couples token from the entry's directory:

```
anchors checked 23; failures 0
couples checked 21; unresolved 0 []
```

The 23 assertions cover `cosmology:71,:102`, `sacred-topography:5`, `direction:51`,
`architecture:95`, `writing-media:3`, `transport:28,:117`, `timekeeping:50`,
`material-culture-inference-method:69,:76`, `japan-sengoku:157`, `mesoamerica:58`,
`polynesia:52`, `writing-systems:117,:149,:156`, `calibration-registry:78`,
`real-world-inspiration-boundaries:6`, `myth-consistency-gate:34`,
`dialect-faction-map-workflow:2` (the "map is a verb" false positive),
`craft-artisan:44`, `vessel-container:115`. All 23 pass.

### 4.3 Couples resolution

The 21 tokens in the `- couples:` line were resolved against
`corpus/knowledge/culture-material/` (direct paths with `../` where cross-partition); 21/21
resolve. The resolver's own policy (`tools/harness/basename-couples-resolver.py:144-160`)
accepts Tier-1 direct resolution from the entry directory, which is what these are.

### 4.4 Pre-staging conformance (C07 field contract)

The fenced block was extracted to `.scratch/c04/head-block.md` and checked against C07's
pre-staging contract (`reports/round-47/cov/C07-contract-audit.md` §7): H1 exactly one; the
eight fields present **and in convention order**; no extra head field; topic one physical line.

```
topic byte_equal: True len: 775 775
fields found: ['topic', 'gap filled', 'sources', 'source', 'couples', 'verified-at', 'recheck', 'scope']
all present: True
order ok: True
extra head fields: []
H1 count: 1
head length: 51 lines
```

`provenance-audit.py` on the same head block: `findings=0 blocked=0`, exit 0
(`INFO to-verify-count … 22 mark(s) on 21 line(s)`). This is a **head-block** result, not a
whole-entry verdict: the calibration vocabulary required by `corpus/QUALITY.md:9-12` is carried
by C03's calibration bank, and the whole-entry audit is re-run after assembly.

### 4.5 What this seat did **not** do

- No external source was fetched or read (no network): every Tier B edition/page is `(to-verify)`.
- No body section was written (C01–C03 own §§1–15); this block stops at the head.
- No README edit (C09/integrator own rev 2.5); the rev-2.4 defect is flagged, not repaired.
- No corpus write, no git commit, no round-runner execution; the only files written are this one
  and the disposable `.scratch/c04/anchors.py` instrument.

### 4.6 To-verify list (carried honestly)

1. Every Tier B edition, volume and page locator (18 shelf entries) — no network at seat time.
2. The exact volume/book count of *The History of Cartography* — deliberately not asserted;
   the shelf says "volume/book count `(to-verify)`" rather than a guessed number.
3. Campbell 1987 page range — `(to-verify)`.
4. Whether a later seat (C01–C03) changes the body's section numbering; this block names no
   section number for the calibration bank precisely so the head does not drift from the body.
5. The README row text depends on `- topic:`; if any seat proposes a topic change, the change
   must be made in **both** places in the same edit, and this block's byte-equality claim is
   void until re-checked.

---

## Owed

- **C09/integrator:** README row byte-equal to §2's `- topic:`; rev-2.5 header/totals/footer;
  repair `corpus/README.md:11`.
- **C01–C03:** body sections under this head block; no restatement of the coupled neighbours.
- **C05:** re-verify the slug at landing time (this seat measured it unused at `6e9a30d`).
- **C06:** audit the Tier A anchors against the assembled draft (23/23 already checked here).
- **C07:** contract audit against `corpus/QUALITY.md:5-20` (this block cites all five clauses).
- **C13:** couples resolution (21/21 already checked here from the entry directory).

No blocker. The head block is integration-ready.
