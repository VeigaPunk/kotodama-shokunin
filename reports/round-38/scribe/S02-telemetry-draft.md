- Seat: S02 | scribe | cross | date 2026-10-19 | baseline 9bccc9b

# S02 — round-38 telemetry draft: observed template, closing-snapshot skeleton, and the no-declared-fallback route

Mission (`reports/round-38/targets.json:216-220`, S02 seat object): "Telemetry draft."
Out path: `reports/round-38/scribe/S02-telemetry-draft.md`.

**This fragment drafts bytes for the integrator; it is not a measurement of the round-38
wave.** No file under `reports/round-38/telemetry/` was written or modified by this seat
(`targets.json:5`). Every JSON block below is text for the integrator to lift, per the
round-34/35/36/37 precedent (`reports/round-37/scribe/S05-telemetry-draft.md:3`).

Round-38 delta, up front — and it is a bigger one than round 36's:

1. **There is no declared fallback this round.** The r36 deviation was a *pre-declared*
   fallback (`claims.json:11` of that round named `devin/deepseek-v4-1-flash-high`);
   round 38's `claims.json:8` and `telemetry/dispatch-declared.json:6-11` name
   `xai-oauth / grok-4.7-fast` and **nothing else**. `REGIMEN.md:16` (schedule row 6) is the
   one schedule row in the table with **no fallback clause** — row 4 alone carries
   "fallback devin/deepseek-v4-1-flash-high" (`REGIMEN.md:14`). The re-dispatch onto
   devin is therefore recorded as a **named deviation**, not as a REGIMEN-authorized
   fallback (`reports/round-38/telemetry/availability-attempt-1.json:13`). §3 works this out.
2. **The seat list carries a claim id that `claims.json` does not declare.** `claims.json`
   declares two claims, `D` and `O` (`claims.json:13,19`); the seat census shows a third,
   `A` (3 seats: A01/A02/A03), plus 6 `cross` seats. First regimen-2 round with this shape
   (§2, F2).
3. **No calibration block.** The r33/r35/r37 verify rounds carried `calib/` and a `Ca`/`C`
   group; r38 is a build round with groups K/P/X/D/O/A/R/S only. A round-38 runner written
   by cloning the r37 runner will look for `calib/recount-ledger.json` and fail (§7 F8).

## 1. Declaration facts measured by S02 (durable sources)

Command (the filed `counting_command` at `reports/round-38/telemetry/dispatch-declared.json:12`,
extended with `stat`/`git`; its third clause is not runnable as written — see F1):

```sh
date -u +%FT%TZ; sha256sum reports/round-38/claims.json reports/round-38/targets.json \
  reports/round-38/telemetry/dispatch-declared.json \
  reports/round-38/telemetry/availability-attempt-1.json; \
stat -c '%n %s bytes mtime=%y' <same paths>; git rev-parse HEAD; git rev-parse 9bccc9b; \
tail -c 1 reports/round-38/claims.json | xxd -p
```

Read at 2026-10-19T11:05:06Z, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

| path | bytes | sha256 | mtime (UTC, converted from `-0300`) |
|---|---|---|---|
| `reports/round-38/claims.json` | 3164 | `45ff6f202a56704209144a6f5031a8c2f44a6dfd6ecd3d608cf26db8f793615d` | 2026-10-19T11:02:41Z |
| `reports/round-38/targets.json` | 6770 | `fe3091b91623f47211d673070f7c3d9fac3711c1375361cd27de246c10f7c601` | 2026-10-19T11:03:26Z |
| `reports/round-38/telemetry/dispatch-declared.json` | 810 | `7112af756da589ea359111feb5b2e9ef4b5266566672e16d4e46c2fca8f4599f` | 2026-10-19T11:03:26Z |
| `reports/round-38/telemetry/availability-attempt-1.json` | 1088 | `531b2dfa3b619dbba054098f27ed3335f24314ac6aca2288741c46106eb601eb` | 2026-10-19T11:04:18Z |

`git rev-parse HEAD` = `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git rev-parse 9bccc9b` =
the same 40-hex value, so `claims.json:7` and `dispatch-declared.json:14` resolve to the live
tree. `tail -c 1 | xxd -p` → `0a` for claims, targets and the declaration (trailing-newline
trap accounted for, `reports/round-30/fixes/telemetry-convention.md:34`).

**Digest cross-check: PASS.** My measured claims digest equals `dispatch-declared.json:18`
(`45ff6f20…`) and my targets digest equals `:22` (`fe3091b9…`), so the filed declaration is
bound to the same bytes this seat read. The declaration's own digest is pinned by no record
yet; S02's measurement is `7112af756da589ea359111feb5b2e9ef4b5266566672e16d4e46c2fca8f4599f`
(810 bytes). Template B uses it as `closes_sha256` **only after re-hashing at close time**
(the r37 snapshot's own warning: a point-in-time digest is not the closing digest).

**Stamp-vs-mtime (F4 carried).** `claims.json:6`, `dispatch-declared.json:5` and
`availability-attempt-1.json:5` all carry `2026-10-19T11:01:56Z`. The file mtimes are
11:02:41Z / 11:03:26Z / 11:03:26Z / 11:04:18Z — i.e. the stamp precedes every artifact by
45–142 s, the r35/r37 pattern, **not** r36's anomaly (there the claims mtime preceded its own
stamp by 3 min 2 s). The stamp remains nominal; do not compute a wall time from it.

## 2. Composition reproduction: 32 == 32, and one claim id is declared by seats but not by claims.json

Command (re-runnable; window-free):

```sh
python3 -B -c "import json,collections; t=json.load(open('reports/round-38/targets.json')); s=t['seats']; ids=[x['id'] for x in s]; print(dict(collections.Counter(i[0] for i in ids))); print('seat_count', t['seat_count'], 'seats', len(s), 'ids_unique', len(set(ids)), 'out_unique', len({x['out'] for x in s})); print('role census', dict(collections.Counter(x['role'] for x in s))); print('claim census', dict(collections.Counter(x.get('claim') for x in s)))"
```

