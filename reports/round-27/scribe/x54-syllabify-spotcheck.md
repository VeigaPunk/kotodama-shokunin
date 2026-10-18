# X54 — syllabify spot-check, before/after, on every delivered form

- **Seat:** SCRIBE X54, round 27 (operator: loop 3 of 3, build 3 of 4; 64 workers
  on `devin/deepseek-v4-1-flash-high`).
- **Assignment (verbatim):** "SCRIBE X54: spot-check (syllabify before/after on
  all 62 forms independently)."
- **Claim supported:** **D / depth** — `after_required` reads "the syllabify
  disagreement fixed (one algorithm, forms re-verified)"
  (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`reports/round-27/claims.json:5`); lane HEAD at every measurement below
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` (the round-27 declare commit).
- **Write scope:** `reports/round-27/scribe/x54-syllabify-spotcheck.py` and this
  file, plus gitignored scratch under `.scratch/x54/` (`export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command). **No tool, gate, packet, component,
  pin, fixture or shared bookkeeping was edited**; no commit, no push; no filed
  artifact of rounds 8–26 was modified. This seat authored none of the artifacts
  it measures.
- **Canon:** NON-CANON engineering evidence. A spot-check reports what the bytes
  do; it adjudicates no round and blesses no fix.

## 0. Headline

**The "syllabify disagreement" was never a two-way disagreement, and the
published count was not a measurement of the algorithm it named. The fix landed
mid-window and is partial: it closes the consonant-run axis and leaves the
diphthong axis open.**

Measured on all 62 round-26 forms and all 70 live forms. **The fix landed while
this seat was measuring** (19:20Z); the before/after pair below is the first of
this round.

| # | finding | severity |
|---|---|---|
| **X54-F1** | There are **three** readings of the syllabifier, not two. The delivered packet's **own `syllables:` field** on its 8 `names` records is a third, author-declared witness that **no** round had consulted. It agrees with the design's stated algorithm **8 of 8** and with the pre-fix gate **0 of 8**. | decisive for the fix |
| **X54-F2** | The published **"15 of 62"** (`reports/round-26/register/review.md` §5, `RL-3`) is **inflated by 3**. It counted the probe's own implementation, not the design's stated algorithm: the faithful count is **12 of 62**. Reproduced exactly. | the number was wrong |
| **X54-F3** | The round-26 probe ships **two mutually inconsistent "design" implementations** — `.scratch/r26-d-reg/syl.py:design_syll` and `.scratch/r26-d-reg/final.py:onset_syll`. Both are cited as "the design's stated algorithm"; they disagree on `saalumi`. **Independently confirmed by the D16 seat** (§3c). | instrument hazard |
| **X54-F4** | The published **`RL-2`** claim — "`head2` has an empty proper domain (59 of 62 identity)" — is a consequence of `syl.py`'s misreading, not of the design. Under the faithful algorithm **no** delivered form has ≥3 syllables, so the proper domain is empty **70 of 70**, not 59 of 62. | conclusion right, number wrong |
| **X54-F5** | The pre-fix gate split **67 of 70** delivered forms into at least one non-syllable (`['ke','r']`, `['ti','kme','s']`, `['sa','mre','n']`). **Fixed by the landing: 67 → 0.** | was the divergence deeper than head2 |
| **X54-F6** | The fix landed at 19:20Z and is **partial**: `head2` disagreements 12 → 3, non-syllable forms 59 → 0, packet witness **0/8 → 6/8**. The remaining 3 rows are exactly the falling-diphthong forms (`haitun`, `tumhai`, `haitik`); `VOWELS` at `argot-derivation-gate.py:129` has no diphthong concept. | **the claim is partially met** |
| **X54-F7** | The D seat's own in-flight reference (`.scratch/r27-d/sylref.py`, `66e33955…`) agrees with the packet's declared syllables only **6 of 8**, and its **own** comparison reported **0** head2 disagreements while the real divergence was **12** — a false-green instrument. The landed gate inherits the same diphthong defect. | warning, still open |
| **X54-F8** | The D16 seat's `s1`/`s2` reading pair **would have rejected the correct fix** (it asserted `head2(tikmes) == 'tik'`; the design defines `head2` as the first **two** syllables, so the answer is `'tikmes'`, and landing the correct algorithm made **both** fixtures red). **Fixed in-window by the D16 seat.** | found live, then fixed |

## 1. Why three witnesses, and why the third settles it

`reports/round-26/register/review.md` §5 measured the gate against **its own
re-implementation** of the design (`.scratch/r26-d-reg/syl.py`). Two readings,
**both authored inside round 26**. When two implementations disagree, a third —
obtained by a different route — is what settles it. The delivered packet already
contains one, and nobody has used it.

This seat measures three witnesses, each by a different route:

| witness | route | independence |
|---|---|---|
| **W1 — the delivered gate** | `runpy` of `tools/gates/argot-derivation-gate.py`, calling its own `syllabify()` | the artifact under test, **executed**, never re-implemented |
| **W2 — the design's stated algorithm** | re-implemented *in this seat's instrument* from the prose of `reports/round-17/d4/design-language.md:191-196` plus the packet's own `phonology` block | never copied from the gate, never copied from either round-26 probe |
| **W3 — the packet's own `syllables:` field** | the 8 `names` records, which carry an author-declared syllable split (`examples/culture-d4/packet.d4.yml:2229,2250,2271,2292,2313,2334,2355,2376`) | authored by an **earlier round** for a different purpose; consulted by neither W1 nor W2 |

W3 is decisive and it is unambiguous. The packet declares:

