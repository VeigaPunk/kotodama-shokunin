# Filler40 — round 71 wave 2 — fresh-clone re-run of frozen claim C counting command (variant 39)

Seat: L1Kotodama71.Filler40 (falsify / mutation-tester posture, findings only, leaf).
Claim chosen: **C** (coverage, ACCEPT-C-71). Command extracted byte-for-byte from
`reports/round-71/claims.json` `.claims[id=C].counting_command` into `/tmp/f40-cmd.sh`
(sha256 `b548208fcc1f4aefe73286c8b68914ff5cdf747f1c6850d30690454280ff5b11`).

## Verdict

| Item | Verdict |
|---|---|
| Frozen C counting command at lane HEAD, fresh clone | **PASS** (all targets met, exit 0) |
| Same at moved HEAD `ccadb598` (second fresh clone) | **PASS** (identical output, exit 0) |
| Chained-command exit code as a pass signal | **FAIL (finding F1)**: it masks a non-zero check-cited-lines exit |
| C receipt committed at HEAD | **FAIL (finding F2)**: `measures-c.txt` is untracked in the lane |

## Run 1 — lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`

```
T=$(mktemp -d /tmp/f40-XXXX); git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$T/c"; cd "$T/c"
git rev-parse HEAD          # 14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6
git status --porcelain | wc -l   # 0
bash /tmp/f40-cmd.sh; echo "EXIT=$?"
```

Command (frozen bytes):

```
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l; find corpus/knowledge -type f -name '*.md' | wc -l; grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md; python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md; test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
```

Exact output:

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Here is each step against the target `culture-material=36, corpus=243; registry >= 784 + 12; entry exists; check-cited-lines exit 0`:

| Step | Measured | Target | |
|---|---|---|---|
| culture-material files | 36 | 36 | PASS |
| corpus `.md` files | 243 | 243 | PASS |
| registry rows | 797 | >= 796 | PASS (base `b94a543c` = 784, so the delta is 13) |
| check-cited-lines (run alone) | `LEG4_EXIT=0`, 0 findings | exit 0 | PASS |
| `test -f` entry (run alone) | `LEG5_EXIT=0` | exists | PASS |

Hashes: claims.json `73d3ad73120a0c13ce99e4498f710e3a265a41f3b34b848a57d460a44087b9be`;
tools/check-cited-lines.py `a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a`;
entry `3d7d0510cae347f485bf79c2f6df372fdc8858a3a439179714c057f2db2358a4`.

Cross-checks in the same clone:
- `git diff b94a543c HEAD -- corpus/SOURCES.md` adds S861..S873 (13 new ids). S860 also appears in the diff because its row was modified (the V70-2 repoint), not added.
- Distinct ids S861..S873 cited by the entry: all 13 (the target is >= 12).
- The landed counter `python3 -B reports/round-71/accept-c.py --root .` printed `ACCEPT-C-71: PASS` with every step PASS (CITED 13, ROWS missing=[], USEDBY-PATHS missing=[], CITED-LINES exit=0, SWEEP), exit 0.
- Freeze order: claims.json was last touched at `65ff151` (the re-freeze). The claim C data commits `498db73` and `8c203bd` come after it, so no claims.json bytes changed after data landed.

## Run 2 — HEAD moved during the seat to `ccadb5989bc33b230dfd496441ddafefa1ab4b73`

`ccadb59` adds only `.ufo/waves/round-71/assimilation/fetches/*` (7 files). It is a fresh clone with the same command:

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

## Finding F1 — the frozen command's exit code is the exit of `test -f` only

Steps are joined with `;`, so `$?` reflects only the last step. Mutation probe in scratch clone 1 (disposable, bytes restored anyway):

- Mutant: I appended `- bogus: S861 and S862 on one line` to the entry. Entry sha went from `3d7d0510…` to `625607bb960b3724cf4e79ff7ccd82698e4a0b29c58f1907368a8347142b42f7`.
- Expected detector: check-cited-lines exits 1, so the counting command should go red.
- Output: `MULTI-ID …dance-performance-movement-codes.md:127 S861,S862` / `CITED-LINES: 1 finding(s) in 1 file(s)`. The checker alone gave `CHECKER_EXIT=1`, but the frozen chained command gave **`CHAINED_EXIT=0`** while still printing 36/243/797.
- Verdict: the mutant **survived** the command's exit code. It is killed only if a reader parses the `CITED-LINES: k finding(s)` line. `accept-c.py` does echo the checker exit as a named step, so the landed counter covers this, but a receipt that records only "exit 0" of the frozen shell command is not evidence for the check-cited-lines step.
- Restoration: the entry sha is back to `3d7d0510…`, `git status --porcelain | wc -l` gives 0, and the restored run exits 0.

An earlier probe (appending `[S999] bogus cite line 99999`) was **inconclusive**. The checker only flags multi-id or table-id lines, so it reported 0 findings, which is not a detector failure.

This is a coverage finding only. The frozen command is not amended (freeze rule).

## Finding F2 — claim C's after-state receipt is not committed

At both HEADs (`14c88d9b`, `ccadb598`), `git ls-files reports/round-71/telemetry` lists `controls-{c,ca,d}.txt`, `measures-ca.txt`, `measures-d.txt`, `census-{start,end}.txt` and `quarantine-verdicts.md`, but **not `measures-c.txt`**. In the lane worktree it is `?? reports/round-71/telemetry/measures-c.txt` (mtime 2026-10-25 08:35:30 -0300), and `git log --all -- reports/round-71/telemetry/measures-c.txt` is empty. Its header stamps `8c203bd9…` (an ancestor of HEAD; `ACCEPT-C-71: PASS culture-material=36 corpus=243 registry=797`), which matches this re-run.

The claims.json `controls.green` rule says the output "is committed as the receipt". For C it is not committed at lane HEAD, so a fresh clone cannot see the C green receipt.

## Tooling

No installs or updates. The seat wrote nothing to the lane except this file. The scratch clones were `/tmp/f40-HlVF/c` and `/tmp/f40b-AnKO/c`.
