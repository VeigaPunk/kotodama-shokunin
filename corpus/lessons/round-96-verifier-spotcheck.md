author: hyaku closure (non-author integrator, @m_zfl)

# kotodama round 96 — non-author verifier spot-check

Base `0539276c0e329743200b60e98bf289c540f78864` → lane HEAD `16c4759241cbe8687394657feb1d08ad4eff659f` (branch `main`).
Report `.ufo/reports/round-96/kotodama.md` (fleet commit `f9826304dbfbfa48ced8212432f94b034ee9426a`).
Driver digest (copied from `.ufo/watchdog.log`):
`2026-11-05T16:52:10-03:00 launch kotodama round=96 pgid=4074531 driver=hyaku-inline attempt=1` /
`2026-11-05T19:14:44-03:00 complete kotodama round=96; hyaku-inline attempt=1`.
All measurements below were run by this verifier on 2026-11-05 over committed bytes; no lane gate was executed.

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an %H' -- .ufo/reports/round-96/kotodama.md` | `kotodama-shokunin f9826304…` (2026-11-05 19:14:16 -03) | pass |
| SHONEN heading, one line per box | `grep -c '^## SHONEN'` → 1; SHONEN.md has 4 boxes; report has 4 `[~]` lines | 4/4 | pass |
| cited commits exist and are ancestors of `main` | `git cat-file -t` + `git merge-base --is-ancestor <h> main` for `0539276c`, `deca7e6f`, `063f70c9`, `66d2e915`, `16c47592` | all `commit`, all ancestors | pass |
| lane pushed, no leftovers | `jj-lane.sh state …` | `branch=main local=remote=16c47592… ahead=0 behind=0 tracked=0 untracked=0`; `git status --porcelain` empty | pass |
| prompt carries template contract | `.ufo/prompts/kotodama-round-96.md` (886 lines, commit `13c89fb0`) | §1 MISSION/AXES, §2 claims, §2b frontier, §3 L2 floor, §4 report contract (SHONEN), §5 commit/L0, §6 hyaku addendum | pass |
| marker? | — | real report with landed commits | not a marker |

Conformance notes (status-neutral): the dispatch-prompt commit `13c89fb0` is authored under the lane identity
(`kotodama-shokunin`) though it is orchestrator dispatch evidence — attribution note only. SCORECARD's round-96 row cites
`reports/round-96/controls/battery96-control-v6.txt`, which exists (`BATTERY-SUMMARY survivors=9 … refused=15`).

## 2. Claims

### Claim O — operability (grader v6 → v8) — evidence-verified (lane gate) + re-measured sha/freeze

- Tool sha: `git show 16c47592:tools/check-advance-evidence.py | sha256sum` → `f29ab0139b4590fa…c9` (≠ base `f7981ba2…ec`). Re-measured.
- Frozen counter integrity: `git diff deca7e6f 16c47592 -- reports/round-96/predispatch.py` → empty; `claims.json` changed only by
  `063f70c9` (pre-data before-prediction correction); `git diff 063f70c9 16c47592 -- claims.json predispatch.py` → 0 lines. Re-measured.
- Battery driver pin: `sha256(battery96.py)` = `9f80f594…c21` = `reports/round-96/controls/battery96.sha256`. Re-measured.
- Committed evidence (evidence-verified, not executed): `reports/round-96/predispatch-lands.txt` → O0 PASS, O1 `147/147 floor=144`,
  O2 `survivors=0 unnamed=0 refused=24`, O3 `111/111 killed, 0 survived, 0 broken-pattern`, O4 `34 … byte-identical`,
  `PREDISPATCH-96: PASS legs=12/12`, measured on tool `f29ab013…` = the landed bytes. Before: `predispatch-base.txt` FAIL 3/12;
  control `control-v6.txt` survivors=9 refused=15 (matches report).
- v7 history: `git log 0539276c..16c47592 -- tools/check-advance-evidence.py` → only `66d2e915`, whose parent tool sha is v6.
  v7 (`2e28a289…`) never entered lane history; the "lands measurement" is therefore v8 by construction. Ruling on the
  lane's question: **the v8 repair counts as the claim's landing** — the frozen predicate and its counter were unchanged,
  the v7 failure (109/112) is kept on the record.
- Retired mutant: `diff mutants96.py.pre-retire mutants96.py` → exactly one line removed (`id-lookalike-refuse-off`);
  its target (`has_nonascii_letter`) occurs 0 times in v8 (`grep -c`), and the live ID-NONASCII branch keeps its own mutant
  `cyr-idnonascii-off` (mutants96.py line 129). Retirement is justified, disclosed, and total 111 ≥ floor 95.
  Defect (routed): the mutation driver was not sha-pinned at freeze (only battery96 was), so it was editable after its first
  measurement; freeze the mutation driver's sha next time.
- Spot read of the diff: the ten round-96 selftest pins + CYR1/BR1/DASH1 account for 134 → 147. Cosmetic: v8 docstrings still
  say "Round-96 v7", and `def _refuse_disguised` now has a blank line before its docstring.
- Verdict: **operability improved** (frozen predicate met on landed bytes).

### Claim C — coverage (oath, blessing and curse formulae) — re-measured

- Entry: `git show 0539276c:<entry>` → path absent; at `16c47592` `wc -c` → 30143, `grep -c '^## '` → 11.
- Registry: `grep -c -E '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` base 898 → 908; highest S974 → S984;
  `git diff … -- corpus/SOURCES.md` removed lines 0, added 10.
