# RevengerReceipts — r65/r66 receipt-sequencing failure chronology (round 67, w1)

seat: L1-kotodama-r67.RevengerReceipts · 2026-10-24 · method: committed bytes only
(git read-only at lane tip; no counter re-execution against live data; no repo mutation).
No tools installed (operator directive noted; pacman guard respected — nothing needed).

## 1. Round-65 chronology (from committed bytes)

Commit chain (verified `git log -1 --format='%H %P | %s'`):

```
17c32302 (base)
  └─ f107e849  "round-65: declaration + instruments" (counters rev2/rev3/rev3)
       └─ 3b1b5a67  "round-65: land sourced games register and round repairs"  ← LANDS A
            └─ 53a60275  "round-65: file measurements and prepared wave receipts"
                 │            carries final-measures-{c,ca,o}.txt (+LOG.md +15, SCORECARD +23)
                 └─ 3e85a610  "round-65: record final measurements and prepared wave"
                              touches SCORECARD only (2 lines)                 ← RECORDS B
```

The r65 RECEIPTS leg never looks up the receipt's carrier. It hard-derives the
expected lands from the moving tip — `reports/round-65/accept-ca.py:363`:
`lands_code, lands_out = git_out(root, ["rev-parse", "main^"])` — with the
assumption stated in the comment at :355: each receipt "must name the LANDS
commit (**main^ while the receipts themselves ride the records commit**)", then
requires every receipt to contain `measured revision: {main^}` and
`tree: {main^^{tree}}` (:378-381).

Two runs, both FAIL, same leg, two distinct geometries:

1. **Lands-time run** (`telemetry/final-measures-ca.txt`, stamped A=3b1b5a67,
   tree e27ce372): main = A, so the leg derives lands = A^ = **f107e849** (the
   declaration) — one commit too early by construction. Output:
   `RECEIPTS FAIL lands=f107e849 bad=[c:lands_stamp, c:tree, o:lands_stamp,
   o:tree, ca:absent]`. The `ca:absent` is pure self-reference: the receipt
   being written cannot be read by the run that writes it.
2. **Post-records run** (`telemetry/accept-ca-post-records-fail.txt`, main =
   B=3e85a610): the leg derives lands = B^ = **53a60275**. But the receipts
   stamp A=3b1b5a67, and they were committed in 53a60275 — the prepared-wave
   commit inserted between A and B — not in B as the plan assumed. Output:
   `RECEIPTS FAIL lands=53a60275 bad=[c:lands_stamp, c:tree, o:lands_stamp,
   o:tree, ca:lands_stamp, ca:tree]`.

The LOG records both halves. Plan (`LOG.md:4176`): "The three receipts are
committed with this record entry, stamped to A/tree A; the report records the
post-record re-run of ACCEPT-CA-65 at records commit B, where RECEIPTS passes."
Correction (`LOG.md:4181`): "The preceding planned Ca post-record pass did not
occur. The actual ... run at records tip `3e85a610` printed `RECEIPTS FAIL
lands=53a60275`: the receipts stamp lands `3b1b5a67`, but the intervening
prepared-wave commit `53a60275` changed the receipt parent. ... Do not retarget
the frozen counter after data."

