# Round-8 metadata sweep — M08 linguistics (NON-CANON)

- worker: M08; assignment: audit `corpus/knowledge/linguistics/` — all 16 entries — frontmatter (`source` / `verified-at` / `recheck`); fixes in place on own-lane files only.
- snapshot: 2026-10-17T20:19:01Z (UTC); baseline HEAD `cf338a713060f274269cdacb18cdc0085bb06aeb` (working tree carries the 16 in-place edits; not committed — the orchestrator integrates and commits once per round).
- scope: exactly the 16 `corpus/knowledge/linguistics/*.md` entries + this fragment. No other partition (civilizations, synthesis, myth-symbol, culture-material, verification) touched; those belong to sibling M-workers. No network retrieval was performed — every receipt below is an in-repo record.
- protocol basis: the SCORECARD "Planned" debt "corpus metadata conformance" (`SCORECARD.md:121`) and the sweep contract in `reports/round-8/targets.json` (`metadata_sweep`); house convention read off entries already carrying the triple (e.g. `corpus/knowledge/civilizations/burma.md:12`, `corpus/knowledge/civilizations/mali-songhai.md:14`). All 16 linguistics entries already carried `- sources:` (including multi-line source blocks), so only `- verified-at:` and `- recheck:` were missing.

## 1. Finding (before state)

Command (2026-10-17T20:15:49Z), header block = lines up to the first `## `:

```
python3 - <<'EOF'   # regex audit: ^-\s+<field> in the header block, per file
...
EOF
```

Result (before): `topic=16 sources=16 couples=16 verified-at=0 recheck=0` — every linguistics entry carries `- topic:` / `- sources:` / `- couples:`, but **0/16 declare `- verified-at:` or `- recheck:`**. The round-4 apparatus audit (`corpus/lessons/round-4-audit/linguistics.md`, snapshot HEAD `c610e0a`) checked only the three older fields (48/48 nonempty), so this gap was previously unflagged.

## 2. Fix applied (all 16 files)

In each header block, between the `- sources:` value block and the `- couples:` line, two fields were inserted:

- `- verified-at: 2026-10-17 — …` stating the entry's actual recorded verification history at its actual access level, with record pointers;
- `- recheck: …` stating use-trigger conditions and the re-run rule.

Exactly +2 lines per file; no other line modified (`git diff --numstat`: `2  0` for each of the 16 files; `git diff --check`: clean).

Two honest verification classes:

- **Group A (6 entries)** — a dated live source recheck exists on record (supplement-opencode-1, plus round-5 follow-ups). The field cites the audit record and its claim dispositions. Rows: color (color.json: 7 claims — 4 supported / 1 contradicted / 2 unresolved; r5 `10.json` COL-06–07), kinship (kinship.json: 9 — 6/1/2; r5 `11.json` KIN-A07–A08), orality (orality.json: 5 — 3/1/1; r5 `12.json` ORALITY-05), phonetics (phonetics.json: 11 — 7/3/1; r5 `12.json` PHON-A11), semantic-fields (lexicon.json: 5 — 3/2), sociolinguistics (registers.json: 8 — 5/1/2; r5 `13.json` SR-REG-04/07).
- **Group B (10 entries)** — no dated source recheck on record. The field says "apparatus audit only" (round-4 report, HEAD `c610e0a`), carries the negative-claim sweep (below), and marks the cited figures `(to-verify)` at handoff. Two entries additionally carry their open round-4 findings: politeness FLAG-01, semantics-pragmatics CAL-01 (not repaired here — outside a frontmatter sweep).

### Per-file rows (sha256 before `HEAD:<path>` → after working tree; short16)

