# R67 corpus/README.md edit plan — corpus/knowledge/culture-material/medicine-healing-codes.md
# Scribe seat: ScribeReadmePlan. Read-only measurement of the lane at base+rounds
# (sweep.py green: 240 rows / 240 files, culture-material 33, totals 240,
# footer 30/29/33/29/24/95). Nothing here is applied; the L1 integrates.
#
# ROW GRAMMAR (measured, not guessed): reports/round-28/readme/sweep.py ROW_RE is
#   ^- `([^`]+\.md)` — (.*)$        (space EM DASH space, single physical line)
# and its topic leg compares the row text to the entry's `- topic:` head-block
# text (continuation lines space-joined) with EQUALITY. accept-c.py TOPIC
# (lines 419-431) takes the FIRST physical line starting "- topic:", strips it,
# and substring-tests it inside the first line that starts "- " and contains the
# basename. Both pass only if the row is one line, uses the backticked BASENAME,
# and carries the full topic string (a wrapped entry topic still passes TOPIC by
# prefix containment, but then sweep's equality leg fixes the full text).
#
# CONSEQUENCE: the wave prompt's shorthand `- corpus/knowledge/culture-material/
# medicine-healing-codes.md — ...` (full path) does NOT satisfy ROW_RE; it would
# show as 1 ghost row + 1 missing row -> SWEEP fails -> ACCEPT-C-67 fails.
# Use the line below verbatim (it is the only line in this file starting with
# "- `medicine-healing-codes.md`" for easy extraction).

- `medicine-healing-codes.md` — medicine, healing and physicians as a material and social register for fictional cultures - the healer-role map (physician, surgeon, apothecary, herbalist, ritual healer) and the institutions that train and license it; disease theory as a code (humoral, dosha, qi and meridians, the Four Tantras) and the regimen each licenses; materia medica, pharmacy and guild regulation; surgical instruments and wound care; the hospital, infirmary, lazaretto and quarantine as built institutions; diagnosis, prognosis and the consilia advice literature; protective dress, amulets and the materia of prophylaxis; and medical texts as objects of transmission - a sourced design reference for fictional medicine, not a universal history of medical practice.

