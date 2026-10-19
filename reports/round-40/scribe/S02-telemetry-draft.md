- Seat: S02 | scribe | cross (telemetry draft) | date 2026-10-19 | baseline fd55e1f

## Purpose

Draft of the round-40 telemetry set the integrating parent lands under
`reports/round-40/telemetry/`, per the AGENTS.md availability/dispatch rules.
Everything below observed from the S02 seat vantage is labeled **partial**.
Unknown counters stay `null` with owner + reason; nothing is inferred from
landed files. No credentials, authorization headers, or prompt payloads.

## 1. What S02 observed from the seat vantage (partial)

- **Declared snapshot present and digest-verified.**
  `reports/round-40/telemetry/dispatch-declared.json` exists; sha256
  `abffc26b4cd3a7e9de2b6ab819803cf6221485c8d231123ac395ccee1d81d080`
  (command `sha256sum reports/round-40/telemetry/dispatch-declared.json`,
  2026-10-19). Its two `durable_sources` digests match the live bytes:
  `claims.json` = `a2e122c60f66c64bbdce5b7e44922075a40c848ec3e551f8f3c8c63a9b5a22c0`,
  `targets.json` = `710b81ccde9dd6e218d35fef3e951acc2b1ba7d94fadd509de9cbb65476afe72`
  (same command/date). Requested allocation per that record: zai-coding-plan /
  glm-5.3-flash, 24 workers, 1 batched call (dispatch-declared.json:6-11).
- **Baseline holds.** `git rev-parse HEAD` = `fd55e1f...` =
  declared `baseline_commit` (dispatch-declared.json:14). `git status
  --porcelain` shows only `M LOG.md` (parent integration) and untracked
  `reports/round-40/` — no seat-side drift into filed bytes (observed
  2026-10-19T14:08:33Z).
- **Seat census — partial observation, seat vantage.** Landed out-paths are
  launch+completion evidence for the seats that wrote them; absent out-paths
  are in-flight **or** failed — indistinguishable from here. Counting command
  (reproducible, run 2026-10-19):

  ```bash
  python3 -B - <<'EOF'
  import json, os
  t = json.load(open('reports/round-40/targets.json'))
  peers = [s['out'] for s in t['seats'] if s['id'] != 'S02']
  landed = sorted(o for o in peers if os.path.exists('reports/round-40/' + o))
  print(f"peers={len(peers)} landed={len(landed)} absent={len(peers)-len(landed)}")
  print("landed:", landed)
  EOF
  ```

  - 2026-10-19T14:08:33Z: peers=23 landed=3 (plan/P01-plan.md,
    calib/Ca03-receipt.md, cross/X01-trades.md)
  - 2026-10-19T14:09:20Z: peers=23 landed=4 (+ adj/A01-audit.md), absent=19

  The delta between the two samples is direct evidence the batch was still
  live at 14:09Z (declared 13:38:42Z; r39's 16-seat batch ran ~73 min, so a
  24-seat batch still in flight at 30 min is expected, not anomalous).
- **`reports/round-40/validation.json` does not exist** as of
  2026-10-19T14:09:20Z (`os.path.exists` probe). Therefore the declared
  snapshot's `closing_snapshot: open-at-seat-close` (dispatch-declared.json:25)
  is still owed — see §3.

## 2. Files the integrator lands under `reports/round-40/telemetry/`

Convention follows rounds 38/39 (`reports/round-39/telemetry/`):

1. `telemetry/inputs/claims.json` + `telemetry/inputs/targets.json` — copies
   of the round inputs, digests as in §1 (convention: r38/r39
   `telemetry/inputs/`). Owner: integrator.
2. `telemetry/observed-dispatch.json` — template (r39 shape,
   observed-dispatch.json:9-22). Requested allocation stays verbatim from the
   declared snapshot, separate from observed counters:

   ```json
   {
     "record": "observed-dispatch", "round": 40,
     "state": "open-at-seat-close",
     "owner": "orchestrator (goal-mode parent)",
     "reason": "counters filled; closes when availability-close-40.json lands",
     "observed_window_utc": "<declared 2026-10-19T13:38:42Z> / <batch close>",
     "requested_allocation": {"provider_lane": "zai-coding-plan",
       "model": "glm-5.3-flash", "requested_workers": 24, "batched_calls": 1},
     "launched_workers": null,
     "completed_workers": null,
     "failed_workers": null,
     "failed_workers_note": "<any re-dispatch, r39-C05 precedent; else omit>",
     "runtime_concurrency": null,
     "runtime_concurrency_owner": "orchestrator",
     "runtime_concurrency_reason": "not observable from the parent",
     "actual_route": "<wire route as observed; declared = zai-coding-plan lane, glm-5.3-flash>",
     "durable_sources": ["claims.json", "targets.json", "dispatch-declared.json — digests in §1"]
   }
   ```

   The three `null` worker counters are filled ONLY by the orchestrator from
   the AgentSwarm result — never from landed out-paths (a landed file proves
   its seat completed, but absence proves nothing; see §1 census). Owner:
   orchestrator.
