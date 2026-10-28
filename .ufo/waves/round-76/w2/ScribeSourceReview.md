# ScribeSourceReview — round 76 wave 2 (lesson sections + source Gate)

Seat: `ScribeSourceReview`. Date: 2026-10-27. Mode: read-only falsification; no edits to
claims, counters, lane files or reports; no builds/tests/linters/formatters.

Revisions reviewed (all resolve in this lane repo, see §Provenance):

- base `98c486bdb4650ba5b8e651d332910e8ee60ad121`
- frozen C/Ca configuration `df0f0309d61e5485bb17035d3f8791b1e6a11d40`
- Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c`
- C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a` (**final lesson**; `corpus/lessons/round-76.md` is
  absent at base, `df0f030` and `a43ed80`; it is added whole at `722e69f`, 93 lines)

Every read below is from committed trees (`git show <rev>:<path>`), not the mutable worktree.
The reviewed files are byte-identical in the worktree to `722e69f`
(`git status --porcelain corpus/lessons/round-76.md corpus/SOURCES.md corpus/knowledge` is empty);
the worktree *is* dirty elsewhere (`M SCORECARD.md`, `M .ufo/waves/round-76/w1/stage/ExecAdaptC/claim-C.json`,
untracked `w2/`), which is why SCORECARD/LOG reads are pinned to `722e69f`.

## Verdict

**NOT CONFORMANT at `722e69f` against `CORPUS.md`.**

- Source-Gate completeness for the three admitted rows **conforms**: each new row's URL, access
  date, capped quote and locator are recorded, and each was re-derived.
- The Gate is **missing the required spot-check result** (F1, blocking).
- The lesson's required citation set is **incomplete**: no `LOG.md` round and no round report
  (F2, major).
- The Gate's **candidate limb does not identify the adopted candidate** (F3, major).
- Four wording/form defects (F4–F8, minor); none of them changes a number.

## Gate element matrix (`CORPUS.md:19-20`, `LEARNING.md:68-71`)

| required element | present at `722e69f`? | evidence |
|---|---|---|
| candidates | partial — triage counts and refusal families, no candidate identity (F3) | `round-76.md:21`, `:27-29` |
| admitted | yes — S894/S895/S896 with tiers | `round-76.md:11-13` |
| rejected with reasons | yes — 3 rows + 9 families, each with a flip condition | `round-76.md:16-19`, `:23-35` |
| spot-check result | **no** | `round-76.md:5-35`; grep below |
| `## Mistakes` (mined this round) | yes | `round-76.md:79-85` |

## Findings

### F1 — BLOCKING: no spot-check result in the Gate

