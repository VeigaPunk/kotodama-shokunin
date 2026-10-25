# RevEntryCoupling — dangling-reference audit of the two staged heritage entries (round 72, w1)

Seat: L1Kotodama72.RevEntryCoupling (leaf). Date: 2026-10-25.
Scope: the two heritage-taxonomy entries as they will land, audited against the lane tree at HEAD
(`b60c7b1`, matches claims base). Drafts audited: `/tmp/r72-entries/heritage-taxonomy-models.md`
(canonical) and `/tmp/r72-entries/heritage-taxonomy-models.amend-2026-10-24-r13.md` (amendment),
produced by ExecRenumber. Staged (source) versions: `/home/vgpnk/Projects/shokuknow/merge/
kotodama/knowledge/corpus/knowledge/culture-material/` (read-only). ScribeEntries' final adopted
drafts (`/tmp/r72-entries-scribe/`) were NOT present when this audit closed (11:24Z and later
re-checks); see Residual gaps.

Tools: built-ins only (grep/find/read + lane `tools/check-cited-lines.py`); nothing installed,
pacman untouched.

---

## 1. Coupling/source/ground path check against the lane tree at HEAD

Paths named in the staged entries' couples/sources/ground cells, and in the adopted drafts:

| # | Path (as cited) | Where | At HEAD? | Verdict |
|---|---|---|---|---|
| 1 | `culture-material/material-culture-inference-method.md` | canonical couples + ground | EXISTS (`corpus/knowledge/culture-material/material-culture-inference-method.md`) | OK |
| 2 | `culture-material/era-periodization-models.md` | canonical couples + §4 | EXISTS | OK |
| 3 | `culture-material/calendar-festival-systems.md` | canonical couples (draft), amendment couples (draft) | EXISTS | OK |
| 4 | `synthesis/worldbible-integration-contract.md` | canonical couples + §7 | EXISTS (`corpus/knowledge/synthesis/worldbible-integration-contract.md`) | OK |
| 5 | `culture-material/heritage-taxonomy-models.md` | amendment couples/ground (self-coupling) | not yet at HEAD (lands with this round) | OK if both entries land together (they are in the same admission) |
| 6 | `heritage-taxonomy-models.amend-2026-10-24-r13.md` | canonical §6 | not yet at HEAD (lands with this round) | OK if amendment lands (same admission) |
| 7 | `myth-symbol/calendar-festival-systems.md` | **staged canonical couples** | **MISSING** — no `corpus/knowledge/myth-symbol/calendar-festival-systems.md`; the file lives under `culture-material/` | FIXED in draft → `culture-material/calendar-festival-systems.md` (item 3). Confirm final text has no myth-symbol variant. |
| 8 | `culture-material/calendar-festival-systems.amend-2026-10-24-r10.md` | **staged amendment couples** | **MISSING** — no r10 amend file exists in `culture-material/` (only the base file) | FIXED in draft → base `culture-material/calendar-festival-systems.md` (item 3). Confirm the text no longer cites the r10 amend filename. |
| 9 | "the lane's row S837" | **staged amendment** (gap filled + §N+1) | **MISLEADING** — lane row S837 = BBC Religions "Sikhism: The Five Ks" (`corpus/SOURCES.md` row S837), not the ihchina register | FIXED in am: both spots now say "the ihchina live page" / "this round's fetch". Confirm no S837 remains in final text (draft grep: 0 hits). |

All *draft* couples targets that must already exist at HEAD are verified present. The two
forward references (items 5–6) are safe only if both entries land together; they are one
admission, so no dangling path remains.

## 2. "Gap filled" sweep claim: staged 643-row vs real 797-row registry

