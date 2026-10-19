# S02 — telemetry scribe: observed-dispatch + availability-close-47 skeletons

- Seat: **S02**, role scribe, claim cross (`reports/round-47/targets.json:63`).
- Round 47, loop 2, position 1, baseline `6e9a30d` (`reports/round-47/claims.json:5-6`).
- Dispatch under observation: `opencode-go` / `deepseek-v4.1-flash`, key-1, 64 requested workers, 1 batched call (`reports/round-47/telemetry/dispatch-declared.json:5-13`).
- Observed at `2026-10-19T17:59:45Z` (`date -u +%Y-%m-%dT%H:%M:%SZ`); local zone `-03`.
- Writes: **this file only** (`reports/round-47/scribe/S02-telemetry-draft.md`). Nothing under `reports/round-47/telemetry/` is created or edited by this seat; the skeletons below are for the integrator.
- Canon: NON-CANON. No corpus, tools, README, or filed-round byte touched; no runner executed; no commit/push/install/network.

Mission: draft the observed-dispatch and availability-close-47 skeletons — owner, observation window, counting commands, durable source paths, SHA-256 pins — so the integrator can file them without reconstructing numbers. The skeletons are §3–§6; the provenance that shapes them is §2; the fill procedure is §7.

---

## 1. Durable inputs read at observation

| Path | Bytes | SHA-256 (measured `2026-10-19T17:59:45Z`) | mtime UTC |
|---|---:|---|---|
| `reports/round-47/claims.json` | 6113 | `7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34` | `2026-10-19 17:47:07.820590014` |
| `reports/round-47/targets.json` | 18755 | `d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d` | `2026-10-19 17:48:10.806752986` |
| `reports/round-47/telemetry/dispatch-declared.json` | 985 | `3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8` | `2026-10-19 17:48:20.024776793` |

Commands and raw output:

```console
$ sha256sum reports/round-47/claims.json reports/round-47/targets.json reports/round-47/telemetry/dispatch-declared.json
7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34  reports/round-47/claims.json
d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d  reports/round-47/targets.json
3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8  reports/round-47/telemetry/dispatch-declared.json
$ wc -c reports/round-47/claims.json reports/round-47/targets.json reports/round-47/telemetry/dispatch-declared.json
 6113 reports/round-47/claims.json
18755 reports/round-47/targets.json
  985 reports/round-47/telemetry/dispatch-declared.json
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git ls-files reports/round-47 | wc -l
0
$ TZ=UTC stat -c '%y %s %n' reports/round-47/claims.json reports/round-47/targets.json reports/round-47/telemetry/dispatch-declared.json
2026-10-19 17:47:07.820590014 +0000 6113 reports/round-47/claims.json
2026-10-19 17:48:10.806752986 +0000 18755 reports/round-47/targets.json
2026-10-19 17:48:20.024776793 +0000 985 reports/round-47/telemetry/dispatch-declared.json
```

Precedent read for schema: `reports/round-43/telemetry/{observed-dispatch,availability-close-43}.json`, `reports/round-44/telemetry/*`, `reports/round-46/telemetry/*`, `reports/round-35/telemetry/availability-attempt-{1,2,3}.json`, and the binding rules in `AGENTS.md:15-39` ("Availability and dispatch telemetry", "Close what you open").

---

## 2. Provenance findings

### T1 — the declared artifact pins match the live files exactly

`dispatch-declared.json:14-17` pins `claims.json` at `7eb16979…` and `targets.json` at `d60e5572…` with `seat_count: 64`. Both live digests match byte-for-byte (§1). This is the opposite of r43, where the declared `claims.json` digest named different content and the closing snapshot had to re-pin the live digest (`reports/round-43/telemetry/availability-close-43.json:18`; seat draft finding `reports/round-43/scribe/S02-telemetry-draft.md:40-67`). **No dispatch-declared amendment is owed for r47.**

One timing nuance, not a drift: `declared_at_utc` is `17:46:52Z` (`dispatch-declared.json:5`), while the artifacts carry mtimes `17:47:07`–`17:48:20`. The pins were taken over the final bytes (they match), so the declaration time is the intent time, not a digest timestamp. Recorded here so a later reader does not misread the 88-second gap as a stale pin.

### T2 — HEAD equals the declared baseline; the round directory is untracked

```console
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git log -1 --format='%H %ad %s' --date=iso
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe 2026-10-19 14:46:42 -0300 round-46: loop-1 retrospective — 9 admitted / 4 honest-stops / 1 skipped (argon); defects + provider amendments carried to loop 2
$ git ls-files reports/round-47 | wc -l
0
$ git status --porcelain reports/round-47
?? reports/round-47/
$ git status --porcelain reports/round-47 | wc -l
1
```

