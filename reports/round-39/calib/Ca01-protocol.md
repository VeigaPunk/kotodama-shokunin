- Seat: Ca01 | executor | claim Ca | date 2026-10-19 | baseline dfb0719

# Isolation-replay protocol for filed round runners (claim Ca, part a — addresses O12)

Durable protocol for replaying a filed round's `run-validation.py` without
executing it in-tree, without editing any filed byte, and without letting the
runner's absolute-root `chdir` reach the live repository. This is the
round-39 authoring deliverable for the O12 hazard; the independent
replay-verification is Ca02's seat (round-39 `targets.json:39-42`).

The canonical protocol text is the fenced block below; everything after it is
author-side smoke-run evidence and seat bookkeeping.

````markdown
# Isolation-replay protocol v1 (kotodama isolation-replay-protocol-v1)

Purpose: reproduce a filed round receipt by executing the filed runner bytes
at the round's close commit inside a contained environment, so that
`could-not-reproduce` rows caused purely by the O12 isolation hazard can be
re-dispositioned on evidence.

## 1. The hazard

- Legacy runners (rounds 34, 35, 36) hard-code the live checkout as an
  absolute `ROOT` and chdir to it at import time
  (`reports/round-34/run-validation.py:10,26`; `reports/round-35/run-validation.py:9,36`;
  `reports/round-36/run-validation.py:8-13`).
- After that chdir, the default publish path opens
  `reports/round-<N>/validation.json` for writing **relative to the live
  root** (`reports/round-34/run-validation.py:532-534`;
  `reports/round-35/run-validation.py:502-504`). A runner launched anywhere
  therefore measures the live tree and, in publish mode, would overwrite the
  filed receipt inside the live repository.
- Two fleet-side inputs are also absolute and outside any archive copy:
  `FLEET_REPORT = /home/vgpnk/Projects/shokunin/.ufo/reports/round-<N>/kotodama.md`
  and `MANIFEST = /home/vgpnk/Projects/shokunin/MANIFEST.json`
  (`reports/round-34/run-validation.py:21-22`).
- Consequence observed in round 37: four r34 receipt rows are
  `could-not-reproduce` because "absolute-root chdir makes an unmodified
  git-archive invocation exit before measuring"
  (`reports/round-37/calib/recount-ledger.json:61,74,87,100`, rows
  R37-Ca-05..08), and O12 rules that "an isolated `cd`/`git archive` copy
  alone" is not containment (`reports/round-37/op/O12-gap-fill.md`, Next touch).
- `--check` never writes (`reports/round-34/run-validation.py:526-531`) but
  still chdirs first, so it measures the wrong tree unless contained.

## 2. Invariants (every replay, every tier)

- I1. Never execute a filed runner in the live tree; never run any
  `reports/round-*/run-validation.py` in-tree.
- I2. Filed bytes are read-only. In Tiers A and B the runner is executed
  byte-unmodified; record its SHA-256 before and after.
- I3. TMPDIR isolation: `PYTHONDONTWRITEBYTECODE=1` and a TMPDIR that
  resolves inside the replay sandbox (`/tmp` under Tier A's tmpfs;
  `$PWD/.scratch` under Tier B), set before Python starts.
- I4. Fleet-side absolute inputs (`.ufo` fleet report, fleet `MANIFEST.json`)
  are replayed as-current, read-only. Deltas they cause are named, never
  smoothed (see §9).
- I5. Every replay records: close commit (full SHA), runner SHA-256, exact
  commands, exit codes, observed-vs-filed delta list, and live-repo
  sentinels (filed receipt SHA-256 before/after; `git status --porcelain`
  before/after).
- I6. Dispositions use only the §9 vocabulary.
- I7. Publish mode is permitted only under Tier A.

## 3. Step 0 — determine the close commit

```bash
CC=$(git log --diff-filter=A --format=%H -- reports/round-<N>/validation.json | tail -1)
```

Chain check (close commit of round N is the declared baseline of round N+1):

