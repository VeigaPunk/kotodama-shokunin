- Seat: O11 | verifier | O | date 2026-10-19 | baseline 4a7aede

# O11 — second independent isolated-copy verification (claim O, R34-N1 hardening)

Mission (`reports/round-35/targets.json` seat O11): *"Second independent
isolated-copy verification: rebuild the git-archive yourself, apply O01's patch,
run the r6-row replay + r7 default chain + selftest; file defects."*

## 0. What is verified, what is owed

| mission leg | state |
|---|---|
| rebuild the `git archive` myself | **done** — own copy at `.scratch/o11/iso/repo` |
| run the r6-row replay | **done, pre-patch** — reproduced the R34-N1 crash independently (§1 B1) |
| run the r7 default chain | **done, pre-patch** — exit 0, packet `45f57132…` (§1 B2) |
| run the selftest | **done, pre-patch** — v1 17 controls, v3 39 controls (§1 B3/B4) |
| apply O01's patch and re-run the three legs | **done** — O01's draft landed after my first pass; applied in my own archive, results in §7 (catch-site fix verified; two deliberate trades left for the integrator) |
| file defects | **done** — five findings, §5, plus the two post-patch findings in §7 |

Dependency note: at my first pass `reports/round-35/op/O01-patch-draft.md` was
**absent** (probed 05:19 / 05:24 / 05:31; only `O02-controls.md O04-regressions.md
O08-validation-legs.md O10-scribe.md` present), so I built the calibrated harness
(§6) against the pre-patch state. The fragment landed during my run; I applied it
and re-ran the harness (§7), so no part of the mission is left owed.

Write discipline: nothing outside `reports/round-35/op/O11-verify-2.md` was
written durably; every command ran in `.scratch/o11/` or an isolated
`git archive` copy under it. No `reports/round-*/run-validation.py` was executed
anywhere (F-C13-1); no `--freeze` was run; `git status --porcelain` at the end of
every batch showed only `?? reports/round-35/`.

## 1. Independent rebuild and pre-patch measurements

```
$ git rev-parse HEAD
4a7aede22cd8395b01ce6dd9f46bcae364ca24e4
$ git archive 4a7aede | tar -x -C .scratch/o11/iso/repo      # 13 top-level entries
```

| # | command (in `.scratch/o11/iso/repo`) | observed |
|---|---|---|
| B1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | **exit 1**, raw traceback, `KeyError: 'reports/round-20/handoff/claims-map.md'` raised at `tools/exercise-handoff-e2e.py:3822`; no diagnostic line, no receipt |
| B2 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | **exit 0**; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| B3 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | **exit 0** in 39.1 s; header `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 39 controls:`; `grep -c '^  - '` = **40** |
| B4 | `python3 -B tools/exercise-handoff-e2e.py --selftest` (no `--profile`) | **exit 0**; header `… plus 17 controls:`; `grep -c '^  - '` = **18** — the **v1** matrix |

