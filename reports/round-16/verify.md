# R16-V01 — verifier: independent re-run of the three fixer controls + regression

- Seat: **R16-V01** (verifier, O lane, round 16 — operator regimen loop 1,
  GLM round 2 of 2), run 2026-10-17 23:29–23:59 -03:00 from the lane root.
- Assignment: independently re-run all three fixers' controls (aggregate
  rejected; dangling L rejected; coverage/deviation per the F9-2/O03 recipe);
  regression: battery + craft + validators + frozen-verify selftests green;
  this file.
- Write scope: **this file only**, plus in-lane scratch
  `.scratch/r16-verify/` (`TMPDIR=$PWD/.scratch` set before every
  scratch-writing command). No filed round-8–15 byte was written; no git
  operation; no canon, rank, or real-world rights claim. All artifacts
  judged are NON-CANON.
- Tree at verify: HEAD `0ce7714` ("round-16: declare GLM-2 claims C/O"),
  baseline `16652e8` intact; worktree = `tools/harness/packet_links.py`
  modified (both harness fixers, region-disjoint, combined diff +112/−18)
  plus untracked round-16 artifacts. Fixer receipts read as filed:
  `reports/round-16/fixes/edge-source.md`
  (sha256 `13397209d0ec60c9a5cc5328c5469fa1e38fa754acd2012a719ed701a0cd7434`),
  `reports/round-16/fixes/l-anchor.md`
  (`37363d4dae6df47a989bdabfb6bee73aa3ab6e17e0695e4294a263ddd863604b`),
  `reports/round-16/fixes/orphan-census.py`
  (`ef7165c1e53025b4d808290a21c6be77d0dbfc4f376372f20e23836d60cff1ce`).
  Tool under test pinned at
  `66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899`.
- Method: no trust in the fixers' own runs — every control below was
  re-derived by this seat (own fixture packets, own census, HEAD-bytes
  BEFORE reproductions). Where a number is quoted from a receipt it is
  marked as such.

## 1. Control 1 — F10-1 aggregate rejected (`E-SOURCE-UNKNOWN`)

Baseline bytes (`git show HEAD:tools/harness/packet_links.py`): the string
`E-SOURCE-UNKNOWN` occurs **0** times and `resolve_edges` never reads the
`source` field — the review-10 gap is real in the baseline.

