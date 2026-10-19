# S02 — telemetry scribe: observed-dispatch + availability-close-44 skeletons

- Seat: **S02**, role scribe, claim cross (`reports/round-44/targets.json:43`).
- Round 44, loop 1, baseline `c9f4eaa` (`reports/round-44/claims.json:6-7`).
- Observed at `2026-10-19T17:21:33Z` (`date -u +%Y-%m-%dT%H:%M:%SZ`), plus a post-write sample recorded in §2 T6.
- Writes: **this file only** (`reports/round-44/scribe/S02-telemetry-draft.md`). Nothing under `reports/round-44/telemetry/` is created or edited by this seat; every JSON below is a draft for the integrator.
- Canon: NON-CANON. No corpus, tools, README, or filed-round byte touched; no runner executed; no commit/push/install/network.

Mission: draft the observed-dispatch and availability-close-44 skeletons (owner, window, counting commands, durable source paths + sha256 placeholders the integrator fills). Skeletons are §3–§4; the redacted native-extract schema with all 32 seat rows is §5.1; the fill procedure and post-fill invariant check are §6.

Binding text: `AGENTS.md:15-39` ("Availability and dispatch telemetry", "Close what you open"), `REGIMEN.md:48-49` (telemetry including the digest-pinned closing snapshot once `validation.json` lands).

---

## 1. Durable inputs read at observation

| Path | Bytes | SHA-256 (measured `2026-10-19T17:19:40Z`) |
|---|---:|---|
| `reports/round-44/claims.json` | 6987 | `5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8` |
| `reports/round-44/targets.json` | 12310 | `1f73f17245f6af43791ce86f632b17eaa6d5919ff855edc07738d9aff61a9501` |
| `reports/round-44/telemetry/dispatch-declared.json` | 1342 | `565e4fbd505c9e7ff652e9dff9e2bbdef07c1b9555932bf401fb5fdf68570844` |

Commands and raw output:

```console
$ sha256sum reports/round-44/claims.json reports/round-44/targets.json reports/round-44/telemetry/dispatch-declared.json
5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8  reports/round-44/claims.json
1f73f17245f6af43791ce86f632b17eaa6d5919ff855edc07738d9aff61a9501  reports/round-44/targets.json
565e4fbd505c9e7ff652e9dff9e2bbdef07c1b9555932bf401fb5fdf68570844  reports/round-44/telemetry/dispatch-declared.json
$ wc -c reports/round-44/claims.json reports/round-44/targets.json reports/round-44/telemetry/dispatch-declared.json
 6987 reports/round-44/claims.json
12310 reports/round-44/targets.json
 1342 reports/round-44/telemetry/dispatch-declared.json
```

Precedent read for schema: `reports/round-40..42/telemetry/{dispatch-declared,observed-dispatch,availability-close-*.json}`, `reports/round-43/telemetry/*`, `reports/supplement-opencode-1/dispatch.json` (native AgentSwarm receipt shape: `native_tool`, `tool_call_id`, `result_sha256`, per-assignment outcome), and `reports/round-39/calib/isolation-replay-protocol.md:1-25` (the no-in-tree-execution rule).

---

## 2. Provenance findings

### T1 — declaration digests match the live files (no amendment owed at observation)

`dispatch-declared.json:13-14` pins `claims.json` at `5bd54b71…` and `targets.json` at `1f73f172…`; both match the live bytes exactly (§1). This is the r43 stale-declared-digest defect **not** recurring: r43's declaration pinned `beda7644…/6353 B` while the executed contract was `9662e2bd…/6546 B` (`reports/round-43/telemetry/availability-close-43.json:18`). At close, re-run the digests; if they moved (an operator redirect edited `claims.json`), file a new `dispatch-declared-amendment-1.json` (§5.3) and never edit the filed declaration (`AGENTS.md:29-31`).

### T2 — declaration timestamp vs file write time (minor provenance note, not a defect)

```console
$ TZ=UTC stat -c '%y %s %n' reports/round-44/claims.json reports/round-44/targets.json reports/round-44/telemetry/dispatch-declared.json
2026-10-19 17:19:00.383051910 +0000 6987 reports/round-44/claims.json
2026-10-19 17:16:20.705662642 +0000 12310 reports/round-44/targets.json
2026-10-19 17:19:05.113063407 +0000 1342 reports/round-44/telemetry/dispatch-declared.json
```

`claims.json:6` and `dispatch-declared.json:5` both say `2026-10-19T17:15:17Z`, while the declaration file was written at `17:19:05Z` (3m48s later). Because the pinned digests match the live content, the declaration describes the final contract; the timestamp names the declared moment, not the write moment. No correction is owed. Recorded here so the close does not mistake the gap for drift.

### T3 — the pre-dispatch route deviation is declared, not sampled

