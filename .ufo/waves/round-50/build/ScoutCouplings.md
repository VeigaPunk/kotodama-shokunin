# ScoutCouplings — in-corpus coupling inventory for claim C (`pastoralism-animal-husbandry.md`)

Seat: `ChousaR27R2.ScoutCouplings-4` (scout, leaf). Round 50, claim C. Base
`4ad26836552462d28a946ca3b067cab0b5ce3532`. Author-lane advice, never admission.
Read-only: no lane file edited, no clone, no patch, no git/jj command, no installs, no
network opened by this seat. Hashing was `sha256sum <path>` on the lane working tree,
2026-10-21.

## Result at a glance

- All **17** assigned coupling targets exist; **0 missing**. Every file hashed, owner line
  and body seam anchors pinned below.
- The register is genuinely unowned: **0** topic owners corpus-wide for
  pastoral/pastoralism/herding/husbandry/transhumance/livestock, **0** filename
  owners, **0** `nomad`/`pasture`/`transhuman` filename owners, **0** section headers naming
  herd/pastoral/husbandry/livestock, **0** forward references to the new filename.
- Live counts at seat time: total **225**, culture-material **27**, vector
  `25/26/27/29/24/94`; SOURCES registry has **47** rows (`| S001`…`| S047`), so the next id is
  **S048** — and three sibling frontier seats have each drafted a candidate *as* S048
  (`SrcZederDomestication.md`, `SrcUnescoGer.md`, `SrcDysonHudson.md`); **L1 must assign
  distinct ids** and C must cite the assigned ids.
- README insertion point is exact: row goes at `corpus/README.md:286`, between
  `music-instrument-lexicon.md` (:285) and `ritual-garments.md` (:286).

## Freshness evidence (the gap premise, re-measured)

Commands run from the lane root, 2026-10-21:

```
grep -rliE '^- topic:.*(pastoral|herding|husbandry|transhumance|livestock)' corpus/knowledge/ | wc -l   -> 0
grep -rliE '^- topic:.*\bnomad' corpus/knowledge/                                                      -> (no output)
find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l            -> 0
find corpus/knowledge -iname '*nomad*' -o -iname '*transhuman*' -o -iname '*pasture*' | wc -l          -> 0
grep -rniE '^#{1,4} .*(herd|pastoral|husbandry|livestock|transhuman)' corpus/knowledge/ | wc -l        -> 0
grep -rn 'pastoralism-animal-husbandry' corpus/ | wc -l                                                -> 0
```

One substring false positive to keep out of the entry's gap paragraph:
`corpus/knowledge/culture-material/writing-media-surface-economy.md:3` matches `herd` only
because it contains **sherd** (`:51`,`:55`,`:75`,`:96` use it for pot-sherd surfaces). It is
not a pastoral owner; L1's `word`-mode probe in `claims.json` should not trip on it
[INFERENCE: word-boundary match, not re-run by this seat].

## The coupling inventory (17 files, hashes, owner line, seams)

Format: path — sha256, lines. **Owns** = the exact `- topic:` declaration line (that is the
line that makes the file the register owner; the README row must reproduce this text
byte-equal). **Seams** = body anchors C must cite with `path:line` + this sha256. **C owns**
= the share that must stay in the pastoral entry, per the partition's existing boundaries.

### culture-material siblings (7)

1. `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md` — sha256
   `23564220aa3befa4d460978f63d728bb6e2ad3df47dbb66cfa713177bdd668bb`, 179 lines.
   Owns `:4` (`- topic:`; note this legacy file has `- gap:` at :3, `- topic:` at :4): "the
   field system as the substrate under every other material register — the FOUR INSTITUTIONS
   (parcel, implement, water, claim)…". Seams: `:56` heavy-plough open-field row (communal
   herding after harvest, common pasture rights); `:62` **agropastoral row** — "fields +
   pasture + transhumance routes", "herd calendar; manure contracts", "fold, transhumance,
   stubble-right"; `:80` secondary-products revolution (traction, milk, wool, manure;
   contested as one horizon); `:123` ploughland measures (hide/virgate/oxgang — land named by
   the team it supports); `:132` manure/night-soil/rendering as the taboo layer.
   C owns: the herd as production unit (composition, breeding, seasonal movement, labour,
   yield, risk). Must not restate the field system and must cite `:62` as the *already-owned*
   field+herd subtype rather than presenting transhumance as new.

