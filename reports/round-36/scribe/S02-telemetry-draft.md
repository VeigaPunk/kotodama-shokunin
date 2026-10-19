- Seat: S02 | scribe | cross | date 2026-10-19 | baseline ce103bf

# S02 — round-36 telemetry: observed record template + closing-snapshot skeleton + the first declared-fallback round

Mission (`reports/round-36/targets.json:43`, S02 seat object): "Telemetry draft (observed
template, closing-snapshot skeleton; window anchored on the dispatch stamp)." Out path:
`reports/round-36/scribe/S02-telemetry-draft.md`.

**This fragment drafts bytes for the integrator; it is not a measurement of the round-36
wave.** No file under `reports/round-36/telemetry/` was written or modified by this seat
(out-path constraint; `targets.json:4`). Every JSON block below is text for the integrator to
lift, per the round-34/35 precedent (`reports/round-35/scribe/S05-telemetry-draft.md:8-11`).

Round-36 delta versus round 35, up front: round 36 is the first regimen-2 round whose
dispatch ran on a **declared fallback** rather than on its declared lane, and the first whose
fallback is pre-declared in both `claims.json:9-11` and `telemetry/dispatch-declared.json:6-8`
*before* the failure. Round 35's deviation was recorded only after the fact, in
`availability-attempt-3.json:14`'s disposition. Round 36 has a filed attempt record
(`telemetry/availability-attempt-1.json:13`) that names the fallback clause itself, so the
requested-vs-observed split below is a *planned* deviation, not a discovered one — and the
templates must still keep the two apart (`AGENTS.md`: requested allocation separate from
observed route).

## 1. Declaration facts measured by S02 (durable sources)

Command (the filed `counting_command` at `reports/round-36/telemetry/dispatch-declared.json:9`,
extended with `stat`; the filed command's third clause is not runnable as written — see F1):

```sh
date -u +%FT%TZ; sha256sum reports/round-36/claims.json reports/round-36/targets.json \
  reports/round-36/telemetry/dispatch-declared.json \
  reports/round-36/telemetry/availability-attempt-1.json; \
stat -c '%n %s bytes mtime=%y' <same paths>; git rev-parse HEAD; \
tail -c 1 reports/round-36/claims.json | xxd -p
```

Read at 2026-10-19T09:26:47Z, re-verified 2026-10-19T09:28:03Z (all four digests unchanged),
lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

| path | bytes | sha256 | mtime (UTC) |
|---|---|---|---|
| `reports/round-36/claims.json` | 3505 | `b8d1af8fd1fb3814e707e24965a6bd404e83158ae26d48d852118d7abec470b8` | 2026-10-19T09:23:02Z |
| `reports/round-36/targets.json` | 6851 | `39ddbc72345d15bc9ec3aa272e161b9e9c7ce652301abca3f55a9c3e28c343d8` | 2026-10-19T09:23:43Z |
| `reports/round-36/telemetry/dispatch-declared.json` | 906 | `48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16` | 2026-10-19T09:24:40Z |
| `reports/round-36/telemetry/availability-attempt-1.json` | 790 | `ecbcdd4ca880b8acb543386ac21a74817ad54d84ec14e0476dd30ef83e5df1db` | 2026-10-19T09:25:45Z |

`git rev-parse HEAD` = `ce103bf5885af00023cdc4a174c17602476cdcf8`; `git rev-parse ce103bf` =
the same 40-hex value, so `claims.json:7` (`ce103bf`) and `dispatch-declared.json:11` resolve
to the live tree. mtimes are `stat -c %y` values converted from the host's `-0300` offset to
UTC (`06:23:02 -0300` → `09:23:02Z`).

**Digest cross-check: PASS.** My measured claims digest equals `dispatch-declared.json:13`
(`b8d1af8f…`) and my targets digest equals `:14` (`39ddbc72…`), so the filed declaration is
bound to the same bytes this seat read. Both sources end in `0a`
(`tail -c 1 | xxd -p` → `0a`; trailing-newline trap accounted for,
`reports/round-30/fixes/telemetry-convention.md:34`).

**Third digest:** `dispatch-declared.json` is pinned by no record yet; S02's measurement is
`48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16` (906 bytes). Template B
uses it as `closes_sha256`.

## 2. Composition reproduction: 32 == 32, and the declared composition string is absent

Command (re-runnable; window-free):

```sh
python3 -B -c "import json,collections; t=json.load(open('reports/round-36/targets.json')); s=t['seats']; ids=[x['id'] for x in s]; print(dict(collections.Counter(i[0] for i in ids))); print('seat_count', t['seat_count'], 'seats', len(s), 'ids_unique', len(set(ids)), 'out_unique', len({x['out'] for x in s})); print('role census', dict(collections.Counter(x['role'] for x in s))); print('claim census', dict(collections.Counter(x.get('claim') for x in s)))"
```

Observed output (2026-10-19T09:26Z):

```
{'K': 3, 'P': 1, 'X': 3, 'D': 10, 'C': 10, 'R': 3, 'S': 2}
seat_count 32 seats 32 ids_unique 32 out_unique 32
role census {'scout': 3, 'planner': 1, 'connector': 1, 'executor': 12, 'verifier': 4, 'scribe': 6, 'reviewer': 3, 'critic': 2}
claim census {'D': 14, 'C': 6, 'Ca': 6, 'cross': 6}
```

**`requested_workers` 32 equals the enumerable seat list 32.** `claims.json:9` and
`dispatch-declared.json:7` both declare 32; the seat array holds 32 rows, ids unique 32, out
paths unique 32. The round-34 CO4 deviation (63 vs 64,
`reports/round-34/run-validation.py:122-126`) and round-35's role sub-census defect
(`reports/round-35/scribe/S05-telemetry-draft.md` F1-r35) have **no round-36 analogue** — but
for a different reason than round 35's: the r36 declaration carries **no composition string at
all** (compare `reports/round-35/telemetry/dispatch-declared.json:13`), so there is nothing to
reproduce and nothing to contradict. The census is measured against `seat_count`,
`requested_workers` and the seat rows only.

The claim census (`D` 14, `C` 6, `Ca` 6, `cross` 6) partitions the 32 seats across the three
declared claims plus the cross seats, matching `claims.json:15-34`'s three claim objects and
`targets.json`'s per-seat `claim` fields. The group census (`K`3 `P`1 `X`3 `D`10 `C`10 `R`3
`S`2) sums to 32; note `C` here counts `C01`–`C05` **and** `Ca01`–`Ca05` (both prefixes begin
`C`), so a prefix-based census must special-case `Ca` or it will mis-split the coverage and
calibration blocks.

