# ScribeRowS721 — local artifact audit

## Behavior and findings

No finalized S721 registry row or bullet was present in the scratch artifact: `row.txt` is empty. The saved `article.html` identifies Maya Gratier et al., “Early development of turn-taking in vocal interaction between mothers and infants,” *Frontiers in Psychology* (2015), at `https://pmc.ncbi.nlm.nih.gov/articles/PMC4560030/`. Its abstract contains text about infant protoconversations, turn-taking, and overlapping vocalization. This is a relevant candidate source, not an admitted or locator-verified row.

`archive.json` records a Wayback availability response for that PMC URL: `available: true`, closest snapshot `status: "200"`, timestamp `20250917215951`, and closest URL `http://web.archive.org/web/20250917215951/https://pmc.ncbi.nlm.nih.gov/articles/PMC4560030/`. The saved JSON does not contain a separate `original` field or the requested `id_` capture URL, so neither is asserted here.

No tier was finalized. [INFERENCE] The peer-reviewed paper could be tier A for its own empirical findings; an abstract statement that protoconversations are “known” summarizes prior research and may warrant tier B for that proposition rather than being represented as a finding of this paper.

## Commands, gates, and outcomes

No source-search query, `curl` request, Wayback lookup, lane locator, self-check, or acceptance script was run in this session. Their outputs therefore are not available as execution evidence. The user-provided command strings are not reported as executed commands. The saved HTML and JSON are inherited local artifacts; their creating commands, HTTP status for the source GET, and access date are not recorded in the scratch directory. The Wayback metadata above is a fact read from the saved JSON, not a newly exercised gate.

No acceptance gate or test was exercised. The required locator line, row field/cell check, quote word-count check, and final row/bullet are absent. This item is not ready for integration as S721.

## Touched surfaces and limits

Read-only inspection: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS721/row.txt`, `article.html`, and `archive.json`. Created this requested scoped report: `.ufo/waves/round-64/w1/ScribeRowS721.md`. No product code, corpus entry, source registry, judge, or lane index was changed; no tool was installed or updated.

## Artifact paths

- Scratch source artifacts: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS721/article.html` and `archive.json`
- Empty row artifact: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS721/row.txt`
- Scoped findings report: `.ufo/waves/round-64/w1/ScribeRowS721.md`
