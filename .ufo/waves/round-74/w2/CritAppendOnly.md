# CritAppendOnly — round 74 wave 2 (falsify), leaf seat

**ATTACK:** append-only and scope discipline over `git diff f7104cbce186bc2e1522abf0cfd619cc834628bb main`
(`--stat`, `--name-status`, per-file removed-line census), in-place edits only where a REPAIR pair names them
(SKILL.md:594), no write outside `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, MANIFEST.json untouched, the
round-73 tracked files restored (R74-M10), shokuknow untouched.

Lane `kotodama-shokunin`. Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`, operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`, claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`, claim C
lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`, lane `main` at attack time
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236`. Frozen claims read first
(`git show 00c408a0:reports/round-74/claims.json`, leg APPENDONLY and the Ca kill rule). Every mutation in this
report ran in a throwaway clone (`/tmp/tmp.DRjqONoYPz/lane`, `mktemp -d` → `git init` → top level printed $D →
`git clone`), never in the lane. No network fetch; no tool install; pacman not run.

## Verdict

The append-only record over `base..main` **survives**: 248 deletions in total, **zero in the seven protected
files**, and all 248 are accounted for by two sanctioned places plus one inherited-file class whose bytes are
independently corroborated by two wave-1 reports written before the freeze. The in-place discipline also survives:
the only content line changed outside the six inherited files is `SKILL.md:594` (the LC-09 REPAIR pair) plus the
S877 `used-by` cell that claim C's ROWS leg names.

Four defects are reported, none of which removes a line from a protected file:

