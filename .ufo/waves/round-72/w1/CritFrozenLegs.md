# CritFrozenLegs — pre-data freeze audit (kumitate r42 class)

Seat: `L1Kotodama72.CritFrozenLegs` (critic, leaf; no delegation). Round 72, hyaku run 6. Date 2026-10-25.
Scope: the two frozen claims in `reports/round-72/claims.json` vs the two Exec*Counter drafts
`.ufo/waves/round-72/counters/accept-ca.py` (ExecCaCounter) and `accept-c.py` (ExecCCounter),
per assignment (a) same predicate sentence, (b) wrong legs corrected NOW pre-data with a documented
correction, (c) kill rules checkable by a non-author with one command.
All repo reads are read-only. No tools installed; pacman untouched (host-wide pause, orchestrator ruling 2026-10-20).

## 0. Executive summary

- **Leg-name sets match.** Ca: same 12 leg names in claims.json and accept-ca.py (only QUAL21 runs 2nd
  in the counter vs 8th in the claims — cosmetic, `legs=12/12` invariant unaffected). C: same 10 leg
  names in the same order. **No missing/extra legs on either side.**
- **The predicate sentences diverge on 11 points** (detailed §2): 4 make the Ca counter unable to print
  PASS on any lands (QUAL20/QUAL21 regex, MAPCORR path, REPORTCORR fleet-repo path, NOHARM census layout),
  2 make legs vacuous (W2FILES wrong file set, REPORTLAST vacuous ancestry), 1 makes a leg unpassable as
  worded (CASTAMP), 2 are under/over-specified (LOGCORR missing S992; CAPOEIRA hardcoded timestamps),
  1 makes the C counter's COLLCHECK fail on correct data (filename mismatch with the artifacts the wave
  actually produced).
- **One claims.json text defect**: Ca before-text says "five round-71 w2 seat files … (2 modified,
  5 untracked)" — self-contradictory (2+5=7); the W2FILES leg correctly says seven. Documented
  correction required NOW (claims.json is untracked; edit + commit to pin the freeze — cf. RevClaimsFidelity F10).
- **Kill rules**: the leg-falsity clause reduces to one command per claim (the counter itself). Two
  kill-rule sub-clauses have no one-command enumerator (Ca: "fleet report round-71" byte-rewrite;
  C: "cited source was opened this round"). Details §4.

## 1. Leg-list diff (names, counts, order)

| claim | claims.json legs | counter legs | verdict |
|---|---|---|---|
| Ca (12) | QUAL20, W2FILES, LOGCORR, LESSONCORR, REPORTCORR, MAPCORR, CASTAMP, QUAL21, CAPOEIRA, APPENDONLY, REPORTLAST, NOHARM | QUAL20, QUAL21, W2FILES, LOGCORR, LESSONCORR, REPORTCORR, MAPCORR, CASTAMP, CAPOEIRA, APPENDONLY, REPORTLAST, NOHARM | set identical; only QUAL21 order differs — cosmetic |
| C (10) | ENTRIES, ROWS, REPOINTED, GATE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK | same 10, same order | identical |

Counter output strings match the frozen `after` sentences: `ACCEPT-CA-72: PASS legs=12/12`
(accept-ca.py:134) and `ACCEPT-C-72: PASS legs=10/10` (accept-c.py main). Both take `--root/--lands`;
accept-ca.py also parses `--fleet-root` (see 2.6 — unused).

## 2. Predicate mismatches (claims.json leg sentence vs counter code)

Severity: **B** = counter cannot reach PASS on any lands / exits 2; **V** = vacuous or unpassable;
**S** = under/over-specified vs the frozen sentence.

