# Filler31 — round 71 wave 2 (variant 30): fresh-clone re-run of the frozen claim C counting command

Seat: L1Kotodama71.Filler31 (leaf, findings only). Date 2026-10-25.

## Verdict

**PASS** for claim C at lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`: the frozen counting command reproduces the declared target in a fresh clone.
Two record findings are listed below, and neither changes the verdict. **F1 (receipt not committed):** the claim C green receipt is not committed at HEAD. **F2 (weak exit code):** the raw command's exit code depends only on its last leg.

## Setup

```
T=$(mktemp -d /tmp/f31-XXXX); git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin $T/k; cd $T/k
# CLONE=/tmp/f31-LZx8/k HEAD=14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6 dirty=0
```

I read the command verbatim from `reports/round-71/claims.json` (sha256 `73d3ad73…9be`, last touched by the re-freeze commit `65ff151`). Then I ran it with `bash -c "$CMD"`:

```
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l; find corpus/knowledge -type f -name '*.md' | wc -l; grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md; python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md; test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
```

## Exact output and exit code

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

I also ran each leg on its own. All five legs exited 0: the culture-material file count (36), the corpus file count (243), the registry row count (797), check-cited-lines (0 findings), and the entry-exists test.

| Target leg | Declared | Observed | Result |
|---|---|---|---|
| culture-material count | 36 | 36 | PASS |
| corpus count | 243 | 243 | PASS |
| registry rows | at least 784 + 12 = 796 | 797 | PASS |
| check-cited-lines exit | 0 | 0 (0 findings) | PASS |
| entry exists | yes | `test -f` exit 0 | PASS |

## Cross-checks (same clone)

- **Registry delta.** At `b94a543` (base), `corpus/SOURCES.md` has 784 rows; at HEAD it has 797. The difference is 13, which matches the 13 new rows found by grep (S861 through S873). This satisfies "increases by exactly the number of new rows".
- **Landed counter.** `python3 -B reports/round-71/accept-c.py --root .` passes all 7 legs (ENTRY, COUNTS, CITED=13, ROWS, USEDBY-PATHS, CITED-LINES, SWEEP). It prints `ACCEPT-C-71: PASS` and exits 0.
- **Freeze order.** `git merge-base --is-ancestor 65ff151 498db73` succeeds, so the re-freeze precedes the data commit. Claim C's `counting_command` hash is `017a7879…` at `825b78a` and `94787d00…` at both `65ff151` and HEAD. In other words, it changed only in the pre-data re-freeze and has not changed since. The `target` hash is `76658932…` at all three commits.

## Findings

- **F1: the claim C green receipt is not committed.** `reports/round-71/telemetry/measures-c.txt` exists in the lane worktree but is untracked. `git ls-files reports/round-71/telemetry` at HEAD lists measures-ca and measures-d but not measures-c, and `git log --all -- …/measures-c.txt` returns 0 commits. Commit `3764c2d` ("final measurement receipts (Ca/D)") skipped C. `controls.green` requires each claim's output to be "committed as the receipt", so C's green control currently has no committed receipt. The untracked file stamps revision `8c203bd`, and its counter sha `1df995c2…d5db4` matches the HEAD `accept-c.py`.
- **F2: the raw command's exit code depends only on its last leg.** The legs are joined with `;`, so the overall exit code is just the `test -f` result. If check-cited-lines failed, the command would still exit 0, and only its printed text would show the failure. `accept-c.py` covers this by naming the CITED-LINES leg and its exit code explicitly. A grader reading only the raw command's exit code would miss a failure in that leg.
- **F3 (observation): `accept-c.py` first appears in the data commit `498db73`, after the freeze.** The frozen artifact is the shell `counting_command` in `claims.json`, not `accept-c.py`. My fresh-clone run of the frozen command agrees with `accept-c.py`, so this does not change the verdict.

## Tooling

No installs or updates.
