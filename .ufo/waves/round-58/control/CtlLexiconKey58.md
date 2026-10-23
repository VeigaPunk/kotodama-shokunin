VERDICT: BLOCKING

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| 01 index-header-two-keys (cheapest) | `.ufo/waves/round-58/control/CtlLexiconKey58/01-index-header-two-keys/fixture.patch` | none; all twelve PASS | 0 |
| 02 sid-stop-stems | `.ufo/waves/round-58/control/CtlLexiconKey58/02-sid-stop-stems/fixture.patch` | none; all twelve PASS | 0 |

## Counterexample and evidence

Both variants were built in `/fast/scratch/hyaku/kotodama-r58/CtlLexiconKey58/clone`, checked out at the prescribed declaration receipt `d4a5ea31cde8cd20633f2ec03ae22296e389082b`. Each adds exactly twenty rows, S500 through S519 individually, the required entry, and the README index/count changes. Neither supplies a source-derived toponymy explanation, decision table, or worldbuilding method. No instrument was changed.

**01:** twenty IDs repeat one eight-word index heading from [Wikipedia's Lists of renamed places](https://en.wikipedia.org/wiki/List_of_renamed_places):

> renamed places by country sorted by continent africa

Every teaches cell is just `place renam`; every cited entry line is just `- S500: place renam` with its respective ID. The quote is metatext identifying an index and its organization, not a teaching about place-name formation or use. It has one NAMING–PLACE window; the index page has 70. The quote is absent from the site's successfully fetched root page. Two shared stems satisfy all RELEVANCE bindings without copying any six-word run. Distinct IDs, not distinct evidence, satisfy FLOOR.

**02:** twenty distinct eight-word fragments were selected automatically from that same index using the counter's NAMING/PLACE tests. Teaches is `" ".join(sorted(rowcheck.stems(quote)))`, and each entry line is `- S###: TOPIC RELEVANCE shared=<the same stems>`. For example, S501 quotes `renamed places in chad dr congo list of` and teaches `chad congo list place renam`. These are broken link-list fragments, not explanations. This variant also passes, so deduplicating identical quotes alone would not repair the defect.

Each variant directory contains `fixture.patch`, the complete untracked entry at `untracked/corpus/knowledge/linguistics/toponymy-place-names.md`, full `stdout.txt`, full `stderr.txt` (empty), `exit.txt`, and `run.json`. Variant 02 also contains `lexical-selection.json` with the exact quotes, offsets and stems. Both stdout files end `ACCEPT-C-58: PASS`; their live checks were stamped `2026-10-23T01:14Z` and `2026-10-23T01:15Z`, respectively. Each run used `timeout 1200 python3 -B reports/round-58/accept-c.py` once.

Shared evidence is under `.ufo/waves/round-58/control/CtlLexiconKey58/`: `source-gets.json` records ordinary urllib GET outcomes and body hashes; `list-page-text.txt` and `root-page-text.txt` preserve the extracted text; `provenance.json` records receipt, instrument hashes and runtime; `results.json` records both runs and replay instructions. FRESH passed in both runs: the source URL is not reused from a registry row below S500. No browser, access-control solving, instrument mutation, or external runtime was used. All started subprocesses completed; none remains running.

Identity note: the assignment names claim base `a43f5336b56179e1a11b7e1157f3ee2af4432ae5`, whereas the prescribed receipt's `claims.json` records `91fb8fd9ff48d64d871fa0778996c38423b54063`. This discrepancy is preserved in provenance; it was not used to change the assignment or counter.

## Impacted axes and smallest safe correction

The claimed **coverage/learning** move is falsely admitted by the frozen measurement: the extra file contains counter keys, not knowledge. Evidence-grounding and shortcut resistance are also affected; URL freshness does not establish substantive novelty. This is an observed measurement defect, not an axis tradeoff or a canonical-judge decision.

Route C for **pre-data redesign**, as the binding control rule requires. Make independently checked support for an explicit, substantive entry proposition a required acceptance condition rather than review-only. Keep lexical overlap as a screening aid, not proof of teaching. Preserve both fixtures as required rejection controls. Counting deduplicated evidence would address ID inflation, but does not by itself address variant 02. No redesign, admission, integration, or shipping was performed here.

## Cheapest variant not built

No requested construction was blocked: both the minimal lexical-key fixture and the S-id/STOP-stem fixture were built and scored. A still cheaper two-word anchor (`renamed places`) cannot be an eligible passing fixture because LOCATE requires at least eight normalized words (`reopen-quote.py:172-173`); it was not scored. No unobserved counter result is claimed.

## Installs

None. Existing Python 3, Git, GNU timeout, urllib and the frozen stdlib instruments were sufficient. Pacman was not used.

## Revision 2 (c42121f4)

Not scored by this seat: the parent superseded this revision while source discovery was underway. No verdict is inferred from that unmeasured revision.

## Revision 3 (edecdc90)

Not scored by this seat: the parent superseded it with `1a07344e77ea34c3e6b3c38a838c7c35654522be` before the counter was run. Its sandbox-only draft was not presented as evidence.

## Revision 4 (1a07344e)

VERDICT: BLOCKING

The final requested counter was measured in a fresh sandbox clone at **`1a07344e77ea34c3e6b3c38a838c7c35654522be`**, not either intervening revision. It has fourteen legs, including TIER and DISTINCT, the eight-word teaches requirement, distinct quote function words, discipline terms, and title/h1/meta rejection.

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| 03 diverse-two-key-sentences | `.ufo/waves/round-58/control/CtlLexiconKey58/revision-4-1a07344e/03-diverse-two-key-sentences/fixture.patch` | RELEVANCE: S517 only | 1 |
| 04 diverse-stable-key-sentences (cheapest passing final fixture) | `.ufo/waves/round-58/control/CtlLexiconKey58/revision-4-1a07344e/04-diverse-stable-key-sentences/fixture.patch` | none; all fourteen PASS | 0 |

### Counterexample

Variant 04 uses **twenty distinct URLs, twenty distinct eight-word quotes, and twelve actual source hosts**. Sources are institutional/directory pages from Esri, UCLA, GeoNames, UN Statistics, Washington University, the University of Washington, Illinois, BYU, the UK Gazetteer, World Historical Gazetteer, Nottingham, and USGS. There are no Wikipedia rows, tier-C relabeling, first-URL host padding, URL aliases, or instrument changes. Every row has one source URL and tier B.

The construction reads no source proposition into the entry. A machine scans normalized page words for an eight-word window that meets the exposed NAMING/PLACE/FUNCTION tests, is absent from the root and combined title/h1/meta labels, and contains two usable content stems. Teaches is the fixed sentence:

> The counter keys retained here are &lt;stem&gt; &lt;stem&gt;.

The entire entry consists of `S###: TOPIC RELEVANCE.` labels followed by those generated sentences. It explicitly says it contains counter keys, not worldbuilding knowledge. Each teaches sentence has eight whitespace words and ends with a period; none teaches toponymy.

Examples from the passing fixture:

- S501, UCLA: `guides maps and cartographic resources gazetteers search this`; teaches `The counter keys retained here are carto gazet.`
- S505, Washington University: `and gazetteers gazetteers place name dictionaries search this`; teaches `The counter keys retained here are dicti gazet.`
- S510, Nottingham: `place names the university of nottingham uk china`; teaches `The counter keys retained here are china name.`
- S519, USGS: `geographic names faqs web tools links to the`; teaches `The counter keys retained here are faqs geogr.`

These remain navigation/list/cross-element fragments, despite two distinct function words. Requiring that the whole quote not appear in a title/h1/meta field does not reject a fragment spanning a label and neighboring navigation.

Variant 03 failed because one generated stem was not idempotent: original `domestic` becomes `domes`, but re-stemming the teaches token `domes` yields `dome`. S517 therefore shared only `compl`. Variant 04 changes only that row's teaches and citing entry line from `compl domes` to `compl geogr`. This is a generator correction, not a counter change. Both complete fixtures and outcomes are retained.

### Evidence and correction

Variant 03's stdout ends `ACCEPT-C-58: FAIL` at `2026-10-23T01:22Z`; variant 04's stdout ends **`ACCEPT-C-58: PASS`** at `2026-10-23T01:23Z`. The passing stdout reports `DISTINCT PASS shared=[] hosts=12 need=10`, all twenty rows located, all twenty clearing BOILER, RELEVANCE and TOPIC, and FRESH PASS. Each run used `timeout 1200 python3 -B reports/round-58/accept-c.py` once.

Each variant directory contains its tracked diff, full untracked entry, full stdout/stderr, exit code, and run metadata. Shared revision evidence is in `revision-4-1a07344e/`: `source-gets.json`, `root-gets.json`, `source-texts/S500.txt` through `S519.txt`, `lexical-selection.json`, `provenance.json`, and `results.json`. The selection file records the initial two-key proposal; variant 04's exact patch and entry record the one-token S517 correction. Ordinary GETs only; failed or forbidden scout pages were discarded rather than circumvented.

**Impacted axes:** coverage/learning and source-grounding integrity. Distinct hosts and source-tier labels now pass honestly, but the entry still contains no source-backed knowledge. The smallest safe correction remains a required independent check that the teaches and entry assert a substantive proposition actually supported by the cited passage. Adding another length, punctuation, or function-word threshold would not establish that property. Preserve variant 04 as a required rejection control and route the passing control for pre-data redesign; this seat makes no admission or canonical-judge decision.

### Cheapest unavailable construction and installs

No requested final construction was blocked. The original one-page shortcut is no longer eligible under DISTINCT; a bare stem list no longer meets RELEVANCE (e). Variant 04 meets both revised requirements without performing the claimed learning work. No installs or updates were needed, and no started process remains running.
