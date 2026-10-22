# Round 54 — inherited state (attempt 1) — seat ScribeInheritedState

Seat: `ScribeInheritedState` (scribe), attempt 2 of kotodama round 54 (hyaku phase 3, 2026-10-22).
Scope: the round-54 lesson section `## Inherited state (attempt 1)`, plus the state audit behind it.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch `main`, jj-colocated). I read only; I wrote
only this file. No install was needed; no tool was installed or upgraded.

---

## 1. Draft lesson section (paste-ready)

```markdown
## Inherited state (attempt 1)

Round 54, attempt 1, ran from 17:09Z to 17:26Z and left five pushed commits and no build-wave report.
The wave watchdog recorded the lane's death and the retry: attempt 1 launched at 2026-10-22T14:09:03-03:00
(17:09:03Z) and was marked `lane-dead-no-report` at 14:30:09-03:00 (17:30:09Z) with the cause
"omp process restart at 17:26Z; no landed report; fresh successor inherits work"; attempt 2 launched two
seconds later at 14:30:11-03:00 (17:30:11Z).

What attempt 1 pushed (lane log `e0bfb13e..7fa37fbb`, author dates, lane-local -03:00):

| commit | time | what |
|---|---|---|
| `d761ee8` | 13:00:12 | prerequisite: the round-53 closure's routed fixes (gesture entry lines 68/133/150/199, speech-surrogates line 75 re-cited from S145 to S185, S145 retired as superseded, S225 access note, `corpus/lessons/README.md` row for the round-53 spot-check) |
| `4b2299b` | 14:15:29 | claim C's instruments: `reports/round-54/accept-c.py`, `base-knowledge-files.txt` (229 paths), `criterion11-controls.py`, the start census receipt |
| `1ec84db` | 14:16:54 | the declaration: `claims.json` (claim C), the clause list, `dry-run.py`, `claims-agree.py`, `separability-manifest.json`, the criterion-11 receipt and the dry-run receipt |
| `260c68d` | 14:22:23 | the instruments revised after the two pre-dispatch critic seats: SET walks every file under `corpus/knowledge` and not only `*.md`; RANGE fails a cited id with no row or with two rows and fails any S-id range notation; five further red controls (RED-COUNT, RED-SET-EXT, RED-RANGE-NOROW, RED-RANGE-DUP, RED-RANGE-SPAN) added |
| `7fa37fb` | 14:22:24 | the declaration revised to match: claim C's statement, its eight-clause list, the controls receipt (13 legs: one GREEN and twelve REDs) and the dry-run receipt |

Those five commits are the round's real inheritance and all five survive into attempt 2 unchanged: the
prerequisite `d761ee8`, the claim base `260c68d` and the declaration `7fa37fbb` are the same three
references attempt 2 ran on. The declaration's own `before` state was measured and filed before the wave
dispatched, so nothing about the claim needed re-deciding; what needed re-doing was the work itself.

The dead wave. Attempt 1's build wave was a 36-seat registry (`.ufo/waves/round-54/build/swarm-registry.json`,
`createdAt` 2026-10-22T17:19:54.138Z, `updatedAt` 2026-10-22T17:22:52.217Z, wave `kotodama-r54-build`,
report directory `.ufo/waves/round-54/build`): 26 scouts, 2 connectors, 4 critics, 4 reviewers, every
member with `agentId: null`. The registry was updated at 17:22:52Z, which is when the wave dispatched, and
the omp process restart at 17:26Z killed the seats roughly three minutes later. The proof that no seat
reported is in the tree, not in the log: `.ufo/waves/round-54/build/` holds exactly one file, the registry
itself, and no `<Seat>.md` was ever written there; a lane-wide search for `ScoutGelede.md`,
`CriticCalibrationMasks.md`, `ReviewRoutedFixes.md` and `ScoutYupik.md` finds no attempt-1 report anywhere
in the lane or in the attempt-1 scratch. The 36 dead seats are:

ConnectInLaneMasks, ConnectSiblingMasks, CriticCalibrationMasks, CriticGapPremise, CriticMistakeMining,
CriticSingleClaim, ReviewEntryContract, ReviewGateSplits, ReviewRoutedFixes, ReviewSacredAccess,
ScoutCham, ScoutCommedia, ScoutDeathMasksAncient, ScoutEgungun, ScoutEntryMechanics, ScoutEuropeanCarnival,
ScoutGelede, ScoutGuleWamkulu, ScoutHaudenosauneeStatement, ScoutKwakwakawakw, ScoutMalagan,
ScoutMaskTheory, ScoutMaskVoice, ScoutMexicaMosaic, ScoutMummering, ScoutNoh, ScoutNuo, ScoutParachicos,
ScoutPersonaProsopon, ScoutRomanImagines, ScoutS225Recheck, ScoutSowei, ScoutSriLankaKolam, ScoutTalchum,
ScoutVenice, ScoutYupik.

Their cause is one cause, not thirty-six: the omp process restart at 17:26Z. They were never resumed; the
watchdog's retry line says a fresh successor inherits the work.

Attempt 1's scratch is not evidence. `/fast/scratch/hyaku/kotodama-r54/` holds 30 attempt-1 seat
directories, 8082 files in total, and it is a census of a dead wave, not a record of sources. Eight of the
36 registered seats never created a directory there at all (ConnectInLaneMasks, CriticGapPremise,
CriticSingleClaim, ReviewSacredAccess, ScoutCommedia, ScoutEntryMechanics, ScoutHaudenosauneeStatement,
ScoutMexicaMosaic) and ScoutCham's directory is empty. Two directories in that tree are not build-wave
seats: `CriticClauseList` (3903 files) and `CriticControlsReplay` (3907 files) belong to the two
pre-dispatch critic seats, whose reports did land and are committed at `.ufo/waves/round-54/predispatch/`.
The scratch also shows why it cannot be cited: `ScoutGelede/gelede-unesco.html` is a bot-challenge page
("Please enable JavaScript to view the page content", a support id, the word "captcha" twice) and
`ScoutGelede/ajol.html` is an nginx 403 body, while two files named as PDFs there
(`ScoutGelede/ajol.pdf`, `ScoutGelede/gelede-00002-EN.pdf`) are HTML documents. Attempt 2 therefore
re-opens every source itself; the scratch is read only as a count and a warning.

What attempt 2 re-verifies rather than trusts. Three attempt-2 seats exist for this, and each names the
artifact it is checking:

- `ExecControlsReplay` re-runs the criterion-11 control builder in a sandbox clone of the lane at
  `7fa37fbb`, diffs its output against the committed receipt, recomputes every sha256 the receipt lists,
  and then builds one further near-miss for the SET and RANGE legs of `accept-c.py` that the receipt does
  not already cover.
- `ExecDryRunCensus` re-runs the declaration's before-state in a sandbox clone at `7fa37fbb`:
  `accept-c.py`, `dry-run.py` and its check mode, `check-claim-separability.py`, `claims-agree.py`,
  `check-source-access.py`, `reports/round-28/readme/sweep.py` and the sources census, and compares each
  result with the declaration's `expected_pre_landing_counting` and with the lane's own `git diff --stat`
  and `git status --porcelain` against `7fa37fbb`.
- `ReviewRoutedFixes` attacks the prerequisite `d761ee8` line by line against the round-53 closure's routed
  items: gesture entry lines 68 (S201's printed page for the Northamptonshire and Campania data, the "wide
  hand point" and the Kendon 208 quote), 133 (S221), 150 (S223), 199 (S234), speech-surrogates line 75
  (S185 now cited), and the `SOURCES.md` edits (S145 rejected as superseded, S185 mined, S225 access note)
  and the lessons README row.

The rest of attempt 2 repeats attempt 1's seat prompts unchanged except for the report directory: 35 of the
36 inherited seats carry a byte-identical prompt once the `Report:` trailer is removed, and
`CriticMistakeMining` differs only in its scratch path (`kotodama-r54` becomes `kotodama-r54-a2`) and its
report path. Attempt 2 adds six seats the round had not had: four executors (`ExecControlsReplay`,
`ExecDryRunCensus`, `ExecGateQuoteCheck`, `ExecIntegrateRows`) and two scribes (`ScribeInheritedState`,
`ScribeSpotcheckRouting`), for 42 seats in all.
```

