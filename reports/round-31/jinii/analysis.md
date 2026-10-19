# R31-D12 — jin'i-ryu candidate analysis: which self-improvement move does the telemetry actually mandate?

- **Round:** 31 (operator regimen close-out; loop 3, GLM round 1 of 2, 16w zai glm-5.3-flash MAX)
- **Assignment:** R31-D12..D13 — select ONE falsifiable self-improvement move to the lane's own
  operating files from regimen telemetry; draft it with its falsification condition
  (companion: `reports/round-31/jinii/draft.md`).
- **Date:** 2026-10-18 · **Baseline revision:** `71cd9d376ebd144e94e4f12d997f73e5d2839aa9`
  (declaration commit per `reports/round-31/claims.json`); lane HEAD at analysis time
  `e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c`.
- **Status:** analysis only. The patch itself is a DRAFT for the orchestrator; nothing outside
  `reports/round-31/jinii/` was written, and no filed round 8-30 artifact was modified.

## 1. Method

Read the regimen telemetry end to end, extract the recurring defect classes, score each
candidate move on (a) recurrence count in filed artifacts, (b) demonstrated downstream cost,
(c) whether a partial fix already landed (delta size), (d) crispness of a falsifiable
condition. Sources: `reports/round-{19,25,26,27,28}/availability.json`,
`reports/round-29/devin-availability-disposition.md`, `reports/round-29/defects/ledger.json`,
`reports/round-30/routed-resolution.json`, `LOG.md` (rounds 8-30 admissions), the current
`AGENTS.md` and `SKILL.md`, `PROVINCE.md`.

## 2. The telemetry census — what the availability records actually say

Canonical audit (command recorded per the counts-carry-command rule; run 2026-10-18T22:39:21Z,
from the lane root):

```
python3 -c "import json,glob,os
for f in sorted(glob.glob('reports/round-*/availability*.json')):
    d=json.load(open(f)); parts=f.split('/')
    v=os.path.join('reports',parts[1],'validation.json')
    print(f'{f} | state: {d.get(\"state\")} | completed_workers: {d.get(\"completed_workers\")} | validation_landed: {os.path.exists(v)}')"
```

Observed output:

```
reports/round-10/availability-attempt-1.json | state: None | completed_workers: 0 | validation_landed: True
reports/round-10/availability-attempt-2.json | state: None | completed_workers: 0 | validation_landed: True
reports/round-10/availability-attempt-3.json | state: None | completed_workers: 0 | validation_landed: True
reports/round-19/availability.json | state: open-at-seat-close | completed_workers: None | validation_landed: True
reports/round-25/availability.json | state: open-at-seat-close | completed_workers: None | validation_landed: True
reports/round-26/availability.json | state: open-at-seat-close | completed_workers: None | validation_landed: True
reports/round-27/availability.json | state: open-at-seat-close | completed_workers: None | validation_landed: True
reports/round-28/availability.json | state: open-at-seat-close | completed_workers: None | validation_landed: True
reports/round-5/availability-attempt-1.json | state: None | completed_workers: 0 | validation_landed: True
```

Reading, with evidence:

1. **Five of five modern availability records are permanently unfinished.** r19, r25, r26,
   r27, r28 all carry `"state": "open-at-seat-close"`, `completed_workers: null`
   (r19:16, r25:54, r26:42, r27:49, r28:63), and a `finalization_note` that delegates the
   close-out: "Fields left open for the integrating parent: … Fill them from that artifact
   when it lands" (r19:25, r25:256; the r27:275 and r28:423 notes leave the fields null and
   report the receipt landing). Every referenced `validation.json` HAS landed and every round
   was admitted to `LOG.md` — yet no closing snapshot exists anywhere in the repo. The
   declared finalization protocol was declared 5/5 times and executed 0/5 times.
2. **The cost is already on the books as a could-not-evaluate verdict.** The r25-r28
   `completion_measurement.instrument` fields point at `.scratch/x41/sample.py`,
   `.scratch/x59/sample.py`, `.scratch/x53/sample.py`, `.scratch/x53-r28/sample.py`; the
   samples were never landed and `.scratch` is cleaned between rounds, so the r29 verify seat
   could not check the devin route's completion numbers and filed
   `reports/round-29/devin-availability-disposition.md` as a documented could-not-evaluate,
   naming the cause class "process defect (telemetry not persisted to the round repo)"
   (disposition ¶5-7, ¶16-17).
3. **The restate hazard has already fired once.** The same disposition asserts the four
   records are "each carrying the route, requested/completed workers, and wall time" and cites
   "completed in {26, 24, 24, 24}" (`devin-availability-disposition.md:12-14`). No availability
   record contains those numbers — all four say `completed_workers: null`. The set matches the
   `LOG.md` admission lines instead (26/64 at LOG:3365; 24/64 at LOG:3378, 3391, 3401). A
   verify seat cited counts "from the records" that the records do not contain, and with no
   closing snapshot there is no durable artifact to arbitrate what the records do say.
