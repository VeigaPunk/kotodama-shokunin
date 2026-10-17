# R10-F05 — drift shard 05: SKILL.md lines 81-100

- round: 10 (loop 1 of 3; build round 3 of 4); worker: L2 drift re-runner 05
- date: 2026-10-17; lane: kotodama-shokunin; baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (ancestor of HEAD `e3a1ec9`; confirmed in `.scratch/shard-05/git-identity.txt`)
- shard range: `SKILL.md:81-100` — the error-patterns table, rows 5-20
- TMPDIR: `$PWD/.scratch`; all receipts under `.scratch/shard-05/`
- live shas at read time: `SKILL.md` `17d1326caa50a3186c43404a96c0595709703d619c5994754e72877ef6197c59`; `tools/d2-typed-labels.py` `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` (identical at baseline `9dc18ec`); `SCORECARD.md` `cc032db8b2749d492cea0847a894d303916c944f23757f54dd2dd26f8d5f7bee`; full list in `.scratch/shard-05/cited-sha256.txt` (`cde0ed94…`)

Lines 81-84 (static language / modern garment words / names without morphology / detached myth) carry **no citable artifact** — nothing to re-run or locate there. Lines 85-100 carry 21 citable items: 9 current, 12 stale-documented (4 code-id drift, 8 line-number drift, of which 2 are also live behavior gaps). No URLs in this range, so no web access attempts are needed.

## 1. Executed commands (every runnable artifact in range)

