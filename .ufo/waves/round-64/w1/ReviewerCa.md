# ReviewerCa — claim Ca (calibration, bookkeeping repair) review

## Scope

Claim Ca: round-63 closure routed defects 1, 2, 3, 4, 8, 9, 10 repaired in
`LOG.md`, `corpus/LOG.md`, `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt`;
predicate ACCEPT-CA-64 (every leg of `reports/round-64/accept-ca.py` prints PASS).
Frozen predicate from `reports/round-64/claims.json`, assignment = review-only.
Counter audited: `reports/round-64/accept-ca.py` sha256
`f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678`
(revision 1; same blob CriticCa fingerprinted). No tools installed or updated.

## Executed counter run (pasted verbatim)

```text
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-64/accept-ca.py --root .
CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
PTRS PASS score_dead=False stray_dead=False o_fixed=True c_fixed=True
HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
DISPO PASS items5_7=True s687_flip=True s693_kind=True
REVNAMES PASS missing=[]
NITS PASS seat_reports_nit=True w04_nit=True
R63SEP PASS result_cited=True dep_class_named=True
ACCEPT-CA-64: PASS
EXIT=0
```

Counter revision provenance: `git diff HEAD -- reports/round-64/accept-ca.py`
shows three pre-data rev1 fixes, each with its own forcing comment:
(a) CANONLOG heading regex `count("## Round")`/`>60` → `findall(r"^## .*Round")`/`>50`
(rev0 could never pass — `git grep -c '^## Round'` prints **7** across all of LOG.md
history, since canonical entries are `## <date> — Round N`);
(b) PTRS narrowed from whole-SCORECARD to the `## Axes — round 63` block (rev0
could never pass — rounds 51–58 legitimately cite their own
`final-measures.txt`, e.g. SCORECARD.md:1013);
(c) REVNAMES actually emitted (rev0 computed `rev_ok` but never called `leg()` —
the committed 6-leg receipt matches this exactly).
Docstring header still reads "revision 0" — stale label, code/comments are rev1
(cosmetic nit).

## Independent per-defect verification

Routed list verified verbatim at `corpus/lessons/round-63-verifier-spotcheck.md` §6.

| defect | disposition | verification (command → observed) |
|---|---|---|
| 1 canonical LOG | root `LOG.md` carries `## Round 64` entry; first bullet names root canonical and `corpus/LOG.md` the stray (explicit-pointer form permitted by the route) | diff shows append-only add at LOG.md:4152; entry text read at :4152-4158 |
| 2 dead pointer | `SCORECARD.md` r63 operability row now cites `final-measures-o.txt`; `corpus/LOG.md` O/C lines cite `-o.txt`/`-c.txt`; corrections block names both | `git cat-file -e ff30a205:reports/round-63/telemetry/final-measures.txt` → absent (dead at base); both `-o`/`-c` exist at base; `final-measures.txt` substring gone from r63 block and stray |
| 3 tier histogram | corrections block + LOG record A=13 B=11 with frozen census command | re-ran the exact awk over `ff30a205:corpus/SOURCES.md` → `A=13 B=11`; S702 confirmed tier B `docs` |
| 4 r62 items 5–7 | LOG entry disposes all three: resid/ prefix naming (`KotodamaR62.ResidRerunO.md` + `ResidRerunD.md` — both exist at `.ufo/waves/round-62/resid/`), 28-vs-32 selftest, S693 `docs` vs S692 book, line-75 cosmetic nit, S687 `mined -> queued` | `ResidRerunO.md:88` shows `32 checks, 0 failures`; `ExecReopenTool.md:115` shows `28 checks` (pre-revision-1) — disposition matches r62 spotcheck items 5–7 text (:76-78); S693/S692 kinds match registry |
| 8 revisions.txt | names 8d2041fa / 38ec1316 / 0c892ce / 80ff34c against the four receipts | all four hashes `git cat-file -t` → commit; `rev-separability.txt` last carried by 80ff34c ✓ (`git log --diff-filter=A` + modify commits); `80ff34c..38ec1316` touches only `separability-manifest.json` ✓; `accept-o.py` blob `934bb052…` identical at 0c892ce/9e9885d/80ff34c/38ec1316 ✓ |
| 9 numeric nits | 47 seat reports (not 45); 27 W04 rows (not S650/S651); 9 dry-run FAIL legs (not 6) | `ls .ufo/waves/round-63/w1/*.md | wc -l` → **47**; `census-end.txt` contains exactly 27 `W04` lines incl. S650/S651 — live fleet census `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama | grep -c W04` → **27**; `declaration-dry-run-o.txt:3-15` FAIL legs = GEN/ORDER/BOUND/REDIRECT/MALFORMED/GZIP/TRUNC/TIMEOUT/REVIEW = **9** verbatim |
| 10 separability | LOG records `SEPARABILITY: 2 findings`, `exit=1`, findings C→REC and O→base, dependency class = record dependency | `rev-separability.txt` verified byte-matching all four claims |

## Filed-bytes check (assignment requirement)

