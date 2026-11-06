# ExecGraderV9 — round-97 w1, lane kotodama (attempt 1)

Seat: ExecGraderV9. Task: grader v8 -> v9 in place at `tools/check-advance-evidence.py`, closing the seven CriticO96 survivor classes (claims.json Claim O). Single writer of the lane tool file. No commits.

## Result summary

- v8 sha256 `f29ab0139b4590fa8da7232a7372574675ef60763c475eea003006eb1dbcd9c0` (verified on the copied base, `stage/ExecGraderV9/v8-base.py`).
- v9 sha256 `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b` (differs from v8: leg O0 pass).
- All seven classes closed by name; battery97 `survivors=0 unnamed=0 refused=31 traceback=0 clean=2`; selftest `SELFTEST PASS 155/155` rc 0; REG lines 34/34 byte-identical to `reports/round-95/controls/reg-v5.txt`.
- No class left open.

## Diagnostics added (raise sites in tools/check-advance-evidence.py)

| Diagnostic | Class(es) | Raised at | Message shape |
|---|---|---|---|
| `VERDICT-CTRL` | CR1 (U+000D), US1 (U+001F), NUL1 (U+0000) + remaining C0 | `_refuse_verdict_channel`, lines 318-320 | `verdict token carries control character U+XXXX (VERDICT-CTRL)` |
| `VERDICT-SEPARATOR` | OGH1 (U+1680), IS1 (U+3000) + remaining Zs | `_refuse_verdict_channel`, lines 321-323 | `verdict token carries space separator U+XXXX (VERDICT-SEPARATOR)` |
| `HEADING-COMBINING` on `FAIL TOPIC` (rc 1) | CM1 (Mn on numbering token), CMW2 (Mn in phrase word) | `grade_entry` TOPIC block, line 740 | `h2 heading carries a combining mark (HEADING-COMBINING)` |

Token names match the frozen battery97 manifest lists (`VERDICT-CTRL`, `VERDICT-SEPARATOR`, `HEADING-COMBINING`, `LEG FAIL TOPIC`); the task text's "such as VERDICT-CONTROL" is realized as VERDICT-CTRL to satisfy the frozen driver, each refusal naming the codepoint as required.

Preserved by construction:
- Tabs keep `VERDICT-TAB` (U+0009 in the skip set); NBSP/VT/FF/line-separator/NEL/ANSI keep their v8 names (raised before the new loop).
- Plain U+0020 stays a legitimate verdict spacing (the anchored rule reads `NOT LOCATED`) — caught and fixed after the first battery run regressed REG line A5c; see "Repairs".
- CR-only line breaks still parse as line breaks (`splitlines`), pinned clean by `round-97 CR-only line breaks do not sever or hide dispositions` (rc 0, PASS 9/9); a lone U+000D only refuses when it sits inside the verdict window (`LOCA<CR>TED`).
- ZWNJ U+200C (Cf) stays benign: battery controls `G0` and `ZWNJ1` both CLEAN rc 0.
- Precomposed accents (category Ll) are unaffected by the heading check; only Mn/Me in h2 headings refuse.

## Selftest

Command: `python3 -B tools/check-advance-evidence.py --selftest --work /fast/scratch/hyaku/kotodama-r97/ExecGraderV9/selftest` — rc 0, `SELFTEST PASS 155/155`, 0 BAD lines. All 147 v8 pins kept; 8 new pins (lines 1908-1946): CR1, US1, NUL1, OGH1, IS1 (each asserts the token name AND the codepoint string, rc 2), CM1 and CMW2 (rc 1, `FAIL TOPIC` + `HEADING-COMBINING`), plus the CR-only-linebreak clean control. N = 155 >= floor 154.

## Battery97 over v9

Command: `python3 -B .ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py --tool tools/check-advance-evidence.py --work /fast/scratch/hyaku/kotodama-r97/ExecGraderV9/battery` — rc 0, no traceback.

- `BATTERY-SUMMARY survivors=0 unnamed=0 refused=31 traceback=0 clean=2 not-clean=0` (target 0/0/31).
- New classes: CR1/US1/NUL1 rc=2 named=VERDICT-CTRL; OGH1/IS1 rc=2 named=VERDICT-SEPARATOR; CM1/CMW2 rc=1 named=TOPIC — all REFUSED.
- Controls: G0 CLEAN, ZWNJ1 CLEAN.
- Driver identity: battery97.py sha `79efb67c40f9a534a051fa4e2b99fca0bb196decadc3a9987e5acc72d13fb94c` == `reports/round-97/controls/battery97.sha256` pin == `BATTERY-SHA256` in `reports/round-97/controls/battery97-control-v8.txt`; that control receipt shows `survivors=7 unnamed=0 refused=24` over TOOL-SHA256 f29ab013… (v8), the measured before-state.
- `REG R93/R92` output: 34/34 lines byte-identical to `reports/round-95/controls/reg-v5.txt` (diff empty).

