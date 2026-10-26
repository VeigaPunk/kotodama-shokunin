# Round 16 — lessons C09: the 94-entry civilizations coverage map, built from C-shard receipts

source: `reports/round-16/claims.json` (claims C and O); `reports/round-16/targets.json` (8 C-shards, 1 map-scribe, 1 map-auditor); `corpus/lessons/round-15.md`; `corpus/lessons/round-14.md:84-86`; `reports/round-11/claims.json:31`; `AGENTS.md`.
verified-at: opening census 2026-10-18T02:30:37Z (UTC, `date -u --iso-8601=seconds`; lane-local date 2026-10-17). All later observations carry their own UTC stamps.
scope: C09 writes only `reports/round-16/civ-map.json` and `corpus/lessons/round-16.md`. Filed artifacts of rounds 8-15 are read-only; corrections land as new files. This is a **coverage map, not a freshness axis-move** — the round-11 freshness pause stands (`corpus/lessons/round-14.md:86`: "preserve round-11's rejection and the existing pause on freshness axis-move claims"; restated `corpus/lessons/round-15.md:71`; round-16's own shards cite it at `LOG.md:3028` / `SCORECARD.md:201-205`). Every status in the map is a receipt of *which shard evidence covers which entry*, never a freshness-threshold claim. All round-16 artifacts are NON-CANON.

## Opening census (commands + dates)

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```sh
ls corpus/knowledge/civilizations/*.md | wc -l      # 94 at 2026-10-18T02:30:37Z
git rev-parse HEAD                                   # 0ce77140bf64eec6517631c8d5af0521488d6e84
git log --format='%h %cI %s' -1 16652e822e9dd5d83f7ab9e6078cbf010fc8f7e6
```

- Count command returned **94** at the census (`.scratch/c09-census.txt`); re-asserted **94** at map build time (2026-10-18T02:52:19Z).
- HEAD `0ce7714` is the round-16 declaration commit ("round-16: declare GLM-2 claims C/O (civ-map, routed harness fixes)", 2026-10-17T23:28:06-03:00); the claims' `baseline_revision` `16652e8` verified as the round-15 admission commit ("round-15: admit O/D — handoff v2 closes semantic reject…", 2026-10-17T23:27:05-03:00). At the census the round-16 tree held exactly `claims.json` + `targets.json` (`git ls-files reports/round-16`); `LOG.md`/`SCORECARD.md` had zero round-16 mentions (grep, census date).

## Dependency wait (C-shard receipts)

The map cannot be built from nothing: statuses must come from shard bytes, not from this seat's own reading of 94 files (that would fabricate coverage the shards were dispatched to produce). C09 polls `reports/round-16/civ/` every 60 s, 20-poll cap (`.scratch/c09-poll.log`).

- **Threshold (≥7 shards) met at poll 17, 2026-10-18T02:46:37Z** (`poll=17 shards=7`): range shards `013-024.md` through `084-094.md` (positions 13–94).
- C01 (positions 1–12) then landed **incrementally as one file per entry** — `001.md`…`012.md` — first three at 02:50:46Z, all twelve by 02:52:14Z (`.scratch/c09-c01b-poll.log`, `files=19` at poll 2 of the second poller).
- Total dependency wait: census 02:30:37Z → complete shard set 02:52:14Z (~22 min), inside the poll budget; the map was built at 02:52:19Z against the complete set.

## Map craft rules (what made the map auditable)

1. **Statuses are receipt-backed only.** The three statuses admitted are the claim's own vocabulary — `current`, `stale-fixed`, `stale-documented` (`reports/round-16/claims.json`, claim C after_required) — the same verdict set round-10's drift ledger used (`reports/round-10/drift/ledger.json`, `round10_verdict` values). A fourth status (`unreceipted`) exists only for the incomplete-build fallback; it was **not used** — the final map is complete.
2. **Conflicts abort, they are not merged.** If two shards receipt the same file with different statuses, the build fails loudly and names both shards; a scribe does not pick a winner. No conflict occurred (19 shards → 94 unique files, zero double-receipts).
3. **`evidence_path` names the shard, not the scribe.** Each entry's evidence points into `reports/round-16/civ/<shard>` so the auditor's independent ≥10-entry spot-check can go straight to the bytes. All 94 evidence paths verified to exist at build time.
4. **The map pins its inputs.** The build embeds each shard's SHA-256, parsed-receipt count, and detected format, plus `git_head_at_build` (`0ce7714…`), so a later revision of a shard cannot silently change what the map was built from (round-15 lesson: moving bytes are superseded only by new dated receipts, never silently inherited).
5. **The count is re-asserted at build time, not inherited from the census.** `ls corpus/knowledge/civilizations/*.md | wc -l` must return 94 when the map is written; a build against a moving partition is refused.
6. **Four shard dialects, one parser, zero guesses.** The eight C-shards used four receipt layouts: fenced ```json blocks (C02, C03, C06, C07, C08 — list rows or a counts-vs-slug `statuses` dict that must be told apart by key shape), receipt tables (C04: status as last cell, bolded; C05: status in column 3), and one-receipt-per-entry prose files (C01: `- entry:` + `- **status: current**`). Parser rules: fenced-JSON first, then prose, then tables; a table row receipts an entry iff it names exactly one known filename and exactly one status token (scope-list rows carry no status and are skipped); ambiguity or an unknown status aborts the build. Every abort fired during development matched a real dialect difference, and none was bypassed by relaxing the status vocabulary.
7. **Position tiling verified.** Each shard's receipts map to contiguous positions of the sorted 94-file list; the union tiles 1–94 with no gap and no overlap (checked programmatically before the build was allowed to write).

## Map result (all counts carry the build date 2026-10-18T02:52:19Z; `python3` over `reports/round-16/civ-map.json`)

- **94/94 entries carry a status receipt** — `{"file", "status", "evidence_path"}` exactly, files unique, count field 94, `complete: true`.
- **Distribution: 82 `current`, 12 `stale-documented`, 0 `stale-fixed`, 0 without status.** `stale-fixed` is 0 everywhere because no shard was dispatched to edit corpus entries (coverage receipts, not repairs; freshness pause in force).
- The 12 `stale-documented`, with their shard-named reason classes (each row's full reason lives in the cited shard):
  - `inuit.md` ← `037-047.md` — one dead citation locator stable across three independent samples since round 8 (round 8 named the fix and its owner; a content-round edit, out of a coverage shard's scope).
  - `maya-classic.md`, `mesoamerica-primary-sources.md`, `mongol.md`, `muisca.md` ← `060-071.md` — named, in-repo-verifiable debts: a couples pointer whose subject is absent from the entry (reproduced by grep this round), hard-fail (000) URLs unre-attempted since round 8 (muisca's four include its main lexical host), plus a round-11 pin-drift note explicitly scored as verdict-neutral.
  - `persia-sasanian.md`, `polynesia-navigation.md`, `rapa-nui.md`, `rome.md`, `ryukyu.md`, `scythian-saka.md`, `siam-thai.md` ← `072-083.md` — **absence of a dated URL-status receipt** ("none exists — never URL-status-swept in-repo; freshness pause defers the sweep"). That shard states plainly: "the stale-documented reason is *absence of a dated URL-status receipt*, not evidence of breakage; no link in these 7 entries is claimed dead or live here."
- Same vocabulary, three distinct reason classes. A future reader of the map must not collapse "dead link documented" (C04/C06) into "never receipted" (C07); the `evidence_path` per entry is what keeps them distinguishable. If a later round aggregates these rows, it should carry the reason class, not just the count 12.

## Lessons for the next coverage pass

1. **Dispatch should pin the receipt format, not just the threshold.** Four dialects from eight workers in one lane, one of which (C01) landed as twelve files against an expected filename pattern that never existed — the map scribe's first two parser designs aborted on real bytes three times before the fourth covered all of them. A shared one-line format contract in `targets.json` (e.g. "one fenced ```json block with `entries: [{file, status}]`") would have made the build a five-minute step instead of a dialect-archaeology dig.
2. **"Map-scribe input" blocks work.** The shards that embedded an explicit machine-readable block (C03's §6, C06's §4, both labeled "map-scribe input") parsed first-pass and carried the richest per-entry provenance (sha256, prior receipts, debt strings). The pure-prose and pure-table shards parsed fine but forced the scribe to trust transcription; the embedded-JSON pattern should be the fleet default for aggregation seats.
3. **A counts-dict and a slug-dict both read as `"statuses": {...}`.** C03's machine block carries `"statuses": {"current": 12, …}` (tally) while C05's carries `"statuses": {"japan-heian": "current", …}` (per-entry). A parser that accepts the second shape must key on the values (or require `.md` keys), or it will ingest a tally as twelve bogus receipts. Caught only because the build refuses statuses outside the claim vocabulary.
4. **Per-entry incremental delivery beats monolithic shards for latency.** C01's twelve small files let the scribe see progress and test the dialect early; the seven range shards each arrived as one large write after ~15 minutes of silence. For a 94-entry partition, 12×small beat 1×large on every axis except file count.
5. **The auditor should sample across reason classes, not just across shards.** The 12 stale-documented rows split 1 + 4 + 7 across three distinct reason classes; a ≥10-entry spot-check drawn uniformly from the 94 could land entirely in the 82 `current` rows and never exercise a single named-reason receipt. Draw stratified: at least one row per non-current reason class.
6. **Coverage receipts about verification debt are not link-rot verdicts.** The C07 rows in particular must never be quoted as "7 entries with dead links"; the shard's own sentence (quoted above) is the correct citation form. This is the same discipline round-14 pinned for the freshness ratios: write the population you actually measured.

## Boundary record

All reads read-only; writes confined to `reports/round-16/civ-map.json` and `corpus/lessons/round-16.md` (plus `.scratch/` working files, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`; builder script `.scratch/c09-build-map.py`). No git commit/push. No freshness threshold moved, no canon or rights ruling made; the freshness pause stands, and the map's `current` statuses inherit each shard's own definition (in-repo verification or sample-level liveness, never claim-level re-verification of external truth). Admission of claim C belongs to the assigned runner (`python3 reports/round-16/run-validation.py`) and the round auditor — never to this map. Independent spot-check (≥10 entries, stratified per lesson 5 above) is the map-auditor seat's pending half of the claim.
