# ScribeReportDraft — round 74 wave 2 (kotodama-shokunin), hyaku run 7

Seat role: scribe. Deliverable: the round-74 fleet-report **draft**, written to
`.ufo/waves/round-74/w2/drafts/report-draft.md` (the path the item names), with this seat report at the
`Report:` trailer path. Nothing else in the lane was written; no product code, judge, claim, counter, lesson,
LOG/SCORECARD/SKILL, corpus byte or lane git state was touched. All lane reads were read-only (`git show`,
`git ls-tree`, `grep`, `find`); the two counters were run **only** inside a disposable clone under
`/tmp/ScribeReportDraft-*`, with `git -C "$D" init -q` verified to print `$D` and `git clone -q` of the lane into
`"$D/lane"`, and every branch/checkout move inside `"$D/lane"`. No `task` spawn, no background job of my own.

## Behavior

1. Read the frozen claims at `git show 00c408a0af2f:reports/round-74/claims.json` (config sha256
   `270e31790e2932c8…`), `reports/round-74/ledger.json`, the round-74 lesson, both counter sources (RECEIPTS leg
   read in full), all `telemetry/*` and `evidence/*` receipts, `w1/w1-results.json`, `w2/swarm-registry.json`,
   `w2/dispatch.json`, the 13 wave-2 reports written so far, `SHONEN.md`, `LEARNING.md:33-35`, `QUALITY.md:20/25`,
   and `git status`/`git log`/`git ls-remote` at the lane (read-only).
2. Re-derived every before/after number from the git tree at its own revision (base, `5e4796c`, `c4bf61a`,
   `1d7add3`), not from the worktree.