| # | Sev | One line |
|---|---|---|
| F1 | HIGH | the frozen ledger declares an in-place repair of `SHONEN.md:6` that did not land and that its own frozen APPENDONLY rule rejects (measured red) |
| F2 | MEDIUM | the protected-set check is cardinal only at Ca's lands; on top of claim C's lands a base-era SCORECARD line can be deleted and `ACCEPT-C-74: PASS legs=13/13` still prints (measured) |
| F3 | MEDIUM | two lesson rows say `pending landing` for fixes that are landed (one of them landed 59 s before the lesson itself) |
| F4 | LOW | two fleet-repo writes fall inside the round window and are not attributable to this lane (`demo-cwd.txt`; the round-41 stub's deletion) |

Method note at the end: the prescribed `git diff … | grep '^-[^-]'` census is **unsound** and undercounts by 39
lines here; I used `--numstat` and the raw-hunk check as well.

## Measurements this attack rests on

`git diff --numstat --no-renames <base>..main` — every file with a deletion:

```
189	14	.ufo/waves/round-73/w2/CritEntryAmendFinal.md
46	15	.ufo/waves/round-73/w2/ExecSelftestAll.md
195	215	.ufo/waves/round-73/w2/SimplifierEntries.md
2	2	.ufo/waves/round-73/w2/drafts/log-entry.md
4	1	SKILL.md
5	1	corpus/SOURCES.md
```

Sum of column 2 = 248 = the `--stat` total (`151 files … 248 deletions`). The other 145 files are additions
(`git diff --name-status … | cut -c1 | sort | uniq -c` → `141 A`, `10 M`; the six inherited files are five `M` plus
`RevengerOrigins.md` as `A`).

Protected set of the frozen leg (`LOG.md`, `SCORECARD.md`, `corpus/lessons/round-74.md`,
`corpus/lessons/round-73.md`, `corpus/lessons/round-72.md`, `reports/round-73/claims.json`,
`reports/round-73/ledger.json`):

```
$ git diff --numstat --no-renames f7104cbc..main -- LOG.md SCORECARD.md \
    corpus/lessons/round-74.md corpus/lessons/round-73.md corpus/lessons/round-72.md \
    reports/round-73/claims.json reports/round-73/ledger.json
19	0	SCORECARD.md
211	0	corpus/lessons/round-74.md
```

(Lines with a non-zero second column: none. `LOG.md`, both earlier lessons and both round-73 report files do not
appear at all — untouched.) So the three explicit sub-checks of the assignment pass:
**0 removed lines in LOG.md, 0 in SCORECARD.md, 0 in any lesson** (`corpus/lessons/round-74.md` is new, so its
`-0` is the whole story).

Hunk-level in-place check (`-U0`), the only tests that can distinguish "appended" from "rewritten":

```
$ git diff -U0 <base> main -- SKILL.md | grep '^@@'
@@ -594 +594 @@ not a detector.
@@ -704,0 +705,3 @@ output files alone remain unpinned legacy evidence.

$ git diff -U0 <base> main -- corpus/SOURCES.md | grep '^@@'
@@ -832 +832 @@ Census (from the lane root): the seven commands in the contract's
@@ -835,0 +836,4 @@ Census (from the lane root): the seven commands in the contract's

$ git diff -U0 <base> main -- SCORECARD.md | grep '^@@'
@@ -1434,0 +1435,19 @@ Wave-2 found content defects in the admitted entries …
```

`594` is exactly LC-09's `stated_at` (the one REPAIR pair); `832` is S877's registry row. A cell-by-cell diff of
that row shows exactly one changed cell and 11 cells at both revisions:

```
CELL 10
OLD: corpus/knowledge/linguistics/conlang-scholarship.md |
NEW: corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md |
```

which is the change claim C's ROWS leg sanctions ("its base value plus exactly the new base-entry path") and the
lesson logs old→new. Every other hunk in the round is a pure append (`old_count == 0`).

The six inherited files were not edited by round 74: apart from `must_track`/`content_pins` (which round 74 wrote)
they are pinned twice by two wave-1 artifacts written before the freeze —

```
$ grep -rn '290a6ccd\|dfc8fe0d\|db254d88\|9469d4d6\|079728a5\|7d145919' .ufo/waves/round-74/ --include=*.md
.ufo/waves/round-74/w1/ScoutLedgerSweepC.md:27… (all six, with base blob ids and mtimes 20:37–20:47)
.ufo/waves/round-74/w1/ExecLeftovers.md:26…31 (verdict table: COMMIT-AS-IS, same sha256s)
```

— and `git show main:<path>` reproduces every pinned sha256 (`must_track` 6/6 True, `content_pins` 6/6 True). The
diff those files show against base is the base-blob-vs-worktree gap R74-M1 records, not a round-74 rewrite.

---

## F1 — HIGH — the frozen ledger declares an in-place repair of `SHONEN.md:6` that did not land, and that its own frozen APPENDONLY rule rejects

`reports/round-74/ledger.json` carries, in the normative repair block:

```
$ grep -n "Line 6 is the only changed SHONEN.md line" reports/round-74/ledger.json
737:   "must_hold": "Line 6 is the only changed SHONEN.md line; the four box marks stay `[~]`; 'no non-author verifier on record' is left as filed …"

$ grep -n "SHONEN.md: add to the in-place path set" reports/round-74/ledger.json
99:   "SHONEN.md: add to the in-place path set with an explicit box-1 span (the `  asserted:` line at :6). LC-01 rewrites that line; no other SHONEN line may change.",
```

`repair_edits[0]` for LC-01 gives `old_line` / `new_line` in full, the new line asserting
`804 rows after round 73 — 709 mined, 58 queued, 37 rejected …`.

The tree says otherwise:

```
$ git diff --numstat --no-renames <base>..main -- SHONEN.md
                                  # (empty: the file is byte-identical base..main)
$ git show <base>:SHONEN.md | sed -n '6p' | sha256sum
71f83d32e8893311ab323e506060ba1f47401ae73e1f5e5f25f2c70bfe6fab16  -
$ sed -n '6p' SHONEN.md | sha256sum
71f83d32e8893311ab323e506060ba1f47401ae73e1f5e5f25f2c70bfe6fab16  -
```

Line 6 still reads `412 rows after round 56` at `main`; zero SHONEN lines changed, so the `must_hold` sentence is
false of the landed bytes. The pair is disposed `ANNOTATE` (LEDGER pairs: 13 = 1 REPAIR (LC-09) + 12 ANNOTATE), so
no leg reads `repair_edits` (`grep -n "repair_edits" reports/round-74/accept-ca.py` → no hit) and the block was
simply left behind when R74-M9 moved LC-01 from REPAIR to ANNOTATE.

It is worse than dead weight: it is **forbidden by the claim's own rule**. The frozen APPENDONLY rule is
line-level, "changed lines elsewhere are a subset of the stated_at lines of REPAIR pairs plus appended lines"
(`leg_appendonly`, `repair_lines` built only from `disposition == "REPAIR"`). I executed the ledger's own
`new_line` on a clone at Ca's lands and ran the claim's counter:

```
$ (clone at 5e4796c; patch SHONEN.md:6 with the ledger's new_line; commit c4d6dd4; main → c4d6dd4)
$ python3 -B reports/round-74/accept-ca.py --root . --lands c4d6dd441a4f… --freeze 00c408a0af2f… --fleet-root …
LEG FAIL APPENDONLY
     protected=[…] protected-removed=0 … repair-stated_at={'SKILL.md': [594]} must_track-exempt=6
     problems=['SHONEN.md: changed lines outside REPAIR stated_at lines [6]']
LEG FAIL RECEIPTS
ACCEPT-CA-74: FAIL legs=9/11
```

(The RECEIPTS failure is an artefact of grading a descendant commit; APPENDONLY is the finding.)
`inplace_spans.required_for_this_ledger` is not read by either counter either
(`grep -n inplace_spans reports/round-74/accept-ca.py reports/round-74/accept-c.py` → no hit), so the ledger asks
for an allowlist entry for an edit its APPENDONLY leg would reject.

**Why it matters.** The ledger is the claim's frozen normative record of what the round did to the tree; it says
the SHONEN box was repaired and that no other SHONEN line moved. The lesson says the opposite (its Routed-to-75
item 4 keeps "SHONEN.md:6 still says '412 rows after round 56'" as a REPAIR owed, and R74-M4's own fix column
mentions the same class). A round-75 executor that follows `repair_edits` mechanically either duplicates an owed
repair as if done, or turns APPENDONLY red. Nothing in the claims flips a leg, which is why it survived eleven
legs — this is a recorded-repair/landed-bytes mismatch, not a data error.

**Smallest safe correction (frozen bytes cannot be rewritten).** In the round-75 ledger: (a) mark
`ledger.json`'s `repair_edits[LC-01]` and `inplace_spans.required_for_this_ledger[SHONEN]` as draft residue in one
correction row that quotes the unlanded `new_line`, and (b) carry the SHONEN repair as a **REPAIR pair**
(`SHONEN.md:6`, stated token `412`, observed `804`) so the edit is legal under the same rule that rejected it here.
Until then the round-74 ledger must not be read as "SHONEN repaired".

## F2 — MEDIUM — the protected-set check is cardinal only at Ca's lands; claim C's counter prints PASS with a base-era protected line deleted

The frozen APPENDONLY leg is evaluated over `base..<lands>` with `<lands>` = Ca's lands. Claim C's leg table
(`claims.json`, claim C, 13 legs) has **no** append-only leg, and the two later landing commits (`d7a3840`,
`c4bf61a`) plus the post-lands `1d7add3` are outside Ca's window. Demonstrated counterexample (clone):

```
$ (clone at c4bf61a = claim C lands; delete SCORECARD.md line 1434, the round-73 wave-2 summary paragraph
   that exists at base; commit cd72ae1; main → cd72ae1)
$ git diff --numstat <base>..cd72ae1 -- SCORECARD.md
19	1	SCORECARD.md
$ python3 -B reports/round-74/accept-c.py --root . --lands cd72ae135fae… --freeze 00c408a0af2f… --fleet-root …
ACCEPT-C-74: PASS legs=13/13
```

Control proving the leg is not vacuous — the same deletion on top of Ca's lands:

```
$ (clone at 5e4796c; same deletion; commit 145f827)
$ python3 -B reports/round-74/accept-ca.py --root . --lands 145f827cf61c… --freeze 00c408a0af2f… --fleet-root …
LEG FAIL APPENDONLY
     protected-removed=1 … problems=['protected-removed=1 19\t1\tSCORECARD.md']
ACCEPT-CA-74: FAIL legs=10/11
```

So the rule works where it runs and is silent for two of the round's three landing commits. (A first attempt that
deleted a *round-added* SCORECARD row was not a counterexample at all — `git diff <base>..<that commit> -- SCORECARD.md`
prints `18 0`, since a removed line that base never had is invisible to "removed lines"; recorded here so the
distinction is not lost.)

