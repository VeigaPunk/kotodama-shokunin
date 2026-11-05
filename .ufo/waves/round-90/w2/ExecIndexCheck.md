# ExecIndexCheck — r90-w2 structural verification of the landed corpus moves

Seat: ExecIndexCheck (leaf, godspeed). Lane: kotodama round 90.
Freeze `d0b6f2a7f9cc36272682749a9b047b739406f0c8`, base `6b0b86e45ae902331aca75863db380f2991458c4`,
claim-C lands revision `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761` (single lands commit verified
with `git rev-parse --verify 7f3a7aa…^{commit}` and `git log -1`: "round-90: claim C landing —
petitionary and votive entry, seven admitted rows and one rejection, captures and manifest,
README moves, separability harness, census end").

Environment: working clone at `/fast/scratch/hyaku/kotodama-r90/ExecIndexCheck/clone`
(`git clone` of the lane, then `git checkout --detach <lands>`; `git status --porcelain` = 0 lines,
HEAD = lands sha). TMPDIR set to `/fast/scratch/hyaku/kotodama-r90/ExecIndexCheck/tmp`. Scratch
removed at exit. Claims.json read first (frozen; not amended). No production files created or
modified; the only writes outside scratch are this report and my stage dir. No git/jj mutations.

---

## Check 1 — `tools/check-corpus-index.py --root <clone>` (expect 0 findings)

Command:
```
python3 -B /fast/scratch/hyaku/kotodama-r90/ExecIndexCheck/clone/tools/check-corpus-index.py --root /fast/scratch/hyaku/kotodama-r90/ExecIndexCheck/clone
rc=0
```
Observed:
```
CORPUS-INDEX: OK files=262 rows=262 findings=0
```

Partition arithmetic (from the tool's `--json`, cross-checked with `find`):
- files on disk: civilizations 95, linguistics 35, myth-symbol 36, synthesis 29,
  verification 24, culture-material 43 — total **262**; `find corpus/knowledge -name '*.md'` = 262.
- README section headers (lines 344/379/413/456/488/514): `## linguistics/ (35)`,
  `## myth-symbol/ (36)`, `## culture-material/ (43)`, `## synthesis/ (29)`,
  `## verification/ (24)`, `## civilizations/ (95)` → sum 35+36+43+29+24+95 = **262** ✓.
- README Round-90 counts footer (line 954, dated 2026-11-04): `(total 262 files; directory
  totals 35/36/43/29/24/95)` — live footer matches the headers and the disk exactly ✓
  (claim-C delta: linguistics 34→35, total 261→262 vs base, per the one-file diff at lands:
  `-## linguistics/ (34)` is the only deletion in the whole base→lands diff).

Selftest (new control):
```
python3 -B tools/check-corpus-index.py --selftest --work <scratch/w>
...
SELFTEST: PASS (23 checks)   rc=0
```

**Result: PASS (0 findings).**

## Check 2 — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`

Command (run per spec against the production root, read-only):
```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
rc=0
```
Observed: last line `kotodama   ok   /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`;
full output = **36 lines, all warnings (W), 0 E-findings**.

**Does any warning name a new row S942–S949?** `grep -c "S94[0-9]"` over the census output = **0**
— no new row appears in any warning. The warnings are 34 pre-existing W04 cross-scope URL
duplicates (S127–S928) and 5 pre-existing W01 tier-C-mined rows (S881, S882, S884, S893, S907).
Cross-check: `diff` of my production-root output against the lane's own committed receipts
`reports/round-90/census-start.txt` and `census-end.txt` shows the two receipts are byte-equal to
each other (identical warning lines, `rc=0` both) and equal to my measured output apart from the
receipts' own header trailer lines — i.e. the round's recorded before/after census state is
reproducible at lands. Lane-repo census variant for completeness: running validate with
`--root <clone>` needs a `shokunin.conf` at that root (lane-resolution mechanics), so the clone
variant is not a supported invocation shape; the production run above and the two committed
receipts cover the same tree state at the same revision.

**Result: PASS (rc=0, no warning names S942–S949).**

## Check 3 — census clauses that matter for the new rows

Direct clauses measured over the lands registry (all counts in the validate output above plus the
tool's documented clause list E01–E12 / W01–W04 read from `scripts/sources-census.sh:607-680`):

- **E01 malformed-row count: 0.** Independent field check: all of S942–S949 have `fields=11`
  (NF=13) — measured with an awk NF pass over those 8 rows (single `|`-split field arithmetic;
  the earlier `fields=11 kind=…` prints). No `E01` and no `E02/E03/E05/E06/E07/E10` lines anywhere.
- **E03 duplicate ids: 0.** `grep -o "^| S94[0-9]" … | sort | uniq -c` → each of S940–S949 once;
  S942–S949 ids do not collide with any other row.
- **E05/E06/E07 enum violations: 0.** Row cells: S942/S943/S944 (docs, A, mined, 90d),
  S945 (docs, B, mined, 180d), S946 (docs, A, mined, 90d), S947 (docs, A, mined, 90d),
  S948 (paper, A, mined, 90d), S949 (community, C, rejected, 180d) — all statuses within
  queued|mined|rejected, all tiers within A|B|C, kinds within the enum; S949 (community, tier C)
  respects the "community is never tier A" rule.
- **Tier inflation: none.** census mode at production HEAD: `rows 873; tier.A 517; tier.B 330;
  tier.C 26; tier.invalid 0`. Base blob (865 rows) tier cells: A 511, B 329, C 25 → delta is
  exactly the 8 new rows: +6 A (S942–S944, S946–S948), +1 B (S945), +1 C (S949 as rejected),
  0 unverifiable promotions. (Raw census at base is not re-derivable with the same fleet-root
  conf — see check 2 note — so the delta is computed from the base blob's own cells, same
  arithmetic the census awk uses.)
- **E11 / "mined rows whose used-by paths do not exist": 0.** All S942–S948 used-by paths name
  `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` and S949's names
  `corpus/lessons/round-90.md`; both files exist on disk in the clone. No `E11` line in the
  census output; no W03 (mined-but-unused) either.
- Bonus structural fact: the lands diff over corpus/SOURCES.md is pure append — 8 added `| S94x`
  rows, **0 removed rows, 0 cell edits** (verified with `git diff base lands -- corpus/SOURCES.md`
  grep counts: `+| S` = 8, `-| S` = 0, and no other changed registry line), rows appended in id
  order directly after S941 (lines 898–905), respecting the freshness pause.

**Result: PASS — all five reported clauses clean for the new rows.**

## Check 4 — `tools/check-gate-registry.py --root <clone>` and the counter-path question

Command:
```
python3 -B /fast/scratch/hyaku/kotodama-r90/ExecIndexCheck/clone/tools/check-gate-registry.py --root /fast/scratch/hyaku/kotodama-r90/ExecIndexCheck/clone
rc=0
```
Observed:
```
GATE-REGISTRY: 0 missing / 86 registered / 63 instruments / 0 dead
GATE-REGISTRY-INFO: 26 tools without a row
```
`--json`: `missing: []`, `dead: []`; the 63 instruments are all `reports/round-*/accept-*.py`
(round counters to date, r53–r84). Tool-glob arithmetic: 35 `.py` at base + 1
(`tools/check-advance-evidence.py`) = 36 at lands ✓ (the earlier 34/35 ls-tree read counted
directory entries, not files — reconciled by filename-set diff).

**Did the round add a counter path this registry should know about?** Two answers, both measured:

1. The **`accept-*.py` instrument set** (what check-gate-registry.py enforces): round 90 added
   **none** — no `reports/round-90/accept-*.py` exists at lands; round 90's counters are
   `reports/round-90/measure90.py`, `mutants.py`, `separability90.py`. So the checker's PASS is
   correct and vacuous with respect to round 90, exactly as with round 89 (whose `measure89.py`
   likewise never entered the accept-* instrument set and has no registry row: `grep -c measure89
   SKILL.md` = 0).
2. The **human gate registry in `SKILL.md` `## Gates and probes`** (86 rows): it does register
   round counters of recent rounds (`measure-86` line 769, `measure-87` line 773, `measure-88`
   line 775) but has **no row for round-90's counter** — `SKILL.md` contains zero occurrences of
   `measure90`/`measure-90`/`round-90`, and `SKILL.md` was not touched by the lands commit (diff
   base→lands on SKILL.md is empty). 26 tools remain without a row (info-only class, includes
   the new `tools/check-advance-evidence.py` itself, which is registered with prior un-registered
   tools until the next SKILL reconcile).

   Finding (advisory, no lane edits by this seat): **yes — the registry should eventually gain a
   round-90 counter row** (`reports/round-90/measure90.py`, the frozen claim-C/O grader), consistent
   with how measure-86/87/88 were given rows in their own rounds. This is not a round-90 kill:
   measure88's row was added in the round-88 landing and measure89 has *no* row, so lane practice
   is inconsistent; I record it as the one divergence this structural pass found, with precedence
   (measure89 unregistered) showing the registry does not currently fail on it, and
   check-gate-registry.py exits 0 at lands because only accept-* instruments are enforced.

**Result: PASS (rc 0, 0 missing / 0 dead), plus one advisory finding (no SKILL row for the
round-90 counter yet).**

## Check 5 — README counts equal on-disk partition counts; new entry's README topic cell byte-equal

- Counts: covered in check 1 (262 = 262; footer vector 35/36/43/29/24/95 matches headers and
  disk; instrument-verified, findings=0 includes the tool's row-topic byte-equality leg and its
  totals/footer legs; the `--json` shows `footer_live` and `parts.*` all reconciled, 0 duplicate rows).
- New entry's README topic cell byte-equality (manual, byte-level, independent of the instrument):
  - README line 360: `` - `petitionary-and-votive-formulae.md` — petitionary address and votive
    formulae: vocative address to deities, petition mood (imperative, optative, precative), the
    conditional vow, votive inscription grammar, prayer-register archaism and parallelism, design
    procedure and failure modes ``
  - Entry line 3: `- topic: petitionary address and votive formulae: vocative address to deities,
    petition mood (imperative, optative, precative), the conditional vow, votive inscription
    grammar, prayer-register archaism and parallelism, design procedure and failure modes`
  - `diff` after stripping the two prefixes → **no difference** (`diff` exit 0, "BYTE-EQUAL after
    prefix strip"). Exact prefix-stripped strings identical, including no trailing whitespace drift.

**Result: PASS.**

---

## Verdict

All five assigned structural checks pass at lands `7f3a7aa6`:
1. CORPUS-INDEX OK files=262 rows=262 findings=0 (rc 0) + SELFTEST PASS 23 checks.
2. sources-census validate rc=0; no warning names S942–S949; committed census-start/end receipts
   reproduce at lands.
3. For the new rows: 0 malformed, 0 duplicate ids, 0 enum violations, pure-append tier delta
   (+6 A / +1 B / +1 rejected C, no inflation), 0 dangling used-by paths.
4. GATE-REGISTRY 0 missing / 86 registered / 63 instruments / 0 dead (rc 0). Advisory: the SKILL
   gate registry has no row yet for the round-90 counter `reports/round-90/measure90.py`
   (precedent: measure-86/87/88 have rows; measure89 also has none — lane practice inconsistent;
   measured, not inferred).
5. README counts = on-disk counts (262 total; 35/36/43/29/24/95 per partition); new entry's
   README topic cell byte-equal to the entry's own `- topic:` line.

No freshness pause breach observed (registry delta is pure append of 8 rows opened 2026-11-04;
no base row touched). Assimilation: none (lane has no considerthese directory; shokuknow
adoption closed). No tool installs were needed (python3, git, coreutils only) — nothing to
record under the tooling authorization.
