- Seat: S04 | scribe | cross | date 2026-10-19 | baseline da68a6d

# S04 — round-34 integration dossier draft + validation-leg spec

Purpose: give the integrating parent (a) the fleet-report draft text for
`../.ufo/reports/round-34/kotodama.md` and (b) a machine-checkable leg spec it
implements as `reports/round-34/run-validation.py`. Every value in §8 was
measured by this seat at the round-34 tree on 2026-10-19 with the commands in
§8; every value keyed to a fragment path is a placeholder the integrator fills
from the landed fragment.

Dependency state at this seat's cut (2026-10-19): `reports/round-34/` contains
only `claims.json`, `targets.json` and `telemetry/dispatch-declared.json`
(measured, §8 M1). **All 63 declared seat fragments were unwritten** at that cut,
including every one this draft would otherwise quote; `../.ufo/reports/round-34/`
does not exist (§8 M13). §10 supersedes this paragraph with the landed-fragment
cross-check (51 of 63 landed at its read). Every `{{...}}` token below is
therefore an owed fill listed in `## Owed`. §9 records three declaration-level
defects this seat found while measuring — they change what the validator may
assert and must be read before implementing §6.

**Non-author declaration:** this seat authored no lane artifact before this
round. No promotion, canon, clearance, or closure verdict is claimed anywhere in
this file; each such token appears only as a negation, a routed reference, or a
quoted pattern (§6.6).

---

## §1 — Fleet-report draft (four required sections)

Heading set required by the filed contract (`reports/round-33/run-validation.py:70-75`,
`SECTIONS`): `Work performed`, `Landed changes`, `Before → after measurements`,
`SHONEN`. Reuse the same regex pair for round 34.

### Draft header

```text
# kotodama — round 34 report (2026-10-19)

Regimen 2 (REGIMEN.md:13), loop 1, build 2 of 3. One 64-seat batched AgentSwarm
on `opencode-go-2 / deepseek-v4.1-flash` (key 2 of the per-round round-robin).
Declared baseline `da68a6d705e41f369f21e8607bfaab5b54077f84`
(claims.json:8 short id `da68a6d`, resolved — §8 M4); this round's work lands in
the same integrating pass that files this report. Claims D/O/C on
depth/operability/calibration (claims.json:17,20-66); freshness axis-move claims
stay paused (claims.json:18). Dispatch honesty: allocation is declared at
`reports/round-34/telemetry/dispatch-declared.json` (digest-pinned); observed
launches/completions/failures are `{{counts or null}}` — {{owner}} — with the
closing snapshot owed once validation.json lands (AGENTS.md:32-39). Seat
accounting: 63 seat rows are declared against `seat_count: 64` and 64 requested
workers (§9 item 1) — reported, not rounded.
```

### Draft — Work performed

```text
- **Depth (claim D):** handoff packet v-next. `reports/round-34/handoff/
  declared-in-r7/` regenerates the v3 packet from the live D2/D3/D4 artifacts,
  rewriting the claim-ledger and OQ prose to live numbers; the pair freezes with
  `expected.json` + `freeze.txt` + a tamper control, and the renderer default
  moves to the new revision with the re-pin cascade landed as **new** rows
  (filed r2/r4/r5/r6 and r8–r33 packet bytes untouched). Before: the declared
  default (`tools/exercise-handoff-e2e.py:1933-1934`) pins the round-30
  `declared-in-r6` pair, which is shape-green — `fields=16/16
  glossary-entries=20 findings=0`, exit 0 (measured, §8 M6) — but semantically
  stale at five sites (`packet.md:148,149,150,152,307`; §9 item 3). After:
  `{{every claim-ledger/OQ figure equals a measured live value}}`. {{D01-D16
  pointers}}.
- **Operability (claim O):** capability acquisition. `tools/harness/
  receipt_guard_adoption.py` inventories every filed round runner, classifies
  whether it writes its own `validation.json` in place and whether it adopts
  `tools/harness/receipt_guard.py`, and files the durable F-C13-1 routing
  inventory. Before: 28 filed runners and 27 filed `validation.json` (§8 M10),
  no inventory instrument. After: `{{inventory covers 28/28; classes per §9
  item 2}}`. {{O01-O05 pointers}}.
- **Calibration (claim C):** box-1 executable-surface evidence pinned at the
  new SKILL.md digest. Before: the round-30 survey was green only as console
  output at `83b0a78a…`; SKILL.md has since moved to `f9bd07c2…` (732 lines,
  §8 M5). After: `reports/round-34/craft/box1-resurvey-durable.json` +
  receipt, 28/28 at `f9bd07c2…`, plus the A09 R1–R8 reissue as new rows.
  {{C01-C06 pointers}}.
```

### Draft — Landed changes

