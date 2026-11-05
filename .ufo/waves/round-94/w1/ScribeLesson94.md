# ScribeLesson94 — round-94 lesson draft (calibration axis)

Seat: ScribeLesson94 (scribe). Stage dir `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ScribeLesson94/`. Base `e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2`; freeze `d4ff93c8844e6db33a6e9d85fc7f0848e9f66ca7`. Date: 2026-11-05.

## Output file

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-94/w1/stage/ScribeLesson94/round-94.md` — 21632 bytes, 79 lines (80 with the trailing newline terminator), sha256 recorded in `stage/ScribeLesson94/DONE`.

Section line counts, measured with a line-classifying pass over the file:

| section | lines |
|---|---|
| `# kotodama round 94 — lesson` (H1 + preamble) | 6 |
| `## Gate` | 47 |
| `## Mistakes` | 17 |
| `## Routed-to-95 candidates` | 10 |

Sections are present in the required order (`# kotodama round 94 — lesson`, `## Gate`, `## Mistakes`, `## Routed-to-95 candidates`), measured with `grep -n "^# \|^## "` → lines 1, 7, 54, 71.

**Gate row count: 5 registry rows** (S965, S966, S967, S968, S969), measured with a regex over the `## Gate` block (`^\| S9\d\d \|` → 5). The claim requires at least three rows from S965 up; five are recorded. **Rejected/unreachable bullets: 12**, each with its exact response.

## Every number in the draft, with its command and exit code

All measurements below were run by this seat on 2026-11-05. `/fast/scratch/hyaku/kotodama-r94/ScribeLesson94/` was the scratch; it is deleted before yield.

### Base values (frozen receipt, re-measured)

- `python3 -B reports/round-94/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` → rc 0. Output reproduced the frozen receipt `reports/round-94/predispatch-base.txt` line for line: `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143`, `C1 entry-present 0`, `C2 registry-rows 888 highest-id S964`, `O0 tool-sha256 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7`, `CENSUS rc=0`, `INDEX rc=0`.
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → rc 0, last line `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`.
- `python3 -B tools/check-corpus-index.py --root .` → rc 0, `CORPUS-INDEX: OK files=265 rows=265 findings=0`.
- `git -C <lane> show e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2:tools/check-advance-evidence.py > <scratch>/base-tool.py` → sha256 `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7`.
- `python3 -B <scratch>/base-tool.py --selftest --work <scratch>/st` → rc 0, `SELFTEST PASS 114/114`, exactly 114 lines beginning `  ok ` (counted with a prefix match on the saved output). This is the N = 114 base claim O's SELFTEST leg names.

### Quote verification (19 quotes, independently re-checked)

- Capture sha256 re-measured with `sha256sum` over `stage/ScoutLullaby94/evidence/`: S965.html `10a716133b7f95dea02718946fac92e5b5cd4cbce6c7a6909187bacc5a295757`; S966.pdf `901b0f9236170dfd4a03c8f320f3a089f97233e948c16b0d94ee6209ff11e17b`, S966.txt `5e810ad6bfcabb1fef5f3d04bcbef4600dbcc133f315429a81949bd63c74d201`; S967.pdf `f566dd70905e8be9c6d4964024bc655af1ff7c81e7ce9b5cc3a6eef0848919e6`, S967.txt `72082b74ee639ef614c1bdd40cf817f8af7b0f81cbaf5f5817cbf0fdf9ba635d`; S968.html `232a3e466441d16b73a61a97d2d0d42b548ff18859de2df8bf2f100f4c10914f`; S969.pdf `d7147c8dcf9b374a02e514e01e73a1911bde31157169620a65d0038e1c6fee86`, S969.txt `f37239cf1946ee66386f14d2674f8750fa0a1e1b8f786d6762124d9385e119cc`. All eight match the scout's own table exactly.
- Every quote in the draft (19 of them: 5 anchor quotes plus 14 further located spans) was checked with a byte-level `bytes.count(quote) == 1` against the capture files. Result: **19/19 occur exactly once; 0 occur more than once; every quote is ≤25 words**. This is the scout's stated `grep -F -c` result reproduced independently in Python over raw bytes.
- A second pass over the finished draft extracted every double-quoted span of 25+ characters (29 distinct) and located 19 of them in the captures; the 10 not in a capture are article titles, command cells, and file pointers, not source quotes, and are listed here so the distinction is auditable: two MDPI titles, "Kinderlieder in Translation", "Meaning and Form in Nursery Rhymes Translation", "Local Wisdom and Didactic Values in Lullaby Kawih Mepende Murangkalih", "Freshness axis-move claims are paused until ruled", "awk on column 5 and column 8 of the registry table", "Noted for MutationTester94", and two spans that are fragments of the M3 error-pointer row and the M2 filed-line citation.
- **A defect in my own first draft was found and fixed.** The first write of the draft carried ASCII apostrophes in three quotes (S965 "l'acte de “parler”", S968 "Les élèves s'en servent", S968 "L'interprétation"), so those three did not locate. They were replaced with the byte-exact strings taken from the scout's rows.md (`l’acte`, `s’en`, `qu’ils`, `L’interprétation`, `s’accompagne`, `l’arrivée`) and re-verified: 19/19 locate, 0 multi-occurrences.

