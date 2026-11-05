# ExecBeforeV2: round-92 counterfeit battery replay (operability, O)

Date: 2026-11-05. Lane: kotodama (base 21350361500aa000b90f91082bf9d7295a9c24cd, freeze 066b9728fc64e78735769c4740d05c1000d31a3b).
Stage: `.ufo/waves/round-92/w1/stage/ExecBeforeV2/`. Scratch (deleted after use): `/fast/scratch/hyaku/kotodama-r92/ExecBeforeV2/`.

## Result

- Builder sha256 `86d3b8168635a1c61928a7732676b0c2a0ec9c92b7d7aaeca8bf86fdc547e05d` (matches the pinned `86d3b816` prefix).
- v2 base tool sha256 `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093` (matches), extracted with `git -C <lane> show 21350361500aa000b90f91082bf9d7295a9c24cd:tools/check-advance-evidence.py`, rc 0.
- v3 tool `tools/check-advance-evidence.py` sha256 `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422` (matches O.tool_sha256).
- Before (v2, args set A): 7/7 counterfeits V10a, V10c, V3, V12, V7, V2, V9 rc 0, `PASS legs=8/8`. G0 rc 0, `PASS legs=8/8`. `BEFORE-V2-DEFECT-PRESENT: yes`.
- After (v3, args set B): 7/7 counterfeits rc 1 on the named leg: V10a APPENDONLY, V10c APPENDONLY, V3 UNIQUENESS, V12 CAPTURE, V7 GATE, V2 TOPIC, V9 CAPTURE (each `legs=7/8`). G0 rc 0, `PASS legs=8/8`. `AFTER-V3-REFUSED: yes`.
- Line-by-line comparison against the committed `reports/round-92/controls/before-v2-counterfeits.txt` and `after-v3-refusals.txt`: 14/14 V-lines and 2/2 G0 lines match (rc and named leg). Both replay receipts are byte-identical to the committed files (`cmp` rc 0; `diff` rc 0). Divergence: none.

## Commands (rc)

1. `git -C <lane> show 21350361500aa000b90f91082bf9d7295a9c24cd:tools/check-advance-evidence.py > $S/v2-tool.py` rc 0
2. `python3 -B reports/round-92/controls/make-counterfeits.py --work $S/battery --tool v2=$S/v2-tool.py --tool v3=tools/check-advance-evidence.py` rc 0 (TMPDIR=$S)
3. `cmp` and `diff` of `$S/battery/{before-v2-counterfeits,after-v3-refusals}.txt` against the committed controls: rc 0 both.

## Stage files

- `.ufo/waves/round-92/w1/stage/ExecBeforeV2/before-after-replay.txt` sha256 `94300c3141f5559d7f421fcb1cc37a018804e67a2dcb243cca46fb31f3268ca2` (commands, shas, rc, per-line verdicts)
- `.ufo/waves/round-92/w1/stage/ExecBeforeV2/before-v2-counterfeits.txt` sha256 `0eccfb27725877f35fb9ca5450b742a9326f9555d84cb415d93d571513c1231b`
- `.ufo/waves/round-92/w1/stage/ExecBeforeV2/after-v3-refusals.txt` sha256 `5da93627e4ef876fe8261852332057dcd458086e3f06df770be4fc31354f6f8f`

## Notes

- The builder runs without writes outside `--work`. Fixture trees are under `$S/battery/<V*|G0>/`; no lane file was modified. The builder wrote no receipt into the lane.
- The builder's stdout matches the receipt files it writes.
- Tooling: no tools were installed. Python 3.14.8 and git were used as present on the host. No pacman, sysctl or ~/.local/bin change.
- Not measured here: the O counter (`measure92.py --claim O`), selftest and mutation receipts. Those are outside this seat's assignment and belong to the main agent's verification pass.
- Hygiene: the process cwd was the lane root; all commands used absolute paths or ran from the scratch dir. Scratch dir deleted at the end of this seat.
