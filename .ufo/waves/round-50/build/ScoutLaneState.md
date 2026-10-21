# ScoutLaneState — kotodama lane state & round-50 commit hazards (read-only recon)

Seat: ChousaR27R2.ScoutLaneState-4. Scope: recon only — no lane file edited, no git/jj mutation
outside disposable sandboxes under `~/.cache/`. All lane reads used `git` read-only subcommands or
`jj --ignore-working-copy`.

## 1. Lane state (observed)

```
$ scripts/hyaku/jj-lane.sh state /home/vgpnk/Projects/shokunin/kotodama-shokunin
state branch=main local=4ad26836552462d28a946ca3b067cab0b5ce3532 \
      remote=4ad26836552462d28a946ca3b067cab0b5ce3532 ahead=0 behind=0 head=attached tracked=0 untracked=2
```

- `git -C … status --porcelain` → `?? .ufo/` and `?? reports/round-50/` (2 collapsed entries).
  `--untracked-files=all` → **21 paths** at measurement (15 under `.ufo/waves/round-50`, 3 under
  `reports/round-50`, 3 clone dirs); **29** when this report was written — siblings were still
  adding `.ufo/waves/round-50/build/*.md` during the recon. The wave dir is live: every count in
  this report is a snapshot, not a steady state.
- `jj --ignore-working-copy -R … status` → `The working copy has no changes.` /
  `@ : oszxrlox 13ae1394 (empty)`, parent `@-` = `vnpnswpm 4ad26836 main`.
- `jj file list -r main | wc -l` = **3481** = `git ls-files | wc -l` = **3481**. jj's view of the
  tree is complete; the empty `@` is the only reason `jj status` looks idle.
- `.jj/` exists (colocated). `jj --version` = `jj 0.45.1-7c41cdeb…`; `git --version` = `git version 2.56.0`.
- HEAD is **attached** at `refs/heads/main` right now — this is the pre-commit steady state, not the
  post-`jj new` state the fleet audit observed (`JjAuditKotodama` R1:
  `HEAD f0e826a8…`, 1 ahead of `origin/main`). After the first `jj-lane.sh commit` of this round HEAD
  detaches.

## 2. jj configuration (observed)

`jj config list --repo` (repo-scoped, effective):

```
revset-aliases."trunk()" = "main@origin"
revset-aliases."immutable_heads()" = "builtin_immutable_heads() | remote_bookmarks()"
snapshot.auto-track = "none()"
user.name = "kotodama-shokunin"
user.email = "kotodama@shokunin.local"
```

- `jj config path --repo` → `/home/vgpnk/.config/jj/repos/e06dafe65b0d6f983438/config.toml`.
  **The repo config does not live inside the repo**; `.jj/repo/config.toml` does not exist.
- `snapshot.max-new-file-size` is not set repo-wide; the effective value is jj's **built-in default
  `1MiB`** (`jj config list --include-defaults` → `snapshot.max-new-file-size = "1MiB"`). The two
  per-repo overrides in `~/.config/jj/repos/*` (4MiB, 3MiB) are other repos, not this lane.
- `immutable_heads() = … | remote_bookmarks()` means `main@origin` is immutable: divergence surface
  is local-only.

## 3. Largest tracked files (>900 KB)

| bytes | path |
|---|---|
| 1,037,171 | `reports/round-23/wording/evidence/tie-break-check-receipt.json` (**>1 MiB**) |
| 1,005,257 | `reports/round-20/validation.json` (**>1 MiB**) |

Next largest is 693,791 (`reports/round-14/validation.json`); `LOG.md` 257,149. Both >1 MiB files are
already tracked and already visible to jj — the size cap applies to **new** paths only (§5 H1/H6).

## 4. `.gitignore` coverage of `.ufo/waves`

```
1  .ufo/state/
2  .ufo/watchdog.log
3  *.log
4  __pycache__/
5  /reports/supplement-opencode-1/scratch/
6  .scratch/
```

