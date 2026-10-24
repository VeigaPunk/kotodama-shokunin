# RevDryRunFidelity — r67 dry-run / control fidelity (QUALITY 8/9/11, seat 1 of the attack wave)

Scope: `reports/round-67/claims.json`, `reports/round-67/telemetry/dry-run-{c,o,ca}.txt`,
`reports/round-67/telemetry/controls-{c,o,ca}.txt`, the three frozen counters, and the
base clone they were run in. Read-only on the lane; all experiments in `/tmp` copies.

## Verdict on the two assigned questions

**Q1 — does the dry run's `--lands` value match the declared `<base>` substitution? YES, all three.**
Each transcript carries `# stamped revision: ad5b52b0ab5691358cd38718ab75649dc9916f9a`, which equals
`claims.base` and equals `accept-c.BASE` / `accept-o.BASE` (`accept-c.py:62`, `accept-o.py:37`; Ca takes
no BASE). `controls-*.txt` records the invocation as
`python3 -B reports/round-67/accept-X.py --root .scratch/eval-base --lands ad5b52b0…`, i.e. the
protocol's pre-landing form (`--root <clone-at-base> --lands <base>`), verbatim modulo the two
declared substitutions. Corroboration: each transcript's `# counter sha256 (self)` equals the
current on-disk counter (`3e5f1a58…`, `f21e9b43…`, `5e8915ac…`), the recorded tree
`de353b04…` == `git rev-parse ad5b52b0^{tree}`, and the base clone's reflog has a single entry
`main@{0}: clone: from …/kotodama-shokunin/.` at `ad5b52b0`. The evidence is against the frozen
counter bytes and the declared base — not a stale revision.
Leg parity is exact: C 13/13, O 10/10, Ca 8/8 declared legs printed, in declared order, no extra
and no unprinted leg.

