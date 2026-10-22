# Claim D instrument controls

## Assignment and axes

Exercise the boundary counter at the declared base and against isolated entry copies. Axes: rejection of invalid anchors, acceptance of valid anchors, enforcement of one distinct neighbour per row, and isolation from lane changes.

Result: all nine requested controls returned the expected verdict. Two additional adversarial controls expose false positives, including at the required `15/15/15` total. Proposed repair below; no lane implementation was edited.

## Setup and retained evidence

- Sandbox: `/fast/scratch/hyaku/kotodama-r51a3/ExecBoundaryCounterControls`.
- Shared clone switched to detached base `bff83ba65bf9559af4d7567e81703059667a0005`; Git printed `HEAD is now at bff83ba round-50 verifier spot-check: original separability self-application unmet`.
- Copied the lane's `reports/round-51/boundary-count.py` into the sandbox. Selecting the base removed the initial copy because the script was tracked at the cloned tip but absent at base; an initial execution batch therefore failed to open the script. Re-read the lane instrument, restored the copy, and executed the controls below. Those setup failures are not counter verdicts.
- Entry copies, two ambiguity fixtures, and exact successful-execution receipts remain only in the sandbox. Receipt: `reports/round-51/boundary-controls/receipts.json` (relative to the sandbox).
- Instrument baseline after selecting base: `rows=11 resolved=11 distinct=11`, exit **0**.
- Every control command was `python3 -B reports/round-51/boundary-count.py --entry reports/round-51/boundary-controls/<filename>`, run from the sandbox. Baseline omitted `--entry`. Exit codes were retained with `printf "exit=%s\n" "$?"` immediately after Python.

## Requested controls

Each mutation starts from the full, unchanged base entry, not another negative control. Baseline first neighbour: `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:31`; second neighbour: `:32`; directory row: `:41`.

| Control file | Exact mutation | Printed line | Exit | Verdict |
|---|---|---|---|---|
| `01-dangling-line.md` | First-row anchor becomes `agrarian-field-system-lexicon.md:999999` | `rows=11 resolved=10 distinct=10` | 1 | Correct rejection |
| `02-nonexistent-file.md` | First-row anchor becomes `controls-nonexistent.md:1` | `rows=11 resolved=10 distinct=10` | 1 | Correct rejection |
| `03-ambiguous-basename.md` | First-row anchor becomes `controls-ambiguous.md:1`; created that basename in both `culture-material/` and `myth-symbol/` under sandbox knowledge | `rows=11 resolved=10 distinct=10` | 1 | Correct rejection |
| `04-duplicate-neighbour.md` | Replace second-row hunting anchor with the first row's `agrarian-field-system-lexicon.md:56,:62` | `rows=11 resolved=11 distinct=10` | 1 | Correct rejection |
| `05-no-backticks.md` | Remove both backticks around the first-row anchor | `rows=11 resolved=10 distinct=10` | 1 | Correct rejection |
| `06-nonexistent-directory.md` | Replace `civilizations/` with `controls-nonexistent-directory/` | `rows=11 resolved=10 distinct=10` | 1 | Correct rejection |
| `07-missing-heading.md` | Rename heading to `## 2. Boundary control with missing expected heading` | No stdout; stderr: `BOUNDARY_INPUT_ERROR list.index(x): x not in list` | 2 | Correct input error |
| `08-fifteen-rows.md` | Append the four resolving, distinct rows listed below | `rows=15 resolved=15 distinct=15` | 0 | Correct instrument acceptance |
| `09-line-range.md` | First-row anchor becomes `agrarian-field-system-lexicon.md:10-12` | `rows=11 resolved=11 distinct=11` | 0 | Correct range acceptance |

Positive-control additions, ready to reproduce (control data, not a proposal to land these rows):

