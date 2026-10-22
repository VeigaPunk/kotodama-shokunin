# CriticClaimC — round 55 falsify, claim C (monsters and hybrid beings, S285–S357)

Seat: critic (leaf), read-only. Target: claim C as landed at `eb0a331786abee5a019308ec2ce10f141a33257b` (on claim O `454a2dc`, base `f4015e7`). Sandbox: `/fast/scratch/hyaku/kotodama-r55-falsify/CriticClaimC/lane`, a clone checked out at `eb0a331`, with the uncommitted lane `corpus/lessons/round-55.md` copied in. Paths are relative to `corpus/knowledge/` unless they start with `corpus/`, `reports/`, `tools/` or `lore-shokunin/`. Entry `E = myth-symbol/monsters-hybrid-beings.md`. No installs.

## Verdict

- **The C acceptance holds.** `accept-c.py` exits 0 at the landed tip, and all seven legs pass. The sourced body mostly holds too. I re-opened 24 cited pages by plain request (all HTTP 200, no challenge met), and most sentences I tested are CARRIED.
- **The round's declared separability command fails at the landed tip.** It exits 1 with one finding, `O->C`. This is a manifest defect, not a real dependency. C's export regex `\bS(28[5-9]|29[0-9]|[3-9][0-9][0-9])\b` covers every id from S300 to S999. O's new selftest line `tools/check-gate-quotes.py:346` uses the fixture id `S900`, so it matches. With the export narrowed to the ids C actually created (S285–S357), the same command exits 0 with no findings. Until that fix lands, the clause "each verifiable on the base plus its own lands" has no passing receipt. The lesson draft does not record this.
- **Review-only clauses:**
  - **Method, not catalogue: CARRIED, with one defect.** §12 (nine decisions, each with a failure mode, plus a build order), the §11 dossier fields and the method labels on the bullets make it a method. But the critic's anti-gazetteer test F14 fails as written: no topic section outside §2, §11 and §12 has a table or a numbered procedure. §6 and §8 also have no decision sentence of their own.
  - **Ground uncovered in substance: CARRIED.** No owner is split wholesale. But the body restates five partial owners that `CriticGapPremise.md` §1 says must only be pointed to. One of these (griffin and *Protoceratops*) gives a second calibration status for a claim that `animal-symbolism.md:109` already rates.
  - **§2 points one-way: CARRIED for the §2 table itself,** and every anchor resolves. But the head promises §2 pointers that §2 does not have, the entry misquotes the column set at `civilizations/algonquian.md:189`, and the lore anchor over-reads `PROVINCE.md`.
  - **Citations in body sentences, not parked in the head: CARRIED.** The head holds only `S285`, as the phrase "S285 and above", and every one of the 73 ids is cited in the body. Carry is thin, though: 51 of the 73 ids have exactly one body citation (F2 flag, not a failure).
- **Fixable defects found: 14.** They are listed below, each with its exact replacement text. None is a tradeoff the judge must reject.

## Command outputs (sandbox at `eb0a331`)

```
$ python3 -B reports/round-55/accept-c.py
SET PASS count=231 required=231 added=['corpus/knowledge/myth-symbol/monsters-hybrid-beings.md'] removed=[]
SWEEP PASS exit=0 rows 231 files 231 missing_from_index 0 []
FLOOR PASS cited=73 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
exit=0

$ python3 -B tools/check-claim-separability.py reports/round-55/separability-manifest.json
SEPARABILITY_DEPENDENCY O->C via export '\\bS(28[5-9]|29[0-9]|[3-9][0-9][0-9])\\b' matched tools/check-gate-quotes.py:346
SEPARABILITY: 1 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=1

$ python3 -B reports/round-55/claims-agree.py
AGREE claims=['C', 'O']
exit=0

# same manifest, C export narrowed to \bS(28[5-9]|29[0-9]|3[0-4][0-9]|35[0-7])\b (scratch copy, --root .)
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=0
```

The two rows ACCESS flags are the pre-existing rejected rows S094 and S132. Neither is a C row.

