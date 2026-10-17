# Verification independence and anti-circularity — earned greens, control sensitivity, and re-pin records

- topic: The verification partition's missing discipline for *independence of verification evidence*: who must be independent of whom (failure sources, not job titles), the circularity modes this lane has actually measured — bless-the-tamper re-pins, green-by-construction self-tests, self-captured manifests, subset-only control matchers, unpinned freeze documents, regex false positives, stale pins, mid-review churn — and the minimum record that converts a re-pin from a blessing operation into a verification act. Gap filled: the partition already carries *source*-corroboration independence rules (`citation-format-and-source-registry.md:90,192`), one checkpoint-anchoring rule for the provenance ledger (`provenance-audit-ledger-format.md:151`), and a named-reviewer requirement (`verification-method-overview.md:163`) — but no entry states verifier independence (who must not certify what they authored or re-pinned), catalogs the circularity modes this lane has measured, or defines the record that makes a re-pin admissible; the round-8/9 adversarial receipts each discovered one mode in isolation and none was carried into method.
- sources:
  - KTD-VI-S-0001 — `reports/round-8/depth/findings.md` (R8-D16 adversarial review of `tools/d2-typed-labels.py`): §S2 no frozen manifest exists for the D2 packet (line 34); §S3 post-pin gate repairs invalidate `assemble-d2 --check` and the round-3 replay (line 47); §S11 the harness SCORECARD check is a whole-file regex that already matches a *Planned* row (line 81); §S13 the metadata sweep's +3 frontmatter lines invalidated pinned digests and line locators (line 98). Read at lane revision `e3a1ec9435787328ac9f828f96cb6390e4916b8f`; sha256 `01c27fde75fd65ee32c03d72b01a681d5c6c60b7552d1d50df4affa2f3dcaf5a`.
  - KTD-VI-S-0002 — `reports/round-8/depth/findings-17.md` (R8-D17 blind hand-typing review): the churn record — the reviewed tool changed five times inside one review window, so every verdict carries the revision hash it was measured on (line 156); §F-D17-1 a field the spec requires was absent from the built artifact (line 190). sha256 `8f6eabadf92ca2186e84c478ef0aaa1579d47b06814240c33f0695e90eac10aa`.
  - KTD-VI-S-0003 — `reports/round-9/d3/findings.md` (R9-D09 circularity audit of the D3 acceptance evidence): §S1 the re-pin of `examples/culture-d3/expected.json` is mechanically indistinguishable from a bless-the-tamper operation until it carries a re-verification record, with the minimum record listed at line 47 (line 33); §S2a the guard's self-test builds its frozen fixtures from live bytes, so a green self-test is compatible with a red committed freeze by construction (line 58); §S2b a manifest built from live runs then replayed 5/5 blesses present behavior unless independently corroborated (line 58); §S3 the control matcher accepts supersets — `expected_ids ⊆ actual` ignores extra findings (line 64); §S4 the freeze document excludes itself from its own manifest (line 75). sha256 `27ba8c2f0694ad6c14602d69d8e7c2c52f8ca8c4fca8b4faf4251087644a437c`.
  - KTD-VI-S-0004 — `reports/round-9/d3/findings-10.md` (R9-D10 independent re-derivation): the forcedness check — the declared bases are the only pair yielding each projected name under the declared E1 forms (line 71); §F2's circularity warning — regenerating a manifest from live bytes converts an explained drift into a green line with no evidence (line 159). sha256 `19376989f22d37cfcd4701275515f12f1c62fd820c4368e313ed1d38b06691be`.
  - KTD-VI-S-0005 — lane method cross-references: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4–§6 (digest pins, tamper semantics, class mapping) and §10 (trusted base, false-confidence check); `corpus/knowledge/verification/verification-method-overview.md` §1–§2 (corpus membership is not proof; internal coherence vs reference adequacy); `corpus/knowledge/verification/provenance-audit-ledger-format.md` §8 (append-only; corrections are new entries). These entries supply the freeze mechanics; this entry supplies the independence and anti-circularity rules the mechanics alone do not state.
  - KTD-VI-S-0006 — John C. Knight and Nancy G. Leveson (1986), “An Experimental Evaluation of the Assumption of Independence in Multiversion Programming,” *IEEE Transactions on Software Engineering* SE-12(1): 96–109, [doi:10.1109/TSE.1986.6312924](https://doi.org/10.1109/TSE.1986.6312924); with the authors' reply to criticisms (1990), *ACM SIGSOFT Software Engineering Notes* 15(1): 24–35, [doi:10.1145/382294.382710](https://doi.org/10.1145/382294.382710). Nominally independent implementations failed together far more often than independence assumptions predict; the finding is a classic with a documented methodological debate, so it is cited as a calibration warning, not as a law.
  - KTD-VI-S-0007 — Ken Thompson (1984), “Reflections on Trusting Trust,” *Communications of the ACM* 27(8): 761–763, doi:10.1145/358198.358210. The verifier belongs to the trusted base: a self-pin proves bytes, never the tool that reads them.
  - KTD-VI-S-0008 — Yue Jia and Mark Harman (2011), “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5): 649–678, [doi:10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62). A control's worth is measured by whether planted defects can make it fail — mutation-testing discipline applied here as a design rule for lane controls.
  - KTD-VI-S-0009 — Edsger W. Dijkstra (1972), “The Humble Programmer,” *Communications of the ACM* 15(10): 859–866, doi:10.1145/355604.361591. Testing shows the presence, never the absence, of defects: a green run is bounded evidence, which is why §4 asks *what would make this green red* before it is quoted.
  - KTD-VI-S-0010 — Reproducible Builds project documentation, [reproducible-builds.org/docs/](https://reproducible-builds.org/docs/) (accessed 2026-10-17). Deterministic re-execution is what lets a stranger reproduce a recorded verdict; the lane's independence rule is the human analog of that requirement.
- couples: verification gates and standards — `gate-frozen-run-standard.md`, `verification-method-overview.md`, `provenance-audit-ledger-format.md`, `internal-consistency-audit.md`, `to-verify-triage-protocol.md`; lane tooling — `tools/check-evidence-coupling.py`, `tools/replay-frozen.py`, `tools/check-gate-battery.py`, `tools/gates/expected/`, `tools/gates/frozen/`, `reports/round-8/depth/`, `reports/round-9/d3/`; handoff contract — `../synthesis/worldbible-integration-contract.md` §4/§9 (frozen manifests, pinned versions); siblings — lore-shokunin owns world-bible consistency verification, chousa-shokunin owns general source-research method; this entry is lane-local verification discipline, never a general research standard and never canon.
- follows: `verification-method-overview.md` §1 (internal coherence vs reference adequacy), §6 (fail-closed verdicts: UNKNOWN is not PASS); `gate-frozen-run-standard.md` §6 (tamper semantics: digest check before verdict compare), §10 (digests are integrity, not truth; the verifier is part of the trusted base); `provenance-audit-ledger-format.md` §8 (append-only — a re-pin is a new entry, never a rewrite).
- verified-at: 2026-10-17 — entry authored this round; header fields and all cross-reference targets checked for resolution at revision `e3a1ec9435787328ac9f828f96cb6390e4916b8f`; the four receipt digests recomputed with `sha256sum` at read time (KTD-VI-S-0001..0004); the absence sweep for this entry's gap re-run (`grep -rn -i "separation of duties\|independent verifier\|verifier independence\|different shard" corpus/knowledge/` → 0 hits; `grep -rc -i "circularity" corpus/knowledge/` → 3 hits, all unrelated senses: polysemy-network circularity in `linguistics/semantics-pragmatics.md:46`, Campbell's selection-circularity in `myth-symbol/hero-journey-variants.md:37`, and dated-from-the-same-chronicle circularity in `synthesis/taboo-euphemism-lifecycle.md:155`). The receipt *commands* (gate runs, re-pin demonstrations) were not re-executed by this entry; they are cited by path and digest as the claim permits. Partition state at write close: 15 files (13 pre-round + peer entry `header-conformance-readings.md`, landed 18:31 during this wave + this entry); lane provenance gate re-run over the partition after the write: `files=15 marks=79 mark-lines=78 findings=0 blocked=0`, exit 0; corpus inventory total re-read: `totals.files=181` at write time (README revision 1.2 baseline 179 + the two round-10 verification entries), `totals.files=183` at 21:33:25Z as sibling round-10 entries landed — a header count is always a point-in-time reading and is re-measured before quoting.
- recheck: before each round acceptance that cites a re-pin, a control count, or a "frozen clean" line; whenever `tools/check-evidence-coupling.py`, `tools/replay-frozen.py`, `tools/check-gate-battery.py`, or a frozen manifest changes; whenever a receipt cited above is superseded (corrections are new entries, never rewrites of this one).

