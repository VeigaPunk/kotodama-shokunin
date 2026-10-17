# Review — component 01-brief (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/01-brief.yml` (338 lines, 48205 B)
- reviewed revision: **sha256 `ea0d67d0179aba4b118016f32f6cbf0d5e0dde92b1e8468ee6535e5026f2ea19`** (mtime 11:33:13 -03, verified stable over an 80 s poll; matches the digest the file's own LOG.md entry pins). The file was still being revised during the first read (310 → 338 lines); this review is against the frozen revision above and must be re-run if the digest moves.
- verdict: **FINDINGS — 7** (seed declaration complete; spine and D1 hygiene clean)
- canon: not canonized (D2 design drill)

## Verdict summary

- **Seed parameters: COMPLETE.** SEED-01..08 restate all eight round-seed
  parameters (transhumance, sky/wind cosmology, clan-segmentary pasture
  rights, herd economy + salt/dried-meat trade, pitch-accent isolate,
  tally-knot pre-writing + late lowland script, the non-negotiable spine,
  the D1 contrast).
- **Coupling model: honored in structure, incomplete in record schema and
  scene scope** — typed edges, era-clock separation, axis tagging, status
  vocabulary, and canon hygiene are declared; findings 1–2 are the schema
  gaps, 3–4 the brief's own unfollowed rules, 5–7 the contrast, registry,
  and scene-test gaps.
- **D1 hygiene: clean in this file.** Scan of the frozen revision found no
  river/binding/oath/repair imagery used as D2 design content; those words
  appear only inside contrast rows (R-*) and bans (D1B-*) or as negations.

## Violations

Each row: `component | violation | corpus path:section that forbids it`.

1. `01-brief | no scene-scale brief anywhere: interval, location, community/group, speakers/wearers, audience, and a resources/inherited-facts premise list are not fixed, and missing premises are marked only as procedural open questions (OQ-01..05), not as premises | corpus/knowledge/synthesis/coupling-model.md §4 step 1 (fix a scene-scale brief: interval, location, speakers/wearers, audience, resources; mark missing premises rather than supplying canon), §1 (every state is X[t, place, community, occasion]), §6 (packet fields require interval/place/group)`
   - Component-level only: the registry and A-ASM never require a scope or
     premise block either, so no downstream artifact supplies it.

2. `01-brief | record_fields define no place/community slot on any packet key and no mechanism slot; the contract also has no coupling-register record type (edge ID, source/target record IDs, relation, mechanism, scope, exceptions), so the §1 assertion card and the handoff contract's coupling register cannot be populated at assembly; only symbols.audience, MYTH-.teller, and costumes.wearer_rank/rite partly cover interpreter/occasion | corpus/knowledge/synthesis/coupling-model.md §1 (store each assertion as form | user/interpreter | occasion | interval | place | mechanism | evidence/status; §3 "record interpreter and setting"); corpus/knowledge/synthesis/worldbible-integration-contract.md §5 (Coupling register: edge ID, source and target record IDs/versions, relation, mechanism, scope, exceptions, evidence/design status)`

3. `01-brief | the brief's own records do not carry the fields its rules demand of records: registry rows C-01..C-10, C-14, C-ASM and the SP-*, AS-*, R-*, D1B-*, A-* blocks have no follows: entry, while RG-02 says "a record without a follows entry is rejected at review" and A-01 check 3 asserts registry rows do cite follows (inline cites exist in some blocks, e.g. D1B check: fields, but not in the RG-02 form) | corpus/QUALITY.md §1 (every factual claim carries a cited, checkable source); corpus/knowledge/verification/verification-method-overview.md §3 (rule locator: corpus filename + heading/table + matching row); self-rules RG-02 and A-01`
   - The 15 F-* items and CP-01..13 carry follows correctly; the gap is the
     other record classes and the registry rows.

4. `01-brief | comparator records CMP-01..06 carry no evidence/calibration status label, although CP-11 requires every record to label its status (design-choice | attested-comparator | contested | unknown) and F-11's stated use is "every record carries an evidence status"; their guardrail prose names cautions but no status field | corpus/QUALITY.md §2 (every framework entry names its status with the reason); corpus/knowledge/verification/calibration-registry.md §1 (authority, status vocabulary, and use)`

5. `01-brief | R-04 misstates the D1 fixture it cites: it attributes "script from the start" to D1, but the D1 fixture has E0 count tallies and introduces its alphabet only at E1 — the real D1/D2 literacy contrast is count tallies vs tally-knots and the record geometry, not script-at-start | corpus/knowledge/synthesis/worked-example-mini-culture.md §3 (Writing: "E0 has count tallies, not a script for speech. E1 introduces a local alphabet"); the brief's own F-12 names §2–§3 as the D1 reference`
   - Low severity: R-04's boundary_rule (no alphabet-first premise, no D1
     letter IDs) is unaffected.