Key nuance: the D2-class predicate itself — *the receipt's carrier commit's
parent equals the stamped revision* — was TRUE even then: the receipts' actual
carrier is 53a60275 and 53a60275^ = 3b1b5a67 = stamped (verified). The r65 FAIL
is an **anchor** artifact: the leg graded against `main^` (B's parent) instead
of looking up the carrier of each receipt.

## 2. Round-66 chronology (from committed bytes)

```
94209e8f (r65 verifier spot-check)
  └─ 65fe8572  "round-66 lands: ..."        ← LANDS
       └─ 4589ebdd  "round-66 records: final-measure receipts stamped at lands rev 65fe8572"
```

The r66 counter renamed the leg D2 and made the carrier explicit —
`reports/round-66/accept-ca.py:125-133`: `git log -1 --format=%H main -- <r>`;
if nothing → `no_carrier`; else `rev-parse {carrier}^` must equal the stamped
`measured revision`. But D2 is post-records-only evidence and the counter had a
single run mode; the receipt of record was taken at lands (main = 65fe8572),
where the three receipts are by construction uncommitted:
`telemetry/final-measures-ca.txt`: `D2 FAIL bad=[...c:no_carrier, ...o:no_carrier,
...ca:no_carrier]` → `ACCEPT-CA-66: FAIL`.

The verifier spot-check (`corpus/lessons/round-66-verifier-spotcheck.md` §2,
Claim Ca) re-derived the predicate at tip without executing gates: carrier of
each receipt = 4589ebdd, 4589ebdd^ = 65fe8572 = stamped revision; tree and
counter-sha lines resolve — "D2's predicate holds at tip for all three
receipts". Its routed defect R66-D3 (§5 item 3) prescribes exactly the r67 fix:
re-run post-records and commit the PASS alongside the FAIL, or give D2 an
explicit `--lands` and grade carrier-parentage against it post-records.

## 3. (a) The exact predicate class that fails lands-time

**Carrier-parentage of the receipt of record — the direct-child invariant
"the commit carrying the receipt is a child of the receipt's stamped lands
revision" — evaluated at a revision/time where its subject cannot exist or is
derived from the wrong anchor.** One family, two forms:

- **r65 = wrong anchor.** The leg substituted `rev-parse main^` for a carrier
  lookup. At lands that anchor is the *previous* commit (self-reference: the
  receipt cannot stamp the commit it is not yet in; `ca:absent`); post-records
  the anchor is whatever commit happens to precede the tip, so any intervening
  commit (53a60275) breaks it even though the true carrier-parentage holds.
- **r66 = wrong time.** The leg looked up the carrier correctly but ran at
  lands, where the carrier definitionally does not exist (`no_carrier`).

Shared root cause: the frozen counters had a single evaluation mode, but the
predicate needs two evaluation times (lands for data legs, post-records for
carrier legs), so the lands-time verdict became the receipt of record — a FAIL
that the frozen-predicate rule converts into an unprovable/rejected claim even
when the substance re-derives HOLDS at tip (true in both rounds).

## 4. (b) Does the r67 protocol cover both incidents? — YES, both, with two named caveats

Instruments read: `reports/round-67/{claims.json,accept-c.py,accept-o.py,accept-ca.py}`,
`tools/check-receipt-seq.py`, `reports/round-67/telemetry/dry-run-{c,o,ca}.txt`.

- **r66 form (no_carrier at lands): covered structurally.** No r67 lands-time
  leg performs a carrier lookup — verified: zero `git log` calls in
  `accept-ca.py`; its legs are STAMP/D1(manifest)/D2(census+S753)/D3(LOG/
  SCORECARD)/D4(rejects)/SEQ(counter sources)/CRITERION/QUOTES. Carrier
  checks live only in `check-receipt-seq.py --topo`, whose docstring (:21-22)
  says "Post-records mode only — never claimed from a lands tree where no
  carrier exists yet", and whose selftest pins `topo-no-carrier-fail` (:403-407).
  The r65 `ca:absent` self-reference mode is likewise eliminated: no lands-time
  leg reads the round's own receipt files — the receipt is the run's output.
- **r65 form (main^ hard-code + drift): covered in both halves.**
  (i) Anchor fixed: lands is operator-declared (`--lands`, REQUIRED, full-40hex
  validated — `accept-ca.py:88,94-97`); evaluated is measured
  (`rev-parse main` of `--root`); STAMP fails closed (`evaluated==stamped` and
  tree resolvable, then `return 1` before any data leg — `accept-ca.py:113-120`;
  same shape in accept-c/accept-o). A moved worktree now prints
  `equal=False` and exits — the r65-b geometry cannot mint a lands receipt.
  (ii) Drift graded explicitly: `--topo` looks up the true carrier
  (`log -1 main -- <receipt>`) and requires `carrier^ == stamped`
  (`check-receipt-seq.py:179-197`); the selftest pins the exact 53a60275
  geometry (`topo-wrong-parent-fail`, :409-422). `--lands` mode reads receipts
  via `git show <lands>:<path>` committed bytes and reports `moved_past` as a
  flag, never a verdict change (:222-236); an absent receipt at lands is FAIL,
  not skip (`lands-absent-is-fail`, :334-336). Dry-run receipts confirm the
  five-field header (stamped/evaluated/measured/tree/counter-sha) exists and
  that base materialization + `--lands <base>` gives STAMP PASS with all data
  legs FAIL (control cannot reach the target).

Caveats (record, do not block): (α) the drift half is detected by **commanded
post-records evidence** (`post-records.txt`, third lane commit) plus a closure
hand re-verification — not by a frozen leg; claims.json's note says this is
unavoidable ("no hash of its own carrier can exist before it is committed").
The frozen verdict is drift-immune by construction; drift detection degrades to
post-records + hand-checked. (β) see RV-2 below for the depth-+1 regress of
that same caveat.

## 5. (c) Third variant the protocol still misses

### RV-1 (routed-defect candidate): stamp-tree binding gap — dirty/untracked clone laundering

The protocol binds `evaluated == stamped` (**commit identity**) and records the
lands tree, but **no instrument binds the measured bytes to the stamped tree**:

- Every r67 data leg reads **worktree bytes**: `accept-ca.py:71-74`
  (`read()` = `open(os.path.join(root, path))`) used by D1-D4/CRITERION/QUOTES;
  accept-c.py's FILE leg likewise `open()`s the entry (dry-run error shows the
  filesystem path `.scratch/eval-base/...`).
