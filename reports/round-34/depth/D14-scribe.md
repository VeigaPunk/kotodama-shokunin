- Seat: D14 | scribe | D | date 2026-10-19 | baseline da68a6d

# D14 — fleet-report D-block material: Work performed + Landed changes, paths, commit-ready list

Mission (`reports/round-34/targets.json:36`): supply the *Work performed* and
*Landed changes* material for the fleet report's D sections, with paths and a
commit-ready list. The fleet report's heading contract is fixed — `Work
performed`, `Landed changes`, `Before → after measurements`, `SHONEN`
(`reports/round-32/run-validation.py:50-55`); this fragment drafts the first two
for the **D block only** (the O/C blocks belong to S02/S03, the cross material
to S04). Prior-report register consulted: `../.ufo/reports/round-33/kotodama.md`
and `../.ufo/reports/round-32/kotodama.md`.

**Non-author declaration:** this seat authored no lane artifact before this
round and moved no lane byte. No promotion, canon, clearance or closure verdict
is claimed anywhere below.

**Method:** every measurement in §4 is this seat's own read at `da68a6d`,
citable to a `file:line` or a command in §7. Everything keyed to a sibling
fragment is a `{{owed…}}` fill naming the path it comes from.

---

## §0 Dependency state at this seat's cut (2026-10-19, wave in flight)

`reports/round-34/` carries exactly three files —
`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`
(`find reports/round-34 -type f`). **All 63 seat fragments are unwritten**,
including every D dependency (D01–D13, D15–D20), the scouts (K01/K02), the
planner (P01), the three D reviewers (R01–R03), the connector (X00) and the D
receipt scribe (S01). The `declared-in-r7` directory does not exist yet.

Consequence: §1/§2 are the report-register drafts with owed fills; §3/§4 are
complete as delivered, because the paths and numbers they carry come from
binding files (`claims.json`, `targets.json`) and from this seat's own reads of
the live tree, not from sibling prose.

---

## §1 Work performed — D block (report-ready draft)

```text
- **Depth (claim D):** the handoff packet's next revision, built from live
  bytes, closing the round-33 finding A02-H1 (named there as "shape-green and
  semantically stale": `reports/round-33/adj/A02-handoff.md:92-94`).
  `reports/round-34/handoff/declared-in-r7/` lands as a five-file revision
  (packet.md + twin.json + expected.json + freeze.txt + run.log, mirroring the
  filed `reports/round-30/handoff/declared-in-r6/` set) whose every
  number-bearing D4 cell equals a measured live value: typed labels 82
  (64 native-form / 12 translated-label / 6 borrowed-strata), findings 12 (12
  hold-or-fail, 0 fails), holds 12 / notes 0 / fails 0, conflicts 0,
  unresolved rank items 0, quarantine handles 0, reconciliation records 6,
  era-alias rows 4 ({{D03/D05 row table}}; live sources at
  `examples/culture-d4/typed-labels.d4.yml:29-47`,
  `examples/culture-d4/expected-holds.json` `counts`). The r6 revision's D4
  cells read 74 / 56 / 16 / 15, holds 15+1 note, conflicts 4, quarantine 3 and
  13 rank items (`packet.md:148-152,:307`) — stale against *the very bytes the
  packet pins* (`expected.json:158,:161` carry the live digests), while its own
  manifest rows `packet.md:68-69` already read live: the packet contradicted
  itself. Seat chain: scouts K01/K02 (packet state + re-pin census), planner
  P01, executors D01–D16 (layout; render; claim-ledger rows; OQ/glossary;
  draft assembly; twin + expected.json; gate; links + uncertainty; freeze
  design; re-pin drafts; preservation proof; receipt; negative controls; two
  gap-fills), verifiers D17–D20, reviewers R01–R03, connector X00, receipt
  scribe S01. {{per-seat outcome pointers — e.g. D07 gate verdict, D08
  links/uncertainty legs, D13 negative controls, D17–D20 re-runs}}
- **The re-pin cascade (claim D, second leg):** the renderer defaults at
  `tools/exercise-handoff-e2e.py:1933-1934` move `declared-in-r6` →
  `declared-in-r7` as the single integrator-applied edit; every other surface
  that pins the r6 pair is recorded as a **new supersession row** in `LOG.md`
  under the filed convention ("Supersession records (new rows; no filed byte
  rewritten)", `LOG.md` tail, round-33 rows), never as an in-place edit.
  Drafted before/after blocks: {{D10}}; draft verification: {{D19}}; census:
  {{K02}}. Filed revisions r2/r4/r5/r6 keep their bytes (§4), and no filed
  round runner is executed in-tree (F-C13-1 prevention, `LOG.md` F-C13-1
  entry; `AGENTS.md` §Availability and dispatch telemetry).
```

Owes: the seat outcome pointers (K01/K02/P01/D01–D13, D15–D20/R01–R03/X00/S01)
and the D10/D19 before/after verification strings.

---

## §2 Landed changes — D block (report-ready draft + path inventory)

```text
- `reports/round-34/handoff/declared-in-r7/` — **new filed revision** (claim D's
  deliverable): `packet.md` {{sha256}}, `twin.json` {{sha256}},
  `expected.json` (packet_sha256 + links/uncertainty expectations),
  `freeze.txt` (packet/twin digests + gate verdict line) and `run.log`
  ({{D06/D09/D12}}). Mirrors the r6 five-file set
  `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json,freeze.txt,run.log}`
  (`find reports/round-30/handoff -type f`).
- `tools/exercise-handoff-e2e.py:1933-1934` — **integrator-applied**, 2 lines:
  before (live bytes today)
      V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"
      V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"
  after — `declared-in-r7` paths per {{D10 before/after block}}.
- `LOG.md` — new rows (append-only) recording the r6 → r7 default move and each
  re-pointed surface as supersession, in the filed new-row shape
  (`LOG.md` "Supersession records" section, dated 2026-10-19). {{K02/D10 row
  list}}.
- `SCORECARD.md` — depth-axis row for round 34 (regimen contract,
  `REGIMEN.md:43-50`). {{integrator}}
- Fleet surfaces (outside this repo's write scope; integrator/parent files
  them): `../MANIFEST.json` `rounds[]` entry for round 34 (shape of the r33
  entry: round/date/type/closed_at/lanes/lane_rounds/promotions/minted/admitted/
  verdicts/notes) and the fleet report
  `../.ufo/reports/round-34/kotodama.md`.
```

### Path inventory (what the round adds or touches)

| # | Path | Kind | Owner | State at my cut |
|---|---|---|---|---|
| 1 | `reports/round-34/handoff/declared-in-r7/packet.md` | new filed revision | D02/D05 → integrator | absent |
| 2 | `reports/round-34/handoff/declared-in-r7/twin.json` | new | D06 → integrator | absent |
| 3 | `reports/round-34/handoff/declared-in-r7/expected.json` | new | D06 → integrator | absent |
| 4 | `reports/round-34/handoff/declared-in-r7/freeze.txt` | new | D09 → integrator | absent |
| 5 | `reports/round-34/handoff/declared-in-r7/run.log` | new | D12 → integrator | absent |
| 6 | `tools/exercise-handoff-e2e.py:1933-1934` | edit (drafted, integrator-applied) | D10 → integrator | live r6 pins (quoted §3, verbatim) |
| 7 | `LOG.md` | append rows | integrator | round-33 rows are the tail |
| 8 | `SCORECARD.md` | append row | integrator | no round-34 row |
| 9 | `reports/round-34/**` (63 seat fragment paths, `targets.json:13-77`) | new | seats | 3 of 66 files present |
| 10 | `reports/round-34/run-validation.py` + `validation.json` | new | integration pass | absent |
| 11 | `../MANIFEST.json` (fleet root) | append `rounds[]` entry | integrator | r33 is the last entry |
| 12 | `../.ufo/reports/round-34/kotodama.md` | new fleet report | integrator | absent |

**Byte-preservation (must stay untouched, verified clean, §4 C1–C5):**
`reports/round-{2,4,5,6,30}/handoff/**` (the four filed packet revisions' bytes),
`reports/round-1..33/**` as a whole, `corpus/lessons/*.md`,
`tools/gates/frozen/**`, fleet `.ufo/**` outside the new round-34 report.
Superseded-but-filed means **new rows, never edits** — the same ruling the
round-33 LOG rows record for the lessons README and the SKILL digest.

---

## §3 Commit-ready list

Staging set for the round-34 commit (lane repo), in dependency order:

1. `git add reports/round-34` — the whole round tree: `claims.json`,
   `targets.json`, `telemetry/` (dispatch-declared + observed + closing
   snapshot once `validation.json` lands, `AGENTS.md` §telemetry), the 63 seat
   fragments per `targets.json`, `depth/`, `op/`, `calib/`, `cross/`, `review/`,
   `scribe/`, the `handoff/declared-in-r7/` five-file revision, and
   `run-validation.py` + `validation.json` from the integration pass.
2. `tools/exercise-handoff-e2e.py` — the 2-line default move (only after D10's
   block is verified against live bytes by D19; the exact before text is in §2).
3. `LOG.md` — the new supersession rows (append-only; no prior byte rewritten).
4. `SCORECARD.md` — the round-34 depth row (and the O/C rows the integrator
   records for their claims).
5. Fleet-root artifacts, by the parent/integrator, outside this repo:
   `../MANIFEST.json` `rounds[]` entry and `../.ufo/reports/round-34/kotodama.md`.

Pre-commit must-exist checklist (all absent at my cut):

- [ ] `reports/round-34/handoff/declared-in-r7/` five files, with
      `packet_sha256` in `freeze.txt` equal to the sha256 of the filed
      `packet.md` (the r6 self-check that today reads 6ced88ad… == freeze.txt,
      §4 C3).
- [ ] Gate green on the new pair: `fields=16/16`, `glossary-entries=20`,
      `findings=0` (`claims.json:32`), links `105/105` and 27 claims (r6's own
      frozen expectations, `expected.json` `links`/`uncertainty` blocks).
- [ ] `e2e --profile v3 --quiet` exit 0 with `packet_sha256 == freeze.txt`
      (`claims.json:33`).
- [ ] Zero D4-context stale figures in the new packet (§5's scoping rule).
- [ ] `LOG.md` rows name every re-pointed surface (K02 census, superseded rows).
- [ ] Telemetry: observed-dispatch record + closing snapshot (owes
      `validation.json`; `reports/round-34/telemetry/dispatch-declared.json`
      `closing_snapshot` field).

**Count honesty for the report header** (do not repeat blindly): `targets.json`
declares `seat_count: 64` and `telemetry/dispatch-declared.json` declares
`requested_workers: 64`, but `seats[]` holds **63** objects
(`len(json.load(open('reports/round-34/targets.json'))['seats'])` → 63) and the
declared composition sums to 63. Whether a 64th seat was intended is
`to-verify` (owner: orchestrator). The report should state declared 64 and the
observed launch count from the observed-dispatch record, and name the 63-target
inventory as the fragment surface — never claim 64 fragments.

---

## §4 Measurements taken by this seat (before → after, D block)

**A. The stale cells in the current default pair** (all `file:line` on
`reports/round-30/handoff/declared-in-r6/packet.md`, read directly):

| Cell | r6 packet reads | Live value | Live source |
|---|---|---|---|
| D4-CL05 `typed_labels` (`:148`) | 74 | **82** | `examples/culture-d4/typed-labels.d4.yml:46` |
| D4-CL05 native-form (`:148`) | 56 | **64** | `…typed-labels.d4.yml:37` |
| D4-CL05 translated-label (`:148`) | 12 | 12 | `:38` |
| D4-CL05 borrowed-strata (`:148`) | 6 | 6 | `:36` |
| D4-CL05 `findings_total` (`:148`) | 16 | **12** | `:32` |
| D4-CL05 `findings_hold_or_fail` (`:148`) | 15 | **12** | `:31` |
| D4-CL06 `hold` (`:149`) | 15 | **12** | `expected-holds.json` `counts.hold` |
| D4-CL06 `note` (`:149`) | 1 | **0** | `expected-holds.json` `counts.note` |
| D4-CL06 hold composition (`:149`) | 12 form + 3 rank + 1 note | **12, all `D2L-FORM-UNRESOLVED`; 0 notes** | `expected-holds.json`: `len(holds)==12`, `len(notes)==0` |
| D4-CL07 conflicts (`:150`) | 4 | **0** | `…typed-labels.d4.yml:30` |
| D4-CL07 quarantine handles (`:150`) | 3 | **0** | `:40` |
| D4-CL07 reconciliation records (`:150`) | 6 | 6 | `:45` |
| D4-CL09 rank items (`:152`) | 13 | **0** | `:44` |
| D4-CL09 quarantine handles (`:152`) | 3 | **0** | `:40` |
| D4-CL09 conflicts (`:152`) | 4 | **0** | `:30` |
| OQ-V3-05 (`:307`) | 12+3 holds, 1 note, 13 items, 3 handles, 4 conflicts | **12 holds, 0 notes, 0/0/0** | sources above |

Also live and unchanged: `label_findings_fail` 0 (`:33`), `label_findings_hold`
12 (`:34`), `rank_rules_component`/`gate_projected`/`normalized` 4/4/4
(`:41-43`), `era_reconciliation.alias_rows` 4 — so r6's manifest row A-30
("82 labels … 12 findings, 0 unresolved rank items, 4 era-alias rows",
`:68`) and A-31 ("12 holds / 0 note / 0 fail", `:69`) **already read live**:
the self-contradiction is confirmed by direct read, not inferred.

**B. The after state** (NOT measurable at my cut — no `declared-in-r7` exists):
renderer default `declared-in-r7`, zero stale cells, gate 16/16 + 20/20 + 0,
links 105/105, 27 claims, `packet_sha256 == freeze.txt`. All `{{owed}}`; owner
= D02/D05/D06/D07/D09 → integrator. Do not write these as achieved before the
artifacts land.

**C. Preservation/state commands run (this seat, 2026-10-19):**

1. `git status --porcelain` → only `?? reports/round-34/` — no filed byte
   modified by the wave so far.
2. `git status --porcelain reports/round-2{2,6,30} reports/round-8` → empty
   (clean) for the filed handoff trees.
3. `sha256sum reports/round-30/handoff/declared-in-r6/packet.md` →
   `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`, equal to
   the `packet_sha256` recorded in that revision's own `freeze.txt` and
   `expected.json` — the r6 pair is intact and its pin self-consistent.
4. `sha256sum reports/round-30/handoff/declared-in-r6/twin.json` →
   `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e`, equal to
   `freeze.txt`'s `twin_sha256`.
5. `sha256sum examples/culture-d4/typed-labels.d4.yml` →
   `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`, equal to
   the r6 `expected.json` inputs pin (`expected.json:161`); likewise
   `expected-holds.json` → `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3`
   (`expected.json:158`). **The packet pins the live bytes and then
   mis-describes them** — the sharpest one-line statement of claim D's defect,
   usable in the report.
6. `grep -rn "declared-in-r6" --include=* -l .` (excluding `.scratch`,
   `reports/round-34`) → 36 paths; the actionable non-filed code surface is
   `tools/exercise-handoff-e2e.py` (other hits are filed evidence, the
   historical SCORECARD row, `LOG.md`, the `.git/index` binary, and a `.pyc`).
   Cross-check only — K02 owns the authoritative census.

---

## §5 Audit scoping rule (prevents a false-firing "zero stale figures" check)

The numerals **13 unresolved rank items / 3 quarantine handles / 4 conflicts /
16 findings** are *live and correct for D2* (`examples/culture-d2/typed-labels.d2.yml`
coverage: typed_labels 58, findings_total 16, findings_hold_or_fail 15, rank
items 13, quarantine 3, conflicts 4, reconciliation records 10; matches
`packet.md:49` A-11 row, `:129` D2-CL01, `:284`, and OQ-V2-03 `:301`). They are
stale **only where the packet attaches them to D4** — `:148-152`, `:307`.
Any stale-figure scan (D20's mandate, `targets.json:42`, and the round-34
validator leg) must therefore be **D4-context-scoped** (rows `D4-CL*` and
`OQ-V3-*`), or it will false-fire on the D2 rows and report a defect that does
not exist. Recorded here because the scribe material is where this audit
instruction will be read next.

---

## §6 This seat's writes and non-writes

- Wrote: this file only inside the repo (`reports/round-34/depth/D14-scribe.md`);
  the one other write was outside the repo, a transient grep listing at
  `/tmp/repin_surfaces.txt` (no repo byte touched).
- Ran: read-only commands (`find`, `git status`, `git log`, `sha256sum`, `grep`,
  `python3 -c` JSON reads, `awk`/`sed` reads). No scratch writes were needed;
  `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1` were exported before
  every python invocation.
- Did not run: any `reports/round-*/run-validation.py` (F-C13-1 prevention), any
  other filed runner, any gate that rewrites a filed receipt, any git mutation.
- Did not edit: `tools/exercise-handoff-e2e.py` (drafted above, never applied),
  `LOG.md`, `SCORECARD.md`, MANIFEST.json, any filed round byte.

## Owed

Sibling fragments this draft quotes or fills from — all absent at my cut; the
integrator completes each `{{…}}` token once these land:

- `reports/round-34/scout/K01-packet-state.md` — packet-state scout (stale census cross-check).
- `reports/round-34/scout/K02-repin-census.md` — authoritative re-pin surface table (fills §1/§2/§3 LOG-row and cascade lists).
- `reports/round-34/plan/P01-d-plan.md` — claim-D execution plan (§1 chain order).
- `reports/round-34/depth/D01-layout.md`, `D02-render.md`, `D03-ledger-rows.md`, `D04-oq-glossary.md`, `D05-packet-draft.md`, `D06-twin-expected.md`, `D07-gate-run.md`, `D08-links-uncertainty.md`, `D09-freeze-design.md`, `D10-repin-drafts.md`, `D11-preservation.md`, `D12-receipt.md`, `D13-negatives.md` — all §1/§2/§3 fills (`{{D03/D05 row table}}`, `{{D06/D09/D12}}`, `{{D10 before/after block}}`, digests, verdict pointers).
- `reports/round-34/depth/D15-gap-fill.md`, `D16-gap-fill.md` — gap-fill record (§1).
- `reports/round-34/depth/D17-verify-gates.md`, `D18-verify-ledger.md`, `D19-verify-repin.md`, `D20-verify-preservation.md` — independent verification of §3's checklist items (§1/§2 pointers; D19 is the precondition for staging item 2).
- `reports/round-34/review/R01-d-review.md`, `R02-d-review.md`, `R03-d-review.md` — reviewer findings folded as accepted/errata by S01.
- `reports/round-34/cross/X00-connector.md` — shared-file collision matrix / integration order (§3 order may be amended).
- `reports/round-34/scribe/S01-d-receipt.md` — final D receipt (supersedes this draft's prose once review lands).
- `reports/round-34/telemetry/observed-dispatch.json` (or the round's chosen name) — observed launches/completions; feeds §3 count honesty.
- `reports/round-34/run-validation.py`, `reports/round-34/validation.json` — acceptance; also closes the telemetry snapshot.

## Citations

Paths read (with the lines actually used):

- `reports/round-34/targets.json` — `:3` seat_count 64, `:14-15` K01/K02, `:19` P01, `:36` D14 mission, `:42` D20 mandate; seat objects `:13-77`.
- `reports/round-34/claims.json` — `:8` baseline da68a6d, `:22-37` claim D (before/after/counting commands/thresholds), `:39-52` claim O, `:54-66` claim C.
- `reports/round-34/telemetry/dispatch-declared.json` — allocation, `closing_snapshot`, `baseline_commit`.
- `REGIMEN.md` — `:25-50` per-round contract, `:43-50` record set (SCORECARD/LOG/report/MANIFEST/telemetry).
- `AGENTS.md` — telemetry and close-what-you-open rules (fleet section quoted in-repo).
- `reports/round-32/run-validation.py:50-55` — the fleet report's four headings.
- `reports/round-30/handoff/declared-in-r6/packet.md` — `:68-69` manifest rows, `:148-152` D4 claim rows, `:284` D2 read-only facts, `:304-307` OQ rows.
- `reports/round-30/handoff/declared-in-r6/expected.json` — `:158,:161` input pins; `counts`/`links`/`uncertainty`/`packet_sha256` blocks.
- `reports/round-30/handoff/declared-in-r6/freeze.txt` — packet/twin digests, gate verdict line.
- `examples/culture-d4/typed-labels.d4.yml` — `:29-47` coverage block (live D4 values), `era_reconciliation.alias_rows`.
- `examples/culture-d4/expected-holds.json` — `counts` {hold 12, note 0, fail 0}, `holds` 12 × `D2L-FORM-UNRESOLVED`, `notes` 0.
- `examples/culture-d2/typed-labels.d2.yml` — coverage (D2 live values, the §5 scoping case).
- `tools/exercise-handoff-e2e.py:1933-1934` — live renderer defaults (quoted verbatim in §2).
- `reports/round-33/adj/A02-handoff.md:92-94` — A02-H1 wording ("shape-green and semantically stale").
- `LOG.md` — final sections (F-C13-1 entry; "Supersession records (new rows; no filed byte rewritten)"; operator concurrency directive).
- `../.ufo/reports/round-33/kotodama.md`, `../.ufo/reports/round-32/kotodama.md`, `../.ufo/reports/round-30/kotodama.md` — report register and section shape.
- `../MANIFEST.json` — `rounds[]` entry shape (last entry = round 33).

Commands run (with observed results):

- `find reports/round-34 -type f | sort` → 3 files (claims.json, targets.json, telemetry/dispatch-declared.json).
- `git status --porcelain` → `?? reports/round-34/` only.
- `git status --porcelain reports/round-2{2,6,30} reports/round-8` → empty.
- `git log --oneline -1 -- reports/round-30/handoff/declared-in-r6/packet.md` → `71cd9d3`.
- `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,twin.json} examples/culture-d4/{typed-labels.d4.yml,expected-holds.json} examples/culture-d2/typed-labels.d2.yml` → digests in §4 C3–C5.
- `python3 -c "import json; …"` JSON reads of `expected-holds.json`, `typed-labels.d4.yml`, `typed-labels.d2.yml`, `targets.json`, `MANIFEST.json` → counts and lengths in §4/§5.
- `grep -rn "declared-in-r6" --include=* -l .` (minus `.scratch`, `reports/round-34`) → 36 paths (§4 C6).
- `grep -n "^## " reports/round-30/handoff/declared-in-r6/packet.md` → 9 sections (delivered record sets, artifact_manifest, dependency_manifest, claim_ledger, coupling_edges, requested_decisions, validation, open_questions, glossary payload).
