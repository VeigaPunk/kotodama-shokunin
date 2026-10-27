# ExecCountsSweep — round 75 (hyaku run 10), wave 3: every counting claim in the landed prose

**Seat.** ExecCountsSweep (leaf executor, no dispatch). **Lane.** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
**Graded revision.** `4f5e3b2535c2c06c51627dc2736c40183847cae1` (claim C landing). **Freeze.** `5d0167464309d8133991b30f7d7a7011a6a0fd14`.
**Base.** `f556d1049fe651d3d63975600b13acd9fb686f15`. Claim Ca landing, cross-checked: `012e8d3c8b92f47c734f735d58d118d574fe6a14`.
Lane main at dispatch `82ced5cc205a116516e40895c4241415d54dae52` (telemetry/spec only; `git diff 4f5e3b2..82ced5c --stat` = no `corpus/**`, no `SHONEN.md`, no `SKILL.md`, no `SCORECARD.md`).

**Verdict: BROKEN.** The two counters do pass and the headline totals re-derive exactly, but **twelve landed statements are false at `4f5e3b2`** (F1–F12), four of them wrong *counting* bindings that name the wrong artifact for a number (F5–F8), and the lesson's first four lines declare the round unfrozen and DRAFT while the freeze is an ancestor of the tree that carries them.

---

## 1. Method (every command names `-C` or runs inside the seat scratch clone)

```
S=/fast/scratch/hyaku/kotodama-r75/ExecCountsSweep
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin "$S/clone"
git -C "$S/clone" rev-parse --show-toplevel          -> /fast/scratch/hyaku/kotodama-r75/ExecCountsSweep/clone
git -C "$S/clone" checkout -q -B main 4f5e3b2535c2c06c51627dc2736c40183847cae1
```
No mutation of the lane, the fleet repo, siblings or any external substrate; no `pacman`; no installs needed;
every number below was re-derived with the command a reader would type, run in the clone (or against
`/home/vgpnk/Projects/shokuknow` read-only for the staged-file digests). `$S` is removed before yield.

Counters run **inside the clone only**:

| counter | invocation | verdict line |
|---|---|---|
| C | `python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2… --freeze 5d01674… --fleet-root /home/vgpnk/Projects/shokunin` | `ACCEPT-C-75: PASS legs=13/13` |
| Ca | `python3 -B reports/round-75/accept-ca.py --root . --lands 012e8d3… --freeze 5d01674… --fleet-root … --combined 4f5e3b2…` (local `main` pinned to `012e8d3` for STAMP) | `ACCEPT-CA-75: PASS legs=12/12` |

---

## 2. The table — claim | where | stated | re-derived | equal?

