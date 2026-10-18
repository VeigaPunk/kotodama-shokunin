# R19-C28 — reviewer of entry `hold-set-contract-in-brief.md`

- round: 19 (loop 2 of 3, build round 3 of 4; `hyper/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- date: 2026-10-18, stamps UTC. Window 11:31–11:42Z. Baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: **NON-CANON** engineering review; author-side evidence only.
- writes: **this file only** plus `.scratch/r19c/`. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/synthesis/hold-set-contract-in-brief.md` — new synthesis
entry, gap `hold-set-contract-in-brief` (`reports/round-19/gaps.md`, seat
R19-C18). Anchor: sha256
`e1c6780a92014281790ade4ff8590dc722c19451ff54e141eeca09bd5cdb113b`, 10,596
bytes, 80 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

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
`- recheck:` L18; `- gap filled:` L4. Decision record `## 6.` (L72), rows 1–6.
Instrument → `missing_frontmatter=[] gap=True decision_record=True`.

## 2. Source resolvability — PASS

| cited surface | this seat's check (11:36–11:41Z) | result |
|---|---|---|
| `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration` | present at L195; the brief's own comment at L66 reads "six unresolved garment form slots, zero fails"; A-07 at L224 restates 6/0/0 | **matches** KTD-HB-S-0001 |
| `examples/culture-d4/brief.md` §"Named hold set" | present at L44 | resolves |
| `reports/round-18/d4/holds.md` §0–§6 | present; read by path | resolves |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` | **matches** KTD-HB-S-0004 |
| `examples/culture-d4/expected-holds.json` | `counts {'hold': 15, 'note': 1, 'fail': 0}` | **matches** |
| `corpus/knowledge/synthesis/conlang-blueprint-template.md` §0, `coupling-model.md` §1/§5 | exist | resolve |
| `corpus/knowledge/verification/pre-declared-hold-set-reconciliation.md`, `verification-independence-anti-circularity.md` §3, `gate-frozen-run-standard.md` §2, `provenance-audit-ledger-format.md` §8 | all exist | resolve |
| `https://reproducible-builds.org/docs/` | HTTP 200 | resolves |

All cited repo paths resolve; the URL returns 200.

## 3. No filler — PASS

- **Gap named and real** (L4). Re-run 11:40Z: `grep -rln -i "hold_set_declaration\|
  hold set\|expected finding" corpus/knowledge/synthesis/` → this entry plus
  three round-19 siblings (which cite it); nothing pre-existing. The concept
  previously lived only in the D4 brief and `reports/round-18/d4/holds.md`.
- **Delivers**: a 6-field declaration schema (§2), a 4-bullet prior-consumption
  section naming the delta classes (§3), a non-licence shelf (§4), a reviewer
  checklist (§5), a 6-row decision record (§6).
- **Canon hygiene**: §4 and §6-5 refuse clearance and hand canon to
  lore-shokunin.
- **Calibration**: reproducible-builds is cited "as the discipline, not as a
  claim about content".

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.221**
  (`verification-independence-anti-circularity.md`) — no near-duplicate.
- **vs round-19 siblings**: J=0.547 with
  `verification/pre-declared-hold-set-reconciliation.md`. This is the intended
  design/check pair — the brief declares the expected set, the verification
  entry reconciles the emitted set against it — and both name each other in
  `couples:`. The high token overlap is the shared object (the D4 declaration,
  the six fields, the delta vocabulary) seen from two sides. Recorded, not
  scored as duplication.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| — | none against this entry | — | — |

## 6. Limits

- Author-side review only; the round-18 `holds.md` receipt was read by path, not
  re-executed (the entry states the same).
- The declaration's six fields are a design schema this seat checked for
  presence against the delivered brief, not for completeness of every possible
  declaration.
- Verdicts bind to sha256 `e1c6780a…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C18.md
