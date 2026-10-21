# ReviewSepFixture — round-50 falsify: the r49 separability fixture and the Ca checker

Seat: `KotodamaR50-2.ReviewSepFixture-21` (reviewer, leaf). Attack target: `reports/round-50/separability/r49-fixture.json` at landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, plus the independent prediction `reports/round-50/separability/r49-expected-independent.txt`, plus `tools/check-claim-separability.py` as it consumes them.

Method: private clone `git clone -q --shared` under `/tmp`, checked out at `1c779e4a`; all landed bytes read with `git show <rev>:<path>` / `git cat-file`; the lane was never written. The lane repo is byte-identical to the clone's `1c779e4a` for every file I attacked (`git rev-parse` on both trees agrees), and `c8865c7` (a later falsify-wave commit) does not touch `reports/round-50/separability/` or `tools/check-claim-separability.py` — so these findings stand against current `main` too. Author-lane advice, not admission.

## Verdict

**PARTIAL.** The fixture's headline claim holds and the C→S finding is reproduced for a defensible reason — but three defects mean the fixture does not measure what it claims to measure.

| question asked | answer | evidence |
|---|---|---|
| Are the lands/trees/exports a faithful mechanical derivation of round 49? | **Lands: yes. Trees: yes, and they are the receipt-measured trees. Exports: NO — hand-picked, and it is under-specified.** | §1, §2, §3 |
| Does the checker on the fixture reproduce the outside verifier's C→S finding? | **Yes — exit 1, `SEPARABILITY_DEPENDENCY C->S` present, on real r49 bytes.** | §4 |
| For the right reason? | **Partly. The land-path leg fires on the right bytes; the export leg fires on a range mention (`rows S031–S042`) that a hand-written shelf note produces, not on per-row citation.** | §5 |
| Does the fixture match `r49-expected-independent.txt`? | **Yes, under the runner's own normalizer — but the normalizer discards multiplicities and the matched-id list, so the comparison is weaker than it reads.** | §6 |
| Would the fixture catch a checker that has stopped working? | **Yes for always-separable and always-dependent mutants; NO for a checker that duplicates findings, and NO for the shared-land exclusion the sibling report requires.** | §7 |

---

## §1 The lands are a faithful derivation of round 49

`reports/round-50/separability/r49-fixture.json:6-11,21-28,40-46` partition the r49 landed bytes into the three claims r49 declared (`reports/round-49/claims.json` declares C and Ca; `reports/round-49/claims-addendum-kaika.json` declares S). Every changed path at the r49 commits is accounted for:

```
git show --name-only --format= c6a174d 8cee755 d91c632 | sort -u
```
→ 18 paths. Fixture lands cover `corpus/knowledge/culture-material/hunting-foraging-subsistence.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-49.md`, `corpus/QUALITY.md`, `SKILL.md`, `tools/check-readme-revisions.py`, `reports/round-49/integration/Ca-evidence.md`. The remaining 10 (integration helpers, `run-validation.py`, `claims-addendum-kaika.json`, `corpus/lessons/README.md`, `LOG.md`) belong to no unit and are left at base bytes in every counterfactual — the sibling report's "unassigned changed path is itself a finding" control is **not** implemented in the landed checker, so this omission is silent rather than surfaced. Re-assigning all 10 to S (my T-B) changes nothing in the finding set, so the omission is currently harmless, but it is unmeasured.

Two of the three trees are exactly the r49 receipt-measured bytes. `reports/round-49/validation.json`'s `input_sha256` pins three files, and all three match the fixture's trees byte-for-byte:

```
receipt README      666fb794c71f94867b923152f747a105ee28ecb1bb2cc7fd5bd9cdffe79e3a35
8c78e6b README.md   666fb794c71f94867b923152f747a105ee28ecb1bb2cc7fd5bd9cdffe79e3a35  ✓
receipt entry      64cb0d555d1970797f0fbff808afe7fda0c776da706fb55cf2fb934bc8a7b590
8c78e6b entry      64cb0d555d1970797f0fbff808afe7fda0c776da706fb55cf2fb934bc8a7b590  ✓
receipt revisions  d49fdf1c9524c457c2a5fb9c647442e682c6a3de98030d3c778b5f33740cdeb7
8c78e6b tool       d49fdf1c9524c457c2a5fb9c647442e682c6a3de98030d3c778b5f33740cdeb7  ✓
```

## §2 The trees are the right trees — and the tree choice is load-bearing in a way the fixture does not disclose

C and Ca use `8c78e6b` (the r49 "C-without-S leg" fix); S uses `d91c632` (the r49 adjudicated state). That is a defensible reading of "the state the outside verifier adjudicated", and the executor says so (`.ufo/waves/round-50/build/ExecSepFixture.md:33`). But it has a consequence the fixture hides: **S's tree is not the tree the r49 receipt measured.**