```text
- `reports/round-34/handoff/declared-in-r7/` — new packet pair + `expected.json`
  + `freeze.txt` + `run.log` (the claim-D deliverable).
- `tools/exercise-handoff-e2e.py:1933-1934` — {{integrator-applied}} renderer
  default move to `declared-in-r7`; drafted with before/after text by D10, never
  edited by a seat.
- `tools/harness/receipt_guard_adoption.py` — new audit instrument (the claim-O
  deliverable); source shipped as a fenced block by O02, landed by the
  integrator.
- `reports/round-34/craft/box1-resurvey-durable.json` — new digest-pinned
  re-survey receipt (the claim-C deliverable).
- `reports/round-34/validation.json` — this round's acceptance receipt
  (integrator-run; the runner never publishes under `--check`).
- `reports/round-34/telemetry/` — dispatch-declared (filed) plus the
  observed-dispatch record and the closing snapshot owed once validation.json
  lands.
- Filed bytes: **zero** writes to `reports/round-1..33/**`, `corpus/lessons/*.md`
  lesson files, `tools/gates/frozen/**` (`{{P1 verdict}}`).
```

### Draft — Before → after measurements

Fill from §3's table (same numbers, prose form). Rule: every after-value names
the fragment that measured it and the counting command; every before-value below
was measured by this seat and is reproducible from §8.

### Draft — SHONEN

```text
All four boxes: {{untouched this round; r24 verdicts and the r30/r33 re-surveys
stand as filed}}. Conditions carried named, none silently closed:
- box 1 (decision tables/errors/checklists/sources): r24 verified-with-conditions;
  the inventory condition closed at r30 (28/28, digest-pinned) and is re-pinned
  this round at the new SKILL.md digest (claim C); citation-level conditions 2-4
  remain open (reports/round-32/dossier-d11-shonen-boxes.md:44-52,205).
- box 2 (end-to-end domain task): verified-with-conditions; standing design debts
  named (the D4 garment-form holds + owed slots, `head2` empty proper domain, the
  RL-3 ceiling) — design, not defect (d11:206; d13:130-132).
- box 3 (cold-run executability): verified-with-conditions; N1/N4/N5/N7 remain
  open as filed (d11:145-150,207).
- box 4 (no bleed / PROVINCE accurate): verified-with-conditions; standing
  readings 3a/3b/3c by design (d11:208).
No promotion decision is taken or implied here; the decision remains
operator-owned (SHONEN.md:10-11).
```

---

## §2 — Integration order and collision notes

1. Land the D build first (the packet pair is a read of live D2/D3/D4 bytes, so
   it must be measured against a settled tree), then the renderer-default move,
   then the re-pin rows. Then O's tool source + inventory, then C's receipt +
   reissue, then `run-validation.py`, then telemetry, then the fleet report,
   then SCORECARD/LOG/MANIFEST.
2. Collision surface: `tools/exercise-handoff-e2e.py` is touched only by D10's
   draft (integrator applies); `tools/harness/receipt_guard_adoption.py` is
   created by O02's draft (integrator applies); `LOG.md` is integrator-only
   (`targets.json:5-12`). **No shared file is written by two seats** — verified
   against the 63 `out` paths, which partition cleanly into 8 directories
   (§8 M3).
3. `reports/round-33/**` is now **filed** (commit da68a6d) and is inside the
   protected set for the whole round; `targets.json:7` restates this. The
   round-33 A09 R1–R8 rows (`reports/round-33/adj/A09-pins.md:107-114`) are read
   as evidence and are never edited — claim C's reissue lands as new rows.
4. One filed-round fact the integrator should carry: `AGENTS.md` lost its
   trailing scaffold at da68a6d (42 → 40 lines; §8 M12), which closes the
   `AGENTS.md:42` half of A09's R5. The SKILL.md self-cites at `:149` and `:183`
   (both citing `SKILL.md:47`) still resolve (§8 M12b) and are R5's live
   remainder.

---

## §3 — Before → after table (fill the after column from fragments)

| claim | axis | before (measured 2026-10-19 by S04, §8) | after required (claims.json) | counting command |
|---|---|---|---|---|
| D | depth | renderer default pins `declared-in-r6` (`tools/exercise-handoff-e2e.py:1933-1934`); that pair gates green (exit 0, 16/16, 20/20, findings 0) but five rows carry stale figures at `packet.md:148,149,150,152,307`; `declared-in-r7/` absent | `declared-in-r7/` lands with every figure equal to a live value; gate green on the new pair; links resolve; freeze digest equals the e2e's `packet_sha256`; renderer default moved; cascade landed as new rows | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md`; `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` |
| O | operability | no inventory instrument; 28 filed runners, 27 filed receipts; this seat's independent census: 11 unguarded in-place writers {5,6,7,8,9,10,11,12,19,21,29}, 17 guarded (§8 M10) | `receipt_guard_adoption.py` with selftest green; inventory JSON naming every runner + class; the four named hazards classified; a routing receipt | `python3 tools/harness/receipt_guard_adoption.py --selftest`; `... --json` |
| C | calibration | SKILL.md `f9bd07c2…` (732 lines); survey green as console output only, and its own `date` field is a hardcoded constant (§9 item 3b); A09 R1–R8 have no reissue | durable JSON + receipt, 28/28 at `f9bd07c2…`, dated and re-runnable; R1–R8 reissue table, each row verified by grep | `python3 -B reports/round-30/craft/box1-survey.py` |
| all | — | regressions green at this seat's cut: handoff 16/16+20/20 findings 0, receipt-guard selftest green (§8 M6, M11) | unchanged or better; zero regressions | §6 `CO5` |

---

## §4 — Telemetry material (draft)

- `telemetry/dispatch-declared.json` (filed, 1,626 bytes): owner = orchestrator
  (goal-mode parent); declared 2026-10-19T06:57:28Z; allocation = `opencode-go-2`
  / deepseek-v4.1-flash / key 2 of the round-robin / 64 requested workers / 1
  batched AgentSwarm call; durable digests `claims.json` = `f2b87ddb…9fcff0` and
  `targets.json` = `76d96524…9eea1d`. **This seat re-verified both against live
  bytes (§8 M2) — they match.**
- Composition cross-check (this seat's count, §8 M3): 63 seat rows by claim
  {D: 27, O: 15, C: 13, cross: 8} and by role {scout 4, planner 2, connector 1,
  executor 28, verifier 9, reviewer 8, scribe 7, critic 4}; 63 unique `out`
  paths, all under `reports/round-34/`. The declaration's own composition string
  also totals 63 while it requests 64 workers (§9 item 1) — both the declaration
  and the census agree on 63, so report 63 and name the 64 as requested-not-filled.
- Owed at close (AGENTS.md:32-39): an **observed-dispatch record** (launches,
  completions, failures, runtime concurrency, actual route; unknown counters
  `null` with owner + reason, never inferred zeroes) and the **closing snapshot**
  that closes `dispatch-declared.json` by path + its SHA-256 at close time. The
  declaration itself says so (`dispatch-declared.json:33`,
  `"open-at-seat-close"`).
- **Closing-snapshot filename (binding):**
  `reports/round-34/telemetry/availability-close-34.json`, mirroring the landed
  convention (`reports/round-{19,25,26,27,28,33}/telemetry/availability-close-N.json`;
  schema `kotodama-availability-closing-snapshot-v1`, keys `closes` +
  `closes_sha256` + `closed_fields` + `could_not_recover` + `sources`, as at
  `reports/round-33/telemetry/availability-close-33.json`). Do **not** name it
  `closing-snapshot.json` — that name exists nowhere in the repo and is the
  F-X16-3 defect the round-33 lane already reproduced (5 false firings at the
  then-current `SKILL.md:715`). **The amendment has since landed**: `SKILL.md:730-732`
  now globs `telemetry/availability-close-*.json` and keys the audit on
  `closes` + `closes_sha256`, so mirror that instrument, not the old one-liner.
  The round-33 close also set the precedent that the snapshot
  records the acceptance run's own receipt digest and that a final re-run follows
  so the receipt's input set covers the snapshot.

---

## §5 — Validator acceptance shape and the two schema traps

Mirror the round-33 receipt key set (`reports/round-33/validation.json`):
`round`, `runner`, `runner_sha256`, `counting_command`, `date`, `measured_at_utc`,
`baseline_revision`, `claims_declared`, `acceptance_checks_passed`, `claims`
(per-claim `{passed, date, command, failures[], measurement{}}`), `failures`,
`missing_dependencies`, `target_outputs`, `input_sha256`, `limits`. Behaviour:
`--check` prints and never publishes; `--selftest` is dependency-free
positive/negative controls; the default mode guards `reports/round-34/validation.json`
through `tools/harness/receipt_guard.py` (a new file, so the guard passes) and
exits 0 iff `acceptance_checks_passed`.

### Trap 1 — the baseline id is a *short* commit

`reports/round-34/claims.json:8` carries `"baseline_commit": "da68a6d"`, which
is **not** 40-hex (§8 M4a). The round-33 runner's `resolve_commit`
(`reports/round-33/run-validation.py:221-231`, `FULL_COMMIT_RE` at `:77`) refuses
anything that is not a full object id, so a copied coherence leg fails a
well-formed round. Round-34's `CO1` must accept the abbreviated id, expand it
with `git rev-parse --verify da68a6d^{commit}` (resolves to
`da68a6d705e41f369f21e8607bfaab5b54077f84`, §8 M4b), and record **both** the
declared token and the expanded id in the measurement — never rewrite the
declared value. `baseline_revision` in the receipt keeps the full expanded id for
cross-round comparability.

### Trap 2 — `seat_count` 64 vs 63 declared rows

`targets.json:3` declares `seat_count: 64`; the `seats` array has **63** entries
(§8 M3). Do not silently coerce and do not fail the round on it: implement `CO4`
as a *measured* leg that (a) asserts `len(seats) == 63` and every other declared
invariant (unique `out` paths, all under `reports/round-34/`, non-empty
`id`/`role`/`mission`/`out`), (b) records `declared_seat_count: 64`,
`observed_seats: 63`, `requested_workers: 64` and the composition-string total,
and (c) emits it as a named deviation with owner = orchestrator, not as a leg
failure. Editing `targets.json` to reconcile is **not** available: its digest is
pinned in `telemetry/dispatch-declared.json:20-25` (verified live, §8 M2), so an
edit would break the declaration's own durable-source digest. Report it.

---

## §6 — Validation-leg spec (machine-checkable)

Format: `id | claim | command/check | expected | parser hint`. `{{}}` means
"resolve from the landed fragment and pin the path". Every leg below was
requested by this seat's mission: packet-v-next green + zero stale figures;
renderer default moved; tool selftest + inventory parity; box-1 28/28 at the new
digest + reissue coverage; preservation; language; report/telemetry.

### §6.1 Coherence / schema legs (cross)

- **CO1** strict-parse `claims.json` and `targets.json` (duplicate JSON keys
  refused, round-33 `strict_json` pattern at `reports/round-33/run-validation.py:124-132`).
  Expect `round == 34` in both; `claims.baseline_commit` expands via
  `git rev-parse --verify <token>^{commit}` to
  `da68a6d705e41f369f21e8607bfaab5b54077f84` (Trap 1); record both forms.
- **CO2** `{c.id: c.axis for c in claims.claims}` ==
  `{"D": "depth", "O": "operability", "C": "calibration"}` and
  `set(claims.axes_in_play) == {"depth", "operability", "calibration"}` with three
  pairwise-distinct axes (REGIMEN.md:26-29; claims.json:17-20).
- **CO3** `claims.freshness_pause_in_force is True` and `"freshness"` absent from
  `axes_in_play` and from every claim's axis (claims.json:18).
- **CO4** dispatch shape (Trap 2): `claims.dispatch.provider_lane ==
  "opencode-go-2"`, `model == "deepseek-v4.1-flash"`, `requested_workers == 64`,
  `batched_calls == 1`; `len(targets.seats) == 63` — measured, with the
  `seat_count` 64 delta reported as a named deviation, never a silent pass and
  never a forced failure.
- **CO5** composition cross-check: role counts == `{scout 4, planner 2,
  connector 1, executor 28, verifier 9, reviewer 8, scribe 7, critic 4}` and
  claim counts == `{D 27, O 15, C 13, cross 8}` (measured 2026-10-19, §8 M3).
  Report the counts as the measurement, not as a threshold alone.
- **CO6** godspeed lead: **not machine-checkable from durable artifacts** — the
  prompts are not persisted and AGENTS.md:30-31 forbids private prompt payloads
  in telemetry. Record `could-not-evaluate` with owner = orchestrator and the
  declaration at `dispatch-declared.json:4` as the only evidence. Never score
  this leg as passed from absence of evidence.

### §6.2 Claim-D legs (packet-v-next green + zero stale figures)

- **D1** `python3 tools/gates/handoff-packet-check.py
  reports/round-34/handoff/declared-in-r7/packet.md` → exit 0; stdout matches
  `fields=16/16`, `glossary-entries=20`, `findings=0`. (The old pair also passes
  this — §8 M6 — which is exactly why D2 exists.)
- **D2 — zero stale figures (the claim's centre of gravity).** Do **not** search
  for bare numbers: the same digits are live in other contexts (58/16/15/13/4/3
  are live **D2** values, §8 M9). Implement as a *paired* check per table row
  below: for each (anchor, live_value) pair assert the new packet contains the
  live value in that context **and** contains none of the stale values in that
  context. Anchors are the round-6 line numbers for reference only; match on the
  claim id.
  | claim row | stale (r6 packet) | live (measured §8 M7/M8) | live source |
  |---|---|---|---|
  | D4-CL05 | typed_labels 74; native-form 56; findings_total 16; findings_hold_or_fail 15; `#stats` labels 74 | 82; 64; 12; 12; `typed_labels.stats.labels` 82 | `typed-labels.d4.yml#coverage`, `#typed_labels.stats` |
  | D4-CL06 | hold 15, note 1, fail 0; "three D2L-RANK holds"; "one D2L-RANK note" | hold 12, note 0, fail 0 | `expected-holds.json#counts` |
  | D4-CL07 | conflicts 4; quarantine handles 3 | conflicts 0; rank_quarantine_handles 0 | `typed-labels.d4.yml#coverage` |
  | D4-CL09 | rank_rules_unresolved_items 13; quarantine 3; conflicts 4 | 0; 0; 0 | `typed-labels.d4.yml#coverage` |
  | OQ-V3-05 | "three rank holds + one note, thirteen unresolved, three quarantine, four conflicts" | 12 form-keyed holds, 0 rank holds, 0 note, 0/0/0 | `expected-holds.json#counts`; `#coverage` |
  Report the count of rows audited and the count of live values matched. The
  round-34 packet's D2 rows are **live-correct today** and must stay so: the
  audit covers D2-CL01/CL02 and the :284/:301 summaries as *controls that must
  not be "corrected"* (§8 M9).
- **D3** links + uncertainty: `tools/harness/packet_links.py` and
  `tools/harness/packet_uncertainty.py --require-oq` against the new pair; every
  link resolves; 27-claim shape parity with the r6 pair (r6: 105/105 links,
  27 claims — `reports/round-30/handoff/declared-in-r6/run.log:3`). One pointer
  form to verify while measuring: the r6 packet cites
  `typed-labels.d4.yml#stats` and the live key is nested at
  `typed_labels.stats` (`:2865`), so "resolved" must be checked against the
  resolver's own semantics, not against a top-level key lookup (§8 M8b).
- **D4** freeze + tamper control: `declared-in-r7/freeze.txt` carries
  `packet_sha256`/`twin_sha256` lines (mirroring
  `reports/round-30/handoff/declared-in-r6/freeze.txt:1-8`), the e2e's reported
  `packet_sha256` equals the frozen line, and a mutated copy of `packet.md`
  gates red (`handoff-packet-check.py` nonzero) in `.scratch` only.
- **D5 — renderer default moved.** `tools/exercise-handoff-e2e.py:1934-1935`
  read `V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT`; assert both now name
  `reports/round-34/handoff/declared-in-r7` and no longer
  `reports/round-30/handoff/declared-in-r6`, and that
  `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` exits 0. Note the
  line numbers shift by the edit; match on the constant names.
- **D6** re-pin cascade: every surface that pinned `declared-in-r6` (K02's
  census) is either re-pointed as a **new** row or explicitly named superseded;
  assert the supersession record exists and that the old rows are byte-unchanged
  (delegates to P1 for the bytes).
- **D7** old-pair semantic-stale class named: assert the receipt states, with
  the §6.2 table as evidence, that the r6 pair gates green while carrying stale
  figures — the D13 negative control.

### §6.3 Claim-O legs (tool selftest + inventory parity)

- **O1** `python3 tools/harness/receipt_guard_adoption.py --selftest` → exit 0,
  `N/N` all green; parse the count and treat a green exit with a shrunken count
  as a failure.
- **O2 — inventory parity and 100% coverage.** `--json` output must name every
  filed runner: the census basis is 28 files (§8 M10). Assert
  `len(inventory) == 28`, every path matches `reports/round-*/run-validation.py`,
  and each row carries a class. **Then assert parity against this seat's
  independent census** (§8 M10) and file any disagreement as a defect rather
  than adjusting either side:
  - unguarded in-place receipt writers (11): rounds 5, 6, 7, 8, 9, 10, 11, 12,
    19, 21, 29;
  - guarded writers (17): rounds 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27,
    28, 30, 31, 32, 33.
  Honesty note for the instrument's own false-negative surface: rounds 8–12 and
  19/21 write through an aliased path variable (`output = ROOT / OUTPUT_REL;
  output.write_text(...)` — e.g. `reports/round-8/run-validation.py:1486`,
  `reports/round-10/run-validation.py:1054`, `reports/round-12/run-validation.py`,
  `reports/round-19/run-validation.py:19-21`, `reports/round-21/run-validation.py:1113-1115`),
  which a pure `write_text(validation.json)` regex misses. This seat's own
  first-pass regex produced exactly those five false negatives (§8 M10) — the
  landed tool must not reproduce them.
- **O3 — the four named hazards, classified honestly.** The claim names
  r5/r6/r7/r26. Measured: r5, r6, r7 write their receipts unguarded
  (`HERE / "validation.json").write_text(...)` at
  `reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py:336`,
  `reports/round-7/run-validation.py:8,1171`); **r26 is guarded** —
  `def guard_receipt()` at `reports/round-26/run-validation.py:1855-1857` is
  called at `:1905-1909` immediately before the write. The instrument must report
  r26 as adopted; the claim's *before* text calling r26 an unguarded hazard is
  wrong on live bytes and must be carried as errata (§9 item 2), not as evidence.
- **O4** routing receipt: unguarded runners → isolated-copy-only protocol;
  guarded runners → `REFRESH_RECEIPTS=1` refresh protocol. Assert the receipt
  covers every unguarded round from O2 with the correct protocol and names the
  r21 irony explicitly: r21 documents the isolated-clone protocol in its own
  `limits` while writing its own receipt unguarded (`:1113-1115`).
- **O5 — F-C13-1 leg (absolute).** No leg, command, control, or fixture in this
  round executes any `reports/round-*/run-validation.py` in-tree. Audit the
  runner's own command list: every historical-round invocation must be either
  absent or against an isolated `git archive`/clone copy under `.scratch`.
  Assert this seat's and the round-33 precedent's posture: the runner itself is
  read-only over filed runners (`reports/round-33/run-validation.py:1143-1182`
  reads them as text only). This leg failing is a round-level rejection, not a
  claim failure.

### §6.4 Claim-C legs (box-1 28/28 at the new digest + reissue coverage)

- **C1** `python3 -B reports/round-30/craft/box1-survey.py` → exit 0,
  `named == resolvable == 28`, `unnamed_in_skill == []`, and
  `skill_sha256 == f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`
  (measured live, §8 M5). Recompute SKILL.md's sha256 independently and assert
  the receipt's pinned digest equals it.
- **C1b — the receipt must carry its own date.** `box1-survey.py:8` hardcodes
  `"date": "2026-10-18"`, so the tool's own date field is **not** evidence of
  when the round-34 re-survey ran (§9 item 3b). Assert the durable JSON carries a
  round-34 stamp distinct from the tool's constant, plus the command, the digest,
  and the 28 rows; the leg must not accept the tool's `date` key as the receipt
  date.
- **C2 — reissue coverage.** The A09 R1–R8 list is
  `reports/round-33/adj/A09-pins.md:107-114`. Assert the round-34 reissue table
  names each of R1..R8 **exactly once** (set equality on the row ids, not a
  count), that each row states old reading → new reading → owning row, and that
  every SKILL.md line anchor in it resolves by grep at HEAD. Carry this seat's
  pre-measurement so a missing row is visible: R5's `AGENTS.md:42` half is
  already closed (AGENTS.md 42 → 40 lines at da68a6d, §8 M12), while the SKILL.md
  self-cites `:149` and `:183` both still resolve and cite `SKILL.md:47`
  (§8 M12b).
- **C3** zero filed-row edits: the reissue is a new table; `reports/round-33/**`
  bytes are unchanged (delegates to P1).

### §6.5 Cross / close legs

- **P1 — preservation (global).** Reuse the round-33 `protected_snapshot`
  approach (`reports/round-33/run-validation.py:733-784`): every blob under
  `reports/round-1..33/**`, `tools/gates/frozen/round-*`, and
  `corpus/lessons/*.md` (excluding `README.md`) is byte-identical to the
  declared baseline commit's tree; plus no new path appears under those prefixes
  in `git status`. Run it before and after measurement. This is where D6, D11
  and C3 actually verify.
- **L1 — language.** Run the embedded scanner pattern over every
  `reports/round-34/**` file; allow a hit only in a negation or routed-reference
  context; require every declared seat `out` path to be present in the scan
  (round-33 `check_language`, `:868-930`, with its `expected_outs` coverage
  assertion); zero unallowed hits. Two known adjudications to pre-clear: this
  file and every fragment quoting audit tokens in a spec block (allowlist the
  fenced spec blocks), and `claims.json`/`targets.json`/the runner itself, which
  round 33 excluded by path (`:903-905`).
- **X1** fleet report at `../.ufo/reports/round-34/kotodama.md` with all four
  required headings and an ISO date, and citing
  `reports/round-34/run-validation.py`. (Round-33 precedent:
  `../.ufo/reports/round-33/kotodama.md`, 8,312 bytes, exists; the round-34
  directory does not, §8 M13.)
- **X2** MANIFEST: the fleet-root `MANIFEST.json` round-34 entry present, or
  recorded `pending-by-construction` with the reason naming the integrator.
- **X3** telemetry: `dispatch-declared.json` SHA-256 recorded; its
  `durable_sources` digests equal the live `claims.json`/`targets.json` digests
  (verified true at this seat's cut, §8 M2); the observed-dispatch record and
  the closing snapshot exist **or** are reported as owed with owner + reason.
  Never infer missing counters.
- **X4** self-consistency: `round == 34`, `counting_command == "python3
  reports/round-34/run-validation.py"`, `acceptance_checks_passed` true only if
  every leg passed, `limits` non-empty, `missing_dependencies` ⊇
  `target_outputs` (every owed seat fragment listed). In-flight evidence changes
  invalidate acceptance (re-read digests before writing).

### §6.6 Leg table (machine-readable)

```json
{
  "round": 34,
  "runner": "reports/round-34/run-validation.py",
  "receipt": "reports/round-34/validation.json",
  "baseline_key": "claims.baseline_commit",
  "baseline_declared_token": "da68a6d",
  "baseline_expanded": "da68a6d705e41f369f21e8607bfaab5b54077f84",
  "legs": [
    {"id": "CO1", "claim": "cross", "check": "strict json + round==34 + short baseline expands to the declared commit", "expect": "pass"},
    {"id": "CO2", "claim": "cross", "check": "claim axes D/O/C on distinct axes == axes_in_play", "expect": "pass"},
    {"id": "CO3", "claim": "cross", "check": "freshness_pause_in_force true and freshness absent", "expect": "pass"},
    {"id": "CO4", "claim": "cross", "check": "provider_lane opencode-go-2 / model deepseek-v4.1-flash / 64 requested / 1 batch; 63 seat rows measured; seat_count 64 delta reported as named deviation", "expect": "pass-with-deviation", "deviation": "declared seat_count 64 vs 63 rows; owner orchestrator; targets.json digest pinned in dispatch-declared.json so no edit"},
    {"id": "CO5", "claim": "cross", "check": "seat role/claim counts == measured census", "expect": "pass", "measured_2026_10_19": {"claims": {"D": 27, "O": 15, "C": 13, "cross": 8}, "roles": {"scout": 4, "planner": 2, "connector": 1, "executor": 28, "verifier": 9, "reviewer": 8, "scribe": 7, "critic": 4}}},
    {"id": "CO6", "claim": "cross", "check": "godspeed lead", "expect": "could-not-evaluate", "owner": "orchestrator", "reason": "prompts not persisted; AGENTS.md:30-31 forbids private prompt payloads"},
    {"id": "D1", "claim": "D", "command": "python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md", "expect": "exit 0; fields=16/16; glossary-entries=20; findings=0"},
    {"id": "D2", "claim": "D", "check": "paired live-vs-stale audit over the 5 audited rows (D4-CL05/06/07/09, OQ-V3-05) with D2 rows as must-not-change controls", "expect": "zero stale in context, all live values matched"},
    {"id": "D3", "claim": "D", "command": "tools/harness/packet_links.py + tools/harness/packet_uncertainty.py --require-oq", "expect": "links resolved; 27-claim shape parity"},
    {"id": "D4", "claim": "D", "check": "freeze.txt packet_sha256 == e2e-reported; mutated copy gates red in .scratch", "expect": "pass"},
    {"id": "D5", "claim": "D", "check": "V3_BASELINE_DEFAULT/V3_FROZEN_DIR_DEFAULT name declared-in-r7; e2e --profile v3 --quiet exit 0", "expect": "pass"},
    {"id": "D6", "claim": "D", "check": "every declared-in-r6 pin re-pointed as a new row or named superseded; old rows byte-unchanged", "expect": "pass"},
    {"id": "D7", "claim": "D", "check": "receipt names the semantic-stale class the old pair hides (old pair gates green)", "expect": "pass"},
    {"id": "O1", "claim": "O", "command": "python3 tools/harness/receipt_guard_adoption.py --selftest", "expect": "exit 0; N/N controls green"},
    {"id": "O2", "claim": "O", "command": "python3 tools/harness/receipt_guard_adoption.py --json", "expect": "28/28 runners; parity with the independent census (11 unguarded, 17 guarded); aliased-path writes detected"},
    {"id": "O3", "claim": "O", "check": "the four named hazards classified; r26 reported as guarded/adopted with errata", "expect": "pass"},
    {"id": "O4", "claim": "O", "check": "routing receipt covers every unguarded runner with the isolated-copy-only protocol", "expect": "pass"},
    {"id": "O5", "claim": "O", "check": "zero in-tree execution of any filed round runner", "expect": "pass", "severity": "round-level"},
    {"id": "C1", "claim": "C", "command": "python3 -B reports/round-30/craft/box1-survey.py", "expect": "exit 0; 28/28; skill_sha256 == f9bd07c2..."},
    {"id": "C1b", "claim": "C", "check": "durable receipt carries its own round-34 date, not the tool's hardcoded 2026-10-18", "expect": "pass"},
    {"id": "C2", "claim": "C", "check": "reissue table names each of A09 R1-R8 exactly once with old->new->owning row; anchors grep-resolve", "expect": "pass"},
    {"id": "C3", "claim": "C", "check": "zero filed-row edits for the reissue", "expect": "pass"},
    {"id": "P1", "claim": "cross", "check": "reports/round-1..33/**, tools/gates/frozen/round-*, corpus/lessons/*.md byte-identical to baseline; no new protected paths", "expect": "pass"},
    {"id": "L1", "claim": "cross", "check": "language scan over reports/round-34/**; every declared seat out present in the scan; zero unadjudicated hits", "expect": "pass"},
    {"id": "X1", "claim": "cross", "check": "fleet report with 4 headings + date + runner citation", "expect": "pass"},
    {"id": "X2", "claim": "cross", "check": "MANIFEST round-34 entry present or pending-by-construction with reason", "expect": "pass"},
    {"id": "X3", "claim": "cross", "check": "telemetry digests match live; observed record + closing snapshot or owed with owner", "expect": "pass"},
    {"id": "X4", "claim": "cross", "check": "validation.json self-consistency + missing_dependencies covers target_outputs", "expect": "pass"}
  ]
}
```

---

## §7 — Selftest control list (`--selftest`, dependency-free, synthetic inputs)

Each control is a positive/negative pair the integrator implements with
in-memory fixtures, mirroring `reports/round-33/run-validation.py:1327-1438`:

1. a packet draft carrying `typed_labels 74` in the D4-CL05 context → **D2 fails**;
2. a packet draft carrying `native-form 64` and `labels 82` in that context →
   **D2 passes**;
3. a packet draft with D2's live numbers (58 / 16 / 13 / 4 / 3) deliberately
   "corrected" to D4's → **D2 fails** (the must-not-change control);
4. `OQ-V3-05` rewritten to "three rank holds + one note" → **D2 fails**;
5. a packet missing `glossary-entries=20` in the gate stdout → **D1 fails**;
6. a `freeze.txt` whose `packet_sha256` differs from the e2e's reported digest →
   **D4 fails**;
7. the renderer default still naming `declared-in-r6` → **D5 fails**;
8. an inventory missing round 19 → **O2 fails on coverage**, and an inventory
   classifying round 26 as unguarded → **O3 fails**;
9. an inventory with round 21 classified guarded → **O2/O3 fail** (the aliased-path
   false negative);
10. a trap runner that imports the guard but never calls it → **O3 must not score
    it adopted** (`could-not-evaluate` or a named class, never a wrong adopted);
11. a trap runner writing via `os.replace` → **O2 must detect the write**, not
    report clean;
12. `box1-survey.py` output claiming 27 resolvable of 28 named → **C1 fails**;
13. a durable C receipt whose only date is the tool's `2026-10-18` → **C1b fails**;
14. a reissue table with 7 of the 8 R-rows → **C2 fails**, naming the missing id;
15. a duplicated R-row (R4 twice, R6 absent) → **C2 fails** (set equality, not count);
16. `baseline_commit` absent or non-resolving → **CO1 fails**;
17. `axes_in_play` containing `freshness` → **CO3 fails**;
18. `targets.json` with 62 seat rows → **CO4 fails** (63 is the measured value);
19. a duplicate `out` path across seats → **CO4 fails**;
20. a protected file with one mutated byte → **P1 fails**, naming the path;
21. a round-34 fragment introducing a promotion token outside a negation → **L1
    fails**;
22. a fleet report with 3 of the 4 headings → **X1 fails**.

Control 17's sibling caution: do not write a selftest that asserts
`seat_count == len(seats)` as a *pass* condition — assert the measured 63 and
report the declaration's 64 separately (Trap 2).

---

## §8 — Measurements taken by this seat (2026-10-19, round-34 tree)

- **M1** `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`;
  `git ls-files | wc -l` → 2735; `git status --porcelain -uall` → exactly three
  rows, all untracked: `reports/round-34/claims.json`,
  `reports/round-34/targets.json`,
  `reports/round-34/telemetry/dispatch-declared.json`.
- **M2** `sha256sum reports/round-34/claims.json reports/round-34/targets.json` →
  `f2b87ddb37d8def04c6479a4ac6831ebf5c07514f91efe453247b84a0f9fcff0`,
  `76d9652497c9b50ff484238e812c0597195db752786913cb7a6201b4b19eea1d` — both
  equal the digests declared in `telemetry/dispatch-declared.json:20-25`.
- **M3** seat census from `targets.json` → **63 rows** (JSON parse) and
  `grep -c '^\s*{"id":'` → 63; ids K01-K04, P01-P02, X00, D01-D20, O01-O10,
  C01-C09, R01-R08, X01-X04, S01-S05; no duplicates; claims {D 27, O 15, C 13,
  cross 8}; roles {scout 4, planner 2, connector 1, executor 28, verifier 9,
  reviewer 8, scribe 7, critic 4}; 63 unique `out` paths across
  {scout 4, plan 2, depth 20, op 10, calib 9, review 8, cross 5, scribe 5}.
- **M4a** `claims.json:8` `baseline_commit` = `"da68a6d"` (7 hex, not 40-hex);
  **M4b** `git rev-parse --verify da68a6d^{commit}` →
  `da68a6d705e41f369f21e8607bfaab5b54077f84`.
- **M5** `sha256sum SKILL.md` → `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`;
  `wc -l SKILL.md` → 732; `python3 -B reports/round-30/craft/box1-survey.py` →
  exit 0, `{"date": "2026-10-18", "named": 28, "resolvable": 28,
  "unnamed_in_skill": [], "skill_sha256": "f9bd07c2…"}`.
- **M6** `python3 tools/gates/handoff-packet-check.py
  reports/round-30/handoff/declared-in-r6/packet.md` → exit 0,
  `INFO scan: fields=16/16 glossary-entries=20 findings=0`.
- **M7** `examples/culture-d4/expected-holds.json` `counts` →
  `{"hold": 12, "note": 0, "fail": 0}`.
- **M8a** `examples/culture-d4/typed-labels.d4.yml` `coverage` →
  `labels_by_kind {native-form 64, translated-label 12, borrowed-strata 6}`
  (=82), `findings_total 12`, `findings_hold_or_fail 12`, `label_findings_hold 12`,
  `label_findings_fail 0`, `conflicts 0`, `rank_quarantine_handles 0`,
  `rank_rules_unresolved_items 0`, `reconciliation_records 6`,
  `rank_rules_component/gate_projected/normalized 4`;
  **M8b** `typed_labels.stats` (`:2865-2869`) → `{"fail": 0, "hold": 12,
  "labels": 82}`; there is no top-level `stats` key (top-level keys:
  assembly, canon, coverage, era_material_reconciliation, era_reconciliation,
  findings, generator, label_kinds, name, rank_rules, typed_labels).
- **M9** `examples/culture-d2/typed-labels.d2.yml` `coverage` → `typed_labels 58`,
  `{native-form 46, translated-label 10, borrowed-strata 2}`, `findings_total 16`,
  `findings_hold_or_fail 15`, `conflicts 4`, `rank_quarantine_handles 3`,
  `rank_rules_unresolved_items 13`, `reconciliation_records 10` — i.e. the
  round-6 packet's **D2** rows at `:129,:130,:284,:301` match live D2 and must
  not be "corrected", while its **D4** rows at `:148-152,:307` carry exactly
  these D2 figures where D4's live figures differ.
- **M10** runner census (28 `reports/round-*/run-validation.py`; 27 filed
  `validation.json`). Unguarded in-place receipt writers (11): 5, 6, 7, 8, 9,
  10, 11, 12, 19, 21, 29. Guarded (17): 14, 15, 16, 17, 18, 20, 22, 23, 24, 25,
  26, 27, 28, 30, 31, 32, 33. Write sites behind aliased path variables:
  `reports/round-8/run-validation.py:1486`, `reports/round-9/run-validation.py:1909-1910`,
  `reports/round-10/run-validation.py:1054`, `reports/round-11/run-validation.py:1738-1740`,
  `reports/round-21/run-validation.py:1113-1115`,
  `reports/round-19/run-validation.py:19-21` (module level, uncoupled from any
  guard), `reports/round-29/run-validation.py:922`,
  `reports/round-5/run-validation.py:194`, `reports/round-6/run-validation.py:336`,
  `reports/round-7/run-validation.py:1171`. This seat's first regex pass
  produced five false negatives (8-12, 21) by matching only
  `write_text(...validation.json...)`.
- **M11** `python3 -B tools/harness/receipt_guard.py --selftest` → exit 0,
  `selftest_passed: true` (also exercised live by round-26 at
  `reports/round-26/run-validation.py:1905-1909`).
- **M12** `AGENTS.md` 42 → 40 lines at da68a6d (`git diff --stat 139e3b6
  da68a6d -- AGENTS.md` → 2 deletions: the stray code fence and the dangling
  `### 2.2 SKILL.md …` heading recorded as F-X16-1 at
  `corpus/lessons/round-32.md:32`);
  **M12b** `grep -rn "SKILL\.md:[0-9]" AGENTS.md SKILL.md` → only the SKILL.md
  self-cites at `:149` and `:183` (both citing `SKILL.md:47`, whose table row is
  intact).
