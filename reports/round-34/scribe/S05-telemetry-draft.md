- Seat: S05 | scribe | cross | date 2026-10-19 | baseline da68a6d

# S05 — round-34 telemetry: dispatch-declared companion shapes (observed record template + closing-snapshot skeleton)

Mission (`reports/round-34/targets.json` S05 seat object): "Telemetry draft:
dispatch-declared companion shapes (observed record template, closing-snapshot skeleton)
per the round-33 convention." Out path: `reports/round-34/scribe/S05-telemetry-draft.md`.

**This fragment drafts bytes for the integrator; it is not a measurement of the round-34
wave.** No file under `reports/round-34/telemetry/` was written or modified by this seat
(out-path constraint); every JSON block below is text for the integrator to lift.

What changed versus the round-33 S05 draft (`reports/round-33/scribe/S05-telemetry-draft.md`):
round 33's companion shapes are now **filed bytes**, so the templates below are anchored to
what the round-33 runner actually accepted and what round 33 actually filed
(`reports/round-33/telemetry/observed-dispatch.json`,
`reports/round-33/telemetry/availability-close-33.json`), not to the round-33 draft's
proposed nesting. Where the draft and the filed record differ, the filed record wins — the
file-naming and schema questions the round-33 draft spent §3/F2 on are settled by landed
bytes and are not re-litigated here.

## 1. Declaration facts measured by S05 (durable sources)

Command (the `counting_command` filed in the declaration record,
`reports/round-34/telemetry/dispatch-declared.json:15`, extended with `stat`):

```sh
date -u +%FT%TZ; sha256sum reports/round-34/claims.json reports/round-34/targets.json reports/round-34/telemetry/dispatch-declared.json; git rev-parse HEAD
```

Read at 2026-10-19T07:01:07Z, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

| path | bytes | sha256 | mtime (UTC) |
|---|---|---|---|
| `reports/round-34/claims.json` | 6696 | `f2b87ddb37d8def04c6479a4ac6831ebf5c07514f91efe453247b84a0f9fcff0` | 2026-10-19T06:55:43Z |
| `reports/round-34/targets.json` | 17948 | `76d9652497c9b50ff484238e812c0597195db752786913cb7a6201b4b19eea1d` | 2026-10-19T06:57:15Z |
| `reports/round-34/telemetry/dispatch-declared.json` | 1626 | `53e2bb01071a3f97ae015ed7259d6539c5e281fc6a2a2699ff7168d7837dff44` | 2026-10-19T06:57:48Z |

`git rev-parse HEAD` = `da68a6d705e41f369f21e8607bfaab5b54077f84` — equal to the
`baseline_commit` declared at `reports/round-34/claims.json:8` (`da68a6d`) and
`dispatch-declared.json:17`. mtimes are `stat -c %y` values converted from the host's
`-0300` offset to UTC (`03:55:43 -0300` → `06:55:43Z`).

**Digest cross-check: PASS.** The two declaration digests equal those filed in
`dispatch-declared.json:21` (`f2b87ddb…`) and `:25` (`76d96524…`), so the filed declaration is
bound to the same claims/targets bytes S05 read (measured 2026-10-19T07:01:07Z). Re-verified
2026-10-19T07:06Z: both digests unchanged.

**Third digest (F3):** `dispatch-declared.json` is itself pinned by no record yet; S05's
measurement is `53e2bb01071a3f97ae015ed7259d6539c5e281fc6a2a2699ff7168d7837dff44`
(1626 bytes). Template B (below) uses it as `closes_sha256`.

Round-33's identical check passed the same way (`reports/round-33/scribe/S05-telemetry-draft.md:33-36`);
that fragment's numbers are now historical and are not reused for round 34.

## 2. Composition reproduction and the counter it falsifies

Command (re-runnable; window-free):