3. `telemetry/availability-close-40.json` — **owed, not landable yet.**
   Schema `kotodama-availability-closing-snapshot-v1` (r39 precedent,
   availability-close-39.json:1-24). Filed ONLY once
   `reports/round-40/validation.json` lands; it is a NEW append-only file
   (never an in-place edit) that:
   - names `closes: reports/round-40/telemetry/dispatch-declared.json` and
     `closes_sha256` re-verified at close time (digest at S02 draft time:
     `abffc26b…d080`; any later in-place edit of the declared record becomes a
     detectable mismatch);
   - fills every open field (launches, completions, failures, window, route,
     runtime_concurrency) each citing its durable artifact, or records
     `could-not-recover` with owner + reason (r39 recovered
     `runtime_concurrency` as could-not-recover/null — likely the same here);
   - carries the validation.json receipt reference. Provider liveness is not
     round acceptance; the close fills counters, it does not admit the round.

   Label all partial samples (e.g. the §1 census) as partial when cited.
   If any launch-level failures occur, record them r38-style with class +
   basis + disposition (availability-attempt-1.json:1-16), never as inferred
   zeroes.

## 3. Not observable from the seat vantage (owner: orchestrator)

`launched_workers`, `completed_workers`, `failed_workers`, per-seat failure
classes at launch, `runtime_concurrency`, and the actual wire route per seat.
These stay `null` in my draft; the integrator fills them from the swarm
result and closes the record per AGENTS.md. This draft does NOT claim
24/24/0.

## Owed

- `reports/round-40/telemetry/observed-dispatch.json` — owner: orchestrator;
  fill from the AgentSwarm result at batch close (template §2.2).
- `reports/round-40/telemetry/inputs/claims.json` + `targets.json` — owner:
  integrator; digests in §1.
- `reports/round-40/telemetry/availability-close-40.json` — owner:
  integrator; owed once `reports/round-40/validation.json` lands (§2.3); the
  round is not admitted to LOG.md while this is open (AGENTS.md
  close-what-you-open).
- S01's integration dossier should cite this draft for the telemetry leg of
  the fleet report.

## Citations

- `reports/round-40/telemetry/dispatch-declared.json:6-11` (allocation),
  `:14` (baseline fd55e1f), `:15-24` (durable sources + digests), `:25`
  (closing snapshot open-at-seat-close); file sha256
  `abffc26b4cd3a7e9de2b6ab819803cf6221485c8d231123ac395ccee1d81d080`
  (`sha256sum`, 2026-10-19).
- Digest cross-check output (2026-10-19T14:08:33Z): claims.json
  `a2e122c6…5a22c0`, targets.json `710b81cc…afe72` — both match the declared
  snapshot's `durable_sources`.
- `git rev-parse HEAD` = `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106`;
  `git status --porcelain` = `M LOG.md` + `?? reports/round-40/` (2026-10-19T14:08:33Z).
- Seat census command + outputs at 2026-10-19T14:08:33Z (3/23) and
  2026-10-19T14:09:20Z (4/23: + adj/A01-audit.md) — §1, reproducible command
  quoted.
- `reports/round-39/telemetry/observed-dispatch.json:9-22` (field template,
  null-with-owner convention), `reports/round-39/telemetry/availability-close-39.json:1-24`
  (closing-snapshot schema + could-not-recover precedent),
  `reports/round-38/telemetry/availability-attempt-1.json:1-16` (failure-class
  labeling precedent), `reports/round-39/telemetry/inputs/` +
  `reports/round-38/telemetry/inputs/` (inputs-copy convention).
- `AGENTS.md` telemetry rules (durable samples, null-with-owner, closing
  snapshot owed before LOG.md admission, no credentials in telemetry).
