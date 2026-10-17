# Review — component 10-materials (culture D2)

- reviewer: round-4 REVIEW worker, materials assignment
- target: `examples/culture-d2/components/10-materials.yml` (670 lines)
- reviewed revision: sha256 `11a374d3a5b937a49ed10dc3026a1b681332e6081060ff5710e85a28d519865d`
- principal reference: `corpus/knowledge/culture-material/textile-technology.md` (TT), sha256 `993ea708614a908472e834e66dbee43c49f4f7de2eecbbcbe5a4435b9cd6a6d9`
- verdict: **FINDINGS — 8: 3 REJECT contradictions and 5 HOLD dependencies/data issues**; not material-ready for unqualified packet use
- canon: **NON-CANON** design review; lore-shokunin owns canon

## Scope and standard

Checked plateau availability, seasonality and route eras, fiber preparation, dye chemistry/auxiliaries, loom/finish bounds, and the proposed costume interface. All 670 target lines and all 101 TT lines were read in windows of at most 120 lines. Related files were read only for the cited contracts and procedures; this is not their full review.

Additional reference abbreviations:

- CG: `corpus/knowledge/verification/costume-era-consistency-gate.md`, §§2–5, 7–9: distinguish contradiction from missing evidence; trace inputs and operations; do not infer an exact loom from weave alone.
- MC: `corpus/knowledge/culture-material/material-culture-inference-method.md`, §§3–6: production chains, fuel/transport/seasonality, and constraints rather than determinism.

REJECT below means a contradiction between this design's own declarations, not a historical impossibility or a canon ruling. HOLD means the evidence or interface is incomplete. A declared fictional ecology is permissible; an unverified analogue remains `(to-verify)`. Tool-arrival dates are this drill's choices, not universal real-world invention dates.

## Findings

### M10-R01 — HOLD: era slots are not an executable shared chronology

- **Evidence:** `examples/culture-d2/components/10-materials.yml:65–99` makes E1 the closed, pre-road inventory, E2 road opening, and E4 script/media arrival. Its E0 is mythic only (`:100–103`). The concurrently revised `examples/culture-d2/components/09-eras-calendar.yml:20–25,44–49,88–98` explicitly maps contract E0 to the pre-script strata, E1 to script arrival, E2 to the literate anchor, and E3 to a prospective stratum. The target's `:19` promises mapping at integration; OH-03 (`:657–659`) already flags part of the seam.
- **Bound/consequence:** CG §2 requires a local interval; §§7–8 keep access and documentary clocks separate. Literal same-number merging would misdate imports, grades, and writing surfaces. The revised `11-costumes.yml:62–66` still marks its proposed mapping of 10-materials slots `(to-verify)`; it is not a resolved alias contract. In particular, that proposal puts script arrival at the target's E2 road seam, earlier than WM-01..03's E4-only media. The shared 09/11 E0–E3 tag fix does not by itself settle this older inventory's chronology.
- **Smallest repair/recheck:** integration must approve an explicit slot-to-contract/named-interval mapping and resolve the first writing-surface/access date. Do not merely subtract one from every E-number or move all systems together. This confirms and expands the existing OH-03 HOLD; it does not decide a new chronology.
- **Supporting snapshots:** 09 and 11 were refreshed to revision 1.1 during review; sha256 respectively `540a9339627fdcb802a7f59915a3c72e8234fff37c4a771783382af9c863b030` and `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22`. Recheck these interface references if those files change again.

### M10-R02 — REJECT: mandatory G2 shearing precedes the declared shears

- **Evidence:** E1 expressly has no shears (`10-materials.yml:70–72`); imports and imported-shear finishing start in E2 (`:78–81,452`). Nevertheless G2 is available in E1 (`:461–464`) and its finish is unconditionally “nap-raised and sheared” (`:465`). G1's optional “shear-touched” finish (`:458`) also needs era qualification.
- **Bound/consequence:** TT §1 finish gate and §5's shearing operation; CG §3 T/E and §5 operation dependencies. The declared E1 G2 production route requires an operation outside its own available tool chain. No alternative nap-cropping route is declared.
- **Smallest repair/recheck:** distinguish an E1 unsheared finish from the E2+ sheared finish, or move the sheared grade's availability. If an early substitute is intended, explicitly supply its material and operation before re-review; do not silently invent it to clear the finding.

