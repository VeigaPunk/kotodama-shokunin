# ScribeEntryWitch — claim-D entry draft, round 84 wave 1

Verdict: **draft complete and shape-clean.** The entry is written at the stage path and passes every claim-D shape leg this seat can measure without a lands commit: 56,778 bytes, 15 `## ` sections, 6 decision rows under `## 2. Six design decisions`, 43 anchor bullets under `## 3. Attested anchors` across 25 distinct ids with 0 malformed bullets, and `tools/check-cited-lines.py` = 0 findings (rc 0). Nothing was committed and `corpus/SOURCES.md` was not touched.

## Behavior

1. Re-read the lane freeze chain (`3ca2cf28` → `e160a72e` → `7e6ee2f8`) and the dispatched wave spec before writing, because the seat prompt's frozen hash and the lane tip disagreed (finding 1).
2. Opened all four claim-D sources by ordinary plain GET on 2026-11-04 and recorded HTTP status, served bytes and sha256 per source; accepted the L1's mid-flight source correction (S915 → Howard Williams, 1865; S916 → the Bull subpage) and re-read both replacements.
3. Wrote the entry in the house shape used by `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` (§1 partial owners, §2 six design decisions, §3 attested anchors, then topic sections, build order, NON-CANON worked case, checklist, lore handoff).
4. Checked every `「…」` fragment in §3 character-for-character (whitespace-normalised) against the fetched text for S914/S915/S916/S917 and against the row's own `anchor` cell for the twenty-one existing rows; fixed two apostrophe mismatches (S621, S382); final run: 41 fragments, 0 misses.
5. Ran the lane lint and a local replication of the frozen counter's leg logic; wrote `notes.md` and the five fetch receipts; deleted the seat scratch directory after copying receipts.

## Gates run (seat-local, read-only)

