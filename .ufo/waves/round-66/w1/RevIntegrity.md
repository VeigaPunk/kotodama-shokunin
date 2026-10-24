# RevIntegrity — round-66 v2 dispatch integrity audit

Scope: `spec-v2.json` validity, `taskcall-v2.json` renderer provenance (no hand-edited tasks),
duplicated seat names, Report trailers, absolute paths in the spec context, and live dispatch
evidence under `.ufo/waves/round-66/`. Read-only: no jj/git writes, no registry rewrite, no
`ufo-swarm-wave.mjs run` (it persists the registry and would reset `updatedAt` evidence).

Verdict: **dispatch PASS with one scope-drift finding (F1) and two provenance/contract caveats.**
The spec is generator output, the taskcall is exactly the validator's rendering of that spec, all
64 seat names are unique, every rendered task carries a correct terminal Report trailer, and the
member registry cross-checks 64/64 against the spec. No hand-edited task text found.

## Checks and evidence

### 1. spec-v2.json is generator output, 64 items, valid role mix — PASS
- `python3 -B .ufo/waves/round-66/gen-spec.py | diff - .ufo/waves/round-66/spec-v2.json` → empty diff
  (byte-identical regeneration). File 73163 bytes, mtime 08:28:16.
- 64 items; names unique 64/64; roles: scout 18, reviewer 21, critic 6, mutation-tester 5,
  scribe 5, executor 4, revenger 2, connector 1, sentinel 1, simplifier 1 → build 28 / attack 36.
- Every item has 1–2 axes, all within the declared set `{coverage, operability, calibration, depth,
  freshness, adjacency}`; no empty-axes item. Note: `freshness` is declared but carried by 0 items.
- Row allocation is exactly the frozen set: the union of `S###` named by `ScoutRow01..12` is
  `S777..S800` (24 rows), no row uncovered, no row opened by two ScoutRow seats.

### 2. taskcall-v2.json is the validator's rendered payload, not hand-edited tasks — PASS
- Rendered `planToDispatchPayload(planSwarmWave(spec, {policy}))` from
  `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs` against `spec-v2.json` and
  deep-compared to `taskcall-v2.json`: **DEEP-EQUAL: True** (schema, wave, policy, counts,
  registry, compaction, taskCall context+tasks, resumeSends, note).
  The policy block injected was read from the file's own `policy` field; band numbers trace to
  `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json`
  (`maxLanes 256, minLanes 16, waveMinLanes 64, waveMaxLanes 128, ramp 5/700`).
- Every task body = `/skill:godspeed\n\n` + the item's `prompt` + renderer trailer; the only delta
  from spec prompt to dispatched task is the appended block
  `Lane bounds / Judged on / Milestone / Report:`. 64/64 otherwise exact.
- No duplicated task bodies (sha256 of all 64 distinct), and no duplicates after normalizing the
  seat-specific trailer path. Every task names its own seat; the single cross-seat name mention
  (`RevClaimO` → `RevSeparability`) is an intentional attack cross-reference, not a copy bug.
- No task instructs a direct write into the lane tree (`corpus/`, `tools/`, `reports/`, `docs/`):
  0 matches for write/append/edit/create verbs against those prefixes. Build output stays drafts.

### 3. Seat names and Report trailers — PASS
- Duplicated seat names: **none** (64 distinct in spec, 64 distinct in taskcall, order-identical,
  roles order-identical; no role/agent mismatch).
- All 64 rendered tasks end with
  `Report: write your scoped findings to .ufo/waves/round-66/w1/<SEAT>.md`, the path basename equals
  the seat name for all 64, and each `Judged on:` axis list equals the item's `axes` and
  `Milestone:` equals `r66-v2` (0 mismatches).
- Live effect: 55 of 64 seat reports present in `w1/` at audit time; the set of `w1/*.md` names is a
  subset of the spec names (no stray/foreign seat files), and no
  `/home/vgpnk/Projects/shokunin/.ufo/waves/round-66/` exists (relative trailers resolved to the lane
  root in practice).

### 4. Registry / one-wave evidence — PASS (with F2 caveat)
- `w1/swarm-registry.json` is `ufo-swarm-registry-v1`, 64 members, all `kind: spawn`,
  `createdAt == updatedAt == 2026-10-24T11:29:01.355Z` (one write; taskcall mtime 08:29:01.356).
- Registry names == taskcall task names (set equality), 0 role mismatches, 0 axes mismatches vs spec.
- `taskcall.counts = {spawn: 64, resume: 0, total: 64}`, `resumeSends: []`; the live coop roster
  exposes 64 `L1-kotodama-r66.*` seats plus L1, and every live seat name checked is in the spec.
- `run.stderr` 0 bytes. No `plan-*`/dispatch transcript for round-66 (round-65 kept
  `plan-run.stderr`/`plan-err.txt`), so the "ONE task call" fact is attested by the single registry
  write plus roster, not by a logged invocation.