**State at `main`:** no such deletion exists — the protected-set numstat above is clean. The defect is the missing
grading window, not landed damage.

**Smallest safe correction.** One line in the round-close step: run
`git diff --numstat <base>..main -- <the seven protected paths>` and require an empty second column, after the last
landing commit. Cheaper than a new leg, and it cannot be satisfied by a self-shrinking landing because it names
`main`.

## F3 — MEDIUM — two `Mistakes` rows say `pending landing` for fixes that are landed

`corpus/lessons/round-74.md`, state column:

```
$ awk '/^\| R74-M[0-9]+ \|/{n=split($0,a,"|"); printf "%s => %s\n", a[2], a[n-1]}' corpus/lessons/round-74.md
 R74-M1 => fixed at freeze
 R74-M2 => fixed at freeze
 R74-M3 => pending landing
 R74-M4 => pending landing
 R74-M5 => open — routed
 …
 R74-M8 => fixed at freeze
```

- **R74-M4**: its fix is "the Ca ANNOTATE pair names `LOG.md:4297` and the fleet report only, and its correction
  row re-derives 10 from the receipt". Those rows (LC-02, LC-03) are in `SCORECARD.md` at Ca's lands —
  `git show 5e4796c:SCORECARD.md | grep -c '^| LC-'` → `12` — and Ca's lands (`22:48:30`) **precedes** the lesson's
  own commit `d7a3840` (`22:49:29`). The state was false when the lesson was written.
