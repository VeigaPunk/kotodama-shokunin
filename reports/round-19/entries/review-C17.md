# R19-C27 — reviewer of entry `generated-artifact-lifecycle.md`

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

`corpus/knowledge/synthesis/generated-artifact-lifecycle.md` — new synthesis
entry, gap `generated-artifact-lifecycle` (`reports/round-19/gaps.md`, seat
R19-C17). Anchor: sha256
`a3393d06a3c234efd97d4e4121304b3beb093a7ed8f0991b1dab3f90918950bb`, 10,969
bytes, 84 lines, mtime 2026-10-18 11:40:11Z (stable at 11:41:52Z).

**Verdict: 3 of 4 mandated checks pass clean; 1 low-severity defect (a quoted
absence sweep that does not reproduce).**

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **pass** |
| no filler (gap named, real, delivered) | **pass**, with one false quoted sweep (§3) |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

Head block = L1–19 (first `## ` at L21). `- topic:` L3, `- sources:` L5
(9 sub-bullets), `- couples:` L16, `- source:` L17, `- verified-at:` L18,
`- recheck:` L19; `- gap filled:` L4. Decision record `## 6.` (L76), rows 1–6.
Instrument → `missing_frontmatter=[] gap=True decision_record=True`.

## 2. Source resolvability — PASS

| cited surface | this seat's check (11:35–11:41Z) | result |
|---|---|---|
| `examples/culture-d4/ASSEMBLY.md` §1–§3 | present; §1–§3 carry the chain and the measured run table | resolves |
| `examples/culture-d4/README.md` §"Reproduce" | present at L20 ("Reproduce from the repository root:"); L15 carries "never hand-edited" | resolves |
| `python3 tools/assemble-culture-d4.py --check` | exit 0, `packet.d4.yml: byte-identical deterministic assembly` | **matches** KTD-GL-S-0003 |
| `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | exit 0, same line | **matches** |
| `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | exit 0, `byte-identical deterministic projection` | **matches** |
| `tools/gates/frozen/round-18/MANIFEST.tsv` rows 2–3 | present | **matches** KTD-GL-S-0004 |
| `reports/round-18/d4/determinism.md` §0–§1 | present (read by path) | resolves |
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` §4/§9 | exist | resolve |
| `https://reproducible-builds.org/docs/` | HTTP 200 | resolves |

All cited repo paths resolve; the URL returns 200.

## 3. No filler — PASS, with one false quoted sweep

- The gap is real: before this round no synthesis entry stated which files are
  authored sources versus generated outputs and what a designer must do instead
  of editing an output.
- **The quoted absence sweep does not reproduce.** The entry says
  `grep -rln "generated artifact\|never hand-edit\|rebuild"
  corpus/knowledge/synthesis/` → **0 files**. Re-run 11:40Z it returns
  `corpus/knowledge/synthesis/loanword-material-dating.md` (pre-existing,
  round-17), whose L139 contains the substring **"rebuilding"** ("mosque
  rebuilding"). The hit is a substring artifact, not a real ownership overlap —
  but the claim "0 files" is false as written, and a rechecker running the
  quoted command will see one file.
- **Delivers**: a 5-row source/generated split table (§2), a 6-step rebuild loop
  R1–R6 (§3), a non-licence shelf (§4), a reviewer checklist (§5), a 6-row
  decision record (§6).

## 4. No duplication — PASS

- **Slug** unique against the 189-file baseline.
- **vs pre-existing corpus**: max token-Jaccard **J=0.238**
  (`gate-frozen-run-standard.md`) — no near-duplicate.
- **vs round-19 siblings**: J=0.470 with
  `verification/generated-artifact-roundtrip-verification.md` — the intended
  design/check pair, mutually named in `couples:`. Recorded, not scored.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| R19C27-F1 | The quoted absence sweep `grep -rln "generated artifact\|never hand-edit\|rebuild" corpus/knowledge/synthesis/` → 0 files does not reproduce: `loanword-material-dating.md` (pre-existing) matches on the substring "rebuilding". The gap remains real; the sweep wording needs narrowing (e.g. word-boundary or phrase form). | low | **open — reported to parent** |

## 6. Limits

- Author-side review only. The round-17/18 receipts were read by path, not
  re-executed (the entry states the same).
- The R1–R6 rebuild loop is a design assertion this seat did not attempt to
  falsify end-to-end.
- Verdicts bind to sha256 `a3393d06…`; a later edit invalidates them.
- NON-CANON throughout.

FILES: reports/round-19/entries/review-C17.md
