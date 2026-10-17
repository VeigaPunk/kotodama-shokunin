# Drift shard 10 — SKILL.md lines 181-200 (R10-F10)

- date: 2026-10-17 (measurement window 18:26–18:29 local = 21:26–21:29 UTC)
- shard: R10-F10 (freshness drift re-runner, shard 10 of 13)
- source surface: `SKILL.md` lines 181-200 (sha256 of range: `c58d05d660b5753ef64730ffb2cf954890bc4bf613aef6793e32f5641624e6d7`; whole file: `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`)
- baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (declared in `reports/round-10/claims.json`); live HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
- `git diff --stat 9dc18ec..HEAD -- SKILL.md` → empty, exit 0: the shard bytes are unchanged since baseline, so every verdict below is against baseline content.
- isolation: `export TMPDIR=$PWD/.scratch`; every command ran in the disposable full-tree mirror `.scratch/r10f10/iso/` (`tar` copy of the repo excluding `.git`/`.scratch`/`__pycache__`). Live tree untouched by this shard: `find tools examples -type f | sha256sum` before vs after → identical (`LIVE-TREE-IDENTICAL`). The two ` M` files in `git status` at close (`corpus/README.md`, `reports/round-9/validation.json`) are concurrent coverage workers' edits, not this shard's.
- environment note (corroborates rounds 8–9): `/tmp` is still inode-exhausted — `df -i /tmp` → `1048576 1048576 0 100% /tmp`, 2026-10-17T21:29Z. All scratch artifacts are in-lane under `.scratch/r10f10/`.

## What lines 181-200 contain

The "Gates and probes" registry table (12 rows, lines 183-194): seven structural gates (`phonology-sanity-gate`, `lexicon-coverage-audit`, `myth-consistency-gate`, `costume-era-consistency-gate`, `naming-collision-gate`, `provenance-audit`, `handoff-packet-check`), plus `frozen-replay`, `uncertainty-inventory`, `D2 assembly drift`, the contrastive craft example, and the isolated legacy selftest battery. Each row carries an entry command, verdict map, self-test spelling, pinned-value path, write scope. Prose 196-200 carries three claims: the contrastive checker is example-specific; `--counts` echoes the exercise's declared `audit_counts` block after checks; its embedded historical counting-command string points to ignored scratch and is not an executable instruction; the `LAW-ORDER` early-return limitation is recorded in `reports/round-5/15-cli-review.md`. Lines 201-212 (battery limits, round-5 runner) are shard 11's surface and were not re-run here.

## Inventory: runnable commands in range

`awk 'NR>=181 && NR<=200' SKILL.md | grep -cE 'python3|--selftest'` → **12**, exit 0. No URLs in range (`grep -cE 'https?://'` → 0), so no web access attempt was required.

## Entry commands + selftests — results (all in mirror)

All output hashes are sha256 of combined stdout+stderr (`.scratch/r10f10/out/<label>.out`). ID-set comparison = sorted unique `FINDING <id>` vs the committed `.expected`.

