# Round-9 metadata re-audit — fragment V08: `corpus/knowledge/linguistics/` (all 16 entries)

- worker: V08 (metadata_verify shard "linguistics all"); fragment location `reports/round-9/metadata/v08-linguistics.md` (this file).
- date: 2026-10-17 (audit commands run 20:40Z–20:57Z UTC; `date -u` receipts inline).
- baseline: round-9 claims baseline `e1694bad6ac96aca45a11ca5746582b275929355` (`reports/round-9/claims.json`); working-tree HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` at audit time. No commit, push, or LOG.md write by this worker; no network retrieval performed — every receipt below is an in-repo record.
- protocol source: `reports/round-9/targets.json` field `metadata_verify` ("11 shards re-audit all 179 corpus/knowledge entries for complete source/verified-at/recheck frontmatter after round 8's sweep; fix stragglers in place; fragments under reports/round-9/metadata/ + 1 auditor shard") plus the fleet contract `CORPUS.md:17` ("Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`", quoted in `reports/supplement-opencode-1/28-corpus-contract.md` §1). The operative lane field is the plural `- sources:` block; the `source:`/`sources:` fleet-text question was filed by round-8 M11 (`28-corpus-contract.md` §6.2) and is not re-decided here. `tools/gates/provenance-audit.py` reads only `topic|sources|couples`, so the metadata trio is gate-neutral.
- assigned files: all 16 `corpus/knowledge/linguistics/*.md` — color-terminology, conlang-methodology, historical-linguistics, kinship-terminology, language-contact, linguistic-anthropology, morphological-typology, naming-systems, orality-formulaic-language, phonetics-phonology, politeness-taboo-euphemism, semantic-fields-lexicon-building, semantics-pragmatics, sociolinguistics-registers, syntax-typology, writing-systems.
- corpus context (the 179 in `targets.json`): `find corpus/knowledge -name '*.md' | wc -l` → **179**; per-subdir `ls <dir>/*.md | wc -l` → civilizations 94, culture-material 16, linguistics 16, myth-symbol 16, synthesis 24, verification 13; 94+16+16+16+24+13 = 179 (2026-10-17).

## Axis result

**In-partition stragglers found: 0. In-place fixes applied by this shard: 0 files (zero corpus edits).** All 16 linguistics entries carry the full header block `topic` / `sources` / `verified-at` / `recheck` / `couples`, correct order, dated 2026-10-17, byte-identical to their round-8 after-state digests (§3). Four body-placement stragglers exist elsewhere in the corpus (§8) — reported, not edited (write-scope discipline).

## 1. Method

Five checks per entry, all line-anchored and dated: (1) header-block field presence + order + duplicates + payload; (2) digest drift against round-8's committed after-state pins; (3) receipt-content verification of the `verified-at:` figures (Group A record files, claim counts, round-5 follow-up IDs); (4) Group B negative-claim sweep re-run; (5) `couples:` cross-reference resolution. Plus the commit-chain check (§4) and the provenance gate re-run (§9).

## 2. Field completeness (pre-state = post-state)

Command (2026-10-17T20:44Z), header block = lines up to the first `## `; anchored regex `^-\s+<field>\s*:`:

```
python3 - <<'EOF'
import re, glob, os
fields = ['topic','sources','verified-at','recheck','couples']
pats = {f: re.compile(r'^-\s+'+re.escape(f)+r'\s*:', re.M) for f in fields}
for f in sorted(glob.glob('corpus/knowledge/linguistics/*.md')):
    text = open(f, encoding='utf-8').read()
    hdr = []
    for ln in text.split('\n'):
        if ln.startswith('## '): break
        hdr.append(ln)
    hdr = '\n'.join(hdr)
    counts = {fd: len(pats[fd].findall(hdr)) for fd in fields}
    missing = [fd for fd in fields if counts[fd]==0]
    print(f"{os.path.basename(f):45s} " + ' '.join(f"{fd}={counts[fd]}" for fd in fields)
          + ("  MISSING:"+','.join(missing) if missing else "  OK"))
EOF
```

