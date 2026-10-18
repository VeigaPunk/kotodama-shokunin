# Handoff v3 — uncertainty plan for the D4 claim set

- topic: How each D4 claim row gets its `uncertainty {status, basis}`: the
  status decision table, the clause grammar and its validation legs, the census
  the v3 packet must hit, the owner-routing rules for `unresolved` rows, the
  one status that was a function of another seat's evidence (now landed), and
  the moves the plan forbids. Written for the packet seat (which types the
  rows) and the audit seat (which re-derives them independently).
- sources: `reports/round-15/handoff/v2-design.md` §2 (schema, enum, grammar,
  the zero-boilerplate checks, the decision table this plan extends);
  `tools/harness/packet_uncertainty.py` (the validator, its measured codes and
  `--require-oq` leg); `corpus/knowledge/verification/
  to-verify-triage-protocol.md` §1 (status vocabulary crosswalk) and
  `provenance-audit-ledger-format.md` §1 (`supported` ≠ improved ≠ canon);
  `examples/culture-d4/typed-labels.d4.yml` (coverage, findings, stats, the
  era-reconciliation basis), `expected-holds.json`, `components/01-brief.yml`
  (`hold_set_declaration`); `reports/round-18/d4/holds.md` (the
  declared-vs-emitted reconciliation) and `determinism.md` (the D2 pre-change
  gate bytes); `reports/round-19/validation.json` (the wart routing);
  `tools/assemble-d4-typed.py` and `tools/d2-typed-labels.py` (the live
  per-family behaviour measured 2026-10-18).
- couples: `claims-map.md` (the rows being typed); `design.md` §2 rules and §4
  flip rule; the packet seat's `validation` rows (each basis witness must be a
  recorded command or a measured byte, not prose); the freeze seat's census
  pin.
- taken-from: the v2 schema and its measured validator behaviour; the D4
  records' own states (holds, `(to-verify)` lines, residuals); nothing is
  invented that the bytes do not carry.
- verified-at: 2026-10-18 — the plan's census and grammar were exercised: the
  twelve rows validated at `claims=12 findings=[]`; five mutations produced
  `U-BASIS-DUPLICATE`, `U-BASIS-NO-RESTRICTION`, `U-BASIS-NO-OWNER`,
  `U-STATUS-VOCAB`, `U-BASIS-SHORT` (`review.md` §3). The D4-CL08 flip was
  then measured against the live tree (`review.md` §4): the projection's basis
  now names the D4 packet with an explicit skip, the adapter's selftest is
  12/12 with no `examples/culture-d2` in its mirror, and the D2 control stays
  byte-identical.
- recheck: before the v3 packet is frozen; whenever the O seat's alias bytes
  move again (the flip is symmetric — a revert re-flips D4-CL08); whenever a D4
  byte, tool or receipt cited by a basis moves.

## 1. The schema, restated for v3 (no change from v2)

Each claim carries exactly `uncertainty: {status, basis}`:

- `status ∈ {supported, partial, unresolved}` — case-sensitive lowercase, no
  other token (`tentative`, `high`, `unknown` are builder errors; measured:
  `U-STATUS-VOCAB`);
- `basis` is one sentence-set with the literal prefixes `grounding:`,
  `restriction:`, `open:`, `owner:` — one `grounding:` always; `restriction:`
  iff `partial`; `open:` **and** `owner:` iff `unresolved`; a slot may hold at
  most once;
- `basis` is unique across the whole ledger after whitespace normalization, at
  least 40 characters, and free of boilerplate tokens (measured: basis
  `grounding: unknown` → `U-BASIS-SHORT`; duplicate basis →
  `U-BASIS-DUPLICATE`);
- `evidence_status` stays a separate, independent dimension and is never
  merged into or restated by the status (contract §6; triage protocol §1
  "keep three independent fields");
- severity inherits upward only: an edge or record derived from a
  `partial`/`unresolved` claim carries at least that status
  (`supported < partial < unresolved`).

## 2. Decision table — which status a D4 row gets

Extends v2-design §2.4 with the archetypes the D4 surface actually produced:

| claim archetype (as it appears in D4) | evidence_status | status | basis witness shape |
|---|---|---|---|
| A design rule or staged structure the delivered packet records and a gate/check reproduces (eras ER-01..04; rank rules RK-01..04) | invented | `supported` | the record block + its ids + the check that re-reads them |
| An authored design record whose scope is the design itself (the drill's non-canon declaration; provenance rows) | invented | `supported` | the scope/registry records, with the wording's own design-only scope kept |
| A projection of the packet's own records that is deterministic and equals its committed file (the typed channel, the hold set, the reconciliation) | derived projection (author-side) | `supported` | the coverage/stats/counts block re-read live + the equality leg |
| A committed expectation that differs from an earlier declaration and is reconciled by a filed delta (the brief's 6-row set vs the emitted 15/1/0) | derived projection (author-side) | `supported` | the committed counts + the reconciliation receipt naming the delta |
| A rule whose object is a declared completeness with a named unmodelled leg (the loan ledger; the sixth slot's owed kind) | invented | `partial` | `grounding:` the ledger/slot records; `restriction:` the exact unmodelled or conditional leg |
| A negative/screening statement about the lane's own process ("no sweep performed") | invented (fact about the lane's process) | `supported` for the absence as worded | the provenance record; the dependent clearance question goes to `open_questions`, never into this status |
| A hold or residual inherited from another family's normalization (D2's 13 unresolved rank items, 3 handles, 4 conflicts inside the D4 projection) | derived projection (author-side), holds open | `unresolved` | `grounding:` the coverage block; `open:` the item set; `owner:` kotodama |
| A dependency on another seat's work, **while it has not landed** (the alias leg before the round-20 O edits) | derived projection (author-side), hold open | `unresolved` | `grounding:` the measured locations; `open:` what has not landed; `owner:` the seat that owns it |
| The same dependency **after it lands, with the run measured** (the alias leg now) | derived projection (author-side) | `supported` | the D4-side basis (declared source or explicit skip) + the run whose mirror lacked the foreign tree + the unchanged-foreign-path control |
| A candidate world-fact awaiting a baseline/entity keys | candidate world-fact | `unresolved` | `open:` no baseline/entity keys; `owner:` lore |

Crosswalk kept from v2-design §2.4: triage protocol §1 maps
`Unknown`→`unresolved`, `Scoped-supported`/`Contested`→`partial` (the
restriction preserves the disagreement), `Inspected` with unqualified
wording→`supported`; `Located` alone never rises above `partial`.
Provenance-audit format §1: `supported` does not mean improved, accepted,
import-ready or canon.

## 3. The v3 census (what the packet must hit; the freeze seat pins it)

**Live census (the landed branch, measured 2026-10-18; `review.md` §4):**

| source | claims | supported | partial | unresolved |
|---|---|---|---|---|
| v2 rows carried verbatim (D2 ×2, D3 ×13) | 15 | 8 | 5 | 2 |
| D4 rows (`D4-CL01..D4-CL12`) | 12 | 8 | 2 | 2 |
| **v3 total** | **27** | **16** | **7** | **4** |

- The census is asserted by the exercise (`E2E-COUNT` on mismatch) and pinned
  by the v3 baseline; the audit re-derives it from the ledger rows
  independently.
- The v2 subset's statuses must not drift: the v2-subset equality control
  (`design.md` §6) compares the 15 rows (status and basis included) against the
  filed v2 packet bytes; any difference is `E2E-DIGEST`.
- **Pre-flip census (admissible only if the O bytes are reverted):**
  **15 supported / 7 partial / 5 unresolved** (D4-CL08 `unresolved`). The plan
  declares both censuses and requires the packet's `validation` to name which
  one it measured and why; the flip is symmetric, and a revert of the O bytes
  re-flips the row and the census.

## 4. Owner routing for `unresolved` rows (`--require-oq` leg)

Every `unresolved` claim needs an `open_questions` row that names it (the
harness leg runs with `--require-oq` and must report zero findings):

| unresolved claim | OQ row | owner | blocking scope |
|---|---|---|---|
| `D4-CL09` | `OQ-V3-05` | kotodama | the affected D2 rank records and the six garment terms |
| `D4-CL12` | `OQ-V3-06` | lore-shokunin | non-blocking |
| v2 rows `D2-CL02`, `CL13` | `OQ-V2-03`, `OQ-V2-01` (carried) | kotodama / kotodama + lore | as filed |

`D4-CL08`'s row `OQ-V3-04` **retires with the flip** (the claim is now
`supported`; the harness's `--require-oq` leg ignores supported rows). The OQ id
is not reused: if the O bytes are reverted, the row returns as `OQ-V3-04`
re-opened in a new build, not as a silent edit.

Rules: an owner is a lane or seat, never "TBD"; a blocking claim must say what
it blocks and what it does not; an `open:` clause states the question, not the
symptom ("the per-family resolution has not landed" — not "the wart is
annoying").

## 5. The one evidence-keyed status: D4-CL08 (flip executed)

`design.md` §4 fixes the rule; this plan fixes the typing. The two admissible
forms:

- **Not landed** (the state measured earlier on 2026-10-18): `unresolved`, with
  the two then-live locations as the grounding (the projection's
  `era_reconciliation` basis naming the D2 component; the adapter's selftest
  mirror copy), the missing per-family resolution as `open:`, and the O seat as
  `owner:`.
- **Landed — now live:** `supported`, grounding the per-family resolution's
  measured behaviour: the projection's basis names the D4 packet's own records
  and an explicit skip; the adapter's selftest mirror no longer carries
  `examples/culture-d2` and passes 12/12; the D2 control is byte-identical. The
  `open:`/`owner:` clauses leave with the status.
- **Forbidden:** typing it `supported` on the strength of the round's intent,
  of a code change with no run, or of a run whose mirror still copied the D2
  tree (that run cannot distinguish a family-local resolution from the old
  cross-family read). The controls on the flip are: (a) the D4-side basis
  names the D4 packet or an explicit skip; (b) a d4 run exits 0 with no
  `examples/culture-d2` present; (c) the D2 path stays byte-identical — live
  measured: `tools/d2-typed-labels.py --selftest` exit 0, 50/50 checks, and
  `tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml`
  exit 0, 13/13 legs, stdout sha256
  `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` — the same
  digest the round-18 receipt recorded **before** the generalization, so the
  D2 output bytes did not move; (d) the negative control (the same run with
  the D2 tree restored still exiting 0) belongs to the O seat's own receipts,
  and the audit seat should demand it if the O claim files one.

## 6. Forbidden moves (each is a builder error, not a style choice)

1. Promoting a hold: no D4 status may rise because the round is closing; the
   12 form holds, 3 rank holds, 1 note, 13 unresolved rank items and 4
   conflicts stay open until their own owners resolve them.
2. Merging dimensions: `uncertainty.status` may not absorb `evidence_status`
   text, and neither may restate the other.
3. Boilerplate: a basis that names no locator, repeats a sibling's sentence,
   or restates the status word (measured rejections in §1).
4. Asserting canon, acceptance or clearance in any basis or statement — the
   gate's canon-verb traps reach basis cells (v2-design §4, probes C1/C2), and
   no D4 claim's support language may imply an import ruling.
5. Silently widening scope: a basis may not cite a file the v3 read set does
   not pin, and a link may not point outside the repo (the resolver's
   `L-PATH-OUTSIDE` / `L-PATH-MISSING`).
6. Re-typing a v2 row: the v2 ledger rows are carried verbatim; if a v2 basis
   genuinely needs repair, that is a v2-side correction filed as a new
   artifact, not an edit inside v3.

## 7. What the validator will and will not catch (measured, 2026-10-18)

- **Will catch:** off-vocabulary status, missing/duplicated clauses, thin or
  boilerplate basis, duplicate basis, and (with `--require-oq`) an unresolved
  claim with no OQ reference — five codes measured firing (§1, `review.md` §3).
- **Will not catch:** whether a `grounding:` witness *exists* — that leg is
  the packet seat's and the audit's (the link resolver resolves the `links:`
  specs; the basis's inline locators are re-resolved by the audit's own
  checker, as the round-15 audit did); and whether a basis's claim wording is
  actually narrower than its evidence. Both are named as audit obligations in
  `design.md` §7.
- **Gate-invisible by construction:** the shape gate cannot see this dimension
  (v2-design §1, probes D/E: a basis cell of `unknown` and the status token
  `tentative` both exit 0). The semantic teeth live in the two harness tools
  and in the audit's independent re-derivation — never in the shape gate.
