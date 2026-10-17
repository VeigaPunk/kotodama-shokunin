# Drift shard 07 — SKILL.md lines 121-140 (R10-F07)

- date: 2026-10-17
- shard: R10-F07 (freshness drift re-runner, shard 07 of 13)
- source surface: `SKILL.md` lines 121-140 (sha256 of range: `39329792bcc91f0df5714a2e1facc27b10fef3039da292cca351a43002db20fd`; whole file: `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`)
- baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (declared in `reports/round-10/claims.json`)
- live HEAD: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`; baseline is an ancestor, and `git diff --stat 9dc18ec..HEAD -- SKILL.md` is empty — the shard bytes are unchanged since baseline, so all verdicts below are against baseline content.
- isolation: `export TMPDIR=$PWD/.scratch`; selftests ran in the disposable copy `.scratch/iso-shard07/` (`cp -r tools examples corpus`); live tree untouched — `git status --porcelain tools/ corpus/` returns 0 lines.
- TMPDIR note: all scratch artifacts are under `.scratch/shard07-runs/` in-lane; nothing written outside this repo.

## What lines 121-140 contain

Tail of checklist item 2 (myth/symbol calibration pointer, line 121), checklist items 3-4 (costume/era coupling, world-bible handoff), and the Corpus map for `linguistics/` (129-130), `myth-symbol/` (131-133), `culture-material/` (134-136), `synthesis/` (137-139), `verification/` (140, description continues to 142).

## Inventory: runnable commands in range

| # | command | output | exit |
|---|---|---|---|
| 1 | `awk 'NR>=121 && NR<=140' SKILL.md \| grep -cE 'python3\|--selftest\|run-validation'` | `0` | 1 (grep no-match) |

Verdict: **current** — lines 121-140 cite zero runnable commands. The only backticked spans in range are the five partition paths (`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification}/`), so the drift work for this shard is path/topic resolution plus the executable counterparts of the checklist items it carries. No URLs appear in range (`awk 'NR>=121 && NR<=140' SKILL.md | grep -cE 'https?://'` → `0`, exit 1), so no web access attempt was required in this shard.

## Cited paths — all resolve

| locator | cited path | observed | verdict |
|---|---|---|---|
| SKILL.md:121 | `corpus/knowledge/synthesis/source-discipline-calibration.md` | exists, 197 lines, sha256 `3cbc98b4266aea08d2e8b19513ee369b3f0c6727f16f3c40eafe44796f0e4e93` | current (see DR-07-01 for its wording coupling) |
| SKILL.md:129 | `corpus/knowledge/linguistics/` | exists, 16 `.md` entries | current |
| SKILL.md:131 | `corpus/knowledge/myth-symbol/` | exists, 16 `.md` entries | current |
| SKILL.md:134 | `corpus/knowledge/culture-material/` | exists, 16 `.md` entries | current |
| SKILL.md:137 | `corpus/knowledge/synthesis/` | exists, 24 `.md` entries | current |
| SKILL.md:140 | `corpus/knowledge/verification/` | exists, 13 `.md` entries | current |

Counting command: `for p in linguistics myth-symbol culture-material synthesis verification; do printf "%s %s\n" "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done` → output sha256 `aac7ddaae7dce77eba9e77042ecfb7361774986ad3b1628fa0ca64d4aa9fa3fa`, exit 0.

## Topic coverage map — every topic word resolves

Listing command: `{ ls corpus/knowledge/linguistics; ls corpus/knowledge/myth-symbol; ls corpus/knowledge/culture-material; ls corpus/knowledge/verification; }` → output sha256 `898ac8009b7c396d7c7943cb9436ba52a92f96348892bfd155d44ce25d57907c`, exit 0.

| partition (locator) | map topics | resolving entries |
|---|---|---|
| linguistics (129-130) | phonology through pragmatics, historical linguistics, writing, naming, contact, registers | `phonetics-phonology.md`, `semantics-pragmatics.md`, `historical-linguistics.md`, `writing-systems.md`, `naming-systems.md`, `language-contact.md`, `sociolinguistics-registers.md` |
| myth-symbol (131-133) | comparative frameworks, creation/hero/trickster taxonomies, cosmology, color/animal/number/celestial symbolism, ritual, folktale indexing | `comparative-frameworks.md`, `creation-myths-taxonomy.md`, `hero-journey-variants.md`, `trickster.md`, `cosmology-cosmography.md`, `color-symbolism.md`, `animal-symbolism.md`, `number-symbolism.md`, `celestial-symbolism-calendars.md`, `ritual-liminality.md`, `motif-index-usage.md` (+ `myth-folktale-genres.md`) |
| culture-material (134-136) | dress through eras, costume semiotics, textiles, food, architecture, trade, calendars, craft, music, adornment | `dress-through-eras.md`, `costume-semiotics.md`, `textile-technology.md`, `cuisine-food-lexicon.md`, `architecture-settlement-lexicon.md`, `trade-economy-lexicon.md`, `calendar-festival-systems.md`, `craft-artisan-lexicon.md`, `music-instrument-lexicon.md`, `adornment-body-codes.md` |
| synthesis (137-139) | decision tables, matrices, pipelines, lore handoff contract, worked example, source discipline | decision tables: `consistency-verification-checklist.md` (T02/T04/T07/T08/T12), `worldbible-integration-contract.md` §3; `era-myth-language-costume-matrix.md`; `deity-name-derivation-pipeline.md`; `worldbible-integration-contract.md`; `worked-example-mini-culture.md`; `source-discipline-calibration.md` |
| verification (140-142) | gate specifications, citation/provenance formats, calibration registry, to-verify triage, real-world-inspiration boundaries | `*-gate.md` specs + `verification-method-overview.md`; `citation-format-and-source-registry.md`, `provenance-audit-ledger-format.md`; `calibration-registry.md`; `to-verify-triage-protocol.md`; `real-world-inspiration-boundaries.md` |

