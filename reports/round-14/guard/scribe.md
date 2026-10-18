# R14-D08 — filed-rounds exposure erratum and capability-row draft

Seat: R14-D08, D / depth scribe. Round declaration date: 2026-10-17.
Reference checkout: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`.
Writes: the new `FRR-14-EXPOSURE` ledger entry and this artifact only; no
SCORECARD, LOG, guard implementation, runner, historical receipt, commit or push.
The capability row below is a draft, not an admission or promotion assertion.

Axes: depth (receipt-preservation boundary), operability (safe rechecks),
calibration (restoration is not prevention; proposed behavior is not proof).

## 1. Filed-rounds exposure erratum

`reports/round-12/defects/ledger.json`, entry `FRR-14-EXPOSURE`, supplements
`FRR-10`, `FRR-12a`, and `FRR-12b` without changing those entries. Its
`resolved-by-documentation` status closes this exposure-documentation task only;
`legacy_exposure` explicitly remains `retained-by-design`.

The restoration controls repaired the recorded overwrite incidents, not the
legacy writers. The preserved runners still unconditionally write their own
`validation.json`:

- `reports/round-8/run-validation.py:1485-1487`;
- `reports/round-9/run-validation.py:1909-1911`;
- `reports/round-10/run-validation.py:1053-1056`;
- `reports/round-11/run-validation.py:1738-1742`.

The causal distinction is independently documented at
`reports/round-11/adjacency.md:39-67`: a stable command-output measurement does
not prove preservation of the filed tree. The admitted round-8 state is not
invalidated by a later overwrite (`reports/round-12/defects/sweep-r8.md:13-25`).
The round-14 successor requirement is in `reports/round-14/claims.json:18-23`;
its historical-exposure route is `reports/round-12/defects/routed.md:10-16`.

Control: do not run filed validators in the live lane. Prefer read-only
source/commit comparisons. If execution is necessary, use a disposable,
independent full-tree copy below `.scratch`, confine every writer's destination
to that copy, and compare original filed-path hashes before and after. Avoid
hardlinks to filed files. Guarding a new parent's receipt does not guard an old
child's output. `REFRESH_RECEIPTS=1` is an explicit exception for authorized,
guard-enabled writers, not a protection for unguarded legacy runners and not
permission to alter rounds 8-12.

## 2. Successor contract and scope

Design authority: `reports/round-14/guard/design.md:53-155` and its limits at
`:196-212`. The intended committed predicate is exact-path membership in the
current HEAD commit tree, not the mutable index or worktree existence.
Uncommitted receipts may be re-generated; a committed receipt requires the exact
environment value `REFRESH_RECEIPTS=1`, otherwise the runner must exit 3 before
writing. Git/path failures must fail closed. The CLI is a preflight probe, not a
writer; a permitted probe is not itself a refreshed receipt.

The first implementation read, SHA-256
`d7199bd6f87c3ddec18407d6117c43cdd1bb092bfacd752219a9b41e5ef39c83`, exposes
`guard_receipt(path, repo_root=...)`, `ReceiptGuardError`, and
`round_runner_main(callback, path, repo_root=...)`. The wrapper emits the named
diagnostic and returns 3 before calling the callback on refusal. A caller using
the lower-level function must propagate its exception; merely importing the
module or ignoring a separate probe does not protect a writer. Integration
must be checked against the version actually filed.

## 3. Read-only append/preservation control

Run from the lane root; no historical validator is imported or executed:

```sh
export TMPDIR="$PWD/.scratch"
python3 -B -c 'import pathlib; p=pathlib.Path("reports/round-14/guard/scribe.md"); exec(compile(p.read_text().split("```python\n",1)[1].split("\n```",1)[0], str(p), "exec"))'
```

```python
import ast
import datetime
import hashlib
import json
import pathlib
import subprocess

