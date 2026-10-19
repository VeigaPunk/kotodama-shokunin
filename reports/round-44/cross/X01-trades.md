# X01 — trades critic, round 44

Seat `X01`, claim `cross`. Baseline `c9f4eaa`. Report written 2026-10-19 from the
live tree at that commit.

Method: read `reports/round-44/claims.json` + `targets.json`; independently
byte-extracted the r43 O09 successor body and ran it; ran the r42 extractor
read-only; ran a token-level parity across all 223 entries; ran ad-hoc naive
"freshness" checks against `reports/round-43/claims.json` at `7ceff59`; measured
the README/sweep state; inspected the r28 sweep's checks. No filed byte was
edited; scratch artifacts live under `.scratch/x01/`.

**Reading note.** At this seat's read time `reports/round-44/` contained only
`claims.json`, `targets.json` and `telemetry/dispatch-declared.json` — no C draft
and no freshness tool existed yet. C and Ca findings below are therefore
*pre-registered against the claims as written*, not observations of another
seat's output. O findings are measured against the actual O09 body.

---

## 1. Verdict summary

| # | Suspected trade | Verdict | Strongest evidence |
|---|---|---|---|
| T1 | Successor landing shadows the r42 extractor into two authorities | **Not a live fork; residual label risk is real but bounded** | 0 token-set differences across 223 entries / 2730 tokens; only 5 `prospective→unresolved` transitions; both files still runnable; no instrument index exists |
| T1b | Successor silently drops tokens its own docstring says it captures | **Confirmed latent defect, 0 live occurrences** | blank line + hyphen soft-wrap + indented continuation → successor 0 tokens, old extractor 2 tokens; corpus scan finds 0 such shapes |
| T1c | Landed body stamps itself `round: 43` | **Confirmed provenance defect** | `payload["round"] = 43` at `op/O09-scribe.md:816`; docstring line 357 says "(r43 claim O)" |
| T2 | C lands a gap that is already owned | **Cannot be ruled out; the round's own green criterion cannot detect it** | r43 C had true counts (26/223) and an already-owned topic; r28 sweep has no ownership leg (`sweep.py:139-146`, `:191-193`) |
| T3 | Freshness gate is theater | **Measured real risk: naive gates flag 0/2 r43 claims** | path-existence and count checks both miss; only capability + topic-ownership predicates catch O and C |
| T4 | C's landing invalidates O's census denominator | **Confirmed ordering hazard** | a new entry adds 36–44 distinct couples refs (measured on r42 landings); O's literal `2730` is a pre-C number |
| T5 | README rev 2.5 is "green" while carrying the rev-2.4 vector defect | **Confirmed pre-existing; sweep already green today** | rev-2.4 prose vector `25/23/26/25/24/94` sums **217**, not 223; sweep exits 0 at HEAD |

---

## 2. T1 — successor vs the r42 extractor: fork or witness?

### What I ran

Extracted the fenced body exactly as the integrator would:

```
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/x01/basename-couples-resolver.py
wc -l    -> 515
sha256   -> 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
--selftest -> SELFTEST OK: 27/27 controls
--census   -> entries=223 refs=2730
              policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
              artifacts: glob-fragment=1; conservation True; 50 fallback mappings
```

The digest matches the claim's expected `43ce341f…`, and the four-class fold is
`2556+166+0+7 = 2729` plus `1` glob = `2730`. The wrapped field's control `S1b`
compares the token **set** to `LIVE_TOKENS`, so it is identity, not arity
(`op/O09-scribe.md:684-685`).

### Token-level parity (the anti-fork evidence)

