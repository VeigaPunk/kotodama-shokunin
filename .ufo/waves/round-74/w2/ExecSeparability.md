# ExecSeparability — causal separability attack (kotodama round 74, wave 2)

Seat: ExecSeparability (leaf). Assignments attacked: QUALITY 7 (`corpus/QUALITY.md:31`) and the
AXES obligation, on claim C (`coverage`) and claim Ca (`calibration`).

Frozen inputs (read before attacking, never modified):

| item | value |
|---|---|
| base | `f7104cbce186bc2e1522abf0cfd619cc834628bb` |
| operative freeze F3 | `00c408a0af2fa5ddf65af2224152ce258b26d896` |
| claim Ca lands | `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` (parent = freeze) |
| claim C lands | `c4bf61a8d722f9168ce0fd8021a6261c000610c5` |
| lane main at dispatch | `1d7add3f7b9eaf6f3349c56c36f6d06325d74236` |
| claims read from | `git show 00c408a…:reports/round-74/claims.json` and the tree copy (identical) |

All work was done in a throwaway clone (`D=$(mktemp -d /tmp/ExecSeparability.XXXXXX)`,
`git -C "$D" rev-parse --show-toplevel` printed `$D`, `git clone -q <lane> "$D/lane"`). Every
counter run was launched with cwd `$D/lane`, `--root .`, and the clone's local `main` pinned to the
`--lands` commit (`git -C "$D/lane" branch -f main <lands>` after `git checkout --detach`). No
byte of the fleet root, no sibling lane, no lane git state outside `$D` was written. The only file
written in the lane tree is this report.

Tooling: nothing installed or upgraded. `pacman` was not run (host-wide pause).

## Verdict up front

* **Claim C survives the separability attack.** The synthetic C-only landing passes
  `ACCEPT-C-74: PASS legs=13/13` with every one of Ca's seven landed files absent.
  `reports/round-74/accept-c.py` names no Ca-landed path at all.
* **Claim Ca survives the separability attack at its declared lands** (`5e4796c`:
  `ACCEPT-CA-74: PASS legs=11/11`), and it needs no C bytes.
* **F1 (MEDIUM): one Ca leg is sensitive to claim C's landing bytes.** `APPENDONLY` is defined over
  the whole `base..lands` tree, and claim C's mandated in-place edit of `corpus/SOURCES.md:832`
  (the S877 `used-by` cell) turns it red. Consequently the two PASS values the round publishes
  (`legs=13/13` and `legs=11/11`) cannot both be observed at one revision: at `c4bf61a` and at the
  lane main the Ca counter is `FAIL legs=10/11`, APPENDONLY only.
* No leg of claim C depends on any byte claim Ca's landing writes (F2 below, read-set proof).
* **F4 (LOW):** claim C's do-nothing control receipt `reports/round-74/telemetry/controls-c.txt` at
  C's lands is *written by Ca's landing commit*, not by either C commit.
* **F5 (LOW):** `SEPARABLE`'s read set contains `reports/round-74/telemetry/controls-ca.txt`, and the
  freeze blob of that file still cites `S881` and the family literal; the leg is green only because
  Ca's own landing regenerated the receipt. The pass is thus partly self-authored.
* **F6 (LOW):** QUALITY 7's mandated `tools/check-claim-separability.py` run on a round manifest was
  never made for round 74 (no `reports/round-74/separability-manifest.json` at freeze or lands;
  rounds 70–73 also lack one).
* **F7 (LOW, environment):** `/tmp` is 100 % full on this host; the first `accept-ca` run on landing
  A produced a **false** `RECEIPTS` red because the round-73 re-run's `git archive | tar` could not
  write (tar rc=2). Re-run with `TMPDIR` on `/var/tmp` passes 11/11. Anyone re-running these
  counters now will hit this.

## Synthetic landings (clone-local, fixture identity `sep-fixture <sep@example.invalid>`)

Landing A = freeze + only the claim-Ca landing commit. Because `5e4796c` is a direct child of the
freeze, the cherry-pick reproduces its tree exactly; I recorded both the cherry-pick and the
identity:

