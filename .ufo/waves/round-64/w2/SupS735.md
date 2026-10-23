# SupS735 — blind support of the fixed S735 row

Axes judged: **coverage, operability, calibration**. This is a blind-support review of the fixed
contribution row only; I did not edit the row, the registry, any counter, or any lane state.

**Verdict: SUPPORTED.** The fixed bullet is a faithful, sample-bounded restatement of its anchor
quote and drops the previous success/outcome overstatement. One LOW residual in the same row and
one HIGH cross-cutting defect in the frozen claim-C counter are recorded below; neither is a
defect of the fixed bullet.

## Snapshot identity

- `.ufo/waves/round-64/rows/ScribeRowS735/row.txt` — 1316 bytes, 5 lines, mtime
  `2026-10-23 23:51:31 -0300`, md5 `a451be42758b42acb6d9323f22bd6edb`; read at `2026-10-23T23:54:54-03:00`.
- Old bullet (wave 1 / CriticEntrySweep CE2 target):
  `- Teacher questions and comments shape sharing-time discourse toward structure and focus, showing how oral classroom interaction can rehearse literacy. (S735)`
- Fixed bullet (current):
  `- In the observed classroom, the teacher tried through questions and comments to help children structure and focus their discourse. (S735)`
- The row is untracked in the lane git index (`git status` → `?? .ufo/waves/round-64/rows/ScribeRowS735/`); the fixed file is the only authority read here.

## Source evidence (pypdf path, not pdftotext)

- **Lane locator**, run at 23:54:54 from the lane root:
  `python3 -B reports/round-61/reopen-quote.py 'https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf' 'The teacher, through her questions and comments, tries to help the children structure and focus their discourse.'`
  → `LOCATED https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf`, exit 0. The locator's PDF reader is pypdf 5.4.0 (`reports/round-61/reopen-quote.py:19–22`), so this is the pypdf path, not pdftotext.
- **Independent pypdf extraction**: live GET `HTTP 200`, `application/pdf`, 658862 bytes, effective URL identical to the live URL (no redirect); extracted with `uv run --no-project --quiet --with pypdf==5.4.0`. The anchor quote appears verbatim on **PDF page 2** (abstract) after NFKC/casefold/NONWORD normalization; anchor is 17 words (row rule 8–25).
- Source text read in the same extraction:
  - Abstract: `The teacher, through her questions and comments, tries to help the children structure and focus their discourse.` — the sentence is the teacher's **attempt**, not an outcome.
  - Abstract, immediately following: `When the child's discourse style matches the teacher's own literate style and expectations, collaboration is rhythmically synchronized and allows for informal practice ... For these children, sharing time can be seen as a kind of oral preparation for literacy. In contrast, when the child's narrative style is at variance ... collaboration is often unsuccessful ... Sharing time, then, can either provide or deny access to key literacy-related experiences ...`
  - Design bound: abstract studies `an ethnically mixed, first grade classroom`; conclusion (PDF pp. 439–440): `premature to make sweeping statements about specific educational outcomes, based on this analysis of sharing time in a single first grade classroom.`

## Bullet fidelity judgment

| Fixed-bullet element | Source support | Judgment |
|---|---|---|
| `In the observed classroom` | single first-grade classroom study (abstract; conclusion p. 440) | correct sample bound; no generalization |
| `the teacher tried through questions and comments to help children` | abstract `tries to help`, teacher's questions/comments | faithful attempt framing; the prior "shape" success premise is gone |
| `structure and focus their discourse` | abstract verbatim | faithful, within copy-run limit |
| *(absent)* shaping success / literacy rehearsal | source conditions literacy preparation on shared conventions; mismatch is `often unsuccessful` | omission is the correct repair, not a loss of anchor support |

Mechanical rule derivation using `check-rows.py`'s own `content_words`/`norm_words`
(`.ufo/waves/round-64/check-rows.py:100–160`): clause 19 words; content words 12; in-order quote
content hits **9** (`teacher, through, questions, comments, help, children, structure, focus, discourse`);
novel content words `{classroom, observed, tried}`; longest copied run **6**
(`children structure and focus their discourse`, ≤12); exactly one terminal `(S735)`.

## Format and invariant checks (row scope)

- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` at 23:54:54
  → `S735 OK`, `CHECK-ROWS: 32/32 clean`, exit 0.
  - Chronology caveat: an earlier run (~23:47) returned `31/32 clean` with `S719 PROBLEMS bullet_shape`
    while `FixRowS719` was mid-write (`ScribeRowS719/row.txt` mtime 23:52:10); the final 32/32 run is
    after that write. The transient failure was a sibling's half-written file, not S735.
- Row shape: 11 cells, tier `A`, status `mined`, opened `2026-10-23`, recheck `180d`, used-by
  `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`; teaches cell 18 words (≤25);
  capture timestamp `20161020153309` with the same normalized original URL; `VERIFY: LOCATED`.
- Live URL uniqueness: `grep -F` of `https://www.ling.ohio-state.edu/.../Michaels1981.pdf` matches only
  this row among `.ufo/waves/round-64/rows/*/row.txt`; it does **not** occur in `corpus/SOURCES.md`
  (827793 bytes at snapshot), so integration introduces no duplicate registry URL.
