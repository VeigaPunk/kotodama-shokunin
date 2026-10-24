# RevCounterCaKeying — attack `accept-ca.py` R1 keying depth

Seat: attack (independent leaf). Lane: `kotodama-shokunin`, base `17c32302c6845c8f164b985a8cb312d3181c8788`.
Target: frozen claim **Ca** counter `reports/round-65/accept-ca.py` (rev 1), leg **R1** only
(`accept-ca.py:105-121`). Nothing in the lane, its jj/git state or its index was mutated; every
write is under `.ufo/waves/round-65/att-r1/` and `.ufo/waves/round-65/att-r1-v2/` (scratch
fixture roots; `git status` reports them as untracked wave scratch). No commits, no git writes.

What I attacked: the R1 leg's *keying* — what the receipt text is anchored to, and whether the
leg can print PASS while the thing R1 demanded (a truthful re-stamp, preserved originals,
corrected repeats) is absent or contradicted.

The leg, verbatim (`reports/round-65/accept-ca.py:106-118`):

```
tree_code, tree_out = git_out(root, ["rev-parse", f"{TRUE_REV}^{{tree}}"])
r1_ok = (f"measured revision: {TRUE_REV}" in receipt
         and re.search(rf"^tree: {re.escape(tree)}$", receipt, re.MULTILINE) is not None
         and "re-stamped" in receipt
         and "measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2"
             in receipt.split("original receipt bytes")[-1])
r1_repeats_ok = ("Correction (round 65, R1)" in log_text
                 and ... in score_text and ... in lesson_final)
```

## Verdict per requested attack

| # | Attack | Verdict | One line of evidence |
|---|--------|---------|----------------------|
| 1 | Preserved-original block truncated to just the old `measured revision:` line (no diff of originals against git history) | **HOLE (HIGH)** | 7-line receipt keeps **1 of 15** original lines → `R1 PASS` |
| 2 | Correct `tree:` of 8bab271c, **different marker text** | **HOLE (HIGH)** | 20-line receipt, old-hash line at line 1 (above the marker), marker renamed one word → `R1 PASS` |
| 3 | Canonical marker present, old line **above** it instead of below | **FINE (correctly rejected)** | same 20 lines as #2 with `original receipt bytes` → `R1 FAIL restamp=False` |

Attacks #2 and #3 are a **minimal pair**: byte-identical receipts except the marker wording
(`--- original receipt (round-64 run, verbatim) ---` vs `--- original receipt bytes (round-64
run, verbatim) ---`, line 6 of 20). The directional rule that rejects #3 exists **only while the
exact literal is present**; rename one word and the same layout passes. So #3 is rejected, but
its rejection is load-bearing on an unpinned string, not on provenance.

## Findings

### F1 (HIGH) — the marker literal is unpinned; its absence silently deletes the below-marker rule
`accept-ca.py:112` uses `receipt.split("original receipt bytes")[-1]`. When the literal is absent,
`split` returns the whole receipt, so the check degenerates to "old revision line appears
anywhere". Consequence: the **exact R1 defect** — the false `measured revision: 95c9194e…` stamp
— can remain as the receipt's *header* line (line 1) while the leg prints PASS, provided the
marker is renamed (fixture `A2_renamed_marker_old_above`, receipt 20 lines, old hash at line 1,
marker at line 6, preserved body below the marker lacks the revision line). There is also no
uniqueness rule on `measured revision:` lines, so a receipt may carry both hashes with no
structural means to tell which one the header asserts (fixture `A2b_no_marker`: old-hash line
first, true hash later → PASS).

Fix: require `receipt.count("original receipt bytes") == 1` and split once; parse the header
region (lines before the marker) and require exactly one `measured revision:` line there,
equal to `TRUE_REV`.

