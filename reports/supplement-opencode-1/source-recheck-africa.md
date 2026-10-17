# source-recheck-africa — supplement-opencode-1 fragment report

Role: SOURCE-RECHECK (worker scope 13). Entry owned: `corpus/knowledge/civilizations/africa-primary-sources.md`.
Baseline pinned: `fe34faaafbe0add59ff68827a0df6c5782a72404` (entry sha256 before edits `51e16738…a31e1a`).
Checked: 2026-10-17. Audit record: `corpus/lessons/supplement-opencode-1/sources/africa.json`.
Retrieval log (commands, digests, blocked route): `scratch/source-recheck-africa/retrieval-log.md`.

## What was checked and how

Direct retrieval only. Two PDFs were downloaded and converted locally with
`pdftotext -layout` so that every excerpt below comes from retrieved full text,
not a search snippet or metadata line; printed-page locators were verified against
page headers/footers inside those PDFs (Nyame Akuma 76 paginates 3–8; Manuscript
Cultures 17 headers carry the running title and page number). HTML sources were
fetched directly (journal, catalogues, archives, finding aid).

**12 audits: 11 supported, 1 contradicted, 0 unresolved.**

Coverage deliberately includes language/myth/era/dress coupling rather than
bibliography-only facts:

| id | target | type of test | verdict |
|---|---|---|---|
| AFR-01 | Raia colophon: copyist vs owner vs author, pp. 69–70 | script/language + naming roles | supported |
| AFR-02 | [RAI] cited as "Printed pp. 65–71" | source extent / locator honesty | **contradicted** |
| AFR-03 | SM017 coin+carnelian, SM023 shell beads, "p. 6" | era/material, observation vs interpretation | supported |
| AFR-04 | SM11 "Geophysical Survey"/"Open Spaces" headings; wattle-and-daub | era/material, phase separation | supported |
| AFR-05 | Sanye endonym vs catalogue "Dahalo"; tiers and restrictions | language/naming coupling | supported |
| AFR-06 | Verba Africana items 6–9 "planned performances"; item 3 Kéla version | performance/ritual provenance | supported |
| AFR-07 | Sunjata production: concise staging, poetic paraphrase not translation; 2025 issue | myth/language, edition-vs-performance | supported |
| AFR-08 | EAP334/1 "likely 1980s" content-based date | calendrical calibration of an inference | supported |
| AFR-09 | EAP1042/32/5 dual literacy, genres, water damage/ink stains | script/register + item condition | supported |
| AFR-10 | NEH Ajami four-language scope; recitations by local scholars | script/language; dated reading event | supported |
| AFR-11 | HMML Mali family libraries; Arabic/Bambara/Fulfulde listed | language listing vs "Timbuktu manuscript" | supported |
| AFR-12 | Bleek finding aid: prisoner access, custody at Mowbray | collection-setting constraint | supported |

## Correction made (append-only erratum, §11 of the entry)

AFR-02: the Raia 2021 article in *Manuscript Cultures* 17 runs to printed **p. 86**,
not p. 71 — the issue's article list shows Raia at 65 and the next article at 87, and
pp. 72–86 carry the article's running head, including the Group I–III variant tables
and orthographic-variant discussion. The entry's "printed pp. 65–71 inspected" is
retained as a reading record but labelled as a sub-range, not the article's extent.
Verified with `git diff --numstat`: 4 insertions, 0 deletions; no historic byte changed
(entry sha256 after edits `f50b14d3…e4191`).

## Limits and unresolved items

- Blocked: `https://eap.bl.uk/archive-file/EAP1042-32-5` returned HTTP 202 with an
  empty body; the searcharchives.bl.uk catalogue record for the same item was used.
- Web search was quota-blocked for this worker, so no third-party corroboration of
  journal metadata beyond the journal's own archive was attempted.
- Manuscript images, recordings, videos, filmed performances, museum objects, and the
  ELAR bundle contents were not accessed — matching the entry's own stated boundary.
  No lexical, phonological, or costume datum was extracted anywhere here.
- No verdict on contested interpretations named in entry §9; only source-to-claim
  correspondence at the cited locators was tested. AFR-07 notes one cosmetic variance
  the entry may harmonize later: the article spells "Lucy Duran" without the accent.

## Status

Author-side evidence for the parent to integrate. No shared bookkeeping written
(no LOG.md, SCORECARD.md, or packet files). No SHONEN box checked, no rank promotion,
no canon asserted; everything here is non-canon reference material for
lore-shokunin's separate handoff.
