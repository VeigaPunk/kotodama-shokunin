# Round-16 CIV map audit — independent re-derivation, spot-checks, shard and map verification (CIV R16-C10)

- Auditor: map-auditor (CIV R16-C10), independent of the map scribe (CIV R16-C09) and of the C-shards (C01–C08).
- Date: 2026-10-17 (runs 23:28–24:00 local / 2026-10-18T02:28–03:00Z). Lane: `kotodama-shokunin`, HEAD `0ce7714`, claims baseline `16652e8`.
- Object audited: round-16 claim C — the civilizations staleness coverage map (`reports/round-16/civ-map.json`), its underlying shard receipts, and its agreement with an independently re-derived map.
- Read-only audit: no corpus byte, filed round artifact, or shared bookkeeping was modified by this seat. This file is the seat's only write.
- Method, stated before results: (1) I re-derived the coverage map myself, entry by entry, from the corpus and prior-round filed evidence **before** reading any round-16 shard output: per-entry `verified-at` statement class, `(to-verify)` count, round-8/9 freshness-receipt linkage, round-8/9 metadata report rows. (2) I re-ran status evidence for 20 entries myself (in-repo ledgers, report rows, receipt files, digest re-hashes). (3) I parsed every landed shard's receipts and re-verified digest, record, and stale-reason claims. (4) I compared the filed map to the shards and to my derivation, and ran the round's counting command (`python3 reports/round-16/run-validation.py`, 2026-10-17). Every disagreement is a finding (§5).
- Freshness pause respected: no freshness axis-move; every external-source status cited below is carried by dated in-repo receipts from prior rounds or by round-16 shards — none re-established by this audit.

- Counting commands (this audit, 2026-10-17):
  - `ls corpus/knowledge/civilizations/*.md | wc -l` → **94**
  - dated `- verified-at:` statement present in every entry → **94/94, 0 missing** (scan `.scratch/audit-derivation.json`, sha256-recorded scan of all 94 files)
  - `python3 reports/round-16/run-validation.py` (counting command of record): map rows 94, `zero_unstatused` = 1 (map row set == corpus partition), claim C FAIL in both observed runner states — 83 row-level causes (runner of 23:53), then 37 (amended runner of 23:57) (§4)

## 1. Independent derivation (built before reading round-16 shards)

