#!/usr/bin/env python3
"""Writes the DRAFT round-74 claims (pre-data, not frozen). Output: reports/round-74/claims.json"""
import json
LANE="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE="f7104cbce186bc2e1522abf0cfd619cc834628bb"
C={
 "round":74,
 "status":"DRAFT — not frozen; wave-1 seats attack it; frozen by the commit that adds the final claims.json together with ledger.json, both counters, the do-nothing controls and the junk-landing controls; no seat scores landed data before then. A rule changed after any seat scores landed data is not the claim's rule.",
 "frozen":None,
 "base":BASE,
 "axes_note":"Lowest-axis obligation: SCORECARD holds no numeric scores (SCORECARD.md:13-15); freshness axis-move claims are paused under the open L0 row `kotodama | round-11` (/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47). The round works calibration (round-73 closure routed defects 1-5) and coverage (assimilation). No stagnation-nudge waiver is claimed.",
 "pre_data_corrections":[],
 "claims":[
  {"id":"C","axis":"coverage","kind":"assimilation-sourced",
   "title":"shokuknow assimilation: worldbuilding-setting-practice theme (CJK practitioner craft), two entries on uncovered ground",
   "before":f"at base {BASE}: (a) `find corpus/knowledge -iname '*worldbuilding-setting*' | wc -l` = 0 (README names worldbuilding only as a method label on other entries); (b) the 804-row registry (`grep -cE '^ {{0,3}}\\|[[:space:]]*S[0-9]{{3,}}[[:space:]]*\\|' corpus/SOURCES.md` = 804, last id S880) holds 0 occurrences of litmemo.com, tuduku.space, chinawriter.com.cn; (c) 0 knowledge files contain 設定ノート, 世界観 or 世界观 (`grep -rlE '設定ノート|世界観|世界观' corpus/knowledge | wc -l`).",
   "after":"`python3 -B reports/round-74/accept-c.py --root . --lands <lands> --freeze <freeze>` prints ACCEPT-C-74: PASS legs=<n>/<n> (n fixed at freeze). Adopted staged->lane map by document (committed pre-data at .ufo/waves/round-74/assimilation/id-renumber-map.json): staged S883->S881 (litmemo.com/ja/blog/novel-worldbuilding-guide); S884->S882 (tuduku.space/column/novel-worldbuilding); S899->S883 (chinawriter.com.cn/n1/2025/0605/c404024-40494534.html); S900->S884 (chinawriter.com.cn/n1/2022/1207/c404024-32582252.html); staged S882 is NOT appended: its document already holds lane row S877 (philol.msu.ru conlangs.pdf), cited by the base entry, S877's used-by changed in place old->new and logged.",
   "row_set":[{"id":"S881","staged":"S883"},{"id":"S882","staged":"S884"},{"id":"S883","staged":"S899"},{"id":"S884","staged":"S900"}],
   "reused_rows":[{"id":"S877","staged":"S882","note":"in-place used-by change only"}],
   "entries":["corpus/knowledge/culture-material/worldbuilding-setting-practice.md","corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md"],
   "rejects":{"refused_staged_not_appended":["S882"],"forced_new_quotes":["S899","S900"],"refused_files":["narrative-structure-frameworks (base + 4 amendments; staged S870 refused round 72)","naming-systems x11","calendar-festival-systems x3","era-periodization-models x2","verification x9 amendments","conlang-scholarship.amend-2026-10-23b/-23c/-2026-10-24","conlang-methodology.amend-2026-10-24"]},
   "ground":{"fragments":["litmemo.com","tuduku.space","chinawriter.com.cn"],"cjk_terms":["設定ノート","世界観","世界观"]},
   "legs":[
    "ENTRIES: both entries exist at <lands>, absent at base, with the provenance header (source/verified-at/recheck/ground/topic/gap-filled/sources/couples/scope) first, no placeholder values, and a body at least as long (in words) as the smallest corpus/knowledge entry at base",
    "ROWS: the registry diff base..<lands> adds exactly S881..S884 (contiguous), none removed; each row status mined, opened 2026-10-25, a cadence-only recheck cell, no pipe in any cell, the map URL verbatim in the source cell, the evidence quote inside the anchor cell, used-by exactly the admitted entries whose source: lines cite it; the only in-place registry change is S877's used-by cell (old->new in the lesson)",
    "REPOINTED: every `source:` line carries exactly one id whose row URL equals the cited URL (S877 or S881..S884); every inline S-id in both entries resolves to one of those five rows; no staged-namespace id (S882..S884 of the campaign, S899, S900) is cited as if it were a lane row",
    "GATE: corpus/lessons/round-74.md `## Gate` carries per adopted row URL + access date 2026-10-25 + a <=25-word located quote + locator, and >=1 admit and >=1 reject; every reject row carries its probed URL, reason and flip; S883/S884 rows state the re-quote (the staged S899/S900 quotes were absent: R72 refusal, URL-quote mispairing) with the located replacement",
    "EVIDENCE: reports/round-74/evidence/<id>.txt exists per adopted row at <lands> with fetch line, a browser-shaped UA, HTTP 200, a 64-hex sha256 of the fetched body, and the body window around the quote stored verbatim; the counter checks the Gate quote occurs inside that stored window (not merely that a flag says so)",
    "REJECTS: the lesson names refused staged S882 (not appended: existing row S877), the earlier-refused staged S899/S900 quotes and the re-quote, each not-adopted staged file/family listed in rejects, with reason and flip",
    "GROUND: reports/round-74/telemetry/gap-sweep.txt names the 804-row registry and 0 matches per fragment and per CJK term; the counter independently re-derives 0 at base",
    "CITEDLINES: tools/check-cited-lines.py over both entries from the materialized tree prints 'CITED-LINES: 0 finding(s) in 2 file(s)'",
    "CENSUS: sources-census.sh validate --root <materialized fleet> kotodama exits 0 at the registry bytes of <lands> with no E-codes",
    "SCRATCHMIRROR: .ufo/waves/round-74/assimilation/validate-receipt.txt shows `validate --file` exit 0 on the mirrored corpus carrying the four rows and both entries, in a commit strictly before the registry-append commit",
    "COLLCHECK: reg-ids/collisions hold no adopted id; guard-proof shows a planted 1-3-space-indented collision found and a 4-space one not found; the regenerated map maps old->new for every adopted id",
    "FROZENCFG: row set, entry paths, fragments, map and every constant the counter uses are read from claims.json AT the <freeze> commit (git show), never from the graded tree; <freeze> must be a strict ancestor of <lands>"],
   "kill_rule":"any admitted entry cites a refused/unknown staged id or an id naming an unrelated lane document, or any cited source lacks a round-74 Gate record and a committed evidence window containing the Gate quote, or any staged row is appended as-is (un-normalized recheck cell, escaped pipe, used-by not exactly the citing entries, opened date != 2026-10-25), or any leg false at <lands> -> the claim fails as declared",
   "do_nothing_control":"reports/round-74/telemetry/controls-c.txt: lands == base FAILS; plus the junk-landing controls (two stub entries with a header; four rows copied from staged with used-by pointing at stubs; Gate quote not in the evidence window; counter config edited in the graded tree) each FAIL their named leg",
   "counter":"python3 -B reports/round-74/accept-c.py --root . --lands <lands> --freeze <freeze>"},
  {"id":"Ca","axis":"calibration","kind":"records",
   "title":"Self-assessment vs repo-state ledger: round-73 closure routed defects (leftover seat files, missing PASS-at-lands receipts, scenario-count drift, README footer reading) plus swept mismatches repaired or annotated append-only",
   "before":f"at base {BASE}: the committed-bytes ledger reports/round-74/ledger.json (>= 10 pairs, fixed before data) shows every listed pair red — stated token != observed token (or file untracked / receipt absent); pairs include: the six .ufo/waves/round-73/w2 files modified/untracked in the worktree and absent from the pushed tree; no committed PASS-at-lands receipt for ACCEPT-C-73 / ACCEPT-CA-73; report/LOG/SCORECARD '9 scenarios' vs selftest-r3.txt 'SELFTEST OK: 10 scenarios'; and the pairs the wave-1 sweeps add (ids fixed at freeze).",
   "after":"`python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin` prints ACCEPT-CA-74: PASS legs=<n>/<n>: REPAIR pairs green; ANNOTATE pairs each carry a SCORECARD '## Corrections — round 74' row naming id + old token + new token + re-derivation command; the round-73 w2 seat files tracked; PASS-at-lands receipts for both round-73 counters committed with stamped==evaluated==measured revision headers.",
   "ledger":"reports/round-74/ledger.json",
   "legs":[
    "LEDGER: reports/round-74/ledger.json is committed in the freeze commit, declares round 74 / claim Ca / base, >= 10 unique pairs, each structurally valid (argv observe_cmd over a read-only allowlist that EXCLUDES interpreters and echo-style constant printers, compiling parse with a capture group, stated_text found at stated_at in the BASE tree, stated token anchored in it)",
    "BASEMISMATCH: at the base revision, in a materialized clone, every pair declared red has stated token != observed token and none is unobservable; the number of red pairs >= 10",
    "REPAIR: every REPAIR pair's statement re-read at <lands> (last occurrence) equals the truth observed at <lands> and differs from the base statement",
    "ANNOTATE: every ANNOTATE pair has a row under '## Corrections — round 74' in SCORECARD.md naming the pair id, the base stated token and the observed token at <lands>, and the row's re-derivation command re-runs inside the counter and returns the observed token",
    "APPENDONLY: zero removed lines in LOG.md, SCORECARD.md, corpus/lessons/round-73.md, corpus/lessons/round-72.md (lane base..<lands>); the fleet round-73 report is the blob at the ledger's fleet_pin with zero removed lines; in-place edits permitted only in files a ledger REPAIR pair names",
    "NOSTUB: every correction row carries id + old token + new token + the re-derivation command and no placeholder token",
    "SEPARABLE: no byte the Ca legs read cites an S-id >= S881, names a claim-C path (worldbuilding-setting-practice*), or reads a claim-C file; count pairs measure at the pinned base revision so landing C cannot move them (the frozen sentence — the counter implements exactly it, no wider)",
    "TRACKED: the ledger's must_track paths (the six .ufo/waves/round-73/w2 files) are, at <lands>, byte-equal to the worktree-at-base content recorded in the ledger (sha256) and non-empty",
    "RECEIPTS: reports/round-74/telemetry/ carries a PASS-at-lands receipt for ACCEPT-C-73 and for ACCEPT-CA-73, each produced inside a clone materialized at round 73's lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0, whose header stamped==evaluated==measured==that revision",
    "FROZENCFG: ledger, constants and allowlists are read from claims.json/ledger.json AT <freeze> (git show), never from the graded tree; <freeze> is a strict ancestor of <lands>",
    "STAMP: the receipt carries the stamped/evaluated/measured revision, tree and counter-sha256 headers (QUALITY 17/19 grammar of tools/check-receipt-seq.py) with stamped == evaluated == measured == <lands>, produced inside a clone materialized at <lands>"],
   "kill_rule":"any pair unannotated and unrepaired at <lands>, any correction row naming only an id, any removed line in the APPENDONLY set, or any leg false at <lands> -> the claim fails as declared; the after-state never requires rewriting frozen bytes (round-69 Ca2 failure class)",
   "do_nothing_control":"reports/round-74/telemetry/controls-ca.txt: lands == base FAILS; the --selftest covers stub-row, append-only removal, in-place-outside-allowed, shell-string/interpreter argv, constant-printer observe_cmd, min-pairs gate, and config-edited-in-graded-tree controls",
   "counter":"python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin"}
 ],
 "frontier_step":{
  "census_cmd":"/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama",
  "census_start":"reports/round-74/telemetry/census-start.txt (exit 0, 804 rows)",
  "mistake_to_mine":"R73 closure routed defects 1-4: late seat writes after the push (six w2 files), missing PASS-at-lands receipts, counter survivors (junk landings pass; config read from graded tree; constant-printer ledger; SEPARABLE wider than frozen) — recorded in corpus/lessons/round-74.md ## Mistakes with the junk-landing controls as the red-before",
  "sourced_claim":"C (rows S881..S884 opened and mined this round)",
  "quality_candidate":"QUALITY 25 — a counter reads its constants from the frozen commit and ships junk-landing controls (R73 routed defect 4)",
  "considerthese":"absent for this lane (ls considerthese -> no such directory)"}
}
json.dump(C,open(f"{LANE}/reports/round-74/claims.json","w"),ensure_ascii=False,indent=1)
print("ok")