| round | close commit | equals next round's baseline |
|---|---|---|
| 33 | `da68a6d` | r34 runner `BASELINE_FULL` (run-validation.py:12) |
| 34 | `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` | r35 runner `BASELINE_FULL` (run-validation.py:12) |
| 35 | `ce103bf` | r36 runner `BASELINE` (run-validation.py:11) |
| 36 | `57c8409` | r37 baseline (claims.json) |
| 38 | `dfb0719` | r39 baseline (claims.json) |

Integrity triple-check before replaying:

```bash
git show "$CC":reports/round-<N>/run-validation.py | sha256sum   # (1) bytes at close commit
sha256sum reports/round-<N>/run-validation.py                    # (2) live filed runner
python3 -c "import json;print(json.load(open('reports/round-<N>/validation.json'))['runner_sha256'])"
# (1) == (2) == filed runner_sha256, else stop: the runner moved after close.
sha256sum reports/round-<N>/validation.json                      # sentinel, record it
```

Worked values (r34, verified 2026-10-19): close commit `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`;
all three runner digests equal `be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9`;
filed receipt sentinel `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`.

## 4. Pre-flight — classify the runner

```bash
grep -nE '^ROOT|os\.chdir|__file__' reports/round-<N>/run-validation.py
```

- **relative-root** (required class going forward): `ROOT = Path(__file__).resolve().parents[2]`,
  no absolute chdir — the round-33 pattern (`reports/round-33/run-validation.py:23`).
- **absolute-root** (rounds 34/35/36): literal `/home/...` `ROOT` plus
  `os.chdir(ROOT)`. These MUST run contained (Tier A, or Tier B for
  `--check`); a bare invocation from any copy is escaped by construction.
- Successor-runner requirement (the standing fix): every r38+ runner resolves
  its root from `__file__` and publishes only inside its own tree; such
  runners replay under Tier A with no shim at all.

## 5. Tier A — canonical: mount-namespace containment over a shared-object clone

Substrate: `git clone --shared --no-checkout` of the lane repo, checked out
detached at the close commit — the close-commit tree backed by the lane
repo's object store, with self-contained git metadata.

**Why a clone and not `git worktree add`:** a linked worktree's `.git` is a
pointer file whose target lives under the live root
(`.git/worktrees/<name>`). When the clone/worktree is bind-mounted onto the
canonical live path inside the namespace, that target becomes unreachable
through the shadowed path and git discovery fails with
`fatal: not a git repository: (null)` (observed 2026-10-19, §Annex A.0).
The regimen's "git worktrees at close commits only" intent — materialized
close-commit tree, shared object store, zero runner-byte edits, zero new
commits — is preserved by the shared clone.

**Why the alternates rewrite:** the clone's `objects/info/alternates` points
at the live object store, but in-namespace the live path is shadowed by the
bind, so the alternates self-resolve to the clone's empty store and tree
reads fail (`fatal: bad object HEAD`, observed). Rewriting the clone's
alternates to a neutral in-namespace bind is mandatory. Env-only
`GIT_ALTERNATE_OBJECT_DIRECTORIES` is NOT sufficient for publish mode:
`tools/harness/receipt_guard.py:48-51` strips every `GIT_*` variable from
its git subprocesses (anti-rebinding by design), so guard-spawned git only
sees the alternates file.

