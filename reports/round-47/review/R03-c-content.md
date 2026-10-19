# R03 — cartography entry: content review (non-author)

- Seat: `R03` | role: reviewer | claim: **C** (coverage) | round 47, loop 2, position 1
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-47/claims.json:7`
- Out path: `reports/round-47/review/R03-c-content.md` (this file)
- Non-author statement: I drafted none of C01–C04 and edited no fragment. Every judgement below is from the filed bytes at the baseline; commands are in §9. I wrote only this file.

**One-line judgment.** The cartography draft is a **real domain entry, not filler**: the five-condition register test, the seven-link survey chain, the form-by-question typology, the warrant chain, the word-fossil bank and the 14-row calibration bank are correct method and add decision surfaces the 223 entries do not have. It is **not landing-ready**: I confirm nine blocking content/assembly defects (B1–B9) — arithmetic (B1), an unreproducible gap count (B2), a false citation accusation that would corrupt a correct quote (B3), a mis-cited workshop ladder (B4), two cross-reference defects covering three references (B5–B6), a blocking worked-example inconsistency (B7), a competing-ownership sentence (B8), and an incomplete "per form" table (B9) — plus a volume problem (739 body lines against a 149-line partition median). The topic is fresh; the bytes are not yet the entry the claim describes.

---

## 1. What I reviewed and measured

| Fragment | Role | File lines | sha256 of the file I read |
|---|---|---:|---|
| C01 | entry §§1–4 | 358 | `cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d` |
| C02 | entry §§5–9 | 503 | `5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af` |
| C03 | entry §§10–15 | 287 | `4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5` |
| C04 | head block | 301 | `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0` |

These hashes pin the read; they are not a claim that the files will not change before assembly.

**Assembled fenced body (my extraction of C04's fence + C01/C02/C03 fences):**

```
body lines 739
words 17601
chars 106997
H2 sections 15
table rows (lines starting '|') 240
(to-verify) marks 29
```

**Live partition at the baseline:**

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221   (25 files; mean 150.2)
```