B2's packet digest equals the digest filed in `reports/round-34/handoff/repin.json`
(`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, R34-D-default-pointer
control) — the rebuild reproduces the filed pin byte-for-byte.

The renderer digest is unchanged from the filed repin row: `sha256sum
tools/exercise-handoff-e2e.py` = `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9`
== `repin.json` `surface_sha256_after` — independent confirmation that the pinned
surface is still the pinned bytes, and that no seat has edited the tool in-tree.

## 2. The mechanism, exactly

`tools/exercise-handoff-e2e.py:3817-3822`:

```
3817        drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]
3818        if drifted:
3819            for rel in drifted:
3820                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
3821            raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
```

The drift *detection* at `:3817` is deliberately tolerant (`assembly.digests.get(rel)`,
so an unknown member reads as `None != digest` and lands in `drifted`); the
diagnostic *formatter* at `:3820` then uses the plain index `assembly.digests[rel]`
and raises `KeyError` for exactly that member. The refusal is right; the mechanism
is an unhandled exception raised **while building the refusal's own message** —
so the member path never reaches the operator, and the designed `E2E-DIGEST`
message (with the "first three" naming convention) is never printed.

Two consequences the patch must respect:

- the fix belongs at the *classification* point (before `drifted` is computed), not
  as a bare `try/except KeyError` around `:3820` — a catch-all would keep the member
  unnamed unless the message is rebuilt by hand;
- whatever fires must be visible on the **`--quiet`** path, because the claim's own
  counting command is `--quiet` (`reports/round-35/claims.json:48`) and `main:4603`
  gates the `handoff-v3: {code}: {detail}` print on `not args.quiet`.

## 3. The superseded-row predicate, measured

Loaded both filed baselines in the isolated copy and diffed their `inputs` against
the live `V3_READ_SET` (`tools/exercise-handoff-e2e.py:1935`):

| baseline row | `inputs` keys | live read set | baseline member ∉ live read set | live member ∉ baseline |
|---|---|---|---|---|
| `reports/round-30/handoff/declared-in-r6/expected.json` (`ea1e2927…`) | 58 | 58 | **1** — `reports/round-20/handoff/claims-map.md` | 1 — `reports/round-34/handoff/declared-in-r7/claims-map.md` |
| `reports/round-34/handoff/declared-in-r7/expected.json` (`bbe15887…`) | 58 | 58 | 0 | 0 |

So the predicate is one line of set arithmetic on `baseline["inputs"]` vs
`V3_READ_SET`, and the r6 row isolates cleanly: **exactly one** unresolvable member
and **zero** resolvable-but-drifted members, so a superseded-row control cannot be
confused with the digest leg. (This independently reproduces the counts in
`reports/round-35/op/O02-controls.md` §1 — two seats, separate archives, same
numbers.)

The member itself **exists and is readable** at the baseline:
`ls -la reports/round-20/handoff/claims-map.md` → 24 888 bytes, mtime 2026-10-18 10:11.
That is decisive for the code choice: the renderer's documented `E2E-ARTIFACT`
means *"missing/unreadable read-set file"* (`tools/exercise-handoff-e2e.py:91-92`),
and this file is neither. The condition is a **baseline whose read set no longer
matches the profile's read set** — a superseded row.

## 4. Preserved controls, reproduced from the CLI (not from the selftest summary)

Each in a throwaway archive copy; the filed bytes were never edited.

| # | control | observed |
|---|---|---|
| C-a | flip the first hex digit of `packet_sha256` in a copy of the r7 baseline, no re-sign | **exit 2**, `E2E-BASELINE`, `baseline integrity digest mismatch — the baseline file was edited without re-freezing` |
| C-b | append `\n` to `reports/round-19/validation.json` (a read-set member the assembler does **not** re-measure) | **exit 1**, `E2E-DIGEST`; `FAIL input-digest: reports/round-19/validation.json: frozen 7dbc346ccab1… live e5ac9806abe2…` + `1 read-set file(s) changed since the baseline was frozen` — this is the leg *adjacent to the patch site*, the nearest-neighbour regression |
| C-c | append `\n` to `examples/culture-d2/components/05-lexicon.yml` | **exit 1**, `E2E-DIGEST` via the assembler leg: `D2 component …: the assembler recorded 9bdcb8d895be… but the bytes measure 5639c6089bc7…` |
| C-d | v3 selftest control lines (`--profile v3 --selftest`) | `  - preservation: the 58 read-set files are byte-identical before and after a run`; `  - m12a tamper baseline: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass`; `  - m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file` |

C-b and C-c matter because they are the two ways the digest leg can still fire once
a superseded-row guard is inserted: the guard must not shadow either.

## 5. Findings

**V-O11-1 (claim-level evidence defect — the declared selftest command cannot see
the new controls).** `reports/round-35/claims.json:47` declares
`python3 -B tools/exercise-handoff-e2e.py --selftest` as the counting command for
claim O's "selftest N/N" threshold, and `reports/round-35/targets.json` repeats the
claim. That command runs the **v1** matrix (measured: `plus 17 controls:`, 18 result
lines, §1 B4); the two new controls land in `v3_selftest`
(`tools/exercise-handoff-e2e.py:4154`), reachable only via `--profile v3 --selftest`
(39 controls, 40 result lines, §1 B3). **A round that ran the declared command
verbatim would report "selftest green" while the new controls were absent.** The
acceptance leg must be `--profile v3 --selftest` with N ≥ 41 (claim floor: 39 + 2),
and the fragment/report should record the corrected command. `op/O02-controls.md`
§6 already uses the corrected form; the defect is in the declared command, not in
O02's design. My harness leg 3 runs the v3 form (§6).

**V-O11-2 (exit-code class is a live decision, and the two authorities disagree).**
`claims.json:48` declares `(expect: exit 1, named diagnostic)`; `op/O08-validation-legs.md`
§2 O1 requires exit ∈ {1,2} and argues exit 2 (`could-not-evaluate`) is the
convention-correct class for an unusable baseline, mirroring `E2E-BASELINE`.
Both readings are defensible and I am **not** resolving it: the round contract binds
`after_required` ("exits non-zero with a named diagnostic"), which both satisfy, but
only exit 1 satisfies the literal counting command. What is *not* defensible is
`E2E-ARTIFACT` (see §3: the member is readable) or an unnamed non-zero exit. If the
integrator lands exit 2, `claims.json:48`'s expectation must be recorded as a named
deviation in the round record rather than silently dropped.

**V-O11-3 (false-pass shapes the acceptance leg must refuse).** (a) a non-zero exit
alone — the **unpatched** tree already exits 1, so "exit != 0" passes with the
defect present (my harness shows this explicitly: `leg1 r6 replay: exit 1
(non-zero)` PASSes on the no-op patch while the traceback leg FAILs); (b) a
`try/except KeyError` that prints a message without the member path; (c) a fix
that widens `V3_READ_SET` or moves `CLAIMS_MAP` back, which would make the r6 row
replay "successfully" and destroy the superseded-row control; (d) a fix visible
only on the non-quiet path (V-O11-1/§2). The leg must assert *no traceback + named
code + the member path in the same line, on the `--quiet` command*.

**V-O11-4 (freeze-byte pins verified, not assumed).** All seven pinned files and
the 250-file `tools/gates/frozen` tree digest were measured before any patch (§8).
The r7 `packet.md`/`claims-map.md`/`expected.json` digests equal the values filed in
`reports/round-34/handoff/repin.json` (R34-D-new-row), and the r6
`expected.json` equals the filed `surface_sha256` — an independent re-verification
of the round-34 pin set at 4a7aede.

**V-O11-5 (harness self-defect, fixed and disclosed).** My first revision's leg-3
regex required `E2E-DIGEST` *before* `exit 1` on one line, which the filed control
line (`m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST …`) does not satisfy —
a false negative. Fixed to accept either order; the delivered revision
(`sha256 3a33242bcc111e660babaa4522b4a5a0504e57e9523fe347c5e0bc8a4abe7726`, the
bytes embedded in §6) passes that line pre-patch. The §6 calibration runs used
`bdf45e5c7654fdc582a7cdaf5b457256aac26917987fb50075a28fc4303aa2c1`; the two
revisions differ only in two comment lines (byte-diff verified, executable code
identical). Disclosed because an
un-calibrated verifier harness is itself an unverified claim.

## 6. The apply-ready harness (calibrated in both directions)

Written to `.scratch/o11/verify-patch.sh`; it takes either a patch file or O01's
fragment (extracting the largest ```` ```diff ````/```` ```patch ```` fenced block),
rebuilds a fresh `git archive 4a7aede` copy, applies the patch with `git apply -p1`,
and runs 19 assertions. It never writes in-tree and never runs a filed validator.

Calibration evidence (final revision):

| patch applied to the archive | result |
|---|---|
| no-op patch (two comment lines appended — no fix) | **10 passed, 8 failed**: all four leg-1 assertions and the leg-1b code+path assertion FAIL, leg 3 control legs FAIL; legs 2/4a/4b/5 PASS |
| O11 probe fix (guard before `drifted` + quiet-path print hoist + docstring census; **no** new controls) | **16 passed, 3 failed** — the only failures are the three control-matrix legs (39 controls < 41, 40 lines < 42, no superseded-row control line); the WARN records O02's predicted 43 |
| **O01's landed draft** (block 0, then both blocks) | **16 passed, 3 failed** in both states — the real patch, §7 |

The extraction path was exercised on a synthetic fragment (`.scratch/o11/fake-O01.md`):
`extracted 1 fenced block(s); using the largest (817 bytes)` → patch applied → legs ran;
on the real fragment it extracted `2 fenced block(s); using the largest (3937 bytes)`,
which is why §7 also reports the both-blocks run.

```bash
#!/usr/bin/env bash
# O11 independent verification harness (round 35, claim O).
# Usage: bash .scratch/o11/verify-patch.sh <patch-file | O01-fragment.md> [tag]
# Rebuilds a fresh git archive of the baseline commit, applies the patch, and
# runs the legs with exact expected codes. Never touches the repo tree and never
# executes any reports/round-*/run-validation.py.
set -u
REPO=/home/vgpnk/Projects/shokunin/kotodama-shokunin
BASE=4a7aede
SRC=$(readlink -f "${1:?patch file or O01 fragment path}")
TAG=${2:-run}
WORK=$REPO/.scratch/o11/harness-$TAG
LOGS=$WORK/logs
export TMPDIR=$REPO/.scratch PYTHONDONTWRITEBYTECODE=1
PASS=0; FAIL=0
ok(){ echo "  PASS  $1"; PASS=$((PASS+1)); }
no(){ echo "  FAIL  $1"; FAIL=$((FAIL+1)); }

