# Round 50 falsify — README revision checker mutation probe

## Scoped result

**Item attacked:** claim O's `tools/check-readme-revisions.py` at landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, specifically whether its normal `--selftest` detects regressions in fail-closed pin handling and Git isolation. **Verdict: PARTIAL (selftest coverage).** The landed implementation met every exercised expected result; this probe did not find a landed fail-open implementation defect. Its normal selftest killed **2/6** selected mutants and **4/6 survived**. The same executable, exercised with three additional bounded fixture configurations, distinguished all six mutants from pristine/restored behavior. These are author-lane findings, not an admission/integration judgment.

Axes: operability/selftest sensitivity; valid pristine/restored controls; exact byte restoration; isolated writes. Six independent source copies were tested concurrently, never mutating the lane or another seat's source. No delegation, background jobs, alternate application runtime, network, credentials or live-process probing.

## Provenance and isolation

- Landed source was first read with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:tools/check-readme-revisions.py`, then from private shared clone `/tmp/MutateReadmeRev-W7FJ` checked out at that exact commit. `git rev-parse HEAD` printed the exact landed SHA.
- Original target SHA-256, and every pristine/restored mutation copy: `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4`. Actual `sha256sum` outputs are recorded below.
- Reproduction setup: `mktemp -d /tmp/MutateReadmeRev-XXXX`; `env GIT_CEILING_DIRECTORIES=/tmp git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin <clone>`; `env GIT_CEILING_DIRECTORIES=/tmp git -C <clone> checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`. Each case lived at `<clone>/tools/mutation-probes/M0N/check-readme-revisions.py`, with explicit `--lane` so file relocation did not change the tested object store.
- Only this report is written to the lane. All fixture repositories, Git commits, replacement ref and source mutations were under the private `/tmp` clone. No lane index/ref/jj state was changed. The checkout's original `tools/check-readme-revisions.py` remained pristine throughout.
- Existing tools: Python **3.14.8**, Git **2.56.0**. **Installs/updates: none.** Host rules were read first; no pacman transaction was performed.
- `reports/round-50/validation.json` could not be read at the landed SHA (`git show` exit 128: `fatal: path 'reports/round-50/validation.json' exists on disk, but not in '1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0'`). No working-tree receipt was substituted. This did not block the direct source/behavior probe.

## Fixed bounded detector

For **every** case, the same four commands were run on pristine, mutated and exact-restored bytes. Each invocation had a 120-second cap. There were **72 controlled invocations** (6 cases × 4 configurations × 3 phases), plus two initial pristine sanity invocations of the original path. No baseline/restored control was inconclusive.

```sh
env GIT_CEILING_DIRECTORIES=/tmp TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1 \
  python3 <clone>/tools/mutation-probes/<case>/check-readme-revisions.py \
  --selftest --lane <object-store> --base-commit <pin>
```

| Configuration | Object store / pin | Expected exit | Required interpretation |
|---|---|---:|---|

| default | `<clone>` / `c42d675be96b6b3957e6e5c00ab192080cb70083` | 0 | all existing 15 controls pass |
| missing-pin | `<clone>` / `0000000000000000000000000000000000000000` | 2 | committed-fixture ERROR propagates to process status; never SKIP/success |
| duplicate-only | `<clone>/probe-fixture` / `2a5396448e4954c9749c7f6b844f4416fdd19ebf` | 1 | reject a pinned README with DUP but no STUB |
| replace-ref | `<clone>/probe-fixture` / `5613ed4fcbdac3220af1025a1c2f87441824c394` | 0 | ignore a local replacement ref; inspect original DUP+STUB bytes |

The three additional configurations are **supplemental controls**, not claims that the normal/default selftest kills those mutants. An expected negative exit of 1 or 2 is a successful detector baseline, not a baseline failure.

### Fixture bytes and Git construction

One tiny repository at `<clone>/probe-fixture` was initialized, with three commits made using `git -C probe-fixture -c user.name=mutation-fixture -c user.email=mutation-fixture@invalid -c commit.gpgsign=false -c core.hooksPath=/dev/null commit -q -m <name>`. Only `corpus/README.md` was staged in that scratch repository.

Duplicate-only commit `2a5396448e4954c9749c7f6b844f4416fdd19ebf`:
```text
revision: 2.0 — duplicate one
body