Observed output (2026-10-19T11:05Z):

```
{'K': 2, 'P': 1, 'X': 3, 'D': 10, 'O': 8, 'A': 3, 'R': 3, 'S': 2}
seat_count 32 seats 32 ids_unique 32 out_unique 32
role census {'scout': 2, 'planner': 1, 'connector': 1, 'executor': 12, 'verifier': 7, 'scribe': 4, 'reviewer': 3, 'critic': 2}
claim census {'D': 13, 'O': 10, 'cross': 6, 'A': 3}
```

**`requested_workers` 32 equals the enumerable seat list 32.** `claims.json:8` and
`dispatch-declared.json:9` both declare 32; the seat array holds 32 rows, ids unique 32, out
paths unique 32. The round-34 CO4 deviation (63 vs 64) has no r38 analogue.

**The `A` block is not in `claims.json`.** `claims.json` declares exactly two claims, `D` and
`O` (`claims.json:12-25`), with `axes_in_play: ["depth","operability"]` (`:9`). The seat
census adds `A` (3 seats: A01/A02/A03, `targets.json:152-172`) — an adjacency block whose
claim id appears nowhere in `claims.json`, including its `non_goals` (`:26-27`). Cross-check
over the regimen-2 rounds:

| round | `claims.json` claim ids | seat claim census keys | match? |
|---|---|---|---|
| 33 | O, C, A | O, C, A, cross | yes |
| 34 | D, O, C | D, O, C, cross | yes |
| 35 | C, O, A | C, O, A, cross | yes |
| 36 | D, C, Ca | D, C, Ca, cross | yes |
| 37 | Ca, O, A | Ca, O, A, cross | yes |
| 38 | **D, O** | **D, O, A, cross** | **no — `A` undeclared** |

The `A` seats carry a claim axis (adjacency) that the round never declared in `claims.json`
and that `axes_in_play` does not list. Whatever the integrator decides, the observed record
and the runner must not silently absorb it: the honest options are (a) record it as a
declaration-form difference with the A block named as unadjudicated adjacency work, or
(b) have the runner assert the partition against `claims.json`'s declared ids and **fail**
on the extra block. Silent tolerance is the defect (§7 F2).

The group census (`K`2 `P`1 `X`3 `D`10 `O`8 `A`3 `R`3 `S`2) sums to 32. The `D` prefix count
(10) is **not** the `D` claim count (13): `K01`, `P01` and `R01` carry `claim: "D"`
(`targets.json:12-17, 26-31, 173-178`), and `D10b` begins with `D`. A prefix-based census and a
claim-based census disagree by construction this round; report both.

## 3. The route: no declared fallback, a named deviation, and two readings of the stop rule

Round 38 is the first round in this regimen whose declared lane failed **and which had no
fallback clause to fall back to**.

| fact | filed evidence |
|---|---|
| declared lane | `xai-oauth / grok-4.7-fast`, 32 workers, 1 batched call (`claims.json:8`, `dispatch-declared.json:6-11`) |
| declared fallback | **none filed** (`claims.json` has no fallback key; `dispatch-declared.json:6-11` has no `declared_fallback`; `REGIMEN.md:16` names none for position 6) |
| attempt 1 route | `xai-oauth / grok-4.7-fast (xhigh)` (`availability-attempt-1.json:6`) |
| attempt 1 result | 32 requested / **0 launched / 0 completed / 32 failed** (`:7-10`) |
| failure class | `403 out of credits (grok.com)` (`:11`), basis "all 32 seats failed at launch (agent-516..agent-547); zero started" (`:12`) |
| disposition | "position 6 carries NO declared fallback in REGIMEN.md … the batch re-dispatches on devin/deepseek-v4-1-flash-high (proven live at r36, 32/32) as a NAMED DEVIATION: owner orchestrator, reason 'grok 403 out-of-credits; no declared fallback; live-lane substitution to keep the round's claims on schedule'" (`:13`) |

Two readings of the governing text, both recorded rather than resolved by this seat:

- **`REGIMEN.md:73-75`** ("If a provider lane is exhausted or unreachable, apply the declared
  fallback once; if that also fails, file the round `could-not-dispatch` with owner + reason in
  telemetry and advance to the next scheduled round") — read strictly, position 6 has no
  declared fallback, so the rule's own route is `could-not-dispatch`, and the round should
  have advanced to position 7.
- **`REGIMEN.md:66-69`** ("Provider deviations are permitted only as declared (hyper→devin
  fallback; counts within declared ranges; skipping 402'd opencode-go keys with the failure
  recorded); **undeclared providers/models are not**") — read strictly, the devin substitution
  is exactly the class the Scope paragraph forbids.

The orchestrator took the stop rule's *intent* (keep the round's claims on schedule; the r35/r36
named-deviation precedent) and recorded the substitution in `availability-attempt-1.json:13`,
naming it a deviation rather than a fallback. **Consequence for telemetry, which is this
seat's business:** the observed record must (i) keep `requested_allocation.provider_lane`
as the declared `xai-oauth` (never overwrite it with devin), (ii) state in one explicit field
that the actual route rests on **no REGIMEN fallback clause**, and (iii) not carry a
`declared_fallback` field, because there is none to carry — an invented fallback clause would
be a fabrication. Whether the round is admissible with a recorded undeclared-provider
deviation is the integrator's and the operator's call, not a telemetry verdict; this fragment
only guarantees the record cannot be read as if a fallback had been declared.

Also note: **`availability-attempt-1.json` is the only attempt file**, so the devin batch is
attempt 2 and is the batch itself. `ls reports/round-38/telemetry/` at 11:04Z showed only
`availability-attempt-1.json` and `dispatch-declared.json`; a missing
`availability-attempt-2.json` is not a defect while the devin batch is the batch.

