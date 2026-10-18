# Round 19 — Scope watch, second seat (auditor R19-A20)

- **Seat:** R19-A20 (auditor, SCOPE — the second of the two scope seats,
  R19-A19..A20). **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **Date:** 2026-10-18, local clock UTC-03:00. Observation window
  **08:33:20–08:34:30 -03:00** (11:33–11:34Z).
- **Role limits:** this seat executes and measures; it decides no admission,
  promotes no claim, and certifies no canon or source content. Its only write
  is this file. Scratch under `.scratch/r19-a20/` with `TMPDIR=$PWD/.scratch`
  exported. No git mutation, no commit, no push, no write outside the lane
  repo, no filed-round byte of rounds 8–18 touched, no historical validator
  executed.
- **Independence from R19-A19:** this seat re-derives the same three
  conclusions with a *different* measurement path — a per-round git `ls-tree`
  digest at the baseline revision instead of A19's whole-surface `sha256sum`,
  and a fresh post-A19 status snapshot — rather than re-reading A19's file.
- **Revision binding:** lane `HEAD = 169c616613899f7ba86b8fb58ed808bdfd4b5ccd`
  (round-19 declare, 08:30:39 -03:00); `HEAD^ = e5718945a1ab0a0c3db955338d2cae77d68fd348`
  = declared `baseline_revision` (round-18 admit, 08:29:20 -03:00). Fleet root
  HEAD `a2f0d3432f05686fedc9c84da3ca975b20257ee1`.

## 0. Verdict

**IN SCOPE AND CLEAN.** Fleet root clean; the filed surface of rounds 8–18 is
untouched (all 821 tracked filed paths git-object-identical to the baseline
revision, verified per-round); `PROVINCE.md` is accurate and byte-unchanged
since the baseline. One recurring out-of-lane finding (F-A20-1) and one
in-flight observation (N1) below.

## 1. Fleet root clean (independent re-check)

`git -C /home/vgpnk/Projects/shokunin status --porcelain=v1` → **empty**
(0 lines) at 08:33:54 -03:00. Fleet root `.gitignore` line 1 `*-shokunin/`
ignores every lane repository (`git check-ignore -v kotodama-shokunin` →
`.gitignore:1:*-shokunin/`); `.ufo/waves/*/*-scratch/` is ignored (line 3);
`.tower/` is excluded via `.git/info/exclude`. Fleet HEAD is the round-18
close `a2f0d34`, committed 08:29:58 -03:00, before this round's declaration.
No fleet-root commit postdates it.

## 2. Filed rounds 8–18 untouched (per-round re-derivation)

**Tracked filed surface:** `git ls-files reports/round-{8..18}` → **821
paths**. Per-round tracked counts and a per-round `ls-tree` digest at the
baseline revision (command: `git ls-tree -r e571894 -- reports/round-N |
sha256sum`; 2026-10-18):

| round | tracked files | baseline `ls-tree` digest (16 hex) |
|---|---|---|
| 8 | 153 | `045b06cc6825f668` |
| 9 | 87 | `653bb8c4d13b1703` |
| 10 | 73 | `c4fe57c798258e13` |
| 11 | 252 | `bee64f7d51aa9397` |
| 12 | 44 | `a3f3659620d7291d` |
| 13 | 2 | `bab7d795ecbc9c62` |
| 14 | 40 | `ee44819da25f67c4` |
| 15 | 20 | `60ab6cb343ac2a05` |
| 16 | 23 | `276a81d7fb54ef50` |
| 17 | 67 | `99f4cf3ccf3863dd` |
| 18 | 60 | `14920b529336f720` |

**Identity of the working tree against the baseline objects.** For each of the
821 tracked filed paths, `git rev-parse e571894:<p>` equals `git hash-object
<p>` — **821 match, 0 mismatch, 0 not-in-baseline** (R19-A19 ran the same
per-path comparison; this seat re-derived it as the primary path and reports
the identical result). Equivalently, `git diff --name-status e571894 169c616`
returns exactly two rows, both additions under `reports/round-19/`
(`claims.json`, `targets.json`) — nothing under rounds 8–18.

**No filed byte written after the baseline commit.** `find reports/round-{8..18}
-type f -newermt "2026-10-18 08:29:20"` → empty: no file in the filed surface
carries an mtime at or after the round-18 admit commit. (The in-flight wave is
writing *new* round-19 and tooling artifacts, not filed rounds — see N1.)

**Composition note.** Non-`__pycache__` on-disk files under rounds 8–18 number
826; 821 are tracked and 5 are git-ignored run logs
(`reports/round-9/baselines/{naming-collision-gate,myth-consistency-gate,handoff-packet-check}/run.log`,
`reports/round-11/handoff/{run.log,tamper-control.log}`; `.gitignore` `*.log`).
Ignored files have no git baseline, so they are reported as observed-only, not
as "byte-stable". 10 ignored `__pycache__/*.pyc` files are likewise excluded.