2. `corpus/knowledge/culture-material/hunting-foraging-subsistence.md` — sha256
   `64cb0d555d1970797f0fbff808afe7fda0c776da706fb55cf2fb934bc8a7b590`, 205 lines.
   Owns `:3` (`- topic:`): hunting/fishing/trapping/gathering as a subsistence-production
   register (locate→acquire→process→preserve→distribute). Seams: `:19` the `- couples:` model
   line C should imitate (relative path + "owns X — :lines; this entry owns Y" per target);
   `:36` the four-condition test's **wild-source** clause — "the organism or material is not
   planted, herded or owned as a standing crop". That clause is the partition's own boundary:
   a managed herd **fails** it, which is why pastoralism needs a distinct entry [INFERENCE].
   C owns: the domesticated-herd register; must cite `:36` as the definitional split and not
   re-open hunting method.

3. `corpus/knowledge/culture-material/fire-fuel-light.md` — sha256
   `481cf1c24734c1251879f3e2928fb9d470db7eae11a375982786602ed74c6558`, 173 lines.
   Owns `:4` (`- topic:`; `- gap:` at :3): fire as the material system a culture is organized
   around (hearth as institution, fuel ladder, ignition, lamp/candle, fire-risk apparatus).
   Seam: `:37` dried-dung fuel row — "the herds' output, and therefore the fields'", "a real
   trade-off against manure; fuel-poor pastoral cultures pay for it in soil"; also `:127` fuel
   map first (ecology and ownership).
   C owns: the dung/manure budget as a herd-output decision; cites `:37` as the fire
   register's consequence, never re-derives the fuel ladder.

4. `corpus/knowledge/culture-material/cuisine-food-lexicon.md` — sha256
   `36df983d91d964989ec0e08e0685c2c4c86a2822470752e8d00367ce61d56474`, 177 lines.
   Owns `:3` (`- topic:`): food as the most daily cultural system (staple theory, culinary
   triangle, feast/famine, fermentation, taboo/identity, restaurant registers). Seams: `:67`
   yogurt lineages as a bacteria+lactobacilli fermentation row; `:69` cheese washes in the
   mixed/aged row; `:81` milk+meat separation rules (Ex 23:19); `:83` milchig/fleishig/pareve
   kitchen lexicon.
   C owns: the raw product and its supply schedule (lactation, seasonality, yield, herd
   composition) and hands the meal, preservation-as-cuisine and dietary law to cuisine.
   Boundary sentence needed in both directions.

5. `corpus/knowledge/culture-material/transport-mobility-lexicon.md` — sha256
   `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70`, 129 lines.
   Owns `:4` (`- topic:`; `- gap:` at :3): mobility as ROUTE/VEHICLE/DRAFT/… four layers
   (draft includes ox, horse, camelid, dog). Seam: `:70` llama load figures — "llama ~30 kg
   at 20 km/day…; llama herds rather than carts because the animal is nimble on mountain
   roads".
   C owns: the animal as a production unit (breeding, herd sex/age structure, fodder, herd
   mobility as a management problem); transport owns the vehicle/draft/route institution and
   the load numbers.

