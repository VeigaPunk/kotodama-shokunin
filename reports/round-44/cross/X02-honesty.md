# X02 — Honesty critic ledger (round 44)

- Seat: `X02` (critic, claim `cross`)
- Baseline commit: `c9f4eaa`
- Audit cut: `2026-10-19T17:21:38Z` (UTC), round-44 working tree
- Method: every headline number was re-measured from primary sources; each row below
  names the command actually run and its captured output. A claim's *embedded number*
  being true is recorded separately from the claim being *delivered* — at this cut most
  seat artifacts did not exist, so delivery is marked `unmeasured`, never assumed.

Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

---

## 1. Measured ledger — claim O

Extraction (reproducible; the `.scratch` copy is disposable, the digest is the record):

```bash
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/x02-home/basename-couples-resolver.py
wc -l .scratch/x02-home/basename-couples-resolver.py   # 515
sha256sum .scratch/x02-home/basename-couples-resolver.py
# 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
```

Fence boundaries confirmed: `grep -n '^````' reports/round-43/op/O09-scribe.md` →
`355:````python` opener, `871:```` ` closer; body is exactly 356–870, 515 lines.

| # | Assertion (source) | Measurement | Verdict |
|---|---|---|---|
| O-1 | body sha256 `43ce341f…` (claims.json O) | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` | **measured true** |
| O-2 | `--selftest` 27/27 green (claims.json O thresholds) | `SELFTEST OK: 27/27 controls`, exit 0; all 27 PASS lines captured, including S1b wrapped 4/4, S3a–c ambiguous, S7c blank-line+indented prose, S8b glob-precedence, S4a wrapped-identity | **measured true** |
| O-3 | census `entries=223 refs=2730` (claims.json O, O06) | `entries=223 refs=2730` | **measured true** |
| O-4 | four-class `2556+166+0+7=2729` (claims.json O) | `direct=2556 fallback=166 ambiguous=0 unresolved=7`; sum 2729 | **measured true** |
| O-5 | `+1 glob artifact` → 2730 (claims.json O) | `artifacts (excluded from the four-class totals): glob-fragment=1`; `conservation: True (sum=2730 refs=2730)` | **measured true** |
| O-6 | 50 distinct fallback mappings (O06 mission) | census header says `fallback mappings (50 distinct)`; independent row recount `sed -n '6,56p' census.out \| grep -c '^    '` → **50** | **measured true** |
| O-7 | 7 unresolved rows, each reasoned (claims.json O/O06) | 7 rows; reasons `declared-prospective-seed` ×5 and `dangling-reference` ×2; no blank reason | **measured true** |
| O-8 | ambiguous = 0 (claims.json O) | `ambiguous (0 rows):` | **measured true** |
| O-9 | wrapped field reads 4/4 by identity, field at `phonetics-phonology.md:72-77` | field spans lines 72–77; tokens `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md` (selftest S1b and S10 pass; r42 witness independently prints the same four) | **measured true** |
| O-10 | r42 extractor bytes unchanged, digest `d8d23a26…` | `sha256sum tools/harness/couples-reference-extractor.py` → `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`; identical at `7ceff59` (`git show 7ceff59:…`) and at `c9f4eaa` | **measured true** |
| O-11 | r42 six-class census `2556/166/2/5/1` (claims.json O `before`) | `entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1`, exit 0 | **measured true** |
| O-12 | successor lands at `tools/harness/basename-couples-resolver.py` (claims.json O `after_required`) | `ls tools/harness/` at this cut → **absent** | **unmeasured / not yet delivered** |
| O-13 | ONE census artifact filed at `reports/round-44/calib/` | `ls -la reports/round-44/calib` → empty (dir exists, 0 files) | **unmeasured / not yet delivered** |
| O-14 | O07 parity receipt filed | `reports/round-44/op/` does not exist at this cut | **unmeasured / not yet delivered** |

Independent parity fold, pre-computed from the two measured runs (this is the *only*
difference a correct parity receipt may show):

```
r42 witness : direct 2556 | fallback 166 | unresolved 2 + prospective 5 | glob 1 = 2730
successor   : direct 2556 | fallback 166 | ambiguous 0 | unresolved 7        | glob 1 = 2730
expected map: direct->direct, fallback->fallback, (unresolved+prospective)->unresolved, glob->glob
```

If O07's receipt reports any other delta, that difference is **unexplained** and must
block O.

## 2. Measured ledger — claim C

| # | Assertion (source) | Measurement | Verdict |
|---|---|---|---|
| C-1 | total 223 (claims.json C `before`) | `find corpus/knowledge -name '*.md' \| wc -l` → `223` | **measured true** |
| C-2 | README sweep green at 223 row/file parity (README rev 2.4) | `python3 -B reports/round-28/readme/sweep.py` → `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_ok True`, `footer_ok True`, exit 0 | **measured true** |
| C-3 | README revision 2.4, footer vector `25/26/25/29/24/94` | sweep output order `linguistics, myth-symbol, culture-material, synthesis, verification, civilizations` = `25/26/25/29/24/94`, sum 223; `readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | **measured true** |
| C-4 | pre-existing rev-2.4 prose-vector defect sums 217 (C02 mission) | revision line reads vector `25/23/25/29/24/94 → 25/23/26/25/24/94`; `25+23+26+25+24+94 = **217**`, while the footer sums 223. The prose vector is wrong; the footer is right. | **measured true (defect confirmed)** |
| C-5 | a fresh sweep names a genuinely unowned gap (claims.json C) | no scout output exists at this cut (`reports/round-44/scout/` empty) | **unmeasured** |
| C-6 | total 223 → 224; sweep green 224==224 | total is 223 at this cut; no landing applied | **unmeasured / not yet delivered** |
| C-7 | one new entry, no overwrite, audits PASS | no `reports/round-44/cov/` file exists at this cut | **unmeasured / not yet delivered** |

