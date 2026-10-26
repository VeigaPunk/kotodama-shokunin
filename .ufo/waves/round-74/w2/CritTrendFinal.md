# CritTrendFinal — attack on the round-74 trend verdicts (before filing)

Seat: wave-2 critic, round 74 (falsify). Lane `kotodama-shokunin`. Read set: `LEARNING.md` (fleet root),
`corpus/QUALITY.md` 20/21/24/25, `corpus/lessons/round-74.md`, `corpus/lessons/round-72-verifier-spotcheck.md`,
`corpus/lessons/round-73-verifier-spotcheck.md`, `.ufo/reports/round-73/kotodama.md`, `PROVINCE.md` (at base),
`corpus/README.md` (base + lands), `corpus/SOURCES.md` (base + lands), the two landed entries, the frozen
`claims.json` at the operative freeze, `reports/round-74/telemetry/*` listing, `.ufo/waves/round-74/w1/ScoutWayback.md`.
Revisions: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; freeze F3
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; claim Ca lands
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; lane main at dispatch `1d7add3`.

**Fetch hygiene.** This seat made **no network request**: every read below is a `git show` / `git grep` /
`git ls-tree` read at a named revision, or a file read of committed bytes. No User-Agent was sent, so no UA record
is owed. **Tool installs: none.** **Writes:** this file only (plus `/tmp/CritTrendFinal/` scratch). I did not run the
counters — their PASS claims are other seats' legs, not mine.

**Verdict summary (what survives attack).**

| trend | candidate | verdict that survives | driver |
|---|---|---|---|
| expansion | improved | **improved, with the one-ground caveat and a narrowed novelty sentence** (F1, F4, F5) | 247 → 249 knowledge files, two files added on ground with 0 filename owners, 0 topic-line owners and 0 registry host hits at base; both entries have coverage-map rows |
| quality | unchanged | **unchanged — conditional**: only if F1's two sentences are marked before filing; if filed unmarked, the clause "an entry is found false … and left unmarked" fires and quality is `harmed` (LEARNING.md:34) | `git diff --stat base..lands -- corpus/knowledge` = two additions, zero modifications; no existing entry re-verified/deepened/superseded |
| discernment | unchanged or improved | **unchanged at filing**, with a named flip condition for the non-author closure (F2) | no outside spot-check of round 74 exists in any tree; QUALITY 25 is instrument-class, and QUALITY 20's own preamble bars instrument work from the discernment observable; round-73's filed verdict for the identical shape was `unchanged` (`.ufo/reports/round-73/kotodama.md:34`) |

LEARNING.md:37-38 governs the interaction: if quality is filed `harmed` while expansion is `improved`, the pair is a
**trade** and "never admitted". The round therefore cannot dodge F1 by keeping `unchanged`.

---

## F1 — HIGH — the amendment's `gap filled:`/`ground:` deny content its own parent entry holds

The amendment's header says its parent lacks the build order; the parent's `§4` is titled after that order and
quotes it verbatim. The two sibling files landed in the same claim.

```
$ git show c4bf61a:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md | sed -n '8p;10p'
- ground: … This amendment supplies the two decisions the corpus lacked — in what order the work is done, and when the reader is told — …
- gap filled: the entry this amends records what a setting is made of and the settings-note tables that carry it; it does not say which part is built first, which part is derived from which, or when in a serial the reader is shown any of it. This amendment records those three things for one author, and nothing more.

$ git show c4bf61a:corpus/knowledge/culture-material/worldbuilding-setting-practice.md | sed -n '9p;53p;72,74p'
- topic: … a five-step build order, a four-layer causal chain from environment to individual experience, …
| in what order to fill the parts | not addressed | five steps, five elements, five note sections |
## §4 Build order — the five steps, and the two orders they allow
The five-step order as the page states it: "世界観の作り方は、①物語の核になるルールを決める ②主人公の生活圏から作る ③自然→社会→文化→個人の順に因果をつなぐ ④物語で使う分だけ掘り下げる ⑤一か所にまとめて書きながら更新する、の5ステップです。" (S881).
```

