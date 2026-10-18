# Finding disposition workflow — turning gate findings into design debt, never clearance

- topic: The design workflow for **dispositioning a gate's findings**: read each finding's id and severity (`fail` / `hold` / `note`), classify it as a design defect, an owed form, a tolerated artifact, or a false positive, route it to the design seat that owns the fix, and record the disposition so the next run can be compared. Covers the severity ladder, the disposition record, the rule that a `hold` is debt and a `note` is information, and why a disposition — and a green re-run — is never a clearance or canon. Reference method and design workflow only; canon belongs to lore-shokunin.
- gap filled: the synthesis partition carries consistency and verification checklists (`consistency-verification-checklist.md`, `symbolism-consistency-rules.md`) but no entry states the **finding-to-disposition loop** — how a gate's output becomes owned design work, and how the severities map to it. Absence sweep 2026-10-18: `grep -rln "disposition\|finding severity\|design debt" corpus/knowledge/synthesis/` → 0 files (the term lives in the verification and provenance entries, not as a design workflow).
- sources:
  - KTD-FD-S-0001 — `examples/culture-d4/ASSEMBLY.md` §3: the measured gate runs over the D4 packet — `naming-collision-gate` exit 1 with 8 findings (`PHON-INVENTORY` FAIL ×6, `NAME-NEAR` REVIEW ×1, `CROSS-HOLD` HOLD ×1), `phonology-sanity-gate` exit 1 with one `A-CLASS` REVIEW, and three gates exit 0 with 0 findings. The raw material a disposition works on. NON-CANON drill record.
  - KTD-FD-S-0002 — `examples/culture-d4/ASSEMBLY.md` §4 and `examples/culture-d4/brief.md` §"Named hold set": the disposition the round actually made — the six `PHON-INVENTORY` lines are the glosses the typed routing replaces, and the six `D4L-FORM-UNRESOLVED` holds are “open design debt, never a clearance”. The disposition is written before the fix exists.
  - KTD-FD-S-0003 — `examples/culture-d4/expected-holds.json` and `reports/round-18/d4/holds.md` §0: the committed disposition set (`counts {hold 15, note 1, fail 0}`) and the reconciliation that every delta is dispositioned as engine-defect or declaration-defect.
  - KTD-FD-S-0004 — measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` — the severity split a disposition reads.
  - KTD-FD-S-0005 — `corpus/knowledge/verification/to-verify-triage-protocol.md` §2 (priority ladder P0–P3, with immediate containment per priority) and §1 (evidence states). The queue discipline a disposition borrows for design findings.
  - KTD-FD-S-0006 — `corpus/knowledge/verification/provenance-audit-ledger-format.md` §8 (append-only; corrections are new entries) and `corpus/knowledge/verification/verification-method-overview.md` §6 (fail-closed verdicts: UNKNOWN is not PASS). The record shape and the fail-closed rule the disposition must satisfy.
  - KTD-FD-S-0007 — `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md` and `corpus/knowledge/verification/label-channel-routing-verification.md` (this lane, round 19): the check-side procedures that consume a disposition. A disposition without a check-side counterpart is an opinion.
  - KTD-FD-S-0008 — `corpus/knowledge/synthesis/consistency-verification-checklist.md` and `worldbible-integration-contract.md` §4/§9 (frozen manifests, pinned versions, no auto-upgrade). The handoff the disposition feeds: a packet with open holds is handed off as open work.
  - KTD-FD-S-0009 — Dijkstra, Edsger W. (1972), “The Humble Programmer,” *Communications of the ACM* 15(10): 859–866, doi:10.1145/355604.361591. A green re-run shows the presence, never the absence, of defects — why a disposition is bounded evidence.
  - KTD-FD-S-0010 — Yue Jia and Mark Harman (2011), “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5): 649–678, [doi:10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62). A disposition that no re-run can contradict is not a disposition; cited as a design rule.
- calibration: the disposition loop is this lane's house policy, not a published standard; Jia–Harman (a survey of a contested technique) and Dijkstra are cited as design rules, never as laws; the D4 severity counts are NON-CANON drill records.
- couples: synthesis — `consistency-verification-checklist.md`, `symbolism-consistency-rules.md`, `hold-set-contract-in-brief.md`, `generated-artifact-lifecycle.md`, `typed-label-routing-workflow.md`, `worldbible-integration-contract.md`; verification — `../verification/pre-declared-hold-set-reconciliation.md`, `../verification/to-verify-triage-protocol.md`, `../verification/provenance-audit-ledger-format.md`, `../verification/verification-method-overview.md`, `../verification/gate-battery-surface-verification.md`; tooling — `tools/d2-typed-labels.py`, `tools/gates/*.py`, `examples/culture-d4/expected-holds.json`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the D4 gate-run and hold-set records, the round-18 reconciliation receipt, and this round's re-measurement of the severity split; the disposition workflow is this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: projector run exit 1 with `stats {fail 0, hold 15, labels 74, note 1}`; `examples/culture-d4/expected-holds.json` read → `counts {hold 15, note 1, fail 0}`. Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The D4 gate-run receipts were read by path, not re-executed.
- recheck: whenever a gate's severity vocabulary or exit-code semantics changes, or the packet's finding set changes; before treating a disposition as closure; and whenever a disposition is revised (corrections are new entries, never rewrites).

## 1. What this workflow licenses

- A **loop**, not a verdict: it tells a designer how to take a gate's output and turn it into owned work with a record. It does not decide whether a finding is acceptable — that judgement is written down and reviewable.
- Disposition is **where design debt becomes visible**: a finding read and left unrecorded is indistinguishable from a finding never seen.
- A disposition is **not closure**: a `hold` dispositioned as “owed” stays owed until the form exists; a re-run that still holds is the expected reading, not a failure of the disposition.

## 2. The severity ladder and what each level owes

| severity | meaning in this lane | disposition it owes | it is never |
|---|---|---|---|
| `fail` | the artifact contradicts a rule the gate enforces | a fix or an explicit block; a fail carried into a handoff must be named | a hold, a note, or a warning |
| `hold` | the artifact is unresolved: an owed form, a `(to-verify)` row, a conflict carried | an owner, a reason, and a queue item; stays open | approval, or a pass |
| `note` | information the gate emits without blocking (e.g. a declared conflict) | a read and a disposition (“carried”, “accepted as information”) | a silent drop |
| `REVIEW` (legacy gates) | a manual-review request (e.g. `A-CLASS`, `NAME-NEAR`) | a named reviewer and a recorded outcome | a pass by default |

The measured D4 set is `fail 0 / hold 15 / note 1`; the raw gate runs add
`REVIEW` rows (`A-CLASS` ×1, `NAME-NEAR` ×1) and a `CROSS-HOLD` hold for the
missing real-language sweep.

## 3. The disposition record

| field | required contents | why |
|---|---|---|
| finding id + where | the gate's own id and the record key (`D2L-FORM-UNRESOLVED` at `GAR-01`) | lets the next run be compared row by row |
| class | design defect / owed form / tolerated artifact / false positive / external block | separates work from noise |
| owner | the seat or artifact that owns the fix | an unowned finding is not work |
| action | the concrete next step, or the reason there is none | “will address later” is not an action |
| evidence | the source edit, new file, or recorded decision that closes or carries it | a disposition without evidence is an opinion |
| run revision | the gate revision and input digest the finding came from | a disposition without a revision is unreproducible |
| non-clearance note | that the disposition is debt, never a clearance | keeps the handoff honest |

## 4. The loop

| step | action | check |
|---|---|---|
| D1 collect | run the packet's gates; collect every finding with its severity and where-key | exit codes read per the gate's own semantics (0/1/2), never collapsed |
| D2 classify | assign each finding a class (§3) | a finding that fits no class is a finding against the gate, not a shrug |
| D3 route | assign an owner and an action | an unowned finding stays open by construction |
| D4 record | write the disposition record and hand it off as open work | the record is append-only; a revision is a new entry |
| D5 re-run | after the fix, re-run the gates and compare | a finding that disappears with no source change is itself a finding |
| D6 report | state what remains open | a handoff that reports only the green re-run hides the debt |

## 5. What the loop never licenses

- **A disposition is not closure.** Recording “owed” does not make the form exist; the hold survives until the source changes.
- **A green re-run is not a cleared packet.** It shows the findings that were there are gone; it does not show none remain (Dijkstra).
- **A `note` is not nothing.** A note read and not dispositioned is a silent drop.
- **A false-positive disposition needs a rule, not a feeling.** “The gate is wrong” requires naming the gate rule and why it does not apply; otherwise the disposition is a blessing.
- **A disposition is not canon.** It records design work on a non-canon artifact; canon belongs to lore-shokunin.

## 6. Decision record — the disposition rules this workflow adopts

1. **Adopted:** every finding gets a disposition record with class, owner, action, evidence, and run revision (§3–§4). Consequence: a finding left unrecorded is a defect in the process, not a quiet pass.
2. **Adopted:** a `hold` is design debt and stays open until its source changes; a `note` is dispositioned as carried or accepted (§2). Consequence: a re-run that still holds is the expected reading.
3. **Adopted:** a false-positive disposition names the gate rule and why it does not apply; a finding that fits no class is escalated as a finding against the gate (§4 D2, §5). Consequence: “the gate is wrong” is a claim with evidence, not a dismissal.
4. **Adopted:** the disposition record is append-only and names the run revision (§3). Consequence: a disposition is reproducible and its revision history is preserved.
5. **Rejected:** treating a disposition, or a green re-run, as a clearance or as canon (§5). Reason: both assert bounded progress, not soundness.
6. **Open (to-verify):** whether the six `PHON-INVENTORY` FAIL rows in the legacy D4 gate run should be retired once the typed routing is the only path, or kept as a regression that the routing must keep removing. Owner: this lane's D/O boundary; not disposed here.
