# Round-81 counter/config revisions

| what | old | new | moved? | receipt |
|---|---|---|---|---|
| claims.json re-freeze: claim C `tool_markers` `SELFTEST: PASS` -> `SELFTEST:` | freeze `b1ebb6097e3a269c2dc53fe73d5ea07316c7bd25` | the re-freeze commit (supersedes `b1ebb609` for grading; it is itself the graded lands commit) | no predicate moved - the marker list is a source-byte check, and the over-specified literal appears only in the checker's runtime output (`SELFTEST: PASS` printed by `--selftest`), not in its source bytes; the tool bytes are unchanged, `tool_sha256 e99658df...` unchanged | red-before: `telemetry/lands-c81-graded-r1-TOOL-marker.txt` (first graded run at lands `4ad08c83`, freeze `b1ebb609`: `LEG FAIL TOOL (marker missing: 'SELFTEST: PASS')`, `ACCEPT-C-81: FAIL legs=4/6`, exit 1); green re-run: `telemetry/lands-c81-graded-r2.txt` |

Selftest receipts were re-run after the re-freeze only where the counter bytes
changed: no counter byte changed (the counters were never edited after the
first freeze), so the committed selftest receipts (`selftest-o81.txt`,
`selftest-c81.txt`, `selftest-d81.txt`) stand.