- Staged canonical `gap filled` claimed the sweep over **the 643-row registry** returns 0.
- Real registry at HEAD (`corpus/SOURCES.md`, markdown rows `^\| S[0-9]{3} `): **797 rows**
  (counted; matches claim C's "registry (797 rows)" and round-71 spotcheck "registry_count 784→797").
- I re-ran the staged sweep verbatim at HEAD over the real file:
  `grep -inE 'ihchina|非物质|非物質|文化遺産|heritage online|bunka' corpus/SOURCES.md` → **0 matches**.
  The zero-owners result survives at 797 rows; the *number* "643" was stale (pre-round-71 registry).
- Draft fix: canonical `gap filled` now says "at the 797-row registry (re-run 2026-10-25, receipt
  reports/round-72/telemetry/gap-sweep.txt)". **Action:** the receipt file named does not exist
  yet (`reports/round-72/telemetry/` holds only `baseline.txt` + `census-start.txt`); it must be
  produced with that exact name before <lands>, or the citation is dangling (see §5).

## 3. Amendment's round-11/12 references: campaign vs lane rounds

- Our lane's round 11 = typed-pipeline wiring / handoff e2e / ledger recheck (2026-10-17,
  `corpus/lessons/round-11.md`); round 12 = gate-keeper survey and provisional Gate
  (2026-10-17, `corpus/lessons/round-12.md`). Grep over `corpus/lessons/round-11*`,
  `round-12*` and `reports/round-11*`, `round-12*` finds **no** ihchina, CANNOT-ANSWER, §4.3,
  or S837 content. Our lane never probed ihchina in rounds 11/12.
- The staged amendment's ground cell ("round 12's CANNOT-ANSWER §4.3 — the register page was held
  unreachable …"), gap filled ("round 12 recorded … from a single reading of the live page (S837)"),
  and §N+1 ("the live page answered neither round 11's probe nor round 12's gate, and round 11's
  CDX query … returned nothing") all implied our lane ran those probes. Those events belong to the
  campaign mirror's history, not this lane. Adopting the staged text verbatim would state false
  lane history.
- ExecRenumber's drafts remove all three claims. The amendment's §N+1 replacement says only "The
  live page did not answer this round's fetch (connection timed out from the lane host,
  2026-10-25, one attempt, 25 s)" — accurate, dated, and lane-local. Grep of both drafts for
  `round 11|round 12|round-11|round-12|CANNOT-ANSWER|4.3|S837|S863|S867|S967|643` = 0 hits.
- Verdict: the drafts handle the round-11/12 hazard correctly. The `[UNVERIFIED-CLAIM:]`
  flags in ExecRenumber.md (items 1–4) are all removed from the adopted text, not merely annotated.

## 4. check-cited-lines run on the drafts (claim C leg CITEDLINES)

`python3 -B tools/check-cited-lines.py /tmp/r72-entries/heritage-taxonomy-models.md
/tmp/r72-entries/heritage-taxonomy-models.amend-2026-10-24-r13.md` →

```
MULTI-ID /tmp/r72-entries/heritage-taxonomy-models.md:6 S874,S875
MULTI-ID /tmp/r72-entries/heritage-taxonomy-models.md:21 S874,S875
CITED-LINES: 2 finding(s) in 2 file(s)   (exit 1)
```

Two canonical lines carry two distinct S-ids: line 6 (recheck cell) and line 21 (§1 tail
"(S874, S875)"). The leg requires 0 findings. **Fixes (both in canonical):**
- Line 6: split per row and fix cadence — the exec report notes the rows carry different cadences
  (S874 180d / S875 90d) but the draft still says "180d" for both. Rewrite, e.g.:
  `- recheck: 180d — re-open S874's captures (web.archive.org 20200216023423id_, 20261020183948id_) and re-locate the quoted spans; 90d — re-open S875 live and re-locate its quoted spans`.
- Line 21: drop the dual parenthetical (or split across lines). §2/§3/§5 already carry each row's
  id on its own line, so the overview needs none; e.g. end the sentence "Read it as a filing
  grammar, not as ethnography. (S874)" and let §3 carry S875 — or remove "(S874, S875)"
  entirely. Any single line must keep at most one distinct S-id.

