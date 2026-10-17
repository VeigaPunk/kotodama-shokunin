# R10-F01 — drift shard 01: `SKILL.md` lines 1-20

- **Round:** 10 (loop 1 of 3, build round 3 of 4) · **Date:** 2026-10-17 · **Shard:** FRESHNESS R10-F01
- **Assignment:** re-run every runnable command cited in `SKILL.md` lines 1-20 (plus any cited
  commands in that range); record output sha256 + exit; web citations get a documented access
  attempt.
- **Lane revision at measurement:** `git rev-parse HEAD` → `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  (round-10 availability-attempt commits on top of round-9 `9dc18ec`).
- **Battery run window:** 2026-10-17T21:26–21:29Z (UTC). Shard compiled 21:29:44Z.
- **Scratch discipline:** `export TMPDIR=$PWD/.scratch` for every command; battery script
  `.scratch/r10f01-battery.sh` (untracked, disposable), captured stdout in `.scratch/r10f01/c*.out`,
  results TSV `.scratch/r10f01/results.tsv` (sha256 `f2ccce467c63ed2cfeb105faf502a9ecebc46dce31b437161975d3a6cdca76d2`).
  `/tmp` remains inode-exhausted ecosystem-wide (round-9 receipts); no write was attempted there.

## 0. Range pin

| Item | Value |
|---|---|
| Range | `SKILL.md` lines 1-20 (YAML frontmatter + title + domain prose + `## Decision table` heading at line 20) |
| Segment bytes | 20 lines, 1402 bytes — sha256 `926bd7557ccfcc1dee2f68e82862c4dab452f3f80decc816c57acb974dd14f7b` (row c01) |
| Full file | sha256 `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b` (row c03 content; 291 lines) |
| Working tree | `git status --porcelain SKILL.md` → empty, exit 0 (row c04) |
| History | last commit touching `SKILL.md`: `e1694bad6ac96aca45a11ca5746582b275929355` (round-8 admit, 2026-10-17); `git diff --stat e1694bad..HEAD -- SKILL.md` → empty, exit 0 (rows c05/c06) → **byte-identical since round-8, unchanged through round-9 and the round-10 declare commits** |

## 1. Runnable commands and web citations in range: **none**

The in-range sweep found no backticked commands, no URLs, no file paths, no executable tokens:

```
sed -n '1,20p' SKILL.md | grep -nE '(`|https?://|python3|bash |curl|wget|git |\.py|\.sh)'
```
→ stdout empty, **exit 1** (row c02; empty-output sha256 `e3b0c442...b7852b855` = SHA-256 of zero bytes).

Consequence per the shard contract: there is nothing runnable to re-run and no web citation to
attempt — **the documented access attempt for this shard is the empty sweep above**, not an omitted
step. The only checkable content in range is the frontmatter and prose claims, verified below.
This is a negative claim, so it carries its sweep: the grep above, run 2026-10-17T21:26Z, exit 1,
against segment sha256 `926bd755...`.

## 2. Checkable claims in range — all verify current

| # | Claim (location) | Check (row) | Result |
|---|---|---|---|
| 1 | Frontmatter is well-formed YAML; `name: kotodama-shokunin` matches the lane directory (`SKILL.md:1-4`) | `ruby -ryaml` parse (c07) | `YAML-OK keys=description,name name=kotodama-shokunin desc_len=613 rank_shonen=true`. PyYAML is absent from the env (`import yaml` → ModuleNotFoundError), so Ruby/Psych was the parser; both keys are plain scalars, no anchors/refs. |
| 2 | `Rank: shonen.` (`SKILL.md:3`) | fleet taxonomy + roster | rank ladder `mint → shonen (apprentice) → shokunin (artisan) → jin'i-ryu` at parent `README.md:40` and `PROTOCOL.md:21`; roster row `README.md:110` lists kotodama-shokunin with rank `shonen`. Match. |
| 3 | Anti-triggers name live sibling lanes: lore / kotoba / chousa (`SKILL.md:3`) | `ls -d ../{lore,kotoba,chousa}-shokunin` (c08) | all three directories exist. |
| 4 | "NOT world-bible canon recording … (lore-shokunin)" | `grep -n -m3 -i canon ../lore-shokunin/PROVINCE.md` (c10) | `lore-shokunin/PROVINCE.md:9` — "Refuses: claiming canon without an in-world citation…". Consistent. |
| 5 | "NOT prompt/skill craft (kotoba-shokunin)" | `grep -n -m3 -i prompt ../kotoba-shokunin/PROVINCE.md` (c11) | `kotoba-shokunin/PROVINCE.md:3` — "**Domain:** prompt & skill craft — scopes SKILL.md/AGENTS.md quality, trigger fidelity". Consistent. |
| 6 | "NOT general source-research method (chousa-shokunin)" | `grep -n -m3 -i 'research method' ../chousa-shokunin/PROVINCE.md` (c12) | `chousa-shokunin/PROVINCE.md:3` — "**Domain:** deep-research method (調査) — the reusable craft of source research." Consistent. |
| 7 | "feeding the world bible" (`SKILL.md:3`, `:13`) | `test -f corpus/knowledge/synthesis/worldbible-integration-contract.md` (c09) | exists, exit 0. |
| 8 | Domain prose `SKILL.md:8-19` vs lane province | `head -12 PROVINCE.md` (c14) | `PROVINCE.md` Domain = "conlang design and diachronic staging; mythic and symbolic systems; era/period models; costume & material-culture terminology; naming systems — for fictional worlds, feeding the world bible." Same scope, same refusal of canon; no drift. |
| 9 | Trigger list (`SKILL.md:3`) covers the decision table | read of `SKILL.md:22-29` | all nine triggers map to a table row: design a language / conlang → row 1; mythology of / symbolism of → row 2; naming system → row 3; era language stages → row 4; costume/dress terms → row 5; word for this concept → row 1 lexicon-by-semantic-field. No orphan trigger. |

