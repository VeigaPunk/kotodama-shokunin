- Seat: C03 | executor | C | date 2026-10-19 | baseline da68a6d

# C03 — the A09 R1–R8 anchor reissue: old anchor → new anchor → owning row

**Mission** (`reports/round-34/targets.json:57`): "Anchor reissue table: for each A09
R1-R8 row, the old anchor → new anchor (post-732-line SKILL.md) → owning
row/section, each verified by your own grep with the cited line content."

**Method.** HEAD is `da68a6d705e41f369f21e8607bfaab5b54077f84`; the working tree
equals HEAD (`git status --porcelain` → `?? reports/round-34/` only, so no seat
has dirtied a tracked file). Old bytes are the round-33 dispatch baseline
`139e3b6:SKILL.md` / `139e3b6:AGENTS.md` / `139e3b6:corpus/lessons/README.md`
(`git show`); new bytes are the live files at HEAD. The old→new line map is a
**difflib opcode table** over the two byte sets (`.scratch/c03/map.py`), then
every anchor's *content* is asserted old→new by the re-runnable verifier in §7 —
never by arithmetic alone. No filed byte, no `corpus/lessons/*.md` byte, no
`tools/gates/frozen/**` byte and no shared file was edited by this seat; the
reissue below is a **new table**, which is what claim C's `after_required`
asks for ("old anchors recorded as superseded readings, filed rows untouched").

## 1. What actually moved (the reissue's premise)

| file | at `139e3b6` | at HEAD `da68a6d` | command |
|---|---|---|---|
| `SKILL.md` | 715 lines, sha256 `79fe91d3…` | **732 lines**, sha256 `f9bd07c2…`, diff 35 added / 18 removed | `sha256sum`; `git diff --numstat 139e3b6 HEAD -- SKILL.md` |
| `AGENTS.md` | 42 lines (blob `959accc`) | **40 lines**, sha256 `5ae7a9c8…`, diff 0 added / **2 removed** | `wc -l`; `git diff 139e3b6 HEAD -- AGENTS.md` |
| `corpus/lessons/README.md` | 346 lines, `ec7469da…`, blob `a3187055…` | **448 lines**, `f752e1d7…`, blob `73f3e1bd…` | `sha256sum`; `git hash-object` = `git rev-parse HEAD:` |

`SKILL.md` moved in **two classes**, which is the whole reason a single
"old+N" rule would be wrong:

- **(a) eight same-line rewrites** — `:128, :479, :481, :483, :486, :488, :491,
  :501`: anchor number stable, content changed (the round-33 C14 Fixes 1–3,
  applied by the integrator). `git diff -U0 139e3b6 HEAD -- SKILL.md` shows
  exactly `@@ -128 +128 @@` … `@@ -501 +501 @@` for these.
- **(b) five insertion hunks** — old `:584` (1→3 lines), `:694-697` (4→5),
  `:699-700` (2→4), `:704` (1→12), `:714-715` (2→3): cumulative deltas **+2,
  +3, +5, +16, +17**. Only these move anchors; everything at or below `:584`
  keeps its number.

Anchored headings are stable except the D3 pair: `## Checklist (executable
where a tool exists)` `522`→**522**, `## Corpus map` `536`→**536**,
`## Error patterns` `468`→**468**, `## Gates and probes` `575`→**575**,
`### Register craft` `354`→**354**, `### Family-clean projection…` `243`→**243**,
`### Slot-label routing…` `130`→**130**, `### Label typing…` `31`→**31**;
`## Source-bounded culture drill — D3 (round 7)` `660`→**662** and
`### D3 replay checklist…` `685`→**687**.

**The one retirement.** `AGENTS.md:42` was not shifted — it was **deleted** by
`da68a6d`. `git diff 139e3b6 HEAD -- AGENTS.md` removes exactly the closing
code fence plus the line `### 2.2 SKILL.md — append one item to "## Checklist
(executable where a tool exists)" (after :534)`; `grep -n "append one item"
AGENTS.md` → rc=1 (0 hits). The only live instruction that carried the
"append after `:534`" anchor is gone (§5).

## 2. The reissue table — A09 R1–R8, old anchor → new anchor → owning row

A09's R1–R8 list is `reports/round-33/adj/A09-pins.md:105-114`. Each row below
names the old anchor as filed, the post-round-33 anchor/value measured by this
seat, the owning row/section, and my own verification.

