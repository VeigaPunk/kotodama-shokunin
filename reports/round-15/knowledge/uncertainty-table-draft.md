# R15-D01 — claim uncertainty-typing decision table (draft for SKILL.md)

- worker: DEPTH R15-D01 (round 15, claim D); deliverable: this file only.
- lands: orchestrator copies the LANDING-READY block (§6) into `SKILL.md`
  (suggested: a `### Claim uncertainty typing` subsection directly after the
  existing "Label typing" table, plus the two extra rows into the existing
  "Error patterns" table). Nothing in `SKILL.md` is edited by this worker —
  same worker-draft / orchestrator-lands pattern as R8-D14
  (`reports/round-8/depth/skill-table-draft.md:1-6`).
- date: 2026-10-17 lane day; receipts timestamped in UTC below (last command
  2026-10-18T00:28:48+00:00).
- revision at read time: `git rev-parse HEAD` →
  `c60b17c21a77182a5c1f0251e98b4ea42e563c3e` (round-15 claims baseline
  `b02cfbc…`); sibling workers edit this tree concurrently, so every cited
  file is pinned by sha256 in §8 and every quote names its file and line.
  Draft rev 2 (2026-10-18T00:40Z window): re-keyed citations to the round's
  own counting command after reading its depth check — every decision-table
  row now carries a resolvable `corpus/` or `reports/round-12|15/` citation,
  and the draft contains no pointer to bytes that do not yet exist.
- dependency state: the O worker's schema design landed mid-draft —
  `reports/round-15/handoff/v2-design.md` (R15-O01, sha256 `9a605731…`, §8)
  pins exactly the vocabulary used here:
  "`uncertainty: {status: <supported|partial|unresolved>, basis: …}`" beside
  `claim_kind`, `evidence_status`, `statement`, `links`
  (`v2-design.md:85-100`, read 2026-10-18T00:40:13+00:00). The final
  `packet-v2.yml` bytes were still absent — `ls reports/round-15/handoff/`
  → `v2-design.md` only at 00:40:13+00:00 — so the earlier polls
  (`ls reports/round-15/handoff/ | wc -l` → `0` at 00:28:48 and 00:32:13
  +00:00) remain part of this record. The round declaration's acceptance
  wording ("zero boilerplate", "claim-to-record links resolving to real repo
  records", `reports/round-15/claims.json:14`) is quoted unchanged. Before
  landing this table against the finished packet, re-check §3–§4 and re-pin
  the packet digest; any drift is `to-verify` against the O worker, not
  silently absorbed here.
- scope: this table types the **uncertainty dimension of one handoff
  claim-ledger row** — when a claim is `supported` vs `partial` vs
  `unresolved`, and what basis form each status requires. It does not type
  claim kind (contract §6 does that), does not decide canon standing (§6:
  lore only), does not perform or clear real-language screening, and adds no
  new gate. This is lane-local policy: the corpus vocabulary it cites is
  binding as *this lane's* craft, not as an external standard.

## 1. What this table decides

Round 12 rejected the handoff packet on semantics, not shape: "the claim
ledger has no explicit per-claim `uncertainty` dimension, and no
claim-to-record/edge relation key" and D2 coupling was "one aggregate
dependency edge" (`reports/round-12/adjacency/A11-A12-handoff.md:14,41`;
`reports/round-12/adjacency/contract.md:27-28`). The same audit showed why
nobody caught it earlier: the shape gate passed 16/16 fields and 20/20
glossary entries, and "this is a shape/gate result, not proof of semantic
completeness" (`contract.md:9-10`). The fix recipe — per-claim uncertainty
status + basis, and claim-to-record links that resolve — exists only in the
round declaration and the audit prose
(`reports/round-15/claims.json:14,21`; `contract.md:27-28`). This table turns
that recipe into decision-table craft so the next packet author does not have
to re-derive it from a reject.

