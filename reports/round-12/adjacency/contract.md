# R12-A05..A08 — handoff contract audit

- Date: 2026-10-17. Scope: compare the round-11 exercise packet with `corpus/knowledge/synthesis/worldbible-integration-contract.md` §4; check the lane's lore boundary and the round-8 contract-digest L0 status.
- Writes: this report only. No contract, PROVINCE, L0, packet, sibling, or filed round-8/round-11 artifact was changed.
- Verdict: the exercise is correctly non-canon and unbound, but it is not a fully conformant transfer envelope. The current contract digest and artifact bytes are reproducible; transfer remains blocked by pending bilateral acknowledgment. The claim ledger and D2 coupling presentation have content-conformance gaps despite the clean shape gate.

## Independent measurements

- **2026-10-17T22:37:57Z** — `export TMPDIR=$PWD/.scratch; python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet.md` → exit 0, `fields=16/16 glossary-entries=20 findings=0`. This is a shape/gate result, not proof of semantic completeness, lore review, or acceptance.
- **2026-10-17T22:37:57Z** — `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md reports/round-11/handoff/packet.md` → contract `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`; packet `6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f`. The packet's `contract_ref` names the measured contract digest.
- **2026-10-17T22:45:44Z** — command: `python3 -c 'from pathlib import Path; from hashlib import sha256; r=Path.cwd().resolve(); s=Path("reports/round-11/handoff/packet.md").read_text().split("## artifact_manifest",1)[1].split("\n## ",1)[0]; rows=[[x.strip().strip("`") for x in l.strip("|").split("|")] for l in s.splitlines() if l.startswith("| A-")]; fs=[(c[0],(r/c[1]).resolve(),c[3]) for c in rows if c[1].startswith(("corpus/","examples/","tools/","reports/"))]; assert all(p.is_relative_to(r) for _,p,_ in fs); ok=[sha256(p.read_bytes()).hexdigest()==h for _,p,h in fs]; print(len(fs),sum(ok),len(fs)-sum(ok))'` → 21 file-backed rows checked, 21 matched, zero mismatches. The inline glossary payload row was not treated as a filesystem path. This verifies the manifest digests, not every stated record-count interpretation.

## §4 field comparison

The gate found all required field names. Field-level review of `reports/round-11/handoff/packet.md` found:

| §4 field(s) | Audit |
|---|---|
| `packet_id`, `packet_version` | Present; the packet declares a stable identifier/version and says revised bytes require a new version. |
| `contract_ref` | ID, revision and current digest are present and the digest matches the measured file. **Transfer blocker:** the packet itself says bilateral same-revision reading is pending. §4 requires acknowledgment by both lanes; the exercise correctly does not represent this as complete. |
| `producer`, `recipient`, `request_ref` | Present; producer/recipient roles are named and `request_ref: none` is explained by the absence of a lore brief. |
| `baseline_bible_ref` | `none` is explicitly qualified as a deliberately unbound research packet, the allowed case in §4. It cannot be imported as canon on these bytes. |
| `artifact_manifest` | IDs, paths, digests and a records column are supplied; the file-backed digests matched in the independent pass above. Some entries are tools or source ledgers, so this audit did not independently validate each row's count semantics or assign a separate semantic version to every input. Exact file digests do pin the bytes. |
| `subject_refs` | Candidate IDs are namespaced and explicitly unresolved; no lore entity IDs are guessed. |
| `scope` | Group/region, variety/script, register and era applicability are supplied by record set; absence of real place/dates is explicit for the unbound drills, not left blank. |
| `dependency_manifest` | Profiles, named rules and pinned dependencies are listed; no floating `latest` is used. |
| `claim_ledger` | **Review finding:** the table has no explicit per-claim `uncertainty` dimension, and no claim-to-record/edge relation key. Some summaries state limitations and the packet has a separate coupling section, but neither provides a consistent per-claim carrier or crosswalk required by §4. The earlier contract-check report noted the uncertainty omission; this audit independently observes it in the exercise packet's actual table. |
| `coupling_edges` | **Review finding:** D3's individual bridges carry typed relations and limits, but D2 is summarized as one aggregate dependency edge for the per-record coupling notes. That aggregate does not expose each source→target relation with its own applicability and justification as §4 requires. |
| `requested_decisions` | Per-record/set questions, alternatives and blockers are stated; the packet explicitly limits “accept” to non-canon candidate retention. |
| `validation`, `open_questions` | Checks and observed outcomes are recorded; open issues name responsible lanes and blocking status. The gate's zero findings does not certify truth or bible-wide consistency. |

The key packet evidence is its claim ledger and coupling section (`packet.md`, “claim_ledger” and “coupling_edges”); §4's requirements are in the contract's “Handoff envelope” table. No correction was applied here: the gaps are reported for the parent/integrator to route, not silently absorbed into canon or the contract.

## Lore boundary and PROVINCE

`PROVINCE.md` says this lane owns generative/coupling craft, its own records, gates and non-canon examples, while refusing canon decisions, real-world rights/attribution rulings and game mechanics; it names the contract as the load-bearing interface and routes contested scope to the integrator. The exercise packet stays within that boundary: it calls itself NON-CANON and deliberately unbound, leaves canon and bible-wide verification to lore, uses unresolved candidate IDs, states that no lore brief/baseline/receipt exists, and does not claim real-language screening, consultation, permission or legal clearance (`packet.md`, opening and `open_questions`). This is consistent with contract §§1, 4, 6, 8 and 10. **Boundary verdict: pass for this exercise; not a lore receipt or transfer authorization.**

## Round-8 L0 contract-digest question

Round-8 X04 recorded the digest change from `50c4c2f2…` at baseline to `5f4c02bf…` after the metadata sweep, while the declared interface revision remained `1.0.0`; it cited lore's L0 question asking whether the older pin should be ratified or the contract reissued with a revision change (`reports/round-8/adjacency.md`, §§2.2–2.4). Its `grep -rln "l0-questions" reports/round-8/` result was zero hits during the 2026-10-17 20:10–20:29Z check window, so round 8 did not answer the L0 item.

The latest lane-local status available to this audit is round-11 X02: at its 2026-10-17 22:07Z check it still recorded the item as open and bilateral same-revision reading as pending (`reports/round-11/adjacency.md`, §3.1); the exercise packet also says the bilateral read is pending. Therefore the operational digest is now `5f4c02bf…`, but the governance/acknowledgment question remains **open in the latest recorded evidence**. Its original `50c4…` premise is stale; the integrator/lore owner should answer or retarget it to the current digest and record both-lane acknowledgment. This pass did not inspect the out-of-lane live L0 surface, so any later status change is `to-verify`.

## Disposition

- Keep the packet classified as a successful non-canon exercise, not an accepted handoff.
- Route the claim-ledger and D2 edge-detail gaps for bounded follow-up; do not edit filed round-11 evidence.
- Keep the L0 item open until lore/integrator action and both-lane read evidence exist. No scope or canon decision is made by this audit.
