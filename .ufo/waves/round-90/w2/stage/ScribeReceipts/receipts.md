# Round 90 — measurement and sources receipts (ScribeReceipts)

Revisions: BASE `6b0b86e45ae902331aca75863db380f2991458c4`, LANDS `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761`, FREEZE `d0b6f2a7f9cc36272682749a9b047b739406f0c8`.
All counts read from committed bytes (`git show <rev>:<path>`, `git archive`). No production file was edited; no git write was run.
Reproduce the registry numbers with `receipts.sh` in this directory: `bash receipts.sh <lane-repo> <BASE> <LANDS> <scratch-dir>`.

## 1. Table

| measure | BASE 6b0b86e4 | LANDS 7f3a7aa6 | delta |
|---|---|---|---|
| registry rows (`corpus/SOURCES.md`, `^| S[0-9]`) | 865 | 873 | +8 |
| tier A | 511 | 517 | +6 |
| tier B | 329 | 330 | +1 |
| tier C | 25 | 26 | +1 |
| status mined | 762 | 769 | +7 |
| status queued | 58 | 58 | 0 |
| status rejected | 45 | 46 | +1 |
| pre-existing rows missing at lands | — | 0 of 865 | — |
| pre-existing rows with a changed cell | — | 0 of 865 | — |
| SOURCES.md diff base→lands | — | +8 / −0 lines, all in `## Registry` (lands lines 898–905) | — |
| knowledge files, total | 261 | 262 | +1 |
| knowledge `linguistics/` | 34 | 35 | +1 |
| knowledge `civilizations/` / `culture-material/` / `myth-symbol/` / `synthesis/` / `verification/` | 95 / 43 / 36 / 29 / 24 | 95 / 43 / 36 / 29 / 24 | 0 |
| knowledge filenames matching `prayer\|petition\|votive\|supplicat` | 0 | 1 | +1 |
| `census validate` rc (re-run on archived revision) | 0 | 0 | — |
| census warning lines (body) | 36 | 36 | identical |
| census warning lines naming S942–S949 | 0 | 0 | 0 |

New ids at lands: S942 S943 S944 S945 S946 S947 S948 S949.

Census mode cross-check (`sources-census.sh census`, same archives): BASE rows 865 / A 511 / B 329 / C 25 / mined 762 / queued 58 / rejected 45; LANDS rows 873 / A 517 / B 330 / C 26 / mined 769 / queued 58 / rejected 46. Both agree with the awk counts above.

## 2. Entry at LANDS

`corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`
- bytes 19930 (`git show 7f3a7aa6:… | wc -c`), lines 128, words 3134
- one H1 plus eight H2 sections (`grep -c '^## '` = 8)
- one table: 7 pipe lines = header, separator, five data rows; 4 columns on every line (`awk -F'|' '/^\|/{print NF-2}'` = 4 ×7)
- header keys present: `- topic:`, `- sources:`, `- verified-at:`, `- recheck:` (plus `- couples:`)
- sha256 `3215d153f43a19ea5dd2f361f338b0143cc895a27ac25187e301100652d28dca`
- cites S942–S948 (`grep -o 'S9[4-9][0-9]'`); each has registry status `mined`, `opened` 2026-11-04, `used-by` = this entry

## 3. Registry rows added at LANDS

| id | tier | status | opened | recheck | used-by |
|---|---|---|---|---|---|
| S942 | A | mined | 2026-11-04 | 90d | the entry |
| S943 | A | mined | 2026-11-04 | 90d | the entry |
| S944 | A | mined | 2026-11-04 | 90d | the entry |
| S945 | B | mined | 2026-11-04 | 180d | the entry |
| S946 | A | mined | 2026-11-04 | 90d | the entry |
| S947 | A | mined | 2026-11-04 | 90d | the entry |
| S948 | A | mined | 2026-11-04 | 90d | the entry |
| S949 | C | rejected | 2026-11-04 | 180d | `corpus/lessons/round-90.md` |

Captures `reports/round-90/evidence/S942.txt`–`S949.txt`: 8 of 8 sha256 values equal `manifest.json` (`sha256sum` of `git show` bytes).

## 4. Counter and grader at LANDS (read-only runs in scratch)

- `measure90.py` at LANDS is counter revision 6, sha256 `6e1ea6a5f96c6e92660e7a18c18b896d46dee3bf6368231e1a4a8fd7895406cd`. Freeze revision 1 is `4091cda9e0b5af399e99e85898f3040b9070d4225cf11584a601fe4c19caf0ce`. Revisions 2–6 are recorded in `reports/round-90/counter-revisions.md`, each marked "before any data".
- `claims.json` sha256 `9c161eeecae4d232490e1523eecbbe00769d871337ba10b5135879c3a312766f` at FREEZE and LANDS (unchanged).
- `tools/check-advance-evidence.py` at LANDS sha256 `121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed`, equal to the claims pin.
- `tools/check-corpus-index.py` unchanged between BASE and LANDS.
- Claim C at LANDS: `MEASURE90-C: PASS legs=4/4` (MATERIALIZE, ENTRY, INDEX, APPENDONLY), `CORPUS-INDEX: OK files=262 rows=262 findings=0`.
- Claim O at LANDS: `MEASURE90-O: PASS legs=6/6` (MATERIALIZE, TOOL, SELFTEST, REFUSALS, MUTATION, STUB); see section 6.

## 5. Commands

