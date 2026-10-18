# R19-C25 — reviewer of entry `two-reader-interop-agreement.md`

- round: 19 (loop 2 of 3, build round 3 of 4; `hyper/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- date: 2026-10-18, stamps UTC. Window 11:31–11:42Z. Baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: **NON-CANON** engineering review; author-side evidence only.
- writes: **this file only** plus `.scratch/r19c/`. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/verification/two-reader-interop-agreement.md` — new
verification entry, gap `two-reader-interop-agreement` (`reports/round-19/gaps.md`,
seat R19-C15). Anchor: sha256
`daebba3ae8253070538bc1c356e531dece9de189b33a32df04125b7036b093b6`, 12,333
bytes, 81 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: all four mandated checks pass.** No defect found.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

Head block = L1–19 (first `## ` at L21). `- topic:` L3, `- sources:` L5
(9 sub-bullets), `- couples:` L16, `- source:` L17, `- verified-at:` L18,
`- recheck:` L19; `- gap filled:` L4. Decision record `## 6.` (L73), rows 1–6.
Instrument → `missing_frontmatter=[] gap=True decision_record=True`.

## 2. Source resolvability — PASS

| cited surface | this seat's check (11:36–11:41Z) | result |
|---|---|---|
| `reports/round-18/d4/interop-2.md` §0–§1 | present; §1 "all 13 commands"; §2 "**12/12 commands with a byte reference match exactly**"; the single non-byte-stable command is the battery (stdout embeds its temp mirror path) | **matches** KTD-IA-S-0002 exactly |
| `reports/round-18/d4/interop-3.md` §0–§1 | present; §0 "the battery exits 0 with all seven gate selftests passing, **8/8 committed baselines pinned** and 0 uncovered; the round-11 frozen generation replays **11/11 rows**" | **matches** KTD-IA-S-0003 |
| `reports/round-18/d4/interop-1.md` §0–§1 | present (read by path) | resolves |
| the two D4 adapter legs | `d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` → exit 0, `byte-identical deterministic projection`; `d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` → exit 0, `byte-identical deterministic assembly`; peers' own `--check` modes produce the same lines | **matches** KTD-IA-S-0004 |
| `tools/gates/frozen/round-18/MANIFEST.tsv` rows 2–3 | present, `output_sha256` pinned | resolves |
| `https://doi.org/10.1109/TSE.1986.6312924` | HTTP 202 (DOI redirect) | resolves |
| `https://reproducible-builds.org/docs/` | HTTP 200 | resolves |

All cited repo paths resolve; both URLs resolve.

## 3. No filler — PASS

- **Gap named and real** (L4). Re-run 11:40Z: `grep -rln -i "interop\|two
  readers\|reader agreement" corpus/knowledge/` → this entry only; nothing
  pre-existing. The partition had single-tool verification and independence
  discipline but no entry stating the two-reader comparison shape.
- **Delivers**: a 5-row agreement-shape ladder E1–E5 (§2), a 5-row divergence
  disposition table (§3), a 5-row control matrix (§4), a non-proof shelf (§5),
  a 6-row decision record (§6).
- **Calibration**: Knight & Leveson 1986 is cited "as a calibration warning
  (with its documented methodological debate), not as a law" — the correct
  hedge for a contested result; Dijkstra is used for its real claim.
- **Canon hygiene**: §6-5 rejects agreement-as-correctness.

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.284**
  (`verification-independence-anti-circularity.md`) — no near-duplicate.
- **vs round-19 siblings**: J=0.413 with
  `generated-artifact-roundtrip-verification.md`; both are verification entries
  in the same D4 family and cross-couple. Recorded, not scored.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| — | none against this entry | — | — |

Point-in-time note for the parent: KTD-IA-S-0003's "8/8 committed baselines
pinned" is correctly attributed to the **round-18** receipt, and this entry does
not restate it as a live count. The live battery now reads 17 baselines / 9 gates
after the round's O change (see `review-C14.md`); the entry is not stale on this
point because it quotes the receipt, not the tool.

## 6. Limits

- Author-side review only. The three interop receipts were read by path, not
  re-executed — the entry states the same. This seat did not re-run the
  13-command standing regression set.
- The E1–E5 ladder's ordering is a design assertion; only E4/E5's D4 instances
  are measured.
- Verdicts bind to sha256 `daebba3a…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C15.md
