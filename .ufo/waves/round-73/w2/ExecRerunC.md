# ExecRerunC — wave 2 (falsify) — claim-C measurement rerun

Seat: `ExecRerunC`, leaf, kotodama round 73 / hyaku run 7. Date 2026-10-25.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Claims read first: `reports/round-73/claims.json` (frozen at `af65165cf269db346ef872e16a656eccd7264d01`).
Landed revision graded: `0316b8883b4f8d44b8efd720140e7f52f734a102` (base `8841ad3b896a0227674fa0725b818c999118046f`).
Counter graded: `reports/round-73/accept-c.py`, sha256 `95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416` (identical blob `5c2541389367df6a2a6d67eb282d2a6df5fb333c` at all five revisions `af65165..0316b88` — no counter rule moved after the freeze).
Environment: Python 3.14.8, git 2.56.0. No tool installed. Lane worktree never graded and never mutated; every byte-changing experiment ran in a throwaway clone.

Scratch: `D=/tmp/tmp.1ofjQ5bDBh` (pristine clone at lands), `D2=/tmp/tmp.dMswVBSwqd` (mutant clone), downloads `/tmp/ExecRerunC/`.

---

## 1. Lands run — the assignment's exact command, in a fresh clone

```
D=$(mktemp -d) && git -C "$D" init -q && git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane" \
  && git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
git -C "$D" rev-parse --show-toplevel   ->  /tmp/tmp.1ofjQ5bDBh   (= $D, verified before any commit)
cd "$D/lane" && python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102
```

Full output, exit code 1:

```
# round-73 acceptance counter — claim C (conlang-scholarship assimilation)
# counter sha256 (self): 95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416
# stamped revision: 0316b8883b4f8d44b8efd720140e7f52f734a102
# evaluated revision: 0316b8883b4f8d44b8efd720140e7f52f734a102
# measured revision (lane main): 0316b8883b4f8d44b8efd720140e7f52f734a102
# tree: 9b10fa06a2d3756c8bacfc8fc7b2115921370d97
# base revision: 8841ad3b896a0227674fa0725b818c999118046f
# materialized: git archive of the stamped revision at /tmp/r73-lands-5ecp9hem/lands
# worktree graded: no (leg bytes read only from the materialized tree)
# access date: 2026-10-25
# config source: lands tree: row_set, entries, rejects.refused_staged, rejects.refused_files, rejects.families, rejects.forbidden_ids, ground.fragments
# adopted rows: S876 S877 S878 S879 S880
# entries: corpus/knowledge/linguistics/conlang-scholarship.md ; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md

LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG FAIL CENSUS
     census script not found: /tmp/tmp.1ofjQ5bDBh/scripts/sources-census.sh
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-73: FAIL legs=10/11
```

**The claim's `after` sentence is not reproducible in a clone.** See finding **M5**. With the fleet root supplied it is 11/11:

```
cd "$D/lane" && python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 \
  --fleet-root /home/vgpnk/Projects/shokunin
```

```
# ... identical header, materialized at /tmp/r73-lands-5jas638o/lands ...
LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r73-fleet-9gr_tfn7/kotodama-shokunin/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-73: PASS legs=11/11
exit 0
```

And the claim's own command **in the lane** (read-only; no writes, `git status` unchanged afterwards):

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102
```

```
# round-73 acceptance counter — claim C (conlang-scholarship assimilation)
# counter sha256 (self): 95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416
# stamped revision: 0316b8883b4f8d44b8efd720140e7f52f734a102
# evaluated revision: 0316b8883b4f8d44b8efd720140e7f52f734a102
# measured revision (lane main): 0316b8883b4f8d44b8efd720140e7f52f734a102
# tree: 9b10fa06a2d3756c8bacfc8fc7b2115921370d97
# base revision: 8841ad3b896a0227674fa0725b818c999118046f
# materialized: git archive of the stamped revision at /tmp/r73-lands-1d56pjrq/lands
# worktree graded: no (leg bytes read only from the materialized tree)
# access date: 2026-10-25
# config source: lands tree: row_set, entries, rejects.refused_staged, rejects.refused_files, rejects.families, rejects.forbidden_ids, ground.fragments
# adopted rows: S876 S877 S878 S879 S880
# entries: corpus/knowledge/linguistics/conlang-scholarship.md ; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md

LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r73-fleet-jahnus29/kotodama-shokunin/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-73: PASS legs=11/11
exit 0
```

## 2. Header cross-check

```
$ sha256sum reports/round-73/accept-c.py
95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416  reports/round-73/accept-c.py
$ git rev-parse 0316b8883b4f8d44b8efd720140e7f52f734a102^{tree}
9b10fa06a2d3756c8bacfc8fc7b2115921370d97
$ git rev-parse 8841ad3b896a0227674fa0725b818c999118046f^{tree}
17c286f5503426a6063a2279c3862fbf3a74c261
```

- Counter sha256 == the `# counter sha256 (self):` line in `reports/round-73/telemetry/controls-c.txt` **and** in my lands run. ✓
- `# tree:` in my lands run == `git rev-parse 0316b88^{tree}`. ✓
- `# tree:` in `controls-c.txt` == `git rev-parse 8841ad3^{tree}` (the control ran at the base). ✓

## 3. Determinism — two runs at lands

Raw diff is only the temp paths:

```
8c8
< # materialized: git archive of the stamped revision at /tmp/r73-lands-d8lvqcbr/lands
---
> # materialized: git archive of the stamped revision at /tmp/r73-lands-_9vl4qbf/lands
24c24
<      exit=0 last-line=kotodama	ok	/tmp/r73-fleet-cmxb7uf6/kotodama-shokunin/corpus/SOURCES.md
---
>      exit=0 last-line=kotodama	ok	/tmp/r73-fleet-o8qtjel5/kotodama-shokunin/corpus/SOURCES.md
```

After normalizing `/tmp/r73-(lands|fleet)-*`, `diff` exits 0 and both files hash `39ce08059c91235ec80a85ebd95f7a20afe9b78686710f6f0c06171ad39f1e5f`. **Deterministic.** Exit codes both 0.

## 4. Leg table per revision

Every run used the same counter bytes and `--fleet-root /home/vgpnk/Projects/shokunin` (see M5 for why that flag is needed outside the lane).

| revision | role | ENT | ROWS | REPT | GATE | EVID | REJ | GROUND | CITED | CENSUS | MIRROR | COLL | verdict | exit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `8841ad3` | frozen base | F | F | F | F | F | F | F | F | **P** | F | F | FAIL 1/11 | 1 |
| `af65165` | freeze | F | F | F | F | F | F | F | F | **P** | F | F | FAIL 1/11 | 1 |
| `e62d731` | Ca SCORECARD/SHONEN | F | F | F | F | F | F | F | F | **P** | F | F | FAIL 1/11 | 1 |
| `3537899` | Ca counter r2/SKILL | F | F | F | F | F | F | F | F | **P** | F | F | FAIL 1/11 | 1 |
| `85f17eb` | C landing | P | P | P | P | P | P | **F** | P | P | **F** | **F** | FAIL 8/11 | 1 |
| `0316b88` | lands | P | P | P | P | P | P | P | P | P | P | P | **PASS 11/11** | 0 |

`e62d731` and `3537899` are byte-identical to the base run except the stamped/evaluated/tree lines (verified by normalized diff); the three intermediate commits requested were `e62d731`, `3537899`, `85f17eb` (from `git log --format=%H 8841ad3..0316b88`, 5 commits, freeze + 2 Ca + C + repair).

**`af65165` (freeze) full output, exit 1 — all red except CENSUS:**