- **M13** `ls ../.ufo/reports/round-33/` → `kotodama.md` (8,312 bytes);
  `../.ufo/reports/round-34/` → absent.

Honest limits: every after-value in §3 is a requirement from `claims.json`, not
an observation — no seat fragment existed at this seat's cut. §6 is a design the
integrator implements and self-tests; this seat executed no part of
`run-validation.py` and executed no filed round runner. §9's defects are
measurements about the *declaration*, and this seat changed no declared byte.

---

## §9 — Declaration defects and errata for the integrator

1. **`seat_count` 64 vs 63 declared rows** (§8 M3, M1). `targets.json:3` says 64;
   the array has 63; `dispatch-declared.json`'s composition string also totals 63
   while `requested_workers` is 64. Handle per §5 Trap 2: measure 63, report the
   delta as a named deviation with owner = orchestrator. Do **not** edit
   `targets.json` — its digest is pinned at `dispatch-declared.json:20-25` and
   verified live (M2). If the round records "64 seats" anywhere without the
   delta, that is a fabricated count.
2. **Claim O's r26 hazard classification is wrong on live bytes** (claims.json:41
   "reports/round-26/run-validation.py carries the same hazard (:90,:1909)").
   Measured: r26 defines and calls the guard at `:1855-1857` and `:1905-1909`,
   immediately before its `:1909` write. The instrument must classify r26 as
   guarded/adopted. The claim's O-threshold ("the four known hazards classified")
   is still satisfiable — classifying r26 as adopted *is* a classification — but
   the *before* narrative must be carried as errata, and the genuinely unguarded
   set (11 rounds, §8 M10) is the materially useful finding.
