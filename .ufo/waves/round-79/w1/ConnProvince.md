# ConnProvince — round 79, wave 1 (pre-data build/recon)

Seat task: check the bounded ledger-token guard's scope against kotodama `PROVINCE.md` and the
chousa/kumitate provinces (read-only); recommend a precise lane-local scope with no
research/protocol ownership claim; causal separability path ownership review.

## Evidence (all read-only; no installs, no scratch needed, nothing mutated)

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD = base `44f76d456c1b326a71ffdb381590af825cbf11be`.

- Guard absent at base: `git cat-file -e HEAD:tools/ledger-token-guard.py` → `fatal: path 'tools/ledger-token-guard.py' does not exist in 'HEAD'` (exit 128). Matches CLAIMS-DRAFT line 3 "base: absent".
- CLAIMS-DRAFT (`.ufo/waves/round-79/CLAIMS-DRAFT.md`): O at line 3 ("acquire a bounded ledger-token guard for this lane's calibration records … The target is one working guard (base: absent), not historical truth certification. Own-work source S897 will cite the opened R77 mismatch evidence; no external-source or new knowledge coverage claim."); Ca at line 4 (one recorded mismatch; "This claim owns records only, not O tool or S897. Distinct paths and separable evaluation required."); freeze requirements at line 6; pre-freeze disposition at line 10 (Ca is a candidate; the census receipt alone is evidence-record repair, not the calibration-sizing target; O remains the declared capability candidate).
- S884 token facts (re-derived, not copied):
  - `git show 44f76d45:corpus/SOURCES.md` line 839 last cell → `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` (actual token at base).
  - `git show 4b255745dea45a45d88b17e3c3fea4cdb6700cf7:corpus/SOURCES.md` line 839 last cell → same `…amend-2026-10-23.md` (actual token at the round-78 recorded revision).
  - `reports/round-78/telemetry/census-end.txt:33` → `used-by=…worldbuilding-setting-practice.amend-2026-10-24-r13.md` (reported token; drifted). File sha256 `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`; git blob `62eb55b77f44bf47c283c98c5645dd7141e98495`.
  - `reports/round-78/telemetry/census-start.txt:33` → `…amend-2026-10-23.md` (correct).
  - `worldbuilding-setting-practice.amend-2026-10-24-r13.md` never existed in this lane: `ls corpus/knowledge/culture-material/` shows only `worldbuilding-setting-practice.md` + `.amend-2026-10-23.md`; `git log --oneline -- <that path>` is empty. The `-r13` suffix belongs to the different `heritage-taxonomy-models.amend-2026-10-24-r13.md` family (landed round 72) — the drifted token is a cross-family suffix transplant, consistent with the R78 spot-check's "uncommitted/regressed working-tree state at capture time" diagnosis (`corpus/lessons/round-78-verifier-spotcheck.md:67`).
  - Corroboration (independent seat, read): `reports/round-79/telemetry/baseline-census-mismatch.json` (ScoutR78Truth stage output) records the same receipt sha256 and `mismatches: 1`.
- Routed-defect lineage: R78-M1 (`corpus/lessons/round-78.md:11`) is the class defect — the round-77 Ca check accepted rows whose recorded base observation ≠ re-run observation; its fix direction ("store the observed token from its exact pinned-base command and reject any pair where stated token equals that observed token") is exactly the O guard's stated behavior (CLAIMS-DRAFT line 3: "rejects an observed_at_base differing from the actual observation and rejects stated_token equal to the actual observation"). Routed defect 2 (`round-78-verifier-spotcheck.md:67`) is the instance defect — the drifted S884 receipt line — which is Ca's repair target.
- Separability control exists: `tools/check-claim-separability.py` (QUALITY 7; static export/path legs + dynamic counterfactual legs, bounded). No round-79 manifest exists yet — claims are not frozen.
- Fleet ownership: fleet root `AGENTS.md:29` — "`scripts/` — operator-side tooling: watchdog driver, source census, `hyaku/` session orchestrator." The drifted receipt's producer `scripts/sources-census.sh` is operator-side fleet tooling, owned by no lane.