## 4. Template A — observed-dispatch record → `reports/round-38/telemetry/observed-dispatch.json`

Lift the round-36/37 filed shape (`reports/round-36/telemetry/observed-dispatch.json`,
`reports/round-37/telemetry/observed-dispatch.json`) and substitute round-38 values. The r37
runner reads this file with `.get` on `state`/`owner`/`reason` and tolerates extra keys
(`reports/round-37/run-validation.py:178,210`).

```json
{
  "record": "observed-dispatch",
  "round": 38,
  "state": "open-at-seat-close",
  "owner": "orchestrator (goal-mode parent)",
  "reason": "counters filled from the batched-dispatch result; the record closes when reports/round-38/telemetry/availability-close-38.json lands in the same integrating pass (AGENTS.md close-what-you-open)",
  "observed_window_utc": "<batch-dispatch instant>/<batch-return instant, both from date -u +%FT%TZ>",
  "window_basis": "the single batched AgentSwarm call that ran on the devin substitution, measured <N> s from <HH:MM:SSZ> to the batch result; the xai-oauth attempt that precedes it is excluded from the window",
  "counting_command": "AgentSwarm result summary and per-seat outcome attribute; date -u +%FT%TZ at dispatch and at return",
  "counting_date": "2026-10-19",
  "requested_allocation": {
    "provider_lane": "xai-oauth",
    "model": "grok-4.7-fast",
    "requested_workers": 32,
    "batched_calls": 1,
    "declared_fallback": null,
    "declared_fallback_basis": "NONE DECLARED — claims.json and telemetry/dispatch-declared.json carry no fallback key this round, and REGIMEN.md:16 (schedule row 6) names none, unlike row 4 at REGIMEN.md:14. The devin re-dispatch is recorded as a named deviation, not a declared fallback (availability-attempt-1.json:13)."
  },
  "route_deviation": {
    "declared_lane": "xai-oauth",
    "declared_model": "grok-4.7-fast",
    "actual_route": "devin / deepseek-v4-1-flash-high",
    "deviation_class": "NAMED DEVIATION, not a declared fallback: no fallback clause exists for position 6; the substitution was chosen by the orchestrator and recorded with owner + reason",
    "basis": "reports/round-38/telemetry/availability-attempt-1.json:7-13 — 32 seats failed at launch with 403 'out of credits' (grok.com), zero started; disposition names the deviation and re-dispatches on devin",
    "authority_claimed": "the stop rule's intent plus the r35/r36 named-deviation precedent; NOT a REGIMEN-declared fallback",
    "conformance_debt": "REGIMEN.md:66-69 forbids undeclared providers/models and REGIMEN.md:73-75 routes a failed lane with no declared fallback to `could-not-dispatch`; the orchestrator substituted and recorded instead. This is recorded conformance debt for the integrator/operator, not a telemetry pass. It is NOT laundered into a fallback.",
    "owner": "orchestrator",
    "declaration_edited": false
  },
  "pre_batch_availability_ledger": {
    "attempts": 1,
    "seats_failed_at_launch": 32,
    "seats_started": 0,
    "excluded_from_batch_counters": "true — zero seats started in attempt 1; the 32 launch failures are launch-availability evidence, not batch outcomes",
    "attempts_after_ledger": "the devin batch itself is attempt 2 and is not a pre-batch attempt; no availability-attempt-2.json is expected while the substitution succeeds",
    "files": [
      {"path": "reports/round-38/telemetry/availability-attempt-1.json", "sha256": "531b2dfa3b619dbba054098f27ed3335f24314ac6aca2288741c46106eb601eb", "route": "xai-oauth / grok-4.7-fast (xhigh)", "failure_class": "403 out of credits (grok.com)", "launched_workers": 0}
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
  "actual_route": "devin lane, wire model deepseek-v4-1-flash-high (declared xai-oauth lane returned 403 at launch on all 32 seats; substitution recorded as a named deviation with no declared-fallback clause)",
  "seat_list_reconciliation": "requested_workers 32 (dispatch-declared.json:9) equals the enumerable seat list (targets.json: seat_count 32, 32 rows, ids_unique 32, out_unique 32) — the round-34 F1 gap stays closed",
  "composition_census_note": "no composition string is filed this round (dispatch-declared.json carries no seat_composition key), so there is no declared composition to reproduce; the measured census (roles scout 2 / planner 1 / connector 1 / executor 12 / verifier 7 / scribe 4 / reviewer 3 / critic 2; claims D 13 / O 10 / cross 6 / A 3) is recorded against the seat rows alone — see scribe/S02-telemetry-draft.md §2",
  "undeclared_claim_block": {
    "claim_id": "A",
    "seats": ["A01", "A02", "A03"],
    "finding": "claims.json declares only D and O (claims.json:12-25; axes_in_play :9); the seat list carries a third claim block A (targets.json:152-172). Recorded, not absorbed — see scribe/S02-telemetry-draft.md §2 and F2.",
    "disposition": "<integrator: declaration-form difference, or runner fails on the partition>"
  },
  "post_batch_integration": "<integrator-only seats and in-session acts; round-33..37 precedent: integration acts are NOT additional craft batches>",
  "durable_sources": [
    {"path": "reports/round-38/claims.json", "sha256": "45ff6f202a56704209144a6f5031a8c2f44a6dfd6ecd3d608cf26db8f793615d"},
    {"path": "reports/round-38/targets.json", "sha256": "fe3091b91623f47211d673070f7c3d9fac3711c1375361cd27de246c10f7c601"},
    {"path": "reports/round-38/telemetry/dispatch-declared.json", "sha256": "7112af756da589ea359111feb5b2e9ef4b5266566672e16d4e46c2fca8f4599f"},
    {"path": "reports/round-38/telemetry/availability-attempt-1.json", "sha256": "531b2dfa3b619dbba054098f27ed3335f24314ac6aca2288741c46106eb601eb"},
    {"path": "reports/round-38/telemetry/inputs/claims.json", "sha256": "<must equal the claims digest above>"},
    {"path": "reports/round-38/telemetry/inputs/targets.json", "sha256": "<must equal the targets digest above>"}
  ],
  "limits": [
    "Requested allocation and requested model are declarations, not execution evidence.",
    "The declared lane (xai-oauth) is not the route used; there is NO declared fallback for this position, so the substitution is a recorded named deviation with conformance debt, and it is not an acceptance signal.",
    "32 pre-batch launch failures are availability evidence; they are neither launched nor completed workers.",
    "Null counters are unavailable, not zero; no completion rate is inferred.",
    "Provider liveness is not round acceptance.",
    "A correction is a new snapshot with its own provenance, never an in-place edit of this record."
  ]
}
```

