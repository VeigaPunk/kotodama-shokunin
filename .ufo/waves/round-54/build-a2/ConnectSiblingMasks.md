# Claim C — sibling ownership scan

## Axis and result

**Declared axis: coverage only.** This is advisory evidence, not an admission or scope ruling. The scan found no sibling owner of masks and masquerade as linguistic-cultural worldbuilding method. It did find adjacent ownership of fictional characters, items, institutions, events and canon; implementation of assets; and produced audio. A mask entry overlaps those provinces if it changes from proposing a system to deciding fictional truth or implementing that system.

All paths below are relative to `/home/vgpnk/Projects/shokunin/`, except explicitly lane-relative verification commands. Evidence was reopened in this session on 2026-10-22. No attempt-1 scratch, external pages, other runtime, git or jj commands, installs, or sibling writes were used.

## Coverage of the scan

The root glob `*-shokunin` returned Kotodama plus these 20 siblings: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotoba, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi. Every sibling's complete `corpus/knowledge` directory and `PROVINCE.md` was searched with `functions.grep`, `case:false`, `gitignore:false`; its root `SKILL.md` was searched where present. Root `SKILL.md` was absent for audio, game-dev-2d and revenger (`functions.glob` exact `SKILL*` paths returned no files); that is an evidence limitation, not a reason to omit their corpus/province.

Search predicates, applied separately to exact lane paths to avoid a timed-out initial wildcard search:

```text
P = (?i)\b(?:masks?|masked|masking|masquerad\w*|costum\w*|theat\w*|carnival\w*|ritual[ -]+objects?|character[ -]+(?:and[ -]+|or[ -]+|/[ -]*)?(?:creature[ -]+)?design|creature[ -]+design|cosplay\w*|props?)\b
R = (?i)\b(?:ritual[ -]+objects?|ceremon\w*|festival\w*|carniv\w*|costum\w*|theat\w*|cosplay\w*|character[ -]+(?:art|creat\w*|concept\w*|design\w*)|creature[ -]+(?:art|creat\w*|concept\w*|design\w*)|sacred[ -]+objects?|funerar\w*|masquerad\w*|prop[ -]?(?:making|design)\w*)\b
D = (?i)\b(?:(?:character|creature)[ -]+(?:design\w*|art\w*|model\w*|asset\w*|animat\w*|concept\w*|creat\w*|custom\w*|backstor\w*|sheets?|silhouett\w*|rig\w*|mesh\w*|sculpt\w*)|(?:design\w*|creat\w*|model\w*|animat\w*)[ -]+(?:(?:a|the|for)[ -]+)?(?:characters?|creatures?))\b
B = \bcharacters?\b|\bcreatures?\b|ritual|theat|carnival|cosplay|props?\b|costum|masquerad
```

P searched every sibling corpus and scope document; R searched the same surfaces for related vocabulary; D searched the same surfaces for character/creature art, design, models, animation, creation and backstory. B additionally searched the four creative corpora (lore, game-dev-2d, game-dev-3d, audio) for implicit character/ritual coverage. The appendix is the union of returned `(path, matching line)` pairs: **254 matching lines in 93 files**, derived from those tool results, not a count of topic owners. All returned file pages were consumed; per-lane searches avoided the earlier combined search's file-page cap. Long matching lines were sometimes display-clipped; the decisive costume and character-backstory examples were reopened raw.

A filename scan also searched every sibling corpus using `functions.glob` with `**/*TERM*` for each of `mask, masquer, costum, theat, carniv, ritual, creature, cosplay, prop, character`. Its only filename hits were `kake-shokunin/corpus/knowledge/vault-properties.md:5` (web-property JavaScript array; **mention/homonym**) and `mado-shokunin/corpus/knowledge/window-rule-effects-getprop.md:1,12` (window-property query; **mention/homonym**). Both were opened. No mask, masquerade, costume, theatre, carnival, ritual, creature, cosplay or character filename owner was found by this bounded scan.

## Ownership evidence and contested scope

“Owner” means the declared action belongs to that sibling. “Partial owner” means only the named neighboring surface, not ownership of the proposed mask topic. “Mention” does not award scope.