```
$ git -C "$D/lane" checkout -q --detach 00c408a0af2fa5ddf65af2224152ce258b26d896
$ git -C "$D/lane" cherry-pick -x 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
[detached HEAD e2384a9] round-74: claim Ca landing — SCORECARD corrections (12 annotated pairs), SKILL.md repair and gate rows, QUALITY 25, do-nothing controls at the operative freeze
 7 files changed, 174 insertions(+), 44 deletions(-)
A tree   83257915923cd153c4d20db99432f6b84eec2fe9
5e4796c 83257915923cd153c4d20db99432f6b84eec2fe9
$ git diff --stat 5e4796c ca-only | wc -l
0
```

Landing B = freeze + only the claim-C landing commits. The commit list asked for:

```
$ git log --format='%h %s' 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3..c4bf61a8d722f9168ce0fd8021a6261c000610c5
c4bf61a round-74: claim C landing fixes — entry header template tokens, lesson counts sentence
d7a3840 round-74: claim C landing — worldbuilding-setting-practice entries, rows S881-S884, S877 used-by, README index, lesson, census
```

Both commits touch `corpus/**` (`d7a3840` also adds `reports/round-74/telemetry/census-end.txt`, a
census receipt; the counter does not read it — CENSUS re-runs the census itself), and neither
touches a Ca file.
Cherry-picked onto the freeze:

```
$ git -C "$D/lane" checkout -q --detach 00c408a0af2fa5ddf65af2224152ce258b26d896
$ git -C "$D/lane" cherry-pick -x d7a38405d8c347e1fd94c7adca731437d097e2b1
[detached HEAD 5a4368a] ... 6 files changed, 652 insertions(+), 1 deletion(-)
$ git -C "$D/lane" cherry-pick -x c4bf61a8d722f9168ce0fd8021a6261c000610c5
[detached HEAD f13e823] ... 3 files changed, 4 insertions(+), 4 deletions(-)
$ git diff --stat c4bf61a c-only | tail -1
 7 files changed, 44 insertions(+), 174 deletions(-)
```

The B↔C diff is exactly the inverse of Ca's seven-file commit, i.e. B carries claim C's data and
none of claim Ca's: `apply-landing.py`, `run-controls.sh`, `SCORECARD.md`, `SKILL.md`,
`corpus/QUALITY.md`, `telemetry/controls-c.txt`, `telemetry/controls-ca.txt`.

Ca-landed files (from `git diff --name-only 00c408a 5e4796c`): the seven above.
Claim C's own commits change `corpus/README.md` and `corpus/SOURCES.md` and add the two
`worldbuilding-setting-practice*` entries, `corpus/lessons/round-74.md` and
`reports/round-74/telemetry/census-end.txt`.
Neither landing touches `reports/round-74/claims.json`, `reports/round-74/ledger.json`,
`reports/round-74/evidence/**` or `.ufo/waves/round-74/assimilation/**`
(`git diff --stat 00c408a <landing> -- <those paths>` is empty for both).

## Runs (all at the named lands, local `main` == that lands)

| # | command (counters only) | result |
|---|---|---|
| 1 | `accept-ca --lands e2384a9 (A)` | `ACCEPT-CA-74: PASS legs=11/11` (rc 0) |
| 2 | `accept-c --lands f13e823 (B)` | `ACCEPT-C-74: PASS legs=13/13` (rc 0) |
| 3 | `accept-c --lands e2384a9 (A)` | `ACCEPT-C-74: FAIL legs=4/13` (rc 1) |
| 4 | `accept-ca --lands f13e823 (B)` | `ACCEPT-CA-74: FAIL legs=6/11` (rc 1) |
| 5 | `accept-ca --lands 5e4796c` (claimed Ca lands) | `ACCEPT-CA-74: PASS legs=11/11` (rc 0) |
| 6 | `accept-c --lands c4bf61a` (claimed C lands) | `ACCEPT-C-74: PASS legs=13/13` (rc 0) |
| 7 | `accept-ca --lands c4bf61a` (post-C) | `ACCEPT-CA-74: FAIL legs=10/11` (rc 1) |
| 8 | `accept-ca --lands 1d7add3` (lane main) | `ACCEPT-CA-74: FAIL legs=10/11` (rc 1) |
| 9 | `accept-c --lands 1d7add3` (lane main) | `ACCEPT-C-74: PASS legs=13/13` (rc 0) |