---

## 2. The five pushed attempt-1 commits

Command:

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --format='%h %ad %s' --date=iso e0bfb13e..7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c
```

Output (trimmed to what matters):

```
7fa37fb 2026-10-22 14:22:24 -0300 round-54: declaration revised before dispatch — claim C statement, clause list and controls receipt (13/13), dry run
260c68d 2026-10-22 14:22:23 -0300 round-54: claim C instruments revised before dispatch (SET walks every file; RANGE fails duplicate rows and range notation; five more red controls) after the pre-dispatch critic findings
1ec84db 2026-10-22 14:16:54 -0300 round-54: declaration — claim C (masks and masquerade entry), clause list, criterion-11 controls receipt, dry run
4b2299b 2026-10-22 14:15:29 -0300 round-54: claim C instruments (accept-c.py, base knowledge list, criterion-11 control builder, start census)
d761ee8 2026-10-22 13:00:12 -0300 round-54: prerequisite — round-53 closure routed fixes (gesture lines 68/133/150/199, speech-surrogates line 75 to S185, S145 retired, S225 access note, spot-check index row)
```

(All five subject lines read "round-54"; the em dashes and the S-id list in `d761ee8`'s subject are the
commit message's own wording.)

What each commit carries, from `git show --stat`:

| commit | files | content |
|---|---|---|
| `d761ee8` | 4 files, +14/−9 | `corpus/SOURCES.md` (6 lines: S145 rejected as superseded, S185 queued→mined, S225 access note), `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` (8 lines), `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (2 lines), `corpus/lessons/README.md` (7 lines) |
| `4b2299b` | 4 files, +500 | `reports/round-54/accept-c.py` (102), `base-knowledge-files.txt` (229 paths), `criterion11-controls.py` (155), `telemetry/census-start.txt` (14) |
| `1ec84db` | 6 files, +341 | `claims-agree.py`, `claims.json`, `dry-run.py`, `separability-manifest.json`, `telemetry/criterion11-controls.txt`, `telemetry/declaration-dry-run.txt` |
| `260c68d` | 4 files, +172/−27 | `predispatch/CriticClauseList.md`, `predispatch/CriticControlsReplay.md`, revised `accept-c.py` (SET walks every file; RANGE fails duplicate rows and range notation; `UnicodeDecodeError` caught), revised `criterion11-controls.py` (+5 red controls) |
| `7fa37fb` | 4 files, +142/−31 | revised `claims.json` (statement, 8 clauses, control receipt reference), revised `separability-manifest.json`, revised `telemetry/criterion11-controls.txt`, revised `telemetry/declaration-dry-run.txt` |