| # | claim | where | stated | re-derived (command) | = |
|---|---|---|---|---|---|
| 1 | registry rows 808 → 817 | lesson:11, :364 | 808 / 817 | `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 808 / 817, last id S893 | ✅ |
| 2 | knowledge files 249 → 252 | lesson:11, :370 | 249 / 252 | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -c '\.md$'` → 249 / 252 | ✅ |
| 3 | 0 knowledge paths matching `narrative` at base | lesson:9 | 0 | `… \| grep -ci narrative` → 0 | ✅ |
| 4 | tiers A×3 / B×5 / C×1; all nine `mined`, `opened 2026-10-27`, `recheck 180d` | lesson:364-368 | as stated | `awk -F'\|' NF==13` over S885-S893 → A,A,A,B,B,B,B,B,C; mined ×9; 2026-10-27 ×9; 180d ×9 | ✅ |
| 5 | quote length per row (chars, whitespace tokens) | lesson:28-36 | 38/6, 48/9, 72/11, 21/1, 64/9, 77/12, 68/9, 51/10, 39/1 | `len(q)` / `len(q.split())` on each `quote:` → all nine exact | ✅ |
| 6 | smallest base entry = 478 words | claims.json C ENTRIES leg | 478 | word-count over all base entries → min 478 (`heritage-taxonomy-models.amend-2026-10-24-r13.md`) | ✅ |
| 7 | **adopted entry byte sizes** | lesson:92-95 | `6862 B` / `5933 B` / `2514 B` | `wc -c` on the three named lane paths → **30920 / 24166 / 23049**. The stated trio is the *staged* copy in `shokuknow/merge/kotodama/…` | ❌ **F5** |
| 8 | triage 40 staged files = 3 adopted / 6 path-present / 31 refused; families 9/17/5/9 | lesson:82-86 | 40; 9,17,5,9 | `find shokuknow/merge/kotodama/knowledge -name '*.md' \| wc -l` → 40; per-dir 9 culture-material, 17 linguistics, 5 myth-symbol, 9 verification; 11+9+3+2+3+1+2 = 31 | ✅ |
| 9 | six path-present digest pairs (12 hex) | lesson:112-118 | b17223b9a04b/09175b1849fb … 8f889666b32c/01029a642c9f | `sha256sum` staged vs `git show <base>:<path> \| sha256sum` → all 6 pairs match, staged ≠ lane | ✅ |
| 10 | `reg-ids` 808 lines S001…S884, sha `dd090b02…` | lesson:189 | match | `wc -l` 808, head S001 / tail S884, `sha256sum` dd090b02e0f5… | ✅ |
| 11 | `staged-ids` 132 lines S859…S990; 41 start `S8`, 91 start `S9` | lesson:190 | match | 132 lines; `grep -c '^S8'` 41, `grep -c '^S9'` 91; sha bab11d7d… | ✅ |
| 12 | `collisions` 26 lines S859…S884, sha `01ad6576…` | lesson:191 | match | 26 lines, S859…S884, sha 01ad6576b56d… | ✅ |
| 13 | 0 same-document pairs, 26 different-document pairs | lesson:196 | 0 / 26 | `collision-documents.txt:3-4` → `0` / `26` | ✅ |
| 14 | guard proof: 1/2/3-space plants found (exit 1), 4-space and tab not found, column-zero control sees 0 of 3 | lesson:203-209 | as stated | `guard-proof/proof.txt` lines 25-41, verbatim | ✅ |
| 15 | quarantine slice 21 lines = 21 rows = 18 `payload-absent` + 3 unreachable | lesson:130-138 | 21 / 18 / 3 | prompt's own `awk -F'\|'` over `absent-defect-register.md` → 21; class histogram → 18 + 3 | ✅ |
| 16 | re-count over `quarantine-verdicts.md`: PRESENT 10, REFUSED 7, UNVERIFIABLE 4, rows 21 | lesson:139-142 | 10/7/4/21 | `grep -cF '| PRESENT |'` → 10, `REFUSED` → 7, `UNVERIFIABLE` → 4, `^\| S[0-9]{3} \|` → 21 | ✅ |
| 17 | ledger 10 pairs, 6 REPAIR / 4 ANNOTATE, L75-01…L75-10 | lesson:12-14 | 10 / 6 / 4 | `json` over `pairs` → 10; `Counter(disposition)` → REPAIR 6, ANNOTATE 4 | ✅ |
| 18 | Ca-alone tuple 808/713/58/37; close 817/722/58/37 | `SHONEN.md:6` | as stated | status histogram `awk -F'\|' $9` → 713/58/37 at `012e8d3` and `f556d10`, 722/58/37 at `4f5e3b2` | ✅ |
| 19 | README footer total 252, vector 32/32/40/29/24/95; `## myth-symbol/ (32)` | `corpus/README.md:829-831`, `:376` | match | live per-dir counts: linguistics 32, myth-symbol 32, culture-material 40, synthesis 29, verification 24, civilizations 95 | ✅ |
| 20 | every base footer preserved byte-identical and in order, new footer appended | claims C INDEX leg | 3 base blocks + 1 new | base 749/792/813 = 243/247/249 → lands 754/797/818 identical; 252 appended at 829; counter reports `822 base / 831 lands line(s), 12 exempt` | ✅ |
| 21 | SCORECARD corrections tokens 249→247, absent→present ×2, 43→44 | `SCORECARD.md:1476-1479` | 247 / 1 / 1 / 44 | the four pasted commands re-run → `…:247`, `…:1`, `…:1`, `44 files changed, 13810 insertions(+)` | ✅ |
| 22 | QUALITY 23 addendum measured table (limb 1 `GROUND_RECEIPT` on r72, nothing on r73/r74; limb 2 exit 0, line 2 clean) | `corpus/QUALITY.md:186-192` | as stated | both one-liners re-run verbatim: r72 → `GROUND_RECEIPT`, r73/r74 ×4 → empty; `head -2 round-74 selftest-ca.txt` line 2 = `selftest: clean -> exit=0 …` | ✅ |
| 23 | addendum "sits at the file's end" | `QUALITY.md:164` | end | file is 197 lines; addendum block 164-197, last non-empty line 197 | ✅ |
| 24 | SKILL `:701` repair landed; round-75 gate rows state 13/13 and 12/12 | `SKILL.md:701`, `:707`, `:708` | match | `:701` carries "this is narrative evidence, not a standalone committed receipt"; `:707` `legs=13/13`, `:708` `legs=12/12` (and states "COMBINED needs `--combined`") | ✅ |
| 25 | `accept-c.py` prints `PASS legs=13/13` | lesson:11-12 | 13/13 | run in clone: `ACCEPT-C-75: PASS legs=13/13` | ✅ |
| 26 | `accept-ca.py` prints `PASS legs=12/12` | lesson:14, claims Ca `after` | 12/12 | run as printed in `after` (no `--combined`) → **`FAIL legs=10/12`** (COMBINED fails: "the explicit --combined revision is required"); 12/12 only with `--combined 4f5e3b2` | ❌ **F6** |
| 27 | lesson:3-5 "base … (also HEAD; no freeze commit exists — `git cat-file -e HEAD:reports/round-75/claims.json` → absent … this lesson grades none of them)" | lesson:3-5 | absent | `git cat-file -e 4f5e3b2:reports/round-75/claims.json` → **present**; also present at the freeze; `git merge-base --is-ancestor 5d01674 4f5e3b2` → 0 | ❌ **F1** |
| 28 | "the claims are `DRAFT`" | lesson:15 | DRAFT | `claims.json.status` = `"FINAL — wave-1 and wave-2 attacks applied; frozen by the commit that adds this file …"` | ❌ **F2** |
| 29 | R75-M1 "At this wave `git cat-file -e HEAD:reports/round-75/claims.json` still fails" | lesson:313-315 | fails | present at `4f5e3b2`, present at `5d01674` | ❌ **F3** |
| 30 | R74-M8 "at this wave neither is committed (`git cat-file -e HEAD:reports/round-75/accept-c.py` fails)" | lesson:330-333 | absent | `accept-c.py` present at `5d01674` **and** `4f5e3b2`; `accept-ca.py` likewise | ❌ **F4** |
| 31 | `used-by` rewrite: S885 → base + amend-23; S886/S887/S891/S892 → amend-23; S888/S889/S890/S893 → base | lesson:244-246 | as stated | landed cells: S885 → base + amend-23 **+ amend-23b**; S891 → **amend-23b**; S892 → **amend-23b**; rest as stated. The landed mapping is the one the three entries' `source:` lines produce, and the counter's ROWS leg passes on it | ❌ **F7** |
| 32 | Gate note 3 "**three times**" whole-document; "The other six declare `excerpt`" | lesson:53-56 | 3 whole / 6 excerpt | `grep -h '^window-scope:' reports/round-75/evidence/*.txt \| sort \| uniq -c` → **4 whole-document / 5 excerpt** (S891 is whole-document, 2169 visible) | ❌ **F8** |
| 33 | R74-M6 pointer "this round exercises it three times" | lesson:325-327 | 3 | 4 | ❌ (same defect as F8) |
| 34 | Gate note 2 "Two stored windows would fail the EVIDENCE leg as they stand. S888's window (`chars=4097 before=10`) and S892's (`chars=4097 before=284`) both start at the document head and stop well before p. 3 and p. 7" | lesson:46-52 | fail / 4097 / before=10 / before=284 | landed evidence: S888 `chars=4096 … before=3266`, S892 `chars=4097 … before=2020`; the Gate quote occurs in **both** stored windows after NFKC+fold, and `window-sha256` recomputes in all nine files | ❌ **F9** |
| 35 | S888 Gate cell "`excerpt` window 4097 (visible 5481); the anchor quote is **not** in that stored window (note 2)" | lesson:34 | 4097 / not present | 4096 / **present** | ❌ F9b |
| 36 | S885 Gate cell "HTTP 200, 111486 B, body sha256 `2bcdd019…`" | lesson:28 | 111486 / 2bcdd019 | the probe receipt says that; the committed `reports/round-75/evidence/S885.txt` says **109588 B / 20b571d7a6a9…** | ❌ **F10** |
| 37 | S887 Gate cell "HTTP 200, 118776 B, sha256 `fbf48ad2…`" | lesson:30 | 118776 / fbf48ad2 | probe receipt; committed evidence **116878 B / e056064986d5…** | ❌ F10b |
| 38 | Gate note 4 "Three stored observations of S885 disagree … (111487 / 9be2c68d; 111486 / 2bcdd019; 109589 / 25cfd7f6). S886 and S887 drift the same way (109335 vs 111234; 118776 vs 118777)" | lesson:57-63 | 3 observations | there is a **fourth**, the artifact the EVIDENCE leg grades (109588 / 20b571d7), absent from the note; S887's committed value 116878 is neither 118776 nor 118777 | ❌ F10c |
| 39 | entry `verified-at` "byte counts 111487 / 225123 / 1085244 / 697092 / 45238 for the notice, the syllabus PDF, the two J-STAGE PDFs and the article page" | `narrative-structure-frameworks.md:8` | 111487 | committed evidence: 109588 / 225123 / 1085244 / 697092 / 45238 (four of five match; S885 does not) | ❌ **F11** |
| 40 | Gate "the per-row fetch line lives in the receipt named in the evidence column"; "Every quote below is the text inside that row's `anchor` cell in `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md`" | lesson:21-24 | path named | that directory **never existed in any commit** (`git log --all -- '.ufo/waves/round-75/assimilation/validate/*'` → 0; `ls-tree 5d01674 .ufo/waves/round-75/assimilation/` has no `validate/`). The nine Gate quotes *do* match the landed `corpus/SOURCES.md` anchor cells (verified 9/9) | ❌ **F12** |
| 41 | "One normalization defect found and not repaired here. In `…amend-2026-10-23.md:11` the S892 `source:` line's URL is hard-wrapped mid-percent-escape — the line ends `…2014%20marrone%20age%`" | lesson:250-255 | defect present | no line in any entry ends with `%`; `amend-2026-10-23.md:11` is `- sources:`; the S892 `source:` line is `amend-2026-10-23b.md:5` and carries the full URL on one line. Routed item 6 repeats the dead defect | ❌ **F13** |
| 42 | "S891 and S893 have no probe receipt" / "the receipts that would bind them … do not exist at this wave" | lesson:64-67, :34, :36 | no receipt | true of `counters/probe-receipts/` (7 receipts for 9 rows), false as a statement about capture: `reports/round-75/evidence/S891.txt` and `S893.txt` are committed with fetch line, HTTP 200, bytes, sha256, window | ⚠️ stale (minor) |
| 43 | round-75 axes rows in SCORECARD | `SCORECARD.md` | (seats enumerated in this wave) | **absent**: no `## Axes — round 75`; last is `## Axes — round 74` (`:1455`), and `git show 82ced5c -- SCORECARD.md` is empty. Every round 67-74 has a section. Owed by a later wave (`RevScorecardCorrections` is in the w3 roster), not by these two claims | ⚠️ gap, not a false number |
| 44 | census `Rows 808 → 817, exit 0 both times` | lesson:300 | 808/817, exit 0 | `reports/round-75/telemetry/census-end.txt` is real (35 lines, `exit=0`, W04 ×28, W01 ×4 = S881/S882/S884/**S893**), and the lesson's pasted block is that file byte-for-byte (one trailing blank line aside); but the census prints **no row count** — 0 occurrences of `808`/`817` — and `census-start.txt` carries no `exit` line | ⚠️ derived, not printed |

Counters, for the record: **C 13/13 PASS**, **Ca 12/12 PASS** (with `--combined`), and the Ca run's
do-nothing/frozen-config legs behave as the claim states.

---

## 3. Defects, ranked

**F1 — the landed lesson says the round is not frozen (lesson:3-5).** Stated: *"base `f556d1049…` (also HEAD; no freeze commit exists — `git cat-file -e HEAD:reports/round-75/claims.json` → absent, so the round's files are untracked working bytes and this lesson grades none of them)"*. At the commit that carries the sentence, `claims.json` is present and `5d01674` is an ancestor. Severity: high — a reader takes the lesson as ungraded draft prose while it is the landed Gate/Quarantine record the claims' GATE leg points at.

**F2 — "the claims are `DRAFT`" (lesson:15).** `claims.json.status` begins `FINAL`. High (it is the sentence that tells a reader the predicates do not bind).

**F3 — R75-M1's live assertion (lesson:313-315).** "At this wave `git cat-file -e HEAD:reports/round-75/claims.json` still fails" — false at both `5d01674` and `4f5e3b2`. Medium.

**F4 — R74-M8's live assertion (lesson:330-333).** "at this wave neither is committed (`git cat-file -e HEAD:reports/round-75/accept-c.py` fails)" — both counters are in the freeze commit. Medium (it asserts a missing receipt where the receipt exists, the exact class R74-M8 was about).

**F5 — adopted byte sizes bound to the staged copies (lesson:92-95).** 6862/5933/2514 B are the `shokuknow` staged sizes; the three lane paths the sentence names are 30920/24166/23049 B. The mirror receipt's own entry digests (`3ea4d6f8…`, `25992609…`, `63a4d5bf…`) equal the landed files, so the numbers are simply the wrong artifact — QUALITY 27's class, in the triage prose.

**F6 — Ca's printed command does not reproduce its own verdict.** `claims.json` Ca `after` and lesson:14 print `accept-ca.py --root . --lands … --freeze … --fleet-root …` "prints ACCEPT-CA-75: PASS legs=12/12". Run verbatim: `LEG FAIL COMBINED` → **`FAIL legs=10/12`**. The committed receipt (`telemetry/measures-ca.txt`, header line 3) and `SKILL.md:708` both carry `--combined`; the claims' text drops it. Low-medium (a reader re-running the claim gets a red).

**F7 — `used-by` rewrite sentence contradicts the landed rows (lesson:244-246).** Three of nine rows are misdescribed: S885 lacks `amend-2026-10-23b`, and S891/S892 are attributed to `amend-2026-10-23` where the registry (correctly, per their `source:` lines, and per the counter's ROWS leg) says `amend-2026-10-23b`. Root: the sentence copies `validate-receipt-draft.txt:320-326` (`USEDBY PASS`), which is the pre-move mapping; the final `validate-receipt.txt` (46 lines) contains no USEDBY block at all, so the "checked both ways" citation points at a draft. High for a counts seat: it is the row→entry census of this claim.

**F8 — whole-document / excerpt census off by one (lesson:53-56, :325-327).** 4 whole-document, 5 excerpt; the lesson says 3 and 6, twice. Low.

**F9 — note 2 describes windows that no longer exist (lesson:46-52) and S888's Gate cell asserts non-presence (lesson:34).** Landed: S888 `chars=4096 before=3266`, S892 `chars=4097 before=2020`; both contain the Gate quote after folding; all nine `window-sha256` recompute. The note's *requirement* ("must therefore window p. 3 and p. 7") was met; the note's *state* was not updated, and the S888 cell's "**not** in that stored window" is false. Medium — it tells a reader the landed evidence fails the leg the counter passes.

**F10 — two Gate rows carry the probe receipt's bytes/sha as if they were the stored record (lesson:28, :30, :57-63).** S885 111486/`2bcdd019` vs evidence 109588/`20b571d7`; S887 118776/`fbf48ad2` vs evidence 116878/`e0560649`. The nine rows are otherwise consistent (S886, S888, S889, S890, S891, S892, S893 all match their evidence byte counts). Note 4's "three observations" omits the fourth — the committed one. Medium-high: the byte/digest pair is exactly the number a QUALITY-22 reader checks.

**F11 — the base entry's `verified-at` asserts 111487 B for S885** (`narrative-structure-frameworks.md:8`), a fourth distinct value (evidence 109588, probe 111486, w1 111487, rehearsal 109589). Same class as F10, inside the admitted entry rather than the lesson. Low-medium.

**F12 — the Gate points quotes at a path that never existed.** `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md` is absent from every round-75 tree (rounds 72-74 have their `validate/` dirs; round 75 does not). The nine quotes do resolve against the landed `corpus/SOURCES.md` anchors, so the claim is true and the pointer is dead — the R74-M8 class again. Low.

**F13 — the "not repaired here" normalization defect is not there** (lesson:250-255, Routed item 6): no entry line ends mid-percent-escape, the cited file/line do not carry an S892 `source:` line, and `amend-2026-10-23b.md:5` carries the full URL on one line. A reader re-running the described check finds nothing. Low-medium (it is the one item in the lesson presented as an open defect at landing).

**Stale-minors.** (a) "S891 and S893 have no probe receipt … not yet captured as one" — true of `counters/probe-receipts/`, but committed evidence exists for both and the Gate never names `reports/round-75/evidence/<id>.txt` for any of the nine rows, although its column header says "this wave's stored record". (b) `Rows 808 → 817` is not printed by either census receipt (`census-start.txt` also has no `exit` line). (c) No `## Axes — round 75` in SCORECARD at `4f5e3b2` or `82ced5c`, where rounds 67-74 all have one; that is a later-wave obligation, recorded here only so the gap is not mistaken for a measured zero.

---

## 4. What survives the sweep (for the critic's balance)

Every headline total re-derives at `4f5e3b2` with no drift: 808→817 rows, 713/58/37→722/58/37 statuses,
249→252 files, README footer 252 with vector 32/32/40/29/24/95 and the `## myth-symbol/ (32)` heading, the
three base footers preserved in order, nine quote lengths exact to the character and token, the 40-file
triage arithmetic, all six staged/lane digest pairs, the three guard artifact digests and the guard-proof
matrix, the 21-row quarantine slice with its 18+3 split and 10/7/4 verdict histogram, the 10-pair ledger with
its 6/4 split, the four SCORECARD correction tokens, the QUALITY 23 addendum's six measured rows, the two
SKILL gate rows, and the census-end receipt (28 W04 / 4 W01 / `exit=0`). Both counters pass: C 13/13, Ca 12/12.

---

## 5. Blockers

None. Nothing was edited outside this report and `$S`; the lane worktree, index and refs were never touched
(all git use was read-only); `shokuknow` was read-only; no tool was installed.
