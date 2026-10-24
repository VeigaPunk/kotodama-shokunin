# ScoutRow08 — ROW-OPENING (claim C): S819, S820

Artifacts (under .ufo/waves/round-67/rows/ScoutRow08/):
- row-S819.txt — U.S. National Library of Medicine, Historical Anatomies on the Web, "Andreas Vesalius: Author & Title Description" (docs, tier A). Anchor: "Vesalius performed his own careful dissections and observed the body in great detail, confirming and refuting many of Galen's anatomical and physiological tenets." (24 words, verified verbatim in live body text).
- row-S820.txt — Tognotti, "Lessons from the History of Quarantine, from Plague to Influenza A," Emerging Infectious Diseases 19(2) 2013 (paper, tier A). Anchor: "the first permanent plague hospital (lazaretto) was opened by the Republic of Venice in 1423" (15 words, verbatim in live body text).
- rejects.txt — 3 rejected candidates with flip notes (wrong-PMC-id; NLM nav-only page; EuropePMC XML mirror kept as fallback).

Verification performed (curl, 2026-10-24):
- S819 live: HTTP 200, Date Sat, 24 Oct 2026 12:37:52 GMT, quote present in stripped body text; no redirects/paywall.
- S819 capture: 20260803194629 id_ replay HTTP 200, 11,651 bytes, quote present. 5+ snapshots in CDX (2025-10-06 .. 2026-08-03).
- S820 live: HTTP 200, Date Sat, 24 Oct 2026 12:39:26 GMT, quote present; note the live page carries 4 'lazaretto' mentions including the anchor sentence in §History.
- S820 capture: 20260927110912 id_ replay HTTP 200 — capture is stored content-encoded; needs `curl --compressed` (without it, output is gzip garbage). With decompression: 150,614 bytes identical-length to live, quote present.
- Uniqueness: grep of corpus/SOURCES.md and all current .ufo/waves/round-67/rows/ fragments — no collision for either URL (pmc.ncbi.nlm.nih.gov/articles/PMC3559034/ is a distinct article id from existing PMC rows S050/S075/S099/S100/S117/S119/S124).

Field validation: simulated accept-c.py RESTATE logic locally — S819 bullet in-order quote hits = 3, teaches coverage 0.0, novel words present; S820 bullet hits = 5 (first/permanent/plague/hospital/venice), teaches coverage 0.0, novel words present. quotes 8–25 words, teaches ≤240 chars, scope ≤60 chars, cells = 11, kind enum, tier A/B, status mined, opened 2026-10-24, used-by = medicine-healing entry.

Instrument gap (informational, not a row defect): tools/check-row-fragments.py ENTRY constant is still the round-65/66 games entry, so it flags every r67 row `used-by` — including mine — and sibling rows S829-S832 (rejects) and S818 (teaches 242>240) show real findings for the L1 to weigh.

Hosts contributed: www.nlm.nih.gov, pmc.ncbi.nlm.nih.gov (distinct).

Tooling: no installs needed (curl, python3 already present).

Confidence: high on both rows; both sources are official body (NLM) and peer-reviewed CDC journal (EID) — tier A.

Report: .ufo/waves/round-67/rows/ScoutRow08/row-S819.txt
Report: .ufo/waves/round-67/rows/ScoutRow08/row-S820.txt
Report: .ufo/waves/round-67/rows/ScoutRow08/rejects.txt
