# ScribeReadmeIndex — round 73 w1 report (claim C README rows + Ca footer pair)

- **seat:** `ScribeReadmeIndex` (scribe, leaf — no dispatch, no background jobs, no peer messages).
- **base revision:** `8841ad3b896a0227674fa0725b818c999118046f`.
- **artifact:** `.ufo/waves/round-73/w1/drafts/readme-rows.md` (23 548 bytes) — the
  ready-to-paste README change set, split into Block A (Ca), Block B (claim C),
  Block C (adjacent repair neither claim permits), with measurements and controls.
- **`corpus/README.md` NOT edited.** Measured before and after:
  `sha256 35e2cf6d07869ffd1bd3d6ec72c7385dc7f62ccbbb04f3fa859d1c164248687b`;
  `git -C . diff --stat -- corpus/README.md` empty. Lane `git status` shows only
  the pre-existing untracked round-72 seat files and the untracked
  `.ufo/waves/round-73/` + `reports/round-73/` trees.
- **No tool installed, no network fetch, no UA record needed.** Python 3.14.8.

## Behavior delivered

1. **Index rows for the two new entries** — derived mechanically by the filed
   sweep's own `topic_of()` (`reports/round-28/readme/sweep.py`, sha256
   `9b2ccac0…cdd3`), i.e. the entry's first `- topic:` block with continuations
   space-joined, wrapped as ``- `<file>` — <topic>``, inserted in filename order
   after `conlang-methodology.md`. Verified byte-equal to the derived strings and
   to the built candidate (`topic_mismatch 0`).
2. **Footer correction (Ca pair)** — the two in-place footer token edits
   (`Total knowledge entries: 243.` → `245.`; `(total 243 files; directory totals
   30/29/36/29/24/95).` → `(total 245 files; directory totals 30/29/38/29/24/95).`),
   an append-only dated correction paragraph carrying **old token → observed
   token → re-derivation command**, plus two drop-in Ca ledger pair objects
   (`P-README-TOTALS`, `P-README-DIRTOTALS`) with argv `observe_cmd`, capture
   regex, `observed_at_base` (run, not assumed), `expected_after`, disposition.
3. **Post-landing count (+2)** — a second dated paragraph moving 245 → **247**
   and `## linguistics/` 30 → **32**, with its commands; plus the `revision: 2.22`
   block every prior landing carries (labelled as a recommended addition, since
   it is not one of the three named items).
4. **Known-gaps bullet** — round-64..67 shape: the new surface, the registry
   append direction (S876 upward, no invented count), the 0-owner pre-state
   (re-measured by me: `find -iname '*conlang-scholarship*'` → 0, topic-grep → 0,
   five-URL registry grep → 0 at 799 rows / tail `S875`), and the four named
   partial-scope neighbours (`conlang-methodology.md`, `naming-systems.md`,
   `phonetics-phonology.md`, `synthesis/conlang-blueprint-template.md`).

## Gates exercised (only these)

| command | result |
|---|---|
| `find corpus/knowledge -type f -name '*.md' \| wc -l` | **245** |
| `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 245`; per-dir 30/29/**38**/29/24/95 |
| `python3 -B reports/round-28/readme/sweep.py` (base) | **exit 1** — `missing_from_index 2`, `header_drift {culture-material: 36 vs 38}`, `totals_line 243`, 2 `footer_findings` |
| `sweep.sweep(candidate-A, root_override=/tmp sim tree)` | **ok False** — 245 rows vs 247 files, same 2 missing rows + header drift; `topic_mismatch 0`, footer/totals green |
| `sweep.sweep(candidate-B, …)` | **ok True** — 247 rows vs 247 files, 0 missing, 0 ghosts, 0 mismatch, 0 drift |
| controls C1–C5 on candidate B | all fail as predicted (paraphrased row → `REWRITE`; second-topic row → `REWRITE`; deleted amend row → `missing_from_index`; reverted totals → `totals_ok False`; reverted footer → `FOOTER_TOTAL`+`FOOTER_DIR_TOTALS`) |
| `tools/check-readme-revisions.py --readme <candidate>` | findings 0, exit 0 (pre-existing `REVISION-ORPHAN` warning only, same paragraph at base) |
| `tools/check-readme-heading.py --readme <candidate>` | findings 0, exit 0 |

The sim tree is `/tmp/ScribeReadmeIndex/knowledge` (245 committed files + the two
staged linguistics files = 247); builder `/tmp/ScribeReadmeIndex/build_candidate.py`.

## Touched surfaces

