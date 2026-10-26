# ExecCountsSweep — round 74 WAVE 2 (falsify): every counting claim in the landed prose

Seat: `ExecCountsSweep` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze F3 = `00c408a0af2fa5ddf65af2224152ce258b26d896`
(earlier freezes `de93d91c…`, `3595c919…` per R74-M9); claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`;
claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; lane main at attack `1d7add3f7b9eaf6f3349c56c36f6d06325d74236`
(post-freeze commits: `5e4796c`, `d7a3840`, `c4bf61a`, `1d7add3` — all telemetry/LOG/SCORECARD/report-side except `d7a3840`/`c4bf61a`, which are claim C's own landing and fixes).

Attack: grep the landed prose (`corpus/lessons/round-74.md`, `SCORECARD.md` `## Corrections — round 74`,
`SKILL.md` rows, `corpus/README.md` appended block, `QUALITY 25`, both entries' headers) for every number that carries
(or implies) a command, re-derive each, and flag numbers that carry no command.

Method: read-only git against the lane; base and lands trees materialized with `git archive`; both counters and both
selftests re-executed in a clone made per the counter protocol (`mktemp -d` + `git init` + `git clone`), with the clone's
local `main` forced to each claim's lands after `git checkout --detach`. Scratch: `/home/vgpnk/tmp/ExecCountsSweep/`
and `/var/tmp/ExecCountsSweep-ca/` — **`/tmp` was 100 % full on this host** (`df -h /tmp` → `128G 128G 22M 100%`), so
the counters were run with `TMPDIR=/var/tmp/ExecCountsSweep-ca` (see F15). Nothing was installed; pacman was not run.
Nothing in the fleet repo, the lane tree (except this report), `.ufo/state`, `MANIFEST.json`, `LOG.md`,
`SCORECARD.md`, `SKILL.md`, `corpus/**`, `reports/**` or shokuknow was written.

---

## 1. The two legs the round actually promises

```
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-74: PASS legs=13/13                      exit=0

$ TMPDIR=/var/tmp/ExecCountsSweep-ca python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6a… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-CA-74: PASS legs=11/11                     exit=0
```

`reports/round-74/telemetry/measures-c.txt` and `measures-ca.txt` restate exactly these two lines at exactly these two
revisions. **Both survive.**

`ACCEPT-CA-74: PASS` is conditional on the temp root being normalizable — see F15 (with `TMPDIR` under `/home`, the same
command prints `ACCEPT-CA-74: FAIL legs=10/11`, RECEIPTS red; the normalization regex is
`/(?:var/)?tmp/[^\s:,"']+` at `reports/round-74/accept-ca.py:183`).

## 2. Counts table

`match` = ✔ when the stated number re-derives with its own command at the stated revision; ✘ when it does not;
`base`/`lands` mark the revision; `—` = no command is stated for the number (CORPUS rule: a count carries its command).

### 2.1 `corpus/lessons/round-74.md`

