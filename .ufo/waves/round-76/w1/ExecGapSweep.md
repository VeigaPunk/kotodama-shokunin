# ExecGapSweep — round 76, wave 1 (claim C before-state receipt + do-nothing control design)

Seat: `ExecGapSweep`, leaf. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`98c486bdb4650ba5b8e651d332910e8ee60ad121` (lane HEAD at read time was `98c486b`; tree
`6e961f92169764069d36136752671301ce971677`). 2026-10-27. No delegation, no spawns, no background
job, no install, no lane/fleet write outside the two artifacts and this report, no fetch.

Mandate (assignment, verbatim in intent): (1) the claim-C before-state receipt at base; (2) the
concrete design of the do-nothing controls for C and Ca. Both are delivered; neither was measured,
because no round-76 counter exists yet — that is stated, not hidden (§5).

Deliverables (paths relative to the lane):
- `Report:` `.ufo/waves/round-76/w1/ExecGapSweep.md` (this file)
- `.ufo/waves/round-76/w1/stage/ExecGapSweep/gap-sweep.txt` — 302 lines, 17131 bytes,
  sha256 `9157e70666a1ffe5cd5bcd351122aee0499c8828110bc34c6d3d6d1b2b879e32`
- `.ufo/waves/round-76/w1/stage/ExecGapSweep/controls-design.md` — 324 lines, 21771 bytes,
  sha256 `3663e34ab88eb3273bbd0ca1ef86a3141c41a0659fd0800f3f467039bb765703`
  (`wc -c`/`wc -l`/`sha256sum` on both files, run in that directory).

Scratch: `/fast/scratch/hyaku/kotodama-r76/ExecGapSweep/` (only the `git archive` extract of
`corpus/` at base, plus `usedby.txt`); deleted before yield after the numbers were copied into the
receipt. Nothing under `/tmp` was written or cited.

---

## 1. Claim C before-state, measured at base

Every number below is in `gap-sweep.txt` with its command, raw output and exit code. Summary:

| quantity | value | command |
|---|---|---|
| knowledge `.md` files | **252** (exit 0) | `git -C <lane> ls-tree -r --name-only 98c486b corpus/knowledge \| grep -c '\.md$'` |
| knowledge files, all types | 252 | `… ls-tree -r --name-only 98c486b corpus/knowledge \| wc -l` |
| registry rows | **817** (exit 0) | `git -C <lane> show 98c486b:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` |
| registry rows (census form) | 817 (exit 0) | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (cwd = extract) |
| tier histogram | **A=491 B=310 C=16** (exit 0) | CORPUS.md manual census awk, from the extract |
| status histogram | **mined=722 queued=58 rejected=37** (exit 0) | same receipt |
| malformed rows (NF≠13) | **0** (exit 0) | CORPUS.md awk |
| duplicate ids | **none** (exit 0, no output) | CORPUS.md `sort \| uniq -d` |
| enum violations / tier inflation | **none** (exit 0) | CORPUS.md awk |
| used-by references resolving at base | **750 / 750** (0 missing) | `awk` over `git show 98c486b:corpus/SOURCES.md` + `git cat-file -e 98c486b:<path>` per path |
| last registry id | **S893**; S894–S898 present 0 times each | `grep -cE '^\|[[:space:]]*S(894…898)[[:space:]]*\|'` |
| maintained parser agreement | identical totals, `exit=0` | `scripts/sources-census.sh census --file …/SOURCES.md --today 2026-10-27` |

Both instruments (CORPUS.md manual awk and `scripts/sources-census.sh`) agree: 817 / 491 / 310 / 16 /
722 / 58 / 37 / invalid 0. The draft's after-state baselines (252, 817) are **confirmed at base**.

One scope correction the counter must carry: `reports/round-76/telemetry/census-start.txt` (already
installed) contains four `W01` lines — `S881`, `S882`, `S884`, `S893 tierC mined used-by=…` (raw in
`gap-sweep.txt` §1.5). A lane-wide reading of the draft clause "no tier-C row is the sole support of
an admitted entry" is therefore RED at base; the clause must be scoped to the round's admitted
entries.

