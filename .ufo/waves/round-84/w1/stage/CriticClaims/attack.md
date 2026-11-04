# CriticClaims — attack artifact (round 84, w1)

Companion to `.ufo/waves/round-84/w1/CriticClaims.md`; this file carries the raw re-derivations and
predicate reproductions. No lane byte was modified. Scratch trees were read-only extractions of
`81499ee4…` / `3ca2cf28…` and were removed at exit.

## Axes

1. **before-state truth** — is the frozen `before` text re-derivable at `81499ee4`?
2. **leg kill power** — which landing satisfies the `after` text without being the claimed work, and
   which leg catches it?
3. **control** — refusal at the frozen base, red at the freeze.
4. **contract determinacy** — where do two correct implementations of the tool contract disagree?
5. **falsifiability** — one command per claim that decides the after-state.

## A. Before-state, exact commands and results (base `81499ee4`)

```
git -C <lane> ls-tree -r --name-only 81499ee4 -- corpus/knowledge | grep -c '\.md$'   -> 257
find corpus/knowledge -name '*.md' | sed 's#.*/##' | grep -icE 'witch|witchcraft|sorcer|malefic'  -> 0
grep -rlE '^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)' corpus/knowledge | wc -l  -> 0
grep -roiE '\b(witch|witches|witchcraft|sorcer[a-z]*|malefic[a-z]*)\b' corpus/knowledge | wc -l     -> 22   (20 lines, 12 files)
grep -roiE '\b(witch|witchcraft|sorcery|sorcerer|malefic)\b'          corpus/knowledge | wc -l     -> 19   (17 lines, 10 files)
grep -rliE '^- gap filled:.*(witch|sorcer|malefic)' corpus/knowledge | wc -l                         -> 1
```

The single `- gap filled:` hit is `myth-symbol/amulets-talismans-apotropaic-marks.md:4`, which names
"witch mark" only as an absence probe for its own amulet surface. "No gap-filled **owner**" is true;
"no gap-filled **mention**" is false.

Registry, using `accept-d84.py`'s own `ROW_LINE` / 11-cell predicate on `corpus/SOURCES.md`:

```
all S-rows matched: 837
11-cell rows: 837
malformed: 0
first/last: ['S001', 'S002', 'S003'] ['S911', 'S912', 'S913']
distinct ids: 837
missing numbers 1..913: 76
S914..S917 present? []
```

Claim O, exact commands and results:

```
git ls-tree -r --name-only 81499ee4 tools examples | grep -ciE 'sound.?law|soundchange'   -> 0
git ls-tree -r --name-only 81499ee4 tools examples | grep -iE 'sound|chang'               -> examples/supplement-opencode-1/sound-change-vs-taboo.json
git grep -c SOUNDLAWS 81499ee4 -- tools examples reports | wc -l                          -> 0
git ls-tree -r --name-only 81499ee4 examples/sound-laws | wc -l                           -> 0
python3 tools/check-gate-registry.py --root .                                             -> GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead
                                                                                             GATE-REGISTRY-INFO: 25 tools without a row
```

The capability that **does** exist at base:

```
tools/check-craft-exercise.py:45   # --- toy law engine ---
tools/check-craft-exercise.py:50   def law_l1(w): ...
tools/check-craft-exercise.py:57   def law_l2(w): ...
tools/check-craft-exercise.py:64   def law_l3(w): ...
tools/check-craft-exercise.py:71   def law_l4(w): ...
tools/check-craft-exercise.py:199  for case in mech.get("cases", []):
tools/check-craft-exercise.py:201      out = word
tools/check-craft-exercise.py:203      for fn in funcs: out = fn(out)
```

Four ordered laws applied left-to-right to proto-forms, with a reversed-order control. The frozen
sentence "no committed tool applies ordered sound laws to a lexicon" is therefore false as written;
the narrow true sentence is "no committed tool is driven by a rule set, exposes apply/selftest, or
emits a trace; the only law engine is four laws hardcoded to one exercise". The `BEFORE` leg
(filename regex + `SOUNDLAWS` marker) passes either way.

At the freeze (`3ca2cf28`) the registry's arithmetic is already committed:
`GATE-REGISTRY: 2 missing / 74 registered / 63 instruments / 0 dead`, missing =
`reports/round-84/accept-d84.py`, `reports/round-84/accept-o84.py`. So O's `REGISTRY` leg forces
`SKILL.md` to add **three** rows (tool + both counters) to reach `0 missing / 77 registered / 63
instruments`; dropping the D-counter row fails `missing=0`.

## B. Predicate reproductions (claim D)

The `anchors` and `rows_leg` predicates below are verbatim from
`reports/round-84/accept-d84.py` at `3ca2cf28`.

```
LANDING-A bytes=1555 sections=7 decision_rows=6 anchors bullets=20 ids=4 malformed=0 -> ANCHORS PASS
LANDING-B grew=4 problems=none -> ROWS PASS
LANDING-C bullets=20 ids=['S9910', 'S9911', 'S998', 'S999'] malformed=0 ANCHORS PASS ; cited=['S914', 'S915', 'S916'] SOURCED PASS
S-registry at base contains S998? False
```

- **A**: 20 filler bullets over four ids pass; the 16 000-byte floor is padding, satisfied
  independently of the anchors.
- **B**: four 11-cell rows whose `source`, `anchor`, `teaches` cells are `x` pass `ROWS`; only
  cells 7/8/10 are read.