| # | location | stated | command run | observed | match |
|---|---|---|---|---|---|
| 1 | :4 | 804 registry rows at base | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` @base | 804 | ✔ base |
| 2 | :4 | 0 `*worldbuilding-setting*` files | `find corpus/knowledge -iname '*worldbuilding-setting*' \| wc -l` @base | 0 | ✔ base |
| 3 | :4 | 247 knowledge files | `find corpus/knowledge -type f -name '*.md' \| wc -l` @base | 247 | ✔ base |
| 4 | :5 | 0 registry hits litmemo/tuduku/chinawriter | `grep -cE 'litmemo\|tuduku\|chinawriter' corpus/SOURCES.md` @base | 0 | ✔ base |
| 5 | :5 | four rows S881–S884; 808 rows at lands | same registry regex @lands | 808; added exactly S881..S884 | ✔ lands |
| 6 | :7 | 13 ledger pairs (1 REPAIR, 12 ANNOTATE) | counter output `pairs=13`, `green=['LC-09']`, `annotate-pairs=12` | 13 / 1 / 12 | ✔ lands |
| 7 | :8 | 6 must_track pins | `len(ledger.must_track)` (frozen) | 6 | ✔ |
| 8 | :8 | legs=13/13 and legs=11/11 | both counters at their lands (§1) | 13/13, 11/11 | ✔ |
| 9 | :18-22 | evidence bytes/sha256/window for S877,S881,S882,S883,S884 | re-fetched all five URLs with the recorded browser UA, `sha256sum`, `wc -c`; window recomputed | 1055723 B `e512a20d…`; 101615 B `441fc921…`; 17068 B `754f504c…`; 48536 B `a3b6640c…`; 62604 B `344de345…` — all exact | ✔ |
| 10 | :18-22 | windows 4098 / 4098 / 2953 / 4104 / 4103 chars | recompute over each stored window line + `window-sha256` | 4098 / 4098 / 2953 / 4104 / 4103; all window-sha256 match | ✔ |
| 11 | :26 | sentence 108 chars / 15 tokens; cell 54 chars / 7 tokens | `len()`, `split()` on the located Russian sentence and the cell clause | 108 / 15; 54 / 7 | ✔ (but see F7 for **where** the sentence lives) |
| 12 | :27 | 2953 = 631 + 33 + 2289; `window: chars=2953 min=4096` | arithmetic + header | 2953; header exact | ✔ |
| 13 | :28 | round-73 evidence "one collapsed paragraph, 1564 B" | `git cat-file -s <base>:reports/round-73/evidence/S877.txt`; `sed -n 14p \| wc -c` | file 2417 B; window paragraph 1615 B (1614 + newline), 894 chars | ✘ **F9** |
| 14 | :40 | 2 adopted / 4 path-present / 34 refused of 40 | `find …/merge/kotodama/knowledge -type f \| wc -l`; staging compare | 40 files: 2 adopted, 4 path-present (sha differs in all four), 34 refused | ✔ |
| 15 | :47-52 | family counts 5 / 11 / 3 / 2 / 9 / 3+1 (=34) | per-family `ls`/`find` of the staged package | 5 / 11 / 3 / 2 / 9 / 3+1 = 34 | ✔ (`naming-systems` composition text ✘ **F10**) |
| 16 | :61-63 | reg-ids 804, staged-ids 132, collisions 22 (+ three sha256) | `wc -l`, `sha256sum` | 804 `94a495c7…`; 132 `bab11d7d…`; 22 `130ec2d1…` | ✔ |
| 17 | :61-63 | id ranges S001…S880 / S859…S990 / S859…S880 | `head -1`/`tail -1` | exact | ✔ |
| 18 | :65-66 | 0/22 collision pairs name the same document (URL join) | URL join lane vs staged for the 22 ids | 0 same; 2 pairs have no URL on the lane side (S859/S860 are own-work rows) | ✔ (caveat in §6) |
| 19 | :69 | `grep -c` over reg-ids for S883/S884/S899/S900 = 0 | `grep -cE 'S883\|S884\|S899\|S900' reg-ids` | 0 | ✔ |
| 20 | :73 | map sha256 `d3573f7d…` | `sha256sum id-renumber-map.json` | `d3573f7d3cf2…aeb24afa` | ✔ |
| 21 | :85-86 | single pass yields S877×4, S881×4/S882×4, S883×3/S884×3 | `grep -oE '\bS\d{3}\b'` on the **staged** entries | staged base: S882×4, S883×4, S884×4; staged amend: S899×3, S900×3 | ✔ |
| 22 | :88 | S729/S730/S742/S743/S754/S895 in neither entry | `grep -c` both entries | 0 every id | ✔ |
| 23 | :96 | `corpus/SOURCES.md:832` = S877 at base | `grep -n '^\| S877 '` | 832 | ✔ |
| 24 | :99-101 | theme rows "split … into 12 cells instead of 11"; one escaped pipe each | `awk -F'\|'` per row; `grep -o '\\\|'` | NF 14 (12 cells naive), 1 escaped pipe each | ✔ |
| 25 | :105-108 | recheck `grep -c` 4 / 1 / 1 / 1 (ran 2026-10-23) | `grep -c` of each term on today's bodies | 4 / 1 / 1 / 1 | ✔ |
| 26 | :116 | mirror 804 → 808 rows; diff exactly `801c801`, `804a805,808` | row-extracted diff base vs mirror | 801c801 / 804a805,808; 808 rows | ✔ (row granularity; a file-line diff gives 832c832/835a836,839 and is **not** the stated instrument) |
| 27 | :115-116 | mirror draft entries `658a8fa4…9986b00b` / `bb5504e2…d80d8673e` | `sha256sum` mirror entries and `drafts/` | `465051db…e65fc` / `0b2e06dc…b2790d31` | ✘ **F5** |
| 28 | :116 | mirror registry `sha256 81fcebe1…f2f326` | `sha256sum .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md` | `c8da0a5a765d…f83c5614` | ✘ **F5** |
| 29 | :117 | `validate --file` exit 0, zero E-codes | both mirror receipts | exit=0; E-codes NONE; W01×3, W04×28 | ✔ |
| 30 | :122-125 | guard: 804→805 ids, collisions 23, new id S883 (2sp, 3sp, 4sp) | `guard-proof/out/*.summary.txt` | 2sp/3sp: rows 805, collisions 23, sees S883; 4sp: 804/22/0 | ✔ (m4 column-zero and m5 tab have **no committed output** — §6) |
| 31 | :129 | "8 of 132 staged rows have 11 cells" | `awk -F'\|' 'NF==13'` over the 132 staged rows | 7 (S928, S945, S946, S955, S956, S961, S962) | ✘ **F6** |
| 32 | :135-136 | `s816.html` 48536 B `a3b6640c…`; `s817.html` 62604 B `344de345…` | `wc -c`, `sha256sum` of the round-71 captures | exact; and byte-identical to the S883/S884 evidence bodies | ✔ |
| 33 | :153-156 | 21 rows = 18 payload-absent + 3 unreachable; PRESENT 10, REFUSED 7, UNVERIFIABLE 4 | count the verdict table | 21; 10/7/4; id lists identical | ✔ |
| 34 | :169 | R74-M2 greps return 0 lines | `git grep -c 'ACCEPT-C-73: PASS' <base> -- reports/round-73/telemetry` (and CA) | 0 / 0 | ✔ |
| 35 | :170 | R74-M3 "junk landings pass 8 of 12 probes" | count `MutPredicateC.md` P0a..P7b rows and `PASS 11/11` | 12 probes, 8 survivors | ✔ |
| 36 | :171 | R74-M4 `grep -c scenarios SCORECARD.md` = 0 | same @base | 0 (empty, rc=1) | ✔ base (2 at main — F14) |
| 37 | :175 | R74-M8 `SELFTEST: 69/69` and `179 checks across 41 scenarios` | both `--selftest` at the landed counters | `SELFTEST: 69/69`; `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0` | ✔ |
| 38 | :182 | census before 804 / after 808 rows; W01×3; W04×28 | `grep -c` on the receipts + registry regex | W01 3, W04 28, E-codes 0; row counts **not in the receipts** | numbers ✔, citation ✘ **F11** |
| 39 | :197 | README 245 index rows vs 247 files | `grep -cE '^- `[^`]+\.md` — '` @base vs `find` | 245 / 247 | ✔ base |
| 40 | :197-198 | linguistics heading 30 vs 32 files | heading literal vs `git diff --shortstat <empty> <base> -- 'corpus/knowledge/linguistics/*.md'` | 30 / 32 | ✔ base |
| 41 | :199 | SHONEN.md:6 "412 rows" vs 804 | `sed -n 6p SHONEN.md` @base | 412; registry 804 | ✔ base |
| 42 | :200 | SKILL.md:594 civilizations "94" vs 95 files | `sed -n 594p SKILL.md` @base; per-dir count | 94; 95 files | ✔ base (lands: 95/95) |
| 43 | :201 | `selftest-r3.txt:6` truncated mid-word | `sed -n 6p … \| tail -c 80` | ends `min-pairs gate FAI` | ✔ |
| 44 | :201 | `SKILL.md:703` "measured 10/11" has no committed receipt | `sed -n 703p` @base; `grep -rn 10/11 reports/round-72/telemetry` | 10/11 present; 0 receipts | ✔ |
| 45 | :204 | round-72 GROUND receipt "797/ihchina 0/bunka 0" | `reports/round-72/telemetry/baseline.txt:3`, `gap-sweep.txt:3-4` | 797; 0; 0 | ✔ |
| 46 | :204-206 | commit `5897ddf` re-pointed `leg_ground` | `git show 5897ddf --stat` | commit exists, touches `reports/round-72/accept-c.py` | ✔ |
| 47 | :172 (R74-M5) | S758/S759 url↔quote mispairing, `binding: id` | `census-adjudication.json` records | S758 url=2025 quote=这个我肯定考虑过…; S759 url=2022 quote=Sowers-Wills; both `binding: id` | ✔ |
| 47a | :137-139 | S816's span 0 hits on the 2025 page, 1 on the 2022 page; S817's Sowers-Wills span absent from both chinawriter pages, present in the S880 document | `grep -c` on today's re-fetched bodies; `reports/round-73/evidence/S880.txt:14` | 0 / 1; 0 / 0; S880 window carries `Sowers-Wills's "Phonology from the inside out…"` | ✔ |
| 47b | :146 | "The four clearing conditions" | numbered list | 4 | ✔ |
| 47c | :176-177 (R74-M10) | two appended round-73 reports; two `*.postwave.md` copies; originals restored | `grep -c 'Post-wave update'` on the four paths | postwave copies 1 each; round-73 `w1` originals 0 each | ✔ |

### 2.2 `SCORECARD.md` `## Corrections — round 74`

| # | stated | command | observed | match |
|---|---|---|---|---|
| 48 | 12 rows ("12 annotated pairs") | count table rows 1442-1453 | 12 (`LC-01,02,03,06,07,08,11,12,15,16,17,18`) | ✔ |
| 49 | LC-01 412 → 804 | `git grep -c -E '^. S[0-9]{3}' f7104cb… -- corpus/SOURCES.md` | `f7104cb:corpus/SOURCES.md:804` | ✔ |
| 50 | LC-02/LC-03 9 → 10 | `git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' … selftest-r3.txt` | `SELFTEST OK: 10 scenarios` | ✔ |
| 51 | LC-06/LC-07 243 → 247 | `git diff --shortstat 4b825dc… f7104cb… -- 'corpus/knowledge/*/*.md'` | `247 files changed` | ✔ |
| 52 | LC-08 30 → 32 | same, `linguistics/*.md` | `32 files changed` | ✔ |
| 53 | LC-11 23443 → 97656 | `git grep … 'decompress.*23443.*[0-9]+ bytes' … ScoutReopenS879.md` | `decompress -> 23443 -> 97656 bytes` | ✔ |
| 54 | LC-12 no → two | `git grep … 'HAS two status-200 Wayback captures' …` | 1 line | ✔ |
| 55 | LC-15 776 → 724 | `git grep -c … 65fe857 f7104cb -- corpus/SOURCES.md` | `65fe857…:724`, `f7104cb…:804` | ✔ (token = the pinned-rev line) |
| 56 | LC-16 reachable → present | `git grep -h -o -E 'wall (present) \("Client Challenge"\)' …` | `wall present ("Client Challenge")` | ✔ |
| 57 | LC-17 752 → 728 | same shape, `c5f0992…` | `c5f0992…:728` | ✔ |
| 58 | LC-18 753 → 701 | same shape, `94209e8…` | `94209e8…:701` | ✔ |

