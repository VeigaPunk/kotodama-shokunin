# ScribeQuality — round 76, wave 1 (QUALITY.md additions, staged)

Seat: ScribeQuality (leaf; no dispatch). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `98c486bdb4650ba5b8e651d332910e8ee60ad121` (unmoved; `git -C <lane> rev-parse HEAD` printed it at the
end of the seat). Fleet root was never written; no lane tracked file was written; `git -C <lane> status
--porcelain` ends as:

```
?? .ufo/waves/round-76/
?? reports/round-76/
```

**Verdict.** Three append blocks staged as
`.ufo/waves/round-76/w1/drafts/quality-additions.md` (19,712 bytes, 91 lines): criterion **29** (supersedes 27),
criterion **30** (R75-M2 receipt↔anchor binding), and an **Addendum to criterion 18** (R74-M5 register
adjacency guard). Highest criterion at base is 28, so 29 is the next free number. Every check embedded in the
draft was executed twice: once from its receipt file and once extracted from the draft's fenced block (byte-equal
apart from the trailing newline). No candidate was dropped; the reason each check can fail is measured below,
and the one candidate whose red is a recomposition rather than a landed byte is flagged as such.

## Axes

- **Calibration (Ca):** the instrument that grades the round's own Gate rows was measured against the round-75
  reject table and found blind; criteria 29 and 30 are the repair, each with a red-before on base bytes.
- **Coverage (C):** no new source was opened by this seat; the addendum closes a routed item (register
  adjacency guard) with a check, not with an entry.

## Measurements

All commands were run read-only, from the lane root, at `98c486b`. Scratch fixtures lived under
`/fast/scratch/hyaku/kotodama-r76/ScribeQuality/` (deleted at the end; fixture file content copied to
`stage/ScribeQuality/fixture-src/`).

### F0 — the numbering this draft appends under

```
$ grep -oE '^[0-9]+\.' corpus/QUALITY.md | sort -n | tail -3
26.
27.
28.
$ grep -c '' corpus/QUALITY.md
197
```