Independent fixture packet (this seat's own, `.scratch/r16-verify/
fixture-f10-1.json`: manifest row `A-FIX → examples/culture-d3/packet.json`
with live digest and `record_ids [L01, L02]`; one edge with the v1-style
prose source "29 coupling_note fields over examples/culture-d2/packet.d2.yml"
plus concrete targets `[L01, L02]` and a real claim id `CL-1`; one
concrete-source control edge; one resolving claim link):

```
python3 .scratch/r16-verify/run-fixtures.py
→ fixture-f10-1.json: exit=1 links=1 resolved=1 codes=['E-SOURCE-UNKNOWN'] PASS
  (2026-10-17 23:41 and re-run 23:47 on the combined bytes)
```

The prose-aggregate survivor yields exactly `E-SOURCE-UNKNOWN`, exit 1, and
**no other finding** — targets, claim crosswalk and digests stay clean, and
the concrete-source control edge passes (no over-rejection). Module selftest
agrees: 31 → **38 checks passed** (23:47), its own prose-aggregate /
missing-source / aggregate-id / unresolvable-path fixtures all green.
**Control 1: PASS.**

## 2. Control 2 — F9-1 dangling `#L<n>` rejected (`L-SELECTOR-UNRESOLVED`)

BEFORE (this seat captured it live on pre-edit bytes at ~23:31, and
reproduced from HEAD bytes at 23:57:
`git show HEAD:tools/harness/packet_links.py > .scratch/r16-verify/
packet_links_head.py`):

```
python3 .scratch/r16-verify/packet_links_head.py --links "examples/culture-d3/packet.json#L99" --repo-root .
→ ok [examples/culture-d3/packet.json#L99] links=1 resolved=1 findings=0  exit 0
  (HEAD selftest: 31 checks passed)
```

AFTER (fixed bytes, same probe, 23:37): `L-SELECTOR-UNRESOLVED […]
selector 'L99' resolves to no key path or value in
examples/culture-d3/packet.json`, `findings=1`, **exit 1**.

End-to-end fixture packet (this seat's own,
`.scratch/r16-verify/fixture-f9-1.json`: claim links
`["examples/culture-d3/packet.json#L01", "…#L99", "A-FIX#L77",
"AGENTS.md#L3"]` with the `A-FIX` manifest row):

```
python3 .scratch/r16-verify/run-fixtures.py
→ fixture-f9-1.json: exit=1 links=4 resolved=2
  codes=['L-SELECTOR-UNRESOLVED','L-SELECTOR-UNRESOLVED'] PASS
```

Both dangling shapes (`path#L99` and the artifact-form `A-FIX#L77`) reject;
the real lexeme `#L01` still resolves through record semantics and the
non-JSON line anchor `AGENTS.md#L3` is untouched (no over-rejection in
either direction). Line addressing of JSON bytes keeps working via the
colon form, re-verified 23:58: `--links
"examples/culture-d3/packet.json:78,examples/culture-d3/packet.json:991"`
→ `ok […:78]` + `L-LINE-RANGE […:991] line 991 beyond end … (990 lines)`.
Stamped-packet regression: all 50 filed v2-05 link specs still resolve
(`links=50 resolved=50`, 23:47; only finding is the expected
`M-DIGEST-MISMATCH` on the self-pinned harness row, §4). **Control 2: PASS.**

## 3. Control 3 — F9-2 coverage on the amended packet (build 07)

Amended packet landed 23:55 -03:00:
`reports/round-16/handoff/packet-v2-07.md`
(sha256 `1295f5b35c35a0c57f4e8a85800d75385fd1a1d5fe1d3e04727949407a4567d7`)
/ `packet-v2-07.yml`
(`717e29e5aecf4c1f5e2e154964553674cd559c7fbbddc0b5688fc489afd6438b`).

- **O03's standing census** (`python3 reports/round-16/fixes/orphan-census.py`,
  default packet = build 07 machine twin; selftest 3/3, 23:44): **exit 0 —
  delivered D3 record ids 64; carried in claim links 56; carried in edges
  only 8 (BR01–BR05, O01, O04, U01); orphans: 0** (23:56). Its build-05
  BEFORE control is reproduced by the packet's own dated receipt
  (packet-v2-07.md §validation, line 169): exit 1, orphans 33 (L03–L20,
  N01–N06, M01–M03, O02–O03, U03–U06) — exactly the review-9 census.
- **This seat's independent census** (`.scratch/r16-verify/orphan-census.py`,
  own coverage logic over the manifest-declared id set, cross-checked the
  D3 payload's live `id` fields — 64 ids, none missing from the manifest):
  build 05 → **74 orphans of 142 declared** (the 33 review-9 records + 5
  bridges carried only as edge ids + 15 D2 ids + 21 artifact-meta ids);
  build 07 → **41 orphans**, i.e. **every D3 payload record that review-9
  scoped is now carried**; links grew 50 → **83** (+33 = the 33 per-record
  links, dotted `A-02#<collection>.<record>` form, which also sidesteps
  F9-1 as the reviewer prescribed).
