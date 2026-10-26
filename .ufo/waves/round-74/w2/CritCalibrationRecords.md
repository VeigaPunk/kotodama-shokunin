# CritCalibrationRecords — round 74 / wave 2 (falsify): self-assessment vs repo state

**Attack.** For every count, path, hash, row id and pass/fail assertion in the round's *own new bytes*
(`corpus/lessons/round-74.md`, the new `corpus/README.md` Round-74 block/footer, the `SCORECARD.md`
`## Corrections — round 74` rows, the `SKILL.md` gate rows, `corpus/QUALITY.md` 25, plus `LOG`/`SHONEN` and the frozen
`claims.json`/`ledger.json` they rest on), compare the stated value with what the tree actually holds.

**Method (read-only).** Isolated clone: `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/CritCalibrationRecords/lane`,
then `git branch -f main <lands>` *inside the clone only*. Revisions used:

| role | revision |
|---|---|
| base | `f7104cbce186bc2e1522abf0cfd619cc834628bb` |
| operative freeze F3 | `00c408a0af2fa5ddf65af2224152ce258b26d896` |
| claim Ca lands | `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3` |
| claim C lands | `c4bf61a8d722f9168ce0fd8021a6261c000610c5` |
| round head at dispatch | `1d7add3f7b9eaf6f3349c56c36f6d06325d74236` |

Counters run in the clone, each at its own lands:
`accept-c.py` at `c4bf61a` → `ACCEPT-C-74: PASS legs=13/13`, exit 0;
`accept-ca.py` at `5e4796c` → `ACCEPT-CA-74: PASS legs=11/11`, exit 0.
Both selftests run: `accept-c.py --selftest` → `SELFTEST: 69/69 scenarios`, exit 0;
`accept-ca.py --selftest` → `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0`, exit 0.
No tool was installed; no byte was written under `/home/vgpnk/Projects/shokunin/**` except this report.

**Verdict on the axis.** Neither claim fails as declared *at its own lands*. Calibration (Ca) nevertheless does not
survive this attack as a *record*: the round's new bytes contain **15 stated-vs-observed mismatches (2 HIGH, 5 MEDIUM,
8 LOW)**, including a frozen status line that is false about its own freeze commit, a gate row that pins a counter
sha256 that exists nowhere in the tree, and a Ca counter that is red at the round's own final tree.

---

## A. Required-item calibration table

`stated_at` cites the file:line at the round head (`1d7add3`), which is also claim C's lands content for these files.

