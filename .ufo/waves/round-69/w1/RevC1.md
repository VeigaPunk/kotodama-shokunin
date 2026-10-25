# RevC1 — round-69 w1 — calibration: append-only discipline + counter write-safety

Seat: RevC1 (leaf, calibration) · milestone r69-v1 · measured 2026-10-24 (host local)
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (jj-colocated; HEAD detached)
Base: 793f79746712a79f915bb481215e54bbea8b5e7a · HEAD == main == 6a98d7d042b6c58d2165773b1585069798111035
(base is the direct parent of main; base..main is exactly the one declaration commit)

## Task 1 — append-only discipline of the round-68 filed surfaces

Command (as assigned):

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --stat \
    793f79746712a79f915bb481215e54bbea8b5e7a main -- \
    corpus/lessons/round-68.md corpus/SOURCES.md reports/round-68
```

Real output: **empty** (zero bytes — no modification, no addition, no deletion on
any of the three assigned surfaces between base and main).

Cross-checks, all read-only:

```
$ git diff --name-status 793f79746712a79f915bb481215e54bbea8b5e7a main
A	.ufo/waves/round-69/assimilation/collisions
A	.ufo/waves/round-69/assimilation/quarantine-slice
A	.ufo/waves/round-69/assimilation/reg-ids
A	.ufo/waves/round-69/assimilation/staged-ids
A	reports/round-69/accept-ca.py
A	reports/round-69/accept-d.py
A	reports/round-69/accept-o.py
A	reports/round-69/claims.json
A	reports/round-69/telemetry/census-start.txt
A	reports/round-69/telemetry/controls.txt
A	reports/round-69/telemetry/declaration-dry-run.txt
A	tools/check-settlement-fixture.py
```

The only base..main changes are the declared round-69 additions themselves.
`git status --porcelain` at measure time showed only untracked
`.ufo/waves/round-69/{dispatch-v1.sh,gen-spec.py,spec-v1.json,taskcall-v1.json,w1/}` —
no tracked file modified, so the working tree matches main on every filed surface.

VERDICT (task 1): PASS — round-68 filed surfaces (corpus/lessons/round-68.md,
corpus/SOURCES.md, reports/round-68) are byte-identical between base 793f7974
and main; append-only discipline held with zero edits.

## Task 2 — do the round-69 counters write anything?

Method: (a) grep all four instruments for write/mutate calls, (b) read every hit
in context to resolve its destination, (c) behavioral proof — run the three
declared counting commands against the real lane behind a pre-run marker and
`find -newer` all production paths.

### Static analysis (files: reports/round-69/accept-{o,ca,d}.py, tools/check-settlement-fixture.py)

Every write call found and its resolved destination:

| File | Write call | Destination |
|---|---|---|
| accept-d.py:204,217,220,229,236 | `open(..., "w"/"wb")` | inside `build_fixture_root(fx)`; `fx` only ever under `tempfile.TemporaryDirectory(prefix="d69-selftest-")` (accept-d.py:241) |
| accept-o.py:147,193,198 | `open(..., "w")` | inside `tempfile.TemporaryDirectory(prefix="o69-negprobe-")` (:144) and `o69-selftest-` (:203) |
| accept-o.py:179,190 | `shutil.copy2` | copies FROM lane INTO tempdir fixture only (lane→fixture direction) |
| accept-ca.py:306,312,314,327,332,339 | `shutil.copy2` / `open(..., "w"/"a")` | fixture tree under `tempfile.TemporaryDirectory(prefix="ca69-selftest-")` (:345); the `open(lesson,"a")` append and the `claims.json` rewrite (:339) hit the FIXTURE COPIES, not the lane's LOG/lessons/claims. The fleet report read at :310 (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md`) is read-only (read + copy into fixture) |
| check-settlement-fixture.py:83,88 | `open(..., "w")` | `write_fixture(root,...)`; root only ever under `tempfile.TemporaryDirectory(prefix="settlement-fixture-")` (:112) |
| check-supersession-settlement.py:260 (pre-existing, invoked by the harness's LANE leg) | `open(p, "w")` inside `_mk` | called ONLY from `selftest()` under `tempfile.TemporaryDirectory(prefix="srs-")` (:270); the `--scan` path (:151,172,174) opens read-only |

Subprocess audit — exactly three call sites, all lane-internal tools, no git/jj:

- accept-o.py:97 `run_tool` → `[sys.executable, "-B", <root>/tools/check-settlement-fixture.py]` with `--selftest` or `--root <root>`
- accept-o.py:149 → `[sys.executable, "-B", tools/check-supersession-settlement.py, "--scan", "--root", <tempdir>]`
- check-settlement-fixture.py:94 → `[sys.executable, "-B", checker, "--scan", "--root", <fixture-or-lane>]`

`-B` on every subprocess suppresses `__pycache__` writes. No `os.remove`,
`os.rename`, `os.system`, `Popen`, tempfile-outside-TemporaryDirectory, or any
git/jj string exists in any of the four files (grepped). Each file's docstring
claim "reads only / no mutation of the lane tree" is accurate for the lane tree;
writes are confined to OS tempdirs.

### Behavioral proof

```
$ MARK=/tmp/r69c-revc1-marker && touch "$MARK"
$ python3 -B reports/round-69/accept-o.py --root .          # rc=0, ACCEPT-O-69: PASS legs=7/7
$ python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin
                                                             # rc=1, ACCEPT-CA-69: FAIL legs=2/8
$ python3 -B reports/round-69/accept-d.py --root .          # rc=1, ACCEPT-D-69: FAIL legs=1/8
$ find SKILL.md LOG.md SCORECARD.md README.md PROVINCE.md REGIMEN.md MINT.md SHONEN.md \
      corpus reports tools templates examples -type f -newer "$MARK"
(no output — zero production files created or modified)
$ git status --porcelain
?? .ufo/waves/round-69/dispatch-v1.sh
?? .ufo/waves/round-69/gen-spec.py
?? .ufo/waves/round-69/spec-v1.json
?? .ufo/waves/round-69/taskcall-v1.json
?? .ufo/waves/round-69/w1/
(identical to the pre-run listing — nothing new anywhere in the tree)
```

Calibration corroboration: the three runs reproduce the committed pre-data
receipt `reports/round-69/telemetry/declaration-dry-run.txt` (23:16:05) leg-for-leg
and hash-for-hash (o STAMP self=committed=8724f9a08911; ca 5 hits identical:
LEGCOUNT 9/10 ×3, DEADPOINTER R68-M9, OVERREACH 'improved' vs FAIL; d 1/8,
SECTION missing) — the counters are deterministic and unedited since declaration.

VERDICT (task 2): PASS — invoked as declared (`python3 -B ...`), the round-69
counters and their subprocess children write NOTHING to the lane tree; all
writes are confined to `tempfile.TemporaryDirectory` fixtures under /tmp, and
no counter invokes git or jj.

### Finding (defect class, not a violation): `__pycache__` inside reports/

```
$ ls reports/round-69/__pycache__/   # accept-d.cpython-314.pyc, 2026-10-24 23:14:06
$ git check-ignore -v reports/round-69/__pycache__/accept-d.cpython-314.pyc
.gitignore:4:__pycache__/	reports/round-69/__pycache__/accept-d.cpython-314.pyc
```

Running a script as `__main__` never writes its own .pyc, so this file (created
23:14:06, between accept-d.py's write at 23:14:27's mtime cohort and the
controls receipt at 23:15:56) proves something IMPORTED
`reports/round-69/accept-d.py` as a module WITHOUT `-B` /
`PYTHONDONTWRITEBYTECODE` during declaration. Tracked bytes are unaffected
(ignored + untracked; same pattern as the pre-existing `tools/__pycache__/`),
so this is not an append-only breach — but the clean-tree property above
depends on the declared `-B` habit. Recommendation to L1: any driver that
imports the counters (rather than exec-ing them) should set
`PYTHONDONTWRITEBYTECODE=1` or run with `-B`, so no `__pycache__` materializes
inside `reports/round-69/`. Severity: low, cosmetic; no action owed for round 69.

## Corroboration — independent re-derivation of the R68FROZEN freeze

```
$ sha256sum reports/round-68/accept-{o,ca,c}.py
f409096c9167989fb56ec2830e846c282201d37e5d6a6a1752e1697418a07fae  accept-o.py
a6d1c1c24e779817a3344b063054d3c10bc09fcf466b578f38ba8008c6fc9925  accept-ca.py
515fa492aac176b62dc776c16777d6f9cf1750bb31b802cdecaa4121ac7bbf7d  accept-c.py
$ grep -H "counter sha256 (self)" reports/round-68/telemetry/final-measures-*.txt
final-measures-o.txt:  f409096c... (MATCH)
final-measures-ca.txt: a6d1c1c2... (MATCH)
final-measures-c.txt:  515fa492... (MATCH)
```

VERDICT (freeze corroboration): PASS — all three round-68 counters are
byte-identical to the sha256 their own receipts recorded; no post-data
amendment of frozen instruments.

## Current measured state (context for the L1; not a claim verdict)

- accept-o 7/7 PASS pre-data (instrument exists; O2 data is the harness itself).
- accept-ca FAIL 2/8, `unannotated_mismatches=5` — corrections not yet landed, exactly the declared pre-data state.
- accept-d FAIL 1/8 — SKILL.md table not yet landed, exactly the declared pre-data state.
- `reports/round-69/telemetry/{controls.txt,census-start.txt,declaration-dry-run.txt}` present and read; controls receipt (23:15:56) shows SELFTEST 2/2 on all three counters (green PASS + do-nothing FAIL as required).

Not evaluated here (other seats' scope): the claims' post-data predicates
(reports/round-69/corrections-r68.md, S859 row, SKILL.md table do not exist yet);
availability telemetry quality; D2 content depth.

No external network was used; no production file was modified by this seat;
scratch lived in /tmp; the only file written is this report.