### 2.1 QUAL20 — B (new; the F6 class also hits QUAL20)
accept-ca.py:77 `re.search(r"^20\\. ", q, re.M)`. The raw string double-escapes the dot: the pattern
matches `20\` + any char, not `20. `. Verified empirically on a synthetic QUALITY blob: `r"^20\\. "`
does not match `"20. criterion"`; `r"^20\. "` does. Frozen leg: "carries '^20\\. '" — the criterion
line "20. …" will never match → QUAL20 always FAIL.
**Smallest safe correction (counter, pre-data):** `r"^20\. "` (and same for QUAL21, see 2.2).

### 2.2 QUAL21 — B + S (RevClaimsFidelity F6)
Identical regex defect at accept-ca.py:78 (`r"^21\\. "` → never matches `21. `). Additionally the
frozen sentence's parenthetical — "(CDX canonical-slug probe before ruling 'no capture'; every Gate
reject records its URL)" — has no counter term; the counter tests only the criterion line.
**Correction:** fix regex; either add a counter term for "every Gate reject records its URL" or trim
the parenthetical from the frozen sentence (documented pre-data edit of claims.json).

### 2.3 W2FILES — V + wrong enumeration (RevClaimsFidelity F4, confirmed independently)
Frozen: "the seven round-71 w2 seat files are committed at <lands>" — the seven = the uncommitted set
the before text enumerates: **2 modified** (`Filler30.md`, `RevReceipts.md`) **+ 5 untracked**
(`CritTrends.md`, `Filler28.md`, `Filler36.md`, `RevCounterCa.md`, `RevEntry.md`) — confirmed against
`git status --porcelain` at b60c7b1.
Counter W2 tuple (accept-ca.py:12-20): `RevReceipts, RevCounterCa, RevSeparability, CritGaming2,
RevRows, RevCausality, Filler33` — five of those are already committed-and-clean at base
(RevSeparability, CritGaming2, RevRows, RevCausality, Filler33 — verified via `git cat-file -e`);
the five actually-untracked/modified files Filler30/CritTrends/Filler28/Filler36/RevEntry are absent.
Intersection with the true set: 2 of 7. The leg as coded is TRUE at base (vacuous do-nothing) and does
not measure the claim's seven.
**Smallest safe correction (counter):** W2 := the git-status seven above.

### 2.4 LOGCORR — S (under-check)
Frozen: names "the three superseded round-71-entry lines old->new (S861->S992 -> S874->S1005;
<RECORDS> placeholder line; misroot-sweep line)".
Counter (accept-ca.py:91-93) checks `"S861" and "S874" and "S1005" and "<RECORDS>" and "misroot"` in
the round-72 log portion — **S992 is not required**. All three superseded lines are confirmed real:
Item-10 line `S861→S992`→`S874→S1005` edited in place at 99e3d63; header line `records <RECORDS>`→
``records `1d1b4325`; final receipts `3764c2df` / re-stamps `7179d6d6`` at 1721fbd; misroot-sweep line
rewritten at 1721fbd. A round-72 entry naming "S861 → S874→S1005" without S992 would pass the counter
and fail the frozen sentence.
**Smallest safe correction (counter):** add `"S992"` to the tuple.
Also note the split `log.split("round 72", 1)` keys on the first occurrence — "round 72" appears
nowhere in LOG.md at base (verified), so this is safe today, but brittle to any earlier mention.

### 2.5 LESSONCORR, APPENDONLY — consistent
LESSONCORR counter checks the appended `## Corrections (round 72)` for the id-map old→new
(S861/S992/S874/S1005), tally (10/6/5, 10/7/4), seats (41/78/40/77) — matches the frozen sentence
(the in-place lesson edit `id-renumber-map.json S861→S992`→`S874→S1005` at 99e3d63 is confirmed real).
APPENDONLY: `git diff -U0 b60c7b1..<lands> -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md`
with no `-` content lines — matches the frozen sentence verbatim. Ca selftest exercises an in-place
edit fixture that must FAIL APPENDONLY (verified in code).

