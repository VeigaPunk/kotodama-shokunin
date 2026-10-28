# Round 76 — ScribeReportCheck (wave 2, leaf scribe)

Seat: `ScribeReportCheck`, wave 2, leaf — no delegation, no background jobs, no `task` spawns.
Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `98c486bdb4650ba5b8e651d332910e8ee60ad121`.
Revisions read: frozen configuration `df0f0309d61e5485bb17035d3f8791b1e6a11d40`; Ca landing
`a43ed807ea38b5fc5a7875a839d576cea73aba7c`; C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a`; latest
lane commit at review `af6744353937e56f296e3094fb077baa1e22f65f`.
Method: read-only `git show <rev>:<path>` / `git ls-tree` / `git log` over committed bytes; no counter, build,
test, linter or formatter was run. Nothing was written except this file.

**Verdict: NOT REVIEWABLE — the draft round-76 report does not exist.** Every item the seat names
(sections/order, wave counts, stale-lane line, tool-install line) is a property of
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotodama.md`, which is absent at review time. I did not
dress the lesson or any sibling seat's file up as that report. I reviewed the only committed round narrative
(`corpus/lessons/round-76.md`) against the same checklist and the report contract, and recorded the findings
the report must not paper over when it is written.

## Behavior

1. **Target check.** `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-76/` lists only `audio.md`,
   `game-dev-2d.md`, `game-dev-3d.md`, `kotoba.md` (dated 2026-10-14/2026-10-27); no `kotodama.md`.
   `git -C /home/vgpnk/Projects/shokunin log --oneline -- .ufo/reports/round-76/kotodama.md` prints nothing;
   `git -C /home/vgpnk/Projects/shokunin status --porcelain` carries no round-76 kotodama path (its only
   `reports` entry is an unrelated ` M .ufo/reports/round-58/chousa.md`).
2. **Fallback review.** Because no report exists, I checked the committed round narrative at `af67443`
   (identical to `722e69f` for every section except `## Routed to round 77`, which `af67443` rewrote to the
   measured outcome): `corpus/lessons/round-76.md` 93 lines; `SCORECARD.md:1509-1555`;
   `reports/round-76/{claims,ledger}.json`; `reports/round-76/telemetry/*`; `reports/round-76/evidence/S894-S896.txt`;
   `.ufo/waves/round-76/{w1,w2,assimilation}`.
3. **Counts re-derived** (not taken from the lesson): base `98c486b` 817 rows / A491 B310 C16 /
   mined722 queued58 rejected37 / 252 knowledge `.md`; at `722e69f` 820 rows / A493 B311 C16 /
   mined725 queued58 rejected37 / 253 knowledge `.md`. Commands: `git show <rev>:corpus/SOURCES.md | grep -cE
   '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` plus the tier/status cells by `awk -F'|'`;
   `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`.
4. **Wave inputs re-derived** for the report's wave-count line (section F7): `w1/dispatch.json` counts
   `spawn 44 / total 44`, registry 44; `w1/w1-results.json` `seats: 44`, `results: 44`;
   `w2/dispatch.json` counts `spawn 32 / total 32`, registry 32; `w2/spec.json` `items: 32`.

## Required sections / order — cannot be verified, checklist recorded

Contract source: `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-76.md:99-125` (identical to
`templates/round-prompt.md` §4). The filed report must carry, **in this order**: `## Work performed`
(opening by naming claims C and Ca and their axes, then one bullet per item with an evidence pointer),
`## Landed changes` (each row tied to a LOG.md entry **and** a commit hash), `## Before → after measurements`
(one per claim, with counting command and measured commit), `## Sources & frontier` (rows before→after with the
counting command, rows by tier, rows touched old→new — conformance item, not a marker predicate),
`## Trend verdicts` (one each for expansion / quality / discernment, no scalar), `## SHONEN` (one line per box,
`[x]` only with a named non-author verifier, `[~]` with a resolvable pointer). Round-75 precedent adds
`Tool installs:` and `Stale-lane:` lines (`.ufo/reports/round-75/kotodama.md:17,52-54`), and the seat checklist
names them explicitly. None of these can be checked until the file exists; findings F1, F2 and F8 below are the
pre-filing blockers for the same checklist.

