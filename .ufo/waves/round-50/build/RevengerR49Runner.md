# RevengerR49Runner — Ca: what the r49 separability legs removed, checked, and why they passed

Scope: `reports/round-49/run-validation.py` L264–339 (legs `c_without_s`, `s_without_c`) and the lines that consume them (L39, L252–253, L342–343). Lane untouched (HEAD 4ad2683): read-only git and file reads only. All executions ran in a temp clone of landed commit d91c632, restored by sha256 after each mutation, then deleted. No installs.

## Summary

- **`c_without_s` removes nothing and never reads the registry.** It checks that every S-id in C's text has an inline URL on C's `- source:` line. It passes because the lane copied those URLs into the entry. It still passes with the registry deleted (P3).
- **`s_without_c` deletes the evidence it is meant to test, then tests what remains.** It removes the 12 `used-by` references to C and demotes those 12 rows to `queued` before running the census predicates. It passes by construction. Its own guard (L302–305) can never fire.
- **Neither leg can gate.** Both are informational and excluded from `admitted`. The r49 receipt therefore says `admitted`, while the outside verifier adjudicated REJECTED-HONEST-STOP on separability.

## 1. Inputs (identical blobs at d91c632, lane HEAD 4ad2683, and lane working tree)

| path | blob |
|---|---|
| reports/round-49/run-validation.py | 6c8ffdc |
| corpus/SOURCES.md | 34e27f6 |
| corpus/knowledge/culture-material/hunting-foraging-subsistence.md | ae2226c |
| reports/round-49/validation.json | bd762a8 |
| corpus/lessons/round-49.md | f03d4c7 |

## 2. `c_without_s` (L264–274)

**Removed:** nothing. Inputs are C's own text only (`elines`, `entry_text`, read at L97–100). No other file is read, written, or deleted.

**Checked:**
- L265–266 `url_ids`: S-ids matching `**Snnn** (http…` on the `- source:` line. Result: S031–S042 (entry line 20).
- L267 `cited`: every `\bS\d{3}\b` in the entry. Result: S031–S042.
- L268 `no_inline_url = cited − url_ids` = ∅; L273 `passed = not no_inline_url` = true.

**Why it passed:** the lane placed each cited id's URL in the `- source:` field (line 20). The leg verifies the presence of that copied text, not dependence on the registry. The cited ids are introduced in the `- sources:` field (lines 5–18). Line 18 defers "full locators and quotes" to the round lesson's `## Gate`, and that deferral is never inspected.

## 3. `s_without_c` (L276–339)

**Removed**, in a `.scratch/` copy only (copy written L295–299, unlinked L313; SOURCES.md on disk untouched):
- L285–287: every `used-by` token equal to C's path. Result: 12 tokens, all in rows S031–S042 (status `mined`).
- L288–289: each `mined` row left with no citer becomes `queued`. Result: 12 rows demoted (P1), so 20 mined → 8 (derived).
- C's file is not removed by this leg.

**Checked** (L316–324): malformed == 0; duplicate ids == ""; enum/tier-inflation violations == ""; missing used-by == "". These are the census commands at L56–62, rerun on the copy with the L303–305 exemption.

**Not checked on the counterfactual:** rows ≥ 1, rejected ≥ 1, headings (L198–200), `opened` dates (L209), lesson `## Gate` coverage (L211–221).

**Why it passed**, three independent reasons, each observed:
1. census[6] (L62) inspects only `mined` rows' used-by paths. After L285–289 the counterfactual contains 0 C-path tokens (P1) and no mined row names C, so there is nothing for it to find.
2. The edits cannot violate the other three predicates. Cell count is preserved (malformed 0), ids are untouched (dup ""), and `queued`/`mined` are both valid enum values (enum "").
3. The guard at L302–305 is inert. The replacement matches CENSUS[6] (verified), but the counterfactual has no C-path token for it to act on, because L286 removed them before L301 ran.

The intent is recoverable from the L302 comment: C should be treated as absent so census[6] reports it. L285–289 removes the reference before the check, so the signal never exists. P2 shows the signal does exist when the reference is not stripped.

## 4. Probes (temp clone at d91c632)

