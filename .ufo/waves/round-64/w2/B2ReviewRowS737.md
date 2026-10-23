# B2ReviewRowS737 — row falsification report

Draft reviewed: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS737/row.txt` (wave-1 inheritance, unverified).
Full verdict table: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ReviewRowS737/review.md`.

## HTTP results (verbatim)

- Live: `200 https://eric.ed.gov/?id=ED149852` (`curl -sL --max-time 90`)
- Capture: `200 https://web.archive.org/web/20250426225743id_/https://eric.ed.gov/?id=ED149852` (first attempt `000`/exit 7 transient; retry 200)
- Availability API: `{"timestamp": "20250426225743", "status": "200", "available": true}` — same-page capture, original matches live URL.
- Lane locator (`reports/round-61/reopen-quote.py`): attempt 1 `NOT_LOCATED ... ConnectionResetError` (transient), attempt 2 `LOCATED https://eric.ed.gov/?id=ED149852`.

## Findings

Row cells verify clean: 11 cells; citation author `Schwartz, Judy I.`, year `1977-Apr`, title `Metalinguistic Awareness: A Study of Verbal Play in Young Children.` all match the ERIC record (`Accession Number: ED149852`, `Record Type: Non-Journal`); tier A justified for the exactly-scoped "operational definition of verbal play in Schwartz's study" (the study's own official record); anchor quote verbatim in body text of both live page and capture (25 normalized words, within 8–25); `mined`/`2026-10-23`/`180d`/used-by entry path all correct.

**Defect (required fix) — BULLET overreach:** `- Children's verbal play makes sound, semantics, and syntax available as material for playful worldbuilding (S737)`. The quote establishes only the operational definition — verbal play *is* an observable manipulation of "the sound, semantics and/or syntax of the language". `"worldbuilding"` asserts a downstream outcome the source never claims and appears nowhere in the quote, abstract, or record. Mechanically RESTATE-safe (11 content words, 5 in-order quote words, copy-run 3), so the counter will not catch it — the clause still misstates support.

Required fix: rewrite the clause to assert only what the quote establishes, e.g. `- Children's verbal play is an observable manipulation of sound, semantics and syntax, treating language itself as material (S737)` (keeps ≥5 content words, ≥3 in-order quote words, a novel content word, no >12 copied run).

Minor residual (no fix required): teaches cell generalizes "young children" → "Learners … practice noticing language structure … in playful verbal experiments" — mild extrapolation, not counter-checked. Draft's ACCESS note "linked full-text PDF attempt returned HTTP 404" could not be reproduced (no PDF link on the record); immaterial.

VERDICT: FIX-REQUIRED BULLET overreaches the quote — invented "worldbuilding" outcome not established by the source; all other fields verified clean.

Tooling: no installs or updates performed (curl/python3 already present); PACMAN GUARD observed.
