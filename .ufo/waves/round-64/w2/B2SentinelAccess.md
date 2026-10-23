# B2SentinelAccess — source-access safety

## Deliverable
Rulebook and audit: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2SentinelAccess/access.md`.

Grounding: `corpus/QUALITY.md` criteria 10/16 and hold/lift lines 51–53; round-51 S094 challenge incident and `.ufo/l0-questions.md:98`; round-62 `tools/reopen-row.py` safety hold; round-63 repair/independent-review lift and archive 403/429 incidents. The rulebook covers ordinary opens, “challenge met, not passed” records, exact same-page Wayback `14-digit timestamp + id_` form and evidentiary limits, private/loopback SSRF risk, need-only `reopen-row.py` use, fabricated/AI-generated body rejection, and a 10-item pre-filing checklist.

## Pre-filing checklist

1. Public source URL; no private, loopback, local, or internal target.
2. Repeatable plain request, permitted public copy, archive capture, or permitted library/archive scan only.
3. No CAPTCHA/bot challenge, paywall, login, or geo restriction passed or bypassed.
4. ACCESS records date, URL, method, exact result/status, and challenge indicator.
5. For an ordinary alternate route, record “challenge met, not passed” and its result.
6. Same-page archive capture follows the live URL and uses actual 14-digit timestamp plus `id_`.
7. Capture/quote is checked within the frozen locator budget and scoped to authentic body text.
8. Errors and retries are reported accurately; no inference of absence from one 403/429.
9. Run `tools/reopen-row.py` only if needed, never on private/local services or targets.
10. Verify genuine source body and scan/copy permission; fabricated/AI-generated bodies or unauthorized scans mean reject, file no row.

## Audit result

Grepped `ACCESS` lines and literal source hosts in all 19 inherited `row.txt` drafts under `/home/vgpnk/.cache/hyaku/kotodama-r64/`. **No confirmed access-policy violations**: no reported bypass/automation or private/loopback literal host. Each row also includes a `web.archive.org` capture. The full file-by-file host and ACCESS summary is in `access.md`; DNS resolution was not tested.

Two permission/provenance cases need resolution before filing, not a confirmed violation from the local evidence: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS730/row.txt` (`www.psych.mcgill.ca`) and `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS735/row.txt` (`www.ling.ohio-state.edu`) are direct PDFs whose ACCESS records establish only HTTP 200. Under criterion 10, a university host alone does not establish permission for a third-party scan; verify each is an allowed copy or do not file it. `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS724/row.txt` reports live HTTP 403 and an ordinary archive HTTP 200; it reports no bypass, but if the 403 was a bot challenge, ACCESS must say “challenge met, not passed.” S737's extra linked-PDF 404 does not affect the cited ERIC record, which the ACCESS line says opened normally.
