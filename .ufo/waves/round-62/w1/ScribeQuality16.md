# ScribeQuality16 — Round 62 W1 records

Axis: calibration. Scope: report-only draft; no product files changed.

## Draft for `corpus/QUALITY.md` (text only)

Append as criterion 16:

> 16. **Live fetches are bounded and quotations are body-scoped** — before data, a predicate with a live-fetch leg states its retry budget for transient results (attempts per URL, number of passes, and the gap between passes), and each row lists the live URL followed by an archived capture of that same page. Freeze the budget and row sources before data; one transient result must not decide the claim, while failure after the declared budget remains a failure. A quotation found only in a caption, alt/title/data attribute, or figure caption is not body text: replace it with a body-text quotation or explicitly scope the entry line as a caption. Check: once `tools/reopen-row.py` lands, run `python3 -B tools/reopen-row.py S665`; `CAPTION_ONLY` is not a body-text locate and requires caption-scoped wording or replacement. Shown able to fail on round-61 bytes: S665's anchor identifies a “17th century image caption,” and the spot-check found its quote only in caption fields; the entry line is not caption-scoped. R61-M4 records S671's single capture erroring on the first LOCATE and locating on a diagnostic run about two minutes later. Grounded in `corpus/lessons/round-61-verifier-spotcheck.md` §7 items 1 and 5 and `corpus/lessons/round-61.md` R61-M4; drafted by ScribeQuality16.

## Evidence and limits

- Section 7 item 1 routes the unmarked S665 caption quote (alongside S666, S692, and S687); item 5 identifies the gap in QUALITY criterion 13 after S671's transient archive error.
- R61-M4 states that S671's live URL returned 403, its only capture errored at 09:58Z, and that same capture located on a later diagnostic run; the first claim receipt remained a miss.
- Round-61 spot-check §5 says the S665 page's three quote occurrences are caption fields (`data-img-description` and `thumbnail-description`), with no body text. Its SOURCES anchor labels the passage a “17th century image caption”; its entry line 74 is not caption-scoped.
- The round-62 `accept-o.py` contract defines `CAPTION_ONLY` for a caption match without a body match and specifies the tool's retry and pass behavior. `tools/reopen-row.py` is absent at the round-62 base, so the suggested S665 check was not executed; it is expressly conditional on the tool landing. No tool was installed.
- Affected surface: proposed text for `corpus/QUALITY.md` only. No changes were made to `QUALITY.md`, SOURCES, the entry, or tools.