- Requirement: `CORPUS.md:19-20` ("each `lessons/round-<N>.md` carries a `## Gate` section
  (candidates, admitted, rejected with reasons, **spot-check result**)"), `CORPUS.md:113-115`
  (SOURCES rule 1: "Non-author verification re-opens a sample"), `LEARNING.md:41-46` (a non-author
  spot-checks a sample, **at least one admit and one reject**, and records `agree`/`disagree`
  with a reason **in the round's lesson**), `LEARNING.md:68-71` (Gate includes "the spot-check result").
- Observed at `722e69f`:
  - `git show 722e69f:corpus/lessons/round-76.md | grep -niE 'spot|agree|disagree|non-author'`
    → **0 hits** (whole 93-line lesson).
  - `git ls-tree -r --name-only 722e69f corpus/lessons | grep round-76` → only
    `corpus/lessons/round-76.md`. The lane carries 27 `corpus/lessons/round-NN-verifier-spotcheck.md`
    files, one for every round 49–75 with no gaps; round 76 has no counterpart, so the result is not
    parked in a companion file the lesson could be read as citing.
  - No wave-1 seat records a gate spot-check either: grepping `spot[- ]?check|non-author|agree|disagree`
    over the 67 w1 markdown files at `722e69f` returns only planning statements —
    `.ufo/waves/round-76/w1/RevQualityFit.md:263` ("discernment needs the outside spot-check"),
    `ConnectorFrontier.md:76,:81` (dispute framings), `CritLedgerDesign.md:40`,
    `ExecAdaptCa.md:40` (round-75 spotcheck), `RevengerMistakes.md:159`, `ScoutLedgerB.md:23`.
  - The frozen claim does not supply it: `grep -ci 'spot'` over `reports/round-76/claims.json`
    → 0; `reports/round-76/ledger.json` has `fleet_report: null`.
- Why it matters: the Gate is the only carrier of the round's rejection taste; an unrecorded
  spot-check leaves `discernment` unfired under `LEARNING.md:35` regardless of the gate's quality.
- Clear condition: one non-author spot-check of this Gate covering ≥1 admit (S894/S895/S896 or
  candidate a) and ≥1 reject (showGb alias, duplicate archive table, or drafter interpretation),
  with `agree`/`disagree` and a reason, **in the lesson** (or a cited, committed
  `round-76-verifier-spotcheck.md`).

### F2 — MAJOR: lesson does not cite a LOG.md round or a report; neither exists at `722e69f`

- Requirement: `CORPUS.md:25` — "`lessons/` entries cite the round and the evidence (LOG.md round,
  commit, report)."
- Observed:
  - commit limb OK: `round-76.md:3` cites base `98c486bdb4650ba5b8e651d332910e8ee60ad121`.
  - **LOG limb absent**: `git show 722e69f:LOG.md | grep -ci 'round-76'` → **0**; the last
    heading is `LOG.md:4320` `## Round 75 (2026-10-27, hyaku run 10, …)`, and the file ends on
    the round-75 line "**Tool installs:** none. **Stale-lane:** none." The lesson never names
    `LOG.md` (`grep -c 'LOG.md'` → 0).
  - **report limb absent**: `round-76.md:93` says the post-landing census "appears in the round
    report", but at `722e69f` the lane's `reports/round-76/` holds only `accept-c.py`,
    `accept-ca.py`, `claims.json`, `evidence/S894-S896.txt`, `fixtures/*`, `ledger.json`,
    `telemetry/*` — no report markdown; and `.ufo/reports/round-76/` holds only `audio.md`,
    `game-dev-2d.md`, `game-dev-3d.md`, `kotoba.md` (no `kotodama.md`). `reports/round-76/ledger.json`
    `fleet_report` is `null`.
- Caveat for the canonical judge: a LOG entry and fleet report are normally written at round
  close, i.e. after this landing. At the cited revision the corpus rule is unmet; this may be a
  sequencing artifact rather than an omission, but it is not satisfied on the committed bytes.
- Clear condition: a `LOG.md` round-76 section plus a report (or a lesson sentence citing the
  report path that exists); the census pointer at `:93` must name a real file.

### F3 — MAJOR: Gate's "candidates" limb has no candidate identity, and never names the adopted file

- Requirement: `CORPUS.md:19-20` (Gate: "candidates, admitted, rejected with reasons").
- Observed:
  - `round-76.md:21` gives counts only: "Triage of the 40 staged knowledge files: **1 adopted /
    9 path-present at base / 30 refused**"; candidate a is referenced ("Candidate a's staged
    citations to campaign ids were re-pointed…") but is never identified by path.
  - `git show 722e69f:corpus/lessons/round-76.md | grep -c 'amend-2026-10-24'` → **0**: the
    adopted candidate's file is absent from the lesson.
  - The four candidates exist only in the frozen claim: `reports/round-76/claims.json`
    `claims[0].candidates` — a = `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md`
    (admitted true); b = `…-r10.md`; c = `era-periodization-models.amend-2026-10-23b.md`;
    d = `…amend-2026-10-23c.md`.
  - The Gate's admitted table (`:11-13`) admits **source rows**, not candidate a, so a reader
    cannot map "1 adopted" to the emitted entry from the lesson alone. (The entry path is
    recoverable only indirectly from `corpus/SOURCES.md:849-851` `used-by`.)
- Clear condition: name candidate a and the emitted entry path in the Gate, or cite the frozen
  `candidates` block.

### F4 — MINOR: Collision guard attributes post-adoption overlap mappings to "the collision set" (stale wording)

- `round-76.md:69` ends: "The collision set was resolved by document, not arithmetic: staged
  S908/S935→S894; S932/S938→S895; S937→S896."
- The committed 35-id collision artifact is **S859–S893**, nothing else:
  `.ufo/waves/round-76/assimilation/collisions` (35 lines; `grep -cx` for each of S908, S935,
  S932, S938, S937 → **0** for all five).
- Those five ids are the **post-adoption numeric-overlap** records, not the 35-collision set:
  `.ufo/waves/round-76/assimilation/id-renumber-map.json` `post_adoption_numeric_overlap[0..2]`
  (`planned_lane_id` S894→`["S908","S935"]`, S895→`["S932","S938"]`, S896→`["S937"]`;
  `staged_row_with_same_number` S894/S895/S896). `staged-ids` does contain S894/S895/S896
  (`grep -cx` = 1 each), which is what makes them overlaps after adoption.
- The mapping itself is true; only its attribution is wrong. The 35-collision resolution is
  documented separately in `.ufo/waves/round-76/w1/ScoutIdMap.md:86-95` and the map's
  `numeric_collisions_at_base`.
- Clear condition: call the five-id mapping "post-adoption numeric overlap"; keep the 35-row
  collision statement separate.

### F5 — MINOR: "Census after landing is required by CORPUS.md" is not what CORPUS.md says

- `round-76.md:93`: "Census after landing is required by CORPUS.md and appears in the round report."
- `CORPUS.md:131-159` (`### Census — run from the lane root …`) supplies the seven manual
  commands and the maintained-parser note; `grep -niE 'after landing|post-landing' CORPUS.md`
  → no hit (the only "landing" token is the mistake-class word at `CORPUS.md:175`). No sentence
  in `CORPUS.md` imposes a post-landing census.
- The substantive census is present and sound (`round-76.md:77`, receipts at
  `reports/round-76/telemetry/census-{start,end}.txt`), so this is attribution wording only.
- Clear condition: attribute the after-landing practice to the protocol/LOG convention, not to
  `CORPUS.md`.

### F6 — MINOR: `## Mistakes` rows use non-vocabulary classes and a non-criterion `captured-by`

- Requirement: `CORPUS.md:171-176` (one row per mistake: class · evidence pointer · captured-by =
  the `QUALITY.md` criterion or protocol rule that should have caught it, or `none` · fix;
  "Classes come from the `mistakes.md` §5 vocabulary (`vacuous`, `survivor`, `stale-premise`,
  `reference-drift`, `number-drift`, `scope`, `attribution`, `landing`, `provider`)").
- Observed in `round-76.md:83-85`:
  - R76-M1 — `attribution` ✓; captured-by `QUALITY criterion 29 (new)` ✓ (`corpus/QUALITY.md:199`).
  - R76-M2 — class `counter/claim surface mismatch` is not in the vocabulary; captured-by
    `frozen LEGCOUNT/selftest` names an instrument, not a criterion/rule/`none` (nearest
    candidates are `QUALITY.md:77` (23) and `:125` (26)).
  - R76-M3 — class `source-census parser treated…` is not in the vocabulary; captured-by
    `none (routed)` ✓.
- Evidence pointers and red-before artifacts do exist at `722e69f`
  (`.ufo/waves/round-76/w1/RevengerMistakes.md` §2 + `stage/RevengerMistakes/recurrence.txt`;
  `stage/L1/freeze-control-legcount-redbefore.txt`; `reports/round-76/telemetry/controls-c.txt`),
  so only the class/captured-by cells are defective.
- Clear condition: relabel M2/M3 with a §5 class and name a criterion or `none` for M2.

### F7 — MINOR: three counted blocks lack the `<number> — <command> <date>` form

- Requirement: `CORPUS.md:34-38` ("A count carries its command … `<number> — <command> <date>`").
- `round-76.md:21` (1 adopted / 9 path-present / 30 refused; 27-split ×11/×9/×1/×3/×1/×2),
  `:39` (21 rows; PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4), `:69` (registry 817, staged 132,
  collisions 35) state correct numbers without a command/date. The census block (`:77`) and the
  Mistakes pointers do carry commands.
- I re-derived every one of them from committed bytes — they are **true**, so this is form, not
  value drift:
  - rows/tiers/status: base 817 / A491 B310 C16 / mined722 queued58 rejected37; landing 820 /
    A493 B311 C16 / mined725 queued58 rejected37 (manual awk over `git show <rev>:corpus/SOURCES.md`,
    malformed-NF = 0 both sides; matches `reports/round-76/telemetry/census-{start,end}.txt`).
  - staged package: `find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge -type f | wc -l`
    = 40; exact-path-present at base = 9 (`ls-tree -r 98c486b corpus/knowledge` vs the 40 paths);
    frozen claim counts `{"adopted":1,"path_present":9,"refused":30,"total_staged_files":40}`.
  - quarantine: `reports/round-71/telemetry/quarantine-verdicts.md` at `722e69f` lists 21 ids with
    10 PRESENT / 7 REFUSED / 4 UNVERIFIABLE — identical per-row verdicts to `round-76.md:43-63`.
  - id lists: `reg-ids` 817 lines, `staged-ids` 132, `collisions` 35; sha256
    `97eef07a…a7`, `bab11d7d…ad`, `be203dd8…47` — all three equal the pins at `round-76.md:69`
    exactly.
- Clear condition: append the command and date to each of the three blocks, as the census block does.

### F8 — MINOR: negative claims without a sweep

- Requirement: `CORPUS.md:39-41` ("A negative claim carries its sweep") and `CORPUS.md:128`.
- Unswept negatives at `722e69f`:
  - `round-76.md:39` — "No current candidate or new lane row is a slice document; no quarantine
    verdict was upgraded or retired." (no command; the slice/verdict comparison is real —
    `quarantine-verdicts.md` rows match — but unpublished in the lesson).
  - `round-76.md:93` — "No `considerthese/` directory exists in this lane." (I confirmed the
    directory is absent with `ls considerthese` → "No such file or directory", but the lesson
    carries no sweep).
  - `round-76.md:93` — "No pre-existing row status/recheck/used-by changed." (true:
    `git diff 98c486b 722e69f -- corpus/SOURCES.md` = 8 insertions, 0 deletions; no command given.)
