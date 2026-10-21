# ScoutCensus — `corpus/SOURCES.md` census at the round-50 base (2026-10-21)

Assigned (frontier, not a claim): run the maintained validator
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` and the seven
manual census commands from `CORPUS.md` §"SOURCES.md — where a shokunin learns" against
`corpus/SOURCES.md`; paste outputs and exit codes; report rows by tier/status.

Lane `kotodama-shokunin`, HEAD `4ad26836552462d28a946ca3b067cab0b5ce3532` (declared base),
jj-colocated. All commands read-only; no lane file, index or jj state touched. No installs.

Tiers below are the registry's declared tiers, not an endorsement. Everything marked
`[INFERENCE]` is reasoning from observed bytes, not something a command printed.

## 1. Assigned command 1 — maintained validator

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
    --root /home/vgpnk/Projects/shokunin kotodama
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```
**exit 0.** No E-code and no W-code emitted, so E01–E12 and W01–W04 are all silent on the
landed registry (the tool prints `ok` only when every check is clean). `--today` defaults to
`date -u` = `2026-10-21`; the run is date-stable because every row's `opened` is
`2026-10-19` and no `recheck` cell is an ISO date.

## 2. Assigned commands 2–8 — the seven manual census commands

Run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, commands copied
verbatim from `CORPUS.md` (contract `## Census` block).

| # | command | stdout | exit |
|---|---|---|---|
| 1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `47` | 0 |
| 2 | awk `NF!=13` malformed-row count | `0` | 0 |
| 3 | awk tier histogram | `A=34 B=6 C=7` | 0 |
| 4 | awk status histogram | `mined=20 queued=22 rejected=5` | 0 |
| 5 | duplicate ids (`sort \| uniq -d`) | *(empty)* | 0 |
| 6 | enum + tier-inflation check | *(empty)* | 0 |
| 7 | mined rows whose `used-by` paths do not exist | *(empty)* | 0 |

Command 1 stdout verbatim: `47`. Command 3: `A=34 B=6 C=7`. Command 4:
`mined=20 queued=22 rejected=5`. Commands 5–7 printed nothing (the required outcome);
each exited 0 because the last stage of the pipeline succeeded.

## 3. Rows by tier/status (47 rows)

Cross-tab from the same row regex (`$5`=tier, `$9`=status):

| tier | mined | queued | rejected | total |
|---|---|---|---|---|
| A | 18 | 16 | 0 | 34 |
| B | 2 | 4 | 0 | 6 |
| C | 0 | 2 | 5 | 7 |
| **total** | **20** | **22** | **5** | **47** |

Membership:

- **A/mined (18)** — S001 S002 S003 S007 S016 S018 S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042
- **A/queued (16)** — S004 S005 S006 S010 S012 S014 S017 S019 S020 S021 S022 S023 S024 S025 S026 S027
- **B/mined (2)** — S008 S013
- **B/queued (4)** — S015 S044 S045 S046
- **C/queued (2)** — S009 S011
- **C/rejected (5)** — S028 S029 S030 S043 S047

Consequences visible in the numbers: there is **no** `C/mined` row, so W01 (tier-C mined
with non-`—` used-by) has no input; all 20 mined rows carry at least one `used-by` path, so
W03 has no input; the five rejected rows each carry a `REJECTED:` `teaches`, so W02 is silent.

## 4. Corroboration (extra, read-only)

**Maintained `census` mode, same lane** — counts agree with the manual commands:
```
$ scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotodama
kotodama	rows	47
kotodama	tier.A	34
kotodama	tier.B	6
kotodama	tier.C	7
kotodama	status.mined	20
kotodama	status.queued	22
kotodama	status.rejected	5
FLEET	rows	47
FLEET	tier.A	34
FLEET	tier.B	6
FLEET	tier.C	7
FLEET	tier.invalid	0
FLEET	status.queued	22
FLEET	status.mined	20
FLEET	status.rejected	5
FLEET	status.invalid	0
FLEET	missing	0
```
exit 0.

**Recorded baseline agrees.** `reports/round-50/telemetry/census-before.txt` contains the same
validator line and `exit=0`, plus `rows=47 at base 4ad2683 (round start 12:08 -03 run
identical)` — the round's recorded before-state reproduces byte-for-byte.

**Tool selftest.** `scripts/sources-census.sh selftest` → `selftest ok`, **exit 0**;
tally over its output: `killed 96`, `SURVIVED 0` (no mutant survived).