`claims.json:6` declares `baseline_commit: 6e9a30d`; live HEAD is that commit. But **zero r47 files are tracked at HEAD** — the entire round directory is untracked (`git status --porcelain reports/round-47` returns one `??` row). Consequences for telemetry:

1. The round's durable identity is the SHA-256 pins and the filed telemetry records, not a commit.
2. Any tool that re-derives a `before` at the baseline — the O claim's freshness gate — must read `git show 6e9a30d:<path>`, never the worktree. The worktree already contains r47 drafts.
3. A close snapshot cannot cite a commit for r47; it cites the pinned digests and `reports/round-47/validation.json`.

### T3 — close preconditions are not met at observation

```console
$ ls reports/round-47/run-validation.py reports/round-47/validation.json reports/round-47/telemetry/inputs
ls: cannot access 'reports/round-47/run-validation.py': No such file or directory
ls: cannot access 'reports/round-47/validation.json': No such file or directory
ls: cannot access 'reports/round-47/telemetry/inputs': No such file or directory
```

The availability close is therefore **blocked** until the round's `validation.json` lands. The `observed-dispatch` record may be filed before that (it does not depend on acceptance), but the round cannot be admitted to `LOG.md` while the close is owed (`AGENTS.md:32-38`). A rejected round still closes — r44 filed a close with `verdict: rejected-honest-stop` (`reports/round-44/telemetry/availability-close-44.json:11`).

### T4 — the declared seat contract is clean and reproducible

```console
$ python3 - <<'PY'
import json,os
from collections import Counter
d=json.load(open('reports/round-47/targets.json'))
s=d['seats']
print('seat_count',d['seat_count'],'seats',len(s),'unique_ids',len({x['id'] for x in s}),'unique_outs',len({x['out'] for x in s}))
print('roles',dict(Counter(x['role'] for x in s)))
print('claims',dict(Counter(x['claim'] for x in s)))
print('escapes',[x['out'] for x in s if x['out'].startswith('/') or '..' in x['out'].split('/')])
print('exts',sorted({os.path.splitext(x['out'])[1] for x in s}))
print('collisions',[k for k,v in Counter(x['out'] for x in s).items() if v>1])
PY
seat_count 64 seats 64 unique_ids 64 unique_outs 64
roles {'scout': 3, 'planner': 3, 'connector': 1, 'executor': 19, 'verifier': 23, 'scribe': 5, 'reviewer': 5, 'critic': 5}
claims {'C': 22, 'O': 21, 'cross': 13, 'Ca': 8}
escapes []
exts ['.md']
collisions []
```

All 64 out paths are `.md`; there are no duplicate out paths and no path escapes. This is the reproducible count behind `requested_workers: 64` — **it is not a launch, completion, or failure count.**

### T5 — partial worker observation: fragments appear 8–13 minutes after declaration

Read-only samples, each with its own timestamp and the same counting command:

| Sampled at (UTC) | `.md` fragments | Present (new since previous sample) |
|---|---:|---|
| `17:51:40` | 0 | — |
| `17:53:32` | 0 | — |
| `17:55:10` | 3 | K01, K02, Ca02 |
| `17:55:56` | 6 | P01, C05, C10 |
| `17:56:47` | 8 | C04, Ca01 |
| `17:57:47` | 11 | C03, Ca03, X00 |
| `17:59:45` | 17 | C01, C07, Ca05, O10, V01, X05 |

```console
$ date -u +%Y-%m-%dT%H:%M:%SZ; find reports/round-47 -name '*.md' | wc -l
2026-10-19T17:59:45Z
17
$ find reports/round-47 -name '*.md' -printf '%f\n' | sort
C01-entry-a.md C03-entry-c.md C04-entry-header.md C05-freshness.md C07-contract-audit.md C10-sweep.md Ca01-stale-premises.md Ca02-resolver-edge.md Ca03-manifest-schemas.md Ca05-verify.md K01-gap-recheck.md K02-seed-extract.md O10-exit-codes.md P01-plan.md V01-post-landing.md X00-connector.md X05-baseline-drift.md
```

Scope: **one worker's self-observation plus file-presence samples.** It proves concurrent seats were active and that at least 17 deliverables existed at `17:59:45Z`. It is **not** evidence of 64 launches, 64 completions, any failure count, runtime concurrency, wall time, or actual route. A failed seat can file a fragment and a completed seat can file none, so fragment count is not a completion rate.

### T6 — standing provider amendments in force (not r47 route deviations)

The loop-1 retrospective and the r47 declaration both carry two standing amendments:

