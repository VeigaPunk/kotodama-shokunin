# X04 — baseline-drift critic (round 48)

- Seat: X04 | role: critic | claim: cross | date 2026-10-19
- Out path: `reports/round-48/cross/X04-baseline-drift.md` (this file)
- Declared baseline: `a01405d` — `reports/round-48/claims.json:7`, `reports/round-48/telemetry/dispatch-declared.json:11`
- Declared instant: `2026-10-19T19:45:00Z` — `claims.json:6`, `dispatch-declared.json:5`
- Observation window: `2026-10-19T19:37Z`–`2026-10-19T19:40Z` (UTC); last git/digest re-check `19:40:02Z`
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Read-only git, read-only gate runs, read-only sweep. No commit, no in-tree round runner, no corpus write, no network.

**Verdict: baseline identity and digest pinning PASS; the r43 claims.json drift class does not recur. The two `before` premises are true at the baseline tree, and the dropped O claim was correctly refused. Two evidence defects remain, neither a baseline drift: the gate's inputs exist only in gitignored `.scratch` (F-1, durability), and the Ca gate check counts files, not headings, so it would report FRESH after the defect is fixed (F-2, vacuous guard). The C gate check is real but partition-scoped while the claim is corpus-wide (F-3, warn).**

---

## 1. Baseline identity — PASS

```console
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git rev-parse a01405d
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git rev-parse --disambiguate=a01405d | wc -l
1
$ git rev-list --count a01405d..HEAD
0
$ git show -s --format='%H %cI %s' a01405d
a01405dd36367292255c2652ac0a601f4cd6a0af 2026-10-19T16:34:48-03:00 round-47: NOT ADMITTED on C; O+Ca improved — claims-freshness gate landed 62/62 (R01-43-12 closed); C over-built+blocked; loop-2 opener
$ git tag --points-at HEAD          # empty
$ git for-each-ref --format='%(refname) %(objectname:short)' refs/heads
refs/heads/main a01405d
```

- `a01405d` is a **unique, un-ambiguous** object; `refs/heads/main` points at it; no tag points at it.
- Baseline commit time is `19:34:48Z`. `claims.json` was written at `19:36:19Z`, `targets.json` at `19:37:21Z`, `dispatch-declared.json` at `19:37:31Z` — all **after** the baseline commit, all with zero commits following.
- `.git/logs/HEAD` is linear through `6e9a30d → a01405d`; no reset/amend/checkout row. The only remote refs are pre-existing and none is ahead of local `main` in this check.
- The baseline commit adds the r47 gate and reports; it touches **no** corpus file:
  ```console
  $ git diff --name-status 6e9a30d a01405d -- corpus tools
  A	tools/harness/claims-freshness.py
  ```
- Worktree has no tracked drift:
  ```console
  $ git status --porcelain
  ?? reports/round-46/review/
  ?? reports/round-48/
  $ git diff --stat; git diff --cached --stat   # both empty
  ```

## 2. Digest pin audit — PASS (r43 defect class reproduced only as history)

`reports/round-48/` is untracked, so `dispatch-declared.json` is the contract's digest anchor. Both pins match the live bytes byte-for-byte:

```console
$ sha256sum reports/round-48/claims.json reports/round-48/targets.json reports/round-48/telemetry/dispatch-declared.json
bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292  reports/round-48/claims.json
d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446  reports/round-48/targets.json
40a96ab6227ca229d615a8bdcca1d32124447a5433bfbe53f7e26c9e33d2ab4e  reports/round-48/telemetry/dispatch-declared.json
```

- `dispatch-declared.json:15` pins `bf8df21b…` == live; `:16` pins `d029eaa1…` == live and `seat_count: 64` == 64 unique seat ids in `targets.json` (my count).
- The r43 defect is real and reproduces exactly: `reports/round-43/telemetry/dispatch-declared.json:14` pins `beda7644…` / 6353 B, while the live file is `9662e2bd…` / 6546 B (`sha256sum`, `wc -c`). The r43 closing snapshot records the re-pin at `reports/round-43/telemetry/availability-close-43.json:18`.
- **At r48 the class does not recur.** No post-declaration edit to either contract file: the digests are unchanged from the dispatch pin at `19:37:31Z` through my last check at `19:40:02Z`, and both contract files predate the dispatch record.

