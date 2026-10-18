# R19-D10 — round-19 fragment ledger (read-time census of `reports/round-19/**`)

- round: 19 (operator: loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  provider `hyper/deepseek-v4.1-flash` per the operator substitution). Lane:
  `kotodama-shokunin`.
- seat **R19-D10** (fragment ledger). Date 2026-10-18 (stamps UTC). Baseline
  revision `e5718945a1ab0a0c3db955338d2cae77d68fd348` (round-18 admit); declare
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd`.
- canon: **NON-CANON integration ledger.** It admits nothing, certifies no round,
  and edits no byte outside `reports/round-19/integration/`.
- writes: this file, `reports/round-19/integration/fragment-ledger.json`, plus
  gitignored scratch under `.scratch/`. No commit, no push.

## 0. What this ledger is

A **read-time census** of every file under `reports/round-19/` at
**2026-10-18T11:38:51Z**, with per-file byte size, sha256, mtime and the seat that
appears to own it. It is the index the parent uses to integrate the wave's
fragments into `LOG.md` / `SCORECARD.md`. It is **not** a completeness claim and
**not** a round verdict: the wave was still writing at the census (39 files, up
from 2 at the 11:32:27Z opening census, 16 at 11:34:26Z, 25 at 11:35:51Z), and the
worktree was dirty throughout. Re-run on the settled tree:

```sh
find reports/round-19 -type f | sort
# regenerate fragment-ledger.json with the same per-file shape (path, bytes,
# sha256, mtime_utc, owner_seat) plus baseline_revision / declare_revision /
# census_utc / fragment_count.
```

The machine-readable twin is `reports/round-19/integration/fragment-ledger.json`
(same rows, plus the `collision_record` block described in §3).

## 1. Census (2026-10-18T11:38:51Z, 39 files)

| path | bytes | sha256 (12) | mtime UTC | owner seat |
|---|---:|---|---|---|
| `__pycache__/run-validation.cpython-314.pyc` | 81476 | `89a43e1ec4b5` | 11:38:08 | build artifact (the runner has been executed) |
| `audit/coverage-audit.py` | 6194 | `56f764845334` | 11:32:37 | auditors |
| `audit/entry-audit.py` | 8398 | `2e2ed99da9e2` | 11:37:27 | auditors |
| `audit/lessons-audit.py` | 4998 | `ca2e6ead86e5` | 11:33:56 | auditors |
| `audit/receipt-coverage.json` | 2244 | `dec7c0e1f20e` | 11:35:18 | auditors |
| `audit/receipt-entries-3.json` | 2588 | `9c154a85c29d` | 11:35:26 | auditors |
| `audit/receipt-entries-new.json` | 7139 | `2326c171c624` | 11:37:48 | auditors |
| `audit/receipt-lessons.json` | 10620 | `06dde2707036` | 11:35:18 | auditors |
| `audit/x26-spotcheck-entries.md` | 8482 | `fab218621e76` | 11:38:30 | auditors |
| `audit/x27-coverage-readme-vs-files.md` | 5782 | `9a2e1c1115c9` | 11:37:45 | auditors |
| `audit/x28-lessons-audit.md` | 7082 | `54efe80a2daf` | 11:37:02 | auditors |
| `availability.json` | 6286 | `8c1d2632c488` | 11:38:07 | dependency/availability seat |
| `claims.json` | 2358 | `b9a964c136b2` | 11:30:39 | declaration (parent) |
| `entries/R19-C11.md` | 2668 | `e6e596686a0c` | 11:33:09 | C-authors |
| `entries/R19-C12.md` | 2333 | `553cf97d8ec5` | 11:33:40 | C-authors |
| `entries/R19-C13.md` | 2778 | `1683500dd2ee` | 11:34:09 | C-authors |
| `entries/R19-C14.md` | 2127 | `85146c4f3dd7` | 11:35:04 | C-authors |
| `entries/R19-C15.md` | 2132 | `775a93be25ac` | 11:35:36 | C-authors |
| `entries/R19-C16.md` | 1863 | `d0b125407520` | 11:36:06 | C-authors |
| `entries/R19-C17.md` | 1990 | `3bab42b828b7` | 11:36:29 | C-authors |
| `entries/R19-C18.md` | 1855 | `6fac3637d662` | 11:36:51 | C-authors |
| `entries/R19-C19.md` | 2181 | `88bfd58f9989` | 11:37:18 | C-authors |
| `entries/R19-C20.md` | 1801 | `47adb4bc9dfb` | 11:37:47 | C-authors |
| `gaps.md` | 4170 | `22b653712804` | 11:33:09 | C-author gap registry |
| `integration/d4-lessons-entry.md` | 13670 | `6ed6b4083a37` | 11:37:52 | **R19-D08 (this seat)** |
| `integration/fragment-ledger.json` | 6549 | `5f128472c564` | 11:35:58 | **R19-D10 (this seat)** |
| `integration/fragment-ledger.md` | 6272 | `2c658997976e` | 11:36:12 | **R19-D10 (this seat)** |
| `integration/log-fragment.md` | 11470 | `c9e59278d3f5` | 11:38:29 | **R19-D09 (this seat)** |
| `integration/scorecard-fragment.md` | 5804 | `c90ccb7d40e1` | 11:38:45 | **R19-D09 (this seat)** |
| `knowledge/analyst-1.md` | 9711 | `017b86a332a6` | 11:33:19 | D-knowledge |
| `knowledge/analyst-2.md` | 8865 | `54b220c24420` | 11:34:36 | D-knowledge |
| `knowledge/analyst-3.md` | 11129 | `be359a9722d9` | 11:34:15 | D-knowledge |
| `knowledge/review-1.md` | 13893 | `ec19967145a2` | 11:37:57 | D-knowledge |
| `knowledge/skill-draft-a.md` | 16062 | `d6a85e7ac79e` | 11:34:58 | D-knowledge (R19-D04) |
| `knowledge/skill-draft-b.md` | 19700 | `f27cf184e66b` | 11:34:42 | D-knowledge (R19-D05) |
| `run-validation.py` | 58214 | `4da558975e1a` | 11:38:32 | runner owner |
| `scope-a20.md` | 8513 | `38ea4e5399a5` | 11:34:13 | scope watcher (X) |
| `scope.md` | 12025 | `400bf3c25e48` | 11:33:49 | scope watcher (X) |
| `targets.json` | 249 | `52d43bf2a3b0` | 11:30:39 | declaration (parent) |

**Self-reference caveat:** the ledger's own two rows
(`integration/fragment-ledger.{md,json}`) show the revision immediately
*preceding* this census's own write — re-hash them rather than inheriting those
values. The md was written after the census (digest `2c658997976e` is the prior
revision); the json's current digest is whatever `sha256sum` reports now.

Two notes the parent needs: the `__pycache__/run-validation.cpython-314.pyc`
entry means **the runner has been executed** (a `validation.json` may exist by the
time this is read; it did not at 11:38:51Z), and `run-validation.py` itself moved
(`f63562f2…` at 11:35:56Z → `4da558975e1a` at 11:38:32Z), so the runner was being
edited while it was being run.

## 2. Fragments landing outside `reports/round-19/` (same census window)

The round's deliverables are not all under `reports/round-19/`. Observed with
`git status --porcelain` at 11:37Z, each owned by its seat and **not** written by
this one:

| path | owner seat | claim |
|---|---|---|
| `corpus/lessons/round-19.md` | **X21** (survey; see §3) | D |
| `corpus/knowledge/verification/label-channel-routing-verification.md` | C-author (R19-C11) | C |
| `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md` | C-author (R19-C12) | C |
| `corpus/knowledge/verification/generated-artifact-roundtrip-verification.md` | C-author (R19-C13) | C |
| `corpus/knowledge/verification/gate-battery-surface-verification.md` | C-author (R19-C14) | C |
| `corpus/knowledge/verification/two-reader-interop-agreement.md` | C-author (R19-C15) | C |
| `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` | O-baselines seat | O |
| `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` | O-baselines seat | O |
| `tools/check-gate-battery.py` (**modified**) | O-battery seat | O |

Partition counters (read-only): verification **15 → 20**, synthesis **24 → 28**,
civilizations 94 (unchanged), at 11:37:21Z. The C claim requires >=8 new sourced
entries across verification + synthesis (>=3 each); the observed net is +9, so the
count looks met but must be re-measured on the settled tree. `corpus/README.md`
still read `revision: 1.3` / "Total knowledge entries: 189" at 11:37Z (digest
`9df4b7c5…`), so the README reconciliation lags its content.

## 3. Collision record — `corpus/lessons/round-19.md`

This seat (R19-D08) and peer seat **X21** were both assigned
`corpus/lessons/round-19.md`. X21's gate-keeper survey landed there (~11:33Z;
digest `df4de597…` at 11:37Z) and **superseded this seat's 20 260-byte draft** of
that file (verified: the draft's distinctive strings are absent from the current
file). This seat did **not** re-write the path — a second write would race X21 and
destroy its survey. Consequences recorded for the parent:

- The D4 craft lesson entry is preserved at
  `reports/round-19/integration/d4-lessons-entry.md` (this seat).
- X21's own survey records the collision and states the D claim's lesson entry
  "must land as a **different** path or name its owner".
- Claim D's "corpus/lessons gains the D4 lesson entry" is therefore **unresolved at
  a settled path** until the parent picks one (`corpus/lessons/round-19-d4.md`, a
  merge into X21's survey, or a drop).

## 4. Dependency watch

This seat ran a read-only watcher over `reports/round-19/**` (20 ticks, sixty
seconds apart, from 2026-10-18T11:33Z) so late-landing fragments are captured
rather than assumed absent. The census above is the authoritative snapshot; a later
re-scan supersedes it. Nothing in this ledger is inherited by a later read
(round-15 lesson).

## 5. Limits

- The census is a snapshot of a live wave; the file count grew 2 → 16 → 25 → 39 in
  six minutes. Counts here are evidence of movement, never a completeness score.
- `owner_seat` is an inference from path conventions and file headers, not an
  authority statement; the parent confirms ownership at integration.
- No canon, rights, clearance or freshness ruling is made or absorbed. The
  freshness axis-move pause stands; the two round-11 ratios remain separate and
  un-reopened.
