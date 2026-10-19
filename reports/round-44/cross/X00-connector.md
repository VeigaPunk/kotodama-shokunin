# X00 — cross-claim connector

- Seat: X00 | role connector | claim cross | round 44 | date 2026-10-19
- Baseline: `c9f4eaa` (`git log --oneline -1`; `git status --porcelain` → `?? reports/round-44/` only)
- Out path: `reports/round-44/cross/X00-connector.md` (the only repo write)
- Mission (`reports/round-44/targets.json:17`): how O's census-artifact denominator (223 vs 224)
  orders against C's landing; how Ca's freshness gate would have caught r43's O and C; the
  single census-artifact name.
- Method: read-only commands at `c9f4eaa`, plus an extracted copy of the O09 body and copied
  corpus trees under `.scratch/` (`TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`). No filed
  byte edited, no corpus staging, no `run-validation.py` executed, no git/network mutation.

## 0. Axes named (godspeed)

| axis | what it means for this seat | move |
|---|---|---|
| A1 denominator ordering | O's four-class identity is only provable at 223; C lands 224 | bind the measurement order + post-C delta rule |
| A2 retrospective freshness | the Ca gate must mechanically falsify r43 O and C without false-flagging Ca | give typed probes with measured outputs |
| A3 artifact identity | one name, one schema, no rival JSON, no round-43 header leaking into r44 | name `reports/round-44/calib/couples-census-r44.json` |

## 1. O's census denominator vs C's landing (A1)

### 1.1 The two live states, measured