Commands, verbatim shape (one line per run; `--freeze 00c408a… --fleet-root /home/vgpnk/Projects/shokunin`):

```
python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
python3 -B reports/round-74/accept-c.py  --root . --lands <lands> --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
```

Stored logs: `/tmp/ExecSeparability/logs/{ca-on-A,ca-on-B,c-on-A,c-on-B,ca-on-c4bf61a,ca-on-main,c-on-main,identity}.txt`
(seat scratch; a copy also sits under `/var/tmp/ExecSeparability/logs/` because `/tmp` was full during the
first run, see F7).

## Findings

### F1 — MEDIUM (BLOCKER if the counters are graded at one shared lands): Ca `APPENDONLY` depends on claim C's landing bytes

*What it attacks:* "the other claim's data legs must fail ONLY for the other claim's data", and the
round's single after-state value (`ACCEPT-C-74: PASS legs=13/13` **and**
`ACCEPT-CA-74: PASS legs=11/11`).

Claim C's landing is required to rewrite one registry line in place — `corpus/SOURCES.md:832`, the
`S877` row whose `used-by` cell gains exactly the new base-entry path (claim C's `ROWS` leg and
`reused_rows` demand it). Claim Ca's `APPENDONLY` leg (`reports/round-74/accept-ca.py:1361-1460`,
frozen text: "changed lines elsewhere are a subset of the stated_at lines of REPAIR pairs plus
appended lines, except the six must_track paths") diffs the **whole** `base..lands` tree and allows
in-place hunks only at the `stated_at` line of a REPAIR pair (`SKILL.md:594` and nothing else after
the wave-1 dispositions) plus pure appends, and exempts the six `must_track` paths. `SOURCES.md` is
not in any allowed set.

Raw output, `accept-ca --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5` (run 7):

```
LEG FAIL APPENDONLY
     protected=['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-74.md', 'corpus/lessons/round-73.md', 'corpus/lessons/round-72.md', 'reports/round-73/claims.json', 'reports/round-73/ledger.json'] protected-removed=0 fleet-pin=dad39efd2798 report=.ufo/reports/round-73/kotodama.md blob-sha256=000bab3a3664 repair-stated_at={'SKILL.md': [594]} must_track-exempt=6 problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
ACCEPT-CA-74: FAIL legs=10/11
exit=1
```

Identical line at the lane main `1d7add3` (run 8): `ACCEPT-CA-74: FAIL legs=10/11`, same sole
problem. The line is claim C's, not Ca's:

```
$ git diff --numstat 00c408a c4bf61a -- corpus/SOURCES.md
5	1	corpus/SOURCES.md
$ git diff -U0 5e4796c d7a3840 -- corpus/SOURCES.md | grep -E '^@@'
@@ -832 +832 @@ Census (from the lane root): the seven commands in the contract's
```

That the red is C's and not Ca's is proved by the synthetic pair: at A (Ca only) `APPENDONLY` is
`LEG PASS`; at B (C only) it is `LEG FAIL ... problems=['corpus/SOURCES.md: changed lines outside
REPAIR stated_at lines [832]']`. The ledger's own design note anticipated in-place spans and lists
only `SKILL.md`, `SHONEN.md` and "NO README.md or corpus/README.md in-place span is needed"
(`reports/round-74/ledger.json` → `inplace_spans`); it never names `corpus/SOURCES.md:832`, and
`grep -n inplace_spans reports/round-74/accept-ca.py` returns nothing — the leg does not consult the
block at all.

*Why the claim itself survives:* at `<lands>` = `5e4796c` (the claim's declared lands, and the
revision its `measures-ca.txt` receipt stamps) no leg is false: `ACCEPT-CA-74: PASS legs=11/11`.
The claim is separable from C's bytes; the **counter is not composable with C's bytes**.

