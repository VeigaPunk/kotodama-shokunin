# RevClaimCa — attack on claim Ca dispositions (round 65, hyaku run 5)

seat: RevClaimCa (independent leaf, attack)
lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin
base: 17c32302c6845c8f164b985a8cb312d3181c8788 (verified `git rev-parse HEAD` = base; `git rev-parse main` = base)
date: 2026-10-24

## 0. Requested measurement (recorded)

```
$ git rev-parse 8bab271c691c6b1006da95316a24ae1958ec01e2^{tree}
0ec0e50ea828ca6d8e20298f72af49414692e9e4
```

Cross-check: `reports/round-64/telemetry/final-measures-ca.txt` at `17c32302` and at `8bab271c`
are byte-identical (`sha256 c69d173954076a6aab98ceddb179c9e97ec994830b110e1fa89b5e06e5317cb6` both),
so a genuine R1 re-stamp has a well-defined preservation target; the frozen R1 leg never compares
against it (finding H1 below).

## 1. Inputs and dependencies

| input | state |
|---|---|
| `corpus/lessons/round-64-verifier-spotcheck.md` §6 (R1–R7) | present; read in full |
| `reports/round-65/accept-ca.py` rev1 (frozen) | present; all 9 legs read at source |
| `reports/round-65/claims.json` Ca statement/legs | present; frozen |
| `reports/round-65/telemetry/dry-run-ca.txt` (base dry run) | present; every leg FAIL at base |
| **`.ufo/waves/round-65/stage/records-fix/` (ExecRecordsFix draft)** | **ABSENT — dependency unmet at review time.** No disposition draft exists; this review is therefore of the frozen instrument + the facts each disposition must assert. `reports/round-64/*` and `corpus/*` are unmodified in the worktree (`git status --porcelain` lists only untracked `reports/round-65/`, `.ufo/waves/round-65/`, `tools/check-row-fragments.py`). |
| **`reports/round-65/telemetry/controls-ca.txt`** | **ABSENT.** `claims.json` `controls` says controls-ca.txt lands "before any data seat". Only `controls-c.txt` exists (which is claim C's, and is itself defective — see §5 adjacent). |
| `.ufo/reports/round-65/` (filed report for the R1 erratum) | ABSENT; L1-written at the end. R1's fourth element has no leg, so it can pass without it (H1). |

## 2. Per-defect verdicts

Legend: **bypass** = satisfiable by token presence/keyword suppression with the defect intact
(HIGH-1 class). Proofs in §3 were evaluated against the exact leg expressions.

### R1 — HIGH — **VACUOUS-ADJACENT BYPASS (cosmetic re-stamp passes)**
Leg predicate (`accept-ca.py:105-120`): `"measured revision: <TRUE_REV>" in receipt` **anywhere**,
`^tree: <8bab271c^{tree}>$` anywhere, `"re-stamped"` anywhere, and the old stamp
`measured revision: 95c9194e…` after the **last** `"original receipt bytes"` marker; plus
`"Correction (round 65, R1)"` in LOG.md, SCORECARD.md, `w2/LessonFinal.md`.

- **No positional anchor.** The operative header can remain the false stamp while a correction note
  appended below satisfies containment. Proven (§3): a receipt whose line 2 is still
  `measured revision: 95c9194e…` and whose note repeats the old stamp passes `r1_ok=True`.
  That is exactly the defect R1 asks to remove.
- **No byte-preservation check.** The leg cannot tell the preserved "original bytes" from invented
  text; the committed original (`sha256 c69d1739…`, identical at base and 8bab271c) is available
  for a byte comparison and unused.
- **No read-input verification.** It checks the tree hash resolves and matches the literal, never
  that the receipt's read-input list hashes to it. The claim's requirement "pin a tree hash of
  its read inputs" is reduced to "print the right 40 hex".
- **Repeats are heading-token only.** The stale string
  `PASS 7/7 at \`95c9194e\`` still exists in SCORECARD.md at base (`grep -c` = 1) and is not
  required to change; a new `Correction (round 65, R1)` heading anywhere passes.
- **Fourth element uncounted.** "the filed-report repeat corrected by the round-65 report's
  erratum" has no leg and (today) no artifact; Ca can pass with the erratum absent.

Verdict: **disposition as instrumented is HIGH-1-satisfiable.** Recommended hardening (does not
change the frozen predicate: "every leg prints PASS"): compare the receipt's bytes below the marker
to `git show 8bab271c:<path>` (or require the legacy original's sha256 literal), require the first
`^measured revision:` line to be TRUE_REV, and add an ERRATUM leg over
`.ufo/reports/round-65/kotodama.md`.

### R2 — MEDIUM — **PARTIAL BYPASS (heading-only)**
`r2_named = "Correction (round 65, R2)" in rev_text and "final-measures-c.txt" in rev_text`.
The filename token is **base-green** (`revisions.txt:10` already says
`final-measures-c.txt   measured 8d2041fa…`; dry run confirms `original_intact=True named=False`).
Only the heading token discriminates. The correction need not state the falsehood, need not name
`0c892ce`, and need not record that the path is absent at `8d2041fa`.

Facts the disposition will assert — **independently verified true**:
`git cat-file -e 8d2041fa:reports/round-63/telemetry/final-measures-c.txt` → absent;
`git log --diff-filter=A` → `0c892ce` ("… final measures …"). So the substance is correct; the leg
cannot confirm it was written. The byte-preservation half (`base_rev == rev_text[:len(base_rev)]`
against `17c32302`) is genuine and strong — keep it.

Verdict: substance verifiable, instrument heading-only.

### R3 — HIGH — **TOKEN-PRESENCE BYPASS**
`r3_ok = ("w1/ReviewerCa.md" in LOG) and ("w2/ReviewerCa.md" in LOG) and ("Correction (round 65, R3)" in SCORECARD)`.
- Base LOG.md contains **neither** path (verified `git show 17c32302:LOG.md | grep -c ReviewerCa` = 0),
  so the discriminating work is adding a line containing both strings in **any semantic
  arrangement**. "w2/ReviewerCa.md is the correct path and w1 is wrong" passes identically to the
  true correction. No anchoring to "Correction (round 65, R3)" in LOG.
- The SCORECARD half checks only the heading token — **not** that the correction table names
  `w1/ReviewerCa.md`, which the Ca statement explicitly requires ("the round-65 LOG entry **and
  the SCORECARD correction table** name .ufo/waves/round-64/w1/ReviewerCa.md").
- The existing wrong citation at `SCORECARD.md:1235` (`w2/ReviewerCa.md`) is not required to be
  annotated.

Verdict: HIGH-1-satisfiable. Harden: require the LOG line to match an ordered pattern
(`Correction (round 65, R3)` … `actual` … `w1/ReviewerCa.md` … `w2/ReviewerCa.md` … `erratum`
target), and require `w1/ReviewerCa.md` inside the SCORECARD R3 row.

### R4 — MEDIUM — **TOKEN-PRESENCE BYPASS; JSON validity unchecked**
`r4_ok` = substring `statement_correction`, substring `at least their pinned leg`, substring of the
frozen predicate sentence, over raw text with backslashes stripped. Proven (§3): a file that is not
valid JSON passes. `reports/round-64/claims.json` currently parses (verified). Base-green conjunct:
the predicate sentence is already present at base (`grep -c` = 1; `statement_correction` = 0), so it
is an invariant check, fine — but nothing verifies the *correction content*: m1/m2's disclosed extra
failures (EDGE_USERINFO/EDGE_HTTPS on m1; EDGE_MALTARG on m2) need not be named, and the original O
statement need not be preserved. The spotcheck R4 requires both.

Verdict: medium; harden by `json.loads` + asserting `statement_correction` is a non-empty string
containing `m1`, `m2`, `EDGE_USERINFO`, `EDGE_MALTARG`, and that the original offending sentence is
preserved as data.

### R5 — MEDIUM — **BASE-GREEN CONJUNCT**
`r5_in_control` is satisfied by the **unchanged** `reports/round-64/telemetry/control-o.txt`:
base lines 1–2 already carry `b7d22703`, `(revision 3)` and `c27a9fef` (verified by `git show
17c32302:… | grep`; dry run prints `in_control=True` at base). The only discriminating token is
`control-o binding` in LOG.md, and that line need carry neither the rev3 sha nor `b7d22703`.
Moreover R5's demand is that the *report* name the binding, not control-o.txt — the leg checks the
wrong artifact for the substance.

Verdict: medium; move the sha + measured-revision requirement into the LOG line (regex with both
literals) and drop the base-green conjunct, or accept it as a consistency invariant with a comment.

### R6 — MEDIUM — **TOKEN-PRESENCE BYPASS**
`r6_ok = "Correction (round 65, R6)" in lesson64 and "R64-M12" in lesson64`.
`R64-M12` is already in `round-64.md:321` at base (verified) — base-green. An empty
`Correction (round 65, R6)` heading passes. The correction need not state that the S687 flip is
committed in `95c9194e`.

Fact check — **true**: `git show 95c9194e -- corpus/SOURCES.md` shows the S687 row flipping
`mined` → `queued` in that commit (commit subject: "S687 flip mined→queued"). So the substance the
executor will write is correct; the instrument cannot distinguish it from an empty heading.

### R7 — HIGH — **NEGATIVE-ONLY, KEYWORD-SUPPRESSION BYPASS — and it collides with claim C (H4)**
`r7_ok = (m is not None) and not re.search(r"skeleton|await L1", verified_at, re.I)`.
- Proven (§3): `- verified-at: 2026-10-23 — structure prepared; cited source claims await review and
  insertion.` passes while still asserting the stale status. The fix is "delete two keywords", not
  "state verification". An empty value (`- verified-at:`) also passes.
- The leg rejects the errant line's deletion only because `m is not None` — good — but accepts any
  replacement.
- The spotcheck allowed "corrected in round 65's entry touch **or a named erratum**"; the frozen leg
  accepts only the entry edit. A named erratum disposition would print **FAIL** — the disposition
  space the spotcheck granted is narrower than the frozen predicate. This is a pseudo-frozen
  mismatch, not just a weak leg.

Harden: require `verified-at: 2026-10-24` (or an ISO date ≥ the correction date) plus the literal
`verified` and, if a verification seat is named, a seat id; and record in claims.json that the
erratum route is *not* accepted by rev1 (or add an ERRATUM alternative leg).

### CRITERION — MEDIUM — **INDEX/TOKEN BYPASS**
`re.search(r"^1[7-9]\.\s", QUALITY)` and `"tree hash" in QUALITY` (anywhere).
Base QUALITY.md has 16 criteria and no `tree hash` (verified), so today the leg is base-red — good.
But criterion **18 or 19** satisfies the number arm if added first, and the phrase `tree hash` may sit
in a glossary line. The criterion's required substance (measured revision **and** a tree hash of
read inputs, never the counter sha only) is not checked. Note also that H1's receipt would violate
the very criterion this leg certifies while the leg still passes — criterion 17 does not retro-bind
the R1 leg.

### QUOTES — MEDIUM — **VACUOUS ON AN EMPTY `## Gate` SECTION**
`tools/check-gate-quotes.py <round-65 lesson>`: exit 2 on unreadable path or missing `## Gate`
section (good — dry run `exit=2` with the lesson absent), but a lesson containing `## Gate` with
**zero recognised rows prints `GATE_QUOTES: 0 findings`, exit 0** (proven empirically, §3). The tool
prints only a finding count, never a row count, so the leg cannot distinguish "26 rows checked,
0 findings" from "0 rows checked". This is the **only** quote-integrity instrument for claim C's 26
new anchors (`accept-c.py` has no quote leg) and it is assigned to the calibration claim, where the
vacuous case is reachable.
Latent (not exploitable): `"0 finding" in q_out` also matches `10 findings`; the `returncode == 0`
guard currently prevents it (`check-gate-quotes.py` returns 1 on any finding). Keep the guard; prefer
`out.rstrip().endswith("GATE_QUOTES: 0 findings")`.
Harden: have the tool print `GATE_QUOTES: <n> rows, <k> findings` and require `rows == 26` and
`k == 0`, or a leg comparing the lesson's Gate row S-ids to SOURCES/S750–S775.

## 3. Bypass proofs (evaluated against the exact leg expressions, no lane mutation)

```
R1 cosmetic pass: True | first stamp still: measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2
R2 heading-only pass (named conjunct): True
R3 pass (any-arrangement mention): True
R5 in_control on UNCHANGED base file: True
R7 pass (keyword-suppressed, claim still false): True
CRITERION pass with criterion 18 + stray 'tree hash': True
R4 pass on broken (non-JSON) input: True
empty `## Gate` section: GATE_QUOTES: 0 findings, exit=0   [empirical, tools/check-gate-quotes.py]
```

## 4. H4 — HIGH: claim C's NOHARM and claim Ca's R7 are mutually exclusive on any single committed tree

`accept-c.py:379-384`: `NOHARM` runs
`git diff --name-only BASE main -- corpus/knowledge` and requires `diff == [ENTRY]`
(`ENTRY = corpus/knowledge/culture-material/games-play-sport-contests.md`).
R7's target `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` is **inside that
path filter**. Therefore, in any commit reachable from `main`:

- if the R7 correction is committed, `diff` lists two paths → NOHARM **FAIL**;
- if it is not committed, the R7 leg (`read(root, R64_ENTRY)` — working tree) passes only while the
  worktree is **dirty**, i.e. the measurement runs over bytes that are not the cited revision.

There is no single tree on which both frozen predicates print PASS. `claims.json`'s `separability`
promise — "Re-run design: `python3 -B reports/round-{c,o,ca}.py --root .` in any order" — is
therefore **false at the final integrated tree**: any re-run of `accept-c` after the R7 fix lands
prints `NOHARM FAIL`. Today `main == BASE == 17c32302`, so the conflict is live and unavoidable at
integration time.

Escape hatches, both defective: (a) measure C before the R7 commit and Ca after — two receipts at
different revisions, C's no longer reproducible on the shipped tree (stale receipt); (b) leave the
R7 edit uncommitted while Ca runs and commit nothing — H1 recurrence (worktree ≠ cited revision).
A third, (c) commit Ca's corpus edit off `main`, breaks "the L1 commits the round" and leaves the
shipped branch without the correction.

Recommendation (L1 decision, since the predicate sentences are frozen): `NOHARM` should compare the
**union of this round's lands** rather than hard-code `[ENTRY]`, or R7 should be dispositioned as a
named erratum with an ERRATUM leg. Either way the wave must not present both counters as
simultaneously reproducible unless the contradiction is resolved in the frozen form before data.

## 5. Adjacent observation (claim O/C receipts, outside Ca scope but same class)

`reports/round-65/telemetry/controls-c.txt` control 2 records `ACCEPT-C-65: FAIL` followed by
`exit=0`, while `accept-c.py` itself ends `return 0 if verdict else 1`. A control receipt whose
exit line contradicts the counter's documented exit contract is a false stamp of the same family
R1 routes; hand to the C/O reviewer. Not used as evidence against Ca.

## 6. Positives (verified, so the review is not one-sided)

- Base dry-run (`dry-run-ca.txt`) shows **all nine legs FAIL** at `17c32302`; the counter is not
  base-green overall, and the QUOTES leg correctly exits 2 on the absent lesson.
- R2's append-only check is a real byte comparison against `git show 17c32302:reports/round-63/telemetry/revisions.txt`, not a token scan.
- R1's tree line is validated against the actual git tree object (`0ec0e50e…`), so a wrong 40-hex fails; `grep -c` of the old stamp below the last marker is at least a constraint on ordering.
- R7 correctly rejects line deletion (`m is not None`).
- Facts behind R2 and R6 check out exactly (0c892ce added the receipt; 8d2041fa lacks the path; the
  S687 flip is in 95c9194e), and the three named records files
  (`w1/ReviewerCa.md`, `w2/CaReceipts.md`, `w2/LessonFinal.md`) are tracked.

## 7. Residual risk / verification gaps

- **No ExecRecordsFix draft exists**, so no disposition bytes could be audited; all verdicts above
  are instrument-level plus fact-checks of what the drafts must assert. If the draft lands, every
  leg must be re-attacked at its bytes (especially R1's header position and R2's correction text).
- **No controls-ca.txt.** The claim's own pre-data control is missing; Ca's do-nothing control is
  unproven beyond the base dry run (which does prove base-red for the whole counter, not for the
  base-green conjuncts named above).
- The final Ca receipt has **no leg** pinning the revision/tree it was measured at, although R1 and
  CRITERION demand exactly that of round-64 receipts — the round-65 receipt can repeat H1 while
  certifying the criterion that forbids it.
- `git rev-parse main` = base; the NOHARM path assumes `main` advances to the round-65 land commit.
  If the L1 commits on a detached HEAD and does not move `main`, NOHARM fails for a different reason
  (diff empty) — either way, integration must decide the ref before the first measurement.
- I did not execute `accept-ca.py` end-to-end (it would read uncommitted lane records and is the
  build seats' job); leg logic was read at source and its predicates exercised in isolation.

## 8. Tool installs

None. Host `git`, `python3` only; no packages installed or upgraded this session.