| Evidence class (what the entry's dated statement names) | n | Entries (abbreviated) |
|---|---|---|
| direct-dated-checks | 21 | aegean, africa-primary-sources, ainu, akan, aksum, algonquian, amazigh, amazonia, anatolia-hittite, ancestral-puebloan, arabia, australia, austronesia, balts, benin, china-shang-zhou, japan-heian, moche, rome, ryukyu, siam-thai |
| r8-metadata-3link-sample | 36 | celts … malagasy block (pointer to round-8 `m02`/`m03`; 3 links sampled per entry) |
| r8-metadata-full-sweep | 17 | mamluk … persia-achaemenid block (all cited links status-swept in `m04-civ-58-76.md`) |
| m05-apparatus-only | 15 | persia-sasanian … zapotec-mixtec block (frontmatter/apparatus only) |
| r1-triage-pointer | 3 | bali, byzantium, carthage — no entry-level dated inspection; latest dated inspection is round-1 triage Z04/Z05 |
| restated-indirect | 1 | burma — verified-at restates the bundled trio line (which does carry the date) |
| vacuous-bare-date | 1 | mali-songhai — `verified-at: 2026-10-17` with **no statement**; qualifier lost when the round-9 admit (`9dc18ec`) split the original combined triad line (per `m04-civ-58-76.md`: "mali-songhai already conformant (combined line)") |

Freshness-receipt linkage (on disk): round-8 receipts → 9 entries; round-9 escalated receipts → 3 of them (mesopotamia-sumer-akkad, anatolia-hittite, levant-canaan-phoenician). `(to-verify)` open marks range 0–16 (vietnam 16, zimbabwe-shona 16, igbo 13, malagasy 13) — debt markers, not staleness verdicts.

My pre-shard prediction was 89–90 current / 0–1 stale-fixed (africa-primary-sources' [RAI] correction) / 3–5 stale-documented (bali, byzantium, carthage, mali-songhai, burma). **The filed map disagrees on 17 labels, zero of them on evidence** — see §4/§5 (F-AUD-1).

## 2. Independent spot-checks re-run by this auditor (20 entries; requirement ≥10)

| Entry | Class | Evidence I re-ran in-repo | Result |
|---|---|---|---|
| bali | r1-triage-pointer | `corpus/lessons/round-1-triage/Z04.md` line 6 = `- date: 2026-10-17`; batch lists bali | reproduce |
| byzantium | r1-triage-pointer | `Z05.md:3` = `- round: 1; batch: Z05; date: 2026-10-17.`; `LOG.md:218` carries the Z05 heading | reproduce |
| carthage | r1-triage-pointer | Z05 rows: Krahmalkov 2000 scan fetched/text-searched (`brrm` Byb 13.3, `ḥbl` CIS I 3189.3); Hurst–Stager 1978 open copy checked; stale-DOI quirk noted inline | reproduce |
| africa-primary-sources | direct + fix | inspection-boundary line at the cited "line 23"; `[RAI]` pp. 65–71 inspected; §11 corrected locators pp. 72–86 present | reproduce |
| mali-songhai | vacuous | header: bare `verified-at` (no statement); `m04` sweep row = 21 links / 18 live / 3 non-live; Stoller profile line dated 2026-10-17 (entry L195) | **anomaly confirmed** (F-AUD-2) |
| burma | restated | bundled trio line exists (`- source: …; verified-at: 2026-10-17; recheck: …`) + standalone restatement (L6) | reproduce |
| celts; chimu; egypt-ancient | r8-3link | `m02-civ-20-38.md` rows + per-file digest lines (celts L26/L52 `aa0e8a4bd35da08d`; chimu L27/L53; egypt L35/L61) | reproduce |
| mesopotamia-sumer-akkad | r8-sweep + fresh8/9 | `m04` row 14/11/3 with the two 429s (L117–118); R8-F01/F02 and R9-F01a-c/F02a-c entry-linked; today's `sha256sum` = `bf6c92f9…` equals the receipts' recorded hash | reproduce |
| nubia-kush | r8-sweep + fresh8 | `m04` row 9/9/0; R8-F14/F15 entry-linked | reproduce |
| etruria | r8-3link + fresh8 | m02 rows; R8-F13 entry-linked | reproduce |
| china-shang-zhou | direct + fresh8 | verified-at names accessible translations/institutional records; R8-F07/F08 entry-linked | reproduce |
| anatolia-hittite | direct + fresh8/9 | Fulcrum inaccessibility documented in-entry (verification-boundary section); R8-F03/F06, R9-F03a-c entry-linked | reproduce |
| levant-canaan-phoenician | r8-3link + fresh8/9 | m03 row; R8-F04, R9-F04a-c entry-linked | reproduce |
| persia-achaemenid | r8-sweep + fresh8 | `m04` row 15/12/3; R8-F11/F12 entry-linked | reproduce |
| rome | direct + r9-pointer | `- source:` pointer names `reports/round-9/metadata/v05-civ-77-94.md`; v05 records rome "already conformant, no diff", digest `f0b2747c5afe92bc`; today's `sha256sum` equals it | reproduce |
| vietnam | m05-apparatus | `m05-civ-77-94.md:29` (added 2 fields, §"Source ledger and calibration"); anchor exists (entry L9); 16 open marks | reproduce |
| tibet | m05-apparatus | `m05:27` (§10 "Provenance cautions and stop rules"); anchor matches verified-at text | reproduce |
| ainu | direct-dated-checks | 3 × `accessed 2026-10-17` in-entry (AMNH, NMS, Upopoy), exactly as verified-at names | reproduce |
| japan-heian; mamluk; maya-classic; mesoamerica-primary-sources; persia-sasanian | byte-identity legs claimed by shards C05/C06/C07 | `sha256sum` re-run today: all five equal the shard-claimed digests (`137f603a…`, `28d61088…`, `d3520973…`, `6d40a97d…`, `9d0a65e3…`) | reproduce |

Digest re-hashes run by this auditor: **8/8 exact matches** against round-16 shard claims (japan-heian, mali-songhai, mamluk, maya-classic, mesoamerica-primary-sources, rome, persia-sasanian, mesopotamia-sumer-akkad).

## 3. Round-16 shard receipts: parsed and verified (7 range shards + C01)

Statuses extracted from each shard's machine-readable block or status table:

| Shard file | Entries | current | stale-documented | External fetches this round | Stated standard |
|---|---|---|---|---|---|
| 001-012 (C01) | 12 | 12 | 0 | per its fragments | prose receipts (fragment restructured in-flight, see F-AUD-6) |
| 013-024 (C02) | 12 | 12 | 0 | yes (per-entry code/bytes) | current = in-repo record **and** ≥1 live refetch |
| 025-036 (C03) | 12 | 12 | 0 | yes (URL samples with codes) | digest + gate + frontmatter + couples + sample |
| 037-047 (C04) | 11 | 10 | 1 (inuit 44) | no (carries round-8 sample statuses) | header 6/6 + digest + dated sample receipt |
| 048-059 (C05) | 12 | 12 | 0 | **0** | byte-identity anchor + dated in-repo record |
| 060-071 (C06) | 12 | 8 | 4 (maya-classic 61, mesoamerica 62, mongol 67, muisca 68) | **0** | hard-fail (000) URLs unre-attempted ⇒ stale-documented; 403/429 = bot walls, not rot |
| 072-083 (C07) | 12 | 5 | 7 (persia-sasanian 77, polynesia-navigation 78, rapa-nui 79, rome 80, ryukyu 81, scythian-saka 82, siam-thai 83) | **0** (none, freshness pause cited at `LOG.md:3028`) | stale-documented = no dated URL-status receipt exists in-repo (absence, not breakage) |
| 084-094 (C08) | 11 | 11 | 0 | **0** | apparatus + digest |

Stale-reason verification — every filed `stale-documented` reason re-run by this auditor:
- **inuit (44)**: round-8 sample 404 receipt exists — `m03-civ-39-57.md:67` (Dorais 2010 PDF → 404). Reproduce.
- **maya-classic (61)**: `grep -in 'sacbe\|causeway\|white road' corpus/knowledge/civilizations/maya-classic.md` → **0 hits** (my re-run), while `culture-material/transport-mobility-lexicon.md:20` couples line names `civilizations/maya-classic.md (sacbeob)`; original finding `round-10/coverage/review-C08.md:182` (N2). Reproduce.
- **mesoamerica (62) / mongol (67) / muisca (68)**: `m04-civ-58-76.md:80` documents exactly 9 × 000 hard failures (retried once); L224 names muisca's `muysca.cubun.org` as 4 of the 9 and the entry's main lexical host; the shards' per-entry lists (3/1/4) partition those 9. Reproduce.
- **C07's seven rows**: negative claim ("never URL-status-swept in-repo") tested by me against rounds 5–15: `m04` sweeps 58–76 only; `m05`/`v05` are apparatus audits without URL statuses; round-5's dated access attempts (`14-source-review.md`) touch slavs-early/sogdian-silk-road/tibet/turkic-steppe — all in C08's range, none of the seven. Negative claim survives.

Cross-checks that passed: shard digests vs today's files (8/8); digest anchors vs round-8/9 recorded after-digests (celts/chimu in `m02`; rome/persia-sasanian in `v05`; zero corpus drift since the round-9 admit `9dc18ec`, corroborated by my own `git log` on the corpus path); receipt→entry linkage for 12 round-8/9 receipt files spot-opened.

## 4. The filed map: count, coverage, integration, and validator state

`reports/round-16/civ-map.json` (built 2026-10-18T02:52:19Z by CIV R16-C09), verified by this auditor:

- **94 rows; file set == corpus partition exactly** (set-equality and no duplicates re-derived by me; map `count: 94`; validator `zero_unstatused` = 1). Statuses: **82 current / 12 stale-documented / 0 stale-fixed** — integrating the eight shards 1:1 (12+12+10+1+12+8+4+5+7+11 = 82; 1+4+7 = 12). No entry invented, none missing.
- **Agreement with my derivation**: zero evidence-level contradictions. The 17 label disagreements (map-stale 12 vs my-predicted-stale {bali, byzantium, carthage, mali-songhai, burma}; zero overlap) each trace to a stated-but-divergent shard standard, not to a factual error — the r1-triage trio was upgraded to current by this round's live re-fetches (a stronger result than my prediction), while 12 entries I could have called current were marked stale-documented under stricter, stated rules (F-AUD-1).
- **Defect 1 — 12 dangling evidence paths (F-AUD-6):** rows for entries 1–12 point at `reports/round-16/civ/001.md` … `012.md`, which **do not exist**; C01's evidence actually landed as the single consolidated file `reports/round-16/civ/001-012.md` (mtime 23:52 local). The map's `shards` registry likewise pins twelve sha256s (`ab2c05ef…` … `3aa3f53c…`) for those twelve nonexistent files. The other seven registry hashes match disk byte-for-byte (my re-hash: 7 match / 0 mismatch). The map's own `complete: true` and `unreceipted: []` therefore overstate the filed state: 12/94 rows have status but no resolvable evidence pointer.
- **Defect 2 — rows lack the claim's date+command (F-AUD-5):** every row is `{file, status, evidence_path}` only. The claim's `after_required` and the counting command both require a current status to carry "date+command". Two validator states were observed during this audit (the runner was amended concurrently — see F-AUD-8):
  - **Run 1** (runner mtime 23:53, row-text check): claim C FAIL with **83 failures** = 82 × "status 'current' lacks a date matching this round and a command" + 1 × "No auditor artifact found … spot-checking >=10 entries".
  - **Run 2** (runner mtime 23:57, evidence-file text check): claim C FAIL with **37 failures** = 12 × dangling `evidence_path` "not a file in the repo" (the C01 dozen — Defect 1, now harness-confirmed) + 12 × current rows (the same dangling dozen) still lacking date+command + 12 × stale-documented rows lacking an in-row named reason + 1 × auditor-artifact absence. The 70 current rows whose evidence files exist now pass via their evidence text — the map's indirection was accepted for those, but cannot be checked for the 12 dangling rows.
- **Auditor leg:** both runs record `entries_spot_checked: 0`. This file is a genuine independent, dated, command-carried audit naming 20+ entries (§2), but the 23:57 runner restricts the auditor scan to artifacts **outside `civ/`**, while this seat's assigned output path is `reports/round-16/civ/map-audit.md` — the two are incompatible (F-AUD-8). Until the parent resolves the location, the auditor leg stays unmet by my assigned artifact.
- Claim O's FAIL in the same runs ("amended keyed packet build" missing) belongs to the fixer lanes' dependency, not to claim C; noted here only so the parent does not conflate the two.

## 5. Findings

**F-AUD-1 (process, cross-shard): the status vocabulary is shard-relative, not fleet-uniform — four operational definitions of the same labels.** `current` under C02 = in-repo record **and** live refetch; under C03 = digest+gate+sample; under C05/C06/C08 = in-repo verification only (zero external fetches); the claim's own text ("re-fetched **or** verified in-repo") supports the OR reading, so the stricter variants are legitimate — but the map rows carry no per-row standard, so a reader cannot tell that rome's `stale-documented` (no dated URL-status receipt exists anywhere) is a different kind of claim from muisca's (4 cited URLs hard-failed and unre-attempted). Concrete inversion produced: **rome** (deep in-entry verification record) is stale-documented while **mali-songhai** (vacuous one-word receipt) is current — evidence strength runs the opposite way. 403/429-vs-404/000 handling is principled but shard-local (C02 availability notes with control probes; C06 routes only 000s; C04 routes a sample-404). Remedy: map rows should carry the shard standard (or a normalized `basis` field) alongside the status.

**F-AUD-2 (entry-level, pre-existing): mali-songhai's receipt is the weakest of the 94** — bare `verified-at: 2026-10-17`, no statement, after the round-9 header split (`9dc18ec`) dropped the qualifier of the original combined line; its `current` status rests on byte-identity + the r9 normalization record (defensible, but the row must not look identical to C02's two-leg rows). Corpus fix is a one-line entry edit — outside this audit's write scope; owner: a C-shard follow-up or round-17 hygiene.

**F-AUD-3 (schema): shard machine blocks are heterogeneous** — key spellings (`tally` vs `statuses` vs `counts`; `stale-fixed` vs `stale_fixed`), C05's fenced block carries no rows (statuses in a table), C04 has no fenced block at all, evidence field names vary (`refetch` / `basis` / `record`). The map normalized the statuses correctly; the residual burden is per-row evidence carriage (F-AUD-5).

**F-AUD-5 (map defect): map rows carry no date+command.** Rows are `{file, status, evidence_path}` only. Under the 23:53 runner this failed all 82 `current` rows; under the 23:57 runner the 70 rows with existing evidence files pass via their evidence text, but the 12 dangling-path rows (F-AUD-6) still fail, and the claim's own "with date+command" wording is met only by indirection. The information exists in the evidence files; the map should surface it per row (e.g., `checked: "2026-10-17 via <command>"`) — owner: map scribe C09 via a corrected map build. Not fixable by this seat (write scope).

**F-AUD-6 (map defect): 12 dangling evidence paths + 12 dangling registry hashes.** Entries 1–12 point at `civ/001.md`–`012.md`; the landed artifact is `civ/001-012.md`. The seven range-file registry hashes match disk exactly, so the fix is mechanical: repoint the 12 rows at `001-012.md` (or have the C01 seat emit the twelve per-entry files it originally hashed) and re-pin the registry. Until then `complete: true` / `unreceipted: []` overstate coverage. Owner: map scribe C09 with C01; not fixable by this seat.

**F-AUD-7 (harness hole, for the record): the validator's auditor-detector cannot distinguish an independent auditor from a shard fragment.** Run 1's `civ_auditors()` scanned all of `reports/round-16/**`: the C02 shard file (`013-024.md`, which says "Claim audited" and names 12 entries) would have satisfied it — author-side evidence passing as independent audit. The 23:57 runner revision responds by excluding `civ/` entirely (failure text now reads "outside civ/"), which closes the hole but also excludes this seat's assigned artifact path (F-AUD-8). A durable rule needs to distinguish *who* wrote a file, not just *where* it sits.

**F-AUD-8 (routing conflict + moving harness): the runner was amended during the audit window, and its new auditor location rule excludes this seat's assigned output path.** `reports/round-16/run-validation.py` changed between my two runs (mtime 23:53 → 23:57, sha256 differs), adding the evidence-path existence check and the `outside civ/` auditor restriction while I was auditing. The auditor leg now requires an artifact directly under `reports/round-16/` (not `civ/`), but my seat assignment pins `reports/round-16/civ/map-audit.md` — which I wrote and will not duplicate outside my write scope without authorization. Parent options: (a) amend the detector to accept the assigned `civ/map-audit.md` (it is verifiably independent of C01–C09), or (b) authorize a pointer/copy at `reports/round-16/map-audit.md`. Also note for the integrator: a validator that changes mid-round makes cross-run failure counts incomparable; both states are pinned above.

**Positive results, for the record:** (a) 94/94 entries carry dated in-repo verification statements — the claim's "zero entries without a status" has a real evidence floor; (b) all 12 filed `stale-documented` reasons reproduce from named in-repo anchors (§3); (c) zero corpus drift since the round-9 admit is corroborated independently of the shards (my 8 re-hashes; `git log` on the corpus path); (d) the map's row set, statuses, and 7/8 registry hashes integrate the shards faithfully; (e) the round-16 live re-fetches of the r1-triage trio (bali/byzantium/carthage) legitimately upgrade those rows over my pre-derivation — the map's coverage is *stronger* than my prediction there, not weaker.

— CIV R16-C10, map auditor, 2026-10-17. Spot-check evidence commands: `grep`, `sed -n`, `sha256sum`, `git log/show`, `python3` (json parsing), `ls`; all runs dated 2026-10-17 local in this lane.
