# C10 — README rev 2.5 draft (claim C, coverage)

- Seat: `C10` | role: executor | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19) = `reports/round-48/claims.json` `baseline_commit`
- Out path: `reports/round-48/cov/C10-readme.md` (this file)
- Status: **DRAFT** — no bytes under `corpus/` were written; the change is a fenced diff for the integrator. Staging and verification ran only under `.scratch/c10/`.
- Non-author statement: I drafted no entry body and edited no other seat's fragment. Every number below is from a command I ran at the baseline; §7 carries the log.

**One-line.** The rev-2.5 README edit is four content changes (revision block, section header + row, totals line, counts footer) plus the rev-2.4 prose-vector repair; on a staged 224 tree the sweep is green (`224 == 224`, footer `224 / 25/26/26/29/24/94`), the prose vector sums 224, and neither existing row nor any other heading changes. The diff is supplied in two order variants (before/after Ca01's duplicate-H1 removal) because hunk 1's context straddles that line.

---

## 1. Measured pre-state (not asserted)

| Item | Value | Evidence |
|---|---|---|
| Index file | `corpus/README.md`, **575 lines**, sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | `wc -l`; `sha256sum` |
| Duplicate H1 | count **2** (`:1` and `:3`) | `grep -c '^# kotodama-shokunin corpus index$' corpus/README.md` → `2` |
| Latest revision | 2.4 at `corpus/README.md:5` | `grep -n '^revision: 2.4'` |
| Rev-2.4 vector line | `corpus/README.md:11` | `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with` |
| Totals line | `corpus/README.md:544` → `Total knowledge entries: 223.` | `grep -n '^Total knowledge entries'` |
| Counts footer | `corpus/README.md:548` → `(total 223 files; directory totals 25/26/25/29/24/94).` | `sed -n '546,548p'` |
| culture-material header | `corpus/README.md:234` → `## culture-material/ (25)` | `grep -n '^## culture-material/ ('` |
| Insert neighbours | `:240` `calendar-festival-systems.md`; `:241` `costume-semiotics.md` | `grep -n '^- \`calendar-festival-systems.md\`\|^- \`costume-semiotics.md\`'` |
| Live total / partition | 223 files; `25 / 26 / 25 / 29 / 24 / 94` | `find corpus/knowledge -name '*.md' \| wc -l` → `223`; `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `"files": 223` |
| Live sweep | green, exit 0 | `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, `totals_line 223 totals_ok True`, `footer_findings [] footer_ok True`, `readme_sha256 7c788a1d…` |
| Target slug | free | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → absent; `ls corpus/knowledge/culture-material/*.md \| wc -l` → `25` |

Section order is fixed by `reports/round-28/readme/sweep.py:50` (`PARTS`), so the footer vector's slots are `linguistics / myth-symbol / culture-material / synthesis / verification / civilizations`. The declaration of what a footer is (`sweep.py:66`, `FOOTER_RE`) and of the topic comparison (`sweep.py:74-82`, `topic_of`, continuations space-joined) are the two mechanics this edit must satisfy.

Filename order is verified, not assumed: the section's 25 slugs sort `… calendar-festival-systems.md, costume-semiotics.md …`, and `cartography-and-mapmaking.md` falls between them (`car` < `cos`). The seed asserted the same position at `reports/round-44/scout/K02-gap-scout.md:219`.

---

## 2. The rev-2.4 prose-vector defect and its repair

### 2.1 What the bytes say

`corpus/README.md:10-12` reads:

```
`## myth-symbol/` moved 23 → **26**; the totals and footer moved 220 → **223** and
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
`python3 reports/round-28/readme/sweep.py`: 223 rows vs 223 files, exit 0.
```

The before-vector (`25/23/25/29/24/94`) sums 220, matching the stated 220. The after-vector as filed sums **217**, against a stated total of 223. The footer at `:548` had the correct live value all along (`25/26/25/29/24/94`).

### 2.2 Arithmetic, recomputed

| Vector | Sum | Status |
|---|---:|---|
| rev-2.4 before (`README:11`) | `25+23+25+29+24+94` = **220** | correct |
| rev-2.4 after, as filed (`README:11`) | `25+23+26+25+24+94` = **217** | **defect** |
| rev-2.4 after, repaired | `25+26+25+29+24+94` = **223** | matches footer and total |
| rev-2.5 after landing | `25+26+26+29+24+94` = **224** | this edit |

The defect is a slot slip: myth-symbol's new `26` was written into slot 3 (culture-material), culture-material's old `25` was pushed into slot 4 (synthesis), and synthesis's `29` disappeared; slot 2 stayed `23`. Delta from correct: `-3 +1 -4 = -6` → 217.

### 2.3 The control the sweep does not have

Re-inserting the defective token into the staged post-edit README and re-running the same sweep:

```
control_revert_defect_ok True totals 224 footer_findings []
```

i.e. the sweep stays green with the 217-sum in place. It reads the totals line (`sweep.py:62`, `TOTALS_RE`) and the `Counts checked` block (`sweep.py:66`, `FOOTER_RE`), never the revision prose. This is why the repair needs an arithmetic receipt (the table above) rather than a green sweep, and why "sweep green" alone would not have caught the defect in r42. The repair is a one-token line edit at `README:11`; the defective reading is preserved inside the new rev-2.5 block as a quoted record, not deleted.

---

## 3. The edit — fenced diffs (integrator applies exactly one)

Both diffs were generated with `diff -u --label a/corpus/README.md --label b/corpus/README.md` from the live file and a staged copy. Both are 3 hunks, `+24 / -4` lines, net `+20`. Neither touches `README:1` or `README:3`; the duplicate-H1 removal remains Ca01's edit.

### 3.1 Patch A — apply against live HEAD (before Ca01)

- base: live `corpus/README.md` (575 lines, sha `7c788a1d…`)
- post: 595 lines, sha256 `5767d3c43d286e0863c44c55cfd1ebe8d13e7d8cd5a19c5d2c3424bc0e25648f`
- patch sha256: `80625041661bfd2dab9582e257c6f24f1e0c8ca03f2cb3d90a12d37750c211ba`
- `git apply --check` at HEAD → exit **0**

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -2,13 +2,32 @@
 
 # kotodama-shokunin corpus index
 
+revision: 2.5 — Round-48 culture-material expansion (2026-10-19): one
+culture-material entry landed (`cartography-and-mapmaking.md`, the map as an
+instrument and a claim about space; the gap was scouted fresh at
+`reports/round-44/scout/K02-gap-scout.md` §3 — 0 filename owners and 0
+topic-line owners at the 223 census), audited under `reports/round-48/cov/`.
+Its row was added in filename order between `calendar-festival-systems.md` and
+`costume-semiotics.md`, carrying the entry's own `- topic:` text byte-equal.
+`## culture-material/` moved 25 → **26**; the totals line and the counts footer
+moved 223 → **224** and the footer vector 25/26/25/29/24/94 →
+**25/26/26/29/24/94**. This revision also repairs the rev-2.4 prose-vector
+defect in place: rev 2.4's first-filed after-vector read `25/23/26/25/24/94`
+(sum 217 — myth-symbol's new 26 sat in the culture-material slot,
+culture-material's 25 was pushed into the synthesis slot, and synthesis's 29
+was dropped); the token now reads `25/26/25/29/24/94` (sum 223), the value the
+footer already carried. Re-measured with `python3 reports/round-28/readme/sweep.py`
+against a staged 224 tree via its `root_override` leg (receipt in
+`reports/round-48/cov/C10-readme.md` §5): 224 rows vs 224 files, exit 0.
+Non-canon examples and passing structural gates do not certify historical truth.
+
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
 myth-symbol entries landed (`mineral-stone-symbolism.md`,
 `purity-pollution-boundary-systems.md`, `sacred-topography-pilgrimage.md`),
 each audited (`reports/round-42/cov/C05-audit.md`); a fourth draft (C01's lithic
 register) collided with C04's and is routed as a named spare by integrator ruling.
 `## myth-symbol/` moved 23 → **26**; the totals and footer moved 220 → **223** and
-the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
+the vector 25/23/25/29/24/94 → **25/26/25/29/24/94**. Re-measured with
 `python3 reports/round-28/readme/sweep.py`: 223 rows vs 223 files, exit 0.
 
 revision: 2.3 — Round-40 linguistics-partition expansion (2026-10-19): four
@@ -231,13 +250,14 @@
 - `trickster.md` — the trickster as a cross-cultural figure class (Wakdjunkaga, Coyote, Raven, Anansi, Loki, Sun Wukong, Èṣù/Legba, Hermes, Br'er Rabbit) — Hynes's feature set, Radin's Winnebago cycle and its contested evolutionary reading, Hyde's boundary-crosser interpretation, structural and liminal analyses (Lévi-Strauss, Turner, Babcock-Abrahams), institutionalized sacred clowns, and how trickster tales encode the critique of the weak under durable power asymmetry; typology table, design protocol, and calibration flags for building a fictional culture's trickster
 
 
-## culture-material/ (25)
+## culture-material/ (26)
 
 - `adornment-body-codes.md` — the inscribed body as a legible system for fictional cultures — the master claim is that every body code sits in one of three columns, WEALTH (assayable, alienable: jewelry as walking bank account, from Norse hacksilver and ring-giving to bead economies, inalienable heirlooms like the kula shells and pounamu, seal-rings as documents), RITE (inalienable: Polynesian tattoo with its tapu protocol, Māori moko as legal signature, Nuer gar and Yoruba ila lineage scars, Khalsa kesh, mourning hair), and PUNISHMENT (administered by authority: Chinese mò 黥 and Roman stigma, Song convict-soldier face marks, Meiji bans) — and the craft is keeping the columns distinct while designing their leaks; secondary claims: hair is the most regulable body part and therefore the state's favorite (Qing queue, 1871 danpatsu-rei, Merovingian tonsure-deposition, Mexica warrior hair); cosmetics is a vocabulary before it is a pigment (Egyptian kohl → Arabic *al-kuḥl* → English *alcohol*; Greek kosmētikē vs kommotikē; Heian oshiroi/ohaguro; sindoor); greeting and posture are engineered honorific gradients (bow degrees, wai/sampeah, proskynesis, kowtow diplomacy, Byzantine adoratio, homage's immixtio manuum) that fail legibly at embassy scenes.
 - `agrarian-field-system-lexicon.md` — the field system as the substrate under every other material register — the FOUR INSTITUTIONS (parcel, implement, water, claim) that any fictional agrarian economy must name, and the vocabulary each one generates. Master claim: a culture's agrarian lexicon is generated at the seams where three quantities (yield per unit area, water control, labor calendar) meet four institutions, so an author who fixes the peak-labor month, the water source, and the harvest claim first gets the field, plough, measure, and status words almost for free. The entry supplies: a ten-system field typology with labor/tenure/lexical signatures; the plough family (ard, coultered mouldboard, wheeled) as a capacity chain, not a progress ladder; the water chain (source → lift → deliver → right) with the baray/qanat/acequia/paddy cases; rotation and crop-loanword clocks; the harvest tool-and-share vocabulary; the work-unit land measures (jugerum, morgen, acre, hide, carucate); a calibration shelf of the framework's contested claims (heavy-plough revolution, plough→gender, hydraulic despotism, rice culture); and a decision record for authors
 - `architecture-settlement-lexicon.md` — built-environment vocabulary across real cultures — how houses, roofs, thresholds, sacred buildings, and cities are named; the semantic logic of house parts (Roman domus, Japanese moya/hisashi/engawa/doma, Chinese siheyuan, Arab dār, the English hall and its storage rooms, Mongolian ger); roof-form typology vs climate (gasshō, badgir, ondol/kang); the courtyard / hall / stilt design arcs; why temple, church, shrine, mosque, synagogue are conceptually distinct words; planning lexica (cardo/decumanus, Hippodamian grid, Kao Gong Ji, feng shui schools, jōkamachi/machiya, madina/khittaṭ); and how settlement vocabulary fossilizes worldview (lord/lady, town/Zaun, villain, þing→thing, 家, tatemae, paradise) — with design levers for coining a fictional culture's built-environment lexicon
 - `bathing-and-body-hygiene.md` — the bath as a material institution for fictional cultures — the five bathing regimes (Roman thermae and balnea, the Islamic hammam, the East Asian sentō/onsen, the sweat-lodge family, and domestic/personal washing) compared on sequence, heating, staffing, social function and relation to purity; the bath sequence as designed space (undress → warm → hot/steam → cool/immersion → rest) and what each stage demands in water, fuel and staff; the load-bearing **purity vs hygiene** distinction (ritual immersion families: mikveh, ghusl/wudu, baptismal and river bathing) with the rule that the two systems stay separate and their *leaks* are the design work; the water-and-heat infrastructure decision (aqueduct, well, cistern, river, water-carrier; hypocaust, stove, kettle; drainage and the latrine) and who pays for it (evergetism, waqf, taxation, household); who bathes where and when (privacy and gender regimes, the bath as sociability, the weekly bath, the bath as gift and as tax); the kit and its trade (soap chemistry and the Aleppo/Marseille/Castile families, oil and strigil, whisk and loofah, towels, basins) with the loan-word strata that date contact (*hammam*, *sauna*, *onsen*, *temazcal*, *shampoo*, *spa*); hygiene's move from emic doctrine to evidence-based practice (hydrotherapy, the public-bath and wash-house acts, Semmelweis and Snow as the calibration spine); and a calibration bank that dates both "Romans were clean" and "medieval people never washed". Reference knowledge and method only; canon decisions belong to lore-shokunin.
 - `calendar-festival-systems.md` — The civil machinery of time — how cultures square the 29.53-day moon against the 365.2422-day year (observation, fixed cycle, and doctrinal-prohibition intercalation strategies), the Egyptian 365-day design that walks through the seasons (Sothic cycle, Canopus fix, Coptic/Ethiopian children), calendar reform as political act from Caesar and Gregory to the French Republican, Soviet, and corporate 13-month experiments, week systems (the seven-day empire and its 3/5/6/8/10/13-day rivals), festival-cycle engineering (new-year placement, carnival polarity, seasons of the dead, four-new-years systems, sabbatical/jubilee economies), era and epoch as statute, the working vocabulary of timekeeping for in-world coinage; calibration flags throughout.
+- `cartography-and-mapmaking.md` — the map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative; the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo); projection and scale as claims about what matters; the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank); the reproduction economics (manuscript, woodblock, copperplate, the atlas); the map's silences and its use as a legal/territorial instrument; a build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)
 - `costume-semiotics.md` — clothing as a sign system — Barthes' fashion semiotics calibrated against what dress actually encodes (rank, rite, region, gender, occupation, faction, age), sumptuary display and its enforcement economies, modesty codes as legible-and-deniable systems, the legibility dial from engineered uniforms to fashion noise, and cross-era signaling drift (scarcity collapse, production tech, invented tradition) — the meaning-of-color side lives in myth-symbol/color-symbolism.md, the lexicon side in linguistics files; this file owns the code structure, reading mechanics, and drift
 - `craft-artisan-lexicon.md` — the workshop as a speech community — a closed technical register with five banks of terms: (1) tool names and etymologies (Japanese pull-cut carpentry nomenclature — ryōba "both-edge", kugihiki "nail-pull", the sumitsubo "ink-pot" with its makigitsune "winding-fox" crank, the adze whose kanji say "hand-axe", yasurime file-marks as smith handwriting; the body-metaphor grammar of tool anatomy; the homonym traps of fuller/bickern/hardie); (2) material-grading vocabularies (tamahagane "jewel-steel", kawagane/shingane "skin/heart metal", the hada grain words masame/itame/mokume shared with wood via the -me 目 "grain/eye" classifier, nie "boiling" and nioi "scent" in the temper line, NHLA timber grades, karat/fineness, GIA's 4Cs, the Kaogongji four-factor quality formula and qiao/zhuo aesthetic inversion); (3) workshop organization across seven systems (Lehrling–Geselle–Meister with Meisterstück and Wanderjahre; London apprentice→journeyman→freedom→livery with three entry routes; Ottoman çırak–kalfa–usta with gedik and şed investiture; Persian ustād–shāgird; Chinese shifu–xuetu under hang/huiguan; Japanese shishō–deshi under za→kabunakama; Indian śreṇī guilds and Roman collegia with Egyptian papyrus contracts; Benin's royal hereditary ateliers as the non-guild model); (4) signatures and marks as a six-type typology (authorship, assay, brand, license/proof, registry celebrity, attribution forensics — from the 1300 leopard's head through Dürer's monogram lawsuit to Morelli's clue paradigm); and (5) craft deity and ritual (Ptah's heart-and-tongue creation, Athena's kiln prayer, Viśvakarman, Lu Ban's hidden build-curses, Kanayago-kami, Ottoman pîrs, hari-kuyō needle funerals, tsukumogami), plus the anti-fraud machine (assize, jurés, hallmarks, proof marks) that quality vocabulary is really about
 - `cuisine-food-lexicon.md` — Food as the most daily of cultural systems — how a staple grain organizes labor, landscape, and lexicon (meal=staple lexicalization in East/Southeast Asian languages vs bread-based companionship etyma in Europe); the Lévi-Straussian culinary triangle read as generator rather than law, with flavor principles (Rozin) and meal grammar (Douglas) as the surviving craft tools; the feast/famine cycle (omen and homophone foods, fast calendars, mourning meals, Sen's entitlement theory of famine, famine foods); fermentation as inheritable heritage (koji, garum, Ninkasi, chicha, kimjang, sourdough mothers); dietary law as identity boundary with kashrut and halal as the calibration case studies (Douglas vs Milgrom vs Harris); etiquette as table grammar (fork history, chopstick taboos, guest-right of bread and salt, pre/post-meal formulas); and the social registers of eating from palace kitchen to night market (Song dynasty restaurants, the Parisian invention of the restaurant, street-food institutions, menu-language drift) — all as worldbuilder method with calibration flags.
@@ -541,11 +561,11 @@
   `reports/round-{5,6}/parent-reconciliation.json` receipts and name the drift;
   do not edit the old runners.
 
-Total knowledge entries: 223.
+Total knowledge entries: 224.
 
 Counts checked 2026-10-19 from the repo root:
 `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
-(total 223 files; directory totals 25/26/25/29/24/94).
+(total 224 files; directory totals 25/26/26/29/24/94).
 The inventory counts markers, not verified facts.
 Superseded reading, preserved as the dated record it was: this footer read
 `(total 199 files; directory totals 19/19/18/29/20/94)` from round 20 through
```

### 3.2 Patch B — apply if Ca01 removed `README:3` first

Variant A's hunk 1 carries the second H1 as context, so it fails (hunk 1 only) on a post-Ca tree: verified with `patch -p1 --dry-run` on a 573-line post-Ca copy → `Hunk #1 FAILED at 2`, hunks 2–3 applied. Patch B is the same edit anchored on the single-H1 file.

- base: live file with `README:3` and its blank line removed → 573 lines (`wc -l`)
- post: 593 lines, sha256 `3960c5e2753a1cb2f8a7345b9f7210ad35405da9fe1189f0fb590772a22cebc7`
- patch sha256: `12dd7dcddec377c3c3425120d552d3ce3978e2048e90529b22f1f2e0ed41b556`
- `patch -p1 --dry-run` on the post-Ca copy → exit **0**
- H1 count in patch B's post file → **1** (Ca's end state)

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,12 +1,31 @@
 # kotodama-shokunin corpus index
 
