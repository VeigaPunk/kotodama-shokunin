# ScoutSouthAsiaProtection — claim C source seat (round 59)

Scope: South Asian protective practices and objects (nazar/nazar battu, ta'wiz-adjacent amulets and
talismans, protective threads, yantras) as material for the amulets/talismans/apotropaic-marks entry.
Two rows offered, ids S630 and S631. Lane /home/vgpnk/Projects/shokunin/kotodama-shokunin, base
39c9ce8a6be5e5625d8befb54df53d621a3a7929; work done 2026-10-23 from
/fast/scratch/hyaku/kotodama-r59/ScoutSouthAsiaProtection/. No files outside the scratch directory
and this report were written; no git/jj write commands; no installs (nothing was needed).

Evidence mode: external pages opened by plain GET (curl, python urllib, the V&A's own JSON API);
no repository code question arose, so no LSP server was used and no grep output is presented as
semantic proof. Every quote below was located in the body of the page/PDF served now by a plain
request (rowcheck LOCATE PASS), and each row was pre-filed against the frozen checker.

## Rows (11 cells each)

| S630 | Victoria and Albert Museum, London, object record 1198-1874, "Amulet", white nephrite jade, engraved on the front face with a Persian inscription surrounded by a border of small cross marks in individual boxes, Mughal empire, 19th century; acquired in India by William Tayler (in India 1829-1867) and sold by him to the South Kensington Museum in 1874. — https://collections.vam.ac.uk/item/O472426/amulet/ (plain GET, HTTP 200, text/html, 47,609 bytes, no challenge, no login; record fields read 2026-10-23) | docs | A | a Mughal protective amulet read through its material and its script — white nephrite jade engraved with a Persian inscription and a border of cross marks, made to protect the wearer | served text: "This amulet was made to protect the wearer from harm or misfortune and has been fashioned in white nephrite jade." | A white jade amulet was made to shield its wearer from harm and misfortune. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S631 | Tahir, Tayabba Batool, "A Discursive Analysis of Religio-cultural Perceptions about Evil Eye among Female Residents of Ghareebabad, Multan", Global Sociological Review VI(II), 2021, pp. 97-103, DOI 10.31703/gsr.2021(VI-II).12. — https://www.gsrjournal.com/pdf/gsr/d6KYBF41pB.pdf (plain GET, HTTP 200, application/pdf, 1,037,920 bytes, 7 pages, text read with pypdf 5.4.0, 2026-10-23); capture https://web.archive.org/web/20260608063258id_/https://www.gsrjournal.com/pdf/gsr/d6KYBF41pB.pdf | paper | B | who supplied protective amulets in a Pakistani town — imams acting as spiritual healers who recommended an evil-eye amulet and talisman | PDF p. 6: "Most commonly, imams are considered as spiritual healers and they suggest evil eye amulet and talisman." | Spiritual healers such as imams advised an evil-eye amulet and talisman as protection for the afflicted. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S630 — https://collections.vam.ac.uk/item/O472426/amulet/ — accessed 2026-10-23 — served text: “This amulet was made to protect the wearer from harm or misfortune and has been fashioned in white nephrite jade.”. Grounds: A white jade amulet was made to shield its wearer from harm and misfortune. Seat: ScoutSouthAsiaProtection.
- S631 — https://www.gsrjournal.com/pdf/gsr/d6KYBF41pB.pdf — accessed 2026-10-23 — PDF p. 6: “Most commonly, imams are considered as spiritual healers and they suggest evil eye amulet and talisman.”. Grounds: Spiritual healers such as imams advised an evil-eye amulet and talisman as protection for the afflicted. Seat: ScoutSouthAsiaProtection.

## rowcheck output (pasted verbatim)

```
S630 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://collections.vam.ac.uk/item/O472426/amulet/ | BOILER: root-clear https://collections.vam.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'harm', 'jade', 'misfo', 'weare', 'white'] | TOPIC: quote_hits=1 function_words=9 page_hits=14 page_terms=11 need=1/2/3/2
S631 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.gsrjournal.com/pdf/gsr/d6KYBF41pB.pdf | BOILER: root-clear https://www.gsrjournal.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'evil', 'heale', 'imam', 'spiri', 'talis'] | TOPIC: quote_hits=2 function_words=3 page_hits=27 page_terms=171 need=1/2/3/2
```

Command: `cd /fast/scratch/hyaku/kotodama-r59/ScoutSouthAsiaProtection && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutSouthAsiaProtection/rows3.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutSouthAsiaProtection/stub3.md` → exit 0.

## Draft entry sentences

S630:

1. A protective amulet could be a white jade pendant made to protect its wearer from harm or misfortune (S630).
2. White nephrite jade was the material of this protective amulet (S630).

S631:

1. An evil eye amulet or talisman could be prescribed by an imam, who served the household as a spiritual healer (S631).
2. For healing and protection, families in Multan visited imams and religious leaders (S631).

(Written to /fast/scratch/hyaku/kotodama-r59/ScoutSouthAsiaProtection/stub3.md and checked with
`--entry`; RELEVANCE (c) and (d) PASS for both rows.)

## Rejected / opened but not offered

1. **Arooj, Nimra, "The Cultural Enactment of Evil Eye: An Ethnography of Strange Power and
   Well-Being", Innovare Journal of Social Sciences 13(3), 2025, 13-15, DOI
   10.22159/ijss.2025v13i3.53151 (live PDF opened, HTTP 200, 1,059,369 bytes).** Rich on Pakistani
   nazar practice (black mark behind the ears, black thread knotted 7 times with verses recited on
   each knot, clay pot on the roof, kala teeka on vehicles), but its sentences do not put a CHARM
   stem within three words of a GUARD stem, so the row failed TOPIC. Verbatim:
   `S631 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://journals.innovareacademics.in/index.php/ijss/article/download/53151/31888 | BOILER: root-clear https://journals.innovareacademics.in/; not a title, h1 or meta label | RELEVANCE: shared=['appli', 'behin', 'black', 'ears', 'evil', 'mark'] | TOPIC: quote_hits=0 function_words=7 page_hits=21 page_terms=60 need=1/2/3/2`
2. **Science Museum Group object A639137, "Amulet, India, 1850-1916"**
   (https://collection.sciencemuseumgroup.org.uk/objects/co125352/amulet-india-1850-1916, HTTP 200,
   39,495 bytes). Passes every leg; held back only by the two-row cap, offered here as the spare if a
   row is lost. Verbatim:
   `S630 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co125352/amulet-india-1850-1916 | BOILER: root-clear https://collection.sciencemuseumgroup.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'bring', 'harm', 'healt', 'luck', 'magic'] | TOPIC: quote_hits=1 function_words=4 page_hits=11 page_terms=10 need=1/2/3/2`
   Its quote: "Many people believe amulets have magical or spiritual powers, that they can bring luck
   and health while protecting from sickness and harm." Row cell available on request in
   /fast/scratch/hyaku/kotodama-r59/ScoutSouthAsiaProtection/rows2.md.
3. **V&A O472423, O472424, O472425, O472427, O472362, O472492, O472421, O472429, O119211,
   O1138177, O1313427, O450622, O451744** (opened through the museum's own JSON API,
   https://api.vam.ac.uk/v2/museumobject/<id>, HTTP 200 each). Editorial exclusion, not a tool
   failure: the Tayler jade group repeats one summary sentence ("This amulet was made to protect the
   wearer from harm or misfortune…"), so one representative (O472426) carries the teaching; the
   amulet cases (O119211, O1138177) and the Rajasthan silver amulet (O1313427) give no sentence that
   ties an object to a named danger, and O450622/O451744 describe meditation diagrams, not
   protection.
4. **V&A O139483 (record 909-1872).** Opened (HTTP 200); excellent protective sentence — "Many people
   believed that the supernatural powers embodied in an amulet could promote fertility and good health
   and offer protection against malign forces or the 'evil eye'." — but the object is a German amulet
   ring, "Group of three amulets on a steel split ring, Schwäbisch Gmünd (South Germany), 1750-1800.",
   outside this seat's South Asian subtopic.
5. **Science Museum Group co126661, co126305, co125831** (HTTP 200 each). Served text is a caption
   sentence only (e.g. "Small talcous plaque, triangular shaped with mythical inscription imitation of
   Musulman jade amulet, British India, 1880-1930"), with no body sentence carrying both a charm term
   and a protective claim; caption fragments are excluded by the row rules.
6. **Metropolitan Museum of Art, object 446771 "Necklace with Embellished Amulet Forms" (India,
   18th century, four tawiz).** The object API record opened (HTTP 200, 1,787 bytes) but carries no
   curatorial text, and the public page refused two plain GETs: `429 34228` and `429 34217`.
7. **British Museum collection search** (https://www.britishmuseum.org/collection/search?keyword=amulet%20india):
   `403 5685` on a plain GET.
8. **Smithsonian (si.edu search and api.si.edu open-access search):** `403 46611` and `403 127`.
9. **Brooklyn Museum open collection search:** `429 34217`.
10. **Aga Khan Museum collection search:** `301 0`, then `404 62344` on the redirected host.
11. **Pitt Rivers Museum online collections (collections.prm.ox.ac.uk):** curl: (6) Could not resolve
    host.
12. **Pitt Rivers "Small Blessings" amulet trail** (http://web.prm.ox.ac.uk/amulets/index.php/protection/index.html,
    HTTP 200, 15,422 bytes). The page opened is the trail's general introduction; its list runs
    Corsica, Italy, France, North Ossetia, Bolivia and similar, with no South Asian object in view, so
    it could not carry a South Asian claim.
13. **Wayback capture of the V&A O472426 page.** The availability API reports a 2024 capture, but
    web.archive.org connections failed in this session when I tried to open it (`curl: (7) Failed to
    connect to web.archive.org:443`), so it is not listed in the row.

## Notes and limits

- S630's teaching is the object's stated purpose and its jade material. The same page's physical
  description also records the Persian inscription and the border of small "+" marks in boxes; that
  detail is page body text but is **not inside the frozen quote**, so do not hang an entry sentence
  about inscribed text or cross marks on S630 — the quote would not carry it to a blind reviewer.
- S631 is a small qualitative study (Multan, Punjab); it supports the practice it reports (an imam as
  spiritual healer recommending an evil-eye amulet and talisman), not a general claim about all of
  Pakistan or all of South Asia. The page also reports black threads from a pir, chilli/mustard
  burning and pathkari rites, which are page-level context only, outside the frozen quote.
- The two rows come from different hosts (collections.vam.ac.uk, www.gsrjournal.com) and share no URL
  or quote. The GSR capture was downloaded and hashed: sha256 a49d80f2fcd31504410d864e26b033805c2724f9830ced000be4f22f66912c5e,
  identical to the live PDF, and it contains the quote.
- The SMG spare is deliberately kept in scratch (rows2.md) rather than written anywhere in the lane.
