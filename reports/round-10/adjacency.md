# Round-10 adjacency / connector report — X02

- round: 10 (loop 1 of 3, build round 3 of 4) · shard: X02
  (`reports/round-10/targets.json` `scribe_review`: "X02 adjacency/connector +
  out-of-lane watch")
- date: 2026-10-17 · check window 18:26:35–18:30:41 local (-03:00) =
  21:26:35–21:30:41Z
- baseline revision (declared): `9dc18ec1339bffd6f81e74f1a5742464ef578749`
  (`reports/round-10/claims.json:5`); worktree HEAD during the check:
  `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (`git rev-parse HEAD`, 18:26;
  round-10 availability commits only — **no worker committed**)
- writes: this file only. No acceptance verdict on C/F/O; boundaries only.
- **live-tree caveat**: the round-10 batch is still writing (lane status
  `git status --porcelain=v1 -uall | wc -l` moved 856 → 4238 → 5351 → 6296 →
  7157 across stamps 18:26:35 → 18:30:41). Every count below is stamped;
  every check names its re-run command.

## Verdicts

| # | check | verdict | key evidence |
|---|---|---|---|
| 1 | No canon decisions recorded (lore's province) | pass | §1 — 1 sweep hit, disclaimer class only |
| 2 | Handoff contract untouched by round-10 work | pass | §2 — digest `5f4c02bf…` identical at baseline/HEAD/worktree; 3 round-10 references, all read-only |
| 3 | `PROVINCE.md` still accurate | pass | §3 — unchanged (`05b34a57…`); round-10 write surfaces map onto Owns; refusals unviolated |
| 4 | No writes outside `kotodama-shokunin/` | pass | §4 — root status 0 paths at 6 stamps; round-9 breach remediated; sibling activity is lore's own wave |
| 5 | Fleet root stays clean this round | pass | §4.1 — `/home/vgpnk/Projects/shokunin` `git status --porcelain -uall` = 0 at 18:26:35, 18:26:59, 18:28:17, 18:28:48, 18:29:45, 18:30:15 |
| 6 | L0 surface untouched | pass | §5 — `../.ufo/l0-questions.md` mtime 18:17:33 (round-9 close), unchanged through my final stamp |
| 7 | Filed artifacts mutated by live-lane re-runs | **finding (in-lane)** | §6 — round-5 transient (self-remediated, control demonstrated), round-9 outstanding at final stamp |

## 1. No canon decisions recorded

Scan commands (2026-10-17T21:30:0xZ, lane root, over the round-10 tree as it
stood — 16 files at 18:30):

```sh
grep -rniE "canon( |_)?(decision|ruling|status|standing)|canoniz|ratified" reports/round-10/
grep -rniE "accepted by lore|lore accepted|established as canon|admitted to the (world )?bible" reports/round-10/
```

- canon sweep: **1 hit** — `reports/round-10/drift/shard-07.md:55`, a
  drift-table row citing the handoff gate's own §6 rule ("§6 canon standing
  stays lore's (`tools/gates/handoff-packet-check.py`)"). Disclaimer class;
  no lane file asserts canon standing.
- lore-acceptance sweep: **0 hits**.

Live-tree caveat applies: re-run both sweeps at integration over the complete
round-10 set.

## 2. Handoff contract — untouched by round-10 work

Target: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
(contract_id `kotodama-lore-adjacency`, revision `1.0.0`).

### 2.1 Digest chain (three states, no movement)

```sh
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md
git show 9dc18ec1339bffd6f81e74f1a5742464ef578749:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum
git show HEAD:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum
git diff --stat 9dc18ec… -- corpus/knowledge/synthesis/worldbible-integration-contract.md   # empty
```

| state | sha256 | stamped |
|---|---|---|
| baseline `9dc18ec` blob | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` | 18:26:37 |
| HEAD `e3a1ec9` blob | same | 18:26:37 |
| worktree | same | 18:26:37, 18:30:15 |

Identical to the digest round-9 recorded at baseline/HEAD/worktree
(`reports/round-9/adjacency.md` §2.1) — the contract has not moved since
round 8's metadata pass. `git status --porcelain -- corpus/knowledge/synthesis/`
→ empty (18:28:33); `git status --porcelain -- examples/` → empty (18:28:33).

### 2.2 Every round-10 reference to the contract is read-only

`grep -rn "worldbible-integration-contract" reports/round-10/` → **3 hits**
(18:30:0xZ):

- `reports/round-10/drift/shard-07.md:45` — drift-table row listing the
  synthesis partition's files, contract cited as a document, no edit.
- `reports/round-10/drift/shard-06.md:53` — `stale-documented` row quoting
  contract `:193` ("real typological inspirations separately cited") as
  prose-only, unchecked.
- `reports/round-10/findings-tracker.json:83` — quotes the round-8/9 D3
  frozen-pin drift finding (`50c4c2f2…` declared vs current bytes) and
  explicitly forbids regenerating the manifest from live bytes.

No round-10 file edits the contract, and no fragment claims to have edited it.

### 2.3 Escalations carried forward (unchanged)

- Round-8 L0 question (contract digest drift vs lore's r93 ratification) —
  still open: `../.ufo/l0-questions.md:45`, file mtime 18:17:33 (round-9
  close), no round-10 write (§5).
- Round-9 L0 question (/tmp inode exhaustion) — `../.ufo/l0-questions.md:46`,
  still unanswered; `/tmp` still 100% inode-full at my stamp
  (`df -i /tmp` → `1048576 1048576 0 100%`, 18:28:48).
- The D3 pin-drift remediation is now a **round-10 O finding** in the tracker
  (`reports/round-10/findings-tracker.json:83`, quoted above) — the
  orchestrator still owes the disposition (re-acknowledge, never regenerate).

## 3. PROVINCE.md still accurate

```sh
git diff --stat 9dc18ec… -- PROVINCE.md   # empty
sha256sum PROVINCE.md   # 05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6
```

Digest identical to round-8/round-9 records — unchanged since baseline.

- **Owns list covers the round-10 write surfaces**: new entries under
  `corpus/knowledge/{linguistics,myth-symbol,culture-material,verification}`
  and the `corpus/README.md` index update (declared C21/C22; tracked
  modification at 18:28:39, §6.3), lane reports (`reports/round-10/**`),
  worker scratch (`.scratch/**`). `SKILL.md`, `SCORECARD.md`, `LOG.md`,
  `AGENTS.md`, `tools/` are untouched at my stamps
  (`git status --porcelain` over those paths → empty, 18:30:41).
- **Refusals unviolated**: no canon recording (§1); no real-world
  rights/attribution ruling; no game mechanics; no general research method
  (the drift shards re-run this lane's own commands; no chousa-style source
  retrieval added); no web publishing; no prompt/skill craft.
- The named adjacent-contract path exists and is untouched (§2). The
  "allowed append-only L0 questions" clause was not exercised this round
  (§5).
- One boundary-relevant nuance recorded, not adjudicated: the §6 mutations
  are *worker deviations inside the lane*, not a PROVINCE inaccuracy — no
  amendment to `PROVINCE.md` is needed.

## 4. No writes outside kotodama-shokunin/

### 4.1 Repo topology and fleet-root cleanliness

```sh
cd /home/vgpnk/Projects/shokunin && git check-ignore -v kotodama-shokunin
# .gitignore:1:*-shokunin/	kotodama-shokunin   (parent ignores all lane dirs)
git ls-files -s kotodama-shokunin        # empty — not tracked, no submodule (.gitmodules absent)
git status --porcelain -uall | wc -l     # 0 at 18:26:35, 18:26:59, 18:28:17, 18:28:48, 18:29:45, 18:30:15
```

The fleet root stayed **clean (0 paths) at every stamp of this check** —
including while the round-10 batch was actively writing inside the lane
(lane status 856 → 7157 paths over the same window). Root `.git` mtime
movement is my own `git status` stat-cache refresh; no file was added.

### 4.2 Round-9 breach: remediated before this round

- `../reports/round-9/metadata/v09-myth.md` (the round-9 §4.2 stray) — **gone**:
  `ls ../reports/round-9/metadata/` → No such file or directory (18:26:36).
  The fragment is now in-lane: `reports/round-9/metadata/v09-myth.md` exists
  (12 files in that dir, 18:30:0x) — i.e. relocated as round-9's X03
  recommended.
- `../mtk-zeichentragende.pdf` (round-9 §4.3 stray) — **gone** (18:26:36).
- Residual: the parent `../reports/` directory still exists but is **empty**
  (`ls -la` → 0 entries, mtime 18:15) — git does not track empty dirs, so the
  root stays clean; a one-line `rmdir ../reports` is the orchestrator's call,
  reported not performed (outside my write surface).

### 4.3 Sibling / fleet sweep (round-10 window)

```sh
cd /home/vgpnk/Projects/shokunin
find . -newermt "2026-10-17 18:18:46" -not -path "*/.git/*" -type f \
  | grep -v "^./kotodama-shokunin" | sed -E 's|^\./([^/]+).*|\1|' | sort | uniq -c
#  13 lore-shokunin        (lore's own round-96 wave: seats/V38, V43, V58 + scratch)
```

- `lore-shokunin/` activity is lore's own concurrent wave (`.ufo/waves/round-96/seats/V43-*`,
  `V58-*`, `receipt.json`); `grep -ln kotodama` over those 13 files → 0 hits —
  nothing in the lore delta cites kotodama round 10.
- Root-level files newer than the round-10 declaration: **none**
  (`MANIFEST.json` 18:17:33 and `.ufo/l0-questions.md` 18:17:33 are the
  round-9 close, both pre-window; `MANIFEST.json` is tracked and clean).
- `/tmp` — no writes at depth 1 since 18:18:46
  (`timeout 20 find /tmp -maxdepth 1 -newermt "2026-10-17 18:18:46"` → empty;
  the round-7 fixture `/tmp/d3-outside-probe.json` is 16:43:37, untouched).
  The lane's TMPDIR rule (`.scratch`) is being followed.

### 4.4 No write route out of the lane found in round-10 material

```sh
grep -rnoE "(>>?|tee -a?|cp |mv |curl -o |wget -O )\s*/home/vgpnk/Projects/shokunin/[a-zA-Z0-9._-]+" \
  .scratch reports/round-10 | grep -v kotodama-shokunin          # 0 hits
grep -rnE "\.\./(reports|\.ufo|mtk-)" reports/round-10/          # 0 hits
grep -rnoE "(git -C|cd )\s*/home/vgpnk/Projects/shokunin($|/[a-zA-Z0-9._-]+)" \
  .scratch reports/round-10 | grep -v kotodama-shokunin          # only mirrored copies of
                                                                 # round-9 adjacency.md:233 (read-only quote)
```

- All out-of-lane absolute paths appearing in `.scratch` are **content inside
  exported/mirrored copies of historical reports** (`.scratch/r10f15/export*`,
  `.scratch/r10f16/mirror`, `.scratch/f09/export-*`, `.scratch/f19/iso*`),
  not write targets. Cited examples: the V09 path and `mtk-zeichentragende.pdf`
  inside the mirrored `reports/round-9/adjacency.md`; `CORPUS.md:17` quoted in
  metadata fragments; `.ufo/l0-questions.md` quoted in the round-7 prompt
  template.
- No tracked symlink can route a write out (`git ls-files -s | awk '$1=="120000"'`
  → empty). Untracked, ignored round-7 fixtures under
  `reports/supplement-opencode-1/scratch/round7-15/` include
  `link-real-outside.json -> /tmp/d3-outside-probe.json` — a negative-control
  fixture, target untouched since 16:43 (§4.3); `.gitignore:5` covers that
  scratch dir.

### 4.5 Git scope of lane changes (final stamp 18:30:41)

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
git status --porcelain=v1 -uall | wc -l                    # 7157
git status --porcelain=v1 -uall | sed -E 's/^...//' | awk -F/ '{print $1}' | sort | uniq -c
#  7142 .scratch    14 reports    1 corpus
git diff --name-only HEAD                                  # corpus/README.md, reports/round-9/validation.json
```

| group | paths |
|---|---|
| `.scratch/` worker scratch (f09 2862, f19 990, r10f10 883, o02 834, f11 549, iso-shard07 489, …) | 7142 |
| `reports/round-10/` fragments (16 files at 18:30) + the §6 round-9 mutation | 14 |
| `corpus/README.md` (tracked, declared C21/C22 index update) | 1 |

No path outside the lane. Tracked modifications are the two §6.3 rows;
everything else is untracked. `.scratch/` is still **not gitignored**
(`git check-ignore .scratch` → no match) and contributes 7142 of 7157 status
paths — carried forward from round-9 §5; the orchestrator should
exclude/ignore `.scratch/` deliberately at integration rather than sweep it
into history.

## 5. L0 surface untouched

```sh
stat -c '%y %s' ../.ufo/l0-questions.md   # 2026-10-17 18:17:33.943321833 -0300, 36866 B
```

The file's mtime equals the round-9 close write (`MANIFEST.json` at
18:17:33.947, root commit `f2b68a7`) and did not move through my final stamp
(18:30:0x). No round-10 seat appended an L0 question; `grep -rln "l0-questions"`
over `.scratch`/`reports/round-10` returns only mirrored copies of historical
files. The PROVINCE clause "allowed append-only L0 questions" was not
exercised — and nothing suggests it was needed.

## 6. Finding: live-lane re-runs rewrote filed validation artifacts

Claim F requires every SCORECARD counting command to be re-run; several
counting commands are `python3 reports/round-N/run-validation.py`, which
**writes `reports/round-N/validation.json` next to itself**. Seats that
isolate the run (`.scratch/r10f10/iso`, `.scratch/r10f16/mirror`,
`.scratch/r10f15/export2`, `.scratch/f09/export-*`, `.scratch/f19/iso*`) leave
the filed bytes alone; at least two runs happened in the **live lane** and
mutated filed round-5/round-9 artifacts.

### 6.1 Round-9 — outstanding at final stamp

- State: `reports/round-9/validation.json` is ` M` at 18:26:58–18:30:04
  (stamped twice), 47866 B, diff `+4/−14` vs HEAD (`git diff --stat HEAD`).
  The changed rows are re-run consequences: `git_status` `[]` and
  `untracked_additions` removed (the round-9 close commit `9dc18ec` had since
  tracked those baselines), and two `stdout_sha256` values changed.
- Attribution signal: `.scratch/r10f14/rv9.out` (73 B, mtime
  **18:26:58.398944507 — identical to the live file's mtime**) contains the
  rv9 stdout summary ("claim F: PASS / claim O: PASS / claim D: PASS /
  acceptance_checks_passed: True"). `.scratch/f19/iso/reports/round-9/validation.json`
  (47866 B, same mtime) is f19's `cp -p` copy of the mutated live bytes.
- Note: round-9's own scribe explicitly declined to run this command for this
  reason (`reports/round-9/adjacency.md` §6, "it writes `validation.json`,
  another shard's deliverable"), and the F15–F18 brief says "never rewrite
  filed report bytes — corrections are new entries".
- **Disposition owed** (F fixers/auditors or orchestrator; not absorbed here):
  revert to HEAD bytes (`git show HEAD:reports/round-9/validation.json`) or
  admit the re-run as a new record. Leaving it as a silent worktree mutation
  is the one state the round's own rules exclude.

### 6.2 Round-5 — mutated, then self-remediated with a demonstrated control

- 18:27:32.746906697: live `reports/round-5/validation.json` rewritten
  (17367 B; diff then `+6/−355`, the F-claim measurement block stripped).
  The only round-10 artifact sharing that exact mtime is `.scratch/f11/rv.out`
  (16748 B; a run-validation-shaped stdout with
  `acceptance_checks_passed: false`, `F: false`, `O: false`, exit 1) —
  co-mtime is the attribution signal, not process observation; note stdout and
  file bytes differ in size, so the attribution rests on the co-mtime plus
  f11's surrounding artifacts.
- 18:29:29: **restored**: f11 captured HEAD bytes first
  (`.scratch/f11/validation.json.head`, 23928 B, mtime 18:29:29.556978814) and
  wrote them back (live file mtime 18:29:29.558978819, size back to 23928 =
  HEAD; `git diff --stat HEAD` empty at 18:29:51 and after).
- 18:29:42: re-ran rv5 **in isolation** (`.scratch/f11/mirror/reports/round-5/validation.json`,
  17406 B) and recorded controls (`.scratch/f11/controls.txt`, 18:29:44).
- Verdict: transient in-lane mutation, self-remediated; the remediation
  (HEAD-bytes capture → restore → isolated re-run) is the control the round-9
  instance still needs.

### 6.3 Independent corroboration and current tracked-modification set

- `.scratch/drift-shard13/out-git-scope.txt` (18:27) independently records
  exactly the two ` M` rows — the drift shards see the same state.
- Final tracked-modification set at 18:30:41: `corpus/README.md` (declared
  C21/C22 work, 18:28:39) and `reports/round-9/validation.json` (§6.1).
  Round-5 is clean.
- Class-level recommendation (orchestrator): state in the integration prompt
  that counting-command re-runs must execute against an isolated copy of the
  tree, and reconcile any live `validation.json` mutation before commit.

## 7. Observations outside this shard's verdict scope (reported, not adjudicated)

- **`.scratch/` not gitignored** — see §4.5; now 7142 of 7157 status paths.
- **Empty parent dir** `../reports/` (§4.2) — leftover from the round-9 stray
  cleanup; harmless to git, one `rmdir` from tidy.
- **`/tmp` still 100% inode-full** (`df -i /tmp`, 18:28:48) — round-9 L0
  question 46 still open; lane workers are correctly using in-lane TMPDIR.
- **Drift shard 06 found a stale executability claim** in `SKILL.md`
  (`.scratch/…`, filed at `reports/round-10/drift/shard-06.md:53`): the
  "typological basis" item is prose-only, no gate enforces it —
  `stale-documented` by the shard, not by me; noted here only because it is a
  documentation-vs-behavior boundary item.
- **`reports/round-10/coverage/` currently holds review fragments
  (`review-C04/C08/C10`) with no corresponding `C0x.md` entries on disk at my
  stamps** — reviewers ran ahead of/polling for entries. C-axis business;
  flagged for the C auditor only because a review-without-subject is the kind
  of thing the C claim's counting command should not silently accept.

## 8. Limits of this check

- Live tree: every count is a stamp. Re-run §2.1 (digest), §4.1 (root status),
  §4.5 (lane status), §5 (L0 mtime) and both §1 sweeps at integration over
  the complete round-10 set; §6.1's mutation may be reverted by then (if so,
  the finding stands as "mutation occurred, remediated").
- §6 attributions are by artifact co-mtime and content shape, not by observing
  the process; they are exact enough to name the seat directory
  (`r10f14`, `f11`) and the mechanism, not to swear to the seat's intent.
- No sibling lane or world-bible file was read beyond directory/mtime/status
  sweeps and quoted lines; no cross-lane write was made by this shard.
- I did not run `reports/round-10/run-validation.py` (it does not exist at my
  stamps; it writes `validation.json`, another shard's deliverable) — C/F/O
  counting is the orchestrator's.

## Evidence index

| claim | command / location |
|---|---|
| contract digest chain | §2.1 `sha256sum` + `git show` stamps; diff empty |
| round-10 contract refs read-only | §2.2 `grep -rn`, 3 hits, quoted |
| L0 escalations open | `../.ufo/l0-questions.md:45,46`; mtime 18:17:33 unchanged |
| canon sweep | §1 command, 1 hit (shard-07:55, disclaimer) |
| PROVINCE unchanged | `git diff --stat 9dc18ec… -- PROVINCE.md` empty; sha `05b34a57…` |
| root clean at 6 stamps | §4.1 `git status --porcelain -uall \| wc -l` → 0 |
| v09 stray relocated | `reports/round-9/metadata/v09-myth.md` present; parent dir absent (18:26:36) |
| stray PDF gone | `ls ../mtk-zeichentragende.pdf` → No such file |
| sibling sweep | §4.3 `find -newermt` grouping; 13 lore files, 0 kotodama cites |
| no out-of-lane write route | §4.4 three greps; symlink audit |
| lane status scope | §4.5 stamped commands (7157; 7142 `.scratch`) |
| round-9 mutation | §6.1 `git diff --stat HEAD`; `.scratch/r10f14/rv9.out` co-mtime 18:26:58.398944507 |
| round-5 mutation + control | §6.2 `.scratch/f11/{rv.out,validation.json.head,mirror/reports/round-5/validation.json,controls.txt}` |
| independent corroboration | `.scratch/drift-shard13/out-git-scope.txt` (18:27) |

## 9. Addendum (18:32:30) — extends §1 and supersedes §3's SKILL.md clause

The batch kept writing past my first stamps; two checks were re-run and one
new state change is recorded here.

### 9.1 §1 re-sweep over the grown round-10 tree (26 files at 18:31:35)

`grep -rniE "canon( |_)?(decision|ruling|status|standing)|canoniz|ratified"
reports/round-10/` → **9 hits**, all classified:

- `drift/shard-07.md:55` — handoff gate's §6 rule quoted in a drift row
  (disclaimer; already in §1).
- `drift/shard-09.md:72` — "scope/canon standing is lore-shokunin's and
  outside this lane" (disclaimer).
- `run-validation.py:967` and `validation.json:915` — "no admission,
  promotion or canon decision" (disclaimer, round-10 X03 deliverable).
- `adjacency.md:22,30,36,41,43` — this report's own sweep lines and hits.

Verdict 1 stands: **no canon assertion**; every hit is a disclaimer, a rule
statement, or this report's self-reference. The lore-acceptance sweep stays
at 0.

### 9.2 SKILL.md is now a tracked modification (supersedes §3's clause)

§3 said `SKILL.md` was "untouched at my stamps" — true at 18:30:41, no longer
true after. Fresh stamps:

```sh
stat -c '%y %s' SKILL.md            # 2026-10-17 18:31:58, 31025 B
git diff --numstat HEAD -- SKILL.md # 18  9   (net +9 lines; 291 → 300)
git diff -U0 HEAD -- SKILL.md | grep '^@@'
# hunks at old lines 73, 96, 115 (in place), 118 (+1), 120 (+1), 143 (+2),
# 162, 177 (+5)
```

Two edit moments observed: 18:31:40 (30400 B) and 18:31:58 (31025 B). Content
read from the diff (all in-lane, all documentation):

- locator corrections `costume-language-coupling-table.md:40` → `:43` (×2);
- header "Checklist (executable)" → "Checklist (executable where a tool
  exists)";
- the typological-basis item annotated as a prose gap, citing
  `reports/round-10/drift/shard-06.md` §06-G;
- calibration vocabulary updated to the per-claim set (S/C/H/R/U/V) with
  `source-discipline-calibration.md:67`;
- civilizations count 92 → 94, naming the two source maps.

This is claim F's stale-fixing executed in-lane with evidence pointers — not a
boundary breach. It is recorded here because it changes a surface other
round-10 shards depend on (§9.3).

### 9.3 Consequence: drift-shard `SKILL.md:<line>` locators now point into a moved file

The drift shards ran against the **pre-edit** bytes (isolated copies hold the
30086 B version: `.scratch/f12/iso/SKILL.md` 18:29:48,
`.scratch/r10f15/c5/SKILL.md` 18:29:55, `…/c6`, `…/c7`) and filed line-based
source locators against it. With the §9.2 hunks the cumulative shift is +1 at
old line ≥119, +2 at ≥121, +4 at ≥145, +9 at ≥181.

Demonstrated instance (checked, not inferred):

- `SKILL.md:161` at HEAD = the `CROSS-HOLD` row — exactly what
  `reports/round-10/drift/shard-09.md:23,72` cites it for.
- At 18:32:18, line 161 holds a different row (`A-NEUTRAL` REVIEW).
- Shard-09's ledger row `R10-F09-11` (`shard-09.md:88`) records
  `source_locator: "SKILL.md:161-180"`, command
  `awk 'NR>=161 && NR<=180' SKILL.md | grep -cE 'python3|--selftest|run-validation'`,
  stdout sha256 `4355a46b19d348dc2f57c046f8ef63d4538ebb93600…` — that hash
  can no longer be reproduced against the edited file.

Disposition owed to F14 (ledger) and F19/X04 (audit), not absorbed here: pin
the SKILL.md digest per shard/entry, and either validate locators against the
pre-edit revision or re-derive them and classify the affected entries
`stale-fixed` with a superseding mapping. Left as-is, the ledger's `current`
verdicts for SKILL.md-range commands are true only of the pre-edit revision —
the "silent staleness" claim F forbids.

### 9.4 State at this addendum's close (18:32:18–18:32:30)

- Fleet root: `git status --porcelain -uall` → **0** (still clean).
- Contract `5f4c02bf…`, `PROVINCE.md` `05b34a57…` — unchanged (re-checked).
- Lane tracked modifications: `SKILL.md` (§9.2), `corpus/README.md`
  (declared C21/C22), `reports/round-9/validation.json` (§6.1, still ` M`,
  `+4/−14`, mtime 18:26:58).
- Lane status 7294 paths; round-10 tree 26 files; drift ledger still absent
  (`reports/round-10/drift/ledger.json` → No such file at 18:32).
- §1/§3 verdicts otherwise unchanged; §4 (no out-of-lane writes) re-affirmed
  by the root stamp above.

### 9.5 Post-close observation (18:32:55): round-8 script repair lands

`reports/round-8/run-validation.py` is now a tracked modification
(mtime 18:32:28, `git diff --numstat HEAD` → 48/14). Read from the diff: a
deliberate repair adding `gate_blob_for_pin()` so the round-3 pins resolve by
matching committed blobs ("Round 10 repair: the pinned revisions are resolved
by matching each manifest…") — an F-axis stale-fix in place with in-code
evidence, i.e. the disposition the brief allows, not the §6.1 pattern.

Recorded because it extends the §9.3 principle: **filed per-round scripts are
being repaired in place this round**, so any recorded output hash or line
locator tied to the pre-edit script (e.g. `reports/round-8/validation.json`
entries in the ledger, or the round-8 script's own line references) is valid
only against the pre-edit revision. The ledger should pin a digest per
command source (script or SKILL.md), exactly as §9.3 recommends for SKILL.md.

Final stamps at 18:32:55: root `git status --porcelain -uall` → **0**; lane
status 8273 paths; tracked modifications = `SKILL.md`, `corpus/README.md`,
`reports/round-8/run-validation.py`, `reports/round-9/validation.json`; no
path outside the lane; contract `5f4c02bf…` and `PROVINCE.md` `05b34a57…`
unchanged.
