BREAKS: the frozen separability manifest commits `BASE_PLACEHOLDER` as its `base`, so the canonical command exits 2 (`SEPARABILITY_INPUT_ERROR`) before evaluating anything — the round-60 separability control is not operable at the freeze, never emits a verdict, and emits no dependency-attribution line at all.

# ReviewSeparabilityA3 — falsify report (round 60 attempt 3, wave 2)

Seat `KotodamaR60A3.ReviewSeparabilityA3` (leaf, falsify). Lane tip = freeze = `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse main`). All work in the sandbox clone `/fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/lane` (clone at tip; env `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` unset). No installs, no upgrades, no pacman. No LSP (not applicable to a tool run). All python runs with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`; no `__pycache__` created; no process left running.

## 1. The requested re-run (twice, second under `unshare -rn`)

Command, run 1 (cwd = sandbox clone root):

```
cd /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/lane && env PYTHONDONTWRITEBYTECODE=1 timeout 900 python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json > /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run1.out 2>&1; echo RUN1_EXIT=$?
```

Full output (`run1.out`, 143 bytes):

```
SEPARABILITY_INPUT_ERROR base 'BASE_PLACEHOLDER' does not name a commit in lane '/fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/lane'
RUN1_EXIT=2
```

Command, run 2 (same, under a new network namespace):

```
cd /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/lane && env PYTHONDONTWRITEBYTECODE=1 unshare -rn timeout 900 python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json > /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run2.out 2>&1; echo RUN2_EXIT=$?
```

Full output (`run2.out`, 143 bytes):

```
SEPARABILITY_INPUT_ERROR base 'BASE_PLACEHOLDER' does not name a commit in lane '/fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/lane'
RUN2_EXIT=2
```

Byte-identity check:

```
cmp -s /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run1.out /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run2.out; echo CMP_EXIT=$?; wc -c /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run1.out /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run2.out; sha256sum /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run1.out /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run2.out
```

Full output:

```
CMP_EXIT=0
143 /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run1.out
143 /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run2.out
286 total
e80a1dfc0f92e756a8aa9145a411ce56ee40a5f28fa5c5a39275311a0a1c5048  /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run1.out
e80a1dfc0f92e756a8aa9145a411ce56ee40a5f28fa5c5a39275311a0a1c5048  /fast/scratch/hyaku/kotodama-r60a3/ReviewSeparabilityA3/run2.out
```

Control run in the real lane (read-only; same result, lane path differs):

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && env PYTHONDONTWRITEBYTECODE=1 timeout 900 python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json; echo REAL_EXIT=$?
```

Full output:

```
SEPARABILITY_INPUT_ERROR base 'BASE_PLACEHOLDER' does not name a commit in lane '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
REAL_EXIT=2
```

Answers to the item's two questions:

- **Byte-identical: yes.** Both runs produced the same 143 bytes (`cmp -s` exit 0; identical sha256 `e80a1dfc…`), including when run inside `unshare -rn` (a fresh network namespace with no route). The failure is fully deterministic and independent of the network.
- **Does any line attribute a dependency the counter cannot have? No — the run attributes no dependency at all.** The only line is an input-error diagnostic. There is no `SEPARABILITY_DEPENDENCY` line, no `SEPARABILITY_NOTE`, no verdict. The counter `reports/round-60/accept-d.py` has no network leg: its only network-adjacent import is `urllib.parse` (URL decoding/parsing used to *detect* fetch-like calls in seat transcripts, `FETCH_VERB` at accept-d.py:405); it performs no network I/O. The checker `tools/check-claim-separability.py` imports only `argparse, contextlib, dataclasses, io, json, math, os, re, shutil, stat, subprocess, sys, tempfile`; its only git use is read-only `git cat-file --batch`. Identical output with and without a network namespace confirms no leg depends on the network.

## 2. Why the command cannot evaluate: the frozen manifest is unrunnable

