# RevBaseCensus — independent re-derivation of the claim-C base census

Seat: `L1-kotodama-r66.RevBaseCensus` (reviewer, coverage). Round 66 / hyaku 5 / v2 wave.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Read-only on the lane: no git/jj writes, no commits, no mutation of `corpus/` or jj state.
Installs/upgrades this seat: **none**.

## 0. Tree identity (what the census actually measured)

```
HEAD   = 94209e8   (short)
main   = 94209e8
base   = 94209e8f80969dbac48d56c5d0e2e623635b8616   (claims.json .base)
git status --porcelain -- corpus/  ->  <empty>
```

All three are the same commit and `corpus/` has no uncommitted change, so the census below
measures the *declared base tree*, not a dirty worktree. Caveat, stated plainly: this is a
**committed-tree** census. Drafts under `.ufo/waves/round-66/` (the not-yet-landed entry) are
correctly invisible to it; nothing in this report should be read as a statement about the draft.

Base totals recovered independently (not read from the claim):

| quantity | source | value |
|---|---|---|
| `corpus/knowledge` `.md` files | `git ls-tree -r --name-only BASE -- corpus/knowledge` | **239** |
| `corpus/knowledge/culture-material` files | same, narrower path | **32** |
| `corpus/README.md` index bullets (`` - `x.md` — ``) | `git show BASE:corpus/README.md` | **239** |
| README `## culture-material` bullets | section slice | **32** |
| distinct `S\d{3}` ids in `corpus/SOURCES.md` | `grep -oE '\bS[0-9]{3}\b' \| sort -u` | **701** |
| highest id at base | same | **S775** |
| occurrences of `S777`–`S800` at base | `grep -cE '\bS77[7-9]\b\|\bS78[0-9]\b\|\bS800\b'` | **0** |

So `239 -> 240` and `32 -> 33` are sound, the registry base count `701` is sound, and
`S777–S800` are genuinely unoccupied new ids. `S776` is **also absent at base** (max is
`S775`) — see MED-2.

## 1. The required three totals (scent filename pattern, at base)

All three run against `git ls-tree -r --name-only 94209e8… -- corpus/knowledge` (239 paths).

