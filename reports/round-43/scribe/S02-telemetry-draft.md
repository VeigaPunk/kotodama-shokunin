# S02 — telemetry scribe: observed-dispatch + availability-close-43 skeletons

- Seat: **S02**, role scribe, claim cross (`reports/round-43/targets.json:43`).
- Round 43, loop 1, baseline `7ceff59` (`reports/round-43/claims.json:6`).
- Observed at `2026-10-19T16:55:37Z` (`date -u +%Y-%m-%dT%H:%M:%SZ`); local zone `-03`.
- Writes: **this file only** (`reports/round-43/scribe/S02-telemetry-draft.md`). Everything below is a draft for the integrator; nothing is filed under `reports/round-43/telemetry/` by this seat.
- Canon: NON-CANON. No corpus, tools, README, or filed-round byte touched; no runner executed; no commit/push/install/network.

Mission: draft the observed-dispatch and availability-close-43 skeletons (owner, observation window, counting commands, durable source paths + sha256 placeholders the integrator fills). The skeletons are in §3–§4; the provenance findings that shaped them are in §2; the fill procedure is in §6.

---

## 1. Durable inputs read at observation

| Path | Bytes | SHA-256 (measured `2026-10-19T16:55:06Z`) |
|---|---:|---|
| `reports/round-43/claims.json` | 6546 | `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b` |
| `reports/round-43/targets.json` | 12285 | `44d1f7ce1de23be7f92da6b5915770d05aab448b722acb33c0f8c0447f0f99cc` |
| `reports/round-43/telemetry/dispatch-declared.json` | 1387 | `76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe` |

Commands and raw output:

```console
$ sha256sum reports/round-43/claims.json reports/round-43/targets.json reports/round-43/telemetry/dispatch-declared.json
9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b  reports/round-43/claims.json
44d1f7ce1de23be7f92da6b5915770d05aab448b722acb33c0f8c0447f0f99cc  reports/round-43/targets.json
76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe  reports/round-43/telemetry/dispatch-declared.json
$ wc -c reports/round-43/claims.json reports/round-43/targets.json reports/round-43/telemetry/dispatch-declared.json
 6546 reports/round-43/claims.json
12285 reports/round-43/targets.json
 1387 reports/round-43/telemetry/dispatch-declared.json
```

Precedent read for schema: `reports/round-42/telemetry/{dispatch-declared,observed-dispatch,availability-close-42}.json`, `reports/round-39..41/telemetry/*`, `reports/round-30..32/telemetry/{worker-observation,dispatch-stats}.json`, `reports/round-35/telemetry/availability-attempt-{1,2,3}.json`, and the binding rules in `AGENTS.md` ("Availability and dispatch telemetry", "Close what you open").

---

## 2. Provenance findings

### T1 — the declared `claims.json` digest is stale (must be handled append-only)

`dispatch-declared.json` pins `claims.json` at 6353 bytes / `beda7644…`, but the live file at observation is 6546 bytes / `9662e2bd…` (`wc -c` + `sha256sum`, §1). `targets.json` matches exactly.

Evidence that the live file is a plain serialization (so the mismatch is not a re-indent artifact):

```console
$ python3 - <<'PY'
import json,hashlib
raw=open('reports/round-43/claims.json','rb').read()
d=json.loads(raw)
b=(json.dumps(d,indent=1,ensure_ascii=False)+'\n').encode()
print('bytes',len(b),'sha256',hashlib.sha256(b).hexdigest(),'equal_to_live',b==raw)
PY
bytes 6546 sha256 9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b equal_to_live True
```

A compact serialization of the same content is 6281 bytes (`sha256 567c85ed…`), so the declared 6353 bytes cannot be produced from the live content by any of indent=1, indent=2, or compact formatting. The declared row therefore names **different content** (or a staging copy that never landed), not a formatting variant.

Timing evidence (`TZ=UTC stat -c '%y %n'`):

```text
2026-10-19 16:53:15.764970004 +0000 reports/round-43/claims.json
2026-10-19 16:53:15.764970004 +0000 reports/round-43/telemetry/dispatch-declared.json
2026-10-19 16:41:31.611393200 +0000 reports/round-43/targets.json
```

