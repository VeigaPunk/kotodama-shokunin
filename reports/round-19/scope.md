# Round 19 — Scope watch (auditor R19-A19)

- **Seat:** R19-A19 (auditor, SCOPE). **Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  **Date:** 2026-10-18, local clock UTC-03:00. Observation window
  **08:31:00–08:34:00 -03:00** (11:31–11:34Z), with the closing re-check
  recorded in §6.
- **Role limits:** this seat executes and measures; it decides no admission,
  promotes no claim, and certifies no canon or source content. Its only write
  is this file (and its sibling `scope-a20.md`); scratch snapshots under
  `.scratch/r19-a19/` with `TMPDIR=$PWD/.scratch` exported. No git mutation,
  no commit, no push, no write outside the lane repo, no filed-round byte of
  rounds 8–18 touched, no historical validator executed.
- **Regimen / state:** operator loop 2 of 3, build round 3 of 4 — one 64-worker
  batch on `hyper/deepseek-v4.1-flash` (operator provider substitution),
  per `reports/round-19/claims.json` (`state: declared-before-dispatch`).
- **Revision binding:** lane `HEAD = 169c616613899f7ba86b8fb58ed808bdfd4b5ccd`
  ("round-19: declare claims D/C/O", 2026-10-18T08:30:39-03:00), and
  `HEAD^ = e5718945a1ab0a0c3db955338d2cae77d68fd348` = the declared
  `baseline_revision` (round-18 admit, 08:29:20-03:00). The declare commit is
  the baseline's direct child, so the graded artifact tree below is identical
  at the declared revision and at HEAD.
- **Question this file answers (assignment, verbatim):** "AUDIT R19-A19..A20
  (SCOPE x2): fleet root clean; filed rounds 8-18 untouched; PROVINCE accurate."

## 0. Verdict

**IN SCOPE AND CLEAN, with one recurring out-of-lane informational finding
(F-A19-1) and two observational notes (N1–N2).** The fleet root worktree is
clean; the filed surface of rounds 8–18 is byte-stable — all 821 tracked files
under `reports/round-8 … reports/round-18` are git-object-identical to the
declared baseline revision, and the round-19 declaration commit touched exactly
two paths, both under `reports/round-19/`; `PROVINCE.md` is accurate against
the repository surface and unchanged since the baseline. Nothing was absorbed,
nothing was repaired in place, no sibling or out-of-lane byte was written.

## 1. Fleet root clean

`git -C /home/vgpnk/Projects/shokunin status --porcelain=v1` → **empty** (0
lines), sampled at 08:32:00 and again at 08:33:40 -03:00. Fleet root HEAD
`a2f0d3432f05686fedc9c84da3ca975b20257ee1` "close kotodama round-18: admitted
(gate generalized; D4 verified)", 2026-10-18T08:29:58-03:00.

Why a clean root is the expected reading despite busy-looking meta dirs (all
checked 2026-10-18):

- `*-shokunin/` is ignored by the fleet `.gitignore` line 1; `git check-ignore
  -v kotodama-shokunin` → `.gitignore:1:*-shokunin/`. Every lane is an
  independent repository, correctly invisible to fleet git.
- `.ufo/` content is largely tracked (`git ls-files .ufo | wc -l` → 2173);
  `.ufo/waves/*/*-scratch/` is ignored (fleet `.gitignore` line 3); `.scratch/`
  is empty (git-invisible); `.tower/` is excluded via `.git/info/exclude`
  (unchanged from prior rounds).
- The fleet-root `reports/` directory is empty and not ignored — an empty
  directory carries no git entry, so it is not dirt.

Fleet HEAD advanced only by the round-18 close (`a2f0d34`), committed before
this round's declaration; no fleet-root commit postdates it.

## 2. Filed rounds 8–18 untouched

**Scope of the check:** every tracked file under `reports/round-8` …
`reports/round-18` (the filed-round surface), i.e. `git ls-files
reports/round-{8,9,10,11,12,13,14,15,16,17,18}` → **821 paths**.

**Method and result (all commands 2026-10-18, window above, `TMPDIR=$PWD/.scratch`).**