*Proposed fix (cannot be applied to the frozen counter):* route as a round-74 defect and, for the
next freeze, (a) add a frozen `inplace_allowed` entry `{path: "corpus/SOURCES.md", old_start: 832,
old_count: 1, owner: "claim C reused-row rule"}` and have `leg_appendonly` honour it, or better
(b) scope the leg to the claim's own write set: evaluate `changed_files(base, lands) ∩ (own landed
paths ∪ paired stated_at paths ∪ protected ∪ must_track)` instead of the whole tree. Any round text
that publishes both PASS values must name each claim's own lands revision; "PASS at lands" for both
at one revision is unobservable.

### F2 — attack FAILED (evidence): claim C needs zero bytes of claim Ca's landing

`accept-c --lands f13e823 (B)` (no `SCORECARD.md` correction rows, no `SKILL.md` repair, no
`corpus/QUALITY.md`, no Ca control receipts, no Ca scripts):

```
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES / CENSUS /
         SCRATCHMIRROR / COLLCHECK / FROZENCFG / INDEX
ACCEPT-C-74: PASS legs=13/13
```

Static read-set proof (the counter's only path literals, none of them Ca's):

```
$ grep -nE 'SCORECARD\.md|SKILL\.md|corpus/QUALITY\.md|QUALITY\.md|controls-c|controls-ca|apply-landing|run-controls' reports/round-74/accept-c.py
NONE
```

Cross-run on the Ca-only landing A: `ACCEPT-C-74: FAIL legs=4/13`, with exactly the nine C-data legs
red and the four base/freeze gates green:

```
LEG FAIL ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / CITEDLINES / SCRATCHMIRROR / INDEX
LEG PASS GROUND / CENSUS / COLLCHECK / FROZENCFG
ACCEPT-C-74: FAIL legs=4/13
```

Every red names a missing C artifact (`worldbuilding-setting-practice*.md`, the S881–S884 rows,
`corpus/lessons/round-74.md`, the registry-append commit, the README index rows); none names a Ca
artifact. The four green legs are the same four green legs claim C's own `lands == freeze` control
prints (`git show c4bf61a:reports/round-74/telemetry/controls-c.txt`, control 1, `FAIL legs=4/13`).
Ca's landing contributes nothing to any green C leg. `accept-c` at the lane main still passes
(run 9, `PASS legs=13/13`).

### F3 — attack FAILED (evidence): claim Ca needs zero bytes of claim C's landing at its own lands

`accept-ca --lands e2384a9 (A)` = `ACCEPT-CA-74: PASS legs=11/11` (all eleven legs, including
`SEPARABLE`, `APPENDONLY`, `ANNOTATE`, `REPAIR`). The baseline run at the real `5e4796c` gives the
same. `SEPARABLE`'s read set at A is `ledger`, `corrections-rows`,
`reports/round-73/telemetry/selftest-r3.txt`, `reports/round-74/telemetry/accept-c-73-at-lands.txt`,
`reports/round-74/telemetry/controls-ca.txt`, and the thirteen `stated:` lines (twelve read from the
base tree, one from the fleet pin); no byte it reads is C-written.

### F4 — LOW: claim C's do-nothing control receipt is authored by claim Ca's landing commit

`reports/round-74/telemetry/controls-c.txt` is listed in claim C's `do_nothing_control` as the
claim's control evidence. No C commit touches it; Ca's commit rewrites it:

```
$ git diff --stat 00c408a 5e4796c -- reports/round-74/telemetry/controls-c.txt
 1 file changed, 17 insertions(+), 19 deletions(-)
