- Seat: C02 | executor | C | date 2026-10-19 | baseline da68a6d

# C02 — durable box-1 re-survey receipt JSON (claim C, content)

**Mission** (`reports/round-34/targets.json:56`): the full 28-row JSON for the integrator
to land at `reports/round-34/craft/box1-resurvey-durable.json`, digest-pinned at SKILL.md
`f9bd07c2…`. Landing is the integrator's write; this fragment carries the exact bytes.

**Measured, this seat** (2026-10-19, lane HEAD `da68a6d`, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `sha256sum SKILL.md` → `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` (732 lines).
- `python3 -B reports/round-30/craft/box1-survey.py` → exit `0`; stdout:
  `named 28`, `resolvable 28`,
  `unnamed_in_skill []`, `skill_sha256 f9bd07c2bd13462367be20e8…`.
- Row census (this seat's own enumeration, same pattern as `box1-survey.py:6`):
  28 named executables, 28 resolve on disk, 0 unresolvable.
- `sha256sum reports/round-30/craft/box1-survey.py` → `d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89`.
- Independent re-check (this seat, after writing the fragment): the fenced JSON extracted
  from this file is byte-identical to the generator's output; a second enumeration
  (`grep -oE 'tools/[A-Za-z0-9_./-]+\.py' SKILL.md | sort -u`, then `sha256sum` per row)
  reproduces the set, every digest and every line list with zero mismatches; the fragment's
  own verification block, run against a byte-identical copy, exits 0 with
  `box1-resurvey-durable: OK 28 rows at f9bd07c2bd13`.

## Landing instruction

Write the fenced block below **verbatim** (contents only, no fence) to
`reports/round-34/craft/box1-resurvey-durable.json`. Nothing in it edits filed bytes:
the round-30 receipt and the r32 console re-verify stay as they are; this file is a new
dated reading at the round-34 SKILL.md bytes.

```json
{
 "date": "2026-10-19",
 "measured_at_utc": "2026-10-19T07:11:01Z",
 "mode": "landed",
 "round": 34,
 "provenance": {
  "owner": "round-34 seat C02 (content author); landed by the round-34 integrator at reports/round-34/craft/box1-resurvey-durable.json",
  "supersedes": "reports/round-30/craft/box1-landed-survey.json (SKILL.md 83b0a78a..., 28/28) and the r32 console re-verify at 79fe91d3... (reports/round-32/final-dossier.md:46) - both remain filed, unedited; this is a new dated reading at the round-34 SKILL.md bytes",
  "not_a_promotion_verdict": "re-survey of the executable surface named in SKILL.md; promotion decisions stay operator-owned"
 },
 "skill": "SKILL.md",
 "skill_lines": 732,
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b",
 "survey_script": "reports/round-30/craft/box1-survey.py",
 "survey_script_sha256": "d923ae0fcd544513122851b55389111b3195528f8e3a4c8fb69703072132cf89",
 "rerun": "export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1; python3 -B reports/round-30/craft/box1-survey.py",
 "rerun_exit_code": 0,
 "survey_stdout": {
  "date": "2026-10-18",
  "named": 28,
  "resolvable": 28,
  "unnamed_in_skill": [],
  "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"
 },
 "survey_stdout_note": "The survey script hard-codes its 'date' field (box1-survey.py:8 -> 2026-10-18), so survey_stdout.date is the script's filing date, not the run date; the run date is measured_at_utc above, and the pin that matters is skill_sha256, read live by box1-survey.py:10.",
 "named_in_skill": 28,
 "resolvable": 28,
 "unresolvable": [],
 "rows_scope_note": "Rows are the executables (tools/*.py paths) named in SKILL.md, matched by box1-survey.py:6 r'tools/[\\w./-]+\\.py'. 'line'/'lines' are SKILL.md line numbers at skill_sha256 above; 'sha256' is the executable file's digest at that same tree.",
 "reverify": "re-run: export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1; python3 -B reports/round-30/craft/box1-survey.py ; then re-extract this receipt's rows and diff executable/sha256 and skill_sha256. A moved skill_sha256 reads as a superseded reading, never a tamper finding on this file.",
 "executable_inventory_note": "28 named executables, 28 resolvable, 0 unnamed_in_skill: the box-1 executable inventory condition is green at these bytes.",
 "rows": [
  {
   "executable": "tools/assemble-culture-d3.py",
   "resolves": true,
   "line": 673,
   "lines": [
    673
   ],
   "sha256": "ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014"
  },
  {
   "executable": "tools/assemble-culture-d4.py",
   "resolves": true,
   "line": 207,
   "lines": [
    207
   ],
   "sha256": "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2"
  },
  {
   "executable": "tools/assemble-d2-typed.py",
   "resolves": true,
   "line": 449,
   "lines": [
    449
   ],
   "sha256": "c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071"
  },
  {
   "executable": "tools/assemble-d2.py",
   "resolves": true,
   "line": 615,
   "lines": [
    615
   ],
   "sha256": "8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d"
  },
  {
   "executable": "tools/assemble-d4-typed.py",
   "resolves": true,
   "line": 139,
   "lines": [
    139,
    158,
    163,
    195,
    207,
    210,
    211,
    213,
    294
   ],
   "sha256": "92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0"
  },
  {
   "executable": "tools/check-craft-exercise.py",
   "resolves": true,
   "line": 616,
   "lines": [
    616
   ],
   "sha256": "b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5"
  },
  {
   "executable": "tools/check-evidence-coupling.py",
   "resolves": true,
   "line": 674,
   "lines": [
    674
   ],
   "sha256": "849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e"
  },
  {
   "executable": "tools/check-gate-battery.py",
   "resolves": true,
   "line": 617,
   "lines": [
    617,
    617,
    617
   ],
   "sha256": "455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce"
  },
  {
   "executable": "tools/d2-typed-labels.py",
   "resolves": true,
   "line": 35,
   "lines": [
    35,
    169,
    208,
    258,
    272,
    281,
    288,
    289,
    290,
    291,
    292,
    293,
    304,
    308,
    329,
    479,
    481,
    483,
    491
   ],
   "sha256": "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3"
  },
  {
   "executable": "tools/exercise-handoff-e2e.py",
   "resolves": true,
   "line": 448,
   "lines": [
    448
   ],
   "sha256": "a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df"
  },
  {
   "executable": "tools/gates/argot-derivation-gate.py",
   "resolves": true,
   "line": 375,
   "lines": [
    375,
    376,
    377,
    429,
    438
   ],
   "sha256": "b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb"
  },
  {
   "executable": "tools/gates/costume-era-consistency-gate.py",
   "resolves": true,
   "line": 609,
   "lines": [
    609
   ],
   "sha256": "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f"
  },
  {
   "executable": "tools/gates/d4-assembly-check-gate.py",
   "resolves": true,
   "line": 450,
   "lines": [
    450
   ],
   "sha256": "df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a"
  },
  {
   "executable": "tools/gates/d4-typed-labels-check-gate.py",
   "resolves": true,
   "line": 451,
   "lines": [
    451
   ],
   "sha256": "05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841"
  },
  {
   "executable": "tools/gates/handoff-packet-check.py",
   "resolves": true,
   "line": 500,
   "lines": [
    500,
    500,
    612
   ],
   "sha256": "e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575"
  },
  {
   "executable": "tools/gates/lexicon-coverage-audit.py",
   "resolves": true,
   "line": 607,
   "lines": [
    607
   ],
   "sha256": "2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287"
  },
  {
   "executable": "tools/gates/myth-consistency-gate.py",
   "resolves": true,
   "line": 608,
   "lines": [
    608
   ],
   "sha256": "5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08"
  },
  {
   "executable": "tools/gates/naming-collision-gate.py",
   "resolves": true,
   "line": 610,
   "lines": [
    610
   ],
   "sha256": "d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d"
  },
  {
   "executable": "tools/gates/phonology-sanity-gate.py",
   "resolves": true,
   "line": 606,
   "lines": [
    606
   ],
   "sha256": "d5fe087ffb2342e54cd6d6f3ef1e891315a95224bc25cdc5bc425b91dec34230"
  },
  {
   "executable": "tools/gates/provenance-audit.py",
   "resolves": true,
   "line": 611,
   "lines": [
    611
   ],
   "sha256": "8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a"
  },
  {
   "executable": "tools/gates/register-law-gate.py",
   "resolves": true,
   "line": 409,
   "lines": [
    409,
    409,
    410,
    418,
    430,
    439
   ],
   "sha256": "15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169"
  },
  {
   "executable": "tools/gates/typed-pipeline-gate.py",
   "resolves": true,
   "line": 138,
   "lines": [
    138,
    187,
    196,
    209,
    212,
    418,
    431,
    439
   ],
   "sha256": "b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85"
  },
  {
   "executable": "tools/harness/packet_links.py",
   "resolves": true,
   "line": 452,
   "lines": [
    452
   ],
   "sha256": "66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899"
  },
  {
   "executable": "tools/harness/packet_uncertainty.py",
   "resolves": true,
   "line": 89,
   "lines": [
    89,
    128,
    501
   ],
   "sha256": "cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26"
  },
  {
   "executable": "tools/harness/r8_checks.py",
   "resolves": true,
   "line": 454,
   "lines": [
    454
   ],
   "sha256": "0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe"
  },
  {
   "executable": "tools/harness/receipt_guard.py",
   "resolves": true,
   "line": 453,
   "lines": [
    453
   ],
   "sha256": "d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1"
  },
  {
   "executable": "tools/replay-frozen.py",
   "resolves": true,
   "line": 212,
   "lines": [
    212,
    573,
    613
   ],
   "sha256": "a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464"
  },
  {
   "executable": "tools/source-audit-inventory.py",
   "resolves": true,
   "line": 614,
   "lines": [
    614
   ],
   "sha256": "f617bb99318f501db2ff51c0c180daeacf548b1a36591b1a1a80c253197b2210"
  }
 ]
}
```

## Verification (re-runnable)

```sh
#!/bin/sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/craft/box1-survey.py; echo "exit=$?"
python3 -B - <<'PY'
import json, re, hashlib, pathlib
r = json.loads(pathlib.Path("reports/round-34/craft/box1-resurvey-durable.json").read_text())
skill = pathlib.Path("SKILL.md").read_bytes()
assert hashlib.sha256(skill).hexdigest() == r["skill_sha256"], "SKILL.md moved: reading is superseded"
occ = {}
for i, line in enumerate(skill.decode().splitlines(), 1):
    for hit in re.findall(r"tools/[\w./-]+\.py", line):
        occ.setdefault(hit, []).append(i)
assert sorted(occ) == sorted(x["executable"] for x in r["rows"]), "named-executable set moved"
for row in r["rows"]:
    p = pathlib.Path(row["executable"])
    assert p.is_file() == row["resolves"] is True, row["executable"]
    assert hashlib.sha256(p.read_bytes()).hexdigest() == row["sha256"], row["executable"]
    assert row["lines"] == occ[row["executable"]], row["executable"]
    assert row["line"] == occ[row["executable"]][0], row["executable"]
print("box1-resurvey-durable: OK", len(r["rows"]), "rows at", r["skill_sha256"][:12])
PY
```


A re-run that moves `skill_sha256`, the row set, a line list, or an executable digest
means this reading is **superseded** (new file, new reading) — not that the filed JSON is
tampered with.

## Fidelity notes (what a verifier should check)

- **Row shape.** `executable` / `resolves` / `line` / `lines` / `sha256`. `line` and
  `lines` are SKILL.md line numbers at `skill_sha256`; several executables are named on
  more than one line (e.g. `tools/d2-typed-labels.py` on 19 lines,
  `tools/assemble-d4-typed.py` on 9), so `lines` is the complete list and
  `line` its first element. C01's independent row-shape design (`calib/C01-survey-run.md`)
  had not landed at this seat's reads; the keys here are a superset of the declared
  `executable/resolves/line/digest` shape (`digest` = `sha256` here) so the integrator can
  land either mapping without new measurement.
- **The survey's own limits.** `box1-survey.py` proves *resolvability* only (path strings
  → existing files); it does not run any executable, and it does not check that a named
  path is the *right* tool. It reports no per-row detail, which is why this receipt adds
  `rows` plus per-file digests.
- **The `date` field.** `survey_stdout.date` is hard-coded `2026-10-18`
  (`box1-survey.py:8`); it is the script's filing date, not the run date. The run date is
  `measured_at_utc` (2026-10-19T07:11:01Z), and the pin that carries the claim is `skill_sha256`,
  read live at `box1-survey.py:10`.
- **Supersession, not falsification.** `reports/round-30/craft/box1-landed-survey.json:4`
  records `83b0a78a…` and `reports/round-32/final-dossier.md:46` records the r32 console
  re-verify at `79fe91d3…`; both are filed and stay unedited. This receipt is the round-34
  reading at `f9bd07c2…`.
- **No in-tree runner execution.** Nothing here runs a `reports/round-*/run-validation.py`
  (F-C13-1 prevention); the only executed artifact is the read-only survey script.

## Owed

- `reports/round-34/calib/C01-survey-run.md` — C01's independent row-shape design and its
  own survey run; not on disk at this seat's reads (mission-declared sibling, not named as
  a hard dependency). Reconcile my key names against C01's before landing the JSON; the
  values need no re-measurement (both seats read the same live bytes at `f9bd07c2…`).
