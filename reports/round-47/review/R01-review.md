# R01 — non-author review of round 47: C is a real gap with a defective assembly, O has a method and no instrument, Ca is complete but carries one false sentence

- Seat: `R01` | role: reviewer (non-author) | claim: **cross** | round 47, loop 2, position 1 (refire wave)
- Out path: `reports/round-47/review/R01-review.md` (the only repo path this seat writes)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`), equal to `reports/round-47/claims.json:7`
- Review cut: **2026-10-19T19:18Z** (UTC); first census at 19:13Z. R03, R04, O07, O14, V02, W01 and X03 landed during this review (19:14–19:17Z); their findings are folded into §2.5, §3.3 and §3.5. The round was still filing at close; verdicts are bound to the bytes named in §8 and to no later revision.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Boundary: I read filed bytes and seat artifacts; I ran read-only probes, two harness selftests, and one scratch assembly of the O drafts under `.scratch/r01/`. I did not edit a filed byte, did not stage under `corpus/`, did not run any `reports/round-*/run-validation.py`, and made no git/network/install call. `git status --porcelain` at the cut shows only `?? reports/round-46/review/` and `?? reports/round-47/`; `git diff` and `git diff --cached` are empty.

## 0. Verdict summary

| claim / axis | verdict at this cut | basis |
|---|---|---|
| **C — coverage** | **premise GREEN; `after_required` NOT MET; no axis harm; not `improved`** | 223 entries / culture-material 25 / target absent / 0 owners (my commands, §2.1). No entry has landed. The assembly is **790 fenced lines (51 head + 739 body)** against a partition maximum of 221; R03 files **B1–B9 blocking** content/assembly defects and C14 files a blocking worked-example FAIL. The audit chain is pinned to superseded bytes and cannot be called "audits PASS". |
| **O — operability** | **`could-not-evaluate` on the deliverable; method `unprovable-but-better`; no axis harm; not `improved`** | `tools/harness/claims-freshness.py` is absent at the baseline commit and at HEAD. The O01–O03 drafts **do not concatenate** as O01 claims: a `from __future__` import at assembled line 694 is a `SyntaxError`; after that is repaired, O02's `__main__` guard exits 0 after its registry selftest, so `--claims` evaluates nothing. No CLI exists. R04 independently measures the same false green plus a status-vocabulary break at the O02→O03 seam and malformed O05/O06 fixtures. W01 now pins a corrective four-strip assembly (104,538 bytes, `6cbfdef1…`) with a green scratch run, and V02 reproduces the verdicts — but the durable path is still absent and no `calib/` demo is filed. |
| **Ca — calibration** | **`PASS-with-required-correction`; record `improved` only after the correction and filing** | Ca06 covers the loop-1 carried list 5/5 plus the r46 MANIFEST item as 3 defect rows + 2 named deviations, parent pinned `dfc9265d…` and byte-unchanged, zero `fixed` rows. But Ca04:195 and Ca06:371 carry a demonstrably false verification sentence about zai; filing it as-is would reproduce the class of defect the queue exists to prevent. |
| **cross — axis harm** | **none observed on disk** | corpus 223 / culture-material 25, target absent; `git diff` empty; parent queue digest unchanged; no corpus/tool/README staging; all writes under `reports/round-47/` except the pre-existing r46 review anomaly. |

**One-line judgment:** the round has a real coverage candidate, a real calibration successor, and a proven-but-undelivered operability method. Only Ca is complete enough to carry an axis move, and only after one correction; C and O must be recorded as `could-not-evaluate`, not as partial passes.

---

## 1. What I measured myself

All commands from the lane root, 2026-10-19, with the round's environment variables.

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ git diff --stat
(empty)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223
missing_from_index 0 []  topic_mismatch 0 []  orphan_rows 0 []  header_drift {}
totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
exit=0
$ sha256sum corpus/README.md reports/round-40/op/defect-queue-v2.json
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
$ ls reports/round-47/run-validation.py
ls: cannot access 'reports/round-47/run-validation.py': No such file or directory
```

The README rev-2.4 defect reproduces exactly as C09/C10 describe: `corpus/README.md:10-11` declares `25/23/25/29/24/94 → 25/23/26/25/24/94`, which sums **220 → 217**, while the live footer (`corpus/README.md:548`) is `25/26/25/29/24/94` = **223**. The corrected post-landing vectors are rev-2.4 = `25/26/25/29/24/94` (223) and rev-2.5 = `25/26/26/29/24/94` (224). I verified the arithmetic with `python3`: 217 / 223 / 224.

At my first census `reports/round-47/` held **55 files**: 51 declared seat artifacts (A03 landed at its 19:08:57Z cut), `claims.json`, `targets.json`, and two telemetry notes. R03 and R04 landed at 19:14–19:15Z, so the pre-this-file count is **57**; with this review it is 58. The wave continued after the cut: O07, O14, V02, W01 and X03 landed at 19:16–19:17Z. At the final check the round holds **63 files / 59 seat artifacts**; O08, O11, O15, Q01 and W02 remain absent. The durable tool is still absent.

---

## 2. Claim C — coverage

### 2.1 The premise is true at the baseline

