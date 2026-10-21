# ReviewReadmeRev: Claim O, fail-closed pinned base in `tools/check-readme-revisions.py`

Seat `ChousaR27R2.ReviewReadmeRev-4` (leaf reviewer, round 50). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.

Lane access was read-only: `git clone` (source only), `git show`, `cat-file`, `merge-base`, `log`, `rev-parse`, `ls-files`, `test -d .jj`, and one `git status --porcelain` without `GIT_OPTIONAL_LOCKS=0` (may refresh the index stat cache; no content change). Every selftest ran in temp copies under `/tmp/rr50-O-27vj_cg9/`. Nothing in the lane was edited.

Axes: coverage (every selftest control enumerated and run), operability (fail-closed design and consumer impact), calibration (spec checked against a temp prototype; trigger attribution corrected).

Subject bytes: `tools/check-readme-revisions.py` sha256 `d49fdf1c9524c457c2a5fb9c647442e682c6a3de98030d3c778b5f33740cdeb7` (equals HEAD blob and base blob).

## 1. Findings, ranked

1. **High, operability: an unreachable pin exits 0.** `skip()` (L233-235) only prints and appends to `skips`. It never clears `ok`, so control 9 SKIP leaves `selftest: all checks passed` and `main` returns 0 (L358). Reproduced on unmodified bytes four ways (section 2): no repository (E2), shallow clone (E3), `git` missing (E5), and an ambient `GIT_DIR` pointing at a missing path (E4).
2. **The trigger is generic git state, not jj.** `c42d675` is an ancestor of HEAD (`merge-base --is-ancestor` rc 0), `cat-file -t` returns `commit` in the lane, and HEAD equals base. The lane is colocated (`.jj` exists), but jj did not remove or hide the object. Fix it anyway, but describe R3 as "generic fail-open; jj is not a trigger in this lane". [INFERENCE: durability under future jj GC is not tested.]
3. **Only control 9 depends on git history.** Controls 1-8, 10, 11 are pure. The selftest is hermetic except for the one SKIP path.
4. **Calibration hazard for Ca.** The separability dynamic leg runs acceptance argv in a git-free temp dir. There the base tool passes vacuously via SKIP, and the fixed tool exits 2. Do not list `check-readme-revisions.py --selftest` as any claim's acceptance argv.
5. **Not R3, optional:** `in_span` (L166) is assigned and never used. ruff 0.17.1 and pyflakes 4.0.3 both flag F841 on base and on the prototype. Pre-existing; leave it unless those lines change.

## 2. Evidence (every run exercised)

| run | setup | rc | control 9 | tail | transcript sha256 |
|---|---|---|---|---|---|
| E1 base | full clone at `4ad2683`, pin reachable | 0 | PASS | 11 PASS, `selftest skips: 0`, all checks passed | `2116d844ab7f03163a5f8d9df87893ee4efa3413e3a440c205bcd392c7eb1469` |
| E2 base | tool bytes alone, no repo | 0 | SKIP `(base object unreachable)` | `selftest skips: 1`, all checks passed | `ba494dab34cdfd16931eb340483ae76fd57823f3f92f0c5435f72c5af35d05e7` |
| E3 base | `git clone --depth 1 file://...`; `cat-file -e` rc 128 | 0 | SKIP | same as E2 | `345da5e9a648d2883b28d929eefc4f53e8b4415e3e29f7809b9c1dbab5dc6bb1` |
| E4 base | E1 with `GIT_DIR=/nonexistent` | 0 | SKIP | same as E2 | not hashed |
| E5 base | tool in ROOT, `env -i PATH=/nonexistent` | 0 | SKIP (OSError path) | `selftest skips: 1`, all checks passed | not hashed |
| E1 proto | full clone, prototype (section 5) | 0 | PASS | 13 PASS, all checks passed | `652454ad09c0117688d7a7e0619aea486007c2a64a9d9ed0ef099e68040fbd1b` |
| E2 proto | no repo | 2 | ERROR `(base object unreachable: c42d675...)` | 12 PASS, 1 ERROR, `selftest: could not evaluate` | `a9f23f4fa881c9820d0a365c87b1776540ed52db4f46b53ecb293c18ed80bc39` |
| E3 proto | shallow clone | 2 | ERROR | same as E2 proto | `484085b70411a59c203cdb25894d537db8ce35c933eadd4b91e9cc225a12cc30` |
| E4 proto | E1 with `GIT_DIR=/nonexistent` | 0 | PASS (ambient GIT_* scrubbed) | 13 PASS | not hashed |
| E5 proto | tool in ROOT, `env -i PATH=/nonexistent` | 2 | ERROR `(FileNotFoundError(2, 'No such file or directory'))` | `selftest: could not evaluate` | not hashed |

