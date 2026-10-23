# CriticEntry57 — residual falsify of landed claim C entry (round 57)

Seat: KotodamaR57.CriticEntry57 (critic, read-only leaf). Target: `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` (ENTRY) as landed at `78d83b5e`; registry rows S413-S454 in `corpus/SOURCES.md`. Checklist: `.ufo/waves/round-57/build/CriticEntryContract57.md`. Paths are relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. No installs. Nothing written except this report. I did not run ACCEPT-C-57 and did not touch any predicate. Two external source texts were read by plain `curl` from archive.org to check how rows were read (S413 Fox-Davies djvu text; S428 McClatchie djvu text), both HTTP 200, saved under `/tmp/ce57-*.txt`.

Axes: calibration (codes, hedges, scope), coverage (boundary/one-way pointers), provenance (row carries the claim), restricted-mark ceiling, lore boundary.

## Findings

### HIGH

**H1. The calibration codes are redefined against the lane registry while the entry claims to follow it.**
- `ENTRY:16` says "Codes as in the lane's calibration practice", then gives: B = "well supported by the cited row", C = "contested or hedged by the row itself", R = "rejected by the cited row", T = "tradition reported as tradition".
- The registry, `corpus/knowledge/verification/calibration-registry.md:35-39`, says otherwise: B is "Bounded, usable within a named domain"; T is "Unresolved provenance or claim check — Mark `(to-verify)` inline … do not make it load-bearing"; R is "Rejected/discredited as the specified general inference". H is missing from the entry.
- The round-56 exemplar cites the registry directly: `kongo-kingdom.md:136` reads "Codes as in `../verification/calibration-registry.md:35-39`."
- So every T in ENTRY (`:61` "T for the origin story", `:93` "the attribution is T", `:141`) means something different from registry T. None carries `(to-verify)`. This is a duplicate authority for the codes.
- Fix at `ENTRY:16`:
  - old: `Codes as in the lane's calibration practice: **B** well supported by the cited row at its stated strength; **C** contested or hedged by the row itself; **R** rejected by the cited row; **T** tradition reported as tradition.`
  - new: `Codes as in `../verification/calibration-registry.md:35-39` (R rejected as the specified general inference; C contested interpretation; B bounded to a named domain; H heuristic; T unresolved provenance, marked (to-verify)). A tradition the row itself reports as tradition is written "reported as tradition (row)", not T.`
- Then recode as follows:
  - `:61`: `(T for the origin story)` becomes `(the origin story is reported as tradition, S428)`.
  - `:93`: `the attribution is T` becomes `the attribution is reported as tradition`.
  - `:141`: code `T` becomes `B (the museum's attribution is hedged "said to be"; not a settled maker attribution)`.

**H2. The header claims every anchor quote was re-located; the landing commit says 40 of 42.**
- `ENTRY:7` reads "each anchor quote re-located live by the round's locator".
- The commit `78d83b5e` subject reads "SOURCES S413-S454 (42 rows opened this round, all cited, live-located 40/42)".
- So two rows' first quotes were not located, and "each" is false provenance. Only first quotes go through LOCATE (`ExecIntegrateRows57.md:6`), so "each anchor quote" overstates even the 40.
- I found no committed receipt that names the two misses. `rg 'located=4|40/42' reports/round-57 .ufo/waves/round-57` turns up only the controls.
- Fix at `ENTRY:7`:
  - old: `each anchor quote re-located live by the round's locator.`
  - new: `each row's first anchor quote run through the round's locator at integration: 40 of 42 located (the two misses are named in the round receipt).`
- The closure must name the two ids.

**H3. S413 is misread twice: a Scottish practice becomes a "lineage" bearer unit, and Fox-Davies's own conjecture about early crests becomes a rule.**
- The served text, lines 17289-17292 of the `completeguidetoh00foxduoft` djvu, says: "whilst one dislikes the Scottish idea under which the same identical crest can be and regularly is granted to half-a-dozen people of as many different surnames".
  - The persons are unrelated grantees under Scottish practice. That is not "a lineage across many surnames".
  - Row 42 (`ENTRY:42`) drops "the Scottish idea" and concludes "a crest can mark representation of a family, not a name". The source says the opposite: a Scottish crest does not uniquely mark any one family.
