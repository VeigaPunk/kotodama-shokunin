# ScribeReport — round 79 W1 (SHONEN four-box evidence, trend classification, Ca S884 disposition)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base: `44f76d456c1b326a71ffdb381590af825cbf11be`
(`round-78 verifier spot-check`). Scope: records/tool only. No claim was frozen, no counter was run, no
production file was edited. Draft/receipts live under `.ufo/waves/round-79/w1/stage/ScribeReport/`.

## 1. Verdict in brief

| item | observed | disposition |
|---|---|---|
| SHONEN four boxes | all four `[~]` at base (`SHONEN.md:5,7,9,11`); every named pointer resolves; 2 of the 4 boxes carry a caveat (below) | no box change; no `[x]`; report caveats only |
| S884 used-by token mismatch (Ca) | census receipt `reports/round-78/telemetry/census-end.txt:33` records `…amend-2026-10-24-r13.md`; registry at 4b255745 and 44f76d45 records `…amend-2026-10-23.md`; read-only probe: `mismatch=1` | the mismatch is real and reproducible |
| SCORECARD/SHONEN self-assessment naming that token | **none found** (see §4) | **no genuinely corresponding self-assessment mismatch → Ca rejected before freeze, as CLAIMS-DRAFT's pre-freeze clause provides**; the correction lands as unclaimed conformance repair |
| Trend verdicts for this round (records/tool only) | no LEARNING.md-class observable fires | expansion `unchanged`, quality `unchanged`, discernment `unchanged`; freshness paused (open L0 round-11); no numeric axis score |

## 2. SHONEN four-box evidence (base bytes, read-only)

Probe: `stage/ScribeReport/shonen-box-probe.sh` → raw output `stage/ScribeReport/raw/shonen-box-probe.txt`.

| box | pointer(s) | observed at base | verdict |
|---|---|---|---|
| 1 SKILL.md structure | `SKILL.md:20`, `:505`, `:564` | lines 20 `## Decision table`, 505 `## Error patterns`, 564 `## Checklist (executable where a tool exists)` | **verified** |
| 1 registry counts | census start/end `reports/round-75/telemetry/census-{start,end}.txt` | both receipts `exit=0`; neither receipt contains a row count (0 hits for 808/713/817/722). Counts recomputed from committed registry: `d7a38405` (round-74 landing) 808/713/58/37; `4f5e3b25` (round-75 landing) 817/722/58/37 | **verified by recomputation, not by the cited receipts.** Caveat: the box says "re-derived at census-end.txt"; that receipt only carries validate exit 0. Also the box labels 808 as the "round 75 Ca landing" count, while 808 is the round-75 *start* count (the 817 close count is the round-75 landing). Dated; base is now 820/725/58/37 after `cab52475` (round 76), which the box does not claim to describe. |
| 2 round-51 gap sweep | `reports/round-51/telemetry/final-measures.txt`; `LOG.md` round-51 | `1923bfe` (70 rows) → `2b956d7` (131 rows): **61 new rows**. Queued at `2b956d7`: S004 S005 S006 S009 S010 S011 S012 S014 S015 S017 S019 S020 S021 S022 S023 S024 S025 S026 S027 S044 S045 S046 S070 S081 S123 S124 S125 S127–S131; the new-row queued subset is exactly S081, S123–S125, S127–S131 (**9**), so "52 mined, 9 queued" holds | **verified** for counts and queued ids. **Caveat:** the cited final receipt ends with `MISSING_FROM_RECEIPT ['D', 'C']` (line 35; the QUALITY-9 two-way check it runs reports a miss). The box cites this receipt as the "final receipt" without disclosing that line. Historical; preserved. "build wave admitted 54" was not recomputed. |
| 3 round-50 instructions executable from committed bytes | SCORECARD round-50 counting commands; `1923bfe`, `4ad2683` | both commits exist; `SCORECARD.md:989–991` names clones of `1923bfe`/`4ad2683` and `acceptance_passed: true`, exit 0 | **partially verified**: pointer and commits exist; I did not re-run the round-50 command (not in my scope). "falsify seats worked from committed paths only" is not observed here. |
| 4 cross-domain bleed | `corpus/knowledge/linguistics/sign-languages-manual-modality.md` §15, §2; `.ufo/waves/round-51/build/ConnectSiblingSign.md` | line 224 (§15 "Scope") verbatim: "hands body-code etiquette, finger counting, word order and writing to their owners (§2). Handoff: lore-shokunin owns whether a signed language exists in-world…"; §2 owner table has 14 `file.md:NN` rows; `ConnectSiblingSign.md:17` "No sibling lane owns or partly owns any part of claim C's scope"; `:70` names the unowned WCAG 1.2.6 surface | **verified** for the quoted handoff and the 0-owner / one-unowned-surface statements. Individual §2 owner rows not re-checked. |