- **Antigravity lanes non-functional** — positions 12/13 (rounds 44/45) and loop-2/3 argon positions are skipped or re-routed (`reports/round-46/loop-1-retrospective.md:4,23,52,59-60`; `reports/round-47/telemetry/dispatch-declared.json:18`).
- **zai usage exhausted** — zai seats route to `openai-codex/gpt-6-luna-max` for the session (`reports/round-46/loop-1-retrospective.md:53,59`; `dispatch-declared.json:18`).

Neither applies to the r47 batch: position 1 is `opencode-go/deepseek-v4.1-flash` on key-1 (`dispatch-declared.json:6-8`). No `availability-attempt-47*.json` exists, and the declaration names a single batched call (`dispatch-declared.json:9-10`). The close skeleton records the amendments as named deviations **in force**, not as observed r47 route changes. The key census (`keys 1-2 live, 3-7 402`) is likewise a declaration (`dispatch-declared.json:8`; retrospective `:58`), not a re-census this round.

### T7 — prior closes omit the closed record's digest; this draft makes it mandatory

`AGENTS.md:38-39` requires the closing snapshot to name the record it closes **and that record's SHA-256 at close time**. The filed precedents do not fully comply:

- `reports/round-43/telemetry/availability-close-43.json:6` carries the literal string `"see declared_artifacts below"` instead of a digest.
- `reports/round-44/telemetry/availability-close-44.json:5` and `reports/round-46/telemetry/availability-close-46.json:5` name `closes_record` but have no `closes_record_sha256_at_close` key at all (verified by `grep -n "closes_record\|closes_sha256"` over both files).
- `reports/round-46/telemetry/availability-close-46.json:26` leaves `open_at_close` non-null ("swe-2 reviewer file pending") — by `AGENTS.md:32` that record is not complete.

The r47 skeletons below fix all three: `closes_record_sha256_at_close` is a required field pinned to the measured `3d826369…`; `open_fields` must be `[]`; any unresolved field is recorded as `could-not-recover` with an owner and reason, which is complete rather than open.

### T8 — counter semantics this draft enforces

1. **Requested ≠ observed.** `requested_workers: 64` is an allocation. It must never be copied into `launched`, `completed`, or `failed`.
2. **Unknown is null, not zero.** Every null counter carries `owner` + `reason`; the close either fills it from a durable artifact or records `could-not-recover`.
3. **Provider liveness is not round acceptance** (`AGENTS.md:26`). Acceptance lives in `validation_receipt`, never in the counters.
4. **A flat batch result cannot measure runtime concurrency.** It stays null unless concurrent-session samples exist.

---

## 3. Skeleton A — `reports/round-47/telemetry/observed-dispatch.json`

Fence for the integrator. Replace every `<FILL …>`; keep `null` only where an owner and reason are named. **Do not file this with `state: open-at-seat-close`** — that is an incomplete record under `AGENTS.md:32`.