```
git --no-pager show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'
git --no-pager show <rev>:corpus/SOURCES.md | awk -F'|' '/^\| S[0-9]/{gsub(/^ +| +$/,"",$5); print $5}' | sort | uniq -c        # tier
git --no-pager show <rev>:corpus/SOURCES.md | awk -F'|' '/^\| S[0-9]/{gsub(/^ +| +$/,"",$9); print $9}' | sort | uniq -c        # status
git --no-pager diff --numstat 6b0b86e4 7f3a7aa6 -- corpus/SOURCES.md                                                          # 8 0
bash receipts.sh /home/vgpnk/Projects/shokunin/kotodama-shokunin 6b0b86e4… 7f3a7aa6… <scratch>                               # cell compare
git --no-pager ls-tree -r --name-only <rev> corpus/knowledge | awk -F/ '{print $3}' | sort | uniq -c
git --no-pager show <rev>:corpus/knowledge/linguistics/petitionary-and-votive-formulae.md | wc -c
python3 -B measure90.py --root <lane> --freeze d0b6f2a7… --lands 7f3a7aa6… --claim C --work <scratch>
bash scripts/sources-census.sh validate --root <fleet-shaped tree at rev> kotodama; echo rc=$?
```

The census script lives at the fleet root (`scripts/sources-census.sh`, reads `shokunin.conf`). Revisions were census-checked by copying that script and `shokunin.conf` into a fleet-shaped scratch tree beside `kotodama-shokunin/` materialized with `git archive <rev>`. Both trees print the same warnings as the fleet-root census-start.

## 6. Negative controls and counter verdicts

- Cell-compare negative control: flipping one status cell (S001 `mined`→`queued`) in a copy of the LANDS registry produces `neg changed rows: 1`.
- Claim O counter run at LANDS (`counter-O-lands.txt`, rc 0): `LEG PASS TOOL` sha256 `121888f0…`; `LEG PASS SELFTEST` `SELFTEST PASS 67/67`; `LEG PASS REFUSALS` `all ok` (13 cases); `LEG PASS MUTATION` `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern`; `LEG PASS STUB` recorded. Wall time 326 s.

## 7. Paste-ready: Before-to-after measurements

```
Measured from committed bytes at base 6b0b86e4 and lands 7f3a7aa6 (no working-tree reads).
- Registry, corpus/SOURCES.md `## Registry`: 865 -> 873 rows (+8, S942-S949; `grep -c '^| S[0-9]'`). Tier A 511 -> 517, B 329 -> 330, C 25 -> 26. Status mined 762 -> 769, queued 58 -> 58, rejected 45 -> 46 (awk over fields 5 and 9).
- Pre-existing rows: 865 of 865 present at lands; 0 cells changed (13-field cell comparison; a one-cell negative control is detected).
- SOURCES.md base->lands: 8 insertions, 0 deletions, all in `## Registry`; Paths, Search log and Leads byte-identical.
- Knowledge: total 261 -> 262 files; linguistics/ 34 -> 35; other partitions 95/43/36/29/24 unchanged. Filenames matching prayer|petition|votive|supplicat: 0 -> 1.
- New entry corpus/knowledge/linguistics/petitionary-and-votive-formulae.md at lands: 19,930 bytes, 128 lines, 3,134 words, one H1 and eight H2 sections, one 4-column table of five data rows, header keys topic/sources/verified-at/recheck present.
- Census, `scripts/sources-census.sh validate kotodama`: rc 0 at base and at lands; the same 36 warning lines at both; warnings naming S942-S949: 0 before, 0 after.
- Counter (freeze-pinned measure90.py revision 6, sha256 6e1ea6a5...): claim C at lands MEASURE90-C PASS legs 4/4; claim O at lands MEASURE90-O PASS legs 6/6 (rc 0 each).
```

## 8. Paste-ready: Sources and frontier

```
Sources. Seven sources opened live on 2026-11-04 and admitted to corpus/SOURCES.md: S942 WALS ch.72 (A), S943 WALS ch.73 (A), S944 WALS ch.71 (A), S945 SIL Glossary "Vocative case" (B), S946 IGI3 646 Attic dedication (A), S947 Blidstein, PLOS One votive epigraphy (A), S948 Galofaro & Kubas, OASIcs litany grammar (A). Each capture is in reports/round-90/evidence/ and its sha256 matches manifest.json (8 of 8 captures checked, S949 included). S949 (Wikipedia "Votive offering", tier C) is a retained rejection with its flip condition. The lesson's seed-rot section names three tier-C Wikipedia seeds; only S949 has a registry row, and the other two were not admitted and are not registered.
Frontier. Coverage axis: the new entry is the first dedicated knowledge file on petitionary and votive language; no knowledge filename carried prayer|petition|votive|supplicat at base. No lead on this topic was added to the Leads (unopened) section, which is unchanged. Freshness is paused (open L0 kotodama round-11 and round-89): no registry row was re-verified, re-dated or repaired, and no freshness move is claimed. Assimilation: none.
```

## 9. Discrepancies for L1 (not edited by this seat)

1. `corpus/lessons/round-90.md` "Registry changes" says "six `mined`" for S942–S948. The registry has seven `mined` rows (S942–S948, all `mined`). The lesson's "Admitted (seven rows, six A and one B)" is correct. Paste the registry figure (7), and ask the lesson author to fix the sentence.
2. `reports/round-90/census-end.txt` (committed at lands) has 36 lines and no `rc=` line; census-start has 39 lines including `rc=0`. The warning bodies are identical; the rc was recorded at re-run instead (see section 5).
3. `measure90.py` is described in claims.json as frozen, but the bytes at lands are revision 6 (five post-freeze revisions, all listed in counter-revisions.md). The fleet report should cite revision 6 and its sha256 alongside the freeze pin.
4. The lesson's seed-rot section says three tier-C Wikipedia seeds were not admitted; only one (S949) is in the registry.