## Findings (exact evidence)

### F1 — BLOCKER: draft report absent
Evidence: `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-76/` (no `kotodama.md`);
`git -C /home/vgpnk/Projects/shokunin log --oneline -- .ufo/reports/round-76/kotodama.md` → empty.
Consequence: sections/order, wave counts, stale-lane line, tool-install line are unverifiable at submission
time. This is a statement of absence, not a review.

### F2 — HIGH: no LOG.md round-76 entry, so `## Landed changes` cannot cite one
`git show af67443:LOG.md | grep -c 'Round 76\|round-76'` → `0`; `LOG.md` ends inside the round-75 entry
(`- **Tool installs:** none. **Stale-lane:** none.` at the file's last line). The contract at
`.ufo/prompts/kotodama-round-76.md:107-108` requires every landed change tied to a LOG.md entry; the entry
(and its wave-shape / tool-install / stale-lane lines, round-75 precedent `LOG.md` round-75 entry) must exist
before the report can be filed honestly.

### F3 — HIGH: claim-C rows landed **before** the cited freeze commit, and the control receipt asserts otherwise
- `cab5247` (“round-76: correct base ground and mirror receipts”) appends `S894`–`S896`, the Paths line
  `- calendar-standard design — S896 → S895 → S894` and the `**State-standard calendar compilation (round 76).**`
  search-log paragraph to `corpus/SOURCES.md` (`git diff b4965d5 cab5247 -- corpus/SOURCES.md`; 817 → 820).
- Row counts per rev (`git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`):
  `98c486b` 817, `b4965d5` 817, `df0f0309` **820**, `a43ed80` 820, `722e69f` 820. The entry file is absent at
  `df0f0309`/`a43ed80` and present only at `722e69f`
  (`git cat-file -e <rev>:corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`).
- `reports/round-76/telemetry/controls-c.txt` (committed `58e6c81`, measured at `df0f0309`) annotates control 1 as
  `## control 1: lands == freeze (legal ancestor relation; no data landed)` — false at `df0f0309`: three of the
  claim's four data artifacts (rows + Paths + search log) are present; only the entry is absent. The same run's
  CENSUS leg shows the consequence: `census TSV carries E-code line(s): E11 … S896 missing used-by …`.
- The report must attribute the row append to `cab5247` (not to the `722e69f` landing), and must not present
  `df0f0309` as a pre-data tree. The frozen claim's own control text survives (`claims.json` C
  `do_nothing_control` asks only that ENTRIES/ROWS/GATE/EVIDENCE/GROUND/INDEX fail with FROZENCFG green; observed
  1/13 with FROZENCFG green, `controls-c.txt`), so this is a **sequencing/receipt-wording defect, not a
  counter failure** — exactly the boundary the report has to state.

### F4 — HIGH: `validate-receipt.txt` contradicts itself at the commit that carries it
`git show df0f0309:.ufo/waves/round-76/assimilation/validate-receipt.txt:1-2` reads “Round-76 final scratch
mirror before registry append … **live lane SOURCES.md has not yet been appended**”, while
`git show df0f0309:corpus/SOURCES.md` has 820 rows (the same commit's parent chain appended them at `cab5247`;
`validate-receipt.txt` was added by `cab5247` itself). The lesson cites this file as the 820-row mirror receipt
(`corpus/lessons/round-76.md:80-81`), so a report sentence such as “the mirror was validated before the live
append” would be false as written. It is usable only as a mirror-receipt with the append already in-tree.