6. `01-brief | the registry's stems do not match the round's delivered set: rows C-04..C-10 name files that were not delivered under those names (04-lexicon, 05-pantheon, 06-symbols, 07-costumes, 08-names, 09-eras, 10-records), while the delivered components/ holds 04-orthography, 05-lexicon, 06-pantheon, 07-myths-motifs, 08-symbols, 09-eras-calendar, 10-materials, 11-costumes, 12-rank-rules, 15-pragmatics with no registry row; A-01 check 2 asserts coverage of components 02–10 only, and the assembly packet_keys list omits `orthography`, a key naming-collision-gate consumes (optional, so a mapping gap, not a guaranteed gate failure). RCN-02/OQ-04/OQ-05 declare the reconciliation mechanism, but as frozen the registry cannot bind the delivered artifacts | corpus/knowledge/synthesis/worldbible-integration-contract.md §4 (artifact_manifest: artifact IDs, paths/sections, versions, file digests, record counts — identify the exact delivered bytes); §5 (artifact payload minimum content per system/naming/era-costume artifact)`
   - Severity: assembly-blocking for the manifest unless the integrator
     reconciles via RCN-02 (append rows) or OQ-04's full dispatch list.

7. `01-brief | acceptance requires six gate runs and the handoff-packet check but no observable scene tests (mundane exchange, ritual performance, era-boundary artifact), and no naming/address-at-accession, market, funeral, or inherited-garment fixture situation | corpus/knowledge/synthesis/coupling-model.md §6 ("Hand lore the graph slice, sound-law/word table, era table, costume production/access sheet, and observable scene tests"); corpus/knowledge/synthesis/worldbible-integration-contract.md §5 (suggested fixture situations: accession naming/address, interregional market, funeral, inherited garment, archaizing inscription)`

## Checked and clean (evidence)

- Seed completeness — SEED-01..08 present and faithful to the round seed,
  including the non-negotiable spine (SEED-07) and the D1 contrast (SEED-08).
- Spine: SP-01/SP-02 define verticality and wind with required_evidence;
  SP-03 + RG-05 make per-record `axis:` checkable (neutral needs rationale).
- D1 hygiene: d1_contrast R-01..06 and d1_no_import D1B-01..09 present with
  check methods; `grep -i` scan of the frozen file found no D1 design
  import. RG-01 forbids knot-as-obligation (D1B-02 aligned).
- Citation integrity: all 15 F-* locators resolve (section headers checked:
  conlang-methodology §Stage 0; blueprint §0; coupling-model §1/§3/§5.5;
  integration contract §12; lexicon-coverage-audit §2; myth gate §2;
  costume gate §2; naming gate §2; inspiration boundaries §3/§5; calibration
  registry §11; worked example §2–§3; QUALITY §1–§5; phonology gate §7), and
  every CP-* section reference resolves (semantic-fields §3–§4;
  ritual-liminality §5; politeness-taboo §3; phonetics-phonology §6;
  writing-systems §6; kinship §5/§9; pantheon-archetypes §1/§7; era-language
  staging §4/§7/§8; era-periodization §13; language-contact §4/§6/§10;
  textile-technology §2/§6; costume-language-coupling-table §2/§8;
  costume gate §4–§7; symbolism-consistency-rules §3–§5/§7; cosmology §2/§4;
  celestial §4/§8; calibration registry §1; integration contract §6/§11/§12).
- CMP-01..06 sections verified present in mongol/ainu/finnic-sami/inca/tibet/
  inuit. CP-05's parenthetical verified accurate: phonetics-phonology §6 does
  flag the stress-/syllable-/mora-timing dichotomy as Discredited (Pike 1945).
  CMP-01's guardrail verified against mongol.md §Heaven (both warnings present).
- CP-13 (added in the frozen revision) correctly resolves whistled speech to
  phonetics-phonology §7; the deferred Andean terrace comparator stays honestly
  (to-verify).
- RCN-01 evidence verified: LOG.md `round 3 D2: component 14-kin-address
  written` exists; the delivered 14-kin-address.yml does use K01–K24 and
  ES0–ES3.
- Format/canon: header keys, `canon: not canonized (D2 design drill)`,
  record ids, gate commands against existing tools/gates/*.py; the brief
  never decides canon and names lore as recipient.

## Method notes

- Reads: `sed -n` windows of <=80 lines over the component (twice: the
  11:29 revision, then the frozen 11:33 revision) and <=80-line windows over
  all corpus files cited above; digest/stat polled; the file's own LOG.md
  entry read for the digest claim.
- This file first carried an `ABSENT — component not delivered` review
  (written 11:28, when the component had not yet landed); it was replaced by
  this review when the component arrived at 11:29 and was revised to the
  frozen digest above.
- No LOG.md entry was written by this worker: the review-assignment write
  scope is this file only. No commit made; the component was not edited.