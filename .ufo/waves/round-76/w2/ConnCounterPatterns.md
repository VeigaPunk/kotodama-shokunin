# ConnCounterPatterns — round 76, wave 2 (connector, read-only)

Scope: cross-axis connection of (a) claim C ROWS leg (registry row-only diff) and (b) claim Ca COMBINED leg (README ownership of the culture-material heading). Read-only. Evidence is the committed blobs at the frozen configuration commit `df0f0309d61e5485bb17035d3f8791b1e6a11d40` (C/Ca freeze), the C landing `722e69f...` and the Ca landing `a43ed80...`. The lane worktree was not used as evidence. No builds, tests, counters or selftests were run; the counters were read as code from `git show df0f030:reports/round-76/accept-{c,ca}.py`.

Tooling: none installed or updated. Scratch under `/fast/scratch/hyaku/kotodama-r76/ConnCounterPatterns` was used for extracted blobs and removed before yield.

## Verdict

1. **C ROWS: claim failed as declared, not an over-read by the counter.** The committed registry carries two non-row, non-blank lines outside the `## Registry` table. The frozen ROWS wording says the registry diff "adds exactly S894-S896 (817 -> 820)". The counter's R1 applies that literally. The two lines were introduced by `cab5247` (`round-76: correct base ground and mirror receipts`), which precedes the freeze, so the freeze itself already contains them. The lesson's R76-M3 framing ("valid registry table plus study-path/search-log appends ... under the exact line-diff implementation") is inaccurate as a counter-error claim, and its routed-to-77 sentence attributes a showGb mismatch to ROWS that belongs to COLLCHECK.

2. **Ca COMBINED: the README failure is a schema-key mismatch between two frozen claims, not a landing defect.** Claim C's frozen `owned_inplace` entry carries `path`, `base_text`, `after_text` and no line key. The Ca counter's consumer requires an integer `base_line`. The result is a red COMBINED leg at any tree where the README heading edit is present, while the same heading edit is correct: base line 410 is `## culture-material/ (40)` and line 410 at the landing is `## culture-material/ (41)`.

3. **Shared pattern:** both defects are shape-keyed predicates over a shared surface, with ownership declared somewhere the consuming predicate does not read. ROWS keys ownership on the `ROW_RE` line shape and nothing else; the non-row sections have no declared owner. COMBINED keys C's README ownership on an integer `base_line` that C never declares. The README heading is additionally described as owned by Ca in three comments and by C in the claim. The self-tests cover neither failure path.

4. **Minimum next-round boundary (proposal only; no claim edits this round):** one frozen ownership manifest per shared file, keyed by region (section heading, or line number plus exact text), with exactly one owner claim id and allowed change kinds. Both counters read it from the freeze blob. Concretely: declare `## Paths`, `## Search log` and `## Leads (unopened)` either in-scope or out-of-scope for claim C, by heading and not by line shape; key `owned_inplace` by the same region key the consumer reads; add fixtures for a planted non-row prose line, for a README heading edit with a matching owned entry, and for a README heading edit without one.

## Evidence

### A. C ROWS

- Frozen predicate: `git show df0f030:reports/round-76/claims.json`, line 156 (ROWS wording: "the registry diff base..<lands> adds exactly S894-S896 (817 -> 820) ... none removed; ... pre-existing rows are byte-identical"). Claim C has no row-only qualifier and no declared non-row region.
- Counter R1: `df0f030:reports/round-76/accept-c.py` lines 1529–1533 (R1 text), 1584–1605 (line-multiset diff; any non-blank added line that does not match `ROW_RE` is "registry line added outside the frozen row_set"). `ROW_RE` is at line 258 (`^ {0,3}\|\s*(S\d{3,})\s*\|`). Lines 1544–1551 (R5, used-by both ways).
- Landed non-row content, `df0f030:corpus/SOURCES.md`:
  - line 853 `## Paths`, line 854 `- calendar-standard design — S896 → S895 → S894: ...` (the bullet is not a row; the same convention is used by the existing Paths bullets at base);
  - line 890 `## Search log`, line 902 `**State-standard calendar compilation (round 76).** Question: ...` (non-row paragraph).
  - rows S894–S896 are at lines 849–851; line 852 is blank.
  - Introduced by `git log base..df0f030 -- corpus/SOURCES.md` → `cab5247` only (`+8` lines: 3 rows, 3 blank, one bullet, one paragraph).
