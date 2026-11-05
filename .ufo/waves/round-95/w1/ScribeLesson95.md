# ScribeLesson95 — round-95 lesson draft (calibration axis)

Seat: ScribeLesson95 (scribe, milestone `r95-v1`). Date: 2026-11-05.
Stage dir: `.ufo/waves/round-95/w1/stage/ScribeLesson95/`; scratch `/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/` (deleted before yield).
Main output: `stage/ScribeLesson95/round-95.md` — 22565 bytes, 82 lines, sha256 `b8a2493e85398174424b70b19f9dddf1aa0da1a62bcf9a56faf16e1003f21ef7` (also in `stage/ScribeLesson95/DONE`).

The L1 lands it as `corpus/lessons/round-95.md`. No lane production file was written by this seat.

## 1. Output file and section shape

`stage/ScribeLesson95/round-95.md`, sections in order (measured with `grep -n '^## '`):

| section | line | lines |
|---|---|---|
| `# kotodama round 95 — lesson` (H1 + preamble) | 1 | 6 |
| `## Gate` | 7 | 52 |
| `## Mistakes` | 60 | 13 |
| `## Routed to round 96` | 74 | 8 |

Header carries round 95 attempt 1, base `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`, freeze `d41eb594d27fa71869c0c28d9c2dc051fda40079`, claims O and C as frozen in `reports/round-95/claims.json` (not amended), the freshness pause with `.ufo/l0-questions.md` lines 47 and 303 and no L0 ANSWER, and the lowest-axis obligation neither met nor waived.

**Gate registry rows: 5** (S970–S974), measured with `grep -c '^| S97[0-4] |'` → 5. The claim requires at least three new rows from S970 up; five are drafted.

## 2. Every number in the draft, with its command and rc

All measurements below were run by this seat on 2026-11-05. Receipts are kept live in `stage/ScribeLesson95/receipts/`.

### Validity gates

- `python3 -B tools/check-gate-quotes.py .ufo/waves/round-95/w1/stage/ScribeLesson95/round-95.md` → `GATE_QUOTES: 0 findings`, **rc 0**. The checker finds 5 Gate rows and 5 quote runs of 14, 15, 8, 12 and 11 words (all ≤ 25); 0 html-entity, 0 doubled-locator, 0 truncated-grounds, 0 ellipsis-joined findings.
- QUALITY criterion 37 per-bullet sweep, `awk '/^## Gate/{g=1;next} /^## /{g=0} g' … | grep -E '^- ' | grep -vE '^- S[0-9]+ admit' | grep -viE 'reason|because|off-topic|…|population' | wc -l` → **0** (rc 0). Every rejected/unreachable bullet carries an explicit reason class.
- `python3 -B tools/check-cited-lines.py …/round-95.md` → `CITED-LINES: 6 finding(s) in 1 file(s)`, all `TABLE-ID` on the 5 registry-table rows plus the R95-M6 row. These are the registry rows the claim itself requires (one row per new S-row with an id column); no `MULTI-ID` finding remains after the two multi-id lines were reworded. The round-94 lesson carries 8 findings of the same shape, so this is the lesson-format norm, not a regression.
- `python3 -B receipts/final_check.py` → `gate lines: ['S970', 'S971', 'S972', 'S973', 'S974']`, `quote occurrences checked: 20 | failures: 0`, **rc 0**. Every quoted span on an id-bearing Gate line is an exact single occurrence (`count == 1`) in the committed capture named for that id, and no id-bearing line anywhere in the file carries a lowercase verdict token.

### End-to-end: the drafted lesson through the grader

`python3 -B receipts/check_lesson_end_to_end.py --work <fresh> --tool <grader>` builds a scratch mini-lane from ExecRegistry95's staged `SOURCES.append.md`, the ScribeEntry95 entry draft, the staged captures and **this lesson file**, then runs the grader in entry mode. Receipts `receipts/entry-mode-v5-run{1,2,3}.txt` and `receipts/entry-mode-v6.txt`.

