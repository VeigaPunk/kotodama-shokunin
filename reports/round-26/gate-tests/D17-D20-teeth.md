# R26-D17..D20 — the teeth control: plant, rebuild, grade, revert

- **Seats:** R26-D17..D20 (gate+tests x4), round 26, loop 3 build 2 of 4, claim **D**
  `register-stratum`.
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope:** this fragment and `reports/round-26/gate-tests/**`; the plant
  itself happens **only inside a throwaway `git clone`** under
  `.scratch/r26-d17-d20/clone`, never the lane worktree.
- **Canon:** NON-CANON. The planted form is a probe; it is not a design claim.

## 0. Verdict

**The argot leg has teeth through the D4 typed gate, not only standalone.** A
register-scoped record whose declared `head2` chain does not yield its form is
planted into a component, the whole chain is rebuilt, and the gate reads
`D4L-ARGOT-DERIV` with `FAIL L3b-argot`. Reverting the clone returns the tree to
17/17 green — so the control demonstrates discrimination, not an always-red leg.

## 1. Why a clone

A control that moves the tree it measures is not a control. The plant edits
`examples/culture-d4/components/04-lexicon.yml`, which is a **tracked input**;
editing it in the lane worktree would dirty the packet, the projection, the
typed packet and the frozen inputs at once. So the control runs entirely inside
`git clone --no-hardlinks .` under scratch, and the clone is removed at the end.

## 2. The control, step by step

Measured 2026-10-18T18:22Z on the settled post-register tree,
`TMPDIR=$PWD/.scratch`:

1. **Clone.** `git clone -q --no-hardlinks . .scratch/r26-d17-d20/clone` → exit 0.
2. **Plant.** Insert one lexicon record into `components/04-lexicon.yml`:

   ```yaml
   - {id: NEG-D17-01, term: saalum, ..., register: quote,
      derived_from: saalumi, derivation: head2}
   ```

   `saalum` is `head2(saalumi)` under the maximal-coda reading, which the design
   rejects (`design-language.md` §5); the design's maximal-onset reading yields
   `saalu`.
3. **Rebuild.** `assemble-culture-d4.py`, then `d2-typed-labels.py --emit`, then
   `assemble-d4-typed.py --emit`. All succeed. (`--emit` returns the *findings*
   exit 0/1 after writing — `tools/d2-typed-labels.py:3624` — so the step accepts
   `(0, 1)`; only `2` means nothing was written.)
4. **Grade.** `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml`:

   ```
   FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form NEG-D17-01 'saalum'
     (register 'quote'): declared chain 'head2' applied to 'saalumi' yields
     'saalu'; the stated inputs and rules do not yield the candidate
   FAIL L3b-argot: argot leg exit 1: FINDING D4L-ARGOT-DERIV: FAIL — ...
   ```

   exit **2** (the gate also fails closed on the stale projection pin the plant
   invalidates — `FAIL L1-profile`).
5. **Revert.** `git checkout -- examples/culture-d4/`, rebuild, re-grade:
   **exit 0, 17/17 legs, no FAIL** — the clean tree is green again.

## 3. What the control shows, and what it does not

- **Shows:** the leg is wired into the gate (a standalone argot run is not
  enough — the gate's `L3b-argot` leg must go red), the finding names the
  offending record, and the leg is discriminating (revert restores green).
- **Does not show:** that the *delivered* packet contains such a record. The
  delivered tree is clean (`violations=0`); this is a planted probe.
- **Does not show:** that the register stratum is complete. The domain is still
  empty on the delivered packet (`derived_pairs=0`), which is the claim's open
  leg (`D17-typed-gate.md` §1).
