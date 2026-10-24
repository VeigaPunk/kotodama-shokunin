# RevCounterO — `reports/round-67/accept-o.py` line-by-line review

Seat: RevCounterO (reviewer). Lane tip read-only. No tool installed or upgraded.
Base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`; reviewed at tip
`b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21` (= `main`, tracked tree clean).
Method: read `accept-o.py` (309 lines) and `tools/check-receipt-seq.py` (441 lines)
line-by-line; executed the frozen counter at tip, the base dry-run evidence, all five
mutants, and hand-built adversarial fixtures. Materialised clones were made under
`/tmp` (`git clone --no-local --single-branch --branch main .`) and deleted; the lane
was not written (no git/jj writes; `git status --porcelain --untracked-files=no` is
still empty after every run).

## Verdict

- **MUT_EXPECT pins are correct against the mutants on disk** — every one of the five
  committed mutants exits 1 with `SELFTEST: 13/14` and exactly its single pinned check
  FAILing; no extra FAIL name appears (table below).
- **R66 leg derivation is identical to the CJ's** (`corpus/lessons/round-66-verifier-spotcheck.md`
  §2 re-derivation): `git log -1 --format=%H main -- <receipt>` → `rev-parse <carrier>^`
  → parse the receipt's `measured revision (lane main)`; values re-derive (carrier
  `4589ebdd`, parent `65fe8572`, stamp `65fe8572` ×3). The CJ's fuller re-derivation also
  checked the tree line and counter sha (`f0681e6e`, `987c4bbc`/`b366c25b`/`f206095b` —
  all re-verified here, all match); the R66 leg does not, but does not claim to.
- **Fixture hygiene is temp-only**: all fixture repos are `tempfile.TemporaryDirectory`;
  no write lands in `--root`. Two low-severity hygiene gaps are named below.
- **The frozen predicate passes at tip**: `ACCEPT-O-67: PASS`, 10/10 legs, 3.0 s
  (`--lands b78f8b8e…`). The base dry run fails as recorded, and the counter sha
  `f21e9b43…` matches `dry-run-o.txt` and the committed counter, so revision 0 was not
  edited after freezing.
- **Actionable defects remain** (H1/H2/M1/M2): the tool's own header contract is
  violated for the counter-sha header, the central `--lands` capability has no positive
  fixture (a dead `--lands` still scores 14/14), `STAMP` passes dirty tracked worktrees,
  and the `MUT` leg accepts forged mutants.

## MUT_EXPECT vs actual mutants (executed)

Command: `python3 -B .ufo/waves/round-67/stage/mut-o/<mut>.py --selftest` per mutant;
tool at `SELFTEST: 14/14`, rc 0.

| mutant | pinned list | observed rc | observed count | FAIL line(s) | extra FAIL |
|---|---|---|---|---|---|
| mut1_equality_always_true.py | `moved-receipt-fail` | 1 | 13/14 | `FAIL moved-receipt-fail SEQ-telemetry/moved.txt PASS … equal=True` | none |
| mut2_parent_always_true.py | `topo-wrong-parent-fail` | 1 | 13/14 | `FAIL topo-wrong-parent-fail … TOPO-telemetry/wrongparent.txt PASS …` | none |
| mut3_missing_headers_ok.py | `missing-headers-fail` | 1 | 13/14 | `FAIL missing-headers-fail SEQ-telemetry/bare.txt PASS missing_headers=…` | none |
| mut4_no_carrier_pass.py | `topo-no-carrier-fail` | 1 | 13/14 | `FAIL topo-no-carrier-fail … TOPO-telemetry/never.txt PASS no_carrier` | none |
| mut5_tree_unchecked.py | `tree-mismatch-fail` | 1 | 13/14 | `FAIL tree-mismatch-fail … TREE-telemetry/badtree.txt PASS recorded=ffffffff` | none |

`MUT_EXPECT` names match `claims.json` leg MUT exactly, and each mutant's diff vs
`tools/check-receipt-seq.py` is the single pinned site (`check_headers` eq / `check_topo`
parent / missing-header early leg / no-carrier leg / `check_tree` `actual = h["tree"]`).
The files are tracked at HEAD (`git ls-files` non-empty, worktree clean), so a
materialised clone at lands contains them — the MUT leg is reachable in the prescribed
runtime.

## Findings by severity

All fixes named below are **post-round hardening** of the instrument; revision 0 of the
frozen counter is the r67 predicate and must not be edited mid-wave. The findings are
recorded so the L1 can (a) judge the claim on its actual evidentiary strength and
(b) route the fixes into the next round's counters.

### H1 — a receipt can omit `# counter sha256 (self)` and still PASS; the tool's stated header contract is false