| # | stated_at | stated | observe command | observed | match |
|---|---|---|---|---|---|
| 1 | lessons/round-74.md:3-9 | "40 staged knowledge files triaged" | `find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge -type f -name '*.md' \| wc -l` | 40 | Y |
| 1b | :3 | "two v1 waves"; the claims line states no seat count | `ls -d .ufo/waves/round-74/w1 .ufo/waves/round-74/w2`; `head -2 .ufo/waves/round-74/build-w2.py` | both dirs exist (44 w1 files, 43 w2 entries); builder docstring "Builds the round-74 wave-2 (falsify) spec" | Y (no seat count is claimed anywhere in the new bytes) |
| 2 | :4 | "at base 804 registry rows" | `git grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' f7104cb -- corpus/SOURCES.md` | `f7104cb…:corpus/SOURCES.md:804` | Y |
| 3 | :4 | "0 `*worldbuilding-setting*` files" | `git ls-tree -r --name-only f7104cb -- corpus/knowledge \| grep -c worldbuilding-setting` | 0 | Y |
| 4 | :5 | "247 knowledge files" | `git ls-tree -r --name-only f7104cb -- corpus/knowledge \| grep -c '\.md$'` | 247 | Y |
| 5 | :5 | "0 registry hits for litmemo/tuduku/chinawriter" | `git show f7104cb:corpus/SOURCES.md \| grep -cE 'litmemo\|tuduku\|chinawriter'` | 0 | Y |
| 6 | :6-7 | "four rows S881–S884 … two entries admitted" | `grep -c '^\| S88[1-4] ' corpus/SOURCES.md`; `find corpus/knowledge -name 'worldbuilding-setting-practice*.md' \| wc -l` | 4 rows; 2 files | Y |
| 7 | :7 | "accept-c.py printing `ACCEPT-C-74: PASS legs=13/13` at lands" | clone at `c4bf61a`, counter run | `ACCEPT-C-74: PASS legs=13/13`, exit 0 | Y |
| 8 | :7-8 | "13 ledger pairs (1 REPAIR, 12 ANNOTATE)" | `ledger.json` `pairs[].disposition` | 12 ANNOTATE + 1 REPAIR (`LC-09`) | Y (but see F4) |
| 9 | :8 | "6 must_track pins" | `len(ledger["must_track"])` + sha256 of each path | 6; all six sha256 equal the pinned values | Y |
| 10 | :8 | "accept-ca.py printing `ACCEPT-CA-74: PASS legs=11/11`" | clone at `5e4796c`, counter run | `ACCEPT-CA-74: PASS legs=11/11`, exit 0 | Y at Ca lands; **N at head** (F3) |
| 11 | :9 | freeze `00c408a0…`; earlier freezes `de93d91c…`, `3595c919…` (R74-M9) | `git rev-parse --verify <rev>^{commit}` | all three exist | Y |
| 12 | :18-22 (Gate) | 5 rows, access 2026-10-25, sizes/sha256/windows 1055723/e512a20d, 101615/441fc921, 17068/754f504c, 48536/a3b6640c, 62604/344de345; windows 4098/4098/2953/4104/4103 | `head -8 reports/round-74/evidence/S87*.txt reports/round-74/evidence/S88*.txt` | every size, sha256 and `window: chars=` identical | Y |
| 13 | :26 | "sentence is 108 characters and 15 whitespace tokens; cell carries the 54-character first clause (7 tokens)" | measure evidence `locator:` sentence and Gate cell | 108 / 15; 54 / 7 | Y (but F13 on *which field*) |
| 14 | :27 | "631 before + 33 quote + 2289 after = 2953" | `grep '^window:' evidence/S882.txt` | `chars=2953 … before=631 after=2289` | Y |
| 15 | :28 | round-73 `S877.txt` "one collapsed paragraph, 1564 B" | `wc -c`; longest line of `reports/round-73/evidence/S877.txt` | file 2417 B; paragraph 1614 B (893 chars) | **N** (F12) |
| 16 | :40 | "2 adopted / 4 path-present … / 34 refused … of the 40" | staged package counts | 2 + 4 + 34 = 40 | Y |
| 17 | :47-53 | family counts 5 / 11 / 3 / 2 / 9 / 3+1 | `find … -name '<family>*'` per family; `find …/verification` | 5 / 11 / 3 / 2 / 9 / 3+1 = 40 | Y |
| 18 | :60-63 | `reg-ids` 804 S001…S880 `94a495c7…`; `staged-ids` 132 S859…S990 `bab11d7d…`; `collisions` 22 S859…S880 `130ec2d1…` | `wc -l` + `sha256sum` on the three files | 804 / 132 / 22; hashes identical | Y |
| 19 | :67 | map sha256 `d3573f7d…aeb24afa` | `sha256sum .ufo/waves/round-74/assimilation/id-renumber-map.json` | `d3573f7d3cf23afa7296c281d201225eed643aef2b406b3a403c2a67aeb24afa` | Y |
| 20 | :78-79 | "single pass yields `S877`×4 and `S881`×4/`S882`×4 in the base entry and `S883`×3/`S884`×3 in the amend" | `grep -o 'S[0-9][0-9][0-9]'` on the staged entries | staged base: S882×4, S883×4, S884×4; staged amend: S899×3, S900×3 | Y |
| 21 | :84-86 | S877 used-by old / new | `awk` cell 11 of row S877 at base and lands | `…/linguistics/conlang-scholarship.md` → same + `, …/culture-material/worldbuilding-setting-practice.md` | Y |
| 22 | :113-116 | mirror holds "the two draft entries (sha256 `658a8fa4…9986b00b` and `bb5504e2…d80d8673e`), and a mirrored registry … sha256 `81fcebe1…f2f326`" | `sha256sum .ufo/waves/round-74/assimilation/validate/corpus/knowledge/culture-material/worldbuilding-setting-practice*.md .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md` | `465051db…`, `0b2e06dc…`, registry `c8da0a5a…` (808 rows) | **N** (F6) |
| 23 | :119 | SCRATCHMIRROR sequencing clause "is not exercised by a leaf seat and stays owed" | SCRATCHMIRROR leg in the counter run at `c4bf61a` | `LEG PASS SCRATCHMIRROR` (leg enforces receipt-before-append via `is_ancestor`) | **N** (F7) |
| 24 | :153-157 | "21 slice rows (18 payload-absent + 3 unreachable-class)"; PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 | `awk` verdict column of `reports/round-71/telemetry/quarantine-verdicts.md`; row count | 10 / 7 / 4 = 21 | Y |
| 25 | :130-136 | "byte-identical to the committed round-71 captures (`s816.html` 48536 B `a3b6640c…`; `s817.html` 62604 B `344de345…`)" | `wc -c` + `sha256sum` `.ufo/waves/round-71/assimilation/fetches/s81{6,7}.html` | 48536 / `a3b6640c…bee94d`; 62604 / `344de345…d3d659` | Y |
| 26 | :168-177 | Mistakes states, incl. M3 and M4 "pending landing" | tree at head | M3's junk receipts and M4's SCORECARD rows both landed | **N** (F8) |
| 27 | :199-200 | "M4 `SHONEN.md:6` still says '412 …' (a REPAIR…)"; "`SKILL.md:594` civilizations '94' vs 95 files" | `git diff f7104cb..c4bf61a -- SHONEN.md`; `sed -n 594p SKILL.md` | SHONEN unchanged (still 412); SKILL:594 = "95 entries: 93" | **N** (F4/F9) |
| 28 | :181-185 | census before exit 0 / 804 rows; after exit 0 / 808 rows; W01×3, W04×28 | `tail`/`grep` of `telemetry/census-{start,end}.txt` | `exit=0` both; 804 → 808; W01 on S881, S882, S884 (3); W04 count 28 | Y |
| 29 | SCORECARD.md:1436-1449 | 12 `LC-*` rows, each id + old token + new token + re-derivation command; counter re-runs them | run all 10 distinct `rederive` commands | 804; 10; 247; 32; `decompress -> 23443 -> 97656 bytes`; `HAS two status-200 Wayback captures`; 724; `wall present ("Client Challenge")`; 728; 701 | Y |
| 30 | SCORECARD.md:1438 | "Append-only record … each row carries … which the counter re-runs" | `LEG PASS ANNOTATE … rows=14 annotate-pairs=12 unannotated=0` | 12 data rows + header + separator = 14 lines; 0 unannotated | Y |
| 31 | SKILL.md:594 | "95 entries: 93 earlier-civilization bases plus two source maps" | `find corpus/knowledge/civilizations -maxdepth 1 -name '*.md' \| wc -l` | 95 | Y |
| 32 | SKILL.md:705 | accept-c-74 PASS 13/13 / FAIL n/13 / refused `legs=0/13` / `lands==freeze` graded | counter runs at lands, base, freeze | 13/13; refused on base (`legs=0/13`, exit 2); freeze graded `FAIL legs=4/13`, exit 1 | Y |
| 33 | SKILL.md:706 | accept-ca-74 PASS 11/11 / REFUSED `legs=0/11` | counter runs at Ca lands and base | 11/11; base `FAIL legs=0/11 (REFUSED: --lands equals the frozen base …)`, exit 2 | Y |
| 34 | SKILL.md:706 | selftest "measured at counter sha256 `76d00b88325f…`: exit 0, `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`" | `sha256sum reports/round-74/accept-ca.py`; `accept-ca.py --selftest` | sha256 `8052f1e2…`; `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` | **N** (F2) |
| 35 | SKILL.md:706 | "the ten allowlisted observe executables" | `OBSERVE_ALLOW` in `accept-ca.py:166-167`; ledger R2 | 9 (`git, grep, wc, sha256sum, ls, cat, head, tail, cut`) | **N** (F11) |
| 36 | SKILL.md:707 | round-73 shas: accept-c `95aee881…`, accept-ca r3 `222d4dd6…`, freeze bytes `f8ebb5d8…` print 9, r3 prints 10; c-73 PASS only with census named; ca-73 PASS only with `--main` | `git show <rev>:reports/round-73/accept-{c,ca}.py \| sha256sum`; `sed -n 6p reports/round-73/telemetry/selftest-r3.txt` | `95aee881…`; `222d4dd6…`; `f8ebb5d8…`; `SELFTEST OK: 10 scenarios` | Y |
| 37 | QUALITY.md:81-84 | criterion 25(b): "The freeze commit carries `counters/junk-fixtures.py` and four receipts … `junk-c.txt` (J1–J3), `junk-ca.txt` (J4, J4b, J5–J7), `controls-c.txt` and `controls-ca.txt`" | `git ls-tree -r --name-only 00c408a -- reports/round-74/telemetry` | 8 files, **no** `junk-c.txt`, **no** `junk-ca.txt` | **N** (F1) |
| 38 | QUALITY.md:84 table | fixtures J1–J7 with named legs | `grep '^fixture:' telemetry/junk-c.txt telemetry/junk-ca.txt` | junk-c: J1,J2,J3,J9; junk-ca: J4,J4b,J5,J6,J7,J8,J9 | **N** (F10) |
| 39 | QUALITY.md:88-96 | one-liner exits: accept-c 0, accept-ca 0, round-73 c 1, round-73 ca 1 | run the four one-liners | 0, 0, 1, 1 | Y |
| 40 | QUALITY.md:88-96 | counter sha256 pins `8d30487f…` / `8052f1e2…` | `sha256sum` of the two counters | identical | Y |
| 41 | README.md:445-446 | one row per adopted entry under the culture-material section | `grep -n 'worldbuilding-setting-practice' corpus/README.md` | rows at 445 (amend) and 446 (base) | Y |
| 42 | README.md:733-745 | "0 filename owners and 0 registry rows" at `f7104cb` | `git ls-tree`/`git grep` at base | 0 / 0 | Y |
| 43 | README.md:806 | "the live directory holds 40 files and the section 38 rows"; "Two culture-material files remain unindexed … `heritage-taxonomy-models.md` and `heritage-taxonomy-models.amend-2026-10-24-r13.md`" | `find …/culture-material -name '*.md' \| wc -l`; count `^- \`` rows in the section; set-difference of files vs index rows | 40 files; 38 rows; exactly those two files unindexed | Y |
| 44 | README.md:806-808 | "Registry: 804 -> 808 rows (four new rows, S881-S884 …)" | base/lands row counts | 804 → 808 | Y |
| 45 | README.md:813-817 | "Total knowledge entries: 249"; totals 32/29/40/29/24/95; older footers byte-identical | `find`; `git diff f7104cb..head -- corpus/README.md` | 249; 32/29/40/29/24/95; older footer lines unchanged | Y |
| 46 | lessons/round-74.md:175 (M8) | `SELFTEST: 69/69 scenarios`; `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` | both `--selftest` runs | identical | Y |
| 47 | claims.json `axes_note` | one freshness-pause disposition sentence | `axes_note.count("The freshness pause is a lane-filed L0 disposition")` | **5** | **N** (F14) |