## 1. What independence means in this lane, and what it does not

- Independence is a property of **failure sources**, not of job titles. Two shards that read the same entry, the same corpus, and the same receipts with the same tooling are **correlated verifiers** — the second reading adds no independent information (KTD-VI-S-0006: nominally independent implementations failed together far more often than the independence assumption predicts; the effect is a warning calibrated by a documented debate, not a theorem).
- Independence does **not** mean the second party must be a stranger, a different model, or an external auditor. It means the second party's *evidence path* must not reuse the surface whose honesty is in question. Three separations do the work:

| Separation | The two surfaces | Reuse that destroys independence |
|---|---|---|
| **Author ≠ certifier** | the shard that authored or re-pinned an artifact vs the shard that certifies the green | the re-pinning shard also running the acceptance command (KTD-VI-S-0003 §S1: the refresh and the blessing are the same operation) |
| **Evidence ≠ generator** | the committed frozen copy vs the live tree the generator reads | a self-test that rebuilds its fixtures from live bytes, so it is green while the committed freeze is red (KTD-VI-S-0003 §S2a) |
| **Claim ≠ anchor** | the artifact's self-description vs a measurement taken outside it | a freeze document that excludes itself from its own manifest (KTD-VI-S-0003 §S4) |

- This is **lane policy informed by cited method**, not a published verification standard. It applies to lane-local engineering evidence (gates, frozen runs, packet acceptance, round validation). It does not adjudicate real-world historical claims — those pass through `to-verify-triage-protocol.md` and the calibration registry — and it never decides canon.
- Corollary used throughout this entry: *a green is only as strong as the check that could have turned it red.* Before any green line is quoted in a round report or handoff, name the failure it excludes and the command that would have produced that failure (KTD-VI-S-0009).

