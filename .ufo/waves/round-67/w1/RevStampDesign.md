# RevStampDesign — adversarial review of the r67 stamp mechanism

Seat: RevStampDesign (r67 w1). Scope: the `--lands <40hex>` + `git rev-parse main`
equality stamp, its binding to the claim, detached-HEAD behaviour in the
jj-colocated lane, and whether `stamped` should come from claims.json.
Method: read the three frozen counters, `tools/check-receipt-seq.py`, claims.json,
the pre-data receipts/controls; reproduce attacks in throwaway `/tmp` clones
(lane read-only; no git/jj writes in the lane). All claims below are observed
unless marked `[INFERENCE]`.

## Answers first

1. **Spoofable? Yes, trivially.** `--lands` is caller-supplied and the only check
   is `rev-parse main == --lands`. Both sides of the equality are controlled by
   the same caller, so `--lands $(git rev-parse main)` at any tip is a
   tautology. Nothing binds `lands` to claims.json, to the base commit, to the
   claim's artifact set, to the bytes actually read, or to the instrument that
   reads them. The only external anchor in the whole round is the post-records
   carrier-parentage (`check-receipt-seq.py --topo`), and it validates the
   receipt's *self-declared* stamped value, not its provenance.
2. **Should `stamped` be read from claims.json? No.** claims.json is frozen
   pre-wave; the lands commit does not exist at freeze time, so it cannot
   contain a lands hash without post-freeze mutation of the frozen predicate
   (the exact sin Ca is meant to close). What claims.json *must* carry instead:
   `base`, a freeze ref, and the per-claim declared artifact sets. `--lands`
   stays the declared value but must be constrained (spec below).
3. **Does STAMP fail on detached HEAD? No — it passes, measuring the wrong
   bytes.** In the jj-colocated lane, git HEAD is detached by construction
   (`.git/HEAD` = `b78f8b8`, jj `@` = `406440ae`), while `refs/heads/main` is a
   bookmark export. `rev-parse main` resolves a ref that is independent of the
   checkout, so a clone checked out at base with `main` at tip prints
   `STAMP PASS` while every leg reads base bytes. It fails closed only when the
   ref is absent or renamed — by accident, not design — and even then it
   misreports (`evaluated revision: main`, see F6).

## Findings

### F1 (critical) — STAMP compares the `main` ref, not the evaluated bytes
`accept-c.py:175`, `accept-o.py:130`, `accept-ca.py:98` all do
`git -C <root> rev-parse main`; every leg then reads the **worktree** via
`open(root/path)` (`accept-ca.py:71-77`, `accept-c.py:228`). No leg compares
`HEAD` to `lands`, and no leg requires the checkout to be clean.

Observed (fresh `--no-local` clone at tip, `git checkout --detach ad5b52b0`,
`--lands b78f8b8`):
```
HEAD=ad5b52b0... main=b78f8b8... sym=detached
STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e
```
The stamp certifies tip while the process reads the base tree (and prints a
receipt whose "evaluated revision" is false). This is the moved-worktree PASS
class the round claims to have closed.

### F2 (critical) — dirty and untracked bytes pass the stamp
`dirty_tracked` is computed (`accept-c.py:181-184`, `accept-o.py:136-139`) but
is **not** in `stamp_ok` (`accept-c.py:200-202`, `accept-o.py:152-154`);
`accept-ca.py` does not compute it at all. The dirty check also passes
`--untracked-files=no`, so a **new** file is invisible.

Observed A (dirty tracked file, `--lands` = tip):
```
 M corpus/QUALITY.md
STAMP PASS ... dirty_tracked=True
CRITERION FAIL  ->  CRITERION PASS      (after appending an uncommitted criterion 19)
git show <lands>:corpus/QUALITY.md | grep -c '^19\.'  =  0
```
A leg flips FAIL→PASS on bytes that are not in the lands tree, under a PASS
stamp.

