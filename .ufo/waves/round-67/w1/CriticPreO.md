# CriticPreO — pre-data attack on ACCEPT-O-67

Scope: `reports/round-67/accept-o.py` (rev0, sha `f21e9b43…`) + `tools/check-receipt-seq.py`
(sha `3e06e502…`, both committed in instruments commit `b78f8b8`) + `stage/mut-o/` mutants.
Attacks assigned: wrong-tree stamped==evaluated receipts, `--topo` committed-twice/merge
carriers, unregistered/stub mutants, fixture spoof. All experiments run in
`tempfile` lanes; the lane repo was only read (plus one in-place smoke run of the
counter, which mutates nothing outside `/tmp`).

Baseline: `python3 -B reports/round-67/accept-o.py --root . --lands b78f8b8e…` on the
live worktree → `ACCEPT-O-67: PASS` (all 10 legs, 3.1s). The instruments *work*; the
findings below are the holes that remain.

---

## F1 — STAMP PASS on a dirty/diverged worktree: "stamped==evaluated, wrong tree" (HIGH, fixable)

`accept-o.py` computes `dirty_flag` (`git status --porcelain --untracked-files=no`),
prints it in the receipt header and in the STAMP detail — **and then never gates on
it**. `stamp_ok` is only `main == lands and lands^{tree} resolvable`. STAMP also never
checks `HEAD == main`, so `lands` and the worktree can diverge completely.

Demonstrated: fixture repo where `tools/check-receipt-seq.py` is committed (real
bytes), `lands == main`, then the worktree file is overwritten with an uncommitted
attacker stub (`print('14/14'); sys.exit(0)`). Counter output:

    # stamped revision: 1db9cfc7…
    # evaluated revision: 1db9cfc7…
    # worktree dirty (tracked): True
    STAMP PASS … equal=True tree=0fa64783 dirty_tracked=True
    SELFTEST PASS exit=0 count=True        ← produced by the STUB, not committed bytes

The receipt header records `stamped == evaluated == lands` while the behavior under
measurement is uncommitted bytes. That is exactly the "lands matches but contents
moved" case: **STAMP does not fail**; only downstream legs can catch it, and here the
stub even satisfied SELFTEST. Every git leg (DIFF/R66) reads *committed* bytes while
SELFTEST/OPTIONS/LANDS/TOPO/HEADERS execute *worktree* bytes — split-brain by design.
A lands commit whose committed tool is a DIFF-satisfying stub + worktree-copied real
tool yields a fully-valid receipt for bytes that never existed in history.

Axes: O (capability claim — receipt protocol is the claim); Ca (SEQ leg + the same
`--lands` protocol in accept-c/accept-ca inherit the pattern if copied).

Smallest safe correction: `stamp_ok = … and not dirty_flag and
git rev-parse HEAD == lands` (HEAD==main==lands, clean tracked worktree). One line;
no fixture cost.

## F2 — `--lands` mode reads WORKTREE counter bytes (HIGH, fixable)

Tool docstring: "`--lands` … receipt reads come from `git show <hash>:<path>`
(committed bytes), never a worktree" — but `check_counter_sha` does
`read_worktree(root, cpath)` **first**, falling back to `main:` only on OSError,
in every mode. Demonstrated (E4c): receipt `r2.txt` committed in `C`, stamped to `A`,
counter `tools/counter-x.py` clean at `C`; then one uncommitted edit to the counter:

    LANDS PASS lands=1dce0e1c … moved_past=False (evaluating committed bytes at lands)
    SEQ-… PASS equal=True    TREE-… PASS
    SHA-telemetry/r2.txt FAIL tools/counter-x.py recorded=14f95ddd actual=bfb454af

Receipt committed bytes are identical and valid; the FAIL is caused purely by
uncommitted worktree drift — so post-hoc `--lands` re-verification of old receipts
(the whole point of the mode) breaks under any touched worktree. Symmetrically, a
receipt can attest sha256 of *uncommitted* counter bytes: put weaker counter bytes
in the worktree, record their sha, `--lands` still certifies them.