Author dates vs committer dates differ for `d761ee8` (authored 13:00:12, committed 14:15:16) and `7fa37fb`
(authored 14:22:24, committed 14:22:41) — both are rebase/amend artefacts of the pre-dispatch revision
cycle. The declaration hash `7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c` is what attempt 2's context names, and
`git rev-parse` of the lane's `main` gives `5757c45118771d8baac238b52aa5e95fc18cbd54` as the current tip
(commit `5757c45`, 15:34:44, "attempt-1 dead build-wave dispatch records (36 seats, omp restart 17:26Z, no
reports) committed as evidence; attempt-2 build-a2 spec (42 seats: +4 executors, +2 scribes), generator,
dispatch and sent payload; census at attempt-2 start"). Read-only `jj --ignore-working-copy status` in the
lane agrees: working copy `8ee0468b` empty, parent `5757c451`.

---

## 3. Untracked paths and the decision rule

Command:

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain
```

Output at the time of this seat's run (15:38–15:42 lane-local, 18:38–18:42Z):

```
?? .ufo/waves/round-54/build-a2/
```

with `--untracked-files=all`:

```
?? .ufo/waves/round-54/build-a2/CriticSingleClaim.md
?? .ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md
?? .ufo/waves/round-54/build-a2/ScoutS225Recheck.md
?? .ufo/waves/round-54/build-a2/ScoutSriLankaKolam.md
?? .ufo/waves/round-54/build-a2/swarm-registry.json
```

(the list grows as attempt-2 seats land; 20 seat reports were present when this report was written).

**Conflict with my assignment, stated verbatim.** My assignment says the expected untracked set is
`.ufo/waves/round-54/build-dispatch.json`, `build-sent-payload.json`, `build-spec.json`,
`build/swarm-registry.json`, `gen-build-spec.py`. Those five paths are **no longer untracked**. They were
committed by `5757c45` (15:34:44) while attempt 2 was running, together with the attempt-2 spec, dispatch,
sent payload and the attempt-2 start census. `git ls-files .ufo/waves/round-54/` now lists all eight wave
artifacts plus the two pre-dispatch critic reports, and the only untracked thing is the live `build-a2/`
report directory. The assignment's expectation was true when it was written and was overtaken by the L1's
own commit while I worked; the decision rule it names has therefore already been executed.

The decision rule, and what each path is:

| path | what it is | fate |
|---|---|---|
| `.ufo/waves/round-54/build-spec.json` (52 578 bytes) | attempt 1's wave spec: wave `kotodama-r54-build`, reportDir `.ufo/waves/round-54/build`, axes coverage+calibration, the shared context, and 36 items (name, role, axes, prompt) | committed as dead-wave evidence in `5757c45` |
| `.ufo/waves/round-54/build-dispatch.json` (73 805) | attempt 1's dispatch record: schema `ufo-swarm-wave-dispatch-v1`, policy (maxLanes 100, hardCeiling 256, rampBatchSize 5), counts `{spawn: 36, resume: 0, total: 36}`, the embedded registry, `compaction.applied: false`, the `taskCall` with 36 tasks, `resumeSends: []`, and the note "Issue exactly one batched task call ... never split a wave into multiple task calls" | committed as dead-wave evidence |
| `.ufo/waves/round-54/build-sent-payload.json` (63 165) | the exact payload sent to the wave: the same context plus 36 `{name, task, agent}` tasks | committed as dead-wave evidence |
| `.ufo/waves/round-54/build/swarm-registry.json` (10 607) | attempt 1's 36-seat registry (`createdAt` 2026-10-22T17:19:54.138Z, `updatedAt` 2026-10-22T17:22:52.217Z, `wave` `kotodama-r54-build`, `reportDir` `.ufo/waves/round-54/build`; 26 scout / 2 connector / 4 critic / 4 reviewer; every `agentId` null) | committed as dead-wave evidence |
| `.ufo/waves/round-54/gen-build-spec.py` (32 442) | the generator that produced the spec, the dispatch, the payload and the registry | committed — **but overwritten in place** at 14:46 for attempt 2: it now writes `build-a2-spec.json`, names wave `kotodama-r54-a2-build`, sets `SCR = /fast/scratch/hyaku/kotodama-r54-a2` and reportDir `.ufo/waves/round-54/build-a2`, and adds the six attempt-2 seats. The attempt-1 generator source is therefore **not** recoverable from the lane; only the attempt-1 generated JSON survives |

Attempt 2's own artifacts, for symmetry: `build-a2-spec.json` (65 263 bytes, 42 items),
`build-a2-dispatch.json` (90 247, counts `{spawn: 42, resume: 0, total: 42}`,
`registry.path` `.ufo/waves/round-54/build-a2/swarm-registry.json`), `build-a2-sent-payload.json` (75 046,
42 tasks, `context` byte-identical to the spec's context) and `build-a2/swarm-registry.json` (12 478,
`createdAt` = `updatedAt` = 2026-10-22T17:46:52.913Z, 42 members: 26 scout / 2 connector / 4 critic /
4 reviewer / 4 executor / 2 scribe). The a2 registry file is mode `0600` and is still untracked at the time
of writing; the a1 registry, also mode `0600`, is tracked. The a2 dispatch's embedded registry and the
a2 registry file carry the same 42 member names (`set(...) == set(...)` true for both waves), and likewise
for attempt 1.

---

## 4. The dead attempt-1 seats

Source of truth: `.ufo/waves/round-54/build/swarm-registry.json` (36 members) and
`.ufo/waves/round-54/build-sent-payload.json` (36 tasks, same names). All 36 registry members carry
`agentId: null`; the registry's `updatedAt` (17:22:52.217Z) is the dispatch moment; no `.md` report was
ever written under `.ufo/waves/round-54/build/`.

Command and output (trimmed):

```
find /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build -type f | wc -l
1
```

```
find /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r54 \
  -name 'ScoutGelede.md' -o -name 'CriticCalibrationMasks.md' -o -name 'ReviewRoutedFixes.md' -o -name 'ScoutYupik.md'
