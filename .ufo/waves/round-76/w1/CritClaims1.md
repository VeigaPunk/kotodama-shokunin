# CritClaims1 — attack on CLAIMS-DRAFT.md claim C (coverage, "calendar and era instruments")

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `98c486b`. Read-only seat; no repo state mutated; no scratch dir created (nothing to delete); no tool installed.
Each finding: counterexample, evidence (command -> raw output), impacted axes, smallest safe correction (an exact replacement sentence).

## Verdict
Claim C as drafted is NOT one concrete value and its "before" predicate is false at base. Four defects are blocking (F1, F2, F3, F5); the rest are sizing/provenance repairs.

---

## F1 — the draft's "Before" command does not print nothing at base (false pre-state)  [BLOCKING]
Draft text: "Before: `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` each print nothing (exit 1)."

Evidence:
- `git -C <lane> grep -c -E 'GB/T 33661' 98c486b -- corpus` -> `98c486b:corpus/lessons/round-68.md:1` / `98c486b:corpus/lessons/round-69.md:2`, rc=0.
- `git -C <lane> grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` -> `98c486b:corpus/lessons/round-68.md`, rc=0.
- Scoped to where the claim lands, the pre-state IS empty: `git -C <lane> grep -l -E '33661|digital\.archives|openstd|gmw\.cn' 98c486b -- corpus/knowledge corpus/SOURCES.md` -> (no output) rc=1.
- The draft also states no AFTER command, so the before/after pair is not a measurement of anything: with the draft's scope (`corpus`) the "after" grep would already be non-empty before any work.

Axes: measurability, honesty of pre-state (a false "before" is a self-falsified claim at freeze).
Correction (replace the Before sentence):
> Before/after probe, scoped to the surfaces the claim moves: `git grep -l -E 'GB/T 33661|digital\.archives\.go\.jp' <rev> -- corpus/knowledge corpus/SOURCES.md` prints nothing (exit 1) at `98c486b` (verified; lessons `round-68.md`/`round-69.md` already mention both strings and are deliberately out of scope), and at the landing rev prints >= 1 knowledge path and `corpus/SOURCES.md` (exit 0).

## F2 — "n>=2 of four" is a threshold fixed before data but unreachable on the stated floor, and one candidate is dead by the draft's own rule  [BLOCKING]
Counterexamples:
- Candidate d cites ONLY S916, tier C (staged text: "sources: the one row above, tier C"). The draft says "no tier-C row is the sole support of an admitted entry" -> d is inadmissible by construction. Effective pool = {a, b, c}; the "four candidates" framing overstates it.
- Word counts (`wc -w` on staged files): a=1094, b=445, c=275, d=340. The round-75 counter derives a floor from the smallest base knowledge entry (`reports/round-75/accept-c.py:987 _min_entry_words`, constant 478 at r75). At base 98c486b the smallest entry is `heritage-taxonomy-models.amend-2026-10-24-r13.md` = 478 words (`for f in $(git ls-files corpus/knowledge ...); wc -w | sort -n | head -1` -> `478`). Staged b (445), c (275), d (340) are all below 478; only a clears. So with the floor kept, n<=1 from staged bytes -> "n>=2" fails unless entries are rewritten/expanded by the lane; with the floor dropped, the threshold was narrowed post hoc to fit. Either way the draft hides the dependency.
- Entry a's 1094 words include a "Superseded passage — the round7 entry" block that is NOT about the claim (S919/S921 Marrone/Barthes; the staged text itself says "Neither is a source about GB/T 33661-2017") and carries scaffold prose ("Proposed body (dated addition)", "§N", "Trim it if the later entry supersedes it outright"). Counting it toward floor/n is padding.
- Is "n>=2" declared or post hoc? It is declared in the draft, but nothing justifies 2; n=2 is reachable by {a,b} (two entries about the SAME standard) with zero era-table coverage although the theme/claim title names "archival era-name tables".

Axes: claim sizing (value vs threshold), mix of surfaces, adoption quality.
Correction (replace the n sentence):
> n is exactly the number of files admitted among the four candidate paths, with the freeze-time floor `n >= 2` AND at least one admitted file from each named surface (the GB/T 33661 calendar-compilation surface: a or b; the archival era-name surface: c or the S935 section of a); candidate d is held as a declared reject (tier C is its sole support) unless a staged or lane-written co-supporting tier-A row is cited in its own `source:` lines; each admitted entry body is >= the base-derived word floor (478 words at `98c486b`, heading lines excluded, the superseded-passage block excluded) — entries below it are rewritten by the lane from opened rows before admission or rejected.

