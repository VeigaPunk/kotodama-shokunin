# Filler32 — variant 31: re-run one frozen claim counting command at lane HEAD in a fresh clone

Seat: L1Kotodama71.Filler32 (falsify, leaf, read-only on lane; scratch clones only).
Lane HEAD measured: `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` (tree `2a9f2ab5622b62a51c7f49df0577bd659ce191c8`).
Claim re-run: **C** (coverage), frozen `counting_command` extracted verbatim from `reports/round-71/claims.json`.
Scratch: `/tmp/f32-clone` (fresh `git clone` of lane at HEAD), `/tmp/f32-base` (fresh clone checked out at `b94a543c`), `/tmp/f32-mut` (copy of the HEAD clone, mutated).

## 1. The command, verbatim (368 bytes, sha256 `b548208fcc1f4aefe73286c8b68914ff5cdf747f1c6850d30690454280ff5b11`)

```
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l; find corpus/knowledge -type f -name '*.md' | wc -l; grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md; python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md; test -f corpus/knowledge/culture-material/dance-performance-movement-codes.md
```

## 2. Re-run at lane HEAD in a fresh clone — PASS

```
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/f32-clone && cd /tmp/f32-clone
$ git rev-parse HEAD          -> 14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6
$ git status --porcelain | wc -l -> 0            (clean clone, no lane edits)
$ bash /tmp/f32-claimC.sh
36
243
797
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0
```

Stdout exactly 4 lines, stderr empty, exit **0**.
`culture-material=36`, `corpus=243`, `registry=797`, `check-cited-lines exit=0 (0 findings)` — byte-for-byte the numbers the receipt `ACCEPT-C-71: PASS / culture-material=36 corpus=243 registry=797` prints, and all legs of the frozen target are met (`36`, `243`, `797 >= 784+12=796`, entry present, lint exit 0). The claim **holds at HEAD**, not only at its stamped revision `8c203bd`.

Independent re-derivation (same clone, not the counter):

```
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md           -> 797
$ ... | grep -oE 'S[0-9]{3,}' | sort -u | wc -l                          -> 797   (no duplicate ids; uniq -d empty)
$ git show b94a543:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' -> 784
$ for n in 861..873; grep -cE "^ {0,3}\|[[:space:]]*S$n\b"               -> 1 each (S861..S873, 13 rows)
$ grep -nE '^#{1,3} ' corpus/SOURCES.md   -> ## Registry at 26, ## Paths at 829
$ grep -nE '^ {0,3}\|[[:space:]]*S(861|873)[[:space:]]*\|'               -> 816, 828   (inside Registry)
$ awk -F'|' over S861..S873 -> status=mined for all 13; used-by=corpus/knowledge/culture-material/dance-performance-movement-codes.md for all 13
$ sha256sum reports/round-71/accept-c.py                                  -> 1df995c2...d5db4    (== receipt "# counter sha256 (self)")
$ git rev-parse 8c203bd^{tree}                                            -> ffb5c549...d33a     (== receipt "# tree")
```

## 3. Before-state control re-derived at base — PASS

```
$ cd /tmp/f32-base && git checkout -q b94a543c && find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'   -> (empty)
$ grep -rniE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b' corpus/knowledge/culture-material/*.md          -> (empty)
$ grep -rniE '^- topic:.*(danc|choreograph|movement culture|performance)'   (unbound) -> 1 line: funerary-material-culture.md:4 ("avoidance")
$ culture-material=35 corpus=242 registry=784
```

The entry's `- gap filled:` line (`corpus/knowledge/.../dance-performance-movement-codes.md:19`) states exactly this, including the `funerary-material-culture.md:4` false-match — verified byte-level at base. Do-nothing control stands.

## 4. FAIL — the frozen command's exit code is masked and cannot express the kill rule

The command's last statement is `test -f ENTRY`, so its exit status is 0 whenever the entry exists; every earlier leg's status is discarded (no `set -e`, no `&&`, no explicit exit aggregation). Demonstrated on a mutated copy of the HEAD clone (`/tmp/f32-mut`: two registry rows S872/S873 deleted → 795, plus one line citing `S861 and S862` appended to the entry):

```
$ bash /tmp/f32-claimC.sh
36
243
795
MULTI-ID corpus/knowledge/culture-material/dance-performance-movement-codes.md:127 S861,S862
CITED-LINES: 1 finding(s) in 1 file(s)
EXIT=0                      <-- registry below target (795 < 796) AND lint non-zero, yet exit 0
$ python3 -B reports/round-71/accept-c.py --root .
LEG FAIL ROWS          missing=['S872', 'S873']
LEG FAIL CITED-LINES   exit=1 CITED-LINES: 1 finding(s) in 1 file(s)
ACCEPT-C-71: FAIL
COUNTER_EXIT=1
```

