# Round-84 counter revisions

The frozen counter bytes are the `--freeze` revision's; every revision below
records what changed, why, and the red-before that made the change visible.
No claim verdict is ever recorded under a superseded revision.

## r0 — freeze `3ca2cf288fb593618e0559ea86a36e2dd3110eb8`

Initial freeze: `reports/round-84/claims.json`, `reports/round-84/counterlib.py`,
`reports/round-84/accept-d84.py`, `reports/round-84/accept-o84.py`. Smoke at the
freeze (no claim artifact yet): `BEFORE` passes for both claims, every claim leg
fails, no traceback (`.ufo/waves/round-84/w1/stage/L1/smoke-d-r0.txt`, `smoke-o-r0.txt` in the same directory),
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

**Red-before.** `.ufo/waves/round-84/w1/stage/L1/smoke-d-r0.txt` and
`smoke-o-r0.txt` in the same directory (grade at r0: `ACCEPT-D-84: FAIL legs=2/10`,
`ACCEPT-O-84: FAIL legs=2/8`). **After.** `stage/L1/smoke-d.txt` and
`stage/L1/smoke-o.txt` (grade at r1, same leg table, `BEFORE` still green, claim
legs still red).

## r2 — freeze `7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` (current)

**What changed.** One frozen constant in claim O's `tool84`: `shape_markers`
`SOUNDLAW_ERROR:` -> `SOUNDLAW_ERROR`. No counter code line changed.

**Why.** A conforming implementation keeps the label in a constant and prints
`"%s: %s" % (LABEL, detail)`; the literal with the colon therefore need not
appear in the source, and the frozen marker would have failed a correct tool.
The fixture proof is `.ufo/waves/round-84/w1/stage/L1/fixture-o.txt` (grade at
the r1 freeze: `TOOL FAIL bytes=11283/5000 missing=['SOUNDLAW_ERROR:']` while
`SELFTEST`, `DEMO`, `NEGATIVE` and `REGISTRY` all pass). After the revision the
same fixture grades `TOOL PASS`.

**Pre-data, but POST-dispatch — corrected 2026-11-04 after the sentinel probe.**
No claim artifact had landed, but the wave *had* been dispatched at
`2026-11-04T10:28:24` (`.ufo/waves/round-84/w1.ready.dispatched`), seven seconds
after r1 (`10:28:17`) and two minutes before this r2 commit (`10:31:06`). The
spawned seats therefore read the r1 context; the only constant that moved is the
`SOUNDLAW_ERROR` shape marker, which the delivered tool satisfies (it keeps the
label in a constant). Seat receipts that name `--freeze e160a72e` are stale on
`FROZENCFG`; the round's verdicts are graded at r2 and the L1 re-grades every
receipt it cites. The earlier draft of this paragraph said "pre-dispatch": that
was false and is kept here as the correction (mistake R84-M4).

**Red-before.** `stage/L1/smoke-d.txt` and `stage/L1/smoke-o.txt` (grade at r1).
**After.** `stage/L1/fixture-o.txt` (synthetic landing: `TOOL PASS` after the
revision, `ACCEPT-O-84: FAIL legs=7/8`, the only red leg being SEPARABLE, which
fails by design on a one-commit fixture touching both claims) and the r2 smoke
`stage/L1/smoke-d-r2.txt` / `smoke-o-r2.txt`.

## r3 — working-tree revision, not a new freeze

**What changed.** `reports/round-84/accept-d84.py`'s `junk_battery` only: the
`anchor-two-ids` mutant's expected leg changed from `ANCHORS` to `LINT`. No
grading leg, threshold or frozen constant changed; `claims.json` is unchanged,
so the freeze stays r2.

**Why.** The mutant adds a second S-id to one anchor bullet. The ANCHORS leg
skips that bullet and its floor still holds (43 >= 20), so it passes; the
LINT leg reports `MULTI-ID` and fails. The battery's expectation named the
wrong leg, not the counter's kill power. Recorded as mistake R84-M7, with the
named limit: ANCHORS alone tolerates a single malformed bullet as long as the
remaining count clears the floor.

**Red-before.** `reports/round-84/telemetry/junk-d84.txt` (first run:
`JUNK anchor-two-ids expect ANCHORS killed=False`, `JUNK-D-84: FAIL 2/3`).
**After.** `reports/round-84/telemetry/junk-d84-r3.txt` (`PASS 3/3`).
