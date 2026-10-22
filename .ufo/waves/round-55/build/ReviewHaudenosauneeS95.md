# Review — `haudenosaunee.md` `[S95]` citation identity (round-54 carried item)

Seat: `KotodamaR55.ReviewHaudenosauneeS95` (reviewer, leaf). No files modified; this is a diagnosis plus a proposed landing for the L1. Carried origin: `corpus/lessons/round-54.md:200` (residual list) and `corpus/lessons/round-54.md:178` ("the owner's `[S95]` citation identity clash is carried to Frontier").

## Finding 1 — what `[S95]` means inside the entry: an entry-local key, not a registry id

`corpus/knowledge/civilizations/haudenosaunee.md` defines `S95` itself, in its own provenance ledger:

- `corpus/knowledge/civilizations/haudenosaunee.md:162` — `- **S95:** Grand Council of the Haudenosaunee, signed Chief Leon Shenandoah, Tadadaho. 1995. "Haudenosaunee Confederacy Announces Policy on False Face Masks." *Akwesasne Notes*, Spring, vol. 1; [full transcription hosted by NativeTech](http://www.nativetech.org/cornhusk/maskpoli.html). Text checked in full. ...`
- The same ledger defines every other key used in the entry (N09, D24, M99, O, HCW/HCF/HCC, HCS/HCH/HCCL, HCT/HCL, G92, F98) — all entry-local keys, matching the corpus-wide civilizations convention of a per-entry source ledger (same pattern in `ainu.md` `[S11]` = Strong 2011, `siam-thai.md` `[S1]`–`[S13]`, `nubia-kush.md` `[S32]` = Strabo, `zapotec-mixtec.md` `[S73]` = Smith, `khmer-angkor.md` `[S03]` = Sanderson, `mali-songhai.md` `[S1]`–`[S14]`).
- All in-body uses resolve to that Grand Council policy: lines 78, 133, 134, 137, 138, 139, 140, 141. No line in the entry intends the sign-language source.
- The `- sources:` frontmatter field (line 3) names the same document without an id and needs no change.

## Finding 2 — the clash is real and has a canonical fix already in the registry

- Registry `S095` (zero-padded id space) is unrelated: `corpus/SOURCES.md:124` — Brentari, Fenlon & Cormier, "Sign Language Phonology" (Brentari 2019, Cambridge UP), kind paper, tier A. Any unpadded/`int()`-normalized resolution of `[S95]` lands on a sign-language chapter.
- The cited document already exists in the registry as `S265`: `corpus/SOURCES.md:294` — Grand Council of the Haudenosaunee, signed Chief Leon Shenandoah, Tadadaho, 1995, same *Akwesasne Notes* title, same NativeTech URL; kind `community`, tier B, status `mined`, opened 2026-10-22, `used-by` = `corpus/knowledge/culture-material/masks-masquerade.md` only.
- `corpus/knowledge/culture-material/masks-masquerade.md:69` already cites this same document as `S265` with full section-name locators (`"Exhibition of Medicine Masks"; "Authority over Medicine Masks"`).
- No superseding or sibling registry row carries the same URL (only S265 matches `maskpoli` in `SOURCES.md`).
- I opened the page this session (read tool, plain request, HTTP 200 page text, 2026-10-22). Its actual section headings are: `Medicine Societies`, `Status of Masks`, `Sales of Masks`, `Authority over Medicine Masks`, `Exhibition of Medicine Masks`, `Return of Medicine Masks`. The entry's locators `"Status," "Sales"`, `"Exhibition"`, `"Return"` are prefixes of the real headings; the registry row's anchor cell and `masks-masquerade.md` use the full names.

## Finding 3 — tooling confirms the direction and the safety of the re-cite