6. `corpus/knowledge/culture-material/trade-economy-lexicon.md` — sha256
   `760a9df61364916b69e91c4d7f21ee4bff6bf138af6643f585afdcb10f05f277`, 166 lines.
   Owns `:3` (`- topic:`): market language as a worldbuilding system (measures and their
   sacred standardization, currency-word etymologies, market registers, guilds, contracts,
   credit). Seams: `:69` "fee, pecuniary | Gmc *fehu*, Lat. *pecūnia* < *pecus* 'cattle' |
   PIE *\*peḳu-* 'movable wealth = cattle' (Watkins); cf. Nuer cattle as the idiom of all
   value"; `:70` "capital, cattle, chattel | Lat. *caput* 'head' | wealth counted by heads".
   C owns: the herd as movable property and the herd-wealth accounting logic; trade owns the
   money-word drift and the market institution — cite, do not re-etymologize.

7. `corpus/knowledge/culture-material/textile-technology.md` — sha256
   `62ba304ab88eb8fb234247807b37662cea6933e5eed5500e9fb04d5e63eb14c0`, 103 lines.
   Owns `:3` (`- topic:`): the material substrate of dress (fiber hierarchy, dye chemistry,
   looms, finishing) and the ceiling on costume vocabulary. Seams: `:11` fiber gate ("what the
   land raises (flax fields, sheep flocks, mulberry/silkworm sheds…)"), `:22` wool row
   (shear→wash→card/comb→spin; Ur III wool-ration workshops), `:27` worsted-vs-woolen fork,
   `:30` camelid hierarchy vicuña > alpaca > llama, `:76` the "stink trades" incl.
   tanning-adjacent work as a taboo layer.
   C owns: flock management and fibre supply (who keeps the animals, at what scale, on what
   land); textile owns every prep/processing step and the cloth vocabulary.

### linguistics and myth-symbol (3)

8. `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` — sha256
   `80b5e2c89fc8a97be343d32be4071ec40cc2a0e2aedac4a8abf2311b7175f65d`, 162 lines.
   Owns `:3` (`- topic:`): engineering a lexicon by semantic field (core-vocabulary floors,
   field elaboration briefs, culture-type bundles). Seams: `:66` "decide which terrain
   differences carry subsistence weight (pasture types, flood stages, pass routes) and
   lexicalize only those"; `:70` "Pastoral wealth vocabulary (herd-age, herd-color,
   herd-condition terms) indexes property systems"; `:105` the "steppe pastoral" bundle row
   (subsistence = herd wealth; landscape = pasture; gap = sea/coast terms).
   C owns: the management facts the field must encode; semantic-fields owns the lexical
   elaboration brief. C supplies the inventory, not the word list.

9. `corpus/knowledge/myth-symbol/animal-symbolism.md` — sha256
   `8f1fce2d21a1a174c3e8e06ae47ecb928c4a9be283c8eb96da7987381b028ffc`, 133 lines.
   Owns `:3` (`- topic:`): fauna as symbolic substrate (totemism and its demolition, guardian
   beasts, food law, calendar animals, heraldry, serpent). Seams: `:73` Nuer "cattle of money"
   row (cattle as social idiom — names, songs, bridewealth; not primarily food); `:110`
   "Faunal economy writes the idiom: the Mongol five livestock (horse, cattle, camel, sheep,
   goat) structure wealth-language; Nuer cattle structure personhood-language"; `:122` write
   the biome/fauna list first, then assign meaning (§9 biogeography rule).
   C owns: the faunal economy (which species, in what ratio, for what product); animal
   symbolism owns the meaning assignment — cite `:110`/`:73` as idiom owners.

10. `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` — sha256
    `120302e6a132b4608a4060f2179a53e213fa45e0aeae3243649d0aacd98e5ecd`, 203 lines.
    Owns `:3` (`- topic:`): how myth legitimates a ruler — the eight legitimation channels.
    Seam: `:65` the **delegation** row — "the ruler is the god's tenant, servant, or shepherd
    — an office, not a person", with Mesopotamian kingship as *sipa*, shepherd (Jacobsen 1976
    at `:21`).
    C owns: the pastoral *production* reality behind the shepherd metaphor (who actually herds,
    what the metaphor would mean to herders); kingship owns the political-theology channel.
    Cite `:65`, do not restate the eight channels.

### civilizations — regional owners (7)