### 1.1 Adjacent rules that already exist — and the residual this entry fills

Three rules in the partition touch this entry's subject without stating it; none is restated here, each is extended:

| Existing rule (path:line) | What it already says | What it leaves open |
|---|---|---|
| `citation-format-and-source-registry.md:90,192` | several URLs or witnesses copying one account are one evidential lineage, not independent corroboration — "count witnesses, not websites" | applies to *source* corroboration; says nothing about who may certify a lane artifact or when a green is earned |
| `provenance-audit-ledger-format.md:151` (§8 item 10) | persist a closed prefix's digest "against an independently retained anchor; exclude a checkpoint's own bytes from the bytes it describes. A digest printed from a mutable file alone detects no drift" | states the anchoring principle for ledger checkpoints only; the freeze-document/re-pin case (C5) and the control/matcher cases have no equivalent rule |
| `verification-method-overview.md:163` (§10 item 8) | "a prose walkthrough is not an independent reviewer sign-off; name any reviewer and what they actually checked" | requires the reviewer to be named; does not require the reviewer to differ from the author, nor define what record makes a re-pin admissible |

- Residual gap filled here: the **failure-source model** of independence (§1, §3), the **measured circularity catalog** (§2), **control sensitivity and exactness** (§4), and the **re-pin record with dispositions** (§6). Adjacency sweep at authoring time, 2026-10-17 over the then-15-file partition: `grep -rn -i "separation of duties\|independent verifier\|verifier independen\|different shard"` → 0 hits outside this entry.

## 2. Circularity catalog — the modes this lane has measured

Each row is a mode that actually occurred in rounds 8–9; the receipt names the measured instance. The control column is the lane rule this entry adopts.