## 3. The declared fallback: hyper → devin, pre-declared and then invoked

Round 36 is the first regimen-2 round whose dispatch did not run on its declared lane, and
the first where that outcome was pre-declared.

| fact | filed evidence |
|---|---|
| declared lane | `hyper / deepseek-v4.1-flash` (`claims.json:9`, `dispatch-declared.json:6`) |
| declared fallback | `devin/deepseek-v4-1-flash-high (declared if hyper exhausted)` (`claims.json:11`, `dispatch-declared.json:8`) |
| attempt 1 route | `hyper / deepseek-v4.1-flash` (`availability-attempt-1.json:6`) |
| attempt 1 result | 0 launched / 0 completed / **32 failed at launch**, `402 You're out of credits (hyper.charm.land)` (`:8-12`) |
| attempt 1 disposition | "DECLARED FALLBACK per REGIMEN.md position 4 … the batch re-dispatches on devin/deepseek-v4-1-flash-high as attempt-2" (`:13`) |
| authority | `REGIMEN.md:14` (schedule row 4: "hyper / deepseek-v4.1-flash; fallback devin/deepseek-v4-1-flash-high"), `:66-69` (provider deviations permitted only as declared; the hyper→devin fallback is the named one), `:73-75` (apply the declared fallback once; if that also fails, file the round `could-not-dispatch`) |

Binding consequences for Template A:

- `requested_allocation.provider_lane` stays `hyper` (the declaration);
  `actual_route` names `devin / deepseek-v4-1-flash-high` and cites
  `availability-attempt-1.json:13`. Do not overwrite the declared lane with the actual one
  (`AGENTS.md`: requested allocation separate from actual route). This is the round-35
  `declared_lane_as_actual` trap in a new costume.
- The **32 launch failures are not** `launched_workers` and **not** `failed_workers` for the
  observed batch: zero seats started in attempt 1. They belong in the pre-batch availability
  ledger the record carries by digest, with an explicit sentence that they are excluded from
  the batch counters (round-35 `attempt_failures_as_batch_failures` control).
- Only one attempt file exists (`ls reports/round-36/telemetry/` → `availability-attempt-1.json`,
  `dispatch-declared.json`; 2026-10-19T09:28Z). If the devin batch succeeds, attempt 1 is the
  **only** pre-batch attempt and the record must say so; a missing `availability-attempt-2.json`
  is not a defect — the fallback is attempt 2 and it is the batch itself. If devin also fails,
  `REGIMEN.md:73-75` binds: file the round `could-not-dispatch` with owner and reason, and the
  record's state becomes that instead of `open-at-seat-close`.
