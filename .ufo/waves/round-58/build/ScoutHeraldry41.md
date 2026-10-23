# ScoutHeraldry41 — round 58 records item: heraldry entry :41 (spot-check §5 item 3)

Seat: KotodamaR58A2.ScoutHeraldry41 (scout, leaf). Accessed 2026-10-23 UTC.

## Verdict

FOUND. The Court of the Lord Lyon's own guidance PDF supports the cadet clause. The PDF is "Information Leaflet No. 4 — Petitions for Arms" and is served live on the official site; it is the file linked as "Guidance Note: On Petitioning for Arms" on `notes and judgments.htm`. It says this on two pages:

- printed p. 4: "Younger children inherit only a right to matriculate the Arms with a slight difference added, and they must petition separately for this to be done".
- printed p. 8: "younger sons and their descendants inherit a right to apply for a Matriculation of their ancestral Arms with a small mark of difference added".

**Calibration:** the page does not say a cadet *must* matriculate in order to bear arms. It says the following:

- the arms themselves descend "usually to his eldest son";
- younger children inherit "only a right to matriculate" with a difference;
- they "must petition separately" for that matriculation.

The new line 41 text below says exactly that much and no more.

**Vintage:** PDF metadata `CreationDate` is 2011-04-01, and the filename is `formsofpetition042011`. The leaflet still prints the old address "H.M. New Register House" and `www.lyon-court.com`. It remains the current official guidance note on the court's live Notes & Judgments page. The address and fee references are stale; the inheritance rule is not presented as time-bound.

## (1) Registry row

| S575 | Court of the Lord Lyon, 2011 (PDF metadata CreationDate 2011-04-01; filename `formsofpetition042011`), "Information Leaflet No. 4 — Petitions for Arms", linked as "Guidance Note: On Petitioning for Arms" from https://courtofthelordlyon.scot/notes%20and%20judgments.htm, official website of the Court of the Lord Lyon (Scotland) — https://courtofthelordlyon.scot/index_htm_files/formsofpetition042011.pdf (direct, HTTP 200, `application/pdf`, 98,899 bytes, 12 PDF pages; plain GET, no challenge) | docs | A | may support the entry's claim on how arms pass in Scotland: whole to the heir (usually the eldest son), while younger sons inherit only a right to matriculate them with a mark of difference by separate petition; not current fees or address (2011 leaflet) | printed p. 8 (PDF p. 9), "Applying for a Matriculation off Existing Arms", ¶1: "younger sons and their descendants inherit a right to apply for a Matriculation of their ancestral Arms with a small mark of difference added"; printed p. 4 (PDF p. 5), "Applying for a New Grant of Arms", ¶3: "Younger children inherit only a right to matriculate the Arms with a slight difference added, and they must petition separately for this to be done" | supersedes S420 for entry :41's cadet clause only — Scottish arms usually descend to the eldest son, while a younger son may only petition to matriculate them with a small mark of difference. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

About the "supersedes S420" opener: S420's own four quotes still locate and stay valid for lines 54 and 78. Only entry :41's cadet clause moves off S420. If the L1 reads `supersedes` as condemning the whole of S420, the alternative is to drop the opener and log the change as an entry citation fix in the round lesson.

## (2) Gate line

- S575 — https://courtofthelordlyon.scot/index_htm_files/formsofpetition042011.pdf — accessed 2026-10-23 — printed p. 8 (PDF p. 9), "Applying for a Matriculation off Existing Arms", ¶1: “younger sons and their descendants inherit a right to apply for a Matriculation of their ancestral Arms with a small mark of difference added”. Grounds: Scottish arms usually descend to the eldest son, while a younger son may only petition to matriculate them with a small mark of difference. Seat: ScoutHeraldry41.

## (3) Locator output (`reports/round-58/reopen-quote.py`, run from the lane root)

```
$ timeout 300 python3 -B reports/round-58/reopen-quote.py 'https://courtofthelordlyon.scot/index_htm_files/formsofpetition042011.pdf' 'younger sons and their descendants inherit a right to apply for a Matriculation of their ancestral Arms with a small mark of difference added'
LOCATED https://courtofthelordlyon.scot/index_htm_files/formsofpetition042011.pdf
exit 0
$ timeout 300 python3 -B reports/round-58/reopen-quote.py 'https://courtofthelordlyon.scot/index_htm_files/formsofpetition042011.pdf' 'Younger children inherit only a right to matriculate the Arms with a slight difference added, and they must petition separately for this to be done'
LOCATED https://courtofthelordlyon.scot/index_htm_files/formsofpetition042011.pdf
exit 0
```