Result: **16/16 `OK`** — each file `topic=1 sources=1 verified-at=1 recheck=1 couples=1` (verbatim per-file lines omitted for space; all 16 identical in shape). Supplementary checks, same script family (2026-10-17T20:45Z):

- field **order** per header block = `topic → sources → verified-at → recheck → couples` in **16/16** (`order=OK`);
- `verified-at` payload contains `2026-10-17` in **16/16**; `recheck` payload non-empty in **16/16**; `sources` payload non-empty in **16/16** (kinship-terminology and naming-systems use the multi-line `- sources:` block with indented bullets — allowed shape, same as round 8);
- whole-file anchored occurrence count is exactly 1 per field in 16/16 (no duplicates, no second copy in the body);
- variant scan (`- Verified-at:` capital, `- verified_at:`, `verified-at: to-verify` placeholder, `**verified-at:**` bolded) over all 16 headers: **0 hits** — no case/format variants in this partition.

This is the round-9 re-audit result, not the round-8 state: at the round-8 baseline `cf338a7` these files carried 0/16 `verified-at`/`recheck` (receipt §4); round 8 added them, and round 9 verifies them as still complete and unchanged.

## 3. No drift vs round-8 pins

Command (2026-10-17T20:45Z): `for f in corpus/knowledge/linguistics/*.md; do sha256sum "$f"; done`. Current digest vs the after-state digest recorded in `reports/round-8/metadata/m08-linguistics.md` §2 — **16/16 match**:

| entry | round-8 after (short16) | current (short16) | match |
|---|---|---|---|
| color-terminology.md | 7ee9f7e45d8a63ac | 7ee9f7e45d8a63ac | yes |
| conlang-methodology.md | 272329f70c1fe93e | 272329f70c1fe93e | yes |
| historical-linguistics.md | 019f28f09ceac28a | 019f28f09ceac28a | yes |
| kinship-terminology.md | c51d3483a27b0943 | c51d3483a27b0943 | yes |
| language-contact.md | 52385e3d81f7d8f8 | 52385e3d81f7d8f8 | yes |
| linguistic-anthropology.md | ffa38d0f2e89a774 | ffa38d0f2e89a774 | yes |
| morphological-typology.md | b423e811651aca42 | b423e811651aca42 | yes |
| naming-systems.md | d972a1d65e7a8fba | d972a1d65e7a8fba | yes |
| orality-formulaic-language.md | f827bbee6f305466 | f827bbee6f305466 | yes |
| phonetics-phonology.md | b4f9b00384bc6840 | b4f9b00384bc6840 | yes |
| politeness-taboo-euphemism.md | a73c0b1fb8fd0052 | a73c0b1fb8fd0052 | yes |
| semantic-fields-lexicon-building.md | 80b5e2c89fc8a97b | 80b5e2c89fc8a97b | yes |
| semantics-pragmatics.md | 9b9a3ff757fe3290 | 9b9a3ff757fe3290 | yes |
| sociolinguistics-registers.md | 95ea235f9e10e2ef | 95ea235f9e10e2ef | yes |
| syntax-typology.md | 258accfd4e435628 | 258accfd4e435628 | yes |
| writing-systems.md | 76263260dd8181ba | 76263260dd8181ba | yes |

Full current hashes (sha256, 2026-10-17T20:45Z):

