# OReceiptFresh — claim O receipt semantics and freeze chain (round 64, wave 2)

Seat: `kotodama-r64.OReceiptFresh` (reviewer; judged axes coverage/operability/calibration).
Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Scratch
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/OReceiptFresh/`. No lane edit, no commit, no index/jj
mutation, no subagent dispatch, no tool install (pacman guard respected: no pacman transaction).

Observation window: 2026-10-23T23:44–2026-10-24T00:11 -03:00 (includes a 255 s `--only MUT` run and
the post-receipt amendment). Every hash below was taken at the stated time; the counter was edited
concurrently, so revision attribution is explicit.

## Verdict

1. **`final-measures-o-rev4.txt` arrived at 00:08 and is honestly RED.** It is internally
   consistent — 23 legs in `claims.json` order, 22 PASS + `MUT FAIL`, `ACCEPT-O-64: FAIL`, `exit=1`,
   counter sha `6d9c9354…` (the bytes it ran, hash re-checked before/after), tool sha `c0f10a84…` —
   and its header says "pre-data falsification evidence, NOT an acceptance receipt". My independent
   `--only MUT` run produced the same `m5:EDGE_SCHEMEREL isolation=…` failure. **It is not an
   acceptance receipt and must not be cited as one.**
   The counter was then amended at 00:08:52 (`760ddd4d…`): the m5 mutation is restructured and now
   compiles (`f04dc002…`; verified SCHEMEREL PASS / SLASHLESS FAIL) and the docstring inversion is
   corrected — **but the docstring still says "revision 4", so two different byte sequences now
   share one revision label.** A new full capture on `760ddd4d` is the owed acceptance receipt, and
   the revision stamp must be bumped or the sha↔revision mapping recorded.
2. The on-disk `final-measures-o.txt` is a **complete, internally consistent rev3 receipt** and
   passes every structural check in this assignment — but it binds revision 3 (`c27a9fef…`), which is
   no longer the counter on disk (`760ddd4d…`). It **must not be cited as the rev4 receipt**.
3. The round-63 **freeze chain verifies clean**: all four frozen entries match both the worktree and
   the base `ff30a205` blobs; the freeze record itself is byte-identical to its base blob.
4. The rev4 edits are on disk. The unknown-selector fix was verified directly (exit 2, stable
   bytes), but **the m5 mutant is syntactically invalid as landed** (`IndentationError`, mutant
   sha256 `795b8d19…`, independently reproduced) → `MUT FAIL` → **`ACCEPT-O-64: FAIL`, exit 1**
   observed on the landed bytes. A four-space dedent makes the mutant compile and restores the
   intended kill (validated in scratch). No attack seat had examined the rev4 bytes before this.

## 1. rev4 receipt at first check — absent (HIGH-1; since resolved, §1a)

```
$ date -Is
2026-10-23T23:56:42-03:00
$ ls reports/round-64/telemetry/ | grep -i rev4
(no output)
$ sha256sum reports/round-64/accept-o.py
6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1  reports/round-64/accept-o.py
```

Attribution of the gap (both seats acted honestly; the wave schedule did not overlap them):

- `.ufo/waves/round-64/w2/RevVerifyO2.md` (mtime 23:55): verdict states the revised counter "does
  not exist on disk", reports rev3 `c27a9fef…`, and **leaves a literal `RESULTS_PLACEHOLDER`** in
  §4. It declined to write the receipt rather than mislabel rev3 as rev4 — correct.
- `.ufo/waves/round-64/w2/RevCounters.md` (mtime 23:55): rev4 landed; by its own words "no post-edit
  PASS/FAIL is claimed" and "the requested post-edit m5 paired output and unknown-selector exit-2
  output remain unobserved".
- RevVerifyO2's scratch `full-run-rev4.txt` is **397 B, seven legs (TOOL…PRIV), no verdict, no
  `exit=`**, captured 23:51 — i.e. a partial run against **rev3** bytes under a "rev4" filename.
  It must never be promoted to `telemetry/`. (Same truncated shape as `dry-run-o.txt`, §5 LOW-1.)
- An `--only GEN,MUT,BOUND,EDGE_SCHEMEREL,EDGE_SLASHLESS,DRIP` process (pid 158918) was live at
  23:55 — the parent's quick check, not a full run.

**Required for closure (as of this first check; superseded by §1a):** first fix the m5 indent (§4)
and re-land; then a full frozen-command run
(`python3 -B reports/round-64/accept-o.py --root .`) on the final bytes, captured complete to
`final-measures-o-rev4.txt`, with the header fields of §3 and the m5 paired evidence of §4. A red
capture on `6d9c9354` is **not** acceptance evidence and must not be installed as one. The full run
exceeds 300 s (MUT alone was 255 s; DEFAULT is 150 s); it must be launched detached and captured in
full.

## 1a. Receipt arrival (00:08) and post-receipt amendment (00:08:52)

**The installed rev4 receipt, verified.** `reports/round-64/telemetry/final-measures-o-rev4.txt`,
4 196 B, sha256 `fed0ded28f1dc5a3ff3dd62c739cf3e17bf8593a902474a9302b6b0131158da3`.

| assignment check | result |
|---|---|
| header fields present (measured revision, parent, jj `@`, base, date, counter sha, tool sha, command) | **yes** — plus an explicit `RESULT: FAIL … NOT an acceptance receipt` line |
| counter sha matches on-disk `accept-o.py` | **yes at run time**: `6d9c9354…`, "unchanged before and after the run"; on-disk since 00:08:52 is `760ddd4d…` (post-receipt amendment, below) |
| tool sha matches on-disk and `ff30a205` blob | **yes**: `c0f10a84…` in all three |
| all 23 legs PASS | **no — 22 PASS, 1 FAIL** |
| exit=0 | **no — `ACCEPT-O-64: FAIL`, `exit=1`** |

Parsed independently: 23 leg lines, names in `claims.json` order, 22 `PASS`, 1 `FAIL` (`MUT`, with
`bad=["m5:EDGE_SCHEMEREL isolation=['EDGE_SCHEMEREL FAIL rows=[] tgt_hits=0 src_hits=0 tb=False']"]`),
verdict line `ACCEPT-O-64: FAIL`, trailer `exit=1`, run window 02:59:50Z–03:06:56Z (426 s), header
date `03:07Z`. The receipt does **not** overclaim an acceptance; it is valid falsification evidence.

Header improvement over rev3: it names `097c21d0` (the lane git HEAD from `jj-lane.sh state`) as the
measured revision and reports jj `@` `8325191b…` separately at run start, rather than implying the
worktree is recoverable. Residual: `8325191b`'s tree still contains neither the counter nor the
receipt (`git cat-file -e` → fatal), so the instrument remains bound by its sha line only.

**Post-receipt amendment.** At 00:08:52, after the red run had ended and been hash-checked, the
counter changed to `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7`:

- m5 replacement restructured (`slashless_relative = (…)` at the correct 8/12-space indent); rebuilt
  mutant sha256 `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710`, **compiles**;
  paired run: `EDGE_SCHEMEREL PASS`, `EDGE_SLASHLESS FAIL`, exit 1. Unpatched-tool control: both PASS,
  exit 0.
- Docstring inversion fixed: now "requires the former to PASS and the latter to FAIL"
  (`accept-o.py:117-119`), matching the code.
- **Defect: the docstring still says "revision 4".** `6d9c9354` and `760ddd4d` are both labelled
  revision 4 while differing by the m5 block and one docstring sentence. The installed receipt names
  revision 4 / `6d9c9354`; a reader comparing it to the on-disk revision-4 file gets a silent
  mismatch. Per the wave rule ("every counter change is a stamped pre-data revision"), the amendment
  needs a stamp bump (revision 5) or an explicit amendment line recording both shas.

**Owed acceptance evidence:** a full frozen-command run on `760ddd4d` captured complete to a receipt
whose counter sha is `760ddd4d…` (the existing `final-measures-o-rev4.txt` should be retained as the
falsification capture or renamed, not overwritten, so the falsification record survives). Expected
result if the m5 fix is the only behavioural change: 23/23 PASS, `ACCEPT-O-64: PASS`, exit 0 — but
only a full run can certify it; MUT alone is 255 s and the predicate is ~426 s.

## 2. rev3 receipt — complete and green for rev3 (verified)

`reports/round-64/telemetry/final-measures-o.txt`, 3 847 B, sha256 `009bbde3c7720a496b26f224646a5d99e6e55f247d22b9d9c38da93ccad84193`, mtime 23:38.

Programmatic parse (not eyeballed):

```
leg lines: 23   unique: 23   all PASS: True
names == claims.json O.legs order: True   missing: []   extra: []
verdict: ['ACCEPT-O-64: PASS']
exit lines: ['exit=0']        last line: exit=0
header: measured revision b7d22703dfb684713826a4064e614264867e8cd
        (jj working copy @, parent 097c21d0…; lane base ff30a205…), 2026-10-24T02:37Z
        counters: accept-o.py (revision 3, working-copy bytes) sha256 c27a9fef…
        tool: c0f10a84… (identical to ff30a205 blob and round-63 freeze record: yes)
        command: python3 -B reports/round-64/accept-o.py --root .   (launched detached; captured in full)