### 5. Spec context absolute paths — PASS (with F3 wording caveat)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin` exists; base `94209e8f80969dbac48d56c5d0e2e6
  23635b8616` is reachable (`git cat-file -t` → commit) and equals the lane tip `94209e8`.
- `reports/round-66/claims.json` (mtime 08:23), `accept-c.py`, `accept-o.py`, `accept-ca.py`,
  `tools/check-claim-separability.py`, `telemetry/{dry-run-*,controls-*,census-start,s753-recapture,
  seat-evidence}.txt`, `/home/vgpnk/.omp/agent/RULES.md` all exist. Ordering is pre-wave:
  claims 08:23 < spec 08:28 < payload/registry 08:29.
- `reportDir` agrees across spec, payload registry block and registry: `.ufo/waves/round-66/w1`.

## Findings (severity order)

### F1 — MEDIUM — four reject-candidate seats write rows outside claim C's frozen 24-row set
`ScoutReject01..04` are told to "open the candidate … and decide admit-or-reject for a row slot
S801/S802/S803/S804", and on admission to write `rows/<SEAT>/row-S801.txt`. claims.json freezes
"exactly 24 registry rows S777-S800", and `accept-c.py` targets `NEW_IDS = range(777,801)` — so
S801–S804 have **no acceptance leg at all**.
Live impact, not hypothetical: at audit time `rows/` already contains
`row-S801.txt row-S802.txt row-S803.txt row-S804.txt` alongside the frozen rows
(`row-S779..S804` present, `S777/S778/S797/S798` still missing), i.e. all four frontier candidates
were admitted.
Consequence: if the L1 integrates them into `corpus/SOURCES.md`, four append-only registry rows
enter the corpus that the frozen predicate neither requires nor polices — the round's records cannot
state whether they were justified, and the "corpus 239→240 / 24 rows" accounting is silently
widened. If the L1 drops them, four seats' output is dead. Fix at integration: either land only
S777–S800 and record the four candidates as explicitly rejected/held (with their evidence kept
under `rows/`), or amend the claim record; do not let S801+ slip into the registry unclaimed.

### F2 — LOW — policy provenance is `source: "config"` but no single on-disk config reproduces the block
No config in `/home/vgpnk/Projects` or `/home/vgpnk/.config` declares
`maxLanes 256 / minLanes 16 / waveMinLanes 64 / waveMaxLanes 128` together. A second independent
sweep over the candidate set (`ufo-fsd-alpha/config/ufo.json` 256/32/32/256, bundled `config.json`
100/16/16/32, `shokunin-kaika/policy-ufo.json` 100/16/32/64 and `w1-dispatch.json` 100/16/32/64,
tower fixtures 100/16/16/32, 100/64/32/100, 32/16/16/32) found no quartet either. The band numbers match
`/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json`, but that file's
`globalRunnerCeiling` is null while the payload says `1056`, and `hardCeiling: 256` is a validator
constant — so the emitted `policy` block is a merge, not a byte echo, and the "config" attribution
is only reconstructible by inference. The identical block appears in round-65's
`taskcall-prepared-unissued.json`, so the numbers are stable across rounds, not freshly minted.
No legality defect: 64 seats sit inside both the fleet band (32–256) and the hyaku band (64–128).
Recommend the L1 record the exact `UFO_CONFIG_PATH` (or policy file) used, plus the `plan`/`run`
invocation, in the round's records; otherwise a later reader cannot re-derive the gate.

### F3 — LOW — write-path contract is stated as absolute, rendered as relative
Context Rules say "Absolute paths for writes, under
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/` only, at the exact paths your
item names", while every rendered per-seat trailer is relative
(`.ufo/waves/round-66/w1/<SEAT>.md`) and most task bodies also name relative `rows/…` / `stage/…`
targets. Empirically harmless here (55 reports landed in the lane `w1/`, no fleet-root
`.ufo/waves/round-66/` was created), but this seat's own cwd is the fleet root
(`/home/vgpnk/Projects/shokunin`), so any seat that writes before its first `cd` lands outside the
lane. Residual risk only; no evidence of a stray write in this wave.

### F4 — INFO — declared-but-unused axis and a misleading `maxLanes`
`freshness` is in `spec.axes` yet carried by 0 items (axes counts: coverage 36, calibration 30,
operability 18, depth 14, adjacency 3). The spec declares no `maxLanes`, so the payload echoes the
policy cap 256 while the hyaku gate is `waveMaxLanes 128`; a reader could over-read headroom. The
64-seat count is legal under both.

## Residual risk / verification gaps
- I did not execute `ufo-swarm-wave.mjs run` (it rewrites `w1/swarm-registry.json`, resetting
  `updatedAt`); provenance was proven by function-level re-render, which is stronger for content but
  does not re-test the CLI's config load (`UFO_CONFIG_PATH` merge) that produced F2.
- "ONE task call" cannot be proven from disk alone: a split dispatch issued after the same single
  `run` would leave an identical registry. Evidence for oneness is indirect (single registry write,
  no resume entries, 64 concurrent live seats).
- Roster cross-check was limited to the 34 names the coop roster prints (34 more live + 546 parked
  omitted); all checked names are in the spec.
- 9 of 64 seats had not yet written `w1/*.md` at audit time; that is liveness, not an integrity
  defect.
- Factual quality of seat prompts (source tiers, quote requirements) was not judged here; that is
  the coverage/calibration seats' scope.

## Tooling
No installs or upgrades were needed (node/python3/ufo validator already present); nothing to record
under the operator tooling directive.

Report: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/w1/RevIntegrity.md