Highest numbered criterion at base is 28 (an `Addendum to criterion 23` follows it at the file's end), so the
draft appends `29.`, `30.`, then `Addendum to criterion 18`.

### F1 — criterion 27's selector matches none of round 75's reject rows (verifier §7 item 3)

```
$ git show 98c486b:corpus/lessons/round-75.md | grep -cE '^\|.*\| *refused *\|$'
0
$ git show 98c486b:corpus/lessons/round-75.md | grep -cE '^\|.*\|[[:space:]]*([Rr]efused|[Rr]ejected)[^|]*\|[[:space:]]*$'
4
$ git show 98c486b:corpus/lessons/round-74.md | grep -cE '^\|.*\| *refused *\|$'
4
$ git show 98c486b:corpus/lessons/round-75.md | sed -n '/^| reason | flip | probed URL | verdict |/,/^$/p' | grep -c '^| '
5
```

The four reject verdict cells (last cell of each row, `sed 's/.*|\([^|]*\)|$/\1/'`):

```
refused as staged; the document re-opened as S893
refused; not used
refused as a live-only anchor
refused as a live-only anchor
```

So the selector misses 4 of 4 rows because the cell carries a qualifier, not because the regex is broken
(round 74: 4 of 4). Criterion 27's own check over round-75 bytes is therefore empty and green:

```
$ ( cd <lane> && sh -c '<criterion 27 one-liner>' _ 98c486b corpus/lessons/round-75.md )
(no output)
exit=0
```
receipt: `stage/ScribeQuality/base-q27-oneliner.out`

### F2 — criterion 29, staged

Check over base bytes (receipt `base-check-29.out`):

```
$ ( cd <lane> && sh -c "$(cat check-29.line)" _ 98c486b corpus/lessons/round-75.md )
NO-FIELD | staged S870's quote `作品中的人物名字和地名也一样…` is absen
NO-FIELD | the article-level PDF endpoint is CAPTCHA-prot
NO-FIELD | the live URL of S891 is not an openable anchor
NO-FIELD | the live URL of S892 answers HTTP 403 with a C
exit=1
```

Red control — same one-liner with 27's selector substituted (`base-check-29-oldsel.out`):

```
EMPTY-SELECTOR heading=Rejections selected=0
exit=1
```

Fixture controls (fixture commit `3488ffbacbb951812d4b35a67cadeaeebec01e75`, files shipped under
`stage/ScribeQuality/fixture-src/`):

```
fixture-check-29-clean.out        OK reports/round-76/evidence-clean/S895.txt count=0
                                  OK reports/round-76/evidence-clean/S895.txt count=1      exit=0
fixture-check-29-misfiled.out     MISFILED reports/round-76/evidence-clean/S895.txt count=1 (reason asserts absence)  exit=1
fixture-check-29-oldsel-clean.out EMPTY-SELECTOR heading=Rejections selected=0             exit=1
```

The span-delimiter limb is measured, not asserted — `«`/`「` counts per anchor cell of S885–S893:

```
S885 guillemets=1 kagi=0   S886 guillemets=2 kagi=0   S887 guillemets=1 kagi=0
S888 guillemets=0 kagi=1   S889 guillemets=1 kagi=0   S890 guillemets=1 kagi=0
S891 guillemets=1 kagi=0   S892 guillemets=1 kagi=0   S893 guillemets=0 kagi=1
```

(7 rows use «», 2 use 「」 — criterion 27 accepted only 「」.)

### F3 — criterion 30 (R75-M2), staged

```
$ ( cd <lane> && sh -c "$(cat check-30.line)" _ 98c486b corpus/SOURCES.md .ufo/waves/round-75/counters/probe-receipts )
S885 MISBOUND=yes OUTSIDE_WINDOW=no
S886 MISBOUND=yes OUTSIDE_WINDOW=no
S887 MISBOUND=yes OUTSIDE_WINDOW=no
S888 MISBOUND=yes OUTSIDE_WINDOW=yes
S889 MISBOUND=no OUTSIDE_WINDOW=no
S890 MISBOUND=yes OUTSIDE_WINDOW=no
S892 MISBOUND=yes OUTSIDE_WINDOW=yes
exit=1
```
receipt: `stage/ScribeQuality/base-check-30.out` (7 receipts: `git ls-tree --name-only 98c486b
.ufo/waves/round-75/counters/probe-receipts/ | grep -cE 'S[0-9]{3}\.txt$'` → `7`)

Fixture: dirty receipts `1 MISBOUND + 1 OUTSIDE_WINDOW, exit=1`; repaired receipts `3 × MISBOUND=no
OUTSIDE_WINDOW=no, exit=0` (`fixture-check-30-dirty.out`, `fixture-check-30-clean.out`).

Corroboration of the window limb by an independent route: `corpus/lessons/round-75.md` Gate notes 1–2 (`:40-52`)
already record that S888's and S892's stored windows stop before the quoted page; this check measures the same
two rows `OUTSIDE_WINDOW=yes`.

### F4 — Addendum to criterion 18 (R74-M5 adjacency), staged

Base control (receipt `base-check-31.out`) — the round-75 evidence set is adjacency-clean, so the limb is green
on landed bytes:

```
$ ( cd <lane> && sh -c "$(cat check-31.line)" _ 98c486b corpus/SOURCES.md reports/round-75/evidence )
S885 OK own=3 … S893 OK own=3        (9 lines)   exit=0
```

Red — the R74-M5 pair recomposed from committed captures (S883.txt/S884.txt copied byte-for-byte from
`98c486b`, register rows carrying the two quotes R74-M5 names):

```
$ ( cd <fixture> && sh -c "$(cat check-31.line)" _ <H> corpus/SOURCES-r74-mispair.md reports/round-74/evidence )
S883 ADJACENT -> S884 (own=0 hits=1)
S884 ADJACENT -> S883 (own=0 hits=1)
exit=1
```

Direct counts behind that recomposition (`stage/ScribeQuality/round74-span-counts.out`):

```
这个我肯定考虑过。      S883 0    S884 1
非凡特性来自最初造物主  S883 1    S884 0
```

Green after repair (`fixture-check-31-r74repaired.out`: two `OK own=1`, exit=0); synthetic one-row swap
(`fixture-check-31-swap.out`: two `ADJACENT`, exit=1); unswapped captures (`fixture-check-31-clean.out`:
three `OK own=1`, exit=0).

### F5 — the draft's own fenced blocks run

Extracted mechanically from the draft (`re.findall(r"```\n(.*?)\n```")` → 4 blocks, 1214/1172/977/1060 chars
without the trailing newline) and executed from the lane root: outputs identical to the receipts above
(criterion 29 → 4 `NO-FIELD`, exit 1; 27-selector control → `EMPTY-SELECTOR`, exit 1; criterion 30 → 6
`MISBOUND` + 2 `OUTSIDE_WINDOW`, exit 1; addendum → 9 × `OK own=3`, exit 0). Each block differs from its
receipt `.line` file by exactly 1 byte (the trailing newline).

## Criteria kept, and the candidate question

- **(i) → criterion 29**, "supersedes criterion 27": kept. Red on base bytes (F2), green on the fixture, and
  the count limb fires on the exact defect the verifier reported (`EMPTY-SELECTOR` where 27 printed nothing).
- **(ii) → criterion 30**, "a receipt's stored quote is the row's anchor cell, and the anchor lies in that
  receipt's own window": kept. Red on base bytes 6/7 + 2/7 (F3), green on repaired fixture. Six of seven
  receipts are title-bound; the check is not vacuous on the bytes that carry R75-M2.
- **(iii) → Addendum to criterion 18**, not a new number: it amends a rule 18 already states (the anchor must be
  findable in a named anchor's body) by fixing what a checker may conclude when it is not. **Stated weakness:**
  its red is a recomposition over committed captures, not a landed lane byte — the round-75 register/evidence
  pair is green at base (F4). This is the only candidate whose base control is green, and it is reported as
  such rather than dressed as a base failure.
- **None dropped.** A candidate would have been dropped if its one-liner could not be shown failing on an input
  that carries the defect; all three can (F2, F3, F4).

## Gates

None. This seat runs no counter, dispatches nothing, freezes nothing. The L1 installs the draft; only the L1
commits.

Unrun, and reported as unrun: `reports/round-75/accept-c.py`, `reports/round-75/accept-ca.py`, the census, and
any fetch (no source was opened by this seat).

## Touched surfaces

Written (all under the lane):
- `.ufo/waves/round-76/w1/drafts/quality-additions.md`
- `.ufo/waves/round-76/w1/stage/ScribeQuality/` — the four check one-liners (`check-29.line`, `check-29-oldsel.line`,
  `check-30.line`, `check-31.line`), `q27-oneliner.txt` (criterion 27's block as extracted from
  `corpus/QUALITY.md:132`), 16 `.out` receipts, `selector-counts.out`, `round74-span-counts.out`,
  `fixture-head.txt`, and `fixture-src/` (the fixture's files, no `.git`).
- `.ufo/waves/round-76/w1/ScribeQuality.md` (this report).

Not written: `corpus/QUALITY.md` (draft only), `corpus/**` in any form, `reports/round-75/**`,
`reports/round-76/**`, `.ufo/state`, `.ufo/watchdog.log`, the fleet repo, `/home/vgpnk/Projects/shokuknow/**`.

## Out of scope

- Deciding whether round 75's four reject rows *should* have been refused. Criterion 29 only makes their shape
  failure visible (`NO-FIELD` ×4); the Gate verdict stays the round's.
- Editing criterion 27 in place, or retro-fitting any earlier Gate line. Criterion 29 binds from round 76.
- The routed counter defects (`accept-c.py` QUALITY 23 limb 1) — not touched, not re-run.

## Tooling

No install, no upgrade, no package operation. Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeQuality/` deleted
after the receipts were copied into the wave dir; `/fast/scratch/hyaku/kotodama-r76` itself untouched.

Report: .ufo/waves/round-76/w1/ScribeQuality.md