+revision: 2.5 — Round-48 culture-material expansion (2026-10-19): one
+culture-material entry landed (`cartography-and-mapmaking.md`, the map as an
+instrument and a claim about space; the gap was scouted fresh at
+`reports/round-44/scout/K02-gap-scout.md` §3 — 0 filename owners and 0
+topic-line owners at the 223 census), audited under `reports/round-48/cov/`.
+Its row was added in filename order between `calendar-festival-systems.md` and
+`costume-semiotics.md`, carrying the entry's own `- topic:` text byte-equal.
+`## culture-material/` moved 25 → **26**; the totals line and the counts footer
+moved 223 → **224** and the footer vector 25/26/25/29/24/94 →
+**25/26/26/29/24/94**. This revision also repairs the rev-2.4 prose-vector
+defect in place: rev 2.4's first-filed after-vector read `25/23/26/25/24/94`
+(sum 217 — myth-symbol's new 26 sat in the culture-material slot,
+culture-material's 25 was pushed into the synthesis slot, and synthesis's 29
+was dropped); the token now reads `25/26/25/29/24/94` (sum 223), the value the
+footer already carried. Re-measured with `python3 reports/round-28/readme/sweep.py`
+against a staged 224 tree via its `root_override` leg (receipt in
+`reports/round-48/cov/C10-readme.md` §5): 224 rows vs 224 files, exit 0.
+Non-canon examples and passing structural gates do not certify historical truth.
+
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
 myth-symbol entries landed (`mineral-stone-symbolism.md`,
 `purity-pollution-boundary-systems.md`, `sacred-topography-pilgrimage.md`),
 each audited (`reports/round-42/cov/C05-audit.md`); a fourth draft (C01's lithic
 register) collided with C04's and is routed as a named spare by integrator ruling.
 `## myth-symbol/` moved 23 → **26**; the totals and footer moved 220 → **223** and
