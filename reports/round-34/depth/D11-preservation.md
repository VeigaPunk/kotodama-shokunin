- Seat: D11 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D11 — Byte-preservation proof for claim D (filed-round immutability)

## Method

Read-only git evidence at HEAD `da68a6d705e41f369f21e8607bfaab5b54077f84`
(`git rev-parse HEAD`, `git log -1`) plus an independent on-disk witness set:
per-file `git hash-object` comparison against the committed blob, `freeze.txt`
digest re-computation, a whole-set content fingerprint, and an mtime scan of
every filed-round file against the baseline commit time.

Commands were run with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
in `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. No filed-round file was
written, opened for write, or executed by this seat. Per shared rule
(F-C13-1), no `reports/round-*/run-validation.py` was executed in-tree.

## Correction to the mission's path shorthand (material)

The mission says "over `reports/round-{2,4,5,6}/handoff`". Those paths do not
exist, and rounds 2 and 4 have no report directory at all — neither on disk
nor in the HEAD tree:

```
$ for p in reports/round-2/handoff reports/round-4/handoff reports/round-5/handoff reports/round-6/handoff; do printf '%s -> ' "$p"; test -e "$p" && echo EXISTS || echo ABSENT; done
reports/round-2/handoff -> ABSENT
reports/round-4/handoff -> ABSENT
reports/round-5/handoff -> ABSENT
reports/round-6/handoff -> ABSENT

$ ls -d reports/round-* | tr '\n' ' '
reports/round-10 ... reports/round-34 reports/round-5 reports/round-6 reports/round-7 reports/round-8 reports/round-9

$ git ls-tree --name-only HEAD reports/ | grep -E '^reports/round-[0-9]+$' | tr '\n' ' '
reports/round-10 ... reports/round-33 reports/round-5 reports/round-6 reports/round-7 reports/round-8 reports/round-9
```

The filed packet revisions `declared-in-r2/r3/r4/r5/r6` are homed under rounds
22/23/25/26/30 (this is what claims.json's shorthand "r2/r4/r5/r6" refers to):

```
$ git ls-files 'reports/**/declared-in-*' | sed 's#/[^/]*$##' | sort -u
reports/round-22/handoff/declared-in-r2
reports/round-23/wording/declared-in-r3
reports/round-25/v3-supersession/declared-in-r4
reports/round-26/handoff/declared-in-r5
reports/round-30/handoff/declared-in-r6
```

So the preservation set used here is the union: every tracked file of
`reports/round-5..33` (1909 files), which is a superset of both the mission's
`round-8..33` and the five revision homes. Any validator or prose that repeats
the shorthand `reports/round-{2,4,5,6}/handoff` should use these corrected
paths (see `## Owed`).

## Evidence A — tree-level cleanliness vs baseline

```
$ git diff-index --quiet HEAD; echo "EXIT=$?"
EXIT=0

$ git diff --cached --name-only HEAD | wc -l     # index vs HEAD
0

$ git diff --name-only | wc -l                   # worktree vs index
0

$ git diff --summary HEAD -- reports/ | wc -l    # mode/type changes
0

$ git diff --name-only HEAD | wc -l              # whole tree vs HEAD
0

$ git status --porcelain
?? reports/round-34/
```

One untracked path only: this round's own in-flight directory
`reports/round-34/` (which contains `claims.json`, `targets.json`,
`telemetry/`, and the seat fragments). Zero tracked bytes differ anywhere in
the tree, let alone in filed rounds.

## Evidence B — per-round changed-row table (worktree vs HEAD)

```
$ for i in 5 6 7 8 9 $(seq 10 33); do n=$(git diff --name-only HEAD -- "reports/round-$i" | wc -l); printf '%-12s %s\n' "round-$i" "$n"; done
round-5 0   round-6 0   round-7 0   round-8 0   round-9 0   round-10 0
round-11 0  round-12 0  round-13 0  round-14 0  round-15 0  round-16 0
round-17 0  round-18 0  round-19 0  round-20 0  round-21 0  round-22 0
round-23 0  round-24 0  round-25 0  round-26 0  round-27 0  round-28 0
round-29 0  round-30 0  round-31 0  round-32 0  round-33 0
```

