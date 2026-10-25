# kotodama round 73 — fleet report DRAFT (skeleton with every number re-derived)

Seat: ScribeReportDraft (wave 2, FALSIFY, hyaku run 7). This file is the skeleton of
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-73/kotodama.md`; it is **not** the fleet report.
Only `[L1 to fill]` markers below are unfilled: the three trend verdicts and the wave-2 totals
(§5). Everything else carries the command that produced it.

- Base `8841ad3b896a0227674fa0725b818c999118046f`; freeze `af65165cf269db346ef872e16a656eccd7264d01`;
  lands `0316b8883b4f8d44b8efd720140e7f52f734a102`; claim text
  `reports/round-73/claims.json` (read first; 189 lines, 13 `pre_data_corrections`).
- Every number below was re-run by this seat on 2026-10-25 in throwaway clones, never in the lane
  worktree. Clone setup actually used:

```
D=$(mktemp -d -p /tmp/ScribeReportDraft) && git -C "$D" init -q && \
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane" && \
git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
# -> /tmp/ScribeReportDraft/tmp.6VzBNC47uc ; git -C "$D" rev-parse --show-toplevel == $D
```

For the two counter runs a *fleet-shaped* clone was also built (the C counter's CENSUS leg needs
`<parent>/scripts/sources-census.sh`; see F3):

```
F=/tmp/ScribeReportDraft/fleet2; mkdir -p "$F/scripts"
cp /home/vgpnk/Projects/shokunin/scripts/sources-census.sh "$F/scripts/"
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$F/kotodama-shokunin"
git -C "$F/kotodama-shokunin" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
```

No live network fetch was made by this seat, so no User-Agent record applies to this report and no
source-reachability ruling is made here (the Gate rows' HTTP/byte/sha256 claims are quoted from the
committed captures, not re-fetched; see §9).

## 1. Work performed

Two frozen claims, both landed at `0316b88`:

- **Claim C — axis `coverage`, kind `assimilation-sourced`**: the shokuknow `merge/kotodama`
  conlang-scholarship theme assimilated as two admitted knowledge entries on ground the lane did not
  hold, carried by five registry rows `S876..S880` re-pointed *by document* from staged
  `S881/S882/S892/S893/S901` (`reports/round-73/claims.json:76-157`).
- **Claim Ca — axis `calibration`, kind `records`**: an eight-pair self-assessment-vs-repo-state
  ledger, every red pair repaired in place (REPAIR) or annotated append-only (ANNOTATE), plus the
  three round-72 routed defects R1/R2/R3 (`reports/round-73/claims.json:159-189`).

Work items, one bullet each, with the pointer that proves the item exists:

- **Gap sweep before adoption** — the theme had no owner in the lane or in 20 sibling lanes;
  receipt `reports/round-73/telemetry/gap-sweep.txt:1-72` (sections [1]-[7]), seat report
  `.ufo/waves/round-73/w1/ScoutGapSweep.md`, mined by `CritMistakeFix` (R73-M6 repaired the
  receipt's shape additively at `0316b88`).
- **Staged→lane id re-pointing by document** — `.ufo/waves/round-73/assimilation/id-renumber-map.json`
  (`map` key, carrier `af65165` + `0316b88`), `register-id-overlap.txt`, `theme-row-collision.txt`,
  `collisions` (17 ids, S859..S875); seats `ScoutMapIds`, `ExecRenumber`.
- **Five documents opened and captured** — `reports/round-73/evidence/S876.txt`..`S880.txt`
  (carrier `af65165`), each with `fetch:`, browser-shaped `user-agent:`, `http-status: 200`,
  `bytes:`, 64-hex `sha256:`, `quote-found-verbatim: yes`, quote and ±400-char context window; seats
  `ScoutS881`, `ScoutS882`, `ScoutS892`, `ScoutS893`, `ScoutS901`.
- **Refused / not-adopted triage with probed URLs** — `corpus/lessons/round-73.md:42-58` (refused
  S869/S894/S910 + four not-adopted staged files + four families, each with reason, flip, probed
  URL); seats `ScoutAmendTriage`, `RevSowersAccess`, `ScoutQuarantineConlang`.
- **Two entries authored** — `corpus/knowledge/linguistics/conlang-scholarship.md` (105 lines) and
  `…/conlang-scholarship.amend-2026-10-23.md` (90 lines), carrier `85f17eb`; seats `ScribeEntryBase`,
  `ScribeEntryAmend`, `RevEntryQuality`, `SimplifierRows`.
- **Registry append, normalized** — `corpus/SOURCES.md:831-835` (carrier `85f17eb`): `status=mined`,
  `opened=2026-10-25`, `recheck=180d`, `used-by` exactly the citing entry (2 base rows → base entry,
  3 amendment rows → amendment), tier B ×5.
- **Gate + rejects recorded in the lesson** — `corpus/lessons/round-73.md:10-75` (5 admit rows with
  access date, ≤25-word quote, locator, capture path; 6 reject rows).
- **Claim-C counter hardened against the wave-1 vacuity class** — `reports/round-73/accept-c.py`
  (1687 lines, sha256 `95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416`, carrier
  `af65165`), 11 legs, `--selftest` → `SELFTEST: 29/29`
  (`reports/round-73/telemetry/selftest.txt`); seats `CritCCounterVacuity`, `ExecCCounter`.
- **Collision guard + scratch mirror (item 10)** — `.ufo/waves/round-73/assimilation/guard-proof/guard-proof.txt`
  (planted 1-3-space-indented row found, 4-space control not found) and
  `.ufo/waves/round-73/assimilation/validate-receipt.txt` (carrier `af65165`, ids block added
  `0316b88`). The seat `ExecScratchMirror` returned nothing (dead); the mirror was done by the L1
  (`corpus/lessons/round-73.md:140-142`).
- **QUALITY 22 and 23 authored with their controls** — `corpus/QUALITY.md:66` (UA↔response binding)
  and `:77` (selftest receipt + red-before), `reports/round-73/telemetry/quality22-controls.txt`;
  seats `ScribeQuality22`, `CritQuality22`.
- **README footer appended** — `corpus/README.md:766-775` (two index lines, registry 799 → 804,
  `Total knowledge entries: 247.`, directory totals `32/29/38/29/24/95`); seat `ScribeReadmeIndex`.
- **Ca ledger committed before data** — `reports/round-73/ledger.json` (8 pairs, `fleet_pin`
  `80d8c9b576d45d3c390e1e8edc6c149cfb698483`, `must_track` = the two round-72 seat files), carrier
  `af65165`; seats `ExecLedger`, `CritCaVacuity`.
- **Five ANNOTATE correction rows** — `SCORECARD.md:1409-1419` (L01, L02, L03, L06, L07; each row
  names id + old token + new token + re-derivation command), carrier `e62d731`.
- **Three REPAIR edits** — `SHONEN.md:6` `:468`→`:505`, `:522`→`:564` (L04/L05) and `SKILL.md` last
  registry row `accept-o-69`→`accept-ca-73` (L08, line 704), carrier `e62d731`.
- **Round-72 dead-seat files tracked (R1)** — `.ufo/waves/round-72/w1/ScoutMergeScan.md` (183 lines)
  and `ScribeLesson.md` (217 lines), carrier `e62d731`.
- **R2 re-run receipt** — `reports/round-73/telemetry/measures-ca72-rerun.txt` (round-72 counter sha
  `f080c240…`, stamped `21ad3088`, `ACCEPT-CA-72: PASS legs=12/12`, fleet pin recorded), carrier
  `e62d731`; seat `ExecReceiptRerun`.
- **Ca counter revisions r2 and r3 with red-before** — `reports/round-73/counter-revisions.md`
  (carriers `3537899`, `85f17eb`), `selftest-r2.txt`, `selftest-r3.txt`, `red-before-r3.txt`
  (`SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'`); seats `ExecCaCounter`, `CritCaVacuity`.
