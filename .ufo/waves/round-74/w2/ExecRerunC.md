# ExecRerunC — round 74 / wave 2 / claim-C measurement attack

Seat: `ExecRerunC` · role: executor (leaf, no subagents; no labrat needed — every check below is a local command)
Target: claim **C** (shokuknow worldbuilding-setting-practice assimilation), the measurement only.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only except this file).
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb` · freeze `00c408a0af2fa5ddf65af2224152ce258b26d896` · claim-C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`.
All counter runs were done inside a clone created by the mandated rule (never against the lane worktree's git state):

```
$ D=$(mktemp -d) && echo "D=$D" && git -C "$D" init -q && git -C "$D" rev-parse --show-toplevel
D=/tmp/tmp.QGfOC1Gu8G
/tmp/tmp.QGfOC1Gu8G
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
$ git -C "$D/lane" checkout -q --detach c4bf61a8d722... && git -C "$D/lane" branch -f main c4bf61a8d722... && git -C "$D/lane" checkout -q main
$ git -C "$D/lane" rev-parse HEAD
c4bf61a8d722f9168ce0fd8021a6261c000610c5
```

A second, independent clone was made at base for the before-values (same rule; removed after use).

---

## A. The counter exactly as the claim states — PASS reproduced

Claim C's `counter` field (`reports/round-74/claims.json`, frozen at F3):

```
python3 -B reports/round-74/accept-c.py --root . --lands <lands> --freeze <freeze>
```

Command actually run (the seat brief adds `--fleet-root`, and the claim's own `after` sentence also prints PASS with it):

```
$ cd /tmp/tmp.QGfOC1Gu8G/lane
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
# round-74 acceptance counter — claim C (shokuknow worldbuilding-setting-practice assimilation)
# counter sha256 (self): 8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a
# stamped revision: c4bf61a8d722f9168ce0fd8021a6261c000610c5
# evaluated revision: c4bf61a8d722f9168ce0fd8021a6261c000610c5
# measured revision (lane main): c4bf61a8d722f9168ce0fd8021a6261c000610c5
# tree: 29c8c147c948b9fe03af8f092ac92028a23fed56
# base revision: f7104cbce186bc2e1522abf0cfd619cc834628bb
# freeze revision: 00c408a0af2fa5ddf65af2224152ce258b26d896
# config sha256 (frozen claims.json): 270e31790e2932c8d418904e16e721a6ae5343e4e2c157e5409c1c27dfdeca19
# config source: git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/claims.json (never the graded tree)
# frozen legs: 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX)
# frozen map: .ufo/waves/round-74/assimilation/id-renumber-map.json sha256=d3573f7d3cf23afa7296c281d201225eed643aef2b406b3a403c2a67aeb24afa
# materialized: git clone of /tmp/tmp.QGfOC1Gu8G/lane, checkout --detach c4bf61a8d722 at /tmp/r74-lands-glglnu4t/clone
# worktree graded: no (leg bytes read only from the checkout and the git-archive base tree)
# lane worktree HEAD (disclosure only): c4bf61a8d722f9168ce0fd8021a6261c000610c5
# access date: 2026-10-25
# adopted rows: S881 S882 S883 S884 (staged S883 S884 S899 S900)
# reused rows: S877 (staged S882)
# entries: corpus/knowledge/culture-material/worldbuilding-setting-practice.md ; corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md

LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r74-fleet-sz3e2_lf/kotodama-shokunin/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
LEG PASS FROZENCFG
     constants from git show 00c408a0af2f:reports/round-74/claims.json (sha256 270e31790e2932c8): rows=S881 S882 S883 S884 reused=S877 entries=2 fragments=3 cjk_terms=3 refused=S882 forced=S899,S900 access_date=2026-10-25
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13
EXIT=0
```

The claim's `after` assertion (`ACCEPT-C-74: PASS legs=13/13 (exit 0)`) reproduces exactly. Repeated with `main` moved away from lands and back: 13/13 both times (see F1).

## B. Before-values at base — all five equalities hold

Second clone at `f7104cbc…` (clean checkout, so worktree == tree):

```
=== B1 worldbuilding-setting files ===
$ find corpus/knowledge -iname '*worldbuilding-setting*' | wc -l
0
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
804
=== B3 fragment counts (grep -cF over corpus/SOURCES.md) ===
litmemo.com=0
tuduku.space=0
chinawriter.com.cn=0
$ grep -rlE '設定ノート|世界観|世界观' corpus/knowledge | wc -l
0
$ find corpus/knowledge -name '*.md' | wc -l
247
$ find corpus/knowledge -type f -name '*.md' | wc -l
247
last registry ids: S878 S879 S880
```

Claim's `before` states 0 / 804 (last id S880) / 0 0 0 / 0 / 247. **All five equalities hold exactly.**

## C. After-values at lands — all three equalities hold

Same commands in the clone at `c4bf61a8d722…`:

```
$ find corpus/knowledge -iname '*worldbuilding-setting*' | sort
corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
corpus/knowledge/culture-material/worldbuilding-setting-practice.md
count=2
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
808
fragments: litmemo.com=1  tuduku.space=1  chinawriter.com.cn=2
$ grep -rlE '設定ノート|世界観|世界观' corpus/knowledge | wc -l
2
$ find corpus/knowledge -name '*.md' | wc -l          # 249
$ find corpus/knowledge -type f -name '*.md' | wc -l  # 249
last registry ids: S879 S880 S881 S882 S883 S884
```

| quantity | claim before (base) | measured base | claim after (lands) | measured lands | delta |
|---|---|---|---|---|---|
| `*worldbuilding-setting*` files | 0 | **0** | 2 (two named entries) | **2** | +2 |
| registry rows (`^ {0,3}\| S###+ \|`) | 804, last S880 | **804, last S880** | 808 | **808** | +4 |
| litmemo/tuduku/chinawriter counts | 0 0 0 | **0 0 0** | (not stated as a number) | **1 1 2** | — |
| CJK grep files | 0 | **0** | (not stated) | **2** | +2 |
| knowledge `.md` files | 247 | **247** | 249 | **249** | +2 |

No difference between a stated value and the measured value.

## D. Selftest

```
$ python3 -B reports/round-74/accept-c.py --selftest
SELFTEST: 69/69 scenarios
EXIT=0
```

Committed receipt `reports/round-74/telemetry/selftest-c.txt` carries the identical line (`69/69`, `exit=0`); counter sha256 at freeze == at lands == `8d30487f…ca5433a`, so the selftest is the frozen one.

---

## Findings

### F1 — LOW — `measured revision (lane main)` is not measured; it echoes `--lands`
What it attacks: the receipt's own revision stamp.

Command (inside the clone; branch moves only in the clone):

```
$ git checkout -q --detach c4bf61a8d722f9168ce0fd8021a6261c000610c5
$ git branch -f main 00c408a0af2fa5ddf65af2224152ce258b26d896
lane main now: 00c408a0af2fa5ddf65af2224152ce258b26d896      # NOT the lands
lane HEAD now: c4bf61a8d722f9168ce0fd8021a6261c000610c5
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722... \
    --freeze 00c408a0af2f... --fleet-root /home/vgpnk/Projects/shokunin
# stamped revision: c4bf61a8d722f9168ce0fd8021a6261c000610c5
# evaluated revision: c4bf61a8d722f9168ce0fd8021a6261c000610c5
# measured revision (lane main): c4bf61a8d722f9168ce0fd8021a6261c000610c5   <-- false here
ACCEPT-C-74: PASS legs=13/13
EXIT=0
```

Cause (raw): `reports/round-74/accept-c.py:1871` — `print("# measured revision (lane main): %s" % lands)`. No leg of claim C reads the clone's `main` (contrast claim Ca's STAMP leg), so the verdict is unaffected: the graded bytes are the detached checkout of `--lands`, which is what the legs read. But the header asserts a fact it never observed.
Proposed fix: either print `git -C <root> rev-parse main` (and name the checkout separately) or relabel the line `graded checkout (--lands)`. Verdict impact: none for claim C; claim survives.

### F2 — LOW — the claim's own `counter` command fails outside the fleet root (no `--fleet-root`)
What it attacks: reproducibility of the command as written in `claims.json` (`counter`, and the first sentence of `after`).

```
$ cd /tmp/tmp.QGfOC1Gu8G/lane
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722... --freeze 00c408a0af2f...
...
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG FAIL CENSUS
     census script not found: /tmp/tmp.QGfOC1Gu8G/scripts/sources-census.sh
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
LEG PASS FROZENCFG
LEG PASS INDEX
ACCEPT-C-74: FAIL legs=12/13
EXIT=1
```

Cause: `--fleet-root` defaults to `os.path.dirname(os.path.abspath(root))` (`accept-c.py:1962`). In the real lane that parent is `/home/vgpnk/Projects/shokunin` (the fleet root) and the default works, which is why the claim's command is valid there; in any clone outside the fleet, the same command degrades to a false FAIL on CENSUS only. The seat brief's command (with `--fleet-root`) is the one that passes.
Proposed fix: write the `--fleet-root /home/vgpnk/Projects/shokunin` argument into the claim's `counter` string (the assignment's command already does), or fall back to searching known fleet roots before failing.
Verdict impact: none when graded with the brief's command; claim survives.

