# ExecProbe: round 50, claim O counting probe (refinement 2)

Seat: `ChousaR27R2.ExecProbe-4` (leaf executor, critic refinement from ChousaR27R2). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin` was read only. Base `4ad26836552462d28a946ca3b067cab0b5ce3532`.

- Clone: `.ufo/waves/round-50/work/ExecProbe-4` (base checkout, probe added as intent-to-add).
- Patch: `.ufo/waves/round-50/patches/ExecProbe-4.patch` (382 lines, new file mode 100755). `git apply --check` passes on a fresh clone at base.
- Probe: `reports/round-50/jj-colocation-probe.py`.

## Result on base bytes

Tools: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive 4ad2683 tools | tar -x -C /tmp/kotodama-r50-jj-probe-base`

Command (the lane is passed as the history repository, which holds the pin):

```
python3 reports/round-50/jj-colocation-probe.py --tools-root /tmp/kotodama-r50-jj-probe-base --history-repo /home/vgpnk/Projects/shokunin/kotodama-shokunin
```

Output, verbatim, exit 0:

```
{"case": "R1", "detail": "guard presents committed_sha=a9bb765e0a3a7441749e7d0ba9d44ff466e231ee as landed, but it is not an ancestor of refs/remotes/origin/main; the local-only HEAD is a9bb765e0a3a7441749e7d0ba9d44ff466e231ee", "evidence": "receipt_guard: refusing overwrite path=reports/validation.json committed_sha=a9bb765e0a3a7441749e7d0ba9d44ff466e231ee committed_blob=c9ddb682421f394edb113f3358a1f022b7fd6bee; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]", "exit": 3, "flagged": true, "kind": "defect", "local_head": "a9bb765e0a3a7441749e7d0ba9d44ff466e231ee", "name": "cited-sha-not-landed", "presented": ["committed_sha=a9bb765e0a3a7441749e7d0ba9d44ff466e231ee"]}
{"case": "R2", "detail": "guard exits 0 and allows the overwrite: the receipt is committed on main and origin/main while HEAD is detached at 098eb20f4312e4c8c12eee6223537cbc94633098", "evidence": "", "exit": 0, "flagged": true, "head": "098eb20f4312e4c8c12eee6223537cbc94633098", "kind": "defect", "name": "overwrite-allowed"}
{"case": "R3", "detail": "selftest exits 0 with pinned BASE_COMMIT c42d675be96b6b3957e6e5c00ab192080cb70083 absent from the repository", "evidence": "SKIP control: base c42d675 README flagged (r49 defect) (base object unreachable)", "exit": 0, "flagged": true, "kind": "defect", "name": "skip-pass", "pinned_base": "c42d675be96b6b3957e6e5c00ab192080cb70083"}
{"case": "P1", "detail": "guard allows the normal state: HEAD == origin/main, receipt absent", "evidence": "", "exit": 0, "flagged": false, "kind": "positive", "name": "normal-state-allowed"}
{"case": "P2", "detail": "guard allows a new untracked receipt that no commit holds", "evidence": "", "exit": 0, "flagged": false, "kind": "positive", "name": "new-untracked-receipt-allowed"}
{"case": "P3", "detail": "selftest exits 0 and PASSes the control for pinned c42d675", "evidence": "PASS control: clean revision list passes [] PASS control: duplicate label flagged at [1, 4] [{\"class\": \"REVISION-DUP\", \"detail\": \"revision label '2.0' repeated\", \"lines\": [1, 4]}] PASS control: truncated stub flagged [{\"class\": \"REVISION-DU", "exit": 0, "flagged": false, "kind": "positive", "name": "pinned-readme-selftest-passes", "pinned_base": "c42d675be96b6b3957e6e5c00ab192080cb70083"}
{"case": "P4", "detail": "guard honours REFRESH_RECEIPTS=1 for a committed receipt", "evidence": "receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=reports/validation.json committed_sha=f50e16aed8ff794c66454ef09470a61fe31f5842 committed_blob=1b15da2baad549988a43ff461e37306c1319a6ee [RECEIPT-GUARD-REFRESH]", "exit": 0, "flagged": false, "kind": "positive", "name": "refresh-permit-allowed"}
JJ_COLOCATION_FALSE_NEGATIVES=3/3
JJ_COLOCATION_FALSE_POSITIVES=0/4
```

Commit SHAs differ between runs: the probe no longer pins commit dates, so only the identity and the fixture shape are deterministic.

## What the refinement changes

- Sandboxes: each run uses `tempfile.mkdtemp` in `/tmp` (the same primitive as `mktemp -d`), never under the lane. Host `GIT_*` variables are dropped, and `GIT_CEILING_DIRECTORIES=/tmp` stops discovery at the sandbox. `HOME` and `XDG_CONFIG_HOME` point into the sandbox. Each run removes its sandbox (0 leftovers after all runs).
- R1 is judged by ancestry. Every sha the guard presents as committed or landed must be an ancestor-or-equal of `refs/remotes/origin/main`. A label containing `committed` or `landed` presents a sha. Labels containing `blob` or `tree` are ignored. A label containing `head` or `local` with no committed or landed term is the local HEAD and is not presented. Unlabelled tokens count only when they name a commit object. The fake fix that prints `landed_sha=<HEAD>` is a defect (see the matrix).
- R3 has two legs. R3 (defect): a repository without the pin; the selftest must be nonzero. P3 (positive): `git clone --shared --no-checkout` of the history repository, so the pin is present through alternates; the selftest must exit 0 and print the PASS control for the pin.
- Positive states count false positives. P1 normal state (HEAD == origin/main, receipt absent). P2 new untracked receipt. P3 above. P4 receipt committed with `REFRESH_RECEIPTS=1`, the documented permit. The denominator is k=4.
- Every case is a state with an expected outcome. An always-refusing guard therefore scores false positives. There is no setup-error control that would hide an always-allowing guard.
- The history repository defaults to the git work tree containing `--tools-root`. For `/tmp` trees the operator passes `--history-repo`. Without it, the probe exits 2.