The r49 receipt pins `corpus/SOURCES.md` at `933013a1…` and `corpus/lessons/round-49.md` at `272eab2e…`. Those are the **8c78e6b** blobs. At `d91c632` the same paths hash to `662f9626…` and `51ab6a5c…` — the 8cee755/d91c632 post-review edits. So the fixture's S unit reads bytes the r49 receipt never measured, and the fixture's own S acceptance (`assert len(ids)==47 and len(set(ids))==47`) is pinned to the *later* 47-row registry while the receipt measured 43 rows.

Swapping S's tree to the receipt-measured `8c78e6b` changes the verdict:

```
T1  S tree = 8c78e6b  →  rc=1, 7 findings, adds
    SEPARABILITY_DEPENDENCY S-><base> via acceptance [...] fails on base+S.lands (rc=1, stderr 'AssertionError')
    and no declared unit's lands repairs it
```

That is the correct behaviour (43 rows ≠ 47), and it shows the fixture's acceptance is measuring the tree, not the claim. **Smallest fix:** either pin S's tree to `8c78e6b` and its acceptance to 43 rows (matching the receipt), or state in the fixture that S is the adjudicated-registry unit and that its acceptance is a registry-state assertion rather than a claim assertion. Both trees are already `lands`-faithful; only the acceptance constant is wrong for one of them.

## §3 The export is hand-picked and under-specified — a real false-negative surface

`r49-fixture.json:29-31` declares S's export as `\bS0(3[1-9]|4[0-7])\b` — S031 through S047. But S's added bytes introduce **53** distinct S-ids, and the export covers only 17 of them:

```
ids S's added bytes introduce: 53   (S001-S047 plus stage labels S101 S113 S201 S215 S301 S315)
covered by declared export:      17
UNCOVERED: S001-S030, S101, S113, S201, S215, S301, S315
```

