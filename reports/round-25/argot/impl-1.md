# R25-D05 — argot-derivation leg, impl 1 of 6: the host decision and the replay core

- **Seat:** R25-D05 (argot impl 1 of 6; the integrator for the touched files),
  round 25, loop 3 build 1 of 4 (`devin/deepseek-v4-1-flash-high`), claim **D**
  `argot-derivation-check` (`reports/round-25/claims.json:20-27`).
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD at write time `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **Write scope:** `tools/gates/argot-derivation-gate.py` (new),
  `tools/gates/fixtures/argot-derivation-gate.{yml,expected}` (new), the
  round-25 binding of the leg inside `tools/gates/typed-pipeline-gate.py`, and
  this fragment set `reports/round-25/argot/impl-{1..6}.md`. Scratch under
  `.scratch/r25-d05/` (`TMPDIR=$PWD/.scratch` preceded every scratch write).
  No filed round-8–24 byte, no packet, no component, no pin file touched; no
  commit, no push.
- **Canon:** NON-CANON engineering evidence.

## 1. Where the leg lives, and why

The claim's `after_required` says "the D4 typed gate grows the leg with selftest
controls". Three candidate hosts were examined before choosing:

| host | verdict |
|---|---|
| `tools/d2-typed-labels.py` | **rejected** — byte-pinned (`projector_sha256 2819f687…`) in `typed-pipelines.json`, in `examples/culture-d4/expected-holds.json`, and in `tools/gates/frozen/round-22/d4-repin/freeze-receipt.json`. An edit moves a filed pin and collides with the concurrent O-workers' re-pin cascade. |
| `tools/gates/naming-collision-gate.py` | **rejected** — the `DERIV-REPLAY`/`DERIV-HOLD` classes are the *name-formation* leg over `names`, and the gate's committed fixture pins its finding set (`fixtures/naming-collision-gate.expected`, 11 ids). A new class there changes the selftest's pinned counts. |
| `tools/gates/typed-pipeline-gate.py` | **chosen for the binding**, as a *call* to a sibling — not as the semantics owner. |

So the leg's **semantics** live in a new flagless sibling,
`tools/gates/argot-derivation-gate.py`, and the typed gate **invokes** it with
the same single input. This is the same shape the lane already uses for the two
D4 adapters (`d4-typed-labels-check-gate.py` calls `tools/d2-typed-labels.py` by
path and forwards its verdict), and it keeps the sibling freezable by
`tools/replay-frozen.py`, which launches `[python3, <gate>, <input>]` — one path,
no flags.

The sibling is **not** a re-implementation of the naming gate's replay kernel: it
loads `tools/gates/naming-collision-gate.py` read-only by path (`runpy`) and
calls its `load_yaml`, `_match_with_budget`, `_catastrophic_pattern`,
`_template_problem` and `_MatchBudgetExceeded`. Its live digest is printed on
every run, so a reader can tell which bytes the replay used:

```
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

## 2. What the leg replays

Three sources of rule, tried in order, so the packet's own declared inputs are
what get replayed:

1. **the two declared argot operations**, whose algorithms are fixed by
   `reports/round-17/d4/design-language.md` §5 and embedded here as an explicit
   table: `head2` (first two syllables, **maximal-onset**) and `reverse`
   (character-level string reversal);
2. **a packet `morphology.derivation_rules` entry** whose `id` is the declared
   rule, replayed through its machine-readable `pattern`/`output` pair — the
   SKILL's "machine-readable pattern/output pairs" requirement
   (`SKILL.md:209`), executed with the naming gate's own budgeted matcher;
3. **the packet's own `formation` idiom** (`formation: {stem: …, rule: …}`),
   which states the same relation in the vocabulary the delivered packets
   actually use;
4. **the borrow-adaptation relation** for a register-scoped loan: the declared
   layer's `substitutions` applied to the record's own `donor_form`.

Every replay is a text comparison of the replayed string against the delivered
form, NFC-normalized. The report prints one coverage line naming the counts and
one dependency line naming the kernel's digest.

## 3. Measured

Command, date, and result (2026-10-18, lane root, `TMPDIR=$PWD/.scratch`):

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit 0
```

The six `register_scoped` records are the six loans `L-49..L-54` (reachable via
`loan_layer` → `layers[*].register`); all six adaptations replay; the eight
`claimed_chains` are `NM-01..NM-08`'s `formation` records against `CX-01`; zero
violations on the delivered tree. `derived_pairs=0` is the forecast's own gap and
is the subject of `impl-3`.

## 4. Controls carried by this fragment

- **positive:** the live D4 source run exits 0 with 0 violations (§3).
- **negative:** see `impl-4` (the fixture's four planted violations) and
  `impl-5` (the typed-gate binding's teeth).
