# Falsification of claim O — round 82 w1, seat CriticClaimO

Scope: attack the frozen instrument `reports/round-82/accept-o82.py` before data.
Method: re-measure the before-state, recompute the QUEUE leg's expected values
with the counter's own parser, build five do-nothing/adversarial controls in a
scratch clone, grade each with the counter, and register every contractual
ambiguity against the reading the counter actually enforces.

No installs. Scratch: `/fast/scratch/hyaku/kotodama-r82/CriticClaimO/fx/fx.ToPY`
(removed after the run; receipts copied to
`.ufo/waves/round-82/w1/stage/CriticClaimO/receipts/`).
Fixture: `git clone --shared` of the lane at base `c285b2af…` (HEAD == base;
`reports/round-82/claims.json` exists on disk but is NOT committed at HEAD —
confirmed by `git cat-file -e HEAD:reports/round-82/claims.json` → fatal). So
the fixture freezes by committing a byte copy of the working-tree
`reports/round-82/claims.json`:

- FREEZE  = c661e5c56b49a78efc7acf06479190499e161f39 (base + claims.json)
- LANDS_A = 6ae2e23d2969f5938f03e7b5b0e4e497a0739c11 (canned single-line stub)
- LANDS_B = e9df77544f728805c5d5a80c2b1c73fb86a9d3f6 (working parser, NO DUE lines)
- LANDS_C = c9a0797e038cccdac547436b91cf69ae346131b6 (B + decoy summary line first)
- LANDS_D2= 24b0715f0bdc5fe0937b780adb79fc6ef409a287 (B ignoring --registry)
- LANDS_E = 2abb22cef24760c2ad96db8c2f5c50543e983dc0 (date-conditional canned)

Every fixture git call named `-C "$D/lane"`; `git -C "$D/lane" rev-parse
--show-toplevel` == `$D/lane` asserted before the first commit. Lane left
untouched (clone --shared is read-only on the source).

---

## 1. Before-state re-measurement

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only c285b2afb19d4b64320e18df1f55e426bf2d0b0c tools/ | grep -c recheck; echo "exit=$?"
0
exit=1
```

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -c 'RECHECK-QUEUE' c285b2afb19d4b64320e18df1f55e426bf2d0b0c -- tools/ reports/; echo "exit=$?"
exit=1
```

Both expectations hold: 0 recheck tools, 0 `RECHECK-QUEUE` occurrences at base
(grep prints nothing and exits 1 on no match).

## 2. The binding code path of the QUEUE leg

The QUEUE leg does NOT trust the tool's numbers against a stored constant; it
recomputes them with the counter's own parser over the frozen registry blob
(`git show <freeze>:corpus/SOURCES.md`) and compares all four numbers at BOTH
frozen as-of dates:

- `parse_rows` line 92-97 — row membership = `ROW_RULE` line 42
  `^\s{0,3}\|\s*S\d{3,}\s*\|`, cells stripped.
- `due_date` line 100-108 — `on-release` → None (103-104); `(\d+)d` →
  opened + NN days (105-107); else `date.fromisoformat(recheck)` (108).
- `tally` line 111-129 — due `d <= as_of` (125-126); upcoming
  `d <= as_of + window` (127-128); rows = all ROW_RULE matches (129).
- QUEUE leg line 264-297: gate on st_ok (270-271); `want = tally(reg_text, …)`
  (280); tool run over a scratch copy of the frozen blob (281); **last** line
  matching `SUMMARY` (line 43) wins (283-286); rc must be 0 (287);
  `got != want[:4]` → FAIL (291-296).

Independent recompute using the counter's own module over the base blob:

```
$ python3 - <<'EOF'   (importlib load of accept-o82.py; git show base:corpus/SOURCES.md)
frozen registry bytes: 991457
2026-11-04 (0, 18, 14, 827, 0)
2027-11-01 (813, 0, 14, 827, 0)
```

This matches claims.json's frozen "after" (`0/18/14/827` and `813/0/14/827`)
and ExecEvidence's independent tally. The QUEUE leg's `want` binds these
exact numbers; bad-row count is 0.