### F3 — LOW (record placement; would be MEDIUM under a strict "receipt at `<lands>`" reading) — declared junk-landing receipt is not at the claim's lands
What it attacks: `do_nothing_control`'s third clause, which names `reports/round-74/telemetry/junk-c.txt`.

```
$ git -C <clone> ls-tree --name-only c4bf61a8d722... reports/round-74/telemetry/
accept-c-73-at-lands.txt  accept-ca-73-at-lands.txt  census-end.txt  census-start.txt
controls-c.txt  controls-ca.txt  gap-sweep.txt  selftest-c.txt  selftest-ca.txt
        # no junk-c.txt (and no junk-ca.txt) — same list at the freeze 00c408a0
$ git ls-tree --name-only 1d7add3 reports/round-74/telemetry/ | grep junk
reports/round-74/telemetry/junk-c.txt
reports/round-74/telemetry/junk-ca.txt
$ git merge-base --is-ancestor c4bf61a8d722... 1d7add3 && echo descendant
descendant
```

So the junk controls exist only in `1d7add3` (a descendant of lands, added after the claim landed; the same topology applies to `measures-c.txt`, which is also only in `1d7add3`). This is structurally expected — a receipt for `<lands>` cannot be committed inside `<lands>` — and no claim-C leg reads the file, so the kill rule is untouched. The residual is that a grader restricted to `<lands>` cannot audit the declared red-before. Content is otherwise as declared: `junk-c.txt` (from `1d7add3`) has the stub-entry fixture (ENTRIES red), the staged-rows/copied-rows fixture (ROWS red), the quote-absent + typed `quote-found: yes` fixture (EVIDENCE red) and the graded-tree `claims.json` edit (FROZENCFG red), all `accepted: no`.
Proposed fix: reference the receipt commit (`1d7add3`) in the lesson's controls index, or let the claim name the receipt's provenance commit rather than a bare path.

