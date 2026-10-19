- Seat: S04 | scribe | cross | date 2026-10-19 | baseline 4a7aede

# S04 — round-35 integration dossier draft + validation-leg spec

Purpose: give the integrating parent (a) the fleet-report draft text for
`../.ufo/reports/round-35/kotodama.md` and (b) a machine-checkable leg spec it
implements as `reports/round-35/run-validation.py`. Every value in §8 was
measured by this seat at the round-35 tree on 2026-10-19 with the commands in
§8; every value keyed to a fragment path is a placeholder the integrator fills
from the landed fragment.

Dependency state at this seat's cut (2026-10-19): `reports/round-35/` contains
only `claims.json`, `targets.json` and four telemetry files (§8 M1). **All 64
declared seat fragments were unwritten** at that cut, including every one this
draft would otherwise quote; `../.ufo/reports/round-35/` does not exist (§8
M12). Every `{{...}}` token below is therefore an owed fill listed in `## Owed`.
§9 records five declaration-level defects this seat found while measuring — they
change what the validator may assert and must be read before implementing §6.

**Non-author declaration:** this seat authored no lane artifact before this
round. No promotion, canon, clearance, or closure verdict is claimed anywhere in
this file; each such token appears only as a negation, a routed reference, or a
quoted pattern (§6.7).

---

## §1 — Fleet-report draft (four required sections)

Heading set required by the filed contract (`reports/round-34/run-validation.py:319`,
the four `SECTIONS` strings it matches): `Work performed`, `Landed changes`,
`Before → after measurements`, `SHONEN`. Reuse the same regex pair for round 35.

### Draft header

```text
# kotodama — round 35 report (2026-10-19)

Regimen 2 (REGIMEN.md:13), loop 1, build 3 of 3. One 64-seat batched AgentSwarm
on `opencode-go / deepseek-v4.1-flash`. Declared allocation is
`opencode-go-3` (claims.json:11, dispatch-declared.json:8); the observed route
was **opencode-go key 1** — keys 3, 4 and 5 each failed at launch with a 402
"insufficient account funds" and zero seats started, recorded in
`reports/round-35/telemetry/availability-attempt-{1,2,3}.json`; key 1 is the
round-robin's only proven-live key this loop (§9 item 2). Declared baseline
`4a7aede` (claims.json:8; expands to
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`, §8 M4); this round's work lands in
the same integrating pass that files this report. Claims C/O/A on
coverage/operability/adjacency (claims.json:17,20-65); freshness axis-move claims
stay paused (claims.json:18). Seat accounting: `seat_count: 64` with 64 declared
rows — the round-34 64-vs-63 deviation does **not** repeat (§9 item 1). Dispatch
honesty: allocation is declared at `reports/round-35/telemetry/dispatch-declared.json`
(digest-pinned); observed launches/completions/failures are `{{counts or null}}`
— {{owner}} — with the closing snapshot owed once validation.json lands
(AGENTS.md:32-39).
```

### Draft — Work performed

```text
- **Coverage (claim C):** the two thinnest partitions gain ten sourced entries —
  culture-material 18 → 24 (+6) and myth-symbol 19 → 23 (+4); total 201 → 211.
  Each entry is gap-named, frontmatter-complete (source / verified-at / recheck /
  scope), decision-record carrying, and source-resolving; `corpus/README.md` is
  reconciled across all four count surfaces (the two section headers, the totals
  line, the counts footer) and the index rows. Before: 21/19/18/29/20/94 = 201
  files, index rows 201 == 201 files, inventory `totals.files` 201 (§8 M5, M6,
  M7). After: `{{partition counts 24/23/211; audit parity per §6.2}}`.
  {{C01-C17 pointers}}.
- **Operability (claim O):** the R34-N1 hardening. Before: replaying the r6 row
  after the CLAIMS_MAP move dies with an uncaught
  `KeyError: 'reports/round-20/handoff/claims-map.md'` — reproduced by this seat
  in an isolated copy, exit 1 via traceback (§8 M9). The refusal is correct (the
  r6 read set names a member the live assembly no longer reads) but the mechanism
  is an unhandled exception, so the designed diagnostic leg is unreachable for
  this class. After: a named diagnostic carrying the unresolvable member; the
  digest-mismatch leg preserved. {{O01-O11 pointers}}.
- **Adjacency (claim A):** bleed-scope audit of every surface rounds 33-34
  created or edited — the declared-in-r7 packet pair + claims-map + repin.json,
  `tools/harness/receipt_guard_adoption.py` + its inventory, the `examples/`
  digest repoints, the round-33/34 `SKILL.md` and `AGENTS.md` and ceilings edits,
  the box-1/reissue records — re-scanned for cross-domain language, ownership
  drift and PROVINCE conformance, with PROVINCE itself re-verified against the
  post-edit tree. Before: no consolidated adjacency pass covered those surfaces
  (the r33 audit predates the r34 edits). After: `{{per-surface verdicts per
  §6.4}}`. {{A01-A11 pointers}}.
```

### Draft — Landed changes

```text
- `corpus/knowledge/culture-material/*.md` — six new entries (the claim-C
  deliverable); drafted as fenced blocks by C01-C06, landed by the integrator.
- `corpus/knowledge/myth-symbol/*.md` — four new entries; drafted by C07-C10,
  landed by the integrator.
- `corpus/README.md` — index revision: two section headers, the totals line, the
  counts footer, and ten new index rows (drafted by C11, applied by the
  integrator).
- `tools/exercise-handoff-e2e.py` — the R34-N1 hardening (the claim-O
  deliverable): the read-set member resolution catch at the site this seat
  located (§8 M9); drafted with before/after text by O01, never edited by a seat.
- `reports/round-35/validation.json` — this round's acceptance receipt
  (integrator-run; the runner never publishes under `--check`).
- `reports/round-35/telemetry/` — the three availability attempts and
  dispatch-declared (filed) plus the observed-dispatch record and the closing
  snapshot owed once validation.json lands.
- Filed bytes: **zero** writes to `reports/round-1..34/**`, `corpus/lessons/*.md`,
  `tools/gates/frozen/**` (`{{P1 verdict}}`); `reports/round-34/handoff/declared-in-r7/**`
  freeze bytes stay pinned (§6.3 O6).
```

### Draft — Before → after measurements

Fill from §3's table (same numbers, prose form). Rule: every after-value names
the fragment that measured it and the counting command; every before-value below
was measured by this seat and is reproducible from §8.

### Draft — SHONEN

```text
All four boxes: {{untouched this round; r24 verdicts and the r30/r33/r34
re-surveys stand as filed}}. Conditions carried named, none silently closed:
- box 1 (decision tables/errors/checklists/sources): verified-with-conditions;
  the inventory condition closed at r30 (28/28) and was re-pinned durable at r34
  (claim C); citation-level conditions 2-4 remain open
  (reports/round-32/dossier-d11-shonen-boxes.md:44-52,205).
- box 2 (end-to-end domain task): verified-with-conditions; standing design debts
  named (the 12 D4 garment-form holds + owed slots, `head2` empty proper domain,
  the RL-3 ceiling) — design, not defect (d11:206; d13:130-132).
- box 3 (cold-run executability): verified-with-conditions; N1/N4/N5/N7 remain
  open as filed (d11:145-150,207).
- box 4 (no bleed / PROVINCE accurate): verified-with-conditions; standing
  readings 3a/3b/3c by design (d11:208).
