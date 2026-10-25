# CritTrendObservables — pre-declared trend verdicts, round 74 (hyaku run 7)

Leaf seat. Read-only on every repo path; this file is my only write. No network fetch, no
download, no tool installed (nothing to record). Evidence is committed bytes at the lane base
`f7104cbce186bc2e1522abf0cfd619cc834628bb` plus the draft pair and wave-1 seat reports; **no
landed data exist and none was scored** (no `<lands>`, `reports/round-74/accept-c.py` and
`accept-ca.py` are not yet on disk, `reports/round-74/ledger.json` is not yet committed).

Purpose: fix, before data, which trend may fire, on which exact observable, and what would make
it fire *against* the round — so the closure cannot pick the reading after seeing the numbers.

---

## 0. The base facts I re-derived (the pre-declaration rests only on these)

All at `f7104cbce186bc2e1522abf0cfd619cc834628bb`, re-run 2026-10-25:

| fact | command | observed |
|---|---|---|
| registry rows / last id | `git show <base>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 804; last S880 |
| host rows | `git show <base>:corpus/SOURCES.md \| grep -c <host>` for `litmemo.com`, `tuduku.space`, `chinawriter.com.cn` | 0 / 0 / 0 (`philol.msu.ru` = 1, row S877) |
| setting ground owners | `git ls-tree -r --name-only <base> corpus/knowledge \| grep -ciE 'worldbuilding\|setting'` | 0 |
| CJK term owners | `git grep -l -- <term> <base> -- corpus/knowledge \| wc -l` for 設定ノート / 世界観 / 世界观 | 0 / 0 / 0 |
| **S877 `used-by` cell at base** | `git show <base>:corpus/SOURCES.md \| awk -F'\|' 'NR==832{print $(NF-1)}'` | `corpus/knowledge/linguistics/conlang-scholarship.md` |
| S877 citers at base | `git grep -c 'S877' <base> -- corpus/knowledge` | `conlang-scholarship.md`:25 |
| staged S882 document | `grep -n '^| S882' …/merge/kotodama/SOURCES.append.md` | same document as lane S877 (philol.msu.ru conlangs.pdf) — dedup is real by document |

Claim C's `before` is therefore true as declared. That matters: a trend pre-declaration whose
"before" is unverified is worthless, and this one is checked.

---

## 1. The three questions put to this seat

### 1a. Does an amendment co-admitted with its base count as deepening? **No. Cannot fire quality.**

Deepening is an observable about **held** knowledge: LEARNING.md quality fires when "a weaker entry
is superseded by a stronger one, or stale entries re-verify". At the base commit this family has
0 filename owners and 0 term owners (table above); `claims.json:76` itself requires both entries to
be "absent at base". Both files are therefore **the same admission**, listed together at
`claims.json:42-43`, and the amendment's own back-reference ("The entry this amends records what a
setting is made of", draft amend header) is an internal pointer, not evidence of a prior revision —
it can point at a file in the same landing commit.

Two corroborating precedents, same lane, same shape:
- round-72 SCORECARD row: "no existing entry re-verified or deepened (**C is net-new ground, not
  depth**)" (`SCORECARD.md`, round-72 axes table).
- round-73 non-author closure §5: expansion improved with the caveat "**base+amendment is one
  ground**"; quality unchanged.

Do not let the filename `…amend-2026-10-23.md` argue otherwise: the date precedes both the pair's
`verified-at: 2026-10-25` and every adopted row's `opened` date (2026-10-25). A name that predates
its own sources cannot evidence a revision history, so a closure reading it as "deepened an entry
from 2026-10-23" would be recording false provenance. (The same date is carried by round-73's
`conlang-scholarship.amend-2026-10-23.md`, so it is a naming convention, not a revision date.)

**Consequence for expansion:** one ground, two files. Improved at **1 net new ground**; the report
must say "one ground / two entries". A report that counts "two grounds" or uses the amendment as a
second expansion unit **overstates the observable** (the wording, not the count, is the defect).

### 1b. Does re-quoting two earlier-REFUSED rows fire discernment? **No. It is a disposition repair, and the refusal was correct.**

The refusal was not a taste judgment that new evidence overturns. It was a **census off-by-one quote
binding**, and the round's own wave-1 scout says so in terms:

- register S816 (2025 URL) was filed `payload-absent` with quote `这个我肯定考虑过。我自己就是资深读者…`,
  which is **on the other URL** (the 2022 page, 1 hit); register S817 (2022 URL) was filed with
  `Sowers-Wills's 'Phonology from the inside out…'`, a clause belonging to **lane row S880's**
  document (`absent-defect-register.md:129-130`; `ScoutQuarantine816817.md` §3-§4).