- `round-76.md:73` "no escaped pipes" is verified (`grep -c '\|'` over the three rows = 0) but
  also uncited; counted here as the same class of omission.
- Clear condition: cite the producing command beside each negative, as SOURCES rule 1/5 already
  requires for the search log.

## Verified conformant (re-derived; no finding)

| check | result | evidence |
|---|---|---|
| new rows carry URL, access date, ≤25-word/≤80-char quote, locator | yes for S894/S895/S896 | `round-76.md:9-13`; quotes 18/19/21 chars, 4/2/1 whitespace tokens; each quote present verbatim in its evidence file (`quote-found-verbatim: yes`) |
| evidence windows committed, with digest + request metadata + quote + one stored window | yes | `reports/round-76/evidence/S894.txt` … `S896.txt` (37 lines each; 1 `--- window ---`, 1 `quote:` line; `access-date: 2026-10-27`) |
| tiers A/A/B match the registry | yes | `corpus/SOURCES.md:849-851` tier cells A/A/B; status `mined`; `opened 2026-10-27`; `recheck 180d`; NF=13 (11 cells); no escaped pipes; `used-by` = the one amendment |
| rejected rows/families carry reason + flip; families sum to 30 and triage to 40 | yes | `round-76.md:16-35`; family sum `1+1+1+9+11+1+3+1+2 = 30`; matches `claims.json` `rejects.counts` |
| in-place SOURCES changes logged old→new | nothing changed | `git diff 98c486b 722e69f -- corpus/SOURCES.md` adds 3 rows + 1 Paths bullet (`:854`) + 1 search-log paragraph (`:902`), 0 deletions |
| search log has question, where searched, counts, exclusion reasons, stop rationale | yes | `corpus/SOURCES.md:902` (full line ends "…and overclaimed passages; no second candidate adds independent uncovered calendar ground.") |
| "seven manual table-shape and histogram checks … in validate-receipt.txt" | accurate | `.ufo/waves/round-76/assimilation/validate-receipt.txt` contains 2 CLI runs + 7 `MANUAL` blocks (rows, malformed-NF, tier, status, duplicate-ids, enum/inflation, missing-mined-usedby), all exit=0 |
| census start/end receipts exit 0; end has no E-code | yes | `reports/round-76/telemetry/census-{start,end}.txt`; end shows only inherited W04 duplicate-URL and W01 tier warnings |
| frozen counter/config bytes survived the landings | yes | `git diff --stat df0f030 722e69f -- reports/round-76/{claims.json,accept-c.py,accept-ca.py}` → empty |
| guard fixtures (1-space found / 4-space not) | yes | `assimilation/guard-proof/planted-{1,4}space-proof.txt`; 1-space output includes S897 exit=0, 4-space "(no rows)" exit=1 |
| entry provenance trio + index + criterion | yes | `corpus/knowledge/…amend-2026-10-24.md:3-7` (`source:` ×3, `verified-at:`, `recheck:`); `corpus/README.md:416` index row; `corpus/QUALITY.md:199-201` criterion 29 |
| "C and Ca are not admitted" vs "admitted (tier A)" | not a contradiction | `round-76.md:89` refuses the **claims**; `:11-13` admits **source rows** |

