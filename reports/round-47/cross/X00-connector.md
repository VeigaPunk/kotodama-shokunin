# X00 — cross-claim connector (round 47, loop 2)

- Seat: X00 | role: connector | claim: cross | date 2026-10-19
- Baseline: `6e9a30d` (`git rev-parse HEAD` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`), equal to
  `reports/round-47/claims.json` `baseline_commit`; `claims.json` sha256 `7eb16979…1fa34`.
- Out path: `reports/round-47/cross/X00-connector.md` (the only repo write this seat makes).
- Mission (`reports/round-47/targets.json`, id `X00`): how the O freshness gate would have flagged
  r43 O/C and r44 C; how C's landing orders against the census; how Ca records the loop-1 amendments.
- Method: read-only commands at `6e9a30d`, plus a disposable `.scratch/x00/` mirror for the
  post-landing census delta. No filed byte edited, no corpus staging, no `run-validation.py`
  executed, no git/network mutation, no tool under `tools/harness/` modified.

**One-line result.** The r43 O and C premises are mechanically falsifiable at `7ceff59` with
capability and ownership probes (3/4 and 2/4 split clauses contradict), r43 Ca is a clean negative
control; r44 C is **not** stale by its literals — its `before` binds the process but never the
candidate gap, so the gate must refuse it as `could-not-evaluate`, not pass it green. C's landing
is a **+1 entry / +n couples-ref** delta on a 223/2730 census, and the README rev-2.5 edit must
repair a rev-2.4 prose vector that currently sums **217** while the sweep stays green. Ca's
successor needs **six** rows: the five r46-carried items plus the claim-added MANIFEST schema row.

## 0. Axes named (godspeed)

| axis | what this seat can move | move taken here |
|---|---|---|
| A1 stale-premise detection | encode each r43 `before` clause as a typed probe measured at its own baseline | §2 probe tables with the exact commands and measured values |
| A2 coverage-claim binding | show why a clauses-only gate cannot catch r44 C, and what probe would | §3 required-probe rule + the r47 C binding check |
| A3 landing order and ledger routing | fix the pre/post census order and the Ca row→owner map | §4 ordering + §5 six-row successor map |

## 1. State measured at HEAD `6e9a30d`

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

The index sweep is green at the live tree (`python3 -B reports/round-28/readme/sweep.py`, rc 0):

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 223 totals_ok True
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

Cartography ownership at HEAD (the C claim's premise):

```
$ find corpus/knowledge \( -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*map-making*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' -o -iname '*atlas*' \) | wc -l
0
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo PRESENT || echo ABSENT
ABSENT
$ grep -rliE 'cartograph|mapmak|map-making' corpus/knowledge/ | wc -l
2
```

The two body-mention files are `myth-symbol/cosmology-cosmography.md` (which explicitly says T-O
diagrams are **not** cartographic) and `civilizations/mesoamerica-primary-sources.md` (a manuscript
inventory row) — by-products, not owners, exactly as K02 scouted
(`reports/round-44/scout/K02-gap-scout.md:151-168`).

The topic-line sweep is **11 hits, 0 owners** — and this number is the trap for a naive probe:

```
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ | wc -l
11
```

Every hit is a false positive of one of three classes: `map` as a verb
(`synthesis/dialect-faction-map-workflow.md:2`), `map` as a metaphor for a system
(`purity-pollution-boundary-systems.md:4` "boundary map", `africa-primary-sources.md:2` "source
map"), or `chart` inside *charter*. **A `topic_owner_absent` probe for cartography must target
`cartograph|mapmaking|portolan|cadastr`, never `\bmap\b`** — otherwise it inherits the r44 R02
novel-phrasing false-positive class (`reports/round-44/review/R02-review.md:207-227`).

Prior-round registry check (the "not carried" clause):

```
$ grep -rniE 'cartograph|mapmaking' reports/round-*/scout/ reports/round-*/plan/ 2>/dev/null \
    | grep -v 'reports/round-44/scout/K02-gap-scout.md' | wc -l
0
```

`reports/round-19/gaps.md` and `reports/round-35/scout/K01-coverage-census.md` contain no
cartography row. So no prior round ever adopted a cartography slot. See §7.1 for the wording
precision problem: K02-r44 *is* itself a prior-round report recommending the landing.

## 2. How the O gate would have flagged r43 O and C (and spared Ca)

The tool does not exist yet (`tools/harness/claims-freshness.py` is absent at `6e9a30d`); the
tables below are **hand-encoded probes** against committed bytes. They are the verdicts the O
seat's tool must reproduce; they are not a tool run, and this seat does not claim otherwise.
Baseline for all r43 probes: `7ceff59` (r43's declared baseline).

### 2.1 Probe encoding rule

Each clause becomes exactly one measurable proposition:

```
{clause, probe_kind, target, expect, evidence_command}
```

`expect` is the measured state that makes the clause true (declared polarity, never inferred from
prose). A claim is STALE when **any** clause's measured value contradicts `expect`. Compound
sentences must be split; a bundled clause can hide a contradiction behind a true conjunct (see
§2.2, O-c3).

### 2.2 r43 O — STALE (the durable instrument existed)

| # | clause (paraphrase of `reports/round-43/claims.json:27`) | probe | expect | measured at `7ceff59` | verdict |
|---|---|---|---|---|---|
| O-c1 | "no durable instrument implements the r39 basename-couples policy" | `capability_present`: a tracked `tools/harness/*.py` whose text names and implements the policy | absent | **present** — `tools/harness/couples-reference-extractor.py:8` says `Policy implemented: reports/round-39/calib/basename-couples-policy.md`; sha256 `d8d23a26…`; `--selftest` rc 0 | **contradicted** |
| O-c2 | "the single wrapped couples field reads 0/4 tokens" | `count_eq` on the wrapped field `linguistics/phonetics-phonology.md` | 0 | **4** — selftest `PASS N6 regression guard: block read yields 4 tokens ['sound-change.md','sound-symbolism.md','tone-prosody.md','writing-systems.md']` | **contradicted** |
| O-c3a | "the verbatim policy landing lacks block extraction" | `capability_present`: block extraction in the tracked extractor | absent | **present** — `couples_block()` at `couples-reference-extractor.py:50`, `join_parts()` at `:76`, `couples_field()` at `:95` | **contradicted** |
| O-c3b | "…and a disposition leg" | `capability_present`: per-token reason/fallback listing | absent | absent (the r44 O `before` confirms it lists no fallback mappings and names no per-token reason) | holds |

Verdict: **STALE (3 of 4 sub-clauses contradict)**. The naive probe — `path_absent
tools/harness/basename-couples-resolver.py` — would have returned *true* (the claim-named path was
indeed absent) and called the premise fresh. That is the anti-theater case: the gate must measure
the capability, not the literal path the claim proposes to mint.

Reproduction of the capability probe (read-only extraction of the baseline bytes):

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py > .scratch/x00/base/couples-reference-extractor.py
$ sha256sum .scratch/x00/base/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
$ python3 -B .scratch/x00/base/couples-reference-extractor.py --selftest | tail -3
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens [...]
PASS glob fragment classified
rc=0
```

### 2.3 r43 C — STALE (counts true, ownership false)

| # | clause (`reports/round-43/claims.json:40`) | probe | expect | measured at `7ceff59` | verdict |
|---|---|---|---|---|---|
| C-c1 | "myth-symbol 26" | `count_eq corpus/knowledge/myth-symbol` | 26 | 26 | holds |
| C-c2 | "total 223" | `count_eq corpus/knowledge` | 223 | 223 | holds |
| C-c3 | "lithic slot named but **unbuilt**" | `topic_owner_absent` target `lithic` | absent | **1 owner** — `git grep -niE '^- topic:.*lithic' 7ceff59 -- 'corpus/knowledge/*/*.md'` → `myth-symbol/mineral-stone-symbolism.md:5` | **contradicted** |
| C-c4 | implied by c3: the entry is absent | `path_absent corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` | absent | **present**, sha256 `c99f44ca…` (`git show 7ceff59:… | sha256sum`) | **contradicted** |

Verdict: **STALE (2 of 4 clauses contradict)**. The count clauses are true, which is why a
count-only gate passes this claim — the exact failure the r44 R01 measured
(`reports/round-44/review/R01-review.md:243-247`).

### 2.4 r43 Ca — FRESH (the negative control in the same file)

| # | clause (`reports/round-43/claims.json:53`) | probe | expect | measured at `7ceff59` | verdict |
|---|---|---|---|---|---|
| Ca-c1 | no per-finding disposition record on record | `path_absent reports/round-43/calib/dispositions-r38-r39.json` | absent | absent (`git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/` → empty) | holds |
| Ca-c2 | the successor is not yet filed | `path_absent reports/round-43/calib/defect-queue-v2-successor-r43.json` | absent | absent (same empty tree) | holds |

Verdict: **FRESH**. The gate must not flag Ca; this is the positive regression's built-in
negative control (r44 R01 §4.3 item 3). The distinction is not "Ca is calibration" — it is that
Ca's `before` is a measurable absence that is actually absent.

### 2.5 What this closes

R01-43-12 (`reports/round-43/review/R01-review.md:400`) is closed when the gate refuses these two
`before` lines **before dispatch**. It does not retroactively validate r43: both claims remain
rejected at `7ceff59` (`reports/round-43/validation.json`, O `could-not-evaluate`, C
`blocked-by-topic-collision`).

## 3. How the gate treats r44 C — the coverage-claim boundary

### 3.1 The literals are true; the claim is nevertheless unbound

r44 C's `before` (`reports/round-44/claims.json:40`) is:

> "total 223; the r43 lithic claim was blocked because its topic was already owned — the correct
> coverage move is a fresh, verified-unowned gap"

Hand-encoded at `c9f4eaa`:

| # | clause | probe | measured | verdict |
|---|---|---|---|---|
| C-c1 | "total 223" | `count_eq corpus/knowledge` | 223 | holds |
| C-c2 | the r43 lithic topic was owned | `topic_owner_present` target `lithic` | present (`mineral-stone-symbolism.md` exists at `c9f4eaa`) | holds |
| C-c3 | the move is "a fresh, verified-unowned gap" | **no probe declared** — the candidate gap is deferred to a scout not yet run | — | **could-not-evaluate** |

A clauses-only gate returns **FRESH (2/2)**, which is a false green: the claim's actionable object
is not in the sentence. The actual failure was downstream and different in kind — the drafted
candidate (dream/vision/trance) had already been proposed at
`reports/round-42/scout/K02-myth-gaps.md:216`, so it was *carried*, not *owned*
(`reports/round-44/validation.json` claims.C.failures; `reports/round-44/review/R01-review.md`
§3.2). Meanwhile the fresh cartography gap had no entry body (`reports/round-44/validation.json`).

**Stale ≠ underspecified.** r44 C is not stale; it is unbindable. The contract's existing
`could-not-evaluate != green` rule must be extended from "no checks declared" to "no check binds
the claim's object".

### 3.2 Recommendation to the O author (O02/O03) — per-axis required probes

A coverage claim must declare, at minimum:

- `topic_owner_absent` with the candidate topic (domain word-mark, not a generic `map`);
- `path_absent` with the candidate slug;
- for "not carried", a **scoped** prior-proposal probe over the registry files, not a global grep
  (see §7.1).

If a coverage claim declares no such probe, the gate returns `could-not-evaluate` and exits
non-zero. This would have refused r44 C at dispatch — the honest verdict — and would have forced
the wave to name the candidate before claiming it. It would **not** have called r44 C stale, and
the artifact must not pretend it would.

A second, cheap control: run the gate twice — dispatch-time (as declared) and landing-time (after
the candidate is bound). r47's C claim already carries the binding at dispatch, so it can be
checked now (§3.3).

### 3.3 r47 C is bindable — measured at `6e9a30d`

| probe | expected | measured | verdict |
|---|---|---|---|
| `path_absent corpus/knowledge/culture-material/cartography-and-mapmaking.md` | absent | absent | holds |
| `count_eq corpus/knowledge` | 223 | 223 | holds |
| `topic_owner_absent` target `cartograph|mapmaking|portolan|cadastr` | absent | 0 owners | holds |
| registry proposal probe, scoped to r19 gaps + r35 census + r39/r40/r42 scouts | absent | 0 (r44 K02 excluded as this round's seed) | holds |

So r47 C passes a landing-time freshness check **if** the registry scope is declared. The global
"no prior-round proposal" wording is false on its face and must be read as "no prior-round
registry proposal" — §7.1.

## 4. How C's landing orders against the census

### 4.1 The pre-landing authority

At `6e9a30d`, the O-side census authority (`tools/harness/basename-couples-resolver.py`,
sha256 `43ce341f…`, 27/27 selftest) prints:

```
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
```

### 4.2 The post-landing delta — measured, not asserted

A disposable mirror with the same resolver and a 223-entry corpus, plus one synthetic
`cartography-and-mapmaking.md` carrying **3** `- couples:` tokens, measured:

```
223 entries / 2730 refs   (pre)
224 entries / 2733 refs   (post)
conservation: True in both
```

The delta is exactly **+1 entry / +3 refs** for three couples tokens. If the landed entry carries
`n` tokens (brace-expanded), the post census must read `entries=224`, `refs=2730+n`, and
`conservation: true`; the new entry's tokens must appear once each in the class split.

**Caveat — absolute class counts are not portable to a corpus-only mirror.** The same mirror
prints `direct=2539 fallback=166 ambiguous=0 unresolved=27`, not the in-tree
`2556/166/0/7`, because some refs name targets outside `corpus/knowledge/` that the mirror does
not contain. This repeats the r44 X00 root-sensitivity finding
(`reports/round-44/cross/X00-connector.md:72-79`). Only the **delta** is portable; the
**authoritative absolute census must run in-tree**, and the artifact must record the measured
root.

### 4.3 Required order (integrator)

1. Run the in-tree pre-census at `6e9a30d` **before any corpus byte moves**; record
   `entries=223 refs=2730`, the four-class split, the tool sha256, and the command.
2. Land the O tool and its demos (no corpus delta).
3. Apply the C entry as a new file (`A`, not `M`); `git status --porcelain` must show `??`
   before staging and no other corpus path.
4. Re-run the in-tree census: require `entries=224`, `refs=2730+n`, `conservation: true`.
5. Apply the README row + rev 2.5 (§4.4), then run the sweep: `224 rows vs 224 files`.
6. Run the prose-vector assertion (§4.5).
7. File Ca's successor citing the O artifact digest and the r43 demo output.

If C is accidentally applied before step 1, the pre-state is recoverable from `git show
6e9a30d:corpus/knowledge/...` / `git archive 6e9a30d`, but the run must say so; do not
reconstruct from memory.

### 4.4 README rev 2.5 arithmetic

Live section order and counts (sweep footer order):
`linguistics 25, myth-symbol 26, culture-material 25, synthesis 29, verification 24,
civilizations 94` = **223**.

rev-2.4's prose (`corpus/README.md:10-11`) says:

```
the totals and footer moved 220 → **223** and
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**
```

Measured with a six-integer sum over the arrow:

```
pre=25/23/25/29/24/94 sum=220   (correct for the 220 total)
post=25/23/26/25/24/94 sum=217  (contradicts the 223 on the same line)
```

The defect is entirely in the right-hand side: myth-symbol was not bumped (23, should be 26),
culture-material was wrongly bumped (26, should be 25), and synthesis was cut (25, should be 29).
Correct pre-vector = `25/26/25/29/24/94` (223); corrected rev-2.4 post-vector =
`25/26/25/29/24/94` (223); rev-2.5 post-C vector = `25/26/26/29/24/94` (**224**).

rev 2.5 must therefore carry, in the same edit:

- section header `## culture-material/ (25)` → `(26)`;
- totals line 223 → 224 and footer total 223 → 224;
- footer vector `25/26/25/29/24/94` → `25/26/26/29/24/94`;
- the new row inserted in `LC_ALL=C` filename order — between
  `calendar-festival-systems.md` (README:240) and `costume-semiotics.md` (README:241); the
  three-name sort check passes;
- the row's prose taken byte-equal from the entry's own `- topic:` line (rev-2.1 precedent);
- the rev-2.4 sentence repaired as a **forward correction** (sanctioned by r47's `non_goals`),
  not a rewrite of any closed round's filed bytes.

### 4.5 Why the sweep is green over a 217 vector

`sweep.py` reads the totals line and the footer (`footer_live` above), never the revision prose.
Measured: the live README is green at 223 while rev-2.4's own post-vector sums 217. So a green
sweep does **not** certify the prose. C09/C10 must add a one-line vector assertion. Executable
check (run against the current file; prints the defect):

```
$ python3 - <<'PY'
import re
t = open('corpus/README.md').read()
for m in re.finditer(r'the vector ([0-9/]+) \u2192 \*\*([0-9/]+)\*\*', t):
    a = [int(x) for x in m.group(1).split('/')]
    b = [int(x) for x in m.group(2).split('/')]
    print(f"pre={m.group(1)} sum={sum(a)}  post={m.group(2)} sum={sum(b)}")
PY
pre=25/23/25/29/24/94 sum=220  post=25/23/26/25/24/94 sum=217
```

After the fix it must print `post=25/26/26/29/24/94 sum=224` for rev 2.5 (and, if the rev-2.4
line is corrected, `sum=223`).

### 4.6 Collision check

No collision: the target path is absent (§1), the filename test has 0 owners, the topic-line test
has 0 owners after disposition, and no prior round adopted a cartography slot. The entry is `A`;
overwriting any existing entry is a stop condition, not a routing option.

## 5. How Ca records the loop-1 amendments

### 5.1 Ledger contract (measured)

- Parent: `reports/round-40/op/defect-queue-v2.json`, **38 rows**, sha256
  `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` — measured at HEAD and equal
  to the r43 successor's `parent_sha256_at_assembly`. **Pinned, never edited.**
- Precedent schema: `kotodama-defect-queue-successor-v1`
  (`reports/round-43/calib/defect-queue-v2-successor-r43.json`), keys
  `schema, round, date, artifact, parent, parent_sha256_at_assembly, parent_history,
  baseline_commit, source_dispositions, class_vocabulary, rows, application_gates, observations,
  provenance`; four-row body with `id, origin, class, owner, reason, next_touch, evidence,
  verification`.
- Classes: `fixed-with-evidence | routed-with-owner | recorded | could-not-recover`; v2 merge
  mapping to `carried-with-owner`.

`queue-successor-r47.json` is a **sibling successor**: it cites the r43 successor, never edits it.

### 5.2 The six rows (five r46-carried + one claim-added documentation row)

r46's carried list is exactly five bullets (`reports/round-46/loop-1-retrospective.md:45-53`),
which matches Ca's `before` count ("5 carried defects/amendments"). The MANIFEST schemas are the
claim's added documentation row (`reports/round-47/claims.json` Ca body), not a sixth carried
item — but they need a row so the claim's "documented" clause has a landing place. Zero dropped.

| id | origin (filed evidence) | class | owner | next_touch | re-run / evidence command |
|---|---|---|---|---|---|
| `R47-L1-FRESHNESS-GATE` | r46:45-46; r44 R01 §4.3 (`reports/round-44/review/R01-review.md:243-251`); R01-43-12 (`reports/round-43/review/R01-review.md:400`) | `routed-with-owner` | r47 O claim / integrator | land `tools/harness/claims-freshness.py`; flip to `fixed-with-evidence` only after the demo | `python3 tools/harness/claims-freshness.py --selftest` then `--claims reports/round-43/claims.json` (must flag O+C, spare Ca, exit 1) |
| `R47-L1-STALE-PATTERN` | r46:47-48; r43 `claims.json:27,40`; r44 `claims.json:40` | `recorded` (pattern note; the mechanical fix is the row above, do not double-count as two fixes) | integrator | none beyond the gate row | same gate run; record the pattern as the reason the gate exists |
| `R47-L1-RESOLVER-EDGE` | r46:49-50 (blank-separated hyphen soft-wrap drops tokens, 0 live incidence) | `recorded` | resolver maintainer (integrator-designated) | next resolver change | `python3 tools/harness/basename-couples-resolver.py --census` and a targeted soft-wrap fixture; assert 0 live incidence |
| `R47-L1-MANIFEST-SCHEMAS` | r46:37-38; `reports/round-46/audit/Ca01-manifest.md:6-8` and the 12-row table | `recorded` | integrator | none — recorded | the audit's reconciliation: closure rows 33-42 vs per-lane rows 43-44; 12/12 YES, zero discrepancies |
| `R47-L1-ANTIGRAVITY` | r46:51-52; r44 `claims.json:13`; r43 `claims.json:13`; r45 absent (`reports/round-45/` does not exist) | `recorded` (named deviation) | integrator | loop-2 positions 12-13 skip/re-route | cite the operator ruling; no round-45 directory to cite |
| `R47-L1-ZAI` | r46:53 and :59; r43 `claims.json:13` | `recorded` (named deviation) | integrator | zai → `openai-codex/gpt-6-luna-max` for the session | cite the r46 readiness line; do not claim a zai round ran |

### 5.3 Successor gates (recommended, in the r43 successor's style)

- **G1** The parent stays byte-identical at sha256 `dfc9265d…`; the successor is a new file.
- **G2** Every row carries non-empty `class`, `owner`, `evidence`; `fixed-with-evidence` only
  with a pasted re-run output.
- **G3** `R47-L1-FRESHNESS-GATE` must **not** be marked fixed merely because the tool file
  exists; it flips only when the r43 demo flags O and C, spares Ca, passes the negative control
  and the anti-theater mutation, and the selftest is green.
- **G4** Do not edit the r43 successor or any r43/r44 filed byte; cite them.
- **G5** The provider rows are **deviations**, not defects; keep the class `recorded` and name the
  operator ruling.

## 6. Cross-claim dependency map

```
C (coverage)  ── independent of O except one shared denominator:
                 pre-census 223/2730 must be captured before the entry lands
O (operability) ── lands the gate; no corpus change; its r43 demo reads filed bytes
Ca (calibration) ── row 1 routes to O's tool; rows 3-6 cite r46/r43/r44

integrator order: pre-census -> O tool -> C entry -> README rev 2.5 -> sweep + vector check
                  -> post-census -> Ca successor -> post-landing verifiers (V01/V02)
```

Failure handling: if O does not land, Ca's row 1 stays `routed-with-owner` — not fixed, not
dropped. If C does not land, the O census remains the 223/2730 authority and README stays rev 2.4
(do not file rev 2.5). The three claims never share a commit that would make a partial state look
complete.

## 7. Contested / to-verify (reported, not resolved here)

### 7.1 "no prior-round proposal" is imprecise

`reports/round-47/claims.json` C says "K02-r44: no owner, no prior proposal, not carried". K02-r44
**is** a prior-round report that recommends this exact landing (`reports/round-44/scout/K02-gap-scout.md:8`).
The defensible statement is: *no prior-round registry slot adopted it; no draft was ever produced;
the r44 scout is this round's seed*. A gate probe must be scoped to the registry files
(r19 gaps, r35 census, r39/r40/r42 scouts) — a global `grep_absent` over `reports/round-*/`
would flag the seed itself and call the claim stale. **Status: to-verify by R02/X04; recommend the
claim text be read with the registry scope, or amended at integration.**

### 7.2 r47's O `before` overstates the r44 history

It says "r43 and r44 both declared claims on stale premises (green resolver existed; owned/carried
topics)". Measured: r44 O's `before` was true and its claim landed `improved`
(`reports/round-44/validation.json` claims.O.verdict `improved`, passed `true`); r44 C failed for
a **carried candidate**, not an owned topic. The actionable clause — "no durable gate exists" — is
true (`tools/harness/claims-freshness.py` absent at `6e9a30d`), so the claim is FRESH, but the
historical parenthesis is imprecise. **Status: to-verify; do not repeat the overstatement in
`LOG.md`.**

### 7.3 The gate cannot catch a deferred candidate

§3.2's required-probe rule is a **recommendation to the O author**, not a property of a tool that
does not yet exist. Until the rule is encoded, a coverage claim with no bound topic passes green.
The r47 C claim is safe because it binds the topic; the rule is what makes that binding mandatory
rather than lucky.

### 7.4 Round 45 has no directory

The schedule's position 13 / round 45 was skipped (antigravity), and `reports/round-45/` does not
exist. Ca's antigravity row must cite the r46 retrospective (`:23`, `:51-52`) and the operator
ruling, not a nonexistent round receipt.

### 7.5 Absolute census portability

Only the delta is portable across roots (§4.2). Any census artifact that reports 2556/166/0/7
must name the in-tree root and the tool sha256; a mirror run reporting 2539/166/0/27 is not a
contradiction, it is a different root.

## 8. Evidence index (commands run, all read-only)

| evidence | command | result |
|---|---|---|
| HEAD / baseline match | `git rev-parse HEAD`; compare `claims.json` | `6e9a30d…` == declared |
| census | `find corpus/knowledge -name '*.md' | wc -l`; `ls corpus/knowledge/culture-material/*.md | wc -l` | 223 / 25 |
| index | `python3 -B reports/round-28/readme/sweep.py` | green, 223==223, sha `7c788a1d…` |
| cartography absence | find filename/glob; `test -e`; topic grep | 0 / ABSENT / 11 hits 0 owners |
| r43 O capability | `git show 7ceff59:tools/harness/couples-reference-extractor.py`; `--selftest` | sha `d8d23a26…`, rc 0, 4-token PASS |
| r43 C ownership | `git grep -niE '^- topic:.*lithic' 7ceff59 -- 'corpus/knowledge/*/*.md'`; `git ls-tree` count | 1 owner; 26 myth-symbol; 223 total |
| r43 Ca control | `git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/` | empty → FRESH |
| r44 C | `reports/round-44/validation.json`; `claims.json:40`; R01 §3.2 | blocked for carried candidate |
| post-landing delta | `.scratch/x00/post` mirror, synthetic 3-token entry | 223/2730 → 224/2733, conservation both |
| README vector | regex sum over `corpus/README.md:10-11` | pre 220, post **217** |
| parent queue pin | `sha256sum reports/round-40/op/defect-queue-v2.json` | `dfc9265d…` |
| r46 carried items | `reports/round-46/loop-1-retrospective.md:45-53` | 5 bullets |

Files read (no edits): `reports/round-43/claims.json`, `reports/round-44/claims.json`,
`reports/round-47/claims.json`, `reports/round-43/validation.json`,
`reports/round-44/validation.json`, `reports/round-46/loop-1-retrospective.md`,
`reports/round-44/scout/K02-gap-scout.md`, `reports/round-44/review/R01-review.md`,
`reports/round-44/cross/X00-connector.md`, `reports/round-46/audit/Ca01-manifest.md`,
`reports/round-40/op/defect-queue-v2.json`,
`reports/round-43/calib/defect-queue-v2-successor-r43.json`, `corpus/README.md`,
`tools/harness/basename-couples-resolver.py`.

## 9. Handoff

- **Integrator:** follow §4.3 exactly; the pre-census must precede the C landing. Apply rev 2.5
  with the §4.4 arithmetic and run the §4.5 vector check (the sweep alone is green over the
  defect).
- **O seats (O01-O04, O05-O07):** §2 is the regression fixture: r43 O STALE on capability +
  wrapped-count, r43 C STALE on ownership, r43 Ca FRESH. Encode clauses one proposition each
  (§2.2 O-c3 shows why compound clauses hide contradictions), and declare polarity explicitly.
  §3.2 is the required-probe recommendation; §3.3 is the r47 self-check.
- **C seats (C09/C10):** §4.4 gives the exact insert point and the three-slot vector repair;
  rev 2.4's pre-vector (220) is correct, only its post-vector is wrong.
- **Ca seats (Ca01-Ca06):** §5.2 is the six-row map; seven rows would double-count the pattern,
  five would drop MANIFEST. Pin the parent sha and keep row 1 `routed-with-owner` until O lands.
- **Reviewers (R02/R04/R05):** §7.1-7.2 are two honest precision defects in the round's own
  claim text; judge them as `to-verify`, not as fabricated evidence.
- **Not done by this seat:** no tool written or run, no entry drafted, no corpus staged, no filed
  byte touched, no `run-validation.py` executed. The probe tables are hand-encoded measurements,
  not a tool run, and are labelled as such.