- `.ufo/waves` — **NOT ignored** (`git check-ignore -q -- .ufo/waves/round-50` → rc 1).
- `.ufo/waves/round-50/build/ScoutLaneState.md` — **NOT ignored** (this report's own path).
- `.ufo/watchdog.log` — ignored. `.ufo/state/anything` — ignored (line 1, dir-only pattern; the
  literal path `.ufo/state` does not exist yet so a no-slash probe reports NOT_IGNORED — an artifact
  of the probe, not a gap).
- `.ufo/waves/round-50/work/ExecGuard/.git` — NOT ignored: git never "ignores" a nested repo, it
  records a gitlink. jj skips it (§5 H2).
- No `.ufo` file has **ever** been tracked: `git ls-files .ufo | wc -l` = **0**.

Footprint: `.ufo` = 268 MB (`du -sb` 256,505,377 B); three private clones
`work/ExecGuard` 105M, `work/ExecProbe-4` 82M, `work/ExecReadmeRev` 82M, each with a nested `.git`
and a 17,860,094-byte pack. Non-clone wave content: **15 files, 708,149 B** (largest
`build-task-result.json` 361,431). Round-50 evidence proper: `reports/round-50` = 3 files, 13,990 B.

## 5. Hazards for committing round-50 evidence

Severity is mine; every mechanism below was reproduced or read in code this session. Sandboxes:
`~/.cache/scout-lane-state-sandbox{,2,3}` (disposable, plain git + `jj git init --colocate`).

**H0 — critical — a bare `jj` run from a private clone mutates the LANE.**
`work/<NAME>` clones live *inside* the lane tree, so jj discovery walks up and finds the lane's `.jj`:

```
$ cd .ufo/waves/round-50/work/ExecGuard
$ jj --ignore-working-copy root   → /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ git rev-parse --show-toplevel   → …/kotodama-shokunin/.ufo/waves/round-50/work/ExecGuard
```

Sandbox reproduction: `jj status` run inside `CloneA` printed the lane's own `@`
(`A ../note.md`, same `@` change id as the lane) — it operated on the lane working copy, not the
clone. Any mutating jj verb there (`new`, `commit`, `describe`, `abandon`) violates the lane's
"helper is the only writer" rule and can strand or sweep lane work. Mitigation: inside a clone use
only `git -C <clone>`; never `jj` with cwd inside the lane tree.

**H1 — high — a new file >1 MiB is dropped silently by a directory-name commit.**
`jj file track` on a directory drops oversize new files, **exits 0**, and stages whatever else is
eligible; when the oversize file is the only new content, the commit prints `nothing to commit` and
exits 0 having landed nothing (`scout-lane-state-sandbox3`, sole 2 MiB file):

```
$ jj file track -- 'root:"d"'   → track_rc=0
  stderr: Warning: Refused to snapshot some files: d/big.bin: 2.0MiB … maximum size allowed is 1.0MiB
$ jj diff --summary             → (empty)   staged_count=0
```

The helper redirects that stderr to `$LOCKBASE.err` and prints it **only on nonzero exit**
(`jj-lane.sh:658-663`), so a directory request whose only content is oversize prints
`nothing to commit` and **exits 0 having landed nothing**. Named *files* are safe: they are tracked
with `--include-ignored`, which admits oversize new files (verified: 1.5 MiB file → rc 0,
`A wave/big.json`); the helper's post-commit "refused to track" warning also covers named files only
(`jj-lane.sh:719-725`), never directories. The 10 MiB `--allow-large` gate applies to named files
(`jj-lane.sh:638-640`).

**H2 — high — `.ufo/waves` passes the commit path guard.**
`repo_path_allowed` (`jj-lane.sh:506-517`) refuses only `.git*`, `.ufo` exactly, `.ufo/state*`, and
`.ufo/watchdog.log`. `.ufo/waves/round-50` is therefore committable, and a directory request would
land the 15 build JSON/MD files (708 KB) permanently in lane history. jj skips the three nested
clones today (sandbox: tracking a dir containing `CloneA/.git` added only `note.md`; `git status`
still shows `?? …/CloneA/`), but *git* would record them as gitlinks — and nothing in the lane's
history has ever tracked `.ufo`. This is a policy decision for L1, not a default to take.

**H3 — medium — `auto-track = none()` makes new evidence invisible to every jj read.**
`jj status` says "no changes" and `jj diff` is empty while git shows 21 untracked paths. Any check
phrased as "did round-50 land?" against `jj diff`/`jj status` answers *no* until `file track` runs.
The helper handles this for named paths; nothing else does.

**H4 — low — `state`'s `untracked=2` is directory-collapsed.** It counts `??` lines, not files
(2 vs 21 with `--untracked-files=all`). Do not cite it as a file count in the round report.

**H5 — medium — the lane's jj guarantees travel with the *path*, not the bytes.**
`auto-track=none()` and the lane identity live in
`~/.config/jj/repos/e06dafe65b0d6f983438/config.toml`. A copy of the repo at another path (restore,
scratch clone used as a jj repo) silently gets jj's default `all()` snapshot. The helper is
fail-closed here: it refuses to commit unless `config list --repo` shows `none()`
(`jj-lane.sh:624-627`). This is why sandbox jj repos reproduce "everything snapshots" behaviour.

**H6 — info — two tracked files already exceed 1 MiB** (§3). They stay safe because the cap is on
new paths; but a round-50 `validation.json` (round-20's was 1,005,257 B, round-23's 1,037,171 B) that
crosses 1 MiB must be named as an individual file, never swept via `reports/round-50`.

## 6. Recommended commit shape for round-50

Name every path individually; do not name `reports/round-50` as a directory this round (its
`validation.json` is the one artifact historically near the 1 MiB line) and never name
`.ufo/waves/round-50`:

```
scripts/hyaku/jj-lane.sh commit /home/vgpnk/Projects/shokunin/kotodama-shokunin --as kotodama \
  -m "round-50: …" -- <each corpus/tools/report file by path>
```

Then verify with `scripts/hyaku/jj-lane.sh state …` (`ahead=`, `local=`), never `@{u}` /
`git rev-parse HEAD` (detached after the first helper commit), and never `git add`/`commit`.

This report's own path (`.ufo/waves/round-50/build/ScoutLaneState.md`) is untracked by design: no
`.ufo` path has ever been tracked in this lane. If L1 needs it citable post-merge, copy it into
`reports/round-50/` in the same commit as the claim evidence.

## 7. Unrun checks

- Did not run `jj-lane.sh commit` (mutating) — helper behaviour above is read from
  `jj-lane.sh:598-726` plus jj probes in disposable sandboxes.
- Did not run any lane gate/selftest (out of scope for this seat).
- Did not exercise `receipt_guard.py` / `check-readme-revisions.py` (O seat's ground).
- Did not probe nested-repo handling of a *named file* under a clone; irrelevant to this round's
  paths.

## 8. Tooling

No installs, no upgrades. Used the host's `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`,
`git 2.56.0`, `python3 3.14.8` (sandbox file generation only). No pacman transaction attempted.
