# ExecSeparability — round 89 w1 (milestone r89-v1)

Seat: executor (leaf). Built the claim-separability tool and tested it against a synthetic combined landing on the REAL freeze 1cbd0efc56edaa9394e3532fc5d8ef924f122f01 (base 42816d25). No fetches, no production-file edits, no commits in the lane, no tool installs.

## Files written (stage `.ufo/waves/round-89/w1/stage/ExecSeparability/`)
- `separability89.py` (sha256 54b02c6572cd49fd34eccb91b20f5944a711abbb5d2d3eaa21685343ad81d4c2). Goes to `reports/round-89/separability89.py` at integration.
- `synth_landing89.py` (sha256 d2f3a9d61f0d4f1c4941a3551d6c15352af22f0d88bd616bf9e054fc23ef1b10). Adapts `controls89.py`: in one clone of the lane at the real freeze it commits F-forged-capture + C-forged-capture as ONE commit (`combined`), then two children: `f-revert` (the population recheck cells set back to their freeze values) and `c-revert` (the entry removed). Commit dates are fixed to the freeze's committer date, so the ids can be reproduced.
- Receipts: `synth-landing.json`, `sep-combined.json`, `sep-combined-rerun.json`, `sep-f-revert.json`, `sep-c-revert.json`, `sep-refuse-badrev.json`, `helper-checks.txt`.

## How separability89.py works
CLI: `--lane --freeze --lands --work EXISTING_DIR --out JSON [--keep]`. For each claim it makes its own `git clone --shared --no-checkout` sandbox under --work, then `checkout --detach <freeze>` and checks `rev-parse --show-toplevel` (once before the overlay and again right before the commit).
- **F overlay:** `corpus/SOURCES.md` is rebuilt from the FREEZE bytes. Only cell 9 of the 16 claims.json population rows is replaced, with its LANDS value, and the cell keeps its padding. `set_cell` asserts that every other cell is unchanged. The lesson and `reports/round-89/rechecks/` come from lands.
- **C overlay:** FREEZE bytes, plus the lands row lines whose ids are absent at the freeze, inserted in lands order right after the last registry row. Used-by (cell 10) of old rows takes its lands value. The entry, `corpus/README.md`, the lesson and `reports/round-89/evidence/` come from lands.
- **Path handling:** lands paths are restored with `git rm -r` followed by `git checkout <lands> -- <path>`, which keeps the exact blob and mode. A path absent at lands is removed. The tool refuses if the overlay diff against the freeze touches any path outside the overlay.
- **Commit:** identity sep89 <sep@invalid>; author and committer dates = the freeze's %cI; fixed message; hooks and signing off. This makes the overlay commit and tree ids reproducible from committed revisions, which addresses R88-V5.
- **Grading:** runs the FROZEN counter (`git show <freeze>:reports/round-89/measure89.py`, written to `<sandbox>/.git/sep89-measure89-frozen.py`) with `--root <sandbox> --freeze <freeze> --lands <overlay commit> --claim F|C --work <fresh dir>`.
- **--out records:**
  - claims and counter sha256, and the tool's own sha256
  - whether lands descends from the freeze
  - per overlay: the rebuild log (replaced/inserted/used-by ids), the diff against the freeze, and path/mode/blob/sha256/bytes for every overlaid file
  - overlay commit and tree, the command, rc, the verdict line, the legs and the full stdout
  - the full procedure text, including a manual equivalent
- **Exit codes:** 0 iff both overlays PASS; 1 otherwise; 2 on refusal. Sandboxes are removed unless --keep.

## Observed commands (cwd = scratch, TMPDIR = scratch)
| command | rc | result |
|---|---|---|
| `synth_landing89.py --lane <lane> --freeze 1cbd0efc… --work <scratch> --out synth-landing.json` | 0 | combined cb6559d0930c2e7997adb084446afd727bd1b533, f-revert c8121f98a1412e0a208e2a47a3447298f85958f1, c-revert 0cdc1052e8ae6bd207901224b60a237ef601c864. Direct frozen-counter grading: combined F PASS 5/5 and C PASS 8/8; f-revert F FAIL 4/5 (ADVANCED) and C PASS; c-revert F PASS and C FAIL 2/8 |
| `separability89.py --lane <synth clone> --freeze 1cbd0efc… --lands cb6559d0… --out sep-combined.json` | 0 | F overlay 8974bc6095b154de3d91a41ee76cb29510eb7a9a (tree 5f6f285f…, 19 files) **PASS 5/5**; C overlay 7821c6bad18bb0dce6431ca66f35805d4845d523 (tree 05ec5f41…, 8 files) **PASS 8/8** |
| same, rerun → sep-combined-rerun.json | 0 | the same overlay commits, trees and per-file sha256 (`cmp` printed DETERMINISTIC-MATCH) |
| `… --lands c8121f98… (f-revert)` → sep-f-revert.json | 1 | F overlay **FAIL 4/5 (LEG FAIL ADVANCED)**; C overlay PASS 8/8 (same tree 05ec5f41 as combined) |
| `… --lands 0cdc1052… (c-revert)` → sep-c-revert.json | 1 | F overlay PASS 5/5 (same tree 5f6f285f as combined); C overlay FAIL 2/8 |
| `… --lands deadbeef` → sep-refuse-badrev.json | 2 | refused: not a 40-hex revision |
| helper invariants (helper-checks.txt) | 0 | row_map equals measure89.rows over 859 freeze rows; 1718 set_cell probes left the other cells unchanged; the C rebuild applies used-by, inserts after line 891 and keeps the population rechecks; the F rebuild changes only the target recheck |

I checked the overlay diffs by hand on a `--keep` run:
- F changes exactly 16 SOURCES cells, `90d` → `2027-05-03`, plus the lesson and 17 rechecks files.
- C inserts S936–S938 after freeze line 891 (the synthetic lands appended them at the end of the file, so the tool really does move them), plus the entry, README, lesson and evidence.

`rm -rf /fast/scratch/hyaku/kotodama-r89/ExecSeparability` rc 0.

## Risks and defects (reported honestly, nothing amended)
1. **Cross-claim interaction that the overlays cannot show.** F OTHERCELLS requires every population-row cell except recheck to stay at its base value. If the C entry cites a population id (for example S020 or S021) and the landing adds the entry to that row's used-by, the COMBINED landing fails F, yet both overlays pass, because the F overlay discards used-by. Separability PASS does not imply that the combined lands passes. The combined lands must still be graded directly. L1 should keep C from touching used-by on S009…S875 (the 16 ids).
2. **Both overlays carry the whole lands `corpus/lessons/round-89.md`, as the spec requires.** The lesson is shared, not split per claim, so a claim that relies on the other claim's lesson lines would not be caught.
3. **The synthetic landings use the controls' forged captures.** These are known survivors: the quote is pasted in, the URLs are example.org, and `fetched_at` is 2026-11-04T00:00:00-03:00. This run tests overlay mechanics only, not freshness or coverage evidence.
4. **The synthetic commit ids are not durable**, because the clone was deleted. They can be reproduced by re-running `synth_landing89.py` at the same freeze, since the dates are fixed. The overlay ids are reproducible in the same way (shown by the rerun).
5. **Untested branches.** The used-by branch of the C rebuild and the `missing_at_lands` path are exercised only by helper-checks, not by the counter run. A population row that has extra literal pipes would still map cell 9 the same way measure89 does.

Not run (parent owns gates): measure89 --selftest, any lint or format, and any run on the real lands (it does not exist yet).
