# S02 — telemetry scribe: observed-dispatch + availability-close-48 skeletons

- Seat: **S02**, role scribe, claim cross (`reports/round-48/targets.json:3` plans 64 seats; this out path is the S02 row).
- Round 48, loop 2, position 2, baseline `a01405d` (`reports/round-48/claims.json:7`).
- Dispatch under observation: `opencode-go` / `deepseek-v4.1-flash`, key-2 (round-robin), 64 requested workers, 1 batched call (`reports/round-48/telemetry/dispatch-declared.json:6-10`).
- Seat sampling window: opened `2026-10-19T19:38:23Z`; last sample `2026-10-19T19:39:39Z` (`date -u +%Y-%m-%dT%H:%M:%SZ`). Local zone `-03`.
- Writes: **this file only** (`reports/round-48/scribe/S02-telemetry-draft.md`). Nothing under `reports/round-48/telemetry/` is created or edited by this seat; the skeletons below are for the integrator.
- Canon: NON-CANON. No corpus, tools, README, or filed-round byte touched; no runner executed; no commit/push/install/network.

Mission: draft the observed-dispatch and availability-close-48 skeletons — owner, closed sampling window, counting commands and date, durable source paths, SHA-256 pins — so the integrator can file them after the batch without reconstructing a single number. Skeletons are §3–§7; provenance is §2; the fill procedure is §8.

---

## 1. Durable inputs measured at draft time

| Path | Bytes | SHA-256 (measured `2026-10-19T19:39:39Z`) | mtime UTC |
|---|---:|---|---|
| `reports/round-48/claims.json` | 5545 | `bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292` | `2026-10-19 19:36:19.844155825` |
| `reports/round-48/targets.json` | 18585 | `d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446` | `2026-10-19 19:37:21.331292519` |
| `reports/round-48/telemetry/dispatch-declared.json` | 1239 | `40a96ab6227ca229d615a8bdcca1d32124447a5433bfbe53f7e26c9e33d2ab4e` | `2026-10-19 19:37:31.180314421` |
| `tools/harness/claims-freshness.py` | — | `466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d` | unchanged since r47 close |

```console
$ sha256sum reports/round-48/telemetry/dispatch-declared.json reports/round-48/claims.json reports/round-48/targets.json tools/harness/claims-freshness.py
40a96ab6227ca229d615a8bdcca1d32124447a5433bfbe53f7e26c9e33d2ab4e  reports/round-48/telemetry/dispatch-declared.json
bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292  reports/round-48/claims.json
d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446  reports/round-48/targets.json
466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d  tools/harness/claims-freshness.py
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain corpus/ tools/
(empty)
```

Precedent read for shape: `reports/round-43/telemetry/`, `reports/round-44/telemetry/`, `reports/round-46/telemetry/`, `reports/round-47/telemetry/`, and the binding rules at `AGENTS.md:15-39`.

---

## 2. Provenance findings

### T1 — the declaration's artifact pins reproduce exactly

`dispatch-declared.json:14-16` pins `claims.json` at `bf8df21b…` and `targets.json` at `d029eaa1…` with `seat_count: 64`. Both live digests match byte-for-byte (§1). No dispatch-declared amendment is owed for a pin mismatch. The r43 digest-drift defect does not recur.

### T2 — both declared timestamps are in the future of the system clock

`claims.json:6` and `dispatch-declared.json:5` both read `"2026-10-19T19:45:00Z"`. Measured against the system clock at sampling:

```console
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-19T19:38:49Z
$ python3 -c "... fromisoformat(d) - now ..."
claims.declared_at_utc 2026-10-19T19:45:00Z  delta_vs_now_sec=370.2   (positive = in the future)
dispatch.recorded_at_utc 2026-10-19T19:45:00Z  delta_vs_now_sec=370.2
```

The artifact mtimes (`19:36:19Z`, `19:37:21Z`, `19:37:31Z`) are all **before** the declared time by 7.5–8.7 minutes. Either the declaration timestamp is a round-clock intent time or a transcription error; no artifact in the round proves `19:45:00Z` was an observed instant. Recorded here as a provenance caveat, not repaired (this seat writes one file). The close should not copy this value into any observed field. Owner: integrator; status `to-verify`.

### T3 — the close is blocked at draft time

```console
$ ls reports/round-48/
claims.json  targets.json  telemetry
$ ls reports/round-48/validation.json
ls: cannot access 'reports/round-48/validation.json': No such file or directory
$ ls reports/round-48/telemetry/
dispatch-declared.json
```

