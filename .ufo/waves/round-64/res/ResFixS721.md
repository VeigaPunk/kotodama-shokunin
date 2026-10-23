# ResFixS721 — RF1 repair (S721 tier A→B, secondary-definition scope)

Lane: kotodama-shokunin, round 64 RESIDUAL REPAIR, seat ResFixS721. Leaf member: no subagent
dispatch, no commit, no jj/git command of any kind (so no index or jj-state mutation), no
fleet/sibling repo writes, no pacman. Only the named row file was edited, plus this report and
scratch under `/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS721/`. No tools installed or
updated.

## Assignment applied

RF1 from `.ufo/waves/round-64/w2/CriticRowsFinal.md`:
"retain this source/quote/bullet and mark B with scope explicitly describing the review's
secondary definition, or re-anchor A to the review's own result and adjust the dependent clause.
The former is smaller and preserves useful coverage. No counter change."

Applied as the former option: a two-cell correction on
`.ufo/waves/round-64/rows/ScribeRowS721/row.txt`, source/quote/bullet untouched.

## Old vs new cells (only diff in the file)

| Cell | Old | New |
|---|---|---|
| 4 (tier) | `A` | `B` |
| 5 (scope) | `infant vocal turn-taking and protoconversation in early development` | `the review's secondary literature-background definition of infant proto-conversation (citations to Hsu & Fogel 2003, Hsu et al. 2001, Kaye 1977), not its own synthesis result` |

Unchanged and verified equal: cell 1 source + live URL + capture URL, cell 2 `paper`, cell 3
title/author metadata, cell 6 anchor (`The developmental trajectory of turn-taking and its
moderators, paragraph 1: "<quote>"`), cell 7 teaches (`Helps worldbuilders portray early infant
social exchange as structured, nonlinguistic vocal turn-taking`), cells 8–11
`mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md`,
and the `BULLET`, `VERIFY`, `CAPTURE`, `ACCESS` lines.

Line-level diff of the reconstructed pre-edit text against the post-edit file: exactly one
`ROW:` line changed, and a cell-split comparison shows exactly two differing cells — index 4
(`A`→`B`) and index 5 (scope). Every other cell and every other line compares equal.

## Evidence

