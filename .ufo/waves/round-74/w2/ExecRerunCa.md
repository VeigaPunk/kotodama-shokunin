# ExecRerunCa — attack on the claim-Ca measurement (round 74, wave 2, hyaku run 7)

Seat: `ExecRerunCa` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Revisions used: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze
F3 `00c408a0af2fa5ddf65af2224152ce258b26d896`; claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`;
claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; final lane main
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236`. All counters were executed only inside
throwaway clones made under `/tmp/ExecRerunCa.tDicb6/` (clone `lane` pinned to 5e4796c,
`base` to f7104cb, `cland` to c4bf61a8, `mainclone` to 1d7add3, `freezeclone` to 00c408a).
No lane/fleet byte was written except this report. No tool was installed.

Environment: Python 3.14.8, git 2.56.0. Host `/tmp` was at 100 % during part of this run
(see the §5.2 environment note); every counter run below is reported with the disk state it ran in.

**Bottom line.** Claim Ca survives at its own lands: `ACCEPT-CA-74: PASS legs=11/11` (exit 0),
all 13 pairs reproduce red at base with the stated `expected_after`, all 12 SCORECARD
re-derivation rows reproduce their new token, the REPAIR line reads the repaired value, and the
selftest is `179 checks across 41 scenarios reported-fail=0` (exit 0). It does **not** survive
claim C's landing or the final main: at both, `ACCEPT-CA-74: FAIL legs=10/11` (exit 1), with the
single red leg `APPENDONLY` naming `corpus/SOURCES.md` line 832 — claim C's contractually
permitted in-place S877 `used-by` edit. The cross-order test the fleet asked for therefore
**fails** (F1). Further findings F2–F8 (control description, receipt mutability, pair quality,
frozen metadata, scan breadth, dead code) do not flip a frozen leg at Ca's own lands; two of the
13 "red" pairs (LC-11, LC-16) do not evidence a stale fact.

---

## 1. Primary measurement — counter at Ca lands (as stated)

Clone: `git init` in a fresh temp dir; `git clone -q <lane> "$D/lane"`; then
`git -C "$D/lane" checkout -q --detach HEAD && git -C "$D/lane" branch -f main 5e4796c… &&
git -C "$D/lane" checkout -q main` (the required pin dance; a direct `branch -f main` is refused
while `main` is checked out).

```
$ cd /tmp/ExecRerunCa.tDicb6/lane
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
# counter sha256 (self): 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
# stamped revision: 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
# evaluated revision: 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
# measured revision (lane main): 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3
# tree: 83257915923cd153c4d20db99432f6b84eec2fe9
# freeze: 00c408a0af2fa5ddf65af2224152ce258b26d896 (config read at this commit only)
# ledger: reports/round-74/ledger.json source=freeze sha256=88d5fd522c86b3ef37577531d39b148633455836ecd207f27a27a449c8725bd4
… (13 PAIR lines; see §2/§3)
LEG PASS LEDGER            pairs=13 min=10 source=freeze
LEG PASS BASEMISMATCH      red=13 min=10 ids=['LC-01','LC-02','LC-03','LC-06','LC-07','LC-08','LC-09','LC-11','LC-12','LC-15','LC-16','LC-17','LC-18']
LEG PASS REPAIR            green=['LC-09'] red=[]
LEG PASS ANNOTATE          rows=14 annotate-pairs=12 unannotated=0 []
LEG PASS NOSTUB            minimum-shape=leading-id+old-token+new-token+rederive stubs=[]
LEG PASS APPENDONLY        protected-removed=0 fleet-pin=dad39efd2798 blob-sha256=000bab3a3664 repair-stated_at={'SKILL.md': [594]} must_track-exempt=6
LEG PASS SEPARABLE         lane-ids=4 ids-sha256:ddc5bbce family-sha256:36049478 forbidden=5 problems=[]
LEG PASS TRACKED           paths=6 problems=[]
LEG PASS RECEIPTS          rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16','accept-ca-73=864c94192854'] problems=[]
LEG PASS FROZENCFG         freeze=00c408a0af2f first-parent-of-lands …
LEG PASS STAMP             stamped=evaluated=measured=5e4796c0cb6a tree=83257915923c counter=8052f1e25c36
ACCEPT-CA-74: PASS legs=11/11
EXIT=0
```

The declared statement reproduces exactly. (Wall time 21.9 s; `/tmp` had room for this run.)