- The fallback is a **single** application (`REGIMEN.md:73`: "apply the declared fallback
  once"). A third route would be an undeclared provider deviation.

## 4. Template A — observed-dispatch record → `reports/round-36/telemetry/observed-dispatch.json`

Lift the round-35 **filed** shape (`reports/round-35/telemetry/observed-dispatch.json`, sha256
`f7a1e1f968a3d7b212e4393e42884675299b458cb891ab5dcc397f35b01c0c53`) and substitute round-36
values. The round-35 runner's `leg_close` reads this file with `.get` on
`state`/`owner`/`reason`/`round` (`reports/round-35/run-validation.py:336-345`) and tolerates
extra keys; the round-36 leg should keep those four semantics and may add the checks in §8.

```json
{
  "record": "observed-dispatch",
  "round": 36,
  "state": "open-at-seat-close",
  "owner": "orchestrator (goal-mode parent)",
  "reason": "counters are filled from the batched-dispatch result; the record closes when reports/round-36/telemetry/availability-close-36.json lands in the same integrating pass (AGENTS.md close-what-you-open)",
  "observed_window_utc": "<batch-dispatch instant>/<batch-return instant, both from date -u +%FT%TZ>",
  "window_basis": "the single batched AgentSwarm dispatch call that ran on the devin fallback, measured <N> s from <HH:MM:SSZ> to the batch result; the hyper attempt that precedes it is excluded from the window. The window is anchored on the filed dispatch stamp 2026-10-19T09:20:00Z (dispatch-declared.json:5), which is nominal — see F4",
  "counting_command": "AgentSwarm result summary '<summary>completed: N</summary>' and per-seat outcome attribute; date -u +%FT%TZ at dispatch and at close",
  "counting_date": "2026-10-19",
  "requested_allocation": {
    "provider_lane": "hyper",
    "model": "deepseek-v4.1-flash",
    "requested_workers": 32,
    "batched_calls": 1,
    "declared_fallback": "devin/deepseek-v4-1-flash-high (declared if hyper exhausted)",
    "declared_note": "declared per reports/round-36/claims.json:9-11 and telemetry/dispatch-declared.json:6-8; the batch actually ran on the declared fallback (route_deviation below)"
  },
  "route_deviation": {
    "declared_lane": "hyper",
    "declared_model": "deepseek-v4.1-flash",
    "actual_route": "devin / deepseek-v4-1-flash-high",
    "deviation_class": "declared fallback (pre-declared, then invoked) — not an undeclared substitution",
    "basis": "reports/round-36/telemetry/availability-attempt-1.json:8-13 — 32 seats failed at launch with 402 'You're out of credits' (hyper.charm.land), zero launched; disposition names the REGIMEN position-4 fallback and re-dispatches on devin as attempt-2",
    "authority": "REGIMEN.md:14 (schedule row 4 names the fallback), REGIMEN.md:66-69 (provider deviations permitted only as declared), REGIMEN.md:73-75 (apply the declared fallback once)",
    "owner": "orchestrator",
    "declaration_edited": false
  },
  "pre_batch_availability_ledger": {
    "attempts": 1,
    "seats_failed_at_launch": 32,
    "seats_started": 0,
    "excluded_from_batch_counters": "true — zero seats started in attempt 1; the 32 launch failures are launch-availability evidence, not batch outcomes",
    "attempts_after_ledger": "the fallback batch itself is attempt 2 and is not a pre-batch attempt; no availability-attempt-2.json is expected while the fallback succeeds",
    "files": [
      {"path": "reports/round-36/telemetry/availability-attempt-1.json", "sha256": "ecbcdd4ca880b8acb543386ac21a74817ad54d84ec14e0476dd30ef83e5df1db", "route": "hyper / deepseek-v4.1-flash", "failure_class": "402 You're out of credits (hyper.charm.land)", "launched_workers": 0}
    ]
  },
  "launched_workers": null,
  "launched_workers_basis": "<the native result artifact this count was read from; 32 is the requested and the enumerable count — do not fill it from either>",
  "completed_workers": null,
  "completed_workers_basis": "<same artifact; per-seat outcome attribute>",
  "failed_workers": null,
  "failed_workers_basis": "<same artifact; a zero-failure statement needs the same basis as the positive counts>",
  "runtime_concurrency": null,
  "runtime_concurrency_owner": "orchestrator",
  "runtime_concurrency_reason": "seat-level launch telemetry is not observable from the parent; AgentSwarm queues launches automatically. Unknown counters stay null per AGENTS.md, not inferred.",
  "actual_route": "devin lane, wire model deepseek-v4-1-flash-high (declared hyper lane was 402'd at launch; declared fallback invoked once)",
  "seat_list_reconciliation": "requested_workers 32 (dispatch-declared.json:7) equals the enumerable seat list (targets.json seats: 32 rows, ids_unique 32, out_unique 32) — the round-34 F1 gap stays closed",
  "composition_census_note": "no composition string is filed this round (dispatch-declared.json carries no seat_composition key), so there is no declared composition to reproduce; the measured census (roles scout 3 / planner 1 / connector 1 / executor 12 / verifier 4 / scribe 6 / reviewer 3 / critic 2; claims D 14 / C 6 / Ca 6 / cross 6) is recorded against the seat rows alone — see scribe/S02-telemetry-draft.md §2",
  "post_batch_integration": "<integrator-only seats and in-session acts; round-33/34/35 precedent: integration acts are NOT additional craft batches>",
  "durable_sources": [
    {"path": "reports/round-36/claims.json", "sha256": "b8d1af8fd1fb3814e707e24965a6bd404e83158ae26d48d852118d7abec470b8"},
    {"path": "reports/round-36/targets.json", "sha256": "39ddbc72345d15bc9ec3aa272e161b9e9c7ce652301abca3f55a9c3e28c343d8"},
    {"path": "reports/round-36/telemetry/dispatch-declared.json", "sha256": "48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16"},
    {"path": "reports/round-36/telemetry/inputs/claims.json", "sha256": "<must equal the claims digest above>"},
    {"path": "reports/round-36/telemetry/inputs/targets.json", "sha256": "<must equal the targets digest above>"}
  ],
  "limits": [
    "Requested allocation and requested model are declarations, not execution evidence.",
    "The declared lane (hyper) is not the route used; the fallback is declared in REGIMEN.md and named above, and is not an acceptance signal.",
    "32 pre-batch launch failures are availability evidence; they are neither launched nor completed workers.",
    "Null counters are unavailable, not zero; no completion rate is inferred.",
    "Provider liveness is not round acceptance.",
    "A correction is a new snapshot with its own provenance, never an in-place edit of this record."
  ]
}
```

Round-36 deltas versus the round-35 filed record, and why:

- `route_deviation.deviation_class` is **new**: round 35 had to argue that a post-hoc key
  substitution was within the rules; round 36's substitution is the one `REGIMEN.md:14`
  pre-names, so the record can say so in one field instead of a paragraph.
- `requested_allocation.declared_fallback` is **new**: the declaration carries it
  (`dispatch-declared.json:8`) and the observed record is the natural place to bind the
  declaration to the invocation.
- `pre_batch_availability_ledger.attempts` is **1**, not round 35's 3 — only one attempt file
  exists. `attempts_after_ledger` states explicitly that the fallback batch is attempt 2 so a
  future reader does not go looking for a missing `availability-attempt-2.json`.
- `composition_census_note` **replaces** round 35's `composition_census_note` content: round
  35's reported a measured mismatch against a declared string; round 36's reports that no
  string is declared.
- `completed_workers_basis` / `failed_workers_basis` are carried from round 35's **draft**
  recommendation, not from filed bytes — round 35 filed only `launched_workers_basis`
  (`reports/round-35/telemetry/observed-dispatch.json`). Keeping the trio means each counter
  carries its own basis string, which is the `AGENTS.md` bar.
- Fill rules unchanged: counters only from a native dispatch/result extract the owner holds,
  filed under `reports/round-36/telemetry/`; otherwise the honest filing is
  `state: open-at-seat-close` with `null` counters, owner and reason
  (`reports/round-32/telemetry/dispatch-stats.json` precedent). Never point a
  `durable_sources` entry at `.scratch/` (`.gitignore:6`). No credentials, authorization
  headers or private prompt payloads (`AGENTS.md` telemetry rules).

## 5. Template B — closing-snapshot skeleton → `reports/round-36/telemetry/availability-close-36.json`

Name authority is settled by filed bytes and is not re-opened: eight snapshots exist, all
`availability-close-<N>.json` (`find reports -name "availability-close*.json"` →
`{19,25,26,27,28,33,34,35}`, 2026-10-19T09:26Z); zero `closing-snapshot*.json`. The
`SKILL.md:732` instrument globs `telemetry/availability-close-*.json` and keys on `closes` +
`closes_sha256`.

```json
{
  "schema": "kotodama-availability-closing-snapshot-v1",
  "round": 36,
  "date": "<date reports/round-36/validation.json lands>",
  "closes": "reports/round-36/telemetry/dispatch-declared.json",
  "closes_sha256": "48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16",
  "closed_fields": {
    "observed_launches": "<int|null> (read from reports/round-36/telemetry/observed-dispatch.json launched_workers, basis: <artifact>)",
    "observed_completions": "<int|null> (observed-dispatch.json completed_workers)",
    "observed_failures": "<int|null> (observed-dispatch.json failed_workers)",
    "observed_window_utc": "<start/end> (observed-dispatch.json observed_window_utc)",
    "actual_route": "devin / deepseek-v4-1-flash-high — the declared hyper lane returned 402 with zero seats launched (observed-dispatch.json actual_route + route_deviation)",
    "pre_batch_availability": "1 attempt, 32 launch failures, 0 seats started; hyper returned 402 'You're out of credits' (observed-dispatch.json pre_batch_availability_ledger, digest of availability-attempt-1.json)",
    "declared_fallback_invoked": "devin/deepseek-v4-1-flash-high, pre-declared at claims.json:11 and dispatch-declared.json:8, applied once per REGIMEN.md:73; no availability-attempt-2.json is owed while the fallback batch succeeds",
    "runtime_concurrency": "could-not-recover as a measured counter: null with owner orchestrator and reason recorded in observed-dispatch.json (AGENTS.md: unknown counters stay null, not inferred)",
    "seat_list_reconciliation": "requested_workers 32 == 32 enumerable seat rows (dispatch-declared.json:7, targets.json seat_count 32)",
    "composition_census": "no declared composition string this round; measured roles scout 3 / planner 1 / connector 1 / executor 12 / verifier 4 / scribe 6 / reviewer 3 / critic 2 and claims D 14 / C 6 / Ca 6 / cross 6 over 32 seat rows (scribe/S02-telemetry-draft.md §2)"
  },
  "could_not_recover": [
    "runtime_concurrency: seat-level launch telemetry is not observable from the parent process"
  ],
  "owner": "integrator (goal-mode parent), for the lane",
  "reason": "closing snapshot filed once reports/round-36/validation.json landed; every field the declaration left open is filled above, each citing the durable artifact it was read from",
  "sources": [
    "reports/round-36/telemetry/dispatch-declared.json (sha256 48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16, re-verified unchanged at 2026-10-19T09:28:03Z)",
    "reports/round-36/telemetry/observed-dispatch.json",
    "reports/round-36/telemetry/availability-attempt-1.json",
    "reports/round-36/validation.json"
  ],
  "also_closes": [
    {"path": "reports/round-36/telemetry/observed-dispatch.json", "sha256": "<digest at close time>"},
    {"path": "reports/round-36/telemetry/availability-attempt-1.json", "sha256": "ecbcdd4ca880b8acb543386ac21a74817ad54d84ec14e0476dd30ef83e5df1db"}
  ],
  "append_only_note": "the closed record's bytes are unchanged; this snapshot is the correction surface"
}
```

Shape authority: the schema string, `closes` on the **declaration** record, `closes_sha256`
equal to its live digest, a flat `closed_fields` map whose values carry their basis inline, and
`could_not_recover` as a list are all carried from the filed round-33/34/35 snapshots. All
three live snapshots still verify: pinned == live for `closes_sha256`
(33 `139b964e…`, 34 `53e2bb01…`, 35 `93e205a2…`, re-checked 2026-10-19T09:28Z).

**`also_closes` is optional and rounds 33/34/35 all declined it** —
`grep -c also_closes reports/round-3{3,4,5}/telemetry/availability-close-3*.json` → `0`, `0`,
`0`. The residual is carried, not repaired: `reports/round-35/telemetry/observed-dispatch.json`
is referenced by the snapshot's `sources` (line 20) but its own bytes
(`f7a1e1f968a3d7b212e4393e42884675299b458cb891ab5dcc397f35b01c0c53`) are pinned nowhere, and
the same is true of rounds 33 and 34. If the integrator drops `also_closes` again, the
round-36 observed record's `reason` names the snapshot that closes it (as round 33's does) and
the unpinned bytes are recorded as a carried gap rather than left silent.

