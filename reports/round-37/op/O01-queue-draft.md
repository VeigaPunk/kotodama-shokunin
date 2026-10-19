# O01 — round-33–36 defect-queue draft

**Status: partial, provisional draft; not an acceptance or completeness receipt.** The designated census `reports/round-37/scout/K02-defect-census.md` was absent at this draft cut. The queue below records source-backed, currently routeable candidates only; it does not claim to be the full defect set. `census_ids` is `null` (unknown), not an empty set. No item is marked `fixed-with-evidence`: O02's available fragment says no controls were run and could not evaluate any fixed row. O09's routing is used where filed, but remains explicitly provisional pending census reconciliation and O03 verification.

```json
{
  "schema": "kotodama-r37-defect-queue/1",
  "round": 37,
  "scope_rounds": [33, 34, 35, 36],
  "census_source": "reports/round-37/scout/K02-defect-census.md",
  "census_cut": null,
  "census_status": "missing-at-draft-cut",
  "census_ids": null,
  "queue_ids": [
    "F-C13-1",
    "F-C15-1",
    "RC-4",
    "R36-D-DECLARATION",
    "R36-D-F6",
    "OI-02",
    "R36-D-RL8",
    "R36-R7-READSET-13",
    "R36-ABSOLUTE-ROOT",
    "R36-README-DUPLICATE-HEADING",
    "R36-README-E3-PLACEHOLDERS",
    "R36-README-ORDER-CONTIGUITY-REVERIFY"
  ],
  "set_equality": {
    "status": "could-not-evaluate",
    "missing_ids": null,
    "extra_ids": null,
    "reason": "K02 census is absent; O05's independent skim explicitly says it is non-exhaustive and categories may overlap. No set comparison or count can be inferred.",
    "evidence": [
      "reports/round-37/op/O05-verify.md:3-12",
      "reports/round-37/op/O11-final.md:7,13-16"
    ]
  },
  "items": [
    {
      "id": "F-C13-1",
      "census_membership": "to-verify",
      "summary": "Historical in-tree receipt writes/restores breached the runner-isolation rule; the legacy guard-adoption debt remains distinct from the later absolute-root mechanism defect.",
      "origin_refs": [
        {"path": "LOG.md", "lines": "3548-3567", "record_kind": "incident-and-routing-record", "round": 33},
        {"path": "LOG.md", "lines": "3695-3698", "record_kind": "recurrence-record", "round": 36},
        {"path": "reports/round-36/cross/X02-conformance.md", "lines": "187-234", "record_kind": "conformance-finding", "round": 36}
      ],
      "also_reported_at": [
        "reports/round-34/op/O05-routing.md:241-257,282-289",
        "reports/round-37/op/O03-carry-verify.md:7",
        "reports/round-37/cross/X00-connector.md:16-18"
      ],
      "linked_records": [
        {"id": "RC-1", "path": "reports/round-36/calib/recount-ledger.json#/findings/RC-1", "relationship": "corroborating Ca filed-byte-drift measurement; Ca retains filed/observed readings and O retains defect lifecycle; writer attribution remains to-verify"}
      ],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator for routing/record; future operability/runner maintainer for prevention",
        "reason": "The historical runners and filed receipts are immutable; restoration and a clean later sample do not establish prevention. Per-write actor attribution remains to-verify, and later evidence reports recurrence.",
        "next_touch": "Round 38: before any publish-mode replay, assign the runner-maintainer work and verify a safe successor/containment path; preserve writer attribution as unknown unless evidence resolves it. Do not edit or execute the filed runners in-tree."
      }
    },
    {
      "id": "F-C15-1",
      "census_membership": "to-verify",
      "summary": "The stated numeral '12 standing open items' is reconstructed from a nine-row source table; no filed source establishes the expansion rule.",
      "origin_refs": [
        {"path": "reports/round-33/calib/open-items-ledger.json", "lines": "417-424", "record_kind": "finding", "round": 33},
        {"path": "SCORECARD.md", "lines": "593-600", "record_kind": "round-finding-summary", "round": 33}
      ],
      "also_reported_at": ["reports/round-33/calib/K03-open-items.md:45-53", "reports/round-37/plan/P02-oa-plan.md:36"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Integrator/C13/R05 for source reconciliation; integrator for any correction record",
        "reason": "The source's own count provenance says the number is reconstructed, and no evidence in the available records resolves the derivation. Preserve the filed historical wording rather than silently replacing it.",
        "next_touch": "Round 38: reconcile the numeral against its cited source table, record a supported count or retain the uncertainty in a new dated correction; do not rewrite the filed r33 record."
      }
    },
    {
      "id": "RC-4",
      "census_membership": "to-verify",
      "summary": "The r33 A3 gate pins a lane-open census literal (2655) and asserts equality after admission, making that census check self-invalidating as the tree grows.",
      "origin_refs": [
        {"path": "reports/round-36/calib/recount-ledger.json", "lines": "239-245", "record_kind": "recount-linked-finding", "round": 36},
        {"path": "reports/round-36/scout/K03-recount-scout.md", "lines": "346-348", "record_kind": "routed-gate-design-finding", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/cross/X00-connector.md:21"],
      "linked_records": [
        {"id": "RC-33-4", "path": "reports/round-36/calib/recount-ledger.json#/rows/RC-33-4", "relationship": "related r33 command measurement; retain Ca row separately and link it rather than cloning its counts into the defect queue"}
      ],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Integrator; future owner of the r33 A3 gate/runner",
        "reason": "The literal/equality design defect remains in filed bytes; a recount or matching command output does not repair the gate, and the filed runner must not be rewritten.",
        "next_touch": "Round 38 or the next runner-generation claim: replace the self-invalidating census predicate with a durable, non-self-referential check and verify it against an isolated copy."
      }
    },
    {
      "id": "R36-D-DECLARATION",
      "census_membership": "to-verify",
      "summary": "Round-36 D was rejected as declared because its 'register-form domain EMPTY' before-state was stale; nothing was landed under that failed claim.",
      "origin_refs": [
        {"path": "reports/round-36/validation.json", "lines": "49-78,145-165", "record_kind": "rejected-claim-receipt", "round": 36},
        {"path": "LOG.md", "lines": "3682-3689", "record_kind": "rejection-and-residue-record", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/cross/X00-connector.md:24", "reports/round-37/op/O11-final.md:21-23"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator/planner",
        "reason": "The rejected claim's historical evidence must remain rejected and unchanged; future work needs a truthful claim based on the already-landed forms and the separately identified residue.",
        "next_touch": "Round 38: append a corrected, scoped claim declaration and route only the verified residue to its implementation owner; do not reinterpret or edit reports/round-36/validation.json."
      }
    },
    {
      "id": "R36-D-F6",
      "census_membership": "to-verify",
      "summary": "The register coverage block lacks the forecast's derived_forms/derived_ok counters and no producer for those keys was found.",
      "origin_refs": [
        {"path": "reports/round-36/scout/K01-register-scout.md", "lines": "103-125,208-212", "record_kind": "residue-finding", "round": 36},
        {"path": "reports/round-36/validation.json", "lines": "53-59", "record_kind": "rejected-claim-residue", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/op/O09-routing.md:11"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator to assign the corrected-claim executor; future register/coverage maintainer",
        "reason": "No producer exists for the named counters; the rejected D claim did not implement them, and the actual measurements under different names are not equivalent to delivering the requested coverage keys.",
        "next_touch": "Round 38: scope the counter work in a truthful claim; if retained after scoping, assign implementation in round 45 and require a non-vacuous producer/control."
      }
    },
    {
      "id": "OI-02",
      "census_membership": "to-verify",
      "summary": "The head2 operation remains declared but has no delivered proper domain; the r36 residue is the same underlying item, not a second row.",
      "origin_refs": [
        {"path": "reports/round-33/calib/open-items-ledger.json", "lines": "90-115", "record_kind": "carried-design-debt", "round": 33},
        {"path": "reports/round-36/scout/K01-register-scout.md", "lines": "107-112,119-129", "record_kind": "reconfirmed-residue", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/op/O03-carry-verify.md:10", "reports/round-37/op/O09-routing.md:11"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator for claim scoping; operator for the design/acceptance decision; future D executor if implementation is approved",
        "reason": "The condition is explicitly disclosed and the operation is identity on the delivered tree; neither a rejected D claim nor the existing declaration resolves whether to author a domain or accept/retire it.",
        "next_touch": "Round 38: scope the operator decision and corrected claim; if the operation remains in scope, assign the design/implementation to the round-45 executor. Do not invent a domain or rewrite the r33 ledger."
      }
    },
    {
      "id": "R36-D-RL8",
      "census_membership": "to-verify",
      "summary": "The specified RL-8 era check is not implemented: the law can declare era but no gate grades the E0/E1 dating constraint.",
      "origin_refs": [
        {"path": "reports/round-36/scout/K01-register-scout.md", "lines": "130-138,215-216", "record_kind": "unimplemented-residue", "round": 36},
        {"path": "reports/round-36/validation.json", "lines": "53-59", "record_kind": "rejected-claim-residue", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/op/O09-routing.md:11"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator to assign the corrected-claim executor; future register-law maintainer",
        "reason": "The law is specified but unimplemented, and nothing landed under the rejected r36 D claim.",
        "next_touch": "Round 38: scope the era leg in a corrected claim; if retained, assign the implementation to round 45 and require a negative control for a form dated before its availability."
      }
    },
    {
      "id": "R36-R7-READSET-13",
      "census_membership": "to-verify",
      "summary": "The r7 frozen input roster omits 13-register-law.yml although the packet source manifest names 13 D4 components; A01 adjudicated this as a roster/completeness defect, not a demonstrated integrity bypass.",
      "origin_refs": [
        {"path": "reports/round-34/handoff/declared-in-r7/expected.json", "lines": "124-183", "record_kind": "frozen-read-set", "round": 34},
        {"path": "reports/round-37/adj/A01-freeze-adjudication.md", "lines": "24-35", "record_kind": "independent-adjudication", "round": 37}
      ],
      "also_reported_at": ["reports/round-36/scout/K01-register-scout.md:140-192", "reports/round-37/op/O09-routing.md:10"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Integrator/renderer maintainer",
        "reason": "A01 confirms the exclusion is undocumented even though the separate component-digest check catches changed bytes. The filed r7 packet and freeze remain immutable; no integrity bypass is claimed.",
        "next_touch": "Round 38: in a successor baseline, either add direct read-set membership or explicitly define/document the transitive-read-set contract while retaining the component-digest control. Do not re-freeze or edit the filed r7 pair."
      }
    },
    {
      "id": "R36-ABSOLUTE-ROOT",
      "census_membership": "to-verify",
      "summary": "The r34/r35 runners hard-code the live repository root and chdir there, so a plain clone/archive does not contain their publish-mode receipt writes.",
      "origin_refs": [
        {"path": "reports/round-34/run-validation.py", "lines": "10,26,527-535", "record_kind": "unsafe-root-and-publish-path", "round": 34},
        {"path": "reports/round-35/run-validation.py", "lines": "9,36,496-505", "record_kind": "unsafe-root-and-publish-path", "round": 35},
        {"path": "reports/round-36/cross/X02-conformance.md", "lines": "187-234", "record_kind": "mechanism-finding", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/op/O08-gap-fill.md:5-13", "reports/round-37/op/O12-gap-fill.md:5-12", "reports/round-37/op/O09-routing.md:7-10"],
      "linked_records": [
        {"id": "F-C13-1", "path": "LOG.md:3548-3567; reports/round-36/cross/X02-conformance.md:187-234", "relationship": "related isolation incident/policy breach but distinct mechanism-level runner-design defect; do not merge the two lifecycle rows"}
      ],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-38 operability/runner maintainer, to be assigned by the round-37 integrator",
        "reason": "The absolute ROOT/chdir defeats plain-copy containment on the publish path; filed runners cannot be edited, and --check returning before publication does not repair the hazard. Per-write actor attribution is to-verify.",
        "next_touch": "Round 38, before any publish-mode recount/replay: provide a copy-relative successor runner or explicit containment and verify that its publish invocation writes only inside the isolated copy."
      }
    },
    {
      "id": "R36-README-DUPLICATE-HEADING",
      "census_membership": "to-verify",
      "summary": "The live corpus README repeats its title line at lines 1 and 3.",
      "origin_refs": [
        {"path": "corpus/README.md", "lines": "1,3", "record_kind": "current-live-index-defect", "round": 36},
        {"path": "reports/round-37/op/O09-routing.md", "lines": "12,32", "record_kind": "newly-reported-current-defect", "round": 37}
      ],
      "also_reported_at": [],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator to assign a corpus-index editor",
        "reason": "The duplicate is present in the current live bytes and is outside O01's write scope; no correction or independent control is filed.",
        "next_touch": "Round 38 corpus-index integration: remove the redundant title in a permitted new correction, then recheck the complete index and preserve prior revision history."
      }
    },
    {
      "id": "R36-README-E3-PLACEHOLDERS",
      "census_membership": "to-verify",
      "summary": "Two literal __E3_PLACEHOLDER__ lines remain in the live corpus README where the r36 delta called for actual sorted rows.",
      "origin_refs": [
        {"path": "corpus/README.md", "lines": "214-215", "record_kind": "current-live-index-defect", "round": 36},
        {"path": "reports/round-36/cov/C02-audit-delta.md", "lines": "223-258", "record_kind": "intended-row-repair", "round": 36},
        {"path": "reports/round-37/op/O09-routing.md", "lines": "12,32", "record_kind": "newly-reported-current-defect", "round": 37}
      ],
      "also_reported_at": [],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "Round-37 integrator to assign a corpus-index editor",
        "reason": "The current bytes contain placeholders rather than valid index rows; the r36 audit delta provides the intended content, but no repair is evidenced in the current README.",
        "next_touch": "Round 38 corpus-index integration: replace the placeholders with the intended rows or remove them as appropriate, then recheck row count, order, contiguity, topic equality and the README sweep."
      }
    },
    {
      "id": "R36-README-ORDER-CONTIGUITY-REVERIFY",
      "census_membership": "to-verify",
      "summary": "The r36 README row-order and section-contiguity defects were reported repaired in the staged/revised delta, but O02 has not independently rechecked the delivered bytes this round.",
      "origin_refs": [
        {"path": "reports/round-36/cov/C02-audit-delta.md", "lines": "159-175,408-417", "record_kind": "original-findings-and-repair-control", "round": 36},
        {"path": "reports/round-36/cov/C03-verify.md", "lines": "166-234,325-351,382-385", "record_kind": "independent-r36-repair-verification", "round": 36},
        {"path": "SCORECARD.md", "lines": "660-661", "record_kind": "round-36-integration-record", "round": 36}
      ],
      "also_reported_at": ["reports/round-37/op/O02-controls-verify.md:5-9", "reports/round-37/op/O06-verify.md:3-8"],
      "linked_records": [],
      "disposition": "carried-with-owner+reason+next-touch",
      "carry": {
        "owner": "O02 non-author verifier for the recheck; integrator for any further correction",
        "reason": "R36 reports an independently checked repair, but O02 explicitly ran zero fix controls because O01 and K02 were missing. The current README also has separate new defects; the old repair must not be treated as a queue-wide fixed disposition without the assigned O02 evidence.",
        "next_touch": "Immediately after K02 and O01 land, O02 rechecks the current README row order and section contiguity with an independent control; if it cannot be verified before closure or fails, O09 routes the residual correction to round 38."
      }
    }
  ],
  "unresolved_candidates": [
    {
      "source": "reports/round-36/cov/C01-audit.md:256-263; reports/round-36/cov/C03-verify.md:246-281,440-469",
      "candidate_ids": ["C01-F1-stager-target", "C01-F2-hour-boundary", "C01-F3-term-count", "C01-F4-drift-disclosure", "C01-F5-target-path", "C01-F6-pointer-coverage", "C03-couples-fire-fuel"],
      "membership": "to-verify",
      "reason_not_yet_queued": "O09 says the timekeeping-spare/couples findings must first be re-verified by the assigned round-37 adjacency scan; no A02 result is available here. The current timekeeping entry still quotes the stale 201-file/28-term sweep at lines 4 and 8, so these are not treated as absent or resolved.",
      "next_touch": "A02 rechecks the landed entry; O03 then confirms owner/reason/next-touch and O09 files the round-38+ route for each surviving defect."
    },
    {
      "source": "reports/round-35/adj/audit-assembled.md:192-318",
      "candidate_ids": ["R35-A-F1", "R35-A-F2", "R35-A-F3", "R35-A-F4", "R35-A-F5", "R35-A-F6", "R35-A-F7", "R35-A-F8", "R35-A-F9", "R35-A-F10", "R35-A-F11", "R35-A-F12", "R35-A-F13"],
      "membership": "to-verify",
      "reason_not_yet_queued": "The round-35 assembled audit records F1-F13 with owners and differing states, but K02's source census and the per-row O03 carry check are absent. Do not infer that every named observation is a distinct open defect or that the partially answered rows are fixed.",
      "next_touch": "Reconcile each census ID to its audit finding and later resolution evidence after K02/O03 land; route only unresolved defect rows, retaining aliases for merged mentions."
    },
    {
      "source": "reports/round-33/calib/open-items-ledger.json:59-415",
      "candidate_ids": ["OI-01", "OI-02", "OI-03", "OI-04", "OI-05", "OI-06", "OI-07", "OI-08", "OI-09", "OI-10", "OI-11", "OI-12"],
      "membership": "to-verify",
      "reason_not_yet_queued": "The ledger includes design debts, an explicit constraint-not-defect, operator/lore-owned items, historically carried rows, and four rows previously labelled fixed-with-evidence. Those historical classes cannot be imported as r37 fixes; K02 must determine which findings belong in this round's defect census, then O02 must freshly verify any fixed disposition.",
      "next_touch": "K02 reconciles the ledger's canonical IDs and aliases; O02 independently verifies any proposed fixed row; O03 checks every carry. OI-02 is already represented above and must not be duplicated."
    },
    {
      "source": "reports/round-37/cross/X00-connector.md:19-23; reports/round-36/calib/recount-ledger.json:224-245",
      "candidate_ids": ["RC-2", "RC-3", "RC-34-3", "RC-34-5", "R36-README-PREDICTION-DELIVERY"],
      "membership": "to-verify",
      "reason_not_yet_queued": "These are recount measurements or revision-boundary readings unless K02 supplies separate defect evidence. RC-3 is explicitly no-action; RC-2 must not turn the accurate r34 historical count into a bad filed value. The README prediction/delivery discrepancy is recorded but its defect class and originating owner remain unresolved.",
      "next_touch": "K02 classifies each candidate against its underlying source; keep Ca rows in the recount ledger and add only independently evidenced defect lifecycle rows to this queue."
    },
    {
      "source": "reports/round-37/op/O09-routing.md:14-16; SCORECARD.md:620-626,630-649",
      "candidate_ids": ["R34-N1", "CO4-seat-count-64-vs-63", "R35-route-402", "R36-route-402"],
      "membership": "to-verify",
      "reason_not_yet_queued": "R34-N1 was explicitly closed in r35 and is not the absolute-root defect. CO4 is a named recorded deviation; the r35/r36 402 observations were declared fallback routes, not defects by themselves. Do not reopen or count these as defects absent a distinct census finding.",
      "next_touch": "K02 reconciles the names to source findings; preserve the historical r34/r35/r36 records and their declared route/status."
    }
  ],
  "routing": {
    "status": "provisional; not a zero-unowned or complete-routing result",
    "routes": [
      {"item_id": "F-C13-1", "destination_round": 38, "owner": "Round-38 operability/runner maintainer; assigned by round-37 integrator", "action": "Verify preventive successor/containment before any publish-mode replay; preserve actor attribution as to-verify.", "source": "reports/round-37/op/O03-carry-verify.md:7; reports/round-36/cross/X02-conformance.md:187-234"},
      {"item_id": "F-C15-1", "destination_round": 38, "owner": "Integrator/C13/R05", "action": "Reconcile the reconstructed numeral and file a dated correction or retain uncertainty without rewriting the historical record.", "source": "reports/round-33/calib/open-items-ledger.json:417-424"},
      {"item_id": "RC-4", "destination_round": 38, "owner": "Integrator and future r33-A3 gate maintainer", "action": "Replace the self-invalidating literal census predicate in a successor gate/claim and verify it on an isolated copy.", "source": "reports/round-37/cross/X00-connector.md:21; reports/round-36/scout/K03-recount-scout.md:346-348"},
      {"item_id": "R36-D-DECLARATION", "destination_round": 38, "owner": "Round-37 integrator/planner", "action": "Append a truthful, scoped claim for surviving residue; leave the rejected r36 validation evidence untouched.", "source": "reports/round-37/cross/X00-connector.md:24; reports/round-37/op/O09-routing.md:11"},
      {"item_id": "R36-D-F6", "destination_round": 38, "owner": "Round-37 integrator to assign a round-45 register/coverage executor", "action": "Scope the counter producer in a corrected claim; implement only if retained and verify non-vacuously.", "source": "reports/round-37/op/O09-routing.md:11"},
      {"item_id": "OI-02", "destination_round": 38, "owner": "Round-37 integrator for scope; operator for design decision; round-45 executor if approved", "action": "Decide whether to author a head2 domain or accept/retire the declared operation; do not invent domain content.", "source": "reports/round-33/calib/open-items-ledger.json:90-115; reports/round-37/op/O09-routing.md:11"},
      {"item_id": "R36-D-RL8", "destination_round": 38, "owner": "Round-37 integrator to assign a round-45 register-law maintainer", "action": "Scope the era-check leg in a corrected claim; implement if retained with a pre-availability negative control.", "source": "reports/round-37/op/O09-routing.md:11"},
      {"item_id": "R36-R7-READSET-13", "destination_round": 38, "owner": "Integrator/renderer maintainer", "action": "Use a successor baseline to add direct read-set membership or document the transitive contract; do not re-freeze or edit the filed r7 pair.", "source": "reports/round-37/adj/A01-freeze-adjudication.md:24-35; reports/round-37/op/O09-routing.md:10"},
      {"item_id": "R36-ABSOLUTE-ROOT", "destination_round": 38, "owner": "Round-38 operability/runner maintainer; assigned by round-37 integrator", "action": "Deliver a copy-relative successor or explicit containment and verify that publish writes remain in the isolated copy.", "source": "reports/round-37/op/O09-routing.md:7-10"},
      {"item_id": "R36-README-DUPLICATE-HEADING", "destination_round": 38, "owner": "Round-37 integrator to assign a corpus-index editor", "action": "Remove the redundant title in a permitted correction and recheck the index.", "source": "reports/round-37/op/O09-routing.md:12"},
      {"item_id": "R36-README-E3-PLACEHOLDERS", "destination_round": 38, "owner": "Round-37 integrator to assign a corpus-index editor", "action": "Replace/remove the placeholders, then recheck count, order, contiguity, topic equality and the README sweep.", "source": "reports/round-37/op/O09-routing.md:12"},
      {"item_id": "R36-README-ORDER-CONTIGUITY-REVERIFY", "destination_round": 38, "owner": "O02 verifier; integrator if control fails", "action": "O02 first rechecks after K02/O01 land; route any residual repair to round 38 if the assigned check does not verify it before closure.", "source": "reports/round-37/op/O02-controls-verify.md:5-9; reports/round-37/op/O09-routing.md:5,21-22"}
    ],
    "not_routed_yet": ["unresolved_candidates: timekeeping findings await A02, r35 F1-F13 and the r33 OI ledger await census reconciliation, and RC-2/README prediction class await K02; O09 explicitly does not claim these routes complete"]
  }
}
```

