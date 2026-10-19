- Seat: D05 | verifier | claim D | date 2026-10-19 | baseline 9bccc9b

# D05 — independent isolated verification of D03 (claim D: register residue)

## 0. Status of the artifact under verification

**D03's fragment does not exist at seat close.** `find reports/round-38 -type f`
returns exactly four files — `claims.json`, `targets.json`,
`telemetry/availability-attempt-1.json`, `telemetry/dispatch-declared.json`. No
`depth/` directory exists. `reports/round-38/run-validation.py` does not exist
either (`ls` → No such file or directory), so claim D's third declared counting
command is `to-verify` regardless of what D03 lands.

I therefore **cannot verify D03's result**. What I *can* do, and did, is verify
the claim's own premises independently and build the falsifiable control set that
D03's landing must flip. That is the honest scope of this fragment: it is a
**pre-verification harness plus an independent reproduction of the `before`
state**, not a verdict on D03. The verdict on D03 is owed.

## 1. Method — isolation, per F-C13-1

No `reports/round-*/run-validation.py` was executed in-tree or at all. Every
control ran in a fresh `git archive HEAD | tar -x` copy under
`.scratch/d05/iso{,2,3,4}` (gitignored). The base copy reproduces the tree
exactly: `python3 -B tools/assemble-culture-d4.py --check` → `packet.d4.yml:
byte-identical deterministic assembly`, exit 0, and the packet sha256 is
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` — the same
digest the filed r36 scout pinned. The isolated copy is therefore
indistinguishable from the lane root for this claim.

## 2. Claim D's `before`, independently reproduced

Claim D's `before` has two halves. Both reproduce.

### 2.1 F-6 — no emitter for `derived_forms` / `derived_ok`

```
$ for t in derived_forms derived_ok derived_pairs; do
    examples=$(grep -rl "$t" examples/ | wc -l); tools=$(grep -rl "$t" tools/ | wc -l)
    reports=$(grep -rl "$t" reports/ | wc -l); ...
