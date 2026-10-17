# Review — component 06-pantheon (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/06-pantheon.yml`
- reviewed revision: **510 lines, sha256 `ef0ebf64f787d04730b6a22c7cf9fafb4de0c5e6dae2db223f57cf53de460478`**
  (mtime 2026-10-17 14:37:46Z)
- review window: 14:33–14:39Z; the writer was still finalizing during the read
  (file moved 494 → 507 → 510 lines), so findings 1–6 and every CLEAN item were
  re-verified against this final revision at 14:38Z. The writer's LOG.md
  round-3 digest (`5c5fbe71…`) belongs to the intermediate 507-line revision —
  recompute at assembly before pinning.
- status: **FINDINGS** — 6 defects, all minor/repairable; no FAIL-class violation
  in the three assigned checks (role coverage, no real-pantheon renaming, era
  consistency), which all pass
- canon: not canonized (D2 design drill) — review is of a non-canon sample
- scope: assigned checks plus citation resolvability, which the finding format
  itself requires. No component or corpus file was edited.

## Violations

Format: `component-id | violation | corpus path:section that forbids it`

1. 06-pantheon | PF-33 and PF-34 cite `corpus/knowledge/synthesis/comparative-frameworks.md` §1/§7 — **no such file**. The cited content exists at `corpus/knowledge/myth-symbol/comparative-frameworks.md` §1 (emic/etic rule + Bascom partition, verified) and §7 (falsifiability habit, verified); the file's narratives were re-prefixed to `PAN-MYTH-*` in the final revision (OQ-P06), so PAN-MYTH-01 and PAN-MYTH-05 inherit the dead path through PF-33/PF-34; repair: fix the directory in the two cites | corpus/QUALITY.md §1 (every claim carries a cited, checkable source); 01-brief RG-08 (corpus paths are the citations)
2. 06-pantheon | PF-37 cites `corpus/knowledge/synthesis/symbolism-synthesis-method.md` §5 — **no such file**. R1/R3/R5 live at `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md` §5 (verified, lines 90–96); repair: fix the path | corpus/QUALITY.md §1; 01-brief RG-08
3. 06-pantheon | PH-01…PH-05 (`pantheon_history`) carry no `follows:` entry although each is an id-carrying design choice; repair: cite `corpus/knowledge/myth-symbol/pantheon-archetypes.md` §5 ("Gods have careers") and §7 step 10 | 01-brief RG-02 ("a record without a follows entry is rejected at review"); corpus/QUALITY.md §1
4. 06-pantheon | The `theonym_pipeline` rule records TP-01…TP-03 carry no per-record `evidence` status (contract record pattern), and TP-01 asserts "matching the M- record for compounding" while `03-morphosyntax.yml` contains **no** compounding record (M-/SYN- scan: zero hits) and the same file's suffix notes call the M- record "pending" — the match is asserted, not recorded UNRESOLVED; repair: mark the dependency UNRESOLVED per RG-04 or cite an existing order/compounding table | 01-brief record_fields ("every component record additionally carries `id`, `axis`, and `evidence`"); RG-03, RG-04; corpus/QUALITY.md §1
5. 06-pantheon | `roles:` row `mortality-breath` is marked ASSIGNED with no reason or scope; repair: one scope line (sole keeper, breath-souls counted, no substitute) | corpus/knowledge/verification/myth-consistency-gate.md §3 ("Mark each relevant role …; give the reason and its scope")
6. 06-pantheon | status token `EXPLICITLY-UNEXPLAINED` deviates from the gate's fixed mark `EXPLICITLY UNEXPLAINED`; repair: use the gate string (or declare the alias) so the assembly parses the mark by exact token | corpus/knowledge/verification/myth-consistency-gate.md §3

## Checked and CLEAN

**Role coverage** (myth-consistency-gate.md §3; pantheon-archetypes.md §2, §5, §7; 01-brief A-05)

- 15 role rows; all six gate prompt rows covered (subsistence/weather, authority/oath, mortality, reproduction, craft/exchange/travel, cosmic origins); all 7 PAN- agents carry `name, role, domain, era, axis, evidence` (A-05 satisfied).
- Deliberate blanks (creator, sun, moon, love, separate war, smith, devil) exceed the §7 20–40% band, which is admissible: gate §1 says numerical quotas are design hypotheses, not gate requirements.
- MC-P01 not triggered (exclusive agents are assigned, substitutes denied, invocations scoped); MC-P02 avoided (reproduction-care marked UNKNOWN as a knowledge gap, not absent); overlapping jurisdictions scoped with a dispute path ("a disputed invocation goes to the pass rite first"); MC-P03-style exception recorded for foreign-trade-vow.
- Ritual-address test (§5): PAN-02/03/04/05 pass fully; PAN-01 fails on purpose and is demoted to story — the rule's own alternative; PAN-06 is a tale figure bound to an institution, not claimed as a god; PAN-07 has a market address, a festival day, and a live refusal, and gate §3 forbids requiring a fixed epithet count.
- War theology tracks the army type ("no standing army; a raid is filed as a debt claim"); love/war configuration and its blanks are explicit (§2 cluster notes); gender is parameterized with an anti-uniformity note and teller-dependent gender for the trickster (§5).

