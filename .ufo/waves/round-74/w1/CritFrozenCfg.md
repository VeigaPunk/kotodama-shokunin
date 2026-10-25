# CritFrozenCfg — attack on hardening H1 (counter constants read at a named freeze commit)

Seat: CritFrozenCfg (critic, leaf; no delegation, no background jobs, no `task`).
Round 74 / hyaku run 7, lane `kotodama-shokunin`, base `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Lane written: this file only. Fixtures, downloads and logs live under `/tmp/CritFrozenCfg/`
(`fx/<name>/lane` per fixture, `run.log`, `build.py`, `acceptc.tmpl`, `pincheck.py`).
Nothing was installed; pacman not used; no network fetch was made.

## 0. The target, quoted exactly

The hardening under attack is the one the round-74 build item names as **(H1)** and the one the two
DRAFT claims already carry as a leg:

- `reports/round-74/claims.json:87` (claim C) — `FROZENCFG: row set, entry paths, fragments, map and every constant the counter uses are read from claims.json AT the <freeze> commit (git show), never from the graded tree; <freeze> must be a strict ancestor of <lands>`
- `reports/round-74/claims.json:111` (claim Ca) — `FROZENCFG: ledger, constants and allowlists are read from claims.json/ledger.json AT <freeze> (git show), never from the graded tree; <freeze> is a strict ancestor of <lands>`
- The counters' CLI (`reports/round-74/claims.json` `counter`, build item `ExecCCounter`) is
  `python3 -B reports/round-74/accept-c.py --root . --lands <lands> --freeze <freeze>`; Ca adds `--fleet-root`.
- The quality candidate for the round states the same rule (`QUALITY 25`, draft clause (a),
  `.ufo/waves/round-74/drafts/quality-25.md:12`): required `--freeze`, `git merge-base --is-ancestor <freeze> <lands>`,
  constants via `git show <freeze>:…`, no worktree constant.

What H1 actually establishes is only: *the constants are read from a commit the caller names, and that
commit is an ancestor of `--lands`*. It does not establish **which** ancestor, **whether it was the
freeze when anyone scored**, **whether the graded tree still carries those bytes**, or **whether the
counter that ran is the counter that was frozen**. Those four gaps are the attacks below.

Today's red-before (round-73 bytes, run from this lane, read-only, 2026-10-25):

```
$ python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102
# config source: lands tree: row_set, entries, rejects.refused_staged, rejects.refused_files, rejects.families, rejects.forbidden_ids, ground.fragments
ACCEPT-C-73: PASS legs=11/11
```

`load_config()` prefers the graded tree, then the lane worktree (`reports/round-73/accept-c.py:432-437`);
the only committed config-source line in round-73 telemetry is `# config source: lane worktree: …`
(`reports/round-73/telemetry/controls-c.txt:13`). H1 removes exactly that. The attacks below show it
does not remove the next four.

## 1. Method — twelve throwaway repos, two model counters

Round-74's real counters do not exist yet, so I attacked the *rule*, not a file: one model counter
(`/tmp/CritFrozenCfg/acceptc.tmpl`) with four legs, built in two variants:

- **naive** = H1 as drafted: `--freeze` 40-hex, strict ancestor of `--lands`, constants read with
  `git show <freeze>:reports/round-74/claims.json`; legs `ANCESTRY`, `ROWS`, `ENTRIES` (3 legs).
- **hard** = H1 plus the candidate corrections this report proposes; legs `ANCESTRY`, `ROWS`, `ENTRIES`,
  `FROZENCFG` (4 legs). Every attack fixture is graded twice, by the same legs, so a PASS/FAIL delta is
  attributable to `FROZENCFG` and nothing else.

Each fixture is its own repo, `D=$(mktemp -d)`-equivalent under `/tmp/CritFrozenCfg/fx/<name>/lane`,
`git init -q` there, `git rev-parse --show-toplevel` verified equal to the repo path before the first
commit, and every git call names `-C <repo>`; all commits use `-c user.name=fx -c user.email=fx@fx.invalid`
inside that repo only. Full transcript: `/tmp/CritFrozenCfg/run.log`. Rebuild:
`python3 -B /tmp/CritFrozenCfg/build.py`.