S001–S030 are S-owned: they are rows in `corpus/SOURCES.md` (S's land) whose `used-by` columns point at pre-existing corpus entries. A claim citing any of them has a genuine dependency on S that the declared export cannot see. The executor's own note (`.ufo/waves/round-50/build/ExecSepFixture.md:36`) says the assignment's guessed range "was wrong in both directions — registry defines S001–S043 at 8c78e6b / S001–S047 at d91c632" — the correct range was known and the narrow range was shipped anyway.

This is a **false negative on real bytes**, not a synthetic concern. I rebuilt the r49 entry with every S-id replaced by `S012` and the registry path renamed (so the land-path leg cannot fire), then re-ran the checker:

```
MUT-G  declared export S031-S047 (as shipped)          →  C->S findings = 0   ← MISSED
MUT-G  mechanically-derived export (all 47 S rows)     →  C->S findings = 1
       SEPARABILITY_DEPENDENCY C->S via export '\bS0(0[1-9]|[1-4][0-9])\b' matched ...:18
```

A claim citing an S-owned row is reported separable. **Smallest fix:** derive S's export mechanically from the ids S's landed bytes introduce — `\bS0(0[1-9]|[1-4][0-9])\b` covers S001–S047 and stays novel at base (base `corpus/SOURCES.md` and `corpus/lessons/round-49.md` do not exist, and base `corpus/QUALITY.md`/`SKILL.md` contain 0 `\bS\d{3}\b` tokens, so `_check_novelty` at `tools/check-claim-separability.py:491` still passes — I confirmed the widened export runs without an input error). Note the widened export does not change the r49 verdict: it still reports exactly the same 6 findings, because the entry cites only S031–S042.

## §4 The checker does reproduce C→S on the fixture

Against the landed clone, read-only:

```
$ python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json --lane <clone>
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 6 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
EXIT=1
```

Identical output when `--lane` points at the real lane. The `C->S` finding is present, and the claim's `after_required` ("exits 1 naming the C->S dependency (1/1 detected)") is met.

The **land-path leg fires for the right reason.** `corpus/SOURCES.md` is absent at base `c42d675` (`git cat-file -e c42d675:corpus/SOURCES.md` → absent) and is a path S newly lands; C's added bytes name it. That is exactly the r49 defect the outside verifier adjudicated (`corpus/lessons/round-49-verifier-spotcheck.md:17` — "C cites the registry S creates"). The tool's `name_paths()` (`tools/check-claim-separability.py:366-368`) correctly restricts path hits to base-absent lands, so ambient `corpus/README.md` and `corpus/QUALITY.md` mentions do not fire.

## §5 But the export leg fires on a range mention, not on a citation

The export leg's reported hit is `hunting-foraging-subsistence.md:18` — the shelf-note line:

```
  - External shelf — **opened this round (2026-10-19)**, registered in `corpus/SOURCES.md` rows S031–S042 (plus one rejected, uncited popular-press row)
```

The regex `\bS0(3[1-9]|4[0-7])\b` matches the literal tokens `S031` and `S042` inside the range string `S031–S042`. The tool reports only the **first** matching line (`_first_line_hit`, `tools/check-claim-separability.py:607-614`), so the finding's cited location is the range mention. I confirmed in isolation that this is sufficient on its own: an entry whose entire content is the single line

```
registered in corpus/SOURCES.md rows S031-S042 (no individual ids cited below)
```

produces `SEPARABILITY_DEPENDENCY C->S via export` with no body citation anywhere.

The r49 bytes are stronger than the finding text shows — the entry carries 52 individual `\bS03[1-9]\b` citations (lines 20, 92, 96, 104, 106, 112, 116, 123-126, 141-146, 182-189, 193, 197, 201), and removing only the range token keeps the finding alive (MUT-H). So the r49 *verdict* is right; the *evidence the tool prints* is one line weaker than the truth. **Smallest fix:** have the export leg report the number of distinct ids matched and the first line containing a **standalone** id (not one inside a range), so the printed location is a citation.

## §6 The runner's comparison against the "independent prediction" is weaker than it reads

`reports/round-50/run-validation.py:387-394` normalizes both sides to `(kind, pair, via, target)` and `:397-404` compares the two **sets**. The normalizer's trailing group `(?: (?:named at|matched|x\d).*)?$` discards the multiplier (`x12`), the matched-id list, and the location. I verified by corrupting the expected file:

| corruption applied to `r49-expected-independent.txt` | runner still says match? |
|---|---|
| multiplicity `x12` → `x99` | **yes** (ignored) |
| all `xN` multipliers deleted | **yes** (ignored) |
| export matched-id list `S031,…,S042` → `S001,S002` | **yes** (ignored) |
| land-path target `corpus/SOURCES.md` → `corpus/OTHER.md` | no (caught) |
| export regex changed | no (caught) |

So `r49_matches_independent_prediction: true` (receipt `reports/round-50/validation.json`) certifies the **pair set and the leg kind**, and nothing about multiplicity or about which ids were matched. The expected file's `x12` for `S->C` is a claim the tool never makes (the tool prints one line, not a count) — the tool's own output has no multiplicity, so the expected file's `xN` column is not checkable against the tool at all, and the receipt's `true` does not mean what a reader will take it to mean.

Separately, `r49-expected-independent.txt` is not independent of the tool in the sense the name implies: it was produced by the same seat that wrote the fixture, and its line order and wording track the fixture's own `expected_findings` array (which the landed fixture does **not** carry — see §8). "Independent prediction" here means "second implementation of the same author's semantics", not "outside verifier".

## §7 Mutation discrimination: partial

| mutant | runner's `r49_matches` | note |
|---|---|---|
| always-separable (all findings suppressed) | **False** ✓ caught | |
| always-dependent (every ordered pair) | **False** ✓ caught | |
| duplicate every finding line | **True** ✗ **not caught** | set comparison collapses duplicates |
| shared-land exclusion (the sibling report's gate 3) | **True**, but the finding set changes | see below |

The duplicate mutant matters: `report()` (`tools/check-claim-separability.py:676-687`) prints findings and then a count; a checker that emits each finding twice, or that emits 6 findings and claims 12, still satisfies the set comparison. The receipt's `r49_fixture_rc: 1` would still be 1.

The shared-land mutant is the substantive one. `.ufo/waves/round-50/build/ConnectSiblingSeparability.md:142-145` (gate 3) requires bytes of a path in `X.lands ∩ Y.lands` to be reported as `SEPARABILITY_OVERLAP` and **not** used for directed dependency. The landed checker does not implement that: `corpus/README.md` is in both C's and Ca's lands, and the `C->Ca` finding fires on a line that is **Ca's own prose**, present in Ca's added bytes and C's added bytes verbatim (I verified all 24 of C's added README lines are byte-identical to Ca's; C's *unique* land — the entry — contains 0 occurrences of `check-readme-revisions`):

```
C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
  text: `python3 tools/check-readme-revisions.py` (exit 1). Routed residual, not
  same line present in Ca's own added README lines: True
```

Implementing the gate correctly (exclude co-land bytes from the directed scan) drops `C->Ca` and makes the fixture's expected set no longer match:

```
MUT-E  rc=1, dropped ('DEP','C->Ca','land path','tools/check-readme-revisions.py')
       → runner r49_matches = False
```

The tool's own docstring already says the right thing (`tools/check-claim-separability.py:28`: "Overlap: the same path in two units' lands is a finding, not a dependency") — the implementation does not honour it. **This is the fixture's most consequential defect: the expected file freezes the un-corrected behaviour as the oracle, so a later fix to the tool will look like a fixture regression.** Smallest fix: implement gate 3 in the checker, and drop the `C->Ca` line from `r49-expected-independent.txt` at the same time (the `S->C` and `S->Ca` findings are on S's own non-shared lands and survive).

## §8 Two provenance defects in the shipped artifacts

1. **The patch in the lane cannot be applied as-is.** `.ufo/waves/round-50/patches/ExecSepFixture-4.patch:10` carries an `"expected_findings": [...]` key in the fixture, but the landed checker rejects unknown manifest keys (`tools/check-claim-separability.py:85` `MANIFEST_KEYS`, `:374` `_check_keys`). Running the patched fixture gives `rc=2 SEPARABILITY_INPUT_ERROR manifest has unknown key(s) expected_findings`. The landed fixture correctly omits the key — but `.ufo/waves/round-50/build/CriticFrontier.md:50` asked for exactly that key inside `r49-fixture.json` ("Add `expect_findings`: [...] to `r49-fixture.json`. The selftest compares the set for equality"). The request is unsatisfiable against the landed schema; the expectation had to move to the sidecar file, which is where it went. Worth resolving explicitly rather than leaving two artifacts that disagree about where the expectation lives.

2. **The shipped digests do not match the shipped bytes.** `ExecSepFixture.md:13-14` records `6bd7f750…` for the fixture and `7a31beaa…` for the r50 manifest. The landed files hash to:

```
r49-fixture.json   3a6e39bce756c1777b910e82f20a0f2879679980546378849e2dd620237f0c67
r50-manifest.json  ab3c7658c9c46253fcf09adcd0e4895138fe5e804658ca9674eafcf6c1678717
```

The r50 manifest also differs substantively from the patch (acceptance argv filled in, `needs_git: true` added, `REC` extended with the manifest itself, Ca's `lands` changed from a glob to two explicit paths). `ExecSepFixture.md:37` pins the patch digests as "frozen"; the landed bytes are not those bytes. The receipt `reports/round-50/validation.json` is itself **untracked** (`git cat-file -e 1c779e4a:reports/round-50/validation.json` → absent), so nothing in the landed tree records the digests that were actually verified.

## §9 What I could not evaluate

- Whether `d91c632` (S's tree) is the *right* adjudicated state for round 49 is a lane-policy question I cannot settle from bytes; I report both trees' behaviour and the receipt drift, not a verdict on the choice.
- I did not re-open any source URL behind S001–S047; the "S-owned" claim rests on the rows living in S's land `corpus/SOURCES.md` with `used-by` columns, which is what the export-leg semantics keys on.
- `reports/round-50/validation.json` (the Ca receipt) is untracked, so I could not check its provenance; I re-derived its two Ca claims independently and both hold against the landed bytes.
- The r50 manifest is outside my assigned item; I ran it only to confirm the fixture's own findings do not leak into it (`SEPARABILITY: 0 findings` at the landed tree).

## Recommended order (smallest first)

1. Implement gate 3 (co-land bytes excluded from directed scans) in `tools/check-claim-separability.py`, and drop the `C->Ca` line from `r49-expected-independent.txt` in the same change.
2. Widen S's export to the mechanically derived set (`\bS0(0[1-9]|[1-4][0-9])\b`) so the export leg cannot miss an S-owned row outside S031–S047. r49's finding set is unchanged by this.
3. Reconcile S's tree with the r49 receipt: either pin `8c78e6b`/43 rows, or label the S acceptance as a registry-state assertion and say so in the fixture.
4. Make the export leg report matched-id count and a standalone-id location, so the printed evidence is a citation rather than a range token.
5. Resolve where the expectation lives (inside the fixture is impossible under the current schema — amend the schema, or amend `CriticFrontier.md`'s request), and record the digests of the bytes actually landed.

## Checks run (read-only; `/tmp` only, deleted)

- `git clone --shared`, `git checkout`, `git show`, `git cat-file`, `git ls-tree`, `git log`, `git rev-parse`, `git diff`, `git grep -E/-c/-o`, `git hash-object -w` + `git update-index`/`git write-tree`/`git commit-tree` (mutant trees built **in the private clone** only; verified absent from the lane).
- Checker runs: landed fixture (clone lane and real lane), 5 fixture variants (S tree 8c78e6b; C/Ca tree c6a174d; C.lands minus README; lesson removed from S.lands; all 10 unassigned r49 paths added to S), 3 export-range variants, 5 mutant checkers (always-separable, always-dependent, duplicate-findings, shared-land-exclusion ×2), 5 tree mutations of the real r49 entry bytes (S-ids stripped; registry path renamed; S031→S012 + path renamed; S-ids→S012 only; range token removed).
- `--selftest` on the landed checker: 56/56 checks pass, exit 0.
- The lane repo was not written: `git log`/`git status` show only pre-existing wave state; none of my four mutant commit objects exist in the lane (`git cat-file -e` → absent for all four).

No tools installed; none needed.
