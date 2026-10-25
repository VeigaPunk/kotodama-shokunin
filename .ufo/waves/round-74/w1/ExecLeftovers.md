# ExecLeftovers — round 74 / wave 1 (inherited-state resolver)

Seat: LEAF resolver. Target: the six inherited paths under `.ufo/waves/round-73/w2/` that
`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain` reports at the
round-74 base revision `f7104cbce186bc2e1522abf0cfd619cc834628bb`. `git rev-parse HEAD` in
the lane **is** `f7104cb`, and `git diff --cached --stat` is empty, so "worktree vs base blob"
and "worktree vs index" are the same comparison here.

I modified none of the six files, made no commit, ran no formatter or build, fetched nothing
from the network, downloaded nothing, installed no tool, and ran no `git status` inside the
fleet repo (it can rewrite that repo's index; every check there used `ls`/`stat`/`find`
plus `git ls-files`/`git check-ignore`, which only read). Raw unified diffs are kept in
`/tmp/ExecLeftovers/` (`w2.diff`, `crit.diff`, `simplifier.diff`, `ExecSelftestAll.diff`,
`ScribeLogScorecard.diff`, `Logentry.diff`) and are ordinary scratch output, not evidence.

## Verdict table

`base lines` = `git show f7104cb:<path> | wc -l`; `wt lines` = `wc -l` on the worktree file.
Classes: **(a)** late seat append after the push, **(b)** content the landed lesson already
carries (checked against `corpus/lessons/round-73.md` `## Corrections`, `## Mistakes`,
`## Routed to round 74`, and the SCORECARD/SKILL rows), **(c)** new evidence not in any
landed file.

| path | worktree sha256 | base sha256 (f7104cb) | lines base→wt | class | recommendation |
|---|---|---|---|---|---|
| `.ufo/waves/round-73/w2/CritEntryAmendFinal.md` | `290a6ccd839cb8cd09fc5089d1360dc4bcfabdea38f7a83733063159185c50aa` | `246de174216dc07fc11594b95a98b98faee001c6ebdfa755a4427d1cf651066b` | 426→601 (+189/−14) | (a) + (c), partial (b) | **COMMIT-AS-IS** — sole carrier of F17's rendered abstract, the `c1b5b47` disposition table, and the open wording residue (F1/F8/F14) |
| `.ufo/waves/round-73/w2/ExecSelftestAll.md` | `dfc8fe0d2c54442bd5fa1a8f122c37751b89c861aeec2b5e77c041f66c11e71c` | `0d24aeed83b9871de343dacd69db4087f0c62a521804589b171b0f52230ecf5d` | 629→660 (+46/−15) | (a) + (c), one fact (b) | **COMMIT-AS-IS** — sole carrier of the 783-row mirror measurement, the incidental `collision` token, the `legs=1/9` control reading and the four-space-control critique |
| `.ufo/waves/round-73/w2/ScribeLogScorecard.md` | `db254d8896d7cbce3377dc1d3f56ca41312063383a9c319324bf1c1a02e445b3` | `f4f14669fc0d0eaf0b26b9bc8ee78c3a628e76aa0403c90fea89118b20d2db45` | 369→378 (+9/−0) | **(b) entirely** | **COMMIT-AS-IS**, information-neutral; `git show` restore is lossless if a minimal diff is preferred (see §3) |
| `.ufo/waves/round-73/w2/SimplifierEntries.md` | `9469d4d689aeb1f32a4127b9d2a0388236c622d206995df4ff8f11a201bdd481` | `985dd88383609c543198a8ee1c548d04fe6f2cc294905eb5b917a838f3663bed` | 314→294 (+195/−215) | (a) re-run + (c) | **COMMIT-AS-IS** — the rewrite re-measures at `7aa8f99`; the superseded 0316b88 cut list remains readable in the base blob, so nothing is lost either way, and the 20-item cut list is landed nowhere else |
| `.ufo/waves/round-73/w2/drafts/log-entry.md` | `079728a53490714a350ec17195bc72b1034d1878130b6f491a200de53bf6ca6a` | `01d503258c8a6f06712473e4e63e2bbab1816b99ca54d7e4df947984999fd3d3` | 28→28 (+2/−2) | (a) + (c) | **COMMIT-AS-IS** — the only file that records the misroot sweep; caveat §5: its second named path no longer exists |
| `.ufo/waves/round-73/w2/RevengerOrigins.md` | `7d14591923aff7b1dd5a28bc73d4933faf9cf721e4a7b113f6f7178206d581ed` | **absent** (`git show` fails; `e3b0c442…` is the empty-input hash) | —→450 (new file) | (b) for F1–F4, **(c)** for F5/F6 | **COMMIT-AS-IS** — a real 450-line seat report that arrived 2m25s after the fleet report was filed and 1m41s after the round was marked complete; F5/F6 are still open at HEAD (verified, §6) |

