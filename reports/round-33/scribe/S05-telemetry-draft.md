- Seat: S05 | scribe | cross | date 2026-10-19 | baseline 139e3b6

# S05 — round-33 telemetry: observed-dispatch record template + closing-snapshot skeleton

Mission (`reports/round-33/targets.json:83`): draft the observed-dispatch record template
(allocation vs observed launches/completions/failures, owner, UTC window, digests of
claims/targets) and the closing-snapshot skeleton per `AGENTS.md`; note the round-30
telemetry-durability convention. **This fragment drafts bytes for the integrator; it is not a
measurement of the round-33 wave.** No file under `reports/round-33/telemetry/` was written by
this seat (out path constraint); every JSON block below is text for the integrator to lift.

Everything in §1 and §4 is measured at the timestamps named; everything else is a template.

## 1. Declaration facts measured at S05 (durable sources)

Command (also the counting command filed in the declaration record):

```sh
date -u +%FT%TZ; sha256sum reports/round-33/claims.json reports/round-33/targets.json
```

Read 2026-10-19T03:52:51Z, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

| path | bytes | sha256 | mtime (UTC) |
|---|---|---|---|
| `reports/round-33/claims.json` | 6991 | `ba69090f90c007064fb9c08d04b2fc07ec1514eddf09937bc190021684b3fb12` | 2026-10-19T03:49:35Z |
| `reports/round-33/targets.json` | 18025 | `342c8f80eb857f96109fc7fcc3d1b816be1264898a25c3f4f8786451f27df13f` | 2026-10-19T03:50:55Z |
| `reports/round-33/telemetry/dispatch-declared.json` | 1500 | `139b964ead124364443d208cb858967b12a108532eab01b22229dfea1c1ad9ac` | 2026-10-19T03:51:23Z |

Byte-size and digest method: `len(Path(p).read_bytes())`, `hashlib.sha256(...).hexdigest()`
(round-30 artifact-hashing method, `reports/round-30/telemetry/control-receipt.json`).

**Digest cross-check: PASS.** The two declaration digests equal those already filed in
`reports/round-33/telemetry/dispatch-declared.json:20` and `:24`, so the filed declaration
record is bound to the same bytes S05 read. `dispatch-declared.json` is not yet itself pinned by
any record; its digest above is S05's measurement at 2026-10-19T03:52:51Z.

**Declaration-count cross-check (re-runnable):**

```sh
python3 -B -c "import json; t=json.load(open('reports/round-33/targets.json')); s=t['seats']; ids=[x['id'] for x in s]; g=lambda p: sum(1 for i in ids if p(i)); c={'scouts':g(lambda i:i.startswith('K')),'planners':g(lambda i:i.startswith('P')),'connector':g(lambda i:i=='X00'),'O-executors':g(lambda i:i.startswith('O')),'C-executors':g(lambda i:i.startswith('C')),'A-executors':g(lambda i:i.startswith('A')),'reviewers':g(lambda i:i.startswith('R')),'critics':g(lambda i:i.startswith('X') and i!='X00'),'scribes':g(lambda i:i.startswith('S'))}; print(c, sum(c.values())); print('A split', g(lambda i:i.startswith('A') and int(i[1:])<=10), g(lambda i:i.startswith('A') and 11<=int(i[1:])<=14), g(lambda i:i.startswith('A') and int(i[1:])>=15)); print('seat_count', t['seat_count'], 'seats', len(s), 'ids_unique', len(set(ids)), 'out_unique', len({x['out'] for x in s}))"
```

Observed output (2026-10-19T03:55Z): `{'scouts': 4, 'planners': 2, 'connector': 1,
'O-executors': 8, 'C-executors': 16, 'A-executors': 16, 'reviewers': 8, 'critics': 4,
'scribes': 5} 64`; `A split 10 4 2`; `seat_count 64 seats 64 ids_unique 64 out_unique 64`.

