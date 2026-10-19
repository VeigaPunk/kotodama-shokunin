- Seat: A11 | verifier | A | date 2026-10-19 | baseline 4a7aede

# A11 — second adjacency verifier

Mission: re-run A06's PROVINCE checks independently, plus spot-check two other
A-block slices. **A06's fragment (`reports/round-35/adj/A06-province.md`) did
not exist when §1-§3 were produced**, so those checks were re-derived from
`PROVINCE.md` and the live tree rather than read off A06's text. A06 landed
before this fragment was finalized; §6 reconciles the two runs claim-by-claim
and re-measures every checkable number in A06's fragment. `Owed: none`.

Slices chosen for spot-check (stated per mission): **A01** (r7 packet +
claims-map + repin.json) and **A02** (`receipt_guard_adoption.py` +
`adoption-inventory.json`). Both are the two highest-blast-radius r34 surfaces.

Working state: HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`; worktree clean
apart from the untracked `reports/round-35/`. After every command below,
`git status --porcelain | grep -v '^?? reports/round-35/' | wc -l` = **0**, so
no filed byte moved under me (`reports/round-1..34/**`, `corpus/lessons`,
`tools/gates/frozen` all clean).

---

## 1. PROVINCE re-verification at HEAD (A06's check, run independently)

### 1a. Owns list vs the tree — GREEN

`PROVINCE.md:9-11` owns
`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`
plus "this lane's own gates, source-check records, non-canon examples and reports".

| owns-list partition | on disk | census |
|---|---|---|
| linguistics | yes | 21 |
| myth-symbol | yes | 19 |
| culture-material | yes | 18 |
| synthesis | yes | 29 |
| verification | yes | 20 |
| civilizations | yes | 94 |
| **total** | — | **201** |

`ls -d corpus/knowledge/*/` returns exactly those six directories — **no
knowledge partition exists that the owns list does not name, and no named
partition is absent.** Census matches the round-35 `claims.json` before-count
(201) at HEAD.

The three r33/r34 surfaces A06 must place in-lane:

| surface | path | in-lane under |
|---|---|---|
| new tool | `tools/harness/receipt_guard_adoption.py` | `PROVINCE.md:11` "this lane's own gates" (lane tooling; `parents[2]` = repo root, never walks out) |
| r7 packet | `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,run.log,claims-map.md}` | `PROVINCE.md:11` "and reports" |
| repointed renderer | `tools/exercise-handoff-e2e.py` | `PROVINCE.md:11` "this lane's own gates" |

Repoint confirmed at the bytes: `CLAIMS_MAP = "reports/round-34/handoff/declared-in-r7/claims-map.md"`
(`tools/exercise-handoff-e2e.py:184`) and
`V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT` = the same `declared-in-r7`
directory (`tools/exercise-handoff-e2e.py:1933-1934`).

**Verdict: owns list accurate against the post-edit tree. GREEN.**

### 1b. Refuses list vs the tree — GREEN

`PROVINCE.md:16-20` refuses: canon claiming/recording (lore-shokunin);
real-world rights/attribution rulings on reference works; game mechanics
(game-dev-2d/3d); general source-research method (chousa); web publishing
(kake); prompt/skill craft (kotoba).

- **Sibling provinces still exist and are untouched**: `../lore-shokunin/`,
  `../chousa-shokunin/`, `../kake-shokunin/`, `../kotoba-shokunin/`,
  `../game-dev-2d-shokunin/`, `../game-dev-3d-shokunin/` all present as
  siblings. Nothing in this repo writes to them.
- **No out-of-repo path resolution in either tool**: a scan for
  `parents[3-9]` / `../../../` in `tools/harness/receipt_guard_adoption.py` and
  `tools/exercise-handoff-e2e.py` returns **none**; the deepest walk is
  `Path(__file__).resolve().parents[2]` = repo root
  (`receipt_guard_adoption.py:58`).
- **No out-of-repo path references in the r34 artifacts**: grep for
  `/home/vgpnk`, `../../`, `Projects/(lore|chousa|kake|kotoba|game-dev)` and
  `sibling/` across the r7 packet files, `repin.json`, `adoption-inventory.json`
  and both tools returns exactly **one** hit — `"root":
  "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` at
  `reports/round-34/op/adoption-inventory.json:109`, which is the tool's own
  repo-root field (in-repo), not a sibling reference.