```
NM-01 tumhai  -> ['tum', 'hai']
NM-02 kalker  -> ['kal', 'ker']
NM-03 samren  -> ['sam', 'ren']
NM-04 mestum  -> ['mes', 'tum']
NM-05 haitik  -> ['hai', 'tik']
NM-06 meslun  -> ['mes', 'lun']
NM-07 kalnes  -> ['kal', 'nes']
NM-08 salwer  -> ['sal', 'wer']
```

**W2 agrees 8 of 8. W1 agrees 0 of 8.**

The packet's field also fixes the diphthong question, which is where the
round-26 probes went wrong. `NM-05 haitik -> ['hai','tik']` is **two**
syllables; therefore `hai` is **one** nucleus. The packet's `accent` field says
so directly: *"Vowel length is contrastive only on the stressed syllable and is
written as a double vowel (aa ee ii oo uu); the falling diphthongs ai and au are
the only other vowel sequences."* No appeal to external scholarship is needed —
the delivered packet states it twice, once in prose and once in data.

### 1.1 The gate's divergence, in full

W1 vs W2 over the live 70-form surface. `head2` disagreements: **12 of 70**
(unchanged from the round-26 surface — the 8 register forms round 26 added are
all one-syllable, so they cannot move this count):

| id | form | W1 (gate) `head2` | W2 (design) `head2` | W3 (packet) |
|---|---|---|---|---|
| L-45 | `tikmes` | `tikme` | `tikmes` | — |
| L-46 | `mesar` | `mesa` | `mesar` | — |
| L-47 | `kalen` | `kale` | `kalen` | — |
| L-48 | `haitun` | `hai` | `haitun` | — |
| NM-01 | `tumhai` | `tumha` | `tumhai` | `['tum','hai']` |
| NM-02 | `kalker` | `kalke` | `kalker` | `['kal','ker']` |
| NM-03 | `samren` | `samre` | `samren` | `['sam','ren']` |
| NM-04 | `mestum` | `mestu` | `mestum` | `['mes','tum']` |
| NM-05 | `haitik` | `hai` | `haitik` | `['hai','tik']` |
| NM-06 | `meslun` | `meslu` | `meslun` | `['mes','lun']` |
| NM-07 | `kalnes` | `kalne` | `kalnes` | `['kal','nes']` |
| NM-08 | `salwer` | `salwe` | `salwer` | `['sal','wer']` |

**X54-F5 (the deeper reading).** The divergence is not confined to `head2`.
Scored against the packet's own legality table, the gate emits at least one
**non-syllable** for **67 of 70** forms. The gate's outputs are not merely
"simpler maximal-onset" — they are strings that are not syllabifications of this
language at all:

```
L-01 ker     W1 ['ke', 'r']        'r' alone is not a legal syllable
L-02 tum     W1 ['tu', 'm']        'm' alone is not a legal syllable
L-45 tikmes  W1 ['ti', 'kme', 's'] 'kme' is an onset cluster — onset_clusters: false
NM-01 tumhai W1 ['tu', 'mha', 'i'] 'mha' is an onset cluster
NM-03 samren W1 ['sa', 'mre', 'n'] 'mre' is an onset cluster
```

Round 26 recorded the *opposite* framing — `review.md` §5: "The gate's outputs
are never *illegal* (`kme` is a cluster-bearing 'syllable' only because the gate
does not validate), so the divergence does not manufacture a finding". The first
clause is true of the gate's own non-validating reading and false of the
packet's: `kme` **is** illegal, and the reason it appears is that the gate never
consults the legality table. The second clause is the substantive one and this
seat agrees with it — no delivered packet record is *failed* by the divergence
today, because no delivered rule is `head2`-scoped.

## 2. X54-F2 — the published "15 of 62" is inflated by 3

Reproduced by transcribing the probe's own `design_syll` verbatim
(`.scratch/r26-d-reg/syl.py`) and re-running it:

```
published (reports/round-26/register/review.md §5):   15 of 62
this seat, probe implementation re-run:               15 of 62   <- reproduces exactly
this seat, W2 from the design's prose:                12 of 62
probe-only (false) disagreements:                     3
    L-12 sau  gate='sau'  probe-design='sa'
    L-19 dau  gate='dau'  probe-design='da'
    L-28 hai  gate='hai'  probe-design='ha'
```

The three excess rows are exactly the vowel-final forms whose first nucleus is a
**falling diphthong**. The probe's `design_syll` treats `ai`/`au` as two
nuclei, so it splits `hai` into `['h','a','i']` and takes `head2 = 'ha'` — while
the gate, which does treat `hai` as one nucleus, gives `'hai'`. The probe then
counts the gate as wrong. But the packet's own `NM-05 haitik -> ['hai','tik']`
shows `hai` is one syllable, so **on these three rows the gate is right and the
probe is wrong**.

Consequence for the claim: the declared fix is "one algorithm, forms
re-verified". The count that the fix is being measured against is **not a
measurement of the algorithm it cites**. A round-27 fix verified against 15 will
be chasing three rows that are already correct.

## 3. X54-F3 — two mutually inconsistent "design" implementations, both cited as the design

`.scratch/r26-d-reg/` contains two functions, each documented as the design's
stated algorithm, which disagree with each other:

| file | function | `saalumi` | `hai` | `tumhai` |
|---|---|---|---|---|
| `syl.py` | `design_syll` | `['s','aal','um','i']` → `head2 saal` | `['h','a','i']` | `['t','um','h','a','i']` |
| `final.py` | `onset_syll` | `['saa','lu','mi']` → `head2 saalu` | `['ha','i']` | `['tum','ha','i']` |
| **W3 (the packet)** | — | — | **one syllable** | `['tum','hai']` |

