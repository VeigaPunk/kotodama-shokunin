# V70-6 falsification attempt — no-git guard

## Counterexample and evidence

The prescribed `git archive 453676a2363c97e158cb112c9588906564d95a21` reproduction was run in a fresh temporary extraction with the frozen round-69 counter. Output was:

```
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
EXIT=1
```

This confirms the false-red. In `reports/round-69/accept-d.py:197-210`, the fixture starts with live `SKILL.md`; only a successful `git show 793f797:SKILL.md` replaces it with pre-table contents. In an archive there is no object store, so fallback preserves the table and makes the supposedly do-nothing fixture pass.

The proposed round-71 wrapper checks only whether `git -C LANE rev-parse --git-dir` exits zero (`reports/round-71/accept-d.py:41-47`). This is not equivalent to checking that the required historical object is available. A concrete false-positive: with the actual lane repository present, setting `GIT_DIR=/definitely/missing` makes `git rev-parse --git-dir` fail with status 128; invoking the proposed selftest under that environment prints `SELFTEST: COULD-NOT-EVALUATE (no git)` and exits 2, although the lane has a valid `.git` directory and the required object `793f797:SKILL.md` is available normally. Other git invocation/configuration failures can similarly be mislabeled as repository absence.

## Impacted axes

- **Depth / instrument correctness:** the original false-red is real and the wrapper avoids grading that archive case as a craft failure.
- **Calibration / verdict provenance:** exit 2 currently conflates “no repository metadata” with “Git could not be queried”; it may suppress a genuine selftest failure when a repo exists but Git is misconfigured/unavailable.

## Smallest safe correction

Do not classify every nonzero `rev-parse` result as “no git.” Distinguish repository absence from command failure. For this specific contract, the narrowest robust guard is to require successful retrieval of `793f797:SKILL.md` (or explicitly probe for the expected `.git` metadata while accounting for `.git` files/worktrees), returning the declared exit 2 only when the object store is genuinely unavailable; surface unexpected Git errors separately as an evaluation error. Merely checking `.git` directory existence is not robust for linked worktrees, whose `.git` is a file. The existing exit-2 behavior can be robust if the no-git condition is made specific, but this implementation's return-code-only detection cannot distinguish the demonstrated case.

No tools were installed.
