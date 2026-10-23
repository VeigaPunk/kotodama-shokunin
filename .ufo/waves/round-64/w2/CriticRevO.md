# CriticRevO — revised-operability attack

Axes: **coverage, operability, calibration**. This seat reviews counter/control soundness only; it does not judge, admit, integrate, or alter a claim.

## Revision dependency — revised results unavailable

The requested **revision 4 was absent when sampled**. The canonical `reports/round-64/accept-o.py` still says `revision 3 (pre-data)` at line 2 and has only revisions 1–3 in its history (lines 92–115). Direct identity capture:

```text
$ sha256sum reports/round-64/accept-o.py tools/reopen-row.py
c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18  reports/round-64/accept-o.py
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  tools/reopen-row.py
```

The counter hash is exactly the rev3 identity in `.ufo/waves/round-64/w1/CriticO.md:19` and `reports/round-64/telemetry/control-o.txt:2`. The latter receipt explicitly names revision 3. A filename or existing green receipt therefore cannot establish the requested rev4 behavior. Main acknowledged that `kotodama-r64.RevCounters` owns the in-progress rev4 edits and instructed this seat to attack the observed rev3 bytes, record the dependency, and never wait.

**All four requested revised-byte checks remain unmeasured by this seat.** No rev3 runtime output is relabeled as revised evidence. Known wave-1 failures were not rerun merely to confirm them. The findings below are direct current-source observations plus explicitly attributed inherited live receipts.

## Counterexample and evidence

### O-R1 — selector validation remains absent in the observed bytes

At `accept-o.py:428–445`, `--only` is split into a set without validation against the 23 declared leg names. `leg()` excludes nonselected names from `legs`; line 1110 computes `all(legs)`.

[INFERENCE from current code] `--only NOSUCHLEG` reaches an empty `legs`, hence a vacuous PASS/exit 0. A valid-plus-invalid selector is not rejected either; a passing selected leg can produce PASS despite the unknown token. These are not newly executed results. The inherited live receipt in `.ufo/waves/round-64/w1/ReviewerCounterO2.md:23–51` records both `NOSUCHLEG` yielding PASS/0 and `EDGE_308,BOGUS` yielding PASS/0 on these same counter bytes.

**Smallest safe correction:** validate the complete selector set before fixture work or any PASS output; unknown-only and mixed selectors must exit 2. Preserve every defined assertion. The required rev4 negative controls are still missing here.

### O-R2 — m5 is still broad; exact-isolation remains unmeasured

The current literal `MUTANTS` tuple at `accept-o.py:1037–1040` still replaces:

```python
target = urllib.parse.urljoin(current, location.strip())
```

with:

```python
target = urllib.parse.urljoin(current, "/" + location.strip())
```

This is not confined to slashless relative paths. The strongest local counterexample is the inherited exact-table reconstruction in `.ufo/waves/round-64/w1/CriticO.md:128–148`:

```text
EDGE_SCHEMEREL FAIL rows=[('S2939', 'UNREACHABLE', 2)] tgt_hits=0 src_hits=1 tb=False
EDGE_SLASHLESS FAIL rows=[('S2630', 'UNREACHABLE', 2)] dir_hits=0 root_hits=1 exit=1
ACCEPT-O-64: FAIL
```

The paired healthy/docstring-only tool passes both (`CriticO.md:108–125`). `ReviewerOReceipt.md:30` independently records the same two-leg failure. These are **wave-1 executions**, not fresh rev4 executions. Because the inspected current counter has the identical full hash and unchanged m5 tuple, the claimed narrowing has not yet landed in the sampled artifact.

The exactness authority is also duplicated incorrectly: `claims.json:32` promises each mutant fails **exactly** its pins, and counter history lines 113–115 claim observed failure-set equality. Yet `accept-o.py:1076–1091` selects only the pins for each child and filters only pinned output lines before comparing sets. Failures outside the selected pins are never observed. Narrowing m5 alone cannot repair this measurement defect.

