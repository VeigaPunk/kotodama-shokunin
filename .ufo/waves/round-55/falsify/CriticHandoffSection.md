# CriticHandoffSection — round 55 falsify, claim C §11 (Handoff to lore)

**Verdict: DEFECTS FOUND, all fixable in §11; none blocks C's mechanical legs.** §11 claims no intake, acceptance or canon outright: it says "proposal-only" and "NON-CANON". But it overstates in four places and leaves out evidence in two:

- One ownership word ("habitats") is not carried by its anchor.
- One inference ("so no bestiary section exists to receive a being") is falsified by an exercised run of lore's checker.
- One contract anchor (`:96`) is read as a rule it does not state.
- "each source-attributed" contradicts the entry's own invented beings (§10 last line, §13).
- The hold condition makes a lore receipt sound sufficient for canon or binding, which the cited contract range itself denies (`:132`, `:57`).
- It drops the evidence, carried by its own cited line PROVINCE.md:28, that lore has not acknowledged the contract and that kotodama intake is uncovered.

Compared with the build draft (`.ufo/waves/round-55/build/ConnectLoreHandoff.md`), the landed text lost the candidate ID, the scope, the evidence-or-invention status, the bilateral-acknowledgement hold, the intake-uncovered citations and the lore reference-ledger receiver. It added the `:96` over-read and the "so" inference. It kept the build's "habitats" over-read.

Axes: **calibration** (claims stated at the strength the anchor carries), **adjacency** (the seam with lore and the contract that owns the handoff format, entry header line 8).

## Checked items

- `monsters-hybrid-beings.md:132` "Lore-shokunin owns entity existence and identity, approved names and habitats, chronology and canon (`lore-shokunin/PROVINCE.md:3-9,28`)": **OVER-READ** ("habitats", "identity").
  - Evidence: PROVINCE.md:3 "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration".
  - Evidence: PROVINCE.md:28 "lore owns the names and dates recorded on landed entities and events".
  - Neither line says "habitat" or "identity". A case-insensitive search of all of `lore-shokunin/` for `habitat|bestiar|creature|monster` matches no file.
  - Identity and approved names are carried in-lane at `synthesis/worldbible-integration-contract.md:42`: "Entity identity, approved names, official/contested status". Chronology and canon are at `:17`: "lore owns world-bible entities, relations, chronology, canon decisions, and bible-wide consistency verification".
  - Lines 4-8 of the cited range are the Sources block and blank lines, and support nothing in the sentence.
  - Fix, old: `Lore-shokunin owns entity existence and identity, approved names and habitats, chronology and canon (`lore-shokunin/PROVINCE.md:3-9,28`, fleet-relative).`
  - Fix, new: `Lore-shokunin owns entity records and identity, approved names and places, chronology, canon decisions and bible-wide consistency (`synthesis/worldbible-integration-contract.md:17,42`; `lore-shokunin/PROVINCE.md:3,9,28`, fleet-relative).`

- `monsters-hybrid-beings.md:132` "Its checker admits only `character`, `place`, `faction` and `item` (`…/check_bible.py:7`)": **CARRIED**, though the anchor is thin.
  - Evidence: check_bible.py:7 `KINDS = {'character', 'place', 'faction', 'item'}`.
  - The rejection that "admits only" asserts is at `:153-154`: `errors.append(f'{location}.kind: unknown kind {row["kind"]!r}')`.
  - Exercised run: the `kind: "monster"` copy printed `VIOLATION: entities[4].kind: unknown kind 'monster'` and exited 1. The anchor should read `check_bible.py:7,153-154`.

- `monsters-hybrid-beings.md:132` "so no bestiary section exists to receive a being": **DEFECT** (non sequitur, falsified by a run).
  - The counterexample was exercised in scratch at `/fast/scratch/hyaku/kotodama-r55-falsify/CriticHandoffSection/`. I copied lore's `corpus/fixtures/consistent` and appended the §13 heron-*tekh* as an entity with `"kind": "character"` and an in-world claim. `python3 -B lore-shokunin/corpus/fixtures/check_bible.py asChar` printed "CLEAN: schema, citations, relations, timeline; 0 violations" and exited 0.
  - So a being can enter lore's schema today. The kind set shows only that there is no `monster`/`creature` kind. That no bestiary section exists is true, but the evidence for it is the search, not line 7.
  - Fix, old: `so no bestiary section exists to receive a being; a being travels as an attributed in-world belief (`synthesis/worldbible-integration-contract.md:96`).`
  - Fix, new: `and reports any other kind as a violation (`:153-154`); lore has no bestiary or creature section, so whether a being enters as a `character`, as a claim on a `place`, or not at all is lore's decision. A being's existence travels by default as an attributed in-world belief, not a world-fact (`synthesis/worldbible-integration-contract.md:43,103`).`

- `monsters-hybrid-beings.md:132` "a being travels as an attributed in-world belief (`synthesis/worldbible-integration-contract.md:96`)": **OVER-READ**.
  - Evidence: `:96` "Claim kind | Real-world reference; generative rule; candidate world-fact; attributed in-world belief; designer interpretation". That line lists five kinds and assigns none of them to beings.
  - The §11 table itself mixes kinds: a §1 lexicon gloss is a real-world reference, and a §4 body method is a generative rule.
  - The "belief, not fact" rule is carried at `:43` "Who holds a belief; whether any supernatural claim is true | Sacred doctrine is not automatically world-fact" and at `:103` "“The temple teaches P” and “P is true” are separate candidate propositions." The replacement text is in the item above.