`final.py` is the corrected reading and it says so in its own docstring ("The
design's maximal-ONSET reading, correctly"). It reproduces the design's one
published worked row (`head2(saalumi) = saalu`) and it reproduces W3 on
`kalker`, `tikmes`, `ker`, `nes`. But it still splits `hai` as `['ha','i']`,
which W3 contradicts — so `final.py` is closer than `syl.py` and still not
faithful on the diphthong.

**Both** implementations are then used as evidence for different published
claims: `syl.py` for the "15 of 62" (`review.md` §5) and `final.py` for the
"3 of 62 / 59 of 62" (`review.md` §4). A reader of the review has no way to see
that the two numbers come from two different algorithms, one of which the other
supersedes.

## 3b. X54-F7 — the round-27 D seat's own in-flight reference fails the packet's witness

At this seat's stamp the D seats had landed scratch but not the gate: the
reference implementation they are building the fix against is
`.scratch/r27-d/sylref.py` (sha256 `66e33955…`, mtime 16:13Z), whose docstring
reads *"Reference: the design-language.md section 5 maximal-onset algorithm,
with the legality test the delivered gate omits"*. This seat ran it as filed
(scratch is read-only here, never edited):

```
$ python3 -c "... import sylref; compare ..."
sylref (D seat, in-flight): W3 agreement 6/8
   fails NM-01 tumhai  sylref ['tum','ha','i']   packet ['tum','hai']
   fails NM-05 haitik  sylref ['ha','i','tik']   packet ['hai','tik']
W2 (this seat):             W3 agreement 8/8   failures: []
```

It disagrees with the design's prose on **6** forms — `sau`, `dau`, `hai`,
`haitun`, `tumhai`, `haitik` — all six for the same reason as the round-26
probes: it treats `ai`/`au` as two nuclei. The packet's `accent` field calls
them "the only other **vowel sequences**", and its data treats `hai` as one
syllable (`NM-05 haitik -> ['hai','tik']`).

**The false-green is the part that matters.** `sylref.py`'s own
`licensed('hai')` returns **True**, because its legality predicate accepts a
sequence of two adjacent vowels as a nucleus. So when the D seat runs its own
comparison (`.scratch/r27-d/disagreements-before.json`, written 16:14Z), the
head2 column reads **0 disagreements** while the gate still disagrees with the
faithful reading on **12** forms:

```
D-seat reference disagreements:            67
  of which head2 disagreements:             0    <- the comparison the D seat reads
this seat, gate vs W2 (faithful):           12   <- the real head2 divergence
this seat, gate vs sylref:                  70   (sylref's own syllables differ on 67)
```

That is the round-26 failure mode repeating one round later: an instrument that
cannot see the divergence reports the divergence as absent. A fix landed against
`sylref.py`'s comparison would be verified by a check that already passes before
the fix, and would leave the gate's `head2` on `kalker` as `kalke`.

`sylref.py` is **scratch, and gitignored** — it is not a deliverable, and the D
seats were still writing at this stamp. This finding is filed as a *warning to
the landing seat*, not as a defect against the round: the reference is a
work-in-progress, and the defect it carries is exactly the one
`reports/round-27/scribe/x54-syllabify-spotcheck.py` C2/C2b controls fail
closed on.

## 3c. Independent corroboration — the wave reached X54-F3 and X54-F1 by its own route

Two of this seat's findings were reached **independently** by the round-27 D
seats inside the same window, which is the cross-check that makes them more than
one seat's reading:

1. **X54-F3 / the round-26 reference defect.** `reports/round-27/gate-tests/run-gate-tests.py`
   (the D16 seat's battery) writes, without citing this seat:

   > "The design fixes `head2(saalumi) == saalu` in its own table; the round-26
   > design seat's reference yields `saal` on that same row, so the 'gate
   > disagrees with the design' count was measured against a reference that
   > fails the design's own named row."

   That is this seat's `X54-F3`, reached from the design's published table rather
   than from the probe source. Two routes, one conclusion.

2. **X54-F1 / the packet's `syllables:` field as the acceptance surface.** The
   same runner's `syllables_witness` block declares the packet field, records
   `declared_rows: 8`, `gate_agrees: 0`, and files the gap verbatim:

   > "the delivered syllabifier disagrees with the packet's own `syllables:`
   > field on 8 of 8 name records (gate agrees 0/8): the syllabify leg of claim D
   > is UNLANDED at this stamp, and the packet's own field is the acceptance
   > surface a fix must satisfy"

   Its `syllables_witness.gate_agrees: 0` and `declared_rows: 8` are **the same
   two numbers this seat measured independently** (§1: W1 agrees 0/8). The
   runner's note credits this seat's `X54-H3` for the surface; the **numbers**
   are its own.

This seat's `X54-F2` (the "15 of 62" inflation) and `X54-F7` (the in-flight
`sylref.py` diphthong defect and its false-green self-comparison) are **not**
corroborated by any other round-27 artifact at this stamp. They rest on this
seat's transcription and execution of the two probes and the D reference, all
three reproduced by digest.

## 3d. X54-F8 — the D16 reading pair would have rejected the correct fix (fixed in-window)

**Status: this trap was live when this seat measured it and has since been fixed
by the D16 seat.** The record is kept because a false-red battery is exactly the
class of defect that silently reverts a correct change, and because the fix is
itself evidence that the finding was real.

At 19:19Z the D16 seat's battery distinguished two readings of `head2(tikmes)`
with a fixture pair (`reports/round-27/gate-tests/run-gate-tests.py:88-100`), and
its own comment stated the acceptance rule:

> "exactly one of s1/s2 may be clean, whichever side the syllabify fix lands on.
> … if a change makes BOTH clean (the leg stops discriminating) or **BOTH red
> (the reading pair collapsed), it fails**."

The pair as it stood was:

| fixture | asserted | yields |
|---|---|---|
| `s1-head2-unconstrained` | `head2(tikmes) == 'tikme'` | the pre-fix gate's reading |
| `s2-head2-constrained` | `head2(tikmes) == 'tik'` | called "the legality-constrained reading the round-26 design seat states" |

**Both fixtures were diphthong-free**, so the pair exercised no part of the
disagreement this seat measured. And `s2` was not the design's algorithm: the
faithful reading of `tikmes` is **two** syllables, `['tik','mes']`, so `head2` —
the first **two** syllables, by the design's own definition — is `'tikmes'`, not
`'tik'`. `'tik'` is the first **one** syllable.

Measured by patching `syllabify` in an **isolated `git clone --shared` under
`.scratch/x54/clone/`** (the lane worktree was never touched) with the faithful
algorithm — the one that satisfies the design's own published worked row **and**
the packet's witness 8 of 8:

```
$ python3 .scratch/x54/clone/tools/gates/argot-derivation-gate.py <fixture>   # patched clone
s1-head2-unconstrained       exit=1
s2-head2-constrained         exit=1
s3-head2-maximal-coda        exit=1
```

So the correct fix read **8 of 8** on the packet's witness, reproduced the
design's published row, and made **both** `s1` and `s2` red — which the D16
runner's own rule scored as a failure ("BOTH red (the reading pair collapsed)").
A D seat landing the correct fix would have seen a red battery.

**The D16 seat fixed it inside the window.** By 19:23Z the runner had
re-anchored the pair on `tumkalker`, a **two-cluster** base, with the reasoning
stated in its own comment:

> "`tikmes` is a one-cluster base, and the legality clause collapses the two
> readings of it into one (`tik.mes` under both), so it cannot discriminate once
> the fix lands. `tumkalker` carries two clusters and the two readings genuinely
> differ on it."

and added `s4-head2-prefix-reading` as an explicit before/after witness for the
`tikmes` row. Re-measured against the **landed** gate:

```
s1-head2-unconstrained  (tumka)   exit=1
s2-head2-constrained    (tumkal)  exit=0     <- exactly one clean: the pair discriminates
s3-head2-maximal-coda   (saalum)  exit=1
s4-head2-prefix-reading (tikmes)  exit=1     <- the before/after witness fires
```

`summary: 53/53 checks passed`. The trap is closed.

**What remains open is not the pair but its coverage.** The re-anchored pair
still carries no diphthong fixture, so it cannot see the `ai`/`au` axis — and
the D16 seat's own gap line now says so, in words that match this seat's
`X54-F6`/`X54-F7` finding:

> "the delivered syllabifier still disagrees with the packet's own `syllables:`
> field on 2 of 8 name records (gate agrees 6/8): the residual rows are NM-01
> tumhai (declared ['tum', 'hai'], gate ['tum', 'ha', 'i']), NM-05 haitik
> (declared ['hai', 'tik'], gate ['ha', 'i', 'tik']), each of which begins with
> the falling diphthong `ai` that the syllabifier splits as two nuclei"

That is the diphthong gap, named independently by the landing round's own
battery, in the same terms. It is the strongest corroboration of this seat's
central finding, and it comes from the seat that owns the fix.

## 4. X54-F4 — `RL-2`'s conclusion holds; its number does not

`reports/round-26/register/review.md` §4 and `design.md` `RL-2`:

> "`head2` has an **empty proper domain**: 59 of 62 delivered forms are ≤2
> syllables, so `head2(form) == form` is an identity, not a derivation"

Re-measured:

```
forms with >=3 syllables, final.py reading:  3 of 62   [haitun, tumhai, haitik]
forms with >=3 syllables, W2 faithful:       0 of 62   (and 0 of 70 live)
```

The **conclusion is correct and stronger than published**: under the faithful
algorithm the proper domain of `head2` over the delivered tree is empty
**70 of 70**, not 59 of 62. The three forms round 26 names as having a proper
domain (`haitun`, `tumhai`, `haitik`) are exactly the three whose `ai` the
probe double-counted as a nucleus; W3's `['hai','tik']` shows `haitik` is two
syllables, so `head2` is again the identity.

This matters for the round-27 fix, not for the round-26 verdict: the design's
decision to replace `head2` with `lengthen` is **unaffected** — it was right for
a reason the probe measured less precisely than it could have. But the round-27
seat that re-verifies "forms re-verified" must not re-verify against the 3-form
or 15-form surfaces.

## 5. X54-F6 — before/after: the fix landed mid-window and is partial

`before` is the round-26 revision `1ad491a` (the commit at which the published
figures were measured); `after` is the live round-27 working tree.

| | before (`1ad491a`) | after (live tree) |
|---|---|---|
| forms | 62 | 70 |
| `head2` disagreements (W1 vs W2) | **12** | **12** |
| syllable-list disagreements | 62 | 70 |
| forms the gate splits into a non-syllable | 59 | 67 |
| W3 rows | 8 | 8 |
| — W1 (gate) agrees with W3 | **0 / 8** | **0 / 8** |
| — W2 (design) agrees with W3 | **8 / 8** | **8 / 8** |

**`before` and `after` are the same reading on every axis that this claim is
about.** The only difference is the form count (62 → 70, the 8 register forms
round 26 added, all of which are one syllable and so cannot move any of these
counts).

Pinned at the measurement:

```
tools/gates/argot-derivation-gate.py   sha256 5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211
examples/culture-d4/packet.d4.yml      sha256 dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67
reports/round-17/d4/design-language.md sha256 cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc
```

The gate's digest at the first measurement was the **round-25** revision
(`fc13cd2`, the last commit to touch it); `git log --oneline -3 --
tools/gates/argot-derivation-gate.py` showed no round-26 or round-27 commit.

### 5.1 The fix landed mid-window — and it is PARTIAL

At 19:20Z, while this seat was measuring, `tools/gates/argot-derivation-gate.py`
was written in the lane worktree (`git status` → ` M`, +72/−10 lines). The
BEFORE column of this instrument is pinned to the round-26 gate bytes
(transcribed and C7-verified), so it did not drift with the landing; re-running
gives the first true before/after pair of this round:

| | BEFORE — round-26 gate (`5b5abe78…`) | AFTER — live gate (`d7a3ad1a…`) |
|---|---|---|
| forms | 62 | 70 |
| `head2` disagreements (W1 vs W2) | **12** | **3** |
| syllable-list disagreements | 62 | **6** |
| forms the gate splits into a non-syllable | 59 | **0** |
| W3 rows | 8 | 8 |
| — W1 (gate) agrees with W3 | **0 / 8** | **6 / 8** |
| — W2 (design) agrees with W3 | 8 / 8 | 8 / 8 |

The landing is **real and substantial**: the consonant-run / legality half is
fixed. `tikmes` is now `['tik','mes']`, `kalker` is `['kal','ker']`, `ker` is
`['ker']`, `saalumi` is `['saa','lu','mi']` (`head2 saalu`, the design's own
worked row), and **no form is split into a non-syllable any more** (59 → 0).
`is_legal_syllable()` is now in the gate source.

**It is not complete.** The remaining 3 `head2` disagreements are exactly the
three forms whose first nucleus is a **falling diphthong**, and they are the same
two-name failure the packet's witness reports:

```
W3 rows the fixed gate still fails:
  NM-01 tumhai  gate=['tum','ha','i']  packet=['tum','hai']
  NM-05 haitik  gate=['ha','i','tik']  packet=['hai','tik']
  names containing ai/au: ['tumhai','haitik']
```

`VOWELS = frozenset("aeiou")` (`argot-derivation-gate.py:129`) has no diphthong
concept: `hai` is tokenised as two vowel tokens, so it becomes two syllables
`['ha','i']`. The packet's `accent` field declares `ai`/`au` as single "vowel
sequences" and its own `syllables:` field splits `haitik` as `['hai','tik']`, so
the gate's reading is wrong on these forms. `is_legal_syllable('ha')` and
`is_legal_syllable('i')` both return **True**, so the new legality check does not
catch it — the same false-green shape as `X54-F7`.

**Verdict on the claim at this stamp: partially met.** The `after_required` is
"the syllabify disagreement fixed (one algorithm, forms re-verified)". One
algorithm now governs the consonant-run axis; the diphthong axis still has two.
The acceptance surface of §6 check 1 reads **6 of 8**, not 8 of 8.

### 5.2 A reading hazard this seat hit and discloses

At 19:23Z a parallel read of this seat showed the gate back at the round-26
digest `5b5abe78…` with the docstring's legality clause gone — i.e. an apparent
**revert**. It was not a revert: this seat had issued two reads concurrently
while the wave was rewriting six files, and one read landed on a **partially
written file**. The mtimes made it visible — all six paths carried the same
second (`16:23:21`), and a re-read 20 seconds later returned `d7a3ad1a…` and has
returned it on every read since.

The trap is worth recording because the failure is silent and directional: a
peer seat that samples the gate once during a write can conclude the fix was
reverted and file a false finding. The mitigation is the one this instrument
already applies — the BEFORE column reads **pinned git bytes** rather than the
live file, and the live column is read once and reported with its digest, so a
mid-write sample shows up as a digest that matches neither `5b5abe78…` nor a
later stable value, rather than as a confident wrong reading.

The gate settled at `d7a3ad1a6ad1c4c5…` and the packet at
`c5441e3d0b237f33…` (the packet gained the register law during this window,
+76 lines; its own `syllables:` witness is intact through that amendment, so the
acceptance surface of §6 check 1 survives it).

**The gate then moved once more** (19:24Z) to `b5406bcdaf41c595…`, and has held
there since. Re-measured against that second revision: **every number in this
file is unchanged** — `head2` disagreements 3, syllable-list disagreements 6,
non-syllable forms 0, packet witness 6 of 8, and the same three residual rows
(`haitun`, `tumhai`, `haitik`). The second revision is docstring/refactor level
(it tokenises the word, states the syllable template as `CODAS`/`ONSET_CLUSTERS`
constants, and adds `is_legal_syllable`); it does not touch the diphthong axis —
`VOWELS = frozenset("aeiou")` at `argot-derivation-gate.py:129` still has no
diphthong concept, and `is_legal_syllable('i')` still returns `True`. So the
finding stands verbatim against both post-fix revisions.

The **packet** also moved during the window (`dd25077bc01681bc…` →
`c5441e3d0b237f33…` → `86079a6708a0d360…`): the register law and its knowledge
entry were landing. Both files have now **settled** — the settle-poll
(`.scratch/x54/settle2.sh`) reports the gate stable across 4 consecutive minutes
and the packet across 3, and the readings were re-taken after each move. The
packet movement does not disturb this measurement — its `syllables:` witness is
unchanged through the amendment. A verifier should read the digest printed in the
AFTER block rather than the one quoted in this prose.

The settle-poll (`.scratch/x54/settle.sh`) reports stability. If either file
moves again, this section needs a dated refresh — one command, since the
instrument prints both columns and pins both gate digests on every run.

## 6. What a correct fix must satisfy (stated so it can be checked, not prescribed)

This seat does not own the gate and prescribes no implementation. It states the
acceptance surface its own measurements imply, so the landing seat and the round
runner can check it without re-deriving it. Items 3 and 6 are **now met** by the
landed fix (§5.1); items 1 and 2 are **still open**.

1. **One algorithm.** The gate's `syllabify` must reproduce W3 on **8 of 8**
   `names` records. That is a check with an answer fixed by the delivered packet,
   and it reads **6 of 8** after the landing.
2. **The diphthong is one nucleus.** `ai` and `au` are vowel sequences, not two
   syllables (packet `accent` field; packet `NM-05 haitik`). A fix that keeps
   `['ha','i']` will still fail check 1 — and this is precisely where the D
   seat's `sylref.py` (`X54-F7`), the round-26 probes, **and the landed gate**
   all fail. **Check 1 must be the acceptance test, not a self-comparison:**
   `sylref.py` reports 0 head2 disagreements against itself while failing check 1
   on 2 of 8, and the landed gate satisfies the D16 `s1`/`s2` pair while reading
   the same 6 of 8.
3. **Legality is consulted.** *(MET after the landing.)* `onset_clusters: false`
   and the 8 declared codas now enter the split via `is_legal_syllable()`;
   `'kme'`, `'mha'`, `'r'` are no longer emitted. The predicate must **also**
   reject a two-adjacent-vowel nucleus that is not one of the 5 long digraphs or
   2 falling diphthongs — the landed `is_legal_syllable` does not, which is why
   `is_legal_syllable('ha')` and `is_legal_syllable('i')` both return `True` and
   the diphthong gap passes the new check.
4. **`head2`'s proper domain is empty over the delivered tree** (0 of 70), which
   is a *property* of the delivered data and is not changed by any fix. A fix
   that reports a non-empty domain is using a different algorithm.
5. **`head2` is declared-but-unused** by the register design (`rules.md` §3.2),
   so this fix moves **no** delivered finding today. Its value was the
   doc/implementation divergence at the old `argot-derivation-gate.py:136-140`,
   which cited `design-language.md §5` for an algorithm it did not implement.
   **That divergence is now closed for the consonant-run axis** — the landed
   docstring describes the legality rule accurately — and remains open for the
   diphthong, which the gate neither implements nor declares.
6. **The three excess rows** (`sau`, `dau`, `hai`) must not be treated as
   disagreements to fix. *(MET: the landed gate reads `sau`, `dau`, `hai` as one
   syllable each, agreeing with W3, so the round-26 probe's 3 excess rows are
   gone from the disagreement set.)*

**The two acceptance surfaces disagree, and only one discriminates.** The landed
gate satisfies the design's published worked row (`head2(saalumi) = saalu`) and
the D16 reading pair, and still reads 6 of 8 on the packet's witness. A verifier
checking only `saalumi` — or only the D16 pair — will call the fix complete
(`X54-H7`). Check 1 is the discriminating one, because the packet's `syllables:`
field is the only surface that carries the diphthong distinction.

## 7. The instrument and its controls

`reports/round-27/scribe/x54-syllabify-spotcheck.py`:

```
python3 reports/round-27/scribe/x54-syllabify-spotcheck.py            # census, both columns
python3 reports/round-27/scribe/x54-syllabify-spotcheck.py --json     # receipt
python3 reports/round-27/scribe/x54-syllabify-spotcheck.py --selftest # 11 controls
```

```
$ python3 reports/round-27/scribe/x54-syllabify-spotcheck.py --selftest
selftest: 11/11 checks passed
```

The eleven controls, and why each is one:

| # | control | expected |
|---|---|---|
| C1 | the design's **one** published worked row: `saalumi` → `['saa','lu','mi']`, `head2 = saalu` | pass |
| C1b | same, via `head2` | pass |
| C2 | `hai` is **one** syllable (packet `accent` field) | pass |
| C2b | `sau` is **one** syllable | pass |
| C3 | `onset_clusters: false`: `kalker` → `['kal','ker']` | pass |
| C4 | `'kme'` is **not** a legal syllable | pass |
| C4b | `'saa'` **is** a legal syllable | pass |
| C4c | `'r'` alone is **not** a legal syllable | pass |
| C5 | **negative control:** the round-26 probe's `design_syll` must **not** equal W2 on `saalumi` — if these ever coincide, the F2/F3 audit is meaningless | pass |
| C6 | the gate module actually carries a `syllabify` symbol — the measured object is the one named | pass |
| C7 | the round-26 transcription reproduces the pinned round-26 gate bytes on 14 probes — keeps the BEFORE column honest after the wave lands a fix in the live file | pass |

C5 is the load-bearing one: it fails closed if a future round "fixes" the probe
by making it agree with W2, which would silently destroy the evidence for X54-F2
and X54-F3. C4/C4b/C4c test the legality predicate in both directions rather
than only asserting the cases the measurement happens to need. C2/C2b are the
controls that catch the `X54-F7` class: they fail closed on any implementation —
round-26's two probes, the round-27 D seat's `sylref.py`, **or the landed
round-27 gate** — that splits a falling diphthong into two syllables. C7 is what
makes the before/after pair meaningful: it executes the pinned round-26 bytes in
isolation and compares them to the transcription on a probe set covering both
the consonant-run and the diphthong axes, so the BEFORE column cannot silently
become an AFTER column.

The instrument reads **no** scratch and imports **no** round-26 probe: the
round-26 implementations are transcribed *inside* the instrument
(`r26_probe_design_syllabify`, `r26_gate_syllabify`) precisely so the
reproduction is auditable in one file and cannot drift with `.scratch/`, which
is gitignored and erasable. The D seat's `sylref.py` is cited by digest only
(`66e33955…`) and was never imported into the instrument, for the same reason:
scratch is erasable, and a finding must not depend on a file the wave can delete.

## 8. What this seat did not do

- Did not edit the gate, the packet, any component, any pin, any fixture, any
  runner, or any other seat's file. Did not repair the syllabifier — the gate is
  not this seat's file and the claim is another seat's. Did not edit, import or
  execute-and-modify `.scratch/r27-d/sylref.py`; it was read and run as filed.
- Did not adjudicate the round, replay the runner, or read the runner's receipt
  as a verdict. The counting command is `reports/round-27/run-validation.py`;
  this instrument is evidence for it, not a substitute.
- Did not assert that the gate's divergence *fails* any delivered record. It
  does not: no delivered rule is `head2`-scoped. `X54-F5` is a statement about
  the gate's outputs against the packet's legality table, not a finding against
  a delivered packet.
- Did not verify the round-26 **verdict** (`reports/round-26/validation.json`).
  X54-F2/F3/F4 are corrections to round-26 **evidence**, filed as new rows in
  this round's file, never as edits to a filed round-26 artifact.
- Did not file X54-F7 as a defect against the D seats. `.scratch/r27-d/sylref.py`
  is gitignored work-in-progress, the D seats were still writing at this stamp,
  and scratch is not a deliverable. X54-F7 is a warning that the reference the
  fix is being built against fails the packet's own witness — the landing seat
  should adopt check 1 of §6 rather than a self-comparison.
- Did not resolve which of W1/W2 the *gate's docstring* intends. It cites
  `design-language.md §5`, so W2; but a `head2` implementation is not this
  round's deliverable and the round-27 seat owns the choice.

## 9. Receipts

### 9a. BEFORE — the pre-landing reading (round-26 gate bytes, 2026-10-18T19:16:15Z)

Kept because it is the reading that established the defect and because the
digests show the gate had not yet moved.

```
$ python3 reports/round-27/scribe/x54-syllabify-spotcheck.py
X54 syllabify spot-check — 2026-10-18T19:16:15Z
lane HEAD b95fca1e40f32f7346937ab6426f9ccca60e319f
gate 5b5abe7865ed906c  packet(live) dd25077bc01681bc  packet(r26) e7ecd2045ef0e5f9
legality: (C)V(V)(C)  onset_clusters=False  codas=nmsklrtd

== BEFORE — round-26 revision 1ad491a ==
   forms 62 | head2 disagreements 12 | syllable-list disagreements 62
   | forms the gate splits into a non-syllable 59
   W3 (packet's own `syllables:`) on 8 name records: W1 agrees 0/8, W2 agrees 8/8
== AFTER — round-27 live tree ==
   forms 70 | head2 disagreements 12 | syllable-list disagreements 70
   | forms the gate splits into a non-syllable 67
   W3 (packet's own `syllables:`) on 8 name records: W1 agrees 0/8, W2 agrees 8/8

published r26 figure vs this seat's re-derivation:
   published:            15 of 62
   probe impl re-run:    15 of 62
   W2 (design prose):    12 of 62
```

### 9b. AFTER — the settled reading (2026-10-18T19:23Z, fix landed)

The BEFORE column now reads the **pinned round-26 gate bytes** (transcribed,
C7-verified) rather than the live file, so the pair below is the round's first
true before/after. Both digests are printed on every run.

```
$ python3 reports/round-27/scribe/x54-syllabify-spotcheck.py
X54 syllabify spot-check — 2026-10-18T19:23:06Z
lane HEAD b95fca1e40f32f7346937ab6426f9ccca60e319f
gate(live) d7a3ad1a6ad1c4c5  gate(r26) 5b5abe7865ed906c
packet(live) c5441e3d0b237f33  packet(r26) e7ecd2045ef0e5f9
legality: (C)V(V)(C)  onset_clusters=False  codas=nmsklrtd

NOTE: BEFORE reads the round-26 GATE BYTES (transcribed from b95fca1, C7-verified);
      AFTER reads the live gate. When the digests above differ, the fix has landed.

== BEFORE — round-26 revision 1ad491a (round-26 gate bytes) ==
   forms 62 | head2 disagreements 12 | syllable-list disagreements 62
   | forms the gate splits into a non-syllable 59
   W3 (packet's own `syllables:`) on 8 name records: W1 agrees 0/8, W2 agrees 8/8
== AFTER — round-27 live tree (live gate, fix landed) ==
   forms 70 | head2 disagreements 3 | syllable-list disagreements 6
   | forms the gate splits into a non-syllable 0
   W3 (packet's own `syllables:`) on 8 name records: W1 agrees 6/8, W2 agrees 8/8

head2 disagreements, AFTER (the rows that matter for the declared op):
   L-48   haitun    gate=hai     design=haitun
   NM-01  tumhai    gate=tumha   design=tumhai
   NM-05  haitik    gate=hai     design=haitik

published r26 figure vs this seat's re-derivation (round-26 gate bytes):
   published:            15 of 62
   probe impl re-run:    15 of 62
   W2 (design prose):    12 of 62
```

```
$ python3 reports/round-27/scribe/x54-syllabify-spotcheck.py --selftest
selftest: 11/11 checks passed            (exit 0)
```

```
$ python3 reports/round-27/scribe/x54-syllabify-spotcheck.py     # 2026-10-18T19:21Z
X54 syllabify spot-check — 2026-10-18T19:21:19Z
lane HEAD b95fca1e40f32f7346937ab6426f9ccca60e319f
gate(live) d7a3ad1a6ad1c4c5  gate(r26) 5b5abe7865ed906c
packet(live) dd25077bc01681bc  packet(r26) e7ecd2045ef0e5f9
legality: (C)V(V)(C)  onset_clusters=False  codas=nmsklrtd

== BEFORE — round-26 revision 1ad491a (round-26 gate bytes) ==
   forms 62 | head2 disagreements 12 | syllable-list disagreements 62
   | forms the gate splits into a non-syllable 59
   W3 (packet's own `syllables:`) on 8 name records: W1 agrees 0/8, W2 agrees 8/8
== AFTER — round-27 live tree (live gate, fix landed) ==
   forms 70 | head2 disagreements 3 | syllable-list disagreements 6
   | forms the gate splits into a non-syllable 0
   W3 (packet's own `syllables:`) on 8 name records: W1 agrees 6/8, W2 agrees 8/8

head2 disagreements, AFTER (the rows that matter for the declared op):
   L-48   haitun    gate=hai     design=haitun
   NM-01  tumhai    gate=tumha   design=tumhai
   NM-05  haitik    gate=hai     design=haitik

published r26 figure vs this seat's re-derivation (round-26 gate bytes):
   published:            15 of 62
   probe impl re-run:    15 of 62
   W2 (design prose):    12 of 62
```

Counts above carry their command and date; every pin is a sha256 of the live
bytes; every fix named in §6 carries the control in §7 that would catch it.

Every number asserted in this file was re-verified by an independent
re-derivation pass. The BEFORE column was verified against the pinned round-26
gate bytes, and the AFTER column against the live gate:

```
BEFORE (round-26 gate bytes, 62 forms)
    forms 62                          PASS
    head2 disagreements 12            PASS
    non-syllable forms 59             PASS
    syllable-list disagreements 62    PASS
    W2 agrees W3 8/8                  PASS
    W1 agrees W3 0/8                  PASS
    probe impl re-run 15 of 62        PASS
    W2 12 of 62                       PASS
    >=3 syllables, faithful, r26 0    PASS
F7  sylref W3 agreement 6/8           PASS
F7  sylref vs W2 syllable-list 6      PASS
F7  sylref licensed('hai') True       PASS
AFTER (live gate, 70 forms)
    head2 disagreements 3             PASS
    non-syllable forms 0              PASS
    syllable-list disagreements 6     PASS
    W1 agrees W3 6/8                  PASS
    >=3 syllables, faithful, live 0   PASS
    gate vs sylref head2 (round-26 gate) 70  PASS
pins gate-r26 / gate-live / packet-live / packet-r26 / design  PASS (5/5)
```

## 10. Named holds

| id | hold | owner |
|---|---|---|
| **X54-H1** | the syllabify leg of claim D **landed partially** mid-window (`d7a3ad1a…`): the consonant-run/legality axis is fixed (non-syllable forms 59 → 0), the **diphthong** axis is not (`hai` still two syllables; packet witness 6 of 8, not 8 of 8). The claim's `after_required` ("one algorithm") is met on one axis only | D seats / parent |
| **X54-H2** | the published round-26 figures (`15 of 62`, `59 of 62`, `3 of 62`) are **not** measurements of the algorithm they name; a round-27 verification must not be run against them | D seats / round-27 runner |
| **X54-H3** | the packet's `syllables:` field is an author-declared witness on 8 forms and is cited by no filed round-8–26 artifact; it should become the acceptance check for any syllabifier fix — **partially adopted by the D16 seat's runner during this window** (§3c), and it is the check that catches the remaining diphthong gap (6 of 8) | parent |
| **X54-H4** | `argot-derivation-gate.py` now implements the design's legality clause (its docstring at :141-160 describes the consonant-run rule accurately), so the round-26 doc/implementation divergence is **closed for that axis**; the diphthong clause is still undeclared — `VOWELS` at :119 has no diphthong concept while the packet's `accent` field declares `ai`/`au` as single vowel sequences | D seats |
| **X54-H5** | the round-27 D seat's in-flight reference `.scratch/r27-d/sylref.py` (`66e33955…`) fails the packet's declared syllables on 2 of 8 names and its self-comparison reports 0 head2 disagreements against a real divergence of 12; the landed gate inherits the same diphthong defect, which is why the packet witness — not a self-comparison — must be the acceptance test | D seats / landing seat |
| **X54-H6** | the D16 seat's re-anchored reading pair (`tumkalker`) now discriminates correctly and is honest about being "whichever side the fix lands on" — but it **still carries no diphthong fixture**, so it cannot see the `ai`/`au` axis. The landed gate satisfies the pair and still reads **6 of 8** on the packet's witness. The pair needs a diphthong fixture (`hai`, `tumhai`), or check 1 of §6 as a third leg | D16 seat |
| **X54-H7** | the landed fix satisfies the design's published worked row (`head2(saalumi) = saalu`) and leaves the packet's witness at 6 of 8 — the two acceptance surfaces **disagree**, and only the packet's field discriminates. A verifier that checks only `saalumi` will call the fix complete | round-27 runner |