- v5 base bytes (`7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`): three consecutive fresh runs, each **rc 0**, each `ENTRY-EVIDENCE: PASS legs=9/9` (legs ENTRY, SHAPE, TOPIC, NEWIDS, UNIQUENESS, BASEROWS, GATE, CAPTURE, APPENDONLY).
- v6 candidate (`f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec`): **rc 0**, `ENTRY-EVIDENCE: PASS legs=9/9`.

### Claim C projection (scratch mirror; the L1 owns the real landing)

- `python3 -B reports/round-95/predispatch.py --root <mirror> --work <scratch> --base-rev 19aa4dd… --base-registry <base SOURCES.md>` → rc 1 with `LEG C1 PASS bytes=50148 h2=12 table=11x5 phrases=6/6 topic-line=equal`, `LEG C2 PASS rows=898 highest=S974 new=5 qualifying=5`, `LEG C3 PASS added=6 removed=0`, `LEG C4 PASS census rc=0`, `LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=267 rows=267 findings=0`. The O legs fail in the mirror only because the drivers are not inside it (`tool missing`, `driver missing`) — expected.
- Base control re-measured: the same counter over a `git archive` of the base into scratch prints the frozen base receipt line for line (`PREDISPATCH-95: FAIL legs=4/10`), rc 1.

### Claim O measurements quoted in the draft

- `git show 19aa4dd…:tools/check-advance-evidence.py` → sha256 `7957945d…`; the round-94 `dispo-fallback` pattern string occurs **1×** in the v4 bytes (`e7fa8eaf…`) and **0×** in the v5 bytes — the pattern was written against v4 and is stale for v5 (R95-M1).
- Applying that same mutant to the v5 bytes still prints `SELFTEST PASS 126/126` at rc 0 — the >= 2-token heading rule is unpinned (R95-M2).
- `grep -in advance SKILL.md` → no output, rc 1; `tools/check-gate-registry.py --root . --json` lists `tools/check-advance-evidence.py` under `tools_without_rows` (26 tools without a row) while its own instrument set covers only `reports/round-*/accept-*.py`; the tool is named as the round instrument in `reports/round-90/claims.json` through `reports/round-94/claims.json` (R95-M3).

### Wave evidence re-read (not re-measured here, cited by path and number)

