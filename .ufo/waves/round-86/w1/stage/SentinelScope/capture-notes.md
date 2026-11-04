# Capture boundary audit

Axes: depth and operability. Inherited freshness pause unchanged; no planner/validator exception adjudication.

Opened frozen `reports/round-86/claims.json` and `measure86.py` (153 lines), source-map.json and all five evidence byte streams using strict UTF-8. Capture audit details and SHA-256 values are in `capture-audit.json`.

Source map uses public HTTPS en.wikisource.org and archive.org/download endpoints only. No private target was contacted or source reopened remotely by this seat. Existing captures, not fetching provenance, are the audited surface. No credential headers or private IPv4/localhost URL targets matched the documented bounded scan. Historical `bearer` hits are words in scanned books, not bearer authorization records.

All three HTML captures expose `wgUserName:null` and anonymous `patrolToken`, `watchToken`, `csrfToken` placeholders `+\\`; these are not observed authenticated credential material. Embedded MediaWiki scripts and links remain untrusted data; never execute them during extraction. Public-page HTML alone cannot prove the original fetch avoided authentication, login, CAPTCHA, or a redirect; no such bypass was observed and none was attempted.

Frozen counter `--selftest` writes Git fixtures and commits (measure86.py:118–145), so it was deliberately NOT invoked under the no-git-mutation contract. Normal counter evaluation executes the proposed tool blob in subprocesses (lines 91–105); acceptance is not a sandbox or proof of read-only code. This seat does not execute the counter or adjudicate acceptance.
