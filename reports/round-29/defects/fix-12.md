# R29-O12 — stale v2/v3 successor pins and the duplicate r26 v3 row

- Date: 2026-10-18.
- Status: **v2 tail closed; v3 tail superseded, with a stale duplicate row retained historically.**

## Defect and disposition

The R25 O queue carried a stale v2 projector pin and a stale v3 packet/read-set pin. R26 produced successor rows rather than editing their filed R20 sources. Its full `pin-repoint-check.py --check` was measured exit 0 with **17/17** controls on 2026-10-18 (`reports/round-26/remainders/pins.md` §3); the paired stale rows replay red and the new v2/v3 rows replay green.

The R26 closing regression then found a wiring defect in its own v3 remainder: `reports/round-26/remainders/v3-baseline-r26/expected.json` was stale while the sibling `reports/round-26/register/v3-baseline-r26/expected.json` was live-correct. The round-26 regression's dated command `python3 reports/round-26/remainders/pin-repoint-check.py --check` exited 1 because `new-v3-row-replays-green` failed; this was not silently treated as green. Later R27/R28 successor rows supersede that stale duplicate. Do not rewrite it or present its historical red as a current v3 failure.

## Independent current controls

At **2026-10-18 17:59:23−03:00**, `python3 reports/round-26/remainders/pin-repoint-check.py --selftest` exited 0, **5/5** static controls. At the same timestamp, `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` exited 0 on the current default baseline: fields **16/16**, glossary **20/20**, findings **0**, links **105/105**, claims **27**, statuses **16/7/4**. The selftest does not re-run the historical pin replay; the current handoff command confirms the user-facing default, not the stale R26 row.

## Disposition / route

Keep the R20 rows and the R26 duplicate as filed evidence. The machine ledger should name the R26 duplicate as superseded by the later baseline, rather than claiming the R26 replay control was green at its closing stamp. If a historical row is ever re-measured, run its checker in an isolated clone and preserve its original receipt.