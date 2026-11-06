# kotodama round 100 — lesson

L1 KotodamaR100 (hyaku run 15, attempt 1). Base `60010a55fb5f04ee728070c463b1a57ae1cc17fc`; freeze
`255d84776c12c918b7bfb2a7173d7b495e3f966e` (`reports/round-100/claims.json`, counter `reports/round-100/predispatch.py`,
battery100 + pin + base and feasibility receipts + forgery controls, all committed before any seat ran). No earlier
attempt of round 100 (`.ufo/watchdog.log` has only the attempt-1 launch line).

Claims:
- **O (operability, capability).** `tools/check-table-support.py`: for a table whose caption claims recorded cases, each
  row is bound to its sources by the paragraph under the table and each cell must have 3/4 of its content stems inside
  one 80-token window of one bound capture (closes round-99 closure R2 / lesson R99-M2).
- **C (coverage).** `corpus/knowledge/linguistics/work-song-labour-chant.md` on rows S1018–S1027.

## Controls before data (freeze commit)

| control | what it skips | result |
|---|---|---|
| do-nothing (`reports/round-100/predispatch-base.txt`) | all work | FAIL legs=4/15 |
| F-O-ALLCLEAN | all checking | battery100 fail 19/28 |
| F-O-NOWORD | cell support (id-presence checker) | fail 7 (F1 F6 F7 F9 F11 F13 T2) |
| F-O-ANYWHERE | co-location (word presence anywhere) | fail F11 |
| F-O-UNION | row isolation | fail F6 |
| F-O-WIDE | caption scope (any "recorded") | fail benign B7 |
| P-O-FEAS (L1 reference) | nothing; feasibility | battery 28/28; counter O0/O2/O3 PASS, O1 FAIL (no selftest) |

Calibration before freeze: a first all-words-co-located rule flagged 29/36 praise cells and did NOT separate the forged
R99-M2 cell from the real one (both flagged); a presence-anywhere rule passed the forged cell (Finnegan's whole book holds
"property"). The frozen 3/4 rule separates them (forged 4/7 flagged; real cell 5/6 clean). Recorded so a later round does
not re-derive it.

## Mistakes

### R100-M1 — a uniform seat-report path stated without enumerating the seats (round 99)

- Class: a report states a property of every seat output ("each seat writes `w1/<Seat>.md`") from the spec, not from
  the files.
- Evidence: `corpus/lessons/round-99-verifier-spotcheck.md` §1 defect D1 (ReviewerC99's report only at
  `w1/stage/ReviewerC99/review.md`).
- Captured-by: none.
- Fix: `reports/round-100/seat-report-paths.py --spec <wN-spec.json> --wave-dir <dir>` enumerates every spec seat and
  tests `<Seat>.md`; shown able to fail on round 99: `reports/round-100/seat-reports-r99-control.txt` →
  `SEAT-REPORTS: 11/12 present`, rc 1. Run on round 100 before the report: `reports/round-100/seat-reports-r100.txt`.

### R100-M2 — a frozen design deadlock between two seats (round 100, this round)

- Class: ExecRegistry100's acceptance required census rc 0, but the census refuses (E11) a used-by path that does not
  exist until ScribeEntry100 writes it, and ScribeEntry100 waited on ExecRegistry100's DONE.
- Evidence: `.ufo/waves/round-100/w1/stage/ExecRegistry100/census.txt` (E11 on S1018–S1027); the L1 broke the wait by
  a message ruling census E11-pending acceptable; C4 then passed after the entry landed (`predispatch-lands.txt`).
- Captured-by: none (round 99 had the same ordering and its seat happened to finish).
- Fix: a registry item's acceptance names census E11-for-the-pending-entry as expected; the L1 measures C4 after the
  entry lands. Not yet shown able to fail by a gate.

### Routed content defects found by reading (CriticC100), repaired before landing

F1 unmarked universal ("in each") over ten sources, F2 self-contradiction about Bücher's scope, F3 dropped hedge
("seems to have been" → "was", S1022), F4 duplicated §12 paragraph — all repaired in the entry by the L1. F5: three
registry `teaches` cells overstate (S1026 "earliest", S1022 "only", S1021 "cooper" for Kessler/coppersmith); not
repaired this round because C3 freezes the `teaches` cell; the entry repeats none of them. Routed to round 101.

## Gate

Rows S1018–S1027 were opened by ScoutSources100, re-verified by ExecRegistry100 and re-opened by ReviewerC100
(`.ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json`: 10/10 http 200, quote count 1). Quotes, URLs, capture
sha256s and attempts are in `reports/round-100/evidence/manifest.json`; the registry anchor cell of each row carries its
located quote (≤25 words, count 1 on the whitespace-collapsed capture). All ten rows: absent → mined, opened
2026-11-06, recheck 180d, used-by `corpus/knowledge/linguistics/work-song-labour-chant.md`. No existing row's status,
recheck or used-by changed (C3 in-place=0). No row added then superseded.

Admits sampled for the closure: S1022 Collinson, oyster dredging songs (Scottish Studies, tier A); S1020 Slave Songs of
the United States 1867 (primary, tier A).

Rejected (ScoutSources100 `candidates.md` §3, full records in `candidates.json`): C5 EB1911 "Chanty" on Wikisource
(404 ×3; flip: a scan-backed transcription); C9 loc.gov work songs (403 wall); C10 britannica.com (403 wall); C13 Roos,
JEOL 47 (503 ×4; flip: host recovers — would be tier A); C14 Smithsonian Gunderson essay (403); C15 Merzeban (connection
error ×4); C16 ARCE Naga pounding song (403); Gioia *Work Songs* not opened (copyright; no open edition).

Re-judged (routed R3): Encyclopaedia Iranica "Courts and Courtiers x. Court poetry" (round-99 C6). ScoutRejudge100:
24 requests over 14 minutes, all HTTP 403 Cloudflare managed challenge (`cf-mitigated: challenge`), host-wide; no
bypass. Rejection stands on the access reason; this disagrees with the round-99 closure's recorded HTTP 200 from its
host, so the flip condition is a re-measured 200 from this host or an open `id_` capture
(`.ufo/waves/round-100/w1/stage/ScoutRejudge100/verdict.md`).

Search: ScoutSources100 ran its query log in `candidates.md`; stop rationale there. No claim to exhaustive coverage.

Outside discernment spot-check: pending the orchestrator's non-author closure.

Assimilation: none (no shokuknow package adopted). `considerthese/` is absent. No `corpus/lessons/operator-*.md` files.
