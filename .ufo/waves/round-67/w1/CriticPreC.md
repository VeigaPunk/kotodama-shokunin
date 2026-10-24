# CriticPreC — pre-data attack on reports/round-67/accept-c.py

Counter under test: `reports/round-67/accept-c.py` rev0, self-sha `3e5f1a58…`
Attack surface: STAMP/lands discipline, ROWS fabricability, LINK dup classes,
APPEND flip allowance, NOHARM/SWEEP/CAPTURE gaps.
Scratch clone: `.ufo/waves/round-67/w1/fabric-c` (copy of `.scratch/eval-base`,
git main = base `ad5b52b`). Lane repo untouched; all edits confined to the
scratch clone.

## Verdict summary

The counter is **FABRICABLE END-TO-END**: a fully uncommitted worktree state
prints `ACCEPT-C-67: PASS` at stamped==evaluated==lands==base. Four distinct
bypasses ride inside that PASS. STAMP lands-validation is sound; ROWS is sound
on every fabricated defect tried. The critical hole is that legs read the
worktree, never the stamped tree, and `dirty_tracked` is advisory only.

## F1 — CRITICAL: PASS on zero committed bytes (worktree-vs-stamp split)

Staged, *uncommitted*: new entry file (untracked), 24 well-formed S805–S828
rows, S001 used-by flip + verbatim S001 dup, README count/topic updates.
Nothing was committed — `git status` shows ` M corpus/README.md`,
` M corpus/SOURCES.md`, `?? …/medicine-healing-codes.md`.

    python3 -B reports/round-67/accept-c.py --root .ufo/waves/round-67/w1/fabric-c \
        --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a

Observed (verbatim, exit 0):

    STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=True
    FILE/SET/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/CAPTURE/TOPIC all PASS
    ACCEPT-C-67: PASS

Root cause: STAMP compares `git rev-parse main` (committed) with `--lands`,
but FILE/registry/README legs `open()` worktree bytes, and NOHARM runs
`git diff BASE` — also worktree. `dirty_flag` is computed, printed, and never
used in any verdict. So stamped==evaluated certifies the *commit*, while every
leg measures *uncommitted* bytes. Consequences:

- A receipt claiming "lands = X" can be minted on bytes that exist in no
  commit — false provenance, the exact class the r66 fix was meant to kill.
- `git rev-parse main` never checks the checkout: `main == lands` while the
  worktree is checked out to *another* revision still yields STAMP PASS —
  the receipt is measured revision-faithful in name only.
- Untracked files are doubly invisible: not in `dirty_flag`
  (`--untracked-files=no`) and not in `git diff BASE`.

Impacted axes: C integrity (fatal), and the same read-worktree pattern in
accept-o/accept-ca should be re-audited (not measured here).

Smallest safe correction: either (a) gate on `not dirty_flag` **and**
`git rev-parse HEAD == lands`, or better (b) read FILE/SOURCES/README via
`git show {lands}:<path>` and enumerate knowledge files via
`git ls-tree {lands}`, keeping `git diff` only for NOHARM. (b) makes the
counter physically incapable of reading anything but the stamped tree; it
also unbreaks the legitimate workflow of re-running a counter on a dirty
clone, since dirt becomes irrelevant.

## F2 — HIGH: generic mutable-cell rule makes the S753 flip allowance dead code

APPEND (accept-c.py:368-370) permits ANY row to rewrite cells 7 (status),
9 (recheck), 10 (used-by) simultaneously, unlogged, undeclared:

    if len(oc) == 11 and len(nc) == 11 and oc[:7] == nc[:7] and oc[8] == nc[8]:
        continue

Observed: S001's used-by flipped to append the new entry path →
`APPEND PASS … immutable_violations=[]`, full PASS. The `sid in ALLOWED_FLIP`
branch at :365 is unreachable for its declared purpose — S753's declared
single-cell flip already satisfies the generic rule. "can another row's cell
ride the flip?" — worse: no row needs the flip; every row's status/recheck/
used-by is mutable by construction, so the r66 E11 repair can silently hide
inside a lands commit alongside arbitrary undeclared flips (e.g. flipping a
mined row to `queued`, or re-pointing used-by away from a live entry, breaking
the corpus' mined⇔used-by invariant with the counter's blessing).

Smallest safe correction: bound the generic rule to the declared disposition
set, or require undeclared mutable flips to be listed in claims.json (i.e.
make the allowance `ALLOWED_FLIP`-keyed per-cell).

## F3 — HIGH: `tip_set`/`base_set` dict-collapse hides duplicate rows AND masked mutations