## 3. Battery — verbatim rows (exit + sha256 of captured stdout)

| id | exit | output sha256 | command |
|---|---|---|---|
| c01 | 0 | `926bd7557ccfcc1dee2f68e82862c4dab452f3f80decc816c57acb974dd14f7b` | `sed -n '1,20p' SKILL.md` |
| c02 | 1 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | `sed -n '1,20p' SKILL.md \| grep -nE '(\`\|https?://\|python3\|bash \|curl\|wget\|git \|\.py\|\.sh)'` |
| c03 | 0 | `fb9212da5891138156fd424e42fa2a68ebc6c9b7ceb69e2f44c31684358890ef` | `sha256sum SKILL.md` (output text names the file hash `2bce468d...`) |
| c04 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | `git status --porcelain SKILL.md` |
| c05 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | `git diff --stat e1694bad..HEAD -- SKILL.md` |
| c06 | 0 | `3789dbc4059bf76c965be3adbb5c88541aaa8639fba85ca1ba412f91653bbf2f` | `git log -1 --format='%H %ad %s' --date=short -- SKILL.md` |
| c07 | 0 | `2823b617493069da169258e79ddf21cb7cefd0c01081c1fe44ec2f5bd1adeba0` | `ruby -ryaml` frontmatter parse (see §2 row 1 for output) |
| c08 | 0 | `8c8ea9a595be263ae05de64a3b085aaeaa8d334f2a78bdc1b872d90eb047d617` | `ls -d ../lore-shokunin ../kotoba-shokunin ../chousa-shokunin` |
| c09 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) | `test -f corpus/knowledge/synthesis/worldbible-integration-contract.md` |
| c10 | 0 | `8dbb9f7acbf6b70c0d1a8698fb39ca9a2bac4e87b21c359d9ffb790a603b5bde` | `grep -n -m3 -i canon ../lore-shokunin/PROVINCE.md` |
| c11 | 0 | `a69804634e6eec7259ea51434be7f460e0cacc0f218efeb7139dbab5363256a5` | `grep -n -m3 -i prompt ../kotoba-shokunin/PROVINCE.md` |
| c12 | 0 | `a5aecd59e7cce362b0a23aeaf70042d73bdb0229a09b6c8287b4088a4e2dfc20` | `grep -n -m3 -i 'research method' ../chousa-shokunin/PROVINCE.md` |
| c13 | 0 | `060d4722e672e8584d00b99fcf72e95a339d50c2ac1fe5592e268dcfc9f9b164` | `grep -n -i shonen /home/vgpnk/.kimi-code/skills/shokunin/SKILL.md` (rank taxonomy context, hits at :103, :110) |
| c14 | 0 | `58e2e7d5fe70ed5f5e151ede16deec787baeb405f4104d4bfd89ac5a96534c6e` | `head -12 PROVINCE.md` |

## 4. Ledger-ready rows (for F14 scribe)

