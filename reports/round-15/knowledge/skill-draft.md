# R15-D02 — SKILL.md integration draft: claim-uncertainty subsection + error-pattern rows

- worker: DEPTH R15-D02 (round 15, claim D); deliverable: this file only.
- lands: the orchestrator copies BLOCK A (§2) and BLOCK B (§3) into `SKILL.md`.
  Nothing in `SKILL.md` is edited by this worker — same worker-draft /
  orchestrator-lands pattern as R8-D14 (`reports/round-8/depth/skill-table-draft.md:1-6`).
- date: 2026-10-17 lane day; receipts timestamped in UTC (last command
  2026-10-18T00:41:05+0000).
- revision at read time: `git rev-parse HEAD` →
  `c60b17c21a77182a5c1f0251e98b4ea42e563c3e` (baseline `b02cfbc…` per
  `reports/round-15/claims.json:5`). Sibling seats edit this tree
  concurrently; every cited file is sha256-pinned in §6 and every quote was
  re-verified at its cited line by this worker (§5), not inherited from D01.
- relation to siblings: D01 landed the knowledge decision table
  (`reports/round-15/knowledge/uncertainty-table-draft.md`, §3 statuses, §6
  landing block); O-design landed the v2 schema
  (`reports/round-15/handoff/v2-design.md` §2). This draft is the
  **integration text**: SKILL.md-voice subsection and error-pattern rows with
  per-rule citations, vocabulary-matched to both. Where D01's §6 block is a
  compact 3-column table, BLOCK A below is the citation-complete form the
  claim requires ("every rule cited to corpus paths or round-12/15
  artifacts", `reports/round-15/claims.json:21`). The orchestrator lands one;
  if D01's block is preferred, merge its rows with the citations here — the
  two agree on enum, grammar and authority.
- scope: types the uncertainty dimension of handoff claim-ledger rows only.
  Not claim kind, not canon standing (contract §6: lore only), not
  real-language screening or clearance, no new gate. Lane-local policy.

## 1. Landing coordinates (against pinned SKILL.md, §6 digest `52d5f4d1…`)

1. BLOCK A → new `###` subsection inserted immediately after the label-typing
   cautions paragraph (current `SKILL.md:67-73`) and before
   `## Error patterns` (current `SKILL.md:75`). It sits beside the existing
   `### Label typing — translated labels, native forms, borrowed strata`
   (`SKILL.md:31`) as the second typing rule of the packet boundary.
2. BLOCK B → append the rows at the end of the existing `## Error patterns`
   table (after current `SKILL.md:100`, the `naming-collision-gate.md:52`
   row).
3. Optional, non-required: the checklist's handoff item (`SKILL.md:125-127`)
   can gain "with per-claim uncertainty typed (§ Claim uncertainty typing)";
   landing it is the orchestrator's call and is not part of the claim.

## 2. BLOCK A — exact subsection text

````markdown
### Claim uncertainty typing — supported / partial / unresolved

Every handoff claim-ledger row carries `uncertainty: {status: supported|
partial|unresolved, basis}` plus claim-to-record links that resolve: contract
§4 requires per-claim "uncertainty, and relation to other records"
(`corpus/knowledge/synthesis/worldbible-integration-contract.md:63`), and the
round-12 audit rejected the v1 packet because the ledger had neither the
uncertainty dimension nor claim-to-record keys, while D2 coupling was one
aggregate edge (`reports/round-12/adjacency/contract.md:27-28`). Status says
how completely this packet's pinned records and checks ground the claim
**exactly as worded**; claim kind and evidence status stay independent
dimensions, never merged with it (`worldbible-integration-contract.md:92-106`).
Executable authority `tools/harness/packet_uncertainty.py` (`--selftest`);
design authority `reports/round-15/handoff/v2-design.md` §2; knowledge draft
`reports/round-15/knowledge/uncertainty-table-draft.md` §3; vocabulary
`reports/round-15/claims.json:14`. Basis grammar: one `grounding:` witness per
claim (a manifest artifact id, a repo path, or a named validation check);
`restriction:` iff `partial`; `open:` + `owner:` iff `unresolved`
(v2-design §2.2).

| Status | Assign when (necessary condition) | Required basis | Never |
|---|---|---|---|
| `supported` | every element of the claim-as-worded is grounded by a named record in the packet's manifest or a named check with an observed result; nothing open narrows the wording | the resolving `grounding:` witness; residual limits are named even here — scoped-supported is "bounded and revisable, not certainty" (`corpus/knowledge/verification/to-verify-triage-protocol.md:18`) | upgrade a node's support onto its coupling edge (`to-verify-triage-protocol.md:97`); cite a shape-gate pass or digest match as the basis of a semantics claim (`reports/round-12/adjacency/contract.md:9-10,23`) |
| `partial` | the claim holds only under a stated restriction — scope limit, translation/mediation, projection-of-records, caveat-carrying source | `grounding:` + `restriction:` naming the exact bound, as BR05 did: "the Behistun cross-version leg … remain[s] unverified" (`reports/round-11/handoff/packet.md:108`) | widen the evidence instead of narrowing the wording (`to-verify-triage-protocol.md:70,76`); drop the `(to-verify)` from the downgraded remainder (`:182`) |
| `unresolved` | a named open question blocks the claim as worded: unperformed work, an external authority still pending, or contested alternatives that must coexist | `grounding:` + `open:` question + `owner:` lane — "a naked marker without a research question is not a usable queue item" (`to-verify-triage-protocol.md:32`) | let a deadline or failed search force closure (`:80`); present open as a fourth verdict — it is a queue state (`:80,181`); read absence as disproof ("silence is not proof of absence", `worldbible-integration-contract.md:179`) |

Partition crosswalk (`corpus/knowledge/verification/`): triage §1 evidence
states route to statuses — `Located` alone never rises above `partial`
(`to-verify-triage-protocol.md:16`); `Inspected` with unqualified wording
grounds `supported` (`:17`); `Scoped-supported` and `Contested` map to
`partial`, the restriction preserving the disagreement (`:18-19`); `Unknown`
maps to `unresolved`, and unknown is not false (`:21`). The corpus's
framework statuses S/C/H/R/U/V (`source-discipline-calibration.md:67`) stay
framework-level: they calibrate a source or framework, never substitute for a
claim's basis. Provenance-audit wording governs: `supported` does not mean
`improved`, and neither means canon
(`corpus/knowledge/verification/provenance-audit-ledger-format.md:12`).
Legacy `HARD/SOFT/DOCTRINE/DESIGN` labels are advisory and do not map onto
these statuses without lore's explicit mapping
(`worldbible-integration-contract.md:104`; `to-verify-triage-protocol.md:100`).

Cautions that are part of the rule: `supported` is not true and not canon —
evidence strength and fictional truth are orthogonal
(`worldbible-integration-contract.md:102`) and canon standing is lore's alone
(`:100`); `unresolved` is not false; `partial` describes the evidence, not a
demotion of the design. Status never inherits downward: an edge derived from
a `partial` or `unresolved` claim carries at least that status ("A confirmed
node does not upgrade an uncertain relationship",
`to-verify-triage-protocol.md:97`; severity `supported` < `partial` <
`unresolved`, v2-design §2.2). Basis is never boilerplate: unique per claim,
its witness must resolve, and a basis that restates the status word is
rejected (`worldbible-integration-contract.md:183`; v2-design §2.3).
````

## 3. BLOCK B — exact error-pattern rows (append to `## Error patterns`)

````markdown
| A claim's status rides as prose inside `evidence_status` or `kind` | no per-claim uncertainty carrier — the round-12 reject (`reports/round-12/adjacency/contract.md:27`; v1 rows `reports/round-11/handoff/packet.md:82,88,95`); fill the dedicated `uncertainty` field, don't decorate another column |
| The packet passes `16/16 + 20/20` with no uncertainty column anywhere | shape-clean is not uncertainty-populated: the gate has zero uncertainty checks (`grep -ci uncertainty tools/gates/handoff-packet-check.py` → 0, 2026-10-17) and its fixture ledger has five columns, none of them uncertainty (`tools/gates/handoff-packet-check.py:651`) |
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `worldbible-integration-contract.md:183`) |
| A digest match or gate exit 0 offered as a claim's basis | byte identity is not meaning: the audit matched 21/21 digests and still declined the count-semantics claim (`reports/round-12/adjacency/contract.md:11,23`) |
| A claim-to-record link present but not resolving | same defect class as an absent basis (`reports/round-15/claims.json:14`); existence-check every link at freeze and digest-pin the bytes |
| An edge or record inherits its source node's `supported` | nodes do not upgrade arrows: each source→target row is typed with its own status, applicability and justification (`to-verify-triage-protocol.md:97`; `worldbible-integration-contract.md:64`) |
| A date, count, or bound invented to avoid writing `unresolved` | retain uncertain bounds rather than invent precision (`worldbible-integration-contract.md:120`); an unverified conversion stays `(to-verify)` (`to-verify-triage-protocol.md:112`) |
| An open item closed because the round ended | a deadline never forces confirmation; unresolved rows carry owner + reopen condition, not a closure date (`to-verify-triage-protocol.md:80,181`) |
| A landed packet whose uncertainty markers disappeared | a disappearing uncertainty marker is not a verified claim (see *Using the evidence*); recheck every reused reference and unresolved id before each handoff (`to-verify-triage-protocol.md:139`) |
````

