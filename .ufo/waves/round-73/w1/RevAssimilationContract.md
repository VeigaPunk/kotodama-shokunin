# RevAssimilationContract — round 73, wave 1 (kotodama, hyaku run 7)

Seat: leaf reviewer. Scope: the round's assimilation plan (claims.json claim C legs + frontier_step)
against prompt §6 item 10 (kotodama-round-73.md:440-545) and the staged package's own adopt
checklist (shokuknow/merge/kotodama/MERGE-REPORT.md). claims.json untouched (attacked only).
No lsp server answers .md/.json here, so all checks are text/command-based; every number below was
re-run by this seat on 2026-10-25. No tool installs were needed (nothing added; pacman untouched).

## Verified facts (exercised, not assumed)

1. **Slice re-derivation = 21, matches the prompt.** The prompt's awk command over
   `shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` yields **21** data rows for
   kotodama (18 `payload-absent` + 3 prose-class rows S807/S812/S835 whose class cell reads
   "the cited source could not be fetched, so no quote was checked" — 12 words by wc -w).
   Slice file: `.ufo/waves/round-73/assimilation/quarantine-slice` (this seat's re-run).
   The prompt's 2026-10-24 count (kotodama 21) holds at round time.
2. **Wave-4 quarantine-first was round 71's duty and is discharged.** Round-71's prompt predates the
   directive binding; round-72's prompt already carried item 10 (round-72 paths). The round-71
   receipt `reports/round-71/telemetry/quarantine-verdicts.md` verdicts all 21 rows:
   "PRESENT 10 · REFUSED 7 · UNVERIFIABLE 4 = 21" (10 words), "Adoption stays CLOSED" (3 words);
   the 10/6/5→10/7/4 tally defect was corrected in round 72. Round 72 (second round under the item)
   adopted heritage-taxonomy (lane S874/S875). **Round 73 is the third round — adoption is licensed.**
   Claim C's two-entry admission is therefore NOT a quarantine-first violation.
3. **Base/registry state matches the claim's before-leg.** Lane HEAD == base 8841ad3b…; registry
   799 rows, last id S875; 0 `*conlang-scholarship*` files in the base tree; my own sweep of the
   799-row registry for ojs.unito.it / philol.msu.ru / journals.rudn.ru / cyberleninka.ru /
   sanders.phonologist.org returns **0 rows** (the claim's GROUND result is true).
   BUT the cited receipt `reports/round-73/telemetry/gap-sweep.txt` does not exist yet — see G10.
4. **Collisions and the stale round-71 map are as the claim says.** reg-ids 799 ∩ staged-ids 132 =
   17 collisions (S859..S875); none of the theme's staged ids (S881/S882/S892/S893/S901) collides;
   S876..S880 unoccupied. The round-71 map (actual path `.ufo/waves/round-71/assimilation/id-renumber-map.json`,
   NOT reports/round-71/) is arithmetic (+15), built at 797 rows/next_free S874; two of its targets
   (S874, S875) are now live lane rows naming other documents → would be census E03. Supersession
   is required and the claim's COLLCHECK leg is grounded. Guard proof exists in scratch
   (`assimilation/guard-proof/` A1–A3: planted indented collision caught by the 0–3-space pattern,
   empty under a column-zero-only pattern).
5. **The by-document map draft confirms the tentative five.** `assimilation/id-renumber-map-draft.json`
   (ScoutMapIds): S881→S876, S882→S877, S892→S878, S893→S879, S901→S880, each with per-row evidence
   (URL absent from all 799 lane rows; target id unoccupied). It also correctly excludes
   source_already_adopted_by_url rows (staged S863→lane S874, S867→S875, adopted in round 72) and
   lists 4 campaign-id defects: S728 (canonical :11), S769 (amend-23c :14), S806 (amend-24 :42 and
   methodology-amend :17). Lane S728 verified = Qaqet child-directed speech (SOURCES.md:683) — the
   campaign-id defect class is real and the claim's REPOINTED leg catches it.
6. **The two admitted entries cite SIX staged rows, not five.** Staged conlang-scholarship.md cites
   S881, S882 (source lines 4–5; prose also mentions the refused conference paper via stale id S728
   at :11). Staged conlang-scholarship.amend-2026-10-23.md (round-4 S901 section + folded round-3
   section) cites S901 (:4), S892 (:30), S893 (:31), **S894 (:32)**. The tentative map and the map
   draft cover only five — S894 is unmapped. See G1/G2.
7. **S894's document is a quarantine-slice row.** Register S812 = doi.org/10.1017/cnj.2024.21
   (Sowers-Wills, CJL 69(3)) — the same document as staged S894 — round-71 verdict UNVERIFIABLE
   ("DOI now resolves to open metadata/abstract; register gives no quoted span"); no fetch artifact
   for it exists in `.ufo/waves/round-71/assimilation/fetches/`. Staged S910's document (Palgrave
   chapter DOI 10.1007/978-3-032-03277-5_15) = register S827, verdict PRESENT (Crossref metadata).
8. **S894's payload is walled right now.** Live fetch 2026-10-25 of https://doi.org/10.1017/cnj.2024.21
   with browser-shaped UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
   Chrome/130.0 Safari/537.36` → **HTTP 429**, title "429 Too many automated requests from this
   network." (8 words); capture saved to /tmp/RevAssimilationContract/s894-cnj.html (this seat's only
   download; no fleet-root writes). CDX under the DOI lists only two 302 stubs (2024-11-01), no 200
   payload capture; a journal-prefix CDX probe timed out once (inconclusive — the canonical-slug CDX
   probe remains the adopting wave's duty before any 'no capture' ruling, QUALITY 21/22).
9. **Ca before-state facts verified.** `reports/round-72/telemetry/measures-ca.txt` ends
   "ACCEPT-CA-72: FAIL legs=12/12" (3 words) with LEG FAIL REPORTCORR (fleet-rev=MISSING) and LEG
   FAIL REPORTLAST (report-names-lands=False), while SCORECARD.md:1401 asserts "ACCEPT-CA-72 PASS
   legs=12/12 at the measured revision" (7 words) — R2 real. R1 real (git ls-files --others
   .ufo/waves/round-72 → ScoutMergeScan.md, ScribeLesson.md). R3 real (0 SKILL.md rows matching
   accept-ca-70..72/accept-c-70..72). R4 real: `find corpus/knowledge -type f -name '*.md' | wc -l`
   = 245 vs corpus/README.md:732 "Total knowledge entries: 243." — but see G10's path note.
10. **frontier_step checks out where testable.** census-start receipt exists, exit=0 (29 W04
    duplicate-URL warnings, warnings allowed), base named; mistake_to_mine (R2) verified real;
    quality_candidate (QUALITY 22 UA-record clause) is supported by my own 429 measurement;
    considerthese: no such dir in the lane (verified) — the frontier line is correct; the staged
    package has no doctrine/ dir.

## Gaps (numbered, each with its fix)

- **G1 (high — claim C self-contradicts on the S894 branch).** ENTRIES unconditionally admits
  conlang-scholarship.amend-2026-10-23.md, whose folded round-3 section cites S894; REJECTS refuses
  "staged S894/S910 if their payload stays unreachable by ordinary means". Under an unreachable
  S894 the two legs collide: refusing the citing entry makes ENTRIES false and the claim fails as
  declared. Measured today: S894's payload is register-quarantined (S812, UNVERIFIABLE) AND live-walled
  (429 with browser UA; CDX shows only 302 stubs). Fix: make ENTRIES conditional on the S894
  re-ground outcome and declare the fallback explicitly — (a) adopt via a dated Wayback capture of
  the article page if the canonical-slug CDX probe finds one (probe URLs filed per QUALITY 21/22),
  or (b) land the entry without the S894-dependent §N+2 passage and append no S894 row, recording
  the Gate refusal (reason: payload walled 429 + register S812 unverifiable; flip: adopt when an
  openable carrier exists), or (c) re-scope to the canonical entry alone (still ≥1 admit; the amend
  entry refused with flip). Any branch must keep the kill rule's "admitted entries cite no
  un-grounded row" true by construction.
- **G2 (high — the row set and map omit a cited source).** The map draft maps five ids; the adopted
  amend entry also cites S894 (source :32, body §N+2 :47). If the freeze fixes the row set at five,
  the S894 citation dangles and REPOINTED ("every source: line … names a lane id ≥ S876 whose row's
  URL matches") is false. Fix: extend the map by document — S894 → next free lane id (S881 if the
  five stand) — or drop the S894 citation per G1(b); the ROWS leg's "one per source the two entries
  cite" must equal the mapped set (six rows if S894 is kept). Never arithmetic; the URL is the evidence.
- **G3 (medium — register-slice joins unnamed).** The plan never says that one cited document is a
  slice row with a standing verdict: S894 ↔ register S812 (UNVERIFIABLE, round 71) and S910 ↔
  register S827 (PRESENT). Slice rows are "not appendable until hand-checked this round"; for S894
  that hand-check (fetch + own located ≤25-word quote) is the load-bearing step. Fix: name the
  S812↔S894 (and S827↔S910) joins in the GATE/ROWS legs; require the hand-check receipt (probe URLs,
  UA, verdict transition UNVERIFIABLE→PRESENT-with-anchor or refused) in
  `.ufo/waves/round-73/assimilation/` and a verdict line in the lesson Gate + report.
- **G4 (medium — E03/E04 disposition missing).** SCRATCHMIRROR requires `validate --file` exit 0
  before the first append but nowhere states the consequence rule: an E03 (duplicate id) or E04
  (within-scope duplicate URL) finding means refuse that row or supersede per CORPUS.md rule 2 —
  never append past it. Measured today: 0 registry hits for all six cited documents' URLs/DOIs, so
  E04 should not fire — but the rule must be declared, not silently relied on. Fix: add the
  disposition clause to SCRATCHMIRROR (or a dedicated leg).
- **G5 (medium — report-paste obligation missing).** Item 10 requires the round report to paste both
  id lists, the collision count and the renumber map. No claim leg requires it; the artifacts exist
  only as scratch files. Fix: extend COLLCHECK (or add a leg): the report carries reg-ids/staged-ids
  counts (799/132), the 17-row collision list (S859..S875), and the full old→new map.
- **G6 (medium — per-entry PROVINCE/QUALITY gates and re-dating missing).** No leg requires the
  PROVINCE.md scope check or the QUALITY.md bar per admitted entry (the header's `scope` field is
  not that check), and nothing pins the landed entries' `verified-at`/`recheck` to the round-73
  re-ground date — the campaign's 2026-10-23 dates "prove nothing about this lane". Fix: add a leg:
  per admitted entry, a filed scope+quality receipt (or Gate record) and header dates re-stamped
  2026-10-25 from this lane's own re-opens.
- **G7 (low-medium — refusal coverage incomplete).** REJECTS refuses quarantine-citing entries and
  names "naming-systems / calendar / era / verification" as not adopted — omitting the
  worldbuilding-setting-practice and narrative-structure-frameworks families and the cap-skipped
  conlang entries (amend-2026-10-23b/-23c/-24, conlang-methodology.amend-2026-10-24 and
  amendments/conlang-methodology.md). Every non-adopted staged entry needs reason (1–3 cap or
  quarantine) + flip (next round) in the Gate. Fix: extend REJECTS to name all remaining families
  and require per-entry reason+flip rows.
- **G8 (low — COLLCHECK leg imprecision).** The leg reads "collisions file … has zero id tokens for
  the adopted ids" — the actual collisions file is nonempty by design (17 rows S859..S875). Fix: pin
  the path `.ufo/waves/round-73/assimilation/collisions`, state the exact predicate (collisions ∩
  adopted-ids = ∅; adopted ids S876.. absent from reg-ids), pin the stale map's real path
  (`.ufo/waves/round-71/assimilation/id-renumber-map.json`, not reports/round-71/) and the
  regenerated map's filing path, and cite `guard-proof/` A1–A3 as the planted-collision proof.
- **G9 (low — package checklist conflicts unreconciled).** MERGE-REPORT's adopt checklist contradicts
  item 10 at steps 2 (spot-reopen a sample vs re-open every cited source), 3 (append the whole
  SOURCES.append.md — 132 rows — vs cited rows only), 4–6 (all 56 entries vs 1–3); step 1's "the
  lane's SOURCES-PROPOSED.md" is not in merge/kotodama/ (it lives at
  shokuknow/lanes/kotodama/roundN/SOURCES-PROPOSED.md — verified for other lanes' layout). A seat
  following the checklist literally would bulk-append. Fix: one supersession line in the lesson and
  report (item 10 overrides checklist steps 2–4 on sample-reopen/bulk-append/entry-count) and pin
  the round-2/3/4 SOURCES-PROPOSED paths that the stripped recheck prose points at.
- **G10 (low — pending receipts + one path ambiguity).** Not yet filed, though the legs require them
  before data/freeze: reports/round-73/telemetry/gap-sweep.txt (GROUND), reports/round-73/ledger.json
  (Ca LEDGER), reports/round-73/accept-c.py and accept-ca.py (the named counters). These are
  legitimate pre-wave artifacts — flag so freeze does not happen without them. Also the Ca R4 pair
  says "README" while the line lives at corpus/README.md:732 (README.md has no such line): the
  ledger's stated_at must pin corpus/README.md:732 (observed find = 245, verified).

## Residual risk and verification gaps

- The five reachable theme rows (S881/S882/S892/S893/S901) have not been re-opened by this seat —
  the in-round re-ground (own access date + ≤25-word quote) is the adopting wave's obligation; this
  report verifies the plan's structure, not those quotes.
- The S894 canonical-slug CDX probe is unrun here (journal-prefix probe timed out once); a 'no
  capture' ruling may not be issued without it (QUALITY 21/22). My 429 measurement rules the live
  route out for today only.
- The round-71 verdict receipt's REFUSED rows (S779, S787, S792, S814, S816, S817, S786) were taken
  from the committed receipt, not re-fetched; none of them is cited by the two entries round 73
  admits, so no adopted row depends on them.
- Fetch record: one live fetch (doi.org/10.1017/cnj.2024.21, browser UA as above, HTTP 429) and two
  CDX queries (DOI urlkey: two 302 captures 2024-11-01; journal-prefix: timeout). Downloads only in
  /tmp/RevAssimilationContract/. No writes outside my assigned paths; claims.json, the fleet repo,
  shokuknow, and all never-mutate files untouched.