Instrument-gap mutants (scratch copy, reverted). These are not claim failures. They show what stays review-only:
- **MUT-HOLLOW.** Everything after the head was replaced by one line listing all 73 S-ids, leaving a 16-line entry. All seven legs PASS, exit 0.
- **MUT-NEIGHBOUR.** One line was appended to `myth-symbol/animal-symbolism.md`. SET PASS, exit 0.
- F15 at the tip lists three neighbour edits under `corpus/knowledge` besides the entry: `gesture-co-speech-pointing.md`, `speech-surrogates-whistled-drummed.md` and `divination-omen-systems.md`. All three come from the routed-fix commits `b9c44a2`, `81178c8` and `d52c9df`, none from `eb0a331`. But `claims.json` `records_not_claims` names only "routed registry fixes in corpus/SOURCES.md rows below S285", and the manifest's REC lands do not list these three knowledge files.

## Failing items (exact old -> new)

1. `reports/round-55/separability-manifest.json`, C `exports[0]` — DEFECT. Evidence: the finding above, where `tools/check-gate-quotes.py:346` reads `("hard-wrapped-26", lesson('- S900 — p. 1: ...`.
   - Old: `"\\bS(28[5-9]|29[0-9]|[3-9][0-9][0-9])\\b"`
   - New: `"\\bS(28[5-9]|29[0-9]|3[0-4][0-9]|35[0-7])\\b"`
   - Then re-run the separability command and paste the exit-0 receipt into the lesson.
