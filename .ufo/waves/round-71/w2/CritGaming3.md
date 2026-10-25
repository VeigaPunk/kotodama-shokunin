# CritGaming3 — round 71 wave 2 — Attack D (GIT_DIR / no-git guard)

Seat: falsify, leaf. Target: `reports/round-71/accept-d.py`
(sha256 `459cfa9da53fe3c4b44cfa5be4f82a2794298cc3b79c7f4e0f330f0977945930`, lane HEAD `14c88d9`).
Lane not written except this file; all runs used `python3 -B`; scratch trees under `/tmp` only.
Tooling installs/updates: none.

## Verdict

| Leg | Result |
|---|---|
| Assigned: `GIT_DIR` pointing at a missing path inside the lane gives `COULD-NOT-EVALUATE (git unavailable: ...)` and exit 2, never a craft red | **PASS** |
| Assigned: a real no-git copy prints the exact `SELFTEST: COULD-NOT-EVALUATE (no git)` line, exit 2 | **PASS** (byte-exact via `cmp`) |
| Declared ACCEPT-D-71 predicate (in-repo 2/2 exit 0; declared no-git command exit 2; frozen data predicate 8/8 exit 0) | **PASS** |
| Surface promise "never a craft red" / "an exported tree no longer reports a false red" (V70-6) | **FAIL**: 3 counterexamples below |

## Assigned attack: commands and output (from lane root)

```
python3 -B reports/round-71/accept-d.py --selftest
  → GREEN 8/8, DO-NOTHING FAIL (as required) 1/8, SELFTEST: 2/2, EXIT=0
GIT_DIR=$PWD/.no-such-gitdir python3 -B reports/round-71/accept-d.py --selftest
  → SELFTEST: COULD-NOT-EVALUATE (git unavailable: fatal: not a git repository: '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.no-such-gitdir')  EXIT=2
GIT_DIR=.no-such-gitdir ...            → COULD-NOT-EVALUATE (git unavailable: fatal: not a git repository: '.no-such-gitdir')  EXIT=2
GIT_DIR=$PWD/.git/nope ...             → COULD-NOT-EVALUATE (git unavailable: ...'.git/nope')  EXIT=2
GIT_DIR=<existing empty dir> ...       → COULD-NOT-EVALUATE (git unavailable: fatal: not a git repository: '/tmp/tmp.…')  EXIT=2
GIT_DIR= (empty) ...                   → COULD-NOT-EVALUATE (git unavailable: fatal: not a git repository: '')  EXIT=2
PATH=/nonexistent /usr/bin/python3 -B ... (no git binary)
                                       → COULD-NOT-EVALUATE (git unavailable: [Errno 2] No such file or directory: 'git')  EXIT=2
```

Genuine no-git, using the exact declared counting command:

```
bash -c 'T=$(mktemp -d); tar --exclude=.git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin -cf - . | tar -C $T -xf -; cd $T; python3 -B reports/round-71/accept-d.py --selftest; echo EXIT=$?'
  → SELFTEST: COULD-NOT-EVALUATE (no git)   EXIT=2
(cd $T && python3 -B reports/round-71/accept-d.py --selftest | cmp - <(printf 'SELFTEST: COULD-NOT-EVALUATE (no git)\n')) → BYTE-EXACT
no-git copy + GIT_DIR=$T/.missing      → SELFTEST: COULD-NOT-EVALUATE (no git)  EXIT=2
python3 -B reports/round-69/accept-d.py --root .  → ACCEPT-D-69: PASS legs=8/8  EXIT=0
```

## Counterexamples: the false craft red still happens

The guard `_git_available()` asks `git -C LANE rev-parse --is-inside-work-tree`, which only checks that *some* work tree contains the lane. The frozen selftest actually needs *the lane's* object store to resolve `793f797`. When that commit doesn't resolve, the frozen counter's `except Exception: pass` falls back to the live SKILL.md, so the defect is the same as V70-6.

