# ResFixS737 — RF3 repair (S737 tier A→B, ERIC-scoped)

Lane: kotodama-shokunin, round 64 residual repair, seat ResFixS737. Leaf member: no subagent
dispatch, no commit, no jj/git index mutation, no fleet/sibling repo writes, no pacman. Only the
named row file was edited, plus this report and scratch under
`/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS737/`. No tools installed or updated.

## Assignment applied

RF3 from `.ufo/waves/round-64/w2/CriticRowsFinal.md`: "B, explicitly scoped to the ERIC-reported
operational definition; retain the honest full-text access limit. No new work/URL is needed."
Applied verbatim as a two-cell correction on `.ufo/waves/round-64/rows/ScribeRowS737/row.txt`.

## Old vs new cells (only diff in the file)

| Cell | Old | New |
|---|---|---|
| 4 (tier) | `A` | `B` |
| 5 (scope) | `operational definition of verbal play in Schwartz's study of young children's metalinguistic awareness` | `ERIC abstract-reported operational definition of verbal play in Schwartz's study of young children's metalinguistic awareness` |

Unchanged and verified byte-identical: cell 1 source/live URL/capture URL, cell 2 `paper`, cell 3
title/author metadata line, cell 6 anchor (`ERIC abstract, verbal-play definition: "<quote>"`),
cell 7 teaches, cells 8–11 `mined | 2026-10-23 | 180d | corpus/knowledge/linguistics/language-socialization-and-acquisition.md`,
and the `BULLET`, `VERIFY`, `CAPTURE`, `ACCESS` lines.

Cell-split diff of the reconstructed pre-edit text against the post-edit file: exactly two
differing cells, `(4, ' A ', ' B ')` and `(5, ' operational definition …', ' ERIC abstract-reported
operational definition …')`. Every other cell and line compares equal.

## Evidence

- **Tier basis.** `corpus/QUALITY.md` criterion 6: "publisher descriptions and abstracts are tier B
  for substantive claims about a work … reserve tier A for sources primary or authoritative for the
  exact scope." The opened evidence here is the ERIC summary, which ends `(BD)`, not the study.
  Precedent cited by the receipt: registry **S102** (`corpus/SOURCES.md:131`), tier B for a paper's
  substantive claim known through its ERIC abstract.
- **Quote is verbatim in the ERIC record.** Reopened <https://eric.ed.gov/?id=ED149852>: the
  sentence "A sample was considered an example of verbal play if it incorporated an observable
  manipulation of the sound, semantics and/or syntax of the language." appears verbatim in both
  `meta-citation_abstract`/`meta-description` and the rendered abstract. Author `Schwartz, Judy I.`,
  date `1977/04/00`, title match the row.
- **Full-text access limit is real and still current.** `https://files.eric.ed.gov/fulltext/ED149852.pdf`
  returned **HTTP 404** on 2026-10-23; the archive capture
  `https://web.archive.org/web/20250426225743id_/https://eric.ed.gov/?id=ED149852` returned **HTTP 200**.
  The ACCESS line was therefore retained unchanged rather than weakened or strengthened.
- **No filed-tier edit.** `grep '^| S737 '` over `corpus/SOURCES.md` returns 0 rows; the registry's
  highest id is S717. S737 is pre-integration staging, so QUALITY criterion 6's "correct a filed
  tier with a superseding SOURCES row, never an in-place tier edit" does not apply here — nothing is
  filed to supersede. Post-integration, any further tier change for S737 must use a superseding
  registry row (S044–S046 pattern), not an edit inside the entry.

## Verification (exercised by this seat)

- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`:
  `S737 OK` and final line **`CHECK-ROWS: 32/32 clean`** (post-edit; run twice, both 32/32). Transcript:
  scratch `check-rows.txt`.
- Invariant probe on the edited file (scratch `post-edit-check.txt`): 11 cells; no `|` inside any
  cell; tier `B`; status `mined`; opened `2026-10-23`; recheck `180d`; used-by exact; anchor quote
  **25 normalized words** (within the 8–25 bound); teaches **16 words** (≤25); five lines
  `ROW/BULLET/VERIFY/CAPTURE/ACCESS`; `VERIFY` starts `LOCATED`; LF-only, single trailing newline.
- Byte custody: pre-edit file `aca195c0acd73b50ab3b47f3e22aca492b15dbb522209be92cdbfdc74c4c1459`
  (trailing LF included); stripping the trailing LF reproduces the critic's snapshot hash
  `f8df43e2e3701066d056400cdbbbb15a8604a9134399b302740aab337db2353a` exactly, so the mutation
  started from the critic-reviewed bytes. Post-edit:
  `3b4ba7f776153326ec77efbfab679d7565d8e30bf55446550c267d47e61fd5bd`.
- Downstream counter impact checked, none: `reports/round-64/accept-c.py:199–208` accepts `A` or `B`
  and has no tier-count minimum; the `HISTOGRAM` leg (`reports/round-64/accept-ca.py:111–120`) counts
  `S69[4-9]|7[01][0-9]` at the base commit, a set S737 cannot enter. No round-64 spec line requires a
  minimum count of tier-A rows.

## Findings by severity

- **RF3 (assigned): resolved.** Tier now B, scope names the ERIC-reported origin of the definition,
  quote/teaches/bullet/source unchanged, ACCESS limit retained.

No new blocking or major finding in the row is actionable under this seat's edit authority. Minor
observations, left unchanged because they are outside RF3 or forbidden by the assignment:

1. **Minor — quote at the ceiling.** 25/25 normalized words leaves zero margin to any future
   normalizer change (e.g. counting `and/or` or the trailing period differently) before
   `quote_words` fails. Pre-existing, not introduced here; flagged for the next recheck.
2. **Minor — summary authorship.** The definitional sentence is ERIC summary prose (record marked
   `(BD)`), so "ERIC abstract-reported operational definition" is the honest maximum; the study's own
   instrument wording remains unread while the full text 404s. If a future seat obtains the paper,
   A becomes available with the same quote re-anchored to the document itself.
3. **Minor — teaches paraphrase.** "playful verbal experiments" in cell 7 is an inference from the
   recorded definition, not its wording. Kept per assignment ("keep teaches"); the inference is
   narrow and does not touch the tier claim.

## Residual risk and verification gaps

- The repair is scoped to this row; the other four RF repairs are sibling seats. A 32/32 run proves
  the whole staged set was clean at the moment of my two runs, but not that it stays clean while
  siblings continue editing.
- I did not re-derive the full-text 404 by following ERIC's own "Full text" link from the live page
  (the page exposes no direct link in the fetched HTML); the 404 is for the canonical
  `files.eric.ed.gov/fulltext/ED149852.pdf` path named by the ACCESS line. That matches the ACCESS
  wording "linked full-text PDF attempt".
- LSP: the `lsp` device is not mounted in this runtime (`xd://lsp` → "No such tool", mounted devices
  `ast_edit`, `debug`), and the artifact is a plain-text data row with no language server. All
  caller/definition/invariant checks above are therefore exact byte/cell probes and the canonical
  checker itself, not semantic LSP queries; recorded here per the reviewer requirement rather than
  presenting text grep as semantic proof.
- No admission or judgment is claimed: verdict data remains with the canonical acceptance run.

Report: .ufo/waves/round-64/res/ResFixS737.md
