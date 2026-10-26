# ScribeLogScorecard — round 74, wave 2 (kotodama-shokunin)

Seat role: scribe. Deliverable: the two draft texts L1 appends — the `LOG.md` round-74 entry and the
`SCORECARD.md` `## Axes — round 74` section — with every number carrying its command, verdicts left
`AUTHOR-SIDE`, and anything unverified marked `to-verify`. By this seat: no product code, judge, claim, counter or
lane state was edited; the lane was read with read-only git commands only (one concurrent worktree change by another
seat is recorded as F6).

## Behavior

1. Read the frozen claims (`git show 00c408a0…:reports/round-74/claims.json`) and the round-73 LOG entry shape
   (`git show f7104cb:LOG.md` lines 4288-4302).
2. Re-derived every before/after number at its own revision from the git tree (not the worktree).
3. Re-ran both counters in a disposable clone of the lane (`/tmp/ScribeLogScorecard-2.LgWcjz/lane`), grading each
   claim at its own lands revision, with the clone's local `main` pinned to that lands.
4. Wrote the two drafts:
   - `.ufo/waves/round-74/w2/drafts/log-entry.md`
   - `.ufo/waves/round-74/w2/drafts/scorecard-axes.md`
5. Attacked the landed record's prose against its own receipts: five findings (F1-F5) plus one concurrent-state
   observation (F6).

## Gates exercised by this seat

| gate | command | raw result |
|---|---|---|
| claim C counter at C lands | `python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin` | `ACCEPT-C-74: PASS legs=13/13`, exit 0 |
| claim Ca counter at Ca lands | `python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin` | `ACCEPT-CA-74: PASS legs=11/11`, exit 0 |
| append-only, protected set base..C lands | `git diff --numstat f7104cb c4bf61a -- LOG.md SCORECARD.md corpus/lessons/round-74.md corpus/lessons/round-73.md corpus/lessons/round-72.md reports/round-73/claims.json reports/round-73/ledger.json` | `19 0 SCORECARD.md` / `211 0 corpus/lessons/round-74.md` — zero removed lines |
| count drift (before) | see the fenced block below | 804 / 247 / 0 / 0 / 0 |
| count drift (after) | see the fenced block below | 808 / 249 / 2 |

```
# before (base f7104cb)
git show f7104cb:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'   -> 804
git ls-tree -r --name-only f7104cb corpus/knowledge | grep -c '\.md$'                            -> 247
git ls-tree -r --name-only f7104cb corpus/knowledge | grep -ci 'worldbuilding-setting'           -> 0
git show f7104cb:corpus/SOURCES.md | grep -cE 'litmemo\.com|tuduku\.space|chinawriter\.com\.cn'  -> 0
git grep -lE '設定ノート|世界観|世界观' f7104cb -- corpus/knowledge | wc -l                      -> 0
# after (C lands c4bf61a)
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md                       -> 808
find corpus/knowledge -type f -name '*.md' | wc -l                                               -> 249
git ls-tree -r --name-only c4bf61a corpus/knowledge | grep -ci 'worldbuilding-setting'           -> 2
```

Not run by this seat (cited from committed receipts only): the two `--selftest` runs, the do-nothing and
junk-landing runs, and the census. Receipts read: `reports/round-74/telemetry/selftest-c.txt`
(`SELFTEST: 69/69 scenarios`, exit 0), `selftest-ca.txt` (`SELFTEST OK: 179 checks across 41 scenarios
reported-fail=0`, exit 0), `controls-c.txt` (`ACCEPT-C-74: FAIL legs=4/13`, exit 1; lands==base refused
`legs=0/13`, exit 2), `controls-ca.txt` (`ACCEPT-CA-74: FAIL legs=7/11`, exit 1; lands==base refused
`legs=0/11`, exit 2), `junk-c.txt` (`J1=FAIL, J2=FAIL, J3=FAIL, J9=FAIL`, `ACCEPTED JUNK LANDINGS: none`),
`junk-ca.txt` (`J4=FAIL, J4b=FAIL, J5=FAIL, J6=FAIL, J7=FAIL, J8=FAIL, J9=FAIL`, `ACCEPTED JUNK LANDINGS: none`).

