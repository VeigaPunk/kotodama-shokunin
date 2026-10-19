- Seat: R08 | reviewer | claim A | date 2026-10-19 | baseline 139e3b6

# R08 — second pass over `adj/`, focused on A09's pin-cascade correctness

**Mission** (`reports/round-33/targets.json:72`): "Second pass over adj/ with focus on A09
pin-cascade analysis correctness (would the proposed shared-file edits actually break a
pin?)." **Out:** this file only.

**Method.** I did not restate A09 (`adj/A09-pins.md`, landed). I re-ran every A09 command
that bears on a pin, and I executed the two *asserting* code paths A09's inventory classes
describe but does not run (the round-30 box-1 binding, the round-25 runner's run guard).
Read-only throughout: `python3 reports/round-30/run-validation.py --check` prints the
measured JSON and writes nothing (`reports/round-30/run-validation.py:892-893,918-919`);
its output was redirected to `.scratch/r08-r30-check.json`. No filed byte was written.
Window: 2026-10-19T04:0x–04:3xZ, HEAD `139e3b6`, env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## 1. Direct answer to the mission question

| proposed edit | breaks a pin? | which, and how |
|---|---|---|
| in-place reconciliation of `corpus/lessons/README.md` (claim O) | **YES — by construction** | `reports/round-26/run-validation.py:97` hard-codes the README's Git blob `a3187055…`; `:1498-1501` fails with "the filed lessons index was edited in place … the claim requires a new revision file, not an in-place edit". The same constant is mirrored in `reports/round-26/lessons/c51-revision-audit.py:48,199-203` (`C52-7_filed_unchanged`). No frozen manifest, `expected.json`, or freeze receipt moves (independently confirmed, §2). |
| SKILL.md edits (C14's pointer fixes) | **no *new* break — but only because the one hard binding is already red** | `reports/round-30/run-validation.py:679` asserts the live SKILL.md sha256 appears in a **round-30** markdown document (`bound = bool(section) and digest in text`), failing at `:698`. Measured now: live `79fe91d3…` occurs **0×** in `reports/round-30/craft/review-D29-box1.md` while the pinned `83b0a78a…` occurs once; `--check` reads `claim D passed=false` with exactly that failure. SKILL.md changed at `17e90b9` (round-31 admit, 2026-10-18T21:28:45-03:00), so this leg has been red since round 31 — before round 33. A round-33 edit neither creates nor repairs it. |
| line-count-changing SKILL.md edit (e.g. the `AGENTS.md:42` append) | **stales filed line anchors** | `AGENTS.md:42` instructs "append one item … (after :534)"; an insertion at `:534` shifts every line below it, including the r31-landed item `SKILL.md:713-715` and the filed citations `corpus/lessons/round-31.md:46` (`:535`, `:536`) and `corpus/lessons/round-32.md:33,41` (`:660`, `:710`, `:713-715`). C14's drafts are same-line-count replacements (`reports/round-33/calib/C14-fix-drafts.md:510-511`), so C14 alone is safe; the AGENTS.md append is the shift. |

## 2. A09 verification — what holds under independent re-execution

| A09 item | my command / read | result | verdict |
|---|---|---|---|
| E1 r26 blob pin | `git hash-object corpus/lessons/README.md`; `git rev-parse HEAD:corpus/lessons/README.md`; `sed -n '97p;1494,1501p' reports/round-26/run-validation.py` | `a31870556c733498243b56697896504a2fb3679a` both; constant and failure text exactly as A09 quotes | **holds** (A09 cites `:1494-1500`; the `failures.append` spans `:1498-1501`) |
| E1 re-run hazard | `sed -n '90p;1871p;1909p'` r26 runner | `OUTPUT` `:90`, `--check` `:1871`, write `:1909` | **holds** |
| E1 revision-file requirement | `sed -n '1503,1507p'` | "no new lessons README revision landed under reports/round-26 … requires the README updated as a new file" | **holds** |
| §1.1 frozen surface | `grep -rc 'lessons/README\|SKILL.md' tools/gates/frozen/*/MANIFEST.tsv tools/gates/frozen/*/*/MANIFEST.tsv` | total **0** | **holds** |
| §1.1 baselines | python enumeration of every `expected.json` `inputs` map under `tools/gates/expected`, `tools/gates/frozen`, `reports/round-9/baselines` | **20 baselines, 45 distinct input keys, 0** naming README/SKILL.md | **holds** |
| §1.2 source-ledger digests | `sha256sum corpus/lessons/round-6-sources/{05,03,13,09}.json` | `a00a5dc4…`, `adb22c9a…`, `69504356…`, `0dd2820d…` — all four exact | **holds** |
| E2 r25 receipt is a *record*, not a live pin | `grep -n corpus/lessons/README.md reports/round-25/validation.json`; `sed -n '98p' reports/round-25/run-validation.py` | `:1020` = `ec7469da…` = live sha256; r25 `PROTECTED` = `reports/round-8..24` + `tools/gates/frozen/round-8..24` — README not protected | **holds; A09's classification is the correct one** (A10/A13's "pinned twice" overstates — see F5) |
| E2 other digest sites (spot-check) | `sed` at the cited lines | `reports/round-26/audit/x63-lessons-receipt.json:75`, `reports/round-25/lessons/C35-C36.md:156,229`, `reports/round-26/lessons/C53.md:144`, `reports/round-26/scribe/fragment-ledger.json:401`, `reports/round-32/dossier-d11-shonen-boxes.md:50`, `reports/round-30/validation.json:449` all carry the digests A09 lists | **holds** |
| E3 box-1 instrument | `python3 -B reports/round-30/craft/box1-survey.py` path + `head -8 box1-landed-survey.json` | receipt `skill_sha256 83b0a78a…`, `named_in_skill 28 / resolvable 28` | **holds** |
| E4 anchors | `wc -l SKILL.md corpus/lessons/README.md AGENTS.md`; `sed -n '42p' AGENTS.md`; `sed -n '522p;534p;536p;713,715p' SKILL.md` | 715 / 346 / 42; `AGENTS.md:42` verbatim as quoted; `## Checklist` `:522`, last content `:534`, `## Corpus map` `:536`, item `:713-715` | **holds** |
| E5 c31 before-state | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 1; `FAIL C31_index_rows_eq_files` + `FAIL C34b_prose_arithmetic`; `C31-1` = the seven r26–r32 files; `C34-2` stated `[26,26]` measured `[26,33]` | **holds** |
| E5 README prose sites | `sed -n '97p;207p' corpus/lessons/README.md` | `**Rows: 26. Files: 26.**`; `Rows: **49**. Of the 26 index rows, **23 carry at least one question**` | **holds** |
| E5 peer instruments | `x45` (exit 1, `X45-P1` round-4 glob); `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` (34/37); `grep -rn x57 reports/round-2[6-9]/run-validation.py reports/round-3[0-2]/run-validation.py` (0 hits) | all three reproduce | **holds** |

## 3. Corrections and additions (severity-ranked)

**R08-F1 — material: the SKILL.md half of the "pinned nowhere" conclusion is false at the
runner level, and A09's E3/R4 understate the consequence.** Round-30's runner does not only
"make a dated receipt a claim requirement" (`A09-pins.md` §2.3); it *asserts* the live
SKILL.md digest against a round-30 document (`reports/round-30/run-validation.py:679,698`).
Executed now:

```
python3 reports/round-30/run-validation.py --check   # read-only
acceptance_checks_passed: False
failures: ["claim D: box-1 executable re-survey has no dated receipt pinned to the post-landing SKILL.md bytes"]
skill_sha256: 79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d
box1_resurveys[0]: {"path": "reports/round-30/craft/review-D29-box1.md", "post_landing_digest": false, "passed": false}
```

`grep -c 79fe91d3 reports/round-30/craft/review-D29-box1.md` → `0`; `grep -c 83b0a78a` → `1`.
Two consequences A09's R4 does not carry:

1. The binding is **already red at HEAD** (pre-existing, caused by `17e90b9`, not by round
   33). The correct record is "standing red, superseded by the round-32 dossier's box-1
   closure at `79fe91d3…` (`reports/round-32/final-dossier.md:46`)", not "an edit will break
   it".
2. **R4 as written cannot green that leg.** `documents()` scopes to
   `safe_path(ROUND).rglob("*.md")` with `ROUND = "reports/round-30"`
   (`reports/round-30/run-validation.py:24,290-294`), so only a digest match inside a
   `reports/round-30/` markdown file satisfies it — a round-33 receipt never will, and
   writing a new file into a filed round directory is outside round 33's write surface.
   R4's honest purpose is the *forward* pin (the next survey at the post-edit digest for the
   round-33 record), not a repair of r30's leg.