**Gap probes (my own, not carried):**

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access ...: No such file or directory
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
$ grep -rli 'mapmaking|portolan|graticule|theodolite' corpus/knowledge/   # 0 files each
$ grep -rli 'cadastr' corpus/knowledge/ | wc -l
2
$ grep -rliE 'cartograph|mapmak|portolan|cadastr|mappa mundi|surveyor|theodolit|compass rose|graticule|world map|drawn map|map of|maps of' corpus/knowledge/ | wc -l
28
$ grep -rniE 'cartograph|mapmak|portolan|cadastr|mappa mundi|surveyor|theodolit|compass rose|graticule|world map|drawn map|map of|maps of' corpus/knowledge/ | wc -l
31
```

The 28/31 broad-probe figure in `C04:115` reproduces exactly. The `cartograph` sub-count does **not** — see B2.

---

## 2. Is it a real domain entry? — depth judgment

### 2.1 The method is correct, not vocabulary

| Section | What it actually does | Representative evidence | Verdict |
|---|---|---|---|
| C01 §1 | States the four load-bearing choices (what is measured / preserved / drawn / who may copy) and the one-owner boundary; the map is a **composition** register, not a sixth symbolic register | `C01:86-107`; the register-of-registers rule at `:145` | real |
| C01 §2 | A **five-condition test** (ground index, bounded notation, structural selection, conventional readability, reproductibility/citability) applied object by object; "partial" is a fail, and the failure names what the object is instead | `C01:109-152`; the object table `:124-134`; field book, painting, T-O, itinerary, portolan, cadastral, star chart, stick chart, mental map | real and genuinely discriminating |
| C01 §3 | Six meaning mechanisms — selection, projection, scale, orientation, symbolization, authority — each ending in a design lever; the projection table states preserves/distorts; scale is three numbers; orientation is a convention with a cosmology | `C01:154-232`; projection table `:171-177`; scale `:184-187`; compass trap `:197`; legend `:202-207`; cartouche `:211-215` | real |
| C01 §4 | Form follows the question: eight forms with survey feed, medium, patron, exemplar, and **what each structurally cannot show**; eight trade classes and R1–R5 | `C01:234-286`; eight forms `:238-249`; trade classes `:267-276`; rules `:280-286` | real; the "cannot show" column is the best anti-typology move in the draft |
| C02 §5 | Seven-link chain (select → measure → control → reduce → project → symbolize → reproduce) with a weakest-link rule, an instrument→form table, control as political infrastructure, field book vs fair copy, and a failure table | `C02:41-147`; chain table `:47-55`; weakest-link rule `:45`; failure table `:124-133` | real |
| C02 §6 | A cost stack, four scarcity regimes, four prestige currencies, the working-map/monument split, and four loop-breaks | `C02:149-216`; cost stack `:155-162`; regimes `:168-178`; prestige `:182-187`; working/monument `:191-196` | real |
| C02 §7 | Six trade roles, six organization models, the workshop ladder, four products, three customers | `C02:218-276`; roles `:224-231`; models `:237-244`; products `:256-263`; customers `:270-274` | real, with one mis-cite (B4) |
| C02 §8 | A five-link warrant chain (warrant, record, attestation, authentication, use), the performative map, an authority ladder, five provenance failures, the contest rule, eight decisions | `C02:278-345`; warrant chain `:284-292`; performative `:294-300`; ladder `:304-312`; failures `:314-320`; contest `:324-330` | real; one tension with C03 (P2-1) |
| C02 §9 | A 13-word fossil bank (`mappa`, `charta`, `atlas`, `portolan`, `cartouche`, `legend`, `scale`, `table`, `plat`, `gazetteer`, `itinerary`, `album`, `cartulary`), the method, an ur-medium table, false fossils | `C02:347-401`; word bank `:353-367`; method `:371-378`; ur-medium table `:385-395`; false fossils `:399` | real and cartography-specific, not a lithic reuse |
| C03 §10–15 | Nine-step build order with the artifact each step writes; minimum build per form; a two-map NON-CANON example with a storm; 14 calibration rows; 12 `DR-CT` decisions; recheck; scope | `C03:73-249`; build order `:77-87`; example `:107-152`; bank `:158-173`; DR `:193-206`; recheck `:212-222`; scope `:231-247` | real; F-1 and the 5-of-8 table are defects inside it |

### 2.2 Why it is not filler

- **240 of 739 body lines are table rows.** The tables carry decision content, not layout: the form typology's "what it structurally cannot show" column (`C01:240-249`), the failure table (`C02:124-133`), the warrant chain (`C02:284-292`), the authority ladder (`C02:304-312`), and the 12 decision rows (`C03:193-206`) are all usable at a worldbuilding desk.
- **Every major section terminates in a lever, a rule, or a decision row.** The draft follows `corpus/QUALITY.md:16-17` ("decision tables, typology tables, checklists, worked examples. No essays").
- **The worked example is a derivation, not a vignette.** It runs the nine steps twice on the same lagoon, then uses a storm to show that the warrant and the update rule, not draughtsmanship, decide the dispute (`C03:107-152`). That is the register's method demonstrated rather than asserted.
- **The calibration bank is honest about status.** Fourteen rows carry R/C/B/H/T codes from `verification/calibration-registry.md:33-39`, and the "precision trap" at `C03:187` makes every number a design range until page-checked.

### 2.3 What is repetition or over-build

- `C01:164` ("the blank has three readings") and `C02:109` restate the same rule almost verbatim; `C01:204` and `C02:110` do the same for the boundary line. C02 says it removed duplication (`C02:32-34`), but these two bullets remain duplicates.
- `C03` §10 restates the projection/scale/orientation/symbol mechanisms that C01 §3 and C02 §5 own; the build order should **sequence** them, not re-describe them.
- The assembled entry is **739 body lines / 17,601 words**, against a live partition of 103–221 lines, median 149 (`C07:130,412`). This is 5.0× the median and 3.3× the longest existing entry. Table density means it is not an essay, but it is still outside the house band; C07's own pre-staging check warns outside the 100–260 band (`C07:354`). Fix by cutting the duplicate bullets and the restated mechanism prose, not the tables.

### 2.4 Depth verdict

**PASS on substance.** This is one of the stronger recent drafts in the partition: it has a real method, a real boundary argument, and a real calibration posture. The problem is assembly discipline and a handful of factual slips, not a hollow entry.

---

## 3. Boundary table — real, with one competing sentence and four missing rows

### 3.1 The eight-row table holds

I re-read every citation in `C01:94-103` at `6e9a30d`:

| Neighbour | Live text I verified | Table's disposition | Verdict |
|---|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | `:71` "T-O diagrams are symbolic, not survey maps (§10)"; `:102` "T-O diagrams are symbolic devices, not cartographic claims"; `:133` "Toponyms are cosmographic claims… A fictional map is a set of etymological arguments" | owns the world model and the T-O symbolic diagram; this entry owns the measured sheet | correct |
| `myth-symbol/sacred-topography-pilgrimage.md` | `:5` "sacred-geography mapping … as a diagram"; `:69` the three route types | owns the place register and route-as-rite; this entry owns how a route is surveyed and drawn | correct |
| `myth-symbol/direction-symbolism.md` | `:51` "The compass trap: an abstract north requires deciding *which* north — true or magnetic" | owns the orientation register; this entry owns the map convention | correct |
| `culture-material/architecture-settlement-lexicon.md` | `:95` castrum "surveyed with the **groma**… The grid is cadastral"; `:101` "instrument + founding rite + claim word" | owns the settlement lexicon; this entry owns land survey as a map-production step | correct |
| `culture-material/writing-media-surface-economy.md` | `:3` the seven surface families; `:48` palm/bark/cloth; `:62` the fossil rule; `:73` the cost ladder; `:78` "Cheapness widens the base…"; `:81` the survivor's ledger | owns the surface economy; this entry owns map-specific media and reproduction | correct |
| `civilizations/mesoamerica-primary-sources.md` | `:58` "Lienzos and cartographic histories… the copy chain is the evidence" | owns the lienzo source class; this entry cites the genre | correct |
| `culture-material/transport-mobility-lexicon.md` | `:28` "a route is only real if someone maintains it"; `:117` DR-TR-02 | owns the route institution; this entry owns the representation of a route | correct |
| `linguistics/naming-systems.md` | `:40` onomastics; `:70` "Every renaming is datable; a map is an archive of coups"; `:97` the royal-name taboo | owns toponymy; this entry owns the toponym layer of the sheet | correct |

No second owner. The explicit disclaimers at `cosmology-cosmography.md:71,:102` are the load-bearing proof, and they are live.

### 3.2 The competing sentence at cosmography `:27`

`corpus/knowledge/myth-symbol/cosmology-cosmography.md:27` defines cosmography as "the projected, inhabited version: **how the world is drawn (maps)**, named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." The draft's central gap sentence — "the corpus owns … and owns no made map" (`C04:115`; `C01:90`) — cites only `:71`/`:102`, the disclaimers, and not `:27`, the competing definition. A strict one-owner reading will ask why "drawn (maps)" is not already an owner. The answer is that `:27` owns the **cosmogram/world-picture**, while the survey→projection→reproduction sheet is a different object, but the entry must **say** that. Add one sentence to C01 §1.1 and the `- gap filled:`:

> Cosmography owns the world-drawn content (`cosmology-cosmography.md:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production.