| Gate | Command | Output |
|---|---|---|
| cited-lines lint | `python3 -B tools/check-cited-lines.py .ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md` | `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0 |
| shape replication (ENTRY/SECTIONS/DECISIONS/ANCHORS) | local Python replication of `reports/round-84/accept-d84.py` leg logic over the draft | bytes 56,778; sections 15; decision rows 6; bullets 43; distinct ids 25; malformed 0 |
| before-state (knowledge files) | `git ls-tree -r --name-only 81499ee4 corpus/knowledge \| grep -c '\.md$'` | 257 |
| before-state (registry rows) | `git show 81499ee4:corpus/SOURCES.md \| grep -cE '^ {0,3}\| *S[0-9]{3,} *\|'` | 837 |
| before-state (owners) | topic-line and filename sweeps at 81499ee4 | 0 owners, 0 filename owners |
| occurrence census | `git grep -niE '\b(witch\|witches\|witchcraft\|sorcerer\|sorcery\|malefic)\b' 81499ee4 -- corpus/knowledge` | 19 lines / 11 files |
| quote audit | per-bullet fragment search against fetched text or row anchor cell | 41 fragments, 0 misses |
| path audit | named sibling paths and `corpus/knowledge/synthesis/worldbible-integration-contract.md` | all resolve |
| absolute-path audit | `grep -nE '/(home\|fast\|tmp)/'` over the entry, notes and receipts | none |

The frozen counter itself was not run: it needs a lands revision and a work directory, and this seat neither commits nor lands. The L1 owns that run.

## Touched surfaces

- `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md` (new, 56,515 bytes)
- `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/notes.md` (new)
- `.ufo/waves/round-84/w1/evidence/ScribeEntryWitch/S914.txt`, `S915.txt`, `S915-stub-candidate.txt`, `S916.txt`, `S917.txt` (new receipts)
- `.ufo/waves/round-84/w1/ScribeEntryWitch.md` (this report)

No other path was written. `corpus/SOURCES.md`, `SKILL.md`, `corpus/QUALITY.md`, `MANIFEST.json`, `.ufo/state/`, the fleet repo and sibling lanes were left untouched. No git/jj mutation was run; no tool was installed or upgraded.

## Findings

1. **Freeze hash drift between the seat prompt and the lane tip (blocking for grading, not for the draft).** The prompt cites `3ca2cf288fb593618e0559ea86a36e2dd3110eb8` and the headings `## 2. The decision table` / `## 4. Attested anchors`. The lane tip is `7e6ee2f8` (freeze revision r2). Freeze r1 (`e160a72e`, message "entry section headings aligned to the house shape") replaced those headings with `## 2. Six design decisions` / `## 3. Attested anchors`; r2 changed only claim O's shape-marker list. `git diff e160a72e 7e6ee2f8 -- reports/round-84/accept-d84.py` is empty and the claim-D block in `claims.json` is byte-identical across the two, so r1 and r2 grade D identically. This draft follows the lane tip. **A counter run with `--freeze 3ca2cf28` would fail DECISIONS and ANCHORS on this draft by construction**; the L1 should confirm the r2 freeze before landing/running.
2. **S915 candidate was not usable and the substitute is now the row's source.** The EB11 "Sorcery" page served HTTP 200 / 60,730 bytes / sha256 `2c4092db…`, but its body is a single definition paragraph of roughly ninety words. Per the L1 correction the row is Howard Williams, *The Superstitions of Witchcraft* (1865), Project Gutenberg #22822 (HTTP 200, 450,230 bytes, sha256 `88407510…`). The stub is cited nowhere; its receipt is kept for the record. The source scout's second correction also binds the locator form: the e-text has no page markers, so all three S915 bullets locate by Part + chapter + the paragraph's opening subject, and the printed page numbers in the 1865 contents are not used.
3. **S916 must quote the Bull, not the Malleus cover.** The `Malleus_Maleficarum` top page serves a cover and table of contents; the Bull subpage serves the body. The entry's three S916 bullets quote only the Bull's own words (crime list, empowerment clause, date) and locate them at printed pp. xliii–xlv. Per the source scout: the printed text carries literal ellipses at three points, both quotes end before any of them, there is **no Wayback capture** of the Bull page (the entry claims none), and the manual's own body is not transcribed on Wikisource (part subpages 404), so no procedural anchor is attributed to the manual. The same correction records that S914's only capture (2008-10-06) predates the transcription and lacks the quoted text (the entry claims no capture for it), and that S917's 2022 capture is body-identical with the header/footer-only diff (the entry's S917 spans are in the body).
4. **The frozen ANCHORS leg's duplicate guard is a no-op, and this is a real leniency.** In `accept-d84.py`, the malformed test is `found[0] in bad` while `bad` collects line prefixes — so a repeated S-id is not malformed, and a 20-bullet entry with only four ids passes (exactly what the L1's own fixture shows: `bullets=21/20 ids=4/4 malformed=0`). The draft does not rely on this: it carries 25 distinct ids across 43 bullets. But the critic and mutation seats should know that ANCHORS + LINT + SOURCED + ROWS, not the distinct-id floor, carry the anti-stub weight, and a stub entry with four repeated ids is a live mutation that ANCHORS alone will not kill.
5. **Before-state count disagreement, small and honest.** The frozen claim's before-text says "19 times across 10 files"; this seat's word-boundary sweep measures 19 lines across **11** files. The entry's `- gap filled:` reports 11 (its own measurement) and keeps the 19. ScoutGapWitch's census should arbitrate; the difference does not affect any counter leg.
6. **Existing rows keep their original `used-by`.** The twenty-one already-registered rows cited in §3 still name their prior entries. Only the four new rows (`S914`–`S917`) must name this entry in `used-by`, which is ScribeRowsWitch's line to write; the ROWS leg checks those four ids only.
7. **No dual-heading hedge was added.** Adding legacy heading aliases would have required duplicating the decision table and the anchor list, which would damage the entry's craft for a freeze that the lane has already superseded. The risk is recorded here instead; if the L1 intends to grade with `3ca2cf28`, this draft must be re-headed before the run.

## Out of scope (not done, by bound)

- No `corpus/SOURCES.md` rows and no `used-by` cells (ScribeRowsWitch/L1).
- No `## Gates and probes` rows (ExecRegistryRows/L1) and no `SKILL.md` edit.
- No commit, push, jj operation, or lands revision.
- No tool install or upgrade; `curl`, stdlib `python3` and read-only `git` sufficed, and no pacman transaction was attempted.
- No claim about any world (lore-shokunin owns canon), no claim about any living community, no accusation or interrogation procedure.

## Artifact paths (repo-relative)

- `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md`
- `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/notes.md`
- `.ufo/waves/round-84/w1/evidence/ScribeEntryWitch/S914.txt`
- `.ufo/waves/round-84/w1/evidence/ScribeEntryWitch/S915.txt`
- `.ufo/waves/round-84/w1/evidence/ScribeEntryWitch/S915-stub-candidate.txt`
- `.ufo/waves/round-84/w1/evidence/ScribeEntryWitch/S916.txt`
- `.ufo/waves/round-84/w1/evidence/ScribeEntryWitch/S917.txt`
- `.ufo/waves/round-84/w1/ScribeEntryWitch.md`

Scratch: the seat scratch directory was deleted after the receipts were copied; nothing is left behind.
