# RevCensusE12 — E12/E11 repair verification (round 67)

Seat `L1-kotodama-r67.RevCensusE12` (UFO-FSD reviewer, leaf). Read-only over the lane;
no git/jj writes; nothing installed or upgraded (bash, coreutils, gawk, python3, git only).

Targets: `corpus/SOURCES.md` at lane tip `b78f8b8e` (file == base `ad5b52b0…` for this
path — `git status --porcelain corpus/SOURCES.md` empty), sha256
`8811130821ec57e3b03ede213c271fca0bfa35ecd5720a60fb1dbc50d37e266e`, 852 lines, 724
row-shaped lines. Instrument: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
(`validate`), the binary the Ca D2 leg shells out to (`reports/round-67/accept-ca.py:165`).

## Verdict

**The E12 half of the repair plan is sound; the E11 half is insufficient and the declared
repair as written does not reach census exit 0.** The minimal "move the 23 rows + flip
S753's used-by" edit (`V2` below) converts E12×23 + E11×1 into a **new E04**:
S776 duplicates S753's live URL *and* scope with no `supersedes S753` in its teaches cell,
and S776's cell is immutable under `accept-c.py`'s APPEND leg. Exit stays 1. A one-cell
status flip on the older row (S753 `mined`→`rejected`) clears it and is APPEND-legal
(`V4`), but it is **not** covered by accept-c's declared flip ("the one declared in-place
flip is S753's used-by cell") — the L1 has to record it. That flip is not an improvisation:
`corpus/QUALITY.md` criterion 18 names S753 by id as a durability failure ("round-65 row
S753 carried a committed capture whose id_ replay answered a 302-stub … the fix lands as a
new row … or a superseding ID"), so the base registry's `mined` S753 is already a
criterion-18 violation and the declared E11 fix alone would leave it one.

## 1. Exact inventory of the 23 misplaced rows

`## Registry` starts at line 26; the table runs **S001–S775 through line 731**; line 732 is
blank; `## Paths` 733, `## Search log` 768, `## Leads (unopened)` 780. A contiguous block
of 23 row-shaped lines sits at the **very end of the file inside `## Leads (unopened)`**,
immediately after line 829 (`- Liebenberg on persistence hunting.`) with no heading and no
blank separator:

| lines | id | used-by |
|---|---|---|
| 830 | S776 | `corpus/knowledge/culture-material/games-play-sport-contests.md` |
| 831 | S779 | `…/scent-perfume-aromatics-codes.md` |
| 832 | S780 | same |
| 833 | S781 | same |
| 834 | S782 | same |
| 835 | S783 | same |
| 836 | S784 | same |
| 837 | S785 | same |
| 838 | S786 | same |
| 839 | S787 | same |
| 840 | S788 | same |
| 841 | S789 | same |
| 842 | S790 | same |
| 843 | S791 | same |
| 844 | S792 | same |
| 845 | S793 | same |
| 846 | S794 | same |
| 847 | S795 | same |
| 848 | S796 | same |
| 849 | S797 | same |
| 850 | S798 | same |
| 851 | S799 | same |
| 852 | S800 | same |

= **S776 + S779–S800 = 23**. S777/S778 exist nowhere in the file (ids are non-contiguous
by design; the census does not require contiguity). This matches `accept-ca.py`'s
`R66_ROWS = ["S776"] + S779..S800` exactly, and the census `E12` count is 23, not 22.

## 2. The S753 cell

Line **709**, cell 11 (0-based) of 11: value **`-`** (ASCII hyphen-minus, U+002D).
The census skips only the em dash when resolving used-by
(`scripts/sources-census.sh:565`: `[ -n "$path" ] && [ "$path" != "—" ] || continue`),
so `-` is treated as a relative path `<root>/-` and fires
`E11 S753 missing used-by -`. The empty marker used everywhere else in the registry is
**U+2014** (`| — |`, bytes `7c 20 e2 80 94 20 7c`); `W03` tests `usedby=="—"` literally.
The flip must be to U+2014, not to `--`, `–` (U+2013) or `-`.

## 3. Minimal edit

### 3a. The move (accepted)

Cut lines 830–852 and re-insert them **verbatim, in order, immediately after line 731**
(the S775 row), i.e. as the tail of the `## Registry` table before the blank line 732.
Order is already ascending (S775, S776, S779…S800) so no re-sorting is needed and the block
stays where the round's next appended ids (S801–S828) will follow.

Byte-identity of the moved lines matters and is preserved: APPEND compares **by id, not by
line position** — `accept-c.py:353-354` builds `base_set`/`tip_set` dicts from
`ROW_RE` matches with no section filter — so a pure relocation produces
`missing_old=[] appended=0 immutable_violations=[]` (simulated with the leg's own code
against `git show ad5b52b0…:corpus/SOURCES.md`: `append_ok=True` for V1–V4, `False` for V5).
Row id multiset and order are unchanged (724 → 724, `same order True`).

### 3b. The E11 flip is not enough — E04 blocks the plan

S753 and S776 are the **same source page and the same scope**:

- both live URLs normalize to
  `www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf`
  (S753 `…/web/20250926172224id_/…` vs S776 `…/web/20261024111013id_/…`; the census
  `url_of()` takes only the first scheme-bearing URL in the source cell, which is the
  penn.museum one for both);
- both scopes are `mancala family distribution and sowing gameplay`;
- S776's teaches has no `supersedes S753` token.

E04 (`scripts/sources-census.sh:646-649`) fires on the later row of such a pair when both
are non-rejected. Reordering cannot help: whichever of the pair comes second fires.
Adding `supersedes S753` to S776's teaches or changing S776's scope is **impossible under
APPEND** (teaches = cell 6 and scope = cell 4 are inside the `oc[:7]` immutability window,
`accept-c.py:369`), and dropping S776 breaks APPEND (`missing_old=['S776']`, V5) *and*
orphans the games entry's `(S776)` citation. The surviving exits are therefore exactly two
status flips, both legal because APPEND's second branch permits status/recheck/used-by
changes on any base row with `opened` fixed (`accept-c.py:367-370`).

### 3c. Recommended: `V4` — S753 `mined`→`rejected`, used-by `-`→`—`

Rationale from the corpus record, not preference: `games-play-sport-contests.md:5` records
that the mancala bullet was **re-pointed S753 → S776 in round 66** because "S753's 2025
capture proved a redirect-stub (same PDF, fresh capture, sha256-verified)", and line 23
cites `(S776)`. So S753 is the superseded stub and S776 is the live row. Rejecting the
stub keeps the citation honest; rejecting S776 (V3) would leave the entry citing a rejected
row and contradict the r66 note. The census's own selftest blesses this shape —
`E04-rejected-pair-exemption` (`sources-census.sh:379-381`, expects `ok`/exit 0).

The status flip is also what the standing contract already demands: `corpus/QUALITY.md`
criterion 18 lists "round-65 row S753 carried a committed capture whose id_ replay answered
a 302-stub to a later record" as a shown failure and prescribes "is `rejected` for
durability, and the fix lands as a new row carrying the same row-id slot's replacement or a
superseding ID" — S776 is that superseding row. Leaving S753 `mined` after the E11 flip
would repair the census symptom while keeping the criterion-18 violation.

Exact edit on the live file (3 changes, 48 diff lines = 2 for S753 + 23 added + 23 removed):

1. line 709, cell 7 ` mined ` → ` rejected `;
2. line 709, cell 11 ` - ` → ` — ` (U+2014);
3. move lines 830–852 verbatim to after line 731.

Result: `V4-flip+s753-rejected.md`, sha256
`1b0755042b6bfed43725982edbda4f713ab8d278cbdf56592ff62d2861cf2798`, 852 lines, row
multiset and order identical to base.

**Caveat for the L1 (must be recorded, not silently taken):** the flip is legal in code but
outside accept-c's declared allowance (`ALLOWED_FLIP={"S753"}` only authorizes the *used-by*
cell, `accept-c.py:72,365-366`; the docstring says "the only allowed in-place flip is
S753's used-by cell"). It also cannot carry a rejection *reason*: APPEND forbids editing
S753's teaches, so the registry will show a substantively-described source with status
`rejected` and no stated grounds — the reason survives only in the entry's `verified-at`
line and must be restated in the round's LOG/manifest. If the frozen instruments must not
be widened, the honest alternative is to leave S753 mined with `—` and accept that
**Ca D2 is unachievable this round** (census exit 1, D2 fails); that is a claim-design
decision, not a repair.

## 4. Receipts (all runs: `sources-census.sh validate --today 2026-10-24`)

Copies were placed at `<scratch>/corpus/SOURCES.md` with `<scratch>/corpus/knowledge`
symlinked to the lane, because `--file` resolves used-by against
`realpath(dirname(file)/..)` (`sources-census.sh:497-503`) — a copy kept anywhere else
produces **662 phantom E11** lines (observed once, discarded). Scratch root:
`.ufo/waves/round-67/w1/RevCensusE12.scratch/`.

| variant | edit | exit | codes |
|---|---|---|---|
| base (`git show ad5b52b0:corpus/SOURCES.md`) | — | **1** | E12 ×23, E11 ×1, W04 ×27, W03 ×0 |
| live tip | == base | 1 | identical to base |
| V1 | move only | **1** | E12 ×0, E11 ×1 (`S753 -`), **E04 ×1** (`S776`), W04 ×27 |
| V2 | move + S753 `-`→`—` (**the declared repair**) | **1** | E11 ×0, **E04 ×1** (`S776`), W03 ×1 (`S753 mined but unused`), W04 ×27 |
| V3 | V2 + S776 `mined`→`rejected` | **0** | W03 ×1, W04 ×27 (28 warnings) — but S776 is the row the entry cites |
| **V4 (recommended)** | V2 + S753 `mined`→`rejected` | **0** | **W04 ×27, W03 ×0**, `ok` |
| V5 | move + S753 `-`→`—` + S776 deleted | 0 | W03 ×1, W04 ×27, but APPEND `missing_old=['S776']`; entry citation orphaned |

V4 stdout (`RevCensusE12.census-V4.txt`, sha256 `17705294e100a1c091a09d89a7b2df32b1abffa03f309c3fd279856f997a97fd`) is
one `ok` line plus exactly 27 W04 lines with the same ids, URLs and scopes as base
(`diff` of `(code,id…)` columns base vs V4 → `IDENTICAL 27`):

```
file	ok	<scratch>/corpus/SOURCES.md
… W04 ×27: S127 S128 S129 S130 S131 S132 S133 S185 S186 S358 S482 S483 S485 S490
           S561 S564 S565 S566 S569 S570 S571 S572 S573 S648 S649 S650 S651
```

No E-code remains, W01/W02/W03 do not fire, and `## Paths` / `## Search log` /
`## Leads (unopened)` are byte-unchanged apart from losing the 23 tail rows.

### The "same 28" figure is wrong for the recommended repair

Base has **27** warnings, all W04, and **zero** W03. The 28 in the plan only appears in
V2/V3 (27 W04 + 1 W03), where the W03 is *manufactured by the S753 `—` flip*, not
pre-existing. Under the recommended V4 the count is **27** (W03 disappears with the
`rejected` status). If the acceptance text is frozen at 28 it will fail V4 for the wrong
reason; it should be restated as "W04 ×27 with base's exact ids, no other warning, exit 0".

## 5. Instrument findings (calibration)

**F1 [HIGH] accept-c's SET/ROWS legs are placement-blind, so claim C alone cannot catch the
r66 defect class.** `reg_lines = [l for l in reg_text.splitlines() if ROW_RE.match(l)]`
(`accept-c.py:236`) has no section filter, so rows parked under `## Leads` satisfy SET,
ROWS, ONEID and RESTATE. Verified on the live file: the SET/ROWS id map contains 724 ids
including `S776` and `S800`, which the census rejects as E12. C's predicate therefore
passes on a registry that the census refutes; only Ca's D2 leg sees placement. Any future
claim that "the registry is clean" must cite the census, not ACCEPT-C.

**F2 [MED] APPEND's declared allowance is narrower than its code, and its own comment
contradicts itself.** `reports/round-67/claims.json` (APPEND leg) and the counter docstring
(`accept-c.py:39-41`) both say "the one declared in-place flip is S753's used-by cell";
`ALLOWED_FLIP={"S753"}` only covers that cell (`accept-c.py:72,365-366`). But the inline
comment (`accept-c.py:350-352`) starts "Status/recheck/used-by cells are mutable in place"
and the code branch at `accept-c.py:367-370` indeed permits status/recheck/used-by changes
on **every** base row (`oc[:7]==nc[:7] and oc[8]==nc[8]`). So any base row can be retired
(`mined`→`rejected`) or postponed (`recheck`) without the APPEND leg noticing — and the
recommended V4 relies on exactly that hole while the claim's own wording counts it as a
second, undeclared flip. The leg should either enumerate the permitted row/cell pairs or be
described as "status/recheck/used-by cells are mutable", and the round's declared-flip list
must then include S753's status.

**F3 [MED] D2 forces a records choice the frozen instruments cannot express.** E04's only
in-row escape is a `supersedes Sxxx` token in the *later* row's teaches, and APPEND makes a
base row's teaches immutable. For r66's S753/S776 duplicate the two legs are jointly
unsatisfiable without a status flip, i.e. the round is pushed toward editing a record's
status while being forbidden to write its reason into the row. Criterion 18 sanctions the
status (`rejected` for durability, replacement/superseding id as the fix) and criterion 10's
"a superseding row keeps the reason and the flip" cannot be honoured in-row at all, so the
reason can only live in the entry's `verified-at` line, this round's manifest and LOG. That
should be recorded as the standing repair shape for duplicate pairs: reject the superseded
row, record the reason outside the cells, and never widen teaches for a base row.

**F4 [LOW] D2's placement regex is redundant, not exploitable.** `accept-ca.py:171-183`
only requires `## Registry` ≤ position < first `Leads` heading, which a row in `## Paths`
would satisfy — but census exit 0 is required in the same leg, and the census would raise
E12 there. No exploit; noted so no one "simplifies" the census call away.

**F5 [INFO] The C-APPEND / Ca-D4 id conflict is real, but D4 is id-agnostic — and my repair
feeds it.** accept-c's APPEND rejects any new id outside `NEW_IDS ∪ EXTRA_IDS`
(`accept-c.py:357-360`), while accept-ca's D4 requires `rej_opened_today >= 6`
(`len(R66_REJECTS)=4` plus 2, `accept-ca.py:226-228`). D4 counts **any** row whose status is
`rejected` and whose opened cell is `2026-10-24`, anywhere in the file — not new ids
(measured at base: 49 rows opened `2026-10-24`, **0** of them rejected, S753 among the 49).
So a
base row already opened today can be rejected within APPEND's allowance (status mutable,
opened fixed) and count; my recommended V4 does that for S753 (opened `2026-10-24`),
supplying one of the two "extra" rejects with **zero new ids**. "Jointly unsatisfiable" is
therefore too strong; what is genuinely blocked is adding *new* reject ids S829+ while
claim C's own APPEND is evaluated at the same revision. The L1's mid-run ruling resolves it
by per-claim lands separation (C at `A_c` where only S805–S828 append over base; Ca at
`A_ca` carrying the S829+ rejects; `A_r` carrying S801–S804 before `A_c`), and my edit is
compatible: the diff at `A_c` is 23 relocated rows + S753's status/used-by flips (APPEND
branch 2) + S805–S828; D4 at `A_ca` then sees S801–S804 + S829+ + S753 ≥ 6.
Calibration residue: because D4 counts provenance-free today-dated rejections, its
"≥2 beyond S801–S804" can be satisfied by durability rejections unrelated to the r66
defects. D4 measures a count, not that the rejects are the round's frontier.

