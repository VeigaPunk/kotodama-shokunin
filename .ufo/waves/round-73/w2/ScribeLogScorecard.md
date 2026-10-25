# ScribeLogScorecard — round 73, wave 2 (falsify), leaf seat

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; base `8841ad3b896a0227674fa0725b818c999118046f`;
lands `0316b8883b4f8d44b8efd720140e7f52f734a102` (tree `9b10fa06a2d3756c8bacfc8fc7b2115921370d97`,
`git rev-parse 0316b8883b4f8d44b8efd720140e7f52f734a102^{tree}`). Claims read first from
`reports/round-73/claims.json` (frozen at `af65165`).

**Seat task.** DRAFT (not land) the `LOG.md` round-73 entry and the `SCORECARD.md`
`## Axes — round 73` section, following the round-72 shapes, stating a fact only after
re-deriving it by a command, marking every claim verdict "author-side, pending non-author
closure", and using no trend scalar. Both drafts are written; every fact in them is re-derived
below. Nothing in the lane was mutated: `git status --porcelain` after my writes shows
`tracked-modified=0` and only the pre-existing untracked `.ufo/waves/round-73/w2*` paths.
All byte-changing experiments ran in a throwaway clone
`/tmp/ScribeLogScorecard/A0DNXb/lane` (created with `git init` + `git clone` + detached checkout
of `0316b88`; `git -C /tmp/ScribeLogScorecard/A0DNXb rev-parse --show-toplevel` =
`/tmp/ScribeLogScorecard/A0DNXb`). No `task` spawn, no background job, no delegation, no write
outside the lane's `w2/drafts/` and this report.

---

## 1. Artifacts produced

| artifact | path |
|---|---|
| LOG.md round-73 entry (append text) | `.ufo/waves/round-73/w2/drafts/log-entry.md` |
| SCORECARD.md `## Axes — round 73` section (append text) | `.ufo/waves/round-73/w2/drafts/scorecard-section.md` |
| this report | `.ufo/waves/round-73/w2/ScribeLogScorecard.md` |

Both drafts are append-only text: they edit nothing above them. The LOG draft adds one bullet the
round-72 entry does not have (`Landed changes by commit`) because the assignment requires every
landed change tied to its commit, and one bullet (`Open at this entry`) carrying findings §3 F1,
F4 and the missing fleet report rather than hiding them. The SCORECARD draft adds a **discernment**
row that the round-72 section omits (see F6).

---

## 2. Facts re-derived (each with the command that produced it)

All commands were run in the clone at `/tmp/ScribeLogScorecard/A0DNXb/lane` (cwd) unless the command
says otherwise.

**F-2.1 Claim C counter — PASS 11/11, sha prefix `95aee881`.**
```
$ sha256sum reports/round-73/accept-c.py
95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416  reports/round-73/accept-c.py
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b88... --census-sh /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES / CENSUS / SCRATCHMIRROR / COLLCHECK
ACCEPT-C-73: PASS legs=11/11
exit=0
```
Header pins `stamped=evaluated=measured=0316b88`, `tree: 9b10fa06a2d3756c8bacfc8fc7b2115921370d97`
(= `git rev-parse 0316b88^{tree}`), `worktree graded: no`. **Caveat, see F3**: the bare declared
command fails outside a fleet layout.

**F-2.2 Claim Ca counter — PASS 9/9, counter r3 sha prefix `222d4dd6`.**
```
$ sha256sum reports/round-73/accept-ca.py
222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89  reports/round-73/accept-ca.py
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b88... --fleet-root /home/vgpnk/Projects/shokunin
PAIR L01..L08 (5 ANNOTATE: L01 L02 L03 L06 L07; 3 REPAIR: L04 L05 L08)
LEG PASS LEDGER (pairs=8 min=8) / BASEMISMATCH (found=8) / REPAIR (green=['L04','L05','L08'] red=[]) /
         ANNOTATE / NOSTUB / APPENDONLY (lane-removed=0 fleet-pin=80d8c9b576d4 blob=ea256ae7f9d7) /
         SEPARABLE / TRACKED / STAMP (stamped=evaluated=measured=0316b888)
ACCEPT-CA-73: PASS legs=9/9
exit=0
```

