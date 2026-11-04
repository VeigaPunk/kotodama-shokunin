DRAFT FRAGMENT — NOT FILED. For L1 integration into `corpus/QUALITY.md` only by appending below criterion 33 (base highest criterion is 33). Author-side, ScribeLesson seat, round 87.

34. **A counterfeit-reader control is killed by a forgery that answers from the packet's label, and a finite battery's verdict is bounded by the forgeries it actually survived.** — adds to criteria 11, 19 and 23.

Scope: every round counter or review that grades a production CLI or reader against a finite battery of packets, and every round report, lesson or scorecard sentence that describes what such a battery "proves", "defeats", "rejects" or "discriminates".

Four clauses, binding from round 87:

(i) **An absence control is not a counterfeit control.** A row showing that a tool is missing (`TOOL_ABSENT`, exit 1) tests absence. It discharges no counterfeit requirement. Round 86 shows the gap: the frozen r86 O counter, run on the lane's CriticPredicate probe `O-nonreader-fake-selftest-and-bare-registry`, printed `ACCEPT-O-86: PASS legs=8/8` for a non-reader fake through its `TOOL` leg. That is a transport overlay on synthetic lands, not live-CLI evidence, and it is recorded as such.

(ii) **Each finite battery freezes its counterfeit set before the claims freeze.** The set includes at least one constant non-reader (the same output for every input), one blanket refusal (the same rejection for every input) and one malformed-output control. Each is committed in a commit strictly earlier than the claims freeze, and each must score strictly below the claim's target. A counterfeit that reaches the target is a counter red, whatever the claim's own verdict.

(iii) **A kill is evidence only for its counterfeit class.** A battery that defeats constant and blanket counterfeits does not thereby defeat forgeries keyed on the packet's file name or on its labels. Round 87 measured both: the constant non-reader scores 3/12 and the blanket refusal 1/12 against `reports/round-87/measure87.py`, but a filename-keyed non-reader that never opens the packet body scores 12/12 (CriticCounter `filename-spoof.receipt.json`; ScribeLesson author-side repeat `receipts/forge-filename-keyed-measure87.json`). A report on such a battery writes "finite battery N/M on the frozen cases" and may not write that the battery defeats forgery in general.

(iv) **A counter whose candidate output cannot be parsed fails closed with a receipt.** A candidate that returns a `findings` value the counter cannot iterate (`findings: null`) produces a failed case row and a receipt. A traceback that leaves no aggregate receipt is not a 0/N result and not a pass; it is a counter defect to be recorded as such.

Check (red-before, pre-dispatch), draft at `.ufo/waves/round-87/w1/stage/ScribeLesson/check34-draft.py`, one command over the committed control receipts:

```
python3 -B check34-draft.py reports/round-<N>/constant-pass.json reports/round-<N>/counter-selftest.json
```

prints `COUNTERFEIT-KILL: PASS` only when the committed non-reader and blanket-refusal controls both score below the battery total. Measured 2026-11-04 on the frozen round-87 receipts: `COUNTERFEIT-KILL: PASS non-reader=3/12 rc=1 blanket-refusal=1/12`, exit 0. The same checker on a manufactured non-reader receipt reading 12/12 printed `COUNTERFEIT-KILL: FAIL non-reader=12/12 rc=0 blanket-refusal=1/12`, exit 1. This check does not see filename-keyed or label-echo forgeries; clause (iii) names that gap and the check is not a complete anti-forgery test.

Limits, stated: the check grades only the two counterfeit classes named in clause (ii), on committed receipts; it does not measure mutation coverage, does not prove the battery's case set is complete, and does not judge whether a production tool is correct. Clause (iii)'s forgeries are a finite demonstration, not a universal set. Binds prospectively from round 87. No earlier counter is re-run, re-scored or amended; the round-87 frozen claims, counter and controls remain byte-identical history, and the 12/12 filename-keyed result is recorded as a survivor, not a retroactive failure of the frozen predicate.

Grounded in: `reports/round-86` lane probe `CriticPredicate` (`O-nonreader-fake-selftest-and-bare-registry`, `ACCEPT-O-86: PASS legs=8/8`); round-87 freeze `2a3b5643899c3520867ae930593cafef6ef19cad`, prefreeze controls `732c45394c73fcffd9fc623b939d446c7b11a9db`; CriticCounter receipts `.ufo/waves/round-87/w1/stage/CriticCounter/filename-spoof.receipt.json`, `all-labels-wrong-record.receipt.json`, `null-findings.receipt.json`; and `corpus/lessons/round-86-verifier-spotcheck.md` R86-C2 (fake-reader and empty-decision-cell counter debts).