revision = "a7bc9e9ff05a57515c5efaaa7e50116eb30938ff"
ledger_path = pathlib.Path("reports/round-12/defects/ledger.json")
original = subprocess.check_output(["git", "show", f"{revision}:{ledger_path}"])
current = ledger_path.read_bytes()
old = json.loads(original)
new = json.loads(current)
boundary = original.rindex(b"\n ]\n}")
assert current.startswith(original[:boundary] + b",")
assert current.endswith(original[boundary:])
assert {k: v for k, v in old.items() if k != "entries"} == {
    k: v for k, v in new.items() if k != "entries"
}
assert new["entries"][:len(old["entries"])] == old["entries"]
ids = [entry["id"] for entry in new["entries"]]
assert len(ids) == len(set(ids))
assert ids.count("FRR-14-EXPOSURE") == 1
legacy = []
for number in (8, 9, 10, 11):
    runner = pathlib.Path(f"reports/round-{number}/run-validation.py")
    receipt = pathlib.Path(f"reports/round-{number}/validation.json")
    source = runner.read_text()
    ast.parse(source)
    assert "receipt_guard" not in source
    assert "output.write_text(json.dumps(receipt" in source
    for path in (runner, receipt):
        assert path.read_bytes() == subprocess.check_output(
            ["git", "show", f"{revision}:{path}"]
        ), str(path)
    legacy.append({
        "round": number,
        "runner_sha256": hashlib.sha256(runner.read_bytes()).hexdigest(),
        "receipt_sha256": hashlib.sha256(receipt.read_bytes()).hexdigest(),
    })
for admission, number in (("e1694ba", 8), ("9dc18ec", 9)):
    assert subprocess.run([
        "git", "diff", "--quiet", admission, "--",
        f"reports/round-{number}/validation.json"
    ]).returncode == 0
print(json.dumps({
    "observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "reference_revision": revision,
    "original_ledger_entries_preserved": len(old["entries"]),
    "original_ledger_entry_bytes_preserved": True,
    "added_entry_ids": ids[len(old["entries"]):],
    "legacy_runner_count": len(legacy),
    "unchanged_runner_and_receipt_paths": 2 * len(legacy),
    "legacy_runners_with_receipt_guard_reference": 0,
    "legacy_paths": legacy,
}, indent=2))
```

Initial read-only AST/JSON/Git inspection at `2026-10-17T23:58:02Z` found
15 original ledger entries, 4 unguarded legacy runners, and 8 runner/receipt
paths byte-identical to the reference checkout. The command above additionally
checks the append itself and prints its own measurement date. The separate
admission controls ran at `2026-10-17T23:58:02Z`:

```sh
git diff --quiet e1694ba -- reports/round-8/validation.json
git diff --quiet 9dc18ec -- reports/round-9/validation.json
```

Both exited 0. No restoration or historical re-generation was performed.

## 4. Capability-row draft — conditional, parent integrates

Landing format: `SCORECARD.md:43-44`, columns
`name | demonstrated behavior | command / evidence | first working`.
Do not paste this row as demonstrated until the admission conditions in §6 pass.
It deliberately makes no retroactive protection claim for filed runners.

```markdown
| receipt-guard | Cooperative preflight for guard-enabled round runners: a receipt present at its exact path in HEAD is refused before runner side effects with exit 3 and a named diagnostic unless the operator explicitly sets REFRESH_RECEIPTS=1; an uncommitted receipt remains re-runnable. Git/path errors fail closed. Historical rounds 8-11 remain unguarded and are rechecked only in independent disposable copies; this is not a sandbox or race-proof lock | `python3 tools/harness/receipt_guard.py --selftest`; `python3 reports/round-14/run-validation.py`; dated implementation/runner controls and the append-only `FRR-14-EXPOSURE` entry; `reports/round-14/guard/scribe.md` §§3,5-6 | round 14 — proposed; only after integrated controls and parent admission |
```

## 5. Runtime observations — retain red attempts

At `2026-10-18T00:00:20Z`, with `TMPDIR=$PWD/.scratch` and
`PYTHONDONTWRITEBYTECODE=1`:

- `python3 -B tools/harness/receipt_guard.py --selftest` exited **1**:
  **19/20** controls passed, `selftest_passed=false`. The sole failure was
  `git-error-fails-closed`: expected exit 3, observed exit 0 with no stderr.
  The selftest's `not-repo` fixture sits inside this lane, so Git discovers the
  enclosing repository; the implementation did not require an explicit
  `repo_root` to equal Git's reported root. Source remained byte-identical
  during the run (SHA-256 in §2). This is an implementation/control finding,
  not authority for this scribe to edit those seats' files.
- Direct guard CLI probes, **not historical runner invocations**:
  `env -u REFRESH_RECEIPTS python3 -B tools/harness/receipt_guard.py --repo-root . reports/round-8/validation.json`
  and the same command for `reports/round-9/validation.json` both exited **3**,
  named `RECEIPT-GUARD-COMMITTED`, and left receipt bytes unchanged.
  SHA-256 values were respectively
  `359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba`
  and `036f84278c4817901413d97839ceba78aa8a367f91579de7505c92800611e418`.

These probes show what an explicit guard call does; they do not retrofit the
historical runners. No override was set against a live historical target.

## 6. Integration conditions and open handoff

- The initial implementation failure and design/runtime differences recorded in
  §5 were resolved at the later measured implementation in §7. Retain the red
  attempt; do not report every implementation snapshot as green.
- The later source uses direct `SystemExit(3)`, full committed commit/blob
  identities, an explicit-refresh warning, explicit-root agreement, and a
  two-phase callback/publisher helper. Final integration must still propagate
  refusal and guard the actual writer, not merely import the helper.
- Runner owner: demonstrate the real round-14 guard before side effects, no
  unguarded historical writer invoked on the live tree, and normal pre-filing
  operation with isolated committed-target controls. The source inspection and
  in-memory selftest in §7 do not replace actual production-runner controls.
- Parent: bind final guard/runner digests, independent controls, and integrated
  regression evidence to the row before admission. `guard/neg-04.md` and
  `guard/neg-05.md` initially bind guard SHA-256
  `82eec760c45a81bb12a71423ba3137797a5a84f5c70d7f400c02b236dfd60c5e`, not the
  later implementation tested here. Re-run or explicitly reconcile controls
  after source churn; do not transfer a green verdict silently between digests.
- `python3 reports/round-14/run-validation.py` is the declared integrated counting
  command. This scribe ran its non-writing `--selftest`, not the receipt-writing
  acceptance command or the whole regression suite; those remain integration
  seats' responsibility.
- Bookkeeping remains parent-owned: integrate this evidence in append-only LOG
  and SCORECARD records. This scribe does not mark a capability admitted, a round
  accepted, or a promotion checklist verified.

Dependency polls used the prescribed 60-second cadence (maximum 20 minutes).
The design appeared at `2026-10-17T23:59:18Z`; the guard implementation was read
at `2026-10-17T23:59:58Z`. The later measurements below supplement, not erase,
the initial red attempt.

## 7. Follow-up controls and handoff state

At `2026-10-18T00:01:27Z`, the exact §3 command exited **0**, preserving the
original **15** ledger entries and their byte prefix, with only
`FRR-14-EXPOSURE` added. It confirmed **4** still-unguarded historical runners
and **8** runner/receipt paths unchanged from the reference checkout; the
round-8/9 admission-byte controls also remained green. The ledger entry stores
this executable command and measurement date. Original entries and all other
historical runner/receipt bytes were not rewritten.

At `2026-10-18T00:02:28Z`, after the next 60-second dependency poll:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 -B tools/harness/receipt_guard.py --selftest
```