`closes_sha256` is the digest **at close time**: if the integrator must edit
`dispatch-declared.json` after this fragment, the snapshot pins the post-edit digest and says
so; the rule prefers no edit (`AGENTS.md` corrections-are-new-snapshots). A round is not
admitted to `LOG.md` while this snapshot is owed (`AGENTS.md` close-what-you-open; round-35's
admission at `LOG.md:3648-3674` cites its snapshot as the closure evidence).

## 6. Template C — worker self-observation (lower bound only)

S02's own sample, filed here as text because a seat cannot write into `telemetry/`:

```json
{
  "round": 36,
  "owner": "S02",
  "observed_at_utc": "2026-10-19T09:27:47Z",
  "evidence_kind": "worker-self-observation",
  "source": "S02 received the round-36 telemetry-scribe assignment (cross claim) and is executing it; UTC observation time from date -u +%FT%TZ. No native full-wave result was supplied to this worker.",
  "sessions": [{"assignment": "S02", "state_at_observation": "active"}],
  "counts_date": "2026-10-19",
  "counting_command": "<the scratch-marker census one-liner in this section, t0 = 2026-10-19T09:20:00Z (the filed declaration stamp)>",
  "peer_marker_census": {
    "window_utc": {"start": "2026-10-19T09:20:00Z", "end": "2026-10-19T09:27:47Z", "closed": true},
    "markers": 31,
    "seat_labels_from_hyphenated_names": ["c04", "ca04", "ca05", "k02", "o06", "r02", "x01", "x02"],
    "seat_labels_from_bare_names": ["c01", "c02", "c03", "ca01", "ca02", "ca03", "d03", "d06", "k03", "p01"],
    "unattributed": ["assemble-d4-typed-7dk8y_np", "handoff-control-51qcfjjm", "handoff-control-i7rdbggb", "handoff-e2e-5buevapo", "handoff-selftest-lgk5oml4", "handoff-selftest-vrh_ditr", "iso", "r36-d07", "r36-ro1", "replay-frozen-stb27v4y", "tmpsex_v6hy"],
    "interpretation": "lower bound on concurrently active seats; not a census, not a completion count"
  },
  "scope": "One worker self-observation plus a scratch-marker lower bound; neither an independent worker census nor evidence of the actual upstream model, full-wave launch/completion count, concurrency, wall time or HTTP traffic.",
  "unavailable_owner": "Round-36 orchestrator (native dispatch/result holder)",
  "unavailable_reason": "The worker-visible round-36 claims and targets declare requests, not native execution outcomes. Full-wave dispatch metadata is not available in this worker's assigned inputs. File a new snapshot with redacted native dispatch/result extracts; do not replace this partial observation."
}
```