- `stage/ExecBattery95/red-before-v5.txt`: `BATTERY-SUMMARY survivors=7 unnamed=0 refused=7` on the v5 bytes, exactly the seven round-94 classes refused and the seven new ones surviving; `stage/ExecBattery95/reg-v5.txt` is 34 lines and byte-identical to `reports/round-94/controls/reg-v5.txt` (`diff` empty).
- `stage/ExecGraderV6/selftest.txt`: `SELFTEST PASS 134/134`; `stage/ExecGraderV6/battery.txt`: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=14`; `stage/ExecGraderV6/reg-diff.txt` empty.
- `stage/CriticO95/CriticO95.md`: v6 run `survivors=10 refused=6 unnamed=0 traceback=0` (9 fresh classes plus the ZWNJ1 control).
- `stage/CriticC95/critic.md`: 7 findings (3 medium, 4 low) on the entry and rows; the medium ones are F1 (two paragraphs restate the lullaby entry), F2 (S971 misattributed) and F3 (an unsourced cross-tradition claim). Those are entry findings, not lesson findings, and are not re-stated here.
- `stage/ScoutTopic95/rows.md`: 27 query operations, 265 records screened, 12 direct captures staged, 253 excluded at screening; the gap left open in the landed set is a non-European professional-mourner source.

## 3. Findings this seat added (the Mistakes section carries 7 rows)

R95-M1, R95-M2 and R95-M3 are the three mandated rows, each written with the class, evidence pointer, captured-by and fix the seat spec names, and each re-measured so it can fail.

Four further rows are wave-found, each with a measured pointer:

- **R95-M4 — coupling defect.** Four of the five new registry rows open their `teaches` cell with their own anchor quote verbatim, so the grader's GATE leg refuses the lesson's own gate line with `gate quote is the row teaching cell (self-quote)`. Measured: `LEG FAIL GATE` on four of five rows with both the v5 base bytes and the v6 candidate; `LEG PASS GATE` and `ENTRY-EVIDENCE: PASS legs=9/9` once the gate lines carry a second span from the same capture. The base registry shows no such collision (0 of its 5 anchor-quote rows), and the round-95 counter has no entry-mode leg, so nothing in the frozen measurement sees it.
- **R95-M5 — missing deliverable.** No round-95 seat staged `reports/round-95/evidence/manifest.json`, the per-row manifest the grader's CAPTURE leg reads; without it the grader refuses with `ADVANCE-EVIDENCE_ERROR: unreadable …/manifest.json` (rc 2, measured). Round 94 shipped the same file in its land commit.
- **R95-M6 — reason-not-recorded.** The scout staged twelve candidates and the registry seat landed five without recording a reason for the seven it dropped, one of them the only non-European professional-mourner source in the set.
- **R95-M7 — grader-input hazard in the lesson text.** A lesson line that names a registry id and also carries the word `located` in any case is refused outright by the grader's verdict-disguise channel (`VERDICT-LOWERCASE`), aborting the whole entry grade before any leg is scored. Measured on this seat's own first draft: the grader refused the draft at line 82, rc 2. The draft was reworded (ids and that word on separate lines); the row records the hazard for the next author.

## 4. Routed to round 96 (6 bullets in the draft)

CriticO95's nine surviving new classes (four splitlines-severing verdict channels — VT1/FF1/LS1/NEL1; two NFKC-unrejoinable token-breakers — NB1/ANSI1; CYR1 lookalike id letter; BR1/DASH1 heading-token anchors); the three open title-only exclusion re-decisions (Awetí 2015, Zulu Lexikos 2011, Turkish Signifiances 2020); the F1 non-numbered variant (measured refused on TOPIC by both the v5 base bytes and the v6 candidate in the numbered and the non-numbered form, so the tool closes it — what is still open is the battery predicate, whose 14-class manifest has no F1 entry); the R95-M4 teaches-cell coupling; the R95-M5 manifest and R95-M6 drop-reason gaps (both L1 landing decisions); and the unchanged freshness pause with the round-92 ideophones overlap question.

## 5. Not measured / not claimed

- I did not run the round-95 mutation battery or the v6 mutation score: `ExecMutants95/DONE` had not landed when this draft was written, so no mutation number is asserted here.
- The lands tree, the registry append, the README and the evidence manifest are the L1's; every claim C number above is a scratch-mirror projection measured by this seat, labelled as such.
- I did not verify the CriticC95 entry findings; they are entry findings outside this seat's scope.
- No claim is made about the round's freshness axis: the obligation is neither met nor waived.

## 6. Tooling

None installed, none upgraded, no pacman transaction, no sysctl or host change. The tooling record is: **none** — every command used was already present (`python3`, `git`, `awk`, `grep`, `sha256sum`, `pdftotext`).

## 7. Discipline

- Writes: `stage/ScribeLesson95/round-95.md`, `stage/ScribeLesson95/DONE`, `stage/ScribeLesson95/receipts/` (six files: the four scripts used, four entry-mode receipts and the final-check receipt), and this trailer. No lane production file was written; no sibling lane was touched; no fleet-root file was written; no `~/.local/bin` write.
- No git or jj mutation of any kind (read-only `git show` and `git archive` into scratch only); no `sudo`.
- Sources: this seat opened no URL. Every quote was re-verified against the scout's and registry seat's committed capture bytes in scratch; the search log and the capture hashes are the scout's and registry seat's, cited by path.
- Scratch `/fast/scratch/hyaku/kotodama-r95/ScribeLesson95/` deleted before yield.
