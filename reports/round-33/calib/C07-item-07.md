- Seat: C07 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C07 — open item 7 disposition

## Mission and dependency status

Mission (per `reports/round-33/targets.json`, seat C07): "Same as C01 for item 7."
C01's mission: "Disposition open item 1 from K03's canonical table: verify its
status quo at HEAD (pointer still accurate, dated command), classify
fixable-now vs carried, and produce the disposition with evidence; if fixable,
add the exact fix draft to your fragment."

**K03's canonical table is not landed at this seat's cut** — `reports/round-33/calib/`
was empty (ls, 2026-10-19; sibling seats run in the same batch). Item-7 identity is
therefore ordering-dependent. Evidence for the primary mapping:

- `reports/round-32/dossier-d13-operator-decisions.md:130-138` is the Decision-4
  table, 9 rows in fixed file order; K03's mission names that table **first**
  (`targets.json` K03: "Canonicalize THE twelve standing open items from
  reports/round-32/dossier-d13-operator-decisions.md (Decision 4 table) plus … D11").
- In that table, row 7 (1-indexed) is `dossier-d13-operator-decisions.md:136`:
  `| calibrated numeric rubric undefined | r5 | SCORECARD.md header |`.

So the **primary** disposition below is the rubric item, under the hypothesis
that K03's row order follows the D13 table. Two contingency mappings are also
dispositioned so the integrator can slot whichever K03 files: if K03 orders by
origin round, item 7 falls in the cold-run cluster (N4, r24); if K03 expands the
cold-run row into N1/N4/N5/N7, item 7 is plausibly the devin could-not-evaluate
row (`:137`). All three are covered.

## Primary: item 7 = calibrated numeric rubric undefined (origin r5)

### Status quo at HEAD — re-verified 2026-10-19 at `139e3b6`

HEAD `139e3b662900557afe54f632b468619593dc9fcb` equals the declared baseline
(`git rev-parse HEAD`; `reports/round-33/claims.json` baseline_commit). Commands
run this date, in-tree:

```sh
grep -n "protocol-conformance gap" SCORECARD.md
# 14:numeric rubric remains an explicit protocol-conformance gap. Freshness is
# (the gap sentence wraps from :13 "defining a calibrated" to :14)
grep -n "rubric" corpus/QUALITY.md          # no matches, exit 1
grep -n "Q-05-3" corpus/lessons/README.md
# 163:| Q-05-3 | whole-corpus header conformance and numeric-rubric debts remain explicit | `corpus/QUALITY.md` | open |
grep -rn "rubric" reports/round-2[7-9]/ reports/round-3[0-1]/ | wc -l
# 0   (rounds 27-31 never touched the item)
```

Every pointer still accurate at HEAD:

- `SCORECARD.md:13-14` — the header gap statement stands verbatim.
- `SCORECARD.md:624` — the debt is also in the "debts folded into rounds 9-28"
  list ("reproducible numeric axis rubric"); rounds 9-28 did not close it
  (rubric touches in r27-r31 artifacts = 0, above).
- `corpus/lessons/README.md:163` — the standing ledger row still reads `open`;
  `:75` indexes the carrying round-5 lesson with `Q-05-3`.
- `corpus/QUALITY.md` — 23 lines, zero rubric/header matches; the r26 evidence
  command reproduces identically (`reports/round-26/open-questions/C42.md:51-53`).
- `reports/round-5/kotodama.md:54` — "no calibrated numeric rubric is claimed"
  (origin statement, unchanged).
- r32 restatements: `reports/round-32/dossier-d13-operator-decisions.md:136`;
  `reports/round-32/dossier-d12-capability-inventory.md:79-81`.

### Disposition: carried-with-owner+reason+next-touch (not fixable-now)

Not fixable by a lane seat, on two filed grounds: (1) the r26 carry explicitly
refused to paper it over — "deliberately left open rather than papered over with
an invented rubric" (`reports/round-26/open-questions/C42.md:58-60`); (2) a
calibrated rubric is a calibration-standard ruling, which this lane routes to
the operator (r32 D13 decision materials; `reports/round-33/claims.json`
non_goals: "no promotion, canon, clearance, or closure verdicts"). No fix draft
is therefore in scope for C14 from this item.

New fact this seat adds: the r26 row's next-touch was **round 27**, and round 27
never took it (zero rubric touches in r27-r31, command above) — the carry is
overdue and the next touch must be re-declared, not inherited.

### Ledger row (ready for C15; id provisional pending K03)

```json
{
  "id": "OI-07",
  "item": "calibrated numeric rubric undefined (whole-corpus header conformance + numeric-rubric debts remain explicit)",
  "origin": "r5; re-stated r26 Q-05-3; r32 D13 Decision-4 row 7",
  "pointer": "SCORECARD.md:13-14; corpus/lessons/README.md:163; reports/round-32/dossier-d13-operator-decisions.md:136",
  "status_quo_check": "2026-10-19 @ 139e3b6: SCORECARD.md:14 gap stands; corpus/QUALITY.md grep rubric = no matches (exit 1); corpus/lessons/README.md:163 = 'open'; rubric touches r27-r31 = 0",
  "disposition_class": "carried-with-owner+reason+next-touch",
  "evidence": [
    "SCORECARD.md:13-14",
    "SCORECARD.md:624",
    "corpus/lessons/README.md:163",
    "reports/round-5/kotodama.md:54",
    "reports/round-26/open-questions/C42.md:43-60",
    "reports/round-32/dossier-d13-operator-decisions.md:136",
    "reports/round-32/dossier-d12-capability-inventory.md:79-81"
  ],
  "fix_draft": null,
  "owner": "operator (calibration ruling); artifact pointer-owner corpus/QUALITY.md per r26 Q-05-3",
  "reason": "no calibrated rubric exists; inventing one is explicitly refused by the r26 carry; rubric definition is operator-owned calibration, out of lane scope",
  "next_touch": "operator calibration ruling; until issued, re-checked at the next regimen-opening calibration audit (r26's next-touch round 27 was never taken)"
}
```

## Contingency A: item 7 = cold-run N4 (origin r24)

If K03 orders by origin round, item 7 lands in the r24 cold-run cluster.
Status quo re-verified 2026-10-19 at `139e3b6`:

- `reports/round-24/promotion-review.md:186-188` (N4): "no real costume/era
  artifact set and no real handoff packet path is named in the cold-run file
  set; checklist items 3/4 gain declarations, not operands."
- At HEAD the checklist still carries declarations, not operands:
  `SKILL.md:531-532` item 3 = prose gap + gate name only; `SKILL.md:533-534`
  item 4 names `handoff-packet-check` but no packet-path operand.
- `reports/round-32/dossier-d11-shonen-boxes.md:150-153` re-confirms as filed
  ("declarations only"), `:167` and `:207` repeat it.

**Class: fixable-in-part (bounded text draft).** The unclosed part is the
cold-run *file set* itself (its pinning is N7, `promotion-review.md:193-195`),
which no lane seat can close unilaterally. The bounded draft available now
(verified paths only, 2026-10-19):

```text
SKILL.md:531-532 (checklist item 3) — before:
  - [ ] Every costume/era claim couples to a term, a material, and a rule of
        who may wear it — prose gap (machinery: `costume-era-consistency-gate`).
after (append operand):
        who may wear it — prose gap (machinery: `costume-era-consistency-gate`,
        `tools/gates/costume-era-consistency-gate.py <packet.yml>`;
        worked set: `examples/culture-d4/`).
SKILL.md:533-534 (checklist item 4) — after (append operand):
        open questions — `handoff-packet-check` enforces per packet
        (`python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md`);
        no canon here.
```

Verified supporting bytes: `tools/gates/costume-era-consistency-gate.py` exists
and its CLI is documented at `SKILL.md:607`; `examples/culture-d4/` carries the
D4 packet set; `examples/handoff-packet.sample.md` and
`tools/gates/fixtures/handoff-packet-check.{md,expected}` exist (`ls`,
2026-10-19). C14 consolidation owed if this is item 7. `to-verify`: that the
culture-d4 example counts as a "real costume/era artifact set" under r24's
intent — the phrase is not defined in the filed review, so the draft claims an
operand, not closure of N4.

## Contingency B: item 7 = devin availability could-not-evaluate (origin r29)

If K03 expands the cold-run/citation rows, item 7 is plausibly
`dossier-d13-operator-decisions.md:137`. Status quo at HEAD:

- The canonical artifact **exists**: `reports/round-29/devin-availability-disposition.md`
  (`test -s` exit 0, 2026-10-19), dated 2026-10-18 — route
  `devin/deepseek-v4-1-flash-high`, requested 64, completed {26,24,24,24},
  cause class "process defect (telemetry not persisted)", explicitly "a
  documented could-not-evaluate, not a pass".
- **Pointer-accuracy finding:** D13's pointer `reports/round-29/recount/` is
  loose — that directory holds the recount audit (`reports/round-29/recount/audit.md:18`
  covers the availability census), but the disposition record itself is
  `reports/round-29/devin-availability-disposition.md`. For C13/C15.
- The cause was fixed r30: `reports/round-30/fixes/telemetry-convention.md`
  (5353 bytes) + the durable-telemetry rule now in `AGENTS.md:15-31`; the
  convention is live this round (`reports/round-33/telemetry/dispatch-declared.json`).
- What cannot be recovered: the wave-time samples (`.scratch` cleaned) — the
  r29 record says so; per `AGENTS.md:27-31`, missing evidence is recorded, not
  reconstructed.

**Class: carried-with-owner+reason+next-touch** (the samples are unrecoverable;
the durable records stand as partial evidence). Ledger row:

```json
{
  "id": "OI-07",
  "item": "devin availability could-not-evaluate (r25-28 sample-level verification)",
  "origin": "r29 (availability recount)",
  "pointer": "reports/round-29/devin-availability-disposition.md; reports/round-29/recount/audit.md:18",
  "status_quo_check": "2026-10-19 @ 139e3b6: disposition record present (test -s exit 0); durable r25-28 availability.json records present; wave samples unrecoverable by the record's own statement",
  "disposition_class": "carried-with-owner+reason+next-touch",
  "evidence": [
    "reports/round-29/devin-availability-disposition.md",
    "reports/round-29/recount/audit.md:18",
    "reports/round-30/fixes/telemetry-convention.md",
    "AGENTS.md:15-31"
  ],
  "fix_draft": null,
  "owner": "integrating parent (telemetry convention); provider-lane owner for future waves",
  "reason": "wave-time samples were never landed to a durable path and .scratch was cleaned; reconstruction is barred by AGENTS.md; cause fixed r30, evidence gap permanent",
  "next_touch": "next devin-lane round's telemetry record under reports/round-<N>/telemetry/ (convention live as of r33)"
}
```

## Pointer-accuracy findings (for C13/C15)

1. D13's devin pointer (`dossier-d13-operator-decisions.md:137` →
   `reports/round-29/recount/`) resolves to the census, not the disposition
   record; canonical path is `reports/round-29/devin-availability-disposition.md`.