rm -rf "$WORK"; mkdir -p "$WORK/repo" "$LOGS"
git -C "$REPO" archive "$BASE" | tar -x -C "$WORK/repo" || { echo "archive failed"; exit 9; }

# --- extract the patch ------------------------------------------------------
if [[ "$SRC" == *.md ]]; then
  PATCH=$WORK/extracted.patch
  python3 - "$SRC" "$PATCH" <<'PY'
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
blocks = re.findall(r"^```(?:diff|patch)\n(.*?)^```", text, re.S | re.M)
if not blocks:
    sys.exit("no ```diff / ```patch fenced block found in %s" % sys.argv[1])
open(sys.argv[2], "w", encoding="utf-8").write(max(blocks, key=len))
print("extracted %d fenced block(s); using the largest (%d bytes)" % (len(blocks), len(max(blocks, key=len))))
PY
  [[ $? -eq 0 ]] || { echo "patch extraction failed"; exit 9; }
else
  PATCH=$SRC
fi

cd "$WORK/repo"
git apply --stat "$PATCH" 2>&1 | tail -5
git apply -p1 "$PATCH" || { echo "PATCH DID NOT APPLY"; exit 9; }
echo "patch applied; renderer sha256 = $(sha256sum tools/exercise-handoff-e2e.py | cut -c1-16)…"

