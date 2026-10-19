- Seat: D01 | executor (claim D, F-6 counter emitter design) | date 2026-10-19 | baseline 9bccc9b

# D01 — the F-6 counter emitter: the pair, the domain, and the consumer

**Mission (binding, `reports/round-38/targets.json` seat `D01`):** "Design the F-6
counter emitter (fenced patch draft): shape, consumers, where it lives."

**Write scope.** `reports/round-38/depth/D01-f6-design.md` only. Every mutation ran
inside a `git archive 9bccc9b` copy at `.scratch/d01/` (gitignored); the live tree
was never written (`git status --porcelain` at the stamp: `?? reports/round-38/`
only, `HEAD 9bccc9b`). No commit, no push, no install, no network. No
`reports/round-*/run-validation.py` was executed anywhere, in-tree or in a copy
(F-C13-1); no `--freeze` of `reports/round-34/handoff/declared-in-r7`.

**Stamp.** `date -u +%FT%TZ` → **2026-10-19T11:14:28Z**; `git rev-parse --short HEAD`
→ `9bccc9b`. Every command ran with `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1` from the lane root or from the isolated copy.

**Canon.** NON-CANON engineering evidence. A digest is integrity, never truth, never
clearance.

---

## 0. Headline

Three findings, each measured, and the first two change what the D block must land:

1. **The formula the block converged on is wrong in general.** P01 §3.1, D08 §2.1 and
   D04 §3.1 all draft `derived_ok = derived_pairs - violations`. `violations` is the
   gate's *shared* failure total: it is incremented at **five** sites across **three**
   classes — derivation (`:571`, `:587`), claimed-chain (`:619`, `:626`) and borrow
   (`:652`). K01 §8 owed exactly this ("the draft's `derived_ok = derived_forms` assumes
   `violations == 0`, which is true over the delivered packet and false in general. An
   honest emitter must read the violation count from the replay. **Owner: the D executor
   (D01)**"). Measured: a control with one claimed-chain failure and one borrow failure
   reads `derived_pairs=2`, `violations=3`, so the drafted formula emits **`derived_ok=-1`**.
2. **The consumer must be the argot gate's own selftest, and that is forced, not chosen.**
   `evaluate_text` returns `EXIT_CLEAN if not findings else EXIT_FINDINGS` (`:709`; `:723`
   in the patched revision), so a
   *finding* that reports a coverage disagreement would turn the live D4 packet red and
   break the typed pipeline's `L3b-argot` leg. A selftest control is the only host that
   reads the counters without changing any exit code. This also settles D10b §4's
   "and/or" — the argot selftest is the host; the `L3b-argot` sub-assertion is not.
3. **Zero pins move, and the r7 threshold pin is verified unchanged** — so the emitter's
   host decision (argot gate, not the projector) is now verified from a second direction
   than D03/D04's.

The patch is **one** gate file plus its selftest; no packet, component, projection, pin or
filed byte moves.

---

## 1. The shape — what the two counters are

F-6 is `reports/round-17/d4/design-brief.md:306-307`: *"the coverage block reports
`derived_forms` and `derived_ok` counts that agree"*, re-measured at
`reports/round-25/argot/forecast.md:37`. The domain is the gate's own derivation class,
which the module docstring already defines ("three sources of rule, tried in order"):
the declared argot operations, a packet `morphology.derivation_rules` entry, and a
borrowed record's layer substitutions.

| counter | definition | source |
|---|---|---|
| `derived_forms` | every record carrying a `derived_from`/`derivation` pair | `counters["derived_pairs"]` (`:567`) |
| `derived_failures` | the subset of those whose declared chain does not replay | **new** counter, incremented at `:571` and `:587` |
| `derived_ok` | `derived_forms - derived_failures` | the pair's clean condition is `derived_ok == derived_forms` |

`derived_forms` is the pair's *domain* and `derived_ok` its *pass count*; the "agreement"
the forecast names is `derived_failures == 0`, i.e. `derived_ok == derived_forms`. On the
delivered packet that is `8 == 8`; on the gate's own committed fixture it is `8 != 5`.

### 1.1 Why the shared total cannot be the source — the measurement

`violations` is not the derivation failure count. Its five increment sites:

```
:571   op in OP_FUNCTIONS, replay mismatch          -> D4L-ARGOT-DERIV (derivation)
:587   op in rules, replay_rule verdict is False    -> D4L-ARGOT-DERIV (derivation)
:619   claimed formation rule, replay verdict False -> D4L-ARGOT-DERIV (claimed-chain)
:626   claimed formation rule not among the packet's rules -> D4L-ARGOT-DERIV (claimed-chain)
:652   borrowed record, layer substitution mismatch -> D4L-ARGOT-DERIV (borrow)
```

The committed fixture proves the divergence is not hypothetical. Its own expected id
census is `FIXTURE_EXPECTED = {"D4L-ARGOT-DERIV": 4, "D4L-ARGOT-RULE": 1}` (`:733-736`),
and its line is:

```
coverage: tools/gates/fixtures/argot-derivation-gate.yml records=14 register_scoped=11 \
  derived_pairs=8 claimed_chains=0 borrow_pairs=3 violations=4 rule_holds=1
```

`violations=4` = **3** derivation failures (`Q-11 saalum`, `Q-12 kin`, `Q-13 suk`) + **1**
borrow failure (`B-03 gal`). The block's drafted formula emits `derived_ok=4`; the honest
count is **5**. One integer of drift on the gate's own fixture.

### 1.2 The control that makes the wrong domain unmissable

A synthetic control with one claimed-chain failure and one borrow failure, and no
derivation failure at all (`TWO_MIXED_CONTROL`, §4):

```
derived_pairs=2  claimed_chains=1  borrow_pairs=1  violations=3
  FINDING D4L-ARGOT-DERIV: FAIL — form Q-03 'bad' ... claimed formation 'UP-COMPOUND' ...
  FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-02 'wrong' ...
  FINDING D4L-ARGOT-DERIV: FAIL — register-scoped loan B-01 'res' ...
```

`derived_pairs - violations` = `2 - 3` = **-1**. A negative pass count is not a rounding
disagreement; it is the wrong domain. The corrected emitter emits
`derived_forms=2 derived_ok=1` on the same control.

**Scope note, recorded rather than smoothed.** This is a *narrower* domain than
`derived_forms`. `derived_pairs` (`:567`) is inside the `derivation is not None` branch and
`continue`s before the claimed-chain and borrow branches, so the two classes are mutually
exclusive per record and no record is double-counted. The alternative reading — count every
`D4L-ARGOT-DERIV` failure regardless of class — is a *different* contract (F-6's
`design-brief.md:303` names the `derived_from` + `derivation` pair, F-3), and it is not
this seat's to choose. It is listed in §7 as a contract question, not absorbed.

---

## 2. The consumer — where it lives, and why it is forced

F-6's threshold is "the new coverage named (no vacuous-pass)", and D10b's independent
verdict is that at `9bccc9b` **no consumer reads the counters on either route** (D10b §2:
the `L3b-argot` leg keeps only `line.startswith("FINDING D4L-ARGOT-")`, `typed-pipeline-gate.py:530-531`;
D10b §3: the projection's byte-identity check accepts a lying value, measured with
`"derived_forms": 999`). A key-only emitter is a vacuous pass.

D10b §4 names two candidate hosts: "a new `check(...)` in
`tools/gates/argot-derivation-gate.py --selftest` (Route A, self-contained, no new file),
**and/or** as an `L3b-argot` sub-assertion in `tools/gates/typed-pipeline-gate.py:539`".
**The "and/or" is not a free choice**, and the measurement that settles it is one line:

```
tools/gates/argot-derivation-gate.py:709      (baseline)   ;  :723 in the patched revision
    return (EXIT_CLEAN if not findings else EXIT_FINDINGS), findings, totals
```

The gate's exit code is a pure function of its finding list. So an F-6 *finding* that
reports a coverage disagreement would fire on any packet whose derivation class has a
failure — including the gate's own committed fixture (4 FAILs already) — and, more to the
point, it would make the gate's verdict depend on its own counters. On the delivered D4
packet the pair agrees, so a finding-based guard would be silent there; but the design
would then be unfalsifiable on the delivered tree and would change the gate's contract
from "replay the derivations" to "assert a counter relation". A **selftest control** reads
the counters, asserts the relation, and moves no exit code.

**The second host is also foreclosed, by pin cost.** `tools/gates/typed-pipeline-gate.py`
is **not** a member of the r7 read set (`reports/round-34/handoff/declared-in-r7/expected.json#inputs`
has 58 members; the only `tools/gates/*` members are `costume-era-consistency-gate.py`,
`d4-assembly-check-gate.py`, `d4-typed-labels-check-gate.py`, `handoff-packet-check.py` —
measured in the citation block's final command), so editing it is not forbidden. But it is
the *pipeline* gate: widening its
`L3b-argot` check to consume the counters would make the pipeline's verdict depend on the
argot gate's counters, and the r7 `expected.json`'s L3b rows would then need re-pinning in
the same edit set. The selftest host costs nothing and is where the gate's own controls
already live (27 of them at baseline).

**Where the pair is materialised.** Not at the print. `evaluate_packet` returns
`(findings, counters, declared_ops)` and `evaluate_text` accumulates the counters into
`totals`, so the pair is stored in `counters` (`:672-673` in the patched revision) and
printed from `totals` at the coverage line. A consumer can therefore assert it; a print-time
expression could not (this was measured — the first prototype put the pair only in the
print, and all six consumer controls failed, §4.1).

---

## 3. The fenced patch (integrator applies; this seat wrote no tool byte)

Applies to `tools/gates/argot-derivation-gate.py`. Patched file: 928 → **1063** lines,
sha256 `8c7dd098d9ac76a1702ad920bedd80402960816dee64a066f7ceb5616cbdef07`
(from `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`). The applier
used for every measurement is at `.scratch/d01-apply.py` (scratch, not promoted); it
asserts each anchor matches exactly once, so a moved anchor fails loudly rather than
patching the wrong site.

```diff
--- tools/gates/argot-derivation-gate.py	2026-10-18 16:31:37 -0300
+++ tools/gates/argot-derivation-gate.py	2026-10-19 08:16:20 -0300
@@ -565,10 +565,17 @@
             if derivation is not None:
                 op, base = derivation
                 counters["derived_pairs"] += 1
+                # F-6 (reports/round-17/d4/design-brief.md:306-307) needs the
+                # derivation class counted on its own. The shared `violations`
+                # total also counts claimed-chain (:626) and borrow (:652)
+                # failures, so `derived_pairs - violations` is NOT the
+                # derivation pass count. K01 section 8 owed this decision and
+                # reports/round-38/depth/D01-f6-design.md measures it.
                 if op in OP_FUNCTIONS:
                     replayed = apply_op(op, base)
                     if norm(replayed) != norm(form):
                         counters["violations"] += 1
+                        counters["derived_failures"] += 1
                         findings.append(finding(
                             "D4L-ARGOT-DERIV", "FAIL",
                             "register-scoped form %s %r (register %r): declared chain %r applied to "
@@ -585,6 +592,7 @@
                             % (eid, form, op, detail)))
                     elif verdict is False:
                         counters["violations"] += 1
+                        counters["derived_failures"] += 1
                         findings.append(finding(
                             "D4L-ARGOT-DERIV", "FAIL",
                             "register-scoped form %s %r (register %r): declared chain %r applied to "
@@ -658,6 +666,12 @@
                             % (eid, form, scoped, layer_label,
                                text_of(entry.get("donor_form")).strip(), replayed)))
 
+    # F-6 (reports/round-17/d4/design-brief.md:306-307): the coverage block
+    # reports `derived_forms` and `derived_ok` counts that agree. The pair is
+    # materialised here, not at the print, so a consumer can assert it.
+    counters["derived_forms"] = counters["derived_pairs"]
+    counters["derived_ok"] = counters["derived_pairs"] - counters["derived_failures"]
+
     declared_ops = packet_declares_ops(packet)
     if declared_ops and counters["register_scoped"] and not counters["derived_pairs"]:
         findings.append(finding(
@@ -776,6 +790,81 @@
 """
 
 
+def _recount_derivations(text):
+    """Re-derive (forms, failures) from packet bytes, sharing no gate code.
+
+    Counts every mapping that declares a `derivation` key, in either of the two
+    styles the tree uses: block style (`  derivation: head2` on its own line,
+    the delivered packets) and flow style (`, derivation: head2}` inside a
+    `{...}` record, the committed fixture). The `derivation_rules:` key is not a
+    match, because the token must be followed directly by a colon. This is
+    deliberately not the gate's own reader — a recount that reused the gate's
+    parse could not catch a wrong count. The failure half is not inferable from
+    bytes alone (it needs the replay), so it is returned as zero and the failing
+    control asserts it separately.
+    """
+    return len(DERIVATION_KEY_RE.findall(text)), 0
+
+
+DERIVATION_KEY_RE = re.compile(r"(?:^|[,{]\s*)\s*derivation\s*:")
+
+
+def _printed_pair(text):
+    """The (derived_forms, derived_ok) pair the CLI prints for a packet text.
+
+    Runs the gate as a subprocess over a temporary copy of `text` and parses its
+    own `coverage:` line, so the assertion is on the delivered output rather
+    than on the counter object.
+    """
+    import subprocess
+    import tempfile
+    with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False,
+                                     encoding="utf-8") as handle:
+        handle.write(text)
+        temp = handle.name
+    try:
+        proc = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()),
+                               temp], capture_output=True, text=True, check=False)
+    finally:
+        Path(temp).unlink()
+    for line in proc.stdout.splitlines():
+        if line.startswith("coverage:"):
+            fields = dict(re.findall(r"(\w+)=(\d+)", line))
+            return int(fields["derived_forms"]), int(fields["derived_ok"])
+    return None
+
+
+RULE_MISMATCH_CONTROL = """\
+name: F-argot-rulemismatch
+morphology:
+  derivation_rules:
+    - id: CX-01
+      pattern: "^(?P<a>.+)[+](?P<b>.+)$"
+      output: "{a}{b}"
+lexicon:
+  - {id: Q-01, term: wrong, register: quote, derived_from: nope, derivation: CX-01}
+"""
+
+TWO_MIXED_CONTROL = """\
+name: F-argot-mixed
+morphology:
+  derivation_rules:
+    - id: CX-01
+      pattern: "^(?P<a>.+)[+](?P<b>.+)$"
+      output: "{a}{b}"
+    - id: UP-COMPOUND
+      pattern: "^(?P<B1>[a-z]+)[+](?P<B2>[a-z]+)$"
+      output: "{B1}{B2}"
+layers:
+  - {id: LY-01, name: "West layer", register: trade, substitutions: {sh: s}}
+lexicon:
+  - {id: Q-01, term: nim, register: quote, derived_from: min, derivation: reverse}
+  - {id: Q-02, term: wrong, register: quote, derived_from: nope, derivation: CX-01}
+  - {id: Q-03, term: bad, register: quote, formation: {stem: "su+bel", bases: [su, nel], rule: UP-COMPOUND}}
+  - {id: B-01, term: res, route: borrowed, layer: LY-01, loan_layer: "West layer", donor_form: resk}
+"""
+
+
 def selftest():
     checks = []
 
@@ -857,6 +946,52 @@
                    cov_code == EXIT_FINDINGS
                    and [item["id"] for item in cov_findings] == ["D4L-ARGOT-COVERAGE"]))
 
+    # 6b. F-6 (reports/round-17/d4/design-brief.md:306-307): the coverage
+    #     block reports `derived_forms` and `derived_ok` counts that agree, and
+    #     the pair is CONSUMED, not merely printed. These controls re-derive
+    #     both numbers from the committed fixture bytes by an independent line
+    #     scan and assert the emitter's own relation against that recount — the
+    #     vacuous-pass guard D10b's mission requires. The projector's
+    #     byte-identity check provably accepts a lying value, so byte-equality
+    #     cannot stand in for this.
+    fixture_forms, fixture_failures = _recount_derivations(fixture_text)
+    checks.append(("f6-recount-matches-the-fixture",
+                   fixture_forms == _totals["derived_pairs"]))
+    checks.append(("f6-counters-agree-on-clean-control",
+                   pos_totals["derived_forms"] == pos_totals["derived_ok"]
+                   and pos_totals["derived_forms"] == 4))
+    checks.append(("f6-counters-are-non-vacuous",
+                   pos_totals["derived_forms"] > 0))
+    # the discriminating control: a record whose declared chain does not replay
+    # moves `derived_ok` and leaves `derived_forms` alone.
+    _rm_code, _rm_findings, rm_totals = evaluate_text(RULE_MISMATCH_CONTROL, naming)
+    checks.append(("f6-counters-disagree-on-a-failing-record",
+                   _rm_code == EXIT_FINDINGS
+                   and rm_totals["derived_forms"] == 1
+                   and rm_totals["derived_ok"] == 0
+                   and rm_totals["derived_failures"] == 1))
+    # the domain control: `violations` also counts claimed-chain and borrow
+    # failures, so the shared total must NOT be the emitter's source. On this
+    # control violations (3) exceeds derived_pairs (2), so the formula the block
+    # drafted (`derived_pairs - violations`) yields -1 — a negative count.
+    _mx_code, _mx_findings, mx_totals = evaluate_text(TWO_MIXED_CONTROL, naming)
+    checks.append(("f6-derived-ok-ignores-non-derivation-violations",
+                   mx_totals["derived_pairs"] == 2
+                   and mx_totals["violations"] == 3
+                   and mx_totals["derived_forms"] == 2
+                   and mx_totals["derived_ok"] == 1))
+    checks.append(("f6-shared-violations-total-is-not-the-emitters-source",
+                   mx_totals["derived_ok"]
+                   != mx_totals["derived_pairs"] - mx_totals["violations"]))
+    checks.append(("f6-derived-forms-is-a-recount-not-a-constant",
+                   fixture_forms > 0
+                   and fixture_forms != pos_totals["derived_forms"]))
+    # the printed line itself is asserted against the recount, so a print that
+    # lies about the pair is caught here (D10b's C3 control).
+    checks.append(("f6-printed-line-agrees-with-an-independent-recount",
+                   _printed_pair(fixture_text) == (fixture_forms,
+                                                   fixture_forms - _totals["derived_failures"])))
+
     # 7. malformed input exits 2 with D4L-ARGOT-DATA, never a traceback.
     for label, text in (("root-is-a-string", "just a string"),
                         ("unclosed-flow", "name: F\nlexicon: [\n"),
@@ -915,10 +1050,10 @@
     except ValueError:
         shown = str(path)
     print("coverage: %s records=%d register_scoped=%d derived_pairs=%d claimed_chains=%d "
-          "borrow_pairs=%d violations=%d rule_holds=%d"
+          "borrow_pairs=%d violations=%d rule_holds=%d derived_forms=%d derived_ok=%d"
           % (shown, totals["records"], totals["register_scoped"], totals["derived_pairs"],
              totals["claimed_chains"], totals["borrow_pairs"], totals["violations"],
-             totals["rule_holds"]))
+             totals["rule_holds"], totals["derived_forms"], totals["derived_ok"]))
     print("dependency: %s sha256 %s"
           % (NAMING.relative_to(ROOT), sha256_file(NAMING)))
     return code
```

**Design notes the integrator needs.**

- The emitter is **additive**: it adds one counter (`derived_failures`) and two keys. It
  renames nothing, so `derived_pairs` and `violations` keep their contracts and the gate's
  docstring ("one `coverage:` line") stays true.
- `derived_failures` is a `Counter`, so it is absent (reads as `0`) on packets with no
  derivation failures and is never printed — no change to the line's shape beyond the two
  appended keys. The `_totals["derived_failures"]` reads in the controls therefore need no
  `Counter` default.
- `_printed_pair` spawns one subprocess per selftest run. That is deliberate: it is the
  only way to assert the *delivered* line rather than the counter object, which is what
  makes the control catch D10b's C3 lie (§4.2).

---

## 4. Measured — the isolated copy

Copy: `.scratch/d01/` (`git archive 9bccc9b | tar -x -C .scratch/d01`). Every command
below ran inside that copy with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

### 4.1 The selftest grows 27 → 35, and every new control discriminates

```
$ python3 -B tools/gates/argot-derivation-gate.py --selftest
selftest: 35/35 checks passed                      exit 0
```

27 baseline + **8** new: `f6-recount-matches-the-fixture`,
`f6-counters-agree-on-clean-control`, `f6-counters-are-non-vacuous`,
`f6-counters-disagree-on-a-failing-record`,
`f6-derived-ok-ignores-non-derivation-violations`,
`f6-shared-violations-total-is-not-the-emitters-source`,
`f6-derived-forms-is-a-recount-not-a-constant`,
`f6-printed-line-agrees-with-an-independent-recount`. The pre-existing 27 are unchanged and
still pass.

**The intermediate measurements are the evidence, not just the final green.** The patch was
built in three states, and each state's failure set is a control on the design:

| state | selftest | what the failures showed |
|---|---|---|
| pair only in the `print` expression | 27/33 | all 6 controls failed — nothing could read the pair, so a consumer is impossible unless the pair is materialised in `counters` |
| pair in `counters`, recount as a `derived_from:` line scan | 29/33 | `f6-recount-matches-the-fixture` failed: the committed fixture writes records in **flow** style (`, derivation: head2}`), which a line-prefix scan cannot see — measured `recount forms = 0` against the gate's `derived_pairs=8` |
| final (flow-or-block recount, both controls) | **35/35** | — |

The first state is the direct measurement of §2's claim: a print-time pair is unreadable by
any in-process consumer, which is why D10b had to build a subprocess probe. The second is a
warning for anyone re-deriving the counter from bytes — the tree uses **both** styles.

### 4.2 The delivered packet, the fixture, and the lying print

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 \
  claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0 derived_forms=8 derived_ok=8
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit 0

$ python3 -B tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml | grep '^coverage'
coverage: tools/gates/fixtures/argot-derivation-gate.yml records=14 register_scoped=11 \
  derived_pairs=8 claimed_chains=0 borrow_pairs=3 violations=4 rule_holds=1 \
  derived_forms=8 derived_ok=5
```

The delivered packet is unchanged in verdict (`exit 0`, zero findings) and the pair agrees
non-vacuously (`8 == 8`, and `derived_pairs` has 8 real members). The fixture — the tree's
own negative control — now reads `8 / 5`, which is the value the drafted formula would have
misreported as `8 / 4`.

**The lying-print control, run.** D10b's C3 replaced the printed values with
`derived_forms=0 derived_ok=8` and found the pipeline stayed green. This patch's
`f6-printed-line-agrees-with-an-independent-recount` is built to catch exactly that, so it
was tested against a deliberately lying variant (`.scratch/d01/tools/gates/argot-lie.py`,
the print arguments replaced by `0, 999`):

```
recount forms      = 8
lying print pair   = (0, 999)
control verdict    = CAUGHT (mismatch)
```

The control is not always-true; it fails on the lie and passes on the honest print.

### 4.3 Zero pins move — the no-harm proof

Every pin-reading surface, run in the patched copy:

| # | surface | command | observed |
|---|---|---|---|
| 1 | gate battery | `tools/check-gate-battery.py` | `summary {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`; `baselines {baseline_exit: 0, pinned: 20, coverage: "10/10", gates_uncovered: [], readings: {pinned: 20}}`; findings `[]` |
| 2 | typed pipeline | `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `ok L3b-argot` … `summary: 20/20 legs passed` |
| 3 | v3 default chain (r7) | `tools/exercise-handoff-e2e.py --profile v3 --quiet` | `exit=0 fields=16/16 links=105/105 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| 4 | r31-post sweep | `tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4 rows reproduced` |

Row 3 is the claim's own threshold: the r7 packet digest is **unchanged** at `45f57132…`.
Row 1 is the reason the host decision matters: the argot gate is in none of
`GATE_NAMES` / `D4_GATE_NAMES` / `REGISTER_LAW_GATE_NAMES` (`tools/check-gate-battery.py:117-132`,
read live: 7 + 2 + 1 names, argot absent) and in no `tools/gates/expected/` generation
(`ls` → `costume-era-consistency-gate d4-assembly-check-gate d4-typed-labels-check-gate
phonology-sanity-gate register-law-gate`), so editing it moves nothing the battery pins.

This independently reproduces D03 §3.1 and D04 §3.1 from a different patch, and it is the
reason the F-6 half of claim D can land green inside the round's declared byte budget while
the RL-8 half cannot (the law gate *is* battery-registered — D02 §3.5, D04 §4, R01 F2).

---

## 5. What this changes in the sibling fragments

| seat | its drafted F-6 shape | this seat's correction |
|---|---|---|
| P01 §3.1 / §3.4 | `derived_ok = derived_pairs - violations` | **domain is wrong** — `violations` spans three classes; use a dedicated `derived_failures` (§1.1) |
| D08 §2.1 | `derived_ok = totals["derived_pairs"] - totals["violations"]` | same correction; D08's two selftest controls (`derived-counters-agree-on-clean-control`, `…-disagree-on-negative-fixture`) are the right *shape* but their negative fixture is the committed fixture, whose disagreement is 1 borrow + 3 derivation — they cannot distinguish the two definitions |
| D04 §3.1 | `derived_forms=8 derived_ok=8` on the delivered packet | the values are right **on this packet only** (`violations=0`), which is exactly why the drift was invisible |
| D10b §4 | "selftest **and/or** `L3b-argot` sub-assertion" | the selftest is forced, not optional (`:709`), and the `L3b-argot` host would need the r7 L3b rows re-pinned (§2) |
| D03 §3 | verified P01's draft verbatim | its `derived_forms=8 derived_ok=8` measurement stands; the draft it verified carries the wrong `derived_ok` domain, which the delivered packet cannot expose |

None of this contradicts those seats' *pin* findings — route A is zero-cost, verified again
here — and it does not touch the RL-8 half. It corrects the arithmetic.

---

## 6. The patch is one file, and the pin surface is empty

| artifact | change | verdict |
|---|---|---|
| `tools/gates/argot-derivation-gate.py` | `derived_failures` counter + 2 increments + 2 counter keys + 2 selftest helpers + 2 controls + 8 checks + the coverage line | **the patch** |
| `tools/gates/fixtures/argot-derivation-gate.yml` | none — read as the independent recount's input | **no change** |
| `tools/gates/typed-pipelines.json` | none — the argot gate is not a profile field | **no change** |
| `examples/culture-d4/**`, `examples/culture-d2/**` | none | **no change** |
| `tools/gates/expected/**`, `tools/gates/frozen/**` | none — no generation pins the argot gate | **no change** |
| `reports/round-34/handoff/declared-in-r7/**` | none — not a read-set member; packet pin `45f57132…` verified unchanged | **no change** |

**Re-pin list: empty.** Stated explicitly because P01 §5 R-7, D04 §6 and the claim's own
`after_required` ("pins updated as new rows") all anticipate one. On this route **no pin
moves**, so that clause is satisfied vacuously and is reported as such, never ticked
(P01 §6.4 reaches the same wording).

---

## 7. Contested scope — reported, not absorbed

1. **The counter domain.** `derived_forms` = the `derived_from`/`derivation` class (8 on
   the delivered packet), or = every `D4L-ARGOT-DERIV` failure source (which would also
   admit the claimed-chain and borrow classes)? This patch takes the first, on F-3's
   wording. The alternative is a contract decision, not a measurement. **Owner: the D
   planner / integrator.**
2. **`derived_ok`'s relation.** `derived_forms - derived_failures` (this patch), or
   "the count that replayed", where a `rule_holds` record (a HOLD, not a FAIL) counts as
   not-ok? On the delivered packet both give 8; they differ on the committed fixture
   (`rule_holds=1`, `derived_ok` 5 vs 4). **Owner: the integrator** — F-6 says only
   "counts that agree".
3. **The consumer's permanence.** The selftest controls are permanent in the gate; but the
   *round-level* threshold ("no vacuous-pass") is satisfied by an in-tree control whose
   pass/fail a reader must trust. D03 §7.3's scratch-side probe and D10b §4's fenced probe
   are alternative instruments; if the round wants an independent reader, one of them must
   be filed as a tool. **Owner: the integrator.**
4. **The projector route.** If the integrator reads "the coverage block" as binding the
   *projection* literally, the five-row cascade of D04 §3.2 applies, plus the D2 family.
   This patch does not preclude that; it prices the alternative as route B. **Owner: the
   integrator.**
5. **Battery registration of the argot gate.** P01 §4.4 and D04 §3.1 record it as O's
   territory; if O registers the gate while D grows it, the freeze row must pin D's
   post-change bytes, so the freeze must follow D's landing. **Owner: the O block.**
6. **`13-register-law.yml:57`'s enforcement prose** (D02 §2.1's deviation, K01 §7.6) is
   unaffected by this patch — it is an RL-8 artifact, not F-6's.

---

## 8. What this seat did not do

- Did not write, edit or create any tool, gate, packet, component, fixture, pin,
  `expected-holds.json` row, `typed-pipelines.json` row or frozen baseline. The patch above
  is a fenced draft; every measurement ran in `.scratch/d01/` (gitignored).
- Did not run any `reports/round-*/run-validation.py` anywhere (F-C13-1);
  `reports/round-38/run-validation.py` does not exist, so claim D's third counting command
  is `to-verify`.
- Did not re-freeze or edit `reports/round-34/handoff/declared-in-r7`; it was read only, and
  the chain still exits 0 with the packet pin unchanged.
- Did not decide any contested item in §7, and did not touch the RL-8 era leg (D02's).
- Did not commit, push, install, or reach the network.

## Owed

- **The `derived_ok` relation** (§7.2) — `derived_failures`-based (this patch) vs
  HOLD-excluding. Measured both ways on the fixture (5 vs 4); the choice is the
  integrator's. **Owner: the integrator.**
- **The counter domain** (§7.1) — the derivation class vs every `D4L-ARGOT-DERIV` source.
  **Owner: P01 / integrator.**
- **The patch is not landed.** The integrator applies §3; `.scratch/d01-apply.py` is the
  applier used for the measurements (scratch, not promoted).
- **`reports/round-38/run-validation.py`** — absent; claim D's declared counting command is
  `to-verify` until landed, and must not be run in-tree regardless. **Owner: the
  integrator.**
- **The projection route (route B)** — priced in D04 §3.2, not taken here. **Owner: the
  integrator.**
- **A filed independent consumer** — D10b §4's probe or D03 §7.3's probe, if the round
  wants the F-6 threshold enforced by a file rather than by the gate's own selftest.
  **Owner: the integrator.**
- **Not measured by this seat:** whether any *filed* round-1..37 byte quotes the gate's
  coverage-line shape (a filed fragment may quote the old 7-key line and would then be a
  stale quote rather than a defect); and whether `reports/round-38/run-validation.py`'s
  eventual leg set includes an F-6 leg. Both are `to-verify`.

## Citations

Files (sha256 measured 2026-10-19T11:14:28Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py        (baseline)
8c7dd098d9ac76a1702ad920bedd80402960816dee64a066f7ceb5616cbdef07  tools/gates/argot-derivation-gate.py        (patched, in isolated copy)
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce  tools/check-gate-battery.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd  tools/gates/fixtures/argot-derivation-gate.yml
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
```

Commands run (lane root or `.scratch/d01/`, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`):

```
git rev-parse --short HEAD                                       # 9bccc9b
date -u +%FT%TZ                                                  # 2026-10-19T11:14:28Z
git status --porcelain                                           # ?? reports/round-38/ only
git archive 9bccc9b | tar -x -C .scratch/d01
python3 -B .scratch/d01-apply.py .scratch/d01                     # 928 -> 1063 lines

# the domain measurement
python3 -B tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml
    # derived_pairs=8 violations=4 derived_forms=8 derived_ok=5 ; FIXTURE_EXPECTED DERIV=4 RULE=1
python3 -B -c "<evaluate_text on RULE_MISMATCH_CONTROL>"          # derived_forms=1 derived_ok=0 derived_failures=1
python3 -B -c "<evaluate_text on TWO_MIXED_CONTROL>"              # derived_pairs=2 violations=3 derived_ok=1
                                                                  # -> drafted formula gives -1

# the patch
python3 -B tools/gates/argot-derivation-gate.py --selftest        # 35/35 checks passed, exit 0
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
    # derived_forms=8 derived_ok=8, exit 0
python3 -B -c "<_printed_pair against a lying variant (0, 999)>"  # CAUGHT (mismatch)

# the no-harm proof
python3 -B tools/check-gate-battery.py                            # exit 0; pinned 20; coverage 10/10; findings []
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # 20/20
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet     # exit 0, packet 45f57132…
TMPDIR=/var/tmp python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv  # 4/4
sed -n '117,132p' tools/check-gate-battery.py                     # argot gate absent from all three name tuples
ls tools/gates/expected/                                          # no argot generation
python3 -c "<r7 expected.json inputs>"                            # 58 members; argot absent; typed-pipeline absent
```

**Source lines cited:** `tools/gates/argot-derivation-gate.py:96,485-513,542-676,567,571,587,594,609,613,619,626,633,650,652,669,671-676,694-709,733-736,779,815-829,833-856,917-921,928` (baseline numbering; the patched revision is +4 to +135, with the emitter at `:672-673`, `_recount_derivations` at `:793`, `_printed_pair` at `:812`, `RULE_MISMATCH_CONTROL` at `:837`, `TWO_MIXED_CONTROL` at `:848`, `selftest` at `:868`);
`tools/gates/typed-pipeline-gate.py:517-541,530-531,539`;
`tools/check-gate-battery.py:117-132,540`;
`tools/gates/fixtures/argot-derivation-gate.yml:32-47`;
`examples/culture-d4/packet.d4.yml:1018-1175`;
`reports/round-17/d4/design-brief.md:296-310` (F-6 at `:306-307`, F-3 at `:303`);
`reports/round-25/argot/forecast.md:33-41`;
`reports/round-26/register/execution-3.md:74`;
`reports/round-36/validation.json` (claim D, failed as declared);
`reports/round-38/{claims.json,targets.json}`;
`reports/round-38/scout/K01-residue.md` §2.1, §3.1-3.2, §4.2-4.3, §7.1-7.2, §8 (the owed `derived_ok` semantics);
`reports/round-38/plan/P01-d-plan.md` §2.1, §3.1, §3.4, §4.2, §5, §6.4;
`reports/round-38/depth/D02-rl8-design.md` §3.5, §6;
`reports/round-38/depth/D03-isolated.md` §3.1, §4, §5, §7.3;
`reports/round-38/depth/D04-pins.md` §1, §3.1, §3.2, §6, §7;
`reports/round-38/depth/D08-gap-fill.md` §2.1-2.3, §3, §5;
`reports/round-38/depth/D10b-verify.md` §1-§5;
`reports/round-38/review/R01-d-review.md` §3-§5;
`reports/round-34/handoff/declared-in-r7/expected.json` (`inputs`, 58 members).