Census command and observed output (run by S02, window anchored on the declaration stamp
`dispatch-declared.json:5` = 2026-10-19T09:20:00Z):

```sh
python3 -B -c "import pathlib,datetime,re; t0=datetime.datetime(2026,10,19,9,20,0,tzinfo=datetime.timezone.utc).timestamp(); rows=[(datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),p.name) for p in pathlib.Path('.scratch').iterdir() if p.stat().st_mtime>=t0]; print(len(rows)); print(sorted(rows)); print(sorted({re.match(r'^([A-Za-z0-9]+?)-',n).group(1).lower() for _,n in rows if re.match(r'^([A-Za-z0-9]+?)-',n)}))"
```

- 2026-10-19T09:26:59Z → `14` markers; hyphen labels `['handoff', 'r02', 'typed']`.
- 2026-10-19T09:27:47Z (same start boundary) → `31` markers; hyphen labels add `c04`, `ca04`,
  `ca05`, `k02`, `o06`, `r36`, `replay`, `x01`, `x02`.

The count **grows** with the same window anchor (rounds 33/34/35 behaviour,
`reports/round-35/scribe/S05-telemetry-draft.md` §6); only the value printed with its instant
is meaningful. Method caveat carried from round 35: the label regex only attributes names
containing a hyphen, so the ten bare-name markers (`c01`, `c02`, `c03`, `ca01`, `ca02`, `ca03`,
`d03`, `d06`, `k03`, `p01`) appear in the name list but not in the printed label set — both
lists are filed rather than one label set. `.scratch/` is gitignored (`.gitignore:6`,
`git check-ignore -v .scratch/` → `.gitignore:6:.scratch/`), so this census is **not** a
durable evidence surface and must never be promoted into `launched_workers` /
`completed_workers`.

## 7. Findings for the integrator

- **F1 — the filed `counting_command`'s third clause is not runnable, and differently than
  round 35's.** `dispatch-declared.json:9` reads `… ; python3 seat census`. Run verbatim at
  2026-10-19T09:26Z it exits 2 with
  `python3: can't open file '/home/vgpnk/Projects/shokunin/kotodama-shokunin/seat': [Errno 2] No such file or directory`
  — there is no `seat` script or `seat/` package in the tree (`ls tools/`, `find . -maxdepth 3
  -name "seat*"` → nothing; `grep -rn "seat census" tools/ SKILL.md` → no hits). Round 35's
  third clause failed with `NameError: name 'json' is not defined` (a missing `import`);
  round 36's fails on the target file, not the import. A corrected, re-runnable form (S02,
  09:26Z) is
  `python3 -c 'import json; print(len(json.load(open("reports/round-36/targets.json"))["seats"]))'`
  → `32`. Route: the round-36 runner's telemetry leg uses the corrected form and cites this
  fragment; `dispatch-declared.json` is not edited (corrections are new snapshots).
- **F2 — `claims.json:8` files `baseline_expanded` in short form.** It reads `"ce103bf"`
  while `git rev-parse ce103bf` = `ce103bf5885af00023cdc4a174c17602476cdcf8`. Round 33 filed no
  such field; round 35 filed the full 40-hex form
  (`reports/round-35/claims.json:9` = `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`). The
  round-34/35 runners do **not** read `claims.baseline_expanded` — they expand
  `claims.baseline_commit` themselves via `git rev-parse --verify {base}^{commit}` and compare
  to a hardcoded `BASELINE_FULL`
  (`reports/round-35/run-validation.py:102-106`, `:415`; `reports/round-34/run-validation.py:95-98`).
  So a round-36 CO1 leg written on the round-35 pattern passes as long as it hardcodes
  `ce103bf5885af00023cdc4a174c17602476cdcf8`; a leg that instead asserts
  `claims.baseline_expanded == git rev-parse baseline_commit` **fails as filed**. `claims.json`
  is digest-pinned (`dispatch-declared.json:13`), so the honest route is to record the
  short-form field as a declaration-form difference (r34 CO4 style) rather than to edit it.
