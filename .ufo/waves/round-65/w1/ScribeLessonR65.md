# ScribeLessonR65 — round-65 lesson skeleton + lessons-index revision bump

Seat: `kotodama-r65.ScribeLessonR65` (scribe, round-65 v2 wave, build side).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, jj-colocated git,
base revision `17c32302c6845c8f164b985a8cb312d3181c8788` (`git rev-parse HEAD`
read at seat open; no writes to git or jj). Date: 2026-10-24.

## 1. Behavior delivered

Wrote **one artifact**: `.ufo/waves/round-65/stage/lesson-skeleton.md`
(18475 bytes, 312 lines, sha256
`de4eabd2dfea9b183a2306abc1051a0f734dbeb04a352411b17ccc488bd94a63`). It is a
draft; nothing in it is asserted as a measurement of unlanded work.

Contents, in the assignment's order:

1. **Part A — the `corpus/lessons/round-65.md` skeleton**: header
   `# Round 65 — 2026-10-24 (hyaku run 5, L1 <FILL>)`, the four column-0
   contract lines (`source:`, `verified-at:`, `recheck:`, `scope:`) with fill
   rules, `## Round summary` with the three claim predicates and their exact leg
   lists from `claims.json`, `## Gate` placeholder for S750-S775 (row template,
   seven row rules tied to a checker class or a round-64 defect id, the
   `Note: S### —` convention, the recipe for the frozen LIVE subset
   S750/S755/S760/S765/S770/S775), `## Mistakes` carrying **R65-M1**, and
   `## Census and counts` with placeholder slots.
2. **Part B — the `corpus/lessons/README.md` bump**: the exact revision in
   force, the live base measurement, the exact §2 row to append with per-cell
   rules, the machine-read count-line correction, ready-to-paste revision-14
   block text, and the write-scope notes.

## 2. Gates and controls actually run (read-only)

| command | outcome |
|---|---|
| `ls corpus/lessons/*.md \| wc -l` | 65 |
| `grep -c '^| \`corpus/lessons/' corpus/lessons/README.md` | 50 |
| pin re-derivation over every §2 row (bytes/lines/sha8 vs live bytes) | **0 drift** |
| per-row `test -e` over §2 rows | **0 rows name a missing file** |
| `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | **exit 1**, `findings: 3` (C31-1 15 unindexed files; C34-3 shape drift on rounds 54-57; C34-2 stated 43/43 vs measured 50/65); `queue rows: 78`; formats `{gate-keeper: 35, fragment-index: 5, plain: 25}` |
| `python3 -B tools/check-gate-quotes.py corpus/lessons/round-64.md` | `GATE_QUOTES: 0 findings`, exit 0 |
| `python3 -B tools/check-gate-quotes.py corpus/lessons/round-63.md` | `GATE_QUOTES: 0 findings`, exit 0 |
| `python3 -B tools/check-gate-quotes.py .ufo/waves/round-65/stage/lesson-skeleton.md` | `GATE_QUOTES: 0 findings`, exit 0 |
| **negative control** — skeleton copy with `## Gate` renamed | exit 2, stderr `GATE_QUOTES_ERROR: … no `## Gate` section` |
| **forcing control** — one injected 30-word `- S750 …` row inside the Gate section of a skeleton copy | exit 1, `<path>:122 S750 words=30`, `GATE_QUOTES: 1 findings` |
| `grep -n "lessons\|round-65.md" reports/round-65/accept-c.py accept-o.py accept-ca.py` | only `accept-ca.py` reads `corpus/lessons/round-65.md` (the QUOTES leg, `:229-236`); C and O do not |
| `ls -A .ufo/waves/round-65/rows/` | only `ScoutGapGames/`, `ScoutRow02/`; **no `row-<SID>.txt` for S750-S775 exists** |

Controls were run in `/tmp` scratch copies; nothing outside the two artifacts
below was written in the lane.

## 3. Touched surfaces

- Written: `.ufo/waves/round-65/stage/lesson-skeleton.md` (new, 18475 B),
  `.ufo/waves/round-65/w1/ScribeLessonR65.md` (this report).
