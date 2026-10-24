# RevReceipts — round-65 attack on the R1 receipt class

seat: RevReceipts (revenger, wave 1, read-only)
lane: kotodama-shokunin @ base `17c32302c6845c8f164b985a8cb312d3181c8788`
scope: `reports/round-64/telemetry/final-measures-{ca,c,o}.txt` (+ `-rev5` named variant),
round-64 counter `reports/round-64/accept-ca.py` (rev2 `d0787979`), frozen round-65 leg
`reports/round-65/accept-ca.py` R1, H1 (`corpus/lessons/round-64-verifier-spotcheck.md:52`),
section 6 R1 (:3), claims Ca R1/CRITERION.
attacked: "does the receipt file alone let a reader re-derive the measured tree?", and the
ExecRecordsFix re-stamp draft.

## Verdict up front

No. None of the three round-64 FINAL receipts can be re-derived from the file alone, and the
frozen R1 leg does not test the property R1 names ("original bytes preserved", "tree hash of
its read inputs"). A 315-byte receipt that deletes the entire original output still passes R1.
The re-stamp target itself is sound and I re-ran it: the round-64 counter at `8bab271c` prints
the receipt's lines byte-for-byte, 7/7 PASS, so the honest apparatus exists — the receipt and
its counter simply do not pin it.

## Verified facts (evidence)

| fact | command | result |
|---|---|---|
| receipt absent at its own stamped revision | `git cat-file -e 95c9194:reports/round-64/telemetry/final-measures-ca.txt` | `NO` (path exists on disk, not in `95c9194`) |
| receipt created 16m42s after the stamped commit | `git show -s --format='%ci' 95c9194` vs `8bab271` | run `00:28:55`, commit `95c9194` `00:28:20`, receipt created in `8bab271` `00:45:02` |
| re-stamp target is honest | extracted `8bab271` read paths to `/tmp/r64ca`, ran `python3 -B reports/round-64/accept-ca.py --root /tmp/r64ca` | 7/7 PASS, `r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56` … identical to the receipt's lines; exit 0 |
| counter read-set is exactly 5 paths | code read of `reports/round-64/accept-ca.py` (constants + `git show`) | `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt`, and git blob `ff30a205:corpus/SOURCES.md` |
| base blob of the receipt (must be preserved) | `sha256sum` worktree = blob at base | `c69d173954076a6aab98ceddb179c9e97ec994830b110e1fa89b5e06e5317cb6` |
| `tree:` expected value | `git rev-parse 8bab271^{tree}` | `0ec0e50ea828ca6d8e20298f72af49414692e9e4` |
| per-input sha256 at `8bab271` (for the required manifest) | `git cat-file blob 8bab271:<p> \| sha256sum` | `LOG.md f0cfa467d629…`, `corpus/LOG.md d6e7a56bcc87…`, `SCORECARD.md d75047194991…`, `revisions.txt a321e8aaff95…`, `ff30a205:corpus/SOURCES.md c93a0d9b41bd…` |
| O receipts are two different runs | `sha256sum`, `diff` | `final-measures-o.txt 8e5c7ade…` vs `final-measures-o-rev5.txt 1cb15569…`; every randomized fixture id differs (`S2368/S2530/S2484` vs `S2033/S2913/S2482`) |
| O receipt has no honesty caveat | `grep -c 'exclusiv\|pinned leg' final-measures-o.txt` | `0` (the `-rev5` file carries the full scope caveat at its head) |
| O output is non-reproducible by construction | `grep -n 'random' reports/round-64/accept-o.py` | `148 import random`, `498 rng = random.SystemRandom()`, `520 rng.shuffle(plan)` |
| stale false repeats still on disk | `grep -n 95c9194 LOG.md SCORECARD.md` | `LOG.md:4162` "at the claim-C land `95c9194e` … ACCEPT-CA-64 PASS 7/7"; `SCORECARD.md:1235` "ACCEPT-CA-64 PASS 7/7 at `95c9194e`", `:1238` "C/O/Ca verify at `95c9194e`" |
| criterion 17 absent today | `grep -nE '^1[5-9]\.\|tree hash' corpus/QUALITY.md` | criteria 15, 16 only; no "tree hash" |

## Findings

### HIGH-1 — R1's leg accepts a receipt that throws the original bytes away (315 bytes passes)

Emulated the R1 predicate verbatim (`reports/round-65/accept-ca.py:49-53`) against four
candidate receipts (script kept in-session; logic copied character-for-character):

```
original(on disk)                 R1_predicate=False  len=784
HONEST full (bytes preserved)     R1_predicate=True   len=2007
BYPASS drops original output      R1_predicate=True   len=315
APPEND keeps false line 2 first   R1_predicate=True   len=1017
```

The passing 315-byte bypass is, in full:

```
ACCEPT-CA-64 evidence (FINAL, re-stamped round 65, R1)
measured revision: 8bab271c691c6b1006da95316a24ae1958ec01e2
tree: 0ec0e50ea828ca6d8e20298f72af49414692e9e4
date: 2026-10-24T09:00:00-03:00
--- original receipt bytes: see git; not reproduced here ---
measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2
```

This deletes the counter sha, the command, the date of the original run and all seven legs —
the exact bytes R1 says must be preserved — and still prints `R1 PASS`. Root cause: the leg
only requires the substring `measured revision: 95c9194…` to appear *after* the literal
substring `original receipt bytes`; the marker is not a fence, the block is never hashed, and
no `original-sha256:` is required.

Also passing (third line): the original file with the false stamp still on line 2 and a
correction merely appended at the bottom. Append-only record discipline arguably wants that
shape, but then the first line a reader reads is still the false stamp — the leg cannot tell
that apart from a genuine re-stamp, so it certifies neither shape honestly.

Fix (with base blob now known): require the receipt to pin
`original-sha256: c69d173954076a6aab98ceddb179c9e97ec994830b110e1fa89b5e06e5317cb6`, require the
corrected stamp to appear *before* the marker and the false stamp *only* inside the preserved
block, and make the leg extract `receipt.split(marker,1)[1]` (or a fenced block) and compare
`hashlib.sha256(block).hexdigest()` to the pinned original sha. Delete-the-original then fails.

### HIGH-2 — `tree:` is the commit's whole-repo tree id, not "a tree hash of its read inputs"

`accept-ca.py:47` computes `git rev-parse 8bab271^{tree}` and line 50 requires a line
`tree: 0ec0e50e…`. That value is a deterministic function of the revision already stamped on
the line above — it can be produced in one command without running the counter, and it changes
if any file anywhere in the repo changes, including the 500 MB of files the counter never
reads. It is therefore (a) redundant with the revision line and (b) no evidence of
measurement: a fabricated receipt passes HIGH-1's bypass with it. Criterion 17 and R1 both say
"a tree hash of its read inputs"; that is not what the leg checks. A reader still cannot tell
which paths were read or that the bytes read are the bytes of that commit.

Correct form (all values measured and listed above): an `inputs-sha256:` aggregate over the
sorted `sha256  path` lines of the five read paths at the measured revision, plus the literal
construction command, e.g.
`python3 -c "..."`/`git cat-file blob <rev>:<p> | sha256sum`, and the per-path lines themselves
so a reviewer can spot-check one entry without trusting the aggregate. For the round-64
counter the set is closed: `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`,
`reports/round-63/telemetry/revisions.txt`, `ff30a205:corpus/SOURCES.md` (+ the counter file,
`d0787979…`). No path outside that set affects any leg — verified by running the counter in a
tree containing only those paths.

### HIGH-3 — the re-stamp cannot honestly be stated only as "measured revision: 8bab271"

The run predates the target commit (`00:28:55` vs `00:45:02`) and the receipt's bytes never
existed in `95c9194`. Section 6 R1 offers two dispositions ("re-stamp to `8bab271c` *or* record
'worktree dirty at run; read-path bytes = 8bab271'"), but the frozen leg accepts only the first
form (`measured revision: <TRUE_REV>` literal) — the second form would FAIL R1. So the draft
must carry both: the literal `measured revision: 8bab271c691c…` *and* an explicit
"worktree dirty at run (`git status --porcelain` non-empty); records committed 16m42s later in
`8bab271c`" line. Without the second line the re-stamp replaces one false stamp with a subtly
different one (the receipt bytes were not in that commit when measured). This is the
"provenance fairness" judgment claims Ca asks review to make.

### MEDIUM-4 — the "FINAL" O receipt drops the caveat its own `-rev5` capture carried

`final-measures-o.txt` (the file LOG.md:4162 and SCORECARD.md:1234 cite) is headed
"(FINAL, rev5, second capture)" and contains **zero** occurrences of "exclusiv" or "pinned
leg", while `final-measures-o-rev5.txt` documents at its head that MUT verifies only the pinned
leg and that m1/m2 also fail other EDGE legs, so claims.json's "each fail exactly their pinned
leg" is false. A reader of the FINAL receipt sees `MUT PASS bad=[] mutants=10` and the exact
falsehood the round-64 R4 correction exists to retract. Not fabrication — fixture ids differ,
so it is a genuine later capture — but the later file is strictly less honest than the earlier
one it supersedes. Same defect class as H1: the artifact cited as evidence is not the artifact
that carries the provenance.

### MEDIUM-5 — the O receipt is unreplayable even in principle

`accept-o.py` uses `random.SystemRandom()` (148/498/520) to shuffle plan rows and assign
fixture ids, and no seed, fixture manifest, or row→URL map is pinned in either O receipt. The
two captures disagree on every fixture id (`S2368/S2550/S2080/S2530/S2484` vs
`S2033/S2919/S2918/S2913/S2482`), so "same counter sha, same legs PASS" cannot be checked
against the receipt by anyone. A receipt for a randomized counter must pin the run's fixture
manifest (or a seed) to be re-derivable; the `-rev5` file at least pins the jj working copy and
re-checks the counter hash, the FINAL file pins neither working-copy state nor a tree hash.

### MEDIUM-6 — R1's repeat check is presence-only; the false sentence is never required to go

`accept-ca.py:57-59` requires the substring `Correction (round 65, R1)` in `LOG.md`,
`SCORECARD.md`, `LessonFinal.md`. `LOG.md:4162` and `SCORECARD.md:1235,1238` still say
"ACCEPT-CA-64 PASS 7/7 at `95c9194e`"; appending the marker anywhere in each file satisfies
the leg while the false claim stays. Require a pinned value pair at the corrected site (the R2
leg's model: original bytes intact + named correction) or require the false phrase to be
absent outside the preserved original block.

### LOW-7 — R4 checks a sentence, not "the frozen predicate byte-unchanged"

`accept-ca.py:80-83` tests `"ACCEPT-O-64: every leg …"` inside `claims.replace("\\","")` — any
position, any field. Editing the `predicate` field and pasting the original sentence into the
`statement_correction` text passes. R4's own wording is "the frozen predicate sentence is
byte-unchanged"; compare the field against `git show <base>:reports/round-64/claims.json`.

### LOW-8 — CRITERION accepts any 17-19 criterion containing the words "tree hash"

`accept-ca.py:109-111`: `^1[7-9]\.\s` + the substring "tree hash". It cannot tell a criterion
that generalizes the R1 class (measured revision *and* input-manifest hash, never counter sha
alone) from a sentence containing the phrase. Today QUALITY.md has criteria 15 and 16 and no
"tree hash" (pre-data, expected). Recommend a required clause set: `measured revision`,
`read inputs`, `not only the counter` (or equivalent three phrases) rather than one phrase.

### LOW-9 (note, not a defect) — R5's control half was already true at base

`control-o.txt:1-2` already carries `b7d22703`, `revision 3`, `c27a9fef…`; only the LOG mention
was missing (dry run: `in_control=True in_log=False`). The leg therefore scores a one-line
phrase addition. Acceptable because the binding really exists, but R5's "counting" weight is
one string, and the phrase `"Control-O binding"` is satisfiable by a heading with no content.

## What a correct re-stamped ca receipt must contain (craft, for the L1/ExecRecordsFix)

Append-only over the round-64 blob (`c69d1739…`; identical at base `17c32302`), all values
verified in this seat:

1. Header line 1: `ACCEPT-CA-64 evidence (FINAL, re-stamped round 65, R1)` — contains `re-stamped`.
2. Line 2 literal: `measured revision: 8bab271c691c6b1006da95316a24ae1958ec01e2`.
3. `worktree: dirty at run 2026-10-24T00:28:55-03:00 (finalization); read-path bytes equal 8bab271c, committed 00:45:02 (16m42s later)`.
4. `counter sha256: d0787979ae4e318c4a7cde4385dd2b2e36890f8e258b3733cc1a6e980533f917` (rev2, unchanged before/after — as the O receipt does).
5. `command: python3 -B reports/round-64/accept-ca.py --root .` and the original date line preserved verbatim in the block.
6. `tree: 0ec0e50ea828ca6d8e20298f72af49414692e9e4` (satisfies the frozen leg as written).
7. `original-sha256: c69d173954076a6aab98ceddb179c9e97ec994830b110e1fa89b5e06e5317cb6` — for the base blob, so preservation is checkable.
8. `inputs-sha256:` aggregate + per-path lines for exactly:
   `LOG.md f0cfa467d6295690281364a77b97c423bcf21080f67b0874962de7896f9e7371`,
   `corpus/LOG.md d6e7a56bcc87bdb63b53868fd271386c7d66efc61de779a051838fa522063482`,
   `SCORECARD.md d7504719499194f51e77efd6e65b83af053f0bf3bde787139e99cf4cd30befa6`,
   `reports/round-63/telemetry/revisions.txt a321e8aaff95b2987c96dba8cbba7470b18c195f398603171da968f2fa0b34fe`,
   `ff30a205c8d23b35f1ac533740121a955a9fda96:corpus/SOURCES.md c93a0d9b41bdb3db68039ca756fa74a2ab779b2860e5ebf98e05c2d2e1d7cc1f`,
   with the construction command (`git cat-file blob <rev>:<p> | sha256sum`, sorted lines hashed).
9. `replay: python3 -B reports/round-64/accept-ca.py --root <tree extracted from 8bab271>` → 7/7 PASS, lines identical; this seat reproduced it.
10. The marker line, then the **original 15-line receipt byte-for-byte** below it (784 bytes, sha `c69d1739…`), nothing elided.

A re-stamp that omits 3, 7, 8, or 10 is a false stamp of the class R1 routed — and the current
counter will still print it PASS (HIGH-1/HIGH-2).

## Dependency (recorded, unresolved)

`/.ufo/waves/round-65/stage/records-fix/final-measures-ca.txt.replacement` is **absent**:
`.ufo/waves/round-65/stage/` does not exist (`ls` exit 2), `find .ufo/waves/round-65 -name
'*replacement*' -o -name '*records-fix*'` returns nothing, and `agent://kotodama-r65.ExecRecordsFix`
reports "running / nothing produced yet" at attack time. I could not attack the draft's bytes;
I attacked the leg that will judge it and specified the required content instead. When the
draft lands it must be checked against HIGH-1 (marker is not a fence), HIGH-2 (`tree:` is not
an input hash), and HIGH-3 (dirty-worktree disclosure), and its `inputs-sha256` values must
equal the five values in item 8 above — any other sha means the draft pinned the round-65
corrected worktree bytes (LOG/SCORECARD now carry round-65 text), which would be a false
tree claim, not a re-stamp.

Additional dependency: pre-data control for Ca (`reports/round-65/telemetry/controls-ca.txt`)
is absent (telemetry holds `census-start`, `controls-c`, `dry-run-{c,ca,o}`). Per claims.json
"Controls", a control must fail the round-65 form before data; `dry-run-ca.txt` (01:20:49)
shows the base FAIL set and is the only available control evidence.

## Residual risk

- I did not execute the round-65 counter end-to-end (build lands are absent; every leg but
  R1/R2/R5 currently FAIL by design).
- My replay of the round-64 counter used the base-extracted tree at `8bab271` with only the
  five read paths materialized; a full tree would exercise nothing else (read-set verified by
  code and by the successful 7/7 run).
- `final-measures-c.txt` has the same class defect (revision + counter sha only) but sits at a
  truthful revision; it is not in R1's land set, so criterion 17 must be read as forward-only
  or C needs its own re-stamp.
- No tool installs were made in this seat; no git/jj writes; the only writes were under
  `/tmp/r64ca` (scratch clone) and this report.
