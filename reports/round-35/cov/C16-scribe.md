- Seat: C16 | scribe | C | date 2026-10-19 | baseline 4a7aede

# C16 — landed-changes material for the fleet report (claim C)

Mission: supply the `Landed changes` section material for this round's fleet
report (`../.ufo/reports/round-35/kotodama.md`, integrator-authored). Method:
measure every change surface at the declaration cut, pin a digest for each
surface the round may move, hand the integrator a paste-ready section plus the
recompute commands that prove each row in it, and name what is still owed.

Every `before` value below was measured by this seat on 2026-10-19 at HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (commands in §6); every `after`
value is a `{{...}}` slot listed under `## Owed`. No promotion, canon,
clearance or closure verdict is claimed anywhere in this file — each such
token appears only as a negation or a routed reference.

## §0 — Point-in-time state at this seat's read

- `date -u +%FT%TZ` → `2026-10-19T08:14:32Z` (first read), `2026-10-19T08:15:18Z`
  (re-census); `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
  (committed `2026-10-19T05:01:17-03:00`).
- `find reports/round-35 -type f` → **6 files**: `claims.json`, `targets.json`,
  `telemetry/{dispatch-declared,availability-attempt-1,availability-attempt-2,
  availability-attempt-3}.json`. **Zero seat fragments had landed** at that
  read, so §1's coverage/operability/adjacency rows are declared requirements,
  not observations.
- `git status --porcelain=v1 -uall` → exactly those 6 rows, all `??`; **no
  modified tracked path** anywhere in the tree.
- `git ls-files | wc -l` → 2815 tracked paths.
- Seat census from `reports/round-35/targets.json` (measured): **64 rows ==
  declared `seat_count: 64`**, 64 unique `out` paths, no duplicate ids. Roles
  `{scout 4, planner 2, connector 1, executor 26, verifier 8, scribe 10,
  reviewer 9, critic 4}`; claims `{C 24, O 16, A 15, cross 9}`; out directories
  `{scout 4, plan 2, cross 5, cov 17, op 11, adj 11, review 9, scribe 5}`.
  This round has **no** round-34-style seat-count deviation.
- C16's own binding row: `targets.json:170-174` (id/role/claim/mission/out).

## §1 — Fleet-report `Landed changes` section (paste-ready draft)

Heading contract: the four required headings are `Work performed`,
`Landed changes`, `Before → after measurements`, `SHONEN`
(`reports/round-33/run-validation.py:70-75`; restated at
`reports/round-34/run-validation.py:319`). Fill the `{{...}}` slots from the
landed fragments, then verify every row with §3.3 before filing.

```text
## Landed changes

The round lands in one integrating pass after the wave. At the declaration cut
(`reports/round-35/claims.json`, sha256 ccfaafc3…) zero seat fragments had
landed; every row below is either a seat fragment landed during the wave or an
integrator-applied file.

- `corpus/knowledge/culture-material/` — {{6 new entries}}: {{paths}}. Each is
  an addition; no pre-existing corpus file is edited (baseline set digest
  cc5deee3…, §3.2).
- `corpus/knowledge/myth-symbol/` — {{4 new entries}}: {{paths}}.
- `corpus/README.md` — revision 2.0 reconciliation for the ten additions
  (rows, totals line, footer vector and the two section headers move together,
  §4; drafted byte-exact by C11 at `cov/C11-readme-delta.md:69-130`, which also
  notes the next-value convention behind 2.0). Before `053966a2…` (493 lines,
  106,218 bytes) → after `{{digest}}`.
- `tools/exercise-handoff-e2e.py` — the R34-N1 hardening: the superseded-baseline
  read-set member raises a named diagnostic instead of an unhandled KeyError
  (drafted by O01/O02, applied by the integrator). Before `34c85f57…` (4613
  lines; default pair at `:1933-1934`, `CLAIMS_MAP` at `:184`) → after
  `{{digest}}`; renderer selftest {{N/N}}.