- The served text at lines 17366-17377 says: "I think I am the first to put into print what actually were the rules … The rules, I believe, were undoubtedly these: — Crests were, save in the remote beginning … transmitted by an heiress. Perhaps this heritability was limited to those cases … We, judging by present laws, look upon the crest as … inseparable from the shield. What proof have we that in early times …"
  - This is one author's novel thesis about early practice, hedged with "I believe" and "Perhaps", and contrasted with present law.
  - Row 81 (`ENTRY:81`) states it flat and timeless: "crests can descend through an heiress and are not bound to a surname".
- Fixes:
  - `ENTRY:42`, the bearer cell becomes `a crest shared across unrelated grantees (Scotland)`. The case cell becomes `Fox-Davies, disapproving, reports "the Scottish idea under which the same identical crest can be and regularly is granted to half-a-dozen people of as many different surnames" (S413, chapter on crests, served text)`. The consequence becomes `in Scottish practice a crest alone does not identify a family; the arms do`.
  - `ENTRY:81`, the rule cell becomes `Fox-Davies, as his own first-in-print thesis ("I believe"; "perhaps"), holds that in early times the crest was a separate inheritance that could pass through an heiress; he contrasts this with present law (S413, chapter on crests, served text) — C`.

**H4. Restricted Northwest Coast crests are routed through museums, not holders, against the round-55 ceiling.**
- `ENTRY:154` says "describe them only as the holding museum states (S450, S451)".
  - S450 is the Museum of Anthropology at UBC's school-program "Background Information" PDF.
  - S451 is a Royal BC Museum online exhibit page.
  - Neither is the crest holders' own statement.
- The ceiling in the checklist (item A8, after the round-55 Gate S346) is "a community's own public statement can publish the existence, holder and shape of a restriction". ENTRY's prose substitutes the custodian for the holder.
- `ENTRY:111` also turns the row's "represent four Kwakwaka'wakw nations" (S451 scope) into "honour".
- Fixes:
  - `ENTRY:154`, old `describe them only as the holding museum states (S450, S451)`, new `this entry states only that crests are defined, maintained rights and where they are displayed, as two museums' public pages report (S450, S451); no holder's own statement was opened this round, so the crests, their stories and their owners are not described, and design use belongs to the holders (`myth-symbol/animal-symbolism.md:33`)`.
  - `ENTRY:111`: `honour four nations` becomes `represent four Kwakwaka'wakw nations`.

**H5. A national rule is stated as universal inside the calibration bank and the bearer table, and the entry's own rows contradict it.**
- `ENTRY:140`: "cadency marks are ancient and compulsory" is coded R with no jurisdiction. But:
  - S415's teaches cell says "only Scotland kept old differencing alive";
  - S422's scope reads "cadency differences as an office allocation";
  - `ENTRY:78` itself has Scottish matriculation.
  - So "compulsory" is rejected only for England.
- `ENTRY:41`'s consequence "each cadet needs a difference or a new record" is the Scottish rule. It contradicts `ENTRY:77`, "cadency is optional in England".
- `ENTRY:41`'s case cell cites the College of Arms (S419) without saying "England".
- Fixes:
  - `ENTRY:140`, old `| R |`, new `| R (England); B (Scotland: differencing allotted by the Lyon, S415, S422) |`.
  - `ENTRY:41`: case cell prefix `in England arms are granted or confirmed …`. The consequence becomes `no surname arms (§11); in Scotland each cadet matriculates with a difference, in England cadency is optional (§6)`.

### MEDIUM