- **Do-nothing controls for both claims** — `controls-c.txt` (carrier `af65165`),
  `controls-ca.txt` (r1, `af65165`), `controls-ca-r2.txt` (`3537899`), `controls-ca-r3.txt`
  (`85f17eb`).
- **Six mistakes recorded** — `corpus/lessons/round-73.md:104-121` (R73-M1 … R73-M6) plus the routed
  list `:132-140`.

## 2. Landed changes

Range: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --format='%H %s' 8841ad3b896a0227674fa0725b818c999118046f..0316b8883b4f8d44b8efd720140e7f52f734a102`

```
0316b8883b4f8d44b8efd720140e7f52f734a102 round-73 C: repair artifact shapes found at first grading (gap-sweep literal fragments, mirror receipt ids, renumber map key, README footer without claim-C ids), lesson R73-M6, QUALITY 23 freeze-commit run
85f17eb9f977d16d9c1d0caaf213c41265ceb217 round-73 C: conlang-scholarship adoption — 2 entries, rows S876-S880, lesson round-73, evidence, QUALITY 22/23, README footer; counter r3 + receipts
3537899031508864c1b3deb7c5dc3a81cf2333db round-73 Ca: counter r2 (ledger read at <lands>, bug disclosed in counter-revisions.md), SKILL.md row text, r2 control + selftest receipts
e62d731614f438b9a1f7c07a174a962f85d82d66 round-73 Ca: SCORECARD corrections (L01-L03, L06, L07), SHONEN pointers (L04/L05), SKILL.md gate rows (L08), R2 rerun receipt, round-72 seat reports tracked (R1)
af65165cf269db346ef872e16a656eccd7264d01 round-73: freeze — claims C+Ca, ledger, counters (selftest 29/29, 9 scenarios), do-nothing controls, wave-1 evidence (34/37 seat reports), assimilation scratch
```

Total: `git diff --stat 8841ad3..0316b88 | tail -1` → `133 files changed, 24658 insertions(+), 1
deletion(-)`. The single deletion is the SHONEN.md line replaced in place (L04/L05), a non-append-only
file — `git diff --numstat 8841ad3 0316b88 -- SHONEN.md` → `1 1`.

| # | change | commit(s) | LOG.md entry |
|---|---|---|---|
| 1 | `reports/round-73/claims.json`, `ledger.json`, `accept-c.py`, `accept-ca.py` (r1), `evidence/S876..S880.txt`, `telemetry/{census-start,controls-c,controls-ca,selftest}.txt`, wave-1 spec/registry/results + 34 seat reports, assimilation scratch | `af65165` | **absent** (see below) |
| 2 | `SCORECARD.md` `## Corrections — round 73` (16 lines: L01, L02, L03, L06, L07 + REPAIR/REPORT/R1 prose) | `e62d731` | **absent** |
| 3 | `SHONEN.md` line 6 (L04/L05 pointers) | `e62d731` | **absent** |
| 4 | `SKILL.md` +7 gate rows (`accept-c-71` … `accept-ca-73`) | `e62d731` | **absent** |
| 5 | `.ufo/waves/round-72/w1/ScoutMergeScan.md`, `ScribeLesson.md` tracked | `e62d731` | **absent** |
| 6 | `reports/round-73/telemetry/measures-ca72-rerun.txt` | `e62d731` | **absent** |
| 7 | `reports/round-73/accept-ca.py` r2 + `counter-revisions.md` + `controls-ca-r2.txt` + `selftest-r2.txt` + SKILL.md `accept-ca-73` row text | `3537899` | **absent** |
| 8 | two knowledge entries (105 + 90 lines) | `85f17eb` | **absent** |
| 9 | `corpus/SOURCES.md` +5 rows (831-835) | `85f17eb` | **absent** |
| 10 | `corpus/lessons/round-73.md` (141 lines at `85f17eb`, 142 at lands) | `85f17eb` (+1 line `0316b88`) | **absent** |
| 11 | `corpus/QUALITY.md` +14 (criteria 22, 23) | `85f17eb` (+1 line `0316b88`) | **absent** |
| 12 | `corpus/README.md` +14 (round-73 footer) | `85f17eb` (+1 line `0316b88`) | **absent** |
| 13 | `accept-ca.py` r3, `counter-revisions.md` +4, `controls-ca-r3.txt`, `selftest-r3.txt`, `red-before-r3.txt`, `quality22-controls.txt`, `census-end.txt` | `85f17eb` | **absent** |
| 14 | `assimilation/id-renumber-map.json` (`map` key), `validate-receipt.txt` ids block, `gap-sweep.txt` section [7], README footer without claim-C ids, lesson R73-M6 row | `0316b88` | **absent** |

