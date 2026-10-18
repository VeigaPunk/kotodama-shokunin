# R19-C26 — reviewer of entry `typed-label-routing-workflow.md`

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

`corpus/knowledge/synthesis/typed-label-routing-workflow.md` — new synthesis
entry, gap `typed-label-routing-workflow` (`reports/round-19/gaps.md`, seat
R19-C16). Anchor: sha256
`5e37da4aaaf849e6c2cb2eacec0207911290db32c3c91bc6bd7bca357d96bff2`, 12,811
bytes, 88 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: 3 of 4 mandated checks pass clean; 1 defect (a broken `couples:`
target, the same one as `review-C11.md`).**

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **defect — 1 broken cross-reference** (§2) |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

Head block = L1–19 (first `## ` at L21). `- topic:` L3, `- sources:` L5
(9 sub-bullets), `- couples:` L16, `- source:` L17, `- verified-at:` L18,
`- recheck:` L19; `- gap filled:` L4. Decision record `## 6.` (L80), rows 1–6.
Instrument → `missing_frontmatter=[] gap=True decision_record=True`.

## 2. Source resolvability — DEFECT (1 broken cross-reference)

| cited surface | this seat's check | result |
|---|---|---|
| `SKILL.md` §"Label typing — translated labels, native forms, borrowed strata" | present at `SKILL.md:31` | resolves |
| `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | re-run → exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` | **matches** |
| `examples/culture-d4/typed-labels.d4.yml` `coverage` | `typed_labels 74`, `labels_by_kind {native-form 56, translated-label 12, borrowed-strata 6}`, `label_findings_fail 0`, `label_findings_hold 12` | **matches** KTD-TW-S-0003 |
| `examples/culture-d4/brief.md` §"Named hold set (pre-implementation)" | present at `brief.md:44` | resolves |
| `examples/culture-d4/components/01-brief.yml` `contract.hold_set_declaration` | present at L195; six garment slots, zero fails (A-07 at L224) | resolves |
| `corpus/knowledge/synthesis/glossary-registry-format.md`, `loanword-material-dating.md`, `conlang-blueprint-template.md`, `worldbible-integration-contract.md`, `costume-language-coupling-table.md` | all exist | resolve |
| `corpus/knowledge/linguistics/language-contact.md`, `color-terminology.md` | exist | resolve |
| `https://doi.org/10.1109/TSE.2010.62` | HTTP 202 | resolves |

### The defect: `../linguistics/phonology-sanity.md` does not exist

L16 `couples` names, under `linguistics —`, `../linguistics/phonology-sanity.md`.
That path does not exist: `corpus/knowledge/linguistics/` holds
`phonetics-phonology.md`. The entry already cites the verification file
`../verification/phonology-sanity-gate.md` on the same line, which resolves — so
the broken pointer is a scope mix-up, not a missing source.

- Severity: **low** — a couples pointer that does not resolve; no load-bearing
  claim depends on it.
- This is the same defect class as `review-C11.md` R19C21-F1 (the paired
  verification entry). The two entries were authored by sibling seats from the
  same couples template, so one fix likely addresses both.

## 3. No filler — PASS

- **Gap named and real** (L4). Re-run 11:40Z: `grep -rln -i "translated-label\|
  route.*channel\|typed label" corpus/knowledge/synthesis/` → this entry only;
  nothing pre-existing.
- **Delivers**: a 7-step routing pass P1–P7 (§2), a scoped-slot section (§3), a
  5-row owed-slot backlog table (§4), a non-licence shelf (§5), a 6-row decision
  record (§6).
- **Canon hygiene**: §1 and §5 hand canon to lore-shokunin; §6-5 rejects
  filling an owed slot with a gloss.
- **Calibration**: the mutation-testing survey is cited "as a design rule for
  the routing pass's controls, not as a law".

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.211**
  (`verification-independence-anti-circularity.md`) — no near-duplicate.
- **vs round-19 siblings**: J=0.509 with
  `verification/label-channel-routing-verification.md`. This is the intended
  design/check pair: the workflow routes records before a gate reads them, and
  the verification entry checks the routing. Both name each other in `couples:`.
  Recorded, not scored as duplication.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| R19C26-F1 | L16 `couples` names `../linguistics/phonology-sanity.md`; no such file exists (the partition holds `phonetics-phonology.md`). The same line already cites `../verification/phonology-sanity-gate.md`, which resolves. | low | **open — reported to parent**; this seat holds no corpus write |

## 6. Limits

- Author-side review only; the round-17/18 receipts behind the counts were read
  by path, not re-executed (the entry states the same).
- The P1–P7 order is a design assertion this seat did not attempt to falsify.
- Verdicts bind to sha256 `5e37da4a…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C16.md
