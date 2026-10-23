# FixRowsS728S742 — round 64 wave 2

Axes: coverage, operability, calibration.

## Changes

- `.ufo/waves/round-64/rows/ScribeRowS728/row.txt` — old: “Kaluli caregivers teach children to correct non-target-like speech with explicit prompts (S728)”; new: “Frye relays Schieffelin's report that Kaluli mothers use elema to prompt children to correct non-target utterances (S728)”. The new wording keeps the claim explicitly attributed to Schieffelin as relayed by Frye.
- `.ufo/waves/round-64/rows/ScribeRowS742/row.txt` — old: “Morning greetings teach students to expect peer welcome as a shared classroom practice. (S742)”; new: “In one second-grade classroom, greetings became what students did routinely and expected from each other (S742)”. The new wording retains the source's one-classroom limit.

## Retained evidence

- Read wave-1 `ReviewerEntry.md`, F5: it flags the S728 secondary-account hedge and S742 single-classroom bound.
- Reopened S728's live PDF (`https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf`). Section 8.1 states: “Schieffelin (1990), for example, reports that Kaluli mothers use *elema* ‘say it like this’ to prompt the children to correct their non-target-like utterances”. This supports keeping the Schieffelin attribution rather than presenting it as Frye's direct finding.
- Reopened S742's live PDF (`https://files.eric.ed.gov/fulltext/EJ1271032.pdf`). Page 48 contains the quoted routine passage; the paper identifies its focal setting as “one second-grade classroom” (Methods, p. 44). The revised bullet retains that limit.
- Ran `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`: S728 OK and S742 OK, but overall **31/32 clean**. The only reported remaining finding is S739 `quote_words=5 in_order=0`, outside the two assigned edit paths and unchanged. Therefore the requested 32/32 result is blocked by S739; no out-of-scope row was edited.

No tools were installed or updated.