```
# stamped revision: af65165cf269db346ef872e16a656eccd7264d01
# evaluated revision: af65165cf269db346ef872e16a656eccd7264d01
# tree: 7b50777ed53b124e984d9945d8369568be51a02d
# config source: lands tree: row_set, entries, rejects.refused_staged, rejects.refused_files, rejects.families, rejects.forbidden_ids, ground.fragments
LEG FAIL ENTRIES
     corpus/knowledge/linguistics/conlang-scholarship.md missing; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md missing
LEG FAIL ROWS
     added=[] (want ['S876', 'S877', 'S878', 'S879', 'S880']); ... S876 row missing; ...; used-by union [] (want both admitted entries)
LEG FAIL REPOINTED
     corpus/knowledge/linguistics/conlang-scholarship.md missing; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md missing
LEG FAIL GATE
     corpus/lessons/round-73.md
LEG FAIL EVIDENCE
     corpus/lessons/round-73.md
LEG FAIL REJECTS
     corpus/lessons/round-73.md
LEG FAIL GROUND
     receipt does not name ojs.unito.it; receipt does not name philol.msu.ru; receipt does not name journals.rudn.ru; receipt does not name cyberleninka.ru/article/n/klassifikatsii; receipt does not name sanders.phonologist.org
LEG FAIL CITEDLINES
     corpus/knowledge/linguistics/conlang-scholarship.md missing; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md missing
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r73-fleet-m358quff/kotodama-shokunin/corpus/SOURCES.md
LEG FAIL SCRATCHMIRROR
     receipt does not carry S876, S877, S878, S879, S880; no registry-append commit reachable from lands for S876
LEG FAIL COLLCHECK
     .ufo/waves/round-73/assimilation/id-renumber-map.json has no map object; map records no old->new for S876; ... for S880
ACCEPT-C-73: FAIL legs=1/11
```

Reasons: at the freeze the lesson `corpus/lessons/round-73.md` and both entries do not exist; the gap-sweep receipt prints escaped regexes, not literal fragments; the mirror receipt has no row ids and no append commit is reachable; the pre-data map holds its assignments in a list (`assignments`), not under `map`.

**`85f17eb` (C landing) red legs and reasons, exit 1:**

```
LEG FAIL GROUND
     receipt does not name ojs.unito.it; ... sanders.phonologist.org
LEG FAIL SCRATCHMIRROR
     receipt does not carry S876, S877, S878, S879, S880
LEG FAIL COLLCHECK
     .ufo/waves/round-73/assimilation/id-renumber-map.json has no map object; map records no old->new for S876 ... S880
ACCEPT-C-73: FAIL legs=8/11
```

**`8841ad3` (base) full output, exit 1 — the do-nothing control reproduced:**

```
LEG FAIL ENTRIES      corpus/knowledge/linguistics/conlang-scholarship.md missing; ...amend-2026-10-23.md missing
LEG FAIL ROWS         added=[] (want [...]); ...; used-by union []
LEG FAIL REPOINTED    both entries missing
LEG FAIL GATE         corpus/lessons/round-73.md
LEG FAIL EVIDENCE     corpus/lessons/round-73.md
LEG FAIL REJECTS      corpus/lessons/round-73.md
LEG FAIL GROUND       receipt missing: reports/round-73/telemetry/gap-sweep.txt
LEG FAIL CITEDLINES   both entries missing
LEG PASS CENSUS       exit=0 last-line=kotodama	ok	/tmp/r73-fleet-ss6mvhpk/kotodama-shokunin/corpus/SOURCES.md
LEG FAIL SCRATCHMIRROR receipt missing: .ufo/waves/round-73/assimilation/validate-receipt.txt
LEG FAIL COLLCHECK    collision id files missing under .ufo/waves/round-73/assimilation
ACCEPT-C-73: FAIL legs=1/11
exit 1
```

This is exactly the claim's `do_nothing_control` sentence ("FAIL legs=1/11; only CENSUS … green"). ✓

## 5. Selftest

```
cd "$D/lane" && python3 -B reports/round-73/accept-c.py --selftest
SELFTEST: 29/29
exit 0    (2.9 s)
```

Verdict line matches `reports/round-73/telemetry/selftest.txt`, `selftest-r2.txt` and `selftest-r3.txt`, all of which carry `SELFTEST: 29/29` at the same counter sha `95aee881…`.

## 6. Comparison with the committed receipts — every difference

**`reports/round-73/telemetry/controls-c.txt` vs my base run.** Normalized diff (temp paths collapsed) is:

```
-$ python3 -B reports/round-73/accept-c.py --root . --lands 8841ad3b896a0227674fa0725b818c999118046f
 # round-73 acceptance counter — claim C (conlang-scholarship assimilation)
 # counter sha256 (self): 95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416
 # stamped revision: 8841ad3b896a0227674fa0725b818c999118046f
 # evaluated revision: 8841ad3b896a0227674fa0725b818c999118046f
-# measured revision (lane main): 8841ad3b896a0227674fa0725b818c999118046f
+# measured revision (lane main): 0316b8883b4f8d44b8efd720140e7f52f734a102
 # tree: 17c286f5503426a6063a2279c3862fbf3a74c261
 ...
 ACCEPT-C-73: FAIL legs=1/11
-exit=1
```

Differences, all accounted for: (a) the receipt keeps the command line and an `exit=1` trailer that my capture did not; (b) the receipt's `measured revision (lane main)` is `8841ad3` (lane HEAD then) while my clone's HEAD is the detached lands commit `0316b88` — `print_receipt` prints HEAD, not `<lands>`; (c) I passed `--fleet-root`, which the receipt's command line does not. The eleven leg lines and their detail lines are otherwise identical modulo temp paths. The claim's control sentence is reproduced.

**`reports/round-73/telemetry/selftest*.txt` vs my run.** My `--selftest` prints one line, `SELFTEST: 29/29`, exit 0. Each receipt additionally contains: a header line; the `$ python3 …` command line; an `accept-ca.py --selftest` run (`ERROR: base 8841ad3… is not a commit in /tmp/r73-ca-selftest-…` followed by `SELFTEST OK: 9 scenarios` in `selftest.txt`/`selftest-r2.txt`, `10 scenarios` in `selftest-r3.txt`); and a `sha256sum` block. The accept-c verdict line and its counter sha agree with mine in all three. No other difference.

**No committed PASS-at-lands receipt exists** for claim C (see m1).

---

## 7. Findings

Every finding has the command that reproduces it. Severities per the L1's scale.

### BLOCKER

**B1 — the COLLCHECK leg's 4-space sentence is false about the artifact it names.**
`claims.json` line 152: *"guard-proof shows a planted 1-3-space-indented collision found and a 4-space one not found"*. The guard-proof tree has no 4-space plant at all:

```
$ for f in $(git ls-tree -r --name-only 0316b88 .ufo/waves/round-73/assimilation/guard-proof/); do
    echo "$f four_space_rows=$(git show 0316b88:$f | grep -cE '^ {4}\|[[:space:]]*S[0-9]{3,}')"; done
...guard-proof.txt four_space_rows=0
...run-guard-proof.sh four_space_rows=0
...validate-A1.txt four_space_rows=0
...validate-A2.txt four_space_rows=0
...validate-A3.txt four_space_rows=0
   (all 28 files: 0)
$ git show 0316b88:.ufo/waves/round-73/assimilation/guard-proof/guard-proof.txt | grep -n 'S881' | cut -c1-90
15:831:  | S881 | Planted guard fixture (Enguehard 2022, ojs.unito.it art
19:validate findings naming S881 (must be none): 0
21:A2 control (column-zero-only): sees S881? 0  collisions=17
22:A2 guard   (0-3 spaces)     : sees S881? 1  collisions=18
24:  S881
30:A3 guard   (0-3 spaces)      collisions: 1 -> S881
```

Every S881 mention is the A2/A3 2-space plant; no 4-space fixture exists.

`guard-proof.txt` covers A1 (baseline), A2 (2-space plant found), A3 (separability), real pair. The counter's `leg_collcheck` likewise never tests a 4-space case (it only scans for `INDENTED_ROW_RE` matches plus a detection marker). The 4-space fact itself is **true and documented elsewhere**: `.ufo/waves/round-73/w1/MutRegistryCollision.md:33` — `| m3 | \`    | S881 |\` 4 spaces | 17 / S881 absent — missed | rows 799 (line skipped as indented code); silent | survives both — by design |`. So the claim's verdict is unaffected, but one sentence of a frozen claim leg is wrong about the artifact it cites. If the L1 reads "claim leg" as the predicate only, downgrade to MAJOR; the text is wrong either way.

### MAJOR

**M1 — GATE/REJECTS check `reason` and `flip` section-wide, not per reject row, although the claim says "every reject row carries … reason and flip".**
Mutant (throwaway clone `$D2/lane`, commit on top of lands, then the counter at that commit):