- Precedent: among the 25 most recent commits touching `corpus/SOURCES.md` (rounds 61–76), `git log -n 25 -- corpus/SOURCES.md` filtered for added non-blank, non-row lines prints output only for `cab5247`; every other landing added row lines (and blanks) only. Round 75 `4f5e3b2` adds S885–S893 and nothing else (`git diff 5d01674 4f5e3b2 -- corpus/SOURCES.md`). Round-72 `868107e` is the E12 fix that moved rows into the Registry section, which shows the lane treats non-Registry lines in that position as defects. The census accepts the prose (`reports/round-76/telemetry/census-end.txt` at `722e69f`, lines 1–35: no E-code; exit 0), so the census and the C counter disagree on this point; the frozen predicate is what governs.
- Controls evidence: `reports/round-76/telemetry/controls-c.txt` at `722e69f`, lines 28–31. The ROWS detail names the prose line first ("registry line added outside the frozen row_set: '- calendar-standard design — S896 → S895 → S894: start with '" and "**State-standard calendar compilation (round 76).** Question"), then the expected do-nothing causes (entry missing, orphan used-by). The prose-line failure is independent of data landing: it is computed from freeze-plus-landing bytes and would persist at any `lands` that keeps lines 854 and 902.
- Decomposition: `722e69f` diff against base adds the same 8 lines as the freeze (`git diff --stat 98c486b 722e69f -- corpus/SOURCES.md` = 8 insertions), so the prose lines persist at the C landing.
- Self-test gap: the ROWS mutant list (`accept-c.py` 5894–5908) contains only row-shaped mutants (`row_extra` appends a row `| S821 |`, line 5697–5699). No mutant appends a non-row, non-blank line, so the branch at 1598–1605 is unexercised. `selftest-c.txt` at `722e69f` reports `SELFTEST: 89/89`.
- Missing receipt: `reports/round-76/telemetry/` at `722e69f` contains `accept-ca-75-at-lands.txt`, `census-end.txt`, `census-start.txt`, `controls-c.txt`, `controls-ca.txt`, `gap-sweep.txt`, `selftest-c.txt`, `selftest-ca.txt`. No `measures-c.txt` or `measures-ca.txt` exists at the lands. The "final C counter receipt" the lesson cites (`corpus/lessons/round-76.md:89`) is therefore not committed; the only committed C ROWS red is the freeze-level do-nothing control.

### B. Ca COMBINED (README ownership)

- Claim C's frozen declaration: `df0f030:reports/round-76/claims.json` lines 170–176: `owned_inplace = [{path: "corpus/README.md", base_text: "## culture-material/ (40)", after_text: "## culture-material/ (41)"}]`. No `base_line` key.
- Ca consumer: `df0f030:reports/round-76/accept-ca.py` line 814–817 (loads `owned_inplace` into `claim_c_owned_inplace`), lines 1914–1926 (reads `item.get("base_line")` at 1916; if not an int in range, appends "claim-C owned-inplace line has invalid line number" at 1925 and `continue`s), lines 1959–1968 (`allowed = repair_lines ∪ c_exempt_lines`; a removed base line outside `allowed` fails APPENDONLY).
- Trigger: `c_exempt_lines` is only populated when `cfg["combined_exemptions"]` is set, which happens only in `leg_combined` (line 2570). The README is unchanged between base and freeze (no README commit in `base..df0f030`), so the problem appears only at a combined tree. This matches the committed control: `controls-ca.txt` at `722e69f`, line 58 (`LEG FAIL COMBINED`) with the detail `claim-C owned-inplace line has invalid line number: {'path': 'corpus/README.md', 'base_text': '## culture-material/ (40)', 'after_text': '## culture-material/ (41)'}` (line 59 of the file, same run).
- Line evidence: `git show 98c486b:corpus/README.md` line 410 = `## culture-material/ (40)`; `git show 722e69f:corpus/README.md` line 410 = `## culture-material/ (41)`; hunk at `@@ -409,3 +409,3 @@` in `git diff 98c486b 722e69f -- corpus/README.md` (commit `788bd56`).
- Inference (not executed): with `base_line: 410` supplied, the check at 1927–1931 passes for this edit and the README edit becomes an exempt line at 1932 and 1959. I did not run this; the remaining COMBINED sub-checks would need a real combined tree.

