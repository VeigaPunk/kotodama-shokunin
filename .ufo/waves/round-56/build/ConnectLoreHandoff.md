# ConnectLoreHandoff — one bounded proposal

## Axes and proposed move

**Coverage; calibration.** Supply the six requested payload families as a two-layer handoff: retain Kongo evidence and generative rules in a NON-CANON packet; identify only the existing lore fields into which lore could later approve fictional adaptations. This improves the proposed entry's handoff coverage without claiming a culture schema, importer, acknowledgement or canon decision. These are expected effects, not an admission verdict. Claim O is untouched.

## Evidence and explicit contradictions

- **Requested receiver versus actual interface:** lore owns entities, relations, chronology and consistency (`lore-shokunin/PROVINCE.md:3,9,28`). Its current checker defines only `character`, `place`, `faction`, `item` and five JSON tables (`lore-shokunin/corpus/fixtures/check_bible.py:7,25-32,43-45`); other kinds violate the checker (`:153-154`). A culture/polity dossier therefore cannot honestly be presented as an existing dedicated record type. Lore explicitly calls kotodama intake uncovered and its contract digest unacknowledged (`lore-shokunin/PROVINCE.md:19,28`; `lore-shokunin/corpus/README.md:73,79,94`). The anchors below establish candidate field mappings, not an authorized receiving directory or receipt path.
- **Early schema versus current chronology:** the proposal in `lore-shokunin/corpus/knowledge/seed.md:8-13` uses `when`/`what`; current fields are `tick`/`description` (`lore-shokunin/corpus/fixtures/check_bible.py:29-30`). The old coverage-map admission of relative-time handling is expressly reversed (`lore-shokunin/corpus/README.md:98`); the current instruction preserves the dating phrase and forbids converting relative order into a prerequisite (`lore-shokunin/SKILL.md:27`). A historical era table is not a ready-made event timeline.
- **Reference evidence versus fictional testimony:** real-world references belong in the separate four-column ledger, not fictional `sources.json` (`lore-shokunin/corpus/knowledge/reference-ledger.md:3,10-12`; `lore-shokunin/corpus/knowledge/r88-sourced-inspiration-decision-table.md:17`). The existing comparison separates editorial rows from fictional claims (`lore-shokunin/corpus/fixtures/r93-m2-kojiki-cluster/README.md:5`). A well-attested reference is still not an in-world witness.
- **Reuse the in-lane convention:** `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md:131-147` already distinguishes dossier fields, restricted access and NON-CANON status. `corpus/knowledge/synthesis/naming-canon-workflow.md:79-96,148,166-170` keeps derivations and alias relations in the packet, separate from lore's decision. `corpus/knowledge/synthesis/worldbible-integration-contract.md:58-69,126-133` requires lore's baseline and actual receipt surface, rather than an invented sibling path.

## Ready-to-paste handoff section

The following section is 14 physical lines, including its heading and blank lines. Lore anchors are fleet-root-relative; synthesis anchors are relative to kotodama's `corpus/knowledge/`.

```markdown
## Handoff to lore

Kotodama supplies a reference dossier, not a canon culture/polity record. Lore owns identity, canon and consistency (`lore-shokunin/PROVINCE.md:3,9,28`); its kinds omit culture/polity (`lore-shokunin/corpus/fixtures/check_bible.py:7`). These are conditional field mappings, not an established intake endpoint.

| Kotodama payload | Lore-facing field and retained decision |
|---|---|
| Language sketch and naming rules | Kikongo/Koongo variety, period, spelling, name slots, aliases and supported derivations stay in the packet; lore selects fictional `entities.json.name` and sourced usage `claims` (`lore-shokunin/corpus/fixtures/check_bible.py:27,156-161`). |
| Title ladder and provinces | Distinguish office, bearer, rank and regional/era variants; proposed institutional `claims` and typed `relations.json` edges use lore-selected identities, never an automatic title-to-character conversion (`lore-shokunin/corpus/fixtures/check_bible.py:27-28`). |
| Era table | Supply dated stages, founding-tradition attribution and uncertain bounds; lore chooses events and dates. `timeline.json` uses editorial ticks and descriptions, not historical-date conversion; relative order alone is not `depends_on` (`lore-shokunin/corpus/fixtures/check_bible.py:29-30`; `lore-shokunin/SKILL.md:27`). |
| Dress and rank signals | Supply materials, techniques, wearer/occasion rules and prescription versus observed use; any adopted `entities.json.claims` belong to lore-selected institutions/items, with actual wearers and enforcement decided by lore (`lore-shokunin/corpus/fixtures/check_bible.py:27,156-161`). |
| Ritual-object categories | Carry attributed roles, holder authority and public/restricted/unknown access notes; do not transmit restricted procedures. Lore decides any individual `item` and sourced `claims`; attributed efficacy is not automatically world-fact (`lore-shokunin/corpus/fixtures/check_bible.py:7,27`; `synthesis/worldbible-integration-contract.md:43,103,167`). |
| Calibration flags | Keep source locators, community/place/era, missionary/colonial filters, contested cosmogram interpretations and unknowns attached to each claim. Real-world works go to the separate reference ledger, with attribution, rights and training permission distinct (`lore-shokunin/corpus/knowledge/reference-ledger.md:3,10-12`). |

Retain an unbound research packet: NON-CANON. Binding requires bilateral contract/digest acknowledgement, lore's baseline and authorized receipt surface; canon requires a lore receipt naming approved bible IDs, resulting revision, retained qualifiers and required operator approval (`synthesis/worldbible-integration-contract.md:14-16,58,68-69,126-132`). Lore still records intake as uncovered and unacknowledged (`lore-shokunin/PROVINCE.md:19,28`); this section transfers nothing.
```

## Risks and second-order effects

- **Runtime:** the current checker reads five JSON tables, not this dossier. Putting language rules or calibration into extra JSON keys would not establish their validation. No new importer or schema is proposed.
- **Contract and substrate:** the map leaves both lanes' authority intact and creates no lore files. Actual cluster/receipt locations remain lore-supplied prerequisites, not missing paths to invent. Generic `claims` do not replace the full naming ledger or source packet.
- **Verification:** selecting an object, title or costume rule can affect names, permitted wearers, beliefs and era applicability together. Preserve those scoped links when lore accepts a subset; do not turn an attested object category into a universal ritual rule. Schema `CLEAN` and lexical `PASS` cannot certify those meanings (`lore-shokunin/SKILL.md:22-23,41-46`).

## Verification and unrun checks

Evidence above was opened and the final lore anchors re-read in this session. No external source, test, acceptance script, checker or other runtime was invoked. No tools were installed or updated.

For L1: re-read the cited field mappings after integration; check that all six payload families retain qualifiers and that the section still disclaims live intake. Run Claim C's declared `python3 -B reports/round-56/accept-c.py` on the integrated revision. A later real lore import additionally needs lore's structural, excerpt-support and manual whole-claim review (`lore-shokunin/SKILL.md:41-46`); none is claimed here.