$ git show 00c408a:.ufo/waves/round-74/run-controls.sh   # added by Ca's 5e4796c
# writes reports/round-74/telemetry/controls-{c,ca}.txt
python3 -B reports/round-74/accept-c.py --root . --lands $F --freeze $F 2>&1; ...
```

At the freeze the file still carries the *previous* freeze's measurement (`measured at freeze
de93d91…`, `LEG FAIL GROUND  receipt names a 19-row registry`) — at B the file is that stale blob
(`GROUND` red) while the counter itself prints `LEG PASS GROUND`; at `c4bf61a` the file is the
version Ca's landing commit (`5e4796c`) regenerated, measured at the operative freeze `00c408a`,
which matches the frozen claim's control-1 shape
(`ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, CITEDLINES, SCRATCHMIRROR, INDEX` red;
`GROUND, CENSUS, COLLCHECK, FROZENCFG` green; `FAIL legs=4/13`).

No graded C leg reads the file (`grep` in F2), so no C PASS depends on it, but the claim's declared
control evidence is not owned by the claim. This is the cross-claim write QUALITY 7 names ("rewrites
the other claim's bytes before checking"): here it is not before a check of C's counter, but it is a
Ca commit writing C's evidence. *Fix:* regenerate `controls-c.txt` in claim C's own landing commit
(or split `run-controls.sh` per claim and commit only the claim's own receipt), and have the
`do_nothing_control` field name the commit that produced the receipt.

### F5 — LOW: `SEPARABLE`'s pass at Ca's lands is partly self-authored

`leg_separable` (`reports/round-74/accept-ca.py:1531-1597`) scans
`reports/round-74/telemetry/controls-ca.txt` **at lands**. At the operative freeze that blob still
cites the lane ids and the family literal:

```
$ git show 00c408a:reports/round-74/telemetry/controls-ca.txt | grep -nE 'S88[1-4]|worldbuilding-setting-practice'
42:     id-floor=S881 family=worldbuilding-setting-practice forbidden=['corpus/SOURCES.md', …]
49:     freeze=de93d91cab5a first-parent-of-lands; … min-pairs=10 separable>=S881 family=worldbuilding-setting-practice …
$ git show 5e4796c:reports/round-74/telemetry/controls-ca.txt | grep -cE 'S88[1-4]|worldbuilding-setting-practice'
0
```

On B (no Ca landing) `SEPARABLE` is red for exactly that reason — and *not* for any C-landed byte:

```
LEG FAIL SEPARABLE
     ... scanned=['ledger', 'reports/round-73/telemetry/selftest-r3.txt', 'reports/round-74/telemetry/accept-c-73-at-lands.txt', 'reports/round-74/telemetry/controls-ca.txt', …]
     problems=['cites <redacted lane id> in reports/round-74/telemetry/controls-ca.txt', 'names the frozen …']