This correction also lands on A10's A09 row ("SKILL.md is pinned nowhere") and on R07-F4,
whose confirmations were scoped to `tools/gates/frozen/**` — true there, incomplete as a
whole-file verdict. A09's own E3 is closer than either; F1 tightens it, it does not reverse
it.

**R08-F2 — material: quantify R5's line-neutrality against the `AGENTS.md:42` append.**
`AGENTS.md:42` is a live instruction to *append* a checklist item after `:534`; C14's drafts
are same-line-count replacements (`C14-fix-drafts.md:510-511`). The two are not the same
class of edit: C14 alone leaves every line number intact, while the AGENTS.md append inserts
lines at `:534` and stales the r31/r32 filed citations A09's E4 lists
(`corpus/lessons/round-31.md:46` `:535`,`:536`; `corpus/lessons/round-32.md:33,41` `:660`,
`:710`, `:713-715`). R5 should say: *C14 drafts are line-neutral by construction; the
AGENTS.md:42 append is not, and if it is applied the shift and the staled citations must be
recorded.* The append also collides with the already-landed item at `:713-715`, which X00
already names (`cross/X00-connector.md:68`).

**R08-F3 — procedural: restate E1's remedy as a declared supersession, not a standing
rule.** "Round-26's runner is not re-run at the round-33 revision" (R1) is policy; the
mechanical fact is that the r26 claim-C leg fails *by construction* after any in-place README
edit, and nothing short of editing filed bytes can re-green it. The round record should say
so and cite the r20 re-pin precedent A13 names (`A13-verify-a07-a09.md:148-152`), rather than
imply the runner is merely "not consulted".

