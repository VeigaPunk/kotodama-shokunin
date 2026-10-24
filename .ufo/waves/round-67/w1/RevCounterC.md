# RevCounterC — attack on `reports/round-67/accept-c.py` rev0 vs claims.json claim C

Seat: reviewer (attack), lane kotodama, round 67. Base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`,
lane tip `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21` (counters rev0, pre-data).
Method: line-by-line read of `accept-c.py` (449 lines) against the 13 declared legs in
`reports/round-67/claims.json` (claim C), plus runtime probes in a scratch clone of the lane at
tip (`git clone --no-local`, root `.ufo/waves/round-67/w1/scratch/eval-tip`, removed after use).
Lane repo, jj state and Git index untouched; no installs needed (python3/git only).
`lsp` device is not in this seat's tool inventory, so semantic checks are literal source reads +
runtime probes (recorded per role rule; no server was available to query).

**Leg inventory: all 13 declared legs exist** (`STAMP FILE SET ROWS ONEID RESTATE HOSTS LINK
APPEND NOHARM SWEEP CAPTURE TOPIC`). Two legs diverge from their frozen declaration (F2 weaker,
F3 stronger); one leg's equality check is satisfiable while the counter evaluates different bytes
(F1); two malformed-input paths crash / misclassify (F4, F5); and the recorded control command does
not materialize lands (F9). The C↔Ca id-set conflict (F10) is satisfiable only under L1's sequenced
lands (A_r < A_c < A_ca) and is recorded as a design finding, not a revision request. F1 is not theoretical: the sibling smoke seat produced `ACCEPT-C-67: PASS`
with exit 0 from a clone whose `main == lands` and **zero committed wave bytes**. Counter rev0 should
not be frozen as-is.

---

## F1 — HIGH (receipt discipline): `STAMP` equality is satisfiable while the counter reads bytes that are not in the stamped tree

`accept-c.py:175` derives the *evaluated* revision from `git rev-parse main` of `--root`, but every
evaluated byte is read from the **worktree filesystem**, not from `lands`:
`open(path)` entry (`:213`), `open(root/corpus/SOURCES.md)` registry (`:228`), `open(root/README)`
(`:424`), and `SWEEP` runs with `cwd=root`. Only the *base* read uses git (`git show BASE:...`).
Nothing compares `HEAD`, the checked-out tree, or the untracked set to `lands`; the dirty probe is
`git status --porcelain --untracked-files=no` (`:181`), i.e. untracked files are invisible.

Evidence (scratch clone at tip; `--lands b78f8b8e...`):

- EXP1 — wrote `corpus/knowledge/culture-material/medicine-healing-codes.md` as an **untracked**
  file (not in the lands tree, never committed):
  `STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e dirty_tracked=False`
  then `FILE PASS exists lines=5 h1=1 h2=1 h3=0 topic=True`. A file absent from the stamped commit
  passes FILE, and the receipt's dirty flag says `False`.
- EXP2 — `git checkout --detach ad5b52b0` (main still at tip) →
  `HEAD=ad5b52b0 main=b78f8b8e`, run prints `STAMP PASS ... equal=True`, then
  `FILE FAIL unreadable: .../medicine-healing-codes.md` — the counter evaluated **base** bytes while
  stamping tip. Same result for a branch checkout (`git checkout -b sneak; commit`) or any dirty
  worktree: equality holds, bytes differ.

This is the r66 class the round claims to fix: the docstring (`:17-23`) promises "a clone whose main
moved past lands, or a stale clone, makes evaluated != stamped"; it does not, and claims.json's
"never on a worktree that may have moved past the stamp" is a protocol promise the counter cannot
enforce. A run inside a dirtied clone can therefore produce a PASS receipt whose measured bytes are
not the lands bytes — including hand-crafted "perfect" rows.

Corroborated and completed by the sibling smoke seat (`w1/ExecCounterSmokeC.md` §7): a clone with
`main == lands == ad5b52b0`, an untracked entry plus dirty `corpus/SOURCES.md`/`README.md`, prints
`STAMP PASS … dirty_tracked=True` and **all 13 legs PASS, `ACCEPT-C-67: PASS`, exit 0**, while
`git show main:corpus/SOURCES.md|README.md` are sha-equal to the base blobs and the entry is absent
from `main`. The forged receipt's headers are byte-identical to the committed honest FAIL in
`telemetry/dry-run-c.txt` (same stamped/evaluated/measured/tree/counter-sha), differing only in
`dirty_tracked` and the verdict. `git rev-parse main == --lands` binds a branch name, not bytes.
That also shows the legs have no cross-row freshness check: 24 rows sharing one quote and one
teaches string on 24 synthetic `.example.org` hosts pass `RESTATE`/`HOSTS`/`LINK` (see F8).
Fix: read every evaluated path with `git show {lands}:{path}` (already done for base), or add legs
`HEAD == lands` and `git status --porcelain` (with untracked) empty; make `dirty_tracked` fail STAMP
instead of printing it.

## F2 — HIGH (leg weaker than declaration): `APPEND` allows used-by/status flips on *every* base row

Declared (claims.json, C): "additions bounded to S805-S828 + disposition ids S801-S804; **the one
declared in-place flip is S753's used-by cell**". Body (`:365-372`): after the S753 branch, a second
branch `if len(oc) == 11 and len(nc) == 11 and oc[:7] == nc[:7] and oc[8] == nc[8]: continue` makes
cells 7 (status), 9 (recheck) and 10 (used-by) mutable **on any base row** — contradicting the code's
own comment two lines above ("the only allowed in-place flip is S753's used-by cell").

Evidence EXP3: flipped base row `S100` to `status=rejected` and
`used-by=corpus/knowledge/culture-material/medicine-healing-codes.md` in the scratch clone →
`APPEND PASS missing_old=[] appended=0 extra=[] immutable_violations=[]` (only `dirty_tracked=True`).
Consequence: a build seat can retroactively attach the new entry to arbitrary pre-existing rows
(coverage inflation the claim's "exactly 24 rows … used-by the entry" is supposed to exclude), or
rewrite base grading, and APPEND still passes. Precision (per the sibling smoke seat): `ROWS` does
assert the 24 **new** rows each name the entry (`accept-c.py:272`, `if ENTRY not in c[10]`), so the
gap is not "used-by is unchecked" but "**which** rows name the entry and **how many** is unbounded,
and base rows' used-by/status/recheck cells may flip at will" — APPEND is the only leg that could
bound it and the `:369` branch disables that bound. Note the two defects are independent: the
sibling's §7 PASS (`w1/ExecCounterSmokeC.md`) did not need this looseness at all, so F1 stands alone.
Fix: drop the broad branch (keep only ALLOWED_FLIP); add a leg asserting exactly 24 registry rows
name `ENTRY` in used-by and that no base row (other than S753) changed any cell.

## F3 — MEDIUM (leg stricter than claim text): the declared `no-capture` escape hatch is not implemented

Declared (claims.json, C): "each new row's source cell carries a same-page web.archive.org capture
**or an explicit no-capture reason**"; docstring `:45-46` says the same. Body (`:403-417`) requires
`CAPTURE_RE` unconditionally and has no token branch at all.

Evidence EXP4: appended well-formed row `| S805 | https://example.org/med-text (no-capture:
paywalled, checked 2026-10-24) | book | A | …` → `CAPTURE FAIL bad=['S805:no_capture', …]`.
So a build seat following the claim text fails; the only ways out are fabricating an archive
timestamp (the exact shortcut class this wave attacks) or a mid-round counter revision. Also the
"reason" has no grammar, so even implemented it would be unfalsifiable.
Fix (claim is frozen, body is rev0 → fix the body): require `no-capture:\s*\S+` with a non-empty
reason, reject it when a capture is present, and reject the bare token.

## F4 — MEDIUM (malformed input): short registry row crashes the counter with an untraced verdict

`RESTATE` dereferences `c[5]`/`c[6]` (`:304-309`) and `CAPTURE` dereferences `c[1]` (`:403-404`)
without a `len(cells) == 11` guard; `ROWS` only records `cells=1` and continues.
Evidence EXP5a: row `| S805 |` added under Registry, entry citing `(S805)` once →
`STAMP PASS`, `SET FAIL`, `ROWS FAIL bad=['S805:cells=1'] n=1`, `ONEID PASS`, then
`IndexError: list index out of range` at `quote = anchor_quote(c[5]) or ""`; rc=1, and **no
`ACCEPT-C-67:` line is printed at all**. `main()`'s handler (`:441`) catches
RuntimeError/OSError/SubprocessError/ValueError/KeyError — IndexError escapes. The predicate
("every leg prints PASS") is unsatisfiable but the failure is a traceback with no leg attribution.
Missing anchor *quote* is handled (`or ""`), so only the cell-count path crashes.
Fix: in RESTATE and CAPTURE, `if len(c) != 11: bad.append(...); continue`.

## F5 — LOW/MEDIUM (misclassified fault): a missing row is reported as "infrastructure unusable" (exit 2)

`RESTATE` indexes `reg_by_id[sid][0]` (`:304`) — KeyError when the entry cites an id with no row;
`main()` prints `COUNTER_FAULT infrastructure unusable: KeyError('S805')` and returns 2.
Evidence EXP5b (`SET FAIL missing=[...25 ids...]`, entry cites `(S805)`) → rc=2, one `COUNTER_FAULT`
line then `ACCEPT-C-67: FAIL`. A pure data defect is labelled infrastructure-unusable (the
"unusable input" code), which invites a counter revision instead of a data fix.
Fix: treat absent rows as a RESTATE bad entry (SET already fails).

## F6 — LOW (duplicate bypass): duplicate ids are invisible to APPEND and the row count is unpinned

`base_set`/`tip_set` are dicts keyed by id (`:352-354`), so a duplicated id collapses to one entry;
`extra_ids` only sees ids absent from base. Evidence EXP6: an **identical** copy of base row `S100`
appended → `APPEND PASS … appended=0`, file grew 724 → 725 rows, no leg flagged. A duplicate of an
existing id with *different* content is likewise invisible when placed above the original
(last-wins dict). No leg pins `len(tip rows) == 752` or `len(base rows) == 724` (base measured at
724 today, so the statement's "724 -> 752" is unasserted; the real bound from SET+EXTRA_IDS is
748..752, and Ca D5 covers S801-S804).
Fix: compare ordered row multisets, and assert tip 752 / base 724 explicitly.

## F7 — LOW (section placement unchecked in C's own predicate)

`ROW_RE` (`:73`) matches rows anywhere in `SOURCES.md`; no leg requires S805-S828 between
`## Registry` and the next `##`. The base itself carries 23 rows under `## Leads (unopened)`
(701 Registry / 23 Leads) — the exact r66 D2/E12 defect class. Mitigation exists only cross-claim:
`accept-ca.py:170-190` runs `sources-census.sh validate` over the whole file and fails on nonzero
exit, so E12 rows would break Ca — but C's frozen predicate accepts them, and that census is an
absolute-path script outside the lane repo (`accept-ca.py:54`), so C is not self-contained.
Fix: add a section-position leg in accept-c.