Correction: in `--lands` mode resolve counter bytes via `git show <lands>:<cpath>`
(or `<stamped>:<cpath>`), never `open()`. ~4 lines.

## F3 — `--topo` accepts a receipt never committed on `main` (merge carrier) (HIGH, fixable)

`check_topo` finds the carrier with `git log -1 --format=%H main -- <path>`.
Path-simplified log *follows into side branches*: demonstrated (E6a) — receipt
committed only on `side` (parent `A`), then merged into `main` by `M`:

    TOPO-telemetry/r.txt PASS carrier=fe7ad399 parent=55e0fa38 stamped=55e0fa38
    → carrier == side commit S, rc=0, RECEIPT-SEQ: PASS

The receipt was never the object of any `main`-line records commit; the "carrier"
is a commit on a branch that `main` merely merged. Stamping `S^ = A` passes. So
provenance can be faked through arbitrary side histories (incl. `jj` colocated
workspaces, cherry-picks, vendored branches): the predicate certifies *reachability
+ parentage of some commit*, not *main-line records-carrier* — a hidden authority
the claim's "receipts carried by B on main" framing does not admit.

Also demonstrated (E7): identical receipt bytes committed in `B` on main AND in `S`
on a side branch, merged `M` → carrier reported `B`, PASS — benign but shows the
"carrier" is ambiguous under TREESAME merges; the tool cannot distinguish first-class
provenance from duplicated bytes.

Correction: `git log --first-parent -1 --format=%H main -- <path>` (the merge `M`
becomes the carrier → `M^ ≠ stamp` → FAIL), or explicitly document that
any-side-branch carriers are acceptable evidence.

## F4 — MUT leg has no mutant-provenance check; stubs pass (HIGH, fixable)

The leg requires `rc==1` + `FAIL <expected>` + no extra FAIL lines — and nothing
about the mutant being a mutation of the tool. Demonstrated (E1): five files
consisting only of `import sys; print('FAIL <check>'); sys.exit(1)` satisfy all of
`MUT_EXPECT`; the leg prints `MUT PASS mutants=5 bad=[]`. The committed mutants are
real 1-line mutations (verified: each diffs `check-receipt-seq.py` in exactly one
line) — but the *counter* would pass a wave that ships printed stubs, and the
`mut_count == len(MUT_EXPECT)` count check does not bind content either.

Correction: for each registered mutant, diff against `tools/check-receipt-seq.py`
and require a bounded delta (e.g. `git diff --stat`-style ≤2 changed lines), or pin
each mutant's sha256 in MUT_EXPECT. ~10 lines in the counter.

## F5 — `GIT_*` env vars reach every git call in counter AND tool (MED, fixable)

Both `git()` helpers do `env = dict(os.environ)` and only neutralize config
(`GIT_CONFIG_GLOBAL`, `GIT_CONFIG_NOSYSTEM`). Demonstrated (E2): `GIT_DIR=<atk>/.git`
overrides `git -C <root>` entirely — `rev-parse HEAD` inside a fresh fixture
directory returned the *attacker's* HEAD. `GIT_INDEX_FILE`, `GIT_WORK_TREE`,
`GIT_OBJECT_DIRECTORY` likewise survive, so in a poisoned environment every fixture
"commit" and every `git show/log` can be redirected to a prepared repository —
fixture evidence is fabricated wholesale.

Correction: in `git()` env, `env = {k: v for k, v in os.environ.items()
if not k.startswith("GIT_")}` then re-add the config pins + AUTHOR/COMMITTER.

## F6 — `tools/` sibling modules shadow stdlib for the tool (MED, fixable)

`python -B tools/check-receipt-seq.py` puts `<root>/tools/` at `sys.path[0]`.
Demonstrated (E8): a wave-landed `tools/re.py` is imported by the tool instead of
stdlib `re` (observed: hard crash; a competent shim would silently control every
header regex — e.g. `fullmatch` that always matches — giving total spoof). No leg
audits for extra files under `tools/`; DIFF only diffs the tool's own path.
Same vector for `argparse.py`, `subprocess.py`, `hashlib.py`, `sys.py`…