Note for C-4: if rev 2.5's prose repeats the rev-2.4 vector style without re-summing,
the defect multiplies. The C02 draft must show its arithmetic, not merely state 224.

## 3. Measured ledger — claim Ca (r43 stale-premises regression)

The r43 `before` lines are the regression fixture. Measured at the r43 baseline
`7ceff59` (both probes read committed bytes, not the working tree):

```bash
git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'        # 223
git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | grep -c '\.md$'  # 26
git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol/ | grep -i 'mineral\|stone\|lithic'
# corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
# d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
```

| # | r43 premise | Measured at `7ceff59` | Verdict |
|---|---|---|---|
| Ca-1 | r43 O `before`: "no durable instrument implements the r39 basename-couples policy; the only resolver that ever ran … lives in ephemeral `.scratch`" | A durable instrument existed: `tools/harness/couples-reference-extractor.py`, digest `d8d23a26…`, `--selftest` exit 0, census over all 223 entries / 2730 refs. The absence framing is false. | **stale confirmed** |
| Ca-2 | r43 O narrower remainder: four-class report + disposition leg + ambiguous/indented-prose controls absent | r42 selftest has **no ambiguous control**; its over-capture fixture (`couples-reference-extractor.py:231-241`) puts the prose at column 0, so blank-line + *indented* prose is untested; census lists no fallback mappings and no per-token reasons. | **true remainder** (the defect was hardening, not blank slate) |
| Ca-3 | r43 C `before`: "myth-symbol 26 … the lithic slot named but unbuilt" | myth-symbol = 26 and total = 223 are true; but `mineral-stone-symbolism.md` already existed at `7ceff59` (its own `- topic:` is "the lithic register …", and its `- gap filled:` paragraph claims the slot). The ownership premise is false. | **stale confirmed (counts true, ownership false)** |
| Ca-4 | a durability gate exists that refuses a stale `before` | `ls tools/harness/ \| grep -i 'fresh\|claim'` → no match; `reports/round-44/calib/` empty | **unmeasured / not yet delivered** |
| Ca-5 | positive regression: gate flags r43 O and C | no run exists | **unmeasured** |
| Ca-6 | negative control: gate does not flag a true `before` | no control exists | **unmeasured** |