(no output)
```

Attempt-1 scratch census (files per seat directory, `find | wc -l`; **not evidence**, only a count):

```
   1  ConnectSiblingMasks            31  CriticCalibrationMasks     29  ScoutGuleWamkulu
   2  ReviewEntryContract             7  ReviewGateSplits          30  ScoutKwakwakawakw
   7  ReviewRoutedFixes               0  ScoutCham                 12  ScoutMalagan
  22  ScoutDeathMasksAncient          4  ScoutEuropeanCarnival      7  ScoutMaskTheory
   9  ScoutEgungun                    8  ScoutGelede                4  ScoutMaskVoice
   1  ScoutMummering                 12  ScoutNoh                   1  ScoutNuo
  10  ScoutParachicos                11  ScoutPersonaProsopon       6  ScoutRomanImagines
   5  ScoutS225Recheck               14  ScoutSowei                10  ScoutSriLankaKolam
   8  ScoutTalchum                    7  ScoutVenice               12  ScoutYupik
3903  CriticClauseList (pre-dispatch seat, report landed)
3907  CriticControlsReplay (pre-dispatch seat, report landed)
8082 files total in seat directories
```

Eight registered seats have no attempt-1 scratch directory at all: ConnectInLaneMasks, CriticGapPremise,
CriticSingleClaim, ReviewSacredAccess, ScoutCommedia, ScoutEntryMechanics, ScoutHaudenosauneeStatement,
ScoutMexicaMosaic. `ScoutCham`'s directory exists and is empty.

Why the scratch cannot be cited: `ScoutGelede/gelede-unesco.html` (44 243 bytes) is a bot-challenge page —
"Please enable JavaScript to view the page content.", "Your support ID is: 5619449045325002101.", "What
code is in the image?", and the word "captcha" twice; `ScoutGelede/ajol.html` and `ScoutGelede/ajol.pdf` are
an nginx "403 Forbidden" body; `ScoutGelede/gelede-00002-EN.pdf` is an HTML document, not a PDF. The
attempt-1 wave had also reached one genuine PDF per seat in places (`ScoutGuleWamkulu/nom-00142-EN.pdf`,
10 pages; `ReviewRoutedFixes/s201.pdf`, 20 pages) — but a file left in a dead seat's scratch is not an
opened source. Attempt 2 re-opens everything.

---

## 5. What attempt 2 re-verifies

Attempt 2 adds six seats to the 36 inherited ones. Four are executors and two are scribes; attempt 1 had
**no** executor and **no** scribe seat (roles were 26 scout / 2 connector / 4 critic / 4 reviewer), which is
why nothing was replayed or re-measured in attempt 1 before it died.

`ExecControlsReplay` (executor; axes coverage+calibration) — verbatim task:

> Re-verify inherited attempt-1 input. `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin
> /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane` (a sandbox clone; never run anything that
> writes git in the lane itself), then in the clone `git checkout -q
> 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c`. Run the criterion-11 control builder exactly as
> /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-54/telemetry/criterion11-controls.txt says
> it was run (read its header), write the output to your scratch dir, and `diff` it against the committed
> receipt. Also recompute every sha256 the receipt lists. Verdict: REPLAY MATCH or MISMATCH with the diff.
> Then attack the instrument: for two legs of .../reports/round-54/accept-c.py (SET and RANGE), construct one
> further near-miss in the clone that the receipt does not already cover and report whether accept-c.py
> catches it (exit and failing legs). Write your code and fixtures ONLY under
> /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/ ... Python 3 stdlib only.

The receipt it replays is `reports/round-54/telemetry/criterion11-controls.txt`: header `tree
260c68d58c5d3c2b9a6463ca5c667b7e0fff5987`, five sha256 lines (accept-c.py, base-knowledge-files.txt,
sweep.py, check-source-access.py, criterion11-controls.py), the argv `python3 -B reports/round-54/accept-c.py`,
then 13 legs — GREEN exit 0 and twelve REDs, each exit 1 with exactly its declared legs failing
(RED-COUNT fails SET+SWEEP; RED-SET, RED-SET-EXT, RED-SWEEP, RED-FLOOR, RED-RANGE, RED-RANGE-NOROW,
RED-RANGE-DUP, RED-RANGE-SPAN, RED-STATUS, RED-USEDBY, RED-ACCESS each fail one leg).

`ExecDryRunCensus` (executor) — verbatim task:

> Re-verify the inherited declaration's before-state. In a sandbox clone (`git clone -q .../kotodama-shokunin
> /fast/scratch/hyaku/kotodama-r54-a2/ExecDryRunCensus/lane`, then `git checkout -q
> 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c`), run each command and paste command, output and exit:
> `python3 -B reports/round-54/accept-c.py` (compare with `expected_pre_landing_counting` in
> reports/round-54/claims.json), `python3 -B reports/round-54/dry-run.py` and its check mode (read the script
> for the flag), `python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json`,
> `python3 -B reports/round-54/claims-agree.py`, `python3 -B tools/check-source-access.py`,
> `python3 -B reports/round-28/readme/sweep.py`, and
> `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
> kotodama` (this one reads the real lane; it writes nothing). Verdict per command: MATCHES DECLARATION or
> DIFFERS (with the difference). Also run `git -C .../kotodama-shokunin diff --stat 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c`
> and `git -C .../kotodama-shokunin status --porcelain` and say which paths differ from the declaration commit.

`ReviewRoutedFixes` (reviewer) — verbatim task:

> Attack the prerequisite commit `d761ee825f94f7ae45e098ad551d7f735645ad22` (`git -C .../kotodama-shokunin show
> d761ee8...`). Against the round-53 closure's routed items (.../corpus/lessons/round-53-verifier-spotcheck.md:114-121
> and :169-183), check each changed line: gesture entry lines 68 (S201 page numbers: re-open the S201 proof PDF
> from its row URL and confirm which printed page carries the Northamptonshire/Campania data, the 'wide hand
> point' and the Kendon 208 quote), 133 (S221), 150 (S223) and 199 (S234: re-open and confirm the quote and its
> section), and speech-surrogates line 75 (S185 now cited; confirm S185's quote carries what the line says). Also
> check the SOURCES.md edits (S145 rejected as superseded, S185 mined, S225 access note) and the lessons README
> row. Verdict per item: FIXED, PARTLY or NOT FIXED, with verbatim evidence.

The other two attempt-2 additions, for the ledger: `ExecGateQuoteCheck` (writes `check-gate-quotes.py`, the
frontier-step fix for round-53's over-long joined Gate quotes), `ExecIntegrateRows` (writes
`integrate-rows.py --start 239`, mapping `NEW-<Seat>-<n>` draft ids to S-ids from S239 upward and emitting
`rows.md`, `map.tsv`, `gate.md`, `sentences.md`), and the scribe `ScribeSpotcheckRouting` (drafts
`## Spot-check intake (round-53 outside verifier)`).

