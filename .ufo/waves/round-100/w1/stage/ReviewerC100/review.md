# ReviewerC100 — independent non-author review of claim C (round 100)

Seat: ReviewerC100 (coverage attack). Entry author: ScribeEntry100; registry/evidence: ExecRegistry100.
I am not an author of the entry, the registry rows or the manifest; everything below was re-derived
from the frozen counter bytes, the landed tree, and fresh network fetches.

## 0. Method

- Read the frozen counter `reports/round-100/predispatch.py` (583 lines) and `claims.json` first; C legs C1-C9 judged on the frozen bytes only.
- Re-opened EVERY qualifying row (10: S1018-S1027) with plain `curl -sL --max-time 30` from the exact URL in the registry `source` cell, into scratch, converted as the captures were (pdftotext for PDF URLs, tag-strip only for real HTML, plain text kept as-is), whitespace-collapsed, manifest quote counted in the fresh text.
- No LSP server answered for this lane (markdown corpus, no lsp device in this session); all checks are byte/command-level. Recorded as a tooling limitation, not silent grep-as-proof.
- Scratch: /fast/scratch/hyaku/kotodama-r100/ReviewerC100/ (deleted before yield). No writes outside my stage + this Report.

## 1. Re-open table (leg C9 input; full machine form in stage/ReviewerC100/reopen.json)

All 10 qualifying rows re-opened (not just the 3 the counter requires):

| id | http | fresh sha256-12 | manifest capture match | quote_count (fresh) | attempts |
|---|---|---|---|---|---|
| S1018 | 200 | f51fe9f0f6a7 | == S1018.txt | 1 | 1 (200) |
| S1019 | 200 | 3e55e9ac9cea | == S1019.txt | 1 | 2 (302+timeout28, then 200) |
| S1020 | 200 | 4f1b337df7fd | == S1020.txt | 1 | 4 (302+timeout28 x3, then 200) |
| S1021 | 200 | 65a63dfffa9a | == S1021.txt | 1 | 2 (302+timeout28, then 200) |
| S1022 | 200 | 6484fba38028 | == S1022.pdf | 1 | 1 (200) |
| S1023 | 200 | d3c4a9a97e2e | == S1023.pdf | 1 | 1 (200) |
| S1024 | 200 | e7ce572e6984 | text identical; 2 B differ | 1 | 1 (200) |
| S1025 | 200 | 3a5ed52bc060 | == S1025.pdf | 1 | 1 (200) |
| S1026 | 200 | 76deafbaf013 | == S1026.txt | 1 | 1 (200) |
| S1027 | 200 | adbe4952c9df | same size; 114 B differ | 1 | 1 (200) |

Fresh-vs-manifest differences explained:

- S1024 (UCD repository PDF, 842805 -> 842807 B): exactly one FlateDecode stream (object 1167, /Length 886 -> 887) re-serialized server-side near EOF; extracted text identical (quote found once). Same document, not a silent content change.
- S1027 (SIL Philippines HTML, 43071 B both): all 114 differing bytes are inside the per-request CDN link id + timestamp (`cdn-cgi/content?id=...-1793966160.36794` -> `...-1793968616.66784`). Content otherwise byte-equal (quote found once).
- PDF rows: fresh raw bytes equal the manifest `.pdf` capture; the manifest also stores a pdftotext `.txt` whose sha differs from raw by construction.
- S1020 needed the full retry budget (criterion-38: initial + 3 retries, 20 s backoff, every attempt recorded; archive.org datanode hung twice, 200 on attempt 4).
- Conversion note: my first driver tag-stripped the plain-text djvu captures and mangled OCR noise; fixed by content-sniffing (the manifest captures for text URLs are the raw bytes — the correct convention). No lane file was touched by this; scratch only.

`quote_count 1` was observed in fresh bytes for all 10; `http 200` observed for all 10. Nothing was written on assumption.

## 2. Frozen counter run (C1-C9) and verdict

Run after reopen.json existed (frozen bytes, `python3 -B reports/round-100/predispatch.py --root <lane> --work <scratch>/counter --base-rev 60010a55…`, rc=1, 183 s; full output at stage/ReviewerC100/counter.txt):

| leg | result | detail |
|---|---|---|
| C1 | PASS | bytes=41933 h2=12 table=21x3 phrases=6/6 topic-line=equal |
| C2 | PASS | rows=951 highest=S1027 new=10 qualifying=10 |
| C3 | PASS | added=10 removed=0 in-place=0 illegal=0 (pure append) |
| C4 | PASS | census rc=0 |
| C5 | PASS | CORPUS-INDEX: OK files=272 rows=272 findings=0 |
| C6 | PASS | qualifying ids cited in entry: 10/10 |
| C7 | PASS | 10/10 bound, captures-verified=15 failures=[] |
| C8 | PASS | files scanned=272 other owners=0 |
| C9 | PASS | 10 qualifying ids re-opened with count 1 (min 3): S1018-S1027, from my reopen.json |