-the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
+the vector 25/23/25/29/24/94 → **25/26/25/29/24/94**. Re-measured with
 `python3 reports/round-28/readme/sweep.py`: 223 rows vs 223 files, exit 0.
 
 revision: 2.3 — Round-40 linguistics-partition expansion (2026-10-19): four
@@ -229,13 +248,14 @@
 - `trickster.md` — the trickster as a cross-cultural figure class (Wakdjunkaga, Coyote, Raven, Anansi, Loki, Sun Wukong, Èṣù/Legba, Hermes, Br'er Rabbit) — Hynes's feature set, Radin's Winnebago cycle and its contested evolutionary reading, Hyde's boundary-crosser interpretation, structural and liminal analyses (Lévi-Strauss, Turner, Babcock-Abrahams), institutionalized sacred clowns, and how trickster tales encode the critique of the weak under durable power asymmetry; typology table, design protocol, and calibration flags for building a fictional culture's trickster
 
 
-## culture-material/ (25)
+## culture-material/ (26)
 
 - `adornment-body-codes.md` — the inscribed body as a legible system for fictional cultures — the master claim is that every body code sits in one of three columns, WEALTH (assayable, alienable: jewelry as walking bank account, from Norse hacksilver and ring-giving to bead economies, inalienable heirlooms like the kula shells and pounamu, seal-rings as documents), RITE (inalienable: Polynesian tattoo with its tapu protocol, Māori moko as legal signature, Nuer gar and Yoruba ila lineage scars, Khalsa kesh, mourning hair), and PUNISHMENT (administered by authority: Chinese mò 黥 and Roman stigma, Song convict-soldier face marks, Meiji bans) — and the craft is keeping the columns distinct while designing their leaks; secondary claims: hair is the most regulable body part and therefore the state's favorite (Qing queue, 1871 danpatsu-rei, Merovingian tonsure-deposition, Mexica warrior hair); cosmetics is a vocabulary before it is a pigment (Egyptian kohl → Arabic *al-kuḥl* → English *alcohol*; Greek kosmētikē vs kommotikē; Heian oshiroi/ohaguro; sindoor); greeting and posture are engineered honorific gradients (bow degrees, wai/sampeah, proskynesis, kowtow diplomacy, Byzantine adoratio, homage's immixtio manuum) that fail legibly at embassy scenes.
 - `agrarian-field-system-lexicon.md` — the field system as the substrate under every other material register — the FOUR INSTITUTIONS (parcel, implement, water, claim) that any fictional agrarian economy must name, and the vocabulary each one generates. Master claim: a culture's agrarian lexicon is generated at the seams where three quantities (yield per unit area, water control, labor calendar) meet four institutions, so an author who fixes the peak-labor month, the water source, and the harvest claim first gets the field, plough, measure, and status words almost for free. The entry supplies: a ten-system field typology with labor/tenure/lexical signatures; the plough family (ard, coultered mouldboard, wheeled) as a capacity chain, not a progress ladder; the water chain (source → lift → deliver → right) with the baray/qanat/acequia/paddy cases; rotation and crop-loanword clocks; the harvest tool-and-share vocabulary; the work-unit land measures (jugerum, morgen, acre, hide, carucate); a calibration shelf of the framework's contested claims (heavy-plough revolution, plough→gender, hydraulic despotism, rice culture); and a decision record for authors
 - `architecture-settlement-lexicon.md` — built-environment vocabulary across real cultures — how houses, roofs, thresholds, sacred buildings, and cities are named; the semantic logic of house parts (Roman domus, Japanese moya/hisashi/engawa/doma, Chinese siheyuan, Arab dār, the English hall and its storage rooms, Mongolian ger); roof-form typology vs climate (gasshō, badgir, ondol/kang); the courtyard / hall / stilt design arcs; why temple, church, shrine, mosque, synagogue are conceptually distinct words; planning lexica (cardo/decumanus, Hippodamian grid, Kao Gong Ji, feng shui schools, jōkamachi/machiya, madina/khittaṭ); and how settlement vocabulary fossilizes worldview (lord/lady, town/Zaun, villain, þing→thing, 家, tatemae, paradise) — with design levers for coining a fictional culture's built-environment lexicon
 - `bathing-and-body-hygiene.md` — the bath as a material institution for fictional cultures — the five bathing regimes (Roman thermae and balnea, the Islamic hammam, the East Asian sentō/onsen, the sweat-lodge family, and domestic/personal washing) compared on sequence, heating, staffing, social function and relation to purity; the bath sequence as designed space (undress → warm → hot/steam → cool/immersion → rest) and what each stage demands in water, fuel and staff; the load-bearing **purity vs hygiene** distinction (ritual immersion families: mikveh, ghusl/wudu, baptismal and river bathing) with the rule that the two systems stay separate and their *leaks* are the design work; the water-and-heat infrastructure decision (aqueduct, well, cistern, river, water-carrier; hypocaust, stove, kettle; drainage and the latrine) and who pays for it (evergetism, waqf, taxation, household); who bathes where and when (privacy and gender regimes, the bath as sociability, the weekly bath, the bath as gift and as tax); the kit and its trade (soap chemistry and the Aleppo/Marseille/Castile families, oil and strigil, whisk and loofah, towels, basins) with the loan-word strata that date contact (*hammam*, *sauna*, *onsen*, *temazcal*, *shampoo*, *spa*); hygiene's move from emic doctrine to evidence-based practice (hydrotherapy, the public-bath and wash-house acts, Semmelweis and Snow as the calibration spine); and a calibration bank that dates both "Romans were clean" and "medieval people never washed". Reference knowledge and method only; canon decisions belong to lore-shokunin.
 - `calendar-festival-systems.md` — The civil machinery of time — how cultures square the 29.53-day moon against the 365.2422-day year (observation, fixed cycle, and doctrinal-prohibition intercalation strategies), the Egyptian 365-day design that walks through the seasons (Sothic cycle, Canopus fix, Coptic/Ethiopian children), calendar reform as political act from Caesar and Gregory to the French Republican, Soviet, and corporate 13-month experiments, week systems (the seven-day empire and its 3/5/6/8/10/13-day rivals), festival-cycle engineering (new-year placement, carnival polarity, seasons of the dead, four-new-years systems, sabbatical/jubilee economies), era and epoch as statute, the working vocabulary of timekeeping for in-world coinage; calibration flags throughout.