3. **Claim D's stale-figure census is right in substance and sharper in detail.**
   (a) The five stale sites are `packet.md:148,149,150,152,307`; the manifest rows
   at `:68-69` already agree with live bytes (§8 M8a/M7), so the
   self-contradiction the claim names is real and located. (b) `:148` cites
   `typed-labels.d4.yml#stats (fail 0, hold 12, labels 74)` — the same live file's
   `typed_labels.stats` reads `labels 82` (§8 M8b), so one row contradicts the
   live bytes twice, and the pointer is to a nested key rather than a top-level
   one. (c) The stale D4 figures `16/15/4/3/13` are *live D2* figures (§8 M9),
   which is the mechanism; expect this explanation in the receipt rather than a
   bare list of wrong numbers.
4. **Claim C's receipt date is not sourceable from the survey tool.** See §6.4
   C1b and §8 M5: `box1-survey.py:8` hardcodes `2026-10-18`. Claim C's
   `after_required` demands a "digest-pinned, dated, re-runnable" receipt, so the
   durable JSON must carry the round-34 measurement date and the command, and the
   integrator should not cite the tool's constant as the date.
5. **A09's R-row list is a re-pin list, not a line-anchor list.** The mission's
   phrasing ("the A09 R1–R8 SKILL anchor reissue") reads as eight SKILL anchors;
   the filed rows are eight re-pin *needs*, of which R3 (SKILL.md digests), R4
   (box-1 re-survey) and R5 (line anchors) concern SKILL.md
   (`reports/round-33/adj/A09-pins.md:109-111`). C2 checks coverage of all eight
   rows exactly once; the old→new *anchor* mapping is R5's content, with R5's
   `AGENTS.md:42` half already closed (§8 M12).