---

## 6. Findings for the L1

1. **The wave died; the round did not.** All five pushed attempt-1 commits are intact and are attempt 2's
   inheritance. The claim, its instruments, its clause list and its pre-dispatch receipts need no
   re-decision. What was lost is only the 36 seats' work.
2. **Attempt 1 had no executor and no scribe seat** (26/2/4/4 over scout/connector/critic/reviewer). Attempt
   2 adds four executors and two scribes, and the three named above re-verify the inherited instruments
   against the committed receipts instead of trusting them. That is the right repair for a wave that died
   before it could measure anything.
3. **The assignment's "expected untracked" list is stale.** `5757c45` (15:34:44) committed the five
   attempt-1 wave artifacts as dead-wave evidence; the live untracked set is now `build-a2/` (seat reports and
   the a2 registry). If the lesson says "untracked", it must say so as of `5757c45`, not as of the
   assignment.
4. **`gen-build-spec.py` was overwritten in place** at 14:46 for attempt 2. The attempt-1 generator source
   is not in the lane; the attempt-1 spec, dispatch, payload and registry JSON are. Worth one line in the
   lesson's inherited-state section: the wave records were preserved, the tool that wrote them was not.
5. **Attempt 1's scratch is a trap for the integrator.** It contains 8082 files of plausible-looking
   downloads, and among them a bot-challenge page, a 403 body, and two HTML files named `.pdf`. Any S-row
   built from that scratch would be an unopened source (QUALITY criterion 10). Attempt 2's context already
   forbids it; the lesson should record why.