---

## B. Findings

### F1 — HIGH — the frozen status line and QUALITY 25(b) claim the freeze commit ships the junk-landing receipts; it does not

*Stated* (`reports/round-74/claims.json` `status`, frozen in `00c408a`):
> "frozen by the commit that adds this file together with ledger.json, id-renumber-map.json, both counters, the six
> inherited round-73 w2 files and the do-nothing and junk-landing controls"

and `corpus/QUALITY.md:84` (criterion 25(b), binding from round 74):
> "The freeze commit carries `counters/junk-fixtures.py` and four receipts under `reports/round-<N>/telemetry/`:
> `junk-c.txt` (J1–J3), `junk-ca.txt` (J4, J4b, J5–J7), `controls-c.txt` and `controls-ca.txt`."

*Observed*:

```
$ git -C …/kotodama-shokunin ls-tree -r --name-only 00c408a0af2f -- reports/round-74/telemetry
reports/round-74/telemetry/accept-c-73-at-lands.txt
reports/round-74/telemetry/accept-ca-73-at-lands.txt
reports/round-74/telemetry/census-start.txt
reports/round-74/telemetry/controls-c.txt
reports/round-74/telemetry/controls-ca.txt
reports/round-74/telemetry/gap-sweep.txt
reports/round-74/telemetry/selftest-c.txt
reports/round-74/telemetry/selftest-ca.txt

$ git log --oneline --diff-filter=A -- reports/round-74/telemetry/junk-c.txt reports/round-74/telemetry/junk-ca.txt
1d7add3 round-74: junk-landing receipts, measured receipts at each claim's own landing, wave-2 builder

$ head -3 reports/round-74/telemetry/junk-ca.txt
# junk-ca.txt — round 74 junk-landing controls … generator sha256 ce6505fc…; freeze 00c408a0af2f…
# generated: 2026-10-26T01:53:19Z
```