### 2.3 `SKILL.md` rows

| # | location | stated | command | observed | match |
|---|---|---|---|---|---|
| 59 | :705 accept-c-74 | PASS legs=13/13; "thirteen implemented legs"; LEGCOUNT refusal at twelve legs | C counter + `# frozen legs: 13 (…)` | 13/13; 13 names | ✔ |
| 60 | :705 accept-c-74 | selftest receipt `selftest-c.txt` | `--selftest` | `SELFTEST: 69/69 scenarios`, exit 0 | ✔ |
| 61 | :706 accept-ca-74 | PASS legs=11/11; "eleven implemented legs" | Ca counter + frozen leg list | 11/11; 11 names | ✔ |
| 62 | :706 accept-ca-74 | "measured at counter sha256 `76d00b88325f…`: exit 0, `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`" | `sha256sum reports/round-74/accept-ca.py` (and at freeze/lands/main); `--selftest` | counter `8052f1e2…` at all four revisions; selftest `179 checks across 41 scenarios`; `selftest-ca.txt` tail identical | ✘ **F4** |
| 63 | :707 correction | r3 selftest `10 scenarios`, sha `222d4dd6…`; freeze bytes sha `f8ebb5d8…` print 9 | `sha256sum` at `2d1cd914`/`af65165`; `selftest.txt` vs `selftest-r3.txt` | 222d4dd6… / f8ebb5d8…; `9 scenarios` vs `10 scenarios` | ✔ |
| 64 | :707 correction | accept-c-73 "prints `SELFTEST: 29/29`" | `reports/round-73/telemetry/selftest*.txt:3` | `SELFTEST: 29/29` ×3 | ✔ |