## 6. Residual risk / verification gaps

- I did not run `accept-c.py` or `accept-ca.py` end to end: at base there is no
  `medicine-healing-codes.md` and no S805–S828 rows, and ACCEPT-C's STAMP leg needs a
  materialized clone at the lands commit. My APPEND evidence is a faithful re-implementation
  of `accept-c.py:352-372` over `git show ad5b52b0:…` vs each variant (same regex, same
  branches, same id-keyed dicts), not the counter binary itself.
- V3/V4 both flip a *base* row's status. Neither accept-c nor accept-ca asserts anything
  about base-row statuses beyond APPEND, so this passes, but it is a records change that
  the round's manifest and LOG must state explicitly; I did not audit `reopen-row.py` or
  QUALITY criteria for a conflicting rule about rejected rows in the Registry.
- The move is verified only against this file. `sweep.py` reads `corpus/README.md` +
  `corpus/knowledge/**` and not `SOURCES.md`, so it is insensitive to the move; I did not
  execute it.
- L1 ruled mid-run (IRC) that the C-APPEND / Ca-D4 id conflict is handled by per-claim
  lands separation (`A_r` S801–S804 → `A_c` S805–S828 with claim C stamped there → `A_ca`
  S829+ rejects and the round-67 lesson), with no counter or claims revision. I verified the
  ruling is compatible with my edit (F5) but did not run any counter at a lands commit, so
  the sequencing itself is unverified from this seat.