Neither `run-validation.py` nor `validation.json` exists at the sampling window. `observed-dispatch.json` may be filed once the batch result is read; `availability-close-48.json` is **blocked** until the validation receipt lands, and the round is not admissible to `LOG.md` while the close is owed (`AGENTS.md:32-38`). A rejected round still closes — r44 filed a close with `verdict: rejected-honest-stop` (`reports/round-44/telemetry/availability-close-44.json:11`).

### T4 — the declared seat plan is internally clean

```console
$ python3 -B - <<'PY'  # census over targets.json
seat_count 64 | seats 64 | unique_ids 64 | unique_outs 64 | missing_out 0
roles {'verifier': 32, 'executor': 13, 'critic': 5, 'reviewer': 5, 'scribe': 4, 'scout': 3, 'connector': 1, 'planner': 1}
claims {'C': 30, 'Ca': 12, 'cross': 22}
top_dirs {'cov': 26, 'cross': 10, 'calib': 9, 'review': 5, 'adj': 4, 'op': 4, 'scribe': 3, 'scout': 2, 'plan': 1}
```

All 64 out paths are `.md`, unique, and relative. This is the reproducible basis of `requested_workers: 64` — **it is an allocation, not a launch, completion, or failure count**. The round carries 2 claims (`claims.json:25-53`, ids `C` and `Ca`); claim count is not seat count.

### T5 — partial worker observation only

Read-only samples, each with its own timestamp and the same counting command:

| Sampled at (UTC) | `.md` fragments | all files under `reports/round-48` |
|---|---:|---:|
| `19:38:33` | 0 | 3 |
| `19:38:49` | 0 | 3 |
| `19:39:39` | 4 | 7 |

```console
$ date -u +%Y-%m-%dT%H:%M:%SZ; find reports/round-48 -name '*.md' -type f | wc -l; find reports/round-48 -type f | wc -l
2026-10-19T19:39:39Z
4
7
```

Scope: **one worker's self-observation plus file-presence samples.** It proves concurrent seats were active by `19:39:39Z`; it is **not** evidence of 64 launches, 64 completions, any failure count, runtime concurrency, wall time, or actual route. A failed seat can file a fragment and a completed seat can file none, so fragment presence is not a completion rate.

### T6 — the freshness gate's first live use has no durable raw sample

Both declarations report the gate verdicts (`claims.json:23`; `dispatch-declared.json:20`) but file the command with placeholders:

```
python3 tools/harness/claims-freshness.py --claims <candidates> --checks <overlay>
```

(`claims.json:22`; `dispatch-declared.json:19`.) The concrete inputs exist only in `.scratch/`:

| Scratch path | SHA-256 at draft time | Content |
|---|---|---|
| `.scratch/r48-claims-skel.json` | `65b8644146f235e51d70211c4d2650fd97a699db6a089668d3edfa1f254a5080` | 3 candidate claims (C, O, Ca) |
| `.scratch/r48-freshness-check.json` | `7acbd8ca5fa79d3fff5efee3738e4111e8a6a3de3ace490195b4664982813c13` | checks overlay: C×2, O×1, Ca×1 probes |

`AGENTS.md:17-20` requires the raw samples needed to reproduce every reported count to land under `reports/round-<N>/telemetry/` before scratch cleanup. Without them, "O STALE / C FRESH / Ca FRESH" is prose, not a reproducible check. Skeleton E (§7) is the durable manifest; copying the two inputs (checks contain no prompts or credentials) is the minimum fix.

### T7 — prior closes omit the closed record's digest; r48 makes it mandatory

`AGENTS.md:38-39` requires the closing snapshot to name the record it closes **and that record's SHA-256 at close time**. Precedents:

- `reports/round-43/telemetry/availability-close-43.json:6` carries the literal string `"see declared_artifacts below"`, and `declared_artifacts` does not list the dispatch-declared record.
- `reports/round-44/telemetry/availability-close-44.json:5` and `reports/round-46/telemetry/availability-close-46.json:5` name `closes_record` but have no digest key (`grep -n "closes_record\|closes_sha256"` over both files).
- `reports/round-47/telemetry/availability-close-47.json:5` likewise names the record with no digest.
- `reports/round-46/telemetry/availability-close-46.json:26` leaves `open_at_close` non-null, which by `AGENTS.md:32` is not a complete record.

Skeleton B therefore pins `closes_record_sha256_at_close` to the measured `40a96ab6…`, requires `open_fields: []`, and records unresolved fields as `could-not-recover` with owner + reason (complete, not open). Filed rounds are not edited; this is a successor-record convention.

### T8 — counter semantics this draft enforces