- `reports/round-55/accept-c.py:74-81` extracts cited S-ids (`\bS\d{3}\b`) **only from `ENTRY`** (the new `monsters-hybrid-beings.md`). `haudenosaunee.md` is never scanned, so a `[S265]` there cannot touch FLOOR/RANGE/STATUS/USEDBY; editing the file keeps SET intact (the path is already in `base-knowledge-files.txt`). Verified by code read.
- `tools/check-source-access.py` cited leg flags only exact ids of rows whose source/anchor/teaches cells match the bypass regex. Ran it: `ACCESS: 2 flagged rows, 0 findings`, exit 0 — S265's row has no bypass wording, so the re-cite produces no ACCESS findings.
- `tools/check-draft-ids.py:62` (`S\d{3,}`) scopes to draft rows, not knowledge entries; unaffected.
- Recommendation is consistent with `corpus/lessons/round-54.md:178`: "the Haudenosaunee line keeps S265 (the Grand Council's own text, which this entry's restricted-tradition rule asks for)".

## Recommended minimal fix (option a: re-cite to registry S265)

Why not option (b): renaming the local key (e.g., `GC95`) touches the same nine lines but leaves one document with two corpus identities and keeps an id-shaped token in the local keyspace — the defect is named an "identity clash," so resolve it at the cause.

### `corpus/knowledge/civilizations/haudenosaunee.md`

```
:78 OLD | Medicine beings | The mask policy identifies sacred medicines and obligations to community welfare. [S95] | Restricted context; do not extract a fantasy bestiary or catalogue of powers. |
:78 NEW | Medicine beings | The mask policy identifies sacred medicines and obligations to community welfare. [S265] | Restricted context; do not extract a fantasy bestiary or catalogue of powers. |

:133 OLD - “False Face” is retained as the assignment's and historical literature's label; S95 discusses **medicine masks** and the societies responsible for them. These are not entertainment masks or a public costume category.
:133 NEW - “False Face” is retained as the assignment's and historical literature's label; S265 discusses **medicine masks** and the societies responsible for them. These are not entertainment masks or a public costume category.

:134 OLD - The Grand Council's 1995 statement, signed by Tadadaho Chief Leon Shenandoah, identifies wooden and cornhusk masks, medicine societies, sacred duties, and community welfare. That is the public contextual limit used here. [S95]
:134 NEW - The Grand Council's 1995 statement, signed by Tadadaho Chief Leon Shenandoah, identifies wooden and cornhusk masks, medicine societies, sacred duties, and community welfare. That is the public contextual limit used here. [S265]

:137 OLD | Who holds authority? | Medicine societies and the Grand Council, not a collector or museum. [S95, “Authority over Medicine Masks”] | Outsider ownership or a catalogue entry cannot authorize reconstruction. |
:137 NEW | Who holds authority? | Medicine societies and the Grand Council, not a collector or museum. [S265, “Authority over Medicine Masks”] | Outsider ownership or a catalogue entry cannot authorize reconstruction. |

:138 OLD | Are small/new/commercial examples exempt? | The policy calls all wooden and cornhusk medicine masks sacred regardless of size or age, and rejects commercial production. [S95, “Status,” “Sales”] | Do not invent a tourist-object exception as permission. |
:138 NEW | Are small/new/commercial examples exempt? | The policy calls all wooden and cornhusk medicine masks sacred regardless of size or age, and rejects commercial production. [S265, “Status of Masks”, “Sales of Masks”] | Do not invent a tourist-object exception as permission. |

:139 OLD | May images be used as design references? | The policy opposes public exhibition and exhibition use of reproductions, photographs, castings, or illustrations. [S95, “Exhibition”] | No mask images, facial pattern descriptions, replica instructions, or “inspired” ritual ensemble here. |
:139 NEW | May images be used as design references? | The policy opposes public exhibition and exhibition use of reproductions, photographs, castings, or illustrations. [S265, “Exhibition of Medicine Masks”] | No mask images, facial pattern descriptions, replica instructions, or “inspired” ritual ensemble here. |

:140 OLD | Is old ethnography unrestricted knowledge? | S95 says information about medicine societies is not for general distribution and rejects outsider presentation of their significance. | Publication history does not settle cultural authority or access. |
:140 NEW | Is old ethnography unrestricted knowledge? | S265 says information about medicine societies is not for general distribution and rejects outsider presentation of their significance. | Publication history does not settle cultural authority or access. |

:141 OLD | What about museum holdings? | S95 calls for return to the Grand Council for appropriate care. [S95, “Return”] | Treat custody and repatriation as living obligations, not lost-civilization salvage. |
:141 NEW | What about museum holdings? | S265 calls for return to the Grand Council for appropriate care. [S265, “Return of Medicine Masks”] | Treat custody and repatriation as living obligations, not lost-civilization salvage. |

:162 OLD - **S95:** Grand Council of the Haudenosaunee, signed Chief Leon Shenandoah, Tadadaho. 1995. “Haudenosaunee Confederacy Announces Policy on False Face Masks.” *Akwesasne Notes*, Spring, vol. 1; [full transcription hosted by NativeTech](http://www.nativetech.org/cornhusk/maskpoli.html). Text checked in full. This is a statement of the issuing authority's policy, not an outsider declaration that every individual has identical practice.
:162 NEW - **S265:** Grand Council of the Haudenosaunee, signed Chief Leon Shenandoah, Tadadaho. 1995. “Haudenosaunee Confederacy Announces Policy on False Face Masks.” *Akwesasne Notes*, Spring, vol. 1; [full transcription hosted by NativeTech](http://www.nativetech.org/cornhusk/maskpoli.html). Registry row: `corpus/SOURCES.md` S265 (opened 2026-10-22; kind community, tier B). Text checked in full. This is a statement of the issuing authority's policy, not an outsider declaration that every individual has identical practice.
```