derived_forms    examples=0 tools=0 reports=28
derived_ok       examples=0 tools=0 reports=28
derived_pairs    examples=0 tools=2 reports=142
```

Confirmed: zero hits in `examples/` and `tools/`; the 28 `reports/` files are
filed prose only. The two keys occur 0 times in each delivered artifact —
`packet.d4.yml`, `typed-labels.d4.yml`, `packet.d4.typed.yml` (grep -c → 0/0/0).

The contract the keys must satisfy is `reports/round-17/d4/design-brief.md:306-307`:
*"the coverage block reports `derived_forms` and `derived_ok` counts that agree."*
The live gate prints `derived_pairs`/`violations` instead
(`tools/gates/argot-derivation-gate.py:917-921`) — a different key set, as
`reports/round-25/argot/delta.md:255` recorded. The natural producer site is the
projection's coverage block, emitted at `tools/d2-typed-labels.py:2879-2894`
(`coverage = {...}` with `typed_labels`, `labels_by_kind`, …). **No gate validates
the projection's coverage keys** (`grep -n "labels_by_kind" tools/gates/*.py` →
no hits), so F-6 is a *new key pair plus a producer*, exactly as K01 r36 said.

**Vacuous-pass hazard (named for the threshold "no vacuous-pass"):** if D03 lands
the two keys by emitting `derived_forms`/`derived_ok` as constants, the coverage
block would "report counts that agree" with nothing behind them. The non-vacuous
floor is measurable: the packet carries **8** `derived_from:` records and the
argot leg reports `derived_pairs=8` — so a correct emitter must print
`derived_forms=8`, and the pin cascade must make the number load-bearing. A
`0/0` emission is a vacuous pass and must be rejected.

### 2.2 RL-8 — the era leg is unimplemented

Two mechanisms are missing, and they are missing in different gates:

- **The argot gate has no era concept at all.** `grep -n "stage\|era\|E0\|E1"
  tools/gates/argot-derivation-gate.py` returns only prose/docstring hits — no
  code path reads a record's `stage`, the `eras` block, or `available_from`.
- **The law gate reads `kind: era` as a vocabulary token only.**
  `tools/gates/register-law-gate.py:121` puts `era` in `DECLARED_KINDS`, but
  `grep -n "available_from\|E0\|stage" tools/gates/register-law-gate.py` → **no
  hits**. It never grades dating. RGL-05's own text declares this:
  `examples/culture-d4/components/13-register-law.yml:57` — *"no gate executes
  these rows. The era leg (RGL-05) is specified and unimplemented."*

The defect RGL-05 names is at `13-register-law.yml:49`: *"every stamp form is
available_from E1 … an E0 stamp claim is a defect."*

## 3. The era control suite — and a finding that narrows the claim

I built four isolated controls. The result matters for adjudicating D03: **era
blindness is real, but one delivered gate already catches one shape of the
defect**, so D03 must show the era leg firing on the *residual* shape or the
claim's `after_required` ("the era leg runs") is weaker than filed.

| # | control (isolated copy) | command | observed |
|---|---|---|---|
| C1 | `L-55` stage `E1→E0`, legitimate reassembly | `lexicon-coverage-audit.py packet` | **exit 1** — `FINDING D-stage-mismatch: 'tuum' is formed in 'E0' but construction 'STAMP-LENGTHEN' is only available from 'E1'` |
| C2 | as C1 + `construction` dropped | `lexicon-coverage-audit.py packet` | exit 1 — `D-rule-underspecified` (different finding; not the era leg) |
| C3 | as C1, argot + law legs | `argot-derivation-gate.py`, `register-law-gate.py` | **exit 0, findings=0** on both — era-blind |
| C4 | as C1 **+ `STAMP-LENGTHEN.available_from` widened to `E0`** | `lexicon-coverage-audit.py packet` | **exit 0, silent** |

**Reading, no more and no less.** C1 shows `lexicon-coverage-audit.py` fires
`D-stage-mismatch` on an E0-dated stamp form — but the finding is driven by
*construction availability* (`tools/gates/lexicon-coverage-audit.py:846-867`,
`available_from` vs the entry's `stage`), not by RGL-05's register law. C4 is the
isolating step: widen the availability window and the same E0-stamp defect
becomes **invisible to every delivered gate** — coverage audit silent, argot leg
silent (C3), law leg silent (C3). So the RGL-05 substance ("an E0 stamp claim is
a defect", independent of whether the construction window happens to disagree)
has **no grader**.

Two consequences for D03:

1. A D03 "era leg" that merely relies on `D-stage-mismatch` is **not the era
   leg** — it is a construction-availability check that already exists and would
   have fired anyway. The era leg must grade the *register-era* relation
   (`stage` vs the register's declared `available_from E1`), which C4 proves is
   currently ungraded.
2. The control D03 must ship is C4-shaped (or stronger), not C1-shaped. A C1-shaped
   control would pass vacuously against work already done.

## 4. Baseline readings the landing must not regress

All at HEAD `9bccc9b`, in-tree and in the isolated copy (identical):

```
argot-derivation-gate.py packet.d4.yml   exit 0  records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
register-law-gate.py     packet.d4.yml   exit 0  law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0
typed-pipeline-gate.py   packet.d4.yml   exit 0  summary: 20/20 legs passed (ok L3b-argot, L3-counts, L3-baseline, L4-pins)
argot-derivation-gate.py --selftest      exit 0  selftest: 27/27 checks passed
register-law-gate.py     --selftest      exit 0  selftest: 45/45 checks passed
lexicon-coverage-audit.py --selftest     exit 0  selftest: 14/14 checks passed
assemble-culture-d4.py   --check         exit 0  packet.d4.yml: byte-identical deterministic assembly
exercise-handoff-e2e.py  --profile v3 --quiet  exit 0  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

The r7 default chain is unchanged (`45f57132…`) and the pinned
`reports/round-34/handoff/declared-in-r7/expected.json` sha256 is
`bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55` — matching
K01 r36's pin. No freeze byte moved.

**Non-vacuity check on the existing coverage:** the argot leg's pass is *not*
vacuous — `derived_pairs=8` matches 8 `derived_from:` records in the packet, and
`register_scoped=14` is non-zero. Any D03 landing that moves these to zero, or
that makes the new keys agree by both being zero, is a vacuous pass.

## 5. What D03's landing must satisfy (the harness)

When `depth/D03-isolated.md` lands, verification against this fragment requires
**all** of:

1. A C4-shaped control: E0-dated stamp form with the construction window widened
   still produces a finding from the new era leg. C1/C2-shaped controls do not
   count.
2. The new era leg's selftest has ≥2 controls (fires on the defect; green on the
   delivered packet), and the selftest count is stated before→after.
3. `derived_forms`/`derived_ok` are emitted **non-vacuously** — `derived_forms`
   equals the packet's derived-record count (8 at baseline) and `derived_ok`
   equals the leg's non-violating count, not a constant 0/0.
4. Every §4 baseline reading holds unchanged; `argot`/`law`/`typed` legs still
   exit 0 with the same counters.
5. The r7 packet pin stays `45f57132…` and the two named artifacts
   (`tools/gates/argot-derivation-gate.py`, `tools/gates/register-law-gate.py`
   or the D01/D02-named equivalents) are the **only** changed files; filed bytes
   untouched.

## Owed

- **D03 verification.** `depth/D03-isolated.md` absent at seat close; the verdict
  on D03 is owed to the integrator/reviewer (R01). Owner: whoever re-runs after
  D03 lands, against §5.
- **`reports/round-38/run-validation.py`.** Does not exist; claim D's third
  counting command is `to-verify`. Owner: integrator. Per F-C13-1 it must not be
  run in-tree regardless.
- **F-6 key agreement semantics.** "counts that agree" (`design-brief.md:306-307`)
  is read here as `derived_ok == derived_forms` over the delivered set; the
  original round-17 author is not available to confirm, so the reading is
  `to-verify` and D03's own design (D01) should state which reading it implements.
- **RL-8 ownership.** Filed owner is "whoever grows the leg"
  (`reports/round-27/law/impl-8.md:68`); the era leg's gate placement (argot gate
  vs a new leg vs the law gate) is D02's design decision, not this seat's.

## Citations

Files (sha256 measured 2026-10-19, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287  tools/gates/lexicon-coverage-audit.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
```

Commands (all from lane root or an isolated `git archive` copy, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
git archive HEAD | tar -x -C .scratch/d05/iso{,2,3,4}          # isolated copies, HEAD 9bccc9b
python3 -B tools/assemble-culture-d4.py --check                # exit 0, byte-identical
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml          # exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml              # exit 0, findings=0
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml            # 20/20
python3 -B tools/gates/argot-derivation-gate.py --selftest                                  # 27/27
python3 -B tools/gates/register-law-gate.py --selftest                                      # 45/45
python3 -B tools/gates/lexicon-coverage-audit.py --selftest                                 # 14/14
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet                               # exit 0, 45f57132…
# C1..C4: L-55 stage E1->E0 (+ STAMP-LENGTHEN available_from -> E0 for C4), reassemble, rerun legs
for t in derived_forms derived_ok derived_pairs; do grep -rl "$t" examples/ tools/ reports/; done
grep -n "stage\|era\|E0\|E1" tools/gates/argot-derivation-gate.py                           # prose only, no code path
grep -n "available_from\|E0\|stage" tools/gates/register-law-gate.py                        # no hits
grep -n "labels_by_kind" tools/gates/*.py                                                   # no hits
find reports/round-38 -type f                                                               # 4 files, no depth/
```

Source lines cited: `reports/round-17/d4/design-brief.md:296-309`;
`reports/round-17/d4/design-language.md:186-219`;
`reports/round-25/argot/delta.md:255`; `reports/round-26/register/rules.md:128`;
`reports/round-27/law/impl-8.md:68`; `reports/round-36/scout/K01-register-scout.md:115,210`;
`reports/round-36/depth/D06-gap-fill.md:226-249`;
`examples/culture-d4/components/13-register-law.yml:49,57`;
`examples/culture-d4/components/04-lexicon.yml:98,110,118,238`;
`tools/gates/argot-derivation-gate.py:917-921`;
`tools/gates/register-law-gate.py:121`;
`tools/gates/lexicon-coverage-audit.py:846-867`;
`tools/d2-typed-labels.py:2879-2894`.