| # | check | command | observed |
|---|---|---|---|
| 1 | working-tree cleanliness | `git status --porcelain=v1` (lane) | empty at both observation points |
| 2 | untracked in filed surface | `git status --porcelain=v1 -uall -- reports/round-8 … reports/round-18` | `0` |
| 3 | commit hygiene | `git diff --name-only e571894 169c616 -- reports/round-8 … reports/round-18` | `0` (empty) |
| 4 | declare-commit contents | `git show --stat 169c616` | exactly `reports/round-19/claims.json` (+32), `reports/round-19/targets.json` (+14) |
| 5 | **git-object identity** | per path: `git rev-parse e571894:<p>` vs `git hash-object <p>` | **821 match, 0 mismatch, 0 not-in-baseline** |
| 6 | whole-surface digest | `find reports/round-{8..18} -type f -not -path '*__pycache__*' \| sort \| xargs sha256sum \| sha256sum` | `17cfb543bcd32c2133b7905aa55a01c2dfb859a4402562927b52b52a072bdd80` |
| 7 | hardlink contamination | `find reports/round-{8..18} -type f -links +1` | empty (no hardlinks into the filed surface) |
| 8 | tree identity | `git diff --stat e571894 169c616` | 2 files, both `reports/round-19/*`; `e571894^{tree}`=`1b4490602cd0b0849fbb33b9d11fcbac90a194dd`, `169c616^{tree}`=`7dec3d25240e0d84d36aab283fbb62c83f82d0f1` |