- **F3 — no composition string to reproduce (§2).** The r35 `seat_composition` clause
  (`reports/round-35/telemetry/dispatch-declared.json:13`) has no round-36 counterpart, so
  round 35's F1-r35 role-sub-census defect cannot recur — but also means the runner must assert
  the census against `seat_count`/`requested_workers`/the seat rows, not against a declared
  string. The r35 runner hardcodes `seat_count != 64 or len(seats) != 64`
  (`reports/round-35/run-validation.py:132-133`); round 36's must be `32/32`.
- **F4 — the declaration stamp is nominal, not a measured instant.** `claims.json:6`,
  `dispatch-declared.json:5` and `availability-attempt-1.json:5` all carry
  `2026-10-19T09:20:00Z`, while mtimes are 09:23:02Z (claims — *before* its own stamp by
  3 min 2 s), 09:23:43Z (targets), 09:24:40Z (declaration) and 09:25:45Z (attempt 1). The
  window anchor mandated for this draft is therefore the filed stamp; Template A's
  `window_basis` says so and requires the batch's own instants to come from `date -u` at
  dispatch and return. Do not compute a wall time from a nominal stamp. (Round 35's F4 is the
  same defect with a 63 s gap; it has now recurred in three consecutive rounds.)
- **F5 — `inputs/` durable copies owed.** `ls reports/round-36/telemetry/inputs` → No such file
  or directory (2026-10-19T09:26Z). Round 33, 34 and 35 all hold byte-exact copies: `cmp
  reports/round-35/claims.json reports/round-35/telemetry/inputs/claims.json` → exit 0 and the
  targets pair → exit 0 (re-verified 09:26Z). Method: copy
  `reports/round-36/{claims,targets}.json` byte-exact and re-run `cmp`; both sources end in
  `0a`.
- **F6 — the observed record's bytes are pinned nowhere, again (§5).** Rounds 33/34/35 all
  declined `also_closes`; the gap is carried, not repaired (filed bytes). Round 36 either
  adopts `also_closes` or carries the residual with the `reason`-names-the-snapshot form.
- **F7 — the closure audit still cannot see the open record.** `SKILL.md:732` globs
  `reports/round-*/availability*.json` (round-level, not `telemetry/`); run verbatim at
  2026-10-19T09:26Z it printed nothing, exit 0. Round-level matches are only
  `reports/round-{5,10}/availability-attempt-*.json` and `reports/round-{19,25,26,27,28}/availability.json`
  — none of them r36. The binding instrument is the round-36 runner's own telemetry leg (§8),
  not the audit. **Do not create a decoy `reports/round-36/availability.json`** — the
  round-30 `duplicate_evidence` control is the reason to file one record, not two.
