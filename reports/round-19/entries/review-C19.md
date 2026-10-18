# R19-C28 (extended) — reviewer of entry `era-material-scoped-reconciliation.md`

- round: 19 (loop 2 of 3, build round 3 of 4; `hyper/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- **seat record:** eight reviewer seats (R19-C21..C28) were dispatched against
  ten landed entries. The 1:1 mapping covers entries C11–C18
  (`review-C11.md` … `review-C18.md`). This file is the **extended coverage**
  for the ninth entry, filed by seat R19-C28 so that no entry in the round's
  declared gap registry is left unreviewed. `review-C20.md` covers the tenth.
- date: 2026-10-18, stamps UTC. Window 11:31–11:42Z. Baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: **NON-CANON** engineering review; author-side evidence only.
- writes: **this file only** plus `.scratch/r19c/`. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/synthesis/era-material-scoped-reconciliation.md` — new
synthesis entry, gap `era-material-scoped-reconciliation`
(`reports/round-19/gaps.md`, seat R19-C19). Anchor: sha256
`6c92cf3b13a52ec0c7bc9c82ebc714d7e711d5cb0a937784bc5b0b45d5379fd2`, 11,468
bytes, 76 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: all four mandated checks pass.** No defect found.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

Head block = L1–18 (first `## ` at L20). `- topic:` L3, `- sources:` L5
(8 sub-bullets), `- couples:` L15, `- source:` L16, `- verified-at:` L17,
`- recheck:` L18; `- gap filled:` L4. Decision record `## 6.` (L68), rows 1–6.
Instrument → `missing_frontmatter=[] gap=True decision_record=True`.

**`to-verify` mark census (recorded to prevent a false positive).** The
instrument counts 13 literal `to-verify` occurrences, but they are the entry's
**row vocabulary** (`mapped-unconfirmed`, "a `(to-verify)` row holds"), not 13
unverified claims. The only genuine open item is decision-record row 6.

## 2. Source resolvability — PASS

| cited surface | this seat's check (11:36–11:41Z) | result |
|---|---|---|
| `tools/d2-typed-labels.py --selftest` | exit 0, `39/39 checks passed`; the era rows the entry quotes are present verbatim ("era: a contract tag is identity", "era: the declared legacy handle is mapped-confirmed", "era: a (to-verify) ERX row is mapped-unconfirmed, never promoted", "era: an unnamed label is unmapped, never identity-by-number", "era: the declared two-to-one row is kept, not collapsed", "probe: a foreign era label holds rather than merging by number") | **matches** KTD-EM-S-0002 |
| `examples/culture-d4/typed-labels.d4.yml` `era_material_reconciliation` | 6 records `GAR-01`…`GAR-06`, each with `era {code: R-ERA-IN-SCOPE, tag: E0/E1}` and `material {code: R-MAT-RESOLVED, resolved: CMAT-0n}`, `findings: []` | **matches** KTD-EM-S-0003 |
| same file, `coverage` | `reconciliation_records 6`, `conflicts 4`, `rank_quarantine_handles 3`, `rank_rules_unresolved_items 13` | **matches** KTD-EM-S-0004 |
| `corpus/knowledge/synthesis/era-language-staging.md`, `era-myth-language-costume-matrix.md`, `loanword-material-dating.md` | exist | resolve |
| `corpus/knowledge/verification/to-verify-triage-protocol.md` §1–§2, `calibration-registry.md` §1 | exist | resolve |
| `corpus/knowledge/culture-material/era-periodization-models.md`, `material-culture-inference-method.md` | exist | resolve |

All cited repo paths resolve. The entry cites **no URL**, so the "retrievable
locator" requirement is met by repo paths (13 resolved).

## 3. No filler — PASS

- **Gap named and real** (L4). Re-run 11:40Z: `grep -rln -i "reconcile_scoped\|
  mapped-confirmed\|mapped-unconfirmed" corpus/knowledge/synthesis/` → this
  entry plus `typed-label-routing-workflow.md` (a round-19 sibling that cites
  it); nothing pre-existing. `era-language-staging.md` stages language across
  eras but never states the label-resolution rule.
- **Delivers**: a 5-row row-vocabulary table (§2), a 6-row design-obligation
  table (§3), a non-licence shelf (§4), a 6-item reviewer checklist (§5), a
  6-row decision record (§6).
- **Calibration**: the entry is careful to bound its claim — "a resolution is
  not a date", "a mapping is not attestation" — and hands chronology to
  lore-shokunin.
- **Canon hygiene**: §6-5 rejects resolving by ordinal or text.

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.189**
  (`verification/header-conformance-readings.md`) — the lowest of the ten new
  entries; no near-duplicate.
- **vs round-19 siblings**: J=0.343 (`typed-label-routing-workflow.md`), which
  cites this entry's row vocabulary in its §3. Cross-coupled by design.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| — | none against this entry | — | — |

## 6. Limits

- Author-side review only. The round-8 design shard (R8-D05) behind the rule was
  cited via the tool, not re-inspected — the entry says the same.
- The `conflicts 4` and `rank_rules_unresolved_items 13` coverage counts were
  read from the projection, not re-derived from the packet.
- Verdicts bind to sha256 `6c92cf3b…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C19.md