**F-2.3 Selftests re-run (QUALITY 23 artefacts).**
```
$ python3 -B reports/round-73/accept-c.py --selftest   -> SELFTEST: 29/29   exit=0
$ python3 -B reports/round-73/accept-ca.py --selftest  -> SELFTEST OK: 10 scenarios  exit=0
$ git -C <clone> status --porcelain                    -> (empty: selftest leaves the tree clean)
```

**F-2.4 Registry and knowledge counts (base → lands).**
```
$ git show 8841ad3b:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'   -> 799
$ git show 0316b8883b4f8d44b8efd720140e7f52f734a102:corpus/SOURCES.md | grep -cE ...same...        -> 804
$ git ls-tree -r --name-only 8841ad3b corpus/knowledge | grep -c '\.md$'                            -> 245
$ git ls-tree -r --name-only 0316b888... corpus/knowledge | grep -c '\.md$'                         -> 247
$ git diff 8841ad3b..0316b888 -- corpus/SOURCES.md | grep -E '^[+-]\| *S[0-9]'
  + S876 / + S877 / + S878 / + S879 / + S880   (no removed row line)
$ git show 0316b888:corpus/SOURCES.md | awk -F'|' over S876..S880
  S876..S880: tier=B kind=paper,paper,book,paper,paper status=mined opened=2026-10-25 recheck=180d
  used-by: S876,S877 -> conlang-scholarship.md ; S878,S879,S880 -> ...amend-2026-10-23.md
```

**F-2.5 Ground before-state (0 owners).**
```
$ for f in ojs.unito.it philol.msu.ru journals.rudn.ru cyberleninka.ru/article/n/klassifikatsii sanders.phonologist.org; do
    git show 8841ad3b:corpus/SOURCES.md | grep -c -- "$f"; done   -> 0 0 0 0 0
$ git ls-tree -r --name-only 8841ad3b | grep -c 'conlang-scholarship'                      -> 0
$ git ls-tree -r --name-only 8841ad3b corpus/knowledge | grep -i conlang                   -> 2 files
  (linguistics/conlang-methodology.md, synthesis/conlang-blueprint-template.md)
```

**F-2.6 Census exit 0 at start and end (re-run, not read from the receipts).**
```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
  ... 28 W04 lines ... kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md   exit=0
$ (base materialized: git archive 8841ad3b | tar -x -C /tmp/.../base-mat)
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /tmp/ScribeLogScorecard /tmp/ScribeLogScorecard/base-mat
  ... 28 W04 lines ... base-mat	ok	/tmp/ScribeLogScorecard/base-mat/corpus/SOURCES.md                  exit=0
```
Both ends: exit 0, 28 W04 rows each. The census script is read-only in `validate` mode (its only
writes are inside `selftest`), so running it against the fleet root mutated nothing.

**F-2.7 Wave accounting.**
```
$ ls .ufo/waves/round-73/w1/*.md | wc -l                    -> 34
$ python3 -c "json.load(open('.ufo/waves/round-73/w1/w1-results.json'))"  -> seats: 37, wave: w1, results: 37 names
$ names absent from w1/*.md                                 -> ConnectorSiblings, ScribeMistakes, ExecScratchMirror
$ python3 -c "json.load(open('.ufo/waves/round-73/w1/dispatch.json'))"    -> counts {'spawn': 37, 'total': 37},
                                                               policy waveMinLanes 32 / waveMaxLanes 64
$ role tally from w1/dispatch.json: scout 11, scribe 6, executor 6, critic 5, reviewer 4,
  connector 2, mutation-tester 1, sentinel 1, simplifier 1  -> 37; attack roles 11/37 = 29.7%
$ python3 -c "json.load(open('.ufo/waves/round-73/w2/dispatch.json'))"    -> counts {'spawn': 33, 'total': 33}
```
No policy document sets an attack-role floor: `grep -rn 'attack role' --include='*.md' .ufo/*.md`
→ no hits (the phrase appears only in round reports). Recorded as an observation, not a violation.

**F-2.8 Mistakes M1..M6 and QUALITY 22/23.**
```
$ grep -n '^| R73-M[0-9]' corpus/lessons/round-73.md        -> M1 landing, M2 reference-drift, M3 stale-premise,
                                                               M4 survivor, M5 survivor, M6 scope  (6 rows)
$ grep -n '^2[23]\. \*\*' corpus/QUALITY.md                  -> 22. at :66 (wall/UA binding), 23. at :77 (selftest receipt)
$ git show 85f17eb -- corpus/QUALITY.md                      -> adds criteria 22 and 23
$ git show 0316b8883b4f8d44b8efd720140e7f52f734a102 -- corpus/QUALITY.md -> amends criterion 23 only
```

