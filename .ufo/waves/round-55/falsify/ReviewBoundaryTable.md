# Round 55 boundary-table and pointer review

Verdict: **ACTIONABLE** — one ledger-column defect and four imprecise locators. All remaining checked anchors support the stated ownership or claim.

## DEFECT

- `monsters-hybrid-beings.md:126` → `civilizations/algonquian.md:189` — **DEFECT**. The entry's quoted ledger omits three columns. Evidence: “`feature | source/community/date | language/form/category | public/restricted/unknown | linked material or narrative practice | invention boundary | unresolved check`” (`:189`). Replace the parenthetical with exactly: ``(`feature | source/community/date | language/form/category | public/restricted/unknown | linked material or narrative practice | invention boundary | unresolved check`)``.

## WRONG-LOCATOR

- `monsters-hybrid-beings.md:33` → `myth-symbol/trickster.md:57` — **WRONG-LOCATOR** for “licensed boundary-crosser”: line 57 supports the institutional slot (“never ship a trickster without his institutional slot”), but line 13 supplies the license and boundary definition (“the licensed crossing of a boundary a culture otherwise polices”). Replace `myth-symbol/trickster.md:57` with `myth-symbol/trickster.md:13`.
- `monsters-hybrid-beings.md:36` → `myth-symbol/sacred-topography-pilgrimage.md:17` — **WRONG-LOCATOR** for the access part of “holy places, journeys, custody and access.” Line 17 supports holy places, travel and ownership; line 92 says “Access law is the entry's sharpest deliverable.” Replace `:17` with `:17,81-93`.
- `monsters-hybrid-beings.md:146` → `synthesis/worldbible-integration-contract.md:57,69,126` — **WRONG-LOCATOR** at `:57`: that row defines producer/recipient/request, not the baseline bible reference. Line 58 defines `baseline_bible_ref`; lines 69 and 126 support the handoff constraint and receipt surface. Replace `:57,69,126` with `:58,69,126`.
- `monsters-hybrid-beings.md:132` → `lore-shokunin/corpus/fixtures/check_bible.py:7` — **WRONG-LOCATOR** for “lore has no bestiary or creature section”: line 7 lists entity kinds, not the checker’s top-level sections. The section inventory is `FIELDS` at lines 25-32 and the checker loads only those section files at 43-45. Replace the clause with: “the checker reads only sources, entities, relations, timeline and contradictions, and the allowed entity kinds omit creature (`lore-shokunin/corpus/fixtures/check_bible.py:25-32,43-45`).”

## CARRIED

