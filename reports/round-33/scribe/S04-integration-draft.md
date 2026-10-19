- Seat: S04 | scribe | cross | date 2026-10-19 | baseline 139e3b6

# S04 — round-33 integration dossier draft + validation-leg spec

Purpose: give the integrating parent (a) the fleet-report draft text for
`../.ufo/reports/round-33/kotodama.md` and (b) a machine-checkable leg spec it
implements as `reports/round-33/run-validation.py`. Everything below that is a
measurement was taken by this seat at the round-33 tree on 2026-10-19 with the
commands in §8; everything keyed to a fragment path is a placeholder the
integrator fills from the landed fragment.

Dependency state at this seat's cut (2026-10-19, earlier in the wave):
`reports/round-33/{op,calib,adj,cross,review,scribe}/` were **empty** — all 64
seat fragments unwritten, including the ones this draft quotes.
`reports/round-33/telemetry/` carried only `dispatch-declared.json`.
`../.ufo/reports/round-33/` did not exist. **Superseded by §9**, which records the
fragments that landed later in the same wave and the leg amendments they force;
every `{{...}}` token below is still an owed fill, listed in §7.

**Non-author declaration:** this seat authored no lane artifact before this
round. No promotion, canon, clearance, or closure verdict is claimed anywhere in
this file; every such token below appears only as a negation or as a quoted
audit pattern (§6.7).

---

## §1 — Fleet-report draft (four required sections)

Heading set required by the r32 validator's `SECTIONS` contract
(`reports/round-32/run-validation.py:50-55`): `Work performed`, `Landed changes`,
`Before → after measurements`, `SHONEN`. Reuse that regex pair for round 33.

### Draft header

```text
# kotodama — round 33 report (2026-10-19)

Regimen 2 (REGIMEN.md:13), loop 1, build 1 of 3. One 64-worker batch on
`opencode-go/deepseek-v4.1-flash` (key 1 of the per-round round-robin). Declared
baseline `139e3b662900557afe54f632b468619593dc9fcb` (claims.json:8); this round's
work lands in the same integrating pass that files this report. Claims O/C/A on
operability/calibration/adjacency (claims.json:16); freshness axis-move claims
stay paused (claims.json:18). Dispatch honesty: allocation is declared at
`reports/round-33/telemetry/dispatch-declared.json` (digest-pinned); observed
launches/completions/failures are `{{observed dispatch counts or null}}` —
{{owner}} — with the closing snapshot owed once validation.json lands
(AGENTS.md:32-39). Scope watch: {{A03 verdict}}.
```

### Draft — Work performed