### M10-R03 — REJECT: E3 yellow/green is supplied with seed, not harvested weld

- **Evidence:** MAT-12 imports seed in E3 and supplies local harvested dyestuff only in E4 (`10-materials.yml:235–243`). Yet DP-04 offers fast yellow/overdye green in both E3 and E4 (`:403`), the E3 summary calls weld an entering dyestuff (`:86–87`), and RT-3 moves valley-plot harvest from E3 (`:501`). RT-m12a labels a seed lot `stage: dye`; that label does not supply the missing harvest.
- **Bound/consequence:** TT §1 fiber/dye gates, §3 weld row, and §7.2 supply-chain requirement; CG §4 MAT-02/03/04 and §7 access clock. On the written routes, E3 lacks a usable weld supply for the stated color. Indigo and alum being available does not supply the yellow component of green.
- **Smallest repair/recheck:** either restrict plot-harvest color use to E4 and reconcile the summary/RT-3, or declare a separately sourced E3 harvested-dyestuff route or first harvest. This is not a claim that weld biologically cannot produce in its first season; climate, sowing and harvest timing were not established here. Madder is explicitly imported dried root in MAT-11 (`:225–233`); the summary's broader seed/plot wording must not be read as an evidenced local madder crop either.

### M10-R04 — REJECT: the reserved fleece allocation contradicts G2's composition

- **Evidence:** MAT-01 reserves the fine combed clip for “G2-G3” (`10-materials.yml:124`), repeated in BULK-05 (`:377`). G2 explicitly has “no combed content” (`:463`); only G3 specifies combed fiber (`:470`).
- **Bound/consequence:** TT §2's carded/combed fork and CG §4 MAT-01 require actual composition, not interchangeable grade labels. These two descriptions cannot both identify G2's input. This is a stock-allocation contradiction, not a claim that combed wool cannot be felted.
- **Smallest repair/recheck:** reconcile the reserved fleece destinations with the intended G2/G3 compositions and export stock, without changing unrelated rank assignments. The grade rationale at `:475` also needs qualification: TT §2 lists washing separately from harvesting, so “without shears there is no clean fleece” is not established by that source. Retain the chosen E2 tool/grade seam as DESIGN, not proof that plucked fleece cannot be cleaned.

### M10-R05 — HOLD: the local woven-fiber chain skips operations and tool sourcing

- **Evidence:** RT-m01b calls locally herded fleece `kind: import` because the shears arrive by road (`10-materials.yml:115–122`); RT-m01c/d label combing/carding as `stage: yarn` without a spinning operation. LM-01/02 promise local framed weaving from E1 (`:417–430`), while E1 excludes every import (`:69–74`) and BULK-03 calls the plateau treeless (`:361`). Frame/beam stock and the preparation/yarn-making tool chain are not sourced. Stone weights alone do not resolve that chain.
- **Bound/consequence:** TT §§1–2 distinguish preparation from spinning and weaving; MC §6 steps 0/2 and CG §§4–5 require an actual production route. Highland weaving is not ruled out, but the closed E1 inventory does not yet explain the claimed kit. Nettle's retting/hackling and spinning need the same operation-level treatment.
- **Smallest repair/recheck:** separate local fleece production from imported tool access, name the actual yarn-making operation, and declare an E1-compatible source for frame/preparation equipment or a different realizable construction. Local material, inherited kit, or a nonwood alternative may be proposed, but none is assumed by this review. Do not require a spinning wheel or iron equipment merely because yarn is fine.

### M10-R06 — HOLD: dyestuff identity is stronger than the supplied dye recipes