## Validation matrix (throwaway stand-in tools at `/tmp/kotodama-r50-probe-standin`, not lane tools)

Each stand-in mode is selected by an environment variable (`STANDIN_GUARD`, `STANDIN_GATE`). Every row is an actual probe run with `--history-repo` set to the lane.

| guard | gate | R1 | R2 | R3 | P1 | P2 | P3 | P4 | FN | FP | exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base bytes (real) | base bytes | FLAG | FLAG | FLAG | ok | ok | ok | ok | 3/3 | 0/4 | 0 |
| fixed (consults origin/main, honours REFRESH) | fixed (fails closed without pin) | ok | ok | ok | ok | ok | ok | ok | 0/3 | 0/4 | 0 |
| landed-head (fake: prints `landed_sha=<HEAD>`) | fixed | FLAG | FLAG | ok | ok | ok | ok | ok | 2/3 | 0/4 | 0 |
| refuse (always refuses) | fixed | ok | ok | ok | FLAG | FLAG | ok | FLAG | 0/3 | 3/4 | 0 |
| allow (always allows) | fixed | ok | FLAG | ok | ok | ok | ok | ok | 1/3 | 0/4 | 0 |
| fixed | fail (always fails) | ok | ok | ok | ok | ok | FLAG | ok | 0/3 | 1/4 | 0 |
| fixed | pass (exit 0 without pin) | ok | ok | FLAG | ok | ok | ok | ok | 1/3 | 0/4 | 0 |
| base bytes, no `--history-repo` | — | — | — | — | — | — | — | — | setup error | — | 2 |

Setup-error output for the last row: `jj-colocation-probe: setup error: the tools root is not inside a git work tree; pass --history-repo DIR`.

The base row is the verbatim run above. The stand-in rows show that the probe reports zero for a correct tool, counts the critic's fake fix as an R1 defect through ancestry, counts an always-refusing guard as positive false positives, and counts an always-failing gate as a P3 false positive.

## Base evidence (exact lines, base bytes unchanged)

- `tools/harness/receipt_guard.py:68-69`: `_head_commit` resolves `HEAD^{commit}` only. R1 cites that HEAD as `committed_sha`.
- `tools/harness/receipt_guard.py:129`: `ls-tree -z --full-tree <head> -- <path>` is a HEAD-only receipt probe. This is the R2 mechanism.
- `tools/check-readme-revisions.py:67`: `BASE_COMMIT = "c42d675…"`.
- `tools/check-readme-revisions.py:311`: `skip(name, "(base object unreachable)")`. Nothing downstream clears `ok`, so the exit stays 0. This is the R3 mechanism.

## Blind spots

1. A sha presented under a label with `head` or `local` and no committed or landed term is treated as the local HEAD and is not checked. A fix that presents a non-landed sha under such a label would pass.
2. Unlabelled commit shas count as presented. A fixed guard that prints an unlabelled local HEAD in prose would be flagged as an R1 defect. The current base and stand-in outputs do not do this.
3. R1 and R2 test one anchoring depth (HEAD one commit off the tip).
4. P3 needs a 40-hex `BASE_COMMIT = "..."` at line start in the gate, and the pin must exist in the history repository. Otherwise the probe exits 2. That is loud, not silent.
5. P4 encodes the documented REFRESH permit. If the O fix removes that permit, P4 flags, which is intended.
6. jj is never invoked. The fixtures model jj's anchored HEAD with git plumbing and are not compared with a live jj-colocated repository in this seat.
7. The probe runs the gate's `--selftest` in both R3 legs. It does not run the guard's `--selftest`.

## Installs and updates

None. Used git 2.56.0 and Python 3.14.8 as present. No pacman, uv, npm or cargo activity.

## Lane and writes

The lane was only read: `git cat-file`, `git merge-base --is-ancestor`, and `git clone --shared --no-checkout` (alternates into a sandbox clone, which is removed afterwards). Writes: the clone, the patch, this report, and the `/tmp` stand-in tree.

## Checks for the main agent (not run by me)

1. Run the probe against the landed O tools with `--history-repo /home/vgpnk/Projects/shokunin/kotodama-shokunin`. Expect `JJ_COLOCATION_FALSE_NEGATIVES=0/3` and `JJ_COLOCATION_FALSE_POSITIVES=0/4`, exit 0.
2. Run `python3 tools/harness/receipt_guard.py --selftest` and `python3 tools/check-readme-revisions.py --selftest` on the landed tree. Both should exit 0.