## F8 — LOW (weaker-than-statement details)

- `HOSTS` normalizes only `www.` off `netloc` (`:328-332`): ten subdomains of one site satisfy
  ">=10 distinct normalized hosts"; "normalized" is undeclared.
- `ONEID` scans the whole entry text, so a narrative/handoff mention also counts toward the one
  citation, and any foreign `(S###)` citation (e.g. an r66 id cited for contrast) fails — stricter
  than the declared "cited exactly once by it".
- `TOPIC` uses substring containment against the first README line starting `- ` that contains the
  filename, so a topic string that is a prefix of another entry's row text would pass if that row
  is encountered first.
- Entry counts are covered: SWEEP's exit-0 path includes `drift` and `totals_line == total_files`
  (`sweep.py:149,193`), and base is 240 `corpus/knowledge` files / 33 `culture-material` — so
  "240 -> 241, 33 -> 34" is genuinely asserted through the SWEEP leg, unlike the registry count.
- No cross-row freshness: each RESTATE check is per-row, so 24 rows sharing a single quote and a
  single teaches string pass; HOSTS accepts 24 synthetic `.example.org` hosts; `mined` is a
  self-declared status cell with no leg tying rows to `## Search log`. (Inherently review-only, but
  the wave's "fabricated anchors" attack class lands squarely on it — demonstrated in
  `w1/ExecCounterSmokeC.md` §7.)

