# ScribeLullaby94 — report

Seat: ScribeLullaby94 · lane: kotodama-shokunin · milestone r94-v1 · axis: coverage (claim C).
Scope: draft the lullaby entry text only. No registry row, no README row, no claim-A pointer edit — those belong to
ExecRegistry94 / ExecAdjacency94 and to the L1's integration. No lane production file was written by this seat.

## 1. Files written

| path (lane-relative) | bytes | role |
|---|---|---|
| `.ufo/waves/round-94/w1/stage/ScribeLullaby94/lullaby-child-song-formulae.md` | 43411 | the entry draft (target path `corpus/knowledge/linguistics/lullaby-child-song-formulae.md`) |
| `.ufo/waves/round-94/w1/stage/ScribeLullaby94/DONE` | 65 | written last; contains the entry's sha256 |
| `.ufo/waves/round-94/w1/ScribeLullaby94.md` | — | this report trailer |

Entry sha256: `4b6e331a4d7177966c491007238a62915f30767a03e39082f08e8a2a9df657b1`.

## 2. Measurements (each with its command)

All commands run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

| # | what | command | rc | result |
|---|---|---|---|---|
| M1 | byte size | `wc -c .ufo/waves/round-94/w1/stage/ScribeLullaby94/lullaby-child-song-formulae.md` | 0 | **43411 bytes** (predicate floor 12000) |
| M2 | count of `## ` sections | `grep -c '^## ' <file>` | 0 | **11** (predicate floor 6) |
| M3 | table dimensions | inline python: split the file on lines starting with `|`, group contiguous runs, count `split('|')[1:-1]` of the header row | 0 | table 1 at line 155: **4 data rows × 4 columns**; table 2 at line 243: **12 data rows × 5 columns** (predicate: ≥1 table with ≥5 data rows and ≥3 columns) |
| M4 | clause-scoped citations | `python3 -B tools/check-cited-lines.py <file>` | **0** | `CITED-LINES: 0 finding(s) in 1 file(s)` — no MULTI-ID, no TABLE-ID (QUALITY.md criterion 15) |
| M5 | topic line byte-equality to the frozen claim | inline python: compare the `- topic:` line's text against `json.load(...)['C']['topic']` | 0 | **True**, 277 chars each — verbatim |
| M6 | S-ids used ⊆ scout's rows | inline python: `set(re.findall(r'\bS[0-9]{3,}\b', entry)) <= set(re.findall(r'^\| (S[0-9]{3,}) \|', rows.md, re.M))` | 0 | **True** — used = [S965, S966, S967, S968, S969]; scout rows = S965–S969 |
| M7 | every quoted span is a substring of its capture | inline python + `open()`: for each line carrying exactly one S-id, check each `"..."` span of ≥12 chars against that row's capture file | 0 | **14/14 quoted spans exact** (the entry quotes 14 spans of ≥12 chars across 14 lines; all are exact substrings of their row's capture); no finding |
| M8 | no design line carries an S-id | inline python: flag any line holding both `(design, not sourced)` and an S-id | 0 | **0 findings** |
| M9 | header block | inline python: check lines 1–12 | 0 | `# Lullaby and child-directed song formulae`; `- topic:` (verbatim); `- sources:` listing only S965–S969; `- verified-at: 2026-11-05`; `- recheck: 180d`; `- couples:` (connector's line, byte-identical) |

## 3. Section inventory

- line 14: ## 1. Scope and what this entry owns
- line 28: ## 2. The speech of putting a child to sleep
- line 52: ## 3. Nonsense syllable refrains
- line 85: ## 4. Archaic retention in lullaby text
- line 114: ## 5. Address to the child
- line 141: ## 6. Register shift between the song and ordinary speech
- line 172: ## 7. Tune and tone: the carrier, and where this entry stops
- line 201: ## 8. The lullaby as archive
- line 237: ## 9. Decision table for a fictional lullaby register
- line 264: ## 10. A worked design example (NON-CANON)
- line 291: ## 11. Limits, open questions and the handoff

## 4. The six required phrases, and where each was found

Each appears in a **section heading** (predicate accepts heading or table-cell text):

| phrase | heading line | heading text |
|---|---|---|
| `nonsense syllable` | line 52 | ## 3. Nonsense syllable refrains |
| `archaic retention` | line 85 | ## 4. Archaic retention in lullaby text |
| `address to the child` | line 114 | ## 5. Address to the child |
| `register shift` | line 141 | ## 6. Register shift between the song and ordinary speech |
| `tune and tone` | line 172 | ## 7. Tune and tone: the carrier, and where this entry stops |
| `lullaby as archive` | line 201 | ## 8. The lullaby as archive |

All six are present (predicate floor: four). Counts over the whole file, case-insensitive (`re.findall(re.escape(p), entry, re.I)`):
`nonsense syllable` 2, `archaic retention` 3, `address to the child` 3, `register shift` 4, `tune and tone` 1,
`lullaby as archive` 1.

## 5. S-ids cited, with line numbers

Every S-id cited is one ScoutLullaby94 opened (M6). Each appears on a line that carries **exactly one** id (M4).

| S-id | source | citation lines in the entry |
|---|---|---|
| S965 | Geneix-Rabault & Wacalie 2019 (TIPA 35), Kanak lullaby repertoire | header 5; body 34, 62, 145, 213, 215 |
| S966 | Ó Madagáin 1985 (Scottish Studies 29), Gaelic/Irish vocable chorus | header 6; body 56, 58, 60, 97, 118, 120, 297 |
| S967 | Nurijeva 2024 (Mäetagused 90), Udmurt two-layer lullaby | header 7; body 32, 89, 91, 93, 95, 217, 299 |
| S968 | Le Hénaff et al. 2024 (Contextes et didactiques 23), Tahitian comptine taught in Breton nursery schools | header 8; body 149, 151, 180, 301 |
| S969 | Okon 2021 (Art and Design Review 9), Ibibio cradle-song sound devices and apostrophe | header 9; body 64, 122, 182, 303 |

The `- sources:` header block lists only these five ids.

## 6. Sourcing discipline as implemented

- Each line stating a fact about a real language or people carries **exactly one** S-id, on the same line (M4, M8).
- Each design statement about the fictional register carries the literal label `(design, not sourced)` **on the same line**
  and cites no S-id. A scripted pass appended the label to the 43 list-item lines whose parent paragraph carried it only
  in aggregate; header lines (`- topic:`, `- sources:`, `- verified-at:`, `- recheck:`, `- couples:`) were excluded.
- All 14 quoted spans in the entry are exact substrings of their row's committed capture under
  `.ufo/waves/round-94/w1/stage/ScoutLullaby94/evidence/` (M7); four spans were widened to the scout's full located quote
  during this seat's pass (S966 vocable chorus, S966 Combarieu formula, S967 improvised group, S967 supplanting).
- No claim is made about a source beyond what its quoted span supports: §11 states the scope limit of each of the five cases
  (abstract-level for S967, single classroom setting for S968, selected repertoire for S969, hypothesis-not-result for S966).

## 7. Boundary and NON-CANON labelling

- The connector's **owner boundary sentence** is reproduced verbatim in §1, together with its `- couples:` line byte-identical
  to `ConnectorLullaby94/overlap.md:49`.
- The entry states no canon, no lore acceptance, no real-world rights and no cultural permission (§1, §11).
- The worked design example (§10) is labelled **NON-CANON** in the section heading and in its first line; §1 and §11 carry the
  NON-CANON label for the entry as a whole. Three `NON-CANON` occurrences in the file.
- The entry ends with a handoff paragraph to lore-shokunin's world bible (§11), using the vocabulary of
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` (packet, claim ledger, canon decision, `to-verify` items).
- QUALITY.md criterion 4 (usability): §9 is a **12-row × 5-column decision table** for a fictional lullaby register; §10 is a
  worked design example (the Tavrin, NON-CANON).
- QUALITY.md criterion 3 (coupling): the `- couples:` line names nine owners, one clause each.

## 8. Not measured / not done by this seat

- The entry was **not** landed into `corpus/knowledge/`; the L1 integrates it. `corpus/README.md`'s linguistics index, the
  `## linguistics/` count and the footer totals are therefore untouched and are the L1's to move.
- `corpus/SOURCES.md` was **not** edited. The five rows S965–S969 exist only in the scout's staged `rows.md`; ExecRegistry94
  owns the registry landing.
- Claim A (the two dangling greeting pointers) and claim O (the grader v5) are outside this seat's scope.
- The INDEX leg (`tools/check-corpus-index.py`) and the CENSUS leg cannot pass until the entry is landed and the README is
  updated by the L1; this seat did not run them against a landed tree and does not claim their outcome.
- Freshness: no freshness claim is declared, consistent with the frozen obligation in `claims.json`.

## 9. Tooling

**None installed or upgraded.** No pacman transaction was run, no sysctl was touched, no browser automation was used, and no
source was fetched by this seat — every source byte comes from the scout's staged captures, which were opened by plain `curl`
with the default user agent. `pdftotext` (poppler) was used by the scout to render the three PDFs; this seat only read the
already-rendered `.txt` files.

Scratch `/fast/scratch/hyaku/kotodama-r94/ScribeLullaby94/` was deleted before this seat yielded.