```
color-terminology.md                7ee9f7e45d8a63ac4362a95d71db923dde118d4a1f0a598fa0a0888e68105992
conlang-methodology.md              272329f70c1fe93e47f47d8c2618371902d1e5ccc78b6987abf437e101ac77ea
historical-linguistics.md           019f28f09ceac28a1bcb6685f756170b66944129a6b3dca17ca76d9663ab3caf
kinship-terminology.md              c51d3483a27b0943b257fa25287d0dec4dba3fe16f737b1893ce237ba92c07f8
language-contact.md                 52385e3d81f7d8f8eb1423d408a47bd12c968f1444fd9fc5d77a9c3e691cd409
linguistic-anthropology.md          ffa38d0f2e89a774f373c9759978e8bd173e6e28b1f5cc1b1c87847fd5e54458
morphological-typology.md           b423e811651aca4229e6621dd2a884df360a53809230778aa85bef6376dfeddb
naming-systems.md                   d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d
orality-formulaic-language.md       f827bbee6f305466a17a8b6e911539c38820e6865eb7755881e779ad143a6a95
phonetics-phonology.md              b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b
politeness-taboo-euphemism.md       a73c0b1fb8fd0052a46252e6262101220ca145e3c9a7f8b44c2151e45fc047e4
semantic-fields-lexicon-building.md 80b5e2c89fc8a97be343d32be4071ec40cc2a0e2aedac4a8abf2311b7175f65d
semantics-pragmatics.md             9b9a3ff757fe3290a1435a75d08b96705645f68cdc9c200d27ed26cb8af6ae9b
sociolinguistics-registers.md       95ea235f9e10e2efc6f1f917008fa3ac3cfc2e8cd5e21258a4615cd5e90abebd
syntax-typology.md                  258accfd4e435628190c537e68ca84ab57f40e9b53aed0675bf98d92d7bbd090
writing-systems.md                  76263260dd8181bae0d969c2d4cd647892535a692eb0e41033d83ea8f005a98b
```

## 4. Commit-chain verification

Receipts (2026-10-17T20:46Z):

```
git diff --numstat cf338a7 e1694ba -- corpus/knowledge/linguistics/   → 2  0  ×16 files (the round-8 insert)
git diff --numstat e1694ba a7bb205 -- corpus/knowledge/linguistics/   → empty (nothing touched in round-9 declare)
git status --short -- corpus/                                          → empty (clean at audit time)
```

The round-8 base state check: `git show cf338a7:corpus/knowledge/linguistics/<f>.md | grep -c -E '^- (verified-at|recheck):'` → **0** for sampled files (color, kinship, conlang, writing-systems); `git show e1694ba:…` → **2** for the same files. So round 8's declared 0/16 → 16/16 transition is real in history, is committed, and has carried no edits into round 9.

## 5. Group A receipt-content verification (6 entries)

The six `verified-at:` lines cite wave `supplement-opencode-1` records with claim-count dispositions. Parsed the record JSONs (`json.load` → `audits` array, count by `verdict`), 2026-10-17T20:48Z:

| entry | record | cited in entry | audits parsed | verdicts parsed (supported/contradicted/unresolved) | match |
|---|---|---|---|---|---|
| color-terminology.md | supplement-opencode-1/sources/color.json | 7 — 4/1/2 | 7 | 4/1/2 | yes |
| kinship-terminology.md | …/kinship.json | 9 — 6/1/2 | 9 | 6/1/2 | yes |
| orality-formulaic-language.md | …/orality.json | 5 — 3/1/1 | 5 | 3/1/1 | yes |
| phonetics-phonology.md | …/phonetics.json | 11 — 7/3/1 | 11 | 7/3/1 | yes |
| semantic-fields-lexicon-building.md | …/lexicon.json | 5 — 3/2 | 5 | 3/2 (0 unresolved) | yes |
| sociolinguistics-registers.md | …/registers.json | 8 — 5/1/2 | 8 | 5/1/2 | yes |

Each JSON's `entry` field equals the cited `corpus/knowledge/linguistics/<file>` path (6/6). Round-5 follow-up IDs cited in the same lines all found (`json.dumps` substring check, 2026-10-17T20:48Z): `round-5-sources/10.json` COL-06, COL-07; `11.json` KIN-A07, KIN-A08; `12.json` ORALITY-05, PHON-A11; `13.json` SR-REG-04, SR-REG-07 — all FOUND. The Group A figures in the frontmatter are therefore receipt-backed, not decorative.