| entry | history on record | verified-at class | sha256 before → after |
|---|---|---|---|
| color-terminology.md | color.json 7 rows; r5 10.json | A | d9b20414439959dd → 7ee9f7e45d8a63ac |
| conlang-methodology.md | — | B | d8e8cd835e1b8cd0 → 272329f70c1fe93e |
| historical-linguistics.md | — | B | 258350fbe09059a9 → 019f28f09ceac28a |
| kinship-terminology.md | kinship.json 9 rows; r5 11.json | A | 5dd68cea0e42771b → c51d3483a27b0943 |
| language-contact.md | — | B | 3d4d77749bd894b0 → 52385e3d81f7d8f8 |
| linguistic-anthropology.md | — | B | 6e6ab88da0205d91 → ffa38d0f2e89a774 |
| morphological-typology.md | — | B | 1b6a413e87879279 → b423e811651aca42 |
| naming-systems.md | — | B | 9542d71b9025e8ad → d972a1d65e7a8fba |
| orality-formulaic-language.md | orality.json 5 rows; r5 12.json | A | d765c5b2c4c17b69 → f827bbee6f305466 |
| phonetics-phonology.md | phonetics.json 11 rows; r5 12.json | A | dd132967cd9502b5 → b4f9b00384bc6840 |
| politeness-taboo-euphemism.md | — (FLAG-01 open) | B | 7fe13a118539dc46 → a73c0b1fb8fd0052 |
| semantic-fields-lexicon-building.md | lexicon.json 5 rows | A | 674d7be5f0743609 → 80b5e2c89fc8a97b |
| semantics-pragmatics.md | — (CAL-01 open) | B | b36694fb3d066ff4 → 9b9a3ff757fe3290 |
| sociolinguistics-registers.md | registers.json 8 rows; r5 13.json | A | 9a98f945ed4d0312 → 95ea235f9e10e2ef |
| syntax-typology.md | — | B | 7b1c488743f68a2e → 258accfd4e435628 |
| writing-systems.md | — | B | 03b6a7adc9fa66a8 → 76263260dd8181ba |

Full hashes (command: `for f in corpus/knowledge/linguistics/*.md; do git show HEAD:$f | sha256sum; sha256sum $f; done`, 2026-10-17T20:19Z):

```
color-terminology.md                d9b20414439959dd6c5b1aa1fefcc110112ebeb972322557e5147a5444b4c916 -> 7ee9f7e45d8a63ac4362a95d71db923dde118d4a1f0a598fa0a0888e68105992
conlang-methodology.md              d8e8cd835e1b8cd0c69d2f609ecb2a451915d74adb8e7fd013f2b30bdbc5eb0b -> 272329f70c1fe93e47f47d8c2618371902d1e5ccc78b6987abf437e101ac77ea
historical-linguistics.md           258350fbe09059a910caddfcbd9c1cdb5d7ef37c5e15cf202977fc26e2653dbd -> 019f28f09ceac28a1bcb6685f756170b66944129a6b3dca17ca76d9663ab3caf
kinship-terminology.md              5dd68cea0e42771b0bc8bf208cd3a4d257d0822d5f31392151d6340361545213 -> c51d3483a27b0943b257fa25287d0dec4dba3fe16f737b1893ce237ba92c07f8
language-contact.md                 3d4d77749bd894b063ceb6f03427f7d1052af0d7ee667a975912765747509507 -> 52385e3d81f7d8f8eb1423d408a47bd12c968f1444fd9fc5d77a9c3e691cd409
linguistic-anthropology.md          6e6ab88da0205d91e151ca18d9a57b9837608aaf94b19146b385280ffba656df -> ffa38d0f2e89a774f373c9759978e8bd173e6e28b1f5cc1b1c87847fd5e54458
morphological-typology.md           1b6a413e87879279bef0eafc5348490d0e51952eef7ea5a02a9035034dfa2f6c -> b423e811651aca4229e6621dd2a884df360a53809230778aa85bef6376dfeddb
naming-systems.md                   9542d71b9025e8ad76209ac6b999099abe4fe42c5cac61137fd602916cc94e7c -> d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d
orality-formulaic-language.md       d765c5b2c4c17b695ce14d0e4a06a04957daece5859820eb09c55379be81e9bc -> f827bbee6f305466a17a8b6e911539c38820e6865eb7755881e779ad143a6a95
phonetics-phonology.md              dd132967cd9502b54a44ca1e635bfeac093e2dc5a0544a8ee4b5b3220a91ec96 -> b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b
politeness-taboo-euphemism.md       7fe13a118539dc467d48c99473439b04e268eca9b0e3552139ab8db5b7f22b80 -> a73c0b1fb8fd0052a46252e6262101220ca145e3c9a7f8b44c2151e45fc047e4
semantic-fields-lexicon-building.md 674d7be5f0743609264e5a52606b6afc3f7202e76652f7f53fcf9bcd6e736717 -> 80b5e2c89fc8a97be343d32be4071ec40cc2a0e2aedac4a8abf2311b7175f65d
semantics-pragmatics.md             b36694fb3d066ff4ed9bf816db7151f323becf36eb0c514992e7d2028af5a910 -> 9b9a3ff757fe3290a1435a75d08b96705645f68cdc9c200d27ed26cb8af6ae9b
sociolinguistics-registers.md       9a98f945ed4d03129d39651ee14412943fdf9bf34a39baffdc5c790fd74007fb -> 95ea235f9e10e2efc6f1f917008fa3ac3cfc2e8cd5e21258a4615cd5e90abebd
syntax-typology.md                  7b1c488743f68a2e0bda81fc04b29b6ce510b1354d3c61e6a236081d5217b85d -> 258accfd4e435628190c537e68ca84ab57f40e9b53aed0675bf98d92d7bbd090
writing-systems.md                  03b6a7adc9fa66a8dc1acc2e6a82422a2d821259be9ada86c64f30388e86cef8 -> 76263260dd8181bae0d969c2d4cd647892535a692eb0e41033d83ea8f005a98b
```

