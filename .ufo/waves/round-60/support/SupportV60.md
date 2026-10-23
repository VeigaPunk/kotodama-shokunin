# SupportV60 — blind source review (Round 60 attempt 3, wave 2)

VERDICT P01 NOT-SUPPORTED — (1) fails: the page (V&A API record O79276) body text reads "Silver amulet holders, often containing symbolic material or a piece of paper with a magical or holy inscription, were worn throughout the Muslim world."; the word "folklore" appears nowhere on the page, so the packet quote "folklore amulet holders, …" is not verbatim body text. (3) also fails: the entry claim "tälsäm boxes were strung as a necklace" appears nowhere (no "tälsäm", "tilsam" or "necklace" in the record; the case "may have been worn on the upper arm").

VERDICT P02 NOT-SUPPORTED — (1) and (2) hold: "Silver amulet holders, often containing symbolic material or a piece of paper with a magical or holy inscription, were worn throughout the Muslim world." is verbatim in the record's summaryDescription and carries the teaches. (3) fails: the entry claim "tälsäm boxes were strung as a necklace" is not carried — the page never mentions tälsäm/tilsam or necklace (summaryDescription says the case "may have been worn on the upper arm, fastened by straps which would have passed through the loops at either side").

VERDICT P03 SUPPORTED — "This artefact is the first and so far only find of its kind in a Polish context." quote verbatim in the article's body (abstract of "Christian textual amulet on a lead sheet from Rękawczyn"); the packet quote "Other amulets do not cite the Gospels but use an apotropaic adjuration formula by which they banish evil spirits and diseases." appears verbatim in body text; the teaches is carried (textual amulets that do not cite the Gospels but use an adjuration formula to banish evil spirits and diseases); both entry claims are carried by the same sentences.

VERDICT P04 SUPPORTED — "They are usually found at the thresholds of buildings to prevent witches and evil spirits from entering, thus protecting inhabitants and visitors from harm." quote verbatim in body text of the exhibitions page; the packet quote "Witches' marks were a common form of ritual protection in which symbols or patterns were carved into the stonework or woodwork of historic buildings." appears verbatim (curly apostrophe); the teaches and the single entry claim are carried.

VERDICT P05 SUPPORTED — "On one side is a representation of the demon surrounded by various ritual paraphernalia (fig. 1), and on the other, a ritual incantation carved in cuneiform script (fig. 2)." quote verbatim in the article body (Miriam Said, "Radiance and the Power of Erasure in an Obsidian Lamaštu Amulet"); the packet quote "This amulet, small enough to fit in the palm of one's hand, provides protection from the Mesopotamian demon Lamaštu." appears verbatim; the teaches and both entry claims (palm-sized protective object against Lamashtu) are carried.

VERDICT P06 SUPPORTED — "It was acquired in India by William Tayler who sold it to this museum in 1874." quote verbatim in body text of the V&A collections page; the packet quote "This amulet was made to protect the wearer from harm or misfortune and has been fashioned in white nephrite jade." appears verbatim; the teaches is carried; the entry's "Mughal" claim is carried by the page's Brief description ("… white nephrite jade, Persian inscription, Mughal empire").

VERDICT P07 NOT-SUPPORTED — (1) holds: "The bottom of the talisman is sharp so it can be fitted onto the door." is verbatim body text of the Sinica item page ("Wooden Talismans"). (2) and (3) fail: the page says only that the Han used these talismans "to avoid evil spirits and hexes"; neither the teaches nor the entry claims appear — "frontal face", "plague", "apotropaic eyes" and "ships" all have zero occurrences anywhere on the page.

VERDICT P08 SUPPORTED — "Hence, evil eye belief is commonly accepted by every segment of society whether educated or not." quote verbatim in the thesis body; the packet quote "As the result of naturalization of myth, evil eye bead has a pervasive usage as souvenir in Turkey." appears verbatim; the teaches and the single entry claim are carried.

URLs opened (all via curl, live fetches; no archives needed):
- https://api.vam.ac.uk/v2/museumobject/O79276 — HTTP 200, 4909 bytes
- https://journals.iaepan.pl/sa/article/download/2498/2871 — HTTP 200, 9410020 bytes
- https://www.provanhall.org/exhibitions — HTTP 200, 229010 bytes
- https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf — HTTP 200, 16579613 bytes
- https://collections.vam.ac.uk/item/O472426/amulet/ — HTTP 200, 47986 bytes
- https://museum.sinica.edu.tw/en/collection/20/item/36/ — HTTP 200, 55323 bytes
- https://openaccess.iku.edu.tr/bitstreams/8b0b8456-e29b-4568-b622-5859e4029189/download — HTTP 200, 12295670 bytes

Tooling: no installs performed (curl, pdftotext, python3 -B with PYTHONDONTWRITEBYTECODE=1 already present); every process capped with `timeout`; all work under /tmp/SupportV60.