```
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo present || echo absent
absent
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
$ grep -rn 'cartograph' corpus/knowledge
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102: ... T-O diagrams are symbolic devices, not cartographic claims.
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58: | Lienzos and cartographic histories ...
# 2 lines / 2 files
```

The slug is free, the sort slot is between `calendar-festival-systems.md` and `costume-semiotics.md`, and the landing is an **A** (add), not an **M**. The only prior-round naming is the r44 K02 seed; there is no prior-round draft or landing. The claim's phrase "0 prior-round proposals" (`claims.json:26`) is literally false at r47 because r44 K02 **is** a prior-round proposal. The correct scoped sentence — used by K01, C05 and X00 — is: **0 proposals before r44 K02; r44 K02 is the cited seed and was never drafted or landed.** This is a recording defect, not a landing blocker, but it must not be repeated unqualified in LOG/SHONEN.

### 2.2 The deliverable is absent; the draft is the only object

No entry has been applied. I measured the fenced entry bodies:

| fragment | entry-body lines |
|---|---:|
| C04 head block (`cov/C04-entry-header.md:111-163`) | 51 |
| C01 §§1–4 (`cov/C01-entry-a.md:85-287`) | 201 |
| C02 §§5–9 (`cov/C02-entry-b.md:40-402`) | 361 |
| C03 §§10–15 (`cov/C03-entry-c.md:72-250`) | 177 |
| **assembled** | **790 (51 head + 739 body; 601 non-blank)** |

R03's independent extraction reports **739 body lines / 17,601 words / 240 table rows**, which reconciles exactly with the 51-line head excluded; both measurements are far outside the band. The live culture-material partition is min 103 / median 149 / **max 221** lines (`wc -l corpus/knowledge/culture-material/*.md`). The draft is **3.6× the longest existing entry and 5.3× the median**. C07's own executable band is 100–260 (`cov/C07-contract-audit.md` §7), and C11 ran C07's checker on the then-assembly and got exactly one FAIL: `length in partition band: 854 lines` (`cov/C11-scribe.md:67-78`). C02 has since been trimmed from 424 to 361 body lines, which reduces the assembly from 854 to 790 but does not bring it into band. The count would move to 224 while the craft contract regresses: that is the trade this review exists to block.

### 2.3 Factual defects that survive in the current bytes

These are not inherited from earlier revisions; I read them in the files as they stand now. R03 independently files B1–B9; I confirm the ones below at the cited lines.

**C-R01-1 — the `- gap filled:` line contains an unreproducible count.** `cov/C04-entry-header.md:115` says `grep -rli 'cartograph' …` → **"2 files / 3 lines"**, attributing the lines to `cosmology-cosmography.md:71,:102` and `mesoamerica-primary-sources.md:58`. Measured: **2 lines in 2 files** (`cosmology:102`, `mesoamerica:58`). `:71` contains "Mappa Mundi" / "survey maps", not the token `cartograph`; and `grep -rli` lists files, not lines, so the cited command cannot produce "3 lines". This is the same failure class as R01-43-12 one level down: an evidence sentence its own command does not produce. R02 C-D3, R03 B2, X04 F-11/F-12 and C11 §5 D3 all flag it; it is still unfixed.

**C-R01-2 — the head block miscounts its own pins.** `C04:117` says "sha256 pinned for the six load-bearing anchors" while **nine** files are pinned. R03 P2-2; C06 §10 correction 2; still unfixed.

**C-R01-3 — the boundary table omits the strongest competing definition.** `cov/C01-entry-a.md:92-101` disposes eight neighbours and cites `cosmology-cosmography.md:71,:102` (the disclaimers), but never cites `:27`: "**Cosmography** = the projected, inhabited version: how the world is drawn (**maps**), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)." The one-owner claim is defensible — cosmography owns the world-model/world-diagram, this entry owns the surveyed, projected, reproduced sheet — but the table must say so at `:27`. R02 C-D2, R03 B8 and X04 §3 agree. I verified `grep -n ':27' cov/C01-entry-a.md` returns no hit.

**C-R01-4 — four boundary rows are missing and one anchor is wrong.** The table has no rows for `craft-artisan-lexicon`, `trade-economy-lexicon`, `celestial-symbolism-calendars`, or `sacred-kingship-mythic-charter`, although the body develops the mapmaker trade, the legal instrument, the star-chart form, and the legal-vs-mythic charter. Worse, `cov/C02-entry-b.md:248` anchors the apprentice→journeyman→master ladder at `craft-artisan-lexicon.md:44`; I read line 44: it is the **steel-grading row** (tamahagane/kawagane/shingane). The guild ladder is at `:54-65` (`:56-63` the systems). C02's own audit table at `:421` certifies the wrong anchor as "workshop ladder table … real". R03 B4, C08 P1-2 and R02 C-D4 reproduce this.

**C-R01-5 — the worked example has a blocking internal inconsistency.** `cov/C14-example.md:11` says **FAIL as filed**, F-1 blocking: the update rule is stated three incompatible ways at `C03:123` ("re-survey after any storm that breaches a dike"), `C03:137` ("the re-survey is not due until the levy year turns"; the joint survey needs "a new update rule (re-survey after every breach, not every levy year)"), and `C03:150` ("after a dike breach, per levy year"). I read all three lines and agree: the example's causality depends on the levy sheet **not** having been re-surveyed, so a breach-triggered rule at `:123` makes the office violate its own rule without saying so. F-2 is also real: zero `DR-CT-` ids in §11 and no consequence↔rule map. R03 B7. C03 is unchanged (`4b699e06…`), so this FAIL stands.

