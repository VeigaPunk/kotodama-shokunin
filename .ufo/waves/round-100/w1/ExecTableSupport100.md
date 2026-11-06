# ExecTableSupport100 — table-cell support checker (claim O)

Tool: `tools/check-table-support.py` (the only file this seat wrote; started byte-identical
to the L1 feasibility reference `reports/round-100/controls/feasibility/table_support_ref.py`,
sha 24fd73f4… — battery over the reference passes 28/28, and the shipped tool's CASE lines are
identical to the reference's; behavioural divergences from the reference are only the frozen-
contract conformance fixes noted below.)

## Tool sha and rule (line numbers in shipped bytes)

- sha256 `972cefea2b429a9d9ca3d9efc1acf3a63391e7c6ba2da576a1225fda6258b73a` (634 lines).
  Drift note for the L1: MutationTester100's first receipt binds tool sha `271c42fa…` (the bytes
  at their freeze); the landed tool is `972cefea…` after the E7 repair below. The counter's O4
  leg re-runs the frozen driver (sha 18dbcf3b…, pinned), which prints 36/36 on `972cefea…`, so O4
  passes on the landed bytes.
- Rule (module docstring, lines 1–45, states it exactly): scope = table whose caption paragraph
  above the header matches `\brecorded cases?\b` (line 161); binding = paragraph below the last
  data row, label tokens NFKD-folded `[a-z]+` len ≥ 3 not in STOP and not `and` (line 109),
  token equality (line 200); support = content words len ≥ 4 not in STOP (lines 93–98), stems by
  `stem()` (lines 79–86), best over any 80 consecutive tokens via `window_best` (lines 130–157),
  supported iff `best*4 >= total*3` (line 222). Measures lexical co-location, not meaning
  (docstring, lines 21–26). Findings UNSUPPORTED-CELL / UNBOUND-ROW / NO-CAPTURE / NO-PATH with
  `line` (lines 173–231); rc 0/1/2 with TABLE_SUPPORT_ERROR and no traceback (lines 580–614).
- Divergences from the reference (all frozen-contract conformance):
  1. `check()` rejects unreadable captures/support files with ToolError → rc 2 (lines 184, 193);
     a non-file named `<S-id>.txt` (e.g. a directory) counts as absent → NO-CAPTURE rc 1, matching
     the contract's enumeration of rc-2 conditions (CriticO100 EARLY.md, confirmed and fixed).
  2. `--entry` / evidence / unreadable-entry / directory-as-entry / `--work` under /tmp refusals
     → rc 2 TABLE_SUPPORT_ERROR, no traceback (lines 580–600).

## Measurements (commands and rc)

- `python3 -B …/tools/check-table-support.py --selftest --work <scratch>/st7` → SELFTEST PASS 40/40, rc 0. (`stage/ExecTableSupport100/selftest.txt`)
- `python3 -B …/controls/battery100.py --tool …/tools/check-table-support.py --work <scratch>/bat7` → `BATTERY-SUMMARY cases=28 pass=28 fail=0 traceback=0`, rc 0. (`stage/.../battery.txt`)
- Lane exposure: every `corpus/knowledge/**/*.md` (271 files) with `--root <lane>` and all 21
  `reports/round-*/evidence` dirs → 270 files rc 0, 1 file rc 1
  (`corpus/knowledge/linguistics/praise-poetry-panegyric.md`: `TABLE-SUPPORT: 21 finding(s) in 1 scoped table(s)`);
  0 tracebacks. (`stage/.../exposure.txt`)
- Seven revert-show-red probes (each patch on a scratch copy, then its selftest; rc 1 each):
  - `WINDOW = 80` → `10000`: `PIN F11-window-80-colocation FAIL rc=0 got=[]`
  - `best * 4 < len(stems) * 3` → `best * 2 < len(stems) * 1`: `PIN F13-threshold-three-quarters FAIL rc=0 got=[]`
  - `stem()` dropped from cell stems: `PIN B2-stemming-rallies-boxes FAIL rc=1 got=[('UNSUPPORTED-CELL', 'Town', 'object'), ('UNSUPPORTED-CELL', 'Town', 'place')]`
  - token binding → substring: `PIN F10-token-not-substring-binding FAIL rc=0 got=[]`
  - caption regex widened to `\brecorded\b`: `PIN B7b-recorded-not-cases-out-of-scope FAIL rc=1 got=[('UNBOUND-ROW', 'Court', '')] scoped=1` (a raw `recorded` widening also fails B7)
  - union support across rows: `PIN F6-no-union-per-row FAIL rc=0 got=[]`
  - NO-CAPTURE not deduplicated: `PIN S-nocapture-deduplicated FAIL rc=1 got=[('NO-CAPTURE', 'S9999', '')]`
- Frozen counter (read-only): `python3 -B …/reports/round-100/predispatch.py --root <lane> --work <scratch>/counter6 --base-rev 60010a55fb5f04ee728070c463b1a57ae1cc17fc` → O0–O4 PASS (O3: actual rc=0 findings=0; forged rc=1 findings=1; forged-minus-actual = `[('UNSUPPORTED-CELL', 'Yoruba', 'limit on the praise')]`, actual-minus-forged empty), O5 FAIL (L1-owned), PREDISPATCH-100 FAIL legs=10/15 with C legs still landing (rc 1). (`stage/.../counter.txt`)
- Pinned mutation driver: `python3 -B …/stage/MutationTester100/mutants100.py --tool …/tools/check-table-support.py --work <scratch>/mut7` → `MUTATION-SCORE: 36/36 killed, 0 survived, 0 broken-pattern`, rc 0. (`stage/.../mutation-after-repair.txt`)

## What this seat could not close

- O5 (SCORECARD capability row + SKILL.md mention) is L1-owned; counter O5 FAIL on this seat's run.
- Claim C legs are other seats' surfaces.
- Calibration warning for any future edit: the frozen driver counts exact occurrences
  (`return 2` ×7, `TABLE_SUPPORT_ERROR` ×13) and exact handler blocks; the tool was recalibrated
  to those counts after the E7 repair (intermediate versions showed 35/36 with 1 broken-pattern).
  Do not edit the tool without re-running the pinned driver.
- Tools installed/upgraded: none (no new tools; only python3 stdlib used).