These own the worked regional cases; C owns the comparative method. Cite each with its
sha256 below; never generalize a regional detail into a cross-cultural law without saying so.

11. `corpus/knowledge/civilizations/mongol.md` — sha256
    `e60b3903402034bcd897617fac589340fb9c70439a028583fbe193fec14c1163`, 197 lines.
    Owns `:3` (`- topic:`): Mongol linguistic-cultural coupling (Uyghur-derived writing,
    Secret History registers, Heaven/earth vocabulary, deel dress, naming, yam relay). Seams:
    `:40` "not a ladder from 'primitive nomad' to 'civilization.' Mobile pastoralism, urban
    production, and documentary administration can coexist"; `:146` Cleaves pp.224–227 service
    ontology (station keepers, post-horse keepers, geldings, provision sheep, milch mares, cart
    oxen); `:166` winter pasture as a bottleneck; `:185` costed communications — "make the
    relay network consume horses, pasture, food, carts…".

12. `corpus/knowledge/civilizations/turkic-steppe.md` — sha256
    `ffc8ea6e9338fb1a7ab7e5b2e926b6e003550b5672529259b72107ca47ba7189`, 205 lines.
    Owns `:3` (`- topic:`): Turkic steppe reference base (Old Turkic inscriptions, qut,
    Ashina narratives, titles, portable dwellings, dress). Seams: `:18` "Era staging: preserve
    transitions, not a timeless nomad kit"; `:148` "Felt, wool textiles, leather… belong to
    different production/exchange chains. Do not make pastoral production synonymous with
    economic isolation"; `:194` reject the nomad→civilized ladder. (Also owns yurt vocabulary
    `:104-:123`; C should not restate tent terminology.)

13. `corpus/knowledge/civilizations/scythian-saka.md` — sha256
    `cb3a6428c4b174a4917871185e416f3ac7d3ecdf62a016432f87a486b3ab5c51`, 188 lines.
    Owns `:2` (`- topic:`; this file has no blank line after the H1): evidence-calibrated
    coupling of language, myth, oath, animal imagery, period and costume across Pontic
    Scythian / Central Asian Saka. Seams: `:70` "Do not equate pastoralism with total absence
    of farming: even Herodotus distinguishes farming and nomadic Scythians (4.17–20). His own
    categories should not become timeless ethnic castes"; `:173` preserve port-elite vs mobile
    pastoral vs mountain-burial distinctions.

14. `corpus/knowledge/civilizations/finnic-sami.md` — sha256
    `79dd14e82d1bd4fb03abc6167f15cce3e68d0976558a8cc68e5cc3ccae920384`, 214 lines.
    Owns `:3` (`- topic:`): Finnic/Sámi reference base (Uralic inheritance vs substrate, joik,
    noaidi drum, gákti, contested sky/thunder terms). Seams: `:140` "Do not map herding status
    directly onto Sámi identity. Fishing, hunting, craft, coastal, inland, and urban histories
    cannot be reduced to the image of one reindeer-herding outfit"; `:150` "Large-scale
    pastoralism has a history; it is not the eternal condition of all Sámi communities (Aikio
    2012: 86). Date herd scale and seasonal labor by locality".

15. `corpus/knowledge/civilizations/inca.md` — sha256
    `53ea1e83dfa4efab8e578fa16f1caffa67d1c8d3e77e1597716c862d5cdc3e99`, 199 lines.
    Owns `:3` (`- topic:`): Inca/Tawantinsuyu base (Quechua lingua franca, khipu debate, Inti,
    cumbi as prestige cloth). Seam: `:128` "Cotton and camelid fibers | Region, access,
    technique, and intended use influence cloth; 'all wool, all alpaca' is too simple…
    Connect herding and cultivation to specialist vocabulary and supply routes". (§7 `:115`
    owns cumbi; C must not restate cloth economics.)