---

## §10 — Landed-fragment cross-check (addendum, 2026-10-19, same wave)

Read by this seat after the draft was written. The wave is still dispatching, so
every list here is a point-in-time snapshot with its command.

**Dependency supersession.** At this seat's first cut `reports/round-34/` held
only `claims.json`, `targets.json` and `telemetry/dispatch-declared.json`; §1-§9
were written against that empty state. At this addendum's read the directory
holds 54 files and **51 of the 63 declared seat outputs have landed**. The 12
still absent at that read — recompute with the command in §10.6, do not trust
the list — were: `depth/{D05,D13,D15,D17,D19,D20}`, `op/O02-tool-source.md`,
`cross/X00-connector.md`, `review/{R01,R06,R07,R08}`.

**§10.1 — Claim-O census is now two-seat (legs O2/O3 strengthened).**
`op/O04-predicted-inventory.md` reports the same census this seat measured
independently (§8 M10): `counts {runners 28, guarded_in_place 17,
unguarded_in_place 11}` with the same round sets, and its `known_hazards` block
records `round 26 … "agrees": false`, i.e. r26 measured **guarded** against the
claim's "same hazard" text — independently reproducing §9 item 2
(`op/O04-predicted-inventory.md:160-166`). O04 also supplies detail this seat's
census lacked and leg O2 should adopt: r12's receipt write is at
`reports/round-12/run-validation.py:1071`; r19's write lives inside an embedded
`-c` **script string** (`:21`, which is why a source-text regex misses it); and
`reports/round-22/validation.json` never existed, so the filed receipts number
**27 for 28 runners**. **Leg amendment:** O2's parity target is O04's landed
inventory (with `sha256` per runner and a `class`/`hazard` pair), and its
`counts` block is the assertion surface — a landed tool that reports a different
runner count than O04's 28/17/11 fails parity even if its own selftest is green.