**M1. The gap line says §2 points to every partial owner. Two named owners are missing from §2, and the §2 table misses owners that already hold ENTRY's sub-topics.**
- `ENTRY:4` names `pastoralism-animal-husbandry.md:79` and `pacific-northwest.md:109`, then says "§2 points to each one-way".
  - §2 (`ENTRY:20-32`) has neither.
  - pastoralism appears nowhere else in ENTRY.
  - pacific-northwest appears only at `:154`, as `:111`.
- Owners re-read at base `0314aa98` and absent from §2:
  - `civilizations/japan-edo.md:143`: "Assuming every repeated crest proves blood descent".
  - `civilizations/japan-medieval-sengoku.md:32`: "a crest does not establish ancestry".
  - `civilizations/turkic-steppe.md:40`: "A tamga, an inscriptional letter … must be catalogued separately".
  - `civilizations/mamluk.md:125`: the "Rank blazons" hedge.
  - `culture-material/costume-semiotics.md:43`: livery and anti-livery statutes, which overlap the S447 affinity badges.
  - `myth-symbol/color-symbolism.md:81`: the cardinal's red hat, 1245, which overlaps `ENTRY:90`.
  - `myth-symbol/color-symbolism.md:129` and `myth-symbol/symbolism-synthesis-method.md:64`: the rule of tincture, which overlaps `ENTRY:66`.
  - `culture-material/adornment-body-codes.md:20`: signet seals.
- The §2 row for warrior-material-culture (`ENTRY:27`) points to `:58` (mon) and says "owns marks beyond combat". But `warrior-material-culture.md:50-53` is titled "heraldry as grammar" and owns the European blazon grammar and the arms/badge/livery/crest stack, which duplicates ENTRY §5.
- Fixes:
  - `ENTRY:4`: `§2 points to each one-way` becomes `§2 and §13 point to them one-way`.
  - Add §2 rows:
    - `culture-material/pastoralism-animal-husbandry.md:79` | herd lexicon and ownership marks | compares brand grammar only.
    - `civilizations/japan-edo.md:143` and `civilizations/japan-medieval-sengoku.md:32` | crest ≠ descent | §6 kamon agrees.
    - `civilizations/turkic-steppe.md:40` | tamga vs letter | §11 defers.
    - `culture-material/costume-semiotics.md:43` | livery statutes | §7 affinity badges compare only.
    - `myth-symbol/color-symbolism.md:129` | rule of tincture as colour code | §5 keeps the blazon wording.
  - Rewrite the `:27` row as `culture-material/warrior-material-culture.md:50` | European blazon grammar and the arms/badge/livery/crest stack; mon on war gear (`:58`) | this entry compares authority regimes and transmission; it does not restate that grammar as general.

**M2. Calibration codes the cited rows do not carry.**
- `ENTRY:136`, "a tamga is a script", is coded R with the gloss "not an alphabet (S434)".
  - No S434 anchor or scope says "not an alphabet" or "script". The row says only "signs of group identity".
  - The owner `turkic-steppe.md:40` asks for separate cataloguing, not a rejection.
  - Fix: code `B (in S434's medieval Turkic corpus tamgas function as group-identity signs; tamga–letter resemblance is catalogued separately, `civilizations/turkic-steppe.md:40`)`.
- `ENTRY:135`, "kamon are Japanese coats of arms", is coded C. But S428 p. 2 states it flat: "No such thing as a coat-of-arms proper has ever been known in the country". Registry C means "contested interpretation"; the row does not contest anything.
  - Fix: `R (as the general equation; S428 p. 2); kamon function as badges and crests (S428, S430)`.
- `ENTRY:132`, "C for Poland": the Polish case is a bounded exception, not a contest. Fix: `B for medieval Poland, where one coat served a clan of many families (S435)`.
- `ENTRY:97`, "(C: one case, an 1853 claim)": S439 does not hedge this; the code is the entry's own judgement. Fix: `(B: one case, reported by Michelsen 1853)`.

**M3. Hedges dropped from the rows.**
- `ENTRY:44` quotes S446 as "with very few exceptions represented the office held by the amir". The same anchor sentence opens "the emblems, so far as we can understand them, with very few exceptions …". S446's teaches cell also says "on Mayer's hypothesis".
  - Fix: `Mamluk emblems, "so far as we can understand them, with very few exceptions represented the office held by the amir" (S446, served text)`.