# --- leg 1: r6 superseded row — named diagnostic, non-zero, no traceback -----
python3 -B tools/exercise-handoff-e2e.py --profile v3 --json \
  --baseline reports/round-30/handoff/declared-in-r6/expected.json \
  > "$LOGS/r6-replay.json" 2> "$LOGS/r6-replay.err"; R6=$?
if grep -q "Traceback" "$LOGS/r6-replay.err" "$LOGS/r6-replay.json"; then
  no "leg1 r6 replay: traceback still present"
else ok "leg1 r6 replay: no traceback"; fi
if [[ $R6 -ne 0 ]]; then ok "leg1 r6 replay: exit $R6 (non-zero)"; else no "leg1 r6 replay: exit 0"; fi
CODE=$(python3 -B - "$LOGS/r6-replay.json" <<'PY'
import json, sys
text = open(sys.argv[1], encoding="utf-8").read()
start = text.find("\n{")
if start == -1:
    start = text.find("{")
print(json.loads(text[start:]).get("code") or "" if start != -1 else "")
PY
)
[[ "$CODE" =~ ^E2E-[A-Z]+$ ]] && ok "leg1 r6 replay: named code $CODE" || no "leg1 r6 replay: code='$CODE' (not E2E-*)"
grep -q "reports/round-20/handoff/claims-map.md" "$LOGS/r6-replay.json" \
  && ok "leg1 r6 replay: diagnostic names the unresolvable member" \
  || no "leg1 r6 replay: diagnostic does NOT name reports/round-20/handoff/claims-map.md"

# --- leg 1b: the claim's literal counting command (--quiet) -----------------
# claims.json:48 runs this exact command; a diagnostic printed only on the
# non-quiet path would leave the claim's own evidence command showing nothing.
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet \
  --baseline reports/round-30/handoff/declared-in-r6/expected.json > "$LOGS/r6-quiet.log" 2>&1; RQ=$?
[[ $RQ -ne 0 ]] && ok "leg1b --quiet replay: exit $RQ (non-zero)" || no "leg1b --quiet replay: exit 0"
grep -qE "E2E-[A-Z]+.*reports/round-20/handoff/claims-map\.md" "$LOGS/r6-quiet.log" \
  && ok "leg1b --quiet replay: one line carries the code and the member path" \
  || no "leg1b --quiet replay: no line carries code+path on the --quiet path (main:4603 gates the print)"
