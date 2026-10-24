# ScoutReopenA — blind re-open (claim C)

## Evidence and limits

Observed: `.ufo/waves/round-65/rows/` was empty when listed. A follow-up `test -f` check found each of the eight assigned fragment paths below absent. The expected paths follow the row-seat assignments in `.ufo/waves/round-65/taskcall-final.json` (ScoutRow01–04).

Because the fragments are absent, no live URL, anchor quote, or capture URL/timestamp is available to re-open or validate. No `curl` request was issued: choosing a URL without its assigned fragment would not be a re-open of that row. Thus there is no HTTP status or body-text quote evidence yet. Verdicts below mean the required evidence could not be located because of the missing fragment, not that an attempted URL returned an error.

## Row findings

| Row | Verdict | Expected fragment | Evidence / dependency |
|---|---|---|---|
| S750 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow01/row-S750.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S751 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow01/row-S751.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S752 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow02/row-S752.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S753 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow02/row-S753.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S754 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow03/row-S754.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S755 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow03/row-S755.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S756 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow04/row-S756.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |
| S757 | NOT-LOCATED: fragment absent | `.ufo/waves/round-65/rows/ScoutRow04/row-S757.txt` | `test -f` returned absent. No URL to pass to `curl`; quote-in-body and capture/original-path match remain untested. |

## Exact existence-check output

Command run from the lane root:

```text
for f in .ufo/waves/round-65/rows/ScoutRow01/row-S750.txt .ufo/waves/round-65/rows/ScoutRow01/row-S751.txt .ufo/waves/round-65/rows/ScoutRow02/row-S752.txt .ufo/waves/round-65/rows/ScoutRow02/row-S753.txt .ufo/waves/round-65/rows/ScoutRow03/row-S754.txt .ufo/waves/round-65/rows/ScoutRow03/row-S755.txt .ufo/waves/round-65/rows/ScoutRow04/row-S756.txt .ufo/waves/round-65/rows/ScoutRow04/row-S757.txt; do if test -f "$f"; then printf 'PRESENT %s\n' "$f"; else printf 'ABSENT %s\n' "$f"; fi; done
ABSENT .ufo/waves/round-65/rows/ScoutRow01/row-S750.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow01/row-S751.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow02/row-S752.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow02/row-S753.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow03/row-S754.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow03/row-S755.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow04/row-S756.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow04/row-S757.txt
```

No tooling installed or updated.
