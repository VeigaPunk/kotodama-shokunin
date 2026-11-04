# Round-84 counter revisions

The frozen counter bytes are the `--freeze` revision's; every revision below
records what changed, why, and the red-before that made the change visible.
No claim verdict is ever recorded under a superseded revision.

## r0 — freeze `3ca2cf288fb593618e0559ea86a36e2dd3110eb8`

Initial freeze: `reports/round-84/claims.json`, `reports/round-84/counterlib.py`,
`reports/round-84/accept-d84.py`, `reports/round-84/accept-o84.py`. Smoke at the
freeze (no claim artifact yet): `BEFORE` passes for both claims, every claim leg
fails, no traceback (`telemetry/smoke-d-r0.txt`, `telemetry/smoke-o-r0.txt`),
and the do-nothing control refuses at `--lands <base>` with
`FAIL legs=0/10` / `FAIL legs=0/8 (refused: lands equals the frozen base --
do-nothing control)` (exit 2).

## r1 — freeze `e160a72e4adf1620e09f812b913d4ece0fcd5243` (current)

**What changed.** Two frozen constants in claim D's `entry84` block:
`decision_heading` `## 2. The decision table` -> `## 2. Six design decisions`
and `anchors_heading` `## 4. Attested anchors` -> `## 3. Attested anchors`.
No counter code line changed; the counters read both headings from the frozen
config.

**Why.** The lane's two newest house entries
(`corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md` and
`guest-right-hospitality-law.md`) carry the section shape
`1. Partial owners / 2. Six design decisions / 2.1 Lexicon interface /
3. Attested anchors / 4. Craft checklist / 5. Worked example / 6. Lore
handoff`. Grading a divergent shape would establish a second convention for no
gain, and the closure compares entries to their neighbours.

**Pre-dispatch.** No claim artifact had landed and the wave had not been
dispatched at the change: `.ufo/waves/round-84/w1.ready` carried no
`.ready.dispatched` marker, and `w1-dispatch.json` was regenerated from the r1
spec. No seat read the r0 heading text.

**Red-before.** `telemetry/smoke-d-r0.txt` and `telemetry/smoke-o-r0.txt`
(grade at r0: `ACCEPT-D-84: FAIL legs=2/10`, `ACCEPT-O-84: FAIL legs=2/8`).
**After.** `telemetry/smoke-d.txt` and `telemetry/smoke-o.txt` (grade at r1,
same leg table, `BEFORE` still green, claim legs still red).