### F5 — HIGH: claim Ca's frozen do-nothing control description is contradicted by its committed receipt
`reports/round-76/claims.json` (Ca `do_nothing_control`, at `af67443`) states: at `lands == <freeze>` the run
“FAILS with REPAIR and ANNOTATE red (and RECEIPTS red …), R1EXEMPT green …, FROZENCFG and LEDGER green”.
`git show af67443:reports/round-76/telemetry/controls-ca.txt` (control 1, measured at `df0f0309`) observes:
`LEG FAIL LEDGER`, `LEG FAIL REPAIR`, `LEG FAIL ANNOTATE`, `LEG FAIL NOSTUB`, `LEG PASS APPENDONLY`,
`LEG FAIL R1EXEMPT`, `LEG FAIL SEPARABLE`, `LEG PASS RECEIPTS`, `LEG FAIL COMBINED`, `LEG PASS FROZENCFG`,
`LEG PASS STAMP` → `ACCEPT-CA-76: FAIL legs=5/12`. Only BASEMISMATCH/APPENDONLY/RECEIPTS/FROZENCFG/STAMP pass.
The receipt's own `# expected: exit=1, FAIL on REPAIR/ANNOTATE/R1EXEMPT, PASS on FROZENCFG and LEDGER` repeats
the same false expectation. The lesson (`corpus/lessons/round-76.md:89-91`) and `SCORECARD.md:1534-1555` report
the lands outcome but neither discloses this control mismatch. The report must print the observed control legs
(5/12, exact red set) and route the claim-text defect; quoting the claim's expectation as if measured would be a
false control statement.

### F6 — MEDIUM: `junk-ca.txt` is named by the frozen claim but does not exist for round 76
Ca `do_nothing_control` names “plus junk-ca.txt fixture controls … named at the freeze”.
`git ls-tree -r --name-only af67443 | grep -i junk-ca` returns only `reports/round-74/telemetry/junk-ca.txt`
and `reports/round-75/telemetry/junk-ca.txt`. A report bullet must not cite a round-76 `junk-ca.txt`; state the
fixture set as absent and the consequence (no round-76 junk-landing control for Ca).

### F7 — MEDIUM: verified wave counts for the report (w1 has four seats without report files)
Derived counts to state: **w1 = 44 seats** (`w1/dispatch.json` `counts {spawn:44,total:44}`, registry 44,
`w1/w1-results.json` `seats:44`/`results:44`; roles from `results[].agent`: scout 14 / executor 9 / scribe 9 /
critic 4 / reviewer 2 / mutation-tester 2 / connector 2 / sentinel 1 / revenger 1), **w2 = 32 seats**
(`w2/dispatch.json` counts 32/32, registry members 32; `w2/spec.json` items 32; roles critic 7 / reviewer 6 /
mutation-tester 6 / executor 5 / scout 4 / scribe 2 / connector 2), **round total 76**.
**Four w1 seats settled with no report file:** `ScoutPackageTriage`, `CritClaims2`, `RevVerifierDefects`,
`MutOldCa` (`ls .ufo/waves/round-76/w1/*.md | wc -l` → 40 vs 44 result names; their `results[]` entries carry
no `report` field, and `CritClaims2`'s own output names `.ufo/waves/round-76/w1/CritClaims2.md`, which does not
exist). A bare “dead seats: none” line would be false; the report must name these four as missing-report seats
(their outputs are truncated `think`-prefixed fragments, not usable evidence). At review time 12 of 32 w2 report
files exist in `.ufo/waves/round-76/w2/`; the final count is the L1's to fill in.

