# Quote receipt — marriage-alliance-bridewealth.md

Seat `ScribeEntry-2` (owner of `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`).
Every quotation in `## 3. Attested anchors` was matched against the folded read of the exact page
the binding receipt at `.ufo/waves/round-83/w1/stage/ScribeRows/S9xx.txt` names. Folded read, per
the rows seat's definition: drop script/style/comments; every other tag becomes one space; entities
decoded; U+00A0 and U+2003 to space; every whitespace run to one space. Plain-text sources are
whitespace-collapsed only.

| row | page fetched | bytes | sha256 (decoded) |
|---|---|---|---|
| S909 | https://avalon.law.yale.edu/ancient/hamcode.asp | 74531 | 93410a95441d28fd498df423ec7860ae5ee821df3811989bb469838075c9eb12 |
| S910 | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Marriage | 147040 | 79faf53312fc7a8abcad5685004520ea01c460b95ce65962e75d4b6293d050df |
| S911 | https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85 | 70655 | 4d4737d7a06da9a21c17457a412ebc44c702ae0a4b26c707294bc29c70058a29 |
| S912 | https://www.gutenberg.org/cache/epub/10/pg10.txt | 4455950 | 0204adaed1f25700aa854218cae63c7172228c41088f335e99167a071eed83c0 |
| S904 | https://www.gutenberg.org/cache/epub/1727/pg1727.txt | 717782 | (byte count matches the S904 row) |
| S905 | https://en.wikisource.org/wiki/Germania_(Church_%26_Brodribb) | 163266 | (byte count matches the S905 row) |

Result at final state: **57 quotations checked, 0 not located**. The S904 and S905 digests were not
recorded in their round-82 rows at first read; only their byte counts were compared here.

## Deviations found and how they were resolved

The rows seat measured five deviations against its folded reads. One was a real transcription
divergence and four were normalisation classes:

1. **S911 edition divergence (transcription, not normalisation).** The seat's binding page is the
   Wikisource Griffith (70655 bytes, revision 14397100), where "Surya" occurs 30 times and "Sūrya"
   0 times, and "Pusan" 6 times against "Pūṣan" 0. The seat's receipt binds. All fourteen S911
   quotations in the entry were therefore checked against that page and the two diacritic forms
   were re-pointed to its spelling ("Surya", "Pusan"). No wording differed between the two
   Griffiths transcriptions at the quoted verses.
2. **S909 §164 capitalisation.** Avalon prints `the "Purchase price"` with a capital P inside the
   quotation marks. The entry now quotes the served capitalisation.
3. **S905 hyphenation.** Church and Brodribb print "grand-children" across a source line break.
   The entry quotes a different clean span of the same passage ("what she must hand down to her
   children neither tarnished nor depreciated") and paraphrases the entailment in its own words
   outside the quotation marks.
4. **S910 tag-separator spacing (two spans).** The folded read of the Parsoid page prints
   "confarreatio , coemptio in manum , and usus" and "mancipatio ,", because inline markup becomes
   a separator. The entry quotes only spans that are contiguous in the folded read — "a religious
   ceremony before ten witnesses", "an ox was sacrificed and a wheaten cake broken and divided
   between the spouses by the priest", "might be described as a fictitious sale per aes et
   libram", "on the same footing as the children" — and paraphrases the connecting words outside
   quotation marks. No quotation in the entry now depends on a tag boundary.
5. **S912 glyph.** Gutenberg #10 uses U+2019 in possessives. The entry's Leviticus quotations
   carry U+2019 exactly where the file does.

No absolute working path is recorded in this receipt; only public URLs, byte counts and digests.

## Re-verification at the final state

After the calibration rewrite the six pages were fetched again from the same URLs. Digests were unchanged and
equal to the receipts for all four rows that record one (S909, S910, S911, S912); S904 and S905 matched on byte
count. All **57** `## 3` spans located, **0** did not. Entry size at that state: 56555 bytes.

The L1's integration note listed the same five spans; they were already fixed in the bytes it scanned later, and
the locations were reported back (lines 91, 97, 99, 112, 134).
