# Kotodama round 5 — pre-launch availability report

This is an attempted-dispatch report, **not a completed craft round**.
Prepared work committed before filing:
`2c66f7759be04159113add2264ee6024c5577b44` (child HEAD at filing).
Baseline: `c52f2c07abcfae4d363e6057e3bc7f60b1329efc`.

## Work performed

- Re-read current fleet and lane contracts, then declared two measurable
  claims in `reports/round-5/claims.json`: source follow-ups on the historical
  lowest axis, freshness, and bounded CLI/isolation work on operability.
- Prepared one 16-member batch: ten source scouts cover the twenty previously
  unresolved rows exactly once, two executors own separate tool surfaces,
  and four planner/connector/review/critic fragments have distinct outputs.
  The exact template and assignments are in `prompt-template.txt` and
  `dispatch-plan.json`. Godspeed directive bytes and pairwise-distinct
  prompt expansions were verified before publication.
- Measured the craft checker's baseline: six malformed-input/CLI cases
  produce exit 1 with tracebacks; its positive ten-mutation selftest exits 0.
  The standalone isolated battery does not yet exist. These are recorded
  before-values, not newly repaired behavior.
- Made one actual native AgentSwarm call with the exact non-flash model
  `zai-coding-plan/glm-5.3` and matching profile. The tool immediately returned
  `Invalid model "zai-coding-plan/glm-5.3"`, before any worker launched.
  The exact available-model list and request-file digests are retained in
  `availability-attempt-1.json`. The only listed Z.ai alias was Flash-low.

## Landed changes

Commit `2c66f7759be04159113add2264ee6024c5577b44` carries the prepared claims,
template, assignments, refusal receipt, availability lesson, append-only
LOG entry (`LOG.md:2208`) and SCORECARD pending-status section
(`SCORECARD.md:63`). No tool, fixture, exercise, source ledger, knowledge
entry or packet changed. No provider configuration, credentials, sibling,
fleet state, world bible, rank or canon was touched.

This report is filed after that work commit and is committed separately
under the lane identity. The operator's child-only scope keeps it local to
the lane; it is not a canonical fleet completion signal or ledger closure.

## Before → after measurements

- Prepared assignment count: 16; distinct expanded prompts: 16; unresolved
  original IDs assigned exactly once: 20. These are preparation counts,
  not claims of source improvement or launched runtime concurrency.
- Native request → launched workers → completed workers: **16 → 0 → 0**.
  Reproduce the receipt count with:
  `python3 -c 'import json; d=json.load(open("reports/round-5/availability-attempt-1.json")); print(d["requested_workers"], d["launched_workers"], d["completed_workers"])'`.
- Claim F: no new source ledger exists; follow-ups and three parent passage
  re-fetches have not run. **Pending, not admitted.**
- Claim O: no executor launched, no tool code changed, no after-measurement
  over repaired code exists. **Pending, not admitted.**
- Existing deliverable regression check: the full supplemental acceptance
  runner was rerun from a clean staged export and exited 0:
  `python3 reports/supplement-opencode-1/run-validation.py` reported
  `acceptance_checks_passed: true`, the existing 148 audit rows, 7/7 frozen
  replay, all legacy/assembler/replay/inventory/craft selftests passing, and
  the existing 20 D2 findings. Those are baseline observations, not round-5
  improvement. `git diff --cached --check` also passed before the work commit.
- Prepared JSON syntax, receipt SHA256 pins, exact directive prefix,
  assignment coverage, append-only LOG prefix and absence of tool/example/
  knowledge changes were checked against the baseline.

Every-axis verdict: **depth unchanged; coverage unchanged; operability
unchanged; freshness unchanged; calibration unchanged; adjacency unchanged.**
No scalar score or capability was added. This preflight attempt cannot be
admitted or counted toward the completed-round criterion.

## SHONEN

- [ ] Decision tables/error patterns/checklists: untouched by this attempt;
  existing author-side evidence remains in SKILL.md and the supplemental report.
- [ ] End-to-end domain task: no new task ran; the existing D2/craft outputs
  do not become new round-5 evidence by repetition.
- [ ] Runnable instructions: the existing acceptance battery passes, but
  neither prepared new capability was executed or delivered.
- [ ] Province/no-bleed review: no promotion reassessment was performed;
  scope was retained and no domain surface changed.

No independent reviewer or promotion verifier ran; SHONEN.md remains unchecked.

## Blocker and continuation

The observed failure is the native host's model-registry validation, not
an upstream Z.ai 429 or proof of provider failure. The provider may work
elsewhere; this exact request did not reach it. A rate-limit cooldown alone
cannot prove the native alias is available. No Flash substitution, implicit
profile/default reroute, custom API client or manual execution of the worker
assignments was used to force a round through.

Round 5 remains pending. Reuse the prepared request only after rechecking
its baseline and the exact native route. This is the first consecutive
post-supplement goal turn encountering this registry blocker; the overall
goal has not yet met the required repeated-turn blocked audit. The pending
three non-flash Z.ai rounds, remaining DeepSeek rounds, and final Grok
128-worker round after DeepSeek are unchanged. Extra documentation commits
must never stand in for completed training rounds.
