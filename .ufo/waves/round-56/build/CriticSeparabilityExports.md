# CriticSeparabilityExports — round 56, routed defect 1 (R55-M5)

Seat: critic, leaf. Lane HEAD measured: `456f5ad` (declaration `b4b7db9`, manifest base `045f458`). All write-side work ran in sandbox clones under `/fast/scratch/hyaku/kotodama-r56/CriticSeparabilityExports/` (`r55` checked out at `2935c47`, `r56` at `456f5ad`). Nothing in the lane was written except this report. No tools were installed.

Axes judged: **operability** (is the declared separability check evaluable, and does it fail where it should) and **calibration** (do the declared statements say what the bytes show).

## Verdict

- The export is exact for the block. C's regex matches exactly S359 to S418 (60 ids), and those ids do not overlap any id in O's land or fixtures. The separability tool fires at S359, S400 and S418 and stays silent at S358 and S419.
- **Counterexample to the premise of item (1).** The declared command does not exit 2 only because C's entry is absent. A second declared land is also absent: REC's `corpus/lessons/round-56.md`. The tool stops at the first absent land it reaches, which is C's.
- Round 55 fits the closure's account. The declared manifest exits 1 with one finding, O->C at the S900 fixture. The exact-range regex exits 0.
- **Calibration defect.** `claims.json` `export_rule` says "O's fixture ids are S951-S957". The fixtures actually carry S951 to S961. The ids are still outside C's block, but the sentence is false.
- **Gap.** `claims-agree.py` does not compare exports. A manifest export widened back to S285-S999 still prints AGREE and exits 0.
- **On question (4):** I recommend accepting the reserved block as C's export, under the name "the exact id block a claim owns". It should come with the replay check below, and the manifest should not be narrowed after the fact.

## 1. Round-56 manifest