```sh
python3 -B -c "import json; t=json.load(open('reports/round-34/targets.json')); s=t['seats']; ids=[x['id'] for x in s]; g=lambda p: sum(1 for i in ids if p(i)); c={'scouts':g(lambda i:i.startswith('K')),'planners':g(lambda i:i.startswith('P')),'connector':g(lambda i:i=='X00'),'D-executors':g(lambda i:i.startswith('D') and int(i[1:])<=16),'D-verifiers':g(lambda i:i.startswith('D') and int(i[1:])>=17),'O-executors':g(lambda i:i.startswith('O') and int(i[1:])<=6),'O-verifiers':g(lambda i:i.startswith('O') and 7<=int(i[1:])<=9),'O-scribes':g(lambda i:i.startswith('O') and int(i[1:])==10),'C-executors':g(lambda i:i.startswith('C') and int(i[1:])<=6),'C-verifiers':g(lambda i:i.startswith('C') and 7<=int(i[1:])<=8),'C-scribes':g(lambda i:i.startswith('C') and int(i[1:])==9),'reviewers':g(lambda i:i.startswith('R')),'critics':g(lambda i:i.startswith('X') and i!='X00'),'scribes':g(lambda i:i.startswith('S'))}; print(c); print('sum', sum(c.values())); print('seat_count', t['seat_count'], 'seats', len(s), 'ids_unique', len(set(ids)), 'out_unique', len({x['out'] for x in s}))"
```

Observed output (2026-10-19T07:01Z):

```
{'scouts': 4, 'planners': 2, 'connector': 1, 'D-executors': 16, 'D-verifiers': 4,
 'O-executors': 6, 'O-verifiers': 3, 'O-scribes': 1, 'C-executors': 6, 'C-verifiers': 2,
 'C-scribes': 1, 'reviewers': 8, 'critics': 4, 'scribes': 5}
sum 63
seat_count 64 seats 63 ids_unique 63 out_unique 63
```