| Evidence | Classification and effect on C |
|---|---|
| `lore-shokunin/PROVINCE.md:3,9`; `lore-shokunin/SKILL.md:7,16` | **Owner:** fictional entities, including characters and items, relations, timeline, integration and canon. A proposed wearing rule is not a ruling that a named character wears a particular mask, that an institution enforces it, or that its supernatural persona is objectively real. |
| `lore-shokunin/PROVINCE.md:17,18,19,23,28,35` | **Partial owner:** canon status, recorded names/dates and continuity; character knowledge and Kotodama intake are frontier/uncovered, not established capabilities. Line 28 explicitly gives generation and calendar/era design to Kotodama while reserving landed records to lore. The packet digest remains unacknowledged. |
| `lore-shokunin/corpus/knowledge/2026-10-12-lore-decision-table.md:108,120,121,170`; `lore-shokunin/corpus/knowledge/seed.md:9` | **Partial owner:** character identity, kinds and source-attributed records, not visual character or creature design. A character's self-description is not independent identity proof. |
| `lore-shokunin/corpus/knowledge/r98-clerk-scope-note.md:24` | **Partial owner:** a named fictional character and supported institutional role. This is the kind of landed record C must not produce. |
| `lore-shokunin/corpus/knowledge/r88-sourced-inspiration-decision-table.md:8,16,18,20,24,25,26,120-125` | **Partial owner:** inspiration provenance and in-world claim integration. A real-world reference is not an in-world witness, rights grant or canon proof; structural/lexical checks do not settle meaning. General research method stays with chousa. |
| `lore-shokunin/corpus/knowledge/r94-cross-myth-design-comparison.md:11,13` | **Mention:** source characters and imported ritual are expressly not established by a cross-myth comparison. Not a theatre or mask-method owner. |
| `game-dev-3d-shokunin/PROVINCE.md:3-12,33-41,51-58` | **Partial owner:** executable 3D scenes, mesh/assets, movement, animation and engine import. A cultural masking method is separate; making a playable mask/creature/prop asset or claiming runtime/rendered behavior crosses this boundary. No dedicated character concept-art or cosplay ownership is stated. |
| `game-dev-2d-shokunin/PROVINCE.md:3,10,16-19,31-33`; `game-dev-2d-shokunin/corpus/knowledge/2026-10-19-physics-replay-boundary.md:31,95` | **Partial owner:** implemented 2D characters, physics and scene/game behavior; not character backstory, cultural costume rules or canon. The corpus character hits concern movement inequalities. |
| `audio-shokunin/PROVINCE.md:3-5,25-29,53` | **Partial owner:** SFX and soundtrack signal production. Line 29 is a **mention** of character backstory and explicitly reserves canon to lore. Licensed voice as a social permission is not audio synthesis; recorded/performed audio and engine triggers are separate outputs. |
| `kotoba-shokunin/corpus/knowledge/sibling-overlap-census-round49.md:79`; `kotoba-shokunin/PROVINCE.md:3,52` | **Mention:** an old census quotes Kotodama's costume remit; Kotoba owns prompt/skill wording, not costume systems. The historical quote is not fresh source support for C. |
| `kasegi-shokunin/corpus/knowledge/repo-git-state.md:14` | **Mention:** “Halley Comet Festival” occurs only in a historical commit title; no carnival, ritual or festival-method ownership follows. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-19-arc3-r4-evm-vyper-leg.md:26` | **Mention/metaphor:** “costume-carrying” describes path-sensitive bytecode metadata, not worn objects. |
| `chousa-shokunin/PROVINCE.md:3-6`; `kotoba-shokunin/PROVINCE.md:3`; `kaidoku-shokunin/PROVINCE.md:3-6`; `revenger-shokunin/PROVINCE.md:3-6` | **Owners of different actions:** research method, prompt craft, and shipped-artifact inspection respectively. C may consume their evidence/patterns, not establish a new general research, prompt or reverse-engineering province. |

The remaining province declarations are unrelated to the requested cultural subject: `mori-shokunin/PROVINCE.md:3-4` (observability), `kumitate-shokunin/PROVINCE.md:3` (orchestration), `tsukuroi-shokunin/PROVINCE.md:3-4` (host repair), `kake-shokunin/PROVINCE.md:3` (web publishing), `kengaku-shokunin/PROVINCE.md:3` (model evaluation), `kasegi-shokunin/PROVINCE.md:3` (security research), `kagi-shokunin/PROVINCE.md:3` (vault operations), `tameshi-shokunin/PROVINCE.md:3-5` (verification method), `mado-shokunin/PROVINCE.md:3-4` (desktop configuration), `souji-shokunin/PROVINCE.md:3-4` (workspace hygiene), `tabi-shokunin/PROVINCE.md:3-4` (browser interaction), and `kama-shokunin/PROVINCE.md:3-4` (model endpoints). Their lexical hits are mentions/homonyms, itemized below.

### Contradictions and reservations for the integrator

- **Generation versus canon:** Kotodama owns candidate wearer permissions and sign systems (`kotodama-shokunin/PROVINCE.md:3-25`); lore owns actual fictional wearers, artifacts, institutions and their recorded permissions. The existing contract makes this precise at `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md:40-47`. Calling both “mask design” would conceal two different actions. Reserve the latter to lore; report any disputed request, never absorb it.
- **Declared interface versus working intake:** the same contract `:14-19,58-69,124-136` requires bilateral acknowledgement, a lore baseline and a lore disposition. Lore's `PROVINCE.md:19,28` still calls intake uncovered and the digest unacknowledged. Do not call C an operational or accepted lore handoff.
- **Missing named art owner:** game-dev-2d `PROVINCE.md:31-33`, game-dev-3d `PROVINCE.md:34-36`, and revenger `PROVINCE.md:21` cite `art-east-asian-design`; that lane was absent from the current root enumeration, and lore `PROVINCE.md:33` explicitly records the stale owner name. This does not make cosplay fabrication, production prop making, visual direction, asset clearance or real-world permissions Kotodama's. Those requests remain an integrator/operator routing question, not new scope for C.
- **Permission is not permission:** a source describing who may wear/speak in a masquerade does not authorize copying restricted objects, grant rights/training permission, or make a fictional utterance true. The local handoff contract separates these at `:92-106,163-178`; lore's inspiration table `:8,14,18` does the same. Community-access restrictions must remain attached to the particular source and practice, not generalized into a single universal masking system.

## One bounded proposed move

**In the one new entry, separate permission to speak from authority to establish truth.** Add one compact, explicitly non-canon design table distinguishing the worn object, the candidate wearer, the represented persona and the attributed utterance; ask who licenses which audience/occasion, and give a one-way pointer to the existing handoff contract for identity, institutional enforcement and truth decisions. Do not add schema fields, an importer, another corpus file or a sibling edit.

This is a proposed design rule, not an ethnographic conclusion about every tradition. It reuses the existing contract's claim-kind/evidence/canon split (`worldbible-integration-contract.md:92-106`) and symbol/costume ownership row (`:44`), rather than duplicating lore's registers. [INFERENCE] It improves coverage of C's specifically declared “embodied presence and licensed voice” surface while leaving its one-file/source/length bounds and all sibling ownership unchanged. It is not an additional adjacency claim.

| Surface | Second-order effect and bound |
|---|---|
| Runtime | [INFERENCE] A downstream designer is less likely to merge a physical wearer, performed persona and supernatural entity, or treat an authorized speech act as proof. Actual entity mappings and game/audio implementations still go to their owners. No runtime behavior changed or was exercised here. |
| Contract | Uses existing `subject_refs`, `scope`, `claim_ledger` and `requested_decisions` concepts (`worldbible-integration-contract.md:60-66`); no required-field change or newly claimed bilateral activation. |
| Substrate | Entry-local prose/table and one-way path reference only. No routing, dispatch, engine, browser, corpus gate or sibling substrate change. |
| Verification | A reader must distinguish a proposed rule, an attributed belief and a world-fact. The seven acceptance legs count/register/access-marker properties, not this semantic boundary (`kotodama-shokunin/reports/round-54/claims.json:94-99`). |

**Risks:** universalizing the four analytical distinctions; implying every masquerade speaks; converting community access restrictions into legal clearance; losing source nuance within 230 lines; or spending lines on a duplicate governance register. Keep distinctions optional and case-scoped, preserve contrary cases, cite the newly opened source that actually supports each cultural statement, and point outward instead of restating governance.

**Unrun verification for the integration owner:** run the declared `python3 -B reports/round-54/accept-c.py` from Kotodama only after integration; independently read the table and every case for canon/production/rights bleed; check that the source-supported examples still carry their specific community, wearer, occasion and access restrictions and that C remains at most 230 lines with its declared new-source floor. No build, test, linter, formatter, acceptance command or source-access gate was run by this seat.

## Complete content-hit inventory

Every comma-separated line number denotes a separate hit at the named path; classification applies to each listed line unless an exception is stated. These are search hits, not additional owners. Technical masking, code properties/props, word-character counts and metaphorical masquerading are not cultural coverage.

| Path:line(s) | Classification |
|---|---|
| `audio-shokunin/PROVINCE.md:29` | Mention — character backstory; reserves canon to lore, audio output only. |
| `audio-shokunin/corpus/knowledge/2026-10-12-fixture-battery.md:30` | Mention — acoustic/perceptual masking, not a worn mask. |
| `chousa-shokunin/SKILL.md:345,346,362,435,436` | Mention — normalization masking or metaphorical ceremony. |
| `chousa-shokunin/corpus/knowledge/citation-chain-fidelity-r24.md:73` | Mention — normalization masking or metaphorical ceremony. |
| `chousa-shokunin/corpus/knowledge/gate-baseline-r8.md:56,59,65,71,80,86,88,90,138,142,143,165,166` | Mention — normalization masking or metaphorical ceremony. |
| `chousa-shokunin/corpus/knowledge/hardening-r10.md:271` | Mention — normalization masking or metaphorical ceremony. |
| `chousa-shokunin/corpus/knowledge/json-delimiter-r24.md:56` | Mention — normalization masking or metaphorical ceremony. |
| `chousa-shokunin/corpus/knowledge/verification-r16.md:16,31,63` | Mention — normalization masking or metaphorical ceremony. |
| `game-dev-2d-shokunin/corpus/knowledge/2026-10-12-production-checklist.md:9` | Mention — collision mask, not a worn mask. |
| `game-dev-2d-shokunin/corpus/knowledge/2026-10-19-physics-replay-boundary.md:31,95` | Partial owner — runtime character movement bounds, not character design. |
| `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/executability/sequencer.md:170` | Mention — hidden failures, text characters or character of evidence; no cultural owner. |
| `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/executability/vfx-niagara-dataflow.md:37` | Mention — hidden failures, text characters or character of evidence; no cultural owner. |
| `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/gate/README.md:244,347` | Mention — hidden failures, text characters or character of evidence; no cultural owner. |
| `kagi-shokunin/PROVINCE.md:47,49` | Mention — secret/output masking or metaphorical masquerade. |
| `kagi-shokunin/SKILL.md:32,378,380,441,493,642,650` | Mention — secret/output masking or metaphorical masquerade. |
| `kagi-shokunin/corpus/knowledge/op-ref-consumption.md:32,98,101,106,107,108,109,110,111,115,124,128,129,131,200,207,209,210,212,213` | Mention — secret/output masking or metaphorical masquerade. |
| `kagi-shokunin/corpus/knowledge/transcript-hygiene.md:105` | Mention — secret/output masking or metaphorical masquerade. |
| `kaidoku-shokunin/SKILL.md:830` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-13-r2-provider-capability-matrix.md:133` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-evm-interface.md:87` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-16-frontier-rescan.md:471` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4u-04-dnfile-il.md:180` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-13-r8-01-queue-a-ops.md:342` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-14-r9-01-queue-a-ops.md:143,155,178,306` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-19-arc3-r4-evm-vyper-leg.md:26` | Mention — costume metaphor for bytecode metadata. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-20-r19-go125-toolchain-replay.md:94,97` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-20-r20-go1246-first-failure-forecast.md:1,5,12,64` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kaidoku-shokunin/corpus/knowledge/2026-10-22-r25-evm-selector-name-resolution.md:125` | Mention — bit masks, hidden error status or metaphorical masquerade. |
| `kake-shokunin/SKILL.md:222` | Mention — masked byte drift. |
| `kake-shokunin/corpus/knowledge/free-read-verbs.md:151` | Mention — masked byte drift. |
| `kake-shokunin/corpus/knowledge/ghp-subpath-spotcheck.md:16,24,102` | Mention — masked byte drift. |
| `kama-shokunin/PROVINCE.md:13` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/SKILL.md:174,660,667,687,690` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/consumer-registry.md:176` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/context-capacity.md:10,23,48,176` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/cross-lane-scope.md:14` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/endpoint-identity.md:89` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/gguf-declared-identity.md:28` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/listener-census.md:192` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/llamacpp-loading-lifecycle.md:108` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/served-identity-crosswalk.md:27,28,51,64` | Mention — /props endpoint or masked outage. |
| `kama-shokunin/corpus/knowledge/served-model-identity.md:10,18,44` | Mention — /props endpoint or masked outage. |
| `kasegi-shokunin/corpus/knowledge/repo-git-state.md:14` | Mention — festival in a historical commit title. |
| `kasegi-shokunin/corpus/knowledge/root-loss-2026-10-12.md:58` | Mention — metaphorical masquerade of a missing tree. |
| `kengaku-shokunin/PROVINCE.md:14` | Mention — /props metadata or masked evaluation/relay failure. |
| `kengaku-shokunin/SKILL.md:105` | Mention — /props metadata or masked evaluation/relay failure. |
| `kengaku-shokunin/corpus/knowledge/attrib-r21.md:85,251` | Mention — /props metadata or masked evaluation/relay failure. |
| `kengaku-shokunin/corpus/knowledge/bench-arena-task27-timeout-anatomy.md:55` | Mention — /props metadata or masked evaluation/relay failure. |
| `kotoba-shokunin/corpus/knowledge/claim-census-round12.md:54,166` | Mention — masked verification failures. |
| `kotoba-shokunin/corpus/knowledge/corpus-integrity-round11.md:203` | Mention — masked verification failures. |
| `kotoba-shokunin/corpus/knowledge/harness-independent-round41-census.md:21,47,70` | Mention — masked verification failures. |
| `kotoba-shokunin/corpus/knowledge/sibling-overlap-census-round49.md:79` | Mention — historical quotation of Kotodama costume scope. |
| `kumitate-shokunin/corpus/knowledge/kimi-mcp-plane.md:101` | Mention — bit masks, normalized fields or hidden failures. |
| `kumitate-shokunin/corpus/knowledge/kimi-residue-files.md:85,86,87,222` | Mention — bit masks, normalized fields or hidden failures. |
| `kumitate-shokunin/corpus/knowledge/ops-watchers.md:300` | Mention — bit masks, normalized fields or hidden failures. |
| `kumitate-shokunin/corpus/knowledge/remaining-scripts-census.md:652` | Mention — bit masks, normalized fields or hidden failures. |
| `kumitate-shokunin/corpus/knowledge/route-probe-cluster.md:593` | Mention — bit masks, normalized fields or hidden failures. |
| `kumitate-shokunin/corpus/knowledge/runtime-support.md:190` | Mention — bit masks, normalized fields or hidden failures. |
| `lore-shokunin/PROVINCE.md:28` | Partial owner — recorded names/dates; explicitly points generation to Kotodama. |
| `lore-shokunin/corpus/knowledge/2026-10-12-lore-decision-table.md:108,120,121,170` | Partial owner — character/entity kind and attributed fictional record checks. |
| `lore-shokunin/corpus/knowledge/holder-assessment-boundary.md:77,203,228,268,311,347,363,387,392,395,502,562,563,565,569,624` | Mention — masked failures; line 268: partial owner, character versus item schema. |
| `lore-shokunin/corpus/knowledge/r101-r10-register-first-entry.md:122` | Mention — no character adjudication or canon conclusion asserted. |
| `lore-shokunin/corpus/knowledge/r87-provenance-chain-decision-table.md:39,59,60,61,99,101,166,176,235` | Mention — masked failures; line 39: partial owner, character versus item schema. |
| `lore-shokunin/corpus/knowledge/r94-cross-myth-design-comparison.md:11,13` | Mention — source characters/ritual; expressly rejects imported canon. |
| `lore-shokunin/corpus/knowledge/r95-aftermath-scope-note.md:7,57` | Mention — no character adjudication or canon conclusion asserted. |
| `lore-shokunin/corpus/knowledge/r96-response-scope-note.md:7,61` | Mention — no character adjudication or canon conclusion asserted. |
| `lore-shokunin/corpus/knowledge/r97-acknowledgment-scope-note.md:8,70` | Mention — no character adjudication or canon conclusion asserted. |
| `lore-shokunin/corpus/knowledge/r98-clerk-scope-note.md:8,24,72` | Mention — character non-adjudication; line 24: partial owner, recorded character/office. |
| `lore-shokunin/corpus/knowledge/r99-lapse-scope-note.md:8,71` | Mention — no character adjudication or canon conclusion asserted. |
| `lore-shokunin/corpus/knowledge/seed.md:9` | Partial owner — fictional character/place/faction/item records. |
| `mado-shokunin/SKILL.md:372` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/gate-standing-use.md:385` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/hyprland-config-era-r12.md:96` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/keybind-rule-semantics.md:78,98,173,176,177,178,189,206,215,216,294` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/omarchy-drift-watch.md:232` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/tripwire-precision-r20.md:105` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/waybar-walker-semantics.md:100` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mado-shokunin/corpus/knowledge/window-rule-effects-getprop.md:32,35,113,125,142` | Mention — configuration properties/props, bit masks or hidden failures. |
| `mori-shokunin/SKILL.md:283` | Mention — bit masks or evidence/normalization masking. |
| `mori-shokunin/corpus/knowledge/audit-r11.md:121,211,252` | Mention — bit masks or evidence/normalization masking. |
| `mori-shokunin/corpus/knowledge/drift-pin-r10.md:1,24,87,97,110,113,120,125,129,131,133,135,138,141,142,147,148,152,156,157` | Mention — bit masks or evidence/normalization masking. |
| `mori-shokunin/corpus/knowledge/evidence-minimization-r18.md:16,17` | Mention — bit masks or evidence/normalization masking. |
| `mori-shokunin/corpus/knowledge/selftest-flake-r9.md:123` | Mention — bit masks or evidence/normalization masking. |
| `mori-shokunin/corpus/knowledge/verdict-machine-r5.md:76` | Mention — bit masks or evidence/normalization masking. |
| `revenger-shokunin/corpus/knowledge/round-62-commonjs-require-name-evidence.md:176,184,185` | Mention — code variable props (properties). |
| `souji-shokunin/corpus/knowledge/process-residue-observations.md:179,180,226` | Mention — sensitive-data masking. |
| `tabi-shokunin/SKILL.md:1800` | Mention — masking mutant in a verification recipe. |
| `tameshi-shokunin/SKILL.md:287,2112` | Mention — masking contract or metaphorical masquerade. |
| `tameshi-shokunin/corpus/knowledge/gates-survey-kagi.md:451` | Mention — masking contract or metaphorical masquerade. |
| `tsukuroi-shokunin/SKILL.md:2426` | Mention — mount/taint bit masks or obscured host signals. |
| `tsukuroi-shokunin/corpus/knowledge/degraded-triage-r4.md:62,69,78,92,130,137,139,270,372,399,409` | Mention — mount/taint bit masks or obscured host signals. |
| `tsukuroi-shokunin/corpus/knowledge/kernel-taint-r27.json:18,53,170,173` | Mention — mount/taint bit masks or obscured host signals. |
| `tsukuroi-shokunin/corpus/knowledge/kernel-taint-r27.md:23` | Mention — mount/taint bit masks or obscured host signals. |

## Tooling and changes

No tools installed or updated. The only write is this report; all sibling repositories and Kotodama implementation files remain untouched.