All five partitions: **current**. No map topic is orphaned; no listed partition is missing or empty.

## Checklist executables in range (items 3-4, and item 2's pointer)

| item (locator) | executable surface | run | exit | output sha256 | verdict |
|---|---|---|---|---|---|
| item 3 — costume/era claim couples to term + material + wearer rule (122-123) | `costume-era-consistency-gate` — `MAT-01..07` material identification, `R-01..R-07` rank rules, `EAR-*` era coupling (`tools/gates/costume-era-consistency-gate.py`) | `python3 tools/gates/costume-era-consistency-gate.py --selftest` in isolated copy | 0 | `854709454f11d36ccee38957efeda061637df9850f8a9adde9a522babac2cb33` | current — "self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs" |
| item 4 — handoff names recipient (lore) + open questions (124-125) | `handoff-packet-check` — requires `recipient` + `open_questions` fields; §6 canon standing stays lore's (`tools/gates/handoff-packet-check.py`) | `python3 tools/gates/handoff-packet-check.py --selftest` in isolated copy | 0 | `dea5e942ff6dde9e514eb7c01aa9c0ba9155479ccea36db392c8a42b41d6fcd8` | current — "selftest: OK — fixture findings 11 across 9 ids; clean control exit 0; malformed inputs exit 2" |
| item 2 tail — calibration status pointer (119-121) | `source-discipline-calibration.md` §3 contested-framework registry | `grep -c -i mainstream corpus/knowledge/synthesis/source-discipline-calibration.md` → `0` | 1 (grep no-match) | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | **stale-documented** — see DR-07-01 |

Live-tree isolation check after the runs: `git status --porcelain tools/ corpus/` → empty (0 lines), exit 0.

## Findings

### DR-07-01 — calibration vocabulary mismatch (stale-documented, in shard)

- Locator: `SKILL.md:119-121` — "Every mythic/symbolic claim names its framework and its calibration status (mainstream / contested / discredited — see `synthesis/source-discipline-calibration.md`)."
- Observed: the cited file's operational statuses are **S / C / H / R / U / V** (`source-discipline-calibration.md:67`), and the word "mainstream" occurs **0** times in it (`grep -c -i mainstream` → 0). The file explicitly warns at line 94 that "'Contested,' 'hard to test,' 'not established,' and 'discredited' are not synonyms" and tells readers not to inherit blanket verdicts from `comparative-frameworks.md` — the exact conflation the parenthetical's three-word vocabulary invites.
- Verdict: **stale-documented** (not fixed here; this shard writes only its own report). Proposed fix for F15-F18: replace the parenthetical with the file's own vocabulary, e.g. "(calibration status per that file's S/C/H/R/U/V registry — see `synthesis/source-discipline-calibration.md`)". The pointer itself resolves; only the gloss is stale.
- Evidence: commands above; file sha256 `3cbc98b4266aea08d2e8b19513ee369b3f0c6727f16f3c40eafe44796f0e4e93`.

### DR-07-02 — boundary note for shard 08 (out of range, not owned here)