1. **Requested ≠ observed.** `requested_workers: 64` is never copied into `launched`, `completed`, or `failed`.
2. **Unknown is null, not zero.** Every null carries owner + reason; the close either fills it from a durable artifact or records `could-not-recover`.
3. **Provider liveness is not round acceptance** (`AGENTS.md:26`). Acceptance lives only in `validation_receipt`.
4. **A flat batch result cannot measure runtime concurrency.** It stays null unless concurrent-session samples are filed.
5. **Fragment presence is corroboration, not completion.** A closed-window `find` is required for the final count.

---

## 3. Skeleton A — `reports/round-48/telemetry/observed-dispatch.json`

Fence for the integrator. Replace every `<FILL …>`; keep `null` only where an owner and reason survive. Do not file with `state: open-at-seat-close`.

```json
{
 "schema": "kotodama-observed-dispatch-v1",
 "round": 48,
 "kind": "observed-dispatch",
 "owner": "kotodama-shokunin (integrator)",
 "state": "<FILL: final | final-with-could-not-recover>",
 "state_rule": "never open-at-seat-close (AGENTS.md:32-38)",
 "observation_closed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ at filing>",
 "observation_date": "2026-10-19",
 "observation_window_utc": {
  "start": null,
  "end": null,
  "basis": "<FILL: native start/end or wall_seconds from telemetry/inputs/dispatch-result.raw.json; else could-not-recover + owner>"
 },
 "requested_allocation": {
  "provider_lane": "opencode-go",
  "model": "deepseek-v4.1-flash",
  "key": "key-2 (round-robin)",
  "requested_workers": 64,
  "batched_calls": 1,
  "baseline_commit": "a01405d",
  "loop": 2,
  "position": 2,
  "claims_in_round": ["C", "Ca"],
  "source": "reports/round-48/telemetry/dispatch-declared.json:5-13; reports/round-48/claims.json:6-12"
 },
 "observed": {
  "launched": null,
  "launched_owner": "kotodama-shokunin (integrator)",
  "launched_reason": "<FILL: count(seats[].started == true) from the native extract; if any started is null -> could-not-recover; never copy requested_workers>",
  "completed": null,
  "completed_owner": "kotodama-shokunin (integrator)",
  "completed_reason": "<FILL: count(seats[].outcome == 'completed'); do not derive from fragment presence>",
  "failed": null,
  "failed_owner": "kotodama-shokunin (integrator)",
  "failed_reason": "<FILL: count(seats[].outcome == 'failed'); write 0 only after the command returns 0>",
  "counter_invariant": "completed + failed == launched, asserted only when every seats[].started and seats[].outcome is known",
  "failure_classes": null,
  "failure_classes_source": "<FILL: seat ids + error classes from the native summary; [] only if measured 0>",
  "filed_fragments_md": null,
  "filed_fragments_owner": "kotodama-shokunin (integrator)",
  "filed_fragments_reason": "<FILL: integer from a closed-window find at observation_closed_at_utc; draft-time samples were 0/0/4 and are partial>",
  "filed_fragments_counting_command": "find reports/round-48 -name '*.md' -type f | wc -l",
  "absent_seats": null,
  "absent_seats_source": "<FILL: seat ids with no non-empty declared out file at the closed window; [] only if measured>",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "kotodama-shokunin (integrator)",
  "runtime_concurrency_reason": "not derivable from a flat batch result; no concurrent-session sampler ran",
  "actual_route": {
   "requested": "opencode-go/deepseek-v4.1-flash key-2",
   "observed": null,
   "observed_owner": "kotodama-shokunin (integrator)",
   "observed_reason": "<FILL: wire model/provider response from the native extract; do not copy the requested route; could-not-recover if no wire identity>"
  },
  "key_census": {
   "observed": null,
   "declared": "key-2 (round-robin)",
   "source": "reports/round-48/telemetry/dispatch-declared.json:8",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "declared row only; no key re-census this round"
  }
 },
 "deviation": null,
 "deviation_note": "<FILL: named deviations only; null if the opencode-go key-2 batch ran as declared>",
 "partial_observation": true,
 "partial_observations": [
  {
   "kind": "worker self-observation + seat-output presence samples",
   "filing": "file telemetry/worker-observation-s02.json (§6) before citing; otherwise drop this row",
   "samples": [
    {"at_utc": "2026-10-19T19:38:33Z", "md_fragments": 0, "all_files": 3},
    {"at_utc": "2026-10-19T19:38:49Z", "md_fragments": 0, "all_files": 3},
    {"at_utc": "2026-10-19T19:39:39Z", "md_fragments": 4, "all_files": 7}
   ],
   "counting_command": "date -u +%Y-%m-%dT%H:%M:%SZ; find reports/round-48 -name '*.md' -type f | wc -l; find reports/round-48 -type f | wc -l",
   "scope": "one worker (S02) plus file-presence samples; not a dispatch census of 64"
  }
 ],
 "durable_sources": [
  {"path": "reports/round-48/claims.json", "sha256": "bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292", "bytes": 5545, "observed_at_utc": "2026-10-19T19:39:39Z", "matches_declaration": true},
  {"path": "reports/round-48/targets.json", "sha256": "d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446", "bytes": 18585, "observed_at_utc": "2026-10-19T19:39:39Z", "matches_declaration": true, "seat_count": 64},
  {"path": "reports/round-48/telemetry/dispatch-declared.json", "sha256": "40a96ab6227ca229d615a8bdcca1d32124447a5433bfbe53f7e26c9e33d2ab4e", "bytes": 1239, "observed_at_utc": "2026-10-19T19:39:39Z"},
  {"path": "reports/round-48/telemetry/inputs/dispatch-result.raw.json", "sha256": "<FILL at filing; otherwise remove this row and set counters could-not-recover>", "note": "redacted native extract (§5); the artifact that makes the counters reproducible"}
 ],
 "closing_snapshot": {
  "owed": true,
  "path": "reports/round-48/telemetry/availability-close-48.json",
  "rule": "AGENTS.md:32-38 — a round is not admitted to LOG.md while this record owes a close"
 }
}
```

