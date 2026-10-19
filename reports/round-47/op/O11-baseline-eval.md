# O11 — baseline-evaluation verifier: the gate measures committed bytes, not the worktree

- Seat: `O11` | role verifier | claim **O** (operability) | round 47, loop 2
- Out path: `reports/round-47/op/O11-baseline-eval.md` (the only file this seat writes under `reports/round-47/`)
- Mission: `reports/round-47/targets.json:43` — "confirm the gate evaluates against git show at baseline_commit, NOT the worktree — a claim whose `before` is true in the worktree but false at baseline must flag."
- Contract: `reports/round-47/claims.json:37-47` (claim O; the `after_required` at `:41`, thresholds at `:47`)
- Baselines under test: `7ceff59` (r43's baseline, `reports/round-43/claims.json:7`) and `6e9a30d` (r47's baseline, `reports/round-47/claims.json:7`)
- Cut: **2026-10-19T19:29:44Z** (`date -u +%Y-%m-%dT%H:%M:%SZ`); first cut 19:20Z, re-measured after removing a non-filed `- verified-at:` line from the capability fixture so it matches `op/O02-probe-registry.md` §4 exactly
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Boundary: no filed byte edited; nothing staged under `corpus/`; no `reports/round-*/run-validation.py` executed; no git mutation, commit, push, install, or network. All scratch is under `.scratch/o11/`; the only durable write is this file.

## 1. Verdict

**The baseline-evaluation property holds: every measurement route tested reads the Git object store at `baseline_commit`, and the worktree is unreachable by design and by measurement.** A claim whose `before` is true in the worktree but false at `7ceff59` is flagged **STALE, exit 1**; the identical check evaluated against the live files is FRESH. The reverse claim stays FRESH at baseline and is STALE against the worktree. An empty-worktree clone inverts both verdicts, which no worktree-reading gate could survive.

This is a **seat-level PASS on the property, not a pass on claim O's deliverable**. The durable `tools/harness/claims-freshness.py` is still absent at HEAD, the assembled fenced parts have no `main()` or `--selftest`, and the parts do not compose without adapters (§8). The O claim's `after_required` (`claims.json:41`) therefore remains unproven; this seat verifies the method, not the landing.

| question this seat was asked | answer | measured evidence |
|---|---|---|
| Is file content read from the baseline commit? | **yes** | `Baseline.sha256(extractor)` = `d8d23a26…` = `git show 7ceff59:… \| sha256sum`; §7 |
| Is there any worktree fallback? | **no path found** | `Baseline` has no worktree constructor (`part1.py:447`); `at="worktree"` is `GateInputError`; §6 |
| Does a worktree-true / baseline-false premise flag? | **yes, STALE exit 1** | W1; §3 |
| Does a worktree-false / baseline-true premise stay fresh? | **yes, FRESH exit 0** | W3; §3 |
| Do untracked r47 files leak into a `6e9a30d` evaluation? | **no** | U1: baseline false (STALE) although the file exists on disk; §3 |
| Does an empty worktree change any verdict? | **no** | clone C1 FRESH / C2 STALE, exit 1; §4 |
| Does the r43 regression come out O stale, C stale, Ca fresh? | **yes, exit 1** | §5 |
| Is the assembled artifact runnable as filed? | **no** | no CLI/selftest; six integration seams; §8 |

**Axis judgment for this seat:** operability is not harmed and the baseline property is demonstrably real, but the axis cannot be called *improved* until the durable path exists. Candidate verdict from this fragment: **`unprovable-but-better`**, matching `op/O12-scribe.md:30` and `op/O12-scribe.md:25` (O11 listed absent at that cut).

## 2. What was tested, and how

The three filed fenced bodies were extracted byte-for-byte and checked against their own pins:

| part | source | lines | SHA-256 | pinned at | match |
|---|---|---|---|---|---|
| 1/3 core + `Baseline` | `op/O01-tool-core.md` §8 | 633 | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` | `O01-tool-core.md:13-14` | **yes** |
| 2/3 probe registry | `op/O02-probe-registry.md` Appendix A | 967 | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` | `O02-probe-registry.md:1224` | **yes** |
| 3/3 verdict + exits | `op/O03-verdict-contract.md` §6 | 487 | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` | `O03-verdict-contract.md:84` | **yes** |

Assembly: plain concatenation of the three bodies **fails** (`from __future__` appears three times; see seam S1, §8). The verifier's assembled module strips the two duplicate future imports and is importable; its SHA-256 is `15f6b23bab49377cb14b345e79b5d18db5cd93fe69f2005475ef1504201a5315` (80,051 bytes). It has no `main()` and no `selftest()` — `hasattr(gate, "main")` → `False`, `hasattr(gate, "selftest")` → `False`.

Two views are used for every claim:

1. **`part1.Baseline`** — `git ls-tree -r -z --full-tree <commit>` for the path index; `git cat-file --batch` for blob bytes; `read`, `sha256`, `grep`, `glob`, `file_count` all route through that index (`part1.py:446-582`). No `open()` on repo paths.
2. **`WorktreeTree`** — a verifier-only counterfactual that reads the live files, including untracked ones (`.scratch/o11/verify_o11.py:57-107`). It is never passed to the durable tool; it exists solely to show what a worktree-reading gate would have said.

Fixtures are in `.scratch/o11/fixtures/`; the harness is `.scratch/o11/verify_o11.py`; its full JSON is `.scratch/o11/verify_o11.json`. The two views are fed the **same declared check objects**; only the `tree` argument differs.

## 3. The discriminator matrix — the seat's central evidence

Each row is a separate **verifier fixture**, not a round-47 claim; the fixtures exist only to make the two views disagree, so the verdict difference is attributable to the measurement source and nothing else. "baseline exit" is a one-claim `build_report` so the exit is attributable to that claim. The worktree column is the counterfactual measurement of the same check.

| id | before (abridged) | probe | at | baseline measured → verdict / exit | worktree measured → verdict |
|---|---|---|---|---|---|
| **W1** | "a durable basename-couples resolver exists at `tools/harness/basename-couples-resolver.py`" | `path_present` `expect=true` | `7ceff59` | `False` → **STALE / 1** | `True` → **FRESH** |
| **W3** | "no durable basename-couples resolver exists at …" | `path_absent` `expect=true` | `7ceff59` | `True` → **FRESH / 0** | `False` → **STALE** |
| **U2** | "the r43 per-finding disposition is on record at `reports/round-43/calib/dispositions-r38-r39.json`" | `path_present` `expect=true` | `7ceff59` | `False` → **STALE / 1** | `True` → **FRESH** |
| **W2** | same as W1 | `path_present` `expect=true` | `6e9a30d` | `True` → **FRESH / 0** | `True` → **FRESH** |
| **U1** | "the r47 O-claim tool-core fragment is filed at `reports/round-47/op/O01-tool-core.md`" | `path_present` `expect=true` | `6e9a30d` | `False` → **STALE / 1** | `True` → **FRESH** |
| **SHA7** | "SCORECARD.md has the r43-era digest" | `sha256_eq` `expect=e2ca0e17…` | `7ceff59` | `e2ca0e17…` → **FRESH / 0** | `c91bdac0…` → **STALE** |
| **CNT** | "no O-claim fragments exist under `reports/round-47/op`" | `count_eq` `expect=0` | `6e9a30d` | `0` → **FRESH / 0** | `17` → **STALE** |
| **GRP** | "no O01 tool-core H1 exists under `reports/round-47`" | `grep_absent` `expect=true` | `6e9a30d` | `True` → **FRESH / 0** | `False` → **STALE** |
| **TOP** | "the lithic register is owned" | `topic_owner_absent` `expect=false` | `7ceff59` | `False` → **FRESH / 0** | `False` → **FRESH** |

How to read the first row, which is the mission verbatim:

- W1's `before` is **true in the live worktree**: `tools/harness/basename-couples-resolver.py` exists, 21,732 bytes, SHA-256 `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`.
- W1's `before` is **false at `7ceff59`**: `git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py` → exit 128, "exists on disk, but not in '7ceff59'".
- The gate flags it **STALE, exit 1**; the worktree counterfactual says **FRESH**. That is the required discrimination, measured rather than asserted.

U1 is the untracked-file control: `reports/round-47/op/O01-tool-core.md` was created by a sibling this round and is not in `6e9a30d`; a worktree gate reads it and passes, the baseline gate ignores it and flags. SHA7/CNT/GRP extend the same proof to the byte, count, and grep probes rather than only path membership.

TOP is deliberately a non-discriminating consistency row (the lithic owner exists at both views); it shows `topic_owner_absent` reads partition headers through `tree.glob`/`tree.read`, not the live corpus, and the r43 C result in §5 uses the same probe to produce the real ownership contradiction. Worktree values are observations at the cut; CNT counts files created by other seats during the wave and is expected to grow.

## 4. Empty-worktree clone: the strongest control

A `--no-checkout` clone shares the object store with the lane repo but has **zero files in its worktree**:

```
$ git clone --shared --no-checkout --quiet . .scratch/o11/clone-no-worktree
$ ls -a .scratch/o11/clone-no-worktree
.  ..  .git
$ git -C .scratch/o11/clone-no-worktree rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
```

Two claims use the **same path with opposite polarity** at the same baseline `6e9a30d`:

| claim | check | baseline `6e9a30d` | empty worktree | baseline verdict | worktree counterfactual |
|---|---|---|---|---|---|
| **C1** | `path_present` resolver `expect=true` | `True` | `False` (no file) | **FRESH** | STALE |
| **C2** | `path_absent` resolver `expect=true` | `False` | `True` (no file) | **STALE** | FRESH |

```
$ python3 -B .scratch/o11/clone_check.py
clone empty worktree: True
baseline: 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
  C1  path_present measured=True   expect=True  holds
  C2  path_absent  measured=False  expect=True  mismatch
  [C1] fresh
  [C2] stale
