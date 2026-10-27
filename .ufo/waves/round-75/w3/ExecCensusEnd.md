# ExecCensusEnd — W3 falsification: the frontier census (kotodama round 75, hyaku run 10)

**Seat:** leaf executor, wave 3 (falsify). No delegation, no background jobs, no peer messages.
**Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Fleet root:** `/home/vgpnk/Projects/shokunin`.
**Revisions attacked:** base `f556d1049fe651d3d63975600b13acd9fb686f15`; freeze `5d0167464309d8133991b30f7d7a7011a6a0fd14`;
claim Ca lands `012e8d3c8b92f47c734f735d58d118d574fe6a14`; claim C lands `4f5e3b2535c2c06c51627dc2736c40183847cae1`;
lane `main` at dispatch `82ced5c` (telemetry + wave-3 spec only; `git log --oneline 4f5e3b2..main` = 1 commit).
**Scratch:** `/fast/scratch/hyaku/kotodama-r75/ExecCensusEnd/` (clone `lane` + run outputs), deleted before yield; nothing
citable points at it. **No lane file was written except this report; no fleet file, no sibling lane, no jj/git state.**
**Tooling:** nothing installed.

## Verdict

**HOLDS.** The census estate reproduces byte-for-byte at every revision it claims. **No E-code exists at base, at either
landing, or at main.** Three minor documentation observations (F1–F3) are recorded below; none is a claim-leg failure and
none is a data defect. The one warning the round *adds* is the designed `W01` for a tier-C row (F2).

---

## 1. The frozen census command, run live at main

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
exit=0   stdout=33 finding lines: 28 × W04, 4 × W01, 1 × ok
```

Codes histogram: `1 ok; 4 W01; 28 W04`. No line matches `\tE[0-9][0-9]\t`.
`diff` of my stdout against `reports/round-75/telemetry/census-end.txt` after deleting the receipt's blank line and its
`exit=0` line: **identical** (`IDENTICAL_TO_CENSUS_END`). The receipt body is reproduced exactly at `main`, including the
final line `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`.

## 2. `validate --file` over a clone's registry at each revision

Clone `git clone -q --shared <lane> $S/lane`; `git -C $S/lane rev-parse --show-toplevel` == `$S/lane`; checkout with
`git -C … checkout -q -B main <rev>`; every git call names `-C`.

| revision | `grep -cE '^\| *S[0-9]{3,} *\|'` | census exit | finding lines | codes |
|---|---|---|---|---|
| `f556d10` (base) | 808 | 0 | 32 | 28 W04 · 3 W01 · 1 ok |
| `012e8d3` (Ca lands) | 808 | 0 | 32 | 28 W04 · 3 W01 · 1 ok |
| `4f5e3b2` (C lands) | 817 | 0 | 33 | 28 W04 · 4 W01 · 1 ok |
| `82ced5c` (main) | 817 | 0 | 33 | 28 W04 · 4 W01 · 1 ok |

`git diff 012e8d3 f556d10 -- corpus/SOURCES.md` is **empty**: the Ca landing does not touch the registry, so `Ca` and
`base` share one census. The only delta from base to C-lands is the single line

```
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
```

Base-body vs `census-start.txt`: identical after normalising the first column (`file` for `--file`, `kotodama` for
`--root`) — only the final `ok <path>` line's path differs, because it is the clone's path.
C-lands-body vs `census-end.txt`: identical on the same normalisation.

`git diff --numstat f556d10 4f5e3b2 -- corpus/SOURCES.md` → `9 0`; removed row-shaped lines: `0`; added ids exactly
`S885 S886 S887 S888 S889 S890 S891 S892 S893` (contiguous, no id reused).

## 3. CORPUS.md manual census commands (lane root, main tree)

`CORPUS.md` §"Census — run from the lane root" (fleet root file; read-only).

| command | result at main (817-row tree) | result at base (clone, 808-row tree) |
|---|---|---|
| rows | `817` | `808` |
| malformed `NF!=13` (must print 0) | `0` | `0` |
| tier histogram | `A=491 B=310 C=16` | `A=488 B=305 C=15` |
| status histogram | `mined=722 queued=58 rejected=37` | `mined=713 queued=58 rejected=37` |
| duplicate ids (must print nothing) | nothing | nothing |
| enum violations + tier inflation (must print nothing) | nothing | nothing |
| mined rows whose `used-by` path is missing (must print nothing) | nothing | (not re-run; base used-by set unchanged from Ca) |

The manual `grep -cE '^\|…'` row count and the script's `rows` metric agree at 817, which also proves no row is
indented 1–3 spaces (the script tolerates indentation, the frozen manual command does not).

`census` mode (histogram authority) at main:
`FLEET rows 817 · tier.A 491 · tier.B 310 · tier.C 16 · tier.invalid 0 · status.queued 58 · status.mined 722 ·
status.rejected 37 · status.invalid 0 · missing 0`, exit 0.
At base: `rows 808 · A488 · B305 · C15 · mined 713 · queued 58 · rejected 37` — which is exactly claim Ca's declared
Ca-alone tuple `808/713/58/37`, and the lands tuple `817/722/58/37` is exactly claim C's declared combined tuple.

Knowledge-file cross-check (the lesson's `## Sources & frontier` numbers):
`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → base **249**, C-lands **252**;
`… | grep -ci narrative` → base **0**, C-lands **3**.

## 4. Comparison with the telemetry receipts

| receipt | sha256 | content |
|---|---|---|
| `reports/round-75/telemetry/census-start.txt` | `0a8c74ce…fefa4990` | 32 finding lines, **no** `exit=` line, no row-count token |
| `reports/round-75/telemetry/census-end.txt` | `99771bb2…380ce6c5` | 33 finding lines + blank line + `exit=0` |
| `.ufo/waves/round-75/census-start.txt` (committed at the freeze `5d01674`) | same sha `0a8c74ce…` | byte-identical copy of the telemetry start receipt |

`grep -c 808 census-start.txt` → **0**; `grep -c 817 census-end.txt` → **0**; `grep -c '^exit=' census-start.txt` → **0**.
The lesson `## Census` fenced block (lines 265–301) equals `census-end.txt` body exactly (`LESSON_BODY_EQUALS_RECEIPT`,
after dropping the block's leading `$ …` command line). The lesson's prose — "Rows 808 → 817, exit 0 both times, no
E-code line; W01 rows S881/S882/S884 as at start plus the new tier-C row S893 (the same class); the standing W04
duplicate-URL warnings are unchanged" — is true line for line: 28 W04 in both receipts, W01 3 → 4, exit 0 both times.

