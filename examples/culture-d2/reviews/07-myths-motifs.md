# Review — component 07-myths-motifs (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/07-myths-motifs.yml`
- revision pinned: sha256 `fe4426002890e18e876b826aeb50d98da28839f0fad103ad15a217a92ef11bae`,
  618 lines, mtime 2026-10-17 11:36:46 -03 — stable for 2+ minutes before the read
- status: **FINDINGS** (not clean; 1 blocking cross-file item, 5 corpus-cited items, 3 minor)
- canon: not canonized (D2 design drill)

Revision note: the component was rewritten three times while this review ran
(47 KB at 11:31 → 11.7 KB at 11:34 → 48.9 KB at 11:36). This review audits the
pinned revision only. If the file is revised again, re-run this review.

## Violations

Format: `component | violation | source that forbids it`. Sources marked
`[round contract]` are the round's own binding file (01-brief.yml), not corpus;
corpus paths are given wherever the corpus is the binding source.

- `07-myths-motifs | duplicated role ledger diverges from 06-pantheon on the oath role: this file marks storm-law-oath ASSIGNED + exclusive:true [Kahatu], while 06-pantheon marks oath-enforcement SHARED [Kahatu] (with a separate storm-petition row carrying the exclusive marker) — two coverage claims now exist for one culture | corpus/knowledge/verification/myth-consistency-gate.md §2 (one role ledger per review unit: dependency, agent, status, uncertainty) and §3 (status marks need a reason and their scope; overlapping jurisdictions must be scoped and must predict how a disputed invocation is handled)`
- `07-myths-motifs | role-ledger divergence, sky row: sky-axis-holding marked ASSIGNED [Halatu] here, while 06-pantheon marks sky-and-stars NON-DIVINE [] (Halatu formula-only, no cult, no patron) and vertical-axis SHARED [Kalweha, Humweha] | corpus/knowledge/verification/myth-consistency-gate.md §3 (status mark + reason + scope; ASSIGNED and NON-DIVINE are different coverage claims)` — cross-ref: 06-pantheon.yml, sha256 `ef0ebf64f787d04730b6a22c7cf9fafb4de0c5e6dae2db223f57cf53de460478`
- `07-myths-motifs | trade-vows-and-strangers: status SHARED with agents [Seratu], but the record's own note assigns jurisdiction to Ula as well ("a market oath invokes Seratu and a road debt invokes Ula"), and 06-pantheon's foreign-trade-vow lists agents [Seratu, Ula] — the agents field contradicts its own jurisdiction note | corpus/knowledge/verification/myth-consistency-gate.md §3 (SHARED requires the jurisdiction record; the agent list is part of the coverage claim)`
- `07-myths-motifs | myth-tier type codes KTD-M0001, KTD-M0002, KTD-M0003 use a KTD-M prefix where the house convention fixes KTD-T#### for lane-internal type ids | corpus/knowledge/myth-symbol/myth-folktale-genres.md §3 (house convention: mint lane-internal type ids `KTD-T####`) and §8 item 8 (index field: a `KTD-T####` lane type id)` — MOT-04's KTD-T0001 conforms; the deviation is declared in-header but is still off-convention
- `07-myths-motifs | MOT-02 carries compound values outside their fields: tier "myth-law carried into legend" and record "MYTH-06 secondary and MYTH-07 etiology" — tiers are the Bascom set, and promotion/demotion belongs in the stratum field | corpus/knowledge/myth-symbol/motif-index-usage.md §5 step 0 (list the tales, tiered myth/legend/folktale per Bascom) and corpus/knowledge/myth-symbol/myth-folktale-genres.md §5 (the `stratum` field carries former form + the event that moved it)`
- `07-myths-motifs | coherence_audit.distortion_log says "near absence of a reward and fate chapter", conflating Q (Rewards and Punishments) and N (Chance and Fate), and contradicting its own reward_economy line, which claims counted-act-rewarded causality (a Q-hot claim) | corpus/knowledge/myth-symbol/motif-index-usage.md §2 (chapter inventory: Q = rewards and punishments; N = chance and fate) and §5 check 3 (Q-heavy = earned moral causality, D/F/N-heavy = luck) with §5's standing rule (distort exactly one axis and log it)` — the intended single distortion is the cold N chapter; the log should say that and only that
- `07-myths-motifs | terminology defect: "memoral" is not a von Sydow slot; the corpus term is "memorate" (MYTH-06 von_sydow line) | corpus/knowledge/myth-symbol/myth-folktale-genres.md §8 item 1 (von Sydow slot: memorate / fabulate)`
- `07-myths-motifs | no `spine_coupling:` declaration anywhere in the file | [round contract] examples/culture-d2/components/01-brief.yml §spine SP-03 (every component file declares spine_coupling naming its two strongest couplings and their record IDs)` — note 05-lexicon implements this; 06-pantheon shares the gap, so this is a round-level item for the integrator as well
- `07-myths-motifs | no per-record `follows:` list: citations sit in the header plus inline basis/frame_tags/index_note prose, while records are required to cite their corpus decision tables in follows | [round contract] examples/culture-d2/components/01-brief.yml §contract.rules RG-02 (a record without a follows entry is rejected at review); corpus analogue: corpus/knowledge/verification/myth-consistency-gate.md §4 (record edition + identifier + checked entry + witness for every claimed comparison)` — 06-pantheon's PAN records carry per-record follows; the fix is mechanical
- `07-myths-motifs | minor: lexicon, names and symbols proposal records carry no short id (`id:` absent; symbol refs are descriptive, not id-based) | [round contract] component-file format (every record SHOULD carry a short id) and 01-brief §contract.record_fields (L-/NM-/SYM- ids)` — mitigated: the file declares every L-/NM-/SYM- dependency UNRESOLVED per RG-04, and no id is invented, so assembly only has to mint/track them

