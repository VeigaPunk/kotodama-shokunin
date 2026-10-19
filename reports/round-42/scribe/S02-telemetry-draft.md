- Seat: S02 | scribe | cross (telemetry draft) | date 2026-10-19 | baseline ac47c78

# S02 — round-42 telemetry draft

Draft of the round-42 telemetry set the integrating parent lands under
`reports/round-42/telemetry/`, per `AGENTS.md:15-39`. Everything observed from
this seat is labeled **partial**; unknown counters stay `null` with an owner and
reason; nothing is inferred from landed files. No credentials, authorization
headers, or prompt payloads appear here.

Round identity: regimen 2, loop 1, position 10 = lane round 42, declared
`devin` / `deepseek-v4-1-flash-high`, 32 workers, one batched call
(`REGIMEN.md:19`; `reports/round-42/claims.json:5-8`;
`reports/round-42/telemetry/dispatch-declared.json:6-11`).

## 1. What S02 observed from the seat vantage (partial)

- **Declared snapshot present and digest-verified.** `reports/round-42/telemetry/dispatch-declared.json`
  exists; sha256 `50d29b3f60e3cff471842796798507fc8c0df321893988eccf6dbec70713aff4`
  (`sha256sum reports/round-42/telemetry/dispatch-declared.json`, 2026-10-19).
  Its two `durable_sources` digests match the live bytes
  (`dispatch-declared.json:15-24` vs live, same command/date):

  | path | declared sha256 | live sha256 | match |
  |---|---|---|---|
  | `reports/round-42/claims.json` | `513ae21042c7516e028ff21675a48590b75f69dbb321da715efd7c49f3131b58` | same | yes |
  | `reports/round-42/targets.json` | `6db0a9ebcde81d555c48e80e75958f616d0990591357ee0421332b0c3c3b7b23` | same | yes |

- **Baseline holds.** `git rev-parse HEAD` =
  `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`, matching the declared
  `baseline_commit: ac47c78` (`dispatch-declared.json:14`,
  `claims.json:7`). `git status --porcelain` = `?? reports/round-42/` only — no
  seat-side drift into filed bytes (2026-10-19T15:58:36Z).