## 4. Wording and precision flags

1. **"confirmed blank-line over-capture"** (claims.json O `before`): the *code* fact is
   confirmed at `tools/harness/couples-reference-extractor.py:64-65`
   (`if not following.strip(): continue`). But no live token moves: both censuses cover
   the same 2730 refs with identical `direct=2556` and `fallback=166`. The honest
   description is **latent over-capture trap, confirmed by code and by synthetic
   control**, not a measured live miscount. The r44 claim's wording is defensible but
   must not be upgraded to "live data was wrong".
2. **"the r42 selftest lacked an indented-prose control"**: verified in the stronger
   form — the r42 fixture's prose is unindented, so it exercises only the `break` path,
   not the blank-line `continue` then `INDENT_RE` path. The successor's S7c control is
   genuinely new.
3. **No "should work" wording found** in the round's filed contract:
   `grep -rniE 'should work|should be|might|presumably|obviously|expected to|assume'
   reports/round-44/` returns only the X02 mission text itself (which quotes the phrase
   as the thing to hunt). This is a clean scan at this cut, not a guarantee for
   seat outputs filed later; the integrator must re-run it at close.
4. **Ca "refuses to file"**: a gate that only greps prose the claim author supplied can
   be theater. Acceptance must include an actual non-zero exit and a refusal line
   naming the false predicate, plus a predicate the gate derived independently (file
   existence, count, topic ownership) — not merely a string match against the claim's
   own `before`.
5. **O "ONE census artifact"**: the artifact must carry the generating command and a
   digest, and its totals must reconcile to the tool's stdout. A hand-written JSON with
   the right totals is indistinguishable from a generated one unless provenance is
   recorded.

## 5. Scope / no-unauthorized-write audit

At the audit cut:

```bash
git status --porcelain                      # ?? reports/round-44/   (only)
git status --porcelain corpus/ | wc -l      # 0
git status --porcelain | grep -vE '^\?\? reports/round-44/?$' | wc -l   # 0
find corpus -newer reports/round-44/claims.json -type f                 # (none)
sha256sum tools/harness/couples-reference-extractor.py                  # d8d23a26…
```

- Nothing staged under `corpus/`; no filed byte changed; no second resolver path
  exists; the r42 witness bytes are untouched.
- Telemetry declaration digests verify: `reports/round-44/claims.json` =
  `5bd54b71…c06e8` and `reports/round-44/targets.json` = `1f73f172…a9501`, matching
  `telemetry/dispatch-declared.json`.
- Caveat: **no seat output existed at this cut** (only integrator scaffolding:
  `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`). The
  no-out-of-path check is therefore provisional; it certifies the scaffolding and the
  baseline, not seats that had not yet written. Re-run at close:
  `git status --porcelain` must show exactly the round-44 out files, `corpus/` must
  stay clean except the single integrator-applied C landing, and every seat file must
  sit under its assigned `out` path from `targets.json`.
- `requested_workers: 32`, `batched_calls: 1` are a declaration, not an observation.
  The declaration itself says observed launches land in `observed-dispatch.json` +
  `availability-close-44.json`; until those exist, observed count/completion/failure
  counters must stay `null`, not inferred.

## 6. Acceptance gates for the integrator (do not admit until each passes)

1. **O landing**: `tools/harness/basename-couples-resolver.py` exists, sha256
   `43ce341f…` (or the O01-preferred bytes with a stated digest), `--selftest` exit 0
   with 27/27, `--census` reproduces `223/2730`, `2556+166+0+7=2729`, `+1 glob`,
   conservation True.
2. **O artifact**: exactly one census artifact under `reports/round-44/calib/`,
   carrying generation command + tool digest + the 50 mappings + 7 reasons; `--json`
   output reconciles to stdout.