(O legs on the same run: O0-O4 PASS — selftest 40/40, battery 28/28, R99-M2 replay exact {(UNSUPPORTED-CELL, Yoruba, limit on the praise)}, mutation 36/36 — and O5 FAIL: scorecard-capability-rows=0, skill-mentions=2. O5 is claim O's registration leg, not judged by this seat.)

**Counter verdict for claim C: PASS — legs C1-C9 all PASS; first failing leg of claim C: none.**
Overall PREDISPATCH-100 on this run: FAIL legs=14/15, driven solely by O5 (claim O).

## 3. Sentence-support table (does the source support the sentence, not merely the topic?)

58 citation markers `(S10xx)` in the entry, one per sourced sentence. Every marker's load-bearing
specifics were probed against the capture it cites (39 probe groups; full hit counts in scratch
support_probe.py run):

- supported: 58/58. No bullet rests on the topic alone; none is unsupported.
- weak (supported with a loose paraphrase, flagged for honesty): 2 —
  - §4 (S1025) "when serious rowing declined" paraphrases "few people do any serious rowing that is not for sport or leisure" — same fact, looser words.
  - §6 (S1020) "a hundred lashes" normalizes the capture's "a hundred lash"; "a rower describes" — the account sits in the rowing chapter (capture footnote "For another curious circumstance in rowing") though the narrator was toting rice.
- unsupported: none. Every named figure (16-30 strokes/min, 24 average, 25-30, max 46, eight minutes, two and a half miles inland), quoted phrase ("worth his weight in gold", "couple of extra hands", "tags", "Hog-Eye Man", "unprintable", "work it in", "made a sing, just puttin' a word") and structural claim (alternating vs uniform rhythm; precentor = foreman; psychological moment; no song sung twice; simulated waulking on Barra; dreg-song scope; two-types-unverified Collinson suggestion) locates in the cited capture. The German S1021 claims locate exactly: "entweder reine Chorgesänge oder Wechselgesänge; bei letzteren ist der Vorsänger zugleich auch Vorarbeiter", "bei den Arbeiten im Gleichtakt geradezu wie ein fortgesetztes Kommando".
- Attribution check: no sentence's id points at the wrong source; cross-checked the two near-duplicate shantyman descriptions (Terry S1018 vs Sharp S1019 phrasings kept distinct).

## 4. Naturalness, non-canon, PROVINCE, README, supersede

- Phrase hits natural: all six frozen phrases land in `## ` h2 headings that carry content (§2 "What a work song is", §3 "The song leader, the call and response", §4 "Work rhythm and the task: hauling song, ...", §5 "The shanty and other occupational repertories"), plus natural table hits (§7 header "song leader and crew", data row "hauling shanties"). No phrase was stuffed into an empty cell or a heading that does not govern real content. 6/6 >= 4 required.
- §7 table cells are deliberately telegraphic ("cells restate what its capture says"); each restatement was spot-verified against its capture (hauling/capstan/Sea Islands/waulking/oyster/iorram rows all reduce to capture facts). Readability cost, not a defect: the legend line and binding lines below the table make the compression decodable.
- Non-canon: worked example tagged **NON-CANON**; design material tagged *design, not sourced*; §1 states "no canon (lore-shokunin), and no research method (chousa, `PROVINCE.md`)"; §11 handoff gives lore-shokunin the decision rights. PROVINCE deferrals present: sound production -> audio-shokunin, canon -> lore-shokunin, source-grading method -> chousa.
- README edit: `corpus/README.md` adds the index line in filename order (between verbal-duelling and writing-systems), `## linguistics/` 44 -> 45, new changelog block "Round 100 work song entry (2026-11-06)" with totals 271 -> 272 and the per-round footer convention (19 historical footers before it, 20 now) — matches precedent exactly.
- Same-round supersede: none of the 10 new rows' `teaches` contains "supersedes" (count 0); registry diff is pure append (10 insertions, 0 deletions — C3 will confirm).

## 5. Defects found (non-leg)

1. §12 Inference ledger: the lead paragraph is duplicated verbatim, back to back ("The readings listed here are mine; ..." twice). Mechanical copy-paste slip; cosmetic, no leg reads it.
2. Entry line 3 says "- source: corpus/SOURCES.md (the registry rows below, one id per line)" while line 4 says "- sources:" with the id list — the singular `source:` line is redundant legacy phrasing. Cosmetic.
3. S1020 fetch needed 4 attempts today (archive.org slowness, recorded above) — a freshness hazard for future re-opens of that row, not a claim defect.

None of these fails a frozen leg.

## 6. Verdict

**PASS — claim C holds on this counter run: C1-C9 all PASS, no failing leg.** The entry, the ten
registry rows, the evidence binding and the non-author re-open survive attack: fresh fetches
reproduce every capture (two byte-drifts explained as server-side re-serialization and CDN nonce,
content identical), all 58 citations locate in their captures (2 loose paraphrases flagged),
phrases are natural headings/cells, append-only and README conventions hold, no same-round
supersede. The overall counter is FAIL 14/15 only because O5 (SCORECARD capability row — claim O
surface) had not landed when I ran it; that is outside claim C and outside this seat.

Advice to the L1 (recommendation, not a claim edit): re-run the counter after the O5 SCORECARD row
lands; C9's input file is committed at `.ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json`
(sha256 printed on the stage DONE line) and needs no regeneration.

## 7. Residual risk and verification gaps

- C7 binds bytes, not truth: the counter cannot detect a fabricated capture. My fresh re-fetch closes this for all 10 rows today (fresh shas equal or content-explained above) — the strongest anti-forgery check available to this seat.
- My conversion for text URLs is byte-exact; for PDFs it is the same pdftotext binary as the captures', so count parity is meaningful, not incidental.
- I did not re-audit O legs (outside seat); O3's praise-entry repair (ScribeTable100) touched `corpus/knowledge/linguistics/praise-poetry-panegyric.md` — the Yoruba row label/header/limit-cell invariance is O3's leg to guard, not mine.
- archive.org rows (S1019-S1021, S1026) may hang again for future verifiers; the registry `recheck` cells (on-release / 365d) govern that, not this review.
