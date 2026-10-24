# RevAuditD — report (round 68 residual, claim O chain audit)

Seat: L1-kotodama-r68-attempt2.RevAuditD. Full rulings with CITE=/EVIDENCE=/ANCHOR= lines: `.ufo/waves/round-68/rows/RevAuditD/audit.md`. Verified 2026-10-24 by live re-open of all four s URLs. No registry or entry files touched; no git/jj writes; no tool installs needed (curl, python3, pdftotext already present and used as-is).

## Rulings — all four chains: activate, repoint

| chain | target used-by | correction substance | verified against served source |
|---|---|---|---|
| S358>S256 | masks-masquerade.md | tier A->B (register's condensed summary) | live page HTTP 200, 211,091 B = S358's declared count; all 9 stored spans verbatim; tier basis is the round-55-prescribed correction |
| S481>S359 | kongo-kingdom.md | printed-page locators 469/489 -> 470/490 | djvu.xml page tails: q1/q2 on obj 531 = printed 470, q3/q4 on obj 551 = printed 490; doc opens on 468/488 |
| S482>S367 | kongo-kingdom.md | teaches hedge: founding descent kept as reported claim | served sentence prints "uma parte que reclama ser fundadora…"; anchors byte-identical, pp. 174/173 confirmed |
| S483>S383 | kongo-kingdom.md | teaches agency: "royal control" -> "its control" | served abstract contains zero "royal control"; "its control over the Church organization and finance" verbatim; anchors byte-identical |

Key structural finding: the two kongo citing sentences (:82 "Kongo's control", :18/:110/:140/:146 pp. 470/490) were already written against the corrected rows, so S481/S483 repoint with zero entry edits; masks :62/:86/:89 repoint with zero sentence fixes, :86's two claims carried by S358's scope cell (which names "the shrine-to-courtyard order, the two registers of the dance") — the same scope-carry route as the AuditChain8 S568 ruling.

## Residual risk

- S358's anchors 3–4 truncate served sentences mid-span (served ¶2 sentences 2–3 each continue past the stored quotes; the stored halves are verbatim prefixes) and its cross-paragraph "s" numbering is cosmetic-wrong. Anchor cells are outside the frozen MUTABLE set, so this lands with the row; a future superseding row or an anchor erratum (round-55 `b9c44a2` route) can repair. Does not block activation: the tier defect it repairs is worse and was adjudicated in round-55, and every stored word is served verbatim.
- W04 duplicate-URL warnings on S358/S482/S483 remain by design (superseding rows re-use the target URL); S481 is unflagged (same-scope re-use). Census noise, not contract noise.

## Verification gaps

- Brásio printed-page numbers were recovered from OCR page tails with letter substitutions ("* 7 °" = 470, "49°" = 490); the mapping is unambiguous (docs 142/147 open at 468/488, printed sequence increments by one per object) but the raw tokens are OCR, not clean type.
- Thornton byte count differs by 1 byte from S383's declared 1,158,765 (same capture replayed, 1,158,764) — trivial replay drift, recorded not acted on.
- S256's declared 210,913 B vs live 211,091 B (same URL): un-investigated 178-byte drift on the 2026-10-22 measurement; all stored spans serve verbatim today, so not ruling-relevant.