Wording note (not a mismatch with the evidence): every box says "no non-author verifier on record". Rounds 75–78 have hyaku "non-author integrator" closure spot-checks (`corpus/lessons/round-7{5,6,7,8}-verifier-spotcheck.md`). The round-78 spot-check states that none of the four boxes is mechanically checkable by a non-author from its evidence and that promotion remains operator-owned. The two statements are consistent only if "verifier" in the boxes means a promotion-gate verifier. The operator should decide whether to state that explicitly; I did not edit SHONEN.md.

Verifier-record inconsistency (not a lane self-assessment; routed, not Ca): `round-77-verifier-spotcheck.md` says "SHONEN heading has four `[ ]` box lines", and `round-78-verifier-spotcheck.md` step-1 table says "4 lines `[ ]`". SHONEN.md at `211f9526`, `0d9ff15f`, `9fa0615c`, `6f119326`, `4b255745` and base `44f76d45` all carry `[~]`. The round-78 spot-check's own SHONEN note says `[~]`, so its step-1 row contradicts its own note.

## 3. Ca — S884 census token (what is actually true)

Read-only probe `stage/ScribeReport/probe-used-by.py` (stdlib; `git show <rev>:<path>` only; no writes), run as:

    python3 -B .ufo/waves/round-79/w1/stage/ScribeReport/probe-used-by.py <lane> 44f76d456c1b326a71ffdb381590af825cbf11be reports/round-78/telemetry/census-end.txt

| receipt (at base) | tierC-mined lines compared | mismatch |
|---|---|---|
| `reports/round-78/telemetry/census-end.txt` (blob `62eb55b7`, added by `4b255745`) | S881, S882, S884, S893 | **1** (S884 receipt `…amend-2026-10-24-r13.md` vs registry `…amend-2026-10-23.md`) |
| `reports/round-78/telemetry/census-start.txt` | same | 0 |
| `reports/round-75/telemetry/census-end.txt` | same | 0 |

Registry S884 used-by cell: `…amend-2026-10-23.md` at `4b255745` and at `44f76d45` (base). `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` does not exist at base (only `…amend-2026-10-23.md` does).

Data for the unclaimed append-only correction (bytes only; the counter is not part of this seat):

- receipt: `reports/round-78/telemetry/census-end.txt`, line 33, sha256 `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` (copy: `stage/ScribeReport/raw/r78-census-end.base.txt`)
- measured revision: `44f76d456c1b326a71ffdb381590af825cbf11be` (and `4b255745…`, which introduced the receipt; registry token identical at both)
- old token (receipt): `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`
- actual token (registry): `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`
- the 24-r13 token names a file that never existed in this lane; the round-78 verifier (`round-78-verifier-spotcheck.md:67`, routed defect 2) already called the receipt irreproducible.

Probe limits (stated): it parses the `used-by` cell as the second-to-last populated cell and compares whole strings; it handles single-path cells only (true for S881–S893 here); it is not a frozen counter and not a claim leg.

## 4. Is there a genuinely corresponding SCORECARD/SHONEN self-assessment mismatch?

Searched committed base bytes of `SCORECARD.md`, `SHONEN.md`, `LOG.md`, `corpus/lessons/round-78.md` and `corpus/lessons/round-78-verifier-spotcheck.md`:

- `git grep 'S884'` / `'amend-2026-10-2[34]'` in SCORECARD and SHONEN: no cell records S884's used-by token. Hits are other rows: `SCORECARD.md:1521` (L76-07, S891 row, `amend-2026-10-23`→`amend-2026-10-23b`), `:1528–1530` (narrative-structure amend files), `:1402` (heritage-taxonomy-models amend-2026-10-24-r13), `:1480` (L75-09, S884 **evidence presence**, `reports/round-74/evidence/S884.txt`, not used-by).
- The `…amend-2026-10-24-r13` token appears only in `reports/round-78/telemetry/census-end.txt:33` and in the round-78 verifier's description of it (`round-78-verifier-spotcheck.md:67`).
- `corpus/lessons/round-78.md` cites `census-start.txt` and `census-end.txt` as the registry census receipts with no token claim.
- Round-78 SCORECARD section and LOG entry state "no source row changed" and "census exit 0" only. The receipt's exit code is 0 and it is accurate on that; the mismatch is in line content.

Conclusion: the mismatch lives in a receipt (an evidence record), and the only self-assessment prose about that round's census is exit-status prose, which is not contradicted. Per CLAIMS-DRAFT's "Pre-freeze scope disposition", Ca is **rejected before freeze**. Its correction lands as **unclaimed conformance repair** (append-only correction bound to the §3 data), not as a calibration claim and not as an O/S897 input.

## 5. Trend classification for this round (records/tool only)

Per QUALITY criterion 20, record/instrument repairs (receipt headers, pointer fixes, token corrections, a read-only probe/guard) are calibration work and never fire quality or discernment observables. No LEARNING.md-class observable fires: no entry is re-verified, deepened or superseded, and no gate decision is taken with an outside spot-check or a new lesson-grounded criterion. `LEARNING.md` is absent at base (checked).

- expansion: **unchanged** (no admitted or rejected entry; no registry row changed by this seat)
- quality: **unchanged**
- discernment: **unchanged**
- freshness: paused (open L0 round-11); no axis score or numeric score is produced here.

## 6. Commands run (all read-only against the lane; all observed output preserved)

| command | purpose | output |
|---|---|---|
| `git rev-parse --show-toplevel`; `git rev-parse --verify 44f76d…^{commit}` | host guard, base check | `raw/shonen-box-probe.txt` header |
| `sh stage/ScribeReport/shonen-box-probe.sh <lane>` (includes `git show`, `git grep`, `git cat-file -t`, `probe-used-by.py`) | SHONEN pointers, counts, round-51, round-50, §15, S884 probe | `raw/shonen-box-probe.txt` |
| `python3 -B stage/ScribeReport/probe-used-by.py <lane> 44f76d… reports/round-78/telemetry/census-end.txt` | S884 mismatch count | `raw/probe-census-end-r78.txt` (mismatch=1) |
| `git show <rev>:<path>` for receipts, SHONEN, S884 row | preserve copies | `raw/r78-census-end.base.txt`, `raw/r78-census-start.base.txt`, `raw/S884-registry-row.base.txt`, `raw/SHONEN.base.md`; `raw/sha256sums.txt` |

No build, lint, test, or counter was run. No `task`/delegation. No git/jj mutation anywhere (only `show`, `grep`, `ls-tree`/`cat-file`, `rev-parse`, `log`, `diff`-free reads). No tool installs; no pacman; no host-service change; `~/.local/bin` untouched. Scratch `/fast/scratch/hyaku/kotodama-r79/ScribeReport/` created for the first probe and removed after copying the receipts above.

## 7. Out of scope / not verified

- Not verified: round-51 "build wave admitted 54"; the individual §2 owner rows of the sign-language entry; the round-50 counting command output (only its pointer and commits).
- Not touched: SHONEN.md, SCORECARD.md, LOG.md, census receipts, the S884 row, any corpus or lesson file. Historical receipts preserved.
- Routed (not Ca): (a) S884 census-end correction, append-only, per §3; (b) SHONEN box-1 pointer caveat (counts not carried by the cited census receipts); (c) SHONEN box-2 "final receipt" disclosure of `MISSING_FROM_RECEIPT ['D','C']`; (d) verifier-record `[ ]` misstatements in round-77/78 spot-checks; (e) "non-author verifier" wording in the four boxes, operator decision.

## 8. Report trailer (paths relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`)

- Report: `.ufo/waves/round-79/w1/ScribeReport.md`
- Stage: `.ufo/waves/round-79/w1/stage/ScribeReport/` (`probe-used-by.py`, `shonen-box-probe.sh`, `raw/`)
- Base: `44f76d456c1b326a71ffdb381590af825cbf11be`