**Q2 — does every expected-fail leg named in `controls-*.txt` actually fail? YES, every named leg fails.**
C: FILE, SET, ONEID, HOSTS, CAPTURE, TOPIC all FAIL. O: SELFTEST, DIFF, OPTIONS, LANDS, TOPO,
HEADERS, MUT all FAIL (and exactly those). Ca: D1, D2, D3, D4, SEQ, CRITERION, QUOTES all FAIL
(and exactly those). STAMP PASSes in all three, as the controls predict. Caveats are in MEDIUM-4
(boilerplate expectation lines, and C's undeclared RESTATE failure).

The receipts' *fidelity* is the weak part, not the substitution: see HIGH-1/HIGH-2.

## Findings

### HIGH-1 — STAMP does not grade the dirty axis: a lands clone with uncommitted edits passes and is graded
All three counters compute or read the root's tracked-dirty state but none fails on it:

- `accept-c.py:182-206`: `dirty_flag` is computed, printed as `# worktree dirty (tracked)`, printed in
  the STAMP detail — and excluded from `stamp_ok` (`mv_rev == lands and <tree is 40hex>`).
- `accept-o.py:139-158`: identical `stamp_ok`, identical exclusion.
- `accept-ca.py`: **no dirty computation at all** (`grep dirty_flag` matches only c and o); its
  receipt has 5 header lines where c/o have 6.

Demonstrated, not inferred: copied the recorded base clone (`cp -a --reflink=auto .scratch/eval-base
/tmp/r67-dirt`), appended one line to the tracked `LOG.md` (`git status` → `M LOG.md`), then
`python3 -B reports/round-67/accept-c.py --root /tmp/r67-dirt --lands ad5b52b0…`:

```
# worktree dirty (tracked): True
STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=True
… counter proceeded to grade the modified worktree …
COUNTER_EXIT=1   (fails only because the entry is absent at base)
```

Why it matters: the graded artifacts are read from the worktree
(`open(os.path.join(root, ENTRY))`, `open(os.path.join(root, REGISTRY))` in accept-c; `read(root, …)`
in accept-ca), while `--lands` pins only the clone's `main` and the *lands* tree. So at lands a seat
can edit the clone to satisfy any failing leg (add a citation, a row, a manifest line), rerun, and
get `ACCEPT-X-67: PASS` with a receipt that still reads `stamped=<lands> tree=<lands tree>`. The
predicate "every leg prints PASS" cannot distinguish committed from uncommitted bytes. This is the
R66-D3 class ("evaluated bytes ≠ stamped revision") re-entered through the dirty axis, and the
receipt's own `dirty_tracked=True` field is the only trace — an ungraded field.
Asymmetry worth noting: `tools/check-receipt-seq.py` reads committed bytes (`git(root,"show",
f"{rev}:{path}")`, line 81) and `accept-o.py`'s R66 leg reads `git show main:{path}`, so the *tool*
is immune; the two counters that carry claims C and Ca are not.
Fix: `stamp_ok &= not dirty_flag` in c/o and add the same computation to ca, and/or bind every graded
read to `git show <lands>:<path>`.

### HIGH-2 — Ca's SEQ leg (the round's own protocol audit) passes on a do-nothing counter
`accept-ca.py:241-256` certifies the three counters by substring tests over source text:
`"--lands" in text and "required=True" in text`, `"stamped revision" in text and "evaluated
revision" in text`, `"mv_rev == lands" in text`. Comments satisfy all three. Demonstrated:
`git clone --shared . /tmp/r67-tip` (main = b78f8b8), replaced `reports/round-67/accept-c.py` with a
5-line stub that only carries those four strings in comments and prints `no-op`, then
`python3 -B reports/round-67/accept-ca.py --root /tmp/r67-tip --lands b78f8b8…`:

```
STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e
SEQ PASS bad=[]
```

A counter that would never require `--lands`, never print the headers, and never compare
stamped/evaluated satisfies SEQ. Because SEQ is the sole leg that pins the protocol across *all
three* counters (C and O each pin only themselves, behaviorally), ACCEPT-CA-67's central r66-D3
disposition rests on a comment-satisfiable check. Fix: anchor the markers to executable constructs
(AST: `add_argument("--lands", required=True)`, a `Compare` node on `lands`), or pin each counter's
sha256 in accept-ca.py and in claims.

### MEDIUM-3 — SEQ conflates "file absent" with "protocol absent"; the control never exercises SEQ's discrimination
The base clone contains zero files under `reports/round-67` (`git -C .scratch/eval-base ls-tree -r
--name-only HEAD -- reports/round-67 | wc -l` → 0), yet `dry-run-ca.txt` reports
`accept-c.py:no_required_lands`, `:no_headers`, `:no_equality_assert`. `read(root, cpath) or ""`
turns absence into an empty string, which then fails all three substring tests with a
non-compliance diagnostic. So the only pre-data exercise of SEQ is a missing-file exercise: nothing
in the controls shows SEQ rejecting a *present but non-compliant* counter — and per HIGH-2 it would
not. Fix: emit `<path>:absent` when `read()` returns None, and add a fixture counter without
`--lands` to the control.

### MEDIUM-4 — the three `controls-*.txt` expectation lines are one boilerplate string; C's expected set is incomplete
`md5sum` differs only by the claim token; the files are byte-identical except `controls-c`↔`controls-o`
↔`controls-ca` and `ACCEPT-X-67`. Each file therefore names the legs of counters it does not run
(controls-c.txt names O's and Ca's legs; controls-o.txt names C's and Ca's legs). For C the named set
also *omits* a leg that actually failed: `dry-run-c.txt` has `RESTATE FAIL bad=['S805:bullets=0',…]`
while controls-c.txt names only FILE/SET/ONEID/HOSTS/CAPTURE/TOPIC. All named legs do fail (Q2 above),
so this is a control-quality defect, not a false control: the declared expectation was not generated
from the transcript, which is exactly the copying pattern that hid r66's defect. Fix: per-counter
expected sets derived from the transcript, and name the expected-PASS legs too — on base, C passes
ROWS/LINK/APPEND/NOHARM/SWEEP vacuously and O passes R66/FIXTURES, so a revised counter could go
degenerate (e.g. only FILE failing) and still satisfy "the control fails".

### MEDIUM-5 — O's FIXTURES leg text overstates its check and passes where the tool does not exist
claims.json O leg: "FIXTURES: the harness builds >=2 temp git lanes **and runs the tool via subprocess
inside 240s**". Code (`accept-o.py:290-291`): `fixtures_built >= 2 and wall < 240`. The leg reads no
tool return code; it PASSes at base with zero tool invocations succeeding (`dry-run-o.txt`:
`FIXTURES PASS lanes=2 wall=0.1s`, while SELFTEST/OPTIONS/LANDS/TOPO/HEADERS all report exit=2 for
the missing tool). Fix: assert at least one fixture invocation's rc/out inside the leg, or narrow the
leg text to "builds >=2 lanes within 240s".

### MEDIUM-6 — the recorded control recipe does not pin base, and the transcripts are not self-describing
controls-*.txt records `git clone --no-local --single-branch --branch main . .scratch/eval-base &&
python3 -B reports/round-67/accept-X.py --root .scratch/eval-base --lands ad5b52b0…`. That clones
whatever `main` is at run time; it materialized base only because the dry runs (mtimes 09:33:13-19)
preceded the freeze commit `b78f8b8` (committed 09:33:22). Re-running the recorded command today
yields a clone at `b78f8b8`; with `--lands ad5b52b0` it dies at
`STAMP FAIL stamped=ad5b52b0 evaluated=b78f8b8e equal=False … ACCEPT-C-67: FAIL` — a different
failure shape than the leg-level failures the control asserts, so the control cannot be replayed as
written. Separately, `dry-run-*.txt` contains no `# command:`, no argv, no exit status; the
"observed: … (exit 1)" claim lives only in the hand-written header. Fix: `git clone … && git -C
<clone> checkout --detach <base>` (or `reset --hard`), and have the counter print its own argv and
exit line into the receipt.

### LOW-7 — `# measured revision (lane main)` is the clone's `main`, not the lane's; measured ≡ evaluated
Both fields print the same `mv_rev` (`accept-c.py:187-188`, same in o/ca). Demonstrated false label:
`accept-c.py --root .scratch/eval-base --lands b78f8b8…` printed
`# measured revision (lane main): ad5b52b0ab5691…` while the lane's `main` was `b78f8b8e…`. In the
canonical lands run they coincide, but the receipt's third revision is not an independent
measurement, so the "stamped + evaluated + measured" trio is two values; the closure hand-check of
`stamped==evaluated==lands` gains nothing from it. Fix: derive the lane revision from the lane, or
rename the field to `# measured (root main)`.

### LOW-8 — malformed tree header when `--lands` is unresolvable in the root
`git rev-parse <lands>^{tree}` echoes its argument on failure, so the header prints
`# tree: b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21^{tree}` (observed in the wrong-lands run in
`.scratch/eval-base`) instead of `unresolvable`. No bypass — the string is not 40-hex, so `stamp_ok`
fails — diagnostics only. Fix: run `rev-parse --verify` and map empty/echo to `unresolvable`.

### LOW-9 — C's TOPIC leg prints its pass condition on failure
`dry-run-c.txt`: `TOPIC FAIL entry topic text appears verbatim in the README row`. Every other
failing leg prints a bad-list; this one reads as a success sentence. Fix: print the entry's `- topic:`
text and/or the nearest README row.

### LOW-10 — Ca's receipt is the weakest of the three
`dry-run-ca.txt` has no `# worktree dirty (tracked):` header and its STAMP detail omits
`dirty_tracked`; accept-ca.py never computes it. The claim *about* receipt discipline therefore
carries the least receipt discipline (see HIGH-1). Fix: align all three headers in one change.

## Addendum — post-IRQ verification (still pre-data, 2026-10-24)

### HIGH-11 — the frozen Ca instrument rev0 could never pass, and its hot-fix is uncommitted and post-control
`git show HEAD:reports/round-67/accept-ca.py` line 272 (the byte sequence pinned by
`dry-run-ca.txt` as `5e8915ac…`) reads:

```python
gate_ids = set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {
    f"S{n}" for n in range(805, 829)}
```

The captured group is the digits only (`"805"`), the intersection set is `"S805"…"S828"`, so the
intersection is empty for *every possible* lesson text and `len(gate_ids) >= 20` (`accept-ca.py:274`)
is permanently False. QUOTES was an always-FAIL leg: ACCEPT-CA-67 was unsatisfiable as frozen, and no
lands commit could have rescued it. The worktree now carries the correct capture group
(`\b(S8[0-2]\d)\b`, current sha `5382ffed6f6c…`, `git status` → `M reports/round-67/accept-ca.py`),
while `claims.json` still says `statement_revision: revision 0` and both `dry-run-ca.txt` and
`controls-ca.txt` still record `5e8915ac…`. Consequences:
1. the Ca pre-data control is stale with respect to the counter that will be committed — regenerate
   the base dry run and re-file the control (pre-data is the only time this is clean), or bump
   `statement_revision` and file the delta;
2. the base control **could not** have caught it: at base `corpus/lessons/round-67.md` is absent, so
   `lesson_text = ""`, `gate_ids = 0`, the quote tool exits non-zero — QUOTES fails for absence
   either way. This is the general form of MEDIUM-3: an absence-driven base failure cannot
   distinguish a discriminating predicate from a permanently-failing one. The same blindness applies
   to D1–D4;
3. pre-data controls need a **reachability** leg, not only a base-failure leg: at least one fixture
   root where every non-data leg can print PASS (for Ca: a lesson file carrying ≥20 gates ids and a
   clean quote-tool exit; for C: a synthetic registry+entry; for O: such a root already exists in its
   fixture lanes). Without it, "counter fails at base" is satisfied by a counter that can never pass.

I checked O's leg literals against the tool and they are all reachable
(`unreadable`, `moved_past=True`, `missing_headers`, `equal=`, `parent=`, `RECEIPT-SEQ: PASS` all
occur in `tools/check-receipt-seq.py`), and its `14/14` was verified at the freeze tip. HIGH-11 is
specific to Ca's QUOTES leg.

### MEDIUM-12 — the C-APPEND vs Ca-D4 id conflict is real, and the L1's per-claim lands resolution is sound only under three conditions
Confirmed in source: `accept-c.py:357` `allowed_new = set(NEW_IDS) | EXTRA_IDS` with
`EXTRA_IDS = {"S801"…"S804"}` (`:70`) and `append_ok = not missing_old and not extra_ids and not
mutable_bad`, so any S829+ row inside the clone evaluated by accept-c is `extra_ids` → APPEND FAIL.
`accept-ca.py` D4 counts rows whose status cell is `rejected` and whose opened cell is `2026-10-24`
and requires `>= len(R66_REJECTS)+2 = 6`. Base registry is 724 rows (verified in `.scratch/eval-base`),
so C's statement is 752 at its lands and Ca needs ≥754 at its own. The resolution — C's receipt at
A_c (only S805-S828 appended over base), Ca's at a later A_ca carrying the S829+ rejects — is
mechanically satisfiable, but only if:
1. **A_c contains no S829+ row** (a clone of A_ca would fail APPEND; the C evaluation must be a clone
   at A_c, never at tip);
2. **each receipt is committed in a records commit whose parent is its own lands commit**:
   `check_topo` grades `git log -1 main -- <receipt>` parent == *that receipt's* stamped, per receipt
   (no shared-lands assumption), so a receipt added inside its own lands commit, or touched by any
   later commit, breaks TOPO;
3. **claims.json C's row-count sentence is scoped**: "registry 724 -> 752 rows" is true at A_c and
   false at tip (≥754), so it must say "at C's lands commit" or closure will read it as a false
   statement. Likewise Ca's D1 exclusion list must name the wave scratch clone trees (a 172 MB
   `w1/scratch/eval-tip` clone existed during this review and is not gitignored).

