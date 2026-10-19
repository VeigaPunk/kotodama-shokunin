- Seat: S02 | scribe | cross | date 2026-10-19 | baseline 456674d

# Telemetry draft

Axes: cross. This capture supports dispatch/availability accounting only; it does not verify either the operability or calibration claim.

At 2026-10-19T15:42:23Z, the durable round-41 evidence available to this seat declared one batched openai-codex / gpt-6-luna-max allocation of 32 workers. The targets file has 32 seat objects, including S02. These are declared/requested counts, not observed launches or completions. The telemetry directory contained only `dispatch-declared.json`; no durable observed-dispatch/result extract or `validation.json` was present in the round listing at capture. Therefore observed launches, completions, failures, runtime concurrency, actual route, and the actual dispatch window are `null` / `could-not-evaluate`, not inferred from the allocation or seat census.

## Integrator draft: observed-dispatch record

This is a draft from S02's limited filesystem observation, not a filed telemetry snapshot. Replace `null` counters only from durable native dispatch/result evidence; unknowns must retain an owner and reason. Do not use this as proof of round acceptance.

```json
{
  "record": "observed-dispatch",
  "round": 41,
  "state": "partial; could-not-evaluate observed counters",
  "owner": "orchestrator (goal-mode parent)",
  "observed_at_utc": "2026-10-19T15:42:23Z",
  "observed_window_utc": null,
  "observed_window_owner": "orchestrator (goal-mode parent)",
  "observed_window_reason": "The only durable timestamp available to S02 is the declaration time; no dispatch-start/end extract was present in reports/round-41/telemetry at capture.",
  "counting_command": "sha256sum reports/round-41/{claims.json,targets.json,telemetry/dispatch-declared.json}; jq -r '\"declared=\" + (.seat_count|tostring) + \" target_objects=\" + (.seats|length|tostring)' reports/round-41/targets.json; ls -1 reports/round-41 reports/round-41/telemetry",
  "counting_date": "2026-10-19",
  "requested_allocation": {
    "provider_lane": "openai-codex",
    "model": "gpt-6-luna-max",
    "requested_workers": 32,
    "batched_calls": 1
  },
  "launched_workers": null,
  "launched_workers_owner": "orchestrator (goal-mode parent)",
  "launched_workers_reason": "No durable native dispatch/result extract was available to S02 at capture; the requested allocation and seat census are not observed launches.",
  "completed_workers": null,
  "completed_workers_owner": "orchestrator (goal-mode parent)",
  "completed_workers_reason": "No durable native dispatch/result extract was available to S02 at capture.",
  "failed_workers": null,
  "failed_workers_owner": "orchestrator (goal-mode parent)",
  "failed_workers_reason": "No durable native dispatch/result extract was available to S02 at capture.",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "orchestrator (goal-mode parent)",
  "runtime_concurrency_reason": "Not observable from S02's durable filesystem evidence at capture.",
  "actual_route": null,
  "actual_route_owner": "orchestrator (goal-mode parent)",
  "actual_route_reason": "The declaration names the requested lane/model but no observed route evidence was available to S02.",
  "durable_sources": [
    {
      "path": "reports/round-41/claims.json",
      "sha256": "dc00fba12cca0e3df17d26242173c86487c757cd24d704827d818c1f1ceb3bf5"
    },
    {
      "path": "reports/round-41/targets.json",
      "sha256": "6c56cc9ba6a0487fcd2779fd461c916a50877cc4758852a202cc8c2b1de3f0e8"
    },
    {
      "path": "reports/round-41/telemetry/dispatch-declared.json",
      "sha256": "e4f4800c79bcf7ed8f6c98aed8a8b1097d473c78d5880d053cc13efcec45d623"
    }
  ],
  "finalization_note": "Once native observed dispatch/result evidence is persisted under reports/round-41/telemetry/, record its path and digest in a new observed-dispatch snapshot. After validation.json lands, the integrating parent must file a new availability-close-41.json snapshot (never edit an earlier record), name the exact record and its SHA-256 at close, and fill each recoverable field from cited durable evidence or mark it could-not-recover with owner and reason."
}
```

## Owed

- `reports/round-41/telemetry/observed-dispatch.json` — orchestrator to file after preserving redacted native dispatch/result evidence; S02 could not evaluate the observed counters or route from the available durable files.
- `reports/round-41/telemetry/availability-close-41.json` — integrating parent to file as a new, digest-pinned closing snapshot after `reports/round-41/validation.json` lands, per `AGENTS.md:32-39`.

## Citations

- `reports/round-41/claims.json:3-8` — loop/position, baseline, and declared provider/model/allocation.
- `reports/round-41/targets.json:1-10,223-227` — seat-count declaration/shared rules and S02 assignment.
- `reports/round-41/telemetry/dispatch-declared.json:1-26` — declaration owner/time, requested allocation, baseline, source digests, and open-at-seat-close note.
- `AGENTS.md:17-39` — durable evidence, owner/time/command/digests, null unknown counters, and mandatory append-only close after validation.
- Command output at 2026-10-19T15:42:23Z: `git rev-parse HEAD` returned `456674dec01b8c433d7635a0edb49448f7714e12`; `sha256sum` returned the three digests included above; `jq` returned `declared=32 target_objects=32 S02=[{"role":"scribe","claim":"cross","out":"scribe/S02-telemetry-draft.md"}]`; `ls -1 reports/round-41 reports/round-41/telemetry` showed only `claims.json`, `targets.json`, `op/`, `telemetry/`, and `dispatch-declared.json` at capture.
