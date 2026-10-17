# Review — component 08-symbols (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/08-symbols.yml`
- reviewed revision: 512 lines / 60,398 bytes, sha256 `7479dc7d…5f9dee1784`
  (full digest: `7479dc7df321bb3ef12e35ab229b4921923f52f18923b09c176b7d5f9dee1784`),
  mtime 2026-10-17 11:31:59 -03; digest re-verified unchanged at write time
- status: **REVIEWED — 6 findings, all label/table-completeness level; no
  meaning, domain, or era-assignment error found; none of the three assigned
  checks fails**
- canon: not canonized (D2 design drill)
- corpus read: `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
  (169 lines, full, ≤80-line windows); cross-cite spot-checks in
  `myth-symbol/color-symbolism.md` §4, §5, §12 (component's §4/§5/§12 cites
  verified and hold)

## Verdict on the three assigned checks

1. **One-domain-per-symbol — CLEAN.** Ten registered signs (S1–S10) carry ten
   distinct primary-domain ids (STORM-LAW, HERD-YIELD, ABSENCE-COUNTED,
   LEDGER-BURDEN, SOUL-BREATH, HIDDEN-SPEECH, ACCOUNT-CLOSURE, AXIS-UNMOVING,
   SEASONAL-OPEN, LIMINAL-PASS) — no collision across signs or registers
   (method §5 R1). Satellites per sign are ≤3 (max = 3 at S1, S3, S4, S5, S7,
   S10). The one R5 hazard — two whites — is found and repaired inside the
   artifact: CL-1 splits fleece-white (HERD-YIELD, lines 95–118) from
   ridge-grey (ABSENCE-COUNTED, lines 119–143) and declares the contrast axis
   (grease-soft fleece vs rain-bleached rock). Contrasts are also declared for
   the colour triad (S1/S2/S3) and the lead-animal riddle (S4 vs lead-ewe).
2. **Era scoping — PASS with findings V1–V3 (table/log completeness only).**
   Every sign carries an era string; all drifts are forward-stamped; no
   retro-projection found (law_2's three assertions survive spot-check: E2
   slate does not explain E1 bog-dark; the script-era bill is not read back
   into E1 cords; the E4 script does not retro-explain the E1+ oath grammar).
   T1–T5 carry mechanism/old/new/interval/agents/dissent/residues. Findings:
   the transition table is not complete over the drifts the records tag (V1),
   one mechanism tag is unsupported and one is double-labelled (V2), and the
   drift-law-3 neighbour audit is logged for T1 only (V3).
3. **Unaligned gap deliberate — CLEAN.** The single UNALIGNED cell
   (SHELTERWARD/celestial) carries a reason, an in-world doctrine, and a
   structural consequence (star-delayed disputes wait for the next ascent) —
   exactly the §3 step 4 "preserve the lump" behaviour; §5 R2 satisfied. CL-3
   documents that a draft "hearth star" fill was removed, so the gap is
   deliberate, not a silent hole. The gate's colour cell is a PATTERN entry,
   explicitly declared "not an UNALIGNED cell" and grounded in
   color-symbolism §5 ("Pattern is not hue… the second, older channel") —
   verified, a legitimate fill rather than a smuggled second gap. All 20
   matrix cells are addressed (19 values + 1 reasoned UNALIGNED).

## Violations

Format: `component-id | violation | corpus path:section that forbids it`.

- 08-symbols | era_transition_table (T1–T5) omits mechanism-tagged drifts that
  the sign records themselves date: S2's E4 "white-measure" satellite (line
  98, M5), S9's E4 doctrine split (line 275, M2/M5), S10's E2 and E4 changes
  (line 300, M1/M5 and M3); drift law 1 makes the era table the artifact, and
  these changes live only in the sign records | `myth-symbol/symbolism-synthesis-method.md`
  §6 drift law 1 ("the era table is the artifact") + §7 checklist line 11
- 08-symbols | S9 tags its E4 drift "M2/M5" (line 275) but no
  conquest/revolution is staged — the described change (donor calendar names
  arriving with the script) is contact M5, at most media M3; separately, S5's
  record tags the same drift "M3/M5" (line 173) where T4 tags it M5 — one
  drift, two mechanism labels | `myth-symbol/symbolism-synthesis-method.md`
  §6 M2 row (political/religious overwrite = conquest or revolution re-keys
  symbols) + drift law 1
- 08-symbols | drift law 3 neighbour audit is logged for T1 only (law_3, line
  377); T2 (DOWNWARD/colour) and T5 (THE-GATE/animal) are slot re-keys and
  carry no neighbour-audit log, nor do the sign-level drifts in finding V1;
  audit drift_13 (line 478) marks PASS citing T1 alone |
  `myth-symbol/symbolism-synthesis-method.md` §6 drift law 3 + §7 checklist
  line 13
- 08-symbols | the two "ritual inversion" satellites (S3, S10) never name the
  polarity axis the inversion runs on — only the audit asserts it
  (coherence_5, line 470, claims "name AX-1/AX-2"); the records cite no AX-id |
  `myth-symbol/symbolism-synthesis-method.md` §5 R6 (inversion needs its axis
  named) + §5 R3 operator "inversion on a named polarity"
- 08-symbols | S6 satellite operator "insult register" is not one of R3's
  seven licensed transformations; the reading is documented but its derivation
  has no licensed operator (nearest: metaphor along a declared axis) |
  `myth-symbol/symbolism-synthesis-method.md` §5 R3
- 08-symbols | S8 satellite 2 is a borrowing whose donor is self-marked
  UNKNOWN and which carries no adoption era; audit drift_14 (line 479)
  nevertheless claims "every loan carries its donor … and adoption era" |
  `myth-symbol/symbolism-synthesis-method.md` §5 R3 (borrowing = donor + era)

## Checks run (detail)

- **Inventory/format**: `component:` + `culture: D2` header, `canon: not
  canonized (D2 design drill)`, status/rev/spine/spine_boundary present; ten
  symbols[] records each with sign, register, era, audience, domain (id,
  definition, includes, excludes, contrasts), ground, carrier, satellites,
  couples, follows, notes; every record id-carrying (S1–S10, AX-1–3, E1–E4,
  T1–T5, CL-1–5, V1–V10, CR-1, LAW-1, TAB-1, PRV-1, TIN-1).
- **R3 operator census**: metonymy ×5, synecdoche ×1, metaphor (AX-n) ×3,
  event-index ×4, borrowing ×6, taboo substitution ×4 — all within R3's set
  except the two denominations in findings V4–V5; homophone rebus deliberately
  not used (pitch-accent expense, PENDING 01/02) with the single household
  oath marked (to-verify).
- **R4 grounding quota**: 9 of 10 signs indexical/institutional, 1
  anomaly-ground (S6) — §3/§5 R4 floor (≥1/3) cleared.
- **R7 productivity**: four compounds minuted (three + one deliberate refusal),
  with competing readings and reader groups.
- **§7 line 17 (language coupling)**: self-marked PARTIAL/PENDING against
  01/02/03 — a declared dependency under the fleet's PENDING-interface
  convention, not counted as a violation here.
- **Cross-cites verified** (spot): color-symbolism §4 "white is usually
  undone" (S2 ground) ✓; §5 pattern channel (gate cell) and dualism modes
  (S1's Mode A/B; V2's ban) ✓;
  §12 step 6 enforcement artifacts (LAW-1, TAB-1, PRV-1, TIN-1 — all four
  present) ✓.

## Notes (not violations)

- Spine coupling is explicit and D1-free: verticality in the frame, the
  soul-carrier, the anomaly, and the counting direction; wind in the oath
  witness, the two witnesses, the storm colour, and PRV-1; scan found no
  river/water/binding record (CL-4 shows the binding draft was excised).
- law_4's E3 fossil is listed as "the exactness dissent in the count" — an
  event rather than a dead meaning surviving as idiom; T2's "grey verbs in the
  descent count" residue is the actual fossil. Rename only; no meaning at stake.
- PENDING interfaces use the contract key names
  (`06.costumes[].*`, `07.pantheon[].*`, `03.lexicon[].*`, `phonology.tones`)
  and assert no other component's content — worker rule respected.
- The component's own audit ends "READY-FOR-REVIEW"; that remains fair to the
  content — findings V1–V6 are reachable by label/table edits only, no design
  change.
- No LOG.md entry was written by this worker (review write scope = this named
  file only), consistent with the sibling review precedent
  (`03-morphosyntax.md`); the parent/integrator should log the delivery.