29/29 rows = 0. The five revision homes independently:

```
$ for d in reports/round-22 reports/round-23 reports/round-25 reports/round-26 reports/round-30; do printf '%-22s rows=%s\n' "$d" "$(git status --porcelain -- "$d" | grep -c .)"; done
reports/round-22       rows=0
reports/round-23       rows=0
reports/round-25       rows=0
reports/round-26       rows=0
reports/round-30       rows=0
```

## Evidence C — blob-identity census (1909/1909)

Per-file comparison of each tracked filed-round file's on-disk bytes against
its committed blob hash (catches any content change even if the index were
somehow staged-silent):

```
$ python3 - <<'PY'   # full script in the run; compares git hash-object vs git ls-files -s blob
...
PY
compared=1909 mismatches=0
```

1909 tracked files under `reports/round-5..33` — the census equals
`git ls-files 'reports/round-*' | wc -l` = 1909 at baseline, 0 mismatches.

## Evidence D — freeze-digest re-computation at HEAD

On-disk sha256 vs the `packet_sha256` / `twin_sha256` lines declared in each
revision's own `freeze.txt` (filed bytes, unedited):

| revision | path | freeze.txt packet_sha256 | on-disk packet.md | twin.json |
|---|---|---|---|---|
| declared-in-r2 | reports/round-22/handoff/declared-in-r2 | a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e | match | d3de56a8be1d28fdcead751aa0ac9364f7b43ff2b8bad71b696f0b57955b4d5c = twin_sha256 |
| declared-in-r3 | reports/round-23/wording/declared-in-r3 | 084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250 | match | (no twin.json filed — validator-facing supersession per its freeze.txt) |
| declared-in-r4 | reports/round-25/v3-supersession/declared-in-r4 | 5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03 | match | (no twin.json filed — validator-facing supersession per its freeze.txt) |
| declared-in-r5 | reports/round-26/handoff/declared-in-r5 | e3fb1ca500d62981b59129f898ef7e4b2843b1fa5ab7d12e8fc16818d1f764b8 | match | b849e2f9c919320f17166c54b53492d6be3da26d0a2184466ab81a26018f6f13 = twin_sha256 |
| declared-in-r6 | reports/round-30/handoff/declared-in-r6 | 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb | match | 6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e = twin_sha256 |

`r5`/`r6` freeze.txt also carry a `re-frozen packet_sha256:` line
(69ce3877… → e3fb1ca5… and ec30b11f… → 6ced88ad…) that agrees with the
on-disk value, so the frozen predecessor chain is intact too.

Measured `expected.json` digests (not declared in freeze.txt; recorded here so
the re-pin cascade leaves them provably untouched):

```
4879e7602efcbc57f134b0e1604d38ca54d837bcbf8407d1667ef9bf30e238b7  reports/round-22/handoff/declared-in-r2/expected.json
737e54842fffa68d07f2e05370e5618a85fd50e4d9be639429ea14a0e75f01ff  reports/round-23/wording/declared-in-r3/expected.json
c2d4eb7af2b9807afa9cae4720448144bcefa4bb0c678500bf8d6c41c660b093  reports/round-25/v3-supersession/declared-in-r4/expected.json
855603f66ca125d027e3d1629a236209ae58eb05c9d31000e826981b42650de1  reports/round-26/handoff/declared-in-r5/expected.json
ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0  reports/round-30/handoff/declared-in-r6/expected.json
```

## Evidence E — whole-set content fingerprint (durable witness)

A single value any later seat can recompute without trusting this fragment's
narrative:

```
$ git ls-files 'reports/round-5' ... up to 'reports/round-33' > /tmp/d11-files.txt
$ wc -l < /tmp/d11-files.txt
1909
$ xargs -a /tmp/d11-files.txt sha256sum | LC_ALL=C sort > /tmp/d11-sums.txt
$ sha256sum /tmp/d11-sums.txt
1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71  /tmp/d11-sums.txt
```

`listing_sha256 = 1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71`
(sha256 of the `LC_ALL=C`-sorted `sha256sum` listing of all 1909 tracked files).
Reproduce with:

