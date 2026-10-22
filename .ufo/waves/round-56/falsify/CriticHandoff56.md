# CriticHandoff56: attack on kongo-kingdom.md §14 (handoff to lore)

**Verdict: DEFECT (two fixable defects, one wrong locator, two small gaps).** Every anchor in §14 resolves, and the nine cited line sets say roughly what the entry uses them for. But the section's two load-bearing sentences say more than their anchors carry:

1. Line 151 derives "a real polity never enters as a faction or place" from the checker's kind list. Lore's checker accepts the Kingdom of Kongo as a `faction` and Mbanza Kongo as a `place` and exits 0. The bar on real polities is lore's written policy, not a check.
2. Line 162's NON-CANON condition, "until lore receipts it", is weaker than the contract it cites. A receipt alone does not canonize anything. An unbound packet cannot be imported as canon at all without a lore baseline and a new handoff. The section also leaves out that lore has not acknowledged the contract. The lane's own earlier entry, `myth-symbol/monsters-hybrid-beings.md:147`, already states the correct condition, so this section falls back from that precedent.

No real polity is handed off as a faction or place: the payload table hands over only categories, rules and dated reference stages, and line 162 says the section transfers nothing. Impacted axes: calibration, and claim C's review-only items "the entry's handoff section names what lore-shokunin's world bible receives and what stays with lore" and "each factual sentence … at the strength stated".

**Revisions read:** the lane entry at `767040e` (its working copy is unmodified). Lore HEAD is `380ef3a`; the three cited lore files were last changed at `dcfecc5` (2026-10-19), and their working copies are clean. `synthesis/worldbible-integration-contract.md` was last changed at `e1694ba`, and its working copy is clean.

## Items

- `kongo-kingdom.md:151` (Lore owns identity, canon and consistency, citing `lore-shokunin/PROVINCE.md:3,9,28`): **CARRIED.** `PROVINCE.md:3`: "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification". Line 9: "Refuses: claiming canon without an in-world citation". Line 28: "lore owns the names and dates recorded on landed entities and events". The contract states this more directly: `worldbible-integration-contract.md:17` says "lore owns world-bible entities, relations, chronology, canon decisions, and bible-wide consistency verification".
- `kongo-kingdom.md:151` (the checker admits only four kinds, citing `check_bible.py:7`): **CARRIED.** Line 7 reads "KINDS = {'character', 'place', 'faction', 'item'}", and lines 153-154 enforce it.
- `kongo-kingdom.md:151` ("so a real polity never enters as a faction or place"): **OVER-READ / DEFECT.**
  - Counterexample, kept at `/fast/scratch/hyaku/kotodama-r56-falsify/CriticHandoff56/bible-realpolity/`: one source of kind `real-world reference` (Lopes 1591), the entity `kongo` (kind `faction`, name "Kingdom of Kongo"), the entity `mbanza-kongo` (kind `place`), and a 1491 timeline event.
  - `python3 -B lore-shokunin/corpus/fixtures/check_bible.py <dir>` printed "CLEAN: schema, citations, relations, timeline; 0 violations" and exited 0.
  - The kind list cannot carry the "so". What actually excludes real polities is lore's policy: `PROVINCE.md:3` ("fictional-world records") and `reference-ledger.md:12` ("No reference work is ingested as fictional canon.").
  - Exact replacement text: "Kotodama supplies a reference dossier, not a canon culture or polity record. Lore owns world-bible entities, canon decisions and consistency (`synthesis/worldbible-integration-contract.md:17`; `lore-shokunin/PROVINCE.md:3,9,28`, fleet-relative), records fictional-world entities only (`lore-shokunin/PROVINCE.md:3`), and ingests no reference work as fictional canon (`lore-shokunin/corpus/knowledge/reference-ledger.md:10-12`). Its checker admits only `character`, `place`, `faction` and `item` (`lore-shokunin/corpus/fixtures/check_bible.py:7,153-154`) but cannot tell a real polity from a fictional one, so keeping the Kingdom of Kongo out of the bible as a faction or place is lore's policy, not a check; it travels only as a real-world reference with generative rules under `synthesis/worldbible-integration-contract.md`."
- `kongo-kingdom.md:155` (language row, "lore selects fictional names", citing `check_bible.py:27,156-161`): **WRONG-LOCATOR.**
  - Lines 156-161 are the loop that requires every entity claim to carry a statement and a resolvable `source_id`. They say nothing about names or who selects them.
  - The anchors that carry the clause are `check_bible.py:27` (the entity `'name': str` field) and `PROVINCE.md:28`: "lore owns the names and dates recorded on landed entities and events".
  - Exact replacement text: "variety, period, spelling, name slots and aliases stay in the packet; lore selects fictional names (`check_bible.py:27`; `lore-shokunin/PROVINCE.md:28`)".
