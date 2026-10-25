# SKILL.md §Gates and probes — missing registry rows (round-73 w1, seat ScribeSkillGates)

Draft only. SKILL.md is NOT edited by this seat; the canonical writer applies the rows below at
the stated anchor. Measured at lane HEAD `8841ad3b896a0227674fa0725b818c999118046f`
(2026-10-25), which is also `reports/round-73/claims.json` `.base`.

## 1. What is missing, measured

| probe | command | result |
|---|---|---|
| registry rows present | `grep -cE '^\| [^|]+ \| (gate\|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py' SKILL.md` | `36` |
| counter files present | `find reports -name 'accept-*.py' \| sort \| wc -l` | `41` |
| counters with no row | `for f in $(find reports -name 'accept-*.py' \| sort); do grep -qF "reports/${f#reports/}" SKILL.md \|\| echo "MISSING-ROW $f"; done` | exactly five: `round-71/accept-c.py`, `round-71/accept-ca.py`, `round-71/accept-d.py`, `round-72/accept-c.py`, `round-72/accept-ca.py` |
| registry mentions of rounds 70-72 | `grep -n 'round-7[012]' SKILL.md` | no output |

`reports/round-70/` holds **no** `accept-*.py` at all (`ls reports/round-70/` -> `claims.json`,
`corrections-r69.md`, `telemetry/`). Round-70's three claims were counted by shell pipelines
(`grep -cE …`, `awk -F'|' …`, `python3 -B tools/check-supersession-settlement.py --selftest`;
`reports/round-70/claims.json` `.claims[].counting_command`), so `accept-c-70` and `accept-ca-70`
never existed as files and no registry row can be drafted for them without inventing a gate.
Round-70 claim **O** was itself "give every counter a registry row", so its predicate
(`row count == find count`) read `36 == 36` when filed; today it reads `36 != 41` and this
insertion restores `41 == 41`.

## 2. Exact insertion anchor

Insert the five rows **after SKILL.md line 697 and before line 698**. Line 697 is the last row of
the registry table (`accept-o-69`); line 698 is blank; line 699 begins the paragraph
"The contrastive checker is example-specific…". Verbatim surrounding lines (raw, pipes intact):

```
696: | accept-d-69 | gate | `python3 -B reports/round-69/accept-d.py --root .` | Exit codes: 0 pass · 1 fail · 2 usage/env. | `python3 -B reports/round-69/accept-d.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
697: | accept-o-69 | gate | `python3 -B reports/round-69/accept-o.py --root .` | Exit codes: 0 pass · 1 fail · 2 usage/env. | `python3 -B reports/round-69/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
698: (blank)
699: The contrastive checker is example-specific, not a general culture validator.
```

Append-only insertion; no existing row is rewritten. The table header stays line 648
(`| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |`,
8 columns) and every drafted row carries exactly those 8 cells. Verdict cells avoid the
`PASS|FAIL` pipe used by the round-66/67 rows so the column count stays 8.