`tools/check-receipt-seq.py:137-145` lists only
`("stamped","evaluated","measured","tree")` for `missing_headers`, and
`check_counter_sha` (`:166-176`) does `if not cpath or not h["counter_sha"]: continue`.
So an absent counter-sha header is *skipped*, even when the counter is paired — while
the module docstring says "every receipt must carry all of … `# counter sha256 (self):
<64hex>`" and "A receipt missing a header line is a FAIL, not a skipped check", and
`claims.json` claim-O says "the default mode asserts stamped==evaluated==measured plus
tree and counter-sha pins".

Reproduction (temp repo, receipt stamped/evaluated/measured equal, tree correct, body
`legs pass`, no sha line, counter paired):

```
python3 -B tools/check-receipt-seq.py --root <tmp> telemetry/nosha.txt tools/c.py
SEQ-telemetry/nosha.txt PASS … equal=True
TREE-telemetry/nosha.txt PASS …
RECEIPT-SEQ: PASS            (rc 0)
```

Same with `--topo` (rc 0, `TOPO… PASS`). This is a bypass of the one header that binds
the receipt to the counter bytes: drop the line and the counter-sha pin silently
vanishes, so a counter edited after measurement cannot be detected. Neither
`accept-o.py` HEADERS (only `bare.txt` missing all four headers) nor the mutant space
(no sixth mutant for missing-sha-accepted) exercises this class, and the selftest's
`sha-mismatch-fail` pins only a *wrong* sha, never the absent one. Fix: add
`counter_sha` to `missing` (or FAIL when a counter is paired and the header is absent)
and add a mutant/HEADERS case.

### H2 — `--lands` (the claim's central new capability) has no positive fixture; a dead `--lands` still satisfies every leg

Every `--lands` assertion in the tool selftest (`lands-absent-is-fail`,
`lands-read-committed`) and in `accept-o.py` LANDS uses a receipt that is *absent* at
lands and expects "unreadable". No fixture ever places a correct receipt *at* lands and
requires PASS from committed bytes — even though claim-O's leg text says the fixture
"still evaluates the receipt at `--lands` (committed bytes)".

I patched only the lands read (`texts[rpath] = read_rev(root, lands, rpath)` →
`texts[rpath] = None`) in a temp copy and ran the selftest:

```
SELFTEST: 14/14   rc=0   (no FAIL lines)
```

So a `--lands` mode that can never evaluate any receipt passes the frozen predicate
(`accept-o.py` LANDS would see FAIL-unreadable + `moved_past=True` on its absent
fixture). It fails closed, so no false PASS is produced by the tool — but the capability
the claim acquires is unproven, and `claims.json`'s "14/14 selftest fixtures pin every
failure class" is false for the lands path.

The positive path does work when exercised directly (temp repo: receipt committed at
lands A, later commit B, `--lands B telemetry/r.txt tools/c.py` → `LANDS PASS … 
moved_past=True`, `SEQ/TREE/SHA PASS`, rc 0). Fix: add a positive fixture
(a receipt present at lands PASSes; worktree-only drift does not change the result), and
register the always-None mutant as mut6.

### M1 — `STAMP` PASSes a dirty tracked worktree; `measured` is not an independent measurement

`accept-o.py:139-157`: `dirty_flag` is computed and printed but never used in
`stamp_ok` (`:152-153`), which is only `mv_rev == lands` + a 40-hex tree. `mv_rev` is used for both
`# evaluated revision` and `# measured revision`, so the three-way equality is true by
construction and says nothing about the bytes actually executed.

Reproduction in a materialised clone at the lands revision, with the cloned counter's
own bytes modified (uncommitted):

```
# tampered counter bytes, uncommitted   (appended to reports/round-67/accept-o.py)
# counter sha256 (self): e1038dce86225cba912db740f34eb7daac271187bf459dd2fae45c4a2506c4ad
STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e dirty_tracked=True
ACCEPT-O-67: PASS
committed accept-o sha: f21e9b436cd2a2a6        worktree accept-o sha: e1038dce86225cba
```

A receipt so produced claims `measured revision = lands` while its recorded counter sha
is not the lands counter; the instrument knows (`dirty_tracked=True`) and does not gate.
Fix: `stamp_ok = … and not dirty_flag` (or FAIL the leg and refuse the receipt), and
derive `measured` separately if it is meant to be a distinct claim.

### M2 — the `MUT` leg accepts forged/stub mutants and does not pin the 14-check remainder

`accept-o.py:236-260` accepts a mutant iff `rc == 1`, each pinned name matches
`^FAIL\s+<name>\b`, and no other `^FAIL\s+(\S+)` names appear. A two-line stub satisfies
it:

```
import sys
print('FAIL moved-receipt-fail')
sys.exit(1)
```

Verified against the counter's own predicates: `missing=[] extra=[] -> accepted: True`.
Nothing checks that the mutant is a byte-diff of `TOOL`, that the other 13 checks ran
and passed, or that `SELFTEST: 13/14` is printed. (The SELFTEST leg is similarly loose:
`"14/14" in out` is a substring test, so `114/14` would pass.) Because mutants are
committed wave evidence, a compromised or careless stage could make MUT green without
exercising the tool. Fix: require the literal `SELFTEST: 13/14` line, require
`git diff --no-index TOOL mutant` to be exactly one hunk at the pinned site (or pin
sha256 of each mutant), and anchor the selftest count with `^SELFTEST: 14/14$`.

