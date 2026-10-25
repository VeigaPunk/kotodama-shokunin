# Filler30 — variant 29: re-run one frozen claim counting command in a fresh clone

Seat: sentinel (leaf, no spawns). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only;
all clones under `/tmp/f30/`). Tooling: none installed, none updated.

## Assigned command

Primary (claim D, V70-6 wrapper over the frozen data predicate):

```
python3 -B reports/round-71/accept-d.py --root .
```

Fresh clone protocol: `git archive <sha> | tar -x -C /tmp/f30/<dir>` (no `.git` in the clone), then the
command above run with the clone as CWD.

## Lane HEAD moved during this seat — every claim below is pinned to a sha

`git reflog` at measurement time:

```
2166e45 HEAD@{08:43:35}: export from jj
c21213a HEAD@{08:43:29}: export from jj
ccadb59 HEAD@{08:41:59}: export from jj
14c88d9 HEAD@{08:40:45}: export from jj
3764c2d HEAD@{08:39:02}: export from jj
```

Clones actually graded:

| clone | revision | tree | kind |
|---|---|---|---|
| `/tmp/f30/c1` | `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` | `2a9f2ab5622b62a51c7f49df0577bd659ce191c8` | git archive (no `.git`) |
| `/tmp/f30/c4` | `2166e45cd0ce71fc85508572ea3fd9c6d942b8bf` | `4c354e07362960233cd467287e9659c1247c19ec` | git archive (no `.git`) |
| `/tmp/f30/c5` | `cb772004f813851f5846e63f8d46d6e2ba81e236` | — | full `git clone --no-local` |
| `/tmp/f30/c6` | `cb772004f813851f5846e63f8d46d6e2ba81e236` | — | `git clone --depth 1 file://…` |

Clone fidelity (c2 = second extraction of `14c88d9`):

```
$ git -C /tmp/f30/c2 init -q . && git -C /tmp/f30/c2 add -A -f && git -C /tmp/f30/c2 write-tree
2a9f2ab5622b62a51c7f49df0577bd659ce191c8
$ git -C <lane> rev-parse 'HEAD^{tree}'      # at 14c88d9
2a9f2ab5622b62a51c7f49df0577bd659ce191c8
```

Exact tree equality, 6894 files. Zero-mutation proof (same tree re-hashed after all counter runs):

```
$ cd /tmp/f30/c4 && git init -q . && git add -A -f && git write-tree
4c354e07362960233cd467287e9659c1247c19ec          # == HEAD tree, no new files (no __pycache__)
$ cd /tmp/f30/c1 && git init -q . && git add -A -f && git write-tree
2a9f2ab5622b62a51c7f49df0577bd659ce191c8          # == HEAD tree
```

## Exact output and exit code — primary command

At `2166e45` (`/tmp/f30/c4`, no `.git`):

```
$ python3 -B reports/round-71/accept-d.py --root .
LEG PASS STAMP self=c41ffbc8244f committed=c41ffbc8244f
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
### EXIT=0
```

At `14c88d9` (`/tmp/f30/c1`, no `.git`): byte-identical output, `EXIT=0`.
Full clone `c5` (`cb77200`), frozen counter invoked directly:

```
$ python3 -B reports/round-69/accept-d.py --root .
… (same 8 PASS legs) …
ACCEPT-D-69: PASS legs=8/8
### EXIT=0
```

**Result: PASS, exit 0, reproducible at two pinned shas and in a full clone; graded tree unmutated.**

## Cross-runs in the same clones (cheap, same materialized trees)

At `2166e45` (and identically at `14c88d9`):

```
$ python3 -B reports/round-71/accept-c.py --root .
LEG PASS ENTRY … LEG PASS COUNTS culture-material=36 corpus=243 (want 36/243)
LEG PASS CITED distinct S-ids cited=13 (want >=12)
LEG PASS ROWS missing=[] not-mined=[] usedby-missing=[]
LEG PASS USEDBY-PATHS missing-paths=[]
LEG PASS CITED-LINES exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
LEG PASS SWEEP filename-owners=['corpus/knowledge/culture-material/dance-performance-movement-codes.md'] …
ACCEPT-C-71: PASS
### EXIT=0

$ python3 -B reports/round-71/accept-ca.py --root .
LEG PASS V70-1 … LEG PASS V70-2 … LEG PASS V70-3 words=25 (want <=25)
LEG PASS V70-4 … LEG PASS V70-5 … LEG PASS QUARANTINE rows=21 unique-ids=21 labels-ok=True
ACCEPT-CA-71: PASS
### EXIT=0

$ python3 -B reports/round-71/accept-d.py --selftest      # clone without .git
SELFTEST: COULD-NOT-EVALUATE (no git)
### EXIT=2
```

