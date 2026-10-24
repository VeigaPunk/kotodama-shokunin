# RevAuditE — chain rulings S484>S385, S485>S392, S486>S395, S487>S396 (claim O residual)

Artifact: `.ufo/waves/round-68/rows/RevAuditE/audit.md`. All four rulings are **activate | repoint** against the sole citing file `corpus/knowledge/civilizations/kongo-kingdom.md`; all re-verified live on 2026-10-24. Two carry conditions the L1 should apply at landing.

## Findings by severity

- **Moderate — S485 anchor regression (repair at landing).** S485's p.22 and p.24 anchors store straight apostrophes (`Mbânz'a`, U+0027, byte-verified at `corpus/SOURCES.md:488`) where the served PDF prints `Mbânz’a` (U+2019) — S392's anchors are verbatim-correct. This is the same defect class S484 was filed to fix in S385. Ruling is still **activate**: the scope correction ("execution in 1706 vs the movement's disputed end — after 1719 in Batsîkama, 1712 in the Randels block") is verbatim-supported by the served PDF (985,805 bytes, HTTP 200) and all four citing locators carry. Landing repair: two bytes in S485's anchor cell. If the integrator prefers zero-mutation landing, retire-and-refile is the alternative, but it leaves S392's conflated scope live.
- **Minor — S484 drops two live anchors (recommend restoring).** S484 removes the p.61-note-5 and p.63-note-8 anchors S385 carried; the p.61 anchor is directly cited at `kongo-kingdom.md:93`. The cited claims remain on-scope and the sentences are verbatim in the served PDF — restoring the two anchors into S484's cell at landing is a pure cell edit. Not grounds for retirement.
- **Minor — S484's access note is stale.** Its stated basis (Anubis JS challenge on the live OpenEdition PDF) no longer holds: a plain GET today returns HTTP 200, `application/pdf`, 492,733 bytes — the exact bytes S385 recorded. The recorded Wayback copy (303,987 bytes) is a smaller re-encoded same-identity PDF; all four S484 anchors verified verbatim in it. Harmless, but the note overstates.
- **Informational — S487 replay-size variance.** Recorded 54,094 bytes vs 204,151 served for the same capture id — same class of variance falsify already logged for Met captures; content unaffected, all four anchors verbatim in order, third-paragraph locator confirmed.

## Verification performed

- S484: `web.archive.org/web/20240327164523id_/…/assr/pdf/2480` → HTTP 200, PDF, 303,987 bytes (byte-exact to record); pdftotext: all 4 anchors verbatim incl. restored `qu’une`/`l’attention` and the new `Tous les rituels…ont disparu` anchor that grounds the previously unanchored royal-rites clause.
- S485: live USP PDF → HTTP 200, 985,805 bytes (byte-exact); anchors 2/3 verbatim under U+2019; `só cessou depois de 1719` and `(quer dizer, em 1712)` verified — scope fix supported.
- S486: `web.archive.org/web/20230308010409id_/…/search/320053` → HTTP 200, 209,131 bytes (matches record); all 4 anchors verbatim; title block/Culture field carry `Kongo artist and nganga, Yombe group`, Date `Second half of the 19th century`, Geography `Chiloango River`, accession `2008.30` — fixes S395's wrong-locator (its 2021 capture had no artist credit).
- S487: `web.archive.org/web/20230529091312id_/…/search/312342` → HTTP 200; all 4 anchors verbatim in served order; the `Knots and the act of tying…` sentence sits in the third paragraph block, matching the falsify wrong-locator finding S487 repairs.
- Census: only `kongo-kingdom.md` cites any of the four targets (lines 16, 85, 89, 90, 93, 113, 121); lessons files mention ids as history only. Canonical identity preserved on all four chains (same journal PDF / same USP PDF / same metmuseum.org object ids; only capture routes updated where needed).

## Residual risk

The three other chains in this supersession block (S481-S483, S488-S491) and the remaining pending chains belong to other seats. S485's anchor bytes and S484's dropped anchors are integrator-landing decisions; both are documented in the audit rows. No registry or entry edits were made; this seat ruled only.

No tools installed; system curl/pdftotext/python3 only. pacman untouched.