**F-2.9 Counter-revision history (sha per revision).**
```
$ git show af65165:reports/round-73/accept-ca.py | sha256sum -> f8ebb5d849c9113d...  (r1)
$ git show 3537899:reports/round-73/accept-ca.py | sha256sum -> be1917950bfb992d...  (r2)
$ git show 85f17eb:reports/round-73/accept-ca.py | sha256sum -> 222d4dd6d4082b49...  (r3 = lands)
$ git show af65165:reports/round-73/accept-c.py  | sha256sum -> 95aee88166023f4b...  (r1, unchanged at lands)
```

**F-2.10 Commit→change map used by the LOG draft.**
```
$ git log --format='%h %s' 8841ad3b..0316b8883b4f8d44b8efd720140e7f52f734a102
  af65165 freeze (claims, ledger, counters, controls, selftest, census-start, gap-sweep, evidence, assimilation scratch, 34 w1 reports)
  e62d731 Ca: SCORECARD corrections, SHONEN L04/L05, SKILL seven gate rows, measures-ca72-rerun, round-72 w1 ScoutMergeScan+ScribeLesson
  3537899 Ca: accept-ca r2, counter-revisions, SKILL accept-c-73 row, controls-ca-r2, selftest-r2
  85f17eb C: both entries, SOURCES S876-S880, lesson round-73, QUALITY 22/23, README footer, census-end, accept-ca r3, r3 receipts
  0316b88 C: id-renumber-map, validate-receipt, QUALITY 23, README footer ids, lesson M6, gap-sweep [7]
```
Per-file `git log --diff-filter=A` confirms `claims.json`, `ledger.json`, `evidence/S876..S880.txt`,
`census-start.txt`, `selftest.txt`, `gap-sweep.txt`, `controls-c.txt`, `controls-ca.txt` all enter at
`af65165`; `.ufo/waves/round-72/w1/{ScoutMergeScan,ScribeLesson}.md` enter at `e62d731` (R1).