No promotion decision is taken or implied here; the decision remains
operator-owned (SHONEN.md:10-11).
```

---

## §2 — Integration order and collision notes

1. Land the C build first (ten corpus entries + `corpus/README.md`), because
   claim A's surfaces include the resulting tree and the C legs measure the
   landed counts. Then the renderer hardening, then `run-validation.py`, then
   telemetry, then the fleet report, then SCORECARD/LOG/MANIFEST.
2. Collision surface: `tools/exercise-handoff-e2e.py` is touched only by O01's
   draft (integrator applies); `corpus/knowledge/**` and `corpus/README.md` are
   written only by the integrator from C01-C11's fenced drafts; `LOG.md` is
   integrator-only (`targets.json:5-13`). **No shared file is written by two
   seats** — verified against the 64 `out` paths, which partition cleanly into 9
   directories (§8 M3).
3. **`corpus/README.md` is NOT in the protected set.** The r34 preservation leg's
   protected regex (`reports/round-34/run-validation.py:268`) covers
   `reports/round-1..33/**`, `corpus/lessons/*.md` (excluding `README.md`) and
   `tools/gates/frozen/round-*` only. Round 35 must widen the round range to
   `1..34` and must **not** add `corpus/knowledge/**` or `corpus/README.md` —
   they are this round's deliverables. Widening the range is what makes the
   r34 freeze bytes immovable (§6.3 O6).
4. Two filed-round facts the integrator should carry: the round-34 fleet report
   already records R34-N1 as routed to renderer hardening
   (`../.ufo/reports/round-34/kotodama.md:29-30`), so claim O closes a routed
   finding rather than opening one; and `reports/round-34/validation.json` is now
   inside the protected set, so the r34 receipt's digest (`ba2fa4dc…`, LOG.md
   round-34 entry) must stay put.

---

## §3 — Before → after table (fill the after column from fragments)

| claim | axis | before (measured 2026-10-19 by S04, §8) | after required (claims.json) | counting command |
|---|---|---|---|---|
| C | coverage | 21/19/18/29/20/94 = 201 files; index rows 201 == 201 files; inventory `totals.files` 201; README rev 1.9 with headers `(21)/(19)/(18)/(29)/(20)/(94)`, totals line 201, footer `201` / `21/19/18/29/20/94` — currently self-consistent (§8 M5, M6, M7) | culture-material 24, myth-symbol 23, total 211; every new entry audited clean by two independent auditors; README counts == live census on **all four** count surfaces; inventory total 211; zero fabricated sources | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done`; `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`; `python3 reports/round-35/run-validation.py` |
| O | operability | r6-row replay dies with an uncaught `KeyError: 'reports/round-20/handoff/claims-map.md'` at `tools/exercise-handoff-e2e.py:3822` (`assembly.digests[rel]` indexed directly while the drift check one line above uses `.get()`); exit 1 via traceback; renderer selftest green at **39 v3 controls / 40 result lines** (17 controls on the default profile — a different suite); r7 default chain exit 0, packet_sha256 `45f57132…` (§8 M8, M9) | named diagnostic carrying the unresolvable path at the r6 replay; the designed E2E-DIGEST digest-mismatch path unchanged; v3 selftest green at ≥41 controls incl. the new refusal control; r7 default chain still exit 0; no freeze bytes move | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`; `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`; `python3 reports/round-35/run-validation.py` |
| A | adjacency | rounds 33-34 edited shared/live files and created new durable artifacts; no consolidated adjacency pass covers those surfaces | per-surface verdicts (green or named-finding with owner); zero unfiled cross-domain bleed; PROVINCE owns/refuses accurate at HEAD; contested items routed-not-absorbed; no promotion/canon/clearance/closure language outside negations | `python3 reports/round-35/run-validation.py` |
| all | — | regressions green at this seat's cut: renderer v3 selftest exit 0 (39 controls), r7 chain exit 0, protected drift 0 rows (§8 M8, M10) | unchanged or better; zero regressions | §6 `CO9` |

---

## §4 — Telemetry material (draft)

- `telemetry/dispatch-declared.json` (filed, sha256 `93e205a2…`): owner =
  orchestrator (goal-mode parent); declared 2026-10-19T08:05:00Z; allocation =
  `opencode-go-3` / deepseek-v4.1-flash / 64 requested workers / 1 batched
  AgentSwarm call; durable digests `claims.json` = `ccfaafc3…` and
  `targets.json` = `56ad0392…`. **This seat re-verified both against live bytes
  (§8 M2) — they match.** Its `authoring_note` (`:28`) records that targets.json
  was first authored with 60 seats and corrected to 64 before dispatch, so the
  pinned digest is the corrected one — do not "fix" a 60-seat ghost.
- `telemetry/availability-attempt-{1,2,3}.json` (filed): the three 402 refusals
  on keys 3/4/5, each recording 64 requested, **0 launched, 0 completed, 64
  failed** with the identical error and the seat-id ranges
  (agent-130..193, agent-194..257, agent-258..321). attempt-3 carries the
  `key_census_so_far` line (key 1 r33 live 64/64; key 2 r34 live 63/63; keys 3-5
  402) and names the key-1 re-dispatch as a recorded deviation. This is the
  round's availability evidence and the reason §9 item 2 exists.
- Composition cross-check (this seat's count, §8 M3): **64 seat rows** by claim
  {C: 24, O: 16, A: 15, cross: 9} and by role {scout 4, planner 2, connector 1,
  executor 26, verifier 8, scribe 10, reviewer 9, critic 4}; 64 unique `out`
  paths, all under `reports/round-35/`. The declaration's own prose
  `seat_composition` string (`:13`) is a lossy paraphrase ("17 C-seats … 11
  O-seats, 11 A-seats, 9 reviewers, 4 critics, 5 scribes") that totals 64 but does
  not equal the measured role census; report the **measured** census and treat the
  prose as declaration colour, not as a threshold (§9 item 3).
- Owed at close (AGENTS.md:32-39): an **observed-dispatch record** (launches,
  completions, failures, runtime concurrency, actual route = key 1; unknown
  counters `null` with owner + reason, never inferred zeroes) and the **closing
  snapshot** that closes `dispatch-declared.json` by path + its SHA-256 at close
  time. The declaration itself says so (`dispatch-declared.json:30`,
  `"open-at-seat-close"`).
- **Closing-snapshot filename (binding):**
  `reports/round-35/telemetry/availability-close-35.json`, mirroring the landed
  convention (`reports/round-{19,25,26,27,28,33,34}/telemetry/availability-close-N.json`;
  schema `kotodama-availability-closing-snapshot-v1`, keys `closes` +
  `closes_sha256` + `closed_fields` + `could_not_recover` + `sources`, as at
  `reports/round-33/telemetry/availability-close-33.json`). Do **not** name it
  `closing-snapshot.json` — that name exists nowhere in the repo and is the
  F-X16-3 defect the round-33 lane already reproduced. The live instrument globs
  `telemetry/availability-close-*.json` and keys the audit on `closes` +
  `closes_sha256` (`SKILL.md:730-732`), so mirror that. The closing snapshot
  must fill the key-1 route the declaration left open, citing attempt-3's
  `disposition` — that is exactly the "close what you open" obligation this round
  created.

---

## §5 — Validator acceptance shape and the four schema traps

Mirror the round-34 receipt key set (`reports/round-34/validation.json`):
`round`, `runner`, `runner_sha256`, `counting_command`, `date`, `measured_at_utc`,
`baseline_revision`, `baseline_expanded`, `claims_declared`, `acceptance_checks_passed`,
`claims` (per-claim `{passed, date, command, failures[], measurement{}}`),
`failures`, `missing_dependencies`, `target_outputs`, `input_sha256`, `limits`.
Behaviour: `--check` prints and never publishes; `--selftest` is dependency-free
positive/negative controls; the default mode guards `reports/round-35/validation.json`
through `tools/harness/receipt_guard.py` (a new file, so the guard passes) and
exits 0 iff `acceptance_checks_passed`.

### Trap 1 — the baseline is declared twice; verify, don't trust

`reports/round-35/claims.json:8-9` carries **both** `"baseline_commit": "4a7aede"`
(7 hex, not 40) **and** `"baseline_expanded": "4a7aede22cd8395b01ce6dd9f46bcae364ca24e4"`;
`telemetry/dispatch-declared.json:17` carries the full id in the same key name.
Round 34's Trap 1 (short-only id) is therefore half-mitigated — but the declared
expansion is still a *claim*, not a measurement. `CO1` must (a) run
`git rev-parse --verify 4a7aede^{commit}`, (b) assert the result equals the
declared `baseline_expanded` **and** the dispatch-declared id, and (c) record all
three tokens in the measurement. Never rewrite the declared value.

### Trap 2 — the seat-count deviation does NOT repeat; do not copy round 34's constant

`targets.json:3` declares `seat_count: 64` and the `seats` array has **64**
entries (§8 M3). Round 34's validator asserts `len(seats) == 63` as its measured
value (`reports/round-34/run-validation.py:122`) and reports a named deviation.
Copying that line into round 35 **fails a well-formed round**. Implement `CO4` as
`len(seats) == 64` with no deviation block. If the integrator wants the
deviation machinery kept for future rounds, it must be driven by the measured
count, not a hard-coded 63.

### Trap 3 — the provider key is a declared-vs-observed divergence

`claims.json:11` declares `provider_lane: "opencode-go-3"` and
`dispatch-declared.json:8` agrees; the batch actually ran on **key 1** (§4,
attempt-3's `disposition`). AGENTS.md forbids conflating requested allocation with
observed route. Implement `CO5` as two separate assertions plus a named deviation:
assert the *declared* allocation exactly (lane `opencode-go-3`, model
`deepseek-v4.1-flash`, 64 requested workers, 1 batched call), then record the
observed route (`opencode-go-1`), the three 402 attempts as its evidence, and the
owner (orchestrator) — as a deviation row, never as a leg failure and never as a
silent pass. Do **not** edit `claims.json`: its digest is pinned at
`dispatch-declared.json:20-24` and verified live (§8 M2).

### Trap 4 — the r6 replay's exit code does not discriminate the fix

Claim O's counting command says `(expect: exit 1, named diagnostic)`. Measured:
the replay **already exits 1 today** — via an uncaught `KeyError` traceback
(§8 M9). A leg asserting `exit == 1` therefore passes both before and after the
hardening and proves nothing. The discriminator must be: exit non-zero **and** a
named diagnostic token in the output **and** the unresolvable path named **and**
`Traceback` absent from stderr. See §6.3 O2/O3 and §9 item 4.

---

## §6 — Validation-leg spec (machine-checkable)

Format: `id | claim | command/check | expected | parser hint`. `{{}}` means
"resolve from the landed fragment and pin the path". Every leg below was
requested by this seat's mission: partition counts 24/23/211 + entry-audit parity
+ README equality; named-diagnostic regex + exit codes + selftest count;
per-surface audit verdicts + PROVINCE accuracy; preservation incl. corpus
baseline bytes; language; report/telemetry.

### §6.1 Coherence / schema legs (cross)

- **CO1** strict-parse `claims.json` and `targets.json` (duplicate JSON keys
  refused, round-34 `strict_json` pattern at `reports/round-34/run-validation.py:47-56`).
  Expect `round == 35` in both; baseline three-way agreement (Trap 1); record the
  short token, the declared expansion and the git-resolved expansion separately.
- **CO2** `{c.id: c.axis for c in claims.claims}` ==
  `{"C": "coverage", "O": "operability", "A": "adjacency"}` and
  `set(claims.axes_in_play) == {"coverage", "operability", "adjacency"}` with
  three pairwise-distinct axes (REGIMEN.md:26-29; claims.json:17-20).
- **CO3** `claims.freshness_pause_in_force is True` and `"freshness"` absent from
  `axes_in_play` and from every claim's axis (claims.json:18).
- **CO4** seat census (Trap 2): `len(targets.seats) == 64` == `seat_count`; every
  `out` unique and under `reports/round-35/`; non-empty `id`/`role`/`mission`.
  No deviation block. Report the measured count as the measurement.
- **CO5** dispatch shape + provider deviation (Trap 3): declared allocation
  asserted exactly; observed route recorded as a named deviation with the three
  attempt records as evidence and owner = orchestrator.
- **CO6** composition cross-check: role counts == `{scout 4, planner 2,
  connector 1, executor 26, verifier 8, scribe 10, reviewer 9, critic 4}` and
  claim counts == `{C 24, O 16, A 15, cross 9}` (measured 2026-10-19, §8 M3).
  Report the counts as the measurement, not as a threshold alone. The
  declaration's prose `seat_composition` string is not an assertion surface
  (§9 item 3).
- **CO7** lowest-axis rule: `claims.axes_in_play` contains `coverage`, and the
  coverage claim's axis is the least-worked non-paused axis per the declaration's
  own `lowest_axis_reasoning` (claims.json:17-19). Assert the *presence* of the
  coverage axis and that no freshness axis-move claim exists; do not re-derive the
  priority ordering (that is the orchestrator's declaration, not a measurement).
- **CO8** godspeed lead: **not machine-checkable from durable artifacts** — the
  prompts are not persisted and AGENTS.md:30-31 forbids private prompt payloads
  in telemetry. Record `could-not-evaluate` with owner = orchestrator and the
  declaration at `dispatch-declared.json:6` as the only evidence. Never score this
  leg as passed from absence of evidence.
- **CO9** regression floor: renderer selftest exit 0 and `--profile v3 --quiet`
  exit 0 with `packet_sha256 == 45f57132…` (§8 M8). This is the "no axis harmed"
  leg; it is deliberately independent of the O legs so that a bad hardening shows
  up as a regression rather than as its own verdict.

### §6.2 Claim-C legs (coverage: 24/23/211 + audit parity + README equality)

- **C1 — partition counts.** Run
  `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
  and assert the vector is `21/23/24/29/20/94` (sum 211). Assert **per partition**,
  not just the total: a 211 total with the +10 landed in the wrong partitions is
  the failure mode this leg exists for. Record the before vector (21/19/18/29/20/94)
  from §8 M5 in the measurement so the delta is visible.
- **C2 — no partition drift outside the two named.** Assert `linguistics == 21`,
  `synthesis == 29`, `verification == 20`, `civilizations == 94` exactly. The claim
  names only culture-material and myth-symbol; a change anywhere else is a defect
  even if the total still reads 211.
- **C3 — inventory total.** `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → `totals.files == 211`, and every file appears exactly once in `files[]`.
  Record `lines`/`raw_lines`/`marker_occurrences` as the measurement (before:
  36395 / 717 / 655, §8 M6) — they must grow, and a *shrink* is a named finding.
- **C4 — README equality on all four count surfaces.** `corpus/README.md` must
  agree with the live census at:
  (a) the section header `## culture-material/ (24)` and `## myth-symbol/ (23)`
  (before: `:169` reads `(18)`, `:147` reads `(19)`);
  (b) the totals line (before: `:9` region reads 201);
  (c) the counts footer (before: `:473` reads `(total 201 files; directory totals 21/19/18/29/20/94)`);
  (d) index-row parity: the number of `^- \`<name>.md\`` rows equals the live
  file count (before: 201 == 201, §8 M7).
  **This four-surface leg is the direct response to the r28 defect**: a sweep that
  checked rows but never read the footer went green over a stale claim
  (`corpus/README.md:19-33`). A leg that checks only the totals line reproduces
  it. Assert the footer vector in its declared order
  (linguistics/myth-symbol/culture-material/synthesis/verification/civilizations)
  and assert the new revision note exists at the top of the file.
- **C5 — entry audit parity (two independent auditors).** Every one of the ten new
  entries passes: frontmatter 4/4 (`source` / `verified-at` / `recheck` / `scope`)
  or a documented 3/4 class; decision record present; gap named in-file; every
  source pointer resolves **or** is marked `to-verify` in-file. The leg reads the
  two auditors' fragments (C13 for entries 1-5, C14 for entries 6-10, C17's
  sample) and asserts: both auditors ran, their per-entry verdicts cover all ten
  entries exactly once, and any disagreement between them is filed as a defect
  rather than resolved by the validator. **A green single-auditor result is a
  failure of this leg**, because the claim's threshold is "two independent
  auditors".
- **C6 — zero fabricated sources.** Assert the union of `to-verify` markers across
  the ten drafts equals the count the audit fragments report, and that every
  non-`to-verify` citation resolves by `test -e`/grep at HEAD. The leg must not
  accept an empty `to-verify` set as proof of resolution — it must re-resolve the
  pointers itself. Report both counts.
- **C7 — the new entries carry no bleed.** Each draft's language scan for
  canon/clearance/closure grant frames outside negations; contested items routed
  to lore-shokunin, never absorbed. Delegates the token machinery to L1 (§6.7) but
  scopes the assertion to `corpus/knowledge/**` text as quoted in the C fragments
  (L1 itself scans `reports/round-35/**` only — see §9 item 5).
- **C8 — the lessons partition is untouched.** `ls corpus/lessons/*.md | wc -l` ==
  33 (measured, §8 M5). The ten new entries land in `corpus/knowledge/`; a change
  to the lessons count means the wrong tree was written. R09's question (whether
  any counting command beyond `corpus/README.md` needs updating) is answered here:
  the lessons index and the 33-file partition do not move.

### §6.3 Claim-O legs (named diagnostic + preserved digest path + selftest count)

**Id reconciliation (binding).** Seat O08 owns the claim-O leg spec and ships a
paste-ready, content-addressed implementation at
`reports/round-35/op/O08-validation-legs.md:202-332` with ids **O1** (r6 replay),
**O2** (selftest), **O3** (r7 regression), **O4** (freeze bytes), **O5** (patch
present), **O6** (validator fences). The integrator should implement **that id
set**, not the one this section originally proposed. What follows therefore maps
onto O08's ids, keeping only the legs O08 does not already cover as extensions
**O7/O8**.

- **O1 (O08) — the named diagnostic, the claim's centre of gravity.** See the
  bullets below under "the r6 replay"; O08's version is authoritative and its
  regexes were self-checked against the measured bytes.
- **O2 (O08) — selftest count and green.** The claim-relevant suite is the **v3**
  one: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0
  and the header's `plus (\d+) controls` is **≥ 41** (before: **39**, with 40
  `^  - ` result lines — measured independently by this seat and by K03/O08, §8
  M8). **O02's landed design makes the actual number 43**: four new control lines
  — `m13a` (synthetic superseded row) and `m13b` (filed r6-row replay) for the new
  refusal, `m14a` (flipped read-set sha) and `m14b` (content-tampered live member)
  for the preserved path (`op/O02-controls.md:114-169,252,272`). So the floor is
  satisfied with margin; assert `>= 41` **and** the content anchors, never an exact
  number alone (§11.8). Parse the count from the header and treat a green exit with
  a *shrunken* count as a failure. **Do not run the default-profile suite by
  mistake:** plain `--selftest` (no `--profile`) runs a different, smaller suite —
  17 controls, 18 result lines (§8 M8) — and the superseded-row control lands in
  the v3 suite. This is a live trap: claim O's own counting command
  (`claims.json:47`) omits `--profile v3` while its threshold requires the v3
  control, so the declared command and the declared threshold point at different
  suites (§9 item 6). O08's content anchors (an `E2E-READSET` control line naming
  the superseded row and its exit code; the preserved `m12b` `E2E-DIGEST` + exit 1
  line; the `m12a` exit 2 `E2E-BASELINE` line) are the binding shape.
- **O1 (O08) — the r6 replay raises the named diagnostic** (renumbered from the
  "O2" this section first proposed; O08's version is authoritative and its
  regexes were self-checked against the measured bytes). Run the replay **in an
  isolated `git archive` copy under `.scratch`** (the renderer is permitted
  in-tree for non-freeze modes, but the isolated copy is what this seat measured
  and is the honest reproduction):
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`.
  Assert **all four**: (a) exit in `{1, 2}`; (b) a named diagnostic token matches
  `E2E-READSET` (or whichever code the landed patch chose, resolved from O01);
  (c) the unresolvable member is named verbatim —
  `reports/round-20/handoff/claims-map.md`; (d) neither `Traceback (most recent
  call last)` nor `KeyError` appears in the combined output. Conditions (b) and
  (d) are the true before/after discriminator (Trap 4); the pre-fix state
  satisfies (a) and (c) but fails (b) and (d).
- **O3 (O08) — the r7 default chain still exits 0.** `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`
  → exit 0 and the reported `packet_sha256` equals the on-disk
  `reports/round-34/handoff/declared-in-r7/packet.md`
  (`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, §8 M8).
  Match the constant names `V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT`
  (`tools/exercise-handoff-e2e.py:1933-1934`), not line numbers — they shift with
  the edit.
- **O4 (O08) — the freeze bytes do not move.** `reports/round-34/handoff/declared-in-r7/`
  is now inside the protected set. Assert `packet.md` sha256 == `45f57132…`,
  `twin.json` == `0e229138…`, and `claims-map.md` ==
  `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`
  (all three independently measured by this seat, §8 M8) — plus the `freeze.txt`
  lines agreeing. No re-freeze of declared-in-r7 is permitted this round
  (claims.json:69-70). **Correction to O08's leg:** O08's `FREEZE_FILES` list
  (`op/O08-validation-legs.md:210,289-297`) compares `git show HEAD:<path>` for
  `expected.json`, `packet.md`, `twin.json`, `freeze.txt`, `claims-map.md` in both
  the r6 and r7 dirs — correct, but note `run.log` is gitignored
  (`.gitignore:3 *.log`), so it can only be checked by before/after digest
  snapshot, never against HEAD; O08 already handles this and labels it
  `could-not-evaluate`. Do not silently green it.
- **O5 (O08) — the patch is present and renderer-only.** Live renderer sha !=
  `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9` (the
  pre-patch digest, **confirmed independently by K03** at
  `scout/K03-keyerror-path.md:8` and by O08 at `op/O08-validation-legs.md:15-17`),
  `git show HEAD:tools/exercise-handoff-e2e.py` == that digest, and the renderer
  source carries the `E2E-READSET` token. Additionally assert the diff touches the
  read-set resolution region and the selftest block only — no default-pair move,
  no `CLAIMS_MAP` re-point, no packet-affecting edit (extension this seat adds to
  O08's leg).
- **O6 (O08) — the validator itself stays inside the fences (F-C13-1 / freeze
  ban).** The validator source contains no `--freeze` argv literal and no filed
  round-runner path (`reports/round-(?:[1-9]|[12]\d|3[0-4])/run-validation\.py`;
  its own round-35 path is exempt). Any in-tree execution of a filed round runner
  is a **round-level rejection**, not a claim failure.
- **O7 (extension) — the designed digest-mismatch path is preserved.** O08's O2
  content anchors cover the two existing control lines (`m12b` exit 1
  `E2E-DIGEST`; `m12a` exit 2 `E2E-BASELINE`) remaining present. This seat adds
  the *mechanism* assertion: the hardening edits the same loop that produces the
  `E2E-DIGEST` message (`tools/exercise-handoff-e2e.py:3819-3823`), so a careless
  `.get()`-with-default would swallow the drift class and turn a real content
  mismatch into a silent pass. Assert that a genuinely drifted member still trips
  its own leg, not merely that the control *line* still prints. K03 notes the
  existing `m12b` control covers a member **present** in the live read set
  (`scout/K03-keyerror-path.md:139-142`) — which is exactly why the membership
  case and the content case must both be asserted, and why O02 should not simply
  re-add `m12b`'s leg and call the claim's second control satisfied.
- **O8 (extension) — the v1 mirror site.** K03 measured the same latent defect at
  the v1 block (`tools/exercise-handoff-e2e.py:1436-1441`: detection at `:1436-1438`,
  the mirror crash line at `:1440`, the designed raise at `:1441`), currently
  unreachable because the v1 default baseline's 21 members are a subset of
  `V1_READ_SET`. Record whether the patch fixes both sites or only v3, as a named
  decision with its reason — an unfixed mirror site is a *routed finding*, not a
  claim failure, but it must not be silently omitted. Assert also that any new
  exception subclasses `Failed` or `Unevaluatable`, because the catch tails accept
  only those two families (v1 `:1510-1515`, v3 `:3971-3975`) and anything else
  escapes as a traceback.
- **O9 (extension) — the docstring exit table stays true.** `E2E-READSET` occurs
  **0 times** at HEAD (`scout/K03-keyerror-path.md:99-103`), so the module's own
  contract text (`tools/exercise-handoff-e2e.py:88-93`) goes stale unless the
  patch extends it. Assert the docstring names `E2E-READSET` and its exit class.
  Recommended, not claim-binding — report it as a finding, not a failure.

### §6.4 Claim-A legs (per-surface verdicts + PROVINCE accuracy)

- **A1 — every touched surface has a verdict.** The census source is K04's
  fragment plus this round's claim text (claims.json:55-59). Assert the assembled
  audit document names **each** surface exactly once (set equality on surface
  ids, not a count) and that each row carries a verdict (`green` or a named
  finding with an owner). The nine declared surface classes: (1) the
  declared-in-r7 packet pair + claims-map + repin.json; (2)
  `tools/harness/receipt_guard_adoption.py` + adoption-inventory.json; (3) the
  `examples/` digest repoints + culture-d3 repoint; (4) the round-33/34 `SKILL.md`
  edits; (5) the `AGENTS.md` excision; (6) the ceilings errata; (7) the
  box-1/reissue records; (8) the contract-read-record; (9) the r34 renderer edits
  (which claim O now modifies again — the A verdict for the renderer must be
  re-taken *after* the hardening lands).
- **A2 — zero unfiled bleed.** Any cross-domain reference found on those surfaces
  must appear in the audit document as a named finding with an owner. Assert the
  count of unfiled findings is zero and report the count of *filed* findings
  (a non-zero filed-finding count is not a leg failure — routing is the correct
  disposition).
- **A3 — PROVINCE accuracy at HEAD.** Re-verify `PROVINCE.md` (31 lines, §8 M11)
  against the post-edit tree: the new tool, the r7 packet and the repointed
  renderer all fall under the owns-list's "this lane's own gates, source-check
  records, non-canon examples and reports"; the refuses-list (canon/lore,
  rights rulings, game mechanics, chusa, kake, kotoba) is unchanged. Assert the
  owns-list's corpus path set
  `{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`
  still matches the six live partition directories, and that the two
  load-bearing lines (`lore-shokunin owns the world bible`; `Contested scope →
  report to the integrator, never absorb`) are intact.
- **A4 — contested items routed, not absorbed.** Assert the audit document
  contains no canon/clearance/closure assertion and that every contested item
  names its owner. Delegates the token machinery to L1.
- **A5 — second verifier present.** A11's independent re-run of A06's PROVINCE
  checks plus two spot-checked slices must have landed; assert the fragment exists
  and that any disagreement is filed, not smoothed.
- **A6 — the audit's own commands re-run.** A07's fragment re-runs every cited
  command in A01-A06. Assert A07 exists and reports either the same result or a
  filed defect with the differing output.

### §6.5 Cross / close legs

- **P1 — preservation (global).** Reuse the round-34 `protected_snapshot`
  approach (`reports/round-34/run-validation.py:264-280`) with the round range
  widened to `1..34`: every blob under `reports/round-1..34/**`,
  `tools/gates/frozen/round-*`, and `corpus/lessons/*.md` (excluding
  `corpus/lessons/README.md`) is byte-identical to the baseline commit's tree;
  plus no new path appears under those prefixes in `git status`. **Deliberately
  excludes `corpus/knowledge/**` and `corpus/README.md`** — this round's
  deliverables (§2 note 3). Run it before and after measurement. This is where
  O6, C8 and the A-claim's "filed bytes untouched" assertions actually verify.
- **L1 — language.** Run the embedded scanner over every `reports/round-35/**`
  file; allow a hit only in a negation or routed-reference context; require every
  declared seat `out` path to be present in the scan; zero unallowed hits. Carry
  the round-34 two-pass design (`reports/round-34/run-validation.py:283-310`):
  `LANG_TOKENS` flags token presence, `LANG_ALLOW` clears negations, and only
  `LANG_FRAME` grant/completion frames are UNSUPPORTED. Evidence prose naming
  tokens (audit dossiers, "the verified surface", digests) must **not** fire. Two
  adjudications to pre-clear by path: this file and every fragment quoting audit
  tokens inside a fenced spec block, and `claims.json`/`targets.json`/the runner
  itself.
- **X1** fleet report at `../.ufo/reports/round-35/kotodama.md` with all four
  required headings, an ISO date, and a citation of
  `reports/round-35/run-validation.py`. (Round-34 precedent:
  `../.ufo/reports/round-34/kotodama.md`, 6,259 bytes, exists; the round-35
  directory does not, §8 M12.) Note the report lives **outside** this repo, so
  the integrator writes it — seats cannot.
- **X2** MANIFEST: the fleet-root `MANIFEST.json` round-35 entry present, or
  recorded `pending-by-construction` with the reason naming the integrator.
- **X3** telemetry: `dispatch-declared.json` SHA-256 recorded (`93e205a2…`); its
  `durable_sources` digests equal the live `claims.json`/`targets.json` digests
  (verified true at this seat's cut, §8 M2); the observed-dispatch record and the
  closing snapshot `availability-close-35.json` exist **or** are reported as owed
  with owner + reason. Never infer missing counters.
- **X4** self-consistency: `round == 35`, `counting_command == "python3
  reports/round-35/run-validation.py"`, `acceptance_checks_passed` true only if
  every leg passed, `limits` non-empty, `missing_dependencies` ⊇ `target_outputs`
  (every owed seat fragment listed). In-flight evidence changes invalidate
  acceptance (re-read digests before writing).

### §6.6 Leg table (machine-readable)

```json
{
  "round": 35,
  "runner": "reports/round-35/run-validation.py",
  "receipt": "reports/round-35/validation.json",
  "baseline_key": "claims.baseline_commit",
  "baseline_declared_token": "4a7aede",
  "baseline_expanded": "4a7aede22cd8395b01ce6dd9f46bcae364ca24e4",
  "legs": [
    {"id": "CO1", "claim": "cross", "check": "strict json + round==35 + baseline three-way agreement (short token, declared expansion, git-resolved)", "expect": "pass"},
    {"id": "CO2", "claim": "cross", "check": "claim axes C/O/A on distinct axes == axes_in_play", "expect": "pass"},
    {"id": "CO3", "claim": "cross", "check": "freshness_pause_in_force true and freshness absent", "expect": "pass"},
    {"id": "CO4", "claim": "cross", "check": "64 seat rows == seat_count 64; unique outs; NO r34-style 63 deviation", "expect": "pass"},
    {"id": "CO5", "claim": "cross", "check": "declared allocation opencode-go-3 / deepseek-v4.1-flash / 64 / 1 batch asserted; observed route key 1 recorded as a named deviation", "expect": "pass-with-deviation", "deviation": "declared lane opencode-go-3 vs observed route opencode-go key 1; keys 3/4/5 returned 402 with zero launched; owner orchestrator; claims.json digest pinned in dispatch-declared.json so no edit"},
    {"id": "CO6", "claim": "cross", "check": "seat role/claim counts == measured census", "expect": "pass", "measured_2026_10_19": {"claims": {"C": 24, "O": 16, "A": 15, "cross": 9}, "roles": {"scout": 4, "planner": 2, "connector": 1, "executor": 26, "verifier": 8, "scribe": 10, "reviewer": 9, "critic": 4}}},
    {"id": "CO7", "claim": "cross", "check": "coverage axis present in axes_in_play; no freshness axis-move claim", "expect": "pass"},
    {"id": "CO8", "claim": "cross", "check": "godspeed lead", "expect": "could-not-evaluate", "owner": "orchestrator", "reason": "prompts not persisted; AGENTS.md:30-31 forbids private prompt payloads"},
    {"id": "CO9", "claim": "cross", "check": "regression floor: renderer selftest exit 0; r7 chain exit 0 with packet_sha256 45f57132...", "expect": "pass"},
    {"id": "C1", "claim": "C", "command": "for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done", "expect": "21/23/24/29/20/94 (sum 211), per partition"},
    {"id": "C2", "claim": "C", "check": "linguistics 21, synthesis 29, verification 20, civilizations 94 unchanged", "expect": "pass"},
    {"id": "C3", "claim": "C", "command": "python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "expect": "totals.files == 211; every file once; line/marker totals grew from 36395/717/655"},
    {"id": "C4", "claim": "C", "check": "README equality on all four count surfaces: two section headers, totals line, counts footer, index-row parity 211==211", "expect": "pass"},
    {"id": "C5", "claim": "C", "check": "10/10 new entries audited by TWO independent auditors; set-equality coverage; disagreements filed not smoothed", "expect": "pass"},
    {"id": "C6", "claim": "C", "check": "zero fabricated sources; every non-to-verify pointer re-resolved by the leg itself; to-verify census reported", "expect": "pass"},
    {"id": "C7", "claim": "C", "check": "new entries carry no grant-frame bleed; contested items routed to lore-shokunin", "expect": "pass"},
    {"id": "C8", "claim": "C", "check": "corpus/lessons/*.md count == 33 unchanged", "expect": "pass"},
    {"id": "O1", "claim": "O", "command": "python3 -B tools/exercise-handoff-e2e.py --selftest", "expect": "exit 0; control count >= 19 (was 17)"},
    {"id": "O2", "claim": "O", "command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json (isolated copy)", "expect": "exit != 0; E2E-READSET named; unresolvable member reports/round-20/handoff/claims-map.md named; NO Traceback in stderr", "severity": "claim-centre"},
    {"id": "O3", "claim": "O", "check": "preserved paths: flipped-sha expectation still exit 2 E2E-BASELINE; content-tampered live read-set member still exit 1 E2E-DIGEST naming the file", "expect": "pass", "severity": "highest-value control"},
    {"id": "O4", "claim": "O", "command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet", "expect": "exit 0; packet_sha256 == 45f57132... == freeze.txt"},
    {"id": "O5", "claim": "O", "check": "zero in-tree execution of any filed round runner", "expect": "pass", "severity": "round-level"},
    {"id": "O6", "claim": "O", "check": "declared-in-r7 freeze bytes pinned: packet 45f57132..., twin 0e229138..., claims-map d181de28...; no re-freeze", "expect": "pass"},
    {"id": "O7", "claim": "O", "check": "renderer diff touches only the read-set resolution region + selftest block; no default-pair move; before/after sha256 reported", "expect": "pass"},
    {"id": "A1", "claim": "A", "check": "every touched surface named exactly once with a verdict (green or named finding with owner)", "expect": "pass"},
    {"id": "A2", "claim": "A", "check": "zero unfiled cross-domain bleed; filed-finding count reported", "expect": "pass"},
    {"id": "A3", "claim": "A", "check": "PROVINCE owns/refuses accurate at HEAD; six corpus paths match the six live partitions; two load-bearing lines intact", "expect": "pass"},
    {"id": "A4", "claim": "A", "check": "contested items routed-not-absorbed; no canon/clearance/closure assertion", "expect": "pass"},
    {"id": "A5", "claim": "A", "check": "A11 second verification landed; disagreements filed", "expect": "pass"},
    {"id": "A6", "claim": "A", "check": "A07 re-ran every cited command in A01-A06; same result or filed defect", "expect": "pass"},
    {"id": "P1", "claim": "cross", "check": "reports/round-1..34/**, tools/gates/frozen/round-*, corpus/lessons/*.md byte-identical to baseline; no new protected paths", "expect": "pass"},
    {"id": "L1", "claim": "cross", "check": "language scan over reports/round-35/**; every declared seat out present in the scan; zero unadjudicated grant-frame hits", "expect": "pass"},
    {"id": "X1", "claim": "cross", "check": "fleet report with 4 headings + date + runner citation", "expect": "pass"},
    {"id": "X2", "claim": "cross", "check": "MANIFEST round-35 entry present or pending-by-construction with reason", "expect": "pass"},
    {"id": "X3", "claim": "cross", "check": "telemetry digests match live; observed record + availability-close-35.json or owed with owner", "expect": "pass"},
    {"id": "X4", "claim": "cross", "check": "validation.json self-consistency + missing_dependencies covers target_outputs", "expect": "pass"}
  ]
}
```

### §6.7 Language and negation posture (binding on every leg)

No leg, fragment, receipt or report in this round asserts promotion, canon,
clearance or closure. Every occurrence of those tokens must be a negation, a
routed reference, or a quoted pattern. The three legitimate shapes, all present
in this file: `no promotion decision is taken` (§1 SHONEN draft), `canon
decisions belong to lore-shokunin` (PROVINCE.md:20), and quoted scanner patterns
(§6.5 L1). The r34 scanner's frame rule is the contract: **token presence alone
never fires; only grant/completion frames do.**

---

## §7 — Selftest control list (`--selftest`, dependency-free, synthetic inputs)

Each control is a positive/negative pair the integrator implements with
in-memory fixtures, mirroring `reports/round-34/run-validation.py:439-464` and
the round-34 control set (12 controls). Round 35 needs 24, because this round
adds three new assertion surfaces (partition arithmetic, the named diagnostic,
the README footer):

1. `claims.json` with `round: 34` → **CO1 fails**;
2. a duplicate JSON key → **strict parse refused**;
3. `baseline_commit` absent or non-resolving → **CO1 fails**;
4. a declared `baseline_expanded` that disagrees with `git rev-parse` → **CO1
   fails** (the declared expansion is a claim, not evidence);
5. `targets.json` with 63 seat rows → **CO4 fails** (64 is the measured value —
   the inverse of round 34's control 18);
6. a duplicate `out` path across seats → **CO4 fails**;
7. `axes_in_play` containing `freshness` → **CO3 fails**;
8. a fixture with the declared lane `opencode-go-2` → **CO5 fails** on the
   declared-allocation assertion;
9. a fixture declaring key 1 with no attempt records → **CO5 fails** on the
   deviation's evidence requirement (a deviation without evidence is not
   recordable);
10. a partition vector `21/23/24/29/20/94` → **C1 passes**;
11. a partition vector `21/19/24/29/20/94` (myth-symbol short) → **C1 fails**,
    naming myth-symbol;
12. a vector summing to 211 with the +10 in the wrong partitions → **C1/C2
    fail** (per-partition assertion, not total-only);
13. `totals.files == 211` with one file listed twice → **C3 fails**;
14. a README whose totals line reads 211 but whose footer still reads
    `201` / `21/19/18/29/20/94` → **C4 fails** (the r28 defect, reproduced as a
    control — this is the single most important control in the set);
15. a README whose section header still reads `## culture-material/ (18)` →
    **C4 fails**;
16. a README with 210 index rows against 211 files → **C4 fails**;
17. one new entry with no decision record → **C5 fails**;
18. a replayed r6 row that exits 1 with a `KeyError` traceback → **O1 fails**
    (the pre-fix state must not pass the leg — Trap 4);
19. a replayed r6 row that exits in `{1,2}` with `E2E-READSET` naming the member
    and no traceback/`KeyError` → **O1 passes**;
20. a flipped-sha expectation that exits 0 → **O2/O7 fail**;
21. a tampered live read-set member that exits 0 → **O2/O7 fail** (the
    swallow-the-drift regression the `.get()`-with-default would cause);
22. a protected file with one mutated byte → **P1 fails**, naming the path;
23. a round-35 fragment introducing a promotion token outside a negation →
    **L1 fails**; and `no promotion decision is taken here` → **L1 passes**;
24. a fleet report with 3 of the 4 headings → **X1 fails**.

### §7b — The NEW renderer controls (claim O, owned by the renderer)

These are controls *inside* `tools/exercise-handoff-e2e.py --profile v3 --selftest`
(note the **v3** profile — see §6.3 O2 and §9 item 6), not in `run-validation.py`,
and they are the claim's own threshold ("renderer selftest controls covering both
the superseded-row refusal and the preserved E2E-DIGEST digest-mismatch path",
`claims.json:40,45`):

- **the new control (superseded-row refusal):** a synthetic baseline whose
  `inputs` names a member absent from the live assembly's digests → the exercise
  exits with the named diagnostic (`E2E-READSET`) naming that member, and **not**
  with an unhandled exception. Fixture design: reuse the shape this seat
  reproduced — a baseline `inputs` map carrying one extra key (§8 M9). This is the
  only genuinely new *behavioural* control the claim requires.
- **the preserved digest-mismatch path:** the claim's second clause is satisfied
  by the **existing** `m12b` control line (`exit 1 E2E-DIGEST naming the changed
  file`) remaining present and green, not necessarily by a new control. K03's
  reading (`scout/K03-keyerror-path.md:139-142`): `m12b` already covers a member
  that *is* in the live read set, so O02 should not re-add it as if it were new —
  but the membership case and the content case are different classes and both must
  be asserted (§6.3 O7). The integrator may land one new control plus an explicit
  preservation assertion, or two new controls; either satisfies the claim text.

Count after the patch: the v3 suite's header goes **39 → 43** as O02 actually
landed it (`op/O02-controls.md:252,272`: four new control lines — `m13a`, `m13b`,
`m14a`, `m14b`), which satisfies O08's binding floor of **≥ 41** with margin. The
`^  - ` result lines go to **controls + 1** (43 + 1 = 44). The *default*-profile
suite is a different, smaller suite (17 controls, 18 result lines) and is not the
assertion surface. Leg O2 (O08) asserts the floor and the content anchors, and leg
O7 (extension) asserts the preserved mechanism independently, so a shrunken
renderer selftest is caught twice. Assert the **floor plus the anchors**, never an
exact count alone: if the integrator lands a fifth corroborating control, an exact
assertion would read as a failure.

---

## §8 — Measurements taken by this seat (2026-10-19, round-35 tree)

- **M1** `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`;
  `git status --porcelain -uall` → exactly six rows, all untracked:
  `reports/round-35/{claims.json,targets.json}` and
  `reports/round-35/telemetry/{availability-attempt-1,availability-attempt-2,availability-attempt-3,dispatch-declared}.json`.
  `reports/round-35/run-validation.py` and `validation.json` do not exist.
- **M2** `sha256sum reports/round-35/claims.json reports/round-35/targets.json
  reports/round-35/telemetry/dispatch-declared.json` →
  `ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4`,
  `56ad03927c7063a3616af2ed0e78ab7b1ca1f3ea43fdf67f2ecf60a7f1b63215`,
  `93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83`. The first
  two equal the digests declared in `dispatch-declared.json:20-24` — **verified
  live**.
- **M3** seat census from `targets.json` (JSON parse) → `seat_count` field 64,
  **64 rows**, 64 unique `out` paths, 0 duplicates, 0 landed at this cut; claims
  {C 24, O 16, A 15, cross 9}; roles {scout 4, planner 2, connector 1, executor
  26, verifier 8, scribe 10, reviewer 9, critic 4}. Ids: K01-K04, P01-P02, X00,
  C01-C17, O01-O11, A01-A11, R01-R09, X01-X04, S01-S05.
- **M4a** `claims.json:8` `baseline_commit` = `"4a7aede"` (7 hex, not 40-hex);
  **M4b** `claims.json:9` `baseline_expanded` and `dispatch-declared.json:17`
  both carry `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`, which equals
  `git rev-parse HEAD` — three-way agreement confirmed.
- **M5** partition census
  `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
  → `21 / 19 / 18 / 29 / 20 / 94` = **201**; `ls corpus/lessons/*.md | wc -l` →
  **33**.
- **M6** `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → `schema kotodama-source-audit-inventory/1`, `read_only true`,
  `deterministic true`, `totals.files 201`, `files_with_marker 135`, `lines
  36395`, `raw_lines 717`, `raw_occurrences 731`, `marker_occurrences 655`,
  `class_totals {substantive-flag-candidate 563, policy-use-mention 37,
  needs-review 133}`, `skipped []`.
- **M7** README census by python over `corpus/README.md`: index rows **201**,
  live files **201**, rows-not-files `[]`, files-not-rows `[]` — parity holds
  today. Structure: `## linguistics/ (21)` at `:123`, `## myth-symbol/ (19)` at
  `:147`, `## culture-material/ (18)` at `:169`, `## synthesis/ (29)` at `:190`,
  `## verification/ (20)` at `:222`, `## civilizations/ (94)` at `:245`,
  `## Known gaps (frontier)` at `:342`; counts footer at `:471-473` reading
  `(total 201 files; directory totals 21/19/18/29/20/94)`; revision 1.9 at `:3`.
- **M8** `python3 -B tools/exercise-handoff-e2e.py --selftest` (default profile)
  → **exit 0**, positive run `fields=16/16 glossary-entries=20 findings=0` plus
  **17 controls** (18 `^  - ` result lines). **This is not the claim-relevant
  suite.** `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` →
  **exit 0**, header `selftest: OK — positive run (exit 0, fields=16/16,
  glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4,
  v2_subset=equal, alias_leg=landed) plus 39 controls:` with **40** `^  - `
  result lines — independently confirmed by K03 (`scout/K03-keyerror-path.md:129-136`)
  and O08 (`op/O08-validation-legs.md:32`), including their finding that the
  header's `39` and the printed `40` bullets differ by the witnesses line
  (`tools/exercise-handoff-e2e.py:4169`, printed at `:4466-4467` while the header
  prints `len(results) - 1` at `:4464`). **The v3 suite is the assertion surface;
  assert the bullet count, not the header label** (O08's leg does both).
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → **exit 0**,
  `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
  `declared-in-r7/freeze.txt` → `packet_sha256 45f57132…`, `twin_sha256
  0e229138…`, read set 58 files, `claims: 27 statuses 16/7/4`.
  `sha256sum declared-in-r7/claims-map.md` →
  `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c`, which
  equals the `re-frozen input` line in `freeze.txt`. The pre-patch renderer
  digest is `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`
  (K03 `:8`, O08 `:15-17`). `V3_BASELINE_DEFAULT`
  (`:1933`) and `V3_FROZEN_DIR_DEFAULT` (`:1934`) name
  `reports/round-34/handoff/declared-in-r7`; `CLAIMS_MAP` (`:184`) names the
  r7 successor map.
- **M9 — R34-N1 reproduced independently in an isolated copy.**
  `git archive HEAD | tar -x -C .scratch/s04-iso` then
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
  → **exit 1 via an uncaught exception**:
  ```
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
  KeyError: 'reports/round-20/handoff/claims-map.md'
  ```
  The mechanism is precise: line 3820 computes the drift list with
  `assembly.digests.get(rel) != digest` (safe), then the *diagnostic* loop at
  `:3822` indexes `assembly.digests[rel]` directly (unsafe). So the fix is a
  one-site catch at `:3822`, and the surrounding `Failed("E2E-DIGEST", …)` at
  `:3823` is the designed leg that is unreachable for this class. Exit-code
  constants: `EXIT_PASS 0` (`:112`), `EXIT_FAIL 1` (`:113`),
  `EXIT_UNEVALUATED 2` (`:114`). Error classes: `Unevaluatable` (`:244`, code
  `E2E-DATA`), `ArtifactError` (`:250`, `E2E-ARTIFACT`), `MissingArtifact`
  (`:254`), `BaselineError` (`:258`, `E2E-BASELINE`), `Failed` (`:262`, takes
  `(code, message)`). The module docstring (`:88-93`) enumerates the design: six
  failed codes (`E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC`,
  `E2E-LINK`) and three could-not-evaluate codes (`E2E-ARTIFACT`,
  `E2E-BASELINE`, `E2E-DATA`). **An unresolvable read-set member is an
  unevaluatable input by that taxonomy, which argues for exit 2 — see §9 item 4.**
- **M10** `git status --porcelain -uall -- reports/round-1..34 corpus/lessons tools/gates/frozen`
  → **0 rows**; `git diff --stat` over the same prefixes is empty. All six new
  files live under `reports/round-35/`. This is the round's P1 pre-state.
- **M11** `PROVINCE.md` → 31 lines; owns-list names
  `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`;
  refuses-list names canon/lore, rights rulings, game mechanics (game-dev-2d/3d),
  general source-research method (chousa), web publishing (kake), prompt/skill
  craft (kotoba); the adjacent contract and the "contested scope → report to the
  integrator, never absorb" line are at `:23-26`.
- **M12** `ls ../.ufo/reports/round-34/` → `kotodama.md` (6,259 bytes);
  `../.ufo/reports/round-35/` → **absent**. The lane repo's own `.ufo/reports/`
  is empty — the fleet report belongs at the fleet root.
- **M13** the claims.json "matches A11's reading" reference resolves to **round
  33's** A11 seat, `reports/round-33/adj/A11-verify-a01-a03.md:35`, which
  measured exactly `21/19/18/29/20/94`. Round 34 had no A-block (its seats are
  K/P/X/D/O/C/R/X/S); round 35's own A11 is a different, unrun seat
  (`adj/A11-verify-2.md`). The integrator must cite the round-33 path.

Honest limits: every after-value in §3 is a requirement from `claims.json`, not
an observation — no seat fragment existed at this seat's cut. §6 is a design the
integrator implements and self-tests; this seat executed no part of
`run-validation.py` and executed **no** filed round runner (the only renderer run
was in an isolated `git archive` copy, §8 M9, plus two in-tree non-freeze runs
authorized by the round boundaries, §8 M8). §9's defects are measurements about
the *declaration*, and this seat changed no declared byte.

---

## §9 — Declaration defects and errata for the integrator

1. **The round-34 seat-count deviation does NOT repeat — and copying its
   assertion would fail a well-formed round.** `targets.json:3` declares
   `seat_count: 64`; the array has 64 rows (§8 M3); `dispatch-declared.json:28`
   records that targets.json was first authored with 60 seats and corrected to 64
   before dispatch. Round 34's validator hard-codes `len(seats) == 63`
   (`reports/round-34/run-validation.py:122`). Round 35's `CO4` must assert 64
   with no deviation block (Trap 2). If the round records a 63-vs-64 deviation,
   that is a fabricated carry-over.
2. **The provider lane is a declared-vs-observed divergence, not a failure.**
   `claims.json:11` and `dispatch-declared.json:8` declare `opencode-go-3`; keys
   3, 4 and 5 each returned `402 Upstream request failed: Insufficient account
   funds` with **0 launched, 64 failed** and zero seats started
   (`availability-attempt-{1,2,3}.json`); the batch ran on **key 1**. attempt-3's
   `disposition` names this as a recorded deviation under REGIMEN.md's
   "provider deviations are permitted only as declared" and the round-10
   precedent. Two consequences the integrator must honour: (a) the closing
   snapshot's `closed_fields` must fill the observed route as key 1 citing
   attempt-3; (b) any report sentence that says "64 seats on opencode-go-3" is
   wrong — the allocation was key 3, the *route* was key 1. The 192 failed
   launches across the three attempts (64 × 3) must not be netted against the 64
   completed seats.
3. **The declaration's prose `seat_composition` string does not equal the
   measured census.** `dispatch-declared.json:13` reads "4 scouts, 2 planners, 1
   connector, 17 C-seats …, 11 O-seats, 11 A-seats, 9 reviewers, 4 critics, 5
   scribes" — it totals 64 but its per-group numbers do not match the measured
   claim census {C 24, O 16, A 15, cross 9} or role census {executor 26,
   verifier 8, scribe 10, …} (§8 M3). Its own text concedes this ("role/claim
   census measured by the round-35 validator"). Assert on the measured census and
   treat the prose as declaration colour. Do not "reconcile" it — the file is
   digest-pinned.
4. **The r6 replay's "expect: exit 1" is not a discriminator, and the renderer's
   own taxonomy argues for exit 2.** `claims.json:48` parenthesises
   `(expect: exit 1, named diagnostic)`. Measured: the replay already exits 1
   today via an uncaught `KeyError` traceback (§8 M9), so an exit-1 assertion
   passes before and after the hardening. The claim's *threshold* ("named
   diagnostic at the r6 replay") and its `after_required` ("exits non-zero") do
   not pin the code, so the parenthetical is errata. Recommendation: raise the
   new diagnostic as an `Unevaluatable` subclass carrying code `E2E-READSET`
   (exit **2**), which matches the module's own taxonomy — an unresolvable
   read-set member is "input cannot be evaluated", exactly the class
   `E2E-ARTIFACT`/`E2E-BASELINE`/`E2E-DATA` occupy (`:88-93`) — and file the
   exit-1 parenthetical as errata. The alternative (raise `Failed("E2E-READSET",
   …)` → exit 1) honours the parenthetical but asserts "the exercise ran and its
   verdict is negative" for a run that never executed. Either way, leg O1 (O08)
   must assert the diagnostic token and the absence of a traceback, not the exit
   code (Trap 4).
5. **The L1 language scanner does not cover `corpus/knowledge/**`.** The r34
   scanner walks `ROUND` (`reports/round-34/run-validation.py:297`). Ten new
   corpus entries containing canon-boundary prose therefore sit **outside** L1's
   reach, and the audit fragments that quote them sit inside it. The integrator
   must either extend the walk to the ten new entry paths (preferred — the claim
   requires "no bleed" on the new entries) or add the C7 leg scoped to the drafts,
   and must state which in the receipt's `limits`. A green L1 that never read the
   new entries is a false assurance.
6. **Claim O's counting command and its threshold point at different selftest
   suites.** `claims.json:47` declares `python3 -B tools/exercise-handoff-e2e.py
   --selftest` — no `--profile`, which runs the **default** suite (17 controls, 18
   result lines, §8 M8). The threshold at `claims.json:51` ("selftest N/N") and the
   `after_required` at `:45` require a control over the **v3** replay's
   superseded-row refusal, which lands in the **v3** suite (39 controls, 40 result
   lines). So the declared command cannot observe the declared control. Errata:
   the acceptance surface is `--profile v3 --selftest`; the O08 leg
   (`op/O08-validation-legs.md:70-88`) already uses the right invocation, and the
   receipt should record the default-suite count separately or not at all — never
   as the N in "selftest N/N". Do not edit `claims.json` (digest-pinned, §8 M2).

---

## §10 — Owed

All 64 declared seat fragments — in particular `scout/K01-K04`,
`plan/P01-P02`, `cross/X00`, `cov/C01-C17`, `op/O01-O11`, `adj/A01-A11`,
`review/R01-R09`, `cross/X01-X04`, `scribe/S01-S03`, `scribe/S05`. Snapshot at
this seat's first cut: **0 of 64 landed**; §11 supersedes that with the
landed-fragment cross-check at its read (recompute with §10.1; do not trust
either list). Beyond the seat fragments:

- the ten new corpus entries at
  `corpus/knowledge/culture-material/*.md` (×6) and
  `corpus/knowledge/myth-symbol/*.md` (×4) (claim C's deliverable);
- the `corpus/README.md` reconciliation — two section headers, the totals line,
  the counts footer, ten index rows, and a new revision note (drafted by C11,
  applied by the integrator);
- the `tools/exercise-handoff-e2e.py` hardening (claim O) — drafted by O01,
  applied by the integrator, never edited by a seat;
- `reports/round-35/run-validation.py` and `reports/round-35/validation.json`
  (integrator-authored; this seat executed no part of either);
- `reports/round-35/telemetry/observed-dispatch.json` and the closing snapshot
  `reports/round-35/telemetry/availability-close-35.json` (§4);
- `../.ufo/reports/round-35/kotodama.md` (the four-section report this draft
  supplies), the fleet-root `MANIFEST.json` round-35 entry, `SCORECARD.md`, and
  the append-only `LOG.md` entry — integrator-only writes.

### §10.1 — Recompute commands (do not trust the snapshot list)

```bash
python3 -c "import json,os;t=json.load(open('reports/round-35/targets.json'));print([s['out'] for s in t['seats'] if not os.path.isfile('reports/round-35/'+s['out'])])"
find reports/round-35 -type f | wc -l
git status --porcelain=v1 -uall -- reports corpus/lessons tools/gates/frozen | wc -l
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
```

---

## §11 — Landed-fragment cross-check (addendum, 2026-10-19, same wave)

Read by this seat after §1-§10 were written. The wave is still dispatching, so
every list here is a point-in-time snapshot with its command (§10.1).

**Dependency supersession.** At this seat's first cut `reports/round-35/` held
only `claims.json`, `targets.json` and four telemetry files; §1-§10 were written
against that empty state. At this addendum's read **51 of the 64 declared seat
outputs have landed** — the wave is still dispatching, so recompute rather than
trusting any list. The fragments this dossier's legs depend on have **all**
landed: `scout/K03` (the KeyError scout), `op/{O01,O02,O08}` (the patch, the
controls, the O-group leg spec), `cov/C11` (the README delta), `adj/A11`
(second adjacency verifier), `cross/X00` (the connector). §11.1-§11.9 record what
each changed in this draft. Still absent at this read: `plan/P01`,
`cov/{C04,C09,C13}`, `op/{O05,O07,O09,O11}`, `adj/{A03,A04,A08}`,
`review/{R01,R05}` — 13 paths. Leg C1's partition count and leg C5's two-auditor
parity cannot go green until the four remaining C authors and the C13 auditor
land, so the receipt's `missing_dependencies` must list them.

**§11.1 — Claim O: two independent seats reproduce this seat's defect finding
exactly.** K03 (`scout/K03-keyerror-path.md:19-31,42-59`) and O08
(`op/O08-validation-legs.md:30`) both measured the same traceback, the same
defect line `tools/exercise-handoff-e2e.py:3822`, the same `KeyError` member, and
the same conclusion this seat reached independently (§8 M9): the exit code alone
does not discriminate the fix. K03 sharpens it with detail this seat's census
lacked and the leg spec now adopts:

- `V3Assembly.__init__` builds `self.digests` over the live `V3_READ_SET` only
  (`:3479-3484`), which is *why* the lookup misses — not a digest change;
- the condition is **membership, not content drift**: the superseded member's
  bytes are unchanged (`reports/round-20/handoff/claims-map.md` still hashes
  `4b1b9a35…`, 24888 bytes), and the read-set difference is exactly one member
  each way (baseline-only r20 map; live-only r34 successor `d181de28…`);
- therefore the existing `E2E-DIGEST` message text ("read-set file(s) changed
  since the baseline was frozen") is a **false statement** for this row — a patch
  that swaps the index for `.get()` and reuses that text emits a misleading
  diagnostic;
- the same latent defect exists at the **v1 mirror** (`:1436-1441`), currently
  unreachable; and any new exception must subclass `Failed` or `Unevaluatable`
  because the catch tails accept only those families (v1 `:1510-1515`, v3
  `:3971-3975`);
- `E2E-READSET` occurs **0 times** at HEAD, so the patch must extend the module's
  own exit-code table (`:88-93`) or the tool's contract text goes stale.

**§11.2 — Leg-spec ownership resolved.** O08 ships a paste-ready, content-addressed
claim-O implementation (`op/O08-validation-legs.md:202-332`) with ids O1-O6, and
self-checked its regexes against the measured bytes (`:356-373`). §6.3 now adopts
O08's ids as authoritative and keeps only non-overlapping extensions as O7-O9. No
contradiction was found between O08's leg set and this seat's: O08's O4 already
handles the gitignored `run.log` honestly (`could-not-evaluate`, not a silent
green), and its O6 fence leg matches this seat's F-C13-1 posture.

**§11.3 — The selftest count in §6.3/§7b/§8 M8 was corrected from this seat's own
first measurement.** This seat's initial `--selftest` run omitted `--profile v3`
and measured the **default** suite (17 controls / 18 lines). K03 (`:129-136`) and
O08 (`:32`) independently measured the **v3** suite at **39 controls / 40 result
lines**, which is the claim-relevant surface. The corrected numbers are in place
throughout; §9 item 6 records the underlying declaration defect (claim O's
counting command omits `--profile v3` while its threshold requires a v3 control).

**§11.4 — Claim C: C11's README delta is the reconciliation artifact to audit.**
`cov/C11-readme-delta.md` has landed; §11.9 records its five edit surfaces, the
totals-line anchor `:469`, and the existing sweep instrument leg C4 should invoke.
The r28 defect (`corpus/README.md:19-33`) is precisely the "totals line updated,
footer not" case, and C4 asserts against the footer explicitly.

**§11.5 — Claim A: A11 landed and is *not* the seat claims.json cites.** Round
35's own `adj/A11-verify-2.md` (second adjacency verifier) has landed. The
"A11's reading" reference in `claims.json:26` resolves to **round 33's** A11
(`reports/round-33/adj/A11-verify-a01-a03.md:35`), which measured exactly
`21/19/18/29/20/94` — the same vector this seat measured (§8 M5, M13). The two
are different seats; citing the round-35 path for that claim would be wrong.

**§11.6 — Preservation re-check (leg P1, point-in-time).** At this addendum's
read `git status --porcelain -uall -- reports/round-1..34 corpus/lessons
corpus/knowledge tools/gates/frozen` returns **0 rows**: all 19 new files live
under `reports/round-35/` and nothing filed moved. This is the round's P1
pre-state, measured before the integrator's close-time writes.

**§11.7 — Claim O: O01's patch lands `E2E-READSET` at exit 1, and the leg must
accept it.** O01 (`op/O01-patch-draft.md:31-37,97-120,149-152`) chose the
`Failed`-family refusal — `raise Failed("E2E-READSET", …)` → **exit 1** — with
three reasons: the filed `repin.json` records the r6 control at `"exit": 1` and is
never editable; the sibling drift leg is exit 1 `E2E-DIGEST`, so both read-set
conditions stay in one class; and exit 2 is documented for *missing/unreadable*
artifacts or *absent/edited* baselines, neither of which holds (the file exists and
the baseline is integrity-valid). It also honours claim O's own counting command
(`expect: exit 1`). **This supersedes §9 item 4's exit-2 recommendation** — O01
owns the patch and its reasoning is sound; §9 item 4 stands only as the record of
the alternative considered. The leg keeps the accept-`{1,2}` posture and asserts
the diagnostic token plus the absence of a traceback, so either family passes.
O01 also fixes the **v1 mirror site** (`:1440`/`:1441`), closing this seat's O8
extension, and its observed post-patch output is
`handoff-v3: E2E-READSET: 1 read-set member(s) named by the frozen baseline are
not in the live read set: reports/round-20/handoff/claims-map.md — the baseline
row is superseded (re-point or re-freeze it)` with a `FAIL read-set-roster:`
record line carrying the frozen digest (`op/O01-patch-draft.md:150`). Note the
patch adds a `read-set-roster` check, so the diagnostic line and the record line
are two lines; O08's single-line regex (code + member path on one line) is
satisfied by the `handoff-v3: E2E-READSET: … reports/round-20/handoff/claims-map.md`
line.

**§11.8 — Claim O: O02 lands four new controls (39 → 43).**
`op/O02-controls.md:114-169` designs and observes: `m13a` synthetic superseded row
(exit 1 `E2E-READSET` naming the member), `m13b` filed r6-row replay against the
live tree (same), `m14a` flipped read-set sha, `m14b` content-tampered live member
(the two preserved-path controls — this seat's O7 extension). Its own counts:
"39 controls before the patch; +4 leg lines" and "control count 39 → 43"
(`:252,272`), against an isolated patched copy. `m13a`/`m13b` are unpatched-KeyError
under the pre-patch bytes (`:175-176`), which is the before/after discriminator
made executable inside the suite. Leg O2's `>= 41` floor is therefore satisfied
with margin; assert the floor and the anchors, never 43 alone.

**§11.9 — Claim C: C11 names five README surfaces and an existing instrument.**
`cov/C11-readme-delta.md` lands the delta this seat's C4 leg audits: a new
**revision block** inserted between `corpus/README.md:2` and `:3` (E1, becoming
revision 2.0), the **myth-symbol header** at `:147` → `(23)` (E2), the
**culture-material header** at `:169` → `(24)` (E3), the **totals line** at `:469`
→ `Total knowledge entries: 211.` (E4 — this seat independently confirmed the
`:469` anchor and the current `201`), and the **counts footer** at `:471-473` →
`(total 211 files; directory totals 21/23/24/29/20/94)` (E5). **This is five edit
surfaces, not four** — §6.2 C4's "four count surfaces" should be read as the four
*count-bearing* ones (two headers, totals line, footer) plus the revision block.
C11 also names the **existing instrument** the C4 leg should invoke instead of
reimplementing: `python3 -B reports/round-28/readme/sweep.py`, which this seat ran
at HEAD → exit 0, `rows 201 files 201`, `missing_from_index 0`, `topic_mismatch 0`,
`orphan_rows 0`, `header_drift {}`, `totals_ok True`, `footer_ok True`, README
sha256 `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`. That
sweep already carries the r28 footer leg and its two planted controls, so it is
the correct assertion surface for C4's footer clause — prefer it over a bespoke
check, and record its `readme_sha256` before and after the reconciliation.

**§11.10 — Claim A: K04's census landed and it is the authoritative A-leg
population.** `scout/K04-touched-census.md` (234 lines) has landed and it is much
richer than this dossier's prose surface list. Measured population:
**13 live/shared surfaces** outside `reports/round-33|34/` — r33 authored 11, r34
authored 4 (`scout/K04-touched-census.md:17-19`) — each row carrying a path, an
author, a line delta, its `PROVINCE.md` anchor, a risk class (R1-R5) and HEAD
evidence: `SKILL.md`, `AGENTS.md`, `REGIMEN.md`, `SCORECARD.md`, `LOG.md`,
`corpus/lessons/README.md`,
`corpus/knowledge/linguistics/register-lexicon-ceilings.md`,
`examples/culture-d3/{README.md,handoff.md}`, `examples/handoff-packet.sample.{md,yml}`,
`tools/exercise-handoff-e2e.py`, `tools/harness/receipt_guard_adoption.py`
(`:37-51`), plus the durable in-round artifacts in its §2 (`:68-81`).

**Leg A1 must assert against K04's census, not this dossier's nine prose
classes** — §6.4 A1's list was written before K04 landed and is a coarser
partition. Two K04 findings the A legs must carry by id: **K04-F1**
(`SCORECARD.md:616`, `LOG.md:3635`) and **K04-F2** (the r34 `run.log` is
**untracked**, `.gitignore:3`, so it can only be digest-snapshotted, never
HEAD-compared — the same constraint O08's O4 already handles). K04 also flags
`corpus/lessons/README.md` as an R1/R2/R5 surface whose `corpus/lessons` path is
**not enumerated** in PROVINCE's owns-list (`:44`) — that is a genuine adjacency
question for A3/A6 to adjudicate, not a defect this seat may rule on.

## Citations

- `REGIMEN.md:13,25-29,34-36,52-58` — schedule position 3 of 3, per-round
  contract, done-when.
- `reports/round-35/claims.json:4-19,20-65,67-73` — position/dispatch, the three
  claims and their before/after + counting commands, non-goals (baseline tokens at
  `:8-9`; the r6 replay command at `:48`; the freeze-pin non-goal at `:69-70`).
- `reports/round-35/targets.json:3-13,14-463` — `seat_count` 64 (`:3`),
  shared_rules (`:5-13`), 64 seat rows.
- `reports/round-35/telemetry/dispatch-declared.json:4,6-17,18-27,28-30` —
  declaration, allocation/composition prose, durable-source digests, authoring
  note, `open-at-seat-close`.
- `reports/round-35/telemetry/availability-attempt-{1,2,3}.json` — the three 402
  refusals, their launch/failure counts, seat-id ranges, and attempt-3's
  `key_census_so_far` + key-1 disposition.
- `reports/round-34/run-validation.py:47-56,122,264-280,283-310,319,439-464` —
  `strict_json`, the r34 63-row assertion this round must NOT copy, the
  preservation walk, the language scanner, the four SECTIONS strings, the selftest
  style; `reports/round-34/validation.json` — the receipt key set.
- `reports/round-33/run-validation.py:733-784,868-930` — `protected_snapshot` and
  `check_language` precedents; `reports/round-33/telemetry/availability-close-33.json` —
  the closing-snapshot schema and `closed_fields` precedent;
  `reports/round-33/adj/A11-verify-a01-a03.md:35` — the partition vector claims.json
  cites as "A11's reading".
- `tools/exercise-handoff-e2e.py:88-93,112-114,184,244-262,1762-1763,1933-1934,3479-3484,3819-3823,4169,4464-4467`
  — the code taxonomy, exit constants, `CLAIMS_MAP`, the error classes, the
  existing tamper-read-set control, the two defaults, `V3Assembly`'s live-read-set
  digest map, the R34-N1 site, and the selftest header/bullet count mismatch.
- `reports/round-34/handoff/declared-in-r7/{freeze.txt;claims-map.md;run.log}` —
  `packet_sha256 45f57132…`, `twin_sha256 0e229138…`, read set 58 files,
  claims 27 (16/7/4), the claims-map digest `d181de28…`; `repin.json` — R34-N1's
  filed record (`named_findings[0]`, `rows[1].control.mechanism`).
- §11 landed-fragment reads: `reports/round-35/scout/K03-keyerror-path.md:8,19-31,42-59,99-103,129-136,139-142`
  (pre-patch renderer digest, the traceback, the resolving code sites, the
  membership-not-drift analysis, the `E2E-READSET` zero census, the selftest
  counts, and the `m12b` coverage note);
  `reports/round-35/scout/K04-touched-census.md:10-19,32-51,68-81` (the 13
  live/shared surfaces with risk classes and PROVINCE anchors, the durable
  in-round artifacts, and the K04-F1/K04-F2 findings);
  `reports/round-35/op/O08-validation-legs.md:15-17,30,32,70-88,202-332,356-373`
  (the pre-patch sha, the replay measurement, the v3 selftest counts, the binding
  O1-O6 legs, the paste-ready implementation, the self-check);
  `reports/round-35/cov/C11-readme-delta.md:35,48,62-126,141-142,199-213` (the
  sweep instrument's current reading, the revision block, the five edit surfaces
  E1-E5, the reconciliation note, and the machine-delta description);
  `reports/round-35/op/O01-patch-draft.md:31-37,69-120,149-152,244-248` (the
  exit-1 decision and its three reasons, the docstring extension, the patch hunks,
  the observed post-patch outputs, the v1 mirror fix);
  `reports/round-35/op/O02-controls.md:114-169,175-176,252,272` (the four control
  designs, their observed lines, the unpatched-KeyError before-state, the 39 → 43
  count); `reports/round-35/adj/A11-verify-2.md`
  (landed; a different seat from the round-33 A11 this file cites).
- `reports/round-30/handoff/declared-in-r6/expected.json` — the superseded
  baseline whose read set names `reports/round-20/handoff/claims-map.md`.
- `corpus/README.md:3,9,19-33,123,147,169,190,222,245,342,469,471-473` — revision
  1.9, the r28 footer-defect record, the six section headers, the totals line
  (`:469`), the counts footer.
- `PROVINCE.md:1-31` — owns/refuses/adjacent-contract lines.
- `SHONEN.md:3-11` — the four boxes and the mark rules;
  `reports/round-32/dossier-d11-shonen-boxes.md:44-52,143-152,200-210` — the box
  conditions quoted in the SHONEN draft.
- `AGENTS.md:15-39` — telemetry rules and close-what-you-open;
  `../.ufo/reports/round-34/kotodama.md` (exists, 6,259 bytes, and records R34-N1
  as routed at `:29-30`); `../.ufo/reports/round-35/` (absent) — §8 M12.
- `LOG.md:3616-3643` — the round-34 admission entry (r34 receipt digest
  `ba2fa4dc…`, the `availability-close-34.json` close, the 61-of-63 seat note).
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): §8 M1-M13 as listed there, plus
  `git archive HEAD | tar -x -C .scratch/s04-iso` and the isolated r6-row replay
  (§8 M9), the in-tree `--selftest` and `--profile v3 --quiet` runs (§8 M8), the
  python census over `targets.json`, the python row/file parity check over
  `corpus/README.md`, and `grep -n "^## " corpus/README.md`.
