# R10-C26 — auditor: filler check on the ten round-10 coverage entries (NON-CANON)

- seat: R10-C26 auditor (filler check). lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *filler check — read all new entries; any entry that names no gap, has no
  decision-record section, or whose source does not resolve is a rejection candidate*;
  deliverable `reports/round-10/coverage/audit-filler.md`.
- date: 2026-10-17 (local clock UTC-03:00). audit window opened 18:26 (poll start) and
  closed with a frozen snapshot at **2026-10-17T21:46:32Z**; the last write to
  `corpus/knowledge/` was `transport-mobility-lexicon.md` at 18:44:03 local (checked:
  `find corpus/knowledge -newermt '2026-10-17 18:44:04'` → empty). An earlier freeze at
  21:43:02Z caught that entry pre-revision; it was re-audited on the revised bytes and
  the verdict is unchanged (§3.1).
- revision binding: declared round-10 baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749`;
  worktree HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f`; tracked corpus tree unchanged
  (`git diff --stat HEAD -- corpus/knowledge` empty; all ten new entries are untracked files).
- role limits: this seat audits and reports. Its only write is this file (plus `.scratch/`
  scratch). It edits no corpus entry, admits no claim, and dispositions no candidate —
  the rejection-candidate list below is routed to the parent for that.
- criteria applied (per the R10-C26 assignment and `reports/round-10/claims.json` C):
  1. **names the gap it fills** (no filler); 2. **at least one decision-record section**;
  3. **sources resolve** (cited repo paths exist; cited commands re-run; URLs get a
  documented access attempt; round-8/9 receipts cited by path count as sources).
- instruments: `.scratch/r10c26-audit.py` (independent field/heading/path/URL census);
  a verbatim replication of the acceptance runner's gap/decision regexes
  (`reports/round-10/run-validation.py:316-332`) applied independently; command re-runs;
  `sha256sum` digest recomputation; bounded `curl` URL sweep. The runner's own latest
  verdict (`reports/round-10/validation.json`, run 18:39:22) is used only as a
  cross-check, never as my evidence.

## 1. Snapshot — the ten new entries, frozen 2026-10-17T21:46:32Z

Baseline: 179 entries (tracked, `git ls-tree -r HEAD --name-only corpus/knowledge` → 179).
Live count at freeze: **189** (`git status --short corpus/knowledge` → 10 untracked `.md`;
`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` ran,
exit 0). Ten new entries, all with complete `topic`/`sources`/`couples`/`verified-at`/
`recheck` header blocks:

| # | entry (under `corpus/knowledge/`) | sha256 (full) | mtime | bytes |
|---|---|---|---|---|
| 1 | `culture-material/transport-mobility-lexicon.md` | `d0a2c836a838c0a6b5830d8413610687d993d08b0df92244b7a9304c077dd8ab` | 18:44:03 | 39375 |
| 2 | `culture-material/vessel-container-lexicon.md` | `073e7fc54b600a81a75e0db480f73597e2295f8daa317a74e9246846b5de2df3` | 18:36:51 | 43056 |
| 3 | `linguistics/language-shift-obsolescence-revival.md` | `89d2a225dd709a7947c4f9d967ffd6ce858f784bfef10f581b11a863dc6c8315` | 18:38:48 | 39676 |
| 4 | `linguistics/numerals-and-measures.md` | `57fc76695c9fed38cf87ddccbaf7e5c5d322125f65b98aea154baf5046129340` | 18:33:06 | 34831 |
| 5 | `linguistics/sound-symbolism.md` | `4f14b05a7df542ad5e3dca39c20cb02dc3f5745c70395418770da93794fddd5d` | 18:38:07 | 28980 |
| 6 | `myth-symbol/direction-symbolism.md` | `5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426` | 18:36:19 | 39499 |
| 7 | `myth-symbol/divination-omen-systems.md` | `6666e7dbd5cc5a4bd9833b3e842843854af8ef7b365396c6d1737aac8cbf2ba4` | 18:41:20 | 48358 |
| 8 | `myth-symbol/plant-symbolism.md` | `a9fd5e8fc2b005293569b9bd7225a4a42002183458aa7e36ece147793623d63f` | 18:38:19 | 42589 |
| 9 | `verification/header-conformance-readings.md` | `d627eba3b99f56933b6eae2ab1339013be57da30a5e5608b4d75ddb7f36feb90` | 18:31:46 | 21829 |
| 10 | `verification/verification-independence-anti-circularity.md` | `743bce544c888a9159728af4b6f5dcecb98166adc3a77d30e7794b5d711d0cff` | 18:33:47 | 31956 |

Partition minimums met: linguistics 3 ≥ 2, myth-symbol 3 ≥ 2, culture-material 2 ≥ 2,
verification 2 ≥ 2; total 10 ≥ 10. No slug collision with any of the 179 baseline files
(`comm -12` of new vs baseline basenames → empty).

## 2. Verdicts

