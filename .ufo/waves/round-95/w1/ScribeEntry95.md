# ScribeEntry95 — claim C entry, round 95 wave 1

Seat: scribe (coverage axis, milestone r95-v1). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`; freeze `d41eb594d27fa71869c0c28d9c2dc051fda40079`.
Frozen inputs read first: `reports/round-95/claims.json`, `reports/round-95/predispatch.py` (frozen, not amended).

## Files written

- `stage/ScribeEntry95/funerary-lament-dirge-formulae.md` — the claim C entry draft (sha256 `397a5de3c64de2ae269bb1c145f18bec668112f2c660e9098ed2bf3c3d4794dc`, 50148 bytes).
- `stage/ScribeEntry95/DONE` — one line: the sha256 above.
- This trailer: `.ufo/waves/round-95/w1/ScribeEntry95.md`.

Nothing outside my stage dir was written. No commits, no pushes, no mutating git/jj. Scratch `/fast/scratch/hyaku/kotodama-r95/ScribeEntry95/` was removed before yield.

## Dependency

Waited for `stage/ScoutTopic95/DONE` (bounded loop, `for i in $(seq 1 20); do [ -f .../DONE ] && break; sleep 30; done`), which appeared at the 5th iteration. Read `stage/ScoutTopic95/rows.md` (37 KB) and its 22 committed capture files under `stage/ScoutTopic95/evidence/` (S970–S980, each `.pdf` + `.txt` rendering).

The scout proposed 11 rows S970–S980. I cite **five** of them, and I messaged `ExecRegistry95` (`write agent://ExecRegistry95`) naming the exact set so the registry rows and the entry agree id-for-id: **S970** (Pärtlas, Seto solo/choral funeral laments), **S971** (Rosenberg, Corsican women's lament), **S972** (McLaughlin, the Irish wake and the keen), **S973** (Williams & Ó Laoire, the keening woman), **S974** (Mzhavanadze & Scherbaum, Svan funeral dirges). I explicitly told that seat not to land **S979**, which the scout marks tier C (lead only), and to drop S974 last if it can only do four. Rationale for the five: they are the only tier-A rows covering all six frozen facets (antiphonal lament S970/S971; professional keeners S972/S973; gendered mourning rules S971/S973; lament refrain S974; praise of the dead S974; address to the dead S974; speech-vs-song S970/S972/S973).

## Measurements (each with its command)

All measured against the committed scout captures under `stage/ScoutTopic95/evidence/`.

**1. Quote verification — every quoted span in the entry is an exact single-occurrence substring of a committed capture, ≤ 25 words.**

```
python3 - <<'EOF'   # re.sub(r'\s+',' ',raw).count(re.sub(r'\s+',' ',q)) over evidence/*.txt
EOF
```
Result: 14 quoted spans, 14/14 found, every count == 1, maximum 14 words. Verbatim list (span → capture → count → words):

| span | capture | count | words |
|---|---|---|---|
| the keen was a sacred improvised chant that evolved over many centuries | S972.txt | 1 | 12 |
| in the forms of homage, praise, etc. | S971.txt | 1 | 7 |
| The family keened over the corpse. Professional keeners took over. | S972.txt | 1 | 10 |
| was important in the role of the female professional mourner who performed ritualized laments | S973.txt | 1 | 14 |
| the antiphonal way of performing Seto songs | S970.txt | 1 | 7 |
| the relationship between the genres of lament and song in Seto culture | S970.txt | 1 | 12 |
| inherently jural and historicizing structure | S971.txt | 1 | 5 |
| The antiphonal nature of voceru performance | S971.txt | 1 | 6 |
| record-keeping function | S971.txt | 1 | 2 |
| Each phrase of her agonized litany ends with a refrain exclamation | S974.txt | 1 | 11 |
| No words were used, only vocables such as | S973.txt | 1 | 8 |
| so that the community gave poignant expression to their emotion in purely musical terms | S973.txt | 1 | 14 |
| Sima praises the good deeds and grace of the deceased | S974.txt | 1 | 10 |
| a predominantly (in many contexts exclusively) feminine mode of expression | S971.txt | 1 | 10 |