**§10.2 — Claim-C's date trap is corroborated and solved (leg C1b confirmed).**
`calib/C02-receipt-json.md:51,57,416-418` independently found that
`box1-survey.py:8` hard-codes `2026-10-18` and handled it exactly as leg C1b
requires: the durable JSON keeps its own `"date": "2026-10-19"` and
`"measured_at_utc": "2026-10-19T07:11:01Z"` as the run evidence and carries the
tool's constant only as `survey_stdout.date` with a note that it is the script's
filing date, not the run date. This corroborates §9 item 4 and the `:8` citation
this seat corrected. **Leg amendment:** C1b should accept C02's field split as
the shape (own date + `measured_at_utc` + the tool's date labelled as the
tool's), not merely "some date that is not 2026-10-18".

**§10.3 — Claim-D's live numbers are two-seat and now have in-file anchors.**
`depth/D03-ledger-rows.md:19-33` independently measures the same live block this
seat measured (§8 M8): `typed_labels 82` (`typed-labels.d4.yml:46`), native-form
64 (`:37`), translated-label 12 (`:38`), `findings_total 12` (`:32`),
`findings_hold_or_fail 12` (`:31`), conflicts 0 (`:30`), quarantine handles 0
(`:40`), unresolved rank items 0 (`:44`), `stats` 0/12/82 (`:2866-2868`),
expected-holds 12/0/0 (`expected-holds.json:47-49`, rows `:53-120`). Its stale
table opens on the same two rows this seat's §6.2 table opens on
(`D03:68-69` → `packet.md:148`). **Leg amendment:** D2's paired table gains these
in-file line anchors as the "live source" column, so a mismatch names the YAML
line rather than the whole file.

**§10.4 — Telemetry convention corroborated; §4 corrected in place.**
`scribe/S05-telemetry-draft.md:186-193,198-202` independently names
`reports/round-34/telemetry/availability-close-34.json` with schema
`kotodama-availability-closing-snapshot-v1` and `closes` + `closes_sha256`, and
records `find reports -name "closing-snapshot*.json"` → empty. It also records
that the round-33 F2 amendment landed: the live instrument is now `SKILL.md:730-732`,
which globs `telemetry/availability-close-*.json`. This seat verified that text
directly and **corrected §4's closing bullet in place** — the `SKILL.md:715`
false-firing is history, not the current instrument. Leg X3 mirrors S05's
Template B.

**§10.5 — Preservation re-check (leg P1, point-in-time).** At this addendum's
read `git status --porcelain -uall` over every protected prefix
(`reports/round-1..33/**`, `corpus/lessons`, `tools/gates/frozen`) returns **0
rows**, and `git diff --stat da68a6d -- reports corpus/lessons tools/gates/frozen`
is **empty**: the 54 new files all live under `reports/round-34/`, and nothing
filed moved. This is the round's own P1 pre-state, measured before the
integrator's close-time writes.

**§10.6 — Recompute commands (do not trust the snapshot lists).**

```bash
python3 -c "import json,os;t=json.load(open('reports/round-34/targets.json'));print([s['out'] for s in t['seats'] if not os.path.isfile('reports/round-34/'+s['out'])])"
find reports/round-34 -type f | wc -l
git status --porcelain=v1 -uall -- reports corpus/lessons tools/gates/frozen | wc -l
```

## Owed

All 63 declared seat fragments — in particular `depth/D01..D20`,
`op/O01..O10`, `calib/C01..C09`, `review/R01..R08`, `cross/X00..X04`,
`scribe/S01..S03`, `scribe/S05`. **Snapshot at §10's read (recompute with §10.6;
do not trust this list): 51 landed, 12 absent — `depth/{D05,D13,D15,D17,D19,D20}`,
`op/O02-tool-source.md`, `cross/X00-connector.md`, `review/{R01,R06,R07,R08}`.**
Beyond the seat fragments:

- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,run.log}`
  (claim D's deliverable path is declared but absent at this cut);
- `tools/harness/receipt_guard_adoption.py` and its inventory/routing artifacts
  (claim O);
- `reports/round-34/craft/box1-resurvey-durable.json` + receipt and the A09
  R1–R8 reissue table (claim C);
- `reports/round-34/run-validation.py` and `reports/round-34/validation.json`
  (integrator-authored; this seat executed no part of either);
- `reports/round-34/telemetry/observed-dispatch.json` and the closing snapshot
  `reports/round-34/telemetry/availability-close-34.json` (§4);
- `../.ufo/reports/round-34/kotodama.md` (the four-section report this draft
  supplies), the fleet-root `MANIFEST.json` round-34 entry, `SCORECARD.md`, and
  the append-only `LOG.md` entry — integrator-only writes.

## Citations

- `REGIMEN.md:13,25-29,34-36,52-58` — schedule position 2 of 3, per-round
  contract, done-when.
- `reports/round-34/claims.json:4-19,20-66,68-74` — position/dispatch, the three
  claims and their before/after + counting commands, non-goals (baseline token at
  `:8`).
- `reports/round-34/targets.json:3-12,13-83` — `seat_count` 64 (`:3`),
  shared_rules (`:5-12`), 63 seat rows (`:13-83`).
- `reports/round-34/telemetry/dispatch-declared.json:4,6-13,15-27,33` —
  declaration, allocation/composition, durable-source digests, `open-at-seat-close`.
- `reports/round-33/run-validation.py:50-55,70-75,77,124-132,221-231,733-784,868-930,1143-1182,1327-1438` —
  SECTIONS contract, `FULL_COMMIT_RE`, `strict_json`, `resolve_commit`,
  `protected_snapshot`, `check_language`, read-only filed-runner handling,
  selftest style; `reports/round-33/validation.json` — receipt key set;
  `reports/round-33/telemetry/availability-close-33.json` — closing-snapshot
  schema and `closed_fields` precedent.
- `tools/exercise-handoff-e2e.py:1930-1935` — `V3_PROFILE`/`V3_PACKET_VERSION` and
  the two defaults this round moves.
- `reports/round-30/handoff/declared-in-r6/{packet.md:68,69,129,130,148,149,150,152,284,301,307;
  freeze.txt:1-8; run.log:1-6}` — the old pair's shape, its live-correct rows and
  its five stale rows.
- `reports/round-30/craft/box1-survey.py:5,8,10` — the SKILL.md read, the hardcoded
  `date` constant at `:8`, the 28 executables, and the `skill_sha256` line at `:10`;
  `reports/round-30/craft/box1-landed-survey.json:4-6` — the prior receipt
  (`83b0a78a…`); `reports/round-30/run-validation.py:697-700` — the dated-receipt
  requirement.
- `examples/culture-d4/typed-labels.d4.yml` (coverage block, `typed_labels.stats`
  at `:2865-2869`); `examples/culture-d4/expected-holds.json#counts`;
  `examples/culture-d4/typed-labels.d2.yml#coverage` — the live values in §6.2.