Transcript hashes embed the temp path (control 8 prints `FileNotFoundError ... /tmp/rr50-O-27vj_cg9/...`), so they reproduce only at that path.

## 3. Ordered control list (base 11 to proposed 13)

Base line numbers are in `tools/check-readme-revisions.py` at `4ad2683`. Proposed controls 12 and 13 are in the prototype at lines 369-371 and 373-379.

| # | control name (exact, as printed) | base line | base, pin reachable | base, pin unreachable | proto, pin unreachable |
|---|---|---|---|---|---|
| 1 | `control: clean revision list passes` | 242 | PASS | PASS | PASS |
| 2 | `control: duplicate label flagged at [1, 4]` | 249 (name 250) | PASS | PASS | PASS |
| 3 | `control: truncated stub flagged` | 258 (name 259) | PASS | PASS | PASS |
| 4 | `control: EOF stub flagged` | 266 (name 267) | PASS | PASS | PASS |
| 5 | `control: increasing order flagged` | 274 (name 275) | PASS | PASS | PASS |
| 6 | `control: fenced 'revision:' ignored` | 282 (name 283) | PASS | PASS | PASS |
| 7 | `control: absent revision lines passes` | 290 (name 291) | PASS | PASS | PASS |
| 8 | `control: missing file exits 2` | 300 | PASS | PASS | PASS |
| 9 | `control: base c42d675 README flagged (r49 defect)` | 302-321 (check 315; skip 311, 321) | PASS | **SKIP, rc 0** | **ERROR, rc 2** |
| 10 | `control: orphan paragraph warned at [4, 5], verdict clean` | 330 (name 331) | PASS | PASS | PASS |
| 11 | `control: minor gap warned` | 338 (name 339) | PASS | PASS | PASS |
| 12 (new) | `control: unreachable pinned base is ERROR` | proto 369-371 | n/a | n/a | PASS |
| 13 (new) | `control: defect verdict fails on clean text and passes on r49 defect` | proto 373-379 | n/a | n/a | PASS |

Hashes (each name followed by `\n`, UTF-8):
- 11-name base list: `6cde117546efd2e0a9ace540c076b60b5f89c869b4c8596e6362b706fdadea26`
- 13-name proposed list: `d9d74fa0d25d7f45f0bba376b6e17d59aaeb58b56ffe5c84ce5c0e7ca4b6ec31`
- base tool file: `d49fdf1c9524c457c2a5fb9c647442e682c6a3de98030d3c778b5f33740cdeb7`
- prototype tool file: `6b55578c4965d2877fc95110ee0cb41d6d5504c87b72b5c6b2a1b732e43b0d09`

Behaviour no control covers: `main` exit 1 on findings (checked by hand: the `c42d675` README gives rc 1 on base and on prototype), `--json`, the `ok: null` branch, and the `receipt()` sha256 field.

## 4. Fail-closed spec (for the author lane; advice, not an admission)

- **S1, triggers.** These must yield ERROR, never PASS, FAIL or SKIP: (a) `git -C LANE cat-file -e <pin>^{commit}` nonzero, covering absent objects and non-commits; (b) `git show <pin>:corpus/README.md` nonzero; (c) `OSError` (git missing); (d) `SubprocessError`, including the 30 s timeout; (e) README bytes not UTF-8.
- **S2, verdict tokens.** `PASS` and `FAIL` keep their meaning. `ERROR` is new and means could-not-evaluate. `SKIP` is deleted, including `skips`, `skip()`, and the `selftest skips:` line. Control 9 was the only SKIP call site.
- **S3, environment.** Drop `GIT_*` from the probe environment, as `receipt_guard.py:49-50` already does. The repository named by `-C LANE` is then the only one read. This turns the E4 SKIP into a correct PASS.
- **S4, exit map.** `selftest()` returns 2 if any ERROR, else 0 if no FAIL, else 1. ERROR outranks FAIL, because a control that could not run leaves the PASS/FAIL list incomplete. Summary lines: `selftest: all checks passed` (0), `selftest: FAILED` (1), `selftest: could not evaluate` (2). This matches the header contract (2 = could-not-evaluate) and control 8's missing-input path.
- **S5, wording.** Keep the phrase `base object unreachable` in the ERROR detail, because `claims.json` before-checks key on it. A tree object at the pin also prints this text, which is slightly imprecise. Acceptable, or use `unreachable or not a commit`.
- **S6, unchanged semantics.** When the pin resolves, control 9 is PASS iff the README at the pin has both REVISION-DUP and REVISION-STUB, else FAIL. Unit check: `4ad2683` (clean README) gives `fail`.
- **S7, new controls.** Append 12 and 13 after control 11 without renumbering. Both are hermetic: a zero sha in any repository, and a pure function over fixed text. No env var or argv seam is needed; `pinned_base_verdict(lane, sha)` is the seam.
- **S8, README gate.** The main path (no `--selftest`) never reads the pin and must stay unchanged. Its stdout hashes were identical before and after the prototype for the pin README (rc 1), the base README (rc 0), and a missing file (rc 2).
- **Rejected alternative:** unreachable pin = FAIL with exit 1. It is the smallest diff, but it merges "environment cannot evaluate" with "tool regressed" and contradicts the header's exit 2.