## Province scope check — kotodama PROVINCE.md

Verdict: the guard as drafted is inside the lane's province; two wording boundaries must be frozen.

- Inside: `PROVINCE.md:9` ("Owns: … this lane's own gates, source-check records …"). A checker that re-runs the lane's frozen calibration-ledger observations against committed bytes is a lane gate/check record, same family as the existing `tools/check-*.py` instruments.
- Refusal lines respected by the draft: `PROVINCE.md:14` — the verification/civilization partitions "do not expand ownership into general research method, fleet protocol, historical truth certification or lore's canon". CLAIMS-DRAFT line 3 already disclaims historical-truth certification and external-source/knowledge coverage. Keep both disclaimers verbatim in `claims.json`.
- Boundary 1 (research method): the guard must not be described as improving how sources are researched or verified in general — that is chousa's "claim-vs-source verification" craft (`chousa-shokunin/PROVINCE.md:6`). The guard applies one lane's frozen observation commands; it exports no method.
- Boundary 2 (fleet protocol / harness): the guard is not OMP/ufo-fsd tooling and not a wave-dispatch instrument — kumitate's domain (`kumitate-shokunin/PROVINCE.md:3`). It must not claim to enforce fleet protocol or harness rules; its writ is lane calibration records only.
- No canon overlap: the guard checks calibration receipts, never world-canon content; lore's adjacent-contract line is untouched.

## Sibling provinces — read-only confirmation

- **chousa-shokunin**: no chousa file is read or needed by the claim; the claim cites no chousa corpus row and no external source (S897 is own-work, precedent `S860` row kind `own-work` in `corpus/SOURCES.md:815`). No absorption.
- **kumitate-shokunin**: the guard is not orchestration; no kumitate file touched. By the kumitate adjacent rule (`kumitate-shokunin/PROVINCE.md:32` — upstream defects are filed for the operator, never patched from a lane), the drifted census receipt's cause is operator-side (`scripts/sources-census.sh`, fleet `AGENTS.md:29`): this lane may diagnose and append-correct its own receipt (Ca) and file the drift observation; it must not patch the census script or claim any census-tool ownership.

## Causal separability path ownership review

Causal roles are distinct and non-dependent:

- **O (capability, forward-looking):** lands the guard that prevents the R78-M1 *class* (ledger pairs whose recorded observation is not re-derivable, and vacuous stated==observed pairs). It does not repair any past receipt.
- **Ca (records, backward-looking):** lands the append-only correction of the R78 routed-defect-2 *instance* (one drifted S884 receipt line). It does not require the guard to exist.

Neither claim's verification may read the other's landed bytes (QUALITY 7; CLAIMS-DRAFT line 4 "Distinct paths and separable evaluation required"):

| Surface | Owner | Rule |
|---|---|---|
| `tools/ledger-token-guard.py` + its selftest/fixture receipts under `reports/round-79/telemetry/` | O | Ca never executes or cites the guard as authority (QUALITY 28: no graded-tree tool execution without a freeze pin) |
| `corpus/SOURCES.md` — S897 own-work row append | O (CLAIMS-DRAFT line 3 allocates S897 to O; line 4 has Ca disclaim it) | Ca's correction binds only (receipt digest, measured revision, old token, actual token); no S897 citation in Ca counting clauses |
| `SCORECARD.md ## Corrections — round 79` rows | Ca | O must not edit; each row names exact observation command + old/new tokens |
| `SKILL.md` gate row for the guard | O (ScribeRegistry seat drafts it) | Ca must not add or edit gate rows |
| `corpus/lessons/round-79.md` | single-writer or explicitly disjoint O/Ca sections (round-76 add/add lesson hazard precedent) | corrections to the R78 spot-check bind by append, not rewrite (`round-78-verifier-spotcheck.md:67` says "append a correcting entry") |
| `corpus/lessons/round-78.md`, `reports/round-78/telemetry/census-end.txt` | historical, append-only both claims (QUALITY 17/19; RevAppendOnly seat) | both counters read them via `git show <freeze|lands>:<path>` only |
| `LOG.md` / `SHONEN.md` | L1 integration; neither claim needs to rewrite SHONEN (CritAxis seat watches axis labeling) | no score-axis claim (CLAIMS-DRAFT lines 5, 10) |