## F9 — MEDIUM (instrument reproducibility): the recorded control command does not materialize lands

`telemetry/controls-c.txt:2` records
`git clone --no-local --single-branch --branch main . .scratch/eval-base && python3 -B
reports/round-67/accept-c.py --root .scratch/eval-base --lands ad5b52b0…`. `--branch main` clones
the lane's **current** main (tip `b78f8b8`), so `git rev-parse main` in the clone is the tip and
`STAMP` fails: the sibling smoke seat reproduces `STAMP FAIL stamped=ad5b52b0 evaluated=b78f8b8e
equal=False … ACCEPT-C-67: FAIL` from exactly that command (`w1/ExecCounterSmokeC.md` §1). The
committed `dry-run-c.txt` nevertheless records `STAMP PASS … evaluated=ad5b52b0`, so the receipt was
not produced by the command recorded beside it: the run needed `git reset --hard <lands>` (or
`checkout -B main <lands>`) after the clone. Claims.json's protocol ("materialize the lands tree
(`git clone --no-local` of the lane at the lands commit)") inherits the same ambiguity.
Consequence: the frozen control is non-reproducible from its own text, and the same mistake at lands
time yields a spurious `STAMP FAIL` on honest bytes (or, worse, tempts an operator to drop `--lands`
back to the tip, which is exactly the moved-worktree PASS that F1 shows is accepted). Fix: record and
freeze the exact eval procedure (`git clone --no-local <lane> <dir> && git -C <dir> reset --hard
<lands> && git -C <dir> clean -fdx`), and assert `HEAD == lands` in STAMP (F1).

## F10 — MEDIUM (cross-claim, design): C↔Ca id-set conflict is satisfiable only under sequenced lands, and C's verdict is then not tip-stable