## 4. Alignment notes (why the text is safe to land)

- **Vocabulary match with the executable.** The three status tokens, the
  basis prefixes (`grounding:` / `restriction:` / `open:` / `owner:`), the
  severity ordering and the zero-boilerplate rules are quoted from v2-design
  §2.2–2.3 (`reports/round-15/handoff/v2-design.md:108-124,131-138`) — the
  same schema the builder enforces. BLOCK A never introduces a fourth status
  or a looser grammar, so the craft rule and the builder cannot diverge on
  landing day.
- **Vocabulary match with the round declaration.** `{status:
  supported|partial|unresolved, basis}` zero-boilerplate and claim-to-record
  links resolving to real repo records are verbatim requirements of
  `reports/round-15/claims.json:14`.
- **Vocabulary match with D01.** D01's §3 necessary conditions and §6 landing
  block use the same enum and the same authorities; BLOCK A adds the
  per-rule citations and the partition crosswalk the claim's wording
  requires. No contradiction was found between the two drafts.
- **Partition crosswalk verified, not asserted.** Each mapping
  (Located/Inspected/Scoped-supported/Contested/Unknown → status) quotes
  triage §1 at the cited lines; S/C/H/R/U/V, the provenance-audit separation
  and the legacy-label caution are cited at their own lines. The crosswalk is
  a reading aid for reviewers; it does not redefine the triage protocol's
  Confirm/Downgrade/Excise outcomes (`to-verify-triage-protocol.md:69-71`),
  which keep governing reference-claim resolution.