- **Evidence:** MAT-08 supplies indigo cakes and names reduction/oxidation (`10-materials.yml:190–201`), but its E2 auxiliary is only “lichen-free alkali” (`:79`); calibration already leaves its availability unresolved (`:643`). No reducing/fermentation input or operating chain is specified. MAT-09/MAT-19/WM-01 share scrub tannin and smith scale (`:202–213,302–309,521–528`), but neither identifies the tannin-bearing plant nor establishes how the scale supplies usable iron for the asserted fast black and ink. MAT-14 supplies carthamin-class cakes without a substrate/process specification (`:254–261`).
- **Bound/consequence:** TT §1 dye gate and §3 distinguish a reduced vat from a mordant/direct process; CG §4 MAT-04 requires auxiliaries, substrate, water/fuel and knowledge separately. TT supports indigo, tannin–iron black, madder/alum red, weld/alum yellow and safflower pink as classes; it does not verify these particular plateau recipes. Treat the vat, scale-to-mordant/ink conversion, tannin species and pink-on-intended-fiber recipe as `(to-verify)`, not impossible.
- **Smallest repair/recheck:** specify an era-accessible process and auxiliary supply for each claimed dye/substrate, with a cited bounded recipe or prototype. Dung already supplies a possible heat source; do not manufacture a charcoal shortage for household dyeing. Locate process water and winter access alongside wind-based siting: the no-water-imagery rule is not a physical exemption from wet processing (`:314,616`). Fastness and routine availability remain unverified until those inputs are resolved.

### M10-R07 — HOLD: treadle weaving does not establish “machine-even weft”

- **Evidence:** MAT-07 supplies E4 lowland treadle-woven broadcloth (`10-materials.yml:181–189`); LM-04 calls its tell “regular twill repeat and machine-even weft” (`:437–442`).
- **Bound/consequence:** TT §4 distinguishes hand/treadle repeat and density regularity from the industrial row's machine-even threads; its forensic paragraph distinguishes handspun slubs from machine evenness. CG §5 also bars inferring an exact machine from a weave alone. Nothing in the stated import route establishes a mechanized yarn chain. Conversely, a very even hand-produced cloth is not proof of a factory.
- **Smallest repair/recheck:** describe the actually supported density/repeat signature, or supply the additional production evidence if “machine-even” is meant literally. Keep broadcloth imported and its finishing delegated; no real-world invention date is imposed on this fictional era.

### M10-R08 — HOLD: an attached comment destroys one typed provenance list

- **Evidence:** `10-materials.yml:335` ends MAT-22's list with `]# ---` rather than a separated comment. Loading the unchanged file with the existing costume gate's `parse_packet` returns `type(materials[-1]['follows']).__name__ == 'str'`, not `list`.
- **Bound/consequence:** the component promises per-record corpus locators; `corpus/QUALITY.md` §1 requires checkable provenance. The gate's documented subset parser does not validate this extra field, so its acceptance of the file is not a typed-record check. This observation does not assert that a conforming YAML parser was run; PyYAML is not installed.
- **Smallest repair/recheck:** separate the comment onto its own line or supply the missing comment delimiter spacing, then confirm MAT-22's `follows` remains a list with the same two locators. No content or gate change is required.

## Availability ledger — all 22 material records

E1–E4 below are **the target's local slots**, not the contract's identical-looking tags (M10-R01). “Plausible” means the declared route fits the fictional premise at this resolution, not measured production capacity.

