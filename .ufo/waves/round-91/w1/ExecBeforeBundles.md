# ExecBeforeBundles — round-91, claim O BEFORE state (2026-11-05)

Seat: ExecBeforeBundles (leaf, no dispatches). Scope: measure the BEFORE state of claim
O on committed bytes, by building three synthetic counterfeit entry bundles and running
the frozen v1 grader (base d39434b3 bytes) and the working-tree v2 grader in entry mode
over each, with the argument list of `reports/round-91/measure91.py::grade_c`.

## Files written

- `.ufo/waves/round-91/w1/stage/ExecBeforeBundles/bundles/bundle-bakery/` (11 files)
- `.ufo/waves/round-91/w1/stage/ExecBeforeBundles/bundles/bundle-shadow/` (11 files)
- `.ufo/waves/round-91/w1/stage/ExecBeforeBundles/bundles/bundle-selfquote/` (11 files)
- `.ufo/waves/round-91/w1/stage/ExecBeforeBundles/before-bundles.txt` (commands, stdout, stderr, rc for all runs)
- `.ufo/waves/round-91/w1/stage/ExecBeforeBundles/bundles.md` (what each bundle is and is for)
- `.ufo/waves/round-91/w1/stage/ExecBeforeBundles/build_and_run.py` (fixture driver, preserved for reproduction)
- this report

No lane-tree writes outside the stage dir and this report. No commits, pushes, or
mutating git/jj commands. Only read-only `git show` against the lane repo.

## Grader bytes (verified)

- `git -C <lane> show d39434b3bc8458e1b66edd2d0d0fea9ea32f3331:tools/check-advance-evidence.py > <scratch>/v1/...` → rc 0; sha256 `121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed` — matches the freeze pin in `claims.json` (`v1_tool_sha256_base`).
- Working-tree `tools/check-advance-evidence.py` sha256 `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093` — matches `O.tool_sha256`.

## Fixtures (synthetic counterfeits, not evidence about any source)

Precheck of the shared entry: 12,889 bytes, 17 h2 headings, table 6x4, 16 shared content
words with the declared round-91 topic, worst sentence repeat 1, cited ids exactly
S952/S953/S954, v2 phrase anchors in headings/table cells: `argot`, `cant` (2/6).
Registry in every bundle = base d39434b3 `corpus/SOURCES.md` bytes (875 rows, last S951)
+ three appended synthetic rows S952–S954 (tier A, status mined, opened 2026-11-05,
used-by `corpus/knowledge/bakery-rota.md`), one `- S9xx LOCATED — "<quote>" — <url>
accessed 2026-11-05, section 2` gate line per row, captures under
`reports/round-91/evidence/` with manifest sha256 + http_status 200 + fetched_at
`2026-11-05T12:00:00-03:00`. Mutations per bundle: shadow = S954 URL duplicates base row
S900's URL; selfquote = S953 gate quote equals its teaching cell.

## Measured results (grader x bundle)

| grader x bundle | rc | final verdict | discriminating LEG observation |
|---|---|---|---|
| v1 x bundle-bakery | 0 | `ENTRY-EVIDENCE: PASS legs=6/6` | v1 TOPIC clean on 16-word overlap |
| v2 x bundle-bakery | 1 | `ENTRY-EVIDENCE: FAIL legs=7/8 failed=TOPIC` | `2 of 6 sub-topic phrases in headings/table cells < 4; phrase anchors 2/6` |
| v1 x bundle-shadow | 0 | `ENTRY-EVIDENCE: PASS legs=6/6` | no UNIQUENESS leg exists in v1 |
| v2 x bundle-shadow | 1 | `ENTRY-EVIDENCE: FAIL legs=6/8 failed=TOPIC,UNIQUENESS` | `S954: url shadows base row S900: https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Ship` |
| v1 x bundle-selfquote | 0 | `ENTRY-EVIDENCE: PASS legs=6/6` | v1 GATE never compares quote to teaching cell |
| v2 x bundle-selfquote | 1 | `ENTRY-EVIDENCE: FAIL legs=6/8 failed=TOPIC,GATE` | `S953: gate quote is the row teaching cell (self-quote)` |

Full per-leg lines and verbatim argv in `before-bundles.txt`.

## Finding (BEFORE state of claim O)

The expectation in the assignment is confirmed exactly: v1 PASSES the bakery bundle on
all six of its legs (rc 0) and v2 FAILS it on TOPIC (rc 1). Beyond that: v1 also passes
the shadow-URL bundle and the self-quote bundle (6/6 each) because its entry mode has no
UNIQUENESS leg and its GATE leg does not compare the gate quote with the row's teaching
cell; v2 refuses each of the three classes by name. v2 fails TOPIC on all three bundles
because the same off-topic entry text is reused per the assignment spec; the
discriminating refusals are UNIQUENESS (shadow) and GATE (selfquote). This is the
before-state weakness claim O's `before` field describes, reproduced on fresh synthetic
fixtures rather than the frozen controls.

## Commands run (with rc)

- `mkdir -p` stage bundles dir and scratch → rc 0.
- `git -C <lane> show d39434b3...:tools/check-advance-evidence.py > <scratch>/v1/...` → rc 0.
- `sha256sum` both grader byte streams → rc 0 (hashes above; also `wc -l`: v1 967, v2 1118, measure91.py 319).
- `git show` of base `corpus/SOURCES.md` (875 rows, last S951) and base `corpus/lessons/round-90.md` into scratch → rc 0.
- Driver run 1 → rc 1 (precheck refused: entry 10,211 B < 12,000; `argot` missing from h2/table anchors). Fixed entry.
- Driver run 2 → rc 0: built 3 bundles, ran 6 grader invocations (rcs 0,1,0,1,0,1 as tabled).

## Bounds, cleanup, environment

- No tools installed or upgraded (none needed); pacman untouched; no sysctl writes; no network access (fixtures are synthetic; v1's own contract is "No network access").
- Scratch `/fast/scratch/hyaku/kotodama-r91/ExecBeforeBundles/` (v1 grader bytes, base registry/lesson bytes, driver) deleted before yield; the reproducible driver copy lives in the stage dir. `/tmp` unused.
- Sibling materials untouched: claims.json, measure91.py, mutants.py, stub control, predicates, corpus/, tools/, reports/ outside stage — read only.