The census **reproduces the declared composition string byte-for-byte in content**:
`dispatch-declared.json:13` ("4 scouts, 2 planners, 1 connector, 16 D-executors, 4 D-verifiers,
10 O-seats (6 executors, 3 verifiers, 1 scribe), 9 C-seats (6 executors, 2 verifiers, 1
scribe), 8 reviewers, 4 critics, 5 scribes") is exactly the seat list's group counts.

**F1 — the declared worker count and the enumerable seat list disagree by one.** The
composition string sums to **63**; the seat array holds **63** entries
(`targets.json:13` `"seats": [` with 63 objects, `ids_unique 63`, `out_unique 63`); but
`requested_workers` is **64** (`dispatch-declared.json:11`, `claims.json:13`) and
`seat_count` is **64** (`targets.json:3`). Round 33 had no such gap: S05's identical census
there returned `sum 64`, `seat_count 64 seats 64 ids_unique 64 out_unique 64`
(`reports/round-33/scribe/S05-telemetry-draft.md:44-46`).

Consequences binding the observed record (Template A):
- `launched_workers` may **only** be filled from the native batch result. It must not be set
  to 64 because 64 was requested, and it must not be set to 63 because 63 were enumerable —
  either value needs its own basis string naming the artifact it was read from.
- If the native result says `completed: 64`, the record must also state the reconciliation:
  64 requested/returned vs 63 enumerable seat objects, and name which artifact holds the
  64th. If no artifact names it, the honest filing is the delta plus a `to-verify` owner —
  not a silent 64.
- `targets.json:3` vs the 63-element array is a **declaration defect in an
  orchestrator-authored file** (`targets.json` is not a seat out-path; S05 does not edit it).
  Route: integrator/orchestrator corrects the count field in a later round's targets, or
  records the 64th seat's identity; this fragment only measures it.
- The round-34 runner's telemetry leg should assert the census equals the composition string
  (both are 63 here) and separately report `requested_workers` (64) — a leg that hardcoded
  "64 = seats" would fail on round 34's own inputs.

## 3. Template A — observed-dispatch record → `reports/round-34/telemetry/observed-dispatch.json`

Lift the round-33 **filed** shape (`reports/round-33/telemetry/observed-dispatch.json`,
sha256 `89985f43e9ce277e03d6cc760571dc2977dff6995ebed1ca67f04fd9be148ded`) and substitute
round-34 values. Keys marked `[X3]` are what the round-33 runner's telemetry leg reads and
validates (`reports/round-33/run-validation.py:1055-1110`): `state` must equal
`open-at-seat-close`, `owner` and `reason` must be non-empty, `round` must equal the round,
and each of `launched_workers` / `completed_workers` / `failed_workers` that is `null` needs
an owner (`f"{field}_owner"` or the record-level `owner`).

```json
{
  "record": "observed-dispatch",
  "round": 34,
  "state": "open-at-seat-close",
  "owner": "orchestrator (goal-mode parent)",
  "reason": "counters are filled from the batched-dispatch result; the record closes when reports/round-34/telemetry/availability-close-34.json lands in the same integrating pass (AGENTS.md close-what-you-open)",
  "observed_window_utc": "<dispatch-call instant>/<batch-return instant, both from date -u +%FT%TZ>",
  "window_basis": "the single batched AgentSwarm dispatch call measured <N> s from the <HH:MM:SSZ> declaration stamp to the batch result",
  "counting_command": "AgentSwarm result summary and per-seat outcome attribute; date -u +%FT%TZ at declaration and close",
  "counting_date": "2026-10-19",
  "requested_allocation": {
    "provider_lane": "opencode-go-2",
    "model": "deepseek-v4.1-flash",
    "lane_key": "opencode-go key 2 (second of the per-round round-robin)",
    "requested_workers": 64,
    "batched_calls": 1
  },
  "launched_workers": null,
  "launched_workers_basis": "<the native result artifact this count was read from; see F1 before filling 64>",
  "completed_workers": null,
  "completed_workers_basis": "<same artifact; per-seat outcome attribute>",
  "failed_workers": null,
  "failed_workers_basis": "<same artifact; zero-failure statement needs the same basis as the positive counts>",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "orchestrator",
  "runtime_concurrency_reason": "seat-level launch telemetry is not observable from the parent; AgentSwarm queues launches automatically. Unknown counters stay null per AGENTS.md, not inferred.",
  "actual_route": "opencode-go lane, wire model deepseek-v4.1-flash, lane key 2",
  "seat_list_reconciliation": "requested_workers 64 (dispatch-declared.json:11); enumerable seat objects 63 (targets.json seats array); see F1",
  "post_batch_integration": "<integrator-only seats and in-session acts, per the operator concurrency directive; round-33 precedent: observed-dispatch.json:27 — integration acts are NOT additional craft batches>",
  "durable_sources": [
    {"path": "reports/round-34/claims.json", "sha256": "f2b87ddb37d8def04c6479a4ac6831ebf5c07514f91efe453247b84a0f9fcff0"},
    {"path": "reports/round-34/targets.json", "sha256": "76d9652497c9b50ff484238e812c0597195db752786913cb7a6201b4b19eea1d"},
    {"path": "reports/round-34/telemetry/dispatch-declared.json", "sha256": "53e2bb01071a3f97ae015ed7259d6539c5e281fc6a2a2699ff7168d7837dff44"},
    {"path": "reports/round-34/telemetry/inputs/claims.json", "sha256": "<must equal the claims.json digest above>"},
    {"path": "reports/round-34/telemetry/inputs/targets.json", "sha256": "<must equal the targets.json digest above>"}
  ],
  "limits": [
    "Requested allocation and requested model are declarations, not execution evidence.",
    "Null counters are unavailable, not zero; no completion rate is inferred.",
    "Provider liveness is not round acceptance.",
    "A correction is a new snapshot with its own provenance, never an in-place edit of this record."
  ]
}
```

Round-34 deltas versus the round-33 filed record, and why:
- `seat_list_reconciliation` is **new** (F1). The round-33 record needed no such key because
  its list and its count agreed.
- `completed_workers_basis` and `failed_workers_basis` are **new**: round 33 filed only
  `launched_workers_basis` (`observed-dispatch.json:21`) and a prose `failed_workers_note`
  (`:22`). Each of the three counts gets its own basis string so the trio is reproducible
  from the record alone, which is the AGENTS.md bar ("the redacted raw samples or native
  dispatch/result extracts needed to reproduce every reported count").
- All other keys keep the filed round-33 names. Round-33's draft had nested
  `allocation`/`observed` objects (`reports/round-33/scribe/S05-telemetry-draft.md:77-96`);
  the filed and runner-accepted shape is flat `requested_allocation` + top-level counters, and
  that is what is templated here.
- `observed_worker_sessions_lower_bound`, `wall_seconds`, `http_attempts`, `completion_rate`,
  `served_model` from the round-33 draft were all dropped by round 33's filed record. Do not
  add them back: the lower bound belongs in the worker-observation record (§5), and the rest
  are unavailable.

Fill rules:
- `observed.*` counts may be filled **only** from a native dispatch/result extract the owner
  holds. File that extract under `reports/round-34/telemetry/` as well; if none exists, the
  leg-compatible honest filing is `state: open-at-seat-close` with the counters `null`, the
  owner, and a reason (round-30/31/32 `could-not-evaluate` precedent:
  `reports/round-32/telemetry/dispatch-stats.json`).
- No credentials, authorization headers, or private prompt payloads anywhere
  (`AGENTS.md:29-31`).
- Never let a `durable_sources` entry point at `.scratch/` (non-durable; `.gitignore:6`).

## 4. Template B — closing-snapshot skeleton → `reports/round-34/telemetry/availability-close-34.json`

Name authority (settled by filed bytes, not re-opened here): six snapshots exist, all
`availability-close-<N>.json` (`find reports -name "availability-close*.json"` →
`{19,25,26,27,28,33}`), zero `closing-snapshot.json` (`find reports -name
"closing-snapshot*.json"` → empty, 2026-10-19T07:03Z). The SKILL.md instrument now agrees:
`SKILL.md:732` globs `telemetry/availability-close-*.json` and keys the check on
`closes` + `closes_sha256` — the round-33 F2 amendment landed (SKILL.md is now 732 lines,
digest `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`).

```json
{
  "schema": "kotodama-availability-closing-snapshot-v1",
  "round": 34,
  "date": "<date reports/round-34/validation.json lands>",
  "closes": "reports/round-34/telemetry/dispatch-declared.json",
  "closes_sha256": "53e2bb01071a3f97ae015ed7259d6539c5e281fc6a2a2699ff7168d7837dff44",
  "closed_fields": {
    "observed_launches": "<int|null> (read from reports/round-34/telemetry/observed-dispatch.json launched_workers, basis: <artifact>)",
    "observed_completions": "<int|null> (observed-dispatch.json completed_workers)",
    "observed_failures": "<int|null> (observed-dispatch.json failed_workers)",
    "observed_window_utc": "<start/end> (observed-dispatch.json observed_window_utc)",
    "actual_route": "opencode-go lane key 2, wire model deepseek-v4.1-flash (observed-dispatch.json actual_route)",
    "runtime_concurrency": "could-not-recover as a measured counter: null with owner orchestrator and reason recorded in observed-dispatch.json (AGENTS.md: unknown counters stay null, not inferred)",
    "seat_list_reconciliation": "requested_workers 64 vs 63 enumerable seat objects (F1); <identity of the 64th slot or to-verify with owner>"
  },
  "could_not_recover": [
    "runtime_concurrency: seat-level launch telemetry is not observable from the parent process"
  ],
  "owner": "integrator (goal-mode parent), for the lane",
  "reason": "closing snapshot filed once reports/round-34/validation.json landed; every field the declaration left open is filled above, each citing the durable artifact it was read from",
  "sources": [
    "reports/round-34/telemetry/dispatch-declared.json",
    "reports/round-34/telemetry/observed-dispatch.json",
    "reports/round-34/validation.json"
  ],
  "also_closes": [
    {"path": "reports/round-34/telemetry/observed-dispatch.json", "sha256": "<digest at close time>"}
  ],
  "append_only_note": "the closed record's bytes are unchanged; this snapshot is the correction surface"
}
```

Carried from round 33 (`reports/round-33/telemetry/availability-close-33.json:2-6,:7-14,:18-20`):
the schema string, `closes` on the **declaration** record, `closes_sha256` equal to its live
digest, a flat `closed_fields` map whose values carry their basis inline, and
`could_not_recover` as a list. The round-33 draft's nested
`{"value","basis","command","date"}` shape (`reports/round-33/scribe/S05-telemetry-draft.md:154-158`)
was not filed; do not reintroduce it now that the flat shape has six precedents.

Two deltas, both optional-but-recommended:

1. **`also_closes` (new, F5).** Round 33's snapshot pins the declaration only; the observed
   record's `state: open-at-seat-close` is closed by prose alone and its bytes are pinned
   nowhere, so an edit after close would be undetectable. Adding a digest for the observed
   record fixes that without breaking the r33-accepted leg: that leg reads the snapshot with
   `.get` on `schema`, `round`, `date`, `closes`, `closes_sha256`
   (`reports/round-33/run-validation.py:1093-1101`) and ignores extra keys. Verified shape
   tolerance is a claim about the round-33 leg, which is a filed read-only artifact; round
   34's own runner is not authored yet, so the integrator must re-confirm tolerance there.
   If the integrator prefers byte-minimality, drop `also_closes` and instead make the round-34
   observed record's `reason` name the snapshot that closes it — as round 33's does
   (`observed-dispatch.json:6`) — and record the residual as carried.
2. **`seat_list_reconciliation` inside `closed_fields` (F1).** The declaration's
   `requested_workers: 64` is one of the open fields this snapshot closes; closing it with
   `64` alone would paper over the 63-object list.

`closes_sha256` is the digest of the declaration **at close time**. If the integrator must
edit `dispatch-declared.json` after this fragment, the snapshot pins the post-edit digest and
says so; the rule prefers no edit (`AGENTS.md` corrections-are-new-snapshots).
A round is not admitted to `LOG.md` while this snapshot is owed.

## 5. Template C — worker self-observation (lower bound only)

S05's own sample, filed here as text because a seat cannot write into `telemetry/`:

```json
{
  "round": 34,
  "owner": "S05",
  "observed_at_utc": "2026-10-19T07:05:15Z",
  "evidence_kind": "worker-self-observation",
  "source": "S05 received the round-34 telemetry-scribe assignment (cross claim) and is executing it; UTC observation time from date -u +'%Y-%m-%dT%H:%M:%SZ'. No native full-wave result was supplied to this worker.",
  "sessions": [{"assignment": "S05", "state_at_observation": "active"}],
  "counts_date": "2026-10-19",
  "counting_command": "<the scratch-marker census one-liner in this section, t0 = 2026-10-19T06:57:28Z>",
  "peer_marker_census": {
    "window_utc": {"start": "2026-10-19T06:57:28Z", "end": "2026-10-19T07:05:15Z", "closed": true},
    "markers": 42,
    "seat_labels": ["c05", "c07", "c08", "c09", "d03", "d12", "k04", "o03", "r04", "r05", "s02", "x02"],
    "unattributed": ["assemble", "outside (outside-secret.txt)", "receipt", "round (round-34-O07)"],
    "interpretation": "lower bound on concurrently active seats; not a census, not a completion count"
  },
  "scope": "One worker self-observation plus a scratch-marker lower bound; neither an independent worker census nor evidence of the actual upstream model, full-wave launch/completion count, concurrency, wall time or HTTP traffic.",
  "unavailable_owner": "Round-34 orchestrator (native dispatch/result holder)",
  "unavailable_reason": "The worker-visible round-34 claims and targets declare requests, not native execution outcomes. Full-wave dispatch metadata is not available in this worker's assigned inputs. File a new snapshot with redacted native dispatch/result extracts; do not replace this partial observation."
}
```

Census command and observed output (run by S05, window anchored at the declaration stamp
`dispatch-declared.json:5` = 2026-10-19T06:57:28Z):

```sh
python3 -B -c "import pathlib,datetime,re; t0=datetime.datetime(2026,10,19,6,57,28,tzinfo=datetime.timezone.utc).timestamp(); rows=[(datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),p.name) for p in pathlib.Path('.scratch').iterdir() if p.stat().st_mtime>=t0]; print(len(rows)); print(sorted(rows)); print(sorted({re.match(r'^([A-Za-z0-9]+?)-',n).group(1).lower() for _,n in rows if re.match(r'^([A-Za-z0-9]+?)-',n)}))"
```

- 2026-10-19T07:02:51Z → `27` markers; labels `['c07','c08','d12','k04','o03','outside','r04','r05','round','s02','x02']`; sample names `K04-named.tsv`, `d08`, `D12-freeze`, `o03-census.py`, `r05-census.json`, `x02-census.json`, `s02-census.py`.
- 2026-10-19T07:05:15Z (same start boundary) → `42` markers; labels add `c05`, `c09`, `d03`, `assemble`, `receipt`.

The count **grows** with the same window anchor — the round-33 draft recorded the same
behaviour (`reports/round-33/scribe/S05-telemetry-draft.md:241-244`). Only the value at the
instant printed with it is meaningful; never re-quote a later count as the observation above.
`.scratch/` is gitignored (`.gitignore:6`), so this census is **not** a durable evidence
surface and must never be promoted into `launched_workers` / `completed_workers`.

## 6. Round-30 durability convention — what binds round 34

- Records live under `reports/round-34/telemetry/`, never only `.scratch` (`AGENTS.md`).
- Requested allocation stays separate from observed launches/completions/failures/route.
- Nulls stay null with an owner and reason; no inferred zeroes, no completion rate.
- Corrections are new append-only snapshots; filed rounds are never rewritten.
- No credentials/headers/private prompts in telemetry.
- Captures print to stdout; never redirect a fresh capture over a filed snapshot
  (`reports/round-30/fixes/telemetry-convention.md:29-31`).
- Durability is not acceptance; provider liveness ≠ round acceptance.
- **F4 — the durable `inputs/` copies are owed.** `reports/round-34/telemetry/inputs/` does
  not exist (`ls` → No such file or directory, 2026-10-19T07:0xZ). Round 33's copies are
  byte-exact and digest-equal to their sources: `cmp reports/round-33/claims.json
  reports/round-33/telemetry/inputs/claims.json` → exit 0, `cmp … targets.json …` → exit 0,
  and both copies carry the source digests (`ba69090f…`, `342c8f80…`). Same method applies:
  copy `reports/round-34/claims.json` and `targets.json` byte-exact and re-run `cmp`
  (watch the trailing-newline trap recorded at
  `reports/round-30/fixes/telemetry-convention.md:34` — both round-34 sources end in `0x0a`,
  verified with `tail -c 1 | xxd -p`).
- Committability check (run 2026-10-19T07:03Z): `git check-ignore -v` produced **no match**
  for `reports/round-34/telemetry/{dispatch-declared,observed-dispatch,availability-close-34}.json`;
  `.scratch/` matched `.gitignore:6`. `git status --porcelain` shows `?? reports/round-34/`
  (untracked, as expected pre-commit).

## 7. Findings for the integrator

- **F1 — 64 requested vs 63 enumerable seats (§2).** Highest-priority item in this fragment.
  The observed record and the closing snapshot both owe the reconciliation; the
  orchestrator-authored `targets.json:3` count field is the likely defect site and is not a
  seat out-path.
- **F2 — the round-34 open record is invisible to the landed closure audit.** `SKILL.md:732`
  globs `reports/round-*/availability*.json`; round 34's open-state record lives at
  `reports/round-34/telemetry/observed-dispatch.json`, which that glob cannot match (and
  round 33 filed no `reports/round-33/availability.json` — `find reports -name
  "availability*.json"` returns the r10/r5 attempt files, r19/r25–r28 `availability.json`,
  and the six `telemetry/availability-close-*.json`). Run verbatim at 2026-10-19T07:03Z the
  audit printed **nothing** (exit 0). So the binding instrument for round 34 is the runner's
  own telemetry leg (round-33 `X3`, `reports/round-33/run-validation.py:1055-1110`), not the
  audit. **Do not create a decoy `reports/round-34/availability.json`**: if it carried
  `state: open-at-seat-close` while the snapshot's `closes` pointed at
  `dispatch-declared.json`, the audit would print it as a false positive; the round-30
  `duplicate_evidence` control is the second reason to file one record, not two.
- **F3 — declaration digest pin available now.** `53e2bb01071a3f97ae015ed7259d6539c5e281fc6a2a2699ff7168d7837dff44`
  (1626 bytes, S05 measurement 2026-10-19T07:01:07Z). Template B pins it.
- **F4 — `inputs/` copies owed (§6).**
- **F5 — the observed record's own bytes are unpinned by the round-33 convention.**
  `reports/round-33/telemetry/availability-close-33.json:5-6` pins the declaration; nothing
  pins `reports/round-33/telemetry/observed-dispatch.json` (sha256
  `89985f43e9ce277e03d6cc760571dc2977dff6995ebed1ca67f04fd9be148ded`, S05 measurement
  2026-10-19T07:03Z). Template B's `also_closes` closes that gap for round 34; the round-33
  gap itself is filed bytes and is not repaired in place — if the operator wants it pinned,
  it is a new supersession row (owner: a future round), not an edit.
- **F6 — lower bound only (§5).** Never promote the scratch census.
- **F7 — no fleet report for round 34 yet.** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-34/`
  → No such file or directory (2026-10-19T07:02Z). The `.ufo/reports/round-34/kotodama.md`
  round report is owed at close and is the parent's artifact; it is an input to the closing
  pass, not to this draft.
- **F8 — the declaration record was stamped after the claims declaration.** `claims.json:6`
  `declared_at_utc` 2026-10-19T06:35:00Z vs `dispatch-declared.json:5` 2026-10-19T06:57:28Z
  (22.5 min apart). Not a defect (the declaration record is filed at dispatch time), but the
  observed window must be anchored on the **dispatch** stamp, not the claims stamp.
- **F9 — F-C13-1 context for the telemetry record.** `dispatch-declared.json:28` carries the
  standing rule "no in-tree execution of any filed round runner (F-C13-1 prevention)"; the
  incident and prevention are on record at `LOG.md` (round-33 F-C13-1 entry, `:3548-3562`).
  The telemetry record should not be extended to carry a runner-adoption verdict — that is
  claim O's instrument this round (`targets.json` O-seats), and duplicating it risks the
  `duplicate_evidence` control.

## 8. Counting commands and controls for the round-34 runner (draft leg)

The round-34 runner does not exist yet (`test -f reports/round-34/run-validation.py` → NO,
2026-10-19T07:04Z) and `reports/round-34/validation.json` does not exist either, so the
closing snapshot is owed. Draft leg, mirroring round-33 `X3`
(`reports/round-33/run-validation.py:1055-1110`) with round-34 numbers:

Positive checks:
1. `sha256sum reports/round-34/claims.json reports/round-34/targets.json` equals the digests
   at `dispatch-declared.json:21,:25` (`f2b87ddb…`, `76d96524…`) and in the observed record's
   `durable_sources`.
2. `sha256sum reports/round-34/telemetry/dispatch-declared.json` equals the snapshot's
   `closes_sha256`; `closes` resolves to that same path.
3. `cmp reports/round-34/claims.json reports/round-34/telemetry/inputs/claims.json` and the
   targets pair → exit 0 (round-30 control).
4. §2 composition census reproduces `dispatch-declared.json:13`'s string; **and** the leg
   separately reports `requested_workers` 64 vs 63 enumerated (F1) instead of asserting
   equality.
5. Observed record: `round == 34`, `state == "open-at-seat-close"`, non-empty `owner` and
   `reason`; every null counter has an owner (r33 leg semantics).
6. Snapshot: `schema == "kotodama-availability-closing-snapshot-v1"`, `round == 34`, `date`
   matches `YYYY-MM-DD`, `closes`/`closes_sha256` pin the declaration.
7. `git check-ignore -v` on the three telemetry paths → no match.
8. `test -s reports/round-34/telemetry/availability-close-34.json` once
   `reports/round-34/validation.json` lands.

Negative controls to reject (names follow the round-30 control set):
`null_to_zero`, `invented_completion_count` (this round: filling 64 with no native extract),
`requested_as_completed` (completion_rate derived from declarations),
`invented_served_model`, `full_wave_pass_without_extract`,
`scratch_only_dependency`, `scratch_evidence_path`, `raw_evidence_tamper`,
`duplicate_evidence`, `missing_counting_command` / `missing_counts_date`,
`closing_snapshot_digest_mismatch`, `historical_recovery_overclaim`, plus one round-34
addition: **`count_field_over_seat_list`** — a record asserting `launched_workers: 64` while
the enumerable seat list has 63 and no artifact names the 64th.

## Owed

- `reports/round-34/telemetry/observed-dispatch.json` — integrator lands from Template A
  (S05 may write only its own out path). Not present at 2026-10-19T07:04Z.
- `reports/round-34/telemetry/inputs/{claims,targets}.json` — byte-exact durable copies +
  `cmp` control (F4).
- `reports/round-34/telemetry/availability-close-34.json` — owed once
  `reports/round-34/validation.json` lands (Template B); the round is not admissible to
  `LOG.md` while it is owed.
- The round-34 runner's telemetry leg (§8 draft spec) — owner: whichever seat/integrator
  authors `reports/round-34/run-validation.py`; the round-33 leg it mirrors is filed and
  read-only.
- F1 seat-list reconciliation (64 vs 63) — owner: orchestrator/integrator, in the observed
  record and the closing snapshot; `targets.json:3` is not a seat out-path and is not edited
  by S05.
- F5 decision: file Template B with `also_closes`, or drop it and carry the residual with the
  round-34 observed `reason`.
- F7 fleet report `.ufo/reports/round-34/kotodama.md` — parent's artifact, owed at close.
- `to-verify`: whether the round-34 orchestrator holds a native dispatch/result extract.
  S05 cannot see one and no fleet round-34 dir exists (F7); the counters in Template A stay
  `null` until such an artifact exists.

## Citations

- `reports/round-34/targets.json:3` (`seat_count: 64`), `:13` (`seats` array, 63 objects,
  `ids_unique 63`, `out_unique 63`), S05 seat object (`out: scribe/S05-telemetry-draft.md`),
  `shared_rules` array.
- `reports/round-34/claims.json:6,:8,:11,:13,:17` — declared_at_utc, baseline_commit,
  provider lane, requested_workers 64, axes.
- `reports/round-34/telemetry/dispatch-declared.json:5,:7-13,:15-17,:18-27,:28,:29` —
  declaration stamp, allocation + composition string, counting command, baseline commit,
  durable sources + digests, standing rules, `open-at-seat-close` note.
- `REGIMEN.md` — round-34 schedule row (build 2 of 3, opencode-go round-robin), per-round
  contract, record set, admission rule.
- `AGENTS.md` — availability/dispatch telemetry rules, "Close what you open", null-stays-null,
  no-credentials, append-only corrections.
- `reports/round-33/telemetry/observed-dispatch.json` (filed shape, sha256 `89985f43…`):
  `:2-6,:7-10,:11-19,:20-27,:28-49`.
- `reports/round-33/telemetry/availability-close-33.json:2-6,:7-14,:15-17,:18-20` — filed
  closing-snapshot shape.
- `reports/round-33/run-validation.py:31-33,:60,:1055-1110,:1264-1268` — telemetry leg
  constants, closing schema string, `check_telemetry` semantics (state/owner/reason; null
  owners; schema/round/date; `closes`/`closes_sha256` = declaration digest).
- `reports/round-33/scribe/S05-telemetry-draft.md:33-36,:44-46,:77-96,:154-158,:241-244` —
  round-33 digest cross-check, composition census result, the not-filed nested shapes, and
  the census-growth caveat.
- `reports/round-33/validation.json` (`acceptance_checks_passed: true`, `baseline_revision`
  `139e3b6…`) — round-33 acceptance state; `LOG.md:3519-3545` — round-33 admission entry
  (observed 64/64; closure recorded) and `:3548-3562` — F-C13-1 incident + prevention.
- `SKILL.md:732` — the re-keyed close-what-you-open one-liner (globs
  `telemetry/availability-close-*.json`, keys on `closes` + `closes_sha256`);
  `sha256sum SKILL.md` = `f9bd07c2…`, 732 lines.
- `reports/round-30/fixes/telemetry-convention.md:29-34` — stdout-capture rule, byte-exact
  `inputs/` copies, trailing-newline trap; `reports/round-30/telemetry/control-receipt.json`
  — the negative-control name set.
- `reports/round-32/telemetry/dispatch-stats.json` — `could-not-evaluate` partial-observation
  precedent.
- `.gitignore:6` — `.scratch/` ignored.
- Commands run by S05 (lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all
  2026-10-19T07:01–07:06Z): `date -u +%FT%TZ`; `sha256sum` + `stat -c '%n %s bytes mtime=%y'`
  on the three round-34 declaration artifacts; `git rev-parse HEAD`;
  `sed -n '1,64p' reports/round-34/telemetry/dispatch-declared.json` (numbered read);
  the §2 composition one-liner; `find reports -name "availability-close*.json"` (6) and
  `find reports -name "closing-snapshot*.json"` (empty); `find reports -name
  "availability*.json"`; the verbatim `SKILL.md:732` audit one-liner (no output, exit 0);
  `cmp` on round-33's `telemetry/inputs/` pairs (both exit 0); `tail -c 1 | xxd -p` on
  round-34 claims/targets (both `0a`); `git check-ignore -v` on the three telemetry paths and
  `.scratch/`; `git status --porcelain` (`?? reports/round-34/`); the §5 scratch census
  one-liner twice (27 then 42 markers); `grep -n "closing-snapshot\|availability-close"
  SKILL.md` (`:732`); `ls` of `/home/vgpnk/Projects/shokunin/.ufo/reports/round-34/`
  (No such file or directory).
