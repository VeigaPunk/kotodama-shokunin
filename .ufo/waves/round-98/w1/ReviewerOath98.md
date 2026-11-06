# ReviewerOath98 — round 98, wave 1 — sentence-support sweep of oath-blessing-curse-formulae.md

Scope: verify every citing sentence of `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` against its round-96 capture (`reports/round-96/evidence/`, manifest S975–S984). Routed R97-M2 class (cited sentence not supported by its source). Nothing outside my stage dir, my Report, and DONE was written; no frozen file touched; nothing committed.

## Files written
- `.ufo/waves/round-98/w1/stage/ReviewerOath98/support.md` — full table, totals, repairs (main output; sha256 337118906efaf7badd3f633ef5d739fe34892982f890f0b38fe94a51a523fe2d)
- `.ufo/waves/round-98/w1/stage/ReviewerOath98/DONE` — one line, the sha256 above (written last)
- this Report.

## Method and measured numbers
1. `grep -n -E 'S[0-9]{3}' corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` — rc 0, 32 hits: 22 body citing sentences (L43–L126) + 10 front-matter registry rows (L5–L14, not sentences).
2. 22 ≤ 40 → all 22 sentences judged; systematic sample not needed (k n/a).
3. Occurrence counts in captures (Python `str.count`, decoded UTF-8) — rc 0:
   - 10/10 entry quotes occur exactly once in their named capture; manifest `quote_count` is 1 for all 10 entries — agrees.
   - 17/17 deciding spans used as evidence are count==1 and ≤25 words (list in support.md).
4. Absence checks backing the unsupported verdicts — rc 0: S977 `archetype|later|quot` → 0/0/0; S980 `sanction` → 0; S984 `sanction` → 0; S981 `practitioner|fixed|occasion|addressee` → 0.
5. Manifest cross-check: capture files S975.txt–S984.txt all present; 10/10 URLs recorded, `http: 200`, `access: 2026-11-05`.

## Verdict totals (support.md has the per-line table)
- supported 11: L43, 45, 55, 67, 69, 80, 84, 94, 98, 100, 124
- weak 3: L49 (hedged conjecture stated flat; quote truncates "geissupported" mid-compound), L51 ("The same account" misattributes S980 to S978's account), L53 (commentator's division, not practitioner requirement)
- unsupported 5: L47 (no "quoted in a later text as the archetype" in the Iliad capture), L96 (addressee/occasion-fixed and count-the-sections claims absent; agent inverted), L120 (seven requirements are composition requirements, not target-status), L122 (ungrammatical sentence; "sanction" absent from capture — likeliest R97-M2 defect), L126 (cited span is treaty borrowing, not witness-enforced sanction)
- contradicted 3: L82 (capture: geases share the **conditional-type** curse = attached breach-penalty, opposite of "breach is itself the sanction"), L92 (same formula continues "hjálpi mér svá Freyr ok Njǫrðr…" = direct address, so "naming act rather than an address" is wrong), L118 (fear strikes "those who swear the oath", i.e. the swearers, not "the community rather than the hearer")

Quote integrity is intact everywhere: every defect is a characterization defect, not a broken or duplicated quote.

## Repairs
Eleven concrete repairs (R1–R11, one per defective line) are listed in support.md for a later round to apply; the entry itself was not edited by this seat.

## Blockers
None. No tool installed or upgraded (none needed; pacman paused, respected). Scratch `/fast/scratch/hyaku/kotodama-r98/ReviewerOath98/` deleted before yield (verified absent).
