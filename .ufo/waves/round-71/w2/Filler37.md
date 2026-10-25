# Filler37 — round 71 wave 2, mutation-tester (variant 36)

Claim re-run: **C** (variant 36 mod 3 = 0 over the claims.json order C, Ca, D).

## Verdict

- **PASS**: the frozen ACCEPT-C-71 counting command, re-run at lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` in a fresh clone, prints 36 / 243 / 797 / `CITED-LINES: 0 finding(s) in 1 file(s)` and exits 0. Every leg meets its target.
- **Re-confirmed at the new HEAD**: the lane advanced during this seat. At `cb772004f813851f5846e63f8d46d6e2ba81e236`, in a second fresh clone (0 dirty files), the command bytes are unchanged (sha256 `94787d00…`; 0 commits touch claims.json in `65ff151..HEAD`). It prints the same `36 / 243 / 797 / CITED-LINES: 0 finding(s) in 1 file(s)` and exits 0.
- **FINDING F1 (receipt not committed) — RESOLVED at `c21213a`**: at `14c88d9` the C green receipt `reports/round-71/telemetry/measures-c.txt` was untracked, and the entry's line-17 pointer to it was dead in committed bytes. `c21213a` ("commit C receipt (measures-c.txt) …") then committed it with sha256 `1d4467a6c52c679342954bc6de63b9f8b7b19eefb88816f4ca03ea1dad0c9efe`. Those are the same bytes as the 08:35:30 worktree file, so the receipt was not rewritten after measurement. The pointer resolves at `cb77200`. The record of the gap at `14c88d9` is kept below.
- **FINDING F2 (mutant survives on exit code)**: in the counting command the legs are joined with `;`, so its exit code comes only from the final `test -f`. A cited-lines defect leaves the exit code at 0. The mutant is killed only by reading the output or by `accept-c.py`.

## Freeze check

The counting command bytes were hashed (sha256 of the `counting_command` string, plus the sha256 of predicate, counting_command, target and kill_rule together) in `reports/round-71/claims.json` at three commits:

| rev | 4-field sha256 | counting_command sha256 |
|---|---|---|
| 825b78a (declaration) | a6ba93a2…bc643c | 017a7879bd6eef4e… |
| 65ff151 (re-freeze) | 62e987cd…17fb86 | 94787d005a3a821e… |
| HEAD 14c88d9 | 62e987cd…17fb86 | 94787d005a3a821e6a9e1b717c40f91aafddce4e73fd17955adaa36223982a38 |

The only change was the re-freeze at `65ff151` (08:23:39). It came before the claim-C data commit `498db73` (08:34:29) and is recorded as a pre-data correction in the claim's `correction` field. No later commit touches claims.json (`git log 825b78a^..HEAD -- reports/round-71/claims.json` lists only 825b78a and 65ff151). `base_revision` b94a543 predates claims.json (`git show` reports the path absent), so the declaration commit is the freeze point. The freeze holds.

## Re-run (fresh clone)

```
T=$(mktemp -d /tmp/f37.XXXX); git clone -q --no-local /home/vgpnk/Projects/shokunin/kotodama-shokunin $T/clone; cd $T/clone; git checkout -q 14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6
# clone HEAD=14c88d9b…, git status --porcelain = 0 lines
CMD=$(git show HEAD:reports/round-71/claims.json | python3 -c "import json,sys;print([x for x in json.load(sys.stdin)['claims'] if x['id']=='C'][0]['counting_command'])")
bash -c "$CMD"; echo EXIT=$?
```

Output, verbatim:

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Per-leg exit codes, each leg run separately:

| leg | output | exit | target | result |
|---|---|---|---|---|
| `find corpus/knowledge/culture-material -maxdepth 1 -type f \| wc -l` | 36 | 0 | 36 | PASS |
| `find corpus/knowledge -type f -name '*.md' \| wc -l` | 243 | 0 | 243 | PASS |
| `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` | 797 | 0 | >= 796 | PASS (797 = 784 + 13; S861–S873 is exactly 13 rows, which also matches the claim's "after" text: registry rises by exactly the number of new rows) |
| `python3 -B tools/check-cited-lines.py <entry>` | `CITED-LINES: 0 finding(s) in 1 file(s)` | 0 | exit 0 | PASS |
| `test -f <entry>` | (none) | 0 | exists | PASS |

Cross-check: `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` prints `/totals/files 243` and exits 0.
`python3 -B reports/round-71/accept-c.py --root .` in the clone prints `ACCEPT-C-71: PASS` and exits 0.

## F1 — claim C receipt not committed at 14c88d9 (resolved at c21213a)

```
git -C <clone> ls-files reports/round-71/telemetry
  census-end.txt census-start.txt controls-c.txt controls-ca.txt controls-d.txt measures-ca.txt measures-d.txt quarantine-verdicts.md
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --short
  ?? reports/round-71/telemetry/measures-c.txt