- `ENTRY:61` reads "in Japan badges were at first assumed at will and only later conferred by chieftains on retainers".
  - McClatchie, djvu lines 17576-17584: "In Japan, as in European countries, the badges were at first assumed at will … In later times, apart from such assumption, there are to be found instances of badges being conferred … As a general rule, however, each man selected his own".
  - So conferral was occasional, and assumption stayed the rule. "Only later conferred" and the design note "grant by a lord can be a late innovation" overread the source.
  - Fix, regime cell: `self-assumed, occasionally conferred`. Case: `badges "were at first assumed at will"; later there are "instances" of a chieftain conferring one on a retainer, though "as a general rule … each man selected his own" (S428, pp. 4-5)`. Note: `a lord's grant is an occasional honour beside self-assumption`.
- `ENTRY:108`: "a masterless samurai still wears his former clan's mon (S430)".
  - The row is a V&A record of a 1962 film costume. It says the mon is "probably the emblem of his former samurai clan".
  - The hedge is dropped, and a fiction costume label is read as historical practice (checklist A7).
  - Fix: `the V&A's record of the Sanjuro (1962) film costume names a montsuki, "kimono with family crest", whose mon is "probably the emblem of his former samurai clan" (S430) — a film's reading, not evidence of Edo practice`.
- `ENTRY:93`: the purpose clause "in order to encourage a martial spirit" sits inside the row's "He is also said to have incised …".
  - Fix: `the chrysanthemum that Gotoba "is also said to have incised" on a sword tang "in order to encourage a martial spirit among his subjects" (S431, served text)`.

**M4. False provenance in the authority-regime and living-authority statements.**
- `ENTRY:59`: "an archive's design opinion for public bodies".
  - S445 is Hans Cappelen for Norsk Heraldisk Forening, a heraldry society. Its source cell reads "recommended by KS in 2009 … design advice authored by the society". KS is the municipal association.
  - Fix: `a heraldry society's design advice for municipalities | Norwegian Heraldry Society guidance (recommended by KS): …`.
- `ENTRY:154`: "described through those authorities' pages (S418, S420, S423, S443, S431)".
  - S431 is a Kyoto National Museum object record, not a page of the imperial authority. Calling the chrysanthemum "arms" is also the Eurocentric slip the checklist (A1) names.
  - Fix: `Arms and marks of living authorities (the Lord Lyon's register, the College of Arms, the Canadian Heraldic Authority, the Holy See) are described through those authorities' pages (S418, S420, S423, S443); the imperial chrysanthemum only through one national museum's object record (S431)`.
- `ENTRY:113`: "a flag simple enough for a child to draw, two or three basic colours, never writing or a seal (S452)".
  - This is one association's 2001 booklet, given unattributed as a design fact. The checklist (A6) flags NAVA "rules" as one association's guidance.
  - Fix: `NAVA's 2001 booklet advises a flag simple enough for a child to draw, two or three basic colours, and "Never use writing of any kind or an organization's seal" (S452) — one association's guidance, not a standard`.
  - Tier: S452 and S450 are filed A. NAVA advice is primary only for NAVA's opinion, and the MOA PDF is a school resource. Because the rows have landed, `corpus/QUALITY.md:29` requires a superseding SOURCES row, not an in-place edit. Leave this to the next round's Frontier.

**M5. Other universal or period slips.**
- `ENTRY:47`: "a house mark was the main means by which property was recognized (S439)". This is unscoped, but S439 is Michelsen 1853 on Germanic material.
  - Fix: `in Michelsen's 1853 German material the house mark was the main means by which property was recognized (S439)`.
- `ENTRY:68`: "The verbal blazon … governs a granted design (S418)". S418 is the College of Arms. Fix: prefix `In English grants, the verbal blazon …`.
- `ENTRY:125`: "1865 to now | state brand boards". S438 says the board was "Formed by Colorado's livestock industry in approximately 1865, when Colorado was still a territory".
  - Fix: `about 1865 to now | an industry-formed brand board that became a state division (Colorado)`.