- **Validators on build 07** (all 23:56): handoff gate `fields=16/16
  glossary-entries=20 findings=0` exit 0; `packet_links.py --packet …-07.yml
  --repo-root .` → `links=83 resolved=83 findings=0` exit 0 **with live
  digest re-measurement — the v2-05 harness self-pin mismatch cleared**
  (build 07 re-pins the fixed tool's bytes); `packet_uncertainty.py --packet
  …-07.yml` → `claims=15 findings=0` exit 0.
- **Deviation/interpretation note (for the parent):** design §3.2 rule 4
  reads "≥1 claim link or edge target". In build 07 the five bridge records
  BR01–BR05 ride as coupling-edge **row ids** (the BR01–BR05 edges whose
  `source` is S01/S02), and O03's census counts edge `source`/`edge_id` as
  carriage; the packet discloses all 8 edge-only-carried ids by name in its
  §validation receipt. Under a strictly literal link-or-target reading, 5
  bridge records (plus the 15 D2 and 21 meta ids, which were never in F9-2's
  delivered-D3 scope) stay uncarried. The F9-2 finding as written
  (lexemes/names/materials/objects/utterances) is **closed with margin**;
  the bridge edge-id carriage is an interpretation, disclosed, not a silent
  gap. **Control 3: PASS** (coverage completed; no owner-note needed for
  the F9-2 scope itself).

## 4. Regression — battery + craft + validators + frozen-verify

All commands 2026-10-17 23:33 (pre-fix baseline) and re-run 23:46–23:58
(post-fix, final bytes) from the lane root, `TMPDIR=$PWD/.scratch`:

| check | command | post-fix result |
|---|---|---|
| gate battery (7 selftests + baselines + tree preservation) | `python3 tools/check-gate-battery.py` | exit **0** |
| craft tamper selftest | `python3 tools/check-craft-exercise.py --selftest` | exit **0** (`SELFTEST OK 10/10` + `CLI-SELFTEST OK 18/18`) |
| craft positive | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | exit **0** |
| uncertainty selftest | `python3 tools/harness/packet_uncertainty.py --selftest` | **19 checks passed**, exit 0 (unchanged, green) |
| links selftest | `python3 tools/harness/packet_links.py --selftest` | **38 checks passed** (31 → 38: +4 edge-source, +4 anchor, count line now computed), exit 0 |
| replay-frozen selftest | `python3 tools/replay-frozen.py --selftest` | exit **0** |
| round-15 frozen-verify selftest | `python3 reports/round-15/handoff/frozen-verify.py --selftest` | exit **0** |
| round-15 frozen baseline verify | `python3 reports/round-15/handoff/frozen-verify.py` (default baseline) | exit 0 — baseline integrity digest recomputes to its recorded `ab0ff238…` under the tool's canonicalization (`json.dumps(…, sort_keys=True, indent=1)`), re-derived 23:59 |
| round-16 frozen baseline verify (late-landing artifact) | `python3 reports/round-15/handoff/frozen-verify.py --baseline reports/round-16/handoff/expected-v2-07.json` | **exit 2 — `V2F-BASELINE: baseline integrity digest mismatch`** (23:58 and 00:01; bytes stable since mtime 23:55:28). Recomputed digest of the baseline body under the tool's canonicalization (`indent=1`) = `7e68d9fe893faec7a5e97128dd21ccfd7327f20be763198ca43226126f3eae33`, recorded `baseline_digest` = `e023e752d315a4bd76e61e6e8ba05b6e3ee0fb156dc11579420c8e400d0b6d0e` — which this seat reproduced exactly under `json.dumps(body, ensure_ascii=False, sort_keys=True)` with **no indent** (00:07). Recipe divergence, not tampering — see §5(e) |
| round-15 runner selftest | `python3 reports/round-15/run-validation.py --selftest` | exit **0** (37/37 controls per its receipt) |
| stamped packet re-run | `packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .` | `links=50 resolved=50`, exit 1 with exactly one finding: `M-DIGEST-MISMATCH [tools/harness/packet_links.py]` — the documented self-pin interaction, clears on build 07 (verified §3) |
| filed-packet validators unchanged | `packet_uncertainty.py --packet …-05.yml` / `handoff-packet-check.py …-05.md` | `claims=15 findings=0` / `16/16 + 20 findings=0` |

## 5. Verdict and handback notes

- **All three fixer controls re-verified independently: PASS.** The
  round-16 O-claim's fix layer (F10-1, F9-1, F9-2) is control-complete on
  the bytes pinned above; selftests grew (31→38) and stay green; the gate
  is 16/16 + 20/20 with zero findings on the amended packet, whose digest
  pins match live bytes. The one **red** item this seat found in the O
  chain is the freeze leg, §5(e): the round-16 frozen baseline does not
  verify against the landed freeze/verify tool.
- **Residuals for the parent (no action forced by this seat):** (a) the
  bridge edge-id carriage interpretation in §3 — accept as disclosed or ask
  O-packet for literal target links; (b) `packet_uncertainty.py` did not
  grow in round 16 (19 checks, unchanged since round 15) — the claim
  sentence "packet_uncertainty + packet_links selftests grow and stay
  green" is satisfied by links growing and both staying green; a strict
  both-must-grow reading is unmet (the O03 receipt confirms the module's
  bytes are unchanged round-15 `cdcc1931…`); (c) the O03 seat's coverage
  receipts live in `packet-v2-07.md` §validation (lines 168–169),
  `fixes/orphan-census.py`, and `fixes/link-coverage.md` (landed 00:05,
  after this seat's first sweep at 23:59); (d) this seat did not audit the
  C-claim civ map (`reports/round-16/civ/` + `civ-map.json`, map-auditor's
  lane) and did not run the round counting command
  (`reports/round-16/run-validation.py`, validation seat's — see (f)).
- **(e) Round-16 frozen baseline fails the landed verifier's integrity
  check — recipe divergence, pinned (found 23:58/00:01, bytes stable since
  23:55:28):** `expected-v2-07.json` (frozen_by "R16-O03 … keyed build 07
  re-pin of round-15…"; its receipt
  `reports/round-16/fixes/link-coverage.md` §4 landed 00:05 and states the
  recipe as "sha256 over the canonical sort-keys JSON of the payload minus
  the digest key"). This seat recomputed the recorded `baseline_digest
  e023e752…` **exactly** under `json.dumps(body, ensure_ascii=False,
  sort_keys=True)` — no `indent` — while the landed round-15
  `frozen-verify.py:baseline_digest()` uses `indent=1`, which yields
  `7e68d9fe…`. So the baseline **content is intact under the seat's
  recipe** (no post-freeze edit: bytes stable, recipe reproduces), but the
  freeze/verify pair is mismatched and `frozen-verify.py` will exit 2 on
  this baseline every time — the freeze leg cannot read green as landed.
  Required before the O claim's frozen-baseline leg can read green: the
  owning seat re-freezes with the landed tool's canonicalization (or an
  owner amends the tool's `baseline_digest` recipe, with its selftest
  re-run), then the parent re-runs `--baseline
  reports/round-16/handoff/expected-v2-07.json` expecting exit 0. Until
  then the round-16 freeze step is **red, could-not-evaluate** — recorded
  as an open item, not repaired in place by this seat. Corroborating
  receipt note: the O03 battery table (§4) froze the baseline itself but
  never shows a `frozen-verify.py` re-verify run against it — the missing
  step this seat's probe closed.
- **(f) Validation receipt is stale relative to late landings:**
  `reports/round-16/validation.json` was written 23:53:59, **before** the
  amended packet finished landing (23:55), the frozen baseline (23:55:28)
  and the runner's own last edit (23:58:20); its current body shows claim C
  failing on civ-map rows lacking dated commands while
  `reports/round-16/civ-map.json` was still untracked-and-growing, and its
  two claim-O failures are the validator's own fixture-authoring defects
  (diagnosed in `fixes/link-coverage.md` §7 and consistent with this seat's
  independently built fixtures, whose malformed-source edge emitted exactly
  `E-SOURCE-UNKNOWN` alone). Per the round-15 precedent ("integrator acts:
  settled-tree validation rerun on late-landing artifacts"), the parent
  must re-run `python3 reports/round-16/run-validation.py` on the settled
  tree before recording any round-16 verdict; this seat did not run it
  (outside write scope).
- Scratch evidence kept for the parent: `.scratch/r16-verify/`
  (`run-fixtures.py`, `fixture-f10-1.json`, `fixture-f9-1.json`,
  `orphan-census.py`, `packet_links_head.py`). Safe to prune after
  integration.
