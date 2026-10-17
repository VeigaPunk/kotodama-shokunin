# supplement-opencode-1 — 03 EXECUTOR: D2 assembler (`tools/assemble-d2.py`)

Role: implementation (EXECUTOR, child of the supplement lane). Baseline revision
`fe34faaafbe0add59ff68827a0df6c5782a72404`. Working tree at start of work was clean
except `reports/`.

Files touched: `tools/assemble-d2.py` (only). `examples/culture-d2/packet.d2.yml` was
**not** regenerated (parent owns that); no component, gate, corpus or frozen artifact
was modified. No corpus erratum was needed: every change below is assembler metadata
or an error path, and no historic flag or source record was rewritten.

## 1. `--selftest` added (operability)

Interface: `python3 tools/assemble-d2.py [--check | --selftest]` — `--check` is
unchanged and mutually exclusive with `--selftest`. The selftest copies the script
under test and the reader into a `tempfile.TemporaryDirectory`, writes a nine-file
fixture component tree (02/03/05/06/07/08/09/11/13), and drives the **real CLI** by
subprocess with `cwd` set to the temp root, so exit codes are the shipping exit codes.

Controls (deterministic, no network, no absolute or traversal input paths):

| control | expectation | observed |
|---|---|---|
| positive: CLI assemble ×2 | exit 0, "Wrote", identical bytes | pass |
| `--check` on clean output | exit 0, "byte-identical" | pass |
| structural: 19 packet keys, coda/onset override, 06-then-07 roles/motifs, `source_era_dates` as declared, `formation` stems `su+nel`/`su` verbatim, 03 `derivation_rules` present, each stem replays through its declared rule to the record's `name`, all 9 source digests recorded and matching, reader digest, generator name, no stale derivation-hold note | all | pass |
| tamper: one changed vowel in 02 | `--check` exit 1, "differs" | pass |
| restore fixture | `--check` exit 0 | pass |
| duplicate record IDs (two `L-01`) | exit 2, "duplicate record IDs" | pass |
| incomplete record (drop `layer`) | exit 2, "incomplete record" | pass |
| duplicate top-level `lexicon:` | exit 2, "exactly one top-level" | pass |
| empty block (`lexicon:` no records) | exit 2, "no usable records" | pass |
| wrapper instead of ledger (`lexicon:` mapping) | exit 2, "expected list" | pass |
| malformed block (`name sunel` without colon) | exit 2, "YAML subset parse error" | pass |
| missing component (13 deleted) | exit 2, message names the file | pass |

Observed: `selftest: 42/42 checks passed` (exit 0). `ls -d /tmp/assemble-d2-selftest-*`
→ no leftovers.

Two error paths were repaired so the negative controls are exit-2 rather than an
uncaught traceback: the reader's `Malformed` is mapped to `ValueError` in a
`reader_parse()` wrapper (a malformed block previously escaped `main()`'s
`except (ValueError, OSError)`), and `extract()` now reports a missing block key as
`"<key> has no usable records"` instead of `KeyError`. Neither weakens a gate; both
only convert crashes into the documented exit 2.

## 2. Stale assembly metadata removed (evidence)

Removed from `assembly.unresolved`:

> "03 morphology has no derivation_rules adapter for 05 UP-COMPOUND; naming replay remains held"

Disproved by three rechecks at the pinned baseline:

1. `03-morphosyntax.yml` (revision 1.1, baseline bytes) now carries
   `morphology.derivation_rules` with 8 rules including
   `UP-COMPOUND: ^(?P<B1>[a-záéíóú]+)[+](?P<B2>[a-záéíóú]+)$ → {B1}{B2}` (line 159–169).
2. `13-naming.yml` (revision 1.1) supplies the full serialized input:
   `formation: {stem: su+nel, bases: [su, nel], rule: UP-COMPOUND, expected: sunel}`
   for NM-01..NM-08; the string `su+nel` is present in the committed packet (1 hit).
3. The naming gate replays it: `tools/gates/frozen/round-3/naming-collision-gate.out`
   has **8 DERIV-HOLD** findings; `tools/gates/frozen/round-4/naming-collision-gate.out`
   and a live run against the committed packet both have **0 DERIV-\*** (round-4 totals:
   6 NAME-NEAR, 1 PHON-CODA, 10 PHON-INVENTORY, 1 CROSS-HOLD = 18).

## 3. Assembly metadata added (justification)

- `normalizations` +: "03 morphology.derivation_rules and 13 formation records ride
  through verbatim; the assembler rewrites no rule, stem or affix, and naming gate C
  replays the B1+B2 stems". True by construction (`take()` copies whole blocks) and
  asserted by the selftest's replay checks.
