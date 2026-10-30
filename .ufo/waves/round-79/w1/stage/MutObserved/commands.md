# MutObserved — reproduction commands

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base `44f76d456c1b326a71ffdb381590af825cbf11be`).
Driver: `stage/MutObserved/mut_observed.py` (sha256 `1395e7d0fc8a8070c9965e6c48d06b18a3b6a95c2969b3acc94d3a005c880243`).
Tools used: Python 3.14.8, git 2.56.0 (both pre-existing on host; no installs made).

## Run the probe (creates an isolated fixture repo under a fresh scratch dir)

```sh
W=/fast/scratch/hyaku/kotodama-r79/MutObserved/work-<n>   # must NOT exist
O=/fast/scratch/hyaku/kotodama-r79/MutObserved/out-<n>
S=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-79/w1/stage/MutObserved
python3 -B "$S/mut_observed.py" --work "$W" --out "$O"; echo "RC=$?"
```

The driver:
1. `git init -b main` in `$W/fixture-repo`, then asserts `git rev-parse --show-toplevel` equals that path before any commit.
2. Commits B1 (keys.txt: 3 key lines + note; other.txt: 2 key lines; status.txt: `PASS legs=12/12`) and B2 (keys.txt: 13 key lines + note); then appends one uncommitted key line (worktree only).
3. Derives truth from `git show <rev>:<path>` bytes in python (never from the guard's observer), and self-checks the hand-written expectations against that truth.
4. Runs the pristine guard, 13 mutants and 2 controls over 22 cases; writes `results.json` and `run.txt` to `$O`; exit 0 only if pristine clean, every mutant killed, both controls behave, self-check true.

## Clean up own scratch after copying receipts

```sh
rm -rf "$W"   # receipts are in $O; the stage copy is in $S/receipts
```

## Determinism check (run twice, compare matrices)

```sh
python3 -B "$S/mut_observed.py" --work "$W2" --out "$O2"
diff <(sed 's#work-[^/]*#WORK#g' "$O/run.txt") <(sed 's#work-[^/]*#WORK#g' "$O2/run.txt")
```

Observed: identical matrix and identical raw observation bytes across two independent runs (see report).

## Committed-bytes references cited in the report (read-only)

```sh
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 44f76d456c1b326a71ffdb381590af825cbf11be:reports/round-76/accept-ca.py | sed -n '1317,1340p;1644,1670p'
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 44f76d456c1b326a71ffdb381590af825cbf11be:reports/round-76/accept-ca.py | sed -n '1586,1590p'
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 44f76d456c1b326a71ffdb381590af825cbf11be:.ufo/waves/round-73/w1/drafts/ledger-draft.json | sed -n '8p' | cut -c1-400
```