**R08-F4 — minor, cross-file: X00's §3 mis-records one exit code and omits two asserting
sites.** `cross/X00-connector.md:172-173` and `:312` record `python3
reports/round-25/run-validation.py` as `exit 0`; measured: `exit 2` with `could-not-evaluate:
run round validators only in an isolated Git clone under the lane's .scratch` (guard at
`reports/round-25/run-validation.py:1124-1127`). X00's live-instrument list (five readers)
also omits the two *asserting* sites: the r26 runner's blob pin and the r30 runner's box-1
binding. A09's R1 covers the first; neither covers the second as a live assertion (see F1).
For the integrator's R↔X00 match, A09 is the superset on pins — carry the direction
A09→X00, not the reverse.

**R08-F5 — minor, precision credit where due.** A10's and A13's "the lessons README is
pinned twice, both pins currently intact" (`adj/A10-receipt.md` A09 row; F1 in
`A13-verify-a07-a09.md:89-101`) reads `reports/round-25/validation.json:1020` as a live pin.
It is a recorded measurement: r25's runner builds that map from its own run and never
compares it to a filed baseline (r25 `PROTECTED` excludes the README; the runner additionally
refuses to run in-lane, exit 2). A09's E2 classification is the correct one; the assembled
audit should use A09's wording, and the two "pins" reduce to one hard pin (r26) plus one
mirrored filed auditor (c51 `C52-7`).

## 4. Not verified here (`to-verify`)

- Post-integration state of every pin above — all measurements are pre-integration point
  readings; the integrator's re-measure after applying O/C drafts is the control (A09 §3
  R1–R8, my F1–F3).
- Whether C14's drafts, applied literally, preserve SKILL.md line counts on the integrator's
  tree — C14 asserts it (`:510-511`); I verified the *targets* (`:128,213,479,481,483,485,486,
  488,490,491,501,701-704` are the cited lines and the digest at the cut is `79fe91d3…`), not
  the applied diff.
- `reports/round-30/run-validation.py` claim C/O legs at HEAD read `passed=true` in my run;
  I did not audit those legs beyond the box-1 failure.