- mechanism: campaign ids S758/S759 paired each id's URL with the **next** row's quote
  (`census-adjudication.json`, `binding: id`).
- the wave-1 scout's conclusion, verbatim: "The re-open path is a fresh row with a located quote,
  **not a reversal of the REFUSED verdict**" (`ScoutQuarantine816817.md` §5).

QUALITY 20 is explicit: record/instrument repairs — and it names "dispositions" — "are calibration
work, **never quality or discernment observables**". The staged rows stay refused; the documents are
re-opened by a fresh row with a fresh quote. That is a gate **decision republished on new bytes**,
not a decision reversed.

So: if the round's lesson or report describes this as "a gate decision reversed with evidence", that
is a false account of a correct refusal (and it would be the lane marking its own homework with the
word "reversed" doing the work). The honest sentence is: *the staged quote bindings were refused in
rounds 68/71 and remain refused; the documents are re-opened this round by fresh rows S883/S884 with
quotes located on the page*. Claim C's GATE leg (`claims.json:79`) already asks for that sentence —
hold it to that language.

**The only way this can contribute to discernment** is as an *admit* the non-author spot-check
re-opens and agrees with. The lane's own re-probe contributes nothing (LEARNING: "A subagent the lane
dispatched is still the lane").

### 1c. Does repairing records fire quality? **No — and Ca must declare `unchanged` on both trends.**

QUALITY 20, verbatim: "A round that repairs records must declare `unchanged` on both trends unless
an observable fires." Ca is a records claim (`"kind": "records"`, axis calibration): ledger pairs,
tracked seat files, PASS-at-lands receipts, scenario-count drift, README footer readings. None is a
re-verified/deepened/superseded entry, so quality cannot fire; none is a gate decision or a new
lesson-grounded criterion, so discernment cannot fire from Ca either. Round 72 already ruled the
nearest case: authoring QUALITY 20 itself "is calibration, never quality — criterion 20".
**Calibration `improved` on the axes table and `unchanged` on the trends are not in conflict**; round
72 recorded exactly that pair.

---

## 2. Pre-declared verdict table

