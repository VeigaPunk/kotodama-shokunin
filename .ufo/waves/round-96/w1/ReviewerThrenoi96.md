# ReviewerThrenoi96 — Report (round 96, w1, attempt 1, milestone r96-v1)

Judged axis: calibration. Seat: re-decide the round-95 reject of Thrênoi to Moirologia
(Oral Tradition 23/2, 2008) on content; check whether the access reason held. Non-author verifier;
no registry rows written (nomination only). Frozen files untouched; nothing committed.

## Work performed

1. Re-open, plain curl `-sS -L --max-time 30`, default user agent, ≤3 attempts with 20 s backoff
   (loop rc 0). Every attempt recorded:
   - Issue page https://journal.oraltradition.org/issues/23ii/ — attempt 1: curl rc 0, HTTP 200, 43010 B. No retries consumed.
   - PDF https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf — attempt 1: curl rc 0, HTTP 200, 302080 B (byte-identical size to the round-95 closure re-open). No retries consumed.
   - Two earlier dispatches of the same loops failed to start (scratch cwd race, harness start error): no HTTP request made; not counted as attempts.
   - Captures: stage/captures/R1-issue.html sha256 936d9e1ce9ad608d91efd0559aa45fdd45f979ccedfab3a01e4c18ebc895d6dc; captures/R1-article.pdf sha256 1e53dabf880576270d134fa285914b17c802d62ee84b159a72e535fc3fc5599a. pdfinfo (rc 0): Pages 29, Title "ORAL TRADITION 23.2 - Thrênoi to Moirológia: …", 302080 bytes (file(1)'s "8 page(s)" is wrong; pdftotext's full works-cited tail confirms completeness).
2. Extraction: pdftotext (poppler 26.10.0, preinstalled) rc 0 → 83367 B, 1497 lines.
   Located quotes (python3 bytes.count, rc 0; ≤25 words; each count 1):
   - Title line (7 words, count 1): "Thrênoi to Moirológia: Female Voices of Solitude," — the 3-word core occurs 2× (running head), hence the longer form.
   - Q1 (19 words, count 1): "the antiphonal structure and style of lament performance contribute to / social bonding among women; they mourn in a fugue."
   - Q2 (18 words, count 1): "Antiphonic reciprocity between women in the mourning ritual entails the intensive / interpenetration of collective and individual poetic creation"
   - Q3 (11 words, count 1): "the leader of the dirge (koriféa), twice widowed, asks her audience"
3. Access verdict: the round-95 access reason DID NOT HOLD — transient connection timeout (curl exit 28)
   misread as unreachable; both URLs answer 200 first-try on 2026-11-05 within the same 30 s budget.
   Matches the frozen claims.json frontier_step class (transient-timeout misread as unreachable).
4. Content decision: ADMIT-AS-CANDIDATE, tier A (peer-reviewed journal, publisher-hosted PDF, mined
   secondary synthesis with page-cited Seremetakis/Alexiou/Caraveli-Chaves). The lament entry
   funerary-lament-dirge-formulae.md (S970-S974) does not already cover it: grep -c -i -E
   "greek|maniat|maniot|kommos|seremetakis|alexiou|epiros|moirolog|thr[eê]noi|korif" = 2 (rc 0),
   both secondhand via S971 (entry lines 90, 157). Adds first-hand: moiroloyístra/koriféa
   professional-leader facet (entry §3) and kommos → Maniat moirológia antiphonal continuity (§4).
5. Re-opener class check (code read; not run against the registry): transient rule = 429/5xx/expired
   30 s budget/connection error → TransientFetch, ≤3 attempts per URL per pass, min(gap,5) s apart,
   ≤3 passes (gap 60 s default). curl exit 28 maps to TransientFetch → would have been retried, never
   UNREACHABLE. LOCATED for the PDF URL: NO — non-HTML bodies are matched as raw text (split_content,
   lines 350-361), so the 200 PDF yields ABSENT, not LOCATED; LOCATED requires an HTML-visible anchor
   (an issue-page-anchored row would be LOCATED today). UNREACHABLE was the wrong class either way.
6. Nomination to ExecRegistry96 (writer of S975+): future row for the PDF URL with anchor quotes Q1/Q2,
   tier A mined, used-by funerary-lament-dirge-formulae.md, capture under reports/round-96/evidence/.
   Flip condition: a later full bounded re-open (3×3) timing out on all row URLs on a different day
   reinstates the reject, class access-transient.

## Trend verdict

Supports the frozen claims.json frontier_step: the round-95 reject is a confirmed transient-timeout
misclassification; the QUALITY.md rule (reject-by-access must pass tools/reopen-row.py first) would
have prevented it. No defect found in the re-opener's retry rule; its one blind spot (PDF bytes are
never text-matchable → ABSENT, not LOCATED) is a verdict-precision limit, not an access error, and is
documented here for the row writer to anchor on the issue page if HTML confirmation is wanted.

## Tooling record

Installed: none. pdftotext/pdfinfo poppler 26.10.0 already present. pacman untouched (host pause
respected). No sysctls touched. No model routing touched.

## Files written

- .ufo/waves/round-96/w1/stage/ReviewerThrenoi96/decision.md (main output; DONE carries its sha256)
- .ufo/waves/round-96/w1/stage/ReviewerThrenoi96/captures/R1-issue.html, captures/R1-article.pdf
- .ufo/waves/round-96/w1/stage/ReviewerThrenoi96/DONE (last)
- .ufo/waves/round-96/w1/ReviewerThrenoi96.md (this report)

Scratch /fast/scratch/hyaku/kotodama-r96/ReviewerThrenoi96/ deleted before yield. No blockers.