| # | artifact (A09 row) | old anchor (pre-r33 bytes) | new anchor at HEAD `da68a6d` | owning row / section | verify |
|---|---|---|---|---|---|
| **R1** | README blob pin | `README_BASELINE_BLOB = "a3187055…"` at `reports/round-26/run-validation.py:97` (mirror `reports/round-26/lessons/c51-revision-audit.py:48`) | live blob **`73f3e1bd29d4569ddd2a5d9a2309f4451fa35ae5`** — the pin is now a **stale reading**, supersession record owed | A09-F1 (`A09-pins.md:122`) + new round-34 supersession row | `git hash-object corpus/lessons/README.md` = `git rev-parse HEAD:corpus/lessons/README.md` = `73f3e1bd…` ≠ `a3187055…` |
| **R2** | README sha256 receipts | `ec7469da…` (6 sites named at `A09-pins.md:71`) | **`f752e1d79ae627a0d9728fe16fd1532e7cb9e587f6ac7025a880d8af46233868`** (43 454 B / 448 lines); first durable record `reports/round-33/validation.json:1019` | A09 R2 (`A09-pins.md:108`); `SCORECARD.md:588` carries the before→after | `grep -rn 'ec7469da'` → **95 line-hits in 47 files** (the census is far larger than A09's six sites: also `corpus/lessons/round-26.md:141`, `reports/round-25/fragment-index-x44.md:236`, `reports/round-26/audit/x63-lessons-audit.md:21,76,88,246,257`, `reports/round-25/lessons/C35-C36.md:25,30`, `reports/round-26/lessons/C53.md:31,219`); `grep -rn 'f752e1d7'` → 20 hits |
| **R3** | SKILL.md sha256 receipts | `79fe91d3…` (8 surfaces / 10 line-hits: `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`; `reports/round-32/dossier-d11-shonen-boxes.md:50,205`; `reports/round-32/dossier-d12-capability-inventory.md:97`; `reports/round-32/dossier-d13-operator-decisions.md:48`; `reports/round-32/final-dossier.md:46,133`; `reports/round-32/scribe/fragment-ledger.md:178,235`) | **`f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`**; recorded at `reports/round-33/adj/audit-assembled.md:30` and `SCORECARD.md:599` (`79fe91d3…` → `f9bd07c2…`) | A09 R3 (`A09-pins.md:109`) | `grep -rn '79fe91d3'` → **127 hits in 44 files**, of which only `SCORECARD.md:599` and `LOG.md` are non-filed; `grep -rn 'f9bd07c2'` → 107 hits |
| **R4** | box-1 re-survey receipt | `reports/round-30/craft/box1-landed-survey.json:4-6` → `skill_sha256 83b0a78a…`, `named_in_skill 28`, `resolvable 28`, date 2026-10-18 | **28/28 at `f9bd07c2…`**, exit 0; durable receipt owed at `reports/round-34/craft/box1-resurvey-durable.json` (claim C's `after_required`, C01/C02 own the bytes) | A09 R4 (`A09-pins.md:110`); C14 note 4 (`C14-fix-drafts.md:518`) | my own run, §6; `grep -n 'skill_sha256' reports/round-30/craft/box1-landed-survey.json` → `83b0a78a…` |
| **R5** | SKILL.md line anchors (`AGENTS.md:42`; self-cites `:149,:183`; filed lesson citations) | the §3 table's "old" column | the §3 table's "new" column; `AGENTS.md:42` **retired** | A09-F3 (`A09-pins.md:124`), R5 (`:111`) | §3 + §7 verifier (30 rows, failures 0) |
| **R6** | README prose arithmetic + row cells | `corpus/lessons/README.md:97` "**Rows: 26. Files: 26.**"; `:207` "Rows: **49**. Of the 26 index rows, **23 carry at least one question**" | **`:105`** "**Rows: 33. Files: 33.**"; **`:254`** "Rows: **78**. Of the 33 index rows, **30 carry at least one question**"; revision-3 section `:398-442` | A09 R6 (`A09-pins.md:112`); O02 delta (`reports/round-33/op/O02-readme-delta.md`) | `sed -n '105p;254p'`; my `c31` run: exit 0, `index rows 33 / lesson files 33 / queue rows 78`, 6/6 PASS, `findings 0` |
| **R7** | x45 / x57 instruments | `x45` exit 1, `X45-P1`; `x57 --selftest` 34/37 (both as read at `139e3b6`) | **`x45` exit 1**, `FAIL P1_pointers_resolve`, findings 1 with **4** unresolved-pointer items; **`x57 --selftest` exit 1, 28/37** | A09-F4 (`A09-pins.md:125`); standing debt row, "do not cite as green" | my re-runs, §6 |
| **R8** | README rows vs `round-33.md` landing order | partition 33 `*.md` (32 lesson files + `README.md`) | `corpus/lessons/round-33.md` **does not exist** at HEAD → no orphan row owed; revision-3 covers rounds 26–32 (`README.md:108`) | A09 R8 (`A09-pins.md:114`); `README.md:398-442` | `ls corpus/lessons/round-33.md` → No such file; `ls corpus/lessons/*.md \| grep -vc README` → 32; `ls corpus/lessons/*.md \| wc -l` → 33 |

No R-row is a frozen-baseline re-pin; A09's §1.1 zero-exposure finding was not
re-opened by this seat (nothing in this round's reissue touches
`tools/gates/frozen/**`).

## 3. R5 in full — every line anchor, old → new, owning row/section

Classes: **identical** (content byte-equal, number maybe shifted), **in-place**
(same number, content rewritten), **rewritten** (range restructuring),
**retired** (target deleted). "Owning row/section" is the nearest enclosing
SKILL.md heading (computed by machine over the new bytes) plus the filed row
that cites the anchor.

| old anchor | new anchor | class | owning row / section (new bytes) | cited by (old anchor, filed) |
|---|---|---|---|---|
| `AGENTS.md:42` | **retired — line deleted** | retired | its target section `## Checklist (executable where a tool exists)` `:522-534` is unchanged; the r31 item it pointed at now lives at `:729-732` | `corpus/lessons/round-31.md:46` ("the draft's SKILL anchor … is **correct**"); A09-F3 |
| `SKILL.md:47` | `SKILL.md:47` | identical | `### Label typing — translated labels, native forms, borrowed strata` `:31` — row `Untyped legacy record` | `SKILL.md:149`, `SKILL.md:183` (self-cites) |
| `:149` | `:149` | identical | `### Slot-label routing…` `:130` — register-exemption row | SKILL.md self |
| `:183` | `:183` | identical | `### Slot-label routing…` `:130` | SKILL.md self |
| `:157` | `:157` | identical | `### Slot-label routing…` `:130` | `corpus/lessons/round-15.md:25` |
| `:205` | `:205` | identical | `### Derivation replay…` `:189` — replay-requirement table header | `corpus/lessons/round-15.md:25` |
| `:208` | `:208` | identical | `### Derivation replay…` `:189` — "Named inputs" row | `corpus/lessons/round-14.md:141` |
| `:189-214` | `:189-214` | identical | `### Derivation replay…` `:189` (whole section) | `corpus/lessons/round-25.md:44` |
| `:262-278` | `:262-278` | identical | `### Family-clean projection…` `:243` — gates-and-probes table rows | `corpus/lessons/round-19.md:101` |
| `:278` | `:278` | identical | `### Family-clean projection…` `:243` — batched spot-check row | `corpus/lessons/round-19.md:88,179` |
| `:294` | `:294` | identical | `### Family-clean projection…` `:243` — `Propagation/tamper` row (`mirror_unsafe` exit-2 r24 cold-run control) | `corpus/lessons/round-31.md:46`; `round-32.md:58`; `corpus/lessons/README.md:245` |
| `:323-375` | `:323-375` | identical | `### Family-clean projection…` `:243` — decision-table block | `corpus/lessons/round-19.md:100` |
| `:375` | `:375` | identical | `### Register craft` `:354` — stratum-derivation row | (range end) |
| `:456-458` | `:456-458` | identical | `### Register craft` `:354` — mirror-safety prose | `corpus/lessons/round-31.md:46` |
| `:522` | `:522` | identical | `## Checklist (executable where a tool exists)` heading | `round-31.md:46`; `round-32.md:33,57`; `README.md:244` |
| `:534` | `:534` | identical | last content line of the checklist (`handoff-packet-check enforces per packet`) | `round-31.md:46` |
| `:535` | `:535` | identical | blank separator | `round-31.md:46` |
| `:536` | `:536` | identical | `## Corpus map` heading | `round-31.md:46` |
| `:660` | **`:662`** | identical, **+2** | `## Source-bounded culture drill — D3 (round 7)` heading | `round-32.md:33,57` |
| `:710` | **`:726`** | identical, **+16** | `### D3 replay checklist…` `:687` | `round-32.md:33` |
| `:713` | **`:729`** | identical, **+16** | `### D3 replay checklist…` `:687` — r31 landed item, first line | `round-32.md:33,57`; `README.md:244` |
| `:714-715` | **`:730-732`** | **rewritten** (2→3) | the item's audit one-liner, re-keyed to `closes` / `closes_sha256` (round-33 O05 draft; `reports/round-33/op/O05-falsifier-disposition.md:78-118`) | `round-32.md:7,41,55`; `README.md:242` |
| `:128` | `:128` | in-place | `### Claim uncertainty typing…` `:77` — basis-row cite repointed to `tools/harness/packet_uncertainty.py:205,209` | `round-32/final-dossier.md:46` (`:128` mis-cite, box-1 condition 3) |
| `:479`,`:481`,`:483` | same numbers | in-place | `## Error patterns` `:468` — `TL-01`/`TL-02` retired-anchor errata | `round-32/final-dossier.md:46` (condition 4) |
| `:486`,`:488` | same numbers | in-place | `## Error patterns` `:468` — loanword-dating cites `:30-31,63` / `:59,63` | `round-32/final-dossier.md:46` (condition 2) |
| `:491` | `:491` | in-place | `## Error patterns` `:468` — `FIELD_DEFAULTS` retired anchor → live projection | `round-32/final-dossier.md:46` |
| `:501` | `:501` | in-place | `## Error patterns` `:468` — contract-`:183` mis-cite erratum | `round-32/final-dossier.md:46`; `round-33/calib/C16-receipt.md:65` |

**Housekeeping consequences.** (i) `AGENTS.md:42`'s "append after `:534`" and
`corpus/lessons/round-31.md:46`'s confirmation of it are both now *historical*:
the section boundary `:522-534` is unchanged, but the landed item sits at
`:729-732` — outside `## Checklist`, i.e. Q-32-3 / F-X16-2 (`corpus/lessons/README.md:244`)
is still open and the deletion removes the instruction that would have carried
it. (ii) `corpus/lessons/README.md:242,244,245` (filed in round 33) cite
`:715`, `:713-715`, `:522-534`, `:294`; the first two reissue to `:732` and
`:729-732`. (iii) `SCORECARD.md:520` cites `SKILL.md:264`; that anchor is
**unchanged** — `:264` is byte-identical old→new and below the first hunk.
(iv) **Era caveat** — the `:157`, `:205`, `:208`, `:262-278`, `:278`,
`:323-375` rows above are identical *relative to the pre-round-33 revision*
(the round-33 baseline this table maps from), but the filed citations that own
them were written against older era blobs and are therefore era-relative; §9
resolves their live referents.

## 4. What needs no reissue (and why that is not an assumption)

21 anchors in §3 verify byte-identical. Every anchor the box-1 conditions 2–4
depend on is in the stable region — `:128`, `:486`, `:488`, `:501`
(conditions 2/3) and `:479`/`:481`/`:483`/`:491` (condition 4), each rewritten
**in place at the same line number** — while the r31 item's own first line
shifted `:713`→`:729` and its audit one-liner `:714-715`→`:730-732`. The
claim-C threshold "the reissue table covers every A09 R1–R8 row" is met by §2;
§3 is the R5 expansion.

## 5. Retirement finding — `AGENTS.md` lost the SKILL anchor in `da68a6d`

- Old: `git show 139e3b6:AGENTS.md | wc -l` → **42**; `:42` =
  `### 2.2 SKILL.md — append one item to "## Checklist (executable where a tool exists)" (after :534)`.
- New: `wc -l AGENTS.md` → **40**; `grep -n "append one item" AGENTS.md` → rc=1;
  `grep -c "2.2 \`SKILL.md\`" AGENTS.md` → 0. `sha256sum AGENTS.md` →
  `5ae7a9c8abab0843cfc6db09849f2fff369c0e880085deb546ec7ab764333808`.
- `git diff 139e3b6 HEAD -- AGENTS.md` is exactly `0 added / 2 removed`
  (`-``` ` closing fence, `-### 2.2 …`).
- This is **class "retired", not "shifted"**: any table that maps `AGENTS.md:42`
  to a new line number would be fabricating an anchor. The instruction that the
  anchor lived on no longer exists; A09-F3's "live line anchor" finding is
  discharged by deletion, and the reissue records the retirement.

## 6. Backing measurements for R4 and R7 (my own runs, 2026-10-19)

**R4 — box-1 re-survey at HEAD bytes** (`python3 -B reports/round-30/craft/box1-survey.py`,
read-only: the tool only reads `SKILL.md` and prints, `reports/round-30/craft/box1-survey.py:5-13`):

```
exit 0
{"date": "2026-10-18", "named": 28, "resolvable": 28, "unnamed_in_skill": [],
 "skill_sha256": "f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"}
```

**Trap for the durable receipt (R4).** The tool's `date` field is a **hardcoded
literal** — `"date": "2026-10-18"` at `reports/round-30/craft/box1-survey.py:8` —
so a receipt that pastes this JSON verbatim carries a wrong date. The
`reports/round-34/craft/box1-resurvey-durable.json` receipt must carry its own
dated stamp and cite the tool output; C01/C02 own that file, this note is the
handoff.

**R7 — the two instruments, re-read at HEAD** (both are read-only audits; the
`x45` run printed and wrote nothing — `git status --porcelain` after both runs
is still `?? reports/round-34/`):

- `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` → **exit 1**;
  `FAIL P1_pointers_resolve`, `PASS P2_prose_counts`, `PASS P3_queue_cross_consistency`;
  `findings: 1` — `X45-P1 unresolved-pointer` now carries **4** items: the
  original round-4 `reports/round-4*` glob plus three cite-form items from the
  round-33 README (`corpus/lessons/round-26.md:178-186`,
  `round-27.md:165-193`, `round-29.md:110`).
- `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` → **exit 1**,
  `passed 28 / total 37` (9 failing historical controls). The failures and their
  observed values are the *historical* readings, so the drop from A09's 34/37
  is the round-33 README revision moving live bytes: `partition is 27 md files`
  observed **33**; `filed rows are 26` observed **33**; `filed queue is 49 rows`
  observed **78**; `filed orphan is exactly round-26.md` observed `[]`;
  `revision has no orphan` observed `["round-27.md"…"round-32.md"]`;
  `G2 silent when the revision pin matches the live bytes` observed the README
  drift `claimed 29059 B/346 lines/ec7469da` vs `live 43454/448/f752e1d7`;
  `I reads 49 queue ids` observed `[78, 49]`; `I is green on the live revision`
  observed `["Q-26-1","Q-26-2","Q-27-1"]`; `revision pins drift on exactly one row`
  observed `["README.md","round-26.md"]`.
  The cause attribution (round-33 README landing) is my inference from the
  observed values and is marked **to-verify** as a cause; the *readings* are
  measured.

**R6 — the counting command is green at HEAD**:
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → **exit 0**,
`lesson files: 33 / index rows: 33 / queue rows: 78`,
`formats {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}`,
`PASS C31_index_rows_eq_files`, `C32_owners_resolve`, `C33_formats_documented`,
`C34_pins_rederived`, `C34c_shape_cells_rederived`, `C34b_prose_arithmetic`,
`findings: 0`.

## 7. Re-runnable verifier (the "each verified by grep" leg)

Source: `.scratch/c03/check-anchors.py` (30 rows: 21 identical/rewritten line
pairs + 8 in-place + the AGENTS retirement). It reads `git show 139e3b6:SKILL.md`
and the live `SKILL.md`, asserts range content equality for every *identical*
row, content inequality for the *rewritten*/*in-place* rows, and the
`AGENTS.md` 42→40 deletion. Observed:

```
[... 21 identical/rewritten rows PASS ...]
[PASS] old:714-715 -> new:730-732 rewritten   | "      validation.json has landed carries a closing snapshot ..."
[PASS] old:128 -> new:128 in-place  | "rejected (`tools/harness/packet_uncertainty.py:205,209`; v2-design §2.3 ..."
[PASS] old:479 -> new:479 in-place  | "| A label-only record passes silently | ..."
[PASS] old:481 -> new:481 in-place  | "| A sound kind declared with no bytes supplied | not clean: ..."
[PASS] old:483 -> new:483 in-place  | "| A record with no declared kind at all | refused with a stable reason: ..."
[PASS] old:486 -> new:486 in-place  | "| A loan's oldest form used to date the referent's arrival | ..."
[PASS] old:488 -> new:488 in-place  | "| Imported prestige terminology for locally made goods read as evidence ..."
[PASS] old:491 -> new:491 in-place  | "| Era tags or slot glosses graded on the name/sound channel | ..."
[PASS] old:501 -> new:501 in-place  | "| Two claims share one basis sentence, or a basis restates the status wo..."
[PASS] AGENTS.md:42 retired (42 -> 40 lines; '2.2 `SKILL.md`' present: False)
rows=21+8+1  failures=0
```

`checker exit=0`. Complementary greps used for the §2 rows:
`grep -rn "SKILL\.md:[0-9]"` tree-wide → **1169 line-hits in 266 files**
(`reports/` 256 files, `corpus/` 7, `SKILL.md` 1, `SCORECARD.md` 1, `LOG.md` 1);
**`tools/` → 0 hits**, `AGENTS.md` → 0 hits at HEAD. Live (non-filed) surfaces
are exactly `corpus/lessons/` (18 hits in 7 files:
`round-14,round-15,round-19,round-25,round-31,round-32,README` — of which 15 are
non-README and `README.md` carries 3 at `:242,:244,:245`), `SCORECARD.md:520`
(1 hit, `SKILL.md:264`), `SKILL.md:149,183` (2 self-cites) = 21 hits. Everything
else is a filed historical reading — superseded, never edited.

## 8. Byte-preservation

This seat wrote only `reports/round-34/calib/C03-anchor-reissue.md` (plus
`.scratch/c03/` scratch). `git status --porcelain` before and after every
command run above reads `?? reports/round-34/` — no tracked file modified, so
`reports/round-1..33/**`, `corpus/lessons/*.md` and `tools/gates/frozen/**` are
untouched; the module-loading runs (c31, x45, x57, box1-survey) wrote no file.

## 9. Era-relative citations — adopting C08-F1, with the live referents measured

`reports/round-34/calib/C08-verify-reissue.md:135` files **C08-F1**: "old anchor
exists as cited" is revision-relative — the r14/r15/r19 citations resolve only
against their era blobs, not against the pre-edit revision. This seat
reproduced that independently and extends it with the **referent's live
address**, which a pre-r33→HEAD map alone cannot produce (the map preserves the
*number*, not the *meaning*):

| filed cite | era blob | era line = what the row saw | live referent at HEAD `da68a6d` | my command |
|---|---|---|---|---|
| `corpus/lessons/round-14.md:141` | `b02cfbc` (305 lines) | `:208` = `| isolated legacy selftest battery | gate | …` | **`:617`** | `grep -n "isolated legacy selftest battery" SKILL.md` → `617:` |
| `corpus/lessons/round-15.md:25` | `b02cfbc` | `:157` = "…A disappearing uncertainty marker is not a verified claim."; `:205` = `| uncertainty-inventory | probe | …` | **`:564`** and **`:614`** | `grep -n "A disappearing uncertainty marker"` → `564:`; `grep -n "uncertainty-inventory | probe"` → `614:` |
| `corpus/lessons/round-19.md:88,179` | `16652e8` (375 lines) | `:278` = the battery row | **`:617`** | as above |
| `corpus/lessons/round-19.md:101` | `16652e8` | `:262-278` = the `| name | kind | entry command … |` table (battery row at `:278`) | `## Gates and probes` `:575`; header **`:604`**; rows **`:606-617`** | `awk 'NR>662…'`; `grep -n "^| name | kind | entry command"` → `604:` |
| `corpus/lessons/round-19.md:100` | `16652e8` | `:323` = `## Source-bounded culture drill — D3 (round 7)` heading (older census: `corpus/lessons/round-19.md:179` names `e8d238a6…`) | **`:662`**, section runs to EOF `:732` | `git show 16652e8:SKILL.md \| sed -n '323p'`; `grep -n "Source-bounded culture drill" SKILL.md` → `662:` |
| `corpus/lessons/round-25.md:44` | `fc13cd2` (598 lines) | `:189-214` **byte-identical** to the pre-r33 revision | `:189-214` (unchanged) | module-level compare of `fc13cd2:SKILL.md[188:214]` vs `139e3b6:SKILL.md[188:214]` → equal; cited row `Round-trip corruption class` at `:210` |
| `corpus/lessons/round-31.md:46`; `round-32.md:7,33,41,55,57,58` | `17e90b9` = the pre-r33 revision (`git log --oneline -- SKILL.md`: `da68a6d` follows `17e90b9` directly) | as §3 | as §3 | §7 verifier |

**So the §3 rows split in two.** Era-stable (their citing round's era **is** the
pre-r33 revision, or byte-identical to it): `:47`, `:149`, `:183`, `:189-214`,
`:294`, `:456-458`, `:522`, `:534-536`, `:660`, `:710`, `:713-715`, plus the
eight in-place `## Error patterns` / `:128` lines. Era-relative (a live
*semantic* re-point is needed, not just the number map): `:157`, `:205`,
`:208`, `:262-278`, `:278`, `:323-375` — their rows above give the live
addresses. C08's row-by-row verdict remains owed
(`reports/round-34/calib/C08-verify-reissue.md` `## Owed`); this section is the
authorship-side reconciliation, not a substituted verdict.

## Owed

- `reports/round-34/craft/box1-resurvey-durable.json` — R4's **new anchor** is
  still not on disk (`ls reports/round-34/` → no `craft/` at this seat's close).
  Its content owners have landed: `calib/C01-survey-run.md` (survey stdout,
  exit 0) and `calib/C02-receipt-json.md` (the receipt JSON, which already
  resolves the hardcoded-`date` trap at `C02-receipt-json.md:57,416-417`). The
  integrator lands the file; this table names the target and the trap.
- `reports/round-34/calib/C04-byte-check.md` (landed) — the R-row 0-edit proof
  is C04's mission; §8 above is this seat's own narrower reading.
- **Row-by-row verdict on this table** — `calib/C08-verify-reissue.md` has
  landed with the independent ground truth, the acceptance checks A–F, and its
  own `## Owed` for the comparison; §9 folds in its F1 finding from the
  authorship side. The comparison against these bytes is owed by C08/integrator,
  and this seat cannot be its own verifier.
- `reports/round-34/review/R06-c-review.md`, `review/R07-c-review.md` —
  second/third C-pass reviews of this table.
- `reports/round-34/calib/C05-receipt.md`, `C06-scribe.md` — claim-C
  before→after narrative and Landed-changes material consume this table.
- **Era-relative re-points (§9)** — the six era-relative rows are recorded
  readings, not edits: `corpus/lessons/*.md` is on this round's never-edit list,
  so the live referents (`:617`, `:564`, `:614`, `:604-617`, `:662`) exist so a
  future reader is not misled by the stale numbers. If the operator wants them
  *fixed* in the lesson files, that is a separate, explicitly authorised edit.
- Integrator-applied rows: the `AGENTS.md` retirement is already in filed bytes
  (no edit owed), but any round-34 record that needs the reissue as *live* prose
  (SCORECARD round-34 row; fleet report) must copy §2/§3/§9 rather than
  re-derive.

## Citations

- `reports/round-34/targets.json:57` (C03 mission/out), `:5-11` (shared rules);
  `reports/round-34/claims.json:54-65` (claim C before/after/thresholds)
- `reports/round-33/adj/A09-pins.md:36` (runner blob pin), `:55-65` (E1),
  `:67-75` (E2 digest tables), `:77-83` (E3 box-1), `:85-94` (E4 line anchors),
  `:96-101` (E5 README pins), `:105-114` (the R1–R8 deliverable list),
  `:120-126` (findings A09-F1..F5)
- `reports/round-33/calib/C14-fix-drafts.md:30-102` (Fix 1), `:103-181` (Fix 2),
  `:183-333` (Fix 3), `:335-408` (Fix 4), `:502-520` (application notes)
- `reports/round-33/op/O05-falsifier-disposition.md:78-118` (the `:713-715` → re-keyed replan), `reports/round-33/op/K01-falsifier-scout.md:136-141`
- `reports/round-33/adj/audit-assembled.md:29-30` (README/SKILL digest supersession, current readings)
- `reports/round-30/craft/box1-landed-survey.json:4-6` (old box-1 receipt); `reports/round-30/craft/box1-survey.py:5-13` (read-only, hardcoded `date` at `:8`)
- `reports/round-26/run-validation.py:96-97`; `reports/round-26/lessons/c51-revision-audit.py:48`
- `corpus/lessons/README.md:97`(old)→`:105`, `:207`(old)→`:254`, `:108`, `:242`, `:244`, `:245`, `:398-442`
- `corpus/lessons/round-31.md:46`; `corpus/lessons/round-32.md:7,33,41,55,57,58`; `corpus/lessons/round-25.md:44`; `corpus/lessons/round-19.md:88,100,101,179`; `corpus/lessons/round-15.md:25`; `corpus/lessons/round-14.md:141`
- `SKILL.md:31,47,77,130,149,157,183,189,205,208,214,243,262,278,294,323,354,375,456-458,468,479,481,483,486,488,491,501,522,534-536,575,660,662,687,710,713,726,729,730-732`
- `AGENTS.md` (40 lines, `5ae7a9c8…`); `git show 139e3b6:AGENTS.md:42`
- `SCORECARD.md:520`, `:588`, `:599`
- `reports/round-34/calib/C08-verify-reissue.md:5-15` (dependency state),
  `:56` (§3 ground truth), `:96` (acceptance checks A–F), `:135` (**C08-F1**),
  `:153-163` (its `## Owed`); `reports/round-34/calib/C01-survey-run.md` (survey
  stdout); `reports/round-34/calib/C02-receipt-json.md:57,416-417` (the
  hardcoded-`date` disposition)
- Era blobs compared in §9: `b02cfbc:SKILL.md` (305 lines, r14/r15 census),
  `16652e8:SKILL.md` (375 lines, r19; `corpus/lessons/round-19.md:179` names
  `e8d238a6…`), `fc13cd2:SKILL.md` (598 lines, r25); `17e90b9:SKILL.md` =
  pre-r33 revision for the r31/r32 rows (`git log --oneline -- SKILL.md`)
- Commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`;
  `git status --porcelain` → `?? reports/round-34/`;
  `sha256sum SKILL.md AGENTS.md corpus/lessons/README.md`;
  `git show 139e3b6:SKILL.md | wc -l` → 715 / `sha256sum` → `79fe91d3…`;
  `git show 139e3b6:AGENTS.md | grep -n "append one item"` → `42:### 2.2 …`;
  `git diff --numstat 139e3b6 HEAD -- SKILL.md AGENTS.md` → `35 18` / `0 2`;
  `git diff -U0 139e3b6 HEAD -- SKILL.md` (13 hunks);
  `git hash-object corpus/lessons/README.md` = `git rev-parse HEAD:corpus/lessons/README.md` → `73f3e1bd…`;
  `python3 -B .scratch/c03/map.py …` (difflib opcode table);
  `python3 -B .scratch/c03/check-anchors.py` → exit 0, `failures=0`;
  `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, 28/28, `f9bd07c2…`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0, findings 0;
  `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` → exit 1, 1 finding;
  `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` → exit 1, 28/37;
  `grep -rn "SKILL\.md:[0-9]"` (tree-wide, `tools/` → 0);
  `grep -rn "ec7469da"` → 95 hits/47 files; `grep -rn "79fe91d3"` → 127 hits/44 files;
  `grep -rn "f752e1d7"` → 20; `grep -rn "f9bd07c2"` → 107;
  `ls corpus/lessons/*.md | wc -l` → 33; `grep -vc README` → 32; `ls corpus/lessons/round-33.md` → absent;
  §9: `git show {b02cfbc,16652e8,fc13cd2}:SKILL.md` (305 / 375 / 598 lines);
  `grep -n "isolated legacy selftest battery" SKILL.md` → `617:`;
  `grep -n "A disappearing uncertainty marker" SKILL.md` → `564:`;
  `grep -n "uncertainty-inventory | probe" SKILL.md` → `614:`;
  `grep -n "^| name | kind | entry command" SKILL.md` → `604:,671:`;
  `grep -n "regex backslashes" SKILL.md` → `210:`;
  module-level slice compare `fc13cd2:SKILL.md[188:214]` vs `139e3b6:SKILL.md[188:214]` → equal