```
python3 - <<'PY'   # blank cells 3 and 4 (reason, flip) of the S894 reject row
p='corpus/lessons/round-73.md'; t=open(p,encoding='utf-8').read().splitlines()
for i,l in enumerate(t):
    if l.startswith('| conlang-scholarship.amend-2026-10-23.md (embedded') and 'S894' in l:
        c=l.split('|'); c[3]=' — '; c[4]=' — '; t[i]='|'.join(c); break
open(p,'w',encoding='utf-8').write("\n".join(t)+"\n")
PY
git commit -am "mutant M2"
python3 -B reports/round-73/accept-c.py --root . --lands HEAD --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS GATE
LEG PASS REJECTS
ACCEPT-C-73: PASS legs=11/11
```

Cause: `leg_gate` ends with `low = "\n".join(section).lower(); if "reason" not in low or "flip" not in low` — the reject table's own header carries both words, so the check is satisfied by the header alone. `leg_rejects` repeats the same section-wide test over the whole lesson. Wave-1 `CritCCounterVacuity.md:117-118` already recorded this survivor (`gate_noreason → PASS`). **The landed data does satisfy the stronger reading** — all six reject rows carry non-empty reason, flip and probed URLs (reason lengths 616/588/614/238/242/110, flip 128/92/78/60/78/48, 1–3 URLs each), and the families paragraph carries reason+flip. So the verdict stands; the leg text does not describe the counter.

**M2 — EVIDENCE's "fetch line" is never checked.**
Mutant:

```
grep -v '^fetch:' reports/round-73/evidence/S876.txt > /tmp/ExecRerunC/S876_nofetch.txt
cp /tmp/ExecRerunC/S876_nofetch.txt reports/round-73/evidence/S876.txt
git add -A && git commit -q -m "mutant M1"
python3 -B reports/round-73/accept-c.py --root . --lands HEAD --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS EVIDENCE
ACCEPT-C-73: PASS legs=11/11
```

`leg_evidence` reads access-date, http-status, sha256, user-agent, quote-found-verbatim, quote, window and the Gate row; it never reads `ev.get("fetch")` or `bytes`. The five landed captures do carry `fetch:` lines (verified), so the verdict stands.

**M3 — EVIDENCE's sha256 is shape-only (64 hex); the capture's bytes are never checked.**
Mutant: `sha256: 000…0` (64 zeros) in `reports/round-73/evidence/S879.txt` → `LEG PASS EVIDENCE`, `ACCEPT-C-73: PASS legs=11/11`.
Corroboration of the landed captures (my own fetches, browser-shaped UA, `/tmp/ExecRerunC/`):