3. **O parity**: `tools/harness/couples-reference-extractor.py` digest still
   `d8d23a26…`; the parity receipt's delta is exactly `2 unresolved + 5 prospective →
   7 unresolved`, everything else identical.
4. **C**: fresh sweep output filed with commands; the named gap's topic line matches
   no existing entry; total 224; `readme/sweep.py` green with `rows 224 files 224`;
   footer vector sums 224; the new revision's prose vector is arithmetically checked
   (the rev-2.4 217-vs-223 defect must not recur); zero existing entries changed
   (`git status` shows one added corpus file + README).
5. **Ca**: the gate is durable under `tools/harness/` (not `.scratch`), run over
   `reports/round-43/claims.json` yields a refusal naming **both** O and C with a
   non-zero exit; a negative control with a true `before` exits 0; the demonstration
   output is pasted command output, not a summary.
6. **Honesty re-scan at close**: `grep -rniE 'should work|might|presumably|expected
   to|assume' reports/round-44/` over seat outputs; any hit must be quote-or-delete.

## 7. Bottom line

- **No fabricated number found.** Every numeric assertion embedded in the round-44
  contract that could be measured at this cut reproduced exactly: the O09 digest and
  27/27, the four-class census and its conservation identity, the 50/7/0/1 detail, the
  r42 witness digest and six-class fold, the 223 total and sweep parity, and the
  declared telemetry digests.
- **Claim O is not yet delivered**, though its source body is verified: the authority
  path, census artifact, and parity receipt are absent at this cut.
- **Claims C and Ca are wholly unmeasured at this cut** — no scout, draft, audit, gate,
  or demonstration exists. They must not be described as done or "on track to pass".
- **The r43 stale-premises defect is real and reproduces**: both `before` lines were
  false at `7ceff59`, with the count-only fragments true — exactly the failure mode a
  freshness gate must catch, and a warning that count equality alone is not freshness.

---

## 8. Addendum — audit of seat outputs filed mid-cut (O02, O03, O07)

Three claim-O seat reports appeared after §1–§7 were written. Each was checked against
my own runs; none is accepted on its own say-so. **This supersedes §7's line that the
parity receipt is absent** — O07 filed, and was reproduced. Append-only correction:
the earlier sentence stands as the state at `17:21:38Z`.

### 8.1 Cross-check table

| Number | Seat claim | My reproduction | Verdict |
|---|---|---|---|
| whole-note digest `956d478b…cb341` | O02 §1 | `sha256sum reports/round-43/op/O09-scribe.md` → match | **measured true** |
| body digest `43ce341f…ad64`, 515 lines | O02/O03/O07 | my own `sed -n '356,870p'` extract → same digest, 515 lines | **measured true** |
| selftest 27/27 | O02 §3, O07 §3 | my run → 27 PASS, exit 0; **24 `check()` call sites** confirmed (`grep -c '^[ ]*check('` = 24), S5 runs 4 fixtures → 24−1+4 = 27 | **measured true** |
| `census.out` sha256 `87ef57d5…c7867` | O02 §4.2 | my census from `.scratch/x02-home` (different scratch dir) → **byte-identical**; rerun also identical | **measured true; cross-seat determinism** |
| 25 zero-token entries | O02 §4.3 | `--census --json` recount → 25 of 223 | **measured true** |
| 50 mappings, 166 occurrences | O02/O07 | JSON: 50 distinct; `sum(occurrences)` = 166 = fallback class count; every mapping non-null | **measured true** |
| 8 disposition rows (7 unresolved + 0 ambiguous + 1 glob) | O02 §4.1 | JSON disposition lists: 7/0/1 = 8; every row has a non-empty reason | **measured true** |
| 0 token diffs, 0 fallback mismatches, exact class-pair table | O07 §5 | ran O07's `.scratch/o07-parity/compare.py` myself: 223 entries, 2730 refs, pairs `direct→direct 2556`, `fallback→fallback 166`, `glob→glob 1`, `prospective→unresolved 5`, `unresolved→unresolved 2`, **0 diffs, 0 mismatches**, 25 zero-token | **measured true** |
| shadow `.scratch/o07` corpus has 212 entries | O07 §2 | `find .scratch/o07/corpus/knowledge -name '*.md' \| wc -l` → 212 | **measured true (hazard is real)** |
| live branch order `:134-150`; S3a/S3b `:725-726`; S7c `:768`; S8b `:777`; blank-line logic `422-433` | O03 §2–§5 | direct `sed`/`grep` of both files → all refs real and as described | **measured true** |
| docstring overclaims an unreachable soft-wrap exception | O03 §7.1 | body has `soft_wrap = parts[-1].endswith("-") and not saw_blank`, so after a blank line the documented exception can never fire | **measured true (body-level finding)** |

