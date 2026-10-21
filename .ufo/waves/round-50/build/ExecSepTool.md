# ExecSepTool — round 50, claim Ca (separability checker), with L1 refinements

Seat: ChousaR27R2.ExecSepTool-4. Base: 4ad26836552462d28a946ca3b067cab0b5ce3532.
Clone: `.ufo/waves/round-50/work/ExecSepTool` (only `tools/check-claim-separability.py` is new; nothing else changed).
Patch: `.ufo/waves/round-50/patches/ExecSepTool.patch` (same path as before the refinement; 1,236 lines; `new file mode 100755`; `a/` `b/` prefixes; clone HEAD verified as 4ad2683).
Tool: 1,230 lines, sha256 `3ce3de9cf707f4bee98595d8cef08ade98a8b9f0a8a6219f03b6503ffe7f8043`.

## Result

- Tool implements the Shared contract (Ca) plus the eight L1 refinements from the IRC message. The earlier draft is fully replaced.
- `python3 -B tools/check-claim-separability.py --selftest` in the clone: **56/56 checks passed, exit 0**, 2.91 s wall. Temporary repos only; the lane was not written.
- Stdlib only. Lane reads go through one `git -C LANE cat-file --batch` process. Refinement 7 adds one other git class: `git clone --shared` from `--root` into a temp dir, followed by `checkout --detach` inside that temp clone, only for `needs_git` units.

## Refinement map (L1 item to code)

| L1 | Behaviour | Anchor (tool line) |
|---|---|---|
| 1 scan added lines only | `unit.added[rel]` = lines of the landed file not present as a line in the base blob; absent-at-base = all lines | `_load_units` 469–488 |
| 2 base-existing paths are not dependencies | base presence via `cat-file --batch` on `<base>:<path>` (MissingObject = absent); only `name_paths()` (absent at base) produce name hits | `_base_object` 223; `name_paths` 366–368; `_static_findings` 616 |
| 3 export novelty, exit 2 | each export regex must match no line of base bytes in its own unit's lands | `_check_novelty` 491 |
| 4 overlap finding | same path in two units' lands → `SEPARABILITY_OVERLAP X/Y path` (X earlier in manifest), exit 1 | `_overlap_findings` 637 |
| 5 role `record` | role validated; records never scanned as dependers (`continue` at 619); claims citing a record's exports or new paths are findings; records carry no acceptance (exit 2) | `_parse_manifest` 371–420 |
| 6 `tree: "WORKTREE"` | lands read from the filesystem under `--root` (default `--lane`) via lstat; absent → exit 2 | `_read_worktree` 451; root default in `main` |
| 7 `needs_git` | acceptance runs in `git clone --shared --no-checkout ROOT work` + `checkout --detach <base oid>`, overlays applied; any git, clone, checkout or launch failure → `SEPARABILITY_UNEVALUATED <reason>` on stdout, exit 2; `needs_git` without acceptance → exit 2 | `_git_counterfactual` 582; `main` 1218–1220 |
| 8 output | finding lines `sorted()`, then `SEPARABILITY: <n> findings`; counts moved to a stderr `SEPARABILITY_NOTE` line so stdout ends with the summary; OK/FAIL lines retired | `report` 712–717 |

Mandated selftest controls, each present and passing:
- inline-URL-only citation of another unit's export → exit 1 (`negative: an inline-URL-only citation ...`)
- base-existing path mention → no finding (`positive: a base-existing path mention ...`)
- back-reference (Y's used-by names X's new file) → `S->C` finding (`negative: a back-reference ...`)
- manifest without schema → exit 2 (`malformed: manifest without schema`)

## Selftest evidence

Final line, verbatim: `selftest: 56/56 checks passed - negative controls (...), positive controls (...) and malformed or unevaluable input (exit 2)`.
Breakdown: 11 positive (exit 0), 15 negative (exit 1), 30 malformed or unevaluable (exit 2).

- Every negative asserts the exit code and the exact finding text. Where a reverse direction could plausibly appear, the control also asserts its absence (for example `S->C` absent in the inline-URL case, `C->S` absent in the back-reference case). The overlap and sorted-output controls assert the complete finding list.
- Dynamic controls assert the `acceptance_runs` count for the positive and attribution cases (`acceptance_runs=1`, `acceptance_runs=2`); the timeout and T-attribution negatives assert the finding text only.
- Each malformed case asserts exit 2 and the specific diagnostic on stderr (or `SEPARABILITY_UNEVALUATED` on stdout), so a generic internal fault cannot pass as an input error.
- The `needs_git` positive asserts `.git` exists in the acceptance cwd, which only the clone path satisfies.
- These controls are designed to discriminate the refined semantics (for example, a base line citing S031 must not flag). I did not mutation-test them, so that discrimination is asserted by design, not measured.

## Decisions for L1 to rule on (not in the contract text)

1. A path nested under another unit's path (`a` vs `a/b`) stays exit 2: one path cannot be both a file and a directory. Refinement 4 covers only equal paths.
2. When two units share a path, the repair overlay applies X then Y, so Y's bytes win. The overlap finding already yields exit 1.
3. `UNEVALUATED` goes to stdout, as the IRC says "print"; all other input errors stay on stderr.
4. Export and name regexes match per line; a multi-line pattern cannot match.
5. `--root` is a new option. `tree: "WORKTREE"` is a reserved literal. WORKTREE reads follow symlinked ancestors (read-only, no containment check).
6. Exports are not checked against the exporting unit's own added lines. An export that matches none of its own bytes is silent, not an error.

## Discrepancy to flag

- The round-50 `claims.json` after-required line says "run on reports/round-50/claims.json exits 0". That file is the claim ledger: it has no `schema`, `tree`, `exports` or `role`. Under the contract the tool exits 2 on it, by design. Exit 0 on claims.json is not reachable without a derived manifest, which I did not produce.
- The after-required fixture check (`r49-fixture.json` exits 1 naming C->S) depends on `ExecSepFixture`'s file, which is not present at base. It was not run.

## Not run (explicit)

- No run against the frozen r49 fixture or against real lane history (tree commits, real exports).
- No timing on the 77 MB, 3,481-file base, nor on `needs_git` clones.
- No mutation testing of the controls, no `git apply --check` of the patch, no QUALITY criterion 7 work (not this seat).

## Risks and residual limits

- Acceptance argvs are program executions from the manifest. `shell=False` still runs them; manifests are trusted planner input.
- Timeouts count as failures (exit 1, `timeout after Ns`).
- `cat-file` was exercised on plain selftest repos only, not on the jj-colocated lane.
- A unit that rewrites an existing base line so that the new line cites another unit's new export is flagged, because the rewritten line counts as added.

## Tooling record

- No installs or updates. Used the existing python3 3.14.8 and git 2.56.0. No pacman, uv, npm or cargo activity.
- Directories `.ufo/waves/round-50/work/` and `patches/` were created with `mkdir -p`, as the assignment specifies.

## Checks for the main agent to run

1. `python3 -B tools/check-claim-separability.py --selftest` in the applied tree: expect 56/56, exit 0.
2. `git apply --check` of `.ufo/waves/round-50/patches/ExecSepTool.patch` against 4ad2683.
3. After the fixture lands: `python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json`: expect exit 1 with a `SEPARABILITY_DEPENDENCY C->S` line.
