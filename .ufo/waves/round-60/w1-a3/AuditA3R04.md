# AuditA3R04 — pre-freeze wording audit, ids S611, S612, S613
Lane: kotodama-shokunin, round 60 attempt 3, wave 1. Candidate: /fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md (uncommitted build). SOURCES rows read at the working tree. Pages re-opened 2026-10-23 by ordinary curl (plain requests only); quotes scored with the lane locator `reports/round-60/reopen-quote.py` (`to_text`/`locate_in`, copied to my sandbox, unmodified originals). Saved bytes under /fast/scratch/hyaku/kotodama-r60a3/AuditA3R04/ (s611.html, s612.json, s613.html).

Round-59 rejection cross-check (lesson section 3, S602/S616/S623/S643): none of the four rejected ids maps to S611/S612/S613, so no "over-reach reworded" question applies to my ids.

## AUDIT S611 OK
- Line (candidate-entry.md:117): `- Image and inscription: a printed childbirth amulet frames its main panel with images of the zodiac around an inscription banishing the demon Lilith (S611). **B**` (only line citing S611).
- Page: https://www.posenlibrary.com/entry/amulet-woman-childbirth-germany — HTTP 200, 105,290 bytes text/html live (row recorded 15,932 at mining time; live shell is heavier today, but the description body is present and verbatim). Quote located by lane locator: True.
- Page sentence carrying each clause (object description paragraph, body text, not heading/nav/cookie):
  - "printed ... childbirth": "This early printed amulet from Germany, meant as protection for a woman in childbirth, is adorned with woodcuts illustrating the Hebrew months of the year." — located True.
  - "main panel ... framed ... zodiac ... inscription banishing the demon Lilith": "The main panel, framed by images of the zodiac, features an inscription banishing the demon Lilith, who, according to folklore, was Adam’s first wife." — located True.
  - Support for "printed": also "Amulet printed on parchment from Germany." — located True.
- Every entry clause is carried; no universal, no added cause/date/place; row quote is the entry's description body. No defect.

## AUDIT S612 REWRITE
Lines citing S612 (three): candidate-entry.md:69, :95, :120.
- Page: https://api.vam.ac.uk/v2/museumobject/O79276 — HTTP 200, 4,909 bytes JSON, byte-identical to the row's recorded size. Verbatim summaryDescription (located True): "Silver amulet holders, often containing symbolic material or a piece of paper with a magical or holy inscription, were worn throughout the Muslim world." plus "They were believed to protect the wearer from all kinds of physical and spiritual dangers." and "It may have been worn on the upper arm, fastened by straps which would have passed through the loops at either side."
- L69 `Containment in silver: silver amulet holders, often containing symbolic material or a paper with a magical or holy inscription, were worn throughout the Muslim world (S612).` — OK: mirrors the page sentence with "often" kept; only "a piece of" dropped. No over-reach.
- L120 `Holy text in a case: a silver amulet holder could contain a paper with a magical or holy inscription (S612).` — OK: "could contain" is carried by "often containing symbolic material or a piece of paper with a magical or holy inscription"; possibility claim, no quantifier added.
- L95 S612 half — DEFECT (quantifier/hedge drop): `silver amulet holders containing a paper with a holy inscription were worn throughout the Muslim world` deletes the page's own "often" and "magical or", turning "often containing symbolic material OR a piece of paper with a magical or holy inscription" into a bare property of the worn class. A strict blind seat can bounce this as a claim the page does not carry (the page quantifies "often" over the disjunction, not over the paper-with-holy-inscription subtype). Minimal fix now, keeping line structure and the id:
  - old: `- Arm and neck: silver amulet holders containing a paper with a holy inscription were worn throughout the Muslim world (S612); tälsäm boxes were strung as a necklace (S613). **B**`
  - new: `- Arm and neck: silver amulet holders, often containing symbolic material or a paper with a magical or holy inscription, were worn throughout the Muslim world (S612); tälsäm boxes were strung as a necklace (S613). **B**`
  (Section heading "Arm and neck" is independently supported: V&A "It may have been worn on the upper arm..."; "neck" rests on S613, see below.)
- Teaches cell carried: held ("symbolic material or a piece of paper with a magical or holy inscription"), carried on the body ("worn on the upper arm"), guarded against ("physical and spiritual dangers") — all located True. No TEACHES issue.

## AUDIT S613 OK
Lines citing S613 (two): candidate-entry.md:71 and :95 (second half).
- Page: https://www.clevelandart.org/art/2025.152 — HTTP 200, 84,820 bytes text/html, matching the row's recorded size exactly. Curatorial description located True; note the CMS ships the inner `<em>` around "tälsäm" as escaped markup (`(&lt;em&gt;tälsäm)&lt;/em&gt;`), which renders as plain "(tälsäm)" — the locator strips it and locates the row quote.
- L71 `Many containers: a silver necklace of numerous box-shaped amulet pendants (tälsäm) was meant to ward off the evil eye or other dangers (S613). **B**` — OK: verbatim carried by "This silver necklace is composed of numerous box-shaped amulet pendants (tälsäm) meant to ward off the evil eye or other dangers." (description paragraph, body text).
- L95 S613 half `tälsäm boxes were strung as a necklace (S613)` — OK: the page's object is titled "Necklace (ashän ketab) with amulet pendants (tälsäm)" and the description says the necklace "is composed of numerous box-shaped amulet pendants (tälsäm)" — the boxes form the necklace, i.e. strung as one; no added cause/place/comparison.
- Corroborating body sentence also locates True: "Linked to Islamic amuletic practices, the boxes are effective whether empty or whether they contain magical or prayerful texts." (not cited by the entry lines; no conflict).
- Teaches cell carried (box pendants, evil eye, filigree work "characteristic of Harar", thaler silver "melting high-purity Maria Theresa thaler coins"). No TEACHES issue.

## Residual notes
- No quote among the three is a heading, caption fragment, promo, cookie or navigation text: S611 = object description paragraph; S612 = API summaryDescription field; S613 = curatorial description paragraph.
- S611 live byte count (105,290) differs from the row's recorded 15,932; quote and surrounding description verbatim on the live page, so no refresh of the row's capture facts is required, but the L1 may note the drift.
- If the L1 takes the S612 L95 rewrite, nothing else in the candidate entry changes for my ids.