16. `corpus/knowledge/civilizations/dine-navajo.md` — sha256
    `cfdc8cb78d24252ef69f85a98bd1c39d48c82401b1a2b62d40f210a59bb4eb6a`, 177 lines.
    Owns `:2` (`- topic:`; no blank line after H1): Diné linguistic-cultural coupling (tone
    and register, hózhǫ́, sandpainting, weaving, kinship, clan intros). Seams: `:116` "Causal
    chain to model: grazing conditions → sheep/fleece → preparation labor and water → yarn/dye
    access → weaving decisions → exchange and family livelihood"; `:125` Spanish-colonial and
    later pastoral transformations — "'Traditional' can incorporate introduced" stock.
    C owns: the herd→fibre supply link; Diné owns the weaving/kidnapping register.

17. `corpus/knowledge/civilizations/india-tamil-sangam.md` — sha256
    `ee0dea3dfa585af6400c671dc1ba166ddb3f0dd8037442a5be9b2d534a0460d9`, 180 lines.
    Owns `:2` (`- topic:`; no blank line after H1): Tamil/Sangam reference base (landscape
    poetics, contact layers, dress-as-description). Seams: `:77` the **Mullai** row —
    "Pastoral woodland; rainy season and evening | Cattle, herding, returning paths, jasmine;
    return schedules become promises"; `:84` "evening herds make absence noticeable" —
    landscape vocabularies as indexes of socially meaningful action.
    C owns: herding as a production/seasonal round; Sangam owns the poetic landscape code.

## Boundary rules the coupling implies (design constraints for C)

- **vs hunting** — the wild-source clause (`hunting…:36`) is the definitional test; C's §1
  must state that a managed herd fails it and therefore pastoralism is a new register.
- **vs agrarian** — `:62` already owns fields+pasture mixtures as an agrarian subtype; C owns
  the herd when the herd, not the field, is the production unit, and must name the agropastoral
  case as shared boundary.
- **vs cuisine** — dairy/meat are *food* there (`:67,:69,:81,:83`); C owns lactation, yield,
  seasonality, herd composition, and hands processing over.
- **vs textile** — C owns flocks and fibre supply; textile owns prep/loom/finish (`:11,:22`).
- **vs transport** — C owns the animal as production unit; transport owns draft, vehicles,
  routes and load figures (`:4,:70`).
- **vs trade** — C owns herd-as-property and herd wealth; trade owns money-word drift
  (`:69,:70`) and the market.
- **vs semantic fields** — C supplies the management facts; semantic-fields owns the field
  elaboration brief (`:70,:105`).
- **vs animal symbolism** — C owns the faunal economy; symbolism owns the idiom (`:73,:110`).
- **vs kingship** — C owns herders' reality; kingship owns the shepherd-as-delegation
  metaphor (`:65`).
- **vs civilizations** — each owns a dated regional case; C must carry the anti-ladder
  calibration lines explicitly (`mongol:40`, `turkic:194`, `scythian:70`, `finnic:140,:150`,
  `dine:125`) so the entry cannot become "timeless nomad kit".

## Mechanical contract the C author must hit (verified, not remembered)

- **Head: 8 fields, in this order** — `topic`, `gap filled`, `sources`, `couples`, `source`,
  `verified-at`, `recheck`, `scope`. Evidence: `hunting-foraging-subsistence.md:3-:23` and
  `cartography-and-mapmaking.md:3-:23`. (Agrarian/fire/transport are legacy 9-field variants
  with `- gap:` before `- topic:`; do not copy that form.)
- **`- topic:` must be one top-level line** — `reports/round-28/readme/sweep.py:61`
  (`TOPIC_RE`) captures it and compares it to the README row; a mismatch is `topic_mismatch`.
- **`- couples:` must name something it connects** — `tools/gates/provenance-audit.py:9-21`
  reports `missing-couples`/`empty-couples`; couples refs resolve by **unique basename**
  (`tools/harness/basename-couples-resolver.py:131-159`), so `../civilizations/mongol.md` and
  `agrarian-field-system-lexicon.md` both resolve direct. Model the line on
  `hunting-foraging-subsistence.md:19`.
