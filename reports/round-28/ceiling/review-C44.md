# R28-C54 — reviewer of `C44.md` (the mechanism)

- **seat:** R28-C54 (C-ceiling, reviewer 4 of 6). **lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **lane HEAD** `69cecbc`.
- **canon:** NON-CANON engineering review. Author-side evidence; admits nothing,
  certifies no round, is not independent promotion verification.
- **writes:** this file only. No corpus byte touched. Scratch `.scratch/`,
  `TMPDIR=$PWD/.scratch`.
- **reviews:** `reports/round-28/ceiling/C44.md` against the delivered phonology
  component and the gate.

## 0. Verdict

**PASS, with one defect found in the fragment (a wrong line citation for the
`lengthen` declaration), fixed by the author. The mechanism is verified from the
component's own bytes, and the fragment's own hedge about `lengthen` is accurate.**

| check | verdict |
|---|---|
| the biconditional holds 27/27 | pass |
| the never-coda set is `b g h j p w` | pass |
| the eight refusals all begin with a never-coda consonant | pass |
| the component line citations | **defect D-1** (fixed by the author) |
| the gate `reverse` citation | pass — checked and the suspicion withdrawn (§3a) |
| the `lengthen` hedge is not over-claimed | pass |

## 1. The biconditional, re-derived from the component

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/ceiling/measure-ceiling.py | tail -3
# mechanism: reverse is legal <=> the base-initial consonant is a licensed coda
#            -> True (27/27)
#   onsets=14 codas=8 never-coda=b,g,h,j,p,w
```

and independently from the component's own bytes:

```sh
python3 -B - <<'PY'
import runpy
n = runpy.run_path('tools/gates/naming-collision-gate.py')
p = n['load_yaml'](open('examples/culture-d4/packet.d4.yml').read())
cons = p['phonology']['consonants']
print('inventory', len(cons), cons)
PY
# inventory 14 ['p','t','k','b','d','g','m','n','s','r','l','w','j','h']
```

The eight codas are in the component at `:119` (`[n, m, s, k, l, r, t, d]`), so
`set(onsets) - set(codas)` = `{b, g, h, j, p, w}` — the fragment's set, exactly.
The mechanism is therefore not a fitted observation: it follows from the
component's own two lists.

## 2. The refusal table, checked row by row

Every one of the eight delivered refusals begins with a never-coda consonant:
`wak` (w), `wer` (w), `bek` (b), `wat` (w), `gim` (g), `gis` (g), `wad` (w),
`gul` (g). Verified:

```sh
python3 -B reports/round-28/ceiling/measure-ceiling.py --json | python3 -c \
 "import json,sys; d=json.load(sys.stdin); print(d['delivered']['illegal_ids'])"
# ['L-08','L-15','L-17','L-24','L-26','L-30','L-44','L-51']
```

and each of those IDs begins with `w`, `b` or `g` (the three never-coda
consonants that actually occur word-initially in the delivered lexicon; `h`, `j`
and `p` do not). The fragment's table is accurate.

## 3. Defect D-1 — a wrong citation for the `lengthen` declaration (fixed)

`C44.md` §3 cited `examples/culture-d4/components/02-phonology.yml:257` for the
`lengthen` operation's declaration. **No such declaration exists there.** Line 257
of that component is in the `witnesses:` block, and the only `lengthen`-adjacent
line in the whole component is `:216`, a sound-change rule
(`*h → ∅ / V _ V with lengthening of the first vowel`) that has nothing to do with
the register operation. The declaration is in a **different component**:

```sh
grep -rn "lengthen" examples/culture-d4/components/*.yml
# 02-phonology.yml:216:  rule: "*h → ∅ / V _ V with lengthening of the first vowel"
# 04-lexicon.yml:112:    operation: lengthen
# 04-lexicon.yml:115:    description: "the register's fire operation: ..."
# 04-lexicon.yml:116:    productivity: "closed; the register licenses a fixed set of lengthened forms"
```

**Disposition: fixed by the author** — `C44.md` §3 now cites
`04-lexicon.yml:112-116` and the packet's `morphology.derivation_rules`.

This is the defect class the lane names most often — a plausible-looking path
that resolves to nothing (round 27's `review-C43.md` §4 caught a fabricated
`linguistic-anatomy.md` the same way). Here the path resolved but the **line did
not**, which is the harder half to catch: a locator that lands on an unrelated
line is worse than one that 404s, because a reader who checks the file passes it.

### 3a. A withdrawn finding, recorded so the withdrawal is visible

This seat first suspected `C44.md` §1's citation of
`tools/gates/argot-derivation-gate.py:239` for `reverse` was wrong, on the theory
that `:239` was inside a docstring. Re-reading showed `:239` **is**
`def op_reverse(base):` — the citation was correct and **no edit was made**. The
withdrawal is recorded because a reviewer that silently drops a false alarm hides
the fact that it checked.

## 4. The `lengthen` hedge, checked

`C44.md` §3 says the D4 `lengthen` is packet-declared rather than a gate operation,
and that it produced no illegal form in this tree, explicitly **not** used by the
entry. Verified:

```sh
python3 -B - <<'PY'
import runpy
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
print(sorted(g['OP_FUNCTIONS']))     # ['head2', 'reverse']
PY
# ['head2', 'reverse']
```

So the gate computes only `head2` and `reverse`; `lengthen` is declared as a
machine-readable pattern/output pair in the component
(`examples/culture-d4/components/02-phonology.yml:257`), and the gate replays it
through `replay_rule`. The fragment's characterisation is exact, and its decision
**not** to rest any entry claim on the lengthen count is the right one — that
count is outside the ceiling's population and outside the entry's subject.

## 5. What this review did not do

Did not edit the fragment (the one suspected defect was withdrawn); did not
re-measure the cross-tab (that is `review-C41.md`'s subject); did not certify
claim C.

## 6. Replay

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest   # 10/10
python3 -B reports/round-28/ceiling/measure-ceiling.py | tail -3
grep -n "def op_reverse" tools/gates/argot-derivation-gate.py
sed -n '119p' examples/culture-d4/components/02-phonology.yml
```