Quote 1 (the row's first span, which `--row S575` will test) is 24 words, a full clause, and contains the function words "and", "a", "to", "for", "of" and "with". Quote 2 is 26 words, which is one word over the claim-row 8–25 bar. That bar does not bind this records row, and the span the locator tests first is quote 1. Not registered yet: `grep -F 'courtofthelordlyon.scot/index_htm_files' corpus/SOURCES.md` returns no match (exit 1).

## (4) Entry text, line 41 (old → new)

old:
```
| one person and descendants | arms granted or confirmed "to one person and their descendants in the legitimate male line" (S419, Q. Do coats of arms belong to surnames?); in Scotland "all Arms are individual to a person" (S421, served text) | no surname arms (§11); in Scotland a cadet matriculates with a difference (S420) |
```
new:
```
| one person and descendants | arms granted or confirmed "to one person and their descendants in the legitimate male line" (S419, Q. Do coats of arms belong to surnames?); in Scotland "all Arms are individual to a person" (S421, served text) | no surname arms (§11); in Scotland the arms usually descend to the eldest son, and a younger son inherits only a right to petition to matriculate them with a small mark of difference (S575, Information Leaflet No. 4, p. 8) |
```

## Sibling defect, not routed: entry line 140

Line 140 makes the same unsupported claim from S420:

```
| "cadency marks are ancient and compulsory" | R (England) | Tudor systematisation, optional in England, unworkable past two generations (S415; S413); Scotland still differences cadets by matriculation (S420) |
```

S420's page has no "diffe" string; the round-57 spot-check measured `grep -ci diffe` → 0. Suggested fix, at the L1's discretion:

```
| "cadency marks are ancient and compulsory" | R (England) | Tudor systematisation, optional in England, unworkable past two generations (S415; S413); in Scotland younger sons matriculate the arms with a small mark of difference (S575) |
```

## Rejected (opened, not offered)

- https://courtofthelordlyon.scot/faqs.htm (200, 12,602 B). It says "even the heir to a coat of arms has to bear it with a sign of difference". That is about the heir apparent in the holder's lifetime, not about cadets matriculating, so it does not carry :41.
- https://courtofthelordlyon.scot/ (200), `about%20us.htm` (200), `crests.htm` (200), `education.htm` (200), `statutes.htm` (200), `fees.htm` (200), `consulting%20the%20register.htm` (200). The only cadency hits are matriculation as the Lyon's judicial function (about us) and "Making a Difference, unicorns to colour in" (education). None states the cadet rule.
- `notes%20and%20judgments.htm` (200, 14,535 B). It is an index page only; it was used to map the S575 PDF to "Guidance Note: On Petitioning for Arms".
- `index_htm_files/SuccessionofChiefsGuidanceNote.pdf` (200, 410,106 B). It covers chiefs and undifferenced arms, not the cadet rule.
- `index_htm_files/craigend.pdf`, `irvingofbonshawinterlocutor.pdf`, `CarruthersDecision.pdf` and `peerage.pdf` (all 200). These are case-specific decisions; they mention differenced matriculations in passing but state no general rule.
- `index_htm_files/Buchanan.pdf` (200, 298,283 B) and `Pringle.pdf` (200, 4,609,210 B). pypdf 5.4.0 extracted 1 character from each (image-only scans), so they were not read further.
- `https://www.courtofthelordlyon.scot/IsolationHeraldry{Quiz1,Arbroath,Week2Lesson2,Week2Lesson3,Week2Lesson4,Week2Quiz,Lesson1,Lesson2,Lesson3,Lesson4}.pdf` (all 200). The pypdf scan found 0 hits for cadet / younger son / second son / differenc / matriculat in each.

Not opened: Fox-Davies 1909 and Woodward. An official Lyon page answered the question, and the registered copies (S413, S415) use URLs already in SOURCES.md. The 1672 Act was also not opened: S422 already holds the legislation.gov.uk text, and the live page returns a challenge to a plain GET (per S422).

Scratch: `/fast/scratch/hyaku/kotodama-r58/ScoutHeraldry41/` (fetched HTML/PDF and text extracts). No processes left running.

installs: none. pypdf 5.4.0 ran ephemerally through `uv run --no-project --with pypdf==5.4.0`, the same pin `reopen-quote.py` uses; nothing was installed persistently.
