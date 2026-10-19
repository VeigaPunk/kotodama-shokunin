# W02 — Ca landing wire: README duplicate-H1 removal + over-build queue successor

- Seat: `W02` | role: executor | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Out path: `reports/round-48/calib/W02-landing-spec.md` (this file, the only write by this seat)
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Contract read: `reports/round-48/claims.json:41-52` (claim Ca), `reports/round-48/targets.json:54` (this seat)
- Mission: the integrator's exact apply for (A) the live README duplicate-H1 fix and (B) the new queue-successor record dispositioning the r47 over-build defect class.

**One-line statement.** Two independent applies: A removes the redundant second H1 at `corpus/README.md:3`, measured as sha `7c788a1d…` → `d407260d…` with the sweep still green; B extracts a **new** successor artifact (`queue-successor-r48.json`) carrying a closing row for `R36-README-DUPLICATE-HEADING` and a `routed-with-owner` row for `r47-overbuilt-entry-draft`. The parent queue and every r47 byte stay untouched.

---

## 1. Live state measured at the baseline

All commands run from the lane root, 2026-10-19, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| object | command | measured |
|---|---|---|
| HEAD | `git rev-parse HEAD` | `a01405dd36367292255c2652ac0a601f4cd6a0af` |
| README pre-state | `sha256sum corpus/README.md`; `wc -lc` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`; 575 lines / 143866 bytes |
| duplicate H1 | `grep -n '^# kotodama-shokunin corpus index' corpus/README.md` | `1:` and `3:`; `grep -c` → **2** |
| all H1s | `grep -n '^# ' corpus/README.md` | only lines 1 and 3 — no third H1 to preserve |
| prologue bytes | `sed -n '1,6p' corpus/README.md \| od -c` | `# index\n\n# index\n\nrevision: 2.4 …` (the two titles are byte-identical) |
| baseline sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, 0 missing / 0 topic mismatch / 0 orphan, totals 223, footer ok, `readme_sha256 7c788a1d…`, exit 0 |
| corpus census | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l` | 223; 25 |
| cartography slot | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | absent (C owns this landing, not Ca) |

Pins for the successor chain (all re-read from committed bytes at `a01405d`):

| artifact | sha256 |
|---|---|
| `reports/round-40/op/defect-queue-v2.json` (parent) | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` |
| `reports/round-43/calib/defect-queue-v2-successor-r43.json` | `77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38` |
| `reports/round-47/calib/queue-successor-r47.json` (immediate predecessor) | `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58` |
| `reports/round-47/review/R03-c-content.md` (over-build evidence) | `7e3e0880cfc7610b5d066bdf09c713a22038121b84cabb12c4fb8f968e8f238e` |
| `reports/round-47/claims.json` | `7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34` |
| `reports/round-47/validation.json` | `17f8f1d4498f5c0f89ac51989e2c42d91b3275a692b988f02b88c56d6942d166` |
| `reports/round-48/claims.json` | `bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292` |
| `reports/round-28/readme/sweep.py` | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` |

`git status --porcelain corpus/README.md reports/round-40/op/defect-queue-v2.json reports/round-47/calib/queue-successor-r47.json` → no output (all tracked and clean).

---

## 2. Application A — remove the duplicate H1 at `corpus/README.md:3`

### A.1 Preconditions (stop if any fails)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
test "$(git rev-parse HEAD)" = "a01405dd36367292255c2652ac0a601f4cd6a0af"
test "$(sha256sum corpus/README.md | cut -d' ' -f1)" = "7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd"
test "$(grep -c '^# kotodama-shokunin corpus index' corpus/README.md)" = "2"
test "$(grep -c '^# ' corpus/README.md)" = "2"
git diff --quiet -- corpus/README.md
```

If C's rev-2.5 README edit has already been applied, the README sha will not match. In that case read §2.5 before editing; do **not** force the pin.

### A.2 Exact edit

Delete the second H1 and one of its two adjacent blank lines. Operational rule: the prologue must go from

```text
# kotodama-shokunin corpus index

# kotodama-shokunin corpus index

revision: 2.4 — ...
```

to

```text
# kotodama-shokunin corpus index

revision: 2.4 — ...
```

Unified diff (this is the whole change; no other line is touched):

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -1,7 +1,5 @@
 # kotodama-shokunin corpus index
 