### L1 — `FIXTURES` counts fixture *stages*, not lanes

`accept-o.py:186-224,290-291`: one `TemporaryDirectory` with one repo (`f1`); the second
`fixtures_built += 1` follows a commit to the same repo. The leg prints
`lanes=2`, and `claims.json` says "the harness builds >=2 temp git lanes". The code
builds one lane with two record commits. Rename the count or build a genuine second
lane.

### L2 — wrong-parent fixture carries an incidental tree mismatch

`accept-o.py:203-212`: `wrong.txt` stamps `base_anc` (= A) but records
`tree_a = HEAD^{tree}` taken while HEAD = B, so the receipt also fails TREE. The TOPO
leg still requires the exact `TOPO-telemetry/wrong.txt FAIL` string, so mut2 is caught,
but parentage is not isolated in this fixture. Stamp `tree_a = rev-parse base_anc^{tree}`
to keep the leg single-cause.

### L3 — partial `GIT_*` scrubbing in fixture helpers

`accept-o.py:66-80` and `tools/check-receipt-seq.py:63-72` set `GIT_CONFIG_GLOBAL`,
`GIT_CONFIG_NOSYSTEM` and identity, but not `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`
or `GIT_OBJECT_DIRECTORY`. With any of those exported by a calling harness, the fixture
`git init/commit` targets the inherited repo instead of the temp dir. Sibling
`tools/harness/receipt_guard.py` scrubs every `GIT_*`; adopt that here.

### L4 — R66 leg reads `main` (tip), not `--lands`

`accept-o.py:272-286` uses `git show main:<rpath>` and `git log … main`. That is correct
only because the protocol runs the counter in a clone where `main == lands`; `STAMP`
enforces revision equality, so a moved lane is rejected before this leg. In the
prescribed runtime the bytes are identical to the CJ derivation. No action needed, but
do not reuse the leg on a worktree that is allowed to move past the stamp.

### L5 — unclosed file handles

`accept-o.py:104,125` (`open(...).read()` for the counter sha and `self_sha`) leak
handles (ResourceWarning under `-W error`). Cosmetic; use `with`.

## Attacked surfaces (what I tried)

- Mutant pin fidelity: ran all five against the real tool (correct).
- Shortcut/forgery: replaced a mutant with a stub printing the pinned FAIL (accepted, M2).
- Sequence bypass: removed the counter-sha header (PASS, H1).
- Moved worktree: dirty tracked worktree at the stamped revision (PASS, M1); moved `main`
  is correctly caught by STAMP.
- Dead capability: `--lands` always unreadable (14/14, H2).
- False stamp: receipt stamped to lands but measured in a dirty clone (M1 self-sha drift).
- Stale receipts: counter sha `f21e9b43…` matches `dry-run-o.txt` and the committed
  counter, so no post-freeze edit; dry run at BASE fails (control is non-vacuous).
- Duplicates/tier inflation/fabricated anchors: not applicable to claim O.

## Residual risk and verification gaps

- `reports/round-67/telemetry/post-records.txt` (claim O's stated post-records
  `--topo` evidence, per `claims.json` `receipt_protocol`) does not exist at review
  time; it is produced after records land. Dependency, not a defect.
- The receipt-generation run at the final lands commit (clone materialisation, clone
  path, final `--lands`) is L1's step; I verified the counter is runnable and green at
  tip, and that a clone contains everything it needs (tool, counter, mutants all
  tracked at HEAD).
- `accept-o.py`'s in-process STAMP cannot observe the *caller's* clone provenance; H2/M1
  mean the frozen predicate alone cannot distinguish a healthy clone run from a dirty
  or lands-dead run. A post-hoc `check-receipt-seq.py <receipt> <counter>` against a
  clean clone at lands remains the real guard for M1 (the dirty counter sha will
  mismatch); nothing guards H1 except the fix.
- Cross-claim note (CriticFrontier alert, L1 resolution): the frozen C APPEND
  (`accept-c.py:349-376`, `allowed_new = NEW_IDS ∪ {S801..S804}`) and Ca D4
  (`accept-ca.py:207-238`, today-dated rejected count ≥ `len(R66_REJECTS)+2`) are
  jointly satisfiable only under per-claim lands commits — C at A_c, before any S829+
  reject rows exist, Ca at the later A_ca. I re-read both predicates: APPEND compares
  base vs its own tip, so the sequencing is coherent; claim O's A_o is independent
  provided tool + counter + `stage/mut-o/` are in that tree (they are tracked at HEAD).
- Time leg: 240 s cap vs observed 3.0 s — no risk.

Report: .ufo/waves/round-67/w1/RevCounterO.md