Both files carry the identical nanosecond mtime while `claims.json` declares `declared_at_utc: 2026-10-19T16:40:27Z`; this is consistent with the digest being taken before the final claims content was written, or over a staging copy that did not land. **Cause: `to-verify`, owner integrator.** The rule-compliant fix is a new append-only amendment record (§5.1), never an edit to `dispatch-declared.json` (AGENTS: "Corrections and final-wave updates are new snapshots or rows with their own provenance").

### T2 — the pre-completion route history names two different intermediate lanes

`claims.json:5` says the operator redirected to **antigravity gemini-3.8-flash**; `claims.json:13` says the interruptions were zai ×2 followed by **cursor/gemini-4-argon** ×1. Both cannot describe the same attempt. No r43 availability-attempt record exists (compare r35/r38, which filed `availability-attempt-*.json`). The close must not average or guess this: record the route history with both citations and `to-verify`, or record `could-not-recover` + owner. My skeleton carries both rows explicitly (§3, `route_history`).

### T3 — `telemetry/inputs/` is absent

r39–r42 each carry `telemetry/inputs/{claims.json,targets.json}` byte-identical to the round root. Verified for all four rounds at observation:

```console
$ for r in 39 40 41 42; do for f in claims.json targets.json; do if diff -q reports/round-$r/$f reports/round-$r/telemetry/inputs/$f >/dev/null 2>&1; then echo "r$r $f identical"; else echo "r$r $f DIFF-or-MISSING"; fi; done; done
r39 claims.json identical
r39 targets.json identical
r40 claims.json identical
r40 targets.json identical
r41 claims.json identical
r41 targets.json identical
r42 claims.json identical
r42 targets.json identical
```

r43 has no `inputs/` directory at observation. AGENTS requires the durable samples to reproduce every reported count, so §6 step 2 stages these copies before scratch cleanup.

### T4 — close preconditions are not yet met

At `2026-10-19T16:55:06Z`:

```console
$ ls reports/round-43/run-validation.py reports/round-43/validation.json
ls: cannot access 'reports/round-43/run-validation.py': No such file or directory
ls: cannot access 'reports/round-43/validation.json': No such file or directory
```

The close snapshot is therefore **blocked** until `validation.json` lands. r42 precedent: a rejected round still closes (`availability-close-42.json` exists despite the rejection receipt). Acceptance is recorded in the receipt, never inferred from dispatch completions ("Provider liveness is not round acceptance", AGENTS).

### T5 — seat contract census is clean (reproducible)

```console
$ python3 - <<'PY'
import json
from collections import Counter
d=json.load(open('reports/round-43/targets.json'))
s=d['seats']
print('seat_count',d['seat_count'],'seats',len(s),'unique_ids',len({x['id'] for x in s}),
      'unique_outs',len({x['out'] for x in s}))
print('roles',dict(Counter(x['role'] for x in s)))
print('claims',dict(Counter(x['claim'] for x in s)))
print('escapes',[x['out'] for x in s if x['out'].startswith('/') or '..' in x['out'].split('/')])
PY
seat_count 32 seats 32 unique_ids 32 unique_outs 32
roles {'scout': 2, 'planner': 1, 'connector': 1, 'executor': 11, 'verifier': 9, 'scribe': 4, 'reviewer': 2, 'critic': 2}
claims {'O': 12, 'C': 8, 'cross': 9, 'Ca': 3}
escapes []
```

This is the reproducible count for `requested_workers: 32` in the contract; it is **not** a launch/completion count.

### T6 — partial availability samples (one worker, not a census)

Two read-only samples of seat deliverables:

```text
2026-10-19T16:53:55Z  find reports/round-43 -mindepth 2 -type f ! -path '*/telemetry/*' | wc -l  ->  0
2026-10-19T16:55:37Z  python3 seat-output census (non-empty files)                                   ->  1  (K02)
                      reports/round-43/scout/K02-landing-scout.md mtime 2026-10-19T16:55:30.942387704Z
```

Labeled `partial-worker-observation`; it proves one concurrent worker was active and one deliverable landed. It is **not** evidence of 32 launches, completions, failures, concurrency, wall time, or route. The optional `worker-observation-s02.json` (§5.3) preserves this sample under `telemetry/` if the integrator wants it durable before scratch cleanup.

### T7 — schema choices in this draft (improvements over r39–r42, all additive)

