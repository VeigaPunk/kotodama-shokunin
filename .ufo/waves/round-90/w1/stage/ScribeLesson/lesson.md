# Round 90 — an advance-evidence grader and a petitionary/votive entry

author: kotodama lane (including its dispatched seats), 2026-11-04.
Claims: **O / operability** — capability acquisition: `tools/check-advance-evidence.py`,
a grader whose `--selftest` pins every sub-check and whose committed mutation pass
kills every mutant, refusing the round-89 survivor classes by name;
**C / coverage** — one dedicated entry
`corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` plus at least three
new mined A/B registry rows opened 2026-11-04, each with a lesson gate line, a
committed capture and a citation from the entry.
Base `6b0b86e45ae902331aca75863db380f2991458c4`; claims, counter, at-freeze controls,
the grader and its selftest/mutation receipts land in freeze
`d0b6f2a7f9cc36272682749a9b047b739406f0c8`.
Freshness is **not** claimed: L0 `kotodama | round-11` and the round-89 closure's
routed defect 1 keep freshness axis-move claims paused, so no old registry row is
re-verified, re-dated or repaired this round. Coverage is the lowest workable
non-retired axis, and claim C works it directly.

## Gate

<!-- PENDING: ScribeEntry packet (gates.md/rows.md) not present at write time; see notes.md -->

