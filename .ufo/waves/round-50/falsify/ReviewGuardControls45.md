# ReviewGuardControls45 — round 50 falsify: are the 45 original `receipt_guard --selftest` controls unchanged?

Seat: `KotodamaR50-2.ReviewGuardControls45-21` (reviewer, leaf). Axis judged: **operability**.
Landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Method: private `git clone -q --shared` of the lane into `/tmp/r50c-guard` (base) and `/tmp/r50c-head`
(landed), `GIT_CEILING_DIRECTORIES=/tmp`, `python3 tools/harness/receipt_guard.py --selftest` in each
clone; landed bytes read with `git show <sha>:<path>`, never from the lane working tree. No installs
were needed (`git`, `python3` only). I made **no** change to the lane repo: no `git add/commit/
checkout/reset/stash`, no jj command, no edit to any lane file other than this report; all mutation
copies were made under `/tmp` and deleted.

> **Lane working tree diverged from the landed commit during this review.** At the start
> `git status --short` showed only `M reports/round-50/run-validation.py` plus untracked
> `.ufo/waves/round-50/*` and `reports/round-50/validation.json`. By the end of the session the
> working tree additionally showed `M tools/harness/receipt_guard.py`, `M corpus/SOURCES.md`,
> `M corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`,
> `M corpus/lessons/round-50.md`, `M reports/round-50/jj-colocation-probe.py` and a new
> `?? reports/round-50/telemetry/jj-probe-v3.txt`. These are **not mine** — they are concurrent
> sibling agents working in the lane. Concretely, the working-tree `tools/harness/receipt_guard.py`
> now contains an unlanded `refs/jj/root` special case in `_head_state` and a changed
> `_enumerate_refs` symbolic-ref policy. **Every measurement in this report is against the landed
> commit bytes only** (private clones at `4ad2683` and `1c779e4a`), so these concurrent edits do not
> affect any finding below — but any re-measurement must likewise use the landed bytes, not the
> working tree.

Byte identity of what was measured:

| bytes | sha256 |
|---|---|
| landed `tools/harness/receipt_guard.py` | `5a61c35016b61c71071d774773b329a4bb6646f9959bd3b82a15528b328cef14` |
| base `4ad2683 tools/harness/receipt_guard.py` | `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` |

## Item attacked and verdict

**Item:** claim O's clause *"Existing selftests keep every control; new controls added"* /
`after_required`: *"receipt_guard --selftest and check-readme-revisions --selftest pass with all
prior controls retained"* — narrowed to the specific question I was given: **do all 45 original
`receipt_guard --selftest` controls survive unchanged in name, order and expectation at the landed
commit?**

**Verdict: HOLDS** for name and order (exact), and **HOLDS with one documented, defensible
exception** for expectation: 44 of 45 controls are byte-identical in name, order, exit code and
asserted substrings; the 45th, `runner-rechecks-before-publisher`, had its **fixture** amended and
one **extra** conjunct added to its assertion. The amendment is *required* by the landed
implementation (proven by mutation below) and it **strengthens** the control rather than weakening
it: it converts a control that had become vacuous under the new multi-ref probe into one that
actually exercises the two-phase recheck. It is not a silent weakening.

## Evidence

### 1. Ordered control names: identical, first 45 positions byte-for-byte

```
$ cd /tmp/r50c-guard && python3 tools/harness/receipt_guard.py --selftest > /tmp/selftest_base.json
base  : controls_total=45 controls_passed=45   exit=0
$ cd /tmp/r50c-head  && python3 tools/harness/receipt_guard.py --selftest > /tmp/selftest_head.json
landed: controls_total=69 controls_passed=69   exit=0   (3 consecutive runs: 69/69 each, deterministic)
```

```
base n= 45 head n= 69
first45 identical & ordered: True
prefix diff at: None
base names missing from head: []
duplicates in head: []
base order == head[:45] exactly: True
base names in head at same index: True   (all 45 at identical index)
index 44: corrupt-head-fails-closed   index 45: r50-detached-below-remote
```

The 24 new controls are appended strictly **after** the original 45 (`_landing_controls(...)` is
called at landed `receipt_guard.py:685`, i.e. after `corrupt-head-fails-closed` at `:683`). None of
the new names collides with an original name; the three non-`r50-` new names
(`attached-head-holds-refused`, `unborn-local-branch-refused`, `other-local-branch-refused`) are
distinct from all 45 originals.

