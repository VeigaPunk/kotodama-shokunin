# ExecGraderV5 — grader v5 changes vs base v4 (sha 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7)

Candidate: `check-advance-evidence.py` sha256 `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`
(diff: 163 insertions, 9 deletions; only `tools/check-advance-evidence.py` touched, in a detached clone at e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2.)
Selftest: `SELFTEST PASS 126/126`, rc 0 (114 base checks kept + 12 new). All five mutation-target source
lines (script/style strip, comment strip, `return _html.unescape(s)`, `DISPO_ANY_RE = re.compile(...)`,
`for i in (0, 1, 2, 3, 4, 5, 6, 8):`) are byte-identical to v4 so textual mutant patterns still apply.

## Per-class changes (line numbers are in the candidate file)

- **A1 (Cyrillic lookalike in the verdict token)** — `_refuse_disguised()` at 256-270 with
  `HOMOGLYPH_MAP` at 126-128; wired in `dispositions()` at 288-289. An id line whose verdict matches
  only after NFKC + homoglyph folding refuses named.
  Diagnostic token: `VERDICT-NONASCII` (rc 2, stderr `ADVANCE-EVIDENCE_ERROR: line N: verdict token
  carries non-ASCII letters (VERDICT-NONASCII)`).
  Selftest: `round-94 A1: non-ASCII letters in the verdict token refused` (line 1630, chk rc 2).
  Direct receipt: rc 2 with the token above on the CriticClaims93 recipe line `- S001 L<U+041E>CATED ...`.
- **B1 (soft hyphen in the verdict token)** — U+00AD added to the verdict-normalisation strip `ZW_MAP`
  (124-125, `ZW_ONLY` keeps the v4 zero-width set for the raw re-test); the refusal at 285-286 fires when
  a verdict matches only after the soft-hyphen strip and the v4 view of the same line does not match.
  Diagnostic token: `VERDICT-SOFTHYPHEN` (rc 2, `line N: soft hyphen inside the verdict token (VERDICT-SOFTHYPHEN)`).
  Selftest: `round-94 B1: soft hyphen inside the verdict token refused` (line 1635, chk rc 2).
- **G1 (numbered phrase-only headings)** — `head_span_anchors()` at 635-642 strips a leading list number
  (`^\d+[.)]`) before counting heading tokens; `span_heads` at 655 feeds the span count at 661. The v4
  `head_anchors` rule is kept unchanged for phrase HITS, because battery93's frozen G0 positive control
  relies on `## 4. Efficacy` / `## 5. Table` as hit surfaces (floor 4, span 3 — G0 span under v5 is
  exactly 3). A number+one-phrase-word heading still supplies a hit but no longer supplies a SPAN
  surface, so the round-93 G1 counterfeit (hits 4/4, all numbered phrase-only) fails
  `phrase anchors span 1 heading/table surfaces < 3`.
  Named leg: `LEG TOPIC FAIL` (rc 1). Selftest: `round-94 G1: numbered phrase-only headings do not
  anchor` (line 1645, chk_leg TOPIC).
- **H1 (manifest row value that is a list)** — upfront row-value guard in `grade_entry` at 566-571
  (after the frozen A6g `manifest rows is not a JSON object` refusal, so battery93 A6g keeps rc 2 and
  its message) and the same guard in `grade_advance` at 411-419.
  Diagnostic token: `MANIFEST-ROW-TYPE` (rc 2, `manifest row value is not a JSON object (list where
  mapping expected): S011 (MANIFEST-ROW-TYPE)`).
  Selftest: `round-94 H1: manifest row value that is a list refused` (line 1652, chk rc 2).
- **I1 (registry row shorter than eleven cells)** — NEWIDS length guard at 684-687 (before
  `cells[3], cells[7], cells[8], cells[10]`); BASEROWS length guard at 750-753 (after the cell-count
  equality check, before the identity loop).
  Named legs: `LEG NEWIDS FAIL` / `LEG BASEROWS FAIL` with `<rid>: registry row has N cells < 11` (rc 1).
  Selftest: `round-94 I1: registry row shorter than eleven cells refused` (line 1659, chk_leg NEWIDS,
  ten-cell row variant so NEWIDS is the only failing leg).
- **J1 (en-dash inside NOT-LOCATED)** — `DASH_MAP` at 125 folds U+2010-U+2015, U+2212, U+FF0D to '-'
  in the verdict-normalisation path (line 283), so `NOT–LOCATED` matches the NOT-LOCATED arm and is
  never parsed as a LOCATED flip. The reported flip direction is now the true one
  (`disposition LOCATED -> NOT-LOCATED`), named leg `LEG APPENDONLY FAIL` (rc 1); the v4 false text
  `NOT-LOCATED -> LOCATED` no longer appears.
  Selftest: `round-94 J1: en-dash NOT-LOCATED reads as NOT-LOCATED, no false flip` (line 1664, chk).
