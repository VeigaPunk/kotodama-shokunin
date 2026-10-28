# ScoutLedgerA findings

Base: `211f9526800906e0c585d878d265c37e5e090c15`. Draft read first; no draft edits. I found one candidate verified RED (below), not the required four; remaining candidates are intentionally not fabricated. A-01's statement is present at the cited line and its observe command is in the allowed argv vocabulary.

## A-01 — verified RED

Statement location/text: `SCORECARD.md:1559` — “C was re-measured at `3c2893bf87f5247e8d2d7af59d1ec1e11895647b`: `ACCEPT-C-76: FAIL legs=11/13`, still only ROWS and COLLCHECK red (`reports/round-76/telemetry/measures-c-final.txt).”

Observed command:
`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -o -E '^# measured revision \\(lane main\\): [0-9a-f]+' 211f9526800906e0c585d878d265c37e5e090c15 -- reports/round-76/telemetry/measures-c-final.txt`

Raw output:
`211f9526800906e0c585d878d265c37e5e090c15:reports/round-76/telemetry/measures-c-final.txt:# measured revision (lane main): cb4f6c6a550b3233f3c12a266e72dee6f4bc126b`

Parse `^# measured revision \\(lane main\\): ([0-9a-f]+)$` gives `cb4f6c6a550b3233f3c12a266e72dee6f4bc126b`, unequal to stated `3c2893bf87f5247e8d2d7af59d1ec1e11895647b`. `measures-c-final.txt` actually records the cb4f6c6 measurement, while SCORECARD attributes it to 3c2893b. Pair JSON: `.ufo/waves/round-77/w1/stage/ScoutLedgerA/pairs.json`.

## Sweep evidence / other observations

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:LOG.md | grep -n '^## Round 76'` → raw `4331:## Round 76 (2026-10-27, hyaku run 10, L1 KotodamaR76, attempt 1) — author-side, pending non-author closure`.

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -c -E '^' 211f9526800906e0c585d878d265c37e5e090c15 -- .ufo/waves/round-76/assimilation/reg-ids .ufo/waves/round-76/assimilation/staged-ids .ufo/waves/round-76/assimilation/collisions` → raw counts: collisions 35; reg-ids 817; staged-ids 132. This matches round-76 lesson line 72.

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -c -E '^' 211f9526800906e0c585d878d265c37e5e090c15 -- .ufo/waves/round-76/w1/stage/ScoutQuarantine/quarantine-slice` → raw `...quarantine-slice:21`; matches lesson line 42's count.

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:reports/round-76/telemetry/measures-c-final.txt | grep -E 'measured revision|ACCEPT-C-76'` → raw `# measured revision (lane main): cb4f6c6a550b3233f3c12a266e72dee6f4bc126b` and `ACCEPT-C-76: FAIL legs=11/13`. The corresponding SCORECARD:1561 cb4f6c6 attribution matches this receipt.

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:reports/round-76/telemetry/measures-c-final-c7.txt | grep -E 'lands |ACCEPT-C-76'` → raw command names lands `b40113eb3961bce44fba6b066ce6a656f0e16fec`, output `ACCEPT-C-76: FAIL legs=11/13`; matches SCORECARD:1565 and lesson:97.

Other checks not run: a complete search/verification capable of producing four valid RED pairs; no claim that the four-pair acceptance condition is met. No tools installed.