Stage artifacts: `stage/ExecGraderV9/battery-v9.txt`, `stage/ExecGraderV9/selftest.txt`, `stage/ExecGraderV9/V9-READY` (one line: v9 sha), `stage/ExecGraderV9/v8-base.py`.

## Cosmetic (routed round-96 closure defect 6)

- Module docstring: "Round-96 v7 refuses the nine fresh CriticO95 classes" -> v8 (code landed as v8 in 66d2e915; landed tool sha == v8 == base tree).
- `_refuse_verdict_channel` docstring label v7 -> v8, extended with the v9 channels.
- `_content_toks` comment "Round-96 v7 (routed CriticO95 BR1/DASH1)" -> v8.
- Pins header comment "round-96 v7 pins (10)" -> v8.
- Blank line between `def _refuse_disguised(...)` and its docstring removed (line 331).
- A Round-97 v9 history paragraph was added to the module docstring per the file's convention. No behaviour change from this step (battery + REG prove bytes around them unchanged in behaviour).

## Repairs

1. First battery run over v9 regressed exactly one REG line: `REG R93 A5c rc=2 ... outcome=refused-unnamed` vs baseline `rc=1 fail=APPENDONLY`. Cause: the Zs check fired on plain space U+0020 inside the `NOT located` verdict window (A5c fixture spells the flip with a space). Fix: U+0020 added to the skip set (`_refuse_verdict_channel` line 316) — a legitimate verdict spacing, same semantics as the anchored `NOT[ _-]?LOCATED` rule. Re-ran selftest and battery97: both green, REG 34/34 byte-identical. No other repair.

## Tooling authorization

None installed or upgraded (nothing needed beyond python3/git already present). pacman untouched (host-wide pause respected). No host sysctls touched. Scratch dir `/fast/scratch/hyaku/kotodama-r97/ExecGraderV9/` (deleted before yield); nothing written under /tmp; fleet root untouched except lane paths assigned to this seat.

## Mutation (MutationTester97)

First measurement landed (`stage/MutationTester97/DONE` after a bounded 77-check wait) and shows **no survivors — no repair performed**, so the grader bytes measured by selftest/battery above are final:

- Receipt: `reports/round-97/controls/mutation97-first.txt` — `MUTATION-SCORE: 121/121 killed, 0 survived, 0 broken-pattern` (floor total 118; killed == total), over `TOOL sha256=1021dc9d…` (v9 as landed).
- Driver identity: `stage/MutationTester97/mutants97.py` sha `f9c623fd384d276ad2b53ea10d67ac021a2fc77a3baca50df33d5e505bd22259` == `reports/round-97/controls/mutants97.sha256` pin == `DRIVER-SHA256` in the first-measurement receipt.
- The ten new-round mutant classes are all KILLED: `verdict-ctrl-off`, `verdict-separator-off`, `heading-combining-off`, `cr1-allow-000d`, `us1-allow-001f`, `nul1-allow-0000`, `ogh1-zs-exempt-1680`, `is1-zs-exempt-3000`, `cm1-mark-lasttoken-only`, `cmw2-mark-numbering-only` — each killed by the corresponding v9 pin(s).
- No repair was needed, so `mutation-after-repair.txt` does not exist by design (the seat spec requires it only "if any survived mutant").

## Frozen counter (predispatch.py)

Command: `python3 -B reports/round-97/predispatch.py --root <lane> --work /fast/scratch/hyaku/kotodama-r97/ExecGraderV9/counter --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569` — rc 0 (`counter rc=0`), read-only over the lane tree. Output: `stage/ExecGraderV9/counter.txt`.

`PREDISPATCH-97: PASS legs=13/13`:

- O0 PASS tool-sha `1021dc9d…` differs from v8 `f29ab013…`; O1 PASS 155/155 floor=154 rc=0; O2 PASS survivors=0 unnamed=0 refused=31, pin=receipt=driver; O3 PASS 121/121 killed, 0 survived, 0 broken-pattern; O4 PASS 34/34 REG lines byte-identical.
- C legs also all PASS on this run (the coverage seat had landed): C1 bytes=36739 h2=13 table=7x6 phrases=6/6 topic-line=equal; C2 rows=917 highest=S993 new=9 qualifying=8; C3 added=9 removed=0; C4 census rc=0; C5 index rc=0; C6 8/8 cited; C7 8/8 captured; C8 files=269 other owners=0.

A first counter attempt hit this seat's 900 s shell deadline during the O3 mutant replay (the counter itself re-runs selftest + battery97 + mutants97, ~1417 s wall); it was re-run once to completion with no deadline. The frozen counter bytes were never edited.

## Acceptance

- Lane `tools/check-advance-evidence.py` is v9 (`1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b`); nothing committed.
- Stage `stage/ExecGraderV9/`: `v8-base.py`, `battery-v9.txt`, `selftest.txt`, `counter.txt`, `V9-READY`, `DONE` (last).
- No class left open; no blockers.
