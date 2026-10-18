# R20-C — `corpus/README.md` reconciliation (R20-C01..C04)

- **seat:** R20-C01..C04 (C-readme). **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **assignment (verbatim):** "C R20-C01..C04 (README reconciliation x4):
  reconcile corpus/README.md against actual partition contents (command-carried
  counts: civ 94, ling 20, myth 19, culture 18, synth 29, verif 20); index rows
  == files; known-gaps updated; reports/round-20/readme/{reconcile,verify}.md."
- **date:** 2026-10-18, local clock UTC−03:00. Measurement window
  12:5xZ–13:02:57Z. **baseline revision:** `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`
  (`reports/round-20/claims.json`); **HEAD:** `122086b` plus the live round-20
  working tree (other seats' artifacts landed during this run — §6).
- **canon:** NON-CANON engineering evidence. This seat admits no entry, judges
  no entry's quality or sources, touches no gate, ledger, or canon.
- **writes:** `corpus/README.md`, this file, `reports/round-20/readme/verify.md`,
  and disposable scratch under `.scratch/`. No commit, no push.
- **counting command for this round:** `python3 reports/round-20/run-validation.py`
  — **absent at 13:02:30Z** (`ls reports/round-20/` showed no runner), landed
  from another seat ~13:06Z, and re-run in `--check` mode (no receipt write) at
  13:07:53Z: **claim C passes, `failures: []`**, revision checks
  `commanded/dated/numbers_present` all true, `placeholder` false. That run's
  full receipt shows D and O failing on their own in-flight artifacts (missing
  v3 baselines, stale pins), which are their seats' legs, not C's. This receipt
  still carries its own independent commands; the runner's verdict is quoted,
  not substituted for them.

## 0. Verdict at a glance

| claim | requirement | measured | status |
|---|---|---|---|
| C01 | counts command-carried against actual contents | `19/19/18/29/20/94` = 199 files, two independent methods (§1); the declared `ling 20` is **not reproducible** — the tree measures **19** | done, with the discrepancy recorded |
| C02 | index rows == files | 199 rows vs 199 files; 0 missing, 0 ghosts, 0 header drift; **10 topic mismatches measured and repaired** | done |
| C03 | known-gaps updated | 4 in-place dated corrections + 1 new round-20 bullet + tail re-measure line; every closure carries its command | done |
| C04 | receipts | this file + `verify.md` (independent re-measure, 10/10 controls) | done |

## 1. Counts, command-carried (C01)

Method 1 — the lane's own inventory (read-only, deterministic):

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files = 199; per-dir civilizations 94, culture-material 18, linguistics 19,
# myth-symbol 19, synthesis 29, verification 20
```

Method 2 — an independent plain-filesystem count:

```sh
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# 19 19 18 29 20 94;   find corpus/knowledge -maxdepth 2 -name '*.md' -type f | wc -l → 199
```

Both methods agree. **The round-20 C-claim declares `linguistics 20`; the tree
measures 19** (the declared six numbers sum to 200 against 199 files). The
README records the measured counts and the non-reproducible declaration
(revision 1.5, `corpus/README.md:3`), so the declared number cannot circulate
unqualified.

## 2. The sweep — index rows vs the files they name (C02)

**Convention** (derived by measurement in round 10, R10-C21, and enforced since):
every row is `- \`<file>\` — <topic>`, where `<topic>` is the entry's own
`- topic:` head-block text with continuation lines joined by single spaces;
rows ordered by filename within each partition. The sweep also checks the
`## <partition>/ (N)` header against the live file count and flags rows whose
file does not exist ("ghosts").

**Before** (12:5xZ, first run of this seat):

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/r20-c-readme-sweep.py
# parts {'linguistics': 19, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94} rows 199 files 199
# missing_from_index 0 []
# topic_mismatch 10 [the ten round-19 rows — §3]
# orphan_rows 0 []
# header_drift {}                       → exit 1
```

**After** (repair in §3, re-measured 13:02:57Z):

```sh
python3 .scratch/r20-c-readme-sweep.py
# parts {'linguistics': 19, 'myth-symbol': 19, 'culture-material': 18, 'synthesis': 29, 'verification': 20, 'civilizations': 94} rows 199 files 199
# missing_from_index 0 []
# topic_mismatch 0 []
# orphan_rows 0 []
# header_drift {}                       → exit 0
```

**Controls** — the sweep must be able to fail (fresh run, exit 0, 10/10):

```sh
python3 .scratch/r20-c-readme-sweep.py --selftest
# ok live: rows == files / 0 missing / 0 topic mismatches / 0 ghosts / 0 header drift
# ok control: planted paraphrase flagged (1 mismatch)
# ok control: truncated rewrite flagged (1 mismatch)
# ok control: planted ghost row flagged
# ok control: deleted row surfaces a missing file
# ok control: wrong header count flagged
# selftest: 10/10 checks passed
```

Control history, recorded because it is evidence about the sweep, not the
README: the first selftest run returned **8/9** — the planted-paraphrase control
compared the flagged row against the bare filename while the sweep reports
`partition/filename`; the sweep was right and the control's expectation was
wrong. Fixed, and a second control was added for the exact defect class found in
§3 (a truncated rewrite), giving the 10/10 above. The three planted controls
plus the two live legs are the reason the green sweep is readable as a
measurement rather than a blessing.

## 3. Drift found — the ten round-19 rows were condensed rewrites (C02)

All ten mismatches are the ten entries the round-19 wave landed; each README row
carried a **shorter rewrite** of the entry's topic, not the topic text (every
row: `REWRITE`, none a prefix-truncation, none a superstring):

| row | partition | row chars → topic chars |
|---|---|---|
| `era-material-scoped-reconciliation.md` | synthesis | 622 → 713 |
| `finding-disposition-workflow.md` | synthesis | 538 → 584 |
| `generated-artifact-lifecycle.md` | synthesis | 552 → 531 |
| `hold-set-contract-in-brief.md` | synthesis | 474 → 606 |
| `typed-label-routing-workflow.md` | synthesis | 620 → 658 |
| `gate-battery-surface-verification.md` | verification | 623 → 634 |
| `generated-artifact-roundtrip-verification.md` | verification | 640 → 616 |
| `label-channel-routing-verification.md` | verification | 634 → 529 |
| `pre-declared-hold-set-reconciliation.md` | verification | 620 → 548 |
| `two-reader-interop-agreement.md` | verification | 552 → 699 |

**History, measured, not inferred.** The ten entries' last-write mtimes are
2026-10-18 11:40:11–11:40:15Z; `corpus/README.md` was written at 11:40:46Z —
the rows were composed ~30 s *after* the topic texts were final, so they were
wrong from birth, not drifted by a later entry edit. At `169c616` the two
partitions held 24 (synthesis) and 15 (verification) entries and the README read
`revision: 1.3`; all ten entries and the revision-1.4 README landed together in
`caf1bea`.

**Why it survived round 19.** Revision 1.4's line asserts "every row is
re-measured against the files it indexes (199 rows, 0 missing, **0 topic
mismatches**…)". The round-19 coverage auditor's own tool states the opposite
scope: "*It does not verify that an indexed description matches its file's
content*" (`reports/round-19/audit/x27-coverage-readme-vs-files.md` §1), and its
five structural legs (§5) contain no topic comparison. The phrase then
propagated into `reports/round-19/report-draft.md:69` and
`reports/round-19/fragment-index.md:113` with no measuring command anywhere in
the round. So the assertion was **unmeasured**, not falsified by a tool; the
verbatim comparison had simply not been run since round 10.

**Repair.** The ten rows were replaced with their entries' current `- topic:`
text, byte-for-byte (multi-line topics joined with single spaces, the round-10
convention). The replacement was mechanical and asserted-unique:
`.scratch/r20-c-repair-rows.py` aborts unless each old row matches exactly once;
it wrote only `corpus/README.md` and left the diff at `.scratch/r20-c-rows.diff`
(22 `+`/`-` lines, 10 rows). `sha256` before
`3ecd619ed8bff84dbf9be74928599d7c6eb087899b060e81ffe92e44514549bc` → after
`fa1671218cb790f1ed22e0fa3a106004677a7b7bda559740f0e482a32b8db4fb`.

## 4. Known-gaps reconciliation (C03)

The section is chronological; corrections are dated notes appended to the
bullet they correct (round-10 discipline: no earlier bullet is deleted), and
the new round-20 bullet names the current open set. Every closure carries its
command.

| bullet (line at HEAD) | statement before | action | evidence (measured 2026-10-18) |
|---|---|---|---|
| replay-frozen / baselines (296) | "the separate per-gate `expected.json` layout … remains pending" | dated note (297–302) | `find tools/gates/expected tools/gates/frozen reports/round-9/baselines -name expected.json \| wc -l` → **17**; battery `coverage 9/9`, `pinned 17` |
| D2 needs (304) | "D2 still needs typed … rank-rule … scoped material/era reconciliation" | dated supersede note (311–318) | `python3 tools/d2-typed-labels.py --selftest` → **39/39, exit 0** (re-measured 13:02:57Z, after the O seat's concurrent edit); rank-rule adapter and `reconcile_scoped` present in the tool |
| D3 / round-7 (314) | "Round7 acceptance remains pending until `reports/round-7/validation.json` records the original F/O commands…" | dated note (328–331) | the file exists (last changed `a3f6fce`, round 11) and records `acceptance_checks_passed: false` — F claim wrong rejection, a preservation failure, the chained round-6 acceptance |
| round-19 battery clause (352) | "the D4 family is outside the battery's seven-name constant" | dated correction (366–373) | `python3 tools/check-gate-battery.py` → `pass 7 / fail 0 / unevaluable 0`, exit 0, `coverage 9/9` (7 structural + 2 D4 adapters, `REGISTERED_GATE_NAMES = GATE_NAMES + D4_GATE_NAMES`), `pinned 17`. The round-19 auditor had already flagged this sentence as a point-in-time reading (`x27` §6) |
| new (375) | — | round-20 bullet | names the three closures above and the still-open set |
| tail (404) | — | re-measure line | sweep command + receipts pointer |

**Still open after the sweep** (named, each with its measurement): 
`tools/gates/d4-assembly-check-gate.py` ships no `--selftest` (measured
`--selftest` → `assembly error … '--selftest'`, exit 2, re-measured 13:0xZ);
round-4 outputs have no frozen manifest (`tools/gates/frozen/round-4/` holds
five `.out` files only) and remain unpinned; the fleet header-conformance
question remains an integrator question
(`corpus/knowledge/verification/header-conformance-readings.md`); round-7
acceptance is recorded false; the round-5/6/7 claim residuals, the earlier
rounds' strict historical path whitelists, and cultural permission / name
screening / lore receipt / independent promotion review remain outside the
current evidence.

## 5. What this seat did not do

- No `corpus/knowledge/` byte, no gate, no ledger, no round-8..19 filed artifact
  was touched: `git diff --name-only` names `corpus/README.md` for this seat
  (the other modified paths — `reports/round-5/validation.json`,
  `reports/round-7/validation.json`, `reports/round-9/validation.json`,
  `tools/d2-typed-labels.py` — are other seats' concurrent writes, §6).
- Revision 1.4's text is left as changelog history; revision 1.5 states the
  current truth and supersedes it explicitly.
- No entry was admitted, re-scored, or re-reviewed; the index certifies
  row↔file correspondence only.

## 6. Limits

- **Live tree.** Other round-20 seats wrote during this run (observed:
  `reports/round-20/audit/`, `handoff/`, `integration/`, `report-draft.md`,
  `rerun.json`, `corpus/lessons/round-20.md`, and an edit to
  `tools/d2-typed-labels.py`). Counts and gate readings are point-in-time
  (13:02:57Z, HEAD `122086b` + working tree); a later write to
  `corpus/knowledge/` or `corpus/README.md` invalidates the sweep until it is
  re-run. README `sha256`: `fa1671218cb790f1ed22e0fa3a106004677a7b7bda559740f0e482a32b8db4fb`
  at the 13:02:57Z stamp (row repair + known-gaps corrections),
  `a20b6b263f089364dbfa236afdca58f160954d03d2ef9822c9540ef8ef584f7b` at the
  13:05:13Z close stamp after the §8 addendum, and
  `1a359d55387eef1aebd79316a7bf19d53a2ac6f0bcacb1cd109bdeff1294e7ce` at the
  13:07:53Z final stamp after the revision block named its counting command; all
  three sweeps exit 0, and the 13:07:53Z sweep is the binding one.
- The sweep proves correspondence and verbatim topic text, not entry quality,
  sources, non-duplication, or canon. "Verbatim" means the row equals the
  entry's own `- topic:` line — it does not certify that the topic is accurate.
- The `to-verify` marker inventory is `tools/source-audit-inventory.py`'s
  surface, not this one.
- Same-seat verification (`verify.md`) re-runs these measurements in a fresh
  process with controls; it is a re-measurement, not independent-seat review.

## 7. Files written

- `corpus/README.md` (revision 1.5 line; 10 rows repaired; 4 known-gaps dated
  corrections; 1 new round-20 bullet; tail re-measure line)
- `reports/round-20/readme/reconcile.md` (this file)
- `reports/round-20/readme/verify.md`
- scratch (disposable, untracked): `.scratch/r20-c-readme-sweep.py`,
  `.scratch/r20-c-repair-rows.py`, `.scratch/r20-c-rows.json`,
  `.scratch/r20-c-rows.diff`, `.scratch/r20-c-sweep.json`,
  `.scratch/r20-c-sweep-out.txt`, `.scratch/r20-c-battery.json`,
  `.scratch/r20-c-battery2.json`, `.scratch/r20-c-verify.py`

## 8. Addendum (13:05:13Z) — one merged frontier row from the sibling C05..C08 seat

`reports/round-20/readme/gaps.md` (seat R20-C05..C08, the C gap-refresh seat,
landed 13:04Z, after §4 of this file was written) surveyed the same frontier
against rounds 17–20 and reached the same statuses for F3 (filled), F5 (filled),
F6 (stale → closed as failed), F11 (battery superseded, D4 assembly selftest
open) — and added one defect this seat had not carried: the README's **round-5
and round-6 bullets instruct readers to reproduce their counts with the
round-local runners**, and those runners now exit 1 at HEAD (round 5: a
non-append corpus edit plus seven `gate_digest_mismatch` rows in the round-3
manifest replay; round 6: `historical file changed: .gitignore`; digests in
`gaps.md` §1.5). The claim is theirs and is cited as attributed evidence: this
seat did **not** re-execute those runners, because running them rewrites their
own filed `reports/round-{5,6,7}/validation.json` in place (the same hazard the
sibling measured and then restored with `git checkout --`), and filed round-8..19
artifacts are outside this seat's write scope.

Merged as a clause on the round-20 known-gaps bullet (`corpus/README.md:388-396`
at the close stamp): read those counts from the filed
`reports/round-{5,6}/parent-reconciliation.json` receipts, name the drift, do
not edit the old runners. The sibling's remaining merge-ready rows (header
readings A/B/C, the three-live-baseline-roots residue, the round-9 open-item
disposition) are left to the integrator: this seat's frontier bullet already
points at the header readings entry, names the three baseline roots, and defers
round-9 items to their filed draft, so merging the rest would duplicate rows
without adding a measurement.

Close re-measurement after the addendum (13:05:13Z): sweep exit 0 (199 rows vs
199 files; 0 missing, 0 topic mismatches, 0 ghosts, 0 header drift), selftest
10/10, V3a 10/10 rows byte-equal, V3b 10 mismatches on the reconstructed text
and 0 on the current one, counts 94/19/19/18/29/20 = 199. README `sha256`
`a20b6b263f089364dbfa236afdca58f160954d03d2ef9822c9540ef8ef584f7b`; diffstat
`1 file changed, 82 insertions(+), 14 deletions(-)`.

Final pass (13:07:53Z). The round's counting command
(`reports/round-20/run-validation.py`) landed from another seat ~13:06Z; run in
its no-write `--check` mode it returns **claim C: PASS, `failures: []`** — six
partition headers and rows vs live files clean, revision block
`commanded/dated/numbers_present` all true with no placeholder, and the declared
`linguistics 20` delta documented in the README — while D and O fail on their
own in-flight artifacts (missing v3 baselines, stale D4 pins, the foreign-tree
mirror), which are their seats' legs. Reading that verdict, this seat made the
revision block's counting command explicit
(`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`,
cross-checked with `ls corpus/knowledge/<partition>/*.md | wc -l`) rather than
leaning on the runner's loose `command` keyword match, then re-ran everything:
sweep exit 0, selftest 10/10, V3 10/10 and 10/0, runner C leg still PASS.
Final README `sha256`
`1a359d55387eef1aebd79316a7bf19d53a2ac6f0bcacb1cd109bdeff1294e7ce`; diffstat
`1 file changed, 85 insertions(+), 14 deletions(-)`.