### 8.2 Flags from the seat reports that must follow the evidence into integration

1. **Docstring overclaim** (O03 §7.1, independently confirmed): the body's prose promises
   a hyphen soft-wrap continuation after a blank line, but the code cannot reach it. No
   live token is affected (0 blank-separated continuations), so this is a
   **successor-record note, not a byte edit** — the body is pinned at `43ce341f…`.
2. **JSON provenance is location- and round-stamped** (O02 §7.2, O03 §7.2): verified —
   my JSON carries `"round": 43` and `"tool": ".scratch/x02-home/basename-couples-resolver.py"`.
   Consequence: JSON digests are path-dependent (mine `c67a24a8…` vs O02's `f53899ea…`
   for otherwise identical content); only stdout is path-independent (`87ef57d5…`). The
   filed artifact must be generated **after** landing and must not silently rewrite
   `round` without recording it as provenance.
3. **Denominator ordering is a real cross-claim dependency** (O03 §7.4): if C lands
   before the O census artifact is generated, the artifact reads 224 entries and cannot
   match the claim's 223 / `2556+166+0+7`. Pin `entries=223` and the measured tree in
   the artifact, or state the order explicitly in the receipt.
4. **O07's observation time is `2026-10-19T14:2xZ`** — not a precise timestamp. The
   final receipt must carry a real observation time (telemetry provenance norm).
5. **O07's harness line `conservation extractor: 2730 == refs True` is a self-comparison**
   (`sum(...) == sum(...)`). The 2730 sum is correct; the equality is vacuous. The real
   conservation check is the tool's own `conservation: True`. Flagged so the phrase is
   not over-read.
6. **Not independently re-derived** (marked `to-verify` as counts, not as conclusions):
   O03's injected-index D2 outputs (scratch driver) and its "19 entries have couples as
   the last header field" count. The code branch order was verified directly, and O07's
   live token diff is 0, so no live conclusion depends on these counts.
7. **Scratch clones are a denominator hazard, not a scope violation.** `.scratch/o07`
   (212 entries) and the `.scratch/r22-*` clones pre-exist and are untracked. O07 caught
   and discarded its 212-entry run — good honesty. Every census must assert
   `KNOW == <repo>/corpus/knowledge`; the default text output does not print the root.

### 8.3 Scope check with seat outputs present

Files in `reports/round-44/` at this addendum: `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json`, `op/O02-verify.md`, `op/O03-defects-verify.md`,
`op/O07-parity.md`, `cross/X02-honesty.md`. Every seat file sits at its assigned
`targets.json` out path. `git status --porcelain corpus/` → 0 lines; the r42 witness digest
is still `d8d23a26…`; the only untracked path is `reports/round-44/`. No seat wrote
outside its out path, and nothing is staged under `corpus/`.

### 8.4 Revised bottom line (O only)

O's support evidence is now **three independently reproduced reports**, not one; the
token-level parity is confirmed by my own run of the diff harness. Still missing for O:
the landed authority path, the single filed census artifact, the O04 demotion record,
O08's negative proof, and O01/O05/O06/O09/O10. **C and Ca remain entirely absent** —
no scout, draft, audit, gate, or demonstration exists, so neither may be described as
done or on track.

---

## 9. Addendum 2 — audit of the next evidence wave (K04, O06, O08, O10, S01, S02)

Filed between `17:22Z` and `17:25Z`; state recorded here as of `17:26Z`. §8.4's absence
list is now partly superseded: O06/O08/O10/O09 and K04 did land. Append-only correction.

