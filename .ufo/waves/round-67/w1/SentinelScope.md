# SentinelScope — scope/security review of the r67 instruments (round 67, w1)

**What I attacked:** `tools/check-receipt-seq.py` and `reports/round-67/accept-c.py`,
`accept-o.py`, `accept-ca.py` (their subprocess call graphs, env handling, path
resolution, external surfaces), plus the wave's own no-network premise. No lane
mutation, no installs (nothing needed), no git/jj writes. All fixtures built under
`/tmp`; read-only git elsewhere.

**Verdict: NOT a clean bill.** No `shell=True`, no `os.system`/`os.popen`, no `eval`/`exec`,
no network import or fetch in any of the four files (confirmed by token count: 0 matches
for `shell=True|os.system|os.popen|eval(|exec(` and 0 for
`urllib.request|urlopen|requests|http.client|socket|ftplib|smtplib|curl|wget`).
But the receipt checker's headline promise is **false on one leg and exploitable**, the
counter-sha pin is **circular**, and the Ca counter executes an **untracked out-of-tree
script**.

---

## S1 — HIGH — `--lands` "committed bytes only" is false for the counter-sha leg; false PASS

`check-receipt-seq.py:184-199` (`check_counter_sha`) reads the paired counter from the
**worktree first** and only falls back to git:

```python
blob = read_worktree(root, cpath)          # worktree wins, always — even in --lands mode
if blob is None:
    blob = read_rev(root, "main", cpath)   # and the fallback is main, not --lands
```

The module docstring (line ~28: *"--lands mode reads committed bytes only"*) and the
claim-O statement (*"committed-bytes --lands mode"*) do not hold: the receipt is read at
lands, the counter it is pinned to is read from the moved worktree.

**Exploit (executed, /tmp fixture).** lands commit carries counter `B`; the receipt in
that same commit pins `sha(A)`; a later commit reverts the counter to `A`:

```
lands counter (git show $LANDS:tools/c.py) -> B     tip/worktree counter -> A
=== checker --lands $LANDS telemetry/r.txt tools/c.py ===
LANDS PASS lands=8f712e80 head=4312adbf moved_past=True (evaluating committed bytes at lands)
SEQ-telemetry/r.txt PASS stamped=ff966e39 evaluated=ff966e39 measured=ff966e39 equal=True
TREE-telemetry/r.txt PASS recorded=208c1c78 actual=208c1c78
SHA-telemetry/r.txt PASS tools/c.py recorded=06f961b8 actual=06f961b8
RECEIPT-SEQ: PASS
exit=0
```

A receipt whose counter bytes at lands **do not match the recorded sha** returns PASS,
exit 0. This is the exact defect class the tool exists to close (r65/r66: verdicts
derived from a worktree that moved past the stamp) — it survives inside the fix.

**Impact:** any repo that touches the counter after lands (a "fix" commit, a revert, a
lane tip rebuild) can make a stale/false receipt grade green under the strongest mode the
claim advertises. The `moved_past=True` flag is printed but never gates anything.

**Smallest remediation:** in `--lands` mode read the counter only as
`read_rev(root, lands, cpath)` (pass `lands` into `check_counter_sha`); drop the
worktree-first branch entirely, or gate it behind an explicit `--worktree` flag that the
claim does not use.

## S2 — HIGH — the `counter sha256 (self)` pin is circular (both sides hash the worktree)

All three counters compute their self-pin from the **worktree copy of themselves**:

- `accept-c.py:172`, `accept-o.py:126`, `accept-ca.py:92`:
  `self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()`

`accept-c`/`accept-o` print `# worktree dirty (tracked): {dirty_flag}` in the STAMP detail
but **never make it a leg** (accept-ca does not even compute it). `STAMP` only asserts
`rev-parse main == --lands` + a resolvable tree.

So: run any counter from a *dirty* worktree at a clean lands HEAD → STAMP passes, the
receipt records the sha of the modified (not committed) counter, and S1 makes the checker
agree with it because it hashes the same mutable file. Nothing in the protocol can
distinguish the counter that produced the receipt from the counter committed at lands.
That is the "fabricated provenance" failure mode the round is supposed to prove fixed.

**Executed evidence:** `git status --porcelain --untracked-files=no` is captured in
accept-c:181 / accept-o:139 and printed, never graded; the only gate is
`mv_rev == lands` (accept-c:198-205), which is blind to tracked dirt.

**Smallest remediation (two lines each):** compute
`self_sha = sha256(git -C root show <lands>:<counter-relpath>)`, and add
`leg("CLEAN", not dirty_flag, ...)` so a tracked-dirty evaluation cannot stamp.

