# ScoutPartialOwners — scent-adjacent partial owners, r66 w1

Seat: scout (leaf). Question: which of the five named scent-adjacent corpus
entries actually carry scent/perfume/incense/aromatics, and which slice does the
new `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` cite
one-way from each. All paths below are lane-relative
(`/home/vgpnk/Projects/shokunin/kotodama-shokunin/`). Verified at lane tip by
word-boundary grep (`scent|perfume|incense|aromatic|fragran|odor|odour|smell|
stench|musk|myrrh|frankincense|ambergris|camphor|civet|castoreum|pomade|unguent|
sandalwood|cosmetic|kohl|henna|resin|balm|anoint`); all five files read at the
hit lines. LSP not applicable (Markdown corpus, no server).

## Per-file verdicts

### 1. corpus/knowledge/culture-material/bathing-and-body-hygiene.md — PARTIAL OWNER (washing-removal boundary)

Line where scent appears (the only literal `scent` token in the file, :7 couples):

> `corpus/knowledge/culture-material/adornment-body-codes.md` (that entry owns the
> *adorned* surface — paint, scent, hair; this entry owns the *washing regime*
> beneath it, and the boundary is where a purity mark is applied after a bath)

Adjacent smell tokens: :59 "the night-soil trade, and the urban stench"; :67
"the smell map of the city". The kit rows own the removal side (:24 "oil +
strigil, **not soap**"; :80–81 soap chemistry and the non-soap kit).

Slice the new entry cites one-way: the washing regime that *removes* scent —
oil+strigil, soap, the bath sequence — and the explicit boundary rule "a purity
mark is applied after a bath". Bathing owns the body *before/beneath* scent;
it never owns applied aromatics. Note: its claim that adornment owns "paint,
scent, hair" is a **delegation, not a delivery** — see §3.

### 2. corpus/knowledge/culture-material/fire-fuel-light.md — PARTIAL OWNER (combustion-smell rank code)

Section header :62: "## 4. Light: what burns, what it smells like, and who can
afford it". The load-bearing line (:76):

> **Craft rule (smell is a rank code).** Tallow's rancid smoke versus beeswax's
> sweetness is a *legible* difference at a distance — the cheapest possible way
> to stage rank in a scene without a single line of exposition. Couple
> `culture-material/sumptuary-law-rank-display.md` (who may burn what) and
> `culture-material/costume-semiotics.md` (what a smell tells a visitor).

Supporting rows: :67 tallow "rancid smoke … the smell is the tell"; :68 beeswax
"bright, sweet-smelling"; :38 coal "a willingness to smell sulphur"; :130 build
order "what burns for light, what it smells like". No `incense` token anywhere —
fire-fuel-light does **not** own incense.

Slice the new entry cites one-way: burn-smell as a legible rank code (tallow vs
beeswax vs oil smoke) — the *fuel* aromatics boundary. Perfume/incense-as-worn-
or-offered aromatics is outside it; the entry inherits its "smell is readable
at a distance" craft rule but must not restate the fuel rows.

### 3. corpus/knowledge/culture-material/adornment-body-codes.md — PARTIAL OWNER (cosmetic lexicon method; scent register ABSENT)

No literal `scent`/`perfume`/`unguent`/`pomade` token exists in the file — the
nearest scent-bearing line is the §6 craft rule (:75):

> **Craft rule**: build each culture's cosmetic lexicon in four strata —
> material word (kohl, ceruse), applicator/tool word (palette, brush, mirror
> case), occasion word (the bridal application, the mourning removal), and moral
> slur ("painted"). The strata date your scenes: a character who says the slur
> is telling you her era and faction.

§6 (:68–75) owns cosmetics vocabulary (kohl→alcohol etymology, cerussa/fucus,
oshiroi/ohaguro, sindoor) and the moral-register war on "paint" (:72). Word "oil"
appears only at :49 as a scarification irritant — unrelated.

**Finding for the new entry:** bathing :7 asserts adornment "owns the adorned
surface — paint, scent, hair", but adornment itself never carries scent — the
attribution is one-directional and orphaned. The scent register the bathing entry
thought was covered is exactly the gap scent-perfume-aromatics-codes fills. Cite
adornment one-way for: the body-surface boundary (scent sits on the adorned
surface, per bathing's boundary rule) and the four-strata lexicon method, which
transfers directly to perfume vocabulary (material / applicator / occasion /
moral slur).

### 4. corpus/knowledge/myth-symbol/animal-symbolism.md — INCIDENTAL (no scent content)

No genuine scent token. Every regex hit was a substring false positive:
`de**scent**` at :41 ("descent group ↔ species name") and :55 ("**Descent
animals:** the Göktürks traced descent to a she-wolf"), and `em**balm**` inside
"emblem". Zero hits for civet, musk, castoreum, ambergris — even though the
musk-deer, civet and ambergris-whale are the canonical perfume animals.

Verdict: incidental mention (effectively absent). The new entry should cite it
one-way *only* if it needs the animal-symbol register behind an aromatic source
(musk/civet/ambergris as animal products) — and should note that no existing
entry owns animal-derived aromatics.

### 5. corpus/knowledge/culture-material/timekeeping-instruments.md — PARTIAL OWNER (incense as consumable timer)

Line where scent appears (the functional row, :26, FIRE instrument family):

> | FIRE | a known burn rate of a consumable measures elapsed time | calibrated
> candles (…), oil lamps with graduated reservoirs, **incense sticks and
> seal-stamps (Bedini 1994)**, rope fuse | coarse: tens of minutes; … | draft,
> humidity, fuel quality, and the fact that it is consumed | almost nothing:
> ash, lamp metal, holder ceramics — the *consumable* is the timekeeper |

Also :3 topic ("FIRE: calibrated candle, lamp and incense measures"), :5 source
(Bedini 1994 *The Trail of Time: Time Measurement with Incense in East Asia*),
:86 ("candles, incense … do not survive").

Slice the new entry cites one-way: incense owned purely as a *burn-rate
consumable* — sticks and seal-stamps as clocks, with the survival-bias caveat.
Aromatics, compounding and the perfumer's trade are outside it. This is the only
file of the five where `incense` itself is owned content.

## Summary for the entry's couples line

- One-way cite targets (partial owners): **timekeeping-instruments** (incense
  clock slice, :26), **fire-fuel-light** (burn-smell rank code, §4/:76),
  **adornment-body-codes** (adorned-surface boundary + four-strata lexicon
  method, §6/:75), **bathing-and-body-hygiene** (scent-removal/washing regime,
  :7 boundary).
- **animal-symbolism**: incidental only — no owned slice; cite at most for
  perfume-animal symbolism backdrop.
- **Gap confirmed**: no entry owns applied/worn/offerred aromatics; bathing :7's
  "adornment owns scent" is an orphaned delegation the new entry absorbs.
- Direction check: all four partial owners are one-way targets — none of the
  five files cites `scent-perfume-aromatics-codes.md` (it does not yet exist on
  disk at this tip), and none needs a back-reference for the claim to hold.

Confidence: high — full-corpus word-boundary grep plus line-level reads; the
false-positive analysis (descent/emblem) is mechanical and reproducible.
No installs. No blockers.