At the round baseline the tree has **223** entries:

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for d in corpus/knowledge/*/; do printf '%s ' "$d"; find "$d" -name '*.md' | wc -l; done
corpus/knowledge/civilizations/ 94
corpus/knowledge/culture-material/ 25
corpus/knowledge/linguistics/ 25
corpus/knowledge/myth-symbol/ 26
corpus/knowledge/synthesis/ 29
corpus/knowledge/verification/ 24
```

The r43 O09 successor body was extracted byte-for-byte from
`reports/round-43/op/O09-scribe.md:356-870` and reproduces the claim's digest:

```
$ sha256sum .scratch/x00/tools/harness/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  ...
$ python3 -B .scratch/x00-live/tools/harness/basename-couples-resolver.py --selftest
...
SELFTEST OK: 27/27 controls        (rc=0)
$ python3 -B .scratch/x00-live/tools/harness/basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct): ...
```

This is exactly the claim's `2556 + 166 + 0 + 7 = 2729` plus the one quarantined glob
artifact (`reports/round-44/claims.json:26-28`), and it matches O09's own print at
`reports/round-43/op/O09-scribe.md:226-229`. The r42 extractor, read-only, agrees on the
denominator through its six-class vocabulary:

```
$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 [...]
  misaligned: none        (rc=0)
```

`2 unresolved + 5 prospective = 7`, so the two tools' totals reconcile at the same 223-entry
state; the class vocabulary, not the token count, differs (the parity receipt's job).

### 1.2 Root-sensitivity trap — the census is not portable to a corpus-only tree

A copy of `corpus/knowledge` alone (223 entries) under a clean `.scratch` root does **not**
reproduce 2556/7. Measured:

```
corpus-only scratch root : direct=2536  fallback=166  ambiguous=0  unresolved=27   (entries=223)
mirrored scratch root    : direct=2556  fallback=166  ambiguous=0  unresolved=7    (entries=223)
```

The 20-token difference is entirely refs that resolve only against the **lane root**:
`AGENTS.md` (11 rows), `SKILL.md` (2), `LOG.md` (1), `corpus/README.md` (2),
`SCORECARD.md` (1), `reports/round-20/readme/{gaps,reconcile,verify}.md` (3).
These are `direct` under `classify()`'s Tier-1 `LANE` base
(`reports/round-43/op/O09-scribe.md:499-507`) but absent from a corpus-only copy, so they fall
to `unresolved`. The selftest does **not** catch this: S9 checks only conservation
(`:782`) and S10 checks only arity (`:787`); S1b checks identity only for the one wrapped live
field (`:684`). A 2536/27 run is selftest-green but is the wrong census.

Binding consequence: O02/O06/O10 must run the census either **in-tree before C lands**, or in a
scratch root that mirrors the eight non-`corpus/knowledge` targets above. "Clean .scratch dir"
alone is insufficient. This is a measurement-environment constraint, not a defect in the O09
body.

### 1.3 Binding ordering rule

1. **File the census at 223, before C's bytes move.** The artifact's identity is
   `entries=223 ∧ refs=2730 ∧ direct=2556 ∧ fallback=166 ∧ ambiguous=0 ∧ unresolved=7 ∧
   glob=1`. This identity is only provable at `c9f4eaa`; after C lands the 2729 predicate no
   longer describes the tree.
2. **C is a later corpus delta, not part of O's census.** If the new entry's couples block has
   `N = |field_refs(new entry)|` distinct brace-expanded tokens, the post-C state must read
   `entries=224 ∧ refs=2730+N ∧ conservation=true`, with the four-class fold gaining exactly
   those `N` tokens. `field_refs()` dedupes per entry (`O09-scribe.md:474-481`), so `N` is a
   distinct-token count, not an occurrence count.
3. **Do not regenerate the artifact at 224 to "fix" the entries header.** That silently
   absorbs C's tokens under a heading that claims 2729 and makes the claim's threshold
   unprovable. The artifact's `state_note` must say
   `"pre-C-landing; measurement commit c9f4eaa; entries 223; claim C lands 224 as a later delta"`.
4. **The post-C re-run is C's evidence, not a second census artifact.** Record it as
   `post_landing_check: {entries: 224, refs: 2730+N, delta_refs: N, conservation: true}` inside
   the same JSON (or in C05/C03's audit, citing the same artifact). No second census JSON name.
5. **If C lands first anyway**, measure the artifact from a pristine `git archive c9f4eaa
   corpus/knowledge` tree plus the eight root targets, and name `measured_root` in the artifact.
   Never run `--census` on a 224 tree and label it 223.

The C landing itself is the only corpus delta allowed in r44 (`claims.json:60-68`), so
`2730+N` is the complete post-round expectation; no other entry may move.

### 1.4 README is not the denominator

`corpus/README.md:544` reads `Total knowledge entries: 223` (true) and the footer vector at
`:548` reads `25/26/25/29/24/94` (sums 223, true). The rev-2.4 header at `:11` still carries
the stale vector `25/23/26/25/24/94` (sums **217**) — the pre-existing prose-vector defect C02
was told to repair. The census counts files by glob, never README rows, so this defect cannot
contaminate O; but C's rev 2.5 edit must not propagate 217, and the post-landing sweep must be
`224 == 224` (`reports/round-28/readme/sweep.py`), with the partition vector repaired to the
live `25/26/25/29/24/94` plus C's partition increment.

### 1.5 Tool-emit `round=43` — a wrapper, not an edit

The O09 body hardcodes `payload["round"] = 43` (`reports/round-43/op/O09-scribe.md:816`).
The claim requires the body landed byte-exact (sha `43ce341f…`). Therefore the r44 artifact
must carry the filing round in a **wrapper** and leave the tool's emit untouched:

```
artifact.round = 44
artifact.tool_emit_round = 43          # value printed by the byte-exact tool
artifact.tool_emit.schema = "kotodama-couples-census-v3"
artifact.tool_sha256 = 43ce341f...
```

Do not rewrite the `round` key in the captured JSON; O10's rule is not to hand-enter values
the tool did not print, and a rewritten key would break the `tool_sha256` self-hash contract
(the tool hashes its own file, `O09-scribe.md:817-819`).

## 2. How Ca's freshness gate catches r43 O and C (A2)

### 2.1 Contract: typed probes, three statuses, refusal is not a pass

A gate cannot parse arbitrary English `before` prose. The durable contract should be:

- Each claim carries a probe list (in `claims.json` for future rounds, or a sidecar for filed
  rounds). Each probe asserts one premise of the `before`: `absent | present | count_eq |
  sha256_eq`, evaluated with `git ls-tree` / `git show` at the claim's own
  `baseline_commit`, never against the worktree.
- Per claim: `stale` if any probe mismatches; `fresh` if all match; `unverifiable` if the claim
  has no probes.
- Exit 0 only when every claim is `fresh`. `stale` or `unverifiable` → exit 1. Usage/IO → exit 2.
- `unverifiable` must **not** pass: a prose-only claim that the gate cannot check is not
  fresh. This is the anti-theater line X01 will probe.

The r43 claims file was untracked at `7ceff59` (`git cat-file -e 7ceff59:reports/round-43/claims.json`
→ absent; it was committed at `c9f4eaa`). So the gate must read the claims JSON from the
worktree and probe at the `baseline_commit` recorded inside it — exactly the r43 regression
shape.

### 2.2 r43 O — falsified at `7ceff59` by three independent probes

`reports/round-43/claims.json:27` asserts "no durable instrument", "only resolver in
`.scratch`", and "wrapped field reads 0/4". Measured at the r43 baseline:

```
$ git ls-tree --name-only 7ceff59 tools/harness/ | grep couples
tools/harness/couples-reference-extractor.py
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ git diff --stat 7ceff59 c9f4eaa -- corpus tools
(empty)
$ python3 -B tools/harness/couples-reference-extractor.py --selftest   # same bytes as 7ceff59
PASS wrapped positive 4/4 tokens [...]
... rc=0
$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
```

Probe `O-p1 {assert: "absent", path: "tools/harness/couples-reference-extractor.py"}` →
actual present → **STALE**, falsified by the tracked N6 successor. Probe `O-p2 {assert:
"count_eq", target: "wrapped live field tokens", expected: 0}` → actual 4/4 → **STALE**.
The `git diff` emptiness proves the HEAD run is valid evidence for `7ceff59`. This is the
same finding R01 recorded at `reports/round-43/review/R01-review.md:400` and the r43
validation at `reports/round-43/validation.json:45,52`.

### 2.3 r43 C — falsified at `7ceff59`

`reports/round-43/claims.json:40` asserts "lithic slot named but unbuilt". Measured:

```
$ git cat-file -e 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md && echo EXISTS
EXISTS
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -
$ git ls-tree --name-only 7ceff59 corpus/knowledge/myth-symbol/ | wc -l
26
```

Probe `C-p1 {assert: "absent", path: "corpus/knowledge/myth-symbol/mineral-stone-symbolism.md"}`
→ actual present → **STALE**. The `total 223` half of the sentence was true; the ownership
half was false. The gate flags the claim, which is the correct outcome: a `before` is a
conjunction and one false conjunct makes the premise stale. This matches
`reports/round-43/validation.json:13,18`.

### 2.4 Negative control — r43 Ca must not be flagged

`reports/round-43/claims.json:53` asserts that no per-finding disposition record exists.
Probe `Ca-p1 {assert: "absent", path: "reports/round-43/calib/dispositions-r38-r39.json"}`:

```
$ git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json
fatal: path '...' exists on disk, but not in '7ceff59'
```

Actual absent → premise true → **FRESH**, not flagged. This is the negative control: the gate
distinguishes a true `before` from the two stale ones.

r44's own claims also produce true baseline probes:
`tools/harness/basename-couples-resolver.py` absent at `c9f4eaa` (O's "no four-class
authority" holds), `tools/harness/claims-freshness.py` absent at `c9f4eaa` (Ca's "no
mechanical check" holds), and `find corpus/knowledge -name '*.md' | wc -l` = 223 (C's
denominator holds). C's ownership clause remains `to-verify` until K02/K04 name the gap; the
gate should report C `partial`/`unverifiable` on that conjunct, not `fresh`.

### 2.5 What this closes, and what it does not

R01-43-12 (`reports/round-43/review/R01-review.md:400`) is closed when the gate refuses the
two stale `before` lines at dispatch, before they can enter `LOG.md`/`SHONEN.md`. It does
**not** retroactively validate r43: the r43 claims remain rejected at `c9f4eaa`. The demo
files should be one probe sidecar (recommended:
`reports/round-44/calib/freshness-probes-r43.json`) plus the run output; Ca01/Ca02 own the
final names and must not file two competing sidecars.

## 3. The single census artifact name (A3)

**`reports/round-44/calib/couples-census-r44.json`**

- Collision check: `git cat-file -e c9f4eaa:reports/round-44/calib/couples-census-r44.json`
  → absent; `reports/round-44/calib/` is empty on disk at this cut; the two rival names
  (`couples-census.json`, `basename-couples-census.json`) are also absent. No existing entry
  or filed artifact is overwritten.
- Precedent: r42 filed one JSON with a wrapper schema, `round`, `baseline_commit`, `figures`,
  `rules`, `evidence` (`reports/round-42/op/couples-census-corrected.json`). The r43 F4
  conflict (`reports/round-43/op/O09-scribe.md:122-130`) resolved to **one** name; r44 must
  not repeat two JSONs.
- The artifact is JSON only. A human `.md` summary is optional but, if filed, uses the same
  basename and is not a second JSON. The claim says "ONE census artifact"
  (`reports/round-44/claims.json:28`), so the conservative reading is JSON only.

Required header in the artifact:

```json
{
  "schema": "kotodama-couples-census-artifact-v1",
  "round": 44,
  "date": "2026-10-19",
  "baseline_commit": "c9f4eaa",
  "state_note": "pre-C-landing; measurement commit c9f4eaa; entries 223; claim C lands 224 as a later delta",
  "measured_root": "<in-tree lane root | .scratch mirror path>",
  "entries": 223,
  "refs": 2730,
  "four_class": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 7},
  "artifacts": {"glob-fragment": 1},
  "conservation": true,
  "fallback_mappings_distinct": 50,
  "tool": "tools/harness/basename-couples-resolver.py",
  "tool_sha256": "43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64",
  "tool_emit_round": 43,
  "tool_emit": { "...": "verbatim --census --json output, round key untouched" },
  "post_landing_check": {"entries": 224, "refs": 2730, "delta_refs": 0, "conservation": true}
}
```

The `post_landing_check` numbers are placeholders until C's `N` is measured (the example shows
the `N=0` case, lawful only if the new entry's couples block names no `.md` token). The
integrator fills them from the post-C re-run; the pre-C identity fields are never rewritten.

## 4. Integration order (single sequence the parent can follow)

1. Land the O09 body byte-exact at `tools/harness/basename-couples-resolver.py`
   (0644, sha `43ce341f…`); leave `tools/harness/couples-reference-extractor.py` at
   `d8d23a26…` untouched.
2. `python3 tools/harness/basename-couples-resolver.py --selftest` → 27/27 in-tree.
3. Run `--census --json` **before** C's bytes move (in-tree, or mirrored root per §1.2); file
   `reports/round-44/calib/couples-census-r44.json` with the §3 header and verbatim emit.
4. File O04's witness-demotion note and O07's parity receipt (r42 extractor = N6 witness,
   both runs, differences solely subclass separation).
5. Apply C's single entry + README rev 2.5 (224, vector repaired, sweep green 224==224).
6. Post-C check: `entries=224`, `refs=2730+N`, `delta_refs == N`, conservation true; record it
   in the same artifact's `post_landing_check` and in C05/C03's audit. Do not file a second
   census JSON.
7. File Ca's gate + r43 regression demo; admit no claim whose status is `stale` or
   `unverifiable`.

Steps 1-3 are order-binding against step 5. Steps 4 and 7 are independent and can run in
parallel.

## 5. Handoffs and open items

| owner | item |
|---|---|
| O02 | scratch root must mirror the eight lane-root targets in §1.2 or the census reads 2536/27; run in-tree if C has not landed |
| O06 | wrapper schema/§3 header; `state_note`; `tool_emit_round: 43`; one JSON name |
| O10 | re-derive 2556+166+0+7+1=2730 from the verbatim emit; confirm `post_landing_check` delta = new entry's distinct tokens |
| O07 | parity receipt must explain 2+5 (r42 six-class) vs 7 (r44 four-class) at the same 223/2730 denominator |
| C05/C03 | post-C `entries=224`, `delta_refs=N`, no other file changed; collision check before bytes move |
| Ca01/Ca02 | typed probes, `unverifiable` refusal, r43 positive regression (O,C) + Ca negative control; one sidecar |
| integrator | apply order §4; never run `run-validation.py` in-tree; no corpus staging by seats |

Open / `to-verify`:
- `N` (C's couples-token contribution) is unknown until C01's draft lands; the post-C numbers
  beyond `entries=224` are formulae, not measurements.
- C's "genuinely unowned" conjunct is `to-verify` until K02/K04's fresh absence sweep names
  the gap; the freshness gate cannot certify it from the current claims text alone.
- The O09 body's `--census` counts non-corpus refs (`AGENTS.md`, `SKILL.md`, `LOG.md`,
  `SCORECARD.md`, `corpus/README.md`, `reports/round-20/readme/*.md`) as `direct` by design of
  Tier-1 base `LANE`. That is the measured 2556, not an error; anyone reproducing the census
  must reproduce the same root, or the denominator drifts by 20.

## 6. Evidence command log (condensed)

```
find corpus/knowledge -name '*.md' | wc -l                                  -> 223
for d in corpus/knowledge/*/; do find "$d" -name '*.md' | wc -l; done       -> 94 25 25 26 29 24
sha256sum .scratch/x00/tools/harness/basename-couples-resolver.py           -> 43ce341f...5ad64
python3 -B .scratch/x00/tools/harness/basename-couples-resolver.py --selftest -> 27/27, rc=0
python3 -B .scratch/x00-live/tools/harness/basename-couples-resolver.py --census -> 223/2730, 2556/166/0/7, glob=1
python3 -B .scratch/x00/tools/harness/basename-couples-resolver.py --census (corpus-only root) -> 2536/166/0/27
python3 -B tools/harness/couples-reference-extractor.py --selftest          -> 8/8 PASS, rc=0
python3 -B tools/harness/couples-reference-extractor.py --census            -> 223/2730, 2556/166/2/5/1
git ls-tree --name-only 7ceff59 tools/harness/ | grep couples              -> couples-reference-extractor.py
git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum  -> d8d23a26...
git cat-file -e 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md -> EXISTS
git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum -> c99f44ca...
git ls-tree --name-only 7ceff59 corpus/knowledge/myth-symbol/ | wc -l      -> 26
git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json    -> absent in rev
git diff --stat 7ceff59 c9f4eaa -- corpus tools                             -> empty
git cat-file -e c9f4eaa:reports/round-44/calib/couples-census-r44.json      -> absent
git status --porcelain                                                      -> ?? reports/round-44/
```
