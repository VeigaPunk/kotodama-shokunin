# Filler35 — round 71 wave 2 (variant 34): frozen Ca counting command re-run in a fresh clone

Seat: L1Kotodama71.Filler35 (falsify filler, leaf, read-only on the lane).
Claim picked: **Ca**. Variant 34 mod 3 = 1, which selects `claims[1]`.

## Verdict

**FAIL (one leg).** The frozen Ca `counting_command` runs at lane HEAD and exits 0, but its verdict-table leg prints `0` where the target is 21. The table actually holds 21 well-formed rows. The leg is structurally vacuous: its awk can never count a markdown pipe-table row. Under the declared kill rule, "the verdict table not carrying 21 nonempty rows" is a leg mismatch, so the claim fails as declared. The committed PASS receipt comes from a different counter, `accept-ca.py`.

## Setup (observed)

- Lane HEAD: `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` ("round-71: wave-2 spec/plan/dispatch evidence (40 seats)").
- Fresh clone: `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/f35.7Ibg/clone`. `git status --porcelain | wc -l` printed 0, so the clone is clean. The lane worktree's untracked `reports/round-71/telemetry/measures-c.txt` is not in the clone.
- I extracted the command verbatim from the frozen declaration: `python3 -c "import json;print([c for c in json.load(open('reports/round-71/claims.json'))['claims'] if c['id']=='Ca'][0]['counting_command'])" > cmd.sh`.
  - `cmd.sh` sha256: `91cf60f81ed1116297d36fbe5198bfb2dcb02b417df782441b9503d0bb11c6a8`
  - `claims.json` sha256: `73d3ad73120a0c13ce99e4498f710e3a265a41f3b34b848a57d460a44087b9be`. It was last touched by `65ff151` (the re-freeze, before any data landed).
- Run: `bash cmd.sh > out.txt 2> err.txt; echo EXIT=$?`, using GNU Awk 5.4.1.

## Exact output

```
EXIT=0
---STDOUT---
      6 6
1
25
1
1
0
---STDERR---
(empty)
```

## Leg-by-leg against the declared target

| leg | printed | target | result |
|---|---|---|---|
| per-file 17/19 header (`sort \| uniq -c`) | `6 6`, meaning 6 files × 6 lines = 36 | 36 | PASS |
| `grep -c acc2d614 corpus/SOURCES.md` | 1 | >=1 | PASS |
| round-70 Gate quote words (`NR==13 $4 \| wc -w`) | 25 | <=25 | PASS (at the boundary) |
| `round-70 trend-correction` in SCORECARD.md | 1 | >=1 | PASS |
| `rejected this round:` in lesson round-71 | 1 | >=1 | PASS |
| quarantine verdict rows (awk) | **0** | 21 | **FAIL** |

## Root cause of the FAIL leg (observed)

- The frozen awk is `awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/'`. The table rows look like `| S776 | PRESENT | … |`. With `-F'|'`, a leading pipe makes `$1` empty and `$2 = " S776 "`. I confirmed this with an awk field dump: `[$1=] [$2= S776 ] [$3= PRESENT ]`. The `$2` anchors also reject the padding spaces.
- Minimal repro: `printf '| S1 | PRESENT | x |\n' | awk …` prints `0`, while `printf 'S1|PRESENT|x\n' | awk …` prints `1`.
- The data is fine. `rg -c '^\| *S[0-9]+' quarantine-verdicts.md` gives 21. A shifted, trimmed awk (`$2` for the id, trimmed `$3` for the verdict) also gives 21.
- The do-nothing control `reports/round-71/telemetry/controls-ca.txt` prints `verdict-labels: ` (empty) because the file was absent at base. The awk was never run against any table, so the control could not reveal that this leg can only ever print 0.

## Receipt substitution (observed)

- The committed `reports/round-71/telemetry/measures-ca.txt` (stamped at `1d1b432`, counter sha256 `3f3f63fc…`) reports `ACCEPT-CA-71: PASS … QUARANTINE: rows=21`. That is the output of `reports/round-71/accept-ca.py`, not of the frozen shell `counting_command`. In the clone at HEAD, `python3 -B reports/round-71/accept-ca.py --root .` prints `ACCEPT-CA-71: PASS` with all legs PASS (`rows=21 unique-ids=21 labels-ok=True`) and exits 0. Its sha256 `3f3f63fc628aeac1fb9d076a77c6840161bbeacdde065294f01b13ea5139eb46` matches the receipt.
- `claims.json` `controls.green` says "each claim's counting command is run on the landed bytes … and its output is committed as the receipt". The receipt is not the counting command's output. Running the counting command itself gives 0 on the verdict leg.
- The Ca target also names "check-gate-quotes exit 0 with 0 findings", but the frozen `counting_command` never invokes `tools/check-gate-quotes.py`. I ran it separately: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md` printed `GATE_QUOTES: 0 findings` and exited 0. That leg holds, but only outside the frozen command.

## Separation

- **Observed:** the exact output and exit code above, the awk field split, the repro, the 21 real rows, the receipt's provenance (`accept-ca.py`, matching sha), and `check-gate-quotes` exit 0.
- **Inference:** the Ca landings are substantively correct. Both the data and `accept-ca.py` agree on 21/21. The defect sits in the frozen shell counter, and the PASS receipt hides it by swapping counters.
- **Routing (for Main, not a fix):** the freeze rule forbids editing the frozen command. Either record ACCEPT-CA-71 as failing its declared verdict leg, or log a declared counter defect with old→new in the lesson or corrections file and re-declare in a later round. Do not silently rely on `accept-ca.py` as "the counting command".
- **Unresolved:** I did not check whether other seats' Ca receipts or the scorecard cite the shell command's output, and I did not re-run the C or D counting commands. Both are outside this seat's single-command scope.

## Tooling

No installs or updates.
