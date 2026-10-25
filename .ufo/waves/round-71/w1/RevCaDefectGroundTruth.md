# RevCa — round-70 defect ground truths (V70-1..V70-5) verified against the current lane tree

Seat: `L1Kotodama71.RevCaDefectGroundTruth` (leaf, read-only). Lane tree:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (HEAD `b694afd6`, git via jj repo).
Source of record: `corpus/lessons/round-70-verifier-spotcheck.md` §6 (routed defects).
All five ground truths **hold** in the current tree, each with the exact command + output below.

---

## V70-1 — six round-70 telemetry receipts lack the QUALITY 17/19 header block — CONFIRMED (absent)

All six files exist and carry only single-line headers; none contains any of the six
17/19 header lines.

Command (run from lane root):

    grep -cE '^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)' \
      reports/round-70/telemetry/measures-{o,ca,d}.txt reports/round-70/telemetry/controls-{o,ca,d}.txt

Output:

    reports/round-70/telemetry/measures-o.txt:0
    reports/round-70/telemetry/measures-ca.txt:0
    reports/round-70/telemetry/measures-d.txt:0
    reports/round-70/telemetry/controls-o.txt:0
    reports/round-70/telemetry/controls-ca.txt:0
    reports/round-70/telemetry/controls-d.txt:0
    exit=1

Actual headers (cat of each file, line 1):

- measures-o.txt: `# after-state receipt O — measured at lane 6cb51a4+landed edits, 2026-10-25`
- measures-ca.txt: `# after-state receipt Ca — measured at lane 6cb51a4+landed edits, 2026-10-25`
- measures-d.txt: `# after-state receipt D — measured at lane 6cb51a4+landed edits, 2026-10-25`
- controls-o.txt: `# pre-data control O (do-nothing) - measured at base 21e6a7f on 2026-10-25`
- controls-ca.txt: `# pre-data control Ca (do-nothing) - measured at base 21e6a7f on 2026-10-25`
- controls-d.txt: `# pre-data control D (do-nothing) - measured at base 21e6a7f on 2026-10-25`

No `# counter sha256`, `# stamped revision`, `# evaluated revision`, `# measured revision (lane main)`,
`# tree`, or `# worktree dirty` line appears in any of the six. V70-1 ground truth holds.

---

## V70-2 — S860 verify-at cell names 6cb51a4 with the wrong blob pair — CONFIRMED

`corpus/SOURCES.md:815` (S860) current cell text:

    file blob 6a314e9c7c5635a15a9b2f8b57bc34db8039a301 at lane revision 6cb51a447043a9691c59794d7479c1a81c0626a4

Commands (from lane root):

    git rev-parse '6cb51a447043a9691c59794d7479c1a81c0626a4:tools/check-supersession-settlement.py'
    git rev-parse 'acc2d614a097484d8dc41230229dc4ead07d8a19:tools/check-supersession-settlement.py'
    git show 6cb51a447043a9691c59794d7479c1a81c0626a4:tools/check-supersession-settlement.py | grep -c MALFORMED-ROW
    git show acc2d614a097484d8dc41230229dc4ead07d8a19:tools/check-supersession-settlement.py | grep -c MALFORMED-ROW

Output:

    1ef2e965204f53f40ffbabf45abea3fae9f029a6     # blob at 6cb51a4 (NOT 6a314e9c)
    6a314e9c7c5635a15a9b2f8b57bc34db8039a301     # blob at acc2d614 (= the blob named in the cell)
    0                                            # MALFORMED-ROW count at 6cb51a4
    2                                            # MALFORMED-ROW count at acc2d614

Blob `6a314e9c` first appears in commits `e345c7ab` / `acc2d614` (2026-10-25 07:19:40/41),
both children of `6cb51a4` (verified: parent of both is `6cb51a4`; `6cb51a4` is an ancestor of
`acc2d614`). At the named revision `6cb51a4` the file is the pre-hardening blob `1ef2e965`
(0 `MALFORMED-ROW`), so the blob named in the cell does not live at the revision named. V70-2
ground truth holds; the cell should name `acc2d614`.

---

## V70-3 — round-70 Gate quote is 27 words (not 25) — CONFIRMED

Quote cell extracted from `corpus/lessons/round-70.md` line 13 (Gate table, S860 row):
field 4 under `|` split:

    "A row whose `used-by` names a path that does not contain the row's own id is `STALE-USED-BY` (reported; gated only for the frozen ruling set, not globally...)"

Command:

    awk -F'|' 'NR==13 {print $4}' corpus/lessons/round-70.md | wc -w

Output:

    27

(Words: A row whose used-by names a path that does not contain the row's own id is
STALE-USED-BY (reported; gated only for the frozen ruling set, not globally...) = 27.)
The table header on line 11 declares `quote (≤25 words)`, and the fleet report
`.ufo/reports/round-70/kotodama.md:101` calls it "a 25-word located quote" — both
characterizations are wrong for the committed bytes. V70-3 ground truth holds.

---

## V70-4 — round-70 fleet report claims expansion/discernment improved — CONFIRMED

File: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-70/kotodama.md`, §Trend verdicts.

Command:

    grep -nE '^- \*\*(expansion|quality|discernment)' /home/vgpnk/Projects/shokunin/.ufo/reports/round-70/kotodama.md

Output:

    111:- **expansion — improved.** Registry 783→784 rows (S860, tier A, mined, `used-by`
    114:- **quality — improved.** The checker's three routed gaps (malformed-row swallow, per-pair
    119:- **discernment — improved.** The round repaired the round-69 closure's own record defects (D1..D10

Expansion and discernment are both graded `improved` (quality too). V70-4 ground truth holds.

---

## V70-5 — round-70 lesson has no reject-sweep statement — CONFIRMED

`corpus/lessons/round-70.md`: the `## Gate` table (line 13) holds exactly one candidate (S860),
verdict `admitted`; there is no reject row and no "rejected this round: none" / sweep statement.

Command:

    grep -nEi 'reject|sweep' corpus/lessons/round-70.md

Output:

    1:# Round 70 (2026-10-25, hyaku run 6, L1 kotodama-r70) — repair-first after round 69 closure rejection
    3:The round-69 closure rejected the round (honest stop: operability and depth improved, but the

The only reject mentions are historical references to the round-69 closure verdict (title and
line 3); there is no statement of this round's reject-sweep outcome. V70-5 ground truth holds.

---

## Summary

| id | ground truth | status | key evidence |
|---|---|---|---|
| V70-1 | six receipts carry no six-line 17/19 header | CONFIRMED absent | grep 0 in all six files; single-line headers only |
| V70-2 | S860 verify-at pairs blob 6a314e9c with revision 6cb51a4 | CONFIRMED wrong pair | at 6cb51a4 blob = 1ef2e965, MALFORMED-ROW count 0; blob 6a314e9c first exists at acc2d614 |
| V70-3 | round-70 Gate quote is 27 words | CONFIRMED | `wc -w` = 27; report wrongly calls it 25 words |
| V70-4 | fleet report claims expansion/discernment improved | CONFIRMED | report :111 `expansion — improved`, :119 `discernment — improved` |
| V70-5 | round-70 lesson has no reject-sweep statement | CONFIRMED | Gate = 1 candidate admitted, no reject row, no sweep statement |

Residual risk / verification gaps: none material. Blob/revision checks were run against the lane's
git objects at the current HEAD (lane is jj-backed; `git rev-parse HEAD` = `b694afd6`). The
round-71 fix work (V70-1..V70-5) is in flight elsewhere in the round; this seat verified the
frozen ground truths only, per its read-only scope. No tools installed (none needed).
