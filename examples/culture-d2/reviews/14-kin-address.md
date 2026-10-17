# Review — component 14-kin-address (culture D2)

- reviewer: round-4 review worker; round-3 missing-review completion
- target: `examples/culture-d2/components/14-kin-address.yml`
- reviewed revision: SHA-256 `4bfa35d08ae7345dea47852ebfc4734b469c671764bbefd2cc0f3a257330a6a6` (436 lines, 41,578 bytes)
- reference: `corpus/knowledge/linguistics/kinship-terminology.md`, all 158 lines; SHA-256 `ece4439fac6c4012fd6ca6a8b1ff523c924752a5d0a19d2d77d78c6ff4f0af62`
- status: **RETURN WITH FINDINGS** — 10 finding rows: 7 confirmed conflicts/delivery defects, 3 completeness or precedence HOLDs
- canon: **NON-CANON**; D2 design drill; canon decisions remain with lore-shokunin

## Verdict on the declared type

**Conditionally appropriate, not cleanly implemented.** The declared male-line pasture-holding groups and exogamy make an Omaha-style design plausible under the reference's §2. Segmentary organization alone does not select a Murdock type. The actual core merges support the choice: K01 F=FB, K02 M=MZ, distinct MB/FZ, sibling/parallel-cousin merging, and MBD raised into the mother class (`14-kin-address.yml:59–95`; reference §1, §4). These are better evidence than the social label alone.

The declaration nevertheless names the wrong side of skewing, overstates social correlations, and combines maternal-line marriage exclusion with incompatible sex-neutral cross-cousin permissions. The address layer has useful independent mechanisms, but its tables and scenes do not consistently realize its rules. Keep the Omaha option; do not treat this review as a demand to replace it with another type.

Below, component line references are to the pinned target above. Kin abbreviations: F father, M mother, B brother, Z sister, S son, D daughter, W wife, H husband; chains start from the stated ego.

## Findings

### KA14-01 — CONFIRMED: skewing side is mislabelled

`14-kin-address | T01 calls Omaha skewing patrilateral although its own MBD/MBS rules operate matrilaterally | corpus/knowledge/linguistics/kinship-terminology.md:§1, §4 rule 4`

- Evidence: line 61 says “patrilateral skewing”; lines 67–68 and K02/K03 at lines 88–89 raise the mother's brother's descendants. The reference explicitly calls the Omaha upward-skewed side **matrilateral** (line 34); patrilateral upward skew is its Crow contrast (line 35).
- Required resolution: distinguish **patrilineal descent** from **matrilateral skewing**. Correct the side label without silently changing the existing cousin equations.

### KA14-02 — CONFIRMED: alternative rejection exceeds the calibration

`14-kin-address | social correlations become necessary conditions in the type justification and rejected alternatives | corpus/knowledge/linguistics/kinship-terminology.md:§2, §3, §11`

- Evidence: T01-a's “exactly” package (line 64), Crow “requires matrilineages” (75), descriptive terminology “not an oral segmentary system” (78), and lineal terminology “presumes no unilineal groups” (81) read as categorical comparative exclusions. The component's own calibration at line 82 instead says moderate tendency, not law.
- The reference labels the packages “typical (not necessary)” and records counterexamples (§2–§3, §11). Patriliny is a legitimate D2 design reason to prefer this option; it does not establish that the rejected systems are impossible.
- Required resolution: phrase these as local design preferences or weighted fits, retaining the explicit calibration. Do not invent an external ethnographic counterexample to justify the edit.

### KA14-03 — CONFIRMED: marriage permissions fail reciprocal genealogy

`14-kin-address | marriageable FZD/FZS and a general maternal-line marriage ban cannot all apply to every ego as stated | corpus/knowledge/linguistics/kinship-terminology.md:§3, §4 rules 4 and 6, §5, §11`

- Evidence: T01-b blocks marriage toward the mother's line (67–68); T01-c and K08/K09 make FZD/FZS marriageable (70, 94–95); M5 supplies no speaker-sex distinction (57). A07 then treats this preference as a shared lineage-pair prescription (186).
- Concrete counterexample: a **woman marrying her FZS** is that man's **MBD**, the very relationship T01-b excludes. A **man marrying his FZD** is that woman's **MBS**, which K03 places in the mother's-brother class. If the maternal-line ban also binds her, that pairing needs an explicit exception too.
- K08/K09's WZ/WB and HZ/ZH extensions therefore cannot simply inherit one undifferentiated “marriageable cross-cousin” rule. This is a reciprocity check, not a claim that all real Omaha systems share one marriage law.
- Required resolution: supply the permitted-pair table from both spouses' perspectives, including the scope of the maternal-line ban and any ego-sex-conditioned design rule. Re-derive A07's giver/taker sequence and affine merges from that table; do not infer the prescription or alternation from the type name alone.