## S3 — MEDIUM-HIGH — accept-ca executes a mutable script outside `--root` and outside the lands tree

`reports/round-67/accept-ca.py:54`

```python
CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"
```

- Not in the lane: `git ls-files --error-unmatch scripts/sources-census.sh` →
  *"did not match any file(s) known to git"*.
- Not in the claim's `lands` list; no hash pin anywhere in the receipt.
- Executed as a subprocess (`accept-ca.py:165`, `[CENSUS, "validate", "--file", reg_path]`)
  for the **D2** leg — i.e. the leg that certifies R66-D2 (registry placement/schema).

**Exploit:** `printf '#!/bin/sh\nexit 0\n' > /home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
→ `validate` exits 0 for any registry; D2's `census_exit` and `E_lines` sub-checks go
green with no registry repair at all. The rest of D2 (placement, S753 cell) is parsed in
Python and would still catch some cases, so this is a *partial* bypass, but it is a
frozen-predicate dependency that a third party can rewrite between the dry run and the
receipt with zero trace in git.

**Impact:** breaks the predicate's hermeticity and the "never act on external surfaces"
rule; the receipt understates what was executed.

**Smallest remediation:** vendor the script at `tools/sources-census.sh`, add it to the
claim's `lands` files, call it root-relative, and add a `sha256(git show <lands>:tools/sources-census.sh)`
pin leg (which S1's fix also makes meaningful).

## S4 — MEDIUM — receipt/counter arguments escape `--root` (path escape confirmed)

`read_worktree` (`check-receipt-seq.py:73-79`) does `os.path.join(root, path)`, which
returns `path` unchanged when it is absolute and happily walks `..`. Nothing validates
confinement.

Executed:

```
$ checker --root . ../outside.txt          # file lives OUTSIDE the repo
SEQ-../outside.txt PASS stamped=ff966e39 ... equal=True
TREE-../outside.txt PASS recorded=208c1c78 actual=208c1c78
RECEIPT-SEQ: PASS          exit=0

