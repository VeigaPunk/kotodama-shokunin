# RevClaimC — attack on claim C's declared gap (scent register "unowned at base")

Seat: reviewer (leaf), round 66 / w1. Target: `reports/round-66/claims.json` claim C,
`reports/round-66/accept-c.py`, `reports/round-66/telemetry/{census-start,controls-c,dry-run-c}.txt`.
Read-only git only; no lane/jj/git state touched; no files written outside this report.
LSP: not applicable — the artefacts under test are Markdown corpus files and a Python
counter with no configured language server; every "no server answered" claim below is
recorded as such and all searches are literal/word-bounded text (not semantic proof).

Assignment: re-derive the base filename census, run the topic-line sweep, name every
base file that would argue the register is already held, and say loudly whether
"0 owners" is reachable on a technicality.

## Verdict

The **numeric** premise reproduces exactly. The **instrument and its evidence do not
survive**: the census is one-sided by construction, no leg of ACCEPT-C-66 re-derives it,
and the file named as the census receipt is a different artefact. "0 owners" is a
contingent truth about this base, not a robust finding — and it is unfalsifiable by the
frozen predicate.

| # | Severity | Finding |
|---|---|---|
| F1 | HIGH | No ACCEPT-C-66 leg re-derives the ownership census (pre or post). "0 owners" is prose-only; a do-nothing tree cannot fail it. |
| F2 | HIGH | `telemetry/census-start.txt` is not a census receipt — it is a W04 duplicate-URL audit. The premise has no on-disk evidence. |
| F3 | MED (loud) | The word-bounded regex misses plural/derived forms; 6 of 8 "obvious owner" filenames score 0. The new entry survives only on its `scent-` token. |
| F4 | MED | 22 base files carry word-bounded register tokens (partial owners); a 23rd carries only the plural form. One of them, `bathing-and-body-hygiene.md:7`, states in-corpus that another entry *owns scent*. Named per file below. |
| F5 | MED | Id-space bypass: `NEW_IDS` is hard-pinned to S777–S800 while S776 (Ca's row) is free at base; a 23-row + S776/S753 citation mix passes every C leg. |
| F6 | LOW | No post-state assertion: after landing the census should print exactly 1; nothing checks it, and a second (duplicate) owner would also pass. |

## F1 — HIGH: the census is not in the counter

`accept-c.py` constants (`:43-49`) and leg list (`:156,159,190,214,222,248,257,269,277,287,298,311,324`):

```
BASE/GAMES_ENTRY/REGISTRY/SWEEP/README/NEW_IDS = range(777,801)
legs: FILE SET ROWS ONEID RESTATE HOSTS LINK APPEND NOHARM SWEEP CAPTURE TOPIC
```

- `grep -n "census\|ls-tree\|owner\|grep -ciE" reports/round-66/accept-c.py` → only the
  docstring line 4 and `ENTRY` on line 45. No subprocess runs `git ls-tree`, and no leg
  is named CENSUS/OWNER.
- The `SWEEP` leg (`:290-298`) is `reports/round-28/readme/sweep.py` — registry-rows vs
  files vs README topic-line consistency. It is **not** the claim's topic-line keyword
  sweep and says nothing about register ownership.
- `claims.json` leg list has the same 12 legs; the statement's parenthetical is the only
  place the census command and the `0` appear.

Consequence: the claim's declared gap ("unowned at base") is asserted, never verified.
A do-nothing control cannot fail it — `controls-c.txt` itself lists the failing legs
(FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC) and none of them is the premise. The
frozen-predicate rule ("a counter a do-nothing control passes is revised") therefore
does not reach the premise at all.

## F2 — HIGH: `census-start.txt` does not contain the census

```
cat -n reports/round-66/telemetry/census-start.txt   # 28 lines, 3200 B
  1  kotodama W04 S127 duplicate url voices.uchicago.edu/... across scopes
 ...
 27  kotodama W04 S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
 28  kotodama     ok     /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
grep -niE 'census|grep|ls-tree|scent|perfum|aromat|incens|owner' census-start.txt  -> exit 1 (no match)
```

The file is a W04 duplicate-URL audit of S127–S651 (27 rows) plus one `ok` line for
SOURCES.md. It records neither the census command, nor `239`, nor `0`, nor the
topic-line sweep. Citing it as the base census receipt is a false stamp of exactly the
class this round is auditing; the round-66 record should either re-run the census into a
named receipt or drop the receipt claim.

## F3 — MED, loud: "0 owners" is reachable on a word-boundary technicality

Exact claim regex (from `claims.json`, verbatim):

```
git ls-tree -r --name-only 94209e8f... -- corpus/knowledge \
  | grep -ciE '(^|[^a-z])(scent|perfume|aromatic|incense|fragran|cosmetic|unguent)([^a-z]|$)'
```

Re-derived: **0** (exit 1), over **239** files, **32** under `culture-material/`. The
claim's `239 -> 240` and `32 -> 33` counters are correct.

But the same regex applied to filenames that plainly own the register returns 0, because
the trailing `([^a-z]|$)` demands the stem end at a non-letter (probe run on stdin, no
files written):

```
aromatics-lexicon.md             -> 0     # 'aromatic'+'s'
perfumery-and-trade.md           -> 0     # 'perfume'+'r' (and 'perfum'+'ery')
cosmetics-and-unguents.md        -> 0     # 'cosmetic'+'s' AND 'unguent'+'s'
fragrance-codes.md               -> 0     # 'fragran'+'c'
scented-oils.md                  -> 0     # 'scent'+'e'
unguents-of-antiquity.md         -> 0     # 'unguent'+'s'
incense-trade.md                 -> 1     # bare singular before '-'
scent-codes.md                   -> 1
```

Stem morphology: 6 of the 7 stems miss every inflected/derived English form —
`scented/scenting`, `perfumes/perfumery`, `aromatics`, `cosmetics`, `unguents`,
`fragrance/fragrant` (`fragran` matches *no* word-final English token at all; it can only
fire as `fragran-`). `incenses` also misses.

Loudest consequence: the round's own entry name passes only because of its prefix —
`perfume-aromatics-codes.md` would score 0, and `scent-perfume-aromatics-codes.md` is
counted as **one** owner by the leading `scent-` alone. So the census cannot distinguish
"register unowned" from "register owned by a file whose only token is plural/derived".

In fairness: the boundary discipline is not gratuitous — unbounded `scent` matches 112
base files, overwhelmingly `descent`/`ascent`; the claim's regex correctly rejects those.
The defect is that the guard is one-sided: `0` is an **upper bound on owners**, and the
claim states it as absence. Any re-statement of this premise should either add the
inflected stems (`scent(s|ed|ing)?|perfum(e|es|ery)|aromatic(s)?|incense(s)?|fragran(t|ce|ces)?|cosmetic(s)?|unguent(s)?`)
or be worded "no base filename carries the register under the singular-token census".

## F4 — MED: every base file that would argue the register is already held

Word-bounded body sweep at base (`git grep -ciE` same stems, whole `corpus/knowledge`):
**22 files** carry ≥1 token; a 23rd (`masks-masquerade.md`) carries only the plural
`cosmetics` and therefore scores 0 under the claim's own regex — a realized instance of
the F3 miss class, listed last in the table. Per file, with the distinct token(s) that
matched:

| file (base) | lines | matched token(s) | what it actually holds |
|---|---|---|---|
| `culture-material/adornment-body-codes.md` | 7 | `cosmetic` ×7 | H2 "…Tattoo and Scar Systems, Hair Politics, **Cosmetic Vocabulary**…"; :3 "cosmetics is a vocabulary before it is a pigment (Egyptian kohl → Arabic *al-k…)". Holds the **cosmetic/applicator lexicon**, not perfume/incense systems. |
| `culture-material/timekeeping-instruments.md` | 5 | `incense` ×5 | "FIRE: calibrated candle, lamp and **incense** measures"; :5 cites Bedini (1994) *The Trail of Time: Time Measurement with Incense in East Asia*; :26 "incense sticks and seal-stamps". Real slice: **incense-as-timekeeping**. |
| `culture-material/vessel-container-lexicon.md` | 5 | `cosmetic` ×4, `perfume` ×1 | :38 "**cosmetic/perfume** (Greek *alabastron*, *aryballos*; the kohl pot…)"; :3 "ritual/cosmetic/funerary extensions". Holds **perfume-container typology**. |
| `culture-material/funerary-material-culture.md` | 3 | `cosmetic` ×3 | :75 "build the **cosmetic lexicon** in four strata: material word, applicator word, occasion word…"; :11 grave-assemblage method. Holds **grave-goods cosmetic method**. |
| `culture-material/craft-artisan-lexicon.md` | 3 | `scent` ×3 | "nioi 'scent' in the temper line" — metallurgical, **false positive** for this register; name it so it is not credited as ownership. |
| `culture-material/cuisine-food-lexicon.md` | 2 | `incense` ×2 | incense/spice as flavour-smoke adjacency — partial, not a perfume system. |
| `culture-material/bathing-and-body-hygiene.md` | 1 | `scent` ×1 | **:7 "adornment-body-codes.md (that entry owns the *adorned* surface — paint, scent, hair; this entry owns the *washing regime* beneath it…)"** — an in-corpus *ownership statement* for `scent`. See below. |
| `culture-material/masks-masquerade.md` | **0 bounded / 4 plural** | `cosmetics` (plural — invisible to the claim regex) | :8 "`adornment-body-codes.md` (owns **cosmetics** and applied facial treatment)"; :35 cites `adornment-body-codes.md:75` cosmetics lexicon; :152 "cosmetics … stay with their ow[ner]". Second in-corpus delegation of the cosmetic/scent surface to `adornment-body-codes.md`. |
| `culture-material/costume-semiotics.md` | 1 | `scent` | scent as a costume signal (one line). |
| `culture-material/ritual-garments.md` | 1 | `scent` | one line, vestment adjacency. |
| `civilizations/india-classical-sanskrit.md` | 2 | `perfume`, `scent` | :127 "Jewellery, girdles, hair, garlands, **scent**"; :141 "a court can value **perfume**, poetry, conversation…". Holds **scent as rank/court marker**. |
| `civilizations/japan-heian.md` | 2 | `scent` ×2 | :67 "Early-spring recognition, anticipation, **scent** and voice"; :128 "Voice, handwriting, **scent**, and sleeves provide partial evidence of identity". Holds **scent as identity evidence**. |
| `civilizations/sogdian-silk-road.md` | 1 | `incense` | :149 Mongolian **küji** "incense" loanword trail. |
| `civilizations/arabia-pre-islamic.md` | 1 | `incense` | :122 "challenges the projection of much earlier **incense**/spice commerce onto Muhammad's Mecca". |
| `civilizations/maya-classic.md` | 1 | `incense` | incense-offering line. |
| `civilizations/zapotec-mixtec.md` | 1 | `incense` | incense-offering line. |
| `civilizations/aegean-minoan-mycenaean.md` | 1 | `scent` | one line. |
| `civilizations/celts.md` | 1 | `cosmetic` | figurative ("cosmetic."), not the register. |
| `civilizations/vietnam.md` | 1 | `cosmetic` | figurative, not the register. |
| `myth-symbol/death-afterlife-eschatology.md` | 1 | `incense` | funerary incense-offering line. |
| `myth-symbol/mineral-stone-symbolism.md` | 1 | `scent` | one line. |
| `linguistics/register-strata-attestation.md` | 1 | `cosmetic` | figurative ("cosmetic"), not the register. |
| `linguistics/dialect-register-consistency.md` | 1 | `cosmetic` | figurative, not the register. |

Named honestly: **none is a whole-register owner** (no talk of a perfume/incense/anointing
*code system*), so the claim's "partial-scope mentions, not whole-register owners" holds at
section granularity. But two of them are more than incidental and must be resolved by the
entry, not waved past:

1. **`bathing-and-body-hygiene.md:7` (scent) and `masks-masquerade.md:8` (cosmetics) are
   two in-corpus delegations to `adornment-body-codes.md`.** The corpus therefore does *not* read as "scent unowned";
   it reads as "scent assigned, undelivered". `adornment-body-codes.md` contains no
   `scent`/`perfume`/`unguent` token (my sweep finds only `cosmetic`), so the delegation is
   unfulfilled — that is the strongest *legitimate* support for the gap claim, and it is
   better evidence than the filename census. The entry must cite that line one-way and
   state the boundary (cosmetic vocabulary stays there; applied aromatics/incense systems
   are here), or the two entries contradict each other.
2. **`timekeeping-instruments.md` owns incense-as-timekeeping** (Bedini, "incense clock",
   :26 incense sticks). An entry that covers incense must cite it and not re-teach the
   fire-clock measures.

Also not a defect, checked: no prior round proposed this entry —
`git grep -inE '(scent|perfum|aromat|incens)[a-z-]*-(lexicon|codes|register)|scent register|perfume register'`
at base over `reports/`+`corpus/` returns nothing, and repo-wide base filenames matching
the stems are zero, so the register is not a re-litigation of an earlier landed entry.

## F5 — MED: id-space bypass around S776 (and citations outside the pinned set)

At base `corpus/SOURCES.md` has **701** rows, max id **S775**, with gaps incl. `576 -> 600`;
**S776 does not exist at base**. Claim C pins `NEW_IDS = range(777,801)` (`:49`), while this
same round's Ca claim introduces **S776** (games-entry supersession) as a *26th* new id.

- `SET`/`ROWS`/`CAPTURE`/`HOSTS`/`LINK` all iterate `NEW_IDS` only, so a scent row
  mis-numbered **S776** is invisible to every C leg (it would only be caught, if at all,
  by Ca-shaped checks on the games entry).
- `ONEID` enforces "each of S777–S800 cited exactly once", but does **not** forbid the entry
  citing any base id. An entry that mines 23 rows and pads the 24th bullet with `S753`
  (the round-65 fragile row) or `S776` passes ONEID, RESTATE (if the bullet's words come
  from a legitimately-cited row) and SET simultaneously.

Concrete bypass to close: assert that the entry's *set* of `S\d+` citations equals
`S777..S800` exactly (two-sided), and extend the id range to whatever ids the round adds.

## F6 — LOW: no post-state assertion

After the entry lands, the claim's own census command should print exactly **1** (the new
file, matched on `scent-`). No leg checks that, and a *second* file carrying the register
(e.g. a draft left in `culture-material/`) would not be seen either — `NOHARM` compares
against `GAMES_ENTRY`+`ENTRY` only for paths, so an extra corpus file would fail NOHARM,
but a duplicate *inside* the accepted path (two register entries, one stale) would not.
Cheap fix: add the post-state census `== 1` as a leg and record it in telemetry.

## Residual risk / verification gaps

- The draft entry does not exist on disk at review time
  (`corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` absent; worktree
  still 239 files, census 0), so I could not test the draft's boundary statements against
  the 22 partial owners in F4, nor whether it cites `S776`/base ids (F5). Those must be
  re-checked against the integrated draft.
- No LSP server answers Markdown in this lane; all ownership evidence above is
  word-bounded literal text. The `grep -ci` numbers count *lines*, not occurrences; every
  cited line was read individually.
- `census-start.txt` may have been overwritten by a W04 seat after being written as a
  census; either way the committed tip does not carry the premise, which is what the
  record must show.
- My probe filenames (F3) are constructed, not present in the base; they demonstrate the
  instrument's blindness. Realized *filename* misses at this base: **0** (no base filename
  carries a register token in any inflection). Realized *body-text* miss under the same
  regex: **1** — `masks-masquerade.md` (4× plural `cosmetics`, 0 bounded), i.e. the
  inflected-form gap is already observable in this corpus, not merely hypothetical.

Report: .ufo/waves/round-66/w1/RevClaimC.md
