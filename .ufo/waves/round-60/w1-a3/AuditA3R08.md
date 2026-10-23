# AuditA3R08 — BUILD ATTACK pre-freeze wording audit, ids S625 S626 S627

Scope: entry `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md`, SOURCES rows grepped at
`corpus/SOURCES.md` (S625 line 580, S626 line 581, S627 line 582). Pages re-fetched by ordinary
means, first URL literal, from `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R08/` on 2026-10-23.
None of S625–S627 is among the round-59 rejected ids, so the S648–S651 section-3 comparison is
not applicable to this batch. No installs used (curl, pdftotext, python3 already present).

## AUDIT S625 REWRITE

Entry line 137: `Return after use: omamori, the lucky charms available at shrines, are usually returned once they have served their purpose or after about a year (S625).`

Fetch: `curl 'https://www.mlit.go.jp/tagengo-db/en/H30-00525.html'` → HTTP 200, 17,999 bytes (matches row).
Quote located verbatim as body text (the interpretive sign's English text, not nav/caption):
"Omamori , the lucky charms available at shrines, are usually returned once they have served their purpose, or if they are more than a year old."
Teaches cell carried by the same paragraph: "shrines set up boxes such as this one for believers to return their omamori , household ofuda (amulets), and decorative arrows. Returned items are then burned in a sacred fire."

Carried clauses: "lucky charms available at shrines", "usually returned", "once they have served
their purpose" — all verbatim. Defect: the page's second trigger is the threshold "more than a year
old"; the line paraphrases it as "after about a year", which reads as an approximate age rather than
the stated cutoff. A strictly literal seat could call it an added approximation. Minimal narrowing
the page carries, keeping structure and the id:

old: `- Return after use: omamori, the lucky charms available at shrines, are usually returned once they have served their purpose or after about a year (S625). **B**`
new: `- Return after use: omamori, the lucky charms available at shrines, are usually returned once they have served their purpose or if they are more than a year old (S625). **B**`

(The teaches cell's own "after roughly a year" is looser than the page's "more than a year old" but
is not independently over-reaching — the line fix above removes the only clause a seat could flag;
no TEACHES verdict.)

## AUDIT S626 OK

Entry line 53 (danger-to-remedy table, single id): `| demons that cause ailments | a Tang-dynasty method aimed to identify the demons that caused ailments and expel them through sacrifices, incantations, talismans and other exorcistic rituals | S626 (B) |`

Fetch: `curl -L 'https://dao.crs.cuhk.edu.hk/Main/wp-content/uploads/2025/02/DAO1516_04.pdf'` → HTTP 200, 2,439,068 bytes (matches row). `pdftotext -layout` locates the row quote verbatim on printed p. 127, body paragraph, not a caption: "Iatromancy (busui 卜祟) was a method of divination and related techniques used to diagnose and treat illnesses. This method aimed to identify the demons that caused the ailments and expel them through sacrifices, incantations, talismans, and other exorcistic rituals." (quote differs only by the dropped "the"/Oxford comma, both within verbatim tolerance of a normalized extract).

Carried clauses: "Tang-dynasty" — the same paragraph says "Many iatromantic writings of the Tang
dynasty were discovered in Dunhuang" and the article is a Tang-dynasty treatment; "identify the
demons that caused ailments" and "expel them through sacrifices, incantations, talismans and other
exorcistic rituals" — verbatim. The line adds no comparison, universal, cause, date or place beyond
the paragraph. Teaches cell matches the page.

## AUDIT S627 OK

Entry line 97: `- Door: a Han-period wooden talisman from Edsen-gol has a sharp bottom so that the talisman can be fitted onto the door (S627). **B**`

Fetch: `curl -L 'https://museum.sinica.edu.tw/en/collection/20/item/36/'` → HTTP 200, 55,323 bytes (matches row). Quote located verbatim in the collection-item description (body field, under the "Wooden Talismans" heading; the sentence itself is descriptive text, not a heading or caption fragment): "The Han used these ferocious looking talismans to avoid evil spirits and hexes. The bottom of the talisman is sharp so it can be fitted onto the door."

Carried clauses: "Han-period" — record field "Period Han dynasty (206 B.C.-A.D.220)"; "wooden
talisman" — record title "Wooden Talismans"; "Edsen-gol" — findspot "Edsen-gol" (sites A35
Taralingin-durbeljin, A21/A22 Bukhen-torei, P9 Borotsonch) under collection "Han Dynasty Wooden
Slips from Edsen-gol"; "sharp bottom … fitted onto the door" — verbatim. Singular "a … talisman"
fits the record's own generic singular ("the talisman is sharp"). No added claim. Teaches cell
(evil-spirits purpose + sharp base for door fitting) matches the page exactly.

## Summary

- S625: REWRITE — one clause ("after about a year") softened from the page's threshold "more than a
  year old"; replacement above keeps id, structure, and adds nothing.
- S626: OK — every clause verbatim-supported on p. 127, no over-reach.
- S627: OK — every clause verbatim/field-supported, no over-reach.
- No heading/caption/promo/cookie/nav quote flagged among the three rows.