## 3. Attack on the legs (escape routes named, with the leg that catches each)

### (a) Can a tool that prints a canned summary line pass QUEUE?

- Single canned line: **no**. QUEUE tests two as-of dates with one tool binary;
  one constant line cannot equal both `(0,18,14,827)` and `(813,0,14,827)`.
  Control A: `LEG FAIL QUEUE (2026-11-04: 0/18/14/827 ok; 2027-11-01: tool
  (0, 18, 14, 827) != counter (813, 0, 14, 827))`. The two-date design at
  lines 279-296 is what binds here.
- Strongest canned adversary (date-conditional: correct numbers at both frozen
  dates, selftest line, never reads the registry): **still fails**. Control E:
  QUEUE PASS, `LEG FAIL MODULAR`, `LEG FAIL ERROR` → FAIL 5/7. MODULAR's
  population append (lines 309-312, checks at 333) demands rows move +1 on a
  mutated registry; a canned count is frozen. ERROR (line 354) demands
  `RECHECK-ERROR` + exit 2 on a malformed registry.
- Residual gap in QUEUE itself: it reads only the LAST `SUMMARY` match
  (283-286) and never counts matches. "Exactly one summary line" is not
  enforced — control C (decoy wrong line, then correct line) **PASSes 7/7**.

**Verdict on (a): no canned tool passes; the two-date QUEUE + MODULAR + ERROR
triad binds. But the "exactly one summary line" clause of the contract is
unenforced.**

### (b) Can a tool that ignores `--registry` pass?

- Control D2 (parser hardcoded to `corpus/SOURCES.md`, counter run with
  cwd = clone so the default resolves to the base registry, byte-identical to
  the frozen blob): `LEG PASS QUEUE` — yes, it passes QUEUE when the default
  path's bytes equal the frozen blob. QUEUE alone does not prove the flag is
  honored.
- But MODULAR and ERROR always catch it: they hand the tool scratch registries
  with different content (MODULAR appends at 309-312/320-323; ERROR's broken
  12-cell registry at 346-352). D2: `LEG FAIL MODULAR (neutral +1 row ->
  (0, 18, 14, 827)…)` and `LEG FAIL ERROR (exit=0 labelled=False)`. FAIL 5/7.
- If the lane's live registry later diverges from the frozen blob, QUEUE also
  catches it (tool reads live, counter reads frozen).

**Verdict on (b): yes for QUEUE alone under byte-identical defaults; no for the
counter as a whole — MODULAR + ERROR bind registry honoring.** Note
`tool_run` (180-183) always passes `--registry/--as-of/--window` explicitly,
so the contract's defaults are never exercised by any leg (see §5).

### (c) Does MODULAR actually catch a count that moves with its population?

Yes, empirically, three times: controls A, D2, E all keep rows at 827 under
appends and fail. MODULAR's design: neutral row `S900` (opened = as_of,
`365d` → due as_of+365, far outside the window) must leave due/upcoming/
on-release unchanged with rows+1 (check line 333); due row `S901` (recheck =
ISO `as_of − 1`) must raise due by exactly one with rows+1 (line 334).

**Blind spot (calibration defect, not a tradeoff): MODULAR never exercises
NNd arithmetic near a bucket boundary.** Its due row uses an ISO cadence
(line 320-321 → `due_date` line 108 branch), and its only `NNd` row is
365 days out (line 309-310), where ±1 day cannot change the bucket. Probe —
a full sweep of the frozen population with the counter's own parser, NNd
dates shifted ±1 day:

```
NNd-1day 2026-11-04 (0, 18, 14, 827)
NNd-1day 2027-11-01 (813, 0, 14, 827)
NNd+1day 2026-11-04 (0, 18, 14, 827)
NNd+1day 2027-11-01 (813, 0, 14, 827)
baseline  2026-11-04 (0, 18, 14, 827)
baseline  2027-11-01 (813, 0, 14, 827)
```

