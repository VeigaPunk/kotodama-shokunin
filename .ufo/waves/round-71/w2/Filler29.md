# Filler29 — round 71 wave 2 (variant 28): frozen counting command re-run, fresh clone

Seat: `L1Kotodama71.Filler29` (falsify, leaf). Findings only; no lane bytes edited except this file.
Tooling: no installs or updates.

## Selection

The seat prompt does not pin a claim. Rule applied: variant 28 mod 3 = 1, which selects the
second claim in `reports/round-71/claims.json` order (C, Ca, D): **claim Ca**.

## Setup (observed)

```
T=$(mktemp -d /tmp/f29.XXXX); git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$T/k"; cd "$T/k"
# HEAD=14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6  porcelain-dirty=0
python3 -c "import json;print(json.load(open('reports/round-71/claims.json'))['claims'][1]['counting_command'])" > "$T/cmd.sh"
# sha256(cmd.sh) = 91cf60f81ed1116297d36fbe5198bfb2dcb02b417df782441b9503d0bb11c6a8
bash "$T/cmd.sh"
```

The command was taken verbatim from `claims.json`, not retyped, and run under `bash` because the
first leg uses brace expansion. Freeze check: `claims.json` was last touched in 65ff151
(re-freeze, 08:23). Every data-landing commit comes after it (498db73, 8c203bd, 1d1b432, 3764c2d),
and b94a543 (base) is an ancestor of HEAD. So the command run here is the frozen one.

## Exact output — frozen Ca counting command at HEAD 14c88d9

```
      6 6
1
25
1
1
0
```
stderr: empty. **EXIT=0** (exit code of the final `awk`; the command does not gate on its legs).

## Leg-by-leg against the frozen target

| leg | output | target | verdict |
|---|---|---|---|
| per-file 17/19 header, 6 receipts | `6 6` (6 files, each with 6 matches; no `MISSING:`) | 6 x 6 = 36 | PASS |
| S860 names acc2d614 | `1` (SOURCES.md:815) | >= 1 | PASS |
| round-70 Gate quote words (lesson NR==13, `$4`) | `25` | <= 25 | PASS |
| SCORECARD `round-70 trend-correction` | `1` (SCORECARD.md:1393) | >= 1 | PASS |
| lesson-71 `rejected this round:` | `1` (round-71.md:33) | >= 1 | PASS |
| quarantine verdict rows | `0` | 21 | **FAIL** |
| `check-gate-quotes.py` exit 0 / 0 findings | not run by the command | exit 0, 0 findings | **NOT MEASURED by the frozen command** |

**Result: the frozen Ca counting command does NOT reach its declared target at HEAD.** Its last
leg prints 0, not 21. Under the claim's own kill rule ("the verdict table not carrying 21 nonempty
rows" means any leg mismatch fails the claim), the shell counter as declared reads FAIL.

## Root cause (observed + derived)

`reports/round-71/telemetry/quarantine-verdicts.md` is a standard markdown table with a leading
pipe (`| S776 | PRESENT | ... |`). With `awk -F'|'`, `$1` is the empty string before the first
pipe, `$2` is ` S776 ` and `$3` is ` PRESENT ` (with padding spaces). The frozen predicate
`$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/` has two defects:

1. It is off by one field.
2. It is anchored without trimming spaces.

So it can match no row of a leading-pipe table. Diagnostics, all run in the same clone:

- `awk -F'|' '$1 ~ /S[0-9]+/' quarantine-verdicts.md | wc -l` → `2`. These are prose lines
  (S778, S859/S860), not table rows, and `$2` is empty on both.
- Corrected field/trim (diagnostic only, NOT the frozen command):
  `awk -F'|' '$2 ~ /S[0-9]+/ {gsub(/ /,"",$3); if ($3 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/) n++} END{print n+0}'`
  → `21`. The data does satisfy the target; the frozen counter cannot see it.

This is a vacuous leg: it reads 0 both on the base tree, where `controls-ca.txt` has
`verdict-labels:` empty, and on the landed tree. So the do-nothing control and the landed state are
the same on this leg, and the leg cannot tell them apart.

## Contrast with the committed receipt

`reports/round-71/telemetry/measures-ca.txt` (stamped 1d1b432) reports `ACCEPT-CA-71: PASS` and
`QUARANTINE: rows=21`. That receipt was not produced by the frozen `counting_command`. It came from
`reports/round-71/accept-ca.py`: the counter sha `3f3f63fc…eb46` in the receipt header matches
`sha256sum reports/round-71/accept-ca.py` in the clone. Re-run in the fresh clone:

```
python3 -B reports/round-71/accept-ca.py
LEG PASS V70-1 … LEG PASS V70-2 … LEG PASS V70-3 (words=25) … LEG PASS V70-4 … LEG PASS V70-5 …
LEG PASS QUARANTINE  rows=21 unique-ids=21 labels-ok=True (want 21/21/True)
ACCEPT-CA-71: PASS
EXIT=0
```

`python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md` → `GATE_QUOTES: 0 findings`,
EXIT=0. The predicate's gate-quotes leg holds, but only when run separately.

## Findings

- **F29-1 (FAIL, frozen-counter vs receipt divergence):** the `counting_command` frozen in
  `claims.json` for Ca prints `0` on the quarantine leg at HEAD 14c88d9, where the target is 21.
  The PASS receipt comes from a different instrument (`accept-ca.py`). The `controls.green` rule
  says "each claim's counting command is run on the landed bytes … and its output is committed as
  the receipt". As stated, that rule is not met for Ca: the frozen command's output is not the
  receipt, and it would not pass. Confidence: high (direct observation; awk field semantics).
- **F29-2 (gap):** the frozen command omits the `check-gate-quotes.py` leg named in the predicate
  and target, and it exits 0 whatever the leg values are. Its exit code carries no verdict.
  Confidence: high.
- **F29-3 (PASS):** the other five legs of the frozen command meet target at HEAD.
- **Data state:** the underlying Ca after-state appears real. With the corrected parse, the
  verdict table holds 21 labelled rows (10/6/5), and `accept-ca.py` passes in a fresh clone. The
  defect is in the instrument, not in the landed data. [INFERENCE: whether accept-ca.py's checks
  are equivalent to the frozen sentence beyond these legs was not audited by this seat.]

## Remaining unknowns

- Whether the lane's rules treat `accept-ca.py` as the authoritative "counting command" for Ca,
  which would supersede the frozen shell string. `claims.json` names only the shell string, and the
  freeze rule forbids editing it after scoring.
- Claims C and D were not re-run by this seat (variant scope = one command).
