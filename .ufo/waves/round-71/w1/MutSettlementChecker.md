# MutSettlementChecker — round-71 wave-1 mutation probe (round-70 D surface)

- Seat: `L1Kotodama71.MutSettlementChecker` (UFO-FSD mutation tester, leaf — no delegation)
- Date: 2026-10-25
- Target: `tools/check-supersession-settlement.py` at lane HEAD (round-70 claim D / ACCEPT-D-70 surface)
- Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- Probe: 4 mutations applied to scratch copies **only**; lane tool bytes never touched (restoration evidence below).

## 1. Goal and method

Round-70 claim D asserts `tools/check-supersession-settlement.py --selftest` prints `SELFTEST: 10/10` exit 0
with three new behaviors: (1) `missing_paths` counts UNIQUE missing files across multi-path used-by cells;
(2) duplicate path references across rows count once; (3) malformed registry rows are reported via
`MALFORMED-ROW` lines and a malformed target no longer crashes.

Method: copy the committed tool into scratch `/tmp/mut-settlement/pristine.py`; run baseline selftest; apply
four single-point mutations; run the same selftest on each mutant; record outputs, exit codes, and
before/after SHA-256 hashes. Verdicts: **killed** = selftest fails vs baseline; **survived** = selftest
still exits 0; **inconclusive** = baseline itself fails (baseline passes, so none).

## 2. Baseline (committed tool)

```
$ sha256sum tools/check-supersession-settlement.py  → 1e01c76a12aaa3f2dc8454f73212aed88206914999477abfb6f7ff58cc12564f
$ python3 -B pristine.py --selftest → SELFTEST: 10/10, EXIT=0
```
All 10 cases PASS: pending-detected, settled-active, settled-retired-closed, settled-split, ledger-clean,
ledger-inconsistent-rejected, unreadable-exit-2, missing-unique-file, malformed-rows-report,
malformed-target-no-crash. (Base control in `reports/round-70/telemetry/controls-d.txt` compares against the
pre-hardening 7/7, matching the claim's before-state.)

## 3. Mutants and verdicts

| # | Mutation (behavior probed) | Exact edit | Selftest result | Verdict |
|---|---|---|---|---|
| M1 | Drop malformed-row reporting (behavior 3) | Delete the `MALFORMED-ROW` print loop in `scan()` (`for rid in sorted(... if r.get("malformed")): print(...)`) | `FAIL malformed-rows-report` → `SELFTEST: 9/10`, EXIT=1 | **killed** |
| M2 | Switch `missing_paths` to per-pair counting (behavior 1) | Replace unique-set comprehension `{p for _, p in stale if not exists(...)}` with per-pair list `[p for _, p in stale if not exists(...)]` | `FAIL missing-unique-file` → `SELFTEST: 9/10`, EXIT=1 | **killed** |
| M3 | Drop the missing-unique-file case (the f6 test case) | Delete the whole f6 block in `selftest()` (fixture build + `scan` + `chk("missing-unique-file", ...)`) | `SELFTEST: 9/9`, EXIT=0 — no check fails; case count/output line changes (10/10 → 9/9) | **survived** (changes case outputs) |
| M4 | Allow a duplicate path count in `missing_paths` (behavior 2) | Replace unique-set with occurrence count (duplicates counted): `Counter(p for _, p in stale if not exists(...))`, `missing_paths = sorted(miss.elements())` | `FAIL missing-unique-file` → `SELFTEST: 9/10`, EXIT=1 | **killed** |

Hashes: pristine `1e01c76a…`; M1 `2e2d1f89…`; M2 `951f402718…`; M3 `9478ea5112…`; M4 `2c7858894f…`.
All mutant selftest runs used `python3 -B`.

### Detailed outputs

- **M1** — all checks PASS except `FAIL malformed-rows-report` (f7 output no longer contains
  `MALFORMED-ROW S099` / `MALFORMED-ROW S100`); `malformed-target-no-crash` still PASS (exit path intact).
  `SELFTEST: 9/10`, EXIT=1.
- **M2** — all checks PASS except `FAIL missing-unique-file`. Direct scan on the f6 fixture confirms the count
  flip: pristine `missing_paths=1` → mutant `missing_paths=2` (same `usedby_paths=3`, `pending=0`, EXIT=0).
  `SELFTEST: 9/10`, EXIT=1.
- **M3** — all 9 remaining checks PASS; `SELFTEST: 9/9`, EXIT=0. The receipt line differs from committed
  `10/10` (a grader matching `SELFTEST: 10/10` sees the change), but no assertion detects the removal of the
  case itself.
- **M4** — identical observable behavior to M2 on f6 (`missing_paths=2`), `FAIL missing-unique-file`,
  `SELFTEST: 9/10`, EXIT=1. M2 and M4 are distinct byte-mutations probing the same uniqueness line: claim
  behaviors (1) and (2) share one implementation (the set-comprehension in `scan`), so both mutations kill the
  same case.

## 4. Finding

The round-70 D selftest is **not vacuous** for the three claimed behaviors:

- Behavior (3) — malformed-row reporting — is genuinely pinned: removing the report kills `malformed-rows-report` (M1 killed).
- Behavior (1)/(2) — unique `missing_paths` counting — is genuinely pinned: both the per-pair revert (M2) and
  the duplicate-count allowance (M4) are killed by `missing-unique-file`.
- Removing the test case itself (M3) is not detected by the remaining checks (it survives), but it changes the
  case outputs: the receipt line becomes `SELFTEST: 9/9`, so the claimed `10/10` string no longer holds —
  the kill rule's "SELFTEST != 10/10" leg would fire on the print, though exit code alone would not.

Observation (not a mutant): the `SETTLEMENT` summary's `usedby_paths={len(stale)}` counts per-pair with
duplicates and is not pinned by any selftest case; only `missing_paths` uniqueness is asserted.

## 5. Restoration evidence

- Lane tool untouched: `sha256sum tools/check-supersession-settlement.py` after all runs =
  `1e01c76a12aaa3f2dc8454f73212aed88206914999477abfb6f7ff58cc12564f` (identical to pre-probe).
- No writes to the lane repo or sibling lanes; scratch copies live in `/tmp/mut-settlement/` (disposable);
  f6 scan fixture built in scratch only.
- No tools installed (no installs/updates to record; `python3` already present).