| id | URL | status | bytes | sha256 fetched | evidence sha256 | match |
|---|---|---|---|---|---|---|
| S876 | `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` | 200 | 30289 | `e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c` | same | **yes** (twice, stable) |
| S877 | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1055723 | `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` | same | **yes** |
| S878 | `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` | 200 | 959171 | `9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c` | same | **yes** |
| S879 | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` | 200 | 97622 / 97656 / 97554 | `165c93e0…`, `0fb80d6b…`, `6ea71288…` (three fetches, all different) | `709e186b934c9ccb…` | **no — page is dynamic** |
| S880 | `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` | 200 | 193610 | `26dbcf2c0fab6d75214df6285e5c7dab92544f598d81a063df91fb4995a0d535` | same | **yes** |

4 of 5 captures are byte-exact today; S879's sha cannot be re-derived because the page varies per request (its quote and byte order are present — see §8). The EVIDENCE leg cannot tell a real capture from a forged one; wave-1 already declared this (`CritCCounterVacuity.md:207`).

**M4 — SCRATCHMIRROR does not check "both entries", and its "strictly before the registry-append commit" test only looks at the receipt's *introduction* commit.**
Mutant M5 (entry pins deleted from the mirror receipt) → `LEG PASS SCRATCHMIRROR`, `ACCEPT-C-73: PASS legs=11/11`. Control M6 (ids block deleted) → `LEG FAIL SCRATCHMIRROR`, `ACCEPT-C-73: FAIL legs=10/11` — so the ids check is live, the entries check is not.
`leg_scratch_mirror` uses `git log <lands> --diff-filter=A -- RECEIPT` and takes the last line: the *add* commit is `af65165` (pre-append). But the receipt's graded bytes at lands were written at `0316b88`, which is **after** the append at `85f17eb`:

```
$ git log --format='%H %s' -- .ufo/waves/round-73/assimilation/validate-receipt.txt
0316b88… round-73 C: repair artifact shapes found at first grading (... mirror receipt ids ...)
af65165… round-73: freeze — ...
$ git diff 85f17eb 0316b88 -- .ufo/waves/round-73/assimilation/validate-receipt.txt
+## ids carried (appended 2026-10-25 after the landed data was first graded; the mirror run above inserted exactly these five rows)
+mirror registry sha256 93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774 == the lane registry sha256 after the append ...
+S876 row sha256 95d0e105…  ... S880 row sha256 8cb61588…
```

The receipt is honest about the post-grading append, and the strongest pre-data prediction it records is **true**: I verified `sha256(corpus/SOURCES.md at 85f17eb) = 93d60464…` (equals the mirror sha committed at the freeze), the two entry pins equal the lands entries (`5584ecc0…` main, `089d41b9…` amend), and all five row-line shas in the ids block equal the actual row lines at lands (each `MATCH` nonl). But the counter re-derives none of this; the leg's sentence "in a commit strictly before the registry-append commit" is only true of the file's introduction, not of the bytes it grades.

**M5 — the claim's `after` command is not reproducible in a throwaway clone; CENSUS needs an undocumented `--fleet-root` and reads an unpinned external script.**
§1 shows `FAIL legs=10/11` with `census script not found: /tmp/tmp.1ofjQ5bDBh/scripts/sources-census.sh`. `leg_census` defaults `fleet_root` to `dirname(root)`; in a clone that is the clone parent, which has no `scripts/`. The claim's `counter` field and its `after` sentence name no flag. With `--fleet-root /home/vgpnk/Projects/shokunin` (or `--census-sh`) it is 11/11. The script it runs is the fleet's live worktree copy — tracked at fleet blob `3f314620b2395eeb70d8405410132027dfe608e4`, sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`, clean — but the receipt names neither its revision nor its sha. Also note `leg_census` passes `--today 2026-10-25` (the access date), which pins E08 ("opened not a past/present date") to the round's date; that is defensible for this claim but is another hidden input.

**M6 — the ENTRIES leg does not check "absent at base", though its text says it does.**
Run with a base that already holds both entries:

```
python3 -B reports/round-73/accept-c.py --root . --lands 0316b88… --base 85f17eb… --fleet-root /home/vgpnk/Projects/shokunin
# base revision: 85f17eb9f977d16d9c1d0caaf213c41265ceb217
LEG PASS ENTRIES
LEG FAIL ROWS
LEG PASS REPOINTED
...
ACCEPT-C-73: FAIL legs=9/11
```

`leg_entries` reads only the lands tree (`mat_base` is used solely for the word floor). The base-absence property is covered by GROUND's `strays` check (`corpus/knowledge` basenames containing `conlang-scholarship`), which is why the overall run still fails; the leg text attributes the check to the wrong leg.

**M7 — the renumber map's `map` object, which COLLCHECK reads, was committed after the data, although the claim calls the map "committed pre-data".**
`claims.json`: *"Adopted staged->lane map (by document, committed pre-data at .ufo/waves/round-73/assimilation/id-renumber-map.json)"*.

```
$ git show af65165:.ufo/waves/round-73/assimilation/id-renumber-map.json | python3 -c "import json,sys;print(list(json.load(sys.stdin).keys()))"
['round','wave','seat','drafted','supersedes',...,'assignments','assignment_order_rule','conditional_assignments','not_assigned','stale_entries','campaign_id_defects']
$ git show 0316b88:…/id-renumber-map.json | python3 -c "import json,sys;d=json.load(sys.stdin);print('map' in d, d.get('map'))"
True {'S881': 'S876', 'S882': 'S877', 'S892': 'S878', 'S893': 'S879', 'S901': 'S880'}
$ git log --format='%H %s' -- .ufo/waves/round-73/assimilation/id-renumber-map.json
0316b88… round-73 C: repair artifact shapes ... (renumber map key) ...
af65165… round-73: freeze — ...
```

