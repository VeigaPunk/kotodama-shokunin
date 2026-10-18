# R17-D35 — reviewer: D4 myth–costume coupling

- **Seat:** R17-D35 (reviewer, claim D `culture-d4-assembly`), round 17 (operator
  loop 2 of 3, build round 1 of 4; 64 declared workers, `opencode-go/deepseek-v4.1-flash`).
- **Assignment (verbatim):** "D4 R17-D33..D37 (reviewers x5): internal consistency;
  language sketch soundness; myth-costume coupling; hold-set hand re-derivation;
  D2/D3-lesson cross-check. reports/round-17/reviews/review-<n>.md."
- **Date / clock:** 2026-10-18, local -03:00; measurements 09:4x–09:5xZ. Wave in
  flight; statements pinned to the digests in review-1 §1 (packet `2776d85c…35d72`).
- **Write scope:** this file only, plus scratch under `.scratch/r17-review/`. No
  artifact under `examples/`, `tools/`, `reports/round-{8..16}/`, or `corpus/` was
  written; no commit, no push.
- **Canon:** NON-CANON engineering review. Nothing here is canon, a lore receipt,
  a handoff, or a real-world clearance/rights statement.

## 0. Verdict

**The myth–costume coupling system holds: every declared coupling edge I tested
resolves, both coupling gates that cover this area run clean, and the coupling is
carried by records rather than asserted in prose.** Specifically: all 8 symbols
carry the five key fields (`sign/medium/era/register/audience`) plus a holder; all
6 festivals name a declared role and — where a rite is claimed — a declared rite;
all 3 narratives' roles and motifs resolve; all 4 motifs index declared
narratives; all 6 costumes reference a declared material by **slot id**
(`material_ref`) and a declared era; all 4 rank rules' eras/rites/wearer ranks
resolve against the costume and era ledgers; the imported material (`CMAT-04`)
is the only non-local route and it is the one the salt-road contact record names.
`myth-consistency-gate` exit 0 / 0 findings and `costume-era-consistency-gate`
exit 0 / 0 findings (my runs). No new finding; two observations (O2, O3) and two
cross-references (F4 undeclared rank terms; F3 stale register reference).

## 1. Evidence

All commands cwd = lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18; packet digest
`2776d85c…35d72`. Coupling matrix by scratch script (review-1 §2 M6); record
fields read from the packet and the components.

### 1.1 The coupling matrix (all resolved)

| edge class | records | resolution |
|---|---|---|
| narrative → roles | `MYTH-01` ROL-01/06; `MYTH-02` ROL-03/06; `MYTH-03` ROL-02/05 | all 6 roles declared (`ROL-01..06` ↔ `PAN-01..06`) |
| narrative ↔ motifs | `MYTH-01` MOT-02; `MYTH-02` MOT-01/04; `MYTH-03` MOT-03 | 4/4 motifs declared and back-indexed (`MOT-0x.narratives`) |
| festival → role | `FES-01..06` → ROL-01/06/03/02/05/05 | all declared |
| festival → rite | `FES-01`→`RIT-01`, `FES-02`→`RIT-02`, `FES-06`→`RIT-04`; `FES-03/04/05` → `null` | declared rites resolve; three festivals claim no rite (declared null, not a gap) |
| symbol fields | `SYM-01..08` each carry `sign/form/medium/audience/holder/era/register` | all 8 complete (the D2 `MC-S00` aggregate class — symbols lacking a medium — is **not** present here) |
| symbol ↔ institution | holders name the furnace-master, the stamp-house, the smith at the quench, the shade-keeper, the weigh-master (see O2), the bellows crew | institutions of 09/10/11; one undeclared office term (F4) |
| costume → material | `GAR-01..06` → `material_ref` `CMAT-01/02/02/01/03/04` | all declared by slot id (the D3 lesson shape: reconcile by id, never by label; the human label rides `material`) |
| costume → era | `GAR-01..06` → E0/E0/E1/E0/E0/E1 | declared era tags |
| costume ↔ rank rules | `RK-01..04` `wearer_ranks` ⊆ costume `wearer_ranks` ∪ {furnace-master} | gate-checked, exit 0 |
| material → route/era | `CMAT-01..05` each carry `routes[{name,kind,stage,eras}]`; only `CMAT-04` (salt-road cloth) is `import`, eras E1/E2 | matches `11-contact-history` `CT-01` (salt road, E1/E2) and `routes` `RT-01` |
| rank rule → rite/era | `RK-01..04` rites {forge work, league assembly, attesting work, market days}; eras ⊆ E0–E2 | eras declared; rites are free-text labels (O3) |