- `reports/round-35/adj/` — {{the assembled adjacency audit document}}
  (A08's draft, finalized by the integrator) plus the PROVINCE re-verification
  record (A06/A11).
- `reports/round-35/run-validation.py` + `reports/round-35/validation.json` —
  this round's acceptance runner and receipt (integrator-authored; no seat
  executed it).
- `reports/round-35/telemetry/` — `dispatch-declared.json` (filed) plus the
  observed-dispatch record and the closing snapshot
  `availability-close-35.json`, which closes `dispatch-declared.json`
  (sha256 `93e205a2…` at this read).
- `../.ufo/reports/round-35/kotodama.md` — this report; fleet-root
  `MANIFEST.json` round-35 entry; append-only `SCORECARD.md` and `LOG.md` rows.
- Filed bytes: **zero** writes to `reports/round-1..34/**`,
  `corpus/lessons/*.md`, `tools/gates/frozen/**` (§3.1 measured 0 rows), and the
  `declared-in-r7` freeze pair stays pinned at `45f57132…` (no re-freeze).
- Seat fragments: {{landed}} of 64 declared `out` paths landed;
  {{missing list}} recorded in `missing_dependencies`.
```

## §2 — Change-surface inventory (before digests measured; after slots owed)

| surface | class | drafted by | applied by | before (measured 2026-10-19) | after |
|---|---|---|---|---|---|
| `corpus/knowledge/culture-material/<6>.md` | new files | C01-C06 | integrator | absent (partition = 18 files) | {{names + digests}} |
| `corpus/knowledge/myth-symbol/<4>.md` | new files | C07-C10 | integrator | absent (partition = 19 files) | {{names + digests}} |
| `corpus/README.md` | edit | C11 | integrator | `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`, 493 lines, 201 index rows | {{digest, lines, rows}} |
| `tools/exercise-handoff-e2e.py` | edit | O01/O02 | integrator | `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`, 4613 lines | {{digest, selftest count}} |
| `reports/round-35/**` seat fragments | new files | seats | seats (own `out`) | 0 of 64 landed at 08:15Z | {{landed count}} |
| `reports/round-35/run-validation.py`, `validation.json` | new files | integrator | integrator | absent | exit 0 / receipt digest |
| `reports/round-35/telemetry/observed-dispatch.json`, `availability-close-35.json` | new files | integrator | integrator | absent; `dispatch-declared.json` = `93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83` | close names `closes` + `closes_sha256` |
| `../.ufo/reports/round-35/kotodama.md` | new file | integrator | integrator | directory absent at 08:15Z | 4 headings + date |
| `/home/vgpnk/Projects/shokunin/MANIFEST.json` | edit (fleet root) | integrator | integrator | round-34 row filed (close stamp `2026-10-19T05:01:37-03:00`) | round-35 row |
| `SCORECARD.md`, `LOG.md` | append-only | integrator | integrator | `e972478b…`, `24331e82…` | new rows only |

Never-move set (see §3): `reports/round-1..34/**`, `corpus/lessons/*.md`,
`tools/gates/frozen/**` (2,404 tracked protected paths), the 201 pre-existing
`corpus/knowledge/**/*.md`, and the `declared-in-r7` freeze bytes.

## §3 — Preservation legs and recompute commands

### §3.1 Protected prefixes (measured clean)

- `git status --porcelain=v1 -uall -- reports/round-1 … reports/round-34
  corpus/lessons tools/gates/frozen` → **0 rows**; `git diff --stat 4a7aede --
  reports corpus/lessons tools/gates/frozen` → **empty**. 2,404 tracked paths
  are in the protected set; `corpus/lessons/` holds 33 files.
- The freeze pin survives: `sha256sum
  reports/round-34/handoff/declared-in-r7/packet.md` →
  `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, equal to
  the `packet_sha256:` line of the same directory's `freeze.txt`
  (`3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223`).

### §3.2 Corpus baseline (the 201-file set the ten additions must not disturb)