Parent line 53 is the parent's own comparison table: the practitioner pages **answer** "in what order to fill the
parts". Parent §4 states which part is built first (①核になるルール) and which is derived from which
(③自然→社会→文化→個人), and the parent's own `gap filled:` (line 10) claims "what to decide first" as its gap. So:

- "does not say which part is built first" — **false** (parent ①, and parent §4's heading).
- "which part is derived from which" — **false at face value** (parent ③); the narrower true sentence is: *the parent
  does not say how a power/progression ladder is derived from a world-view.*
- "when in a serial the reader is shown any of it" — **true and new**: the parent has no disclosure content
  (`grep -niE 'disclos|reveal|when the reader' <parent>` matches one unrelated table cell, line 250).

Impact on the verdicts: (a) expansion's novelty sentence must not repeat the header ("fills gaps the parent lacks");
the honest sentence is *a second practitioner register (Chinese) adding the disclosure-timing tolerance and the
premise→laws→ladder derivation*. (b) QUALITY 1's rule — "A claim the author cannot verify is marked `(to-verify)`
inline — never laundered into assertion" — is not satisfied by a corpus claim that the same commit refutes, so the
entry is an admitted entry carrying a falsified header claim. Round 73's precedent is exact: its outside verifier
kept quality `unchanged` only because "the false statements wave-2 found in the new amendment were repaired in the
committed head" (`corpus/lessons/round-73-verifier-spotcheck.md:80`). Here they were not repaired.

**Smallest safe correction.** Append one `## Erratum` section at the end of the amend file quoting line 8 and line 10,
naming the parent `## §4` and `:53` as the contradiction, and restating what is new (disclosure timing; the ladder
derivation; a second register). Append-only inside the file — no line removed, no header field rewritten. Then the C
counter must be re-run with `--lands` at the erratum commit and the receipt re-stamped (its `ENTRIES`/`CITEDLINES`
legs grade `<lands>` bytes; a post-lands edit without a re-stamp leaves main ≠ graded bytes). Afterwards quality is
`unchanged` (found-and-marked), not `harmed`.

## F2 — MEDIUM — `discernment: improved` is not supportable at filing; state `unchanged` plus the flip

Evidence that no round-74 outside spot-check exists:

```
$ git ls-tree -r --name-only c4bf61a corpus/lessons | grep -c 'round-74'
1
$ grep -niE 'spot.check|non-author' corpus/lessons/round-74.md | cut -c1-90
168:| R74-M1 | landing | Six round-73 wave-2 seat files …
$ ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-74/
game-dev-2d.md  game-dev-3d.md          # no kotodama.md; hyaku closure not run
```

The single hit is R74-M1 citing *round 73's* spot-check. LEARNING.md:42-44 requires a non-author spot-check each
round and says "A subagent the lane dispatched is still the lane" — so this seat and the CritFactBase seats cannot
serve it.

QUALITY 25 **is** lesson-grounded (`corpus/QUALITY.md:81` cites `corpus/lessons/round-74.md` `## Mistakes` R74-M3;
`git show f7104cb:corpus/QUALITY.md | grep -c '^2[5-9]\. \*\*'` = 0), so QUALITY 20's remedy clause read alone would
license `improved`. Two things defeat that reading here:

1. QUALITY 20's own preamble (`corpus/QUALITY.md:61`) says "**record/instrument repairs** … are calibration work,
   **never** quality or discernment observables". R74-M3 is a counter-survivor defect; QUALITY 25 governs counters.
   A criterion about instruments is instrument work, whatever its number.
2. The lane filed exactly this shape as `unchanged` one round ago — lesson-grounded criteria on instrument/record
   defects with no outside check: `.ufo/reports/round-73/kotodama.md:34` "discernment: unchanged — QUALITY 22/23/24
   are lane-authored from lane-internal measurements; no outside spot-check of this round's gate yet." Filing
   `improved` now contradicts the lane's own prior filing for the same shape.

Where QUALITY 20 is genuinely ambiguous (preamble vs remedy clause) it is **too late to clarify**: the freeze has
landed and seats have scored landed data — "A rule changed after any seat scores landed data is not the claim's
rule" (frozen `claims.json` status). Route the one-line clarification (does an instrument-class lesson-grounded
criterion count?) to round 75; do not edit QUALITY.md now.