Correction: counter invokes the tool as `python -I` (isolated: no script-dir in
`sys.path`, env-stripped — also fixes PYTHONPATH bleed); optionally a leg asserting
no new `tools/<stdlib-name>.py` landed.

## F7 — `# counter sha256` is optional even when a counter is paired (MED, fixable)

Docstring: "every receipt must carry **all of** … `# counter sha256 (self)`".
`check_headers` requires only stamped/evaluated/measured/tree; `check_counter_sha`
silently skips when `h["counter_sha"]` is None. Demonstrated (E5): receipt with four
headers, no sha line, run paired with `tools/counter-x.py` → `RECEIPT-SEQ: PASS`,
exit 0 — the counter-provenance pin is voidable by omission. No mutant covers the
SHA leg (MUT coverage gap: mut1-5 pin SEQ/TOPO/TREE only).

Correction: when a counter is paired (`cpath` non-None), treat missing
`counter_sha` as FAIL; else fix the docstring. Add a mutant (`mut6_sha_unchecked`).

## F8 — stale-clone freshness is unverifiable by design (MED — tradeoff, needs external discipline)

"a materialized clone at the lands commit" guarantees `main == lands` *inside the
clone* — so a clone materialized of a superseded commit still emits
`evaluated == stamped == lands`, `STAMP PASS`, all legs green (BASE is still an
ancestor, R66 still resolvable). Nothing binds `--lands` to the commit the wave
intends to land; the receipt is cryptographically self-consistent about a stale
stamp. The counter cannot fix this — the *operator/runbook* must bind lands to the
landing event (e.g., record `git rev-parse main` of the lane at evaluation time in
the manifest, or have the post-records step confirm `lands ∈ parents(tip)` via
`--topo` on the counter's own receipt). Flagging so the closure's
"re-verified by hand" step explicitly checks `lands` ancestry into the tip.

## F9 — moved_past edge semantics (LOW, cosmetic)

`moved = rev-list --count lands..main > 0` counts only commits reachable from main.
`lands` ahead of `main` (lands not yet merged) → `moved_past=False`; divergent →
True. The flag is informational only, but "moved_past" mislabels the divergent/ahead
cases. One-line fix: also compute `main..lands` or use `--left-right --count`.

## F10 — R66 leg reads `measured` as the stamp proxy (LOW, accurate-only)

For each r66 receipt the leg greps `measured revision (lane main): 65fe8572` and
calls it "their stamped" — r66 receipts predate the stamped/evaluated/measured
triplet so only `measured` exists; the leg is correct as re-derivation, but the
claim text overstates it as checking "their stamped". Also uses the same
non-`--first-parent` `log -1` as F3 (pinned carrier hash makes it harmless here).

---

## Verified-holding (attacked, held)

- Unregistered mutant → `MUT FAIL fname:unregistered` (code, MUT_EXPECT.get → mut_bad).
- Receipt committed twice **on main** (E6b): carrier = latest toucher → TOPO FAIL.
- stamped≠evaluated → `equal=False` FAIL; missing stamped/evaluated/measured/tree →
  `missing_headers` FAIL; receipt absent at `--lands` → `unreadable` FAIL;
  unresolvable/bad-format `--lands` → exit 2; lands==base dry-run → claim legs FAIL
  (dry-run-o.txt controls hold).
- claims.json O-leg names == counter leg names (STAMP…FIXTURES); mutants are true
  1-line byte-mutations of the tool (all 5 diffed).

## Cross-seat note

CriticFrontier's C-APPEND vs Ca-D4 id-conflict alert was superseded by the L1 ruling
(per-claim lands sequencing A_r < A_c < A_ca) — recorded, no action in O-scope.

## Installs

None. (pacman paused per guard; no tools needed beyond python3/git.)