### 1.1 The draft's before-predicate is false as written (independently reproduced)

Draft: "Before: `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and
`git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` each print nothing (exit 1)."

Measured (raw, `gap-sweep.txt` §2.1):
- `GB/T 33661` over `corpus` → `corpus/lessons/round-68.md`, `corpus/lessons/round-69.md`, **exit 0**
- `digital\.archives\.go\.jp` → `corpus/lessons/round-68.md`, **exit 0**
- `openstd\.samr` → `corpus/lessons/round-68.md`, **exit 0**
- `gmw\.cn` → no output, **exit 1** (the only one of the four that holds as written)

Scoped to the surfaces the claim moves — `corpus/SOURCES.md corpus/README.md corpus/knowledge` —
all four print nothing, **exit 1** (12/12 cells of the 4×3 matrix, §2.2). That is the honest
before-predicate. It is also the only scope a counter carrying round-75's GROUND leg can grade: that
leg re-derives absence from the base REGISTRY text only (`accept-c.py:2824-2828`).

The lesson hits are not noise: `corpus/lessons/round-68.md:111-112` records round-68's judgement of
the same documents under campaign ids — `S776 (openstd.samr.gov.cn GB/T 33661-2017 page, HTTP 200)`
listed as *present/adoptable*, and `S825 (digital.archives.go.jp/search is a portal landing, not the
table page)` among eight *refused* candidates. The claim's era half rests on a URL the lane has
already refused once; the Wayback capture (S935) is the only candidate carrier. Sibling
`w1/CritClaims1.md` F5 reaches the same conclusion; I reproduce the raw lines.

## 2. Staged-package facts that constrain claim C (measured; `gap-sweep.txt` §3)

1. **132 staged rows, 125 malformed.** NF histogram: `7×13, 115×14, 9×15, 1×16`. The break is an
   unescaped `|` inside the recheck cell (a shell pipeline: e.g. S908 `180d — \`curl -fsSL
   '…/search' | grep -c '元号名称'\` -> 3`), which also pushes the real used-by cell out of position
   and leaves a grep count where entry paths belong. Staged `opened` is 2026-10-23/24, not
   2026-10-27. ("Append the staged rows" fails NF=13, cadence-only recheck, used-by, and opened.)
