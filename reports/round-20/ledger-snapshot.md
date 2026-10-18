# R20-A15..A16 — drift-ledger snapshot for the loop-2 verify round (NON-CANON)

- seat: R20-A15..A16 (freshness auditors, audit-only x2). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  Assignment (verbatim): *"AUDIT R20-A15..A16 (freshness-audit-only x2): per the pause,
  NO axis-move — but record the current drift-ledger state for the loop-2 verify round;
  reports/round-20/ledger-snapshot.md"*.
- date: 2026-10-18 (lane-local UTC-03:00; all stamps below UTC).
- role limits: this seat audits and reports. Its only writes are this file and gitignored
  `.scratch/ledger-snapshot/`. It edits no ledger row, receipt, corpus entry, tool, pin or
  fixture; it admits no claim and disposes nothing. **No axis-move:** the freshness pause
  stands (`SCORECARD.md:201-205`, `LOG.md:3021-3029`, `reports/round-14/loop1-retrospective`
  context); nothing below is a stability claim — the counts are a state record for the
  verify round.
- reading window: live batch **13:01:10–13:01:34Z**, mirror batch **13:01:47–13:02:19Z**,
  full-capture pass **13:05:36–13:06:11Z**, clean-HEAD control **13:08:33Z**, window-late
  D2 recheck **13:10:39–13:10:41Z** (2026-10-18). HEAD `122086b` throughout; the worktree
  was **dirty and moving** (round-20 wave in flight — §3 F4/F2). Everything here binds to
  that window and those tree states.

## 1. The ledger and its filed state (as filed, not re-disposed)

| artifact | sha256 (first 16) | state |
|---|---|---|
| `reports/round-10/drift/ledger.json` | `9ae5ed2ee5599629` | 192 rows; verdicts as filed: 153 `current` / 29 `stale-documented` / 10 `stale-fixed` |
| `reports/round-11/recheck/row-000..191.json` | set digest now `c8c1c599ee9640e2` | 192 per-row recheck receipts |
| `reports/round-11/recheck/summary.json` | `f633b2ff9b54c73b` | `rows_reckecked 192, stable 147, unstable 45, stability 0.7656, undispositioned 0` |
| `reports/round-11/recheck/dispositions.md` | `de61aec0b38c60da` | 43 unstable rows dispositioned: 15 legitimate-change / 21 environmental / 7 defect; bound to receipts-set digest `86b55e921604b5a5` (22:14Z snapshot) |

Commands: `sha256sum` of the four artifacts + a sorted per-receipt `sha256` list, both
re-run 2026-10-18 13:03Z.

**The 147↔149 reconciliation (recorded here so the verify round does not re-derive it).**
`summary.json` (147/45) and the receipts agree row-for-row. `dispositions.md` says 149/43
because it was written against the 22:14Z receipt snapshot; the integrator afterwards
re-measured two receipts — **row 47** (capture-convention only: `sha256('94')` vs
`sha256('94\n')`, value identical) and **row 187** (ledger transcription defect; the
sha256sum leg reproduces its pin exactly). Both carry their disposition in their own
receipt (`integrator_note`, `drift_cause`); `dispositions.md` predates that repair. The
current receipts-set digest `c8c1c599…` ≠ the `86b55e92…` the prose bound to, confirming
the two repaired receipts are the delta. Net: **all 45 unstable rows carry a named cause**,
but the filed prose count is two short of the receipts.

## 2. Live re-measurement (this seat, 2026-10-18)

**Method.** All 192 ledger rows were attempted 1:1 from the receipt's command-as-run text;
176 rows re-ran — 162 read-only rows in the lane root, 14 write-capable rows
(`96, 102, 113, 114, 120, 129, 130, 131, 132, 147, 170–173` — validators and the
`--report` craft row) in a disposable full mirror (`.scratch/ledger-snapshot/iso-full`,
copied ~13:00Z). 16 rows are not 1:1 re-runnable and are carried (§2.4). Receipt pins were
matched across three capture conventions (stdout / stderr / stdout+stderr); a full-capture
pass (`.scratch/ledger-snapshot/full/`) resolved convention and inner-digest rows.
Instruments: `.scratch/ledger-snapshot/{rerun.py, fullcap.py, classify.py, out/, out-late/,
final-status.json}`. Commands: `python3 .scratch/ledger-snapshot/rerun.py <176 rows>` and
`python3 .scratch/ledger-snapshot/fullcap.py <67 rows>`; both 2026-10-18.

