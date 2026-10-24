# CriticSizing — claim-sizing attack, round 68

Seat: CriticSizing (w1). Scope: is 24 rows the right batch; is O one claim or three;
are C/O/Ca separable (record-dependency vs real coupling). All paths lane-relative.

## F1 — C's batch: 24 is a sizing convention, not a measured bound — the predicate's "exactly 24" is a hard equality straitjacket (both directions fragile)

Evidence:
- C-claim row counts across rounds: r64=26, r65=26, r66=22, r67=24, r68=24
  (`reports/round-{64..68}/claims.json`, statement "exactly N" / "N registry rows").
  The count tracks each round's harvested register, so 24 is not anomalous. But nothing
  in claims.json derives 24 from the register's size — no harvest census, no ceiling
  argument, no "these are all the reachable tier A/B sources" statement. The claim
  sizes the batch by what was found, then freezes it as `exactly 24` (SET leg).
- `claims.json` C.statement pins `exactly 24 registry rows S833-S856`; accept-c.py
  SET leg requires each of the 24 ids occur exactly once. Direction (a) — if mining
  yields <24 good rows, the claim cannot accept n=22 honestly: it must either pad
  with marginal rows (all counter legs still pass — ROWS checks shape/tier/date/
  used-by, ONEID/RESTATE check citation arithmetic, never semantic adequacy —
  claims.json C.review_only admits this) or fail the whole claim. Direction (b) —
  if mining yields >24 qualified sources, the claim silently discards the surplus
  or the predicate fails; nothing credits it.
- The register itself is correctly scoped: base-gap.txt prints `0` filename owners
  under the word-bounded census; the gap is real. The size is the question, not the gap.

Counterexample: a row-miner stopping at 24 because the counter says 24 delivers the
claim's letter whether the register needed 22 or 30; and a 24th row mining a weak
tier-B stub passes every leg. The number is unfalsifiable as "right" — it is a
frozen convention (r66/r67 precedent ±10%), and the "exactly" predicate converts
batch-size noise into whole-claim fragility.