### F4 — LOW — the do-nothing control's red-leg list is non-exhaustive
What it attacks: `do_nothing_control` clause (1) ("FAILS with ENTRIES, ROWS, GATE, EVIDENCE, REJECTS, INDEX red and FROZENCFG green").

```
$ python3 -B reports/round-74/accept-c.py --root . --lands 00c408a0af2f... --freeze 00c408a0af2f... \
    --fleet-root /home/vgpnk/Projects/shokunin
LEG FAIL ENTRIES
LEG FAIL ROWS
LEG FAIL REPOINTED
LEG FAIL GATE
LEG FAIL EVIDENCE
LEG FAIL REJECTS
LEG PASS GROUND
LEG FAIL CITEDLINES
LEG PASS CENSUS
LEG FAIL SCRATCHMIRROR
LEG PASS COLLCHECK
LEG PASS FROZENCFG
LEG FAIL INDEX
ACCEPT-C-74: FAIL legs=4/13
EXIT=1
```

Nine legs are red: the six the claim lists **plus REPOINTED, CITEDLINES, SCRATCHMIRROR**; four are green including FROZENCFG (as declared). The claim's list is a true subset, not a false statement, and the committed `controls-c.txt` shows the full set, so a reader of the receipt is not misled. Reproduced exactly: `FAIL legs=4/13`, exit 1 — identical to `reports/round-74/telemetry/controls-c.txt`.
Proposed fix: list all nine, or write "among others". Verdict impact: none; claim survives.

### F5 — LOW (inherited README defect; outside every claim-C leg) — stale section labels in the graded README
What it attacks: the claim's INDEX context, not the INDEX leg. The INDEX leg (`footer total == 249`, vector == partition counts) passes, but the same file's section headers disagree with the file counts:

```
$ grep -nE '^## ' corpus/README.md     # at lands
344:## linguistics/ (30)         # actual 32
376:## myth-symbol/ (29)          # 29
407:## culture-material/ (36)     # actual 40
447:## synthesis/ (29)           # 29
479:## verification/ (24)        # 24
505:## civilizations/ (95)      # 95
$ tail -1 footer; total 249 files; directory totals 32/29/40/29/24/95
```

Labels sum to 243 vs the footer's 249. At base the same two labels were already stale (`(30)` with 32 files, `(36)` with 38 files per the L02 correction), so claim C did not introduce the inconsistency and no leg gates it; adding two culture-material files widened it from 2 to 4 (`(36)` vs 40).
Proposed fix: update the two labels (a future round; frozen claim bytes are not rewritten).

### Observations — measured and reconciled, not defects
- **Evidence date straddle.** Every evidence file records `access-date: 2026-10-25` and `fetched: 2026-10-26T01:09Z`. The host is at `-03` (`date -u` = 2026-10-26 02:05Z; local = 2026-10-25 23:05 `-03`), so 01:09Z is 22:09 local on 2026-10-25: same access date in the fetch host's timezone. A UTC-only reader would see a one-day difference; the claim fixes no timezone, and `_evidence_core` compares only `access-date`.
- **Lesson R74-M6 wording** ("accept-c.py's leg_evidence does not read the floor, so the limb is vacuous here") is accurate only for `whole-document` scope: `_evidence_core` *does* enforce `>= 4096` for `excerpt` and enforces `< 4096` + `visible-chars == len(window)` for `whole-document`, which is exactly the claim's rule. S882 (2953 chars) is legitimately `whole-document`; the four `excerpt` windows are 4098/4098/4104/4103 chars.

---

## Attacks that FAILED (the claim survived) — with the evidence

1. **Counter verdict.** PASS 13/13, exit 0 at `c4bf61a8d722…` (section A). Repeated runs produced the same verdict; only the temp paths differ.
2. **Before-values.** 0 / 804 (last S880) / 0 0 0 / 0 / 247 measured exactly (section B).
3. **After-values.** 808 / 249 / 2 measured exactly (section C).
4. **Registry diff is exactly as declared.**
   ```
   $ git diff f7104cbc... c4bf61a8... -- corpus/SOURCES.md | grep -E '^[-+][^-+]'   # six lines only
   -| S877 | ...   +| S877 | ...   +| S881 | ...   +| S882 | ...   +| S883 | ...   +| S884 | ...
   ```
   Parsed per row: base 804 rows, lands 808; added `['S881','S882','S883','S884']` (contiguous), removed none; the only changed line is S877 and only its **last cell** changed (`used-by`), other 10 cells byte-identical; the other **803/803** rows byte-identical; no prose/header line changed. The four new rows have 11 cells, `status=mined`, `opened=2026-10-25`, cadence recheck `180d`, source cell carries the mapped URL verbatim, anchor cell carries the quote; used-by is exactly `practice.md` for S881/S882 and `amend-2026-10-23.md` for S883/S884, matching each entry's `source:` lines (entry 1 cites S877,S881,S882; amend cites S883,S884; no other S-id appears inline).
5. **Evidence windows recompute.**
   ```
   S877 window-sha256 MATCH (4098 chars, 7558 B, scope=excerpt, quote present after NFKC+fold)
   S881 MATCH (4098, 11709 B, excerpt, quote present)
   S882 MATCH (2953, 8410 B, whole-document, 2953 == visible-chars, quote present)
   S883 MATCH (4104, 12184 B, excerpt, quote present)
   S884 MATCH (4103, 12226 B, excerpt, quote present)
   ```
   `window-bytes` equals the stored payload's byte length in all five.