- Citations: each of S975–S984 occurs 3–4 times in the entry (`grep -c`); `reports/round-96/evidence/` holds 20 capture files + manifest.
- Census: re-run below, rc 0. Index: evidence-verified (`CORPUS-INDEX: OK files=268 rows=268 findings=0` in predispatch-lands).
- Ground-novelty caveat (defect, routed): the "zero owned knowledge file at base" before-state rests on a filename sweep
  (`ScoutSurface96/surface.md` §1). At base, `myth-symbol/binding-speech-complex.md` §4 already teaches the oath's
  "Formula anatomy" as invocation / assertion / self-imprecation / uptake (lines 99–108), the same four slots as the new
  entry's §2 title. The new entry's blessing and curse formula grammar, witness invocation, sanction clause, register
  allocation and the ten captured tier-A/B sources are new; CriticC96's 0.29% 8-gram overlap is a wording measure, not a
  topic one. The scout's statement that binding-speech owns "not the linguistic formula grammar" is false for the oath.
- Verdict: **coverage improved** (predicate met; net new sourced surface), with the duplicate-authority defect routed.

### Owned axes not claimed

`git diff 0539276c 16c47592 -- SCORECARD.md`: appends a round-96 axes section + round-97 plan only; no prior row edited.
adjacency unchanged (no sibling-lane file touched; `git diff --stat -- corpus/knowledge` lists only the new entry);
depth unchanged; freshness unchanged (L0-paused); calibration unchanged (no calibration claim; criterion 38 counted
under discernment). No axis harmed.

| axis | verdict |
|---|---|
| operability | improved |
| coverage | improved |
| adjacency | unchanged |
| depth | unchanged |
| freshness | unchanged |
| calibration | unchanged |

## 3. Discernment spot-check (`corpus/lessons/round-96.md` `## Gate`)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S983 Aston 1905 ch. 12 (Wikisource) | admit (tier A) | `curl -sL --max-time 30` → HTTP 200, 303938 B; tag-stripped text count of “the recital of a norito or formula—not a prayer, as it is sometimes called” = 1 (14 words) | agree | quote located once, ≤25 words; primary 1905 text supports the blessing-formula/register slot |
| S978 Tuomi 2013 review (journal.fi PDF) | admit (tier B) | HTTP 200, 256566 B, PDF 7 pp; `pdftotext` count of “curse-enhanced oaths or vows lie behind the notion of the geis” = 1 | agree | located; a review is correctly held at tier B |
| C4 Ó Murchú 1992 (Persée) | reject (dropped: fresh 404) | 3 attempts: rc-timeout (000), 404 (27171 B), 404 (29069 B) | agree | non-transient 404 on retry; dropping rather than falling back to the scout's earlier capture is correct. Note: the registry seat's record (`reverification.json`) carries 1 attempt; criterion 38 does not require retries for a non-transient status, so not a defect |
| R26 Sefaria Numbers 6:24-26 | reject (app shell) | HTTP 200, 118737 B HTML; script-stripped text = 578 chars, no blessing wording (“make his face” count 0) | agree | served body is the shell, not the text, as recorded |

Registry row re-opened: S983 (`corpus/SOURCES.md`), quote 14 words ≤ 25, located (above).
Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok …/corpus/SOURCES.md`, rc 0
(pre-existing W04 duplicate-url and W01 tier-C warnings only; none on S975–S984).

Not sampled: R27 (Manusmriti 8.109 rejected as a "registry duplicate of S838"): S838 is a different verse page (2.35,
tonsure) of the same edition; whether one edition = one row is a lane registry rule to state explicitly (routed).

## 4. Trend verdicts

- **expansion: improved** — new entry + 10 mined tier A/B rows, census rc 0; partial overlap with binding-speech §4 routed, not harming.
- **quality: unchanged** — no existing entry re-verified, deepened or superseded (`git diff --stat -- corpus/knowledge` → new file only).
- **discernment: improved** — non-author spot-check agrees on 2 admits and 2 rejects; the round-95 Thrênoi access reject was
  re-opened, mined (R96-M1) and produced grounded criterion 38 citing that lesson.

## 5. Routed defects (lane fixes next round)

1. Claim-C before-state: replace the filename-only zero-owner sweep with a content sweep; reconcile oath formula-anatomy
   authority between `linguistics/oath-blessing-curse-formulae.md` §2 and `myth-symbol/binding-speech-complex.md` §4 (one owner, one pointer).
2. Freeze the mutation driver's sha alongside the battery pin; a driver editable after first measurement is an unpinned instrument.
3. CriticO96's seven v7 survivors (CR1, US1, OGH1, IS1, NUL1, CM1, CMW2) were not re-run on v8 — measure them on v8.
4. Thrênoi to Moirológia row nominated, not written — write it (or record why not) in round 97.
5. State the registry rule behind R27 (one row per edition vs per cited passage).
6. Cosmetic: v8 docstrings say "v7"; blank line between `def _refuse_disguised` and its docstring.
7. Dead seat ReviewerC96 (no verdict, not substituted) — the round's reviewer coverage for claim C rests on CriticC96 and this closure.

SHONEN: all four boxes remain `[~]`; boxes 2–4 look checkable by a non-author from committed pointers (operator-owned promotion; not written here).