### 2.4 `corpus/README.md` appended block (round-74)

| # | stated | command | observed | match |
|---|---|---|---|---|
| 65 | Registry 804 → 808 rows; four new rows | registry regex @base/@lands; `git diff --numstat` | 804 / 808; +5/−1 (four rows + S877) | ✔ |
| 66 | Total knowledge entries: 249 | `find corpus/knowledge -type f -name '*.md' \| wc -l` @lands | 249 | ✔ |
| 67 | directory totals 32/29/40/29/24/95 | per-directory `find` counts | 32/29/40/29/24/95 (sum 249) | ✔ |
| 68 | live directory 40 files; section 38 rows | `find culture-material`; count `` - `x.md` — `` rows in the section | 40; 38 | ✔ |
| 69 | two culture-material files remain unindexed | file count − row count | heritage-taxonomy-models (2 files) unindexed | ✔ |

### 2.5 `corpus/QUALITY.md` criterion 25

| # | stated | command | observed | match |
|---|---|---|---|---|
| 70 | "adds to criteria 9, 11, 17, 19 and 23" | `grep -cE '^[0-9]+\. '` / numbering in QUALITY.md | those five criteria exist | ✔ |
| 71 | "The freeze commit carries … four receipts: junk-c.txt (J1–J3), junk-ca.txt (J4, J4b, J5–J7), controls-c.txt, controls-ca.txt" | `git ls-tree -r 00c408a reports/round-74/telemetry/` | **2** of the four: `controls-c.txt`, `controls-ca.txt`; no `junk-*` at the freeze (added in `1d7add3`); at main the roster is junk-c = J1,J2,J3,**J9**; junk-ca = J4,J4b,J5,J6,J7,**J8**,**J9** | ✘ **F1** |
| 72 | J-table "must FAIL" legs (8 rows) | per-fixture `LEG FAIL` lines in the receipts | J1 ENTRIES ✔, J2 EVIDENCE ✔, J3 FROZENCFG ✔, **J4/J4b not LEDGER (FROZENCFG)**, J5 ANNOTATE ✔, J6 APPENDONLY ✔, J7 SEPARABLE ✔ | ✘ **F2** |
| 73 | one-liner exits: C/CA `0`; r73 C/CA `1` | ran the published `sh -c` one-liner on each source | 0, 0, 1, 1 | ✔ |
| 74 | "round 73's counter declared LEGS (8, fixed at freeze)" while the driver requires 9 | `grep -n LEGS reports/round-73/accept-ca.py`; `MutLandedCa.md:115` | `45:LEGS (8, fixed at freeze)`; line 115 says the same | ✔ |

### 2.6 The two entries' headers (and header-adjacent counts)

| # | location | stated | command / source | observed | match |
|---|---|---|---|---|---|
| 75 | base `- source: S877` | 1,055,723 bytes, sha256 `e512a20d…` | re-fetch (browser UA) + `sha256sum` + `wc -c` | exact | ✔ |
| 76 | base `- source: S877` | "the whole 184-page monograph" | `pdfinfo S877.body \| grep Pages` | `Pages: 185` (imprint: 184 с.) | ✘/obs **F13** |
| 77 | base `- source: S877` | "cited here at printed pages 7, 35, 36, 139 and 140" | `pdftotext -enc UTF-8` per page + locate each quoted span | quotes locate on 7, 35, 36, 139 only; nothing cites p.140 | ✘ **F8** |
| 78 | base `- source: S881` | 101,615 bytes, sha256 `441fc921…`; "CDX holds no capture of this slug" | re-fetch; CDX API with browser UA | exact; CDX `[]` for the slug (host `litmemo.com` has 3 captures → control) | ✔ |
| 79 | base `- source: S882` | 17,068 bytes, sha256 `754f504c…`; "no capture of this slug or host in CDX" | re-fetch; CDX slug and host | exact; slug `[]`, host `[]` | ✔ |
| 80 | amend `- source: S883` | 48,536 B, sha256 `a3b6640c…` | re-fetch + `sha256sum` | exact; byte-identical to round-71 `s816.html` | ✔ |
| 81 | amend `- source: S884` | 62,604 B, sha256 `344de345…` | re-fetch + `sha256sum` | exact; byte-identical to round-71 `s817.html` | ✔ |
| 82 | base `- ground:` | 804 rows; `grep -ciE 'worldbuilding\|setting-practice'` = 0; CJK = 0; three hosts = 0 | the three commands @base | 0 / 0 / 0 | ✔ |
| 83 | amend `- ground:` | same classes, `grep -ciE 'worldbuilding\|setting'` = 0 | @base | 0 | ✔ |
| 84 | base `- topic:` | five-step, four-layer, five elements, five sections + four fields, two sub-sheets | S881/S882 page structure (headings/list boxes/templates) | h3 1–5; 第1–4層; 5要素; 5 note sections; 種類・説明・ルール・関連; 2 sub-sheets | ✔ |
| 85 | base §7 | "eight-field country sheet"; "seven questions" | S881 text: 「次の8項目」; 源…権力との関係 | 8; 7 | ✔ |
| 86 | base §8 | "three depths" | S881 核/背景/彩り | 3 | ✔ |
| 87 | base §1 | tuduku "about 1,100 characters by its own count" | `grep -o '1,100文字'` on S882 | present | ✔ |
| 88 | amend recheck | "94 such elements" in `div.end_article`; commented 责编 last | textual `<p` inside the div span | 94 (93 elements + 1 in the comment) | ✔ |
| 89 | amend recheck | "92 p elements carrying a text-indent 2em"; anchors 67th/68th | paragraph scan | 92; P68 = 67th, P69 = 68th | ✔ |
| 90 | amend recheck | "the 34th of the 2022 page's 69" | paragraph scan of S884 | 69 text-indent p; quote = 34th | ✔ |
| 91 | Gate S883 | P68 | `p` ordinal in `div.end_article` | 68 | ✔ |
| 92 | Gate S884 / body | "para 35 (the 14th 乌贼 answer)" | textual `<p>` order (browser-upgrade notice = 1) | 35th; 14th answer | ✔ |
| 93 | amend §1 | "twelve writers"; "three named interviewers" | S883 text (十二位作家); credit lines P3–P6 | 12; 3 | ✔ |