```
git ls-files $(for i in 5 6 7 $(seq 8 33); do echo reports/round-$i; done) \
  | xargs sha256sum | LC_ALL=C sort | sha256sum
```

## Evidence F — mtime witness (no post-commit writes)

```
$ git log -1 --format=%cI HEAD
2026-10-19T03:52:53-03:00

$ find reports/round-5 ... reports/round-33 -type f -newermt "2026-10-19T03:52:53-03:00" | wc -l
0
```

Zero filed-round file has a modification time after the baseline commit —
independent confirmation (beyond git) that nothing in a filed round was
written during this round's dispatch window.

## Verdict (this seat, pre-build instant)

`0 rows expected` → **observed 0 rows**. Filed-round immutability holds for
claim D as of this seat's execution: whole tree byte-clean vs `da68a6d`
(Evidence A), 29/29 filed rounds 0 changed rows (Evidence B), 1909/1909 blob
identities (Evidence C), all five filed revision freeze digests re-computed and
matching (Evidence D), set fingerprint `1713e725…` (Evidence E), zero
post-commit mtimes (Evidence F). The only untracked path is
`reports/round-34/` itself, so claim D's builders cannot have touched filed
bytes at this instant.

Limit of this proof: it is a snapshot at the pre-build instant. The
post-build re-run (after the integrator lands `declared-in-r7`, moves
`tools/exercise-handoff-e2e.py:1933-1934`, and lands the O/C artifacts) is
owed — see below.

## Dependency check

The D-block fragments named by neighboring seats (D01–D10, K01/K02, P01) did
not exist when this seat read the round directory:

```
$ find reports/round-34 -type f | sort
reports/round-34/claims.json
reports/round-34/targets.json
reports/round-34/telemetry/dispatch-declared.json
```

No dependency was required for this seat's mission, so the missing-fragment
rule did not block any part of the work.

## Closing re-check (after this seat's own write)

Re-run immediately after this seat wrote its own fragment (the write is the
only act this seat performs, and it lands under `reports/round-34/`, not in a
filed round):

```
$ git diff-index --quiet HEAD; echo "EXIT=$?"
EXIT=0
$ git diff --name-only HEAD | wc -l
0

$ git status --porcelain | grep '^??'
?? reports/round-34/

$ git diff --name-only HEAD -- reports/round-5 ... reports/round-33 | wc -l
0

$ git ls-files <round-5..33> | xargs sha256sum | LC_ALL=C sort | sha256sum
1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71  -

$ find reports/round-34 -type f | sort
reports/round-34/claims.json
reports/round-34/depth/D11-preservation.md
reports/round-34/targets.json
reports/round-34/telemetry/dispatch-declared.json
```

The fingerprint is **identical before and after** this seat's write
(`1713e725…` = `1713e725…`), and the aggregate filed-round change count is
still 0. This seat's write added exactly one path, under `reports/round-34/`.

Note: this fragment's own digest changes with this closing edit, so it is not
a fixed point — measured at the pre-closing version:
`b6ba30c9f8d4aafb78c30a11ea3c63712ceb818d5668b47b55fa319ccd2127e9`. The
integrator should pin the final `D11-preservation.md` digest in the round
manifest rather than this fragment pinning itself.

## Owed

1. `reports/round-34/depth/D20-verify-preservation.md` — D20's independent
   re-run of Evidence A–F with its own git commands, and its check that the
   D05 draft carries none of the six stale figures. Not filed when this seat
   read the round directory (`find reports/round-34 -type f` returned only
   `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`), so the
   verification of *these* numbers by a second seat is owed.
2. **Post-build re-run of Evidence A/E/F by the integrator.** This fragment is
   a pre-build snapshot: at the instant of measurement nothing from claim D
   had landed. After the integrator writes `reports/round-34/handoff/declared-in-r7/*`,
   moves `tools/exercise-handoff-e2e.py:1933-1934`, and lands the O/C
   artifacts, the same four commands must be re-run and the fingerprint must
   still read `1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71`.
   The close-time proof belongs in the round's own validation leg, not here.