Filing rule: if no native dispatch result is retained, leave `launched`/`completed`/`failed` null, set each reason to `could-not-recover` with the integrator as owner, set `state: final-with-could-not-recover`, and say so in the close. Do **not** infer 64 from `requested_workers` and do **not** infer completion from the fragment count.

---

## 4. Skeleton B — `reports/round-48/telemetry/availability-close-48.json`

File only after `reports/round-48/validation.json` exists. This is a **new append-only file**; never edit `dispatch-declared.json` or `observed-dispatch.json` to close the round.

```json
{
 "schema": "kotodama-availability-closing-snapshot-v1",
 "round": 48,
 "kind": "availability-close",
 "owner": "kotodama-shokunin (integrator)",
 "filed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ>",
 "closed_sampling_window_utc": {
  "start": "<FILL or null>",
  "end": "<FILL or null>",
  "basis": "<FILL: native start/end or wall_seconds; else could-not-recover + owner>"
 },
 "closes_record": "reports/round-48/telemetry/dispatch-declared.json",
 "closes_record_sha256_at_close": "<FILL: re-measure; draft-time value 40a96ab6227ca229d615a8bdcca1d32124447a5433bfbe53f7e26c9e33d2ab4e>",
 "closes_record_digest_note": "measured 2026-10-19T19:39:39Z. If the close-time digest differs, the original was edited in place (forbidden): file an amendment, never rewrite it",
 "also_closes": [
  {"path": "reports/round-48/telemetry/observed-dispatch.json", "sha256": "<FILL at close: sha256sum reports/round-48/telemetry/observed-dispatch.json>", "note": "primary source for the counters in closed_fields"}
 ],
 "baseline_commit": "a01405d",
 "counting_command": "python3 - <<'PY' (checklist §8 step 4 over telemetry/inputs/dispatch-result.raw.json); find reports/round-48 -name '*.md' -type f | wc -l",
 "counting_date": "2026-10-19",
 "closed_fields": {
  "observed_launches": {
   "value": "<FILL: integer, or null>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: telemetry/inputs/dispatch-result.raw.json#/seats>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL: null if measured; otherwise why>",
   "re_derivation_command": "python3 - <<'PY' (checklist §8 step 4)"
  },
  "observed_completions": {
   "value": "<FILL: integer, or null>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: same extract>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL>"
  },
  "observed_failures": {
   "value": "<FILL: integer, or null>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: same extract>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL>"
  },
  "failure_classes": {
   "value": "<FILL: seat ids + error classes, or [] if measured 0>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: native summary>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL>"
  },
  "observed_window_utc": {
   "value": "<FILL: start/end or wall_seconds>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: native extract>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL>"
  },
  "actual_route_observed": {
   "value": "<FILL: wire model/provider response, or null>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: telemetry/inputs/dispatch-result.raw.json#/route.observed_wire_model>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL: do not copy the requested route into value>"
  },
  "runtime_concurrency": {
   "value": null,
   "status": "could-not-recover",
   "source": "none — a flat batch result cannot measure concurrency",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "no concurrent-session samples were supplied"
  },
  "filed_fragments_md": {
   "value": "<FILL: integer measured at filed_at_utc>",
   "status": "<FILL: measured>",
   "source": "find reports/round-48 -name '*.md' -type f | wc -l",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "corroboration only; not a completion count"
  },
  "absent_seats": {
   "value": "<FILL: seat ids with no non-empty declared out file; [] only if measured>",
   "status": "<FILL: measured>",
   "source": "deliverable census, checklist §8 step 5",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL>"
  },
  "provider_liveness": {
   "value": null,
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: native result only>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "provider liveness is not round acceptance (AGENTS.md:26); null until a native result names it"
  }
 },
 "could_not_recover": ["runtime_concurrency"],
 "could_not_recover_rule": "list every closed_fields key whose status is could-not-recover; runtime_concurrency is always present",
 "declaration_checks": {
  "freshness_gate": {
   "verdicts": {"C": "FRESH", "Ca": "FRESH", "O": "STALE"},
   "verdict_source": "reports/round-48/claims.json:23; reports/round-48/telemetry/dispatch-declared.json:20",
   "durable_sample": "<FILL: reports/round-48/telemetry/freshness-gate-48.json (§7), or could-not-recover with owner>",
   "note": "the gate's raw inputs existed only in .scratch at seat time (T6); persist them before scratch cleanup"
  }
 },
 "validation_receipt": {
  "path": "reports/round-48/validation.json",
  "sha256": "<FILL at close: sha256sum reports/round-48/validation.json>",
  "verdict": "<FILL: admitted | rejected | rejected-honest-stop>",
  "acceptance_checks_passed": "<FILL: true | false>",
  "partial": "<FILL: validation.json#/partial or null>",
  "runner_sha256": "<FILL: validation.json#/input_sha256['reports/round-48/run-validation.py']; else sha256sum the runner and say which basis>",
  "produced_by": "isolated git-archive replay (--out publish inside sandbox); no in-tree runner execution",
  "caveat": "a later runner re-run is a new snapshot row, never an in-place edit"
 },
 "declared_artifacts": {
  "reports/round-48/claims.json": {"declared_sha256": "bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292", "observed_sha256": "<FILL: re-measure at close>", "declaration_match": "<FILL: true | false>"},
  "reports/round-48/targets.json": {"declared_sha256": "d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446", "observed_sha256": "<FILL: re-measure at close>", "seat_count": 64, "declaration_match": "<FILL: true | false>"},
  "reports/round-48/telemetry/dispatch-declared.json": {"sha256_at_close": "<FILL: re-measure; expected 40a96ab6…>", "matches_draft_time": "<FILL: true | false>"},
  "tools/harness/claims-freshness.py": {"sha256": "466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d", "note": "same bytes as the r47 close pinned"}
 },
 "availability": {
  "requested_lane": "opencode-go/deepseek-v4.1-flash key-2 (round-robin; position 2; 64 seats)",
  "observed_route": null,
  "observed_route_owner": "kotodama-shokunin (integrator)",
  "observed_route_reason": "<FILL: from the native extract/validation; never copy the requested lane>",
  "route_history": [
   {"attempt": "1", "lane": "opencode-go", "model": "deepseek-v4.1-flash", "key": "key-2", "status": "the batch this record closes", "source": "reports/round-48/telemetry/dispatch-declared.json:5-13"}
  ],
  "availability_attempts": {"files": [], "note": "no availability-attempt-48 file exists at seat sampling; if an interruption occurred but went unrecorded, file an attempt row with its own provenance"},
  "provider_liveness": null,
  "provider_liveness_note": "provider liveness is not round acceptance (AGENTS.md:26); fill only from the native result, else null + owner"
 },
 "open_fields": [],
 "open_fields_rule": "must be [] at close; any entry means the record is incomplete and the round is not admissible to LOG.md (AGENTS.md:32-38)",
 "sources": [
  "reports/round-48/telemetry/dispatch-declared.json (sha256 pinned above)",
  "reports/round-48/telemetry/observed-dispatch.json (sha256 pinned above)",
  "reports/round-48/telemetry/inputs/dispatch-result.raw.json (if filed)",
  "reports/round-48/telemetry/worker-observation-s02.json (if filed)",
  "reports/round-48/telemetry/freshness-gate-48.json (if filed)",
  "reports/round-48/validation.json (sha256 pinned above)"
 ]
}
```

