# R9-D03 — D3 evidence-coupling: selftest + independent domain-control re-drive

- **Round:** 9 · **shard:** R9-D03 (claim D — culture-d3-acceptance) · **date:** 2026-10-17 (all commands below run on this date; all outputs captured verbatim)
- **Repo:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin` · **HEAD:** `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
- **Contract reference:** `reports/round-7/d3-contract.json` (`guard_cli`, `diagnostics`, `controls_format`) — sha256 `8969b1c89945720b0e53314759aa78f358d12bd339e0f6f35dd6ada56e261093`
- **Environment:** Python 3.14.7 · `TMPDIR` <unset> · `/tmp` was inode-exhausted when this shard ran (`df -i /tmp` → `1048576 1048576 0 100%`, 2026-10-17T20:48Z), so every control packet copy and foreign cwd lives under `/dev/shm/r9-d03`, **outside the repo tree**; nothing below writes into the worktree.
- **This shard writes exactly one repo file:** this md. It does not edit the guard, packet, controls, Expected pin, or gate tools; no commit (parent integrates).

## 0. Artifacts under test — digest pins

| artifact | sha256 (measured this run) | matches expected.json manifest pin |
|---|---|---|
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` | yes |
| `examples/culture-d3/packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` | yes |
| `examples/culture-d3/controls.json` | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` | yes |
| `examples/culture-d3/expected.json` | `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` | pin source (frozen verdict label itself) |

So the checker, packet and controls exercised here are byte-identical to the artifacts the round-7 pin describes; only `expected.json` is older than the tree (see §3).

## 1. `--selftest` — exit 0, selftest_passed true

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py --selftest)
{
  "domain_controls": {
    "passed": 16,
    "total": 16
  },
  "frozen_checks": {
    "passed": 5,
    "total": 5
  },
  "malformed_controls": {
    "passed": 4,
    "total": 4
  },
  "missing_inputs": [],
  "note": "all committed-input selftest cases passed",
  "positive_controls": {
    "passed": 5,
    "total": 5
  },
  "profile": "kotodama-d3-evidence-coupling/1",
  "results": [
    {
      "actual": 0,
      "expected": 0,
      "kind": "positive",
      "name": "positive-repo-cwd",
      "passed": true
    },
    {
      "actual": 0,
      "expected": 0,
      "kind": "positive",
      "name": "positive-foreign-cwd",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "cli-usage",
      "name": "usage-no-arguments",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "cli-usage",
      "name": "usage-unknown-option",
      "passed": true
    },
    {
      "actual": 0,
      "expected": 0,
      "kind": "positive",
      "name": "positive:positive-translated-costume-label-change-stays-clean",
      "passed": true
    },
    {
      "actual": 0,
      "expected": 0,
      "kind": "positive",
      "name": "positive:positive-ordinary-utterance-place-change-stays-clean",
      "passed": true
    },
    {
      "actual": 0,
      "expected": 0,
      "kind": "positive",
      "name": "positive:positive-belief-proposition-reword-stays-clean",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-CANON-canon-status-promoted",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-REFERENCE-bridge-target-unknown-record",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-DIGEST-reference-hash-mismatches-ledger-bytes",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-SCOPE-reference-scope-laundered-to-scoped",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-SCOPE-screening-sweep-flag-faked",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-NATIVE-L07-forms-consistent-nonprofile-glyph",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-DERIVATION-name-concat-does-not-yield-declared-form",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-UTTERANCE-ordinary-reading-uses-E0-form",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-TIMING-chosen-offset-outside-discrete-set",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-TIMING-chosen-offset-bool-rejected",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-MYTH-belief-truth-status-certified",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-OBJECT-ground-surface-marked-worn",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-ERA-material-route-missing-costume-era",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-RANK-prohibited-costume-claimed-lawful",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-BRIDGE-bridge-asserted-as-historical",
      "passed": true
    },
    {
      "actual": 1,
      "expected": 1,
      "kind": "domain",
      "name": "domain:domain-D3-SYMBOL-symbol-audience-scope-emptied",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "malformed",
      "name": "malformed:malformed-invalid-json",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "malformed",
      "name": "malformed:malformed-invalid-utf8",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "malformed",
      "name": "malformed:malformed-wrong-root",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "malformed",
      "name": "malformed:malformed-missing-file",
      "passed": true
    },
    {
      "actual": 0,
      "expected": 0,
      "kind": "frozen",
      "name": "frozen-good",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "frozen",
      "name": "frozen-tampered-digest",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "frozen",
      "name": "frozen-unknown-manifest-entry",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "frozen",
      "name": "frozen-bool-expected-exit-false",
      "passed": true
    },
    {
      "actual": 2,
      "expected": 2,
      "kind": "frozen",
      "name": "frozen-bool-expected-exit-true",
      "passed": true
    }
  ],
  "selftest_passed": true
}
exit 0
```

Summary groups in that output: positive 5/5 · domain 16/16 · malformed 4/4 · frozen 5/5; `results` carries 32 case entries and no `missing_inputs`.

Note (for auditors): the selftest's `frozen-*` cases build the good manifest from **live bytes** at run time (`tools/check-evidence-coupling.py:1863-1876`), so a green selftest validates the snapshot machinery, not the committed round-7 `expected.json`. §3 is the missing piece that the selftest cannot see.

## 2. Base positive anchors on the delivered packet

Plain run, repo cwd, and a run from a foreign cwd with an absolute packet path — identical result, which also shows REPO_ROOT resolution is by tool location (`tools/check-evidence-coupling.py:108`), not by cwd:

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json)
{
  "counts": {
    "total": 0
  },
  "exit": 0,
  "findings": [],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 0
```