`counters/junk-fixtures.py` **is** in the freeze; the two junk receipts and the two `measures-{c,ca}.txt`
receipts are not — they land in `1d7add3`, after both claims' lands (`5e4796c`, `c4bf61a`) and after the lesson commit.
So criterion 25(b) is violated by the very freeze it describes, and the frozen `status` is false about its own commit.

*Smallest safe correction.* The freeze blob cannot be edited (FROZENCFG pins it). Append one dated line to
`corpus/lessons/round-74.md` (append-only-safe) recording: "the freeze commit 00c408a carries `junk-fixtures.py` and
the controls/selftest receipts only; `junk-c.txt`, `junk-ca.txt`, `measures-c.txt`, `measures-ca.txt` landed in
1d7add3, measured against the frozen counter" — and either satisfy 25(b) in a successor round or restate 25(b) as
"the round's receipts, shipped before the falsify wave", not "the freeze commit carries". Do not report the
freeze-content clause as satisfied.

### F2 — HIGH — the `accept-ca-74` gate row pins a counter sha256 and selftest counts that exist nowhere in the tree

*Stated* (`SKILL.md:706`):
> "`python3 -B reports/round-74/accept-ca.py --selftest` — measured at counter sha256 `76d00b88325f…`: exit 0,
> `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`; receipt `reports/round-74/telemetry/selftest-ca.txt`"