**No real-pantheon renaming** (SKILL.md decision table "never paste a real-world pantheon with renamed gods"; pantheon-archetypes.md §3, §5; real-world-inspiration-boundaries.md §3, §5)

- All 7 theonyms derive from the file's own working roots (hala/kaha/huma/kala/sera/weha/su-) with stated derivations; a scan for real theonyms (Zeus, Dyaus/Dyēus, Indra, Perun, Þórr, Baal, Marduk, Osiris, Yama, Óðinn, Amaterasu, Inanna, Aphrodite, Ares, Mars, Hades, Hel, Loki, Prometheus, Māui, Raven, Coyote) returns zero record-text hits.
- No real story survives beat-for-beat (the §5 "residue test"): no serpent/dragon, no flood, no dying-rising god; the succession is a seat handover dated to a charter, not Uranus–Cronus–Zeus; the exposure legend is marked a legitimation device.
- Contact is in-world interpretatio, not translation: the lowland partner's mapping gives Seratu gates/keys/receipts he never had, and the distortions are kept as contact evidence (§5).

**Era consistency** (myth-consistency-gate.md §5; era-myth-language-costume-matrix.md §1; 01-brief CP-07, contract.era_tags; D2 seed)

- Tags stay inside the contract's fixed space E0–E3 (only E0–E2 used) and match its definitions: E0 pre-script/knot era, E1 script-arrival seam, E2 literate anchor.
- Seed honoured: the lowland script arrives late by adaptation (Ula, E1; market scribes and written receipts), tally-knots remain the pre-script record; no D1 import (river/water/flood terms appear only as an explicit guard; "knot" only as RG-01 counting geometry — verified by grep, matches the writer's self-scan).
- Careers and layers are dated (demotion E1, rise E1, deified human E1 person/E2 cult, foreign equation E1–E2, schism E2); attestation vs origin kept apart ("attested from E1", "E0 formula; demoted by the E1 charter").
- Gate run reproduced by this reviewer: `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/components/06-pantheon.yml` → exit 1, exactly one finding `MC-S00: no symbol ledger` — matches the writer's V-P01; the disposition (symbols[] is owned by the symbols component, assembled at packet level) is accepted. No other finding: the P/M/E checks evaluated clean.
- Freeze digest: LOG.md's round-3 entry records `5c5fbe71…` for the intermediate 507-line revision, and the writer then revised the file again (510 lines, `ef0ebf64…`) without a matching LOG update — the digest no longer pins the delivered bytes; recompute at assembly (contract freeze rule), and the writer/integrator should refresh the LOG record.

## Escalations verified (not this file's defects)

- Era-tag conflict (OQ-P02) is real and broader than stated: `08-symbols.yml` dates in E1–E4, and `09-eras-calendar.yml` delivers E0–E5 and itself asks for renumbering (line 515), while the contract fixes E0–E3 with an alias rule. Integrator's call (also 01-brief OQ-05); the final revision's OQ-P02 text now records the era component's E0–E5 as well — verified accurate.
- Component numbering (OQ-P01) verified: 01-brief registry `C-05 = 05-pantheon` / `C-06 = 06-symbols`, dispatch names 06-pantheon. Integrator's call.
- MYTH- namespace collision (OQ-P06) verified: `07-myths-motifs.yml` occupies `MYTH-01`, `MYTH-04`…`MYTH-08`; this file re-prefixed its narratives to `PAN-MYTH-01`…`PAN-MYTH-05` in the final revision and requests aliasing/dedup at assembly. Integrator's call.
- Writer's V-P03 claim (delivered symbols block yields MC-S00 under-normalized keys) is a symbols-component issue; it belongs in 08's review, not counted here.

## Observations (not violations)

- `roles:` ledger rows and `deliberate_blanks` rows carry no `follows:`/ids; read as ledger rows rather than design-choice records, so not counted — the assembly may still want the coverage ledger's disputed rows (war-raiding merged, cosmic-origins NON-DIVINE) to cite gate §3.
- PAN-02/PAN-04 name two festivals (pass-opening dawn, milk-first rite) with no RIT- record; A-05's minimum (≥2 RIT-) is met and no rule requires a record per festival, but the calendar coupling would be tighter with RIT- or dated festival references at assembly.
- Recheck trigger: this review pins revision `ef0ebf64…` (510 lines, 14:37:46Z); if the writer revises again after 14:39Z, re-verify findings 1–6 against the new revision before assembly; the era-tag reconciliation (OQ-P02) also re-triggers the §5 "changes propagate" pass over theonyms, epithets and calendar references.