### F8 — MEDIUM: the lane is not clean, so `Stale-lane: none` cannot be filed yet
`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain` at review:
` M .ufo/waves/round-76/w1/stage/ExecAdaptC/claim-C.json` plus untracked `reports/round-76/counters/`,
`.ufo/waves/round-76/w2/`, `.ufo/waves/round-76/w2.ready`, `.ufo/waves/round-76/w2.ready.dispatched`,
`.ufo/waves/round-76/selftest.sh`. The modified stage file replaces the frozen INDEX predicate line
(`… the heading count is 41 …`, still the text in `reports/round-76/claims.json`) with
`… validate-receipt.txt` shows `validate --file` exit 0 …` — a stage-copy edit only; the frozen
`reports/round-76/claims.json` is untouched (`git diff --stat` lists only the stage file). Restore the stage
copy or disclose it; the round's own waves are otherwise untracked and would be committed at filing.
The fleet repo's ` M .ufo/reports/round-58/chousa.md` is another lane's file, not kotodama's.

### F9 — LOW (verified clean): every lesson evidence pointer resolves and supports its sentence
All 18 cited paths exist at `722e69f` and `af67443`: `reports/round-76/evidence/S894.txt|S895.txt|S896.txt`;
`w1/stage/ExecCensusRows/window/S896-openstd.showGb-followed-2026-10-27.html`,
`…/S895-xingzuobaike.com-2026-10-27.html`; `w1/RevengerMistakes.md` §2,
`w1/stage/RevengerMistakes/recurrence.txt`; `w1/stage/L1/freeze-control-legcount-redbefore.txt`,
`…/pre-data-counter-repair.txt`; `reports/round-76/telemetry/{controls-c.txt,census-start.txt,census-end.txt}`;
`w1/ScoutQuarantine.md`; `reports/round-71/telemetry/quarantine-verdicts.md`;
`assimilation/guard-proof/planted-1space-proof.txt` and `planted-4space-proof.txt`;
`assimilation/validate-receipt.txt`. Content checks that agree with the lesson:
- Collision guard: `w1/stage/ScribeLesson-7/measurements.txt` records `817 / 132 / 35` and exactly the three
  lesson sha256 values (`97eef07a…`, `bab11d7d…`, `be203dd8…`); 1-space proof output contains `| S897 |`,
  `exit=0`; 4-space proof `output: (no rows)`, `exit=1` (lesson lines 72-76).
- Quarantine: `quarantine-verdicts.md` per-row tally = **PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4** (21 rows);
  `w1/ScoutQuarantine.md` also 21 rows, including S807/S812/S835 with the trailing-backtick note (lesson 47-70).
- Validate receipt: the **seven** MANUAL blocks (rows 820; malformed-NF 0; tier A=493 B=311 C=16;
  status mined=725 queued=58 rejected=37; duplicate-ids none; enum/tier-inflation none; missing mined used-by
  none) all `exit=0` (lesson line 83).
- Census end: `reports/round-76/telemetry/census-end.txt` ends `kotodama ok …` `exit=0` with only W04
  duplicate-URL lines and W01 tierC lines for pre-existing S881/S882/S884/S893 — no E-code, as the lesson says.
- Gate quotes: each is present **3×** in its own evidence window (`grep -c` on S894/S895/S896), and the window
  headers carry `bytes`, `sha256`, `quote-found: yes`, `quote-words: 4`, `quote-chars: 18` (S894) — within the
  ≤25-token/≤80-char rule (lesson lines 9-13).
- Rows: S894-S896 are 11 cells each (`awk -F'|' … NF=13`), tier A/A/B, status mined, recheck `180d`, opened
  `2026-10-27`; `used-by` names only
  `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`, which cites S894 ×10,
  S895 ×9, S896 ×13. Lesson 78-81 is accurate.

### F10 — LOW: claim-verdict honesty at the land level is accurate (verified, not taken on trust)
`reports/round-76/telemetry/measures-c.txt` → `ACCEPT-C-76: FAIL legs=11/13` with only `ROWS` and `COLLCHECK`
red; `measures-ca.txt` → `ACCEPT-CA-76: FAIL legs=5/12` with LEDGER/REPAIR/ANNOTATE/NOSTUB/R1EXEMPT/SEPARABLE/
COMBINED red. `corpus/lessons/round-76.md:89-91` (at `af67443`) enumerates exactly those legs;
`SCORECARD.md:1537-1555` says “Neither frozen acceptance counter passes … no score delta”. No committed
artifact claims a round-76 PASS (`git grep -n 'ACCEPT-C-76\|ACCEPT-CA-76' af67443` returns only the lesson's
FAIL line). Two wording points the report should keep precise:
- Ca REPAIR is red because the frozen `statement_after` regex pins the phrase ``committed counter sha256``
  (`ledger.json` L76-16), which the repaired `SKILL.md:707` row does not contain
  (`git show af67443:SKILL.md | grep -c 'committed counter sha256'` → 0), while both digests **are** present
  (`fa5060b91bdb` ×1, `315c5f3f27fd` ×1). The SCORECARD sentence (`SCORECARD.md:1534`) is substantively true;
  the counter is red on a phrase mismatch. Say that, not “the repair is missing”.
- `reports/round-76/telemetry/selftest-ca.txt` lines 46-48 place three `ERROR: …` negative-probe lines **after**
  `SELFTEST: 170/170`; a report citing the file as a green selftest must say those lines are refusal probes,
  otherwise the receipt reads as failing. `selftest-c.txt` ends cleanly (`SELFTEST: 89/89`).

### F11 — LOW: stale counts the report's `## SHONEN` section must not present as current
`SHONEN.md` (protected, append-only under Ca) still carries round-75 close counts in its first box
(“rows: 808 … close counts to 817 rows / 722 mined”); the registry at `af67443` is 820 / 725 / 58 / 37, and
round 76 admitted no claim. The report's SHONEN lines must cite SHONEN.md as the checklist with `[~]`
pointers and note the count staleness, not re-assert 817/722 as round-76 close values.

