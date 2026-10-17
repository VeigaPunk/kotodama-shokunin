# Round-8 metadata sweep, fragment M06 — synthesis files 1–12

- Worker shard: M06 (metadata sweep; `corpus/knowledge/synthesis/` positions 1–12).
- Date: 2026-10-17. Declared round baseline `e7ca0faeb6680fa9891b907be628d9db578c28f4`; working-tree parent at edit time `cf338a713060f274269cdacb18cdc0085bb06aeb` (edits uncommitted; workers do not commit).
- Selection command: `ls corpus/knowledge/synthesis/*.md | LC_ALL=C sort | sed -n '1,12p'` → conlang-blueprint-template.md, consistency-verification-checklist.md, contact-scenario-builder.md, costume-language-coupling-table.md, coupling-model.md, cultural-translation-protocol.md, deity-name-derivation-pipeline.md, dialect-faction-map-workflow.md, era-language-staging.md, era-myth-language-costume-matrix.md, glossary-registry-format.md, loanword-material-dating.md.
- Protocol basis: the SCORECARD "Planned" debt "corpus metadata conformance (`source`/`verified-at`/`recheck`)" and the sweep contract in `reports/round-8/targets.json` (`metadata_sweep`). House convention read off the entries that already carry the triple: `glossary-registry-format.md:6–8`, `coupling-model.md:14–15`, and the corpus-wide `- source:` examples (7 files, `grep -rln '^- source:' corpus/knowledge/`).
- Method: read each file's header block and its own provenance/verification section; add the missing header fields **in place**, with content grounded in what the entry itself records (section pointer named in each added line). No source re-retrieval was performed — live source rechecks are the F claim's work, not this sweep's. No sibling or shared file was touched; no commit made.

## Per-file results

Before state = presence of `- source:` / `- verified-at:` / `- recheck:` in the header block.

| # | File | Before | Action | Grounding pointer for the added lines |
|---|---|---|---|---|
| 1 | `conlang-blueprint-template.md` | — / — / — | added 3 fields | "Source register and verification boundaries" (register + "Verification date: 2026-10-17"); "Specific historical borrowings require their own source dossier"; "editorial acceptance gates, not claims to have implemented fleet verdict scripts" |
| 2 | `consistency-verification-checklist.md` | — / — / — | added 3 fields | "Checkable editions and what a worldbuilder can take" ("not a fresh page-by-page verification of their contents"); calibration section's claim-specific uncertainty rule |
| 3 | `contact-scenario-builder.md` | — / — / — | added 3 fields | §13 ("Verification scope here is bibliographic records, publisher descriptions/contents…"; Sidebotham contents checked 2026-10-17) |
| 4 | `costume-language-coupling-table.md` | — / — / — | added 3 fields | `- sources:` list ("accessed 2026-10-17"); "Provenance cautions and open verification" (collection API re-checked 2026-10-17) |
| 5 | `coupling-model.md` | — / ✓ / ✓ | added `- source:` only | source block above; "Provenance cautions and known gaps" ("bibliographic metadata, not a fresh complete reading") |
| 6 | `cultural-translation-protocol.md` | — / — / — | added 3 fields | §14 ("strongest evidence is bibliographic and conceptual"; Appiah direct full-text collation still open); source-block check levels |
| 7 | `deity-name-derivation-pipeline.md` | — / — / — | added 3 fields + base declaration on the `- couples:` line | §11 "Verification boundary" (Tacitus §43, Mishnah, JPS Exodus checks) and "Open debt" (Apollo/Athena, Ugaritic garment terms) |
| 8 | `dialect-faction-map-workflow.md` | — / — / — | added 3 fields | §13 "Verification scope" (DOI/abstract/catalogue/frontmatter level) and "Stop rule" |
| 9 | `era-language-staging.md` | — / — / — | added 3 fields | §12 "Source/verification record" ("checked 2026-10-17…") and its existing "Recheck:" bullet |
| 10 | `era-myth-language-costume-matrix.md` | — / — / — | added 3 fields | §12 ("Verification date: 2026-10-17. …not a claim that every cited book was read in full") |
| 11 | `glossary-registry-format.md` | ✓ / ✓ / ✓ | none — already conformant | n/a |
| 12 | `loanword-material-dating.md` | — / — / — | added 3 fields | §1 "Verification scope" ("checked 2026-10-17…") and §11 handoff audit |

Totals: 11 files edited (32 insertions, 1 deletion); 1 file no edit; 36 field lines present across the 12 files after the pass (12 × 3, `grep -h` count).

## Defect fixed in place (beyond field presence)

- `deity-name-derivation-pipeline.md` — its `- couples:` line used `corpus/knowledge/`-relative paths (`linguistics/…`, `myth-symbol/…`, `culture-material/…`) without declaring the base, unlike the sibling `glossary-registry-format.md:5` which states "Paths above are relative to `corpus/knowledge/`." All 15 referenced files resolve only under the `corpus/knowledge/` base (check below). Fix: appended the same base declaration to the `- couples:` line; no path rewritten. Evidence: the pre-edit line is the `-` side of `git diff -- corpus/knowledge/synthesis/deity-name-derivation-pipeline.md`.

## Checks run (command → output)

1. Provenance gate, before and after (12 files):
   `python3 tools/gates/provenance-audit.py $(ls corpus/knowledge/synthesis/*.md | LC_ALL=C sort | head -12)`
   → before: `INFO scan: files=12 marks=55 mark-lines=51 findings=0 blocked=0`, exit 0;
   → after: identical line, exit 0. The pass adds no gate finding and leaves the `(to-verify)` inventory unchanged (55 marks on 51 lines both runs; two draft recheck lines that had introduced literal marks were reworded before final measurement).
2. `- couples:` path resolution (backticked and markdown-link targets, brace expansion, `../` relative to the file, bare paths relative to `corpus/knowledge/`): inline Python over the 12 files → `checked=126 broken=0`. Before the fix, file 7's paths resolved only under the undeclared base (no broken target once the base is assumed) — the defect was the missing declaration, not a dead path.
3. Header section-pointer check (every `§N` in the header block resolves to a `## N.` section of the same file): all resolve; the single exception is `deity-name-derivation-pipeline.md`'s `§43`, which cites Tacitus *Germania* 43, a source location, not a file section.
4. Field presence after: `grep -c '^- source:' / '^- verified-at:' / '^- recheck:'` → 1 / 1 / 1 for each of the 12 files.
5. Scope: `git diff --numstat -- corpus/knowledge/synthesis/<my 12>` → 11 files, 32 insertions / 1 deletion; `git status` shows no other path touched by this shard. (A sibling metadata shard, synthesis 13–24, landed edits concurrently; those files are not part of this fragment.)
6. Line counts before → after: +3 for files 1–4, 6, 8–10, 12; +1 for coupling-model; +3 for deity (plus the modified couples line). `glossary-registry-format.md` unchanged at 224.

## Limits

- The `- verified-at:` additions state what the metadata pass checked (header fields, couples-path existence, source-list form) and restate the verification levels the entry itself already records, with section pointers; they do not claim a new content verification, page retrieval, or quotation check. Files whose bodies record no check date (e.g. 2, 6, 7, 8) carry no invented date for their own source checks — the dated part is this pass.
- Sources were not re-retrieved; freshness receipts belong to the F claim. Link-level access was not re-tested here.
- The `- source:` lines describe the entry's provenance basis and the lane-authored-vs-external distinction where the file already states it; they add no new source claims.
- No commit, no LOG.md/SKILL/SCORECARD edit, no sibling or world-bible write from this shard.
