# QUALITY criterion 10 — routed defect 6

## Findings

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/QUALITY.md:37` permits ordinary access routes and addresses bypassed access controls, but does not address the permission status of third-party scans.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-56.md:159` records R56-M4: two third-party journal scans were filed as ordinary public copies; neither had stated permission, and the L1 rejected both before landing. The Gate records their rejection at `corpus/lessons/round-56.md:81-82`.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-56-verifier-spotcheck.md:127-128` confirms both outcomes and the decisive details: the 1991 JSTOR cover states personal-use terms without host permission; the 2001 site's CC BY 4.0 licensing covers only its images, while the PDF cover says it was downloaded from JSTOR.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:404` identifies S375 as an open-access PDF served from Ghent University's repository record. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md:410` identifies S381 as an OJS galley PDF on periodicos.unifesp.br and its article landing page on that same journal site; §3 of the spot-check admits S381 at `round-56-verifier-spotcheck.md:122`.

## Proposed append — preserve criterion 10's existing words

Append after the current final sentence on `corpus/QUALITY.md:37` (ending `ReviewCriterion10).`):

> Third-party journal or book scans served without stated permission are not ordinary public copies. Reviewer check: inspect the host page and the scan's provenance; accept only when the host page names a licence or permission covering the scan, or the copy is the publisher's, in the author's institutional repository, or the digitising library or archive's own scan; a university or library host alone does not establish permission. This clarification is grounded in R56-M4 (`corpus/lessons/round-56.md#mistakes`) and the discernment spot-check (`corpus/lessons/round-56-verifier-spotcheck.md`, §3).

## Application to the four round-56 cases

| Case | Result under proposed text | Why |
|---|---|---|
| Thornton 1991, `stono.pdf` | Fail | A JSTOR scan on a university library web host is not shown to be the library's own digitisation; the host stated no permission, and the JSTOR cover limited use to personal use. A university host name alone is insufficient. |
| Thornton 2001, `africankingdoms.co.uk` | Fail | The site is a third-party host; its CC BY 4.0 notice covers images only, not the journal scan, whose cover records a JSTOR download. No permission covering the scan or qualifying publisher/repository/library digitisation is recorded. |
| S375, Ghent repository | Pass | The source row identifies an open-access PDF served from Ghent University's repository record, meeting the institutional-repository route (rather than relying on a third-party host's domain alone). |
| S381, journal site | Pass | The source row identifies the article's OJS galley PDF and landing page on periodicos.unifesp.br, the journal's own site; this meets the publisher/journal-copy route. The round-56 spot-check independently records S381 as admitted. |

## Gates, surfaces, and limits

- This is a proposed policy addition, not a landed edit. No source, criterion, checker, test, build, or other product file was changed; only this report was written.
- No command or external request was run. The four-case application uses the round-56 records cited above, not a fresh re-opening of those hosts.
- The existing mechanical access check is not evidence of scan permission: criterion 10 itself says its checker sees only reported bypasses and leaves sample re-opening to a reviewer. The proposed host-page/provenance check is manual.
- No tools were installed. Out of scope: editing `QUALITY.md`, changing source rows, or independently adjudicating permissions beyond the recorded evidence.

Artifact: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/ScribeQuality10.md`.
