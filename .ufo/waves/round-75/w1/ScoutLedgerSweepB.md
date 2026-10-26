# ScoutLedgerSweepB — round-75 draft ledger sweep

Base: `f556d1049fe651d3d63975600b13acd9fb686f15`. Draft files read only; no code or ledger edits made.

## Observe results (L75-05..L75-11)

| Pair | Command result at base | Assessment |
|---|---|---|
| L75-05 | `git grep -c "was absent from the page it was bound to" f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/lessons/round-74.md` → `f556d1049fe651d3d63975600b13acd9fb686f15:corpus/lessons/round-74.md:1` (exit 0) | Observed count `1`, equals `expected_after`; differs from the stated prose token, so red. Anchor exists at line 37. |
| L75-06 | `git grep -c "was the Sowers-Wills clause, absent from this page" f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/lessons/round-74.md` → `f556d1049fe651d3d63975600b13acd9fb686f15:corpus/lessons/round-74.md:1` (exit 0) | Observed count `1`, equals `expected_after`; differs from stated prose token, so red. Anchor exists at line 38. |
| L75-07 | `git grep -c "re-pointed read path" f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/QUALITY.md` → **empty stdout**, exit 1 | Zero matches is intended/`expected_after` 0, but the specified `:([0-9]+)$` parse has no output token to extract. Thus the command is not directly parseable as a numeric `0` from stdout; flag for counter treatment. It is an absence observation, which the draft status says is never kept. Anchor exists at lesson line 208. |
| L75-08 | Fleet-root command `git grep -c "see the closing line below" 3a7401609325341eb3fe0efd42d0eec29d06be3c -- .ufo/reports/round-74/kotodama.md` → `3a7401609325341eb3fe0efd42d0eec29d06be3c:.ufo/reports/round-74/kotodama.md:1` (exit 0) | Observed count `1`, equals `expected_after`; differs from stated hash-promise token, so red. Line 20 anchor exists in the fleet-pinned blob. |
| L75-09 | `git show f556d1049fe651d3d63975600b13acd9fb686f15:reports/round-73/telemetry/selftest-r3.txt` prints the committed receipt; line 6 ends `... min-pairs gate FAI`. | Observation token from `min-pairs gate (\S+)$` is `FAI`, equals `expected_after`, and differs from stated `FAIL`, so red. **Anchor absent as stated:** exact text `min-pairs gate FAIL` is not in the base file (exact `git grep -c` returns empty stdout, exit 1); line 6 has only `FAI`. The draft ledger's stated-text-at-anchor requirement is therefore not met literally. Also the listed rederive `tail -c 4` returns the file's final `son\n` (from `json`), not `FAI`; it does not substantiate this token. |
| L75-10 | Running `ls .ufo/waves/round-74/w2` at lane root, then counting names ending `.md` → `44`; directory listing confirms 44 `.md` names. | Observed `44`, equals `expected_after`, differs from stated `43`, so red. The same relative `ls` path does not exist at fleet root; the lane root is the applicable context for this lane's wave reports. Line 4318 of base `LOG.md` contains the stated historical count. |
| L75-11 | `git grep -c "SELFTEST: 10/11" f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-72` → **empty stdout**, exit 1 | Intended zero matches/`expected_after` 0, but the specified `:([0-9]+)$` parse has no stdout token to extract. This is an absence observation, which the draft status says is never kept. `SKILL.md:701` contains the stated text. |

## Requested anchor/evidence checks

At the base lesson blob, lines 37 and 38 contain the exact disputed clauses for L75-05 and L75-06, respectively; line 208 contains `... **QUALITY 23 addendum**: a re-pointed read path`. The fleet blob at `3a7401609325341eb3fe0efd42d0eec29d06be3c:.ufo/reports/round-74/kotodama.md:20` contains `Lane pushed hash: see the closing line below`.

The full base `selftest-r3.txt` line 6 ends `min-pairs gate FAI` (truncated `FAIL`); its file tail is unrelated to that line: `tail -c 4` yields `son\n`. The `reports/round-72` search for `SELFTEST: 10/11` has no matches (exit 1).

At base, `reports/round-74/evidence/S883.txt` contains `非凡特性来自最初造物主` once (`git grep -c` reports `...S883.txt:1`); `S884.txt` contains `这个我肯定考虑过` once (`...S884.txt:1`). Both requested evidence spans are present.

## Items requiring attention

- L75-09's `stated_text` is absent at its claimed base anchor: the receipt says `FAI`, not `FAIL`. Its `tail -c 4` rederive also does not yield the claimed observation.
- L75-07 and L75-11 are zero-match observations whose commands produce empty stdout and exit 1, rather than a parseable `:0` line; both appear to be absence-observation candidates under the draft's own stated rule.
- No other requested anchor was absent; L75-05..06 and L75-08..11 observations are red under the stated-vs-observed tokens (with the above parse/anchor caveats).