- `ENTRY:100`: S433 covers Sarmatian-like tamgas in the Tagar Great Salbyk barrow. It is a different people and period from S434's "medieval Turkic nomads", but it is joined to that sentence without a break.
  - Fix: `; separately, in the Tagar Great Salbyk barrow, tamgas "of late time, similar to Sarmatian ones" run "in narrow stripes along the edges" (S433)`.
- `ENTRY:86`: the heading "Office and rank emblems that do not descend" is contradicted at `:89`, "the blazon was hereditary among amirs".
  - Fix: `## 7. Office and rank emblems (descent limited or absent)`.

### LOW

- **L1. Silent disagreement with an owner.** `ENTRY:139` (C: the 1149 seal shows no armory; the plaque is posthumous) disagrees with `warrior-material-culture.md:52`: "the Le Mans enamel … is the earliest surviving depiction of arms borne in person (Wagner 1956)". ENTRY cites its own row, so this is permitted, but it does not name the disagreement. Fix: append `; disagrees with `culture-material/warrior-material-culture.md:52` on "borne in person"`.
- **L2. Undefined umbrella term.** §1 (`ENTRY:14-16`) never defines "heraldry"/"arms" as the European system versus "emblem" (umbrella) versus "mark" (checklist A1). The European scope is stated only locally, at `:67`. Fix: add one sentence to §1: `"Arms"/"heraldry" means the European hereditary armory system and its derivatives; "emblem" is the umbrella; "mark" covers tamga, house, merchant and livestock marks.`

## Checks that held

- Anchors re-read at base `0314aa98` match their §2 cells and the handoff: `animal-symbolism.md:33`, `color-symbolism.md:11`, `costume-semiotics.md:13`, `sumptuary-law-rank-display.md:38`, `naming-systems.md:46`, `warrior-material-culture.md:58`, `symbolism-consistency-rules.md:154`, `mamluk.md:126`, `china-ming.md:86`, `turkic-steppe.md:96`, `writing-media-surface-economy.md:112`, `pacific-northwest.md:111`, `worldbible-integration-contract.md:17` and `:129`.
- The handoff packet fields `scope`, `claim_ledger` and `coupling_edges` exist at `worldbible-integration-contract.md:61,63,64`. The gesture owner `linguistics/gesture-co-speech-pointing.md` exists.
- Cited set equals the block: `uncited [] unrowed []`. No quote in ENTRY is over 25 words. `wc -l` gives 172 (≤ 230). The commit touches exactly `corpus/README.md`, `corpus/SOURCES.md` and ENTRY, so no back-pointer was added to any owner.
- Lore boundary: §14 makes no canon decision and states "NON-CANON: this section transfers nothing" (`ENTRY:168`). PROVINCE fit holds: myth-symbol partition (`PROVINCE.md:9-10`), no real-world rights ruling (`:17-18`; ENTRY `:154` gives no use advice).
- §15's "four rows read through Wayback captures" matches the registry: S418, S419, S422, S452.
- §5 scopes its grammar as "a British grammar" (`ENTRY:67`), and §11 scopes the surname R to England and Scotland (`ENTRY:132`).

## Verdict

**Disagree** with the entry as landed on calibration and provenance. The registry block, the size and the separability are sound.

Must fix before closure judges claim C:
- H1: redefined calibration codes, and T misused.
- H2: "each anchor quote re-located" against 40 of 42.
- H3: S413 misread twice.
- H4: holder ceiling breached.
- H5: English or Scottish rule stated as universal inside an R code.

M1–M5 are fixable defects in the same three-file land. Every fix above edits ENTRY only, except the tier corrections in M4, which need superseding rows next round. No predicate is implicated: ACCEPT-C-57 has no leg for code semantics, hedges or holder provenance. A PASS from it does not contradict these findings, and the judge must not read it as clearing them.
