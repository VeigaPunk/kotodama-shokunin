# ScribeQualityFinal — QUALITY.md append staged for claim Ca (round 75, wave 2)

Seat: `ScribeQualityFinal` (leaf scribe). Date: 2026-10-27. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(hyaku run 10, round 75), lane base `f556d1049fe651d3d63975600b13acd9fb686f15`. Fleet root read only, never written.
No delegation, no background jobs, no subprocess seats; no tool installed or upgraded (`pacman` not run, nothing written to
`~/.local/bin`); no network fetch, so no User-Agent is bound to any response in this report. Lane git read-only
(`show`/`grep`/`ls-tree`); no `git add`, `commit`, `checkout`, `stash`, `reset` and no jj call anywhere.

## 1. Deliverable

| path (repo-relative) | what it is | sha256 |
|---|---|---|
| `.ufo/waves/round-75/w2/stage/corpus/QUALITY.md.append` | the staged append for `corpus/QUALITY.md`: criterion 27, criterion 28, and the unnumbered addendum to criterion 23 | `d26d6c986fbd802c739e114fde2587b0481e6637ee8cdb9fab71dfb4ff1f9acd` (12,980 B, 72 lines) |

The file is **append-only text**: `git diff --no-index --numstat` between `f556d10:corpus/QUALITY.md` and that blob plus
this file is `72  0` — 72 insertions, zero deletions. Base highest criterion is **26** (`corpus/QUALITY.md` ends at
`:125`), so the two new criteria are **27** and **28**; nothing below the highest base criterion is rewritten.

## 2. What the staged text says (final numbers and bindings)

| block | number | binds from | check | grounding |
|---|---|---|---|---|
| a reject reason names the artifact it was observed on | **criterion 27** | round 75 (round-74 Gate rows stay as filed, annotated under `## Corrections — round 75`) | one `sh -c` line: per reject row, extract artifact path + 「span」, count the span in the artifact, `MISFILED` when the count contradicts the stated `absent`/`present`; exits 0 only with no `NO-FIELD`/`MISFILED` | `corpus/lessons/round-74-verifier-spotcheck.md:100` item 2 (R2), R74-M5, `## Quarantine` `:143-144`, RevLessonGate F1, ScoutRejectProbes F2 |
| a leg's authority is pinned at the freeze, not read from the graded tree | **criterion 28** | round 76 (round-75's CITEDLINES leg is already declared and names only the tool's output) | one `sh -c` line: `comm -23` of executed repo tools vs a 64-hex pin table; prints nothing | `corpus/lessons/round-74.md` R74-M3; MutPredicateC F1 (executed); w1 `CritCCounterVacuity.md` ranked repair 1 |
| addendum to criterion 23 | unnumbered (label binds it; it sits at EOF because an `.append` can only grow the file at its end) | round 75 | limb 1: receipt-path constants a counter defines but `build_fixture` never names; limb 2: `head -2 …/selftest-ca.txt | grep -q 'clean -> exit=0'` | `corpus/lessons/round-74.md` `## Routed to round 75` item 4 (R73-M4); ExecSelftest72 §1 and `:194` |

## 3. Gates run (verbatim outcomes)

Scratch: `/fast/scratch/hyaku/kotodama-r75/ScribeQualityFinal/` (git fixture for the two criterion-27 controls, verified
with `git -C "$D" rev-parse --show-toplevel` → the fixture path before its first commit). The directory was removed at the
end of this seat; every output it produced is transcribed below. Two controls were built as one-row-per-fixture lesson
files over a copy of `reports/round-74/evidence/S883.txt`.

**Criterion 27, red-before on round-74 bytes** (block 0 of the staged file, `_ f556d10 corpus/lessons/round-74.md`):

```
exit 1
NO-FIELD | staged S882 (Сидорова/Шувалова PDF) is not app
NO-FIELD | staged S895's folded passage (王昕玥, 论《龙族》的叙事失控与
NO-FIELD | staged S899's quoted span was absent from the
NO-FIELD | staged S900's quoted span was the Sowers-Wills
```

**Criterion 27, controls** (same block, fixture `HEAD`):

