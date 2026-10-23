# ScribeRejS747 — scoped findings

## Axes
Coverage, source-ground accuracy, and auditability.

## Candidate and provenance
- Read `corpus/lessons/round-63.md` first, then `corpus/lessons/round-63-verifier-spotcheck.md` and `.ufo/waves/round-63/w1/ScribeRowS711.md` to reconstruct the candidate. The seat note identifies `https://www.britannica.com/topic/mortarboard` as the Britannica candidate and records the original HTTP 404; the spot-check lesson groups it among the academic-dress rejects.
- Web search query: `Britannica academic dress`. Search results did not surface the Britannica mortarboard URL. The exact URL above comes from the round-63 seat's rejection record, not an inference from search results.
- Filed citation: Encyclopaedia Britannica, “Mortarboard”; kind `docs`, tier `B`, scoped to the mortarboard as academic headwear in academic dress. No candidate-page quote was available to test.

## Re-test and result
Command run exactly as assigned:

```text
curl -sS -o /dev/null -w '%{http_code} %{url_effective}' -L --max-time 60 'https://www.britannica.com/topic/mortarboard'
```

Verbatim output:

```text
403 https://www.britannica.com/topic/mortarboard
```

The historical HTTP 404 is documented in the round-63 seat note but was not reproduced: the current ordinary request returned HTTP 403. Therefore the exact 404 ground is not confirmed by this re-test; the row records only the measured 403 refusal, not a current 404. The response did not serve an article, and no quote was involved, so the quote locator was not run (`TEST2: not applicable`). The positive contradiction condition in the assignment (page serves the entry or locator finds a quote) was not observed. No challenge was solved or routed around.

## Row artifact
`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRejS747/row.txt` contains the required three labelled lines. It records the re-tested output verbatim, keeps status `rejected`, and flips the verdict if an ordinary request later serves the article with a verifiable relevant quote.

## Gates, touched surfaces, and limits
- No ACCEPT-C-64 gate or other test was run; this was a source-ground re-test only.
- Touched surfaces: the scratch `row.txt` and this specifically requested wave report. No product code or registry in the lane was changed.
- No tools were installed or updated.
- Locator verification remains inapplicable because the unavailable candidate page supplied no quote; the exact prior 404 was not reproduced.