revision: 2.0 — duplicate two
body
```
Complete-defect commit `5613ed4fcbdac3220af1025a1c2f87441824c394`:
```text
revision: 2.0 — truncated

revision: 2.0 — real
body
```
Clean replacement commit `2829acb7f9b9f341cd0c9702a453faf0bea9b20d`:
```text
revision: 2.0 — clean
body
```
`env GIT_CEILING_DIRECTORIES=/tmp git -C probe-fixture replace 5613ed4fcbdac3220af1025a1c2f87441824c394 2829acb7f9b9f341cd0c9702a453faf0bea9b20d` installed the local replacement. Direct `git show 5613ed4fcbdac3220af1025a1c2f87441824c394:corpus/README.md` printed the original four-line defect under `GIT_NO_REPLACE_OBJECTS=1`, and the clean two-line replacement when that environment key was unset. Those observed bytes establish that M06's supplemental difference was real replacement behavior, not a hypothetical mutant.

## Mutants and results

Line numbers below refer to the **landed original** `tools/check-readme-revisions.py`. Each mutant changed one behavior-bearing site; no control/assertion was removed.

| Mutant | Smallest change | Default selftest | Supplemental distinguishing control |
|---|---|---|---|

| M01: Restore SKIP in ERROR dispatch | `366–369 (changed 367)` | **SURVIVED**, exit 0 | `missing-pin`: expected 2, observed 0 |

| M02: Drop commit-type/presence cat-file gate | `274–281` | **KILLED**, exit 1 | `default`: expected 0, observed 1 |

| M03: Drop inherited GIT_* scrubbing | `240–241` | **KILLED**, exit 1 | `default`: expected 0, observed 1 |

| M04: Return success on aggregated ERROR | `512–514 (changed 513)` | **SURVIVED**, exit 0 | `missing-pin`: expected 2, observed 0 |

| M05: Accept either pinned defect instead of both | `299` | **SURVIVED**, exit 0 | `duplicate-only`: expected 1, observed 0 |

| M06: Allow replacement refs to rewrite pinned bytes | `242` | **SURVIVED**, exit 0 | `replace-ref`: expected 0, observed 1 |


**Normal selftest: 2 killed / 4 survived / 0 inconclusive.** This is a deliberately selected six-mutant sample, not a repository-wide mutation score. The four supplemental configurations together distinguish 6/6; they were not silently counted as normal selftest coverage.

### Complete exit ledger

Vector order: `[default, missing-pin, duplicate-only, replace-ref]`.

| Case | Pristine | Mutated | Restored |
|---|---|---|---|

| M01 | `[0, 2, 1, 0]` | `[0, 0, 1, 0]` | `[0, 2, 1, 0]` |

| M02 | `[0, 2, 1, 0]` | `[1, 2, 1, 1]` | `[0, 2, 1, 0]` |

| M03 | `[0, 2, 1, 0]` | `[1, 2, 1, 1]` | `[0, 2, 1, 0]` |

| M04 | `[0, 2, 1, 0]` | `[0, 0, 1, 0]` | `[0, 2, 1, 0]` |

| M05 | `[0, 2, 1, 0]` | `[0, 2, 0, 0]` | `[0, 2, 1, 0]` |

| M06 | `[0, 2, 1, 0]` | `[0, 2, 1, 1]` | `[0, 2, 1, 0]` |

### Actual decisive stdout

The following lines are verbatim selected process stdout, not predicted output. Omitted lines were unchanged PASS controls or Git continuation text; the ledger above records every exit.


#### M01 — Restore SKIP in ERROR dispatch

- Landed site: `tools/check-readme-revisions.py:366–369 (changed 367)`.
- Mutation: `error(name, detail)` → `print("SKIP " + name + " (base object unreachable)")`.
- Expected detector: default selftest should expose the regression; supplemental `missing-pin` supplies the decisive external/fixture witness where default survives.

Default mutated run:
```text
selftest: all checks passed
```

`missing-pin`, pristine, exit 2:
```text
ERROR control: base 0000000 README flagged (r49 defect) pinned BASE_COMMIT 0000000000000000000000000000000000000000 unreachable in /tmp/MutateReadmeRev-W7FJ: fatal: Not a valid object name 0000000000000000000000000000000000000000^{commit}
selftest: could not evaluate (ERROR)
```

`missing-pin`, mutated, exit 0:
```text
SKIP control: base 0000000 README flagged (r49 defect) (base object unreachable)
selftest: all checks passed
```

`missing-pin`, restored, exit 2:
```text
ERROR control: base 0000000 README flagged (r49 defect) pinned BASE_COMMIT 0000000000000000000000000000000000000000 unreachable in /tmp/MutateReadmeRev-W7FJ: fatal: Not a valid object name 0000000000000000000000000000000000000000^{commit}
selftest: could not evaluate (ERROR)
```


#### M02 — Drop commit-type/presence cat-file gate

- Landed site: `tools/check-readme-revisions.py:274–281`.
- Mutation: `cat-file -e <pin>^{commit} and its error return` → `deleted the eight-line probe/return block`.
- Expected detector: default selftest should expose the regression; supplemental `default` supplies the decisive external/fixture witness where default survives.

Default mutated run:
```text
FAIL control: unreachable base pin fails closed (never skips) git show 0000000000000000000000000000000000000000:corpus/README.md failed: fatal: path 'corpus/README.md' exists on disk, but not in '0000000000000000000000000000000000000000'
FAIL control: git-free tree fails closed (never skips) git show c42d675be96b6b3957e6e5c00ab192080cb70083:corpus/README.md failed: fatal: not a git repository (or any parent up to mount point /)
FAIL control: shallow clone with unreachable pin fails closed (never skips) git show 64f825352439c0345337d3c4e75abca8063bcf04:corpus/README.md failed: fatal: path 'corpus/README.md' exists on disk, but not in '64f825352439c0345337d3c4e75abca8063bcf04'
FAIL control: GIT_DIR override cannot mask an unreachable pin git show 3233603b6339d84c0f57fe84a5e3d9b93f5a6e73:corpus/README.md failed: fatal: not a git repository (or any parent up to mount point /)
selftest: FAILED
```

Default pristine: exit 0; `selftest: all checks passed`.

Default restored: exit 0; `selftest: all checks passed`.

Important qualification: the cat-file removal is killed because four seams require `unreachable` in the detail. `git show` still returned an ERROR for a missing pin, and that process still exited 2. This kill demonstrates diagnostic/type-gate sensitivity, **not** a demonstrated missing-pin fail-open.


#### M03 — Drop inherited GIT_* scrubbing

- Landed site: `tools/check-readme-revisions.py:240–241`.
- Mutation: `{key: value for key, value in os.environ.items() if not key.startswith("GIT_")}` → `dict(os.environ)`.
- Expected detector: default selftest should expose the regression; supplemental `default` supplies the decisive external/fixture witness where default survives.

Default mutated run:
```text
FAIL control: GIT_DIR override cannot mask an unreachable pin []
selftest: FAILED
```

Default pristine: exit 0; `selftest: all checks passed`.

Default restored: exit 0; `selftest: all checks passed`.


#### M04 — Return success on aggregated ERROR

- Landed site: `tools/check-readme-revisions.py:512–514 (changed 513)`.
- Mutation: `return 2` → `return 0`.
- Expected detector: default selftest should expose the regression; supplemental `missing-pin` supplies the decisive external/fixture witness where default survives.

Default mutated run:
```text
selftest: all checks passed
```

`missing-pin`, pristine, exit 2:
```text
ERROR control: base 0000000 README flagged (r49 defect) pinned BASE_COMMIT 0000000000000000000000000000000000000000 unreachable in /tmp/MutateReadmeRev-W7FJ: fatal: Not a valid object name 0000000000000000000000000000000000000000^{commit}
selftest: could not evaluate (ERROR)
```

`missing-pin`, mutated, exit 0:
```text
ERROR control: base 0000000 README flagged (r49 defect) pinned BASE_COMMIT 0000000000000000000000000000000000000000 unreachable in /tmp/MutateReadmeRev-W7FJ: fatal: Not a valid object name 0000000000000000000000000000000000000000^{commit}
selftest: all checks passed
```

`missing-pin`, restored, exit 2:
```text
ERROR control: base 0000000 README flagged (r49 defect) pinned BASE_COMMIT 0000000000000000000000000000000000000000 unreachable in /tmp/MutateReadmeRev-W7FJ: fatal: Not a valid object name 0000000000000000000000000000000000000000^{commit}
selftest: could not evaluate (ERROR)
```


#### M05 — Accept either pinned defect instead of both

- Landed site: `tools/check-readme-revisions.py:299`.
- Mutation: `REVISION_DUP in classes and REVISION_STUB in classes` → `REVISION_DUP in classes or REVISION_STUB in classes`.
- Expected detector: default selftest should expose the regression; supplemental `duplicate-only` supplies the decisive external/fixture witness where default survives.

Default mutated run:
```text
selftest: all checks passed
```

`duplicate-only`, pristine, exit 1:
```text
FAIL control: base 2a53964 README flagged (r49 defect) [{"class": "REVISION-DUP", "detail": "revision label '2.0' repeated", "lines": [1, 4]}]
selftest: FAILED
```

`duplicate-only`, mutated, exit 0:
```text
PASS control: base 2a53964 README flagged (r49 defect) [{"class": "REVISION-DUP", "detail": "revision label '2.0' repeated", "lines": [1, 4]}]
selftest: all checks passed
```

`duplicate-only`, restored, exit 1:
```text
FAIL control: base 2a53964 README flagged (r49 defect) [{"class": "REVISION-DUP", "detail": "revision label '2.0' repeated", "lines": [1, 4]}]
selftest: FAILED
```


#### M06 — Allow replacement refs to rewrite pinned bytes

- Landed site: `tools/check-readme-revisions.py:242`.
- Mutation: `env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")` → `env.update(GIT_OPTIONAL_LOCKS="0", LC_ALL="C")`.
- Expected detector: default selftest should expose the regression; supplemental `replace-ref` supplies the decisive external/fixture witness where default survives.