## Findings

### F1 — MEDIUM — the frozen claim-Ca control prose contradicts its own committed receipt (RECEIPTS)

The frozen `do_nothing_control` for Ca says (verbatim, `git show 00c408a0…:reports/round-74/claims.json`):
"controls-ca.txt: (1) lands == <freeze> FAILS with REPAIR, ANNOTATE, RECEIPTS red and FROZENCFG/LEDGER green".
The committed receipt measures four different red legs and RECEIPTS green.

```
$ git show 5e4796c:reports/round-74/telemetry/controls-ca.txt | grep -E '^LEG (PASS|FAIL) (REPAIR|ANNOTATE|NOSTUB|SEPARABLE|RECEIPTS)|^ACCEPT-CA-74'
LEG FAIL REPAIR
LEG FAIL ANNOTATE
LEG FAIL NOSTUB
LEG FAIL SEPARABLE
LEG PASS RECEIPTS
ACCEPT-CA-74: FAIL legs=7/11
ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base f7104cbce186)
```

The measured red set is REPAIR, ANNOTATE, NOSTUB, SEPARABLE (4 red, 7 green), not the frozen prose's "REPAIR,
ANNOTATE, RECEIPTS red"; RECEIPTS is green because the round-73 PASS-at-lands receipts exist at the freeze tree.
Why the prose differs is not observable in the frozen bytes; the receipt is the measured artifact. [INFERENCE] The
prose was drafted before the SEPARABLE/RECEIPTS patch carried at the re-freeze `3595c919` and was frozen unchanged.
Claim C's control prose is weaker, not false: it names six red legs and omits REPOINTED, CITEDLINES and
SCRATCHMIRROR (`controls-c.txt`: `LEG FAIL` on ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, CITEDLINES,
SCRATCHMIRROR, INDEX; `ACCEPT-C-74: FAIL legs=4/13`).