**Overdue queue (not assigned; shows why "green" is not "fresh").**
```
$ scripts/sources-census.sh overdue --root /home/vgpnk/Projects/shokunin kotodama --today 2026-10-21
kotodama	cadence	S001 recheck=on-release opened=2026-10-19
... (one `cadence` line for each of the 47 rows) ...
kotodama	cadence	S047 recheck=365d opened=2026-10-19
```
exit 0. Every row is on a symbolic/relative cadence and every `opened` is the single date
`2026-10-19`, so the overdue leg is structurally inert for this lane today: it can never
report anything. A green overdue run must not be quoted as freshness evidence.

## 5. Calibration probes — do the gates actually fire on a round-50 row?

Synthetic registry in a temp dir (`/tmp/scout-census-probe2-*`), temp `corpus/knowledge`
symlinked to the lane's, rows injected **inside `## Registry`** before `## Paths`, then the
validator plus the relevant manual commands were run. Lane bytes untouched. Every mutant
was caught; the clean control stayed green:

| synthetic S048 row | validator | manual command |
|---|---|---|
| queued, unique URL, `—` used-by, opened `2026-10-21` | `probe-shokunin ok …` exit **0** | rows `48`; malformed `0`; dups empty; enum empty; used-by empty |
| mined, `used-by` names the not-yet-landed pastoralism entry | `E11 S048 missing used-by corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` exit 1 | cmd 7 prints `missing: …` |
| `community` at tier A | `E10 S048 community-at-A` exit 1 | cmd 6 prints `tier-inflation S048` |
| duplicate id `S047` | `E03 S047 duplicate id` exit 1 | cmd 5 prints `S047` |
| extra `\|` inside a cell | `E01 S048 fields=12` exit 1 | cmd 2 prints `1` |
| `opened 2026-11-01` (future) | `E08 S048 opened=2026-11-01` exit 1 | — |
| row appended **after** `## Paths` (first probe attempt) | `E12 S048 row outside Registry section` exit 1 | — |

Two operational readings: (a) `opened 2026-10-21` is accepted today, so round-50 rows can
carry the real access date; (b) a mined row whose `used-by` path does not yet exist is red, so
the registry rows and the entry that they name must land in the same tree — a validate run
between them reports E11.

## 6. Findings

**F1 — Baseline is census-green and reproducible.** 47 rows, exit 0, matching the round's own
`telemetry/census-before.txt` and the manual histograms. Fact, not inference.

**F2 — The provenance pointer is already one round stale.** `corpus/SOURCES.md:8` says the
round lesson's `## Gate` is `lessons/round-49.md` **for S001–S043**, but the registry holds
S044–S047 and their Gate bullets exist at `corpus/lessons/round-49.md:79–82`. The same stale
range appears in the lesson frontmatter at `round-49.md:6` (`scope: … S001–S043`) and in the
body at `round-49.md:20` ("Every row … S001–S043"), while the lesson's own mistakes table at
`:308–309` cites "Gate S044–S046". No census command can see this: the validator parses rows
and headings only. For claim C's frontier step, the header pointer must be extended to the
true span when S048+ land — a second pointer sentence that also stops at the old id would
reproduce the defect.

**F3 — The round-49 validation runner cannot be reused unchanged for round 50.**
`reports/round-49/run-validation.py:49` pins `LESSON = "corpus/lessons/round-49.md"`,
`:46` pins `BASELINE = "c42d675"`, and `:209`
`opened_ok = … all(v == "2026-10-19" for v in opened_vals)` hardcodes the access date — a
round-50 row opened `2026-10-21` makes `opened_ok` false. `:220` also requires each id to have
a bullet matching `^- S0NN ` exactly inside the Gate section. [INFERENCE] Round 50 will write
its own runner; this list is the parameter set it must not copy verbatim.

**F4 — The citation check the claim needs does not exist in the census, in either direction.**
`usedby_findings()` (`scripts/sources-census.sh:538–570`) walks *registry rows → files on
disk* (`[ -e "$dir/$path" ]`). Nothing reads `corpus/knowledge/`; `grep -n knowledge
scripts/sources-census.sh` hits only the selftest fixture. So the census cannot tell you that
an entry cites an id that is still `queued`, nor that a row's `used-by` omits the entry that
cites it — yet claim C's `after_required` is exactly "every cited S-id resolves to a SOURCES
row whose `used-by` names the entry". The seven manual commands share the single direction.
Working acceptance command (difference must be empty), run from the lane root:
```sh
entry=corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
comm -3 \
  <(grep -oE '\bS0[0-9]{2}\b' "$entry" | sort -u) \
  <(awk -F'|' -v e="$entry" '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 \
      {id=$2;s=$9;u=$12; gsub(/[[:space:]]/,"",id); gsub(/[[:space:]]/,"",s); \
       if (s=="mined" && index(u,e)) print id}' corpus/SOURCES.md | sort -u)
```
Calibrated on the round-49 pair: for the hunting entry the cited set and the claiming set are
identical — `S031 S032 S033 S034 S035 S036 S037 S038 S039 S040 S041 S042`, difference empty.
(The command also catches ids cited in prose; [INFERENCE] the C seat may prefer to scope the
left side to the external-shelf block, at the cost of no longer catching prose drift.)

