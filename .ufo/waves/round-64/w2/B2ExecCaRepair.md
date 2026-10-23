# B2ExecCaRepair — Round 64 claim Ca

## Scope and behavior

Worked only in `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecCaRepair/lane`. Changed the copied `LOG.md` and `corpus/LOG.md`. `SCORECARD.md` already carried the round-63 O/C receipt corrections, A=13 B=11 census correction and the three numeric corrections; `reports/round-63/telemetry/revisions.txt` already named the measured revisions; the `REVNAMES` leg already existed in `reports/round-64/accept-ca.py`. Those files were left unchanged.

The new canonical root-log entry identifies root `LOG.md` as canonical and `corpus/LOG.md` as the stray Round-63 log; records dispositions of Round-62 spot-check items 5–7; and records the round-63 pointer, histogram, numeric and separability corrections. The stray log's false attribution of items 5–6 to R63-M2 was corrected.

## Copied gate — final

Command: `python3 -B reports/round-64/accept-ca.py --root /home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2ExecCaRepair/lane`

```text
CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
PTRS PASS score_dead=False stray_dead=False o_fixed=True c_fixed=True
HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
DISPO PASS items5_7=True s687_flip=True s693_kind=True
REVNAMES PASS missing=[]
NITS PASS seat_reports_nit=True w04_nit=True
R63SEP PASS result_cited=True dep_class_named=True
ACCEPT-CA-64: PASS
```
Exit status: 0.

## Lane-base gate — before

Command: `python3 -B reports/round-64/accept-ca.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin`

```text
CANONLOG FAIL r64_at=-1 stray_has_r63=True points_at_stray=False prior_rounds=0
PTRS PASS score_dead=False stray_dead=False o_fixed=True c_fixed=True
HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
DISPO FAIL items5_7=False s687_flip=False s693_kind=True
REVNAMES PASS missing=[]
NITS FAIL seat_reports_nit=True w04_nit=False
R63SEP FAIL result_cited=False dep_class_named=False
ACCEPT-CA-64: FAIL
```
Exit status: 1.

## Full unified diff

Generated with `diff -u` for the five permitted paths. Paths not shown had no differences: `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt`, and `reports/round-64/accept-ca.py`.

