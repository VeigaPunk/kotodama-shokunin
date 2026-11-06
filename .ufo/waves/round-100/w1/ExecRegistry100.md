# ExecRegistry100

- lane: kotodama, round 100, wave w1. ONLY writer of `corpus/SOURCES.md` and `reports/round-100/evidence/` this round.
- Dependency: ScoutSources100 DONE (`ed78b2a636a22d00376fb05c6d010c46b1e8694b45c370755f79ddcba5a70f4a`) — `candidates.json` read.
- Tools: none installed or upgraded. curl 8.23.0 / pdftotext 26.10.0 / python3 3.14.8 pre-existing; pacman untouched.

## Appended rows (S1018–S1027, after S1017 at line 974 of corpus/SOURCES.md)

10 rows, candidate-key order C1, C2, C3, C4, C6, C7, C8, C11, C12, C17 -> S1018–S1027.
All: tier A/B, `mined`, opened `2026-11-06`, recheck `180d`, used-by exactly `corpus/knowledge/linguistics/work-song-labour-chant.md`.
Source cells carry the exact fetched URL. Anchor cells: `body text; reports/round-100/evidence/<S>.txt; exact locator: "<quote>"`.
No literal or escaped pipe in any cell; 11 cells each (verified programmatically).

## Re-verification (per admitted candidate)

Plain `curl -L --max-time 30 -sS` (default UA), one attempt each, all HTTP 200; attempts and fresh sha256 in
`evidence/manifest.json`. Whitespace-collapsed quote count == 1 in the shipped `.txt` for all 10.
Fresh sha equals scout sha for 8/10; C8 fresh PDF is 842805 bytes vs scout 842807 (source changed; quote still count 1);
C17 uses this seat's stdlib HTML strip (quote still count 1). Detail in `stage/ExecRegistry100/rows.md` appendix.

## Collision grep (before assigning)

`grep -cE '^ {0,3}\|[[:space:]]*S10(1[8-9]|[2-9][0-9])' corpus/SOURCES.md` printed `0`, rc=1 (no S1018+ rows pre-existed).
Each candidate URL was also checked absent from SOURCES.md before fetching.

## Counter (frozen predispatch.py, --base-rev 60010a55fb5f04ee728070c463b1a57ae1cc17fc)

Full output: `stage/ExecRegistry100/counter-c.txt`. Legs owned by this seat:

```
LEG C2 PASS rows=951 highest=S1027 new=10 qualifying=10 (min rows 945, highest >= S1021, qualifying >= 4)
LEG C3 PASS added=10 removed=0 in-place-status/recheck/used-by=0 illegal=0 []
LEG C7 PASS qualifying ids bound: 10/10 captures-verified=15 failures=[]
```

C3 shows `illegal=0` (append-only holds). Other legs: O0–O4 PASS (other seat's tool), C5/C8 PASS;
C1/C6/C9 fail until ScribeEntry100 and ReviewerC100 land; O5 (L1-owned) fails. C4 see census below.

## Census

`scripts/sources-census.sh validate --file corpus/SOURCES.md`; output saved in `stage/ExecRegistry100/census.txt`.
First run rc=1 with the ONLY errors being ten `E11 ... missing used-by corpus/knowledge/linguistics/work-song-labour-chant.md`
lines (the entry file is ScribeEntry100's surface and did not exist yet); W04/W01 warnings pre-exist and do not affect rc.
Final census rc=1 with every finding an E11 line for the not-yet-written entry path `corpus/knowledge/linguistics/work-song-labour-chant.md` (S1018–S1027, 10 lines); no other E-code. Per L1 ruling this is expected-pending: the entry is ScribeEntry100's surface and that seat waits for this DONE; the L1 re-runs census after the entry lands and counter leg C4 is measured then. Saved output: `stage/ExecRegistry100/census.txt`.

## Drop list

None. All 10 admitted candidates re-verified and written; `stage/ExecRegistry100/dropped.md` says so.

## Files written

- `corpus/SOURCES.md` (10 appended registry rows only)
- `reports/round-100/evidence/` (15 captures + `manifest.json`)
- `stage/ExecRegistry100/{rows.md, rows.json, rows.lines, census.txt, counter-c.txt, dropped.md, DONE}`
- this Report