---

## 5. Skeleton C — `reports/round-48/telemetry/inputs/dispatch-result.raw.json`

Redacted native extract. It must reproduce every counter in §3–§4 and never contains prompts, credentials, or authorization headers. The generator in §8 emits all 64 seat ids from `targets.json` so no seat is silently dropped.

```json
{
 "schema": "kotodama-dispatch-result-extract-v1",
 "round": 48,
 "source_kind": "<FILL: native batch tool result | provider result file | operator transcript; be exact>",
 "tool": "<FILL: tool/route name>",
 "batch_id": "<FILL or null>",
 "owner": "kotodama-shokunin (integrator)",
 "captured_at_utc": "<FILL>",
 "wall_seconds": null,
 "seats": [
  {"seat_id": "K01", "out": "scout/K01-rightsized-spec.md", "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null, "fragment_present": null}
 ],
 "route": {
  "provider_lane": "opencode-go",
  "requested_model": "deepseek-v4.1-flash",
  "observed_wire_model": "<FILL or null>",
  "basis": "<FILL: response header/field, or null + reason>"
 },
 "redactions": ["credentials", "authorization headers", "prompts and private payloads"],
 "limits": [
  "A flat seat list does not measure runtime concurrency.",
  "Provider liveness is not round acceptance.",
  "Null timing fields mean unavailable, not zero.",
  "fragment_present is a file-presence check, not proof the seat completed."
 ]
}
```

