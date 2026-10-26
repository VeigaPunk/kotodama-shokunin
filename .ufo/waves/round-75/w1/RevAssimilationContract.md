# RevAssimilationContract — kotodama round 75, wave 1 (assimilation-plan review)

Seat: reviewer (leaf, no delegation). Scope: check the round's assimilation plan (DRAFT
`reports/round-75/claims.json`, claim C) against prompt §6 item 10 (2026-10-24 operator directive)
and the staged package's own checklist (`shokuknow/merge/kotodama/MERGE-REPORT.md`), walking every
obligation. I edited nothing but this file; claims.json/ledger.json untouched; shokuknow read-only;
read-only git only in the lane. All base-tree facts re-derived at base `f556d1049fe651d3d63975600b13acd9fb686f15`.

## Findings

**F1 — HIGH — row_set registers two documents no admitted entry cites (§10/CORPUS rule 4 violation latent in the frozen predicate).**
Staged citation truth (read from the package files):
- `knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` cites S876, S864, S865, S866, S870 (lines 4, 29–32).
- `...narrative-structure-frameworks.amend-2026-10-23.md` cites S902, S904, S885 (lines 4–5, 30).
- `...amend-2026-10-23b.md` cites **S905** (line 4) — a file claim C lists as refused-pending-triage.
- `...amend-2026-10-24.md` cites **S919 + S921** (lines 4–5) — also refused-pending-triage. (`...amend-2026-10-23c.md` cites S917, which folds into the Barthes document and is harmless.)