Round-38 deltas versus the round-36 filed record, and why:

- `requested_allocation.declared_fallback` is **explicitly `null`** with a
  `declared_fallback_basis` that says *none declared*. Round 36 set this key to the devin
  string because that round had one; copying it here would fabricate a REGIMEN clause.
- `route_deviation.deviation_class` is **not** "declared fallback". It says named deviation
  and carries `conformance_debt`, because `REGIMEN.md:66-69` and `:73-75` both point at
  `could-not-dispatch` rather than at substitution. Round 36's record could say "the one
  `REGIMEN.md:14` pre-names"; round 38's cannot, and must not be made to look as though it can.
- `pre_batch_availability_ledger.files` is a single entry — only one attempt file exists —
  and carries its digest so the 32 launch failures are reproducible from a durable path.
- `undeclared_claim_block` is **new** (§2). It is the round's second declaration-shape defect
  and belongs in the observed record rather than only in this draft, because the runner's
  seat-partition leg will read the same seat list.
- Fill rules unchanged: counters only from a native dispatch/result extract the owner holds,
  filed under `reports/round-38/telemetry/`; otherwise the honest filing is
  `state: open-at-seat-close` with `null` counters, owner and reason
  (`reports/round-32/telemetry/dispatch-stats.json` precedent). Never point a
  `durable_sources` entry at `.scratch/` (`.gitignore:6`, verified: `git check-ignore -v
  .scratch/` → `.gitignore:6:.scratch/`). No credentials, authorization headers or private
  prompt payloads (`AGENTS.md:31`).

## 5. Template B — closing-snapshot skeleton → `reports/round-38/telemetry/availability-close-38.json`

Name authority is settled by filed bytes and is not re-opened: ten snapshots exist, all
`availability-close-<N>.json` (`find reports -name "availability-close*.json"` →
`{19,25,26,27,28,33,34,35,36,37}`, 2026-10-19T11:05Z); zero `closing-snapshot*.json`. All five
regimen-2 snapshots still verify: pinned `closes_sha256` == the live digest of the file its
`closes` names (33 `139b964e…`, 34 `53e2bb01…`, 35 `93e205a2…`, 36 `48cbee5a…`, 37
`d2eb583e…`, re-checked 11:05Z, all MATCH).

```json
{
  "schema": "kotodama-availability-closing-snapshot-v1",
  "round": 38,
  "date": "<date reports/round-38/validation.json lands>",
  "closes": "reports/round-38/telemetry/dispatch-declared.json",
  "closes_sha256": "<recompute at close time; 7112af756da589ea359111feb5b2e9ef4b5266566672e16d4e46c2fca8f4599f as read 2026-10-19T11:05Z>",
  "closed_fields": {
    "observed_launches": "<int|null> (read from reports/round-38/telemetry/observed-dispatch.json launched_workers, basis: <artifact>)",
    "observed_completions": "<int|null> (observed-dispatch.json completed_workers)",
    "observed_failures": "<int|null> (observed-dispatch.json failed_workers)",
    "observed_window_utc": "<start/end> (observed-dispatch.json observed_window_utc)",
    "actual_route": "devin / deepseek-v4-1-flash-high — the declared xai-oauth lane returned 403 with zero seats launched (observed-dispatch.json actual_route + route_deviation)",
    "pre_batch_availability": "1 attempt, 32 launch failures, 0 seats started; xai-oauth returned 403 'out of credits' (observed-dispatch.json pre_batch_availability_ledger, digest of availability-attempt-1.json)",
    "declared_fallback_invoked": "NONE — no fallback clause exists for position 6 (REGIMEN.md:16; claims.json and dispatch-declared.json carry no fallback key). The devin substitution is a named deviation with conformance debt recorded in observed-dispatch.json route_deviation; it is not a declared-fallback invocation.",
    "runtime_concurrency": "could-not-recover as a measured counter: null with owner orchestrator and reason recorded in observed-dispatch.json (AGENTS.md: unknown counters stay null, not inferred)",
    "seat_list_reconciliation": "requested_workers 32 == 32 enumerable seat rows (dispatch-declared.json:9, targets.json seat_count 32)",
    "composition_census": "no declared composition string this round; measured roles scout 2 / planner 1 / connector 1 / executor 12 / verifier 7 / scribe 4 / reviewer 3 / critic 2 and claims D 13 / O 10 / cross 6 / A 3 over 32 seat rows (scribe/S02-telemetry-draft.md §2)",
    "undeclared_claim_block": "seats A01/A02/A03 carry claim 'A', absent from claims.json (which declares only D and O); recorded in observed-dispatch.json undeclared_claim_block, not absorbed"
  },
  "could_not_recover": [
    "runtime_concurrency: seat-level launch telemetry is not observable from the parent process"
  ],
  "owner": "integrator (goal-mode parent), for the lane",
  "reason": "closing snapshot filed once reports/round-38/validation.json lands; every field the declaration left open is filled above, each citing the durable artifact it was read from",
  "sources": [
    "reports/round-38/telemetry/dispatch-declared.json (sha256 <re-verified at close>)",
    "reports/round-38/telemetry/observed-dispatch.json",
    "reports/round-38/telemetry/availability-attempt-1.json (sha256 531b2dfa3b619dbba054098f27ed3335f24314ac6aca2288741c46106eb601eb)",
    "reports/round-38/validation.json"
  ],
  "append_only_note": "the closed record's bytes are unchanged; this snapshot is the correction surface"
}
```