| # | Mode | Measured instance (receipt) | Control rule |
|---|---|---|---|
| C1 | **Bless-the-tamper re-pin** — refresh a manifest from live bytes and the drift becomes a green with no record | KTD-VI-S-0003 §S1: appending one byte to a component then re-measuring only the digest values into a copy of `expected.json` yields exit 0, `findings: []`; a green frozen run "proves *someone refreshed the manifest after the edit* and nothing about whether the edit was legitimate" | No re-pin without the §6 record. The re-pin is a new ledger entry naming the pre-refresh token, the causing commit, and the verdict-preservation differential |
| C2 | **Green-by-construction self-test** — the check's own fixtures come from the live tree, so a green self-test coexists with a red committed freeze | KTD-VI-S-0003 §S2a: the guard's selftest builds `frozen-good`/`frozen-tampered` from live bytes (`tools/check-evidence-coupling.py:1863-1876`); the auditor ran selftest exit 0 and `--frozen examples/culture-d3/expected.json` exit 2 **at the same time** | A summary may cite only the surface it measured: the frozen leg's evidence is the `--frozen` run, never `selftest_passed` |
| C3 | **Self-captured manifest** — rows built from live runs, then replayed 5/5, bless present behavior | KTD-VI-S-0003 §S2b: the proposed projection manifest pins the current gate revisions; 5/5 alone "blesses present behavior" | A replay result is *reproduction*, not design-cleanliness evidence; carry an independent corroboration (pre-existing README expectations, an old-vs-new differential) into the record |
| C4 | **Subset-only matcher** — expected ⊆ actual, extras ignored, so an over-firing check stays "16/16 green" | KTD-VI-S-0003 §S3: `run_case` (`tools/check-evidence-coupling.py:1687-1706`) checks `missing = want − got`; five controls emit more ids than expected | Matchers are exact or the subset semantics are declared in the record; a control's verdict is the contract's verdict, not a superset of it |
| C5 | **Unpinned freeze document** — the manifest excludes itself, so in-tool checks cannot witness an edit of `expected_exit`/`finding_ids` | KTD-VI-S-0003 §S4 (documented design, residual only) | Anchor the freeze document outside itself: sha256 + git blob in the ledger, and a hash sweep computed without the guard's code |
| C6 | **False-positive matcher** — a whole-file regex matches a *Planned* row and certifies a capability that never ran | KTD-VI-S-0001 §S11: `run-validation.py` searched the whole SCORECARD for `d2[-_ ]typed[-_ ]labels`, which already occurs in the Planned section (`SCORECARD.md:117`) | Anchor capability checks to a specific section/table/anchor, not to a whole-file pattern; a check that can match a plan is not a measurement |
| C7 | **Stale pin after a concurrent edit** — frontmatter sweeps shift lines and digests; pins taken before the sweep no longer resolve | KTD-VI-S-0001 §S13: the metadata sweep inserted three frontmatter lines, shifting line numbers by +3 and changing digests of two pinned synthesis files (pins were correct at HEAD when taken) | Every pinned locator names its revision and digest at read time; re-measure before quoting; a stale pin reads could-not-evaluate, never a silent pass |
| C8 | **Mid-review churn** — the reviewed artifact changes while the review runs, so "the tool is broken/green" depends on when it was read | KTD-VI-S-0002: the tool changed five times inside one review window (`d9e084a8 → … → 623b5b1f`), with intermediate broken states | Verdicts carry the hash they were measured on; re-run on the revision the orchestrator freezes; a verdict without a revision is not reusable |

- Two further surfaces from the same receipts are **not** circular and are recorded here so the catalog is not read as a blanket distrust: (a) a replay tool whose controls prove tampering reads `could_not_evaluate` and whose live path is never opened *is* independent evidence (KTD-VI-S-0003 §S2b); (b) a self-pin whose value is corroborated by an independent hash sweep that used no guard code is externally anchored *at that revision* (KTD-VI-S-0003 §S3 item 7) — the residual C5 hazard returns only after an in-place edit.

## 3. The five questions before any green is quoted

Ask in order; the first "no" blocks the quote, not merely annotates it (fail-closed, `verification-method-overview.md` §6).

