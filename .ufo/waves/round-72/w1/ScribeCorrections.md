# ScribeCorrections — round 72, wave 1 (append-only correction texts)

Seat: `L1Kotodama72.ScribeCorrections` (scribe, leaf; no subagent dispatch).
Date: 2026-10-25. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base: `b60c7b140c5350caa7d1073711f14092541533f0` (`b60c7b1`).
Frozen claims read: `reports/round-72/claims.json` (Ca, 12 legs; C, 10 legs).

## Deliverable

`/tmp/r72-corrections.md` — two append-only correction texts, drafted for the L1
to land:

1. **TEXT 1** — the `LOG.md` round-72 entry: a round-72 heading plus **eight
   bullets, one per K71-1..K71-8**, each naming the disposition and the
   evidence.
2. **TEXT 2** — the `corpus/lessons/round-71.md` appended section
   `## Corrections (round 72)`: five rows (id map, quarantine tally, wave-seat
   counts, Capoeira reject reason, counter-sha pairing) in the round-69
   `## Corrections` table shape (`| class | surface | filed text | observed |
   correction |`), each row with its own re-derivation, old → new.

Plus landing notes (not part of the filed text) for the L1: heading-token
uniqueness, required-token coverage, a nested-backtick repair, the optional
`corpus/id-renumber-map.json` artifact, and two verified conflicts (below).

**No lane or fleet byte was written.** Both texts are drafts in `/tmp`. The
never-mutate list (`LOG.md`, `corpus/lessons/round-71.md`, `corpus/SOURCES.md`,
`corpus/QUALITY.md`, `SCORECARD.md`) is untouched; the L1 is the sole writer of
those files, per `SentinelScope.md` OBS-4.

## Convention followed

