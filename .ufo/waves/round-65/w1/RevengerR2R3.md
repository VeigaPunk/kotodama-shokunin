# RevengerR2R3 — OVER-CORRECTION attack on R2/R3 (round 65, wave 1)

Seat: kotodama-r65.RevengerR2R3 · 2026-10-24 · base `17c32302c6845c8f164b985a8cb312d3181c8788`
Scope: spotcheck R2/R3 (corpus/lessons/round-64-verifier-spotcheck.md §6 items 2–3), targets
`reports/round-63/telemetry/revisions.txt`, `/home/vgpnk/Projects/shokunin/.ufo/reports/round-64/kotodama.md` (read-only), `SCORECARD.md` round-64 rows, frozen `reports/round-65/accept-ca.py` legs R2/R3.

## 0. Dependency (recorded per instructions)

**ExecRecordsFix draft ABSENT.** `.ufo/waves/round-65/stage/records-fix/` does not exist (checked twice during the window; `stage/` holds only `mut-o/`); `.ufo/waves/round-65/w1/` had no ExecRecordsFix report. The build seat has not landed. Consequence: I cannot attack the draft's actual bytes; I attack the surfaces the frozen counter + spotcheck define for R2/R3 and state the exact contract any conforming draft must meet. Everything below is grounded in committed/current bytes I measured myself.

## 1. Verified ground truth (all commands run by me)

- Working tree `reports/round-63/telemetry/revisions.txt` sha256 `a321e8aa…` == `git show 17c32302:…` byte-identical. The file's only commit is `6f3e0b2` (created once with its round-64 inline corrections; never edited since). R2 leg precondition intact pre-fix.
- Spotcheck R2 premise TRUE: `git rev-parse 8d2041fa:reports/round-63/telemetry/final-measures-c.txt` → fatal "not in '8d2041fa'"; adder = `0c892ceac42fc1ef13b27d9705e622eda63f4473` (2026-10-23 16:45:04, "round-63: records … ACCEPT-C-63 PASS at 8d2041fa").
  Note: the first probe must target the **round-63** path — `reports/round-64/telemetry/final-measures-c.txt` is a different file, added by `8bab271c`.