```diff
--- lane/LOG.md
+++ copy/LOG.md
@@ -4148,3 +4148,14 @@
 - **Records:** QUALITY criterion 16; lesson `corpus/lessons/round-62.md` (Gate S693 and four rejects; mistakes R62-M1..M5).
 - **Waves:** wave 1 (controls + build) 37 seats; residual falsify call 8 seats (reviewer 7, critic 1); round total 45.
 - **Evidence:** `reports/round-62/telemetry/`; `.ufo/waves/round-62/`; `corpus/lessons/round-62.md`.
+
+## Round 64 — 2026-10-23 (hyaku run 5, attempt 2; calibration repairs)
+
+Canonical log: root `LOG.md` is the canonical lane log going forward. `corpus/LOG.md` is a stray file holding the Round-63 entry; it is not canonical.
+
+- **Round-62 closure items 5–7** (`corpus/lessons/round-62-verifier-spotcheck.md` §5): item 5, `.ufo/waves/round-62/resid/` is the correct directory; the exact receipts are `KotodamaR62.ResidRerunO.md` and `ResidRerunD.md` (the `ResidRerun{O,D}.md` shorthand misnames O). Both receipts remain unchanged. item 6: 28 checks is the builder report's pre-revision-1 capture; 32/32 is the landed-tool selftest evidenced by `KotodamaR62.ResidRerunO.md`; they measure different revisions, not conflicting results. item 7: retain S693 kind `docs` for the online Dictionary.com entry; S692 names the Random House Unabridged Dictionary book. The line-75 dropped “from” remains a cosmetic, meaning-neutral nit. Census W03 S687 was `mined` and unused; disposition selected: `mined` → `queued`. The registry row itself is outside this scoped file allowlist and remains `mined` in this scratch copy pending registry integration.
+- **Round-63 receipt pointers:** the O and C receipts are `reports/round-63/telemetry/final-measures-o.txt` and `reports/round-63/telemetry/final-measures-c.txt`; the dead pointer has been removed from the round-63 correction records. `SCORECARD.md` and the stray `corpus/LOG.md` carry the corrected O/C pointers.
+- **Round-63 tier histogram:** S694–S717 are A=13 B=11. Census command: `git show ff30a205c8d23b35f1ac533740121a955a9fda96:corpus/SOURCES.md | awk -F'|' '/^\|[[:space:]]*S(69[4-9]|7[01][0-9])[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for (k in n) printf "%s=%d ", k, n[k]; print ""}'` → A=13 B=11.
+- **Round-63 numeric corrections:** 47 seat reports landed, not 45; W04 covers 27 duplicate-URL rows, not just S650/S651; the ACCEPT-O-63 dry run had 9 FAIL legs (GEN/ORDER/BOUND/REDIRECT/MALFORMED/GZIP/TRUNC/TIMEOUT/REVIEW), not 6.
+- **Round-63 separability:** re-run printed `SEPARABILITY: 2 findings`, `exit=1`; findings were C→REC via acceptance and O→base via acceptance. The dependency class is a record dependency: the acceptance counters are REC lands, not an inter-claim dependency.
+- **Measured revisions:** `reports/round-63/telemetry/revisions.txt` records the measured revisions for the round-63 receipts, including 8d2041fa (final-measures-c.txt), 38ec1316 (final-measures-o.txt and rev-separability.txt), 0c892ce (census-end.txt), and 80ff34c (the final-measures record).
--- lane/corpus/LOG.md
+++ copy/corpus/LOG.md
@@ -4,7 +4,7 @@
 - **Claims:** O (operability, capability repair under the r62 safety hold) — `tools/reopen-row.py` repaired in place (`dd81fd29`, build seat ExecRepairTool, final sha `0d965ccb`, 1217 lines, mode 755): redirect targets re-validated against the private-host refusal (cross-authority hops refused even under `--allow-private`; <=5 requests per chain; each request counted); malformed registry URLs answer `MALFORMED attempts=0 url=-` with no traceback (exit 1); gzip Content-Encoding decoded (<=64 MiB expansion cap); 4 MiB truncation answered `TRUNCATED` when the quote is absent from the read bytes; new `--timeout SECONDS` per-request wall budget (default 30). ACCEPT-O-63 measured at the round tip (receipt `reports/round-63/telemetry/final-measures-o.txt`). Independent review gate: RevToolA/B/C restated against the landed bytes + residual RevHoldLift, all `VERDICT: NO-OPEN-HIGH-MED`; safety hold lifted per `corpus/QUALITY.md`.
 - C (coverage, sourced) — new entry `corpus/knowledge/culture-material/headgear-head-covering-codes.md` + 24 rows S694-S717 (`corpus/SOURCES.md` 619 → 643). ACCEPT-C-63 measured at the round tip; receipt `reports/round-63/telemetry/final-measures-c.txt`.
 - **Instruments:** frozen at `80d53ff` (rev 0); pre-data revisions, each receipt-forced: accept-o rev1 (RevCounterO: REVIEW substance+markers), rev4 (CtlODoNothing: TOOL X_OK), rev5 (RevToolB/ExecRepairTool: token self-match), rev6 (CtlOShortCircuit: GZIP fixtures padded >1 MiB), rev7 (MutCounterO: token required + remainder scanned); accept-c rev2+3 (CtlCLineScam: NOMARK/anti-dump/HOSTS; CtlCUrlReuse: normalized-URL LINK + anchored 14-digit CAPTURE_RE), rev3 (RevCounterC: locator-byte pin + exact 11 cells). Residuals disclosed: homograph/subset fixtures vs the blind-review ring (CtlCJunkRow), wall-deadline drip distinction (MutToolNeutral), RESTATE 3-overlap floor.
-- **Routed records:** r62 separability re-run (RevSepPost, telemetry/rev-separability.txt); r62 LOG hash-citation append: `25b44b8a` (final measures) and `2ce9d4d1` (records) named here; cosmetic nits per closure items 5-6 recorded in the round-63 lesson (R63-M2) and the r62 lesson left byte-unchanged.
+- **Routed records:** r62 separability re-run (RevSepPost, telemetry/rev-separability.txt); r62 LOG hash-citation append: `25b44b8a` (final measures) and `2ce9d4d1` (records) named here. The prior claim that r62 closure items 5–6 were recorded in R63-M2 was incorrect: R63-M2 concerns stale instrument pins. Round-64 dispositions of r62 closure items 5–7 are in the canonical root `LOG.md` entry; this `corpus/LOG.md` is the stray Round-63 log, not canonical.
 - **Waves:** one v2 wave 69 seats (reviewer 29, scribe 26, mutation-tester 8, executor 2, scout 2, connector 1, critic 1; attack 38/69 = 55%) + residual call 6 (reviewer 6); round total 75. Dead/unproductive seats: ScribeRowS702 (empty scratch; its reviewer drafted and fully verified the row), CtlORedirectEdge/ScoutEntryOwners/ScoutSiblingO/ConnectorOverlap/CriticClaims/ScribeLesson/ScribeCensus (no report landed by round end; named, not rerouted).
 - **Frontier:** census exit 0 at start and end; registry 619 → 643 rows; lesson `corpus/lessons/round-63.md` (Gate S694-S717, mistakes R63-M1..M5); web.archive.org egress intermittency held 7+ rows to named-hold, resolved by L1 retry loop + read-tool corroboration (met-not-passed recorded).
 - **Evidence:** `reports/round-63/telemetry/`; `.ufo/waves/round-63/`; `corpus/lessons/round-63.md`.
```

## Risks and blocker

`corpus/SOURCES.md` is explicitly outside the permitted edit list. Therefore the copied registry still shows S687 as `mined`; the log records the selected `mined → queued` disposition but cannot enact it. The parent must integrate the row-status flip with the registry land. The acceptance leg checks that the canonical log records the disposition, not that the registry cell has changed.

No tool was installed or updated. No builds, tests, linters or formatters were run; the two CA acceptance invocations above were the explicitly requested gate evidence.