## 6. Group B negative-claim sweep (10 entries) — re-run

Claim under audit: the ten Group B `verified-at:` lines assert "no entry-named record in corpus/lessons/{round-5-sources,round-6-sources,round-7-sources,supplement-opencode-1/sources}". Re-run (2026-10-17T20:49Z):

```
grep -rln -e 'conlang-methodology' -e 'historical-linguistics' -e 'language-contact' \
  -e 'linguistic-anthropology' -e 'morphological-typology' -e 'naming-systems' \
  -e 'politeness-taboo-euphemism' -e 'semantics-pragmatics' -e 'syntax-typology' \
  -e 'writing-systems' corpus/lessons/round-5-sources corpus/lessons/round-6-sources \
  corpus/lessons/round-7-sources corpus/lessons/supplement-opencode-1/sources
```

Result: **one file — `corpus/lessons/round-6-sources/04.json`**, hit at line 24, a `coupling_implication` note naming `writing-systems, historical-linguistics, naming-systems` as adjacent coupled entries of the Aegean record (`entry` field: `corpus/knowledge/civilizations/aegean-minoan-mycenaean.md`). That is **not** an entry-named recheck record for any Group B file — identical to round-8's sweep result. Directory inventory at audit time: `ls -d corpus/lessons/*sources*` → `round-5-sources`, `round-6-sources`, `round-7-sources` only (no round-8/9 sources dir); `supplement-opencode-1/sources/` holds 15 JSONs. The ten Group B `verified-at:` lines' negative claim stands.

## 7. `couples:` cross-reference resolution

Resolver (2026-10-17T20:53Z): extract `[\w./{},-]+\.md` tokens from each `- couples:` value (continuation lines joined; brace-expanded), resolve exact path relative to the entry dir, then to `corpus/knowledge/`, then by basename anywhere under `corpus/knowledge/**`; plus repo-root files (the lane `SKILL.md` exists at the repo root).

- **28 concrete `.md` tokens in 4 files; 21 resolve to existing files; 7 unresolved** — and all 7 unresolved are filenames the entries themselves declare as future/planned, not citations of existing files:
  - `conlang-methodology.md` — 19 tokens, **19/19 resolve**: 12 sibling linguistics files (`linguistics/*.md`), 2 myth-symbol (`ritual-liminality.md`, `color-symbolism.md`), 2 culture-material (`dress-through-eras.md`, `costume-semiotics.md`), 2 synthesis (`source-discipline-calibration.md`, `consistency-verification-checklist.md`), and `SKILL.md` (repo root, found). The field's own wording is "planned per SKILL.md".
  - `language-contact.md` — 5 tokens: `writing-systems.md` resolves; `phonology-basics.md`, `naming-and-onomastics.md`, `honorifics-and-register.md`, `numerals-and-measures.md` do not exist — the field itself says "sibling knowledge files **to seed**" (declared future files).
  - `phonetics-phonology.md` — 4 tokens: `writing-systems.md` resolves; `sound-change.md`, `tone-prosody.md`, `sound-symbolism.md` do not exist — the field itself says "**prospective** sibling files" (declared future files).
- The other 12 files' `couples:` values are prose (directories, entry-siblings, themes) with no `.md` path tokens — non-concrete by design, same reading as round-8 M11 (`m11-verification.md` §2).
- Result recorded as: **0 broken references to existing-file citations**; 7 declared-planned names as listed.

## 8. Cross-partition findings (report-only — outside this shard's write scope)

Whole-corpus sweep (2026-10-17T20:47Z), two readings:

1. **Opening-block reading** (anchored `^- verified-at:` / `^- recheck:` before the first `## `): present in **175/179** entries; **4 entries** carry the fields only in the body — **not edited by this shard**:
   - `corpus/knowledge/civilizations/mali-songhai.md` — first `## ` at :7; at audit time (20:50Z) all three fields sat merged on one line, `:14`: `- source: [S1–S16] below; verified-at: 2026-10-17; recheck: before assigning an exact ritual restriction, …`. Shard V04's fragment (`v04-civ-58-76.md`, written by 20:57Z) records the split fix; the working tree then showed `:14 source / :15 verified-at / :16 recheck` — still **after** the first `## ` at :7, i.e. body placement remains.
   - `corpus/knowledge/verification/citation-format-and-source-registry.md` — first `## ` at :13; `- verified-at:` :16, `- recheck:` :17 (inside §1 "Contract and named frameworks"). Working tree clean (unclaimed at audit time).
   - `corpus/knowledge/verification/myth-consistency-gate.md` — first `## ` at :6; `- verified-at:` :10, `- recheck:` :11 (inside §1). Working tree clean.
   - `corpus/knowledge/verification/provenance-audit-ledger-format.md` — first `## ` at :6; `- verified-at:` :10, `- recheck:` :11 (inside §1). Working tree clean.
2. **Whole-file reading** (case-insensitive substring anywhere): `verified-at` **179/179**, `recheck` **179/179**, `sources` **179/179** — so nothing is absent; the four are placement variants, not omissions.

Routing note for the orchestrator/auditor (V12's `audit.md` already uses the opening-block reading, which will surface the same four): the three verification files belong to the verification shard's partition and are untouched here per write-scope discipline; `mali-songhai.md` is V04's assigned file. No network checks performed.

## 9. Provenance gate re-run

`python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics` (2026-10-17T20:46Z):

```
INFO scan: files=16 marks=29 mark-lines=29 findings=0 blocked=0   (exit 0)
```

The 29 `to-verify` marks equal round-8's post-fix count exactly (`m08-linguistics.md` §4: 17 → 29; `files=16 marks=29 … findings=0`). No marker added or removed by this audit; no delta.

## 10. Residuals carried (unchanged by this audit)

- **Group B freshness debt** — 10/16 entries still have no passage-level source recheck on record (negative sweep §6); their `verified-at:` lines state this plainly and keep the figures `(to-verify)`. A source-recheck wave is the honest repair route, not a metadata sweep.
- **round-4 findings still open** — FLAG-01 (`politeness-taboo-euphemism.md`): occupational-taboo marker now at **:75** (was :73 at the c610e0a round-4 snapshot; +2 shift from the round-8 field insert). CAL-01 (`semantics-pragmatics.md`): "Calibration, plainly" paragraph now at **:135** (was :133; same +2 shift). The round-8 `verified-at:` lines cite the c610e0a snapshot numbers — readers comparing line numbers should apply the +2 shift. Neither is repairable inside a frontmatter sweep; both remain open.
- **Group A unresolved items** (traffic-light statute, NDL record, CIE item, Kroeber/Lowie, Saisiyat count, Meho 12,323, Blasi-adjacent diet/bite debate) remain `(to-verify)` exactly as their entries' errata state; this audit did not touch claim dispositions.
- Class split stays **6 A / 10 B** (§5 / §6); no Group B entry was promoted by this sweep — the audit changed **nothing** in the corpus, by design.

## 11. Verification of this audit

- **Zero corpus files modified by this shard.** `git status --short -- corpus/` → empty when run at 20:46Z (audit window); the only file this shard wrote is this fragment. Later working-tree modifications by sibling shards (e.g. `mali-songhai.md` by V04, the civilizations files) belong to those shards, not V08.
- Every count above carries its command and 2026-10-17 UTC timestamp; every negative claim (§6 sweep, §7 unresolved list, §8 zero-modification) carries its sweep; every citation names file:line or file path.
- All material remains NON-CANON; canon decisions are lore-shokunin's per lane rules.