# ---------------------------------------------------------------------------
# TOPIC INTERLOCK (blocking dependency for the L1)
# ---------------------------------------------------------------------------
# The entry file does NOT exist on disk at drafting time
# (corpus/knowledge/culture-material/medicine-healing-codes.md absent; stage/
# held only mut-o/). The `- topic:` string above is therefore a PROPOSAL.
# The entry's head block MUST carry exactly:
#   - topic: medicine, healing and physicians as a material and social register
#     for fictional cultures - ... (same string, wrapped is allowed; sweep
#     joins continuations with single spaces)
# i.e. `- topic:` + one space + the string after "`medicine-healing-codes.md` — ".
# If integration lands a different `- topic:` text, REGENERATE this row from
# that text (never edit the entry to match a README draft): TOPIC and SWEEP
# both demand byte equality, and the row is derived, not the source.
#
# ---------------------------------------------------------------------------
# INSERTION POINT (filename order inside `## culture-material/`)
# ---------------------------------------------------------------------------
# Culture-material rows are alphabetized by basename. Insert the row directly
# AFTER the `material-culture-inference-method.md` row (README line 403) and
# BEFORE the `music-instrument-lexicon.md` row (README line 404; the two are
# adjacent, so the new row becomes line 404). Verified sort:
#   material-culture-inference-method.md  <  medicine-healing-codes.md  <  music-instrument-lexicon.md
# ("mate" < "medi" < "musi"). Do not append at the section tail.
#
# ---------------------------------------------------------------------------
# COUNT EDITS — exactly three lines change (current README line numbers)
# ---------------------------------------------------------------------------
# 1) line 381   section header
#    before: ## culture-material/ (33)
#    after:  ## culture-material/ (34)
#
# 2) line 703   totals line
#    before: Total knowledge entries: 240.
#    after:  Total knowledge entries: 241.
#
# 3) line 707   counts footer (total AND the third directory total)
#    before: (total 240 files; directory totals 30/29/33/29/24/95).
#    after:  (total 241 files; directory totals 30/29/34/29/24/95).
#    (directory order is the README's own section order:
#     linguistics 30, myth-symbol 29, culture-material 33->34, synthesis 29,
#     verification 24, civilizations 95. Leave the `Counts checked 2026-10-24`
#     date and the command text unchanged; the landing is 2026-10-24.)
#
# DO NOT TOUCH: revision 2.18's own history at lines 8-9 (`32 -> **33**`,
# `239 -> **240**`) records the PREVIOUS move and must stay as written.
# No other `33`/`240` token exists in the file (grep -n '\b33\b\|\b240\b'
# returns lines 8, 9, 381, 703, 707 only).
#
# ---------------------------------------------------------------------------
# REVISION HEADER BLOCK — add ABOVE `revision: 2.18` (precedent: every landing
# since 2.16 prepends one block; 2.17 shows the registry clause is optional, so
# it is omitted here rather than guessed — measure it if integration wants it)
# ---------------------------------------------------------------------------
# revision: 2.19 — Round-67 culture-material landing (2026-10-24): one
# culture-material entry landed (`medicine-healing-codes.md`, medicine, healing
# and physicians as a material and social register; the base had 0
# word-bounded filename owners, with only partial-scope topic mentions
# (bathing prophylaxis, scent plague-costume, myth-symbol purity)). Its row is
# added in filename order between `material-culture-inference-method.md` and
# `music-instrument-lexicon.md`, with the entry's `- topic:` text verbatim;
# `## culture-material/` moved 33 → **34**; the totals and footer moved
# 240 → **241**.
#
# ---------------------------------------------------------------------------
# OPTIONAL, prior-landing pattern (2.16/2.17/2.18 each added one): a single
# bullet at the end of `## Known gaps (frontier)`, e.g.
#   - Round 67 adds `medicine-healing-codes.md` as a sourced culture-material
#     register (24 new registry rows S805-S828). Partial-scope neighbors remain
#     `culture-material/bathing-and-body-hygiene.md`,
#     `culture-material/scent-perfume-aromatics-codes.md` (prophylaxis), and
#     `myth-symbol/` purity material.
# Only land it if every clause is true at integration (registry count is
# claim-frozen at 24 mined rows; do not add a row total).
#
# ---------------------------------------------------------------------------
# VERIFICATION after applying (read-only; run at the lands tree)
# ---------------------------------------------------------------------------
# python3 -B reports/round-28/readme/sweep.py
#   expect: parts {"civilizations": 95, "culture-material": 34,
#                  "linguistics": 30, "myth-symbol": 29, "synthesis": 29,
#                  "verification": 24}
#           rows 241 files 241
#           missing_from_index 0, orphan_rows 0, topic_mismatch 0,
#           header_drift {}, totals_ok True, footer_ok True
#           footer_live dir_totals [30, 29, 34, 29, 24, 95]; exit 0
# and, once the entry exists:
#   grep -n "^- \`medicine-healing-codes.md\`" corpus/README.md   -> exactly 1 line
#   python3 -B reports/round-67/accept-c.py --root <clone> --lands <lands>
#     -> TOPIC PASS (and FILE/no-harm legs unaffected by this edit)

# ---------------------------------------------------------------------------
# MEASURED SIMULATION (this draft, applied to an in-memory README copy + a
# temporary knowledge tree whose culture-material files are symlinks plus a stub
# entry carrying the topic above; reports/round-28/readme/sweep.py imported as a
# module, sweep(text, root_override=tmp))
# ---------------------------------------------------------------------------
# baseline (current tree, unchanged README): sweep ok True, rows 240 files 240,
#   culture-material 33, footer_ok True.
# draft applied (row + 3 count edits):        sweep ok True, rows 241 files 241,
#   culture-material 34, missing 0, orphans 0, topic_mismatch 0, header_drift {},
#   totals_ok True, footer_ok True,
#   footer_live {'total': 241, 'dir_totals': [30, 29, 34, 29, 24, 95]}.
# culture-material section rows: 34, sorted True, new row index 21, neighbors
#   material-culture-inference-method.md < medicine-healing-codes.md <
#   music-instrument-lexicon.md.
# NEGATIVE CONTROL (full-path row exactly as the wave prompt words it):
#   sweep ok False, missing ['culture-material/medicine-healing-codes.md'],
#   orphans [] (the line is invisible to ROW_RE, so it is a MISSING row, not a
#   ghost). This is why the in-file basename grammar is used.
# NEGATIVE CONTROL (one-char topic drift, "healer-role" -> "healer role"):
#   sweep ok False, topic_mismatch 1 class REWRITE. Sweep's equality is what
#   pins the row to the entry's `- topic:` text; accept-c.py TOPIC alone
#   (prefix substring) would not have caught it.
#
# SHADOWING NOTE: accept-c.py TOPIC takes the FIRST `- ` line containing the
# basename. The index row (line 404) is followed only much later by the optional
# Known-gaps bullet (~line 700), which also starts "- " and names the file, so
# the row wins. Never add a `- ` line naming the file above line 404.