No file needs REVERT. Nothing in the six deltas retracts or contradicts a landed byte; every
delta is additive, or a rewrite of bytes that were themselves never landed. The
`git show f7104cb:<path>` originals are intact in the base commit for all five tracked files,
so every recommendation is reversible without cost.

## 1. What the six deltas are, and why the wave directory is a declared carrier

The landed lesson's own Corrections section ends its survivor list with **"Detail:
`.ufo/waves/round-73/w2/`."** (`corpus/lessons/round-73.md:168`). The lesson therefore points
readers at this directory for the detail of findings it only summarises. Committing the
worktree versions is the only way that pointer resolves to the author-side detail; leaving
them uncommitted leaves a dangling pointer behind a lesson paragraph that claims the detail
exists.

The five tracked files were committed at `7aa8f99`/`c1b5b47` in an **in-progress** state: each
worktree revision says so in its own words (ExecSelftestAll: *"`c1b5b47` committed an
in-progress copy of this report"*; SimplifierEntries: the lane *"advanced twice more (to
`c1b5b47`)"*; CritEntryAmendFinal: the repair commit *"also committed an earlier state of
this report"*). So the committed bytes are the earlier snapshot and the worktree bytes are the
seats' finished product.

## 2. `CritEntryAmendFinal.md` — COMMIT-AS-IS

Delta: (+189/−14), four places.

1. **Revision note** (new, 8 lines): states that `7aa8f99` rewrote the amendment and HEAD moved
   to `c1b5b47`, that F1–F16 are stated against the assigned revision, and that **F17** was
   found after the repair. Pure (a).
2. **F17** (new, ~137 lines): the Sowers-Wills "no capture" ruling is false — two status-200
   CDX captures of the canonical article page, replay `20241106195515id_` = 1,030,239 B,
   sha256 `dc061a30bae1c2e207a0494fb6cdbfd1c94b51498c690d78aa26babdd1c35a7e`, body carrying
   the study's own abstract (*"a semester-long language construction project"*), plus the
   429-under-both-UAs control. Its **ground is (b)**: the landed Corrections row 165 already
   records the two captures `20241106195515`/`20241107004043` and reverses the ground to "the
   429 plus scope", credited to ScoutRejectProbes F1. Its **evidence is (c)**: no landed file
   carries the captured abstract's text, the replay byte count, or the consequence that the
   entry's two `(to-verify)` marks are resolvable by ordinary means.
3. **Disposition at `c1b5b47`** (new, ~32 lines): a per-finding table (F2–F7, F9–F13, F15
   closed; F1/F14 wording open; F8 calibration open; F17 open and "worse at HEAD"). (c). The
   Corrections table records the same repairs but not this per-finding adjudication, and not
   the two items it leaves open.
4. **Fetch-log/UA correction** and the verdict rewording (F17 promoted to "the one item that
   moves an axis"). (c).

I re-verified the load-bearing landed-ground overlap at HEAD rather than trusting the report:
`git grep -n "asymmetry"` finds the S876 row, and the S894 correction row is present at
`corpus/lessons/round-73.md:165-166`. I did **not** re-probe Cambridge or Wayback (that is a
fetch, outside this seat's read-only remit); F17's live numbers are the seat's, quoted as such.

## 3. `ExecSelftestAll.md` — COMMIT-AS-IS

Delta: (+46/−15), eight hunks; first changed lines (verbatim excerpts):

```
-No live fetch was made, so QUALITY 21/22 UA records do not apply to this seat. The lane write is this file only;
-`git -C … rev-parse HEAD` is still `0316b888…` and its untracked set is the wave-2 orchestrator's
+… and `c1b5b47` committed an in-progress copy of this report, so `git status` shows
+`.ufo/waves/round-73/w2/ExecSelftestAll.md` modified; I made no commit …
+my hand. **Everything graded below is graded at `0316b888`**, the revision the frozen claim names.
 ### 1.1 `accept-c.py --selftest` = 29 checks (`total = 5 + len(MUTANTS)`, `:1676`)
-The 24 mutants (`MUTANTS`/`EXPECTED_FAIL`, `:1437-1479`) … (`:1668-1675`)
+The 24 mutants (`MUTANTS` `:1425-1450` / `EXPECTED_FAIL` `:1452-1479`) … (`:1670-1675`)
-### 1.2 `accept-ca.py --selftest` = 10 scenario blocks (8 print a leg table, 2 are silent)
+### 1.2 … (7 dump a full leg table, 1 prints only a title, 2 are silent)
```

The substantive additions, and what I measured myself against HEAD:

- **783-row mirror, incidental `collision` token (c).**
  `.ufo/waves/round-73/assimilation/guard-proof/mirror-a3/corpus/SOURCES.md` is 937,676 B;
  `grep -cE '^ {0,3}\| S[0-9]{3,} \|'` = **783**, `grep -ci collision` = **1**. Reproduced
  exactly. The digits `783` appear in no round-73 landed lesson text (the one `783` in
  SCORECARD is the round-69 row count). So the claim that the guard check is satisfied by
  incidental registry prose is (c).
- **four-space control is a narrative, not a receipt (c, one fact (b)).**
  `four-space-control.txt` is **3 lines** and contains no command and no pasted output (I read
  it). The landed addendum (`corpus/lessons/round-73.md:170`) already says guard-proof now
  holds the file and why — that fact is (b); the report's further point, that a three-line
  narrative does not close `guard_receipt_deleted` and that the counter still reads only a
  1–3-space plant, is in no landed file → (c).
- **Counters unchanged after lands (c).** `sha256sum reports/round-73/accept-c.py` at HEAD =
  `95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416`, matching the worktree
  report's quoted sha. Reproduced.
- **`legs=1/9` control reading (c).** The report corrects the claim's control colouring from
  `5/9` to `1/9` under the declared command. `git grep 'legs=1/9'` over the landed lesson and
  SCORECARD returns nothing, so this correction is unlanded; the landed Corrections table says
  only that the counters graded 11/11 and 9/9 at `0316b88`.

Not a REVERT candidate: the deltas are post-lands measurement, and reverting would restore the
seat's superseded belief that HEAD was still `0316b88` — i.e. it would restore a **false**
statement about the lane. That is the decisive reason.

## 4. `ScribeLogScorecard.md` — COMMIT-AS-IS (information-neutral)

Delta: `+9/−0`, one hunk, "F-2.12 Round-72 counter selftest is red (M4's numbers)" with the
command, `exit=1`, and `SELFTEST: 10/11` / `--- clean fixture: expected PASS 10/10, got exit=1`.

This is the one fully (b) delta: the same three strings are landed three times —
`corpus/lessons/round-73.md:111` (R73-M4), `SCORECARD.md:1423`, `SKILL.md:701`. The marginal
information is provenance only: the command line and the `[clone at lands]` qualifier. A
`git show f7104cb:.ufo/waves/round-73/w2/ScribeLogScorecard.md > <path>` restore is therefore
**lossless for the finding** and costs nothing but the provenance block.

I still recommend COMMIT-AS-IS: (i) the round-74 claim Ca premises "the six
`.ufo/waves/round-73/w2` files modified/untracked in the worktree", and committing five of six
while reverting one leaves the wave directory internally inconsistent about which revision
each seat graded; (ii) a seat report that reproduces a landed finding with a command is not
noise — it is the red-before the lesson cites. Flagging it explicitly so the L1 can take the
other branch knowingly.

## 5. `SimplifierEntries.md` — COMMIT-AS-IS

Delta: (+195/−215), a whole-file rewrite against a moved target. The old version graded
`0316b88`; the worktree version re-fetched and re-measured at `7aa8f99` (and states that
`git diff --stat 7aa8f99 c1b5b47 -- corpus/knowledge/ corpus/SOURCES.md` is empty, so its
anchors still hold at HEAD). It:

- keeps the same verdict shape with **re-measured** numbers (495 of 3,957 words cut, base
  2,106→1,830, amendment 1,851→1,632) and both counter runs `PASS legs=11/11`
  (baseline `7aa8f99`, cut `0b50562`);
- adds **"What the repair already fixed"** — (b) for the heading, Harrison/Couturat and
  `naming-systems` pointers (Corrections rows 152–163 cover them), (c) for the S879 page-split
  audit it could *not* pin;
- replaces the 18-item cut list with a **20-item** list anchored to `7aa8f99` line numbers.
  No `SimplifierEntries` finding appears in the Corrections `found by` column, and the cut
  list exists in no landed file → (c). It is the only record that the entries still carry
  ~500 cuttable words.

The superseded 0316b88-anchored list is not destroyed by committing: it is the base blob
(`git show f7104cb:.ufo/waves/round-73/w2/SimplifierEntries.md`). So the rewrite is
strictly-more-informative at the current bytes, and reverting would restore anchors that no
longer exist in the graded tree.

## 6. `drafts/log-entry.md` — COMMIT-AS-IS, with a staleness caveat

Delta: `+2/−2`, both inside already-present bullets:

- `Mistakes mined (R73-M1..M6)`: extended (+651 → +661 chars) — more of the M-series written up.
- `Misroot sweep`: rewritten from a generic count to a named result —

```
-… 18 driver state (`.ufo/state/*.report-baseline`, `.ufo/watchdog.log`, `.scratch/…`) and …
+… 18 driver state (…) and two untracked seat-report artifacts written inside this round's window:
+`.ufo/waves/round-30/wave1/ScribeLesson.md` (round-30 content, mtime 2026-10-25T15:58-03:00)
+and `.ufo/waves/round-41/w1/ExecQuarantineSlice.md` (4-line stub, header "seat report (w1, round 41)",
+mtime 2026-10-25T19:58-03:00). A seat-report write landed in the fleet repo at a wrong-round path …
```

The landed round-73 `LOG.md` entry (`LOG.md:4293-4302`) carries **no misroot paragraph at
all** — the committed entry is a shortened form. So this is (c), and it is the only record of
a wrong-round seat write in the fleet repo.

**Verified, with one drift:**

- `.ufo/waves/round-30/wave1/ScribeLesson.md` — exists, untracked (`git ls-files
  --error-unmatch` → "did not match"), 1521 B, mtime `2026-10-25 15:58:07.367557854`. Matches.
- `.ufo/waves/round-41/w1/ExecQuarantineSlice.md` — **absent now**. `ls` shows the directory
  holding only `swarm-registry.legacy-wave-v1.json`, and the directory's mtime is
  `2026-10-25 21:23:03.905800576`, i.e. something was removed at 21:23, after the draft was
  written at 20:37. So the paragraph's second named path was true when written and is stale
  as committed.

Recommendation stands (commit as-is — the path was real, and rewriting history to match a
later filesystem state would be the wrong repair), but the round-74 Ca ledger or SCORECARD
annotation should record the removal, or a reader will chase a file that no longer exists.

## 7. `RevengerOrigins.md` — COMMIT-AS-IS

Untracked; absent from the base commit; 450 lines, 26,043 B; **birth 20:45:39, mtime
20:47:30**. It is a real seat report: own item (dispatch at
`.ufo/waves/round-73/w2/dispatch.json` → `taskCall.tasks[27]`, name `RevengerOrigins`, agent
`revenger`), own throwaway clone `/tmp/tmp.KiihWafBc1` (created 20:17:20), own fetch directory
`/tmp/revenger/` (13 artifacts 20:22–20:39, including `cap_browser.html`/`cap_curl.html` at
1,030,239 B each), its own UA record, and `no installs; pacman not run`.

Timeline (from `.ufo/watchdog.log`), which settles the class:

```
20:43:14  fleet report .ufo/reports/round-73/kotodama.md written (mtime)
20:43:58  watchdog: "complete kotodama round=73"
20:45:39  RevengerOrigins.md born
20:47:30  RevengerOrigins.md last written
20:48:59  watchdog: "launch kotodama round=74"
```

So the file is a **late seat append after the round closed** — 1m41s after completion and
2m25s after the fleet report that declares it missing. The fleet report says (line 13, wave 2:
"32 of 33 reports returned"): *"RevengerOrigins returned no report by filing time (no
WAVE-DONE received; not replaced)."* That was true at filing and is false as of the commit:
the file exists and no other seat carries its two unique findings.

Content classification against the landed Corrections:

| finding | class | landed carrier (if any) |
|---|---|---|
| F1 S894 "no Wayback capture" ground false | (b) | Corrections row 165 (+ row 166) |
| F2 S879 "23443-byte shell" false | (b) | Corrections row 170 addendum |
| F3 S879 entry "location limit" false | (b) | Corrections row 158. Measured: `0316b88:…amend….md:56` carries "the cyberleninka text is served as extracted HTML with no page markers … (to-verify)"; `grep -c "page marker"` on the HEAD amendment = **0**, `extracted HTML` = 0. The one surviving `(to-verify)` at HEAD (line 73) is the Sowers-Wills one, i.e. F17's target, not this defect |
| F4 S878 conclusion page off by one | (b) | Corrections row 154 |
| **F5 calibration ledger's denominator is author-chosen** | **(c)** | none |
| **F6 an admitted row carries an unswept negative claim** | **(c)** | none |

Both (c) findings were re-checked at HEAD and are **still open**:

- **F5.** `SKILL.md:594` reads "`corpus/knowledge/civilizations/` — 94 entries: 92
  earlier-civilization bases plus two source maps"; at HEAD the directory holds **95** `.md`
  files of which **2** are `primary-sources.md` (so 93 bases), and `corpus/README.md:503` reads
  `## civilizations/ (95)`. `reports/round-73/ledger.json` has **0** mentions of either token,
  and its ids are only L01–L08; no correction row names it. Unchanged at lands.
- **F6.** `corpus/SOURCES.md:831` (S876) still carries the negative clause; no sweep is landed
  for it in the lesson, the entry, or the Gate.

F6/F5 are the two findings the fleet report's "not replaced" ruling silently discards, and F5
is an *axis* finding (the calibration ledger's pair set is author-chosen, with a concrete
counter-example the counter cannot see).

## 8. Is anything still writing there? Is the seat live?

No, on both counts.

- **No open handles:** `lsof --` over every `.md` in `.ufo/waves/round-73/w2/` and
  `…/w2/drafts/` returns nothing.
- **No recent writes:** `find .ufo/waves/round-73/w2 -newermt "2026-10-25 20:48:00"` → empty.
  Latest mtime in the tree is `RevengerOrigins.md` 20:47:30; the wave directory mtime
  (20:45:39) is that file's own creation.
- **No processes:** `ps -eo pid,lstart,etimes,cmd` filtered on `revenger|kotodama|round-73|
  round-74` returns only an unrelated round-73 w1 replay script. The round-73 driver finished
  at 20:43:58 and round 74 launched at 20:48:59.
- **Seat liveness, from read-only fleet state:** the round-73 wave-2 registry
  (`.ufo/waves/round-73/w2/swarm-registry.json`) carries
  `RevengerOrigins = {"kind": "spawn", "agentId": null, "role": "revenger", "item": null}` —
  a spawned slot whose agent id was **never bound** and whose item was never recorded, while
  `dispatch.json` *does* carry the item. That is a dispatch/registry bookkeeping gap, not a
  live seat. The round-73 fleet report likewise records "no WAVE-DONE received". My own peer
  roster does not list the seat, so I cannot add process-level proof beyond the above; what I
  can state is that no process is writing, no handle is open, and the registry binding is
  null.

## 9. Risks for the L1 when committing

1. **Committing all six does not make §7's F5/F6 "handled".** They are open at `f7104cb`; if
   round 74's Ca claim's REPAIR/ANNOTATE legs only read "is the file tracked", a tracked
   report can hide a still-false `SKILL.md` count. The Ca ledger should pair
   `SKILL.md:594 "94 entries … 92 bases"` with the measured `95 files / 93 bases` and
   `README.md:503 "(95)"`, and pair `SOURCES.md:831` with its absent sweep. (Out of this
   seat's write scope — recommendation only.)
2. **`drafts/log-entry.md` names a path that no longer exists** (§6). Commit as-is; annotate.
3. **The fleet report's "RevengerOrigins returned no report" line is now false** and is
   append-only. The round-74 closure should record the late arrival and its two unlanded
   findings rather than repeat "3 dead".
4. **Class (b) does not mean "safe to drop".** ScribeLogScorecard's nine lines are duplicated
   in three landed files, but the *seat-report* provenance (command, `[clone at lands]`,
   `/tmp` receipt path) is unique; dropping it costs the only reproducible run in the seat's
   own voice.
5. **No file here is a retraction of landed bytes.** Nothing was found that contradicts
   `7aa8f99`/`2d1cd91`/`f7104cb`; the six deltas are additive or rewrite never-landed bytes.
   If any wave-2 seat claims it retracted a landed statement, it did so in a file not in this
   set.

## 10. Exercised checks (receipts)

| check | result |
|---|---|
| `git rev-parse HEAD` (lane) | `f7104cbce186bc2e1522abf0cfd619cc834628bb`; `git diff --cached --stat` empty |
| `git status --porcelain` (lane) | 5 ` M` under `w2/`, 1 `??` `w2/RevengerOrigins.md`, plus inherited `??` `.ufo/waves/round-74/`, `reports/round-74/` |
| 12 sha256 pairs (worktree vs `git show f7104cb:`) | as in the table |
| `git diff --stat` / `--numstat` | 5 files, +441/−246 (matches the per-file numbers above) |
| `stat -c 'birth/mtime/ctime'` on the six | §7 timeline; no mtime after 20:47:30 |
| `lsof --` over `w2/*.md`, `w2/drafts/*.md` | empty |
| `find … -newermt "2026-10-25 20:48:00"` | empty |
| mirror-a3 counts | rows 783, `collision` 1 (reproduces the report) |
| `wc -l four-space-control.txt` | 3, header comment + 2 data lines, no command, no output |
| `sha256sum reports/round-73/accept-c.py` at HEAD | `95aee881…fea416` (matches the report) |
| `SKILL.md:594` vs `git ls-tree` civilizations count | 95 files / 2 source maps; `corpus/README.md:503` = `## civilizations/ (95)`; `grep -c` in `ledger.json` = 0 |
| `git grep 'never mention'` at HEAD | present at `corpus/SOURCES.md:831`; no sweep landed |
| misroot paths | round-30 file present/untracked/15:58:07; round-41 file absent, dir mtime 21:23:03 |
| `.ufo/watchdog.log` launch/complete lines | round 73 complete 20:43:58; round 74 launch 20:48:59 |
| `swarm-registry.json` / `dispatch.json` | `agentId: null, item: null` vs `taskCall.tasks[27]` carrying the item |

Not exercised: no fetch, so no UA record applies to this seat (QUALITY 21/22 N/A); no counter,
selftest, lint, build or census was run (the parent owns the integration gate); no probe of the
Cambridge/Wayback numbers quoted from the seats' own reports; no `git status` inside the fleet
repo, by design.
