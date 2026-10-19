# kotodama-shokunin — Regimen 2 contract (operator-approved 2026-10-19)

Run the kotodama-shokunin lane through a new 3-loop × 14-round training
regimen — 42 lane rounds, numbered 33–74 continuing this repo's ledger
(rounds 1–32 are closed, never re-dispatched) — each round executed under the
shokunin protocol: 1–3 declared axis-move claims, per-axis verdicts, honest
stop.

## Schedule (position → lane rounds per loop)

| # | Lane rounds | Provider / model | Swarm | Role |
|---|---|---|---|---|
| 1–3 | 33–35 / 47–49 / 61–63 | opencode-go / deepseek-v4.1-flash, round-robin across live opencode-go keys per round | 64 | build |
| 4 | 36 / 50 / 64 | hyper / deepseek-v4.1-flash; fallback devin/deepseek-v4-1-flash-high | 32–64 | build |
| 5 | 37 / 51 / 65 | openai-codex / gpt-6-luna-max | 64 | loop verify |
| 6 | 38 / 52 / 66 | xai-oauth / grok-4.7-fast (xhigh) | 32–64 | build |
| 7–8 | 39–40 / 53–54 / 67–68 | zai-coding-plan / glm-5.3-flash MAX-effort seats | 16–32 | build |
| 9 | 41 / 55 / 69 | openai-codex / gpt-6-luna-max | 32–64 | mid-loop verify |
| 10 | 42 / 56 / 70 | devin / deepseek-v4-1-flash-high | 32–64 | build |
| 11 | 43 / 57 / 71 | zai-coding-plan / glm-5.3-flash-low (pinned MAX) | 32 | build |
| 12 | 44 / 58 / 72 | antigravity / gemini-3.8-flash | 32–64 | build |
| 13 | 45 / 59 / 73 | antigravity / gemini-4-argon (max effort) | 8 | deep/hard build |
| 14 | 46 / 60 / 74 | devin / swe-2 | 8 | git commit/push/merge correctness audit — read-only audit + report; performs no pushes/merges |

## Per-round contract (all 42 rounds)

- Declare the axis set from `SCORECARD.md`; declare 1–3 claims, each one
  axis-move on a distinct axis with falsifiable before→after (counting
  command for measurable claims; named target + rationale for exploratory).
  At least one claim works the lane's lowest non-retired axis unless the
  stagnation nudge is invoked and recorded. Freshness axis-move claims stay
  paused (operator ruling pending since round 11) unless the operator lifts
  the pause in this regimen.
- Dispatch exactly ONE batched AgentSwarm per round at the declared size;
  every L2 prompt leads with `/skill:godspeed` + the verbatim directive bytes
  from `~/.agents/skills/godspeed/directive.md`.
- Land the work, measure on the delivered revision, judge EVERY axis
  (improved / harmed / unchanged / unprovable-but-better — the last only
  with a named non-author reviewer). No scalar aggregation; a trade is
  reported, never averaged into an accept.
- Admit only when every claim verifies and no axis is harmed; otherwise
  report the round rejected/harmed/unprovable and halt axis progression
  there — never force a pass (rounds 11/17/22 precedent).
- Record per round: verdicts + before→after in `SCORECARD.md`; append-only
  `LOG.md` entry under lane git identity `kotodama-shokunin
  <kotodama@shokunin.local>`; report at `.ufo/reports/round-<N>/kotodama.md`
  with Work performed / Landed changes / Before→after / SHONEN sections;
  `MANIFEST.json rounds[]` entry; telemetry per `AGENTS.md` at
  `reports/round-<N>/telemetry/` including the digest-pinned closing snapshot
  once `validation.json` lands.

## Done when

All 42 rounds (lane rounds 33–74) are dispatched and closed on record
(admitted or rejected), each carrying the full record set above, plus a
final loop-3 retrospective and closure ledger showing 42/42 closed; and for
every admitted round, `python3 reports/round-<N>/run-validation.py` exits 0
at close time.

## Scope

Only this repo (`kotodama-shokunin/`) and its `PROVINCE.md` scope; siblings,
world bible, domain source trees read-only. No fabricated sources — every
claim cites file/command/source. Installs on this host are allowed when they
increase capability, quality, coverage or depth; never persist credentials.
Provider deviations are permitted only as declared (hyper→devin fallback;
counts within declared ranges; skipping 402'd opencode-go keys with the
failure recorded); undeclared providers/models are not. No git push or merge
without explicit operator instruction.

## Stop and report

If a provider lane is exhausted or unreachable, apply the declared fallback
once; if that also fails, file the round `could-not-dispatch` with owner +
reason in telemetry and advance to the next scheduled round. If the same
blocking condition persists across 3 consecutive rounds, stop the regimen
and report to the operator instead of burning the loop.
