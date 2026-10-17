# naming-collision-gate baseline — author seat (round 9, claim O)

- role: **author** — this seat owns `expected.json`, `packet.yml`, `run.log` and `freeze.txt` in
  this directory, plus this fragment. Nothing here is committed; the orchestrator integrates once
  per round. Scope: `tools/gates/naming-collision-gate.py` only; no gate bytes were edited.
- date: 2026-10-17, timestamps local (-03:00). Lane HEAD at freeze:
  `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`git rev-parse HEAD`); round-9 declared
  `baseline_revision: e1694bad…` (`reports/round-9/claims.json`). Measured diff:
  `git diff --stat e1694bad…HEAD` → only `reports/round-9/claims.json` (+34) and
  `reports/round-9/targets.json` (+125), 159 insertions, 0 deletions — the graded artifact tree is
  identical between the declared revision and HEAD.
- gate: `tools/gates/naming-collision-gate.py`, sha256
  `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` (`sha256sum`, 2026-10-17).
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (layout),
  §4 (schema `kotodama-frozen-run-v1`, finding-ID **set** contract), §5 (freeze procedure),
  §6 (verify/tamper semantics). Baseline id: `r9-pre` (phase pre: before the round's edits land).

## 1. Capability — `--selftest` (exit 0)

`python3 tools/gates/naming-collision-gate.py --selftest` → exit **0**; stdout (file:line = command
output, 2026-10-17T17:48:40-03:00): `selftest: OK — fixture findings 12 across 11 ids (CROSS-HOLD,
DERIV-AFFIX, DERIV-HOLD, DERIV-REPLAY, NAME-LEXEME, NAME-NEAR, NAME-REUSE, NAME-VISUAL, PHON-CODA,
PHON-INVENTORY, PHON-ONSET); positive control clean; malformed inputs exit 2; missing profile held;
case policy routed`. `git status --porcelain -- tools/gates` afterwards: no tracked modification.

## 2. Snapshot and frozen run (exit 1, class `findings`)

- Input chosen: `examples/culture-d2/packet.d2.yml` — the standard §7/§9 names the D2 culture packet
  as the intended first real baseline input (the fixture run is the selftest's own capability path).
  `cp` → `packet.yml`; `cmp` clean; sha256
  `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` (equal to the origin file).
- Run: `python3 tools/gates/naming-collision-gate.py reports/round-9/baselines/naming-collision-gate/packet.yml`
  (cwd = lane root) → exit **1**, 17 `FINDING` lines; counts from
  `grep -o 'FINDING [A-Z-]*' run.log | sort | uniq -c` (2026-10-17):
  NAME-NEAR 6, PHON-INVENTORY 10, CROSS-HOLD 1.
- `expected.json` written from the observed run: `expected.exit` 1, `expected.class` `findings`,
  `expected.findings` `["CROSS-HOLD", "NAME-NEAR", "PHON-INVENTORY"]`; advisory
  `stdout_sha256` `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b`.
- Snapshot rule honoured: the copy was made once and never edited after the run.

## 3. Verification runs

| # | Command (2026-10-17) | Observed |
|---|---|---|
| 1 | gate over the **live** path `examples/culture-d2/packet.d2.yml` | exit 1; `cmp` against `run.log` → byte-identical (verdict is path-independent) |
| 2 | gate over `packet.yml` from an **isolated mirror** `.scratch/r9-naming-author/mirror/` (copied gate + packet, different cwd) | exit 1; stdout sha256 `ebc8850d…` = `run.log` sha256 (byte-identical) |
| 3 | input digest re-check against `expected.json` `inputs` | `packet.yml: OK`, exit 0 |

## 4. Tamper negative (standard §6, measured)

Copy of `packet.yml` + `printf '\n# tampered byte\n' >>` → sha256
`265bd5c6a37fd90a5e0692ce39a6564622e0a787bc4293cf7dcedf944f7009d7`;
`sha256sum -c` → `FAILED` + `WARNING: 1 computed checksum did NOT match`, exit 1 →
`snapshot_tampered` (could-not-evaluate). Re-running the gate over the tampered copy printed stdout
**byte-identical** to `run.log`, so an integrator comparing only stdout would false-pass. The
naming gate has **no internal digest check** (documented open item, standard §8); the interim
external `sha256sum` step above is the check that ran, and O15's battery extension is the durable
home for it.

## 5. Negative control — no gate or fixture bytes changed

- `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- tools/gates` → empty.
- `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- examples` → empty.
- `git status --porcelain -- tools/gates examples` (2026-10-17T17:49-03:00) → no tracked
  modification; the only entries were untracked directories created by **sibling O-shard seats**
  (`?? tools/gates/expected/`, `?? tools/gates/frozen/handoff-packet-check/`), not this seat.

## 6. Integration notes (reported to the orchestrator, not absorbed here)

- **`.gitignore` swallows `run.log`:** `.gitignore` line 3 is `*.log`; `git check-ignore -v
  reports/round-9/baselines/naming-collision-gate/run.log` → `.gitignore:3:*.log`. The baseline
  must be committed with `git add -f` for `run.log`, or it lands without its verbatim stdout.
- **Baseline roots diverged across this round's O shards** (observed 2026-10-17T17:5x):
  this baseline (+ the phonology pair's `rerun.md` §6 reading: the author seat owns
  `expected.json`/snapshot/`run.log`/`freeze.txt` “in the same directory”) uses
  `reports/round-9/baselines/<gate-name>/`; `costume-era-consistency-gate` landed at
  `tools/gates/expected/<gate>/r9-pre/`; `handoff-packet-check` and `lexicon-coverage-audit` at
  `tools/gates/frozen/<gate>/r9-pre/`. The standard §3 root is
  `tools/gates/frozen/<gate-name>/<baseline-id>/`. Contested scope — the integrator decides; if the
  fleet standardizes there, `git mv` these four files verbatim (digests unchanged), never re-freeze.
  For O15: a robust battery scan reads `reports/round-9/baselines/*/expected.json` **and**
  `tools/gates/**/expected.json` and dedupes by (gate, baseline_id, input digests).
- **Append-only:** the graded input is a mutable design artifact; a later edit to the live packet
  earns a *new* baseline (`r9-post`), never a re-pin of this one.

## 7. Limits and what this does not claim

- A pasted-in-run is engineering evidence (these bytes, this gate revision, this verdict); it is
  not a design PASS, not a canon ruling, and says nothing about whether the packet's names are good
  (`corpus/knowledge/verification/gate-frozen-run-standard.md` §2, §11).
- `finding_counts` in `expected.json` is advisory; the compared contract is the exit code and the
  finding-ID set (standard §4) — stdout order is not part of it.
- Concurrent observation on the shared tool (not this shard's deliverable):
  `python3 tools/check-gate-battery.py --selftest` → exit 0, `SELFTEST OK 10/10 controls behaved as
  expected` (2026-10-17T17:49-03:00). The battery's baseline-validation extension is O15's shard.
- Independent re-run of this baseline in a copied tree is the paired rerunner seat's deliverable
  (expected in this directory); none was present when this fragment was written (to-verify until it
  lands).
