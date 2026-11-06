# ScribeEntry100 — work song and labour chant entry (claim C, coverage)

Seat: ScribeEntry100 (scribe, leaf; no subagent dispatch). Lane: kotodama, round 100, wave w1.
Base `60010a55fb5f04ee728070c463b1a57ae1cc17fc`; freeze `255d84776c12c918b7bfb2a7173d7b495e3f966e`.
Scratch `/fast/scratch/hyaku/kotodama-r100/ScribeEntry100/` (removed before yield).

## 1. Behaviour

Wrote the new knowledge entry `corpus/knowledge/linguistics/work-song-labour-chant.md` (41933 bytes,
sha256 `65d7391ea6c7894524fc0665d06dfb935683861bf8e4a7795e8d923ea53e4dd7`) and indexed it in
`corpus/README.md`. The entry is reference and generative method only, NON-CANON, and defers canon to
lore-shokunin, research method to chousa and sound production to audio-shokunin.

Structure: 12 `## ` sections — scope/boundary table (21 neighbour rows), what a work song is (four
slots), the song leader and call and response, work rhythm and the task, the shanty and occupational
repertories, improvised verses/complaint/satire, a six-row sourced table with round-99 binding
lines, a 21-step decision procedure with a NON-CANON worked example, 12 error patterns (including the
five the item names: no task, no response, rhythm not fitting the motion, shanty off the job with no
change of function, satire with no licence), a 13-item checklist, source reach/calibration/handoff,
and an 8-item inference ledger.

The frozen topic line is byte-equal to `predispatch.py`'s `FROZEN_TOPIC` (451 bytes including the
`- topic: ` prefix; 1 × U+2014; ASCII apostrophes). All six frozen phrases sit in h2 headings:
`work song` (§2), `song leader` + `call and response` (§3), `work rhythm` + `hauling song` (§4),
`shanty` (§5) — 6/6, floor 4.

## 2. Gates (command, result, rc)

All run from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

| # | command | result | rc |
|---|---|---|---|
| 1 | `python3 /fast/scratch/hyaku/kotodama-r100/ScribeEntry100/selfcheck.py` | BYTES 41933; H2 12; TABLE 21x3; PHRASES 6/6; TOPIC-LINE equal; CITED ids=10 uncited=[]; CITED-LINES multi-id=0 table-id=0; OVERLAP-8GRAM all adjacent owners 0; `SELFCHECK PASS` | 0 |
| 2 | `python3 -B reports/round-100/controls/feasibility/table_support_ref.py --entry corpus/knowledge/linguistics/work-song-labour-chant.md --evidence reports/round-100/evidence --root .` | `TABLE-SUPPORT: 0 finding(s) in 1 scoped table(s)` | 0 |
| 3 | `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/work-song-labour-chant.md` | `CITED-LINES: 0 finding(s) in 1 file(s)` | 0 |
| 4 | `python3 -B tools/check-corpus-index.py --root .` | `CORPUS-INDEX: OK files=272 rows=272 findings=0` | 0 |
| 5 | C8 sweep via `predispatch.tree_knowledge` + `sweep_owners` excluding the entry | `files 272 other owners 0 []` | 0 |
| 6 | `wc -c` / `sha256sum` on the entry | 41933 B; `65d7391e…e4dd7` | 0 |
| 7 | C2/C6 simulation with `predispatch` constants over `corpus/SOURCES.md` | `rows 951 highest S1027 new 10 qualifying 10 uncited []` | 0 |

The full transcript of 1–7 is `stage/ScribeEntry100/self-check.txt`; check 1 is re-runnable with `stage/ScribeEntry100/selfcheck.py` (copied out of scratch before it was removed).

C1 was also simulated with the counter's own code path (`norm`, `PHRASES`, table scan): 41933 bytes,
12 h2, table 21x3, 6/6 phrases, topic equal — PASS. The counter itself was not run by this seat; the
L1 owns the lands measurement.

## 3. Cited ids (all ten qualifying rows, C6)