### 9.1 Coverage: K04's named gap verified independently

K04 names `corpus/knowledge/myth-symbol/dream-vision-trance.md` (dream / vision / trance
altered-state complex). I re-ran the ownership tests at `c9f4eaa`:

```
$ ls corpus/knowledge/myth-symbol/dream-vision-trance.md      # No such file or directory
$ find corpus/knowledge -type f | grep -iE 'dream|trance|vision|ecsta|shaman|incubat'   # (none)
$ grep -rilE -- '^- topic:.*\b(dream(s|ing|er|t)?|trance|ecsta[a-z]*|shaman[a-z]*|incubat[a-z]*|visionary|vision[ -]quest)\b' corpus/knowledge/*/*.md
corpus/knowledge/civilizations/mongol.md
corpus/knowledge/myth-symbol/divination-omen-systems.md
$ grep -rlEi '\b(dream(s|ing|er|t)?|trance|...)\b' corpus/knowledge/*/*.md | wc -l   # 52
```

- The two topic hits are exactly the adjacent owners K04 discloses: `mongol.md`'s topic is
  a civilization/lexical base ("shamanic vocabulary"), and `divination-omen-systems.md`
  owns the *reading technology* by its own topic line; neither owns the altered-state
  complex. **Unowned-as-system confirmed.**
- Sort insertion confirmed: with `LC_ALL=C sort`, `dream-vision-trance.md` lands at line
  11, between `divination-omen-systems.md` (10) and `eschatology-world-end-systems.md`
  (12). Filename collision: none.
- K04's README refs are real: `corpus/README.md:205` = `## myth-symbol/ (26)`;
  `:544` = `Total knowledge entries: 223.`
- Verdict: **K04's ownership and placement claims are measured true.** But C is still
  **not delivered**: `reports/round-44/cov/` is absent (no C01–C05), total remains 223,
  and the README rev-2.5 edit does not exist. The gap is verified; the +1 is not.
- Cross-claim caveat: K02 (the other gap scout) still has no output. K04 explicitly says
  it could not corroborate K02 and names its own gap. The contract's "confirm K02's gap
  or name a different unowned gap" is satisfied in the second branch; the integrator
  should not pretend two scouts agreed.

### 9.2 O06 census artifact draft — pins reproduce