| fixture | exit | verdict line |
|---|---|---|
| reason names `reports/round-74/evidence/S883.txt`, asserts 「这个我肯定考虑过。」 `absent` | 0 | `OK reports/round-74/evidence/S883.txt count=0` |
| same row with 「非凡特性来自最初造物主」 | 1 | `MISFILED reports/round-74/evidence/S883.txt count=1 (reason asserts absence)` |
| reason asserts 「非凡特性来自最初造物主」 `present` | 0 | `OK … count=1` (`count=3` for 「先做的是世界观」) |
| reason asserts 「这个我肯定考虑过。」 `present` | 1 | `MISFILED … count=0 (reason asserts presence)` |
| reason with no artifact and no span | 1 | `NO-FIELD | staged S997's quoted span was absent from the` |

**The span counts behind the round-74 red** (`git grep -c`/`grep -c` over the committed captures):

| span | `S883.txt` (2025 page) | `S884.txt` (2022 page) |
|---|---|---|
| 「非凡特性来自最初造物主」 (staged S899's own anchor) | 1 | 0 |
| 「这个我肯定考虑过」 (register S816's span) | 0 | 1 |

So the filed reason "staged S899's quoted span was absent from the page it was bound to" is true of the register's span on
the register's artifact and false of the staged row's span on the staged row's own URL — the defect criterion 27 names.

**Criterion 28, red-before and pins** (block 1 of the staged file):

| counter | output | note |
|---|---|---|
| `reports/round-74/accept-c.py` | `tools/check-cited-lines.py` | `leg_citedlines` runs it from `mat` (`:1423`); `grep -cE '"[0-9a-f]{64}"'` over the counter = **0**; selftest writes the real tool into its fixture lane (`:2493-2495`), only CITEDLINES mutant is `multi_id_line` (`:2751`) |
| the same bytes with `TOOL_SHAS = {"tools/check-cited-lines.py": "a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a"}` prepended | *(nothing)* | the green side of the same one-liner |
| `reports/round-74/accept-ca.py` | *(nothing)* | its `subprocess` calls run the frozen ledger's allowlisted system executables, never a repository tool |

**Criterion 23 addendum, both limbs** (blocks 2 and 3 of the staged file):

| command | output |
|---|---|
| limb 1 over `reports/round-72/accept-c.py` | `GROUND_RECEIPT` |
| limb 1 over `reports/round-73/accept-c.py`, `reports/round-73/accept-ca.py`, `reports/round-74/accept-c.py`, `reports/round-74/accept-ca.py` | nothing (round 73 writes `GROUND_RECEIPT` from `GROUND_RECEIPT_TEXT` inside its fixture, `:1596`) |
| limb 2, `head -2 reports/round-74/telemetry/selftest-ca.txt \| grep -q 'clean -> exit=0'` | exit 0; line 2 is `selftest: clean -> exit=0 … STAMP=PASS` |
| limb 2 over round 72 | no receipt exists: `git grep -c SELFTEST f556d10 -- reports/round-72/telemetry` exits 1; `git ls-tree --name-only f556d10 reports/round-72/telemetry/` lists eight receipts, none a selftest |
| the re-point commit | `git show 5897ddf -- reports/round-72/accept-c.py`: `+GROUND_RECEIPT = …`, `- receipt = show(root, lands, RECEIPT)` / `+ … GROUND_RECEIPT`, and **no** `build_fixture` hunk (3 files, 15 insertions, 9 deletions) |
| the red-before the addendum cites | `.ufo/waves/round-74/w1/ExecSelftest72.md:37-38`: `SELFTEST: 10/11` / `--- clean fixture: expected PASS 10/10, got exit=1` |
| round-74 enforces a green clean fixture | `reports/round-74/accept-c.py:2858-2875`, `:3013` (`return 0 if passed == total else 1`) |

**Append candidates and witnesses**: base `corpus/QUALITY.md` sha256 `243234017470bf1defe6a5c62bc232f077d5b7aaa31ab33d40ea1f26c910a85a`; base + append = 72 insertions / 0 deletions. Machine witnesses the REPAIR leg can grep, base → candidate:
`re-pointed read path` 0 → 1; `green first` 0 → 1; `names the artifact it was observed on` 0 → 1; `pinned at the freeze` 0 → 2.

## 4. Findings

1. **A w1 attribution is false and must not be carried into the counter.** `drafts/quality-additions.md` says the
   addendum's machine witness is "the L75-07 REPAIR pair's observation (`git grep -c 're-pointed read path' <base> --
   corpus/QUALITY.md` → 0 at base, 1 at `<lands>`)". Measured: `reports/round-75/ledger.json` L75-07 is the SHONEN
   `10 rejected` pair (`observe_cmd` = `git grep -c -E '^\|[[:space:]]*S[0-9]{3,}.*\|[[:space:]]*rejected[[:space:]]*\|' …
   corpus/SOURCES.md`, `expected_after` 37); **no ledger pair names `corpus/QUALITY.md`**. The grep value itself is true
   (base 0), but its attribution is not. The round-75 counter must check the QUALITY.md additions from claim Ca's
   `fixed_surfaces` text ("criterion 23 addendum …", "criterion 27 …") and the REPAIR leg's own wording, not from a
   ledger pair.
2. **Criterion 28 exceeds claim Ca's declared QUALITY surface.** `reports/round-75/claims.json` claim Ca `fixed_surfaces`
   names exactly two QUALITY.md entries (the criterion-23 addendum and criterion 27), and its `after` text says "QUALITY 23
   addendum + criterion 27". Criterion 28 is a third appended block. Nothing in the claim's legs fails because of it
   (APPENDONLY forbids removed lines only; REPAIR checks that the two declared additions are present), and the `after`
   sentence stays true as a lower bound — but landing it makes the after-state an understatement. The L1 decides: keep the
   superset, or delete block 3 (`28. …` to the end of its `Limits`/`Grounded in` lines, delimited by the blank line before
   the `Addendum to criterion 23` paragraph). I did not edit `claims.json` or `ledger.json`.
3. **The round-74 CITEDLINES survivor recurs in round 75, and criterion 28 cannot close it.** Claim C's frozen-pending
   leg text is "CITEDLINES: `tools/check-cited-lines.py` over the entries from the materialized tree prints
   `CITED-LINES: 0 finding(s)`" — the same wording MutPredicateC F1 defeated with a four-line stub. Criterion 28 binds
   from round 76 because the round-75 claim text is final for this wave. If round 75 is to be covered, the claim's leg
   text must gain the pin pre-freeze (L1/ExecCtrCfgMain), not the criterion.
4. **The criterion-23 addendum necessarily sits at EOF.** Claim Ca's APPENDONLY leg forbids removed lines, not insertions,
   so a mid-file addendum would also be legal — but an `.append` can only grow the file at its end. The block carries an
   explicit label and states why; a reader arriving from criterion 23 finds it by that label.
5. **No duplication claimed.** Criterion 27 says how it differs from criterion 12 (which asks for the re-test output, not
   the artifact identity); criterion 28 says how it differs from criteria 19/23/26 (constants are pinned there, tools are
   not). Neither restates an existing rule.
6. **The criterion-27 check has one known false negative**: a reject row that names an archived capture URL rather than a
   repo path is not read by the one-liner and falls to review. Stated in the criterion's `Limits`.

## 5. Touched surfaces

- Written (2 files): `.ufo/waves/round-75/w2/stage/corpus/QUALITY.md.append` and this report.
- Not written: `corpus/QUALITY.md` itself, `reports/round-75/claims.json`, `reports/round-75/ledger.json`,
  `reports/round-75/telemetry/**`, `corpus/lessons/**`, `SCORECARD.md`, `LOG.md`, `SHONEN.md`, `SKILL.md`,
  `corpus/SOURCES.md`, `.ufo/state`, `.ufo/watchdog.log`, any sibling lane file, anything under
  `/home/vgpnk/Projects/shokunin` (fleet repo), anything under `/home/vgpnk/Projects/shokuknow` or
  `/home/vgpnk/Projects/shokuknow/merge/kotodama`. No staged part outside the file above; no `/tmp` path is cited.
- Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeQualityFinal/` created and deleted within this seat.

## 6. Not run (stated, not hidden)

- No round-75 counter exists yet, so none was graded; no selftest was executed. The round-74 counters were **read**, not
  re-run: the "stub landed `LEG PASS CITEDLINES`" fact is MutPredicateC's executed measurement (`.ufo/waves/round-74/w2/
  MutPredicateC.md:59-76`), not mine.
- No live fetch and no CDX probe, so no User-Agent/HTTP record belongs to this seat.
- The round-75 Gate does not exist, so criterion 27's first real grading target is round 75's own Gate section; its
  red-before is round 74's filed rows.