### KA14-04 — HOLD: the kin-position matrix is incomplete

`14-kin-address | parallel-cousin and descending-generation coverage does not establish a complete reference system for all egos | corpus/knowledge/linguistics/kinship-terminology.md:§1, §4 feature bundles, §9 steps 2–3`

- Evidence: K06/K07 and their matrix/table rows repeatedly enumerate FBS/MZS, both sons (92–93, 121–122, 148–149), while claiming sex-neutral sibling/parallel-cousin coverage. FBD/MZD are not explicitly mapped. They may be intended to merge, but that intention is not a completed cell.
- K10/K11 merge children with brother's children; K12 explicitly describes **a man's** sister's children (96–98, 125–127, 152–154). No corresponding female-ego derivation is supplied.
- Required resolution: explicitly map all four parallel-cousin positions and the descending positions for female as well as male egos. Clarify whether M5 means no overt speaker-sex morphology or identical reference extensions for every speaker. Those are different design commitments.

### KA14-05 — CONFIRMED: address forms do not follow one stated derivation

`14-kin-address | PH1/PH2, M2, A01 and the address table prescribe incompatible surface forms | corpus/knowledge/linguistics/kinship-terminology.md:§7 reference/address distinction, §9 steps 3 and 7`

- PH1 licenses final-H/lengthened calls **only at distance** (40), but M2 says address takes the call accent (51), and A01 applies the rising form to upward address without a distance condition (162). T2–T7 retain initial lexical H at the fire and call accent only across distance (143–148).
- PH2 says H is suppressed but illustrates an accented `pátul` (42). T8/T11/T12 similarly retain H in fire-address `túŋal/píkol/sítal` but suppress it in their distance forms (149, 152–153).
- Level address should retain lexical accent under A01, yet spouse distance forms are unaccented `weri/asa` (155–156). K06's matrix direction is “level” (121), whereas T7 and A01 assign senior-level address an up-call.
- Required resolution: choose the fire/distance derivation, distinguish lexical citation from actual surface pitch, and regenerate every table cell. These are internal inconsistencies even before the separately declared NC01 sandhi reconciliation.

### KA14-06 — HOLD: competing address axes have no selection rule

`14-kin-address | generation, seniority, skewed class and marriage-direction pitch can select different calls for one dyad | corpus/knowledge/linguistics/kinship-terminology.md:§4 feature bundles, §7 ordered address alternatives, §9 step 7`

- A01 uses “person a generation up/down” (162), but K02/K03 assign genealogical G0 cousins to a parent-generation term class. The component does not say whether pitch follows genealogical generation, terminological class, or actual relative age in such a case.
- A07 requires takers to up-call the giver lineage (186). An older taker addressing a much younger giver can receive a down-call instruction from A01 and an up-call instruction from A07.
- Required resolution: declare a deterministic priority or a separately marked address dimension and show both conflict cases. PH3 and A03 **already explicitly override pitch by flattening**; their intentional suppression is not itself a defect. The unresolved issue is how the other axes select the pre-flattening form.

### KA14-07 — CONFIRMED: personal-name permissions conflict without bounded exceptions

`14-kin-address | public joking and name-bearing teknonyms collide with the universal winter-fire/name-taboo rules | corpus/knowledge/linguistics/kinship-terminology.md:§7 address occupancy and teknonymy, §9 steps 4 and 7`

- A02 permits personal names only at the same fire in the same winter shelter (166). A08 licenses K08/K09 wind-names **in public** (190), without restricting place, season or taboo state.
- A06 makes `<child-name>-ánpa` an address option after first birth and removes the parent's own name from public use (182). That still contains a child's personal name. A03 bans wind-names during storms (170), and R01 bans **any personal name** (230–234); no name-free teknonym or explicit prohibition on the compound is given.
- Required resolution: state which licences override A02, constrain joking under storm/mourning/avoidance, and decide whether a child's name inside a teknonym is taboo. A workable exception hierarchy is a design option, not a reason to erase the taboos.

### KA14-08 — CONFIRMED: stress-test rows do not test the declared licences

`14-kin-address | CTX2 applies the cross-cousin joking licence to parallel-cousin terms, and SC3 realizes refusal as silence | corpus/knowledge/linguistics/kinship-terminology.md:§7 refusal events, §9 step 7`

- CTX2 uses `táŋa/túŋa` with “joking licence (A08)” (244). Those are K06/K07 sibling/parallel-cousin terms, whereas A08 explicitly licenses **K08/K09** cross-cousin/affinal dyads (188–191).
- SC3 explicitly says the child refuses by “silence” (297), whereas A12 says refusal is a move, **not a silence**, and gives the repair ladder (206). Its test list names A05/CTX6 but does not exercise A12.
- SC1 additionally calls both claimants `táŋa` and tests “both stand level” (291–292). If this is reciprocal address, seniority is not reciprocal; if a third ego supplies the reference terms, identify that ego and distinguish reference from address.
- Required resolution: align the scene participants, terms, refusal act and test IDs with the rules, then actually trace the corrected scenes. Scene presence alone is not a consistency pass.