## 3. Negative-claim sweep (Group B "no dated source recheck on record")

Command (2026-10-17T20:16Z):

```
grep -rln -e 'conlang-methodology' -e 'historical-linguistics' -e 'language-contact' \
  -e 'linguistic-anthropology' -e 'morphological-typology' -e 'naming-systems' \
  -e 'politeness-taboo-euphemism' -e 'semantics-pragmatics' -e 'syntax-typology' \
  -e 'writing-systems' corpus/lessons/round-5-sources corpus/lessons/round-6-sources \
  corpus/lessons/round-7-sources corpus/lessons/supplement-opencode-1/sources
```

Result: one file, `corpus/lessons/round-6-sources/04.json` — and its hit is line 24, a `coupling_implication` note naming `writing-systems, historical-linguistics, naming-systems` as adjacent coupled entries of the Aegean record (`entry` field: `corpus/knowledge/civilizations/aegean-minoan-mycenaean.md`), i.e. **not** an entry-named recheck record for any Group B file. Ledger `entry` fields across round-5/6 confirm: round-5 records 10/11/12/13 are color/kinship/orality+phonetics/registers; round-6 records 02–13 are civilizations only. No round-5/6/7/supplement ledger audits a Group B linguistics entry.

## 4. Marker-count delta (reported, not hidden)

`to-verify` occurrence count per file (command: per-file `str.count('to-verify')` on `HEAD:<path>` vs working tree, 2026-10-17T20:19Z): **17 → 29 (+12)** — one new occurrence in each of 12 files, all inside the new `verified-at` lines where unresolved status is declared. The additions are honest declarations of unverified scope, not new claims; no marker was deleted to buy an improvement. Provenance gate re-run post-fix: `python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics` → `files=16 marks=29 mark-lines=29 findings=0 blocked=0`, exit 0 (was 16 marks pre-fix).

## 5. Residuals (carried, not repaired — outside a frontmatter sweep)

- **Group B freshness debt:** 10/16 entries have no passage-level source recheck on record; the new fields state this plainly and mark their figures `(to-verify)`. A future source-recheck wave (not this metadata shard) is the honest repair route.
- **round-4 findings:** politeness FLAG-01 (unbased occupational-taboo marker at `:73`) and semantics-pragmatics CAL-01 (calibration prose at `:133` without a headed section) remain open; both are named in the new `verified-at` lines.
- **Class split is 6 A / 10 B** — no Group B entry was promoted to "verified" by this sweep; the audit changed metadata declarations only.
- Unresolved items named inside Group A entries (traffic-light statute, NDL record, CIE item, Kroeber/Lowie, Saisiyat count, Meho 12,323 provenance, Blasi-adjacent diet/bite debate) remain `(to-verify)` exactly as their errata state.

## 6. Verification of this sweep

- After-audit (same script as §1, 2026-10-17T20:19Z): `topic=16 sources=16 couples=16 verified-at=16 recheck=16`.
- `git diff --numstat -- corpus/knowledge/linguistics/` → `2  0` × 16; `git diff --check` → clean; `git status --short` → only these 16 files modified.
- No commit made; no file outside the assignment written. All material remains NON-CANON; canon decisions are lore-shokunin's.