- **Seat census — partial observation, seat vantage.** Landed out-paths are
  launch+completion evidence for the seats that wrote them; absent out-paths are
  in-flight **or** failed, indistinguishable from here. Counting command
  (reproducible; the round's `counting_command` is "sha256sum + seat census"):

  ```bash
  export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
  python3 -B - <<'EOF'
  import json, os
  R = 'reports/round-42/'
  t = json.load(open(R + 'targets.json'))
  peers = [s['out'] for s in t['seats'] if s['id'] != 'S02']
  landed = sorted(o for o in peers if os.path.exists(R + o))
  print(f"peers={len(peers)} landed={len(landed)} absent={len(peers)-len(landed)}")
  print("landed:", landed)
  EOF
  ```

  | stamp (UTC) | peers | landed | absent | newly landed |
  |---|---|---|---|---|
  | 2026-10-19T15:58:36Z | 31 | 1 | 30 | `op/O09-scribe.md` |
  | 2026-10-19T15:58:56Z | 31 | 1 | 30 | — |
  | 2026-10-19T15:59:16Z | 31 | 1 | 30 | — |
  | 2026-10-19T15:59:36Z | 31 | 3 | 28 | `op/O10-gap-fill.md`, `scout/K01-n6-scout.md` |
  | 2026-10-19T16:00:00Z | 31 | 9 | 22 | `adj/A01-entries-bleed.md`, `calib/Ca01-gap-fill.md`, `cov/C08-verify.md`, `op/O06-receipt.md`, `op/O07-gap-fill.md`, `op/O08-queue-update.md` |
  | 2026-10-19T16:00:33Z | 31 | 13 | 18 | `cov/C02-entry-2.md`, `op/O03-predicted.md`, `op/O04-verify.md`, `plan/P01-plan.md` |

  The deltas between successive samples are direct evidence the batch was live
  across the 15:58:36Z–16:00:33Z window (declared at 15:55:18Z). A 32-seat
  batch still in flight 5 minutes in is expected, not anomalous. This census
  does **not** establish `launched_workers`, `completed_workers` or
  `failed_workers`; see §4. Counters in this table are point-in-time and will
  be stale by the time the integrator reads them — that is the point of the
  `open-at-seat-close` label, not a defect.

- **Not yet present at 16:00:33Z** (`os.path.exists` probes, same stamp):
  `reports/round-42/validation.json`, `reports/round-42/run-validation.py`,
  `reports/round-42/telemetry/observed-dispatch.json`,
  `reports/round-42/telemetry/availability-close-42.json`, and
  `reports/round-42/telemetry/inputs/` (directory absent). Therefore the
  declared snapshot's `closing_snapshot: "open-at-seat-close: owed once
  validation.json lands"` (`dispatch-declared.json:25`) is still owed — see §3.

## 2. Files the integrator lands under `reports/round-42/telemetry/`

Convention follows rounds 38/39/40/41 (`reports/round-41/telemetry/`).

### 2.1 `telemetry/inputs/claims.json` + `telemetry/inputs/targets.json`

Copies of the round inputs; digests as in §1 (convention: r38/r39/r40/r41
`telemetry/inputs/`). Owner: integrator.

### 2.2 `telemetry/observed-dispatch.json` — landable now, owner orchestrator

Template (r39/r40/r41 shape, `reports/round-41/telemetry/observed-dispatch.json`).
Requested allocation stays verbatim from the declared snapshot, kept separate
from observed counters:

```json
{
 "record": "observed-dispatch",
 "round": 42,
 "state": "open-at-seat-close",
 "owner": "orchestrator (goal-mode parent)",
 "reason": "counters filled; closes when availability-close-42.json lands",
 "observed_window_utc": "2026-10-19T15:55:18Z/<batch close>",
 "window_basis": "<the 32-seat devin/deepseek batch measured N s, as at r41:7>",
 "requested_allocation": {
  "provider_lane": "devin",
  "model": "deepseek-v4-1-flash-high",
  "requested_workers": 32,
  "batched_calls": 1
 },
 "launched_workers": null,
 "completed_workers": null,
 "failed_workers": null,
 "runtime_concurrency": null,
 "runtime_concurrency_owner": "orchestrator",
 "runtime_concurrency_reason": "not observable from the parent",
 "actual_route": "<wire route as observed; declared = devin lane, deepseek-v4-1-flash-high>",
 "durable_sources": [
  {"path": "reports/round-42/claims.json", "sha256": "513ae21042c7516e028ff21675a48590b75f69dbb321da715efd7c49f3131b58"},
  {"path": "reports/round-42/targets.json", "sha256": "6db0a9ebcde81d555c48e80e75958f616d0990591357ee0421332b0c3c3b7b23"},
  {"path": "reports/round-42/telemetry/dispatch-declared.json", "sha256": "50d29b3f60e3cff471842796798507fc8c0df321893988eccf6dbec70713aff4"}
 ]
}
```

The three worker counters are filled **only** by the orchestrator from the
AgentSwarm result — never from landed out-paths (a landed file proves its seat
completed; absence proves nothing; see §1 census). If any seat fails at launch,
add `failed_workers_note` r39-style and file a `availability-attempt-1.json`
r38-style (class + basis + disposition,
`reports/round-38/telemetry/availability-attempt-1.json:1-16`). Owner:
orchestrator.

**Field-name discipline.** Keep the r38–r41 key family exactly. The r30
incident is the cautionary case: a second reader of the same filename under a
different schema (`date`/`seat`/`runtime`/`raw_evidence` vs
`counts_date`/`owner`/`stats`/`sources`) exited 1 with
`KeyError: 'date'` (`corpus/lessons/round-30.md:113`;
`reports/round-30/telemetry/check-dispatch.py:34-56`). No r30-style reader is in
scope for round 42; the r38–r41 family is.

### 2.3 `telemetry/availability-close-42.json` — **owed, not landable yet**

Schema `kotodama-availability-closing-snapshot-v1` (r39/r40/r41 precedent,
`reports/round-41/telemetry/availability-close-41.json:1-24`). Filed **only
once** `reports/round-42/validation.json` lands; it is a **new append-only
file**, never an in-place edit of the declared record. It must:

- name `closes: "reports/round-42/telemetry/dispatch-declared.json"` and
  `closes_sha256` re-verified at close time (digest at this draft:
  `50d29b3f60e3cff471842796798507fc8c0df321893988eccf6dbec70713aff4`, so any
  later in-place edit of the declared record is detectable as a mismatch);
- fill every open field — `observed_launches`, `observed_completions`,
  `observed_failures`, `observed_window_utc`, `actual_route`,
  `runtime_concurrency` — each citing the durable artifact it was read from, or
  record `could-not-recover` with owner and reason (r39/r40/r41 all recorded
  `runtime_concurrency` as `could-not-recover`/null with owner orchestrator —
  expect the same here);
- carry the `validation.json` receipt reference. Provider liveness is not round
  acceptance; the close fills counters, it does not admit the round.

**Ordering constraint (measured, not assumed).** The round runner reads
`telemetry/observed-dispatch.json` and `telemetry/availability-close-42.json`
into its receipt's `input_sha256` at run time
(`reports/round-41/run-validation.py:162-165` and `:198-199`). Consequences:

1. `observed-dispatch.json` should land **before** the acceptance run so its
   digest is covered by the receipt.
2. `availability-close-42.json` necessarily lands **after** `validation.json`
   exists — so a final runner re-run follows, as at r40
   (`reports/round-40/telemetry/availability-close-40.json:20-24`: "a final
   re-run follows so the receipt covers this file"). The re-run must use an
   isolated copy: the shared rule forbids executing `reports/round-*/run-validation.py`
   in-tree.

Label every partial sample (§1) as partial when cited. If any launch-level
failures occur, record them with class + basis + disposition — never as
inferred zeroes.

## 3. Not observable from the seat vantage (owner: orchestrator)

`launched_workers`, `completed_workers`, `failed_workers`, per-seat failure
classes at launch, `runtime_concurrency`, and the actual wire route per seat.
These stay `null` in this draft; the integrator fills them from the swarm result
and closes the record per `AGENTS.md:32-39`. This draft does **not** claim
32/32/0.

## 4. Compliance notes carried forward

- `reports/round-30/telemetry/` contains the two-schema producer/consumer pair
  (`dispatch-telemetry.py` producer, `check-dispatch.py` reader); no
  reconciliation is attempted here and none is in scope for round 42. Recorded
  as a standing integration hazard, not a round-42 defect
  (`corpus/lessons/round-30.md:113`).
- Round-42 telemetry in this draft contains no credentials, no authorization
  headers, and no prompt payloads (`AGENTS.md:29-31`). The `/skill:godspeed`
  directive bytes and seat prompts are not persisted.
- No filed bytes were read-modified or staged; the only write by this seat is
  this fragment.

## Owed

- `reports/round-42/telemetry/observed-dispatch.json` — owner: orchestrator;
  fill the three worker counters + window + route from the AgentSwarm result at
  batch close (template §2.2).
- `reports/round-42/telemetry/inputs/claims.json` + `inputs/targets.json` —
  owner: integrator; digests in §1.
- `reports/round-42/telemetry/availability-close-42.json` — owner: integrator;
  owed once `reports/round-42/validation.json` lands (§2.3). Per
  `AGENTS.md:37-39` the round is not admitted to `LOG.md` while its own
  availability record still owes this closing snapshot.
- S01's integration dossier should cite this draft for the telemetry leg of the
  fleet report.

## Citations

- `REGIMEN.md:19` — position 10 = lane round 42, `devin` /
  `deepseek-v4-1-flash-high`, 32–64 seats; `REGIMEN.md:34-50` — per-round
  record set incl. telemetry and the closing snapshot.
- `reports/round-42/claims.json:5-8` — declared dispatch; `:7` baseline
  `ac47c78`. `reports/round-42/targets.json:4-9` — shared rules.
- `reports/round-42/telemetry/dispatch-declared.json:6-11` (allocation), `:14`
  (baseline), `:15-24` (durable sources + digests), `:25` (closing snapshot
  open-at-seat-close); file sha256
  `50d29b3f60e3cff471842796798507fc8c0df321893988eccf6dbec70713aff4`
  (`sha256sum`, 2026-10-19).
- Digest cross-check output (2026-10-19T15:58:36Z): `claims.json`
  `513ae210…1b58`, `targets.json` `6db0a9eb…7b23` — both match the declared
  snapshot's `durable_sources`.
- `git rev-parse HEAD` = `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`;
  `git status --porcelain` = `?? reports/round-42/` (2026-10-19T15:58:36Z).
- Seat census command + outputs, five stamps 15:58:36Z–16:00:00Z (§1 table) —
  reproducible command quoted.
- `reports/round-41/telemetry/observed-dispatch.json` (field template;
  `null`-with-owner convention), `reports/round-41/telemetry/availability-close-41.json:1-24`
  (closing-snapshot schema + `could-not-recover` precedent),
  `reports/round-40/telemetry/availability-close-40.json:20-24` (post-close
  re-run precedent), `reports/round-38/telemetry/availability-attempt-1.json:1-16`
  (failure-class labeling precedent), `reports/round-38/telemetry/inputs/` +
  `reports/round-39/telemetry/inputs/` (inputs-copy convention).
- `reports/round-41/run-validation.py:162-165`, `:198-199` — the runner's
  `input_sha256` legs over the two telemetry files (ordering constraint §2.3).
- `corpus/lessons/round-30.md:113` and
  `reports/round-30/telemetry/check-dispatch.py:34-56` — the two-schema
  producer/consumer disagreement (§2.2 field-name discipline).
- `AGENTS.md:15-39` — telemetry rules: durable samples, `null`-with-owner,
  closing snapshot owed before `LOG.md` admission, no credentials.