| # | variant | pattern | total |
|---|---|---|---|
| V1 | **word-bounded** (the claim's predicate, verbatim) | `(^\|[^a-z])(scent\|perfume\|aromatic\|incense\|fragran\|cosmetic\|unguent)([^a-z]\|$)` | **0** |
| V2 | **raw substring**, same stems truncated | `scent\|perfum\|aromat\|incens\|fragran\|cosmetic\|unguent` | **0** |
| V3 | **raw substring, widened** to adjacent/peripheral stems | V2 + `aroma\|attar\|balsam\|myrrh\|frankincens\|sandalwood\|musk\|distill\|hydrosol\|enfleur\|balm\|salve\|resin\|spice\|amber\|camphor\|odou?r\|smell` | **0** |

**The claim's predicate reproduces at 0. It also holds under both weaker/looser censuses**, so
the `0` is not an artifact of word-bounding or of stem choice — there is no filename in
`corpus/knowledge` at base carrying this register under any spelling I tried.

Positive control (proves the mechanism can match, not a silently-empty pipe):
`(textile|textiles|cloth|weav)` word-bounded on the same path → **1** (`textile-technology.md`).

### 1a. The raw-substring variant is a false-positive generator on *body text*

Worth recording because it justifies the claim's design choice rather than merely permitting it.
Running V2's stems word-unbounded over the **body** of all 239 files:

- **124 of 239** files match raw; only **2** files have ≥10 hits.
- Both top raw scorers with ~0 word-bounded hits are pure artifacts, e.g.
  `linguistics/kinship-terminology.md` raw=12 / word-bounded=**0** — the match is
  *ado**lescent***; `civilizations/japan-yayoi-kofun.md` raw=9 / word-bounded=0 — same class.

The claim picked *filename scope* + *word boundaries*. Had it picked raw-substring body text,
its own predicate would have printed ~124 and failed on noise. The choice is load-bearing and
correct.

## 2. Adjacent-register census — `dye|pigment|paint|soap` (is an unowned neighbour skipped?)

Filenames, at base:

| variant | total |
|---|---|
| word-bounded `(dye\|dyes\|dyeing\|pigment\|pigments\|paint\|paints\|painting\|soap\|soaps\|saponif)` | **0** |
| raw substring `dye\|pigment\|paint\|soap` | **0** |

So **no adjacent register is owned at filename level either** — the base has zero filename
owners for soap and pigment just as for scent. That is *not* a defect in claim C (C creates one
scent entry and makes no claim about soap), but the honest reading is: these neighbours are
owned **topically or not at all**, and the thing that distinguishes scent from them is topical
ownership, not filenames. Topic-line (`- topic:`) scan at base:

| adjacent register | topic-line owner(s) at base | verdict |
|---|---|---|
| `dye` | `textile-technology.md` ("dye chemistry, fastness classes, and prestige trade (Tyrian purple, indigo vs woad, madder, kermes vs cochineal, fugitive yellows)"); also `dress-through-eras.md`, `ritual-garments.md`, `linguistics/color-terminology.md`, `myth-symbol/color-symbolism.md` | **owned** |
| `soap` | `bathing-and-body-hygiene.md` (`- topic:` contains `soap`; 24 word-bounded body hits) | **owned** |
| `pigment` | `adornment-body-codes.md` (`- topic:` contains `pigment`) + the two colour entries | **owned** |
| `paint`/`painting` | **none** — 0 topic-line owners; 54 word-bounded body hits spread over ~25 civilization entries | **no owner** (see LOW-4) |
| `unguent`/`ointment`/`salve` | **none** — only 1 body hit total (`civilizations/kongo-kingdom.md`) | **no owner** |

Conclusion for the assigned question: **no adjacent unowned register is being silently skipped
by the round's scope** — `dye`, `soap`, `pigment` all have topic-line owners; the two without
owners (`paint`/`painting`, `unguent`) are recorded below at LOW severity rather than as
scope-skip defects. Note `unguent` is one of the *seven stems in the claim's own census pattern*
yet has no base owner anywhere — that stem belongs to the new entry's scope and is unowned, which
supports rather than weakens C.

## 3. Findings

### MED-1 — the claim's supporting clause is false for the `cosmetic` stem: that register has a whole-section owner

Claim C's parenthetical support reads: *"topic-line keyword sweep finds only partial-scope
mentions, not whole-register owners"*. That is accurate for `scent` (1 partial hit:
`craft-artisan-lexicon.md` uses *nioi* "scent" as a sword-tempering term), for `incense`
(`timekeeping-instruments.md`, one sub-family: "FIRE: calibrated candle, lamp and incense
measures"), and for `unguent` (no owner). It is **not** accurate for `cosmetic`, which is one of
the seven stems in C's own census pattern:

`corpus/knowledge/culture-material/adornment-body-codes.md` at base —
`- topic:` line contains `cosmetics`; H1 is "*… Cosmetic Vocabulary …*"; and **H2 §6 is titled
`## 6. Cosmetics and their vocabulary`** carrying **11** word-bounded scent-register hits.
Per-section counts (word-bounded, all seven stems):

```
 7  (preamble: H1 + topic + sources + couples)
11  ## 6. Cosmetics and their vocabulary
 2  ## 8. Calibration
 1  ## 9. Applying it to a fictional culture
21  total
```

That is a whole-register owner of cosmetics, not a partial mention. The predicate is unaffected
(it is filename-scoped, and including more stems can only make a `0` harder to obtain, so the
`0` remains conservative). The risk this creates is on the *other* side:
`adornment-body-codes.md` §6 already teaches the exact craft rule the scent entry is most likely
to reach for — "*build each culture's cosmetic lexicon in four strata — material word,
applicator/tool word, occasion word, and moral slur*" (§6, closing bullet). If the new
`scent-perfume-aromatics-codes.md` restates that four-strata construction for perfumery, the
round ships duplicate coverage while citing "*unowned register*" as its justification.
**Action for L1:** either scope the statement to `scent|perfume|aromatic|incense|fragran|unguent`
and drop `cosmetic`, or have the entry explicitly couple to `adornment-body-codes.md §6` as the
cosmetic owner (the corpus convention is a `- couples:` line, which is how that file already
points at `sumptuary-law-rank-display.md` and `ritual-garments.md`).

### MED-2 — nothing in ACCEPT-C-66 enforces "exactly 24" or "701 → 725+"; and S776 has no owning leg

Three separate gaps in the instrument, all reachable by a draft that legally passes:

1. `accept-c.py:50` is `NEW_IDS = [f"S{n}" for n in range(777, 801)]` — a **fixed 24-id list**.
   `SET` and `ROWS` iterate only that list, so the 24 rows are checked but the *registry delta*
   is not.
2. The `APPEND` leg (`accept-c.py:271-278`) is
   `missing_old = [l for l in base_set if l not in tip_set]; append_ok = len(missing_old) == 0`.
   `appended` is computed and **printed only** (`f"missing_old={len(missing_old)} appended={len(appended)}"`)
   — never asserted. Ten extra mined rows appended alongside S777–S800 leave APPEND green.
3. Consequently the statement's arithmetic "*registry 701 -> 725+ rows*" is **unfalsifiable by
   its own counter**. Verified base arithmetic: 701 ids, max `S775`, `S776` **absent**. The
   `725+` hedge is correct only if `S776` is added (24 + 1 = 726); if only `S777–S800` land, the
   total is 725 and Ca's D1 leg ("the games entry cites S776 exactly once for the mancala
   bullet") cannot pass. `S776` is required by **Ca** but is a registry row in `corpus/SOURCES.md`,
   which is a **C** land (Ca's lands list does *not* include `corpus/SOURCES.md`). So the
   `C → Ca` registry dependency exists and is **undeclared** in `claims.json.separability`, whose
   note asserts "*No C→O, C→Ca, … dependency is declared; any such finding is a real defect*".
   That is exactly this case.

**Action for L1:** (a) add an `APPEND` count assertion, or a `COUNT` leg pinning
`len(appended) == 25` (24 + S776); (b) declare the `C → Ca` dependency on `S776` in the
separability note, or move `S776`'s row into Ca's lands; (c) state the expected final total as a
number (726), not `725+`.

### LOW-3 — the census defines the register with 7 stems; no leg checks the entry covers them

C counts `cosmetic` and `unguent` as register stems, but names the artefact
`scent-perfume-aromatics-codes.md`. None of the 13 legs asserts that the entry actually covers
`incense` or `unguent`. An entry that discusses only perfume passes `FILE`/`SET`/`ROWS`/`ONEID`/
`RESTATE`/`HOSTS`/`LINK`/`APPEND`/`NOHARM`/`SWEEP`/`CAPTURE`/`TOPIC` intact. Given that base has
**no** `unguent` owner and only a 5-hit partial for `incense`, an entry titled aromatics that
omits incense would land a coverage claim with a hole in it. **Action:** require at least one
bullet whose anchor quote matches `incense` and one matching `unguent` (both unowned/partial at
base), or reduce the title/stems to what the entry actually treats.

### LOW-4 — `paint`/`painting` and `unguent` have no topic-line owner at base

Recorded for completeness of the adjacent census. `painting` has 54 word-bounded body hits
concentrated in civilization entries (`india-mughal.md` 18, `levant-canaan-phoenician.md` 12,
`japan-heian.md` 9, `aegean-minoan-mycenaean.md`, `etruria.md`, `moche.md`, `newar-nepal.md`) but
zero topic-line owners; `paint` bodies are mostly "painted" as an adornment/moral-slur word.
This is plausibly out of this corpus's material-culture scope (the register is art-historical,
and `writing-media-surface-economy.md` / `cartography-and-mapmaking.md` touch it only
incidentally), so I am **not** calling it a scope skip. Flagging only so the L1 rules on it
knowingly rather than by omission.

### INFO-5 — verified clean, no action

- Base `0` reproduces under all three required census variants and both adjacent-register
  variants; positive control returns 1.
- `239`/`32`/`239`/`701` all re-derived from the tree, matching the claim.
- Core scent register (excluding `cosmetic`/`unguent`) across `culture-material` bodies totals
  only **16 hits over 7 files**, max `timekeeping-instruments.md` at 5 — genuinely unowned, so
  the "new entry, not a split" premise holds for the *scent* half of the register.
- Base `corpus/README.md` index bullets == `culture-material` bullet count == knowledge file
  count is self-consistent, so `SWEEP`'s rows==files invariant has a clean base to move from.

## 4. Residual risk

- **Not covered here:** the 24 rows themselves (tiers, hosts, captures, anchor quotes) and the
  draft entry's body — other seats. This report is base-tree and instrument only.
- The `accepted`/`rejected` question of whether a *new* entry is the right instrument versus
  extending `adornment-body-codes.md` §6 is a judgment I did not make; MED-1 is the input to it.
- `COUPLING` risk not measured: I did not scan for the scent entry's likely `- couples:` targets
  to detect a cycle or a missing back-link. `adornment-body-codes.md` is the obvious mutual
  coupling and currently would point one way.
- I ran no counter (`accept-c.py`, `accept-o.py`, `accept-ca.py`) — per role, verification after
  integration is main's, and none of them can be meaningful against a base tree anyway.
- Topic-line scans for the scent register were limited to `culture-material/`; the body-density
  scan covered all 239 files, so no whole-register owner is hiding outside that directory: the
  highest word-bounded scent density outside `culture-material` is **3**, in
  `myth-symbol/color-symbolism.md`; next are `civilizations/japan-heian.md` and
  `civilizations/india-tamil-sangam.md` at **2**. Everything above that is inside
  `culture-material` (`adornment-body-codes.md` 20, `vessel-container-lexicon.md` 6,
  `timekeeping-instruments.md` 5, `funerary-material-culture.md` 4).