- At the freeze, `reports/round-60/separability-manifest.json` declares `"base": "BASE_PLACEHOLDER"` (blob sha256 `1a7bf22cff6b545e1ca4e6c3eaaaf1360578e4f4765b888b1d3a43bc27875891`).
- The checker treats `base` as a commit revision (`_parse_manifest` → `_rev` passes the literal string; `_commit_pair` resolves `BASE_PLACEHOLDER^{commit}` through `git cat-file --batch` and raises `InputError` — `check-claim-separability.py:204-213`), which `main` prints as `SEPARABILITY_INPUT_ERROR` and exits 2 (input error, never a verdict).
- A repo-wide grep finds `BASE_PLACEHOLDER` only in the manifest and in wave-1's own report (below). There is no committed substitution mechanism anywhere — the only "fix" is wave-1's uncommitted sandbox edit.
- Even with a real base, the instrument cannot score at the freeze: the D unit lands 76 outputs of the later support wave (`.ufo/waves/round-60/support/registry.json`, `planted-key.json`, `planted-rows.md`, the 24 seat reports, 24 packets, 24 transcripts, plus `reports/round-60/planted-key.sha256`), none of which exist in the freeze commit's tree (`git ls-tree -r --name-only 47f27bd… -- .ufo/waves/round-60/support` → empty). Wave-1 verified the same: with base patched to `14e6413820d482913f723432b62d566967ccd1a6`, the run exits 2 on the first missing land (`registry.json`).

Result: the round-60 separability control produces **no verdict** at the freeze. There is no recorded round-60 `SEPARABILITY:` receipt line anywhere in `reports/round-60/` (grep for `SEPARABILITY_DEPENDENCY|SEPARABILITY:|SEPARABILITY_NOTE|SEPARABILITY_UNEVALUATED|SEPARABILITY_INPUT_ERROR` in `reports/round-60/` → no matches). The claims.json annotation "round 60's separability run uses a counter with no network leg" (records_not_claims item 3) cannot be evidenced by the declared instrument: the instrument does not run.

## 3. Wave-1 comparison

Wave-1's `ExecSeparabilityA3.md` (`.ufo/waves/round-60/w1-a3/`, lane rev `14e64138…`) already reported exactly this shape: "the wave-1 result for the frozen manifest is **not evaluable**, deterministically, for a shape reason"; its untouched-placeholder run gave the same `SEPARABILITY_INPUT_ERROR base 'BASE_PLACEHOLDER' …` and exit 2, and its patched-base run failed on the absent `registry.json`. My independent reproduction confirms their findings byte-for-byte in content and exit code, and adds that the two canonical runs are byte-identical including under `unshare -rn`, and that the prem emits no dependency-attribution line (so nothing "attributes a dependency the counter cannot have" — nothing is attributed at all). Wave-1's honesty is confirmed; the defect is in the L1-produced frozen artifact.

## 4. Findings (by severity)

1. **[BREAKS] The frozen separability manifest is unrunnable.** `base` is the literal `BASE_PLACEHOLDER` at the freeze; the checker resolves it as a commit name and exits 2 with `SEPARABILITY_INPUT_ERROR` deterministically (verified: twice in the sandbox clone at the tip — byte-identical, sha256 `e80a1dfc…` — plus once in the real lane; all exit 2). No committed mechanism fills the placeholder. The command named in claims.json (`python3 -B tools/check-claim-separability.py reports/round-60/separability-manifest.json`) therefore cannot evaluate the claim at the freeze: no findings, no verdict, no receipt.
2. **[BREAKS] The control cannot be scored at the freeze even with a fixed base.** The D unit's declared lands include 76 files produced by the later support wave (registry, packets, reports, transcripts, `planted-key.sha256`), all absent from the freeze commit's tree; the tool reads WORKTREE units strictly and exits 2 on the first missing land. Wave-1 measured this with base = `14e64138…` (exit 2, `registry.json` absent); the freeze commit tree confirms no `.ufo/waves/round-60/support/` file exists at `47f27bd…`.
3. **[Confirming, not breaking] Determinism and offline operation hold.** The two canonical runs are byte-identical (`cmp -s` exit 0, identical sha256), including under `unshare -rn` with no route; the counter and the checker contain no network I/O. No output line attributes a dependency of any kind — so in particular no line attributes a dependency the (networkless) counter cannot have.

## 5. Residual risk / verification gaps

- The static-leg (0 findings, no static dependency) and dynamic-leg results reported by wave-1 were derived from wave-1's *constructs* (a patched manifest with reduced lands), not from the frozen instrument; I did not re-run those constructs. They are not the declared instrument and must not be pasted into any claim score as a separability receipt.
- The freeze precedes the data/support wave; if the orchestrator intends to fill `base` and run the control after the support wave lands, that mechanism is not committed anywhere at the freeze — the frozen artifact as-is remains non-evaluable until then (and, per finding 2, still needs the support lands present).
- Worktree caveat (from the tool's own selftest semantics): WORKTREE units scan uncommitted bytes; at scoring time the worktree must equal the intended commit.