- **C**: anchors on ids that do not exist at lands pass `ANCHORS`; the new ids need only appear as
  substrings somewhere for `SOURCED`. r83 would have failed this (`accept-d83.py:158-162` computes
  `unknown` over all cited ids; the r83 receipt reads `cited=6 unknown=none new_cited=4`).

Cross-leg trap, `tools/check-cited-lines.py` on a one-line citation:

```
MULTI-ID lintprobe.md:1 S914,S917
MULTI-ID lintprobe.md:2 S915,S916
CITED-LINES: 2 finding(s) in 1 file(s)
exit=1
```

So "the four rows S914–S917 are opened this round" — the most natural way to satisfy `SOURCED` —
fails `LINT`. `SOURCED` needs ≥3 new ids as substrings; `LINT` allows at most one distinct id per
line. The entry must distribute them one per line.

## C. Contract ambiguity, demonstrated

Resume point after a replacement (`from=a`, `to=aa`), two readings of "one left-to-right
non-overlapping pass":

```
from='a' to='aa' word='aa'  -> after_source='aaaa'  after_output='aa'   agree=False
from='k' to='kk' word='kaka'-> after_source='kkakka' after_output='kkkk' agree=False
```

`DEMO` pins only the committed example's `c`, so whichever reading the example uses becomes the
de-facto semantics; the contract does not decide.

`#` in `post`, `from="a"` on `t a k a`:

- boundary-slot reading (`#` zero-width, must be the end marker) → `t a k`, 1 change;
- context-slot reading (`#` counted as a context position, guarded by a length check) → `t a k a`,
  0 changes.

I wrote the second first; it silently never fires a word-final rule. Both readings are defensible
from the frozen sentence "`#` means the word start (pre) or word end (post)".

Undefined and ungraded: trace `index` (column 2), trace `before`/`after` (columns 4/5), `rule` =
name vs ordinal (column 3; the counter forces name via `set(rule_names) <= fired`), `from`/`to`
tokenisation, identity rules (`from == to`: 0 or 1 trace line?), missing `pre`/`post`/`to` keys,
and whether `pre`/`post` are immediate or anywhere.

## D. Controls and red-before

Do-nothing (`--lands 81499ee4`, `--freeze 3ca2cf28`):

```
ACCEPT-D-84: FAIL legs=0/10 (refused: lands equals the frozen base -- do-nothing control)   exit=2
ACCEPT-O-84: FAIL legs=0/8  (refused: lands equals the frozen base -- do-nothing control)   exit=2
```

Red-before (`--lands 3ca2cf28`, `--freeze 3ca2cf28`): `ACCEPT-D-84: FAIL legs=2/10`
(FROZENCFG, BEFORE pass; ENTRY/SECTIONS/DECISIONS/ANCHORS/LINT/ROWS/SOURCED/SEPARABLE fail —
`ROWS` prints `grew=0 … problems=['S914 missing', 'S915 missing', 'S916 missing', 'S917 missing']`);
`ACCEPT-O-84: FAIL legs=2/8` (FROZENCFG, BEFORE pass; TOOL/SELFTEST/DEMO/NEGATIVE/REGISTRY/SEPARABLE
fail). Full tables are in the report.

Freeze mismatch: the tip `e160a72e` changes exactly three lines of `reports/round-84/claims.json`
(the `after` sentence, `decision_heading`, `anchors_heading`). Grading any descendant with
`--freeze 3ca2cf28` gives `LEG FROZENCFG FAIL … sha256 ff545df6c108`; with `--freeze e160a72e` it
gives `LEG FROZENCFG PASS`. The brief names `3ca2cf28`; the operative freeze is `e160a72e`.

House shape at base: five files carry `## 2. Six design decisions` and `## 3. Attested anchors`
(`culture-material/footwear-codes-terminology.md`, `culture-material/maritime-seafaring-lexicon.md`,
`myth-symbol/guest-right-hospitality-law.md`, `myth-symbol/marriage-alliance-bridewealth.md`,
`myth-symbol/ordeal-judicial-proof-rituals.md`); zero carry `## 2. The decision table` or
`## 4. Attested anchors`. The r1 headings are the house shape.

`guest-right-hospitality-law.md` gives the anchor budget: 22 bullets in `## 3`, repeated ids per
source row (S904 seven times, S905 once, …). So "20 anchors across ≥4 ids" is the house pattern; a
counter cannot distinguish 20 evidentiary bullets from 20 fillers, and the claim's `review_only`
correctly assigns that judgement to the reviewer.

## E. Falsifiers

Run at the claim's lands; both were run at `3ca2cf28` and correctly printed
`FALSIFIED: entry absent` / `FALSIFIED: tool absent` with exit 1. The full `bash -c` blocks are in
`CriticClaims.md` §5; the O block includes the two held-out derivations (`b a n a` → `b u n u` under
ordered rules; `t a k a` → `t a k` under `from=a, post=["#"]`) that no frozen leg runs.

## F. Corrections (smallest first)

1. Invoke with `--freeze e160a72e4adf1620e09f812b913d4ece0fcd5243`; build to
   `## 2. Six design decisions` / `## 3. Attested anchors`. Zero edits.
2. Tool accepts both `selftest` and `--selftest`. Two lines.
3. Grade each counter at its own claim's lands (r83 precedent: D `386e7002`, O `0f088572`,
   C `86f68b5b`). One protocol line.
4. Never write two distinct S-ids on one line. One authoring rule.
5. Reviewer reads the three ungraded row cells and asserts every anchor id exists; record the r84
   `SOURCED` regression (unknown-id check dropped since r83) for r85.
6. Tool `selftest` carries the two held-out cases; reviewer reruns the O falsifier.