**Surviving text for the report:**

> - **discernment: unchanged** — QUALITY 25 is a new lesson-grounded criterion (R74-M3) but its subject is counter
>   calibration, and QUALITY 20 excludes instrument work; no outside spot-check of this round's gate exists yet.
>   Flips to `improved` only through the non-author closure's spot-check (≥1 admit and ≥1 reject, reasons in the
>   round's lesson), appended as an erratum — never an in-place rewrite of filed bytes (round-71 K71-3).

## F3 — MEDIUM — "the round re-quoted two earlier-refused rows — a reversal with evidence" is contradicted by the lesson

```
$ sed -n '29p' corpus/lessons/round-74.md
- **Re-quote discipline.** S883 and S884 are *new rows for re-opened documents*, not reversals: the register rows S816 and S817 stay REFUSED (see Quarantine), and each admit row names the earlier refusal.
$ sed -n '131,142p' corpus/lessons/round-74.md   # ## Quarantine — four clearing conditions
```

The round denies a reversal in the same bytes that the candidate sentence calls one. If the report says "reversal",
it asserts a change to register verdicts that the Quarantine section forbids, and it hands the closure a false
provenance claim to check. **Fix:** use the lesson's own words — "two documents refused as staged in the register
(S816/S817) were re-opened as new rows S883/S884 with quotes located this round; the register rows stay REFUSED under
the four clearing conditions." The discernment consequence follows: a *non-reversal* is not a learned disagreement,
so it cannot feed the criterion limb either (F2 stands).

## F4 — LOW — "frontier ground entered: setting-practice" overstates the coverage map

```
$ grep -niE 'setting|設定|世界観|世界观' <base corpus/README.md> | head
465:- `myth-to-language-derivation.md` — … includes a disposable worked derivation, not setting canon.
$ git show f7104cb:corpus/README.md | sed -n '601p'
## Known gaps (frontier)
```

Setting practice was never on the base frontier list (`## Known gaps (frontier)`, line 601), and the only base
README hit is the phrase "not setting canon". The expansion observable that fires is "net new admitted entries on
uncovered ground" (LEARNING.md:33) — not "frontier areas entered". **Fix:** "new ground entered (absent from the
base coverage map; not previously on its frontier list)".

## F5 — LOW — attribute the four rows precisely; do not attach "opened this round" to S877

```
$ grep -oE '\bS[0-9]{3}\b' entry-base   | sort | uniq -c   → 5 S877, 31 S881, 9 S882
$ grep -oE '\bS[0-9]{3}\b' entry-amend  | sort | uniq -c   → 20 S883, 16 S884
$ parse SOURCES.md@c4bf61a for S881..S884 → cells 11, status mined, opened 2026-10-25, recheck 180d, used-by = citing entry
$ parse SOURCES.md@f7104cb and @c4bf61a for S877 → both: 11 cells, status mined, opened 2026-10-25; only cell 11 differs
```

Correct sentence: *base entry cites S877 (reused, mined at base) + S881/S882; the amendment cites S883/S884; four
rows opened this round, one reused.* Saying the entries simply "cite four mined rows opened this round" drops the
reused-row fact the candidate itself names — and the reused row's tier note is what a reader must weigh.

---

## Attacks that FAILED (the claim survived)