**F5 — Supersession drift is green to every census command.** S034, S038 and S039 sit at
tier **A**, status `mined`, `used-by` naming the hunting entry, while S044/S045/S046 are the
tier **B** `supersedes` rows that `QUALITY.md:29` (criterion 6) says to use instead of the
filed A tier. Observed statuses: `S034 tier=A status=mined … S039 tier=A status=mined`,
`S044 tier=B status=queued`, `S045 tier=B status=queued`, `S046 tier=B status=queued`. The
validator has no supersede-graph check, so a new entry that cites the superseded A rows is
census-green. For the pastoralism entry: if it reaches for Kelly 2013, Sahlins, or
Stephens–Krebs on optimality, it must cite **S044 / S045 / S046** at tier B, not
S034 / S038 / S039.

**F6 — Where the numbers will move.** Any new row changes `rows`, the tier histogram and the
status histogram by exactly its own count; `FLEET` mirrors the single selected lane because
only `kotodama` was named. With S048+ as `queued` rows the post-step expectation is
`rows=47+n`, `A+B+C` unchanged in shares but larger in absolute, and `mined` unchanged unless
the new entry's citations flip those rows to `mined` (which claim C requires, F4).

**F7 — Tier-A share is the observed failure mode to watch, not a defect.**
34/47 = 72.3% of rows are tier A, 18 of them `mined`. `QUALITY.md:29` reserves A for
"primary or authoritative for the exact scope"; round 49 already corrected three
publisher-page rows from A to B via S044–S046. [INFERENCE] the pastoralism rows will be
graded by an outside check on this exact axis (publisher blurb vs. primary), so each new A
needs a scope where the source is primary, not a scope it merely summarises.

**F8 — Row placement matters.** A registry row appended after `## Paths` is E12-red (probe,
§5). Append inside `## Registry`, after S047 and before `## Paths`.

**F9 — Freshness is uniform.** All 47 rows opened `2026-10-19`; the registry has never
recorded a second access date. The round-50 rows are the first with `opened 2026-10-21`, which
is also the date the Gate quotes must carry.

## 7. What the frontier step must satisfy, census-verifiable

1. Next unused id is **S048**; ids contiguous upward, never reused (E02/E03).
2. Cell rules: no `|` inside any cell (E01), `kind` in the ten-value enum, `tier` in A/B/C,
   `community` never A (E05/E06/E10), `status` in `queued|mined|rejected` (E07).
3. `opened 2026-10-21` accepted (E08 probe, §5); `recheck` an ISO date, `NNd`, or a symbolic
   cadence (E09).
4. Rows the entry cites must be `mined` with `used-by` naming
   `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`, and the entry must
   exist in the same tree (E11 + F4).
5. `corpus/lessons/round-50.md` needs one `- S0NN — URL — accessed 2026-10-21 — "<verbatim
   ≤25-word quote>" <location>. Grounds: …` bullet per new row (F3's `^- S0NN ` regex);
   `corpus/lessons/round-50.md` **does not exist yet** — `ls corpus/lessons/ | grep -c
   round-50` → `0`.
6. Post-step green: validator exit 0; manual commands → rows `47+n`, malformed `0`, duplicate
   ids empty, enum empty, missing-used-by empty; F4 difference empty.
7. Extend the `corpus/SOURCES.md:8` provenance pointer and the round-49 lesson's stale
   S001–S043 range (F2) — or state explicitly that the pointer now reads "S001–S047 in
   `round-49.md`, S048+ in `round-50.md`" so the two spans are auditable.

## 8. Unrun checks

- No external URL was opened this session; the census scope asked for none.
- Fleet-wide default `census` (every lane) not run — only lane `kotodama` was named, and the
  selftest already exercises roster discovery on fixtures.
- `overdue` was run as corroboration only; its `--today` judgment is inert (§4).
- The round-50 validation runner does not exist yet: `reports/round-50/` holds `claims.json`
  and `telemetry/` only; `reports/round-50/separability/` and `reports/round-50/build/` were
  absent/created by this report.
- Claims O and Ca gates (`tools/harness/receipt_guard.py`, `tools/check-readme-revisions.py`,
  `tools/check-claim-separability.py`) untouched — not this seat's question.
- No git/jj mutation, no `git add/commit/checkout`, no lane edit. Temp probe dirs lived under
  `/tmp` and were removed after the run.

## 9. Installs

None. No tool was installed or upgraded for this task.
