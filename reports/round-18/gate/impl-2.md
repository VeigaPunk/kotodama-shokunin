# R18-O04 — Byte-identity of the default D2 path, and the regression battery

- round: 18 · shard: **O04** (impl, single writer of `tools/gates/typed-pipeline-gate.py`)
  · claim O `gate-generalization` (`reports/round-18/claims.json:8-14`).
- assignment (verbatim): "O R18-O03..O06 (impl x4, single writer owns the gate
  file): implement the generalization so the DEFAULT D2 path is byte-identical in
  behavior; the D4 path verifies against assemble-culture-d4.py --check output
  identity; fragments + integration evidence reports/round-18/gate/impl-{1..4}.md."
- date: 2026-10-18. Evidence window 10:18–11:2xZ. Gate before
  `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` (baseline
  revision `3dd3754`); two post-revisions were measured —
  `286d6e82…` (resolver + identity leg) and the final
  `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617`
  (profile channel + resolution line).
- canon: NON-CANON engineering evidence.
- writes: **this fragment only**; scratch under `.scratch/r18-o03/{baseline,post,post2,regress}/`
  (`export TMPDIR=$PWD/.scratch` before every scratch write). No commit, no push.
- **status: the default path is byte-identical on all four pinned invocations, at
  both post-revisions, and the battery is green.**

## 0. Verdict

The same four invocations were captured **before** the edit (`baseline/`) and
**after each revision** (`post/` for `286d6e82…`, `post2/` for `d96958b6…`), on
the same tree, and compared with `cmp -s`: every pair is byte-identical at the
same exit code. The round-11 frozen row's filed stdout pin is reproduced in both
post-revisions. `--selftest` stays 12/12. Every lane check in the regression set
exits 0, the round-11 replay reads exactly the intended cascade (typed row
`gate_digest_mismatch`, the other ten rows reproduced), and the derived round-18
re-pin manifest replays 11/11.

## 1. Method

```sh
export TMPDIR=$PWD/.scratch
mkdir -p .scratch/r18-o03/{baseline,post,post2}
# before the edit (gate sha d102fd1d…):
python3 tools/gates/typed-pipeline-gate.py                                   > baseline/default.out
python3 tools/gates/typed-pipeline-gate.py --json                            > baseline/default-json.out
python3 tools/gates/typed-pipeline-gate.py --selftest                        > baseline/selftest.out
python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml > baseline/typed.out
# after each revision (286d6e82…, then d96958b6…): the same four commands into post/ and post2/
for f in default.out default-json.out selftest.out typed.out; do cmp -s baseline/$f post/$f && echo IDENTICAL $f; done
```

This is the same comparison `reports/round-18/run-validation.py` O2 performs
independently: it builds a mirror from the baseline revision and compares
`stdout_sha256` for `default`, `json`, `frozen-row` and `selftest`.

## 2. The four invocations (before = after, at both revisions)