```text
- **Operability (claim O):** the round-32 routed operability debt, landed.
  (a) lessons index reconciled: `corpus/lessons/README.md` carries one row per
  `corpus/lessons/*.md` file ({{33}}/33) with re-measured bytes/lines/sha8 cells
  for the seven new rows (round-26..round-32.md), prose arithmetic corrected, and
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` exits 0 with
  zero findings (declaration-time state: exit 1, 33 files vs 26 rows, findings 2 —
  C31-1 unindexed round-26..32.md, C34-2 prose drift stated [26,26] measured
  [26,33]; §8 C1/C2). Filed lesson files untouched (append-only). {{O01/O02/O03/
  O04/O06/O07/O08 pointers}} (b) the round-32 falsifier filename-mismatch debt
  dispositioned at `reports/round-33/op/O05-falsifier-disposition.md`:
  {{located-with-fix+control | carried-with-owner+reason}} ({{K01/P01 pointers}}).
- **Calibration (claim C):** the twelve standing open items in the round-32
  dossier dispositioned. `reports/round-33/calib/open-items-ledger.json`:
  {{12}}/12 rows, each with a re-verified status-quo pointer, a disposition class
  in {fixed-with-evidence, carried-with-owner+reason+next-touch} and evidence
  citations; bounded fix drafts for every fixable item at
  `calib/C14-fix-drafts.md`; consistency receipt `calib/C13-consistency.md`
  green. Counting provenance: the d13 Decision 4 table carries **9 data rows**
  (`reports/round-32/dossier-d13-operator-decisions.md:128-138`) against
  SCORECARD's "12 standing open items" (`SCORECARD.md:443-445`) — the ledger's
  12-item canonicalization and its arithmetic are owed from K03 and must be
  reconciled in the receipt ({{K03/C01-C16 pointers}}).
- **Adjacency (claim A):** the consolidated regimen-2 opening boundary audit.
  `reports/round-33/adj/audit-assembled.md` backed by A01-A14: PROVINCE accuracy
  re-verified at HEAD (`PROVINCE.md` last touched `c53782a`, matching the r32
  dossier's claim), handoff gate re-run green, zero unfiled cross-domain bleed,
  scope watch clean, contested items restated routed-not-absorbed, and the
  language audit clean. {{A01-A15 pointers, per-check verdicts, named findings}}.
```

### Draft — Landed changes

```text
- `corpus/lessons/README.md` — {{integrator-applied}} revision: 7 new index rows
  (round-26..round-32.md), §1/§2 prose arithmetic 26→33, §4 queue additions,
  revision stamp. Drafted by O01/O02; applied by the integrator.
- `reports/round-33/op/O05-falsifier-disposition.md` — new disposition record
  (the claim-O counting-command artifact).
- `reports/round-33/calib/open-items-ledger.json` + `calib/C14-fix-drafts.md` —
  new ledger and fix drafts (integrator applies any source edits).
- `reports/round-33/adj/audit-assembled.md` — new consolidated adjacency audit.
- `SKILL.md` — {{none | integrator-applied pointer fixes per C14 with before/after
  text; a checklist item appended after SKILL.md:534 if the integrator lands it}}.
- `reports/round-33/validation.json` — this round's acceptance receipt
  (integrator-run; `run-validation.py` never publishes under `--check`).
- `reports/round-33/telemetry/` — dispatch-declared (filed) + observed dispatch
  and the closing snapshot owed once validation.json lands.
- Filed bytes: **zero** writes to `reports/round-1..32/**`,
  `corpus/lessons/*.md` lesson files, `tools/gates/frozen/**` ({{preservation
  leg verdict}}).
```

### Draft — Before → after measurements

Fill from §3's table (same numbers, prose form). Rule: every after-value must
name the fragment that measured it and the counting command; every before-value
below was measured by this seat and is reproducible from §8.

### Draft — SHONEN

```text
All four boxes: {{untouched this round; r24 verdicts and the r32 re-survey stand
as filed}}. Conditions carried named, none silently closed:
- box 1 (decision tables/errors/checklists/sources): r24 verified-with-conditions;
  the inventory condition closed at r30 (28/28 re-verified, digest-pinned);
  citation-level conditions 2-4 remain open
  (reports/round-32/dossier-d11-shonen-boxes.md:44-52, 205).
- box 2 (end-to-end domain task): verified-with-conditions; standing design debts
  named (12 D4 garment-form holds + owed slots, `head2` empty proper domain, the
  RL-3 ceiling) — design, not defect (d11:206; d13:130-132).
- box 3 (cold-run executability): verified-with-conditions; N1/N4/N5/N7 remain
  open as filed (d11:145-150, 207).
- box 4 (no bleed / PROVINCE accurate): verified-with-conditions; standing
  readings 3a/3b/3c by design (d11:208); this round's adjacency audit adds no
  bleed class {{or names one with an owner}}.
No promotion decision is taken or implied here; the decision remains
operator-owned (SHONEN.md:10-11).
```

---

## §2 — Integration order and collision notes

1. Land O-fragment drafts first (README delta + O05), because the O counting
   command is a file-existence test and the C/A legs read the README.
2. Then C ledger + fix drafts; then the A audit; then `run-validation.py`; then
   telemetry observed-dispatch + closing snapshot; then fleet report; then
   SCORECARD/LOG/MANIFEST entries.
3. Collision surface (from claims/targets): `corpus/lessons/README.md` is touched
   only by O01/O02 drafts (integrator applies) — no other seat writes it;
   `SKILL.md` is touched only by C14 drafts; `LOG.md` is integrator-only
   (`targets.json:7`). `LOG.md` is already modified in the working tree
   (`git status --porcelain` → ` M LOG.md`) before this round's work, plus
   `?? REGIMEN.md` and `?? reports/round-33/` (§8 S1) — the scope leg must
   explain exactly these three, and nothing else.
4. `AGENTS.md` ends with a stray code fence and a dangling heading
   (`AGENTS.md:40-42`). Recorded as an incidental observation for X02/R07, not
   absorbed or edited by this seat; it is not one of the round-33 claims.

---

## §3 — Before → after table (fill the after column from fragments)

| claim | axis | before (measured 2026-10-19 by S04, §8) | after required (claims.json) | counting command |
|---|---|---|---|---|
| O | operability | c31 audit exit 1; 33 files vs 26 rows; findings 2; `op/O05-falsifier-disposition.md` absent; falsifier artifact not located at declaration | audit exit 0, findings 0, rows==files==33, selftest green; disposition record exists naming fix+control or owner+reason | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`; `test -s reports/round-33/op/O05-falsifier-disposition.md` |
| C | calibration | no ledger file; 9 data rows in the d13 table vs SCORECARD's "12" (reconciliation owed) | `calib/open-items-ledger.json` rows == 12, fields complete, classes valid, K03 cross-check + C13 consistency green | `python3 reports/round-33/run-validation.py` (C legs) |
| A | adjacency | no consolidated audit since r29; PROVINCE last touch `c53782a`; tracked paths 2655; `../.ufo/reports/round-33/` absent | `adj/audit-assembled.md` with a verdict for every A01-A10 check; handoff gate exit 0; zero unfiled bleed; scope delta explained | `python3 reports/round-33/run-validation.py` (A legs) |
| all | — | regressions green at declaration: battery 44/44, craft 10/10+18/18, D4 81/81, c31 selftest 28/28, handoff 16/16+20/20 findings=0 | unchanged or better; zero regressions | §8 R1-R5 |

---

## §4 — Telemetry material (draft)

- `telemetry/dispatch-declared.json` (filed, 1,500 bytes): owner = orchestrator;
  declared 2026-10-19T03:49:01Z; allocation = opencode-go / deepseek-v4.1-flash /
  key 1 / 64 requested workers / 1 batched AgentSwarm call; durable digests of
  `claims.json` = `ba69090f…3fb12` and `targets.json` = `342c8f80…f13f`. **This
  seat re-verified both digests against live bytes on 2026-10-19 (§8 S2) — they
  match.**
- Composition cross-check (this seat's count, §8 S3): `targets.json` seats 64 by
  claim {O:15, C:22, A:20, cross:7} and by role {scouts 4, planners 2, connector 1,
  executors 34, verifiers 4, scribes 7, reviewers 8, critics 4}; this matches the
  declared `seat_composition` string (`dispatch-declared.json:13`) exactly.
  All 64 `out` paths are unique and inside `reports/round-33/`.
- Owed at close (AGENTS.md:32-39): an **observed-dispatch record** (launches,
  completions, failures, runtime concurrency, actual route; unknown counters
  `null` with owner + reason, never inferred zeroes) and the **closing snapshot**
  that closes `dispatch-declared.json` by path + its SHA-256 at close time. A
  round is not admitted to LOG.md while its own availability record still owes
  the closing snapshot. The declaration itself says so
  (`dispatch-declared.json:28`, `"open-at-seat-close"`).
- **Filename for the round-33 closing snapshot (corrected 2026-10-19):** use
  `reports/round-33/telemetry/availability-close-33.json` — the landed convention
  (`reports/round-{19,25,26,27,28}/telemetry/availability-close-N.json`, schema
  `kotodama-availability-closing-snapshot-v1`, keys `closes` + `closes_sha256`).
  Do **not** name it `closing-snapshot.json`: that name exists nowhere in the repo
  and is the F-X16-3 defect itself — the `SKILL.md:715` one-liner false-fires on
  five already-closed records today (located and reproduced by
  `op/K01-falsifier-scout.md`; corroborated by this seat, §9 items 6-7). S05's F2
  (`scribe/S05-telemetry-draft.md:270`) names the same file.

---

## §5 — Validator acceptance shape (mirror the r32 receipt)

`validation.json` keys, reused from the filed r32 receipt
(`reports/round-32/validation.json`): `round`, `runner`, `runner_sha256`,
`counting_command`, `date`, `measured_at_utc`, `baseline_revision` (read from
`claims.baseline_commit`; keep the receipt key name `baseline_revision` for
cross-round comparability, since round-33's *claims* key is `baseline_commit`),
`claims_declared`, `acceptance_checks_passed`, `claims` (per-claim
`{passed, date, command, failures[], measurement{}}`), `failures`,
`missing_dependencies`, `input_sha256`, `limits`. Behaviour contract:
`--check` prints and never publishes; `--selftest` is dependency-free
positive/negative controls; the default mode guards `reports/round-33/validation.json`
through `tools/harness/receipt_guard.py` (new file, so the guard passes) and
exits 0 iff `acceptance_checks_passed`.

### §5.1 — Schema trap (do not copy r32's coherence block)

`reports/round-32/run-validation.py:927-934` reads `claims.baseline_revision`
and `sum(targets["workers"].values()) == claims["workers"]`. **Round 33's
schema does not carry those keys**: `claims.json:8` is `baseline_commit`
(full 40-hex) and `targets.json` carries `seat_count: 64` + `seats[]`
(no `workers` map). A copied coherence leg fails on a well-formed round. Use
the r33 rules in §6.1.

---

## §6 — Validation-leg spec (machine-checkable)

Format: each leg is `id | claim | command/check | expected | parser hint`. The
fenced JSON block at the end of this section is the same table in a form the
integrator can load directly. `{{}}` inside a command means "resolve from the
landed fragment and pin the path".

### §6.1 Coherence / schema legs (cross)

- **CO1** strict-parse `claims.json` and `targets.json` (duplicate JSON keys
  refused, r32 `strict_json` pattern). Expect `round == 33` in both;
  `claims.baseline_commit` matches `^[0-9a-f]{40}$` and
  `git rev-parse --verify <it>^{commit}` exits 0.
- **CO2** `{c.id: c.axis for c in claims.claims}` ==
  `{"O":"operability","C":"calibration","A":"adjacency"}` and
  `set(claims.axes_in_play) == {"operability","calibration","adjacency"}` with
  three pairwise-distinct axes (REGIMEN.md:26-29).
- **CO3** `claims.freshness_pause_in_force is True` and `"freshness"` absent
  from `axes_in_play` and from every claim's axis (REGIMEN.md:31-33).
- **CO4** dispatch shape: `claims.dispatch.provider_lane == "opencode-go"`,
  `claims.dispatch.model == "deepseek-v4.1-flash"`, `requested_workers == 64`,
  `batched_calls == 1` (REGIMEN.md:13; REGIMEN.md:34-36); `targets.seat_count ==
  64 == len(targets.seats)`; `{s.claim} ⊆ {"O","C","A","cross"}`; every seat has
  non-empty `id`/`role`/`mission`/`out`; the 64 `out` values are unique and each
  starts with `reports/round-33/` (targets.json:5-10).
- **CO5** composition cross-check: role counts of `targets.seats` ==
  `{scout:4, planner:2, connector:1, executor:34, verifier:4, scribe:7,
  reviewer:8, critic:4}` and claim counts == `{O:15, C:22, A:20, cross:7}`
  (measured 2026-10-19, §8 S3; matches `dispatch-declared.json:13`). Report the
  counts as the measurement, not as a threshold alone.
- **CO6** godspeed lead: **not machine-checkable from durable artifacts** — the
  prompts are not persisted and AGENTS.md:30-31 forbids private prompt payloads
  in telemetry. Record `could-not-evaluate` with owner = orchestrator and the
  declaration at `dispatch-declared.json:4` as the only evidence. Never score
  this leg as passed from absence of evidence.

### §6.2 Claim-O legs

- **O1** `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0;
  zero lines matching `^\s+FAIL C`; parse `lesson files:\s+(\d+)` ==
  `index rows:\s+(\d+)` == 33; `findings:\s+0`. (Declaration state for the
  before-value: exit 1, 33/26, findings 2, §8 C1.)
- **O2** `python3 -B reports/round-25/audit/c31-lessons-index-audit.py
  --selftest` → exit 0 and `SELFTEST OK: (\d+)/\1` (28/28 today, §8 C2).
- **O3** README arithmetic: in `corpus/lessons/README.md` the §1 block states the
  file count (33) and §2's closing line matches `\*\*Rows:\s*33\.\s*Files:\s*33\.\*\*`
  (today: `**Rows: 26. Files: 26.**` at README.md:97-98). C34b PASS in O1 covers
  the drift class; O3 is the human-readable twin. Also assert
  `ls corpus/lessons/*.md | wc -l` == 33 == the README's stated count.
- **O4** `test -s reports/round-33/op/O05-falsifier-disposition.md` (the declared
  counting command, claims.json:35) **and** the file is dated `20\d\d-\d\d-\d\d`
  **and** matches either `(?i)fix` + `(?i)control` (located-and-fixed path) or
  `(?i)owner` + `(?i)reason` (carried path). Fail with a named diagnostic naming
  which branch was missing.
- **O5** owner-resolution (C32 leg, O03 fragment): every owner cell proposed for
  the new README rows resolves — live path, operator token, or a round pointer
  whose `reports/round-<n>/` exists. Assert against O03's per-item verdicts:
  zero unresolved, each verdict dated.
- **O6** format classes (C33 leg, O04 fragment): each of the 7 new files'
  measured class ∈ the three documented in README §3 (README.md:111) and
  `formats:` in O1's output contains no class outside that set.
- **O7** negative controls (O06): ≥3 declared controls, each with an expected
  non-zero outcome and a named mutation (fake unindexed file ⇒ C31 FAIL; row for
  a nonexistent file ⇒ C31 FAIL; prose count lie ⇒ C34b FAIL). Leg = the control
  spec exists, is dated, names all three, and the integrator's control run is
  recorded with the observed codes. Run controls only in an isolated copy — the
  README is never mutated in place.
- **O8** regression battery (§8 R1-R5) re-run inside the validator: battery
  selftest exit 0 (`SELFTEST OK 44/44`), craft selftest exit 0 (`10/10` +
  `18/18`), D4 selftest exit 0 (`81/81`), c31 selftest exit 0, handoff exit 0.
  Parse the counts; a green exit with a shrunken count is a failure.

### §6.3 Claim-C legs

- **C1** `calib/open-items-ledger.json` strict-parses; `len(rows) == 12`; ids
  unique; every row carries `{id, item, origin, pointer, status_quo_check,
  disposition_class, evidence}`; `disposition_class ∈ {"fixed-with-evidence",
  "carried-with-owner+reason+next-touch"}`; a `fixed-with-evidence` row carries
  `fix_draft` + a verification string; a carried row carries `owner`, `reason`,
  `next_touch`. Failures name the row id.
- **C2** cross-check vs K03: ledger ids == K03's canonical id set (set equality,
  not just count) and K03 states how 9 d13 data rows became 12 items; the
  receipt cites `SCORECARD.md:443-445` for the "12" and the count provenance
  (this seat's measurement: d13 Decision 4 has 9 data rows, d13:128-138).
- **C3** `calib/C13-consistency.md` exists, dated, verdict green, and its
  per-item table names each of the 12 ids exactly once (no duplicate, no
  contradiction) — parse the table and count.
- **C4** `calib/C14-fix-drafts.md` exists; for every C1 row whose class is
  `fixed-with-evidence` there is one before/after block whose id matches; for
  every draft that targets `SKILL.md`, the cited anchor line resolves at HEAD
  (the quoted text is found at or near the cited line).
- **C5** preservation: `reports/round-1..32/**`, `corpus/lessons/*.md` lesson
  files (README excluded — it is a shared file the integrator may edit) and
  `tools/gates/frozen/round-*` are byte-identical to the declared baseline
  (reuse the r32 `protected_snapshot` approach, run before and after measurement).

### §6.4 Claim-A legs

- **A1** `adj/audit-assembled.md` exists and carries a verdict for each of
  A01-A10: regex each check id (`A0[1-9]|A10`) with a verdict token ∈
  `{green, named-finding}`; every `named-finding` row names an owner; 10/10
  checks present. A missing check id is a failure naming that id.
- **A2** handoff gate: `python3 tools/gates/handoff-packet-check.py
  examples/handoff-packet.sample.md` exit 0 with stdout matching
  `fields=16/16` and `glossary-entries=20` and `findings=0`; the `.yml` twin
  exit 0 with `fields=16/16` and `findings=0` (today it reports
  `glossary-entries=0` — assert 16/16 fields only there, §8 R5).
- **A3** scope: `git ls-files | wc -l` == 2655 at baseline; `git status
  --porcelain` path set ⊆ {`M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/**`}
  ∪ the integrator's close-time files (`SCORECARD.md`, `MANIFEST.json` at the
  fleet root, `../.ufo/reports/round-33/kotodama.md`); any other path is a
  failure naming it. Also assert no write outside this repo except the fleet
  report/telemetry paths.
- **A4** language audit: run the token scan over every `reports/round-33/**`
  file; allow a hit only when it sits in a negation or routed-reference context
  (e.g. `no <token>`, `not a <token>`, `<token> remains the operator's`,
  `routed`, `never absorb`). Exclude this file's §6 fenced spec block (it quotes
  the audit patterns by construction) or treat quoted patterns as allowlisted —
  the A08 fragment must state which rule it used. Zero unallowed hits.
- **A5** PROVINCE: `git log -1 --format=%h -- PROVINCE.md` == `c53782a` and
  `sha256sum PROVINCE.md` equals its baseline value; the audit's own accuracy
  verdict is present and dated.
- **A6** contested scope: the audit text names both contested items (bilateral
  read; L0 contract digest) with current pointers and routed-not-absorbed
  language; a missing item is a failure naming it.
- **A7** history: ≥2 filed r21/r29 adjacency commands re-run with their filed
  verdicts reproduced; A07 names the commands and A13 re-runs them.

### §6.5 Cross / close legs

- **X1** fleet report exists at `../.ufo/reports/round-33/kotodama.md` with all
  four required headings (r32 `SECTIONS` regexes) and a date; the report cites
  `reports/round-33/run-validation.py`.
- **X2** MANIFEST: the fleet-root `MANIFEST.json` gains a kotodama round-33 entry
  with per-axis verdicts. Close-time leg: entry present **or** recorded
  `pending-by-construction` with the reason (the r32 runner forbade a
  pre-existing entry; r33 may assert presence at close since the integrator
  files it in the same pass).
- **X3** telemetry: `telemetry/dispatch-declared.json` SHA-256 recorded; its
  `durable_sources` digests equal the live `claims.json`/`targets.json` digests;
  the observed-dispatch record and the closing snapshot exist or are reported as
  owed with owner + reason. Never infer the missing counters.
- **X4** self-consistency: `validation.json.round == 33`,
  `counting_command == "python3 reports/round-33/run-validation.py"`,
  `acceptance_checks_passed` true only if every leg passed, `limits` non-empty,
  `missing_dependencies` lists every owed path (including any seat fragment still
  absent at measurement). In-flight evidence changes invalidate acceptance
  (re-read digests before writing).

### §6.6 Falsifiers / negative controls for the validator

Each must be exercised in `--selftest` (dependency-free) with a synthetic input,
mirroring the r32 style (`reports/round-32/run-validation.py:984-1099`):

1. ledger with 11 or 13 rows → C1 fails;
2. ledger row with `disposition_class` outside the licensed set → C1 fails;
3. carried row missing `next_touch` → C1 fails;
4. c31 output with `FAIL C31_index_rows_eq_files` → O1 fails;
5. c31 output with `rows 33 / files 26` → O1 fails even at exit 0;
6. `O05` file present but undated → O4 fails;
7. audit with only 9 A-check verdicts → A1 fails;
8. audit naming a `named-finding` with no owner → A1 fails;
9. handoff stdout `fields=15/16` → A2 fails;
10. a round-33 fragment containing a promotion verdict sentence without negation
    → A4 fails (fixture string);
11. fleet report with 3 of 4 headings → X1 fails;
12. `baseline_commit` that is not a resolvable commit → CO1 fails;
13. claims with `freshness` in `axes_in_play` → CO3 fails;
14. targets with 63 seats → CO4 fails;
15. duplicate `out` path across seats → CO4 fails.

### §6.7 Leg table (machine-readable)

```json
{
  "round": 33,
  "runner": "reports/round-33/run-validation.py",
  "receipt": "reports/round-33/validation.json",
  "baseline_key": "claims.baseline_commit",
  "legs": [
    {"id": "CO1", "claim": "cross", "check": "strict json + round==33 + baseline_commit resolves", "expect": "pass"},
    {"id": "CO2", "claim": "cross", "check": "claim axes O/C/A on distinct axes == axes_in_play", "expect": "pass"},
    {"id": "CO3", "claim": "cross", "check": "freshness_pause_in_force true and freshness absent", "expect": "pass"},
    {"id": "CO4", "claim": "cross", "check": "provider/model/64 workers/1 batch; 64 unique out paths under reports/round-33/", "expect": "pass"},
    {"id": "CO5", "claim": "cross", "check": "seat role/claim counts == declared composition", "expect": "pass", "measured_2026_10_19": {"claims": {"O": 15, "C": 22, "A": 20, "cross": 7}, "roles": {"scout": 4, "planner": 2, "connector": 1, "executor": 34, "verifier": 4, "scribe": 7, "reviewer": 8, "critic": 4}}},
    {"id": "CO6", "claim": "cross", "check": "godspeed lead", "expect": "could-not-evaluate", "owner": "orchestrator", "reason": "prompts not persisted; AGENTS.md:30-31 forbids private prompt payloads"},
    {"id": "O1", "claim": "O", "command": "python3 -B reports/round-25/audit/c31-lessons-index-audit.py", "expect": "exit 0; no FAIL C*; rows==files==33; findings 0"},
    {"id": "O2", "claim": "O", "command": "python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest", "expect": "exit 0; SELFTEST OK N/N"},
    {"id": "O3", "claim": "O", "check": "README rows==files==33 prose", "expect": "pass"},
    {"id": "O4", "claim": "O", "command": "test -s reports/round-33/op/O05-falsifier-disposition.md", "expect": "exists; dated; fix+control or owner+reason"},
    {"id": "O5", "claim": "O", "check": "owner cells resolve (O03)", "expect": "0 unresolved"},
    {"id": "O6", "claim": "O", "check": "7 new files' classes within README §3 set (O04)", "expect": "pass"},
    {"id": "O7", "claim": "O", "check": ">=3 negative controls declared (O06) and run isolated", "expect": "pass"},
    {"id": "O8", "claim": "O", "check": "battery 44/44, craft 10/10+18/18, D4 81/81, c31 selftest, handoff 16/16+20/20", "expect": "all exit 0"},
    {"id": "C1", "claim": "C", "check": "ledger 12 rows, schema, licensed classes", "expect": "pass"},
    {"id": "C2", "claim": "C", "check": "ledger ids == K03 set; count provenance stated", "expect": "pass"},
    {"id": "C3", "claim": "C", "check": "C13 consistency green; each id once", "expect": "pass"},
    {"id": "C4", "claim": "C", "check": "C14 draft per fixed row; SKILL.md anchors resolve", "expect": "pass"},
    {"id": "C5", "claim": "C", "check": "filed rounds/lesson files/frozen untouched", "expect": "pass"},
    {"id": "A1", "claim": "A", "check": "audit carries 10/10 A-check verdicts; findings have owners", "expect": "pass"},
    {"id": "A2", "claim": "A", "command": "python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md", "expect": "exit 0; fields=16/16; glossary-entries=20; findings=0"},
    {"id": "A3", "claim": "A", "check": "scope delta subset of declared set; tracked paths 2655 baseline", "expect": "pass"},
    {"id": "A4", "claim": "A", "check": "no unallowed promotion/canon/closure token", "expect": "pass"},
    {"id": "A5", "claim": "A", "check": "PROVINCE last touch c53782a; bytes unchanged", "expect": "pass"},
    {"id": "A6", "claim": "A", "check": "bilateral read + L0 digest restated routed-not-absorbed", "expect": "pass"},
    {"id": "A7", "claim": "A", "check": ">=2 filed r21/r29 commands reproduce", "expect": "pass"},
    {"id": "X1", "claim": "cross", "check": "fleet report with 4 headings + date", "expect": "pass"},
    {"id": "X2", "claim": "cross", "check": "MANIFEST r33 entry present or pending-by-construction", "expect": "pass"},
    {"id": "X3", "claim": "cross", "check": "telemetry digests match live; observed record + closing snapshot or owed", "expect": "pass"},
    {"id": "X4", "claim": "cross", "check": "validation.json self-consistency", "expect": "pass"}
  ]
}
```

---

## §7 — Owed fills (integrator)

| token / leg | owed path | what to fill |
|---|---|---|
| O before/after evidence | `op/O01..O08`, `op/K01`, `op/K02`, `op/P01` | row cells, README delta, O05 branch, controls, baseline receipt numbers |
| C ledger evidence | `calib/K03`, `calib/C01..C16` | 12 canonical ids, per-item dispositions, C13 verdict, C14 drafts |
| A audit evidence | `adj/K04`, `adj/A01..A16`, `adj/A11..A14` | per-check verdicts, scope counts, language scan, pin exposure |
| review/critic deltas | `review/R01..R08`, `cross/X00..X04` | findings to fold or route |
| observed dispatch + closing snapshot | `reports/round-33/telemetry/` | launches/completions/failures/route with owner, UTC window, digests; closing snapshot names `dispatch-declared.json` + its SHA-256 at close |
| fleet report | `../.ufo/reports/round-33/kotodama.md` | final four-section text (this draft) |
| MANIFEST / SCORECARD / LOG | fleet `MANIFEST.json`, `SCORECARD.md`, `LOG.md` | integrator-only writes under the lane identity |

Note for A08/X02: this file's §6 quotes the audit tokens by construction; treat
the §6 fenced blocks as allowlisted spec text when running the language scan.

---

## §8 — Measurements taken by this seat (2026-10-19, round-33 tree)

- **C1** `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1;
  `lesson files: 33`, `index rows: 26`, `queue rows: 49`,
  `formats: {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`,
  `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, `findings: 2`;
  C31-1 lists round-26..round-32.md; C34-2 `stated [26,26] measured [26,33]`.
- **C2** same tool `--selftest` → exit 0, `SELFTEST OK: 28/28 checks passed`.
- **R1** `python3 tools/check-gate-battery.py --selftest` → exit 0,
  `SELFTEST OK 44/44 controls behaved as expected`.
- **R2** `python3 tools/check-craft-exercise.py --selftest` → exit 0,
  `10/10 tamper cases detected`, `CLI-SELFTEST OK 18/18`.
- **R3** `python3 tools/assemble-culture-d4.py --selftest` → exit 0,
  `81/81 checks passed`.
- **R5** `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md`
  → exit 0, `fields=16/16 glossary-entries=20 findings=0`; the `.yml` twin → exit 0,
  `fields=16/16 glossary-entries=0 findings=0`.
- **S1** `git log -1` → `139e3b662900557afe54f632b468619593dc9fcb`; `git ls-files | wc -l`
  → 2655; `git status --porcelain` → ` M LOG.md`, `?? REGIMEN.md`,
  `?? reports/round-33/`.
- **S2** `sha256sum reports/round-33/claims.json reports/round-33/targets.json`
  → `ba69090f90c007064fb9c08d04b2fc07ec1514eddf09937bc190021684b3fb12`,
  `342c8f80eb857f96109fc7fcc3d1b816be1264898a25c3f4f8786451f27df13f` — both
  equal the digests declared in `telemetry/dispatch-declared.json:20-25`.
- **S3** seat census from `targets.json` → claims {O:15, C:22, A:20, cross:7};
  roles {scout:4, planner:2, connector:1, executor:34, verifier:4, scribe:7,
  reviewer:8, critic:4}; 64 unique `out` paths.
- **S4** `ls corpus/lessons/*.md | wc -l` → 33; `ls -d ../.ufo/reports/round-33`
  → absent; r33 MANIFEST entries → 0.
- **S5** `git log --format=%h -- PROVINCE.md` → newest `c53782a`.
- **S6** `test -s reports/round-33/op/O05-falsifier-disposition.md` → false (absent).

Honest limits: every after-value in §3 is a requirement from
`claims.json`, not an observation — no fragment existed at this seat's first cut.
The §6 leg spec is a design the integrator must implement and self-test; this
seat executed no part of `run-validation.py`. §9 records what landed later.

## §9 — Landed-fragment cross-check (addendum, 2026-10-19, same wave)

Read by this seat after the draft was written, in `reports/round-33/`:
`op/K01-falsifier-scout.md`, `op/K02-lessons-census.md`, `op/O01-row-drafts.md`,
`op/O03-owner-checks.md`, `op/O04-format-checks.md`, `op/O07-baseline-receipt.md`,
`calib/K03-open-items.md`, `calib/P02-plan.md`, `calib/C01-item-01.md`,
`calib/C07-item-07.md`, `calib/C12-item-12.md`, `calib/C16-receipt.md`,
`adj/K04-method-scout.md`, `adj/A01-province.md`, `adj/A10-receipt.md`,
`adj/A13-verify-a07-a09.md`, `adj/A15-audit-draft.md`, `adj/A16-shonen-material.md`,
`scribe/S01-op-receipt.md`.

Still absent at this read (exact owed paths): `op/O05-falsifier-disposition.md`
(the claim-O counting-command artifact — leg O4 stays owed), `op/O02`, `op/O06`,
`op/O08`, `op/P01`, the unlanded `calib/C0*`, the unlanded `adj/A*`, all
`review/R01..R08`, all `cross/X00..X04`, `scribe/S02`, `scribe/S03`,
`scribe/S05`, `reports/round-33/run-validation.py`, the fleet report, and the
observed-dispatch + closing-snapshot telemetry records. Read the `## Owed`
inventory below with this note.

Leg amendments forced by the landed fragments:

1. **C2 (binding):** the canonical id set is **OI-01..OI-12**
   (`calib/K03-open-items.md:62-73`) with the adopted expansion convention at
   `K03:36-42` — 3 design debts + 3 box-1 citation conditions + 1 cold-run
   cluster + 2 lore-owned + 1 rubric gap + 1 devin telemetry + 1 adapter
   semantics = 12. The ledger's ids must equal that set; a count-only check is
   insufficient. K03 also records the literal (9) and maximal (15) conventions
   it rejected (`K03:31-42`).
2. **C2b (binding, honesty):** K03 marks the provenance of the numeral "12" as
   `to-verify`, naming a plausible contamination path — the D13 table's own
   "12 D4 garment-form holds" hold-count (`K03:45-52`, `dossier-d13:130`). The
   ledger/receipt must carry that caveat; a receipt asserting 12 as a filed fact
   fails this leg.
3. **O8 counts cross-seat corroborated:** `op/O07-baseline-receipt.md` records
   the same values this seat measured independently (battery selftest `44/44`;
   craft `10/10` + `18/18`; D4 `81/81`; c31 selftest `28/28`; capture window
   2026-10-19T03:52:07Z–03:52:30Z), so the expected counts in leg O8 are now
   corroborated by two seats rather than one.
4. **O8 addition:** O07 also records the battery's non-selftest mode —
   `pass 7, fail 0, unevaluable 0`, `baselines.summary.coverage "10/10"`,
   `baselines_found 20, pinned 20, gates_registered 10, gates_uncovered []`. That
   is the "battery 10/10" the claim-O threshold names; leg O8 must assert this
   mode, not only the selftest.
5. **A5 corroboration:** `adj/A01-province.md` is landed; this seat's
   `git log -- PROVINCE.md` reading at §8 S5 is its independent twin.
6. **X3 leg amendment — the closing-snapshot filename (this file's §4 note was
   corrected in place).** The round-33 closing snapshot goes at
   `reports/round-33/telemetry/availability-close-33.json`, mirroring the landed
   convention (`reports/round-{19,25,26,27,28}/telemetry/availability-close-N.json`:
   schema `kotodama-availability-closing-snapshot-v1`, keys `closes` +
   `closes_sha256`). The `SKILL.md:715` one-liner is **not** the authority for the
   name: it hardcodes `closing-snapshot.json`, which exists nowhere in the repo,
   and false-fires on five already-closed records. `scribe/S05-telemetry-draft.md:270`
   (F2) reaches the same filename; `op/K01-falsifier-scout.md` locates and
   reproduces the mismatch (F-X16-3, `corpus/lessons/round-32.md:41`, route
   Q-32-1 at `:55`) and notes the live schema key is `closes`, not
   `closes_record`. The validator leg should mirror the working implementation at
   `reports/round-31/run-validation.py:780,792-812`, not the SKILL one-liner.
7. **Independent corroboration of K01's reproduction (this seat's own runs,
   2026-10-19).** Verbatim `SKILL.md:715` one-liner → exit 0 and exactly 5 rows
   (`reports/round-19/availability.json`, `reports/round-25..28/availability.json`);
   substance probe over those five → `schema == kotodama-availability-closing-snapshot-v1`,
   `closes == reports/round-N/availability.json`, `closes_sha256 == live sha256`
   all true (5/5); `find reports corpus tools -name 'closing-snapshot.json'` → 0
   matches; record census → 9 `reports/round-*/availability*.json` files: the 5
   open-at-seat-close records above, plus 3 round-10 attempts and 1 round-5
   attempt (those four carry `state: None`, pre-convention). K01's finding
   therefore stands reproduced by a second seat, and leg O4's disposition
   artifact must choose the re-key or the clause reword (K01 §5 gives both, with
   controls).

## Owed

All 64 seat fragments (see §7) — in particular `op/O01..O08` (O05 is still
absent at this read and is the claim-O counting-command artifact), `op/K01`,
`op/K02`, `op/P01`, `calib/K03`, `calib/C01..C16`, `adj/K04`, `adj/A01..A16`,
`review/R01..R08`, `cross/X00..X04` — plus the round-33 telemetry
observed-dispatch record and the closing snapshot at
`reports/round-33/telemetry/availability-close-33.json` (§9 item 6),
`../.ufo/reports/round-33/kotodama.md`, and
`reports/round-33/run-validation.py` itself.

## Citations

- `REGIMEN.md:13,26-36,52-58` — schedule position 1-3, per-round contract, done-when.
- `reports/round-33/claims.json:8,16,18,19-64` — baseline_commit, axes, pause, claims + counting commands.
- `reports/round-33/targets.json:3-10,12-83` — seat_count 64, shared_rules, seats.
- `reports/round-33/telemetry/dispatch-declared.json:4,13,20-25,28` — declaration, composition, digests, open-at-seat-close.
- `SCORECARD.md:3,427-445` — axes list; round-32 record and routed debt ("12 standing open items").
- `corpus/lessons/README.md:31-40,61-75,97-98,111,202,307` — counting command, row format, "Rows: 26. Files: 26.", §3 formats, queue arithmetic, revision 2.
- `reports/round-25/audit/c31-lessons-index-audit.py` — executed (§8 C1/C2).
- `reports/round-32/run-validation.py:50-55,927-934,984-1099` — SECTIONS contract, r32 coherence keys, selftest style.
- `reports/round-32/validation.json` — receipt key set.
- `reports/round-32/dossier-d13-operator-decisions.md:123-138` — Decision 4, 9 data rows.
- `reports/round-32/dossier-d11-shonen-boxes.md:44-52,145-150,203-208` — box-1 inventory closed, N1/N4/N5/N7 open, box table.
- `reports/round-32/final-dossier.md:1-35` — dossier shape and non-author declaration.
- `SHONEN.md:3-11` — four boxes and mark rule.
- `PROVINCE.md` (whole) + `git log -- PROVINCE.md` → `c53782a` — province scope, last touch.
- `AGENTS.md:15-39,40-42` — telemetry rules, close-what-you-open, stray fence observation.
- `SKILL.md:522,713-715` — checklist heading; close-what-you-open audit item (its audit command hardcodes `telemetry/closing-snapshot.json`).
- `../.ufo/reports/round-32/kotodama.md:16,70,88,109` — four-section report shape.
- Commands in §8 (C1, C2, R1-R3, R5, S1-S6) — this seat's measurements, 2026-10-19.
