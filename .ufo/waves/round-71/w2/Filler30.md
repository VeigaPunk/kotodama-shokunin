# Filler30 — variant 29: re-run one frozen claim counting command in a fresh clone

Seat: sentinel (leaf, no spawns). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only;
all clones under `/tmp/f30/`). Tooling: nothing installed, nothing updated.

## Assigned command

Primary (claim D, V70-6 wrapper over the frozen data predicate):

```
python3 -B reports/round-71/accept-d.py --root .
```

Fresh clone protocol: `git archive <sha> | tar -x -C /tmp/f30/<dir>` (no `.git` in the clone), then the
command above with the clone as CWD. Cross-runs of `accept-c.py` / `accept-ca.py` in the same
materialized trees are reported below; they cost nothing extra and expose the provenance defects.

## The lane HEAD moved continuously during this seat — every result is pinned to a sha

`git reflog` observed (all "export from jj"):

```
e7e7e26 08:45:57   75d1675 08:45:31   cb77200 08:43:54   ccadb59 08:41:59
7179d6d 08:45:52   edd7895 08:44:48   2166e45 08:43:35   14c88d9 08:40:45
64da9e1 08:45:43   0fa36c1 08:44:43   c21213a 08:43:29
                   baf3b6a 08:44:27
```

Clones actually graded:

| clone | revision | tree | kind |
|---|---|---|---|
| `c1`, `c2` | `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` | `2a9f2ab5622b62a51c7f49df0577bd659ce191c8` | git archive (no `.git`) |
| `c4` | `2166e45cd0ce71fc85508572ea3fd9c6d942b8bf` | `4c354e07362960233cd467287e9659c1247c19ec` | git archive |
| `c5` | `cb772004f813851f5846e63f8d46d6e2ba81e236` | — | full `git clone --no-local` |
| `c6` | `cb772004f813851f5846e63f8d46d6e2ba81e236` | — | `git clone --depth 1 file://…` |
| `c8` | `edd789565ea3adbb7492c0eb45758d2da1046a2e` | `d6a269e6efa89fdf7d29cf512eeb87c5425e9ed4` | git archive |
| `c9` | `64da9e14e5fa512c7f9c1d7695f48b6d34009b47` | `ff803f433b07fcbd0f768491af71c915fff5dcb3` | git archive |
| `c10` | `1d1b432525f791840a9f4fc9c512d0a9a824e915` (records) | `84a304babade95a3c68111ba8c4783cc54f3b441` | git archive |
| **`c12`** | **`e7e7e2693b66fa67103d986374b618790ce40203`** (final pin) | **`2c94402366a669977305bd058b7e72a6f81b4294`** | git archive |
| `c11` | `e7e7e2693b66fa67103d986374b618790ce40203` | — | `git clone --depth 1` |

Clone fidelity (`c2`, second extraction of `14c88d9`): `git init -q . && git add -A -f && git write-tree`
→ `2a9f2ab5622b62a51c7f49df0577bd659ce191c8` = `HEAD^{tree}`, 6894 files.
Zero-mutation proof, re-hashed after every counter run: `c1` → `2a9f2ab5…` (= HEAD tree),
`c4` → `4c354e07…`, `c12` → `2c944023…`. No new files appeared (no `__pycache__`: `-B` holds).

## Exact output and exit code — primary command

Final pin `e7e7e26` (`/tmp/f30/c12`, no `.git`):

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

Identical at `14c88d9`, `2166e45`, `64da9e14`, `edd7895` (all `EXIT=0`), and in the full clone `c5`
(`python3 -B reports/round-69/accept-d.py --root .` → `ACCEPT-D-69: PASS legs=8/8`, `EXIT=0`).

**Result: PASS, exit 0, reproduced at five pinned shas, graded tree byte-identical before and after.**

## Cross-runs (same materialized trees)

At final pin `e7e7e26` (`c12`):

```
$ python3 -B reports/round-71/accept-c.py --root .     → ACCEPT-C-71: PASS        ### EXIT=0
$ python3 -B reports/round-71/accept-ca.py --root .    → ACCEPT-CA-71: PASS       ### EXIT=0
$ python3 -B reports/round-71/accept-d.py --root .     → ACCEPT-D-69: PASS legs=8/8 ### EXIT=0
$ python3 -B reports/round-71/accept-d.py --selftest   (clone without .git)
SELFTEST: COULD-NOT-EVALUATE (no git)                                          ### EXIT=2
```

C legs at `e7e7e26` (full text in `/tmp/f30/accept-c.12.out`): ENTRY, COUNTS `culture-material=36
corpus=243`, CITED `distinct S-ids cited=13`, ROWS `missing=[] not-mined=[] usedby-missing=[]`,
USEDBY-PATHS `missing-paths=[]`, CITED-LINES `exit=0 CITED-LINES: 0 finding(s) in 1 file(s)`, SWEEP
`filename-owners=[<entry>]`, all PASS. Ca legs at `e7e7e26`: V70-1…V70-5 PASS, QUARANTINE `rows=21
unique-ids=21 labels-ok=True`. Also `EXIT=0` for C and Ca at `14c88d9`, `2166e45`, `64da9e14`.

