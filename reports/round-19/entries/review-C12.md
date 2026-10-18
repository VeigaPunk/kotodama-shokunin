# R19-C22 — reviewer of entry `pre-declared-hold-set-reconciliation.md`

- round: 19 (loop 2 of 3, build round 3 of 4; `hyper/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- date: 2026-10-18, stamps UTC. Review window 11:31–11:42Z. Baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: **NON-CANON** engineering review; author-side evidence only; no
  admission, no promotion verification.
- writes: **this file only** plus `.scratch/r19c/`. No corpus/tool/filed-round
  byte touched. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md` — new
verification entry, gap `pre-declared-hold-set-reconciliation` (declared in
`reports/round-19/gaps.md`, seat R19-C12). Anchor: sha256
`9c4a6f3e8cec46d39c47a9aa40e6dd5e13b45a6666e073cef741dbef74c372fa`, 12,608
bytes, 83 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: all four mandated checks pass.** No defect found.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

Head block = lines 1–18 (first `## ` at L19). Fields each exactly once:
`- topic:` (L3), `- sources:` (L5, 8 nested sub-bullets), `- couples:` (L14),
`- source:` (L15), `- verified-at:` (L16, dated, scope-bearing), `- recheck:`
(L17); `- gap filled:` clause at L4. Decision record `## 6.` (L74) with rows
1–6. Instrument `.scratch/r19c/check.py` → `missing_frontmatter=[] gap=True
decision_record=True`.

## 2. Source resolvability — PASS

| cited surface | this seat's check (11:36–11:41Z) | result |
|---|---|---|
| `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | re-run → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` | **matches** KTD-HS-S-0004 |
| `examples/culture-d4/expected-holds.json` | read → `counts {'hold': 15, 'note': 1, 'fail': 0}`; keys `counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema` | **matches** KTD-HS-S-0002 |
| `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration` | present at L195; the acceptance criterion A-07 at L224 reads "six holds, zero notes, zero fails" | **matches** KTD-HS-S-0001's 6/0/0 |
| `examples/culture-d4/brief.md` §"Named hold set (pre-implementation)" | present at L44 | resolves |
| `reports/round-18/d4/holds.md` | present; read by path (not re-executed, as the entry states) | resolves |
| `corpus/knowledge/verification/verification-method-overview.md` §3/§6, `gate-frozen-run-standard.md` §2–§3, `verification-independence-anti-circularity.md` §3 | all exist | resolve |
| `https://reproducible-builds.org/docs/` | HTTP 200 | resolves |
| `provenance-audit-ledger-format.md` §8 (cited in §6-4) | exists | resolves |

Every cited repo path resolves; the one URL returns 200. No non-resolving item.

## 3. No filler — PASS

- **Gap named and real** (L4). Re-run 11:40Z: `grep -rln -i "hold set\|
  hold_set_declaration\|pre-declared" corpus/knowledge/verification/` → this
  entry plus its two round-19 siblings (which cite it), and nothing pre-existing.
  The concept previously lived only in the D4 drill and `reports/round-18/d4/holds.md`.
- **Delivers**: a 6-field declaration schema (§2), a three-way reconciliation
  table with four named delta classes (§3), a 5-row control matrix (§4), a
  non-proof shelf (§5), and a 6-row decision record (§6). Usable, table-shaped.
- **Calibration**: the Dijkstra 1972 citation is used for its actual claim (a
  green run shows presence, not absence, of defects); the reproducible-builds
  doc is cited "for the expectation-first discipline, not as a claim about
  content".
- **Canon hygiene**: §6-5 explicitly rejects "matched set as clearance".

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.264**
  (`verification-independence-anti-circularity.md`) — no near-duplicate.
- **vs round-19 siblings**: highest J=0.547 with
  `synthesis/hold-set-contract-in-brief.md`. This is the intended design/check
  pair (the brief declares the set; this entry reconciles the emitted set
  against it), and both entries name each other in `couples:`. Recorded as a
  pairing, not duplication.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| — | none | — | — |

Observations (no action required): (a) the entry's three-way reconciliation
correctly reports the D4 delta (+9 hold, +1 note against the delivered
declaration) — this seat re-measured the two endpoints and they match; (b) the
entry was re-touched at 11:40:11Z by the round's batch revision pass, content
unchanged in the sections checked.

## 6. Limits

- Author-side review only. The round-18 `holds.md` receipt was read by path, not
  re-executed (the entry says the same).
- The 11 union rows "with no delivered trigger and no engine path" were not
  independently re-derived here; they are the cited receipt's finding, and the
  entry correctly leaves the question open (§6-6).
- Verdicts bind to sha256 `9c4a6f3e…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C12.md