`corpus/lessons/round-69.md` `## Corrections` (two sections, `:63` and `:77`)
uses the header `| class | surface | filed text | observed | correction |` and
the rule "the faulty bytes are named, not rewritten, and each row carries its
own re-derivation" (`:78-79`). TEXT 2 uses that exact header and that exact
rule, with old → new stated in the `correction` cell as `old \`X\` → new
\`Y\``. (The `reports/round-71/corrections-r70.md` table's `old → new` column
header — `| id | class | surface | old → new | landing |` — is the sibling
per-defect disposition file and is not the lesson's own convention.)

## Evidence, re-derived by this seat (not cited from the spot-check)

Every figure below was measured by this seat against committed bytes.

| fact | command | result |
|---|---|---|
| quarantine tally at `57e0a72` | `git show 57e0a72:reports/round-71/telemetry/quarantine-verdicts.md \| grep -cE '^\| S[0-9]+ \| PRESENT \|'` (and REFUSED / UNVERIFIABLE) | 10 / 7 / 4 = 21 |
| wave-2 seat count | `python3 -c "import json;print(len(json.load(open('.ufo/waves/round-71/w2/spec.json'))['items']))"` | 40 (wave 1 = 37 → total 77) |
| counter sha at the stamped revision | `git show 64da9e14:reports/round-71/accept-ca.py \| sha256sum` | `f706aacd001ee544…` |
| counter sha at base | `git show b60c7b1:reports/round-71/accept-ca.py \| sha256sum` | `1ce25fb9ade45c26…` |
| id-map spans | `git show 65ff151:…/id-renumber-map.json` / `git show 27db4ce:…` / `git show 99e3d63:…` | `S861→S992` (next_free S861, registry 784) → `S874→S1005` (next_free S874, registry 797) → same span, collisions 2→15 |
| LOG in-place rewrites | `git show 1721fbd -- LOG.md`; `git show 99e3d63 -- LOG.md` | records `<RECORDS>` line and misroot-sweep line rewritten at `1721fbd`; Item-10 `S861→S992`→`S874→S1005` at `99e3d63` |
| lesson in-place rewrite | `git show 99e3d63 -- corpus/lessons/round-71.md` | lesson `:83` `S861→S992`→`S874→S1005` |
| fleet report stale lines | `awk 'NR>=55&&NR<=62' /home/vgpnk/Projects/shokunin/.ufo/reports/round-71/kotodama.md` | `:57` and `:61` still read `S861→S992` |
| Capoeira live + CDX | `/tmp/scoutcapoeira/hdr-*.txt`, `cdx-circle-all.txt` (135 rows, all status 200, earliest three `20170513162348`, `20171120140510`, `20171208155324`), `cdx-plain-all.txt` (0 rows), `wb-20171208155324.html` | live HTTP 200 on both slugs; canonical slug `capoeira-circle-00892` has 135 status-200 captures; probed slug `capoeira-00892` has 0; the 2017 capture serves the narrative |
| located quote | `python3` count on the live body and the 2017 capture | "Capoeira is an Afro-Brazilian cultural practice – simultaneously a fight and a dance – that can be interpreted as a tradition, a sport" — 23 words, 3 occurrences live, 1 in the capture |

## Counter-leg simulation against the drafted texts

The drafted texts were run through the drafted counter's own predicates
(`.ufo/waves/round-72/counters/accept-ca.py`, `check()` at `:76-136`) on the
draft strings only — no lane run, no PASS claimed:

| leg | predicate | result on the drafts |
|---|---|---|
| `LOGCORR` | tail after the first lowercase `round 72` contains `S861`, `S874`, `S1005`, `<RECORDS>`, `misroot` | **True** (all five present) |
| `LESSONCORR` | `lesson.split("## Corrections (round 72)")` has exactly 2 parts, and the tail contains `S861`, `S992`, `S874`, `S1005`, `10/6/5`, `10/7/4`, `41`, `78`, `40`, `77` | **True** (split length 2; all ten tokens present) |
| `CAPOEIRA` | `capoeira-circle-00892`, `20170513162348`, `20171120140510`, `20171208155324`, `200` in the lesson tail and `Capoeira` in the LOG tail | **True** |

The markdown table in TEXT 2 was also checked structurally: every row has
exactly 6 unescaped pipes (5 columns), matching the header and the
separator row.

**Landing-critical detail.** The counter splits `LOG.md` on the *lowercase*
token `round 72`. The base `LOG.md` contains no lowercase `round 72` and the
heading `## Round 72 - …` does not contain it either. TEXT 1's first bullet —
`**Round-71 status-neutral corrections (round 72, append-only; …)**` — is
therefore the split point, and all eight K71 bullets fall after it. If the L1
rewrites that bullet, the lowercase token must be kept and the eight bullets
must stay after it.

## Two conflicts found, both verified, both for the L1 to resolve

### C1 — `CASTAMP`: the leg's sentence and the counter's predicate disagree

The claim leg says *"an appended receipt re-stamps measures-ca at 64da9e14
with its true counter sha f706aacd"*. The drafted counter instead requires
the stale pairing to be **absent** (`accept-ca.py:110-113`):

```python
stamp = ("64da9e14" in receipt and "f706aacd" in receipt
         and re.search(r"1ce25fb9.{0,120}64da9e14", receipt, re.S) is None)
```

Measured over the three candidate landings (base blob of
`reports/round-71/telemetry/measures-ca.txt` at `b60c7b1`):

| landing | predicate |
|---|---|
| base as committed | **False** — `1ce25fb9…` (:1) and `64da9e14` (:2) are 93 chars apart |
| base + the RevReceiptHeader block **appended** (`/tmp/r72-castamp/receipt-ca-64da9e14.txt`) | **False** — the stale pairing at :1–:2 survives the append |
| lines 1–8 rewritten so the top header names `f706aacd`, prior bytes preserved below | **True** |

So the counter as drafted can only pass `CASTAMP` by rewriting the receipt
header **in place** — the round-70 anti-pattern the wave-2 seats flagged, and
against the claim's `kill_rule` ("any K71 defect landed by rewriting a filed
byte"). `RevClaimsFidelity` F1 and `RevReceiptHeader` reached compatible
conclusions independently. Two coherent resolutions, both the L1's:
- **(a) append-only landing + counter re-pointed** — append the
  RevReceiptHeader deliverable verbatim (it already carries the six-line 17/19
  header, tree `ff803f43…`, the counter blob sha, and the reproduced
  `ACCEPT-CA-71: PASS` at `64da9e14`), and make `CASTAMP` test what the leg
  says (an appended block pairing `64da9e14` with `f706aacd`) rather than the
  stale pairing's absence. The stale pairing stays as preserved evidence,
  which is the point of an append-only correction.
- **(b) counter as drafted** — rewrite the header in place; passes `CASTAMP`,
  breaks the append-only discipline the claim title asserts.

TEXT 2's `COUNTER-SHA` row is written neutrally between (a) and (b); the
instruction for a (b) landing is in the draft's landing notes.

### C2 — `W2FILES`: the counter's tuple is not the claim's file set

The claim leg says "the seven round-71 w2 seat files"; the claim's `before`
text says "five … (2 modified, 5 untracked)" — 2 + 5 = 7, so the `before` text
is internally inconsistent (`RevClaimsFidelity` F4). The seven actually
uncommitted at base are `Filler30.md`, `RevReceipts.md` (modified) and
`CritTrends.md`, `Filler28.md`, `Filler36.md`, `RevCounterCa.md`, `RevEntry.md`
(untracked). The counter's `W2` tuple (`accept-ca.py:13-21`) is a **different**
seven — it includes five already-committed-and-clean files (`RevSeparability`,
`CritGaming2`, `RevRows`, `RevCausality`, `Filler33`) and omits five of the
really-uncommitted ones. Land the union, or re-point the counter's tuple and
append a note correcting the `before` text's "five".

## Also recorded, outside this seat's text drafts

- `MAPCORR` reads `corpus/id-renumber-map.json`, a path that does not exist in
  the lane tree (the only id-map is
  `.ufo/waves/round-71/assimilation/id-renumber-map.json`; `RevClaimsFidelity`
  F2, same finding). The draft supplies a suggested JSON body for that path as
  an optional third artifact, and the alternative (re-point the leg at the
  lesson's appended `ID-MAP` row). The frozen leg names the *record*, not its
  path, so either resolution satisfies the claim once the record exists.
- The `CAPOEIRA-REJECT` row quotes round-71 filed text that itself contains
  backticks (`` `capoeira-` ``). Inside a markdown table cell that ends the
  outer code span early; the landed cell needs doubled backticks or italics
  for that one inner pair. Flagged in the draft's landing notes.
- The Capoeira ground truth rests on `ScoutCapoeiraReopen.md` (landed in
  `.ufo/waves/round-72/w1/`), which also records that the challenge wall is
  UA-gated (browser UA → 200, default curl UA → the F5 TSPD "human visitor"
  frame) and that the round-71 blanket "ich.unesco.org live CAPTCHA walls"
  premise does not reproduce today. The correction text states only the
  falsified ground (live 200 + canonical-slug CDX captures) and the standing
  flip to Flamenco, as the assignment specifies; the UA-gating nuance is left
  to the L1's lesson/QUALITY wording so the correction does not over-claim.

## Tooling

No installs, upgrades or updates: no `pacman` (paused host-wide), no
`uv`/`npx`/`cargo`/`npm`. Only pre-existing `git`, `python3` (stdlib),
`grep`, `awk`, `sed` were used. Scratch confined to `/tmp/r72-corrections.md`
(this seat's own draft) and read-only reads of other seats' scratch under
`/tmp/scoutcapoeira/` and `/tmp/r72-castamp/`.

## Out of scope (not touched by this seat)

`LOG.md`, `corpus/lessons/round-71.md`, `corpus/QUALITY.md`,
`corpus/SOURCES.md`, `SCORECARD.md`, `reports/round-71/telemetry/` — all
L1-owned writes; this seat produced drafts only. The fleet report
`.ufo/reports/round-71/kotodama.md` (stale `S861→S992` at `:57`/`:61`) is
outside the lane repo and is not edited; the round-72 fleet report is the
L1's write, and TEXT 1's K71-3/K71-5 bullets name the superseded texts for it.
