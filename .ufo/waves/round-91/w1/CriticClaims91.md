# CriticClaims91 — round-91 critic report (frozen-predicate attack)

Attack seat, leaf, read-only on production. Freeze 691aebf2, base d39434b3. Attacked the frozen v2 entry-mode grader on frozen bytes with 13 counterfeits + 1 control. Tool sha verified before runs: `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093`. Full detail: `.ufo/waves/round-91/w1/stage/CriticClaims91/counterfeits.md` and `attacks.md`.

## Files written
- `.ufo/waves/round-91/w1/stage/CriticClaims91/counterfeits.md` — per-run table (name | class | rc | PASS legs | FAIL legs | verdict).
- `.ufo/waves/round-91/w1/stage/CriticClaims91/attacks.md` — reasoning + smallest correction per passing counterfeit.
- This report. No other production path touched; no commits, no installs (none needed), no pacman, no sysctls. Scratch `/fast/scratch/hyaku/kotodama-r91/CriticClaims91/` deleted before yield (trap-equivalent `shutil`-style cleanup after report extraction).

## Result in one line
Control G0 passes 8/8 (rc 0); 7 of 13 counterfeits pass the frozen entry mode (rc 0): lesson-channel no-dash/blockquote dispositions (task a — bypass confirmed; `- S776: LOCATED` colon form IS counted), chrome-quote gate bound to capture bytes with the quote carried as the entry's own sentence (task b — passes), fragment-suffix base-url shadow, phrase-list heading stuffing, base-registry byte-copy capture, row-url↔capture never bound + capture sharing. 6 named refusal classes hold as claimed.

## Measured (commands, rc)
- `sha256sum tools/check-advance-evidence.py` → matches O.tool_sha256 pin. rc 0.
- 16 × `python3 -B <frozen tool> entry --root <tree> …` with the exact `grade_c` argument vector (grade_c in reports/round-91/measure91.py; `--topic-phrases`, `--min-*`, `--graded`, `--capture-dir` verbatim). rc per run in counterfeits.md; total wall 1.5 s; every LEG line captured for all 16 runs.
- Preflight: base registry `git show d39434b3:corpus/SOURCES.md` → 875 rows (S776 present; base lesson dispositions = S942–S948 only, so S940/S001/S776 are "old id without base disposition" probes).

## Not measurable from this seat
- measure91.py end-to-end (MATERIALIZE/INDEX/APPENDONLY counter legs) needs a committed lands revision; commits are forbidden for this seat. The tool-level APPENDONLY leg (lesson channel) is fully covered above; the counter's registry-append-only leg (base-row diff) was read but not exercised.
- Whether the real landed entry exhibits any of the 7 passing classes: out of scope (attack seat runs only on synthetic frozen-arg trees).

## Smallest corrections proposed (none applied — frozen)
1. Lesson channel: match dispositions under any markdown-marker prefix (`^(?:[>\s]*[-*+>]?\s*)S\d{3,}\b.*\b(NOT[ _-]?LOCATED|LOCATED)\b`), add V10a/V10c shapes to selftest + mutants.
2. Shadow/duplicate URL checks: normalize URLs (strip `#fragment`, trailing `/`, host case) before set membership.
3. Entry mode: reuse the existing `surface_error()` to bind manifest url ↔ row url cell for qualifying ids; refuse one capture path shared by two qualifying ids.
4. Gate quote: bind to the manifest's recorded `quote` field or require ≥3 shared content words with the teaching cell (chrome cannot be rejected mechanically; say so in bounds).
5. TOPIC anchors: require ≥4 phrase anchors across ≥3 distinct h2 headings, and/or compute `--min-topic-overlap` on non-heading non-table prose.
6. `graded_shas`: include base registry (and README/manifest) bytes so V9's base-registry capture is refused.