## Checked and clean

Each item below was evaluated against the pinned revision; "clean" means the
check was run and no violation was found.

- **Executable gate** — `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/components/07-myths-motifs.yml` → exit 0 (clean: every kernel check evaluated, no finding). Re-run on the pinned revision, not the earlier drafts.
- **Type tags** — MYTH-06's dominant/secondary/ambient claim (emergence + world-parent parting + creation-by-breath) follows creation-myths-taxonomy §11's layering rule (one dominant + one secondary + one ambient) and §10's rule that creation-by-speech rides on other types rather than being an eighth type; the refusal of creation-by-combat is stated with its reason (no dragon-slaying charter, no victor-king) and is consistent with the D2 seed's segmentary society. MYTH-07 (legend) and MYTH-08 (folktale) carry correct Bascom slots, emic genre words (kordul, surak) and truth-claims per myth-folktale-genres §1; the Rank/Raglan hero-birth cluster is declined by provenance, with the exposure legend correctly deferred to 06-pantheon's Ula material (§6 inverse direction).
- **Charter logic** — each narrative carries the §4 four-part audit (who repeats, to whom, on what occasion, to make whom do what); MYTH-08 is explicitly tagged "not a charter", matching §4's calibration that not every myth charters; the first-step claim is tagged vestigial (institutional drift is data, per §4); charter is used as a use, not an origin theory (calibration section states this).
- **Record-field checklist** — myth-folktale-genres §8's 13 fields are present on MYTH-06/07/08, including canon_status on all three and stratum with in-world moving events per §5; index hygiene follows motif-index-usage §7 (no minted ATU numbers; MYTH-08 claims only a chapter range with Uther 2004 named, no type number, plus a KTD-T id).
- **Coherence audit** — §5's five checks are all present; negative evidence is converted into a belief (the cold captive/flight letters), tabu symmetry maps each tale tabu to a rule, contact fingerprints read borrowing-without-climate, orphan-motif families are seeded per §6, and exactly one deliberate distortion is logged (the wording defect is item V6 above).
- **Pantheon internal consistency (repaired)** — the earlier drafts carried a seven-agent pantheon (Túlan, Ímrak, Kérum, Sálin, Húna, Hélam, Ántuk) that contradicted 06-pantheon on names, the cosmic-origins policy and the star-calendar role. The pinned revision replaces it with a reference view by PAN id and name (Halatu, Kahatu, Humweha, Kalweha, Seratu, Suweha, Ula), defers to 06 for any rename or role change, and files reconciliation findings RC-1..RC-4. RC-1 verified (06 carries MYTH-01..05; this file adds MYTH-06..08 without renumbering). RC-2 verified as a real sibling tension: 06's PAN-03 carries the last breath below (Still Camp) while 05-lexicon reads the upper breath and the upslope wind as carrying the soul upward — correctly flagged, not silently resolved. RC-4 verified: 09-eras-calendar fixes CAL-GATE-5 "the turn-gate" opened by SKY-03 "the turning wind". Only the role-ledger status divergences (V1–V3) remain open.
- **Era tags** — E0/E1/E2 used with the contract's fixed meanings, era names/dates deferred to 09-eras; no redefinition of a fixed tag remains.
- **Spine axis tags** — 26 `axis:` fields across roles, lexicon, names, symbols, motifs and myth records; no neutral record lacks a coupling rationale where neutral was claimed.
- **D1 guards** — no river/flood agency; oaths are spoken and smoke-tested, never knotted (RG-01); the tally-cord is a record device, not a cosmological figure; script arrives late; the end-shape is the Unturned Year, not an inundation (D1B-01/02, seed SEED-08).
- **Canon hygiene** — canon boundary present; all items that could not be checked are marked `to-verify`; the handoff defers canon and world-truth to lore-shokunin (worldbible-integration-contract §3, §6, §8).

## HOLD — what would resolve the open items

1. **Role ledger (V1–V3):** either delete 07's roles block and reference 06's rows by ID (RG-03), or re-mark the three divergent rows to match 06 exactly. Until then, the packet carries two coverage claims for one culture and the gate's §2 review unit is ambiguous.
2. **Per-record ids (V9):** assembly mints or tracks the L-/NM-/SYM- dependencies per RG-04; no invention at assembly time.
3. **KTD-M codes (V4):** either rename to KTD-T#### or mint the KTD-M extension corpus-side in myth-folktale-genres §3 so the convention and the component agree.
4. **Re-review trigger:** any further revision of the component changes the digest this review pins.

## Evidence

- Chunk reads (≤80-line windows) of `07-myths-motifs.yml` (all 618 lines, three passes),
  `06-pantheon.yml` (pantheon, roles, history, RIT-, MYTH- blocks),
  `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md` (all 135 lines),
  `myth-folktale-genres.md` §3, §4, §5, §8,
  `motif-index-usage.md` §2, §5, §6, §7,
  `pantheon-archetypes.md` §5, §6, §7,
  `corpus/knowledge/verification/myth-consistency-gate.md` §1–§6.
- Commands: `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/components/07-myths-motifs.yml` → exit 0;
  `sha256sum` of 07/06/09 as pinned above; `grep -c 'axis:'` → 26; `grep -c 'spine_coupling'` → 0;
  `grep -n 'KTD-'` → 3× KTD-M + KTD-T0001 (one house-conformant).
- Cross-check, not edit: 06-pantheon.yml and 09-eras-calendar.yml were read only. This worker
  edited no component or corpus file; the write scope is this review file.

## Canon boundary

Review findings only. Which variant is sacred in-world, who may say it, and whether the
gods were human remain lore-shokunin's decisions; nothing here resolves them, and nothing
here is canon (D2 design drill).