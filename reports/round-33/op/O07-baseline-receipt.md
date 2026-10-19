- Seat: O07 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# Round-33 regression baseline receipt (claim O, pre-integration)

Purpose: pin the pre-integration state of the four regression surfaces the
claim-O threshold names ("zero regressions vs the O07 baseline receipt
(battery 10/10, craft selftests, gate selftests, c31 selftest)") plus the
declaration-time claim-O before-state, so the integrator can prove the
reconciled tree did not move anything it should not have.

Capture window: **2026-10-19T03:52:07Z–03:52:30Z (UTC)**, all legs run in one
parallel batch from the repo root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no integration edit
had landed yet (`reports/round-33/` held only `claims.json`,
`targets.json`, `telemetry/dispatch-declared.json`).

## Binding facts at capture

- `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb` — equals
  `reports/round-33/claims.json:8` `baseline_commit`; `git log -1 --format='%H %cI %s'` →
  `139e3b66… 2026-10-18T22:06:24-03:00 fleet report belongs at the fleet root (.ufo/), not the lane repo`.
- `git status --porcelain` (3 rows, all declaration footprint, no integration edit):
  ` M LOG.md` (regimen-2 entry, +18 lines, `git diff --stat LOG.md` = `1 file changed, 18 insertions(+)`);
  `?? REGIMEN.md`; `?? reports/round-33/`.
- `git ls-files | wc -l` → **2655** (matches the claim-A "before" figure).

## The four assigned commands (all exit 0 at baseline)

| # | command | exit | key output line(s) |
|---|---|---|---|
| 1 | `python3 tools/check-gate-battery.py --selftest` | 0 | `SELFTEST OK 44/44 controls behaved as expected` |
| 2 | `python3 tools/check-craft-exercise.py --selftest` | 0 | `SELFTEST OK 10/10 tamper cases detected` / `CLI-SELFTEST OK 18/18 cases passed` |
| 3 | `python3 tools/assemble-culture-d4.py --selftest` | 0 | `selftest: 81/81 checks passed — positive assemble/--check/determinism, tamper drift, malformed, missing-component and missing-output controls, plus collision, duplicate-id, wrong-type, empty-block, missing-field, too-few-files and serializer/reader-absent fail-closed controls; no file outside the temporary directory touched` |
| 4 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | 0 | `SELFTEST OK: 28/28 checks passed` (28 `PASS` lines, no FAIL) |

## Supplemental legs captured in the same window (read-only)

- `python3 tools/check-gate-battery.py` (battery mode) — exit 0; `summary`:
  `pass 7, fail 0, unevaluable 0`; `baselines.summary`: `coverage "10/10"`,
  `baselines_found 20, pinned 20, unevaluable 0, gates_registered 10,
  gates_uncovered []`, `findings []`; `originals`: `preserved true,
  files_hashed_before 33, files_hashed_after 33, modified 0, added 0,
  deleted 0`; `mirror.removed true`. **This is the "battery 10/10" of the
  claim-O threshold** (10/10 registered gates carry a committed baseline;
  the seven structural gate selftests pass inside it).
- `python3 tools/assemble-culture-d4.py --check` — exit 0,
  `packet.d4.yml: byte-identical deterministic assembly` (no drift; the
  assembler's own pinned packet is stable at the baseline tree).
- `python3 tools/check-evidence-coupling.py --selftest` — exit 0,
  `"selftest_passed": true` (supplemental, not named in the mission; cheap
  and read-only).
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (claim-O
  before-state, reproduction of `claims.json:25`) — **exit 1**:
  `lesson files: 33`, `index rows: 26`, `queue rows: 49`,
  `formats: {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`;
  `FAIL C31_index_rows_eq_files`, `PASS C32_owners_resolve`,
  `PASS C33_formats_documented`, `PASS C34_pins_rederived`,
  `PASS C34c_shape_cells_rederived`, `FAIL C34b_prose_arithmetic`;
  `findings: 2` —
  `C31-1 unindexed-file: ['round-26.md','round-27.md','round-28.md','round-29.md','round-30.md','round-31.md','round-32.md']`
  and `C34-2 prose-arithmetic-drift: {'table_rows_vs_files': {'stated': [26, 26], 'measured': [26, 33]}}`.
  This matches the declared before-state exactly (7 unindexed files, prose
  arithmetic 26 vs 33) and is the honest `before` for the claim-O receipt.

## Digest pins (regression comparison anchors)

```json
{
  "captured_at_utc": "2026-10-19T03:52:07Z",
  "head": "139e3b662900557afe54f632b468619593dc9fcb",
  "sha256": {
    "tools/check-gate-battery.py": "455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce",
    "tools/check-craft-exercise.py": "b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5",
    "tools/assemble-culture-d4.py": "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2",
    "reports/round-25/audit/c31-lessons-index-audit.py": "dc3ee4cca19728ffc0226f08453bcc45d2acbac81267ee377f2d40b274b5175f",
    "corpus/lessons/README.md": "ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c",
    "reports/round-33/claims.json": "ba69090f90c007064fb9c08d04b2fc07ec1514eddf09937bc190021684b3fb12",
    "reports/round-33/targets.json": "342c8f80eb857f96109fc7fcc3d1b816be1264898a25c3f4f8786451f27df13f",
    "reports/round-33/telemetry/dispatch-declared.json": "139b964ead124364443d208cb858967b12a108532eab01b22229dfea1c1ad9ac"
  },
  "digest_provenance": "claims.json/targets.json digests agree with reports/round-33/telemetry/dispatch-declared.json durable_sources[] (command: date -u +%FT%TZ; sha256sum reports/round-33/claims.json reports/round-33/targets.json, 2026-10-19)"
}
```

## Expected post-integration deltas (what may move, what must not)

May move (that is the claim): `corpus/lessons/README.md` (integrator applies
the O02 delta; its digest change is the claim-O after-state) and the c31
full-run output, which must flip to **exit 0, 33 rows == 33 files,
`findings: 0`**.

Must not move (any change here is a regression and the receipt no longer
binds): the four tool digests above (byte-identical), and the observed
results —

1. battery `--selftest` 44/44, exit 0;
2. craft `--selftest` 10/10 + CLI 18/18, exit 0;
3. d4 `--selftest` 81/81 and `--check` byte-identical, exit 0;
4. c31 `--selftest` 28/28, exit 0;
5. battery mode `pass 7 / fail 0 / unevaluable 0`, coverage 10/10, pinned 20,
   `originals.preserved true`.

Re-run block for the integrator (from the repo root, after the O02 delta lands):

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sha256sum tools/check-gate-battery.py tools/check-craft-exercise.py \
  tools/assemble-culture-d4.py reports/round-25/audit/c31-lessons-index-audit.py
python3 tools/check-gate-battery.py --selftest        # expect exit 0, 44/44
python3 tools/check-gate-battery.py                   # expect exit 0, pass 7, coverage 10/10, pinned 20
python3 tools/check-craft-exercise.py --selftest      # expect exit 0, 10/10 + 18/18
python3 tools/assemble-culture-d4.py --selftest       # expect exit 0, 81/81
python3 tools/assemble-culture-d4.py --check          # expect exit 0, byte-identical
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest   # expect exit 0, 28/28
python3 -B reports/round-25/audit/c31-lessons-index-audit.py              # expect exit 0, 33==33, findings 0
```

## Notes for the integrator (recorded, not repaired)

- **Scope-count reconciliation (for A03/X00, no contradiction):**
  `reports/round-32/scope.md:13` reports **1,870 tracked paths** — that is
  round 32's *protected surface only* (reports r8–r31 = 1,735 +
  round-tagged frozen gates = 135, `reports/round-32/scope.md:21-24`) at
  baseline `17e90b9`, not a repo-wide `git ls-files` count. The repo-wide
  count at the round-33 baseline is **2,655** = 1,830 under `reports/round-*`
  + 825 elsewhere (`git ls-files | grep -c '^reports/round-'` = 1830,
  `grep -vc` = 825). Do not read 2,655 as drift from 1,870.
- **The filed lessons index has been byte-frozen since round 28:**
  `corpus/lessons/round-28.md:86` records the index sha256 as
  `ec7469dadf87df3e…`; the live digest measured here is
  `ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c`
  (corroboration that no seat has touched the filed index across rounds
  29–33; not a new census).
- **No gate-side pin on the lessons index (pointer for A09, not A09's
  verdict):** `grep -rln "lessons/README\|corpus/lessons" tools/gates/expected
  tools/gates/frozen tools/gates/*.py` returns only
  `tools/gates/frozen/handoff-packet-check/{r9-pre,r18-post}/packet.md` and
  `tools/gates/frozen/provenance-audit/{r9-pre,r18-post}/inputs/corpus/knowledge/verification/provenance-audit-ledger-format.md`,
  and every hit is a `corpus/lessons/round-6-sources/*.json` **path string**
  inside a frozen packet copy (`packet.md:48,69-72`), not a digest pin on
  `corpus/lessons/README.md`. A09 owns the full cascade verdict — marked
  `to-verify` here.
- The battery's two modes touch only a disposable mirror under `.scratch`
  (`mirror.removed true`; `originals` 33/33 hashed, 0 modified/added/deleted),
  so this receipt's own runs left no tree side effect.

## Post-capture observation — two filed round files rewritten in place (03:52–03:55Z)

This seat wrote only `reports/round-33/op/O07-baseline-receipt.md` and ran
read-only commands; the following change is **not** this seat's and landed
between the capture window and 2026-10-19T03:54:59Z. Recorded here because it
moves filed round bytes, which the round's own rules forbid, and because it
changes the tree state this receipt binds:

- `git status --porcelain` at capture (03:52Z): 3 rows (` M LOG.md`,
  `?? REGIMEN.md`, `?? reports/round-33/`).
- `git status --porcelain` at 03:54:59Z: 4 rows — the same three plus
  ` M reports/round-5/validation.json` and ` M reports/round-7/validation.json`
  (numstat: `2 2` and `1 1` lines).
- Cause, visible in the diffs: a seat re-ran the historical validators
  (`reports/round-5/run-validation.py`, `reports/round-7/run-validation.py`),
  which rewrite their own `validation.json` in place. Round 5's `O` leg error
  changed from a `tools/check-gate-battery.py` exit-2 baseline-coverage
  failure to a `tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`
  exit-2 `gate_digest_mismatch` could-not-evaluate (7/7 rows); round 7's
  `tested_file_sha256["tools/check-gate-battery.py"]` moved
  `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` →
  `455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce`.
- Byte evidence (2026-10-19T03:55:11Z): `reports/round-5/validation.json`
  `fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee` (HEAD
  bytes `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794`);
  `reports/round-7/validation.json`
  `af0cf4ed32d68c2b96284b49de97cfe75900c512299d4dd7423580e9573912a4` (HEAD
  bytes `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3`).
  Round 7's record still reads `acceptance_checks_passed: false`.
- Both pre-edit revisions are recoverable from the baseline commit
  (`git show HEAD:reports/round-5/validation.json`). Restoration is an
  integrator decision — this seat did not touch them and did not repair them.
- Owner: unassigned here; the scope/conformance seats (A03, X02) and the
  reviewer pass are the right places to attribute the writer. Marked
  **to-verify** as to which seat ran them.

## Owed: none

## Citations

- `reports/round-33/claims.json:8` (baseline_commit), `:25` (claim-O before-state), `:37` (threshold naming this receipt)
- `reports/round-33/targets.json:28` (O07 mission + out path), `:5-11` (shared rules)
- `reports/round-33/telemetry/dispatch-declared.json` (durable_sources digests, counting command/date)
- commands (all 2026-10-19T03:52Z, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD`; `git log -1 --format='%H %cI %s'`; `git status --porcelain`; `git diff --stat LOG.md`;
  `git ls-files | wc -l`; `git ls-files | grep -c '^reports/round-'`;
  `sha256sum tools/check-gate-battery.py tools/check-craft-exercise.py tools/assemble-culture-d4.py reports/round-25/audit/c31-lessons-index-audit.py corpus/lessons/README.md`;
  `python3 tools/check-gate-battery.py --selftest`; `python3 tools/check-gate-battery.py`;
  `python3 tools/check-craft-exercise.py --selftest`; `python3 tools/assemble-culture-d4.py --selftest`;
  `python3 tools/assemble-culture-d4.py --check`; `python3 tools/check-evidence-coupling.py --selftest`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest`; `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`
- `reports/round-32/scope.md:13`, `:21-24` (1,870 = 1,735 + 135 protected-surface count)
- `corpus/lessons/round-28.md:86` (filed index sha256 `ec7469dadf87df3e…`)
- `grep -rln "lessons/README\|corpus/lessons" tools/gates/expected tools/gates/frozen tools/gates/*.py`; `grep -n "lessons" tools/gates/frozen/handoff-packet-check/r9-pre/packet.md`
- post-capture observation commands (2026-10-19T03:54:59Z–03:55:11Z, repo root):
  `git status --porcelain`; `git diff --stat reports/round-5/validation.json reports/round-7/validation.json`;
  `git diff --numstat …`; `git diff reports/round-5/validation.json`;
  `sha256sum reports/round-5/validation.json reports/round-7/validation.json`;
  `git show HEAD:reports/round-5/validation.json | sha256sum`; `git show HEAD:reports/round-7/validation.json | sha256sum`