The normative hook is contract §4: a `claim_ledger` row must carry
"Statement, claim kind, source/invention provenance, evidence status,
**uncertainty**, and relation to other records"
(`corpus/knowledge/synthesis/worldbible-integration-contract.md:63`), and
§6 already separates claim kind from evidence status from canon standing so
that uncertainty has somewhere honest to live
(`worldbible-integration-contract.md:92-107`).

## 2. Receipts (commands, outputs, date)

All commands run in `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

- **2026-10-18T00:28:48+00:00** — `grep -ci uncertainty tools/gates/handoff-packet-check.py`
  → `0` (exit 1, zero hits). The shape gate contains no uncertainty check of
  any kind; its only claim-ledger findings are section-presence
  (`HO-MISSING`/`HO-EMPTY`, `tools/gates/handoff-packet-check.py:478-500`)
  plus canon-wording guards (`HO-CANON-MARKER`/`HO-CANON-CLAIM`, `:63,65`).
- **2026-10-18T00:28:48+00:00** — `sed -n '649,651p' tools/gates/handoff-packet-check.py`
  → the gate's own fixture `claim_ledger` template is
  `| record_id | kind | statement | provenance | evidence_status |` — five
  columns, **no uncertainty column, no record-link key**. An envelope copied
  from the lane's own fixture shape passes the gate and still fails contract
  §4. Fixture evidence beats argument here: the v1 packet did exactly this
  and read `fields=16/16 glossary-entries=20 findings=0`
  (`contract.md:9`).
- **2026-10-17T22:37:57Z** (as recorded, not re-run) — the audit's gate rerun
  `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet.md`
  → exit 0, `fields=16/16 glossary-entries=20 findings=0`, immediately
  followed by the two semantic findings (`contract.md:9-10,27-28`). Shape
  16/16 and semantic REJECT coexist in one artifact.
- **v1 uncertainty scatter** (read from the filed packet, sha256-pinned §8):
  `reports/round-11/handoff/packet.md:82` D2-CL02 carries status as an
  evidence_status adjective — "`derived projection (author-side), holds
  open`"; `:88` CL06 — "`invented; truth status 'unresolved'`"; `:90-94`
  CL08–CL12 — "`secondary-scholarly; support partial-support; audit R6-05-A`"
  (status welded into the evidence_status cell); `:95` CL13 — kind
  "`screening statement`", evidence_status "`unresolved`". Three different
  columns carry what §4 wants in one consistent per-claim carrier.
- **v1 basis strengths worth keeping**: CL08–CL12 each name a parent
  reconciliation tuple + spotcheck (`R6-05-A` + `P04`, `packet.md:90`; and
  `packet.md:91-94`), and BR05's limits cell names its unverified legs —
  "`S05 is partial-support: the Behistun cross-version leg and all-subject
  speech claims remain unverified`" (`packet.md:108`). The *form* is right;
  the carrier and per-edge typing were the defect
  (`contract.md:27-28`).
- **2026-10-18T00:28:48+00:00** — `ls reports/round-15/handoff/ | wc -l` →
  `0` (v2 packet pending; poll, do not assume).
- **2026-10-18T00:40:13+00:00** — `sha256sum reports/round-15/handoff/v2-design.md`
  → `9a6057315e4a63598ab3c70209a41aa466ebbd42768308b42f40f1328ac00a26`; the
  O worker's landed schema design states the same carrier this table types:
  "`uncertainty: {status: <supported|partial|unresolved>, basis: "<text>">}`"
  beside `claim_kind`/`evidence_status`/`statement`/`links`
  (`v2-design.md:87-100`). Vocabulary drift check against §3: **match**.
- **2026-10-18T00:39Z window** — conformance self-check against this round's
  own counting command, executed read-only (module import; its `main()` was
  **not** invoked — invoking it would write the round's `validation.json`
  receipt, outside this worker's assignment):
  `python3 -c` (importlib load of `reports/round-15/run-validation.py`;
  `measure_d(m.Evidence(), m.round15_files())`) → `passed: true`,
  `failures: []`, draft = this file, 5 tables, **17 rule rows, 17 cited
  rows**, statuses covered `partial`/`supported`/`unresolved`,
  `partition_crossref: true`, zero unresolvable citations. The check ran at
  TMPDIR on the lane's `.scratch`. (Re-check after the last receipts were
  added below flagged one self-inflicted pointer: naming the runner's future
  receipt file by full path reads as an unresolvable citation until the
  runner itself lands it — refer to it by bare name, `validation.json`, and
  let the round's own receipt create the path.)

## 3. The three statuses

Vocabulary from the round declaration (`reports/round-15/claims.json:14`:
"`{status: …, basis}` populated for every claim (zero boilerplate)"),
necessary conditions aligned to the lane's verification partition —
`corpus/knowledge/verification/to-verify-triage-protocol.md` — and to the
contract. Status attaches to **the claim as worded, at its stated scope**:
the same subject matter can correctly carry different statuses in different
rows if the wordings differ (triage §4: "If repairing the wording would
answer a different question, create a linked child claim rather than
pretending the original was confirmed", `to-verify-triage-protocol.md:76`).

| Status | Assign when (necessary condition) | Required basis form | Forbidden move | Authority |
|---|---|---|---|---|
| `supported` | The exact proposition, at the scope stated, is carried by a basis this lane can produce on demand: an in-repo record locator **plus** the dated check event that read it (command + output, assembler `--check`, coupling guard, or measured digest match). | (a) `path` + record id that resolves in-repo; (b) the inspection event (dated command, exit/output, or digest comparison); (c) residual limits named even when supported — scoped-supported is "bounded and revisable, not certainty". | Never upgrade by aggregation: a supported node does not make its edge supported. Never cite a shape-gate pass or a digest match as support for a semantics claim. | Confirm condition and scoped-supported vocabulary, `corpus/knowledge/verification/to-verify-triage-protocol.md:18,69`; the audit's split verdict is the worked example — digests 21/21 matched (`contract.md:11`) while "this verifies the manifest digests, not every stated record-count interpretation" (`contract.md:23`): two claims, two statuses, one packet. |
| `partial` | A stated scope restriction survives inspection but the row's wording exceeds it: some narrower claim is supported and some named part is not. | (a) the supported remainder, narrowed to exact scope, with its own locator; (b) the unsupported legs **named**, not implied ("the Behistun cross-version leg … remain[s] unverified", `packet.md:108`); (c) the parent reconciliation tuple or effective-row id where one exists (`R6-05-A` + `P04`, `packet.md:90`). | Never state partial as supported "for brevity"; never repair by widening the evidence instead of narrowing the wording; a downgraded factual remainder keeps its `(to-verify)` and stays open. | Downgrade row and §7 wording rule ("'not established by the evidence inspected,' naming the inspected corpus"), `corpus/knowledge/verification/to-verify-triage-protocol.md:70,124`; v1 CL08–CL12 are the basis-form model, carried in the wrong column (`contract.md:27`). |
| `unresolved` | The question is open for a named reason with a named owner: work not yet performed, an authority external to this lane still pending, or contested alternatives that must coexist. | (a) `(to-verify)` attached to **the smallest uncertain proposition**, never the whole claim or bibliography (`to-verify-triage-protocol.md:15`); (b) the flag reason — why unresolved (`:30`); (c) owner / responsible lane and blocking status (`worldbible-integration-contract.md:66`; triage `:32` "a naked marker without a research question is not a usable queue item"). | Never let a deadline, failed search, or time budget force closure ("A deadline, failed search, or exhausted time budget never forces confirmation", `:80`); never present open as a fourth *verdict* — it is a queue state (`:80,181`). | `corpus/knowledge/verification/to-verify-triage-protocol.md:15,30,32`; v1 CL13 is the model: unresolved screening stated via the machine-readable flag "`real_language_sweep_performed: false`" with the inference ban spelled out (`packet.md:95`); pending bilateral acknowledgment and lore-owned canon standing are structural unresolveds (`worldbible-integration-contract.md:15,100`; `contract.md:42`). |

**Claim-to-record link rule** (the reject's second finding,
`A11-A12-handoff.md:14`; `claims.json:14` "claim-to-record links resolving to
real repo records"): every row also carries `path` + record id, and the link
must *resolve* — verified by an existence/read check, digest-pinned when the
bytes matter. A dead pointer is a defect of the same class as an absent
basis: the audit had to re-measure digests itself because manifest presence
did not demonstrate resolution (`contract.md:11`). Preferred pattern: the
read-only digest check shape already used by the audit (`contract.md:11`),
extended to assert each linked record id occurs in the linked file.

## 4. Required basis form by claim kind

Cross-reference to contract §6's claim kinds
(`corpus/knowledge/synthesis/worldbible-integration-contract.md:92-107`) and
into the lane's verification partition (`corpus/knowledge/verification/` —
triage protocol, gate specifications, provenance formats). Kind and
uncertainty are independent dimensions: a `generative rule` can be
`supported` as a constructed fact, and a real-world reference can be
`partial` while its cited work is famous. Status never changes the kind, and
kind never launders status.

| Claim kind (contract §6) | Statuses reachable in this lane | Required basis form | Never sufficient as basis | Authority |
|---|---|---|---|---|
| generative rule | `supported` (as constructed fact) | rule id + packet record locator + a reproduction check that read it (`--check` assembler, coupling guard, frozen `expected.json` replay) | plausibility; "the gate passed" without naming which check read the rule | Reproduction/coupling-check column for system specs — show valid and invalid derivations, `corpus/knowledge/synthesis/worldbible-integration-contract.md:76` |
| real-world reference | `supported` / `partial` per scope | effective parent-reconciliation row id + spotcheck id + pinned locator (edition, capture digest, page) + consulted-intermediary statement | a located-but-uninspected URL — "**Located**: … this is not evidence that its text supports the claim"; the raw worker label over the effective tuple (SKILL.md D3 table: "Use the committed parent reconciliation tuple, not the raw worker label") | `corpus/knowledge/verification/to-verify-triage-protocol.md:59` (read the original vs an edition/translation), `:16` (Located) |
| attributed in-world belief | `supported` as attributed account; the world-fact question stays `unresolved` | named in-world speaker + belief record locator + explicit truth-status `unresolved`; "A supported statement that 'author A reports X' confirms the report, not X's truth" | narrator endorsement; counting two opposing accounts as one settled reading — preserve the disagreement | `corpus/knowledge/verification/to-verify-triage-protocol.md:77,19` |
| designer interpretation | `supported` (as author-side) | the author-side projection declaration + the source record the projection reads (e.g. typed-label channel coverage, `packet.md:81-82`) | reading it as the culture's emic self-description — "An etic generator/framework remains designer metadata" | `corpus/knowledge/synthesis/worldbible-integration-contract.md:105` |
| candidate world-fact | `unresolved` in this lane, by construction | namespaced candidate id, explicitly unresolved, never a guessed lore id | any canon assignment — canon standing is lore-only; the gate's canon-wording guards (`HO-CANON-MARKER`, `HO-CANON-CLAIM`) are wording checks, not dispositions | `corpus/knowledge/synthesis/worldbible-integration-contract.md:60,100` |
| screening / clearance statement | `unresolved` unless the work actually happened | the machine-readable flag itself (`real_language_sweep_performed: false`, `packet.md:95`) or the dated sweep record | silence; the absence of a sweep record; "no complaints received" | The audit credits exactly this honesty — "does not claim real-language screening, consultation, permission or legal clearance", `reports/round-12/adjacency/contract.md:36` |

## 5. Anti-patterns (each with its control)

| Observation | Reading | Authority / control |
|---|---|---|
| Packet passes `16/16 + 20/20` and no uncertainty column exists anywhere | Shape-clean is not uncertainty-populated: the gate has zero uncertainty checks (`grep -ci uncertainty tools/gates/handoff-packet-check.py` → `0`, 2026-10-18T00:28:48+00:00) and its fixture ledger has five columns, none of them uncertainty (`handoff-packet-check.py:651`) | `contract.md:9-10` — "a shape/gate result, not proof of semantic completeness"; control: a semantic re-audit over the packet, not just the gate rerun |
| Boilerplate basis — rows share a content-free basis ("checked", "see packet") or one string duplicated across claims | Zero-boilerplate is the v2 acceptance condition (`claims.json:14`); "unknowns are not blank cells" applies to bases too (`worldbible-integration-contract.md:183`) | Control: each basis names a per-claim locator, or a shared measured event plus what that event establishes *for this row* |
| Status lives in the wrong column — `holds open` inside evidence_status (`packet.md:82`), `unresolved` inside kind (`:95`) | No consistent per-claim carrier; downstream tooling and reviewers cannot key on it — this is the exact round-12 finding (`contract.md:27`) | Control: one dedicated uncertainty field per row, values from the fixed three-status set (`claims.json:14`) |
| Supported node cited as support for an edge; D2 carried as one aggregate edge | "A confirmed node does not upgrade an uncertain relationship" (`to-verify-triage-protocol.md:97`); §4 requires typed edges "with applicability and justification" (`worldbible-integration-contract.md:64`) — the section heading itself: "Coupling audit: evidence for nodes is not evidence for arrows" (`:83`) | `contract.md:28` is the named defect; control: every source→target row typed, its own status + basis |
| Precision invented to avoid writing `unresolved` (bounds, dates, counts) | "retain uncertain bounds rather than invent precision" (`worldbible-integration-contract.md:120`); "An unverified conversion stays `(to-verify)` rather than receiving false precision" (`to-verify-triage-protocol.md:112`) | Control: every quantitative assertion carries its measured source or reads `unresolved` |
| Absence of evidence written as evidence of absence | "silence is not proof of absence" (`worldbible-integration-contract.md:179`); the "no surviving source" case downgrades to the inspected corpus (`to-verify-triage-protocol.md:194`) | Control: negative claims name the inspected corpus and the search route |
| Deadline or round end used to close an open item | "A deadline, failed search, or exhausted time budget never forces confirmation" (`to-verify-triage-protocol.md:80`); "`unresolved` is no resolution outcome: it prevents an open investigation from masquerading as a closed verdict" (`:181`) | Control: unresolved rows carry owner + reopen condition, not a closure date |
| Digest match or gate exit 0 cited as the basis for a semantic claim | The audit matched 21/21 digests and still declined count-semantics (`contract.md:11,23`); REJECT coexisted with 16/16 (`contract.md:9` vs `A11-A12-handoff.md:14`) | Control: separate rows for the byte-identity claim and the semantics claim, each with its own status |
| Claim-to-record link present but not resolving (renamed/moved/deleted record) | v2 requires links "resolving to real repo records" (`claims.json:14`); a dead link fails the same §4 clause as no link | Control: existence/read check over every link at freeze time; digest-pin bytes that matter |
| Uncertainty marker dropped because the packet "needs to look finished" | "A disappearing uncertainty marker is not a verified claim" (SKILL.md:157); "Uncertainty survives that chain … never disappear merely because a world bible needs an answer" (`to-verify-triage-protocol.md:218`) | Control: handoff recheck enumerates unresolved rows before submission (triage §8 "Before each lore handoff", `:139`) |

## 6. LANDING-READY block for SKILL.md

### Claim uncertainty typing — supported / partial / unresolved

Every handoff claim-ledger row carries `uncertainty: {status, basis}` and a
claim-to-record link that resolves. Status attaches to the claim **as
worded**, at its stated scope; kind never changes status and status never
changes kind (contract §6).

| Status | Assign when | Required basis | Never | Authority |
|---|---|---|---|---|
| `supported` | exact proposition at stated scope, carried by a locator + a dated check event (command/output, `--check`, frozen replay, digest match) | record locator + inspection event + residual limits | upgrade a node's support onto its edge; cite gate/shape/digest as a semantics basis | `corpus/knowledge/verification/to-verify-triage-protocol.md:18,69` |
| `partial` | a scope restriction survives; part holds, part does not | supported remainder with locator + **named** unsupported legs + effective reconciliation tuple | widen the evidence instead of narrowing the wording; drop the open `(to-verify)` on the remainder | `corpus/knowledge/verification/to-verify-triage-protocol.md:70,124` |
| `unresolved` | work unperformed, external authority pending, or contested alternatives retained | `(to-verify)` on the smallest proposition + why + owner and blocking status | let a deadline close it; present open as a verdict; read absence as disproof | `corpus/knowledge/verification/to-verify-triage-protocol.md:15,80,181` |

Extra error-pattern rows for the existing table:

| Observation | Reading |
|---|---|
| A claim row's status appears as an adjective inside evidence_status or kind | no per-claim uncertainty carrier — the round-12 reject (`reports/round-12/adjacency/contract.md:27`); type the field, don't decorate another |
| A claim-to-record link that does not resolve | same defect class as an absent basis (`reports/round-15/claims.json:14`); verify links at freeze, digest-pin the bytes |

Cautions that are part of the rule: `supported` is not true and not canon —
evidence strength and fictional truth are orthogonal
(`worldbible-integration-contract.md:102`), and canon standing is lore's
(`:100`); `unresolved` is not false ("unknown does not mean false",
`to-verify-triage-protocol.md:21`); `partial` describes the evidence, not a
demotion of the design — but every coupling edge still carries its own
status, because "evidence for nodes is not evidence for arrows" (`:83,97`).

## 7. Boundaries

- This table is lane-local policy for handoff claims. It is not a lore
  disposition, not an evidence-certification standard beyond this lane's own
  records, and not a real-world rights/permission instrument (contract §10
  routes rights questions out; "a bibliography is not permission",
  `worldbible-integration-contract.md:167`).
- Legacy corpus labels (`HARD`/`SOFT`/`DOCTRINE`/`DESIGN`, myth tiers) stay
  advisory; they do not map onto these statuses without lore's explicit
  mapping (`worldbible-integration-contract.md:104`; triage §5,
  `to-verify-triage-protocol.md:100`).
- The statuses do not amend the triage protocol's own outcomes: triage
  confirms/downgrades/excises reference claims (`:67-71`); this table types
  handoff rows so that a lore reviewer can see, per claim, exactly how much
  weight the lane asserts.

## 8. Pinned bytes at read time (2026-10-18T00:28:48+00:00 window)

```
5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069  corpus/knowledge/synthesis/worldbible-integration-contract.md
073a348b38c5d8b27cef8f109afed06ff592da00f2eb91252657ab857e32fb13  corpus/knowledge/verification/to-verify-triage-protocol.md
6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f  reports/round-11/handoff/packet.md
27b9f958c76da4ad29c4395a237ce158a8d7b86103b7b5fa11d04cc3fe6fea64  reports/round-12/adjacency/A11-A12-handoff.md
9fb89a062253a9273196ee8b8122f62598d74ce6b32b124034be5029c44ba0a2  reports/round-12/adjacency/contract.md
a0cf784a8ccc6ccd703aeb5ba876f6607be714d8785addc28d50b04998d59cb5  reports/round-15/claims.json
9a6057315e4a63598ab3c70209a41aa466ebbd42768308b42f40f1328ac00a26  reports/round-15/handoff/v2-design.md
e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575  tools/gates/handoff-packet-check.py
52d5f4d1be6ac97a143323306eafa9c9649484f25de60de8a3ee7630d8c6792c  SKILL.md
```

- HEAD at read time: `c60b17c21a77182a5c1f0251e98b4ea42e563c3e`.
- Dependency status at last poll: v2 **schema design** landed and vocabulary
  verified (§2 receipts); final `packet-v2.yml` bytes still absent
  (`ls reports/round-15/handoff/` → `v2-design.md` only,
  2026-10-18T00:40:13+00:00). `to-verify`: §3–§4 against the finished packet
  bytes before the orchestrator lands §6 into SKILL.md.
- Nothing in rounds 8–14 was read as writable; this worker wrote this file
  only.
