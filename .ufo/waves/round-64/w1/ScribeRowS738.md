# ScribeRowS738 — scoped source-row report

## Behavior and findings

Produced one sourced row and one worldbuilding bullet for S738 in the assigned scratch artifact. The source is Kinga Kozminska and H. Zhu’s 2021 chapter, “Making a family: language ideologies and practices in a multilingual LGBTQ+ family with adopted children,” in *Diversifying Family Language Policy* (Bloomsbury Publishing). The Birkbeck institutional repository record identifies it as a book section and labels the fetched PDF an author’s accepted manuscript.

The 18-word locator quote is from the chapter’s “CONCEPTUALIZATION OF THE FAMILY, NONHETERONORMATIVE MASCULINITY AND ETHNICITY” section, following Excerpt 4.1. The authors report that expert advice shaped the parents’ language choices to prioritize the children’s wellbeing. Tier A is scoped only to the chapter’s own ethnographic finding about this one studied transnational LGBTQ+ adoptive family; it is not evidence for a general rule about all families. The manuscript describes about 12 hours and 30 minutes recorded in this family.

Final scratch artifact:

```text
ROW: | S738 | Kinga Kozminska and H. Zhu, 2021 "Making a family: language ideologies and practices in a multilingual LGBTQ+ family with adopted children", in Diversifying Family Language Policy, Contemporary Studies in Linguistics, Bloomsbury Publishing, pp. 55–79 - https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf ; capture https://web.archive.org/web/20250720191758id_/https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf | book | A | the one studied transnational LGBTQ+ adoptive family's expert-informed caregiver-child language choices | section "CONCEPTUALIZATION OF THE FAMILY, NONHETERONORMATIVE MASCULINITY AND ETHNICITY", paragraph following Excerpt 4.1: "as a result of the experts’ advice, they prioritized the children’s well-being and accommodated to their needs linguistically" | Helps worldbuilders model how adoption experts' advice can shape caregivers' language choices while prioritizing children's wellbeing. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - Expert guidance prioritized children’s well-being and accommodated their needs linguistically during adoptive language socialization (S738)
VERIFY: LOCATED https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf
CAPTURE: timestamp=20250720191758; original=https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf
ACCESS: plain curl GET of the accepted manuscript PDF, HTTP 200, 2026-10-23
```

## Commands, gates, and outcomes

- `web_search` query: `"language ideologies" childrearing socialization child language acquisition ethnography`. The result list included the Birkbeck EPrints item for this chapter.
- `curl -sL --max-time 60 -o record.html -w 'HTTP %{http_code} FINAL %{url_effective}\n' 'https://eprints.bbk.ac.uk/id/eprint/47679/'` — HTTP 200; final URL was the EPrints record.
- `curl -s --max-time 60 -o wayback.json -w 'HTTP %{http_code}\n' 'https://archive.org/wayback/available?url=https%3A%2F%2Feprints.bbk.ac.uk%2Fid%2Feprint%2F47679%2F'` — HTTP 200; record-page response reported a 200 snapshot at timestamp `20250616215111`.
- `curl -sL --max-time 60 -o manuscript.pdf -w 'HTTP %{http_code} FINAL %{url_effective} TYPE %{content_type}\n' 'https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf' && file manuscript.pdf` — HTTP 200, `application/pdf`; PDF 1.7, 21 pages.
- `curl -s --max-time 60 -o pdf-wayback.json -w 'HTTP %{http_code}\n' 'https://archive.org/wayback/available?url=https%3A%2F%2Feprints.bbk.ac.uk%2Fid%2Feprint%2F47679%2F3%2F47679.pdf'` — HTTP 200; Wayback reported `available: true`, closest snapshot `status: "200"`, timestamp `20250720191758`. The response’s top-level `url` is the original PDF URL; the row uses the requested `id_` capture form.
- Ran twice from the lane root: `python3 -B reports/round-61/reopen-quote.py 'https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf' "as a result of the experts’ advice, they prioritized the children’s well-being and accommodated to their needs linguistically"` — both runs printed `LOCATED https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf`.
- Self-check: `awk -F'|' 'NR==1 {printf "fields=%d cells=%d\n", NF, NF-2}' row.txt` printed `fields=13 cells=11`; `printf '%s\n' 'as a result of the experts’ advice, they prioritized the children’s well-being and accommodated to their needs linguistically' | wc -w` printed `18`. The bullet clause has 14 words before `(S738)` and retains distinctive quote words in order.

The locator passed and the archive lookup found a capture. No bot challenge or paywall was encountered. No acceptance script was run: this contribution does not establish that the overall ACCEPT-C-64 predicate passes. No tool was installed or updated.

## Touched surfaces and limits

Read-only source/repository inspection and locator execution only. Created `row.txt` in the assigned scratch directory and this requested scoped report. Did not edit the corpus entry, source registry, product code, judge, Git index, or jj state. Claim O, claim Ca, and the whole claim-C acceptance gate are out of scope here.

## Artifact paths

- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS738/row.txt`
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS738/record.html`
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS738/wayback.json`
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS738/manuscript.pdf`
- `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS738/pdf-wayback.json`
- `.ufo/waves/round-64/w1/ScribeRowS738.md`