```json
{
 "schema": "kotodama-observed-dispatch-v1",
 "round": 47,
 "kind": "observed-dispatch",
 "owner": "kotodama-shokunin (integrator)",
 "state": "<FILL: final | final-with-could-not-recover>",
 "state_rule": "never open-at-seat-close (AGENTS.md:32-38); unresolved counters are null with owner+reason, and availability-close-47.json re-states them",
 "declared_at_utc": "2026-10-19T17:46:52Z",
 "declared_at_source": "reports/round-47/telemetry/dispatch-declared.json:5",
 "observation_closed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ at filing>",
 "observation_date": "2026-10-19",
 "observation_window_utc": {
  "start": null,
  "end": null,
  "basis": "<FILL: native start/end or wall_seconds from inputs/dispatch-result.raw.json; else could-not-recover + owner>"
 },
 "requested_allocation": {
  "provider_lane": "opencode-go",
  "model": "deepseek-v4.1-flash",
  "key": "key-1 (round-robin start; keys 1-2 live, 3-7 402)",
  "requested_workers": 64,
  "batched_calls": 1,
  "baseline_commit": "6e9a30d",
  "loop": 2,
  "position": 1,
  "source": "reports/round-47/telemetry/dispatch-declared.json:5-13; reports/round-47/claims.json:5-14"
 },
 "observed": {
  "launched": null,
  "launched_owner": "kotodama-shokunin (integrator)",
  "launched_reason": "<FILL: count(seats[].started == true) from inputs/dispatch-result.raw.json; if any started is null -> could-not-recover with owner; never copy requested_workers>",
  "completed": null,
  "completed_owner": "kotodama-shokunin (integrator)",
  "completed_reason": "<FILL: count(seats[].outcome == 'completed'); do not derive from fragment presence>",
  "failed": null,
  "failed_owner": "kotodama-shokunin (integrator)",
  "failed_reason": "<FILL: count(seats[].outcome == 'failed'); write 0 only after the command returns 0>",
  "counter_invariant": "completed + failed == launched, asserted only when every seats[].started and seats[].outcome is known",
  "failure_classes": null,
  "failure_classes_source": "<FILL: seat ids + error classes from the native summary; [] only if measured 0; never infer from missing fragments>",
  "fragments_present_md": "<FILL: integer measured at observation_closed_at_utc>",
  "fragments_counting_command": "find reports/round-47 -name '*.md' | wc -l",
  "fragments_observed_at_utc": "<FILL>",
  "fragments_scope": "seat deliverable presence only; a failed seat may file a fragment and a completed seat may file none — not a completion rate",
  "absent_seats": "<FILL: seat ids with no non-empty declared out file at observation; [] only if measured>",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "kotodama-shokunin (integrator)",
  "runtime_concurrency_reason": "not derivable from a flat batch result; no concurrent-session samples supplied",
  "actual_route": {
   "requested": "opencode-go/deepseek-v4.1-flash",
   "observed": null,
   "observed_owner": "kotodama-shokunin (integrator)",
   "observed_reason": "<FILL: wire model/provider response from the native extract; do not copy the requested route; could-not-recover if no wire identity>",
   "basis": "<FILL: inputs/dispatch-result.raw.json#/route.observed_wire_model | owner+reason>"
  },
  "key_census": {
   "observed": null,
   "observed_owner": "kotodama-shokunin (integrator)",
   "observed_reason": "not re-censused this round; declared row only",
   "declared": "keys 1-2 live, 3-7 402",
   "source": "reports/round-47/telemetry/dispatch-declared.json:8; reports/round-46/loop-1-retrospective.md:58"
  }
 },
 "deviation": null,
 "deviation_note": "<FILL: named deviations only (provider redirects, interrupted attempts); null if the opencode-go key-1 batch ran as declared>",
 "partial_observation": true,
 "partial_observations": [
  {
   "kind": "worker-self-observation + seat-output presence samples",
   "filing": "file reports/round-47/telemetry/worker-observation-s02.json (§6) before citing; else drop this row",
   "samples": [
    {"at_utc": "2026-10-19T17:51:40Z", "md_fragments": 0},
    {"at_utc": "2026-10-19T17:53:32Z", "md_fragments": 0},
    {"at_utc": "2026-10-19T17:55:10Z", "md_fragments": 3},
    {"at_utc": "2026-10-19T17:55:56Z", "md_fragments": 6},
    {"at_utc": "2026-10-19T17:56:47Z", "md_fragments": 8},
    {"at_utc": "2026-10-19T17:57:47Z", "md_fragments": 11},
    {"at_utc": "2026-10-19T17:59:45Z", "md_fragments": 17},
    {"at_utc": "<FILL: final sample taken immediately before filing>", "md_fragments": "<FILL>"}
   ],
   "counting_command": "date -u +%Y-%m-%dT%H:%M:%SZ; find reports/round-47 -name '*.md' | wc -l",
   "scope": "one worker (S02) plus file-presence samples; not a dispatch census of 64"
  }
 ],
 "durable_sources": [
  {
   "path": "reports/round-47/claims.json",
   "sha256": "7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34",
   "bytes": 6113,
   "observed_at_utc": "2026-10-19T17:59:45Z",
   "matches_declaration": true
  },
  {
   "path": "reports/round-47/targets.json",
   "sha256": "d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d",
   "bytes": 18755,
   "observed_at_utc": "2026-10-19T17:59:45Z",
   "matches_declaration": true,
   "seat_count": 64
  },
  {
   "path": "reports/round-47/telemetry/dispatch-declared.json",
   "sha256": "3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8",
   "bytes": 985,
   "observed_at_utc": "2026-10-19T17:59:45Z"
  },
  {
   "path": "reports/round-47/telemetry/inputs/dispatch-result.raw.json",
   "sha256": "<FILL at filing: sha256sum reports/round-47/telemetry/inputs/dispatch-result.raw.json>",
   "bytes": "<FILL>",
   "note": "redacted native extract (§5); this is the artifact that makes the counters reproducible"
  },
  {
   "path": "reports/round-47/telemetry/worker-observation-s02.json",
   "sha256": "<FILL if filed; otherwise remove this row and the partial_observations row>",
   "bytes": "<FILL>"
  }
 ],
 "closing_snapshot": {
  "owed": true,
  "path": "reports/round-47/telemetry/availability-close-47.json",
  "rule": "AGENTS.md:32-38 — a round is not admitted to LOG.md while this record owes a close"
 }
}
```

