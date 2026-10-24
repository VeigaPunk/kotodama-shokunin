# ExecCounterSmokeCa — smoke of reports/round-67/accept-ca.py at base clone + live tree

Seat: L1-kotodama-r67.ExecCounterSmokeCa (leaf, build+attack wave).
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (jj-colocated, relative paths below resolve here).
Counter under smoke: reports/round-67/accept-ca.py, sha256 (self-reported) `5e8915ac509cc60a13da65ae6251b499c3132a23cdfe865b9d46378744f36118` — identical to the frozen base dry-run header, i.e. the instrument is unchanged since freeze.
Lane revisions: HEAD == main == `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21` (round-67 declaration + instruments); base == `ad5b52b0ab5691358cd38718ab75649dc9916f9a`.

No lane writes and no git/jj writes were made. Scratch clones live in /tmp (see below). No tools installed or upgraded (nothing was needed).

## 1. Census leg — exact output at live tree (exit 1, as expected today)

Command (assignment text, verbatim):

```
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
  --file /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

Exit status: **1**. 51 finding lines: **27 W04 + 23 E12 + 1 E11**. Full E12/E11 output (tab-separated, first column is the census lane label):

```
file	E12	S776 row outside Registry section
file	E12	S779 row outside Registry section
file	E12	S780 row outside Registry section
file	E12	S781 row outside Registry section
file	E12	S782 row outside Registry section
file	E12	S783 row outside Registry section
file	E12	S784 row outside Registry section
file	E12	S785 row outside Registry section
file	E12	S786 row outside Registry section
file	E12	S787 row outside Registry section
file	E12	S788 row outside Registry section
file	E12	S789 row outside Registry section
file	E12	S790 row outside Registry section
file	E12	S791 row outside Registry section
file	E12	S792 row outside Registry section
file	E12	S793 row outside Registry section
file	E12	S794 row outside Registry section
file	E12	S795 row outside Registry section
file	E12	S796 row outside Registry section
file	E12	S797 row outside Registry section
file	E12	S798 row outside Registry section
file	E12	S799 row outside Registry section
file	E12	S800 row outside Registry section
file	E11	S753 missing used-by -
```

This matches the claim's "E12 x23, E11 x1 gone" exactly: E12 = S776 + S779..S800 (the R66_ROWS set), E11 = S753.

Grounding (scripts/sources-census.sh): E12 is emitted by row_pass for table rows outside `## Registry`; E11 by `usedby_findings`, which scans only `## Registry` rows with status `mined`, splits used-by on commas, and flags any non-empty cell != `—` whose path does not exist under the lane dir. S753 is `mined`, used-by cell is the ASCII hyphen `-` (verified: `awk -F'|'` on line 709 gives cell[11] = `-`; full row is 11 cells), and `./-` does not exist -> E11. Repair to `—` clears E11.

Census label variance (cosmetic, but affects receipt diffing): `--file` mode hardcodes the lane label string to `file` (`sources-census.sh`: `TSV="file	$file_abs	$dir_abs	"`), while the pre-data control reports/round-67/telemetry/census-start.txt was produced with `validate --root ... kotodama` and therefore carries `kotodama`. Verified with `diff <(cut -f2- live) <(cut -f2- census-start)`: **DATA_IDENTICAL_MODULO_LANE_LABEL** (27 W04 / 23 E12 / 1 E11 both). So the D2 census evidence cannot be byte-diffed against the control; it must be compared after field 1.

## 2. Base-clone smoke (materialized clone at ad5b52b, clean)

```
git clone -q --no-local --single-branch --branch main <lane> /tmp/r67-ca-base
git -C /tmp/r67-ca-base switch -q -C main ad5b52b0ab5691358cd38718ab75649dc9916f9a
# rev-parse main == ad5b52b0…, `status --porcelain` empty, reports/round-67 absent
python3 -B reports/round-67/accept-ca.py --root /tmp/r67-ca-base \
        --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a
```

Result: exit 1, and **byte-identical to the committed control** reports/round-67/telemetry/dry-run-ca.txt (`diff` reports no differences). The frozen base dry-run is therefore reproducible; the base control is honest.