4. **The landed fix covers only the write-time half.** `AGENTS.md` §Availability and dispatch
   telemetry (:15-30, landed round 30) requires persistence under
   `reports/round-<N>/telemetry/` "never only `.scratch`", nulls with owner+reason, and
   summaries that cite durable samples. It says nothing about closing a record that was filed
   open once the round's receipt lands. The rule as landed cannot heal — or even detect — the
   5/5 open-record population; item 3 above is what its absence looks like in practice.
5. **The legacy rows corroborate the failure mode this rule class exists for.** The r5/r10
   attempt files carry `completed_workers: 0` — an inferred zero, exactly what the current
   rule forbids ("Unknown counters stay `null` … not inferred zeroes"). They are historical,
   append-only, and out of scope for correction; they are evidence of what happens when no
   rule binds the field.

## 3. The candidate moves, scored

**M1 — Telemetry finalization-closure rule (generalize the r30 persistence rule with the
close-out half).** Recurrence: 5/5 standing records open past close (§2.1). Downstream cost:
one filed could-not-evaluate verdict (§2.2) plus one demonstrated mischaracterization of the
durable bytes (§2.3). Partial fix already landed: yes — AGENTS.md persistence rule, so the
delta is one missing half of an existing rule. Falsifiability: crisp — a countable audit
command whose non-empty output after a round's admission is the falsifier.
**Verdict: selected.**

**M2 — "Freeze follows re-point" pin discipline.** Recurrence: the re-pin cascade recurs
across rounds (r17 D "failed as declared" → generalization + re-pin cascade routed to r18,
LOG:3235; r20 "repin cascade as new rows"; r26 "re-pinned through the r5 chain, pin-repoint
checker 17/17"; r27/r28 D4 pin sweeps). Live open instance:
`reports/round-30/routed-resolution.json` R30-QREG-DANGLES `limits`: "V3 selftest now passes,
but its default frozen read-set is superseded and still needs a new durable baseline and
default-pointer integration." Rejected because: the routed-resolution discipline ("Routed-item
closure is not inferred", r14 onward) already forces an explicit item-to-disposition map with
named owners, and r30's limits text already names this follow-up — a same-round-integration
mandate would largely restate the existing discipline, and its falsification condition is
fuzzier (a named routed owner with a round number is already legal closure). Strong second;
kept on the shelf for a later promotion tier.

**M3 — TMPDIR mirror-safety promoted to a SKILL.md checklist item.** Current state: prose at
`SKILL.md:456-457` ("Run scratch-writing tools only after `export TMPDIR=$PWD/.scratch`; a
mirror-safety leg that rejects an in-repo temporary directory requires its own [outside-root
TMPDIR]") plus the measured control at `SKILL.md:294` (`mirror_unsafe` exit 2, r24 cold run,
2026-10-18). Rejected because: the telemetry shows zero recurrence of an actual
mirror-corruption incident — the `mirror_unsafe` exit is a designed control that worked, not
a defect that recurred. Promotion is cheap but the evidence does not mandate it; this round
should spend the single jin'i-ryu move where the defect class demonstrably recurred.

**M4 (considered, eliminated early) — receipt-clobber discipline.** Rounds 8+9 filed
`validation.json` were clobbered by validator re-runs (LOG:3040); the successor guard
`tools/harness/receipt_guard.py` landed round 14 with exit-3 refusal + `REFRESH_RECEIPTS=1`
escape hatch and a selftest (LOG:3144-3159). Two occurrences, mitigation landed and verified,
no recurrence since r14 — nothing left to codify.

## 4. Selection rationale (M1)

- Highest recurrence: the only candidate whose failure class is present in 100% of its
  applicable population (5/5 open records, §2.1).
- Demonstrated downstream cost already booked against the lane: one could-not-evaluate
  verdict (r29) and one durable-bytes mischaracterization (§2.2-2.3) — not hypothetical.
- Smallest defensible delta: it completes a rule the lane already adopted in round 30 rather
  than introducing a new regime; PROVINCE.md ownership is untouched, corpus untouched, filed
  rounds 8-30 bytes untouched (corrections are new snapshots — matching the repo's own
  append-only discipline).
- Cleanest falsification condition of the three: a deterministic, re-runnable audit command
  whose output is either empty or is the falsifier — no judgment call in the loop.

## 5. Limits of this analysis

- The r29 disposition's {26,24,24,24} characterization (§2.3) is treated as evidence of the
  restate hazard, not as an accusation: the disposition predates the r30 rule's landing and
  its own verdict is honestly could-not-evaluate. The point is that no closing artifact
  existed to arbitrate, which is exactly the gap M1 closes.
- The completed counts the closing snapshots will carry are derived from `LOG.md` admissions
  (the parent's receipt reading), not from per-seat launch receipts, which no worker seat can
  read; the draft requires each filled field to cite its source so a better durable source
  (if the orchestrator holds one) supersedes it.
- This analysis re-ran no wave and measured no provider; it audits filed bytes only. The
  falsification condition and controls are specified in `reports/round-31/jinii/draft.md` §3-4.