This **reproduces** the composition string declared at
`reports/round-33/telemetry/dispatch-declared.json:13` ("4 scouts, 2 planners, 1 connector,
8 O-executors, 16 C-executors, 16 A-executors (10 audit + 4 verify + 2 scribe), 8 reviewers,
4 critics, 5 scribes") and the requested worker count at `:11` / `claims.json:12`. Declared
allocation and the seat list agree at 64; that agreement is a *declaration* consistency check,
not execution evidence.

## 2. Template A — observed-dispatch record → `reports/round-33/telemetry/observed-dispatch.json`

The integrator lands this after the batch returns, filling only what is actually observed. Every
unobserved counter stays `null` with an owner and reason; `0` is never substituted for `null`.
Fields mirror the filed round-30/31/32 schema so the same controls apply
(`reports/round-32/telemetry/dispatch-telemetry.py:31-95`).

```json
{
  "record": "observed-dispatch",
  "round": 33,
  "state": "open-at-seat-close",
  "owner": "<round-33 orchestrator / integrator; the native dispatch+result holder>",
  "observation_kind": "<full-wave | partial-worker-observation>",
  "window_utc": {
    "start": "<earliest observed launch instant, e.g. the dispatch call timestamp>",
    "end": "<last observed completion or the batch-return instant>",
    "closed": true,
    "basis": "<command or receipt the boundaries were read from>"
  },
  "counting_command": "date -u +%FT%TZ; sha256sum reports/round-33/claims.json reports/round-33/targets.json reports/round-33/telemetry/dispatch-declared.json",
  "counting_date": "2026-10-19",
  "allocation": {
    "provider_lane": "opencode-go",
    "model": "deepseek-v4.1-flash",
    "lane_key": "opencode-go key 1 (round-robin position 1)",
    "requested_workers": 64,
    "batched_agentswarm_calls": 1,
    "seat_composition": "4 scouts, 2 planners, 1 connector, 8 O-executors, 16 C-executors, 16 A-executors (10 audit + 4 verify + 2 scribe), 8 reviewers, 4 critics, 5 scribes"
  },
  "observed": {
    "launched_workers": null,
    "completed_workers": null,
    "failed_workers": null,
    "runtime_concurrency": null,
    "actual_route": null,
    "served_model": null,
    "wall_seconds": null,
    "http_attempts": null,
    "completion_rate": null,
    "observed_worker_sessions_lower_bound": null
  },
  "unavailable_owner": "<round-33 orchestrator (native dispatch/result holder)>",
  "unavailable_reason": "<why each null is null; one reason per null or a shared reason naming the missing receipt class>",
  "durable_sources": [
    {"path": "reports/round-33/claims.json", "sha256": "ba69090f90c007064fb9c08d04b2fc07ec1514eddf09937bc190021684b3fb12"},
    {"path": "reports/round-33/targets.json", "sha256": "342c8f80eb857f96109fc7fcc3d1b816be1264898a25c3f4f8786451f27df13f"},
    {"path": "reports/round-33/telemetry/dispatch-declared.json", "sha256": "139b964ead124364443d208cb858967b12a108532eab01b22229dfea1c1ad9ac"},
    {"path": "reports/round-33/telemetry/worker-observation.json", "sha256": "<digest of the filed worker-observation record>"},
    {"path": "reports/round-33/telemetry/inputs/claims.json", "sha256": "<must equal claims.json above>"},
    {"path": "reports/round-33/telemetry/inputs/targets.json", "sha256": "<must equal targets.json above>"}
  ],
  "scratch_dependencies": [],
  "limits": [
    "Requested allocation and requested model are declarations, not execution evidence.",
    "Null counters are unavailable, not zero; no completion rate is inferred.",
    "Provider liveness is not round acceptance.",
    "A correction is a new snapshot with its own provenance, never an in-place edit of this record."
  ],
  "closing_snapshot": "open-at-seat-close: closing snapshot owed at reports/round-33/telemetry/availability-close-33.json once reports/round-33/validation.json lands"
}
```

Fill rules:
- `observed.*` may be filled **only** from a native dispatch/result extract the owner holds
  (per-seat attempt IDs and outcomes, or an equivalent receipt). File that extract under
  `reports/round-33/telemetry/` too — "the redacted raw samples or native dispatch/result
  extracts needed to reproduce every reported count" (`AGENTS.md:18-20`).
- No credentials, authorization headers, or private prompt payloads anywhere in the record
  (`AGENTS.md:29-31`).
- `observed_worker_sessions_lower_bound` is the only counter a seat can honestly fill from
  inside the wave; see §4 for S05's own sample.
- If the orchestrator holds nothing native, `observation_kind` is
  `partial-worker-observation`, all `observed.*` stay `null`, and `unavailable_reason` names the
  round-33 orchestrator as the owner of the missing receipts — the round-30/31/32 precedent
  (`reports/round-32/telemetry/dispatch-stats.json`, `"full_wave_status":
  "could-not-evaluate"`).

## 3. Template B — closing-snapshot skeleton → `reports/round-33/telemetry/availability-close-33.json`

Rule: `AGENTS.md:32-38` ("Close what you open", landed 2026-10-18 per
`reports/round-31/jinii/draft.md:27-35`). Filed shape precedent:
`reports/round-25/telemetry/availability-close-25.json:2` (`schema:
kotodama-availability-closing-snapshot-v1`) and `reports/round-28/telemetry/availability-close-28.json`.
Shape below follows the r31 draft (`reports/round-31/jinii/draft.md:59-76`) because it carries
per-value basis + command, which the r31 runner's integrity checks accept
(`reports/round-31/run-validation.py:792-816`: `date` present, `closes` resolvable,
`closes_sha256` equal to the live digest, closed record unchanged at HEAD).

```json
{
  "schema": "kotodama-availability-closing-snapshot-v1",
  "round": 33,
  "kind": "availability-close-snapshot",
  "date": "<date reports/round-33/validation.json lands>",
  "closes": "reports/round-33/telemetry/dispatch-declared.json",
  "closes_sha256": "139b964ead124364443d208cb858967b12a108532eab01b22229dfea1c1ad9ac",
  "state_before": "open-at-seat-close",
  "closed_fields": {
    "launched_workers": {"value": "<int|null>", "basis": "<durable artifact read>", "command": "<counting command>", "date": "<date>"},
    "completed_workers": {"value": "<int|null>", "basis": "<durable artifact read, e.g. the round-33 LOG.md admission line>", "command": "<counting command>", "date": "<date>"},
    "failed_workers": {"value": "<int|null>", "basis": "<durable artifact read>", "command": "<counting command>", "date": "<date>"},
    "acceptance_verdict": {"value": "<accepted|rejected>", "source": "reports/round-33/validation.json"}
  },
  "could_not_recover": [
    {"field": "actual_concurrency", "reason": "<reason>", "evidence": "<durable path>"},
    {"field": "wall_clock_seconds", "reason": "<reason>", "evidence": "<durable path>"},
    {"field": "http_traffic", "reason": "<reason>", "evidence": "<durable path>"}
  ],
  "owner": "kotodama-shokunin (round-33 integrator)",
  "reason": "<one line: where each filled count was read from>",
  "sources": ["reports/round-33/validation.json", "reports/round-33/telemetry/dispatch-declared.json", "<LOG.md if read>"],
  "validation_sha256": "<sha256 of reports/round-33/validation.json>",
  "rule": "AGENTS.md:32-38 (Close what you open), landed per reports/round-31/jinii/draft.md:27-35",
  "append_only_note": "the closed record's bytes are unchanged; this snapshot is the correction surface"
}
```

Notes binding on the integrator:
- `closes_sha256` is the digest of `dispatch-declared.json` **at close time**. If that file is
  ever edited, the snapshot must pin the new digest — but the rule prefers no edit at all;
  corrections belong in new snapshots (`AGENTS.md:26-28`).
- The r25–r28 filed snapshots use a flat `closed_fields` map plus a top-level `reason`; the r31
  draft nests `{value, basis, command, date}`. Both pass the r31 runner. Pick one and keep every
  filled value citing its source.
- A round is not admitted to `LOG.md` while this snapshot is still owed (`AGENTS.md:35-36`).
- **Naming (see F2, reconciled with S04 and K01):** file
  `reports/round-33/telemetry/availability-close-33.json` — the landed convention of the five
  filed closures (`reports/round-{19,25,26,27,28}/telemetry/availability-close-N.json`) and the
  name both filed runners recognize (`reports/round-31/run-validation.py:780,:792`,
  `reports/round-32/run-validation.py:221-223`). Do **not** additionally file a
  `closing-snapshot.json`: the `SKILL.md:713-715` checklist one-liner hardcodes that literal name,
  which exists nowhere in the repo, so it false-fires on five already-closed records today
  (`corpus/lessons/round-32.md:41` F-X16-3; reproduced by `op/K01-falsifier-scout.md:23,:56` and
  `scribe/S04-integration-draft.md:544-556`). A decoy second file would satisfy a broken
  instrument and trip the round-30 `duplicate_evidence` control — the fix belongs in the
  SKILL.md amendment draft at F2.
- **Key name:** the filed schema key is `closes` (live,
  `reports/round-25/telemetry/availability-close-25.json:5`), not `closes_record` as the round-32
  lesson's prose has it (`corpus/lessons/round-32.md:41`); the scout records the divergence at
  `op/K01-falsifier-scout.md:82-85` (live schema `reports/round-19/telemetry/availability-close-19.json:4`,
  reader `reports/round-31/run-validation.py:799`) — use `closes`.

## 4. Template C — worker-observation record (lower bound only) → `reports/round-33/telemetry/worker-observation.json`

S05's own measured sample, filed here because a seat cannot write into `telemetry/`:

```json
{
  "round": 33,
  "owner": "S05",
  "observed_at_utc": "2026-10-19T03:55:16Z",
  "evidence_kind": "worker-self-observation",
  "source": "S05 received the round-33 telemetry-scribe assignment (cross claim) and is executing it; UTC observation time from date -u +'%Y-%m-%dT%H:%M:%SZ'. No native full-wave result was supplied to this worker.",
  "sessions": [{"assignment": "S05", "state_at_observation": "active"}],
  "counts_date": "2026-10-19",
  "counting_command": "<the peer-marker census command in this section>",
  "peer_marker_census": {
    "window_utc": {"start": "2026-10-19T03:52:11Z", "end": "2026-10-19T03:55:16Z", "closed": true},
    "markers": 23,
    "distinct_seat_labels": ["c01", "c05", "c13", "k02", "o01", "o06", "o08", "p01", "r01", "r02", "r03"],
    "unattributed": ["gate-r21.py"],
    "interpretation": "lower bound on concurrently active seats; not a census, not a completion count"
  },
  "scope": "One worker self-observation plus a scratch-marker lower bound; neither an independent worker census nor evidence of the actual upstream model, full-wave launch/completion count, concurrency, wall time or HTTP traffic.",
  "unavailable_owner": "Round-33 orchestrator (native dispatch/result holder)",
  "unavailable_reason": "The worker-visible round-33 claims and targets declare requests, not native execution outcomes. Full-wave dispatch metadata is not available in this worker's assigned inputs. File a new snapshot with redacted native dispatch/result extracts; do not replace this partial observation."
}
```

Census command and observed output (2026-10-19T03:55:16Z, run by S05):

```sh
python3 -B -c "import pathlib,datetime,re; t0=datetime.datetime(2026,10,19,3,45,tzinfo=datetime.timezone.utc).timestamp(); rows=[(datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),p.name) for p in pathlib.Path('.scratch').iterdir() if p.stat().st_mtime>=t0]; print(len(rows)); print(sorted(rows)); print(sorted({re.match(r'^([a-z0-9]+?)-',n).group(1) for _,n in rows if re.match(r'^([a-z0-9]+?)-',n)}))"
```

Output: `23` markers; times 2026-10-19T03:52:11Z … 2026-10-19T03:55:16Z; labels
`['c01','c05','c13','gate','k02','o01','o06','o08','p01','r01','r02','r03']` (12 labels, of
which `gate` is unattributed to a seat id). Markers seen include `k02-c31-census.json`,
`o08-audit-before.json`, `o01-c31.json`, `r02-audit.json`, `r01-battery.json`,
`c13-consistency-check.py`, `o06-controls.py`, `p01-mirror/`, `r03-controls/` — i.e. seats from
all four claim groups are visibly running. **Honest limit:** these are scratch artifacts;
`.scratch/` is gitignored (`.gitignore:6`) and is not a durable evidence surface, so this census
must never be filed as the round-33 record — it is only the reason S05 can say "≥11 seat labels
were active in the window", never "N of 64 completed".

The census command is window-anchored (`mtime >= 2026-10-19T03:45Z`), so its count **grows** as
the wave continues: a re-run at 2026-10-19T03:58Z printed `41` markers over the same start
boundary, and a third run later still printed `54`. Only the value at the timestamp printed with
it is meaningful; never re-quote a later count as if it were the observation above.

## 5. Round-30 telemetry-durability convention — what binds round 33

- **Where records live:** `reports/round-<N>/telemetry/`, never only `.scratch`
  (`AGENTS.md:17-20`). For this round that means every sample lands under
  `reports/round-33/telemetry/`; the scratch-only storage pattern is exactly the defect the
  round-30 convention fixed (`reports/round-30/fixes/telemetry-convention.md:8`, source defect
  `reports/round-29/devin-availability-disposition.md:3-22`).
- **Durability proof:** round-30 required byte-exact durable copies of the declarations under
  `telemetry/inputs/` plus `cmp` controls (`reports/round-30/fixes/telemetry-convention.md:12`,
  `:34`); r31/r32 both carry `telemetry/inputs/{claims,targets}.json`. **Round 33 has no
  `telemetry/inputs/` yet** (F4).
- **Distinguish requested from observed:** requested allocation/model stay separate from
  launched/completed/failed/route (`AGENTS.md:21-25`).
- **Nulls stay null** with an owner and reason; no inferred zeroes, no completion rate
  (`AGENTS.md:25-27`; round-32 filed the same policy at
  `reports/round-32/telemetry/dispatch-stats.json`).
- **Corrections are new snapshots**; filed rounds are never rewritten (`AGENTS.md:26-28`).
- **No credentials/headers/private prompts** in telemetry (`AGENTS.md:29-31`).
- **Captures print to stdout**; never redirect a fresh capture over a filed snapshot
  (`reports/round-30/fixes/telemetry-convention.md:29-31`).
- **Durability is not acceptance:** provider liveness ≠ round acceptance (`AGENTS.md:27-28`;
  `reports/round-30/fixes/telemetry-convention.md:8`).
- Not-ignored check (run 2026-10-19T03:55Z): `git check-ignore -v
  reports/round-33/telemetry/dispatch-declared.json` → exit 1 (no match), so telemetry records
  are committable; `.scratch/` matches at `.gitignore:6`.

## 6. Findings for the integrator (each with evidence)

- **F1 — the round-33 open record is invisible to the landed closure audit.** The record is
  `reports/round-33/telemetry/dispatch-declared.json`; it declares openness only as a prose
  string, `"closing_snapshot": "open-at-seat-close: ..."` (`dispatch-declared.json:28`), and has
  no `"state"` field. The landed audit command (`reports/round-31/jinii/draft.md:43`) globs
  `reports/round-*/availability*.json`, and `python3 -c "import glob;
  print(glob.glob('reports/round-33/availability*.json'))"` returns `[]` (2026-10-19T03:55Z).
  Run at the same time, that audit prints exactly `reports/round-19/availability.json` and
  `reports/round-{25,26,27,28}/availability.json` — nothing for round 33. **Recommendation:**
  the observed-dispatch record carries `"state": "open-at-seat-close"` (Template A does), the
  round-33 `run-validation.py` implements its own telemetry leg (S04's leg spec) because the
  filed audit cannot see this record, and the integrator may additionally file
  `reports/round-33/availability.json` as the record the filed audit can see — never instead of
  the telemetry-dir record.
- **F2 — closing-snapshot filename: three landed surfaces disagree; corrected against S04.**
  S04's integration draft reached the same question independently and is right about the live
  audit (`reports/round-33/scribe/S04-integration-draft.md:185-187`); this seat's first pass named
  the wrong file. Evidence, all measured 2026-10-19T03:58–04:00Z:
  - **The landed checklist** (`SKILL.md:713-715`) hardcodes
    `os.path.exists(.../telemetry/'closing-snapshot.json')` — run verbatim now, it still prints
    `reports/round-19/availability.json`, `reports/round-{25,26,27,28}/availability.json` (exit 0).
    So the five filed retroactive closures never satisfied the landed checklist.
  - **The filed runners** only recognize the other name: `reports/round-31/run-validation.py:780`
    builds `availability-close-<N>.json`, `:792` globs `telemetry/availability-close*.json`, and
    `reports/round-32/run-validation.py:221-223` sanctions only `"/telemetry/availability-close-"`
    as a new protected path (the r31 jinii draft's proposed §2.2 text,
    `reports/round-31/jinii/draft.md:43`, has no `closing-snapshot.json` clause — the landed
    checklist added it).
  - **On disk** there are exactly five snapshots, all `availability-close-*.json`
    (`find reports -name "availability-close*.json"`), and zero `closing-snapshot.json`
    (`find reports -name "closing-snapshot*.json"` → empty).
  **Recommendation (reconciled with S04's corrected note and K01's scout finding):**
  1. **File the snapshot at `reports/round-33/telemetry/availability-close-33.json`** — the landed
     convention of the five filed closures and the name both filed runners recognize
     (`reports/round-31/run-validation.py:780,:792`,
     `reports/round-32/run-validation.py:221-223`). S04 reached this name independently and
     corrected its §4 note in place to it (`reports/round-33/scribe/S04-integration-draft.md:185-193,:536-556`).
     File **one** copy only — a decoy `closing-snapshot.json` would satisfy a broken instrument
     and trip the round-30 `duplicate_evidence` control
     (`reports/round-30/telemetry/control-receipt.json`).
  2. **Do not treat the `SKILL.md:715` one-liner as the name authority.** It hardcodes a filename
     that exists nowhere in the repo (`find reports -name "closing-snapshot*.json"` → empty) and
     therefore false-fires on five already-closed records — the round-32 lesson's finding
     **F-X16-3** (`corpus/lessons/round-32.md:41`) with its open route **Q-32-1** (`:55`),
     reproduced by `op/K01-falsifier-scout.md:23,:56` and independently by
     `reports/round-33/scribe/S04-integration-draft.md:544-556`. The lesson records that the
     rule's own falsification clause (i) has already fired *instrumentally*, with the substantive
     check passing 5/5.
  3. **Bounded fix draft for the integrator** (the integrator applies SKILL.md changes; seats never
     edit it). Before → after, in the landed checklist item `SKILL.md:713-715`:
     - before: `... and not os.path.exists(os.path.join('reports',f.split('/')[1],'telemetry','closing-snapshot.json'))]"`
     - after: `... and not glob.glob(os.path.join('reports',f.split('/')[1],'telemetry','availability-close*.json'))]"`
     Rationale: re-key the instrument to the convention its own first execution produced (five
     `availability-close-N.json` snapshots, `schema: kotodama-availability-closing-snapshot-v1`,
     keys `closes` + `closes_sha256`) instead of rewording the falsification clause; the scout
     records the same disposition choice at `op/K01-falsifier-scout.md:120-125`. Post-amendment
     control: the amended one-liner must print nothing (0 rows) while the pre-amendment form still
     prints the 5 rows — both runnable at the same instant, which is the falsifiable delta.
  4. **If the operator prefers zero SKILL.md edits this round,** carry the item as
     carried-with-owner (parent/operator) + reason (F-X16-3 / Q-32-1 is operator-owned per the
     lesson) + next touch — never absorb it by filing a decoy file, and never claim the round-33
     snapshot cleared an instrument that cannot see it.
  Residual surface conflict for the integrator to route: the checklist's literal name and the
  runners' glob are mutually unsatisfiable by one file; rounds 8–31 are filed and are not
  rewritten (r32's `PROTECTED` tuple covers rounds 8–31,
  `reports/round-32/run-validation.py:48`), so the amendment in item 3 is the only fix that keeps
  the rule's substance intact.
- **F3 — digest pin available now.** `dispatch-declared.json` sha256 =
  `139b964e…c1ad9ac` (S05 measurement, 2026-10-19T03:52:51Z). Template B pins it; if the
  integrator must edit that file, the snapshot pins the post-edit digest and says so.
- **F4 — durable declaration copies owed.** `reports/round-33/telemetry/inputs/` does not exist
  (`ls` → No such file or directory, 2026-10-19T03:5xZ), so round 33 has not yet run the
  round-30 `cmp` durability control. Land `inputs/claims.json` and `inputs/targets.json`
  byte-exact (watch the trailing-newline trap recorded at
  `reports/round-30/fixes/telemetry-convention.md:34`).
- **F5 — the only worker-fillable counter is a lower bound.** See §4. Do not promote the scratch
  census into `launched_workers`/`completed_workers`.
- **F6 — full-wave counters need native extracts or stay null.** No seat in this batch holds
  them; the declaration itself says the observed record is "a separate observed-dispatch record
  after the batch returns" (`dispatch-declared.json:6-7`). If the orchestrator lands no native
  extract, the honest filing is `observation_kind: partial-worker-observation` +
  `could-not-evaluate` + owner + reason (round-30/31/32 precedent).
- **F7 — claim counting command still unmet elsewhere.** Claim O's third counting command is
  `test -s reports/round-33/op/O05-falsifier-disposition.md` (`claims.json` claim O); that path
  did not exist at 2026-10-19T03:55Z. Not a telemetry matter — flagged so the round-33
  validation leg does not silently assume it.

## 7. Counting commands and controls for the round-33 runner (draft leg)

Positive checks (each must pass on the delivered revision):

1. `sha256sum reports/round-33/claims.json reports/round-33/targets.json` equals the digests in
   `dispatch-declared.json:20,:24` and in the observed record's `durable_sources`.
2. `python3 -B -c "<§1 composition command>"` prints 64 and the composition matching
   `dispatch-declared.json:13`.
3. `cmp reports/round-33/claims.json reports/round-33/telemetry/inputs/claims.json` and the
   targets pair → exit 0 (round-30 control, `reports/round-30/fixes/telemetry-convention.md:36-37`).
4. Closing-snapshot integrity (r31 method, `reports/round-31/run-validation.py:800-816`):
   `closes` resolves; `sha256(closes) == closes_sha256`; `git show HEAD:<closes>` bytes equal
   live bytes; `date` present.
5. `git check-ignore -v reports/round-33/telemetry/observed-dispatch.json` → exit 1.
6. `git status --porcelain -- reports/round-1..32 tools/gates/frozen` → no additions/changes
   beyond the sanctioned closing snapshot named in F2
   (`reports/round-33/telemetry/availability-close-33.json`).
7. Closing-snapshot presence leg (F2 item 1): `test -s
   reports/round-33/telemetry/availability-close-33.json` once
   `reports/round-33/validation.json` lands.
8. Checklist-instrument leg (F2 item 2): run the verbatim `SKILL.md:715` one-liner and expect it
   to still print the 5 pre-existing rows; do **not** record that as a round-33 failure — the
   instrument is the defect (F-X16-3). If the F2 item-3 amendment lands, the amended one-liner is
   the leg instead and must print nothing.

Negative controls the runner must reject (names follow the round-30 control set,
`reports/round-30/telemetry/control-receipt.json`):

| control | planted defect | expected rejection |
|---|---|---|
| `null_to_zero` | `failed_workers: 0` with no native extract | unsupported runtime measurement |
| `invented_completion_count` | `completed_workers: 64` (= requested) with no extract | unsupported runtime measurement |
| `requested_as_completed` | `completion_rate` derived from declarations | unsupported derived counter |
| `invented_served_model` | `served_model` filled from the request | unsupported runtime measurement |
| `full_wave_pass_without_extract` | `state`/`full_wave_status: passed` with null counters | unsupported full-wave pass |
| `scratch_only_dependency` | record whose only evidence path is under `.scratch/` | scratch-only telemetry dependency |
| `scratch_evidence_path` | any `durable_sources` entry under `.scratch/` | non-durable evidence path |
| `raw_evidence_tamper` | `inputs/claims.json` mutated after digesting | raw evidence hash mismatch |
| `duplicate_evidence` | same path listed twice | duplicate evidence path |
| `missing_counting_command` / `missing_counts_date` | field dropped | missing counting command/date |
| `closing_snapshot_digest_mismatch` | edit the closed record after snapshotting | digest mismatch = rule falsified as implemented |
| `historical_recovery_overclaim` | snapshot claiming recovery of an earlier round's samples | historical telemetry was not recovered |

## Owed

- `reports/round-33/telemetry/observed-dispatch.json` — integrator lands from Template A (S05 may
  not write outside `reports/round-33/scribe/S05-telemetry-draft.md`).
- `reports/round-33/telemetry/inputs/{claims,targets}.json` — byte-exact durable copies + `cmp`
  control (F4).
- `reports/round-33/telemetry/availability-close-33.json` — owed once
  `reports/round-33/validation.json` lands (Template B, name per F2); the round is not admissible
  to `LOG.md` while it is owed.
- `reports/round-33/telemetry/observed-dispatch.json` naming note: Template A is the record the
  round-33 runner's telemetry leg should read; `dispatch-declared.json` alone is not enough (F1).
- The round-33 `run-validation.py` telemetry leg (§7 is the draft spec; S04 owns the leg list and
  its table carries leg `X3` for telemetry digests — re-locate it by leg id in S04's landed
  revision, which was rewritten during the wave; `reports/round-33/run-validation.py` did not
  exist at 2026-10-19T03:55Z).
- The SKILL.md amendment in F2 item 3 — integrator-applied shared-file change, or carried with
  owner + reason if the operator prefers no SKILL.md edit this round.
- Cross-reference: S04's integration draft landed during this wave and S05 read it at
  2026-10-19T04:00Z; F2 above is the reconciled correction, and §7's leg spec is aligned with its
  `X3`. X02's conformance findings and A03's scope-watch counts had not landed at that time, so
  no statement here depends on them.
- `to-verify`: whether the round-33 orchestrator holds a native dispatch/result extract; S05
  cannot see one, and no fleet report for round 33 existed at 2026-10-19T03:55Z
  (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-33/` → No such file or directory).

## Citations

- `AGENTS.md:15-38` — availability/dispatch telemetry rules incl. "Close what you open".
- `.gitignore:6` — `.scratch/` ignored (non-durable).
- `REGIMEN.md` — 3×14 regimen, round-33 schedule row, per-round record requirements.
- `reports/round-33/targets.json:3,:83` — `seat_count: 64`; S05 seat object.
- `reports/round-33/claims.json:6,:8,:10-14,:16,:18` — declared_at_utc, baseline_commit, dispatch
  allocation, axes, freshness pause.
- `reports/round-33/telemetry/dispatch-declared.json:6-7,:8-13,:15,:17-26,:28` — declaration
  record: window note, allocation, counting command, durable sources + digests, closing-snapshot
  note.
- `reports/round-30/fixes/telemetry-convention.md:8,:12,:29-34,:36-37` — the durability
  convention, byte-exact `inputs/` copies, stdout-capture rule, `cmp` controls.
- `reports/round-30/telemetry/control-receipt.json` — 11 named negative controls; artifact
  hashing method.
- `reports/round-30/telemetry/dispatch-declaration-x37.json:12-14,:60-64` — declaration-only
  scope, runtime could-not-evaluate, follow-up wording.
- `reports/round-31/jinii/draft.md:27-35,:43,:59-76` — closure-rule text, audit command,
  snapshot shape.
- `reports/round-31/run-validation.py:792,:800-816` — snapshot glob and integrity checks.
- `reports/round-32/run-validation.py:48,:221-223` — `PROTECTED` tuple; sanctioned
  `availability-close-` exception.
- `reports/round-32/telemetry/dispatch-telemetry.py:31-95` — observed-record schema and limits.
- `reports/round-32/telemetry/dispatch-stats.json`, `reports/round-32/telemetry/worker-observation.json`
  — filed partial-observation precedent (nulls + owner + reason).
- `reports/round-25/telemetry/availability-close-25.json:2`, `reports/round-28/telemetry/availability-close-28.json`
  — filed closing-snapshot schema.
- `SKILL.md:713-715` — landed checklist item and the audit command hardcoding
  `telemetry/closing-snapshot.json` (run verbatim by S05 2026-10-19T04:00Z: five rows, r19 +
  r25–r28, exit 0).
- `corpus/lessons/round-32.md:41,:55` — F-X16-3 (the audit false-fires; its falsification clause
  fired instrumentally) and route Q-32-1; the lesson file is read-only to this seat.
- `reports/round-33/op/K01-falsifier-scout.md:6-8,:20-27,:33-56,:82-85,:118-125` — located and
  reproduced F-X16-3; `closes` vs `closes_record` divergence; the two disposition options.
- `reports/round-33/scribe/S04-integration-draft.md:185-193,:536-556` — independent reproduction
  and the corrected filename recommendation (read by S05 at 2026-10-19T04:00Z; the fragment was
  revised during the wave, so F2 pins the reconciled position rather than S04's first pass).
  S04's leg `X3` (`:355-357,:425` in the pre-revision cut; re-locate by leg id in the landed
  revision) is the telemetry-digest leg this seat's §7 aligns with.
- Commands run by S05 (all at 2026-10-19T03:52–04:00Z, lane root, `TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `date -u +%FT%TZ`; `sha256sum reports/round-33/{claims,targets}.json
  reports/round-33/telemetry/dispatch-declared.json`; the §1 composition one-liner; the §4 scratch
  census one-liner (re-run once at 03:59Z to confirm it grows); the r31 §2.2 audit one-liner and
  the `SKILL.md:715` audit one-liner; `find reports -name "closing-snapshot*.json"` (empty) and
  `find reports -name "availability-close*.json"` (five files); `git check-ignore -v …`;
  `git ls-files | wc -l` (= 2655); `git rev-parse HEAD`
  (= `139e3b662900557afe54f632b468619593dc9fcb`).
