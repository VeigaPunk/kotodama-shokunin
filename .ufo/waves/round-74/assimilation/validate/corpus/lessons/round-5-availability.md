# Round 5 preparation — native model registry refusal

source: reports/round-5/claims.json, prompt-template.txt, dispatch-plan.json and availability-attempt-1.json; baseline c52f2c07abcfae4d363e6057e3bc7f60b1329efc
verified-at: 2026-10-17; actual native AgentSwarm returned Invalid model before launch
recheck: retry the exact native non-flash alias only after a meaningful availability interval or host change; retain every refusal and do not substitute Flash

## Observed preparation

Two measurable targets were declared before the attempt: freshness through
follow-ups on unresolved source rows, and operability through isolated gate
selftests plus clearer malformed-input handling. The prepared request has
16 distinct assignments, including ten source workers covering the twenty
unresolved supplemental rows. Baseline CLI probes reproduced six exit-1
tracebacks; the existing ten-mutation selftest still passed. No target
improvement is claimed from this preparation.

The native AgentSwarm request for `zai-coding-plan/glm-5.3` was rejected with
`Invalid model` before any worker launched. Its available-model list names
only `zai-coding-plan/glm-5.3-flash-low` on Z.ai. That is evidence about this
host tool's registry, not proof that the provider itself is broken or that a
provider request was rate-limited. A cooldown cannot by itself establish a
missing native alias. The operator may have a functioning route elsewhere;
this attempt did not reach it.

## Gate

Candidates: two pending claims in claims.json, prepared for one 16-worker
non-flash Z.ai batch. Admitted: none. Rejected as a completed round: this
preflight attempt, because zero workers launched and no after-measurement
exists. The scientific/craft claims themselves remain pending, not
retrospectively tested or relabelled. All six axes are unchanged.

Spot check: exact native refusal and prepared-file digests are retained in
availability-attempt-1.json. No source follow-up, corpus correction, tool
implementation, independent promotion review or canon acceptance occurred.
The supplementary OpenCode Go work remains separate and already published.

## Consequence

Keep round 5 pending. Do not turn retry documentation or extra Git commits
into completed-round credit. Do not route through an implicit default,
Flash alias or custom provider client and call the result non-flash Z.ai.
The prepared source partitions and baseline are reusable if the exact
native route becomes available; recheck the worktree baseline before reuse.
This lesson documents an attempted dispatch, not completion of the training
goal, rank promotion, fleet closure or satisfaction of the model schedule.