`git diff ff30a205 -- LOG.md SCORECARD.md corpus/LOG.md reports/round-63/telemetry/revisions.txt`:

- `LOG.md`: **pure append** (+11 lines, single Round-64 entry). No filed row touched.
- `SCORECARD.md`: one in-place **correction** (r63 operability evidence pointer
  `final-measures.txt` → `final-measures-o.txt`) + appended `### Round-63 corrections`
  block. No other filed row modified.
- `corpus/LOG.md`: three **corrections** — O/C receipt pointers, and the false
  "items 5–6 recorded in R63-M2" sentence replaced by an erratum pointing to the
  canonical LOG. All are the routed defect-2/defect-4 repairs themselves.
- `revisions.txt`: untracked/new (absent at base — confirmed `git cat-file -e`
  fails); adds no rewrite.
- `git status --porcelain` shows no other modifications to round-51–63 paths.

Rounds 51–63 filed bytes: only the named corrections, no rewrites of filed rows. ✓

Control check: committed dry-run receipt `097c21d:reports/round-64/telemetry/
dry-run-ca.txt` shows all legs FAIL at base (6 printed — rev0's un-emitted
REVNAMES; rev1's all-7 FAIL independently executed by CriticCa in scratch,
`REVNAMES FAIL missing=[8 names]`). Separability claim verified: no sibling
counter reads `revisions.txt` (grep over accept-{c,o}.py r63/r64 → no reference).

## Findings

### LOW — revisions.txt prose overstates receipt provenance (defect-8 repair file)

`revisions.txt:14` — "the receipt's 10 legs **and the commit subject both name** 8d2041fa":
`final-measures-c.txt` contains no revision at all (verified; that is the very
omission defect 8 routes). Only the commit subject names it. Same pattern for
final-measures-o.txt. And `revisions.txt:10` — "accept-c.py is unchanged
between 8d2041fa and the records commit": the records commit `0c892ce` is itself
the commit that changed `accept-c.py` (rev0 `4a8791ba` → rev4 `e6322538`; verified
by blob). The named revisions are nonetheless correct — the defect is overstated
provenance prose in a repair file, not wrong revision mapping. The REVNAMES leg
cannot catch it (unordered token membership, no receipt↔revision association).

### LOW — NITS leg does not bind the corrections (counter weakness, frozen)

`accept-ca.py:144-145` tests only substring presence of `45`/`47`/`W04`/`27`
anywhere in LOG.md. CriticCa executed the control: appending prose containing
only a bare `W04` flips NITS FAIL→PASS because `47` and `27` already occur in
historical entries. The third nit (6-vs-9 FAIL legs) is never checked at all.
The genuine land happens to satisfy it; a prose-only future land could too.
Proposed pre-data revision (per CriticCa, valid): scope tokens to the round-64
entry + named r63 correction row, require old→new associations incl. 6→9, pin
the bare-`W04` append as forcing negative control. NOT edited (frozen counter).

### LOW — LOG wording: S687 enactment asserted while pending (claim C dependent)

`LOG.md:4156` "disposition is `mined -> queued`, **enacted** in
`corpus/SOURCES.md` by this round's claim C land" — registry line 642 still
reads `mined`/`used-by —` at review time; SOURCES.md is byte-identical to base.
The LOG's own text is accurate about the intended disposition; the present-tense
"enacted" is premature until claim C's land completes. Not Ca's enactment
responsibility (claim C's); record as pending-dependent wording.

### INFO — PTRS/append-only contract tension (named, no verdict)

The defect-2/defect-4 repair rewrote three filed `corpus/LOG.md` lines and one
SCORECARD r63 row rather than appending errata. Within this charter's
"appends/corrections" allowance it is in-scope and the corrected pointers all
resolve; but it conflicts with strict append-only correction discipline, and the
frozen PTRS leg is designed so append-only repair can never pass (the dead
string must be removed). CriticCa flagged the same conflict. Surfaced for the
judge; not counted against this claim.

### INFO — transient worktree receipt anomaly (resolved, no action)

During review, `reports/round-64/telemetry/dry-run-ca.txt` was observed briefly
carrying a 7-leg variant (`REVNAMES FAIL missing=[]` — content rev1 cannot emit
with the file absent, since absent ⇒ `missing=[8 names]`); the file now sits at
index/HEAD blob `f213bf46` (rev0 6-leg output, mtime 19:35:49Z). Consistent with
live-wave worktree churn; final state authentic. The rev1 7-FAIL evidence stands
on CriticCa's executed scratch run, not this receipt.

## Residual risk / verification gaps

- REVNAMES/R63SEP/DISPO are token-presence legs; they cannot detect wrong
  associations (e.g., swapped receipt↔revision pairs) — frozen-counter limit.
- Separability check was grep-verified (no sibling counter reads revisions.txt);
  no sibling counter execution was performed.
- Round-63 acceptance counters were not re-executed (outside charter); all
  claims rely on committed receipts, which were byte-verified.
- The one real counter weakness (NITS substring binding) has an executed
  witness in CriticCa.md and a proposed pre-data revision; recommend adopting
  it in the next instruments revision.
