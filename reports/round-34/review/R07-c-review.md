- Seat: R07 | reviewer | C | date 2026-10-19 | baseline da68a6d

# R07 — second C pass: A09 R1–R8 coverage cross-check

**Mission** (`reports/round-34/targets.json` R07): "Second C pass: cross-check the reissue
against A09-pins' R1-R8 list for coverage." **Out**: this file.

**Cut.** 2026-10-19T07:11–07:14Z, HEAD `da68a6d705e41f369f21e8607bfaab5b54077f84`,
`git status --porcelain` → `?? reports/round-34/` only (no tracked byte dirty).
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no in-tree round runner was
executed (F-C13-1); the only write is this fragment.

**Artifacts reviewed** (read at the cut, sha256 of my copies): `calib/C01-survey-run.md`
`adc534737b8c…`, `C02-receipt-json.md` `3e7edaa29703…`, `C03-anchor-reissue.md`
`2d72a2b532a9…`, `C04-byte-check.md` `741373ab6210…`, `C05-receipt.md` `b27c36a248a5…`,
`C06-scribe.md` `a5e13b3d250f…`, `C07-verify-survey.md` `3110d0afb2f2…`,
`C08-verify-reissue.md` `5e5b58246c60…`, `C09-final-receipt.md` `d8cb9c848a66…`,
`scout/K04-anchor-census.md` `c7134d10d361…`, `scribe/S03-c-receipt.md` `c294562f4ba4…`,
`cross/X02-conformance.md` `af24d7e51d0a…`.

## 1. The governing finding: "A09 R1–R8" is a re-pin list, not eight anchors

A09's R1–R8 (`reports/round-33/adj/A09-pins.md:107-114`) is heterogeneous. Verbatim classes:

| A09 row | artifact class (A09:line) | line-anchor row? |
|---|---|---|
| R1 | README git-blob pin inside the r26 runner (`:107`) | no |
| R2 | README sha256 receipts, 6 filed sites (`:108`) | no |
| R3 | SKILL.md sha256 receipts, 8 sites (`:109`) | no |
| R4 | box-1 re-survey receipt, count + digest (`:110`) | no |
| R5 | SKILL.md line anchors (`AGENTS.md:42`, self-cites, filed citations) (`:111`) | **yes — the only one** |
| R6 | README prose arithmetic `:97`/`:207` + row cells (`:112`) | no |
| R7 | x45 `X45-P1` / x57 historical controls (`:113`) | no |
| R8 | README rows vs `round-33.md` landing order (`:114`) | no |

Claim C's prose calls this "the A09 R1–R8 **SKILL anchor** reissue … a table of old anchor →
new anchor → owning row" (`reports/round-34/claims.json:56,60`). Read literally, that table
shape fits one row of eight. So the threshold "the reissue table covers every A09 R1–R8 row"
(`claims.json:65`) is satisfiable only **class-wise** — which is what C03 §2 and S03 §4 both
do (value/state columns, not eight anchor pairs), and what C09-F3 rules (`C09-final-receipt.md`
§5.2). **This second pass confirms C09-F3** with the quoted rows above: an eight-anchor table
would misdescribe seven rows; the class reading is the only defensible one.

**Coverage answer: 8/8 rows are present, in two independent artifacts** — C03 §2
(`calib/C03-anchor-reissue.md:62-71`, one row per R1–R8 with old value → HEAD value → owning
row → its own grep) and S03 §4 (`scribe/S03-c-receipt.md:106-115`), folded again at C09 §6.
R5 is expanded in C03 §3 (30 rows, its checker `.scratch/c03/check-anchors.py` exits 0,
`failures=0`, quoted at `C03:207-222`). The remaining risk is not missing rows but **row
content**, §4 below.

## 2. R1–R8 at HEAD — my own measurements (independent of the C block)