## 3. Findings

Each names what it attacks; commands and raw output are the evidence; severities are mine.

### F1 — HIGH — `QUALITY 25(b)` says the **freeze commit** carries four control receipts; it carries two, and the fixture roster is wrong

Attack: the landed QUALITY 25 clause states the freeze ships the junk landings it must reject.

```
$ git ls-tree -l 00c408a0af2fa5ddf65af2224152ce258b26d896 reports/round-74/telemetry/
1298 …/accept-c-73-at-lands.txt     2895 …/accept-ca-73-at-lands.txt
3340 …/census-start.txt             5248 …/controls-c.txt
8401 …/controls-ca.txt              6018 …/gap-sweep.txt
  33 …/selftest-c.txt               7736 …/selftest-ca.txt
$ git cat-file -s 00c408a0af2f:reports/round-74/telemetry/junk-c.txt
fatal: path 'reports/round-74/telemetry/junk-c.txt' exists on disk, but not in '00c408a0af2f…'
$ git log --oneline -- reports/round-74/telemetry/junk-c.txt
1d7add3 round-74: junk-landing receipts, …
```

So the two receipts the criterion rests on were committed **after both lands** (`5e4796c`, `c4bf61a`), and their fixture
roster at main is not the criterion's:

```
junk-c.txt  fixtures: J1 J2 J3 J9
junk-ca.txt fixtures: J4 J4b J5 J6 J7 J8 J9
```

The criterion says `junk-c.txt (J1–J3)` and `junk-ca.txt (J4, J4b, J5–J7)`; J8 and J9 exist and are unlisted.

Proposed fix: state the receipts at the **landing**, not the freeze, or move them into the freeze commit; add the J8
(typed receipt → RECEIPTS) and J9 (leg deleted from frozen claims.json → FROZENCFG) rows and correct the two roster
sentences. The same two receipts are what claim C's and claim Ca's `do_nothing_control` fields point at, so the claim
fields inherit the same late-landing problem.

### F2 — HIGH — `QUALITY 25`'s own rule condemns its own J4/J4b receipts: the named leg `LEDGER` never fails

Attack: the criterion says "A fixture the round-74 counter does not fail on its named leg fails this criterion", and its
table names `LEDGER` for J4/J4b.

```
fixture: J4
exit: 1
LEG FAIL APPENDONLY
LEG FAIL SEPARABLE
LEG FAIL FROZENCFG
verdict: ACCEPT-CA-74: FAIL legs=8/11
expected: FAIL: graded-tree ledger observe_cmds constant-print expected_after (FROZENCFG; LEDGER if read from the tree)
```

`LEDGER` is absent from both J4 and J4b; the receipt itself relabels the expected leg as `FROZENCFG`. Since the ledger
is read from the frozen commit (by design, and by the LEDGER leg's own pass), a graded-tree constant-printer cannot make
`LEDGER` red — the fixture shape cannot reach its named leg.

Proposed fix: make the QUALITY 25 table's must-fail column read `FROZENCFG` for J4/J4b (and say why: the graded-tree
ledger is caught by the freeze-pin, not by the allowlist), or build a fixture that constant-prints inside the **frozen**
ledger (which would then genuinely fail LEDGER and also LEGCOUNT/LEDGER). As landed, 2 of the 8 tabled fixtures fail
their named leg. Scope note: this is a leg-name/leg-count claim, not one of the two counters' legs (both counters pass).

### F3 — HIGH — the frozen claim's control statement for Ca (`REPAIR, ANNOTATE, RECEIPTS red`) is contradicted by its own receipt and by a re-run: `RECEIPTS` is green at `lands == freeze`

Attack: `reports/round-74/claims.json` (freeze) claim Ca `do_nothing_control`: "lands == <freeze> FAILS with REPAIR,
ANNOTATE, RECEIPTS red and FROZENCFG/LEDGER green".

```
$ TMPDIR=/var/tmp/ExecCountsSweep-ca python3 -B reports/round-74/accept-ca.py --root . \
    --lands 00c408a0af2f… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS LEDGER
LEG PASS BASEMISMATCH
LEG FAIL REPAIR
LEG FAIL ANNOTATE
LEG FAIL NOSTUB
LEG PASS APPENDONLY
LEG FAIL SEPARABLE
LEG PASS TRACKED
LEG PASS RECEIPTS
     NOTE lands == freeze: do-nothing control shape; …
LEG PASS FROZENCFG
LEG FAIL STAMP
ACCEPT-CA-74: FAIL legs=6/11
```

The committed `controls-ca.txt` agrees (`LEG PASS RECEIPTS`, verdict `FAIL legs=7/11`). `RECEIPTS` is green because
the round-73 re-execution does not depend on the graded round-74 tree at all; only `REPAIR`, `ANNOTATE`, `NOSTUB`,
`SEPARABLE` (and `STAMP` when `main ≠ freeze`) are data-dependent. `LEDGER`/`FROZENCFG` green does hold.
(`STAMP`'s extra red in my run is `--main` defaulting to my clone's `main`, which I had pinned elsewhere; the committed
receipt was taken with `main == freeze`.)

