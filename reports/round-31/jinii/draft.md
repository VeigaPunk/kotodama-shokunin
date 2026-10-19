# R31-D13 — jin'i-ryu DRAFT: the telemetry finalization-closure rule

- **Round:** 31 · **Date:** 2026-10-18 · **Baseline:** `71cd9d376ebd144e94e4f12d997f73e5d2839aa9`
- **Companion analysis:** `reports/round-31/jinii/analysis.md` (selection rationale §4)
- **Status: DRAFT.** Per the round-31 dispatch rules the orchestrator lands this patch; the
  worker did not and will not modify `AGENTS.md`, `SKILL.md`, `PROVINCE.md`, `LOG.md`, or any
  filed round 8-30 artifact. Everything below is proposed bytes and proposed steps.

## 1. The move, in one sentence

> An availability/dispatch record filed `open-at-seat-close` is not done: once the round's
> `validation.json` lands, the integrating parent files a closing snapshot under that same
> round's `telemetry/` that fills each field the finalization note left open — or closes it as
> `could-not-recover` with an owner and reason — before the round is admitted to `LOG.md`; the
> filed record's bytes are never edited in place, the snapshot is the only correction surface.

This generalizes the round-30 telemetry-persistence rule (`AGENTS.md:15-30`) with the close-out
half it lacks; the analysis shows the missing half is the one that failed 5/5 times (r19,
r25-r28) and already cost the lane one could-not-evaluate verdict plus one durable-bytes
mischaracterization.

## 2. Proposed bytes (exact text for the orchestrator to land)

### 2.1 `AGENTS.md` — append one bullet to "Availability and dispatch telemetry" (after :30)

```markdown
- Close what you open: a record filed `open-at-seat-close` with a finalization note is not
  complete. When the round's `validation.json` lands, the integrating parent files a closing
  snapshot under the same round's `telemetry/` — a new append-only file, never an in-place
  edit of the original record — filling each field the note left open, each filled value
  citing the durable artifact it was read from, or recording `could-not-recover` with an owner
  and reason. A round is not admitted to `LOG.md` while its own availability record still owes
  a closing snapshot. The snapshot names the record it closes and that record's SHA-256 at
  close time, so any later in-place edit is detectable as a digest mismatch.
```

### 2.2 `SKILL.md` — append one item to "## Checklist (executable where a tool exists)" (after :534)

```markdown
- [ ] Every availability/dispatch record filed `open-at-seat-close` whose round's
      `validation.json` has landed carries a closing snapshot in that round's `telemetry/` —
      audit (must print nothing once the round's records are closed):
      `python3 -c "import json,glob,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json'))]"`
      — prose gap recorded in `reports/round-31/jinii/analysis.md` §2 (5 open records with
      landed receipts at 2026-10-18T22:39:21Z); first execution = the r31 retroactive closure.
```

### 2.3 `PROVINCE.md` — unchanged

No ownership or scope change; the rule binds lane-internal telemetry only. Saying so here
because the jin'i-ryu gate names PROVINCE.md as a permitted surface and the explicit
"considered and not needed" record is itself the falsifiable claim.

## 3. The retroactive closure act (first execution, orchestrator)

File five closing snapshots — `reports/round-19/telemetry/availability-close.json` and
`reports/round-{25,26,27,28}/telemetry/availability-close.json` — with this shape:

```json
{
  "round": 25,
  "kind": "availability-close-snapshot",
  "date": "2026-10-18",
  "closes": "reports/round-25/availability.json",
  "closes_sha256": "<sha256 of the closed record's bytes at close time>",
  "state_before": "open-at-seat-close",
  "filled": {
    "completed_workers": {"value": 26, "basis": "LOG.md:3365 admission line (parent receipt reading; no per-seat launch receipt is worker-readable)", "command": "grep -n '26/64 completed' LOG.md", "date": "2026-10-18"},
    "acceptance_verdict": {"value": "accepted", "source": "reports/round-25/validation.json"}
  },
  "could_not_recover": [
    {"field": "completion_measurement raw samples", "reason": ".scratch/x41/sample-60x16.json never landed to a durable path; .scratch cleaned between rounds", "evidence": "reports/round-29/devin-availability-disposition.md"}
  ],
  "append_only_note": "the closed record's bytes are unchanged; this snapshot is the correction surface"
}
```

Per-round filled values (each cites its source; a better durable source supersedes):

| Round | completed_workers | Source (as of 2026-10-18) | Acceptance source |
|---|---|---|---|
| 19 | 17 | `LOG.md:3261` | `reports/round-19/validation.json` |
| 25 | 26 | `LOG.md:3365` | `reports/round-25/validation.json` |
| 26 | 24 | `LOG.md:3378` | `reports/round-26/validation.json` |
| 27 | 24 | `LOG.md:3391` | `reports/round-27/validation.json` |
| 28 | 24 | `LOG.md:3401` | `reports/round-28/validation.json` |

