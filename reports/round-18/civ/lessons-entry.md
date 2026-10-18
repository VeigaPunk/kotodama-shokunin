# R18-C08 — lessons entry: the round-18 civ-map revision (append-only patch application)

- Seat: R18-C08 (scribe, C-map lane; round 18 — operator loop 2 of 3, build 2 of 4).
  Date: 2026-10-18. Lane `kotodama-shokunin`; declare revision `c66ac3c…`; baseline
  `3dd3754…` (round-17 filed).
- Writes: this file only. No commit, no push; no filed round-8..17 byte touched.
- **NON-CANON**: process lessons for this round's C work; no canon, rights, clearance
  or freshness verdict. The freshness axis-move pause stands.
- Objects: `reports/round-18/civ-map-r18.json` (R18-C01/C02 revision),
  `reports/round-18/civ/patch-apply.md` (builder receipt),
  `reports/round-18/civ/README.md` + `reports/round-18/civ/delta-vs-round16.json`
  (R18-C07), `reports/round-17/civ/map-patch.json`, `reports/round-16/civ-map.json`.

## Lessons

1. **A patch's `from_` check needs the null-encoding rule, or an honest reviewer
   writes a false failure.** `map-patch.json` encodes "the filed row has no
   `evidence_path` key" as `from_.evidence_path: null`. Naive dict equality
   (`row == from_`) fails on all 12 rows because the filed row simply lacks the key;
   the correct assertion treats a null as key-absence (fields compared individually).
   This seat's first delta tool tripped exactly there and was corrected before any
   number was published — any one-liner reviewer should fold the rule in
   (`reports/round-18/civ/README.md` §7 carries the corrected check).
2. **A patch `to` object is not a map row.** The builder's first apply wrote the
   patch `to` objects as rows; `to` keeps `file` at patch-row level, so the 12 rows
   lost their entry key and the round-16 row validator failed with
   `civ-map row #43 names no civilization entry` / `map 82 rows vs 94 corpus entries`
   (near-miss recorded in `patch-apply.md` §1; fixed by `{"file": name, **to}`).
   Lesson: after applying a row patch, re-run the row-entry validator against the new
   file **before** filing — the same class of guard as the assembler `--check`.
3. **"Every transitioned row carries date+command" is a row-text property; measure it
   in row text.** Two patch rows (maya-classic, mesoamerica) carry `command` strings
   that name the repair class but no shell token. The revision covers them with a dated
   `verified_r18` probe string in the row and the full probe list in
   `transition.r18_recheck` — the patch's own `command` bytes stay verbatim. A reviewer
   checking only receipt prose would pass rows whose row text fails the requirement.
4. **Two status vocabularies coexisted in the patch; the revision must pick and record
   one reading.** 11 rows `stale-fixed`, rome `current`, with the patch's
   `label_policy_note` explicitly delegating normalization to the map scribe. The
   round-18 revision applies the labels verbatim and carries
   `transition.terminal_status: "current"` plus `terminal_status_counts` for the
   terminal reading (`patch-apply.md` §6). The claim's moved number
   (`stale-documented 12 → 0`) holds under either labeling — which is why the label
   choice is a recording duty, not a threshold.
5. **Two different "fives" collide on the word *attempt*.** The revision's
   `attempt_row: true` flags the round-16 fixed-type group
   (`inuit`, `maya-classic`, `mesoamerica-primary-sources`, `mongol`, `muisca`);
   the round-17 runner's `attempted` class names `mongol`, `muisca`, `rapa-nui`,
   `rome`, `ryukyu` (no new external locator landed). The two sets intersect at
   `{mongol, muisca}`. Receipts must name rows by filename, not by count; the revision
   defuses the collision by re-probing **all 12** transitioned rows
   (`transition.r18_recheck`).
6. **The revision moved while it was being read.** Observed sha256
   `3020401b…` (10:26:15Z build) → `fabcd3dd…` → `5fb4dd1c…` within ~5 minutes as the
   builder enriched rows (`attempt_row`, `verified_r18`, `transition.r18_recheck`).
   Every pin a scribe states is a **read-time** pin of someone else's moving
   deliverable; the README says so, and a later revision supersedes it without
   invalidating the earlier read (round-15 lesson).
7. **Append-only is provable in two lines, and the revision proves it in its header.**
   `supersedes.unchanged: true` plus `sha256sum reports/round-16/civ-map.json` =
   `07cabb69…` before and after; the delta is then exactly 12 changed / 82 byte-equal
   rows. The 12 transitions are new rows in a new file — the shape to copy for any
   later re-pin (the round-17 patch itself was already written this way: a proposal
   file that refused to rewrite the filed map).
8. **Counting is the sheet *and* the partition.** `ls corpus/knowledge/civilizations/*.md
   | wc -l` → 94 is the sheet count; the row set against the corpus partition (94
   unique names, none missing, none extra) is the second half — the round-16 runner's
   `set(named_entries) != set(entries)` check. A 94 that passes while duplicating a row
   and dropping another is the failure this pairing catches.
9. **Re-verification lives in the map rows, not only in prose.** The builder folded
   each round-18 probe (codes, byte counts, body digests) into the row's
   `transition.r18_recheck`, so the filed revision itself carries the re-verification —
   a reader does not have to trust a separate receipt. The four verifier receipts
   (`verify-1..4.md`) and the auditor receipts (`audit-1.md`, `audit-2.md` — the
   latter a 193-URL on-the-wire re-sweep, 0 demoted, `auditor-ledger.json`) landed
   10:34–10:41Z and independently reproduce the transitions (12 KEEP / 0 demotions;
   18/18 round-17 pins; 12/12 rows equal the patch `to` blocks) — with informational
   findings recorded rather than absorbed (an unlisted `openn.library.upenn.edu`
   000 debt, Wayback/MDPI byte-and-code variance). An earlier 10:33Z sweep found
   none of these receipts yet; receipts arrive after the sweep unless the scribe
   re-polls (lesson: re-poll before the close line).
10. **One computation, two renderings.** The human delta table
    (`reports/round-18/civ/README.md` §2) and the machine delta
    (`reports/round-18/civ/delta-vs-round16.json`) are generated from the same
    row-level computation by the scribe seat, and the builder's own assertions
    (`patch-apply.md` §7) are a second, independent derivation. Two methods converging
    (both `12 changed / 82 unchanged`, both `stale-documented → 0`) is the strongest
    form this measurement has had in the round.

## Limits carried forward

- All probes are point-in-time (2026-10-18, 64-worker wave); bot walls (403/429) and
  the incomplete-TLS chain were re-observed, not worked around.
- No freshness axis-move; coverage receipts only. Entry content was not re-read in
  full; statuses are receipts, not verdicts.
- The round verdict belongs to `python3 reports/round-18/run-validation.py`'s receipt
  and the parent — not written at this seat's close.
