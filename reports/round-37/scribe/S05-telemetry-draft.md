- Seat: S05 | scribe | cross | date 2026-10-19 | baseline 57c8409

Draft only: this is a handoff template, not observed round-37 telemetry. The filed declaration names owner `orchestrator (goal-mode parent)`, requests `openai-codex` / `gpt-6-luna-max`, 64 workers in one batch, and leaves closure owed once `validation.json` lands [reports/round-37/telemetry/dispatch-declared.json:2-16]. At inspection, neither `reports/round-37/telemetry/observed-dispatch.json` nor `reports/round-37/validation.json` existed (command evidence below); no launch, completion, failure, route, or window values are asserted here.

## Observed-dispatch template

Create the actual record under `reports/round-37/telemetry/observed-dispatch.json` only after the dispatch result is available. Replace every placeholder with captured evidence. Keep unknown counters `null` with an owner and reason; never convert unknowns to zero or infer runtime concurrency. Separate the requested allocation from observed launches/completions/failures and actual route, as required by AGENTS.md:21-26. The prior records show the observed field pattern and use native batch result/per-seat outcomes as counting evidence [reports/round-33/telemetry/observed-dispatch.json:2-27; reports/round-36/telemetry/observed-dispatch.json:2-27].

```json
{
  "record": "observed-dispatch",
  "round": 37,
  "state": "open-at-seat-close",
  "owner": "orchestrator (goal-mode parent)",
  "reason": "Open pending the round-37 validation receipt; close with a separate snapshot per AGENTS.md:32-39.",
  "observed_window_utc": "<UTC start/end from dispatch result>",
  "window_basis": "<how the observed window was measured>",
  "counting_command": "<exact native batch-result and per-seat outcome counting command/evidence>",
  "counting_date": "<date the count was taken>",
  "requested_allocation": {
    "provider_lane": "openai-codex",
    "model": "gpt-6-luna-max",
    "requested_workers": 64,
    "batched_calls": 1
  },
  "launched_workers": null,
  "launched_workers_basis": "<captured result summary and/or seat outcomes; owner + reason if unknown>",
  "completed_workers": null,
  "failed_workers": null,
  "failed_workers_note": "<basis and any failure classification; owner + reason if unknown>",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "orchestrator",
  "runtime_concurrency_reason": "<measured basis, or why it is not observable>",
  "actual_route": "<observed provider lane and wire model, or null with owner/reason>",
  "durable_sources": [
    {
      "path": "reports/round-37/claims.json",
      "sha256": "85f0c43bd3368e4620bd16a028b5cbf7014d620f8dc7ad145056691d7ad7b8a5"
    },
    {
      "path": "reports/round-37/targets.json",
      "sha256": "3efe5733a144fca60a1cecb7bf4b35548e1630b79bf46ce5cefc09eeb59f440a"
    },
    {
      "path": "reports/round-37/telemetry/dispatch-declared.json",
      "sha256": "d2eb583efff9bddbdee0879f30507459a47c23886515853a92d3ea43b47d1884"
    },
    {
      "path": "<redacted native dispatch/result extract>",
      "sha256": "<digest>"
    }
  ]
}
```

If actual pre-batch launch failures occur, persist each as its own `availability-attempt-N.json` under the round's telemetry directory and cite its durable evidence; don't merge failed attempts into the completed batch's worker counters. Round 35 demonstrates separate attempt records and a separately stated completed-batch count [reports/round-35/telemetry/observed-dispatch.json:18-36]. Persist redacted raw samples/native extracts, not only summaries, and never credentials or private prompt payloads [AGENTS.md:17-31].

## Closing-snapshot skeleton