Additional tool-level defect found while checking the sequencing: `check_counter_sha`
(`tools/check-receipt-seq.py:160-174`) reads the **worktree first** (`read_worktree` then
`read_rev(main)`) even in `--lands` mode, so the counter-sha pin is not lands-scoped on a dirty clone
— it never reads `<lands>:<counter>`. Same class as HIGH-1: neither the counters nor the tool fail
on a dirty evaluation root.

## Positive evidence recorded (so it is not re-litigated at closure)
- `--lands` substitution = declared base for all three; counter shas and base tree match disk.
- Leg parity exact: 13/13, 10/10, 8/8, declared order preserved, no shadow legs.
- All expected-fail legs named in the controls do fail; STAMP passes at base in all three, as declared.
- O's `14/14` selftest is not aspirational: at the freeze tip, `python3 -B tools/check-receipt-seq.py
  --selftest` exits 0 with 14 `PASS <fixture>` lines and `SELFTEST: 14/14` (the `RECEIPT-SEQ: FAIL`
  lines in that output belong to the negative fixtures).
- The base clone is still at base and clean, so base-time reproduction remains possible.

## Residual risk / verification gaps
1. The second control declared in `claims.json:112` — "the same counters on the live worktree with
   `--lands <worktree-tip>` also fail legs" — has **no receipt**. It is not redundant: SEQ is
   root-scoped, so on the live worktree (where `reports/round-67/*` existed as untracked files) SEQ
   would have PASSed while on the clone it failed for absence. Either file the transcript or strike
   the sentence by claim revision; do not let closure cite a control nobody has evidence for.
2. I reproduced C at base (identical leg set, exit 1) but not O/Ca byte-for-byte: their transcripts
   are one-shot and the invocation exists only in prose. MEDIUM-6 is the remedy.
3. Unicode/whitespace attack not attempted (no leg compares transcript bytes to a canonical form, so
   nothing to attack there).
4. `.ufo/waves/round-67/w1/scratch/eval-tip` — a 172 MB `git clone` (main `b78f8b8`) — existed during
   this review and disappeared mid-run; `.ufo/waves/round-67/w1/` was not gitignored at the time
   (`git check-ignore` rc=1). If the L1 blanket-adds `w1/`, that clone tree lands and defeats R66-D1.
   The D1 manifest must name such scratch trees as excluded (claim Ca requires exclusions named).
5. I did not audit semantic leg content (rows, citations, manifest adequacy) — that is the CensusE12 /
   EntrySpec / SourceSupport / ManifestSep seats' scope.
6. Tooling: no installs were needed (pacman paused per the orchestrator ruling; nothing required).

Report: .ufo/waves/round-67/w1/RevDryRunFidelity.md