- `E11` for other rounds' rows is clean at base (only S753), so the fix list is complete;
  if r67 appends S801–S828 the same E11/E12/E04 checks must be re-run on the lands clone.

## 7. Scratch artifacts (all under `.ufo/waves/round-67/w1/`)

| file | sha256 (first 20) | role |
|---|---|---|
| `RevCensusE12.census-base.txt` | `175518a64fed475536f4` | base receipt (exit 1) |
| `RevCensusE12.census-V2.txt` | `5686877ef57672189f8a` | declared-repair receipt (exit 1) |
| `RevCensusE12.census-V4.txt` | `17705294e100a1c091a0` | recommended receipt (exit 0) |
| `RevCensusE12.V1-move-only.md` | `7a70a0d045fc4f465b04` | variant |
| `RevCensusE12.V2-move+flip.md` | `95aeea6a4227775ca69a` | declared repair |
| `RevCensusE12.V3-flip+s776-rejected.md` | `daae59795e1ef70a4ca0` | alternative (contradicts citation) |
| `RevCensusE12.V4-flip+s753-rejected.md` | `1b0755042b6bfed43726` | **recommended patch** |
| `RevCensusE12.V5-drop-S776.md` | `4f0e251d236c26c72b65` | rejected (APPEND fails) |
| `RevCensusE12.scratch/corpus/` | — | scratch root with `SOURCES.md` + `knowledge` symlink |

These are receipts for a reviewer, not deliverables; they are not inputs to any counter.

Report: .ufo/waves/round-67/w1/RevCensusE12.md