```json
[
 {"command": "sed -n '1,20p' SKILL.md", "source_locator": "SKILL.md:1-20", "round10_verdict": "current", "output_sha256": "926bd7557ccfcc1dee2f68e82862c4dab452f3f80decc816c57acb974dd14f7b", "exit": 0, "note": "segment hash pin"},
 {"command": "sed -n '1,20p' SKILL.md | grep -nE '(backtick|https?://|python3|bash |curl|wget|git |.py|.sh)'", "source_locator": "SKILL.md:1-20", "round10_verdict": "current", "output_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "exit": 1, "note": "empty sweep: no runnable commands and no web citations exist in range; empty output is the intended result"},
 {"command": "sha256sum SKILL.md", "source_locator": "SKILL.md", "round10_verdict": "current", "output_sha256": "fb9212da5891138156fd424e42fa2a68ebc6c9b7ceb69e2f44c31684358890ef", "exit": 0, "note": "file hash 2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b"},
 {"command": "git status --porcelain SKILL.md", "source_locator": "SKILL.md", "round10_verdict": "current", "output_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "exit": 0, "note": "clean tree for SKILL.md"},
 {"command": "git diff --stat e1694bad..HEAD -- SKILL.md", "source_locator": "SKILL.md", "round10_verdict": "current", "output_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "exit": 0, "note": "no change since round-8 admit commit"},
 {"command": "git log -1 --format='%H %ad %s' --date=short -- SKILL.md", "source_locator": "SKILL.md", "round10_verdict": "current", "output_sha256": "3789dbc4059bf76c965be3adbb5c88541aaa8639fba85ca1ba412f91653bbf2f", "exit": 0},
 {"command": "ruby -ryaml frontmatter parse of SKILL.md", "source_locator": "SKILL.md:1-4", "round10_verdict": "current", "output_sha256": "2823b617493069da169258e79ddf21cb7cefd0c01081c1fe44ec2f5bd1adeba0", "exit": 0, "note": "PyYAML absent; Psych used"},
 {"command": "ls -d ../lore-shokunin ../kotoba-shokunin ../chousa-shokunin", "source_locator": "SKILL.md:3 (anti-triggers)", "round10_verdict": "current", "output_sha256": "8c8ea9a595be263ae05de64a3b085aaeaa8d334f2a78bdc1b872d90eb047d617", "exit": 0},
 {"command": "test -f corpus/knowledge/synthesis/worldbible-integration-contract.md", "source_locator": "SKILL.md:3,13 (world bible handoff)", "round10_verdict": "current", "output_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "exit": 0},
 {"command": "grep -n -m3 -i canon ../lore-shokunin/PROVINCE.md", "source_locator": "SKILL.md:3", "round10_verdict": "current", "output_sha256": "8dbb9f7acbf6b70c0d1a8698fb39ca9a2bac4e87b21c359d9ffb790a603b5bde", "exit": 0},
 {"command": "grep -n -m3 -i prompt ../kotoba-shokunin/PROVINCE.md", "source_locator": "SKILL.md:3", "round10_verdict": "current", "output_sha256": "a69804634e6eec7259ea51434be7f460e0cacc0f218efeb7139dbab5363256a5", "exit": 0},
 {"command": "grep -n -m3 -i 'research method' ../chousa-shokunin/PROVINCE.md", "source_locator": "SKILL.md:3", "round10_verdict": "current", "output_sha256": "a5aecd59e7cce362b0a23aeaf70042d73bdb0229a09b6c8287b4088a4e2dfc20", "exit": 0},
 {"command": "grep -n -i shonen /home/vgpnk/.kimi-code/skills/shokunin/SKILL.md", "source_locator": "SKILL.md:3 (Rank: shonen)", "round10_verdict": "current", "output_sha256": "060d4722e672e8584d00b99fcf72e95a339d50c2ac1fe5592e268dcfc9f9b164", "exit": 0},
 {"command": "head -12 PROVINCE.md", "source_locator": "SKILL.md:8-19 (domain prose)", "round10_verdict": "current", "output_sha256": "58e2e7d5fe70ed5f5e151ede16deec787baeb405f4104d4bfd89ac5a96534c6e", "exit": 0}
]
```

## 5. Verdict

- **Shard verdict: `current`.** Zero stale items, zero `stale-fixed`, zero `stale-documented`,
  zero `to-verify` in this range. No fix was required and none was made — `SKILL.md` bytes were
  not touched by this shard.
- No web citations exist in range, so no access attempt was applicable; the absence is proven by
  the c02 sweep rather than asserted.
- **Boundary note for other shards:** line 20 is the `## Decision table` heading; the table body
  (lines 21-29, surface names like `conlang-methodology`) begins shard 02's range. Round-9 registry
  citations `SKILL.md:164/181/248` are outside this shard.
- Cross-repo reads (sibling PROVINCE.md files, fleet README/PROTOCOL, the user-scope shokunin
  skill) were read-only; every write of this seat lives in `kotodama-shokunin/reports/round-10/drift/shard-01.md`
  and untracked `.scratch/`.

## Appendix — verbatim segment (sha256 `926bd755...`)

```
---
name: kotodama-shokunin
description: "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible. Triggers: 'design a language', 'conlang', 'culture for this world', 'mythology of', 'symbolism of', 'naming system', 'costume/dress terms', 'era language stages', 'word for this concept'. Anti-trigger: NOT world-bible canon recording or consistency verification (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin), NOT real-world rights/attribution rulings. Rank: shonen."
---

# kotodama-shokunin — linguistic-cultural systems (言霊)

Domain: the generative craft that connects languages, cultures, myths,
symbolisms, and eras to their linguistics and costumes for a fictional
world — and hands the resulting systems to the world bible. 言霊
(kotodama, "word-spirit") names the core premise: a culture's language is
not decoration on its world; it is evidence of it. Myth shapes vocabulary,
era shapes register, costume carries a lexicon, and symbols fossilize into
words.

This repo is the craft's home. The world bible itself — entities, relations,
timeline, canon consistency — belongs to lore-shokunin; this lane supplies
languages and cultural systems to it, never edits it.

## Decision table
```