Shape authority: the schema string, `closes` on the **declaration** record, `closes_sha256`
equal to its live digest, a flat `closed_fields` map whose values carry their basis inline, and
`could_not_recover` as a list are all carried from the filed r33..r37 snapshots. `also_closes`
is again omitted: all five filed snapshots decline it
(`grep -c also_closes reports/round-3{3,4,5,6,7}/telemetry/availability-close-3*.json` → 0
each); the observed record's `reason` names the snapshot that closes it, which is the
`reason`-names-the-snapshot form r33 uses.

`closes_sha256` is the digest **at close time**. `dispatch-declared.json` is the orchestrator's
filed declaration; the rule prefers no edit (`AGENTS.md:29-31`), and if an edit is
unavoidable the snapshot pins the post-edit digest and says so. A round is not admitted to
`LOG.md` while this snapshot is owed (`AGENTS.md:37-39`); round 36's rejection and round 37's
admission both cite their snapshots as closure evidence (`LOG.md:3699-3701`, `:3721-3722`).

## 6. Worker self-observation (lower bound only)

S02's own sample, filed here as text because a seat cannot write into `telemetry/`:

```json
{
  "round": 38,
  "owner": "S02",
  "observed_at_utc": "2026-10-19T11:05:19Z",
  "evidence_kind": "worker-self-observation",
  "source": "S02 received the round-38 telemetry-scribe assignment (cross claim) and is executing it; UTC observation time from date -u +%FT%TZ. No native full-wave result was supplied to this worker.",
  "sessions": [{"assignment": "S02", "state_at_observation": "active"}],
  "counts_date": "2026-10-19",
  "counting_command": "<the scratch-marker census one-liner in this section, t0 = 2026-10-19T11:01:56Z (the filed declaration stamp)>",
  "peer_marker_census": {
    "window_utc": {"start": "2026-10-19T11:01:56Z", "end": "2026-10-19T11:05:19Z", "closed": true},
    "markers": 17,
    "names": ["d03", "o03-base", "d05", "handoff-selftest-wye7hndf", "d07", "o06", "r38-o05", "a03-iso.etqcqm", "a03-iso-path.txt", "a03-iso2.GpZ0h0", "assemble-d4-typed-7gkpgzqh", "tmp1nxhy635", "tmpizhj_eij", "family-clean-m068a8fh", "o06-tmp", "tmp1ae88k80", "tmpbkkffi1d"],
    "seat_labels_from_hyphenated_names": ["a03", "assemble", "family", "handoff", "o03", "o06", "r38"],
    "interpretation": "lower bound on concurrently active seats; not a census, not a completion count"
  },
  "scope": "One worker self-observation plus a scratch-marker lower bound; neither an independent worker census nor evidence of the actual upstream model, full-wave launch/completion count, concurrency, wall time or HTTP traffic.",
  "unavailable_owner": "Round-38 orchestrator (native dispatch/result holder)",
  "unavailable_reason": "The worker-visible round-38 claims and targets declare requests, not native execution outcomes. Full-wave dispatch metadata is not available in this worker's assigned inputs. File a new snapshot with redacted native dispatch/result extracts; do not replace this partial observation."
}
```

Census command and observed output (run by S02, window anchored on the declaration stamp
`dispatch-declared.json:5` = 2026-10-19T11:01:56Z):

```sh
python3 -B -c "import pathlib,datetime,re; t0=datetime.datetime(2026,10,19,11,1,56,tzinfo=datetime.timezone.utc).timestamp(); rows=[(datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),p.name) for p in pathlib.Path('.scratch').iterdir() if p.stat().st_mtime>=t0]; print(len(rows)); print(sorted(rows)); print(sorted({re.match(r'^([A-Za-z0-9]+?)-',n).group(1).lower() for _,n in rows if re.match(r'^([A-Za-z0-9]+?)-',n)}))"
```

- 2026-10-19T11:05:19Z → `17` markers; hyphen labels `['a03', 'assemble', 'family', 'handoff', 'o03', 'o06', 'r38']`.

Method caveats carried from r35/r36: the count grows while the window anchor stays fixed (only
the value printed with its instant is meaningful), and the label regex only attributes names
containing a hyphen, so the bare-name markers (`d03`, `d05`, `d07`, `o06`, `r38-o05`, `tmp*`)
appear in the name list but not in the label set — both lists are filed rather than one label
set. `.scratch/` is gitignored (`git check-ignore -v .scratch/` → `.gitignore:6:.scratch/`,
exit 0), so this census is **not** a durable evidence surface and must never be promoted into
`launched_workers` / `completed_workers`.

## 7. Findings for the integrator

- **F1 — the filed `counting_command`'s third clause is not runnable, for the third consecutive
  round.** `dispatch-declared.json:12` reads `… ; python3 seat census`. Run verbatim at
  2026-10-19T11:05Z it exits 2 with
  `python3: can't open file '/home/vgpnk/Projects/shokunin/kotodama-shokunin/seat': [Errno 2] No such file or directory`.
  There is no `seat` script or `seat/` package in the tree. A corrected, re-runnable form
  (S02, 11:05Z) is
  `python3 -B -c 'import json; print(len(json.load(open("reports/round-38/targets.json"))["seats"]))'`
  → `32`. Route: the round-38 runner's telemetry leg uses the corrected form and cites this
  fragment; `dispatch-declared.json` is not edited (corrections are new snapshots,
  `AGENTS.md:29-31`). The defect is now identical in r36, r37 and r38 and is worth a
  convention fix rather than a fourth note.