- **Tier basis (claim-scoped authority).** `corpus/QUALITY.md:29` criterion 6: "publisher
  descriptions and abstracts are tier B for substantive claims about a work, even when accurate;
  reserve tier A for sources primary or authoritative for the exact scope." The anchor is a
  literature-background sentence that *reports* the definition with upstream citations, so the
  review is secondary for this claim; A is available only for the review's own meta-analytic
  results, which this row does not anchor. Registry precedent for a claim self-limited by its
  evidence level: **S102** (`corpus/SOURCES.md:131`, tier B, scope names "journal abstract via
  ERIC; JSTOR full text blocked"); staged precedent for "secondary" wording: **S728**
  (`Frye's secondary account of Schieffelin's report …`, tier B).
- **Anchor is a background definition, not a result — verified live and in the row's capture.**
  `https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/` (HTTP 200, 318,427 bytes) and the row's
  capture `https://web.archive.org/web/20250212173742id_/…/PMC9271548/` (HTTP 200, 313,768 bytes)
  both contain the quote verbatim and continue:
  `…between infants and their peers or adults (Hsu & Fogel, 2003; Hsu et al., 2001; Kaye, 1977),
  reported already before 3 months of age (Bateson, 1975; Dominguez et al., 2016; Gratier et al.,
  2015).` The surrounding text is `The earliest described examples of vocal turn-taking in infants
  are called proto-conversations. Proto-conversation can be described as …` — background, before
  the reports of earlier studies. This independently reproduces the critic's counterexample.
- **Scope narrowing also resolves wave-1 F5.** `w1/ReviewerRegistry.md:99–108` recorded
  "F5 (LOW) — S721 scope wider than its anchored evidence … the quote only defines
  protoconversation." The new scope names exactly that definition, so the row no longer covers
  turn-taking at large while anchoring a protoconversation definition. The F5 tier note ("Tier A
  itself is fine") is superseded by the critic's stronger, in-article citation evidence, as RF1
  states.
- **No filed-tier edit.** `grep '^| S721 ' corpus/SOURCES.md` → 0 rows; the registry's highest id
  is S717. S721 is pre-integration staging, so QUALITY criterion 6's "correct a filed tier with a
  superseding SOURCES row, never an in-place tier edit" has nothing to supersede here. After
  integration, any further tier change must use a superseding registry row (S044–S046 pattern).
- **No counter or coverage loss.** Source, live URL, capture URL, anchor quote, teaches, bullet and
  used-by are byte-identical; only authority labeling and its claim scope changed.

## Verification (exercised by this seat)

- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`:
  `S721 OK`, final line **`CHECK-ROWS: 32/32 clean`**, exit 0 (transcript scratch
  `check-rows.txt`; run three times across the edit window, all clean).
- Invariant probe on the edited file (scratch `post-edit-check.txt`): **11 cells**; no `|` inside
  any cell; tier `B`; status `mined`; opened `2026-10-23`; recheck `180d`; used-by exact;
  anchor quote **18 normalized words** (8–25 bound, unchanged); teaches **13 normalized / 12
  whitespace words** (≤25, unchanged); `VERIFY` starts `LOCATED`; capture timestamp
  `20250212173742` matches the live URL; five lines `ROW/BULLET/VERIFY/CAPTURE/ACCESS`; LF-only,
  single trailing newline; 1,294 bytes.
- Byte custody: pre-edit file bytes `ca997cf34d319b9c7b19a07fd7ca37dae12f9005c23231b8ce42248abe65e08d`
  (1,187 bytes including the trailing LF); stripping that one trailing LF reproduces the critic's
  snapshot hash `c1492af6f6ec47af06d5a33d85e115e6184d55a689f5a6231cf48c4c4d858d28` exactly, so the
  edit started from the bytes the critic reviewed. Post-edit bytes
  `6c4e32d8a6e0df0f4cd2c8571f8b4db23a07684498b35a2477ae9c8503b69f58`.
- Downstream counters checked, no impact: `reports/round-64/accept-c.py:199–208` accepts tier `A`
  or `B` and asserts no tier minimum; `reports/round-64/accept-ca.py:110–123` HISTOGRAM is fixed on
  the committed round-63 base set `S694–S717` (`{"A":13,"B":11}`), which S721 cannot enter.

## Findings by severity

- **RF1 (assigned): resolved.** Tier now B, scope names the review's secondary
  literature-background definition with its upstream citations and disclaims the review's own
  synthesis; quote/teaches/bullet/source unchanged; no counter change. Blocking findings: none.
- **Minor — stale tier census in a wave-2 receipt.** `w2/ReportFrag2.md:355` states the 26 mined
  rows `S718–S743` are `A = 17, B = 9`. Current staged rows are `A = 14, B = 12` (S719, S721,
  S722, S723, S724, S725, S726, S727, S728, S730, S732, S737 are B) — a point-in-time count, with
  sibling repairs concurrent. Any final receipt must recompute rather than quote that line. Not
  this seat's file; flagged, not edited.
- **Minor observation — locator granularity.** The locator `The developmental trajectory of
  turn-taking and its moderators, paragraph 1` is accurate at section+paragraph level, but on the
  live page the anchor is the third sentence of that opening paragraph, after
  `The earliest described examples of vocal turn-taking in infants are called proto-conversations.`
  Left unchanged per RF1 ("retain this source/quote/bullet"); recheck seats should not read
  "paragraph 1" as "sentence 1".
- **Minor observation — long scope cell.** The new scope is 25 words, the longest staged scope
  (cf. S728 ≈ 16). No formal bound exists and the checker splits cells cleanly, so this is a
  readability note only; kept because RF1 asks the scope to name the secondary definition and its
  citation basis explicitly.

## Residual risk and verification gaps

- Sibling seats are editing S723/S726/S737/S740 concurrently; the `32/32` result is a moment-in-time
  observation of the staged set, not an atomic post-repair snapshot.
- The B rationale rests on the opened page's citation chain and sentence position. The cited
  primary works (Hsu & Fogel 2003; Hsu et al. 2001; Kaye 1977) were **not** opened here; that is
  sufficient for B scoped to the review's secondary statement, but returning to A would require
  anchoring one of those primaries (or a review-authored result), a different row.
- LSP: the `lsp` device is not mounted in this runtime (`xd://lsp` → "No such tool … Mounted
  devices: ast_edit, debug"), and the artifact is a five-line plain-text data row with no language
  server. Caller/definition/invariant checks are therefore the cell/byte probes above plus the
  canonical row checker, not semantic LSP queries; recorded rather than presenting text grep as
  semantic proof.
- The archive capture was verified at one timestamp (`20250212173742`) and the live page at
  2026-10-23; future redirects/edits by the publisher are outside this probe.
- No judgment or admission is claimed: verdict data remains with the canonical Rust judge.

Report: .ufo/waves/round-64/res/ResFixS721.md