- **K1 (lowercase unanchored verdict channel)** — `DISPO_ANY_RE_I` at 117 (case-insensitive view of the
  unchanged case-sensitive fallback, detection only) used by `_refuse_disguised` at 263-264; the gate at
  261-262 accepts lowercase ids (`[Ss]\d{3,}`).
  Diagnostic token: `VERDICT-LOWERCASE` (rc 2, `line N: lowercase verdict token outside the anchored rule
  (VERDICT-LOWERCASE)`). Anchored lowercase (battery93 A5a/A5b/A5c prose lines) still matches the
  re.I anchored rule exactly as in v4.
  Selftest: `round-94 K1: lowercase unanchored verdict refused` (line 1669, chk rc 2).

## Routed mutant pins (one named check per mutant class; each verified to fail under the mutation)

- `script-strip-off` — `mutant pin: script and style stripping active` (1675-1677): in-process
  `html_body_text` unit; script content `var prayer ...` and style `color: red` must be absent, body
  phrase present. Verified: mutant selftest FAIL 125/126 rc 1.
- `comment-strip-off` — `mutant pin: comment stripping active` (1678-1680): comment carrying an inner
  `>` so the generic tag stripper cannot cover for the removed comment rule. Verified: FAIL 125/126 rc 1.
- `unescape-off` — `mutant pin: entity unescape active` (1681-1684): `&amp;`/`&#65;`/`&quot;` must be
  decoded (the fixture carries `<p>` so the HTML path engages). Verified: FAIL 125/126 rc 1.
- `dispo-any-casei` — `mutant pin: lowercase unanchored verdict refused (dispo-any-casei)` (1686-1690):
  in-process `dispositions()` must raise `VERDICT-LOWERCASE`; under the re.I widening of
  `DISPO_ANY_RE` the lowercase token matches the fallback and the refusal never fires. Verified:
  FAIL 124/126 rc 1 (this and the K1 entry check both flip).
- `baserows-drop-cell8` — `mutant pin: base row opened cell change refused (baserows-drop-cell8)`
  (1691-1692): lands base row differing from base only in the opened cell must fail BASEROWS
  (chk_leg, rc 1). Verified: mutant selftest FAIL 125/126 rc 1.

## Regression evidence (scratch, this seat)

- battery93 grade set, v4 base (git archive of e7fa8eaf) vs v5 candidate: all 26 cases identical rc and
  identical named outcome, including `G0 rc=0 CLEAN`, `A5a rc=0 CLEAN` (anchored lowercase prose),
  `A6g rc=2 refused-unnamed` (frozen message unchanged), `A4a/A4b refused on TOPIC`.
  Command: `R93_ROOT=<v4tree|clone> R93_WORK=<scratch> python3 -B reports/round-93/battery93.py`;
  per-case diff of the 26 outcome lines: empty.
- Positive controls: selftest `positive advance` rc 0, `positive entry` rc 0, direct G0-style fixture
  rc 0 `ENTRY-EVIDENCE: PASS legs=9/9`.
- Stability: 4 concurrent selftest runs on separate work dirs — all `SELFTEST PASS 126/126` rc 0,
  126 `  ok ` lines, byte-identical output (md5 unique count 1).

## Named diagnostics for the battery manifest

| class | rc | diagnostic |
|---|---|---|
| A1 | 2 | `VERDICT-NONASCII` |
| B1 | 2 | `VERDICT-SOFTHYPHEN` |
| G1 | 1 | `LEG TOPIC FAIL` (`phrase anchors span N heading/table surfaces < 3`) |
| H1 | 2 | `MANIFEST-ROW-TYPE` |
| I1 | 1 | `LEG NEWIDS FAIL` (`registry row has N cells < 11`) or `LEG BASEROWS FAIL` |
| J1 | 1 | `LEG APPENDONLY FAIL` (`disposition LOCATED -> NOT-LOCATED`, correct direction) |
| K1 | 2 | `VERDICT-LOWERCASE` |

## Behavior notes for the L1

- A1/B1/J1/K1 refusals exit rc 2 via the frozen `Refused` path (stderr
  `ADVANCE-EVIDENCE_ERROR: ...`, no traceback); G1/H1-leg/I1/J1 stay leg refusals rc 1.
- H1 is also guarded in advance mode (same refusal); I1 in BASEROWS covers the equal-short base+lands
  case. Both are outside the CriticClaims recipes but cannot regress any frozen case (battery93 grade
  set verified identical).
- The K1 refusal changes v4's "lowercase prose stays clean" only for UNANCHORED id+located lines
  (battery93 A5a/A5b/A5c are anchored and unchanged). Real-lane lessons with mid-sentence
  `S<id> ... located` prose will now be refused rc 2 — this is the routed intent.