## 5. Other references worth pinning before landing

- `reports/round-72/telemetry/gap-sweep.txt` (canonical `gap filled` citation) — **absent now**;
  must exist at <lands> with exactly this name.
- `reports/round-72/telemetry/measures-c.txt` (amendment `recheck` citation) — **absent now**;
  must exist at <lands> with exactly this name.
- Canonical `sources` cell: "each with a located quote in the round-72 lesson Gate" — the lesson's
  `## Gate` (round-72) must carry the two rows' quotes on admission (claim GATE leg); if the
  lesson drafts rename or re-quote, the cell stays valid as long as quotes exist.
- Row-append shape: drafts cite S874 (ihchina, `https://www.ihchina.cn/project.html` —
  parameterless, matching the archived register URL, `?tid=4` dropped) and S875 (bunka,
  `https://online.bunka.go.jp/db/heritages/search`). Neither row exists in `corpus/SOURCES.md`
  yet (verified: no `^| S874 ` / `^| S875 ` rows; next-free ids S874/S875 per regeneration-71
  renumber). The appended rows must carry exactly these URLs, status `mined`, and `used-by` =
  the two entries, or claims leg ROOWS/REPOINTED fails.
- Canonical header: the staged canonical carried a `ground` cell, the draft **omits `ground`**
  (header is source/verified-at/recheck/gap filled/topic/sources/couples/scope/refuses). Claim C
  leg ENTRIES enumerates `ground` in the full header. House style (e.g. `dance-performance-
  movement-codes.md`) has no `ground` (0/31 culture-material entries use it; 11/31 use
  `gap filled`), so this may be a claim-wording vs house-style mismatch — but as written, the
  canonical draft risks the ENTRIES leg. **Fix (minimal):** restore a `ground` cell adapted from
  the staged canonical's ground text (wave-brief fifth scoped domain; no state-published
  classification; header-conformance gap), or have RevClaimsFidelity confirm the claim accepts the
  house-style field set before landing.

## Findings by severity

**High (would fail a claim leg if unaddressed):**
1. Canonical draft lines 6 + 21: MULTI-ID findings → CITEDLINES leg fails. Fix per §4.
2. Canonical draft missing `ground` header cell → ENTRIES leg at risk. Fix per §5.

**Medium (must be produced before landing, else the text dangles):**
3. Telemetry receipts `gap-sweep.txt`, `measures-c.txt` absent now; names must exist at <lands>.
4. Registry rows S874/S875 must be appended with the exact URLs cited, status mined, used-by the
   two entries.
5. Round-72 lesson Gate must carry both rows' quotes.

**Low / already fixed (verify in final scribe text):**
6. Staged `myth-symbol/calendar-festival-systems.md` → draft `culture-material/calendar-festival-systems.md` (exists).
7. Staged `calendar-festival-systems.amend-2026-10-24-r10.md` → draft `culture-material/calendar-festival-systems.md` (exists).
8. Staged "the lane's row S837" (gate Sikhism) → drafts' "the ihchina live page"; all round-11/12
   campaign-history claims removed from adopted text.

## Residual risk / verification gaps

- ScribeEntries' final adopted files were not yet written at audit close; if they differ from
  `/tmp/r72-entries/*`, re-run §1–§4 against them (the two MULTI-ID lines and missing `ground`
  must be checked there too).
- Registry row bytes unobserved (rows don't exist yet); the URL/status/used-by checks above are
  against the drafts and the renumber mapping, not the final appended rows.
- No live-network probing in this audit (sweep and registry checks are local; ExecRenumber and
  Scouts own the fetch evidence).
- The `reg-to-staged.txt` backtick-key quirk (S807`/S812`/S835`) is noted by MutRegistryCollision
  and does not touch the heritage rows (they are absent from that map), so it is not in scope here.