| # | Environment | Command | Output | Exit |
|---|---|---|---|---|
| X1 | Exported tree (tar `--exclude=.git`) placed inside an unrelated git work tree, e.g. a scratch `git init` dir. This is realistic because `/home/vgpnk/Projects/shokunin` is itself a git repo (`git -C /home/vgpnk/Projects/shokunin rev-parse --show-toplevel` → `/home/vgpnk/Projects/shokunin`), so exporting next to the lane triggers it. | `P=$(mktemp -d); git -C $P init -q; mkdir $P/sub; tar --exclude=.git -C <lane> -cf - . \| tar -C $P/sub -xf -; cd $P/sub; python3 -B reports/round-71/accept-d.py --selftest` | `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)` / `SELFTEST: 1/2` | **1** |
| X2 | Shallow clone without `793f797` | `git clone --depth 1 file://<lane> $S; cd $S; python3 -B reports/round-71/accept-d.py --selftest` (`git cat-file -t 793f797` → `fatal: Not a valid object name`) | `SELFTEST: 1/2` | **1** |
| X3 | `GIT_DIR` set to a valid but foreign repo | `GIT_DIR=/home/vgpnk/Projects/shokunin/.git python3 -B reports/round-71/accept-d.py --selftest` (lane root) | `SELFTEST: 1/2` | **1** |

X1 is the strongest case. It is V70-6 exactly ("exported tree → false red"), and the only difference from the declared no-git leg is *where* the export lands. The declared counting command passes only because `mktemp -d` lands in `/tmp`, which is not inside any repo. In other words, the receipt is green because of where the measurement was run, not because the guard works.

There is also a side note that is not a red. A no-git copy with `GIT_DIR=<lane>/.git` grades `SELFTEST: 2/2` exit 0 against the lane's real store. That result is correct, so I'm recording it only as information.

## Impacted axes

- **Depth / instrument honesty (claim D):** the "never a craft red" guarantee in the claims.json `surface` text and in the counter's own docstring is false in X1–X3. The frozen predicate and target sentences still pass, so the claim is green while overclaiming in its surface text.
- **Provenance:** the `measures-d.txt` no-git leg proves the guard only for exports landing outside any work tree.

## Smallest safe correction (validated on scratch copies only)

Replace the guard so it tests the dependency the selftest actually uses: the lane must be the repo's top level, and the fixture commit must resolve.

```python
def _git_available():
    try:
        top = subprocess.check_output(
            ["git", "-C", LANE, "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL, text=True).strip()
        if os.path.realpath(top) != os.path.realpath(LANE):
            return False
        return subprocess.call(
            ["git", "-C", LANE, "cat-file", "-e", "793f797^{commit}"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    except Exception:
        return False
```

Patched copy, run in `/tmp` trees:

- full clone: `SELFTEST: 2/2`, exit 0
- full clone with missing `GIT_DIR`: `COULD-NOT-EVALUATE (git unavailable: fatal: not a git repository: …)`, exit 2
- full clone with foreign `GIT_DIR`: `COULD-NOT-EVALUATE (git unavailable: /home/vgpnk/Projects/shokunin/.git)`, exit 2
- genuine no-git in `/tmp`: `COULD-NOT-EVALUATE (no git)`, exit 2
- no-git copy nested in an unrelated repo (X1): `COULD-NOT-EVALUATE (no git)`, exit 2
- shallow clone (X2): `COULD-NOT-EVALUATE (git unavailable: .git)`, exit 2

All declared legs are kept and X1–X3 are closed. One leftover issue: for X2 and X3, `_git_error_text()` prints the `rev-parse --git-dir` *success* output (`.git`, or the foreign path) as the "reason", which is uninformative. A follow-on should print `fixture commit 793f797 unresolvable` in that branch.

Routing: this is a fixable defect, not a tradeoff. Under the freeze rule the round-71 counter is frozen once scored, so the fix belongs in a new round-72 counter (or a declared pre-data correction if the judge rules D not yet scored). In the meantime, the D surface/docstring wording "never a craft red" should be scoped to "for exports outside any git work tree".