| id | state under test | `c_without_s` | `s_without_c` | other | reading |
|---|---|---|---|---|---|
| P0 | committed receipt | passed; 12 cited, 12 URL, ∅ missing | passed | verdict `admitted`; `cross.passed` true (hard-coded) | landed result |
| P0r | runner rerun, no edits | identical | identical except temp path: `5ify14e0` vs committed `nhfoehdu` | — | receipt bytes not reproducible (L295–300, L327) |
| P1 | spy on `sh` (no edit) | — | counterfactual: 0 C-path tokens (12 in SOURCES); 12 rows mined→queued | — | confirms §3 |
| P2 | C file moved away; registry unmodified; unedited CENSUS[6] | — | 12 lines `missing: corpus/knowledge/culture-material/hunting-foraging-subsistence.md`; rc 0 | — | the signal the leg strips |
| P3 | all 47 registry rows removed; C intact | passed (∅ missing) | passed (vacuous, 0 rows) | S failed; `admitted` False; `rejected-honest-stop` | c-leg is blind to the registry |

## 5. Divergences

1. **Mechanism vs. definition.** The Ca shared contract defines dependence as X's bytes matching Y's export regex or naming Y's land path. On the r49 bytes, C does both to S: it cites S031–S042 (12 ids) and names `corpus/SOURCES.md` (line 18). The c-leg accepts this only because the URLs are present, so it is strictly weaker than the definition.
2. **Reference stripped before the test** (L285–289 vs. the guard at L302–305). Under the Ca definition, S also depends on C: 12 mined rows name C's land path (observed). The leg hides exactly that edge. The verifier's adjudication (lesson line 17) named only C→S.
3. **Admission excludes both legs** (L264 "these legs never gate admission"; L342–343; docstring L39). Committed verdict is `admitted`; the lesson's adjudication is REJECTED-HONEST-STOP (lesson line 17).
4. **`cross` is hard-coded:** L253 `"passed": True`, L262 `"failures": []`.
5. **C's registry resolution is not checked** (C check L136–139, no resolution term). claims.json line 17 (`after_required`) requires it. P3 shows the gap.
6. **Naming collision:** r49 `Ca` (docstring L20–24, code L147–172) is README revision dedupe, not separability. The r50 `Ca` is a different claim.

## 6. Axis verdicts

- **Calibration.** Known pair: 0 of 2 directional edges detected by the legs, versus 2 of 2 by the Ca definition applied to the same bytes (C→S by S-id export and by path; S→C by path). The receipt's `admitted` contradicts the adjudication.
- **Coverage.** The legs cover (a) presence of inline URLs in C and (b) base structural validity of S. They cover no dependency channel: no resolution check, no used-by naming check, no acceptance run in a counterfactual tree.
- **Operability.**
  - The default output path is `reports/round-49/validation.json` inside the tree (L377–379). Running the runner in a lane overwrites the committed receipt.
  - It creates `.scratch/` in the tree (L278–279). `.gitignore:6` covers it, so porcelain stays clean.
  - The receipt embeds a random temp name (L295–300, L327), so it is not byte-reproducible (P0r).
  - The census exit code is 0 even when it prints `missing:` (P2). Any rc-based gate would miss it.
  - Latent id grammar gaps: L266–267 match exactly three digits (`S\d{3}`), while census and ROW_RE accept `S\d{3,}` (L56–62, L65). Ids ≥ S1000 are invisible to the c-leg. The URL regex (L266) requires the exact `**Snnn** (http` form.

## 7. Implications for the r50 control (advice; inference unless marked)

- Build the fixture from d91c632 or 4ad2683. All five blobs in §1 are identical at both.
- Expect two directional findings on the r49 pair, not one. claims.json line 50 says "1/1 detected (C->S)". The line-48 definition also flags S, because S's rows name C's path (observed). Inference: line 50 under-specifies unless the checker is scoped to claim-side acceptance only.
- Implement the line-17 resolution criterion as C's acceptance in the counterfactual tree (base + C.lands, with S rows absent). Without it, the r49 blind spot reproduces (P3).
- Evaluate the counterfactual with the referenced path absent. Do not strip references before the check (P2 shape).
- Gate on the captured output text, not on `bash -c` exit codes.
- Use deterministic temp names, or keep temp names out of the receipt.
- Require an explicit `--out`. Make separability part of `admitted`.

## 8. Confidence, unrun checks, reproduction

- **Confidence:** high on mechanism (line-cited code, observed probe outputs on byte-identical inputs). Medium on §7 (inference).
- **Unrun:** the r50 checker and fixture (not landed); lane selftests; QUALITY.md criterion 7; fleet-repo verifier reports (not read; the lane lesson was used instead).
- **Reproduce (clone only):** `git clone -q <lane> /tmp/x && git -C /tmp/x checkout -q d91c632 && python3 -B /tmp/x/reports/round-49/run-validation.py --out /tmp/x-receipt.json`. Do not run in the lane: the default output overwrites `reports/round-49/validation.json`.
- **Installs:** none.