run exit: 1
CLONE-CHECK: PASS
```

A worktree-based gate would have to invert both rows; it cannot. The clone's worktree has no bytes to fall back to, so C1's FRESH can only come from `git cat-file` on the shared object store. Artifact: `.scratch/o11/clone_check.json` (SHA-256 `d9c1ee7520944623fc9c08e4019f606b6de53712602a9823b6b182daae6382e9`).

## 5. The real regression: r43 O stale, C stale, Ca fresh

The r43 overlay was re-run through the assembled parts at `7ceff59` (capability target and count/topic/path checks copied from `op/O02-probe-registry.md` §5.2 and Appendix B; the capability fixture is the wrapped `- couples:` field with `refs=4`):

| claim | clause | measured | expect | raw status | verdict |
|---|---|---|---|---|---|
| **O** | "no durable instrument implements the r39 basename-couples policy" | `True` (1/7 candidate: `tools/harness/couples-reference-extractor.py`) | `False` | mismatch | **STALE** |
| **C** | "lithic slot named but unbuilt since r42's C01/C04 collision…" | `False` (owner exists) | `True` | mismatch | **STALE** |
| **C** | "myth-symbol 26" | `26` | `26` | holds | (within C) |
| **C** | "total 223" | `223` | `223` | holds | (within C) |
| **Ca** | "have no per-finding disposition on record" | `True` (artifact absent at baseline) | `True` | holds | **FRESH** |

```
[O] stale  counts={'holds': 0, 'contradicted': 1, 'not_evaluated': 0}
[C] stale  counts={'holds': 2, 'contradicted': 1, 'not_evaluated': 0}
[Ca] fresh counts={'holds': 1, 'contradicted': 0, 'not_evaluated': 0}
run exit=1
```

The candidate list for O is baseline-only: `couples-reference-extractor.py` is the witness at `7ceff59`; the successor `basename-couples-resolver.py` does not exist there and is not a candidate. A literal-path gate would pass r43 O because the successor path is absent at baseline (`git cat-file -e` → 128); the capability probe does not. This reproduces `reports/round-43/review/R01-review.md:389-394` and `reports/round-47/review/R02-review.md:183-185` without reading their summaries for the measurements.

C is stale **only** on ownership: both counts hold. That is the shape the r44 review reported (`reports/round-44/review/R01-review.md:228-231`), and it is why one contradiction must dominate a partially true claim (O03 §2).

Caveat on Ca: the single `path_absent` check is a *trivial* baseline control (the disposition file is r43's own output, so it cannot exist at r43's baseline). It demonstrates baseline scoping, not that the gate avoids over-firing; `cross/X01-trades.md:135-153` makes the same point. O06's r44 fixture is the substantive fresh control, and that is outside this seat.

## 6. Baseline resolution and the absence of a worktree mode

```
HEAD      6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
short_sha 7ceff59a0216a8ea21ee43262d9fc72abf770cee
tree_id   GateInputError   (a tree object is not a commit)
blob_id   GateInputError   (a blob object is not a commit)
missing   GateInputError   (no-such-rev-o11)
```

`open_claims(..., at=...)` is the only override, and it accepts **another commit only**:

```
'worktree' -> GateInputError: baseline_commit 'worktree' does not resolve to a commit …
'WORKTREE' -> GateInputError: same
''         -> 7ceff59a0216 (falls back to the declared baseline)
None       -> 7ceff59a0216
'HEAD'     -> 6e9a30dca8bf, deviation={'declared': '7ceff59', 'used': 'HEAD',
              'reason': '--at override (measurement is still a committed tree, never the worktree)'}
