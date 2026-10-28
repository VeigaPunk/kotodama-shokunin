# Claim-C config contract — what `accept-c.py` (round 77) reads at `<freeze>`

`reports/round-77/claims.json` at the freeze commit is the whole contract. The
counter reads it with `git show <freeze>:reports/round-77/claims.json`, never
from the graded worktree, and FROZENCFG fails the landing when the graded
tree's copy differs byte-wise.

A loadable skeleton with the round-77 values is in this directory:
`claims-C.skeleton.json` (loader proof: `draft-skeleton-load.txt`). Its staged
ids and document URLs come from `CLAIMS-DRAFT.md` (S897→S897, S898→S903); the
entry path is the draft's.

## Required keys (`CLAIM_KEYS`)

| key | shape | counter use |
|---|---|---|
| `entries` | `["corpus/knowledge/<partition>/<file>.md", …]` | ENTRIES/ROWS/REPOINTED/INDEX/CITEDLINES; must be repo-relative |
| `rows_before` | int (820) | ROWS arithmetic |
| `knowledge_before` | int (253) | ENTRIES arithmetic |
| `row_set` | `[{lane_id, staged_id, document_url}, …]` | ROWS set, REPOINTED/GATE/EVIDENCE/COLLCHECK per-row reads; `staged_id` may be one id or a list |
| `required_sections` | `[{path, pattern, min?, label?}, …]` | INDEX: the non-row edits — on this lane the `## Paths` bullet and the `## Search log` entry **in `corpus/SOURCES.md`**, never the entry. `path` is any repo-relative file (a record without `path` applies to every admitted entry); `min` defaults to 1; `pattern` is a Python regex matched per line, so the frozen pattern is the exact-appended-text check |
| `ground` | `{sweeps:[{pattern, candidate?, scope}], fragments:[…], terms?, receipt?}` | GROUND before/after; `candidate` must name an entry; `receipt` is graded (committed, no nonzero `exit`, declared `contains[]`) |
| `rejects` | `{refused_staged_not_appended: […], refused_files/families: […], counts?: {adopted, refused, total_staged_files, path_present?}}` | REJECTS: every S-id in the refusal prose must appear in the Gate reject table and must not be a lane row; declared counts must sum |
| `legs` | `[<name>, …]` | LEGCOUNT (refusal): must equal `--emit-legs` exactly — order, no duplicate, no extra/missing |

## Optional keys

| key | effect |
|---|---|
| `min_entries` | default 1; the loader refuses if fewer entries are listed |
| `rows_after` / `knowledge_after` | exact after-counts, graded when declared |
| `removed_ids` (also `removed_legacy_ids`/`legacy_ids`) | REPOINTED: these ids must not appear in the entry; a cited one fails |
| `staged_ids` | path to the staged-id universe (default `.ufo/waves/round-77/assimilation/staged-ids`, read at `<freeze>`); REPOINTED uses it to name a campaign-namespace citation |
| `scratch_mirror` | `{dir, receipt?}`; SCRATCHMIRROR grades `dir` (default the r77 assimilation tree): `reg-ids`, `staged-ids`, `collisions`, `guard-proof/{indented.md,fourspace.md,reg-ids-indented,reg-ids-four}`. A declared `receipt` is graded for exit 0, every row id and every entry basename |
| `census_start` | `{path, rows?, contains[]}`; CENSUS grades the committed start receipt (row count, no nonzero exit, declared strings) |
| `map` | `{path, sha256}` (r76 shape). COLLCHECK cross-checks the pinned staged→lane→document map when declared; FROZENCFG pins the blob digest. **Absent is legal** — the draft records the map inside `row_set` itself |
| `access_date` | top-level or claim-level `YYYY-MM-DD`; REQUIRED (the loader refuses without it) |
| `owned_inplace` | loadable, not graded (INDEX derives the partition and footer from the tree) |

Document-level stamps read by FROZENCFG: `round` (77), `status` (`frozen`),
`frozen` (`true` or the freeze sha), `base` (40-hex, must equal the claim base).

## Landing-side artifacts the legs read

| artifact | graded by |
|---|---|
| registry rows: 11 cells, `mined`, `opened` == access date, cadence-only `recheck`, `used-by` exactly the citing entry, source cell carrying the live URL **and** a `web.archive.org/web/<ts>id_/<original>` capture of the *same document* | ROWS |
| pre-existing rows: only the rule-2 cells (status, recheck, used-by) may change; no removal, no reorder | ROWS |
| entry: `source:` (one id + the document URL per line), `verified-at:`, `recheck:`, `ground:`, `topic:` in the header block, no placeholders, ≥1 `## ` section, body ≥ the smallest base entry (478 words on this base) | ENTRIES, REPOINTED |
| `tools/check-cited-lines.py` at lands, run over the entry | CITEDLINES |
| README: one index row with the entry's `- topic:` text verbatim inside its partition, live heading counts, last footer total+vector, older footers preserved | INDEX (+ `required_sections`) |
| `reports/round-77/evidence/S###.txt`: fetch/UA/HTTP 200/bytes/sha256/access-date/`claims-source` (naming `<freeze>`)/`claims-frozen: yes`/window block; `window-scope: whole-document` requires `visible-chars` == window length, `excerpt` requires ≥ 4096 characters; `window-sha256`/`window-bytes` re-derived | EVIDENCE |
| lesson `## Gate`: `Access date: …`; admit-table header carrying `quote` + `verdict`, one row per row with the document URL, the access date, a ≤25-token/≤80-character quote and the evidence path; reject-table header carrying `reason` + `flip`, ≥1 reject row with URL/reason/flip | GATE, REJECTS |
| `.ufo/waves/round-77/assimilation/`: reg-ids, staged-ids, collisions, guard proofs | SCRATCHMIRROR |

## Open freeze choices this counter does not make

1. `required_sections[]` must be declared (the loader refuses an empty/absent
   list). For this claim the two required non-row edits live in
   `corpus/SOURCES.md`: a `## Paths` bullet naming S897 → S898 and a
   `## Search log` entry for round 77. The skeleton's patterns key on the row
   ids and the round phrase; pin them to the literal appended text at the
   freeze (the frozen pattern is what the counter checks).
2. The refusal ids in `rejects` are read as "must be visible in the Gate reject
   table"; ids that are only *held* (draft: S906/S907/S911) or merely
   superseded must NOT sit in the refusal keys, or the Gate owes them a row.
3. `removed_ids[]` should carry the draft's legacy six (S886/S888/S889/S890/
   S891/S896), or the rewrite's "do not keep them" clause goes ungraded.
4. `map` may stay absent (row_set is the map) or be pinned; if pinned, its blob
   digest must be recorded at the freeze.
5. Scratch: the counter honours `--work`, `$HYAKU_SCRATCH`, an operator
   `$TMPDIR` and otherwise falls back to `/fast/scratch/hyaku/kotodama-r77/counter`
   (r76 shape); it refuses only the system temporary directory. The harness's
   control 3 is bound to claim Ca by default (`--scratch-refusal ca`), matching
   the draft.