**LOG.md entry: none exists at the measured revision.**

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ grep -c '^## Round 73' LOG.md
0
$ git diff --numstat 8841ad3b896a0227674fa0725b818c999118046f 0316b8883b4f8d44b8efd720140e7f52f734a102 -- LOG.md | wc -l
0
$ grep -n '^## Round ' LOG.md | tail -1
4278:## Round 72 - 2026-10-25 (hyaku run 6, L1 kotodama-r72; repair-first + first shokuknow adoption)
```

So the "every change tied to a LOG.md entry" column cannot be filled at `0316b88`: the round-73 LOG
entry is a close-time obligation that must land in the records commit (the round-72 pattern puts it
there). Until it lands, SHONEN box 2 ("At least one end-to-end domain task executed and logged in
LOG.md") has no round-73 pointer. Marked as F1 in §8.

## 3. Before → after measurements

### Claim C (coverage)

Frozen `before` commands from `reports/round-73/claims.json:80`, run at both revisions:

```
$ C=<clone>; for REV in 8841ad3b896a0227674fa0725b818c999118046f 0316b8883b4f8d44b8efd720140e7f52f734a102; do
    git -C "$C" checkout -q --detach $REV; echo "=== $REV ==="
    find corpus/knowledge -iname '*conlang-scholarship*' | wc -l
    find corpus/knowledge -iname '*conlang*' | wc -l
    grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
    grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md | grep -oE 'S[0-9]{3,}' | tail -1
    find corpus/knowledge -type f -name '*.md' | wc -l
  done