Observed B (untracked new entry — the C claim's central artifact):
```
dirty_tracked=0 untracked=1
STAMP PASS ... dirty_tracked=False
FILE PASS exists lines=113 h1=1 h2=9 h3=0 topic=True
```
`corpus/knowledge/culture-material/medicine-healing-codes.md` was untracked;
`FILE` read it and passed. A seat can commit the registry rows, leave the entry
uncommitted, and every worktree read still sees it. `git cat-file -e
<lands>:corpus/.../medicine-healing-codes.md` would fail while the receipt
asserts that tree.

Two more worktree reads of the same class: D1 reads the manifest with
`read(root, MANIFEST)` and checks `cat-file -e lands:<include>` only for its
INCLUDE entries, never the manifest itself `[INFERENCE: an untracked manifest
would pass D1 if its includes are tracked; not exercised because no
`.ufo/waves/round-66/w1/*.md` is tracked at b78f8b8]`; and D2 runs the census
against the worktree path (`--file reg_path`, `accept-ca.py:176-179`) so the
registry bytes validated are whatever is on disk, not `lands:corpus/SOURCES.md`.

### F3 (critical) — the instrument's own bytes are unbound
`self_sha` is the sha of the running `__file__` (`accept-c.py:170`,
`accept-o.py:125`, `accept-ca.py:93`); nothing compares it to
`git cat-file blob <lands>:reports/round-67/accept-<X>.py`. Running a patched
copy from `/tmp` with `--root <clone>` produces a receipt whose counter sha
exists nowhere in the lands tree, and no leg notices.

This is not hypothetical: the round's own base control already has it.
`reports/round-67/telemetry/dry-run-ca.txt:1-5` records
`counter sha256 (self): 5e8915ac…`, `stamped revision: ad5b52b0…`, and leg output
for accept-ca.py — but
```
git cat-file -e ad5b52b0:reports/round-67/accept-ca.py   -> exit 128
git ls-tree -r ad5b52b0 -- reports/round-67               -> empty
```
So the "base dry-run" was **not** produced in a materialized clone at base (the
instrument does not exist there); it was produced on a worktree carrying the
untracked instruments with `main` still at base. The receipt's SEQ leg proves
it internally: it lists `accept-c.py`/`accept-o.py` as unreadable-but-grepped
yet omits `accept-ca.py`, i.e. `read(root, "reports/round-67/accept-ca.py")`
succeeded under a `--root` whose stamped revision lacks that path.
Reproduced in `/tmp` (`git checkout -B main ad5b52b0`, copy instruments in
untracked, run `--root . --lands ad5b52b0`): identical `STAMP PASS
stamped=ad5b52b0`, `tree=de353b046be5e119c5203f0c5c82e92790c3e546`,
`D1 FAIL bad=['manifest_absent']`. `controls-ca.txt`'s declared command
(`git clone --no-local --single-branch --branch main . .scratch/eval-base`,
then run the counter inside it) cannot reproduce the recorded receipt: at base
the script is absent; at tip the clone's `main` is `b78f8b8` and STAMP fails.
**The r67 pre-data control is itself a false stamp of exactly the r66 class.**

### F4 (high) — `--lands` is unbound to the claim
No counter reads `claims.json` (`grep claims.json reports/round-67/accept-*.py`
→ nothing); there is no `merge-base --is-ancestor` against `base`, no
`lands != base`, no artifact-set check. `claims.json` has `base` and no lands
field (correct for a freeze, but then the binding must be built elsewhere).
A lane can commit its work and pass `--lands $(git rev-parse main)`; a lane can
also hand the verifier a commit from an unrelated history whose tree happens to
satisfy the leg greps.

### F5 (high) — SEQ is a text grep over worktree bytes, not a semantic check
`accept-ca.py` SEQ requires the substrings `--lands`, `required=True`,
`stamped revision`, `evaluated revision`, and `"mv_rev == lands" in text`.
A counter whose check is `mv_rev == lands or True` still contains the substring
and passes; a comment containing it passes; SEQ reads the counters from the
worktree (F1/F2 hole) and runs the selftest tool from the worktree, not from
`lands` (`cwd=root`). It also requires `"14/14" in stdout`, which a stub can
print.

### F6 (medium) — `rev-parse` exit codes are ignored; diagnostics lie
`accept-ca.py:98-99` discards the return code; when `main` is absent git prints
the literal token to stdout, so the receipt says
`# evaluated revision: main` instead of `unresolvable` (observed after
`git branch -m main trunk`). STAMP fails, but the receipt is not
self-describing. `{lands}^{tree}` also resolves any object in the DB, including
dangling commits, with no `--verify <lands>^{commit}` + reachability check.

### F7 (medium) — receipts are not attributable to a root or an interval
No receipt records `--root`, `HEAD`, clean/dirty, `base`, freeze ref, or
claims sha. Post-records topo can therefore only compare the receipt's
self-declared `measured revision` to the carrier's parent. With the L1's
per-claim lands sequence (A_r < A_c < A_ca), a single header without a claim id
and interval cannot distinguish a C receipt from a Ca receipt stamped at the
wrong commit.

### F8 (high, live) — the frozen instrument was mutated after freeze, undetected
`reports/round-67/accept-ca.py` on disk is `5382ffed…`; the blob at the freeze
commit `b78f8b8` is `5e8915ac…`; `git diff b78f8b8` shows the QUOTES regex
changed `S(8[0-2]\d)` → `(S8[0-2]\d)`. The frozen regex captured `805` and
intersected it with `{"S805",…}` — **gate_ids was always 0, so the frozen
QUOTES leg was unsatisfiable** (claim Ca was unreachable with the frozen
instrument). The fix is correct but uncommitted, so: the dry-run receipts name
a counter sha that is no longer the one that will run; SEQ cannot see the
drift (F5); and there is no legal "counter rev1 + re-freeze" path in the
protocol. Any receipt produced now is neither bound to the freeze nor to the
running instrument.

## Recommended exact binding

Freeze-time anchors (claims.json / declaration commit, all knowable pre-data):
`base`, `freeze_ref` (annotated tag `round-67-freeze` at the declaration
commit), and per-claim declared artifact sets. Lands stays declared per claim
(L1 resolution: A_r < A_c < A_ca), but STAMP must enforce:

```
STAMP PASS iff, in --root:
  A1  lands is 40hex and `git rev-parse --verify --quiet <lands>^{commit}` resolves
  A2  head = git rev-parse HEAD          # HEAD, never `main`
      head == lands
  A3  git status --porcelain --untracked-files=normal  == ""   # tracked AND untracked
  A4  git merge-base --is-ancestor base lands
  A5  git merge-base --is-ancestor freeze_ref lands
  A6  lands != base
  A7  sha256(git cat-file blob lands:reports/round-67/accept-<X>.py) == self_sha
  A8  sha256(git cat-file blob lands:reports/round-67/claims.json)  == sha256(on disk)
  A9  files(base..lands) ⊆ declared set for this claim's interval
      (A_r: S801-S804 + r66 dispositions; A_c: entry + S805-S828;
       A_ca: S829+ rejects + lesson + QUALITY/LOG/SCORECARD/telemetry)
```

Every claim-byte read uses `git cat-file blob <lands>:<path>` (the pattern
already exists at `tools/check-receipt-seq.py:80-82`), not `open(root/path)`;
a verified-clean clone is equivalent but the dirty/untracked gate must be in
`stamp_ok`. Header adds `root`, `head`, `status_clean`, `base`, `freeze`,
`counter_sha`, `claims_sha`, `diffset_sha`, and the claim id. Post-records
topo per receipt: `git rev-parse <carrier>^ == lands` **and**
`sha256(blob carrier:<receipt>) == sha256(receipt file)`; the three receipts are
**not** required to share a stamped value — require the chain
`A_r ≤ A_c ≤ A_ca` via `is-ancestor` and each carrier's parent to equal its own
receipt's lands.

Instrument repair: any post-freeze edit to a counter must land as its own
commit with a new freeze tag (`round-67-freeze-1`); receipts naming a
superseded counter sha are SUPERSEDED, not evidence. This is the missing path
F8 exposes.

## Residual risk / verification gaps
- Authority is process-level: a commit whose diff set matches and whose `main`
  the caller moves can still satisfy A1-A9; the reviewer must take `lands` from
  the L1's lands announcement, not from the lane.
- A3 with untracked files is required for the C claim (the entry is new); a
  clean clone satisfies it, the lane worktree does not.
- I did not run any counter to full PASS (base data absent by design) and did
  not attempt a complete all-legs forgery; F1/F2/F3 are reproduced at the leg
  level, which is sufficient to show the stamp does not gate those bytes.
- I did not test an ambiguous tag named `main` (would need a tag) and made no
  jj writes (forbidden). jj 0.45.1 read-only inspection only.
- Cross-seat: L1 resolved the C-APPEND vs Ca-D4 conflict by per-claim lands
  sequencing; that makes interval diff-sets (A9) mandatory, because at A_ca the
  frozen accept-c APPEND leg would fail if C were re-run there. The counters as
  frozen do not encode claim ids or intervals (F7).
- Tooling: no installs/upgrades performed; no pacman. Used system git and
  jj 0.45.1 (read-only), python3.

Report: .ufo/waves/round-67/w1/RevStampDesign.md
