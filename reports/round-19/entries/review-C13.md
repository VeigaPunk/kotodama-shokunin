# R19-C23 — reviewer of entry `generated-artifact-roundtrip-verification.md`

- round: 19 (loop 2 of 3, build round 3 of 4; `hyper/deepseek-v4.1-flash`),
  lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- date: 2026-10-18, stamps UTC. Window 11:31–11:42Z. Baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: **NON-CANON** engineering review; author-side evidence only; no
  admission, no promotion verification.
- writes: **this file only** plus `.scratch/r19c/`. No corpus/tool/filed-round
  byte touched. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/verification/generated-artifact-roundtrip-verification.md` —
new verification entry, gap `generated-artifact-roundtrip-verification`
(`reports/round-19/gaps.md`, seat R19-C13). Anchor: sha256
`66d9aa18f4e23ad4ad0ba11662241f4d3e6a03afaa4cd40b24bc029d58bb13e1`, 12,934
bytes, 84 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: all four mandated checks pass.** No defect found. The entry's own
§6 open obligation (the assembly gate ships no `--selftest`) is independently
confirmed and is the round's live issue.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

Head block = L1–19 (first `## ` at L21). `- topic:` L3, `- sources:` L5
(9 nested sub-bullets), `- couples:` L16, `- source:` L17, `- verified-at:` L18,
`- recheck:` L19; `- gap filled:` L4. Decision record `## 6.` (L76), rows 1–6.
Instrument `.scratch/r19c/check.py` → `missing_frontmatter=[] gap=True
decision_record=True`.

## 2. Source resolvability — PASS

| cited surface | this seat's check (11:35–11:41Z) | result |
|---|---|---|
| `python3 tools/assemble-culture-d4.py --check` | exit 0, `packet.d4.yml: byte-identical deterministic assembly` | **matches** KTD-GA-S-0002 |
| `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | exit 0, same line | **matches** |
| `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | exit 0, `byte-identical deterministic projection` | **matches** |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | exit 0, `39/39 checks passed` | **matches** |
| `python3 tools/gates/d4-assembly-check-gate.py --selftest` | exit 2, `assembly error: [Errno 2] No such file or directory: '--selftest'` | **matches** the entry's §6 open obligation |
| `tools/gates/frozen/round-18/MANIFEST.tsv` rows 2–3 | present; rows pin `d4-typed-labels-check-gate.py` (input `a59990bb…`) and `d4-assembly-check-gate.py` (input `e7ecd204…`) | **matches** KTD-GA-S-0004 and §2's digests |
| `examples/culture-d4/ASSEMBLY.md` §1–§3 | present; §3 carries the measured run table | resolves |
| `reports/round-18/d4/determinism.md` | present | resolves |
| `https://reproducible-builds.org/docs/` | HTTP 200 | resolves |
| `https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf` | HTTP 200 | resolves |

All cited repo paths resolve; both URLs return 200.

## 3. No filler — PASS

- **Gap named and real** (L4). Re-run 11:40Z: `grep -rln -i "round-trip\|
  roundtrip\|serializer" corpus/knowledge/verification/` → this entry plus two
  round-19 siblings that cite it; nothing pre-existing. `gate-frozen-run-standard.md`
  covers frozen runs, not regeneration round-trip.
- **Delivers**: an artifact-chain table (§2), a 5-class corruption taxonomy with
  per-class controls (§3), a 6-row control matrix (§4), a non-proof shelf (§5),
  a 6-row decision record (§6).
- **Calibration**: Thompson 1984 and the NIST SHA-256 standard are both bounded
  explicitly ("cited for digest construction only, never as a truth measure for
  content"); reproducible-builds is cited as a discipline, not a content claim.
- **Canon hygiene**: §6-4 requires the green be reported as "byte-identity of a
  NON-CANON artifact", never as soundness.

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.273**
  (`gate-frozen-run-standard.md`) — no near-duplicate; the nearest neighbours
  are cited for mechanics, not restated.
- **vs round-19 siblings**: J=0.470 with `synthesis/generated-artifact-lifecycle.md`
  — the intended design/check pair (the lifecycle workflow and its verification
  procedure), mutually named in `couples:`. Recorded, not scored.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| — | none against this entry | — | — |

Observation for the parent (out of this entry's authorship): the entry records
in §6 that `tools/gates/d4-assembly-check-gate.py` ships no `--selftest`. That
absence now also makes the **gate battery** report `battery_exit 2,
unevaluable 1` once the D4 gates enter its constant (see
`review-C14.md`). The two entries' findings are the same fact seen from two
sides.

## 6. Limits

- Author-side review only. The round-18 receipts (`determinism.md`,
  `MANIFEST.tsv`) were read by path, not re-executed — the entry says the same.
- The corruption taxonomy's classes C1–C5 are design assertions this seat did
  not attempt to instantiate; only the C4 control (the projector selftest's
  `--check exit 1 on a changed byte`) is a measured case.
- Verdicts bind to sha256 `66d9aa18…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C13.md