## Provenance checks that hold

- Counter bytes match their receipts' self-hashes exactly:

```
1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4  accept-c.py
3f3f63fc628aeac1fb9d076a77c6840161bbeacdde065294f01b13ea5139eb46  accept-ca.py
459cfa9da53fe3c4b44cfa5be4f82a2794298cc3b79c7f4e0f330f0977945930  accept-d.py
```

- Receipt-stamped trees resolve: `8c203bd^{tree} = ffb5c549…` (measures-c), `1d1b432^{tree} = 84a304ba…` (measures-ca, measures-d).
- `registry=797` re-derived independently: `grep -cE '^\s{0,3}\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md` → `797`.
- Lane tracked-dirty at measurement: `git status --porcelain --untracked-files=no` → empty.

## Findings

### F1 — HIGH — the V70-6 guard does not cover "git present, referenced object missing": shallow clone still yields a craft red (exit 1)

The D claim's surface text and its correction (2) state: git failures other than genuine absence
"print `SELFTEST: COULD-NOT-EVALUATE (git unavailable: ...)` and exits 2 — never a craft red."
That invariant is false. `_git_available()` (`reports/round-71/accept-d.py:42-58`) only tests
`git -C LANE rev-parse --is-inside-work-tree`. The frozen fixture's real dependency is
`git -C LANE show 793f797:SKILL.md` (`reports/round-69/accept-d.py:199-210`, `except Exception: pass`).
A repo that answers the first probe but lacks the object falls through to the frozen selftest and
reproduces the exact false red the counter was written to eliminate:

```
$ cd /tmp/f30/c6                       # git clone --depth 1 of cb77200
$ git cat-file -e 793f797:SKILL.md ; echo rc=$?
rc=128
$ git rev-parse --is-inside-work-tree ; echo rc=$?
true
rc=0
$ python3 -B reports/round-71/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
### EXIT=1
```

Same result in a full-history clone whose object store was re-created (`git init` + `add` only, i.e. a
jj/squash export or an archive extracted inside an enclosing git repo):

```
$ cd /tmp/f30/c4 && git init -q . && git add -A -f
$ git show 793f797:SKILL.md ; echo rc=$?
rc=128
$ python3 -B reports/round-71/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
### EXIT=1
```

Control (full clone, object present) — the declared green:

```
$ cd /tmp/f30/c5 && git cat-file -e 793f797:SKILL.md ; echo rc=$?   # rc=0
$ python3 -B reports/round-71/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
### EXIT=0
```

Exploit path: any CI runner that checks out with `--depth 1` (or a partial/filtered clone, a fresh
`git init` export, or an archive unpacked under a git-managed directory such as a dotfiles-tracked
`$HOME`) reports `SELFTEST: 1/2`, exit 1 — a craft red indistinguishable from a genuine depth
regression. This is the same failure class as the pre-fix behaviour, just moved from "no `.git`" to
"`.git` without the object". The three literal kill-rule legs still hold, so D's declared predicate is
not tripped; the *stated rationale* ("never a craft red") is falsified.

Smallest remediation (frozen bytes untouched): in `reports/round-71/accept-d.py`, extend the guard
with an object probe before delegating:

```python
rc = subprocess.call(["git", "-C", LANE, "cat-file", "-e", "793f797:SKILL.md"],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if rc != 0:
    print("SELFTEST: COULD-NOT-EVALUATE (git unavailable: missing object 793f797)")
    return 2
```

This keeps both declared COULD-NOT-EVALUATE spellings and the exit-2 contract, and makes the
"never a craft red" sentence true for shallow/partial object stores.