The mapping is pre-data in substance: the freeze file's `assignments` already carry the same five `staged_id → new_target → url` triples, and ROWS passed at `85f17eb` because `_map_url` scans any top-level list of dicts. The `map` object that COLLCHECK requires (`doc.get("map")`) is post-data. The commit message and `R73-M6` disclose the reshape; the claim sentence does not distinguish the key from the file.

### MINOR

- **m1 — no committed PASS-at-lands receipt for claim C.** `ls reports/round-73/telemetry/` has `controls-c.txt` (base FAIL) and the selftests only; `grep -rl "ACCEPT-C-73: PASS" reports/round-73/` hits only `claims.json` and `accept-c.py`. The after-state is reproducible (this report) but not receipted; QUALITY 23's receipt obligation is met for the selftest, not for the lands verdict.
- **m2 — counter docstring is stale:** it says `Legs (10):` (`accept-c.py:21`) and never documents `EVIDENCE`, while 11 legs run (`run_legs` registers 11). The selftest total (5 + 24 = 29) and the claim's 11 legs are right; the docstring is not.
- **m3 — GATE's "locator" is only a cell-count test:** `cells = [c for c in row_cells(row_line) if c]; if len(cells) < 5`. Any fifth non-empty cell satisfies "locator"; the selftest's own clean fixture uses `§1`/`аннотация`/`p. 455` but the check would accept `s`. The landed rows do carry real locators.
- **m4 — GROUND's re-derivation is narrower than the claim's `before`:** it tests only `row_cells(row)[2]` (the URL cell) for each fragment, while `claims.json` says the registry "holds 0 occurrences". I re-derived the stronger reading myself and it holds: `grep -c -F '<fragment>' <base registry>` = 0 for all five fragments anywhere in the 799-row file, last id `S875`, 799 rows, and 0 `conlang-scholarship` files at base, 2 `conlang` files.
- **m5 — ROWS compares normalized URLs, not "verbatim" as its text says:** `norm_url(mapurl) not in neutral_url_keys(urls_in(cells[2]))`. The landed rows do carry the map URL verbatim.
- **m6 — `# measured revision (lane main)` prints HEAD:** the lane's HEAD is detached (`git symbolic-ref -q HEAD` → empty) though it equals `main` at `0316b88`. The label is accidentally true today; in my clone at base it printed `0316b88` (the clone HEAD) while stamping `8841ad3`.
- **m7 — `corpus/QUALITY.md` was edited in place at the landing commit** (`git diff 85f17eb 0316b88 -- corpus/QUALITY.md` adds the freeze-commit-run sentence to QUALITY 23). Legal under the freeze clause (no seat had scored), disclosed in `R73-M6`, but the round's criteria text moved at lands.
- **m8 — a claim-C artifact was edited to make claim Ca green:** `corpus/README.md`'s C footer lost the ids at `0316b88` (`Registry: 799 → 804 rows (S876–S880, …)` → `(five new rows, …)`), commit message "README footer without claim-C ids", `R73-M6` "Ca SEPARABLE red because the C README footer cited S876". Disclosed; still a cross-claim coupling inside claim C's bytes.
- **m9 — S879's evidence sha256 is not re-derivable** (dynamic page, three fetches today at 97622/97656/97554 B). The capture is not falsified: its quote is present in the page (see §8), and the leg only checks the digest shape.
- **m10 — evidence captures are self-attesting:** no response bytes are committed, so a forged capture passes (wave-1 declared it). For the landed set this is not a live risk: I verified all five quotes against live sources (§8), and S876's capture was independently fetched in wave 1.

## 8. Independent checks of the landed bytes (what the PASS rests on)

All exercised by me unless marked.