```

`resolve_commit` runs `rev-parse <rev>^{commit}` and then `cat-file -t`, requiring `commit` (`part1.py:173-190`). `Baseline.__init__` has no worktree branch (`part1.py:446-470`); its docstring says "The worktree is unreachable by design" (`part1.py:447`). `_git` strips every inherited `GIT_*` variable, sets `GIT_OPTIONAL_LOCKS=0`, `GIT_NO_REPLACE_OBJECTS=1`, `LC_ALL=C`, and invokes `git --literal-pathspecs -C <root>` (`part1.py:118-143`) — so a caller's `GIT_WORK_TREE`, `GIT_DIR`, or replace refs cannot redirect measurement.

**"via git show" is satisfied by an equivalent object-store read, not literally by `git show`.** Content comes from `git cat-file --batch` over the blob oid that `ls-tree` returned for the commit; the measured SHA-256 is byte-identical to `git show <commit>:<path>` (§7), so the contract's intent — re-derive from the named commit, never the worktree — is met. A grep for `git show` in part 1 finds no content call; that is a naming detail, not a worktree fallback.

Static audit of the assembled bytes:

- `open(` occurs twice, both in `_materialize_fixture` / candidate writing under a fresh temp dir (`part2.py` capability probe), never on a repo path.
- `Baseline` content reads are `cat-file --batch` only; `files()` is `ls-tree`, `sha256()` hashes the raw blob (`part1.py:539-540`).
- No `os.getcwd()`, no `Path.cwd()`, no relative file open in part 1.
- The assembled module contains the string "worktree" only in comments/docstrings and the `deviation` reason; there is no code branch on it.

## 7. Byte identity and determinism

| measurement | value |
|---|---|
| `Baseline(7ceff59).sha256("tools/harness/couples-reference-extractor.py")` | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| `git show 7ceff59:tools/harness/couples-reference-extractor.py \| sha256sum` | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| `sha256sum` of the worktree file | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` (identical here) |
| `Baseline(7ceff59).sha256("SCORECARD.md")` | `e2ca0e1747deb036388c9d0ce6ca16424ee30f7595fb77b6857a0c9b8e694a1d` |
| `sha256sum SCORECARD.md` (worktree/HEAD) | `c91bdac01b56312ce4ad8bf250f47e7ffffd370a1a0062ee1a58335245afb927` |
| `Baseline(...).scope` | `"baseline"` |

The extractor happens to be identical in both views; the SCORECARD pair is the discriminating byte test (SHA7 above). Determinism: the same claims doc run twice yields the same `decision_sha256` and the same exit 1 (`verify_o11.json` → `results.determinism.identical = true`).

## 8. Integration seams found while verifying (measured, not stylistic)

These are defects in how the filed parts compose, not in the baseline property. They matter to the integrator because the O claim's `after_required` requires a *durable, runnable* tool.

**S1 — plain concatenation does not compile.** O01 says assembly is plain concatenation (`O01-tool-core.md:23`), but parts 2 and 3 each repeat `from __future__ import annotations`.

```
$ cat part1.py part2.py part3.py > plain_concat.py
$ python3 -m py_compile plain_concat.py
SyntaxError: from __future__ imports must occur at the beginning of the file  (line 694)
```

The verifier strips the two duplicate lines; the assembled digest in §2 covers that. The integrator must either strip them or reorder the future import once.

**S2 — part 2 and part 3 disagree on clause status and polarity keys.** Part 2 emits `status: holds | mismatch | could-not-evaluate` and the key `expect` (`O02-probe-registry.md:687`); part 3 accepts only `HOLDS | CONTRADICTED | NOT_EVALUATED` and reads `expected` (`O03-verdict-contract.md:138`, `part3.py:86-104`). Raw pass-through, measured:

```
raw='mismatch' -> verdict could-not-evaluate
  reason: evaluator-contract-violation: status 'MISMATCH' is not one of HOLDS/CONTRADICTED/NOT_EVALUATED
  expected: null
adapted -> stale
```

Without the one-line adapter, **every contradiction becomes could-not-evaluate (exit 3), so the positive regression can never be green**. This is the difference between the method working and the assembled tool working.

**S3 — part 1's `Check.as_dict()` emits a key part 2 rejects.** `expect_source` is part of the core `Check` dataclass (`part1.py:246-264`), but part 2's strict validator allows only `id, clause, probe_kind, target, expect, evidence_command, note` (`O02-probe-registry.md:577`). `validate_check(check.as_dict(), …)` → `CheckError: check has unknown key(s): expect_source`. The verifier pops it in scratch; the durable assembly must drop it or add it to the allowed set.

**S4 — the parser accepts boolean polarity only, so two of the seven probes cannot be loaded.** `_check_entry` requires `isinstance(expect, bool)` (`part1.py:292-318`), while part 2 declares `int` for `count_eq` and a 64-hex `str` for `sha256_eq` (`O02-probe-registry.md:555-563`). Measured:

```
count_eq  REJECTED: GateInputError before_checks[0] expect is not boolean
sha256_eq REJECTED: GateInputError before_checks[0] expect is not boolean
```

This blocks r43 C (two `count_eq` clauses, 26 and 223) and any digest claim **before any probe runs**. The §5 r43 regression and the SHA7/CNT rows were therefore measured by calling part 2 directly over `Baseline`, not through `load_claims`. The verifier did not patch the filed bytes; this is a finding for the integrator.

**S5 — the fenced parts have no CLI and no selftest.** `hasattr(gate, "main")` → `False`; `hasattr(gate, "selftest")` → `False`. O01 §1 says part 3 owns the argparse entry point (`O01-tool-core.md:20`), but the O03 fence ends at `render_human` (`O03-verdict-contract.md:574`); O04 supplies a selftest body that is not in any tool. `tools/harness/claims-freshness.py` is absent: `ls tools/harness/claims-freshness.py` → no such file. `python3 tools/harness/claims-freshness.py --selftest` cannot be run, so the O claim's first counting command (`claims.json:43`) is not executable.

**S6 — O05's demo overlay does not validate against O02's capability schema.** O05's `target` is `{"capability": "couples_census", "scope": "tools/**.py"}` (`op/O05-r43-demo.md:112,119`); O02's capability target requires `globs, exclude_globs, argv, fixture, success_regex, timeout_s, max_candidates` and rejects unknown keys. Measured:

```
O05 target REJECTED: CheckError capability_present target has unknown key(s): capability, scope
```

The demo's *verdicts* reproduce (§5), but its filed artifact would be rejected by the tool it demonstrates unless the integrator adapts one side. This is a schema-drift defect between two O seats, not a baseline defect.

## 9. Residual limits and what this seat did not verify

- **`capability_present` is the one route where baseline code can see the worktree.** It writes baseline candidate blobs and the fixture under a temp dir and executes them with `cwd=<temp>`, `-I -B`, a timeout, and no shell; O02 declares that this is not an OS sandbox and that a tool walking above the fixture can read the worktree (`O02-probe-registry.md:66,242`). For the r43 witness the candidate list itself comes from `tree.glob`, so *selection* is baseline-only; the residual risk is execution-time reads by trusted repo code, not a worktree fallback in measurement.
- **The claims file is read from the worktree by design.** `load_claims` reads the JSON at the path given (`part1.py:349-355`); only evidence is baseline-scoped. This is necessary because `reports/round-43/claims.json` does not exist at `7ceff59` (`op/O05-r43-demo.md:93`). The report should not be read as "nothing in the process touches the worktree".
- **Tag and annotated-tag resolution** were not re-tested here; O09 measured the prototype's tag defects (`op/O09-traps.md:274-337`). This seat tested `HEAD`, a short sha, a tree id, a blob id, a missing rev, and the literal `worktree` string.
- **Exit-code conformance** (0/1/2/3, malformed cases) is O10's seat; this fragment only reports the exits produced by `build_report` for its own fixtures (0 fresh, 1 stale).
- **Negative control and anti-theater mutation** are O06/O07; this fragment's U1/CNT/GRP are worktree-leak controls, not anti-theater controls.
- **The durable path, `--selftest`, and the filed `calib/` demonstration** do not exist at this cut; `reports/round-47/run-validation.py` was not executed (shared rule), and the integrator owns the post-apply re-run (`V02`, `W01`).

## 10. Commands run (key transcript)

```
$ git rev-parse 7ceff59^{commit} 6e9a30d^{commit} HEAD
7ceff59a0216a8ea21ee43262d9fc72abf770cee
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe

$ for c in 7ceff59 6e9a30d; do
    echo "$c total=$(git ls-tree -r --name-only $c -- corpus/knowledge | grep -c '\.md$') \
myth=$(git ls-tree -r --name-only $c -- corpus/knowledge/myth-symbol | grep -c '\.md$')"; done
7ceff59 total=223 myth=26
6e9a30d total=223 myth=26

$ git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py; echo $?
fatal: path 'tools/harness/basename-couples-resolver.py' exists on disk, but not in '7ceff59'
128

$ sha256sum tools/harness/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64

$ python3 -B .scratch/o11/verify_o11.py        # full matrix, §3/§5/§7
$ python3 -B .scratch/o11/clone_check.py       # empty-worktree clone, §4
```

Artifacts and digests (scratch is not durable; these identify the run):

| path | SHA-256 |
|---|---|
| `.scratch/o11/part1.py` | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` |
| `.scratch/o11/part2.py` | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` |
| `.scratch/o11/part3.py` | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` |
| `.scratch/o11/assembled.py` | `15f6b23bab49377cb14b345e79b5d18db5cd93fe69f2005475ef1504201a5315` |
| `.scratch/o11/verify_o11.py` | `f5d0dbc9f5778523983da89b03ff24da3eab0600972bee4c3122fa31559cfa04` |
| `.scratch/o11/verify_o11.json` | `a6d2328d8e239c52030ee37518d66af00f78146fc522c46c2cdd60f47fe3a791` |
| `.scratch/o11/verify_o11.out` | (console transcript, §3/§5/§7 above) |
| `.scratch/o11/clone_check.py` | `aa3f95a8ddad599c8ab20539974eb6ea17de277624587204f166a98bd8e48462` |
| `.scratch/o11/clone_check.json` | `d9c1ee7520944623fc9c08e4019f606b6de53712602a9823b6b182daae6382e9` |
| `.scratch/o11/fixtures/w-baseline-7ceff59.json` | `e86cef9c0453bd987c1c97471cf5cf01e503597e2a4ae5e806867244464f503b` |
| `.scratch/o11/fixtures/w-baseline-head.json` | `1ea92f4c1b1a90722729f38912308d855acf941f6c206f7b726db01266f507d3` |

## 11. Handoff

- **For the integrator (W01/O12):** the baseline property is proven and needs no code change; the blockers are S1-S6. In particular, do not land the assembled bytes without (a) one future import, (b) a part-2→part-3 status/key adapter, (c) removal of `expect_source` at the seam, (d) typed `expect` support in the parser, (e) a CLI plus the O04 selftest, and (f) a reconciled O05 capability target. Until (a)-(f), `--selftest` and the r43 counting command cannot run, and a stale claim can surface as exit 3 rather than exit 1.
- **For V02 / the post-apply verifier:** re-run this fragment's W1/W3/U1/SHA7/CNT/GRP matrix against the durable path; the empty-worktree clone control is the cheapest end-to-end check that no fallback was introduced. The expected results are in §3 and §4 verbatim.
- **For R02:** this fragment supplies the "baseline-vs-worktree discriminator" R02 asked for (`review/R02-review.md:341`); the answer is PASS on the property, with the seam caveats above.
- **Unproven by this seat:** the durable tool, its selftest, its exit-code contract in a real CLI, the negative control and anti-theater mutation, and any post-landing re-run. Those remain `could-not-evaluate` from this fragment's evidence.