1. **Close both open records.** r39–r42 `availability-close-*.json` names `dispatch-declared.json` only, leaving `observed-dispatch.json` with `state: open-at-seat-close` forever. r43's `dispatch-declared.json` has no `closing_snapshot` field, while `observed-dispatch.json` will carry the literal open state; so the close names `observed-dispatch.json` as `closes` and adds `also_closes` for `dispatch-declared.json`, each with its own digest.
2. **Requested vs observed route separated.** Prior closes say "as declared", which is not an observation. The skeleton keeps `requested` and `observed` in one object and forbids copying the requested route into `observed`.
3. **Counters stay `null` with owner + reason until a native extract is filed.** Requested 32 must never be promoted to launched/completed. `completed + failed == launched` is asserted when every seat's start state is known; otherwise launched is `could-not-recover`.
4. **Receipt is recorded, not assumed.** `validation_receipt` carries path + digest + acceptance; a later re-run is a new snapshot row, never an in-place edit.

---

## 3. Skeleton A — `reports/round-43/telemetry/observed-dispatch.json`

Fence for the integrator; fill every `<FILL …>` before filing. `null` counters are deliberate: unknown is not zero.

```json
{
 "record": "observed-dispatch",
 "round": 43,
 "schema": "kotodama-observed-dispatch-v1",
 "state": "open-at-seat-close",
 "owner": "integrator (goal-mode parent)",
 "reason": "counters filled from inputs/dispatch-result.raw.json; closes when availability-close-43.json lands",
 "declared_at_utc": "2026-10-19T16:40:27Z",
 "declared_at_source": "reports/round-43/claims.json:6",
 "observation_closed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ at filing>",
 "observed_window_utc": "<FILL: min(started_at_utc)/max(ended_at_utc) from inputs/dispatch-result.raw.json>",
 "window_basis": "<FILL: native tool wall_seconds = N s; or 'could-not-recover' + owner>",
 "requested_allocation": {
  "provider_lane": "opencode-go",
  "model": "deepseek-v4.1-flash",
  "model_effort": null,
  "model_effort_note": "operator said 'max'; no -max alias is registered on opencode-go (claims.json:13)",
  "requested_workers": 32,
  "batched_calls": 1,
  "baseline_commit": "7ceff59"
 },
 "route_history": [
  {
   "attempt": "pre-1a",
   "lane": "zai-coding-plan",
   "model": "glm-5.3-flash-low",
   "status": "interrupted pre-completion x2",
   "source": "reports/round-43/claims.json:13",
   "durability": "to-verify: no r43 availability-attempt record filed (compare r35/r38 attempts)"
  },
  {
   "attempt": "pre-1b",
   "lane": "<CONFLICT: 'antigravity gemini-3.8-flash' (claims.json:5) vs 'cursor/gemini-4-argon' (claims.json:13)>",
   "model": "<CONFLICT: resolve from native dispatch records; do not guess>",
   "status": "interrupted x1",
   "source": "reports/round-43/claims.json:5 vs :13",
   "durability": "to-verify: integrator"
  },
  {
   "attempt": "1",
   "lane": "opencode-go",
   "model": "deepseek-v4.1-flash",
   "status": "the batch this record observes",
   "source": "reports/round-43/telemetry/dispatch-declared.json"
  }
 ],
 "launched_workers": null,
 "launched_workers_owner": "integrator",
 "launched_workers_reason": "fill as count(seats[].started == true) from inputs/dispatch-result.raw.json; if any started value is null, record could-not-recover + owner. Never copy requested_workers",
 "completed_workers": null,
 "completed_workers_owner": "integrator",
 "completed_workers_reason": "fill from seats[] outcome==completed",
 "failed_workers": null,
 "failed_workers_owner": "integrator",
 "failed_workers_reason": "fill from seats[] outcome==failed; write 0 only after the command returns 0",
 "failed_workers_note": "<FILL: seat ids + error classes; empty only if measured 0>",
 "counter_invariant": "completed + failed == launched, asserted by the fill command",
 "runtime_concurrency": null,
 "runtime_concurrency_owner": "integrator",
 "runtime_concurrency_reason": "not derivable from a flat batch result; no concurrent-session samples supplied (r39-r42 precedent: could-not-recover)",
 "actual_route": {
  "requested": "opencode-go / deepseek-v4.1-flash",
  "observed": null,
  "observed_owner": "integrator",
  "observed_reason": "fill from the native extract's wire model/provider response; do not copy the requested route",
  "basis": "<FILL: inputs/dispatch-result.raw.json#/route or 'could-not-recover' + owner/reason>"
 },
 "partial_observations": [
  {
   "kind": "worker-self-observation + seat-output presence",
   "candidate_path": "reports/round-43/telemetry/worker-observation-s02.json",
   "filing": "optional: file §5.3 before citing this path, else drop this row",
   "observed_at_utc": "2026-10-19T16:55:37Z",
   "observed_active_sessions": 1,
   "declared_seats": 32,
   "non_empty_seat_outputs": 1,
   "present": ["K02"],
   "scope": "one worker + one file-presence sample; not a dispatch census"
  }
 ],
 "durable_sources": [
  {
   "path": "reports/round-43/claims.json",
   "sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
   "bytes": 6546,
   "observed_at_utc": "2026-10-19T16:55:06Z",
   "note": "live digest; differs from dispatch-declared's stale 6353/beda7644 row — see dispatch-declared-amendment-1.json"
  },
  {
   "path": "reports/round-43/targets.json",
   "sha256": "44d1f7ce1de23be7f92da6b5915770d05aab448b722acb33c0f8c0447f0f99cc",
   "bytes": 12285,
   "observed_at_utc": "2026-10-19T16:55:06Z"
  },
  {
   "path": "reports/round-43/telemetry/dispatch-declared.json",
   "sha256": "76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe",
   "bytes": 1387,
   "observed_at_utc": "2026-10-19T16:55:06Z"
  },
  {
   "path": "reports/round-43/telemetry/inputs/dispatch-result.raw.json",
   "sha256": "<FILL at close: sha256sum reports/round-43/telemetry/inputs/dispatch-result.raw.json>",
   "bytes": "<FILL>"
  }
 ],
 "closing_snapshot": "open-at-seat-close: owed once reports/round-43/validation.json lands (admission or rejection; r42 rejection precedent)"
}
```