```

| measurement | base `8841ad3` | lands `0316b88` |
|---|---|---|
| `*conlang-scholarship*` files | 0 | 2 |
| `*conlang*` files | 2 | 4 |
| registry rows (`grep -cE '^ {0,3}\|…S[0-9]{3,}…'`) | 799 | 804 |
| last registry id | S875 | S880 |
| `corpus/knowledge` `.md` files | 245 | 247 |
| `linguistics/` `.md` files (`find corpus/knowledge/linguistics -type f -name '*.md' \| wc -l`) | 30 | 32 |
| five URL fragments in `corpus/SOURCES.md` (`git show <rev>:corpus/SOURCES.md \| grep -cF '<frag>'`) | 0, 0, 0, 0, 0 | 1, 1, 1, 1, 1 |

The fragment line, verbatim:

```
=== 8841ad3b896a0227674fa0725b818c999118046f ===
  ojs.unito.it: 0
  philol.msu.ru: 0
  journals.rudn.ru: 0
  cyberleninka.ru/article/n/klassifikatsii: 0
  sanders.phonologist.org: 0
=== 0316b8883b4f8d44b8efd720140e7f52f734a102 ===
  ojs.unito.it: 1
  philol.msu.ru: 1
  journals.rudn.ru: 1
  cyberleninka.ru/article/n/klassifikatsii: 1
  sanders.phonologist.org: 1
```

Counter, declared command `python3 -B reports/round-73/accept-c.py --root . --lands <lands>`
(`reports/round-73/claims.json:156`), run in the fleet-shaped clone:

```
LEG PASS ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND / CITEDLINES
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r73-fleet-ri5lduof/kotodama-shokunin/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-73: PASS legs=11/11
EXIT=0
```

Do-nothing control (`--lands 8841ad3`, same clone): `ACCEPT-C-73: FAIL legs=1/11`, only `CENSUS`
green — matches `reports/round-73/telemetry/controls-c.txt` and
`reports/round-73/claims.json:156`. (In a *bare* clone the same control reads `FAIL legs=0/11`
because CENSUS cannot find the census script; F3.)

CITEDLINES re-derived directly:

```
$ python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/conlang-scholarship.md \
      corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