`claims.json:5` names the scheduled position-12 model `antigravity gemini-3.8-flash`; `claims.json:13` and `dispatch-declared.json:10` record that it "aborted twice with zero seat output" and was operator-redirected to `opencode-go/deepseek-v4.1-flash`, with positions 12/13 and the argon rounds skipped in the schedule. Both statements are consistent (unlike r43's conflicting zai/antigravity/cursor history), but they are **operator declarations**, not availability samples.

```console
$ ls -la reports/round-44/telemetry/
total 4
drwxr-xr-x 1 vgpnk vgpnk   44 Oct 19 14:16 .
drwxr-xr-x 1 vgpnk vgpnk  142 Oct 19 14:16 ..
-rw-r--r-- 1 vgpnk vgpnk 1342 Oct 19 14:19 dispatch-declared.json
```

No `availability-attempt-*.json` exists (compare r35's three attempt records). The abort count and "zero seat output" therefore enter the record as declared-by-operator with `durability: to-verify`; they must not be upgraded to a measured launch/failure counter or reconstructed after the fact.

### T4 — close preconditions are not yet met; the runner must not execute in-tree

At `2026-10-19T17:21:33Z`:

```console
$ ls reports/round-44/run-validation.py reports/round-44/validation.json
ls: cannot access 'reports/round-44/run-validation.py': No such file or directory
ls: cannot access 'reports/round-44/validation.json': No such file or directory
```

The close snapshot is **blocked** until `validation.json` lands. A rejected round still closes (r42 and r43 both closed on rejection receipts: `reports/round-42/telemetry/availability-close-42.json:19`, `reports/round-43/telemetry/availability-close-43.json:12-13`). The round's shared rules and `reports/round-39/calib/isolation-replay-protocol.md:1-25` forbid running `reports/round-44/run-validation.py` in-tree; the receipt must be produced by the isolated git-archive replay and then filed, as r43's close records (`availability-close-43.json:15`). Acceptance is recorded from the receipt, never inferred from dispatch completions (`AGENTS.md:26`).

### T5 — seat contract census is clean (reproducible)

```console
$ python3 - <<'PY'
import json
from collections import Counter
d=json.load(open('reports/round-44/targets.json'))
s=d['seats']
print('seat_count',d['seat_count'],'seats',len(s),'unique_ids',len({x['id'] for x in s}),
      'unique_outs',len({x['out'] for x in s}))
print('roles',dict(Counter(x['role'] for x in s)))
print('claims',dict(Counter(x['claim'] for x in s)))
print('escapes',[x['out'] for x in s if x['out'].startswith('/') or '..' in x['out'].split('/')])
PY
seat_count 32 seats 32 unique_ids 32 unique_outs 32
roles {'scout': 4, 'planner': 1, 'connector': 1, 'executor': 7, 'verifier': 11, 'scribe': 4, 'reviewer': 2, 'critic': 2}
claims {'O': 11, 'C': 8, 'Ca': 4, 'cross': 9}
escapes []
```

This is the reproducible count behind `requested_workers: 32`; it is **not** a launch/completion count.

### T6 — partial availability samples (one worker + file presence, not a census)

```text
sample 1  2026-10-19T17:21:33Z  seat-output census over targets.json
          declared=32  present_nonempty=2  absent=30  extra_md_not_declared=[]
          present=["O02","O03"]   (mtimes 17:21:28Z and 17:21:25Z)
          S02 self-observation: this seat active, writing this file
```

Label `partial-worker-observation`. It proves at least two concurrent seats landed deliverables while this seat ran; it is **not** evidence of 32 launches, completions, failures, concurrency, wall time, or route. File presence is corroboration only: r43 recorded 29 `.md` fragments against 16 completed seats (`reports/round-43/telemetry/observed-dispatch.json:10-15`), so a fragment can exist without a completed dispatch.

A second sample taken immediately after this file was written is recorded in the same block at the end of this section (sample 2), so the draft itself is counted reproducibly.

```text
sample 2  2026-10-19T17:23:49Z  same census, after this file was written
          declared=32  present_nonempty=14  absent=18  extra_md_not_declared=[]
          present=["K01","X00","O02","O03","O06","O07","O08","O09","O10","K04","X02","S01","S02","A01"]
```

The delta between the samples (2 → 14 over `17:21:33Z` → `17:23:49Z`) is reproducible evidence that the wave was actively landing deliverables while this seat ran. It remains a file-presence sample only: not a launch/completion/failure count, and per the r43 precedent fragments can exceed completed dispatches.

### T7 — r43's closing snapshot did not digest-pin the record it closed (do not repeat)

`reports/round-43/telemetry/availability-close-43.json:5-6` names `dispatch-declared.json` as `closes_record` but sets `closes_record_sha256_at_close` to the string `"see declared_artifacts below"`, and `declared_artifacts` (`:17-22`) lists `claims.json`, `targets.json`, and two calib artifacts — **not** the dispatch-declared record. `AGENTS.md:38-39` requires the snapshot to name the record it closes **and that record's SHA-256 at close time**. The r44 skeleton fixes this by pinning `closes_sha256` for the observed record and an explicit `also_closes` row for the declaration. Filed r43 bytes are not edited; this is a successor-record correction.

### T8 — provider liveness and key census stay out of acceptance

r43's close recorded `"opencode-go key-1 served 32 launches, 16 completions; not round acceptance"` and the standing key amendment `"keys 1-2 live, 3-7 402 (standing amendment; no re-census this round)"` (`reports/round-43/telemetry/availability-close-43.json:27-28`). Round 44 reuses the same lane; at observation this seat has no native key attribution or re-census. The skeleton keeps `lane_key` and `provider_liveness` `null` with owner + reason, per `AGENTS.md:25-26`. Provider liveness is not round acceptance.

### T9 — schema choices in this draft (all additive, all r40–r43 compatible)

1. **Close both open records.** The observed record carries `state: open-at-seat-close`; the close pins it as `closes` and pins the declaration in `also_closes`, each with its own digest (fixes T7).
2. **Requested vs observed separated.** `requested_allocation` is copied from the contract; `actual_route.observed` is filled only from a native extract and never from the request (`AGENTS.md:22-25`).
3. **Counters stay `null` with owner + reason until measured.** `requested_workers: 32` must never be promoted to launched/completed; `completed + failed == launched` is asserted only when every `started` value is known.
4. **Receipt recorded, not assumed.** `validation_receipt` carries path, sha256, verdict, acceptance, `runner_sha256`, and the out-of-tree production note. A later re-run is a new row, never an in-place edit (`AGENTS.md:29-34`).
5. **No prompt payloads.** The native extract keeps seat ids, out paths, outcomes, error classes and timings only; credentials, authorization headers and prompts are redacted (`AGENTS.md:31`).

---

## 3. Skeleton A — `reports/round-44/telemetry/observed-dispatch.json`

Fence for the integrator. Fill every `<FILL …>` before filing. `null` counters are deliberate: unknown is not zero. The two measured digests and the declared timestamps are pre-filled from §1.

```json
{
 "record": "observed-dispatch",
 "kind": "observed-dispatch",
 "schema": "kotodama-observed-dispatch-v1",
 "round": 44,
 "state": "open-at-seat-close",
 "owner": "integrator (goal-mode parent)",
 "reason": "counters filled from reports/round-44/telemetry/inputs/dispatch-result.raw.json; closes when reports/round-44/telemetry/availability-close-44.json lands",
 "declared_at_utc": "2026-10-19T17:15:17Z",
 "declared_at_source": "reports/round-44/claims.json:6",
 "scheduled_position": 12,
 "schedule_note": "positions 12 (this round) and 13/argon skipped in the schedule (reports/round-44/claims.json:5,13)",
 "observation_closed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ at filing>",
 "observed_window_utc": "<FILL: min(started_at_utc)/max(ended_at_utc) from inputs/dispatch-result.raw.json; if any endpoint is unknown, could-not-recover + owner>",
 "window_basis": "<FILL: native AgentSwarm result wall_seconds = N s; else 'could-not-recover' + owner integrator>",
 "requested_allocation": {
  "provider_lane": "opencode-go",
  "model": "deepseek-v4.1-flash",
  "model_effort": null,
  "model_effort_note": "no effort variant declared or registered; claims.json:9-10 names only the base alias; scheduled antigravity/gemini-3.8-flash was operator-replaced (claims.json:5,13)",
  "requested_workers": 32,
  "batched_calls": 1,
  "baseline_commit": "c9f4eaa",
  "source": "reports/round-44/claims.json:5,7,9-12"
 },
 "route_history": [
  {
   "attempt": "pre-1",
   "lane": "antigravity",
   "model": "gemini-3.8-flash",
   "status": "aborted twice with zero seat output (operator-declared)",
   "source": "reports/round-44/claims.json:5,13; reports/round-44/telemetry/dispatch-declared.json:10",
   "durability": "to-verify: no reports/round-44/telemetry/availability-attempt-*.json filed at observation; the abort count and zero-output claim are not independently sampled here and must not be reconstructed"
  },
  {
   "attempt": "1",
   "lane": "opencode-go",
   "model": "deepseek-v4.1-flash",
   "status": "the batch this record observes",
   "source": "reports/round-44/telemetry/dispatch-declared.json:6-9,11"
  }
 ],
 "launched_workers": null,
 "launched_workers_owner": "integrator",
 "launched_workers_reason": "fill as count(seats[].started == true) from inputs/dispatch-result.raw.json; if any started value is null, record could-not-recover + owner. Never copy requested_workers",
 "completed_workers": null,
 "completed_workers_owner": "integrator",
 "completed_workers_reason": "fill as count(seats[].outcome == 'completed'); write 0 only after the derivation command returns 0",
 "failed_workers": null,
 "failed_workers_owner": "integrator",
 "failed_workers_reason": "fill as count(seats[].outcome == 'failed'); write 0 only after the derivation command returns 0",
 "failed_workers_note": "<FILL: seat ids + error classes; empty only if measured 0>",
 "counter_invariant": "completed + failed == launched, asserted by §6 step 3 when every started value is known; otherwise launched stays null",
 "runtime_concurrency": null,
 "runtime_concurrency_owner": "integrator",
 "runtime_concurrency_reason": "not derivable from a flat batch result; no concurrent-session samples supplied (r39-r43 precedent: could-not-recover)",
 "actual_route": {
  "requested": "opencode-go / deepseek-v4.1-flash",
  "observed": null,
  "observed_owner": "integrator",
  "observed_reason": "fill from the native extract's wire model/provider echo; do not copy the requested route",
  "basis": "<FILL: inputs/dispatch-result.raw.json#/route.observed_wire_model, or 'could-not-recover' + owner/reason>"
 },
 "lane_key": null,
 "lane_key_owner": "integrator",
 "lane_key_reason": "no native key attribution in the batch result at observation; r43 standing amendment: keys 1-2 live, 3-7 402, no re-census this round (reports/round-43/telemetry/availability-close-43.json:28)",
 "provider_liveness": {
  "status": null,
  "owner": "integrator",
  "reason": "provider liveness is not round acceptance (AGENTS.md:26); fill only from a native health/key sample taken this round, else null"
 },
 "deliverable_census": {
  "label": "corroboration-only; file presence is not dispatch outcome (r43: 29 fragments vs 16 completed)",
  "counting_command": "python3 - <<'PY' (seat-output census; §6 step 3b)",
  "counting_date": "<FILL: date -u +%F>",
  "counted_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ>",
  "declared_seats": 32,
  "fragments_present_nonempty": "<FILL>",
  "absent_seats": "<FILL: list; empty list only if measured>",
  "extra_md_not_declared": "<FILL: list of out-name variants or unexpected .md files; [] only if measured>"
 },
 "partial_observations": [
  {
   "kind": "worker-self-observation + seat-output presence",
   "observed_at_utc": "2026-10-19T17:21:33Z",
   "observed_active_sessions": 1,
   "declared_seats": 32,
   "non_empty_seat_outputs": 2,
   "present": ["O02", "O03"],
   "scope": "one worker + one file-presence sample; not a dispatch census",
   "filing": "candidate path reports/round-44/telemetry/worker-observation-s02.json (§5.2); drop this row if that file is not filed"
  }
 ],
 "durable_sources": [
  {
   "path": "reports/round-44/claims.json",
   "sha256": "5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8",
   "bytes": 6987,
   "observed_at_utc": "2026-10-19T17:19:40Z",
   "note": "matches dispatch-declared.json:13; re-verify at close, append an amendment on drift"
  },
  {
   "path": "reports/round-44/targets.json",
   "sha256": "1f73f17245f6af43791ce86f632b17eaa6d5919ff855edc07738d9aff61a9501",
   "bytes": 12310,
   "observed_at_utc": "2026-10-19T17:19:40Z",
   "note": "seat_count 32; 32 unique ids and outs (T5)"
  },
  {
   "path": "reports/round-44/telemetry/dispatch-declared.json",
   "sha256": "565e4fbd505c9e7ff652e9dff9e2bbdef07c1b9555932bf401fb5fdf68570844",
   "bytes": 1342,
   "observed_at_utc": "2026-10-19T17:19:40Z"
  },
  {
   "path": "reports/round-44/telemetry/inputs/dispatch-result.raw.json",
   "sha256": "<FILL at close: sha256sum reports/round-44/telemetry/inputs/dispatch-result.raw.json>",
   "bytes": "<FILL>",
   "note": "redacted native extract; reproduces every counter above (§5.1)"
  }
 ],
 "closing_snapshot": "open-at-seat-close: owed once reports/round-44/validation.json lands (admission or rejection; r42/r43 rejection precedent)"
}
```

Filing rule: if no native dispatch result is retained, leave the three counters `null`, set each owner/reason to `could-not-recover` with the integrator named, and say so in `window_basis`. Do **not** infer 32/32 from `requested_workers`, and do **not** count deliverable files as completions.

---

## 4. Skeleton B — `reports/round-44/telemetry/availability-close-44.json`

Do not file until `reports/round-44/validation.json` exists. Every digest is filled at close time, after the two source records are final. This file is new and append-only; it never edits `dispatch-declared.json` or `observed-dispatch.json` (`AGENTS.md:32-34`).

```json
{
 "schema": "kotodama-availability-closing-snapshot-v1",
 "kind": "availability-close",
 "round": 44,
 "date": "<FILL: date -u +%F>",
 "filed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ>",
 "owner": "integrator (goal-mode parent), for the lane",
 "closes": "reports/round-44/telemetry/observed-dispatch.json",
 "closes_sha256": "<FILL at close: sha256sum reports/round-44/telemetry/observed-dispatch.json>",
 "also_closes": [
  {
   "path": "reports/round-44/telemetry/dispatch-declared.json",
   "sha256": "<FILL at close; expected 565e4fbd505c9e7ff652e9dff9e2bbdef07c1b9555932bf401fb5fdf68570844 unless a filed byte was edited (forbidden)>",
   "note": "pinned explicitly because r43's close deferred this digest to declared_artifacts, which omitted the record (reports/round-43/telemetry/availability-close-43.json:6,17-22; AGENTS.md:38-39)"
  }
 ],
 "closed_fields": {
  "observed_launches": "<FILL: N (source: inputs/dispatch-result.raw.json; or 'could-not-recover' with owner integrator)>",
  "observed_completions": "<FILL: N (same source; or could-not-recover with owner)>",
  "observed_failures": "<FILL: N (classes: ...; same source; or could-not-recover with owner)>",
  "observed_window_utc": "<FILL: start/end from inputs/dispatch-result.raw.json; basis: native wall_seconds, else could-not-recover + owner>",
  "actual_route": {
   "requested": "opencode-go / deepseek-v4.1-flash",
   "observed": "<FILL: wire model from the native extract's provider echo, or 'could-not-recover'>",
   "basis": "<FILL: path#/field, or owner + reason>"
  },
  "runtime_concurrency": "could-not-recover as a measured counter: null with owner integrator (flat batch result; no concurrent-session samples)",
  "provider_liveness": "not round acceptance; <FILL: native sample path or 'could-not-evaluate' + owner>"
 },
 "could_not_recover": ["runtime_concurrency", "<FILL: add any counter left null; keep the list empty only if every counter is measured>"],
 "declared_artifacts": {
  "reports/round-44/claims.json": {
   "declared_sha256": "5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8",
   "sha256": "<FILL at close: sha256sum reports/round-44/claims.json>",
   "note": "if it differs from declared_sha256, the live digest is re-pinned here and a new dispatch-declared-amendment-1.json (§5.3) is filed; the declaration is never edited"
  },
  "reports/round-44/targets.json": {
   "declared_sha256": "1f73f17245f6af43791ce86f632b17eaa6d5919ff855edc07738d9aff61a9501",
   "sha256": "<FILL at close: sha256sum reports/round-44/targets.json>",
   "seat_count": 32
  },
  "reports/round-44/telemetry/observed-dispatch.json": {
   "sha256": "<FILL: must equal closes_sha256 above>"
  },
  "<FILL if filed: reports/round-44/calib/<O census artifact>.json>": {
   "sha256": "<FILL: the single census artifact the O claim files; optional row, omit rather than guess a path>"
  }
 },
 "validation_receipt": {
  "path": "reports/round-44/validation.json",
  "sha256": "<FILL at close: sha256sum reports/round-44/validation.json>",
  "verdict": "<FILL: admitted | rejected | rejected-honest-stop | could-not-evaluate>",
  "acceptance_checks_passed": "<FILL: true | false>",
  "runner_sha256": "<FILL at close: sha256sum reports/round-44/run-validation.py>",
  "produced_by": "isolated git-archive replay (Tier B; TMPDIR in-sandbox, --out publish inside sandbox), then filed — reports/round-39/calib/isolation-replay-protocol.md; no in-tree runner execution",
  "caveat": "if the runner is re-run after close, file a new snapshot row; never edit this file (AGENTS.md:29-34)"
 },
 "open_at_close": "<FILL: null only when every field is filled, or could-not-recover with owner + reason>",
 "reason": "closing snapshot filed once reports/round-44/validation.json landed (admission or rejection); every open field filled citing its durable artifact",
 "sources": [
  "reports/round-44/telemetry/dispatch-declared.json (sha256 re-verified at close)",
  "reports/round-44/telemetry/observed-dispatch.json (sha256 pinned above)",
  "reports/round-44/telemetry/inputs/dispatch-result.raw.json",
  "reports/round-44/validation.json",
  "reports/round-39/calib/isolation-replay-protocol.md (production method)"
 ]
}
```

Admission rule: a round is not admitted to `LOG.md` while its own availability record still owes a closing snapshot (`AGENTS.md:37-39`). Filing this close is a precondition of the r44 LOG entry, independent of the round's acceptance verdict.

---

## 5. Supporting records

### 5.1 `reports/round-44/telemetry/inputs/dispatch-result.raw.json` (redacted native extract)

This is the artifact that makes every count reproducible (`AGENTS.md:17-20`). One row per seat id from `targets.json` (all 32, in contract order); outcomes and timings only — no prompts, credentials, authorization headers, or private payloads. Shape follows `reports/supplement-opencode-1/dispatch.json:1-11` (native AgentSwarm receipt fields).

```json
{
 "schema": "kotodama-dispatch-result-extract-v1",
 "round": 44,
 "source_kind": "<FILL: native AgentSwarm result | provider result file | operator transcript; be exact>",
 "native_tool": "AgentSwarm",
 "tool_call_id": "<FILL or null>",
 "native_result_sha256": "<FILL: sha256 of the redacted native extract if one exists, else null + reason>",
 "owner": "integrator (goal-mode parent)",
 "captured_at_utc": "<FILL>",
 "wall_seconds": null,
 "requested_allocation": {
  "provider_lane": "opencode-go",
  "model": "deepseek-v4.1-flash",
  "requested_workers": 32,
  "batched_calls": 1
 },
 "seats": [
   {"seat_id": "K01",   "out": "scout/K01-resolver-scout.md",           "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "K02",   "out": "scout/K02-gap-scout.md",                "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "K03",   "out": "scout/K03-freshness-scout.md",          "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "P01",   "out": "plan/P01-plan.md",                      "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "X00",   "out": "cross/X00-connector.md",                "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O01",   "out": "op/O01-landing-spec.md",                "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O02",   "out": "op/O02-verify.md",                      "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O03",   "out": "op/O03-defects-verify.md",              "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O04",   "out": "op/O04-witness-demotion.md",            "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O05",   "out": "op/O05-traps.md",                       "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O06",   "out": "op/O06-census-artifact.md",             "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O07",   "out": "op/O07-parity.md",                      "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O08",   "out": "op/O08-negative-proof.md",              "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O09",   "out": "op/O09-scribe.md",                      "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "O10",   "out": "op/O10-census-verify.md",               "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "K04",   "out": "scout/K04-gap-verify.md",               "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "C01",   "out": "cov/C01-entry-draft.md",                "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "C02",   "out": "cov/C02-readme-draft.md",               "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "C03",   "out": "cov/C03-audit.md",                      "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "C04",   "out": "cov/C04-contract-audit.md",             "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "C05",   "out": "cov/C05-collision.md",                  "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "C06",   "out": "cov/C06-scribe.md",                     "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "Ca01",  "out": "calib/Ca01-freshness-gate.md",          "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "Ca02",  "out": "calib/Ca02-verify.md",                  "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "Ca03",  "out": "calib/Ca03-process-record.md",          "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "R01",   "out": "review/R01-review.md",                  "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "R02",   "out": "review/R02-review.md",                  "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "X01",   "out": "cross/X01-trades.md",                   "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "X02",   "out": "cross/X02-honesty.md",                  "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "S01",   "out": "scribe/S01-integration-draft.md",       "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "S02",   "out": "scribe/S02-telemetry-draft.md",         "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null},
   {"seat_id": "A01",   "out": "adj/A01-scope.md",                      "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null}
 ],
 "route": {
  "provider_lane": "opencode-go",
  "requested_model": "deepseek-v4.1-flash",
  "observed_wire_model": "<FILL or null>",
  "basis": "<FILL: provider response field/header, or null + reason>"
 },
 "redactions": ["credentials", "authorization headers", "prompts and private payloads"],
 "limits": [
  "A flat seat list does not measure runtime concurrency.",
  "Provider liveness is not round acceptance.",
  "Null timing fields mean unavailable, not zero.",
  "File presence is not dispatch outcome (r43: 29 fragments vs 16 completed)."
 ]
}
```

`started` is `true | false | null`; `outcome` is `completed | failed | null`. `null` means the native extract does not say, so the corresponding counter must be `could-not-recover`, not zero. The fill command in §6 step 3 asserts seat-id set equality with `targets.json` and, when every `started` is known, `completed + failed == launched`.

### 5.2 `reports/round-44/telemetry/worker-observation-s02.json` (partial sample, optional)

File before citing the path in §3's `partial_observations`; otherwise drop that row.

```json
{
 "record": "worker-observation",
 "round": 44,
 "owner": "S02 (seat; telemetry scribe)",
 "observed_at_utc": "2026-10-19T17:21:33Z",
 "evidence_kind": "worker-self-observation + seat-output presence",
 "source": "date -u in the seat shell; this seat executes reports/round-44/targets.json:43",
 "sessions": [{"assignment": "S02", "state_at_observation": "active"}],
 "seat_output_census": {
  "counting_command": "python3 - <<'PY' (seat-output census; S02 draft §2 T6)",
  "counting_date": "2026-10-19",
  "declared_seats": 32,
  "non_empty_out_files": 2,
  "present": ["O02", "O03"],
  "absent_count": 30,
  "extra_md_not_declared": []
 },
 "scope": "One worker self-observation plus one file-presence sample. Not a dispatch census; no evidence of launches, completions, failures, concurrency, wall time or actual route.",
 "unavailable_owner": "round-44 integrator (native dispatch/result holder)",
 "unavailable_reason": "the native batch result was not supplied to this worker at observation"
}
```

### 5.3 `reports/round-44/telemetry/dispatch-declared-amendment-1.json` (conditional, only on digest drift)

File only if `claims.json` or `targets.json` no longer matches `dispatch-declared.json:13-14` at close. At observation no drift exists (T1), so this file is **not** owed now.

```json
{
 "record": "dispatch-declared-amendment-1",
 "round": 44,
 "owner": "integrator (goal-mode parent)",
 "filed_at_utc": "<FILL>",
 "amends": "reports/round-44/telemetry/dispatch-declared.json",
 "amends_sha256": "<FILL at filing; expected 565e4fbd… unless edited (forbidden)>",
 "class": "stale-declared-artifact-digest",
 "artifact_rows": [
  {
   "path": "reports/round-44/claims.json",
   "declared": {"sha256": "5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8"},
   "observed": {"sha256": "<FILL>", "bytes": "<FILL>"},
   "match": "<FILL: true|false>",
   "status": "<FILL: verified | to-verify>",
   "disposition": "availability-close-44.json re-pins the live digest; dispatch-declared.json is never edited"
  }
 ],
 "reason": "<FILL: exact cause, or 'to-verify' + owner; do not reconstruct>",
 "sources": ["reports/round-44/telemetry/dispatch-declared.json", "reports/round-44/claims.json", "reports/round-44/targets.json"]
}
```

---

## 6. Fill checklist (integrator)

Run from the repo root. `TMPDIR`/`PYTHONDONTWRITEBYTECODE` per the round's shared rules. **Never run `reports/round-44/run-validation.py` in-tree**; produce the receipt with the isolated replay protocol and let it land at `reports/round-44/validation.json`.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. Hard precondition. A rejected round still closes (r42/r43 precedent).
test -f reports/round-44/validation.json && echo CLOSE-READY || echo BLOCKED

# 2. Durable input copies (r39-r42 convention; byte-identical at capture time).
mkdir -p reports/round-44/telemetry/inputs
cp reports/round-44/claims.json reports/round-44/telemetry/inputs/claims.json
cp reports/round-44/targets.json reports/round-44/telemetry/inputs/targets.json
sha256sum reports/round-44/telemetry/inputs/claims.json reports/round-44/telemetry/inputs/targets.json
# expected at observation: 5bd54b71... / 1f73f172...; if claims moved, capture the final bytes and file §5.3

# 3. Land the redacted native extract at telemetry/inputs/dispatch-result.raw.json
#    (§5.1), then derive the counters:
python3 - <<'PY'
import json
raw = 'reports/round-44/telemetry/inputs/dispatch-result.raw.json'
d = json.load(open(raw))
seats = d['seats']
t = json.load(open('reports/round-44/targets.json'))
declared = {x['id'] for x in t['seats']}
got = {x['seat_id'] for x in seats}
print('rows=%d ids_match=%s missing=%s extra=%s' % (
    len(seats), got == declared, sorted(declared - got), sorted(got - declared)))
assert len(seats) == 32 and got == declared
unresolved = [x['seat_id'] for x in seats if x['outcome'] is None]
unknown = [x['seat_id'] for x in seats if x.get('started') is None]
launched = None if unknown else sum(1 for x in seats if x['started'] is True)
completed = sum(1 for x in seats if x['outcome'] == 'completed')
failed = sum(1 for x in seats if x['outcome'] == 'failed')
print('launched=%s completed=%d failed=%d unresolved=%s started_unknown=%d' % (
    'could-not-recover' if launched is None else launched,
    completed, failed, ','.join(unresolved) or '-', len(unknown)))
if launched is not None and not unresolved:
    assert completed + failed == launched, (completed, failed, launched)
PY

# 3b. Deliverable census (corroboration only; NOT dispatch evidence, NOT completions).
python3 - <<'PY'
import json, os
t = json.load(open('reports/round-44/targets.json'))
rows = []
for x in t['seats']:
    p = os.path.join('reports/round-44', x['out'])
    rows.append((x['id'], os.path.isfile(p) and os.path.getsize(p) > 0,
                 os.path.getsize(p) if os.path.isfile(p) else 0))
declared = {x['out'] for x in t['seats']}
extras = []
for root, dirs, files in os.walk('reports/round-44'):
    if 'telemetry' in root.split(os.sep):
        continue
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), 'reports/round-44')
        if f.endswith('.md') and rel not in declared:
            extras.append(rel)