- `monsters-hybrid-beings.md:132` "Kotodama supplies proposal-only dossiers with these fields, each source-attributed": **DEFECT** on calibration and adjacency.
  - "each source-attributed" cannot hold for an invented being. §10 orders "design an original being instead", and §13's *tekh* is invented. The contract gives that case its own status at `:97`: "Evidence status | Attested; inferred with stated bridge; contested with alternatives; invented; `(to-verify)`".
  - The dossier also drops the envelope fields the contract requires at `:60-63`: `subject_refs` ("namespaced candidate IDs, explicitly unresolved, never guessed canon IDs"), `scope`, and `claim_ledger` (claim kind, evidence status). The build draft had them at ConnectLoreHandoff.md:24, "candidate ID, named culture/speaker, language variety, region, period and claim-level evidence or invention status".
  - "supplies" is present tense, but no packet exists and lore has acknowledged nothing (see the next item).
  - The contract owns the handoff format (entry line 8). Its existing payload row for this material is `:80` "Myth-symbol register | Variant ID, attributed tellers, proposition, ritual setting, signs, interpretations, counter-readings". A free-standing "dossier" with no mapping to that row is a second format.
  - Fix, old: `Kotodama supplies proposal-only dossiers with these fields, each source-attributed:`
  - Fix, new: `Kotodama may propose dossiers as myth-symbol register payloads (`synthesis/worldbible-integration-contract.md:80`), each with a namespaced candidate ID, its scope (culture, region, language variety, period) and, per field, a claim kind and an evidence status, attested or invented (`:60-63,96-97`), carrying these fields:`

- `monsters-hybrid-beings.md:145` "Keep each dossier unbound and NON-CANON until lore supplies its receiving surface and receipt (`synthesis/worldbible-integration-contract.md:126-136`)": **DEFECT** (calibration). The anchor range is right: it is all of §8, steps 1-9 plus the acknowledgement note.
  - Evidence: `:132` says acceptance becomes a canonized import "only when the receipt also names approved bible IDs, the resulting bible revision, retained qualifiers". Otherwise it is "accepted for integration; not yet canonized". So a receipt alone never ends NON-CANON.
  - "Unbound" is a baseline property, not a receipt property. `:57` says "`none` only for a deliberately unbound research packet", and `:69` says such a packet "cannot be imported as canon without a lore baseline and a new reviewed handoff".
  - The text omits the bilateral hold at `:15`, "Initial bilateral acknowledgement is **pending** until those records exist".
  - It also omits lore's own record. PROVINCE.md:28, the line §11 itself cites, says "digest unacknowledged by lore — coverage row CM-g", and PROVINCE.md:19 says "CM-g kotodama packet intake stay `uncovered`".
  - I confirmed the record is still current. The contract's sha256 is `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`, the same digest lore's `corpus/README.md:79` names as unacknowledged, and `git grep -l 'kotodama-lore-adjacency' -- corpus/knowledge SKILL.md` in lore exits 1.
  - Fix, old: `Keep each dossier unbound and NON-CANON until lore supplies its receiving surface and receipt (`synthesis/worldbible-integration-contract.md:126-136`).`
  - Fix, new: `Each dossier stays an unbound research packet and NON-CANON: binding needs lore's baseline bible reference and receipt surface (`synthesis/worldbible-integration-contract.md:57,69,126`), and canon needs a lore receipt that names approved bible IDs and the resulting bible revision (`:132`). Lore has not acknowledged this contract (`:15`) and lists kotodama packet intake as uncovered (`lore-shokunin/PROVINCE.md:19,28`); this section sends nothing.`

- `monsters-hybrid-beings.md:134-143` field table: **DEFECT** (coverage of the entry's own method).
  - §6 (Kin and lineage) and DR-MON-05 have no field. §12 puts 05 into the build order before "then the dossier (§11)". Lineage maps onto lore's relations (PROVINCE.md:3, "relations"; check_bible.py:28, `'relations': {'from': str, 'to': str, 'type': str, 'source_id': str}`).
  - Add after the `placement` row: `| lineage | parent, sibling or brood links between candidate IDs, each with its teller; a relation, not an identity | §6 |`
  - Minor: the `body rule` row names five of §4's seven methods. Old: `method (ratio, slots, donors, joint, accretion) and parts`. New: `method (ratio, slots, donor list, diagnostic joint, edited familiar animal, accretion, departure class) and parts`.

- Adjacency loss compared with the build draft: **DEFECT** (minor).
  - The `source genre` field holds real-world references, and lore has a separate receiver for those: `lore-shokunin/corpus/knowledge/reference-ledger.md:3`, "| Work / attribution | Rights question | AI-training permission question | Use here |".
  - Lore also states the rule at `:10-12`: "These citations record real-world references, not fictional canon." The build draft cited it at ConnectLoreHandoff.md:35, but the landed text dropped it.
  - Fix: append to the `source genre` row's Content cell `; real-world references go to lore's reference ledger, not to the bible (`lore-shokunin/corpus/knowledge/reference-ledger.md:3,10-12`)`.

- `monsters-hybrid-beings.md:143` `access status` "public / restricted / unknown": **CARRIED** in substance. Its §10 source at `civilizations/algonquian.md:189` lists seven ledger columns (`feature | source/community/date | language/form/category | public/restricted/unknown | linked material or narrative practice | invention boundary | unresolved check`). §10 line 126 quotes it as four columns, which is outside §11; I'm routing that to ReviewBoundaryTable's scope.

## Unrun checks

- `reports/round-55/accept-c.py` and `accept-o.py`: not run (the assignment is review-only for §11).
- Lore's other checkers and coverage-row commands, apart from the `git grep` acknowledgement check above, were not run.
- No external sources were opened; §11 cites no S-rows.
- Tool installs or updates: none.
