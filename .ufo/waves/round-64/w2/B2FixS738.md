# S738 row repair findings

## Behavior
Replaced the anchor fragment that the counter interpreted as a quoted uppercase section heading with a verbatim body-text fragment about experts’ advice and the instruction not to introduce Polish immediately after meeting the children. Removed quote marks from the locator prose so the anchor parser encounters only the body quote. Rewrote the S738 sentence with quote-derived content words in order and novel content words.

## Gates
- **Locator:** passed. Exact command:
  ```sh
  cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf' 'in relation to experts’ advice, as they were explicitly instructed not to introduce the language immediately after meeting the children'
  ```
  Output: `LOCATED https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf`
- **Source GET:** passed, HTTP 200, `application/pdf`, 793536 bytes.
- **Archive capture GET:** passed, HTTP 200; final URL was the same-page `id_` capture URL.
- **Wayback availability API:** returned HTTP 429 Too Many Requests. The existing capture timestamp/original was retained from the inherited draft; direct retrieval of that capture succeeded.
- Full `accept-c.py` was not run by this seat.

## Corrected lines
```text
ROW: | S738 | Kinga Kozminska and H. Zhu, 2021, “Making a family: language ideologies and practices in a multilingual LGBTQ+ family with adopted children”, in Diversifying Family Language Policy, Contemporary Studies in Linguistics, Bloomsbury Publishing, pp. 55–79 - https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf ; capture https://web.archive.org/web/20250720191758id_/https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf | book | A | the one studied transnational LGBTQ+ adoptive family's expert-informed caregiver-child language choices | section CONCEPTUALIZATION OF THE FAMILY, NONHETERONORMATIVE MASCULINITY AND ETHNICITY, paragraph beginning The parents also explained: "in relation to experts’ advice, as they were explicitly instructed not to introduce the language immediately after meeting the children" | Shows how expert advice shaped caregivers’ timing for introducing Polish to adopted children. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Experts instructed parents not to introduce Polish immediately after meeting the children (S738)
VERIFY: LOCATED https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf
```

The corrected bullet has eight content words; quote-derived words occur in quote order (experts, instructed, introduce, immediately, meeting, children), with novel content words (parents, Polish). The anchor contains 20 normalized words. The source text and locator were independently reopened; the assignment-provided `in_order=0` report was not rerun.

## Touched surfaces
- `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS738/row.txt` — corrected labelled row artifact (includes CAPTURE and ACCESS evidence).
- `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS738/source.pdf` — source PDF fetched by plain GET for provenance.
- `.ufo/waves/round-64/w2/B2FixS738.md` — this report.

## Out of scope
No lane product code, registry, knowledge entry, acceptance script, Git index, or jj state was changed. No full claim-C acceptance run was performed.

## Artifact paths
- Corrected row: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS738/row.txt`
- Retrieved source: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/FixS738/source.pdf`
- Scoped report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-64/w2/B2FixS738.md`