### 2.1 Headline (of the 176 rows re-run)

| outcome | count | rows |
|---|---:|---|
| byte-identical to the round-11 pin | **110** | (see `final-status.json`) |
| value-identical under the receipt's recorded convention | **15** | convention-only: `21, 48, 49, 50, 52, 53, 54, 55, 57, 58`; inner/artifact-digest: `17, 18, 19, 26, 41` |
| moved, cause named (§2.2) | **50** | `2, 4, 5, 16, 34, 39, 40, 51, 56, 60, 65, 66, 71, 79, 83, 90, 91, 98, 99, 100, 102, 103, 106, 111, 112, 114, 117, 120, 121, 122, 127, 128, 130, 132, 144, 149, 152, 153, 154, 161, 162, 170, 171, 172, 173, 174, 177, 178, 189, 190` |
| run in its intended form (deliberate) | **1** | `20` — the ledger's command field is a `<18 surfaces>` placeholder whose pin is a bash syntax error; the receipt's `intended_form` sweep re-ran green: `18 OK / 0 MISSING`, stdout `1184529d370af5dc…` = the receipt's own `intended_form.stdout_sha256` |

This is a state observation under the pause, **not** a stability ratio: the ≥95% contract
remains operator-uncalibrated and no option is selected here.

### 2.2 The 50 moved rows, by named cause

| cause | rows | basis |
|---|---|---|
| legitimate change, rounds 12–19 (committed) | `2, 4, 5, 34, 39, 40, 51, 56, 60, 71, 100, 102, 106, 112, 120, 122, 130, 144, 149, 161, 170, 172, 178` | `git log e3ef171..HEAD -- <paths>`: SKILL.md through `caf1bea`; corpus growth; round-7 runner totals; battery tool/selftest (rounds 14/19); gate glob gained the two D4 gates |
| legitimate change + environmental | `65, 66, 90, 98, 99, 103, 111, 121, 128, 152, 153, 162, 177, 189, 190` | battery rows: 9 gates + random tokens/seconds; inventory rows: corpus growth + absolute-root embedding |
| in-flight uncommitted edit (round-20) | `16` | `tools/d2-typed-labels.py` uncommitted; sha moved `0da0015f → fd70df51 (13:01Z) → 76536a92 (13:10Z)` during the window (§3 F2) |
| defect — a real current failure | `114, 132` | round-9 runner O leg now fails at HEAD (§3 F1) |
| environmental — path-dependent pin | `79, 83` | receipts document mirror-root-bound pins; lane-root output differs only in absolute paths |
| environmental — random temp path | `91, 127, 154` | inventory selftest embeds its `TMPDIR` dir |
| environmental — live-worktree snapshot | `117` | by construction; current output lists the in-flight dirty set |
| environmental — location-bound pin | `174` | substance reproduces (rows 7 / reproduced 0 / could_not_evaluate 7, exit 2); same command row 118 reproduces its lane-root pin `cbde6c5e` byte-exactly |
| context-bound pin | `171, 173` | current output equals a sibling row's pin on the same tree (`171`=`129`=`ef767ba7`; `173`=`113`=`131`=`9d0d40f1`); the r11 pins were clone-variant values |

### 2.3 The 45 round-11-unstable rows, current state

- **9 now reproduce their r11 pin byte-exactly:** `1, 12, 47, 113, 129, 163, 169, 175, 187`.
- **1 value-identical by convention:** `54`.
- **25 moved** (all with the causes above): `2, 4, 5, 39, 40, 51, 65, 66, 90, 98, 99, 102,
  103, 111, 120, 121, 128, 130, 152, 153, 162, 170, 177, 189, 190`.