## 2. Base re-run — all 13 ledger `observe_cmd`s, verbatim argv, in a clone at f7104cb

Runner: `/tmp/ExecRerunCa/rerun_pairs.py` (executes `pair["observe_cmd"]` with `cwd=` the base
clone, applies `pair["parse"]`, and compares to `stated_parse(stated_text)` and `expected_after`).
Every command exited 0. Raw output shown for the token-bearing line:

```
LC-01 ANNOTATE stated='412'   observed='804'   expected_after='804'  red=True  raw='f7104cb…:corpus/SOURCES.md:804'
LC-02 ANNOTATE stated='9'     observed='10'    expected_after='10'   red=True  raw='SELFTEST OK: 10 scenarios'
LC-03 ANNOTATE stated='9'     observed='10'    expected_after='10'   red=True  raw='SELFTEST OK: 10 scenarios'
LC-06 ANNOTATE stated='243'   observed='247'   expected_after='247'  red=True  raw='247 files changed, 43426 insertions(+)'
LC-07 ANNOTATE stated='243'   observed='247'   expected_after='247'  red=True  raw='247 files changed, 43426 insertions(+)'
LC-08 ANNOTATE stated='30'    observed='32'    expected_after='32'   red=True  raw='32 files changed, 5689 insertions(+)'
LC-09 REPAIR   stated='94'    observed='95'    expected_after='95'   red=True  raw='95 files changed, 18546 insertions(+)'
LC-11 ANNOTATE stated='23443' observed='97656' expected_after='97656' red=True  raw='decompress -> 23443 -> 97656 bytes'
LC-12 ANNOTATE stated='no'    observed='two'   expected_after='two'  red=True  raw='HAS two status-200 Wayback captures'
LC-15 ANNOTATE stated='776'   observed='724'   expected_after='724'  red=True  raw='65fe857…:corpus/SOURCES.md:724\nf7104cb…:corpus/SOURCES.md:804'
LC-16 ANNOTATE stated='reachable' observed='present' expected_after='present' red=True raw='wall present ("Client Challenge")'
LC-17 ANNOTATE stated='752'   observed='728'   expected_after='728'  red=True  raw='c5f0992…:corpus/SOURCES.md:728\nf7104cb…:corpus/SOURCES.md:804'
LC-18 ANNOTATE stated='753'   observed='701'   expected_after='701'  red=True  raw='94209e8…:corpus/SOURCES.md:701\nf7104cb…:corpus/SOURCES.md:804'
```