1. **"The ground was not uncovered" (expansion).** Failed.
   ```
   $ git ls-tree -r --name-only f7104cb corpus/knowledge | grep -icE 'worldbuilding|setting'   → 0
   $ git grep -lE '設定ノート|世界観|世界观' f7104cb -- corpus/knowledge | wc -l                → 0
   $ git grep -niE '^- topic:.*(設定|世界観|世界观)' f7104cb -- corpus/knowledge | wc -l        → 0
   $ git show f7104cb:corpus/SOURCES.md | grep -cE 'litmemo\.com|tuduku\.space|chinawriter\.com\.cn' → 0
   ```
   No filename owner, no topic owner, no registry row at base. Both entries carry coverage-map rows
   (`corpus/README.md:445` and `:446`) and the last footer reads 249 (`:815`).
2. **"An existing entry was re-verified/deepened, so quality moved" / "the round repaired records, so quality
   improved".** Failed: `git diff --stat f7104cb c4bf61a -- corpus/knowledge` = `2 files changed, 358 insertions(+)`,
   zero modifications; Ca's lands touch only `SCORECARD.md`, `SKILL.md`, `corpus/QUALITY.md` and telemetry. Under
   QUALITY 20 those are calibration, not observables.
3. **"S877 is not a `mined` row, so the base entry fails the expansion observable."** Failed: row 832 is `mined`
   with `opened 2026-10-25` at base and at lands; only the `used-by` cell changes, 11 cells both sides.
4. **"The entries' no-capture statements violate QUALITY 21/24."** Failed: `.ufo/waves/round-74/w1/ScoutWayback.md`
   carries the canonical-slug CDX probes for all four URLs, repeated without the status filter, six litmemo and seven
   tuduku variants, and positive controls (`example.com` in the identical shape returns rows; `litmemo.com` host rows
   exist) — the S881/S882 no-capture statements are supported as filed.
5. **"The setting ground is out of province / lore's."** Failed at base bytes: `PROVINCE.md` owns "the generative/
   coupling craft … `culture-material` … `synthesis`" and reserves canon/consistency to lore; the entries refuse
   canon, refuse rights rulings, and hand off under `synthesis/worldbible-integration-contract.md`. (Deeper
   adjacency belongs to the ConnectorAdjacency seat; I state only that nothing here makes the trend verdict false.)
6. **"The stale `## culture-material/ (36)` heading is an undisclosed record defect that poisons the coverage map."**
   Failed as a verdict-attack: `corpus/README.md:796-822` names the heading stale in the landing block, names the two
   unindexed heritage files, and keeps the two older footers byte-identical. It is disclosed, and disclosure is the
   lane's rule for drifted counts. It is not a `## Known gaps` deletion, and QUALITY 20 keeps it calibration-side.

---

## What the non-author closure must see

1. **An admit, re-opened:** S881's quote `「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。」`
   found in `reports/round-74/evidence/S881.txt`'s stored window at the h3 locator, or S883's re-quote found on the
   2025 page — and the row's `used-by` cell naming exactly the citing entry.
2. **A reject, re-checked:** staged S882 refused-not-appended (the document already holds lane row S877) and staged
   S895 dropped (the amend file carries no folded "Superseded passage"); both flips as the Gate states them.
3. **The re-quote is not a reversal (F3):** the register rows S816/S817 untouched and still REFUSED; the four clearing
   conditions at `corpus/lessons/round-74.md:131`ff each satisfied.
4. **No admitted entry fails its re-check:** F1's two sentences marked (or the erratum appended) and the C counter
   re-run at the new lands; otherwise quality is `harmed` and expansion+quality is a trade (LEARNING.md:37-38).
5. **The spot-check's own record:** agree/disagree per sampled decision with reasons, appended to the round's lesson
   (append-only). On agreement, `discernment` flips to `improved` through an appended erratum on the filed report —
   never an in-place rewrite of filed bytes (round-71 defect K71-3, `corpus/lessons/round-71-verifier-spotcheck.md:26`).
   This seat and every other wave-2 subagent are the lane, and do not count as that check.