Leg outcomes at base:

| leg | base | detail (verbatim, long D2 list elided as in the receipt) | correct reason? |
|---|---|---|---|
| STAMP | PASS | stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 | yes (clone main == --lands) |
| D1 | FAIL | `bad=['manifest_absent']` | yes — reports/round-67/dispositions/ does not exist at base |
| D2 | FAIL | `census_exit=1 E=[…S776/S779/S780/S781…]`, `S776..S800:outside_registry` (23), `E_lines=24` | yes |
| D3 | FAIL | `log:no_round66_heading`, `log:no_round66_mentions`, `scorecard:no_axes66`, `no_coverage`, `no_operability`, `no_calibration` | yes |
| D4 | FAIL | `nonunique=['S801','S802','S803','S804'] opened_today=0` | leg correct, **label misleading** (F2) |
| SEQ | FAIL | 6 items shown: accept-c/accept-o × (no_required_lands, no_headers, no_equality_assert) | leg correct at base, **detail truncated/mislabeled** (F3) |
| CRITERION | FAIL | QUALITY criterion 19 names receipt sequencing | yes |
| QUOTES | FAIL | `exit=2 gate_ids=0 clean=True` | leg correct, `clean=True` is a **latent false-clean text** (F4) |

Base D2's census sub-run yields the same 24 E lines as the live tree (23 E12 + 1 E11); the base registry placement defect is the round-66 state the claim must repair.

## 3. Live-tree smoke (lane worktree, main == lands == b78f8b8)

```
python3 -B reports/round-67/accept-ca.py --root . --lands b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21
```

Exit 1. `STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e`; **SEQ PASS bad=[]** (live tools/check-receipt-seq.py `--selftest` prints `SELFTEST: 14/14`, rc 0); D1/D2/D3/D4/CRITERION/QUOTES FAIL with the same pre-data details as at base. This is the expected pre-data shape: exactly the build work the Ca claim names is missing (manifest, registry repair, LOG/SCORECARD round-66 restoration, S801–S804 + 2 new rejects, criterion 19, lesson).

No crash at either site: no `COUNTER_FAULT`, no traceback, no exit 2. Guard checks: `--lands deadbeef` -> `STAMP FAIL --lands is not a full commit hash`, exit 2 (correct); `--root /tmp/r67-notrepo --lands <40hex>` -> `STAMP FAIL stamped=ad5b52b0 evaluated= equal=False tree=`, exit 1 (correct, no crash).

## 4. Wrong-reason audit

**No leg fails for the crash/wrong-path class at base**: every failing leg reads the path it names, resolves under `--root`, and states a condition actually true of the base bytes. The census leg really does execute (exit 1 with 24 E lines captured) rather than silently passing on an unreadable file. The following defects are real but are diagnostic or latch defects, not base-leg misclassifications:

- **F1 (inert sub-check — substantive).** D2's documented `S753 used-by is '—'` requirement is unenforceable as written. Code: `m753 = re.search(r"(?m)^\|\s*S753\s*\|", reg)` then `c753 = [... for x in m753.group(0).split("|")[1:-1]]`. The regex match is only the prefix `| S753 |`; splitting it yields `['S753']`, length 1, so `if len(c753) == 11` can never be true. Demonstrated in isolation against the live registry: `cells parsed from match: ['S753'] len: 1 -> len==11 gate: False` (full-line parse gives 11 cells, used-by `'-'`). Since `m753` is truthy, the `S753:absent` branch never fires either. Consequence: if a scribe "repairs" S753's used-by to an existing but non-`—` path, census E11 stays silent and D2 PASSes while contradicting the docstring's stated requirement. Today only census E11 enforces the em dash, so this is not a base-leg wrong reason — it is a false-PASS window at lands time. Fix: parse the whole line (`reg[m753.start():reg.index("\n", m753.start())]`).
- **F2 (mislabel).** D4's `once` set is built with `!= 1`, so **absent** ids are reported as `nonunique=[...]`. At base and live, S801–S804 have 0 rows each (`rows: 0` verified), yet the detail says "nonunique". Leg outcome is correct; the diagnostic conflates absent with duplicated and would send an integrator hunting duplicates. Suggest `absent=[...]` / `duplicated=[...]` split.
- **F3 (truncation + indistinguishable diagnostics).** SEQ detail is `bad=seq_bad[:6]`; at base `len(seq_bad) == 10` and the six hidden items are all three accept-ca items plus `tool_selftest=2` (python cannot open the missing tools/check-receipt-seq.py; rc 2, not a crash). Verified by replaying the leg's exact scan against the base clone: `n_bad= 10 hidden_beyond_6= ['reports/round-67/accept-ca.py:no_required_lands', '…:no_headers', '…:no_equality_assert', 'tool_selftest=2']`. Separately, a **missing** counter file produces the same strings as a present-but-noncompliant counter, so absence is invisible as a distinct cause.
- **F4 (latent false-clean).** `tools/check-gate-quotes.py corpus/lessons/round-67.md` on the missing lesson prints `GATE_QUOTES_ERROR: corpus/lessons/round-67.md: unreadable: No such file or directory` **and** `GATE_QUOTES: 0 findings`, exit 2. Ca's QUOTES detail consequently prints `clean=True` on unusable input. `quotes_ok` requires rc==0, so no false PASS here, but any counter that keys on the `0 finding` text alone would false-PASS. The detail field should derive `clean` from rc.
- **F5 (demonstrated STAMP bypass — moved/dirty worktree).** STAMP binds `git rev-parse main` to `--lands` and prints `rev-parse <lands>^{tree}`, but never checks the worktree is clean nor that the bytes being measured equal that tree. Demonstrated without touching the lane: clone at b78f8b8 (`/tmp/r67-ca-dirty`), append one fabricated line to corpus/QUALITY.md (` M corpus/QUALITY.md`, uncommitted), run the counter -> `STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e` and `CRITERION PASS QUALITY criterion 19 names receipt sequencing` on bytes that exist in no commit. So a moved or dirty worktree can turn a Ca leg green with zero committed work; the "materialized clone at the lands commit" discipline is process-only, not enforced by the counter. Fix: add `git status --porcelain` empty (or `git diff --quiet HEAD`) to the STAMP leg, or read leg inputs from `git show <lands>:<path>` / `git archive` instead of the working tree.
- **F6 (predicate/intent gap — risk, not a current failure).** D4 requires `rej_opened_today >= len(R66_REJECTS) + 2` == 6 rejected rows opened 2026-10-24, i.e. S801–S804 themselves must carry `opened=2026-10-24`. The claim only says "S801–S804 + >=2 new first-class rejected rows". If the scribe restores S801–S804 with an older opened date, D4 can never pass even though the claim text is met. The leg also computes `new_rejects` and never uses it — the intended "new rather than total" semantics were dropped, leaving the dead-code hint that the condition was meant to be `rej_opened_today - existing >= 2`.

## 5. Verdict for the L1

- Frozen base control is **reproducible**: base-clone run at rev0 (sha `5e8915ac…`) is byte-identical to dry-run-ca.txt, exit 1; at rev1 (`5382ffed…`, QUOTES capture-group fix) it differs in the self-sha header line only — see §6.
- Live tree pre-data: STAMP + SEQ PASS; D1, D2, D3, D4, CRITERION, QUOTES FAIL for the correct pre-data reasons.
- Census leg is live and correct: exit 1 with 23 E12 + 1 E11, data identical to census-start.txt modulo the `file`/`kotodama` label.
- **Do not treat D2's S753 clause or D4's "opened today" count as evidence of what they say** (F1 inert; F6 off-claim), and **add a clean-tree check to STAMP (F5)** before any lands-time PASS is believed — as frozen, a dirty clone passes STAMP and can flip legs on uncommitted bytes.

Risks/blockers: none blocking this smoke. Scratch clones under /tmp only; lane left untouched (no writes outside this report). No dependency on other seats was required.

