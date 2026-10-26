# SentinelLanded — round 74 wave 2 (safety and scope of the landed bytes)

Seat: SentinelLanded (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`, operative freeze F3
`00c408a0af2fa5ddf65af2224152ce258b26d896`, claim Ca lands
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`, claim C lands
`c4bf61a8d722f9168ce0fd8021a6261c000610c5`, lane `main` at dispatch
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236`.
Landed diff attacked: `git diff f7104cbce186bc2e1522abf0cfd619cc834628bb main`.
`main` moved under this pass, so both surfaces are measured:

* **dispatched lands** `1d7add3` (= the two claims' landings' successor):
  151 paths (141 A, 10 M), +40157 / −248 lines;
* **current `main`** `92b8d4bb` (orchestrator in-flight snapshot, committed
  23:17:06 with the message "hyaku run 7 interrupted: in-flight snapshot committed
  by the orchestrator (not a landing)"): 683 paths (673 A, 10 M),
  +119891 / −248 lines, i.e. the snapshot adds **532 paths / 16.0 MB / 79 734
  lines** that no claim was graded on — see F8.

**Verdict: the claim survives on credentials, privacy, tracking, reachability and
the 1 MiB bound. It does not survive cleanly on scope: the Ca counter's fleet
probe writes the fleet root's git index (and the legs that certify fleet silence
cannot see the write they make), and `main` stopped being the lands mid-pass when
the orchestrator committed 532 worktree-scratch paths.**

| # | severity | one line |
|---|---|---|
| F1 | HIGH | `accept-ca.py` APPENDONLY probe `git status` on `--fleet-root` rewrites that repo's `.git/index`; reproduced end-to-end on a fleet replica: PASS 11/11 **and** index changed |
| F2 | MEDIUM | "this lane writes no byte under the fleet root" is probed only for the one report path; a stray write anywhere else in the fleet root leaves the leg green (demonstrated) |
| F3 | LOW | the same probe's exit code is ignored: a failing `git status` reads as "clean" (demonstrated, exit 128) |
| F4 | LOW | the fleet `git` calls and the census subprocess inherit the caller's environment; `GIT_INDEX_FILE` retargets the write (demonstrated) |
| F5 | LOW | 12 absolute `/home/vgpnk/...` symlinks and 4 registry copies with a planted `S883` row, landed by F8's snapshot under `assimilation/guard-proof/mirror-*` |
| F6 | LOW | a secret-shaped positive-control token (`ghp_` + 36 chars) is committed in `.ufo/waves/round-74/w1/SentinelScope.md:62` |
| F7 | LOW | `corpus/README.md` was landed by copying an uncommitted `/tmp` file (`apply-landing.py:38`); bytes match today, landing not re-derivable from the repo |
| F8 | MEDIUM | `main` moved from `1d7add3` to `92b8d4bb` ("in-flight snapshot committed by the orchestrator (not a landing)") and now carries 532 un-landed paths / 16.0 MB of worktree scratch (a 483-file corpus copy, 4 mirror registries, 31 w2 seat files) |

Attacks that **FAILED** (claim survived) are listed in §4 with their evidence.

---

## 1. Method, environment, tooling

* **No tool installed or upgraded.** `git 2.56.0`, `python3`, `curl`, `grep`,
  `sha256sum` sufficed. `pacman` not invoked (host-wide pause, orchestrator
  2026-10-20). No network tool installed; all fetches were `curl` from the host.
* **Counters were run only inside my own clone**, per the mandate:

```
$ D=$(mktemp -d); git -C "$D" init -q; git -C "$D" rev-parse --show-toplevel
/tmp/tmp.UWEaaIHuEA
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
$ git -C "$D/lane" checkout -q --detach
$ git -C "$D/lane" branch -f main <lands>          # inside the clone only
```

* **`/tmp` is full host-wide** (`/dev/nvme1n1p1 128G 128G 0 100% /tmp`, 51–172 MB
  free at different moments; other seats' `/tmp/r74-*` clones are still resident).
  The counter's own `tempfile.mkdtemp` therefore honours `TMPDIR`; I set
  `TMPDIR=/var/tmp/SentinelLanded` (`/dev/mapper/root`, 566 GB free) for every
  counter run. Nothing was written under the fleet root by me.
* **Fleet-side reads only**: `git log/show/ls-tree/ls-files --debug`
  (`--no-optional-locks`), `ls`, `stat`, and a `git clone` of the fleet into
  `/var/tmp/SentinelLanded/fleetwt` used as a **replica** so that no fleet
  mutation was needed to exercise the Ca legs.
* **`main` moved under the pass** (`1d7add3` → `92b8d4bb` at 23:17:06, F8). Every
  counter run therefore names an explicit `--lands` commit and pins the clone's
  `main` to it; nothing was graded against the moving branch name.
* **Fetch hygiene**: every fetch below used, verbatim,

  `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

  and was repeated with curl's default UA to test for UA-gating. No wall was
  bypassed by automation; no wall was found.

---

## 2. Findings

### F1 — HIGH — the Ca counter writes the fleet root's git index

**What is attacked.** Ca's APPENDONLY leg claims, as its own evidence sentence:

> … and this lane writes no byte under the fleet root …
> (`reports/round-74/claims.json` Ca.legs[APPENDONLY], frozen at `00c408a0`)

and the counter implements the fleet half of it at
`reports/round-74/accept-ca.py:1449` (identical blob
`.ufo/waves/round-74/counters/accept-ca.py`):

```
1449:            dirty = git(fleet_root, "status", "--porcelain", "--", report)
```

`git()` (line 206) is `subprocess.run(["git", "-C", str(root), *args])` with the
inherited environment — no `--no-optional-locks`, no `GIT_OPTIONAL_LOCKS=0`.

**Why that is a write.** `git status` refreshes the index entry of every
pathspec member whose cached stat data is stale and rewrites `.git/index`.
Minimal reproduction (fresh 2-file repo, content unchanged, mtime only):

```
$ touch -d '2020-03-03' b.txt;       h1=$(sha256sum .git/index); git status --porcelain -- a.txt; h2=…
stale file OUTSIDE pathspec: dd5a84efad63… -> dd5a84efad63… UNCHANGED
$ touch -d '2020-04-04' a.txt;       h3=$(sha256sum .git/index); git status --porcelain -- a.txt; h4=…
stale file INSIDE pathspec:  dd5a84efad63… -> 132f0685224e… CHANGED
```

So the write fires exactly when the probed report has been touched since the
fleet index was last written — the ordinary state of a live lane report.

**End-to-end on a fleet replica, with the unmodified counter** (replica:
`git clone` of the fleet at `/var/tmp/SentinelLanded/fleetwt`, `dad39efd` present,
`.ufo/reports/round-73/kotodama.md` present):

```
$ git clone -q /home/vgpnk/Projects/shokunin /var/tmp/SentinelLanded/fleetwt   # replica; read-only on the source
$ sha256sum /var/tmp/SentinelLanded/fleetwt/.git/index
6be7ca8aa3904e9a0462ad194c711dbf5d2fcc159e9fdb5e4d890df706030089    # fresh after clone
$ python3 -B reports/round-74/accept-ca.py --root . \
    --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 \
    --fleet-root /var/tmp/SentinelLanded/fleetwt
ACCEPT-CA-74: PASS legs=11/11
$ sha256sum .../fleetwt/.git/index
6be7ca8aa3904e9a0462ad194c711dbf5d2fcc159e9fdb5e4d890df706030089    # unchanged

$ touch .../fleetwt/.ufo/reports/round-73/kotodama.md     # mtime only, content identical
$ sha256sum .../fleetwt/.git/index
6be7ca8aa3904e9a0462ad194c711dbf5d2fcc159e9fdb5e4d890df706030089
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0… \
    --freeze 00c408a0… --fleet-root /var/tmp/SentinelLanded/fleetwt
ACCEPT-CA-74: PASS legs=11/11
$ sha256sum .../fleetwt/.git/index
b8fd921659c332d18d6520fb97abf4ee82bd4d266d83af7e81452fd30d5d506e    # WRITTEN
```

The leg that certifies "no byte under the fleet root" changed a byte under the
fleet root and still printed PASS. Isolated in-process reproduction of that one
leg (`leg_appendonly` imported from the clone, sandbox fleet):
index `c370024380d0161174405cecc1d04d7c…` → `725cd5f41825eb10555b20b2d429c72c…`,
same PASS-shaped detail.

**Why this is HIGH, not cosmetic.** It does not flip a leg — all 11 pass at the
claim's lands — so the kill_rule's "any leg false" limb is not triggered; what is
false is the APPENDONLY leg's own evidence sentence, and the documented command
breaks the seat rule that forbids writing the fleet at all.

1. It contradicts a sentence the claim certifies, in a repo the seat mandate
   forbids writing at all ("do not write `/home/vgpnk/Projects/shokunin/**`").
   The **documented counter command** therefore cannot be run by a compliant
   seat without violating its own no-mutation rule — the command is
   self-contradictory.
2. The round itself ran it against the real fleet root twice —
   `reports/round-74/telemetry/controls-ca.txt:3,56` carry
   `--fleet-root /home/vgpnk/Projects/shokunin` — and
   `.ufo/waves/round-74/counters/junk-fixtures.py:644` defaults
   `fleet_root=FLEET_ROOT`. The real fleet is a git repo
   (`/home/vgpnk/Projects/shokunin/.git`, 572 KB index, 4781 tracked paths), and
   its index is rewritten by fleet activity constantly
   (`index mtime 2026-10-25 23:02:16 → 23:05:29 → 23:15:29` during this pass).
3. Optional index locks in a shared repo race with concurrent fleet commits: an
   `index.lock` held by this probe can fail a fleet operation (and vice versa).
   The fleet already carries one same-day shared-history accident
   (`35b91714`, author `t <t@t>`, 4606 files deleted, repaired at 09:29) — that
   one pre-dates this round and is **not** attributed to it, but it shows
   shared-tree accidents on this host are a live failure mode, not a hypothesis.
4. The check is self-referential: the act the sentence rules out is the act that
   performs the check, so a counter cannot certify it.

**Smallest remediation** (two lines, proven):

```
git(fleet_root, "--no-optional-locks", "status", "--porcelain", "--", report)
# or:  env = dict(os.environ, GIT_OPTIONAL_LOCKS="0"); subprocess.run(..., env=env)
```

Proof in the same replica and the same leg: under `GIT_OPTIONAL_LOCKS=0` the
index stays byte-identical (`725cd5f41825eb10555b20b2d429c72c…` before and
after), while the default-env run of that leg changes it
(`c370024380d0161174405cecc1d04d7c…` → `725cd5f41825eb10555b20b2d429c72c…`); in
the 2-file reproduction above both `GIT_OPTIONAL_LOCKS=0` and
`--no-optional-locks` leave the index untouched, the default run gives
`dd5a84efad63…` → `132f0685224e…`. Also narrow the claim sentence
to what is actually proven (see F2) or widen the probe (see F2's fix).

### F2 — MEDIUM — the fleet-silence sentence is checked only at the report path

**Attack.** The claim asserts *no byte* under the fleet root; the probe is
pathspec-limited, so it can only ever see the one file it names. Demonstration
(sandbox fleet, the leg's exact command):

```
$ echo stray > /tmp/SentinelLanded/fakefleet/stray-lane-write.txt
$ git --no-optional-locks -C /tmp/SentinelLanded/fakefleet status --porcelain -- .ufo/reports/round-73/kotodama.md
                                   # (empty: the leg sees nothing)
$ git --no-optional-locks -C /tmp/SentinelLanded/fakefleet status --porcelain | head -3
?? stray-lane-write.txt
```

A lane that wrote, say, a draft or a stray capture anywhere else under the fleet
root would keep APPENDONLY green. The leg's other fleet probes
(`show`, `rev-parse`, `diff --numstat pin HEAD`) are equally path-scoped
(`accept-ca.py:1436-1449`).

**Impact.** The claim's negative is broader than its evidence. At lands nothing
of the sort exists — `.ufo/reports/round-74/` holds only the two round-74
`game-dev-*` files from 2026-10-14, and the pinned round-73 report is
byte-identical at pin and at fleet HEAD (`000bab3a36648498b67b78ea3d7db3f2e8dd17a3ad762aa528d95ef169132bdd`
at both, blob `d104dfa4342078ca258bb0399a1ae241e2e1d684`, worktree clean) — so
this is a vacuity in the leg, not a false statement about the bytes.

**Fix.** Either state the narrower fact ("no byte in the pinned report path
changed"), or run one whole-repo probe and require every line to match an
allowlist:

```
git --no-optional-locks -C "$fleet" status --porcelain   # must be empty
```

(that also subsumes F1's trigger: with `--no-optional-locks` it writes nothing).

### F3 — LOW — a failing fleet probe reads as clean

`dirty = git(...)` is followed only by `if dirty.stdout.strip():`
(`accept-ca.py:1450`); the return code is never inspected. With the probe forced
to fail, the leg reports no fleet problem at all:

```
$ GIT_WORK_TREE=/tmp/SentinelLanded/nonexistent-worktree git -C fakefleet status --porcelain -- .ufo/reports/round-73/kotodama.md
fatal: this operation must be run in a work tree
status exit=128
# the same leg, run in-process with that env:
fleet-related problems: []          # blobs still resolved, status error swallowed
```

So an unreadable worktree, a broken `GIT_*` env, a permission error or a missing
`.git` all convert "cannot tell" into "clean".

**Fix.** Treat a non-zero exit (or stderr) as a problem:
`if dirty.returncode != 0: problems.append("fleet status probe failed: %s" % …)`.

### F4 — LOW — environment passthrough retargets the counter's one write

The fleet calls use the inherited environment, while the round's own round-73
re-run path already shows the sanitized-env pattern
(`accept-ca.py:1726-1740`: explicit `env` with `GIT_CONFIG_NOSYSTEM`,
`GIT_NO_REPLACE_OBJECTS`, `GIT_TERMINAL_PROMPT=0`). Demonstrated influence of the
ambient env on F1's write:

```
$ cp fakefleet/.git/index altidx
$ GIT_INDEX_FILE=/tmp/SentinelLanded/altidx git -C fakefleet status --porcelain -- .ufo/reports/round-73/kotodama.md
$ sha256sum altidx fakefleet/.git/index
0009dcd5a80d23359a487c2ab222f8c261946773d3a3cc7f6d6b0db84311f165  altidx        # written
725cd5f41825eb10555b20b2d429c72c064fe0632299281150c21744fa2fa820  fakefleet/.git/index
```

`GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` are all caller-controlled; F3's
reproduction already shows `GIT_WORK_TREE` breaking the probe outright, and the
run above shows `GIT_INDEX_FILE` moving the write. No live exploit: nothing in
the lane exports these. **Fix.** Reuse the sanitized env dict for every
`git -C <fleet>` call and pass it to the census `subprocess.run`
(`accept-c.py:1458`), so the probe's write target and result cannot come from
the caller's shell.

### F5 — LOW — absolute symlinks and planted registry copies in the snapshot's mirrors

The 12 symlinks below are **not** in the dispatched lands:

```
$ git cat-file -e 1d7add3:….ufo/waves/round-74/assimilation/guard-proof/mirror-2sp/corpus/SOURCES.md
fatal: path '.ufo/waves/round-74/assimilation/guard-proof/mirror-2sp/corpus/SOURCES.md' exists on disk, but not in '1d7add3f7b9eaf6f3349c56c36f6d06325d74236'
exit=128
```

They are worktree debris that F8's snapshot commit landed. In current `main`
their blobs are absolute host paths:

```
$ git cat-file -p main:.ufo/waves/round-74/assimilation/guard-proof/mirror-2sp/corpus/knowledge
/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge
$ … mirror-2sp/SKILL.md -> /home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md
```

and four whole-registry copies with a **planted `S883` row**
(`…/guard-proof/mirror-{control,2sp,3sp,4sp}/corpus/SOURCES.md`, 957543–958927 B,
`grep -n example.invalid` → row at line 836 in `mirror-2sp`).

* Hazard: any tool that follows those links and writes through
  `mirror-*/corpus/knowledge` edits the live `corpus/knowledge`; on any other
  machine the fixtures dangle; the repo records the operator's absolute path.
* The planted rows are false positives for any whole-tree `^ {0,3}\| S883` scan
  (the claim's COLLCHECK reads `corpus/SOURCES.md` only, so its numbers are
  unaffected).
* Not introduced here: round 67 and round 73 committed the same absolute-symlink
  shape (`…/round-73/assimilation/guard-proof/mirror{,-a3}/corpus/knowledge`), so
  this round adds 12 more of an inherited pattern rather than a new one.

**Fix.** Build mirrors in `mktemp -d` and commit only the `out/` receipts (the
`proof.txt`/`out/*` files already carry the numbers), or use repo-relative
symlinks (`../../../../../corpus/knowledge`) plus a `.gitignore`d mirror root.

### F6 — LOW — a secret-shaped positive control is committed

`.ufo/waves/round-74/w1/SentinelScope.md:62` (landed in this diff):

```
1:ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
```

36 characters after `ghp_` — precisely the GitHub personal-access-token shape;
the same file also embeds `op://vault/item` and `?utm_source=news`. These are
declared pre-scan controls, not credentials (I verified no live credential
exists — §4.1), but they will trip secret scanners, push protection, and future
seats' credential greps, and they train false positives.

**Fix.** Use a control string that cannot be mistaken for a token
(`ghp_<REDACTED-CONTROL-36CH>`, or break the charset) and keep the file's
statement that a positive control was planted.

### F7 — LOW — `corpus/README.md`'s landing source is an uncommitted `/tmp` file

`apply-landing.py:38` lands the C claim's index from a scratch path, not from a
tracked draft:

```
38:    shutil.copy("/tmp/ScribeReadmeIndex/r74/README.md",LANE+"/corpus/README.md")
```

The bytes are equal today, so nothing is fabricated —

```
$ sha256sum /tmp/ScribeReadmeIndex/r74/README.md corpus/README.md
0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e  /tmp/ScribeReadmeIndex/r74/README.md
0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e  corpus/README.md
```

— but the landing is not re-derivable from the repository (the tracked
`drafts/readme-rows.md`, sha `5efec092…`, holds the rows only, not the file), and
`/tmp` on this host is the filesystem that is currently full. **Fix.** Land the
whole file from a tracked draft (`.ufo/waves/round-74/drafts/README.md`) and have
`apply-landing.py` copy from there; the INDEX leg already checks the result.

### F8 — MEDIUM — `main` gained 532 un-landed scratch paths mid-pass

The wave-2 reading instruction ("`git diff f7104cbce186bc2e1522abf0cfd619cc834628bb
main`") assumes `main` is the lands. It stopped being so at 23:17:06:

```
$ git log --oneline 1d7add3f7b9eaf6f3349c56c36f6d06325d74236..main
92b8d4b hyaku run 7 interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from here
$ git diff --name-only 1d7add3 92b8d4b | awk -F/ '{print $1"/"$2"/"$3"/"$4}' | sort | uniq -c | sort -rn | head -4
    499 .ufo/waves/round-74/assimilation
     31 .ufo/waves/round-74/w2
      1 .ufo/waves/round-74/w2.ready.dispatched
      1 .ufo/waves/round-74/w2.ready
$ git diff --numstat 1d7add3 92b8d4b | awk '{s+=$1} END {print s" lines"}'
79734 lines
$ <sum of added blob sizes>  → 16.0 MB
```

What the snapshot landed:

* `.ufo/waves/round-74/assimilation/validate/` — **483 files**, a full copy of
  the corpus (`SOURCES.md` 964676 B, `README.md`, `QUALITY.md`, `SKILL.md`,
  `LOG.md`, all 478 `corpus/knowledge` entries) built as the SCRATCHMIRROR
  rehearsal (F5's symlink/registry debris rides along in `guard-proof/mirror-*`);
* 31 `.ufo/waves/round-74/w2/` seat files plus the two `w2.ready*` markers.

Why it matters:

1. No claim is graded on these bytes (`claims.json` lands are `c4bf61a` /
   `5e4796c`), yet every later `git diff base main` measurement — this item's own
   instruction, and CritAppendOnly's — now includes them: the graded surface and
   the reported surface have diverged, and the divergence favours a green read
   (added files are appended lines, so Ca's APPENDONLY treats them as legal).
2. It converts worktree scratch into history: `validate/corpus/` is a duplicate
   corpus whose entries can be cited by path in future rounds without a SOURCES
   row, and the mirrors carry planted `S883` rows (F5) plus absolute host
   symlinks.
3. It commits mid-wave seat files before the seats finished, which is the same
   class as R74-M1 (writes into the tree after the push) — here performed by the
   orchestrator under an explicit "not a landing" label.

**Fix.** Make the snapshot `git add -u`-shaped (tracked modifications only) or
snapshot into a scratch branch that `main` does not move to; alternatively
`.gitignore` the fixture roots (`assimilation/validate/`,
`assimilation/guard-proof/mirror-*`) and have the receipts name a `mktemp` path.
A wave-2 seat should also be told a fixed `--lands` rather than "main".

---

## 3. Scope facts I verified for the record

* **No file over 1 MiB in the landed bytes, on either surface.** At the
  dispatched lands (`base..1d7add3`) the largest added blob is
  `230113 .ufo/waves/round-74/w1/w1-results.json` (then the two 127965-byte
  counter copies, 126459). At current `main` the largest added blob is
  `964676 .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md` (from
  F8's snapshot), then `958927/958926/958925/957543` (its mirror registries);
  largest *modified* blob `964676 corpus/SOURCES.md`. The whole tree at `main`
  contains exactly one file over 1 MiB,
  `1597667 reports/round-60/captures/pages/S637.txt` — pre-existing, absent from
  both diffs.
* **The 1 MiB margin is thin but holds**: the fixture and real registry copies
  sit at 92% of the bound.
* **Evidence S877's fetched body is 1 055 723 B (> 1 MiB) but is not stored** —
  `reports/round-74/evidence/S877.txt` is 9 664 B and keeps a 4 098-char window;
  the over-1-MiB object exists only on the wire.
* **Counters' git write verbs appear only inside mktemp dirs** (full enumeration
  in §4.4). The only exception in either counter is F1's fleet `status`.
* **Freeze scripts touch none of `MANIFEST.json`, `scripts/`, `templates/`.**
  The landed diff contains no path under those names; `apply-landing.py` writes
  only `SKILL.md`, `SCORECARD.md`, `corpus/QUALITY.md`, the two entries,
  `corpus/README.md`, `corpus/SOURCES.md`; `build-claims-final.py` writes only
  `reports/round-74/claims.json`; `run-controls.sh` writes only
  `reports/round-74/telemetry/controls-{c,ca}.txt`; `run-guard.sh` writes only
  `guard-proof/out/`; `make-fixtures.py` writes only `guard-proof/mirror-*`. The
  fleet's `scripts/sources-census.sh` and `MANIFEST.json` are only read (and the
  fleet's own `MANIFEST.json` commit `a8292ab8` is fleet rounds-ledger work by
  `protocol-shokunin`, not this lane).
* **Counters reproduce**: `ACCEPT-C-74: PASS legs=13/13` at `c4bf61a` and at
  `main` `1d7add3`; `ACCEPT-CA-74: PASS legs=11/11` at `5e4796c` — the Ca run
  used the fleet **replica** as `--fleet-root`; with a stub fleet root the same
  counter yields `FAIL legs=8/11` with exactly the three fleet-dependent legs red
  (`LEDGER` → `LC-03: stated_fleet path .ufo/reports/round-73/kotodama.md absent
  at pin dad39efd2798`; `APPENDONLY` → `fleet report absent at fleet_pin`;
  `RECEIPTS` → the round-73 counter's own fleet leg), which is what proves those
  legs are fleet-byte checks and not fleet-liveness checks.

---

## 4. Attacks that FAILED (the claim survived), with evidence

### 4.1 Credential material, `op://`, tokens, private URLs, tracking strings — CLEAN

Scan over every **added** line of the whole `base..main` surface (119 890 added
lines; the F8 snapshot alone contributes 79 733 of them and only 3
pattern-shaped hits of its own — 2 × `op://` in the w2 prompt text, 1 × a prose
"secret:"), with a positive control:

```
$ git diff -U0 $BASE main | grep '^+' | grep -v '^+++' > added.txt   # 119890 lines
$ grep -cEi 'op://|gh[pousr]_[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{12,}|xox[baprs]-|eyJ[A-Za-z0-9_-]{8,}\.|-----BEGIN [A-Z ]*PRIVATE KEY|Authorization: [A-Za-z]|api[_-]?key\s*[:=]|access_token=|password\s*[:=]|passwd|secret\s*[:=]' added.txt
18
$ printf 'text op://vault/item ghp_ABCDEFGHIJKLMNOPQRSTUVWX utm_source=x sk-live_ABCDEFGHIJKLMN\n' > ctrl.txt
$ grep -cE 'op://|gh[pousr]_[A-Za-z0-9]{16,}|sk-[A-Za-z0-9_-]{10,}|utm_(source|medium|campaign)=' ctrl.txt
1        # control fires
```

All 18 hits classified, none is a live secret:

* `added.txt:14382` — prose: "need not be an insult or a political secret".
* `:90807`, `:100939` — the word "Authorization:" in reviewer prose.
* `:79151`, `:79243`, `:102179`, `:102779`, `:110456`, `:110955`,
  `:103124`, `:103298`, `:103172` — seat prompts / `dispatch.json` /
  `w1-results.json` that *name* the scan terms ("`op://` refs", "credential
  material"); they carry host paths, not secrets.
* `:101128`–`:101177` — the wave-1 SentinelScope pattern table and its declared
  pre-scan controls (see F6).
* No `op://`, `AKIA`, `xox*`, JWT, `Authorization: <value>`,
  `password=`/`secret=` assignment, presigned-URL parameter
  (`X-Amz-Signature|X-Amz-Credential|Signature=|access_token=|api_key=|sig=`)
  anywhere in the entries, rows, evidence files, receipts or lesson.

Focused scan of the objects the item names — entries, rows, evidence,
receipts — is clean:

```
$ for f in corpus/knowledge/culture-material/worldbuilding-setting-practice*.md \
           reports/round-74/evidence/S{877,881,882,883,884}.txt \
           reports/round-74/telemetry/accept-c-73-at-lands.txt \
           reports/round-74/telemetry/accept-ca-73-at-lands.txt \
           corpus/lessons/round-74.md; do …; done
--- …/worldbuilding-setting-practice.md: 68:| real world plus a local lie | … | answer why the public never notices the secret |
--- all others: CLEAN
```

(the one hit is the word "secret" in the entry's own secret-worlds table.)

### 4.2 Tracking query strings — NONE on any cited URL

```
$ grep -nE 'https?://[^ )|>`"]+\?[^ )|>`"]*' <both entries> reports/round-74/evidence/*.txt corpus/lessons/round-74.md
(no output)
$ grep -ohE 'https?://[^ )|>`"]+' <both entries> | sort | uniq -c
   1 https://litmemo.com/ja/blog/novel-worldbuilding-guide
   1 https://tuduku.space/column/novel-worldbuilding
   1 https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html
   1 https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
   1 http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
```

The four C URLs (plus reused S877) carry no query string at all. The
registry rows add archive.org copies that embed the original URL in the path
(`…/web/20250610015519id_/https://www.chinawriter.com.cn/…`), also parameter-free.
The 12 query-string-shaped hits anywhere in the added lines are either the
pre-existing British Library row `?ref=Cotton_MS_Vitellius_A_XV` (a document
selector, present at base: `git show $BASE:corpus/SOURCES.md | grep -c '^| S329 '`
= 1), a scout's *recorded observation* that CDX also lists
`…html?utm_source=chatgpt.com` (a different URL, described, not cited), or the
positive-control text.

### 4.3 The four source URLs are public ordinary-means pages — CONFIRMED, byte-identical

Fetched with the recorded browser UA, then again with curl's default UA:

| row | URL | HTTP | bytes | sha256 (fetched) | = committed evidence sha256 | redirects |
|---|---|---|---|---|---|---|
| S881 | `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 101615 | `441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64` | yes | 0 |
| S882 | `https://tuduku.space/column/novel-worldbuilding` | 200 | 17068 | `754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7` | yes | 0 |
| S883 | `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | 200 | 48536 | `a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d` | yes | 0 |
| S884 | `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | 200 | 62604 | `344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659` | yes | 0 |

```
$ curl -sS -L --max-time 45 -A '<browser UA>' -o page$i.bin -D hdr$i.txt \
    -w 'http=%{http_code} bytes=%{size_download} redirects=%{num_redirects} final=%{url_effective} ip=%{remote_ip}' "$u"
http=200 bytes=101615 redirects=0 final=https://litmemo.com/ja/blog/novel-worldbuilding-guide ip=34.54.165.144
http=200 bytes=17068  redirects=0 final=https://tuduku.space/column/novel-worldbuilding            ip=210.131.237.245
http=200 bytes=48536  redirects=0 final=https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html ip=2606:1980:17::cf
http=200 bytes=62604  redirects=0 final=https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html ip=2606:1980:17::cf
$ # headers carried no www-authenticate, no set-cookie, no location, no consent/geo/bot wall
$ # curl default UA repeats all four with the same codes and byte counts
default-UA 200 101615 redirects=0 :: https://litmemo.com/ja/blog/novel-worldbuilding-guide
default-UA 200 17068  redirects=0 :: https://tuduku.space/column/novel-worldbuilding
default-UA 200 48536  redirects=0 :: https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
default-UA 200 62604  redirects=0 :: https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html
```

Public addresses only; no redirect; no private host; identical bytes to what the
evidence files record, ~24 h after their fetch (`fetched: 2026-10-26T01:0xZ`,
i.e. 2026-10-25 22:0x −03). Each Gate quote is present in the page I fetched
(S882 needed entity/tag decoding: the quote is `勢力図・人間関係の構造` +
`：誰が権力を持ち、何が対立の軸になっているか` — 11 + 1 + 21 = 33 characters — split by
`</strong>` on the live page and contiguous in the stored window, which is what
the extractor's "block tags → newline, inline tags dropped" rule produces).

Evidence files are ordinary pages' captures, browser-shaped UA on all five
(`ua:` line verbatim as above), `http: 200`, `bytes` and `sha256` matching, and
no cookie/authorization data stored (`grep -inE 'cookie|authorization|x-api|session'
reports/round-74/evidence/*.txt` → no match).

### 4.4 No write into the lane clone, no git write outside clones (static + observed)

* Whole clone hashed before/after each counter run
  (`find . -path ./.git -prune -o -type f -print0 | xargs -0 sha256sum`, 7350
  entries): `cmp` byte-identical after `accept-c` and after `accept-ca`.
* Every git write verb in both counters, and its target:

| site | verb | target |
|---|---|---|
| `accept-c.py:292,297` | `clone`, `checkout --detach` | `dest` inside `TemporaryDirectory` (`main`:1964-1974) |
| `accept-c.py:2010,2013,2485` | `add -A`, `commit`, `init` | `lane`/`fleet` = `tempfile.mkdtemp` (`build_fixture`:2477-2482) |
| `accept-c.py:308` | `archive` on `--root` | read-only |
| `accept-ca.py:369,374` | `clone`, `checkout --detach` | `dest` = `tmpdir` (`mkdtemp` at 1966) |
| `accept-ca.py:1715` | `checkout -B main` | the round-73 clone under the same `tmpdir` |
| `accept-ca.py:2129-2148,2551,2577,2607` | `add`, `reset`, `commit`, `checkout -B`, `branch -f`, `merge`, `rm` | selftest `lane`/`fleet` = `mkdtemp` (2260-2262) |
| `accept-ca.py:1449` | **`status` on `--fleet-root`** | **the fleet root — F1** |

  All other invocations are `cat-file`, `rev-parse`, `show`, `diff`, `rev-list`,
  `merge-base`, `ls-tree`, `grep` against objects; none touches a worktree or an
  index.
* `accept-c` leaves a fleet root alone entirely — sandbox stub fleet with a stale
  stat on the probe path, index `725cd5f4…` before and after its `PASS
  legs=13/13`; it has no `git -C <fleet>` call at all, only `os.path.join`
  + `subprocess.run([script, "validate", "--root", <temp fleet>, …])`.
* The census subprocess is invoked with `--root <TemporaryDirectory>` and no
  `OUT` (`accept-c.py:1447-1459`); with `OUT` set by me on the real script it
  still printed to stdout and left my marker file at 18 bytes, so I found no
  truncation channel there.
* I wrote nothing under `/home/vgpnk/Projects/shokunin`: every fleet access was
  `git log/show/ls-tree/ls-files --debug` (`--no-optional-locks`), `ls`, `stat`,
  or the `git clone` into `/var/tmp`.

### 4.5 Evidence window geometry is bounded, and S882's whole-document scope is honest

`window-scope` values are `excerpt` for S877/S881/S883/S884 (window 4098–4104
chars, whole page visible-chars 492810 / 9855 / 8162 / 12270) and
`whole-document` for S882 (2953 chars, page 2953). Stored windows are 7677–12319
bytes on disk. Observation for the rights-aware reviewer, not a rule I can
adjudicate: the repo now holds verbatim third-party text up to ~4100 CJK
characters per page (S882 in full), which for S883/S884 is a large fraction of
the article. The claim's EVIDENCE floor (≥4096 chars around the quote) is what
forces this; nothing in this seat's mandate rules on it.

### 4.6 The two counters reproduce the claim's verdicts

```
$ # claim C, own clone, fleet replica (or a byte-identical stub fleet root)
ACCEPT-C-74: PASS legs=13/13           # at c4bf61a and at main 1d7add3, exit 0
$ # claim Ca, own clone, main pinned to its own lands
ACCEPT-CA-74: PASS legs=11/11          # at 5e4796c, exit 0 (fleet replica)
```

With a stub fleet root instead of the replica, Ca yields `FAIL legs=8/11` and the
three red legs are exactly the fleet-byte legs (`LEDGER` LC-03, `APPENDONLY`
fleet report pin, `RECEIPTS` round-73 re-run), which confirms those legs read
fleet commit bytes rather than live fleet state — and confirms that the PASS
does not depend on the fleet being the *real* root (`--fleet-root` is
unauthenticated; worth remembering when reading the sentence in F2).

---

## 5. Residual (what I did not establish)

* I did not run the Ca counter against the **real** fleet root: F1 says that run
  can write the fleet repo, and the seat mandate forbids it. The 11/11 I report
  is on a `git clone` replica with identical commits; the three fleet-byte legs
  therefore certify commit bytes, not the live root's worktree, and the
  live-root worktree limb is the F1/F2/F3 surface.
* I did not fetch `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` (S877,
  reused row, not one of the four). Noted for the record that its capture is a
  1 055 723-byte PDF fetched over **cleartext http** with
  `quote-found-verbatim: no` (PDF line breaks; found after folding) — the sha256
  in the evidence is the only integrity anchor on that body.
* I did not grade content fidelity of the rows/entries (other seats own GATE,
  EVIDENCE, REPOINTED, REPAIRS); I checked only the safety/scope limbs named in
  my item.