A tool computing `opened + NN ± 1 days` violates the contract ("turns `NNd`
into opened+NN days") yet passes QUEUE (counts unchanged at both frozen
dates), MODULAR (synthetic rows bucket-stable), and ERROR. **The instrument
certifies behavior at two frozen dates, not the arithmetic.** Smallest safe
correction: give MODULAR (or QUEUE's fixture) an NNd row whose due date sits
on the as_of or as_of+window boundary.

### (d) Is the SELFTEST floor (>= 8 checks) meaningful if the tool self-reports the number?

- The leg (240-262) runs the lands bytes with `--selftest` and enforces only:
  a line matching `^SELFTEST: PASS \((\d+) checks\)$` (line 44), rc == 0, and
  `n >= cfg["min_selftest_checks"]` (257). The integer is self-declared and
  unverified — controls A/C/E printed "8"/"13" checks with no checks behind
  them and passed.
- What the floor DOES bind: the tool must run and speak the format. Control D
  (first build, a syntax-error tool) failed SELFTEST with `<no verdict line>
  rc=1`, and because st_ok gates QUEUE (270-271), MODULAR (302) and ERROR
  (343), a non-running tool fails everything. The counter's own selftest junk-3
  case proves under-reporting ("(3 checks)") fails; over-claiming is free.

**Verdict on (d): as a work floor it is cosmetic; as a runnability smoke test
it binds the remaining legs. Net: harmless, weak.**

## 4. Controls — build and verdicts (full receipts in receipts/)

All graded: `python3 -B reports/round-82/accept-o82.py --root $D/lane
--lands <L> --freeze c661e5c… --work $D/work` from cwd `$D/lane`.

| control | lands | description | verdict |
|---|---|---|---|
| A | 6ae2e23d… | canned single summary line + canned selftest | **FAIL 4/7** — QUEUE (far date), MODULAR, ERROR |
| B | e9df7754… | working parser, contract-conformant EXCEPT no `DUE` lines | **PASS 7/7** |
| C | c9a0797e… | B + decoy wrong summary line printed before the correct one | **PASS 7/7** |
| D2 | 24b0715f… | B but ignores `--registry` (default path byte-identical to frozen blob) | **FAIL 5/7** — QUEUE PASS; MODULAR, ERROR |
| E | 2abb22ce… | date-conditional canned, correct at both frozen dates, no registry read | **FAIL 5/7** — QUEUE PASS; MODULAR, ERROR |

Control B is the load-bearing result: **a tool that violates the contract's
explicit "one `DUE <id> <iso-date>` line per due row" requirement passes the
frozen counter.** `grep -c DUE accept-o82.py` → 0 matches; no leg inspects
DUE lines.

Raw receipts (verbatim copies):
- receipts/controlA-canned.txt
- receipts/controlB-no-duelines.txt
- receipts/controlC-decoy-line.txt
- receipts/controlD2-ignores-registry.txt
- receipts/controlE-date-canned.txt
- receipts/counter-selftest.txt — the counter's own `--selftest`: PASS (12
  checks), incl. do-nothing-control refused, non-40-hex refused, missing
  --work refused, LEGCOUNT refused, junk canned fails QUEUE, junk weak
  selftest fails SELFTEST, junk malformed-accepted fails ERROR.

Counter verdict lines:
```
A: ACCEPT-O-82: FAIL legs=4/7     (LEG FAIL QUEUE / MODULAR / ERROR)
B: ACCEPT-O-82: PASS legs=7/7
C: ACCEPT-O-82: PASS legs=7/7
D2: ACCEPT-O-82: FAIL legs=5/7    (LEG FAIL MODULAR / ERROR)
E: ACCEPT-O-82: FAIL legs=5/7     (LEG FAIL MODULAR / ERROR)
```

## 5. Under-specification register — each ambiguity and the reading the counter enforces

1. **Window far boundary** — contract: upcoming = `as-of < due_date <= as-of
   + window days`. Counter enforces INCLUSIVE far end: line 127
   `elif d <= as_of + timedelta(days=window)`, reached only when `d > as_of`
   (125-126). `due_date == as-of + window` → upcoming. An exclusive reading
   would shift boundary rows; the frozen population has none within ±1 day
   (§3c probe), so the distinction is unobservable at the frozen dates.