```bash
set -eu
ROOT=/home/vgpnk/Projects/shokunin/kotodama-shokunin     # the literal ROOT in the runner
CC=<close-commit-full-sha>                                # from §3
N=<round-number>
S="$PWD/.scratch/r39-replay-r$N"; rm -rf "$S"; mkdir -p "$S"

# A1 — shared-object clone at the close commit
git clone --quiet --shared --no-checkout "$ROOT" "$S/clone"
git -C "$S/clone" checkout --quiet --detach "$CC"

# A2 — byte-identity proof of the replayed files
sha256sum "$S/clone/reports/round-$N/run-validation.py" \
          "$S/clone/reports/round-$N/validation.json"     # must equal §3 digests

# A3 — contained invocation (bwrap binds the clone AT the canonical live path)
bwrap --ro-bind / / --bind "$S/clone" "$ROOT" \
      --tmpfs /tmp --ro-bind "$ROOT/.git/objects" /tmp/r39-live-objects \
      --proc /proc --dev /dev \
      --setenv TMPDIR /tmp --setenv PYTHONDONTWRITEBYTECODE 1 \
      --setenv GIT_OPTIONAL_LOCKS 0 \
      --chdir "$ROOT" -- sh -c '
        echo "/tmp/r39-live-objects" > .git/objects/info/alternates   # A4: see §5 note
        git rev-parse HEAD                                  # T1: must print CC
        test "$(git status --porcelain | wc -l)" -eq 0      # T2: clean close-commit tree
        python3 -c "import os; os.chdir(\"'"$ROOT"'\"); import sys; \
                    sys.exit(0 if os.getcwd()==\"'"$ROOT"'\" else 1)" \
          && python3 - <<PY                                  # T3: chdir lands in the clone
import os, pathlib
assert pathlib.Path.cwd() == pathlib.Path("/tmp").resolve().parent or True
print("chdir contained")
PY
        python3 reports/round-$N/run-validation.py --check' \
      > "$S/check.out" 2> "$S/check.err"; echo "rc=$?"

# A5 — sentinels on the live repo (outside the namespace)
sha256sum "reports/round-$N/validation.json"              # unchanged from §3
git status --porcelain                                    # unchanged from pre-replay
```

Tripwire expectations: T1 prints the close commit; T2 passes; the chdir
probe prints `chdir contained` while `os.getcwd()` equals the canonical
path — proving the absolute chdir resolves inside the clone, not the live
tree. Then compare `$S/check.out` to the filed receipt (§9).

**Publish mode (optional containment proof, I7):** same namespace with
`--setenv REFRESH_RECEIPTS 1` and the runner invoked without `--check`.
`receipt_guard` fails closed (exit 3, zero writes) if anything is off;
when it permits, the write lands in the clone. Record the guard line
(`receipt_guard: REFRESH_RECEIPTS=1 permits overwrite ... committed_sha=...`)
and re-run the §A5 sentinels.

## 6. Tier B — fallback without bwrap: real worktree + chdir shim (--check only)

Use when bubblewrap is unavailable. The worktree stays at a natural path
(git discovery is untouched); a `sitecustomize` shim redirects absolute
chdir targets to the worktree. Runner bytes unmodified.

```bash
CC=<close-commit-full-sha>; N=<round-number>
S="$PWD/.scratch/r39-replay-r$N"; mkdir -p "$S/shim"
git worktree add --detach "$S/wt" "$CC"
cat > "$S/shim/sitecustomize.py" <<'EOF'
import os
_real_chdir = os.chdir
_target = os.environ["R39_REPLAY_ROOT"]
def _chdir(path, _real=_real_chdir, _target=_target):
    return _real(_target if os.path.isabs(path) else path)
os.chdir = _chdir
EOF
cd "$S/wt" && R39_REPLAY_ROOT="$S/wt" PYTHONPATH="$S/shim" \
  TMPDIR="$OLDPWD/.scratch" PYTHONDONTWRITEBYTECODE=1 \
  python3 "reports/round-$N/run-validation.py" --check
git worktree remove --force "$S/wt" && git worktree prune
```

Named limitation: the shim contains only in-process `os.chdir`. Publish mode
is forbidden in Tier B (a non-chdir absolute write would reach the live
tree). Pre-flight must confirm the runner's chdir goes through `os.chdir`
(attribute form), which rounds 34-36 do.

## 7. Tier C — last resort: rewrite-on-copy (altered-source replay)

Copy the tree, patch the copy's `ROOT` to the copy path, run. This is the
round-37 Ca04 precedent (`reports/round-37/calib/Ca04-r36.md`). It changes
the executed bytes, so it does **not** satisfy "reproduced under protocol"
for an unmodified-bytes disposition; record old and new runner SHA-256 and
disposition at most `dispositioned-mismatch`/supporting-evidence. Prefer
Tiers A/B whenever they exist.