- **3 environmental (temp path):** `91, 127, 154`. **1 snapshot:** `117`. **1 location-bound:**
  `174`.
- **5 not 1:1 re-runnable (carried):** `67, 68, 69` (prose controls), `185` (unrecoverable
  packet input), `188` (scratch-artifact digest).

### 2.4 The 16 rows not 1:1 re-runnable (carried, not re-disposed)

`31, 32, 33, 35, 36, 37` (raw-shorthand rows), `63` (input `.scratch/f09/export-r3` gone),
`67, 68, 69` (prose controls; scripts never filed), `101` (inputs `.scratch/r10f10` gone),
`182, 183, 184` (packet inputs gone; round-11 reproduced bytes via reconstruction — now
also shadowed by the in-flight D2 tool, §3 F2), `185` (unrecoverable input; three hashes,
none matching), `188` (scratch-artifact digest row). Row `28`'s probe was recreated from the
`reports/round-10/drift/shard-04.md` appendix and reproduced byte-exactly (`d84f3736…`).

## 3. Findings for the loop-2 verify round (reported, not fixed)

**F1 — the round-9 runner is red at HEAD; the round-11 green reading no longer holds.**
`python3 reports/round-9/run-validation.py` → exit 1, stdout `f55a6437…` (rows 114/132;
r11 measured exit 0, `4d300b24…`). The O leg names the cause:
`tools/gates/typed-pipeline-gate.py: no expected.json baseline found under
tools/gates/frozen, tools/gates/expected, reports/round-9/baselines`.
Controls: (a) a clean-HEAD copy (`iso-clean` = mirror + `git checkout -- .`) gives the
identical stdout `f55a6437…` and exit 1 — a HEAD-state property, not in-flight dirt;
(b) `find` + `git ls-tree` show no `expected.json` for that gate under the three roots at
any revision — the gate module itself entered at `a3f6fce` (round-11 close, 2026-10-17
19:34 local), *after* the recheck that measured the runner green. Consequence: the
SCORECARD.md:133-class claim (round-9 runner "exits 0") is stale on the delivered tree;
rows 114/132 of the ledger cannot reproduce. Routed to the verify round / scribe; no fix
attempted here.

**F2 — `tools/d2-typed-labels.py` is being edited in-flight; its selftest surface has
already moved.** The file is uncommitted (`git diff --stat`: 1 file changed, 299
insertions(+), 48 deletions(-); the diff is the round-20 era-alias shaping work). Three
revisions were observed in-window: `0da0015f…` (mirror copy ~13:00Z; the round-10/19 pin)
→ `fd70df51…` (row-16 read 13:01Z) → `76536a92…` (13:10Z). Effects measured under the
latest revision (13:10:39Z): `--selftest` stdout `5bb980a5…`, **50/50 checks** vs the pinned
`7231139c…` (39/39) — rows `14, 25, 27` reproduced the pin at 13:01Z but not at 13:10Z;
meanwhile the D2 assembly and CLI surfaces are still byte-identical: `assemble-d2.py
--check` `2fa0c8c1…`, CLI rows `180/181` `b232dffb…`/`880d0e45…`, naming gate over the
culture-d2 packet `ebc8850d…`. Rows 182–185 are carried and shadowed by this edit. Per the
lane's rule, any settled change must keep the D2 path byte-identical and update pins as
**NEW rows** — the verify round must re-pin at settle.

**F3 — the battery default run is now green (round-19 admitted change).** Rows
`65, 98, 103, 128, 162` exit 2 → 0; the row-65 capture summary reads `coverage 9/9`,
`baselines_found 18, pinned 18, gates_uncovered []`; battery selftest rows
`100, 106, 112, 122, 161` now read `35/35` (were `28/28`). Side effect: the round-5
runner's embedded volatile battery JSON is gone from its O error, and rows `102, 120, 170`
now produce byte-identical output across three runs (`c8dc79ec…`) — their r11 pins were
context-bound.