1. **Can this check fail?** Name the planted defect that makes it red, and the command that showed it (KTD-VI-S-0008: a control's worth is what it can kill). If nothing can make it red — e.g. the check matches a planned row (C6) or its fixtures are built from live bytes (C2) — it is a probe, not evidence.
2. **What exactly did it measure?** The committed snapshot, not the live tree; the frozen copy, not the path (`gate-frozen-run-standard.md` §3, §6 step 1). State the surface in the same sentence as the green.
3. **Who ran it, and what did they reuse?** Author ≠ certifier; a re-run by the same shard that edited the artifact is a re-execution, not an independent verification (C1).
4. **What is the matcher's semantics?** Exact set, subset, or count-aware; extra findings are either declared accepted or they are failures (C4). A number like "16/16" must say whether it counts cases or findings.
5. **What is the anchor outside the artifact?** Revision + digest at read time (C7), an independent hash sweep where the artifact self-pins (C5), and a corroborating expectation that predates the run (C3).

## 4. Control design rules

- **Sensitivity (disable-witness).** For every control, show that disabling the checker capable of emitting the expected diagnostic makes the diagnostic vanish and the check go green (KTD-VI-S-0003 §3 item 1: 16/16 domain controls lose their expected id under single-function disabling; one control needs all three emitters disabled — redundancy, not vacuity). A control that passes regardless of its checker is vacuous; delete or repair it.
- **Exactness.** Where the contract names a finding-ID set, the matcher compares that set; where it names counts, the matcher compares counts. Supersets are declared in the contract or they are defects (C4).
- **No-op patch detection.** A mutation-based control must verify that its patch actually changed the input (KTD-VI-S-0003 §3 item 1: all 19 patches applied and verified; earlier rounds found a control whose fixture needle was absent — a no-op fixture, KTD-VI-S-0001 §S1/S4 context).
- **Forcedness, not only consistency.** When a derivation is claimed, enumerate the alternatives: KTD-VI-S-0004 §line 71 enumerated all 400 ordered pairs of declared E1 forms and found exactly one pair per projected name — "the declared bases are the *only* pair". A derivation that merely reproduces the committed value is consistent; a derivation whose alternatives all fail is evidence.
- **Honest superset disclosure.** Where a control genuinely emits more ids than the expectation (KTD-VI-S-0003 §S3 table: `D3-REFERENCE` + `D3-BRIDGE` on one control), the fragment records the superset in prose *and* the contract is amended to match, or the control is repaired. Prose-only disclosure is a stopgap, not a disposition.

## 5. Independence checklist — per round and per handoff

Run before a round's acceptance is written, and before a handoff packet carries a "verified" line.

| # | Check | Command or artifact | Fail reading |
|---|---|---|---|
| 1 | Every "frozen clean" line quotes a `--frozen`-class run, not a self-test | the acceptance runner's own measurement block | could-not-evaluate; rewrite the line to name the surface |
| 2 | Every re-pin this round carries the §6 record | the ledger entry for the re-pin | blessing operation — the green does not count |
| 3 | Every control count is exact or the subset semantics is declared | `tools/gates/expected/`, `tools/check-gate-battery.py` output | control-set strength unproven |
| 4 | Every pinned locator/digest was re-measured at read time | `sha256sum` over the cited paths + `git rev-parse HEAD` | stale pin → could-not-evaluate |
| 5 | The certifying shard differs from the authoring/re-pinning shard | round dispatch ledger | re-execution, not verification |
| 6 | Capability rows are anchored to their section, not to a whole-file pattern | the runner's check source | false positive (C6) |
| 7 | Where an artifact self-pins, an outside hash sweep corroborates it | `python3 -c` hashlib sweep (no tool code) | self-pin unanchored (C5) |

## 6. Decision record — the re-pin record and its dispositions

A **re-pin** is any act that changes a committed expected verdict, digest map, or manifest so that a previously red or could-not-evaluate surface reads green: refreshing `expected.json` digests, adopting a new frozen manifest, or updating a pin in a packet. The decision this section records is what makes a re-pin admissible.

**Decision:** a re-pin is admissible only when it carries all six fields below; otherwise the resulting green is classified **blessing**, not verification, and may not be cited as evidence.

| # | Required field | Why it exists (measured) | What fails without it |
|---|---|---|---|
| 1 | Pre-refresh token of the freeze document itself: sha256 + git blob (`git rev-parse HEAD:<path>`) | KTD-VI-S-0003 §S1 records pre-review `74496aa8…` / blob `c420ac4c…` so any later green is provably ordered after the review | A green after an unknown token cannot be ordered against the review that found the drift |
| 2 | Per-key old → new digests **and** the causing commit | KTD-VI-S-0003 §S1: three keys, per-file causing commit `e1694ba` (round-8 admit); KTD-VI-S-0001 §S3 diagnosed the same class for the round-3 replay (`gate_digest_mismatch`) | "Digests updated" without a cause is exactly C1 |
| 3 | Verdict-preservation proof: old vs new gate bytes over the same projection | KTD-VI-S-0003 §S1: byte-identical stdout, exit 1/1 for both gates — the round-8 hardening is behavior-neutral on this artifact | A re-pin can silently hide a verdict change |
| 4 | Byte-level no-change traversal: components match their pins, artifacts hash to their `HEAD` blobs, `--check` exits 0, an isolated regeneration reproduces the bytes | KTD-VI-S-0003 §S1 (four components, `packet.json`/`packet.gates.yml` worktree = `HEAD`); KTD-VI-S-0004 §3 | A re-pin taken over an unexplained live edit (C1 step 2) |
| 5 | `expected_exit` / `finding_ids` kept predeclared and unedited; the freeze diff shown to be exactly the digest lines | KTD-VI-S-0003 §S1 minimum record; KTD-VI-S-0004 §6 (3-line diff technique) | Editing the expectation to match the observation |
| 6 | Stamped revision + date, and the green re-run by a **different** shard than the re-piner | KTD-VI-S-0003 §S1 recommendation; §5 separations table | Re-execution by the interested party (C1) |

- **Disposition table** (same shape as the triage protocol's verdicts):

| Situation | Disposition | Record |
|---|---|---|
| All six fields present; verdicts preserved | **admissible re-pin** | ledger entry, revision-stamped; green may be quoted with the entry linked |
| Fields 1–3 present, 4–6 missing | **conditional** | quote only as "drift explained, green pending record"; the missing fields are the next action |
| Digests refreshed without fields 1–3 | **blessing** | not evidence; the red/could-not-evaluate reading stands until the record exists |
| The drift is a *live* artifact change, not a pin staleness | **wrong target** | revise the artifact or the gate, preserve the failure (`gate-frozen-run-standard.md` §6) — do not re-pin over it |
| The re-pin would change `expected_exit` or `finding_ids` | **not a re-pin** | this is a new claim about the artifact; it goes through design review, not through the pin |

- The C1 demonstration is the calibration case: the auditor reproduced steps 1–3 of the bless operation and then wrote that the re-pin "should instead cite, per entry: the commit, what changed, and why the change is legitimate" (KTD-VI-S-0004 §F2). The record above is that instruction, operationalized.

## 7. Worked pattern — applying this entry to the round-9 D3 case

| Step | Action | Evidence at the time (round 9) | This entry's verdict |
|---|---|---|---|
| 1 | Read the frozen leg honestly | `check-evidence-coupling.py --frozen examples/culture-d3/expected.json` → exit 2, 3 × `D3-SNAPSHOT` (KTD-VI-S-0004 §F2) | correct: red reported, not papered over |
| 2 | Refuse to re-pin from live bytes | the auditors refused and demonstrated why (KTD-VI-S-0003 §S1 step 3) | correct: C1 identified, no blessing issued |
| 3 | Diagnose the drift | three files, one causing commit `e1694ba`, verdict-preservation differential byte-identical (KTD-VI-S-0003 §S1; KTD-VI-S-0004 §3) | fields 2–3 earned |
| 4 | Refresh the pins with a record | LOG.md round-9 entry: "the orchestrator refreshed three expected.json pins — all three drifts are round-8's legitimate committed changes"; the D2-equivalent precedent is `reports/round-8/depth/test-replay.md` §6 | admissible **if** the ledger carries fields 1/5/6 (pre-refresh token, unedited expectation, different-shard re-run); the LOG entry alone does not show fields 1, 5, or 6 |
| 5 | Re-run the green | the round-9 acceptance records the refreshed state | quote only with the §6 ledger entry linked |

- What this pattern does **not** say: that round 9's acceptance was wrong. It says a green that follows a re-pin inherits the record's quality; where the record is thin, the correct disposition is **conditional** (§6 table), which is a documentation task, not a re-run.
- The same pattern applies forward to any round whose acceptance refreshes a pin after a legitimate repair (the round-8 gate repairs are the standing precedent: two gate files and one contract frontmatter file, all committed, all behavior-neutral on the D3 projection).

## 8. Decision record — rules this entry adopts

| ID | Decision | Evidence | Consequence if violated | Recheck trigger |
|---|---|---|---|---|
| **IND-1** | Independence is required at the failure-source level; the authoring/re-pinning shard never certifies its own green | KTD-VI-S-0003 §S1; KTD-VI-S-0006 | green is a re-execution; quote as such or not at all | any round where author and certifier coincide |
| **IND-2** | A re-pin without the §6 record is classified blessing, not verification | KTD-VI-S-0003 §S1; KTD-VI-S-0004 §F2 | the pre-existing red/could-not-evaluate reading stands | every pin refresh |
| **IND-3** | Controls must be able to fail and must match exactly (or declare subset semantics) | KTD-VI-S-0003 §S3, §3 item 1; KTD-VI-S-0001 §S11; KTD-VI-S-0008 | control-set strength unproven; counts may not be quoted as exact | control-set or matcher changes |
| **IND-4** | A green names the surface it measured; no summary substitutes a self-test, a replay, or a probe for a frozen run | KTD-VI-S-0003 §S2a/b; `verification-method-overview.md` §6 | surface substitution — the line is rewritten before use | every acceptance summary |
| **IND-5** | Verdicts and locators name their revision and digest at read time; churn invalidates re-use | KTD-VI-S-0001 §S13; KTD-VI-S-0002 (churn record); KTD-VI-S-0004 §F1 (two artifacts word one rule differently) | stale verdict reused across revisions | any artifact edit after the verdict |
| **IND-6** | Where an artifact self-pins, the anchor lives outside it (independent hash sweep, git blob, ledger row) | KTD-VI-S-0003 §S4, §3 item 7; KTD-VI-S-0007 | in-place edit + refresh undetectable in-tool | any change to a self-pinning tool |

- **Append-only discipline.** This entry never rewrites a filed round receipt. If a later round supersedes a rule here, the correction is a new section or a new entry linked from `recheck` (`provenance-audit-ledger-format.md` §8); the receipts cited above keep their bytes.

## 9. Calibration, limits, and what this entry does not claim

- **Status of the cited findings.** Knight–Leveson is a classic with a documented debate (the authors' 1990 reply; the finding is about correlated failure *probability*, not about all independence claims); it is used here as a calibration warning. Thompson and Reproducible Builds are engineering classics. Jia–Harman and Dijkstra are standard software-testing references. None of them is a linguistic-cultural source, and none is used to support any claim about a real culture.
- **Thin knowledge, stated.** This entry contains no cryptographic expertise beyond the cited standards, no claim that SHA-256 is unbreakable, no general V&V standard, and no claim that its rules match any other lane's practice. It is lane-local engineering method; the fleet standard and `gate-frozen-run-standard.md` win where they speak, and a fleet amendment overrides this entry without negotiation.
- **Measured, not imagined.** Every circularity mode in §2 has a named instance with a path and line; the catalog would be speculation if it did not. Modes not yet measured in this lane (e.g. a shared fixture between two "independent" verifiers) are not listed as findings — the Knight–Leveson warning covers them as a class, and a future round that measures one adds a row.
- **Limits of this entry's own verification.** The receipt commands were not re-executed by the entry author (the claim permits by-path citation); the four receipt digests were recomputed at read time and are listed in `sources`; a later round's drift audit is the natural independent re-run of the receipt *claims*, and any mismatch is a finding against this entry.

## 10. Canon boundary and handoff

- Nothing here decides what is true in any world. Verification independence is lane-local engineering discipline; it never enters the world bible, never marks a design accepted, and never substitutes for lore-shokunin's consistency verification or canon rulings (`PROVINCE.md`; `AGENTS.md`).
- **Handoff use.** When a round report or a handoff packet cites a green produced after a re-pin, attach the §6 record or mark the green **conditional**; when it cites a control count, state exact-or-subset semantics; when it cites a frozen run, name the `--frozen` command and its revision. The receiving shard (lore) needs the surface and the record, not the adjective.
- **Contested scope.** If a sibling lane or the fleet expects a different independence bar (for example, treating a same-model second reader as independent), that is reported to the integrator and never absorbed here — the same stop rule this lane applies to every coupled system.