All five carry the shared `could_not_recover` row for their `.scratch` sample instruments
(r25 `.scratch/x41`, r26 `.scratch/x59`, r27 `.scratch/x53`, r28 `.scratch/x53-r28`).
An honest null with owner+reason satisfies the rule; silence does not.

## 4. Falsification condition

**Primary falsifier (the rule fails to bind).** Let the rule land at commit L. For any round N
admitted to `LOG.md` strictly after L: if round N filed an availability record with
`state == "open-at-seat-close"` and round N's `validation.json` exists, then the audit command
(§2.2) run after N's admission must NOT list `reports/round-N/availability.json`.
If it does — an admitted round whose availability record still owes its closing snapshot —
the rule is falsified. The audit output is the whole arbitration: no judgment call.

**Integrity falsifier (the rule is violated as implemented).** If any closing is executed by
editing a filed record in place, the `closes_sha256` recorded in the closing snapshot will
mismatch the record's live digest. One mismatched digest = falsified as implemented, regardless
of whether the fields were filled.

**Explicit non-falsifiers (what the rule does NOT claim):**

1. A record still open while its round's `validation.json` has not landed — the poll window is
   simply not closed yet.
2. The legacy r5/r10 attempt rows (`completed_workers: 0`, pre-rule format) — historical,
   append-only, deliberately not rewritten; their zero-fill is what the current null-discipline
   already forbids going forward.
3. A round that filed no availability record at all — nothing to close.
4. A closing snapshot whose `filled` values carry a named basis that a later, better durable
   source revises — revisions are new snapshots with their own provenance (the AGENTS.md
   correction rule), not falsification.

**Success criterion for the gate.** Before: audit output = 5 rows (measured
2026-10-18T22:39:21Z, `analysis.md` §2). After the retroactive closure: 0 rows. Any post-L
admitted round regenerating a row = falsifier fired. That is the falsifiable delta the
shokunin→jin'i-ryu gate requires.

## 5. Controls (re-runnable; each carries command + date)

1. Census (pre-closure state): the §2.2 audit command — output recorded in `analysis.md` §2,
   run 2026-10-18T22:39:21Z: 5 open records, all with landed receipts.
2. No-numeric-count check: `grep -L 'null' reports/round-{19,25,26,27,28}/availability.json`
   (empty = every modern record still carries honest nulls) — consistent with
   `analysis.md` §2.3, run 2026-10-18.
3. Mischaracterization check: `grep -n 'completed in {26, 24, 24, 24}'
   reports/round-29/devin-availability-disposition.md` vs
   `grep -c '"completed_workers": null' reports/round-2{5,6,7,8}/availability.json` → the
   cited set appears in no record; matches `LOG.md:3365,3378,3391,3401` — run 2026-10-18.
4. Post-landing re-run of control 1 must print nothing (the closure act), and again after each
   subsequent round's admission.

## 6. LOG.md entry text (for the orchestrator to append after landing)

```markdown
## 2026-10-18 — Round 31 jin'i-ryu delta: telemetry finalization-closure rule (D)

- **Move:** the r30 telemetry-persistence rule gains its close-out half — a record filed
  `open-at-seat-close` must gain a closing snapshot under the round's `telemetry/` once the
  round's validation.json lands, before LOG admission; fills cite durable sources, honest
  nulls close as could-not-recover, filed bytes are never edited in place (snapshot records
  closes_sha256 so in-place edits are detectable).
- **Motivation (telemetry):** 5/5 standing availability records (r19, r25-28) declared the
  finalization protocol and 0/5 were executed; the r29 devin disposition cites completed
  counts {26,24,24,24} that appear in none of the four records (all null; they match the LOG
  admission lines), and the lost .scratch samples cost a filed could-not-evaluate.
- **Falsification condition:** post-landing, any admitted round whose open availability
  record has a landed validation.json but no closing snapshot (audit command in
  reports/round-31/jinii/draft.md §2.2); or any closes_sha256 mismatch (in-place edit).
- **Landed:** AGENTS.md telemetry bullet + SKILL.md checklist item + five retroactive closing
  snapshots (r19, r25-28); PROVINCE.md unchanged.
- **Evidence:** reports/round-31/jinii/{analysis,draft}.md; audit pre: 5 rows
  (2026-10-18T22:39:21Z), post: 0 rows.
```

## 7. Landing checklist (orchestrator)

1. Apply §2.1 to `AGENTS.md`, §2.2 to `SKILL.md` (single new bullet / single new checklist
   item; no rewording of existing rules needed).
2. File the five §3 snapshots with real SHA-256 digests computed at landing time.
3. Re-run the §2.2 audit — expect empty; record the run date next to the checklist item's
   first-execution note or in this round's validation evidence.
4. Append the §6 LOG entry.
5. Do NOT touch: any `reports/round-8..30` filed artifact, the r5/r10 legacy rows,
   `PROVINCE.md`, corpus, tools. Corrections live only in the new snapshots.