- **F8 — fleet report owed.** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-36/` → No such
  file or directory (09:26Z); round 35's exists. Parent's artifact, owed at close. The round-35
  `leg_close` requires the four headings plus an ISO date and a `run-validation.py` citation
  (`reports/round-35/run-validation.py:321-328`).
- **F9 — no runner, no validation.json, so the closing snapshot is owed.**
  `reports/round-36/run-validation.py` and `reports/round-36/validation.json` are both absent
  (09:26Z). The runner's telemetry leg is drafted in §8 and its author owns the adoption.
- **F10 — the MANIFEST row is absent.** `/home/vgpnk/Projects/shokunin/MANIFEST.json` holds 250
  `rounds[]` entries; the last six are `[10, 11, 104, 33, 34, 35]` — no r36 row yet. The
  round-35 runner tolerates this with `manifest: "pending-by-construction"`
  (`reports/round-35/run-validation.py:330-332`); the round-36 leg should keep that tolerance
  and the integrator files the row in the close pass.
- **F11 — new round-36 negative controls, from the declared fallback (§3).**
  **`declared_provider_as_actual`** — a record whose `actual_route` reads `hyper` while the
  batch ran on devin, or whose `requested_allocation.provider_lane` was overwritten with
  `devin`; and **`fallback_unrecorded`** — a record whose `actual_route` names devin but which
  neither cites `availability-attempt-1.json` nor the `REGIMEN.md:14`/`:73-75` declared-fallback
  authority. Round 35's `attempt_failures_as_batch_failures` and `declared_lane_as_actual`
  controls both carry over unchanged.
- **F12 — F-C13-1 context.** `targets.json:8` carries the standing rule "ABSOLUTE: never run
  reports/round-*/run-validation.py in-tree (isolated git-archive copies only); any `--freeze`
  of declared-in-r7 forbidden"; the incident/prevention record is `LOG.md:3548-3562`. This
  telemetry draft executed no round runner and read only filed bytes plus the round-30/33/34/35
  records.

## 8. Counting commands and controls for the round-36 runner (draft leg)

Positive checks:

1. `sha256sum reports/round-36/claims.json reports/round-36/targets.json` equals
   `dispatch-declared.json:13,:14` (`b8d1af8f…`, `39ddbc72…`) and the observed record's
   `durable_sources`.
2. `sha256sum reports/round-36/telemetry/dispatch-declared.json` equals the snapshot's
   `closes_sha256` (`48cbee5a…`); `closes` resolves to that same path.
3. `cmp reports/round-36/claims.json reports/round-36/telemetry/inputs/claims.json` and the
   targets pair → exit 0 (round-30 control; F5).
4. §2 census: `seat_count == 32`, `len(seats) == 32`, ids unique, out paths unique, and the
   claim census partitions the 32 seats across `{D, C, Ca, cross}`. Assert **32/32**, not
   round 35's hardcoded 64/64.
5. The filed `counting_command` is re-run in its corrected form (F1) and its output recorded
   (`32`); the leg must not claim the filed string is reproducible.
6. `claims.baseline_commit` expands to `ce103bf5885af00023cdc4a174c17602476cdcf8` via
   `git rev-parse --verify ce103bf^{commit}`; if the leg also checks `claims.baseline_expanded`,
   it records the short-form difference (F2) rather than failing the round.
7. Observed record: `round == 36`, `state == "open-at-seat-close"` (or `could-not-dispatch` per
   `REGIMEN.md:73-75` if the fallback also failed), non-empty `owner` and `reason`; every null
   counter has an owner; `requested_allocation.provider_lane == "hyper"` while
   `route_deviation.actual_route` names devin; the 32 pre-batch launch failures appear only in
   the availability ledger.
8. `availability-attempt-1.json` digest in the observed record equals the live file digest
   (`ecbcdd4c…`), and its `launched_workers` is 0.
9. Snapshot: `schema == "kotodama-availability-closing-snapshot-v1"`, `round == 36`, `date`
   matches `YYYY-MM-DD`, `closes`/`closes_sha256` pin the declaration.
10. `git check-ignore -v` on the telemetry paths → no match (run 09:26Z: exit 0 with only the
    `.scratch/` line for `.scratch/`; the three telemetry paths produced no output line, i.e.
    not ignored). `git status --porcelain` shows `?? reports/round-36/` (untracked pre-commit).
11. `test -s reports/round-36/telemetry/availability-close-36.json` once
    `reports/round-36/validation.json` lands.

Negative controls to reject (round-30 name set, `reports/round-30/fixes/telemetry-convention.md:33-35`,
extended): `null_to_zero`, `invented_completion_count`, `requested_as_completed`,
`invented_served_model`, `full_wave_pass_without_extract`, `scratch_only_dependency`,
`scratch_evidence_path`, `raw_evidence_tamper`, `duplicate_evidence`,
`missing_counting_command`, `missing_counts_date`, `closing_snapshot_digest_mismatch`,
`historical_recovery_overclaim`, `declared_lane_as_actual`, `attempt_failures_as_batch_failures`,
plus the two round-36 additions in F11 (`declared_provider_as_actual`,
`fallback_unrecorded`). Round 34's `count_field_over_seat_list` control is retired again this
round because 32 == 32; if it is kept, it must pass, not be relaxed.

## Owed

- `reports/round-36/telemetry/observed-dispatch.json` — integrator lands from Template A
  (S02 may write only its own out path). Absent at 2026-10-19T09:28Z.
- `reports/round-36/telemetry/inputs/{claims,targets}.json` — byte-exact durable copies +
  `cmp` control (F5).
- `reports/round-36/telemetry/availability-close-36.json` — owed once
  `reports/round-36/validation.json` lands (Template B); the round is not admissible to
  `LOG.md` while it is owed.
- The round-36 runner's telemetry leg (§8) — owner: whichever seat/integrator authors
  `reports/round-36/run-validation.py` (absent at 09:26Z).
- F1 corrected counting command and F2 short-form `baseline_expanded` disposition — owner: the
  round-36 runner's CO/telemetry leg; `dispatch-declared.json` and `claims.json` are
  digest-pinned orchestrator files and are not edited by S02.
- F6 `also_closes` decision — integrator: adopt, or carry the residual with the
  `reason`-names-the-snapshot form.
- F8 fleet report `.ufo/reports/round-36/kotodama.md` — parent's artifact, owed at close.
- F10 MANIFEST row for round 36 — integrator, close pass.
- `to-verify`: whether the round-36 orchestrator holds a native dispatch/result extract for the
  devin fallback batch. S02 cannot see one and no fleet round-36 dir exists (F8); the counters
  in Template A stay `null` until such an artifact exists.
- `to-verify`: whether the round-36 batch actually completed on devin, or whether the fallback
  also failed (`REGIMEN.md:73-75` → `could-not-dispatch`). S02's observation window
  (09:20–09:28Z) closed before any batch result; no `validation.json` exists yet.
- `to-verify`: whether round 36's own runner tolerates the extra keys Template A/B add
  (round-35 tolerance verified at `reports/round-35/run-validation.py:336-345`; the round-36
  runner does not exist yet).

## Citations

- `reports/round-36/targets.json` — S02 seat object (`:43`, `role: scribe`, `claim: cross`,
  `mission: "Telemetry draft (observed template, closing-snapshot skeleton; window anchored on
  the dispatch stamp)."`, `out: scribe/S02-telemetry-draft.md`), `:2` `seat_count 32`, `:3-10`
  `shared_rules` (`:8` the F-C13-1 rule), `:11-43` 32 seat rows (ids_unique 32, out_unique 32).
- `reports/round-36/claims.json:5-14` — position 4 hyper + declared devin fallback, `:6`
  declared_at_utc 2026-10-19T09:20:00Z, `:7` baseline_commit `ce103bf`, `:8`
  baseline_expanded `ce103bf` (short form, F2), `:9-11` dispatch block (lane hyper, model
  deepseek-v4.1-flash, 32 workers, 1 batched call, fallback string), `:12` axes_in_play,
  `:14` freshness pause, `:15-34` the three claim objects (D/C/Ca), `:35-36` non_goals.
- `reports/round-36/telemetry/dispatch-declared.json:2-16` — record/round/owner, `:5` stamp,
  `:6-8` allocation + fallback, `:9` counting_command (F1), `:10` counting_date, `:11`
  baseline_commit, `:12-15` durable sources + digests, `:16` open closing-snapshot note.