Default mutated run:
```text
selftest: all checks passed
```

`replace-ref`, pristine, exit 0:
```text
PASS control: base 5613ed4 README flagged (r49 defect) [{"class": "REVISION-DUP", "detail": "revision label '2.0' repeated", "lines": [1, 3]}, {"class": "REVISION-STUB", "detail": "revision '2.0' at line 1 has no changelog body", "lines": [1]}]
selftest: all checks passed
```

`replace-ref`, mutated, exit 1:
```text
FAIL control: base 5613ed4 README flagged (r49 defect) []
selftest: FAILED
```

`replace-ref`, restored, exit 0:
```text
PASS control: base 5613ed4 README flagged (r49 defect) [{"class": "REVISION-DUP", "detail": "revision label '2.0' repeated", "lines": [1, 3]}, {"class": "REVISION-STUB", "detail": "revision '2.0' at line 1 has no changelog body", "lines": [1]}]
selftest: all checks passed
```

## What the survivors establish / smallest author-lane repair

1. **ERROR-to-exit wiring is not protected by the default selftest.** The unreachable-pin seams at `tools/check-readme-revisions.py:462–508` directly inspect `base_readme_verdict` status/detail. They do not force the committed-fixture `record(...)` path (`438`) to receive ERROR or require its aggregated process exit. Thus M01 (`366–369`) restores SKIP+success, and M04 (`512–514`) returns 0 despite an actual ERROR line, while default selftest prints `selftest: all checks passed`. **Smallest repair:** retain a standalone process-level negative-pin control using `--selftest --base-commit 0000000000000000000000000000000000000000`, asserting exit exactly 2 and no SKIP/all-checks-passed banner. Put it in the external validation driver rather than recursively invoking selftest from itself.

