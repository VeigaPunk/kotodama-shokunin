# ExecControls — round-88 O agreement environment (milestone r88-v1)

Seat: ExecControls (leaf, no subagents). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Stage: `.ufo/waves/round-88/w1/stage/ExecControls/`. Scratch (cleared at exit, receipts copied to stage): `/fast/scratch/hyaku/kotodama-r88/ExecControls/`.

Revisions: FROZEN `4b76524c51e1c2f76c99eeb3b629cfac08a44a76`, PRE `0c8c733088df8c4f06770c9e714360eed7f29272`, BASE `4956282281dac1306cfbe59523e46dde99749d75`.

## Verdict

- Committed prefreeze controls reproduce the frozen exact-set vector **13,3,4,4,0** (honest, constant-pass, shotgun-all-labels, extra-id, filename-only) when graded from committed bytes at PRE and FROZEN. Confirmed by the frozen counter, unmodified, run four ways (A1–A4).
- Inherited r87 counter at BASE reproduces **12,3,12,12,12**.
- Defect: the counterfeit wrappers resolve the honest auditor by `parents[2]` (off by one; the correct checkout root is `parents[3]`) and by `KOTODAMA_ROOT`. Two consequences, both reproduced:
  1. Run from the committed controls directory, or from any materialised work directory, without `KOTODAMA_ROOT`, shotgun and extra-id exit 2 with no JSON (B1–B3).
  2. Under the frozen counter, `KOTODAMA_ROOT` is always set to the *live* root. So the counterfeits execute the live checkout's `tools/check-attestation-packet.py` while the honest leg executes the committed blob. Committed-byte and live-tree evaluation therefore diverge whenever the live auditor differs from the committed one: with a tampered live auditor the vector is **13,3,1,1,0** (C1), not 13,3,4,4,0.
- Proposed fix (staged, minimal): the wrappers prefer the committed honest auditor materialised beside them (same revision, same work directory), then `KOTODAMA_ROOT`, then the nearest ancestor checkout, and fail loudly if none exists. With the fix the vector is **13,3,4,4,0 in both committed and tampered-live evaluation** (C2, C3), and the no-env failures disappear (B4–B6).
- The frozen counter was not amended. Its `--selftest` is vacuous and its fallback reads the live worktree; both are reported below as frozen-counter defects.
- O remains **not passing** at every revision tested, but only for the expected reason: `tools/check-finding-sets.py` (the comparator) does not exist at any of them, so `battery-present-at-lands`, `battery-selftest:exit` and `battery-agrees` fail. No score leg of the counter is affected by that.

## Commands and results

All counter runs: `python3 -B <FROZEN-clone>/reports/round-88/measure88.py --root <R> --lands <L> --claim O --work <W>`. The counter was taken from the FROZEN checkout; its sha256 `5a80a439…bd995e7` equals the lane file.

| id | root (graded bytes) | lands | rc | vector (honest,const,shotgun,extra,filename) | expect 13,3,4,4,0 |
|---|---|---|---|---|---|
| A1 | clone @PRE (committed) | PRE | 1 | 13,3,4,4,0 | yes |
| A2 | clone @FROZEN (committed) | FROZEN | 1 | 13,3,4,4,0 | yes |
| A3 | live lane tree | FROZEN | 1 | 13,3,4,4,0 | yes |
| A4 | live lane tree | PRE | 1 | 13,3,4,4,0 | yes |
| A5 | live lane tree | BASE | 1 | 13,3,4,4,0 | yes, but controls and cases are read from the live tree (no committed copy at BASE) |
| A6 | clone @BASE (committed) | BASE | 2 | none (`INPUTS_ABSENT`) | no: cases.json absent at BASE |

rc 1 in A1–A5 is the expected O failure: battery-present/selftest/agrees legs fail because the comparator is absent. The five score legs are the observable of interest.

Direct runs (`direct()` in the runner; `KOTODAMA_ROOT` removed from env; packet = base craft.json with duplicate id):

| id | tool | rc | result |
|---|---|---|---|
| B1 | committed PRE wrapper in controls dir | 2 | looks for `clones/frozen/reports/tools/check-attestation-packet.py` (parents[2]) |
| B2 | shotgun copied with honest into a work dir | 2 | looks for `ExecControls/tools/...` (parents[2]); this is the battery-agrees environment |
| B3 | extra-id copied with honest into a work dir | 2 | same |
| B4 | fixed shotgun, materialised with honest | 1 | 8 labels emitted |
| B5 | fixed extra-id, materialised with honest | 1 | RECORD_ID + invented CLOCK_SCOPE |
| B6 | fixed shotgun in controls-fixed dir (ancestor walk) | 1 | 8 labels from the lane's tools (ancestor walk) |

Scratch-clone experiments (`clone = git clone --shared <lane>`, host guard `rev-parse --show-toplevel` asserted; the lane is not written):

| id | setup | rc | vector |
|---|---|---|---|
| C1 | clone@FROZEN, honest working-tree file tampered (adds an always-present CLOCK_SCOPE finding), unfixed controls, lands FROZEN | 1 | **13,3,1,1,0** |
| C2 | fix committed in scratch clone branch `r88-exec-controls-fix` = `5411289f766bed63ed1786e1a48da942c877f31d`, untampered, lands = fix commit | 1 | 13,3,4,4,0 |
| C3 | as C2, honest tampered in working tree | 1 | **13,3,4,4,0** |

Inherited (I1, `reports/round-87/measure87.py` at BASE, clone@BASE, committed PRE candidates): honest 12/12, constant 3/12, shotgun 12/12, extra 12/12, filename 12/12. Matches the claim's inherited expectation and `pre-dispatch.json`.