- `reports/round-36/telemetry/availability-attempt-1.json:2-15` — `:5` stamp, `:6` route
  `hyper / deepseek-v4.1-flash`, `:7-10` 32 requested / 0 launched / 0 completed / 32 failed,
  `:11` 402 failure class, `:12` failure basis, `:13` declared-fallback disposition,
  `:14` counting_command, `:15` counting_date.
- `REGIMEN.md:14` (schedule row 4: hyper with the devin fallback), `:27-31` (1–3 claims, one
  batched swarm), `:32-34` (godspeed lead), `:41-43` (admission rule), `:53-58` (done when),
  `:66-69` (provider deviations only as declared; hyper→devin is the named one), `:73-75`
  (apply the declared fallback once; else `could-not-dispatch`).
- `AGENTS.md` — availability/dispatch telemetry rules (requested vs observed, nulls with
  owner+reason, durable paths + digests, no credentials/private payloads), "Close what you
  open", append-only corrections, F-C13-1.
- `reports/round-35/telemetry/observed-dispatch.json` (sha256
  `f7a1e1f968a3d7b212e4393e42884675299b458cb891ab5dcc397f35b01c0c53`): `state`
  open-at-seat-close, `launched_workers` 64 / `completed_workers` 64 / `failed_workers` 0,
  `observed_window_utc` 2026-10-19T08:16:00Z/2026-10-19T08:51:40Z, `actual_route` key 1.
- `reports/round-35/telemetry/availability-close-35.json` (sha256 `…`, live digest
  `93e205a2…` matching its `closes_sha256`): schema/round/date/`closes`/`closes_sha256`,
  `closed_fields`, `could_not_recover`, `sources` (line 20 names the observed record),
  `grep -c also_closes` → 0.
- `reports/round-34/telemetry/availability-close-34.json`, `reports/round-33/telemetry/availability-close-33.json`
  — the two other live snapshots; pinned == live re-verified 2026-10-19T09:28Z.
- `reports/round-35/run-validation.py:15-23` (record path constants incl. `AVAILABILITY_CLOSE`,
  `FLEET_REPORT`, `MANIFEST`, `R7_PINS`), `:102-106,:415` (baseline expansion and the hardcoded
  `BASELINE_FULL`), `:118-121` (CO5 declared-allocation check and the `route_deviation` record),
  `:127-133` (seat shape `64/64`), `:319-346` (`leg_close`: fleet-report headings at
  `:321-328`, MANIFEST tolerance at `:329-331`, declaration digest cross-check, observed-record
  reads at `:336-345`, owed-snapshot handling at `:346-347`), `:424` (close-time inputs note).
- `reports/round-34/run-validation.py:95-98,:122-126,:392` — the same baseline-expansion
  pattern, and the r34 CO4 declared-deviation form the r36 leg retires.
- `reports/round-35/scribe/S05-telemetry-draft.md` — the draft-not-measurement framing, the
  r35 F1-r35 role sub-census defect, the F2 counting-command defect, the F4 nominal-stamp
  caveat, the `also_closes` non-adoption, the label-regex method caveat.
- `reports/round-30/fixes/telemetry-convention.md:8-16` (convention + defect source), `:20`
  (stdout-capture rule), `:25-26` (the byte-exact `cmp` reproduction commands), `:34`
  (trailing-newline trap), `:33-35` (the negative-control paragraph); `reports/round-30/telemetry/control-receipt.json` (the named
  controls, incl. `declared_count_inflation`, `invented_completion_count`, `null_to_zero`,
  `scratch_only_dependency`).
- `reports/round-32/telemetry/dispatch-stats.json` — `could-not-evaluate` partial-observation
  precedent.
- `LOG.md:3548-3562` (F-C13-1 incident + prevention), `:3648-3674` (round-35 admission: the
  named route deviation, 64/64 on key 1, telemetry closed via `availability-close-35.json`).
- `SKILL.md:732` — the close-what-you-open audit one-liner (globs
  `reports/round-*/availability*.json`, keys on `closes` + `closes_sha256`); 732 lines.
- `.gitignore:6` — `.scratch/` ignored.
- Commands run by S02 (lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all
  2026-10-19T09:26:36–09:28:03Z): `date -u +%FT%TZ`; `sha256sum` + `stat -c '%n %s bytes
  mtime=%y'` on the four round-36 declaration/attempt artifacts (digests re-verified unchanged
  at 09:28:03Z); `git rev-parse HEAD` and `git rev-parse ce103bf`; `tail -c 1 | xxd -p` on
  claims/targets (both `0a`); the §2 census one-liner; the filed `counting_command` third
  clause verbatim (exit 2, `can't open file '…/seat'`) and its corrected form (`32`);
  `ls reports/round-36/telemetry/inputs` (absent); `find reports -name
  "availability-close*.json"` (8) and `find reports -name "closing-snapshot*.json"` (empty);
  `find reports -maxdepth 2 -name "availability*.json"` (round-level: r5/r10 attempts,
  r19/r25–r28 `availability.json`); `test -f` on
  `reports/round-36/{run-validation.py,validation.json}` (both absent); the verbatim
  `SKILL.md:732` audit one-liner (no output, exit 0); `grep -c also_closes` on the three live
  snapshots (`0`,`0`,`0`); a live-digest re-check of each snapshot's `closes_sha256` (all
  MATCH); `cmp` on round-35's `telemetry/inputs/` pairs (both exit 0); `git check-ignore -v`
  on the telemetry paths and `.scratch/`; `git status --porcelain` (`?? reports/round-36/`);
  the §6 scratch census one-liner twice (14 then 31 markers); `ls
  /home/vgpnk/Projects/shokunin/.ufo/reports/round-36/` (No such file or directory);
  `python3 -c` on `/home/vgpnk/Projects/shokunin/MANIFEST.json` (250 rounds entries; last six
  `[10,11,104,33,34,35]`); `wc -l LOG.md SKILL.md` (3674, 732).
