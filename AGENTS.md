# kotodama-shokunin operating rules

- Work only within this repo and its PROVINCE.md scope; siblings, the world
  bible, and domain source trees are read-only.
- Every change is recorded in an append-only LOG.md entry with the evidence
  that motivated it. During a parallel wave, workers write only their assigned
  evidence fragments; the parent integrates them into LOG.md after the batch.
  Workers never race to append shared bookkeeping or claim independent
  promotion verification.
- Never fabricate domain knowledge or sources: cite a file, a command
  output, or a source; claims you cannot verify are marked `to-verify`.
- Canon decisions are lore-shokunin's; this lane generates systems and
  hands them off, and reports contested scope instead of absorbing it.

## Availability and dispatch telemetry

- Persist availability samples and dispatch evidence under
  `reports/round-<N>/telemetry/`, never only `.scratch`. Before scratch cleanup
  or worker handoff, land the redacted raw samples or native dispatch/result
  extracts needed to reproduce every reported count, not just a summary.
- Each telemetry snapshot names its owner, observation time or closed sampling
  window, counting command and date, durable source paths and SHA-256 digests.
  Keep requested allocation/model separate from observed launches, completions,
  failures, runtime concurrency and actual route; label partial observations.
  Unknown counters stay `null` with an owner and reason, not inferred zeroes or
  claimed completion rates. Provider liveness is not round acceptance.
- Summaries cite the durable samples. If evidence is missing, record
  `could-not-evaluate`; do not reconstruct historical samples or rewrite filed
  rounds. Corrections and final-wave updates are new snapshots or rows with
  their own provenance. Never persist credentials, authorization headers or
  private prompt payloads in telemetry.