CITED-LINES: 0 finding(s) in 2 file(s)
```

### Claim Ca (calibration)

`before` (claims.json:163): 8 of 8 pairs red at base. Ledger:

```
$ python3 -c "import json;d=json.load(open('reports/round-73/ledger.json'));print(len(d['pairs']), [p['id']+':'+p['disposition'] for p in d['pairs']])"
8 ['L01:ANNOTATE', 'L02:ANNOTATE', 'L03:ANNOTATE', 'L04:REPAIR', 'L05:REPAIR', 'L06:ANNOTATE', 'L07:ANNOTATE', 'L08:REPAIR']
```

| measurement | base `8841ad3` | lands `0316b88` |
|---|---|---|
| round-72 seat reports tracked (`git ls-tree -r <rev> --name-only -- .ufo/waves/round-72/w1/ScoutMergeScan.md .ufo/waves/round-72/w1/ScribeLesson.md \| wc -l`) | 0 | 2 |
| L04 truth (`grep -n '^## Error patterns$' SKILL.md`) | statement `468`, truth `505` | statement `505` = truth |
| L05 truth (`grep -n '^## Checklist (executable where a tool exists)$' SKILL.md`) | statement `522`, truth `564` | statement `564` = truth |
| L08 truth (last `accept-*.py` under `reports/`) | statement `accept-o-69`, truth `accept-ca-72` | statement `accept-ca-73` = truth |
| counter `python3 -B reports/round-73/accept-ca.py --root . --lands <lands> --fleet-root /home/vgpnk/Projects/shokunin` | `FAIL legs=5/9` (r1 + explicit `--ledger`, receipt `controls-ca.txt`); `FAIL legs=4/9` (r3 + explicit `--ledger`, receipt `controls-ca-r3.txt`); `FAIL legs=1/9` (r3, declared command, no `--ledger`, this seat's run) | `PASS legs=9/9` |

Lands run, verbatim (trimmed to the legs):

```
# stamped revision: 0316b8883b4f8d44b8efd720140e7f52f734a102
# evaluated revision: 0316b8883b4f8d44b8efd720140e7f52f734a102
# measured revision (lane main): 0316b8883b4f8d44b8efd720140e7f52f734a102
# tree: 9b10fa06a2d3756c8bacfc8fc7b2115921370d97
# ledger: reports/round-73/ledger.json source=lands sha256=c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9
LEG PASS LEDGER      pairs=8 min=8
PAIR L01 ANNOTATE stated='243' observed_base='245' observed_lands='245'
PAIR L02 ANNOTATE stated='36'  observed_base='38'  observed_lands='38'
PAIR L03 ANNOTATE stated='243' observed_base='245' observed_lands='245'
PAIR L04 REPAIR   stated='468' observed_base='505' observed_lands='505'
PAIR L05 REPAIR   stated='522' observed_base='564' observed_lands='564'
PAIR L06 ANNOTATE stated='PASS' observed_base='FAIL' observed_lands='FAIL'
PAIR L07 ANNOTATE stated='F1-F9' observed_base='F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE'
PAIR L08 REPAIR   stated='accept-o-69' observed_base='accept-ca-72' observed_lands='accept-ca-73'
LEG PASS BASEMISMATCH  found=8 min=8
LEG PASS REPAIR        green=['L04', 'L05', 'L08'] red=[]
LEG PASS ANNOTATE      rows=9 annotate-pairs=5 unannotated=0
LEG PASS NOSTUB        stubs=[]
LEG PASS APPENDONLY    lane-removed=0 fleet-pin=80d8c9b576d4 in-place=['SKILL.md(registry)', 'corpus/README.md(footer)']
LEG PASS SEPARABLE     problems=[]
LEG PASS TRACKED       paths=2 problems=[]
LEG PASS STAMP         stamped=evaluated=measured=0316b8883b4f tree=9b10fa06a2d3 counter=222d4dd6d408
ACCEPT-CA-73: PASS legs=9/9
EXIT=0
```

Filed statements the ANNOTATE rows point at, re-read in the clone
(`sed -n '732p;407p;736p' corpus/README.md`, `sed -n '1401p' SCORECARD.md`, `sed -n '4280p' LOG.md`):
`Total knowledge entries: 243.` / `## culture-material/ (36)` / `(total 243 files; directory totals
30/29/36/29/24/95).` / `…ACCEPT-CA-72 PASS legs=12/12 at the measured revision` / `…pre-data
corrections F1-F9 + SCOUT-LIVE documented there`. All five still read as filed (annotated, not
rewritten).

## 4. Sources & frontier

- **Registry 799 → 804 rows.** Count command:
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `799` at base,
  `804` at lands. Diff shape: `git diff --numstat 8841ad3 0316b88 -- corpus/SOURCES.md` → `5  0`
  (five added, none removed, no in-place edit).
- **Rows added by tier** — B ×5:

```
$ awk -F'|' '/^ *\| *S87[6-9] *\||^ *\| *S880 *\|/ {gsub(/^ +| +$/,"",$5); print $2, $5}' corpus/SOURCES.md
 S876  B
 S877  B
 S878  B
 S879  B
 S880  B