Filing rule: if no native dispatch result is retained, leave `launched_workers`/`completed_workers`/`failed_workers` `null`, set each owner/reason to `could-not-recover` with the integrator named, and say so in `window_basis`. Do **not** infer 32/32 from `requested_workers`.

---

## 4. Skeleton B — `reports/round-43/telemetry/availability-close-43.json`

Do not file until `reports/round-43/validation.json` exists. Digests are filled at close time, after the two source records are final.

```json
{
 "schema": "kotodama-availability-closing-snapshot-v1",
 "round": 43,
 "date": "2026-10-19",
 "filed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ>",
 "closes": "reports/round-43/telemetry/observed-dispatch.json",
 "closes_sha256": "<FILL: sha256sum reports/round-43/telemetry/observed-dispatch.json>",
 "also_closes": [
  {
   "path": "reports/round-43/telemetry/dispatch-declared.json",
   "sha256": "<FILL at close; expected 76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe unless the original was edited (forbidden)>",
   "note": "r39-r42 named this record; r43 names observed-dispatch as primary because that record carries state=open-at-seat-close"
  }
 ],
 "closed_fields": {
  "observed_launches": "<FILL: N (source: inputs/dispatch-result.raw.json)>",
  "observed_completions": "<FILL: N (same source)>",
  "observed_failures": "<FILL: N (classes: ...; same source)>",
  "observed_window_utc": "<FILL: start/end; basis: native wall_seconds, else could-not-recover + owner>",
  "actual_route": {
   "requested": "opencode-go / deepseek-v4.1-flash",
   "observed": "<FILL: wire model from the native extract, or could-not-recover>",
   "basis": "<FILL: path#/field or owner+reason>"
  },
  "runtime_concurrency": "could-not-recover as a measured counter: null with owner integrator (flat batch result; no concurrent-session samples)"
 },
 "could_not_recover": ["runtime_concurrency"],
 "owner": "integrator (goal-mode parent), for the lane",
 "reason": "closing snapshot filed once reports/round-43/validation.json landed (admission or rejection); every open field filled citing its durable artifact",
 "validation_receipt": {
  "path": "reports/round-43/validation.json",
  "sha256": "<FILL at close: sha256sum reports/round-43/validation.json>",
  "acceptance": "<FILL: true | false>",
  "caveat": "if the runner is re-run after close, file a new snapshot row; never edit this file (AGENTS 'Close what you open')"
 },
 "sources": [
  "reports/round-43/telemetry/dispatch-declared.json (sha256 re-verified at close)",
  "reports/round-43/telemetry/dispatch-declared-amendment-1.json (if filed)",
  "reports/round-43/telemetry/observed-dispatch.json (sha256 pinned above)",
  "reports/round-43/telemetry/inputs/dispatch-result.raw.json",
  "reports/round-43/validation.json"
 ]
}
```