**F-2.11 Round-72 L06 inputs (so the annotation's own numbers are not taken on faith).**
```
$ grep -E '^LEG FAIL|ACCEPT-CA-72' reports/round-72/telemetry/measures-ca.txt -> LEG FAIL REPORTLAST ; ACCEPT-CA-72: FAIL legs=12/12
$ sha256sum reports/round-72/accept-ca.py -> f080c240ffdc47f0453f4527e23d271112c999dc59d3d63d2703aae10880629f
$ sha256sum /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotodama.md -> ea256ae7f9d758e0962a7fdfeea446d8963e3f7ef1314aeacc6a7334509834be
```
Both match `reports/round-73/telemetry/measures-ca72-rerun.txt`'s headers.

---

## 3. Findings

### F1 — MAJOR: QUALITY 23's required freeze-commit run has no receipt, and `0316b88`'s subject asserts it

QUALITY 23 (`corpus/QUALITY.md:77`) requires "the counter is also run at the FREEZE commit
(receipts present, landing absent) so artifact-vs-leg shape mismatches show before data". No
receipt under `reports/round-73/telemetry/` carries a stamped revision of `af65165`; every control
is stamped at the **base** `8841ad3b`, where the receipts themselves are absent — the exact blind
case the criterion names. The final landing commit's subject nonetheless reads "QUALITY 23
freeze-commit run", and the lesson's own R73-M6 says the shape defects were "first graded against
landed data".

```
$ grep -rn 'af65165' reports/round-73/ | grep -v claims.json
reports/round-73/telemetry/controls-ca-r2.txt:1  (prose: "Ledger committed at af65165 is NOT in the base tree")
reports/round-73/counter-revisions.md:5          (r1 row: "af65165 (freeze)")
$ for f in reports/round-73/telemetry/*.txt; do grep -H '^# stamped revision' "$f"; done
  .../controls-c.txt: 8841ad3b...   .../controls-ca.txt: 8841ad3b...
  .../controls-ca-r2.txt: 8841ad3b...   .../controls-ca-r3.txt: 8841ad3b...
  .../measures-ca72-rerun.txt: 21ad3088...          (no af65165 anywhere)
$ git show --name-only --format='' 0316b88 | grep telemetry
reports/round-73/telemetry/gap-sweep.txt           (no new receipt: the "freeze-commit run" left no bytes)
```

The run was possible and would have caught M6 before data:
```
$ (clone) python3 -B reports/round-73/accept-c.py --root . --lands af65165cf269db346ef872e16a656eccd7264d01 --census-sh .../sources-census.sh
LEG PASS CENSUS
LEG FAIL GROUND          receipt does not name ojs.unito.it; ... philol.msu.ru; ... journals.rudn.ru; ... klassifikatsii; ... sanders.phonologist.org
LEG FAIL SCRATCHMIRROR   receipt does not carry S876, S877, S878, S879, S880
LEG FAIL COLLCHECK       .ufo/waves/round-73/assimilation/id-renumber-map.json has no map object; ...
ACCEPT-C-73: FAIL legs=1/11
exit=1
```
This is precisely the trio the criterion cites as its own evidence. Effect on my drafts: both drafts
state the criterion as landed and carry an explicit "no freeze-commit receipt on file; the run would
have caught M6" line instead of implying the requirement was met. **Escalation note:** if closure
treats `0316b88`'s subject ("QUALITY 23 freeze-commit run") as an admitted statement, this is a
BLOCKER by the seat definition — a recorded statement that the lane's own lesson contradicts. As a
missing artefact it is MAJOR; neither claim C nor Ca turns on it (both counters PASS).

### F2 — MAJOR: the fleet root is not clean of seat artifacts; a round-72-style "no seat wrote to the fleet root" line would be false

The round-72 LOG entry's misroot bullet says the sweep found "no seat wrote to the fleet root this
round ... nothing to relocate". Copying that shape for round 73 would be unsupported: the fleet repo
carries two untracked **seat-report** artifacts whose mtimes fall inside this round's window.

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain | grep '^??'
?? .ufo/waves/round-30/
?? .ufo/waves/round-41/w1/ExecQuarantineSlice.md
$ ls -la --time-style=full-iso .ufo/waves/round-41/w1/ExecQuarantineSlice.md
-rw-r--r-- 1 vgpnk vgpnk 151 2026-10-25 19:58:07 -0300 .ufo/waves/round-41/w1/ExecQuarantineSlice.md
$ cat .ufo/waves/round-41/w1/ExecQuarantineSlice.md
# ExecQuarantineSlice — seat report (w1, round 41)
STATUS: in progress.
Scope: quarantine slice (item 10) derivation + focus-theme row hand-check.
$ ls -la --time-style=full-iso .ufo/waves/round-30/wave1/ScribeLesson.md
-rw-r--r-- 1 vgpnk vgpnk 1521 2026-10-25 15:58:07 -0300 .ufo/waves/round-30/wave1/ScribeLesson.md   ("# Round 30 — scoped lesson assembly report")
```
Both timestamps (18:58Z and 22:58Z) are inside the round-73 window; the second is ~90 s before the
final landing commit (22:59:32Z). Attribution limit, stated: no round-73 seat is named
`ExecQuarantineSlice` — `grep -c ExecQuarantineSlice .ufo/waves/round-73/{w1,w2}/{dispatch,spec}.json`
= 0/0/0/0 and it is absent from the 33 wave-2 registry members — so I cannot prove which process
wrote it; a live peer named `ExecQuarantineSlice-3` exists on the orchestrator roster, and the fleet
tree was restored today at 09:29-03:00 (`f47ad6ba`), which does not explain a 19:58 mtime. What is
provable is the artefact: two untracked seat reports in the fleet repo, one at a wrong-round path.
Effect on my drafts: the LOG draft's misroot bullet reports the 20 paths, names both artefacts and
says nothing was relocated (fleet writes are out of lane scope) — it does not claim a clean sweep.

### F3 — MINOR: the declared claim-C command is fleet-layout dependent (CENSUS leg)

`claims.json` declares `python3 -B reports/round-73/accept-c.py --root . --lands <lands>`. Run in a
clone materialized at `<lands>` outside a fleet root — the QUALITY 19 procedure — the CENSUS leg
cannot find the census script and the claim reads FAIL:
```
$ (bare clone /tmp/.../A0DNXb/lane) python3 -B reports/round-73/accept-c.py --root . --lands 0316b888...
LEG FAIL CENSUS
     census script not found: /tmp/ScribeLogScorecard/A0DNXb/scripts/sources-census.sh
ACCEPT-C-73: FAIL legs=10/11
exit=1
```
The script is resolved from the **realpath parent of `--root`** (a symlinked fleet entry still
resolved to the clone's own parent). In a real fleet layout the declared command passes exactly as
written:
```
$ (real clone at /tmp/.../fleet2/kotodama-shokunin, /tmp/.../fleet2/scripts -> fleet scripts)
LEG PASS CENSUS   exit=0 last-line=kotodama	ok	/tmp/r73-fleet-vfnlu9dj/kotodama-shokunin/corpus/SOURCES.md
ACCEPT-C-73: PASS legs=11/11
```
So the fact "PASS legs=11/11" is true as declared, but a re-opener following the clone instruction
gets a false red unless they add `--census-sh` (the override exists and works). Both drafts carry the
caveat in the re-run cell.

### F4 — MINOR: `counter-revisions.md`'s table is broken; r2's sha sits outside its own row

QUALITY 23 requires a counter revision to record "old sha, new sha". r2's row records a placeholder
instead, and the r3 row is orphaned below prose, so the table renders two rows short:
```
$ cat -n reports/round-73/counter-revisions.md | sed -n '3,13p'
 3  | rev | file | sha256 | when | change | predicate |
 4  |---|---|---|---|---|---|
 5  | r1 | ... | f8ebb5d8... | af65165 (freeze) | as frozen | unchanged |
 6  | r2 | ... | see `sha256sum` below | after the Ca landing commit e62d731 was first graded | BUG FIX: ... |
 8  r1 receipt that exposed the bug ... ACCEPT-CA-73: FAIL legs=8/9 ...
 9  be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0  reports/round-73/accept-ca.py
11  | r3 | ... | 222d4dd6... | before the claim-C landing commit | ...
```
The values are correct (F-2.9 re-derived all three shas); the shape is not. Both drafts cite the
revisions from the re-derived shas, not from the table, and the LOG draft records the defect.

### F5 — MINOR: the census receipts carry no row count, though `claims.json` cites them for "799 rows"

`claims.json` `frontier_step.census_start` reads "reports/round-73/telemetry/census-start.txt (exit
0, 799 rows)". The receipt shows exit 0 and 28 W04 rows; it never prints a registry row count:
```
$ head -3 reports/round-73/telemetry/census-start.txt
# census-start round 73 — base 8841ad3b... — 2026-10-25T22:01:18Z
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	W04	S127 duplicate url ...
$ grep -c 'rows' reports/round-73/telemetry/census-start.txt   -> 0
```
The 799 is true (F-2.4, re-derived from the base registry) but is not evidenced by the file it is
attributed to. Both drafts state "census exit 0 at start and end (28 W04 each)" and derive the row
counts from the registry, not from the receipts.

### F6 — MINOR: the round-72 SCORECARD shape I was told to follow omits the discernment axis, and the axes series has no round-70/71 sections

```
$ grep -n '^## Axes — round 7[0-3]\|^## Corrections — round 7[0-3]' SCORECARD.md
1374:## Corrections — round 70 ...
1397:## Axes — round 72 ...
1409:## Corrections — round 73
```
`LEARNING.md:25-38` names three trends (expansion, quality, discernment) and requires "one verdict
each, every round"; the round-72 section's rows are calibration, coverage, and
"depth / quality / operability / freshness / adjacency" — no discernment row — and no axes section
exists for rounds 70 or 71. My draft keeps the table shape and adds the discernment row
(`unchanged at report time`, with the absent `round-73-verifier-spotcheck.md` and
`CritTrendObservables` §2 D1/D2 as evidence). Verdicts were taken from the wave-1 trend seat's
pre-declaration, not invented: expansion `improved`, quality `unchanged`, discernment `unchanged` at
report time, calibration as an axis row.

### F7 — MINOR: the selftest receipts embed two unlabelled `ERROR:` lines inside an OK verdict

`selftest-r2.txt` / `selftest-r3.txt` show, between the Ca invocation and `SELFTEST OK`, the lines
`ERROR: --lands must be 40 hex` and `ERROR: base 8841ad3b... is not a commit in /tmp/r73-ca-selftest-.../lane`.
They are deliberate negative scenarios (`accept-ca.py:1306-1362`: the worktree-only-ledger scenario
and the CLI input-error scenario), and the selftest genuinely passes (re-run: `SELFTEST OK: 10
scenarios`, exit 0). The receipt does not label them, so a reader can mistake them for a failing run.
Both drafts cite the re-run verdict, not the receipt's raw interleaving.

### F8 — MINOR: the lesson's "see the fleet report" pointers dangle

`corpus/lessons/round-73.md:7` and the sibling-overlap note point at the fleet report; it does not exist:
```
$ ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-73/
audio.md   game-dev-3d.md            (dated 2026-10-13/14; no kotodama.md)
$ ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-73/kotodama.md
ls: cannot access '.ufo/reports/round-73/kotodama.md': No such file or directory
```
Not my item's bytes, but my LOG draft must not repeat the pointer: it names the absence instead and
carries the wave accounting from `dispatch.json` / `w1-results.json` directly.

### Observations that are NOT findings (checked, true)

- Both counters' verdicts, leg counts and sha prefixes are exactly as declared (F-2.1, F-2.2); the
  C header's tree hash equals the lands tree (F-2.1); STAMP holds (stamped = evaluated = measured).
- Ledger: 8 pairs, 8/8 red at base, 5 ANNOTATE rows + 3 REPAIR pairs; the corrections table carries
  5 `| L0x |` rows and each names id + old token + new token + re-derivation command
  (`sed -n '1409,1423p' SCORECARD.md | grep -c '^| L0'` → 5).
- APPENDONLY: lane-removed = 0 over LOG/SCORECARD/lessons 71-72; the only in-place files are
  `SKILL.md` (registry) and `corpus/README.md` (footer), both ledger-named.
- Registry/knowledge counts, tier/status/opened/recheck/used-by cells, ground fragments at base,
  census exit 0 at both ends, wave accounting (37/34/3 + 33), M1-M6, QUALITY 22/23 landing commits,
  and the r1→r2→r3 shas are all re-derived above.
- The round-72 L06 inputs (receipt FAIL, counter sha, fleet blob) match the round-73 annotation and
  rerun receipt (F-2.11), so the annotation is not a laundered claim.

---

## 4. What I could NOT check

- **No live fetch.** I re-opened no source and sent no HTTP request: the Gate quotes, the five
  `evidence/S87*.txt` captures (status, bytes, sha256, "quote-found-verbatim") and the wall/429
  records were not re-measured by this seat. I verified only that the evidence files exist at
  `af65165` and that the counter's EVIDENCE leg passes on them. Quote word caps, the S879 CDX
  "no capture" ruling, and the Springer/Cambridge UA records are other seats' attack surface.
- **Whether the freeze-commit run happened off-record.** I can prove no receipt exists and that the
  run would have caught the three shape legs; I cannot prove the L1 never ran it in a shell.
- **Provenance of the two untracked fleet artifacts** (F2): the dispatch bytes do not name a
  round-73 seat that could have written them.
- **Tool installs by other seats this round:** no install receipt exists under `reports/round-73/`;
  nothing on file, so both drafts say "none on file", not "none happened".
- **Stale-lane / other open mission:** not inspected; the LOG draft says so rather than claiming
  "none".
- **Wave-2 outcomes:** in flight (33 seats); nothing in either draft depends on them.
- **The Gate's substantive judgements** (admit/reject correctness, tier assignments): out of this
  seat's item; my drafts cite them as the lesson's record, with the lesson's own reasons.

## 5. Hygiene / tooling

- No tool installed, upgraded or downloaded. No `pacman` invocation. No `task` spawn, no background
  job. Nothing fetched from the network.
- Clone: `/tmp/ScribeLogScorecard/A0DNXb` (and `/tmp/ScribeLogScorecard/fleet2`, `base-mat`,
  `census-*-rerun.txt` under the same directory). Nothing written to the fleet repo, the lane's
  tracked bytes, `shokuknow`, or any sibling lane. Lane after my writes: `tracked-modified=0`.