Filing rule: if no native dispatch result is retained, leave `launched`/`completed`/`failed` `null`, set each owner/reason to `could-not-recover`, set `state: final-with-could-not-recover`, and say so in the close. Do **not** infer 64 from `requested_workers`.

---

## 4. Skeleton B — `reports/round-47/telemetry/availability-close-47.json`

File only after `reports/round-47/validation.json` exists. This is a **new append-only file**; never edit `dispatch-declared.json` or `observed-dispatch.json` to close the round (`AGENTS.md:33-35`).

```json
{
 "schema": "kotodama-availability-closing-snapshot-v1",
 "round": 47,
 "kind": "availability-close",
 "owner": "kotodama-shokunin (integrator)",
 "filed_at_utc": "<FILL: date -u +%Y-%m-%dT%H:%M:%SZ>",
 "closed_sampling_window_utc": {
  "start": "<FILL or null>",
  "end": "<FILL or null>",
  "basis": "<FILL: native wall_seconds or start/end from inputs/dispatch-result.raw.json; else could-not-recover + owner>"
 },
 "closes_record": "reports/round-47/telemetry/dispatch-declared.json",
 "closes_record_sha256_at_close": "3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8",
 "closes_record_digest_note": "measured 2026-10-19T17:59:45Z; re-measure at close. If it differs, the original was edited (forbidden): file an amendment, never rewrite it",
 "also_closes": [
  {
   "path": "reports/round-47/telemetry/observed-dispatch.json",
   "sha256": "<FILL at close: sha256sum reports/round-47/telemetry/observed-dispatch.json>",
   "note": "primary source for the counters in closed_fields"
  }
 ],
 "baseline_commit": "6e9a30d",
 "counting_command": "python3 - <<'PY' (checklist §7.4 counter derivation over telemetry/inputs/dispatch-result.raw.json); find reports/round-47 -name '*.md' | wc -l",
 "counting_date": "2026-10-19",
 "closed_fields": {
  "observed_launches": {
   "value": "<FILL: integer, or null with status could-not-recover>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: inputs/dispatch-result.raw.json#/seats; command below>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL: e.g. seats[].started unknown>",
   "re_derivation_command": "python3 - <<'PY' (checklist §7.4)"
  },
  "observed_completions": {
   "value": "<FILL: integer, or null>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: same extract>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL: null if measured>"
  },
  "observed_failures": {
   "value": "<FILL: integer, or null>",
   "status": "<FILL: measured | could-not-recover>",
   "source": "<FILL: same extract>",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL: null if measured; cite failure classes>"
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
   "source": "<FILL: inputs/dispatch-result.raw.json#/route.observed_wire_model>",
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
  "fragments_present_md": {
   "value": "<FILL: integer measured at filed_at_utc>",
   "status": "<FILL: measured>",
   "source": "find reports/round-47 -name '*.md' | wc -l",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "corroboration only; not a completion count"
  },
  "absent_seats": {
   "value": "<FILL: seat ids with no non-empty declared out file; [] only if measured>",
   "status": "<FILL: measured>",
   "source": "deliverable census, checklist §7.5",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "<FILL>"
  }
 },
 "could_not_recover": ["runtime_concurrency"],
 "could_not_recover_rule": "list every closed_fields key whose status is could-not-recover; runtime_concurrency is always present",
 "validation_receipt": {
  "path": "reports/round-47/validation.json",
  "sha256": "<FILL at close: sha256sum reports/round-47/validation.json>",
  "verdict": "<FILL: admitted | rejected | rejected-honest-stop>",
  "acceptance_checks_passed": "<FILL: true | false>",
  "runner_sha256": "<FILL: validation.json#/input_sha256['reports/round-47/run-validation.py']; if absent, sha256sum reports/round-47/run-validation.py and say which basis>",
  "partial": "<FILL: validation.json#/partial or null>",
  "produced_by": "<FILL: isolated git-archive replay (--out publish inside sandbox); no in-tree runner execution>",
  "caveat": "a later runner re-run is a new snapshot row, never an in-place edit"
 },
 "declared_artifacts": {
  "reports/round-47/claims.json": {
   "declared_sha256": "7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34",
   "observed_sha256": "<FILL: re-measure at close>",
   "declaration_match": "<FILL: true | false>"
  },
  "reports/round-47/targets.json": {
   "declared_sha256": "d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d",
   "observed_sha256": "<FILL: re-measure at close>",
   "seat_count": 64,
   "declaration_match": "<FILL: true | false>"
  },
  "reports/round-47/telemetry/dispatch-declared.json": {
   "sha256_at_close": "<FILL: re-measure; expected 3d826369…>",
   "matches_draft_time": "<FILL: true | false>"
  }
 },
 "availability": {
  "requested_lane": "opencode-go/deepseek-v4.1-flash (position 1; key-1; 64 seats)",
  "observed_route": null,
  "observed_route_owner": "kotodama-shokunin (integrator)",
  "observed_route_reason": "<FILL: from the native extract/validation; do not copy the requested lane>",
  "route_history": [
   {
    "attempt": "1",
    "lane": "opencode-go",
    "model": "deepseek-v4.1-flash",
    "key": "key-1",
    "status": "the batch this record closes",
    "source": "reports/round-47/telemetry/dispatch-declared.json:6-13"
   },
   {
    "attempt": "standing-amendment-1",
    "lane": "antigravity",
    "model": "gemini-3.8-flash / gemini-4-argon",
    "status": "skipped or re-routed — lanes non-functional on this host",
    "source": "reports/round-46/loop-1-retrospective.md:4,23,52,59-60"
   },
   {
    "attempt": "standing-amendment-2",
    "lane": "zai",
    "model": "glm-5.3-flash-low -> openai-codex/gpt-6-luna-max",
    "status": "standing amendment — zai usage exhausted",
    "source": "reports/round-46/loop-1-retrospective.md:53,59"
   }
  ],
  "availability_attempts": {
   "files": [],
   "note": "no availability-attempt-47 record filed; the round declares one batched call (dispatch-declared.json:9-10). If an interruption happened but went unrecorded, file an attempt row rather than reconstruct it"
  },
  "provider_liveness": null,
  "provider_liveness_note": "provider liveness is not round acceptance (AGENTS.md:26); fill only from the native result, else null + owner",
  "key_census": {
   "observed": null,
   "declared": "keys 1-2 live, 3-7 402",
   "source": "reports/round-47/telemetry/dispatch-declared.json:8; reports/round-46/loop-1-retrospective.md:58",
   "owner": "kotodama-shokunin (integrator)",
   "reason": "declared row only; no re-census this round"
  }
 },
 "open_fields": [],
 "open_fields_rule": "must be [] at close; any entry means the record is incomplete and the round is not admissible to LOG.md (AGENTS.md:32-38)",
 "sources": [
  "reports/round-47/telemetry/dispatch-declared.json (sha256 pinned above)",
  "reports/round-47/telemetry/observed-dispatch.json (sha256 pinned above)",
  "reports/round-47/telemetry/inputs/dispatch-result.raw.json",
  "reports/round-47/telemetry/worker-observation-s02.json (if filed)",
  "reports/round-47/validation.json (sha256 pinned above)"
 ]
}
```