| locator | surface / command (fixture instantiation) | exit | output sha256 (short) | verdict |
|---|---|---|---|---|
| SKILL.md:183 | `phonology-sanity-gate.py tools/gates/fixtures/phonology-sanity-gate.yml` | 1 | `b3843b2a5f50…` | current — 16 FINDING lines / 15 IDs, set identical to `.expected` |
| SKILL.md:183 | `phonology-sanity-gate.py --selftest` | 0 | `3e9a1209afa3…` | current — "fixture exit 1; 15/15 planted finding IDs present; 29 control cases passed" |
| SKILL.md:184 | `lexicon-coverage-audit.py …/lexicon-coverage-audit.yml` | 1 | `af5794955b60…` | current — 20 lines / 18 IDs, set match |
| SKILL.md:184 | `lexicon-coverage-audit.py --selftest` | 0 | `fd731b142344…` | current — "14/14 checks passed" |
| SKILL.md:185 | `myth-consistency-gate.py …/myth-consistency-gate.yml` | 1 | `88385088ca2e…` | current — 6 lines / 6 IDs, set match |
| SKILL.md:185 | `myth-consistency-gate.py --selftest` | 0 | `80e7d9dc86a2…` | current — "fixture exit 1; planted IDs MC-P01…MC-S02; clean control exit 0" |
| SKILL.md:186 | `costume-era-consistency-gate.py …/costume-era-consistency-gate.yml` | 1 | `482c1597a220…` | current — 25 lines / 21 IDs, set match; stdout sha equals the round-9 baseline's own `stdout_sha256 482c1597…08b3` |
| SKILL.md:186 | `costume-era-consistency-gate.py --selftest` | 0 | `add8c431f07e…` | current — "10/10 checks passed; fixture exit 1 with 21 planted finding IDs" |
| SKILL.md:187 | `naming-collision-gate.py …/naming-collision-gate.yml` | 1 | `bea0fd3925c2…` | current — 12 lines / 11 IDs, set match |
| SKILL.md:187 | `naming-collision-gate.py --selftest` | 0 | `d3566a9cad69…` | current — "fixture findings 12 across 11 ids; positive control clean; malformed inputs exit 2" |
| SKILL.md:188 | `provenance-audit.py tools/gates/fixtures/provenance` | 1 | `01340bcc1cba…` | current — 6 lines / 6 IDs, set match; `INFO scan: files=7 marks=2 mark-lines=2 findings=6 blocked=0` |
| SKILL.md:188 | `provenance-audit.py --selftest` | 0 | `0a655a0193ae…` | current — "7 fixture file(s), planted IDs …; exit 1 on defect tree, exit 0 clean, exit 2 missing path" |
| SKILL.md:188 | `provenance-audit.py --self-test` (alias probe) | 2 | `8c2fa8c30b54…` | current — alias is not claimed; matches round-9 registry note ("`--self-test` unrecognized"), see DR-10-03 |
| SKILL.md:188 | `provenance-audit.py corpus/knowledge/verification/gate-frozen-run-standard.md` (corpus-path instantiation) | 0 | `2e5af73aea6a…` | current — `INFO scan: files=1 marks=0 mark-lines=0 findings=0 blocked=0` |
| SKILL.md:189 | `handoff-packet-check.py …/handoff-packet-check.md` | 1 | `ec1ec331a820…` | current — 11 lines / 9 IDs, set match (`.expected` has no trailing newline; compared as a set) |
| SKILL.md:189 | `handoff-packet-check.py --selftest` | 0 | `be1ef058b2cf…` | current — "fixture findings 11 across 9 ids; clean control exit 0; CLI verified from another cwd" |
| SKILL.md:190 | `replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | `76c00a6b80d4…` | **stale-documented** — see DR-10-01; identical output live and in mirror |
| SKILL.md:190 | `replay-frozen.py --selftest` | 0 | `4d6aaea127ad…` | current — "79/79 checks passed"; includes `gate-digest-mismatch: exit 2` control |
| SKILL.md:191 | `source-audit-inventory.py --json` | 0 | `7cc43e4476cc…` | current — valid JSON; `totals: files=179, files_with_marker=118, marker_occurrences=584`; hash is path-dependent (output embeds the absolute root) |
| SKILL.md:191 | `source-audit-inventory.py --selftest` | 0 | `ecb685112afe…` | current — "SELFTEST PASS: 3 planted entries, exact counts, no-write and determinism checks, … exit-code controls" |
| SKILL.md:192 | `assemble-d2.py --check` | 0 | `2fa0c8c19745…` | current — "packet.d2.yml: byte-identical deterministic assembly"; read-only (no live/mirror byte changed) |
| SKILL.md:192 | `assemble-d2.py --selftest` | 0 | `a81294c03476…` | current — "42/42 checks passed …; no file outside the temporary directory touched" |
| SKILL.md:193 | `check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | `18128adfc703…` | current — "OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)" |
| SKILL.md:193 | `check-craft-exercise.py … --counts` | 0 | `20ecc4716330…` | current — printed JSON is **exactly equal** (programmatic `==`) to the exercise's declared `audit_counts` block; it echoes `counting_command` verbatim |
| SKILL.md:193 | `check-craft-exercise.py … --report reports/supplement-opencode-1/32-craft-exercise.md` | 0 | `18128adfc703…` (same as plain run) | current — report file byte-identical before/after (read-only claim holds) |
| SKILL.md:193 | `check-craft-exercise.py --selftest` | 0 | `77d408e10a49…` | current — "SELFTEST OK 10/10 tamper cases detected; CLI-SELFTEST OK 18/18 cases passed" |
| SKILL.md:194 | `check-gate-battery.py` (committed default) | 2 | `3109467a7752…` | **stale-documented** — see DR-10-02; duty 1 `pass 7 / fail 0 / unevaluable 0`, duty 2 `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]` |
| SKILL.md:194 | `check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` | 0 | `08ac35b8caa3…` | current — `baselines_found 8, pinned 8, gates_uncovered []` (green control) |
| SKILL.md:194 | `check-gate-battery.py --selftest` | 0 | `8b1fdd6f2d31…` | current — "SELFTEST OK 28/28 controls behaved as expected" |