2. `reports/round-55/claims.json` `records_not_claims`, and manifest REC `lands` — DEFECT (records are incomplete). The routed knowledge edits are not declared. Add `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`, `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` and `corpus/knowledge/myth-symbol/divination-omen-systems.md` as "routed knowledge fixes, not claims" (in the lesson's routed-fix log, if `claims.json` is frozen).
3. `E:4` (head, gap filled) — DEFECT. The head promises pointers that §2 lacks. It says §2 "points to the nearest ones one-way" after naming "composite-being rows in civilization entries" and "the hundred-year rule in `culture-material/craft-artisan-lexicon.md`". §2 has neither. Two possible fixes:
   - Add a §2 row: `` | `civilizations/olmec.md:97` | Modern composite labels ("were-jaguar") as analytic, not local names | The naming rule for composites; §1 applies it, does not re-derive it | ``
   - Or reword: "§2 points to the nearest ones one-way" -> "§2 points to the myth-symbol ones one-way; the civilization composite rows and the hundred-year rule are not used here".
4. `E:126` — WRONG-LOCATOR (misquote). `civilizations/algonquian.md:189` reads: "`feature | source/community/date | language/form/category | public/restricted/unknown | linked material or narrative practice | invention boundary | unresolved check`".
   - Old: ``the access ledger column set (`feature | source/community/date | public/restricted/unknown | invention boundary`) is at``
   - New: ``the design ledger column set (`feature | source/community/date | language/form/category | public/restricted/unknown | linked material or narrative practice | invention boundary | unresolved check`) is at``
5. `E:132` — OVER-READ. `lore-shokunin/PROVINCE.md:3` says lore "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events". Line 28 says "lore owns the names and dates recorded on landed entities and events". Neither line says "habitats".
   - Old: `Lore-shokunin owns entity existence and identity, approved names and habitats, chronology and canon (`lore-shokunin/PROVINCE.md:3-9,28`, fleet-relative).`
   - New: `Lore-shokunin owns fictional-world records — entities, relations and timeline events — the names and dates recorded on landed entities, and canon (`lore-shokunin/PROVINCE.md:3,9,28`, fleet-relative).`
6. `E:25` (§1 Rule) — OVER-READ. A dictionary lemma cannot carry "a world … has already made a moral claim". This is the lane's etic rule, and F13 found no pointer to it (`grep -c comparative-frameworks.md E` -> 0). `myth-symbol/comparative-frameworks.md:27` reads "generate with the framework, never ascribe the framework".
   - Old: `has already made a moral claim (S292, lemma ag-lǽc-wíf).`
   - New: `has already made a moral claim; "monster" is an etic sorting label (`myth-symbol/comparative-frameworks.md:27`).`
7. `E:48` (S299) — WRONG-LOCATOR. p. 115 carries only an aside on the epoch: "esta época es la transición hacia la Ilustración". The list of thirteen causes is on p. 118. Eudave sorts them into groups on pp. 121–124 (p. 124: "el último grupo denominado de lo imaginario colectivo a lo fantástico"). The row's located quotes carry none of this grouping.
   - Old: `(S299, p. 115)`
   - New: `(S299, pp. 115, 121–124)`
   - Also add a p. 124 quote to the S299 row.
8. `E:178` (S357) — OVER-READ. The page's own type field is `citation_article_type" content="Comment"`, and the S357 row's tier note says "peer-reviewed open-access comment". No "premises" are named.
   - Old: `A 2020 survey names the field's working premises (S357, Introduction).`
   - New: `A 2020 comment summarises how monster studies describes its own scope and its debt to Cohen (S357, Introduction).`
9. `E:124` (S349) — OVER-READ, mild. The paper argues that researchers "misrepresent these tribes" through the category. It does not call the category "discredited". The p. 109 text runs: "In the creation of this phenomenon, researchers drew on Native ideas of windigos…".
   - Old: `and the discredited "Windigo Psychosis" category (S349, pp. 101, 109)`
   - New: `and argues that the psychiatric "Windigo Psychosis" category misrepresents Algonquian peoples (S349, pp. 101, 109)`
10. `E:111` (S342) — OVER-READ, mild. The page says "circa 1887".
    - Old: `an 1887 snake-charmer chromolithograph`
    - New: `a circa-1887 snake-charmer chromolithograph`
11. `E:123` bold label (S348, S308) — OVER-READ. Neither page calls beings legal actors. S348 says "Tjukurpa and Australian law working together in joint management". S308 says "Transit New Zealand agreed to partially reroute the highway".
    - Old: `**Place-tied beings are legal actors.**`
    - New: `**Place-tied beings enter law and public decisions.**`
12. `E:172` (griffin and *Protoceratops*) — DEFECT (two calibration authorities). `animal-symbolism.md:109` rates Mayor's proposal "attractive, contested, not required by the literary record". The entry issues "R as an origin, C as influence" with no pointer back. That breaks `CriticGapPremise.md` must-not 8.
    - Old: `- **R as an origin, C as influence — "griffins came from *Protoceratops* fossils."**`
    - New: `- **C, as at `animal-symbolism.md:109` — "griffins came from *Protoceratops* fossils."**`
    - Keep the S352 and S343 sentences, and add: `Witton and Hing (2024) update the case against it; the status stays with animal-symbolism.`
13. Restatements without a pointer (`CriticGapPremise.md` F4 and must-not 7) — DEFECT. Each needs a pointer clause added in place, as below; no content needs removing.
    - `E:46`: "Here the "monster" is a category violation" -> "Here the "monster" is a category violation (the anomaly engine is `myth-symbol/purity-pollution-boundary-systems.md:41-48`; a generator, not a law)".
    - `E:178`: after "the mixed category that resists classification", add "(read through `myth-symbol/purity-pollution-boundary-systems.md:41-48`)".
    - `E:86` (moralised beast book): add "; the moral-bestiary reading itself is owned at `myth-symbol/animal-symbolism.md:90`".
    - `E:70` (Hereford): add "; map form stays at `myth-symbol/cosmology-cosmography.md:71`".
    - `E:111` (Mami Wata's image arrives first): add "(the print-borne icon is already at `myth-symbol/animal-symbolism.md:56`)".
14. `corpus/SOURCES.md` S346 and S348 (registry cells cited by C) — DEFECT.
    - S346: the tier cell is `B`, but its tier note opens "tier note: A — a community's own published rule". Make the two agree. A is the note's own argument; if B was intended, change the note.
    - S348: the tier note says "not a verbatim iwi statement". *Iwi* is a Māori term, and Aṉangu are not an iwi. Old `not a verbatim iwi statement` -> new `not a verbatim Aṉangu statement`.

## Review-only judgments

- **Method, not catalogue — CARRIED, but F14 FAILs.**
  - For: §12 has nine decision rows, each with a trigger and a failure mode, plus a build order. §11 maps every field back to a section. The body bullets are labelled by method: ratio, slots, donor list, joint, accretion, rim, route, door, water. §13 shows the method in use.
  - Against: §1 and §3–§10 have 0 tables and no numbered procedure. §6 and §8 open with no "Decide" sentence. The last bullets of §8 (lines 104–105) are single-tradition exemplars.
  - Smallest fix: open §6 with `Decide whether beings share a lineage and who keeps the register.` and §8 with `Decide one job per being per telling; a being may hold two.` Or amend F14 to accept §12 as the decision table.
- **Ground uncovered in substance (against `CriticGapPremise.md`) — CARRIED.**
  - What holds: the record-sheet ground (word, body rule, placement, genre, function, drift, access) is owned nowhere else. Every one of CriticGapPremise's counterexamples A and B is fixed:
    - `E:18-19` and `E:173` state Cicero and Festus separately.
    - `divination-omen-systems.md:72` carries the erratum.
    - §11 hands off attributed in-world beliefs through `worldbible-integration-contract.md:96`, with no lore `kind`.
  - Tsukumogami, T-O form and the slayer functions are not restated.
  - The residual splits are items 12 and 13 above.
- **§2 one-way — CARRIED for the table.** I re-read all 12 anchors at the tip, and each line matches its "owns" cell:
  - `animal-symbolism.md:89`, `symbolism-synthesis-method.md:24`, `trickster.md:57`, `hero-journey-variants.md:82`, `cosmology-cosmography.md:29`, `sacred-topography-pilgrimage.md:17`
  - `divination-omen-systems.md:86`, `motif-index-usage.md:91`, `eschatology-world-end-systems.md:60`, `purity-pollution-boundary-systems.md:16`, `masks-masquerade.md:18`, `real-world-inspiration-boundaries.md:97`

  The defects are outside the table: items 3, 4 and 5.
- **Body-sentence citations per S-id** (body = text after the first `## `). Totals: 112 citations, 73 distinct ids, 0 parked in the head (F1 is empty).
  - 6 citations: S295. 5: S289. 4: S304, S338.
  - 3: S287, S290, S296, S302, S307, S308.
  - 2: S286, S292, S297, S300, S301, S305, S310, S312, S318, S319, S340, S343.
  - 1: the other 51 ids — S285, S288, S291, S293, S294, S298, S299, S303, S306, S309, S311, S313–S317, S320–S337, S339, S341, S342, S344–S357.
  - Per section: §1 13, §3 8, §4 14, §5 14, §6 5, §7 15, §8 13, §9 8, §10 6, §14 16; §2, §11, §12, §13, §15 and §16 have 0.
- **Shape:** 186 lines (within 230). Two lines are over 600 characters, both in the head: line 4 (753) and line 8 (750). Critic falsifiers F5, F7, F8, F9, F10, F11 and F12 are clean: every hit is negated, attributed, or inside a calibration line.

## Sentences checked against re-opened pages (2026-10-22, plain curl; Wayback `id_` where the row used a capture)

Each item gives the entry line, the row, and a verbatim quote from the page.

- `E:97` S304, CARRIED: "Pazuzu, as a powerful demon, was frequently set up as a shield against another supernatural terror: Lamashtu" (Met blog, Wayback 20171121161933).
- `E:115` S304, CARRIED: "By the time of the Parthians, Pazuzu's image was already almo[st]…" (same page).
- `E:97` and `E:177` S304 amoral, CARRIED: "supernatural beings in ancient references seem to be presented as largely amoral" (same page).
- `E:23` and `E:114` S295, CARRIED: "The word yōkai is an ambiguous term"; "as of November 2023, the database comprises 35,257 entries" (Nichibunken English overview).
- `E:65` S309, CARRIED: "isolating the limbs or other features of diverse species and recombining them" (Princeton Introduction PDF, p. 1).
- `E:69` S312, CARRIED: "The only characteristic universally agreed upon was that they were always to be found far away" (BL blog, Wayback 20250714121333).
- `E:70` S313, CARRIED: "a Blemmye holding a spear and a shield is located in Africa"; "one in India, and another on the extreme southern edge of the inhabited world" (themappamundi.co.uk).
- `E:72` S317, CARRIED: "This protective spirit guarded the entrance into what may have been the king's private apartments. The pair to it is in the Metropolitan Museum, New York." (BM, Wayback 20250329180841).
- `E:73` S308, CARRIED: "rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided" (Te Ara print view, Wayback 20260208222348).
- `E:123` S308 Karutahi, CARRIED: "Eventually, Transit New Zealand agreed to partially reroute the highway." (same page).
- `E:86` S321, CARRIED: "Some observations may be quite accurate but they are given the same weight as totally fabulous accounts." (abdn.ac.uk/bestiary/what.php). The didactic-tool clause is also CARRIED.
- `E:86` S322, CARRIED: "the bestiary was not a single text, but a series of changeable texts" (bl.uk blog).
- `E:86` S323, CARRIED: "they often "escaped" from manuscripts to inhabit other art works" (Getty exhibition page).
- `E:88` S326, CARRIED: "I argue that the genre of literature of marvels does not exist" (von Hees PDF, p. 101); "a negligible, marginal phenomenon".
- `E:101` S335, CARRIED: "As a mythical creature believed to make rain, the dragon served as a symbol of rulers in premodern East Asia." (CMA API).
- `E:105` S341, CARRIED: "As a "capitalist" deity par excellence"; "the vast and uncountable "school" of African water spirits" (Smithsonian, Wayback 20090407065020).
- `E:111` S342, CARRIED except the date (item 10): "a fifteenth-century bronze medallion bearing a double-tailed mermaid"; "By 1901, the snake charmer had already been interpreted as an African water spirit"; "Mami Wata is recast as a demon" (Fowler page).
- `E:114` S345, CARRIED: objectDate "1890 (first edition published posthumously in 1889)" (Met API).
- `E:113` and `E:172` S343, CARRIED: "although not labelled 'griffins' in their respective cultures"; "finds it uncompelling"; "an 'ex post facto geomyth'" (Portsmouth Pure PDF).
- `E:113` and `E:171` S338, CARRIED: "Others refer to them as dragons – many taniwha looked like reptiles, had wings and ate people." (Te Ara page 1, Wayback 20260921201758).
- `E:121` S346, CARRIED: "This is a sacred place restricted by law."; "this is as much as we can say" (Uluṟu board PDF, p. 3).
- `E:123` S348, CARRIED for "joint management and statute": "Tjukurpa and Australian law working together in joint management"; "a breach of the Environment Protection and Biodiversity Conservation (…)" (uluru.gov.au). The bold label is OVER-READ (item 11).
- `E:124` S349: OVER-READ, item 9.
- `E:171` S351, CARRIED: "a large lizard- or serpent-like creature, conceived in some traditions as evil and in others as beneficent" (Britannica, Wayback 20261007001308).
- `E:176` S354, CARRIED: "a field that tries to appropriate the prestige of science"; the paracryptozoology split (Guelph PDF, pp. 6, 8).
- `E:48` S299: WRONG-LOCATOR, item 7.
- `E:178` S357: OVER-READ, item 8.

## Unrun checks

- I did not re-open the Perseus rows (S285–S287, S290, S297, S300, S310, S311), to respect the Perseus rate limit and because the row-review seats cover S285–S344. I also did not re-open S288–S294, S296, S298, S301–S303, S305–S307, S314–S316, S318–S320, S324, S325, S327–S334, S336, S337, S339, S340, S344, S347, S350, S352, S353, S355 or S356. Rows S345–S357 that I did not re-open (S347, S350, S352, S353, S355, S356) were checked only against their registered located quotes, which agree with the entry wording.
- I did not attack claim O's rules. Its separability interaction is item 1.
- I did not check that the README revision 2.12 counts reconcile beyond the SWEEP leg.