2. **The pinned-base predicate lacks a one-defect negative fixture.** M05 changes the required conjunction at `299` to a disjunction and survives because the real base has both findings and the foreign fixture has neither. **Smallest repair:** add a direct `base_readme_verdict` fixture with duplicate labels but complete bodies, asserting FAIL (and optionally the symmetric stub-only fixture). The exercised duplicate-only configuration changed exit from 1 to 0 under M05.

3. **Replacement-ref isolation is implemented, but untested by the default controls.** Removing `GIT_NO_REPLACE_OBJECTS="1"` at `242` survives; control 15 only poisons `GIT_DIR`. **Smallest repair:** add the tiny local replacement-ref fixture above, asserting that the original defect remains PASS even when the local replace ref targets a clean commit. M06 changed that control's exit from 0 to 1.

No production implementation edit is justified by these surviving mutants: pristine/restored behavior satisfied the tested contract. A survivor is a coverage finding, not permission to change the contract. The separate round-50 counting probe, receipt guard and other claims were not mutation-tested by this seat; no conclusion about their protection is inferred from this selftest-only sample.

## Before / mutant / restored hashes

SHA-256 of file bytes (not Git object ids). For all six cases, before and restored equal the landed original.

| Case | Before | Mutated | Restored |
|---|---|---|---|