**C-R01-6 — C05's post-landing vector is slot-swapped and must not be propagated.** `cov/C05-freshness.md:273`, `:275` and `:295` predict `26/26/25/29/24/94`; slot 3 is culture-material, so the correct vector is `25/26/26/29/24/94`. C10 §5a demonstrated that C05's vector fails the sweep's `FOOTER_DIR_TOTALS` check. C09/C10/V01 use the correct vector; the integrator must use theirs.

**C-R01-7 — do NOT apply C02's "archive of coups" correction.** `cov/C02-entry-b.md:36` and `:501` accuse C01 of quoting a phrase "not in the file" and propose "a map is an archive of renamings". The accusation is **false**. I read the full live line: `corpus/knowledge/linguistics/naming-systems.md:70` ends "Every renaming is datable; **a map is an archive of coups**." C01:90 and C01:344 quote it correctly. C03:219's "renamings" is the paraphrase, not the source. If the integrator follows C02's owed item, it will replace a correct quotation with an invented phrase. R03 B3 reaches the same conclusion; this is the one place where a sibling's "correction" would corrupt the entry.

**C-R01-8 — three more cross-reference/coverage defects (R03 B1/B5/B6/B9).**
- `C02:98`: "0.2 mm on a 1:50,000 sheet claims about 10 m of ground; if the survey closed at 200 m, the drawing asserts **ten times** the available precision." The ratio is **20×** (200 m / 10 m). Fix the number or the wording.
- `C03:79` says "the typology in **§1–3**" and `C03:184` says "the typology in **§2**". The form typology is C01 **§4.1**; §2 is the five-condition register test. C06's correction list quotes line 79 as "§2", which does not match the live string ("§1–3").
- `C01:298` says "Provenance/charter (**§9**)"; the binding map puts provenance/charter at **§8** and the container-name fossil at §9.
- `C03:95-103`'s "minimum credible build **per form**" covers only **5 of the 8** forms in C01 §4.1; the celestial/star chart, thematic, and cartographic-history/lienzo rows are missing.

### 2.4 The audit chain is not "PASS on delivered bytes"

`claims.json:28` requires "audits PASS". At this cut:

| audit | current status | why it is not a pass on delivered bytes |
|---|---|---|
| C05 freshness | PASS on ownership; vector wrong | `:273,:275,:295` |
| C06 source audit | PASS-with-3-corrections on a **superseded assembly** | its assembly sha `2422ca96…`, 855 lines, used C02 before the 424→361 trim; the `cartograph` correction is still unfixed in C04 |
| C07 contract | **pre-bytes** `could-not-evaluate` | audited 17:55Z with no draft; its own checker FAILs length (C11 §2.1) |
| C08 boundary | PASS-with-P1 on **stale pins** | pins C01 `a02031a4…`, C02 `85085d24…`; current are `cfb42955…`, `5f5683a7…` |
| C12 shelf | PASS-with-advisories on **stale C02** | pins C02 `bfce3ac…`; current `5f5683a7…` |
| C10 sweep | PASS on a staged fixture | mechanics only; does not read revision prose |
| C13 couples | PASS on the field | line pin `cf59ba1f…` still matches C04; re-run after assembly |
| C14 example | **FAIL** | F-1 blocking, F-2 required |
| R03 content | **PASS on substance, B1–B9 blocking** | real method, not landing-ready |
| V01 post-landing | staged only | live verdict `could-not-evaluate` |

C02 changed **after** R02's cut as well (`bfce3ac…` → `5f5683a7…`), so even the peer review's C06/C12 citations are one revision behind. This is not a reason to distrust the *findings* — I reproduced the load-bearing ones directly — but it is a reason the integrator cannot record "audits PASS" without re-running C06/C07/C08/C12/C13/C14 on the final assembly.

### 2.5 C verdict

**Premise green; after-state `could-not-evaluate`; no axis harm.** The topic is real — the 223 entries own space as cosmology, sacred route, orientation and built plan, and none owns the survey→projection→reproduction chain. The drafts are real method, not filler: C01's five-condition register test, C02's seven-link chain and word bank, C03's build order and calibration bank. R03's depth judgment ("one of the stronger recent drafts in the partition") is consistent with my read. But 790 lines against a 221-line maximum, a false count in its own gap statement, an undisposed `cosmology:27`, a wrong craft anchor, a blocking worked-example FAIL, and a false "correction" that would corrupt a correct quote are not a landing. **Do not record coverage as improved.**

---

## 3. Claim O — operability

### 3.1 The premise is true at the baseline

```
$ git cat-file -e 6e9a30d:tools/harness/claims-freshness.py; echo rc=$?
fatal: path 'tools/harness/claims-freshness.py' does not exist in '6e9a30d'
rc=128
$ git ls-tree -r --name-only 6e9a30d -- tools/harness | grep -i 'fresh\|claim'
(no output)
```

