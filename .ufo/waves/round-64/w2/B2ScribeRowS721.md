# S721 scoped findings

## Behavior and provenance
- Claim C row for section 3, turn-taking/protoconversation in infancy. Nguyen et al. (2022), “A systematic review and Bayesian meta-analysis of the development of turn taking in adult–child vocal interactions,” *Child Development*, 93(4), 1181–1200, PMC article https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/.
- The paper’s section “The developmental trajectory of turn-taking and its moderators,” paragraph P16, defines proto-conversations as structured nonlinguistic vocal exchanges between infants and peers or adults; the surrounding text reports them before 3 months. The direct quote in the row is 17 words.
- Tier A for the scoped claim: this is the original peer-reviewed systematic review and Bayesian meta-analysis of early adult–child vocal turn-taking, and it explicitly addresses proto-conversation; it is authoritative for that research scope.

## Gates and commands
- Search query: `protoconversation infant turn-taking development review open access peer reviewed paper` returned Nguyen et al. as a relevant open-access systematic review/meta-analysis.
- Opened the primary page by ordinary GET: `curl -sL --max-time 60 -o /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS721/source.html -w 'HTTP %{http_code}\n' 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/'` → `HTTP 200`.
- `curl -s 'https://archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/'`, the repeated direct query `curl -s --max-time 60 'https://archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/'`, the encoded query `curl -s --max-time 60 'https://archive.org/wayback/available?url=https%3A%2F%2Fpmc.ncbi.nlm.nih.gov%2Farticles%2FPMC9271548%2F'`, and the bare-path query `curl -s --max-time 60 'https://archive.org/wayback/available?url=pmc.ncbi.nlm.nih.gov%2Farticles%2FPMC9271548%2F'` all returned HTML `429 Too Many Requests`.
- `curl -s --max-time 60 'https://web.archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/'` returned 404. `curl -s --max-time 60 'https://web.archive.org/cdx/search/cdx?url=pmc.ncbi.nlm.nih.gov%2Farticles%2FPMC9271548%2F&output=json&filter=statuscode%3A200&fl=timestamp%2Coriginal&filter=collapse%3Adigest'` exited 7 (connection failure), with no output.
- Successful ordinary GET `curl -s --max-time 60 'http://archive.org/wayback/available?url=https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/'` returned `available=true`, closest snapshot `status=200`, `timestamp=20250212173742`; the API’s original-page field is `url` with value `https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/`. The row uses `https://web.archive.org/web/20250212173742id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/`.
- Ran twice from the lane root: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/' 'Proto-conversation can be described as a structured, nonlinguistic vocal exchange between infants and their peers or adults'` → `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/` on both runs.
- Row structure/quote check: `awk -F'|' '/^ROW:/{print "ROW fields=" NF}' /home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS721/row.txt && printf '%s\\n' 'Proto-conversation can be described as a structured, nonlinguistic vocal exchange between infants and their peers or adults' | wc -w` → `ROW fields=13` and `17` words.

## Row artifacts
ROW: | S721 | Nguyen et al., 2022 "A systematic review and Bayesian meta-analysis of the development of turn taking in adult–child vocal interactions", Child Development, 93(4), 1181–1200 - https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/ ; capture https://web.archive.org/web/20250212173742id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/ | paper | A | infant vocal turn-taking and protoconversation in early development | The developmental trajectory of turn-taking and its moderators, paragraph 1: "Proto-conversation can be described as a structured, nonlinguistic vocal exchange between infants and their peers or adults" | Helps worldbuilders portray early infant social exchange as structured, nonlinguistic vocal turn-taking | mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md |
BULLET: - A structured, nonlinguistic vocal exchange gives worldbuilders a basis for depicting early infant turn-taking. (S721)
VERIFY: LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/
CAPTURE: timestamp: "20250212173742"; url (original): "https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/"
ACCESS: plain curl, HTTP 200, 2026-10-23

## Touched surfaces and bounds
- Wrote `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS721/row.txt` and fetched `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/ScribeRowS721/source.html`.
- Wrote this requested wave report. Did not edit the corpus entry or registry, lane code, judge, or tests; did not commit or install tools. Round-level acceptance was not run by this row seat; L1 integration remains outside scope.
- No source-access challenge or paywall was encountered. The HTTPS availability endpoint responded with 429; a later plain HTTP GET to the same API returned the same-page capture facts. No challenge was solved or routed around.
