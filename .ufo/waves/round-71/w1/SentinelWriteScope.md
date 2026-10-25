# Round 71 wave-1 write-scope audit

**Result: gaps found.** Reviewed `w1/spec.json`, `plan.json`, `wave1-dispatch.json`, and the registry/assignment manifests. The taskCall copy mirrors the plan tasks and context.

## Findings

- **`ScoutQuarantineFetch1`, `ScoutQuarantineFetch2`, `ScoutQuarantineFetch3`, `RevQuarantineCrossCheck`, `ScoutPackageIdMap` — forbidden read-only tree named.** Their instructions explicitly read `/home/vgpnk/Projects/shokuknow/...`; several label it READ-ONLY, and ScoutPackageIdMap says READ-ONLY. Even though no edit is requested, these violate the stated path boundary if “touch” includes access. Smallest fix: omit these items from the wave or move the needed data into an approved read-only input location under the lane or `/tmp`.
- **`ConnectorSiblings` — sibling lanes named.** It directs scans over `/home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` and sibling corpus paths. Although explicitly read-only/grep-only, that is access to sibling lanes, outside the allowed absolute-path roots. Smallest fix: remove the cross-lane scan or provide a permitted, staged input.
- **`ScoutCensusBaseline` — fleet-root script named.** It runs `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, outside the lane and `/tmp`; the context prohibits mutation of fleet-root scripts but does not prohibit reads. This nevertheless violates the requested absolute-path allowlist. Smallest fix: provide an approved copy/input under `/tmp` or adjust the audit boundary explicitly.

## Checks that passed

- All 37 task `Report:` trailers in the dispatched task list are relative `.ufo/waves/round-71/w1/<item>.md` paths; the spec's `reportDir` is likewise relative.
- Shared contexts in spec, plan, and dispatch state that pacman is paused and prohibit pacman transactions; they direct tooling through `/home/vgpnk/.omp/agent/RULES.md` and say official channels only. **Gap in context specificity:** the context does not reproduce the RULES.md channel order (uv, official binary, etc.); it only refers to that file and says official channels only. If “states the RULES.md tooling channel” requires spelling out the channel/order, this is a gap in `context` (and duplicated contexts).
- Context explicitly forbids mutation of sibling lanes, fleet scripts/templates, `.ufo/state`, watchdog log, `MANIFEST.json`, `.scratch`, and lane jj/git state/index. No instruction directs a write to those prohibited targets. Shokuknow reads and sibling scans above are explicitly read-only; the issue is access/path-boundary compliance, not an observed write directive.
- Paths in many tasks are relative to the declared lane root, while all explicit out-of-root absolute references identified above are the listed exceptions. No instruction directs mutation of a lane git/jj state.

No tools were installed.