- **F2 — the seat list declares a claim id (`A`) that `claims.json` does not (§2).** No prior
  regimen-2 round has this shape. It is a declaration-form defect, not a seat-count defect
  (32 == 32). The runner's partition leg must either assert against `claims.json`'s declared
  ids (and then **fail** on `A`) or record the difference explicitly; the one thing it must
  not do is silently accept a superset.
- **F3 — no declared fallback, and the stop rule's strict route was `could-not-dispatch`
  (§3).** `REGIMEN.md:16` carries no fallback clause for position 6; `REGIMEN.md:66-69`
  forbids undeclared providers and `REGIMEN.md:73-75` routes a failed lane with no declared
  fallback to `could-not-dispatch`. The orchestrator substituted devin and recorded it as a
  named deviation (`availability-attempt-1.json:13`). The record must carry the conformance
  debt in a named field, and the round's admission must not present it as a
  declared-fallback round. This is the round's central telemetry item.
- **F4 — the declaration stamp is nominal, not a measured instant.** Stamp `2026-10-19T11:01:56Z`
  vs mtimes 11:02:41Z / 11:03:26Z / 11:03:26Z / 11:04:18Z (§1). Window anchor is the filed
  stamp; the batch's own instants must come from `date -u` at dispatch and return. Fifth
  consecutive round with a nominal stamp (r35/r36/r37/r38, and r34 before them).
- **F5 — `inputs/` durable copies owed.** `ls reports/round-38/telemetry/inputs` → No such file
  or directory (11:05Z). Rounds 33–37 all hold byte-exact copies; method: copy
  `reports/round-38/{claims,targets}.json` byte-exact and verify with `cmp` (both sources end
  in `0a`, so no trailing-newline trap).
- **F6 — the observed record's bytes are pinned nowhere, again (§5).** All five filed snapshots
  decline `also_closes`; the gap is carried, not repaired (filed bytes). Round 38 either adopts
  `also_closes` or carries the residual with the `reason`-names-the-snapshot form.
- **F7 — the closure audit still cannot see the open record.** `SKILL.md:732` globs
  `reports/round-*/availability*.json` (round-level, not `telemetry/`); run verbatim at
  11:05Z it printed nothing, exit 0. Round-level matches are only
  `reports/round-{5,10}/availability-attempt-*.json` and
  `reports/round-{19,25,26,27,28}/availability.json` — none of them r38. The binding
  instrument is the round-38 runner's own telemetry leg (§8), not the audit. **Do not create a
  decoy `reports/round-38/availability.json`** — the round-30 `duplicate_evidence` control is
  the reason to file one record, not two.
- **F8 — no runner and no calibration block; a cloned r37 runner will fail.** `reports/round-38/run-validation.py`
  and `reports/round-38/validation.json` are both absent (11:05Z). The r37 runner opens
  `calib/recount-ledger.json` unconditionally and asserts `len(rows) >= 30`
  (`reports/round-37/run-validation.py:86-89`), asserts `seat_count == 64 and len(seats) == 64`
  (`:80`), and asserts the allocation model equals `gpt-6-luna-max` (`:78-79`). Round 38 has
  **no `calib/` directory**, `seat_count` **32**, and model `grok-4.7-fast`. All three constants
  must change; the telemetry leg in §8 is drafted for the 32/32, no-calib shape.