- **R74-M3**: its fix is the frozen-constant counters plus "each junk landing is a committed control". The junk
  controls landed in `1d7add3` (`22:59:06`), ten minutes after the lesson; the counters landed at the freeze. At
  `main` the row is stale; at the lesson's commit it was defensible only because the junk receipts were pending.

R74-M8 says `fixed at freeze` for the same counter installation that R74-M3 calls pending, so the two rows
disagree about one artifact. This is reference-drift of the class the round itself records (R74-M4's class), inside
the document the round cites as its lesson.

**Smallest safe correction.** An appended erratum paragraph in `corpus/lessons/round-74.md` (append-only file):
R74-M4 → landed at `5e4796c` (rows LC-02/LC-03); R74-M3 → landed at the freeze for the counters and at `1d7add3`
for the junk controls. No line of the table is rewritten.

## F4 — LOW — two fleet-repo writes inside the round window, neither attributable to this lane

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .scratch/goal-20261025-hyaku-run7.md
 M .ufo/state/*.report-baseline            (16 files)
 M .ufo/watchdog.log
?? .tower/
?? .ufo/waves/round-30/
?? demo-cwd.txt
```

- The 18 `M` paths are driver state (goal, baselines, watchdog); `.ufo/state` and `.ufo/watchdog.log` are in the
  driver's write set, not a seat's.
- `.tower/` (dir `2026-10-25 03:48`, `comms/` `2026-10-24 23:44`) and `.ufo/waves/round-30/wave1/ScribeLesson.md`
  (mtime `2026-10-25 15:58:07`, round-30 content) both predate the round-74 window; the round-30 file is the
  misrooted write round 73 already recorded.
- `demo-cwd.txt` (30 B, content `/home/vgpnk/Projects/shokunin`) was created `2026-10-25 20:54:49`, i.e. after the
  round-73 LOG commit `c1b5b47` (`20:36:38`) and 85 s before this round's `w1.ready` (`20:56:14`) — inside the
  round-74 setup window.
- `.ufo/waves/round-41/w1/ExecQuarantineSlice.md`, recorded present in round 73's misroot sweep at `19:58:07`
  (`.ufo/waves/round-73/w2/ScribeLogScorecard.md:224`), is **gone**: `ls -la .ufo/waves/round-41/w1/` shows only
  `swarm-registry.legacy-wave-v1.json`, the directory's mtime is `2026-10-25 21:23:03`, and round 74's own
  `ExecLeftovers.md:189` records "absent now".
- No round-74 kotodama file exists under the fleet root: `find .ufo/waves .ufo/reports -newermt '2026-10-25 20:30'`
  returns only other lanes' reports (`round-30/kasegi.md`, `round-64/kumitate.md`, `round-51/chousa.md`,
  `round-41/mado.md`, `round-57/kake.md`, `round-31/kasegi.md`, `round-49/mori.md`, `round-73/kotoba.md`) — the
  fleet runs several lanes concurrently (`mado`, `kasegi`, `kumitate`, `mori`, `chousa`, `kake` all wrote between
  21:03 and 22:57), so a fleet write at `20:54` / `21:23` cannot be attributed to this lane from the bytes.
- The lane's own record is consistent with "no relocation": `ExecLeftovers.md:189` says `ls` shows the directory,
  and no round-74 report claims a fleet write.

**Ruling.** The scope duty *for our seats* survives (no round-74 kotodama file, no lane write under the fleet
root). The two unattributed writes are recorded, not charged. The fleet report this lane does own,
`.ufo/reports/round-73/kotodama.md`, is byte-identical to the blob its pin names (`000bab3a…` at `dad39efd` and at
disk, and the lane's APPENDONLY leg re-checks it).

**Smallest safe correction.** None inside this lane. For the driver: a round-close sweep that flags any fleet path
outside `.ufo/reports/<round>/<lane>.md` touched inside the round window, so the next such stray has a name.

**Lane worktree state during this wave (observed, not charged).** `git status --porcelain` in the lane at attack
time shows the untracked wave-2 directories (`assimilation/guard-proof/mirror-*`, `validate/`, `w2.ready`, `w2/`)
and exactly one tracked modification — ` M .ufo/waves/round-74/counters/junk-r74-run.txt` — which is a live wave-2
seat's scratch re-run, not a landing commit and not this seat's write (this seat's only lane write is this report).
It is invisible to every base..main measurement above.

---

## Attacks that FAILED (the claim survived) — with evidence

1. **"Deleted lines in LOG.md / SCORECARD.md / lessons."** Failed: 0, 0, 0 (`--numstat` above; `LOG.md` and both
   earlier lessons absent from the diff entirely; `corpus/lessons/round-74.md` is a new file, `211 0`).
2. **"In-place edits outside a REPAIR pair's line."** Failed: the only `-U0` content hunks with `old_count > 0`
   are `SKILL.md@594` (LC-09 REPAIR) and `corpus/SOURCES.md@832` (S877 `used-by`, sanctioned by claim C ROWS, cell
   diff shown above, lesson logs old→new). Everything else is `old_count == 0`.
3. **"R74-M10's two stray appends reappear."** Failed: `git diff <base> main -- .ufo/waves/round-73/w1 | wc -l` →
   `0`; `grep -rn "Post-wave update" .ufo/waves/round-73/` → no hits; the round-73/w1 tree is untouched and the two
   post-wave texts live only at `.ufo/waves/round-74/w1/{ExecLedger,ScribeReadmeIndex}.postwave.md`.
4. **"The six inherited round-73 files were rewritten to fit round 74."** Failed: `must_track` 6/6 and
   `content_pins` 6/6 reproduce from `git show main:<path>`, and the same six sha256s are recorded independently in
   two wave-1 reports timestamped 20:37–20:47, i.e. before the freeze (`22:28`/`22:46`).
5. **"MANIFEST.json touched."** Failed: the lane has no `MANIFEST.json`
   (`ls: cannot access 'MANIFEST.json'`); the fleet's is clean — `git -C /home/vgpnk/Projects/shokunin status
   --porcelain -- MANIFEST.json scripts templates` → empty.
6. **"shokuknow written."** Failed: `git -C /home/vgpnk/Projects/shokuknow status --porcelain` → 1918 dirty paths,
   all pre-existing; the newest mtime among them is `2026-10-25 13:34:48` (`lanes/tabi/round8/.work/ratelimit-series.tsv`)
   and `MANIFEST.json` is `2026-10-24 23:33:21`, both before the round-74 window (`20:36` onward). No path under
   `merge/kotodama` was touched today.
7. **"The round-73 claims/ledger were rewritten."** Failed: both files absent from the diff (protected-set numstat
   above prints only SCORECARD.md and the new lesson).

## Method note — the prescribed removed-line grep is unsound here

The assignment's check `git diff … | grep '^-[^-]'` per file returns **209**, not 248:

```
$ git diff --no-color <base> main | grep -c '^-[^-]'
209
$ git diff --no-color <base> main | grep -c '^-'
398
$ git diff --no-color <base> main | grep -c '^--- '
150
```

The 39-line gap is removed content whose first character is itself `-`; `SKILL.md`'s only deletion is one of them:

```
$ git diff --no-color <base> main -- SKILL.md | grep -n '^-'
3:--- a/SKILL.md
9:-- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
```

Line 9 is a removed line (`-` marker + content starting `- `), and `^-[^-]` skips it — which is how a per-file loop
can print `SKILL.md: 0` while `--numstat` prints `4 1`. Use `--numstat` (or count `^-` and subtract header lines,
which needs the `--` guard because about one removed content line can itself begin `--- `). Every figure in this
report is `--numstat`-based.

## What I could NOT check

- **Who wrote `demo-cwd.txt` / deleted the round-41 stub.** The fleet root carries no per-lane metadata for
  untracked paths and five other lanes were writing there concurrently; mtime is the only provenance and it does
  not name an author. F4 is therefore recorded, not charged.
- **Whether the six inherited files' worktree bytes were themselves edited by a round-74 seat before the freeze.**
  The two wave-1 pins (20:37–20:47) bound the *latest* possible edit to before the freeze, and the contents read as
  round-73 wave-2 material (no `R74-`/`round-74` string appears in them:
  `grep -n "R74\|round 74\|round-74"` over the six returns only round-73's own "Routed to round 74" phrase). I
  cannot prove no seat touched them between 20:47 and the freeze; the pins and the TRACKED leg both postdate
  any such window, so the claim's own evidence cannot distinguish it either.
- **Post-`1d7add3` writes.** The assignment's revision for the diff is `main` at attack time; if the lane moves
  again after this seat, the census is stale by construction. I re-read `main` (`1d7add3`) at the start of every
  measurement.
- **Whether `corpus/lessons/round-74.md`'s in-place edit at `c4bf61a` (`2 +-`, one line deleted that `d7a3840` had
  added) is disclosed.** It is invisible to the frozen rule (base..main sees only additions) and the commit subject
  names it ("lesson counts sentence"); I did not grade whether a reader is owed a per-line disclosure.