## Provenance checks

At the receipt revision `1d1b432` the counter bytes match the receipts' self-hashes exactly:

| counter | `1d1b432` (= receipt) | final HEAD `e7e7e26` |
|---|---|---|
| `accept-c.py` | `1df995c2207c50f3…` ✓ receipt | `80b4ca093a1d1c84…` ✗ |
| `accept-ca.py` | `3f3f63fc628aeac1…` ✓ receipt | `f706aacd001ee544…` ✗ |
| `accept-d.py` | `459cfa9da53fe3c4…` ✓ receipt | `459cfa9da53fe3c4…` ✓ |

Receipt-stamped trees resolve (`8c203bd^{tree}=ffb5c549…`, `1d1b432^{tree}=84a304ba…`);
`registry=797` re-derived (`grep -cE '^\s{0,3}\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md` → `797` at every
pin); lane `git status --porcelain --untracked-files=no` empty at `2166e45`.

## Findings

### F1 — HIGH — the V70-6 guard misses "git present, referenced object absent": a shallow clone still yields a craft red (exit 1)

The D claim states that git failures other than genuine absence print `SELFTEST: COULD-NOT-EVALUATE
(git unavailable: ...)` and exit 2 — "never a craft red". That invariant is false.
`_git_available()` (`reports/round-71/accept-d.py:42-58`) only runs
`git -C LANE rev-parse --is-inside-work-tree`. The frozen fixture's real dependency is
`git -C LANE show 793f797:SKILL.md` (`reports/round-69/accept-d.py:199-210`, `except Exception: pass`).
A repo that answers the first probe but lacks the object falls through to the frozen selftest and
reproduces the exact false red the counter exists to remove — reconfirmed at the final pin:

```
$ cd /tmp/f30/c11                                  # git clone --depth 1 of e7e7e26
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

Same in a full-history clone whose object store was re-created (`git init` + `add -A`, i.e. a jj/squash
export or an archive unpacked inside an enclosing git repo):

```
$ cd /tmp/f30/c4 && git init -q . && git add -A -f
$ git show 793f797:SKILL.md ; echo rc=$?            # rc=128
$ python3 -B reports/round-71/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
### EXIT=1
```

Control (full clone `c5`, object present) — the declared green:

```
$ cd /tmp/f30/c5 && git cat-file -e 793f797:SKILL.md ; echo rc=$?   # rc=0
$ python3 -B reports/round-71/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
### EXIT=0
```

Exploit path: any CI checkout with `--depth 1` (or a partial/filtered clone, a fresh `git init` export,
or an archive unpacked under a git-managed `$HOME`) reports `SELFTEST: 1/2`, exit 1 — a craft red
indistinguishable from a genuine depth regression, i.e. the pre-fix failure moved from "no `.git`" to
"`.git` without the object". D's three literal kill-rule legs still hold, so the predicate is not
tripped; the *stated rationale* is falsified.

Smallest remediation (frozen bytes untouched) — probe the object before delegating, in
`reports/round-71/accept-d.py`:

```python
rc = subprocess.call(["git", "-C", LANE, "cat-file", "-e", "793f797:SKILL.md"],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if rc != 0:
    print("SELFTEST: COULD-NOT-EVALUATE (git unavailable: missing object 793f797)")
    return 2
```

Both declared COULD-NOT-EVALUATE spellings and the exit-2 contract are preserved.

### F6 — HIGH — frozen counters were edited after their receipts were filed, mid-wave; the receipts now identify bytes that do not exist at HEAD

`claims.json.freeze_rule`: "The predicate, counter, kill rule and target of each claim are frozen at
this commit and are not edited after any seat scores them (kumitate r42 class)." Wave-2 seats are
scoring now, and two counters changed after `1d1b432`:

```
$ git log --oneline 1d1b432..HEAD -- reports/round-71/accept-c.py reports/round-71/accept-ca.py
75d1675 round-71: post-filing hardening — accept-ca.py slice/id fixes, entry S873 cite, …
edd7895 round-71: accept-c.py docstring accuracy (Filler37 nit)
```

`accept-ca.py` changed semantically, not cosmetically:

```diff
-        original_ok = first.startswith("#") and len(first) > 3
+        original_ok = (first.startswith("# after-state receipt")
+                       or first.startswith("# pre-data control"))
@@
-    ids_ok = len(rows) == 21 and len({r[0] for r in rows}) == 21
+    SLICE = {"S776","S778","S779","S786","S787","S791","S792","S795","S796",
+             "S804","S807","S812","S814","S816","S817","S820","S823","S824",
+             "S825","S827","S835"}
+    ids_ok = len(rows) == 21 and {r[0] for r in rows} == SLICE
```

Consequence: the receipts' `# counter sha256 (self)` lines no longer identify the graded bytes at HEAD
(see provenance table). Replay hazard — a reader who re-runs `accept-ca.py` at HEAD runs a *stricter*
counter than the receipt describes, and `accept-c.py` at HEAD is not the byte the C receipt hashed.
The graded entry also moved after the C receipt (`75d1675` appends `(S873)` to the SEP bullet in
`corpus/knowledge/culture-material/dance-performance-movement-codes.md`, one line, entry now differs
from the `8c203bd` bytes the receipt graded).

I tested whether the edits change any verdict — they do not, on the two trees in play:

```
$ python3 -B /tmp/f30/c9/reports/round-71/accept-ca.py --root /tmp/f30/c10   # new counter, receipt tree
ACCEPT-CA-71: PASS ### EXIT=0
$ python3 -B /tmp/f30/c10/reports/round-71/accept-ca.py --root /tmp/f30/c9   # receipt counter, HEAD tree
ACCEPT-CA-71: PASS ### EXIT=0
```

So no false PASS/FAIL was introduced, but the freeze rule was breached and the receipts are stale
provenance. Remediation: re-stamp `measures-c.txt` / `measures-ca.txt` at the revision that carries the
edited counters (and re-record `# counter sha256 (self)`), or revert the counter edits and land the
tightening as a round-72 counter. Silence here is worse than either: the filed receipts are the
evidence of record for C and Ca.

### F2 — LOW — the STAMP leg is tautological inside a single tree (provenance label overclaims)

`evaluate()` compares `sha256_file(HERE/SELF)` with `sha256_file(root/reports/round-69/SELF)`
(`reports/round-69/accept-d.py:133-137`). For every documented invocation the counter runs from the
tree it grades, so both paths are the same file and the leg cannot fail — `self=c41ffbc8244f
committed=c41ffbc8244f`, including in a `.git`-less archive where no committed blob exists. It detects
only "script bytes ≠ graded tree's counter bytes"; a mutated counter still stamps PASS. Discriminating
control only when the graded root lacks the file:

```
$ python3 -B reports/round-71/accept-d.py --root /tmp/f30/empty
LEG FAIL STAMP self=c41ffbc8244f committed=none
…
ACCEPT-D-69: FAIL legs=0/8
### EXIT=1
```

Provenance is intact here only by the out-of-band receipt hash. Remediation: read the committed blob
(`git cat-file blob HEAD:reports/round-69/accept-d.py`) for the `committed` side when `.git` resolves,
or compare against the receipt hash instead of the worktree copy.

### F3 — INFO — `--selftest` accepts `--root` and silently ignores it

`selftest()` grades `LANE`, derived from the counter's own path (`reports/round-71/accept-d.py:27-29,
72-80`); `args.root` is never read on that branch. `--selftest --root /some/other/tree` selftests the
lane, not the named tree, with no diagnostic.

### F4 — INFO — receipts pin revisions the graded surface has moved past

`measures-ca.txt` / `measures-d.txt` stamp `1d1b432` (tree `84a304ba`) and Ca grades
`corpus/lessons/round-71.md` (V70-5). That file changed at least four times afterwards
(`baf3b6a` R71-M8, `0fa36c1` M6, `c21213a` R71-M5, `75d1675` M9/M10); `census-end.txt` and
`measures-c.txt` also changed. I re-ran Ca at `2166e45`, `64da9e14` and `e7e7e26`: still PASS, exit 0 —
no regression — but "evaluated revision 1d1b432" no longer describes the lesson bytes graded at HEAD.
The lane advanced through ≥8 commits in ~5 minutes of wall time; any "at lane HEAD" statement in this
round must carry a sha (this report carries seven).

### F5 — INFO — the C receipt body is a curated bundle, not the counter's stdout

`measures-c.txt` prints `registry=797`, `entries-cited: 13`, `usedby-paths: all exist`, a README sweep
line and a census line; `accept-c.py` emits none of them (its details read `want >=12`, `missing=[]`).
The values are individually true (I re-derived `registry=797`), but the receipt cannot be reproduced
from the counting command alone, so the "same sentence the receipt prints" control holds only for the
`ACCEPT-C-71: PASS` line.

## Verdict for variant 29

- Assigned command `python3 -B reports/round-71/accept-d.py --root .` at the final pin `e7e7e26`
  (fresh `git archive` clone, no `.git`): **PASS, `ACCEPT-D-69: PASS legs=8/8`, exit 0**; identical at
  `14c88d9`, `2166e45`, `64da9e14`, `edd7895` and in a full clone; graded tree unmutated.
- Cross-runs `accept-c.py` / `accept-ca.py`: **PASS, exit 0** at every pin; git-less `--selftest` gives
  the declared `COULD-NOT-EVALUATE (no git)`, exit 2.
- No false PASS found in the counters. Two contract-level defects stand: **F1** (HIGH — "never a craft
  red" is false for shallow/partial object stores; reproducible with `git clone --depth 1`) and **F6**
  (HIGH — freeze rule breached; `accept-c`/`accept-ca` receipt hashes are stale at HEAD). F2-F5 are
  labelling/provenance defects.