| trend | LEARNING.md observable | threshold for `improved` | counter-observable for `harmed` | what the outside spot-check must see |
|---|---|---|---|---|
| **expansion** | net new admitted `knowledge/` entries on ground the coverage map did not hold, each `source:` citing a mined `SOURCES.md` row | **1 net new ground, 2 entries.** At `<lands>`: both files exist and are absent at base; every `source:` line resolves to one of S877/S881–S884 and the row's URL equals the cited URL; S881–S884 contiguous, `mined`, `opened 2026-10-25`; base ground counts stay 0/0/0 (table §0); both entries clear QUALITY 1–5, 15 (cited-lines 0 findings), 16 (quote in body, not caption) and 18-ish row anchors. Report wording "one ground / two entries" — not "two grounds" | a cited row's **Gate quote is not in the page body** on the spot-check's own re-open (the exact r68/r71 class) while the row/entry stays admitted; or a tier-C page (litmemo, tuduku, chinawriter-2022) carries a claim alone (QUALITY 2/6); or the "ground" was already owned at base | re-open S883 and S884 (plus one of S881/S882) with the row's recorded UA; byte count + sha vs the evidence file; **grep the Gate quote in the raw body, not in the lane's window**; read the four registry rows; confirm `804→808`, S881–S884 contiguous, absent-at-base |
| **quality** | entries re-verified, deepened, or superseded; `verified-at` freshness | a file **present at `f7104cb`** is re-verified with its declared recheck command, or superseded by a stronger entry, with no admitted entry failing its re-check. **Nothing in claims C/Ca or the frontier items does this → pre-declared `unchanged`; it cannot fire** | an entry present at base is found false/stale and **left unmarked**; or an in-place registry edit erases a held entry's citation record (see D1) | `git diff base..<lands> -- corpus/knowledge` shows only the two new files (no base entry edited); S877's `used-by` still names `conlang-scholarship.md`; the routed S879 superseding row is **declared outstanding**, not claimed closed |
| **discernment** | gate decisions vs the outside spot-check; `QUALITY.md` criteria | **outside-only.** The non-author spot-check samples ≥1 admit **and ≥1 evidence-based reject of this round**, records agree/disagree with reasons; and for any new QUALITY criterion (25), the criterion cites a lesson row **and** the spot-check independently re-runs its red-before and sees the FAIL. Lane-side work (the re-quote, dispositions, record repairs, its own mutation sweep) fires nothing | a disagreement left unlearned (quote not in body yet admitted; a reject's stated ground falsified and uncorrected); a criterion added with **no lesson behind it**; or `improved` claimed from the re-quote/repair itself (QUALITY 20) | use the **register S816/S817 staged-binding refusal** as the reject sample (probed URL + reason + flip), **not** the S882 dedup; agree/disagree on the S883/S884 admits; re-run QUALITY 25's `sh tools/check-quality25.sh …` red-before at round-73 bytes and see `CONFIG: FAIL` / `JUNK: FAIL` |

**Pre-declared verdicts, before data:** expansion — `improved` **iff** the expansion row above
holds, else `unchanged`; quality — `unchanged`; discernment — `unchanged` unless the non-author row
above fires. No `unprovable-but-better` is available to either claim (that route needs a named
non-author judging the change better, which is the same outside check).

**What the reject sample must not be.** `claims.json:79` requires ">=1 reject". The only round-74
candidate that is *not* a decision is refused staged S882: it is refused because lane row S877
already names the same document (verified, §0) — a dedup, not taste. The evidence-based reject
available is the staged S816/S817 **quote binding** (probed URLs, reason, flip), which the wave-1
scout re-verified on byte-identical pages. If the Gate's only reject is the S882 dedup, the
"at least one reject" requirement is satisfied by a non-decision and the spot-check has nothing to
agree or disagree with.

---

## 3. Defects I attack claim C on (verdict-neutral, must still be fixed)

These are **not** trend harms — no LEARNING observable covers them. That is exactly why they must be
fixed in the claim, not absorbed into a trend label.

### D1 (highest) — S877's `used-by` will be falsified by the leg as worded

`claims.json:77` says: *"each row … used-by exactly the admitted entries whose source: lines cite
it; the only in-place registry change is S877's used-by cell (old->new in the lesson)"*. S877 is not
one of the four added rows, so its cell content is graded by **no mechanical leg** — only the diff
("the only in-place change") and a prose "old->new" in the lesson.

But S877's cell at base is `corpus/knowledge/linguistics/conlang-scholarship.md` (§0), and that
entry cites S877 **25 times**. The true new value is a **union**:
`conlang-scholarship.md` + `worldbuilding-setting-practice.md`. The draft README/footer text already
says "used-by exactly the two files above" (drafts/readme-rows.md §3), and a literal implementation
of "exactly the admitted entries" puts only the new file there. Either outcome is bad: a union fails
an "exactly" leg, and an exclusive value **silently erases a base entry's citation record** — a false
registry cell the census cannot see (`sources-census.sh` E11 only checks that listed paths exist; it
never checks that every citing entry is listed).

*Smallest safe correction:* replace "used-by exactly the admitted entries whose source: lines cite
it" with two legs — (i) for each of S881–S884, `used-by` is exactly the entries whose `source:` lines
cite that id (equality is right for new rows); (ii) S877's `used-by` **contains** every
`corpus/knowledge` file that cites `S877` at `<lands>` (re-derived by `git grep -l 'S877'`), and
contains `conlang-scholarship.md`. Log the in-place change with both full cell values, not a
before/after adjective.

### D2 — the EVIDENCE leg cannot fail on the failure class that already fired twice

`claims.json:80` requires "a 64-hex sha256 of the fetched body, and the body window around the quote
stored verbatim; the counter checks the Gate quote occurs inside that stored window". The window is
lane-authored; the body is **not** retained, so nothing re-derives the sha and nothing checks
window ⊆ body. The shape is inherited from round 73 (`reports/round-73/evidence/S877.txt`, 2,417 B:
`sha256:` of a 1,055,723-byte PDF, then a whitespace-collapsed window) — and round 73's own mutants
record "forged evidence windows" passing 11/11. QUALITY 25's junk landing only covers a quote
*absent* from the window; a window that contains the quote but was not taken from the body passes
every declared leg.

That is the r68/r71 defect (quote absent from the page) surviving in a form the counter cannot see.

*Smallest safe correction:* store what is checked — the fetched body (or the `pdftotext -enc UTF-8`
extract for S877, with the extract's own sha beside the PDF's) under
`reports/round-74/evidence/<id>.body`, and add the leg: `sha256(stored body)` equals the recorded
sha AND the window is a byte substring of the stored body at the recorded offsets. Add one junk
landing `forged-window` (window contains the quote, is not a substring of the body) that must FAIL
EVIDENCE.

### D3 — QUALITY 25, as drafted, binds from round 74 and round 74 does not meet it

Draft `quality-25.md` (b) requires "**five junk landings and one receipt per landing under
`reports/round-<N>/telemetry/junk/`**, each receipt present at the freeze commit", and its closing
line says "Binds from round 74". The round's own declarations name different artifacts: claim C's
do-nothing control is one file `reports/round-74/telemetry/controls-c.txt` with four junk landings
(`claims.json:90`); claim Ca's controls are `--selftest` scenarios (`claims.json:115`). Unless five
per-slug receipts land at the freeze, **round 74 is the first violator of the criterion it adds** —
and the criterion was added precisely against that class.

*Smallest safe correction:* either (a) `Binds from round 75; no earlier round is retro-fitted` (the
criterion-24 precedent), or (b) land `telemetry/junk/<slug>.txt` ×5 at the freeze and name those
paths in `claims.json`'s do-nothing controls. Pick one before freeze; do not let the criterion and
the claim disagree on paths.

### D4 — do not let the lesson call the re-quote a reversal (see §1b)

*Correction:* use "refused staged binding → fresh row, located quote" and name register ids S816/S817
and the census off-by-one as the reason the old rows stay refused. This is also what QUALITY 12
requires: the old reason must keep its re-test output, and the re-test (the scout's fetch, byte
identical to round 71) upholds it.

### D5 — the "furthest behind" rule is unmet on the record

Quality has been `unchanged` for **five consecutive rounds** (round 70 corrected to unchanged,
`SCORECARD.md` round-70 correction row; round 71's report claimed quality/discernment improved and was
corrected because no observable fired, `corpus/lessons/round-71.md:58`; round 72 and round 73
unchanged), and this round plans expansion/coverage again plus calibration repairs. LEARNING.md:
"Choose the round's claims from the trend that is furthest behind." `claims.json`'
`axes_note` asserts the round works calibration + coverage and claims "No stagnation-nudge waiver" —
but it does **not** say why coverage/calibration outrank quality this round.

*Correction (review-only; no counter can check it):* the report states the reason in one line —
e.g. the round-73 closure routed defects are repair-first obligations and the staged package is a
one-shot release — or it records quality work as the next round's claim. Otherwise the verdicts stay
honest while the learning path drifts: three consecutive expansion rounds (72, 73, 74) with quality
unchanged is not a trade, but it is not the path LEARNING.md asks for either.

---

## 4. What this seat did and did not run

Ran: the base re-derivations in §0 (read-only `git show`/`ls-tree`/`git grep`); reads of
`reports/round-74/claims.json`, `corpus/QUALITY.md` (criteria 1–25), `LEARNING.md`,
`corpus/lessons/round-73.md` (`## Routed to round 74`, Corrections), `corpus/lessons/round-73-verifier-spotcheck.md`,
`corpus/lessons/round-67.md`/`round-68.md`/`round-72.md` (the quarantine record), the wave-1 seat
reports `ScoutQuarantine816817.md`, `ScribeQuality25.md` draft, the two entry drafts, the README-row
draft, `reports/round-73/evidence/S877.txt`, the staged `SOURCES.append.md`, and the shokuknow
`absent-defect-register.md` (read-only).

Did **not** run: any counter (none exists at base), any fetch (so no User-Agent record is owed and no
download was made), any check whose input is a land (none exists), and no scoring of landed data.
Not verified by me: whether the lander will implement D1 as a union (the leg is unimplemented); the
final QUALITY 25 wording; the entries' own quote locators (wave-1/2 seats own that).