- **README (C lands it too)** — row format `- \`name.md\` — <topic byte-equal>`
  (`sweep.py:60`); insert at `corpus/README.md:286`, between `music-instrument-lexicon.md`
  (:285) and `ritual-garments.md` (:286); bump `## culture-material/ (27)` at `:266` → **28**;
  `Total knowledge entries: 225.` at `:578` → **226**; counts-footer block at `:580-:582`
  (command `:581`, vector `:582`) `25/26/27/29/24/94` → `25/26/28/29/24/94`; prepend a
  `revision: 2.7` block in the style of the `revision: 2.6` block at `:3-:22`.
- **Sweep target** — `python3 -B reports/round-28/readme/sweep.py` must print rows 226 /
  files 226, missing 0, ghosts 0, duplicates 0, topic_mismatch 0, header_drift `{}`, totals
  226, footer `25/26/28/29/24/94`, exit 0. (Sweep also checks the footer arithmetic:
  `sweep.py:163-191`.)
- **Size** — the two model entries measure 205 lines (`hunting-foraging-subsistence.md`)
  and 239 (`cartography-and-mapmaking.md`), so the `<=~250` cap is a real ceiling; aim at
  the 205–225 range. The 8-field head occupies lines 3–23.
- **SOURCES rows** — registry header at `corpus/SOURCES.md:28` (11 columns: id, source, kind,
  tier, scope, anchor, teaches, status, opened, recheck, used-by); 47 rows exist; next id
  **S048** but **L1 assigns**. Each cited row needs: URL, `opened` 2026-10-21, a ≤25-word
  verbatim quote with its location in the `anchor` cell, tier per `QUALITY.md` criterion 6
  (publisher description/abstract = **B**; **A** only primary/authoritative for the exact
  scope), and `status: mined` only once `used-by` names
  `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`. C's `- source:` line
  should name each cited S-id with its URL + the section read (model:
  `hunting-foraging-subsistence.md:20`).
- **In-corpus anchors** — cite `path:line` and pin the sha256 in `- sources:`, exactly as
  `hunting-foraging-subsistence.md:6-:18` does. The hashes above are seat-time bytes
  (2026-10-21): **re-hash and re-check every line number at the authoring HEAD**, because
  claim C and the other two claims land in the same round and lines can drift.

## Scope question for L1 (evidence, not a recommendation)

**Who owns dairy *processing*?** No entry owns it as production: `grep -rniE
'dairy|cheese|butter|kumiss|airag|yogurt' corpus/knowledge/` yields cuisine (`:67` yogurt
lineage, `:69` cheese washes), fire (`:96` Vedic milk oblation), architecture (`:34` buttery as
"name rooms by stored object"), plus people-specific civilization lines. [INFERENCE] If C
sticks to herd management (lactation cycle, yield seasonality, herd composition, labour), the
handoff to `cuisine-food-lexicon.md:3` stays clean; if C takes milking/churning/preservation
it will collide with cuisine's fermentation/processing ownership. L1 should decide before the
entry is drafted.

## Unrun checks / residual unknowns

- Not run: the sweep, `provenance-audit.py`, the gate battery (no entry exists; scout is
  read-only), and any source fetch — **this seat opened no URL and makes no source-tier
  claim**; the frontier sources are sibling seats' business (`SrcZederDomestication.md`,
  `SrcUnescoGer.md`, `SrcDysonHudson.md`).
- No git/jj command was executed; hashes are working-tree bytes. If the working tree is not
  at base `4ad2683` for some file, C's authoring re-hash will surface it.
- Unknown: final S-id assignment (three sibling drafts all propose S048); whether L1 adds a
  second source row for the herding-social-form side (Dyson-Hudson's closed-access finding
  means that article cannot back a quote).
- Unknown: L1's dairy scope decision above.
- All ownership statements are read off each file's own `- topic:`/body lines; no external
  authority is claimed for them.