```markdown
| `symbolism-synthesis-method.md:69` | animal taboo and rite | control only: herd supply, not symbolic grammar |
| `celestial-symbolism-calendars.md:28` | subsistence and sky figures | control only: herd input, not sky lore |
| `ritual-liminality.md:63` | calendrical sacrifice | control only: herd supply, not ritual grammar |
| `turkic-steppe.md:148` | regional exchange chains | control only: general method, not regional restatement |
```

Those lines were re-read in the lane at `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:69`, `corpus/knowledge/myth-symbol/celestial-symbolism-calendars.md:28`, `corpus/knowledge/myth-symbol/ritual-liminality.md:63`, and `corpus/knowledge/civilizations/turkic-steppe.md:148`. This positive control tests the counter only; it does not establish the required body development for a landed D change.

## Wrong verdicts

| Additional control | Mutation | Printed line | Exit | Why wrong |
|---|---|---|---|---|
| `10-multiple-neighbours-one-row.md` | Append a separately backticked `hunting-foraging-subsistence.md:36,:116` to the first-row neighbour cell; retain the original hunting row | `rows=11 resolved=11 distinct=11` | 0 | One row names two neighbours, with hunting duplicated across rows; global distinctness hides the defect |
| `11-no-line-number.md` | First-row token becomes bare `agrarian-field-system-lexicon.md`, still backticked | `rows=11 resolved=11 distinct=11` | 0 | File existence is accepted without a line anchor; this is weaker than D's required `file.md:N` shape |
| `12-fifteen-multiple-neighbours.md` | Apply control 10's mutation to the positive 15-row entry | `rows=15 resolved=15 distinct=15` | 0 | Same one-owner violation passes the exact claimed final total |
| `13-fifteen-new-row-no-line.md` | In the positive 15-row entry, change the new ritual token to bare `ritual-liminality.md`, still backticked | `rows=15 resolved=15 distinct=15` | 0 | A new row without the required line anchor passes the exact claimed final total |

Evidence: `reports/round-51/claims.json:18` requires one distinct neighbour by a resolving path:line anchor; `:25` requires the final total. In `reports/round-51/boundary-count.py:25`, the first colon-and-number group is optional. At `:87-90`, every resolving token increments a row's resolution once, while targets are unioned globally without requiring one target within each row. These are distinct causes.

The existing directory row (`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:41`) is intentionally preserved. The proposed file-anchor repair does not remove that baseline behaviour. The counter's current permissive bare-file grammar is not itself a regex malfunction; it is insufficient for the declared D acceptance contract.

## Minimal proposed fix — not applied

```diff
--- a/reports/round-51/boundary-count.py
+++ b/reports/round-51/boundary-count.py
@@ -25 +25 @@
-FILE_ANCHOR = re.compile(r"^([\w./-]+\.md)((?::\d+(?:-\d+)?)?(?:,\s*:\d+(?:-\d+)?)*)$")
+FILE_ANCHOR = re.compile(r"^([\w./-]+\.md)((?::\d+(?:-\d+)?)(?:,\s*:\d+(?:-\d+)?)*)$")
@@ -88 +88 @@
-        if tokens and all(hits):
+        if tokens and all(hits) and len(set(hits)) == 1:
```

[INFERENCE] This requires a line number on file anchors, preserves ranges and comma-separated line references, and allows multiple tokens only when all resolve to the same neighbour. Global distinctness still rejects duplicate neighbours across rows. No repaired-instrument result is claimed.

## Files, limits, and unrun checks

- Lane file written: this exclusive report only. Sandbox files: copied counter, thirteen full entry copies, two ambiguity fixtures, and receipts.
- No external sources opened; no tools installed or updated. No LSP tool was exposed in this seat; source inspection used the reader, and no symbol refactor was applied.
- Ran only the assigned instrument controls. No build, lint, formatter, integration gate, semantic ownership audit, or repaired-counter regression run was performed.
- Parent should apply an agreed repair and run the same controls once, including the two 15-row false positives; expected repaired verdict for those is exit 1. Body development and anchored-line support remain non-author review responsibilities, not properties this counter proves.
- No remaining blocker. These are author-lane findings, not admission of either claim.