The durable gate does not exist at the declared baseline. The r43 stale premises are also real, and I reproduced the load-bearing facts from committed bytes:

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
... PASS N6 regression guard: block read yields 4 tokens ['sound-change.md','sound-symbolism.md','tone-prosody.md','writing-systems.md']
SELFTEST OK: 8/8   (exit 0)
$ git ls-tree 7ceff59 -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
100644 blob f38f87e8…  corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -
$ git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json; echo rc=$?
fatal: path ... does not exist in '7ceff59'
rc=128
```

So r43 O is stale (a tracked resolver exists and reads the wrapped field 4/4), r43 C is stale on ownership (the lithic entry exists at `7ceff59` and owns the register at `:5`), and r43 Ca is fresh (the disposition artifact is absent). That is the required asymmetry.

For the negative control I verified the baseline discriminator myself:

```
$ git cat-file -e c9f4eaa:tools/harness/basename-couples-resolver.py; echo rc=$?
fatal: path ... does not exist in 'c9f4eaa'
rc=128
$ git cat-file -e 6e9a30d:tools/harness/basename-couples-resolver.py; echo rc=$?
0
$ git grep -n 'four_class_totals' c9f4eaa -- tools/
(no output)
$ git grep -n 'four_class_totals' 6e9a30d -- tools/
6e9a30d:tools/harness/basename-couples-resolver.py:260:        "four_class_totals": four,
```

r44 O's `before` ("no four-class authority") was **true** at its own baseline. The r47 O claim's parenthesis "r43 and r44 both declared claims on stale premises" (`claims.json:40`) is therefore false for r44 O; the accurate record is "r43 O/C stale; r44 C carried-candidate; r44 Ca undelivered". R02 §3.3, X00 §7.2, Ca01 §3 and O12 §1 say the same. This must not be repeated in LOG/SHONEN.

### 3.2 The deliverable is absent

```
$ ls tools/harness/claims-freshness.py
No such file or directory (exit 2)
$ ls reports/round-47/calib/
Ca01-stale-premises.md  Ca02-resolver-edge.md  Ca03-manifest-schemas.md
Ca04-provider-amendments.md  Ca05-verify.md  Ca06-queue-successor.md  Ca07-integrity.md
```

There is no `claims-freshness-demo.json`, no r43 annotated fixture under `calib/`, and no negative-control fixture under `calib/`. O05 and O06 are **drafts for the integrator**; their runs use a seat-local reference evaluator. O12 states this in its own bottom line (`op/O12-scribe.md:12-30`), and O10/O13 label every prototype row as prototype, not durable. That honesty is correct — but it means the O `after_required` is unmet.

### 3.3 The O drafts do not compose as claimed

O01 asserts: "The assembly is plain concatenation; nothing in part 2/3 needs to edit these bytes" (`op/O01-tool-core.md:23`). I tested that in `.scratch/r01/` by lifting the three large fenced blocks (O01:160-794, O02:254-1222, O03:86-574) and concatenating them.

**Failure 1 — `from __future__` after code.** O02's block begins with `from __future__ import annotations` (`op/O02-probe-registry.md:315`), which lands at assembled line 694:

```
SyntaxError: from __future__ imports must occur at the beginning of the file
```

**Failure 2 — O02's `__main__` guard exits before O03.** O02 ends with `if __name__ == "__main__": sys.exit(selftest_registry())` (`:1220-1221`). After stripping the duplicate future imports and shebangs, the assembled file compiles, and:

```
PROBE-REGISTRY SELFTEST: 43/43     (exit 0)
```

But `--claims reports/round-43/claims.json` prints the same 43/43 selftest and **exits 0 without a verdict**: the first `__main__` block wins. O03 has no `argparse`, no `def main`, and no `ArgumentParser` (`grep -c argparse op/O03-verdict-contract.md` → 0), so the assembled body has no CLI at all. O03's own evidence is a scratch driver (`op/O03-verdict-contract.md` §7, selftest 33/33), not the assembled tool.

R04 independently reached the same result with more seam detail: the O02→O03 status vocabulary does not match (`O02` emits `mismatch`; `O03` accepts `CONTRADICTED`, so the raw seam downgrades a contradiction to could-not-evaluate/exit 3, `review/R04-gate.md:111-123`); O05's r43 overlay is **5 of 6 checks rejected** by O02's validator and O06's control is **9 of 9 rejected** because three check dialects are in play (`R04:125-142`); O04's 46-control suite is not a drop-in (missing `CAPABILITIES`, `SchemaError`, `FixtureBaseline`, `evaluate_claim`, `R04:144-157`). R04 also measured a capability-probe false-negative edge: a candidate that crashes is read as "no capability", which for an absence claim would hold — a present capability could be laundered as absent (`R04:78`). With a native check set and a 3-line status map the parts **can** produce O STALE / C STALE / Ca FRESH / exit 1 (`R04:159-170`) — capability, not delivery.

**W01 has since supplied the missing assembly recipe.** `op/W01-landing-spec.md` pins a four-strip build (not plain concatenation) at **104,538 bytes, sha256 `6cbfdef1f27dbea80450ebd905700dbc13f1a8f233c72d69c512b74d196461d4`**, and reports a scratch run with `registry 43/43 + seam 18/18`, the r43 demo O/C stale + Ca fresh exit 1, the O06 negative control 9/9 exit 0, the O10 suite 14/14, an unchanged anti-theater verdict, and two byte-identical runs. V02 independently reconstructed the same body and reached the same verdicts through a verifier adapter (`op/V02-gate-verify.md:16-30`). This is a real advance: the composition defect is now understood and specified, and the remaining work is mechanical — apply W01's pinned bytes and file the two `calib/` fixtures plus the demo. But none of it is the durable path: `tools/harness/claims-freshness.py` is still absent, so the O claim remains `could-not-evaluate` at this cut.

### 3.4 The demos prove the method, not the tool

I accept the following as measured by their authors and consistent with my baseline probes:

- O05: r43 O STALE, C STALE, Ca FRESH; reference exit 1; every failing clause names a measured capability or owner.
- O06: r44 control 3/3 fresh, 9/9 clauses, exit 0 at `c9f4eaa`; the same fixture turns O stale at HEAD — the baseline-vs-worktree discriminator.
- O09: the prototype fails all three trap families; the contract requires novel-phrasing → could-not-evaluate, unknown kind/missing polarity → exit 2, tag resolving to a commit → resolved sha.
- O10: the prototype's exit codes are inverted (stale→2, malformed→1, C-N-E→0 under `--allow-unverifiable`); the compliant contract is 0/1/2/3.
- O13: 6 of 13 prototype probe kinds have no control; two contract kinds are missing under their names; unknown kinds are downgraded to STALE instead of MALFORMED.

The method is credible. The claim's thresholds are not.

### 3.5 O verdict

**`could-not-evaluate` on the deliverable; `unprovable-but-better` for the method; no axis harm.** The defect is confirmed, the r43 asymmetry and r44 negative control are measured, the trap matrix is acceptance-ready, and W01/V02 have now reduced the remaining work to an apply: W01 pins the exact bytes and a green scratch run; V02 independently reproduces the verdicts. But `tools/harness/claims-freshness.py` is still absent, no `calib/` demonstration or fixture is filed, the raw O01–O03 concatenation is a false green, and the seam vocabulary and fixture dialects still need the documented repairs. R04's independent judgment is identical: "operability is not improved by this round at this cut" (`review/R04-gate.md:25`); V02 says the durable path "does not exist. That is `could-not-evaluate`, not green" (`op/V02-gate-verify.md:12`); X03 says "the method is not theater. The deliverable is" (`cross/X03-gate-theater.md:12`). **Do not record operability as improved.**

---

## 4. Claim Ca — calibration

### 4.1 The premise is true and the parent is intact

At `6e9a30d` there is no successor for the loop-1 carried list, and the parent queue contains none of the relevant rows: `reports/round-40/op/defect-queue-v2.json` has 38 rows; a search for `r43-stale-premises`, `resolver-hyphen`, `manifest-ledger` or `zai-exhaustion` finds none. The r43 successor (`reports/round-43/calib/defect-queue-v2-successor-r43.json`) has 4 unrelated rows (`r39-review-findings-disposition`, `r38-O02-fragment-defects`, `r38-O08-fragment-defect`, `r38-O07-empty-fragment`). So the claim's `before` — five carried items not yet dispositioned — is true.

The parent is byte-unchanged:

```
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
$ git status --porcelain -- reports/round-40/op/defect-queue-v2.json
(empty)
$ python3 -c "import json; d=json.load(open('reports/round-40/op/defect-queue-v2.json')); print(len(d['rows']))"
38
```

### 4.2 Coverage of the loop-1 carried list

`reports/round-46/loop-1-retrospective.md:43-53` names five bullets. Ca06 maps them 5/5, with the first two folded into one row by design (both are the R01-43-12 class) and the r46 audit's MANIFEST schema note as the sixth item:

| retrospective item | Ca disposition | class |
|---|---|---|
| freshness gate absent (`:45-46`) | `r43-stale-premises` | `routed-with-owner` |
| stale-premises pattern (`:47-48`) | same row (narrow incidence r43 O+C) | `routed-with-owner` |
| resolver latent edge (`:49-50`) | `r44-resolver-hyphen-after-blank` | `recorded` |
| antigravity outage (`:51-52`) | `PA-47-01` | `named-deviation`, `defect_row:false` |
| zai exhaustion (`:53`) | `PA-47-02` | `named-deviation`, `defect_row:false` |
| r46 MANIFEST schemas | `manifest-ledger-two-schema-evolution` | `recorded` |

The two provider rows are outside `rows[]` and outside the defect count, following the parent's own "telemetry deviations NOT defect rows" practice (`defect-queue-v2.json:8`). That is the correct classing: no rule breach is alleged, and the requested/observed split is preserved. Ca07 §3 confirms the rows are field-for-field identical to Ca01–Ca04, the parent pin is unchanged, and zero `fixed-with-evidence` rows exist (`calib/Ca07-integrity.md:10-30`). R05 §1 independently re-measured the stale premises, the resolver edge, the MANIFEST schemas and the provider amendments and reached the same class verdicts.

### 4.3 Required correction: a false verification sentence

**Ca-R01-1.** `calib/Ca04-provider-amendments.md:195` and its copy at `calib/Ca06-queue-successor.md:371` say:

> "no dispatch-declared.json at r44, r46 or r47 names zai (lanes: opencode-go, devin, opencode-go)"

The literal sentence is false. `reports/round-46/telemetry/dispatch-declared.json:16` says "zai usage exhausted", and `reports/round-47/telemetry/dispatch-declared.json:18` says "Standing amendments: zai->luna-max all session". The intended true statement is "none of those rounds dispatched **on** zai; the amendment appears only in the notes." This is the same defect class the queue exists to prevent — a verification sentence not re-measured against the bytes it cites. R05 (F-R05-1), Ca05 (F6) and Ca07 (F-Ca07-3) independently flag it. **Fix both copies before the successor is filed.**

**Ca-R01-2 (minor, provenance).** Ca06 pins Ca05 at `747c0fdb…` (`calib/Ca06-queue-successor.md:113`), R05 reviewed `26430501…`, and the current Ca05 is `5dfe7b12…` (revised at 19:09Z). The successor must cite the final verifier digest at filing, or record the drift explicitly. Ca07's F-Ca07-2 reaches the same point.

**Ca-R01-3 (minor, citation reproducibility).** Ca03 and Ca06 cite `MANIFEST.json`, `PROTOCOL.md` and `PROTOCOL-APPENDIX.md` as bare paths; they are fleet-root files, not lane files (`ls PROTOCOL.md` → ENOENT). Prefix the fleet root or add one root note. R05 F-R05-3 / Ca05 N2.

### 4.4 Ca verdict

**`PASS-with-required-correction`; record `improved` only after 4.3 is fixed and the successor is filed.** The substance of the claim is met: every carried item reaches a class with an owner and cited evidence, zero are silently dropped, the freshness row is routed to the O tool rather than prematurely marked fixed, the provider amendments are named deviations, and the parent is pinned and unchanged. If filed as-is with the false zai sentence, the calibration axis would move in the wrong direction.

---

## 5. Cross-claim dependencies and axis-harm ledger

| risk | claim | status at this cut | tripwire |
|---|---|---|---|
| C lands a carried/duplicate topic | C | **No.** 0 owners; only r44 K02 seed; no draft/landing before r47. | Scoped wording for "0 prior-round proposals"; re-run ownership at apply HEAD. |
| C creates a second owner via `cosmology:27` | C | **Open.** The table disposes `:71/:102` but not `:27` ("how the world is drawn (maps)"). | Add the content-vs-production sentence/row. |
| C volume-inflates the partition | C | **Open.** 790 lines vs 103–221 (max 221). | Deduplicate to ≤~340 or file an explicit ruling. |
| C lands a false count in its own gap statement | C | **Open.** "2 files / 3 lines" vs measured 2/2. | Fix C04:115 before apply. |
| C applies C02's false quote "correction" | C | **Open risk.** C02:36/501 would replace a correct quote with an invented phrase. | Drop C02's B3 item; keep C01's exact quote. |
| C README arithmetic wrong | C | **No.** C09's diff is correct; C10 staged green. **But C05's `26/26/25/29/24/94` is wrong.** | Use `25/26/26/29/24/94`; do not copy C05. |
| C "audits PASS" on superseded bytes | C | **Open.** C06/C12/C08 pins are stale; C07 is pre-bytes; C14 FAILs. | Re-run on the final assembly. |
| O gate is theater | O | **Not demonstrated against a durable tool; the drafts are not composable and O02's guard exits; the seam downgrades STALE to CNE.** | Require the assembled tool and O08/V02. |
| O overclaims r44 | O | **Open in the claim text.** r44 O's `before` was true at `c9f4eaa`; r44 C was carried, not owned. | Fix LOG/SHONEN wording. |
| O durable tool absent | O | **Open.** No tool, no CLI, no `calib/` demo, no anti-theater artifact. | Land and verify. |
| Ca edits filed bytes | Ca | **No.** `git diff` empty; parent digest unchanged; no corpus writes. | Ca07 + close gate. |
| Ca files a false verification sentence | Ca | **Open.** Ca04:195 / Ca06:371. | Correct before filing. |
| Write-surface bleed | cross | **No.** All r47 writes under `reports/round-47/`; the only outside path is the pre-existing r46 review, classified by A03 §5.1. | A03 close census. |

**Dependency:** Ca's `r43-stale-premises` row cannot flip to `fixed-with-evidence` in this round. The O tool is absent, so the row stays `routed-with-owner`; its reclass gates G1–G8 (Ca06 §6.5) require a durable path, a green selftest, the r43 asymmetry, the negative control, the anti-theater mutation, the exit contract and a filed demonstration. If O does not land, Ca still stands as a routed row — that is the correct, honest outcome.

---

## 6. What must happen before admission

Ordered, fail-closed.

### C

1. **Drop C02's false correction** (`C02:36`, `C02:501`): `naming-systems.md:70` really does say "a map is an archive of coups". Keep C01's exact quote; either change C03:219 to the exact phrase or mark it as a paraphrase. Do not let this item reach the integrator as an owed fix.
2. Fix `C04:115` to `cartograph` = **2 lines / 2 files**, naming the exact probe; remove `:71` from the hit list.
3. Fix `C04:117` "six" → "nine" load-bearing anchors.
4. Add the `cosmology-cosmography.md:27` disposition (content vs production) to C01 §1.1; add the missing boundary rows (craft, trade, celestial, sacred-kingship) and fix the craft-ladder anchor to `:54-65` (keep `:44` for material grading only).
5. Fix the cross-references: `C03:79` "§1–3" → "§4.1"; `C03:184` "§2" → "§4.1"; `C01:298` "§9" → "§8". Fix `C02:98`'s 200 m / "ten times" arithmetic (20×, or 100 m).
6. Complete or retitle `C03:95-103` ("5 of 8 forms").
7. Repair C03 §11's update rule (C14 option A) and add the `DR-CT-` ids + consequence↔rule map (F-2).
8. Deduplicate C01 §3 against C02 §5.4–5.6 and trim the assembly to the partition band (≤~340 lines, preferably ≤260 per C07's checker). If a longer reference entry is intended, file an explicit ruling — do not let concatenation decide.
9. Re-run C06/C07/C08/C12/C13/C14 on the **final assembled bytes**; C07's `could-not-evaluate` is not a pass, and C08's/C12's pins must match.
10. Use `25/26/26/29/24/94` everywhere; never C05's `26/26/25/29/24/94`. Regenerate the README row from the landed `- topic:`.
11. Record the scoped gap wording: "0 proposals before r44 K02; r44 K02 is the cited seed, never drafted or landed."

### O

1. Apply `tools/harness/claims-freshness.py` from **W01's pinned four-strip assembly** (`op/W01-landing-spec.md:9-24`: 104,538 bytes, sha256 `6cbfdef1f27dbea80450ebd905700dbc13f1a8f233c72d69c512b74d196461d4`), not plain concatenation. W01 reports `registry 43/43 + seam 18/18`, the r43 demo O/C stale + Ca fresh exit 1, the O06 control 9/9 exit 0, the O10 suite 14/14, and deterministic reruns. If the assembled bytes do not match the pin, stop.
2. Confirm the status map `holds→HOLDS`, `mismatch→CONTRADICTED`, `could-not-evaluate→NOT_EVALUATED` is in the applied seam (R04 D3; W01's seam fence claims it).
3. Confirm one check schema is in force: either K03/O05's overlay (`claims_sha256`, baseline equality, unknown ids malformed) or O02's native typed checks; the O05/O06 fixtures must be rewritten to it. As filed, O05 is 5/6 rejected and O06 9/9 rejected by O02's validator (R04 D4).
4. `--selftest` green with a control count computed from the registry; all eight contract probe kinds (the r47 claim names seven; `grep_present` is the eighth) controlled; unknown kinds → MALFORMED/exit 2. Distinguish "candidate ran and failed" from "no candidate" for absence claims (R04 D6).
5. Run the r43 annotated demo from the durable path: O STALE, C STALE, Ca FRESH, exit 1. Run the r44 negative control: FRESH, exit 0; at HEAD the same fixture must turn O stale. Run the anti-theater mutation: still STALE. Run the could-not-evaluate and malformed vectors: exit 3 and exit 2, never 0.
6. File `reports/round-47/calib/claims-freshness-demo.json` with the tool sha256, baseline, per-run verdicts/exits and fixture digests; file the annotated r43 and negative-control fixtures.
7. Fill O08/O11/O15 (O07/O14/V02/W01 have landed) and re-run the §7 acceptance matrix (O12 §7) from the durable path.
8. Fix the r44 overstatement in LOG/SHONEN before it is recorded.

### Ca

1. Correct the zai sentence in both Ca04 and Ca06 (scope it to `provider_lane`/`model`).
2. Re-pin Ca05 to the final digest or record the drift; add the fleet-root prefix to the MANIFEST/PROTOCOL citations.
3. Apply Ca06's fenced JSON as `queue-successor-r47.json` (or record that the `.md` is the successor), run Ca07's integrity check, and file a **new** closing row only if O lands — never edit Ca06 or the parent.

---

## 7. could-not-evaluate / to-verify at this cut

- **O durable tool** — absent; the entire O `after_required` is unproven. Owner: integrator + O01–O04.
- **O verifier set** — at the final check, **O08, O11, O15, Q01 and W02** remain absent (63 files / 59 seat artifacts). O07, O14, V02, W01 and X03 landed at 19:16–19:17Z and are cited in §3.3/§3.5; their verdicts converge on method PASS / durable artifact ABSENT. The composition failure is now owned by W01's landing spec, but the durable path is still unverified by O08/V02 against an applied file.
- **C06/C07/C08/C12/C13/C14 on final bytes** — C06's assembly is superseded; C07 is pre-bytes; C08/C12 pins are stale; C13 is field-level and must be re-run after assembly; C14 is a FAIL.
- **`reports/round-47/run-validation.py` / `validation.json`** — absent. `claims.json:45,56` cite the runner as a counting command; it is not runnable at this cut. The absolute rule forbids in-tree execution, so the integrator must author and run it in isolation.
- **Telemetry close** — `observed-dispatch.json` and `availability-close-47.json` are absent; `refire-key6.json` is a dispatch note with a date-only `recorded_at_utc`, no counting command and no observed counts. Unknown counters stay `null`, not zero. A03 §7 / S02 §3–§6 supply the skeletons.
- **`reports/round-46/review/R01-review.md`** — untracked, mtime 17:48:54Z, an r46-declared artifact filed during r47. It is not an r47 seat path; A03 §5.1 classifies it. Do not count it toward r47.
- **C04 self-audit length** — it reports "seed_len 758 / mine_len 758"; measured line length 775 (content 766). Byte-equality is true; the length number is stale.
- **C02's current revision** — it changed after R02/C06/C12 (`bfce3ac…`/`85085d24…` → `5f5683a7…`). The trim is an improvement; the audits must be re-read against the final bytes.
- **The `.pyc` side-effect** — A03 §5.2 records a gitignored `tools/harness/__pycache__/basename-couples-resolver.cpython-314.pyc` (mtime 17:58:36Z), evidence that at least one invocation skipped `PYTHONDONTWRITEBYTECODE=1`. Content-neutral; the invoking seat is `to-verify`.

---

## 8. Evidence appendix

### 8.1 Digests of the bytes reviewed

```
cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d  cov/C01-entry-a.md
5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af  cov/C02-entry-b.md
4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5  cov/C03-entry-c.md
cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0  cov/C04-entry-header.md
62f9f702540f6b363d1c410ee8a58aa19619aa6b09b1c0caeb323ac4dd8ee5e3  cov/C05-freshness.md
f28e19dd44777f7b698ce02e517a07894d0338c8fcfd0b25779c20a04db946f0  cov/C06-source-audit.md
89d0003c934ae6f36acd409a616b858dea1d87e4aea0932c06b5db7a00c230a3  cov/C07-contract-audit.md
94e35a44ec367f2d93d245ba92b9a2259e62e392382e109c295a6e2d672cc2e0  cov/C08-boundary.md
7bba92cdfd0173183109777b696d88e8b8b0d683087cde9d8ff9f3f91870bc43  cov/C12-shelf.md
8621d68fd2dba9049969aedef1bab3cf483a106aa2f15d1f1aaa77eb78475677  cov/C14-example.md
94b99878a31ae6aa8c376fa35af786e36d07f3210c9f368f9a014f4a4ac2136e  calib/Ca04-provider-amendments.md
5dfe7b12c0f4adbdac16e26942dfbe54fb37582ce17cbbefe44039d279e9207f  calib/Ca05-verify.md
15bb86dfff09ff97cbf8e757bbf139e1cb7bc59f42c66475d19a5a1b02db5ec6  calib/Ca06-queue-successor.md
895d76f7cc2c80b1ab14b05d21b869630a002f293f8ae6e7412fbe77b114eb3b  calib/Ca07-integrity.md
fc041d41b89a337a0f7c759d8059fe30461489f3c609bcbb2f887f2bd75d0f4c  review/R02-review.md
52a1f54fb555ac48b98092eaec534d97ba48400b12ea2638f2fcc2829cec364b  review/R05-reconciliation.md
```

R03 and R04 are cited by section, not hash-pinned here; their own headers pin their bytes (`review/R03-c-content.md:14-21`; `review/R04-gate.md:47-49`). They landed at 19:14–19:15Z, after my first census. V02, W01, O07, O14 and X03 landed at 19:16–19:17Z and are cited by section as well (`op/V02-gate-verify.md`, `op/W01-landing-spec.md`, `op/O07-anti-theater.md`, `op/O14-determinism.md`, `cross/X03-gate-theater.md`); none of them asserts a landed durable tool.

### 8.2 Commands (representative)

```
git rev-parse HEAD; git status --porcelain; git diff --stat
find corpus/knowledge -name '*.md' | wc -l
ls corpus/knowledge/culture-material/*.md | wc -l
python3 -B reports/round-28/readme/sweep.py
grep -rn 'cartograph' corpus/knowledge | wc -l
sed -n '27p;70p;71p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
sed -n '70p' corpus/knowledge/linguistics/naming-systems.md
sed -n '44p;54,65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
git cat-file -e 6e9a30d:tools/harness/claims-freshness.py
git cat-file -e 7ceff59:tools/harness/couples-reference-extractor.py
git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json
git cat-file -e c9f4eaa:tools/harness/basename-couples-resolver.py
git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
python3 -B tools/harness/couples-reference-extractor.py --selftest
python3 -B tools/harness/basename-couples-resolver.py --selftest
python3 -B -m py_compile .scratch/r01/claims-freshness-assembled.py
python3 -B .scratch/r01/claims-freshness-joined.py --selftest
python3 -B .scratch/r01/claims-freshness-joined.py --claims reports/round-43/claims.json
sha256sum reports/round-40/op/defect-queue-v2.json reports/round-47/cov/C0*.md reports/round-47/calib/Ca0*.md
```

The scratch assembly is disposable and is not a deliverable; its only purpose was to test O01's composition claim. The durable path remains `tools/harness/claims-freshness.py`, which does not exist.

Signed: **R01** — non-author reviewer for round 47, claim cross. Every measurement above was re-run by this seat at `6e9a30d`; the digests in §8.1 bind the verdict to the bytes reviewed. No filed byte was edited; nothing was staged under `corpus/`; no `run-validation.py` was executed.