```

  Row cells (same awk over `$9,$10,$11,$12`): `status=mined`, `opened=2026-10-25`, `recheck=180d`,
  `used-by=corpus/knowledge/linguistics/conlang-scholarship.md` (S876, S877) /
  `…conlang-scholarship.amend-2026-10-23.md` (S878, S879, S880). Tier rationale for S877 (B, not the
  scout's A) and the S879 live-leg-only caveat: `corpus/lessons/round-73.md:33-39`.
- **Frontier rows advanced** — none in place: the five new rows *are* the advance, and no pre-existing
  row's `status`/`recheck`/`used-by` moved (numstat `5 0` above). [L1: if "advanced" is meant as
  re-verified rows, the answer is 0 and the command is the same numstat.]
- **Census, exit 0 at both ends** — `reports/round-73/telemetry/census-start.txt` (32 lines, 28 `W04`
  + `kotodama ok`, `exit=0`, header pins base `8841ad3` and `2026-10-25T22:01:18Z`) and
  `census-end.txt` (31 lines, same 28 `W04`, `exit=0`). Re-derived live by this seat:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama > /tmp/ScribeReportDraft/census-live.txt; echo "exit=$?"
exit=0
$ grep -c '^kotodama' /tmp/ScribeReportDraft/census-live.txt
29
$ tail -1 /tmp/ScribeReportDraft/census-live.txt
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

  (29 = 28 `W04` + the `ok` line, same as both receipts. `census-end.txt` carries no
  `# census-end round 73 — <rev>` header and no timestamp; F6.)
- **Assimilation: ADOPTED — one theme, two entries.**
  `corpus/knowledge/linguistics/conlang-scholarship.md` +
  `conlang-scholarship.amend-2026-10-23.md`; five rows re-pointed by document
  (staged S881→S876, S882→S877, S892→S878, S893→S879, S901→S880); refused staged S869/S894/S910 and
  four not-adopted staged files named in `corpus/lessons/round-73.md:42-58`; four families named as
  not adopted. Collision guard: `reg-ids` 799, `staged-ids` 132, `collisions` 17 (S859..S875), the
  adopted ids absent from both id files.
- **`considerthese` absent for this lane**:

```
$ ls -d /home/vgpnk/Projects/shokuknow/considerthese
ls: cannot access '/home/vgpnk/Projects/shokuknow/considerthese': No such file or directory
```

## 5. Trend verdicts

Three verdicts (LEARNING.md observables; `SCORECARD.md:1387-1399` names the set and QUALITY 20
(`corpus/QUALITY.md:61`) forbids firing a trend on a record repair):

- **expansion: [L1 to fill]**
- **quality: [L1 to fill]**
- **discernment: [L1 to fill]**

Round shape / wave totals:

- **Wave-2 totals: [L1 to fill]** — the wave-2 spec carries 33 items
  (`python3 -c "import json;print(len(json.load(open('.ufo/waves/round-73/w2/spec.json'))['items']))"`
  → `33`), and wave-1 was 37 seats with 34 report files on disk (§7). Round total and the dead-seat
  count in wave 2 are L1's to settle.
- Round shape line (fact, not verdict): one wave-1 of 37 seats
  (`.ufo/waves/round-73/w1/w1-results.json` `"seats": 37`), role mix `scout 11, scribe 6, executor 6,
  critic 5, reviewer 4, connector 2, mutation-tester 1, sentinel 1, simplifier 1`.

## 6. SHONEN

`SHONEN.md` holds four boxes; all are `[~]` (lane-asserted). One line per box, pointers only:

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  pointers `SKILL.md:20`, `:505`, `:564` (repaired round 73, pairs L04/L05); registry row count 43
  (`grep -c '^| accept-' SKILL.md`); **no non-author verifier on record**.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — round-51 chain is the
  filed pointer (`SHONEN.md:7`); **round 73 has no LOG.md entry yet** (F1), so no round-73 pointer
  exists; **no non-author verifier on record**.
- `[~]` Instructions executable by an agent without oral context — round-50 fresh-clone re-runs
  (`SHONEN.md:9`); **no non-author verifier on record**.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — round-51 connector sweep + the
  `worldbible-integration-contract.md` handoff cited by both round-73 entries; the round-73
  connector seat `ConnectorSiblings` returned nothing (dead), so the round-73 sweep evidence is
  `ScoutGapSweep` §[5] (20 sibling lanes, 0 files) plus PROVINCE.md; **no non-author verifier on
  record**.

No box is `[x]`: the mark requires a named non-author verifier per **Promotion gates**
(`SHONEN.md:14-15`), and none is on record.

## 7. Extras

- **Stale-lane:** none. The lane carries exactly one open mission, round 73, in flight:
  `grep kotodama /home/vgpnk/Projects/shokunin/.ufo/watchdog.log | tail -1` →
  `2026-10-25T18:56:34-03:00 launch kotodama round=73 pgid=88120 driver=hyaku-inline attempt=1`
  (no `complete` line for round 73); `git -C kotodama-shokunin status --porcelain` lists only four
  untracked round-73 wave paths (`build-w2.py`, `w2.ready`, `w2.ready.dispatched`, `w2/`).