6. **The evidence bytes are live-reproducible, not typed.** Re-fetched each URL once with the recorded browser-shaped UA (`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`), no wall, no retry needed, no automation:
   ```
   https://litmemo.com/ja/blog/novel-worldbuilding-guide  200  101615 B  sha256 441fc921…ca64   == evidence
   https://tuduku.space/column/novel-worldbuilding         200   17068 B  sha256 754f504c…c1b7   == evidence
   https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html 200 48536 B sha256 a3b6640c…bee94d == evidence
   https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html 200 62604 B sha256 344de345…d3d659 == evidence
   http://www.philol.msu.ru/~sidorova/files/conlangs.pdf   200 1055723 B sha256 e512a20d…95a9    == evidence
   ```
   (`size_download` for the two chinawriter pages reports the compressed transfer, 16723 / 21341; the decompressed bodies are the recorded 48536 / 62604 — the same relation the evidence's `content-length`/`bytes` pair records for S882, 6260 vs 17068.)
7. **Windows are derivable from the live bodies.** With the evidence's documented extractor reimplemented (drop comments and script/style/noscript/template/svg/head, block tags → newline, entities decoded, blank lines dropped, ASCII spaces collapsed), the S882 stored window equals the live extraction **exactly** (2953 chars, one line); the S881/S883/S884 stored windows are exact substrings of their live extractions (9855 / 8163 / 12271 chars); `pdftotext -enc UTF-8` over the live PDF gives exactly the recorded 492810 visible chars and contains the S877 window (4098 chars) and its quote.
8. **Census passes independently.** Materialized a fleet root with a `kotodama-shokunin` symlink to the lands checkout and the counter's own `shokunin.conf` idiom:
   ```
   $ sources-census.sh validate --root /tmp/seatC_fleet --today 2026-10-25 kotodama
   EXIT=0   E-codes=0   32 output lines (31 W + 1 ok)
   W01: S881, S882 (tier C, mined, used-by practice.md), S884 (tier C, mined, used-by amend)
   W04 x28 inherited from base (S127..S830), none on S877..S884
   ```
9. **Rejects counts re-derived from the staged package (read-only).** `find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge -type f -name '*.md' | wc -l` = **40**; both adopted names present; the four path-present files all differ in sha256 from the lane's bytes; family counts 5 (narrative) + 11 (naming) + 3 (calendar) + 2 (era) + 9 (verification) + 3 (conlang-scholarship b/c/24) + 1 (conlang-methodology 24) = **34** refused; 2 + 4 + 34 = 40. Matches `rejects.counts`.
10. **Frozen identity/ancestry holds.** `git show <freeze>:reports/round-74/claims.json | sha256sum` == `git show <lands>:…` == `270e31790e2932c8…deca19`; the map at freeze hashes to the frozen `d3573f7d…b24afa`; `git rev-list --first-parent <lands>` contains the freeze (and `5e4796c…`, `d7a3840…` in order). The counter sha256 is identical at freeze and lands (`8d30487f…ca5433a`).
11. **Refusal control.** `--lands f7104cbc…` prints `REFUSED: …` + `ACCEPT-C-74: FAIL legs=0/13 (refused …)`, exit 2.
12. **CITEDLINES.** `python3 -B tools/check-cited-lines.py <both entries>` → `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0.
13. **Entry shape.** Word counts 4317 and 2219 (floor 478); every header key present and clean (no `TODO/TBD/FIXME/XXX/n/a/?/—`, no `<…>` token; the `c4bf61a` fix replaced the remaining `<base>/<p>/<n>` template tokens); ≥1 `## ` section (10 and 6).

## Fetch hygiene (QUALITY 21/22/24)
Five fetches, one per source URL, plain `curl` with the exact browser-shaped UA above; each returned HTTP 200 on the first attempt (no wall, no retry, no automation, no bypass). Local time 2026-10-25 `-03` / 2026-10-26 02:0xZ. No CDX "no capture" ruling was needed or made by this seat.

## Tooling
No installs, no upgrades: every tool used was already present (`python3`, `git`, `curl`, `pdftotext`, `grep`, `find`, `sha256sum`). pacman not run.

## Files changed
- `kotodama-shokunin/.ufo/waves/round-74/w2/ExecRerunC.md` (this report) — the only file written in the lane.

## Risks / residual
- The counter cannot prove a fetch happened offline (the claim says so and pairs it with the non-author re-open). This seat's live re-fetch shows body sha256 equality for all five URLs on 2026-10-26 UTC, which is consistency, not proof of the original fetch.
- `/tmp` was at 100% during part of this work (other seats' `r74-lands-*` clones, 169–393 MB each). This seat removed only its own scratch (base clone, fleet symlink dir); no sibling scratch was touched. A counter run needs ~300 MB free in `/tmp`.