| # | command | exit | stdout sha256 | verdict |
|---|---|---|---|---|
| 1 | `python3 tools/d2-typed-labels.py --selftest` | 0 | `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` | current — 39/39 checks pass ("the three shard control matrices, the loader/parser malformed cases, the live-packet typing and reconciliation cases, and the CLI emit/check/tamper controls") |
| 2 | `python3 tools/d2-typed-labels.py` (default packet) | 1 | `b232dffb365f39598caa0abd79917ed009705d0c327b0a0e701436f1a1a6f869` | current — `labels_by_kind={'borrowed-strata': 2, 'native-form': 46, 'translated-label': 10}`, `label_findings_hold=10`, exit 1 (aggregate stays red) |
| 3 | `python3 tools/d2-typed-labels.py --json` | 1 | `880d0e45f75f1c14c9528a80a70ff1b6d1c034145ed741796f7038f03c124624` | current — codes observed: `D2L-FORM-UNRESOLVED`×10, `D2L-NATIVE`×2, `R-RANK-CONFLICT`×4; **zero** `TL-*` codes |
| 4 | `python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-b4.d2.yml` (L-26 `stage` E1→E0; B4 clock control) | 1 | `e1b3f538e96c87fbef44a022183c0a70578e552dc71783116b3fd723f4035c24` | current — line 1: `FINDING D2L-BORROW: [fail] L-26 — entry_stage E0 precedes referent_available_from E1` |
| 5 | `python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-kindless.d2.yml` (typed_labels entry with no `kind`; SKILL:90 class) | 1 (uncaught) | `f7341e84f3ff7e1b9d3eb3986f828cc6b66f56135714f81919b16e50cd2b774` | **stale + new finding N1** — `KeyError: 'kind'` traceback at `tools/d2-typed-labels.py:2497`; direct `validate_labels` gives exit 2 with stable `D2L-DATA` ("required field 'kind' is missing"; "kind None is not one of ('translated-label', 'native-form', 'borrowed-strata')") — receipt `debug-kindless.out` `9f885663…` |
| 6 | `python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-r5.d2.yml` (CTL-03 `native-form`, `status: to-verify`, no bytes; SKILL:88 class) | 1 | `b5480e214fd27026426202f66268b9e1d1569727a34421859da7f79ef6ab6b3d` | **stale + new finding N2** — 16 findings, none for CTL-03; direct run: `findings for CTL-03: NONE` (`debug-r5.out` `5867bead…`) — no HOLD, silent |
| 7 | `python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-compare-only.d2.yml` (CTL-02 `compare_only: true` + unresolved slot; design-spec R3 class) | 2 | `2ce334574a2e552141cda8ae4b9ee54f614025cbccacffe23b01b0042c00b6ea` | current — `FINDING D2L-SCOPE: [fail] CTL-02 — compare_only is not a licensed exemption for typed labels` + `D2L-FORM-UNRESOLVED` hold |
| 8 | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` (the command behind SKILL:85's frozen claim, from `22-label-representation.md:29`) | 1 | `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b` | current-with-note — live: 6 `NAME-NEAR` + 10 `PHON-INVENTORY` + 1 `CROSS-HOLD` (17 lines); frozen file: 18 lines incl. `PHON-CODA PAN-03`; the single-line diff is explained by the documented PAN-03 packet repair (`examples/culture-d2/packet.d2.yml:1163-1180`: alias "Humweha — the retired pre-repair spelling"; `repair_basis` huma+weha). Gate sha moved `8c5afb0a…`→`d9e4e8f4…`, packet `d5fb4088…`→`e0f21509…` since the 22-report's pinned baseline `fe34faa` |
| 9 | `sha256sum tools/gates/frozen/round-4/naming-collision-gate.out` + line/GAR counts | 0 | file sha `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e`, 18 lines, 10 `GAR-*`, 10 `PHON-INVENTORY` | current — matches `22-label-representation.md:20` exactly |
| 10 | phrase-locator sweeps (`grep -n` for each cited phrase; `.scratch/shard-05/locators.txt` `58e27ee5…`) | 0/1 | see §2 | 8 stale line numbers, 0 missing content |

## 2. Locator verdicts (per citation item)

| SKILL line | citation | live check | verdict |
|---|---|---|---|
| 85 | `22-label-representation.md` §1 (frozen 10/10 `GAR-*`) | §1 = lines 12-95; minimal-packet repro `PHON-INVENTORY=10` all `GAR-*`; frozen file sha + counts match | current |
| 86 | `22-label-representation.md:126-128` | rule 2 at 126-128, "HOLD — never a silent pass" (128) | current |
| 86 | executable `TL-01` | `grep -c "TL-01" tools/d2-typed-labels.py` = **0**; live id is `D2L-FORM-UNRESOLVED` (tool:426; 10 live holds; selftest "the owed form slots stay held, never passed") | **stale — id drift** |
| 87 | `22-label-representation.md:129-130` | rule 3 at 129-130, "the native bytes govern; the check cannot be waived by labelling" | current |
| 88 | `22-label-representation.md:131-132` | rule 4 at 131-132, HOLD without bytes | current |
| 88 | executable `TL-01` | id absent (as above); **and** the declared-sound-kind-no-bytes class is silent in the live tool (N2) | **stale — id drift + behavior gap** |
| 89 | `22-label-representation.md:133-134` | rule 5 at 133-134, untyped legacy still checked | current |
| 90 | `tools/d2-typed-labels.py` `TL-02` | `grep -c "TL-02"` = 0; live kindless typed label → `D2L-DATA` fail + CLI traceback (N1), not a hold | **stale — id drift + behavior gap** |
| 91 | design spec R3 (`compare_only` unresolved) | `reports/round-8/depth/design-spec.md:160-169` (live) states it; tool:787-789 implements `D2L-SCOPE`; control #7 reproduces | current |
| 92 | `language-contact.md:78-79` | 78 = "Two principles worth their weight in canon:"; principles at **80-81** | **stale — line number (off by 2)** |
| 93 | `loanword-material-dating.md:26,60` | :26 = blank line after §2 heading (**heading at 25**, clocks table 27-34); :60 = exact ("It does not establish withdrawal of the object or people") | **stale (:26 off by 1) / current (:60)** |
| 93 | executable B4 | design-spec:210-215 defines B4; tool `check_borrow` (tool:693, clock check 720-724) implements it; control #4 reproduces `D2L-BORROW` FAIL | current |
| 94 | `garment-lexicon-crosslinguistic.md:26` | 26 = blank; content at **28** ("switched referent in transit") and **30** ("two coexisting names") | **stale — line number** |
| 95 | `loanword-material-dating.md:57` | 57 = "Recipient form reflects a donor innovation" row; claimed text ("Dictionary selection bias; imported prestige terminology for local goods") at **59** | **stale — line number (off by 2)** |
| 96 | `costume-language-coupling-table.md:40` | 40 = table separator; claimed text ("A modern curatorial label becomes an attested historical native word") at **43** | **stale — line number (off by 3)** |
| 97 | `era-language-staging.md:124` | 124 = costume/style-period row; claimed text ("Apply sound laws to an inherited spoken label; separately track … translation, exonym, or official replacement") at **127** | **stale — line number (off by 3)** |
| 98 | tool `FIELD_DEFAULTS` | `grep -c "FIELD_DEFAULTS"` = 0; kinds `fictional-coordinate`/`descriptive-gloss` also absent from the live tool (0 occurrences; tool docstring:7-12 and `KINDS` tool:414 ship **three** kinds). The class is handled instead by translated-label projection + era reconciliation; the "neither enters the sound channel" behavior is current (selftest "no GAR label is graded on the sound channel") | **stale — id + kind names** |
| 99 | `naming-collision-gate.md:69-70` | 69-70 = spacing/punctuation + compatibility rows; claimed text ("A collision in that output channel, not native-script identity") at **72** | **stale — line number (off by 2)** |
| 100 | `naming-collision-gate.md:52` | 52 = symbolic-system row; claimed text ("A shared garment label need not mean identical cut or status") at **54** | **stale — line number (off by 2)** |

Line-number drift was already present at authoring: at `e1694ba` (the round-8 commit that added this table) `language-contact.md` lines 78-81 read exactly as live (heading 78, principles 80-81) — `.scratch/shard-05/git-identity.txt`. The corpus files have not changed since `e1694ba`; the content of every claim is present, only the pointers are off.

## 3. Stale items for the F15-F18 fixers

- **S1 (ids).** `SKILL.md:86`, `:88` (`TL-01`), `:90` (`TL-02`), `:98` (`FIELD_DEFAULTS`) name code strings that exist nowhere in the live tool (all counts 0; tool sha `0da0015f…`). Live vocabulary is `D2L-*` (tool:423-431), classes in `design-spec.md:533-544`. The design-spec itself recorded the duty at `design-spec.md:581`: "D02 declares one mapping table; ids are names, the classes in §6 are the contract" — no TL→D2L mapping table exists in the live tool (grep 0). Fix: update the four citations to the live ids (`D2L-FORM-UNRESOLVED`, `D2L-DATA`) or land the mapping table; do not rewrite filed round-8 report bytes.
- **S2 (line numbers).** Eight pointers: `language-contact.md:78-79`→80-81; `loanword-material-dating.md:26`→25/27-34; `:57`→59; `garment-lexicon-crosslinguistic.md:26`→28,30; `costume-language-coupling-table.md:40`→43; `era-language-staging.md:124`→127; `naming-collision-gate.md:69-70`→72; `:52`→54. Content verified present; fix by updating the pointers.
- **S3 (SKILL:88 behavior).** The claimed executable hold for "a sound kind declared with no bytes supplied" is not live for `native-form`/`borrowed-strata` records — see N2. Either the tool gains the R5 hold (design-spec:174-176 requires it) or the SKILL row must state the live mechanism (translated-label + owed form slot).
- **S4 (SKILL:90 behavior).** The claimed "hold with a stable reason" is not live — see N1. Fix either the tool (stable exit 2 per its own contract) or the row.

## 4. Findings surfaced by this shard (route: freshness fixer / operability tracker)

- **N1 — CLI traceback on a malformed `typed_labels` entry (kind missing).** `python3 tools/d2-typed-labels.py --packet <packet with a kindless typed_labels entry>` crashes: `KeyError: 'kind'` at `tools/d2-typed-labels.py:2497` (coverage stats index `parse_result["labels"]` after the kind check `continue`s at :750-752). This violates the tool's own documented contract, "2 = could-not-evaluate (malformed input, `P-*` loader code or `D2L-DATA`; stable message, no traceback)" (tool:40-42). The selftest's L1/L2 malformed controls call `parse_typed_labels` directly (tool:2743-2748), so the CLI stats path is untested — that is why 39/39 still passes. Control: re-run receipt `control-kindless2.out` (`f7341e84…`); expected after fix: exit 2 with a stable `D2L-DATA` message, no traceback.
- **N2 — R5 silent for declared sound kinds with no bytes.** A label `kind: native-form`, `status: to-verify`, no `text` (with field reasons in `issues`) produces **zero findings** (`debug-r5.out` `5867bead…`; CLI receipt `control-r5.out` `b5480e21…`, 16 findings, none for CTL-03). `design-spec.md:174-176` (R5) requires `D2L-FORM-UNRESOLVED` HOLD. The hold logic (tool:784-796) covers only `translated-label`; `check_sound_form` early-returns for non-supplied status (tool:672). The translated-label + owed-slot class does hold correctly (10 live holds), so the gap is specific to the declared-sound-kind path. Control: re-run receipt `control-r5.out`; expected after fix: a `D2L-FORM-UNRESOLVED` hold for CTL-03.

## 5. Notes / cross-references

- `SCORECARD.md:128` cites the same `TL-01/TL-02` (its `B4` part is current) — belongs to the SCORECARD shard; flagged here so the ledger scribe can de-duplicate.
- The live-vs-frozen gate difference (#8) is *explained*, not silent: the PAN-03 repair is documented inside the packet (`packet.d2.yml:1163-1180`), and the frozen file is the historical round-4 record, unchanged (`4d70252b…`). No action needed unless a round-10 claim re-asserts live byte-identity with frozen.
- Nothing in this shard needed `to-verify` marking: every item was verified by command output or file/line inspection.
- **Concurrent edits observed (post-sweep).** `SKILL.md` was edited by sibling round-10 workers while this shard was written (`17d1326c…` → `52d5f4d1…`). One in-range item is already fixed: line 96 now reads `costume-language-coupling-table.md:43` (was `:40`; same fix applied at line 73). Still unfixed in range as of this note: `TL-01` (86, 88), `TL-02` (90), `FIELD_DEFAULTS` (98), `language-contact.md:78-79` (92), `loanword-material-dating.md:26`/`:57` (93, 95), `garment-lexicon-crosslinguistic.md:26` (94), `era-language-staging.md:124` (97), `naming-collision-gate.md:69-70`/`:52` (99, 100). §2's verdicts are a snapshot at the read shas; re-check against the file before fixing to avoid clobbering sibling edits.

## 6. Machine-readable rows (for R10-F14 ledger)

```json
[
 {"command": "python3 tools/d2-typed-labels.py --selftest", "source_locator": "SKILL.md:86,88,90,93,98 (tool authority)", "round10_verdict": "current", "output_sha256": "7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252", "exit": 0},
 {"command": "python3 tools/d2-typed-labels.py", "source_locator": "SKILL.md:85-100 (live vocabulary)", "round10_verdict": "current", "output_sha256": "b232dffb365f39598caa0abd79917ed009705d0c327b0a0e701436f1a1a6f869", "exit": 1},
 {"command": "python3 tools/d2-typed-labels.py --json", "source_locator": "SKILL.md:86,88,90 (finding ids)", "round10_verdict": "stale-documented", "output_sha256": "880d0e45f75f1c14c9528a80a70ff1b6d1c034145ed741796f7038f03c124624", "exit": 1},
 {"command": "python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-b4.d2.yml", "source_locator": "SKILL.md:93 (executable B4)", "round10_verdict": "current", "output_sha256": "e1b3f538e96c87fbef44a022183c0a70578e552dc71783116b3fd723f4035c24", "exit": 1},
 {"command": "python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-kindless.d2.yml", "source_locator": "SKILL.md:90 (TL-02 hold claim)", "round10_verdict": "stale-documented", "output_sha256": "f7341e84f3ff7e1b9d3eb3986f828cc6b66f56135714f81919b16e50cd2b774", "exit": 1},
 {"command": "python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-r5.d2.yml", "source_locator": "SKILL.md:88 (TL-01 hold claim)", "round10_verdict": "stale-documented", "output_sha256": "b5480e214fd27026426202f66268b9e1d1569727a34421859da7f79ef6ab6b3d", "exit": 1},
 {"command": "python3 tools/d2-typed-labels.py --packet .scratch/shard-05/packet-compare-only.d2.yml", "source_locator": "SKILL.md:91 (design spec R3)", "round10_verdict": "current", "output_sha256": "2ce334574a2e552141cda8ae4b9ee54f614025cbccacffe23b01b0042c00b6ea", "exit": 2},
 {"command": "python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml", "source_locator": "SKILL.md:85 (frozen 10/10 GAR-*)", "round10_verdict": "current", "output_sha256": "ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b", "exit": 1},
 {"command": "sha256sum tools/gates/frozen/round-4/naming-collision-gate.out; grep -c GAR-", "source_locator": "SKILL.md:85 (frozen record)", "round10_verdict": "current", "output_sha256": "4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e", "exit": 0},
 {"command": "grep -n <cited phrase> <cited file> (11 locators; locators.txt)", "source_locator": "SKILL.md:92-100 (eight line-number drifts)", "round10_verdict": "stale-documented", "output_sha256": "58e27ee54f66ec1cd356ff66d71e8d86bf5f084bc68b1fcae0a5e5918db0ddd1", "exit": 1}
]
```

FILES: reports/round-10/drift/shard-05.md | SUMMARY: 21 citation items in SKILL.md:81-100 checked live — 9 current, 12 stale-documented (TL-01/TL-02/FIELD_DEFAULTS ids gone in favor of D2L-*, eight corpus line pointers off by 1-3 lines), plus two new live behavior gaps (kindless record crashes the CLI with a traceback at tools/d2-typed-labels.py:2497; declared-sound-kind-no-bytes is silently ignored, no R5 hold).