---

## 5. Supporting records (optional but recommended)

### 5.1 `reports/round-43/telemetry/dispatch-declared-amendment-1.json`

Append-only provenance row for T1; the original declaration stays byte-untouched.

```json
{
 "record": "dispatch-declared-amendment-1",
 "round": 43,
 "owner": "integrator (goal-mode parent)",
 "filed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ>",
 "amends": "reports/round-43/telemetry/dispatch-declared.json",
 "amends_sha256": "76632d7354f4aa602c0ba9c5d1e4f6780bedb3a4a6e2a372cde724745c7f63fe",
 "class": "stale-declared-artifact-digest",
 "reason": "declared_artifacts['reports/round-43/claims.json'] does not match the live file; both files carry mtime 2026-10-19T16:53:15.764970004Z, so the digest was taken before the final content was written or over a staging copy that did not land under telemetry/inputs/",
 "artifact_rows": [
  {
   "path": "reports/round-43/claims.json",
   "declared": {"sha256": "beda7644ec91d61d511af1d62a44f8b93b782c8f68a726a9a57f1a7a80d135aa", "bytes": 6353},
   "observed_at_utc": "2026-10-19T16:55:06Z",
   "observed": {"sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b", "bytes": 6546},
   "match": false,
   "status": "to-verify",
   "owner": "integrator",
   "disposition": "availability-close-43.json cites the observed digest; dispatch-declared.json is not edited"
  },
  {
   "path": "reports/round-43/targets.json",
   "declared": {"sha256": "44d1f7ce1de23be7f92da6b5915770d05aab448b722acb33c0f8c0447f0f99cc", "seat_count": 32},
   "observed_at_utc": "2026-10-19T16:55:06Z",
   "observed": {"sha256": "44d1f7ce1de23be7f92da6b5915770d05aab448b722acb33c0f8c0447f0f99cc", "seats": 32, "unique_ids": 32, "unique_outs": 32},
   "match": true,
   "status": "verified"
  }
 ],
 "verification": {
  "command": "sha256sum reports/round-43/claims.json reports/round-43/targets.json; wc -c reports/round-43/claims.json",
  "output": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b  reports/round-43/claims.json\n44d1f7ce1de23be7f92da6b5915770d05aab448b722acb33c0f8c0447f0f99cc  reports/round-43/targets.json\n6546 reports/round-43/claims.json"
 },
 "sources": [
  "reports/round-43/telemetry/dispatch-declared.json (sha256 76632d73...)",
  "reports/round-43/claims.json",
  "reports/round-43/targets.json"
 ],
 "note": "Successor row per AGENTS.md; corrects the declaration's artifact digest without touching the original file."
}
```

### 5.2 `reports/round-43/telemetry/inputs/dispatch-result.raw.json` (redacted native extract)

This is the artifact that makes every count reproducible. One row per seat id from `targets.json` (32), redacting prompts, credentials, authorization headers, and private payloads; keep outcomes, error classes, and timing.