### KA14-09 — HOLD: register exit and ritual citation remain underspecified

`14-kin-address | the salt-rite escape and closed-name recitation lack conditions sufficient for an unambiguous register trace | corpus/knowledge/linguistics/kinship-terminology.md:§5 avoidance/joking, §7 fictive kin, §9 steps 4 and 7`

- ES1 says the salt rite routes around the cold-pass register (265). A05 makes participants salt-kin (178), but R01-a defines the taboo through an existing nonpreferred marriage and whether the families were kin **before the wedding** (216). State whether the rite must precede that wedding or can discharge an already-triggered affinity; adding a later fictive relation does not itself change that earlier condition.
- A04 closes the name until the reckoning and imposes the still-breath year (174); R01-c and S07 forbid personal names in the triggered register (220, 230). CTX4 recites closed names from the knot without dating the assembly or stating a ritual exception (246). It may be intended as the permitted reckoning, but that timing is not specified.
- SC4's joking brother-in-law can be a relay **within** the required substitute register; A09 says the whole audience is bound (194). Do not read the relay as an undocumented exemption from that rule (300).
- Required resolution: document the rite's timing/exit condition and the permitted citation context, then trace the affected wedding, mourning and tally-recitation scenes.

### KA14-10 — CONFIRMED: document structure blocks the existing reader

`14-kin-address | morphology_kin mixes a mapping entry and sequence items at the same indentation; the full component is not consumable by the existing YAML-subset reader | corpus/knowledge/linguistics/kinship-terminology.md:§9 step 8, §12 handoff artifacts`

- Evidence: `morphology_kin:` has `note:` followed by same-indent `- id:` items (46–58), without a list-valued key. The repository reader `tools/gates/costume-era-consistency-gate.py:322` rejects both the full file and that isolated block: `input is not one mapping (or has unparsed trailing lines)`.
- Required resolution: repair the container structure while preserving its records, then recheck parsing. This is a delivery defect, not a verdict on Omaha terminology. PyYAML is unavailable here, so the repository subset-reader result is **not** general YAML certification or an exhaustive syntax audit.

## Checks run and limits

- Read the complete target in 120/120/120/76-line chunks and the complete assigned reference in 120/38-line chunks. Applied reference §1–§5, §7, §9, §11–§12; no new real-world citation was added or independently verified.
- A read-only `python3 -B` audit computed the pinned hashes and counted **24 K records, 12 address rules, 15 term-table rows, 8 context rows, 6 scenarios, 5 inherited OQ records**. These are coverage counts, not semantic passes.
- Executed the existing `parse_packet` function via `runpy.run_path`, on the full target and on lines 46–58 separately: **both rejected** with the error recorded in KA14-10. `importlib.util.find_spec('yaml')` returned unavailable. No dependency was installed and no gate or fixture was changed.
- Checked marriage permissions by the reciprocal FZS→MBD and FZD→MBS paths above; compared the pitch/name/scene examples directly with their governing rules. These are manual counterexample checks, not a kinship gate implementation.
- Did **not** run or claim a clean packet gate battery. `tools/assemble-d2.py:140` explicitly leaves component 14's address proposals outside its base-ledger merge; a clean assembled packet would not establish that these rules work.
- Existing strengths retained: explicit DESIGN/NON-CANON status; named reference/address distinction; stranger first-contact term and broker/rite concept; explicit audience-triggered avoidance and prosodic override; era-stratified written/spoken proposals; calibration and open-question sections. These do not cancel the findings.

## Flags and handoff

- **10 finding rows = 7 CONFIRMED + 3 HOLD** (KA14-04, KA14-06, KA14-09). None is silently excised or counted as resolved.
- **5 inherited open questions remain open**: OQ-01 homophony sweep; OQ-02 wider phonology/sandhi; OQ-03 K19 donor form; OQ-04 rite ownership; OQ-05 ledger ownership (`14-kin-address.yml:404–409`). K19/CAL5 are two references to the **same unresolved donor slot**, not two independent claims. This is fictional-design provenance, not an independently verified real-language loan.
- No new comparative `(to-verify)` claim is introduced. This review applies the supplied corpus as the assigned standard; it does not authenticate its underlying bibliography or certify real-world universals.
- Only this review was written. The component, corpus, sibling components, gates, fixtures and `LOG.md` were not edited; the assignment's named-file-only write boundary takes precedence over the general log-update convention.
- Return the component to its author/integrator for surgical resolution and unchanged-gate rechecks. The complete cross-component contract, donor language and canon acceptance remain outside this review.
