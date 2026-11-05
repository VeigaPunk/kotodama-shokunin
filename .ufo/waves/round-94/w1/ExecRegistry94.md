# ExecRegistry94 — round 94 claim C registry rows and index row (stage only)

Stage: `.ufo/waves/round-94/w1/stage/ExecRegistry94/` (DONE = sha256 of SOURCES.append.md).
Scratch `/fast/scratch/hyaku/kotodama-r94/ExecRegistry94/` deleted before yield. No production file, commit or git mutation.

## Dependencies
- Waited with the bounded loop (45 × 60 s) for `ScoutLullaby94/DONE` and `ScribeLullaby94/DONE`; both appeared within the bound (wall 1680 s).
  - ScoutLullaby94/DONE = 384f13f18cfc407cf0561070ed176b934d27eb1c1ec06603676ce87a97b9bd1c
  - ScribeLullaby94/DONE = 4b6e331a4d7177966c491007238a62915f30767a03e39082f08e8a2a9df657b1

## Rows added (5; claim C needs ≥3)
S965, S966, S967, S968, S969 — all tier A, kind paper, status mined, opened 2026-11-05, recheck 180d, used-by `corpus/knowledge/linguistics/lullaby-child-song-formulae.md`.
Each is cited by id in the entry body (grep: S965–S969 all present in the entry).

## Normalisation performed (scout rows.md → census grammar)
- Cell count: all 5 rows already have 11 cells (awk field count NF=13 incl. edge pipes; `awk -F'|' '/^\| S96[5-9] \|/{print NF}'` → `5 13`). No cell contains a pipe.
- Recheck: already `180d` (valid NNd). No change; no prose moved to a Gate block.
- used-by: already the exact entry path. Status `mined`. Tier A. Opened `2026-11-05` (ISO).
- **Only change:** the primary located quote was appended to each anchor cell as `; anchor quote "…"` (so the anchor carries an exact capture substring ≤25 words, per claim C's SOURCES leg). Each quote's exact-substring count in its capture was measured with python `str.count` = 1 for all five (S965.html, S966.txt, S967.txt, S968.html, S969.txt, under `ScoutLullaby94/evidence/`). Word counts 14, 13, 12, 17, 12.
  - S965 anchor: `…; accessed 2026-11-05; reports/round-94/evidence/S965.html` → `…; accessed 2026-11-05; reports/round-94/evidence/S965.html; anchor quote "Les premières berceuses qui sont adressées aux nouveau-nés sont constituées de sons vocaux rythmiques"`
  - S966, S967, S968, S969 analogous, quotes: "function of nonsense vocables is strongly indicated by a story which Donald Archie"; "intonations that are meant to soothe or put the child to sleep"; "une version lente chantée de la comptine ainsi que des enregistrements des trois vers en version parlée"; "the refrain stands out as the leading sound modulator in the song."

## Collision check (run on base SOURCES.md and again on the mirror)
- Command: `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort -u`
- Base: 888 distinct ids, highest S964. Ids S965+ in base: none (`grep -oE '^ {0,3}\|[[:space:]]*S(9[6-9][0-9]|[0-9]{4,})'` returns only S960–S964, which are the base rows).
- Mirror after append: 893 distinct ids, 0 duplicate ids (`uniq -d` → 0).

## Census (`scripts/sources-census.sh validate --file <mirror>/corpus/SOURCES.md`)
- Final: exit 0, 35 W0-class warnings (same 35 as the base file's validate run: base run exit 0, 35 W0 lines), 0 E-codes, 0 findings on S965–S969. Output in `census.txt`.
- Mirror setup note: the first mirror run returned rc 1 with E11 (`S859 used-by SKILL.md`, `S860 used-by SKILL.md`, `S897 used-by tools/ledger-token-guard.py`). E11 resolves used-by paths against the lane root, and the scratch mirror held only `corpus/`. I copied `SKILL.md` and `tools/ledger-token-guard.py` into the scratch mirror root (scratch only, no production change). After that the run was rc 0. The base file does not need this because the lane root is complete.

## Index (`python3 -B tools/check-corpus-index.py --root <mirror>`)
- Final: `CORPUS-INDEX: OK files=266 rows=266 findings=0`, exit 0. Output in `index.txt`.
- Before the README edit the same command returned exit 1 with 5 findings (MISSING_ROW, HEADER_DRIFT, TOTALS_DRIFT, FOOTER_TOTAL, FOOTER_DIR_TOTALS) — the expected result of the new file without its index row and counts.
- Index row form: `- \`lullaby-child-song-formulae.md\` — <topic text verbatim>` inserted before `morphological-typology.md` (filename order after `linguistic-anthropology.md`) in `## linguistics/`, which moved (38) → (39). The topic text is the entry's `- topic:` line verbatim (the checker's TOPIC_MISMATCH leg passes).
- README footer: new section `## Round 94 lullaby entry (2026-11-05)` with `Total knowledge entries: 266.` and footer `(total 266 files; directory totals 39/36/43/29/24/95).` A `revision: 2.23` block was added above `revision: 2.22`.
- Diff against base README (`git show e7fa8eaf…:corpus/README.md`): `README.diff` (20 `+` lines, 1 `-` line: the `(38)` heading; the `-` count via `grep -c '^-[^-]'` = 1 header line from `---` excluded).

## Files written (stage)
- `SOURCES.append.md` — the 5 rows (sha256 57b641403d0f0497f402ceb7dbfaa9e8656c32b64ecf9665c38ed838ff784e73)
- `README.new.md`, `README.diff`
- `census.txt`, `index.txt`
- `DONE` (sha256 of SOURCES.append.md)

## Not done / for the L1 at integration
- SOURCES.md search-log note not written (the spec asked for rows only in SOURCES.append.md); the L1 may add one under `## Search log` if the APPENDONLY leg needs it.
- The lane's `corpus/SOURCES.md` and `corpus/README.md` are not edited here; the L1 lands `SOURCES.append.md` (insert after the S964 row, before `## Paths`) and `README.new.md`.
- Entry copy used: `ScribeLullaby94/lullaby-child-song-formulae.md` (43411 bytes, 11 `## ` headings, sha256 4b6e331a4d7177966c491007238a62915f30767a03e39082f08e8a2a9df657b1). Not modified by this seat.

## Tooling
None installed or updated.
