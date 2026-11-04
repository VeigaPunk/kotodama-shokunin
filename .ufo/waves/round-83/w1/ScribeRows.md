# ScribeRows — round 83, wave 1 (claims O/D/C, seat axes: depth, freshness)

Seat: `ScribeRows`. Wrote `corpus/SOURCES.md` (four new rows S909-S912, two `used-by` appends) and the binding
fetch receipts for those rows. Did not insert the S913 draft (L1 appends it under claim C).

## 1. Behavior

1. **Opened all four sources myself, by plain GET, no automation beyond the request.** Two user-agents per URL
   (`curl/8.23.0` and a browser-shaped UA); both returned HTTP 200 and byte-identical bodies for all four.
   Receipts written to `.ufo/waves/round-83/w1/stage/ScribeRows/S909.txt` … `S912.txt`, each carrying the live URL,
   access date 2026-11-04, both UA records, HTTP status, transferred and decoded bytes, sha256 of the decoded bytes,
   the located span with its word count, `raw <n> / folded <m>`, the two read definitions it was counted under, a
   reproducible one-liner, and the same-page Wayback probe.
2. **Inserted S909-S912 as the last rows of the `## Registry` table, immediately before `## Paths`** (lines 865-868),
   each 11 content cells, `opened` 2026-11-04, `status` mined, `used-by`
   `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`.
   - `recheck`: 365d for S909 (Avalon fixed page) and S912 (Gutenberg e-text); **on-release** for S910 and S911
     (live Wikisource pages), per this wave's instruction. Note the divergence: S905 is also a Wikisource page and is
     filed 365d — not changed here, that row is not mine to touch.
   - `tier`: A for S909 (a code's own text), S911 and S912 (scripture's own text); B for S910 (the 1911 survey).
3. **Appended the entry path to S904 and S905 `used-by`** after confirming the entry cites both (S904: Odyssey II and
   XV; S905: Germania ch. 18 five times and ch. 4 once). Old → new logged in §4.
4. **Drafted, did not insert, the S913 superseding row** at `.ufo/waves/round-83/w1/stage/ScribeRows/S913.row`:
   `teaches` starts `supersedes S908 — `, carries `REJECTED:` (contract spelling) with the reason and a `flip:`,
   `anchor` names chapter III ("Sympathetic Magic") with **no quote**, `used-by` `—`.
5. **Ran the census gate**: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
   /home/vgpnk/Projects/shokunin kotodama` → **exit 0**; receipt `.ufo/waves/round-83/w1/stage/ScribeRows/census.md`.
6. **Verified the entry's quotes against the fetched bytes** (56 quote spans in its `## 3`): 51 locate verbatim, 5 do
   not — reported verbatim to the entry's owner, not edited (the entry is not my write scope).

## 2. Gates (all run; nothing inferred)

| gate | command | result |
|---|---|---|
| census validate | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | **exit 0**; 0 E-codes, 5 W01, 28 W04 |
| row shape | split each touched row on `|` | S904, S905, S909, S910, S911, S912 = 13 raw cells → **11 content cells** each; S913 draft same |
| registry growth | `grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md` | **836** now vs **832** at base `3088bd7` = exactly the four rows |
| entry present (E11 leg) | `find corpus/knowledge -name '*.md' | wc -l` | **257** (the entry is on disk, so every `used-by` resolves; its size is not cited here because the entry seat was still editing it) |
| anchor located | folded read of each own source | S909 raw 1 / folded 1; S910 raw 0 / folded 1; S911 raw 1 / folded 1; S912 raw 0 / folded 1 |
| anchor word count | whitespace split | 20 / 17 / 10 / 22 words, all ≤ 25 |

Census profile vs base: `reports/round-82/telemetry/census-start.txt` carries 32 W-lines; the current run carries 33.
The single new line is `W01 S907 tierC mined used-by=…guest-right-hospitality-law.md` — a round-82 row that was filed
after that census was taken. My four rows add **no** warning, no duplicate URL and no E-code.

## 3. Touched surfaces

- `corpus/SOURCES.md` — four rows appended inside the Registry table; two `used-by` cells appended (S904, S905).
  No other cell of any row changed; S908 left byte-identical (superseded by S913, not rewritten).
- `.ufo/waves/round-83/w1/stage/ScribeRows/S909.txt`, `S910.txt`, `S911.txt`, `S912.txt` — binding fetch receipts.
- `.ufo/waves/round-83/w1/stage/ScribeRows/census.md` — census exit code, tail, profile, cell check.
- `.ufo/waves/round-83/w1/stage/ScribeRows/S913.row` — superseding-row draft.
- `.ufo/waves/round-83/w1/ScribeRows.md` — this report.

Not touched: the entry, `corpus/QUALITY.md`, the lesson, any Gate block, `tools/`, `reports/`, S908's row, any other
lane's rows, `MANIFEST.json`, `.ufo/state/`.

## 4. `used-by` changes (old → new, verbatim)

```
S904  corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
   -> corpus/knowledge/myth-symbol/guest-right-hospitality-law.md, corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md
S905  corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
   -> corpus/knowledge/myth-symbol/guest-right-hospitality-law.md, corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md
```
Trigger: the entry's `## 3` carries 2 S904 anchors (`Odyssey` II, XV) and 5 S905 anchors (`Germania` ch. 18 ×4, ch. 4 ×1).