- Wrote: `.ufo/waves/round-73/w1/drafts/readme-rows.md`, this report.
- Scratch only in `/tmp/ScribeReadmeIndex/` (`build_candidate.py`, `README-A.md`,
  `README-B.md`, `README-A.diff`, `README-B.diff`, `sweep-base.txt`,
  `rev-check.txt`, `head-check.txt`, `knowledge/`).
- Not written: `corpus/README.md`, `corpus/knowledge/**`, `corpus/SOURCES.md`,
  `reports/round-73/claims.json`, `SCORECARD.md`, `LOG.md`, `SKILL.md`,
  `.ufo/state`, the fleet repo, `/home/vgpnk/Projects/shokuknow` (read-only reads
  of the staged entries and staged row file only), sibling lanes, git state/index.

## Findings (the attack surface for the canonical judge)

- **F1** The README is **red at base on four finding classes**, and claim Ca names
  only the totals pair. If Ca's `REPAIR` leg is read as "the README is green", it
  cannot pass at `<lands>` unless the other three are dispositioned.
- **F2 (blocking, for the freeze)** `## culture-material/ (36)` and the two
  missing heritage rows cannot be repaired under Ca's `APPENDONLY` leg ("in-place
  edits permitted only to SKILL.md registry rows and README footer"). Measured:
  fixing only footer text leaves the sweep red; adding Block C turns it green.
  Recommend widening the freeze to "the README's count surface — the footer block
  and the six `## <part>/ (N)` headers", with Block C listed in the ledger.
- **F3** Claim C has **no README leg** — a C landing can ship with no index rows
  and no leg fails, which is exactly how round 72 produced F1 (commit `770100f`
  admitted two culture-material files; the README's last write is the round-71
  commit `75d1675`).
- **F4** `conlang-scholarship.amend-2026-10-23.md` is the lane's **first
  multi-topic file**; `TOPIC_RE` takes the first `- topic:` only (control C2
  confirms), so a first-topic row under-describes it. The sweep-faithful fix is a
  single merged `- topic:` in the landed amendment, not a longer row.
- **F5** Row order (`.amend-…` sorts before its base file) is convention only —
  the sweep does not check order.
- **F6** The two row strings are **provisional**: derived from the staged entries,
  not from `ScribeEntryBase` / `ScribeEntryAmend`'s lane drafts (which did not
  exist at write time). The landing seat must regenerate them with the command in
  §3.2 of the draft; `REWRITE` is the failure signature.
- **F7** Block B's tokens (245 / `30/…`) assume Block A landed first; one commit
  is simpler (243 → 247, `30/29/36/…` → `32/29/38/…`) and keeps Ca `SEPARABLE`
  because the Ca sentences cite no C path and no S-id ≥ S876.
- **F8** Every number is a 2026-10-25 working-tree reading; a later landing moves
  them and would make the correction line a second false statement.

## Peer IRC note (out of scope, no action taken)

Seat `R50ReopenRowS105` sent two messages while this seat worked: a flag that
`corpus/evidence/round50/spans.tsv` offsets for row S105 were shifted, then a
**retraction** of that flag (the `offset` column is the span-block start,
`start = max(0, off − CONTEXT)` with `CONTEXT=80` per `build-spans.py:44,119`;
the −80/−48 delta is the designed window, not drift; all 55 rows re-verified, no
defect; residual is a naming note only). That path does not exist in this lane
(`find . -name 'spans.tsv'` → nothing; no `*round50*` path under the lane) — it
resolves to the sibling lane `chousa-shokunin/corpus/evidence/round50/spans.tsv`
(fleet-wide read-only `find`), so it is neither claim C's nor Ca's surface. No
verification of that flag was attempted by this seat and **no reply was sent** —
this seat's bounds forbid messaging other seats. One read-only listing of the
sibling file did return after the retraction: its `offset` column carries the
values the sender named (`0`, `27507`, `30581`, `30665` …) against capture
sha256 `2197abe2…`, which is consistent with their span-block-start reading; no
offset arithmetic was recomputed here, and the sender's "all 55 rows re-verified,
0 mismatches" is quoted, not measured by this seat.

## Out of scope / not done

- Did not run `reports/round-73/accept-c.py` or the Ca counter (absent at write
  time: `reports/round-73/` held only `claims.json` and `telemetry/`).
- Did not adjudicate any entry, source, row id, or registry content; did not open
  a live URL; did not touch `claims.json`.
- Did not verify the staged entries' topic accuracy — the rows certify
  correspondence to the entry's own `- topic:` text, nothing more.