- Integrator-only: the landing write itself plus the pool receipt that points the promotion
  dossier's box-1 evidence at the new digest.

## Citations

- `reports/round-34/targets.json:56` (C02 mission + out path), `:5-11` (shared rules)
- `reports/round-34/claims.json:54-65` (claim C: axis, before, after_required, counting
  commands, thresholds)
- `SKILL.md` (sha256 `f9bd07c2bd134623…`, 732 lines) — lines: 673, 207, 449, 615, 139, 616, 674, 617, 35, 448, 375, 609, 450, 451, 500, 607, 608, 610, 606, 611, 409, 138, 452, 89, 454, 453, 212, 614
- `reports/round-30/craft/box1-survey.py:5-12` (pattern, live digest read, exit rule); sha256 `d923ae0fcd544513…`
- `reports/round-30/craft/box1-landed-survey.json:1-8` (filed prior receipt: `83b0a78a…`, 28/28)
- `reports/round-32/final-dossier.md:46` (r32 box-1 console re-verify at `79fe91d3…`)
- commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `sha256sum SKILL.md`; `wc -l SKILL.md`;
  `sha256sum reports/round-30/craft/box1-survey.py`; `python3 -B reports/round-30/craft/box1-survey.py`; `python3 -B` enumeration heredoc (pattern
  `tools/[\w./-]+\.py`: named set, per-path line lists, per-file sha256); `git status --porcelain`;
  `git log --oneline -3`
- scratch (not durable; the JSON is duplicated in full in this fragment):
  `.scratch/r34-c02/box1-resurvey-durable.json`, generator `.scratch/r34-c02/gen-receipt.py`
