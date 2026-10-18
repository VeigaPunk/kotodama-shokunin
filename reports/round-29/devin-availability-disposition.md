# Devin availability verification — could-not-evaluate disposition (2026-10-18)

The round-29 C claim asks for the devin provider's availability numbers to be
verified against traffic samples. The samples (`.scratch/x41/sample-*.json`,
`.scratch/x59/sample*.json`, `.scratch/x53*/sample.json`) were wave-time
telemetry captured by seats that never landed them to a durable path; the
lane's `.scratch` is cleaned between rounds, so they are unrecoverable.

What IS durable and verified present: the four rounds' availability records —
`reports/round-25/availability.json`, `reports/round-26/availability.json`,
`reports/round-27/availability.json`, `reports/round-28/availability.json` —
each carrying the route, requested/completed workers, and wall time. The
partial verification: all four records agree on the route
`devin/deepseek-v4-1-flash-high`, requested 64, completed in {26, 24, 24, 24},
wall times consistent with a ~30-55 min wave.

Cause class: process defect (telemetry not persisted to the round repo).
Round-30 fix (routed): availability seats must write telemetry under
`reports/round-<N>/telemetry/` (durable), never only `.scratch`.

This is a documented could-not-evaluate, not a pass. The durable records stand
as partial evidence; the sample-level verification is not claimed.