After `reports/round-37/validation.json` lands, the integrating parent files a new append-only `reports/round-37/telemetry/availability-close-37.json`; do not edit the declaration or observed-dispatch record. Recompute `closes_sha256` at close time and populate every value from a named durable artifact, or identify it as `could-not-recover` with owner and reason [AGENTS.md:32-39]. The prior snapshots use this schema; round 36 confirms closure also applies to a rejected validation receipt [reports/round-33/telemetry/availability-close-33.json:2-23; reports/round-36/telemetry/availability-close-36.json:15-21].

```json
{
  "schema": "kotodama-availability-closing-snapshot-v1",
  "round": 37,
  "date": "<snapshot date>",
  "closes": "reports/round-37/telemetry/dispatch-declared.json",
  "closes_sha256": "<sha256 recomputed at close time>",
  "closed_fields": {
    "observed_launches": "<value + reports/round-37/telemetry/observed-dispatch.json field/source>",
    "observed_completions": "<value + source>",
    "observed_failures": "<value + source; keep pre-batch attempts distinct>",
    "observed_window_utc": "<value + source>",
    "actual_route": "<value + source>",
    "runtime_concurrency": "<measured value + source, or could-not-recover with owner/reason>"
  },
  "could_not_recover": [
    "<each unresolved field, with owner and reason; empty only when none remain>"
  ],
  "owner": "integrator (goal-mode parent), for the lane",
  "reason": "Filed after reports/round-37/validation.json lands; each closed value cites its source.",
  "sources": [
    "reports/round-37/telemetry/dispatch-declared.json (sha256 <re-verified digest at close>)",
    "reports/round-37/telemetry/observed-dispatch.json (sha256 <digest>)",
    "reports/round-37/validation.json (<acceptance/rejection result and receipt evidence>)"
  ]
}
```

The current declaration's digest from the inspection command was `d2eb583efff9bddbdee0879f30507459a47c23886515853a92d3ea43b47d1884`; it is only a point-in-time digest, not the closing digest. Do not copy it without recomputing it when the closing snapshot is made. Keep availability/liveness separate from acceptance: the validation outcome is a separate source, not inferred from dispatch counters [AGENTS.md:23-27].

## Owed

- `reports/round-37/telemetry/observed-dispatch.json`: actual native batch/result evidence and observed counts/route/window are not available to S05; populate from the orchestrator's dispatch result. If unavailable, document `could-not-evaluate`, owner, and reason rather than reconstructing [AGENTS.md:27-31].
- `reports/round-37/telemetry/availability-close-37.json`: integrating parent must file after `reports/round-37/validation.json` lands, rehash the declaration at close, and cite the durable source for each resolved field [AGENTS.md:32-39].

## Citations

- `reports/round-37/telemetry/dispatch-declared.json:2-16` — requested route/allocation, declared counting inputs and digests, owner, and open-at-seat-close status.
- `reports/round-33/telemetry/observed-dispatch.json:2-27` — observed-dispatch record fields, independent requested/observed values, route, and unknown concurrency treatment.
- `reports/round-35/telemetry/observed-dispatch.json:18-36` — example distinguishing pre-batch attempts from completed batch counters and recording route deviation.
- `reports/round-33/telemetry/availability-close-33.json:2-23` — closing-snapshot schema and source attribution.
- `reports/round-36/telemetry/availability-close-36.json:15-21` — rejected round closure example.
- `AGENTS.md:17-39` — durable/redacted evidence, null unknowns, and append-only closing-snapshot requirements.
- Command output (2026-10-19): `sha256sum reports/round-37/telemetry/dispatch-declared.json reports/round-37/claims.json reports/round-37/targets.json` returned, respectively, `d2eb583efff9bddbdee0879f30507459a47c23886515853a92d3ea43b47d1884`, `85f0c43bd3368e4620bd16a028b5cbf7014d620f8dc7ad145056691d7ad7b8a5`, and `3efe5733a144fca60a1cecb7bf4b35548e1630b79bf46ce5cefc09eeb59f440a`. The same command checked `reports/round-37/telemetry/observed-dispatch.json` and `reports/round-37/validation.json`; both were absent at inspection.