print('declared=%d present_nonempty=%d absent=%d empty=%d extras=%s' % (
    len(rows), sum(r[1] for r in rows), sum(1 for r in rows if r[2] == 0),
    sum(1 for r in rows if not r[1] and r[2] > 0), extras or '[]'))
print('absent:', ','.join(r[0] for r in rows if not r[1]) or '-')
PY

# 4. Close-time stamps and digests.
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum reports/round-44/telemetry/observed-dispatch.json \
          reports/round-44/telemetry/dispatch-declared.json \
          reports/round-44/telemetry/inputs/dispatch-result.raw.json \
          reports/round-44/validation.json \
          reports/round-44/run-validation.py

# 5. File in this order: (amendment §5.3 only on drift) -> observed-dispatch (§3)
#    -> availability-close-44 (§4). Replace every <FILL …>; leave null only where
#    the record names an owner + reason.

# 6. Post-file invariant check (read-only).
python3 - <<'PY'
import json, hashlib

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

c = json.load(open('reports/round-44/telemetry/availability-close-44.json'))
o = json.load(open('reports/round-44/telemetry/observed-dispatch.json'))
assert c['closes'] == 'reports/round-44/telemetry/observed-dispatch.json'
assert c['closes_sha256'] == sha(c['closes']), 'closes digest mismatch'
for r in c['also_closes']:
    assert r['sha256'] == sha(r['path']), 'also_closes digest mismatch: ' + r['path']