Loaded both modules with `importlib` and compared `resolve_entry` on all 223
entries (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/x01/parity.py`):

```
entries 223
token-set differences: 0
class-transition buckets:
  prospective -> unresolved: 5
      linguistics/language-contact.md: phonology-basics.md,
        honorifics-and-register.md, naming-and-onomastics.md
      linguistics/phonetics-phonology.md: sound-change.md, tone-prosody.md
```

This is the strongest fact in the round for O: the two tools extract **the same
2730 token identities from the same 223 entries**; their totals differ only by
the retired fifth class (`prospective`, 5 rows) that the four-class policy folds
into `unresolved` (`2 + 5 = 7`). So the parity receipt's required claim — "the
differences are explained solely by the documented subclass separation" — is
literally true, and the difficulty of the O07/O10 checks collapses to
reproducing this one comparison.

### Residual risk: no machine-readable demotion

Despite the parity, both files are live and both expose `--census`:

- `tools/harness/couples-reference-extractor.py` remains tracked, executable,
  digest `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`.
- `tools/harness/basename-couples-resolver.py` (to be landed) exposes the
  canonical four-class report.
- There is **no instrument index** in `tools/` (`ls tools/*.md` → none), so
  "witness-only" will exist only in prose (docstring, LOG, SCORECARD, parity
  receipt). A future seat that greps for "couples" will still find two scripts,
  and the old one's output (`unresolved=2 prospective=5`) is superficially
  incompatible with the new one (`unresolved=7`).

Recommendation (cheap, does not violate "old bytes untouched"): the r44 runner
should assert all three of:

```
test "$(sha256sum tools/harness/couples-reference-extractor.py | cut -d' ' -f1)" = \
  d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
test "$(git grep -l 'def couples_block' HEAD -- tools/ | wc -l)" = 2   # successor + witness
# and the parity script's output: token-set differences = 0, transitions = exactly 5
```

If the integrator wants a single durable marker, a tiny `tools/harness/README.md`
(or an `instruments` section in the r44 record) naming the successor authority
and the witness digest is the minimum; prose-only demotion is what makes this a
*suspected* trade rather than a closed one.

**Verdict on T1:** not a fork under the round's definition (one living parser +
one frozen witness, exact token parity). It is a **naming/authority risk**, not a
data risk. Close it by record + runner assertion, not by editing bytes.

---

## 3. T1b — the successor's hyphen-after-blank exception is unreachable

The body's own docstring (`reports/round-43/op/O09-scribe.md:406-414`) claims:

> A blank line terminates the block **unless the previous part ends in a hyphen
> soft wrap and the next line is indented** … the hyphen exception keeps the
> rule total without letting body prose after a blank line be captured.

The code cannot take that exception. At `op/O09-scribe.md:428-429`:

```python
soft_wrap = parts[-1].endswith("-") and not saw_blank
if INDENT_RE.match(following) and (not saw_blank or soft_wrap):
```

`soft_wrap` is forced `False` whenever `saw_blank` is true, so the second
disjunct is redundant: the branch is exactly `not saw_blank`. Measured on a
fixture (`.scratch/x01/hyphen_blank.md`):

```
- couples: language — `tone-

  prosody.md`; method — `writing-systems.md`
```

| tool | result |
|---|---|
| successor | `wrapped=False tokens=0` — **both** `tone-prosody.md` and `writing-systems.md` dropped |
| r42 extractor | `wrapped=True tokens=2` — `tone-prosody.md`, `writing-systems.md` both captured |

Live-corpus impact today: **zero**. A scan of all 223 entries for a
blank-separated indented continuation after a hyphen soft-wrap returns 0 hits
(`.scratch/x01/scan_hyphen_blank.py` → `blank-separated indented continuations
after a hyphen soft-wrap: 0`). So "zero tokens dropped" is true of the live
corpus; the *rule* is still wrong, and the next entry with that shape would lose
tokens silently (the docstring says it would not).

The claim requires landing byte-exact at `43ce341f…`, so this cannot be fixed in
the same move without losing the pinned digest. Correct disposition: file it as
a named limitation (`to-verify` → measured defect, owner: next resolver touch)
and optionally add a selftest control that documents the actual behavior. Do not
silently claim the docstring's rule is implemented.

---

## 4. T1c — the census artifact will self-identify as round 43

`op/O09-scribe.md:816`:

```python
payload["round"] = 43
```

and the docstring begins "Durable resolver + census for the basename-couples
policy (**r43 claim O**)" (`:357`). The tool bytes are pinned and must not be
edited, so an artifact produced with `--census --json` under `reports/round-44/`
will say `"round": 43`. That is a provenance mismatch in the round's own census
artifact — exactly the class of defect this lane keeps paying for.

Recommendation: file the artifact with an explicit envelope rather than raw
tool output, e.g.

```json
{"artifact_round": 44, "tool_round_stamp": 43,
 "tool": "tools/harness/basename-couples-resolver.py",
 "tool_sha256": "43ce341f…", "source_draft": "reports/round-43/op/O09-scribe.md:356-870",
 "baseline_commit": "c9f4eaa", "tree_state": "pre-C (223 entries)",
 "entries": 223, "refs": 2730, "...": "tool payload unchanged under .census"}
```

The r44 runner should verify both stamps and not require the tool to lie about
its origin.

---

## 5. T2 — the C gap: why "genuinely unowned" is the weak link

The C claim's threshold is `sweep green 224==224`. The r28 sweep cannot certify
ownership. Its only topic check compares each README row's text to the *same
file's* `- topic:` field (`sweep.py:139-146`); its pass predicate is
`missing/ghosts/mismatches/drift/footer/totals` (`sweep.py:191-203`). There is
no cross-entry topic-uniqueness leg. R01-43-8 already recorded this
(`reports/round-43/review/R01-review.md:396`), and r43 C is the proof by
demonstration:

- at `7ceff59`, `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`
  **exists** (`git cat-file -e 7ceff59:…` → yes; added by `7ceff59` itself);
- myth-symbol had 26 entries and the corpus 223 (`git ls-tree` counts);
- so r43 C's `before` numbers (`26`, `223`) were **true** while its prose
  premise ("lithic slot named but unbuilt", `reports/round-43/claims.json:40`)
  was false — the same sentence even admits the r42 C01/C04 collision that
  produced the owner.

A count-only or sweep-only verification will reproduce this failure exactly.
Pre-registered acceptance tests for the r44 C landing (run after bytes move, in
this order):

```bash
# 1. exactly one added corpus entry, README modified, nothing else under corpus
git diff --name-status c9f4eaa -- corpus
# expected: A corpus/knowledge/<part>/<new>.md ; M corpus/README.md
git diff --diff-filter=DM --name-only c9f4eaa -- corpus/knowledge   # must be empty

# 2. filename and topic are unique, not just new
ls corpus/knowledge/<part>/<new>.md                                  # one file
grep -rliE -- "^- topic:.*<distinctive 3-5 word phrase from the draft>" corpus/knowledge | wc -l
# expected: 1 (the new file itself)
grep -rli "<the draft's owned-object phrase>" corpus/knowledge | wc -l
# expected small; every hit must be a by-product mention, not a second owner

# 3. the new entry is census-clean under the new authority
python3 -B tools/harness/basename-couples-resolver.py corpus/knowledge/<part>/<new>.md
# every token must be direct/fallback, or unresolved with a declared-prospective-seed
# reason; no new dangling-reference or ambiguous row without a named disposition.

# 4. count + index
find corpus/knowledge -name '*.md' | wc -l                           # 224
python3 -B reports/round-28/readme/sweep.py                          # exit 0, 224==224
```

The decisive test is (2), not (4). The claim should record the topic-ownership
command it used and its output — an absence sweep over *filenames* alone (the
r42 spare's own error mode) is not enough; the r42 spare's topic line and the
landed entry's topic line are near-identical, so a topic-line comparison would
have caught it immediately.

**Verdict on T2:** unprovable at this seat's read time; the risk is structural
(the round's stated green criterion is blind to the failure mode). If the C
evidence does not include a topic-ownership command with output, treat the
"genuinely unowned" claim as `to-verify`, not verified.

---

## 6. T3 — freshness gate: measured theater risk

I implemented the three gate designs a reasonable author would reach for and ran
them over `reports/round-43/claims.json` at `7ceff59`
(`.scratch/x01/naive_gates.py`):

```
baseline 7ceff59
-- Gate A: does any tools/*.py named in after_required already exist at baseline? --
  O: paths={'tools/harness/basename-couples-resolver.py': False} -> stale_flag=False
  C: paths={} -> stale_flag=False
  Ca: paths={} -> stale_flag=False
-- Gate B: do the numbers in before match counts at baseline? --
  corpus_total=223 myth_symbol=26
  O: numbers_in_before=[] -> stale_flag=False
  C: numbers_in_before=[26, 223] all_match_counts=True -> stale_flag=False
  Ca: numbers_in_before=[] -> stale_flag=False
-- Gate C: topic-ownership test on the claim's named spare subject --
  entries whose topic line owns 'lithic': ['corpus/knowledge/myth-symbol/mineral-stone-symbolism.md']
  -> stale_flag=True
```

The two obvious mechanical gates flag **0 of 2** stale claims. Why:

- **r43 O** was false because the *capability* existed under another name. The
  claim-named path `basename-couples-resolver.py` did not exist at `7ceff59`;
  `couples-reference-extractor.py` did (digest `d8d23a26…`, green, 8/8). A gate
  that checks the `after_required` path is structurally incapable of catching
  this. The predicate that does catch it is capability-level:
  `git grep -l "basename-couples" 7ceff59 -- tools/` →
  `7ceff59:tools/harness/couples-reference-extractor.py`.
- **r43 C** was false only in its topic premise; both of its numbers were
  correct. A count gate passes it. The predicate that catches it is the
  topic-ownership test above (the live owner's `- topic:` line contains
  "lithic").

So the Ca claim's threshold ("flags the r43 O and C `before` lines") is
passable by a **lookup table tuned to those two strings**, and a genuine general
check does not yet exist. Anti-theater acceptance tests I would add to Ca's
verification (all cheap, all mechanical):

1. **Capability, not path.** The C-positive must still flag after the r43 claim
   copy is mutated so the durable tool is named `couples-reference-extractor.py`
   instead of the nonexistent target; it must also flag when run at `7ceff59`
   with the policy-name grep, independently of `after_required`.
2. **Topic, not count.** The C-positive must still flag when the claim's numeric
   literals (`26`, `223`) are edited to match the live counts (they already do);
   i.e. the flag must come from ownership, not from arithmetic.
3. **Negative control that is measured, not asserted.** Use r44's own O
   `before` at `c9f4eaa`; every clause is true today:
   `git grep -l "def couples_block" c9f4eaa -- tools/` → only the extractor;
   `git grep -l "four_class" c9f4eaa -- tools/` → none;
   `git show c9f4eaa:tools/harness/couples-reference-extractor.py | sed -n '63,65p'`
   → the blank-line `continue`; the old selftest has no ambiguous control; the
   old census prints no fallback mappings and no reasons. A gate that flags this
   `before` is over-firing.
4. **Baseline pinning.** The gate must read `claims.json.baseline_commit` and
   evaluate *there*. A gate run at post-landing HEAD will "correctly" flag every
   fulfilled `after` (r44 Ca's own `before`, "no mechanical pre-dispatch
   freshness check exists", becomes false once the tool lands). The output must
   print the commit it evaluated.
5. **Refusal semantics.** The claim says the gate "refuses to file a claim whose
   `before` is already false". Since `before` is free prose, a durable design
   needs an explicit predicate list per claim (e.g. a `before_checks` array of
   `{kind: path_absent|path_present|grep_absent|grep_present|count_eq|topic_unowned,
   ...}`), with the prose `before` required to be the human rendering of those
   checks. Without that, the tool is either a hardcoded r43 table or an
   unreliable natural-language parser. This is the single substantive design
   decision the Ca claim leaves open.

**Verdict on T3:** not necessarily theater, but the claim as written admits a
theatrical implementation. Require tests 1–4 in the filed demonstration; a gate
that only reproduces the two known strings should be judged `unchanged`, not
`improved`.

---

## 7. T4 — C's landing changes O's denominator

O's threshold is literal: `direct=2556 fallback=166 ambiguous=0 unresolved=7`
plus `glob-fragment=1`, `refs=2730`, `entries=223`. C requires `224` entries.
These cannot both hold on the same final tree. Measured contribution of a single
new entry (three r42 landings, distinct tokens per entry):

```
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md          tokens=44
corpus/knowledge/myth-symbol/purity-pollution-boundary-systems.md tokens=36
corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md      tokens=39
```

So a post-C census reads `entries=224`, `refs≈2766-2774`, and the four-class
fold shifts by the new entry's tokens. The 2730 figure is **a pre-C measurement
and must be labeled as such**.

The claim says "File ONE census artifact" but does not name the tree state. Two
acceptable resolutions; the round must pick one and say so:

- **pre-C artifact** (recommended, preserves every literal): file the census
  from the `c9f4eaa` tree or from the O landing before C is applied; record
  `baseline_commit: c9f4eaa`, `entries: 223`, and
  `state: pre-C / C-not-applied`; the r44 runner verifies the artifact, not a
  fresh census of the post-C tree.
- **post-C artifact**: re-run after C, record `224 / 2730+tokens(new entry)`,
  and explicitly rule that the claim's literal folds refer to the pre-C state.
  This is acceptable only if the delta is shown per token class.

Either way, a runner that re-runs `--census` after both landings and compares to
`2730` will fail. That is an ordering contract, not a corpus question.

---

## 8. T5 — the README's "green" gate already coexists with a wrong vector

At HEAD the sweep is green:

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25,
       "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223; missing 0; topic_mismatch 0; totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
exit=0; readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

Yet rev 2.4's prose at `corpus/README.md:11` says the vector moved to
`25/23/26/25/24/94`, which sums to **217**, not 223. The sweep does not parse the
revision prose vector, so `224==224` can be green while the new revision block
inherits/copies the same error. C02's mission already flags the vector; my
addition is the measured proof that the sweep cannot catch it. Also present and
untouched by the sweep: the H1 is duplicated at `corpus/README.md:1` and `:3`.

Recommendation for the rev-2.5 draft: compute the vector from the live counts
after the landing (footer format `[25, 26, 25, 29, 24, 94]` in order
linguistics/myth-symbol/culture-material/synthesis/verification/civilizations —
one slot moves), state the sum, and add an explicit arithmetic check to C's
audit evidence. Do not copy the rev-2.4 vector.

---

## 9. Cross-claim checks the integrator can run at close

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# O is real and byte-exact
sha256sum tools/harness/basename-couples-resolver.py   # 43ce341f…
python3 -B tools/harness/basename-couples-resolver.py --selftest   # 27/27
python3 -B tools/harness/basename-couples-resolver.py --census | head -4  # 223/2730, 2556/166/0/7+1
# witness untouched
sha256sum tools/harness/couples-reference-extractor.py # d8d23a26…
# C moved exactly one entry and one README
git diff --name-status c9f4eaa -- corpus
# no seat staged anything
git status --porcelain -- corpus tools | grep -v 'reports/round-44/' || true
```

The parity script I used is reproducible at
`.scratch/x01/parity.py` (loads both modules, compares `resolve_entry` over all
223 paths; expected output: `token-set differences: 0`, one bucket
`prospective -> unresolved: 5`).

---

## 10. Cannot verify / to-verify

- **C draft absent at read time** → the named gap, its partition, its couple
  tokens, and its collision distance are `to-verify`. My T2 checks are
  pre-registered, not applied.
- **Ca tool absent at read time** → whether the landed gate is general or a
  lookup table is `to-verify`; T3's tests 1–4 are the discriminator.
- **O07 parity receipt absent at read time** → I independently measured exact
  token parity; the receipt must reproduce it, not assert it.
- **`reports/round-44/calib/` did not exist at read time** → artifact shape and
  `tree_state` labeling are `to-verify`.
- The O body's `"round": 43` stamp and the hyphen-after-blank defect are
  **measured**, not suspected; the disposition (record vs fix) belongs to the
  integrator because the pinned digest forbids a silent fix.

---

## 11. Second read — observed artifacts (same day, later cut)

At this second read `reports/round-44/` held 21 files (O02/O03/O04/O06/O07/O08/
O09/O10, K01/K02/K04, C01/C05/C06, X00/X02, A01, S01/S02). Still absent:
`plan/P01`, `cov/C02`–`C04`, `review/R01`–`R02`, and the whole `calib/` tree
(`ls reports/round-44/calib/` → empty). So §6 (T3) remains untested, and the
Ca claim currently has no filed artifact; apply §6 tests 1–4 to whatever lands.
`reports/round-44/run-validation.py` does not exist yet either — normal at this
cut, but its O check must follow §7/T4 and its C check §5.

### 11.1 T6 — two scouts named two different gaps; the draft serves the second

This is now the largest live coordination trade in claim C.

- **K02** (the seat the mission names as the gap scout) selected **cartography /
  mapmaking**: `corpus/knowledge/culture-material/cartography-and-mapmaking.md`
  (`scout/K02-gap-scout.md:8`, `:85`, `:91-190`). Its evidence is clean:
  0 filename owners, 11 topic-line hits all dispositioned as metaphor or
  by-product, and the strongest possible charter — `cosmology-cosmography.md:71`
  and `:102` explicitly say T-O diagrams are symbolic, **not survey maps**.
- **K04** (the independent second scout) ran when K02 was absent and named
  **dream / vision / trance**: `corpus/knowledge/myth-symbol/dream-vision-trance.md`
  (`scout/K04-gap-verify.md:10-13`).
- **C01 drafted K04's gap** (`cov/C01-entry-draft.md:8-10`), with an explicit
  caveat that it is a spare if K02 names a different gap. **C05 cleared the
  dream path** (`cov/C05-collision.md:3-13`), also with the caveat that the
  claim-level choice was pending.

Ownership evidence is **not symmetric**, and this is the part no seat owns:

| candidate | filename owners | `- topic:` line containing the domain | nearest-owner evidence |
|---|---:|---:|---|
| cartography / mapmaking | 0 | **0** (11 hits are "map" metaphor: source map, identity map, dialect map, boundary map) | cosmography explicitly disclaims survey maps (`cosmography:71,:102`) |
| dream / vision / trance | 0 | **1** — `myth-symbol/divination-omen-systems.md:3` names "**dream-oracles and incubation**" as one of its fourteen technique rows | divination owns the reading technology; the state/induction/career is genuinely outside it |

Measured for the table:

```
$ grep -n '^- topic:' corpus/knowledge/myth-symbol/divination-omen-systems.md
3:- topic: ... a fourteen-row technique typology ... dream-oracles and incubation ...
$ grep -rilE -- '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey)' corpus/knowledge/*/*.md
(no ownership hit — all matches are metaphor/by-product)
```

So dream is a **soft adjacency** (a legitimate boundary call), not a zero-owner
gap like cartography. The r43 defect was a hard collision (a whole entry owned
lithic); dream is not that, but the claim's `one-owner-per-topic` language will
read 2 topic-line hits after landing, so the new entry must state the split
explicitly in its own `- topic:`/`- couples:` text (C01 §1.5 already does).

**Trade:** the claim says "the wave's scout names a gap" (singular) and `+1`
entry. With K02 and K04 both filed, the integrator must pick one gap and file
the other as a named spare. Do **not** land both (that is `+2`, total 225, and
breaks the claim's threshold). Whichever is chosen, the C evidence chain
currently splits: C01/C05/C06 cover dream; K02 covers cartography with no draft.
If cartography is chosen, C01's draft must be recorded as a spare and a new
draft/audit is owed; if dream is chosen, K02's cartography finding must be
recorded as the unfiled spare (it is not a failed sweep — it is a valid gap).
This is a decision for the integrator, not for a seat to route around.

### 11.2 T4 quantified on the actual draft

Extracted C01's fenced entry (`cov/C01-entry-draft.md:109-392`, 284 lines) and
ran the successor resolver on it:

```
.scratch/x01/c01-entry.md wrapped=False tokens=14
classes: {'direct': 14}          # 0 unresolved, 0 ambiguous, 0 glob
```

All 14 are fully-qualified `corpus/knowledge/...` refs, so they stay `direct`
after the file moves into `corpus/knowledge/myth-symbol/`. The post-C census
therefore has a **exact**, not estimated, expectation:

```
entries 224
refs 2730 + 14 = 2744
direct 2556 + 14 = 2570; fallback 166; ambiguous 0; unresolved 7; glob 1
conservation 2570+166+0+7 = 2743 (+1 glob) = 2744
```

This confirms T4 with the real draft (the earlier 36–44 range was the r42
landings; the actual draft is leaner). It also adds a positive C finding: the
draft is **census-clean** — it introduces no new fallback/ambiguous/unresolved
row, so the single-authority census needs no new disposition for it. Record
`delta_refs: 14` in the census artifact or in C's post-landing check; O's
`2730` remains a pre-C identity.

### 11.3 T1d — root-shadow trap: a selftest-green census on the wrong corpus

O06 and O07 independently hit a pre-existing `.scratch/` lane clone and got a
green selftest over a stale tree. From `op/O06-census-artifact.md:29-56` and
`op/O07-parity.md` §2:

```
.scratch/o06/  -> LANE .scratch/o06 ; KNOW .scratch/o06/corpus/knowledge (212 entries)
census -> entries=212 refs=2508  direct=2337 fallback=163 ambiguous=0 unresolved=7
selftest -> 27/27 (green)         # the wrong corpus, still green
```

The body's root search walks upward to the first `corpus/knowledge`
(`op/O09-scribe.md:382-390`) and the default text output does **not** print the
resolved `LANE`/`KNOW`. So a verifier who extracts into `.scratch/o06` or
`.scratch/o07` can produce a fully green, fully wrong census. This is a real
reproducibility trade, not a hypothetical: two seats hit it in this round.

Mitigation (artifact-layer, since the tool bytes are digest-pinned):

- the filed census JSON must carry `resolved_root` (absolute `KNOW`) and
  `entries`; the integrator should assert
  `resolved_root == $PWD/corpus/knowledge` and `entries == 223` before accepting
  the numbers;
- the runner's O check should print/compare the root, not just the totals;
- verifiers must extract into a directory with **no `corpus/` ancestor** (O02's
  mission says this; O06 had to re-extract to `.scratch/o06c/`, O07 to
  `.scratch/o07-parity/`).

Verdict: real operational trade, already caught by two seats and corrected in
their runs; it becomes a defect only if the filed artifact omits the resolved
root and a later reader regenerates from a shadow.

### 11.4 T2 evidence update

C05's independent enumeration agrees with my sweep on the mechanical facts:
223 entries, `dream-vision-trance.md` absent in every partition, slug
convention-clean, maximum `difflib` similarity 0.609, sorts at myth-symbol
position 11, landing delta exactly two paths (one `A` + README `M`)
(`cov/C05-collision.md:3-13`, §1). My pre-registered checks in §5 still apply;
the only open part is the topic-ownership boundary of §11.1, which is a written
disposition, not a count.

### 11.5 T3 status

No `calib/` artifact exists at this cut, so the freshness gate cannot be
tested. The risk stated in §6 is therefore **unmitigated and unverified**, not
refuted. When Ca01–Ca03 land, the discriminating tests are: the mutated-filename
positive (capability predicate), the numbers-stripped C positive
(topic predicate), the r44-O true-`before` negative control, and the
baseline-commit print. A gate that only reproduces the two r43 strings is
`unchanged`, not `improved`.