*Observed*:

```
$ sha256sum reports/round-74/accept-ca.py
8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f  reports/round-74/accept-ca.py
$ git show 00c408a0af2f:reports/round-74/accept-ca.py | sha256sum
8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f  -
$ sha256sum .ufo/waves/round-74/counters/accept-ca.py
8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f  .ufo/waves/round-74/counters/accept-ca.py
$ python3 -B reports/round-74/accept-ca.py --selftest
… SELFTEST OK: 179 checks across 41 scenarios reported-fail=0: … (exit 0)
$ grep -c 'SELFTEST OK: 179 checks across 41 scenarios' reports/round-74/telemetry/selftest-ca.txt
1
$ grep -rn '76d00b88' . | grep -v SKILL.md
.ufo/waves/round-74/w1/ScribeQuality25.md:234: | `.ufo/waves/round-74/counters/accept-ca.py` | sha256 `76d00b88…`; …
.ufo/waves/round-74/w1/ScribeSkillGates.md:165: | … `--selftest` (sha `76d00b88…`) | 0 | `SELFTEST OK: 138 checks across 37 scenarios …`
```

`76d00b88…` is a pre-freeze draft counter sha (wave-1 reports only); the installed counter is `8052f1e2…` and prints
179/41, which the round's own lesson (R74-M8, `round-74.md:175`) and the committed receipt both report. The two new
byte sets therefore contradict each other. This is the class criterion 25(c) itself names: a counter's documentation
whose counts do not match the shipped counter is not calibrated.

*Smallest safe correction.* Replace the cell's numbers in `SKILL.md:706` with `8052f1e25c36…` and
`SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` (the gate row is part of this round's mutable bytes;
no leg reads it), or append a correction row; do not leave the false pin.

### F3 — MEDIUM — the Ca counter is red at the round's own final tree; `PASS 11/11` is only reproducible at the intermediate Ca lands

```
$ # clone, local main = 5e4796c
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-CA-74: PASS legs=11/11          (exit 0)

$ # same clone, local main = c4bf61a (claim C lands)
ACCEPT-CA-74: FAIL legs=10/11          (exit 1)
LEG FAIL APPENDONLY
     … repair-stated_at={'SKILL.md': [594]} must_track-exempt=6
     problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']

$ # local main = 1d7add3 (round head at dispatch)
ACCEPT-CA-74: FAIL legs=10/11          (exit 1)
LEG FAIL APPENDONLY
     problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
```

Cause: claim C's landing makes the S877 in-place `used-by` edit at `corpus/SOURCES.md:832`, which claim Ca's
APPENDONLY rule allows only for "the stated_at lines of REPAIR pairs plus appended lines". The two claims' rules are
not composable: the calibration record goes red one commit after its own `after` sentence is written, and nothing in
`round-74.md`, `SCORECARD.md` or the README names `5e4796c` as the revision at which "Ca 11/11" holds. A reader
following the documented command at the landed tree gets a FAIL.

