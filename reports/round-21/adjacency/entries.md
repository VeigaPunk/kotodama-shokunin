# Round 21 adjacency — new-entry bleed check (A01–A04)

- **Scope:** the ten new round-19 corpus entries, the round-20 authored fragments and lesson, the v3 handoff surfaces, and the D4 content they carry. This is a boundary audit, not a canon, source-rights, or game-design ruling.
- **Snapshot:** `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-18T13:49:36Z`; `git rev-parse HEAD` → `8115eaaeb57c9dce157fe291337cb52dd914c6cf`; `git status --short` → empty, all run at the lane root on 2026-10-18. `PROVINCE.md` digest `05b34a579c5d…` and the read-only world-bible contract digest `5f4c02bfc4e6…` were re-measured with `sha256sum` on 2026-10-18.
- **Inventory evidence:** at `2026-10-18T13:54:41Z`, with `TMPDIR=$PWD/.scratch` exported at the lane root, this exact command:
  ```sh
  python3 -B -c 'from pathlib import Path; v=["label-channel-routing-verification.md","pre-declared-hold-set-reconciliation.md","generated-artifact-roundtrip-verification.md","gate-battery-surface-verification.md","two-reader-interop-agreement.md"]; s=["typed-label-routing-workflow.md","generated-artifact-lifecycle.md","hold-set-contract-in-brief.md","era-material-scoped-reconciliation.md","finding-disposition-workflow.md"]; r=[Path("corpus/knowledge/verification")/p for p in v]+[Path("corpus/knowledge/synthesis")/p for p in s]; a=[Path("reports/round-19/entries")/f"R19-C{i}.md" for i in range(11,21)]; b=[Path("reports/round-20/entries")/f"R20-D{i}.md" for i in range(21,25)]; print("R19 corpus:",len(r),sum(p.is_file() for p in r)); print("R19 author fragments:",len(a),sum(p.is_file() for p in a)); print("R20 author fragments:",len(b),sum(p.is_file() for p in b))'
  ```
  returned `R19 corpus: 10 10`, `R19 author fragments: 10 10`, and `R20 author fragments: 4 4`. Relevant input digests were captured by `sha256sum` on 2026-10-18; prefixes are shown below. The IDs and E-tags in the tables are source locators, not additional counts.
- **Content scan:** on 2026-10-18, `Grep` query `canon|world[- ]bible|rights|clearance|permission|gameplay|game mechanic|mechanics` over `examples/culture-d4/`, `reports/round-20/entries/`, and the handoff packets `packet-v3-16.md` and `packet.md`; full round-19 corpus entries were read individually, and `capability-draft.md` and `frozen.md` were read individually. Hits were read in context. No round validator was run (its receipt is a writer); no pre-existing file was changed.

## A01–A04 verdicts

| claim | verdict | basis |
|---|---|---|
| **A01 — inventory and per-entry coverage** | **PASS** | The dated inventory command above confirms all ten round-19 corpus entries and all four R20-D21..D24 fragments. Verdicts follow for each; the lesson, handoff v3 packet/docs, claims-map/design and the D4 scope controls are separately listed. |
| **A02 — canon boundary** | **PASS — no bleed found** | `PROVINCE.md` §§Refuses/Adjacent contract reserve canon to lore. The entries document lane methods or explicitly label themselves NON-CANON. The v3 packet's D4-CL12 is typed `candidate world-fact`, `unresolved`, and routed to lore; it is not a world-fact assertion (`packet-v3-16.md`, D4-CL12; `claims-map.md`, D4-CL12). Its requested decisions remain questions for lore, not decisions by kotodama. |
| **A03 — real-world rights/attribution ruling** | **PASS — no ruling found; question stays open** | `PROVINCE.md` reserves real-world rights/attribution rulings. D4's brief/provenance and the handoff explicitly say no real-world clearance, consultation, permission, or rights ruling is claimed or made (`examples/culture-d4/brief.md:3-11`; `components/12-provenance.yml:46-50,68-72`; `packet-v3-16.md`, D4-CL11). The unscreened-name question remains a hold/open item, not a clearance. |
| **A04 — game-mechanics bleed** | **PASS — none found** | The round-19 entries are verification/design workflows. D4's “furnace rights,” garment permissions, and rank rules are explicitly fictional culture/institution records; the `rights` lexical hits are not real-world legal rulings or game mechanics. The scan found no gameplay/game-mechanics content. |