+- `cartography-and-mapmaking.md` — the map as an instrument and a claim for fictional cultures — the survey → projection → drawing → reproduction chain that makes a map authoritative; the map-form typology (itinerary/strip, cadastral, chorographic, portolan, celestial, cosmographic, thematic, and the cartographic history/lienzo); projection and scale as claims about what matters; the symbol grammar (orientation, compass rose, scale bar, legend, boundary, blank); the reproduction economics (manuscript, woodblock, copperplate, the atlas); the map's silences and its use as a legal/territorial instrument; a build order, a decision record, a NON-CANON worked example, and a calibration bank (the neutral-map claim, the flat-earth myth, portolan accuracy, the primitive-map fallacy, map = territory)
 - `costume-semiotics.md` — clothing as a sign system — Barthes' fashion semiotics calibrated against what dress actually encodes (rank, rite, region, gender, occupation, faction, age), sumptuary display and its enforcement economies, modesty codes as legible-and-deniable systems, the legibility dial from engineered uniforms to fashion noise, and cross-era signaling drift (scarcity collapse, production tech, invented tradition) — the meaning-of-color side lives in myth-symbol/color-symbolism.md, the lexicon side in linguistics files; this file owns the code structure, reading mechanics, and drift
 - `craft-artisan-lexicon.md` — the workshop as a speech community — a closed technical register with five banks of terms: (1) tool names and etymologies (Japanese pull-cut carpentry nomenclature — ryōba "both-edge", kugihiki "nail-pull", the sumitsubo "ink-pot" with its makigitsune "winding-fox" crank, the adze whose kanji say "hand-axe", yasurime file-marks as smith handwriting; the body-metaphor grammar of tool anatomy; the homonym traps of fuller/bickern/hardie); (2) material-grading vocabularies (tamahagane "jewel-steel", kawagane/shingane "skin/heart metal", the hada grain words masame/itame/mokume shared with wood via the -me 目 "grain/eye" classifier, nie "boiling" and nioi "scent" in the temper line, NHLA timber grades, karat/fineness, GIA's 4Cs, the Kaogongji four-factor quality formula and qiao/zhuo aesthetic inversion); (3) workshop organization across seven systems (Lehrling–Geselle–Meister with Meisterstück and Wanderjahre; London apprentice→journeyman→freedom→livery with three entry routes; Ottoman çırak–kalfa–usta with gedik and şed investiture; Persian ustād–shāgird; Chinese shifu–xuetu under hang/huiguan; Japanese shishō–deshi under za→kabunakama; Indian śreṇī guilds and Roman collegia with Egyptian papyrus contracts; Benin's royal hereditary ateliers as the non-guild model); (4) signatures and marks as a six-type typology (authorship, assay, brand, license/proof, registry celebrity, attribution forensics — from the 1300 leopard's head through Dürer's monogram lawsuit to Morelli's clue paradigm); and (5) craft deity and ritual (Ptah's heart-and-tongue creation, Athena's kiln prayer, Viśvakarman, Lu Ban's hidden build-curses, Kanayago-kami, Ottoman pîrs, hari-kuyō needle funerals, tsukumogami), plus the anti-fraud machine (assize, jurés, hallmarks, proof marks) that quality vocabulary is really about
 - `cuisine-food-lexicon.md` — Food as the most daily of cultural systems — how a staple grain organizes labor, landscape, and lexicon (meal=staple lexicalization in East/Southeast Asian languages vs bread-based companionship etyma in Europe); the Lévi-Straussian culinary triangle read as generator rather than law, with flavor principles (Rozin) and meal grammar (Douglas) as the surviving craft tools; the feast/famine cycle (omen and homophone foods, fast calendars, mourning meals, Sen's entitlement theory of famine, famine foods); fermentation as inheritable heritage (koji, garum, Ninkasi, chicha, kimjang, sourdough mothers); dietary law as identity boundary with kashrut and halal as the calibration case studies (Douglas vs Milgrom vs Harris); etiquette as table grammar (fork history, chopstick taboos, guest-right of bread and salt, pre/post-meal formulas); and the social registers of eating from palace kitchen to night market (Song dynasty restaurants, the Parisian invention of the restaurant, street-food institutions, menu-language drift) — all as worldbuilder method with calibration flags.
@@ -539,11 +559,11 @@
   `reports/round-{5,6}/parent-reconciliation.json` receipts and name the drift;
   do not edit the old runners.
 
-Total knowledge entries: 223.
+Total knowledge entries: 224.
 
 Counts checked 2026-10-19 from the repo root:
 `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
-(total 223 files; directory totals 25/26/25/29/24/94).
+(total 224 files; directory totals 25/26/26/29/24/94).
 The inventory counts markers, not verified facts.
 Superseded reading, preserved as the dated record it was: this footer read
 `(total 199 files; directory totals 19/19/18/29/20/94)` from round 20 through
```

### 3.3 Apply order

1. **Entry first.** Land `corpus/knowledge/culture-material/cartography-and-mapmaking.md`; otherwise the sweep reports the row as a ghost (the row is generated from the entry's topic, §3.4).
2. **Then the README.** Either order of C10/Ca works if the matching patch is used: **C10 patch A first, then Ca01's line-3 removal** is the shortest path (patch A is checked against live HEAD). If Ca01 lands first, use **patch B**. Do not apply patch A to a post-Ca tree.
3. **Never lift C11's staged rev block instead.** `reports/round-48/cov/C11-sweep.md` §2 row 6 says its rev-2.5 block was inserted "before rev 2.3"; the staged bytes confirm it sits *after* 2.4 and before 2.3 (`.scratch/r48-c11/stage/corpus/README.md:14` follows `:5` revision 2.4). The file's convention is newest-first, and C11's block also hard-codes its 136-line verification fixture as the entry length. Patch A/B place 2.5 above 2.4 and cite no fixture length.

### 3.4 The new row is generated, never hand-typed

`sweep.py:74-82` compares the row text to the entry's own `- topic:` block, space-joined. The row in the patch is therefore generated from the seed topic and pinned:

- `reports/round-44/scout/K02-gap-scout.md:227` — **766 chars**, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495`
- `reports/round-48/cov/C02-header.md:114` — the filed r48 header topic is **byte-equal** to the seed (766 chars, same sha256; compared directly, `EQUAL True`)

Regenerate after the entry lands (same rule as `sweep.py:74-82`):

```bash
python3 -B - <<'PY'
import re
p = 'corpus/knowledge/culture-material/cartography-and-mapmaking.md'
t = open(p, encoding='utf-8').read()
m = re.search(r'^- topic:(.*?)(?=\n- \w)', t, re.M | re.S)
topic = ' '.join(x.strip() for x in m.group(1).strip('\n').splitlines() if x.strip())
print('- `cartography-and-mapmaking.md` — ' + topic)
PY
```

If C02/C01 change the topic, replace only the `+` row line in patch A/B with the generator's output; no other patch byte changes.

---

## 4. Verification against a staged 224 tree

Stage: `.scratch/c10/tree/knowledge` = `cp -r corpus/knowledge` plus a stub entry carrying the pinned topic; `.scratch/c10/corpus/README.post.md` = patch A's post file. Measured through the sweep's own `sweep()` with `root_override` (the module's staging leg), not by reimplementing it:

```
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"date": "2026-10-19", ..., "total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_live {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 5767d3c43d286e0863c44c55cfd1ebe8d13e7d8cd5a19c5d2c3424bc0e25648f
ok True
```

Independent recounts (not read from the sweep):

```
$ find .scratch/c10/tree/knowledge -name '*.md' | wc -l            # 224
$ ls .scratch/c10/tree/knowledge/culture-material/*.md | wc -l     # 26
```

Post-edit prose vectors, summed from the staged file:

| Location | Vector | Sum |
|---|---|---:|
| rev-2.4 repaired (`post:30`) | `25/26/25/29/24/94` | 223 |
| rev-2.5 target (`post:13-14`) | `25/26/26/29/24/94` | 224 |
| footer (`post:568`) | `25/26/26/29/24/94` | 224 |
| totals line (`post:564`) | `224` | 224 |

Heading control: live H1 count `2` → patch A post `2` (Ca01 still owed) → patch B post `1`. No other heading is touched; the diff has no `##` line except the culture-material header.

Apply checks:

```
$ git apply --check .scratch/c10/readme.patch              # exit 0 (live tree)
$ patch -p1 --dry-run -d .scratch/c10/order < ...post-ca.patch  # exit 0
```

What is **not** claimed: the live post-landing sweep. It cannot be run before the entry lands; C11's staged sweep (`reports/round-48/cov/C11-sweep.md` §3) and V01's post-landing run are the certificates, and their staged README differs from mine in the rev-block position noted in §3.3.

---

## 5. What this draft deliberately does not do

- **No duplicate-H1 edit.** Lines 1 and 3 are untouched; patch A keeps both (H1 count 2), patch B assumes Ca01 already removed `:3`. The two edits are separable and order-safe.
- **No footer-history appendix.** `reports/round-47/cov/C09-readme.md` §3 carried a fourth hunk appending revisions 2.1–2.5 to the "Superseded reading" paragraph. That paragraph is explicitly a dated historical record (`README:550`), not a per-revision ledger — the revision blocks are the ledger. The hunk changes no measured count, so it is dropped here for a minimal diff (4 changed lines, 1 inserted block, 1 inserted row).
- **No new measurement claim in the revision prose.** The rev-2.5 block says "re-measured … against a staged 224 tree via its `root_override` leg" and cites this file; it does not assert a live post-landing sweep that has not happened.
- **No r47 path/date reuse.** All r48 citations point at r48 or at filed r44 scout bytes.

---

## 6. To-verify / open items for the integrator

1. **Audit path in rev 2.5.** The block says "audited under `reports/round-48/cov/`" — true if any of the filed C verifier fragments is the audit (C03–C05, C12, R03 land there). If the round files a single `validation.json`-only audit, substitute that exact path; do not invent one.
2. **Date.** `2026-10-19` appears in the rev-2.5 block and the footer. If application happens later, change both to the measurement date; the sweep does not check it, but both are dated present-tense claims.
3. **Topic drift.** The row is pinned to the C02 topic sha `bc7274f4…`. If C01/C02 change it after this draft, regenerate the row (§3.4) — otherwise `topic_mismatch` fires.
4. **Landing surface.** Two files only: the new entry (A) and `corpus/README.md` (M). If any other `corpus/` file is M in `git status`, stop and report; this draft touches none.

---

## 7. Command log (all at HEAD `a01405d`, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`)

```
$ git rev-parse HEAD                                              # a01405dd36…
$ wc -l corpus/README.md                                          # 575
$ sha256sum corpus/README.md                                      # 7c788a1d…
$ grep -c '^# kotodama-shokunin corpus index$' corpus/README.md   # 2
$ grep -nE '^## culture-material/ \(|^Total knowledge entries|^\(total 223 files' corpus/README.md
                                                                  # 234, 544, 548
$ find corpus/knowledge -name '*.md' | wc -l                      # 223
$ ls corpus/knowledge/culture-material/*.md | wc -l               # 25
$ python3 -B reports/round-28/readme/sweep.py                     # exit 0, rows 223 files 223
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
                                                                  # "files": 223
# staged tree + patch generation + checks (scripts under .scratch/c10/):
#   post A 595 lines sha 5767d3c4…; post B 593 lines sha 3960c5e2…
#   patch A sha 8062504…; patch B sha 12dd7dc…
#   sweep(post A, root_override=.scratch/c10/tree/knowledge) -> ok True, 224 == 224
#   control: defective rev-2.4 token reinserted -> ok True (sweep is blind to prose vectors)
#   git apply --check patch A -> 0; patch -p1 --dry-run patch B -> 0
```

No file was written outside this out path and `.scratch/`; no git operation ran.
