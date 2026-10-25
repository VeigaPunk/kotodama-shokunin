# Filler34 — round 71 wave 2 — fresh-clone re-run of frozen claim C counting command (variant 33)

Seat: `L1Kotodama71.Filler34` (leaf, findings only; no lane bytes written other than this file).
Claim chosen: **C** (variant 33 → 33 mod 3 = 0 → first claim in `reports/round-71/claims.json`).

## Verdict

**PASS** — the frozen claim-C counting command, run verbatim in a fresh clone at lane HEAD, prints
`36 / 243 / 797 / CITED-LINES: 0 finding(s) in 1 file(s)` and exits 0; every leg meets the declared target.

Two side findings (not a FAIL of the data predicate):

- **F34-1 (receipt not committed).** `reports/round-71/telemetry/measures-c.txt` is **untracked** at HEAD
  `14c88d9` (`git status` shows `?? reports/round-71/telemetry/measures-c.txt`;
  `git show HEAD:reports/round-71/telemetry/measures-c.txt` → `fatal: ... exists on disk, but not in 'HEAD'`).
  The declaration's green control says each claim's output "is committed as the receipt". The Ca and D receipts
  are tracked; C's is not. A fresh clone therefore carries no C receipt.
- **F34-2 (exit masking in the raw command).** The `;`-joined `counting_command` ends in `test -f`, so its
  overall exit reflects only that last leg. In a disposable scratch copy, replacing `tools/check-cited-lines.py`
  with a stub that prints `CITED-LINES: 1 finding(s)` and exits 1 still gave `EXIT=0`. Exit 0 from the raw
  command is not evidence that check-cited-lines passed; the printed line is. (Round-71 correction (3) has
  `accept-c.py` echo that exit as a named leg; this finding concerns the raw `counting_command` string only.)

## Provenance

| item | value |
|---|---|
| lane HEAD | `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` |
| HEAD tree | `2a9f2ab5622b62a51c7f49df0577bd659ce191c8` |
| clone | `git clone -q --no-local <lane> /tmp/f34.F6Lm/c && git checkout -q 14c88d9b…` ; `git status --porcelain` empty |
| command bytes sha256 (HEAD) | `b548208fcc1f4aefe73286c8b68914ff5cdf747f1c6850d30690454280ff5b11` |
| command bytes sha256 (re-freeze `65ff151`) | `b548208f…5b11` (identical) |
| command bytes sha256 (first declaration `825b78a`) | `49579c9d…7784` (pre-data correction, superseded at `65ff151`) |
| freeze ordering | `git merge-base --is-ancestor 65ff151 498db73` → true (re-freeze precedes C data landing) |
| base_revision `b94a543` | does not carry `reports/round-71/claims.json` (declared after base; expected) |
| python | 3.14.8 |

Command extracted with:
`python3 -c "import json;print(json.load(open('reports/round-71/claims.json'))['claims'][0]['counting_command'])"`

```
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l; find corpus/knowledge -type f -name '*.md' | wc -l; grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md; python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md; test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
```

## Exact output (verbatim run: `bash -c "$(cat cmd)" 2>&1; echo EXIT=$?`)

```
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Output file sha256: `5431fa6a5e97db7f2c1c0b042f3d88f114e0cafb5f65690d9b85bd725c96c73b`.

## Per-leg check against target

| leg | output | exit | target | result |
|---|---|---|---|---|
| culture-material `find \| wc -l` | 36 | 0 | 36 | PASS |
| corpus `find *.md \| wc -l` | 243 | 0 | 243 | PASS |
| registry `grep -cE` | 797 | 0 | ≥ 784 + 12 = 796 | PASS |
| `check-cited-lines.py` on entry | `0 finding(s) in 1 file(s)` | 0 | exit 0 | PASS |
| `test -f` entry | — | 0 | exists | PASS |

Registry delta re-derived: the same grep on `git show 65ff151:corpus/SOURCES.md` → **784**; the id-set diff
(re-freeze → HEAD) adds exactly `S861 … S873` (13 ids), removes none; `uniq -d` on HEAD ids → no duplicates.
797 − 784 = 13 = number of new rows, which agrees with the `after` sentence ("increases by exactly the number of new rows").

Cross-check: the lane's untracked `measures-c.txt` (stamped `8c203bd9`, an ancestor of HEAD) reports
`culture-material=36 corpus=243 registry=797`, `check-cited-lines exit=0 (0 findings)`, which matches this fresh-clone run.

## Exit-masking probe (F34-2) — disposable scratch

`cp -r clone m` → original `tools/check-cited-lines.py` sha256
`a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a` → stub (prints 1 finding, `sys.exit(1)`) →
same verbatim command → output `36 / 243 / 797 / CITED-LINES: 1 finding(s) in 1 file(s)`, `EXIT=0`.
Mutant **survived** the raw command's exit code (detected only by the printed text). The scratch copy was
disposable and was deleted (`rm -rf m`); the clone and the lane were not modified.

## Installs

None.
