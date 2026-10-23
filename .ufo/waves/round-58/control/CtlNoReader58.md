VERDICT: BLOCKING

# No-reader control

The originally assigned frozen counter at `d4a5ea31cde8cd20633f2ec03ae22296e389082b` accepted **title-refined**: exit **0**, all twelve legs PASS, final line `ACCEPT-C-58: PASS` (2026-10-23 01:19 UTC). This is not a claim of a pass against later revisions.

| variant | fixture path | failing legs | exit |
|---|---|---|---:|
| title | `.ufo/waves/round-58/control/CtlNoReader58/title/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |
| title-journal-mix | `.ufo/waves/round-58/control/CtlNoReader58/title-journal-mix/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |
| title-refined | `.ufo/waves/round-58/control/CtlNoReader58/title-refined/fixture.patch` | **none — ACCEPT-C-58: PASS** | 0 |
| meta | `.ufo/waves/round-58/control/CtlNoReader58/meta/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |
| h1 | `.ufo/waves/round-58/control/CtlNoReader58/h1/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |
| snippet | `.ufo/waves/round-58/control/CtlNoReader58/snippet/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |

Each directory contains the full `stdout.txt`, `stderr.txt`, `run.json`, a `manifest.json` mapping every quote to its allowed shallow surface, and the untracked entry at `corpus/knowledge/linguistics/toponymy-place-names.md`. The patch saves both tracked changes (SOURCES rows and README index/counts). Reproduce in a clone of the named declaration by applying the patch and copying that entry, then running `timeout 1200 python3 -B reports/round-58/accept-c.py`.

## Counterexample and evidence

- **Exact accepted fixture:** `.ufo/waves/round-58/control/CtlNoReader58/title-refined/fixture.patch`, plus `.ufo/waves/round-58/control/CtlNoReader58/title-refined/corpus/knowledge/linguistics/toponymy-place-names.md`. Its complete counter output is `.ufo/waves/round-58/control/CtlNoReader58/title-refined/stdout.txt`.
- Twenty distinct fresh URLs, one new indexed entry, twenty cited rows, no changed instruments. Eight PMC pages and twelve Names journal pages supplied only their HTML title. The entry contains twenty generic label prompts, not a toponymy method, decision table, historical analysis, or worldbuilding lore handoff.
- Example: the title “Geospatial analysis of toponyms in geotagged social media posts - PMC” yields teaches `Lexical prompts: analysis; geospatial.` and entry `Use geospatial and analysis as worldbuilding labels. (S503)`. No page-body proposition is extracted. Every row follows the same two-content-word echo construction.
- Extraction downloaded pages using ordinary GET and retained only the HTML title, first h1, and description/og:description values. No challenge solving or alternate authenticated route was used. `surface-receipts.json` and `journal-surface-receipts.json` retain statuses, hashes, URLs and extracted surfaces. The original snippet variant uses only leading 240-character abstract snippets from the Europe PMC bibliographic search index; this is explicitly not a Google/Bing-snippet claim. `indexed-snippets.json` records that provenance.
- Failed original variants are not independent evidence that reading occurred: short headings, URL-reflection rejection, quote absence and live page-topic failures rejected them. In particular, metadata and search snippets still clear RELEVANCE for all twenty rows.

**Impacted axes:** substantive coverage/learning; source-reading provenance; evidence-to-teaching fidelity; counter discriminability. The observed pass is a fixable acceptance-predicate defect, not a harmless formatting or stylistic tradeoff: a metadata label inventory was accepted as the declared learned topic entry. No admission, integration or Rust judgment is made here.

**Smallest safe correction:** distinguish page-label matches from body evidence and keep this exact passing fixture as a required negative control. A title-only inventory must not support a learning claim. A body-location rule alone still cannot establish reading or entailment when a search snippet repeats body text; independently check that entry propositions are carried by source-specific body evidence rather than by author-written stem echoes. Sentence length and host counts do not establish that.

## Revision 4 (1a07344e)

At the parent's request, a fresh clone at `1a07344e77ea34c3e6b3c38a838c7c35654522be` scored four further variants. All have **20 distinct URLs**, tier B rows, fresh URLs, sentence-shaped teaches cells of at least eight words ending in a period, and **DISTINCT PASS**: title/meta/h1 span ten hosts; snippet spans fifteen. No instruments were edited. Each exits 1 and prints `ACCEPT-C-58: FAIL`.

| variant | fixture path | failing legs | exit |
|---|---|---|---:|
| revision4/title | `.ufo/waves/round-58/control/CtlNoReader58/revision4/title/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |
| revision4/meta | `.ufo/waves/round-58/control/CtlNoReader58/revision4/meta/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |
| revision4/h1 | `.ufo/waves/round-58/control/CtlNoReader58/revision4/h1/fixture.patch` | LOCATE, BOILER, RELEVANCE, TOPIC | 1 |
| revision4/snippet | `.ufo/waves/round-58/control/CtlNoReader58/revision4/snippet/fixture.patch` | LOCATE, BOILER, TOPIC | 1 |

`revision4-surface-receipts.json` contains the ordinary-GET receipts and exact web-search snippets used in the final snippet variant. This time the snippets are actual quoted web-search results across multiple hosts, not Europe PMC abstract snippets. Search results that returned unrelated GTA pages were discarded, not treated as evidence.

The final BOILER leg explicitly rejects `quote-is-title-heading-or-meta`; that rejection was exercised in the title and metadata variants. The h1 variant also has genuinely short first headings and two headings with only one shared content stem; its extra RELEVANCE failure is recorded, not concealed. The final snippet variant still clears LOCATE, BOILER, RELEVANCE and TOPIC for **S500, S502, S503, S506, S513, S514 and S518**, derived from the full counter miss lists. Those seven rows remain no-reader constructions. Thus the four final overall failures do **not** prove saturation of the no-reader class; no final-revision full pass was observed.

Revision 2 (`c42121f4`) was superseded by the parent's final revision before any rescore was run; no revision-2 result is claimed.

## Cheapest variant not built

A twenty-row, ten-host **passing** final-revision snippet control. The opened search results provided seven rows that cleared all four page/row checks, not twenty; remaining results had absent/too-short quotes, URL-reflection refusal, header matches, or inaccessible/live-changing responses. I did not invent the missing body quotes, silently substitute page-body reading, or claim a seven-row subset as a twenty-row pass. Likewise, many genuine first h1 elements in the ten-host set are shorter than the counter's eight-word minimum; their actual strings were retained rather than padded with body text.

## Containment and installs

Only the requested report and `control/CtlNoReader58/` artifacts were written in the lane. Git writes were confined to timeout-bounded sandbox clones under `/fast/scratch/hyaku/kotodama-r58/CtlNoReader58/` with Git environment overrides unset. All counter subprocesses and source-GET worker pools completed; no child process remains running. Generated sandbox import caches were removed. No tool installation or update was performed.

Report: .ufo/waves/round-58/control/CtlNoReader58.md