- Locator: `SKILL.md:143` — "92 earlier-civilization bases" (line 143 falls in shard 08's range 141-160, not in 121-140; recorded here only so the ledger does not lose it).
- Observed: `ls corpus/knowledge/civilizations/*.md | wc -l` → **94** (output sha256 `6fc16b03d8c15b9885876848a301a01816cccaf7b48e74f2b51db99c007a3bd5`, exit 0); `corpus/README.md:116` already says `## civilizations/ (94)`.
- Verdict: **stale-documented** — the "92" count is stale against both the directory and the README. Owner: shard 08 / the F15-F18 fixer covering that range.

## Ledger rows (for the F14 scribe)

```json
[
  {"id": "R10-F07-01", "command": "awk 'NR>=121 && NR<=140' SKILL.md | grep -cE 'python3|--selftest|run-validation'", "source_locator": "SKILL.md:121-140", "round10_verdict": "current", "output_sha256": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa", "exit": 1, "note": "0 runnable commands in shard range; grep exit 1 is no-match semantics; nothing stale to re-run"},
  {"id": "R10-F07-02", "command": "for p in linguistics myth-symbol culture-material synthesis verification; do printf \"%s %s\\n\" \"$p\" \"$(ls corpus/knowledge/$p/*.md | wc -l)\"; done", "source_locator": "SKILL.md:129-142", "round10_verdict": "current", "output_sha256": "aac7ddaae7dce77eba9e77042ecfb7361774986ad3b1628fa0ca64d4aa9fa3fa", "exit": 0, "note": "counts 16/16/16/24/13; all five cited partition paths resolve"},
  {"id": "R10-F07-03", "command": "{ ls corpus/knowledge/linguistics; ls corpus/knowledge/myth-symbol; ls corpus/knowledge/culture-material; ls corpus/knowledge/verification; }", "source_locator": "SKILL.md:129-142", "round10_verdict": "current", "output_sha256": "898ac8009b7c396d7c7943cb9436ba52a92f96348892bfd155d44ce25d57907c", "exit": 0, "note": "every topic word in the corpus map resolves to a listed entry"},
  {"id": "R10-F07-04", "command": "test -f corpus/knowledge/synthesis/source-discipline-calibration.md && wc -l corpus/knowledge/synthesis/source-discipline-calibration.md", "source_locator": "SKILL.md:121", "round10_verdict": "current", "output_sha256": "3cbc98b4266aea08d2e8b19513ee369b3f0c6727f16f3c40eafe44796f0e4e93", "exit": 0, "note": "output_sha256 is the target file's own sha256 (197 lines), a stronger pin than the wc output"},
  {"id": "R10-F07-05", "command": "grep -c -i mainstream corpus/knowledge/synthesis/source-discipline-calibration.md", "source_locator": "SKILL.md:119-121", "round10_verdict": "stale-documented", "output_sha256": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa", "exit": 1, "note": "0 matches; file uses S/C/H/R/U/V statuses (line 67) and warns the words are not synonyms (line 94); fix proposed in DR-07-01, owner F15-F18"},
  {"id": "R10-F07-06", "command": "cp -r tools examples corpus .scratch/iso-shard07/ && cd .scratch/iso-shard07 && python3 tools/gates/costume-era-consistency-gate.py --selftest", "source_locator": "SKILL.md:122-123", "round10_verdict": "current", "output_sha256": "854709454f11d36ccee38957efeda061637df9850f8a9adde9a522babac2cb33", "exit": 0, "note": "isolated copy; 10/10 checks passed, 21 planted finding IDs; live tree untouched"},
  {"id": "R10-F07-07", "command": "cp -r tools examples corpus .scratch/iso-shard07/ && cd .scratch/iso-shard07 && python3 tools/gates/handoff-packet-check.py --selftest", "source_locator": "SKILL.md:124-125", "round10_verdict": "current", "output_sha256": "dea5e942ff6dde9e514eb7c01aa9c0ba9155479ccea36db392c8a42b41d6fcd8", "exit": 0, "note": "isolated copy; fixture findings 11 across 9 ids, clean control exit 0, malformed exit 2; live tree untouched"},
  {"id": "R10-F07-08", "command": "ls corpus/knowledge/civilizations/*.md | wc -l", "source_locator": "SKILL.md:143 (shard 08 range; boundary note only)", "round10_verdict": "stale-documented", "output_sha256": "6fc16b03d8c15b9885876848a301a01816cccaf7b48e74f2b51db99c007a3bd5", "exit": 0, "note": "94 vs SKILL.md's '92'; corpus/README.md:116 already says (94); owner shard 08 / F15-F18"},
  {"id": "R10-F07-09", "command": "git status --porcelain tools/ corpus/", "source_locator": "isolation check", "round10_verdict": "current", "output_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "exit": 0, "note": "empty output (sha256 of empty string); this shard's selftests wrote nothing to the live tree"}
]
```

## Re-run recipe (for the F19 auditor)

1. `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch`
2. `sha256sum SKILL.md` → expect `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`.
3. `awk 'NR>=121 && NR<=140' SKILL.md | sha256sum` → expect `39329792bcc91f0df5714a2e1facc27b10fef3039da292cca351a43002db20fd`.
4. `awk 'NR>=121 && NR<=140' SKILL.md | grep -cE 'python3|--selftest|run-validation'` → `0` (exit 1).
5. `grep -c -i mainstream corpus/knowledge/synthesis/source-discipline-calibration.md` → `0` (exit 1).
6. Isolated selftests: `mkdir -p .scratch/iso-shard07 && cp -r tools examples corpus .scratch/iso-shard07/ && (cd .scratch/iso-shard07 && python3 tools/gates/costume-era-consistency-gate.py --selftest; echo "exit=$?"; python3 tools/gates/handoff-packet-check.py --selftest; echo "exit=$?")` → both exit 0. Do not run the costume selftest in the live tree.
7. `ls corpus/knowledge/civilizations/*.md | wc -l` → `94`.

Limits: this shard covers only lines 121-140; the gates table (181-194), SCORECARD rows and `reports/round-9/baselines/registry.md` are other shards' surfaces and were not re-run here beyond the two selftests above. Selftest success demonstrates the executable surface is live; it does not re-certify every packet the gates may read. All verdicts are against baseline `9dc18ec1` content, which equals HEAD for SKILL.md.
