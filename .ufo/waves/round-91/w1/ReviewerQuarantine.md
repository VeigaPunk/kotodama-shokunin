# Round-91 w1 — ReviewerQuarantine report

Role: independent re-check of seven quarantine rows (fetch first, compare later).

## Files written (stage dir)
- `.ufo/waves/round-91/w1/stage/ReviewerQuarantine/independent-verdicts.json` — my seven rows: S776 S786 S804 S814 S816 S825 S835 (id, url, http_status, bytes, sha256, fetched_at, fragments, verdict, note), executor-compatible shape.
- `.ufo/waves/round-91/w1/stage/ReviewerQuarantine/agreement.md` — per-row comparison against ExecQuarantineA/verdicts-A.json; ExecQuarantineB absent (stage dir does not exist), comparison stopped there per seat spec.

## Method
- Read only `reports/round-91/quarantine/slice.tsv` from the register (single file, no other register file opened).
- One `curl -sS -L --max-time 40` per URL (no browser, no challenge passing).
- Normalization: tags→space, entities decoded, U+00A0/U+2003→space, NFKC, whitespace collapse, casefold. Cited quote split on `…` and `...`; fragments ≥ 6 chars tested as casefolded substrings.
- PDF rows via pdftotext (system binary, /usr/bin/pdftotext — no install needed; no tool installs were performed at all this run).

## My verdicts
| id | http | bytes | verdict |
|----|------|-------|---------|
| S776 | 200 | 24058 (sha ed148929…) | PARTIAL — 4/5 fragments located; `标准状态：现行` span absent |
| S786 | 200 | 753374 (sha 19eb1dc1…) | PARTIAL — English title line located in pdftotext; Chinese fragment absent from English deck |
| S804 | 200 | 212285 (sha d6155814…) | LOCATED — exact sentence present (half-width comma variant matches after normalization) |
| S814 | 403 | 162 (sha 1d08335e…) | UNREACHABLE — bare nginx 403 body; timed-out attempt on first hit (`curl (28)` after 40001 ms) then 403 on retry of the exact http URL |
| S816 | 200 | 48536 (sha a3b6640c…) | ABSENT — page loads (爱潜水的乌贼 interview) but quote (`资深读者`) not in body |
| S825 | 200 | 311308 (sha 204b7188…) | PARTIAL — era table content present in order but interleaved with `選択` UI tokens; exact spans absent |
| S835 | 503 | 690 (sha 48c30ea0…) | UNREACHABLE — repository maintenance page (offline since 2026-10-28), both attempts |

fetched_at: 2026-11-05T11:08:34Z … 11:09:50Z window, timestamps recorded per row in independent-verdicts.json.

## Commands run and rc
- mkdir -p stage, scratch: rc 0
- 11 curl fetches (incl. S814 first-attempt timeout rc 28, S786 https retry rc 0, S814 retry rc 0 with 403 body captured, S835 retry rc 0 with 503 body captured)
- pdftotext on S786: rc 0, 42,991 chars text
- python3 fragment tests ×6 batches: rc 0
- copy verdicts into stage dir: rc 0

## Agreement summary (see agreement.md for per-row detail)
- My fetches completed BEFORE opening verdicts-A.json (last fetch 11:09:50Z, file read 11:17Z UTC window).
- Overlapping rows with A (covers up to S804 only): S776 agree (PARTIAL/PARTIAL; A matched 2/5 only because backtick-wrapped fragment strings from the TSV poisoned its substring search); S786 DISAGREE (A: ABSENT; I locate the English title fragment at offset 79 of the pdftotext extraction — same bytes, same sha256 19eb1dc1…); S804 DISAGREE (A: ABSENT; I locate the exact Kotobank sentence at offset 61573 after normalization — same sha256 d6155814…).
- ExecQuarantineB: stage dir did not exist at 11:11:20Z, at 11:14:23Z (after 180 s wait), nor at comparison time → per seat spec, B comparison stopped with "does not exist yet" statement; no B evidence consulted.
- Rows S814/S816/S825/S835 are not present in A's file; only my own independent checks stand for them.

## Residual risk / gaps
- S814: first attempt timed out at 40 s (curl rc=28) before the retry returned a clean 403 body; verdict rests on the retry, fully evidenced.
- S786 Chinese fragment and S776 status-field span: absent under normalization I ran; a renderer with different stride could in principle differ, but the mixed-language citation for S786 is not in a same-language deck so absence is substantive, not decode-artifact.
- No access to executor B; if B lands later its verdicts remain unchecked by me (spec said stop).

Report trailer path (relative to lane root): `.ufo/waves/round-91/w1/stage/ReviewerQuarantine/`