Proposed fix: correct the claim's control text at the next freeze (a SCORECARD correction row naming the frozen sentence
and the observed red set is the append-only way), or make the control materialize a clone **without** the round-73
receipts so `RECEIPTS` genuinely fails. The kill-rule does not cover this field, so the claim's `after` still stands —
but the control sentence as filed is false.

### F4 — MEDIUM — `SKILL.md` accept-ca-74 row carries a counter sha256 and selftest counts that no landed artifact has

Attack: a number with a command, in a SKILL gate row.

Stated: "measured at counter sha256 `76d00b88325f…`: exit 0, `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`".

```
$ for rev in 00c408a 5e4796c c4bf61a 1d7add3; do git show $rev:reports/round-74/accept-ca.py | sha256sum; done
8052f1e25c366a18…   (all four revisions identical)
$ python3 -B reports/round-74/accept-ca.py --selftest
SELFTEST OK: 179 checks across 41 scenarios reported-fail=0
$ tail -1 reports/round-74/telemetry/selftest-ca.txt
SELFTEST OK: 179 checks across 41 scenarios reported-fail=0: …
```

`76d00b88…`, `138`, `37` match no committed counter and no committed receipt. (The lesson's R74-M8 and the receipt both
say 179/41, which is what re-derives.)

Proposed fix: repoint the row to the landed counter sha `8052f1e2…` (full: `8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f`)
and 179/41.

### F5 — MEDIUM — the lesson's scratch-mirror paragraph publishes the **superseded** draft's hashes and citation

Attack: four numbers in `corpus/lessons/round-74.md:113-118`, each with a `sha256sum` available.

```
$ sha256sum .ufo/waves/round-74/assimilation/validate/corpus/knowledge/culture-material/worldbuilding-setting-practice*.md
0b2e06dc…b2790d31  …amend-2026-10-23.md
465051db…e65fc     …practice.md
$ sha256sum .ufo/waves/round-74/drafts/worldbuilding-setting-practice*.md        # same two values
$ sha256sum .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md
c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614
```

Stated in the lesson: entries `658a8fa4…9986b00b` / `bb5504e2…d80d8673e`; registry `81fcebe1…f2f326`. The lesson also
cites `assimilation/validate-receipt-draft.txt`, whose own header calls itself "DRAFT … superseded"; its successor
`validate-receipt.txt` carries `c8da0a5a…` and the two entry hashes above. (The hunk coordinates `801c801` /
`804a805,808` **are** correct — at row granularity; see the table.)

Proposed fix: replace both draft hashes, the registry hash, and the receipt citation with the current
`validate-receipt.txt` values; the claim C `SCRATCHMIRROR` leg already names `validate-receipt.txt`, so this aligns the
prose with the graded artifact.

### F6 — MEDIUM — "8 of 132 staged rows have 11 cells" re-derives as 7

Attack: a count with an implied command.

```
$ awk -F'|' '/^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ {if (NF==13) print $2}' SOURCES.append.md
 S928  S945  S946  S955  S956  S961  S962           # 7 rows, NF==13 → 11 cells
   distribution of naive NF: 13→7, 14→115, 15→9, 16→1   (7+115+9+1 = 132)
```

(`awk -F'|' 'NF==13' SOURCES.append.md | wc -l` = 9 only because the table header and separator lines also split to 11
cells; data rows = 7.) If pipes are unescaped first, **all** 132 rows carry 11 cells, so the "8" cannot be salvaged by
changing the parser either.

Proposed fix: "7 of 132" under the naive split used elsewhere in the same paragraph, or state the census's own split
rule and its count; the load-bearing point (E01 precedence swallows E03) is unaffected.

### F7 — MEDIUM — the "full sentence stays on the evidence file's `quote:` line" is false; it lives on the `locator:` line

Attack: the Gate note that justifies trimming the S877 cell.

```
$ grep -n 'дающий названия' reports/round-74/evidence/S877.txt
29:locator: p.7 (PDF page 7; sentence: "Язык – главный / инструмент … / природных и социальных реалий, ..." …)
$ sed -n '31p' reports/round-74/evidence/S877.txt
quote: Язык – главный инструмент построения вымышленных миров      # 54 chars, 7 tokens
$ python3 -c "…len(full),len(full.split())"
108 15
```

The 108-character sentence exists only inside the `locator:` line, split by PDF line-break slashes and truncated with
`, ...`; the `quote:` line is the 54-character clause. The two figures (108/15, 54/7) are correct; the location
sentence is not.

Proposed fix: say the sentence is quoted on the `locator:` line (PDF line breaks marked), or put it on a second
`quote-full:` line so a re-opener can find it where the lesson says.

### F8 — MEDIUM — the base entry claims five cited printed pages; only four carry a cited passage

Attack: a page count in the entry's header.

```
$ pdftotext -enc UTF-8 S877.body; locate each quoted span per page
[7]   Язык – главный инструмент построения вымышленных миров, …
[139] ВЯ в общем случае не служит средством коммуникации, …
[35]  связь между лингвоконструированием и моделированием миров неразрывна
[36]  некое научное или не совсем научное допущение
$ grep -c '(S877)' worldbuilding-setting-practice.md
4        # and all four quotes locate on 7/139/35/36; no body byte names p.140
```

The source line reads "cited here at printed pages 7, 35, 36, 139 and 140". Page 140's text (worlds are not static,
back-counted history) is not used by any sentence in the entry.

Proposed fix: drop 140, or cite a page-140 passage (the back-counted-history sentence is the natural candidate).

### F9 — LOW — the round-73 evidence file is not 1564 B by any measure taken

Attack: a byte count with a path.

