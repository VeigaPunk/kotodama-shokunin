# Round 10 — coverage expansion, drift sweep, findings closure (2026-10-17)

source: reports/round-10/claims.json; reports/round-10/targets.json; reports/round-10/** worker fragments (indexed below); reports/round-10/validation.json (freshest acceptance receipt, 21:44:36 UTC); reports/round-9/validation.json (prior-round admit receipt, re-run 21:26:58 UTC); reports/round-10/drift/ledger.json (191 rows at 21:49 UTC)
verified-at: 2026-10-17 (gate-keeper survey window 21:26:51–21:49:33 UTC; acceptance receipt 21:44:36 UTC on a tree that took two more coverage writes after it; admission and spot-check pending)
recheck: `python3 reports/round-10/run-validation.py` (declared counting command for C/F/O, authored by scribe X03); re-list fragments with `find reports/round-10 -type f | sort`

Gate-keeper skeleton (scribe X01), opened before the round-10 fragments
landed and closed after a ~23-minute fragment survey. It indexes the
fragments that landed and records the declared gate candidates with bounded
reasons. Nothing is admitted on declaration alone: the admitted/rejected rows
below cite the fragment and acceptance evidence actually read during the
survey window, and every admission stays marked spot-check pending until the
parent's acceptance run on the settled tree and an independent re-run land.

## Fragment index

Survey commands (2026-10-17 UTC): `find reports/round-10 -type f | wc -l`
plus `sort`; a background poller sampled the tree every 30 s for 42 ticks,
21:27:22–21:47:52 UTC, logging to `.scratch/r10-poll.log` (in-lane scratch,
untracked; tick stamps UTC, file mtimes local UTC-03:00). The poller recorded
**68 NEW rows against 68 net new files** (73 at close − 5 at open), i.e. its
first-seen detection was complete this round — unlike round 9, where the same
poller under-sampled. `/tmp` was re-confirmed inode-exhausted at survey open:
`df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`; `df -h /tmp` → 8.5G
available (the by-volume view disagrees, the round-9 finding restated).
Scratch stayed in-lane (`.scratch/`, `export TMPDIR=$PWD/.scratch`).

- 21:26:51 UTC (survey open): **5 files** — `claims.json`, `targets.json`,
  three availability attempts (1–3, all HTTP 402 insufficient funds, 0
  launched / 0 completed). Zero worker fragments at that moment.
- 21:47:52 UTC (last poll tick): **73 files** — coverage 26, drift 24,
  top-level 23. No write landed between 21:47:52 and the close reading
  21:49:33 UTC (`find -newermt '2026-10-17 21:47:52'` → empty), so the close
  list is stable within a ~100 s window, not a settled tree.
- The first worker fragment was a **reviewer**, not an author:
  `coverage/review-C08.md` at 21:28:21 UTC, opened before any C author
  fragment existed and carrying a pre-landing method section plus the
  179-entry baseline (its own count).

| fragment surface | shard range | claim | state at close |
|---|---|---|---|
| `coverage/` — authors `C01.md`–`C10.md` (10), reviewers `review-C01.md`–`review-C10.md` (10), auditors `audit-unchanged.md`, `audit-ling-verif.md`, `audit-filler.md`, `audit-myth-culture.md` (4), index updaters `index-update.md`, `index-update-22.md` (2) — 26 files | R10-C01..C26 | C | landed, all ten author + ten review + four audit fragments present |
| `drift/` — shards `shard-01.md`–`shard-14.md` (14: 01–14, none missing), `ledger.json`, `audit.md`, stale-fixers `fix-16.md`–`fix-23.md` (8) — 24 files | R10-F01..F19 | F | landed |
| top-level — findings fixers `fix-02.md`–`fix-09.md` (8), verifiers `findings-verify-1.md`–`findings-verify-4.md` (4), `findings-tracker.json`, `findings-scribe.md`, `adjacency.md`, `report-draft.md`, `run-validation.py`, `validation.json`, `claims.json`, `targets.json`, `availability-attempt-1..3.json` — 23 files | R10-O01..O14, X02/X03/X04 | O + acceptance | landed |

First-seen rows (UTC; poller tick in parentheses): `coverage/review-C08.md`
21:28:21 (t3) · `findings-tracker.json` 21:28:43 (t4) · first drift shard
`shard-07.md` 21:29:20 (t5) · first audit `audit-unchanged.md` 21:29:25 (t6) ·
`drift/shard-01.md` 21:30:33 and `run-validation.py` 21:30:42, first
`validation.json` 21:30:44 (t8) · `adjacency.md` 21:31:30 (t10) · `C08.md`
21:32:56 and `drift/ledger.json` 21:32:57 (t13) · `report-draft.md` 21:35:20
(t17) · first `fix-0N.md` (O fixer) 21:33:16 (t13) · first drift stale-fixer
`fix-16.md` 21:36:08 (t19) · `findings-scribe.md` 21:43:50 (t34) ·
`index-update-22.md` 21:44:22 (t36) · `audit-filler.md` 21:46:11 (t39) ·
`audit-myth-culture.md` 21:47:38 (t42, last landing).

Key mtimes at close (UTC): `run-validation.py` 21:37:16 ·
`drift/ledger.json` 21:40:09 · `drift/audit.md` 21:40:14 · `report-draft.md`
21:39:17 · `findings-tracker.json` 21:42:05 · `findings-scribe.md` 21:44:18 ·
`validation.json` 21:44:36. Working tree at close: 31 untracked + 4 modified
paths (`git status --porcelain`); the modified tracked files are `SKILL.md`
(drift stale-fix: line-number citations corrected, e.g.
`costume-language-coupling-table.md:40` → `:43`), `corpus/README.md` (index
updater), `reports/round-8/run-validation.py` (a `gate_blob_for_pin` helper
added by a drift fixer), and `reports/round-9/validation.json` (see below).

Round-9 continuity, observed: the round-9 admit commit `9dc18ec` (17:00 -03:00
= 21:17:00 UTC) is round-10's declared `baseline_revision`, and it carried the
D3 pin refresh (`examples/culture-d3/expected.json`, 66 lines) that turned
round 9's D leg green. During this survey window the prior-round receipt was
re-run: `reports/round-9/validation.json` mtime 21:26:58 UTC (7 s after survey
open), now **dirty vs HEAD** (4 insertions / 14 deletions), its two battery
`stdout_sha256` values changed (`25906f6f…` → `a4f97f86…`, `201e6eec…` →
`787a13d3…`) and its embedded `git_status` block removed — consistent with the
gate baselines becoming tracked at the admit commit. It reads all-green. This
is a prior-round artifact re-run on a changed tree, not round-10 evidence.

Fragment presence is not acceptance: a landed file is an input to
`run-validation.py`, not a verdict, and the tree took two coverage writes
(`audit-filler.md` 21:46:11, `audit-myth-culture.md` 21:47:38) **after** the
freshest receipt (21:44:36).

## Gate

Candidates are the three claims declared before dispatch in
`reports/round-10/claims.json` (operator regimen: loop 1 of 3, build round
3 of 4; requested model `opencode-go/deepseek-v4.1-flash` after attempts 1–3
hit 402 on keys 3–5; 64 workers). Each candidate below quotes its declared
`after_required` threshold; no scalar rubric is invented. This round's axes
are C/F/O — coverage replaces the D axis of rounds 8–9.

- **C / coverage**. ">=10 new sourced knowledge entries across the thin
  partitions (linguistics >=2, myth-symbol >=2, culture-material >=2,
  verification >=2), each with complete source/verified-at/recheck
  frontmatter, at least one decision-record section, and grounding in
  retrievable sources (round-8/9 receipts and existing corpus cross-references
  count as sources when cited by path); NO filler — a new entry must name the
  gap it fills; corpus/README.md index rows match actual files (sweep command
  count matches)." Counting command:
  `python3 reports/round-10/run-validation.py`. Before-state verified at
  survey open: `for d in corpus/knowledge/*/; do find "$d" -name '*.md' | wc
  -l; done` → civilizations 94, culture-material 16, linguistics 16,
  myth-symbol 16, synthesis 24, verification 13 = **179** total, matching the
  declared before-state.
- **F / freshness** (declared lowest axis). "A drift ledger
  (reports/round-10/drift/) records every command cited in SKILL.md re-run
  with its observed output hash + verdict (current|stale-fixed|
  stale-documented); every SCORECARD counting command re-run; gate registry
  rows matched against live gate files; stale items are either fixed in this
  round (with evidence) or documented with a reason; zero silent staleness."
  Counting command: `python3 reports/round-10/run-validation.py`. Surfaces at
  open: `SKILL.md` (291 lines, byte-identical since round-8 per shard-01),
  `SCORECARD.md`, `reports/round-9/baselines/registry.md` (7 structural gates
  live under `tools/gates/*.py`).
- **O / operability**. "Every finding in the four files dispositioned in a
  tracker (reports/round-10/findings-tracker.json): fixed-with-control
  (control demonstrated) or documented wont-fix/wrong-with-reason; zero
  findings left without a disposition; no previously green check regresses."
  Counting command: `python3 reports/round-10/run-validation.py`. Sources at
  open (hashes of the four files, sha256 prefixes): `reports/round-8/depth/
  findings.md` `01c27fde75fd65ee` (156 lines), `reports/round-8/depth/
  findings-17.md` `8f6eabadf92ca218` (238), `reports/round-9/d3/findings.md`
  `27ba8c2f0694ad6c` (133), `reports/round-9/d3/findings-10.md`
  `19376989f22d37cf` (236). The tracker compiled at 21:27Z carries 24 rows
  (13 + 3 + 6 + 2 per file).

### Survey verdict at close (2026-10-17 21:49:33 UTC; receipt 21:44:36 UTC)

Freshest filed acceptance receipt: `reports/round-10/validation.json`, mtime
21:44:36 UTC, sha256 prefix `51d661e71d2ec5ee…`; runner `reports/round-10/
run-validation.py` (mtime 21:37:16, sha256 prefix `23d6dc09002fe18c`);
`missing_dependencies: []` (down from four at the first run);
`acceptance_checks_passed: false`.

- C: `passed: false`, 4 failures — `culture-material/
  transport-mobility-lexicon.md: no named gap (filler risk)`;
  `myth-symbol/plant-symbolism.md: no named gap (filler risk)`;
  `myth-symbol/plant-symbolism.md: no retrievable locator (existing repo path
  or URL)`; `coverage: 2 audit fragments < required 4`. Entry counts measured
  by the survey: `git status --porcelain corpus/knowledge` → 10 new untracked
  entries (linguistics 3: `language-shift-obsolescence-revival`,
  `numerals-and-measures`, `sound-symbolism`; myth-symbol 3:
  `direction-symbolism`, `divination-omen-systems`, `plant-symbolism`;
  culture-material 2: `transport-mobility-lexicon`,
  `vessel-container-lexicon`; verification 2:
  `header-conformance-readings`, `verification-independence-anti-circularity`),
  partition counts now 19/19/18/15 = **189** total (179 + 10) — the >=10 and
  per-partition >=2 shape is present on disk; the receipt's entry-level checks
  are what is red. The audit-count failure predates two audits that landed
  after the receipt (21:46:11, 21:47:38; `ls coverage/audit-*.md | wc -l` →
  4 at close).
- F: `passed: false`, 22 failures — 11 × `ledger row N: output_sha256
  missing/not 64-hex` (rows 20, 29–35, 56, 59, 60), 10 × `ledger row N:
  stale-fixed without demonstrated fix evidence` (rows 42, 61, 62, 67, 68, 69,
  98, 113, 131, 176), and `ledger covers 35/36 cited commands; 1 missing`.
  The ledger at close has 191 rows, verdicts {current 152, stale-documented
  29, stale-fixed 10} (measured 21:49:33); the survey's own sweep of the
  ledger's `output_sha256` column finds **14** rows non-64-hex (0-based 20,
  29–37, 56, 59, 60, 183), i.e. the receipt's snapshot (which read an earlier
  150–189-row ledger; `drift/audit.md` records it moving 122 → 146 → 150 →
  189) saw 11 of the 14.
- O: `passed: true`, 0 failures. The tracker's final state (findings-scribe,
  21:44:18): 24 rows, dispositions **18 fixed-with-control, 4 wont-fix, 1
  wont-fix (superseded), 1 wrong**, `undispositioned_rows: []`, 4/4 verifier
  verdict files present; the scribe re-ran the previously green checks and
  reports no regression (battery selftest).
- Overall `acceptance_checks_passed: false`.

**Admitted at this survey close: none yet.** Reasons: (1) the round verdict
is false while C and F are red; (2) the receipt is a snapshot of a tree that
was still being written — two coverage audits landed 1.5 and 3 minutes after
it, and the ledger itself was a moving target during its own audit; (3) no
independent re-run receipt has landed — no `rerun.json` exists under
`reports/round-10/` (`find` → empty; round-8 has one, round-9 never did).
O currently reads green in the receipt; that is recorded as observed evidence,
not admitted, because admission requires the parent's acceptance on the
settled tree plus the independent re-run.

Rejected at this survey close (each names the observed evidence):

- **Counting the first receipt (21:30:44 UTC) as the verdict**: it failed C on
  14 legs (`2 new entries < required 10`, all four partitions at 0 new,
  missing index/audit fragments), F on 9/13 shards plus absent ledger and
  audit, and O on `24 tracker row(s) still pending` and 0 verifier files.
  Those conditions moved within 14 minutes. Receipts must be judged on the
  settled tree, not at first landing.
- **Counting fragment presence (10 authors + 10 reviews + 4 audits + 2 index
  updates) as C acceptance** — the receipt's entry-level checks are the gate,
  and two of the ten entries fail them.
- **Reading `plant-symbolism.md`'s `gap=False`/`locators=0` as plain proof of
  filler**: the file visibly carries a gap clause (topic line: "the gap this
  entry fills"; §1: "**The gap statement.**") and URL/path sources, while the
  runner's `entry_checks` returns `gap=False, locators=0` (runner lines
  435–442). `review-C08.md` independently surfaced the same two failures as an
  out-of-seat observation and routed them to the parent and C16's review. The
  receipt's red C stands as the verdict; the checker-vs-file discrepancy is
  flagged, not adjudicated here. By contrast the same check on
  `transport-mobility-lexicon.md` matches the visible bytes: `grep -inE 'gap'
  <file>` → empty output, exit 1 (sweep run 2026-10-17 21:49 UTC).
- **Treating `review-C08.md`'s observations as filed corrections**: its N2
  (aspirational `couples` pointer `civilizations/maya-classic.md (sacbeob)`,
  file resolves but has no matching content), N3 (imprecise Manguin locator),
  and the mislinked Merriam-Webster URL (link text "coach", target
  `/dictionary/coachable`) are recommendations by an author-side seat; only
  the last is a filed defect against an entry's bytes, and none is an edit.
- **Counting the ledger's row count as "every command cited in SKILL.md
  re-run"**: the ledger's own coverage leg is 35/36 with 1 command missing
  (receipt row), 14 rows carry non-64-hex `output_sha256`, and 10
  `stale-fixed` rows lack demonstrated fix evidence at the receipt's reading.
  The declared threshold is "zero silent staleness"; the receipt measures it
  red, and a moving ledger cannot be blessed by citing its largest snapshot.
- **Counting `stale-documented` as fixed**: 29 rows carry that verdict; the
  threshold requires a reason per row, and the receipt does not fail them at
  this reading — that is a pass on the leg as measured, not a claim that the
  underlying citations were re-fetched.
- **Counting O green as round acceptance**: O's regression guard (battery
  selftest) is the scribe's re-run claim inside its own fragment, and
  admission still requires the parent's run plus the independent re-run.
- **Promoting the three availability attempts to completed-round credit**:
  attempts 1–3 recorded 0 launched / 0 completed each (HTTP 402); the
  SCORECARD round-5 routing-history precedent treats such attempts as
  historical, not current blockers and not work.
- **Treating the round-9 receipt re-run (21:26:58 UTC, dirty vs HEAD) as
  round-10 evidence** — it is a prior-round artifact re-executed on a changed
  tree; its all-green reading belongs to round 9's admission, which already
  happened at `9dc18ec`.
- **Reading the 73-file close count as a settled tree**: writes stopped
  21:47:52 UTC by observation, the freshest receipt predates two of the
  coverage audits, and the round's own runner (X03's) was itself rewritten at
  21:37:16, after the first receipt it produced.

Spot-check status: **pending**. No parent acceptance on a settled tree, no
independent re-run receipt, and no parent source re-fetch receipt for the
round-10 C entries or F ledger rows has landed in this window. Historical
receipts and frozen evidence must not be rewritten; `reports/round-8/`,
`reports/round-9/` filed artifacts are read-only apart from the observed
in-flight edits named above, and the C-leg repairs (gap clause, locator,
ledger row hashes) belong to the round's own seats and the parent. The
round's own counting command and the drift ledger remain the authoritative
evidence once the tree settles; this lesson records the gate-keeper's bounded
survey only.