for p, row in c['declared_artifacts'].items():
    if p.startswith('<FILL'):
        continue
    assert row['sha256'] == sha(p), 'declared artifact digest mismatch: ' + p
for k, v in c['closed_fields'].items():
    assert '<FILL' not in json.dumps(v), 'unfilled closed field: ' + k
rec = c['validation_receipt']
assert rec['sha256'] == sha(rec['path']), 'validation receipt digest mismatch'
assert rec['runner_sha256'] == sha('reports/round-44/run-validation.py'), 'runner digest mismatch'
assert '<FILL' not in json.dumps(o['durable_sources']), 'unfilled durable source'
for k in ('launched_workers', 'completed_workers', 'failed_workers', 'runtime_concurrency'):
    assert o[k] is None or isinstance(o[k], int), k
assert o['requested_allocation']['requested_workers'] == 32
print('CLOSE-OK')
PY
```

Expected at observation: step 1 prints `BLOCKED`; step 2's digests match §1; step 3 cannot run until §5.1 lands; step 6 prints `CLOSE-OK` only after everything is filled.

If the native result is unavailable at close: leave the three counters `null`, set their owner/reason to `could-not-recover` (integrator), keep `launched = null` — do **not** substitute `requested_workers`, and do **not** report file-presence counts as completions. The round still closes; the gap stays visible.

---

## 7. To-verify / open items (owner: integrator unless noted)

1. Native dispatch evidence: `tool_call_id`, result digest, per-seat outcomes, wall seconds. Without it, all three counters and the window are `could-not-recover`, not inferred from 32 requested.
2. Observed wire model / actual route (§3 `actual_route.observed`); do not copy the requested alias.
3. opencode-go key attribution and key census for r44; r43's standing amendment is keys 1-2 live, 3-7 402, no re-census (`reports/round-43/telemetry/availability-close-43.json:28`).
4. The antigravity pre-dispatch abort ("twice, zero seat output"): operator-declared only; no `availability-attempt-*.json` exists. File one if a sample exists, else leave `to-verify` and do not reconstruct.
5. `runtime_concurrency`: null unless concurrent-session samples exist; a flat batch result cannot measure it.
6. Digest drift at close: re-verify `claims.json`/`targets.json`; if an operator redirect edited them, re-pin in the close and file §5.3 — never edit `dispatch-declared.json`.
7. Whether the integrator files `worker-observation-s02.json` (§5.2); if not, drop the corresponding `partial_observations` row.
8. Validation outcome and receipt digest belong in `validation_receipt`, never in the counters. The receipt must be produced out-of-tree per `reports/round-39/calib/isolation-replay-protocol.md`.

---

## 8. Negative proof

- Wrote only `reports/round-44/scribe/S02-telemetry-draft.md`; no file under `reports/round-44/telemetry/` was created or edited by this seat.
- No `corpus/**`, `tools/**`, `README.md`, `reports/round-1..43/**`, or other seat's out path was touched.
- No `run-validation.py` executed; no git commit/push; no install; no network.
- All numbers above came from read-only commands: `ls`, `wc`, `stat`, `sha256sum`, `find`, `date`, and `python3` readers over JSON/text. Scratch artifacts under `.scratch/` (other seats' `o44`/`r44-o10`/`x44` directories exist) are not cited as evidence; every cited number is reproducible from the named repo file or the command shown.