- False clauses in base bytes: line 10 `measured 8d2041fa…`, lines 12–13 "8d2041fa is … the commit that added this receipt" — line 12 **contradicts line 11** ("added by 0c892cea…", true). The file is internally inconsistent today; that is what R2's named correction must resolve.
- R3 ground truth: lane `.ufo/waves/round-64/w1/ReviewerCa.md` exists; **no** `w2/ReviewerCa.md`. The filed round-64 report cites `w2/ReviewerCa.md`; **`SCORECARD.md:1235` (round-64 calibration row, measured-evidence cell) also cites `w2/ReviewerCa.md`, and cites it at `8bab271c` too** (git show: exactly one `ReviewerCa` token, the w2 one). LOG.md pre-state: zero `ReviewerCa` tokens; zero `Correction (round 65, R*)` markers in LOG/SCORECARD → R3 leg is not pre-satisfiable.
- Filed report: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-64/kotodama.md` (sha256 `31bf623a…`) is **tracked in the fleet repo**, commit `e1fe5c9` "kotodama-shokunin round-64: kotodama report". No copy exists under the lane repo. It is outside this round's write scope by rule.
- LOG.md:4161 repeats the R2 falsehood: "…revisions.txt records the measured revisions … including 8d2041fa (final-measures-c.txt)…".

## 2. Verdict A — does the R2 correction preserve originals byte-identically and append below?

**The frozen leg enforces exactly that shape; the (absent) draft must comply with it.**

`accept-ca.py` R2: `r2_original_intact` requires base bytes to be an **unchanged prefix** of the corrected file (`base_rev == rev_text[:len(base_rev)]` and startswith check) → all 37 original lines, including the *false* ones (10, 12–13), must survive byte-identically; the correction can only live below. The MutRecords mutant "rewrite the false clause in place" is killed (any in-place byte change breaches the prefix → R2 FAIL). Fail-closed: unreadable file → FAIL. Verified: worktree currently == base, so the check measures only the fixer's delta.

Gaps found (residuals, none blocking):

1. **Substance not machine-checked (HIGH-1 token surface).** `r2_named` = `"Correction (round 65, R2)" in rev_text and "final-measures-c.txt" in rev_text` — the filename half is **already true at base (line 10)**, so a vacuous marker line appended with false or empty prose PASSES. The leg never requires `0c892cea` (true adder) or the "absent at 8d2041fa" statement inside the correction. Necessary-not-sufficient, per the receipt doctrine — but the docstring names that content, so the leg could pin it cheaply.
2. **Docstring over-asserts vs the routed defect (over-correction pressure on prose).** Spotcheck R2 routes the **adder** falsehood ("8d2041fa added final-measures-c.txt — false; added by 0c892ce"). The counter docstring additionally declares the header clause "measured 8d2041fa" false *because the path is absent at 8d2041fa*. Those are different claims: the receipt bytes omit their measured revision (routed defect 8 — `grep -c 8d2041fa final-measures-c.txt` = 0), and the adding commit's own subject says "ACCEPT-C-63 PASS **at 8d2041fa**". Absence of the file at a revision does not by itself falsify what a run measured. [INFERENCE] The provable correction is: adder = 0c892ce, path absent at 8d2041fa, measured revision unverifiable from receipt bytes (subject-derived only). A draft that "corrects" line 10 to a flat negative risks replacing one unproven claim with another.
3. **Cosmetic:** a correction appended with no separating newline still passes (prefix holds; marker glues onto line 37). Draft should start the entry on a fresh line.
4. Counter hygiene: `SPOTCHECK` constant in accept-ca.py is unused; second prefix condition (`startswith(base_rev.rstrip("\n"))`) is redundant.

**Repeat-surface gap (the real under-coverage):** `LOG.md:4161` repeats the false "8d2041fa (final-measures-c.txt)" attribution in the lane's own round-64 record. R1's repeats are leg-enforced (LOG/SCORECARD/LessonFinal markers); **R2's repeat has no leg and no routed instruction**. Unless the L1 folds it into the round-65 LOG entry voluntarily, ACCEPT-CA-65 can PASS with LOG.md still asserting the falsehood. Recommend: ExecRecordsFix/L1 append an R2 correction to LOG.md as well (append-only, named).

## 3. Verdict B — is the R3 route (erratum in round-65 report + lane records; filed report untouched) consistent with append-only convention and write scope?

**YES — it is the only conforming route.** Evidence:

- The filed report is a **fleet-repo tracked** file (`e1fe5c9`, lane identity); the lane has no copy. Correcting it in place would mutate the fleet repo — prohibited by this round's rules — and rewrite a filed artifact, against the append-only convention ("append-only wherever the target is a filed record", accept-ca docstring).
- The route's writes are all successor records: round-65 report erratum + LOG entry + SCORECARD correction table — appends, not edits of filed bytes. Identical pattern to R1's treatment of the filed-report repeat ("corrected by the round-65 report's erratum; the filed report … stays byte-preserved"). Precedent also exists in LOG (round-51: misrooted report moved byte-exact, never rewritten).
- The frozen R3 leg never reads the fleet path, so passing it creates zero pressure to write out of scope. Consistent.

Gaps found:

1. **Spotcheck R3's parenthetical is factually wrong.** "(SCORECARD cites both correctly)" — `SCORECARD.md:1235` cites only `w2/ReviewerCa.md` (wrong; actual `w1/ReviewerCa.md`), at HEAD and at the spotcheck's judged `8bab271c` alike. An L1 following the spotcheck alone may never touch SCORECARD:1235.
2. **The R3 leg cannot catch that.** `r3_ok` requires both path tokens in **LOG** and the bare marker `Correction (round 65, R3)` in **SCORECARD** — it never requires `w1/ReviewerCa.md` in SCORECARD, never requires SCORECARD:1235 to be corrected (and if it were edited in place, append-only would be breached with the leg still green). A marker-only SCORECARD append plus a substantive LOG entry PASSES while the wrong citation survives at SCORECARD:1235. Recommend the erratum explicitly name `SCORECARD.md:1235` as corrected-to-`w1/ReviewerCa.md` (appended correction row), and a future counter rev pin `w1/ReviewerCa.md` in score_text.
3. Leg reads only LOG+SCORECARD; the "erratum in the round-65 report" half of the route is unverifiable by the instrument (report doesn't exist at counter time / is never read). Accepted as necessary-not-sufficient; noting for the record.

## 4. Contract the absent draft must satisfy (for ExecRecordsFix/L1)

- `revisions.txt`: keep all base bytes sha `a321e8aa…` as unchanged prefix; append below a fresh-line entry starting `Correction (round 65, R2):` naming final-measures-c.txt, the true adder `0c892cea…`, path absent at `8d2041fa`, and the measured-revision provenance stated honestly (subject-derived; receipt bytes omit it) — do NOT rewrite lines 10–13, do NOT delete the round-64 inline corrections.
- Lane records: append `Correction (round 65, R3)` to SCORECARD naming `.ufo/waves/round-64/w1/ReviewerCa.md` as actual and `w2/ReviewerCa.md` as the erratum'd wrong path — including for SCORECARD:1235; LOG entry names both paths (actual first). Do not touch `/home/vgpnk/Projects/shokunin/.ufo/reports/round-64/kotodama.md`.
- Optional but recommended: LOG correction for the R2 repeat at LOG.md:4161.

## 5. Findings summary

| # | severity | finding |
|---|---|---|
| F1 | dependency | ExecRecordsFix draft absent (`stage/records-fix/` missing); attacked frozen surfaces instead |
| F2 | MEDIUM | R2 leg marker+filename half pre-satisfied at base → vacuous-prose correction PASSES; substance (0c892cea / absent-at-8d2041fa) unpinned |
| F3 | MEDIUM | R2 repeat at `LOG.md:4161` uncovered by any leg/instruction — falsehood can survive a green ACCEPT-CA-65 |
| F4 | MEDIUM | spotcheck R3 parenthetical "(SCORECARD cites both correctly)" false at `8bab271c` and base: `SCORECARD.md:1235` cites only wrong `w2/ReviewerCa.md` |
| F5 | MEDIUM | R3 leg never requires `w1/ReviewerCa.md` in SCORECARD → wrong citation survives marker-only PASS; in-place SCORECARD row edit also undetected (over-correction not killed) |
| F6 | LOW | counter docstring's "header clause 'measured 8d2041fa' is false" over-asserts vs the routed adder defect; risk of correcting a subject-backed claim into an unproven negative |
| F7 | LOW | append-without-newline passes R2 (glued marker); SPOTCHECK constant unused; redundant second prefix condition |

Verdicts: **R2 shape enforceable and enforced (byte-identical prefix + append-below, in-place mutants die) — but under-enforced on substance and its LOG repeat. R3 route consistent with append-only convention and write scope — the filed fleet report stays byte-preserved and the leg creates no out-of-scope pressure — but the routed premise about SCORECARD is wrong and the leg under-covers SCORECARD:1235.** No tool installs this session (host git/sha256sum/grep only; pacman pause respected).
