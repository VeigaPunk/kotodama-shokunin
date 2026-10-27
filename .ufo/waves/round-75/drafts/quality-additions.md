# QUALITY additions — round 75 (drafts; not landed)

Seat ScribeQuality (leaf, wave 1). Lane base `f556d1049fe651d3d63975600b13acd9fb686f15`. Two pure
insertions into `corpus/QUALITY.md`, both append-shaped: (1) an addendum paragraph under criterion 23,
sitting between criterion 23 (`corpus/QUALITY.md:77`) and criterion 24 (`:79`); (2) a new criterion 27
appended after criterion 26 (end of file). No base line is removed or rewritten, so the claim-Ca
APPENDONLY leg ("zero removed lines in `corpus/QUALITY.md` below the highest criterion existing at
base") passes for both, and the L75-07 REPAIR pair's observation (`git grep -c 're-pointed read path'
<base> -- corpus/QUALITY.md` → 0 at base, 1 at `<lands>`) is the machine witness for the addendum.
Everything measured below was run read-only against the lane and a fresh `--shared` clone at
`/fast/scratch/hyaku/kotodama-r75/ScribeQuality/lane-clone` (which is where the ANNOTATE/observe legs
run); no live fetch was made, so no User-Agent is recorded, and no tool was installed.

---

## (1) Addendum under criterion 23 — verbatim insertion text

> Insert as one block immediately after criterion 23's paragraph and before `24. **A CDX "no capture"
> probe …**`. Style copied from the existing "Hold on criterion 16's check (appended 2026-10-23)"
> continuation notes.

```markdown
Addendum to criterion 23 (appended 2026-10-27, round 75) — **a re-pointed read path lands with its
fixture in the same commit, and each mutant's redness is shown against a fixture that is green
first.** The first limb is mechanical: when a leg's read path moves (a receipt constant, a tree root, a
path template), the fixture that writes that artifact moves in the same commit, and the selftest run
after the move shows the clean scenario passing — a commit that re-points the read and leaves
`build_fixture` writing only the old path leaves the clean fixture reading a file it never creates. The
second limb says what a caught mutant proves: a mutant's `LEG FAIL <leg>` counts only when the clean
fixture it is compared against was green in the same run, because a mutant that fails for the
baseline's own reason is indistinguishable from one that fires. The selftest receipt therefore carries
the clean scenario's verdict beside the mutant rows (round 74: `selftest: clean -> exit=0 LEDGER=PASS
…`; round 72 carried no such line and no selftest receipt at all).

Check (red-before, pre-dispatch), both limbs one-liners over a counter source:

(i) the receipt-path constants the counter defines at module level that the body of its
`build_fixture` never names —
`bash -c 'f=$1; defined=$(grep -oE "^[A-Z][A-Z0-9_]*RECEIPT[A-Z0-9_]*[[:space:]]*=[[:space:]]*\"" "$f" | grep -oE "^[A-Z][A-Z0-9_]*" | sort -u); infix=$(awk "/^def build_fixture\(/{inside=1;print;next} inside && /^def /{inside=0} inside{print}" "$f" | grep -oE "[A-Z][A-Z0-9_]*RECEIPT[A-Z0-9_]*" | sort -u); comm -23 <(printf "%s\n" "$defined") <(printf "%s\n" "$infix")' _ <counter>`
prints nothing for a coherent counter and the moved constant for a broken one;

(ii) the committed selftest receipt names its clean scenario at a passing exit before the mutant rows.

Measured 2026-10-27 at lane base `f556d10`: limb (i) prints `GROUND_RECEIPT` for
`reports/round-72/accept-c.py` and nothing for `reports/round-73/accept-c.py` (which writes
`GROUND_RECEIPT` from `GROUND_RECEIPT_TEXT` inside its fixture, `:1593`/`:1596`),
`reports/round-74/accept-c.py`, `reports/round-73/accept-ca.py` and `reports/round-74/accept-ca.py`;
limb (ii) holds for round 74 (`reports/round-74/telemetry/selftest-ca.txt:2` is the clean scenario at
`exit=0` with every leg `PASS`; `selftest-c.txt` is `SELFTEST: 69/69 scenarios`) and fails for round 72
(`git grep -c 'SELFTEST' <base> -- reports/round-72/telemetry` exits 1 with no line: eight receipts,
no selftest receipt).

Grounded in `corpus/lessons/round-74.md` `## Routed to round 75` item 4 (the R73-M4 decision; no
corrected successor to `reports/round-72/accept-c.py` is warranted because its real-mode GROUND leg
passes on real bytes and `reports/round-73/accept-c.py` already writes the receipt its leg reads and
cross-checks the row count against the graded tree) and the measured case in
`.ufo/waves/round-74/w1/ExecSelftest72.md` §1–§2 and §6 item 2 — `SELFTEST: 10/11` beside `--- clean
fixture: expected PASS 10/10, got exit=1`, commit `5897ddf` re-pointing `leg_ground` from `RECEIPT` to
`GROUND_RECEIPT` with `build_fixture` untouched, and the `ground_zeros` mutant mutating the now-unread
`RECEIPT_TEXT` so it failed for the baseline's reason. Binds from round 75; no earlier counter is
re-run or retro-fitted.
```

### Grounding, measured (lane base `f556d10`, 2026-10-27)

| fact | command | output |
|---|---|---|
| the re-point defect exists and is detectable | limb (i) over `reports/round-72/accept-c.py` | `GROUND_RECEIPT` |
| successors are coherent | limb (i) over `accept-c.py` r73, `accept-c.py` r74, `accept-ca.py` r73, `accept-ca.py` r74 | empty (exit 0) |
| r73 writes what its leg reads | `grep -n GROUND_RECEIPT reports/round-73/accept-c.py` | `:109` def, `:852`/`:861` leg read, `:1596` `git_write(lane, GROUND_RECEIPT, ground)` |
| the re-point commit moved the read only | `git show 5897ddf -- reports/round-72/accept-c.py` | `+GROUND_RECEIPT = "reports/round-72/telemetry/gap-sweep.txt"`; `- receipt = show(root, lands, RECEIPT)` / `+ … GROUND_RECEIPT`; no `build_fixture` hunk (commit touches 3 files, 15 insertions, 9 deletions) |
| the red-before count | `.ufo/waves/round-74/w1/ExecSelftest72.md:37-38` | `SELFTEST: 10/11` / `--- clean fixture: expected PASS 10/10, got exit=1` |
| round 72 captured no selftest | `git grep -c 'SELFTEST' f556d10 -- reports/round-72/telemetry` | no output, exit 1 |
| round-72 telemetry inventory | `git ls-tree --name-only f556d10 reports/round-72/telemetry/` | 8 receipts (`baseline`, `census-start`, `census-end`, `controls-c`, `controls-ca`, `gap-sweep`, `measures-c`, `measures-ca`); none is a selftest |
| round 74 carries the clean-first verdict | `head -2 reports/round-74/telemetry/selftest-ca.txt` | `selftest: do-nothing -> exit=1 …`; `selftest: clean -> exit=0 LEDGER=PASS … STAMP=PASS` |
| round 74 enforces a green clean fixture | `reports/round-74/accept-c.py:2857-2875` (`scenario("clean")`, `expected PASS 13/13`, `return 0 if passed == total`) | a red clean fixture fails the selftest, not a mutant |

Limits, stated: limb (i) is a name-shape grep — a path built inline (`open(ROOT + "/telemetry/x.txt")`)
or reached through an alias escapes it, and it cannot prove the fixture writes the *same* path a leg
reads, only that the constant is named inside the fixture; limb (ii) reads the receipt, so a receipt
typed without the run is governed by criterion 23's first limb (`STAMP`, `QUALITY 17/19`), not here.
The second limb names the round-72 symptom (a mutant judged against a red baseline) and cannot prove
mutation coverage: a green-first run still cannot show that a mutant *would* fire on a predicate nobody
mutated (that stays criterion 11's ground).

---

## (2) Criterion 27 — verbatim append text

> Append after criterion 26 at the end of `corpus/QUALITY.md`.

```markdown
27. **A reject reason names the artifact it was observed on** — adds to criteria 10, 12, 18 and 21. A
reject reason names the artifact it was observed on: a staged row's own anchor/quote is tested against
its own URL's capture, a register row's against the register's pairing, and a reason observed on one
artifact is never filed against another. The row names its artifact (the staged id and its URL, or the
register row and its pairing), the tested span is the row's own anchor or quote and not a neighbouring
row's, and where both artifacts are in play the row says which one it tested and which one it bridges —
the refused register rows stay refused while the document is re-opened as its own row. Check: a Gate
reject row that names another artifact's span as its reason is rewritten before landing. Pre-dispatch,
the scan re-opens each reject row's own capture and prints `<row-id> <own-url> <count-of-the-reason's
span>`; a row whose reason asserts absence must print 0, and a count of 1 or more means the reason was
observed on another artifact — round 74's staged S899 and S900 rows print 1 on
`reports/round-74/evidence/S883.txt` and `…/S884.txt`, the pages each names, while the absence belongs
to register S816's `这个我肯定考虑过…` bound to the 2025 URL and register S817's Sowers-Wills clause
bound to the 2022 URL. Limits, stated: a grep cannot tell whose clause a quoted span means, and a reason
that names no span at all is criterion 12's subject, not this one; that the named artifact is the one
the observation was made on is review-only (criterion 11). Binds from round 75; no earlier Gate line is
retro-fitted — round 74's filed rows stand as filed and are annotated under `## Corrections — round 75`.
Grounded in the round-74 closure's routed defect R2 (`reports/round-75/claims.json` claim Ca `before`;
`reports/round-75/ledger.json` L75-05/L75-06 `why`) and `corpus/lessons/round-74.md` `## Quarantine`
R74-M5: the register's `census-adjudication.json` entries S758/S759 carry row N's `url` with row N+1's
`quote`, so each register URL is bound to the next row's quote, while the staged rows' own anchors are
present on the pages they name — measured in `.ufo/waves/round-74/w2/RevLessonGate.md` F1
(`非凡特性来自最初造物主` 1 hit on the 2025 page, `这个我肯定考虑过` 1 hit on the 2022 page, at its
`:55-:63`) and `.ufo/waves/round-74/w2/ScoutRejectProbes.md` F2 (the Sowers-Wills clause is staged row
S901's anchor, `:72`), against the reasons as filed at `corpus/lessons/round-74.md:37-38`.
```

### Grounding, measured (lane base `f556d10`, 2026-10-27)

| fact | command | output |
|---|---|---|
| the two reject rows as filed | `git show f556d10:corpus/lessons/round-74.md \| sed -n '37,38p'` | `staged S899's quoted span was absent from the page it was bound to (register S816 mispairing; …)`; `staged S900's quoted span was the Sowers-Wills clause, absent from this page (register S817 mispairing)` |
| staged S899's own anchor is on its own page | `git grep -c '非凡特性来自最初造物主' f556d10 -- reports/round-74/evidence/S883.txt` | `f556d10…:reports/round-74/evidence/S883.txt:1` |
| staged S900's own anchor is on its own page | `git grep -c '这个我肯定考虑过' f556d10 -- reports/round-74/evidence/S884.txt` | `f556d10…:reports/round-74/evidence/S884.txt:1` |
| the absence is the register's | `corpus/lessons/round-74.md` `## Mistakes` R74-M5 (`:172`), `## Quarantine` bridging (`:143-144`), routed item 5 (`:211`) | S816/S817 bind each URL to the *next* row's quote; "a row's `url` and `quote` must be read from one row" |
| the wave-2 measurement behind it | `.ufo/waves/round-74/w2/RevLessonGate.md:42-83`; `.ufo/waves/round-74/w2/ScoutRejectProbes.md:63-72` | 1/0 per page per span; Sowers-Wills clause = staged S901's anchor; the S883/S884 "re-quote" is not a re-quote |
| the bridge the row must state | `.ufo/waves/round-74/w1/ScoutQuarantine816817.md:59` | "staged S899 (2025 URL) … staged S900 (2022 URL) … each pairing is correct against the live bytes" |
| red-before for the check (this criterion, on round-74 bytes) | the two `git grep -c` rows above | a reject reason asserting absence on an artifact whose own window returns 1 → the check fires on the filed rows |

Limits of this criterion as drafted, stated for the L1: the check is a per-row re-open, not a section-wide
grep, so a round that files no reject row has nothing for it to grade (it binds the reason, not the
count); and a reason that is false for a *third* reason (the span is on neither artifact) still passes
the absence limb and must be caught by re-opening the named artifact, which the criterion says but no
grep enforces.