---

## 5. Skeleton C — `reports/round-47/telemetry/inputs/dispatch-result.raw.json`

Redacted native extract. It must reproduce every counter in §3–§4. One row per declared seat; the generator in §7.3 emits all 64 ids from `targets.json` so no seat is silently dropped. This record never contains prompts, credentials, or authorization headers.

```json
{
 "schema": "kotodama-dispatch-result-extract-v1",
 "round": 47,
 "source_kind": "<FILL: native batch tool result | provider result file | operator transcript; be exact>",
 "tool": "<FILL: tool/route name>",
 "batch_id": "<FILL or null>",
 "owner": "kotodama-shokunin (integrator)",
 "captured_at_utc": "<FILL>",
 "wall_seconds": null,
 "seats": [
  {"seat_id": "K01", "out": "scout/K01-gap-recheck.md", "started": null, "outcome": null, "failure_phase": null, "error_class": null, "started_at_utc": null, "ended_at_utc": null, "fragment_present": "<FILL: true | false>"}
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

`seats[]` must contain all 64 ids exactly once. `started` and `outcome` are `true|false|null` / `"completed"|"failed"|null`: `null` means the native extract does not say, which forces `could-not-recover` rather than a guessed zero.

---

## 6. Skeleton D — `reports/round-47/telemetry/worker-observation-s02.json` (partial sample)

This is the only durable home for the §2 T5 samples. If the integrator cites the samples in §3, this file must be filed before scratch cleanup; otherwise drop the `partial_observations` row. It contains no prompt or credential payload.

```json
{
  "schema": "kotodama-worker-observation-v1",
  "round": 47,
  "kind": "worker-observation",
  "owner": "S02 (seat; telemetry scribe)",
  "observed_at_utc": "2026-10-19T17:59:45Z",
  "evidence_kind": "worker-self-observation + seat-output presence samples",
  "source": "date -u +%Y-%m-%dT%H:%M:%SZ and find reports/round-47 -name '*.md' | wc -l, run in the seat shell",
  "sessions": [
    {"assignment": "S02", "state_at_observation": "active"}
  ],
  "samples": [
    {"at_utc": "2026-10-19T17:51:40Z", "md_fragments": 0, "present": []},
    {"at_utc": "2026-10-19T17:53:32Z", "md_fragments": 0, "present": []},
    {"at_utc": "2026-10-19T17:55:10Z", "md_fragments": 3, "present": ["K01", "K02", "Ca02"]},
    {"at_utc": "2026-10-19T17:55:56Z", "md_fragments": 6, "present": ["K01", "K02", "P01", "C05", "C10", "Ca02"]},
    {"at_utc": "2026-10-19T17:56:47Z", "md_fragments": 8, "present": ["K01", "K02", "P01", "C04", "C05", "C10", "Ca01", "Ca02"]},
    {"at_utc": "2026-10-19T17:57:47Z", "md_fragments": 11, "present": ["C03", "C04", "C05", "C10", "Ca01", "Ca02", "Ca03", "K01", "K02", "P01", "X00"]},
    {"at_utc": "2026-10-19T17:59:45Z", "md_fragments": 17, "present": ["C01", "C03", "C04", "C05", "C07", "C10", "Ca01", "Ca02", "Ca03", "Ca05", "K01", "K02", "O10", "P01", "V01", "X00", "X05"]}
  ],
  "counting_command": "find reports/round-47 -name '*.md' | wc -l",
  "counting_date": "2026-10-19",
  "declared_seats": 64,
  "scope": "One worker self-observation plus file-presence samples. Not a dispatch census; no evidence of 64 launches, completions, failures, concurrency, wall time, or actual route.",
  "unavailable_owner": "Round-47 integrator (native dispatch/result holder)",
  "unavailable_reason": "The worker-visible claims/targets declare an allocation; the native batch result was not supplied to this worker."
}
```

The final sample (taken immediately before `observed-dispatch.json` is filed) should be appended as a new row with its own timestamp; do not rewrite the draft-time rows.

---

## 7. Fill checklist (integrator)

Run from the repo root. `TMPDIR`/`PYTHONDONTWRITEBYTECODE` per the round's shared rules. **Never run `reports/round-47/run-validation.py` in-tree**; use the isolated replay precedent and let the receipt land at `reports/round-47/validation.json` (`reports/round-46/telemetry/availability-close-46.json:14`).

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. Hard precondition for the CLOSE (not for observed-dispatch).
test -f reports/round-47/validation.json && echo CLOSE-READY || echo BLOCKED

# 2. Durable input copies (r39-r46 convention; byte-identical).
mkdir -p reports/round-47/telemetry/inputs
cp reports/round-47/claims.json reports/round-47/telemetry/inputs/claims.json
cp reports/round-47/targets.json reports/round-47/telemetry/inputs/targets.json
sha256sum reports/round-47/telemetry/inputs/claims.json reports/round-47/telemetry/inputs/targets.json
# expected: 7eb16979... / d60e5572...

# 3. Emit the 64-row native-extract template (no seat omitted).
python3 - <<'PY'
import json
t=json.load(open('reports/round-47/targets.json'))
template={
 "schema":"kotodama-dispatch-result-extract-v1","round":47,
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
print(json.dumps(template, indent=1))
PY
# Save as reports/round-47/telemetry/inputs/dispatch-result.raw.json, then fill
# started/outcome/failure_phase/error_class from the native result. Do not add prose.

# 4. Derive the counters and assert invariants.
python3 - <<'PY'
import json
d=json.load(open('reports/round-47/telemetry/inputs/dispatch-result.raw.json'))
t=json.load(open('reports/round-47/targets.json'))
s=d['seats']
assert len(s)==64, len(s)
declared={x['id'] for x in t['seats']}; got={x['seat_id'] for x in s}
assert got==declared, (sorted(declared-got), sorted(got-declared))
unknown_start=[x['seat_id'] for x in s if x.get('started') is None]
unknown_out=[x['seat_id'] for x in s if x.get('outcome') is None]
launched=None if unknown_start else sum(1 for x in s if x['started'])
completed=None if unknown_out else sum(1 for x in s if x['outcome']=='completed')
failed=None if unknown_out else sum(1 for x in s if x['outcome']=='failed')
print('rows=%d launched=%s completed=%s failed=%s unstarted=%d unknown_outcome=%d'%(
    len(s), launched, completed, failed,
    sum(1 for x in s if x.get('started') is False), len(unknown_out)))
if launched is not None and completed is not None and failed is not None:
    assert completed+failed==launched, (completed,failed,launched)
    print('INVARIANT-OK completed+failed==launched')
else:
    print('could-not-recover seats: started=%s outcome=%s' % (
        ','.join(unknown_start) or 'none', ','.join(unknown_out) or 'none'))
PY
# Any could-not-recover row goes into the records as null + owner + reason.

# 5. Deliverable census (corroboration only; NOT dispatch evidence).
python3 - <<'PY'
import json,os
t=json.load(open('reports/round-47/targets.json'))
rows=[]
for x in t['seats']:
    p=os.path.join('reports/round-47',x['out'])
    rows.append((x['id'],os.path.isfile(p),os.path.getsize(p) if os.path.isfile(p) else 0))
print('declared=%d present=%d nonempty=%d absent=%d'%(
    len(rows),sum(1 for r in rows if r[1]),sum(1 for r in rows if r[2]>0),
    sum(1 for r in rows if not r[1])))
print('absent:',','.join(r[0] for r in rows if not r[1]))
print('empty:',','.join(r[0] for r in rows if r[1] and r[2]==0))
PY

# 6. Close-time stamps and digests.
date -u +%Y-%m-%dT%H:%M:%SZ
sha256sum reports/round-47/telemetry/observed-dispatch.json \
          reports/round-47/telemetry/dispatch-declared.json \
          reports/round-47/validation.json
sha256sum reports/round-47/claims.json reports/round-47/targets.json
# claims/targets must still equal 7eb16979... / d60e5572...

# 7. File order: worker-observation (§6, if cited) -> observed-dispatch (§3)
#    -> availability-close-47 (§4). Replace every <FILL ...>.

# 8. Post-file invariant check (read-only).
python3 - <<'PY'
import json,hashlib
c=json.load(open('reports/round-47/telemetry/availability-close-47.json'))
assert c['closes_record']=='reports/round-47/telemetry/dispatch-declared.json'
assert c['closes_record_sha256_at_close']==hashlib.sha256(
    open(c['closes_record'],'rb').read()).hexdigest(), 'closed-record digest mismatch'
for row in c['also_closes']:
    assert row['sha256']==hashlib.sha256(open(row['path'],'rb').read()).hexdigest(), row['path']
assert c['open_fields']==[], c['open_fields']
r=c['validation_receipt']
assert r['sha256']==hashlib.sha256(open(r['path'],'rb').read()).hexdigest(), 'receipt digest mismatch'
o=json.load(open('reports/round-47/telemetry/observed-dispatch.json'))
assert o['state']!='open-at-seat-close', 'incomplete record'
assert 'FILL' not in json.dumps(c), 'unreplaced placeholder in close'
print('CLOSE-OK')
PY
```