## 5. Findings

1. **S911 has no archive capture.** The availability API returned `{"archived_snapshots": {}}` and the CDX exact
   query returned `[]` for the probed URL `en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_85`. The row
   therefore rests on the live read (revision 14397100 as the stable pointer) and says so in its `source` cell rather
   than claiming a capture. The folded read serves the prose (raw 1 / folded 1), which under QUALITY 30 is not a
   durability ground.
2. **The Avalon frame URL is a trap.** `hamframe.asp` serves 356 B of frameset markup; the law text is on
   `hamcode.asp`. The receipt records both, so a later reader does not conclude the page is empty.
3. **EB11 "Marriage" is Parsoid-rendered but readable.** The live page (147040 decoded bytes, revision 10430027)
   carries the Proofreadpage `#lst` transclusion as a raw `{"template": …}` JSON payload in the same container; a
   tag-stripper that emits no separator reads that payload as one long sentence. The 2026-08-31 capture (128008
   decoded bytes, 44 `</p>` vs live 43) carries the same 320 sentence units through the legacy renderer. The quoted
   span is in both (raw 0 / folded 1).
4. **EB11 "Marriage" is not a stage-law text.** Independent of the scout's reading, I measured 0 occurrences of
   "promiscuity", "group marriage" and "matriarchy" in the served bytes; the article is a legal/comparative survey
   (concubinage and morganatic marriage, Roman law, Hardwicke's Act and the deceased wife's sister, foreign
   marriages, the German code of 1900). The S910 row's `teaches` claims nothing beyond that.
5. **R82-M3 second reading.** `ScoutSources`' stage dir was **empty** when this seat finished, so the independent
   scout reading could not be compared. The comparison I could make was the entry owner's own fetch: it agreed on
   S909 §138, S910 (147040 decoded bytes), S912 18:6, and S905 ("dower", 163266 bytes). **One disagreement, reported
   not silently picked:** sacred-texts' Griffith page prints `Sūrya` (U+016B) and `Pūṣan` where the Wikisource
   transcription — the URL our S911 row names — prints `Surya` (30×) and `Pusan` (6×), with zero macron forms. Two
   different transcriptions of one translation; **the receipt binds for the row's named URL**, so the row's anchor
   stays ASCII `Surya`.
6. **Five entry quotes deviate from the served bytes** (of 56 checked; reported to the entry's owner):
   - S911 「Let Pūṣan take thy hand…」 — the cited Wikisource page reads `Pusan`; `Pūṣan` occurs 0 times.
   - S909 「…the "purchase price"…」 — Avalon §164 prints `"Purchase price"` with a capital P; lowercase occurs 0 times.
   - S905 「…passed on to her grandchildren」 — Church & Brodribb prints `grand-children`; unhyphenated occurs 0 times.
   - S910 ×2 - locate only after removing tag-separator spaces (`confarreatio ,`, `mancipatio ,`, `( manus )`); faithful
     to the prose, not verbatim to the folded read.
7. **Pre-existing warning, not mine:** the census's only line new against the round-82 receipt is `W01 S907`, created
   because round 82 filed S907 tier C and mined. Left untouched.

## 6. Out of scope / not done

- S913 was **not inserted** — draft only, per the assignment (L1 appends under claim C).
- The entry, `QUALITY` criterion 31's text, `tools/check-cited-records.py`, the round lesson and the Gate block are
  other seats' artifacts; this seat verified against them and changed none.
- No tool installs or upgrades were made; `curl 8.23.0` and `python3` stdlib were sufficient, so the tooling directive
  recorded nothing (pacman is paused host-wide, and no channel was needed).
- Nothing was committed; no git or jj mutation was run.

## 7. Artifacts

| path | contents |
|---|---|
| `corpus/SOURCES.md` | S909-S912 inserted at the Registry end; S904/S905 `used-by` appended |
| `.ufo/waves/round-83/w1/stage/ScribeRows/S909.txt` | Hammurabi — URL, 2 UAs, 200, 74531 B, sha256, §138 span, raw 1 / folded 1, capture byte-identical |
| `.ufo/waves/round-83/w1/stage/ScribeRows/S910.txt` | EB11 "Marriage" — URL, 2 UAs, 200, 147040 B, sha256, consent span, raw 0 / folded 1, Parsoid note, capture 128008 B |
| `.ufo/waves/round-83/w1/stage/ScribeRows/S911.txt` | RV 10.85 Griffith — URL, 2 UAs, 200, 70655 B, sha256, v.9 span, raw 1 / folded 1, uncaptured URLs filed verbatim |
| `.ufo/waves/round-83/w1/stage/ScribeRows/S912.txt` | Leviticus 18 KJV — URL, 2 UAs, 200, 4455950 B, sha256, 18:6 span, raw 0 / folded 1, capture byte-identical |
| `.ufo/waves/round-83/w1/stage/ScribeRows/census.md` | census exit 0, tail, warning profile, cell-shape check |
| `.ufo/waves/round-83/w1/stage/ScribeRows/S913.row` | draft supersession of S908 |

Scratch (outside the repo, on the fast volume) held the fetched bodies and the probe scripts; it was removed at the
end of the seat. Nothing is left behind, and no receipt cites it.