MUT: bad=[] mutants=10; kill_evidence names m1,m2,m3,m5,m6,m7,m8,m9,m10,mread,
     each with its pinned leg
```

Cross-checks:

- counter sha line `c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18` == the rev3 file
  I read at 23:44 (docstring "revision 3", 59 313 B, mtime 20:09:33). **Match.**
- tool sha `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0` ==
  `sha256sum tools/reopen-row.py` == `git show ff30a205:tools/reopen-row.py | sha256sum`. **Match.**
- Header clock 02:37Z vs file mtime 23:38 -03:00 (= 02:38Z). Consistent.

Status: **valid rev3 evidence; superseded on disk.** Because the counter is now rev4, any citation of
this receipt for "the current counter" is a revision mismatch by construction.

## 3. Measured-revision binding — the header overclaims recoverability (HIGH-2)

The header names `b7d22703…` as the measured revision. That commit object exists and its parent is
`097c21d0…` (verified: `git log -1` shows parent `097c21d0eba5023cfd38b767fb41d59409eef125`), and it
is the same jj change as current `@` (`change_id tqmlmnlqwsuy`, verified with
`jj --ignore-working-copy log`). But:

- **Its tree contains neither the counter nor the receipt.**
  `git cat-file -e b7d22703:reports/round-64/accept-o.py` and
  `…:reports/round-64/telemetry/final-measures-o.txt` both fail ("exists on disk, but not in
  'b7d22703'"). `jj-lane.sh` sets `snapshot.auto-track="none()"`, so untracked files are never in a
  snapshot; `accept-o.py`, all O telemetry, and `mutants/` are untracked (`??` in
  `git status --porcelain -- reports/round-64/`).
- **Neither counter sha exists as a git object:** `git cat-file -e` fails for both
  `c27a9fef…` and `6d9c9354…`. The bytes are anchored by hash only.
- **`@` is volatile:** while I observed, the same jj change's commit id moved from `b7d22703`
  (RevVerifyO2's read, 23:51) to `5a9ff972` (mine, 23:53) and onward, because tracked files
  (`LOG.md`, `SCORECARD.md`, `accept-c.py`, `accept-ca.py`) are edited continuously by siblings.

Consequence: "worktree otherwise as measured" is **not recoverable** from the named revision; only
the literal counter sha line binds the instrument. For rev4 the L1 should either (a) track and commit
`accept-o.py` + the receipt + `mutants/` in the same VCS commit and name that landed commit, or
(b) reword the header to say the instrument bytes are untracked and bound by sha only. Do not repeat
the current wording, which implies a recoverable worktree.

## 4. rev4 edits — landed; m5 mutant is broken (BLOCKER)

Landed at sha `6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1` (docstring
"revision 4 (pre-data)"; history block at `accept-o.py:117-124` names the two forcing controls
`.ufo/waves/round-64/w1/CriticO.md` and `.ufo/waves/round-64/w1/ReviewerCounterO2.md`).

**Verified here (direct execution, read-only, hash stable pre/post):**

```
$ python3 -B reports/round-64/accept-o.py --root . --only NOSUCHLEG
ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG
exit=2
```
This closes ReviewerCounterO2 H1 (rev3 silently printed `ACCEPT-O-64: PASS`, exit 0 — reproduced in
control-o.txt and inherited receipts). `accept-o.py:446-448` validates the selector set before
fixture work. The mixed-selector hazard is closed by the same set test.

**BLOCKER — the m5 mutant does not compile; MUT FAILs on the landed bytes.** The m5 replacement is
inserted at `tools/reopen-row.py:604`, where the base indent is 8 spaces, but the replacement's
continuation lines carry 12 spaces (`accept-o.py:1054-1057`). Rebuilding the mutant exactly
(`MUTANTS` extracted with `ast.literal_eval`, single `str.replace`) gives sha256
`795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb` (identical to RevVerifyO2's
independent rebuild) and:

```
$ python3 -m py_compile m5.py
Sorry: IndentationError: unexpected indent (m5.py, line 605)
```

The counter's own MUT leg on the landed bytes (hash `6d9c9354…` stable pre/post, 255 s wall — which
is also why the full predicate exceeds the 300 s tool budget and why RevVerifyO2's first capture was
cut at seven legs):

```
$ python3 -B reports/round-64/accept-o.py --root . --only MUT
MUT FAIL bad=["m5:EDGE_SCHEMEREL isolation=['EDGE_SCHEMEREL FAIL rows=[] tgt_hits=0 src_hits=0 tb=False']"] mutants=10 kill_evidence=[… 'm5->EDGE_SCHEMEREL FAIL rows=[] tgt_hits=0 src_hits=0 tb=False; EDGE_SLASHLESS FAIL rows=[] dir_hits=0 root_hits=0 exit=1' …]
ACCEPT-O-64: FAIL
exit=1
```

`pinned_fail` is satisfied (the EDGE_SLASHLESS FAIL line is present), but the rev4 isolation check
(`accept-o.py:1115-1121`) requires EDGE_SCHEMEREL PASS, so `mut_bad` is non-empty → MUT FAIL → the
frozen predicate FAILs. **A full 23-leg rev4 capture on `6d9c9354` will be red; it must not be
installed as an acceptance receipt.**

**Docstring inverted (calibration).** `accept-o.py:117-119` says the paired run "requires the former
to FAIL and the latter to PASS" — former = EDGE_SCHEMEREL, latter = EDGE_SLASHLESS — but the code
and the intent require the opposite (SCHEMEREL PASS, SLASHLESS FAIL). RevCounters' report prose is
correct; only the on-disk docstring is inverted.

**Validated minimal fix (scratch only; no lane edit).** Dedent the replacement's
`if`/`and`/`target`/`else`/`target` block by four spaces (site 8, body 12) — the same fix proposed by
RevVerifyO2. Rebuilt mutant sha256 `804c9473d752833e143971b734f44b64d853e93f4edafbd64a64f504be35babc`
compiles, and against it (`--root <fixm5> --only EDGE_SCHEMEREL,EDGE_SLASHLESS`):

```
EDGE_SCHEMEREL PASS rows=[('S2482', 'REFUSED', 1)] tgt_hits=0 src_hits=1 tb=False
EDGE_SLASHLESS FAIL rows=[('S2905', 'UNREACHABLE', 2)] dir_hits=0 root_hits=1 exit=1
```
Health control on the unpatched tool: both legs PASS, exit 0. The fix restores exactly the intended
single-property kill.

**Still true in rev4:** for every mutant other than m5, `run_legs = pinned`, so MUT observes only the
pinned legs and cannot certify "exactly" for m1,m2,m3,m6,m7,m8,m9,m10,mread (`accept-o.py:1095-1102`,
`pinned_lines` filter). The claim sentence "ten byte-patched mutants each fail **exactly** their
pinned leg" is supported for m5 only after the indent fix and only against the one previously
observed co-failure (`EDGE_SCHEMEREL`); as landed it has **zero** exclusivity evidence. Either scope
the sentence or run an all-legs-per-mutant exclusivity check (expensive: 10 × 23 legs).

**Post-landing attack gap (MEDIUM-1):** `CriticRevO.md` (23:52) explicitly attacks rev3
(`c27a9fef…`, `:10-11`) and states "All four requested revised-byte checks remain unmeasured".
Rev4 landed at ~23:55. **No seat has attacked the rev4 bytes**; my unknown-selector run is the only
executed rev4 evidence in the wave. The rev4 receipt should not be treated as attack-validated until
a post-landing attack lands (or the L1 records the substitution).

## 5. Freeze chain — CLEAN

`reports/round-63/telemetry/freeze-sha256.txt` (sha256 of the record itself
`3703bcec595808cf43fdea2f4e6018d7fd60505aa0e4681078c412940ef3fdbf`) — all four entries recomputed:

| path | recorded | on disk | base `ff30a205` blob |
|---|---|---|---|
| `reports/round-63/accept-o.py` | `ff4091c4…` | `ff4091c4…` | `ff4091c4…` |
| `reports/round-63/accept-c.py` | `626264c6…` | `626264c6…` | `626264c6…` |
| `reports/round-63/claims.json` | `372050ea…` | `372050ea…` | `372050ea…` |
| `tools/reopen-row.py` | `c0f10a84…` | `c0f10a84…` | `c0f10a84…` |

The freeze record is byte-identical to its base blob (no post-freeze edit). `git status
--porcelain -- reports/round-63/` shows only the untracked `telemetry/revisions.txt` (claim Ca's
land), no modification of a frozen file. **No freeze discrepancy.**

## 6. Lower-severity findings

**LOW-1 — duplicate/truncated dry-run pair.** `dry-run-o.txt` (397 B, 19:33) and
`dry-run-o-baseline-copy.txt` (397 B, 19:36) are **byte-identical** (`cmp` → identical): one run
under two names. Both stop after seven legs (TOOL…PRIV) with no verdict and no `exit=`. They are not
in `claims.json` O.lands, but they are in the receipts list several seats are asked to audit; if
cited, they must be cited as a truncated dry run, not a predicate result.

**LOW-2 — subset runs print the claim-level verdict.** `edge-o.txt`, `mut-o.txt`, `control-o.txt`,
and RevVerifyO2's quick run all end `ACCEPT-O-64: PASS` / `exit=0` while most legs printed `SKIP`.
Rev4's fail-closed selector removes the *unknown-name* hazard, but a valid subset still prints the
full predicate's PASS sentence. Each of these receipts does carry its `--only …` command line in the
header, so provenance is recoverable; keep that header requirement for the rev4 receipt. (The
docstring's "legs not run … do not count" semantics is intentional; the reader hazard is naming.)

**INFO — rev3 mutant evidence set is now stale.** `reports/round-64/mutants/` was populated at 23:38
from the rev3 table (all ten sources present, closing the wave-1 M3 "empty dir" gap). The counter
writes mutants under its own tempdir and `rmtree`s it (`accept-o.py:1068`), so a rev4 run will **not**
refresh that directory. Rebuilding m5 from the rev4 table gives the invalid
`795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb` (§4), versus persisted
`83ecd7341afe979f…` (rev3) → **STALE_DIFFERS**. If `mutants/` is cited as rev4 evidence it must be
re-copied after the rev4 MUT run; otherwise cite it as rev3.

## Verification gaps / residual risk

- No full rev4 run and no rev4 receipt observed; I did not run the 23-leg predicate (≈15 min:
  DEFAULT 150 s + TIMEOUT + DRIP + MUT) because the seat boundary assigns it to RevVerifyO2.
- The rev3 receipt was validated structurally (parse + hash cross-check), not by re-execution.
  Its numbers are consistent with the counter's print schema and with `mut-o.txt`/`edge-o.txt`
  (different random fixture rows, same legs).
- m5's narrowed replacement was rebuilt exactly (`795b8d19…`), shown to be syntactically invalid by
  `py_compile`, and the counter's MUT leg was executed on the landed bytes (FAIL). The dedented fix
  was validated only in scratch (`804c9473…`); the lane file was not edited, so the repair and its
  post-fix MUT leg remain owed.
- Cross-leg exclusivity for the nine mutants other than m5 is never measured by the counter.
- Final re-check at 23:57:55 -03:00: no `final-measures-o-rev4.txt`; counter still `6d9c9354…` and
  tool still `c0f10a84…` while the parent's quick run (pid 158918) was in its MUT phase (`mroot-m8`),
  so that quick run is executing the landed rev4 bytes — but a quick subset is not the receipt.
- jj reads used `--ignore-working-copy`; the observed `@` movement is from other agents' edits, not
  this seat. I did not run `jj` snapshotting commands.
- LSP: no server was surfaced for this repo's Python telemetry scripts; checks used direct
  execution, hash comparison, and `git cat-file` provenance — recorded here as the fallback.