| ID / item | Declared access | Ecology / realism disposition |
|---|---|---|
| MAT-01 ewe-fleece | E1 plucked; E2+ shearing/combing tools | Herd/transhumance premise fits; reconcile local/import stage and grade allocation (R04/R05). Breed, harvest timing and staple are design inputs, not verified real-world dates. |
| MAT-02 felt | Local E1–E4 | Wool nonwoven, warmth/water sites and wind drying are coherent; E1 sheared G2 is not (R02). No loom is required for felt. |
| MAT-03 ox-hair cordage | Local spring shedding, E1–E4 | Plausible coarse-hair cord as an explicit herd-analog premise; do not silently treat it as fine down. No imported fiber required. |
| MAT-04 nettle-bast | Local scrub cutting/retting, E1–E4 | TT §2 permits minor bast; species, altitude and winter retting remain `(to-verify)`. This does not establish a flax crop. |
| MAT-05 lowland plant cloth | Finished cloth imported E2–E4; E1 excluded | Coherent route despite unsuitable local cultivation. TT §2's flax comparator supports emphasis on whiteness/count, not an automatic bright-dye claim. |
| MAT-06 lowland plant cord | Yarn/cord imported E2–E4; E1 excluded | Stage is declared; imported cord need not imply local plant cultivation. |
| MAT-07 lowland broadcloth | Finished cloth imported E4 only | Partner supplies weaving/finish; local finish ceiling is respected. Forensic overstatement remains R07. |
| MAT-08 indigo | Cake imported E2–E4; E1 excluded | Organism→processing→pass→licence chain is explicit; plateau vat auxiliaries remain R06. No local Indigofera cultivation is claimed. |
| MAT-09 wool-black | Local processing E2–E4; leather darkening E1+ | Tannin/iron class is corpus-grounded; iron still depends on E2 imported stock/forge. Leather's earlier tannin treatment is not an E1 iron-black cloth supply. R06 applies. |
| MAT-10 hearth-dark | Local smoke process E1–E4 | Correctly separated from a molecular dye and explicitly abrasion-fugitive; no fastness certification implied. |
| MAT-11 madder root | Dried root imported E3–E4 | Alum also arrives in E3; red class is plausible. No evidenced local seed-to-root crop or Turkey-red process is supplied. |
| MAT-12 weld | Seed imported E3; local harvest E4 | Yellow/green use and RT-3 prematurely begin in E3 (R03); valley growing-season suitability remains `(to-verify)`. |
| MAT-13 alum | Mordant imported E3–E4 | Route supplies the red/yellow auxiliary in the same slots; source region/shipping form explicitly unresolved. Not interchangeable with edible salt. |
| MAT-14 pink | Dyestuff cake imported E4 | Safflower-class, scarce/fugitive description is calibrated; intended fiber/recipe still needs R06. |
| MAT-15 sky-iron | Rare local finds/cold work E1–E4 | Explicit DESIGN with comparator gap retained. This is not evidence of local ore, bulk smelting, or early shears. |
| MAT-16 trail-iron | Stock imported E2–E4; local reforging | No local ore needed; imported charcoal constrains the forge. Tool arrival is a chosen local event. |
| MAT-17 bronze | Imported stock/castings E3–E4 | Partner foundry route is plausible. Any scale claim for local recasting still needs its own process/capacity evidence. |
| MAT-18 silver | Imported by weight E3–E4; coins as metal E4 | Coherent separation of weighed metal from locally minted coinage; no metal-age ladder is inferred. |
| MAT-19 smith-scale | Forge reuse E2–E4; E1 excluded | Era matches imported iron/forge; chemical conversion to useful mordant/ink is unresolved (R06). |
| MAT-20 herd-hide | Local tanning E1–E4; writing preparation E4 | Herd source fits; scrub-tannin supply and process water still matter. “Prepared hide” alone is not a verified parchment recipe. |
| MAT-21 sinew/gut thread | Local herd processing E1–E4 | Plausible explicit seam input; durability/storage under wet weather have not been measured. |
| MAT-22 horn/bone/antler | Local closures E1–E4 | Avoids hidden early metal closures; antler-bearing source is unspecified if actually used `(to-verify)`. Provenance-list delimiter needs R08. |

## Bulk goods, freight and writing surfaces

| Bulk ID | Availability / route check |
|---|---|
| BULK-01 salt | High-pan/lick harvest E1+; down-road trade E2+. A fictional saline plateau is stipulated, not inferred from altitude alone. Pan hydrology/yield is unmeasured. |
| BULK-02 dried meat | Autumn low-camp production E1+; exports require the E2+ road. With no winter traffic, storage and dispatch before closing or in the next opening need a calendar/stock plan; no contradiction is proved without dates/losses. |
| BULK-03 dung | Local dried fuel E1–E4 coherently avoids a forest-dependent household economy. Fuel volume and competition with soil/fodder needs were not quantified. |
| BULK-04 charcoal | Imported sacks E2–E4; E1 excluded. Fuel, rather than local ore, is honestly the forge bottleneck. No unpriced local charcoal source is assumed. |
| BULK-05 grease wool | E2+ down-cargo can fund imports in principle; fine-clip allocation needs R04. Exchange sufficiency and pack throughput are not demonstrated. |
| BULK-06 grain | E2+ bulk up-cargo; E1 excluded. This does not prove an E1 grain dependency, nor does calling grain “ballast” establish affordable transport. |

RT-1 gives one seasonal pass and both endpoints (`10-materials.yml:480–491`); RT-2/3 are internal supply paths. No import exclusion overlaps a declared material route's era in the 22-record parser check. That bookkeeping consistency does **not** detect the seed/harvest or finish/tool contradictions above. No pass capacity, traffic volume, winter stock or production yield is fabricated to turn these qualitative routes into a scale PASS (CG §4 MAT-05/08; MC §4).