### F12 — LOW: lesson has no `## Corrections` section
`corpus/lessons/round-76.md` sections in order: Gate, Quarantine, Collision guard, Normalization, Census,
Mistakes, Routed to round 77, Sources & frontier. Round 75’s lesson carried `## Corrections`; round 76’s Ca
corrections table lives in `SCORECARD.md:1509-1534`, which the frozen claim names. Confirm (ScribeSourceReview’s
lane) whether a lesson `## Corrections` stub is owed; no wave-2 repair has been applied, so today the section
would be empty.

## Gates (this seat — read-only)

- No lane byte written outside `.ufo/waves/round-76/w2/ScribeReportCheck.md`; no claim, counter, lane file,
  ledger, report, SCORECARD, LOG, SHONEN or source tree edited; nothing committed or pushed.
- No build, test, linter, formatter, counter or census executed. Only `git show`/`git ls-tree`/`git log`/
  `git diff`/`git status` and text filters (grep/awk/python over piped bytes).
- No scratch directory created (nothing to remove); `/fast/scratch/hyaku/kotodama-r76/` was read only for
  existence checks.
- `/home/vgpnk/Projects/shokuknow` not touched. No `pacman`/`uv`/`npm`/`cargo` invocation.

## Tool installs

None. No tool, package or runtime was installed, upgraded or removed; nothing was added to `PATH`. The
authorization in `/home/vgpnk/.omp/agent/RULES.md` was read before any work, and no install was needed for this
read-only falsification.

## Touched surfaces

| surface | access |
|---|---|
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w2/ScribeReportCheck.md` | created (this report) |
| lane git objects (`git show` at `98c486b`, `b4965d5`, `6a5d63a`, `cab5247`, `70cc799`, `df0f0309`, `58e6c81`, `a43ed80`, `788bd56`, `722e69f`, `af67443`) | read-only |
| `/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/`, `.ufo/prompts/kotodama-round-76.md`, `templates/round-prompt.md`, `.ufo/reports/round-75/kotodama.md` | read-only |
| `/home/vgpnk/.omp/agent/RULES.md` | read-only |

## Out of scope

- Writing or repairing the report, lesson, LOG, SCORECARD, SHONEN, claims, ledger, counters or wave files.
- Re-running `accept-c.py`/`accept-ca.py`, the census, or any selftest; those belong to the executor/critic/
  mutation seats. My claim verdicts above are read from the committed receipts, as the seat instructs.
- Adjudicating the C/Ca claim outcome itself (the canonical Rust judge rules); I only record whether the
  committed narrative matches the committed receipts.
- Lesson section completeness against CORPUS.md (`ScribeSourceReview`) and source Gate completeness
  (`RevLessonGate`); findings F12 and F9 are cross-references, not a competing review.

## Artifact paths

- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w2/ScribeReportCheck.md`
- Absent target: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotodama.md`
- Reviewed narrative: `corpus/lessons/round-76.md` (at `af67443`), `SCORECARD.md:1509-1555`
- Receipts cited: `reports/round-76/telemetry/{measures-c.txt,measures-ca.txt,controls-c.txt,controls-ca.txt,
  census-start.txt,census-end.txt,selftest-c.txt,selftest-ca.txt}`; `reports/round-76/evidence/S894-S896.txt`
- Wave inputs: `.ufo/waves/round-76/w1/{dispatch.json,w1-results.json}`, `.ufo/waves/round-76/w2/{dispatch.json,
  spec.json,swarm-registry.json}`, `.ufo/waves/round-76/w1/*.md`