```json
{
 "schema": "kotodama-dispatch-result-extract-v1",
 "round": 43,
 "source_kind": "<FILL: native batch tool result | provider result file | operator transcript; be exact>",
 "tool": "<FILL: tool/route name>",
 "batch_id": "<FILL or null>",
 "owner": "integrator (goal-mode parent)",
 "captured_at_utc": "<FILL>",
 "wall_seconds": null,
 "seats": [
  {"seat_id": "K01", "started": null, "outcome": "<completed|failed>", "failure_phase": "<launch|run|null>", "error_class": null, "started_at_utc": null, "ended_at_utc": null},
  {"seat_id": "K02", "started": null, "outcome": "<completed|failed>", "failure_phase": "<launch|run|null>", "error_class": null, "started_at_utc": null, "ended_at_utc": null},
  {"seat_id": "P01", "started": null, "outcome": "<completed|failed>", "failure_phase": "<launch|run|null>", "error_class": null, "started_at_utc": null, "ended_at_utc": null}
 ],
 "route": {
  "provider_lane": "opencode-go",
  "requested_model": "deepseek-v4.1-flash",
  "observed_wire_model": "<FILL or null>",
  "basis": "<FILL: response header/field or null + reason>"
 },
 "redactions": ["credentials", "authorization headers", "prompts and private payloads"],
 "limits": [
  "A flat seat list does not measure runtime concurrency.",
  "Provider liveness is not round acceptance.",
  "Null timing fields mean unavailable, not zero."
 ]
}
```

`seats[]` must list all 32 ids. `started` is `true|false|null`: `null` means the native extract does not say whether the seat began, so `launched` must then be `could-not-recover`, not guessed. The fill command asserts set equality with `targets.json` and, when every `started` is known, `completed + failed == launched`.

### 5.3 `reports/round-43/telemetry/worker-observation-s02.json` (partial sample, optional)

```json
{
 "round": 43,
 "owner": "S02 (seat; telemetry scribe)",
 "observed_at_utc": "2026-10-19T16:55:37Z",
 "evidence_kind": "worker-self-observation",
 "source": "date -u +%Y-%m-%dT%H:%M:%SZ in the seat shell; this seat is executing reports/round-43/targets.json:43",
 "sessions": [{"assignment": "S02", "state_at_observation": "active"}],
 "seat_output_census": {
  "observed_at_utc": "2026-10-19T16:55:37Z",
  "counting_command": "python3 - <<'PY' (seat-output census; see the seat's out file §2 T5/T6)",
  "declared_seats": 32,
  "non_empty_out_files": 1,
  "present": ["K02"],
  "absent_count": 31,
  "note": "earlier sample at 2026-10-19T16:53:55Z returned 0 non-empty seat outputs"
 },
 "scope": "One worker self-observation plus one file-presence sample. Not a dispatch census; no evidence of launches, completions, failures, concurrency, wall time or actual route.",
 "unavailable_owner": "Round-43 integrator (native dispatch/result holder)",
 "unavailable_reason": "The worker-visible round-43 claims/targets declare a request; the native batch result was not supplied to this worker."
}
```

---

## 6. Fill checklist (integrator)

Run from the repo root. `TMPDIR`/`PYTHONDONTWRITEBYTECODE` per the round's shared rules. **Never run `reports/round-43/run-validation.py` in-tree**; use the round's sanctioned out-of-tree invocation and let its receipt land at `reports/round-43/validation.json`.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. Hard precondition. A rejected round still closes (r42 precedent).
test -f reports/round-43/validation.json && echo CLOSE-READY || echo BLOCKED

# 2. Durable input copies (r39-r42 convention; byte-identical).
mkdir -p reports/round-43/telemetry/inputs
cp reports/round-43/claims.json reports/round-43/telemetry/inputs/claims.json
cp reports/round-43/targets.json reports/round-43/telemetry/inputs/targets.json
sha256sum reports/round-43/telemetry/inputs/claims.json reports/round-43/telemetry/inputs/targets.json
# expected: 9662e2bd... / 44d1f7ce...

# 3. Land the redacted native extract at telemetry/inputs/dispatch-result.raw.json
#    (schema §5.2), then derive the counters:
python3 - <<'PY'
import json
d=json.load(open('reports/round-43/telemetry/inputs/dispatch-result.raw.json'))
s=d['seats']
assert len(s)==32, len(s)
unknown=[x['seat_id'] for x in s if x.get('started') is None]
launched=None if unknown else sum(1 for x in s if x['started'])
completed=sum(1 for x in s if x['outcome']=='completed')
failed=sum(1 for x in s if x['outcome']=='failed')
print('rows=%d launched=%s completed=%d failed=%d unstarted=%d'%(
    len(s), 'could-not-recover' if launched is None else launched, completed, failed,
    sum(1 for x in s if x.get('started') is False)))
if launched is not None:
    assert completed+failed==launched, (completed,failed,launched)
