# Filler39 — round 71 wave 2 (variant 38): frozen claim-C counting command, fresh clone at lane HEAD

Seat: `L1Kotodama71.Filler39`, falsifier, findings only. I made no lane writes apart from this file.
Tool installs or updates: none.

## Verdict

**PASS.** At lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`, the frozen claim-C `counting_command` reaches its target, and `ACCEPT-C-71` prints PASS with exit 0. Three lower-severity defects are listed under Findings.

## Setup (exact)

```
L=/home/vgpnk/Projects/shokunin/kotodama-shokunin
T=$(mktemp -d /tmp/f39.XXXX); git clone -q --no-local "$L" "$T/c"; cd "$T/c"
# CLONE=/tmp/f39.TnoP/c HEAD=14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6 DIRTY=0
CMD=$(python3 -c "import json;print([c for c in json.load(open('reports/round-71/claims.json'))['claims'] if c['id']=='C'][0]['counting_command'])")
bash -c "$CMD"; echo "EXIT=$?"
```

- The command is taken verbatim from `reports/round-71/claims.json` (blob `33b3c343`).
- sha256 of the command string: `94787d005a3a821e6a9e1b717c40f91aafddce4e73fd17955adaa36223982a38`. The string is byte-identical at the re-freeze commit `65ff151`.

## Output at HEAD (exact)

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Exit code of each leg, from running the legs separately: find=0, find=0, grep -c=0, check-cited-lines=0, test -f=0.

| target leg | expected | observed | result |
|---|---|---|---|
| culture-material files | 36 | 36 | PASS |
| corpus `*.md` | 243 | 243 | PASS |
| registry rows | >= 784+12 = 796 | 797 (= 784 + 13) | PASS |
| check-cited-lines | exit 0 | exit 0, 0 findings | PASS |
| entry exists | test -f 0 | 0 | PASS |

Cross-check with the Python counter: `python3 -B reports/round-71/accept-c.py --root .` exits 0. All seven legs pass: ENTRY, COUNTS 36/243, CITED 13, ROWS, USEDBY-PATHS, CITED-LINES, and SWEEP (the entry is the only owner).

Row re-derivation:
- The entry cites exactly `S861`..`S873` (13 distinct ids).
- Every one of those rows has status `mined`, opened `2026-10-25`, and used-by set to the entry path.
- Tiers: 12 are A and S873 is B.
- 13 registry rows have an id of S861 or higher, which matches the +13 delta.

Do-nothing control: I re-ran the same command in a worktree at re-freeze `65ff151` and got `35 / 242 / 784 / CITED_LINES_ERROR no such file or directory: …dance-performance-movement-codes.md / EXIT=1`. The control fails to reach the target, as declared, and it matches `controls-c.txt`.

## Findings

1. **MEDIUM: the Python counter was written together with the data, not frozen before it.**
   - Evidence: `git cat-file -e <rev>:reports/round-71/accept-c.py` shows the file absent at `825b78a` (declaration) and at `65ff151` (re-freeze). It first appears in `498db73` ("claim C data lands"), which is also the only commit that touches it.
   - The freeze rule in `claims.json` says the "predicate, counter, kill rule and target … are frozen at this commit". Only the shell `counting_command` was frozen before the data.
   - How this could be exploited: someone writing the counter after the data could fit its legs to the landed bytes. Two examples: the SWEEP leg accepts at most one topic owner, and the CITED leg counts any `S\d{3,}` token rather than "opened this round".
   - Impact: limited at HEAD. My independent check of the rows (opened 2026-10-25, all mined, used-by correct) agrees with the counter. But the PASS from `ACCEPT-C-71` is evidence written by the author after the data landed, not a frozen gate.
   - Smallest fix: in the lesson or log, record the shell `counting_command` as the frozen instrument for claim C. Describe `accept-c.py` as an aid written at land time, or freeze future counters in the declaration commit.

2. **MEDIUM: the claim-C receipt was never committed.**
   - Evidence: in the lane, `git status` shows `?? reports/round-71/telemetry/measures-c.txt`, and `git log --all -- …/measures-c.txt` returns nothing. `git ls-files reports/round-71/telemetry` lists `measures-ca.txt` and `measures-d.txt` but not `measures-c.txt`.
   - The green control in `claims.json` requires that "its output is committed as the receipt". The claim-C line in `LOG.md:4269` ("ACCEPT-C-71 PASS at `8c203bd9`") therefore has no committed receipt behind it.
   - The untracked file is internally consistent. Its counter sha `1df995c2…` matches `accept-c.py` at both 8c203bd and HEAD. Its stamped, evaluated and measured revision is `8c203bd9`, and the only claim-C-surface diff from `8c203bd` to HEAD is a one-line edit to S860's verify-at cell in `corpus/SOURCES.md`, which does not affect claim C.
   - Smallest fix: commit `reports/round-71/telemetry/measures-c.txt` as it is now, and point the LOG claim-C line at it.

3. **LOW: the shell command's exit code only grades the last leg.**
   - The legs are joined with `;`, so the overall exit code is just the exit of `test -f`. The counts are printed but not compared against anything, and a non-zero exit from check-cited-lines would be hidden.
   - At HEAD every leg's own exit is 0, so the verdict does not change.
   - Smallest fix, for future declarations only: chain the legs with `&&` and add explicit `[ "$(…)" = 36 ]` comparisons.

## Cleanup

The scratch base worktree and the fresh clone `/tmp/f39.TnoP` have both been removed.
