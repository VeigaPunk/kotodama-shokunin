# round-49 integration records

Seat fragments as they stood when the integrator stopped merging (2026-10-19). They are
evidence of authorship and process, not the registry: `corpus/SOURCES.md` is canonical.

- `E2-sources.md` (R49SourcesA, temp ids S201–S215 → S001–S015), `E4-sources.md`
  (R49SourcesB, S301–S315 → S016–S030), `E1-sources.md` (S101–S113 → S031–S043; first
  written by the integrator after both entry seats died on provider rate limits, then
  rewritten by R49EntryB). `idmap.json` is the renumbering; `merge.py` built the first
  merged registry.
- The landed registry carries corrections made after the merge and absent here (used-by
  trims on S001/S002/S004/S007/S013, the S003 quote trim, anchor dates, S013 tier A→B);
  each is logged in `corpus/lessons/round-49.md` `## Registry changes before landing`.
  Re-running `merge.py` would undo them.
- `Ca-evidence.md` (R49Revisions): before/after outputs for the README stub deletion and
  `tools/check-readme-revisions.py`.
