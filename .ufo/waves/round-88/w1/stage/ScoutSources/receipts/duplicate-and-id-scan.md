# Duplicate-URL / scope-collision and reserved-id receipt (round 88, seat ScoutSources)

## 1. The three proposed URLs are absent from every SOURCES registry in the fleet

| searched registry | rows | contains `journals.openedition.org/terrain/17506` | contains `mathshistory.st-andrews.ac.uk` |
|---|---|---|---|
| `audio-shokunin/corpus/SOURCES.md` | 15 | 0 | 0 |
| `chousa-shokunin/corpus/SOURCES.md` | 189 | 0 | 0 |
| `game-dev-2d-shokunin/corpus/SOURCES.md` | 31 | 0 | 0 |
| `game-dev-3d-shokunin/corpus/SOURCES.md` | 36 | 0 | 0 |
| `kagi-shokunin/corpus/SOURCES.md` | 88 | 0 | 0 |
| `kaidoku-shokunin/corpus/SOURCES.md` | 208 | 0 | 0 |
| `kake-shokunin/corpus/SOURCES.md` | 201 | 0 | 0 |
| `kama-shokunin/corpus/SOURCES.md` | 317 | 0 | 0 |
| `kasegi-shokunin/corpus/SOURCES.md` | 99 | 0 | 0 |
| `kengaku-shokunin/corpus/SOURCES.md` | 265 | 0 | 0 |
| `kotoba-shokunin/corpus/SOURCES.md` | 180 | 0 | 0 |
| `kotodama-shokunin/corpus/SOURCES.md` | 854 | 0 | 0 |
| `kumitate-shokunin/corpus/SOURCES.md` | 187 | 0 | 0 |
| `lore-shokunin/corpus/SOURCES.md` | 32 | 0 | 0 |
| `mado-shokunin/corpus/SOURCES.md` | 425 | 0 | 0 |
| `mori-shokunin/corpus/SOURCES.md` | 379 | 0 | 0 |
| `revenger-shokunin/corpus/SOURCES.md` | 479 | 0 | 0 |
| `souji-shokunin/corpus/SOURCES.md` | 211 | 0 | 0 |
| `tabi-shokunin/corpus/SOURCES.md` | 167 | 0 | 0 |
| `tameshi-shokunin/corpus/SOURCES.md` | 171 | 0 | 0 |
| `tsukuroi-shokunin/corpus/SOURCES.md` | 329 | 0 | 0 |

No registry row anywhere in the fleet carries the Terrain article, the MacTutor host, or
either MacTutor page; there is therefore no URL+scope duplicate (census E04) and no
same-URL-across-scopes collision (census W04) for the three new rows.

## 2. Chrisomalis has no registry row anywhere, but is already cited in the corpus

`corpus/SOURCES.md` contains zero occurrences of "Chrisomalis" (grep over 854 rows). The
author is nevertheless already cited inside the corpus, so the new row's scope must not
double-count what the corpus already asserts without a registry receipt:

- `corpus/knowledge/linguistics/numerals-and-measures.md:23` — library-level bibliography, marked not re-fetched
- `corpus/knowledge/linguistics/numerals-and-measures.md:111` — "cumulative tallies, ciphered signs ... are typological stages (Chrisomalis 2010)"
- `corpus/knowledge/linguistics/numerals-and-measures.md:209` — open item: "no entry yet exists for numeral *notation* as a writing subsystem (Chrisomalis-grade detail)"
- `corpus/knowledge/myth-symbol/number-symbolism.md:4,5,15,100,142` — Chrisomalis (2010) *Numerical Notation: A Comparative History*

## 3. Reserved ids S931/S932/S933 are unused at the base revision and everywhere else

| check | command | result |
|---|---|---|
| ids present in base `corpus/SOURCES.md` | `git show 4956282281dac1306cfbe59523e46dde99749d75:corpus/SOURCES.md \| grep -c "S93[123]"` | 0 |
| ids present in base numerals entry | `git show 4956282281dac1306cfbe59523e46dde99749d75:corpus/knowledge/linguistics/numerals-and-measures.md \| grep -oE "\bS[0-9]{3}\b"` | 0 (the entry carries no S-id at all yet) |
| current registry rows / max id / duplicate ids | parsed from `corpus/SOURCES.md` | 854 rows, max S930, 0 duplicate ids |
| S931/S932/S933 free in the current registry | id set difference | yes (registry ids run S001..S930 with holes at 455-... ) |
| S931/S932/S933 in any other lane registry | fleet-wide id scan (21 lanes) | none |

The round-71 `id-renumber-map.json` mentions S931/S932/S933 only as *staged* lane ids that
were renumbered to S946/S947/S948; no registry row ever carried them, so the three ids are
free for this round.

## 4. Lane census state at the moment of this seat (read-only run, no files written)

- `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` -> exit 0
- error-class findings (E01..E12): 0
- warning-class findings (W01..W04): 35 (pre-existing W01 tier-C mined rows and W04 same-URL-across-scopes rows)
- `tools/check-source-access.py --root .` -> exit 0, `ACCESS: 3 flagged rows, 0 findings`
- `tools/check-cited-lines.py corpus/knowledge/linguistics/numerals-and-measures.md` -> exit 0, `CITED-LINES: 0 finding(s) in 1 file(s)`