Counterfactual probes to freeze (run before dispatch, receipts committed): accept-o passes at base+O-only; accept-ca re-derives mismatch=1 at base (do-nothing: unresolved≠0) and unresolved=0 at base+Ca-only; combined in both orders with each counter indifferent to the sibling's bytes. `tools/check-claim-separability.py` must run on the frozen manifest (QUALITY 7, pre-dispatch).

## Proposed bounded move (one)

Freeze a scope+ownership contract in `reports/round-79/claims.json` for both claims (machine-readable draft in `stage/ConnProvince/scope-ownership-draft.json` for ScribeClaims/L1):

- **O scope:** "Lane-local capability: `tools/ledger-token-guard.py` re-runs frozen kotodama calibration-ledger observations (read-only `git show` text extraction at pinned commits; no shells/interpreters/worktree reads) and rejects mutable revisions, constant printers, `observed_at_base` ≠ re-run, and `stated_token == observed`. Owns: the tool, its selftest/fixture receipts, its SKILL gate row, S897 (own-work). Claims: no external source, no knowledge coverage, no research-method/fleet-protocol/harness ownership, no historical-truth certification, no axis score."
- **Ca scope:** "Records repair: one append-only correction binding receipt sha256 `05b5011a…`, measured revision `4b255745…`, reported token `…amend-2026-10-24-r13.md`, actual token `…amend-2026-10-23.md`; original receipt bytes unchanged. Owns: SCORECARD Corrections round-79 rows and its telemetry fixtures. Does not own, edit, or counting-cite S897, the guard, or the fleet census script."

This names the S897 owner before dispatch (QUALITY 7's declared-exports rule), keeps both refusals (`PROVINCE.md:14`) explicit, and adds no new surface.

## Risks and verification

- **Live ambiguity — S897 ownership.** The draft assigns S897 to O (line 3) and has Ca disclaim it (line 4), but ScribeLesson's prompt drafts the S897 row with used-by "planned lesson/tool registry", and the round-79 lesson is a Ca-path record. If S897 lands with Ca while O's fixtures cite it, the QUALITY 7 static leg fires (O cites an identifier Ca newly exports). Resolve at freeze: exactly one claim's `exports` lists S897; the other claim's mentions are review-only. Draft above puts S897 in O.
- **Scope-creep channels to watch:** (a) guard grammar drifting toward live fetches/worktree reads would exit the committed-bytes bound and re-enter research-method territory — SentinelExec/SentinelLimits bound it; (b) "one working guard" sliding into lane-wide verification certification — target stays one tool, no axis score (CLAIMS-DRAFT line 6; CritAxis).
- **Contradiction to keep explicit:** the round-78 lesson's diagnosis ("uncommitted/regressed working-tree state at capture time") is a hypothesis about the receipt's provenance; the provenance cannot be established retroactively. Ca must record the drift, not assert a cause (ScoutR78Truth keeps provenance unknown; my read of the token as a cross-family suffix transplant is corroborating texture, not proof of cause).
- **Verification for reviewers:** re-run the four token/digest commands in Evidence against the freeze/lands commits; confirm the two scope sentences appear verbatim in frozen `claims.json`; run `tools/check-claim-separability.py` on the frozen manifest and confirm zero findings at O-only, Ca-only, and combined; confirm no path outside each claim's `lands` list is written by that claim.

Not run by this seat (honest limits): no counter, guard, or separability run (claims not frozen; no manifest exists); no fixture repository created (no mutation authorized or needed); no tools installed; no scratch used. Findings are proposals grounded in the observed commands above, not round-79 run results.