-# kotodama-shokunin corpus index
-
 revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
 myth-symbol entries landed (`mineral-stone-symbolism.md`,
 `purity-pollution-boundary-systems.md`, `sacred-topography-pilgrimage.md`),
```

Equivalently: `sed -i '2,3d' corpus/README.md` after the A.1 checks pass. Either `sed -i '2,3d'` or `sed -i '3,4d'` produces the same final bytes (both remove the second title plus one blank); preserve exactly one blank line between the H1 and `revision: 2.4`.

### A.3 Postconditions (measured on the staged copy this seat)

| check | command | expected |
|---|---|---|
| H1 count | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | `1` |
| all H1 count | `grep -c '^# ' corpus/README.md` | `1` |
| first line | `sed -n '1,3p' corpus/README.md` | line 1 title, line 2 blank, line 3 `revision: 2.4 …` |
| size | `wc -lc corpus/README.md` | `573 143832` |
| digest (Ca-first at `a01405d`) | `sha256sum corpus/README.md` | `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` |
| diff scope | `git diff --name-only` | `corpus/README.md` only (plus the untracked successor file) |
| sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, 0 missing / 0 topic mismatch / 0 orphan, totals 223, footer ok, exit 0 |

The staged measurement this seat ran on the modified text (via `sweep.sweep(after_text, root_override="corpus/knowledge")`): `ok True`, `total_rows 223`, `total_files 223`, `missing_from_index []`, `topic_mismatch []`, `orphan_rows []`, `header_drift {}`, `totals_line 223`, `footer_findings []`. The live sweep at the pre-state was also green; the edit removes prose only.

### A.4 Heading-count control (the sweep has no such leg)

The r28 sweep parses sections, rows, totals and the footer, but no `^#` heading leg (`reports/round-28/readme/sweep.py:49-70`; grep for a heading regex returns nothing). The durable control owed by Ca05 is not present yet. Until it lands, the apply gate is these two commands, and this row is the durable note:

```bash
test "$(grep -c '^# ' corpus/README.md)" = "1"
test "$(grep -c '^# kotodama-shokunin corpus index' corpus/README.md)" = "1"
```

Owner for the durable extension: r48 integrator; Ca05 (`calib/Ca05-heading-control.md`) drafts the tools/ extension or the documented gate. If Ca05's control lands this round, run it in addition to, not instead of, the two commands above.

### A.5 Sequencing against C's README rev 2.5

The Ca edit is orthogonal to C10's rev-2.5 edit, but the pinned post-sha is order-dependent:

- **Canonical order (recommended):** apply A at `a01405d` first → README becomes `d407260d…` / 573 lines / H1 count 1. Then W01 applies the rev-2.5 edit (new culture-material row, totals 223→224, footer 25→26, prose vector repaired). The H1 removal does not move the `revision:` block and C's new revision block goes below the prologue, so the final README still has exactly one H1.
- **If C lands first:** lines 1–4 are still the same prologue (C's insertions go at or below the first `revision:` block), so the rule "delete the second H1 plus one adjacent blank line" still applies. Do **not** assert `d407260d…`; re-derive and record the post-edit sha. The heading-count control in A.4 still must return 1 on the final 224-row README.

Ca does **not** repair the rev-2.4 prose vector. `corpus/README.md:11` reads `25/23/25/29/24/94 → 25/23/26/25/24/94` (220 → 217) while the correct post-rev-2.4 vector is `25/26/25/29/24/94` = 223; the 223 footer at `:548` is correct. That repair is C10/W01's (`reports/round-48/claims.json:29-38`); touching it here would double-edit the same revision block.

### A.6 Boundaries

- Do not touch the revision history, the 223 rows, the totals line, the counts footer, or the prose vector in this apply.
- This is a live index correction, not a rewrite of filed round bytes (`reports/round-48/claims.json:58`).
- No staging under `corpus/knowledge/`; no runner execution; no git mutation beyond the integrator's own commit act.

---

## 3. Application B — file the r48 queue successor

### B.1 Target

Extract the fenced JSON below to a **new** file:

```text
reports/round-48/calib/queue-successor-r48.json
```

Do not edit `reports/round-40/op/defect-queue-v2.json`, `reports/round-43/calib/defect-queue-v2-successor-r43.json`, or `reports/round-47/calib/queue-successor-r47.json`. The new file is the only queue write.

### B.2 Fenced successor JSON (deliverable)

```json
{
  "schema": "kotodama-defect-queue-successor-v1",
  "round": 48,
  "date": "2026-10-19",
  "loop": 2,
  "position": 2,
  "artifact": "defect-queue-v2 successor delta - r48 Ca: README duplicate-H1 close + r47 over-build defect-class disposition",
  "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256_at_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "parent_sha256_recheck_after_assembly": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
  "parent_bytes_edited": false,
  "parent_git_state": "clean: `git status --porcelain reports/round-40/op/defect-queue-v2.json` -> no output; `git show a01405d:reports/round-40/op/defect-queue-v2.json | sha256sum` -> dfc9265d... (measured 2026-10-19, HEAD a01405d)",
  "parent_history": "Committed at 13a1657 with sha256 fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98; edited in place once at ac47c78 (r41) to flip N7-receipt-fidelity and r39-runner-root-regression and append r41_update. The digest has been dfc9265d... since that recorded supersession and is unchanged at a01405d. This successor does not edit the parent; the pin makes any further in-place edit detectable.",
  "predecessor_successor": {
    "path": "reports/round-47/calib/queue-successor-r47.json",
    "sha256": "9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58",
    "rows": 3,
    "provider_amendments": 2,
    "parent_pin": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907"
  },
  "prior_successors": [
    {
      "path": "reports/round-43/calib/defect-queue-v2-successor-r43.json",
      "sha256": "77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38",
      "rows": 4
    }
  ],
  "baseline_commit": "a01405d",
  "baseline_commit_full": "a01405dd36367292255c2652ac0a601f4cd6a0af",
  "source_fragments": {
    "reports/round-48/claims.json": "bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292",
    "reports/round-47/review/R03-c-content.md": "7e3e0880cfc7610b5d066bdf09c713a22038121b84cabb12c4fb8f968e8f238e",
    "reports/round-47/claims.json": "7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34",
    "reports/round-47/validation.json": "17f8f1d4498f5c0f89ac51989e2c42d91b3275a692b988f02b88c56d6942d166",
    "reports/round-28/readme/sweep.py": "9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3",
    "reports/round-40/op/defect-queue-v2.json": "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907",
    "reports/round-47/calib/queue-successor-r47.json": "9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58"
  },
  "class_vocabulary": {
    "fixed-with-evidence": "A landed artifact plus a pasted measured output closes the finding.",
    "routed-with-owner": "No fix is claimed; the finding has a named owner and a next touch.",
    "recorded": "The measured fact or correction is recorded; filed bytes are immutable or no action is owed.",
    "could-not-recover": "The evidence the finding depends on cannot be recovered; a named reason and owner are recorded.",
    "named-deviation": "A scheduled provider/model was not the observed provider/model, or a scheduled position did not execute, under a recorded operator ruling or lane-recorded amendment. Not a defect row: no rule breach is alleged.",
    "v2_mapping": "fixed-with-evidence -> fixed-with-evidence; routed-with-owner -> carried-with-owner (owner + next_touch); recorded -> carried-with-owner with next_touch 'none - recorded'; could-not-recover -> carried-with-owner with the named reason; named-deviation -> no v2 class (v2_class_equivalent null). The `class` field here is authoritative; `v2_class_equivalent` is the merge hint."
  },
  "rows": [
    {
      "id": "R36-README-DUPLICATE-HEADING",
      "origin": "r33-36 census (K02); parent row reports/round-40/op/defect-queue-v2.json:112-120; re-verified live at the r48 baseline a01405d",
      "class": "fixed-with-evidence",
      "v2_class_equivalent": "fixed-with-evidence",
      "owner": "r48 integrator (applies the Ca edit; Ca01 authors, Ca03 verifies)",
      "reason": "At HEAD a01405dd36367292255c2652ac0a601f4cd6a0af the README opens with the same H1 twice: `corpus/README.md:1` and `:3`, separated by one blank line (`grep -c '^# kotodama-shokunin corpus index'` -> 2; `od -c` confirms `# ... index\\n\\n# ... index\\n\\nrevision:`). The r28 sweep is heading-blind: its regexes cover section headers, rows, the totals line and the counts footer, and no `^#` heading leg exists (`reports/round-28/readme/sweep.py:49-70`), so it stayed green over the duplicate. The fix removes the second H1 and one adjacent blank line, leaving one H1, one blank, then `revision: 2.4 ...`. The staged result is 573 lines / 143832 bytes / sha256 d407260d..., and the sweep on that text is green 223 rows == 223 files with the footer ok.",
      "next_touch": "none - fixed at r48 application. The heading-count control the sweep lacks is applied as two commands in the application gate (A.4 / G5); if Ca05's tools/ extension lands this round, run it too. Durable owner for that extension: r48 integrator.",
      "evidence": "corpus/README.md:1,3 (live grep and od, 2026-10-19); reports/round-40/op/defect-queue-v2.json:112-120 (parent row); reports/round-39/cross/X00-connector.md:252-256 (sweep-blind finding); reports/round-28/readme/sweep.py:49-70 (no heading leg); reports/round-48/claims.json:41-45.",
      "verification": "Staged this seat at a01405d: after deleting the second H1 + one adjacent blank, `grep -c '^# kotodama-shokunin corpus index'` -> 1; `grep -c '^# '` -> 1; `wc -l` -> 573; `sha256sum` -> d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079; the r28 sweep run on the modified text -> ok True, total_rows 223, total_files 223, missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}, totals_line 223, footer_findings []. OWED at application (gate G4): re-run on landed bytes and paste the output into the round record.",
      "fixed_at": "round-48"
    },
    {
      "id": "r47-overbuilt-entry-draft",
      "origin": "r47 C landing attempt; non-author review reports/round-47/review/R03-c-content.md; r47 verdict reports/round-47/validation.json:9,69,79,85; carried into r48 as the Ca disposition target (reports/round-48/claims.json:43)",
      "class": "routed-with-owner",
      "v2_class_equivalent": "carried-with-owner",
      "owner": "r48 C claim (right-sized cartography drafter C01-C05) + r48 integrator; the Ca desk owns only this disposition row, not the redraft",
      "reason": "r47's cartography draft was a real domain entry but not landing-ready. R03 measured the assembled body at 739 lines / 17,601 words / 240 table rows against a live culture-material band of 103-221 lines (25 files, median 149, max 221) - 5.0x the median and 3.3x the longest existing entry (R03:8, :42, :87, :96). The r47 validation records the assembled entry as 790 lines (validation.json:9,79) - a different counting scope from R03's body-line count (the four filed fragments total 1449 file lines: C01-entry-a 358, C02-entry-b 503, C03-entry-c 287, C04-entry-header 301). Both figures are quoted with their scope; no subtraction or conversion is claimed. R03 confirmed nine blocking defects: B1 arithmetic (0.2 mm at 1:50,000 = 10 m of ground; a 200 m closure is 20x coarser, not 10x, R03:188); B2 an unreproducible gap count (R03:189); B3 a false source accusation that would corrupt the correct quote at naming-systems.md:70 (R03:190); B4 a mis-anchored workshop ladder (craft-artisan-lexicon.md:44 is steel grading; the ladder is :54-65, R03:191); B5/B6 cross-reference errors (R03:192-193); B7 a worked example that states its update rule three incompatible ways (R03:194); B8 a competing-ownership sentence against cosmology-cosmography.md:27 (R03:195); B9 a 'per form' table covering 5 of 8 forms (R03:196). The defect class is entry quality and volume, not topic ownership: the freshness gate (tools/harness/claims-freshness.py:1-20) re-derives whether a claim's factual premise still holds at the baseline; it does not measure draft length, arithmetic, citation anchors or worked-example consistency. That boundary is why this class needs its own durable row rather than being folded into the freshness row.",
      "next_touch": "r48 C: land one right-sized entry (<=~250 lines; the live partition max was 221 at a01405d) at corpus/knowledge/culture-material/cartography-and-mapmaking.md, with C03 (every number recomputed), C04 (every path:line resolves), C05 (length + contract), C14 (worked example: one update rule stated once, DR-CT rows named), and X03/R03 (depth-per-line, no B1-B9 recurrence) filed PASS on the landed bytes; then file a NEW closing row (fixed-with-evidence) with the pasted outputs. Never edit this row or any r47 filed byte in place. If r48 C does not land, the row stays routed-with-owner and the next corpus build round inherits it.",
      "evidence": "reports/round-47/review/R03-c-content.md:8 (one-line judgment), :16-19 (fragment line counts), :42 (partition band), :87,:96 (volume), :186-196 (B1-B9), :241-248 (do-not-apply order); reports/round-47/validation.json:9,69,79,85 (C unchanged; 790-line assembled-entry scope); reports/round-47/claims.json:23-35 (C claim); reports/round-44/scout/K02-gap-scout.md (topic fresh, sha256 a72fff27ee193cc12e689b5a3b485d3c0389bd4317b7810abf745ee441f335f6); reports/round-48/claims.json:29-38 (right-sized requirement); tools/harness/claims-freshness.py:1-20 (ownership-scope docstring).",
      "verification": "This seat at HEAD a01405d, 2026-10-19: `wc -l reports/round-47/cov/C01-entry-a.md C02-entry-b.md C03-entry-c.md C04-entry-header.md` -> 358 / 503 / 287 / 301 (1449 total); `python3` over corpus/knowledge/culture-material/*.md -> 25 files, min 103, median 149, max 221, mean 150.2; `grep -n '| \\*\\*B[1-9]\\*\\*' reports/round-47/review/R03-c-content.md` -> :188-196; the source shas above were re-computed and match. The 739-vs-790 difference is reported as a scope difference, not recomputed into a single number.",
      "incidence": {
        "rounds": [47],
        "claims": ["C"],
        "drafts": ["C01-entry-a.md", "C02-entry-b.md", "C03-entry-c.md", "C04-entry-header.md"],
        "count": 1
      },
      "class_boundary": "Not the r47-successor row r43-stale-premises: that row is premise freshness before dispatch (claims measured against the baseline), while this row is entry quality after drafting (length and audit legs). Not the r42/r44 topic-collision class: cartography was verified unowned at the r48 declaration, and this row faults volume/audit, not ownership. Not a filed-byte correction: r47 bytes are immutable; this row dispositions the class only.",
      "reclass_gates": [
        "G1 length: the landed entry measures <=~250 lines and the live partition band at landing is recorded; no 700-900-line draft is admitted.",
        "G2 arithmetic: C03 recomputes every number in the landed entry and reports zero B1-class errors, with the commands pasted.",
        "G3 citations: C04 resolves every in-repo path:line and reports zero B3/B4-class miscites, with the resolved count pasted.",
        "G4 worked example: C14 passes on the landed bytes, with one update rule stated once and the DR-CT ids named.",
        "G5 depth: X03 and R03 (non-author) measure depth-per-line and confirm no B1-B9 recurrence.",
        "G6 process: either a durable length/quality control lands (tool or gate extension), or the next C claim declares the discipline explicitly. A green freshness-gate run is not evidence of entry quality (tools/harness/claims-freshness.py:1-20)."
      ]
    }
  ],
  "heading_control": {
    "scope": "corpus/README.md",
    "commands": [
      "grep -c '^# ' corpus/README.md",
      "grep -c '^# kotodama-shokunin corpus index' corpus/README.md"
    ],
    "expected": "1 and 1 on the final README",
    "sweep_gap": "reports/round-28/readme/sweep.py:49-70 has no heading-count leg",
    "durable_owner": "r48 integrator; Ca05 drafts a tools/ extension or a documented gate"
  },
  "application_gates": [
    {
      "id": "G1-parent-pin",
      "check": "sha256sum reports/round-40/op/defect-queue-v2.json and git show a01405d:reports/round-40/op/defect-queue-v2.json | sha256sum",
      "expected": "both dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907; git status --porcelain <parent> empty"
    },
    {
      "id": "G2-predecessor-pin",
      "check": "sha256sum reports/round-47/calib/queue-successor-r47.json reports/round-43/calib/defect-queue-v2-successor-r43.json",
      "expected": "9508b6aa... and 77f9d63e...; neither file edited"
    },
    {
      "id": "G3-parse",
      "check": "parse the extracted JSON; assert schema, round==48, baseline_commit==a01405d, parent path+digest, predecessor path+digest, rows length 2, unique ids, every class in the vocabulary, every owner/reason/next_touch/evidence/verification non-empty",
      "expected": "parse OK; 1 fixed-with-evidence + 1 routed-with-owner; 0 provider amendments"
    },
    {
      "id": "G4-readme-apply",
      "check": "A.1-A.3 commands on landed bytes",
      "expected": "H1 counts 1/1; 573 lines; sha d407260d... if Ca-first at a01405d; sweep exit 0 with 223==223 and footer ok; git diff only corpus/README.md for Ca"
    },
    {
      "id": "G5-heading-control",
      "check": "the two heading strings in heading_control; plus Ca05's control if it landed",
      "expected": "each count 1"
    },
    {
      "id": "G6-row-completeness",
      "check": "re-read R03:186-196 and assert all nine B ids are named in the over-build row; assert its class is routed-with-owner and reclass_gates has G1-G6",
      "expected": "B1-B9 all cited; no fixed claim; gates present"
    },
    {
      "id": "G7-write-surface",
      "check": "git status --porcelain; find corpus/knowledge -name '*.md' | wc -l; ls corpus/knowledge/culture-material/*.md | wc -l",
      "expected": "only reports/round-48/** untracked plus corpus/README.md modified; corpus 223 and culture-material 25 (Ca adds no entry); no corpus staging"
    },
    {
      "id": "G8-no-filed-byte-edit",
      "check": "git diff --name-only -- reports/round-1..47 corpus/lessons tools/gates/frozen; git diff --cached --name-only",
      "expected": "empty; successor and spec are new records only"
    },
    {
      "id": "G9-source-digests",
      "check": "re-hash every path in source_fragments",
      "expected": "all match; a mismatch means a fragment moved after this assembly - reconcile by id alias, never duplicate the rows or edit this file"
    }
  ],
  "observations": [
    "Two counting scopes are deliberately kept apart: R03 measured 739 body lines (its fence extraction), while the r47 validation receipt records 790 assembled lines (validation.json:9,79). The four source fragments total 1449 file lines (358+503+287+301). No arithmetic is derived across the three figures.",
    "The r47 successor remains the immediate predecessor and is not edited. Its three rows and two provider amendments are unchanged; this successor adds only the two r48 rows and the heading-control note.",
    "The README fix is a live index correction, not a rewrite of a closed round's filed bytes (reports/round-48/claims.json:58).",
    "The over-build row is a class disposition, not a new defect census: one round (47), one claim (C), four draft fragments.",
    "The freshness gate exists at a01405d (tools/harness/claims-freshness.py, sha256 466aa60d247293e33907d608b565fe8acd91a04b6e38049e1bffdb6d5bfa858d per reports/round-47/validation.json:37,76) and is not being re-frozen or edited here."
  ],
  "provenance": {
    "seat": "W02",
    "role": "executor",
    "claim": "Ca",
    "out_path": "reports/round-48/calib/W02-landing-spec.md",
    "baseline_commit": "a01405d",
    "head_measured": "a01405dd36367292255c2652ac0a601f4cd6a0af",
    "date": "2026-10-19",
    "commands_run": [
      "git rev-parse HEAD -> a01405dd36367292255c2652ac0a601f4cd6a0af",
      "sha256sum corpus/README.md -> 7c788a1d...; wc -lc -> 575 143866",
      "grep -n '^# kotodama-shokunin corpus index' corpus/README.md -> 1,3; grep -c -> 2",
      "staged delete of lines 2-3 -> 573 lines / 143832 bytes / sha256 d407260d...; heading counts 1/1",
      "import reports/round-28/readme/sweep.py and sweep(modified_text, root_override=corpus/knowledge) -> ok True, 223==223, footer ok",
      "python3 -B reports/round-28/readme/sweep.py -> green, readme sha 7c788a1d... at pre-state",
      "find corpus/knowledge -name '*.md' | wc -l -> 223; culture-material -> 25",
      "wc -l on r47 C01-C04 fragments -> 358/503/287/301 (1449)",
      "wc -l corpus/knowledge/culture-material/*.md -> 25 files, min 103, median 149, max 221, mean 150.2",
      "grep -n '| **B[1-9]**' reports/round-47/review/R03-c-content.md -> :188-196",
      "sha256sum of parent, r43 successor, r47 successor, R03, r47 claims, r47 validation, r48 claims, sweep.py",
      "git show a01405d:<path> | sha256sum for README, parent queue, r47 successor, R03"
    ],
    "writes": "only reports/round-48/calib/W02-landing-spec.md",
    "no_filed_byte_edits": true,
    "no_in_tree_runner_executed": true,
    "no_git_mutation": true,
    "no_corpus_staging": true
  }
}
```

### B.3 What the two rows do

| row | class | what it records | what it does not do |
|---|---|---|---|
| `R36-README-DUPLICATE-HEADING` | `fixed-with-evidence` | Closes the parent row (`reports/round-40/op/defect-queue-v2.json:112-120`) with the measured edit and a staged sweep. | Does not claim a tools/ control landed; G5 keeps the two-command check in force. |
| `r47-overbuilt-entry-draft` | `routed-with-owner` | Names the class (length discipline + unreviewed arithmetic/citation/worked-example legs), owner, next touch, R03 B1-B9 evidence, and the freshness-gate boundary. | Does not claim a fix; does not edit r47 bytes; does not reopen the r43-stale-premises row. |

The first row is safe to file at apply time because the apply gate re-runs the measurement on landed bytes. If the integrator prefers the stricter shape used by the r43 successor, file it as `routed-with-owner` and flip it in place only after G4 passes — but a fixed row with an `OWED at application` verification is the r43 precedent (`reports/round-43/calib/defect-queue-v2-successor-r43.json`, row `r39-review-findings-disposition`) and is the shape used here.

---

## 4. Post-apply runbook (ordered)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. pins before touching anything
sha256sum corpus/README.md \
  reports/round-40/op/defect-queue-v2.json \
  reports/round-43/calib/defect-queue-v2-successor-r43.json \
  reports/round-47/calib/queue-successor-r47.json
# expect 7c788a1d... / dfc9265d... / 77f9d63e... / 9508b6aa...

# 2. apply A (README)
test "$(grep -c '^# kotodama-shokunin corpus index' corpus/README.md)" = 2
sed -i '2,3d' corpus/README.md

# 3. apply A postconditions
test "$(grep -c '^# ' corpus/README.md)" = 1
test "$(grep -c '^# kotodama-shokunin corpus index' corpus/README.md)" = 1
wc -lc corpus/README.md          # expect 573 143832
sha256sum corpus/README.md       # expect d407260d... only if applied at a01405d before C
python3 -B reports/round-28/readme/sweep.py   # expect 223==223, footer ok, exit 0

# 4. extract B.2 to the new successor file, then parse-gate it
python3 -B - <<'PY'
import json, hashlib
p = "reports/round-48/calib/queue-successor-r48.json"
o = json.load(open(p, encoding="utf-8"))
assert o["schema"] == "kotodama-defect-queue-successor-v1"
assert o["round"] == 48 and o["baseline_commit"] == "a01405d"
assert o["parent_sha256_at_assembly"] == "dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907"
assert o["predecessor_successor"]["sha256"] == "9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58"
assert len(o["rows"]) == 2 and len({r["id"] for r in o["rows"]}) == 2
print("successor parse OK:", [(r["id"], r["class"]) for r in o["rows"]])
print("sha256", hashlib.sha256(open(p, "rb").read()).hexdigest())
PY

# 5. write-surface
git diff --name-only                 # expect corpus/README.md only for Ca
find corpus/knowledge -name '*.md' | wc -l          # expect 223 (Ca adds no entry)
ls corpus/knowledge/culture-material/*.md | wc -l   # expect 25
git status --porcelain | head
```

After C's rev-2.5 landing, re-run the heading control and the sweep on the 224-row README: heading count 1/1, `224 rows vs 224 files`, footer vector `25/26/26/29/24/94` = 224. The final census (`F01`) owns those numbers; Ca only guarantees the H1 count stays 1.

---

## 5. Write surface and limits

- This seat wrote only `reports/round-48/calib/W02-landing-spec.md`. The README fix and the successor JSON are **drafts** in fenced blocks; the integrator applies them.
- No filed byte was edited: `reports/round-1..47/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, and fleet `.ufo/**` are untouched; `git status` showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.
- No git commit/push, no install, no network; no `reports/round-*/run-validation.py` was executed in-tree; no corpus staging occurred.
- **to-verify / owned elsewhere:** Ca05's durable heading-count control has not landed at this seat cut (owner r48 integrator; G5 keeps the two-command gate in force). The 739-vs-790 line difference is reported as a counting-scope difference, not resolved to one number; C03/C05/X03 own the landed-entry measurement. The rev-2.4 prose-vector repair is C10/W01's, not Ca's. Whether the integrator applies Ca before or after C changes the post-edit README sha; §2.5 states both paths and forbids asserting `d407260d…` out of order.