### 2. Per-control expectation: 44/45 byte-identical, 1/45 amended (and strengthened)

Machine diff of the two `selftest_receipt` bodies (base `:201-352`, landed `:538-694`):

```
15c15
<         head = _head_commit(root)
---
>         head = _head_state(root)[0]
130a131
>         (root / ".git/refs/heads/control").unlink()
134c135,137
<             f"    Path({str(root / '.git/HEAD')!r}).write_text('ref: refs/heads/control\\n', encoding='ascii')")
---
>             "    print('RUNNER-CALLED')\n"
>             f"    Path({str(root / '.git/HEAD')!r}).write_text('ref: refs/heads/control\\n', encoding='ascii')\n"
>             f"    Path({str(root / '.git/refs/heads/control')!r}).write_text({head + chr(10)!r}, encoding='ascii')")
139a143
>                          and "RUNNER-CALLED" in result.stdout
142a147,148
>
>         _landing_controls(work, controls, env, script)
```

Per-control record comparison across the two runs:

```
key-set differences among 45: 0
expected_exit mismatches: none (all 45 equal)
base limits == landed limits (byte-identical strings)
```

Every one of the 45 passes at both commits (`b_pass`/`h_pass` all `True`), with identical exit codes
and identical expected exit codes. The only per-control stderr differences are the **additive**
identity fields of the landed diagnostic (`landed_ref=`, `landed_sha=`, `landed_blob=`, `hit_refs=`)
and the wording of one fail-closed message:

- base `corrupt-head-fails-closed` → `reading HEAD failed (exit 1)`
- landed `corrupt-head-fails-closed` → `reading the symbolic HEAD failed (exit 128): fatal: No such ref: HEAD`

Both are `RECEIPT-GUARD-GIT`, both exit 3 — the *control's* asserted substring
(`RECEIPT-GUARD-GIT`) and exit code are unchanged; only the free-text message differs. The landed
`_head_state` reads `symbolic-ref` before `rev-parse`, so the same corrupt-HEAD condition is
reported through a different probe. Not a control-expectation change.

### 3. The amended fixture is REQUIRED, not cosmetic — mutation proof

The landed implementation probes HEAD **and every `refs/heads/*` / `refs/remotes/*`** ref, so the
base fixture for `runner-rechecks-before-publisher` (which left `refs/heads/control` present and
pointing at the receipt-bearing commit) is *already* refused at the **first** guard call, before the
runner callback runs. Under the base fixture the base assertion still passes — but vacuously, since
the recheck path is never reached. Direct probe under the landed implementation, base fixture:

```
[BASE fixture (refs/heads/control present) under HEAD impl] exit=3 runner_called=False receipt_unchanged=True committed_diag=True
      stderr: refusing overwrite ... committed_sha=none committed_blob=none landed_ref=none landed_sha=none landed_blob=none hit_refs=refs/heads/control; explicit REFRESH_RECEIPTS=1 required
[AMENDED fixture (control ref unlinked, restored by runner) under HEAD impl] exit=3 runner_called=True receipt_unchanged=True committed_diag=True
      stderr: refusing overwrite ... committed_sha=bc6240a7... committed_blob=203e7040... landed_ref=none ...
```

So the landed amendment (unlink `refs/heads/control` before the runner; the runner restores HEAD
*and* the ref file; assert `RUNNER-CALLED` in stdout) is exactly what makes the control still test
the second guard call. Confirmed by three mutations:

- **M1** (landed impl, second `guard_receipt` deleted from `round_runner_main`) → `runner-rechecks-before-publisher`
  **FAILS** (exit 7 instead of 3). The control has teeth at the landed commit.
  The same mutation on the base impl also fails that one control (45 → 44), so base had teeth too.
- **M3** (landed impl, fixture reverted to base form, landed assertion kept) → `runner-rechecks-before-publisher`
  **FAILS**. Proof the fixture change is load-bearing under the landed probe.
- **VAC** (landed impl, base fixture *and* base assertion) → control **PASSES** but
  `runner_called=False`, i.e. the base expectation is satisfied without exercising the recheck.
  This is precisely the vacuity the amendment removes.