**8 of 10 clear on all three criteria. Two rejection candidates: #1 (substantive — gap
not named) and #8 (mechanical only — gap named in prose, unrecognized by the acceptance
runner's regex).** No entry fails the decision-record criterion and no entry fails source
resolution at the freeze.

| # | entry | gap named | decision record | sources resolve | verdict |
|---|---|---|---|---|---|
| 1 | transport-mobility-lexicon | **NO** | yes (§8 table, §10 DR-TR-01..07) | yes | **REJECTION CANDIDATE (gap)** |
| 2 | vessel-container-lexicon | yes (§1 L9) | yes (§10) | yes | pass |
| 3 | language-shift-obsolescence-revival | yes (frontmatter L4 `- gap filled:`) | yes (§8) | yes | pass |
| 4 | numerals-and-measures | yes (§0 L29) | yes (§9, §12) | yes | pass |
| 5 | sound-symbolism | yes (§1 L21 + L23) | yes (§9) | yes | pass |
| 6 | direction-symbolism | yes (§13 L196) | yes (§13) | yes | pass |
| 7 | divination-omen-systems | yes (§1 L30) | yes (§10) | yes | pass |
| 8 | plant-symbolism | yes (topic L3; body L12 "**The gap statement.**") | yes (§11) | yes | **CANDIDATE (mechanical)** |
| 9 | header-conformance-readings | yes (§1 L9) | yes (§9 DR-1..5) | yes | pass |
| 10 | verification-independence-anti-circularity | yes (topic L3 "Gap filled:"; L44) | yes (§6, §8) | yes | pass |

Cross-check: the acceptance runner's run at 18:39:22 (`validation.json`) lists exactly
two gap failures — #1 and #8 — i.e. it agrees on #1 and disagrees with my merits reading
on #8 (see §3.2). Independent replication of its regexes on the frozen bytes reproduces
both: `GAP-FAIL DEC-OK` for #1 and #8; `GAP-OK DEC-OK` for the other eight.

## 3. Candidates in detail

### 3.1 #1 `culture-material/transport-mobility-lexicon.md` — gap not named (substantive)

- `grep -n -i "gap" <entry>` → **0 hits** (command, 18:33, 18:43Z, and again 18:46Z on the
  revised bytes). No "Gap filled:" clause, no gap heading, no gap frontmatter field; the
  runner's gap regexes both fail on the frozen bytes (replication above). The entry was
  revised once during the window (`36a7370f…` 18:32:36 → `d0a2c836…` 18:44:03, −8 bytes)
  and the revision did **not** add a gap statement — re-verified after the revision.
- Nearest statement, quoted in full from `sources` L18: "In-corpus retrievable
  cross-references: `corpus/knowledge/culture-material/material-culture-inference-method.md:67`
  (the single pre-existing transport row — 'state logistics; military reach' — which this
  entry expands into its own partition file)". The pre-existing row was verified at
  `material-culture-inference-method.md:67` (command: `sed -n '67p'` → the transport row,
  Trigger 2003). So the entry *describes* what it expands, but it never names the gap it
  fills, and its one-line mention sits inside the source list rather than as a claim.
- Everything else about the entry is strong: §10 decision record with seven dispositioned
  rows (DR-TR-01..07), calibration shelf §9, 14 cited Wikipedia URLs (8 spot-checked,
  all HTTP 200), all in-repo paths resolve.
- Route: rejection candidate per the assignment's letter. Cheapest repair is a one-line
  gap clause (e.g. in `topic` or a `## 0` section) naming the partition gap — but the
  repair is the parent's/author's call, not this seat's.

### 3.2 #8 `myth-symbol/plant-symbolism.md` — mechanical candidate only (merits pass)

- The entry **does name its gap**, twice, in prose: topic L3 — "the gap this entry fills,
  since the partition covers fauna (`animal-symbolism.md`) but has no flora file"; body
  L12 — "**The gap statement.** This partition covers fauna in depth … but no file covers
  plants."
- The acceptance runner's gap regex accepts only (a) a `gap …:` clause with
  filled/addressed/served or a bare colon, or (b) a heading containing "gap". This entry
  uses neither form (the bold block is a paragraph, not a heading), so the runner reports
  "no named gap (filler risk)" on bytes whose gap is plainly named. This is a **false
  negative of the mechanical check, not filler**.
