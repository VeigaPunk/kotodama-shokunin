# R20-D18 — adversarial review: boilerplate bases and dangling D4 links, packet v3 (build 13)

- seat: R20-D18 (adversarial review), lane
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- date: 2026-10-18. Baseline revision
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`; observed HEAD
  `122086bce0aa577bec221bb2d37eedf20f4f3ed2`. Readings UTC.
- purpose: attack the v3 packet on the two named axes — **boilerplate bases**
  and **dangling D4 links** — with controls proving each attack discriminates.
  The design seats' own plan (`claims-map.md`, `uncertainty-plan.md`) records
  the link-witness commands and the five uncertainty negative controls in
  `review.md`; this file carries the same evidence **independently re-run**
  (this seat's own synthetic claims and spec lists) so the packet-level attack
  stands on its own.
- path note: `reports/round-20/handoff/review.md` was already filed by the
  design-review seat (a design-level review, not a packet review) when this
  seat measured; to avoid clobbering a filed fragment this review is written
  as a separate file. The parent may merge or rename at integration.
- audited bytes: `reports/round-20/handoff/packet-v3-16.md`, sha256
  `9f37c08af9bd56fce668ccb42bd34351d21e650c49e27898ff7736a70dfdd730`
  (measured 13:14:5xZ; builds 14–16 content-identical apart from key and
  stamps; the initial build-13 render and its repair are recorded in
  `audit-v3.md` §3); plus the pre-render copy surface
  `reports/round-20/handoff/claims-map.md` (specs extracted 13:0xZ).
- writes: **this file** plus the seat's other assigned round-20 fragments and
  gitignored scratch under `.scratch/r20-d17/`. No filed round-8..19 byte
  touched; no commit, no push. NON-CANON engineering evidence.

## 0. Verdict

**No dangling link survives the attack on the audited build; no
exact-duplicate or placeholder basis survives; one advisory near-template pair
and one minor traceability gap are named.** On the repaired build
(`packet-v3-16.md`, sha `9f37c08a…`; builds 14–16 content-identical) the attack
resolves **92/92 claim-to-record links** across all 27 rows (50 carried v2 +
42 D4), 46/46 basis locators, 0 self-references, 0 template-vocabulary pairs at
≥ 0.6. The attack's own detection is what caught the initial build-13 render's
major defect: the 15 carried rows' character-split `links` cells returned
**zero parseable specs** — the defect was repaired in the 13:13:14Z re-render
and is recorded in `audit-v3.md` §3. The adversarial axes themselves are clean;
F-A6 (advisory) and the CL01 validation-citation (F-A7) are the remainders.

## 1. The attacks

| attack | rule | fires when |
|---|---|---|
| A1a exact duplicate | normalized bases equal | any pair |
| A1b placeholder/thin | placeholder token, or basis < 60 chars | any row |
| A1c status restatement | normalized basis opens with its own status token | any row |
| A1d template run | longest common token run between two bases ≥ 12 tokens | any pair |
| A1e template vocabulary | Jaccard ≥ 0.6 on token sets | any pair |
| A1f self-reference | a basis or link cites `reports/round-20/handoff/**` (the packet's own dir) | any row |
| A1g validation citation | a basis names a `tools/*.py` check that the `validation` section never names | any row |
| A2a link resolution | every `path#selector` in every links cell resolves (JSON key path → key/value/element; `L<n>` anchor on non-JSON only; word-bounded token otherwise) | any row |
| A2b basis-locator resolution | every locator inside every basis resolves | any row |
| A2c D4 inventory | every D4-surface link classified and resolved; negative control discriminates | any row |

## 2. Commands and results (measured)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 .scratch/r20-d17/advlib.py reports/round-20/handoff/packet-v3-16.md --json .scratch/r20-d17/v3-16-adv.json
python3 .scratch/r20-d17/auditlib.py reports/round-20/handoff/packet-v3-16.md --json .scratch/r20-d17/v3-16-audit.json
python3 tools/harness/packet_links.py --links "<37 specs from claims-map.md>" --repo-root . --json
python3 tools/harness/packet_links.py --links "examples/culture-d4/packet.d4.yml#ER-99,examples/culture-d4/typed-labels.d4.yml#no_such_block,examples/culture-d4/expected-holds.json#counts" --repo-root . --json
```

| attack | observed on packet-v3-16.md |
|---|---|
| A1a exact duplicate | 0 pairs (27 bases, all distinct after normalization) |
| A1b placeholder/thin | 0; shortest basis 244 chars (CL07), longest 455 (the v2 census range) |
| A1c status restatement | 0 |
| A1d template run | **1 advisory**: D2-CL02 ↔ D4-CL09 share a 15-token tail: `none of them is promoted by this packet; owner: kotodama, blocking for the affected D2 …` — the two rows describe the same inherited residuals, so the overlap is apt, but it is named for the packet seat (F-A6) |
| A1e template vocabulary | 0 pairs at ≥ 0.6; top pair D2-CL02/D4-CL09 at 0.21 |
| A1f self-reference | 0 |
| A1g validation citation | **2** on CL01: the basis names `tools/assemble-culture-d3.py` and `tools/check-evidence-coupling.py`; the `validation` section names neither (its rows defer argv to the build receipt) — this is `audit-v3.md` F-A3's evidence form, reported from the other direction |
| A2a link resolution | **92/92 resolve on the audited build** (50 carried v2 + 42 D4); the initial build-13 render returned 0 parseable specs for the 15 carried rows (character-split cells) — detection recorded, repaired at 13:13:14Z |
| A2b basis-locator resolution | 46/46 resolve (`audit-v3.md` §3) |
| A2c D4 inventory | 42 links, all into `examples/culture-d4/**` or the round-18 receipts; 0 dangling |
| pre-render specs (claims-map) | this seat 37/37; harness `links=37 resolved=37 findings=0` |

## 3. The alias-witness attack (the one claim whose status is another seat's evidence)

D4-CL08 is typed `supported` on the alias-evidence row. Attacked independently:
a scratch mirror holding `tools/` + `examples/culture-d4` **without**
`examples/culture-d2` was built (13:07Z) and the projector run over the D4
packet → exit 0, "byte-identical deterministic projection". The negative
control the design demands (same run with the D2 tree restored) is the packet's
own validation row (both exit 0, declared). The projection's
`era_reconciliation.basis` names the D4 packet's own `named_eras` and records
the skip (measured in `examples/culture-d4/typed-labels.d4.yml`,
`cbcf997f…` at 13:05Z, since re-emitted). The flip is evidence-keyed, not
intent-keyed — the attack finds no support without the run.

## 4. Controls — each attack must fire when the defect is present

| control | mutation | observed |
|---|---|---|
| synthetic boilerplate packet (`.scratch/r20-d17/synth-boilerplate.md`) | two rows share a long basis tail; a third basis is 44 chars | fires `ADV-TEMPLATE-RUN` (17-token run), `ADV-TEMPLATE-JACCARD` (0.89), `ADV-BASIS-SHORT` |
| link negative control | `packet.d4.yml#ER-99`, `typed-labels.d4.yml#no_such_block`, `expected-holds.json#counts` | exit 1: 2 × `L-TOKEN-MISSING`, third ok |
| uncertainty mutations (own synthetic claim sets, `packet_uncertainty.py --claims-json`) | duplicate basis; partial without restriction; unresolved without owner; status `tentative`; basis `grounding: unknown` | exit 1 each: `U-BASIS-DUPLICATE`, `U-BASIS-NO-RESTRICTION`, `U-BASIS-NO-OWNER`, `U-STATUS-VOCAB`, `U-BASIS-SHORT` |
| positive control | the same link resolution over the v2 build05 twin | 50/50 resolve (2 digest-drift findings, expected) |

## 5. Limits

- The attacks are structural (resolution, similarity, duplication); they do not
  judge whether a witness *supports* its claim — that is the contract audit's
  field-by-field reading (`audit-v3.md` §2) and, beyond it, lore's.
- The template heuristics (A1d/A1e) are advisory by construction: a shared run
  is not a validator failure, and F-A6 is filed as advisory.
- Build 13 is expected to be superseded (the D4 tree moved during the audit);
  a later keyed build must be re-attacked as new bytes, and F-A1's repair must
  be verified on the **markdown** surface.