## Round-19 entry verdicts

Each verdict is about province bleed, not whether the entry's engineering measurements are correct. Digests are the first 12 hex characters of `sha256sum` output captured on 2026-10-18.

| entry | subject | verdict and boundary evidence | SHA-256 prefix |
|---|---|---|---|
| `corpus/knowledge/verification/label-channel-routing-verification.md` | Route form-bearing records to the correct verification channel. | **PASS.** Says this is lane policy, not a language claim; canon is lore's. No real-world clearance or gameplay ruling. | `22e27dd62c34` |
| `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md` | Reconcile declared and emitted findings. | **PASS.** Explicitly says reconciled sets are debt, not clearance or canon. | `9c4a6f3e8cec` |
| `corpus/knowledge/verification/generated-artifact-roundtrip-verification.md` | Verify generated artifacts and byte identity. | **PASS.** Limits evidence to lane-local engineering; determinism/digests do not establish truth or canon. | `66d9aa18f4e2` |
| `corpus/knowledge/verification/gate-battery-surface-verification.md` | Describe what the gate battery measures. | **PASS.** Bounded gate-method evidence; explicitly not a canon/design-quality claim. | `48e0ae7590d9` |
| `corpus/knowledge/verification/two-reader-interop-agreement.md` | Compare independent readers. | **PASS.** Agreement is consistency, not truth or clearance; no adjudication of canon. | `daebba3ae825` |
| `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | Design-side typed-label routing workflow. | **PASS.** A workflow for invented packet records; explicitly not a canon decision or claim about a real language. | `5e37da4aaaf8` |
| `corpus/knowledge/synthesis/generated-artifact-lifecycle.md` | Source/generated-artifact lifecycle. | **PASS.** File-ownership and rebuild method only; explicitly rejects treating digests as truth. | `a3393d06a3c2` |
| `corpus/knowledge/synthesis/hold-set-contract-in-brief.md` | Declare expected findings before implementation. | **PASS.** A design brief procedure; declaration is a prior/debt, not approval or canon. | `e1c6780a9201` |
| `corpus/knowledge/synthesis/era-material-scoped-reconciliation.md` | Resolve fixture era/material labels by declared rows. | **PASS.** States tags are fixture-relative, not dates; says reconciliation does not license chronology or canon. | `6c92cf3b13a5` |
| `corpus/knowledge/synthesis/finding-disposition-workflow.md` | Route gate findings to owned design work. | **PASS.** A lane workflow; disposition and green re-run are explicitly not clearance or canon. | `9d23492f6396` |

## Round-20 content verdicts

Digests are first-12-character prefixes from dated `sha256sum` runs on 2026-10-18. The R20-D fragments are operational evidence; the handoff packets and supporting D4 material are the substantive boundary-sensitive content.

| content | verdict and boundary evidence | SHA-256 prefix |
|---|---|---|
| `corpus/lessons/round-20.md` | **PASS.** Scope line says NON-CANON and expressly makes no real-world rights/clearance ruling; it preserves filed-round boundaries. | `d54eb3f77d7d` |
| `reports/round-20/entries/R20-D21.md` | **PASS.** Frozen baseline/tamper evidence only; says it certifies neither claim truth nor canon. | `7bc7611217dc` |
| `reports/round-20/entries/R20-D22.md` | **PASS.** Capability row is a draft; explicitly confers no admission and no truth/canon/clearance. | `e1a837a712ca` |
| `reports/round-20/entries/R20-D23.md` | **PASS.** NON-CANON integration census; no canon or external rights ruling. | `a951a30dc289` |
| `reports/round-20/entries/R20-D24.md` | **PASS.** Engineering documentation only; no claim inside the packet is certified. | `0a6f35abd37c` |
| `reports/round-20/handoff/packet-v3-16.md` | **PASS — routed candidate material, not canon.** It is deliberately unbound and prepared-not-accepted. D4-CL12 remains unresolved for lore; RD-02 asks lore about attributed beliefs rather than asserting their truth. D4-CL11 disclaims any real-world screening/rights ruling. Fictional “furnace-right” ranks are design records. | `9f37c08af9bd` |
| `reports/round-20/handoff/packet.md` | **PASS — prepared, not canon.** Explicitly NON-CANON and prepared-not-accepted. D4-CL12 is an unresolved candidate world-fact routed to lore; D4-CL11 disclaims a real-world rights ruling. “Furnace right” is fictional institution/rank content, not a real-world ruling or game mechanic. | `e92f5e6775b6` |
| `reports/round-20/handoff/capability-draft.md` | **PASS.** The capability row is a draft and confers no admission or clearance. | `f3869cbcde8f` |
| `reports/round-20/handoff/frozen.md` | **PASS.** The baseline proves byte/verdict reproducibility, not claim truth, lore acceptance, canon, or round completion. | `1c6f69f099b6` |
| `reports/round-20/handoff/v3.md` | **PASS.** Usage/evidence documentation; it says the packet certifies no claim, canon standing, or clearance. | `806fcf6467cf` |
| `reports/round-20/handoff/claims-map.md` | **PASS.** D4-CL12 is explicitly `candidate world-fact` / `unresolved` and lore-owned; D4-CL11 describes absence of a rights ruling, not a ruling. | `4b1b9a35a18f` |
| `reports/round-20/handoff/design.md` | **PASS.** §0/§2 assigns canon/import to lore and rights/permission/publication to operator; the D4 rank and costume material is design-only. | `793fc8a64da2` |
| `examples/culture-d4/` boundary controls: `brief.md`, `README.md`, `components/12-provenance.yml`, and the full-tree lexical scan | **PASS — no out-of-province decision found.** The brief and provenance mark the drill NON-CANON, route canon to lore, and disclaim real-world rights/permission/clearance. Grep hits for “rights” include fictional furnace/garment rank rules; they do not decide real-world rights. No gameplay/mechanics hit. | `brief.md` `00aa85ff6f99`; `README.md` `ba69a2b6f48d`; `12-provenance.yml` `540f7d2258f3` |

## Routed observations and limits

- `candidate world-fact` and “canonical E0–E3 tags” in the handoff are typed/local-schema terms, not canon grants. The former is unresolved and lore-owned; the latter means packet tag identity (`packet-v3-16.md`, D4-CL08/CL12; `claims-map.md`, corresponding rows).
- “Furnace rights” and “rights to wear a mark” are fictional institutional relations in D4 material (`components/01-brief.yml`, `components/03-orthography.yml`, `components/09-costumes.yml`); they are not determinations of real-world law, attribution, permission, or clearance. Real-world screening remains explicitly unperformed/open.
- `PROVINCE.md` remains accurate for this content: canon → lore; real-world rights/attribution → operator; game mechanics → game-dev-2d/3d. No repair or scope expansion is proposed.
- This static read/lexical audit is not legal clearance, community consultation, canon adjudication, or a full source-quality audit. The review makes no claim beyond the named snapshot and search surface.

FILES: reports/round-21/adjacency/entries.md | SUMMARY: A01–A04 pass; ten round-19 corpus entries and round-20 boundary-sensitive content show no canon, real-world rights, or game-mechanics bleed; candidate lore decisions and real-world screening remain routed/open.
