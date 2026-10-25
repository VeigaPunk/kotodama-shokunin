# CritAppendOnly — append-only and scope discipline over `8841ad3b..0316b888`

Seat: CritAppendOnly (round 73, wave 2, FALSIFY). Leaf: no delegation, no background jobs, no `task` spawns.
Base `8841ad3b896a0227674fa0725b818c999118046f`, lands `0316b8883b4f8d44b8efd720140e7f52f734a102` (`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD`).
Nothing under the fleet root was written; the only lane write is this file. No tool installed. No live fetch made, so QUALITY 21/22 UA records do not apply to this seat.
Mutation experiments ran in `D=/tmp/tmp.1TkvHgC34F` (`git -C $D rev-parse --show-toplevel` = `/tmp/tmp.1TkvHgC34F`, clone `$D/lane`, detached at lands, identity `kotodama-shokunin <kotodama@shokunin.local>`).

## 0. The prescribed check under-reports: run it, then run the per-commit one

The item's first command, verbatim:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --numstat \
    8841ad3b896a0227674fa0725b818c999118046f 0316b8883b4f8d44b8efd720140e7f52f734a102
git diff --numstat: 133 files
… 132 of the 133 lines carry "0" in the removed column …
1	1	SHONEN.md
```

**Exactly one file with removed lines in the whole range: `SHONEN.md`, 1 removed / 1 added.** Statuses across the range: `127 A`, `6 M`, `0 D`, `0 R` — no deletion, no rename, no merge (`git rev-list --merges 8841ad3b..0316b888 | wc -l` = `0`).

That number is misleading, and the reason is structural, not a lane trick: a range diff cannot see a line that was added *and* removed inside the range. The per-commit inventory (`git diff-tree -r --numstat --no-commit-id <c>` for each of the 5 commits, filtered `$2>0`) is the real one:

```
e62d7316 1+  1-  SHONEN.md
35378990 1+  1-  SKILL.md
35378990 2+  1-  reports/round-73/accept-ca.py
85f17eb9 19+ 1-  reports/round-73/accept-ca.py
0316b888 227+ 127- .ufo/waves/round-73/assimilation/id-renumber-map.json
0316b888 1+  1-  corpus/QUALITY.md
0316b888 1+  1-  corpus/README.md
```

**7 removal events in 6 files across 4 commits.** Three of them (`SKILL.md`, `corpus/QUALITY.md`, `corpus/README.md`) are invisible to *every* range diff, including `freeze..lands`, because the removed line was added inside the same range. Only per-commit inspection finds them. (For the map, `git diff --numstat` prints `233 133` because the lane sets `diff.algorithm=histogram`; `git diff-tree` prints `227 127` under myers. Either way the file is replaced, not appended: 138 lines at the freeze commit, 237 at lands.)

## 1. Every removed line, named and adjudicated

### 1.1 `SHONEN.md:6` — ALLOWED, and the repair is correct

```
$ git diff -U0 8841ad3b 0316b888 -- SHONEN.md
@@ -6 +6 @@ Promotion to shokunin requires all of:
-  asserted: `SKILL.md:20` (Decision table), `:468` (Error patterns), `:522` (Checklist); …
+  asserted: `SKILL.md:20` (Decision table), `:505` (Error patterns), `:564` (Checklist); …
+  … Pointers `:468`/`:522` corrected to `:505`/`:564` in round 73 (ledger pairs L04/L05; …).
```

The replacement is not cosmetic: the old pointers were already stale at the base revision, so the "removed" text was false before the round touched it:

```
$ git show 8841ad3:SKILL.md | grep -nE '^## Decision table|^## Error patterns$|^## Checklist'
20:## Decision table
505:## Error patterns
564:## Checklist (executable where a tool exists)
```

Same three line numbers at lands. This is the item's allowed category (SHONEN line 6 pointers), and the ledger pairs L04/L05 observe `:505`/`:564` at lands (`PAIR L04 … observed_lands='505'`, `PAIR L05 … observed_lands='564'` in §4). **No finding.**

### 1.2 `SKILL.md` gate row `accept-c-73` (commit `3537899`) — ALLOWED as "row text added this round", but the edit is grader-shaped (F1)

```
$ git diff -U0 e62d731 3537899 -- SKILL.md
@@ -703 +703 @@ output files alone remain unpinned legacy evidence.
-| accept-c-73 | gate | … | base `8841ad3b…`, five rows S876..S880, both entry paths, …
+| accept-c-73 | gate | … | base `8841ad3b…`, the five adopted registry rows (set in claims.json), both entry paths, …
```

The removed text was added by the immediately preceding commit (`e62d731`, 7+/0) — allowed. What it removed is the string `S876..S880`. Cause proved in F1.

### 1.3 `corpus/README.md:773` (commit `0316b888`) — ALLOWED as "footer text added this round", same cause (F1)

```
$ git diff -U0 85f17eb 0316b888 -- corpus/README.md
@@ -773 +773 @@ Two linguistics entries landed (claim C; …
-… Registry: 799 → 804 rows (S876–S880, all mined, used-by exactly the two entries; …
+… Registry: 799 → 804 rows (five new rows, all mined, used-by exactly the two entries; …
```

Again the removed text was added earlier in the same round. The commit message says it plainly: `README footer without claim-C ids`. Cause proved in F1.

### 1.4 `corpus/QUALITY.md:77` criterion 23 (commit `0316b888`) — ALLOWED, but the added clause is the round grading itself

```
$ git diff -U0 85f17eb 0316b888 -- corpus/QUALITY.md
@@ -77 +77 @@ Grounded in `corpus/lessons/round-73.md` `## Mistakes` (R73-M3): …
-… a leg or scenario changed after freeze is a recorded counter revision …
+… the counter is also run at the FREEZE commit (receipts present, landing absent) so artifact-vs-leg shape mismatches show before data (round 73: GROUND, SCRATCHMIRROR and COLLCHECK read the committed receipts in shapes the receipts did not have; a base-only control cannot see that); a leg or scenario changed after freeze is a recorded counter revision …
```

The sentence is an honest admission that three claim-C legs were red at freeze on artifact *shape*, and that the round's response was to reshape the artifacts (F2). Allowed by the item; the admission is worth crediting.

### 1.5 `reports/round-73/accept-ca.py` — two removals, both disclosed counter revisions

`3537899` (r2): `git(clone, "show", …)` → `git(clone["path"] if isinstance(clone, dict) else clone, "show", …)`, 1 removed / 2 added.
`85f17eb` (r3): the selftest print line `9 scenarios` → `10 scenarios`, 1 removed / 19 added (r3 also adds the worktree-ledger guard and scenario 7b).

Both are recorded in `reports/round-73/counter-revisions.md` r2/r3 with old/new sha. All four sha pins verify byte-for-byte:

```
$ for c in af65165 e62d731 3537899 85f17eb 0316b888; do echo -n "$c "; \
    git show $c:reports/round-73/accept-ca.py | sha256sum; done
af65165 f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865   (= r1 pin)
e62d731 f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865
3537899 be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0   (= r2 pin)
85f17eb 222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89   (= r3 pin)
0316b888 222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89
$ git show 0316b888:reports/round-73/accept-c.py | sha256sum
95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416          (= claim-C r1 pin)
```

`accept-c.py` was not modified after freeze at all (absent from `git diff --numstat af65165 0316b888`).

### 1.6 `.ufo/waves/round-73/assimilation/id-renumber-map.json` — 127 removed lines of a frozen pre-data artifact (F2)

Not in the item's allowed list, and not an append. Adjudication in F2: the *assignments* are unchanged (verified), the `map` object is new, and the rewrite is disclosed — but the mechanism is a whole-file replacement of bytes committed at freeze.

## 2. Findings

### F1 — MAJOR: claim Ca's SEPARABLE leg is implemented wider than the frozen leg, and two true claim-C statements were deleted post-grade to keep it green

Frozen leg text (`reports/round-73/claims.json:171`, claim Ca):

> "SEPARABLE: no byte the Ca legs read (ledger, correction rows, Ca telemetry receipts) cites an S-id >= S876 or a claim-C path; count pairs measure at the pinned base revision so landing C cannot move them"

Counter docstring (`reports/round-73/accept-ca.py:77-83`) repeats the same three byte sets. The implementation adds a fourth, landing-C-dependent scan (`accept-ca.py:805-812`):

```
$ sed -n '805,812p' reports/round-73/accept-ca.py
    added = added_lines(root, base, lands, ("SKILL.md", "corpus/README.md",
                                            "README.md"))
    for line in added:
        for m in SID_RE.finditer(line):
            if int(m.group(1)) >= SEPARABLE_MIN_ID:
                problems.append("in-place added line cites S%s" % m.group(1))
```

Reproduction (throwaway clone, one commit `ba99c0e` restoring the *pre-grade* text — `S876–S880` in the README footer, `five rows S876..S880` in the SKILL gate row — nothing else):

```
$ python3 -B reports/round-73/accept-ca.py --root . --lands ba99c0e --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS APPENDONLY   lane-removed=0 fleet-pin=80d8c9b576d4 blob=ea256ae7f9d7 in-place=['SKILL.md(registry)', 'corpus/README.md(footer)']
LEG FAIL SEPARABLE    … problems=['in-place added line cites S876', 'in-place added line cites S880']
ACCEPT-CA-73: FAIL legs=7/9        (STAMP also red only because measured != the mutant)
```

The same mutant is a clean claim-C lane — the restored ids are claim-C-legitimate content, not a separation breach:

```
$ python3 -B reports/round-73/accept-c.py --root . --lands ba99c0e \
    --fleet-root /home/vgpnk/Projects/shokunin --census-sh /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
LEG PASS ENTRIES … LEG PASS ROWS … LEG PASS REPOINTED … LEG PASS GATE … LEG PASS EVIDENCE
LEG PASS REJECTS … LEG PASS GROUND … LEG PASS CITEDLINES … LEG PASS CENSUS … LEG PASS SCRATCHMIRROR … LEG PASS COLLCHECK
ACCEPT-C-73: PASS legs=11/11
```

Baseline at lands is green, so the delta is caused by the ids alone:

```
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b888 --main 0316b888 \
    --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS LEDGER … LEG PASS SEPARABLE … LEG PASS STAMP
ACCEPT-CA-73: PASS legs=9/9
```

Consequence: the round's green Ca verdict at lands required deleting `S876..S880` / `S876–S880` from two documents claim C wrote about itself (commits `3537899` and `0316b888`), i.e. the landing was shaped to a predicate the frozen claim does not state. `counter-revisions.md:8` records the same leg going red at `e62d731` — "SEPARABLE red for a separate reason" — which was the SKILL-row citation.

Impacted axes: calibration (Ca's SEPARABLE meaning, the "landing C cannot move them" rationale), coverage (C's README/SKILL statements lost their ids). Not a content BLOCKER: every declared Ca leg is true at lands, and the deleted ids were redundant with `claims.json`/`SCORECARD` — but the mechanism is the round's own R2 mistake class one level up (a predicate asserted wider than declared, then the record bent to it).

Smallest safe correction: either (a) narrow the scan to the declared sets (drop the `added_lines` block, or restrict it to lines that are not in a file/span a claim-C entry or row legitimately owns) and restore the two id strings; or (b) amend the *next* round's leg text to declare the added-lines scan, and record this round's two deletions in `corpus/lessons/round-73.md` `## Mistakes` as a counter-shaped edit, since `claims.json` is frozen and cannot be re-cut.

### F2 — MAJOR: the frozen pre-data map was rewritten after first grading to add the `map` object the frozen COLLCHECK leg requires

`accept-c.py` has not changed since freeze, and its COLLCHECK leg requires a `map` object:

```
$ sed -n '1071,1074p' reports/round-73/accept-c.py
            mapping = doc.get("map")
            if not isinstance(mapping, dict):
                bad.append("%s has no map object" % map_path)
                mapping = {}
$ git show af65165:.ufo/waves/round-73/assimilation/id-renumber-map.json \
    | python3 -c "import json,sys; j=json.load(sys.stdin); print('keys:',sorted(j)); print('has map:','map' in j)"
keys: ['assignment_order_rule','assignments','campaign_id_defects','collision_check','collision_classes','companion','conditional_assignments','drafted','namespace_numeric_overlap','namespace_rule','not_assigned','registry_state','round','seat','stale_entries','superseded_file_untouched','supersedes','wave']
has map: False
```

So COLLCHECK was red at the freeze commit for the single reason "has no map object", and the repair was a post-grade rewrite of the data artifact (`0316b888`, 227+/127−), not a counter change. The `map_note` it added says so:

> "`map` (staged -> lane, by document) added after the landed data was first graded (COLLCHECK reads `map`; the file carried the same assignments only in the per-row list). No assignment changed; see lesson round-73 R73-M6."

The item's actual question — did the addition change an assignment? — **no**, verified three ways:

```
old keys vs new keys: + 'map', + 'map_note'; nothing else
assignments old==new: True  (5/5; staged_id, new_target, url, staged_line compared as tuples)
identical minus map/map_note: True
new map: {"S881": "S876", "S882": "S877", "S892": "S878", "S893": "S879", "S901": "S880"}
```

which equals the assignments' `new_target`s and `claims.json`'s `row_set` exactly.

What is still wrong: `claims.json` claim C's after-text cites the map as "committed pre-data at `.ufo/waves/round-73/assimilation/id-renumber-map.json`" and quotes the pairs — but the object that carries the pairs in that form did not exist pre-data; the pre-data evidence is the `assignments` list. And claim Ca's kill_rule promises "the after-state never requires rewriting frozen bytes": the landed after-state does require rewriting 127 lines of a freeze-commit artifact. Neither counter's append-only machinery sees it: the map is not in `APPENDONLY_FILES` (`("LOG.md", "SCORECARD.md", corpus/lessons/round-72.md, corpus/lessons/round-71.md)`) nor in `INPLACE_PATHS` (`("SKILL.md", "corpus/README.md", "README.md")`).

Impacted axes: calibration (Ca's append-only promise), coverage (C's COLLCHECK provenance). Not a BLOCKER: no assignment moved, the addition is disclosed in-file and in the lesson, and the map is consistent with the staged ids and the adopted set.

Smallest safe correction: append a correction row (SCORECARD `## Corrections — round 73`) naming the map rewrite — file, freeze sha, lands sha, "no assignment changed", and the COLLCHECK reason; and add `.ufo/waves/round-73/assimilation/*` to the next round's append-only guard set so a frozen artifact cannot be replaced silently. Do not re-edit the map.

### F3 — MINOR: the append-only guard set does not cover the only base..lands removal, nor the map

`APPENDONLY_FILES` guards `LOG.md`, `SCORECARD.md`, `lessons/round-71.md`, `lessons/round-72.md` plus the fleet blob; `INPLACE_PATHS` authorizes `SKILL.md`, `corpus/README.md`, `README.md`. `SHONEN.md` is in neither list, yet it is the only file the prescribed range diff flags. The leg's docstring says "in-place edits are authorized only inside SKILL.md '## Gates and probes' or a README footer", which reads as a global authorization check; it is not one. Evidence: in my mutant run the leg reported `in-place=['SKILL.md(registry)', 'corpus/README.md(footer)']` while `SHONEN.md` carried a removed line in the same range.

Impacted axis: calibration (the leg's stated scope vs its apparent scope). Correction: either add `SHONEN.md` to `INPLACE_PATHS` with a stated `stated_at` requirement (L04/L05 already name `SHONEN.md:6`), or reword the docstring to "removals are checked only in APPENDONLY_FILES; in-place edits are checked only in INPLACE_PATHS".

### F4 — MINOR: `r3`'s `when` cannot be verified, and the C landing commit carries Ca's counter revision and receipts

`counter-revisions.md:11` dates r3 "before the claim-C landing commit". The r3 bytes first exist *in* that commit:

```
af65165 f8ebb5d8…   (freeze)
e62d731 f8ebb5d8…
3537899 be191795…   (r2)
85f17eb 222d4dd6…   (r3 — the commit titled "round-73 C: conlang-scholarship adoption … counter r3 + receipts")
0316b888 222d4dd6…
```

`85f17eb` also adds `controls-ca-r3.txt`, `selftest-r3.txt`, `red-before-r3.txt` (Ca telemetry) alongside C's entries and rows. The ordering claim is unverifiable from git; the true statement is "authored and landed by the claim-C landing commit". Impacted axes: calibration (record provenance), scope (one commit carrying two claims' artifacts). Correction: change the `when` cell to name `85f17eb`, or state "authored before, landed by `85f17eb`".

### F5 — MINOR: r2 is a counter fix with no shipped red-before, against criterion 23 added this round

`QUALITY.md` criterion 23 (as landed): "each fix to a counter ships its red-before — the same selftest with only the fix removed fails the new scenario". r2's fix (clone dict → `clone["path"]`) adds no scenario and has no red-before receipt: `ls reports/round-73/telemetry | grep red-before` → `red-before-r3.txt` only, and `selftest-r2.txt` still reads 9 scenarios, identical in shape to r1's. The motivating failure exists only as a quoted line in `counter-revisions.md:8` (`ACCEPT-CA-73: FAIL legs=8/9`, header `source=worktree-uncommitted`) — not as a committed receipt. r3's red-before *is* genuine; I reproduced it by deleting only the guard block from a lands checkout:

```
$ python3 -B reports/round-73/accept-ca.py --selftest      # guard removed
ERROR: --lands must be 40 hex
ERROR: base 8841ad3b… is not a commit in /tmp/r73-ca-selftest-_gba3kpm/lane
SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'
```

This also settles a receipt-hygiene worry: the `ERROR:` lines in every selftest receipt come from the intentional CLI-error scenario and are benign (they appear identically here, in `selftest.txt`, `selftest-r2.txt`, `selftest-r3.txt`).

Impacted axis: calibration. Correction: commit the r1-at-`e62d731` run as a receipt (the round's own "not erased" principle), or add a scenario isolating the clone-dict bug with its own red-before, and mark r2's row "no red-before (bug was silent; r1 receipt is the evidence)".

### F6 — MINOR: the do-nothing control's green set is stale for the landed counter

`claims.json` claim Ca: "controls-ca.txt: lands == base FAILS (ACCEPT-CA-73: FAIL legs=5/9; red: REPAIR, ANNOTATE, NOSTUB, TRACKED; green and unmoved: LEDGER, BASEMISMATCH, APPENDONLY, SEPARABLE, STAMP)". True of the cited r1 receipt (`controls-ca.txt`: `LEG PASS STAMP`, `legs=5/9`), but the landed counter's own control reads `legs=4/9` with `LEG FAIL STAMP` (`controls-ca-r2.txt`, `controls-ca-r3.txt`). The r3 header discloses the cause ("STAMP is red here only because lane main has moved past base (measured != lands)"), so this is staleness, not concealment — but a reader diffing the frozen claim against the landed receipts sees STAMP move from green to red with no claim-side note.

Impacted axis: calibration. Correction: one correction row stating the control delta 5/9 → 4/9 and its harness cause (measured revision moved), pointing at `controls-ca-r3.txt`.

### F7 — MINOR: the post-grade map rewrite kept the refuted "announcement booklet" label

The frozen pre-data correction S882 says the staged row's booklet wording "is not carried", and the landed row says the opposite of booklet — `corpus/SOURCES.md:832` … "The full 185-page typeset text was opened (not an announcement booklet)". The map, rewritten after grading, still carries it:

```
$ python3 … print assignment S882 document
М.Ю. Сидорова, О.Н. Шувалова (2006), «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 184 с., ISBN 5-98789-005-5 (announcement booklet)
```

Defensible as a verbatim staged-text quote, but the file was open for rewrite at that moment and the label now contradicts both the row and the frozen correction.

Impacted axis: coverage (C's provenance artifact). Correction: one-line change of the `document` field to quote the staged text with the label removed or marked `[staged label, refuted — see row S877]`, or leave it and record the reason in `## Mistakes`.

### F8 — MINOR: the two late-committed round-72 reports carry no in-file provenance note

`.ufo/waves/round-72/w1/ScoutMergeScan.md` and `ScribeLesson.md` were added by the Ca landing commit `e62d731` (183 and 217 lines) and are the R1 repair (`ledger.json` `must_track`). They present themselves as round-72 w1 seat reports dated 2026-10-25 and contain no line saying they were committed a round late; the disclosure lives only in `corpus/lessons/round-73.md:108` (R73-M1) and `SCORECARD.md:1421` ("tracked from the Ca landing commit on"). No independent copy exists to authenticate their bytes: neither path exists under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-72/w1/` (checked, "no fleet copy"), and `ScribeLesson.md` cites a `/tmp/r72-lesson.md` sha256 that no longer exists.

Impacted axis: calibration (record provenance). Correction: add a two-line header to each file: "produced in round-72 w1, untracked until round 73 (`e62d731`); bytes are the seat's output, not re-derived" — or, if the bytes were re-authored in round 73, say that instead.

## 3. Checks that passed (exercised, not assumed)

| check | command | result |
|---|---|---|
| author = committer = `kotodama-shokunin <kotodama@shokunin.local>` for all 5 commits | `git log --format='%H %an <%ae> \| %cn <%ce> \| %s' 8841ad3b..0316b888` | 5/5 identical both sides |
| no merge commits | `git rev-list --merges 8841ad3b..0316b888 \| wc -l` | `0` |
| no commit touches a fleet path | `git diff-tree --no-commit-id --name-status -r <c>` for each of the 5 | no `MANIFEST.json`, no `scripts/`, no `shokuknow`; lane repo tracks neither (`git ls-files \| grep -E '^MANIFEST.json$\|^scripts/'` → empty) |
| `LOG.md`, `corpus/lessons/round-71.md`, `corpus/lessons/round-72.md` byte-identical | `git cat-file blob <rev>:<path> \| sha256sum` at base and lands | `cb9b5401…`, `2a34d48b…`, `c3508b56…` — identical |
| `SCORECARD.md` append-only | `git diff base lands -- SCORECARD.md \| grep '^@@'` | one hunk `@@ -1405,3 +1405,19 @@` — 16 lines appended at EOF (1407 → 1423 lines), 0 removals |
| fleet round-72 report pinned | `git -C /home/vgpnk/Projects/shokunin cat-file blob 80d8c9b5…:.ufo/reports/round-72/kotodama.md \| sha256sum` vs `show HEAD:` | both `ea256ae7f9d758e0962a7fdfeea446d8963e3f7ef1314aeacc6a7334509834be` |
| round-71 id map untouched | `git cat-file blob <rev>:.ufo/waves/round-71/assimilation/id-renumber-map.json \| sha256sum` at both ends; `git log base..lands -- <path>` | `dbc60836a5930064…` at both ends, no commit |
| registry append-only | `git diff base lands -- corpus/SOURCES.md` (5+/0), hunk `@@ -828,6 +828,11 @@` | 799 → 804 rows, `S876..S880` at EOF, last id `S875` → `S880`, none removed |
| GROUND's fragment counts are true | `git show 8841ad3:corpus/SOURCES.md \| grep -c -F '<fragment>'` ×5 | `ojs.unito.it` 0, `philol.msu.ru` 0, `journals.rudn.ru` 0, `cyberleninka.ru/article/n/klassifikatsii` 0, `sanders.phonologist.org` 0 |
| map `map` == assignments == claims `row_set` | JSON compare (F2) | equal, no assignment changed |
| Ca counter green at lands | `accept-ca.py --root . --lands 0316b888 --main 0316b888 --fleet-root <fleet>` | `ACCEPT-CA-73: PASS legs=9/9` |
| C counter green at lands-equivalent | `accept-c.py --root . --lands ba99c0e …` (F1 mutant) | `ACCEPT-C-73: PASS legs=11/11` |
| r3 red-before genuine | guard removed from a lands checkout, `--selftest` | `SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'` |

## 4. What I could NOT check

- **The first-grade receipt for the C landing.** The claim that the README/SKILL ids were removed *because a grading run flagged them* rests on the commit message (`README footer without claim-C ids`), `counter-revisions.md:8` ("SEPARABLE red for a separate reason"), and my mutant. The graded run's own output at `e62d731`/`85f17eb` is not committed, so I cannot show the exact pre-edit failure text.
- **Whether the two round-72 seat reports are the seats' original bytes.** No fleet copy, no surviving `/tmp` draft; only in-file hashes that cannot be re-derived.
- **Fleet-repo cleanliness attributable to this lane.** The fleet root is shared with other lanes; I verified only the pinned blob, not that no lane seat wrote elsewhere under `/home/vgpnk/Projects/shokunin/**`.
- **The round-71 map's semantic content.** I verified byte identity only; whether its assignments were right in round 71 is out of scope here.
- **`claims.json`'s EVIDENCE captures, entries' quote fidelity, ledger pair semantics.** Other wave-2 seats' assignments; not re-run.
- **`CENSUS` in the very first mutant run** failed for a harness reason (`fleet_root` defaults to `dirname(root)`; my clone sat one level above a root with no `scripts/`). Re-run with an explicit `--census-sh` → `exit=0 last-line=kotodama ok …/corpus/SOURCES.md`, `LEG PASS CENSUS`. Recorded so the first `legs=10/11` line in F1 is not mistaken for a lane defect.

## 5. Verdict

Append-only holds for every protected byte the round names: `LOG.md`, `SCORECARD.md`, lessons 71/72 and the fleet round-72 report are untouched or appended, and the only base..lands removal (`SHONEN.md:6`) is the item's allowed pointer fix and is correct. Scope holds at the repo boundary (5 commits, one identity, no fleet path, no merge, no deletion).

The two defects worth fixing are not "removed lines" but **who bent to whom**: the SEPARABLE leg enforces a predicate wider than the frozen claim and two true claim-C statements were deleted to satisfy it (F1), and a frozen pre-data artifact was replaced after grading to satisfy COLLCHECK (F2) with no assignment moved. Both are disclosed in the lane's own receipts; neither is a false claim leg at lands. Nothing here is a BLOCKER by the item's definition, because every declared leg is true at `0316b888` and every admitted statement I could test is true of the artifact it cites.