- **Executable authority state.** `tools/harness/packet_uncertainty.py` is an
  in-flight O-impl deliverable (untracked at draft time). Its `--selftest`
  was run by this worker (§5, 19 checks passed, exit 0) and BLOCK A cites it
  with the `--selftest` convention used for every other executable in
  SKILL.md's gates table. If the file moves or lands under a different path,
  the orchestrator updates that one citation at landing; the rule content
  does not depend on the path.

## 5. Receipts (commands run by this worker, all in the lane repo)

- 2026-10-17 (round day), `grep -ci uncertainty tools/gates/handoff-packet-check.py`
  → `0` (exit 1). The shape gate has no uncertainty check; BLOCK B row 2
  rests on this measurement plus the audit's recorded rerun
  (`reports/round-12/adjacency/contract.md:9`).
- 2026-10-17, `sed -n '649,651p' tools/gates/handoff-packet-check.py` → the
  gate fixture's `claim_ledger` template is
  `| record_id | kind | statement | provenance | evidence_status |` (five
  columns, no uncertainty, no link key) — cited as `:651`.
- 2026-10-18T00:41:05+0000,
  `python3 tools/harness/packet_uncertainty.py --selftest` → exit 0,
  `selftest: 19 checks passed (uncertainty rules, boilerplate, oq routing,
  yaml_lines dialect compact+bare)`.