- **F9 — fleet report owed.** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-38/` → No such
  file or directory (11:05Z). Parent's artifact, owed at close. The r37 `leg_close` requires
  the four headings plus an ISO date and a `run-validation.py` citation
  (`reports/round-37/run-validation.py:169-174`).
- **F10 — MANIFEST row absent; the r36/r37 rows have landed.** `/home/vgpnk/Projects/shokunin/MANIFEST.json`
  holds 252 `rounds[]` entries; the last eight are `[10, 11, 104, 33, 34, 35, 36, 37]` — no r38
  row yet, and the r36/r37 rows that r36's draft recorded as absent are now present. The r37
  runner tolerates a pending row; the round-38 leg should keep that tolerance and the
  integrator files the row in the close pass.
- **F11 — new round-38 negative controls, from the no-fallback route (§3).**
  **`invented_fallback`** — a record that carries a `declared_fallback` string (e.g. copying
  r36's devin clause) or whose `deviation_class` reads "declared fallback" when
  `REGIMEN.md:16` and both round-38 declarations carry no fallback key. And
  **`conformance_debt_laundered`** — a record or closing snapshot whose `actual_route` names
  devin but which neither names the absence of a fallback clause nor records the
  `REGIMEN.md:66-69`/`:73-75` tension. Round 35's `declared_lane_as_actual`,
  `attempt_failures_as_batch_failures` and round 36's `declared_provider_as_actual` controls all
  carry over unchanged; round 36's `fallback_unrecorded` becomes `invented_fallback` +
  `conformance_debt_laundered` here, because the failure mode inverted (r36 risked omitting a
  real fallback; r38 risks inventing one).
- **F12 — F-C13-1 context.** `targets.json:8` carries the standing rule "ABSOLUTE: never run
  reports/round-*/run-validation.py in-tree (isolated git-archive copies only); any `--freeze`
  of declared-in-r7 forbidden"; the incident/prevention record is `LOG.md:3548-3562` with the
  r36 recurrence at `:3694-3698`. This telemetry draft executed no round runner and read only
  filed bytes plus the r30/33–37 records.

## 8. Counting commands and controls for the round-38 runner (draft leg)

Positive checks:

1. `sha256sum reports/round-38/claims.json reports/round-38/targets.json` equals
   `dispatch-declared.json:18,:22` (`45ff6f20…`, `fe3091b9…`) and the observed record's
   `durable_sources`.
2. `sha256sum reports/round-38/telemetry/dispatch-declared.json` equals the snapshot's
   `closes_sha256` (re-hashed at close time; `7112af75…` as read 11:05Z); `closes` resolves to
   that same path.
3. `cmp reports/round-38/claims.json reports/round-38/telemetry/inputs/claims.json` and the
   targets pair → exit 0 (round-30 control; F5).
4. §2 census: `seat_count == 32`, `len(seats) == 32`, ids unique, out paths unique. Assert
   **32/32**, not r37's hardcoded 64/64.
5. Claim partition: `claims.json` declares `{D, O}`; the seat claim census is
   `{D, O, A, cross}`. The leg must not assert equality silently — either assert the
   `claims.json` set and fail on `A` (F2), or record the difference in the receipt.
6. The filed `counting_command` is re-run in its corrected form (F1) and its output recorded
   (`32`); the leg must not claim the filed string is reproducible.
7. `claims.baseline_commit` expands to `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` via
   `git rev-parse --verify 9bccc9b^{commit}`. `claims.json` files **no** `baseline_expanded`
   key this round (checked: `has baseline_expanded` → False), so r36's F2 short-form trap has
   no r38 analogue — a leg that reads that key must tolerate its absence rather than KeyError.
8. Observed record: `round == 38`, `state == "open-at-seat-close"` (or `could-not-dispatch`
   per `REGIMEN.md:73-75` if the integrator re-adjudicates the route), non-empty `owner` and
   `reason`; every null counter has an owner;
   `requested_allocation.provider_lane == "xai-oauth"` while `route_deviation.actual_route`
   names devin; `requested_allocation.declared_fallback` is null with its basis string; the
   32 pre-batch launch failures appear only in the availability ledger.
9. `availability-attempt-1.json` digest in the observed record equals the live file digest
   (`531b2dfa…`), and its `launched_workers` is 0.
10. Snapshot: `schema == "kotodama-availability-closing-snapshot-v1"`, `round == 38`, `date`
    matches `YYYY-MM-DD`, `closes`/`closes_sha256` pin the declaration.
11. `git check-ignore -v` on the telemetry paths → no match for the telemetry files (run 11:05Z:
    exit 0 with only the `.scratch/` line for `.scratch/`; the two telemetry paths produced no
    output line, i.e. not ignored). `git status --porcelain` shows `?? reports/round-38/`
    (untracked pre-commit).

Negative controls to reject (round-30 name set, `reports/round-30/telemetry/control-receipt.json:26-83`,
extended): `null_to_zero`, `invented_completion_count`, `requested_as_completed`,
`invented_served_model`, `full_wave_pass_without_extract`, `scratch_only_dependency`,
`scratch_evidence_path`, `raw_evidence_tamper`, `duplicate_evidence`, `missing_counting_command`,
`missing_counts_date`, `closing_snapshot_digest_mismatch`, `historical_recovery_overclaim`,
`declared_lane_as_actual`, `attempt_failures_as_batch_failures`, `declared_provider_as_actual`,
plus the two round-38 additions in F11 (`invented_fallback`, `conformance_debt_laundered`).
Round 34's `count_field_over_seat_list` control is retired again this round because 32 == 32; if
it is kept, it must pass, not be relaxed.

## Owed

- `reports/round-38/telemetry/observed-dispatch.json` — integrator lands from Template A
  (S02 may write only its own out path). Absent at 2026-10-19T11:05Z.
- `reports/round-38/telemetry/inputs/{claims,targets}.json` — byte-exact durable copies + `cmp`
  control (F5).
- `reports/round-38/telemetry/availability-close-38.json` — owed once
  `reports/round-38/validation.json` lands (Template B); the round is not admissible to `LOG.md`
  while it is owed.
- The round-38 runner's telemetry leg (§8) — owner: whichever seat/integrator authors
  `reports/round-38/run-validation.py` (absent at 11:05Z). Its three r37 constants (64/64 seats,
  `calib/recount-ledger.json`, `gpt-6-luna-max`) must change (F8).
- F1 corrected counting command — owner: the round-38 runner's CO/telemetry leg;
  `dispatch-declared.json` is a digest-pinned orchestrator file and is not edited by S02.
- F2 `A`-block disposition and F3 route adjudication — integrator/operator: record the
  undeclared claim block and the no-fallback substitution as named conformance items, or
  re-adjudicate the round. Telemetry records; it does not decide.
- F6 `also_closes` decision — integrator: adopt, or carry the residual with the
  `reason`-names-the-snapshot form.
- F9 fleet report `.ufo/reports/round-38/kotodama.md` — parent's artifact, owed at close.
- F10 MANIFEST row for round 38 — integrator, close pass.
- `to-verify`: whether the round-38 orchestrator holds a native dispatch/result extract for the
  devin substitution. S02 cannot see one and no fleet round-38 dir exists (F9); the counters in
  Template A stay `null` until such an artifact exists.
- `to-verify`: whether the devin batch actually completed, or whether it too failed (in which
  case `REGIMEN.md:73-75`'s `could-not-dispatch` and the 3-consecutive-round stop condition
  both bind). S02's observation window (11:01:56–11:05:19Z) closed before any batch result; no
  `validation.json` exists yet.
- `to-verify`: whether the round-38 runner tolerates the extra keys Templates A/B add
  (round-37 tolerance verified at `reports/round-37/run-validation.py:178,210`; the round-38
  runner does not exist yet).

## Citations

- `reports/round-38/targets.json:216-220` — S02 seat object (`role: scribe`, `claim: cross`,
  `mission: "Telemetry draft."`, `out: scribe/S02-telemetry-draft.md`); `:2` `round` 38,
  `:3` `seat_count` 32, `:4-10` `shared_rules` (`:8` the F-C13-1 rule), `:11-236` 32 seat rows
  (ids_unique 32, out_unique 32); `:161-176` the A01/A02/A03 adjacency seats.
- `reports/round-38/claims.json:6` `declared_at_utc` 2026-10-19T11:01:56Z, `:7`
  `baseline_commit` `9bccc9b` (no `baseline_expanded` key), `:8` dispatch block (lane
  xai-oauth, model grok-4.7-fast, 32 workers, 1 batched call, **no fallback**), `:9`
  `axes_in_play` `["depth","operability"]`, `:10` lowest-axis reasoning, `:11`
  `freshness_pause_in_force` true, `:12-25` the two claim objects (D, O), `:26-27` `non_goals`.
- `reports/round-38/telemetry/dispatch-declared.json:2-26` — `:2-4` record/round/owner, `:5`
  stamp, `:6-11` allocation block (provider_lane `:7`, model `:8`, requested_workers `:9`,
  batched_calls `:10`; **no fallback key**), `:12` counting_command (F1), `:13` counting_date,
  `:14` baseline_commit, `:15-24` durable sources + digests (`:18` claims, `:22` targets),
  `:25` open closing-snapshot note.
- `reports/round-38/telemetry/availability-attempt-1.json:2-16` — `:5` stamp, `:6` route
  `xai-oauth / grok-4.7-fast (xhigh)`, `:7-10` 32 requested / 0 launched / 0 completed / 32
  failed, `:11` 403 failure class, `:12` failure basis (agent-516..agent-547), `:13` the
  NAMED-DEVIATION disposition with no declared fallback, `:14` counting_command, `:15`
  counting_date.
- `REGIMEN.md:14` (schedule row 4, the only row naming the devin fallback), `:16` (schedule row
  6 — xai-oauth/grok-4.7-fast, **no fallback clause**), `:27-33` (1–3 claims; freshness
  pause), `:34-36` (one batched swarm + godspeed lead), `:41-43` (admission rule), `:52-58`
  (done when), `:66-69` (provider
  deviations only as declared; undeclared providers/models are not), `:73-75` (apply the
  declared fallback once; else `could-not-dispatch`; 3-consecutive-round stop).
- `AGENTS.md:15-31` — durable/redacted evidence, requested-vs-observed separation, null
  unknowns with owner+reason, no credentials/private payloads; `:32-39` — close-what-you-open,
  append-only closing snapshot naming the closed record and its digest at close time.
- `reports/round-36/scribe/S02-telemetry-draft.md` — the draft-not-measurement framing, the
  declared-fallback round's templates, the `declared_provider_as_actual` /
  `fallback_unrecorded` controls, the F1 counting-command defect, the F5 `inputs/` gap.
- `reports/round-37/scribe/S05-telemetry-draft.md` — the r37 template form and the
  point-in-time-vs-closing digest warning.
- `reports/round-37/telemetry/observed-dispatch.json` — the filed observed-record shape
  (`state` open-at-seat-close, 64/64/0, window 09:52:25Z/10:26:40Z, route openai-codex).
- `reports/round-36/telemetry/availability-close-36.json`, `reports/round-37/telemetry/availability-close-37.json`
  — the two most recent closing snapshots; schema, `closes`/`closes_sha256`, `closed_fields`,
  `could_not_recover`, `sources`.
- `reports/round-37/run-validation.py:78-80` (allocation/seat-shape constants a cloned runner
  would inherit — F8), `:86-89` (`calib/recount-ledger.json`, `rows >= 30`), `:169-174`
  (fleet-report path and the four required headings), `:175-179` (declaration digest
  cross-check and the optional observed-dispatch read), `:180` (the r37 closing-snapshot
  read), `:210` (close-time record list).
- `reports/round-30/fixes/telemetry-convention.md:8` (the convention), `:10` (the defect
  source), `:25-26` (byte-exact `cmp` reproduction), `:33` (the negative-control paragraph,
  "10/10 controls"), `:34` (the trailing-newline trap);
  `reports/round-30/telemetry/control-receipt.json:26-83` (the named negative controls).
- `reports/round-32/telemetry/dispatch-stats.json` — `could-not-evaluate` partial-observation
  precedent.
- `LOG.md:3548-3562` (F-C13-1 incident: the round-33 in-tree receipt rewrites, their
  restoration and the guard-adoption gap), `:3694-3698` (the r36 in-tree recurrence),
  `:3699-3701` (r36 rejection evidence incl. its closing snapshot), `:3721-3722`
  (r37 admission evidence incl. `availability-close-37.json`).
- `SKILL.md:732` — the close-what-you-open audit one-liner (globs
  `reports/round-*/availability*.json`, keys on `closes` + `closes_sha256`); 732 lines.
- `.gitignore:6` — `.scratch/` ignored.
- Commands run by S02 (lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all
  2026-10-19T11:04:49–11:05:19Z): `date -u +%FT%TZ`; `sha256sum` + `stat -c '%n %s bytes
  mtime=%y'` on the four round-38 declaration/attempt artifacts; `git rev-parse HEAD` and
  `git rev-parse 9bccc9b` (both `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`); `tail -c 1 | xxd -p`
  on claims/targets/declaration (all `0a`); the §2 census one-liner; the claim-id cross-check
  over rounds 33–38; the filed `counting_command` third clause verbatim (exit 2,
  `can't open file '…/seat'`) and its corrected form (`32`); `ls reports/round-38/telemetry/inputs`
  (absent); `test -f` on `reports/round-38/{run-validation.py,validation.json}` (both absent);
  `find reports -name "availability-close*.json"` (10) and `find reports -name
  "closing-snapshot*.json"` (empty); `find reports -maxdepth 2 -name "availability*.json"`
  (round-level only); a live-digest re-check of each filed snapshot's `closes_sha256` (all five
  MATCH); the verbatim `SKILL.md:732` audit one-liner (no output, exit 0); `git check-ignore -v`
  on the telemetry paths and `.scratch/`; `git status --porcelain` (`?? reports/round-38/`);
  the §6 scratch census one-liner (17 markers at 11:05:19Z); `ls
  /home/vgpnk/Projects/shokunin/.ufo/reports/round-38/` (No such file or directory);
  `python3 -c` on `/home/vgpnk/Projects/shokunin/MANIFEST.json` (252 rounds entries; last eight
  `[10,11,104,33,34,35,36,37]`); `wc -l REGIMEN.md AGENTS.md LOG.md SKILL.md` (77, 40, 3723, 732).