### C. Ownership declared four ways

1. `claims.json` `owned_inplace` (line 170–176) → owner: claim C. Claim C INDEX wording (line 164) requires "the heading count is 41", which is the C-owned edit.
2. `accept-c.py` H4 docstring lines 74–77 ("heading lines whose only change is the partition-count parenthetical belong to claim Ca's repairs and are EXEMPT"), D6 comment 594–596, A3 comment 631–633 ("belong to claim Ca's pairs") → owner: Ca. These comments describe round-75 ownership.
3. `accept-c.py` INDEX code, lines 4580–4582: any base partition heading whose parenthetical changes is skipped (`i += 1`) if the partition exists at lands. `leg_index` (from 4393) does not read `owned_inplace` at all. Ownership is therefore pattern-based, not owner-based.
4. Claim Ca at round 76 (`claims.json` lines 186–202): `fixed_surfaces: []`; the only REPAIR is `SKILL.md:707` (`controls-ca.txt` at `722e69f`, `repair-stated_at={'SKILL.md': [707]}`). The README partition-count repairs the C docstring (line 4316) expects from Ca do not exist in round 76. The stale ownership is therefore a comment defect in a frozen counter, not a claim statement.
- Stale citation: `accept-ca.py` line 170 says `corpus/README.md:805` quotes `## culture-material/ (36)`. At base the quote is line 810 (`git show 98c486b:corpus/README.md | grep -n -F '(36)'` → 810).

### D. Selftest coverage of the shared surface

- `accept-ca.py` fixtures (`_build` from 3086, `_claims_legs` from 2977): no fixture carries `owned_inplace`, and no fixture edits a README heading. Only README fixture text is the base at 2880. The COMBINED scenarios (`combined-missing-entry`, line 3643–3648) test a removed C entry, not the owned-line path.
- Consequence: the selftest that gates Ca could pass while the real frozen claim is red at combined. The fixture and the real config diverge at the one key that matters.

### E. Third instance (COLLCHECK), same class

- `map` record `S938` → `S895` (`df0f030:.ufo/waves/round-76/assimilation/id-renumber-map.json` line 603) names `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=...`; row `S895` names `.../newGbInfo?hcno=...`. The counter's `norm_url` (`accept-c.py` 299) compares netloc and path, so `showGb` and `newGbInfo` differ. The `showGb` → `newGbInfo` 302 alias is not modelled. This is the same pattern: a legitimate alternate representation is not declared as an equivalence in the frozen artifact. The lesson's sentence at line 89 places this mismatch under ROWS; the controls show it under COLLCHECK (`controls-c.txt` line 48–49).

## Frontier summary

- Axis 1, attribution correctness: ROWS red is a landing-scope breach (cab5247), correctly reported by the frozen literal predicate; COMBINED red is a claim-schema key mismatch. Both are frozen-claim/counter defects, not landing defects for the Ca one.
- Axis 2, ownership consistency: four statements of the README heading owner disagree (Section C above).
- Axis 3, test coverage: neither failure class has a fixture or mutant (Section D; `accept-c.py` 5894–5908).
- Axis 4, citation accuracy: lesson R76-M3 and line 89; `accept-ca.py` line 170 (`:805` vs `:810`); `accept-c.py` H4/D6/A3 comments.

No claim edits are proposed for this round.

## Verification

- Commits resolved in the lane repo (`98c486b`, `df0f030`, `a43ed80`, `722e69f`), not the source repo (the source repo does not contain them).
- Files read at committed revisions via `git show`. No counter, selftest, build or linter was run.
- Inferences are marked in place.