$ checker --root . /etc/hostname
SEQ-/etc/hostname FAIL missing_headers=['stamped','evaluated','measured','tree']
```

The absolute case proves the read left the tree (the file was opened and parsed); the
`../` case proves a **PASS verdict can be manufactured from a file outside the evaluated
tree** — e.g. grade a clean clone while pointing receipts at the lane worktree, which is
precisely the "moved-worktree PASS claim" class this round is attacking.

**Impact:** bounded disclosure only (the tool echoes at most 8 hex chars of matched
regex groups and a header-key list), but it defeats the "never run outside `--root`"
invariant and makes receipts non-local to the graded tree.

**Smallest remediation:** reject absolute paths and any arg whose
`os.path.realpath(os.path.join(root, path))` does not start with `os.path.realpath(root) + os.sep`
→ `RECEIPT-SEQ: COULD-NOT-EVALUATE`. Same check for the paired counter path.

## S5 — MEDIUM — `--root` is not pinned to a repo top level; git escapes upward

`run()` only does `root = os.path.abspath(args.root)` (`check-receipt-seq.py:206`), and
`git -C <dir>` resolves repositories by walking **up**. Executed:

```
$ checker --root inner/deep --lands $OUTER_HEAD telemetry/r.txt   # inner/deep is NOT a repo
LANDS PASS lands=cf8ee38f head=cf8ee38f moved_past=False (evaluating committed bytes at lands)
SEQ-telemetry/r.txt FAIL missing_headers=[...]
```

`head=cf8ee38f` is the **outer** repo's HEAD; the tool graded bytes belonging to a repo
that is not the named root. Combined with S4, a `--root` typo silently grades the lane
while the operator believes it graded a clone.

**Smallest remediation:** assert
`realpath(git -C root rev-parse --show-toplevel) == realpath(root)`, else
`COULD-NOT-EVALUATE` (the same three-line check belongs in all three counters, which all
take `--root`).

## S6 — LOW — env hygiene: GIT_DIR et al. are not scrubbed; fixture writes can target a foreign repo

`git()` (`check-receipt-seq.py:64-69`) scrubs `GIT_CONFIG_GLOBAL`/`GIT_CONFIG_NOSYSTEM`
only. The selftest *writes* (`git init`, `config`, `add -A`, `commit` — lines 289-303,
344-350; accept-o 96-112, 212-213) are safe only because the paths are temp dirs. With an
exported `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE`, those verbs retarget the env-named
repo. Executed against a throwaway victim repo:

```
victim commits before=1  tool_rc=2
RECEIPT-SEQ: COULD-NOT-EVALUATE RuntimeError('git commit -q -m base: ')
victim commits after=1   (status clean, log unchanged)
```

No commit/index mutation was achieved in this configuration, but `git init` was executed
against the foreign `.git`, and the selftest docstring's "never reads the owning repo"
guarantee is env-dependent, not structural. Note also that `accept-c.py:104,175,178,181`
and `accept-ca.py:80` scrub **nothing**, and `git status` / `git show` honour the
evaluated repo's local config (`core.fsmonitor` is an execution hook).

**Smallest remediation:** one shared wrapper adding
`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_NAMESPACE`, `GIT_CEILING_DIRECTORIES` to the
scrubbed set, used by all four tools.

## S7 — INFO — the LANDS leg can never fail

`seq.leg("LANDS", True, ...)` (`check-receipt-seq.py:227`) is unconditional, and
`moved` collapses to `False` when `rev-list` errors (`code == 0 and ...`). A caller
reading "every leg PASS" cannot distinguish a healthy run from a failed `rev-list`.
Read the flag, not the verdict, and print `moved=unknown` when `code != 0`.

## S8 — PROTOCOL — `--lands` cannot grade the r67 receipts at all (vacuous leg)

`read_rev(root, lands, rpath)` returns `None` for any receipt committed after lands, and
the tool then reports `SEQ-<r> FAIL unreadable` (fixture 1, executed:

```
$ checker --lands $LANDS telemetry/r.txt      # receipt committed in the NEXT commit
SEQ-telemetry/r.txt FAIL unreadable
RECEIPT-SEQ: FAIL
```

`accept-o`'s LANDS leg codifies this as correct (`accept-o.py:187-200`), and
`accept-ca`'s SEQ leg runs **only** `--selftest` (`accept-ca.py:251`) — never `--lands`
over the three real receipts. So the committed-bytes mode is exercised only on synthetic
fixtures; any later attempt to run the declared `--root <clone> --lands <lands>` over
`reports/round-67/telemetry/*.txt` FAILs by construction. Stated plainly: the instrument
is right, but the protocol names a revision at which its own inputs cannot exist.

**Smallest remediation:** grade receipts at the **records** revision
(`--lands <records-commit>`, receipts present, counters and tree still pinned to the
lands they name) and reserve `--topo` for carrier-parentage against `main`; make
accept-ca's SEQ leg do that instead of `--selftest` alone.

---

## No-network premise: the constraint does not exist in the wave context (and the spec requires the opposite)

I printed the shared context that all 64 seats receive
(`.ufo/waves/round-67/taskcall-v2.json` → `taskCall.context`, 3642 chars) in full. It
contains **no** no-network / offline / egress constraint. Its only hard rule is: *"Never
mutate the fleet repo, sibling lanes, lane jj state or the lane Git index; never run
git/jj writes; read-only git is fine"*. `/home/vgpnk/.omp/agent/RULES.md` and the lane
`AGENTS.md` contain no network policy either (0 matches for `network|offline|internet|egress`).

Against that, the frozen seat spec **requires** egress for the data seats:

- `gen-spec.py:62` (every ROW-OPENING seat): *"Verify everything yourself with curl."*
- `spec-v2.json:499` (RevSourceSupport1..4): *"re-fetch live URL + capture yourself."*

So: **(a)** the instruments are network-free (verified above — the only URL-adjacent code
is `urllib.parse` in `accept-c` for normalisation, no fetch); **(b)** a no-network rule,
if the operator intended one, is violated *by instruction* at ~14+ seats, and every
`VERIFY=<live curl …>` / `CAPTURE` cell produced under it would be a claim with no
permitted method — fabricated readiness written into the frozen spec, not a seat error.
Either add the constraint to the wave context and amend those two prompts, or drop the
premise. I am not reporting a "clean bill" for a constraint I could not find.

## Audited subprocess call list

`tools/check-receipt-seq.py` (read-only unless marked FIXTURE)

| site | verb | target | writes? |
|---|---|---|---|
| 66 wrapper | `git -C root <args>` | root | — |
| 105 `read_rev` | `show <rev>:<path>` | root | no |
| 112 `rev_parse` | `rev-parse --verify -q` | root | no |
| 190 `check_tree` | `rev-parse <stamped>^{tree}` | root | no |
| 224 `check_topo` | `log -1 --format=%H main -- <r>` | root | no |
| 226 `check_topo` | `rev-parse <carrier>^` | root | no |
| 218 `run` | `rev-list --count <lands>..main` | root | no |
| 289-303, 344-350 FIXTURE | `init/config/add -A/commit` | temp dir only | temp |
| 313 FIXTURE | `python -B <tool> --root <lane>` | self-exec | temp |

`accept-c.py`: `git show` (104), `rev-parse main` (175), `rev-parse <lands>^{tree}` (178),
`status --porcelain --untracked-files=no` (181), `diff --name-status BASE -- <entry>` (378),
`python -B reports/round-28/readme/sweep.py` `cwd=root` (390) — all read-only, all
root-relative.

`accept-o.py`: git wrapper (73) + `init/config/add/commit` **only** in `fixture_healthy`
(96-112, tempdir) and the wrong-parent fixture (`f1`, tempdir, 212-213);
`python -B tools/check-receipt-seq.py --selftest` (87), `--help`, and
`python -B .ufo/waves/round-67/stage/mut-o/<mut>.py --selftest` (MUT leg — executes
committed mutant sources with `--root root`; the mutants' own `git` verbs are the
selftest fixtures, verified: same `git()` wrapper, temp dirs).

`accept-ca.py`: git wrapper (80) — `rev-parse`, `cat-file -e <lands>:<p>`, `log -1`,
`rev-parse <c>^`; `[CENSUS, validate, --file reg_path]` (165) ← **out-of-tree absolute path, S3**;
`python -B tools/check-receipt-seq.py --selftest` (251); `python -B tools/check-gate-quotes.py
corpus/lessons/round-67.md` `cwd=root` (268).

No counter writes into `--root`. No `--out`, no redirects, no `tee`, no temp files under
the lane. `git status` (accept-c:181, accept-o:139) may refresh `.git/index`'s stat cache —
the only incidental write to the evaluated root.

## Residual watch item (not my surface, flagged because it is the r66 defect recurring)

`.ufo/waves/round-67` is 6181 files and `git status --porcelain` shows
`?? .ufo/waves/round-67/w1/` and `?? .ufo/waves/round-66/` untracked; `w1/scratch/eval-tip`
is a full materialized tree containing `.ufo/waves/round-50/…`. If the Ca D1 manifest does
not name `w1/scratch/eval-tip` (and the seat scratch trees) as EXCLUDE, r67 ships the same
"wave evidence undurable" shape R66-D1 was routed for, one round later.

## S9 — DESIGN FINDING — the C/Ca id conflict is satisfiable only under three load-bearing conditions

The L1 resolution (A_r → A_c → A_ca, no counter/claims revision) is **sound**, and I can
name the exact mechanism that makes it so: `accept-c.py` reads the tip registry from the
**worktree** (`accept-c.py:228`, `open(os.path.join(root, REGISTRY))`) and only the base
from `git show BASE` (`accept-c.py:230`). So APPEND's `appended_ids` set is a property of
the tree the counter is pointed at, not of the repo tip. At a clone materialised at A_c
the appended set is exactly S801-S804 ∪ S805-S828 ⊆ `allowed_new`, so APPEND passes; at
A_ca (S829+ present) the same counter prints `extra=[S829,…]` and FAILs. Ca's D4 is
likewise worktree-read (`accept-ca.py:158-159`), so at A_ca it sees the S829+ rejects.

Three conditions the sequencing depends on — each is currently unenforced by the
instruments:

1. **accept-c must be run only at A_c.** Because of the worktree read above, any run of
   the C counter at A_ca/tip poisons APPEND. This is now load-bearing, not hygiene.
2. **S801-S804 must carry `opened = 2026-10-24`.** D4's gate is
   `rej_opened_today < len(R66_REJECTS) + 2` → **6** rows with
   `status=rejected` **and** `opened=2026-10-24` (`accept-ca.py:226,235`), counted across
   the whole registry. S801-S804 do not exist in the live registry yet (0 matches at
   tip). If the A_r rows carry any other open date, D4 needs six new gate rejects, not
   two, and Ca's statement ("S801-S804 + >=2 new") stops matching its own leg.
3. **Each receipt must be graded against a `--root` sitting at its own lands commit.**
   This is where S1 bites hardest: with three lands revisions instead of one,
   `check-receipt-seq.py --lands A_c` against a root at A_ca passes the sha leg off the
   A_ca worktree counter (S1), so a receipt can be certified against bytes its own lands
   never contained. Grading `--lands A_c --root <clone@A_c>` closes it; the sequencing
   should say that explicitly, because "materialized clone" alone does not name *which*
   commit each root is at.

**Report:** `.ufo/waves/round-67/w1/SentinelScope.md`