| invocation | exit | stdout sha256 (all sides) | verdict |
|---|---|---|---|
| `…typed-pipeline-gate.py` | 0 | `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` | identical |
| `… --json` | 0 | `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62` | identical |
| `… --selftest` | 0 | `22ce048a6528808848c737944e77dfddd370ca93f90757602eb99c0a3e640ddc` | identical |
| `… examples/culture-d2/packet.d2.typed.yml` (the frozen-row command) | 0 | `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | identical |

Receipts: `.scratch/r18-o03/baseline/*.out`, `.scratch/r18-o03/post/*.out`,
`.scratch/r18-o03/post2/*.out`; `cmp -s` per pair (10:41Z for the first revision,
11:1xZ for the final one). The frozen-row digest equals the round-11 `run.log` pin
in `tools/gates/frozen/round-11/MANIFEST.tsv` row 2 (`R11_TYPED_ROW_STDOUT_SHA` in
the validator), reproduced again after the final revision
(`regress/final-frozen-row.out`).

The default report is still `summary: 16/16 legs passed` with 15 `FINDING` lines
and 1 `NOTE` line; the `--json` document is byte-identical, i.e. the same 16
findings, `counts {"hold": 15, "note": 1, "fail": 0}`, and no `resolved` block
(that key, and the resolution line, are written only in non-default runs).

## 3. Why it is byte-identical by construction

- `resolve_config()` returns `D2_DEFAULTS` value-for-value for every D2 input, so
  `generalized` is false: no profile match is attempted against a D2 packet (no
  `assembly.generator` matches the D4 profile), no `L1-profile`, no
  `L1-assembler`, no expected-file leg, and the check train is unchanged
  (`L1-*` adapter arms, `L1-build`, `L1-schema`, `L1-routing`, `L2-channel`,
  `L3-*`, `L3-routing-consistency`, `L4-pins`).
- `resolution_line()` returns `None` and `json_document()` omits the `resolved`
  block whenever `generalized` is false — so the new reporting cannot reach a
  default run.
- The routing classification (`moved_field`) returns the same answer for every D2
  row, the L3 expected source is still the embedded constant plus the filed
  `examples/culture-d2/expected-holds.json`, and the default L4 pin dict is the
  same three keys.
- The legacy-branch prescan that reads a declaration is best-effort and swallows
  every parse failure (`document = None` → defaults), so a malformed or unreadable
  D2 packet still produces the adapter's own canonical exit-2 diagnostic, not a new
  message (design §3.4.2's guardrail, honored).

## 4. Regression battery (final revision, 11:1xZ)

| command | exit | receipt |
|---|---|---|
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 (12/12) | `post2/selftest.out` (identical to baseline) |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 (14/14) | `post2/selftest-generalized.out` |
| `python3 tools/assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-culture-d3.py --check` | 0 | `packet.json … packet.gates.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-culture-d4.py --check` | 0 | `packet.d4.yml: byte-identical deterministic assembly` |
| `python3 tools/assemble-d2-typed.py --check` | 0 | `examples/culture-d2/packet.d2.typed.yml: byte-identical deterministic typed packet` |
| `python3 tools/d2-typed-labels.py --check examples/culture-d2/typed-labels.d2.yml` | 0 | `…byte-identical deterministic projection` |
| `python3 tools/check-gate-battery.py` | 0 | `regress/final-battery.out` |
| `python3 tools/check-gate-battery.py --selftest` | 0 | `regress/final-check-gate-battery.py.out` |
| `python3 tools/check-craft-exercise.py --selftest` | 0 | `regress/final-check-craft-exercise.py.out` |
| `python3 tools/check-evidence-coupling.py --selftest` | 0 | `regress/final-check-evidence-coupling.py.out` |
| `python3 tools/replay-frozen.py --selftest` | 0 | `regress/replay-selftest.out` |
| `python3 tools/assemble-d2-typed.py --selftest` | 0 | `regress/final-assemble-d2-typed.py.out` |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | 2 (the intended cascade) | 10 reproduced + row 2 `could-not-evaluate reason=gate_digest_mismatch` (`regress/replay-round11-post.out`) |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | 0 | 11/11 reproduced, row 2 pinned on the live gate `d96958b6…` |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv` | 0 | 2/2 reproduced (`regress/replay-round18-frozen.out`) |

The round-11 replay reading is the one the validator's O4 leg demands for a
changed gate: the typed row must **stop** reproducing and read
`could-not-evaluate/gate_digest_mismatch` while every other row still reproduces.
`tools/replay-frozen.py` needs a mirror root outside the repo; the in-repo
`.scratch` root is refused by design (`mirror_unsafe`), so the replay receipts
were produced with `env -u TMPDIR`.

## 5. The one measurement that had to change a rule (and did not touch D2)

The lane's YAML-subset reader reads an unquoted `null` as the **string** `"null"`
(measured: `load_packet_strict("a: null\n")` → `'null'`), so a D4 on-channel
routing row (`off_channel_field: null`) would have been classified as moved and
would have failed `L2-channel` on its own retention line. `moved_field()` treats
`null`/`none`/`~`/empty as "no field moved". For D2 every row carries a real field
name, so the rule is a no-op there — proven by §2's byte-identical streams.

## 6. Compliance

Writes: this fragment (plus `impl-1/3/4.md`), scratch under `.scratch/r18-o03/**`,
and the two tool files this shard owns (`impl-1.md` §5 records their before/after
digests). No commit, no push, no filed byte edited.