## 3. Rows to insert (verbatim)

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| accept-c-71 | gate | `python3 -B reports/round-71/accept-c.py --root .` | Output ends `ACCEPT-C-71: PASS` or `: FAIL` (no legs= token); 0 pass / 1 fail / 2 input error. | — (no `--selftest`; passing it is an argparse error, exit 2) | entry path, partition/corpus counts 36 and 243, `>=12` cited ids pinned in script | read-only; no revision pin — grades whatever tree `--root` names | kotodama-shokunin |
| accept-ca-71 | gate | `python3 -B reports/round-71/accept-ca.py --root .` | Output ends `ACCEPT-CA-71: PASS` or `: FAIL` (no legs= token); 0 pass / 1 fail / 2 input error. | — (no `--selftest`; argparse error, exit 2) | 21-id quarantine slice, verdict set {PRESENT, REFUSED, UNVERIFIABLE}, unreachable ids S807/S812/S835, six round-70 receipt paths pinned in script | read-only; no revision pin — grades whatever tree `--root` names | kotodama-shokunin |
| accept-d-71 | gate | `python3 -B reports/round-71/accept-d.py --root .` | Delegates to the frozen round-69 counter, so output ends `ACCEPT-D-69: PASS` or `: FAIL legs=8/8` — a grep for `ACCEPT-D-71` finds nothing; 0/1 from the frozen counter, 2 on usage/env. | `python3 -B reports/round-71/accept-d.py --selftest` (prints the frozen `GREEN FIXTURE`, `DO-NOTHING FIXTURE`, `SELFTEST: n/2`) | frozen counter path `reports/round-69/accept-d.py` and the no-git marker string pinned in script | read-only; selftest scratch in `tempfile.TemporaryDirectory`; a tree without `.git` prints `SELFTEST: COULD-NOT-EVALUATE (no git)` and exits 2 | kotodama-shokunin |
| accept-c-72 | gate | `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex>` | Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10` — the denominator is a literal, so a FAIL receipt still reads `legs=10/10`; 0 pass / 1 fail; 2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`. | `python3 -B reports/round-72/accept-c.py --selftest` — measured `SELFTEST: 10/11`, exit 1 at HEAD (see §5) | base `b60c7b14…`, ids S874/S875, both entry paths, scratch-mirror receipt path, ten mutants pinned in script | read-only against `--lands` via `git show`; selftest builds `tempfile.mkdtemp` fixtures and leaves them behind | kotodama-shokunin |
| accept-ca-72 | gate | `python3 -B reports/round-72/accept-ca.py --root . --lands <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` | Output ends `ACCEPT-CA-72: PASS` or `: FAIL legs=12/12` — literal denominator; 0 pass / 1 fail; 2 on missing or malformed `--lands`; a well-formed but absent revision grades as leg FAILs with exit 1. | — (no `--selftest`; argparse error, exit 2) | base `b60c7b14…`, fleet root, five known round-71 report commits, seven w2 file paths, CASTAMP path, authorized path prefixes pinned in script | read-only (`git show` plus absolute reads of the fleet report); corpus materialized only into temp dirs | kotodama-shokunin |

## 4. Per-gate detail (facts the 8 columns cannot carry)

**accept-c-71 — round 71, claim C (coverage).** Checks the frozen claim-C predicate at the graded
tree: the dance entry exists; culture-material partition count is 36 and corpus total 243;
the entry cites >=12 distinct S-ids; every cited row exists with `status = mined` and a used-by cell
naming the entry; every used-by path exists; `tools/check-cited-lines.py` exits 0 on the entry; and
the gap sweep shows the entry as the only owner. Seven legs: `ENTRY`, `COUNTS`, `CITED`, `ROWS`,
`USEDBY-PATHS`, `CITED-LINES`, `SWEEP`. Stale tree: no `--lands`/`--base` pin — the counter reads
the passed tree's bytes and files, so a pre-round-71 export FAILs legs and exits 1; it never exits 2
for a historical tree. `--lands` is accepted but only printed, never graded.

**accept-ca-71 — round 71, claim Ca (calibration).** Checks the five V70-1..V70-5 landings plus the
item-10 quarantine table: all six round-70 telemetry receipts carry the six 17/19 header lines with
the original first line preserved below a marker; S860's verify-at cell names `acc2d614`; the
round-70 Gate quote is <=25 words; SCORECARD carries a `round-70 trend-correction` row; the
round-71 lesson Gate states `rejected this round:` with >=1 candidate plus reason and flip; and
`reports/round-71/telemetry/quarantine-verdicts.md` carries a recognized verdict for exactly the
21 slice ids, with S807/S812/S835 forced to `UNVERIFIABLE`. Six legs: `V70-1`..`V70-5`,
`QUARANTINE`. Stale tree: same shape as accept-c-71 — no revision pin, historical tree FAILs
(exit 1); a tree missing `reports/round-70/telemetry/*` fails at `V70-1`.