Impacted axes: coverage (claim-sized). Correction: smallest safe fix is not changing
24 — it is recording the derivation (e.g., "N chosen = all qualified rows mined
in the window; count frozen at declaration") so later rounds can distinguish
register-driven counts from inertia; alternatively predicate `== 24` -> `>= floor`
was considered and correctly rejected (a floor invites shallow-row stuffing), so
the honest correction is the derivation note, not a bound change.

## F2 — O is NOT oversized as a work package, but it IS undersized as a claim: the predicate cannot see ruling correctness, and the settlement-model/claim text mutually exclude executable rulings

Structure (confirmed on disk): O's counter (333 lines) + tool (332 lines) measure
tool behavior: SELFTEST 7/7, DIFF/SHA, PENDING=0, LEDGER 0 findings + id coverage,
EXEC fixture lane, MUT mutants, TOPO. The 34 rulings + used-by flips + entry
re-points are O's *precondition*, not its measurement surface. So "tool + 34
rulings" is one claim in land-topology terms (one A_r commit carries both), and
splitting rulings into a separate claim is unnecessary — BUT the semantic adequacy
of every ruling is claims.json `review_only` (O.review_only[0]), meaning:

Counterexample (strongest available): a settlement lands with **retire rulings on
all 34 chains**. Scan prints pending=0 (each s row status `rejected` →
`settled-retired`, tools/check-supersession-settlement.py `classify`), the ledger
validator accepts `retire` iff `status == "rejected"` (validate_ledger), all
citation re-points are skipped (retire "mutates nothing"), and DECITED legs stay
clean since no target-id citations are added or required to be removed for
retired targets — wait: Ca D2 does require ledger rows for flagged ids but checks
ruling *validity* not optimality. ACCEPT-O-68 passes; the corpus learned nothing —
34 corrections refused wholesale is a degenerate but fully passing settlement.
Ruling adequacy is entirely outside the predicate, riding on audit seats that are
not part of the acceptance gate.

**Sharper defect — the claim text's `retire` definition is unexecutable under its
own frozen mutability model.** Settlement model (prompt/claims): "retire =
superseding row status rejected with REJECTED:/flip: teaches, target unchanged."
All 34 pending s rows currently open `supersedes S### —` in teaches (verified:
S044, S127, S560 in corpus/SOURCES.md); none carries `REJECTED:`/`flip:`. The
frozen MUTABLE set permits edits to status/recheck/used-by cells only — teaches
is immutable (accept-c.py EXEC leg: "mutable teaches edit fails"). Therefore no
existing s row can gain the required `REJECTED:/flip:` teaches, so **the
claim-defined `retire` ruling cannot be satisfied for any of the 34 chains**; the
only executable rulings are activate and the keeps. The tool does not enforce the
teaches phrasing for settled-retired (classify checks status only), so the
counter will still PASS — this is a contract-level inconsistency between the
settlement model's retire spec and the frozen mutable-cell set that the tool
silently papers over. Either retire is dead code in the model (fine — but then
the claim statement lies about the ruling space) or teaches mutability was
intended and the MUTABLE set is under-specified.

Also confirmed executable: `settled-split` is unreachable for all 34 chains —
split requires SPLIT_RE in teaches, teaches is immutable, and no pending s row
carries the limiter (grep: 0 hits). Of the 5 settlement classes, only
activate/retire(status-only)/keeps are reachable at lands.

**Docstring/implementation divergence in STALE-USED-BY**: the tool header defines
stale as "used-by names a path that does not contain the row's own id"; the code
only checks path *existence* (`missing_paths`), never greps the file for the id.
A `settled-active` classification needs `s mined + used-by nonempty + t queued` —
the used-by file need not cite s at all. O's claim says "resolves used-by paths";
it resolves existence, not citation truth (the code comment admits "citation
truth is review work"). This widens the review-only hole: activated swaps can be
status-consistent and citation-free.

Impacted axes: operability (predicate sufficiency), calibration (Ca inherits O's
verdict via D2/R68 without re-checking semantics). Smallest safe correction:
state in claims.json that the executable ruling space at this round's mutable set
is {activate, keep-*} and either (a) add "retire requires appended rejected row
(REJECT_IDS mechanism)" to the model, or (b) delete the `REJECTED:/flip:`
requirement from retire's definition. Do not enlarge predicates — the real fix is
making the model's vocabulary match the frozen cells.

## F3 — Separability: the declared "record-dependency" is accurate for Ca but under-declared for C; there IS real state coupling, and it is one-directional (O → C, O → Ca), which the lands topology already enforces

Evidence:
- Ca legs read post-mutation **state**, not just records: D2 requires "every
  pending-chain s row lands consistent with its ruling (activate→mined,
  retire→rejected)" and R68 requires "none left queued". These evaluate the
  registry rows O's lands commit mutates — that is measured output of the
  settlement, exactly the thing separability_note says Ca never asserts
  ("never measured outputs"). The note's claim is half-true: Ca doesn't
  re-verify rulings semantically, but it DOES consume and re-assert O's
  mutation effects. Name: state-consumption coupling, stronger than the declared
  record-dependency, weaker than joint verification.
- C's DECITED leg reads dedup-ledger.tsv (O's lands artifact) to know which
  target ids are forbidden citations — C is therefore ledger-coupled too, not
  declared in separability_note (which lists only Ca->C and Ca->O).
  Additionally C's APPEND leg permits exactly O's mutation footprint (status/
  recheck/used-by on the 68 MUTABLE ids): C's counter embeds O's bounds. C is
  not separable-from-O in the naive sense — it is deliberately *composed* with
  O's edit envelope.
- Ordering is pinned: A_r (O lands) → A_c (C lands) → A_ca (Ca lands); TOPO leg
  requires lands' parent == declaration commit for O. Dry-run controls confirm
  the do-nothing base FAILs all three counters (dry-run-*.txt). The dependency
  is real but acyclic and declared in lands_topology — the failure mode is not
  circularity but **stale-map evaluation**: if a settlement build deviates
  (e.g., an s-id activate applied to a target outside the citing-file set), no
  citing file outside EDITABLE_ENTRIES exists anyway (verified: all 34 targets'
  citing files ⊆ the 7-file EDITABLE set), so the frozen envelope is tight
  — no sizing defect there.

Verdict: 3 claims are separable-but-ordered, not independent. The
separability_note's "record-dependency class only" undersells Ca's D2/R68 legs
and omits C's DECITED ledger read. Smallest safe correction: amend
separability_note to name the third edge (C→O via DECITED/APPEND envelope) and
relabel Ca's D2/R68 legs as state-consumption (bounded to ruling-class
consistency, not ruling truth). No claim needs splitting.

## Sizing summary vs the prompt's three questions

1. 24 rows: right ballpark (22–26 band, register-driven), but "exactly" is a
   convention frozen as a hard bound — fixable with a derivation note; not a
   canonical-judge rejection on its own.
2. O: one claim in topology, but the predicate is tool-shaped while the work is
   settlement-shaped — ruling semantics ride entirely on review-only + audit
   seats; retire/split rulings are unexecutable under the frozen mutable set
   while the claim text still names them. This is a real defect in the
   instrument/model contract, not a tradeoff.
3. Separability: real coupling exists (C reads O's ledger; Ca reads O's mutated
   state), acyclic and topology-enforced — but under-declared in claims.json.
   Class: fixable defect (documentation of the dependency graph), not a
   structural failure.

Installs: none. Read-only git/jj only.
Report: .ufo/waves/round-68/w1/CriticSizing.md
