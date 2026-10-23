VERDICT: ALL-FAIL

# Footer control — CtlFooter58

Axes: **coverage** (the claimed learning), **calibration** (false source support), **operability** (the counter's boilerplate boundary). No axis score or admission is assigned here.

## Frozen declaration: d4a5ea31

All runs used sandbox clones checked out at `d4a5ea31cde8cd20633f2ec03ae22296e389082b`. No instrument was edited. Each run executed `timeout 1200 python3 -B reports/round-58/accept-c.py` from its clone. Every run exited 1 and ended `ACCEPT-C-58: FAIL`.

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| A | `.ufo/waves/round-58/control/CtlFooter58/A/fixture.patch` | BOILER, RELEVANCE, TOPIC | 1 |
| B | `.ufo/waves/round-58/control/CtlFooter58/B/fixture.patch` | BOILER, TOPIC | 1 |
| C | `.ufo/waves/round-58/control/CtlFooter58/C/fixture.patch` | BOILER | 1 |
| C-unique (diagnostic) | `.ufo/waves/round-58/control/CtlFooter58/C-unique/fixture.patch` | BOILER | 1 |
| C-unique-footer | `.ufo/waves/round-58/control/CtlFooter58/C-unique-footer/fixture.patch` | BOILER | 1 |

- **A:** 20 honest toponymy teaching/entry lines, but the anchors are unrelated footer/header/cookie/navigation text.
- **B:** the same 20 anchors, with teaching and citing lines made from their content words, reordered into semicolon-separated vocabulary. This avoids a copied six-word run without adding learning.
- **C:** boilerplate containing place/name words, with the same echo construction. All 20 rows passed LOCATE, RELEVANCE and TOPIC; only BOILER stopped this fixture. BOILER nevertheless cleared **12/20** boilerplate rows: S508–S519.
- **C-unique-footer:** stronger control: 20 distinct quotes, 20 distinct inner-page URLs, ten hosts, and at least two function words per quote. Teaching and entry remain vocabulary junk. This passes every leg except BOILER, including the revised counter's DISTINCT and stricter TOPIC (below). BOILER clears **10/20** rows: S508–S515 and S518–S519.
- **C-unique (diagnostic):** retained to record every run, not offered as a pure-footer control. S506's quote crossed a page-specific title into the shared skip-link/header text; replacing it with an entirely shared footer span produced C-unique-footer. The diagnostic also failed BOILER; its 11/20 BOILER clearance must not be presented as all-template evidence.

A/B both had LOCATE 20/20, RELEVANCE 0/20 and 20/20 respectively, TOPIC 0/20, and BOILER 6/20. All other original legs passed for every variant, including FRESH and ACCESS. ACCESS's `2 flagged rows, 0 findings` are retained baseline registry rows, not a bypass used by these controls.

## Revision 2 (c42121f4)

On the parent's revision notice, the same fixtures were applied in fresh sandbox clones at `c42121f4f4b31fcd6758366592a17fa887b69b4e`. This is a separate measurement, not a change to the frozen-declaration receipts. No instrument was edited.

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| A | `.ufo/waves/round-58/control/CtlFooter58/revision2/A/fixture.patch` | BOILER, RELEVANCE, TOPIC, DISTINCT | 1 |
| B | `.ufo/waves/round-58/control/CtlFooter58/revision2/B/fixture.patch` | BOILER, TOPIC, DISTINCT | 1 |
| C | `.ufo/waves/round-58/control/CtlFooter58/revision2/C/fixture.patch` | BOILER, TOPIC, DISTINCT | 1 |
| C-unique (diagnostic) | `.ufo/waves/round-58/control/CtlFooter58/revision2/C-unique/fixture.patch` | BOILER | 1 |
| C-unique-footer | `.ufo/waves/round-58/control/CtlFooter58/revision2/C-unique-footer/fixture.patch` | BOILER | 1 |

For A/B/C, DISTINCT fails because each site pair quotes the same template span, not because of duplicated page URLs or fewer than ten hosts. C's stricter TOPIC passes 12/20. **C-unique-footer removes both escape hatches:** DISTINCT prints `shared=[] hosts=10 need=10`, TOPIC and RELEVANCE each pass 20/20, but BOILER still fails on ten rows. Thus the revised conjunction rejects the strongest valid fixture tested; function-word counting does not itself establish that a span is a sentence or supports a toponymy teaching.

## Counterexample and local evidence

The fixable defect is **root-page absence is not absence of boilerplate**. A language home page, departmental menu, or section-specific repeated block can be absent from the host root. The HTML locator also joins neighboring navigation nodes into an apparently quotable span.

Strong example: S510 on [Nottingham's EPNS history page](https://www.nottingham.ac.uk/research/groups/epns/history.aspx):

> History Officers Membership Survey of English Place-Names Journal of the English Place-Name Society

This is the section's navigation list (`sys_simpleListMenu`), not a teaching about place-name history. It is also present on the [officers page](https://www.nottingham.ac.uk/research/groups/epns/officers.aspx), but absent from `https://www.nottingham.ac.uk/`. Echoing its words makes LOCATE, BOILER, RELEVANCE and both versions of TOPIC pass for that row. These per-row passes are **not** an overall ACCEPT-C-58 pass.

The ten source sites (two real inner pages per site) were:

| ids | site | boilerplate used by C / unique-footer |
|---|---|---|
| S500, S501 | spns.org.uk | society header / skip links plus shared branding |
| S502, S503 | ulsterplacenamesociety.org | charity-registration footer |
| S504, S505 | snsbi.org.uk | hierarchical place-name navigation |
| S506, S507 | ainmean-aite.scot | resource navigation / shared address-branding footer |
| S508, S509 | logainm.ie | English colophon/navigation, unlike the host-root language |
| S510, S511 | nottingham.ac.uk | EPNS section navigation |
| S512, S513 | linz.govt.nz | repeated centenary sidebar link block |
| S514, S515 | nsw.gov.au | back-to-top / page-manager utility block |
| S516, S517 | usgs.gov | BGN section navigation / global menu on two FAQ pages |
| S518, S519 | cymdeithasenwaulleoedd.cymru | English branding/slogan, unlike the Welsh host root |

These are navigation/branding spans, including multi-node fragments, not grammatical prose sentences masquerading as full quotations. C-unique-footer deliberately supplies function words from the real surrounding template; no words are invented or added to the served quotes. All quotes have at least eight normalized words. No purported linguistic lesson was extracted from these spans.

Evidence: `sources.json` lists the exact A/B/C URLs, quotes, GET times and root comparisons; each unique variant has its own `sources.json`. `boiler-contexts.md` records the first/last HTML text-node ancestry and surrounding text for the pure-template variant. `evidence/S500.html` … `evidence/S519.html` retain decoded GET bodies, with the two replacement USGS bodies under `C-unique/evidence/`. Stored HTML is UTF-8-decoded evidence, not a claim of byte-identical wire captures; `body_sha256` hashes that stored decoded representation.

## Smallest safe correction

Retain this as a red control. If BOILER is intended to certify “not template text,” preserve the located span's HTML-region provenance and reject header, navigation, footer and utility-template occurrences rather than treating a clear host root as sufficient. The stricter function-word count and exact quote deduplication do not repair that boundary: C-unique-footer demonstrates both can pass on genuine template fragments. Sentence support beyond lexical overlap must remain an explicit independent review obligation. This report does not change the instruments or declare the whole claim defeated: **no complete control passed**.

## Cheapest variant not built

A fully passing, pure-template, 20-row/ten-host control was not established. In C-unique-footer, ten rows on five hosts still matched their host roots. Dropping them leaves only ten citations/five hosts; repeating surviving rows violates the assigned shape and revised DISTINCT. Finding five further hosts with verified root-absent template text is an unbuilt fixture, not evidence that such a control is impossible. No quote, page, or pass was fabricated to fill the gap.

## Reproduction and containment

Every fixture directory contains `fixture.patch`, `tracked.diff`, the separate `untracked/corpus/knowledge/linguistics/toponymy-place-names.md`, full `stdout.txt`, `stderr.txt`, and `run.json` (exit, failed legs, UTC start/end). `fixture.patch` combines the sandbox `git diff` with the untracked entry's `/dev/null` diff, so it is directly applicable to a clean clone at the table's revision; the separate untracked copy is also preserved. `runs.json` indexes all ten measurements. `instrument-sha256.txt` records both counter revisions; their locator digest is unchanged.

Initial A/B/C counters ran at 01:17 UTC, revision-2 replays at 01:19, unique diagnostics at 01:21, and corrected pure-template controls at 01:22 on 2026-10-23. Every cited page was opened by ordinary urllib GET, without browser automation, credentials, or access-control circumvention. Only sandbox clones under `/fast/scratch/hyaku/kotodama-r58/CtlFooter58/` received Git writes, with GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset. Lane writes are confined to this report and its matching artifact directory. All timeout-bounded counters and Git processes returned; no service or background process was left running.

## Installs

None. Existing Python 3, Git and standard-library HTTP/HTML facilities sufficed. The operator tool rules were read; no package transaction was performed.