Supporting checks: script sha256s of all seven gates are byte-identical to the round-9 registry values (7/7; the registry lists no script sha for `replay-frozen.py`). The battery script differs from the registry's mid-wave value `9ad0ef95…` — committed bytes now `0a126b70…`; the registry itself recorded the script was under active edit during round 9. All 12 committed gate fixtures and both `.expected` files are byte-identical to the round-9 registry values (`SAME` ×12); `provenance.expected` and `provenance-audit.expected` are byte-identical to each other (`7ba4fa5cd326…`). Mirror fixtures after all selftests equal live fixtures (`MIRROR-FIXTURES-EQUAL-LIVE`): the five fixture-writing selftests rewrote nothing. Battery `originals {preserved: true, modified 0, added 0, deleted 0}`; mirror `removed: true`.

## Findings

### DR-10-01 — round-3 frozen replay no longer reproduces (stale-documented; claim text lives in shard 09's range)

- Locator: `SKILL.md:162` (shard 09's range, recorded here because row 190 is in range 181-200 and I instantiated it): "Frozen replay exits 0 with recorded findings" with the exact command `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`. Also `SKILL.md:177` "The round-3 TSV recording is replayable".
- Observed (live and mirror, identical output, sha `76c00a6b80d4…`): exit **2**, `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s)` — every row `reason=gate_digest_mismatch`, e.g. phonology pinned `fb05c644cafb…` vs live `d5fe087ffb23…`; lexicon `63ee4ec6b151…` vs `2c4dd39702a1…`; myth `26d246e9936d…` vs `5368b13542cd…`; costume `29a9361c7b96…` vs `e6bffd7020c0…`; naming `8c5afb0a5abc…` vs `d9e4e8f4f93a…`; provenance `4aaea6e98b97…` vs `8a96aaf4ccd1…` (twice).
- Cause: `tools/gates/frozen/round-3/MANIFEST.tsv` was committed at `c610e0a` (round 3, its only commit) and pins round-3-era gate bytes; all seven gates were revised in rounds 4-9. The replay tool's pin enforcement is working as designed — it refuses to re-bless revised gates. This is not a tool defect.
- History: `reports/round-8/depth/docs.md` §2.4 already flagged the claim as "not satisfied at this revision" when 1 of 7 rows mismatched (phonology); by round 10 the count is 7 of 7. `SKILL.md` was not amended, and the file that does reproduce (round-9 D3 proposal manifest, `reports/round-9/d3/replay.md`, `REPLAY OK: 5/5`) is scratch and uncommitted.
- Verdict: **stale-documented** (this shard writes only its own report). Fix routing for F15-F18 / orchestrator: amend `SKILL.md:162`/`:177` to state the round-3 manifest is pin-frozen history that now reads could-not-evaluate (7/7), or commit a re-frozen baseline under a new manifest. Do not silently re-pin.

### DR-10-02 — battery committed default still exits 2 on pin discovery (stale-documented; round-9 §5 item 6 remains open)

- Locator: `SKILL.md:194` — row claims entry command `python3 tools/check-gate-battery.py` with verdict map "0 seven selftests pass / 1 recognized selftest failure / 2 could-not-evaluate".
- Observed: the committed invocation exits **2** on the delivered tree, output sha `3109467a7752…`. Duty 1 is green: `pass 7 / fail 0 / unevaluable 0`, `originals {preserved: true, modified 0}`. Duty 2 fails closed: `baselines_found 5, pinned 5, gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]` with two `BASELINE-GATE-UNCOVERED` findings ("no committed expected.json under the declared roots"). The two pins still live only under `reports/round-9/baselines/`; the script's `BASELINE_ROOTS` are still `(tools/gates/expected, tools/gates/frozen)`.
- Green control: the three-root invocation (above) exits 0 with `baselines_found 8, pinned 8, gates_uncovered []`.
- Verdict: **stale-documented** — the row's verdict map describes duty 1 only; the round-9 registry (§5 item 6) recorded the same reading and left the root convention to the orchestrator. Round 10 has not moved the pins; a SKILL row that says "0 seven selftests pass" while the committed command exits 2 remains misleading until either the pins are relocated or the row documents duty 2.

### DR-10-03 — provenance `--self-test` alias (current, no action)

- `python3 tools/gates/provenance-audit.py --self-test` → exit 2 (`8c2fa8c30b54…`), while `--selftest` exits 0. The SKILL row claims only `--selftest`, and the round-9 registry already measured this asymmetry; no drift.

### Note — inventory `--json` hash is path-dependent (current)

`source-audit-inventory.py --json` embeds the absolute scan root in its output, so `output_sha256 7cc43e44…` names the mirror run (`.scratch/r10f10/iso/corpus/knowledge`); a live-tree run will hash differently by construction. Totals themselves (`files=179, marker_occurrences=584`) are content counts, not affected.

### Note — prose claims in 196-200 verified (current)

- `--counts` echo: programmatic equality with the exercise's `audit_counts` → `True` (keys incl. `counting_command`, `total: 7`).
- Embedded historical counting-command string: the exercise JSON (`sound-change-vs-taboo.json:367`) carries `"counting_command": "python3 reports/supplement-opencode-1/scratch/32/check_exercise.py … --counts"`; that path is ignored — `git check-ignore -v` → `.gitignore:5:/reports/supplement-opencode-1/scratch/`. The public entry command (`tools/check-craft-exercise.py`) is the executable one; claim holds.
- `LAW-ORDER` limitation: `reports/round-5/15-cli-review.md` §F4 ("LAW-ORDER early return silently skips most checks", line 57; persistence noted at line 232) — recorded as claimed.

## Ledger rows (for the F14 scribe)

Commands were run inside the mirror `.scratch/r10f10/iso/` with `TMPDIR=$PWD/.scratch`; `output_sha256` is sha256 of combined stdout+stderr. "current" = behaves as its SKILL row declares on the committed inputs.

```json
[
  {"id": "R10-F10-01", "command": "python3 tools/gates/phonology-sanity-gate.py tools/gates/fixtures/phonology-sanity-gate.yml", "source_locator": "SKILL.md:183", "round10_verdict": "current", "output_sha256": "b3843b2a5f50809ffe43fd55212cb9ab320f4ac98c2a59c6f57c7bcc61617018", "exit": 1, "note": "16 FINDING lines / 15 IDs, set identical to .expected; mirror run"},
  {"id": "R10-F10-02", "command": "python3 tools/gates/phonology-sanity-gate.py --selftest", "source_locator": "SKILL.md:183", "round10_verdict": "current", "output_sha256": "3e9a1209afa352902922a64df1d0bf7a48c25cf09126aa62b70855bd3b447843", "exit": 0, "note": "15/15 planted IDs, 29 control cases"},
  {"id": "R10-F10-03", "command": "python3 tools/gates/lexicon-coverage-audit.py tools/gates/fixtures/lexicon-coverage-audit.yml", "source_locator": "SKILL.md:184", "round10_verdict": "current", "output_sha256": "af5794955b60b455b433a570434bf0ab69c110b66c891eab567d5addef0be4f4", "exit": 1, "note": "20 lines / 18 IDs, set match"},
  {"id": "R10-F10-04", "command": "python3 tools/gates/lexicon-coverage-audit.py --selftest", "source_locator": "SKILL.md:184", "round10_verdict": "current", "output_sha256": "fd731b1423443238cb5c1fc75dfd350244cc611295c9713b129252b251478658", "exit": 0, "note": "14/14 checks"},
  {"id": "R10-F10-05", "command": "python3 tools/gates/myth-consistency-gate.py tools/gates/fixtures/myth-consistency-gate.yml", "source_locator": "SKILL.md:185", "round10_verdict": "current", "output_sha256": "88385088ca2ee13192b9669a02cbe44aebf9c22df752a2af76138a13e1cf77d2", "exit": 1, "note": "6 lines / 6 IDs, set match"},
  {"id": "R10-F10-06", "command": "python3 tools/gates/myth-consistency-gate.py --selftest", "source_locator": "SKILL.md:185", "round10_verdict": "current", "output_sha256": "80e7d9dc86a29cf56591cfa0cf5bd8fab82a84d4b9d67f03200f1bd689c5aa53", "exit": 0, "note": "planted MC-* IDs, clean control exit 0"},
  {"id": "R10-F10-07", "command": "python3 tools/gates/costume-era-consistency-gate.py tools/gates/fixtures/costume-era-consistency-gate.yml", "source_locator": "SKILL.md:186", "round10_verdict": "current", "output_sha256": "482c1597a22096b2a0a09f09ce476f6ae5bbd6db70baf50df128fb0c1ed608b3", "exit": 1, "note": "25 lines / 21 IDs, set match; equals round-9 baseline stdout_sha256"},
  {"id": "R10-F10-08", "command": "python3 tools/gates/costume-era-consistency-gate.py --selftest", "source_locator": "SKILL.md:186", "round10_verdict": "current", "output_sha256": "add8c431f07e6f2f7772ce97a7a126d482c7848d5f622a8e455f76f88e0f4ad3", "exit": 0, "note": "10/10 checks, 21 planted IDs"},
  {"id": "R10-F10-09", "command": "python3 tools/gates/naming-collision-gate.py tools/gates/fixtures/naming-collision-gate.yml", "source_locator": "SKILL.md:187", "round10_verdict": "current", "output_sha256": "bea0fd3925c2745ecf6333733d1118deb9831241cf2d12e3742c571ec88a52ac", "exit": 1, "note": "12 lines / 11 IDs, set match"},
  {"id": "R10-F10-10", "command": "python3 tools/gates/naming-collision-gate.py --selftest", "source_locator": "SKILL.md:187", "round10_verdict": "current", "output_sha256": "d3566a9cad69f956fd7a4274cb80ad4b95a92bb63a9cf689e45338d05ca5c7da", "exit": 0, "note": "12 findings / 11 ids; malformed inputs exit 2"},
  {"id": "R10-F10-11", "command": "python3 tools/gates/provenance-audit.py tools/gates/fixtures/provenance", "source_locator": "SKILL.md:188", "round10_verdict": "current", "output_sha256": "01340bcc1cba9583906ea52014b691c990525a2b69d4a6dd61978774c9e129d2", "exit": 1, "note": "6 lines / 6 IDs, set match; INFO scan files=7 findings=6"},
  {"id": "R10-F10-12", "command": "python3 tools/gates/provenance-audit.py --selftest", "source_locator": "SKILL.md:188", "round10_verdict": "current", "output_sha256": "0a655a0193aec587c86f3f68a4730c5892198904a2e4e599377aa4d5ff802734", "exit": 0, "note": "7 fixture files, defect/clean/missing controls"},
  {"id": "R10-F10-13", "command": "python3 tools/gates/provenance-audit.py --self-test", "source_locator": "SKILL.md:188", "round10_verdict": "current", "output_sha256": "8c2fa8c30b5455e9400da96d56ceac88686f654b6cdffc1582ea716bad1d2b19", "exit": 2, "note": "alias not claimed by SKILL; matches round-9 registry note (DR-10-03)"},
  {"id": "R10-F10-14", "command": "python3 tools/gates/provenance-audit.py corpus/knowledge/verification/gate-frozen-run-standard.md", "source_locator": "SKILL.md:188", "round10_verdict": "current", "output_sha256": "2e5af73aea6acf18fdfd257b601b61aa3f97e2e2f37d2cac5214e034b3fc6cca", "exit": 0, "note": "corpus-path instantiation; 0 marks, 0 findings"},
  {"id": "R10-F10-15", "command": "python3 tools/gates/handoff-packet-check.py tools/gates/fixtures/handoff-packet-check.md", "source_locator": "SKILL.md:189", "round10_verdict": "current", "output_sha256": "ec1ec331a820f5eaa4dd916c99a404fa92223c06566ffe8c1e1b6f92a01064b3", "exit": 1, "note": "11 lines / 9 IDs, set match (.expected has no trailing newline)"},
  {"id": "R10-F10-16", "command": "python3 tools/gates/handoff-packet-check.py --selftest", "source_locator": "SKILL.md:189", "round10_verdict": "current", "output_sha256": "be1ef058b2cfc67a564003917fd39125121755ae66960bd9ea5feb04c0c7ef2f", "exit": 0, "note": "11 findings / 9 ids; clean control exit 0"},
  {"id": "R10-F10-17", "command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv", "source_locator": "SKILL.md:190 (claim at SKILL.md:162/177, shard 09)", "round10_verdict": "stale-documented", "output_sha256": "76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80", "exit": 2, "note": "7/7 gate_digest_mismatch; identical live and mirror; see DR-10-01; fix routing F15-F18/orchestrator"},
  {"id": "R10-F10-18", "command": "python3 tools/replay-frozen.py --selftest", "source_locator": "SKILL.md:190", "round10_verdict": "current", "output_sha256": "4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16", "exit": 0, "note": "79/79 checks incl. gate-digest-mismatch control"},
  {"id": "R10-F10-19", "command": "python3 tools/source-audit-inventory.py --json", "source_locator": "SKILL.md:191", "round10_verdict": "current", "output_sha256": "7cc43e4476cc7e66348e5dd5ad5ea1c043cdfbc1fde2f1766c17805b5ba45895", "exit": 0, "note": "files=179 marker_occurrences=584; hash path-dependent (embeds absolute root; mirror run)"},
  {"id": "R10-F10-20", "command": "python3 tools/source-audit-inventory.py --selftest", "source_locator": "SKILL.md:191", "round10_verdict": "current", "output_sha256": "ecb685112afea71e3b6d77ee38ca1935fbca0a0c900594bfebc265e2dcbd2121", "exit": 0, "note": "SELFTEST PASS incl. no-write and determinism checks"},
  {"id": "R10-F10-21", "command": "python3 tools/assemble-d2.py --check", "source_locator": "SKILL.md:192", "round10_verdict": "current", "output_sha256": "2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386", "exit": 0, "note": "byte-identical deterministic assembly; read-only"},
  {"id": "R10-F10-22", "command": "python3 tools/assemble-d2.py --selftest", "source_locator": "SKILL.md:192", "round10_verdict": "current", "output_sha256": "a81294c0347660d9b46952146bac967fc80c79c9d629d7f34e69d0411bec0336", "exit": 0, "note": "42/42 checks; nothing outside temp dir touched"},
  {"id": "R10-F10-23", "command": "python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json", "source_locator": "SKILL.md:193", "round10_verdict": "current", "output_sha256": "18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650", "exit": 0, "note": "audits=7 mech_cases=11 derivations=9 approx_checks_runner=37"},
  {"id": "R10-F10-24", "command": "python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --counts", "source_locator": "SKILL.md:193,199", "round10_verdict": "current", "output_sha256": "20ecc47163309805345d6dc6af0d11a304b9b567bfd8a18a28dd6745d10decfb", "exit": 0, "note": "printed JSON == exercise audit_counts (programmatic equality)"},
  {"id": "R10-F10-25", "command": "python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --report reports/supplement-opencode-1/32-craft-exercise.md", "source_locator": "SKILL.md:193", "round10_verdict": "current", "output_sha256": "18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650", "exit": 0, "note": "report file byte-identical before/after (read-only claim holds)"},
  {"id": "R10-F10-26", "command": "python3 tools/check-craft-exercise.py --selftest", "source_locator": "SKILL.md:193", "round10_verdict": "current", "output_sha256": "77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32", "exit": 0, "note": "10/10 tamper + 18/18 CLI cases"},
  {"id": "R10-F10-27", "command": "python3 tools/check-gate-battery.py", "source_locator": "SKILL.md:194", "round10_verdict": "stale-documented", "output_sha256": "3109467a775245d36f4612288f15836a1f1c004317320f0354d4bc9b9f6ea12a", "exit": 2, "note": "duty1 pass 7/fail 0; duty2 gates_uncovered [myth, naming]; see DR-10-02; round-9 §5 item 6 open"},
  {"id": "R10-F10-28", "command": "python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines", "source_locator": "SKILL.md:194", "round10_verdict": "current", "output_sha256": "08ac35b8caa36b7c42d19bd1e9f2c79f9d9229ea25b7ca5908a80c815959c83d", "exit": 0, "note": "green control: baselines_found 8 pinned 8 gates_uncovered []"},
  {"id": "R10-F10-29", "command": "python3 tools/check-gate-battery.py --selftest", "source_locator": "SKILL.md:194", "round10_verdict": "current", "output_sha256": "8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28", "exit": 0, "note": "28/28 controls"},
  {"id": "R10-F10-30", "command": "diff .scratch/r10f10/out/live-before.txt .scratch/r10f10/out/live-after.txt", "source_locator": "isolation check (SKILL.md:181-200 write-scope column)", "round10_verdict": "current", "output_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "exit": 0, "note": "empty diff (sha256 of empty string): no live byte written by this shard; mirrors cleaned"}
]
```

## Re-run recipe (for the F19 auditor)

1. `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch`
2. `sha256sum SKILL.md` → `2bce468d…1df1b`; `awk 'NR>=181 && NR<=200' SKILL.md | sha256sum` → `c58d05d6…e6d7`.
3. Build the mirror: `mkdir -p .scratch/r10f10/iso && tar --exclude=.git --exclude=.scratch --exclude=__pycache__ -cf - . | tar -xf - -C .scratch/r10f10/iso`
4. In the mirror, run the table's commands (entry + `--selftest` per row). Expected: 7 gates fixture exit 1 with ID sets equal to their `.expected`; all selftests exit 0; `assemble-d2 --check` exit 0; craft plain/counts/selftest exit 0; battery default exit 2 (myth+naming uncovered), 3-root exit 0, selftest exit 0.
5. `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → exit 2, 7 could-not-evaluate (DR-10-01). Compare live vs mirror output hashes: both `76c00a6b…`.
6. `python3 tools/gates/provenance-audit.py --self-test` → exit 2; `--selftest` → exit 0.

## Limits

- This shard covers only `SKILL.md:181-200`; SCORECARD rows, `reports/round-9/baselines/registry.md`, and SKILL lines 201-212 (battery limits prose, round-5 runner) are other shards' surfaces and were not re-run here except where a row in range instantiates them.
- Entry commands were instantiated with the committed fixtures/fixtures tree; a green fixture run demonstrates the executable surface and verdict map, not that any real culture packet passes.
- The `stale-documented` verdicts on DR-10-01/DR-10-02 are claim-text findings for F15-F18/orchestrator routing; no SKILL, gate, fixture or pin byte was modified by this shard.
- Author-side evidence only; no promotion, admission, or canon judgment is made here.