- Census: linguistics 21 / myth-symbol 19 / culture-material 18 / synthesis 29 /
  verification 20 / civilizations 94 = **201**; `git ls-tree -r --name-only
  4a7aede -- corpus/knowledge | wc -l` → **201** (the baseline commit agrees
  with the working tree, so the ten additions are the only delta).
- Aggregate digest over the sorted 201 files:
  `find corpus/knowledge -name '*.md' | sort | xargs sha256sum | sha256sum` →
  `cc5deee39b7e0bc369fa36979ec524bddef02ea139796347b915a548bddb880c`.
  Per-partition: linguistics `c6248d92…`, myth-symbol `da0505ad…`,
  culture-material `ef0560da…`, synthesis `d6fdacc4…`, verification `b88fc106…`,
  civilizations `d1c50bf4…` (all sha256, same command scoped per directory).
- Inventory tool at the same cut: `python3 -B tools/source-audit-inventory.py
  --json --summary --root corpus/knowledge` → `totals.files: 201`
  (the claim's own counting command; after = 211).

### §3.3 Recompute commands (run these before filing the report)

```bash
# seat-fragment landing census (do not trust §0's snapshot)
python3 -c "import json,os;t=json.load(open('reports/round-35/targets.json'));print([s['out'] for s in t['seats'] if not os.path.isfile('reports/round-35/'+s['out'])])"
find reports/round-35 -type f | wc -l
# the ten additions must be the ONLY corpus delta: expect exactly 10 ?? rows
git status --porcelain=v1 -uall -- corpus/knowledge
comm -13 <(git ls-tree -r --name-only 4a7aede -- corpus/knowledge | sort) \
         <(find corpus/knowledge -name '*.md' | sort)
# protected bytes: expect 0
git status --porcelain=v1 -uall -- reports corpus/lessons tools/gates/frozen \
  | grep -vE '^\?\? reports/round-35/' | wc -l
# after-digests for the two edited surfaces
sha256sum corpus/README.md tools/exercise-handoff-e2e.py
# freeze pin: expect the two digests of §3.1
sha256sum reports/round-34/handoff/declared-in-r7/packet.md
```

## §4 — Coverage before → after anchors (must agree with §1's rows)

| surface | before (measured) | after required (`claims.json:22-35`) | proof |
|---|---|---|---|
| culture-material partition | 18 files | 24 | `ls corpus/knowledge/culture-material/*.md \| wc -l` |
| myth-symbol partition | 19 files | 23 | `ls corpus/knowledge/myth-symbol/*.md \| wc -l` |
| corpus total | 201 | 211 | `ls corpus/knowledge/*/*.md \| wc -l`; inventory `totals.files` |
| README index rows | 201 (`corpus/README.md:1-493`, `053966a2…`) | 211 | `grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md` |
| README totals line | `corpus/README.md:469` = `Total knowledge entries: 201.` | 211 | `sed -n '469p' corpus/README.md` |
| README counts footer | `corpus/README.md:473` = `(total 201 files; directory totals 21/19/18/29/20/94).` | `(total 211 files; directory totals 21/23/24/29/20/94).` | `sed -n '473p' corpus/README.md` |
| README section headers | `:147` `## myth-symbol/ (19)`, `:169` `## culture-material/ (18)` | `(23)`, `(24)` | `grep -n '^## [a-z-]*/ (' corpus/README.md` |

`corpus/README.md` currently carries revision 1.9 (`:1-12`); the footer's
re-measure convention (`:471-473`) is the pattern the new revision follows.

## §5 — Notes, traps and honesty items for the integrator

- **C16-N1 (declaration census drift).** `telemetry/dispatch-declared.json`'s
  `allocation.seat_composition` prose census ("authors 10, verifiers 11 …")
  does **not** equal the measured role census of §0 (`executor 26, verifier 8,
  scribe 10 …`). Measure, never quote the string; the pinned digests
  (`claims.json` `ccfaafc3…`, `targets.json` `56ad0392…`, both re-verified
  live) are the authority. The declaration also records that `targets.json`
  was re-authored 60 → 64 seats before dispatch; the pinned digest is the
  64-row file, which is what §0 measured.
- **C16-N2 (declared lane vs actual route).** `claims.json:11` declares
  `provider_lane: opencode-go-3` per the REGIMEN schedule, but attempts 1-3 on
  keys 3/4/5 each failed 64/64 at launch with the same 402
  (`telemetry/availability-attempt-{1,2,3}.json`), and attempt-3's
  `disposition` records the re-dispatch on **key 1** as the named deviation.
  The observed-dispatch record must keep requested allocation separate from the
  observed route and name the three skipped attempts; never edit `claims.json`.
- **C16-N3 (the README has four count surfaces, not one).** Rows, totals line,
  footer vector and the two section headers must move together; moving only
  some of them reproduces the round-20 / round-33 reconciliation failure class.
  C11's delta draft owns the exact before/after bytes.
- **C16-N4 (additions only).** The ten new entries must be new paths. Editing
  any pre-existing `corpus/knowledge` file breaks the §3.2 aggregate digest
  and the corpus-baseline leg; the ten-`??`-rows command in §3.3 is the
  detector.
- **C16-N5 (no invented landed paths).** Every path named in the filed
  `Landed changes` section must exist at filing time; run §3.3 first. Do not
  carry `{{...}}` slots into the filed report.
- **C16-N6 (telemetry close).** The closing snapshot is a new file named
  `reports/round-35/telemetry/availability-close-35.json`, carrying `closes` +
  `closes_sha256` (the dispatch-declared digest `93e205a2…`, or the digest read
  at close time) so a later in-place edit is detectable; unknown counters stay
  `null` with an owner and reason (AGENTS.md availability rules).
- **C16-N7 (claim O wording).** The hardening is a renderer diagnostic change:
  the `Landed changes` row must describe the *diagnostic* and the preserved
  digest-mismatch path, not claim a behavior change to the frozen packet
  (`declared-in-r7` bytes stay pinned; no re-freeze).

## §7 — Wave-progress addendum (same wave, after §1-§6 were written)

`find reports/round-35 -type f` at `2026-10-19T08:18:23Z` → 8 files: the six
declaration/telemetry files of §0, plus `cov/C15-receipt.md` and this file. The
wave was still dispatching at that read, so §0's "zero fragments landed"
statement is true at its own timestamp (`2026-10-19T08:15:18Z`) and is
superseded here rather than rewritten. Recompute the landing census with §3.3
before quoting any count.

Language leg pre-cleared for this file: running the filed round-33 instrument
(`reports/round-33/adj/A08-language.md`'s embedded scanner, pinned digest
`73296aa4…`, its selftest 17/17) over this fragment yields 25-26 broad hits, all
classified `NEGATION` / `MENTION-EXEMPT` / `ROUTED-REFERENCE` / `CITED-RESULT`,
and 0 strict hits — zero `UNSUPPORTED-CLAIM` rows, on both scanned revisions
(`37f541e0a09e3d8da5544e9ab03aa41ac153edfd877052c68ed2841ee6d025b5`, 286 lines,
and the revision carrying this addendum). A stored digest of this file is
self-invalidating — every edit moves it — so the authoritative check is the
re-run itself over `reports/round-35/cov/C16-scribe.md`, plus
`sha256sum` for whatever revision is on disk.

## §8 — Landed-fragment cross-check (2026-10-19T08:20Z, same wave)

Fragments landed while §1-§7 were being written; this section folds in what they
supply and restates what is still owed. Recompute the census with §3.3 — at this
read **19 of 64** declared `out` paths had landed and 45 were still absent,
including every C author seat (`cov/C01`-`C10`), `plan/P01-c-plan.md`,
`cov/C12`-`C14`, `cov/C17`, and the O patch seats (`op/O01`-`O03`, `O05`, `O11`).

**Filled from C11 (`cov/C11-readme-delta.md`).** Its baseline readings agree
with §3.2 independently: 201 files, README sha256 `053966a2…`, 493 lines,
106,218 bytes, and the lane instrument `reports/round-28/readme/sweep.py`
(digest `9b2ccac0…`, `--selftest` 12/12) reports `rows 201 files 201`. The
drafted after-state for the four count surfaces: `## myth-symbol/ (23)`
(`C11:92`), `## culture-material/ (24)` (`C11:99`), `Total knowledge entries:
211.` (`C11:106`), `(total 211 files; directory totals 21/23/24/29/20/94).`
(`C11:118`), plus the dated footer re-measure line (`C11:126`) and a new dated
index paragraph appended after line 493 (`C11:137-143`). Its measured acceptance
on a synthetic +10 tree: `rows 211 files 211`, `missing_from_index 0`,
`topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, exit 0, inventory
`totals.files 211` (`C11:368-370`). The ten entry names stay `⟨slots⟩` until
C01-C10 land, and the applied bytes are still owed.

**Filled from O10 (`op/O10-scribe.md`).** Its baseline measurements agree with
§2's renderer digest (`34c85f57…`) and add the control counts the fleet-report
row should quote: `--selftest` exit 0 with 17 controls (v1) and 39 controls
(v3); the r7 default chain exit 0 with `packet_sha256=45f57132…`
(`O10:64-66`); the r6 row replay exit 1 with the unhandled `KeyError` at `:3822`
fed by the `.get` at `:3819` (`O10:27-32`). It also measures `grep -c E2E-READSET
tools/exercise-handoff-e2e.py` → **0** (`O10:55-56`): the preferred diagnostic
code is new, so §1's renderer row must name whichever code the landed patch
uses, and the exit-code vocabulary it must not disturb is at `:89-93`.

**Still owed for claim C.** `plan/P01-c-plan.md` (topics + author assignment),
`cov/C01-entry-1.md` … `cov/C10-entry-10.md` (the ten entry bytes, hence the ten
new paths and their digests), `cov/C12-audit-runbook.md`, `cov/C13-audit-1-5.md`,
`cov/C14-audit-6-10.md`, `cov/C17-audit-sample.md` (the two-auditor requirement
at `claims.json:35`), and the integrator's applied README bytes plus the
after-digest of `corpus/README.md` and `tools/exercise-handoff-e2e.py`.

## Owed

The wave had landed **no** seat fragments at this seat's first read (§0); §8
records the 19 that landed during the wave and what they fill. Everything below
is owed at this file's cut. Exact paths:

- `reports/round-35/plan/P01-c-plan.md` — the ten entry topics + author
  assignments (fills the `{{6 new entries}}` / `{{4 new entries}}` slots).
- `reports/round-35/cov/C01-entry-1.md` … `cov/C10-entry-10.md` — the ten full
  entry drafts (paths + bytes for §2 rows 1-2).
- `reports/round-35/cov/C11-readme-delta.md` — the README before/after bytes
  (§4's four surfaces).
- `reports/round-35/cov/C12-audit-runbook.md`, `cov/C13-audit-1-5.md`,
  `cov/C14-audit-6-10.md`, `cov/C17-audit-sample.md` — the audit evidence the
  report's coverage row should cite.
- `reports/round-35/op/O01-patch-draft.md`, `op/O02-controls.md`,
  `op/O03-isolated-verify.md`, `op/O05-verify.md`, `op/O11-verify-2.md` — the
  renderer patch + its isolated verification (fills the
  `tools/exercise-handoff-e2e.py` after-digest and selftest-count slots).
- `reports/round-35/adj/A08-audit-draft.md` (assembled audit document),
  `adj/A06-province.md`, `adj/A11-verify-2.md` — the adjacency rows.
- `reports/round-35/scribe/S04-integration-draft.md` — the sibling dossier this
  section must stay consistent with.
- Integrator-only, absent at this read: `reports/round-35/run-validation.py`,
  `reports/round-35/validation.json`,
  `reports/round-35/telemetry/observed-dispatch.json`,
  `reports/round-35/telemetry/availability-close-35.json`,
  `../.ufo/reports/round-35/kotodama.md`, the fleet-root `MANIFEST.json`
  round-35 entry, and the `SCORECARD.md` / `LOG.md` rows.

## Citations

- `reports/round-35/claims.json:8,10-16,17,19,22-35,36-53,54-66,68-73` —
  baseline `4a7aede`, dispatch declaration (lane key 3, 64 requested, one
  batch), `axes_in_play`, freshness pause, the C/O/A claims with
  before/after/thresholds, non-goals.
- `reports/round-35/targets.json:3,5-12,14-463,170-174` — `seat_count: 64`,
  `shared_rules`, the 64 seat rows, C16's own row.
- §8 landed-fragment reads (2026-10-19T08:20Z): `reports/round-35/cov/C11-readme-delta.md:11-15,33-35,69-130,137-143,368-370`
  (pinned README bytes, the three agreeing baseline readings, the five
  before/after edits + the new paragraph, the synthetic-tree acceptance) and
  `reports/round-35/op/O10-scribe.md:16-32,55-56,60-66` (the R34-N1
  reproduction, the read-set arithmetic, the diagnostic vocabulary, the control
  counts); `reports/round-28/readme/sweep.py` digest `9b2ccac0…` per C11:25.
- `reports/round-35/telemetry/dispatch-declared.json` (keys
  `durable_sources[0].sha256` = `ccfaafc3…`, `[1].sha256` = `56ad0392…`,
  `allocation.seat_composition`, `closing_snapshot` = `open-at-seat-close`);
  `availability-attempt-1.json`, `-2.json`, `-3.json` (402 failures,
  `key_census_so_far`, the key-1 reuse disposition).
- `REGIMEN.md:13,25-29,34-36` — the round-35 schedule row, the per-round
  contract (claims, verdicts, records), and the round-record requirements
  (`MANIFEST.json rounds[]`, telemetry).
- `AGENTS.md` — availability/dispatch telemetry rules (durable samples,
  requested-vs-observed separation, unknown counters `null`, close-what-you-open,
  closing snapshot as a new digest-pinned file).
- `reports/round-33/run-validation.py:70-75,868-930` — the four fleet-report
  headings and the language-scan adjudication pattern;
  `reports/round-34/run-validation.py:319` — the same heading tuple.
- `reports/round-34/run-validation.py` / `reports/round-34/handoff/declared-in-r7/`
  — the R34-N1 finding and the freeze pair (`packet.md` `45f57132…`,
  `freeze.txt` `packet_sha256:` line, `3969954b…`).
- `corpus/README.md:1-12,147,169,469,471-473` — revision 1.9 header, the two
  section headers, the totals line, the footer vector and the re-measure
  convention.
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `git log -1 --format='%H
  %cI' 4a7aede`; `git ls-files | wc -l`; `git status --porcelain=v1 -uall`;
  `find reports/round-35 -type f`; `date -u +%FT%TZ`; the `targets.json` python
  census; the six-partition `ls | wc -l` census; `git ls-tree -r --name-only
  4a7aede -- corpus/knowledge | wc -l`; the aggregate and per-partition
  `sha256sum` digests; `python3 -B tools/source-audit-inventory.py --json
  --summary --root corpus/knowledge`; `sha256sum` over `corpus/README.md`,
  `tools/exercise-handoff-e2e.py`, `SKILL.md`, `AGENTS.md`, `SCORECARD.md`,
  `LOG.md` and the `reports/round-35/telemetry/*.json` files;
  `git status --porcelain=v1 -uall -- <protected prefixes>` and `git diff
  --stat 4a7aede -- reports corpus/lessons tools/gates/frozen`;
  `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-35` (absent);
  the round-34 entry read from the fleet-root `MANIFEST.json`.