## 6. Addendum — counter revision rev1, D1 progress, C-APPEND vs Ca-D4 resolution

**Counter moved under me (declared).** The L1 applied the QUOTES capture-group fix; accept-ca.py is now sha256 `5382ffed6f6cbbec4d62bebd5131d2e1bb2d5b6ff621de32dec916010543653c` (was `5e8915ac…`, the sha pinned in dry-run-ca.txt), with `gate_ids` regex now `r"\b(S8[0-2]\d)\b"`. Re-smoked both sites against rev1:

- Base clone `/tmp/r67-ca-base --lands ad5b52b…`: exit 1, and `diff` vs committed dry-run-ca.txt shows **exactly one differing line — the self-sha header**. All eight leg outcomes and details are byte-identical. So the frozen base control remains valid modulo the declared revision line; reviewers should expect the header sha mismatch and nothing else.
- Live tree `--land b78f8b8e…`: exit 1, `STAMP PASS`, `SEQ PASS`, D2/D3/D4/CRITERION/QUOTES unchanged from §3. **D1 changed shape**: reports/round-67/dispositions/r66-wave-evidence-manifest.txt now exists in the worktree (194 INCLUDE lines, 63 seat reports) and D1 fails with `bad=["untracked=['.ufo/waves/round-66/gen-spec.py', '.ufo/waves/round-66/rows/ScoutGapScent/gap.md', …']"]` — i.e. manifest present, but its INCLUDE paths are untracked at b78f8b8 (the r66 wave tree is still untracked). Correct reason; the build seat must commit those paths at A_ca.

**C-APPEND vs Ca-D4: mechanics confirmed, sequencing makes it satisfiable.** Verified in accept-c.py: `allowed_new = set(NEW_IDS) | EXTRA_IDS` with `NEW_IDS = S805..S828`, `EXTRA_IDS = {S801..S804}`, `extra_ids = [sid for sid in appended_ids if sid not in allowed_new]`; and the mutable-cell rule only permits status/recheck/used-by changes on existing rows (`oc[:7] == nc[:7] and oc[8] == nc[8]`), so an existing row **cannot be re-dated** into D4's `opened == 2026-10-24` count. Combined with Ca's D4 needing 6 today-dated rejects, no registry state with both instruments evaluated at one commit exists: at a shared commit, either fewer than 6 rejects or `APPEND extra=[S829…]`.

The L1 resolution (per-claim lands: A_r carries S801-S804 + r66 dispositions → A_c (claim C receipt; only S805-S828 appended over base) → A_ca (Ca receipt; S829+ reject rows + lesson)) is consistent with the code: at A_c, appended ids ⊆ `NEW_IDS ∪ EXTRA_IDS` satisfies APPEND, and Ca's D4 is not evaluated there; at A_ca, D4 sees S801-S804 (from A_r, all `opened=2026-10-24`) plus ≥2 S829+ rejects, and accept-c.py is not run there.

Residual hazards for the L1 to police (recorded as design finding, not a blocker):
1. **C's receipt must be taken at A_c and never re-derived at A_ca** — a post-lands rerun of accept-c.py at A_ca will print `APPEND FAIL extra=['S829',…]` by construction. That FAIL is sequencing, not regression; pin the C receipt's `--lands` to A_c.
2. **D4's 6-reject count still requires S801–S804 themselves to carry `opened=2026-10-24`** (my F6): if A_r dates them otherwise, Ca cannot pass at A_ca regardless of the S829+ rows. `new_rejects` in the D4 leg remains computed-and-unused.
3. **S829+ rejects stay invisible to the census E11 check** (`usedby_findings` filters `status == mined`), so D2's census leg stays green at A_ca; census only adds W02 warnings for thin teaches. D2 therefore does not constrain the new reject rows — D4's own `REJECTED:`/`flip:` check is the sole gate.
4. F1 (inert S753 sub-check) and F5 (STAMP accepts a dirty worktree) remain live counter defects; neither is addressed by the sequencing resolution, and F5 can still flip legs on uncommitted bytes at A_ca.