| M01 | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` | `8fc086132187d8d79ed88dda0460187b7ddbc20ef519783429f32cf11cb17eb3` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |

| M02 | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` | `267677e53f9d2c0939002b31743c1c409ad16287e66020a3186b5a4695f5d11f` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |

| M03 | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` | `8db3387f2e9ea1401f2770123a31a93bb1c2ba5ca2cf1a72e508256e55360ba2` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |

| M04 | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` | `349e382c924ce42935d3622d5e4f2e788c0c0c69bcbc965bab59c3b8f873b22f` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |

| M05 | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` | `0163b5ceb4212d7f05a637f862ec79f1df54c2d3b083e4eb46f60b29b00429dc` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |

| M06 | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` | `c221568aff968da9e98f7c676527ec7029624afee150ef2a33d5d0aa9fab0ecd` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |


Actual final `sha256sum` output before scratch cleanup:
```text
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/check-readme-revisions.py
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/mutation-probes/M01/check-readme-revisions.py
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/mutation-probes/M02/check-readme-revisions.py
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/mutation-probes/M03/check-readme-revisions.py
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/mutation-probes/M04/check-readme-revisions.py
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/mutation-probes/M05/check-readme-revisions.py
54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4  /tmp/MutateReadmeRev-W7FJ/tools/mutation-probes/M06/check-readme-revisions.py
```

All six exact inverse edits restored snapshot tag `5420`; all 24 restored detector exits matched their pristine expected vectors. The untouched original script also retained the same digest. Temporary sources and fixture repository were then removed with the private clone; cleanup result is recorded below.

Cleanup command, exit 0:
```sh
rm -rf -- /tmp/MutateReadmeRev-W7FJ && test ! -e /tmp/MutateReadmeRev-W7FJ && printf 'scratch_removed=/tmp/MutateReadmeRev-W7FJ\nexistence_check=absent\n'
```
Actual output:
```text
scratch_removed=/tmp/MutateReadmeRev-W7FJ
existence_check=absent
```