| check | command / evidence | result |
|---|---|---|
| regex = block | loop S000–S999 against `\bS(359\|3[6-9][0-9]\|40[0-9]\|41[0-8])\b` (`separability-manifest.json:14`, same string at `claims.json:112`) | `60 S359 S418 True` (matched set == range(359,419)) |
| boundary probes | `S358`, `S419`, `S3590`, `S0359`, `S4180`, `xS359`, `S359a` → no match; `S359-`, `(S359,`, `S418.` → match | correct `\b` edges |
| novelty (tool exits 2 if an export matches base bytes of the claim's own lands) | block-id count at `045f458`: `corpus/SOURCES.md` 0, `corpus/README.md` 0, entry absent at base; highest base row S358 | holds |
| disjoint from O's land | S-ids in `tools/check-gate-quotes.py` at `045f458`, HEAD and worktree: S187 ×1, S273 ×1, S900 ×28, S901 ×2; block hits 0 | disjoint |
| disjoint from O's fixtures and instruments | block hits 0 in `reports/round-56/fixtures/SOURCES.md` (S951–S956, S958–S961), `fixtures/lessons/entities.md` (same), `fixtures/lessons/bad-utf8.md` (S957), `accept-o.py`, `criterion11-controls-o.py` | disjoint |
| base drift | assignment names claim base `052f145`; manifest and `claims.json:5` say `045f458`. `git diff --stat 052f145 045f458 -- corpus tools reports/round-56/separability-manifest.json` is empty | no effect on any land |

**Declared command at the lane:** `python3 -B tools/check-claim-separability.py reports/round-56/separability-manifest.json` printed `SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/civilizations/kongo-kingdom.md', which is absent from the worktree ...` with `exit=2`. The committed receipt `reports/round-56/telemetry/declaration-dry-run.txt:49-52` shows the same.

**Counterexample: two lands are absent, not one.** In the `r56` clone I built a stand-in for C's landing with `criterion11-controls.py`'s `green()` (S359 to S378 filled, 20 rows; `accept-c.py` exits 0). The tool still exits 2: `SEPARABILITY_INPUT_ERROR unit REC lands 'corpus/lessons/round-56.md', which is absent from the worktree under '.'`. Listing the manifest's lands gives `REC corpus/lessons/round-56.md ABSENT`, and every other land present. After I add a one-line stand-in lesson, the tool exits 1 with one finding, `O-><base> via acceptance ... accept-o.py fails on base+O.lands (rc=1)`. That finding is expected, because O has not landed.

- Impact on operability: the declared check can be evaluated only at the records tip, never at C's or O's own landing commit. Round 55 behaved the same way: `corpus/lessons/round-55.md` is absent at `eb0a331` (C) and at `454a2dc` (O), and present from `173cab6` on.
- Impact on calibration: the receipt note "checker stops at its first absent land, so later legs are unevaluated" is true and meets criterion 9. Any closure sentence that says the check is red "only because C's entry is absent" would be false.
- Smallest correction: the lesson and final-measures receipt should name both absent lands, and the check should be run after the records commit. The tool and the manifest need no change.

**The export can fail.** I appended one line naming an id to O's land in the `r56` clone, on the stand-in tree:

| id added to `tools/check-gate-quotes.py` | separability result |
|---|---|
| S358 | 1 finding (`O-><base>` only), exit 1 |
| S359 | + `SEPARABILITY_DEPENDENCY O->C via export '...' matched tools/check-gate-quotes.py:431`, exit 1 |
| S400 | + the same O->C finding, exit 1 |
| S418 | + the same O->C finding, exit 1 |
| S419 | 1 finding (`O-><base>` only), exit 1 |

**Residual risk the tool cannot see:** records are never scanned as dependers, and every byte of `corpus/SOURCES.md` is attributed to C's land. A row that a record files inside the block would therefore read as created by C. `claims.json:12` admits this ("a declared rule, checked by the falsify wave").

**Calibration defect:** `claims.json:12` says "O's fixture ids are S951-S957". The fixture files carry S951–S956 and S958–S961 in `fixtures/SOURCES.md` and `entities.md`, and S957 in `bad-utf8.md`, so the range is S951–S961. O's own statement in the claims file names S958, S959 and S960. Smallest correction: the round-56 lesson should log the sentence old->new as "S951-S961".

## 2. Round 55 re-run (scratch clone at `2935c47`)

The only change between the two manifests is line 14, the C export (checked with `diff`).

```
$ python3 -B tools/check-claim-separability.py reports/round-55/separability-manifest.json --lane . --root .
SEPARABILITY_DEPENDENCY O->C via export '\\bS(28[5-9]|29[0-9]|[3-9][0-9][0-9])\\b' matched tools/check-gate-quotes.py:355
SEPARABILITY: 1 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=1
$ python3 -B tools/check-claim-separability.py r55-exact-manifest.json --lane . --root .      # export \bS(28[5-9]|29[0-9]|3[0-4][0-9]|35[0-7])\b
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=2
exit=0
```

`tools/check-gate-quotes.py:355` at `2935c47` is the selftest fixture line `("hard-wrapped-26", lesson('- S900 — ...`. The exact regex matches 73 ids, S285 to S357, which are exactly the rows C created (`f4015e7`→`eb0a331`: 73 new row ids, S285–S357).

**Counterexample to "the exact id range a claim creates".** I measured "created" mechanically, as row ids that are new in C's land `corpus/SOURCES.md`. At the round-55 tip `2935c47` that gives S285 to S358, 74 ids. S358 was filed by the records commit `173cab6` (the commit that adds `| S358 |`), but the manifest attributes it to C, because the record wrote it into C's land path. So "creates" changes with the revision measured. It equals the closure's S285–S357 only at C's landing commit `eb0a331`. Any check of "exact" has to name that commit.

## 3. Amendment for `corpus/QUALITY.md` criterion 7

Proposed sentence, to append to criterion 7:

> Each claim declares its exports before dispatch as the exact id block it owns — the ids it creates, or a block reserved to it that no other unit may assign and whose unused ids stay unassigned — and a closure replays this by looping S000–S999 against each export (the matched set must equal the declared block), checking that the row ids new at the claim's own landing commit lie inside the block, and checking that no other claim's land or fixture carries an id of the block; grounded in R55-M5 at `corpus/lessons/round-55-verifier-spotcheck.md` §5 item 1.

**A demonstration that can fail, replayable by a closure.** The script is scratch only and was never landed: `/fast/scratch/hyaku/kotodama-r56/CriticSeparabilityExports/export-exactness.py`, sha256 `67357a81075f761c5ee590625066110326a27044f8e4fe8cb3d58c113d85ef1a`, stdlib only, about 70 lines. Its usage is `export-exactness.py MANIFEST BASE TIP [--block LO-HI] [--also PATH ...]`. It computes:

- MATCHED: ids S000–S999 that any export matches.
- CREATED: `^\|\s*(S\d{3,})\s*\|` row ids in `corpus/SOURCES.md` at TIP that are absent at BASE.
- OWNED: the block, or CREATED when no block is given.

EXACT requires MATCHED == OWNED and CREATED ⊆ OWNED. DISJOINT requires that MATCHED shares no id with another claim's lands or the `--also` paths.

| case | result |
|---|---|
| r55 declared manifest, base `f4015e7`, TIP `eb0a331` | EXACT FAIL (matched-not-owned 642); DISJOINT FAIL S900, S901 @ `tools/check-gate-quotes.py`; exit 1 |
| r55 exact manifest, TIP `eb0a331` | MATCHED 73 S285–S357 = CREATED; EXACT PASS, DISJOINT PASS; exit 0 |
| r55 exact manifest, TIP `2935c47`, `--block 285-357` | EXACT FAIL, created-not-owned `['S358']` (the record row in C's land path); exit 1 |
| r56 declared, `045f458`→HEAD, `--block 359-418`, `--also` the fixtures and `accept-o.py` | MATCHED 60 S359–S418 = OWNED; CREATED 0; PASS/PASS; exit 0 |
| r56 stand-in landing (S359–S378 filled), block | CREATED 20 ⊆ block; PASS/PASS; exit 0 |
| r56 stand-in plus an S419 row | EXACT FAIL, created-not-owned `['S419']`; exit 1 |
| r56 stand-in, fixture gains `\| S400 \|` | DISJOINT FAIL S400 @ `reports/round-56/fixtures/SOURCES.md`; exit 1 |
| r56 stand-in, no `--block` (exact means created) | EXACT FAIL, matched-not-owned 40; exit 1 (this is the question-4 case) |

**Companion gap (operability):** `reports/round-56/claims-agree.py` compares only ids, lands and base, so it does not check exports. In the `r56` clone I widened the manifest's C export back to S285–S999 and it printed `AGREE claims=['C', 'O']`, exit 0. Smallest correction: compare `exports` the same way it compares `lands`. The manifest and `claims.json` exports match today, but nothing keeps them matching.

## 4. Is a reserved block C may not fill "the exact id range a claim creates"?

**Yes, it can count:**
- The ids are assigned by the L1 at integration, so the created range cannot be known before dispatch. Criterion 9 forbids changing a declared input after measuring. That makes a reserved block the tightest export anyone can declare in advance.
- The block is owned and does not grow. `claims.json:12` forbids every other unit, records included, from assigning an id in it, and unused ids stay unassigned. A hit from another claim in the unused part is therefore a real defect, a breach of C's reservation. Round 55's S900 was different: it was a fixture id in nobody's range.
- It is 60 ids, against round 55's 715, and section 1 shows both edges are exact.

**No, it cannot:**
- The tool's docstring (`check-claim-separability.py:13`) defines exports as identifiers C "introduces", and criterion 7 speaks of an identifier a claim "newly exports". If C fills S359 to S378, an O line naming S400 is reported as `O->C` although C created no S400. That is the R55-M5 shape again, a regex wider than the claim's rows, only 40 ids wide instead of 642.
- The closure's route says "creates". Section 2 shows that "creates" depends on the revision measured.

**Recommendation:** keep the reserved block as the declared export. Do not narrow the manifest after integration: that would be a post-measurement change to a declared input, and `claims-agree.py` would not catch the drift. Rename the rule to "the exact id block a claim owns" and adopt the section 3 sentence and replay. If a claim hits an unused id of the block, the closure should rule it a reservation breach that must be fixed (the other unit renumbers), not a causal dependency. That keeps the verdict honest about what the tool's `O->C` label means.

The two sides do not conflict once the rule names a block rather than a created range. If the lane prefers the literal "creates", the replay's no-`--block` mode is the gate. In that case round 56's declared manifest fails EXACT by 40 ids unless C fills all 60, so that reading would need a different design, not a fix.

## Aside (outside this scope, seen in passing)

`reports/round-56/accept-c.py:18` has an unescaped `\|` in a non-raw docstring. Python prints `SyntaxWarning: "\|" is an invalid escape sequence` on stderr on every `-B` run. The exit status is unaffected (exit 0 on the stand-in). The fix is a raw docstring or `\\|`.

## Unrun checks

- I did not measure the separability check at the real landed tip, because neither claim has landed.
- I did not check `claims-agree.py` against the real records commit.
- I did not scan records for block ids. The tool cannot do it, and it falls to the falsify wave.