grep -q "Traceback" "$LOGS/r6-quiet.log" && no "leg1b --quiet replay: traceback present" || ok "leg1b --quiet replay: no traceback"

# --- leg 2: r7 default chain unchanged -------------------------------------
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet > "$LOGS/r7-default.log" 2>&1; R7=$?
[[ $R7 -eq 0 ]] && ok "leg2 r7 default: exit 0" || no "leg2 r7 default: exit $R7"
grep -q "packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19" "$LOGS/r7-default.log" \
  && ok "leg2 r7 default: packet digest still 45f57132…" \
  || no "leg2 r7 default: packet digest moved: $(tail -1 "$LOGS/r7-default.log")"

# --- leg 3: v3 selftest, including the two new controls --------------------
# NB: bare `--selftest` runs the v1 matrix (17 controls); the new v3 controls
# live behind `--profile v3 --selftest` (39 controls pre-patch). See V-O11-1.
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest > "$LOGS/selftest-v3.log" 2>&1; ST=$?
[[ $ST -eq 0 ]] && ok "leg3 v3 selftest: exit 0" || no "leg3 v3 selftest: exit $ST"
N=$(grep -o "plus [0-9]* controls" "$LOGS/selftest-v3.log" | grep -o "[0-9]*")
[[ ${N:-0} -ge 41 ]] && ok "leg3 v3 selftest: $N controls (>=41 = 39 baseline + 2 new)" \
  || no "leg3 v3 selftest: only ${N:-0} controls (expected >=41; pre-patch 39)"
[[ ${N:-0} -lt 43 ]] && echo "  WARN  leg3 v3 selftest: $N controls; O02's design (op/O02-controls.md §6) predicts 43 (m13a/m13b/m14a/m14b)"
LINES=$(grep -c '^  - ' "$LOGS/selftest-v3.log")
[[ ${LINES:-0} -ge 42 ]] && ok "leg3 v3 selftest: $LINES result lines (>=42 = N+1)" \
  || no "leg3 v3 selftest: only ${LINES:-0} result lines (expected >=42)"
grep -qE "^  - .*E2E-READSET.*(superseded|declared-in-r6|round-30|unresolvable)" "$LOGS/selftest-v3.log" \
  && ok "leg3 v3 selftest: a new control names the superseded-row refusal" \
  || no "leg3 v3 selftest: no control line names the superseded-row refusal"
grep -qE "^  - .*(E2E-DIGEST.*exit 1|exit 1 E2E-DIGEST)" "$LOGS/selftest-v3.log" \
  && ok "leg3 v3 selftest: the preserved E2E-DIGEST control still present" \
  || no "leg3 v3 selftest: the E2E-DIGEST control line is gone"

# --- leg 3b: exit-code expectation declared in claims.json:48 ---------------
if [[ "$CODE" != "E2E-READSET" ]]; then
  echo "  WARN  leg3b r6 diagnostic code is $CODE (claims.json:45 allows any named code)"
fi
if [[ $R6 -ne 1 ]]; then
  echo "  WARN  leg3b r6 replay exits $R6; reports/round-35/claims.json:48 declares '(expect: exit 1, named diagnostic)' — record as a named deviation if the landed class is deliberately exit 2"
fi

# --- leg 3c: a new code must enter the documented exit-code table ----------
if [[ "$CODE" == "E2E-READSET" ]]; then
  sed -n '60,96p' tools/exercise-handoff-e2e.py | grep -q "E2E-READSET" \
    && ok "leg3c docstring exit-code table documents E2E-READSET" \
    || no "leg3c docstring exit-code table (tools/exercise-handoff-e2e.py:60-96) does not name E2E-READSET"
fi

