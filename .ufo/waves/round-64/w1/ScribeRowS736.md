# S736 — Literacy socialization and emergent literacy

## Result
Created the assigned sourced row artifact only. The row supports a narrow claim: in this study, young children created stories with caregivers and siblings, treating home storytelling as a setting relevant to emergent literacy. Tier **A** applies to the authors' own study observations for that scope; it does not establish a universal causal effect.

## Row artifact
Path: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS736/row.txt`

ROW: | S736 | Sperry & Sperry, 2021 "Entering Into the Story: Implications for Emergent Literacy", Frontiers in Psychology, 12, Article 665092 - https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full ; capture https://web.archive.org/web/20261012083034id_/https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full | paper | A | the authors' study of home storytelling as a context for children's emergent literacy | Abstract: "created stories with the assistance of their caregivers and siblings" | Worldbuilders can represent shared household storytelling as an everyday setting for children's emergent literacy. | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |

BULLET: - Family stories with caregivers and siblings can create culturally grounded paths into emergent literacy. (S736)

VERIFY: LOCATED https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full

## Evidence and checks
- Opened the article's official full-text page with ordinary `curl`: HTTP 200, final URL unchanged, 1,017,735 bytes, 2026-10-23.
  - Command: `curl -sL --max-time 60 -A 'Mozilla/5.0' -o /tmp/s736-frontiers.html -w 'http=%{http_code} final=%{url_effective}\\n' 'https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full' && printf 'bytes=' && wc -c </tmp/s736-frontiers.html`
- Wayback availability API returned `closest.status=200`, `available=true`, timestamp `20261012083034`, and capture URL `http://web.archive.org/web/20261012083034/https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full`.
  - Command: `curl -s --max-time 60 'https://archive.org/wayback/available?url=https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full'`
  - The row uses the required `https://web.archive.org/web/<timestamp>id_/<original>` form.
- Ran the lane locator twice, including the required final self-check. Both runs printed exactly: `LOCATED https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full`.
  - Command: `python3 -B reports/round-61/reopen-quote.py 'https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full' 'created stories with the assistance of their caregivers and siblings'`
- Self-check: `awk -F'|'` reported 13 fields (11 delimited cells); the quote has 10 words; `row.txt` has 5 lines.
- The row has one live source URL, a same-page capture, `paper` kind, scoped tier A, `mined` status, and the requested date, recheck interval, and entry path.

## Boundaries and limits
- No lane source registry, knowledge entry, acceptance script, or other product code was edited. `ACCEPT-C-64` and other round gates were not run; this report is not evidence they pass.
- No tool was installed or updated.
- The claim is limited to the article's study context and does not support a general causal assertion about all home literacy settings.
- Alternative checks were not used: PubMed live fetch returned HTTP 203; the UNCG dissertation PDF fetch exited 60 with HTTP 000; the SAGE article page returned HTTP 403. No challenge was solved or bypassed.

## Touched surfaces
- Created `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS736/row.txt`.
- Created `.ufo/waves/round-64/w1/ScribeRowS736.md` (this report).