- Created (empty dirs, required by the write paths): `.ufo/waves/round-65/stage/`
  already existed as a sibling landing directory; no lane file was modified,
  deleted or renamed.
- Read only: `corpus/lessons/round-64.md`, `corpus/lessons/round-63.md`,
  `corpus/lessons/round-62.md`, `corpus/lessons/round-49.md`,
  `corpus/lessons/round-64-verifier-spotcheck.md` §6,
  `corpus/lessons/README.md`, `reports/round-65/claims.json`,
  `reports/round-65/accept-ca.py`, `reports/round-65/accept-c.py` (grep + header),
  `reports/round-25/audit/c31-lessons-index-audit.py`,
  `tools/check-gate-quotes.py`, `tools/check-row-fragments.py` (defaults only),
  `.ufo/waves/round-65/spec-v2.json`, `.ufo/waves/round-65/gen-spec.py`,
  `.ufo/waves/round-65/stage/gate-spec.md` (head).
- No commit, no jj/git write, no index touch, no product code, no counter, no
  tool, no judge.

## 4. Findings

**F1 — the lessons index is 15 rows behind at base, and this round adds the 16th.**
Live state at `17c32302`: 65 lesson files, 50 §2 rows. Unindexed:
`round-57-verifier-spotcheck.md`, `round-58-verifier-spotcheck.md`, `round-58.md`,
`round-59-verifier-spotcheck.md`, `round-59.md`, `round-60-verifier-spotcheck.md`,
`round-60.md`, `round-61-verifier-spotcheck.md`, `round-61.md`,
`round-62-verifier-spotcheck.md`, `round-62.md`, `round-63-verifier-spotcheck.md`,
`round-63.md`, `round-64-verifier-spotcheck.md`, `round-64.md`. Pre-existing, not
caused by this round; `round-65.md` becomes the sixteenth unless the bump lands,
and the audit's `C31-1` will name it.

**F2 — the exact current revision is 13, and its own stated counts are false at base.**
`corpus/lessons/README.md:554-556`: "## Revision 13 … rows 48, files 48 (the §2
count line above is left as filed)". Measured now: 50 rows / 65 files. The next
block is **revision 14**. There is no unstamped revision and nothing after 13.

**F3 — four §2 rows declare a contract cell the files do not carry.**
`C34-3`: `round-54.md`, `round-55.md`, `round-56.md`, `round-57.md` declare
`contract 4/4`; each measures `0/4` (no column-0 `source:`/`verified-at:`/
`recheck:`/`scope:` lines). The model `round-64.md` likewise carries none. So the
round-65 row must use the measured cell, not the neighbours' `4/4` — the skeleton
carries the four lines deliberately so `4/4` is honest for it.

**F4 — machine-read count line is drift the bump must correct in place.**
`README.md:122` `**Rows: 43. Files: 43.**` vs measured 50/65 (`C34b`). Revision 13
explicitly left it filed, so a revision-14 block cannot supersede it; the audit
reads the last `**Rows: N. Files: M.**` occurrence. Post-land values: 51 / 66 if
only the round-65 row is added. Two reader-visible drifts the audit does **not**
flag: `:271` "Of the 42 index rows" (live 50) and §1's `wc -l # 37` annotation
(live 65).