Also verified independently in the base clone: every `stated_text` is a verbatim substring of
its `stated_at` line (all 13 `True`), every `stated_parse` yields the stated token, and the
fleet report line 10 (`fleet:.ufo/reports/round-73/kotodama.md:10`) contains
`selftests (C 29/29; Ca 9 scenarios)`. Independent counts at base with `git ls-tree`
(not the ledger's `git diff`): civilizations 95, culture-material 38, linguistics 32,
myth-symbol 29, synthesis 29, verification 24 = **247** (README's stale 243/30/36 confirmed).
`git grep -c -E '^ACCEPT-(C|CA)-73: PASS' f7104cb -- reports/round-73/telemetry` → exit 1, no
output (claim's before-(b) confirmed). All six inherited files hash to the ledger's
`must_track` sha256 at lands; the five tracked ones have different base blobs; RevengerOrigins
is absent at base (`fatal: path … exists on disk, but not in 'f7104cb'`).

## 3. Lands re-run — every ANNOTATE re-derivation row from `## Corrections — round 74`, plus the REPAIR re-read

Runner: `/tmp/ExecRerunCa/rerun_rederive.py` (parses the 12 `| LC-… |` rows out of the SCORECARD
section and executes each row's own command string in the clone at 5e4796c). All 12 exit 0:

| id | row old→new | token returned | = row new | = ledger expected_after |
|---|---|---|---|---|
| LC-01 | 412→804 | 804 | yes | yes |
| LC-02 | 9→10 | 10 | yes | yes |
| LC-03 | 9→10 | 10 | yes | yes |
| LC-06 | 243→247 | 247 | yes | yes |
| LC-07 | 243→247 | 247 | yes | yes |
| LC-08 | 30→32 | 32 | yes | yes |
| LC-11 | 23443→97656 | 97656 | yes | yes |
| LC-12 | no→two | two | yes | yes |
| LC-15 | 776→724 | 724 | yes | yes |
| LC-16 | reachable→present | present | yes | yes |
| LC-17 | 752→728 | 728 | yes | yes |
| LC-18 | 753→701 | 701 | yes | yes |

REPAIR statement re-read at lands (`statement_after` grammar, last occurrence):

```
SKILL.md:594 -> '- `corpus/knowledge/civilizations/` — 95 entries: 93 earlier-civilization'
base stated_text '94 entries: 92 earlier-civilization' present at lands = False
```

The second token is also correct: 95 files − 2 named source maps (`africa-primary-sources.md`,
`mesoamerica-primary-sources.md`) = 93 (`ls corpus/knowledge/civilizations/*.md | wc -l` = 95).
Independent `git diff --shortstat 4b825dc… 5e4796c -- 'corpus/knowledge/civilizations/*.md'` =
`95 files changed`. The repair is sound.

## 4. Selftest

```
$ python3 -B reports/round-74/accept-ca.py --selftest
… 41 scenario lines …
SELFTEST OK: 179 checks across 41 scenarios reported-fail=0: do-nothing, clean, lands-eq-base, legcount,
stub-rows, no-rederive, annotate-other-token, append-only-removal, protected-in-place, unnamed-in-place,
shell-string, interpreter, constant-printer, out-of-clone, dead-pin, absence-pair, min-pairs,
config-edit-ledger, config-edit-claims, freeze-off-first-parent, repair-no-statement, shadow-repair,
tracked-missing, tracked-blob-mismatch, typed-receipt, receipt-wrong-rev, receipt-missing,
separable-lane-row, separable-non-lane-id, basemismatch-leading-token, separable-sid, separable-family,
fabricated-base-observation, green-pair, stated-line-mismatch, prose-row, expected-after-mismatch,
repair-pinned-observation, worktree-only-ledger, stamp-measured, c…
EXIT=0
```

(the committed `reports/round-74/telemetry/selftest-ca.txt` carries the same summary line, so it is
reproducible). Expected controls behaved: `do-nothing` exit 1 with REPAIR/ANNOTATE/NOSTUB/RECEIPTS red;
`clean` exit 0; `lands-eq-base` exit 2; mutant classes fail their named leg.

## 5. Cross-order runs — Ca at claim C's lands and at the final main

### 5.1 Claim-C lands `c4bf61a8` (clone `cland`, main = c4bf61a8)

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
…
LEG PASS LEDGER / BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB
LEG FAIL APPENDONLY
     protected=[…] protected-removed=0 fleet-pin=dad39efd2798 blob-sha256=000bab3a3664
     repair-stated_at={'SKILL.md': [594]} must_track-exempt=6
     problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
LEG PASS SEPARABLE / TRACKED / RECEIPTS / FROZENCFG / STAMP
ACCEPT-CA-74: FAIL legs=10/11
EXIT=1
```

### 5.2 Final main `1d7add3` (clone `mainclone`, main = 1d7add3)

Clean run (local `TMPDIR` under my scratch, 2.7 G free):

```
$ TMPDIR=/tmp/ExecRerunCa.tDicb6/tmp python3 -B reports/round-74/accept-ca.py --root . \
    --lands 1d7add3f7b9eaf6f3349c56c36f6d06325d74236 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 \
    --fleet-root /home/vgpnk/Projects/shokunin
# tree: 33a67fd9ce175b5ba657f5feafb9f9674a9808a4
…
LEG PASS LEDGER / BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB
LEG FAIL APPENDONLY
     problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
LEG PASS SEPARABLE / TRACKED / RECEIPTS / FROZENCFG / STAMP
ACCEPT-CA-74: FAIL legs=10/11
EXIT=1
```

Environment disclosure: the first main run (same command, stock `/tmp`) printed
`ACCEPT-CA-74: FAIL legs=9/11` with `RECEIPTS` red (`accept-c-73 re-run exit=2 (want 0)` …,
committed stdout vs re-run `… vs e3b0c44298fc` = the empty-string sha256). `/tmp` was at 100 %
(140 M free); a manual clone then failed with `unable to create file …: No space left on device`,
which produces exactly "python can't open the counter → exit 2, empty stdout". After removing my
own scratch (1.4 G) the clean run above shows `RECEIPTS` PASS. **The RECEIPTS failure is
environmental, not a claim defect**; do not score it. The `APPENDONLY` failure reproduces in both
disk states and in the C-lands clone, so it is content-caused.

### 5.3 Do-nothing control at the operative freeze (reproduced)

Clone `freezeclone` at 00c408a, run `--lands 00c408a --freeze 00c408a`:

```
LEG PASS LEDGER BASEMISMATCH APPENDONLY TRACKED RECEIPTS FROZENCFG STAMP
LEG FAIL REPAIR     green=[] red=["LC-09(statement='94' truth='95')"]
LEG FAIL ANNOTATE   no '## Corrections — round 74' section; annotate-pairs=12
LEG FAIL NOSTUB     stubs=['LC-01:no-leading-row', … 12 ids]
LEG FAIL SEPARABLE  problems=['cites <redacted lane id> in reports/round-74/telemetry/controls-ca.txt',
                              'names the frozen claim-C path family in reports/round-74/telemetry/controls-ca.txt']
ACCEPT-CA-74: FAIL legs=7/11
exit=1
```

After normalising the `/tmp` clone path, this output is **byte-identical** to section 1 of the
landed `reports/round-74/telemetry/controls-ca.txt` (only the receipt's header/command/`exit=`
lines differ). Control 2 reproduces too:
`--lands f7104cb --freeze 00c408a` → `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the
frozen base f7104cbce186)`, exit 2.

---

## Findings

### F1 — HIGH — Ca's `APPENDONLY` leg is false at claim C's lands and at the final main; the cross-order test fails

**Command** (§5.1 and §5.2) and **raw output** quoted there:
`ACCEPT-CA-74: FAIL legs=10/11`, `problems=['corpus/SOURCES.md: changed lines outside REPAIR
stated_at lines [832]']`, `EXIT=1` in both clones. At its own lands the same counter prints
`ACCEPT-CA-74: PASS legs=11/11` (exit 0).

**Cause.** Claim C's frozen ROWS leg explicitly allows "the only other registry change is S877's
line, whose `used-by` cell at `<lands>` equals its base value plus exactly the new base-entry
path"; `corpus/lessons/round-74.md:90-96` records that in-place change old→new. Commit d7a3840
does exactly that (`corpus/SOURCES.md | 6 +-`, hunk `@@ -832 +832 @@` = the S877 row). Ca's frozen
`APPENDONLY` leg allows changed lines only at REPAIR `stated_at` lines (SKILL.md:594) plus append
hunks; SOURCES.md is not a `must_track` path. The two frozen claims are therefore mutually
incompatible when Ca is evaluated at any lands at/after C's landing.

**Proposed fix.** Either (a) scope Ca's append-only sweep to `base..ca_lands` by reading the
claim's own lands from the frozen config instead of the graded `--lands`, or (b) allow registry
`used-by`-only line changes that the round's mutation record names (S877) — i.e. add that path+line
to the frozen allowlist, or (c) declare in the round protocol that each claim is scored only at its
own lands commit. As landed, with the fleet's "everything has landed, run the counter at the
stated lands" convention extended to main, **claim Ca fails as declared** on this leg.

### F2 — MEDIUM — the frozen `do_nothing_control` text misdescribes its own receipt (RECEIPTS is green, not red)

The frozen claim says: "lands == `<freeze>` FAILS with **REPAIR, ANNOTATE, RECEIPTS red** and
FROZENCFG/LEDGER green". The receipt it names, and my reproduction, show:
`LEG PASS RECEIPTS … problems=[]` and instead `NOSTUB` and `SEPARABLE` red
(`ACCEPT-CA-74: FAIL legs=7/11`). The freeze-time copy of `controls-ca.txt`
(`git show 00c408a:reports/round-74/telemetry/controls-ca.txt`, lines 45/48) also shows
`LEG PASS RECEIPTS`. So the claim's control description is wrong for both the freeze artifact and
the landed artifact. **Fix:** record the corrected leg set (REPAIR, ANNOTATE, NOSTUB, SEPARABLE
red; LEDGER, BASEMISMATCH, APPENDONLY, TRACKED, RECEIPTS, FROZENCFG, STAMP green) as a correction
row; the frozen text cannot be rewritten.

### F3 — MEDIUM — freeze→lands receipts are mutable and unguarded; the Ca read set was made clean by rewriting its own control receipt at lands

`reports/round-74/telemetry/controls-ca.txt` is **modified in place** between the operative freeze
and the Ca lands commit:

```
$ git diff --stat 00c408a 5e4796c -- reports/round-74/telemetry/controls-ca.txt
 reports/round-74/telemetry/controls-ca.txt | 48 +++++++++++++++---------------
 1 file changed, 24 insertions(+), 24 deletions(-)
```

The freeze copy was a de93d91c-era run (counter sha `dd755893…`) and contains the redacted-now
literals at lines 42/49: `id-floor=S881 family=worldbuilding-setting-practice …`. The landed copy
is a 00c408a rerun (counter sha `8052f1e2…`) with those literals redacted. Because the
`APPENDONLY` leg diffs `base..lands` only, and this file is *new relative to base*, the in-place
rewrite is invisible to it. Consequence: Ca's `SEPARABLE` PASS at lands depends on the seat
editing a file that is inside Ca's own read set after the freeze (at the freeze, `SEPARABLE` is red
precisely because of that file — see §5.3). R74-M9 discloses the redaction, but the measurement
hole stands. **Fix:** pin the control/receipt files (sha256 at freeze) and require them
byte-identical freeze→lands, or run the append-only sweep from `<freeze>` for files that exist at
freeze.

### F4 — MEDIUM — LC-11 pairs a gzip wire size with a decoded payload size; the stated token is not stale

Observe command: `git grep -h -o -E 'decompress.*23443.*[0-9]+ bytes' f7104cb -- .ufo/waves/round-73/w2/ScoutReopenS879.md`
→ `decompress -> 23443 -> 97656 bytes`. The witness (same file, lines 14-19) says:
`status=200 size_download=23443  # = the row's "23443 bytes"` and `python gzip.decompress ->
23443 -> 97656 bytes`; i.e. **23443 is the capture's wire size and 97656 its decoded size — both
true**. The lesson's false clause is "is a shell that does not carry the span" (the scout: "quote
in body = True"), which no pair measures. The ledger's own `why` admits the quantity split ("23443
is the gzip wire size and the decoded 97656-byte payload carries the span"). The ANNOTATE row
`old 23443 → new 97656` therefore tells a later reader the wrong corrected figure. **Fix:** record
the pair as mispaired (correction row), repair the "shell" clause, and do not treat 97656 B as the
capture size.

### F5 — MEDIUM — LC-16 compares the word "reachable" with "present" from a second, UA-scoped sentence

Observe command returns `wall present ("Client Challenge")` from the same lesson's Quarantine row
(:47-48), which says: "the Springer chapter page serves in full under the plain UA and is walled
under the browser UA, so an unreachability ground would be VOID (QUALITY 22)". The paired line
(:138) says the five staged docs "are reachable and span-present (this lane's triage)" — true under
the plain UA; the real gap is the missing UA qualifier, not a wrong value. Together with F4, 2 of
13 "red" pairs are token-inequality artifacts rather than stale statements, which weakens the
claim's phrase "every listed pair red — stated token != observed token" as calibration evidence.
**Fix:** state the correction as a UA qualifier; keep the pair but label it a qualifier gap.

### F6 — LOW/MEDIUM — LC-17 corrects half of README:28; the same sentence's "→ 776" is left false

The ledger's LC-17 `why` says "the stated after-value 776 matches no committed state. This pair
pins the BEFORE token (752 -> 728)". Verified: at the round-67 landing `c58eb84` the registry held
`752` rows (so "→ 776" is false), and the SCORECARD row carries only `752 → 728`. Round-73's
L01/L02/L03 cover README :732/:407/:736 only. **Fix:** add a row for the second token
(776 → 752 at c58eb84) or state the residual in the LC-17 row.

### F7 — LOW/MEDIUM — frozen ledger metadata contradicts the frozen pairs (unperformed LC-01 "repair")

`reports/round-74/ledger.json` at the freeze carries `repair_edits[0].id="LC-01"` with
`old_line`/`new_line` (412 → 804) and `must_hold: "Line 6 is the only changed SHONEN.md line"`, and
`inplace_spans.required_for_this_ledger` says "SHONEN.md: add to the in-place path set … LC-01
rewrites that line". But `pairs[LC-01].disposition="ANNOTATE"`, `annotate_rows` omits LC-01 (11
ids), the landed SCORECARD carries an annotation row for LC-01, and
`git diff --stat f7104cb 5e4796c -- SHONEN.md` is **empty** (line 6 still reads "412 rows after
round 56"). The round lesson (:200) also calls SHONEN:6 "a REPAIR". No counter leg reads
`repair_edits`/`inplace_spans`, so nothing fires. **Fix:** freeze-record LC-01's re-disposition and
drop the unperformed edit (or implement the SHONEN span in the counter if a repair is intended;
the current counter only allows REPAIR `stated_at` lines).

### F8 — LOW — `SEPARABLE` scans a strict subset of its frozen read set

The frozen leg's read set is "the ledger …, every SCORECARD line …, the telemetry receipts and
controls named in this file's Ca section …". The implementation extracts only paths written with
the full `reports/round-N/telemetry/` prefix, so at Ca lands it scans
`selftest-r3.txt`, `accept-c-73-at-lands.txt`, `controls-ca.txt` and **omits**
`accept-ca-73-at-lands.txt`, `junk-ca.txt`, `selftest-ca.txt` (named bare after "and"/"plus").
Live verdict is unaffected — I grepped all three omitted files for
`S88[1-4]|worldbuilding-setting-practice` → `0` hits each (also 0 in `junk-ca.txt`,
`controls-ca.txt` landed; the ledger and corrections section are 0). **Fix:** enumerate the frozen
read set explicitly, or resolve bare telemetry filenames against `TELEMETRY_DIR`.

### F9 — LOW — dead code in the counter

`reports/round-74/accept-ca.py` defines `_must_track` twice (lines ~1601 and ~1629); the first is
shadowed and unreachable. No behavioural effect (the second is a superset). **Fix:** delete the
first definition.

---

## Attacks that FAILED (the claim survived) — evidence

- **Counter inverse (fake PAss):** no; `ACCEPT-CA-74` at 5e4796c is a genuine 11/11, and every leg
  I could recompute independently agrees (LEDGER pair grammar, BASEMISMATCH red set, REPAIR
  statement, ANNOTATE rows, TRACKED hashes, RECEIPTS byte-compare, fleet pin `000bab3a…`).
- **Red-before fabricated by trusting the ledger:** no; I re-executed all 13 `observe_cmd`s in a
  base clone and every stated token differs from the observed one, with `expected_after` matching
  (table §2).
- **Correction rows that only name an id / whose command returns something else:** no; all 12
  SCORECARD row commands re-run to exactly the recorded new token (§3), and the rows carry
  id+old+new+command (`NOSTUB` PASS).
- **REPAIR silently stale at lands:** no; SKILL.md:594 reads `95 entries: 93 earlier-civilization`,
  the base text is gone, `95 == 95 files changed`, and 93 = 95 − 2 named source maps.
- **Selftest vacuous / fake:** no; 179 checks across 41 scenarios, exit 0, including the
  `do-nothing`, `lands-eq-base`, mutant and `separable-*` controls; the committed
  `selftest-ca.txt` reproduces.
- **Do-nothing control does not fail at the freeze:** no; reproduced `FAIL legs=7/11` byte-identical
  to the landed receipt; lands==base is refused with exit 2.
- **Frozen config edited after freeze:** no; `FROZENCFG` PASS in every run and
  `claims.json`/`ledger.json` blobs equal at freeze and lands.
- **Tracked-pin drift:** no; all six `must_track` blobs hash to the recorded sha256 at lands;
  five differ from base blobs; RevengerOrigins is absent at base.
- **Fleet report drifted:** no; `git show dad39efd…:.ufo/reports/round-73/kotodama.md` and
  `HEAD:` both hash `000bab3a3664…`; `git diff --stat dad39efd HEAD -- <report>` empty; worktree
  clean for that path.

## Not run / limits

- `junk-ca.txt` fixtures were **not re-executed** by me (their generator can create junk repos; I
  did not run it to avoid writes). The equivalent mutant classes are covered by the counter's own
  selftest, which I did run. Treat the junk table as unverified by this seat.
- The "this lane writes no byte under the fleet root" limb is implemented by the counter only over
  the named fleet report path (`git status --porcelain -- <report>`); I verified that path only.
- LSP was not used (no symbol/reference task in this measurement).
- All scratch under `/tmp/ExecRerunCa.tDicb6/` and `/tmp/ExecRerunCa/`. `/tmp` hit 100 % once
  during this run (§5.2 environment note); the `lane`/`cland` clones were removed mid-run, and after their
  outputs were captured the `base`/`freezeclone` clones were also removed to leave room for other
  seats; `mainclone` (1d7add3) and the captured stdout files (`/tmp/ExecRerunCa/*.out`,
  `receipt-sec1.txt`, `rerun-sec1.txt`) are retained.