```

So the leg turns green only because Ca's own landing regenerated the read-set file (commit
`00c408a`'s message discloses the counter redaction; the receipt was only re-measured at
`5e4796c`). The claim's rule as frozen reads the lands copy, so this is compliant — but the leg
cannot distinguish "the claim's data is independent of C" from "the claim's landing rewrote its own
evidence clean". *Fix:* pin the telemetry members of the read set to their freeze blobs
(`git show <freeze>:<path>`) instead of the lands worktree, and state the requirement as "the
landed receipt is clean **and** the freeze receipt cited nothing" (the freeze one does not).

### F6 — LOW: QUALITY 7's mandated separability manifest/run is absent for round 74

`corpus/QUALITY.md:31` ends: "Run `tools/check-claim-separability.py` on the round manifest before
dispatch." The tool exists (`tools/check-claim-separability.py`, 69,554 B, executable) and earlier
rounds shipped manifests (`reports/round-51…63,66/…/separability-manifest.json`), but:

```
$ git ls-tree --name-only 00c408a reports/round-74/
reports/round-74/accept-c.py
reports/round-74/accept-ca.py
reports/round-74/claims.json
reports/round-74/evidence
reports/round-74/ledger.json
reports/round-74/telemetry
$ git ls-tree --name-only 00c408a reports/round-73/ reports/round-72/ reports/round-71/ reports/round-70/ | grep -i separab
(no output)
$ grep -rn "check-claim-separability" reports/round-74/ corpus/lessons/round-74.md
(no output)
```

No manifest means the QUALITY 7 check could not run at all; the round's separability obligation rests
only on the two counters' own `SEPARABLE` leg (claim Ca) and on nothing for claim C. This is a
lane-wide lapse since ~round 67, not a round-74 invention, but round 74 is the round whose
frontier step is "QUALITY 25 — a counter … ships junk-landing controls", so shipping round 74
without the QUALITY 7 manifest is inconsistent with its own quality claim. *Fix:* freeze a
`reports/round-74/separability-manifest.json` (units: A = freeze+`5e4796c`, B = freeze+`d7a3840`+
`c4bf61a`, the counter runs above, and their expected verdicts) and commit the tool's receipt; the
manifest's dynamic leg would have flagged F1 automatically.

### F7 — LOW (environment/observability): `/tmp` ENOSPC produces a false `RECEIPTS` red

`/tmp` is a separate 128 GiB filesystem at 100 % on this host:

```
$ df -h /tmp
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme1n1p1  128G  128G  878M 100% /tmp
```

The first `accept-ca --lands e2384a9` run (TMPDIR defaulting to `/tmp`) produced:

```
LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=['accept-ca-73 re-run exit=2 (want 0)', "accept-ca-73 re-run did not print 'ACCEPT-CA-73: PASS legs=9/9'", 'reports/round-74/telemetry/accept-ca-73-at-lands.txt: committed stdout differs from the re-run (55544779204d vs e3b0c44298fc)']
ACCEPT-CA-74: FAIL legs=10/11
```

Direct cause reproduced by running the round-73 counter's own materialization under `/tmp`:

```
ERROR: materialize 8841ad3b896a failed (git rc=0, tar rc=2):
```

Re-running run 1 with `TMPDIR=/var/tmp/ExecSeparability/tmp` gives `ACCEPT-CA-74: PASS legs=11/11`.
The leg reports an empty stdout as a *typed-receipt mismatch* rather than as an environment failure;
on this host the counters are not reproducible without an explicit `TMPDIR`. *Fix:* check free
space before the re-run and, when a re-run exits 2 with empty stdout, print `environment: re-run
could not execute` (distinct from a receipt mismatch). This does not touch either claim's bytes.

## Not found (explicit negatives)

* No C leg reads Ca's scripts, SCORECARD, SKILL, `corpus/QUALITY.md` or control receipts (F2 grep is
  empty); B passes 13/13 with all seven absent.
* Ca's `FROZENCFG` does not depend on C: `git diff --stat 00c408a c4bf61a -- reports/round-74/claims.json
  reports/round-74/ledger.json` is empty, and `LEDGER`/`BASEMISMATCH`/`RECEIPTS`/`TRACKED` are green
  on B.
* Ca's `REPAIR`/`ANNOTATE`/`NOSTUB` on B fail *only* for Ca's own absent data
  (`red=["LC-09(statement='94' truth='95')"]`, `no '## Corrections — round 74' section`,
  `LC-01…:no-leading-row`), never for a C byte.
* Ca's `SEPARABLE` on B fails only because of Ca's own freeze receipt (F5), not because of C's
  landing.
* The reused-row edit itself is correct for claim C: the `ROWS`/`REPOINTED` legs are green on B and
  at `c4bf61a`; the conflict in F1 is entirely on Ca's side of the fence.

## Risks / blockers

1. **F1 cannot be fixed inside this round without re-freezing.** The counter, ledger and leg text
   were frozen before data (`reports/round-74/claims.json` status line); amending `APPENDONLY` now
   would break the "no rule changed after a seat scores" rule. It must be routed as a round-74
   defect (next `R74-M*` row) and fixed in the next freeze; until then, any statement of the form
   "both counters PASS at lands" must carry the two distinct lands revisions.
2. **Operational:** this host's `/tmp` is full (F7). Re-runs of `accept-ca.py` need
   `TMPDIR=/var/tmp/...` or the `RECEIPTS` leg will flake.
3. Nothing in this report modifies a frozen byte; A and B are clone-local commits
   `e2384a9`/`f13e823` made with a fixture identity. The throwaway clone was deleted after the runs
   to relieve `/tmp` (F7); it rebuilds with the three commands in "Synthetic landings" above, and
   the seven run logs plus `identity.txt` in `/tmp/ExecSeparability/logs/` carry the raw
   output quoted here.