```
$ git cat-file -s f7104cb:reports/round-73/evidence/S877.txt
2417
$ git show f7104cb:reports/round-73/evidence/S877.txt | sed -n '14p' | wc -c
1615        # the one collapsed window paragraph (1614 + newline; 894 characters)
$ for f in $(git ls-tree -r --name-only f7104cb -- reports/round-73/evidence); do git cat-file -s f7104cb:$f; done
1600 2417 1702 2731 1628      # no 1564 anywhere; git grep 1564 in reports/round-73 → no hit
```

Proposed fix: state 2417 B (file) or 1614 B (window). The substantive point — the round-73 file is a different grammar
with the p.10 quote — is true.

### F10 — LOW — `naming-systems (base plus 10 amendments) | 11` mis-composes its own 11

Attack: a family row's composition.

```
$ find …/merge/kotodama/knowledge/corpus/knowledge/linguistics -name 'naming-systems*.md'
naming-systems.amend-2026-10-23.md / -23b / -23c / -2026-10-24.md / -24-r10 … -24-r16   # 11 files, all *.amend-*
# the base sits in the separate amendments/ tree: amendments/corpus/knowledge/linguistics/naming-systems.md
```

The count (`11`) is right for the 40-file knowledge set; "base plus 10 amendments" is not (0 base + 11 amendments in
that set; base + 11 = 12 if the `amendments/` tree were counted).

Proposed fix: "(11 amendments)".

### F11 — LOW — the frontier line attributes the census row counts to receipts that do not state them

Attack: a number's cited source.

```
$ tail -2 reports/round-74/telemetry/census-start.txt
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
$ grep -c '804\|808' reports/round-74/telemetry/census-start.txt reports/round-74/telemetry/census-end.txt
0 / 0
```

804 and 808 are correct (registry regex, and 804 is also in `gap-sweep.txt:4`), but neither census receipt carries a
row count.

Proposed fix: cite `gap-sweep.txt` for 804 and add the count to the census invocation output (or name the registry
regex) for 808.

### F12 — LOW — R74-M9's "gap-sweep receipt named a 19-row registry first" is not re-derivable from the named revision

```
$ git show de93d91c:reports/round-74/telemetry/gap-sweep.txt | sed -n '27,30p'
== 4. registry size
804
$ git show de93d91c:reports/round-74/telemetry/controls-c.txt    # (empty: file absent at de93d91c)
```

The narrative describes an intermediate control state whose receipt is not in that commit. Not shown false, but
unverified; a reader cannot re-derive "19".

Proposed fix: point at the control receipt (or the seat report) that carries the 19-row draft, or drop the number.

### F13 — LOW — "184-page monograph" vs `pdfinfo` 185

```
$ pdfinfo S877.body | grep Pages
Pages:           185
$ pdftotext -enc UTF-8 S877.body | tr '\f' '\n' | …        # 185 page breaks (+ trailing)
```

The bibliographic record says 184 с. (printed pages), and the PDF carries a cover/verso, so "the whole 184-page
monograph" is defensible as a bibliographic statement; it is not the page count of the file. Recorded so no later round
"corrects" it in the wrong direction.

Proposed fix (optional): "the whole monograph (184 printed pages; the PDF is 185 pages)".

### F14 — INFO — `grep -c scenarios SCORECARD.md` is 0 at base (as stated) and 2 at main

```
$ git grep -c 'scenarios' f7104cb -- SCORECARD.md      # no output, rc=1 → 0
$ grep -c 'scenarios' SCORECARD.md                     # 2
1443:| LC-02 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' …
1444:| LC-03 | 9 | 10 | … same regex …
```

R74-M4's sentence is a base-time measurement and holds there; the round's own corrections add the word at main. No
fix needed if the entry is read as a base-state record; a reader re-running it at main will see 2.

### F15 — MEDIUM (operational risk, not a claim failure) — the Ca counter's receipt comparison is only reproducible when `TMPDIR` contains `/tmp/`; and `/tmp` is 100 % full on this host

Attack: the `after` sentence "prints ACCEPT-CA-74: PASS legs=11/11" is environment-shaped.

```
$ TMPDIR=/home/vgpnk/tmp/ExecCountsSweep/tmpdir python3 -B reports/round-74/accept-ca.py … --lands 5e4796c …
LEG FAIL RECEIPTS
     problems=['reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run (bda16ca6deec vs 8c16e2dc8b0c)', …
ACCEPT-CA-74: FAIL legs=10/11
$ df -h /tmp
/dev/nvme1n1p1  128G  128G  22M  100% /tmp
$ df -h /var/tmp
/dev/mapper/root  930G  349G  566G  39% /
$ TMPDIR=/var/tmp/ExecCountsSweep-ca  … same command
ACCEPT-CA-74: PASS legs=11/11
```

Cause: `normalize_receipt` substitutes only `/(?:var/)?tmp/[^\s:,"']+` (`accept-ca.py:183`); a `TMPDIR` under `/home`
leaves a `/home/vgpnk` prefix in front of `<TMP>` and the two receipts differ. The claim is **not** falsified (with a
normalizable temp root it reproduces PASS 11/11), but on this host the default `/tmp` is full, so the documented command
fails for disk reasons and the next TMPDIR a reader reaches for may produce a false red.

Proposed fix: normalize `mkdtemp` roots generically (replace the actual `tempfile.gettempdir()` prefix and the run's
`tempfile.mkdtemp` prefixes), not a hard-coded `/tmp`; and/or say in the SKILL row that `TMPDIR` must be on a
filesystem with space. Operational note for the round: `/tmp` being 100 % full is a host-wide condition that will
affect every seat that follows the "run the counter" instruction.

## 4. Numbers that carry **no** command (CORPUS rule)