- **Before-state** (base `8841ad3`): 799 rows by the claim's own regex; last id `S875`; all five fragments 0 hits **anywhere** in `corpus/SOURCES.md`; 0 `conlang-scholarship` files; exactly the two `conlang` files the claim names. ✓
- **Rows:** five rows added contiguously S876–S880; `opened 2026-10-25`, `recheck 180d`, `status mined`; used-by exactly the citing entries (S876/S877 → main entry, S878/S879/S880 → amend). ✓
- **Row-line pins:** all five sha256 values in the mirror receipt's ids block equal the actual row lines at lands (nonl). ✓
- **Entry pins:** `5584ecc0…` main, `089d41b9…` amend — equal to the lands entries. ✓
- **Mirror registry pin:** `93d60464…` equals the post-append registry at `85f17eb` and `0316b88`. ✓
- **Gate quotes vs sources** (browser-shaped UA, `/tmp/ExecRerunC/`):
  - S876 16 words — present verbatim in the fetched page (30289 B, sha `e7260b49…`, equals the capture);
  - S877 9 words — present verbatim in the PDF (`pdftotext`, line 382 of the extracted text; 1055723 B);
  - S878 24 words — present verbatim in the PDF (959171 B, sha equals the capture);
  - S879 16 words — present verbatim in the fetched page (`2.2. Personal languages Это личные, или персональные, языки, …`), byte count matches the capture, sha does not (dynamic);
  - S880 25 words — present verbatim in the PDF (193610 B, sha equals the capture).
  The lesson's stated word counts (16/9/24/16/25) are correct.
- **Archive anchors in the rows** (4 URLs, browser UA, all HTTP 200): 30289 / 1055723 / 959171 / 193610 B — the same byte counts as the live captures — and each archived body **carries its row's quote** (checked with `pdftotext`/tag-stripping). The S876 archive sha (`575e6ee9…`) differs from the live sha at the same size; the page is otherwise stable live (same sha twice), so the difference is in the archived variant. The rows' archive claims are not false.
- **Reject rows:** six rows, each with non-empty reason, flip and 1–3 probed URLs; families named not adopted with reason+flip. ✓
- **Census at lands:** `exit=0`, `kotodama ok`, no E-codes (via the counter's materialized-fleet run). `census-end.txt` is the same verdict on the live lane. ✓
- **CITEDLINES:** `CITED-LINES: 0 finding(s) in 2 file(s)` from the materialized tree. ✓
- **Round-71 map untouched base..lands** and the map's five old→new pairs. ✓

## 9. What I could NOT check

- The `accept-ca` counter and claim Ca (outside this seat); `accept-ca --selftest` output in the receipts was not re-run by me.
- The five captures' original fetch instants: I re-fetched today and matched four shas byte-exactly; I cannot prove the captures were made on 2026-10-25 rather than any time the pages held those bytes.
- S879's capture sha256: impossible to re-derive (page varies per request); I verified only the byte count and the quote.
- The item-10 guard pair and the 4-space fixture: I read `w1/MutRegistryCollision.md`'s m3 result, I did not re-run the mutation matrix.
- The census script's internal semantics beyond exit 0 / no E-codes at base and lands; I did not audit its W-code logic.
- The entries' full scholarly quality and every body claim (other seats own that); I checked headers, word floor, source lines, and the quotes.
- The plain `curl/8.7.1` UA leg: no source was walled or unreachable in my probes, so there was no wall to test in either direction; I did not send a plain-UA request.
- Revisions other than the six named above; no run of the counter at a synthetic "no-op" commit other than the mutants listed.

## 10. Retained evidence

- Full outputs: `/tmp/execreerunC_lands.txt`, `_lands_fleet.txt`, `_lane.txt`, `_rev_<rev>.txt` (5), `_selftest.txt`, `_det1.txt`, `_det2.txt`, `_det1n.txt`, `_det2n.txt`.
- Clones: `/tmp/tmp.1ofjQ5bDBh` (pristine), `/tmp/tmp.dMswVBSwqd` (mutants M1–M6, reset to lands; `git status` clean at end).
- Downloads in `/tmp/ExecRerunC/`: `s876.html` (`e7260b49…`), `s876_2.html` (same), `conlangs.pdf` (`e512a20d…`), `s878.pdf` (`9f745dda…`), `s880` pdf as `anderson-etal-cjl-sotl.pdf` (`26dbcf2c…`), `s879.html`/`s879_1.html`/`s879_2.html` (dynamic), and the four Wayback bodies `wb_08bc51bd`, `wb_b7fb420a`, `wb_26bced46`, `wb_a495b8a6`. Every fetch: UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; status/bytes recorded above.
- No tools installed or upgraded; no pacman.