## Owed

- `reports/round-33/adj/audit-assembled.md` (integrator) — carry A09's R1–R8 with F1's two
  corrections (already-red box-1 binding; R4's scope), F2's append caveat, F3's supersession
  wording, F4's X00 exit-code errata, and F5's A10/A13 wording errata.
- The R1–R8 ↔ X00 §3/§4 row match (A09's own `## Owed`; A09 §5 keys it to X00, which has now
  landed). Two X00 rows have no A09 counterpart (nothing) and two A09 rows have no X00
  counterpart (r26 runner assertion, r30 box-1 assertion) — the match is not one-to-one.
- Post-integration re-measure: `python3 reports/round-30/run-validation.py --check` (expect
  the same single failure until the filed r30 bytes change), `python3 -B
  reports/round-25/audit/c31-lessons-index-audit.py` (expect exit 0, findings 0), and a fresh
  `reports/round-30/craft/box1-survey.py` receipt pinned to the new SKILL.md digest.

## Citations

- `reports/round-33/targets.json:56,72` (A09 mission, R08 mission), `:7,10` (shared rules)
- `reports/round-33/adj/A09-pins.md` (§1–§5, R1–R8, A09-F1..F5); `adj/A10-receipt.md` §1 A09
  row, §2 A10-F5/F10; `adj/A13-verify-a07-a09.md:89-101,116-161`; `review/R07-adj-review.md:138-168,223-281`
- `reports/round-33/cross/X00-connector.md:66-68,128-199,172-173,312`; `reports/round-33/calib/C14-fix-drafts.md:505-520,545`
- `reports/round-26/run-validation.py:90,97,1494-1501,1503-1507,1871,1879,1909`;
  `reports/round-26/lessons/c51-revision-audit.py:48,198-203`
- `reports/round-30/run-validation.py:24,290-294,679,698,888-925`;
  `reports/round-30/craft/review-D29-box1.md:162`; `reports/round-30/craft/box1-landed-survey.json:4-5`;
  `reports/round-30/validation.json:449,1420`
- `reports/round-25/run-validation.py:98,862,1124-1127`; `reports/round-25/validation.json:1020`;
  `reports/round-25/audit/c31-lessons-index-audit.py:36`; `reports/round-25/audit/x45-lessons-pointer-audit.py`
- `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`;
  `reports/round-32/final-dossier.md:46`; `reports/round-26/audit/x63-lessons-receipt.json:75`;
  `reports/round-25/lessons/C35-C36.md:156,229`; `reports/round-26/lessons/C53.md:144`;
  `reports/round-26/scribe/fragment-ledger.json:401`; `reports/round-32/dossier-d11-shonen-boxes.md:50`
- `AGENTS.md:42`; `SKILL.md:522,534,536,713-715`; `corpus/lessons/README.md:97,207`;
  `corpus/lessons/round-31.md:46`; `corpus/lessons/round-32.md:33,41`
- commands (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `git hash-object corpus/lessons/README.md`; `git rev-parse HEAD:corpus/lessons/README.md`;
  `git rev-parse HEAD:SKILL.md`; `git log --oneline -4 -- SKILL.md`;
  `sha256sum SKILL.md corpus/lessons/README.md AGENTS.md corpus/lessons/round-6-sources/{05,03,13,09}.json`;
  `wc -l SKILL.md corpus/lessons/README.md AGENTS.md`;
  `grep -rc 'lessons/README\|SKILL.md' tools/gates/frozen/*/MANIFEST.tsv tools/gates/frozen/*/*/MANIFEST.tsv`;
  python enumeration of every `expected.json` `inputs` map (20 baselines / 45 keys / 0 hits);
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 1, 2 findings);
  `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` (exit 1, X45-P1);
  `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` (34/37);
  `python3 reports/round-25/run-validation.py --check` (exit 2, could-not-evaluate);
  `python3 reports/round-30/run-validation.py --check` (claim D red, box-1 binding);
  `grep -c 79fe91d3|83b0a78a reports/round-30/craft/review-D29-box1.md`;
  `grep -rn x57 reports/round-2[6-9]/run-validation.py reports/round-3[0-2]/run-validation.py` (0)