**F4 — in-flight receipt edits observed in the lane (the receipt-clobber family).** At the
window, `git status` read `M reports/round-5/validation.json` (mtime 13:00:55Z),
`M reports/round-7/validation.json` (13:00:58Z), `M reports/round-9/validation.json`
(13:01:01Z) — before this seat's first command (13:01:10Z), so not written by it; this
seat's write-capable rows ran in the mirror by construction. Also live: `M corpus/README.md`
(C work), `M tools/d2-typed-labels.py` (O work), `M examples/culture-d4/*` +
`M tools/assemble-d4-typed.py` + `M tools/exercise-handoff-e2e.py` +
`M tools/gates/typed-pipelines.json` (D/O work), plus untracked `reports/round-20/*`
artifacts. The verify round should take a before/after receipt snapshot around any
validator re-run (`tools/harness/receipt_guard.py`).

**F5 — carried open items, unchanged from round 11 (no re-disposition here).** Row
113/`fix-20` delivery gap; rows `1, 12` ledger transcription defects; rows `67–69` prose
rows and row `188` artifact-digest row; the 21-row environmental family; rows `182–185`
reconstructed/unrecoverable inputs; the ≥95% measurement-contract recalibration remains
operator-pending (pause in force).

**F6 — live-count note (context only, not a claim).** At the window the corpus read
civilizations 94, linguistics 19, myth-symbol 19, culture-material 18, synthesis 29,
verification 20 (199 files; commands: row 39/48's own counts 13:01:34Z + a direct recount
13:09Z). `reports/round-20/claims.json` claim C declares *linguistics 20*; the live tree
read 19 throughout this seat's window (C work in flight, `corpus/README.md` modified). For
the verify round to check at settle.

## 4. Limits

- No freshness axis-move and no stability claim: the counts above are a state record bound
  to the reading window; the 0.95 contract stays paused and uncalibrated by operator
  decision. Nothing here admits, rejects or repairs anything.
- The tree moved during and after the window (F2/F4; further `M`/untracked entries appeared
  by 13:13Z). Re-measurement at settle belongs to the loop-2 verify round; this snapshot
  tells it what to expect and where the pins live.
- Structural/byte-level checks only: reproductions, conventions, digests, exit codes and
  named causes — not passage-level source support or claim soundness.

## 5. Instruments and controls (evidence)

- `python3 .scratch/ledger-snapshot/rerun.py <rows>` — per-row receipts in
  `.scratch/ledger-snapshot/out/row-NNN.json` (cmd, cwd kind, exit, three stream hashes,
  match sets, window stamps).
- `python3 .scratch/ledger-snapshot/fullcap.py <rows>` — full stdout/stderr captures in
  `.scratch/ledger-snapshot/full/` (convention + inner-digest checks; row `20`'s
  intended-form, row `28`'s recreated probe, rows `174/175`'s corrected command text).
- `python3 .scratch/ledger-snapshot/classify.py` + `final-status.json` — the per-row final
  status behind §2.1–2.3.
- Window-late D2 recheck: `.scratch/ledger-snapshot/out-late/row-{14,16,25,27,92,180,181,186}.json`
  (13:10:39–13:10:41Z).
- Non-interference: every write-capable row ran in `.scratch/ledger-snapshot/iso-full`;
  all other rows are read-only command classes; `TMPDIR` under `.scratch`;
  `PYTHONDONTWRITEBYTECODE=1`; the pre/post live-batch `git status` capture is in
  `.scratch/ledger-snapshot/tree-state.log` (PRE 13:01:10Z dirty=9, POST 13:01:35Z
  dirty=10 — the added entry is a concurrent round-20 artifact, not this seat's).
- Determinism controls: rows `102/120/170` byte-identical across three runs; rows
  `130/172` byte-identical; the D2 selftest run twice at 13:10Z byte-identical; the
  clean-HEAD round-9 control identical to the mirror run.
