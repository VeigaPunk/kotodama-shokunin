# RevAuditA — supersedes chain rulings (claim O, residual wave, round 68)

Seat: L1-kotodama-r68-attempt2.RevAuditA. Audit: `.ufo/waves/round-68/rows/RevAuditA/audit.md` (RULING= per chain, CITE=/EVIDENCE=/ANCHOR= per chain).

## Rulings

| Chain | Ruling | Mechanism | Entry file re-pointed | Basis (one line) |
|---|---|---|---|---|
| S044>S034 | activate | repoint | corpus/knowledge/culture-material/hunting-foraging-subsistence.md | S034's tier-A publisher-abstract placement was reversed; S044 fixes tier/teaches; Crossref serves the anchor verbatim; all 7 citing sites carried |
| S045>S038 | activate | repoint | corpus/knowledge/culture-material/hunting-foraging-subsistence.md | same publisher page (Routledge), tier A->B correction; "controversially" verified on live page; both citing sites carried |
| S046>S039 | activate | repoint | corpus/knowledge/culture-material/hunting-foraging-subsistence.md | same Princeton page (via Wayback 20251023192527; live 403), tier A->B correction; all quoted terms verified; the citing site carried |
| S070>S060 | retire | none | corpus/SOURCES.md | correction verified true (Crossref page 165-181/issue S1; S060's 95-107 anchors are the preprint), but S070's scope disclaims content and anchors are metadata fields — repoint would strand 4 content citations on a metadata record; s row must become REJECTED with flip |
| S125>S095 | retire | none | corpus/SOURCES.md | correction verified true (UCL record 10054130: 2018 ORE Linguistics article), but S125's scope disclaims content and anchors are record fields — repoint would strand 5 content citations; S125's own teaches says "S095's URL, quote and scope stand" (a cell-flip fix), which the frozen activate/repoint mechanics cannot express; s row must become REJECTED with flip |

## Blocked chains / residuals

- S070>S060 and S125>S095 cannot settle as `activate` under the frozen mechanics: both are verified-true bibliographic corrections whose successor rows carry no content anchors. They are ruled `retire` with explicit flips (content-carrying successor, or source-cell/cell-flip correction of the t row). The L1 integration should mark both s rows `rejected` with the `REJECTED: …; flip: …` teaches text as written, and record the flip condition so a later round can settle them as active once a content-bearing row exists.
- The `settle-apply.py` repoint is a blind `\b{t}\b` token swap across citing files; for the three activated chains it is exact (all t tokens are in `(…)` sites or the row's source cell), so no residual tokens remain orphaned. The `(t-verify)` markers and prose tokens of the t ids are unaffected.
- S038>S045: confirmed the `:197` cite is S038 (not repointed by the S044 chain); it is carried by the S045 ruling.

## Tooling records

No installs performed (no tool need beyond curl/pdftotext, already present). pacman guard respected (no pacman transaction).