```
$ (cd /dev/shm/r9-d03/foreign && python3 tools/check-evidence-coupling.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/examples/culture-d3/packet.json)
{
  "counts": {
    "total": 0
  },
  "exit": 0,
  "findings": [],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 0
```

## 3. Committed frozen pin: direct `--frozen` run exits 2 — 3 stale manifest entries (finding, not a control failure)

This invocation is the CLI's own contracted snapshot mode (`<packet.json> [--frozen <expected.json>]`, exit 2 = could-not-evaluate). On the delivered tree it reports three digest mismatches and no verdict:

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json)
{
  "counts": {
    "D3-SNAPSHOT": 3,
    "total": 3
  },
  "exit": 2,
  "findings": [
    {
      "id": "D3-SNAPSHOT",
      "message": "manifest digest mismatch for 'corpus/knowledge/synthesis/worldbible-integration-contract.md': declared 50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1, actual 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069",
      "record_id": "-"
    },
    {
      "id": "D3-SNAPSHOT",
      "message": "manifest digest mismatch for 'tools/gates/costume-era-consistency-gate.py': declared 29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03, actual e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f",
      "record_id": "-"
    },
    {
      "id": "D3-SNAPSHOT",
      "message": "manifest digest mismatch for 'tools/gates/naming-collision-gate.py': declared 8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526, actual d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d",
      "record_id": "-"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 2
```

Independent digest diff of `expected.json`'s manifest against the live bytes (`python3` loop over `json.load('examples/culture-d3/expected.json')['manifest']`, sha256 per file, 2026-10-17) — 3 of 24 entries differ, all non-packet inputs:

| manifest path | declared in expected.json | actual on tree |
|---|---|---|
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |
| `tools/gates/costume-era-consistency-gate.py` | `29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |

Cause evidence (`git log --oneline -3 -- <path>`, 2026-10-17): all three files were last modified by `e1694ba` — *round-8: admit F/O/D — freshness receipts, harness+gate repairs, d2-typed-labels* — while `examples/culture-d3/expected.json` and `examples/culture-d3/packet.json` were last written by `57c3ce6` (*checkpoint: preserve unfinished round-7 D3 integration*). **The packet pin itself has not drifted** (`examples/culture-d3/packet.json` is byte-identical to the pin, §0); the three stale entries are legitimately-edited round-8 siblings, exactly the case `reports/round-7/d3-contract.json` anticipates (`expected.json … limits`: *"later input edits invalidate this snapshot before verdict"*).

Disposition (for the orchestrator / R9-D01 / R9-D04 owners — **not** acted on here): re-pinning `expected.json` after the round-8 edits is a parent-owned snapshot decision; this shard only records the observed state. Until then, any direct `--frozen examples/culture-d3/expected.json` run on this tree must be read as exit 2 (could-not-evaluate), never as a contradiction.

## 4. D3 domain controls — 16 controls, each re-driven independently from both cwds

Method (independent of the checker's own recomputation): `examples/culture-d3/controls.json` is read as data; for each control this shard applies the listed JSON-pointer patch(es) to a **copy** of `examples/culture-d3/packet.json` (all 22 patch ops in `controls.json` — 19 domain + 3 positive — are `replace`, verified by counter over `controls.json`), writes the copy under `/dev/shm/r9-d03/`, and runs the CLI as a subprocess. Comparison mirrors the checker's own normative rule at `tools/check-evidence-coupling.py:1677-1700` (`run_case`): exit code must equal `expected_exit`, and every `expected_ids` entry must be present among the actual findings (extra findings beyond the expected id are permitted — which five of these controls produce, see below). Positive controls additionally require `findings == []`.

| # | control | expected exit / id | actual exit / ids (repo cwd) | verdict |
|---|---|---|---|---|
| 1 | `domain-D3-CANON-canon-status-promoted` | 1 / D3-CANON | 1 / D3-CANON | pass |
| 2 | `domain-D3-REFERENCE-bridge-target-unknown-record` | 1 / D3-REFERENCE | 1 / D3-BRIDGE,D3-REFERENCE (expected id present; superset) | pass |
| 3 | `domain-D3-DIGEST-reference-hash-mismatches-ledger-bytes` | 1 / D3-DIGEST | 1 / D3-DIGEST | pass |
| 4 | `domain-D3-SCOPE-reference-scope-laundered-to-scoped` | 1 / D3-SCOPE | 1 / D3-SCOPE | pass |
| 5 | `domain-D3-SCOPE-screening-sweep-flag-faked` | 1 / D3-SCOPE | 1 / D3-SCOPE | pass |
| 6 | `domain-D3-NATIVE-L07-forms-consistent-nonprofile-glyph` | 1 / D3-NATIVE | 1 / D3-NATIVE,D3-NATIVE,D3-NATIVE (expected id present; superset) | pass |
| 7 | `domain-D3-DERIVATION-name-concat-does-not-yield-declared-form` | 1 / D3-DERIVATION | 1 / D3-DERIVATION,D3-DERIVATION (expected id present; superset) | pass |
| 8 | `domain-D3-UTTERANCE-ordinary-reading-uses-E0-form` | 1 / D3-UTTERANCE | 1 / D3-UTTERANCE | pass |
| 9 | `domain-D3-TIMING-chosen-offset-outside-discrete-set` | 1 / D3-TIMING | 1 / D3-TIMING | pass |
| 10 | `domain-D3-TIMING-chosen-offset-bool-rejected` | 1 / D3-TIMING | 1 / D3-TIMING | pass |
| 11 | `domain-D3-MYTH-belief-truth-status-certified` | 1 / D3-MYTH | 1 / D3-MYTH | pass |
| 12 | `domain-D3-OBJECT-ground-surface-marked-worn` | 1 / D3-OBJECT | 1 / D3-OBJECT,D3-OBJECT (expected id present; superset) | pass |
| 13 | `domain-D3-ERA-material-route-missing-costume-era` | 1 / D3-ERA | 1 / D3-ERA,D3-ERA (expected id present; superset) | pass |
| 14 | `domain-D3-RANK-prohibited-costume-claimed-lawful` | 1 / D3-RANK | 1 / D3-RANK | pass |
| 15 | `domain-D3-BRIDGE-bridge-asserted-as-historical` | 1 / D3-BRIDGE | 1 / D3-BRIDGE | pass |
| 16 | `domain-D3-SYMBOL-symbol-audience-scope-emptied` | 1 / D3-SYMBOL | 1 / D3-SYMBOL | pass |

### 4.1 `domain-D3-CANON-canon-status-promoted`

Patch spec: `replace /canon_status`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-CANON-canon-status-promoted.json)
{
  "counts": {
    "D3-CANON": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-CANON",
      "message": "canon_status must be NON-CANON, got 'CANON'",
      "record_id": "-"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-CANON'], stdout sha256 `6bd9104a3d1be9053409d31a234f2bf41491b4c4bafcdf680a5268cd4a25154f` (byte-identical stdout).

### 4.2 `domain-D3-REFERENCE-bridge-target-unknown-record`

Patch spec: `replace /bridges/0/target_ids/0`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-REFERENCE-bridge-target-unknown-record.json)
{
  "counts": {
    "D3-BRIDGE": 1,
    "D3-REFERENCE": 1,
    "total": 2
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-REFERENCE",
      "message": "bridge target 'U99' is not an existing D3 record id",
      "record_id": "BR01"
    },
    {
      "id": "D3-BRIDGE",
      "message": "bridge targets ['U99', 'U02'] differ from the declared design-only mapping ['U01', 'U02']",
      "record_id": "BR01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-BRIDGE', 'D3-REFERENCE'], stdout sha256 `09ac59bba4d67d535d0dafd5db0ca7cd2753cc09003d97bb9de694bfc1b6f1f5` (byte-identical stdout).

### 4.3 `domain-D3-DIGEST-reference-hash-mismatches-ledger-bytes`

Patch spec: `replace /references/0/file_sha256`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-DIGEST-reference-hash-mismatches-ledger-bytes.json)
{
  "counts": {
    "D3-DIGEST": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-DIGEST",
      "message": "declared file_sha256 '0000000000000000000000000000000000000000000000000000000000000000' disagrees with actual bytes of corpus/lessons/round-6-sources/05.json (a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb)",
      "record_id": "S01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-DIGEST'], stdout sha256 `016dd31cafb1e40bf792d1990da809299eb21f03626f6e57f42043f677904d95` (byte-identical stdout).

### 4.4 `domain-D3-SCOPE-reference-scope-laundered-to-scoped`

Patch spec: `replace /references/0/support_scope`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-SCOPE-reference-scope-laundered-to-scoped.json)
{
  "counts": {
    "D3-SCOPE": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-SCOPE",
      "message": "reference support_scope 'scoped-support' differs from the effective round-6 reconciliation value 'partial-support'",
      "record_id": "S01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-SCOPE'], stdout sha256 `c46efa90f301d389b1759148f7ec98994e29cc966a80c3af31c8ff18cae82128` (byte-identical stdout).

### 4.5 `domain-D3-SCOPE-screening-sweep-flag-faked`

Patch spec: `replace /screening/real_language_sweep_performed`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-SCOPE-screening-sweep-flag-faked.json)
{
  "counts": {
    "D3-SCOPE": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-SCOPE",
      "message": "real_language_sweep_performed must be exactly false in this bounded drill (a claimed sweep is a clearance-scope contradiction)",
      "record_id": "screening"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-SCOPE'], stdout sha256 `7e4178a777fa53cbfcfd5a2ae8da75c57f02181ad964ef4fbf23daa2d7aacfaf` (byte-identical stdout).

### 4.6 `domain-D3-NATIVE-L07-forms-consistent-nonprofile-glyph`

Patch spec: `replace /lexicon/6/native_form`; `replace /lexicon/6/forms/E0`; `replace /lexicon/6/forms/E1`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-NATIVE-L07-forms-consistent-nonprofile-glyph.json)
{
  "counts": {
    "D3-NATIVE": 3,
    "total": 3
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-NATIVE",
      "message": "native form 'tana!' violates the declared profile: no syllable vowel at position 4",
      "record_id": "L07"
    },
    {
      "id": "D3-NATIVE",
      "message": "native form 'tana!' violates the declared profile: no syllable vowel at position 4",
      "record_id": "L07"
    },
    {
      "id": "D3-NATIVE",
      "message": "native form 'tana!' violates the declared profile: no syllable vowel at position 4",
      "record_id": "L07"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-NATIVE', 'D3-NATIVE', 'D3-NATIVE'], stdout sha256 `de6972b200f9d7fc114cf39956c23e53a97ffda82b9fe7f45c820136f8bf0fea` (byte-identical stdout).

### 4.7 `domain-D3-DERIVATION-name-concat-does-not-yield-declared-form`

Patch spec: `replace /names/0/native_form`; `replace /names/0/formation/expected`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-DERIVATION-name-concat-does-not-yield-declared-form.json)
{
  "counts": {
    "D3-DERIVATION": 2,
    "total": 2
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-DERIVATION",
      "message": "formation.expected 'funalu' does not equal the concat of E1 base forms ['suma', 'talu'] (computed 'sumatalu')",
      "record_id": "N01"
    },
    {
      "id": "D3-DERIVATION",
      "message": "native_form 'funalu' does not equal the computed concat 'sumatalu'",
      "record_id": "N01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-DERIVATION', 'D3-DERIVATION'], stdout sha256 `0186c2a465a4dbc0cad2a93ad73c42db0956d53ac3f8557cc93c4afd308e5afd` (byte-identical stdout).

### 4.8 `domain-D3-UTTERANCE-ordinary-reading-uses-E0-form`

Patch spec: `replace /utterances/0/spoken_form`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-UTTERANCE-ordinary-reading-uses-E0-form.json)
{
  "counts": {
    "D3-UTTERANCE": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-UTTERANCE",
      "message": "spoken_form 'pina' fails the ordinary context law (expected 'fina'; exact-match avoidance rule: False)",
      "record_id": "U01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-UTTERANCE'], stdout sha256 `5dc8a2f413aaea6a4220a13b473557bc4ad56d61b379261a0103ff564364208d` (byte-identical stdout).

### 4.9 `domain-D3-TIMING-chosen-offset-outside-discrete-set`

Patch spec: `replace /naming_rule/chosen_offset`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-TIMING-chosen-offset-outside-discrete-set.json)
{
  "counts": {
    "D3-TIMING": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-TIMING",
      "message": "chosen_offset 9 is outside the discrete allowed set [2, 8, 20]",
      "record_id": "NR1"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-TIMING'], stdout sha256 `8fed74b1afbd759e1fc3ac5c886929a055f4a5e218c0cf6248a97d48298e3644` (byte-identical stdout).

### 4.10 `domain-D3-TIMING-chosen-offset-bool-rejected`

Patch spec: `replace /naming_rule/chosen_offset`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-TIMING-chosen-offset-bool-rejected.json)
{
  "counts": {
    "D3-TIMING": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-TIMING",
      "message": "chosen_offset must be an integer (bools rejected), got True",
      "record_id": "NR1"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-TIMING'], stdout sha256 `91424e8095a85d4c8dd6aa6f1897adea81f5330199ca30f2ef9e201a932dbe57` (byte-identical stdout).

### 4.11 `domain-D3-MYTH-belief-truth-status-certified`

Patch spec: `replace /beliefs/0/truth_status`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-MYTH-belief-truth-status-certified.json)
{
  "counts": {
    "D3-MYTH": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-MYTH",
      "message": "truth_status must remain 'unresolved', got 'world-fact' (no world-fact or supernatural certification)",
      "record_id": "B01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-MYTH'], stdout sha256 `11a0934e7bce398103536632610de16012052f3aa97c1ad249cbe10c77caef20` (byte-identical stdout).

### 4.12 `domain-D3-OBJECT-ground-surface-marked-worn`

Patch spec: `replace /objects/0/worn`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-OBJECT-ground-surface-marked-worn.json)
{
  "counts": {
    "D3-OBJECT": 2,
    "total": 2
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-OBJECT",
      "message": "object worn flag must be False, got True",
      "record_id": "O01"
    },
    {
      "id": "D3-OBJECT",
      "message": "a ground-surface object is marked worn",
      "record_id": "O01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-OBJECT', 'D3-OBJECT'], stdout sha256 `176d3c95dc1a83584cb74cbffe1aa9886743170bd7cb99b980cba71c80563eaf` (byte-identical stdout).

### 4.13 `domain-D3-ERA-material-route-missing-costume-era`

Patch spec: `replace /materials/1/routes/0/eras`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-ERA-material-route-missing-costume-era.json)
{
  "counts": {
    "D3-ERA": 2,
    "total": 2
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-ERA",
      "message": "route active in 'E0' before the material's declared availability 'E1'",
      "record_id": "M02"
    },
    {
      "id": "D3-ERA",
      "message": "no active provenance route covers the costume's declared era 'E1'",
      "record_id": "C03"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-ERA', 'D3-ERA'], stdout sha256 `9287646966a2b43a73bb4b41b74819a1041e3b39b2ec2401de36e803db4a49ea` (byte-identical stdout).

### 4.14 `domain-D3-RANK-prohibited-costume-claimed-lawful`

Patch spec: `replace /costumes/2/claimed_status`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-RANK-prohibited-costume-claimed-lawful.json)
{
  "counts": {
    "D3-RANK": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-RANK",
      "message": "falsely claims lawful entitlement to a use prohibited by 'RR1' (material 'plant-cloth', 'assembly' in 'hall' as 'visitor')",
      "record_id": "C03"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-RANK'], stdout sha256 `88e08281f57351f6b0980784704bad1a85a34d709f43193c74274b8c668b4914` (byte-identical stdout).

### 4.15 `domain-D3-BRIDGE-bridge-asserted-as-historical`

Patch spec: `replace /bridges/0/asserted_scope`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-BRIDGE-bridge-asserted-as-historical.json)
{
  "counts": {
    "D3-BRIDGE": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-BRIDGE",
      "message": "asserted_scope must be 'design-only', got 'historical-reconstruction' (no historical reconstruction claim)",
      "record_id": "BR01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-BRIDGE'], stdout sha256 `abc32e03a974b8872e3c5874620544ada2725858921ffc48e49fbaa8ecbbbbd3` (byte-identical stdout).

### 4.16 `domain-D3-SYMBOL-symbol-audience-scope-emptied`

Patch spec: `replace /symbols/0/audience`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/domain-D3-SYMBOL-symbol-audience-scope-emptied.json)
{
  "counts": {
    "D3-SYMBOL": 1,
    "total": 1
  },
  "exit": 1,
  "findings": [
    {
      "id": "D3-SYMBOL",
      "message": "symbol audience scope must be nonempty",
      "record_id": "SY01"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 1
```

- Foreign cwd: same packet path, `cd /dev/shm/r9-d03/foreign && python3 <repo>/tools/check-evidence-coupling.py` → exit 1, ids ['D3-SYMBOL'], stdout sha256 `536a647833914ee81d2f067de555f91780a9588616fd28f3dc4b37f0ab4464d7` (byte-identical stdout).

## 5. Positive controls (contract-required clean cases) — 3/3

These are the "translated-display-label change" and "ordinary unaffected-context" changes the contract requires to stay clean (`controls_format`: *"Positive translated-display-label changes and ordinary unaffected-context controls must remain clean"*). Each must exit 0 with `findings: []`.

### positive-translated-costume-label-change-stays-clean

Patch spec: `replace /costumes/0/display_label`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/positive-translated-costume-label-change-stays-clean.json)
{
  "counts": {
    "total": 0
  },
  "exit": 0,
  "findings": [],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 0
```
- Foreign cwd: exit 0, findings [], stdout sha256 `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d` (byte-identical stdout).

### positive-ordinary-utterance-place-change-stays-clean

Patch spec: `replace /utterances/2/place`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/positive-ordinary-utterance-place-change-stays-clean.json)
{
  "counts": {
    "total": 0
  },
  "exit": 0,
  "findings": [],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 0
```
- Foreign cwd: exit 0, findings [], stdout sha256 `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d` (byte-identical stdout).

### positive-belief-proposition-reword-stays-clean

Patch spec: `replace /beliefs/0/proposition`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/positive-belief-proposition-reword-stays-clean.json)
{
  "counts": {
    "total": 0
  },
  "exit": 0,
  "findings": [],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 0
```
- Foreign cwd: exit 0, findings [], stdout sha256 `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d` (byte-identical stdout).

## 6. Malformed controls — 4/4

Construction (this shard's own bytes, not the tool's helper): `invalid-json` = truncated JSON `{"profile": "kotodama-d3-evidence-coupling/1", "packet": `; `invalid-utf8` = valid JSON wrapper with a raw `0xFF 0xFE` byte pair inside a string; `wrong-root` = the JSON array `["not", "an", "object"]`; `missing-file` = a scratch path deliberately never created. Each must exit 2 with `D3-DATA` and no traceback.

### malformed-invalid-json

Fixture: `bytes b'{"profile": "kotodama-d3-evidence-coupling/1", "packet": '`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/malformed-invalid-json.json)
{
  "counts": {
    "D3-DATA": 1,
    "total": 1
  },
  "exit": 2,
  "findings": [
    {
      "id": "D3-DATA",
      "message": "packet is not valid JSON: Expecting value: line 1 column 58 (char 57)",
      "record_id": "-"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 2
```
- Foreign cwd: exit 2, ids ['D3-DATA'], stdout sha256 `23ec4dc412ffa762093f297929fefc8ba35e1759630c28473f54a43978a8ba37` (byte-identical stdout).

### malformed-invalid-utf8

Fixture: `bytes b'{"profile": "kotodama-d3-evidence-coupling/1", "x": "\xff\xfe"}'`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/malformed-invalid-utf8.json)
{
  "counts": {
    "D3-DATA": 1,
    "total": 1
  },
  "exit": 2,
  "findings": [
    {
      "id": "D3-DATA",
      "message": "packet is not valid UTF-8: 'utf-8' codec can't decode byte 0xff in position 53: invalid start byte",
      "record_id": "-"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 2
```
- Foreign cwd: exit 2, ids ['D3-DATA'], stdout sha256 `5d9de1a52cd31614003ac00fa2c21cf0099f22e79a4461e676a3d96d5ed4759c` (byte-identical stdout).

### malformed-wrong-root

Fixture: `bytes b'["not", "an", "object"]'`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/malformed-wrong-root.json)
{
  "counts": {
    "D3-DATA": 1,
    "total": 1
  },
  "exit": 2,
  "findings": [
    {
      "id": "D3-DATA",
      "message": "packet root must be a JSON object, got list",
      "record_id": "-"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 2
```
- Foreign cwd: exit 2, ids ['D3-DATA'], stdout sha256 `d82df7d3d181aaaecd88b97058b94c11d869dcd685f93d78e401695a312c384a` (byte-identical stdout).

### malformed-missing-file

Fixture: `path deliberately absent from scratch`

```
$ (cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 tools/check-evidence-coupling.py /dev/shm/r9-d03/malformed-missing-file.json)
{
  "counts": {
    "D3-DATA": 1,
    "total": 1
  },
  "exit": 2,
  "findings": [
    {
      "id": "D3-DATA",
      "message": "packet cannot be read: No such file or directory",
      "record_id": "-"
    }
  ],
  "profile": "kotodama-d3-evidence-coupling/1"
}
exit 2
```
- Foreign cwd: exit 2, ids ['D3-DATA'], stdout sha256 `21b6be84a8599067406f3a594efd139c3ac6d16a5cc3b571b84576af68b30b55` (byte-identical stdout).

## 7. Summary, coverage and limits

- **All 23 controls re-driven independently in both cwds: 23/23 pass** (16 domain, 3 positive, 4 malformed; the run script is the inline driver described in §4, receipts captured to `/dev/shm/r9-d03/receipts2.json`, ephemeral). Selftest: `selftest_passed: true`, exit 0, 4 summary groups green and 32 `results` entries.
- **Diagnostic coverage:** the committed domain negatives exercise 14 distinct ids — D3-BRIDGE, D3-CANON, D3-DERIVATION, D3-DIGEST, D3-ERA, D3-MYTH, D3-NATIVE, D3-OBJECT, D3-RANK, D3-REFERENCE, D3-SCOPE, D3-SYMBOL, D3-TIMING, D3-UTTERANCE — which is every diagnostic in `reports/round-7/d3-contract.json` except `D3-DATA` (covered by §6 malformed) and `D3-SNAPSHOT` (covered by the selftest frozen cases and §3's live demonstration). Counting command: `python3 -c` set-difference of `controls.json` domain `expected_ids` against `reports/round-7/d3-contract.json` `diagnostics` keys, 2026-10-17.
- **No-write check:** the guard's normal-run modes left the tree untouched — `git status --porcelain` before and after all runs identical (`True`), and `examples/culture-d3/packet.json` sha256 unchanged (`True`).
- **Residual flagged to the parent (§3):** `--frozen examples/culture-d3/expected.json` exits 2 on this tree because 3 of its 24 manifest entries were legitimately edited in commit `e1694ba` (round 8). Not a checker defect; a stale parent-owned snapshot. Re-pin decision belongs to the orchestrator / R9-D01 / R9-D04.
- **Limits (what this receipt does not certify):** it certifies the checker's discrimination on the committed fixture set and this packet, not universal malformed-schema coverage, historical authenticity, language screening, cultural permission or lore acceptance (`reports/round-7/d3-contract.json` `guard_cli` and `expected.json` `limits`). The scratch copies live outside the repo, so re-running requires re-creating them from the pinned `controls.json`.