*Smallest safe correction.* Append the disclosure ("Ca 11/11 is measured at the Ca lands 5e4796c; the C landing's
S877 registry cell turns APPENDONLY red at c4bf61a, which is a successor round's allowlist question") to the lesson,
and in a successor add "the registry cells claim C is allowed to change" to the Ca in-place allowlist rather than
widening APPENDONLY silently.

### F4 — MEDIUM — LC-01 carries two authorities and a repair edit that never happened

*Stated, three ways at the round head:*

* `ledger.json` `pairs[LC-01].disposition` = `ANNOTATE`, and `SCORECARD.md` carries row `LC-01` (412 → 804,
  `git grep -c -E '^. S[0-9]{3}' f7104cb -- corpus/SOURCES.md`) — this is the shape the lesson's count sentence
  "13 ledger pairs (1 REPAIR, 12 ANNOTATE)" describes.
* `ledger.json` `repair_edits[0]` = LC-01, with `old_line`/`new_line` for `SHONEN.md:6` and
  `must_hold: "Line 6 is the only changed SHONEN.md line"`.
* `round-74.md:199-200` (Routed to round 75): "M4 `SHONEN.md:6` still says '412 rows after round 56' against 804 rows
  (a REPAIR, since SHONEN is not append-only)".

*Observed:*

```
$ git diff --stat f7104cb..c4bf61a -- SHONEN.md
(empty)
$ git show c4bf61a:SHONEN.md | sed -n '6p' | cut -c100-170
sources registered in `corpus/SOURCES.md` (412 rows after round 56 — 367 mined, 35 queued, 10 rejected …
```

No SHONEN line changed at any revision (`1d7add3` included). So the frozen ledger schedules an in-place repair whose
`must_hold` premise is false at lands, the SCORECARD closes the pair as an annotation, and the lesson routes it to
round 75 as a REPAIR. A reader cannot tell whether `412` was repaired or annotated.

*Smallest safe correction.* Append a correction to the lesson recording LC-01 as annotated-only (the `repair_edits`
entry is unapplied and is not a second disposition), remove SHONEN from the RP75 REPAIR list, and let round 75 either
open a new REPAIR pair with its own `stated_at` or drop the edit. Do not edit the frozen ledger.

### F5 — MEDIUM — the Ca do-nothing control's stated red set is wrong: RECEIPTS is green

*Stated* (frozen `claims.json`, Ca `do_nothing_control`):
> "(1) lands == <freeze> FAILS with REPAIR, ANNOTATE, RECEIPTS red and FROZENCFG/LEDGER green"

*Observed* (`reports/round-74/telemetry/controls-ca.txt`, the lands version; the file was rewritten at `5e4796c` to
re-measure at the operative freeze):

```
LEG FAIL REPAIR
LEG FAIL ANNOTATE
LEG FAIL NOSTUB
LEG FAIL SEPARABLE
LEG PASS RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=[]
     NOTE lands == freeze: do-nothing control shape; the strict-ancestor requirement is not applied to this run and a PASS is refused
ACCEPT-CA-74: FAIL legs=7/11
```

RECEIPTS cannot be red at `lands == freeze` because the receipt and the round-73 lands it re-executes are both in the
freeze tree. `git diff 00c408a 5e4796c -- controls-ca.txt` flips only BASEMISMATCH and APPENDONLY (5/11 → 7/11), so
the expectation was wrong from the first freeze, not introduced by the re-measure.

*Smallest safe correction.* Append the actual red set (REPAIR, ANNOTATE, NOSTUB, SEPARABLE) to the lesson/SCORECARD
record and state that RECEIPTS' teeth are the selftest scenarios (`typed-receipt`, `receipt-wrong-rev`,
`receipt-missing`), not this control.

### F6 — MEDIUM — the lesson's scratch-mirror hashes describe bytes that are not in the tree

*Stated* (`round-74.md:113-116`): "`assimilation/validate/` holds … the two draft entries (`sha256 658a8fa4…9986b00b`
and `bb5504e2…d80d8673e`), and a mirrored registry … `sha256 81fcebe1…f2f326`".

*Observed:*

```
$ sha256sum .ufo/waves/round-74/assimilation/validate/corpus/knowledge/culture-material/worldbuilding-setting-practice*.md
465051db89ef9e77b9e24e0ec4f95d50610c72596b071d13505fcdaaba0e65fc  …/worldbuilding-setting-practice.md
0b2e06dcd9638ab181ef61126bb5199165e9fa1f211184de7591dcb0b2790d31  …/worldbuilding-setting-practice.amend-2026-10-23.md
$ sha256sum .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md
c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614
$ grep -c '^| S[0-9]' …/validate/corpus/SOURCES.md   # row count of the mirror
808
$ grep -rl 81fcebe1 .ufo reports corpus
.ufo/waves/round-74/assimilation/validate-receipt-draft.txt
.ufo/waves/round-74/w1/ExecScratchMirror.md
.ufo/waves/round-74/drafts/round-74.md
corpus/lessons/round-74.md
```

The mirror was re-cut with the final drafts; the committed `validate-receipt.txt` records `465051db…`/`0b2e06dc…` and
registry `c8da0a5a…`. `81fcebe1…` survives only as a recorded fact in the DRAFT receipt. The lesson's present-tense
"holds" is false at lands, and neither `658a8fa4…` nor `bb5504e2…` matches any file.

*Smallest safe correction.* Append: "the mirror was re-cut with the final drafts (465051db…/0b2e06dc…, registry
c8da0a5a…); the draft receipt retains 81fcebe1…/658a8fa4…/bb5504e2… as its own dated measurement."

### F7 — MEDIUM — the lesson says the SCRATCHMIRROR sequencing clause "stays owed"; the counter enforces it and it passes

*Stated* (`round-74.md:119`): "The claim's 'commit strictly before the registry-append commit' sequencing clause is
not exercised by a leaf seat and stays owed."

*Observed.* `reports/round-74/accept-c.py:1477-1518` (`leg_scratch_mirror`) locates the first registry-append commit
in `base..lands`, then requires the receipt's first commit to be an ancestor of it. At `c4bf61a` the leg prints
`LEG PASS SCRATCHMIRROR`; `validate-receipt.txt` is in the freeze tree `00c408a`, and the S881 append is in
`d7a3840`, so `is_ancestor(00c408a, d7a3840)` holds. The clause is satisfied, not owed.