### F2 (HIGH) — "preserved originals" is a single-line presence test; no git-history comparison
`reports/round-64/telemetry/final-measures-ca.txt` at the base is 15 lines (committed at
`8bab271`, unchanged at BASE). The leg accepts a preserved block of **one line** (fixture
`A1_pure_truncated`: 5 header lines + marker + old line) — 14 of 15 original lines are deletable,
including `counter sha256: d0787979…`, the `command:` line, `date:`, and the entire 10-line
`--- complete command output ---` block that *is* the receipt's evidence. `ACCEPT-CA-64: PASS /
exit=0` can therefore be asserted in a receipt with no surviving original output at all.
No leg anywhere in `accept-ca.py` does `git show` of `final-measures-ca.txt` (the only `show` is
`accept-ca.py:124` for `revisions.txt`), so "the original bytes are preserved" in the Ca
statement (`reports/round-65/claims.json`, claim Ca) and "each verified by one counting leg over
committed bytes" are not established.

Fix: byte-compare the block after the marker against `git show 17c32302:reports/round-64/telemetry/final-measures-ca.txt`
(exact suffix equality, trailing-newline-insensitive), and require the marker at column 0.

### F3 (MEDIUM) — repeat corrections are unanchored stamps; the fourth repeat has no leg
The three repeats are checked by literal containment only (`accept-ca.py:116-118`). Fixture
`E_unanchored_repeats`: `LOG.md:4162`, `SCORECARD.md:1229/1235`-style lines retain the false
`95c9194e` stamp verbatim, no line names `8bab271c`, and a bare `Correction (round 65, R1)` line
appended at EOF of each of the three files → `R1 PASS repeats_log_score_lessonfinal=True`.
Nothing anchors the stamp to the round-64 entry/row, nothing requires the corrected repeat to
name the true revision, and nothing forbids the false line surviving (contrast the spot-check's
own wording, `corpus/lessons/round-64-verifier-spotcheck.md:84`: "correct the three repeats").
Additionally the **fourth** repeat — the filed fleet-repo report, corrected by "the round-65
report's erratum" per the Ca statement — has **no leg at all**, so one of the four required
corrections is unverified while the claim says "each verified by one counting leg".

Fix: anchor each repeat (require the correction on the same logical record as the old stamp, and
require the corrected text to contain `8bab271c`), and add a leg asserting the erratum exists and
names the filed report repeat.

### F4 (MEDIUM) — "over committed bytes" is false for R1: every read is a worktree read
`read()` (`accept-ca.py:81-85`) opens files from the filesystem; there is no index/HEAD
comparison for the eight lands. All PASS results above were produced against **untracked**
fixture files. This reproduces the exact failure class R1 corrects: the round-64 receipt was
invalid because it was "a run over a moving worktree" (`spotcheck:52`, quoting the protocol's
§Gate standard: "a verdict names the revision it was measured against"). A pre-commit run of
`accept-ca.py` cannot establish the Ca sentence that says it verifies committed bytes; the
receipt must name the revision it was measured against and a post-commit re-run receipt must be
shipped, or the claim wording must be corrected.

### F5 (LOW) — fail-open tree check when the commit is unresolvable
`accept-ca.py:106` computes `tree`, but `r1_ok` never requires `tree_code == 0`. With git unable
to resolve `8bab271c` (probe: `GIT_DIR=/nonexistent/gitdir`, subprocess-local env only `tree`
becomes `""`), the regex becomes `^tree: $` and a receipt line `tree: ` (one trailing space)
passes: `R1 PASS restamp=True tree=unresolvable`. The detail string even prints
`tree=unresolvable` beside `PASS`.

Fix: `tree_code == 0 and tree != ""` as a precondition of `r1_ok`.

## Positive controls (the parts that do hold)

- Correct tree equality is real: fixture `CTL_wrong_tree` (`tree:` = base tree
  `fc0615e31525dde8dbd6ae189f3c919645e2ef7f` instead of `0ec0e50ea828ca6d8e20298f72af49414692e9e4`)
  → `R1 FAIL restamp=False`.
- Full verbatim block below the canonical marker (`CTL_full_block`) → `R1 PASS`, so the leg is
  not rejecting the honest shape.
- The tree pin is the root tree of `8bab271c`; all eight read paths are tracked and present in
  that tree (checked `git cat-file -e 8bab271c:.ufo/waves/round-64/w2/LessonFinal.md`, rc=0), so
  the pin is a superset of the read inputs. Not a defect, though the Ca wording "a tree hash of
  its read inputs" describes the root tree rather than a per-input set.
- Pre-data state is honest: `reports/round-65/telemetry/dry-run-ca.txt` shows `R1 FAIL
  restamp=False`, and the receipt currently on disk has 0 markers and no `tree:` line.

## Residual risk / verification gaps

- I did not exercise the build seats' eventual receipt: it does not exist yet, so the three
  attacks are demonstrated against crafted receipts, not the real land. If the build seat ships
  the canonical marker plus the verbatim 15-line block plus anchored repeats, R1 would pass
  honestly — the holes are about what the leg *cannot distinguish*, not about current bytes.
- The `QUOTES` leg cannot run inside fixture roots (no `tools/`), so fixture verdicts are read
  from the `R1` line only; overall `ACCEPT-CA-65: FAIL` in fixtures is expected and irrelevant.
- R3/R5/R6 use the same unanchored-literal pattern (`accept-ca.py:130-137`, `:145-150`, `:153-156`);
  those are other seats' scope but share F3's class.
- No tooling installed or upgraded (nothing needed; `git`, `python3` only).

Repro: fixtures and their receipts are at
`.ufo/waves/round-65/att-r1-v2/{A1_pure_truncated,A2_renamed_marker_old_above,A3_canonical_marker_old_above,CTL_full_block,CTL_wrong_tree,F_empty_tree}/`;
run `python3 -B reports/round-65/accept-ca.py --root <fixture>` from the lane root and read the
`R1` line. The `E_unanchored_repeats` fixture is at `.ufo/waves/round-65/att-r1/E_unanchored_repeats/`.

Report: .ufo/waves/round-65/w1/RevCounterCaKeying.md
