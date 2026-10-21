# ReviewQuality7 — proposed QUALITY.md criterion 7 wording (claim Ca, draft-review)

Axes: coverage (both r49 defect classes named), operability (wording maps 1:1 to
checker channels lands/exports), calibration (grounded in the spot-check, criterion-6 style).

## Assigned item

Propose the exact wording of `corpus/QUALITY.md` criterion 7 (separability: each claim
verifies on base + its own lands only; a claim may not cite identifiers another claim
lands), grounded in `corpus/lessons/round-49-verifier-spotcheck.md`, matching the style of
criterion 6, <= 6 lines.

## Evidence read this session

- `reports/round-50/claims.json` — Ca lands `corpus/QUALITY.md`; after_required: "QUALITY
  criterion 7 cites the spot-check". Separability contract: dependency = landed bytes match
  a Y export regex OR name a Y land path; leg = base + X lands only.
- `corpus/QUALITY.md:29` (file ends there) — criterion 6 is a single paragraph line: bold
  rule title + em-dash, two–three imperative clauses, closing "Grounded in the reviewer
  disagreement and correction at `corpus/lessons/round-49.md#post-review-corrections`
  (S034, S038, S039 → S044–S046)." No tool paths named. No "separab" text exists yet.
- `corpus/lessons/round-49-verifier-spotcheck.md:15-17` — "## Adjudication" anchor;
  REJECTED-HONEST-STOP because "C cites the registry S creates" and "the c_without_s runner
  leg retained inline URLs rather than the required registry rows and therefore did not
  verify the required counterfactual."

## Proposed exact wording (recommended — variant A, style-faithful)

Insert after `corpus/QUALITY.md:29`, separated by one blank line (criterion 6 names no
tooling; Ca's after_required only demands the spot-check citation, so the checker path
stays in the claims manifest, not QUALITY):

```
7. **Claims stay separable** — each round claim verifies on the base commit plus only the
   paths it itself lands; its landed bytes may not cite an identifier another claim exports
   or name a path another claim lands, and a counterfactual leg that quietly retains the
   dependency (inline URLs where the registry rows should be) does not count as
   verification. Grounded in the r49 REJECTED-HONEST-STOP at
   `corpus/lessons/round-49-verifier-spotcheck.md#adjudication` (C → S).
```

6 wrapped lines (or one paragraph line, criterion-6 layout — either satisfies <= 6 lines).
Style mirrors criterion 6: bold rule title + em-dash; semicolon-separated imperative
clauses; a "does not count as X" clause paralleling "never an in-place tier edit"; closing
"Grounded in … at `<lesson>#<anchor>`" with concrete ids (`C → S`).

## Variant B (only if L1 wants the enforcement named)

```
7. **Claims stay separable** — each round claim verifies on the base commit plus only the
   paths it itself lands; its landed bytes may not cite an identifier another claim exports
   or name a path another claim lands (`tools/check-claim-separability.py` enforces this),
   and a counterfactual leg that quietly retains the dependency does not count as
   verification. Grounded in the r49 REJECTED-HONEST-STOP at
   `corpus/lessons/round-49-verifier-spotcheck.md#adjudication` (C → S).
```

Also 6 lines; trades the concrete parenthetical for the tool path. Not recommended —
breaks criterion 6's no-tool-path convention for no after_required gain.

## Why this wording (per axis)

- Coverage: names both failure classes the r49 stop found — (1) cross-claim citation
  ("C cites the registry S creates" → "may not cite an identifier another claim exports or
  name a path another claim lands", matching the contract's two dependency channels:
  export-regex match, land-path naming) and (2) unfaithful counterfactual ("retained inline
  URLs … did not verify the required counterfactual" → the parenthetical clause).
- Operability: "base commit", "lands", "landed bytes", "exports" are the manifest/checker
  vocabulary verbatim; each clause is decidable by the tool, no aspirational language.
- Calibration: grounding pointer is the exact adjudication anchor
  (`#adjudication`, lesson lines 15–17), same "Grounded in …" pattern as criterion 6,
  which the lesson itself notes was born the same way ("outside tier/quote disagreement
  became QUALITY criterion 6").

## Unrun checks

- `tools/check-claim-separability.py` and `reports/round-50/separability/r49-fixture.json`
  are not present in the working tree at review time (before_checks confirm they land with
  Ca); wording was validated against the dispatch's separability contract semantics, not
  against executed tool output. After Ca lands, the wording's clauses should be re-read
  against the checker's actual finding text (`SEPARABILITY_DEPENDENCY X->Y via <evidence>`)
  for vocabulary drift.
- No rendering check of QUALITY.md post-insertion (no production writes from a review seat).

Report: reports/round-50/build/ReviewQuality7.md (this file, at
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-50/build/ReviewQuality7.md`).
Author-lane advice, not an admission; no test weakened, no control removed.