### 1.2 Gate results (my runs, 09:47–09:51Z)

| gate | exit | findings |
|---|---:|---|
| `myth-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 |
| `costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 |
| `lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml` | 0 | 0 |

The myth gate's three named classes (missing medium, role coverage, motif law)
are all satisfied by the delivered records; the costume gate's era/material/rank
classes are all satisfied. `ASSEMBLY.md` §3 records the same exits.

### 1.3 Cross-checks against the D2/D3 precedent

- **Declared violation class not exercised.** D2 kept one declared costume
  violation visible as exactly one `R-01` note (design §Δ7's analogue); the
  landed furnace-league registry declares **no** violation, and the costume gate
  is clean (exit 0). That is a design choice, not a defect — but the divergent
  `design-brief.md` Δ7 signature ("costume-era gate exits 1 with exactly one R-01
  note") does **not** describe the landed tree; `ASSEMBLY.md` §6 already reports
  the design divergence. The parent should not carry Δ7 forward as an acceptance
  condition for this registry.
- **Attribution discipline.** The D3 lesson "attributed sayings stay attributed"
  has no D4 carrier: the landed registry has no sayings/oaths block, and
  `06-myth.yml:19` points at a register component that does not exist (F3,
  review-1). No narrator-certified truth is claimed anywhere in the myth records
  (they are labelled design records); the missing owner is the finding, not an
  absorbed claim.

## 2. Findings

**No new finding.** F3 (stale register-component reference, `06-myth.yml:19`) and
F4 (`broker`/`weigh-master` undeclared) are filed in review-1 and cross-referenced
here; F5 (finite expansion of `s → z / V_V`) is review-2's and has no coupling
aspect.

## 3. Observations (no action required by this seat)

- **O2 — symbol holders are a mixed population.** Holders name offices
  (`furnace-master`, `stamp-house`, `shade-keeper`, `weigh-master`), crews
  (`bellows crew`), and single actors (`smith at the quench`). The record contract
  does not type `holder`, so this is legal; only the two undeclared terms are
  filed (F4). A future tightening could type `holder` to a rank/office id.
- **O3 — costume/rank `rite` fields are free-text labels.** Only two of the six
  costume labels align by exact name with declared rites ("the quench" ≈ `RIT-02`
  "the quench blessing"; "attesting work" ≈ `RIT-03` "the stamp-taking"); the
  others name occasions/institutions (forge work, the league assembly, the burn,
  market days). The festivals block, by contrast, references rites by id. The
  contract's `record_fields` permits free text, and the costume gate accepts it;
  if the parent wants id-level coupling here, that is a contract change, not a
  repair of these bytes.
- **O4 — the six glossed garments are the coupling seam to the typed chain.**
  Each `GAR-0n` carries `form_slot LEX-GAR-0n` (`status: unfilled`); the legacy
  naming gate turns those six English glosses into the six `PHON-INVENTORY`
  lines, and the declared hold set is exactly those six slots. The coupling
  between the costume ledger and the hold set is therefore one-to-one by record
  (6 costumes ↔ 6 slots ↔ 6 declared holds) — verified at the record level here;
  the typed equality itself is review-4's subject.

## 4. Limits

- This review tests declared couplings, not mythic plausibility, naturalness, or
  any real-world comparison; no real-world source or community is named.
- The typed chain is not landed at this stamp; the typed channel's treatment of
  the six glosses is review-4/review-5 territory.
- The tree was moving during the review; digests in review-1 §1 are the contract.