```

- Lane-worktree file: 720 bytes, mtime 2026-10-25 08:35:30 -0300, sha256 `1d4467a6c52c679342954bc6de63b9f8b7b19eefb88816f4ca03ea1dad0c9efe`. It is stamped at `8c203bd9dd45b42c4b45ecb3afc1b07a23575dbd` with `ACCEPT-C-71: PASS`, `culture-material=36 corpus=243 registry=797`.
- Commit `3764c2d` is titled "final measurement receipts (Ca/D)" and has no C receipt.
- Dead pointer in committed bytes: `corpus/knowledge/culture-material/dance-performance-movement-codes.md:17` says `(commit receipts: reports/round-71/telemetry/measures-c.txt)`, a path absent at HEAD.
- Impact: the claims.json green control ("each claim's counting command is run on the landed bytes … and its output is committed as the receipt") is not met for C at HEAD. The substance re-derives PASS (above); the committed evidence is missing.

## F2 — mutation probe (disposable scratch clone)

- **Mutant**: in the entry, the S862 source line (line 4) gets ` (see also S861)` appended. One line changes (`git diff --stat`: 1 insertion, 1 deletion). The result is a two-id cited line, which `check-cited-lines` reports as MULTI-ID.
- **Invariant challenged**: "`tools/check-cited-lines.py` on the entry exits 0" (predicate and target).
- **Expected detectors**: the counting command (exit code and output) and `reports/round-71/accept-c.py --root .`.

| state | entry sha256 | counting cmd EXIT | cited-lines leg exit | counting cmd cited line | accept-c.py |
|---|---|---|---|---|---|
| pristine | 3d7d0510cae347f485bf79c2f6df372fdc8858a3a439179714c057f2db2358a4 | 0 | 0 | `CITED-LINES: 0 finding(s) in 1 file(s)` | `ACCEPT-C-71: PASS`, exit 0 |
| mutated | 5304a69858c7dd2e8c4b455cdbd792a8de9a4bec849274af4c9154d8fd025cd9 | **0** | 1 | `MULTI-ID …:4 S861,S862` / `CITED-LINES: 1 finding(s) in 1 file(s)` | `LEG FAIL CITED-LINES` / `ACCEPT-C-71: FAIL`, exit 1 |
| restored | 3d7d0510cae347f485bf79c2f6df372fdc8858a3a439179714c057f2db2358a4 | 0 | 0 | `CITED-LINES: 0 finding(s) in 1 file(s)` | `ACCEPT-C-71: PASS`, exit 0 |

- **Verdict**: KILLED by `accept-c.py` (exit 1) and by reading the counting command's output. SURVIVED on the counting command's exit code, which stays 0 because `;` returns only the last leg (`test -f`). The same holds for any regression in the three count legs, which print numbers but never set the exit code.
- **Coverage finding**: a scorer who grades the frozen counting command by exit code alone would pass a broken cited-lines leg. The leg must be graded on its printed `CITED-LINES: 0` line, or through `accept-c.py`. This is a finding, not a request to change the frozen command.
- **Restoration**: entry bytes restored from a pre-mutation copy. sha256 equals pristine, `git diff --quiet` succeeds (byte-equal to HEAD), and `git status --porcelain` shows 0 lines.

## Minor note

`accept-c.py` docstring line 13 says the gap sweep "prints nothing". The SWEEP leg (lines 114–125) actually requires the owner list to be exactly the new entry (`fn_owners == [ENTRY]`, ≤1 topic owner on the entry). That is correct after landing, but the docstring is wrong. This is doc drift only; the leg passes at HEAD.

## Scope / tooling

- No lane writes other than this file. All runs were in the scratch clones `/tmp/f37.tkc5/clone` (HEAD 14c88d9, probe) and `/tmp/f37b.*` (HEAD cb77200, re-confirm). Both were removed afterwards.
- No tools installed or updated.