**2. One-S-id-per-line lint — 0 findings.**

```
python3 -B tools/check-cited-lines.py .ufo/waves/round-95/w1/stage/ScribeEntry95/funerary-lament-dirge-formulae.md
→ CITED-LINES: 0 finding(s) in 1 file(s)   rc=0
```
The first draft put the id range on one frontmatter line (`- source: corpus/SOURCES.md (S970-S974)`) and the tool returned `MULTI-ID ... :3 S970,S974`, rc=1. I rewrote that line to carry no id (`- source: corpus/SOURCES.md (the five registry rows below, one id per line)`) and kept the ids on their own `- sources:` sub-lines, the convention the round-94 sibling entry uses. Re-run after the edit: 0 findings, rc=0. No table row carries an id.

**3. C1 shape floors — PASS.** Reproduced with the frozen counter's own logic (`reports/round-95/predispatch.py` C1 block, run read-only against my draft): `bytes=50148 h2=12 table=11x5 phrases=6/6 topic_equal=True => C1 PASS`. Floors: bytes ≥ 12000 ✓; h2 ≥ 6 ✓; table ≥ 5 data rows × ≥ 3 columns ✓; ≥ 4 of 6 frozen phrases in h2 headings or table data cells ✓ (6/6); `- topic:` line byte-equal to the frozen topic ✓. The table separator row is `|---|---|---|---|---|` and the counter's `^\|[\s:\-|]+\|$` pattern matches it, so the 11 data rows are counted from there.

