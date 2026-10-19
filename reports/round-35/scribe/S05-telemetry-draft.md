- Seat: S05 | scribe | cross | date 2026-10-19 | baseline 4a7aede

# S05 — round-35 telemetry: observed record template + closing-snapshot skeleton + attempt ledger

Mission (`reports/round-35/targets.json` S05 seat object): "Telemetry draft per the
round-33/34 convention (observed record template, closing-snapshot skeleton, window
anchored on the declaration stamp)." Out path: `reports/round-35/scribe/S05-telemetry-draft.md`.

**This fragment drafts bytes for the integrator; it is not a measurement of the round-35
wave.** No file under `reports/round-35/telemetry/` was written or modified by this seat
(out-path constraint). Every JSON block below is text for the integrator to lift, per the
round-34 precedent (`reports/round-34/scribe/S05-telemetry-draft.md:9-11`).

Round-35 delta versus round 34, up front: round 35 is the first regimen-2 round with a
**pre-batch availability ledger** (three 402'd keys, `reports/round-35/telemetry/availability-attempt-{1,2,3}.json`)
and the first whose dispatch **route deviates from its declared lane** (declared
`opencode-go-3`, actual `opencode-go key 1`). The templates below carry both, because
`AGENTS.md` keeps requested allocation separate from observed route, and because a
`64/64`-style summary that folded 192 launch failures into a pass would be the exact
`requested_as_completed` / `full_wave_pass_without_extract` failure the round-30 control
set exists to reject (`reports/round-30/fixes/telemetry-convention.md:33-35`).

## 1. Declaration facts measured by S05 (durable sources)

Command (the `counting_command` filed at `reports/round-35/telemetry/dispatch-declared.json:15`,
extended with `stat`; the filed command's third clause is not runnable as written — see F2):

```sh
date -u +%FT%TZ; sha256sum reports/round-35/claims.json reports/round-35/targets.json \
  reports/round-35/telemetry/dispatch-declared.json \
  reports/round-35/telemetry/availability-attempt-{1,2,3}.json; \
stat -c '%n %s bytes mtime=%y' <same paths>; git rev-parse HEAD
```

Read at 2026-10-19T08:14:08Z, re-verified 2026-10-19T08:16:32Z (all six digests unchanged),
lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

| path | bytes | sha256 | mtime (UTC) |
|---|---|---|---|
| `reports/round-35/claims.json` | 6037 | `ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4` | 2026-10-19T08:03:57Z |
| `reports/round-35/targets.json` | 16379 | `56ad03927c7063a3616af2ed0e78ab7b1ca1f3ea43fdf67f2ecf60a7f1b63215` | 2026-10-19T08:06:16Z |
| `reports/round-35/telemetry/dispatch-declared.json` | 2003 | `93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83` | 2026-10-19T08:06:39Z |
| `reports/round-35/telemetry/availability-attempt-1.json` | 1172 | `b1a9791938664674d192381fefc2a5e37e86ba0c8178f7a034b116d17af50c62` | 2026-10-19T08:08:53Z |
| `reports/round-35/telemetry/availability-attempt-2.json` | 778 | `326675b9b0132265f89473dee031d952b302d720c6826ef0bcc6b4d00fb1ac86` | 2026-10-19T08:10:24Z |
| `reports/round-35/telemetry/availability-attempt-3.json` | 1323 | `667a86d498db3ec4c04b6a333a246af49dc685b4cc5164f3b9a5beb5fd770253` | 2026-10-19T08:12:26Z |

`git rev-parse HEAD` = `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` — equal to
`claims.json:8` (`4a7aede`) and `dispatch-declared.json:17` (full form). mtimes are
`stat -c %y` values converted from the host's `-0300` offset to UTC.

**Digest cross-check: PASS.** My measured claims digest equals `dispatch-declared.json:21`
(`ccfaafc3…`) and my targets digest equals `:25` (`56ad0392…`), so the filed declaration is
bound to the same bytes this seat read. `tail -c 1 | xxd -p` on both sources returns `0a`
(trailing-newline trap accounted for,
`reports/round-30/fixes/telemetry-convention.md:34`).

**Third digest:** `dispatch-declared.json` is pinned by no record yet; S05's measurement is
`93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83` (2003 bytes). Template B
uses it as `closes_sha256`.

## 2. Composition reproduction: the r34 F1 gap is closed; a new role sub-census defect is not

Command (re-runnable; window-free):

```sh
python3 -B -c "import json,collections; t=json.load(open('reports/round-35/targets.json')); s=t['seats']; ids=[x['id'] for x in s]; g=lambda p: sum(1 for i in ids if p(i)); c={'scouts':g(lambda i:i.startswith('K')),'planners':g(lambda i:i.startswith('P')),'connector':g(lambda i:i=='X00'),'C':g(lambda i:i.startswith('C')),'O':g(lambda i:i.startswith('O')),'A':g(lambda i:i.startswith('A')),'reviewers':g(lambda i:i.startswith('R')),'critics':g(lambda i:i.startswith('X') and i!='X00'),'scribes':g(lambda i:i.startswith('S'))}; print(c, 'sum', sum(c.values())); print('seat_count', t['seat_count'], 'seats', len(s), 'ids_unique', len(set(ids)), 'out_unique', len({x['out'] for x in s})); print('role census', dict(collections.Counter(x['role'] for x in s)))"
```

Observed output (2026-10-19T08:14Z):

```
{'scouts': 4, 'planners': 2, 'connector': 1, 'C': 17, 'O': 11, 'A': 11, 'reviewers': 9, 'critics': 4, 'scribes': 5} sum 64
seat_count 64 seats 64 ids_unique 64 out_unique 64
role census {'scout': 4, 'planner': 2, 'connector': 1, 'executor': 26, 'verifier': 8, 'scribe': 10, 'reviewer': 9, 'critic': 4}
```

**R34-F1 closed.** The top-level group census reproduces the declaration's groups exactly
and sums to 64: `dispatch-declared.json:13` reads "4 scouts, 2 planners, 1 connector, 17
C-seats (…), 11 O-seats, 11 A-seats, 9 reviewers, 4 critics, 5 scribes" → 4+2+1+17+11+11+9+4+5
= 64, and the seat array holds 64 rows (`seats 64`, `ids_unique 64`, `out_unique 64`).
`dispatch-declared.json:28` records why: "targets.json was first authored with 60 seats and
corrected to exactly 64 (adding C17/O11/A11/R09) before dispatch". The round-34 CO4
deviation (`reports/round-34/run-validation.py:122-126`) has **no round-35 analogue** —
`requested_workers` 64 (`claims.json:13`, `dispatch-declared.json:11`) now equals the
enumerable list, and the round-35 CO leg must assert equality rather than a deviation.

**F1-r35 — the composition string's role sub-census is unsupported by the seat list.** The
same line asserts "authors 10, verifiers 11 incl. C13/C14/C17/O05/O08/O11/A07/A11,
executors otherwise". The measured role census has **8** verifiers and **26** executors; the
eight verifier IDs named in the string are exactly the eight the seat list holds
(`C13, C14, C17, O05, O08, O11, A07, A11` — so "11" has no nine/ten/eleven behind it), and
"authors 10" is a partial label for a 26-member executor class (12 C + 6 O + 8 A executors).
The parenthetical C-breakdown ("10 authors, 3 auditors, 1 runbook, 2 scribes +1 README")
does sum to 17 and does match C01–C17 by out-path reading, so the defect is confined to the
role sub-census clause. Route: the round-35 runner's CO leg records the mismatch the way
round 34 recorded CO4 (measured, named, not edited); `dispatch-declared.json` and
`targets.json` are digest-pinned orchestrator-authored files and are not seat out-paths.

## 3. The pre-batch availability ledger and the route deviation

Round 35 is the first regimen-2 round whose dispatch did not run on its declared key.

| attempt | file | route | launched | completed | failed | failure_class |
|---|---|---|---|---|---|---|
| 1 | `availability-attempt-1.json` | `opencode-go-3` | 0 | 0 | 64 | 402 insufficient funds |
| 2 | `availability-attempt-2.json` | `opencode-go-4` | 0 | 0 | 64 | 402 insufficient funds |
| 3 | `availability-attempt-3.json` | `opencode-go-5` | 0 | 0 | 64 | 402 insufficient funds |

Each file states its own basis (`availability-attempt-1.json:12`: "all 64 dispatched seats
failed at launch with the identical 402 (agent-130..agent-193); zero seats started"), and
`availability-attempt-3.json:14` records the disposition that binds the observed record:
round 35 re-dispatches on **opencode-go key 1** — "the round-robin cannot advance past
unprovisioned keys; the reuse is a named deviation recorded here, in the observed-dispatch
record, and in the round's LOG/SCORECARD". `claims.json:11` and `dispatch-declared.json:8`
declare lane `opencode-go-3`; `REGIMEN.md:13` (schedule row 1–3) and `REGIMEN.md:66-69`
(provider-deviation clause) are the authorities for declaring rather than silently
substituting.

Binding consequences for Template A:

- `requested_allocation.provider_lane` stays `opencode-go-3` (the declaration);
  `actual_route` names key 1 and cites `availability-attempt-3.json:14`. Do not overwrite the
  declared lane with the actual one (`AGENTS.md`: requested allocation separate from actual
  route).
- The **192 launch failures** (3 × 64) are *not* `launched_workers` and *not*
  `failed_workers` for the observed batch: zero seats started in all three attempts. They
  belong in the attempt ledger the record carries by digest, with an explicit sentence that
  they are excluded from the batch counters.
- `key_census_so_far` (`availability-attempt-3.json:13`) reads "key 1 (r33): LIVE, 64/64 |
  key 2 (r34): LIVE, 63/63". The r33 figure matches `reports/round-33/validation.json`'s
  observed 64/64 admission (`LOG.md:3519-3545`); the r34 figure does **not** carry
  `reports/round-34/telemetry/observed-dispatch.json:19-21`'s `failed_workers: 1` (D17 never
  landed, recorded in `reports/round-34/validation.json` `missing_dependencies`). Both are
  filed bytes; the honest reading is "63 launched, 63 completed, 1 dispatched seat never
  landed", so F3 below routes the cross-file note rather than a correction.

## 4. Template A — observed-dispatch record → `reports/round-35/telemetry/observed-dispatch.json`

Lift the round-34 **filed** shape (`reports/round-34/telemetry/observed-dispatch.json`,
sha256 `57e0b2d95c207e6dd74f07c66b67bd55a37e7cb4caad3eb9c5ca999172b9d2fe`) and substitute
round-35 values. The round-34 runner's `leg_close` reads this file with `.get` on
`state`/`owner`/`reason`/`round` (`reports/round-34/run-validation.py:333-337`) and tolerates
extra keys; the round-35 leg should keep those four semantics and may add the checks in §8.

```json
{
  "record": "observed-dispatch",
  "round": 35,
  "state": "open-at-seat-close",
  "owner": "orchestrator (goal-mode parent)",
  "reason": "counters are filled from the batched-dispatch result; the record closes when reports/round-35/telemetry/availability-close-35.json lands in the same integrating pass (AGENTS.md close-what-you-open)",
  "observed_window_utc": "<batch-dispatch instant>/<batch-return instant, both from date -u +%FT%TZ>",
  "window_basis": "the single batched AgentSwarm dispatch call that ran on opencode-go key 1, measured <N> s from <HH:MM:SSZ> to the batch result; the three 402 attempts below precede it and are excluded from the window",
  "counting_command": "AgentSwarm result summary '<summary>completed: N</summary>' and per-seat outcome attribute; date -u +%FT%TZ at declaration and close",
  "counting_date": "2026-10-19",
  "requested_allocation": {
    "provider_lane": "opencode-go-3",
    "model": "deepseek-v4.1-flash",
    "lane_key": "opencode-go key 3 (third of the per-round round-robin) — declared, not used",
    "requested_workers": 64,
    "batched_calls": 1,
    "declared_note": "declared per reports/round-35/claims.json:11 and telemetry/dispatch-declared.json:8; the batch actually ran on key 1 (route_deviation below)"
  },
  "route_deviation": {
    "declared_lane": "opencode-go-3",
    "actual_lane": "opencode-go key 1",
    "basis": "reports/round-35/telemetry/availability-attempt-3.json:14 — keys 3/4/5 returned 402 insufficient funds; the round-robin cannot advance past unprovisioned keys and the reuse is a named deviation",
    "authority": "REGIMEN.md:66-69 (provider deviations permitted only as declared) and REGIMEN.md:13 (round-robin across live keys)"
  },
  "pre_batch_availability_ledger": {
    "attempts": 3,
    "seats_failed_at_launch": 192,
    "seats_started": 0,
    "excluded_from_batch_counters": "true — zero seats started in attempts 1-3; the 192 launch failures are launch-availability evidence, not batch outcomes",
    "files": [
      {"path": "reports/round-35/telemetry/availability-attempt-1.json", "sha256": "b1a9791938664674d192381fefc2a5e37e86ba0c8178f7a034b116d17af50c62", "route": "opencode-go-3", "failure_class": "402 Upstream request failed: Insufficient account funds"},
      {"path": "reports/round-35/telemetry/availability-attempt-2.json", "sha256": "326675b9b0132265f89473dee031d952b302d720c6826ef0bcc6b4d00fb1ac86", "route": "opencode-go-4", "failure_class": "402 Upstream request failed: Insufficient account funds"},
      {"path": "reports/round-35/telemetry/availability-attempt-3.json", "sha256": "667a86d498db3ec4c04b6a333a246af49dc685b4cc5164f3b9a5beb5fd770253", "route": "opencode-go-5", "failure_class": "402 Upstream request failed: Insufficient account funds"}
    ]
  },
  "launched_workers": null,
  "launched_workers_basis": "<the native result artifact this count was read from; 64 is the requested and the enumerable count — do not fill it from either>",
  "completed_workers": null,
  "completed_workers_basis": "<same artifact; per-seat outcome attribute>",
  "failed_workers": null,
  "failed_workers_basis": "<same artifact; a zero-failure statement needs the same basis as the positive counts>",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "orchestrator",
  "runtime_concurrency_reason": "seat-level launch telemetry is not observable from the parent; AgentSwarm queues launches automatically. Unknown counters stay null per AGENTS.md, not inferred.",
  "actual_route": "opencode-go lane, wire model deepseek-v4.1-flash, lane key 1 (fallback after attempts 1-3)",
  "seat_list_reconciliation": "requested_workers 64 (dispatch-declared.json:11) equals the enumerable seat list (targets.json seats: 64 rows, ids_unique 64, out_unique 64) — the round-34 F1 gap is closed; the corrected digest is pinned at dispatch-declared.json:25 and the correction is documented at :28",
  "composition_census_note": "group census reproduces dispatch-declared.json:13 exactly (4/2/1/17/11/11/9/4/5 = 64); the same string's role sub-census ('verifiers 11', 'authors 10') does not reproduce the measured role census (verifiers 8, executors 26) — see scribe/S05-telemetry-draft.md F1-r35",
  "post_batch_integration": "<integrator-only seats and in-session acts; round-33/34 precedent: integration acts are NOT additional craft batches>",
  "durable_sources": [
    {"path": "reports/round-35/claims.json", "sha256": "ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4"},
    {"path": "reports/round-35/targets.json", "sha256": "56ad03927c7063a3616af2ed0e78ab7b1ca1f3ea43fdf67f2ecf60a7f1b63215"},
    {"path": "reports/round-35/telemetry/dispatch-declared.json", "sha256": "93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83"},
    {"path": "reports/round-35/telemetry/inputs/claims.json", "sha256": "<must equal the claims digest above>"},
    {"path": "reports/round-35/telemetry/inputs/targets.json", "sha256": "<must equal the targets digest above>"}
  ],
  "limits": [
    "Requested allocation and requested model are declarations, not execution evidence.",
    "The declared lane (opencode-go-3) is not the route used; the route deviation is named above and is not an acceptance signal.",
    "192 pre-batch launch failures are availability evidence; they are neither launched nor completed workers.",
    "Null counters are unavailable, not zero; no completion rate is inferred.",
    "Provider liveness is not round acceptance.",
    "A correction is a new snapshot with its own provenance, never an in-place edit of this record."
  ]
}
```

Round-35 deltas versus the round-34 filed record, and why:
- `route_deviation` and `pre_batch_availability_ledger` are **new** (§3): round 34 had a
  single live key and no attempt ledger; round 35 has both a deviation and three durable
  attempt records that would otherwise be orphaned from the round's own observed record.
- `composition_census_note` is **new** (F1-r35), replacing round 34's CO4-style
  `declared_note` inside `requested_allocation` — the count now reconciles, the role
  sub-census does not.
- `completed_workers_basis` / `failed_workers_basis` are kept from the round-34 **draft's**
  recommendation (`reports/round-34/scribe/S05-telemetry-draft.md:162-166`), not from filed
  bytes: round 34 filed only `launched_workers_basis`
  (`reports/round-34/telemetry/observed-dispatch.json:23`) plus a prose `failed_workers_note`
  (`:22`), and round 33 filed the same single basis key. Keeping the trio means each of the
  three counters carries its own basis string in this round's record.
- Fill rules unchanged: counters only from a native dispatch/result extract the owner holds,
  filed under `reports/round-35/telemetry/`; otherwise the honest filing is
  `state: open-at-seat-close` with `null` counters, owner and reason
  (`reports/round-32/telemetry/dispatch-stats.json` precedent). Never point a
  `durable_sources` entry at `.scratch/` (`.gitignore:6`). No credentials, authorization
  headers or private prompt payloads (`AGENTS.md` telemetry rules).

## 5. Template B — closing-snapshot skeleton → `reports/round-35/telemetry/availability-close-35.json`

Name authority is settled by filed bytes and is not re-opened: seven snapshots exist, all
`availability-close-<N>.json` (`find reports -name "availability-close*.json"` →
`{19,25,26,27,28,33,34}`, 2026-10-19T08:14Z); zero `closing-snapshot*.json`; the SKILL.md
instrument globs `telemetry/availability-close-*.json` and keys on `closes` +
`closes_sha256` (`SKILL.md:732`).

```json
{
  "schema": "kotodama-availability-closing-snapshot-v1",
  "round": 35,
  "date": "<date reports/round-35/validation.json lands>",
  "closes": "reports/round-35/telemetry/dispatch-declared.json",
  "closes_sha256": "93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83",
  "closed_fields": {
    "observed_launches": "<int|null> (read from reports/round-35/telemetry/observed-dispatch.json launched_workers, basis: <artifact>)",
    "observed_completions": "<int|null> (observed-dispatch.json completed_workers)",
    "observed_failures": "<int|null> (observed-dispatch.json failed_workers)",
    "observed_window_utc": "<start/end> (observed-dispatch.json observed_window_utc)",
    "actual_route": "opencode-go lane key 1, wire model deepseek-v4.1-flash — the declared lane opencode-go-3 was 402'd (observed-dispatch.json actual_route + route_deviation)",
    "pre_batch_availability": "3 attempts, 192 launch failures, 0 seats started; keys 3/4/5 returned 402 insufficient funds (observed-dispatch.json pre_batch_availability_ledger, digests of the three attempt files)",
    "runtime_concurrency": "could-not-recover as a measured counter: null with owner orchestrator and reason recorded in observed-dispatch.json (AGENTS.md: unknown counters stay null, not inferred)",
    "seat_list_reconciliation": "requested_workers 64 == 64 enumerable seat rows (round-34 F1 closed; dispatch-declared.json:25,:28)",
    "composition_role_subcensus": "measured mismatch carried, not edited: declared 'verifiers 11 / authors 10' vs measured verifiers 8 / executors 26 (scribe/S05-telemetry-draft.md F1-r35)"
  },
  "could_not_recover": [
    "runtime_concurrency: seat-level launch telemetry is not observable from the parent process"
  ],
  "owner": "integrator (goal-mode parent), for the lane",
  "reason": "closing snapshot filed once reports/round-35/validation.json landed; every field the declaration left open is filled above, each citing the durable artifact it was read from",
  "sources": [
    "reports/round-35/telemetry/dispatch-declared.json (sha256 93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83, re-verified unchanged at 2026-10-19T08:16:32Z)",
    "reports/round-35/telemetry/observed-dispatch.json",
    "reports/round-35/telemetry/availability-attempt-{1,2,3}.json",
    "reports/round-35/validation.json"
  ],
  "also_closes": [
    {"path": "reports/round-35/telemetry/observed-dispatch.json", "sha256": "<digest at close time>"},
    {"path": "reports/round-35/telemetry/availability-attempt-1.json", "sha256": "b1a9791938664674d192381fefc2a5e37e86ba0c8178f7a034b116d17af50c62"},
    {"path": "reports/round-35/telemetry/availability-attempt-2.json", "sha256": "326675b9b0132265f89473dee031d952b302d720c6826ef0bcc6b4d00fb1ac86"},
    {"path": "reports/round-35/telemetry/availability-attempt-3.json", "sha256": "667a86d498db3ec4c04b6a333a246af49dc685b4cc5164f3b9a5beb5fd770253"}
  ],
  "append_only_note": "the closed record's bytes are unchanged; this snapshot is the correction surface"
}
```

Shape authority: the schema string, `closes` on the **declaration** record, `closes_sha256`
equal to its live digest, a flat `closed_fields` map whose values carry their basis inline,
and `could_not_recover` as a list are all carried from the filed round-33/34 snapshots
(`reports/round-34/telemetry/availability-close-34.json:2-17`). `closes_sha256` is the
digest **at close time**: if the integrator must edit `dispatch-declared.json` after this
fragment, the snapshot pins the post-edit digest and says so; the rule prefers no edit
(`AGENTS.md` corrections-are-new-snapshots). A round is not admitted to `LOG.md` while this
snapshot is owed (`AGENTS.md` close-what-you-open; round-34 admission at `LOG.md:3616-3646`
cites its snapshot as the closure evidence).

**`also_closes` is optional and round 34 declined it** — `grep -c also_closes
reports/round-34/telemetry/availability-close-34.json` → `0`, so the round-33 draft's F5
recommendation (`reports/round-34/scribe/S05-telemetry-draft.md:238-248`) was not adopted and
the r33/r34 observed records' bytes remain pinned nowhere. If the integrator drops it again,
the residual must be carried explicitly: the round-35 observed record's `reason` names the
snapshot that closes it (as round 33's does, `reports/round-33/telemetry/observed-dispatch.json:6`)
and the unpinned bytes are recorded as a carried gap rather than left silent. The
round-34-runner tolerance check that justifies extra keys is
`reports/round-34/run-validation.py:313,:330-339` (`.get`-based reads, `optional=True`); round 35's
own runner is not authored yet, so the integrator must re-confirm tolerance there.

## 6. Template C — worker self-observation (lower bound only)

S05's own sample, filed here as text because a seat cannot write into `telemetry/`:

```json
{
  "round": 35,
  "owner": "S05",
  "observed_at_utc": "2026-10-19T08:15:04Z",
  "evidence_kind": "worker-self-observation",
  "source": "S05 received the round-35 telemetry-scribe assignment (cross claim) and is executing it; UTC observation time from date -u +%FT%TZ. No native full-wave result was supplied to this worker.",
  "sessions": [{"assignment": "S05", "state_at_observation": "active"}],
  "counts_date": "2026-10-19",
  "counting_command": "<the scratch-marker census one-liner in this section, t0 = 2026-10-19T08:05:00Z (the filed declaration stamp)>",
  "peer_marker_census": {
    "window_utc": {"start": "2026-10-19T08:05:00Z", "end": "2026-10-19T08:15:04Z", "closed": true},
    "markers": 23,
    "seat_labels_from_hyphenated_names": ["a07", "c14", "o10", "r01", "s02"],
    "seat_labels_from_bare_names": ["c09", "c17", "k01", "o04", "o05", "o08", "o09", "r04"],
    "unattributed": ["assemble", "handoff", "tmpb4x0ue5a", "tmpzw4btgnd", "tmpvo4iw5p9", "tmpxpyc1zrg"],
    "interpretation": "lower bound on concurrently active seats; not a census, not a completion count"
  },
  "scope": "One worker self-observation plus a scratch-marker lower bound; neither an independent worker census nor evidence of the actual upstream model, full-wave launch/completion count, concurrency, wall time or HTTP traffic.",
  "unavailable_owner": "Round-35 orchestrator (native dispatch/result holder)",
  "unavailable_reason": "The worker-visible round-35 claims and targets declare requests, not native execution outcomes. Full-wave dispatch metadata is not available in this worker's assigned inputs. File a new snapshot with redacted native dispatch/result extracts; do not replace this partial observation."
}
```

Census command and observed output (run by S05, window anchored on the declaration stamp
`dispatch-declared.json:5` = 2026-10-19T08:05:00Z):

```sh
python3 -B -c "import pathlib,datetime,re; t0=datetime.datetime(2026,10,19,8,5,0,tzinfo=datetime.timezone.utc).timestamp(); rows=[(datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),p.name) for p in pathlib.Path('.scratch').iterdir() if p.stat().st_mtime>=t0]; print(len(rows)); print(sorted(rows)); print(sorted({re.match(r'^([A-Za-z0-9]+?)-',n).group(1).lower() for _,n in rows if re.match(r'^([A-Za-z0-9]+?)-',n)}))"
```

- 2026-10-19T08:15:04Z → `23` markers; sample names include `c09`, `c17`, `o04`, `o05`,
  `o08`, `o09`, `r04`, `k01`, `C14-entry-audit-r19.py`, `r01-poll.sh`, `a07-iso`,
  `s02-selftest-before.txt`, `o10-selftest-baseline.txt`, `assemble-d4-typed-8d3apj0p`,
  `handoff-selftest-zv5or9z_`, and four `tmp*` scratch dirs.
- Method caveat, new this round: the label regex only attributes names containing a hyphen,
  so the eight bare-name markers (`c09`, `c17`, `k01`, `o04`, `o05`, `o08`, `o09`, `r04`)
  appear in the name list but not in the printed label set. Template C therefore files both
  lists rather than one label set. The count is still a **lower bound** and still grows with
  the same anchor (round-33/34 behaviour,
  `reports/round-34/scribe/S05-telemetry-draft.md:295-297`); only the value printed with its
  instant is meaningful.
- `.scratch/` is gitignored (`.gitignore:6`, `git check-ignore -v .scratch/` →
  `.gitignore:6:.scratch/`), so this census is **not** a durable evidence surface and must
  never be promoted into `launched_workers` / `completed_workers`.

## 7. Findings for the integrator

- **F1-r35 — composition role sub-census (§2).** "verifiers 11" / "authors 10" at
  `dispatch-declared.json:13` vs measured verifiers 8 / executors 26. Record in the round-35
  runner's CO leg; do not edit the digest-pinned declaration.
- **F2 — the filed `counting_command` is not runnable as written.** Running
  `python3 -c 'len(json.load(open("reports/round-35/targets.json"))["seats"])'`
  (`dispatch-declared.json:15`, third clause) exits 1 with
  `NameError: name 'json' is not defined` — the `import json` is missing. The `date` and
  `sha256sum` clauses run fine. A corrected, re-runnable form (S05, 08:16Z) is
  `python3 -c 'import json; print(len(json.load(open("reports/round-35/targets.json"))["seats"]))'`
  → `64`. Route: the round-35 runner's telemetry leg uses the corrected form and cites this
  fragment; `dispatch-declared.json` is not edited (corrections are new snapshots).
- **F3 — cross-round availability summary omits r34's non-completion.**
  `availability-attempt-3.json:13` states "key 2 (r34): LIVE, 63/63"; the filed round-34
  record is launched 63 / completed 63 / **failed 1** with the D17 note
  (`reports/round-34/telemetry/observed-dispatch.json:19-22`). Read together; a future
  availability summary should carry the failure, and round 35's own record must not restate
  the r34 line as a clean pass.
- **F4 — the declaration stamp is nominal, not a measured instant.** `claims.json:6`,
  `dispatch-declared.json:5` and `availability-attempt-1.json:5` all carry
  `2026-10-19T08:05:00Z`, while the mtimes are 08:03:57Z (claims — *before* its own stamp by
  63 s), 08:06:39Z (declaration) and 08:08:53Z (attempt 1). The window anchor mandated for
  this draft is therefore the filed stamp; Template A's `window_basis` must say the window is
  anchored on the stamp and that the batch's own instants come from `date -u` at dispatch and
  return, not from these stamps. Do not compute a wall time from a nominal stamp.
- **F5 — `inputs/` durable copies owed.** `ls reports/round-35/telemetry/inputs` → No such
  file or directory (08:14Z). Round 33 and round 34 both hold byte-exact copies
  (`cmp reports/round-34/claims.json reports/round-34/telemetry/inputs/claims.json` → 0,
  same for targets, re-verified 08:16Z; round-33 pair likewise 0). Method: copy
  `reports/round-35/{claims,targets}.json` byte-exact and re-run `cmp`; both sources end in
  `0a`.
- **F6 — the observed record's bytes are pinned nowhere, again (§5).** Round 34 declined
  `also_closes`; round 33's F5 gap is carried, not repaired (filed bytes). Round 35 either
  adopts `also_closes` or carries the residual with the `reason`-names-the-snapshot form.
- **F7 — the closure audit still cannot see the open record.** `SKILL.md:732` globs
  `reports/round-*/availability*.json` (round-level, not `telemetry/`); round 35's open-state
  record is `telemetry/observed-dispatch.json` and the three attempts sit under
  `telemetry/` too, so none can match. Run verbatim at 2026-10-19T08:14Z it printed nothing,
  exit 0. The binding instrument is the round-35 runner's own telemetry leg (§8), not the
  audit. **Do not create a decoy `reports/round-35/availability.json`** — the round-30
  `duplicate_evidence` control is the reason to file one record, not two.
- **F8 — fleet report owed.** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-35/` → No such
  file or directory (08:15Z); round 34's exists (`kotodama.md`). Parent's artifact, owed at
  close.
- **F9 — no runner, no validation.json, so the closing snapshot is owed.**
  `reports/round-35/run-validation.py` and `reports/round-35/validation.json` are both absent
  (08:14Z). The runner's telemetry leg is drafted in §8 and its author owns the adoption.
- **F10 — F-C13-1 context.** `dispatch-declared.json:29` carries the standing rule "no
  in-tree execution of any filed round runner"; the incident/prevention record is
  `LOG.md:3548-3562`. This telemetry draft executed no round runner and read only filed
  bytes plus the round-30/33/34 records.

## 8. Counting commands and controls for the round-35 runner (draft leg)

Positive checks:

1. `sha256sum reports/round-35/claims.json reports/round-35/targets.json` equals
   `dispatch-declared.json:21,:25` (`ccfaafc3…`, `56ad0392…`) and the observed record's
   `durable_sources`.
2. `sha256sum reports/round-35/telemetry/dispatch-declared.json` equals the snapshot's
   `closes_sha256` (`93e205a2…`); `closes` resolves to that same path.
3. `cmp reports/round-35/claims.json reports/round-35/telemetry/inputs/claims.json` and the
   targets pair → exit 0 (round-30 control; F5).
4. §2 composition census reproduces `dispatch-declared.json:13`'s **group** counts and equals
   `requested_workers` 64 — asserted as equality this round (r34's CO4 deviation form is
   retired) — **and** separately reports the role sub-census mismatch (F1-r35) instead of
   asserting equality there.
5. The filed `counting_command` is re-run in its corrected form (F2) and its output recorded;
   the leg must not claim the filed string is reproducible.
6. Observed record: `round == 35`, `state == "open-at-seat-close"`, non-empty `owner` and
   `reason`; every null counter has an owner; `route_deviation.actual_lane` names key 1 while
   `requested_allocation.provider_lane` stays `opencode-go-3`; the 192 pre-batch launch
   failures appear only in the availability ledger.
7. Each of the three `availability-attempt-*.json` digests in the observed record equals the
   live file digest, and each attempt's `launched_workers` is 0.
8. Snapshot: `schema == "kotodama-availability-closing-snapshot-v1"`, `round == 35`, `date`
   matches `YYYY-MM-DD`, `closes`/`closes_sha256` pin the declaration.
9. `git check-ignore -v` on the telemetry paths → no match (run 08:16Z: exit 1, no output);
   `.scratch/` matches `.gitignore:6`.
10. `test -s reports/round-35/telemetry/availability-close-35.json` once
    `reports/round-35/validation.json` lands.

Negative controls to reject (round-30 name set, `reports/round-30/fixes/telemetry-convention.md:33-35`,
extended): `null_to_zero`, `invented_completion_count`, `requested_as_completed`,
`invented_served_model`, `full_wave_pass_without_extract`, `scratch_only_dependency`,
`scratch_evidence_path`, `raw_evidence_tamper`, `duplicate_evidence`,
`missing_counting_command`, `missing_counts_date`, `closing_snapshot_digest_mismatch`,
`historical_recovery_overclaim`, plus two round-35 additions:
**`declared_lane_as_actual`** — a record whose `actual_route`/`provider_lane` reads
`opencode-go-3` while the batch ran on key 1 (F3/§3); and
**`attempt_failures_as_batch_failures`** — a record folding the 192 pre-batch launch failures
into `failed_workers`. Round 34's `count_field_over_seat_list` control is retired this round
because 64 == 64; if it is kept, it must pass, not be relaxed.

**Cross-check against the landed S04 integration draft** (filed while this fragment was being
written; `reports/round-35/scribe/S04-integration-draft.md`): S04 independently reaches the
same telemetry conclusions this fragment measured — the measured role census over the prose
`seat_composition` (`S04:196-202`), the owed observed record plus the binding
closing-snapshot filename and the key-1 route fill (`S04:203-221`), and the declared-vs-observed
lane divergence with the 192 launch failures not netted against the 64 completions
(`S04:768-780`); S04's CO4 also asserts `64 == 64` with no r34-style deviation
(`S04:765-767`). No conflict. This fragment adds four things S04 does not carry: the
availability-attempt ledger inside the observed record (§4), the F2 counting-command defect,
the F4 nominal-stamp caveat, and Template C's worker self-observation with the label-regex
method caveat (§6).

## Owed

- `reports/round-35/telemetry/observed-dispatch.json` — integrator lands from Template A
  (S05 may write only its own out path). Absent at 2026-10-19T08:16Z.
- `reports/round-35/telemetry/inputs/{claims,targets}.json` — byte-exact durable copies +
  `cmp` control (F5).
- `reports/round-35/telemetry/availability-close-35.json` — owed once
  `reports/round-35/validation.json` lands (Template B); the round is not admissible to
  `LOG.md` while it is owed.
- The round-35 runner's telemetry leg (§8) — owner: whichever seat/integrator authors
  `reports/round-35/run-validation.py` (absent at 08:14Z).
- F1-r35 role sub-census record and F2 corrected counting command — owner: the round-35
  runner's CO/telemetry leg; `dispatch-declared.json` and `targets.json` are digest-pinned
  orchestrator files and are not edited by S05.
- F3 r34 `63/63` cross-file note — owner: a future availability summary (new snapshot; the
  attempt file is filed bytes).
- F6 `also_closes` decision — integrator: adopt, or carry the residual with the
  `reason`-names-the-snapshot form.
- F8 fleet report `.ufo/reports/round-35/kotodama.md` — parent's artifact, owed at close.
- `to-verify`: whether the round-35 orchestrator holds a native dispatch/result extract for
  the key-1 batch. S05 cannot see one and no fleet round-35 dir exists (F8); the counters in
  Template A stay `null` until such an artifact exists.
- `to-verify`: whether round 35's own runner tolerates the extra keys Template A/B add
  (round-34 tolerance verified at `reports/round-34/run-validation.py:313,:330-339`; the round-35
  runner does not exist yet).

## Citations

- `reports/round-35/targets.json` — S05 seat object (`role: scribe`, `claim: cross`,
  `mission: "Telemetry draft per the round-33/34 convention…"`, `out:
  scribe/S05-telemetry-draft.md`), `seat_count 64`, 64 seat rows (ids_unique 64,
  out_unique 64), `shared_rules` array.
- `reports/round-35/claims.json:6,:8,:11,:12,:13,:17,:19` — `declared_at_utc`
  2026-10-19T08:05:00Z, `baseline_commit` 4a7aede, lane `opencode-go-3`, model
  `deepseek-v4.1-flash`, `requested_workers` 64, axes in play, freshness pause.
- `reports/round-35/telemetry/dispatch-declared.json:5,:8,:11,:12,:13,:15,:17,:20-25,:28,:29,:30`
  — stamp, declared lane, requested workers/batched calls, composition string, counting
  command, baseline commit, durable sources + digests, authoring note (60→64 correction),
  standing rules, open closing-snapshot note.
- `reports/round-35/telemetry/availability-attempt-1.json:5,:6,:8-13,:15` — route, counters
  0/0/64, 402 failure class and basis, round-10 precedent, counting command.
- `reports/round-35/telemetry/availability-attempt-2.json:5,:6,:8-13` — same shape, key 4.
- `reports/round-35/telemetry/availability-attempt-3.json:5,:6,:8-14` — key 5, `key_census_so_far`
  (key 1 64/64, key 2 63/63), disposition: round 35 re-dispatches on key 1 as a named
  deviation.
- `REGIMEN.md:13` (rounds 33–35 schedule row: opencode-go / deepseek-v4.1-flash, 64 seats,
  round-robin across live keys), `:27-28` (1–3 claims, one batched swarm per round), `:66-69`
  (scope: provider deviations only as declared, 402'd keys skipped with the failure
  recorded), `:41-43` (admission rule), `:53-58` (done when).
- `AGENTS.md` — availability/dispatch telemetry rules (requested vs observed, nulls with
  owner+reason, durable paths + digests, no credentials/private payloads), "Close what you
  open", append-only corrections, F-C13-1.
- `reports/round-34/telemetry/observed-dispatch.json` (sha256 `57e0b2d9…`): `:2-9` state/
  owner/reason/window, `:11-18` requested allocation + the CO4 declared note, `:19-23`
  counters, the prose `failed_workers_note` and the single `launched_workers_basis`,
  `:24-28` concurrency null, actual route, post-batch integration, `:29-50` durable sources
  incl. `inputs/` copies.
- `reports/round-34/telemetry/availability-close-34.json` (sha256 `af2ccd99…`): `:2-6`
  schema/round/date/closes/closes_sha256, `:7-14` flat `closed_fields`, `:15-19`
  `could_not_recover`/owner/reason, `:20-24` sources; `grep -c also_closes` → 0 (F6).
- `reports/round-34/run-validation.py:17-18` (record path constants), `:108-126` (CO4
  dispatch-shape + 64/63 deviation semantics), `:313,:330-339` (`leg_close` definition,
  observed-record reads and owed-snapshot handling), `:401` (close-time inputs note).
- `reports/round-34/scribe/S05-telemetry-draft.md:9-11,:162-166,:238-248,:295-297` — draft-
  not-measurement framing, the per-counter basis recommendation (round 34 filed only
  `launched_workers_basis`), the unadopted F5 `also_closes` recommendation, census-growth
  caveat.
- `reports/round-35/scribe/S04-integration-draft.md:196-202,:203-221,:765-767,:768-780` — the
  sibling seat's independent measured census, owed-record/close-name list, CO4 64==64
  assertion and lane-divergence trap; read after this fragment's first draft (§8 cross-check).
  Read-only; no S04 byte was changed by S05.
- `reports/round-33/telemetry/observed-dispatch.json:6` (reason naming the closing snapshot),
  sha256 `89985f43…`; `reports/round-33/validation.json` (r33 acceptance) via `LOG.md:3519-3545`.
- `LOG.md:3519-3545` (round-33 admission, observed 64/64), `:3548-3562` (F-C13-1 incident +
  prevention), `:3616-3646` (round-34 admission: 63/63 dispatched+completed with the named
  CO4 deviation, telemetry closed via `availability-close-34.json`).
- `SKILL.md:732` — close-what-you-open audit one-liner (globs
  `reports/round-*/availability*.json`, keys on `closes` + `closes_sha256`); `sha256sum
  SKILL.md` = `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, 732 lines.
- `reports/round-30/fixes/telemetry-convention.md:6-16` (convention + defect source and the
  round-30 partial-snapshot demonstration), `:18-37` (controls and reproduction: `:20`
  stdout-capture rule, `:33-35` the 10 controls incl. requested-as-completed inflation and
  scratch-only rejection, `:34` the trailing-newline trap, `:37` the counter-inflation
  rationale).
- `reports/round-32/telemetry/dispatch-stats.json` — `could-not-evaluate` partial-observation
  precedent; `reports/round-10/availability-attempt-{1,2,3}.json` — the 402-key precedent.
- `.gitignore:6` — `.scratch/` ignored.
- Commands run by S05 (lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all
  2026-10-19T08:14:08–08:16:32Z): `date -u +%FT%TZ`; `sha256sum` + `stat -c '%n %s bytes
  mtime=%y'` on the six round-35 declaration/attempt artifacts (digests re-verified
  unchanged at 08:16:32Z); `git rev-parse HEAD`; `tail -c 1 | xxd -p` on claims/targets
  (both `0a`); the §2 composition/role-census one-liner; the filed `counting_command` third
  clause verbatim (NameError, exit 1) and its corrected form (`64`); `find reports -name
  "availability-close*.json"` (7); `find reports/round-35 -name "availability*"` (3 attempts);
  `ls reports/round-35/telemetry/inputs` (absent); `test -f` on
  `reports/round-35/{run-validation.py,validation.json}` (both absent); the verbatim
  `SKILL.md:732` audit one-liner (no output, exit 0); `grep -c also_closes` on the round-34
  snapshot (`0`); `cmp` on the round-33 and round-34 `telemetry/inputs/` pairs (all exit 0);
  `git check-ignore -v` on the telemetry paths (exit 1, no match) and `.scratch/`
  (`.gitignore:6`); `git status --porcelain` (`?? reports/round-35/`); the §6 scratch census
  one-liner (23 markers); `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-35/` (No such
  file or directory); `wc -l LOG.md` (3646) and `grep -n "^## "` for the entry anchors.