*Smallest safe correction.* Append the correction and drop the owed item from RP75 (do not carry a satisfied clause
forward as debt).

### F8 — LOW — M3 and M4 state "pending landing" after both fixes landed

* `round-74.md:170` (M3) ends `| pending landing |`, but `junk-c.txt`/`junk-ca.txt` landed in `1d7add3` and show
  `LEG FAIL` on each fixture's named leg.
* `round-74.md:171` (M4) ends `| pending landing |`, but the LC-02/LC-03 SCORECARD rows landed in `5e4796c` — an
  ancestor of the lesson's own first landing commit `d7a3840` — and `LEG PASS ANNOTATE … unannotated=0` re-runs both
  re-derivations.

*Smallest safe correction.* Append the state corrections (the lesson is append-only; do not edit the cells).

### F9 — LOW — the round routes to round 75 a defect it repaired itself

`round-74.md:200` (RP75 #3) lists "`SKILL.md:594` civilizations '94' vs 95 files". LC-09 is this round's REPAIR pair
and `SKILL.md:594` at lands reads "- `corpus/knowledge/civilizations/` — 95 entries: 93 earlier-civilization". The
routed item is already closed.

*Smallest safe correction.* Append a correction removing the SKILL:594 item from RP75.

### F10 — LOW — QUALITY 25(b)'s fixture list is incomplete against the shipped receipts

QUALITY 25(b) names `junk-c.txt` (J1–J3) and `junk-ca.txt` (J4, J4b, J5–J7) and its table carries J1–J7. The
committed receipts carry `junk-c.txt`: J1, J2, J3, **J9**; `junk-ca.txt`: J4, J4b, J5, J6, J7, **J8**, **J9**. J8
(typed receipt → RECEIPTS) is named in the frozen Ca `do_nothing_control` but has no row in the criterion table, and
J9 appears in neither.

*Smallest safe correction.* Append J8/J9 rows (or a note that they were added in `1d7add3` after the freeze and are
not covered by the criterion's table).

### F11 — LOW — "ten allowlisted observe executables" vs nine

`SKILL.md:706` says "the ten allowlisted observe executables". `reports/round-74/accept-ca.py:166-167`
`OBSERVE_ALLOW = ("git", "grep", "wc", "sha256sum", "ls", "cat", "head", "tail", "cut")` = 9, and ledger R2 lists the
same nine.

*Smallest safe correction.* Correct the row to nine.

### F12 — LOW — the round-73 S877 evidence paragraph is not 1564 B

`round-74.md:28`: "`reports/round-73/evidence/S877.txt` … one collapsed paragraph, 1564 B". Observed: the file is
2417 B; its only collapsed-paragraph line is **1614 B** (893 characters); no line in the file is 1564 B.

```
$ python3 -c "t=open('reports/round-73/evidence/S877.txt','rb').read().split(b'\n');b=max(t,key=len);print(len(b),len(b.decode()))"
1614 893
```

*Smallest safe correction.* Append the measured value and the measurement (`longest line of the file`) so the number
is re-checkable.

### F13 — LOW — the M7 note names the wrong evidence field

`round-74.md:26` says "the full sentence stays on the evidence file's `quote:` line". Observed in
`reports/round-74/evidence/S877.txt`: `quote:` = `Язык – главный инструмент построения вымышленных миров` (54 chars,
7 tokens — the same span as the cell); the 108-character sentence exists only in the `locator:` line, as a
slash-broken, ellipsis-terminated fragment (`… реалий, ...`). The 108/15 and 54/7 figures themselves do reproduce.

*Smallest safe correction.* Append "the sentence is on the `locator:` line, not `quote:`" (or add the full sentence
to the evidence file and re-hash its window; that is a heavier move).

### F14 — LOW — the frozen `axes_note` repeats the same sentence five times

```
$ python3 -c "import json;print(json.load(open('reports/round-74/claims.json'))['axes_note'].count('The freshness pause is a lane-filed L0 disposition'))"
5
```

The note is 1327 characters and carries the 194-character freshness-pause sentence five times in a row (a
copy-paste/merge artifact). It is frozen; a reader cannot tell which instance is authoritative.

*Smallest safe correction.* None in place (frozen); record it in the successor round's claims hygiene note so the
duplication is not copied forward. Optionally append one line to the lesson naming the duplication.

### F15 — LOW — the frozen Ca control enumeration does not match the shipped junk-ca fixtures

Ca `do_nothing_control` says "plus `junk-ca.txt`: stub-row, append-only removal, in-place-outside-allowed,
shell-string/interpreter argv, constant-printer observe_cmd, min-pairs, graded-tree config edit, typed receipt each
FAIL their named leg". Shipped `junk-ca.txt` fixture set: J4 (constant-printer, graded-tree ledger), J4b (evasive
printer), J5 (stub-row), J6 (in-place receipt edit → APPENDONLY), J7 (SEPARABLE), J8 (typed receipt → RECEIPTS), J9
(leg deleted → FROZENCFG). `shell-string`, `interpreter`, `min-pairs` and the LOG-line `append-only-removal` are
**selftest** scenarios (scenarios named in `selftest-ca.txt`), not junk-ca fixtures; J7 and J9 are shipped fixtures
the claim does not name.

*Smallest safe correction.* Append a mapping table (claim item → fixture id / selftest scenario) so each named shape
has exactly one artifact.

---

## C. Attacks that FAILED (the claim survived)

Each of these was attacked and the stated value reproduced:

* **Registry rows 804 → 808** and **knowledge files 247 → 249**; directory vector 32/29/40/29/24/95; base zeros for
  `*worldbuilding-setting*` files and for litmemo/tuduku/chinawriter in `corpus/SOURCES.md`.
* **README section/footer arithmetic**: culture-material section = 38 rows, directory = 40 files, 2 unindexed
  (`heritage-taxonomy-models.md`, `…-r13.md`); total file rows 247 (the 248th `^- \`` line is a `python3 …` command
  bullet, not an index row) against 249 files; the older 243/247 footers are byte-identical base..lands.
* **Reject-family counts 5 / 11 / 3 / 2 / 9 / (3+1) = 40** against the staged package
  `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge` (40 `.md` files, 2 adopted, 4 path-present).
* **Guard hashes and counts**: `reg-ids` 804 / `94a495c7…`, `staged-ids` 132 / `bab11d7d…`, `collisions` 22 /
  `130ec2d1…`, map `d3573f7d…`.
* **S877 used-by old→new** exactly as stated, and 11 cells on all five rows, `mined` / `2026-10-25` / `180d`.
* **S877 substitution counts**: staged base S882×4/S883×4/S884×4, staged amend S899×3/S900×3 (the "×4 / ×3" claim).
* **Quarantine arithmetic** 18+3 = 21 data rows, PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4; round-71 `s816.html`
  48536 B `a3b6640c…`, `s817.html` 62604 B `344de345…` (identical to the S883/S884 evidence body hashes).
* **Gate table numbers**: all five body sizes and sha256 values, window sizes 4098/4098/2953/4104/4103, the S882
  `631+33+2289=2953` arithmetic, the 108-char/15-token sentence and 54-char/7-token cell.
* **SCORECARD correction rows**: 12 `LC-*` rows; every re-derivation command re-run here returns the row's new token
  (804, 10, 247, 32, 97656, "two", 724, "present", 728, 701); the counter's `LEG PASS ANNOTATE` re-runs them.
* **Counter verdicts at their own lands**: C 13/13 at `c4bf61a`; Ca 11/11 at `5e4796c` (both exit 0).
* **Selftest summaries in the lesson** (R74-M8): 69/69 and 179/41, exit 0.
* **QUALITY 25 one-liner** on the two round-74 counters: exit 0 both; on the two round-73 counters: exit 1 both;
  installed counter sha256 pins `8d30487f…` / `8052f1e2…` correct.
* **Round-73 sha pins in the SKILL note**: `95aee881…` (accept-c-73 at `2d1cd914`), `222d4dd6…` (accept-ca-73 r3),
  `f8ebb5d8…` (accept-ca-73 at `af65165`), `SELFTEST OK: 10 scenarios` at `selftest-r3.txt:6`.
* **M2's base claim** ("controls-c 1/11, controls-ca* 4/9–5/9") reproduces at `f7104cb`.
* **Census**: start exit 0 / 804, end exit 0 / 808, W01×3, W04×28.

---

## D. Environment / tooling

* **No tool installed or upgraded** (nothing was needed).
* The first `accept-ca.py --selftest` attempt crashed in fixture construction —
  `RuntimeError: fixture toplevel  != /tmp/r74-ca-selftest-…/short/lane` — because the sandbox `/tmp` was 100 % full at
  that moment (`df` showed 969 M free, 100 % used). The same command with `TMPDIR` on the `/home` filesystem exited 0
  with the reported summary. This is an environment artifact, **not** a counter defect; the committed
  `selftest-ca.txt` is consistent with the clean rerun.
* Clone and all temp artifacts are under `/tmp/CritCalibrationRecords/`; the temporary
  `.ufo/waves/round-74/scratch-CritCalibrationRecords/` directory was removed. The only file written in the lane is
  this report.