- **Tool installs: none.** Thirteen wave-1 seat reports state it explicitly, e.g.
  `grep -rn "pacman\|uv tool install\|npx " .ufo/waves/round-73/w1/*.md` →
  `ScoutAmendTriage.md:19 "No tools installed/updated; pacman not run"`,
  `ExecRenumber.md:8 "Tools installed: none"`, `SimplifierRows.md:144 "Tools installed or upgraded:
  none"`, `ConnectorPatterns.md:7`, `ExecCaCounter.md:263`, `ExecLedger.md:7`,
  `ExecReceiptRerun.md:146`, `RevAssimilationContract.md:7`, `RevSowersAccess.md:97`,
  `ScoutLedgerSweepA.md:75`, `ScoutMapIds.md:5`, `ScoutS892.md:162`, `ScoutS893.md:176`,
  `ScribeEntryBase.md:200`. This seat installed nothing.
- **Dead seats (3 of 37): `ConnectorSiblings`, `ScribeMistakes`, `ExecScratchMirror`.** No error text
  exists anywhere in the lane for them:

```
$ ls .ufo/waves/round-73/w1/*.md | wc -l
34
$ python3 -c "... missing = [names without a report file]"
no report file: ['ConnectorSiblings', 'ScribeMistakes', 'ExecScratchMirror']
$ wc -c .ufo/waves/round-73/w1/dispatch.err .ufo/waves/round-73/w2/dispatch.err
0 .ufo/waves/round-73/w1/dispatch.err
0 .ufo/waves/round-73/w2/dispatch.err
```

  The only recorded text is one generic note repeated for **all 37** results in
  `w1-results.json`, every `output` being `null`: "orchestrator kernel restarted mid-wave; seat
  output was delivered to the orchestrator session but not retained — read the seat report file in
  the wave dir". So the "last error" for the three dead seats is *not recoverable from the lane*
  (F5); the work they owed was done by the L1 (`corpus/lessons/round-73.md:140-142`).

## 8. Findings from this seat's re-runs (draft-blocking)

Each finding has the command that produced it. Severity: BLOCKER = a claim leg or an admitted
statement is wrong; MAJOR; MINOR.

- **F1 — MAJOR — no round-73 LOG.md entry at lands.** The report cannot tie any landed change to a
  LOG.md entry, and SHONEN box 2 has no round-73 pointer.
  `grep -c '^## Round 73' LOG.md` → `0`; `git diff --numstat 8841ad3 0316b88 -- LOG.md | wc -l` → `0`.
- **F2 — MAJOR — neither counter has a committed data-run receipt.** `reports/round-73/telemetry/`
  holds controls and selftests only: `ls reports/round-73/telemetry/ | grep measures` →
  `measures-ca72-rerun.txt` (a round-*72* rerun). There is no `measures-c.txt` and no
  `measures-ca.txt`, unlike rounds 71/72. The PASS lines in §3 are therefore this seat's runs, not a
  committed receipt; commit `85f17eb`'s message says "counter r3 + receipts" but the receipts it adds
  are `controls-ca-r3`, `selftest-r3`, `red-before-r3`, `quality22-controls`, `census-end`.
- **F3 — MAJOR — claim C's declared counter command is not self-contained.** `accept-c.py` resolves
  the census script as `--census-sh` or `KOTODAMA_CENSUS_SH` or `<fleet_root>/scripts/sources-census.sh`,
  with `fleet_root` defaulting to `os.path.dirname(abspath(--root))` (`reports/round-73/accept-c.py:926-929,1186`).
  In a throwaway clone outside the fleet root the *declared* command
  (`--root . --lands 0316b88`) prints:

```
LEG FAIL CENSUS
     census script not found: /tmp/ScribeReportDraft/tmp.6VzBNC47uc/scripts/sources-census.sh
ACCEPT-C-73: FAIL legs=10/11
EXIT=1
```

  The same command prints `PASS legs=11/11` only when the clone's parent holds
  `scripts/sources-census.sh` (§3). Same root cause makes the C control read `FAIL legs=0/11` in a
  bare clone instead of the declared `1/11`. Fix for the report: name the fleet-shaped parent (or
  `--fleet-root`/`--census-sh`) in the command it prints.