**F5 — the index bump is owned by no claim.** `corpus/lessons/README.md` appears
in none of the three claims' `lands` (C: entry, `corpus/SOURCES.md`,
`corpus/README.md`; O: three counters, `tools/check-row-fragments.py`, the
exactness receipt; Ca: the eight printed paths). It is a records edit the L1 must
either land and name, or disposition as omitted. Note also that `corpus/README.md`
(C's land) and `corpus/lessons/README.md` are different files.

**F6 — Ca's statement requires files its `lands` do not name.** The Ca statement
requires R1 repeat corrections in `LOG.md`, `SCORECARD.md` and
`.ufo/waves/round-64/w2/LessonFinal.md`, and R3/R5 legs *read* `LOG.md` and
`SCORECARD.md` (`accept-ca.py` R1/R3/R5), yet neither file is in Ca's `lands`.
Reported as a declaration gap for the L1, not repaired here.

**F7 — the Gate is the only lecture the lesson must satisfy, and it is a cap
checker, not a support check.** The `QUOTES` leg (`accept-ca.py:229-236`) requires
`tools/check-gate-quotes.py corpus/lessons/round-65.md` to exit 0 and print
`0 finding`. A lesson without a `## Gate` section exits 2 and fails the leg
(negative control above). The skeleton passes at 0 findings *because it carries no
quoted span* — that is a format result, never a support result
(`stage/gate-spec.md` says the same); the forcing control shows a 30-word row is
caught.

**F8 — no fragment exists for S750-S775 at this stamp.** `.ufo/waves/round-65/rows/`
holds only `ScoutGapGames/` and `ScoutRow02/` (no `row-<SID>.txt`). The Gate is
placed as a placeholder exactly as assigned; the fills are `ExecGateFill`
(`stage/lesson-gate.md`, quote byte-equal to the fragment) and the L1. Fragment
path convention confirmed from `tools/check-row-fragments.py:265` (`--rows`
default `.ufo/waves/round-65/rows`) and the ScoutRow prompts
(`rows/<SEAT>/row-<SID>.txt`, with a `ROW=| … | "<anchor quote 8-25 body
words>" | …` line — so a byte-equal lift is inside the 25-word cap by
construction).

**F9 — the R7 trap applies to this lesson too.** The round-64 entry's
`verified-at:` kept the phrase "skeleton structure prepared; cited source claims
await L1 insertion" for a whole round and was routed as defect R7. The skeleton's
`verified-at:` slot states the rule explicitly; the L1 must not land it with
skeleton/prepared/await-L1 wording.

**F10 — two independent Gate cutters are in flight.** `stage/gate-spec.md`
(ScribeGateRecords) and the skeleton's Part A both describe the Gate; the skeleton
defers to `gate-spec.md` and to the assembled `stage/lesson-gate.md`, with an
explicit "copy its rows verbatim" instruction, because re-cutting the same quote
in two seats is the R64-M4 entry path.

## 5. Out of scope / dependencies (recorded, not chased)

- **Row content**: no S750-S775 fragment existed, so no URL, quote, tier or
  teaches cell was asserted anywhere in the skeleton. Claim-C row work is the
  ScoutRow/ExecGateFill/L1 path.
- **The three counters** were not executed: the assignment is a skeleton, the
  counters are frozen pre-data and their measurement is the L1's; running them now
  over absent lands would produce a red receipt with no information.
- **Live URL verification** of any round-65 source: not attempted (nothing to
  verify).
- **Back-filling the 15 unindexed rows** and repairing the 4 stale contract cells:
  deliberately not done. They are pre-existing drift outside this seat's artifact
  and would need their own pins and revision; Part B names them so the bump cannot
  read as green.
- Sibling drafts `stage/gate-spec.md`, `stage/entry-draft.md`,
  `stage/readme-patch.md` were read only as heads/for path convention; no
  coordination message was needed.

## 6. Known limits

- The skeleton's `<FILL>` slots are text instructions, not evidence; every
  measured number that *is* in the file (65/50/78/15/0/3/43-43, the revision-13
  text, the two 0-findings controls) was produced by a command in §2 at this
  stamp.
- `c31-lessons-index-audit.py` exit code was measured directly (`real_exit=1`,
  without a pipe); the same run's stdout is quoted in §2 and in the skeleton.
- No tool was installed or upgraded (nothing was needed; pacman guard in force —
  no pacman transaction was attempted).

## 7. Artifacts

- `.ufo/waves/round-65/stage/lesson-skeleton.md` — 18475 B, 312 lines, sha256
  `de4eabd2dfea9b183a2306abc1051a0f734dbeb04a352411b17ccc488bd94a63`.
- `.ufo/waves/round-65/w1/ScribeLessonR65.md` — this report.

Report: .ufo/waves/round-65/w1/ScribeLessonR65.md
