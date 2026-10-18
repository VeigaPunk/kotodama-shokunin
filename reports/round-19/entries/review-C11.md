# R19-C21 — reviewer of entry `label-channel-routing-verification.md`

- round: 19 (operator: loop 2 of 3, build round 3 of 4; 64 workers on
  `hyper/deepseek-v4.1-flash`, operator provider substitution;
  `reports/round-19/claims.json`), lane `kotodama-shokunin`, claim **C**.
- assignment (verbatim): "C R19-C21..C28 (entry reviewers x8): one per entry
  (poll, max 20 min): frontmatter, source resolvability, no filler, no
  duplication; verdicts reports/round-19/entries/review-<id>.md."
- date: 2026-10-18, stamps UTC. Review window 11:31–11:42Z. Lane baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`
  ("round-19: declare claims D/C/O").
- canon: **NON-CANON** engineering review. Author-side review evidence only; it
  admits no entry, promotes no claim, and is not independent promotion
  verification (lane rule, `AGENTS.md`).
- writes: **this file only**, plus gitignored scratch under `.scratch/r19c/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  corpus, tool, packet, or filed-round-8..18 byte touched. No commit, no push.

## 0. Artifact under review and verdict

`corpus/knowledge/verification/label-channel-routing-verification.md` — new
verification entry, gap `label-channel-routing-verification` (declared in
`reports/round-19/gaps.md` §"Declared gaps", seat R19-C11). Anchor revision:
sha256 `22e27dd62c345e1b1e1a73f2153c4403dbe9fdea8090b03b6af36fd7973675ca`,
13,830 bytes, 94 lines, mtime 2026-10-18 11:40:15Z (re-hashed stable at
11:41:52Z).

**Verdict: 3 of 4 mandated checks pass clean; 1 defect (a broken `couples:`
target).** No fabrication, no filler, no duplication.

| mandated check | verdict |
|---|---|
| frontmatter completeness | **pass** |
| source resolvability | **defect — 1 broken cross-reference** (§2) |
| no filler (gap named, real, delivered) | **pass** |
| no duplication of an existing entry | **pass** |

## 1. Frontmatter completeness — PASS

House profile of the five committed fields, each exactly once in the head block
(text before the first `## `, which is line 19): `- topic:` (L3), `- sources:`
(L5, 7 nested sub-bullets), `- couples:` (L14), `- source:` (L15),
`- verified-at:` (L16, dated 2026-10-18 and scope-bearing), `- recheck:` (L17).
The round-19 `- gap filled:` clause is present at L4. Decision record:
`## 6. Decision record — the routing rules this entry adopts` (L86) with rows
1–6, each carrying decision / consequence / status. Instrument:
`.scratch/r19c/check.py` → `missing_frontmatter=[] gap=True
decision_record=True`.

## 2. Source resolvability — DEFECT (1 broken cross-reference)

**Commands re-run by this seat** (lane root, `TMPDIR=$PWD/.scratch`, 11:35–11:41Z):

| cited command | this seat's re-run | matches entry? |
|---|---|---|
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | exit 1, `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` | **yes** |
| `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | exit 0, `byte-identical deterministic projection` | **yes** |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | exit 0, `39/39 checks passed` | **yes** |
| projection `coverage` block | `typed_labels 74`, `labels_by_kind {native-form 56, translated-label 12, borrowed-strata 6}`, `label_findings_fail 0`, `label_findings_hold 12` | **yes** |

URL: `https://doi.org/10.1109/TSE.2010.62` → HTTP 202 (DOI redirect to the IEEE
publisher landing page; resolvable). Cited repo paths resolve except one (§5).

### The defect: `../linguistics/phonology-sanity.md` does not exist

L14 `couples` names, under `linguistics —`, the target
`../linguistics/phonology-sanity.md`. Resolved from the entry's directory that is
`corpus/knowledge/linguistics/phonology-sanity.md`, which does not exist — the
partition holds `phonetics-phonology.md`. The intended target is almost
certainly `../linguistics/phonetics-phonology.md`; note the same entry already
cites the *verification* file `phonology-sanity-gate.md` (L14, resolves), so the
broken pointer is a duplicate-scope mistake, not a missing source.

- Severity: **low** — a couples pointer that does not resolve; no load-bearing
  claim depends on it, and the sound-channel discipline it gestures at is
  carried by `phonology-sanity-gate.md`, which does resolve.
- This is the assignment's own test ("open the cited path/URL"); non-resolving
  items are reported, never silently passed.

## 3. No filler — PASS

- **The gap is named and real.** The entry states it at L4 with an absence
  sweep. Re-run by this seat 11:40Z:
  `grep -rln -i "translated-label\|channel routing\|sound channel"
  corpus/knowledge/verification/` → only this entry. The routing *procedure*
  existed nowhere as a check before this round.
- **It delivers the gap**: a 6-row routing decision procedure (§2), a 6-row
  negative-control matrix (§3), a "what routing never proves" shelf (§4), a
  reviewer checklist (§5), and a 6-row decision record (§6). Decision tables and
  controls, not prose.
- **`QUALITY.md` bar**: provenance (7 cited sources, each with a locator);
  calibration (the mutation-testing survey is explicitly marked "a survey of a
  contested technique, cited as a design rule, not as a law"); coupling (L14
  names 5 partitions plus tooling); canon hygiene (L3 and §6-5 refuse clearance
  and hand canon to lore-shokunin).

## 4. No duplication — PASS

- **Slug**: absent from the 189-file baseline (`git ls-tree -r e571894
  --name-only corpus/knowledge`); no collision.
- **Topic overlap vs the pre-existing corpus** (token Jaccard, this seat's
  screen): max **J=0.247** (`verification-independence-anti-circularity.md`),
  then 0.219 (`gate-frozen-run-standard.md`) — no near-duplicate.
- **Sibling overlap**: J=0.509 against `synthesis/typed-label-routing-workflow.md`
  (this round). That is the design/check pair of one capability — the synthesis
  entry routes records, this one verifies the routing — and the two are
  cross-coupled by design (each names the other). Recorded, not scored as
  duplication.

## 5. Findings

| # | finding | severity | status |
|---|---|---|---|
| R19C21-F1 | L14 `couples` names `../linguistics/phonology-sanity.md`; no such file exists (`corpus/knowledge/linguistics/` holds `phonetics-phonology.md`). The same line already cites `phonology-sanity-gate.md`, which resolves. | low | **open — reported to parent**; this seat holds no corpus write |
| R19C21-F2 | Churn: the entry was revised mid-review (11:40:15Z, +340 B, 92→94 lines). One earlier defect was fixed in that revision: the L92 citation `reports/round-18/d4/ASSEMBLY.md` → `examples/culture-d4/ASSEMBLY.md`, and the corrected claim (§4 "records `tools/d2-typed-labels.py` refusing the D4 packet on `packet.eras`") was verified accurate against `examples/culture-d4/ASSEMBLY.md` §4. | informational | **resolved** |

## 6. Limits

- Author-side review, not independent promotion verification: this seat checked
  the entry against the same in-repo surfaces the author cites; it did not
  re-derive the projector's classification code.
- The round-18 receipts cited (KTD-LR-S-0005, `gate-runs-1.md`) were read by
  path, not re-executed.
- Verdicts bind to sha256 `22e27dd6…` (11:40:15Z). A later edit invalidates them.
- NON-CANON throughout; canon and any real-language claim are out of province
  (`PROVINCE.md`).

FILES: reports/round-19/entries/review-C11.md