else:
    print('launched unknown for seats:', ','.join(unknown))
t=json.load(open('reports/round-43/targets.json'))
declared={x['id'] for x in t['seats']}; got={x['seat_id'] for x in s}
print('seat-id match:', got==declared, 'missing:', sorted(declared-got), 'extra:', sorted(got-declared))
PY

# 3b. Deliverable census (corroboration only; NOT dispatch evidence).
python3 - <<'PY'
import json,os
t=json.load(open('reports/round-43/targets.json'))
rows=[]
for x in t['seats']:
    p=os.path.join('reports/round-43',x['out'])
    rows.append((x['id'],os.path.isfile(p) and os.path.getsize(p)>0,os.path.getsize(p) if os.path.isfile(p) else 0))
print('declared=%d present_nonempty=%d absent=%d empty=%d'%(
    len(rows),sum(r[1] for r in rows),sum(1 for r in rows if r[2]==0),
    sum(1 for r in rows if not r[1] and r[2]>0)))
print('absent:',','.join(r[0] for r in rows if not r[1]))
PY

# 4. Close-time stamps and digests.
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum reports/round-43/telemetry/observed-dispatch.json \
          reports/round-43/telemetry/dispatch-declared.json \
          reports/round-43/validation.json

# 5. File in this order: amendment (§5.1) -> observed-dispatch (§3) -> close (§4).
#    Replace every <FILL ...>; leave null only where the record names an owner+reason.

# 6. Post-file invariant check (read-only).
python3 - <<'PY'
import json,hashlib
c=json.load(open('reports/round-43/telemetry/availability-close-43.json'))
o=open('reports/round-43/telemetry/observed-dispatch.json','rb').read()
assert c['closes']=='reports/round-43/telemetry/observed-dispatch.json'
assert c['closes_sha256']==hashlib.sha256(o).hexdigest(), 'closes_sha256 mismatch'
cf=c['closed_fields']
for k in ('observed_launches','observed_completions','observed_failures','observed_window_utc'):
    assert isinstance(cf[k],str) and '<FILL' not in cf[k], k
assert c['could_not_recover']==['runtime_concurrency']
r=c['validation_receipt']
assert r['path']=='reports/round-43/validation.json'
assert r['sha256']==hashlib.sha256(open(r['path'],'rb').read()).hexdigest(), 'receipt digest mismatch'
print('CLOSE-OK')
PY
```

Expected at observation: step 1 prints `BLOCKED`; step 2's digests match §1; step 3 cannot run until §5.2 lands; step 6 prints `CLOSE-OK` only after everything is filled.

If the native result is unavailable at close: leave the three counters `null`, set their owner/reason to `could-not-recover` (integrator), keep `launched=null` — do **not** substitute `requested_workers`. The round still closes; the gap is visible.

---

## 7. To-verify / open items (owner: integrator unless noted)

1. Cause of the `claims.json` digest mismatch (T1); the amendment record carries `to-verify` until resolved.
2. Which intermediate lane really ran between zai and opencode-go (T2: antigravity gemini-3.8-flash vs cursor/gemini-4-argon). No r43 availability-attempt record exists.
3. Observed wire model and whether "max" effort existed on the lane; requested model is the base alias only.
4. `runtime_concurrency`: null unless concurrent-session samples exist; a flat batch result cannot measure it.
5. Native evidence for the pre-completion interruptions; if none, record `could-not-recover` rows rather than reconstructing from memory.
6. Whether the integrator wants `worker-observation-s02.json` filed (§5.3); it is a partial sample, not a census.
7. Validation outcome (admission or rejection) and the final receipt digest; both belong to `validation_receipt`, not to the counters.

---

## 8. Negative proof

- Wrote only `reports/round-43/scribe/S02-telemetry-draft.md`; no file under `reports/round-43/telemetry/` was created or edited by this seat.
- No `corpus/**`, `tools/**`, `README.md`, or `reports/round-1..42/**` byte touched.
- No `run-validation.py` executed; no git commit/push; no install; no network.
- All measurements came from read-only commands: `ls`, `cat`, `find`, `wc`, `stat`, `date`, `sha256sum`, and `python3` readers over JSON/text. No scratch-only evidence is cited: every number above is reproducible from the named repo file or the command shown.