- `kongo-kingdom.md:156` (title ladder row, citing `check_bible.py:27-28`): **CARRIED** (weak but adequate). Line 27 requires each entity to have "'id': str, 'kind': str, 'name': str, 'first_appearance': str, 'claims': list". A title becomes an entity only through its own row, which needs a sourced first appearance (line 155).
- `kongo-kingdom.md:157` (era table row, citing `check_bible.py:29-30`): **CARRIED.** The timeline row needs "'tick': int, 'entity_id': str, 'place_id': str, 'depends_on': list", so tick and order are lore's fields.
  - Advisory gap: lines 369-382 require every event's `place_id` to resolve to a `place` entity. A §11 stage such as the 1678 burning of São Salvador therefore cannot become a lore event without making a real place an entity.
  - Optional replacement text: "dated stages with attributed founding traditions; lore chooses events and order (`check_bible.py:29-30`); a timeline event binds a place entity (`check_bible.py:369-382`), so a dated stage informs lore's fictional events and never puts a real place on the timeline".
- `kongo-kingdom.md:158` (dress, cloth and money row, "lore decides wearers and enforcement"): **UNSUPPORTED** (no anchor given, though one exists).
  - `worldbible-integration-contract.md:44` lists lore's share as "Actual institutions, permitted wearers, objects, enforcement".
  - Exact replacement text: "materials, licences and units with their hedges; lore decides wearers and enforcement (`synthesis/worldbible-integration-contract.md:44`)".
- `kongo-kingdom.md:159` (ritual-object row, citing contract lines 43, 103 and 167): **CARRIED.**
  - Line 43: "Sacred doctrine is not automatically world-fact".
  - Line 103: "“The temple teaches P” and “P is true” are separate candidate propositions".
  - Line 167: "Hold restricted material; a bibliography is not permission".
- `kongo-kingdom.md:160` (calibration row, citing `reference-ledger.md:3,10-12`): **CARRIED.** Line 3 is the ledger's header (work, rights question, AI-training permission question, use). Lines 10-12: "These citations record real-world references, not fictional canon … No reference work is ingested as fictional canon."
- `kongo-kingdom.md:162` (NON-CANON condition, citing contract lines 14-16, 58, 68-69 and 126-132): **OVER-READ / DEFECT.**
  - The cited lines say the opposite of "until lore receipts it":
    - Line 69: "An unbound research packet … cannot be imported as canon without a lore baseline and a new reviewed handoff."
    - Line 132: "Acceptance becomes a canonized import only when the receipt also names approved bible IDs, the resulting bible revision".
  - A receipt is necessary but not sufficient. For an unbound packet (line 58: `baseline_bible_ref` is "`none` only for a deliberately unbound research packet"), no receipt of this packet can canonize it.
  - Line 68 is about artifact paths and is not relevant here; line 69 carries the point.
  - The section also omits that the route is not active:
    - Contract line 15: "Initial bilateral acknowledgement is **pending**".
    - `PROVINCE.md:28`: "digest unacknowledged by lore — coverage row CM-g".
    - `PROVINCE.md:19`: "CM-g kotodama packet intake stay `uncovered`".
  - Exact replacement text, matching the lane precedent at `myth-symbol/monsters-hybrid-beings.md:147`: "Unbound research packet and NON-CANON: binding needs lore's baseline bible reference and receipt surface (`synthesis/worldbible-integration-contract.md:58,69,126`), and canon needs a lore receipt that names approved bible IDs and the resulting bible revision (`:132`). Lore has not acknowledged this contract (`:14-15`) and lists kotodama packet intake as uncovered (`lore-shokunin/PROVINCE.md:19,28`); this section transfers nothing."
- No real polity handed off as a faction or place (whole of §14): **CARRIED in substance.** No payload row names the Kingdom of Kongo, a province or Mbanza Kongo as a lore entity. Line 156 says "no title becomes a character automatically", and line 162 says "this section transfers nothing". The only fault is the false mechanical justification at line 151, covered above.
- Tradeoff, not a defect: line 162 calls the entry an "unbound research packet" even though it carries none of the envelope fields in contract section 4 (lines 53-63). The lane uses the same wording at `monsters-hybrid-beings.md:147`, so changing it is a convention call for the L1 seat, KotodamaR56.

## Not checked

- I opened no external sources: §14 cites none.
- I did not compare §14 with the Gate lines of `corpus/lessons/round-56.md`.
- I did not attack lore's checker beyond the one real-polity counterexample.
- No tools were installed or updated.