2. **Window near boundary** — due includes `due_date == as_of` (line 125,
   inclusive). Contract "due = due_date <= as-of" — consistent.
3. **Row membership** — contract says "the 11-cell Registry rows (0-3 leading
   spaces)" without defining membership. Counter line 42: a row is a line
   matching `^\s{0,3}\|\s*S\d{3,}\s*\|` — 0-3 leading whitespace (`\s`, so
   tabs too, not just spaces), first cell an S followed by ≥3 digits. Lines
   indented ≥4, or with non-S ids, are invisible (not malformed). A tool with
   a broader row definition diverges on the rows count → QUEUE FAIL.
4. **Malformed vs non-row** — contract: "a malformed row (not 11 cells) exits
   2". Counter: only ROW_RULE-matching lines can be malformed; the ERROR
   fixture (line 346-352) is a 12-cell S-row. Non-matching junk lines are
   ignored by both sides.
5. **`rows` on a malformed registry** — counter's tally counts malformed rows
   in `rows` (line 129 `len(parse_rows(text))`) but the contract forces exit 2
   on malformed, so no summary ever coexists with bad rows; the branch is dead
   w.r.t. the tool comparison. Unobservable.
6. **"ISO date" cadence** — counter line 108 `date.fromisoformat(recheck)`:
   Python ≥3.11 accepts compact `YYYYMMDD` and week dates beyond `YYYY-MM-DD`.
   A stricter tool is indistinguishable on the frozen registry (all cells are
   `YYYY-MM-DD`, `NNd`, or `on-release`).
7. **Whitespace in cells** — counter strips every cell (line ~96). Contract
   silent; enforced.
8. **Success exit code** — contract silent; counter enforces rc == 0
   (line 287).
9. **`DUE` lines (one per due row)** — contract explicit; counter enforces
   NOTHING (0 references; control B passes 7/7). Open gap.
10. **"Exactly one summary line"** — contract explicit; counter takes the last
    match (283-286; same pattern at 315-318 and 326-329). Open gap
    (control C).
11. **`RECHECK-ERROR` stream** — contract "printing"; counter accepts stdout
    or stderr (line 353 concatenates). Both readings pass.
12. **Argument defaults (`--registry` corpus/SOURCES.md, `--window` 90)** —
    `tool_run` (180-183) always passes all three explicitly; no leg invokes
    the tool without them. A tool with no defaults passes; the default
    behavior is unexercised.
13. **`--selftest` floor** — self-reported integer ≥ 8 (257) + rc 0; the count
    is unverified (§3d).
14. **DUE-line ordering, `on-release` casing** — unenforced / exact-match
    enforced respectively (line 103).

## 6. Verdict

- **The claim is not vacuous.** The cheapest do-nothing control (A) fails
  4/7; the strongest canned adversary (E) fails 5/7. The two-date QUEUE
  recompute (line 280) + MODULAR population append (309-334) + ERROR
  malformed-registry probe (346-354) triad forces real parsing of the actual
  registry bytes, and the refusal spine (verified by the counter's own 12-check
  selftest) blocks the do-nothing landing.
- **Two contractual requirements are unenforced** (fixable defects, not
  tradeoffs): per-row `DUE <id> <iso-date>` lines (control B passes without
  them) and "exactly one summary line" (control C passes with a decoy).
  Smallest safe correction: a DUE-line leg comparing per-id due sets against
  the counter's own parse, and counting SUMMARY matches (require == 1) in
  QUEUE/MODULAR/ERROR extraction.
- **One calibration defect**: NNd arithmetic is under-determined by the frozen
  population — an `opened + NN ± 1 days` tool passes everything (§3c sweep).
  Smallest safe correction: a boundary-proximate NNd synthetic row in MODULAR.
- **Two soft spots, bounded**: --registry-ignoring passes QUEUE under
  byte-identical defaults (MODULAR+ERROR catch), and the SELFTEST floor is
  self-reported (but gates runnability, which binds).

Impacted axes: operability (the instrument works; no canned tool passes),
calibration (PASS certifies counts at two dates only — DUE absence, extra
summary lines, and NNd off-by-one all grade green).