**Independent cross-round reference.** `reports/round-18/validation.json`
`input_sha256` carries 89 rows under rounds 8–18 (89/89 match on disk) and
`filed_rounds.baseline.files` carries 761 rows (761/761 match, 0 mismatch,
`changed_during_validation` empty). Re-derived here, not trusted from A19.

## 3. PROVINCE accurate (independent re-check)

`PROVINCE.md` sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`;
git blob `313b182f251564b7997b06996b4f063370778f11`; byte-identical at baseline
and HEAD (`git diff e571894 169c616 -- PROVINCE.md` empty). Surface checks:

- Six owned partitions exist exactly: `corpus/knowledge/` →
  linguistics (19 `.md`), myth-symbol (19), culture-material (18),
  synthesis (24), verification (15), civilizations (94).
- Gates present: 10 scripts under `tools/gates/` (7 structural + the two D4
  gates + `typed-pipeline-gate.py`) — matches "this lane's own gates".
- Adjacent contract `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  present (28421 bytes).
- Refuses clause upheld: `grep -rin 'is canon\|canonical truth\|declared canon'
  corpus examples` returns only refusals/handoffs ("no claim here is canon",
  "which is canon → lore-shokunin"), never a canon claim; no `world-bible/`
  directory exists in the lane.
- Refused domains are real sibling lanes and none is absorbed here: lore,
  chousa, kake, kotoba, game-dev-2d, game-dev-3d all exist as siblings.
- "Only writes this standalone lane repository": of 1528 tracked files, no
  path lies outside the lane; the only non-partition entries are lane-root
  metadata (`AGENTS.md`, `LOG.md`, `MINT.md`, `PROVINCE.md`, `README.md`,
  `SCORECARD.md`, `SHONEN.md`, `SKILL.md`, `.gitignore`).

**Limit:** the negative "siblings … remain read-only" cannot be falsified from
inside the lane; this seat found no evidence of an out-of-lane write and notes
the limit rather than claiming the negative proven.

## 4. Commands (all run 2026-10-18, ~08:33–08:34 -03:00, `TMPDIR=$PWD/.scratch`)

- `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1` → 0; fleet
  `git log -1`.
- `git ls-files reports/round-{8..18} | wc -l` → 821; per round,
  `git ls-tree -r e571894 -- reports/round-N | sha256sum`.
- per-path `git rev-parse e571894:<p>` vs `git hash-object <p>` → 821/0/0.
- `git diff --name-status e571894 169c616` → 2 additions, both `reports/round-19/*`.
- `find reports/round-{8..18} -type f -newermt "2026-10-18 08:29:20"` → empty.
- `sha256sum PROVINCE.md`; `git diff e571894 169c616 -- PROVINCE.md` → empty.
- `ls corpus/knowledge/`; per-partition `ls …/*.md | wc -l`; `ls tools/gates/*.py`;
  `ls corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git ls-files | wc -l`; `grep -rin 'is canon\|canonical truth\|declared canon'`;
  `[ -d ../<sibling> ]` for the six refused domains.
- `python3 -` recheck of `reports/round-18/validation.json` `input_sha256`
  (89) and `filed_rounds.baseline.files` (761) vs on-disk sha256.

## 5. Findings

- **F-A20-1 (out-of-lane, informational):** `lore-shokunin` is dirty (2 lines)
  — the recurring r16/r17/r18 class. Left untouched; lore's own scope.
- **N1 (in-flight wave, no action):** at 08:33:54 the lane worktree showed 10
  porcelain entries, all *new* round-19 activity, none in the filed surface:
  `M tools/check-gate-battery.py` (claim-O battery work),
  `?? corpus/knowledge/verification/label-channel-routing-verification.md`
  (claim-C work), `?? reports/round-19/{audit/,availability.json,entries/,gaps.md,knowledge/,scope.md}`,
  `?? tools/gates/expected/{d4-assembly-check-gate/,d4-typed-labels-check-gate/}`
  (claim-O baselines). These are the running wave's outputs; they do not touch
  rounds 8–18 and do not affect §2. This file's §2 verdict binds the filed
  surface and the declaration commit `169c616` only.

## 6. Compliance self-attestation

This seat wrote only `reports/round-19/scope-a20.md`, plus scratch under
`.scratch/r19-a20/` (`TMPDIR=$PWD/.scratch`). No git mutation, no commit, no
push, no write outside the lane repo, no filed-round bytes of rounds 8–18
touched, no historical validator executed. Out-of-province observations routed
in §5, never absorbed.