### F2 — LOW — the STAMP leg is tautological inside a single tree (provenance label overclaims)

`evaluate()` compares `sha256_file(HERE/SELF)` against `sha256_file(root/reports/round-69/SELF)`
(`reports/round-69/accept-d.py:129-136`). When the counter is run from the tree it grades — every
documented invocation — both paths are the same file, so the leg cannot fail: `self=c41ffbc8244f
committed=c41ffbc8244f`. It detects only "script bytes ≠ graded tree's counter bytes"; it does not
establish that the counter matches the committed blob, so a mutated counter still stamps PASS.
Evidence: identical hashes in the archive clone (no `.git`, no committed blob available), and a
discriminating control only when the graded root lacks the file:

```
$ python3 -B reports/round-71/accept-d.py --root /tmp/f30/empty
LEG FAIL STAMP self=c41ffbc8244f committed=none
…
ACCEPT-D-69: FAIL legs=0/8
### EXIT=1
```

Provenance is nonetheless intact here by an out-of-band check (receipt `# counter sha256 (self)`
lines match all three counters, see above). Remediation: when `.git` is present read the committed
blob (`git cat-file blob HEAD:reports/round-69/accept-d.py`) for the `committed` side, or compare
against the receipt hash instead of the worktree copy.

### F3 — INFO — `--selftest` accepts `--root` and silently ignores it

`selftest()` grades `LANE`, derived from the counter's own path (`reports/round-71/accept-d.py:29-30,
72-80`); `args.root` is never read on that branch. `python3 -B reports/round-71/accept-d.py --selftest
--root /some/other/tree` selftests the lane, not the named tree, with no diagnostic. Harmless for the
declared command, but a reader of the argparse help ("lane root") will infer otherwise.

### F4 — INFO — receipts pin revisions that the graded surface has since moved past

`measures-ca.txt` / `measures-d.txt` stamp `1d1b432` (tree `84a304ba`), and the Ca counter grades
`corpus/lessons/round-71.md` (V70-5 reject-sweep). That file changed after the stamp
(`c21213a`: "commit C receipt (measures-c.txt) + lesson R71-M5 (declared-counter defect)"), and
`census-end.txt` plus `measures-c.txt` also changed. I re-ran Ca at `2166e45`: still `PASS`, exit 0, so
no regression — but "evaluated revision 1d1b432" no longer describes the lesson bytes that were
actually graded at HEAD. A re-stamp (or an explicit "graded at <sha> after c21213a" note) keeps the
receipt honest. Separately, wave-2 measurement is happening on a moving HEAD
(`14c88d9 → ccadb59 → c21213a → 2166e45 → cb77200` in ~3 min): any "at lane HEAD" statement in this
round must carry a sha.

### F5 — INFO — the C receipt body is a curated bundle, not the counter's stdout

`measures-c.txt` prints `registry=797`, `entries-cited: 13`, `usedby-paths: all exist`, the README
sweep line and the census line; `accept-c.py` emits none of those (its legs are ENTRY, COUNTS, CITED,
ROWS, USEDBY-PATHS, CITED-LINES, SWEEP, and its details read `want >=12` / `missing=[]`). The values
are individually true (I re-derived `registry=797`), but the receipt cannot be reproduced from the
counting command alone, so its "same sentence the receipt prints" control holds only for the
`ACCEPT-C-71: PASS` line.

## Verdict for variant 29

- Assigned command `python3 -B reports/round-71/accept-d.py --root .` at `2166e45` (fresh `git
  archive` clone, no `.git`): **PASS, `ACCEPT-D-69: PASS legs=8/8`, exit 0**; identical at `14c88d9`;
  graded tree byte-identical before and after the runs.
- Cross-runs `accept-c.py` and `accept-ca.py`: **PASS, exit 0** at both pinned shas; git-less
  `--selftest` gives the declared `COULD-NOT-EVALUATE (no git)`, exit 2.
- Claim D's three literal kill-rule legs hold, but its declared invariant "never a craft red" is
  **falsified** in the git-present/object-missing state (F1, HIGH, reproducible with `git clone
  --depth 1`); F2-F5 are provenance/labelling defects, no false PASS found.