Consequence: `claims.json` claim C `kill_rule` ("any leg mismatch → the claim fails as declared") is not observable through the frozen counting command's exit status — only through its printed values. A green/red verdict on the command alone is unsound; `reports/round-71/accept-c.py` is the discriminating instrument and it does go red (exit 1) on the same mutation, so the counter is separable and the defect is confined to the frozen shell string. Recorded as a predicate/receipt-provenance defect, not a data defect.

## 5. FAIL — claim C's green receipt is not committed, and is the only receipt not re-stamped at HEAD

`controls.green` in `claims.json` requires "each claim's counting command is run on the landed bytes at the measured revision and its output **is committed as the receipt**".

```
$ git status --porcelain                     -> ?? reports/round-71/telemetry/measures-c.txt
$ git log --all --oneline -- reports/round-71/telemetry/measures-c.txt   -> (empty: never committed)
$ git ls-tree -r --name-only HEAD -- reports/round-71/telemetry/
   census-end.txt census-start.txt controls-c.txt controls-ca.txt controls-d.txt
   measures-ca.txt measures-d.txt quarantine-verdicts.md      <-- measures-c.txt ABSENT
$ ls /tmp/f32-clone/reports/round-71/telemetry/   (fresh clone) -> same list, no measures-c.txt
```

The receipt also stamps an older revision than every other claim's receipt:

```
measures-c.txt : stamped/evaluated/measured revision 8c203bd9..., tree ffb5c549...
measures-ca.txt: stamped/evaluated/measured revision 1d1b4325..., tree 84a304ba...
measures-d.txt : stamped/evaluated/measured revision 1d1b4325..., tree 84a304ba...
```

`8c203bd` is three commits behind HEAD (`1d1b432`, `3764c2d`, `14c88d9`). So the only surviving evidence of claim C's green measurement is an untracked, stale-stamped worktree file: a fresh clone (the artifact other rounds are scored from) carries no claim-C receipt at all. My re-run above shows the numbers still reproduce at HEAD, so this is a provenance/commit defect, not a data regression.

## 6. Minor — census receipt asymmetry

```
$ diff census-start.txt census-end.txt
30d29
< CENSUS_EXIT=0
$ grep -c W04 census-start.txt -> 28 ; grep -c W04 census-end.txt -> 28
```

`census-end.txt` omits the `CENSUS_EXIT=0` line that `census-start.txt` carries, so the receipt's extra claim `census exit=0 (W04=28 same as base)` is not evidenced by the end receipt's own bytes (only the 28 W04 lines are). The `census exit=0` line in `measures-c.txt` is also not a leg of either the frozen command or `accept-c.py` — it is an ungraded rider on the receipt.

## 7. Notes (not defects of claim C)

- `python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material` → `CITED-LINES: 111 finding(s) in 36 file(s)`, exit 1. Pre-existing across the partition (masks-masquerade, pastoralism, hunting-foraging, games-play); claim C's leg scopes the new entry only, which is clean (0 findings). Flagged for the entry-quality seats, not as a C leg failure.
- `git diff --name-only b94a543..HEAD -- reports/round-69 reports/round-70` → only the six round-70 telemetry receipts (claim Ca's declared surface); `reports/round-69/*.py` bytes untouched. Consistent with `freeze_rule`.

## Verdict

| Check | Result |
|---|---|
| Frozen C counting command re-run at HEAD `14c88d9` in fresh clone: `36 / 243 / 797 / CITED-LINES 0 findings`, exit 0 | **PASS** |
| Independent re-derivation of the same numbers (797 rows, 797 distinct ids, 784 base, 13 new S861–S873 inside `## Registry`, all mined + used-by entry) | **PASS** |
| Base before-state control at `b94a543` (empty word-bounded sweeps, unbound false-match at `funerary-material-culture.md:4`, 35/242/784) | **PASS** |
| Frozen command's exit code is a valid acceptance signal | **FAIL** (masked by trailing `test -f`; exit 0 on a 795-row + lint-failing tree) |
| Claim C green receipt committed as required by `controls.green` | **FAIL** (`measures-c.txt` untracked, never in history, absent from fresh clone; stamped 8c203bd vs HEAD) |
| `census-end.txt` evidences its `census exit=0` claim | **MINOR** (no `CENSUS_EXIT=0` line) |

Claim C's measured content is reproducible at HEAD; its receipt custody is not.