Expected at observation: step 1 prints `BLOCKED`; step 2's digests match §1; step 3 cannot be completed until the native result is in hand; step 8 prints `CLOSE-OK` only after every placeholder is replaced and the digests re-check.

If the native result is unavailable at close: leave the three counters `null`, set their status to `could-not-recover` with the integrator as owner, keep `could_not_recover` listing them, and still close. The gap stays visible; the round is not admitted to `LOG.md` until the close file exists.

---

## 8. To-verify / open items (owner: integrator unless noted)

1. **Launch/completion/failure counts and error classes** — fill from the native batch summary or the redacted extract; null + `could-not-recover` if no extract exists.
2. **Observed wire model** — the native extract's provider response; the requested alias is not evidence of the route actually served.
3. **Runtime concurrency** — no measurement exists; stays null with owner + reason unless concurrent-session samples are filed.
4. **Key census** — declared only (`keys 1-2 live, 3-7 402`); no re-census this round.
5. **Interrupted attempts** — no `availability-attempt-47` record exists. If an interruption happened but was not recorded, file a new attempt row with its own provenance; do not reconstruct.
6. **Runner digest basis** — if `validation.json#/input_sha256` lacks `reports/round-47/run-validation.py`, record the computed `sha256sum` of the runner and say which basis was used.
7. **Final fragment sample** — the close's `fragments_present_md` must be measured at filing time, not copied from §6's draft-time samples.
8. **Close file naming** — `availability-close-47.json`; do not edit `dispatch-declared.json` or `observed-dispatch.json` after filing.

---

## 9. Negative proof

- Wrote only `reports/round-47/scribe/S02-telemetry-draft.md`; no file under `reports/round-47/telemetry/` was created or edited by this seat.
- No `corpus/**`, `tools/**`, `README.md`, or `reports/round-1..46/**` byte touched; no file staged under `corpus/`.
- No `run-validation.py` executed; no git commit/push; no install; no network.
- All measurements came from read-only commands: `ls`, `cat`, `find`, `wc`, `stat`, `date`, `sha256sum`, `git rev-parse`, `git ls-files`, and `python3` readers over JSON/text. Every number in §1–§2 is reproducible from the named file or the command shown; unknown counters are marked null with an owner, not asserted.