Counter `--selftest` (S1): rc 0. See defect F4: it passes for the wrong reasons.

Lane host-state check: `git -C lane status` before and after shows only sibling work (`LOG.md`, `corpus/QUALITY.md`, `reports/round-88/counter-selftest-false-green.json`, `probe-counter-selftest.py`, and untracked round-79/round-88 items). `tools/` and `reports/round-88/{measure88.py,controls}` have the same sha256 as the commit. All my lane-path invocations used `-B`. A lane `reports/round-88/__pycache__/measure88.cpython-314.pyc` (mtime 17:14:24) exists; I did not create it and did not remove it. Please attribute it to the owner.

## Live-tree versus committed-byte evaluation (answer)

- The honest leg always reads committed bytes (`materialize` → `git show rev:path`).
- The counterfeit legs read the wrapper bytes from committed bytes, but their honest oracle comes from `KOTODAMA_ROOT` = the counter's `--root`, which is the live tree when the lane is the root. The two agree only when the live `tools/check-attestation-packet.py` equals the committed blob at lands. Today that is true (sha256 `4abcbbd0…c497aa` at lane, at FROZEN, at PRE, at BASE), so the frozen scores are correct today but for an environment reason, not a structural one.
- The fix removes the dependency: the grader materialises the honest auditor next to each wrapper, and the wrapper prefers that file. C1 vs C3 is the demonstration.

## Defects

- **F1 (controls, fixable here).** `parents[2]` off-by-one in `shotgun-all-labels.py` and `extra-id.py`; no committed-bytes honest resolution; silent exit 2 on a missing auditor. Evidence: B1–B3, C1. Fix: `controls-fixed/` (diff `controls-fixed.diff`).
- **F2 (controls, fixable here).** Live-tree contamination through `KOTODAMA_ROOT`. Evidence: C1 (13,3,1,1,0). Fixed by F1's fix (C3).
- **F3 (environment of battery-agrees leg, frozen counter).** The counter invokes the battery with inherited env, not `KOTODAMA_ROOT`. A candidate from a materialised directory (the battery's `--candidate` path) fails rc 2 with unfixed controls (B2, B3). [INFERENCE] the battery's own invocation of candidates is in the same situation, since the battery is absent and I cannot observe it. The fixed wrappers do not depend on env in that path (B4, B5).
- **F4 (frozen counter, `--selftest`, not amended).** The selftest passes by construction, not by testing the comparison layer:
  - `report_partial_tool()` substitutes the body text into a path literal, so the reader crashes, and `evaluate` returns `False` for `exact-accepted`. The check is `passed = not ok` (`True`), so it passes.
  - `extra-id-refused` is computed as `passed = True` whenever `wanted is True` and never consults `ok`.
  - `set-equality` compares two Python literals (tautology).
  - Net effect: exit 0 regardless of any comparator. It does not feed `claim_o`, which runs the battery's own selftest, so the O verdict is unaffected, but the docstring's claim that it exercises the transport layer is false. Verified: `python3 -B measure88.py --selftest` rc 0 (S1); the evaluate probe returned `(False, {...})`.
- **F5 (frozen counter, fallback, not amended).** `materialize()` and `claim_o`'s cases lookup fall back to the live worktree when a revision lacks a file, contrary to the docstring's "never grades the worktree". At lands=BASE it does so (A5 vs A6). No effect at PRE or FROZEN (all inputs committed there). Consequence: `pre-dispatch.json` and `no-work-o.json` "at-base" receipts depend on the live tree at the time they were written.
- **F6 (frozen counter, observation).** O cannot pass at any revision until the comparator and battery exist; this is expected and is not a control defect. The battery's own candidate invocation is unobserved ([INFERENCE] above); the fixed wrappers remove the env dependency on that path regardless.

## Proposed fix (staged only; not applied to lane)

- Files: `stage/ExecControls/controls-fixed/shotgun-all-labels.py`, `controls-fixed/extra-id.py`; diff `controls-fixed.diff`; sha256 in `receipts/stage-digests.sha256`.
- Behaviour change: honest-path resolution order and an explicit `CONTROL_HONEST_ABSENT` rc 2. Scoring logic unchanged; `constant-pass.py` and `filename-only.py` need no change (no honest dependency).
- L1 decision required: committed `reports/round-88/controls/*` change bytes at the lands revision. The frozen counter has no controls hash, so the change is admissible only if L1 treats the controls as non-frozen (claims.json lists them as exports, not as frozen predicate). I did not change the frozen counter or cases.

## Items for the main agent to run after integration

- `python3 -B reports/round-88/measure88.py --root . --lands <lands-with-battery> --claim O --work <dir>` once the comparator lands; expected legs for the five controls as in A1.
- Re-run the stage runner (`stage/ExecControls/run_controls.py`) after applying the fix to the lane, to confirm C2/C3-equivalent behaviour with the fixed bytes in the lane's own commit. Note: the runner's final copy step overwrites `receipts/`; `I1-inherited-r87-at-base.txt` was produced by a manual step with the same commands and must be re-created if the runner is re-run.

## Tools

No installs or upgrades. Used: system `/usr/bin/python3` (3.14.8), `git` (archive, clone --shared, checkout, commit only inside scratch clones), `sha256sum`, `diff`, `tar`. Read `/home/vgpnk/.omp/agent/RULES.md`; nothing needed.

## Scratch and cleanup

Receipts copied to stage before cleanup. Scratch clones, trees and work directories are deleted at exit. The scratch commit `5411289f` lives only in the scratch clone and is discarded with it.

## Not in scope, not verified

- The D claim, the numerals entry and S931–S933 were not touched or evaluated by this seat. No S-ids cited.
- No build, lint or test of sibling outputs was run.
