# supplement-opencode-1 — 07 SCRIBE: historical corrections (round-3/4 records)

- Wave: `supplement-opencode-1` (not a numbered round; not GLM round 5)
- Role: **07 SCRIBE — read-only historical correction.** This file is the only artifact written by this worker. `LOG.md`, `SCORECARD.md`, `SKILL.md`, `corpus/`, and all frozen round-3/4 artifacts were **not** edited; no commits were made; no gate was executed (see §8).
- Baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404` (== `HEAD` during the audit; `git rev-parse HEAD` → `fe34faa…`)
- Audit time (UTC): 2026-10-17T15:43Z (final re-verification); worktree was clean w.r.t. HEAD for every file pinned below.
- All records here are **author-side evidence**; no SHONEN `[x]`, rank, or promotion claim is made.
- Source-recheck role note: no corpus entry was assigned to this role, so no public-source audit JSON is produced (that artifact belongs to the source-recheck workers). Every recheck below is against the committed source of record: frozen outputs, `MANIFEST.tsv`, packet/component bytes, and git history. One recheck exercises a *coupling* rather than an isolated item — the round-4 era retag (dress/era fix) re-diverging into the naming gate's NAME-NEAR class, traced in §4.

Method: dedicated Read/Grep tools for content, `awk`/`python3`/`sha256sum`/`git` for counting and hashing; no shell `grep`/`rg` was executed. All commands quoted below were actually executed at `fe34faa`, with the outputs given.

## 1. What the frozen artifacts actually contain

### 1.1 Per-file finding counts and classes (executed command, abridged output)

Command:

```sh
for f in tools/gates/frozen/round-3/*.out tools/gates/frozen/round-4/*.out; do
  n=$(awk '/^FINDING /{c++} END{print c+0}' "$f")
  cls=$(awk '/^FINDING /{print $2}' "$f" | sort | uniq -c | tr -s ' ' | tr '\n' ';')
  printf '%s | findings=%s | classes=%s\n' "$f" "$n" "$cls"
done
```

Observed (round 3, final freeze):

| file | findings | classes |
|---|---:|---|
| `round-3/phonology-sanity-gate.out` | 3 | 3 A-NEUTRAL |
| `round-3/lexicon-coverage-audit.out` | 0 | — (0 bytes) |
| `round-3/myth-consistency-gate.out` | 1 | 1 MC-S00 (one aggregate line) |
| `round-3/costume-era-consistency-gate.out` | 10 | 10 G-ERA |
| `round-3/naming-collision-gate.out` | 20 | 1 PHON-CODA; 10 PHON-INVENTORY; 8 DERIV-HOLD; 1 CROSS-HOLD |
| `round-3/provenance-mesoamerica-primary-sources.out` | 0 | — (INFO lines only) |
| `round-3/provenance-gate-frozen-run-standard.out` | 0 | — (INFO lines only) |
| **round-3 total (5 culture + 2 provenance runs)** | **34** | 3+0+1+10+20 |

Observed (round 4 freeze — only these five files exist; there is **no** `MANIFEST.tsv` and **no** `inputs/` under `round-4/`):

| file | findings | classes | sha256 |
|---|---:|---|---|
| `round-4/phonology-sanity-gate.out` | 3 | 3 A-NEUTRAL | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` |
| `round-4/lexicon-coverage-audit.out` | 0 | — (0 bytes) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `round-4/myth-consistency-gate.out` | 0 | — (0 bytes) | `e3b0c442…b7852b855` |
| `round-4/costume-era-consistency-gate.out` | 0 | — (0 bytes) | `e3b0c442…b7852b855` |
| `round-4/naming-collision-gate.out` | 18 | 1 CROSS-HOLD; 6 NAME-NEAR; 1 PHON-CODA; 10 PHON-INVENTORY | `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e` |
| **round-4 total** | **21** | 3+0+0+0+18 |

Totals re-derived:

```sh
cat tools/gates/frozen/round-4/*.out | awk '/^FINDING /{c++} END{print c}'   # → 21
cat tools/gates/frozen/round-3/{costume-era-consistency-gate.out,lexicon-coverage-audit.out,myth-consistency-gate.out,naming-collision-gate.out,phonology-sanity-gate.out} | awk '/^FINDING /{c++} END{print c}'   # → 34
```

The same counts were obtained through the dedicated Grep tool (pattern `^FINDING `, count mode) and agree with the `awk` results.

### 1.2 Round-3 `MANIFEST.tsv` re-verification (all hash cells)

Command (run over both `round-3/MANIFEST.tsv` and `round-3/attempt-1/MANIFEST.tsv`):

```sh
while IFS=$'\t' read -r gate gsha input isha exit cnt output osha snap cmd; do
  [ "$gate" = "gate" ] && continue
  g=$(sha256sum "$gate" | cut -d' ' -f1); s=$(sha256sum "$snap" | cut -d' ' -f1); o=$(sha256sum "$output" | cut -d' ' -f1)
  printf '%s | gate:%s snap:%s out:%s exit=%s count=%s\n' "$gate" \
    "$([ "$g" = "$gsha" ] && echo OK || echo MISMATCH)" \
    "$([ "$s" = "$isha" ] && echo OK || echo MISMATCH)" \
    "$([ "$o" = "$osha" ] && echo OK || echo MISMATCH)" "$exit" "$cnt"
done < tools/gates/frozen/round-3/MANIFEST.tsv
```

Result: **7/7 rows OK** (gate script, input snapshot, output — 21 hash cells) for the final manifest; **7/7 OK** for `attempt-1` as well, where `costume-era-consistency-gate` records `exit=2 count=1` (the known `G-DATA` assembly-contract error retained by design). The final manifest's `finding_count` column (3, 0, 1, 10, 20, 0, 0) equals the re-derived counts, and the recorded exit codes are 1, 0, 1, 1, 1, 0, 0.

Round-3 input identity re-checked: `tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml` hashes to `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` (matches the manifest `input_sha256` column; also the hash quoted in `ASSEMBLY.md`). The live `examples/culture-d2/packet.d2.yml` at `fe34faa` hashes to `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` (the v1.1 packet; the round-3 snapshot is the v1 packet, as expected).

**Supported prior claim:** round-3's recorded total of 34 findings with the breakdown `3 + 0 + 1 + 10 + 20` is fully supported by committed bytes (`LOG.md:1928–1939`, `ASSEMBLY.md:55–65`, `MANIFEST.tsv`).

## 2. Correction A — the round-4 finding total: **21, not 24**

Superseded text (baseline `fe34faa`; `LOG.md` sha256 `126b87b3415757b8c0007f2215df7620d283657ac0bc5bf48c3b11307e102b90`):

- `LOG.md:2001–2003`: "depth — D2 design findings <= 10 after fixes (from 34). **Measured: 24** (phonology 3 REVIEW honest-remaining, lexicon 0, myth 0 FIXED, costume 0 FIXED, naming 18)."
- Commit `fe34faa` subject: "round 4 (REJECTED as declared; coverage verified): D2 v1.1 **34->24** findings, 2 classes eliminated; 179 entries; 17 audits".

Corrected fact: the five frozen round-4 outputs contain exactly **21** `FINDING` lines: `3 + 0 + 0 + 0 + 18` (§1.1). The corrected class flow is in §4. The record's own parenthetical lists 3, 0, 0, 0, 18 — it sums to 21, so the sentence is internally inconsistent with its "24". No committed counting basis for 24 exists anywhere in the repo; the nearest simple arithmetic (`34 − 10 costume = 24`) is a **hypothesis, not established** (it ignores the myth −1, the DERIV-HOLD −8, and the NAME-NEAR +6 that the same frozen artifacts show).

Scope of the correction: the commit subject of `fe34faa` cannot and must not be amended (history is append-only); the correction supersedes it from a new, appended record citing the hash.

Verdict: **contradicted** (recorded 24 vs frozen 21).

## 3. Correction B — the audit count: **16 committed audit files, not 17**

Superseded text:

- `LOG.md:2012–2013`: "17 audit reports, defects named per batch."
- `SCORECARD.md:12` (coverage row): "…round 4: 179 entries (africa landed); README regen; **17 audit reports**"; `SCORECARD.md:31` (capabilities row): "corpus/lessons/round-4-audit/ (**17 reports**)".
- `corpus/lessons/round-4-sol-fixes-and-audits.md:11–13`: "**17 audit reports under round-4-audit/** (header/calibration/flag-basis apparatus checks across all 148 seeded entries + gap entries)."

Measured, at `fe34faa`:

```sh
ls corpus/lessons/round-4-audit/ | wc -l                                  # → 16
git show fe34faa --name-only | awk '/round-4-audit/' | wc -l             # → 16
```

The 16 committed files: `civ-01-07.md` … `civ-85-92.md` (13 batch files covering civilizations entries 01–92) plus `culture-material.md`, `linguistics.md`, `myth-symbol.md`. No 17th file under `round-4-audit/` exists in `fe34faa` or in the worktree. The only committed file that could be miscounted as a 17th "audit report" is `corpus/lessons/round-4-sol-fixes-and-audits.md`, which is **not** under `round-4-audit/` and is a fixes-and-audits summary, not a per-partition audit. Under either reading, the phrase "17 audit reports under round-4-audit/" is not reproducible.

Related coverage boundary worth recording while correcting the count:

- The 16 files audit 4 of the 6 corpus partitions (civilizations, culture-material, linguistics, myth-symbol). No `synthesis` (24 files) or `verification` (13 files) partition audit is among them.
- "across all 148 seeded entries" (sol-fixes line 12) is **not reproducible** from the committed tree: `find corpus/knowledge -name '*.md' | wc -l` → 179 (civ 94, culture-material 16, linguistics 16, myth-symbol 16, synthesis 24, verification 13); the audit batch labels cover 92 civilizations entries + 48 other partition entries = 140 entry files. State unknown for the basis of 148; not re-asserted.

Verdict: **contradicted** (17 recorded vs 16 committed).

## 4. Class flow 34 → 21, and why "24" and "2 classes eliminated" mislead

Measured class deltas (round-3 → round-4), from §1.1:

| class | round 3 | round 4 | delta |
|---|---:|---:|---:|
| A-NEUTRAL (phonology) | 3 | 3 | 0 |
| MC-S00 (myth) | 1 | 0 | −1 |
| G-ERA (costume) | 10 | 0 | −10 |
| PHON-INVENTORY (naming) | 10 | 10 | 0 |
| PHON-CODA (naming) | 1 | 1 | 0 |
| DERIV-HOLD (naming) | 8 | 0 | −8 |
| CROSS-HOLD (naming) | 1 | 1 | 0 |
| NAME-NEAR (naming) | 0 | 6 | **+6** |
| **total** | **34** | **21** | **−13** |

- Three round-3 classes emit no round-4 lines: `MC-S00`, `G-ERA`, `DERIV-HOLD`. One new class appears: `NAME-NEAR`, whose six lines flag the era entities `E0/E1/E2/E3` as 1-edit-apart pairs. That new class is the trace of the dress/era coupling: the round-4 costume fix (`09-eras-calendar.yml` era retag with a declared map, committed in `fe34faa`) made the era tags collidable, and the naming gate's recall-oriented check fired. So "2 classes eliminated" (LOG `:2003`) is ambiguous rather than plainly false — three round-3 classes are gone from the output, but one round-3 class was replaced by a newly visible one, and the frozen artifact cannot decide which two the author meant.
- The net naming change is correctly recorded as 20 → 18 (supports `LOG.md:2003` and `claims.json`'s `naming_findings` = {NAME-NEAR 6, PHON-CODA 1, PHON-INVENTORY 10, CROSS-HOLD 1} = 18).

### 4.1 Correction C — the round-4 DERIV residual wording is stale at `fe34faa` (contradicted with limits)

Superseded text:

- `corpus/lessons/round-4-sol-fixes-and-audits.md:31–33`: "**DERIV-REPLAY ×8**: component 03 now carries explicit regex rules that the naming gate cannot replay — the gate needs a derivation adapter (or the assembler needs to materialize derived forms into the packet)."
- Commit `fe34faa` subject residual list: "DERIV-REPLAY adapter".
- The committed packet carries the same stale claim internally: `examples/culture-d2/packet.d2.yml:79` (`derivation_contract.unresolved`): "13 currently supplies only B1 as formation.stem for NM-01..NM-08 … the unchanged naming records remain DERIV-REPLAY findings with the binary rule below."

Contradicted by the committed state of the same revision:

- `examples/culture-d2/components/13-naming.yml:4`: "Serialize both bases in all eight NM formation.stem inputs as B1+B2 … the unchanged gate can then replay the actual compound instead of receiving B1 alone" (all eight records carry e.g. `formation: {stem: su+nel, bases: [su, nel], rule: UP-COMPOUND, …}`, component lines 55–134).
- `packet.d2.yml:153–165` declares rule `UP-COMPOUND` with `pattern: ^(?P<B1>[a-záéíóú]+)[+](?P<B2>[a-záéíóú]+)$`, `output: "{B1}{B2}"`.
- `tools/gates/naming-collision-gate.py` (byte-identical between rounds 3 and 4 — sha256 `8c5afb0a…` equals the round-3 `MANIFEST.tsv` `gate_sha256` column) replays `stem` against the rule (`_gate_c`, lines 1266–1324) and emits `DERIV-REPLAY` only when `re.fullmatch` fails or the output differs. A binary stem `su+nel` against the binary pattern matches and reproduces `sunel`.
- The frozen round-4 naming output contains **no** `DERIV-HOLD` and **no** `DERIV-REPLAY` lines — consistent with the replay path succeeding, inconsistent with the "remains DERIV-REPLAY findings" note.

Conclusion: the `DERIV-HOLD` class (8 lines) is genuinely absent at round 4 because component 13's stems were fixed and the rules declared — not because the gate stopped looking. The residual queue item "DERIV-REPLAY ×8 / the gate cannot replay" describes a mid-round state, not `fe34faa`. **Not re-executed here** (§8): the confirmation that the frozen output byte-matches a fresh gate run on the committed packet is left to the frozen-replay worker; the class-flow statement above rests on the committed output, the unchanged gate code, and the committed packet.

Verdict: **contradicted** (with the stated limits).

## 5. Unresolved — state unknown, deliberately not re-asserted

Per scope: launch-item evidence that is not committed stays unknown rather than invented.

1. **Dispatch counts.** Round-3 "round swarm 34 agents … 25 completed, 3 launch failures …, 6 items absent" (`LOG.md:1989–1992`; also narrated in `corpus/lessons/round-3-d2-build.md:7`) and round-4 "32 agents … 31 completed, 1 unaccounted" (`LOG.md:1999–2000`) appear only as author narration. No committed machine record exists in the repo (no `.ufo/`, no swarm logs; `Glob` over the fleet `.ufo/` for `kotodama*` returns no matches). Status: **unknown / author-asserted only**.
2. **Round-4 exit codes and input digests.** `frozen/round-4/` has no `MANIFEST.tsv` and no input snapshots, unlike round 3. Output bytes are now pinned above, but exit codes are unpinned and the 0-byte outputs cannot by themselves prove `exit 0`. The round-4 battery's fidelity to the committed packet is for the frozen-replay worker to establish.
3. **"7/7 selftests green" (round-4, `LOG.md:2005–2006`).** No round-4 selftest outputs are committed; `round-3/selftests/` holds six outputs (6/6 pass text), not seven. The 7th gate (`handoff-packet-check.py`, added in `1688790`) has no frozen selftest output in either round. The *fixture-unchanged* half of the claim is supported: `git log --oneline -- tools/gates/fixtures/` shows the last change at `1688790` (round 2), i.e. untouched by rounds 3 and 4.
4. **Freshness "22 (33 -> 11)" (`LOG.md:2008–2009`).** Not reproducible as recorded. Measured on `mesoamerica-primary-sources.md` (python `str.count`, not grep): baseline `c610e0a` = 39 `to-verify` occurrences / 35 parenthesized / **32 lines containing it**; at `fe34faa` = 12 / 9 / **11 lines**. Reproducible deltas: 32→11 lines (−21) or 39→12 occurrences (−27); neither equals "33 → 11 (22)". The basis of the recorded 33/22 is unknown; not re-asserted.
5. **"60-row ledger" (`LOG.md:2009`; sol-fixes `:13–14`).** `corpus/lessons/round-4-triage/mesoamerica.md` is a 60-**line** file carrying 36 disposition rows (`M01–M36`); "row" and "line" are conflated in the record.
6. **SCORECARD gate-count drift.** `SCORECARD.md:13` (operability row) cites `ls tools/gates/*.py | wc -l` = 6, "measured against round-1 commit". At `fe34faa` the same command yields **7** (the round-2 handoff gate). The row's citation is time-pinned, but a refresh pass should note that the number no longer reproduces at the current revision.
7. **"148 seeded entries"** (sol-fixes `:12–13`): no partition combination measured matches it (§3); left unknown.

## 6. Proposed append-only correction wording (DRAFT — parent-owned write; not applied by this worker)

For `LOG.md`, appended after the existing entries, citing this report (wording preserved as a single correction entry; supersedes by naming the text it corrects):

> ## 2026-10-17 — supplement-opencode-1 correction: round-3/4 record counts (append-only)
>
> Corrections to the round-4 entry of 2026-10-17 (README of record:
> `reports/supplement-opencode-1/07-historical-corrections.md`, baseline
> `fe34faaafbe0add59ff68827a0df6c5782a72404`):
>
> - The round-4 depth measurement is corrected: **21 findings, not 24** —
>   `cat tools/gates/frozen/round-4/*.out | awk '/^FINDING /{c++} END{print c}'`
>   → `21` (= phonology 3 + lexicon 0 + myth 0 + costume 0 + naming 18; the
>   entry's own parenthetical already sums to 21). Output sha256: naming
>   `4d70252b…`, phonology `1ce5f0cd…`, myth/costume/lexicon `e3b0c442…`
>   (0 bytes each). Commit `fe34faa`'s subject "34->24" is superseded by
>   "34->21"; that commit is not amended. Class flow: MC-S00 −1, G-ERA −10,
>   DERIV-HOLD −8, NAME-NEAR +6 (era tags E0–E3); A-NEUTRAL 3,
>   PHON-INVENTORY 10, PHON-CODA 1, CROSS-HOLD 1 unchanged. The round-3 total
>   of 34 (3+0+1+10+20) is re-verified, including all 7×3 hash cells of
>   `tools/gates/frozen/round-3/MANIFEST.tsv`.
> - "17 audit reports" is corrected to **16** committed files under
>   `corpus/lessons/round-4-audit/` (`ls … | wc -l` → 16;
>   `git show fe34faa --name-only | awk '/round-4-audit/' | wc -l` → 16);
>   no synthesis/verification partition audit is among them, and
>   "148 seeded entries" is not reproducible.
> - The round-4 residual "DERIV-REPLAY ×8 / the gate cannot replay" (lesson
>   file; packet `derivation_contract.unresolved`) is stale at `fe34faa`:
>   component `13-naming.yml` serializes all eight `formation.stem` inputs as
>   B1+B2 and `packet.d2.yml` declares `UP-COMPOUND` with a binary pattern,
>   so the unchanged gate replays; the frozen output contains no DERIV lines.
> - Dispatch counts (round 3: 34/25/3/6; round 4: 32/31/1) have no committed
>   artifact; recorded as unknown, not re-asserted.

## 7. Pinned hashes (baseline `fe34faa`)

| artifact | sha256 |
|---|---|
| `LOG.md` | `126b87b3415757b8c0007f2215df7620d283657ac0bc5bf48c3b11307e102b90` |
| `SCORECARD.md` | `32ca9cbf3a4456da5521ac41f1b5210ace2cd0a18e25974d6c84a5d063c6a9fb` |
| `corpus/lessons/round-4-sol-fixes-and-audits.md` | `adc871785798b0719f758ad376af3216a12f258510ba3449b7332a90e0d6f846` |
| `examples/culture-d2/components/13-naming.yml` | `e0c01eb22977e76e78251cd0b6f8f0b81d1917ca77c9ead04d06b1559b47b6df` |
| `examples/culture-d2/packet.d2.yml` | `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | `d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399` |
| `tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml` | `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` |
| `tools/gates/frozen/round-4/naming-collision-gate.out` | `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e` |
| `tools/gates/frozen/round-4/phonology-sanity-gate.out` | `1ce5f0cdabad1bda177245607226cb6bf643f2bfbbe2ddb0918c510749066dd2` |
| `tools/gates/frozen/round-4/{myth,costume,lexicon}*.out` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) |

Revision pins: `git rev-parse HEAD` → `fe34faaafbe0add59ff68827a0df6c5782a72404`; round-3 commit `c610e0abd8edf90d6c6d86ebebdc7a7cba8d4a0b`; commits touching `tools/gates/fixtures/` and `tools/gates/*.py`: `291c714`, `1688790` only.

## 8. Limits and integrity

- **No gate execution.** This worker deliberately did not run any gate script (read-only role; gate self-tests rewrite fixtures and execution would write `__pycache__`). The replay confirmation of round-4 outputs against the committed packet remains the frozen-replay worker's evidence.
- **No writes outside this file.** `LOG.md`, `SCORECARD.md`, `corpus/`, `examples/`, `tools/`, and every frozen artifact are untouched by this worker; no commit was made. Counts re-derivable with the commands quoted in §1–§4.
- **Worktree context.** During the audit the worktree carried other workers' in-flight edits (`git status --short` as of 2026-10-17T15:43Z: `M corpus/knowledge/civilizations/{africa-primary-sources,ottoman,slavs-early}.md`, `M examples/culture-d2/components/{06-pantheon,07-myths-motifs}.yml`, `M tools/assemble-d2.py`, plus untracked supplement workers' dirs/scripts). None of those files are pinned or counted here; every file pinned in §7 was unmodified against HEAD at audit time.
- **Frozen bytes preserved.** No edit, rename, or annotation was applied to any round-3/round-4 artifact; no corpus erratum was added — Corrections A–C concern records (`LOG.md`/`SCORECARD.md`/lesson/packet notes), not corpus knowledge entries, and the packet is generator-owned, so the corrections are proposed for the parent to land in the parent-owned files.
