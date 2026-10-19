- Seat: Ca03 | executor | claim Ca | date 2026-10-19 | baseline fd55e1f

# Ca03 — calibration receipt draft: the defect-queue v2 refresh

**Status: DRAFT receipt.** This seat landed nothing but this file. The round-40
sibling fragments (K02 queue scout, Ca01 queue-v2 assembly, Ca02/Ca04
verification) do **not** exist at this stamp (`find reports/round-40 -type f` →
only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`), so every
part of the v2 that depends on them is filed under `## Owed`, never assumed. What
this receipt does now, from primary records only: (a) pins the before-state of
queue claim Ca, (b) re-verifies the currentness of each of the r37 queue's 24
rows against the r38/r39 records and the live tree at `fd55e1f`, (c) enumerates
the fold-in inventory the v2 must contain, (d) aligns next-touches with the
remaining loop-1 positions 41-46, and (e) contributes three new findings.

## 1. State pins

| pin | value | source |
|---|---|---|
| HEAD | `fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` | `git rev-parse HEAD`, 2026-10-19 |
| working tree | ` M LOG.md` (parent-owned; line numbers below are against these bytes) + `?? reports/round-40/` | `git status --porcelain` |
| claim under receipt | `reports/round-40/claims.json:18-24` (claim Ca, axis calibration; counting command `python3 reports/round-40/run-validation.py` — **never run by this seat**, shared rule `reports/round-40/targets.json:8`) | read |
| before-object | `reports/round-37/op/defect-queue.json` (schema `kotodama-defect-queue-v1`, 24 rows) | read |
| env | `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` for every command below | set |

## 2. Before-state (measured, not asserted)

The r37 queue carries **24 rows** (`reports/round-37/op/defect-queue.json:11-252`),
in three families:

1. **12 named rows from the r33-36 census** (`:12-131`): F-C13-1, F-C15-1, RC-4,
   R36-D-DECLARATION, R36-D-F6, OI-02, R36-D-RL8, R36-R7-READSET-13,
   R36-ABSOLUTE-ROOT, R36-README-DUPLICATE-HEADING, R36-README-E3-PLACEHOLDERS,
   R36-README-ORDER-CONTIGUITY-REVERIFY.
2. **5 null-id rows, "unclassified at the census cut"** (`:132-181`), each
   `owner: unassigned`, `evidence: null`.
3. **7 findings from r36/r37** (`:182-251`): O10-runner-sha256-null,
   O12-runner-isolation-hazard, basename-couples-policy,
   r37-A01-readset-roster-defect, contract-digest-lore-drift,
   r36-in-tree-runner-incident, readme-prediction-vs-delivery.

Its `census_coverage` (`:6-10`) is **carried, not claimed**: "K02's census was
provisional at its own cut … set-equality is carried, not claimed".

## 3. Row-by-row currentness re-verification (all 24)

Verdicts use the lifecycle vocabulary the r37 queue itself already uses
(`fixed-with-evidence` in its `notes`, `:5`; `carried-with-owner` per row).
Classes are the assembly seat's to finalize; nothing here invents a new scheme.

| # | row | state at `fd55e1f` | verdict for v2 | evidence |
|---|---|---|---|---|
| 1 | F-C13-1 | unchanged; the repeat-prevention note it wants is in force verbatim in this round's own rules (`reports/round-40/targets.json:8`) | carried-with-owner (integrator); next-touch r41+ | queue `:12-21`; targets line |
| 2 | F-C15-1 | unchanged; the r33 provenance record stands (`reports/round-33/calib/open-items-ledger.json`) | carried-with-owner (integrator); next-touch r41+ | queue `:22-31` |
| 3 | RC-4 | unchanged; membership ruling is canon-lane business, external to loop-1 positions | carried-with-owner (integrator/operator); next-touch unchanged | queue `:32-41` |
| 4 | R36-D-DECLARATION | the promised "fields completed at the r38 census cut" **never executed** — no r38 defect-queue census exists in the r38 record (LOG.md:3725-3743 has none; O06-receipt §6 inventories the O block only) | **overdue completion folds into the v2 assembly** (owner Ca01+K02, r40) or re-carry with that owner named | queue `:42-51`; `reports/round-38/op/O06-receipt.md:368-383`; LOG.md:3725-3743 |
| 5 | R36-D-F6 | **fixed-with-evidence at r38**: the counters emit (live: `derived_forms=8 derived_ok=8` on the delivered packet, exit 0, this seat at `fd55e1f`); landed sha `10c88433…` pinned in the r38 receipt | fixed-with-evidence, pointer to r38; row retained, not dropped | queue `:52-61`; `reports/round-38/validation.json:19` (`derived_forms=8 derived_ok=8`), `:17` (sha); live run §6 |
| 6 | OI-02 | same overdue-completion family as row 4 (r37 `:62-71` promised the r38 census cut) | overdue completion → v2 assembly | queue `:62-71` |
| 7 | R36-D-RL8 | **fixed-with-evidence at r38**: the era leg landed at the argot gate as `D4L-ARGOT-ERA` (5 occurrences in the live gate; X01 T1 host decision recorded) | fixed-with-evidence, pointer to r38 | queue `:72-81`; `reports/round-38/validation.json:126`; LOG.md:3732-3735; `grep -c "D4L-ARGOT-ERA" tools/gates/argot-derivation-gate.py` → 5 |
| 8 | R36-R7-READSET-13 | the guard half of this family landed (see row 20); the re-freeze absorption did not | merge into row 20's disposition (same defect, same owner) | queue `:82-91` |
| 9 | R36-ABSOLUTE-ROOT | overdue-completion family (r37 `:92-101`) | overdue completion → v2 assembly | queue `:92-101` |
| 10 | R36-README-DUPLICATE-HEADING | overdue-completion family (`:102-111`); note the duplicate-heading class was also r37's own README repair precedent (LOG.md:3715-3717) | overdue completion → v2 assembly | queue `:102-111`; LOG.md:3715-3717 |
| 11 | R36-README-E3-PLACEHOLDERS | **already fixed at r37 integration** ("the round-35 README apply left two `__E3_PLACEHOLDER__` lines (removed at r37; sweep re-green)") — the r37 queue predates that repair's logging | fixed-with-evidence at r37, pointer LOG.md:3715-3717 | queue `:112-121`; LOG.md:3715-3717 |
| 12 | R36-README-ORDER-CONTIGUITY-REVERIFY | overdue-completion family (`:122-131`) | overdue completion → v2 assembly | queue `:122-131` |
| 13-17 | 5 null-id rows | still id-less and owner-less; the r39 Ca-block dispositioned the *recount-ledger* family (R37-Ca-05..08 → `reproduced-under-protocol`, `reports/round-39/calib/recount-ledger-successor.json:9-46`) but none of these five queue rows | **id + owner assignment is the v2 assembly's first duty** (owner K02 census + Ca01); without it the claim's "every row owner-complete" threshold fails | queue `:132-181`; successor ledger |
| 18 | O10-runner-sha256-null | **still current**: r38 AND r39 receipts both carry `"runner_sha256": null` (`reports/round-38/validation.json:130`; `reports/round-39/validation.json:126`) | carried-with-owner; next-touch: r40's own runner + r41's validation leg | queue `:182-191`; both receipts |
| 19 | O12-runner-isolation-hazard | **addressed-not-fixed**: the isolation-replay protocol governs replays (`reports/round-39/calib/isolation-replay-protocol.md`, landed; Tier A/B/C), but the filed r34/35/36 runners stay absolute-root as filed; the standing successor-runner requirement (protocol §4: "every r38+ runner resolves its root from `__file__`") routes forward | carried-with-owner; next-touch: every r40+ runner generation (verify at r41) | queue `:192-201`; protocol `:1-52` and §4 |
| 20 | r37-A01-readset-roster-defect | **partially fixed at r38**: the manifest-roster guard landed in the renderer (live: 6 `manifest-roster` hits in `tools/exercise-handoff-e2e.py`, sha `e5812751…` matching the LOG-pinned sha), with the recorded limit "naming, not detection"; the fix route (read-set add + successor re-point at the next authorized re-freeze, plus the r34/r35 literal-assertion supersession) is still owed | carried-with-owner (integrator/operator), reason updated to naming-not-detection + owed re-freeze absorption | queue `:212-221`; LOG.md:3736-3738; `reports/round-38/validation.json:38`; live grep §6 |
| 21 | contract-digest-lore-drift | unchanged; contested scope stays routed-not-absorbed | carried-with-owner (lore-shokunin/operator); external next-touch unchanged | queue `:222-231` |
| 22 | r36-in-tree-runner-incident | the repeat-prevention note remains in force in this round's own shared rules | recorded/carried; next-touch: standing | queue `:232-241`; `reports/round-40/targets.json:8` |
| 23 | basename-couples-policy | **documentation leg closed at r39**: the policy landed at the canonical path; but the landed document is **verbatim** — Ca04's D1/D2 one-sentence fixes were **not** applied (grep of the landed file finds no wrapped-field/blocker text), so R01-7's apply-or-queue choice resolves to the **queue branch** | closed-with-pointer (doc leg) + two NEW rows (D1, D2, §4) for the successor instrument | queue `:202-211`; `reports/round-39/calib/basename-couples-policy.md` (landed, no D1/D2 text — grep §6); LOG.md:3755-3759; `reports/round-39/review/R01-review.md:321` |
| 24 | readme-prediction-vs-delivery | unchanged guidance; this round's own C06 receipt draft should honor it (predict by staged-tree sha, cite post-apply sweep) | carried-with-owner; next-touch: r40 integration + future delta audits | queue `:242-251` |

## 4. The r38/r39 fold-in inventory (rows the v2 must contain)

New or updated rows, each with origin and proposed disposition. Minimum eligible
additions: **7** — enough to clear the claim's `row count >= 28` threshold
without padding (24 − 0 dropped + 7 = 31; rows 5/7/11/20/23 stay as
fixed/closed-with-pointer rows, which is how the r37 `notes` treats fixed items).

| # | candidate row | origin | disposition |
|---|---|---|---|
| N1 | Guard row-blindness: the guard names on every filed v3 row (four asymmetric rows, not two), and `--quiet` — the claim's own counting command — prints zero naming hits | r38 O03 G5 + O06-receipt §0/§4.3; LOG.md:3739-3740 "filed to the queue's successor" | NEW row, carried-with-owner; next-touch: next renderer-touching round (r42/r43) or the next re-freeze |
| N2 | O07-scribe.md landed 0 bytes (delivered-empty, counted, recorded) | `reports/round-38/validation.json:124`; LOG.md:3741 | NEW record-only row (no action; the record is the closure) |
| N3 | Argot-gate digest moved at r38 (`b5406bcd…` → `10c88433…`): filed r30 digest rows (`x38-law-gate-*.json`, `rerun.json`) are superseded and must never be rewritten; future register-leg audits cite the new digest with this provenance | `reports/round-38/depth/D07-receipt.md` §5 (last-bullet rule); live sha §6 | NEW carried-with-owner row; next-touch: next register-leg audit |
| N4 | Basename policy D1: single-line couples extractor silently zeroes wrapped fields; live instance `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (0 of 4 tokens captured; 2 phantoms) | `reports/round-39/calib/Ca04-verify.md` D1 | NEW row; owner: successor couples instrument (draft at r42/r43) |
| N5 | Basename policy D2: no `unresolved` disposition leg vs the C12 row-2 blocker rule (`reports/round-35/cov/C12-audit-runbook.md:37`) | `reports/round-39/calib/Ca04-verify.md` D2 | NEW row; same owner as N4 |
| N6 | Corpus couples phantoms (repair dispositions owed): X26-1 `../linguistics/phonology-sanity.md` x2 (`corpus/knowledge/verification/label-channel-routing-verification.md:14`); 3 never-written seeds (`corpus/knowledge/linguistics/language-contact.md:7`); the 2 D1 phantoms | `reports/round-39/calib/Ca03-basename-policy.md` Part 2 (scan findings, "to-verify whether … get repair dispositions"); Ca04 D1 | NEW row (one rollup or three, assembly's choice); owner: integrator via a drafted corpus leg (seats never stage corpus bytes) |
| N7 | Receipt-fidelity defect: `reports/round-39/validation.json:118-123` `named_findings` and its `limits` duplicate r38's **verbatim** (strings at `reports/round-38/validation.json:112-127`), including the grok-403 route deviation — inapplicable to r39's zai 16/16 dispatch (LOG.md:3747-3749) — and O07's 0-byte fragment, an r38 event | this seat's diff (§6) | NEW row, same runner-generation family as O10; owner: r40+ runner work — the r40 runner must emit round-specific named findings and a non-null `runner_sha256` |

Excluded from the queue, per the r37 queue's own precedent ("the r36
D-rejection is a round record, not a defect (excluded)", `defect-queue.json:5`):
the r38 route deviation grok-403→devin (attempt-1) — a telemetry fact, recorded
at `reports/round-38/validation.json:54-58` and LOG.md:3728-3731, owner
orchestrator; not a defect row.

## 5. census_coverage and the claim's second threshold

- **Completion route:** K02-r40's mission ("the r37 queue's 24 rows + every
  finding added in r38/r38-wave/r39 records; each with origin and current
  owner-state", `reports/round-40/targets.json:20-24`) **is** the census
  completion; Ca01 assembles the v2 from it. If either is absent at
  integration, the completion is **carried with an owner** (Ca01+K02), never
  silently — exactly the option claim Ca's `after_required` names
  (`reports/round-40/claims.json:21`).
- **Owner-completeness:** rows 13-17 (null ids, `owner: unassigned`) are the
  direct threat to "every row owner-complete". Assembly must assign each an id
  (canonical id + alias where it merges, per the queue's own row-14 note) and an
  owner, or the threshold honestly fails and the round reports it.
- **Row count:** §4's N1-N7 alone give 31 ≥ 28. A higher count is acceptable
  only with per-row origin citations — no padding.

## 6. Next-touch alignment with loop-1 positions 41-46

Schedule per `REGIMEN.md:9-23`. Alignment is by *capability of the position*,
not convenience:

| position | lane | takes next-touch of |
|---|---|---|
| 41 | codex gpt-6-luna-max, mid-loop verify | O10 (runner emits `runner_sha256`), O12 standing (relative-root runner check), N7 (round-specific named findings), v2 currentness spot-check |
| 42 | devin build | N4+N5 (successor couples instrument draft), N1 candidate (renderer touch) |
| 43 | zai build | N6 (corpus-repair drafts, integrator-applied), N4/N5/N1 overflow |
| 44 | antigravity build | overflow from 42/43; no dedicated calibration claim expected |
| 45 | antigravity deep build (8 seats) | deep items only; re-freeze cascade stays operator-gated here too |
| 46 | devin swe-2 audit | audit the v2's lifecycle bookkeeping (fixed rows cited; zero filed byte edits) |
| external | — | RC-4, contract-digest-lore-drift (lore-shokunin/operator; not loop-1-bound) |

The row-20 re-freeze absorption and N1's renderer half are **operator-gated**
(non_goals: "no re-freeze of declared-in-r7", `reports/round-40/claims.json:32-33`);
their next-touch names the *condition*, not a position.

## 7. Commands run by this seat (all read-only; 2026-10-19, lane root, `fd55e1f`)

```
git rev-parse HEAD                              # fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106
git status --porcelain                          # " M LOG.md" + "?? reports/round-40/"
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
  # coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8
  #           borrow_pairs=6 violations=0 rule_holds=0 derived_forms=8 derived_ok=8  exit=0
sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py \
          tools/exercise-handoff-e2e.py
  # 10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75  (argot; == r38 pinned landed sha)
  # 15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  (law gate; unchanged)
  # e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553  (renderer; == LOG r38 sha)
grep -c "D4L-ARGOT-ERA" tools/gates/argot-derivation-gate.py     # 5
grep -c "manifest-roster" tools/exercise-handoff-e2e.py          # 6
grep -n "wrapped\|blocker\|phonetics-phonology" reports/round-39/calib/basename-couples-policy.md
  # no matches → Ca04's D1/D2 one-liners are NOT in the landed policy
diff <(sed -n '116,121p' reports/round-38/validation.json) \
     <(sed -n '112,117p' reports/round-39/validation.json)
  # only delta: measured_at_utc (clock); the two limits strings: identical
diff <(sed -n '122,127p' reports/round-38/validation.json) \
     <(sed -n '118,123p' reports/round-39/validation.json)      # named_findings: identical (exit 0)
find reports/round-40 -type f                                    # claims/targets/telemetry only (pre-write)
```

No `reports/round-*/run-validation.py` was executed anywhere (absolute rule,
`reports/round-40/targets.json:8`). Claim Ca's declared counting command
(`python3 reports/round-40/run-validation.py`) is therefore **to-verify** at
validation, per the r37/r38 precedent for not-yet-landed runners.

## 8. Dependencies at this stamp

K02 (`scout/K02-queue-scout.md`), Ca01 (`calib/Ca01-queue-v2.md`), Ca02
(`calib/Ca02-verify.md`), Ca04 (`calib/Ca04-consistency.md`): **absent**. §3/§4
stand on primary records (r37 queue, r38/r39 receipts + fragments, live tree),
not on those seats; the v2 JSON itself is their product.

## Owed

- **`reports/round-40/op/defect-queue-v2.json`** — the v2 itself; owner: the
  integrating parent, assembled from Ca01's draft. Landing path by analogy with
  the r37 queue's `op/` home; S01's validation-leg spec is the authority.
- **Id + owner assignment for queue rows 13-17** — owner: K02 census + Ca01
  assembly (r40). Without it the owner-completeness threshold fails honestly.
- **Fold-in confirmation** — Ca02 (sampling ≥30% of v2 rows against origins)
  and Ca04 (strict JSON, row count, class vocabulary, no duplicate ids) confirm
  §4's dispositions; a disagreement with any §4 row is filed, not silent.
- **r40 runner obligations** (closes O10 + N7 at the next generation): emit a
  non-null `runner_sha256` and round-specific `named_findings`/`limits`. Owner:
  the integrating parent / S01 spec.
- **to-verify:** whether the v2 keeps schema `kotodama-defect-queue-v1` with the
  lifecycle vocabulary observed above (`carried-with-owner` /
  `fixed-with-evidence` / `closed-with-pointer` / record-only) or bumps the
  schema string — assembly's decision; Ca04's consistency check names "class
  vocabulary" as a checked field (`reports/round-40/targets.json:126-130`).
- **to-verify:** the N7 line spans (`:112-117` / `:118-123` of r39's receipt)
  were verified at this stamp but sit in filed bytes; re-run the §7 diff at
  integration if any runner rewrite is suspected.

## Citations

- Claim + rules: `reports/round-40/claims.json:18-24` (Ca), `:32-33` (non_goals);
  `reports/round-40/targets.json:3-9` (shared_rules), `:111-116` (Ca03 row).
- Before-object: `reports/round-37/op/defect-queue.json:5-10` (notes +
  census_coverage), `:11-252` (24 rows; family boundaries in §2).
- r38 landing evidence: `reports/round-38/validation.json:19` (live counters),
  `:17` (argot sha), `:38` (naming-not-detection), `:54-58` (route deviation),
  `:112-127` (limits + named_findings), `:130` (`runner_sha256: null`);
  `reports/round-38/depth/D07-receipt.md` §5 (r30 digest-supersession rule);
  `reports/round-38/op/O06-receipt.md:368-383` (O-block seat inventory), §0/§4.3
  (guard channel + row-blindness); LOG.md:3725-3743 (r38 entry).
- r39 landing evidence: `reports/round-39/validation.json:108-123` (duplicated
  limits + named_findings), `:126` (`runner_sha256: null`);
  `reports/round-39/calib/isolation-replay-protocol.md:1-52` + §4 (protocol;
  standing successor-runner requirement);
  `reports/round-39/calib/recount-ledger-successor.json:9-46` (R37-Ca-05..08
  reproduced-under-protocol);
  `reports/round-39/calib/basename-couples-policy.md` (landed verbatim; grep in
  §7 shows no D1/D2 text);
  `reports/round-39/calib/Ca04-verify.md` (D1/D2 + Owed apply-or-queue);
  `reports/round-39/calib/Ca03-basename-policy.md` (Part 2 scan findings);
  `reports/round-39/review/R01-review.md:262-265,315-333` (R01-7);
  LOG.md:3745-3761 (r39 entry).
- Corpus instances cited: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`;
  `corpus/knowledge/verification/label-channel-routing-verification.md:14`;
  `corpus/knowledge/linguistics/language-contact.md:7`.
- Live-tree commands and outputs: §7 (this seat, 2026-10-19, baseline `fd55e1f`).
