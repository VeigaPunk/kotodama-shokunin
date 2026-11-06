# ExecRegistry98 — Report (round 98 w1)

Scoped work: registry rows + evidence + S992 correction. Detail: `.ufo/waves/round-98/w1/stage/ExecRegistry98/rows.md`, `s992.md`, `dropped.md`, `census.txt`, `counter.txt`.

## Appended rows
- S994–S1004 (11 qualifying, candidate-key order C1,C3,C9,C10,C11,C12,C13,C15,C16,C25,C26; tiers A×6, B×5) + S1005 (S992 supersede, tier B) appended after S993; 11 cells each, no pipes.
- Collision: `grep -cE '^ {0,3}\|[[:space:]]*S99[4-9]' corpus/SOURCES.md` → 0 (rc=1) before write; `grep -c -F "<url>" corpus/SOURCES.md` → 0 for all 11 URLs.
- Re-verification: each URL re-fetched `curl -sS -L --max-time 30` → http 200, 1 attempt, rc=0; quote ws-count 1 on each fresh .txt capture; sha256s bound in `reports/round-98/evidence/manifest.json` (12 entries, 18 captures incl. S1005.txt sha e356cd7d…).
- Dropped: none (11/11; dropped.md).

## S992 correction (s992.md)
- Re-opened 37985-0.txt: http 200, bytes 1203657, sha e356cd7d2e57677d48413768956fa9b517ed8f28d9ff8ff63b3651cfa0893066, quote ws-count 1. Census E04 exempts supersede rows (teaches regex), so no fallback.
- S992 in place: status mined→queued, used-by verbal-entry→—. Verbal entry diff: 4 tokens S992→S1005 only.

## Numbers
- Census: `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` rc=0 (census.txt).
- Counter: `python3 -B reports/round-98/predispatch.py --root … --work /fast/scratch/hyaku/kotodama-r98/ExecRegistry98/counter --base-rev bcf664aa…` rc=1 (final, after entry landed); C3 line `LEG C3 PASS added=13 removed=1 in-place-status/recheck/used-by=1 illegal=0 []`; C7 line `LEG C7 PASS qualifying ids bound: 11/11 captures-verified=17 failures=[]`; full log counter.txt shows C1,C2,C4,C5,C6,C8 PASS; O3 FAIL (mutants98.sha256 missing — not this seat), C9 FAIL (reopen.json missing — ReviewerC98 owns it); 13/15 total.
- Pre-entry intermediate (census-pre-entry.txt, counter-pre-entry.log): census rc=1 E11×11 only; C3 already illegal=0, C7 already 11/11 — E11 cleared once ScribeEntry98 landed entry.

## Tools: none installed. Host/pacman untouched.