- Integration contract: `integrate-w2.py:174–207` renders `contributions[sid]["fields"]["BULLET"]` into
  the entry and rejects any generated line with ≥2 S-ids or a leading `|`. The fixed bullet has one
  terminal S-id and starts with `- `, so it satisfies both the generator guard and the
  `check-cited-lines.py` shape that ACCEPT-C ONEID invokes.

## Findings by severity

### HIGH — `accept-c.py` revision-3 RESTATE reads `row` before it is bound (out of assignment; claim-C counter, not the row)

- **Location:** `reports/round-64/accept-c.py:296` (`teaches = cells(row)[6] if row else None`) versus the
  only binding at line 300 (`row = reg_by_id.get(sid, [None])[0]`). Snapshot mtime `23:52:58`, bytes read at 23:53.
- **Evidence:** AST scan reports stores of `row` = `[300]`, loads = `[296, 296, 301, 301]`, and no
  module-level binding. On the first cited line the `if row else None` test raises `NameError`.
- **Why it matters:** the revision-2 teaches-copy guard (forcing control `w1/CriticClaims.md`, 26 copied
  teaches bullets passed rev1) cannot execute. With the revision-3 ONEID requirement that all 26 ids be
  cited exactly once (`accept-c.py:253–266`), any entry that could pass enters this loop and crashes the
  script instead of evaluating RESTATE. The guard is also semantically misplaced: even if `row` happened
  to be bound, it would compare against the preceding REJECTS loop's row, not the cited row.
- **Not my call to fix** (RevCounters owns counters; CriticRevC attacks them). Recorded because the fixed
  S735 bullet's RESTATE compliance cannot be evidenced by the frozen counter in these bytes.
- **If reordered**, the fixed bullet passes the leg deterministically: shape matches
  `^\s*-\s+(.*?)\s*\(S735\)\s*$`; clause ≠ the row's teaches cell; content 12; in-order 9; novel word
  present; copy run 6.

### LOW — teaches cell still states an unconditional learner opportunity

- **Location:** cell 7: `Learners can practice shaping oral turns into focused discourse through teacher questions, building communicative control in classroom narration.`
- **Evidence:** the source conditions beneficial practice on shared discourse conventions (abstract:
  matched-style children get practice/instruction; mismatch `often unsuccessful`; sharing time
  `can either provide or deny access`), and `communicative control` is not the paper's term.
- **Blast radius:** none on claim C today — `integrate-w2.py:189–190` inserts only the `BULLET` field;
  the teaches cell is read only for disposition rows (`integrate-w2.py:112`). So this is calibration
  debt in row metadata, not an entry claim. FixRowS735's instruction was to keep teaches unless it
  overclaims; a later row revision should either condition it (`when teacher and child share narrative
  conventions`) or leave it and keep it out of any exported bullet.

### NOTE — coverage ledger

The fixed bullet intentionally no longer represents the paper's differential-access thesis or the
literacy-preparation link. §7 still carries narrative apprenticeship (S734) and emergent literacy
(S736) (`BULLET_MAP` 7 = S734/S735/S736), so section coverage is not lost, but S735 now contributes
only the teacher-attempt finding. If the coverage ledger needs the differential-access finding, it
needs a separate anchor (the abstract's `can either provide or deny access` sentence), not a rewrite
of this bullet.

## Residual risk and verification gaps

- Anchor is the **abstract** (`Abstract:` locator), not a body page; consistent with the row set and
  located by the pypdf locator, but the row alone cannot page-check the quote. Low.
- I did not run `accept-c.py`, `check-cited-lines.py`, or the entry assembly (acceptance and integration
  belong to the L1); all contract statements above are static readings of the named scripts plus the
  row checker's own output.
- The integrated entry does not exist yet (`corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
  → ENOENT), so the used-by path is prospective and the final ONEID/RESTATE behavior is unexercised.
- `accept-c.py` was being edited concurrently; the HIGH finding is bound to the 23:52:58 bytes.
- No LSP server applies to this pipe-delimited Markdown row; the checks that matter are the row checker,
  the locator, AST ordering, and the PDF extraction, all run above. No LSP query was attempted or
  presented as evidence.
- Wayback capture was not re-fetched; only capture shape/normalized-original equality was verified
  (`check-rows.py` CAPTURE + `capture_mismatch` legs) and the live URL returned HTTP 200.

Tools installed/updated: none. Scratch only:
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/SupS735/` (`Michaels1981.pdf`, `Michaels1981.pypdf.txt`).
The only lane write is this report.

Report: .ufo/waves/round-64/w2/SupS735.md