S1018 Terry, The Shanty Book (1921) · S1019 Sharp, English Folk-Chanteys (1914) · S1020 Allen, Ware
and Garrison, Slave Songs of the United States (1867) · S1021 Bücher, Arbeit und Rhythmus (1896) ·
S1022 Collinson, The Oyster Dredging Songs of the Firth of Forth (1961) · S1023 Blankenhorn, A New
Approach to the Classification of Gaelic Song (2018) · S1024 Bourke, Working and Weeping (1988) ·
S1025 Purser, Hebridean Rowing Songs (2024) · S1026 Whall, Ships, Sea Songs and Shanties (1913) ·
S1027 SIL Philippines, Mangali and Tanudan Valley Music.

No id is cited twice on one line (QUALITY 15) and no table row carries an id; the table's six binding
lines each carry exactly one id and name their row by its first-cell words.

## 4. Inference list

Marked `inference` in the body and listed in §12 of the entry:

1. The four slots (task, crew, leader, beat) are separable, and a song missing one is a different object.
2. The leader's stop when the crew takes the line is a handover, not a lapse.
3. The answer does three jobs (confirmation, timing, rest for the leader).
4. The alternating/uniform distinction predicts which part of a task a song can mark.
5. The tune stock, not the single song, is the unit a crew owns.
6. The licence is bounded by the nearest hearer rather than by the song's content.
7. A repertoire's death is a design event with a date and a cause.
8. The work song's complaint is neither contest nor praise (no adjudicator, no patron).

Two further inline inferences: the shanty is the repertoire the opened sources document most fully
(§5), and the §7 afterword's reading of the table rows against §4's prediction.

## 5. Touched surfaces

- `corpus/knowledge/linguistics/work-song-labour-chant.md` — new (only writer).
- `corpus/README.md` — `## linguistics/ (44)` → `(45)`; one row inserted in filename order before
  `writing-systems.md` carrying the frozen topic byte-equal; a `## Round 100 work song entry
  (2026-11-06)` section appended with `Total knowledge entries: 272.` and the dated footer
  `(total 272 files; directory totals 45/36/43/29/24/95)`.
- `stage/ScribeEntry100/self-check.txt`, `stage/ScribeEntry100/DONE`, this report.

Not touched: `corpus/SOURCES.md`, `reports/round-100/evidence/`, `tools/*`, `SKILL.md`, the praise
entry, `MANIFEST`, fleet files, sibling lanes. No commit, no add, no checkout.

## 6. Out of scope / not done by this seat

- Registry rows, evidence captures and `manifest.json` (ExecRegistry100). The entry cites the ids it
  landed; C7 binding is theirs.
- C9 non-author re-open (ReviewerC100), C3 append-only, C4 census, C5 index run by the counter.
- Claim O and every O leg.
- The stale routing at `culture-material/material-culture-inference-method.md:15` and the maritime
  seam at `maritime-seafaring-lexicon.md:29` are recorded in the entry's §11 as known seams; repairing
  them would edit siblings and is not this item's surface.

## 7. Findings and limits

- The base is weighted to the North Atlantic and to the nineteenth century: three maritime
  collections (S1018, S1019, S1026), one Sea Islands collection (S1020), three Gaelic sources
  (S1023, S1024, S1025), one Scottish fishery (S1022), one comparative treatise (S1021) and one
  Kalinga field-documentation page (S1027). The entry says so and claims no grammar of the genre.
- Bücher's developmental ladder is flagged as a discredited nineteenth-century stage theory; only the
  alternating/uniform distinction is used.
- Purser's report of Collinson's two rowing-song types is carried as an unverified suggestion.
- The 1867 collection is used for its descriptions of practice only; its racial vocabulary and
  judgments are explicitly excluded, and no slur is reproduced in the entry.
- S1024's shipped capture differs from the scout capture by 2 bytes (source PDF changed between
  fetches, per `rows.md`); the table check and every quotation were re-run against the shipped
  `reports/round-100/evidence/` bytes, not the scout copies.
- The 8-gram overlap check exempts the lane's standard header block (`- source:` / `- verified-at:` /
  `- recheck:`), which is a format convention shared by every entry, not prose copied from a
  neighbour; with that exemption the overlap against all nine adjacent owners is 0.
- Tooling: none installed or upgraded this seat.