`seats[]` must contain all 64 ids exactly once. `started` and `outcome` are `true|false|null` and `"completed"|"failed"|null`; `null` forces `could-not-recover`, never a guessed zero.

---

## 6. Skeleton D — `reports/round-48/telemetry/worker-observation-s02.json`

The only durable home for the §T5 samples. File it before citing them, or drop the `partial_observations` row from §3.

```json
{
 "schema": "kotodama-worker-observation-v1",
 "round": 48,
 "kind": "worker-observation",
 "owner": "S02 (seat; telemetry scribe)",
 "observed_at_utc": "2026-10-19T19:39:39Z",
 "evidence_kind": "worker self-observation + seat-output presence samples",
 "sessions": [{"assignment": "S02", "state_at_observation": "active"}],
 "samples": [
  {"at_utc": "2026-10-19T19:38:33Z", "md_fragments": 0, "all_files": 3, "present_md": []},
  {"at_utc": "2026-10-19T19:38:49Z", "md_fragments": 0, "all_files": 3, "present_md": []},
  {"at_utc": "2026-10-19T19:39:39Z", "md_fragments": 4, "all_files": 7, "present_md": null}
 ],
 "counting_command": "find reports/round-48 -name '*.md' -type f | wc -l",
 "counting_date": "2026-10-19",
 "declared_seats": 64,
 "scope": "One worker self-observation plus file-presence samples. Not a dispatch census; no evidence of 64 launches, completions, failures, concurrency, wall time, or actual route.",
 "unavailable_owner": "Round-48 integrator (native dispatch/result holder)",
 "unavailable_reason": "The worker-visible claims/targets declare an allocation; the native batch result was not supplied to this worker."
}
```

`present_md` at `19:39:39Z` is recorded as `null` because this seat did not list the names at that instant; the count is the measured value. The final pre-filing sample should be appended as a new row, not written over these.

---

## 7. Skeleton E — `reports/round-48/telemetry/freshness-gate-48.json` (recommended, new)

This repairs T6: the round's only first-use evidence of the freshness gate currently depends on `.scratch/`. Copy the two inputs into `telemetry/inputs/` (they hold check specs, no prompts or credentials), re-run the concrete command, and file this manifest with the redacted stdout. If the integrator declines, `declaration_checks.freshness_gate.durable_sample` in §4 must read `could-not-recover` with owner + reason.

```json
{
 "schema": "kotodama-freshness-gate-sample-v1",
 "round": 48,
 "kind": "freshness-gate-sample",
 "owner": "kotodama-shokunin (integrator)",
 "gate": {"path": "tools/harness/claims-freshness.py", "sha256": "466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d"},
 "inputs": {
  "candidates": {"scratch_path": ".scratch/r48-claims-skel.json", "sha256": "65b8644146f235e51d70211c4d2650fd97a699db6a089668d3edfa1f254a5080", "durable_path": "reports/round-48/telemetry/inputs/freshness-candidates-48.json"},
  "checks": {"scratch_path": ".scratch/r48-freshness-check.json", "sha256": "7acbd8ca5fa79d3fff5efee3738e4111e8a6a3de3ace490195b4664982813c13", "durable_path": "reports/round-48/telemetry/inputs/freshness-checks-48.json"}
 },
 "command_as_filed": "python3 tools/harness/claims-freshness.py --claims <candidates> --checks <overlay>",
 "command_as_filed_source": "reports/round-48/claims.json:22; reports/round-48/telemetry/dispatch-declared.json:19",
 "command_concrete_required": "python3 tools/harness/claims-freshness.py --claims reports/round-48/telemetry/inputs/freshness-candidates-48.json --checks reports/round-48/telemetry/inputs/freshness-checks-48.json",
 "verdicts": {"C": "FRESH", "Ca": "FRESH", "O": "STALE"},
 "verdict_source": "reports/round-48/claims.json:23; reports/round-48/telemetry/dispatch-declared.json:20",
 "exit_codes": {"C": null, "Ca": null, "O": null, "owner": "kotodama-shokunin (integrator)", "reason": "<FILL from the re-run; do not infer an exit code from verdict prose>"},
 "raw_output_path": "<FILL: reports/round-48/telemetry/inputs/freshness-gate-48.stdout.txt>",
 "raw_output_sha256": "<FILL>",
 "redactions": ["credentials", "authorization headers", "prompts and private payloads"],
 "note": "the gate's first live use dropped the O claim; the durable sample is what makes that ruling re-checkable after scratch cleanup"
}
```