`accept-c.py` bounds registry additions to `NEW_IDS ∪ EXTRA_IDS`
(`:68-71`, `:373`), while `accept-ca.py` D4 requires
`rej_opened_today >= len(R66_REJECTS) + 2` = **6** rows with `status == rejected` and
`opened == 2026-10-24` (`accept-ca.py:226-236`; `R66_REJECTS = S801-S804`, `:68`). Base carries
**0** of S801-S804 (`git show base:corpus/SOURCES.md | grep -c '^| S80[1-4] '` → 0), and `ROWS`
forces every S805-S828 row to `status=mined` (`:264-266`), so the two extra rejects cannot reuse
declared ids and cannot be flips of older rows (the APPEND mutable branch pins cell 8, `:369`).
Single-lands evaluation is therefore **jointly unsatisfiable** — exactly the class CriticFrontier
raised.

L1 resolved it without a counter/claims revision (IRC ruling, this run): per-claim lands separation
— A_r (S801-S804 + r66 dispositions) lands before A_c (S805-S828 only, C's receipt:
evaluated==stamped==A_c), and A_ca (S829+ reject rows + lesson) lands after; Ca's receipt is taken at
A_ca. Under that sequencing APPEND sees only `NEW_IDS ∪ EXTRA_IDS` at A_c (passes) and D4 sees 6
today-rejected rows at A_ca (passes); claims.json's "724 -> 752" (728 + 24) is then the A_c count and
Ca's 754 is a later revision, so the arithmetic reconciles. Recorded here as a design finding, not a
revision request.

Residual risks the ruling creates, which no instrument encodes:

1. **Sequencing is protocol text, not a frozen artifact.** claims.json's receipt protocol describes a
   single lands commit and its note says nothing about A_ca carrying S829+; the A_r < A_c < A_ca order
   currently exists only in the L1 IRC ruling. It must be written into the round's lands plan/records,
   or the next operator will land one commit and get an opaque `APPEND FAIL extra=['S829', …]`.
2. **C's verdict is revision-scoped, not tip-stable.** Any post-A_ca re-run of `accept-c.py` at tip
   (the r66 verifier spot-check pattern: re-derive the predicate at tip) prints
   `APPEND FAIL extra=['S829', …]` on honest data. That FAIL is *not* a lands defect and must not be
   read as one; the verifier must materialize A_c and run there. `check-receipt-seq.py --topo`
   grades parentage, not this id-set drift, so nothing currently tells the two apart automatically.
   Cheap diagnostic (no predicate change): have APPEND's detail name the class when the extra ids
   match `S8(2[9]|[3-9][0-9])` — "post-lands reject additions, verify at A_c" — and note the A_c
   identity in the round's lands record.
3. The dead `new_rejects` variable (`accept-ca.py:232-234`) computes exactly the "rejects beyond
   S801-S804" count but is unused; it is harmless at A_ca but leaves the leg's intent unstated in its
   detail line.

---

## Control sanity (frozen-predicate rule)

The committed base dry-run (`telemetry/dry-run-c.txt`) shows STAMP PASS with
FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC failing on base bytes, so a do-nothing control cannot
pass the predicate. `ROWS PASS n=0` and `LINK PASS`/`APPEND PASS` are vacuous on empty data; SET and
HOSTS carry the failure, which is acceptable.

## Residual risk / verification gaps

- I did not construct a full 24-row PASS state; attacks are at leg granularity with isolated
  injections (each experiment resets the clone to clean `main`).
- EXP1/EXP2/EXP3/EXP4/EXP5/EXP6 ran against tip `b78f8b8e` (pre-data); the lands run happens later,
  so F1's worktree hole is a pre-data instrument defect, not a claim about a future receipt.
- The full false PASS (all legs, exit 0) was produced by the sibling smoke seat on a **base** clone
  (`w1/ExecCounterSmokeC.md` §7); I independently reproduced the untracked-entry and detached-HEAD
  variants at tip and the per-leg bypasses (F2-F6). Neither run touched the lane.
- F10: I did not materialize A_r/A_c/A_ca; the sequencing argument is code-read (`accept-ca.py:226-236`,
  `accept-c.py:68-73,373`, base S801-S804 count 0) plus the L1 ruling, not an executed three-commit
  rehearsal. The load-bearing consequence — a tip re-run of `accept-c.py` fails APPEND on honest data —
  follows directly from `:373` and is the item the closure/spot-check must respect.
- F1's exploit needs a dirtied/moved clone; the declared command's clone is clean *if* the operator
  doesn't touch it — the defect is that the counter cannot detect it, and the receipt's
  `dirty_tracked=False` is wrong for untracked files.
- Two dependencies on artifacts outside the lane repo: `sources-census.sh` (Ca D2) and the
  `SWEEP` script path inside the clone (present).