2. **The four candidate entries, as staged:**

   | staged file | bytes | words | `## ` sections | body words after first `## ` |
   |---|---|---|---|---|
   | `calendar-festival-systems.amend-2026-10-24.md` (a) | 7571 | 1094 | 1 | 537 |
   | `calendar-festival-systems.amend-2026-10-24-r10.md` (b) | 3385 | 445 | 0 | 0 |
   | `era-periodization-models.amend-2026-10-23b.md` (c) | 1983 | 275 | 0 | 0 |
   | `calendar-festival-systems.amend-2026-10-23c.md` (d) | 2406 | 340 | 0 | 0 |

   Round-75's ENTRIES leg requires "at least one `## ` section, and a body of at least 478 words"
   (`accept-c.py:1176-1180`, floor `_ENTRIES_WORD_FLOOR = 478`). **As staged, only candidate a
   clears that shape; b, c and d have no `## ` section at all and are below the floor.** The floor
   is not a full-entry bar imposed on short amendments: at this base the *minimum* knowledge file is
   itself an amendment, `heritage-taxonomy-models.amend-2026-10-24-r13.md`, at exactly 478 words
   (`find corpus/knowledge -name '*.md' | xargs wc -w | sort -n | head -4`). So "n>=2 from these four
   files" is reachable only by rewriting at least one more entry inside the claim — the draft must
   either declare that rewrite or declare a different, justified shape gate. (Sibling F2 measured
   the word counts; the `## `-section result and the 478-is-an-amend derivation are this seat's.)
3. **Absent-at-base holds** for all four candidate paths (base `culture-material/` carries no
   calendar/era `*.amend-2026-10-2*`), and the amend parents exist: `calendar-festival-systems.md`
   (4603 words, 12 `## `) and `era-periodization-models.md` (4873 words, 14 `## `).
4. **Cost-free ids hold:** last id S893; S894–S898 absent (0 each).
5. **Collisions:** `wc -l .ufo/waves/round-76/assimilation/collisions` → **35** (S859–S893). Beyond
   that band the staged entry BODIES cite campaign ids S750, S757, S718, S719, S807, S777; at base
   those lane ids are unrelated documents — S718 Farran 2016 (infant-directed speech), S719 Cristia
   2013, S750 Culin 1907, S757 Huizinga, S807 Li 2021 (median artery); S777 has no row at all. The
   declared already-held pair resolves as documented (S919→S892 Marrone, S921→S885 Barthes).
6. **Couples dangle:** of the `couples:` targets in the four candidates, `linguistics/naming-systems.
   amend-2026-10-24.md`, `culture-material/era-periodization-models.amend-2026-10-23.md` and
   `culture-material/calendar-festival-systems.amend-2026-10-23.md` are **absent** at base and are
   not among the four candidates; two further targets are sibling candidates (chicken-and-egg).
   Checked with `git cat-file -e 98c486b:corpus/knowledge/<rel>`.
7. **README index:** rows exist for the parents (`corpus/README.md:416`, `:423`); the four new files
   are four new index rows plus a `Counts checked` footer, which the draft's after-state does not
   mention (r75's INDEX leg required one row per adopted entry).

## 3. Controls design (`controls-design.md`) — shape and the three r75 holes it closes

The design gives, for each control: the exact mutation, where the mutation commit must sit
(`--freeze` vs `--lands`), the legs that must go red, the legs that must stay green, and the
round-75 receipt that already proves (or fails to prove) that leg.

Claim C: **C-a** `lands == freeze` (carried); **C-b** four header-only stubs, zero rows
(carried, J1 shape); **C-b2** stubs + sed-renumbered rows + README rows + a Gate table — the
*sizing* control that must PASS nowhere if the claim carries a content clause (CritClaims1 F3);
**C-c** staged rows and entries verbatim (new, must be built; measured red surface: CENSUS `E01`,
ROWS, REPOINTED, COLLCHECK); **C-d** entry files landed with every claim resting on held row S885
(new; red on REPOINTED by-document join, ROWS, EVIDENCE quote-in-window, GATE); **C-e** the draft's
own false before-state landed as the GROUND receipt (new, one file, guards the defect in §1.1).

Claim Ca: **Ca-a** `lands == freeze` (carried: r75 `FAIL legs=7/12`); **Ca-b** constant printers
whose ledger is the blob at `--freeze` — the only placement that reaches the LEDGER clause, with six
argv variants (literal printer, evasive printer, shell string, allowlist escape via `awk`/`env`/
`xargs`/`sed`, interpreter, min-pairs trim); **Ca-b2** the same printers at `--lands` (carried J4/
J4b/J4c/J4m — red on FROZENCFG, **not** LEDGER); **Ca-c** correction rows naming only ids (carried
J5; plus SEPARABLE and a rederive-execution variant); **Ca-d** the routed literal-`/tmp` defect,
static + dynamic (r75 `R74_TMPDIR = "/tmp"` at `accept-ca.py:2175`; `accept-c.py:6024` bans `/tmp`
as `--work` but falls back to `tempfile.gettempdir()` at `4450`, `5594`).

The three round-75 weaknesses the design is built to avoid, each with its raw line:
1. **Red baselines void fixtures.** `junk-ca.txt` J4/J4b/J4c/J4m/J4f/J5/J6/J7/J8/J9/J10 all print
   `baseline-legs: … APPENDONLY=FAIL, … COMBINED=FAIL, …`; J6/J7/J10 report `newly-red: (none)`
   against `expected-legs: APPENDONLY` — three APPENDONLY fixtures proved nothing. Only fixture `R`
   reached it (`newly-red: APPENDONLY`). Round 76 must measure a clean-landing baseline first and
   report a fixture void otherwise.
2. **The wrong blob.** J4f intended to be "the only fixture that reaches the LEDGER clause itself",
   but its `--freeze` still named the clean ledger (`--lands 8233ddb --freeze 5d016746`), so the
   result is `LEG PASS LEDGER` … `newly-red: FROZENCFG`, `expected-legs: LEDGER`, `accepted: no`.
   **No round-75 fixture ever turned LEDGER red.** Ca-b moves the printers behind `--freeze`.
3. **`accepted: no` is the good outcome.** In `junk-fixtures.py` the `accepted` list is the set of
   fixtures whose counter verdict was PASS; every r75 fixture printed `accepted: no`, i.e. all junk
   was refused. The round-76 receipt must keep that polarity explicit so it is not misread.

Design commitments the freeze must fix before any control can be measured are listed in the file's
§5 (leg names and pass convention; per-leg `--freeze`/`--lands` read; tier-C scope; document
identity S908+S935 fold vs S932/S938 split and therefore `k`; the content clause C-b2 tests).

## 4. What this seat did NOT do (and why that is not a gap it can close)

- **No round-76 counter was run**: neither `reports/round-76/accept-c.py` nor `accept-ca.py` exists
  at base (`ls reports/round-76/` → `telemetry/` only). Every "expected" row in the design is a
  commitment to be frozen and then measured in wave 2 by the counter owners; nothing is claimed as
  observed.
- **No fetch**: the four documents' reachability and the Wayback captures are the scouts' lane
  (`w1/ScoutDocS894…S898.md`). This seat's four negative sweeps are text sweeps over committed
  bytes, not access attempts.
- **No lane or fleet mutation**: all lane reads were `git -C <lane> show/ls-tree/grep/cat-file` plus
  `git archive` into this seat's scratch. `git status --short` was not needed and not run.

## 5. Risks, ranked (each with its measurement)

1. **`n>=2` is not reachable from the staged bytes under the r75 entry shape**: only candidate a has
   a `## ` section, and only a exceeds 478 words (§2 item 2). The claim must declare the rewrite or
   a different gate before the freeze, or the landing fails as declared.
2. **Candidate d is inadmissible by the draft's own rule**: its only `source:` line is S916, tier C
   ("sources: the one row above, tier C" in the staged text), and its corroborating ids S718/S719 are
   not held. Independently, `w1/ScribeEntryD.md` F2 finds the cited page carries no 原文 block. If d
   is counted in the pool, the "no tier-C sole support" clause kills it; if dropped, `n` must still
   reach 2 from {a,b,c}, i.e. b or c must be rewritten anyway.
3. **Body campaign ids are not covered by the 35-id collision guard** (S718/S719/S750/S757/S807/S777
   resolve to unrelated lane rows, S777 to none). The kill rule as written ("a cited
   campaign-namespace id → fails") would fail even a correct landing unless the citations are
   rewritten by document or the check is scoped to `source:` lines — and then the earlier ids remain.
4. **The tier-C clause is RED at base if read lane-wide** (four `W01` rows in the installed
   `census-start.txt`). Scope it to the round's admitted entries or the claim cannot pass.
5. **GROUND scope is false as written** (§1.1); a receipt written to the draft's wording cannot be
   graded by a registry-scoped counter and would certify the wrong scope.
6. **`k` is a definition, not a value, and its document-identity fold is unfrozen**: S908+S935 are
   folded into one row while S932+S938 are split, and `S938`'s own staged note reports its
   `type=online` route byte-identical to `type=download` (24148 bytes, md5 `9791d9dc…`). `k` is 5
   under the draft's plan; a fold decision changes it and the Gate admit rows. (Sibling F8.)
7. **Dangling couples and unclaimed README work** (§2 items 6–7): a "couples resolve at lands" leg
   fails as staged; the after-state omits the four index rows and the `Counts checked` footer.
8. **Counter reuse**: freeze the candidate paths and document identity, derive `n`/`k`/row ids from
   committed bytes, and print the derivation — a frozen row_set cannot express a threshold claim
   (`w1/CritCounterReuse.md`; the design's rule 4).

No blocker: the assignment's two artifacts are complete, and every claim above carries its command
and raw output in `gap-sweep.txt` or in the round-75 receipts cited by file and line.
