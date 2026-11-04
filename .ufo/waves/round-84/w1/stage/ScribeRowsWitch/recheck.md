# Recheck cadence — S914–S918

The cadence is set on the mutable surface, not the print: each underlying
text is fixed (1911, 1865, 1484, 1867), but each is read through a digital
transcription that can be re-proofread, re-rendered or re-released. The
`recheck` cell carries the interval; the check is a re-fetch and a hash
comparison, then a re-locate of the quoted span if the hash moved.

- **S914 — 365d.** The EB11 volume is fixed; Wikisource is the moving
  part (re-proofreading, page moves, Parsoid render changes — the 2026-01-29
  capture already differs from the live render by 12,947 bytes while the
  article text is the same). One year is enough to catch a revision change;
  a revision change triggers an immediate re-locate.
- **S915 — 365d.** The 1865 print is fixed and the Gutenberg file carries
  no "most recently updated" line (release 2007-10-01), so the file is
  expected to be stable; an annual hash catches an errata update.
- **S916 — 180d.** The Malleus mainspace unit is explicitly incomplete and
  is being transcribed question by question; the Bull itself is stable, but
  the surrounding unit (the landing page's contents, the question pages)
  can gain the judicial Third Part, which would let the entry move its
  proof-technology citations from secondary sources onto the manual itself.
  Semi-annual is the shortest cadence that checks this without polling a
  wiki.
- **S917 — 365d.** The 1867 print is fixed; Gutenberg updated the file on
  2021-10-15, so an errata update is possible but rare; an annual hash is
  enough, and a hash change is a re-locate trigger.
- **S918 — 365d.** Rejected, and its flip depends on the Wikisource
  transcription of the EB11 "Sorcery" article growing past the dictionary
  stub; an annual check of the same URL catches the revision that would
  flip it, and no other surface moves.