**accept-d-71 — round 71, claim D (depth, V70-6).** A no-git guard wrapper around the frozen
`reports/round-69/accept-d.py`: with `.git` present it forwards only `--root` to the frozen counter,
whose verdict line is `ACCEPT-D-69: PASS|FAIL legs=8/8`; without `.git` the selftest prints
`SELFTEST: COULD-NOT-EVALUATE (no git)` and exits 2 instead of reporting the false red that the
frozen fallback produced on an exported tree. A git failure that is *not* a missing store (e.g. a
`GIT_DIR` override pointing nowhere) is graded `COULD-NOT-EVALUATE (git unavailable: …)`, still 2.
The `--lands` flag is reserved and never forwarded. Stale tree: this is the one gate in the set with
a declared historical-tree behaviour — an exported tree lacking `.git` is a declared exit 2 for the
selftest, never a craft failure.

**accept-c-72 — round 72, claim C (coverage, assimilation).** Checks ten legs of committed bytes at
`--lands` via `git show`: `ENTRIES` (both heritage-taxonomy files with the full header), `ROWS`
(exactly S874/S875 added, mined, used-by the two entries), `REPOINTED` (every `source:` citation is
an id >= S874 whose row URL matches), `GATE` (lesson `## Gate` per row: URL, access date, <=25-word
located quote, >=1 admit and >=1 reject with reason and flip), `REJECTS` (the two refused staged
entries named), `GROUND` (gap sweep 0 at the 797-row registry, re-derived from the base registry),
`CITEDLINES`, `CENSUS` (census script exits 0 at `--lands`), `SCRATCHMIRROR`, `COLLCHECK`. Stale
tree: a historical tree is fine *if* `--lands` names it and the revision is present; an absent
revision makes the `git show` legs fail (exit 1), while a malformed/missing `--lands` or a `--root`
without `.git` is exit 2. `--base` defaults to the pinned round-72 base, so a tree whose history
does not contain it cannot satisfy `ROWS`/`GROUND`.

**accept-ca-72 — round 72, claim Ca (calibration).** Twelve legs over `base..lands`:
`QUAL20`, `W2FILES`, `LOGCORR`, `LESSONCORR`, `REPORTCORR`, `MAPCORR`, `CASTAMP`, `QUAL21`,
`CAPOEIRA`, `APPENDONLY`, `REPORTLAST`, `NOHARM`. It reads the fleet report from the absolute
`--fleet-root` (fails closed if unreadable), requires every changed tracked file in `base..lands`
to map to an authorized round-72 path, requires zero removed content lines in the enumerated filed
set, and re-runs the census against a materialized corpus in a temp dir. Stale tree: `--lands` is
required and must be 40 hex (else exit 2); a well-formed but absent revision grades as leg FAILs and
exit 1 (measured, §5). Its receipts are only meaningful at the round-72 lands revision — at any
other tree it reports the mismatch, which is the intended by-design behaviour, not a defect.

## 5. Measured runs (all read-only; nothing written inside the lane)

| command | exit | output |
|---|---|---|
| `python3 -B reports/round-71/accept-c.py --help` | 0 | usage: `[-h] [--root ROOT] [--lands LANDS]` |
| `python3 -B reports/round-71/accept-ca.py --help` | 0 | usage: `[-h] [--root ROOT] [--lands LANDS]` |
| `python3 -B reports/round-71/accept-d.py --help` | 0 | usage: `[-h] [--root ROOT] [--lands LANDS] [--selftest]` |
| `python3 -B reports/round-72/accept-c.py --help` | 0 | usage: `[-h] [--root ROOT] [--lands LANDS] [--base BASE] [--fleet-root FLEET_ROOT] [--census-sh CENSUS_SH] [--selftest]` |
| `python3 -B reports/round-72/accept-ca.py --help` | 0 | usage: `[-h] [--root ROOT] --lands LANDS [--fleet-root FLEET_ROOT]` |
| `python3 -B reports/round-71/accept-d.py --selftest` | 0 | `GREEN FIXTURE: PASS (legs 8/8)` / `DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)` / `SELFTEST: 2/2` |
| `python3 -B reports/round-71/accept-d.py --root .` | 0 | last line `ACCEPT-D-69: PASS legs=8/8` |
| `python3 -B reports/round-72/accept-c.py --selftest` | **1** | `SELFTEST: 10/11`; clean fixture fails `GROUND`: `receipt missing: reports/round-72/telemetry/gap-sweep.txt`, then `ACCEPT-C-72: FAIL legs=10/10` |
| `python3 -B reports/round-72/accept-c.py` (no `--lands`) | 2 | `ERROR: --lands must be a 40-hex commit` |
| `python3 -B reports/round-72/accept-c.py --lands deadbeef` | 2 | same error |
| `python3 -B reports/round-72/accept-c.py --root <empty tmp dir> --lands <40 hex>` | 2 | `ERROR: not a git repository: /tmp/scg-nogit-…` |
| `python3 -B reports/round-72/accept-ca.py --lands deadbeef` | 2 | `ERROR: --lands must be 40 hex` |
| `python3 -B reports/round-72/accept-ca.py --lands 0000…0000` | 1 | `LEG FAIL REPORTLAST`, `LEG FAIL NOHARM` (`corpus materialization failed`), `ACCEPT-CA-72: FAIL legs=12/12` |
| `python3 -B reports/round-71/accept-c.py --selftest` | 2 | `error: unrecognized arguments: --selftest` |
| `python3 -B reports/round-71/accept-ca.py --selftest` | 2 | `error: unrecognized arguments: --selftest` |
| `python3 -B reports/round-72/accept-ca.py --selftest` | 2 | `error: the following arguments are required: --lands` (the required flag is diagnosed before the unknown one) |