## 3. Declared freshness-gate evidence — the one substantive drift

`claims.json:21-23` and `dispatch-declared.json:18-21` declare the gate's first live use. The declared command is a **template**, not a runnable path:

> `python3 tools/harness/claims-freshness.py --claims <candidates> --checks <overlay>` (`claims.json:22`)

No candidate file, overlay path, decision digest, or exit code is named. The only surviving inputs are two gitignored scratch files:

```console
$ git check-ignore -v .scratch/r48-claims-skel.json .scratch/r48-freshness-check.json
.gitignore:6:.scratch/	.scratch/r48-claims-skel.json
.gitignore:6:.scratch/	.scratch/r48-freshness-check.json
$ ls reports/round-48/telemetry/
dispatch-declared.json
```

### 3.1 What does reproduce

Replaying the declared gate on the surviving three-claim skeleton (which still contains O) and the surviving overlay:

```console
$ python3 -B tools/harness/claims-freshness.py \
    --claims .scratch/r48-claims-skel.json \
    --checks .scratch/r48-freshness-check.json --json
exit 1
summary: 3 claims, 4 clauses; 2 fresh, 1 stale, 0 could-not-evaluate, 0 malformed; 3 hold, 1 contradict
[C]  fresh  — cartography unowned HOLDS (0 owners); culture-material 25 HOLDS (25 files)
[O]  stale  — resolver blank-hyphen edge CONTRADICTED (capability_present, 0/1 candidate passes)
[Ca] fresh  — README duplicate heading HOLDS (corpus/README.md -> 1 file(s))
baseline_sha a01405dd36367292255c2652ac0a601f4cd6a0af
```

So the **reported shape is honest**: C fresh (2/2), Ca fresh (1/1), O stale, exit 1, and O was then dropped rather than dispatched. The r47 gate did catch a stale premise. But the result is reproducible only from **gitignored scratch**, and the published contract cannot be replayed into it:

```console
$ python3 -B tools/harness/claims-freshness.py \
    --claims reports/round-48/claims.json \
    --checks .scratch/r48-freshness-check.json --json
exit_code: 2
errors: [".scratch/r48-freshness-check.json: overlay names claim 'O', absent from the claims file"]
summary: 0 claims, 0 clauses, 0 verdicts
```

### 3.2 F-1 (open, durability) — the round's gate evidence is outside the durable record

`AGENTS.md` requires dispatch evidence under `reports/round-<N>/telemetry/`, with the durable source paths and SHA-256 digests, never only `.scratch`. At this cut:

- the overlay (`r48-freshness-check.json`, 1806 B) and candidate skeleton (`r48-claims-skel.json`, 438 B) are gitignored copies with no filed digest;
- `claims.json` carries **no `before_checks`** (`grep -c before_checks reports/round-48/claims.json` → `0`), so the gate cannot be re-run from the contract alone;
- no gate report, decision digest, or exit code is filed anywhere under `reports/round-48/`.

**Effect:** the claim that the gate "flagged O STALE; C FRESH; Ca FRESH" is *unreproduced from filed bytes* at close, though it *reproduces from live scratch*. That is a provenance gap, not a false result. **Fix (integrator):** file an append-only `reports/round-48/telemetry/freshness-gate-48.json` containing the candidate file used at declaration, the overlay, the exact command, exit code, decision sha, and the sha256 of both inputs; alternatively add the overlay to `claims.json` as `before_checks` and re-run. Do not edit the filed `dispatch-declared.json`; file a new snapshot.

### 3.3 F-2 (open, vacuous guard) — the Ca check counts files, not headings

The overlay's Ca check is:

```json
{"clause": "README duplicate heading", "probe_kind": "count_eq",
 "target": {"glob": "corpus/README.md", "value": 1}, "expect": false,
 "evidence_command": "grep -c '^# kotodama-shokunin corpus index' corpus/README.md -> 2"}
```

The compat shim rewrites `count_eq` + `value` into `expect = 1` (`tools/harness/claims-freshness.py:2193`), and `_probe_count_eq` measures `len(paths)` for the glob (`:1053-1056`). The measured reason is literally `corpus/README.md -> 1 file(s)`. It never opens the file. Therefore:

- it holds at baseline (one README file exists), and it would **still hold after the duplicate H1 is removed** — exactly the stale premise the gate is supposed to refuse;
- the `evidence_command` (`grep -c … -> 2`) is recorded as a string and **not executed** by the gate (the tool's own output labels it `evidence`, not a measurement);
- the landed probe vocabulary has no content-count probe at all (`:98-104`, `:875-883`): `count_eq` is file-glob count, `grep_absent` is match-absence, `sha256_eq` is whole-file digest.

**Effect:** `claims.json:23`'s "Ca FRESH (README duplicate-heading holds)" is true only by my independent `grep` (count 2 at `corpus/README.md:1,3`), not by the gate. **Fix:** add a `grep_count_eq`/`line_count_eq` probe (glob + regex + integer expect) or express the premise as `sha256_eq` on the README and require the digest to change at apply; until then the Ca premise needs a hand-filed measurement with its own digest.

### 3.4 F-3 (warn, scope) — the C check is partition-scoped; the claim is corpus-wide

The C check uses `partitions: ["culture-material"]`, `fields: ["h1","topic","gap filled"]`, aliases `cartography|mapmaking|portolan|cadastral` and reports `0 owner(s)`. The probe iterates only `target["partitions"]` (`tools/harness/claims-freshness.py:1088`). The claim says "0 owners at a01405d" without a partition qualifier (`claims.json:30`), and the r44 scout's freshness argument is corpus-wide.

Independent corpus-wide measurement at the baseline tree confirms the premise anyway:

```console
$ git grep -nEi '^- topic:.*(cartograph|mapmak|portolan|cadastr)' a01405d -- corpus/knowledge | wc -l
0
$ git grep -niE 'cartograph|mapmak|portolan|cadastr' a01405d -- corpus/knowledge
…/japan-medieval-sengoku.md:157   (a cadastral-map caution)
…/mesoamerica-primary-sources.md:58 (lienzo/cartographic histories row)
…/architecture-settlement-lexicon.md:95 (groma; "grid is cadastral")
…/myth-symbol/cosmology-cosmography.md:102 ("not cartographic claims")
$ git cat-file -e a01405d:corpus/knowledge/culture-material/cartography-and-mapmaking.md
fatal: path does not exist in 'a01405d'
```

So the result is right; the guard is narrower than the claim. **Recommendation for the landing re-check (C06/V01):** widen `partitions` to all six, or at minimum add `myth-symbol`, so the "no second owner" assertion is measured, not assumed.

## 4. Premise truth at the baseline tree — PASS

All measurements below are `git ls-tree` / `git show` at `a01405d`, not the worktree, except where labelled.

| Premise | Source | Measured at `a01405d` | Verdict |
|---|---|---|---|
| total 223 | `claims.json:30` | `git ls-tree -r --name-only a01405d corpus/knowledge \| grep -c '\.md$'` → **223** | true |
| culture-material 25 | `claims.json:30` | same, `…/culture-material` → **25** | true |
| cartography unowned / target free | `claims.json:29-30` | 0 topic owners corpus-wide; `git cat-file -e` → absent | true |
| README duplicate H1 (lines 1, 3; count 2) | `claims.json:44` | `grep -n '^# kotodama-shokunin corpus index'` → `1:`, `3:`; count 2 | true |
| r47 over-build = 790 lines | `claims.json:19,44,63` | `.scratch/q01-assembled.md` → 790 lines, 128,670 B, sha `e0c8ae56…` == `reports/round-47/cross/Q01-final-gate.md:87,304` | true (basis note §5) |
| R03 B1–B9 are nine blocking rows | `claims.json:29` | `grep -cE '^\| \*\*B[0-9]+\*\*' reports/round-47/review/R03-c-content.md` → **9** (B1…B9) | true |
| R36 defect id is real and still open | `claims.json:43` | `reports/round-40/op/defect-queue-v2.json:112` `R36-README-DUPLICATE-HEADING`, class `carried-with-owner`, `verification: null`; live heading count 2 | true |

README digest is stable across baseline, worktree and the sweep: `git show a01405d:corpus/README.md | sha256sum` = `sha256sum corpus/README.md` = `7c788a1d…` = sweep's `readme_sha256`. Live sweep: `rows 223 files 223`, `missing 0`, `topic_mismatch 0`, `orphan_rows 0`, footer `[25,26,25,29,24,94]`, exit 0.

Arithmetic re-derived, not copied (README anchors `corpus/README.md:544,548`; vector at `:11`):

```text
live footer        25+26+25+29+24+94 = 223
rev-2.4 defective  25+23+26+25+24+94 = 217
rev-2.5 candidate  25+26+26+29+24+94 = 224
```

## 5. Number-basis and provenance notes

- **790 vs 739 vs 797.** The claim's "790-line over-build" names the *assembled file* (`Q01-final-gate.md:87`: 790 = 51 head + 739 body); R03's headline measure is the 739-line *body* (`reports/round-47/review/R03-c-content.md` §1); Q01 later records a corrected 797-line assembly (`Q01-final-gate.md:368`). All three are filed numbers about different objects. The claim is consistent with the primary assembly measure, but the round's guard should be the partition band (max 221; brief ≤ ~250), not a countdown from any of 739/790/797.
- **The r48 queue row is overdue.** `R36-README-DUPLICATE-HEADING` has `next_touch: "r42 or r44 (corpus-owning build round)"` (`reports/round-40/op/defect-queue-v2.json:112`) and is still open at r48 — four rounds past its own next touch. The Ca claim is the right disposition; the closing snapshot should record the lateness, not only the fix.
- **Parent queue is pinned and unchanged.** `sha256sum reports/round-40/op/defect-queue-v2.json` = `dfc9265d…`, equal to `reports/round-47/calib/queue-successor-r47.json:8-9` (`parent_sha256_at_assembly` and recheck). Any r48 successor must reference, not edit, this digest.

## 6. Drift register

| id | class | evidence | status | effect on C / Ca |
|---|---|---|---|---|
| D-1 | commit drift after declaration | `rev-list a01405d..HEAD` → 0; reflog linear; `main` pinned; no tags | **PASS** | none |
| D-2 | contract digest drift (r43 class) | claims `bf8df21…`, targets `d029eaa…` == dispatch `:15-16`; r43 mismatch reproduced only as history | **PASS** | none |
| D-3 | worktree tracked-file drift | `git diff`/`--cached` empty; only r46 review + r48 trees untracked | **PASS** | none |
| D-4 | premise drift at baseline | §4 table, all in-tree | **PASS** | none |
| D-5 | evidence durability (F-1) | gate inputs only in `.scratch`; no `before_checks` in claims; no filed gate report | **FAIL / open** | verdict is reproducible from scratch, not from filed bytes |
| D-6 | guard fidelity (F-2) | Ca check measures `corpus/README.md -> 1 file(s)`; would pass post-fix | **FAIL / open** | "Ca FRESH" is independently true but not gate-established |
| D-7 | guard scope (F-3) | C check scans `culture-material` only; claim says corpus-wide | **WARN** | result true by independent grep; guard narrower |
| OBS-1 | declared instant is later than the artifacts | contract mtimes 19:36:19Z–19:37:31Z, `declared_at_utc` 19:45:00Z; observation 19:40:02Z; baseline commit 19:34:48Z | **info** | timestamps do not bind; digests do |
| OBS-2 | 790/739/797 are different objects | §5 | **info** | none |

**OBS-1 detail.** The declared instant is 5–8 minutes *after* every contract file was written and after seats had already begun filing into `reports/round-48/` (13 files at `19:40:02Z`). At r47 the sign was inverted (declaration 10 s before the commit, mtimes +15.8 s — `reports/round-47/cross/X05-baseline-drift.md` OBS-2). Conclusion: `declared_at_utc` records intent, never a measurement; the digest pins and the baseline commit are what bind. No correction is owed, but the closing snapshot should not cite `19:45:00Z` as the measurement time.

## 7. Could-not-evaluate (stated, not guessed)

- **Actual dispatch observations.** `dispatch-declared.json` records `requested_workers: 64`, `batched_calls: 1`, model and key; no availability sample, launch count, completion count, or route telemetry exists under `reports/round-48/telemetry/` at this cut. Requested is not observed — `could-not-evaluate`, no inferred zeroes.
- **The candidate file as actually run at declaration.** The surviving skeleton is the only candidate; whether the gate was invoked on exactly those bytes is not provable without a filed report (F-1).
- **Seat deliverables.** I read only my own inputs plus the r47/r44 evidence; I judge no other seat's fragment.
- **Remote refs.** `refs/remotes/origin/HEAD` points at `139e3b6`, not `a01405d`; I did not fetch, and remote freshness is outside this lane's evidence.

## 8. Commands and write surface

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19, 19:37Z–19:40Z.

```console
git rev-parse HEAD; git rev-parse a01405d; git rev-parse --disambiguate=a01405d | wc -l
git rev-list --count a01405d..HEAD; git show -s --format='%H %cI %s' a01405d
git reflog (tail); git tag --points-at HEAD; git for-each-ref refs/heads
git status --porcelain; git diff --stat; git diff --cached --stat
git diff --name-status 6e9a30d a01405d -- corpus tools
git ls-tree -r --name-only a01405d corpus/knowledge | grep -c '\.md$'
git ls-tree -r --name-only a01405d corpus/knowledge/culture-material | grep -c '\.md$'
git grep -nEi '^- topic:.*(cartograph|mapmak|portolan|cadastr)' a01405d -- corpus/knowledge | wc -l
git grep -niE 'cartograph|mapmak|portolan|cadastr' a01405d -- corpus/knowledge
git cat-file -e a01405d:corpus/knowledge/culture-material/cartography-and-mapmaking.md
git show a01405d:corpus/README.md | sha256sum; sha256sum corpus/README.md corpus/README.md
sha256sum reports/round-48/{claims,targets}.json reports/round-48/telemetry/dispatch-declared.json
sha256sum reports/round-40/op/defect-queue-v2.json
grep -n '^# kotodama-shokunin corpus index' corpus/README.md
grep -cE '^\| \*\*B[0-9]+\*\*' reports/round-47/review/R03-c-content.md
python3 -B reports/round-28/readme/sweep.py
python3 -B tools/harness/claims-freshness.py --claims .scratch/r48-claims-skel.json --checks .scratch/r48-freshness-check.json --json
python3 -B tools/harness/claims-freshness.py --claims reports/round-48/claims.json --checks .scratch/r48-freshness-check.json --json
python3 -B tools/harness/claims-freshness.py --selftest     # registry 43/43 + seam 19/19, exit 0
```

**Write surface:** this file only — `reports/round-48/cross/X04-baseline-drift.md`. No `corpus/**`, `tools/**`, `LOG.md`, `SCORECARD.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. The gate replays were read-only; the `--json` replay wrote its output only to the shell pipe / `/tmp` for parsing. No in-tree `run-validation.py`, no re-freeze, no packet-surface change, no commit/push/install/network.

**Bottom line for the integrator:** do not record baseline drift — there is none. Record F-1 and F-2 as open evidence defects with owners: file the gate inputs and decision under `reports/round-48/telemetry/`, and either add a content-count probe or hand-file the heading measurement with its digest. C and Ca remain true at `a01405d`; O was correctly refused.
