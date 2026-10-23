VERDICT: ALL-FAIL

# CtlAllFalse58 — fabricated anchor quotations

Axes: coverage, quotation provenance accuracy, LOCATE zero-slack sensitivity, instrument identity, ordinary-access reproducibility.

All five scored control variants exited **1** and ended with `ACCEPT-C-58: FAIL`. No instrument was modified. Original runs used the required sandbox checkout `d4a5ea31cde8cd20633f2ec03ae22296e389082b`; revision-2 runs used a separate clone at `c42121f4f4b31fcd6758366592a17fa887b69b4e`.

Fixture paths below are relative to this report's directory. Every variant directory also contains full `stdout.txt`, `stderr.txt`, `exit-code.txt`, `result.json`, the exact tracked `git diff` in `tracked.patch`, and the untracked entry under `untracked/corpus/knowledge/linguistics/toponymy-place-names.md`. Each `fixture.patch` combines the tracked diff and the new-file diff and is directly applicable to its stated checkout.

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| all-false, canonical URLs | [CtlAllFalse58/all-false/fixture.patch](CtlAllFalse58/all-false/fixture.patch) | LOCATE, BOILER, TOPIC | 1 |
| all-false, official content routes | [CtlAllFalse58/all-false-content-routes/fixture.patch](CtlAllFalse58/all-false-content-routes/fixture.patch) | LOCATE, BOILER, TOPIC | 1 |
| only S500 false, official content routes | [CtlAllFalse58/one-false-content-routes/fixture.patch](CtlAllFalse58/one-false-content-routes/fixture.patch) | LOCATE, BOILER, TOPIC | 1 |

## Counterexample and evidence

The fixture adds exactly the requested entry, its matching README index row/counts, and twenty mined rows S500–S519. Twenty distinct real toponymy URLs cover USGS naming authorities and GNIS, Nottingham's place-name society/research projects, and LINZ place-name guidance. The teaches cells remain honest paraphrases; the entry echoes those cells. Only the anchor quotations are fabricated.

[quote-pairs.json](CtlAllFalse58/quote-pairs.json) records every genuine sentence, its altered counterpart and its teaching. Alterations include 1890 → 1891, 1925 → 1926, 1991 → 1992, adding/removing negation, Domestic → Foreign, included → excluded, assist → interfere, and the published contact's `.gov` → `.mil`.

Ordinary urllib GETs opened the actual pages; saved HTML, extracted text and HTTP receipts are in [pages/receipts.json](CtlAllFalse58/pages/receipts.json), [pages-extra/receipts.json](CtlAllFalse58/pages-extra/receipts.json), and [pages-node/receipts.json](CtlAllFalse58/pages-node/receipts.json). No browser, challenge solving, paid access or echoed-request service was used. Unused British Academy and one USGS candidate returned HTTP 403 and were not cited.

The cached [provenance audit](CtlAllFalse58/provenance-audit.json), using the unchanged locator and row-check functions, found **20/20 genuine quotes present**, **0/20 altered quotes present**, and **0/20 genuine quotes on the corresponding site roots**. Every true/false pair passed RELEVANCE, had at least one quote naming-place window and a page with at least three windows.

The first all-false run exposed an unrelated conservative refusal: seven semantic URL slugs share three quote words, so `url-reflects-quote` refuses them before fetching. The refined fixture uses the sites' own observed Drupal content routes/shortlink for those seven sources. All seven routes were opened by ordinary GET and returned HTTP 200. [route-refinement.json](CtlAllFalse58/route-refinement.json) ties each route to the saved HTML field that disclosed it; these are real source pages, not constructed echo endpoints.

The refined run isolates the intended attack:

- [all-false stdout](CtlAllFalse58/all-false-content-routes/stdout.txt): LOCATE **0/20**, every row explicitly `quote-absent`; RELEVANCE **20/20**. SET, SWEEP, FLOOR, RANGE, STATUS, USEDBY, ACCESS and FRESH all PASS. BOILER and TOPIC fail consequentially because no quote located.
- [one-false stdout](CtlAllFalse58/one-false-content-routes/stdout.txt): only S500 retains the false creation year **1891** instead of the page's **1890**. LOCATE **19/20**, BOILER **19/20**, TOPIC **19/20**; each names **only S500** as failing. All nine other legs PASS, including RELEVANCE **20/20**. This directly exercises zero slack rather than relying on inaccessible pages, bad metadata or off-topic text.

