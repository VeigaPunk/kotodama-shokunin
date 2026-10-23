# S735 — sharing-time narrative

## Behavior / finding
Sarah Michaels's original article analyzes a first-grade sharing-time activity and states that teacher questions and comments help children structure and focus their discourse. This supports the narrow worldbuilding point that classroom narrative is shaped by teacher-child interaction; the article describes the activity as oral preparation for literacy.

## Evidence
- **Source:** Sarah Michaels (1981), “'Sharing time': Children's narrative styles and differential access to literacy,” *Language in Society* 10(3), 423–442. The fetched PDF identifies the journal and Cambridge University Press; it is a primary study, Tier A for Michaels's own analysis of teacher interaction in sharing time.
- **Live URL:** https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf
- **Archive capture:** API response reported `available: true`, `status: 200`, `timestamp: 20161020153309`; original URL: https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf. Capture URL used: https://web.archive.org/web/20161020153309id_/https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf
- **Quote (Abstract):** “The teacher, through her questions and comments, tries to help the children structure and focus their discourse.” (17 words.)
- **Locator, run twice:** `LOCATED https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf`
- **Row:**

ROW: | S735 | Sarah Michaels, 1981 "'Sharing time': Children's narrative styles and differential access to literacy", Language in Society 10(3), 423–442 - https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf ; capture https://web.archive.org/web/20161020153309id_/https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf | paper | A | Michaels's findings on teacher questioning and structuring of sharing-time discourse | Abstract: "The teacher, through her questions and comments, tries to help the children structure and focus their discourse." | Learners can practice shaping oral turns into focused discourse through teacher questions, building communicative control in classroom narration. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |

- **Bullet:** - Teacher questions and comments shape sharing-time discourse toward structure and focus, showing how oral classroom interaction can rehearse literacy. (S735)

## Gates and checks
- Acceptance-C-64 was not run; this receipt is not evidence that the integrated claim passes.
- Two invocations of the specified lane locator both returned `LOCATED` for the live URL.
- `awk -F'|'` reported 13 fields on the row (the expected 11 cells plus boundary fields); quote count was 17 words; `row.txt` contains five labeled lines.
- No tool was installed. No lane source, registry, entry, or acceptance script was edited or run.

## Commands and outcomes
1. Source discovery queries: `"sharing time" "topic-centered" "topic-associating" narrative children`; `schooled narrative children "sharing time" narrative language socialization`. Search identified Michaels's 1981 *Language in Society* paper and an Ohio State-hosted PDF copy.
2. Opened the live PDF with `curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS735/Michaels1981.pdf -w 'HTTP %{http_code}; effective %{url_effective}; content-type %{content_type}; size %{size_download}\n' 'https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf'`. Outcome: HTTP 200, application/pdf, 658862 bytes, same effective URL.
3. Checked Wayback with `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fwww.ling.ohio-state.edu%2Fresearch%2Fgroups%2Flacqueys%2Freadings%2Fearlier%2FMichaels1981.pdf'`. Outcome: closest snapshot available, status 200, timestamp `20161020153309`.
4. Extracted local PDF text with `pdftotext -layout /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS735/Michaels1981.pdf /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS735/Michaels1981.txt`; inspected the abstract and confirmed the quoted sentence.
5. Ran twice from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`: `python3 -B reports/round-61/reopen-quote.py 'https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf' 'The teacher, through her questions and comments, tries to help the children structure and focus their discourse.'`. Both outcomes: `LOCATED https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf`.
6. Count check: `awk -F'|' 'NR==1 {print "ROW fields:", NF} END {print "row.txt lines:", NR}' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS735/row.txt; printf '%s\n' 'The teacher, through her questions and comments, tries to help the children structure and focus their discourse.' | wc -w`. Outcome: 13 fields, 5 lines, 17 quote words.

## Touched surfaces, out of scope, limits
- Scratch artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS735/row.txt`, `Michaels1981.pdf`, and `Michaels1981.txt`.
- Requested report: `.ufo/waves/round-64/w1/ScribeRowS735.md`.
- No other registry rows, entry prose, rejection rows, counter behavior, or calibration work was changed or assessed. No acceptance gate was run.
- Access was the university-hosted PDF copy via plain curl; the article's metadata identifies its journal and publisher. The quoted sentence is from the abstract and supports the stated teacher role, not an independent causal estimate of literacy outcomes.