Claim C's row_set includes S891 (staged S905, unige.ch S/Z excerpt) and S892 (staged S919, unipa
marrone via wayback). Neither document is cited by either admitted entry as staged. §10: "Append
only the rows the admitted entries cite"; CORPUS rule 4: a row no admitted entry cites is not
appended. As drafted, the ROWS leg ("used-by exactly the admitted entries whose source: lines cite
it") would demand an **empty** used-by on S891/S892, and the kill rule has no limb that catches
that — the counter can PASS a §10-violating landing, or silently force the entries to cite
documents whose claims (the five codes; Marrone's account) no declared leg says are folded into the
two admitted files. Fix before freeze (pre-data, allowed): either (a) declare the fold — the frozen
amend-23 file carries re-grounded b/c/24 sections and the rejects rename b/c/24 "folded", row_set
stands at k=8; or (b) drop S891/S892, k=6 (S885..S890).

**F2 — HIGH — the S870 conditional is unreachable under the frozen ROWS leg.**
`rejects.refused_staged_not_appended` keeps staged S870 "appended only if a quote locates on the
page this round". But row_set (8 ids, S885..S892) contains no S870→lane mapping, and the ROWS leg
requires the registry diff to add "exactly the frozen row_set". If a quote locates, appending S870
makes the diff 9 rows ≠ frozen 8 → the counter fails the landing it should pass. If it does not
locate, the admitted canonical entry still carries `source: S870` and its §8 practitioner-register
section → REPOINTED ("no campaign-namespace id is cited as a lane row") and the kill rule ("any
admitted entry cites an unknown ... id") fail unless the entry text is rewritten. The claim must
state the entry-side disposition explicitly (drop the citation+§8, exactly as round 74 dropped the
S895 folded passage, or map the row at freeze). Neither branch is executable as written.

**F3 — MEDIUM — the four path-present files' byte-level decision (round-74 routed item 2) is backed by no leg.**
Verified live at base — all four staged copies differ from the lane's:

| file | staged sha256 | base sha256 |
|---|---|---|
| culture-material/heritage-taxonomy-models.md | b17223b9…8f99b | 09175b18…562c |
| culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md | 9ed5ceef…90206b | 8544fe1e…bc406c |
| linguistics/conlang-scholarship.md | ce666a2b…6854891 | fe7e214a…b8a55b2 |
| linguistics/conlang-scholarship.amend-2026-10-23.md | 8f889666…86a8d6 | 01029a64…94786c |

Neither claim mentions these files; the REJECTS leg requires only triage counts of the 40 staged
files. The routed obligation (diff staged vs lane, decide adopt-new-claims or record-superseded,
name the decision in the lesson) can be silently skipped. Fix: land the diffs/hunk summaries as
wave evidence and name the decision in the lesson; optionally add a REJECTS clause so the counter
sees it.

**F4 — MEDIUM — the by-document map must record the doc↔page URL normalization for S917/S921.**
Staged S917/S921 bind page-level URLs (`persee.fr/doc/page/...T1_0011_0000`, `...T1_0006_0000`);
S876/S885 bind the doc-level URL; all four fold into lane S885. `assimilation/id-renumber-map.json`
does not exist yet (`map.sha256: null`). COLLCHECK's "the map maps staged->lane by document for
every adopted id" is unprovable for S917/S921 unless the map itself states the
page-URL⊂document equivalence. Also: if the per-page transcription service answers through any
access control, the kill rule fires and S885's tier-A page claims (pp. 5/6/11/26) collapse to
notice-level — the freeze-time Gate must test that first.

**F5 — LOW — one row per document means multi-locator claims ride one evidence window.**
If the F1(a) fold happens, p.5/p.6/p.11/p.26 claims all hang off lane S885's single Gate quote +
window. `tools/check-cited-lines.py` (CITEDLINES) lints only MULTI-ID/TABLE-ID shapes — it does not
check quotes-in-windows; EVIDENCE checks only the one Gate quote. Legal per grammar, but the Gate
notes should name the extra locators explicitly so later rounds do not read uncovered spans as
located (round-74 Gate-notes precedent).

**F6 — LOW — staged entry header prose is CITEDLINES-red if carried over.**
Staged headers carry multi-id prose lines (e.g. canonical entry line 34: "recheck: 180d — ...
(S864 → 1, S865 → 3, S866 → 2, S870 → 1)" — four ids on one line = MULTI-ID). The rows' recheck
strip duty is frozen; the same strip must be stated for entry `recheck:`/`ground:` header lines or
CITEDLINES prints findings at lands.

**F7 — LOW — `counters/capture-evidence.py` tmp hygiene.**
Honors TMPDIR (`tempfile.mkdtemp(prefix=...)`, no hardcoded `/tmp` — §7.4 first limb ✓) but accepts
no scratch-dir argument (§7.4 asks counters to accept one). Cheap to add pre-freeze; otherwise
every seat must export TMPDIR explicitly.

**F8 — INFO — obligations verified green (no defect).**
- Claims-C `before` fully re-derived at base: registry 808 rows, last id S884; 0 narrative files
  under corpus/knowledge; 0-3-space id lists: reg 808 / staged 132 / collisions **26**
  (S859..S884, namespace drift only); adopted lane ids S885..S892 absent at base (0 hits).
- Planted-collision guard proof reproduced in scratch: registry + indented `  | S885 |` row →
  0-3-space extractor collisions 26→27; column-zero pattern misses it (26); a 4-space row is
  invisible to the 0-3-space extractor (26) — the COLLCHECK leg's expected both-ways shape.
- Quarantine slice re-derived from the register: 21 rows, 18 `payload-absent` + 3 prose-class,
  matching round-74's standing verdicts (PRESENT 10 / REFUSED 7 / UNVERIFIABLE 4 = 21); REJECTS
  leg carries the `## Quarantine` section. S792/S824 caveats must travel with the table.
- Round shape ✓: ONE theme (narrative-structure-frameworks, 5 staged files), 2 admitted entries
  (within 1-3); ≥1 admit + ≥1 reject in the GATE leg; refused entries/files carry reason+flip;
  append-not-replace holds (both admitted files are new at base; the package's only
  existing-target amendment, conlang-methodology, is refused this round).
- Prior lessons carried: R74-M6 window-scope grammar (excerpt/whole-document + visible-chars) in
  EVIDENCE; R74-M7 GATE cap 25 tokens AND 80 chars; FROZENCFG reads constants/map from the freeze
  blob with map.sha256; SCRATCHMIRROR now counter-checks the validate-receipt committed strictly
  before the append commit (the clause round 74 left owed).
- Census-start receipt exists: `.ufo/waves/round-75/census-start.txt`.

## Residual risk and verification gaps

- `reports/round-75/accept-c.py` / `accept-ca.py` are not yet in the tree (only
  `counters/capture-evidence.py` exists) — the R74-M8 class (counters must exist at the declared
  paths in the freeze commit) is an open freeze debt, as are `map.path`+`map.sha256`, the junk
  fixtures and the do-nothing control receipts.
- The renumber map, reg/staged/collisions artifacts, validate mirror and guard-proof fixture do
  not exist yet (assimilation/ empty at review time); every claim-C artifact leg is
  freeze/lands-time and unverifiable today. My base-side halves (id lists, collision set, guard
  semantics, quarantine slice, path-present hashes) are all reproduced above.
- F1/F2 decide row_set size (k=6 or 8) and the S870 entry disposition; both must be settled in the
  frozen claims before any seat scores landed data (pre-data amendment is legitimate; post-data
  rule change is not the claim's rule).

Scratch: `/fast/scratch/hyaku/kotodama-r75/RevAssimilationContract/` (id lists, quarantine slice,
hash pairs, planted fixture) — deleted before yield; all citable values are reproduced in this
file. No tools installed. No pacman.
