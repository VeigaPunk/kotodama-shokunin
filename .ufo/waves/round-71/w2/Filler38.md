# Filler38 — round 71 wave 2 (variant 37): frozen Ca counting command re-run in a fresh clone

Verdict: **FAIL** (one of six legs). Claim Ca's frozen `counting_command` (from
`reports/round-71/claims.json`, frozen at 65ff151) exits 0. It hits target on five
legs, but its quarantine-verdict leg prints `0` against a target of `21`. The data is
fine (the table carries 21 valid verdict rows). The failure comes from the frozen awk
leg, which reads the wrong fields. The landed PASS receipt comes from a different
counter, `accept-ca.py`, which was created after the freeze.

Claim choice: variant 37 mod 3 = 1 over [C, Ca, D] → Ca.

## Setup (observed)

- Fresh clone: `git clone -q --no-local /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/f38.DzRM/k`
- Clone HEAD = lane HEAD = `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`; clone `git status --short` is empty.
- Command extracted verbatim with `json.load(...)['claims'][Ca]['counting_command']`, sha256
  `91cf60f81ed1116297d36fbe5198bfb2dcb02b417df782441b9503d0bb11c6a8`. Its bytes are identical at
  65ff151 (the re-freeze) and at HEAD, so the command was not edited after the freeze.
- Shell: `bash /tmp/f38.cmd` (the command needs bash for brace expansion).

## Exact output (cwd = clone root)

```
      6 6
1
25
1
1
0
EXIT=0
```

## Legs vs target

| leg | printed | target | result |
|---|---|---|---|
| per-file 17/19 header lines (six receipts) | `6 6` (6 files × 6 lines) | 36 matches, each file 6 | PASS |
| `grep -c acc2d614 corpus/SOURCES.md` | 1 (line 815, the S860 row) | >=1 | PASS |
| round-70 Gate quote words (`NR==13 $4`) | 25 | <=25 | PASS |
| `round-70 trend-correction` in SCORECARD.md | 1 | >=1 | PASS |
| `rejected this round:` in round-71 lesson | 1 | >=1 | PASS |
| quarantine verdict rows | **0** | **21** | **FAIL** |

The claim's kill rule says "any leg mismatch -> the claim fails as declared … or the
verdict table not carrying 21 nonempty rows". By the frozen command, **ACCEPT-CA-71 fails**.

## Root cause of the 0 (observed)

The frozen leg is
`awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}' reports/round-71/telemetry/quarantine-verdicts.md`.

The table rows look like `| S776 | PRESENT | … |`. With `-F'|'` and a leading pipe, `$1` is
empty, `$2` is ` S776 ` and `$3` is ` PRESENT ` (with padding). Field probe:
`awk -F'|' '/S[0-9]+/ {printf "NR=%d $1=[%s] $2=[%s] $3=[%s]\n",NR,$1,$2,$3}' …` shows
`$1=[]` on all 21 table rows (NR 14–34). The only lines where `$1` matches `S[0-9]+` are
prose lines (NR 9 and NR 37), and those have an empty `$2`. So the leg can never count a
table row. It is off by one field and has unanchored padding.

There are two defects in the frozen counter itself:
1. Wrong field index: `$1`/`$2` should be `$2`/`$3`.
2. `^…$` anchors with no whitespace trim, so it would still print 0 even with the index fixed.

A probe that is **not** the frozen command (trimmed `$2`/`$3`) prints `21`. That matches the
file's own tally line (PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5 = 21). The table is correct;
the counter is broken.

## Do-nothing control cannot discriminate this leg (observed)

`reports/round-71/telemetry/controls-ca.txt` (base b94a543c) records `verdict-labels:` as empty.
The frozen leg prints 0 on any table with a leading `|`, so it fails at base and also at the
after-state. As a gate this leg is constant: it cannot tell the base tree from the landed tree.

## The landed receipt uses a post-freeze counter (observed)

- `reports/round-71/telemetry/measures-ca.txt` prints `ACCEPT-CA-71: PASS` /
  `QUARANTINE: rows=21 …`, stamped at `1d1b432`. It comes from `reports/round-71/accept-ca.py`,
  not from the frozen `counting_command`.
- `git cat-file -e 65ff151:reports/round-71/accept-ca.py` gives `fatal: … not in '65ff151'`
  (exit 128). `git log -- reports/round-71/accept-ca.py` shows only `1d1b432` (08:38:53).
  `git merge-base --is-ancestor 65ff151 1d1b432` exits 0. So `accept-ca.py` was created
  **after** the freeze, in the same commit that landed the Ca data.
- Run at HEAD in the clone, `python3 -B reports/round-71/accept-ca.py` prints six `LEG PASS`
  lines, then `ACCEPT-CA-71: PASS`, `EXIT=0` (QUARANTINE `rows=21 unique-ids=21 labels-ok=True`).
- `claims.json` `controls.green` requires "each claim's counting command is run on the landed
  bytes … and its output is committed as the receipt". No committed receipt carries the frozen
  command's output, so the frozen command's FAIL is not recorded anywhere in the lane.
- [INFERENCE] This is the kumitate r42 class the freeze rule names: the receipt is reached by
  a counter written after data landed, and the frozen counter would score FAIL.

## Predicate leg outside the counting command

The predicate and target require `python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md`
to exit 0 with 0 findings. The frozen `counting_command` does not run it. Running it separately
in the clone prints `GATE_QUOTES: 0 findings`, exit 0, so that leg passes.

## Remaining unknowns

- Whether L1 treats the frozen shell command or `accept-ca.py` as the authoritative counter is
  a ruling for L1. Read literally, the freeze rule and `controls.green` point to the shell command.
- I did not test claims C or D (out of scope for this variant).

## Tooling

No installs or updates. The scratch clone `/tmp/f38.DzRM` and `/tmp/f38.cmd` were removed after the run.