## Out of scope / adjacent observations (reported, not graded by this seat)

1. **No round-76 trend verdicts.** `LEARNING.md:26-37` requires one verdict per trend each round.
   At `722e69f`, the last axis rows in `SCORECARD.md` are round 75 (`:1505-1506`); round 76 appears
   only as "## Corrections — round 76" (`:1511`). Possibly a round-close artifact, like F2.
2. **Refused sources are not registered as `rejected` rows.** `LEARNING.md:11-12` says opened and
   rejected sources are curated in `corpus/SOURCES.md`; the three refused candidates live only in
   the Gate (`round-76.md:16-19`, `:27-29`) and no `rejected` row was appended (`corpus/SOURCES.md` diff).
   Two are aliases/duplicates of an adopted document and one is tier C, so "no row" may be the
   right call — flagged for the canonical judge, not asserted as a defect.
3. **The Gate's `verdict` cells for admitted rows** combine tier and re-open condition
   ("admitted (tier A); re-open live and capture; …"). This is richer than required and reads
   consistently with `recheck 180d`; no defect.
4. **`round-76.md:39`** carries three slice ids rendered with a trailing backtick (S807`/S812`/S835`)
   and says so; the table matches the committed register, which itself carries the artifact. No defect.

## Provenance and tooling

- The assignment names `/home/vgpnk/Projects/shokuknow` as the read-only source repo, but **none of
  the four cited revisions exists there** (`git -C /home/vgpnk/Projects/shokuknow cat-file -t <rev>`
  → "could not get object info" for all four). All four resolve in
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, and the chain is
  `98c486b → df0f030 → a43ed80 → 722e69f` (`git merge-base --is-ancestor` each step). The
  `shokuknow` tree was used read-only only for what the lesson itself cites:
  `merge/kotodama/knowledge/` (40 staged files) and
  `.ufo/waves/corpus-expansion-1/absent-defect-register.md` (exists, 83,621 B).
- Tool installs/upgrades: **none**; no pacman transaction (paused per assignment); nothing added to
  any PATH directory. Commands used were git plumbing and read-only text/awk/grep/sha256sum against
  committed blobs. No builds, tests, linters or formatters were run; the round's counters were not
  re-executed (their receipts were read, not re-run).
- Scratch: no `/fast/scratch/hyaku/kotodama-r76/<seat>` directory was created; four derived lists
  written to `/tmp` were removed before this report. `~/.omp/agent/RULES.md` was read before any
  tool decision.
- Touched surfaces: this report only
  (`.ufo/waves/round-76/w2/ScribeSourceReview.md`). No claim, counter, lane file, LOG, SCORECARD,
  MANIFEST or source byte was modified.

## Artifact index

- Lesson: `722e69f:corpus/lessons/round-76.md` (Gate `:5-35`, refusal families `:23-35`,
  quarantine `:37-65`, collision guard `:67-69`, normalization `:71-73`, census `:75-77`,
  mistakes `:79-85`, routed `:87-89`, sources/frontier `:91-93`).
- Contract: `/home/vgpnk/Projects/shokunin/CORPUS.md` (`:18-20`, `:25`, `:34-41`, `:113-115`,
  `:128`, `:131-159`, `:171-181`); `/home/vgpnk/Projects/shokunin/LEARNING.md` (`:11-13`,
  `:29-36`, `:41-46`, `:68-71`).
- Source rows: `722e69f:corpus/SOURCES.md:849-851`, Paths `:854`, search log `:902`.
- Evidence: `722e69f:reports/round-76/evidence/S894.txt` … `S896.txt`.
- Guard/collision: `722e69f:.ufo/waves/round-76/assimilation/{collisions,reg-ids,staged-ids,id-renumber-map.json,guard-proof/*}`;
  `:w1/ScoutIdMap.md:86-95`.
- Quarantine: `722e69f:reports/round-71/telemetry/quarantine-verdicts.md`.
- Census/validation: `722e69f:reports/round-76/telemetry/census-{start,end}.txt`;
  `722e69f:.ufo/waves/round-76/assimilation/validate-receipt.txt`.
- Frozen inputs: `722e69f:reports/round-76/{claims.json,ledger.json,accept-c.py,accept-ca.py}`
  (byte-identical to `df0f030`).
- Entry/index/criterion: `722e69f:corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md:1-16`;
  `722e69f:corpus/README.md:416`; `722e69f:corpus/QUALITY.md:199-201`.
- Absences: `grep -ci 'round-76' LOG.md@722e69f` = 0 (last heading `LOG.md:4320` = round 75);
  `.ufo/reports/round-76/` has no `kotodama.md`; `corpus/lessons/` has no
  `round-76-verifier-spotcheck.md`.