---

## 8. Fill checklist (integrator)

Run from the repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Never run `reports/round-48/run-validation.py` in-tree; use the isolated replay precedent and let the receipt land at `reports/round-48/validation.json`.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. Hard precondition for the CLOSE (not for observed-dispatch).
test -f reports/round-48/validation.json && echo CLOSE-READY || echo BLOCKED

# 2. Durable input copies.
mkdir -p reports/round-48/telemetry/inputs
cp reports/round-48/claims.json reports/round-48/telemetry/inputs/claims.json
cp reports/round-48/targets.json reports/round-48/telemetry/inputs/targets.json
cp .scratch/r48-claims-skel.json reports/round-48/telemetry/inputs/freshness-candidates-48.json
cp .scratch/r48-freshness-check.json reports/round-48/telemetry/inputs/freshness-checks-48.json
sha256sum reports/round-48/telemetry/inputs/*.json
# expected claims bf8df21b... / targets d029eaa1... / candidates 65b86441... / checks 7acbd8ca...

# 3. Emit the 64-row native-extract template (no seat omitted).
python3 -B - <<'PY'
import json
t=json.load(open('reports/round-48/targets.json'))
template={
 "schema":"kotodama-dispatch-result-extract-v1","round":48,
 "source_kind":"<FILL>","tool":"<FILL>","batch_id":None,
 "owner":"kotodama-shokunin (integrator)","captured_at_utc":"<FILL>",
 "wall_seconds":None,
 "seats":[{"seat_id":x["id"],"out":x["out"],"started":None,"outcome":None,
           "failure_phase":None,"error_class":None,"started_at_utc":None,
           "ended_at_utc":None,"fragment_present":None} for x in t["seats"]],
 "route":{"provider_lane":"opencode-go","requested_model":"deepseek-v4.1-flash",
          "observed_wire_model":None,"basis":"<FILL>"},
 "redactions":["credentials","authorization headers","prompts and private payloads"],
 "limits":["A flat seat list does not measure runtime concurrency.",
           "Provider liveness is not round acceptance.",
           "Null timing fields mean unavailable, not zero."]
}
open('reports/round-48/telemetry/inputs/dispatch-result.raw.json','w').write(json.dumps(template,indent=1)+"\n")
print('rows', len(template['seats']))
PY

# 4. Derive counters and assert invariants.
python3 -B - <<'PY'
import json
d=json.load(open('reports/round-48/telemetry/inputs/dispatch-result.raw.json'))
t=json.load(open('reports/round-48/targets.json'))
s=d['seats']
assert len(s)==64, len(s)
declared={x['id'] for x in t['seats']}; got={x['seat_id'] for x in s}
assert got==declared, (sorted(declared-got), sorted(got-declared))
unknown_start=[x['seat_id'] for x in s if x.get('started') is None]
unknown_out=[x['seat_id'] for x in s if x.get('outcome') is None]
launched=None if unknown_start else sum(1 for x in s if x['started'])
completed=None if unknown_out else sum(1 for x in s if x['outcome']=='completed')
failed=None if unknown_out else sum(1 for x in s if x['outcome']=='failed')
print('rows=%d launched=%s completed=%s failed=%s unknown_start=%d unknown_outcome=%d'%(
    len(s), launched, completed, failed, len(unknown_start), len(unknown_out)))
if None not in (launched, completed, failed):
    assert completed+failed==launched, (completed,failed,launched)
    print('INVARIANT-OK completed+failed==launched')
else:
    print('could-not-recover started=%s outcome=%s' % (
        ','.join(unknown_start) or 'none', ','.join(unknown_out) or 'none'))
PY

# 5. Deliverable census (corroboration only; NOT dispatch evidence).
python3 -B - <<'PY'
import json,os
t=json.load(open('reports/round-48/targets.json'))
rows=[(x['id'], os.path.join('reports/round-48',x['out'])) for x in t['seats']]
present=[i for i,p in rows if os.path.isfile(p)]
nonempty=[i for i,p in rows if os.path.isfile(p) and os.path.getsize(p)>0]
absent=[i for i,p in rows if not os.path.isfile(p)]
print('declared=%d present=%d nonempty=%d absent=%d'%(len(rows),len(present),len(nonempty),len(absent)))
print('absent:',','.join(absent))
PY

# 6. Close-time stamps and digests.
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum reports/round-48/telemetry/observed-dispatch.json \
          reports/round-48/telemetry/dispatch-declared.json \
          reports/round-48/validation.json \
          reports/round-48/claims.json reports/round-48/targets.json
# claims/targets must still equal bf8df21b... / d029eaa1...

# 7. File order: worker-observation (§6, if cited) -> freshness-gate (§7, recommended)
#    -> observed-dispatch (§3) -> availability-close-48 (§4). Replace every <FILL ...>.

# 8. Post-file invariant check (read-only).
python3 -B - <<'PY'
import json,hashlib
c=json.load(open('reports/round-48/telemetry/availability-close-48.json'))
assert c['closes_record']=='reports/round-48/telemetry/dispatch-declared.json'
assert c['closes_record_sha256_at_close']==hashlib.sha256(open(c['closes_record'],'rb').read()).hexdigest(), 'closed-record digest mismatch'
for row in c['also_closes']:
    assert row['sha256']==hashlib.sha256(open(row['path'],'rb').read()).hexdigest(), row['path']
assert c['open_fields']==[], c['open_fields']
r=c['validation_receipt']
assert r['sha256']==hashlib.sha256(open(r['path'],'rb').read()).hexdigest(), 'receipt digest mismatch'
o=json.load(open('reports/round-48/telemetry/observed-dispatch.json'))
assert o['state']!='open-at-seat-close', 'incomplete record'
assert 'FILL' not in json.dumps(c), 'unreplaced placeholder in close'
print('CLOSE-OK')
PY
```

Expected at draft time: step 1 prints `BLOCKED`; step 2's digests match §1 and T6; step 3 writes 64 rows; step 4 prints 64 rows with null counters until the native extract is filled; step 5 measures the final fragment census; step 8 prints `CLOSE-OK` only after every placeholder is replaced and every digest re-checks.

If the native result is unavailable at close: leave the three counters `null`, set each status to `could-not-recover` with the integrator as owner, keep `could_not_recover` listing them, and still close. The gap stays visible; the round is not admitted to `LOG.md` until the close file exists.

---

## 9. To-verify / open items (owner: integrator unless noted)

1. **Launch/completion/failure counts and error classes** — fill from the native batch summary or the redacted extract; null + `could-not-recover` if no extract exists.
2. **Observed wire model** — from the native provider response; the requested alias is not evidence of the route served.
3. **Runtime concurrency** — no measurement exists; stays null with owner + reason unless concurrent-session samples are filed.
4. **Declared timestamps** — `claims.json:6` and `dispatch-declared.json:5` read `19:45:00Z`, ~370 s ahead of the system clock at sampling (T2); do not carry into observed fields. Status `to-verify`.
5. **Freshness-gate raw sample** — copy `.scratch/r48-claims-skel.json` and `.scratch/r48-freshness-check.json` into `telemetry/inputs/` and file §7 before scratch cleanup, or record `could-not-recover`.
6. **Interrupted attempts** — no `availability-attempt-48` file exists at sampling; if one occurred unrecorded, file a new row with its own provenance, never reconstruct.
7. **Runner digest basis** — if `validation.json#/input_sha256` lacks `run-validation.py`, record the computed runner digest and say which basis was used.
8. **Final fragment sample** — the close's `filed_fragments_md` must be measured at filing time, not copied from §6's draft-time samples.

---

## 10. Negative proof

- Wrote only `reports/round-48/scribe/S02-telemetry-draft.md`; no file under `reports/round-48/telemetry/` was created or edited by this seat.
- No `corpus/**`, `tools/**`, `README.md`, or `reports/round-1..47/**` byte touched; nothing staged under `corpus/`; no git commit/push; no install; no network.
- No `reports/round-*/run-validation.py` executed.
- Every number above is from a read-only command in this seat (`date`, `find`, `ls`, `stat`, `sha256sum`, `git rev-parse`, `git status`, `python3` JSON readers) and is reproducible from the named path or the shown command. Unknown counters are `null` with an owner and reason, never inferred zeroes.