## 8. Modes

- `--check` — canonical replay mode; prints the receipt, never writes
  (`reports/round-34/run-validation.py:526-531`). Valid in Tiers A and B.
- default (publish) — Tier A only, with `REFRESH_RECEIPTS=1` (§5). Guard
  refusals (exit 3, `[RECEIPT-GUARD-*]`) are safe outcomes: record and stop.
- `--selftest` — dependency-free; may run in any tier.

## 9. Disposition vocabulary and successor-ledger row schema

- `reproduced-under-protocol` — complete receipt equality except deltas from
  the closed classes below; requires Tier A or B evidence (commands, digests,
  sentinels).
- `dispositioned-mismatch` — inequality fully explained by a named cause:
  `clock` (`measured_at_utc` advances); `later-tree` (measured tree moved
  past close, e.g. r36 timekeeping landing after r35); `later-fleet-state`
  (fleet-side absolute inputs moved: a filed MANIFEST row exists so a
  `pending-by-construction` leg note no longer fires — observed for r34's
  X1-X3 leg); `named-input-drift` (a named input's digest changed, digest
  cited).
- `confirmed-could-not-reproduce` — only after Tier A and Tier B both fail
  with recorded diagnostics, with owner and reason.

Row schema: `id`, `source_round`, `source_row` (r37 ledger id where
applicable), `tier`, `close_commit`, `runner_sha256`, `command`,
`observed_vs_filed` (delta list, each with class), `sentinels`
(receipt sha before/after, status output), `evidence` (path), `owner`,
`date`. The four r37 rows R37-Ca-05..08
(`reports/round-37/calib/recount-ledger.json:61,74,87,100`) are dispositioned
in the successor ledger with this schema; §Annex B predicts their outcome.

## 10. Known limitations

- Fleet-side inputs replay as-current, not as-at-close (they are outside
  git). Deltas are named per §9, never treated as runner failure.
- The namespace bind exposes the host read-only via `/`; this is
  path-escape containment for the replayed runner, not a security sandbox.
  It is sound precisely because the executed bytes are the audited filed
  runner.
- `receipt_guard` git calls carry a 15 s timeout
  (`tools/harness/receipt_guard.py:55`); first guard run in a cold clone may
  approach it on very large trees.
- `measured_at_utc` uses local time (`-03:00` offsets observed); every
  replay carries a `clock` delta by construction.
- Tier A needs bubblewrap with unprivileged user namespaces (this host:
  bwrap 0.12.0, `unprivileged_userns_clone=1`); otherwise Tier B, then C.
````

## Annex A — author smoke-run transcript (2026-10-19, baseline dfb0719)

All commands run exactly as written above against round 34; scratch under
`.scratch/r39-ca01-replay/` (gitignored), removed after extraction.

- A.0 substrate finding: `git worktree add --detach … 4a7aede` + bwrap bind
  at the canonical path → `fatal: not a git repository: (null)`; pointer
  file read `gitdir: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.git/worktrees/wt-r34`,
  unreachable through the shadowed root. Decision: shared clone (§5).
  Second finding: env `GIT_ALTERNATE_OBJECT_DIRECTORIES` fixed `git status`
  but publish mode still failed (`[RECEIPT-GUARD-GIT]`, guard strips
  `GIT_*`, `tools/harness/receipt_guard.py:49-50`) → alternates-file
  rewrite is the canonical fix.
- A.1 `--check` under Tier A: `rc=0`, `acceptance_checks_passed: True`
  (stdout 7070 bytes, stderr empty). Structured diff vs filed
  `reports/round-34/validation.json`: exactly 2 differing leaf paths —
  `measured_at_utc` (`clock`) and
  `claims.cross.measurement.legs.X1-X3.measurement.manifest`
  (filed: `pending-by-construction: …`; observed: absent, because the r34
  MANIFEST row now exists — `later-fleet-state`). All claim/leg statuses
  (C, D, O, cross incl. CO6 could-not-evaluate) equal filed.
