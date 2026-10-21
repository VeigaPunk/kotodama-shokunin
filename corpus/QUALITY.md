# corpus/QUALITY.md — the admission bar

An entry is admitted into `corpus/knowledge/` only when it clears all of:

1. **Provenance** — every factual claim carries a cited, checkable source
   (author + year, standard edition, or stable ID). A claim the author
   cannot verify is marked `(to-verify)` inline — never laundered into
   assertion. Invented sources are a conformance defect, not a style issue.
2. **Calibration** — every framework entry names its status: mainstream /
   contested / discredited, with the reason. Pop-mythography
   (Campbell-as-universal, strong Whorf, glottochronology, Frazerian
   evolutionism) must be flagged as such on first use.
3. **Coupling** — the `- couples:` line names the systems/files the entry
   connects. An entry that couples nothing is reference, not craft; it must
   say so.
4. **Usability** — a worldbuilder can act on it: decision tables, typology
   tables, checklists, worked examples. No essays.
5. **Canon hygiene** — no entry decides what is true in any world. Canon
   recording and consistency verification belong to lore-shokunin; entries
   end at the handoff.

Rejections are kept with their rejection reason (see `lessons/`) — a
rejection is evidence of taste.

Source tiers (A/B/C, each scoped to a claim) are defined in `SOURCES.md`,
the lane's opened source registry; a tier-C row is a lead, never sole
support for an admitted claim.

6. **Source authority stays claim-scoped** — publisher descriptions and abstracts are tier B for substantive claims about a work, even when accurate; reserve tier A for sources primary or authoritative for the exact scope. Correct a filed tier with a superseding SOURCES row, never an in-place tier edit. Grounded in the reviewer disagreement and correction at `corpus/lessons/round-49.md#post-review-corrections` (S034, S038, S039 → S044–S046).

7. **Claims stay separable** — each round claim verifies on the base commit plus only the paths it lands itself. Its added lines may not cite an identifier another claim newly exports, nor name a path another claim newly lands; a counterfactual leg that quietly keeps the dependency (inline URLs standing in for the registry rows) or rewrites the other claim's bytes before checking does not count as verification. Sources a claim cites are that claim's lands. Run `tools/check-claim-separability.py` on the round manifest before dispatch. Grounded in the round-49 REJECTED-HONEST-STOP at `corpus/lessons/round-49-verifier-spotcheck.md#adjudication` (C cited the registry S created).
