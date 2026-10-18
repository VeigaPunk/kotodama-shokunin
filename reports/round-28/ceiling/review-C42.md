# R28-C52 — reviewer of `C42.md` (the new entry)

- **seat:** R28-C52 (C-ceiling, reviewer 2 of 6). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **lane HEAD** `69cecbc`.
- **canon:** NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- **writes:** this file only. No corpus byte touched. Scratch `.scratch/`,
  `TMPDIR=$PWD/.scratch`.
- **reviews:** `reports/round-28/ceiling/C42.md` against the entry
  `corpus/knowledge/linguistics/register-lexicon-ceilings.md`
  (sha256 `bb579d51cea0a900571e77b6690978256a607ec08f500923674738107dc1bffe`).

## 0. Verdict

**PASS. Two defects found — one in the entry (a missing `## 4.` parent heading,
fixed by the author) and one in the fragment (an over-claimed read method, fixed
by the author). Every other entry-level check the fragment asserts was re-measured
and holds.**

| check | verdict |
|---|---|
| the entry clears the admission bar | pass — 11/11 sources, 0 unresolved |
| the entry is frontmatter-complete | pass — all five head keys |
| the entry's own `- topic:` text is what the README row carries | pass (see `review-C46.md` §2) |
| the entry names its gap and states the general lesson | pass |
| the entry carries a decision record | pass — `RLC-1..7` |
| the entry's heading hierarchy | **defect D-1** (fixed by the author) |
| the fragment's read-method labels | **defect D-2** (fixed by the author) |
| the entry makes no canon claim | pass |

## 1. The bar, re-derived

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/entry-audit.py corpus/knowledge/linguistics/register-lexicon-ceilings.md
# .../register-lexicon-ceilings.md  bar=True  filler=False  src=11/11
#   refs_unres=0  digests_bad=0  couples_unres=0  index=ok
```

Matches `C42.md` §1 exactly. `refs_unres=0` means every repo path in the entry's
source bullets resolves on disk; `digests_bad=0` means no bullet pins a digest to
a file the same bullet does not name — the laundering shape the leg exists to
catch. The entry pins **no** digest at all, and says why: every round-27 peer it
cites is cited **by revision**, because those files moved during round 27
(`reports/round-27/entry/C43.md` §3's churn measurement). That is the same
discipline the round-27 entry adopted, and it is the correct one here.

## 2. The general lesson, tested against the bytes

The entry's claim — "a register's derivation operation constrains which semantic
fields it can natively spell" — must be *stated*, not merely implied, and the
round-28 runner tests for it:

```sh
python3 -B reports/round-28/run-validation.py --check
# claims.C.measurement.entry.names_the_general_lesson: true
# claims.C.measurement.entry.subject_score: 7
```

`subject_score 7` is the maximum on the runner's token set (`ceiling`, `register`,
`reverse`, `derivation`, `semantic field`, `lexicon`, `spell`) — the entry's first
5 KB names all seven. The entry also states the lesson in bold in §1 and restates
it as `RLC-1`, so it is not a passing mention.

**The mechanism claim the entry rests on was re-measured by this seat** (not taken
from `C41.md`):

```sh
python3 -B reports/round-28/ceiling/measure-ceiling.py | tail -3
# mechanism: reverse is legal <=> the base-initial consonant is a licensed coda
#            -> True (27/27)
#   onsets=14 codas=8 never-coda=b,g,h,j,p,w
```

## 3. The three dispositions, checked for exhaustiveness

`C42.md` §3 and the entry §5 claim the dispositions are exhaustive. This seat
checked the claim by trying to construct a fourth: the register's coverage is
bounded by (i) the base list, (ii) the operation, or (iii) neither — and "neither"
is only possible if the law's vocabulary is already spellable, which is the
ceiling being **zero** for that law, i.e. not a disposition but the absence of the
problem. The entry's `RLC-5` states exactly this ("the three dispositions are
exhaustive, and each forbids one claim"), and the entry adds the useful
qualification that a designer may **combine** them while still choosing among the
three. **No defect.** The claim is stated at the right strength.

## 4. Defect D-1 — the entry had no `## 4.` parent heading (fixed)

The entry's section 4 was written as two `###` subsections (`### 4.1 Worked case`,
`### 4.2 The correction`) **with no `## 4.` heading above them**, so the numbering
jumped `## 3.` → `### 4.1`:

```sh
grep -n '^#\{1,4\} ' corpus/knowledge/linguistics/register-lexicon-ceilings.md
# 58:## 3. Measuring the ceiling: the procedure
# 81:### 4.1 Worked case: the D4 stamp register, measured     <- no ## 4. parent
# 126:### 4.2 The correction this entry carries
# 149:## 5. The three dispositions
```

Every other section of the entry uses `## N.` at the top level, so this was a
structural inconsistency, and a reader following the entry's own cross-references
to "§4.1" would find no §4 to locate them in.

**Disposition: fixed by the author** — a `## 4. The measurement, worked: the D4
stamp register` heading was added above `### 4.1`, and the entry re-measured:
**34,400 bytes**, 11 `##` sections, sha256
`bb579d51cea0a900571e77b6690978256a607ec08f500923674738107dc1bffe`. The bar leg
re-runs clean after the fix (`bar=True … src=11/11 … index=ok`).

This is worth recording because neither round-28 entry instrument catches it: the
audit's `DECISION_RE`/`GAP_RE` legs and the runner's `SECTION_RE` count `##`
headers only, so a missing parent heading passes both. It was found by reading the
heading tree, which is the check a reviewer owes.

## 5. Defect D-2 — an over-claimed read method in the fragment (fixed)

`C42.md` §4's table listed the Dixon (2020) LINGUIST List review as **"fetched"**,
alongside the Gotowski full text. That is an over-claim: what was actually
retrieved for the LINGUIST List page was a **search-result snippet** naming the
review and quoting its chapter-5 characterisation, not the review page itself.
The entry's own sources block is careful about exactly this distinction (it labels
the Dixon social-trigger material as attributed to the review, and keeps the
structural jalnguy facts on Dixon 1972, cited by path) — so the entry was right and
the **fragment** overstated the read method.

**Disposition: fixed by the author** — `C42.md` §4 now records the LINGUIST List
material as a search snippet, not a fetch, and the entry's sources block is
unchanged.

This is the right class of defect to record, because it is the lane's most
common one: a plausible "fetched" label on a source that was only seen in a
snippet. The distinction is load-bearing here — the entry uses the review only to
mark the social trigger as **contested**, a claim a snippet can support, and does
not use it for any structural fact.

## 6. What this review did not do

Did not edit the entry beyond the one heading fix it asked for; did not re-fetch
the external sources (the Gotowski full text was fetched by the author and its
content is consistent with what the entry claims — the attested orders 231/321/312
and the unattested 132/213); did not certify claim C.

## 7. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/audit/entry-audit.py corpus/knowledge/linguistics/register-lexicon-ceilings.md
grep -n '^#\{1,4\} ' corpus/knowledge/linguistics/register-lexicon-ceilings.md
python3 -B reports/round-28/run-validation.py --check
sha256sum corpus/knowledge/linguistics/register-lexicon-ceilings.md   # bb579d51…
```