# --- leg 4: preserved negative controls ------------------------------------
mkdir -p "$WORK/neg" && git -C "$REPO" archive "$BASE" | tar -x -C "$WORK/neg"
python3 -B - "$REPO/reports/round-34/handoff/declared-in-r7/expected.json" "$WORK/neg-flip.json" <<'PY'
import json, sys
b = json.load(open(sys.argv[1]))
p = b["packet_sha256"]; b["packet_sha256"] = ("0" if p[0] != "0" else "1") + p[1:]
json.dump(b, open(sys.argv[2], "w"), indent=1, sort_keys=True, ensure_ascii=False)
PY
( cd "$WORK/neg" && python3 -B tools/exercise-handoff-e2e.py --profile v3 --json --baseline "$WORK/neg-flip.json" > "$LOGS/neg-flip.json" 2>&1 ); F=$?
[[ $F -eq 2 ]] && grep -q '"E2E-BASELINE"' "$LOGS/neg-flip.json" \
  && ok "leg4a flipped-sha expectation: exit 2 E2E-BASELINE" \
  || no "leg4a flipped-sha expectation: exit $F / $(grep -o '"code": "[A-Z0-9-]*"' "$LOGS/neg-flip.json" | head -1)"
printf '\n' >> "$WORK/neg/reports/round-19/validation.json"
( cd "$WORK/neg" && python3 -B tools/exercise-handoff-e2e.py --profile v3 --json > "$LOGS/neg-drift.json" 2>&1 ); D=$?
[[ $D -eq 1 ]] && grep -q '"E2E-DIGEST"' "$LOGS/neg-drift.json" && grep -q "reports/round-19/validation.json" "$LOGS/neg-drift.json" \
  && ok "leg4b tampered read-set member (drift leg): exit 1 E2E-DIGEST naming the file" \
  || no "leg4b tampered read-set member: exit $D / $(head -1 "$LOGS/neg-drift.json")"