### Registry and census, projected state

- `cp -r <lane>/corpus <scratch>/tree/` then the five rows (extracted from the scout's rows.md with `^\| S96[5-9] \|` and a 12-pipe check → exactly 5 rows, 11 cells each, no pipe inside any cell) appended to `<scratch>/tree/corpus/SOURCES.md` immediately before `## Paths`. (Appending before `## Search log` instead gives five `E12 row outside Registry section` findings — measured, then corrected.)
- `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' <scratch>/tree/corpus/SOURCES.md` → **893** (base 888). Highest id **S969** (base S964).
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <scratch>/tree/corpus/SOURCES.md` → rc 0. Finding set identical to the base run's (`sources-census.sh validate --file <lane>/corpus/SOURCES.md`, rc 0) except for the file path in the `ok` line: 35 pre-existing W-findings, **0 E-findings**. The new rows raise no finding. A first run of the same command showed five `E11 missing used-by corpus/knowledge/linguistics/lullaby-child-song-formulae.md` findings, because the entry file is not in the tree yet; re-run after placing the entry path in the tree → rc 0. (An intermediate run also showed three `E11` findings for pre-existing rows S859/S860/S897, an artefact of the scratch tree lacking the lane's `SKILL.md` and `tools/ledger-token-guard.py`; copying those two paths in cleared them, leaving rc 0.)
- `awk -F'|'` over the registry table (columns 5 = tier, 9 = status) on the projected tree: tier-A-any-status 526 → **531**, mined-any-tier 781 → **786**, mined-and-tier-A 470 → **475**.
- The same awk at the two revisions the round-93 spot-check names, for mistake 2: `git -C <lane> show 8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742:corpus/SOURCES.md` and `... 95e7a5cff1687b21d982607ab0bfd8e381c3036c:corpus/SOURCES.md` → tierA 522 / 526, mined 777 / 781, minedA 466 / 470. This independently reproduces the spot-check's numbers and confirms the report label is wrong while the +4 delta is right.

### The A1 counter defect (mistake R94-M3) — measured, not asserted

- Scratch clone: `git clone --shared <lane> <scratch>/work && git -C <scratch>/work checkout --detach e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2` → `rev-parse HEAD` = `e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2`.
- `git -C <scratch>/work apply <lane>/.ufo/waves/round-94/w1/stage/ExecAdjacency94/adjacency.patch` → rc 0. `git -C <scratch>/work diff --numstat` → `1 1 corpus/knowledge/culture-material/adornment-body-codes.md` and `1 1 corpus/knowledge/culture-material/costume-semiotics.md` (two files, two changed lines).
- `python3 -B <scratch>/work/predispatch.py --root <scratch>/work` → rc 0, `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143`. **The frozen counter still reports 2 after a correct repoint.**
- With only the line-33 filter removed from a scratch copy (`if "greet" not in t` → `if True`), the same command → rc 0, `A1 dangling-greeting-pointers 0 ::`.
- Direct probe of the counter's own three candidate paths for each of the two lines → both resolve to `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md`, which exists and matches `greet|leave-taking`. The only thing standing between "resolved" and "counted as resolved" is the filter that discards any target whose path contains "greet" — i.e. the very target the fix is required to use.
- The ExecAdjacency94 seat found the same cause independently and records the same 0 in `stage/ExecAdjacency94/before-after.txt`. The counter and `claims.json` are frozen, so no fix was applied here; this is routed in `## Routed-to-95 candidates`.

### Red-before receipts named in `## Mistakes`

- `stage/ExecBattery94/red-before-v4.txt` → `TOOL sha256=9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7 …`, `BATTERY-SUMMARY survivors=4 unnamed=3 refused=0`. Per class: A1 rc 0 survivor, B1 rc 0 survivor, G1 rc 0 survivor, H1 rc 1 traceback `AttributeError: 'list' object has no attribute 'get'`, I1 rc 1 traceback `IndexError: list index out of range`, J1 rc 1 no traceback refused on APPENDONLY with the wrong verdict direction, K1 rc 0 survivor.
- `stage/ExecMutants94/red-before-v4.txt` → five `MUTANT <name> SURVIVED selftest_rc=0` lines (script-strip-off, comment-strip-off, unescape-off, dispo-any-casei, baserows-drop-cell8) and `MUTATION-SCORE: 0/5 killed, 5 survived, 0 broken-pattern`.
- Stub control: `python3 -B <lane>/reports/round-92/controls/stub-tool.py --selftest --work <scratch>/st2` → rc 0, prints `SELFTEST PASS 89/89` with 34 `  ok ` lines against its own 89-tally — the printed-tally attack the claim's do-nothing control names. Measured here so the draft's sentence about it is not inherited on trust.

### Routed-to-95 items and their evidence pointers (all re-checked here)

- L0 ideophones overlap: `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` line 356 — carries no `L0 ANSWER` (checked by reading the line and testing for that marker). Also `corpus/lessons/round-93-verifier-spotcheck.md` §6 item 5.
- Freshness pause: `.ufo/l0-questions.md` lines 47 and 303 — neither carries an `L0 ANSWER`; the phrase "Freshness axis-move claims are paused until ruled" is present in the file (2 occurrences).
- Title-only exclusions: `corpus/lessons/round-92-verifier-spotcheck.md` §4 and §5 item 1; QUALITY criterion 37 is landed at `corpus/QUALITY.md` line 365; the criterion's own per-bullet sweep over the round-93 lesson's Gate returns **0 of 31** reason-less bullets (command in the draft), but criterion 37 constrains only what a round's own Gate writes and cannot retro-fit the round-92 bullets. The three named re-decisions (Awetí 2015, Zulu Lexikos 2011, Turkish Signifiances 2020) are still recorded as open in `round-93-verifier-spotcheck.md` §6 item 5.
- J1 naming rule: `stage/ExecBattery94/red-before-v4.txt` records J1 as `named=none outcome=UNNAMED` with detail `LEG FAIL APPENDONLY`; the seat's own report discloses that a leg-name-only reading would count it REFUSED. The round-93 critic recorded the class as a wrong-direction refusal.
- F1 not in the battery: `stage/ExecBattery94/manifest.json` lists exactly seven classes — A1, B1, G1, H1, I1, J1, K1 — checked with `python3 -c "import json,re; d=open('.ufo/waves/round-94/w1/stage/ExecBattery94/manifest.json').read(); print(sorted(set(re.findall(r'\"class_name\": \"([A-Z][0-9]?)\"', d))))"` → `['A1', 'B1', 'G1', 'H1', 'I1', 'J1', 'K1']`. No F1 entry. (A first check with the narrower pattern `[A-J]` returned six names and dropped K1; the pattern was widened to `[A-Z][0-9]?` and re-run before this line was written.)
- Mutant patch multiplicities: `stage/ExecMutants94/red-before-v4.txt`'s sibling report `.ufo/waves/round-94/w1/ExecMutants94.md` names the six round-93 patterns that match more than once (self-quote-check-off 2, source-quote-check-off 2, duplicate-id-off 2, duplicate-url-off 3, cellcount-off 2, gap-cap-slash-capture-error-off 2) and states the round-93 score was taken with the same replace-all semantics.

## Not measured / not claimed

- I did not run the battery against a v5 candidate: no v5 candidate existed at the time of writing, and the L1 owns that leg. No post-fix numbers are claimed anywhere in the draft.
- I did not run the full 83-mutant set, the round-92/93 regression grades, or the stub's mutant kills; the draft quotes only the two red-before receipts and the stub selftest, all of which I re-measured or read byte-for-byte.
- I did not verify `claims.json`'s declared after-target for claim A as met: it is not met, and the draft says so with the measured cause.
- The round-94 lesson's `## Gate` records the base and projected-after values of the frozen counter's own lines. The true "after" at the lands revision is the L1's measurement, because no lands revision exists yet; the draft labels the after-values as scratch-measured projections and names the command for each.
- I made no production edit: no file outside my stage dir and my report trailer was written; no commit, push, or mutating git or jj command was run anywhere (read-only `git show`, `git clone --shared`, `git checkout --detach` in scratch, `git diff --numstat`, `git apply` in scratch only).

## Tooling

None installed, none upgraded, no pacman transaction, no sysctl or host change, no network fetch by this seat (the source opens were the ScoutLullaby94 seat's; this seat only read its committed captures). Nothing in the host tooling directive was needed for this task.

## Scratch

`/fast/scratch/hyaku/kotodama-r94/ScribeLesson94/` (clone, mirrored tree, receipts) deleted before yield.