3. **Path-shorthand correction upstream.** `reports/round-34/claims.json:30`
   (`after_required`) and any S04 validation-leg text that repeats
   "r2/r4/r5/r6 packet bytes" should carry the corrected homes
   (round-22/r2, round-23/r3, round-25/r4, round-26/r5, round-30/r6) so the
   close-time preservation leg enumerates real paths. `claims.json` is this
   round's filed declaration; this seat did not edit it — the integrator
   decides whether to record the correction as an errata row in the round
   report or in the validator leg.
4. `reports/round-34/handoff/declared-in-r7/freeze.txt` — not yet existing;
   the new revision's own freeze receipt is what the close-time re-run in
   item 2 must verify alongside the five filed predecessors.

## Citations

Contract / declaration (read-only):

- `REGIMEN.md:25-53` — per-round contract (land, measure, judge; never edit
  filed bytes; F-C13-1 prevention).
- `reports/round-34/claims.json:21-37` — claim D before/after and counting
  commands; `:26` renderer-default pin at `tools/exercise-handoff-e2e.py:1933-1934`;
  `:30` `after_required` ("filed rounds 8-33 and r2/r4/r5/r6 packet bytes
  untouched"); `:68-74` non_goals.
- `reports/round-34/targets.json:5-11` — binding shared rules; `:33` this
  seat's row (mission + `out: depth/D11-preservation.md`).
- `reports/round-34/telemetry/dispatch-declared.json` — dispatch declaration
  (present at read time; not modified by this seat).

Filed revision bytes (read-only, verified, never written):

- `reports/round-22/handoff/declared-in-r2/freeze.txt:1-3` (packet/twin
  digests) and `packet.md`, `twin.json`, `expected.json`, `run.log`.
- `reports/round-23/wording/declared-in-r3/freeze.txt:1-6`, `packet.md`,
  `expected.json`.
- `reports/round-25/v3-supersession/declared-in-r4/freeze.txt:1-4,18`,
  `packet.md`, `expected.json`.
- `reports/round-26/handoff/declared-in-r5/freeze.txt:1-3,8`, `packet.md`,
  `twin.json`, `expected.json`, `run.log`.
- `reports/round-30/handoff/declared-in-r6/freeze.txt:1-3,8`, `packet.md`,
  `twin.json`, `expected.json`, `run.log`.

Commands relied on (all read-only; run from the repo root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`.
- `git log -1 --format='%H %cI' HEAD` → commit time `2026-10-19T03:52:53-03:00`.
- `git diff-index --quiet HEAD` → EXIT=0; `git diff --cached --name-only HEAD`
  → 0; `git diff --name-only` → 0; `git diff --summary HEAD -- reports/` → 0;
  `git diff --name-only HEAD` → 0; `git status --porcelain` →
  `?? reports/round-34/` only.
- Per-round loop: `git diff --name-only HEAD -- reports/round-<N>` for
  N ∈ {5..33} → 0 rows for all 29 rounds.
- `git status --porcelain -- reports/round-{22,23,25,26,30}` → 0 rows each.
- `git ls-files 'reports/round-*' | wc -l` → 1909; per-file
  `git hash-object` vs `git ls-files -s` blob → `compared=1909 mismatches=0`.
- `sha256sum` on each revision's `packet.md`/`twin.json`/`expected.json` →
  values in Evidence D.
- `git ls-files <round-5..33> | xargs sha256sum | LC_ALL=C sort | sha256sum`
  → `1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71`
  (identical before and after this seat's write).
- `find reports/round-5 ... reports/round-33 -type f -newermt
  "2026-10-19T03:52:53-03:00" | wc -l` → 0.
- `ls -d reports/round-*`, `git ls-tree --name-only HEAD reports/`,
  `test -e reports/round-{2,4,5,6}/handoff` → ABSENT (path correction),
  `git ls-files 'reports/**/declared-in-*'` → the five real homes.
- `find reports/round-34 -type f` → the four pre-existing paths (dependency
  check + closing re-check).
- `cat .gitignore` → `.scratch/` and `*.log` ignored; no scratch noise can
  reach filed rounds.

Not executed (F-C13-1 prevention): no `reports/round-*/run-validation.py`, no
gate runner, no in-tree round runner was run by this seat.
