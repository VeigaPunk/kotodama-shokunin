BREAKS: S640's new line states as fact that the Kerala amulet was folded up to be carried — not in that row's quote or teaches, and the page only says creases indicate the users folded it; S622's revised line still says the bottle "was believed to work," which neither the row nor the page says.

## Data-walk
Axes: (1) narrow / widen / neutral against the row's quote and teaches, (2) whether a changed base line's new wording is in that quote or teaches, (3) a proposition now carried twice, (4) whether the page carries the new claim (support-kill test). The r59 entry and `main:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` are the same bytes (`4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d`), so the two diffs are the same hunks. Candidate sha256 `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` equals the dirty working-tree entry. Rows read from the dirty `corpus/SOURCES.md` (anchor = quote, next cell = teaches). No installs.

| line | id | change | vs row quote | in quote or teaches? |
|---|---|---|---|---|
| 38 | S600 | old "Egyptology reserves the word for adornments of unambiguous religious character" to "in Egyptology the word amulet is generally reserved for bodily adornments of unambiguous religious form or context" | narrows (drops the "character" gloss) | NO. Quote is only the armour sentence. Teaches is only worn-protection-by-association. Page (Wayback 20141126174231, 11240 B) has "is therefore generally reserved"; the entry drops "therefore". |
| table, infertility row | S640 | "guarded a woman against" to "was used to guard against both" | narrows | YES. Quote: "was used to guard against both infertility and infant death." |
| 58 | S648 | NEW, not a base line | narrows vs rejected S602 (no "because") | YES. Equals teaches after `supersedes S602 —`. Quote locates in `L1/captures/S648.bin`. |
| 60 | S605 | "worked" / "the same apotropaic eyes" to "was used" / "eyes appear as a common apotropaic device" | narrows | YES. Plague clause is the quote; "common device on ships" is the teaches. |
| 67 | S641 | "names ... as those most at risk" to "says ... are believed to be most at risk" | narrows the modality | NO. Not in the quote or the teaches. The Pitt Rivers page does say "are believed to be most at risk." |
| 70 | S651 | NEW | narrows vs rejected S643 (no shell-versus-contents contrast) | YES. Equals teaches after `supersedes S643 —`. Capture: "This amulet case or ga'u of silver and coral, was used to hold rolled prayers ... from evil." |
| 73 | S632 | adds "while others can only be activated by reading the text written on them" | widens past the row | NO. Anchor and teaches stop at "worn or placed." The clause is the next words of the same PMC12701302 sentence. |
| 82 | S649 | NEW. "The Met's record says " plus the hematite sentence. Marked **C** on a tier-A row. | narrows vs rejected S616 (no material-versus-carving "because") | Sentence YES (quote and teaches). The Met frame is not in the quote or the teaches. Capture has the hematite sentence. |
| 83 | S637 | drops "which makes the stone itself the protective agent" | narrows | YES. Remainder tracks the iaspis quote. |
| 85 | S636 | "joining ... Greek Agathodaimon" to "associated with both ... the Greek god Agathodaimon" | narrows | YES. Those words are the quote. |
| 87 | S607 | shine line rewritten to the quote, including "In some times and places" and "meant to" | narrows | YES. Verbatim quote. |
| 99 | S610 | **C** to **B**; prose unchanged | neutral | Prose unchanged. Row tier is B. |
| 103 | S650 | NEW | narrows vs rejected S623 (not the worn-shoe theory as fact) | PARTLY. Apotropaic fragment is the quote. "good luck and hope" is in the teaches only. "remains a mystery" is in neither cell; it is a separate body sentence in `S650.bin`. |
| 104 | S622 | "worked on the witch it stood for" to "was believed to work on the witch whose bladder it stood for" | hedge and bladder narrow; "work" does not | NO for "work". Quote: symbolised the bladder; sharp objects "were believed to cause her much pain." Teaches: "stood for" / "meant to hurt." Page (museum.wales/blog/1203, 88910 B) has that sentence and "sealed", and neither "work" nor "stood for". |
| 106 | S634 | plural scrolls / "armed angels" to "an Ethiopian amulet scroll" / "images of armed angels" | narrows | YES. Quote has "images of armed angels" and the leather-case clause. |
| 108 | S640 | cradle/neck split to "was folded up so that it was small enough to carry around or hold onto" plus the guard clause | widens | NO for the fold. Guard clause is the quote. Teaches has no folding. Page: "These creases indicate that the person or people who used the amulet folded it up so that it was small enough to carry around or hold onto." |
| 109 | S632 | same reading-only clause added to the placement line | widens past the row | NO. Same as line 73. |
| 118 | S634 | "scrolls are inscribed" to "an Ethiopian amulet scroll is inscribed" | narrows | YES. "images of" is in the quote. |

Frozen OLD_PHRASES (`accept-d.py` 102-106) do not occur in the candidate. S602, S616, S623 and S643 are not cited.

## Flagged base lines
New wording not in the row's quote or teaches: S600 line 38 (page-true except dropped "therefore"); S641 line 67 (page-true); S632 lines 73 and 109 (page-true continuation the anchor cut); S622 line 104 ("work", not on the page); S640 line 108 (fold stated as fact).

## Carried twice
- S632 reading-only activation, lines 73 and 109. New double. The page says it once.
- S607 shine sentence: line 66 was already the quote; line 87 now copies it.
- S640 "guard against both infertility and infant death": the danger-table cell, unchanged line 59, and line 108. The fold claim is only on 108.
- S634 prayers / talismans / images of armed angels: lines 106 and 118. Line 106 newly gained "images of".
- S622 bladder: already on line 72; line 104 now repeats it and adds unsupported "work".

## Support-kill reading
One NOT-SUPPORTED on any cited id fails ACCEPT-D-60. The lines a blind seat can refuse from the page are S640 line 108 (an inference stated as fact) and S622 line 104 ("was believed to work"). S648 and S651 match their teaches cells and the captures. S649 adds only an attribution frame around the quote. S650's mystery sentence is outside the row but present in the capture. The other edits are narrowings or page-true completions.

## Confidence
High on the diffs, the row cells, and the pages fetched this run (S600 Wayback, S622, S632, S640, S641, and L1 captures S648-S651). No remaining unknown on the changed lines.