Two further fixtures (`counter-revision`, `counter-revision-missing`) exercise the post-freeze
counter-revision door with a second hard variant (`/tmp/CritFrozenCfg/acceptc2.py`, same checks plus the
`counter-revisions.md` row).

Leg counts are the model's, not the round's: the real counters will carry 12 (C) and 11 (Ca) legs. The
attacks hit the frozen-constant provenance only; they say nothing about the other legs.

## 2. Results — every attack that survives H1

| fixture | lands shape | naive (H1 as drafted) | hard (this report's rule) |
|---|---|---|---|
| `legit` | base → F(freeze) → data → tail | PASS 3/3 | PASS 4/4 |
| `claims-edit` | base → F → data(2 rows) → **E rewrites claims to 2 rows** → tail | **PASS 3/3 with `--freeze E`** | FAIL `--freeze E` and FAIL `--freeze F` |
| `killrule-edit` | base → F → data → **E2 rewrites `kill_rule`** → tail | **PASS 3/3 with `--freeze F`** | FAIL (2 claims commits; blob ≠) |
| `revert-edit` | base → F → data → E shrink → **R restore F's bytes** → tail | **PASS 3/3** | FAIL (`claims.json touched by 3 commit(s)`) |
| `merge-parent` | base → F → data(2) ; side edits claims(2) ; lands = merge | **PASS 3/3 with `--freeze <side>`** | FAIL (`touched by 2`; blob ≠) |
| `side-freeze` | data on main ; freeze on a side branch ; lands = merge | **PASS 3/3 with `--freeze <side F>`** | FAIL (`freeze not on the lands first-parent chain`) |
| `merge-first-parent` | data on main ; freeze on a branch ; **main merged INTO the freeze branch** | **PASS 3/3** | **PASS 4/4 — SURVIVOR** |
| `late-freeze` | base → data → F → tail | PASS 3/3 | **PASS 4/4 — SURVIVOR** |
| `counter-modified` | legit data ; lands replaces `accept-c.py` with a 3-leg weaker counter (no `FROZENCFG`) | **PASS 3/3** (weakened file run from the worktree) | FAIL (`counter bytes differ between freeze and lands`) |
| `replace` | orphan "freeze" O ; `git replace --graft <lands> <O>` | **PASS 3/3** (forged ancestry) | FAIL (`refs/replace present`, `ancestor=False`) |
| `legit` + main moved | `--lands` is a clean commit that is no longer `main` | **PASS 3/3** | **PASS 4/4 — SURVIVOR** (closure tip check fails) |
| `counter-revision` | lands replaces the counter and discloses `old_sha256 -> new_sha256` | PASS 3/3 | PASS 4/4 (`counter=rev:r2 lands=rev:r2`) |
| `counter-revision-missing` | lands replaces the counter, no revisions row | **PASS 3/3** | FAIL (`names no row`) |

### (a) Freeze is an ancestor, but the claims were edited after a seat scored

Fixture `claims-edit`: a seat scores S883/S884 out; the L1 lands two rows and then commits `E`, a new
`claims.json` whose `row_set` is the two survivors, then a telemetry commit (lands). The counter then
nominated `E` as `--freeze`, which is a strict ancestor of lands:

```
$ python3 -B …/acceptc_naive.py --root . --lands 3de93cf7… --freeze 0c687817…
LEG PASS ANCESTRY freeze40=True lands40=True strict=True ancestor=True
LEG PASS ROWS base=2adf2f01… added=S881 S882 want=S881 S882
ACCEPT-C-74: PASS legs=3/3
```

The declaration in `claims.json` (`"frozen": null`, status text "frozen by the commit that adds the final
claims.json") is not consulted by H1, and the caller's `--freeze` is the only identity of the freeze.
Variants: `killrule-edit` (row set unchanged, `kill_rule` relaxed after the data landed) passes with the
**real** freeze hash, because H1 reads the freeze constants and never compares them with the lands file;
`revert-edit` (edit the claims after scoring, then restore the freeze bytes) also passes the naive rule.

### (b) Lands contains the freeze as a merge parent

Two directions, and they do not have the same answer.

- *Freeze as the second parent, claims smuggled from the side* (`merge-parent`): lands
  `016e46a2 7d7ca485 1fc4d6b6`; the side commit carries the shrunken claims; H1 passes with
  `--freeze <side>`. The naive *ROWS* leg cannot see it because `--lands`' tree holds only the two rows
  the side commit wants.
- *Freeze as the first parent, data merged into the freeze branch* (`merge-first-parent`): data is
  committed first, then the freeze is created on a branch from the base, then main is merged **into**
  the freeze branch:
  ```
  $ git -C …/merge-first-parent/lane rev-list --parents -1 592b3739…
  592b37393d308ca10311da1aafdde19e54a02c7d ba1b5215c93f3e8421d285466d654fbba9423cf1 8379e3c5c4a9b2c97ddcbfbde7700bd5646d6106
  ```
  The hard counter **PASSES 4/4**. Every lane-local invariant this report proposes holds: the sole
  claims commit is the freeze, the blob matches at lands, the freeze is the first parent, the sidecar
  and self-hash match. The freeze was still created *after* the data was scored. This is (a)'s late
  freeze wearing a merge's clothes; no lane-local check can reject it.

### (c) Freeze is an ancestor but on a different branch tip

`side-freeze`: data on main, freeze on `freeze-side`, lands = `git merge --no-ff freeze-side`. H1
passes with the side freeze as `--freeze`. The first-parent rule rejects this shape
(`freeze not on the lands first-parent chain`; the chain is `c372d27 8379e3c 2adf2f0`, the freeze
`ba1b5215` is absent), but the lander controls the merge direction: `merge-first-parent` shows the
same trick re-parented so the rule passes. So the first-parent rule is not a timing witness — it only
kills the lazy shape and forces the lander to write the merge the other way round, which is a
`git checkout F && git merge main` away.

### (d) The counter source changed after the freeze

`counter-modified`: the lands tree carries a three-leg counter (no `FROZENCFG`) and the command named in
the claim runs *that* file; it prints `ACCEPT-C-74: PASS legs=3/3` and its receipt carries the weakened
file's sha256. H1 never compares the running bytes with the freeze. Pinning inside `claims.json` is
circular (the counter's digest would have to live in a file the counter grades), so the pin must live
in an artifact the hash of the freeze covers — see §4.

Ancestry itself is forgeable in the grading repo: `git replace --graft <lands> <orphan>` makes
`git merge-base --is-ancestor <orphan> <lands>` exit 0 for a commit that is not an ancestor
(`exit=1` before the replace, `exit=0` after, `exit=1` again with `GIT_NO_REPLACE_OBJECTS=1`), and
`refs/replace/569c01ee…` is the only trace. `.git/info/grafts` is the same door. H1 as drafted never
looks.

### (e) `--lands` is a clean commit that is no longer the branch tip

Nothing in H1 or in checks 1-7 forces `<lands>` to be the revision that `main` (and the remote) actually
carries. On the `legit` fixture, after the PASS receipt was reproducible, one commit moved `main` past
the graded lands:

```
$ git rev-parse main
c30a234b247e04f93acfe83590cc487b024c138f        # main now
$ python3 -B …/acceptc_hard.py --root . --lands 86dcbe79… --freeze ba1b5215…
ACCEPT-C-74: PASS legs=4/4
$ test "$(git rev-parse main)" = "86dcbe79…"; echo $?
1
```

The counter grades a baited clean sub-history while the branch carries different bytes. Closure check
(not a counter check — retro-grading an old lands is legitimate when the receipt says so):
`test "$(git rev-parse main)" = "$L"` for a receipt produced at the lands, or the receipt's
`measured revision (lane main)` line must equal `<lands>`; round 73's own receipt did *not* satisfy this
(`# measured revision (lane main): f7104cb` while `--lands 0316b888`), which is a retro-grade and must be
disclosed as one.

## 3. What a closure can and cannot know about (a)

**Detectable in the lane, mechanically:**
1. a *second* commit touching `reports/round-74/claims.json` after the first one, including an
   edit-then-revert (`revert-edit`: `claims.json touched by 3 commit(s) … 4d13c004 c62f6ac6 ba1b5215`);
2. a lands `claims.json` blob different from the freeze blob (edits without a commit touching the path
   are impossible to grade; uncommitted worktree edits are already excluded by QUALITY 19 materialization);
3. a smuggled claims blob in a merge result (`merge-parent`).

**Not detectable in the lane:** whether the single `claims.json` commit existed when the first seat
scored landed data. Git cannot witness wall-clock order: the round-73 freeze commit
`af65165` carries author date `2026-10-25T12:52:54-03:00` — *identical* to the round-73 base
`8841ad3`'s author date, i.e. inherited — and committer date `2026-10-25T19:50:10-03:00`; the round-73
lands `0316b88` is at `20:00:54`. Dates are inputs, not evidence. A late freeze (`late-freeze`
fixture) passes the hard counter 4/4.

**Where the freeze hash is pinned today, and why neither pin is an anchor:**

| candidate pin | evidence | why it is not an anchor |
|---|---|---|
| `LOG.md` / `SCORECARD.md` row | lane files | inside the graded repo; the lander writes them before lands |
| wave-2 `dispatch.json` / `spec.json` | `.ufo/waves/round-73/w2/dispatch.json` names `freeze commit af65165cf269…` | also in the lane; in round 73 it was committed only in `7aa8f99` (a lands commit), not at the freeze |
| fleet report `.ufo/reports/round-73/kotodama.md` | fleet repo commit `dad39efd` (2026-10-25T20:43:14-03:00) | (i) it records **`af65165`, 7 hex** — `git grep -o 'af65165[0-9a-f]*'` over the fleet repo returns only `af65165`; the full 40-hex appears nowhere in the fleet repo's tracked files (`git grep` over the fleet repo, exit 1); (ii) written after the freeze (19:50) and after the lands (20:00), so it cannot order anything |
| fleet ledger / state | `.ufo/state/*` are lane mission files, lane-writable | same repo class as the lane for this purpose |

So the honest answer to "how would a closure know?" is: **it can know that the claims did not move
after the first claims commit, and it cannot know when that commit was made.** The only object that can
decide the second question is a fleet-root pin (the fleet repo is `/home/vgpnk/Projects/shokunin`, a
separate git repo that tracks zero lane files — `git ls-files | grep -c '^kotodama-shokunin/'` = 0 — and
that the lane's seats are forbidden to write) written and committed **at freeze time, before the first
seat that scores landings is dispatched**. A 7-hex prefix is not enough: 28 bits is mintable, and an
ambiguous prefix in the grading repo resolves to nothing useful for the attacker only by accident.

## 4. Exact scheme (smallest safe correction)

### 4.1 Freeze content

The freeze commit `F` contains, in one commit:

```
reports/round-74/claims.json
reports/round-74/ledger.json
reports/round-74/accept-c.py
reports/round-74/accept-ca.py
reports/round-74/freeze.json          # sidecar, machine-readable pin
reports/round-74/telemetry/controls-c.txt
reports/round-74/telemetry/controls-ca.txt
reports/round-74/telemetry/junk/<slug>.txt   # the five junk landings' receipts
```

The sidecar, committed **in the same commit** (no chicken-and-egg: nothing below contains its own hash):

```json
{
  "round": 74,
  "lane": "kotodama-shokunin",
  "base": "f7104cbce186bc2e1522abf0cfd619cc834628bb",
  "counters": {
    "reports/round-74/accept-c.py":  "<sha256 of those bytes>",
    "reports/round-74/accept-ca.py": "<sha256 of those bytes>"
  },
  "files": {
    "reports/round-74/claims.json": "<sha256>",
    "reports/round-74/ledger.json": "<sha256>",
    "reports/round-74/telemetry/controls-c.txt": "<sha256>",
    "reports/round-74/telemetry/controls-ca.txt": "<sha256>",
    "reports/round-74/telemetry/junk/stub-entries.txt": "<sha256>",
    "…": "…"
  }
}
```

Commit message (the commit object hashes it, so it can be read back at any later revision):

```
round-74: freeze — claims C+Ca, ledger, counters, freeze sidecar, do-nothing + junk-landing controls

freeze-74 sidecar-sha256: <sha256 of reports/round-74/freeze.json>
freeze-74 files: <n>
```

`claims.json` keeps `"frozen": null`: a commit cannot contain its own hash, and the freeze is derived
(§4.2.3), not declared. A non-null `frozen` at `F` or at lands is a fail (it would name some other
commit — the "freeze" that is not the freeze).

### 4.2 Counter checks (the FROZENCFG leg, made exact)

Every check below runs with `GIT_NO_REPLACE_OBJECTS=1`, with `GIT_DIR`, `GIT_WORK_TREE`,
`GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR` unset.
`<base>` is read from `git show <freeze>:reports/round-74/claims.json`; nothing comes from the graded
tree or the worktree.

1. **Revision syntax and type.** `--freeze` and `--lands` match `^[0-9a-f]{40}$`;
   `git cat-file -t` is `commit` for both; `<freeze> != <lands>`.
2. **Ancestry, unforged.** `git merge-base --is-ancestor <freeze> <lands>` exits 0;
   `git for-each-ref refs/replace` is empty; `$(git rev-parse --absolute-git-dir)/info/grafts` does not exist.
3. **Derived freeze.** `<base>` is 40-hex and `git merge-base --is-ancestor <base> <freeze>` exits 0
   (a slideable range is not a range); `git rev-list --full-history <base>..<lands> --
   reports/round-74/claims.json` prints exactly one commit and it equals `<freeze>`. This closes
   edit-then-revert and the merge-smuggled claims; `--full-history` prevents merge simplification from
   hiding a side commit.
4. **Lands fidelity.** `git rev-parse <freeze>:reports/round-74/claims.json` equals
   `git rev-parse <lands>:reports/round-74/claims.json` (byte equality; catches an edit committed
   without moving the row set, and catches a merge result that takes another parent's claims).
5. **Shape.** `<freeze>` is on `<lands>`' first-parent chain (kills the lazy side-branch freeze).
   State in the leg text that this does not order the freeze against the data (the `merge-first-parent`
   survivor) — the pin does.
6. **Sidecar.** `git show <freeze>:reports/round-74/freeze.json` parses; every `files` entry's digest
   equals `sha256(git show <freeze>:<path>)`; `git show <freeze>:reports/round-74/claims.json` digest
   equals `files[…]`; the commit message carries `round-74 freeze` and
   `freeze-74 sidecar-sha256: <sha256(sidecar)>`; the claims file is a regular blob (`ls-tree` mode
   `100644`/`100755`, not `120000`/`160000`).
7. **Counter identity.** `sha256(open(__file__,'rb').read())` equals `counters[<the counter's own
   COUNTER_REL constant>]`; and `git rev-parse <freeze>:reports/round-74/accept-c.py` equals
   `git rev-parse <lands>:reports/round-74/accept-c.py`, **or** `reports/round-74/counter-revisions.md`
   (committed at lands, append-only, no removed lines) carries a row whose `old_sha256` is the freeze
   blob's content digest and whose `new_sha256` is the running digest, with a non-empty reason and
   `predicate unchanged`. Round 73 needed this door: claim C's counter blob is identical at freeze and
   lands (`5c254138…`), claim Ca's is not (`d12021be…` → `a4c318bb…`, i.e. r1 `f8ebb5d8…` → r3
   `222d4dd6…`, recorded in `reports/round-73/counter-revisions.md:5,11`).
   The revision row's digests must be content sha256, not git blob ids, and both old and new must be
   present — round 73's r2 row records its digest only as a bare line (`counter-revisions.md:9`), which a
   machine check cannot pair with a file.
   *Exercised* (`/tmp/CritFrozenCfg/rev.log`): `counter-revision` — freeze counter sha256 `6d5aad4c…`,
   lands counter `2078c5f0…`, row `| r2 | reports/round-74/accept-c.py | 6d5aad4c… | 2078c5f0… | comment-only, self-sha moves | unchanged |`
   → `LEG PASS FROZENCFG … counter=rev:r2 lands=rev:r2`, `ACCEPT-C-74: PASS legs=4/4`, and the freeze
   bytes extracted from the freeze commit also PASS (`counter=freeze lands=rev:r2`). Without the row
   (`counter-revision-missing`) the same lands prints `LEG FAIL FROZENCFG … running counter bytes !=
   freeze bytes and counter-revisions.md names no row; counter blob differs between freeze and lands and
   no revision row`, exit 1.
   The claim already fixes `n` at freeze (`legs=<n>/<n>`); a counter that drops `FROZENCFG` prints a
   smaller fraction and is caught by the count, and the counter must additionally emit exactly the leg
   names in the frozen claim's `legs` array (the `NAME:` prefix of each string, e.g. `FROZENCFG`). A
   weakened counter can re-pad the count with no-op legs, so the digest — not the fraction — is the
   load-bearing check; the count and names are cheap cross-checks for the closure.
8. **Receipt.** Header lines the closure can compare without parsing prose:
   ```
   # freeze: <freeze 40hex>
   # freeze derived: sole claims.json commit in <base>..<lands>
   # freeze pin: required outside the lane (.ufo/reports/round-74/kotodama-freeze.txt)
   # counter sha256 (self): <sha256>
   # counter sha256 (freeze): <sha256>
   # config source: claims.json @ <freeze> (freeze, strict ancestor of <lands>); constants: row_set, entries, rejects, ground, allowlists
   ```
   No receipt and no counter byte may contain `config source: lands tree` or `config source: lane worktree`.

### 4.3 Fleet-root pin (written at freeze time, outside the lane)

`.ufo/reports/round-74/kotodama-freeze.txt`, committed by the orchestrator in the fleet repo
(`/home/vgpnk/Projects/shokunin`) **before** dispatching the first seat that scores landings:

```
round 74 freeze pin
lane kotodama-shokunin
base f7104cbce186bc2e1522abf0cfd619cc834628bb
freeze <freeze 40hex>
sidecar-sha256 <64hex>
claims-sha256 <64hex>
counter-c-sha256 <64hex>
counter-ca-sha256 <64hex>
```

Closure check (`pincheck.py` shape, exercised on the fixtures):

```sh
test "$(sed -n 's/^freeze //p'      "$PIN")" = "$F"
test "$(sed -n 's/^sidecar-sha256 //p' "$PIN")" = "$(git cat-file blob "$F":reports/round-74/freeze.json | sha256sum | cut -d' ' -f1)"
test "$(sed -n 's/^claims-sha256 //p'  "$PIN")" = "$(git cat-file blob "$F":reports/round-74/claims.json  | sha256sum | cut -d' ' -f1)"
```

A missing pin withholds the verdict (it is not a pass-by-default). Fixture evidence:
`late-freeze` + a pin written for the earlier freeze → `PIN FAIL … pinned freeze 'ba1b5215…' != receipt
freeze '7761aba0…'`, exit 1; the same pin written after the data with the late hash → `PIN PASS`,
which is exactly why the pin must be written and committed at freeze time.

Residual, stated plainly: the pin is only as honest as the orchestrator's own commit. What it buys is
that a *lane* seat, and any lander rewriting the lane's LOG/SCORECARD/dispatch, cannot move it. A
stronger witness would be the remote's push history (GitHub push event for the freeze commit at freeze
time); that is out of scope for a leaf seat and needs network/auth, so the fleet pin is the smallest
available anchor.

## 5. Red-before commands (copy-paste, run from the lane root)

```sh
BASE=f7104cbce186bc2e1522abf0cfd619cc834628bb
L=<lands-40hex>; F=<freeze-40hex>
PIN=/home/vgpnk/Projects/shokunin/.ufo/reports/round-74/kotodama-freeze.txt

# R0 constants come from the freeze, never from graded bytes
python3 -B reports/round-74/accept-c.py --root . --lands "$L" --freeze "$F" \
  | grep -nE '^# (config source|freeze|counter sha256)'
#  must show "# config source: claims.json @ $F (freeze, strict ancestor of $L); constants: …"
#  must NOT contain "lands tree" or "lane worktree"
#  (red before H1: round-73 r1 printed "# config source: lands tree: row_set, …", quoted in §0)

# R1 claims did not move after the freeze (covers edit, edit+revert, merge smuggling)
test "$(git rev-list --full-history "$BASE".."$L" -- reports/round-74/claims.json)" = "$F"
test "$(git rev-parse "$F":reports/round-74/claims.json)" = "$(git rev-parse "$L":reports/round-74/claims.json)"

# R2 freeze is mainline, not a side-branch tip
git rev-list --first-parent "$L" | grep -qx "$F"

# R3 the running counter is the frozen counter (or a disclosed revision)
test "$(git cat-file blob "$F":reports/round-74/accept-c.py | sha256sum | cut -d' ' -f1)" \
   = "$(sha256sum $PWD/reports/round-74/accept-c.py | cut -d' ' -f1)"   # else counter-revisions row

# R4 ancestry is not grafted/replaced
test -z "$(git for-each-ref --format='%(refname)' refs/replace)"
test ! -e "$(git rev-parse --absolute-git-dir)/info/grafts"
GIT_NO_REPLACE_OBJECTS=1 git merge-base --is-ancestor "$F" "$L"

# R5 external pin (fleet repo; written at freeze time)
test -f "$PIN" && test "$(sed -n 's/^freeze //p' "$PIN")" = "$F"

# R6 lands is the tip that carries the claim, not a baited sub-history
test "$(git rev-parse main)" = "$L"            # or: receipt "measured revision (lane main)" == $L
```

The naive-vs-hard deltas that prove each check is load-bearing are the table in §2; the exact
commands for each fixture are in `/tmp/CritFrozenCfg/run.log` (search `### run`). Examples that must be
red before the correction and green after:

```
naive --freeze <edit commit>   → ACCEPT-C-74: PASS legs=3/3      (claims-edit)
hard  --freeze <edit commit>   → LEG FAIL FROZENCFG derived=ambiguous … touched by 2 commit(s) …: 0c687817 ba1b5215
naive --freeze <real freeze>   → ACCEPT-C-74: PASS legs=3/3      (killrule-edit, revert-edit)
hard  --freeze <real freeze>   → LEG FAIL FROZENCFG … claims.json bytes differ between freeze and lands
naive --freeze <side commit>   → ACCEPT-C-74: PASS legs=3/3      (merge-parent)
hard  --freeze <side commit>   → LEG FAIL FROZENCFG … touched by 2 commit(s): 1fc4d6b6 ba1b5215 …
naive --freeze <side F>        → ACCEPT-C-74: PASS legs=3/3      (side-freeze)
hard  --freeze <side F>        → LEG FAIL FROZENCFG … freeze not on the lands first-parent chain
weakened counter in lands      → ACCEPT-C-74: PASS legs=3/3      (counter-modified)
freeze bytes, same lands       → LEG FAIL FROZENCFG … counter bytes differ between freeze and lands
naive --freeze <orphan O>      → ACCEPT-C-74: PASS legs=3/3      (replace)
hard  --freeze <orphan O>      → LEG FAIL ANCESTRY … ancestor=False / LEG FAIL FROZENCFG … refs/replace present
```

## 6. Fixable defect vs. tradeoff the judge cannot reject

- **Fixable in the counter (must be added to the FROZENCFG leg as frozen text):** the freeze identity
  (derived, not nominated), the claims-blob equality, the merge-smuggled claims, the counter-bytes
  identity with a revision door, replace/graft refusal, the regular-blob mode check, and the receipt
  grammar. Fixtures show each failing closed.
- **Not fixable in the lane:** (`late-freeze`, `merge-first-parent`) the ordering of the freeze against
  the first scoring seat. No lane-local rule can decide it without trusting dates or the caller. The
  canonical judge must not read "FROZENCFG PASS" as "the constants predate the data"; the claim text and
  the receipt wording must say the pin decides that, and the closure must withhold a verdict without
  the pin.

## 7. Impacted axes and artifacts (for the owners; I edited none of them)

- **C (coverage)** — leg text `reports/round-74/claims.json:87`; `counter`/`after` strings (the after string
  already requires `--freeze`; the leg must carry §4.2). `reports/round-74/accept-c.py` (building now)
  must implement §4.2 and print §4.2.8; its junk landing `config-edit-in-graded-tree`
  (QUALITY 25 draft table) must fail `FROZENCFG`, and the sidecar/junk receipts must be in the freeze commit.
- **Ca (calibration)** — leg `claims.json:111`; `reports/round-74/accept-ca.py`; the ledger read must be
  `git show <freeze>:reports/round-74/ledger.json` (r3's `load_ledger` reads at `<lands>`,
  `reports/round-73/accept-ca.py:403-430`); the revision door matters most here (Ca's counter changed
  in round 73).
- **QUALITY 25 (quality candidate)** — clause (a) as drafted is H1 and inherits (a)–(d); add the
  derived-freeze, blob-equality, counter-identity and pin clauses, or the criterion certifies the same
  survivors it was written to close.
- **SKILL.md gate rows** (accept-c-74 / accept-ca-74) — must state `--freeze` is required and that the
  receipt names `# freeze:` / `# counter sha256 (freeze):`, so a reviewer can run R0/R3 without reading code.
- **Fleet report** — record the full 40-hex freeze and the sidecar/claims digests (round 73 recorded
  `af65165`, 7 hex, in `.ufo/reports/round-73/kotodama.md:7,10,18`).

## 8. Evidence index

- Round-73 freeze provenance: `af65165` adds `reports/round-73/claims.json`; zero commits in
  `af65165..0316b88` touch it; `af65165` is on `0316b88`'s first-parent chain; claim-C counter blob
  `5c254138…` identical at freeze and lands; Ca counter differs (r1→r3, `counter-revisions.md:5,11`).
- Dates: `af65165` author `2026-10-25T12:52:54-03:00` (= base `8841ad3`'s author date), committer
  `2026-10-25T19:50:10-03:00`; lands `0316b88` committer `20:00:54`; fleet report commit `dad39efd`
  committer `20:43:14`.
- Fleet repo: `/home/vgpnk/Projects/shokunin` is a git repo; it tracks 0 lane files; the only freeze
  mention is the 7-hex `af65165`; `git grep` for the full 40-hex under `.ufo` → no hits.
- Fixtures/log: `/tmp/CritFrozenCfg/{build.py,build_rev.py,acceptc.tmpl,acceptc2.py,pincheck.py,run.log,rev.log,stdout.log,rev-stdout.log,offmain.log}`;
  twelve repos under `/tmp/CritFrozenCfg/fx/` (commits quoted in §2/§5). Notable lands hashes:
  legit `86dcbe79…`, claims-edit `3de93cf7…` (edit `0c687817…`), merge-first-parent `592b3739…`
  (freeze `ba1b5215…`), replace lands `569c01ee…` (orphan `0e81e7c1…`, replace ref
  `refs/replace/569c01eeac4f3a6f1ad2e9ad4fcd8d29c8ab41bb f5e5f05c…`); revision fixtures freeze
  `f9bcc3e4…`, lands `a2ff4fc5…` (disclosed) and `5b8d0c96…` (undisclosed).

## 9. Honesty

- Every verdict above is one of my own runs, quoted from `/tmp/CritFrozenCfg/run.log`; nothing was
  inferred from round-73's reports where a run was possible.
- The model counters are not the round's counters; the attack is against the *rule* and the leg text,
  and the leg counts (3/3, 4/4) are the model's.
- I did not run the fleet census or any campaign tool against `/home/vgpnk/Projects/shokuknow`; the
  lane was read with `git` and one read-only invocation of `reports/round-73/accept-c.py` (which writes
  only `/tmp`).
- The counter-revision door was exercised both ways (disclosed row PASS, missing row FAIL); the
  freeze-byte re-run against a revised lands also PASSES when the row is present.
- I did not test: GitHub push-event evidence, a `--freeze` that is a valid commit of a *different*
  repository, symlinked `claims.json` (a mode check is proposed in §4.2.6; only the regular-file case
  was exercised), or the real round-74 counters (they do not exist yet).