## Mistakes

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R90-M1 | receipt-integrity (attempt-1 leftovers, caught by the freeze) | The round-90 attempt-1 leftovers (untracked at round start) claimed a mutation score for tool sha256 `38f6ebaa…` while the bytes on disk were `cf6c2c05…`, and its selftest failed one case. The receipt's own `tool sha256` line is the criterion that should have caught it (QUALITY23/36). The freeze re-ran selftest and mutation on the final bytes and pinned the sha in `claims.json` O.tool_sha256: `reports/round-90/mutation-score.txt:2` reads `tool sha256 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed`, equal to `claims.json` O.tool_sha256 and to `sha256sum tools/check-advance-evidence.py` measured 2026-11-04 by ScribeLesson; line 3 reads `clean selftest green: rc=0 SELFTEST PASS 67/67`. The leftovers themselves are gone from disk: `grep -rl 38f6ebaa` under the fleet finds only the round-90 spec/dispatch prompt text, so this row rests on the freeze record and the pinned bytes, not on the deleted files. | L1 KotodamaR90a2 (freeze); sha re-measured by ScribeLesson | Fixed at the freeze: selftest and mutation re-run on the final bytes and the sha pinned in `claims.json`, so a stale score line cannot outlive the bytes it describes. |
| R90-M2 | selftest name/fixture mismatch (this round) | Attempt-1's selftest case named "quote is the source cell" actually built a quote equal to the row's teaches cell, so the case passed while the source-cell branch was unpinned — a real survivor, killed only after the mutant run. In the frozen grader the source-cell branch is pinned by a second case, `tools/check-advance-evidence.py:631` `chk('quote is from the source cell', …)` over the `titled` row (the title sits in the row's URL cell) and `lesson_title` (which quotes that title); the fixture at `:624` (`selfq`) quotes the teaches cell, so the name at `:624` still describes the source-cell branch while triggering the teaching-cell branch. Both branches are now covered: mutants `self-quote-check-off` and `source-quote-check-off` are each `KILLED … SELFTEST FAIL 66/67` (`reports/round-90/mutation-score.txt:5` and its neighbour). | L1 KotodamaR90a2 (freeze); ScribeLesson re-read the fixtures and the mutant rows | Criterion: a case name must name the condition its fixture triggers. The source-cell branch is pinned by its own case; the surviving looseness is the *name* at `:624`, which the freeze kept rather than renamed. |
| R90-M3 | vacuous leg (this round, caught by a non-author seat) | The frozen counter's C `ENTRY` leg could never PASS: `reports/round-90/measure90.py:210` (rev 5) built `dict(re.findall(r'^LEG (PASS\|FAIL) (\S+)'))`, whose keys are the verdicts `PASS`/`FAIL`, never leg names, so `missing` was always all six entry legs and a conforming landing still failed. ReviewerEntry-3 proved it with a fixture repo where the freeze-pinned grader alone printed `ENTRY-EVIDENCE: PASS legs=6/6` while the frozen counter printed `LEG FAIL ENTRY … observed=rc=0 missing=['ENTRY','SHAPE','TOPIC','NEWIDS','GATE','CAPTURE']`. Counter revision 6 (`6e1ea6a5…`, before any data) rebuilds `{name: verdict}` (now `measure90.py:210`) and records the defect. | ReviewerEntry-3 (non-author); L1 fixed it as counter revision 6 | Fixed before data with the revision recorded in `reports/round-90/counter-revisions.md` (rev 6, `ebd81b1b`); leg names, thresholds and constants unchanged. Limit: the author's own at-freeze control runs (O and C at base and at freeze) did not surface it, because the base control fails ENTRY for the honest reason (entry absent). |
| R90-M4 | frozen text vs recorded bytes (this round) | `claims.json` O.after_target says the stub control records "the stub failing SELFTEST and MUTATION"; the committed `reports/round-90/controls/stub-tool.txt` records the stub *passing* SELFTEST — `# rc=0 stdout='SELFTEST PASS 67/67'` — and failing `REFUSALS` (`# refusal cases printed ok by the stub: 0/13`) and `MUTATION` (`# rc=1 MUTATION-SCORE: 0/43 killed, 0 survived, 43 broken-pattern`). The genuine control value is stronger than the claim text: a fabricated `SELFTEST PASS 67/67` line is caught by the refusal cases, not by the tally. | ReviewerDiscipline (MINOR-2) | Retained limit: `claims.json` is frozen and no seat may amend it; the discrepancy is recorded here and in the reviewer report, and the receipt's own lines are quoted above. The STUB leg itself is substring-presence without a sha pin (same finding), so a lands revision that keeps those four substrings would still pass STUB. |
| R90-M5 | measurement (unbounded pattern) | An unbounded `petition` grep over `corpus/knowledge` at base matches **91** files, the word-bounded `\bpetition` **35**, and `competition` alone appears in **32** files (ScribeLesson, 2026-11-04: `git grep -lciE "petition"` / `git grep -lciE "\bpetition"` / `git grep -lciE "competition"` at `6b0b86e4`). A surface claim built on the unbounded pattern would have counted competition, repetition and petition owners as one class — the inflation the round-89 defect-5 rule forbids. | ScribeLesson, at L1's instruction to redo the base grep word-bounded | Fixed: `reports/round-90/base-surface.txt` quotes the word-bounded grep `\b(prayer|petition|votive|supplicat)` for headings and body, and notes that a filename match cannot carry a boundary inside a compound name (0 filename owners). Criterion: a base surface is quoted from a word-bounded command at the base commit (QUALITY36). |
| R90-M6 | evidence hygiene (this round) | The committed at-freeze control receipts echo scratch paths: `python3 -B tools/check-cited-records.py --root <lane>` prints `CITED-RECORDS: 0 empty / 12 scratch` (rc=1), 9 of them round-90 hits in `reports/round-90/controls/at-freeze-{C-base,C-freeze,O-base,O-freeze}.txt` (`--work /fast/scratch/…` echoes, MATERIALIZE `observed=` paths, one `FileNotFoundError` path). The same checker at base `6b0b86e4` prints `0 empty / 3 scratch` (the two inherited `/tmp` lesson lines), so the rc=1 pre-exists. | ReviewerDiscipline (MINOR-1) | Retained limit: the hits are command and observation echoes, not source citations, and no round-90 artifact cites `/tmp`, `/var/tmp` or `/fast/scratch` as evidence; the scratch dirs are deleted at wave close. The inherited 3 hits sit in freshness-paused lesson files and are not repaired. |

## Corrections

The round-89 non-author spot-check (`corpus/lessons/round-89-verifier-spotcheck.md`
§6) routed six defects to round 90. Dispositions:

| # | routed defect | disposition in round 90 |
|---|---|---|
| 1 | Freshness pause (governance): L0 `kotodama | round-11` ends "Freshness axis-move claims are paused until ruled"; no further freshness axis move until the operator rules L0 `kotodama | round-89`. | **Obeyed, not tested.** Freshness is not claimed this round; claim C works coverage, the lowest workable non-retired axis. No existing registry row is re-verified, re-dated or repaired, and the counter's `APPENDONLY` leg compares every cell of every base row so a repair kills C. |
| 2 | F predicate counts archive re-locates as advances (S142's only surface is a fixed 2025-03-31 memento). | **Answered in the grader's `ARCHIVE` leg.** A `web.archive.org` surface must carry a 14-digit timestamp whose year is the round's year and must embed one of the row's URLs exactly (`tools/check-advance-evidence.py:15-17`); the selftest pins `archive year predates round` (`:635`, `FAIL ARCHIVE`), `archive foreign host` (`:639`), `same-year archive accepted` (`:643`, rc0 `PASS legs=7/7`) and `archive stamp embeds a foreign url` (`:688`); mutants `archive-year-off` and `archive-embed-off` are each `KILLED … SELFTEST FAIL 66/67`. |
| 3 | Four stale findings carried, not repaired: S142 anchor "by" vs source "for"; S012/S021 arXiv versions; S104's children only in the page script; S157's biome list. | **Deferred, because freshness is paused.** Repairing any of them means re-opening, re-dating or rewriting an old row's cells, which the L0 pause forbids and which claim C's `APPENDONLY` leg kills. The findings stay where round 89 recorded them (`corpus/lessons/round-89.md`, its row-level caveats, and spot-check §6 item 3) and are not re-adjudicated here. |
| 4 | Counter strength: mutation 10/41 and five undeclared survivor classes (shadow duplicate rows, site-chrome/title quotes, capture = graded file, NOT-LOCATED spelling variants, copied-section filler). QUALITY36 binds round 90. | **Answered.** `tools/check-advance-evidence.py --selftest` exits 0 with `SELFTEST PASS 67/67`, one negative per sub-check; the 13 frozen refusal cases are each printed `ok` (shadow duplicate id/url, chrome quote, quote is the source cell, capture is a graded file, capture inside the dir but graded, NOT_LOCATED variant is a disposition, advanced while NOT-LOCATED, repetition filler entry, entry repeats a sentence three times, archive year predates round, archive foreign host, archive stamp embeds a foreign url); `reports/round-90/mutation-score.txt:1` reads `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern` (frozen floor 42) and the do-nothing stub control scores `0/43` with `43 broken-pattern` plus `0/13` refusal cases (`controls/stub-tool.txt`). |
| 5 | Frozen surface statements must be base-measured: C's round-89 `surface` text was false at its freeze. | **Answered.** `reports/round-90/base-surface.txt` quotes the base commit's word-bounded grep: 0 filename owners for `(prayer|petition|votive|supplicat)`; five heading hits (`tibet.md:92`, `direction-symbolism.md:129`, `sacred-topography-pilgrimage.md:1` and `:74`, `religion-language-co-evolution.md:1`); 88 body files; 261 knowledge files, linguistics 34; registry 865 rows, last id S941. R90-M5 records the unbounded-pattern failure that made the word-bounded redo necessary. |
| 6 | Minor precision: the new recheck cell `2027-02-03` is as_of + 91 days while the lesson prose says it "keeps the rows' 90-day cadence". | **Noted, not repaired.** `corpus/lessons/round-89.md:26` keeps the loose sentence; the landed value satisfies the frozen `ADVANCED` leg and is the right one for the predicate. The prose is loose by one day and is not edited this round (the lesson is a landed round-89 record and the round does not re-verify old rows). |

## Rounds

Round 89 froze a counter whose selftest observed failures without establishing a real
positive (QUALITY35) and whose mutation score was 10/41 (QUALITY36 ground). Round 90
answers on the instrument, not on the data: the successor grader turns each round-89
survivor class into a named `LEG FAIL` with its own selftest negative, ships a
mutation receipt over its own source, and pins its bytes so a stale receipt cannot
describe different bytes than the ones on disk (R90-M1). Two defects were caught by
seats rather than by the author — the unpassable `ENTRY` parse (R90-M3, ReviewerEntry-3)
and the stub-control description (R90-M4, ReviewerDiscipline) — and both are recorded
with the receipts that show them, not repaired inside the frozen claim.

What stays open after this round: the L0 questions `kotodama | round-11` and
`kotodama | round-89` (freshness pause, unanswered); the round-89 defect 3 stale
findings (deferred above); the round-88 debts carried by round 89 (formal L2-planner
conflict, numeric/lowest-axis mapping, round-51/round-69 L0 questions); and the
independent spot-check, which is outside closure. No promotion box becomes `[x]`;
admission is operator-owned. Assimilation: none — the lane has no considerthese
directory and the shokuknow package adoption stays closed.

## Census

Round-end census, run 2026-11-04 from the lane root; full output in
`census-after.txt` beside this draft.

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama; echo rc=$?
… kotodama	W04	S927 duplicate url en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Iron; across scopes
… kotodama	W04	S928 duplicate url en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Bronze_Age; across scopes
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
rc=0

$ python3 -B tools/check-sources-recheck.py --as-of 2026-11-04 --window 90
RECHECK-QUEUE: 0 due / 4 upcoming / 16 on-release / 865 rows
rc=0
```

The warnings are the pre-existing duplicate-URL (W04) and tier-C-mined (W01) rows
named in the round-89 census; none is a new row. The recheck queue is unchanged from
the round-89 landing (`0 due / 4 upcoming / 16 on-release / 865 rows`), which is the
expected shape while freshness is paused: this round adds rows and re-dates none.