WM-01 ink, WM-02 prepared hide and WM-03 imported paper are all explicitly E4 (`:521–543`). Their existence as material categories is plausible; R01/R06 and the unverified hide-preparation chain prevent an unqualified writing-substrate clearance. Paper names its imported sheet stage, but no independent paper-making industry is claimed at home.

## Existing calibration flags — all 7 rows retained

These are dispositions for this review, not a FRESH triage ledger or verification of real-world scholarship. The fourteen pending LR surface-form requests are a separate lexical handoff, not fourteen additional empirical flags.

| Target calibration row | Review disposition / basis |
|---|---|
| `:640` meteoric-iron comparator | RETAIN `(to-verify)`; no specific object, experiment or corpus comparator was independently established here. Keep rare toolmaking provisional. |
| `:641` nettle species/retting | RETAIN `(to-verify)`; TT §2 supports nettle as a fiber category, not this altitude or winter pool process. |
| `:642` plucking/shearing transition | RETAIN `(to-verify)` for real-world dating; DESIGN for the fictional seam. TT's fleece-selection chronology does not establish a universal tool date or the “no clean fleece” claim. |
| `:643` vat alkali | RETAIN `(to-verify)`; R06 identifies the missing auxiliary/process chain. Stale urine in a fulling comparator does not by itself certify an indigo vat recipe. |
| `:644` alum source/shipping form | RETAIN `(to-verify)`; the imported mordant route is declared, but no actual source locality or preparation was verified. |
| `:645` script-era seam | RETAIN / expand to R01; shared contract tags and first media access must be reconciled, not merely renamed. |
| `:646` no invented rates | RETAIN as a calibration guardrail, not a measured result. OH-06 correctly requests physical throughput tests; no quantity/capacity PASS follows from their absence. |

## Executed checks and limits

- `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d2/components/10-materials.yml` → **exit 2**, exactly ``FINDING G-DATA: [could-not-evaluate] no `costumes` declared: nothing to review``. This matches the target's `gates_interface.self_run_note`; it is neither a failing outfit nor a clean material review. The eight findings above are manual-review findings, not eight emitted kernel lines.
- Read-only `python3 -B`/`runpy.run_path` check with the existing gate's `parse_packet`: **22 materials / 29 material routes; 6 bulk goods; 4 cloth sources; 3 grade rungs; 3 trade routes; 6 measures; 3 writing media; 14 lexicon requests; 6 open handoffs; 4 fast and 2 fugitive palette entries; 7 calibration rows**. Supplied/excluded era overlaps: zero in each local slot. MAT-22's `follows` type is `str` (R08). `-B` avoids writing import caches.
- `python3 tools/assemble-d2.py --check` initially returned **exit 0**, `packet.d2.yml: byte-identical deterministic assembly`. After concurrent round-4 component fixes, the final recheck returned **exit 1**, `packet.d2.yml differs from deterministic assembly`. The caller must reassemble and rerun closure after the workers settle; this review does not claim a current packet PASS and did not rewrite the packet. The round-3 extraction record `examples/culture-d2/ASSEMBLY.md:28–32` takes material/cloth-source blocks from **11-costumes**, not this 10-materials inventory; that assembly path does not exercise this substrate as a costume source.
- The review's own count/whitespace check passed: 8 unique finding headings (3 REJECT / 5 HOLD), 22 material rows, 6 bulk rows, 7 calibration rows, no trailing whitespace. Both pinned target/TT hashes were rechecked unchanged.
- No chemistry prototype, fleece/ret timing test, freight-capacity trial, conforming YAML parse, or external citation verification was performed. TT supplies comparative classes and constraints, not a plateau species list, universal rates, or passage-level proof for the new recipes. No real-world citation has been invented.
- Review scope only: target component, corpus, gates, packet, sibling reviews and `LOG.md` were not edited by this worker; no commit was made. Concurrent workers changed other paths. The caller must handle any required log/round bookkeeping outside this worker's permitted write scope.

**Handoff counts:** 1 new review file; 8 findings (3 REJECT / 5 HOLD); 22 material-ledger rows + 6 bulk-ledger rows; 7 existing calibration rows retained (6 uncertainty subjects + 1 rate guardrail). Other explicitly unverified resource/process details above remain caveats, not silently closed evidence.