The `accept-c-72 --selftest` run left eleven `tempfile.mkdtemp` fixture trees (`/tmp/r72st-*`) —
`build_fixture` never removes them; this seat deleted only the ones its own run created.

## 6. Findings this draft carries (for the canonical writer / calibration claim Ca)

1. **R3 scope correction.** The round-72 spot-check R3 wording "no rows for accept-ca-70..72 /
   accept-c-70..72" overstates the gap on the 70 side: no round-70 counter file exists. The real
   gap is exactly five rows, all from rounds 71 and 72. A Ca correction row should state the
   observed token as five counters, not six.
2. **`accept-c-72 --selftest` is red at HEAD** (10/11, exit 1), deterministically: the fixture
   writes `RECEIPT = .ufo/waves/round-72/assimilation/validate-receipt.txt`
   (`reports/round-72/accept-c.py:70`, written at `:716`) while leg `GROUND` reads
   `GROUND_RECEIPT = reports/round-72/telemetry/gap-sweep.txt` (`:71`, read at `:380`) — a path the
   fixture never creates. The `ground_zeros` mutant therefore cannot discriminate: it edits the
   scratch receipt, not the GROUND receipt, and the leg fails for the missing-file reason instead.
   The registry self-test cell must not claim a passing selftest; the draft says so.
3. **Hardcoded leg denominators.** `accept-c-72` prints `legs=10/10` and `accept-ca-72` prints
   `legs=12/12` unconditionally (`reports/round-72/accept-c.py:552`,
   `reports/round-72/accept-ca.py:231`), so a FAIL receipt still carries the full denominator —
   measured above as `ACCEPT-C-72: FAIL legs=10/10` and `ACCEPT-CA-72: FAIL legs=12/12`. Any
   receipt check that greps `legs=12/12` without the `PASS` token can read a failure as a full
   pass; this is the same class as routed defect R2 and should be named in Ca, not silently
   "fixed" here.
4. **Name/verdict mismatch.** `accept-d-71` emits `ACCEPT-D-69: …` because it delegates to the
   frozen round-69 counter; the registry row states the printed token so no future grep for
   `ACCEPT-D-71` treats the gate as missing.
5. **Row-count invariant.** Inserting these five rows makes the round-70 claim-O predicate
   (`grep -cE '^\| [^|]+ \| (gate|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py' SKILL.md`
   equals `find reports -name 'accept-*.py' | wc -l`) read `41 == 41`; today it reads `36 != 41`.

## 7. Out of scope / not done

- SKILL.md was not edited; no other lane or fleet file was touched.
- No full data-counter run was performed for accept-c-71 / accept-ca-71 / accept-c-72 /
  accept-ca-72 (the seat's instruction was selftest-or-help only); their verdict maps are read from
  the scripts' own print statements and measured exit-2/exit-1 paths, not from a green round run.
- No tools were installed; no network fetch was made, so no User-Agent record applies.
