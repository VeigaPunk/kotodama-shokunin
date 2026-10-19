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