- **No canon/clearance/promotion assertions outside negations** in the r34
  artifacts. Every hit is a refusal or negation:
  `claims-map.md:22` ("clearance or canon standing is claimed by any row" — in
  a negation), `:60` ("canon standing is not its to give"), `:162` ("no
  clearance may be inferred from this packet"), `:172` ("cannot be imported as
  canon without a lore baseline and a new reviewed handoff"),
  `repin.json:5` ("a pin is integrity, never truth and never clearance"),
  `repin.json:53` ("not canon, not lore acceptance, not round admission").
  Two flagged hits are **not** bleed: `claims-map.md:122`/`:127` use
  "canonical E0–E3 tag" in the technical sense (the packet's own era space),
  and `claims-map.md:172` is the routing clause itself.
- **Lore-owned references stay routed, not absorbed**: `D4-CL12`
  (`claims-map.md:166-172`) names `lore-shokunin` as the recipient of a design
  record with `owner: lore-shokunin, non-blocking for this envelope` — a
  routing record, no canon ruling. `D4-CL11` routes the clearance question to
  the packet's own open questions rather than deciding it.
- **PROVINCE.md itself is unchanged**: `git log --oneline -- PROVINCE.md`
  returns only `c53782a` and `a527120` — no round-33/34 edit. The
  re-verification is therefore of the *unchanged* text against the *changed*
  tree, which is exactly what §1a/§1b test.

**Verdict: refuses list accurate; zero unfiled cross-domain bleed on the
r33/r34 surfaces. GREEN.**

---

## 2. Spot-check slice A01 — r7 packet + claims-map + repin.json

### 2a. Verbatim carry claims-map → packet: **12/12 rows, field-identical**

Independent extraction (regex on `### D4-CLxx` sections in `claims-map.md` vs
the `| D4-CLxx |` table rows in `packet.md`), then whitespace-normalized
comparison of `statement` / `u.basis` / `links`:

```
claims-map sections: 12 packet rows: 12
whitespace-normalized verbatim carry: 12/12 rows identical across statement/u.basis/links
```

**Caveat for whoever re-runs this:** a naive byte-equality check reports
**0/12**. The claims-map wraps statement lines at ~80 columns and separates
links with `, `, while the packet carries each row on one line and separates
links with `; `. Normalizing whitespace and the link separator is required; the
*content* is identical in all 12 rows. This is a formatting difference, not a
carry defect — filed here as an observation (A11-N2) so a later verifier does
not false-fire on it.

### 2b. Frozen digests resolve to live bytes — GREEN

`sha256sum reports/round-34/handoff/declared-in-r7/*`:

| file | live sha256 | declared |
|---|---|---|
| `packet.md` | `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | `freeze.txt:packet_sha256` = same; `expected.json.packet_sha256` = same |
| `twin.json` | `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599` | `freeze.txt:twin_sha256` = same; `expected.json.twin_sha256` = same |
| `claims-map.md` | `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c` | `freeze.txt` re-frozen target `d181de28ccaf…` = same; `repin.json.rows[2].digests["claims-map.md"]` = same |
| `expected.json` | `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55` | `repin.json.rows[2].digests` = same |
| `freeze.txt` | `3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223` | `repin.json.rows[2].digests` = same |

The `freeze.txt` re-freeze chain is internally consistent: it records
`41f92ee9b3f8444b73d29a5faff09944be5e5c7f… -> 45f5713261762a959ba77b057654c8db06d140e1…`
for the packet and `0121559452f2… -> d181de28ccaf…` for the claims-map, and the
live bytes sit at the **after** values on both.

### 2c. Repin rows resolve — GREEN

`repin.json.rows[0]` (`R34-D-default-pointer`) declares
`surface_sha256_before = a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df`
and `surface_sha256_after = 34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`
for `tools/exercise-handoff-e2e.py:1933-1934`. Independently reproduced:

```
git show da68a6d:tools/exercise-handoff-e2e.py | sha256sum
  -> a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df
sha256sum tools/exercise-handoff-e2e.py
  -> 34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9
```

Both match. `rows[1]` (`R34-D-stale-row`) declares the r6 row's sha
`ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0` and its stale
pin `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`; both
reproduce from live bytes (`sha256sum reports/round-30/handoff/declared-in-r6/expected.json`;
`expected.json.packet_sha256`).

### 2d. Both repin controls reproduce exactly at HEAD

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
    --baseline reports/round-30/handoff/declared-in-r6/expected.json
Traceback (most recent call last):
  File ".../tools/exercise-handoff-e2e.py", line 4613, in <module>
    sys.exit(main())
  ...
  File ".../tools/exercise-handoff-e2e.py", line 3822, in v3_exercise
    record("input-digest", False, f"{rel}: frozen ...")
KeyError: 'reports/round-20/handoff/claims-map.md'
EXIT=1

$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
EXIT=0
```

**R34-N1 confirmed independently at HEAD**: the r6-row refusal is correct in
intent but surfaces as an unhandled `KeyError` at
`tools/exercise-handoff-e2e.py:3822`, and the mechanism string in
`repin.json.rows[1].control.mechanism` matches the observed exception exactly.
The default v3 chain exits 0 with the frozen packet digest. Claim O's hardening
target is therefore real and still open at HEAD.

### 2e. Link targets resolve — GREEN

All `links:` entries across the 12 claims-map rows expand to **15 distinct
file targets; 15 resolve, 0 missing** (anchor fragments `#…` not separately
validated — file-level resolution only).

### 2f. Preservation — GREEN

`git status --porcelain reports/` (excluding the untracked `round-35/`) = **0
lines**; `git status --porcelain tools/gates/frozen corpus/lessons` = **0
lines**. The filed r2..r6 packet rows and the round-20 map are byte-identical
to their commits, as `repin.json` claims.

**Slice A01 verdict: GREEN on every check; one non-defect observation
(A11-N2) about formatting normalization.**

---

## 3. Spot-check slice A02 — `receipt_guard_adoption.py` + inventory

### 3a. Selftest — GREEN

```
$ python3 -B tools/harness/receipt_guard_adoption.py --selftest
  "controls_passed": 38, "controls_total": 38,
  "live_runner_count": 29,
  "live_class_counts": {"guarded-refresh": 18, "unguarded-in-place": 11},
  "live_findings": ["RGA-1-round-26", "RGA-2"],
  "selftest_passed": true, "fixture_count": 11
EXIT=0
```

### 3b. Tool is safe by construction — GREEN

- **Never executes a filed runner.** The only `runpy.run_path` targets in the
  file are `tools/harness/receipt_guard.py` (the guard) — lines 877, 903, 925,
  974, 993. The `subprocess` at `:1029` is inside a **fixture string literal**
  (`"reports/round-51/run-validation.py"` synthetic fixture), not live code.
- **Fixtures live under `.scratch`**: `temporary = ... dir=scratch` where
  `scratch = ROOT / ".scratch"` (`:1082-1084`), and `.scratch` is gitignored
  (`.gitignore:6`). Fixture runner paths are `reports/round-41/…`,
  `round-47..51` — no real round number collides with a filed runner.
- **`SKIP_DIRS` includes `.scratch`** (`:63`), so the census does not read its
  own fixtures.
- **Zero worktree dirt** after my full run: `git status --porcelain tools/` = 0.

### 3c. Filed inventory vs fresh census — **FINDING A11-F1**

Running the tool fresh (`--json`, output kept at
`.scratch/a11-fresh-inventory.json`) and diffing against the filed
`reports/round-34/op/adoption-inventory.json`:

| field | filed (r34, at 4a7aede) | fresh census at HEAD |
|---|---|---|
| `runner_count` | **28** | **29** |
| `class_counts` | **{guarded-refresh: 17, unguarded-in-place: 11}** | **{guarded-refresh: 18, unguarded-in-place: 11}** |
| `hazard_count` | 11 | 11 |
| `findings` | RGA-1-r26, RGA-2 | identical |
| `protocols` / `limits` / `glob` / `mode` | — | identical |
| runner set diff | — | fresh-only: `reports/round-34/run-validation.py`; filed-only: none |

The missing row is the round's **own** runner. It is not a late arrival:
`git ls-tree 4a7aede reports/round-34/run-validation.py` returns blob
`08f0ebbbc41d22446cb7931086b3b24520f9ff4e`, i.e. it **is** in the filed commit,
and `git show 4a7aede:reports/round-34/op/adoption-inventory.json` confirms the
filed inventory lists 28 rows with `"r34 present: False"`. The freshly
classified row is `guarded-refresh` (its guard call is
`namespace['guard_receipt'](f'{ROUND}/validation.json')` at
`reports/round-34/run-validation.py:517`, resolving to
`reports/round-34/validation.json`).

`LOG.md`'s **ADMITTED** round-34 entry already states the correct figure
("29 filed runners — 18 guarded-refresh / 11 unguarded-in-place"), and the
earlier in-progress LOG entry states the stale one ("28 … 17 guarded-refresh").
So the **durable JSON is stale, not the LOG**: the census was taken before the
round's own runner landed and never refreshed.

- **Severity:** low-to-moderate. No live behaviour depends on the number, and
  the class of every *other* runner is unaffected (the 11-runner
  unguarded-in-place debt list is identical). But the artifact is the durable
  evidence for claim O's "29 filed runners", and a downstream reader who
  counts from the JSON gets 28.
- **Owner:** the round-34 integrator / a future integrate round.
- **Remedy constraint:** `reports/round-34/**` is a filed byte — it must **not**
  be edited in place. The correct fix is a new append-only snapshot row (a
  round-35 or later inventory artifact naming the stale record and its sha256),
  exactly the supersession pattern the lane already uses for `repin.json`
  rows. I did not write one: it is outside my assigned `out` path.
- **Not a bleed:** an accuracy defect in a lane-owned report, in-lane.

### 3d. Language scan on the tool and inventory — GREEN

No `canon` / `clearance` / `promotion` / `lore-shokunin` / `chousa` / `kake` /
`kotoba` / `game-dev` hits in either `receipt_guard_adoption.py` or
`adoption-inventory.json`. The tool's own `limits` field already refuses to
claim more than it measures ("no filed runner is executed and no filed byte is
written"; the r26 byte fact "disagrees with the F-C13-1 parenthetical").

**Slice A02 verdict: GREEN on safety and selftest; one finding (A11-F1) on
durable-record accuracy.**

---

## 4. Findings ledger

| id | severity | surface | finding | owner |
|---|---|---|---|---|
| **A11-F1** | low-mod | `reports/round-34/op/adoption-inventory.json` | filed census says 28 runners / 17 guarded-refresh; live census says 29 / 18. Missing row = `reports/round-34/run-validation.py`, which **is** in the filed commit (`4a7aede`, blob `08f0ebbb…`). LOG.md's admitted entry already carries 29/18. Filed bytes must not be edited — remedy is a new append-only snapshot row. | round-34 integrator / future integrate round |
| **A11-N1** | note | `PROVINCE.md` | PROVINCE.md unchanged since `c53782a`; its owns list names "this lane's own gates" but not `tools/harness/` explicitly. The new tool is in-lane under that reading; naming the harness directory would remove the ambiguity. No bleed. | integrator (optional) |
| **A11-N2** | note | `declared-in-r7/claims-map.md` vs `packet.md` | carry is content-identical 12/12 but **not** byte-identical: claims-map wraps statement lines and uses `, ` between links, the packet uses one line and `; `. A byte-equality verifier will false-fire. | future verifiers |
| **A11-N3** | note | `declared-in-r7/claims-map.md:122,127` | "canonical E0–E3 tag" is a technical usage (the packet's own era space), not a canon assertion; flagged by a naive `canon` grep. No bleed. | future verifiers |

**Zero unfiled cross-domain bleed on the r33/r34 surfaces.** Contested items
remain routed-not-absorbed (`D4-CL11` clearance question → packet open
questions; `D4-CL12` → `lore-shokunin`, owner named, non-blocking).

## 5. What this does not establish

- A06's PROVINCE text was unavailable when §1 was written, so §1 is an
  independent re-derivation rather than a comparison. §6 now reconciles the
  two; no conflict was found. If a later reader finds one, §1 stands on its own
  evidence.
- Link resolution is file-level only; `#anchor` fragments were not validated.
- The A02 slice checked ownership, safety and census accuracy — not the
  classifier's correctness on the 11 unguarded runners (that is A07's re-run
  scope and the round-34 O-block's own verified claim).

## 6. Reconciliation against A06 (landed during my run)

`reports/round-35/adj/A06-province.md` did **not** exist when §1-§3 were
produced; it landed before this fragment was finalized. A06's text was then
read and **every checkable number in it re-measured independently**:

| A06 claim | A06's value | my independent measurement | agrees |
|---|---|---|---|
| `PROVINCE.md` blob at HEAD | `313b182f251564b7997b06996b4f063370778f11` | `git rev-parse HEAD:PROVINCE.md` → same | yes |
| `PROVINCE.md` sha256 | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` | `sha256sum PROVINCE.md` → same | yes |
| `PROVINCE.md` size | 31 lines / 1636 bytes | `wc -l -c` → `31 1636` | yes |
| no r33/r34 edit | `git diff --stat c53782a HEAD -- PROVINCE.md` empty | empty (exit 0) | yes |
| adoption tool sha256 | `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544` | `sha256sum` → same | yes |
| adoption tool size | 1309 lines | `wc -l` → 1309 | yes |
| round dirs | 31 | `ls -d reports/round-* \| wc -l` → 31 | yes |
| `run.log` ignored | `.gitignore:3` `*.log` | `git check-ignore -v` → `.gitignore:3:*.log` | yes |
| tool language scan | zero `canon\|promot\|clearance\|lore-shokunin\|fleet` | 0 hits | yes |
| tool path scan | zero `/home/` or `../../` | 0 hits | yes |
| renderer canon traps | `:228`, `:229-235` | `CANON_MARKER_RE` `:228`, `CANON_TRAP_RES` `:229` | yes |
| packet read set | examples 32 / tools 12 / reports 9 / corpus 5 | same four counts | yes |
| partition census | 21/19/18/29/20/94 = 201 | same | yes |
| packet/twin/claims-map/expected digests | equal `freeze.txt` | same four digests | yes |

**No conflict.** Two notes for the integrator, neither a defect in A06's
verdicts:

- **A11-N4 (method note):** A06's read-set distribution command
  (`grep -oE '\| [A-Z]-[0-9]+ \| [^ |]+' packet.md | … | cut -d/ -f1 | sort |
  uniq -c`) is not self-contained: run verbatim it also emits rows from other
  packet tables (`D2-CL01` 22, `spine-independence` 10, `field-axis-duty` 6,
  `record-coupling` 5, `borrowed-label-to-layer` 6, `rule-anchor-coupling` 3,
  `spine-content-carrier` 1, `spine-content-carrying` 1). The four in-lane
  counts it reports are correct; a re-runner must scope the grep to the
  read-set table. The packet's read-set total is 58 rows, matching
  `freeze.txt`'s "read set: 58 files".
- **A11-N5 (citation range):** A06 cites `PROVINCE.md:16-20` for the refuses
  block; the block's last content line is 20 (`prompt/skill craft (kotoba).`)
  and line 21 is blank. A06's range is the tighter, correct one — I have
  corrected my own §1b citation from `:16-21` to `:16-20` to match. A06 reads
  owns as `:9-14` (including the `:12-14` scope limit) where I read `:9-11`;
  both point at the same owns statement and the difference is immaterial.

**Net: no owed dependency remains.** A06's fragment landed before this
fragment was finalized and the reconciliation above closes the dependency my
mission named.

## Owed: none

A06's fragment (`reports/round-35/adj/A06-province.md`) landed during this
run; §6 reconciles it claim-by-claim. No other dependency was named in the
A11 mission and none is outstanding.

## Citations

Files read or verified (all relative to repo root at HEAD `4a7aede`):

- `PROVINCE.md:9-11` (owns list), `:16-20` (refuses list), `:22` (adjacent
  contract), `:31` (out-of-province rule)
- `REGIMEN.md`; `reports/round-35/claims.json`; `reports/round-35/targets.json`
  (seat A11 object: `out` = `adj/A11-verify-2.md`)
- `tools/harness/receipt_guard_adoption.py:58` (`ROOT`), `:63` (`SKIP_DIRS`),
  `:877,903,925,974,993` (`runpy` on the guard only), `:1029` (subprocess inside
  a fixture string literal), `:1082-1084,1090` (scratch fixture root)
- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP`), `:1933-1934`
  (`V3_BASELINE_DEFAULT`, `V3_FROZEN_DIR_DEFAULT`), `:3822` (KeyError site),
  `:4578`, `:4613`
- `reports/round-34/run-validation.py:517` (guard call)
- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,run.log,claims-map.md}`
- `reports/round-34/handoff/repin.json` (`rows[0]`, `rows[1]`, `rows[2]`)
- `reports/round-34/op/adoption-inventory.json:109` (`root` field)
- `reports/round-30/handoff/declared-in-r6/expected.json`
- `LOG.md` (round-34 in-progress + ADMITTED entries)
- `SCORECARD.md`; `AGENTS.md:9,12`; `SKILL.md:3,17,112,118,120,185,233-236,254,325`
- `.gitignore:6`
- `examples/culture-d4/{brief.md,packet.d4.yml}` (NON-CANON markers)

Commands run (all read-only; no `--freeze`, no in-tree `run-validation.py`):

```
git rev-parse HEAD
git status --porcelain | grep -v '^?? reports/round-35/' | wc -l        # 0
git ls-tree 4a7aede reports/round-34/run-validation.py                  # blob 08f0ebbb…
git show 4a7aede:reports/round-34/op/adoption-inventory.json            # 28 / 17
git show da68a6d:tools/exercise-handoff-e2e.py | sha256sum              # a5e4a8c5…
sha256sum tools/exercise-handoff-e2e.py                                 # 34c85f57…
sha256sum reports/round-34/handoff/declared-in-r7/*                     # 6/6 match
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
python3 -B tools/exercise-handoff-e2e.py --selftest                     # exit 0, 17 controls
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet           # exit 0, packet 45f57132…
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
  --baseline reports/round-30/handoff/declared-in-r6/expected.json      # exit 1, KeyError
python3 -B tools/harness/receipt_guard_adoption.py --selftest           # exit 0, 38/38
python3 -B tools/harness/receipt_guard_adoption.py --json > .scratch/a11-fresh-inventory.json
grep -nE 'parents\[[3-9]\]|\.\./\.\./\.\.' tools/harness/receipt_guard_adoption.py tools/exercise-handoff-e2e.py
grep -niE 'canon|clearance|promotion|chousa|kake|kotoba|game-dev|lore-shokunin' <r33/r34 artifacts>
git log --oneline -- PROVINCE.md                                        # c53782a, a527120 only
```