## 5. Prototype (temp only; not in the lane)

Path `/tmp/rr50-O-27vj_cg9/proto-src/check-readme-revisions.py`, sha256 `6b55578c4965d2877fc95110ee0cb41d6d5504c87b72b5c6b2a1b732e43b0d09`. It is non-persistent. Core of the change:

```python
def pinned_base_verdict(lane, sha):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        probe = subprocess.run(["git", "-C", lane, "cat-file", "-e", sha + "^{commit}"],
                               capture_output=True, timeout=30, env=env)
        if probe.returncode != 0:
            return "error", "(base object unreachable: %s)" % sha
        proc = subprocess.run(["git", "-C", lane, "show", sha + ":corpus/README.md"],
                              capture_output=True, timeout=30, env=env)
        if proc.returncode != 0:
            return "error", "(corpus/README.md unreadable at %s)" % sha
        text = proc.stdout.decode("utf-8")
    except (OSError, subprocess.SubprocessError, UnicodeDecodeError) as exc:
        return "error", "(%r)" % (exc,)
    return defect_verdict(text), json.dumps(evaluate_text(text)["findings"])

# control 9
verdict, detail = pinned_base_verdict(LANE, BASE_COMMIT)
if verdict == "error":
    error(name, detail)
else:
    check(name, verdict == "pass", detail)

# main
if args.selftest:
    code = selftest()  # 2 if errors else (0 if ok else 1)
    print("selftest: %s" % {0: "all checks passed", 1: "FAILED", 2: "could not evaluate"}[code])
    return code
```

Results against base, per run:
- Reachable (E1): the only byte-level change is `-selftest skips: 0` and `+` two PASS lines (controls 12, 13). The 11 base PASS lines are byte-identical.
- Unreachable (E2, E3, E5): SKIP becomes ERROR, `selftest skips` disappears, `all checks passed` becomes `could not evaluate`, and rc goes from 0 to 2.
- `GIT_DIR` (E4): no SKIP, rc 0.
- Direct calls: pin gives `pass`; base gives `fail`; zero sha, no repo, shallow, git missing, root commit (no README), tree object, and non-UTF-8 README each give `error`.
- Static: ruff and pyflakes report only the pre-existing `in_span` F841. No F821 or E9.

## 6. Operability and consumers

- The README gate does not consume the pin, so the fail-closed change affects only `--selftest`.
- `reports/round-49/run-validation.py:156` treats any nonzero selftest rc as failure. No code parses `selftest skips`. The only occurrences are recorded history in `reports/round-49/validation.json:53` and lesson prose.
- Cost, stated plainly: a shallow, partial, or no-repo checkout now gets exit 2 from `--selftest`. The remedy is full history (`git fetch --unshallow`), not re-pinning.
- For the jj probe's R3 leg: count "SKIP with rc 0 on base bytes in a pin-absent `git init` sandbox" as a false negative (reproduced by E2 and E5). Count "rc 2 with ERROR on landed bytes" as detected. The probe must not run against the lane.

## 7. Unrun checks and limits

- The executor patch (ExecReadmeRev) is not in my scope and was not reviewed. Use section 4 as its acceptance checklist: pin-absent runs must exit 2; the reachable run must show the 11 base PASS lines byte-identical plus 2 new controls; the `GIT_DIR` run must not SKIP.
- The 30 s timeout branch was not exercised.
- No run of `receipt_guard`, the jj probe (not landed), or the Ca tools.
- Did not verify the durability of the pin under jj garbage collection.

## 8. Tooling

No installs. Present and used: ruff 0.17.1 (`~/.local/bin/ruff`), pyflakes 4.0.3, uv 0.13.0, git 2.56.0, jj 0.45.1, system python3 3.14.8.