6. **The registry's `agentId` field is null for all 36 dead seats** and `updatedAt` equals the dispatch
   moment. That pair is a cheap, checkable signature of "dispatched, never started", and it is worth
   teaching: the absence of a report is confirmed by the tree, not asserted from the log.

## 7. Out of scope (not done, and why)

- I did not open any external source and did not draft any entry sentence: this seat's scope is the
  inherited state, and every source must be opened by the seat that cites it.
- I did not verify the correctness of `d761ee8`'s routed fixes, the criterion-11 receipt, or the declaration's
  before-state: those are `ReviewRoutedFixes`, `ExecControlsReplay` and `ExecDryRunCensus`'s work. I read
  their task texts only, to describe what attempt 2 re-verifies.
- I did not run `accept-c.py`, the census, or any counting command: those write or read state owned by the
  executors, and my assignment is a read-only state audit.
- I did not touch `/fast/scratch/hyaku/kotodama-r54-a2/` or any attempt-2 seat's report; I wrote only this
  file.

## 8. Artifact paths

- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScribeInheritedState.md`
- Attempt-1 wave records (now tracked): `.ufo/waves/round-54/build-spec.json`,
  `.ufo/waves/round-54/build-dispatch.json`, `.ufo/waves/round-54/build-sent-payload.json`,
  `.ufo/waves/round-54/build/swarm-registry.json`
- Attempt-2 wave records: `.ufo/waves/round-54/build-a2-spec.json`, `.ufo/waves/round-54/build-a2-dispatch.json`,
  `.ufo/waves/round-54/build-a2-sent-payload.json`, `.ufo/waves/round-54/build-a2/swarm-registry.json`
- Generator: `.ufo/waves/round-54/gen-build-spec.py`
- Pre-dispatch critic reports (landed in attempt 1): `.ufo/waves/round-54/predispatch/CriticClauseList.md`,
  `.ufo/waves/round-54/predispatch/CriticControlsReplay.md`
- Declaration and receipts: `reports/round-54/claims.json`,
  `reports/round-54/telemetry/criterion11-controls.txt`, `reports/round-54/telemetry/declaration-dry-run.txt`,
  `reports/round-54/telemetry/census-start.txt`, `reports/round-54/telemetry/census-start-a2.txt`
- Attempt-1 scratch (counted, not evidence): `/fast/scratch/hyaku/kotodama-r54/`
- Attempt-2 scratch: `/fast/scratch/hyaku/kotodama-r54-a2/`
- Watchdog (read-only): `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log` lines 721, 732, 733

## 9. Commands run (trimmed output)

```
grep -n "kotodama round=54" /home/vgpnk/Projects/shokunin/.ufo/watchdog.log
721:2026-10-22T14:09:03-03:00 launch kotodama round=54 pgid=4046130 driver=hyaku-inline attempt=1
732:2026-10-22T14:30:09-03:00 lane-dead-no-report kotodama round=54; retry same round (hyaku-inline attempt=1: omp process restart at 17:26Z; no landed report; fresh successor inherits work)
733:2026-10-22T14:30:11-03:00 launch kotodama round=54 pgid=1003675 driver=hyaku-inline attempt=2

