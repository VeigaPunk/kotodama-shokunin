- Seat: O05 | executor | claim O (falsifier leg) | date 2026-10-19 | baseline 139e3b6

# O05 — the falsifier-audit filename mismatch (F-X16-3): located, bounded, repoint draft + controls

Verdict: **located and bounded.** The exact repoint draft is at §3 (integrator-applied; no
filed-byte rewrite). A 7-scenario control set (§4) proves the repointed instrument on the live
tree and on synthetic fixtures, including two controls where the *old* instrument gives the
wrong answer. This file is claim O's counting-command artifact
(`test -s reports/round-33/op/O05-falsifier-disposition.md`).

Dependency note. `reports/round-33/op/K01-falsifier-scout.md` (sha256
`9d9dbe83b8b5ca38299cd273786f8c0d4cdb78312edc97ccf6629ba4bf5a7968`) landed mid-flight and is
the scout leg for this disposition; `reports/round-33/op/P01-plan.md` **did not exist** at this
seat's read (see `## Owed`). This seat's scouting ran before K01's file was readable and is
independent of it; the two agree on every checked element, including the `closes` /
`closes_record` key-name nuance K01 raised at its `:82-91`.

## 1. What is being dispositioned

| element | pointer |
|---|---|
| the routed debt, as SCORECARD states it | `SCORECARD.md:443-445` — "the falsifier audit's filename mismatch (substance 5/5)" |
| the finding (full text) | `corpus/lessons/round-32.md:41` (F-X16-3); its heading at `:36` — "The falsifier legs — substance 5/5, instrument false-fires on day one" |
| the open route | `corpus/lessons/round-32.md:55` (Q-32-1, owner parent/operator) |
| the instrument (the mismatch lives here) | `SKILL.md:713-715`, landed by commit `17e90b9` (`git show 17e90b9 -- SKILL.md`, hunk `@@ -710,3 +710,6 @@`) |
| the falsification clause it fires against | `LOG.md:3460-3463`, clause (i) |
| the convention it cannot see | `reports/round-{19,25,26,27,28}/telemetry/availability-close-<N>.json` |
| the standing input list naming the debt | `LOG.md:3512-3514` |

Both legs re-reproduced at lane HEAD `139e3b662900557afe54f632b468619593dc9fcb` this session:

- **Instrument leg — false-fires.** The `SKILL.md:715` one-liner, verbatim, exits 0 and prints
  exactly 5 rows: `reports/round-{19,25,26,27,28}/availability.json`. All five records are in
  fact closed.
- **Substance leg — passes 5/5.** For each of the five, the snapshot in that round's
  `telemetry/` names the record and its `closes_sha256` equals the record's live SHA-256
  (`sha256sum` cross-check, not only Python): r19 `fa9588db60c61a70…`, r25 `51d62532bcbafab8…`,
  r26 `7e23f33daa655141…`, r27 `987b04e12b7bcb33…`, r28 `aceb019cfbec7fa9…` — 5/5.

## 2. The defect, exactly

`SKILL.md:713-714` states the rule (an `open-at-seat-close` record whose round's
`validation.json` has landed must carry a closing snapshot). `SKILL.md:715` carries the
executable test, whose closure predicate is:

```
not os.path.exists(os.path.join('reports', f.split('/')[1], 'telemetry', 'closing-snapshot.json'))
```