### 2.6 REPORTCORR / REPORTLAST — B (RevClaimsFidelity F3, confirmed)
`FLEET_REPORT = ".ufo/reports/round-72/kotodama.md"` read via `blob(root, lands, FLEET_REPORT)`
(accept-ca.py:26,102,128) — i.e. from the LANE repo. The lane has no `.ufo/reports/` at all (verified);
the filed fleet report lives in the fleet repo (`/home/vgpnk/Projects/shokunin/.ufo/reports/…`; the
round-71 one at `.ufo/reports/round-71/kotodama.md` lines :57 and :61 both say `S861→S992` — verified,
matching REPORTCORR's frozen content). `--fleet-root` is parsed (main) and passed to `check()` but
never used. As drafted, `blob()` raises → COUNTER ERROR exit 2 on every run.
**Smallest safe correction (counter):** read the report with `git -C <fleet_root> show <fleet-commit>:.ufo/reports/round-72/kotodama.md`
(the round-72 report is filed after data lands; ExecCaCounter's own report flags this as an open integration item).

### 2.7 MAPCORR — B (RevClaimsFidelity F2, confirmed + one layer deeper)
Counter: `MAP = "corpus/id-renumber-map.json"` (accept-ca.py:24). Verified: no such path exists in the
base tree; the only id-map is `.ufo/waves/round-71/assimilation/id-renumber-map.json`. `blob()` raises
→ exit 2. **Second layer:** even with the path fixed, `mapchecks` requires the strings "65ff151" and
"99e3d63" inside the map JSON — verified the map JSON contains 0 occurrences of either sha; the frozen
leg wants the old→new RECORD (65ff1510's map S861→S992 superseded by 99e3d63's S874→S1005) named in the
round-72 corrections, not shas inside the artifact.
**Smallest safe correction (counter):** point MAPCORR at the corrections record (lesson/LOG round-72
sections) for the sha old→new text; keep the map path only if content is actually asserted there.

### 2.8 CASTAMP — V/unpassable both ways (RevClaimsFidelity F1, confirmed)
Frozen: "an appended receipt re-stamps measures-ca at 64da9e14 with its true counter sha f706aacd".
Two verified facts collide:
1. **Already true at base**: `reports/round-71/telemetry/measures-ca.txt` at b60c7b1 already contains an
   appended re-stamp receipt pairing `f706aacd`@`64da9e14` (lines 7-15) above the original bytes. A
   do-nothing reaches this sub-target — before==after for the leg as worded.
2. **Counter can never pass**: accept-ca.py:110-113 requires `re.search(r"1ce25fb9.{0,120}64da9e14",
   receipt, re.S) is None`; verified the base blob pairs `1ce25fb9…64da9e14` within 84 chars, and any
   further APPEND preserving old bytes keeps that pair present. Only an in-place rewrite of
   measures-ca.txt removes it — which the leg's own "appended" wording forbids (and which sits uneasily
   with the claim title "append-only corrections"; F5).
**This is the one leg that must be corrected NOW pre-data, documented, not post-hoc.** Two clean options:
(a) amend the leg to "the ACTIVE header of measures-ca pairs f706aacd with stamp 64da9e14" and make the
counter check the first/header pairing; or (b) keep the leg and drop the negative regex (presence only).
Pick one and record the correction in the round-72 entry; do not let data land with the sentence and the
counter measuring different conditions.

### 2.9 CAPOEIRA — S (over-specified)
Frozen: "the Capoeira correction (live 200 + CDX captures under capoeira-circle-00892) is appended …".
Counter (accept-ca.py:114-118) hardcodes the three earliest CDX timestamps `20170513162348`,
`20171120140510`, `20171208155324` plus "200". The timestamps are evidence-grounded (ScoutCapoeiraReopen
records exactly these as the earliest three status-200 captures of capoeira-circle-00892), but they are
not in the frozen sentence, and the scout lists additional later captures. A conforming correction that
cites other captures would fail the counter.
**Smallest safe correction:** either relax the counter to (`capoeira-circle-00892` + live-200 evidence)
or amend the frozen leg to name the three earliest captures explicitly. Document the choice.

### 2.10 REPORTLAST — V (vacuous ancestry half)
Frozen: "all round-72 lane commits are ancestors of <lands>; the report names <lands> and the inherited
commits 99e3d63..b60c7b1". Counter (accept-ca.py:125-130) checks `git log BASE..lands` commits are
ancestors of lands — tautologically true for every commit in that range; it cannot detect a lane commit
landing AFTER <lands> (no HEAD==lands guard; the C counter's CENSUS leg has one). The text half
(lands, 99e3d63, b60c7b1 in the report) is real but unreachable until 2.6 is fixed.
**Smallest safe correction:** add `git rev-parse HEAD == lands` to REPORTLAST.

### 2.11 NOHARM — B (new; layout bug)
Counter (accept-ca.py:56-66) materializes `td/tree/corpus/…` from committed bytes, then runs
`census validate --root td kotodama`. sources-census.sh resolves lane "kotodama" under the root
(conf or `*-shokunin` dirs / explicit dirs); `td` contains only `tree/` → registry missing → exit 2 →
NOHARM always FAIL. Verified against the script header (exit 2 = missing registry).
**Smallest safe correction:** checkout := `td/kotodama` (or pass the checkout dir as the lane argument).

### 2.12 C-side findings
- **COLLCHECK — B (new).** Counter (accept-c.py:488-500) requires files literally named
  `reg-ids`, `staged-ids`, `collisions` under `.ufo/waves/round-72/assimilation/` or `…/validate/`.
  The wave's actual artifacts are `collcheck-reg-ids.txt`, `collcheck-staged-ids.txt`,
  `collcheck-collisions.txt` (assimilation/, collisions file verified 0 bytes) and
  `mutations/reg-ids-real.txt`, `staged-ids-real.txt`, `intersection-real.txt` (MutRegistryCollision).
  No file named exactly `reg-ids`/`staged-ids`/`collisions` exists → COLLCHECK always FAILS on correct
  data. Content-wise the check is sound (S874/S875 ∈ staged-ids, ∉ reg-ids, collisions empty — all
  verified true). **Smallest safe correction:** point MIRROR_ID_FILES at the collcheck-* names (or have
  the L1 also drop counter-named copies next to them; the counter draft is the cheaper fix).
- **SCRATCHMIRROR — consistent now.** Frozen path `.ufo/waves/round-72/assimilation/validate-receipt.txt`
  EXISTS as written (ExecScratchMirror, 2026-10-25T11:25-03:00; census `--file` exit 0, both rows named,
  797→799 rows, 0 removed lines). RevClaimsFidelity F11 (file absent) is RESOLVED. The counter also
  requires the receipt's introductory commit to be a strict ancestor of the registry-append commit —
  an L1 sequencing constraint: commit assimilation artifacts BEFORE the corpus/SOURCES.md append.
- **CENSUS — benign tightening.** Counter adds `HEAD == lands` to the frozen sentence ("exits 0 at
  <lands>"). Keep; note that evaluation must run at HEAD==lands or this leg FAILs by definition.
- **ROWS semantics.** Frozen "both used-by the two admitted entries" is implemented as: each new row's
  used-by ⊆ the two entry paths and the union == both entries. This matches the normalized rows
  (S874 used-by = both entries; S875 used-by = canonical only; union = both). Consistent; flagged only
  because the frozen English could also be read as "each row used-by both".
- **ENTRIES/REPOINTED/GATE/REJECTS/GROUND/CITEDLINES** — counter conditions match the frozen sentences
  (verified leg by leg; check-cited-lines.py exit 1 on findings / `CITED-LINES: <k> finding(s)` format
  confirmed). Known data-side dependency: the staged canonical entry currently has no `ground:` header
  line (ExecScratchMirror advisory) — the frozen ENTRIES leg requires it, so ScribeEntries/ExecRenumber
  must add it before landing, and check-cited-lines currently reports 2 findings on the staged entries
  (repair proposed in `validate/cited-lines-repair-proposal.txt`).

## 3. Required pre-data corrections (NOW, documented)

In order of blocking severity:

1. **claims.json text (b)**: Ca before-text "five round-71 w2 seat files are uncommitted (2 modified,
   5 untracked)" → "seven" (2+5). The W2FILES leg is correct; the before text is self-contradictory.
   claims.json is untracked — edit and commit it to hash-pin the freeze (also RevClaimsFidelity F10)
   BEFORE any data lands.
2. **CASTAMP leg sentence vs counter (2.8)** — pick correction (a) or (b), amend leg or counter, record
   the old→new in the round-72 entry. The sentence and the counter currently measure different
   conditions and the leg is do-nothing-true at base.
3. **accept-ca.py blockers (2.1/2.2/2.3/2.6/2.7/2.10/2.11)** — regexes, W2 tuple, fleet-repo read for
   REPORTCORR/REPORTLAST, MAPCORR path+target, HEAD==lands, census layout. All are scratch-path draft
   edits; none touches the frozen claims.
4. **accept-c.py COLLCHECK filenames (2.12)** — align MIRROR_ID_FILES with the produced artifacts.
5. **Documented-correction record**: every leg/text correction above must be named old→new in the
   round-72 LOG entry and the lesson corrections section the same round (the LOGCORR/LESSONCORR legs
   themselves require this discipline).

## 4. Kill-rule checkability (one command, non-author)

- **Leg-falsity clause** (both claims): one command each —
  `python3 -B reports/round-72/accept-ca.py --root . --lands <lands>` and
  `python3 -B reports/round-72/accept-c.py --root . --lands <lands>`. Checkable ✓ (once §3 items land so
  the counters can actually complete).
- **Ca kill clause** "any K71 defect landed by rewriting a filed byte (fleet report round-71, LOG.md
  entries <= round-71, lesson round-71 filed sections)": APPENDONLY covers LOG/lesson/QUALITY with one
  command (frozen inside the counter). The **fleet-report-round-71** sub-clause has no enumerating
  command from the lane (the report is a fleet-repo file; a fleet `git log -p -- .ufo/reports/round-71/
  kotodama.md` check would cover it but is not named anywhere). F7 stands: give it a command or move it
  to the falsifier notes.
- **C kill clause** "any cited source was not opened this round (2026-10-25) by the lane": an opening
  event is not enumerable over committed bytes; only the Gate's self-reported dates/quotes reference it
  (F8). Proxy command exists (GATE leg), the literal clause does not. Accept as tradeoff only if the
  canonical judge treats Gate self-report as the operational witness; otherwise cut the clause.
- C kill clauses "cites a quarantine-REFUSED staged row" / "staged row appended as-is" are enumerable:
  the first via reg-to-staged.txt × the register REFUSED set {S779,S786,S787,S792,S814,S816,S817}
  (confirmed 7; staged S870→S787, S899→S816, S900→S817 all REFUSED — REJECTS leg grounded), the second
  via ROWS/REPOINTED. ✓

## 5. Ground-truth anchors verified this audit (base b60c7b1)

- QUALITY.md: 0 committed `^20\. `, 0 `^21\. `; worktree carries the criterion-20 diff (1 line). ✓
- w2 uncommitted set = 7 (2 M + 5 ??) as listed in 2.3; w2/spec.json carries 40 items (LOG/lesson say 41/78). ✓
- LOG.md round-71 entry: all three superseded lines confirmed via 99e3d63 / 1721fbd diffs; tally 10/6/5
  in LOG:4270 vs true table 10/7/4 (quarantine-verdicts.md rows enumerated). ✓
- Fleet report round-71 :57 and :61 both say `S861→S992`; :61 also carries the 10/6/5 tally. ✓
- measures-ca.txt: current header pairs `1ce25fb9`@`64da9e14`; original preserved bytes pair
  `f706aacd`@`64da9e14`; `git show 64da9e14:reports/round-71/accept-ca.py | sha256sum` = f706aacd… —
  the frozen CASTAMP before-text is accurate. ✓
- Registry: 797 rows, max id S873, S874/S875 free; `ihchina`=0, `bunka.go.jp`=0. Staged S863/S867/S967
  not in the register slice. ✓ Capoeira CDX captures (earliest three 200s) confirmed in
  ScoutCapoeiraReopen.md. ✓

## 6. Tooling

None installed; none needed (read-only git/grep/python checks only). Pacman untouched per host-wide pause.