- `unresolved` +: "13 cross_culture_review (status unresolved, languages []) is not
  exported into this packet, as 13's own assembly_gap records; CROSS-HOLD is expected,
  not cleared." This preserves an explicit source-declared gap that the manifest
  previously omitted. Exporting the block was **not** done: it would change packet
  schema, and 13 declares `status: unresolved` with no bounded sweep, so CROSS-HOLD
  stands either way. Parent decision if export is wanted.

## 4. Isolation proof (my delta only)

Because sibling workers edited `06-pantheon.yml`/`07-myths-motifs.yml` mid-run
(PAN-03 `Humweha` → `Humaweha`, mtimes 12:38), the live diff against the committed
packet is not attributable to me. Re-run on **baseline bytes** fetched with
`git show fe34faa:<path>` (9 components + reader) in a `mktemp -d` tree:

- head region (everything before `assembly:`) is byte-identical to the committed
  packet;
- the entire diff is 3 lines: the removed stale line, the 2 added lines above;
- the temp tree's own `--check` reports "byte-identical deterministic assembly".

Consequence for the parent: the committed packet is now stale twice over (my metadata
plus the in-flight 06/07 repair), so `python3 tools/assemble-d2.py --check` correctly
exits 1 on the repo copy until the packet is regenerated; after regeneration it must
exit 0.

## 5. Battery re-run after the change

All seven registered gate selftests, `--selftest`, exit 0:

```
costume-era-consistency-gate.py 0 | handoff-packet-check.py 0 | lexicon-coverage-audit.py 0
myth-consistency-gate.py 0 | naming-collision-gate.py 0 | phonology-sanity-gate.py 0 | provenance-audit.py 0
```

Regenerated-packet smoke test (temp tree, current components, 12:39):
naming exit 1, 17 findings (6 NAME-NEAR, 10 PHON-INVENTORY, 1 CROSS-HOLD; PHON-CODA is
gone because the sibling PAN-03 repair has landed in 06/07 — observed, not my change);
costume-era exit 0; myth exit 0; lexicon-coverage exit 0; phonology exit 1 with 3
A-NEUTRAL REVIEW findings that are also present on the committed packet (pre-existing,
from 02's `notable_rules`, unrelated to this work). `handoff-packet-check.py` takes a
Markdown handoff document, not this YAML packet (HO-DATA HOLD on `packet.d2.yml`); its
selftest passes. No gate reads the `assembly` block programmatically (the string hits
in the costume gate are fixture prose "guild assembly"), so the metadata edit cannot
move any finding.

## 6. Replay constraints not safely fixed here

1. `03-morphosyntax.yml` still ships its own stale line, `derivation_contract.unresolved`:
   "13 currently supplies only B1 as formation.stem for NM-01..NM-08, although bases
   contains both inputs" — disproved by 13 revision 1.1, but 03 is outside my write
   scope. It reaches the packet verbatim through `morphology`; the 03 owner should
   correct it (a metadata fix cannot remove source text).
2. Two genuine, unresolved derivation constraints remain untouched: 05's AGENT
   mass-base exclusion vs. the held-out `pal > palin` test (lexical-owner review), and
   03's note that combining two contrastive accent peaks is unspecified.
3. Exporting `13.cross_culture_review` (see §3) is a schema change left to the parent;
   the naming gate's CROSS-HOLD remains regardless.

## 7. Command log

```
python3 tools/assemble-d2.py --check                      # baseline: exit 0, byte-identical; sha256 d5fb4088… (matches claims.json)
for g in tools/gates/*.py; do python3 "$g" --selftest; done # baseline: all 7 exit 0
python3 tools/assemble-d2.py --selftest                  # after change: exit 0, 42/42 checks passed
python3 tools/assemble-d2.py --check                     # after change, live repo: exit 1 "differs" (expected until regeneration)
# isolation (mktemp -d; git show fe34faa:<9 components + reader>; new script) → temp --check exit 0; diff vs committed = 3 assembly lines
# regenerated-packet smoke (mktemp -d; live components)   → gates as reported in §5
grep -o "FINDING DERIV-[A-Z]*" tools/gates/frozen/round-3/naming-collision-gate.out | sort | uniq -c   # 8 DERIV-HOLD
```

No commit, push, LOG, SCORECARD, SKILL, packet regeneration or sibling write was
performed. All children of this lane remain author-side evidence; no SHENEN mark and
no rank claim is made.