## F3 — the do-nothing control named in the draft is not the cheapest control; a header-only stub control passes every clause that is written  [BLOCKING]
Draft control: "counter at `lands == freeze` must FAIL the data legs." That only tests *zero* work. The cheap control: four header-only stub files at the four paths (header fields copied from staged files, body empty or the staged "Proposed body" bullets verbatim), plus the 8 staged registry rows run through `sed` (renumber S908/S935->S894 etc., status `mined`, `opened 2026-10-27`, used-by = stub paths). Scored against the draft predicate in prose:

| draft clause | stub control |
|---|---|
| files 252 -> 252+n, n>=2 | PASS (256) |
| registry 817 -> 817+k, one row per distinct document | PASS (sed-built rows; 5 new docs S894–S898) |
| rows `mined`, `opened 2026-10-27`, used-by = citing entries | PASS (sed) |
| no tier-C sole support | PASS by dropping d (n=3) or citing S916 plus any other row in d |
| every Gate quote inside a committed evidence window | PASS vacuously (Gate quotes can be the staged spans; no clause says the *entry body* quotes anything; a Gate with no tool-captured window is only caught if the counter requires the window grammar) |
| Gate carries >=1 admit and >=1 reject | PASS (write two table rows) |
| census exit 0 | PASS if census only checks header fields / count |
| kill rule "a row appended as staged" | PASS after sed (not byte-equal to staged) |
| "Before" greps flip | PASS — and moot: the pre-state already exits 0 (F1) |

Every written clause is about counts/shape; no clause constrains the entry *content*. Entries c and d as staged ARE content-free in the relevant bullets (c: "from S908: the era-name-to-year table the archive searches by, the full span it covers, and what it means that..." — no year, no era name; d: "rule (4) in the standard's own words" — the words are not there, and the staged file never quotes the clause). So a stub and the staged bytes are close to the same artifact.

Axes: control strength, anti-gaming, honesty.
Correction (replace the control sentence; also add content-bearing after-state):
> Controls (both must FAIL the data legs, run before data lands): (i) `lands == freeze`; (ii) the stub control — four header-only files at the candidate paths plus the staged registry rows sed-adapted — which fails the entry-body leg (each admitted entry carries >= 478 words after the first `## ` section and, per bullet, at least one span <= 25 tokens that occurs verbatim inside the evidence window of a row it cites) and the evidence-window leg (`url:`/`fetch:`/`user-agent:`/`http-status: 200`/`sha256:`/`--- window ---`/`--- quote ---` grammar, quote inside window).
And add the after-state content probes: `git grep -l -F '农历的编算和颁行' <landing rev> -- corpus/knowledge` >= 1 path, `git grep -l -E '1 second|一秒|1 秒' ...` (precision clause as S937 quotes it) >= 1 path, and `git grep -l -F '詔勅・勅令・勅書' ...` >= 1 path (each exit 0; each exits 1 at `98c486b`).

