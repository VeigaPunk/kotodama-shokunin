# ScoutReopenC — blind re-open and tier honesty (claim C)

## Finding

All ten assigned round-65 row fragments were absent at inspection. Therefore every row is `NOT-LOCATED: fragment absent` in the reopen protocol sense—not a failed HTTP fetch. There was no live URL, anchor quote, or capture URL to test, so no `curl` request was made. **No row's A/B tier can be judged honest or inflated from the available evidence.** The per-row tier verdict is explicitly pending, rather than inferred from the task topic.

The round-65 `rows/` directory was empty when listed. From the lane root I checked all assigned paths with `test -f`; all returned absent:

```text
ABSENT .ufo/waves/round-65/rows/ScoutRow09/row-S766.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow09/row-S767.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow10/row-S768.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow10/row-S769.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow11/row-S770.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow11/row-S771.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow12/row-S772.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow12/row-S773.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow13/row-S774.txt
ABSENT .ufo/waves/round-65/rows/ScoutRow13/row-S775.txt
```

The owner-to-path mapping follows `.ufo/waves/round-65/taskcall-final.json` (ScoutRow09–13). A search of `corpus/SOURCES.md` for S766–S775 also returned no matches. The baseline `reports/round-65/telemetry/dry-run-c.txt` is consistent with the pre-data state: no new rows/entry and expected `ACCEPT-C-65: FAIL`; this is a frozen baseline receipt, not evidence of live-source failure.

## Per-row verdicts

“Tier check” below is **not assessable** because the fragment containing the selected source, tier, and claimed scope is absent. The final column records the scope-sensitive question to apply once it exists; these are review targets from the assigned topics, not claims about a selected source.

| ID | Expected fragment | Re-open verdict | Tier-honesty check / remaining dependency |
|---|---|---|---|
| S766 | `.ufo/waves/round-65/rows/ScoutRow09/row-S766.txt` | NOT-LOCATED: fragment absent | Not assessable. Need source identity, tier, scope, URL, quote, and capture; test whether the source is authoritative for the specific playing-card history asserted. |
| S767 | `.ufo/waves/round-65/rows/ScoutRow09/row-S767.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; test whether evidence is archaeological/primary or only a secondary summary, and keep the scope to what it establishes about dice. |
| S768 | `.ufo/waves/round-65/rows/ScoutRow10/row-S768.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; test whether the chosen source is scholarship for the teetotum/dreidel claim rather than a general or community description. |
| S769 | `.ufo/waves/round-65/rows/ScoutRow10/row-S769.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; distinguish Opie’s source text from publisher/catalogue or other abstract-only evidence for the claimed playground-game scope. |
| S770 | `.ufo/waves/round-65/rows/ScoutRow11/row-S770.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; determine whether the anchor is Gomme’s catalogue itself or a secondary description, and scope it to what the catalogue records. |
| S771 | `.ufo/waves/round-65/rows/ScoutRow11/row-S771.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; verify the chosen museum/scholarly authority supports the precise lacrosse / First Nations origin account claimed. |
| S772 | `.ufo/waves/round-65/rows/ScoutRow12/row-S772.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; an official source may be authoritative for current ritual grammar, but historical claims require support at that scope. |
| S773 | `.ufo/waves/round-65/rows/ScoutRow12/row-S773.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; test whether the source supports the particular patolli evidence/reconstruction and does not present uncertain interpretation as settled. |
| S774 | `.ufo/waves/round-65/rows/ScoutRow13/row-S774.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; official rules can support current kubb rules, not by themselves a historical relationship among kubb, skittles, and ninepins. |
| S775 | `.ufo/waves/round-65/rows/ScoutRow13/row-S775.txt` | NOT-LOCATED: fragment absent | Not assessable. Need the fragment; check whether a museum survey supports its asserted board-game scope or only its own collection/exhibition. |

## Tier calibration and frozen-counter context

Observed rule: `corpus/QUALITY.md:29` says publisher descriptions and abstracts are tier B for substantive claims about a work; tier A is reserved for a source primary or authoritative for the exact scope. A filed tier correction requires a superseding SOURCES row, not an in-place edit.

The specified round-64 inflation examples illustrate that rule: `.ufo/waves/round-64/res/ResVerifyRows.md:92-94,101-116` records S721, S726, and S737 corrected A→B with scope narrowed to the evidence actually opened. The repair notes explain the reasons: S721 anchored a review's secondary-literature background definition rather than its own synthesis (`res/ResFixS721.md:43-61`); S726 was an ERIC abstract/record rather than the work (`res/ResFixS726.md:63-72`); S737 was an ERIC abstract with linked full text returning 404 (`res/ResFixS737.md:32-45`). These are the concrete patterns to test against each landed row, but they do not establish the tier for any S766–S775.

`reports/round-65/claims.json:11-24` freezes claim C as 26 mined A/B rows cited once. `reports/round-65/accept-c.py:16-20` mechanically checks the A/B label and row structure; its lines 58-59 leave blind source-support judgment review-only. Thus the frozen counter cannot substitute for this missing semantic tier audit. I read the frozen claim, `accept-c.py`, `telemetry/controls-c.txt`, and `telemetry/dry-run-c.txt`; the controls exercise counter behavior (including the RESTATE and query-only URL-twin fixtures), not the missing source choices here.

## Unresolved / method limits

Dependency: the ten exact row fragments above. Once available, reopen each live URL, record HTTP status and whether the 8–25-word quote occurs in body text rather than caption/navigation, and verify the capture's original path matches the live URL; then complete each tier/scope verdict from the actual evidence. No LSP device is exposed in the available tool inventory; this is a source-content review, and no absent row was treated as semantically inspected. No tools were installed or updated.