- `tools/harness/receipt_guard.py:152-169,201-202` — `guard_receipt`,
  `round_runner_main`, `selftest_receipt`;
  `reports/round-{5,6,7}/run-validation.py:194,336,1171`;
  `reports/round-{8,9,10,11,12}/run-validation.py:1486,1909-1910,1054,1738-1740`;
  `reports/round-19/run-validation.py:19-21`; `reports/round-21/run-validation.py:1113-1115`;
  `reports/round-26/run-validation.py:90,1855-1857,1905-1909`;
  `reports/round-29/run-validation.py:922` — the census in §8 M10.
- `reports/round-33/adj/A09-pins.md:1-20,107-116,130-135` — the R1–R8 re-pin
  rows and the class taxonomy.
- `AGENTS.md:15-39` — telemetry rules and close-what-you-open; `git diff --stat
  139e3b6 da68a6d -- AGENTS.md` — the 42 → 40 line change; `SKILL.md:47,149,183,
  522,534,715` — the anchors this draft cites.
- `corpus/lessons/round-32.md:32-33` — F-X16-1/F-X16-2, the scaffold and the
  179-line anchor miss.
- `reports/round-32/dossier-d11-shonen-boxes.md:44-52,145-150,203-208` and
  `dossier-d13-operator-decisions.md:130-132` — box conditions quoted in the
  SHONEN draft; `SHONEN.md:3-11` — the four boxes.
- `../.ufo/reports/round-33/kotodama.md` (exists, 8,312 bytes);
  `../.ufo/reports/round-34/` (absent) — §8 M13.
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): §8 M1-M13 as listed there, plus
  `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md`,
  the python census over `targets.json`, the python census over
  `reports/round-*/run-validation.py`, `grep -o "typed-labels.d4.yml#[a-z_]*"`,
  and the paired stale-figure scan over `declared-in-r6/packet.md`.
- §10 landed-fragment reads: `reports/round-34/op/O04-predicted-inventory.md:3-30,160-166`;
  `reports/round-34/calib/C02-receipt-json.md:1,9,30-57,416-418`;
  `reports/round-34/depth/D03-ledger-rows.md:13-33,68-69`;
  `reports/round-34/scribe/S05-telemetry-draft.md:17,51,186-202,229-230`;
  `SKILL.md:728-732` (the amended close-what-you-open audit);
  `find reports/round-34 -type f | wc -l` → 54 and the three §10.6 recompute
  commands (2026-10-19, same wave).