3. Ran the claim-C counter at the round tip and the claim-Ca counter at the round tip and at its own landing in
   one disposable clone; recorded raw verdict lines and exit codes. Nothing was re-run merely to decorate: the tip
   run establishes a fact no committed receipt holds (Ca's status when both claims are in one tree).
4. Wrote the draft with the required sections in order and the `W2-PENDING:<seat>` marker wherever a fact depends
   on a wave-2 seat that has not written yet.

## Gates exercised by this seat (raw results)

| check | command | raw result |
|---|---|---|
| registry rows, base | `git show f7104cb:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | `804` |
| registry rows, main | same over `corpus/SOURCES.md` | `808` |
| knowledge files, base / main | `git ls-tree -r --name-only f7104cb corpus/knowledge \| grep -c '\.md$'` / `find corpus/knowledge -type f -name '*.md' \| wc -l` | `247` / `249` |
| theme files, main | `find corpus/knowledge -iname '*worldbuilding-setting*' \| wc -l` | `2` |
| source hosts, main | `grep -cE 'litmemo\.com\|tuduku\.space\|chinawriter\.com\.cn' corpus/SOURCES.md` | `4` lines (one per new row S881–S884; 0 at base) |
| CJK-term files, main | `grep -rlE '設定ノート\|世界観\|世界观' corpus/knowledge \| wc -l` | `2` |
| claim C at round tip | `python3 -B reports/round-74/accept-c.py --root . --lands 1d7add3f7b9e… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin` (in clone) | `ACCEPT-C-74: PASS legs=13/13`, exit 0 |
| claim Ca at round tip | `python3 -B reports/round-74/accept-ca.py --root . --lands 1d7add3f7b9e… --freeze 00c408a0af2f… --fleet-root …` (in clone) | `ACCEPT-CA-74: FAIL legs=9/11`, exit 1 — `LEG FAIL APPENDONLY` |
| claim Ca at its landing | same with `--lands 5e4796c0cb6a…` (clone `main` not re-pinned, so STAMP red) | `ACCEPT-CA-74: FAIL legs=10/11` — APPENDONLY/SEPARABLE/RECEIPTS **PASS**, only `STAMP` red (`measured 1d7add3… != lands 5e4796c…`, my own pin error) |
| do-nothing controls | `grep -n 'ACCEPT-C-74:' telemetry/controls-c.txt` / `grep -n 'ACCEPT-CA-74:' telemetry/controls-ca.txt` | `FAIL legs=4/13` / `FAIL legs=7/11`; base runs refused `0/13` / `0/11` (exit 2) |
| component reports, wave 1 | `ls .ufo/waves/round-74/w1/*.md` vs `w1-results.json` seat list | 42/42 seats have a non-empty `*.md` (44 files = 42 + 2 `*.postwave.md`) |
| wave-2 shape | `python3` over `w2/swarm-registry.json` / `dispatch.json` | 44 members; `counts.total` = 44; 13 of 44 reports present at drafting |

## Findings

### F1 — HIGH — `QUALITY 25 (b)`'s freeze receipts do not exist at the freeze or at either claim's landing

`corpus/QUALITY.md` (landed `5e4796c`, QUALITY 25 (b)) states: "The freeze commit carries `counters/junk-fixtures.py`
and four receipts under `reports/round-<N>/telemetry/`: `junk-c.txt` … `junk-ca.txt`, `controls-c.txt` and
`controls-ca.txt`." The frozen claims' `do_nothing_control` strings likewise name
`reports/round-74/telemetry/junk-c.txt` / `junk-ca.txt` as the round's junk controls.

```
$ git ls-tree --name-only 00c408a0af2fa5ddf65af2224152ce258b26d896 reports/round-74/telemetry/
reports/round-74/telemetry/accept-c-73-at-lands.txt
reports/round-74/telemetry/accept-ca-73-at-lands.txt
reports/round-74/telemetry/census-start.txt
reports/round-74/telemetry/controls-c.txt
reports/round-74/telemetry/controls-ca.txt
reports/round-74/telemetry/gap-sweep.txt
reports/round-74/telemetry/selftest-c.txt
reports/round-74/telemetry/selftest-ca.txt

$ git cat-file -e 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/telemetry/junk-c.txt
fatal: path 'reports/round-74/telemetry/junk-c.txt' exists on disk, but not in '00c408a0af2fa5ddf65af2224152ce258b26d896'
```

`git diff --stat 5e4796c..1d7add3` shows `junk-c.txt | 130 +` and `junk-ca.txt | 182 +`: both receipts land only in
`1d7add3`, i.e. **after both claim landings**, so at `5e4796c` (Ca lands) and `c4bf61a` (C lands) the declared junk
controls are absent. The two claims' own control paragraphs therefore name receipts that do not exist at
`<lands>`. (The fixtures themselves were generated pre-data — `junk-r74-run.txt` header `generated:
2026-10-26T01:53:19Z`, generator sha256 `ce6505fc…` — so the ordering defect is in the *split receipts'* commit,
not in the fixture run.)

Corroboration and escalation: `ScribeLogScorecard` F2 states the same independently, and `RevQuality25` F1 files it
as **BLOCKER** with two further counts I re-derived — the freeze carries no `counters/junk-fixtures.py` at all (the
generator is `.ufo/waves/round-74/counters/junk-fixtures.py`), and the generator bytes the receipts name
(`ce6505fc…`) are not the freeze's bytes:

```
$ git cat-file -e 00c408a0af2fa5ddf65af2224152ce258b26d896:counters/junk-fixtures.py
fatal: path 'counters/junk-fixtures.py' does not exist in '00c408a0af2fa5ddf65af2224152ce258b26d896'
$ for c in de93d91 3595c91 00c408a0 1d7add3; do git show "$c:.ufo/waves/round-74/counters/junk-fixtures.py" | sha256sum; done
d4789c39…  (de93d91, 3595c91, 00c408a — identical)
ce6505fc…  (1d7add3)
$ grep -m1 'generator sha256' reports/round-74/telemetry/junk-c.txt
# generator: …/.ufo/waves/round-74/counters/junk-fixtures.py sha256=ce6505fc7d973ced8ad663ee5201eae4931129684dd9794744f115a49fba6d76
```

`RevQuality25` F2 (BLOCKER) adds that J4 and J4b never fail on their named leg (`LEDGER`; they fail `FROZENCFG`),
and F3 (HIGH) that J6/J7 are not differential (their named legs are already red in the clean reference landing
T0) — so clause (b)'s own acceptance test ("a fixture the round-74 counter does not fail on its named leg fails
this criterion") is not met by three of the seven fixtures.

Impact: QUALITY 25 binds from round 74 and
its own round does not satisfy clause (b) at the freeze it names; a future round citing this precedent will cite
a false shape. Not claim-falsifying: no leg checks receipt existence.

**Proposed fix (no frozen byte touched):** append an erratum line to QUALITY 25 (b) — "round 74's split receipts
landed one commit after both claim landings (`1d7add3`); the fixtures were generated at the freeze" — or record
the same as a `## Mistakes` row with class `landing`; and have the freeze checklist make the split receipts part
of the freeze commit's file list (the generator already writes `junk-r74-run.txt`, so the split is a copying
step that can run before the freeze commit).

### F2 — MEDIUM — both claims' `do_nothing_control` prose contradicts the committed control receipts

Claim C (`claims.json` `do_nothing_control`): "lands == <freeze> FAILS with ENTRIES, ROWS, GATE, EVIDENCE,
REJECTS, INDEX red and FROZENCFG green".
Observed (`telemetry/controls-c.txt`): `ACCEPT-C-74: FAIL legs=4/13` with **nine** red legs — the six named plus
`REPOINTED`, `CITEDLINES`, `SCRATCHMIRROR`:

```
LEG FAIL ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / CITEDLINES / SCRATCHMIRROR / INDEX
LEG PASS GROUND / CENSUS / COLLCHECK / FROZENCFG
ACCEPT-C-74: FAIL legs=4/13
```

Claim Ca: "(1) lands == <freeze> FAILS with REPAIR, ANNOTATE, RECEIPTS red and FROZENCFG/LEDGER green".
Observed (`telemetry/controls-ca.txt`): `ACCEPT-CA-74: FAIL legs=7/11` with red = `REPAIR`, `ANNOTATE`, `NOSTUB`,
`SEPARABLE`; **`RECEIPTS` is green** (`LEG PASS RECEIPTS rev=2d1cd9140d3a … problems=[]`), because the round-73
re-run does not depend on this round's landing, and `SEPARABLE` is red only because the freeze tree still carries
the pre-redaction control receipt.

```
$ grep -n 'ACCEPT-CA-74:' reports/round-74/telemetry/controls-ca.txt
52:ACCEPT-CA-74: FAIL legs=7/11
57:ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base f7104cbce186)
```

Both claims are frozen, so the prose stands and the receipts are the truth; the mismatch is unrecorded anywhere.
`ScribeLogScorecard` F1 independently reports the Ca half, and `RevFrozenChain` F2 files the Ca half as **HIGH**
("the frozen Ca `do_nothing_control` clause requires `RECEIPTS red`; its committed receipt prints `LEG PASS
RECEIPTS`").

**Proposed fix:** file a `## Mistakes` row (class `calibration`) naming the two mismatches with the receipt lines,
and stop predicting leg sets in claim prose — quote the receipt path (`controls-*.txt`) instead. For round 75+,
the control generator can emit its red-leg set into `claims.json` at freeze time, so the prose is generated from
the measurement.

### F3 — MEDIUM — claim Ca is green at its own landing only; the combined tree at the round tip fails APPENDONLY

In a disposable clone, with local `main` pinned to the tip:

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands 1d7add3f7b9e… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS LEDGER / BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB
LEG FAIL APPENDONLY
     protected=[…] protected-removed=0 … must_track-exempt=6 problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
LEG PASS SEPARABLE
LEG PASS TRACKED
LEG PASS FROZENCFG / STAMP
ACCEPT-CA-74: FAIL legs=9/11
exit=1
```

At `5e4796c` the same clone shows `APPENDONLY`/`SEPARABLE`/`RECEIPTS` green (only `STAMP` red, my pin error —
`measured 1d7add3… != lands 5e4796c…`), so the red is the *combined-tree* conflict: claim C's required in-place
`used-by` edit on `corpus/SOURCES.md:832` is not a Ca REPAIR `stated_at` line. The lane discloses exactly this in
`telemetry/junk-ca.txt` (`# NOTE (L1, 2026-10-25)` … "claim Ca is therefore measured at its OWN landing commit")
and leaves the frozen claims unamended — correct under the round's own rule. The defect is the **record**: neither
the fleet report nor `measures-ca.txt` says "green only at 5e4796c"; a reader taking the tip as `<lands>` gets
`FAIL`.

**Not counted as evidence:** the tip run also printed `LEG FAIL RECEIPTS … 'accept-c-73 re-run exit=2 (want 0)'`
and `committed stdout differs from the re-run (bda16ca6deec vs e3b0c44298fc)` (the empty-string sha256). I do not
report that as a round defect: during my runs `/tmp` was effectively full (`df -h /tmp` → `128G 128G 90M 100%`,
`250M` free after cleaning my own scratch), and the committed `measures-ca.txt` at `5e4796c` plus
`ScribeLogScorecard`'s and `RevFrozenChain`'s re-runs all show `RECEIPTS` green. The at-tip `RECEIPTS` status is
**unverified** here. Related and reproduced by its own seat: `RevFrozenChain` F1 (HIGH) shows the `RECEIPTS` leg is
materialization-prefix dependent — `normalize_receipt` masks only `/tmp` and `/var/tmp` paths
(`accept-ca.py:165`,`:1721`), so the same bytes fail when the clone root lies outside them.

**Proposed fix:** state the limit in the fleet report's Before→after section (done in the draft) and in
`measures-ca.txt`'s header; if the lane wants the tip green, the only clean route is a round-75 Ca re-freeze whose
APPENDONLY read set includes claim C's `used_by_lines` — never an edit to the frozen ledger.

### F4 — MEDIUM — no round-74 `LOG.md` entry exists at main; the draft's "Landed changes → LOG entry" link is to an unappended draft

```
$ git log --oneline f7104cbce186bc2e1522abf0cfd619cc834628bb..main -- LOG.md
(no output)
```

`LOG.md` is 4302 lines and its last entry is round 73. The wave-2 seat `ScribeLogScorecard` has written the entry
at `.ufo/waves/round-74/w2/drafts/log-entry.md` (untracked), but nothing is appended. The fleet report's required
"each landed change tied to a LOG entry" can therefore only cite the draft path; the draft does so explicitly and
records the limitation.

**Proposed fix:** L1 appends the draft at closure (round-73 precedent: `c1b5b47` "LOG + SCORECARD") and the fleet
report substitutes the `LOG.md:NNNN` line numbers then; until then the report must not cite a LOG line.

### F5 — MEDIUM — the landing carries a falsified header claim and no erratum; the quality verdict is conditional

Verified at main:
```
$ grep -n '## §4' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
72:## §4 Build order — the five steps, and the two orders they allow
$ sed -n '10p' corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
- gap filled: the entry this amends records what a setting is made of and the settings-note tables that carry it; it does not say which part is built first, which part is derived from which, …
$ grep -n 'Erratum' corpus/knowledge/culture-material/worldbuilding-setting-practice*.md
(no match)
```

The parent's `## §4` and its `topic:` line both state the build order the amendment says the parent lacks; the
amendment's `ground:` line repeats the denial. Three wave-2 seats filed this independently (`CritTrendFinal` F1
HIGH, `CritFactAmend2` F1 HIGH, `RevEntryAmendFinal` F1) and it is unrepaired at `1d7add3`. Under LEARNING.md:34
and QUALITY 20/25's precedent the round cannot be filed `quality: unchanged` while an admitted entry carries a
falsified header claim: filed unmarked it is `harmed`, which paired with `expansion: improved` is a trade and "never
admitted" (LEARNING.md:37-38). The draft therefore states the verdict as `unchanged — conditional`, with the
condition spelled out.

**Proposed fix:** append one `## Erratum` section to the amend file (append-only: quote lines 8 and 10, name parent
`## §4` and `:53`, restate what is actually new — disclosure timing, the premise→laws→ladder derivation, a second
register), then re-run `accept-c.py` with `--lands` at the erratum commit and re-stamp `measures-c.txt`;
`ENTRIES`/`CITEDLINES` grade `<lands>` bytes, so a post-lands edit without re-stamp leaves main ≠ graded bytes.

### F6 — LOW — the item's write path and the `Report:` trailer disagree

The item body says to write the draft at `.ufo/waves/round-74/w2/drafts/report-draft.md`; the `Report:` trailer and
the closing line say `.ufo/waves/round-74/w2/ScribeReportDraft.md`. I wrote the draft at the item path (scratch
inside the wave dir, which the seat bounds allow) and this report at the trailer path, and wrote nothing else.
**Proposed fix:** make one path authoritative in the dispatch template; a seat that obeys the trailer and not the
body would otherwise leave the fleet report undrafted.

### F7 — LOW — `w1-results.json` has no per-seat `status`, so "dead seats" is not readable from statuses

```
$ python3 -c 'import json;d=json.load(open(".ufo/waves/round-74/w1/w1-results.json"));print(list(d["results"][0].keys()))'
['name', 'agent', 'output', 'note']
```

Dead-seat accounting therefore rests on report-file existence (42/42 present, two `*.postwave.md` files are not
seat reports). `ScribeLogScorecard` F3 reports the same. **Proposed fix:** the results writer emits
`status` (`done|dead|running`) per seat; the fleet report's dead-seat sentence can then quote a field.

### Peer findings carried (not mine; unrepaired at `1d7add3`, routed)

- `RevQuality25` (instrument criterion 25): F1/F2 **BLOCKER**, F3/F4 **HIGH**, F5-F9 MEDIUM/LOW — QUALITY 25's
  freeze-artifact text is false on four counts (corroborated by my F1), J4/J4b fail `FROZENCFG` not `LEDGER`, J6/J7
  are not differential, and `accept-c.py` returns `PASS legs=13/13` when a landing commit is passed as its own
  `--freeze` (Ca refuses that shape; C has no post-run guard).
- `CritAppendOnly`: F1 **HIGH** — the frozen ledger's `repair_edits[LC-01]` / `SHONEN.md` in-place span declares a
  repair that did not land, and the claim's own APPENDONLY rule rejects that edit; F2 (MEDIUM) — the protected-set
  check is cardinal only at Ca's lands, so claim C prints PASS with a base-era protected line deleted; F3 (MEDIUM) —
  two `Mistakes` rows say `pending landing` for landed fixes; F4 (LOW) — two fleet-repo writes inside the round
  window, unattributable to this lane.
- `RevFrozenChain`: F1/F2 **HIGH** (RECEIPTS prefix dependence; Ca control prose vs receipt), F3 (MEDIUM) the
  "no seat has scored landed data" guard is unqualified and false in the plain git sense of "landed", F4/F5/F6
  LOW/disclosed (provenance sentence, duplicated `axes_note`, pinning gap).
- `ExecWaveLedger` F1 (HIGH): wave-1 attack share 10/42 = 23.8%, below the prompt's ≥25% floor, unrecorded in any
  landed byte; F3 (HIGH): R74-M10's seat-name list is not the collision set (26 collide; 2 listed names exist in
  no round-71..73 artifact); F4 (MEDIUM): a wave-1 report was rewritten after C's lands.
- `ScoutRejectProbes` F1/F2/F4/F7 (HIGH): S895/S899/S900 reject reasons are false for the staged package; four
  staged files under `amendments/` are untriaged ("40 of 40" is 40 of 44); the REJECTS leg certifies reasons that
  the staged bytes contradict.
- `RevReadmeIndex` F1 (MEDIUM): the README claim "0 registry rows naming the theme's venues" is false under the
  theme's own source set; F2 (MEDIUM): the two index rows break the section's filename-order invariant.
- `ScoutReopenS877` F1 (HIGH): the base entry cites S877 outside the row's recorded scope; F4 (MEDIUM): two false
  statements in the round-74 Gate notes (R74-M7). `ScoutReopenS882` F1 (MEDIUM): six uncited authorial claims sit in
  the S882 tables.
- `CritScopeProvince`: both entries **IN-LANE** (attack largely failed), F1/F2 MEDIUM adjacency findings (an axis
  named only in lore's boundary document; a handoff payload the contract does not define), F3-F5 LOW.
- `ExecCensusEnd`: the census-state attack **failed** (registry exactly 808, planted control proves no false PASS);
  F1 (MEDIUM) the CENSUS leg's E-code clause is vacuous against the script's TSV; F2 (LOW) three W01 warnings.
- The remaining 26 wave-2 seats: `W2-PENDING:<seat>`.

## Touched surfaces

- Written: `.ufo/waves/round-74/w2/drafts/report-draft.md` (the draft), `.ufo/waves/round-74/w2/ScribeReportDraft.md`
  (this report). Scratch: `/tmp/ScribeReportDraft-e71jj38q/` (deleted after use).
- Read-only: lane tree and git objects, `reports/round-74/**`, `.ufo/waves/round-74/**`, `corpus/**`, `SHONEN.md`,
  `LOG.md`, `SCORECARD.md`, `SKILL.md`; fleet root `LEARNING.md`, `.ufo/l0-questions.md`, `.ufo/state/` (listing).
  No fleet byte written; no shokuknow access; no pacman/uv/npx install (none needed — `python3 3.14`, `git`, POSIX
  tools sufficed; the tooling directive is recorded as not exercised).

## Out of scope (left to the owner seats)

Repairing the amendment erratum (C seat), appending LOG/SCORECARD (L1 via `ScribeLogScorecard`), the frozen-claim
control prose (an appended lesson/SCORECARD record, never a claims edit), the QUALITY 25 (b) erratum, any wave-2
seat's attack, and the final fleet report at the fleet root — this seat drafts only.

## Artifact paths

- Fleet-report draft: `.ufo/waves/round-74/w2/drafts/report-draft.md`
- This seat report: `.ufo/waves/round-74/w2/ScribeReportDraft.md`