# --- leg 5: no frozen bytes moved ------------------------------------------
cat > "$LOGS/pins.expected" <<'EOF'
d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c  reports/round-34/handoff/declared-in-r7/claims-map.md
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
ffae4ecdcf2558693e9ace21e918572e84d6be6607a5b8a5284805ab7e11136c  reports/round-34/handoff/declared-in-r7/run.log
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0  reports/round-30/handoff/declared-in-r6/expected.json
EOF
( cd "$REPO" && sha256sum reports/round-34/handoff/declared-in-r7/* reports/round-30/handoff/declared-in-r6/expected.json ) > "$LOGS/pins.after"
diff -q "$LOGS/pins.after" "$LOGS/pins.expected" >/dev/null 2>&1 \
  && ok "leg5 declared-in-r7 / r6 expected.json pins unchanged (7 files)" \
  || no "leg5 pin set differs from the 4a7aede capture: $(diff "$LOGS/pins.expected" "$LOGS/pins.after" | head -3)"
GT=$(cd "$REPO" && find tools/gates/frozen -type f | sort | xargs sha256sum | sha256sum | cut -d' ' -f1)
[[ "$GT" == "3b463bb3cffe22c2aaf59da558a34003a045706701ec614b929d8325416a9bfc" ]] \
  && ok "leg5 frozen-gates tree digest unchanged" || no "leg5 frozen-gates tree digest moved: $GT"

echo "harness[$TAG]: $PASS passed, $FAIL failed; logs under $LOGS"
[[ $FAIL -eq 0 ]] || exit 1
```

Integrator use: `bash .scratch/o11/verify-patch.sh reports/round-35/op/O01-patch-draft.md post`
after applying the patch in-tree (the harness needs no in-tree application — it
applies to its own archive copy, so it can also be run **before** the in-tree apply
as a pre-flight). Expect exit 0 with 19 passed once the patch includes both the
catch-site guard and the two control legs; 3 failures (all in leg 3) mean the
catch-site fix landed but the control matrix did not. That prediction was borne out
on the real fragment — see §7.

## 7. Post-patch verification against O01's landed draft

`reports/round-35/op/O01-patch-draft.md` landed during my run and carries **two**
`diff` fenced blocks: block 0 (3 937 B) — the v3 catch site, the docstring census and
one new control (m12c); block 1 (1 054 B) — the **optional** v1 latent-exposure fix.
My extractor takes the largest block only, so I ran both states:

| patch applied to my archive | result |
|---|---|
| block 0 alone | **16 passed, 3 failed** (renderer `8427618935917732…`) |
| both blocks (4 991 B) | **identical** — 16 passed, 3 failed (renderer `16015c91ac1decc9…`); the v1 hunk changes no v3 leg |

Observed on both states:

| leg | observed |
|---|---|
| leg 1 r6 replay (`--json`) | **exit 1, `E2E-READSET`, no traceback**, diagnostic names `reports/round-20/handoff/claims-map.md` — R34-N1 closed in a second, independent archive |
| leg 2 r7 default | exit 0, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` unchanged |
| leg 3 v3 selftest | exit 0, **40 controls** (39 + m12c), 41 result lines; the new control line names the superseded row; m12b `E2E-DIGEST` line still present |
| leg 3c docstring census | `E2E-READSET` is documented in the exit-code table |
| leg 4a / 4b | exit 2 `E2E-BASELINE` / exit 1 `E2E-DIGEST` naming the file — both negatives preserved |
| leg 5 | 7 file pins + the 250-file frozen-gates tree digest unchanged |
| v1 path (extra) | pristine and patched both `handoff-e2e: exit=1 …` (pre-existing red, `E2E-DIGEST: 1 read-set file(s) changed … tools/d2-typed-labels.py`) and both `--selftest` 18 bullets — block 1 is behaviour-neutral here |

**O11-P1 — the diagnostic is invisible on the claim's literal command (deliberate
trade, decision owed).** With O01's patch applied, the claim's counting command
(`reports/round-35/claims.json:48`, the `--quiet` form) prints exactly:

```
handoff-v3: exit=1 fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal alias_leg=? packet_sha256=(not assembled)
```

— `exit=1` but no `E2E-READSET` and no member path; the name appears only on the
non-quiet form (`tools/exercise-handoff-e2e.py:4603-4604`) and in `--json`. This is
O01's stated non-change (`op/O01-patch-draft.md:40-46`: the quiet summary line stays
byte-identical so filed control readings remain reproducible), against O02's designed
one-line hoist (`if err and not args.quiet:` → `if err:`, `op/O02-controls.md` §2
point 5). The round contract says report the trade, never average it:

- **adopt the hoist** → the declared command shows the diagnostic; the failing
  `--quiet` stdout shape changes (O02's consumer survey found no parser of a
  *failing* quiet stdout; only successful quiet stdout is parsed, for
  `packet_sha256=…`);
- **keep O01's byte-identical line** → the round record must name the deviation and
  use the non-quiet (or `--json`) form as the evidence command, because the declared
  command cannot carry the diagnostic.

Harness leg 1b is the instrument for either decision.

**O11-P2 — control count: one new control vs the claim's two-coverages reading.**
O01 adds one control (m12c) and argues the pre-existing m12b already covers the
preserved `E2E-DIGEST` path (`op/O01-patch-draft.md:135-138`); O02's design adds four
lines (m13a/m13b/m14a/m14b) and predicts 43 controls. The claim's wording is
satisfied under either reading — the digest path *is* covered, by m12b — but the
count differs (40 vs 43), so "selftest N/N" must be written against the landed count.
My harness accepts N ≥ 41 and WARNs below 43; with O01 alone N = 40 and the count leg
fails, which is the honest signal that the control-matrix leg is incomplete as
drafted. A validator must also check the control is *new*: the m12b line exists
pre-patch, so "an `E2E-DIGEST` control line exists" passes on the unpatched tree.

Independent corroboration of O01's block 1: the v1 path carries the same latent
shape — `.get` tolerance at `tools/exercise-handoff-e2e.py:1438`, plain index at
`:1442` — and the filed v1 baseline currently trips the *resolvable* drift branch
(`tools/d2-typed-labels.py`), not the unresolvable one, which is why the exposure is
latent rather than live.

## 8. Freeze pins captured before any patch

```
d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c  reports/round-34/handoff/declared-in-r7/claims-map.md
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
ffae4ecdcf2558693e9ace21e918572e84d6be6607a5b8a5284805ab7e11136c  reports/round-34/handoff/declared-in-r7/run.log
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0  reports/round-30/handoff/declared-in-r6/expected.json
34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9  tools/exercise-handoff-e2e.py
```

`find tools/gates/frozen -type f | wc -l` = 250; sorted-`sha256sum`-of-`sha256sum` =
`3b463bb3cffe22c2aaf59da558a34003a045706701ec614b929d8325416a9bfc`.

## Owed

- **Integrator decision on O11-P1** (§7): adopt O02's `--quiet` diagnostic hoist, or
  keep O01's byte-identical quiet summary line and file the deviation with the
  non-quiet/`--json` form as the evidence command. Either way the round record should
  state which, because `claims.json:48` declares the `--quiet` form.
- **Integrator decision on O11-P2** (§7): land the control matrix at 40 (O01's
  m12c alone) or 43 (O01 + O02's m13a/m13b/m14a/m14b), and write the "selftest N/N"
  threshold against the landed count.
- **Corrected counting command** (V-O11-1): `python3 -B tools/exercise-handoff-e2e.py
  --profile v3 --selftest`, N ≥ 41 — the declared bare `--selftest` runs the v1
  matrix (17 controls) and cannot see the new controls.
- **Post-application re-run**: after the integrator applies the patch in-tree, re-run
  `bash .scratch/o11/verify-patch.sh reports/round-35/op/O01-patch-draft.md post` plus
  the same harness against the integrated bytes (O01's two blocks + the chosen
  quiet/control edits). Nothing else from my mission remains owed: the archive
  rebuild, the three legs and the defect filing are all done (§1, §7).
- V-O11-2's exit-code question is **resolved by the landed draft**: O01 chose exit 1
  `E2E-READSET`, matching `claims.json:48`; no deviation is needed on that point.

## Citations

Paths and lines read (all at `4a7aede`, verified via `git rev-parse HEAD`):

- `reports/round-35/targets.json` (seat O11 mission/out; `shared_rules`),
  `reports/round-35/claims.json:37-52` (claim O, incl. `:47` selftest command and
  `:48` "(expect: exit 1, named diagnostic)").
- `REGIMEN.md:25-58` (per-round contract, admission rule).
- `tools/exercise-handoff-e2e.py:90-93` (exit-code census),
  `:184` (`CLAIMS_MAP`), `:247-259` (`Unevaluatable`/`ArtifactError`/`BaselineError`),
  `:1432-1442` (v1 drift leg), `:1935` (`V3_READ_SET`), `:3768-3797`
  (`v3_baseline_digest` / `v3_load_baseline`), `:3807`, `:3817-3822` (the defect),
  `:4154` (`v3_selftest`), `:4430` (m12b anchor), `:4603` (quiet-gated diagnostic
  print), `:4485-4505` (CLI: `--profile` default `v1`, `--selftest` dispatch).
- `reports/round-34/handoff/repin.json:7-14,15-22,23-31,49-51` (R34-D rows and
  R34-N1/N2).
- `reports/round-30/handoff/declared-in-r6/expected.json`,
  `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt,claims-map.md}`.
- `reports/round-20/handoff/claims-map.md` (`ls -la`: 24 888 bytes — exists/readable).
- `reports/round-35/op/O02-controls.md` §1, §2, §3, §4, §5, §6;
  `reports/round-35/op/O08-validation-legs.md` §1, §2 O1/O2;
  `reports/round-35/op/O04-regressions.md` §0-§1.

Commands run (all from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; logs under
`.scratch/o11/logs/` and `.scratch/o11/harness-*/logs/`):

```
git rev-parse HEAD
git archive 4a7aede | tar -x -C .scratch/o11/iso/repo
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
python3 -B tools/exercise-handoff-e2e.py --selftest
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest
python3 -B tools/exercise-handoff-e2e.py --profile v3 --json --baseline .scratch/o11/controls/flip-sha-expected.json
python3 -B -c "<V3_READ_SET vs baseline inputs set-difference probe>"     # §3
sha256sum reports/round-34/handoff/declared-in-r7/* reports/round-30/handoff/declared-in-r6/expected.json tools/exercise-handoff-e2e.py
find tools/gates/frozen -type f | sort | xargs sha256sum | sha256sum
bash .scratch/o11/verify-patch.sh .scratch/o11/noop.patch V-noop          # 10 passed, 8 failed
bash .scratch/o11/verify-patch.sh .scratch/o11/calib2.patch V-calib2      # 16 passed, 3 failed
bash .scratch/o11/verify-patch.sh reports/round-35/op/O01-patch-draft.md O01-real   # 16 passed, 3 failed (§7)
bash .scratch/o11/verify-patch.sh .scratch/o11/o01-both.patch O01-both    # identical, both blocks (§7)
python3 -B tools/exercise-handoff-e2e.py --profile v1 --quiet             # pre-existing red, both sides (§7)
git status --porcelain                                                    # ?? reports/round-35/ only
```