| row | my measurement | verdict on the C block's row |
|---|---|---|
| R1 | r26 pin intact: `README_BASELINE_BLOB = "a3187055…"` (`reports/round-26/run-validation.py:97`); live README blob `73f3e1bd29d4569ddd2a5d9a2309f4451fa35ae5` (`git hash-object` == `git rev-parse HEAD:`) | C03/S03/K04 correct; SCORECARD.md:597-598 records the supersession row |
| R2 | README digest `ec7469da…` (346 L) → `f752e1d7…` (448 L, 43 454 B) | C03/S03 correct; filed-only census: **43 files / 88 lines** still carry `ec7469da` (`corpus/lessons/ reports/round-{1..33}/ tools/`) |
| R3 | SKILL `79fe91d3…` (715 L) → `f9bd07c2…` (732 L) | C03/S03 correct; filed-only census: **31 files / 74 lines** carry `79fe91d3`, **11 files / 19 lines** carry `83b0a78a`, **1 file / 2 lines** carry `f9bd07c2` (`reports/round-33/adj/audit-assembled.md:30,41`) |
| R4 | `python3 -B reports/round-30/craft/box1-survey.py` → **exit 0**, `named 28 / resolvable 28 / unnamed_in_skill [] / skill_sha256 f9bd07c2…` | C03/S03/K04/C07/C09 all agree; the *durable* receipt is still unlanded (§5) |
| R5 | map in §3 (re-derived here) | C03 §3 has 5 row defects (§4 D-R07-1) |
| R6 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json` → **exit 0**, `index_rows 33`, `lesson_files 33`, six checks true (`C34b_prose_arithmetic` among them) | C03/C09/S03 correct; also README `:105` = "**Rows: 33. Files: 33.**", `:254` = "Rows: **78**. … **30 carry at least one question**" |
| R7 | `x45` → **exit 1**, `FAIL P1_pointers_resolve`, `findings 1`, `X45-P1` carries 4 tuples (round-4 glob + `round-26.md:178-186`, `round-27.md:165-193`, `round-29.md:110`); `x57 --selftest` → **exit 1**, `passed 28 / total 37`, 9 named failures (partition 27→33, rows 26→33, queue 49→78, orphan controls, README pin drift `29059/346/ec7469da` vs `43454/448/f752e1d7`) | C03/S03/K04 correct; A09 read 34/37, so the drift worsened by 6 controls — carried as named findings, not a claim-C surface |
| R8 | `ls corpus/lessons/*.md \| wc -l` → 33 = `README.md` + rounds 1–32 (variants included); **`corpus/lessons/round-33.md` does not exist** (also `reports/round-33/` holds no lesson file) | C03 §2's row is **correct** (no orphan at HEAD); S03/K04 "CLOSED" is right at HEAD but the forward half of A09's R8 is still live — see D-R07-6 |

## 3. The R5 anchor map, re-derived (boundary proof + measured deltas)

`git diff -U0 139e3b6 da68a6d -- SKILL.md` → 13 hunks; the eight replacement hunks
`:128, :479, :481, :483, :486, :488, :491, :501` are all 1→1 (net 0). The **first
non-net-zero hunk is `@@ -584 +584,3 @@`**; then `@@ -694,4 +696,5 @@` (+3 cum),
`@@ -699,2 +702,4 @@` (+5 cum), `@@ -704 +709,12 @@` (+16 cum), `@@ -714,2 +730,3 @@`
(+17 cum) = net +17 = 732 − 715 (`git diff --numstat` → `35 18`).

⇒ **Every address ≤ 584 is stable**; the only anchors that move are ≥ 585:

| old (139e3b6) | HEAD | class | my check |
|---|---|---|---|
| `:660` | `:662` | shifted +2 | `## Source-bounded culture drill — D3 (round 7)` at `:662` (`sed -n 662p`) |
| `:710` | `:726` | shifted +16 | old `:710` = "Read `reports/round-7/integration-attempts.json` …" |
| `:713` | `:729` | shifted +16 | item line 1 |
| `:714-715` | `:730-732` | rewritten 2→3 | item now `:729-732`; body re-keyed to `closes`/`closes_sha256` (`sed -n 728,732p`: `:728` is the preceding prose line, item starts `:729`) |
| `AGENTS.md:42` | — | **retired** | `wc -l AGENTS.md` → 40; `grep -n "append one item" AGENTS.md` → exit 1; the text was `:42` at `139e3b6`; A09-F3's live instruction no longer exists |

Stable anchors I re-checked at both revisions (bytes equal, same address): `:47`, `:149`,
`:183`, `:157`, `:205`, `:208`, `:262`, `:278`, `:294`, `:323`, `:456-458`, `:522`, `:534`,
`:535`, `:536`, `:575`, `:581`. So C04's "content before `:581` keeps its address"
(`C04-byte-check.md` §2) is true but conservative — the exact boundary is ≤ `:584`; C03's
"everything at or below `:584` keeps its number" (`C03:39`) and C09's G6 hunk table are exact.

**Era-pinned citations (the finding C03 and C04 miss).** Six filed citations A09 grouped
under R5 were already stale *before* round 33 — they name addresses that were correct at their
own era revision, not at `79fe91d3`. Measured with the era blobs:

| filed citer | cited | era blob = subject | at `139e3b6` | subject's real address at HEAD |
|---|---|---|---|---|
| `corpus/lessons/round-15.md:25` | `:157` | `b02cfbc:157` = uncertainty prose ✓ | `:157` = ROUTED_KINDS line | `:564` (unchanged by r33) |
| `corpus/lessons/round-15.md:25` | `:205` | `b02cfbc:205` = `uncertainty-inventory` row ✓ | `:205` = replay table header | `:614` (+2 from `:612`) |
| `corpus/lessons/round-14.md:141` | `:208` | `b02cfbc:208` = battery row ✓ | `:208` = Named inputs row | `:617` (+2 from `:615`) |
| `corpus/lessons/round-19.md:88,:179` | `:278` | `16652e8:278` = battery row ✓ | `:278` = rank_rules line | `:617` |
| `corpus/lessons/round-19.md:100` | `:323-375` | `16652e8:323` = D3 heading ✓ | `:660` (D3 heading) | `:662-…` |
| `corpus/lessons/round-19.md:101` | `:262-278` | `16652e8:265,267-278` = table rows ✓ | `:660` region only for D3 | Gates-and-probes heading `:575`, rows `:606-617` |

C08's G13–G18 (`calib/C08-verify-reissue.md` §3) reached the same numbers independently;
C04 caught only two of the six ("already stale pre-r33" for `:208`, `:278`) and calls
`:323-375` and `:262-278` "still exact" (`C04-byte-check.md` §3), which is the same
address-stability reading C03 uses (D-R07-1).

## 4. Defects in the C block (new; none of these is in the fragments' own findings)

| id | defect | evidence | required fix |
|---|---|---|---|
| **D-R07-1** | **C03 §3 (and C04 §3) mislabel six era-pinned citations as live.** C03's class "identical" verifies *the bytes at that address are unchanged*, not *the citer's subject is there*. Rows affected: `:157`, `:205`, `:208`, `:278`, `:323-375`, `:262-278` (`C03:91-98`), with owning-section cells describing the wrong subject (e.g. `:208` → "Named inputs row", while the citer `round-14.md:141` cited the battery row). | §3 table; `C08:§3` G13–G18; `sed -n` dumps of `b02cfbc:157/205/208`, `16652e8:278/323`, `139e3b6:157/205/208/278`, HEAD `:564/:614/:617/:662` | Add a "citation resolves?" column (or a note per row): for these six the honest cell is "era-pinned reading; subject now at `:564`/`:614`/`:617`/`:617`/`:662`/`:575-617`", and the class legend should separate *address-stable* from *subject-present*. The reissue must not read as "these citations hold". |
| **D-R07-2** | **C04 §2 double-classes `:617`.** It appears in the "address-stable, content identical" cell **and** in the "+2" cell (`C04-byte-check.md` §2). | HEAD `:617` = "`\| isolated legacy selftest battery \| gate \| …`"; HEAD `:619` = "The contrastive checker is example-specific…" = old `:617` → the "+2" class is right, the first cell wrong | strike `:617` from the stable cell (its own row-3 entry is correct) |
| **D-R07-3** | **C04 §4.4 stale premise.** It asserts `AGENTS.md:42` "carries 'append one item … (after :534)'" at HEAD; the file is 40 lines and the text is gone (its own citation footnote the 40-line reading). | `grep -n "append one item" AGENTS.md` → exit 1; `git show 139e3b6:AGENTS.md \| grep -n` → `42:` | adopt K04-F3/S03-F1/C03 §5 wording: retired, no successor address |
| **D-R07-4** | **S03 §4 R3: "zero filed files carry `f9bd07c2`" is falsified as written.** Two tracked files carry it: `SCORECARD.md:599` and `reports/round-33/adj/audit-assembled.md:30,41`. | my `grep -rl f9bd07c2 corpus/lessons/ reports/round-1..33/ tools/` → 1 file / 2 lines; `grep -n f9bd07c2 SCORECARD.md reports/round-33/adj/audit-assembled.md`; `git ls-files --error-unmatch` → both tracked | restate as K04-F4/C09 do: no `validation.json`/gate receipt carries it; round-34's receipt is the first durable pin (S03's own parenthetical already names audit-assembled, so the sentence is internally inconsistent) |
| **D-R07-5** | **Durable-receipt row schema diverges across four producers**: C02 `{executable,resolves,line,sha256}`; C07 `{executable,first_line,resolves,sha256}`; C09 §3.2 `{executable,resolves,skill_line_anchors[…]}`; S03 Appendix A `{line,path,resolves}`. Only C02's shape satisfies C07's comparator on all fields. I ran C07's §7 comparator verbatim on the landed C02: sets equal (28/28, no missing/extra), digests equal, `MISMATCH []` — but **56 field pairs are silently skipped** because the key names differ (`first_line` vs `line`), i.e. the comparator's green is vacuous for the address column until keys are normalized; with normalization (`line`↔`first_line`, `sha256`↔`digest`) the comparison is also `MISMATCH []`. | `python3 -B .scratch/r07-cmp.py` (C07 §7 code + a normalized variant); `C07-verify-survey.md:209-229`; `C02-receipt-json.md:60-84` | land **C02's** block at `reports/round-34/craft/box1-resurvey-durable.json` (C09 §3.2 already says "prefer C02's"); record C09 §3.2 and S03 Appendix A as superseded drafts; if a markdown twin is added (K04-F2), keep C02's key names |
| **D-R07-6** | **R8's forward half is still live.** C03/S03/K04 record R8 as satisfied at HEAD — correct (33 == 33) — but `corpus/lessons/round-33.md` is not filed anywhere and the README index's last lesson row is `round-32.md` (`README.md:103`). A09's R8 action ("land lesson + row in one edit, or file a follow-up row", `A09-pins.md:114`) is therefore **not discharged**; when the round-33 lesson lands it re-opens `C31_index_rows_eq_files` with exactly one orphan. | `ls corpus/lessons/round-33.md` → No such file; `corpus/lessons/*.md` = README + 32 lesson files; `grep -c "^\| \`corpus/lessons/" README.md` → 33 | record R8 as "no orphan at HEAD; round-33 lesson + row still owed as one edit" (owner: round-33 integrator/parent; intent `to-verify`) |

Minor: C03 §3's cited-by cell for `:294` omits `corpus/lessons/round-32.md:34`, which
C09-F2 added to the census (`sed -n 34p` → cites the `SKILL.md:294`-class cell). No anchor
status changes; add the citer for completeness.

## 5. Claim-C acceptance state at my cut (for the integrator)

| claims.json item (`claims.json:60,65`) | state |
|---|---|
| 28/28 resolve at `f9bd07c2…`, digest-pinned, dated, re-runnable | **measured green** (my run, exit 0; five independent producers agree) |
| `reports/round-34/craft/box1-resurvey-durable.json` + receipt lands | **NOT landed** — `ls reports/round-34/craft/` → No such directory at 07:11Z; C02 §3 bytes are ready |
| R1–R8 reissue as new rows, each grep-verified | present (C03 §2 8/8; C03 §3 30 rows, checker exit 0) — **admit only with D-R07-1 fixed** |
| zero filed-row edits | **measured**: `git status --porcelain` → `?? reports/round-34/` only; filed-only digest census above is a read-only artifact |
| `reports/round-34/run-validation.py` | does not exist at my cut (claim C's second counting command) |

**Verdict:** coverage of A09 R1–R8 is **met class-wise (8/8)** and the box-1 leg is green,
but claim C is **not admit-ready**: its own product artifact (the durable receipt) is
unlanded, and the reissue table needs D-R07-1's correction before its rows are quotable.

## Owed

- `reports/round-34/craft/box1-resurvey-durable.json` (+ markdown twin) — the integrator
  lands C02's shape (D-R07-5); not written by any seat at my cut.
- `reports/round-34/run-validation.py` — claim C's second counting command; absent, so its
  C legs (28/28, reissue coverage, byte preservation) remain unchecked by the round's own
  validator.
- Fold of D-R07-1..6 into `calib/C09-final-receipt.md` / `scribe/S03-c-receipt.md`: C03 is
  the table's author, C04/C09/S03 consume it; the corrections above are integrator-applied
  edits to *round-34* fragments (no filed byte is involved).

## Citations

- Read (digests in §0): `reports/round-34/calib/{C01,C02,C03,C04,C05,C06,C07,C08,C09}*.md`,
  `reports/round-34/scout/K04-anchor-census.md`, `reports/round-34/scribe/S03-c-receipt.md`,
  `reports/round-34/cross/X02-conformance.md`; `reports/round-34/claims.json:53-74`;
  `reports/round-34/targets.json` (R07 row, `shared_rules`)
- `reports/round-33/adj/A09-pins.md:85-94,103-116,120-126` (R1–R8, A09-F1..F5);
  `reports/round-33/cross/X00-connector.md:67-68` (SKILL/AGENTS rows: "any SKILL.md line
  ≥ 535 … must be re-derived"; my §3 refines the trigger to ≥ 585), `:256,277`;
  `reports/round-33/adj/audit-assembled.md:30,41` (`f9bd07c2…` first recorded)
- Live files: `SKILL.md` (`f9bd07c2…`, 732 L) lines `47,149,157,183,205,208,262,278,294,
  323,456-458,522,534-536,564,584,612,614,615,617,660-662,710,726,729,730-732`; `AGENTS.md`
  (40 L, `5ae7a9c8…`); `corpus/lessons/README.md` (448 L, `f752e1d7…`, blob `73f3e1bd…`)
  lines `103,105,242,244,245,254`; `corpus/lessons/{round-14.md:141,round-15.md:25,round-19.md:88,100,101,179,round-25.md:44,round-31.md:46,round-32.md:7,33,34,41,55,57,58}`
- Era blobs: `b02cfbc:SKILL.md` (305 L) `:157,:205,:208`; `16652e8:SKILL.md` (375 L)
  `:278,:323`; `139e3b6:SKILL.md` (715 L, `79fe91d3…`) `:157,:205,:208,:278,:564,:612,:615,:660,:713,:714,:715`;
  `139e3b6:AGENTS.md` (42 L) `:42`
- Filed instruments/pins: `reports/round-26/run-validation.py:96-97`; `SCORECARD.md:597-600`;
  `reports/round-30/craft/box1-survey.py:5-13`; `reports/round-30/craft/box1-landed-survey.json:4`
- Commands (2026-10-19T07:0x–07:14Z, repo root, `TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `git status --porcelain`;
  `git diff -U0 139e3b6 da68a6d -- SKILL.md | grep '^@@'` (13 hunks; first non-net-0 at
  `:584`); `git diff --numstat 139e3b6 da68a6d -- SKILL.md AGENTS.md corpus/lessons/README.md`
  → `35 18` / `0 2` / `130 28`; `sha256sum SKILL.md AGENTS.md corpus/lessons/README.md`;
  `wc -l` on the same; `git hash-object corpus/lessons/README.md`; `git show 139e3b6:AGENTS.md
  | grep -n "append one item"` → `42:`; `grep -n "append one item" AGENTS.md` → exit 1;
  `sed -n` line dumps at HEAD and at `b02cfbc`/`16652e8`/`139e3b6` for every anchor above;
  `python3 -B reports/round-30/craft/box1-survey.py` (exit 0, 28/28, `f9bd07c2…`);
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json` (exit 0, 33/33,
  findings 0); `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` (exit 1,
  `X45-P1`, 4 tuples); `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest`
  (exit 1, 28/37, 9 named failures); `grep -rl/-rn` digest censuses over
  `corpus/lessons/ reports/round-{1..33}/ tools/` and over the whole tree;
  `ls corpus/lessons/*.md`; `ls corpus/lessons/round-33.md` → absent;
  `grep -c "^\| \`corpus/lessons/" corpus/lessons/README.md` → 33;
  `python3 -B .scratch/r07-cmp.py` (C07 §7 comparator + normalized variant; both
  `MISMATCH []`, 56 key-name-skipped pairs)