| Claim | My check | Verdict |
|---|---|---|
| policy sha256 `8c3d7c35…0cdd6` | `sha256sum reports/round-42/calib/basename-couples-policy-full.md` → match | **measured true** |
| corpus fingerprint `7675c724…953ba` over sorted `<path>:<sha256>\n` | recomputed from all 223 files → exact match | **measured true** |
| §5 JSON block sha256 `c0ee791a…40699` | extracted the fenced block; hash of block + trailing newline → exact match | **measured true** |
| `baseline_commit` present in the artifact | `:219` = `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` | **present** (O10's "no baseline_commit" caveat applies to the *tool's* payload, not O06's wrapper) |
| `round: 44` vs body's hardcoded `round: 43` | documented at O06 `:1023-1025` as a wrapper provenance decision; body explicitly not edited | **documented, not silent** |
| `tool.path` = landing path, `tool.run_path` = scratch | both disclosed; run_path is honest about the pre-landing measurement | **disclosed** |

Two integration conditions remain: (a) the artifact names
`tools/harness/basename-couples-resolver.py` although that file **does not exist yet** —
it must be filed only after a byte-exact landing, and its `tool.path` will then be true;
(b) it pins `entries: 223` and a pre-C `state_note`, so C must not land before the census
is generated, or a **new** artifact with 224 is required (never a hand edit). O06 states
both. Its `content_sha256` (`3ee551fc…`) was not independently recomputed (it is defined
over a canonical body minus two fields); the integrator should regenerate it with O06's
`build_artifact.py` rather than trust the literal.

### 9.3 O08 negative proof — manifests reproduce

`sha256sum .scratch/o08/manifest-before.sha256 .scratch/o08/manifest-after.sha256` →
both `3006cd77a57ec77eda1d52022fb2dd7d3b4d9f42c1f1a5143e323014fce4911c`, and `cmp` says
identical. That supports O08's "2,921-file manifest before/after, no write" claim for the
window it measured. O08's N1 (do not follow the r43 `> reports/round-43/calib/...` line),
N2 (do not edit the body's `round: 43`), and N3 (223-before-C ordering) are the same
three hazards I flagged in §8.2 — independent corroboration, not a new claim.

### 9.4 O10 and S01/S02 honesty notes

- **O10** reaches PASS and itself states the key caveat: the tool's `conservation` boolean
  is tautological by construction, so O10's independent policy-derived fold — not the
  boolean — is the evidence that no token was dropped. That matches §8.2 item 5 and is
  the right framing. Its two filing caveats (no `baseline_commit` in the payload;
  hardcoded `round: 43`) are resolved by O06's wrapper, as measured in §9.2.
- **S01** says `NOT ADMITTED at this cut` and correctly records C and Ca as artifact-less;
  it also warns that a free-prose freshness gate is theater. Good. One wording risk:
  "**Claim Ca is executable and this seat has already run its regression shape**" is
  immediately caveated ("the durable gate is still owed"), but the `STALE r43-O / STALE
  r43-C / FRESH r43-Ca` output it reports is a **self-authored scratch probe**, not
  Ca01's deliverable and not the claim's filed demonstration. It must not be cited as
  Ca evidence. The Ca claim remains unmeasured until Ca01 files a durable tool with a
  positive regression and a negative control, and Ca02 independently runs it.
- **S02** keeps `launched_workers`, `completed_workers`, `failed_workers`,
  `runtime_concurrency`, `lane_key`, and `provider_liveness` `null` with owner/reason,
  and states that `requested_workers: 32` is not a launch/completion count. Its
  file-presence observations are labelled `partial-worker-observation` and explicitly
  not evidence of launches. This matches the AGENTS.md telemetry rule; no overclaim found.

### 9.5 Scope at addendum 2

Every seat file now present sits at its assigned `targets.json` out path: `adj/A01-scope.md`,
`cross/X00-connector.md`, `cross/X02-honesty.md`, `op/O02/O03/O06/O07/O08/O09/O10*.md`,
`scout/K01/K04*.md`, `scribe/S01/S02*.md`. `git status --porcelain corpus/` → 0; the only
untracked path is `reports/round-44/`; r42 witness digest still `d8d23a26…`. No
out-of-path write found. Still absent from the declared roster: K02, K03, P01, O01, O04,
O05, C01–C06, Ca01–Ca03, R01–R02, X01, S? (S01/S02 present). Absent is not a pass.

### 9.6 Final honesty position at this cut

- **O**: the body and all its embedded numbers are verified by four independent runs
  (mine, O02, O06's build, O07's diff). The evidence chain is nearly complete. **Not
  delivered**: the landing, the single filed census artifact (O06 is a draft), O04's
  witness-demotion record, O01/O05. O is admissible only after a post-landing re-run.
- **C**: the named gap is independently verified unowned and correctly placed, but no
  entry, audit, collision check, or README edit exists. **Not delivered; +1 is still
  aspirational.**
- **Ca**: no durable gate exists; the only `STALE`/`FRESH` output is S01's scratch probe.
  **Not delivered.**
- **No fabricated number found** in any seat output examined. The recurring risk is
  over-reading draft/scratch evidence as filed evidence; the integrator must apply the
  §6 gates and the §9.4 Ca caveat.

---

## 10. Addendum 3 — O04 filed (correction to §8.4/§9.5/§9.6)

`reports/round-44/op/O04-witness-demotion.md` landed after addendum 2. It is the
witness-demotion record, and its claims check out:

```
$ git ls-files -s tools/harness/couples-reference-extractor.py
100644 1ded489bbb2bb90b3ad883ec0cd052822d870225 0 tools/harness/couples-reference-extractor.py
$ git hash-object tools/harness/couples-reference-extractor.py
1ded489bbb2bb90b3ad883ec0cd052822d870225          # matches O04's tracked-blob claim
$ grep -n 'couples-reference-extractor' <extracted-body>
8:couples-reference-extractor.py (r42, sha256 d8d23a26...), which remains the N6
$ grep -nE 'import .*couples|subprocess|exec\(' <extracted-body>   # NONE
$ sed -n '96p' corpus/lessons/round-28.md    # carries the "filed bytes are read-only;
                                             # correction is a new revision file" precedent
```

O04 correctly frames demotion as a **record-level act, not a byte edit**, and its
single-authority rules W1–W5 (cite the authority only; never import/shell the witness;
pin the witness digest; keep it live as a cross-check; fold `prospective→unresolved`
and treat glob as an artifact) match the contract and my §8.2 findings. Verdict:
**record sound; no byte hazard.** This supersedes the "O04 absent" lines in §8.4, §9.5,
and §9.6. Remaining O holes at this cut: the landing itself, the single filed census
artifact (O06 is a draft under `op/`, `calib/` still empty), O01, and O05. C and Ca are
unchanged: no `cov/` or `calib/` output exists, and S01's scratch probe is still not Ca
evidence.

**Ledger closed at `2026-10-19T17:28Z`.** File digest and scope at close: see the
handoff; any later seat output is outside this audit window and must be checked against
§6 and §9.4 before admission.

---

## 11. Addendum 4 — C01/C05/C06 filed (correction to §9.5/§9.6/§10)

Three claim-C files landed at the cut. Audited:

| File | What it establishes | What it does not |
|---|---|---|
| `cov/C01-entry-draft.md` | Fenced entry draft (lines 108–261) targeting exactly `corpus/knowledge/myth-symbol/dream-vision-trance.md`; header fields present; every in-repo anchor claimed re-read in its self-audit; no corpus staging | Not independently audited (C03/C04 absent); external sources `(to-verify)` by its own statement |
| `cov/C05-collision.md` | PASS at `c9f4eaa` for exactly that slug: absent, no filename siblings, two adjacent topic owners, sort position 11, dry-run delta = 1 `A` + `README.md` `M` | Its own cut predates C01; it says the clearance is conditional on C01 drafting the same slug |
| `cov/C06-scribe.md` | Honest assembly: coverage still **223**, conditional verdict candidates, K02 absent, C03/C04 absent | Authors no entry; its status table is timestamped and now partly stale (C01/C05 have since landed) |

My spot-checks: C01's target path is the same string C05 cleared
(`C01:89`, `C05:10,106`); the heading test reproduces exactly two adjacent hits
(`divination-omen-systems.md:1`, `australia-aboriginal.md:36`); the filename remains
absent; the sort position remains 11; total remains **223**. C01's demand number (61)
differs from K04's (52) because of regex scope, and C01 states that; the ownership
verdict rests on the exhaustive topic/heading tests, which I reproduced. C06's citations
to this ledger (`X02-honesty.md:59-72` for C-1…C-7; `:70-72` for the 217 vector defect)
are accurate.

**Updated position:**
- **C**: gap verified (K04 + my re-run), draft filed (C01), collision cleared for the
  same slug (C05), assembly filed (C06). Still missing: C02's README rev-2.5 diff,
  C03's source audit, C04's contract audit, and the integrator's landing. Total is still
  223, so the +1 is **not delivered**; the honest candidate is `unprovable-but-better`,
  not `improved`.
- **Ca**: unchanged — `reports/round-44/calib/` has zero files; no durable gate; the
  `STALE`/`FRESH` output is S01's scratch probe. **Not delivered.**
- **O**: unchanged from §10 — body/parity/pins verified; landing and filed census
  artifact still absent; O01/O05 absent.
- **Scope**: every file present sits at its assigned out path; `corpus/` has 0 changes;
  only `reports/round-44/` is untracked; the r42 witness digest is still `d8d23a26…`.
  No fabricated number found anywhere in the outputs audited.

**True close:** `2026-10-19T17:31Z`-ish (last command at `17:26:33Z`; C files landed
after). Any later output is outside this window.