- 2026-10-17/18, quote-at-line verification for every cited locator:
  `grep -n "bibliography is not permission|silence is not proof of
  absence|unknowns are not blank cells|retain uncertain bounds"` on the
  contract → :167, :179, :183, :120; `grep -n "A disappearing uncertainty
  marker"` on SKILL.md → :157. v1 rows re-read directly at
  `reports/round-11/handoff/packet.md:75-108` (status-as-adjective cells
  :82, :88, :90-94, :95; named unverified legs :108). All other cited lines
  were read in full files this round (contract §1-§11, triage protocol
  §1-§12, calibration §1-§7, provenance format, both round-12 adjacency
  files, v2-design §1-§3, claims.json, SKILL.md).
- 2026-10-18T00:41:05+0000, dependency poll: `ls reports/round-15/handoff/`
  → `v2-design.md` only; `reports/round-15/handoff/packet-v2.yml` not yet
  landed. Per §6, packet-v2 alignment is an orchestrator re-check, not an
  assumption of this draft.

## 6. Pinned bytes at read time (sha256sum, 2026-10-18T00:41:05+0000 window)

```
52d5f4d1be6ac97a143323306eafa9c9649484f25de60de8a3ee7630d8c6792c  SKILL.md
5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069  corpus/knowledge/synthesis/worldbible-integration-contract.md
073a348b38c5d8b27cef8f109afed06ff592da00f2eb91252657ab857e32fb13  corpus/knowledge/verification/to-verify-triage-protocol.md
3cbc98b4266aea08d2e8b19513ee369b3f0c6727f16f3c40eafe44796f0e4e93  corpus/knowledge/synthesis/source-discipline-calibration.md
dfa66d2af81b2789ad58b710cc577278f331a6cbda6d6c648d8bbf25613501f4  corpus/knowledge/verification/provenance-audit-ledger-format.md
6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f  reports/round-11/handoff/packet.md
9fb89a062253a9273196ee8b8122f62598d74ce6b32b124034be5029c44ba0a2  reports/round-12/adjacency/contract.md
27b9f958c76da4ad29c4395a237ce158a8d7b86103b7b5fa11d04cc3fe6fea64  reports/round-12/adjacency/A11-A12-handoff.md
a0cf784a8ccc6ccd703aeb5ba876f6607be714d8785addc28d50b04998d59cb5  reports/round-15/claims.json
9a6057315e4a63598ab3c70209a41aa466ebbd42768308b42f40f1328ac00a26  reports/round-15/handoff/v2-design.md
e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575  tools/gates/handoff-packet-check.py
d0c86b6265c1649b88c4a895d11bf88c5f01096009bf6947df320f796dc0174b  tools/harness/packet_uncertainty.py
```

- HEAD at read time: `c60b17c21a77182a5c1f0251e98b4ea42e563c3e`.
- Open dependency (`to-verify`): `reports/round-15/handoff/packet-v2.yml` was
  absent at the last poll. Before landing, the orchestrator re-checks BLOCK
  A's status enum and basis grammar against the landed packet-v2 and the
  frozen builder baseline; any vocabulary drift is `to-verify` against the
  O seats, not silently absorbed here.
- Nothing in rounds 8–14 was read as writable; this worker wrote this file
  only. All content is NON-CANON craft; no real-world rights or canon ruling
  is made or implied.