2. Q-05-3's next-touch round 27 was never taken (zero rubric touches in r27-r31)
   — any ledger row reusing the r26 carry must re-declare the next touch.

## Owed

- `reports/round-33/calib/K03-open-items.md` — not landed at this seat's cut;
  final item-7 identity and row id depend on K03's canonical order. This
  fragment dispositions all three plausible item-7 mappings; the integrator
  keeps the primary (rubric) unless K03's table says otherwise.
- `reports/round-33/calib/C15-ledger-draft.json` — insert the matching row
  above (this seat cannot write C15's path).
- `reports/round-33/calib/C14-fix-drafts.md` — only if item 7 is N4
  (Contingency A); consolidation of the two checklist operands.

## Citations

Paths (all read/verified 2026-10-19 at HEAD `139e3b6` unless dated otherwise):
`reports/round-33/targets.json` (C07/C01/K03 seats, shared_rules);
`reports/round-33/claims.json`; `reports/round-32/dossier-d13-operator-decisions.md:130-138`;
`reports/round-32/dossier-d12-capability-inventory.md:79-81`;
`reports/round-32/dossier-d11-shonen-boxes.md:150-153,167,207`;
`reports/round-24/promotion-review.md:178-179,186-188,193-195`;
`reports/round-26/open-questions/C42.md:43-60`;
`reports/round-26/zzz-lessons-index-revision-4.md:229`;
`reports/round-5/kotodama.md:54`; `SCORECARD.md:13-14,444-445,624`;
`corpus/lessons/README.md:75,163`; `corpus/QUALITY.md` (23 lines, no matches);
`SKILL.md:522-534,607,610`; `tools/gates/costume-era-consistency-gate.py`;
`tools/gates/fixtures/costume-era-consistency-gate.{yml,expected}`;
`examples/handoff-packet.sample.md`; `tools/gates/fixtures/handoff-packet-check.{md,expected}`;
`reports/round-29/devin-availability-disposition.md`;
`reports/round-29/recount/audit.md:18`;
`reports/round-30/fixes/telemetry-convention.md`; `AGENTS.md:15-31`;
`reports/round-33/telemetry/dispatch-declared.json`.

Commands (all 2026-10-19, exit 0 unless noted): `git rev-parse HEAD`;
`grep -n "protocol-conformance gap" SCORECARD.md`; `grep -n "rubric" corpus/QUALITY.md`
(no matches, exit 1); `grep -n "Q-05-3" corpus/lessons/README.md`;
`grep -rn "rubric" reports/round-2[7-9]/ reports/round-3[0-1]/ | wc -l` (=0);
`test -s reports/round-29/devin-availability-disposition.md`; `ls tools/gates/`,
`ls examples/`, `ls tools/gates/fixtures/handoff-packet-check.*`.