Command for every score: `timeout 1200 python3 -B reports/round-58/accept-c.py`, run from the applicable clone root. Recorded counter durations were 2.753 s, 1.150 s and 3.053 s respectively; full stdout is preserved, not reconstructed.

Provenance note: the seat context names claim base `a43f5336b56179e1a11b7e1157f3ee2af4432ae5`, while `claims.json` at the explicitly required declaration receipt records `91fb8fd9ff48d64d871fa0778996c38423b54063`. These runs follow the explicit checkout requirement; per-run instrument SHA-256 values in `result.json` identify the actual counters without silently conflating those bases.

## Revision 2 (c42121f4)

These are rescoring runs of the same refined fixtures, not rewritten negative controls. The revised instruments add DISTINCT and tighten TOPIC.

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| revision-2 all-false | [CtlAllFalse58/revision-2/all-false-content-routes/fixture.patch](CtlAllFalse58/revision-2/all-false-content-routes/fixture.patch) | LOCATE, BOILER, TOPIC, DISTINCT | 1 |
| revision-2 only S500 false | [CtlAllFalse58/revision-2/one-false-content-routes/fixture.patch](CtlAllFalse58/revision-2/one-false-content-routes/fixture.patch) | LOCATE, BOILER, TOPIC, DISTINCT | 1 |

[All-false stdout](CtlAllFalse58/revision-2/all-false-content-routes/stdout.txt) again records LOCATE 0/20 and RELEVANCE 20/20. [One-false stdout](CtlAllFalse58/revision-2/one-false-content-routes/stdout.txt) again records LOCATE 19/20, failing only S500; BOILER 19/20; RELEVANCE 20/20. DISTINCT rejects both because these twenty distinct URLs span **3 hosts**, below the newly required 10. Recorded durations: 1.161 s and 2.996 s.

A separate precision tradeoff is observable in the revised TOPIC leg: S511's genuine, complete eight-word sentence, **“Original Māori place names are included where known.”**, fails because FUNCTION recognizes only `are` among its words. The page has **56 naming-place windows** and **46 discipline-term matches**, and the quote is located. Thus revised TOPIC gives 18/20 rather than 19/20. This is a conservative false rejection, not a passing adversarial fixture.

## Impacted axes and smallest safe correction

- **Provenance / coverage admission:** these controls did not evade the frozen counter. Preserve LOCATE's all-rows requirement; no relaxation or repair is supported by this result. RELEVANCE alone accepts the fabricated quotes, but LOCATE rejects them, as intended.
- **Instrument precision:** common title words in ordinary URL paths produce unrelated URL refusals. The smallest fixture-only correction is the observed official content routes already supplied; no instrument change was made or is needed to score this control cleanly.
- **Revision-2 sentence precision:** the two-function-word proxy rejects the attested S511 sentence. Adding `where` to FUNCTION is a minimal candidate correction if that false rejection is unacceptable; whether to retain the conservative tradeoff belongs to the canonical judge, and any change would need pre-data control rescoring. No judgment or implementation was performed here.

## Cheapest variant I could NOT build

A **passing one-date-change fixture** was not obtained: the cheapest attempted semantic forgery, S500's 1890 → 1891 with nineteen genuine anchors, still fails LOCATE on exactly that row in both instrument revisions. Both required variants were built and scored; there is no missing required fixture. This does not claim that all conceivable quotation-normalization attacks are impossible.

## Installs and containment

None. Existing Python 3, Git and coreutils `timeout` sufficed. No git/jj write occurred in the lane or fleet repositories; all source changes and patch applications were confined to the two sandbox clones. Lane writes are confined to this report and `control/CtlAllFalse58/`. Every started process was bounded, all completed, and no service or process tree remains running.