- Consequence: claim C's counting command will fail this entry unless one side moves —
  the entry adds a recognized form, or the runner's gap check is widened. Changing the
  counting command mid-round is a parent/X03 judgment; this seat only reports the
  discrepancy. (The same runner earlier produced a true positive that was then fixed:
  `verification-independence-anti-circularity.md` at sha `0a94507a…` was flagged
  "no named gap", and the author's live revision to `9c5b0652…` cleared it.)
- Everything else passes: §11 decision record (worked-culture table D1…), all in-repo
  paths resolve, no URLs/commands cited, no duplication (no pre-existing flora file in
  the partition: baseline list has `animal-symbolism.md` but no plant file).

## 4. Source-resolution evidence (criterion 3)

- **In-repo paths**: every cited repo path in all ten entries resolves at freeze
  (`.scratch/r10c26-audit.py`, per-entry `missing_paths` → `[]` for all ten). This
  includes the two initially-unresolved citations, both fixed during the window:
  `myth-symbol/direction-symbolism.md`'s mis-segmented `corpus/knowledge/costume-semiotics.md`
  (repaired in a live revision; correct path `culture-material/costume-semiotics.md`
  exists) and `linguistics/language-shift-obsolescence-revival.md`'s citation of its own
  authorship fragment `reports/round-10/coverage/C01.md` (fragment landed; the full
  authorship set C01–C10 exists at freeze).
- **Receipt digests (independent recomputation)**: `verification-independence-anti-circularity.md`
  cites four receipt sha256 values; all four recompute exactly at freeze —
  `findings.md` `01c27fde…af5a`, `findings-17.md` `8f6eabad…0aa`, `findings.md` (r9/d3)
  `27ba8c2f…437c`, `findings-10.md` `19376989…91be` (command: `sha256sum <paths>`).
- **Cited commands re-run** (all from the lane root, 18:39–18:41Z):
  - `python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/direction-symbolism.md`
    → `files=1 marks=4 mark-lines=4 findings=0 blocked=0`, exit 0 (cited by #6).
  - `python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/` →
    `files=19 marks=21 mark-lines=21 findings=0 blocked=0`, exit 0 (cited by #7; its
    claimed before-state was `files=16`, and 19 = 16 + the 3 new myth-symbol entries,
    consistent).
  - `python3 tools/gates/provenance-audit.py corpus/knowledge/verification/to-verify-triage-protocol.md`
    → `files=1 marks=13 mark-lines=13 findings=0 blocked=0`, exit 0 (cited by #9).
  - `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
    → exit 0, 189 files (cited by #4).
- **Independent reproduction of #9's headline count**: #9 claims reading A = 64/179 on
  tree `e3a1ec9`. Re-running its §3 one-liner on the then-current tree gave
  `files=182 missing_any=67`; the three then-new entries are all in the reading-A
  remainder (`source` singular absent; lane profile is plural `sources`), so removing
  them reproduces exactly `64/179`. Claim reproduced arithmetically.
- **URL sweep** (~30 URLs, bounded `curl`, 18:36–18:41Z): all resolve to identification
  level. HTTP 200/202/203 for WALS ×4, Wikipedia ×8, avalon.law.yale.edu, kam.illinois.edu,
  doi.org (Elsevier/PLOS/PMC/Glossa/MPG), reproducible-builds.org, wikisource (full
  paren-bearing URL). Documented non-200s: **403 bot-blocks** on ACM DOI targets ×3
  (`10.1145/382294.382710`, `10.1145/358198.358210`, `10.1145/355604.361591`), PNAS
  (`10.1073/pnas.1605782113`), Royal Society (`10.1098/rstb.2020.0390`),
  `teara.govt.nz`, `gov.wales` — identification-level only, recorded as such, not
  full-text verified. No URL was fabricated; every checked URL returned a live response
  or a documented block.

## 5. Live-churn note (why verdicts are hash-bound)

Entries were revised in place during the audit window (the round's workflow is
concurrent; nothing here is a defect, but verdicts bind the §1 hashes). Observed sha256
prefixes per entry across the window:

- verification-independence: `0a94507a` → `9c5b0652` → `e8b3503c` → `743bce54` (freeze)
- direction-symbolism: `1dfa1689` → `928d048e` → `5a6ef38f` (freeze)
- plant-symbolism: `9d480bd` → `49015d0` → `a9fd5e8f` (freeze; gained its §11 decision
  record during the window — an earlier revision had no decision heading)
- sound-symbolism: `dbc8339` → `17670f8` → `4f14b05a` (freeze)
- language-shift: `289a195` → `f488b17` → `89d2a225` (freeze)
- divination-omen: `f0d3775e` → `6666e7db` (freeze)
- transport: `36a7370f` → `d0a2c836` (freeze; revised 18:44:03 after the first freeze
  snapshot — the revision did not add a gap statement, re-verified; §3.1)
- stable across the window: numerals `57fc7669`, vessel `073e7fc5`,
  header-conformance `d627eba3`.

Two flags from the early window were cleared by these revisions (direction's broken
path; plant's missing decision heading); the two §3 candidates are the residue at the
freeze.

## 6. Limits

- Structural and resolvability checks only: this audit verifies that a gap is named (not
  that the gap is genuine — cross-checks in §4 cover the sampled cases), that a
  decision-record heading exists (not that every decision is sound), and that cited
  sources resolve to live objects (not that the objects support the claims at
  passage level — that is the reviewers' C11–C20 work, not absorbed here).
- Author-side, NON-CANON. This file admits no entry, edits no corpus byte, and decides
  nothing for lore-shokunin. The two candidates are routed to the parent; their
  disposition (entry repair vs runner adjustment) is not this seat's call.
