# ReviewerC97 — round 97 claim C review (independent, non-author; edited nothing in the lane)

Detail: stage/ReviewerC97/review.md (support table, quote recounts, findings). Counter output: stage/ReviewerC97/counter.txt.

## Frozen counter (read-only)
- Command: `python3 -B reports/round-97/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work /fast/scratch/hyaku/kotodama-r97/ReviewerC97/counter --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569`, rc=1.
- Before the dependencies landed the same command gave `PREDISPATCH-97: FAIL legs=4/13` (rc=1), identical to predispatch-base.txt.
- Final: `PREDISPATCH-97: FAIL legs=12/13`. Claim C legs **C1–C8 all PASS** (C1 bytes=37387 h2=13 table=7x6 phrases=6/6; C2 rows=917 highest=S993 new=9 qualifying=8; C3 removed=0; C4 census rc=0; C5 index rc=0 files=269; C6 8/8 cited; C7 8/8 captures; C8 other owners=0). O0, O1 (155/155), O2 (survivors=0 unnamed=0 refused=31), O4 (34/34) PASS. O3 FAIL only because `reports/round-97/controls/mutants97.sha256` has not landed (MutationTester97 still running). Claim O not judged here.

## Re-open of admitted sources (plain curl -L --max-time 30, user-agent `curl/8`; criterion-38 retries not needed)
- Each fetch: attempt 1, http 200, rc 0.
- S989 (pdf): fresh sha256 8a59f531…4292 = lane capture sha. Quote recount: 1 (ws-normalised, pdftotext).
- S992 (txt): fresh sha256 e356cd7d…3066 = manifest sha. Quote recount: 1.
- S993 Threnoi source (pdf): fresh sha256 1e53dabf…5599 = lane capture sha. Quote recount: 1.
- Round-96 S975 (raw): fresh sha 33c896a6…a8f2 = manifest raw_sha256; quote 1.
- Round-96 S984: drift (1157108 → 1157112 bytes; sha f008c784…5538 ≠ pinned 4c62ddf7…e815). Text quote still 1; raw-HTML count 10. Pinned text capture unaffected.

## Quote recount on the lane captures
- 25 quoted fragments in the 16 cited sentences plus the funerary S993 sentence: 24 count 1 (raw and whitespace-normalised). 1 fragment, "judgement" (S986, line 97), count 0: the source reads "judg- ment" (OCR) and spells "judgment".

## Support table (16 cited sentences in the new entry)
- Supported: 12 (lines 37, 44, 48, 64, 66, 68a, 70, 85, 95a, 116, 128, 137).
- Weak: 2 (line 68b: "not invited" is an inference, though "a place and a seat" is in S987; line 135: "next round" where S990 says "final round").
- Unsupported or contradicted: 2 (line 95b: "use among the Polar Eskimos" is a murder-case aside in S986, not song-duel use; line 97: "may be carried on for days at a time" contradicts S986 "for years"; the "named office" and "named judge" are absent from the capture).
- Funerary S993 sentence (in funerary-lament-dirge-formulae.md): contradicted. S993 says the Maniat thrínos "holds no association with professional mourners"; "Maniat lament of Epirus" misplaces Maniat (Inner Mani, Peloponnese).
- §8 table: Inuit song duel "a judge inside the contest" contradicted (applause decides); Norse senna cells, Scottish flyting adjudicator and ritual-insult row (Pagliai 2009) unsupported by their named sources.
- Registry S993 row: "names the professional dirge leader" contradicts its own source.

## Other checks
- Phrase hits: 6/6 natural, each in an h2 heading (verbal duel, ritual insult, flyting, song duel, boast formula, audience adjudication).
- Topic line byte-equal (C1).
- Non-canon: 2 NON-CANON markers; canon deferred to lore (§1 line 27, §12 lines 253–255). The entry does not cite lore-shokunin/PROVINCE.md, which sibling entries do. Non-blocking.
- README edit (corpus/README.md): correct. linguistics 41→42, row filename-ordered, footer 268→269, directory totals sum to 269.
- Funerary edit: `git diff 1ffc5a83… -- corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` (rc=0): exactly one added paragraph (blank line plus one sentence). Only that change; the sentence is the contradicted one above.
- Manifest defect: captures[].file for S985–S992 name nonexistent files (pagliai_2009.txt etc.); C7 passes by id prefix only.
- Uncommitted: corpus/QUALITY.md 6-line modification (not claim C; not reviewed).

## Verdict: claim C
- Frozen legs C1–C8: **PASS (8/8)**. No frozen leg fails.
- Reviewer verdict on sourced coverage: **FAIL**. First failing item: **line 97** (song-duel "days at a time" vs S986 "for years"). The first failing leg is **none**: the frozen counter checks presence, not support.
- Required before accepting claim C as sourced: correct line 97 (days/years, named office, named judge, "judgement" quote), line 95b (Polar Eskimo use), line 135 ("final round"), the §8 table cells, the funerary S993 sentence (professional office, Epirus), and the S993 registry description. Lane content edits for the L1; this seat edited nothing.

## Tools installed
- None.

## Blockers / gaps
- O3 pending (mutants97 pin not landed). Claim O not judged.
- Judgments are on pinned captures plus the fresh re-opens listed above; live pages for S985–S992 were not re-fetched.
