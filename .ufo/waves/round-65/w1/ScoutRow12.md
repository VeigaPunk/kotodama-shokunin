# ScoutRow12 — S772/S773

## Observed

- **S772 — sumo ritual grammar (high confidence).** Draft: `.ufo/waves/round-65/rows/ScoutRow12/row-S772.txt`. The Japan Sumo Association’s official English introduction describes the yokozuna’s *dohyoiri*: clapping to attract the gods, arms and palms, and stamping that symbolically drives evil from the ring. The 25-word anchor is present in the PDF body (p. 5). `curl -L` returned HTTP 200, zero redirects on 2026-10-24. Wayback CDX lists HTTP 200 capture `20250524064848` for the identical original URL.
- **S773 — patolli betting and evidence calibration (high confidence for this scope).** Draft: `.ufo/waves/round-65/rows/ScoutRow12/row-S773.txt`. Fitzmaurice, Watkins & Awe’s UCL *Papers from the Institute of Archaeology* article states that gambling was associated ethnohistorically with patolli; the quote appears in the article body (PDF p. 8). Its first page identifies the paper as double-blind peer-reviewed and CC BY 4.0. The article also says bean throws could have determined piece movement, warns about moralising colonial accounts, and treats Maya-board functions as context-dependent interpretations. `curl -L` returned HTTP 200, zero redirects on 2026-10-24. Wayback CDX lists HTTP 200 capture `20260711144621` for the identical original URL. **Metadata wrinkle:** the landing page says volume 31(1), while the PDF’s citation block says 30(1); the DOI is the same.

## Inference and remaining unknowns

- The sumo source is strong evidence for the Association’s account of ceremonial sequence and meaning, not independent proof that every modern gesture is unchanged from antiquity.
- The patolli paper supports the gambling association and cautions against generalizing from later Aztec testimony to Maya contexts. It does not establish one complete ancient ruleset or prove that every Maya board served the same game/function. Any specific race mechanics should remain qualified or receive a separate source.
- The bullets are drafts for the L1 to re-check against the frozen row predicate and entry context.

## URL uniqueness grep

Searched each literal live URL against `corpus/SOURCES.md` and the complete `.ufo/waves/round-65/rows/` tree. Before writing these rows, both searches returned **No matches found**. After writing, the Sumo URL matched only `row-S772.txt`, and the UCL URL matched only `row-S773.txt` (each appears on its `ROW` and `CAPTURE` lines); neither matched `SOURCES.md` or another fragment.

## Rejected lead

`https://otagomuseum.nz/athome/how-to-play-patolli` is recorded in `rows/ScoutRow12/rejects.txt`: direct curl returned HTTP 403, preventing current live-body verification. CDX does list historical captures, but the peer-reviewed UCL article better serves the historical-evidence and calibration scope.