git -C .../kotodama-shokunin log --format='%h %ad %s' --date=iso e0bfb13e..7fa37fbb...
   (five commits, table in §2)

git -C .../kotodama-shokunin status --porcelain
?? .ufo/waves/round-54/build-a2/

git -C .../kotodama-shokunin log --format='%h %ad %s' --date=iso -8
5757c45 2026-10-22 15:34:44 -0300 round-54: attempt-1 dead build-wave dispatch records (36 seats, omp restart 17:26Z, no reports) committed as evidence; attempt-2 build-a2 spec (42 seats: +4 executors, +2 scribes), generator, dispatch and sent payload; census at attempt-2 start

python3 (registry audit of build/swarm-registry.json vs build-a2/swarm-registry.json)
A1 members=36 createdAt=2026-10-22T17:19:54.138Z updatedAt=2026-10-22T17:22:52.217Z reportDir=.ufo/waves/round-54/build
   roles: {'scout': 26, 'connector': 2, 'critic': 4, 'reviewer': 4}  axes: {('coverage',): 28, ('coverage','calibration'): 8}
   non-null agentId: []
A2 members=42 createdAt=2026-10-22T17:46:52.913Z updatedAt=2026-10-22T17:46:52.913Z reportDir=.ufo/waves/round-54/build-a2
   roles: {'scout': 26, 'connector': 2, 'critic': 4, 'reviewer': 4, 'executor': 4, 'scribe': 2}
   axes: {('coverage',): 28, ('coverage','calibration'): 14}