## Owed

- `reports/round-37/scout/K02-defect-census.md` — absent at this cut. Reconcile every canonical census ID against this draft; replace `census_ids: null` only from the filed census and report missing/extra IDs explicitly.
- `reports/round-37/op/O02-fix-verify.md` — absent. `O02-controls-verify.md` is present but records `could-not-evaluate` and zero controls run (`:5-9`); none of the prior-round repairs may be promoted to `fixed-with-evidence` from that record.
- `reports/round-37/op/O03-carry-verify.md` — present as a partial conditional cross-check, not a per-row verification of this eventual queue (`:3,15-20`). Re-run it against every carried row before routing completeness is claimed.
- `reports/round-37/op/O05-verify.md` and `O06-verify.md` — their current findings are `could-not-evaluate`; rerun census equality and disposition sanity after K02/O01/O02 land.
- `reports/round-37/op/O09-routing.md` — now present and used above; its own table is provisional and asks for reconciliation with the missing census/queue (`:5,18-23`). It does not establish zero unowned rows.
- `reports/round-37/adj/A02` result — required before routing the timekeeping spare/couples findings, per O09 `:16,23`.
- Preserve r36 D's rejected status; do not run `reports/round-*/run-validation.py` or alter filed bytes.

## Citations

- `reports/round-37/claims.json:19-24`; `reports/round-37/targets.json:3-8,12,36-47,74` — O thresholds, allowed output, runner restriction, and rejected-r36 boundary.
- `reports/round-37/plan/P02-oa-plan.md:7-36` — queue schema, linked-record rule, no fixed status without O02, carry fields and round-38+ routing requirement.
- `reports/round-37/op/O02-controls-verify.md:5-9`; `O03-carry-verify.md:3-13,15-24`; `O05-verify.md:3-12`; `O06-verify.md:3-11`; `O09-routing.md:5-23`; `O11-final.md:7,13-16,25-32` — verifier limits, conditional owner checks and provisional routes.
- `reports/round-33/calib/open-items-ledger.json:59-415,417-459`; `SCORECARD.md:593-600`; `LOG.md:3548-3567,3695-3698` — historical OI statuses, F-C15-1 and F-C13-1.
- `reports/round-36/calib/recount-ledger.json:211-245`; `reports/round-36/scout/K03-recount-scout.md:346-348`; `reports/round-37/cross/X00-connector.md:16-24` — RC overlap decisions, RC-4, and separation of measurement from defect lifecycle.
- `reports/round-36/validation.json:49-78,145-165`; `reports/round-36/scout/K01-register-scout.md:103-139`; `reports/round-37/op/O09-routing.md:10-11` — D rejection, remaining F-6/head2/RL-8 work, and read-set route.
- `reports/round-36/cross/X02-conformance.md:187-234,687-697`; `reports/round-37/op/O08-gap-fill.md:5-13`; `O12-gap-fill.md:5-12`; `reports/round-37/op/O09-routing.md:7-10` — r34/r35 absolute-root mechanism and distinction from incident/actor attribution.
- `reports/round-36/cov/C01-audit.md:256-263`; `reports/round-36/cov/C02-audit-delta.md:153-182,223-258`; `reports/round-36/cov/C03-verify.md:166-234,325-351,382-385,440-469`; `corpus/knowledge/culture-material/timekeeping-instruments.md:4,7-8`; `reports/round-37/op/O09-routing.md:12,16,32` — README/timekeeping findings and the A02 routing gate.
- `corpus/README.md:1,3,214-215`; `reports/round-37/adj/A01-freeze-adjudication.md:24-35` — current duplicate heading/placeholders and independent freeze read-set adjudication.
- `reports/round-35/adj/audit-assembled.md:192-318`; `SCORECARD.md:608-649` — R35 F1-F13 and CO4/route/allocation deviations left for census reconciliation.