- **F4 — BLOCKER (admitted statement) — claims.json's Ca do-nothing control numbers do not reproduce
  with the landed counter.** `reports/round-73/claims.json:178` states "lands == base FAILS
  (ACCEPT-CA-73: FAIL legs=5/9; red: REPAIR, ANNOTATE, NOSTUB, TRACKED; green and unmoved: LEDGER,
  BASEMISMATCH, APPENDONLY, SEPARABLE, STAMP)". That is the **r1** run in `controls-ca.txt`. The
  landed counter is r3 (`sha256 222d4dd6…`); its own control receipt `controls-ca-r3.txt` reads
  `FAIL legs=4/9` (STAMP also red, because lane main had moved), and the *declared* command with no
  `--ledger` reads:

```
$ python3 -B reports/round-73/accept-ca.py --root . --lands 8841ad3b896a0227674fa0725b818c999118046f \
      --fleet-root /home/vgpnk/Projects/shokunin
LEG FAIL LEDGER / BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB / APPENDONLY
LEG PASS SEPARABLE
LEG FAIL TRACKED / STAMP
ACCEPT-CA-73: FAIL legs=1/9
```

  (LEDGER is red at `lands == base` because the ledger is committed at the freeze `af65165`, not at
  base — `reports/round-73/ledger.json` is absent from the base tree.) The revision is disclosed in
  `counter-revisions.md` and in the r3 receipt header, but the frozen sentence is still wrong as
  written against the landed counter; the remedy is a SCORECARD/lesson correction row, never a
  claims.json edit.
- **F5 — MINOR — the wave-1 results file cannot distinguish dead from live seats and carries no
  error text.** `w1-results.json`: 37 results, every `output: null`, one identical note for all 37.
  Dead-seat evidence is only the absent report files (§7).
- **F6 — MINOR — `census-end.txt` pins no revision.** First line is
  `$ …/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama  (round end, after the
  registry append)` — no `# census-end round 73 — <rev> — <timestamp>` header, unlike
  `census-start.txt:1` (`# census-start round 73 — base 8841ad3… — 2026-10-25T22:01:18Z`). The
  receipt's `ok` line names a worktree path, not a commit.
- **F7 — MINOR — `counter-revisions.md`'s table is broken at r2.** r2's row says
  `sha256 = "see \`sha256sum\` below"`, and the hash sits on a bare line between the r2 and r3 rows
  (`be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0  reports/round-73/accept-ca.py`),
  outside any table row — `sed -n '1,12p' reports/round-73/counter-revisions.md`.
- **F8 — MINOR — the selftest receipts contain an error line inside a passing run.**
  `selftest.txt`, `selftest-r2.txt`, `selftest-r3.txt` each print
  `ERROR: base 8841ad3… is not a commit in /tmp/r73-ca-selftest-…/lane` immediately before
  `SELFTEST OK: …`. A receipt that a re-opener greps for `ERROR` reads as red. Also note the scenario
  count moved 9 → 10 between `selftest.txt`/claims.json and `selftest-r3.txt` (r3's new scenario 7b);
  claims.json's "9 scenarios" is r1's.

## 9. What this seat could NOT check

- **Live source reachability and the truth of the five quotes.** No fetch was made by this seat, so
  the `http-status: 200`, `bytes`, `sha256` and `quote-found-verbatim: yes` lines in
  `reports/round-73/evidence/S87*.txt` are reproduced *as committed bytes*, not re-measured; no UA
  record is claimed for this report. The Gate rows' Springer/Cambridge 200/429 readings
  (`corpus/lessons/round-73.md:47-48`, QUALITY 22) are likewise quoted, not re-probed.
- **Whether claim C's 11 legs survive the wave-2 attacks** (mutation, forge, junk-landing) — that is
  the other seats' work; this draft records only the counter's own PASS at `0316b88`.
- **The shokuknow staged bytes themselves** — read-only lane discipline; the staged entries and rows
  are cited from the lesson and the renumber map, never opened.
- **The round-72 counter's `SELFTEST: 10/11` (R73-M4)** — recorded from the lesson/SCORECARD, not
  re-run by this seat.
- **Wave-2 totals and the three trend verdicts** — left as `[L1 to fill]` by design.
- **jj state** — not queried; all revision claims above are git-only against the lane.

## 10. Provenance of this file

Written by seat ScribeReportDraft at
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/w2/ScribeReportDraft.md`
(the only lane write made by this seat). Scratch: `/tmp/ScribeReportDraft/` (clone
`tmp.6VzBNC47uc`, fleet-shaped clone `fleet2/`, `SOURCES-*.md`, `census-live.txt`, `logmap.txt`).
No lane/git state was mutated, no fleet write, no shokuknow write, no delegation, no background job.
Tools installed: none.