Proposed fix: one append-only erratum row in `corpus/lessons/round-74.md` `## Mistakes` (R74-M11, class
`stated-vs-measured`) recording the measured red sets for both controls, with the two commands above; do not
rewrite `claims.json` (frozen bytes stand, the lane's own rule). The draft LOG entry and SCORECARD section state the
measured sets only.

### F2 — MEDIUM — the junk-landing receipts named by the frozen controls do not exist at either claim's lands revision

`junk-c.txt` and `junk-ca.txt` are named by both frozen `do_nothing_control` fields, but both first appear at
`1d7add3`, after both lands revisions. A falsifier reading the claim at its own lands finds the path absent.

```
$ for rev in de93d91 00c408a0 5e4796c c4bf61a 1d7add3; do echo "=== $rev ==="; git ls-tree --name-only $rev:reports/round-74/telemetry/ | tr '\n' ' '; echo; done
=== de93d91 === accept-c-73-at-lands.txt accept-ca-73-at-lands.txt census-start.txt gap-sweep.txt selftest-c.txt selftest-ca.txt
=== 00c408a0 === accept-c-73-at-lands.txt accept-ca-73-at-lands.txt census-start.txt controls-c.txt controls-ca.txt gap-sweep.txt selftest-c.txt selftest-ca.txt
=== 5e4796c === accept-c-73-at-lands.txt accept-ca-73-at-lands.txt census-start.txt controls-c.txt controls-ca.txt gap-sweep.txt selftest-c.txt selftest-ca.txt
=== c4bf61a === accept-c-73-at-lands.txt accept-ca-73-at-lands.txt census-end.txt census-start.txt controls-c.txt controls-ca.txt gap-sweep.txt selftest-c.txt selftest-ca.txt
=== 1d7add3 === accept-c-73-at-lands.txt accept-ca-73-at-lands.txt census-end.txt census-start.txt controls-c.txt controls-ca.txt gap-sweep.txt junk-c.txt junk-ca.txt measures-c.txt measures-ca.txt selftest-c.txt selftest-ca.txt
```

`git ls-tree c4bf61a:reports/round-74/telemetry/` exits 0 and lists no `junk-*`; the same for `5e4796c`. The
counters do not read these files, so neither PASS is affected; the defect is evidence provenance: the control the
claim names was produced and committed after the lands it grades. QUALITY 25(b) ("the freeze ships the junk
landings") also cannot be satisfied at `00c408a0`, because QUALITY 25 itself landed later, at `5e4796c`.

Proposed fix: (a) record the ordering in the same lesson erratum ("control receipts `junk-*.txt`, `measures-*.txt`
are committed at `1d7add3`, after both lands"); (b) round 75 commits control receipts before the lands commit, and
a leg (or a receipt-shape check) resolves a named control path against the revision that claims it. Do not rewrite
the frozen claims.

### F3 — LOW — `w1-results.json` carries no per-seat `status`, so "dead seats" cannot be read from statuses

The item instructs reading `w1-results.json` statuses; no seat result has one.

```
$ python3 -c "import json;d=json.load(open('.ufo/waves/round-74/w1/w1-results.json'));print(len(d['results']),sorted({k for r in d['results'] for k in r}))"
42 ['agent', 'name', 'note', 'output']
```

Liveness was therefore determined from two facts instead: every `output` is non-empty (all 42) and every seat has a
report file `.ufo/waves/round-74/w1/<name>.md` (42/42, plus the two `.postwave.md` copies from R74-M10). Result:
**no dead wave-1 seats**. Proposed fix: the wave driver records `status` (`completed|dead|timed-out`) per seat in
`w1-results.json`; the draft LOG states the evidence actually used.

### F4 — LOW — lesson line 119 says the SCRATCHMIRROR sequencing clause "stays owed"; the landed counter enforces it and passes

```
$ sed -n '119p' corpus/lessons/round-74.md
commit" sequencing clause is not exercised by a leaf seat and stays owed.
$ grep -n 'def leg_scratch_mirror' -A 8 reports/round-74/accept-c.py
     """SCRATCHMIRROR: the validate --file receipt carries exit 0 on the
     mirrored corpus with the four rows and both entries, in a commit strictly
     before the registry-append commit."""
$ git log --reverse --format='%h %s' f7104cb..c4bf61a -- .ufo/waves/round-74/assimilation/validate-receipt.txt
de93d91 round-74: freeze — final claims, ledger, counters, controls inputs, inherited round-73 w2 files, wave-1 evidence
```

The receipt is first committed at the freeze `de93d91`, a strict ancestor of the registry-append commit `d7a3840`,
and the leg PASSes at `c4bf61a`. The sentence is true of the seat that wrote the mirror (a leaf cannot commit) but
reads as an open obligation after landing. Proposed fix: the erratum row in F1 also records "clause exercised by
`leg_scratch_mirror`, receipt at `de93d91`, append at `d7a3840`"; the draft LOG does not repeat "stays owed".

### F5 — LOW (observation, not a claim defect) — census W01 fires on 3 of the 4 new rows

`census-end.txt` carries 28 W04 lines and 3 W01 lines (S881, S882, S884); S883 is `tier B`, so the W01 predicate
(`tier=="C" && status=="mined" && usedby!="—"`, `scripts/sources-census.sh:669`) does not apply to it.

```
$ grep 'W01' reports/round-74/telemetry/census-end.txt
kotodama	W01	S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md
kotodama	W01	S884 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
$ grep -E '^\| S883 ' corpus/SOURCES.md | cut -d'|' -f5
 B 
```

Field 5 of the pipe-split row is the tier cell, so S883 is registered `docs` / `B`; a check of the form "one W01 per
new row" is red by design. The mirror receipt states the same (`W01 x3 … W04 x28`) and the draft LOG says 3, not 4.
No census change is warranted; the census rule is working as written.

### F6 — MEDIUM (concurrent-state observation; not authored by this seat) — a tracked round-74 artifact is zero bytes in the worktree while this report is written

`.ufo/waves/round-74/counters/junk-r74-run.txt` (added by `1d7add3`, 242 lines) is empty in the lane worktree at
2026-10-25 23:11 local, during this seat's run. This seat wrote only the three files listed under "Touched
surfaces"; it did not open, truncate or restore this path (its counters ran in `/tmp/ScribeLogScorecard-2.LgWcjz`).
The change appeared after this seat's opening `git status --porcelain`, which listed only untracked paths.

```
$ ls -l .ufo/waves/round-74/counters/junk-r74-run.txt
-rw-r--r-- 1 vgpnk vgpnk 0 Oct 25 23:11 .ufo/waves/round-74/counters/junk-r74-run.txt
$ git diff --numstat -- .ufo/waves/round-74/counters/junk-r74-run.txt
0	242	.ufo/waves/round-74/counters/junk-r74-run.txt
$ git show 1d7add3:.ufo/waves/round-74/counters/junk-r74-run.txt | wc -l
242
```

If a wave-2 seat is regenerating the junk-run log, this is transient; if it is a shell redirection that truncated and
died, the next commit would ship a zero-byte receipt. Proposed fix (owner side, not this seat): re-run the fixture
generator to regenerate the log, or `git checkout -- .ufo/waves/round-74/counters/junk-r74-run.txt`, and check the
worktree is clean of ` M` entries under `.ufo/waves/round-74/` before L1 appends the LOG entry. This is the
R74-M1 class (a seat writing into the tree after the push), seen live.

## Attacks that FAILED (the claim survived)

- **Counts, before and after.** Registry 804 → 808 rows (S881-S884 contiguous, none removed: the ROWS leg plus the
  diff `804a805,808`), knowledge files 247 → 249, `*worldbuilding-setting*` files 0 → 2, rows naming
  litmemo/tuduku/chinawriter 0 → 4, CJK-term files 0 at base. Survived every re-derivation above.
- **Both counters at their own lands, in an independent clone.** `ACCEPT-C-74: PASS legs=13/13` and
  `ACCEPT-CA-74: PASS legs=11/11`, exit 0 each; the clone's local `main` was pinned to the lands revision and the
  counters still resolved the frozen config from `00c408a0` (printed sha256 `270e31790e2932c8`).
- **Append-only.** Zero removed lines in the protected set base..C lands (`SCORECARD.md` +19/-0,
  `corpus/lessons/round-74.md` +211/-0; `LOG.md`, both earlier lessons, and the round-73 claims/ledger unchanged).
- **S877 in-place change.** Only the `used-by` cell differs between base and lands:
  `corpus/knowledge/linguistics/conlang-scholarship.md` → `corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`
  (`awk -F'|' '{print $(NF-1)}'` on both revisions); the ROWS leg independently requires every other cell
  byte-identical and passes.
- **Commit order of the freeze chain.** `00c408a0` is the first parent of `5e4796c` (Ca lands), which is the first
  parent of `d7a3840` (C landing), which is the parent of `c4bf61a` (C fixes), which is the parent of `1d7add3`
  (telemetry + wave-2 builder); `git merge-base --is-ancestor` confirms each step.

## Touched surfaces (write scope)

| path | state |
|---|---|
| `.ufo/waves/round-74/w2/drafts/log-entry.md` | written (draft) |
| `.ufo/waves/round-74/w2/drafts/scorecard-axes.md` | written (draft) |
| `.ufo/waves/round-74/w2/ScribeLogScorecard.md` | written (this report) |

Scratch: `/tmp/ScribeLogScorecard-2.LgWcjz` (disposable clone; `main` force-moved only inside it) and
`/tmp/scribe-clone-path.txt`. No write under the fleet root, no lane commit, no git-index change, no counter,
claim, lesson, LOG, SCORECARD or QUALITY edit. Tool installs: none. `pacman` not invoked.

## Out of scope / handed to L1

- The drafts are unverified prose until L1 appends them; the LOG entry must not be appended before the wave-2
  reports land (the round-73 entry's own shape records wave-2 repairs in a separate bullet).
- The F1/F4 erratum row (and the F2 ordering note) is L1's append to `corpus/lessons/round-74.md`; the claims bytes
  stay frozen.
- Wave-2 falsify findings are not folded in; verdicts stay `AUTHOR-SIDE`.

## Artifact paths

- `.ufo/waves/round-74/w2/drafts/log-entry.md`
- `.ufo/waves/round-74/w2/drafts/scorecard-axes.md`
- `.ufo/waves/round-74/w2/ScribeLogScorecard.md` (this report)
