# Falsify report — Claim D, line 121 (section 7, "court and royal office" row)

Seat: KotodamaR53.ReviewDLines121 · 2026-10-22 · lane /home/vgpnk/Projects/shokunin/kotodama-shokunin
Scope: lines 115-127 of `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`; the only line D's diff changes in this range is line 121 (hunk `@@ -118,7 +118,7 @@`). Rows re-opened: S164, S165, S166.

## Verdict

**No defect found in the landed repair of line 121.** Every clause on the changed line now says only what its cited row's page carries; both quotes are verbatim; the former over-read is gone and no supported detail was dropped.

## Item attacked

Landed line 121 (was, at base a9cf95f: "in Akan (Ghana) practice a master drummer is "appointed Royal Court Drummer to the high chief of the Aburi-Akuapim" at seventeen (S165), and Aburi-Akuapem court drummers are described as resisting change of repertoire (S166)").

Three clauses, three cited rows:

1. Yorùbá hereditary titles and patronage — S164 (clause unchanged by the repair).
2. Ghana appointment quote — S165 (repaired: paraphrase generalized to "Akan practice" replaced by the sourced biography quote).
3. Aburi drummers' attitude to change — S166 (repaired: half-paraphrase "resisting change of repertoire" replaced by the full abstract sentence).

## Checks run

- `git diff a9cf95fe47a82b516f6c2487cb76b89c3a71c493 374ae5a4e4376049e45a7f597e740d09bf94cbc4 -- corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` — one hunk in range; only line 121 changed.
- `git show a9cf95f...:corpus/SOURCES.md | grep 'S16[456]'` — rows S164 (line 193), S165 (194), S166 (195) existed at base; D lands only the entry file, rows untouched.
- `python3 -B reports/round-53/d-count.py` → `OPEN 0 / SID_BAD 0 [] cited 50`, exit 0. Line 121 cites S164/S165/S166 only — no S187+ id (claim's must-not-cite respected), no draft-id fragment, no `(to-verify)` needed.
- S164 — opened https://international.ucla.edu/africa/article/113707 (curl, 52,125 bytes). Body ¶ "Of particular importance is the talking drum's connection to Yorùbá sacred-kingship": "Drumming families that carry the hereditary title of baale or aare onilu (chief drummer) maintain generations-old patronage relationships with families of Yorùbá obas (sacred kings)" (24 words). og:description: "went to southwestern Nigeria". The entry clause is a faithful compression; titles, hereditary carriage, patronage, oba = sacred kings all carried.
- S165 — opened https://music.brown.edu/music-making/ensembles/ghanaian-drumming. About section, biographical paragraph on Kwaku Kwaakye (Martin) Obeng: "by seventeen he was appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region of Eastern Ghana" (19 words; entry quote ends at "region"). **Verbatim match.** The new frame "one master drummer's biography says" is exact — it is one man's bio, and the row itself warns "the page supports the appointment and the course, not the wider Akan institution".
- S166 — live https://www.ideals.illinois.edu/items/87159 returned HTTP 403 to a plain request; no challenge passed. Ordinary copy used instead: Wayback Machine raw replay (`web.archive.org/web/2id_/https://www.ideals.illinois.edu/items/87159`); CDX lists 200-status captures from 20240612235603; the captured page is titled "Rhythms of Power: Royal Drumming in Aburi -Akuapem, Ghana", item 87159. Abstract, Chapter III sentence: "displayed by Aburi court drummers, who fiercely resist change in repertoire and performance practice" ... "yet accept it in the realm of performance context". **Verbatim match** with the entry's quote; the frame "are described as people" matches the abstract's relative-clause syntax. Full text is marked members-only on the page and was not opened, as the row's scope states.
- Section status line (line 126, unchanged, in range): "tiers B, and A for the ministry record" — consistent with SOURCES.md: S170 is tier B, S171 (Spain Ministerio de Cultura) is tier A.

## Findings

**High:** none. **Medium:** none. **Low:** none.

Notes on the repair quality (not defects):

- The base S166 paraphrase "resisting change of repertoire" was a half-statement: the abstract's point is that the drummers resist repertoire change *yet accept* context change. The landed quote restores the counterweight — the repair strengthens fidelity, it does not weaken a claim.
- No supported detail was dropped by the S165 repair: age (seventeen), title (Royal Court Drummer), patron (high chief), region (Aburi-Akuapim) are all inside the verbatim quote; only the false generalization "in Akan (Ghana) practice" was removed.

## Residual risk and verification gaps

- The exact timestamp of the raw Wayback replay used for S166 was not echoed by the fetch; identity is pinned by the captured title/item number and the CDX capture list (all HTTP 200). The abstract sentence matched character for character, so the risk is negligible.
- Unchanged rows in lines 115-127 (citing S164, S167-S171) predate this repair and were not re-opened here; per scope I attacked the changed line only.
- Access note: IDEALS served 403 to an ordinary request — challenge met, not passed; routed around with a public Wayback capture only.