## 5. Cross-lane duplicate probe (the W04 blind spot)

`url_of()` in the fleet script reads only the **first** `https?://` of a row's source cell, so the durable/archive URLs
carried as second URLs by S891/S892 are never census-checked. Probed them directly across all lane registries:

```
persee …_1113 / …_1120 / …_1114 · jw.ucass.edu.cn · jstage …/jcss/25/2 · jstage …/jsik/32/2 ·
unige.ch/lettres/framo · iris.unipa.it · chinawriter.com.cn/n1/2023/0922
web.archive.org/web/20041220223357 · web.archive.org/web/20251111222249
  -> each matches kotodama-shokunin/corpus/SOURCES.md only
```

`sources-census.sh shared --root /home/vgpnk/Projects/shokunin` lists no kotodama URL (no shared pair). No cross-lane
duplicate was introduced by the round.

## 6. Liveness of the "no E-code" reading (falsifiability probe)

A cleanliness statement is worth nothing unless the instrument can go red. On a scratch copy of the registry I planted
one extra row carrying the existing id `S893`:

```
$ sources-census.sh validate --file $S/mut/SOURCES.md --today 2026-10-27
… file	E03	S893 duplicate id
… exit 1                                  (MUT_EXIT=1)
```

The planted row is caught and the run exits 1, so "exit 0 and no E-code line" is a live statement about the real
registry, not a property of the harness. (The same run also printed a long `E11` cascade because my fixture copy put
`knowledge/` one level too high — a defect of my mutation, not of the lane; it is why I did not use that run for any
number.)

## 7. The counter's own CENSUS leg, re-run in the scratch clone

```
$ python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2… --freeze 5d01674… \
    --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS CENSUS
     exit=0 last-line=file	ok	…/clone/corpus/SOURCES.md
ACCEPT-C-75: PASS legs=13/13
```

First attempt (same command **without** `--fleet-root`) printed `LEG FAIL CENSUS — census script not found:
…/ExecCensusEnd/scripts/sources-census.sh` and `legs=12/13`: that was my invocation deriving `fleet_root` from `--root .`,
not a defect of the counter or the census.

---

## Findings

**No E-code anywhere.** Findings are documentation-level only.

**F1 (minor, citation — number not carried by the receipt it is attributed to).**
`claims.json` `frontier_step.census_start` reads `.ufo/waves/round-75/census-start.txt (exit 0, 808 rows, 2026-10-27)`,
and the lesson `## Census` Before line reads "**exit 0, 808 rows** (`.ufo/waves/round-75/census-start.txt`…)"; the file
carries neither token: `grep -c 808` → 0, `grep -c '^exit='` → 0 (it is raw stdout, which for `validate` has no exit
line and no row metric). Both facts are true and independently re-derived here (exit 0 at base; 808 rows by the manual
grep and by `census` mode), and the 808 row count *is* carried by `reports/round-75/telemetry/gap-sweep.txt:4` ("at the
808-row registry"). The defect is attribution, not truth: a reader who opens only the named receipt cannot see either
number.

**F2 (observation — the round adds one W01, by design).** W01 goes 3 → 4. S893 is `kind=community, tier=C,
status=mined, used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`. That is precisely the shape W01
exists to flag (tier-C row used as support). The entry bounds it: `narrative-structure-frameworks.md:198` states "the
term is vocabulary at tier C (S893)", and no tier inflation exists (tier A ×3 / B ×5 / C ×1 in the nine new rows, matching
the lesson). Warning, not error; disclosed in the lesson.

**F3 (cosmetic — the two receipts are not written in the same format).** `census-end.txt` appends a blank line and
`exit=0`; `census-start.txt` carries neither. No factual effect: both bodies reproduce byte-for-byte from the revisions
they describe.

**Non-findings checked and cleared:** registry diff shape (9 added / 0 removed / contiguous ids); malformed rows 0;
duplicate ids 0; enum and tier-inflation violations 0; dangling `used-by` 0; W04 count unchanged at 28 (not 29 — the
earlier impression of 29 was a miscount of the same receipt); no cross-lane URL sharing; knowledge-file and
narrative-file counts as claimed; lesson `## Census` block equals the receipt.

## What would break this verdict (unrun probes)

1. A registry revision between base and C that the census was never run against (none exists: `Ca` does not touch
   `corpus/SOURCES.md` at all).
2. A W04/E04 hidden behind a **second** URL in a source cell — probed for the two rows that carry one (S891, S892); a
   future row with three URLs would need the same probe again.
3. A `used-by` path that exists only as a symlink or directory — `[ -e ]` does not distinguish; not exercised here.