## F4 — not one concrete value; universal/compound clauses the counting command does not enumerate
The after-state is an 8-conjunct sentence. Items that are universal or un-enumerated:
- "every Gate quote located inside a committed evidence window" — no command named; "committed evidence window" has no path set. (Counter legs exist in `accept-c.py` but are not named in the claim text.)
- "no tier-C row is the sole support of an admitted entry" — universal over admitted entries; needs the enumerating command (parse `source:` lines -> row tier cell).
- "k = number of distinct documents cited by the admitted entries that the registry did not hold" — k is a definition, not a target value; a reader cannot re-derive k by one command, and k depends on which documents the planned merge treats as one (S908+S935 are folded into one row S894 although S935 is a different Wayback capture at a different date than the S908 live form; S919/S921 are already-held -> 0 new rows). With plan S894–S898, k is knowable now.
- "census exit 0" — which census command (`reports/round-76/telemetry/census-start.txt` exists only after the freeze).
- "Gate carries >=1 admit and >=1 reject from the assimilation set" — "assimilation set" undefined (staged-ids = 132 ids; the claim's rejects must come from that set, not from nothing).
- "Kill rule … a cited campaign-namespace id" — universal; see F6 (staged bodies contain many).

Axes: claim sizing (QUALITY/AXES prompt §6 item 9).
Correction (replace the Declared after-state lead-in):
> Declared after-state: one measured value, `git ls-files corpus/knowledge | grep -c '\.md$'` = 252 at `98c486b` and = 252+n at the landing rev with n fixed by F2's rule; and `awk -F'|' '/^\| S[0-9]+ /{print $2}' corpus/SOURCES.md | sort -u | wc -l` = 817 at base and = 817+k at the landing rev, where k is fixed in the frozen id map (planned S894–S898 -> k = 5 if all five documents open, listed by id and URL in `claims.json`). Side predicates (tier, used-by, Gate, census) are each stated as a counter leg with its command, not as clauses of the value.

## F5 — "ground the lane does not hold" is overstated; the lane already refused the exact digital.archives.go.jp/search page and already holds most era-start years  [BLOCKING for the era half]
- `corpus/lessons/round-68.md` (grep above): "refused (8 — page fetched HTTP 200, quoted span absent from served bytes; fabrication-class candidates): … S825 (digital.archives.go.jp/search is a portal landing, not the table page)". Staged S908 (campaign) cites the SAME URL `https://www.digital.archives.go.jp/search` as a *live* form anchor (row 56). Staged S932's own text says "the live record page no longer serves this text; the archived capture does", and S935 is the same for the archives page. So S908's live anchor is exactly what the lane already found absent; only the Wayback capture (S935) is a candidate source. S894's "campaign S908 live form + S935 capture, one row" must be anchored on the capture only.
- The lane's `era-periodization-models.md` already holds: Meiji 1868 (line 49), Reiwa 2019 (lines 31, 50), Heisei/1989 (line 55), Gengō-hō, JIS X 0301, the Minguo 1912. Only Taishō 1912 and Shōwa 1926 as a start-year pair are absent. Entry a §N+2's table "明治 1868, 大正 1912, 昭和 1926, 平成 1989, 令和 2019" = 3 of 5 values already held; the new thing is the archival-database provenance, not era data.
- Calendar side genuinely new: `grep -n -i -E '33661|紫金山|new moon|winter solstice|冬至'` on `calendar-festival-systems.md` hits only line 117 (Dongzhi) and line 46/136 (24 solar terms, held). Not held: GB/T 33661 identity, new-moon-first-day / winter-solstice-month-eleventh rule, 1-second precision, drafter = Zijinshan. So the expansion credit is sound for the calendar half and thin for the era half.
- Further: `git grep -l -E '33661|digital\.archives|openstd|gmw\.cn' 98c486b -- corpus/knowledge corpus/SOURCES.md` rc=1 confirms nothing held at the registry/knowledge level (the surface the claim moves) — that part of "frontier -> core" holds.

Axes: coverage honesty / expansion credit.
Correction (replace the "Surface the claim moves" sentence):
> Surface the claim moves: frontier -> core for one calendar-compilation standard (GB/T 33661-2017: its 编算 rules and precision, per S937, and its registry record, per S932/S938) and for the archival provenance of Japanese era-start years (the National Archives of Japan era-name table, anchored on the Wayback capture S935 because the live page `digital.archives.go.jp/search` was refused in round 68 as a portal landing); the lane already holds Meiji 1868, Heisei 1989 and Reiwa 2019 in `era-periodization-models.md` and the claim does not count them as new ground.

## F6 — campaign-namespace ids beyond the 35 listed collisions are present in the staged bodies and will point at DIFFERENT lane documents
- Staged entries cite campaign ids S718, S719, S750, S757, S807, S919, S921 (and S908/S916/S932/S935/S937/S938 which re-map to S894–S898). In the lane registry: S718 = Farran 2016 (infant-directed speech, PLOS ONE), S719 = Cristia 2013, S750 = Culin 1907 (games), S757 = Huizinga, S807 = Li 2021 (median artery/meridians) (`grep -n -E '^\| S(718|719|750|757|807) ' corpus/SOURCES.md`). The entries use those ids for the GB/T registry record, interpretation PDF, etc.; copied as-is, the lane silently cites unrelated papers. `assimilation/collisions` lists only S859–S893 (35 ids), so the collision guard as drafted does not see these.
- The draft says only "coupling only" for S718/S719/S757 in c/d; but a, b (S750, S807 inside b/a text: "tier A from the official registry record (S750) … third-party reproduction (S807)") also carry them.
- Also dangling couples: staged `couples:` cite `culture-material/calendar-festival-systems.amend-2026-10-23.md`, `culture-material/era-periodization-models.amend-2026-10-23.md`, and `linguistics/naming-systems.amend-2026-10-24.md`; none exists in the lane (`ls corpus/knowledge/culture-material/*.amend*` -> only `heritage-taxonomy-models.amend-2026-10-24-r13.md`, `worldbuilding-setting-practice.amend-2026-10-23.md`; `corpus/knowledge/linguistics` has `naming-systems.md` only). The era file's own verified-at line records "15/15 couples targets resolve" — census may check couples.

Axes: provenance/identity (duplicate id authority, false provenance).
Correction (replace the first paragraph's "35 collisions" sentence and the kill rule's tail):
> Every campaign-namespace id (all of S718, S719, S750, S757, S807, S908, S916, S919, S921, S932, S935, S937, S938, whether a citation or a coupling reference) is rewritten BY DOCUMENT to a lane id or to prose naming the document, and the counter greps each admitted entry for `\bS(7[0-9]{2}|8[0-9]{2}|9[0-9]{2})\b` ids not in the frozen id map; every `couples:` path in an admitted entry resolves in the landing tree (`test -e`), with unresolved couples removed.

## F7 — sourced-claim requirement (frontier step item 4) is only nominally met
"Sourced claim: C cites the opened rows S894+" — the rows S894–S898 do not exist at the freeze (they are planned; the draft says "Scouts may change this plan where a document is unreachable or two URLs are one document"). The claim cites rows that are not opened, and the plan allows renumbering after the freeze; a claim that cites ids that may change is not sourced at freeze.
Correction (replace the Sourced claim sentence):
> Sourced claim: C rests on five documents, each cited by URL in `claims.json` at the freeze with its evidence-window path under `reports/round-76/evidence/` (GB/T 33661-2017 state-press report `https://news.gmw.cn/2017-05/23/content_24559485.htm`; openstd record Wayback `…/20260424031027id_/…newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`; openstd `showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296`; National Archives of Japan Wayback `…/20260422145052id_/https://www.digital.archives.go.jp/search`; xingzuobaike `d165803.html` as tier-C context only); ids S894–S898 are assigned from the frozen map, and a document that fails to open at the freeze is removed from the claim, not renumbered after it.

## F8 — registry k accounting hides a merge decision the counter must pin
The draft folds campaign S908 (live form, row 56 teaches "options as served 2026-10-23") and S935 (Wayback capture 2026-04-22, 元号名称／開始西暦年 table in the 詔勅・勅令・勅書 database) into ONE row. They are different pages/captures; whether they are "one document" decides k (5 vs 6) and the Gate admit rows. Entry c cites S908 only; entry a cites S935 only — after the fold, both cite S894. Same fold for S932 (record `newGbInfo` capture) vs S938 (`showGb` live route): different URLs, different dates; the draft assigns separate ids S896/S897, consistent with by-document rule only if the table-of-contents of the record is the same page, which the staged text says it is NOT (S938 = "the registry's own record page … read at `showGb?type=online`"; S932 = `newGbInfo`; both state the same fields).
Correction (add one sentence):
> Document identity for the registry: two URLs are one document only if the evidence windows share a normalised URL key or the Gate row records the fold with both URLs and the reason; the frozen id map lists each fold, and k is the count of map targets absent from the base registry.

## F9 — structural/shape risks for the landed files (counter must name them)
- Staged a/c/d carry "# Amendment — …" headings and the scaffold phrase "Proposed body (dated addition)" with `§N` placeholder numbering; r75 INDEX leg requires README rows ``- `name.md` — <the entry's own `- topic:` text>`` for each adopted entry, and the "Counts checked" footer to match the new total. The draft's after-state does not mention the README index or footer: adding n files without them breaks the lane's own count line (round-75 H4/INDEX leg precedent). 
- The draft's "lesson with `## Gate` … `## Mistakes`" asks for >=1 mined mistake; entry-shape defects found here (the d-entry sole-tier-C support, F6 id collisions beyond the listed 35, the false Before command F1) are candidate mined mistakes with a testable fix (counter legs F3/F6).
Correction (add to after-state):
> `corpus/README.md` carries one index row per admitted entry in `culture-material/` (shape ``- `name.md` — <entry `- topic:` text>``) and its last `Counts checked` footer states file total 252+n; any other README change fails.

---
## Replacement text summary (apply in this order)
F1 Before sentence; F2 n sentence; F3 controls + after-state content probes; F4 after-state lead-in; F5 surface sentence; F6 collision + kill-rule tail; F7 Sourced claim; F8 identity sentence; F9 README sentence.

## Unrun / not verified
- Did not run the census or any accept-c counter against the staged bytes (no landing exists; seat is read-only).
- Did not fetch any live URL; the claim that the live archives page is a portal landing rests on round-68 lesson line `S825 (digital.archives.go.jp/search is a portal landing…)` and the staged S932/S935 "no longer serves this text" statements.
- Evidence windows for S894–S898 are not examined here (assimilation/ has staged-ids, collisions, reg-ids, guard-proof only).