Exit **0**, **45/45** controls passed, `selftest_passed=true`, no failed controls.
Guard SHA-256 was
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` and remained
unchanged during execution. This supersedes the §5 implementation failure for
this measured revision, not for an arbitrary future revision.

At `2026-10-18T00:03:08Z`:

```sh
python3 -B reports/round-14/run-validation.py --selftest
```

Exit **0**, **25/25** in-memory validator controls passed. Runner SHA-256 was
`e0b1133083702220cdf5e4a507ee6cab0200d63d2debe55d7f50b02052c689cf`, unchanged
during the run. A read-only `ast.parse`/`ast.walk` inspection of those same
bytes found the `guard_preflight` calls at lines 655 and 663, before validation
and before receipt publication. This source/control observation does not claim
a full acceptance run or prove the callbacks cannot make arbitrary writes.

At the same `2026-10-18T00:03:08Z` stamp, both direct guard CLI probes from §5
were repeated against the same live historical receipt targets, without an
override. Each exited **3** and preserved the receipt bytes. The newer diagnostic
included the exact pathname, `committed_sha=a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`,
and the appropriate blob identity (`ca49c2e81c0215abd334bfa4073f907be7fe579e` for
round 8; `303d26872c27f3f393b602a8446b6c90a4a97d98` for round 9).
Diagnostic fields are from captured child stderr and are implemented at
`tools/harness/receipt_guard.py:142-149`; the guard source remained at the green
SHA-256 above during both probes. Neither historical validator was executed.

Result: **PASS for this scribe's append-only exposure record and reproducible
preservation controls**. The capability row remains proposed until the parent
binds the final independent controls, real runner behavior, integrated regression
results, and admission decision. No commit or push was made.