`tip_set`/`base_set` are `{id: line}` — last occurrence wins. Observed:

- A byte-identical duplicate `| S001 | …` appended at the table tail →
  APPEND PASS, SET PASS, full PASS. Row-count claims (registry 724→752) are
  meanwhile inflated by bytes the counter never saw.
- A *mutated* duplicate of a base row placed AFTER the original overrides
  `tip_set` — and a mutated-first/original-last pair makes even a mutable-cell
  violation vanish (verified: flipped S001 + verbatim trailing dup → PASS).

Smallest safe correction: collect `tip`/`base` rows as `{id: [lines]}`;
fail APPEND on `len(lines) > 1` for any id not in NEW_IDS (SET already does
this for new ids only).

## F4 — MEDIUM: LINK blind spots — reordered query, second live URL

Inside the F1 PASS run, `LINK PASS` held with two live duplicate classes:

- S827's URL is S826's page with reordered query (`?a=1&b=2` vs `?b=2&a=1`):
  `norm_url_q` keeps raw query order (host+path+unquoted query), so the
  same-page duplicate is a new key. Same hole for `?a=1&` vs `?a=1`,
  `%2F`/`/` path variants (only query is unquoted), `a=1&&a=1`, and any
  case-variant path (lowercase host only).
- S828 carries a second live URL duplicating base row S001's
  `glottolog.org/about.html`: `row_urls()` returns only `live[0]`, so the
  embedded duplicate is never normalized or compared — and CAPTURE checks
  only the first live URL too.

Smallest safe correction: sort query params (parse_qsl + sort) and unquote
path in `norm_url_q`; have `row_urls` return ALL live URLs and check each for
base/new-set collisions; CAPTURE must cover every live URL or the docstring
should say "first".

## F5 — LOW/MEDIUM: used-by substring match; docstring/code drift

- ROWS tests `ENTRY in c[10]` (substring). Observed:
  `used-by='…medicine-healing-codes.md.bak'` → ROWS PASS. A fabricated row
  can name a sibling/backup path. Fix: `ENTRY in c[10].split(", ")`
  (cell is comma-separated paths per registry convention).
- CAPTURE docstring claims an explicit `no-capture` reason token suffices;
  the code has no such branch — every row must carry a matching archive URL.
  Code is stricter than spec (fail-closed), but the frozen docstring lies;
  a data seat following the docstring would produce rows the counter rejects.
  Fix: add the token branch or strike it from the docstring.
- Citation `(S###)` inside code fences/comments counts toward ONEID — minor.

## What held (controls verified, not attacked further)

- Wrong `--lands` (tip `b78f8b8`, ancestor `4589ebd`): STAMP FAIL, exit 1.
  Absent-in-clone lands → `^{tree}` unresolvable → STAMP FAIL. Non-40hex →
  exit 2. Missing `--lands` → argparse exit 2.
- ROWS rejected all four fabricable-defect classes at once (queued status,
  tier C, wrong opened date, foreign used-by): `ROWS FAIL n=4`. Tier
  inflation to `A` is a REVIEW burden, not a counter bug — the counter can't
  see evidence, so pre-data review of tier assignments stays load-bearing.
- BASE is hardcoded; NOHARM diffs against it, not against lands — correct.

## Dependencies / residual risk

- The demonstrated PASS used `main == base` checkout; a clone whose worktree
  is detached at another rev while `main == lands` was reasoned statically
  (STAMP never reads HEAD). Flagged for the integrator to harden via F1(b).
- accept-o.py and accept-ca.py likely share the worktree-read pattern;
  CriticPreO/CriticPreCa should confirm the same F1 class on those counters.
- Report: `.ufo/waves/round-67/w1/CriticPreC.md` (this file). No tool installs.

## Addendum — L1 sequencing resolution (per-claim lands)

L1 ruled (2026-10-24, this wave): no counter/claims revision for the
C-APPEND vs Ca-D4 id conflict. Claim C's receipt is run at its own lands
commit A_c where only S805-S828 append over base (A_r carrying S801-S804 +
r66 dispositions lands before A_c, so EXTRA_IDS stays correct); the S829+
reject rows and the r67 lesson land at Ca's later lands commit A_ca, after
C's receipt. APPEND's NEW_IDS∪EXTRA_IDS bound is therefore correct *per
lands commit* — the conflict is satisfiable as sequenced, and none of F1–F5
changes: F2's rogue mutability and F3's duplicate-collapse would still
admit undeclared registry mutations inside A_c itself.