**Smallest safe correction:** narrow the mutation to nonempty slashless relative paths, preserving scheme-bearing, authority-bearing, root-relative, query-only, and fragment-only references. Separately, measure every defined non-MUT leg for each mutant before claiming complete failure-set equality; do not filter to pins before measuring. Require each expected leg exactly once with a valid result, retain m8's declared `{GEN, BOUND}` pair, and reject missing results or collateral failures. Do not bless this counterexample by expanding m5's pin set or weakening EDGE_SCHEMEREL.

### O-R3 — observed rev3 docstring/code drift still present

This is a current-source comparison, **not a rev4 re-check**:

| Surface | Prose | Actual observed code |
|---|---|---|
| `--only` | Lines 18–19: runs just named legs; every omitted leg prints SKIP | The entire core battery runs when any core name is selected (`445`, `482`); the core block has no SKIP-emitting alternative when omitted. |
| REDIRECT / MALFORMED | Lines 39–42 promise `url=-` | Calls use `parse(out)` without `with_url=True` (`655`, `660`, `680`), so these comparisons do not pin URL. |
| EDGE_USERINFO same-authority | Lines 51–54 specify `UNREACHABLE attempts=6` | Lines 856–858 accept any non-REFUSED verdict with attempts 6. |
| DRIP row output | Lines 69–74 specify attempts 3 and 1 | Lines 1004–1006 compare only `(sid, verdict)`; attempt columns are discarded. |
| DRIP timing and chunk | Lines 70–72 specify 64-byte chunks and wall `[8,60]` seconds | Lines 986–988 send the randomized HTML fragment as each chunk; line 1006 requires `wall < 20` and arrival span >=7, not the stated interval. |
| HTTPS internal explanation | Lines 55–59 specify attempts 6 | Comment at 874–876 still says attempts 3; assertion at 885 pins 6. |
| MUT exactness | History says observed failures equal pins | Only pins are run/filtered (`1076–1091`), so collateral failures are invisible. |

**Smallest safe correction:** the rev4 receipt must bind the actual delivered bytes, and its prose must match the resulting assertions. Where the existing prose specifies a promised property (URL, exact verdict, attempts, chunk size), add the missing assertion/fixture constraint rather than weakening that promise after the fact. Correct stale explanatory text without changing the unchanged tool. The exact-isolation repair is separate from documentation cleanup.

### O-R4 — cosmetic-patch control exists only for rev3

The present `reports/round-64/telemetry/control-o.txt` records:

```text
# counters: reports/round-64/accept-o.py (revision 3) sha256 c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18
# control 2 - do-nothing patch to the tool (docstring only, sha256 f3789feee1488b9a64da05f93e8aeeac3afadbc173ef76ad6a7b3362e7e9bb61)
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
MUT PASS bad=[] mutants=10 kill_evidence=[...]
ACCEPT-O-64: PASS
exit=0
```

I read the complete line 40: it names all ten `m1,m10,m2,m3,m9,m5,m6,m7,m8,mread` with their pinned FAIL lines. Thus the inherited receipt supplies genuine **rev3 pinned-kill** evidence, not evidence of revised controls or complete mutant isolation. Its m5 still has the broad-patch hash described in the wave-1 report.

**Smallest safe correction:** after rev4 is actually available, rebuild mutants from that exact counter's literal table and the unchanged tool; capture the docstring-only GEN/MUT run against those bytes with command, counter/tool/control hashes, complete output, and exit status. Retain the old receipt as rev3 history rather than changing its header to rev4. Until then, the revised cosmetic-patch control is a missing dependency, not a demonstrated regression or success.

## Impact and disposition

- **Operability:** unresolved selector fail-open and mutant-isolation defects in the observed artifact; revised behavior is unavailable to measure.
- **Calibration:** exactness and documentation overstate measured assertions; old control receipts must not acquire false revised provenance.
- **Coverage:** no corpus/registry behavior was exercised or changed; no coverage-axis harm is alleged.

These are fixable counter/evidence defects, not a necessary tradeoff or grounds for this critic to adjudicate a claim. Canonical judgment remains outside this seat.

Only this requested report was written. No counter/tool/row/claim edits, commits, index/jj mutations, subagents, additional runtime invocation, or tool installs/updates. No fresh acceptance execution is claimed. Missing prerequisite: delivered rev4 bytes and their forcing-control revision identity at the canonical path. The revision dependency was communicated to Main without waiting.