A1-only seats: none; A2-only: ExecControlsReplay, ExecDryRunCensus, ExecGateQuoteCheck, ExecIntegrateRows, ScribeInheritedState, ScribeSpotcheckRouting

python3 (prompt diff, attempt 1 vs attempt 2 payloads, Report trailer stripped)
seats whose prompt is identical after removing the Report trailer: 35 of 36
differing: ['CriticMistakeMining']   (scratch path kotodama-r54 -> kotodama-r54-a2, plus the report path)

python3 (context diff between the two waves' shared contexts)
3 replaced lines: the attempt-1/attempt-2 sentence with the restart cause and the "scratch is NOT evidence"
rule; the L1 name KotodamaR54 -> KotodamaR54a2 and "maps" -> "maps, tools and attacks";
the leaf-seat rule plus "(an executor may spawn at most one read-only labrat probe)" and
"executors may also write under their scratch dir".

find /fast/scratch/hyaku/kotodama-r54/ -mindepth 1 -maxdepth 1 -type d | per-dir find | wc -l
  (30 seat dirs, 8082 files; CriticClauseList 3903, CriticControlsReplay 3907, censusroot 3892, test 5376 excluded as
   census/clone trees; 8 registry seats with no directory; ScoutCham empty)

find /fast/scratch/hyaku/kotodama-r54/ -type f | wc -l
17350

jj --ignore-working-copy status   (read-only, in the lane)
The working copy has no changes.
Working copy  (@) : qntnxuoz 8ee0468b (empty) (no description set)
Parent commit (@-): mnsqqouq 5757c451 main | round-54: attempt-1 dead build-wave dispatch records ...
```

Tooling: none installed, none upgraded. The host's pacman transactions remain paused; no install was
needed for a read-only state audit.