Portability: applying the landed fixture+assertion to the **base** implementation still gives 45/45
pass, so the amendment does not depend on the new multi-ref probe; it is valid under both.

### 4. The original 45 still have teeth against the landed guard's own logic

| mutation | effect on the 45 original controls |
|---|---|
| M9 — `_committed_entry` never finds a committed entry | 19 original controls fail (incl. `committed-refused`, `runner-rechecks-before-publisher`) |
| M10 — committed refusal never raised | 18 original controls fail |
| M7 — refresh accepts any non-empty value | 6 original controls fail (`nonexact-refresh-*`) |
| M8 — `landed_*` taken from a local branch instead of a remote | 0 original controls fail (only new `r50-*` controls catch it — see residual risk) |
| M11 — `_enumerate_refs` returns nothing (regress to HEAD-only) | 0 original controls fail; 17 new controls fail |

M11 is the important one: **the original 45 cannot detect a regression that drops the multi-ref
probe.** The landed work compensates with 24 new controls, so total coverage is intact — but the
"prior controls retained" clause alone does not carry that guarantee, and it never did.

### 5. Pre-existing gap (present at base too, not introduced by this wave)

Removing the symlink path check (`stat.S_ISLNK` branch) kills **zero** controls on **both**
commits (45/45 base, 69/69 landed). The `symlink-alias-refused-*`, `symlink-ancestor-refused-*`
and `symlink-dotdot-refused-*` controls assert only the `RECEIPT-GUARD-PATH` token, and the
non-symlink path check catches those cases anyway. Identical at base ⇒ pre-existing, out of this
wave's scope, recorded as residual risk only.

## Residual risk / verification gaps

1. **Original-45 blind spot (low, compensated).** M11 shows no original control detects loss of the
   `refs/heads`/`refs/remotes` probe. The 24 new controls do. If a future wave removes the new
   controls, the whole regression class becomes undetectable from the original set alone.
2. **Pre-existing symlink-check gap (low, pre-existing).** Removing `S_ISLNK` detection changes
   nothing observable in either control set. The four `symlink-*`/`hardlink-*` controls assert a
   diagnostic *token*, not a distinct message, so they cannot tell the symlink branch apart from the
   regular-file branch.
3. **The landed receipt does not record control-level retention.** `reports/round-50/validation.json`
   (`claims.O.after.values`) records only `receipt_guard_selftest_rc: 0` and a stdout tail
   containing `"controls_passed": 69, "controls_total": 69`; `run-validation.py:347-373`
   (`selftest_run`/`measure_o`) captures no ordered control-name list and performs no base-vs-landed
   name/order comparison. The retention property is therefore **not machine-verified by the landed
   evidence** — I verified it by hand (this report). The landed `validation.json` is also
   **untracked** at the landed commit (`git ls-tree 1c779e4a reports/round-50/` lists `claims.json`,
   `jj-colocation-probe.py`, `run-validation.py`, `separability/`, `telemetry/` — no
   `validation.json`), so the receipt a reviewer would normally read is not part of the landed
   bytes.
4. **The landed `corrupt-head-fails-closed` message changed** (`reading HEAD failed (exit 1)` →
   `reading the symbolic HEAD failed (exit 128)`). Same diagnostic token and exit code, so the
   control is unaffected, but any external log-grep keyed to the old wording will miss it.

## Smallest fixes, if the author lane wants them

None are required for the claim to hold. Optional hardening, in priority order:

1. In `reports/round-50/run-validation.py`, capture the ordered control-name list from both trees and
   assert `landed_names[:45] == base_names` and `len(base_names) == 45` in `measure_o`, so the
   "all prior controls retained" clause becomes machine-checked instead of reviewer-checked.
2. Commit `reports/round-50/validation.json` (or generate it into a tracked path) so the receipt is
   part of the landed bytes.
3. Tighten the four `symlink-*`/`hardlink-*` controls to assert the specific message
   (`symlink receipt destination` / `receipt is not a singly-linked regular file`) so the symlink
   branch has teeth. This is a pre-existing gap and can be deferred.

## Cleanup

`/tmp/r50c-guard` (base clone) and `/tmp/r50c-head` (landed clone) plus all mutation copies under
`/tmp/r50c-*` were removed after measurement; `/tmp` free space returned to 6.8 G. No lane file was
created, modified, or deleted other than this report.