Locator completions on :138/:139/:141 use the page's real heading names (verified this session) and match the S265 anchor cell and `masks-masquerade.md:69` convention. Strict id-only swaps also work; completing the locators is free since the lines are being edited anyway.

### `corpus/SOURCES.md` (row `| S265 |`, used-by cell only — permitted in-place change per SOURCES.md header, log old→new in `corpus/lessons/round-55.md`)

```
OLD ... | mined | 2026-10-22 | 365d | corpus/knowledge/culture-material/masks-masquerade.md |
NEW ... | mined | 2026-10-22 | 365d | corpus/knowledge/culture-material/masks-masquerade.md, corpus/knowledge/civilizations/haudenosaunee.md |
```

This keeps the registry invariant (`mined` = "cited by the paths in `used-by`") true for the new citation.

### Do not touch

- `corpus/lessons/round-54.md:178,200` and `corpus/lessons/round-54-verifier-spotcheck.md` — historical records; lessons are append-only.
- No other file references the entry's local `S95` key (corpus-wide grep found `S95` only in `haudenosaunee.md` and the round-54 lesson records).

## Residual risk / gaps

- Same latent ambiguity class elsewhere: sibling entries carry unpadded S-shaped local keys (`ainu.md` `[S11]`, `siam-thai.md` `[S13]`, `nubia-kush.md` `[S32]`, `zapotec-mixtec.md` `[S73]`, `khmer-angkor.md` `[S03]`, `mali-songhai.md` `[S1]`–`[S14]`). None was carried as a defect this round and none of those documents is known to have a registry row; flagging for Frontier only — a lint over knowledge files for local keys matching `\bS\d+\b` would find the whole class if the L1 wants it.
- Unrun checks: `accept-c.py` not executed (by design it fails SET/FLOOR pre-landing; its citation scan is `ENTRY`-only per code read). `check-draft-ids.py` not run (out of path). `check-source-access.py` run once: `ACCESS: 2 flagged rows, 0 findings`, exit 0.
- Source opened this session (route per source norms): `http://www.nativetech.org/cornhusk/maskpoli.html` via `read` tool, direct plain request, page text retrieved, 2026-10-22 — used only to confirm the five section-heading strings above.
- No tool installs or updates; no registry/lane writes performed by this seat.