**Independent cross-round reference (round-18's own filed receipts).**
`reports/round-18/validation.json` records digests for the filed surface it
audited; re-deriving them against the live tree now:

- `input_sha256` rows whose path is under `reports/round-{8..18}`: **89**;
  on-disk sha256 **matches 89/89, 0 mismatch, 0 missing**.
- `filed_rounds.baseline.files` (rounds 8–17, 761 rows): every row's
  `baseline_sha256` and `current_sha256` equal the current on-disk sha256 —
  **761/761 match, 0 mismatch, 0 missing**; `changed_during_validation` = `[]`.

So the filed surface is stable against three independent references: the
baseline git objects (§2 row 5), the round-18 validator's own digest table
(§2 cross-reference), and the whole-surface aggregate digest (row 6).

**Composition note (honest reading).** The non-`__pycache__` on-disk count
under rounds 8–18 is 826, of which **821 are tracked**; the 5-file delta is
git-ignored run logs (`.gitignore` line 3, `*.log`):
`reports/round-9/baselines/{naming-collision-gate,myth-consistency-gate,handoff-packet-check}/run.log`,
`reports/round-11/handoff/{run.log,tamper-control.log}`. Ignored files carry no
git baseline, so they cannot be "byte-stable against baseline"; they are
reported as observed-only. (10 `__pycache__/*.pyc` files also sit under the
filed rounds, likewise ignored — excluded from the digest and the file count.)

## 3. PROVINCE accurate

`PROVINCE.md` (sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`,
git blob `313b182f251564b7997b06996b4f063370778f11`) is **byte-identical to the
baseline revision** (`git diff e571894 169c616 -- PROVINCE.md` → empty; `git
diff --stat e571894 -- PROVINCE.md` → empty). Its last content change is
`c53782a` (supplement-opencode-1), well before this round; the round-19
declaration did not touch it.

Every load-bearing assertion in `PROVINCE.md` was checked against the live
repository surface (2026-10-18):

| PROVINCE assertion | check | observed |
|---|---|---|
| owns `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}` | `ls corpus/knowledge/` | exactly those six partitions; `.md` counts: linguistics 19, myth-symbol 19, culture-material 18, synthesis 24, verification 15, civilizations 94 |
| "this lane's own gates" | `ls tools/gates/*.py` | 10 gate scripts present (7 structural + `d4-assembly-check-gate.py`, `d4-typed-labels-check-gate.py`, `typed-pipeline-gate.py`) |
| "non-canon examples" | `grep -rin 'is canon\|canonical truth\|declared canon' corpus examples` | every hit is a **refusal or handoff** ("no claim here is canon", "which is canon → lore-shokunin"), never a canon claim — consistent with the refuses clause |
| adjacent contract path | `ls corpus/knowledge/synthesis/worldbible-integration-contract.md` | present (28421 bytes) |
| refuses: canon (lore), rights, game mechanics (game-dev-2d/3d), source method (chousa), web publishing (kake), prompt/skill craft (kotoba) | `[ -d ../<lane> ]` for each | all six sibling lanes exist; none is absorbed here |
| "Only writes this standalone lane repository" | `git ls-files` (1528 tracked) filtered for non-lane paths | no out-of-lane tracked paths; the only non-partition tracked entries are lane-root metadata (`AGENTS.md`, `LOG.md`, `MINT.md`, `PROVINCE.md`, `README.md`, `SCORECARD.md`, `SHONEN.md`, `SKILL.md`, `.gitignore`) |
| world bible is lore's, not ours | `ls -d world-bible corpus/world-bible` | neither exists in this lane (no bible recording here) |

The one assertion this seat **cannot** falsify from inside the lane is the
negative "siblings … remain read-only": a lane-local audit cannot prove no
out-of-lane write ever occurred (see §5 N1). No evidence of such a write was
found; the round-19 declaration touches only in-lane paths.

## 4. Commands (all run 2026-10-18, ~08:31–08:34 -03:00, `TMPDIR=$PWD/.scratch`)

- `git status --porcelain=v1` — lane (empty, full) and fleet root (empty), at
  two observation points; `git status --porcelain=v1 -uall` over rounds 8–18
  (empty).
- `git rev-parse HEAD` → `169c616…`; `git rev-parse HEAD^` → `e571894…`;
  `git log -1 --format='%H %cI %s'` for lane and fleet HEAD.
- `git show --stat 169c616`; `git diff --name-only e571894 169c616 --` (and
  over rounds 8–18) → 2 in-lane round-19 paths / 0.
- per-path `git rev-parse e571894:<p>` vs `git hash-object <p>` over the 821
  tracked filed paths → 821/0/0.
- `find reports/round-{8..18} -type f -not -path '*__pycache__*' -print0 |
  LC_ALL=C sort -z | xargs -0 sha256sum | sha256sum` → `17cfb543…`; same with
  `-links +1` → empty; `find … | wc -l` → 826.
- `python3 -` recheck of `reports/round-18/validation.json` `input_sha256`
  (89 rows under rounds 8–18) and `filed_rounds.baseline.files` (761 rows) vs
  on-disk sha256 → 89/0/0 and 761/0/0.
- `sha256sum PROVINCE.md`; `git rev-parse e571894:PROVINCE.md`;
  `git diff e571894 169c616 -- PROVINCE.md` (empty).
- `ls corpus/knowledge/`; per-partition `ls …/*.md | wc -l`; `ls tools/gates/*.py`;
  `ls corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git ls-files | wc -l`; `grep -rin 'is canon\|canonical truth\|declared canon'`.
- `for d in */; do git -C "$d" status --porcelain=v1 | wc -l; done` — sibling
  sweep, 20 lane repos; fleet `git log -1`.

## 5. Findings

- **F-A19-1 (out-of-lane, informational):** `lore-shokunin` working tree is
  dirty (`dirty=2` at the 08:32 sweep) — the recurring r16 F-X02-1 / r17
  F-X02-2 / r18 F-X02-1 class. Cause and disposition are lore's own scope;
  left untouched. All other 18 siblings and the lane itself report `dirty=0`.
- **N1 (limit, negative assertion):** a lane-local scope watch cannot prove the
  negative "no out-of-lane write ever happened". The fleet root is a *different*
  repository and ignores `*-shokunin/`; sibling repos are independent. This
  audit establishes only that the lane's own history and the round-19
  declaration touch in-lane paths, and that the fleet root is clean — not an
  attribution proof of all fleet activity.
- **N2 (in-flight wave):** the 64-worker wave is running while this file is
  written; other seats are landing new untracked files under
  `reports/round-19/` (observed at 08:32: `reports/round-19/audit/`,
  `reports/round-19/availability.json`). Those are *new* round-19 artifacts,
  not filed-round edits — they do not affect the §2 verdict, which binds the
  filed surface of rounds 8–18 and the declaration commit `169c616` only.

## 6. Compliance self-attestation

This seat wrote only `reports/round-19/scope.md` and its sibling
`reports/round-19/scope-a20.md`, plus scratch snapshots under `.scratch/r19-a19/`
(`TMPDIR=$PWD/.scratch` exported before every scratch-writing command). No git
mutation, no commit, no push, no write outside the lane repo, no filed-round
bytes of rounds 8–18 touched (all scratch files are new), no historical
validator executed. Out-of-province observations are routed in §5, never
absorbed, per `PROVINCE.md` ("Out of province → report, never absorb").