| location | number | status |
|---|---|---|
| `corpus/lessons/round-74.md:113-118` | draft sha256 ×2, registry sha256 | F5 — no command, and stale |
| `corpus/lessons/round-74.md:129` | "8 of 132" | F6 — no command, and wrong |
| `corpus/lessons/round-74.md:28` | "1564 B" | F9 — no command, and wrong |
| `corpus/lessons/round-74.md:182` | "804 rows / 808 rows (census receipts)" | F11 — counts right, receipts silent |
| `corpus/lessons/round-74.md:176` | "19-row registry" | F12 — no artifact |
| `corpus/README.md` round-74 block | "Registry: 804 -> 808 rows" | no command in the block (census receipts cited, they carry no count); numbers verify |
| `SKILL.md:706` | `76d00b88…`, 138, 37 | F4 — a command is implied ("measured at"), the numbers are wrong |
| entry `- source: S877` | "184-page" | F13 — no command; `pdfinfo` says 185 |
| `QUALITY 25(b)` | "four receipts", rosters | F1 — no command, and wrong |

Everything else in the table above carries a command in the prose or in the receipt it cites.

## 5. Fetch hygiene (exact UA per fetch)

All fetches used the browser-shaped UA required by the round:

`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

| target | HTTP | bytes (decoded) | sha256 | UA |
|---|---|---|---|---|
| `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` (S877) | 200 | 1055723 | `e512a20d…` | browser-shaped (above) |
| `https://litmemo.com/ja/blog/novel-worldbuilding-guide` (S881) | 200 | 101615 | `441fc921…` | browser-shaped |
| `https://tuduku.space/column/novel-worldbuilding` (S882) | 200 | 17068 | `754f504c…` | browser-shaped |
| `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` (S883) | 200 | 48536 | `a3b6640c…` | browser-shaped |
| `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` (S884) | 200 | 62604 | `344de345…` | browser-shaped |

`curl` reported compressed `size_download` (31737 / 6260 / 16723 / 21341) while `wc -c` of the decoded body equals the
recorded `bytes:` — the evidence files' `bytes:` field is the decoded size, and it matches.

CDX probes (the two "no capture" rulings), canonical slug, with positive controls — all with the same browser UA via
the CDX API:

```
litmemo.com/ja/blog/novel-worldbuilding-guide   → []             (control litmemo.com → 3 captures)
tuduku.space/column/novel-worldbuilding         → []             (control tuduku.space → [])
tuduku.space                                    → []
www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html → 3 captures (20250610015519, 20250611013901, 20250813004013)
```

The positive control (chinawriter) proves the probe form returns captures when they exist; `litmemo.com`'s root captures
prove the host itself is archived while the slug is not.

No wall was bypassed; no automation was used to get past a challenge.

## 6. Where the attack **failed** (claim survived), and what could not be re-run

Survived with exact re-derivation (all rows marked ✔ above): both counters at their own lands; both selftests; every
SCORECARD correction token; all five fetch byte counts and sha256s; every evidence window and its `window-sha256`; the
804/808 registry, 247/249 file, per-directory and CJK ground counts; reg-ids/staged-ids/collisions counts, ranges,
sha256 and the 0/22 document join; the id-renumber map sha256; the staged substitution counts; the guard fixtures
2sp/3sp (805/23/S883) and 4sp (804/22); the 21-row quarantine table (10/7/4, ids identical); the README footer
(249, 32/29/40/29/24/95, 40 files, 38 rows, two unindexed); W01×3 and W04×28; the 478-word floor; the entries' content
counts (5/4/5/5+4/8/7/3/2, 1,100 chars, twelve writers, three interviewers); the locator counts (P68, 94 textual
`<p>`, 92 text-indent, 67th/68th, 34th of 69, para 35, 14th answer); the quarantine span hit counts (S816 0 on the 2025
page, 1 on the 2022 page; Sowers-Wills 0/0 on the chinawriter pages, present in the S880 window) and the R74-M10
postwave pair; the QUALITY 25 one-liner exits (0/0/1/1); the
round-73 LEGS-8/9 claim (R74-M3's 8-of-12) and the R74-M2 zero-receipt claim; the SKILL correction-row hashes and
9-vs-10 scenario reading; the C do-nothing control (re-run: `FAIL legs=4/13` with exactly ENTRIES, ROWS, GATE,
EVIDENCE, REJECTS, INDEX red and FROZENCFG green).

Not re-run, therefore not passed (recorded rather than scored):

- Guard mutations **m4 (column-zero)** and **m5 (tab)**: no fixture output exists under
  `.ufo/waves/round-74/assimilation/guard-proof/out/` (only 2sp, 3sp, 4sp, control, real); the seat report describes
  them but the tree cannot reproduce them.
- The "raw-pair variant … misses all three" comparison: no committed output.
- `QUALITY 25`'s last decoy rows ("counter reading the graded tree under a literal path, decoy `git show`" → exit 0):
  the two decoy files are not committed; only the four named sources were re-run.
- The Ca lands==base refusal was not re-run by me (only the lands==freeze control); the committed receipt shows
  `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: --lands equals the frozen base …)`, exit 2.

## 7. Hygiene / environment record

- Tools installed: **none**. `pacman` not run (host-wide pause). No network tool installed; `curl`, `pdfinfo`,
  `pdftotext`, `git`, `python3` were already present.
- Scratch: `/home/vgpnk/tmp/ExecCountsSweep/` (base/lands trees, clone, fetch bodies) and
  `/var/tmp/ExecCountsSweep-ca/` (counter temp roots). `/tmp` was left untouched after it filled.
- Read-only accesses: shokuknow (`merge/kotodama`, `.ufo/waves/corpus-expansion-1/census-adjudication.json`,
  absent-defect-register via the seat report) — no campaign tool was run there, no byte written.
- Writes: this report only.
- Disclosed defect worth the orchestrator's attention: `/tmp` is at 100 % (`128G 128G 22M 100%`) host-wide, which
  breaks the default `TMPDIR` for every counter run and was the reason the Ca counter first reported a false red.