**4. Phrase placement map** (counter's `hits` computation; every phrase is carried by an h2 heading, none by a table cell alone):

| frozen phrase | placement |
|---|---|
| professional keeners | h2 §3 "Professional keeners: the licensed voice of grief" (+ table row 1) |
| antiphonal lament | h2 §4 "Antiphonal lament: the duet between two groups" |
| lament refrain | h2 §5 "The lament refrain: the anchor that makes a lament a lament" |
| praise of the dead | h2 §6 "Formulaic grief content: praise of the dead, address to the dead, blame and consolation" (+ table row 4) |
| gendered mourning rules | h2 §7 "Gendered mourning rules" (+ table row 6) |
| fictional mourning register | h2 §9 "Decision table for a fictional mourning register"; h2 §10 "Checklist for designing a fictional mourning register" |

**5. Filename stem words present in the body prose** (`grep -oi <word> <file> | wc -l`): funerary 5, lament 147, dirge 9, formulae 11.

**6. ids cited**: S970, S971, S972, S973, S974 — five distinct ids, each on its own line, each adjacent to the sentence it grounds. All five are above the base registry's highest id (S969, measured by `grep -oE '^\| S9[0-9]{2}' corpus/SOURCES.md | sort -u | tail -3` at base, which returns S967/S968/S969 and `grep -c '^| S97' corpus/SOURCES.md` = 0), so no cited id collides with a base row.

**7. `- topic:` field vs the README index row.** `tools/check-corpus-index.py` extracts the topic with `TOPIC_RE = ^- topic:(.*?)(?=\n- \w)` and compares it byte-for-byte with the README row. I extracted the field with that exact regex and compared it with the frozen topic string: equal. The README row text the L1 must write is therefore the frozen topic verbatim, which `ExecRegistry95` has.

**8. Referenced repo paths all resolve** (checked with `test -f`): `linguistics/orality-formulaic-language.md`, `linguistics/lullaby-child-song-formulae.md`, `linguistics/sacred-registers-liturgical-language.md`, `culture-material/funerary-material-culture.md`, `culture-material/music-instrument-lexicon.md`, `culture-material/dance-performance-movement-codes.md`, `synthesis/worldbible-integration-contract.md` — 7/7 present.

**9. `python3 -B tools/check-source-access.py --root .`** → `ACCESS: 3 flagged rows, 0 findings` (rc 0). The three flagged rows are pre-existing base rows; my entry introduces no flagged row and no cited id is a `rejected` row.

**10. A factual mismatch I found and fixed in my own draft**: the decision table has 11 data rows but my prose said "Twelve rows". Re-measured with the counter's own table parser (11 rows), and the prose now reads "Eleven rows". The row count in the entry now matches the counter's count.

## Entry structure (12 h2 sections)

1. Scope: what this entry owns, and what it refuses to own
2. The lament as a sung register: speech, song, and the boundary between them
3. Professional keeners: the licensed voice of grief
4. Antiphonal lament: the duet between two groups
5. The lament refrain: the anchor that makes a lament a lament
6. Formulaic grief content: praise of the dead, address to the dead, blame and consolation
7. Gendered mourning rules
8. Error patterns: genre confusions to avoid (8 named conflations with a discriminating test each: lullaby-function import, keening vs liturgical requiem, dirge vs funeral march, lament vs elegy, vocative confusion, ritual cry vs speech, mourning-rule confusion, musicalised prose)
9. Decision table for a fictional mourning register (11 data rows × 5 columns: decision / options / what each option gives the culture / what it costs / status)
10. Checklist for designing a fictional mourning register (16 numbered items in three phases)
11. A worked design example (NON-CANON) — the invented Vessemi / *tolo* shore-burn
12. Limits, calibration, and the handoff to the lore world bible

## Sourcing and canon discipline

Every real-world statement in the body carries the id of the source that grounds it, and the quoted span is the evidence. Everything invented is marked NON-CANON: the worked example (§11) is the only invented material and it is flagged at its heading and at its first line. Every design statement carries the `(design, not sourced)` marker — 137 occurrences, counted by `grep -c 'design, not sourced'`. The entry makes no canon claim, no rights ruling and no doctrinal claim; §12 states the non-canon status, the calibration limits, and the handoff to the lore world bible (`synthesis/worldbible-integration-contract.md`), with the handoff explicitly a handoff and never an import.

## Out of scope for this seat

The registry rows (`corpus/SOURCES.md`), the README index row and footer, the round lesson `corpus/lessons/round-95.md` and its Gate table, and the landing of the entry into `corpus/knowledge/linguistics/` are all owned by other seats and by the L1 after WAVE-DONE. I wrote none of them. The claims-O artifacts (grader v6, battery95, mutants95) are outside this seat entirely.

## Tooling

None installed, upgraded or removed: `pdftotext` (poppler) and `curl` were already present on the host, and every check I needed was run with the Python standard library plus the lane's own read-only tools (`tools/check-cited-lines.py`, `tools/check-source-access.py`) and a read-only reproduction of the frozen counter's C1 logic. No pacman transaction (the pacman guard pauses all of them host-wide anyway), no sudo, no host sysctl write. `/home/vgpnk/.omp/agent/RULES.md` was read first.

## Blockers

None. The one dependency (`stage/ScoutTopic95/DONE`) appeared inside the bound.

## Notes for the L1 and the reviewer

- The entry cites five ids; `ExecRegistry95` must land exactly those five (S970–S974) for the "used-by" cell, the registry count and the entry's citations to agree. If the registry lands a different subset, the entry's citations must be re-pointed or the extra rows added — this is a coordination item, not a defect, and the message to `ExecRegistry95` states it.
- `S979` (Erzya dissertation notice) must not be landed as a supporting row: the scout marks it tier C, lead only.
- The entry's `- source:` frontmatter line deliberately carries no id so the one-S-id-per-line lint stays at 0 findings; the ids are on their own `- sources:` sub-lines.
- A mirrored-tree run of the frozen counter over a lands tree with these five rows appended is the L1's step; I did not run the counter against a lands tree because the registry rows do not exist yet at the time of this seat.