`closing-snapshot.json` is a **filename that exists nowhere in the repo** (`grep -rn
"closing-snapshot.json"` over the tree: only `SKILL.md:715` itself, the round-32 lesson quoting
it, and K01's fragment quoting it). The landed snapshots are named
`telemetry/availability-close-<N>.json` and are keyed by content — `closes` (the record path)
plus `closes_sha256` — not by that filename. So the predicate is always true and the audit
prints every record it examines: **the instrument cannot see any closure**, on a tree where all
five closures exist.

Two secondary facts, both verified:

1. **The key name in the lesson prose is itself wrong.** `corpus/lessons/round-32.md:41` and
   `:55` paraphrase the snapshot's record pointer as `closes_record`. The live key is `closes`
   (`reports/round-19/telemetry/availability-close-19.json:5`, same shape in 25–28); no
   snapshot in the repo carries `closes_record` (`grep -l closes_record
   reports/round-*/telemetry/*.json` → 0 files). The landed implementation to mirror reads
   `document.get("closes")` at `reports/round-31/run-validation.py:799`. **A re-keyed audit
   that tested `closes_record` would false-fire a second time** — this is the trap the repoint
   draft in §3 avoids.
2. **The pre-landing draft had the opposite defect** — `reports/round-31/jinii/draft.md:40-45`
   carries no closure test at all, so it would have printed the same five rows forever. The
   landing fixed the semantics and broke the path; F-X16-3's "the landing fixed the semantics
   and broke the path" is confirmed at the draft bytes.

## 3. Fix draft — the repoint (integrator applies; SKILL.md is a shared file)

Bounded: one predicate replaced inside one line; the rule sentence, the item's position, and
the "must print nothing" clause are unchanged. No filed byte is rewritten by this seat.

### 3a. Before (verbatim `SKILL.md:713-715`, block sha256 `541bad77bb78f9f18c94aa492febe5ab54e44a74b4ab5c6dd27bde56b0409f41`)

```
- [ ] Every availability/dispatch record filed `open-at-seat-close` whose round's
      validation.json has landed carries a closing snapshot in that round's telemetry/
      (audit: `python3 -c "import json,glob,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not os.path.exists(os.path.join('reports',f.split('/')[1],'telemetry','closing-snapshot.json'))]"` — must print nothing once the round's records are closed)
```

### 3b. After (the repoint; 4 physical lines, command on one physical line)

```
- [ ] Every availability/dispatch record filed `open-at-seat-close` whose round's
      validation.json has landed carries a closing snapshot in that round's telemetry/ whose
      `closes` names that record and whose `closes_sha256` matches the record's live bytes
      (audit: `python3 -c "import glob,hashlib,json,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not any((lambda d: isinstance(d,dict) and d.get('closes')==f and d.get('closes_sha256')==hashlib.sha256(open(f,'rb').read()).hexdigest())(json.load(open(s))) for s in glob.glob(os.path.join('reports',f.split('/')[1],'telemetry','availability-close-*.json')))]"` — must print nothing once the round's records are closed)
```

Design notes, each answering a measured hazard:

- The predicate is **content-keyed, not filename-keyed**: it accepts any file matching
  `telemetry/availability-close-*.json` in the record's own round and requires both
  `closes == <record path>` and `closes_sha256 == sha256(live bytes)`. The filename is thereby
  free to vary (a correction snapshot named `…-correction.json` still closes the record — the
  AGENTS.md append-only correction rule anticipates exactly that), while a snapshot that names
  a *different* record, or whose digest no longer matches (an in-place edit of a filed record),
  does **not** close it.
- This folds clause (ii) (the integrity leg) into the audit: the same command that lists
  unclosed records also lists records whose closure was invalidated by a digest mismatch. The
  substantive form the lesson calls "passes 5/5" is now literally what the item executes.
- `isinstance(d, dict)` guards a snapshot that parses to a non-object; a **malformed** snapshot
  still aborts the command with a traceback rather than silently passing — a loud failure is
  preferred over a silent false green (recorded as a limit in §6, not a defect).
- No `-B` added and no other token changed, keeping the diff minimal against the landed bytes;
  the lane's `python3 -B` convention is orthogonal to this fix.

### 3c. Application instruction for the integrator

Apply 3b in place of 3a at the item's current location (`SKILL.md:713-715`), as a logged
change under the lane identity, and re-run the §4 harness afterwards. **Position is a separate
route**: this item sits at end-of-file inside `## Source-bounded culture drill — D3 (round 7)`
(heading `SKILL.md:660`), outside `## Checklist (executable where a tool exists)`
(`SKILL.md:522`, section content through `:534`) — that is F-X16-2 / Q-32-3, owned by the
parent. The repoint draft is position-agnostic; if the integrator also relocates the item, the
same bytes move. This seat does not absorb Q-32-3.

## 4. Controls — the repoint is proven, not asserted

Harness: `.scratch/o05/build-controls.py` (scratch, gitignored; reproduced inline at §4c). It
builds seven fixture roots under `.scratch/o05/ctl/<name>/reports/round-90/` and runs **both**
the landed one-liner (OLD) and the **one-liner extracted verbatim from §3b's draft bytes**
(NEW — the harness regex-extracts it from `.scratch/o05/after.md`, so the control tests the
draft, not a hand-typed variant). Command: `python3 -B .scratch/o05/build-controls.py`,
2026-10-19, lane root, `TMPDIR=$PWD/.scratch`.

| scenario | fixture state | OLD rc/rows | NEW rc/rows | what it proves |
|---|---|---|---|---|
| `closed` | record + receipt + valid snapshot (`closes`+digest) | 0 / **1** | 0 / **0** | the false fire is cleared on the live convention |
| `unclosed` | record + receipt, no snapshot | 0 / 1 | 0 / **1** | the repoint still fires on a genuine gap |
| `digest-mismatch` | snapshot present, `closes_sha256` wrong | 0 / 1 | 0 / **1** | integrity leg (clause ii) is folded in |
| `wrong-pointer` | snapshot present, `closes` names another record | 0 / 1 | 0 / **1** | presence alone never closes a record |
| `legacy-name-only` | a file named `telemetry/closing-snapshot.json` exists, no valid snapshot | 0 / **0** | 0 / **1** | OLD's green was name-based; NEW is substance-based |
| `receipt-absent` | record, no `validation.json` | 0 / 0 | 0 / 0 | non-falsifier 1 (poll window open) still excluded |
| `legacy-attempt-row` | `state: null` (r5/r10 attempt shape) | 0 / 0 | 0 / 0 | non-falsifier 2 (pre-convention rows) still excluded |

Live tree, same session:

```
live repo root   OLD rc=0 rows=5      # reports/round-{19,25,26,27,28}/availability.json — false fire
live repo root   NEW rc=0 rows=0      # all five closures seen
```

The `closed` and `legacy-name-only` rows are the pair that makes this a control rather than a
demonstration: on the *same* fixture the two instruments disagree, and the disagreement is
resolved in favour of the landed convention by the fixture's content, not by a filename.

### 4a. Independent reproduction of the substance leg (no Python)

```
$ for n in 19 25 26 27 28; do sha256sum reports/round-$n/availability.json; \
    grep closes_sha256 reports/round-$n/telemetry/availability-close-$n.json; done   # 5/5 equal
```

### 4b. Record census behind the OLD fire (so "5 rows" is not read as "5 problems")

9 files match `reports/round-*/availability*.json`: 1 round-5 + 3 round-10 `availability-attempt-*.json`
(all `state: None`, pre-convention, correctly outside both instruments) + the 5
`open-at-seat-close` records above. The OLD fire is 5 rows = 100% of the records it can see,
0% of which are actually unclosed.

### 4c. Harness, verbatim (rebuildable from this fragment alone)

```python
# .scratch/o05/build-controls.py  — run from the lane root with TMPDIR=$PWD/.scratch
# first: copy §3b's after-block verbatim into .scratch/o05/after.md (the harness reads it
# there so the control tests the draft bytes, not a retyped copy)
import hashlib, json, pathlib, re, shutil, subprocess
CTL = pathlib.Path(".scratch/o05/ctl"); DRAFT = pathlib.Path(".scratch/o05/after.md")
OLD = ('python3 -c "import json,glob,os; [print(f) for f in sorted(glob.glob(\'reports/round-*/availability*.json\')) '
       'if json.load(open(f)).get(\'state\')==\'open-at-seat-close\' and os.path.exists(os.path.join(\'reports\',f.split(\'/\')[1],\'validation.json\')) '
       'and not os.path.exists(os.path.join(\'reports\',f.split(\'/\')[1],\'telemetry\',\'closing-snapshot.json\'))]"')
def new_command(): return re.search(r"\(audit: `(.+?)`", DRAFT.read_text(), re.S).group(1)
def build(name, state="open-at-seat-close", receipt=True, snapshot="valid", legacy_name=False):
    base = CTL / name / "reports" / "round-90"; base.mkdir(parents=True)
    rec = base / "availability.json"
    rec.write_text(json.dumps({"round": 90, "state": state, "completed_workers": 3}, indent=1) + "\n")
    if receipt: (base / "validation.json").write_text('{"acceptance_checks_passed": true}\n')
    rel = "reports/round-90/availability.json"; digest = hashlib.sha256(rec.read_bytes()).hexdigest()
    if snapshot != "none":
        t = base / "telemetry"; t.mkdir()
        body = {"valid": {"closes": rel, "closes_sha256": digest, "date": "2026-10-19"},
                "digest-mismatch": {"closes": rel, "closes_sha256": "0" * 64, "date": "2026-10-19"},
                "wrong-pointer": {"closes": "reports/round-91/availability.json", "closes_sha256": digest, "date": "2026-10-19"}}[snapshot]
        (t / "availability-close-90.json").write_text(json.dumps(body, indent=1) + "\n")
    if legacy_name:
        (base / "telemetry").mkdir(exist_ok=True)
        (base / "telemetry" / "closing-snapshot.json").write_text('{"closes": "reports/round-90/availability.json"}\n')
    return CTL / name
def run(cwd, cmd):
    p = subprocess.run(cmd, shell=True, cwd=str(cwd), capture_output=True, text=True)
    return p.returncode, [l for l in p.stdout.splitlines() if l.strip()]
if __name__ == "__main__":
    if CTL.exists(): shutil.rmtree(CTL)
    for name, kw in [("closed", {}), ("unclosed", {"snapshot": "none"}), ("digest-mismatch", {"snapshot": "digest-mismatch"}),
                     ("wrong-pointer", {"snapshot": "wrong-pointer"}), ("legacy-name-only", {"snapshot": "none", "legacy_name": True}),
                     ("receipt-absent", {"snapshot": "none", "receipt": False}), ("legacy-attempt-row", {"state": None, "snapshot": "none"})]:
        root = build(name, **kw); print(name, run(root, OLD), run(root, new_command()))
    live = pathlib.Path(".").resolve(); print("live", run(live, OLD), run(live, new_command()))
```

Observed output, 2026-10-19 (abridged to the rc/rows pairs; full table at §4):

```
NEW command extracted from draft bytes: newline_in_command=False
closed               0/1   0/0        unclosed          0/1   0/1
digest-mismatch      0/1   0/1        wrong-pointer     0/1   0/1
legacy-name-only     0/0   0/1        receipt-absent    0/0   0/0
legacy-attempt-row   0/0   0/0        live repo root    0/5   0/0
```

## 5. Disposition table

| # | element | class | evidence / draft | owner | next touch |
|---|---|---|---|---|---|
| D-1 | the instrument's closure predicate (`SKILL.md:715`) | **fixed-with-evidence (draft ready, integrator applies)** | §3b after-bytes; §4 controls: live 5→0 rows, 7/7 scenarios as designed | integrator (applies) | the round-33 SKILL.md landing, then re-run `python3 -B .scratch/o05/build-controls.py` |
| D-2 | the recorded falsification clause (i) (`LOG.md:3460-3463`) | **carried — no change required once D-1 lands** | clause (i) is "audit prints a non-empty list for an admitted round ⇒ falsified"; with D-1 applied the audit prints nothing, so clause (i) is satisfied as written and its day-one fire is explained as instrumental (F-X16-3) | parent/operator | re-read at the D-1 landing; if the integrator instead chooses the reword variant (Q-32-1 option 2), it is a **new dated LOG entry**, never an edit |
| D-3 | the lesson prose key name `closes_record` (`corpus/lessons/round-32.md:41,55`) | **carried-with-owner+reason+next-touch** | live key is `closes` (§2.1); the lesson is a filed lesson file → append-only, never rewritten | parent (lessons writer) | the next lessons write (r33's own lesson) or a successor file: record that the snapshot key is `closes`, not `closes_record` |
| D-4 | `reports/round-31/run-validation.py:780` closure test keyed to the exact filename `availability-close-<round>.json` | **carried-with-owner+reason+next-touch (adjacent, routed — not absorbed)** | demonstrated below, §6 | parent/operator | the first round that files a correction-named snapshot, or the next AGENTS/SKILL wording pass |

Nothing here is `unassigned`; no row claims a promotion, canon, clearance, or closure verdict.

## 6. Adjacent exposure found while dispositioning (routed, not absorbed)

`reports/round-31/run-validation.py` keys two different tests to the snapshot name:

- `:780` — the **closure** test: `(path.parent / "telemetry" /
  f"availability-close-{path.parent.name.split('-')[1]}.json").is_file()` — name-exact.
- `:792` — the **integrity** test: `ROOT.glob("reports/round-*/telemetry/availability-close*.json")`
  — name-tolerant (a `-correction` suffix would still be checked).

Demonstrated this session with the `:780` expression verbatim against a fixture whose only
snapshot is named `availability-close-90-correction.json` (valid `closes` + matching digest):
`closed_by_snapshot = False` → the record is reported **open** despite a valid closure.
Consequence: a correction snapshot named anything other than the exact
`availability-close-<N>.json` is invisible to that leg. This is the *same defect class* as
F-X16-3 in a different instrument, but it is **not** part of claim O's routed item and this
seat does not absorb it: the file is a filed round artifact (never edited), today's five
snapshots all carry the exact name, and the leg's own receipt is filed green. Recorded so the
parent/operator can decide whether the convention (not the filed file) needs a successor note.

## What this does not claim

No promotion, canon, clearance, or closure verdict — operator-owned. No filed byte edited by
this seat: `SKILL.md`, `AGENTS.md`, `LOG.md`, `SCORECARD.md`, `corpus/lessons/**`,
`reports/round-1..32/**` and `tools/**` are untouched by O05 (`git status --porcelain` over
those roots shows no O05 row). The §3b draft is a draft; only the integrator lands it. The
control fixtures live in `.scratch/o05/` (gitignored scratch) and are rebuildable from §4c.

## Owed

- `reports/round-33/op/P01-plan.md` — **absent at this seat's read** (2026-10-19; `ls
  reports/round-33/op/` listed only K01's and this seat's file among op/ dependencies). P01's
  execution criteria for the falsifier leg were therefore taken from claim O's
  `after_required.b_falsifier` (`reports/round-33/claims.json`) and K01's §5 disposition
  inputs, both of which this fragment satisfies: "either the mismatch is located and a bounded
  fix draft + control lands (integrator-applied; no filed-byte rewrites), or it is carried with
  owner + reason". The integrator should re-read P01 when it lands and fold in any criterion
  this fragment does not already meet.

## Citations

- `SCORECARD.md:443-445`; `LOG.md:3460-3468` (clause i–iii), `:3512-3514` (regimen-2 standing inputs)
- `corpus/lessons/round-32.md:36`, `:41` (F-X16-3), `:55` (Q-32-1); sha256 `8aacfc2bd9f55ec9dae3a721dc793a83bf071e90b98955ffa2cb45a33437ab64`
- `SKILL.md:522` (Checklist heading), `:534` (section end), `:660` (D3 heading), `:713-715` (item + one-liner, line 715 = 418 chars); sha256 `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`; before-block sha256 `541bad77bb78f9f18c94aa492febe5ab54e44a74b4ab5c6dd27bde56b0409f41`; `wc -l SKILL.md` = 715
- `reports/round-31/jinii/draft.md:40-45` (§2.2 draft audit, no closure test), `:59-75` (snapshot shape, key `closes`), `:92-121` (falsification conditions)
- `reports/round-31/run-validation.py:780` (name-exact closure test), `:792-812` (`closing_snapshots`, reads `closes` at `:799`); sha256 `9e01c4274c1afc0be983ba3c7610fc44212ab2d3e934f747b57ef6b9584488dc`
- `reports/round-32/run-validation.py:223` (substring allowlist for `/telemetry/availability-close-` — name-tolerant, unaffected)
- `reports/round-19/telemetry/availability-close-19.json:2-6` (`schema`, `round`, `date`, `closes` at `:5`, `closes_sha256` at `:6`); same shape rounds 25–28
- `reports/round-33/op/K01-falsifier-scout.md:41-49`, `:82-91` (agrees; key-name nuance); sha256 `9d9dbe83b8b5ca38299cd273786f8c0d4cdb78312edc97ccf6629ba4bf5a7968`
- `reports/round-33/claims.json` — claim O `after_required.b_falsifier`, `counting_commands`
- Commands (2026-10-19, lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`; verbatim `SKILL.md:715` one-liner → 5 rows, exit 0; per-record `sha256sum` vs `closes_sha256` → 5/5 equal; `grep -l closes_record reports/round-*/telemetry/*.json` → 0 files; `grep -rn "closing-snapshot.json" .` → only `SKILL.md:715` + quotations of it; `python3 -B .scratch/o05/build-controls.py` → table §4 (OLD 5 rows live / NEW 0 rows live); `git status --porcelain=v1 -uall -- reports/round-33` → round-33 files only