- `accept-c.py:181-184` and `accept-o.py:136-139` compute
  `git status --porcelain --untracked-files=no` but only **print** it:
  `stamp_ok` (`accept-c.py:200-202`) contains no dirty term; the flag appears
  solely in the STAMP detail string (`dirty_tracked={dirty_flag}`). `accept-ca.py`
  computes no cleanliness at all (zero porcelain/dirty hits).
- The `--untracked-files=no` scope blinds all three to **untracked** evidence
  planted in the clone worktree (e.g., an entry .md or the D1 manifest left
  untracked): the leg passes over bytes the stamped tree does not contain, and
  the receipt's `# tree:` line still names pristine lands bytes.
- Nothing downstream catches it: `check-receipt-seq --lands` re-reads only the
  receipt .txt files at lands (`read_rev`), never the leg subjects;
  `--topo` grades `carrier^ == stamped` only; `check_tree` grades the receipt's
  own stamped↔tree consistency, not the evidence's membership in the tree.

So a materialized clone whose files were modified or supplemented after
`git clone --no-local` mints PASS receipts for bytes not in the stamped tree.
Lineage: the r64 incident was exactly a dirty-worktree run (`reports/round-65/
accept-ca.py:12-13`: "the original run over a dirty worktree"), and r65's
counter R1 forced a `dirty-worktree:` disclosure line into the repaired receipt
(:100, :186-187) — the r67 counters dropped both the enforcement and the
disclosure requirement. `claims.json`'s "materialized clone ... never a moved
worktree" is process discipline; the instruments enforce commit identity only.

**Proposed routing (R67-RV1):** r67 legs must read `git show <lands>:<path>`
(the pattern already exists as `check-receipt-seq.read_rev`), or gate on
`git status --porcelain` *including untracked leg-subject paths* — and enforce,
not print. Smallest fix: extend `stamp_ok` with `not dirty_flag` in c/o and add
the same computation to ca.

### RV-2 (secondary): depth-+1 regress — post-records.txt's own carrier is uninstrumented

`claims.json` note: post-records.txt is "`--topo` over the three receipts +
itself", committed in a third lane commit, and "its stamped==evaluated==lands
equality is re-verified by hand at closure". Two wrinkles: (i) as written the
two clauses cannot both hold — topo-on-self requires `carrier^ == stamped`, and
the third commit's parent is the *records* commit, not lands (if
stamped=lands, topo-on-self must FAIL); (ii) no instrument ever grades the
third commit's parentage (`C^ == records commit`) or that post-records.txt was
not re-committed after a rewrite — the r65-b drift class recurs one level up,
held only by a hand check. Proposed routing (R67-RV2): stamp post-records.txt
with the **records** commit (making topo-on-self mechanically satisfiable) and
extend the closure hand-check to `C^ == records`.

### RV-3 (observation): `--topo` grades first parent only

`check_topo` uses `rev_parse(root, f"{carrier}^")` — first parent. A records
commit that is a merge with first parent = stamped lands launders side-branch
parentage. Low severity; one-line hardening or an explicit first-parent
discipline note.

### Design finding (per L1 ruling, recorded not argued)

C-APPEND (new ids bounded to S805-S828 ∪ S801-S804) vs Ca-D4 (>=2 further
2026-10-24 rejects) looked jointly unsatisfiable on one lands tree; resolved by
per-claim lands separation: A_r (S801-S804 + r66 dispositions) → A_c (C's
lands: only S805-S828 appended; APPEND bound to NEW_IDS∪EXTRA_IDS holds) →
A_ca (S829+ rejects + lesson; D4 sees >=6 today-dated rejects at A_ca). No
counter/claims revision; QUOTES capture-group fix already applied.

## 6. Verdict

(a) Predicate class: **carrier-parentage (direct-child invariant) of the
receipt of record, graded at the wrong anchor (r65: `rev-parse main^`) or the
wrong time (r66: lands, `no_carrier`)** — in both rounds the predicate itself
was true at tip; the FAIL receipts were evaluation-geometry artifacts.
(b) The r67 protocol (declared `--lands` + `evaluated==stamped` fail-closed
STAMP + carrier lookup confined to post-records `--topo`) covers **both**
incidents; the drift half is covered as commanded post-records evidence, not a
frozen leg (by construction).
(c) Third variant found: **RV-1 stamp-tree binding gap** (worktree-byte legs +
informational-only dirty flag + `--untracked-files=no` ⇒ dirty/untracked clone
can mint PASS receipts not backed by the stamped tree); plus RV-2 (post-records
receipt's own carrier uninstrumented) and RV-3 (first-parent-only topo) as
smaller residuals. All three named for routing; RV-1 is the one that can
produce a false lands PASS today.

Report: .ufo/waves/round-67/w1/RevengerReceipts.md