- `monsters-hybrid-beings.md:31` → `myth-symbol/animal-symbolism.md:89` — **CARRIED**. Evidence: “Composite beasts are engineered, not archetypal.”
- `monsters-hybrid-beings.md:32` → `myth-symbol/symbolism-synthesis-method.md:24` — **CARRIED**. Evidence: “registers”; “base partition”; “alignment matrix”; “era table.”
- `monsters-hybrid-beings.md:34` → `myth-symbol/hero-journey-variants.md:82` — **CARRIED**. Evidence: “hoard-greed cautionary tale (Fáfnir, Beowulf's dragon).”
- `monsters-hybrid-beings.md:35` → `myth-symbol/cosmology-cosmography.md:29` — **CARRIED**. Evidence: “where is the center; how many layers; what code orders the directions.”
- `monsters-hybrid-beings.md:37` → `myth-symbol/divination-omen-systems.md:86` — **CARRIED**. Evidence: “Terrestrial omen lists”; “scribe-scholar”; “the compendium as a genre.”
- `monsters-hybrid-beings.md:38` → `myth-symbol/motif-index-usage.md:91` — **CARRIED**. Evidence: “The index is a finding aid, not a theory of tradition.”
- `monsters-hybrid-beings.md:39` → `myth-symbol/eschatology-world-end-systems.md:60` — **CARRIED**. Evidence: “the bound adversary released; the fire-giant Surtr; the wolf.”
- `monsters-hybrid-beings.md:40` → `myth-symbol/purity-pollution-boundary-systems.md:16` — **CARRIED**. Evidence: “purity is not a substance; it is a boundary map.”
- `monsters-hybrid-beings.md:41` → `culture-material/masks-masquerade.md:18` — **CARRIED**. Evidence: “separate ontologies in which a mask conceals or disguises a body from ontologies in which it transforms one.”
- `monsters-hybrid-beings.md:42` → `verification/real-world-inspiration-boundaries.md:97` — **CARRIED**. Evidence: “Do not reproduce, translate, reconstruct, publish, or adapt against the restriction.”
- `monsters-hybrid-beings.md:93` → `myth-symbol/motif-index-usage.md:91` — **CARRIED**. Same finding-aid rule as the §2 pointer above.
- `monsters-hybrid-beings.md:126` → `civilizations/haudenosaunee.md:132-141` — **CARRIED**. Evidence: “The policy opposes public exhibition and exhibition use of reproductions, photographs, castings, or illustrations” (:139); lines 137-141 describe authority, image-use, distribution and custody limits. Lines 142-143 add application guidance but are not needed for the cited boundary.
- `monsters-hybrid-beings.md:126` → `culture-material/masks-masquerade.md:55` — **CARRIED**. The locator is the section heading “Access rules: who may make, keep, wear, see, know and unmask.”
- `monsters-hybrid-beings.md:132` → `synthesis/worldbible-integration-contract.md:17,42` — **CARRIED**. Evidence: “lore owns world-bible entities, relations, chronology, canon decisions” (:17); “Entity identity, approved names” (:42).
- `monsters-hybrid-beings.md:132` → `lore-shokunin/PROVINCE.md:3,9,28` — **CARRIED**. Evidence: “entities (characters, places, factions, items)” (:3); “Refuses: claiming canon without an in-world citation” (:9); lore “owns the names and dates recorded on landed entities and events” (:28).
- `monsters-hybrid-beings.md:132` → `lore-shokunin/corpus/fixtures/check_bible.py:7` — **CARRIED**. Evidence: `KINDS = {'character', 'place', 'faction', 'item'}`.
- `monsters-hybrid-beings.md:132` → `lore-shokunin/corpus/fixtures/check_bible.py:153-154` — **CARRIED**. Evidence: “if row['kind'] not in KINDS” emits “unknown kind.”
- `monsters-hybrid-beings.md:132` → `synthesis/worldbible-integration-contract.md:43,103` — **CARRIED**. Evidence: “Who holds a belief; whether any supernatural claim is true” (:43); “The temple teaches P” and “P is true” are separate propositions (:103).
- `monsters-hybrid-beings.md:132` → `synthesis/worldbible-integration-contract.md:80` — **CARRIED**. Evidence: the “Myth-symbol register” record includes “Variant ID, attributed tellers, proposition.”
- `monsters-hybrid-beings.md:132` → `synthesis/worldbible-integration-contract.md:60-63,96-97` — **CARRIED**. Evidence: candidate IDs are “explicitly unresolved” (:60); each record has “scope” and a “claim kind” and “evidence status” (:61, :63, :96-97).
- `monsters-hybrid-beings.md:142` → `lore-shokunin/corpus/knowledge/reference-ledger.md:3,10-12` — **CARRIED**. Evidence: “Real-world references (not in-world canon)” (:1); “No reference work is ingested as fictional canon” (:12).
- `monsters-hybrid-beings.md:146` → `synthesis/worldbible-integration-contract.md:132` — **CARRIED**. Evidence: canonized import requires “approved bible IDs” and “the resulting bible revision.”
- `monsters-hybrid-beings.md:146` → `synthesis/worldbible-integration-contract.md:15` — **CARRIED**. Evidence: bilateral acknowledgement is “pending until those records exist.”
- `monsters-hybrid-beings.md:146` → `lore-shokunin/PROVINCE.md:19,28` — **CARRIED**. Evidence: kotodama packet intake “stay[s] uncovered” (:19; CM-g at :28).
- `monsters-hybrid-beings.md:170` → `../verification/calibration-registry.md:35-39` — **CARRIED**. Evidence: the registry defines R/C/B/H/T as “Rejected/discredited,” “Contested,” “Bounded,” “Heuristic,” and “Unresolved provenance or claim check.”
- `monsters-hybrid-beings.md:174` → `myth-symbol/divination-omen-systems.md:72` — **CARRIED**. Evidence: the cited line records the round-55 erratum and says “Cicero's gloss has no ‘warns’.”
- `monsters-hybrid-beings.md:179` → `../verification/calibration-registry.md`; `myth-ritual-theories.md` — **CARRIED**. Evidence: Campbell calibration is at `calibration-registry.md:48,55-62`; Jung's “shadow arcs” are explicitly calibrated at `myth-ritual-theories.md:91`.

## Residual risk and verification gaps

- The `lsp` device is not available in this tool inventory; LSP status, references, definitions and diagnostics could not be run. I read the cited source lines directly; grep was only used to enumerate pointers, not as semantic proof.
- External S-row source pages and their claims, claim-O gate behavior, and build/test checks were not part of this pointer-and-boundary review and remain unverified here.