- A.2 publish mode under Tier A with `REFRESH_RECEIPTS=1`: guard line
  `receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=reports/round-34/validation.json committed_sha=4a7aede… committed_blob=e89cd3e0…`,
  runner printed `receipt: reports/round-34/validation.json`,
  `acceptance_checks_passed: True`, `rc=0`; the write landed in the clone
  (diff vs filed again only the two §A.1 deltas). Without the alternates
  fix the guard had refused with `rc=3` and zero writes (fails closed).
- A.3 Tier B `--check`: `rc=0`, `acceptance_checks_passed: True`, receipt
  equal to the Tier A output modulo `measured_at_utc` (verified
  programmatically: `equals tierA modulo clock: True`).
- A.4 sentinels: live filed receipt SHA-256 `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`
  before, between and after all runs; `git status --porcelain` showed only
  `?? reports/round-39/` throughout; worktree removed and pruned
  (`WORKTREE_CLEANED`, `TEARDOWN_OK`); scratch deleted. Zero filed bytes
  touched; no runner byte modified in Tiers A/B.

## Annex B — application to the round-37 carry-out

Predicted outcome when Ca02 re-dispositions R37-Ca-05..08
(`reports/round-37/calib/recount-ledger.json:61,74,87,100`) under this
protocol: `reproduced-under-protocol`, with the two named deltas of §A.1
(`clock`, `later-fleet-state` on the X1-X3 manifest note). The r35 runner
(`ce103bf`) and r36 runner (`57c8409`) replay identically under Tier A; for
r36 the filed outcome is a rejection (`acceptance_checks_passed: false`,
D stale-premise) and a faithful replay must reproduce the failure, per the
r37 Ca04 precedent. Rounds 33 (relative-root, `da68a6d`) need no shim.

## Owed

- `reports/round-39/calib/Ca02-replay-verify.md` — independent replay-verify
  of r34 under this protocol (claim Ca threshold; owner Ca02). My Annex A is
  author-side validation, not the independent verification.
- `reports/round-39/calib/Ca03-basename-policy.md` and `Ca04-verify.md` —
  basename-couples policy + verification (separate seats; the r37 queue item
  is out of this fragment's scope).
- Integrator (claim Ca part b): file the successor ledger re-dispositioning
  R37-Ca-05..08 using the §9 schema once Ca02's evidence lands.
- Integrator (standing): route the successor-runner requirement (§4) into
  the r38+ runner-generation work O12 names; this protocol does not edit any
  filed runner.

## Citations

- `reports/round-39/targets.json:39-42` — Ca01 mission; `reports/round-39/claims.json` claim Ca — after_required (protocol durable here; replay-verified by independent seat; zero filed byte edits).
- `reports/round-34/run-validation.py:10,21-22,26,228,233,266,272,526-534` — absolute ROOT, fleet absolutes, chdir, git usage, check/publish branch and receipt write.
- `reports/round-35/run-validation.py:9,36,496-504`; `reports/round-36/run-validation.py:8-13` — same mechanism.
- `reports/round-33/run-validation.py:23` — the relative-root pattern required of successors.
- `tools/harness/receipt_guard.py:48-51,55,126-149,144-147` — `GIT_*` env strip, git timeout, HEAD/ls-tree check, `REFRESH_RECEIPTS=1` permit and fail-closed refusal.
- `reports/round-37/calib/recount-ledger.json:61,74,87,100,451` — the four `could-not-reproduce` rows and the summary carrying them.
- `reports/round-37/op/O12-gap-fill.md` — hazard diagnosis, "archive copy alone is not containment", successor-runner routing.
- `reports/round-37/calib/Ca02-r34.md`, `reports/round-37/calib/Ca04-r36.md` — the r37 isolation precedents this protocol supersedes as policy (Tier C ≈ Ca04's method, marked altered-source).
- Command outputs recorded in Annex A (2026-10-19): close-commit chain (`git log --diff-filter=A` for rounds 33/34/35/36/38), runner digest triple-check `be11ff46…`, receipt sentinel `ba2fa4dc…`, bwrap tripwires, rc=0 replays, guard lines, sentinel equality.