R02 (`C-D2`) and X04 also flagged this; I independently confirm the live line and the omission.

### 3.3 Four boundary rows are missing from the table

C01's table has eight rows; C08's P1/P2 list adds four rows — `culture-material/craft-artisan-lexicon.md`, `culture-material/trade-economy-lexicon.md`, `myth-symbol/celestial-symbolism-calendars.md`, and `myth-symbol/sacred-kingship-mythic-charter.md` — and the body does develop the mapmaker trade, the legal/territorial instrument, the star-chart form, and the legal-vs-mythic charter. The `- couples:` line names craft and trade-economy but not celestial-symbolism or sacred-kingship. Add the four "owns / does not restate" rows (C08's fenced block at `C08:232-237` is integration-ready). This is table-completeness, not a collision.

### 3.4 Divination is not a collision

`myth-symbol/divination-omen-systems.md` owns the sign-reading technology; the draft contains no divinatory material. C08's ruling (`C08:141-150`) is correct. No row is strictly required; an optional one-line non-collision note would make the negative check visible.

### 3.5 Ownership verdict

**PASS.** 0 filename owners, 0 topic owners, slug unused, landing is an **A** not an **M**, and no existing entry is overwritten. The `:27` sentence is a wording fix, not a second owner.

---

## 4. Shelf honesty

### 4.1 External shelf — honest, unread, and marked

`C04:139-157` opens with "**not consulted this round** (no network at seat time)… no unread work is presented as inspected." I counted **18** external bullets, and every one carries a book-level citation with `(to-verify)` on edition, volume or page. C12 measured 18/18 (`C12:18`); C06 measured 49 of 53 external-source lines carrying an inline marker (`C06:11`), with the four unmarked lines dispositioned.

My spot checks of body claims found the same posture:

- `C01:173-177` projection rows carry "Snyder 1987 (to-verify)", "Mercator 1569 (to-verify)", "Campbell, to-verify".
- `C01:242-249` exemplars carry "(to-verify)" on the *Tabula Peutingeriana*, snow/Minard, Dunhuang, Kain & Baigent, etc.
- `C02:74` dates for triangulation and the Ordnance Survey are all "(to-verify)".
- `C02:176,182,239` institutional cases (Padrón Real, al-Idrisi, VOC, Ordnance Survey) all carry "(to-verify)".
- `C02:298,318` statutes and the Vinland Map carry "(to-verify)".
- `C02:369` marks the entire etymology bank "(to-verify) at OED level".

No unread work is presented as read. That is the main honesty test, and the draft passes it.

### 4.2 In-corpus shelf — one semantic mis-cite

C04 pins **nine** sha256 digests (lines 118–125 and 134), and C06 verified 9/9 against the live files (`C06:17`). C06 also resolved 226 citation records with 0 hard failures (`C06:11`).

I spot-checked ~25 `path:line` anchors independently. All matched the cited content except one:

- `craft-artisan-lexicon.md:44` is the **Steel (Japan)** material-grading row (`| Steel (Japan) | tamahagane…`), not the apprentice→journeyman→master ladder. The ladder table is `:54-65` (`:54` header; `:56-63` the systems; `:65` the design rule). C02's body and its audit row both call `:44` the ladder — see B4. C04's own use of `:44` for "material-grading vocabulary" is defensible; C02's is not.

### 4.3 The low-demand statement is honest

`C01:65` states the measured demand plainly: `cartograph=2`, `mapmaking=0`, `portolan=0`, `cadastr=2`, `graticule=0`, `theodolite=0`, and calls the gap a "named-but-unbuilt register, not a high-demand omission." That is the r43 lesson applied — no inflated count. The `- gap filled:` line should keep this tone; it mostly does, except for B2.

### 4.4 Shelf verdict

**PASS on honesty; one citation defect (B4).** The external shelf is a reading list, not an inspection record, and the entry says so.

---

## 5. Defects

Severity: **B** = must fix before apply; **P2** = should fix; **P3** = note.

### 5.1 Blocking

| ID | Location | Finding | Evidence | Fix |
|---|---|---|---|---|
| **B1** | `C02:98` | Arithmetic error in the false-precision rule: 0.2 mm on a 1:50,000 sheet is 10 m of ground; a survey closing at **200 m** is **20×** coarser, not "ten times". | `0.2 mm × 50,000 = 10,000 mm = 10 m`; `200 m / 10 m = 20`. The sentence says "the drawing asserts ten times the available precision." | Either change "200 m" to "100 m" or "ten times" to "twenty times". Keep the rule; it is otherwise correct. |
| **B2** | `C04:115` | The gap statement's own evidence is unreproducible: `grep -rli 'cartograph'` cannot produce "2 files / 3 lines", and `:71` does not contain the token `cartograph` (it says "Mappa Mundi" and "survey maps"). | `grep -rni 'cartograph' corpus/knowledge/` → **2 lines, 2 files**: `cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`. `grep -rli` lists files, not lines. | Write "2 files / 2 lines"; list `:102` and `mesoamerica:58`; keep `:71` as the "Mappa Mundi / survey maps" disclaimer but do not count it as a `cartograph` hit. R02 `C-D3` and X04 found this; I confirm with the exact command. |
| **B3** | `C02:36`, `C02:501` | **False accusation.** C02 says C01's quotation "a map is an archive of coups" is "not in the file" and proposes "a map is an archive of renamings" as the correction. The live line **does** contain the quoted phrase, verbatim. | `grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md` → `70:… Every renaming is datable; a map is an archive of coups.` C01's quote is exact; C03:219's "renamings" is the paraphrase. | **Do not apply C02's correction.** Drop C02's flag; keep C01's exact quote; either change C03:219 to the exact "coups" or mark it as a paraphrase. Applying C02's owed item would replace a correct citation with an invented phrase. No sibling audit caught this; grep over `reports/round-47/` finds the phrase only in C02. |
| **B4** | `C02:248`, audit row `C02:421` | The workshop-ladder anchor is wrong: `craft-artisan-lexicon.md:44` is the steel-grading row, not the apprentice→journeyman→master ladder. The audit row says ":44 workshop ladder table … real" — a false verification. | `sed -n '44p'` → `\| Steel (Japan) \| **tamahagane**…`; `grep -n 'apprentice'` → `:54` table header, `:56-63` the systems, `:65` design rule. | Change the body anchor to `:54-65` (keep `:3` for the topic-line summary and `:44` only for material grading); correct the audit row's description. C08's P1-2 is right; I confirm. |
| **B5** | `C03:79`, `C03:184` | Form-typology cross-references point at the wrong sections: `:79` says "the typology in §1–3"; `:184` says "the typology in §2". The typology is C01 **§4.1**; §2 is the five-condition test. | `C01:109` = §2 (register test); `C01:234` = §4 (material/trade classes); `C01:238` = §4.1 (the eight forms). | Change `§1–3` → `§4.1` at `:79`; change `§2` → `§4.1` at `:184`. Note: C06's correction list quotes line 79 as "§2", but the live text is "§1–3"; its fix would leave line 79 wrong. |
| **B6** | `C01:298` | C01's handoff says "Provenance/charter (§9)"; the binding map puts provenance/charter at **§8** and the container-name fossil at **§9**. | `C02:278` = `## 8. Provenance and charter`; `C02:347` = `## 9. The container-name fossil`. | Change `§9` → `§8` in the C01 handoff note. C02 flagged it; no audit fix list carries it. |
| **B7** | `C03:123`, `:137`, `:150` | The worked example's update rule is stated three incompatible ways: `:123` "re-survey after any storm that breaches a dike"; `:137` "the re-survey is not due until the levy year turns … the joint rule [is] re-survey after every breach, not every levy year"; `:150` "after a dike breach, per levy year". | The three lines quoted; C14 F-1 already failed the example on this (`C14:78,92`). Also F-2: `grep -c 'DR-CT-'` on §11 is 0, so the example does not name the decision rows it instantiates. | Adopt one rule: under C14's option A, Map A's update is "at the levy year", the joint rule is "after every breach"; make `:123`, `:137` and `:150` say that. Add `DR-CT-01..09` (or a step↔row map) to the nine bullets and the six consequences. Re-run C14. |
| **B8** | `C01:90,96`; `C04:115` vs `cosmology-cosmography.md:27` | The "owns no made map" claim is overstated against cosmography's own definition: "how the world is drawn (**maps**), named, walked, and built." The entry cites the disclaimers `:71`/`:102` but not the competing sentence `:27`. | Live `:27` text quoted; the table row at `C01:96` cites only `:71`, `:102`, `:133`. | Add the one-sentence boundary: cosmography owns the world-drawn/cosmogram content (`:27`, `:71`, `:102`); this entry owns the surveyed, projected, reproduced sheet as production. This preserves the one-owner claim instead of overstating it. R02 `C-D2`/X04 also flagged; I confirm. |
| **B9** | `C03:95-103` | "Minimum credible build **per form**" covers only **5 of the 8** forms in C01 §4.1: itinerary, cadastral, portolan, chorographic, cosmographic. Celestial/star chart, thematic, and cartographic history/lienzo are missing. | `C01:238-249` lists eight forms; `C03:97-103` lists five rows. | Either retitle "five common forms" or add the three missing rows (what each cannot do without / can skip / institution). Not caught by the sibling audits I read; C14 cites the table but does not check its completeness. |

### 5.2 Should fix (P2)

| ID | Location | Finding | Fix |
|---|---|---|---|
| **P2-1** | `C02:296` vs `C03:164` | Direct wording conflict on "the map is the territory": C02 says "not a category error but a legal operation" in a registered system; C03's calibration row 5 says "category error" flatly. C02's own §8.6 (`:334`) has the reconciling formulation: "a category error as metaphysics, but a performative fact in a registered system; keep the two apart." | Add that clause to C03's row 5, or cross-reference C02 §8.2/§8.6 from the row. Do not let the assembled entry contain both flat assertions. |
| **P2-2** | `C04:117` | "sha256 pinned for the **six** load-bearing anchors" — nine are pinned (lines 118–125 and 134). C06 verified 9/9. | Change "six" to "nine". |
| **P2-3** | assembled body | Volume: 739 body lines / 17,601 words / 240 table rows, against 103–221 lines (median 149, max 221). Duplicates: `C01:164` vs `C02:109`; `C01:204` vs `C02:110`; C03 §10 restates C01 §3's mechanisms. | Cut the duplicate C02 §5.5 bullets to pointers; make C03 §10 sequence rather than re-describe; target ≤300 lines or record a deliberate exception. Do not cut the tables. |
| **P2-4** | `C03:154-174` vs `C02:214,334` | C03 calls §12 the "full bank", but it omits C02's inline flags: "maps were rare because primitive", "the map was always a state monopoly", "a prestige map is accurate", "cheap printing made map knowledge democratic", "cadastral maps are accurate", "ancient maps were legal documents", "a registered map cannot be wrong", and the dragons note (`C02:111`). I grepped §12 for each: 0 hits. QUALITY clause 2 is still satisfied because the flags are inline in C02, but the "full bank" cross-ref overstates. | Add rows for the missing claims or reword §12 as "principal readings; the inline flags at §5.5, §6.6 and §8.6 are part of the bank." |
| **P2-5** | `C01:133` | The Marshallese stick chart is classified "**not a map** under this test: a navigation instrument that encodes swell interference, not a positional ground index". This is a contested classification, not a settled one; the `(to-verify)` marker covers the description, not the verdict. | Either soften to "not a positional map under this entry's stipulative test" (the test already says "Definition used here") or add a calibration row naming the disagreement. |
| **P2-6** | `C02:355-367` | The 13-row etymology bank is covered by one section-level `(to-verify)` at `:369`; `to-verify-triage-protocol.md:15` asks for the mark "at the exact dependency". | Add per-row markers for the non-obvious claims (`atlas` 1595, `portolan`, `gazetteer` coin, `cartulary`) or a table caption stating every row is `(to-verify)` at OED level. |
| **P2-7** | `C01:94-103` | Missing boundary rows for `craft-artisan-lexicon.md`, `trade-economy-lexicon.md`, `celestial-symbolism-calendars.md`, `sacred-kingship-mythic-charter.md`, although the body develops the mapmaker trade, the legal-instrument, star-chart and legal-vs-mythic charter cases. | Add the four rows from C08's fenced block (`C08:232-237`); the couples line already names craft and trade-economy, and the other two resolve at HEAD. |

### 5.3 Note (P3)

| ID | Location | Finding |
|---|---|---|
| **P3-1** | `C01:111` vs `:132` | The definition says "**ground**-indexed", then the star-chart row says "the test is ground-indexed, not earth-indexed". The word "ground" is doing double duty; define it once as "referent ground" or rename the condition "referent-indexed". |
| **P3-2** | `C03:162` | The portolan row's status is "**C** (overclaim)"; the registry's C is "contested empirical or historical interpretation", while an overclaim is arguably R. The row's content is right; the code mapping deserves one clause. |
| **P3-3** | `C06:260-262` | C06's correction list quotes C03 line 79 as "the typology in §2"; the live line says "§1–3". The audit's fix is directionally right but its quotation is stale. Fix the fix so the integrator changes the actual string. |
| **P3-4** | `C04:127` | C04's `craft-artisan-lexicon.md:44` bullet reads "the material-grading vocabulary (the workshop register)" — defensible for the steel-grading row, but the parenthetical should not imply the ladder; C02's ladder use is the error (B4). |

---

## 6. QUALITY.md clause verdicts

| Clause (`corpus/QUALITY.md`) | Verdict | Basis |
|---|---|---|
| **Provenance** (`:5-8`) | **PASS-with-fixes** | The shelf is honest and the anchors resolve (C06 226 records / 0 hard failures; 9/9 digests). B1 (arithmetic), B2 (unreproducible count), B3 (false quote flag), B4 (mis-cited ladder) and B5/B6 (cross-refs) must be fixed before the entry's factual surface is clean. |
| **Calibration** (`:9-12`) | **PASS** | 14-row bank with R/C/B/H/T statuses (`C03:158-173`), living-practice flags (`C03:175-185`), inline flags at `C02:214,334`, and the precision trap (`C03:187`). P2-1 and P2-4 are wording/consolidation, not missing calibration. |
| **Coupling** (`:13-15`) | **PASS** | 21/21 `- couples:` tokens resolve from the entry directory (C13; I counted 21 backticked `.md` tokens on the one physical couples line). P2-7 adds three table rows but the field is complete. |
| **Usability** (`:16-17`) | **PASS-with-flag** | 240 table rows, nine build steps, 12 decision rows, a worked example; no essay padding. The 739-line volume is the flag (P2-3); the content is usable, the length is not house-normal. |
| **Canon hygiene** (`:18-20`) | **PASS** | `- scope:` (`C04:162`) and C03 §15 state no canon; the worked example is explicitly NON-CANON (`C03:107,109,228`); the handoff is to lore-shokunin; no promotion/clearance/closure verbs in the draft. |

---

## 7. Axis verdict and landing recommendation

**Coverage: +1 genuine.** The gap is real (0 filename owners, 0 topic owners, nearest neighbours disclaim the survey sheet), the topic is fresh (only the r44 K02 seed; r45 absent; r46 zero mentions), and the entry adds method the partition does not have (projection/scale, the survey chain, the map's silences, reproduction economics, the legal/performative map). This is not a manufactured +1, and the draft does not inflate demand — it states the low count honestly.

**Operability / calibration: no harm.** The entry does not touch tools, gates, or the O/Ca claims; it decides no canon.

**Usability: temporarily harmed by volume**, not by shallowness. After the dedup pass, the entry is a clear coverage improvement.

**Landing recommendation: do not apply yet.** Apply after B1–B9 and, preferably, P2-1..P2-7. The order I recommend:

1. Fix B3 first (drop C02's false correction) so the integrator does not corrupt `naming-systems.md:70`.
2. Fix B2 (gap count), B1 (arithmetic), B4 (ladder anchor), B5/B6 (cross-refs), B8 (`:27` sentence), B9 (5-of-8 table).
3. Fix B7 and re-run C14; then re-run C06 on the assembled bytes (not the pre-fix assembly) and C05's ownership sweep at the apply-time HEAD.
4. Do the P2-3 dedup and P2-4 bank consolidation; re-measure; then apply the single C landing and the README rev 2.5, and run C10's staged sweep.

The claim's `after_required` says "audits PASS". At my read that is **not** true: C14 is FAIL on F-1/F-2, C06 is PASS-with-corrections, C07 is pre-bytes `could-not-evaluate`, C08 is PASS-with-P1, and V01 is staged-only. The content is not the blocker; the audit chain is. Re-run the audits on the corrected bytes and file the results, not the pre-fix verdicts.

---

## 8. What I did not verify

- **Every one of the 226 citation records.** I spot-checked ~25 in-corpus anchors; C06 owns the exhaustive resolution. My one semantic find (B4) is the kind of check C06 explicitly leaves to C07/C08/R03 (`C06:40`).
- **Any external bibliographic detail.** No network at seat time; every external edition/volume/page remains `(to-verify)`. I did not check the shelf against a library catalogue.
- **The README rev 2.5 bytes and the staged 224 sweep.** C09/C10 own those; I confirmed only the live arithmetic (`25/23/26/25/24/94` sums 217; `25/26/25/29/24/94` sums 223; `25/26/26/29/24/94` sums 224) and the live header/footer lines.
- **The O and Ca claims.** Other seats; I did not re-run the freshness gate or the queue successor.
- **The final assembled file.** I measured the fenced blocks as filed; the integrator's assembly could differ. The hashes in §1 pin what I read.

---

## 9. Commands and write-surface statement

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md
70:- **Critical toponymy** … Every renaming is datable; a map is an archive of coups.
$ grep -rni 'cartograph' corpus/knowledge/
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:…
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:…
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -rli 'mapmaking' … ; grep -rli 'portolan' … ; grep -rli 'graticule' … ; grep -rli 'theodolite' …
0 each
$ grep -rli 'cadastr' corpus/knowledge/ | wc -l
2
$ sed -n '44p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
| Steel (Japan) | **tamahagane** 玉鋼 …
$ grep -n -iE 'apprentice|journeyman|masterpiece' corpus/knowledge/culture-material/craft-artisan-lexicon.md
54: table header; 56-63: the seven systems; 65: design rule
$ sed -n '27p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
- **Cosmology** = … **Cosmography** = the projected, inhabited version: how the world is drawn (maps), named …
$ python3 (fence extraction)
body lines 739; words 17601; chars 106997; H2 15; table rows 240; (to-verify) 29
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221
$ python3 -c "print(25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
217 223 224
```

**Write surface:** this file only — `reports/round-47/review/R03-c-content.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..46/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed. `git status --porcelain` at my write cut showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-47/`.

**No axis is harmed by anything on disk.** The C draft is a real entry; the landing should be a corrected version of it, not a different topic and not a rollback.
