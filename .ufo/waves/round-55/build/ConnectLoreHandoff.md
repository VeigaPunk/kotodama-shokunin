# Claim C: lore handoff

## Axes and one bounded move

**Coverage** (C's handoff requirement) and **calibration** (an honest receiving boundary). Proposed move: describe a source-attributed, proposal-only being dossier rather than invent a bestiary schema or translate a cultural category into lore's entity `kind`. [INFERENCE] This makes all eight requested fields usable without claiming an unavailable import capability. O's operability work is outside this proposal; no tools or sibling files change.

## Evidence and contradiction

- `reports/round-55/claims.json:94-100` makes the handoff a review-only requirement, not something C's counting command establishes.
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:14-19,51-69,96-106,126-136` requires bilateral acknowledgement, proposal/evidence/canon separation, a lore-supplied baseline and receiving surface, and an explicit receipt. It expressly says the data requirements do not establish an importer.
- `corpus/knowledge/synthesis/naming-canon-workflow.md:18-22,28,65,79-96,168-170` separates names from entities, allows multiple local names, separates literal gloss from current reference, and reserves acceptance to lore.
- `lore-shokunin/PROVINCE.md:3-9,19,28` reserves fictional records, consistency and canon to lore and names kotodama intake as uncovered. `lore-shokunin/corpus/README.md:73,79,94` likewise records no acknowledged packet intake.
- `lore-shokunin/corpus/fixtures/check_bible.py:7,25-31,152-161` admits only `character`, `place`, `faction`, `item`; entity claims use `statement` and an in-world `source_id`. `lore-shokunin/corpus/fixtures/consistent/entities.json:3-11` is the concrete name/claim example, not a creature template. External research has a separate receiver: `lore-shokunin/corpus/knowledge/reference-ledger.md:3-12`, required by `lore-shokunin/corpus/knowledge/r88-sourced-inspiration-decision-table.md:17`.
- **No creature/bestiary section found.** Checked lore's `PROVINCE.md`, `SKILL.md`, `corpus/README.md`, `corpus/knowledge/seed.md:8-16`, generic fixture README/schema/example above, and recursively searched `corpus/` plus the two root contracts for `bestiary|creature|monster|hybrid being|habitat|fauna` (case-insensitive): no matches. Filename discovery found no world-bible/creature/bestiary template; both `lore-shokunin/templates/` and `lore-shokunin/corpus/templates/` are absent.

**Contradiction:** the requested bestiary destination is prospective; the inspected lore lane has neither that section nor established kotodama intake. There is no exact existing creature-receiving path to cite. The generic record shapes below are explicitly examples, not a claimed destination or acceptance.

Paths beginning `lore-shokunin/` below are relative to the fleet root; kotodama evidence paths above are lane-relative.

## Ready-to-paste handoff section (14 lines)

```markdown
## Handoff to lore: proposed beings, not canon
- Kotodama supplies proposal-only records with candidate ID, named culture/speaker, language variety, region, period and claim-level evidence or invention status.
- Native name and gloss: retain original form, transliteration and literal gloss separately; mark uncertainty and distinguish aliases from entity identity.
- Category word: record who calls the being what, with local sense and context; “monster” is an attributed classification, not an automatic species or lore `kind`.
- Body rule: state composite parts, transformations and limits as source-attributed descriptions or explicit design choices, not silently as world-facts.
- Habitat on the map: give the described region, boundary or route and its teller/source; distinguish reported placement from an approved physical range.
- Function: scope omen, guardian, moral or other role to its telling, institution and period; do not infer evil or factual supernatural power.
- Source genre: identify work/edition, locator, collector/translator and genre, such as bestiary, wonder catalogue, narrative or public community account; preserve whose perspective it records.
- Period drift: retain dated variants and changes of name, body, place or role; distinguish source date, attestation and proposed fictional era.
- Restriction flag: record known limits from the community's own public statements, or unknown status; hold restricted detail, and never infer reuse permission from public access.
- Lore owns entity existence/identity, approved names and habitats, chronology, canon and bible-wide consistency (`lore-shokunin/PROVINCE.md:3-9,28`).
- No creature/bestiary section was found: lore's schema has only character/place/faction/item (`lore-shokunin/corpus/fixtures/check_bible.py:7,25-31`).
- Existing shapes, not established intake: external inspiration belongs in `lore-shokunin/corpus/knowledge/reference-ledger.md:3-12`; entity names and cited claims are exemplified at `lore-shokunin/corpus/fixtures/consistent/entities.json:3-11`.
- Keep the dossier unbound and noncanon until lore supplies its receiving surface, baseline and receipt and both lanes acknowledge the contract digest; intake remains uncovered (`lore-shokunin/corpus/README.md:73,79,94`; `../synthesis/worldbible-integration-contract.md:14-19,68-69,126-136`).
```

## Effects, risks and verification

- **Runtime:** `kind: monster` would encounter the checker's unknown-kind branch (`check_bible.py:153-154`, static reading, not an exercised result). This proposal does not add kinds or require a lore checker change.
- **Contract:** an attested category, an attributed in-world belief and a fictional world-fact remain different claims; a correct gloss or public source cannot establish canon or permission.
- **Substrate:** use the existing UTF-8 Markdown packet/claim-ledger convention (`worldbible-integration-contract.md:51-66`); the eight payload fields are proposed dossier contents, not assertions of eight supported lore JSON keys. No actual packet is transferred here.
- **Verification risk:** source genre in the dossier is external provenance, not automatically `sources.json.kind`; period drift is not automatically an event prerequisite, and reported habitat is not an occupancy event. Current structural/lexical checks cannot certify these meanings (`lore-shokunin/SKILL.md:22-28,41-46`).
- **Performed:** local reads, filename discovery and textual searches only. **Unrun:** C/O acceptance scripts and all lore checkers/support tools. L1 should review the pasted section against C's review-only handoff criterion and run C's declared acceptance after integration; any later lore import still needs lore's documented manual/structural checks and bilateral receipt process. No admission or pass is claimed.
- **Tool installs/updates:** none. External sources opened: none.
