# ExecCCounter — claim-C counter draft (round 73, w1)

Seat: ExecCCounter (leaf). Scope: draft the claim-C acceptance counter, run its
selftest, and run it at `lands = base`. Nothing else was written; no claim text,
registry, lesson or scratch file of another seat was touched.

## Files

| path | state | sha256 |
|---|---|---|
| `.ufo/waves/round-73/counters/accept-c.py` | new, 1548 lines, `-rwxr-xr-x` | `de7a5c64ee120dde77ceb17e4bfb0ab425162c2e101932fc4d80df9fd83bcfea` |
| `.ufo/waves/round-73/w1/ExecCCounter.md` | this report | — |

Source adapted: `reports/round-72/accept-c.py` (read whole, 803 lines). The
round-73 draft keeps its leg names and its `git show`-free reading model but
changes the run model to QUALITY 19 (required `--lands`, materialized tree) and
widens four predicates the round-73 claim text adds (inline ids, used-by
exactly-the-citing-entries, reject-row URL, staged-as-is markers).

## Run model (QUALITY 17/19)

- `--lands <40hex>` is **required**; a missing/malformed/unknown revision exits
  2 (`ERROR: --lands must be a 40-hex commit (the worktree is never graded,
  QUALITY 19)`, `ERROR: --lands revision not found: ...`). Exit codes observed:
  `no-lands rc=2`, `unknown-rev rc=2`.
- Both `<lands>` and `<base>` are materialized with
  `git -C <lane> archive --format=tar <rev> | tar -x -C <tmp>/<lands|base>`;
  every leg reads bytes from those trees. The only worktree read is the
  `claims.json` **config fallback** (disclosed on the receipt as
  `# config source: lane worktree: ...`).
- Read-only git against the lane supplies commit metadata only (`rev-parse`,
  `log <lands> -S`, `merge-base --is-ancestor`, `diff --quiet`, `cat-file -e`).
- Receipt header printed before the leg table:

```
# round-73 acceptance counter — claim C (conlang-scholarship assimilation)
# counter sha256 (self): de7a5c64ee120dde77ceb17e4bfb0ab425162c2e101932fc4d80df9fd83bcfea
# stamped revision: 8841ad3b896a0227674fa0725b818c999118046f
# evaluated revision: 8841ad3b896a0227674fa0725b818c999118046f
# measured revision (lane main): 8841ad3b896a0227674fa0725b818c999118046f
# tree: 17c286f5503426a6063a2279c3862fbf3a74c261
# base revision: 8841ad3b896a0227674fa0725b818c999118046f
# materialized: git archive of the stamped revision at /tmp/r73-lands-bo6qwcgt/lands
# worktree graded: no (leg bytes read only from the materialized tree)
# access date: 2026-10-25
# config source: lane worktree: no row_set/entries object (defaults)
# adopted rows: S876 S877 S878 S879 S880
# entries: corpus/knowledge/linguistics/conlang-scholarship.md ; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md
```

(All five labels QUALITY 19 names are present: `# stamped revision:`,
`# evaluated revision:`, `# measured revision (lane main):`, `# tree:`,
`# counter sha256 (self):`.)

## Leg table

`base` = the draft's result at lands = `8841ad3b...` (the do-nothing control).
`proved-failable-by` = the selftest mutant that makes that leg fail for the
reason named.

| leg | predicate at `<lands>` | base | proved-failable-by |
|---|---|---|---|
| ENTRIES | both configured entries exist, non-empty, header carries source / verified-at / recheck / ground / topic / gap-filled / sources / couples / scope | FAIL (both missing) | `drop_entry`, `junk_rows` |
| ROWS | registry diff base..lands adds exactly the configured set; ids contiguous from S876; each status `mined`; recheck a normalized cadence; no `\|` in the row; used-by == exactly the entries whose `source:` lines cite that id; union covers both entries; nothing else added/removed | FAIL (added=[]) | `staged_as_is`, `usedby_empty`, `row_gap`, `claims_narrow` |
| REPOINTED | every `source:` line has exactly one S-id ≥ S876 whose row exists and whose source-cell URL normalizes equal to the cited URL; every inline S-id ≥ S876 and present; S728/S769/S806 appear nowhere | FAIL (entries missing) | `repoint_url`, `campaign_id` |
| GATE | `corpus/lessons/round-73.md` `## Gate`: per adopted row an **admit** row with the row URL, `2026-10-25`, a ≤25-word quoted span, ≥5 non-empty cells; ≥1 admit and ≥1 reject; **each reject row carries its probed URL**; `reason`+`flip` present | FAIL (lesson missing) | `gate_quote`, `gate_reject_no_url`, `gate_no_admit` |
| REJECTS | lesson names refused staged S869/S894/S910 and the three refused staged files, and names the naming-systems / calendar / era / verification families on a line that says not adopted; refusal marker + reason + flip | FAIL (lesson missing) | `no_rejects`, `family_missing` |
| GROUND | `reports/round-73/telemetry/gap-sweep.txt` names an `N-row` registry with N == the base registry's row count (799 pinned when `--base` is the claim base) and a `0` per URL fragment; independently: base registry source cells hold none of the five fragments and the base tree holds no `*conlang-scholarship*` file | FAIL (receipt missing) | `ground_zero` |
| CITEDLINES | `tools/check-cited-lines.py` from the materialized tree over both entries prints exactly `CITED-LINES: 0 finding(s) in 2 file(s)` | FAIL (entries missing) | `multi_id_line` |
| CENSUS | `sources-census.sh validate --root <tmp-fleet> --today 2026-10-25 kotodama` exits 0 with `kotodama\tok\t...` and no `E\d\d` line, the tmp fleet's `kotodama-shokunin` being a symlink to the materialized lands tree | **PASS** (exit 0, 799-row base registry) | `census_fail` |
| SCRATCHMIRROR | `.ufo/waves/round-73/assimilation/validate-receipt.txt` shows `--file`, `exit 0`, every adopted id; its introductory commit is strictly before the registry-append commit for the first adopted id, both reachable from `<lands>` | FAIL (receipt missing) | `receipt_no_exit`, `receipt_in_append` |
| COLLCHECK | reg-ids holds no adopted id; collisions holds no adopted id; a guard-proof file shows a 1–3-space-indented planted (non-adopted) row plus `collision` plus a detection marker; a regenerated map (`.ufo/.../id-renumber-map.json` or `-draft.json`) maps old→new for every adopted id, never old == new, every old in staged-ids, `supersedes` naming the round-71 map; the round-71 map's bytes are unchanged base..lands | FAIL (id files absent at base) | `collisions`, `guard_missing`, `map_missing` |

## Base run (do-nothing control) — exercised

```
$ python3 -B .ufo/waves/round-73/counters/accept-c.py --root . \
    --lands 8841ad3b896a0227674fa0725b818c999118046f
...receipt header as above...
LEG FAIL ENTRIES
     corpus/knowledge/linguistics/conlang-scholarship.md missing; corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md missing
LEG FAIL ROWS
     added=[] (want ['S876', 'S877', 'S878', 'S879', 'S880']); ... S876 row missing; S877 row missing; S878 row missing; S879 row missing; S880 row missing; used-by union [] ...
LEG FAIL REPOINTED
     corpus/knowledge/linguistics/conlang-scholarship.md missing; ...amend-2026-10-23.md missing
LEG FAIL GATE
     corpus/lessons/round-73.md
LEG FAIL REJECTS
     corpus/lessons/round-73.md
LEG FAIL GROUND
     receipt missing: reports/round-73/telemetry/gap-sweep.txt
LEG FAIL CITEDLINES
     corpus/knowledge/linguistics/conlang-scholarship.md missing; ...amend-2026-10-23.md missing
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r73-fleet-1_ahevvr/kotodama-shokunin/corpus/SOURCES.md
LEG FAIL SCRATCHMIRROR
     receipt missing: .ufo/waves/round-73/assimilation/validate-receipt.txt
LEG FAIL COLLCHECK
     collision id files missing under .ufo/waves/round-73/assimilation
ACCEPT-C-73: FAIL legs=1/10
EXIT=1
```

Only CENSUS passes at base, which is correct and is the reason it is not a
vacuous leg: the base registry is a valid 799-row registry, so the census
validator must accept it; every claim-C artifact is absent at base.

## Selftest — exercised

`$ python3 -B .ufo/waves/round-73/counters/accept-c.py --selftest` →
`SELFTEST: 25/25`, exit 0, wall 2.6 s, zero fixture directories left in `/tmp`
(each fixture is `mktemp -d` + `git -C "$D" init -q`; commits use
`-c user.name=selftest -c user.email=selftest@local` scoped to that repo only;
the census stub lives inside the fixture).

Cases (25):

1. clean fixture → `ACCEPT-C-73: PASS legs=10/10` and the receipt stamps lands;
2. do-nothing control `--lands <base>` → FAIL;
3. missing `--lands` → exit 2 naming `--lands`;
4. claims.json `row_set`/`entries`/`rejects`/`ground` at lands → PASS 10/10 with
   `# config source: lands tree: row_set, entries, ...`;
5. claims.json `row_set` narrowed to S876..S879 → `LEG FAIL ROWS` (config is not
   decorative);
6–25. mutants, each asserted to end `ACCEPT-C-73: FAIL` **and** to fail its
   mapped leg: `drop_entry`→ENTRIES, `staged_as_is`/`usedby_empty`/`row_gap`
   →ROWS, `repoint_url`/`campaign_id`→REPOINTED, `gate_quote`/
   `gate_reject_no_url`/`gate_no_admit`→GATE, `no_rejects`/`family_missing`
   →REJECTS, `ground_zero`→GROUND, `multi_id_line`→CITEDLINES,
   `census_fail`→CENSUS, `receipt_no_exit`/`receipt_in_append`→SCRATCHMIRROR,
   `collisions`/`guard_missing`/`map_missing`→COLLCHECK, `junk_rows`→ENTRIES.

Failure details were inspected for every mutant, not only the leg name; e.g.
`receipt_no_exit` → `receipt does not show exit 0`, `receipt_in_append` →
`receipt committed in the append commit (not before)`, `collisions` →
`S876 listed in collisions`, `guard_missing` → `no indent-guard proof under
.ufo/waves/round-73/assimilation/guard-proof (planted 1-3-space collision with a
detection marker)`, `map_missing` → `no regenerated renumber map (...)`,
`staged_as_is` → `S876 row carries an escaped pipe (staged text appended as-is);
S876 recheck='180d — \`curl ... \\' not a normalized cadence; ...`.

## Leg parameters from claims.json

Read from the claim object with `id == "C"` first, then the document root; the
lands tree is preferred over the lane worktree, and the receipt names which one
supplied the configuration. Recognised keys:

- `row_set`: list of `S-id` strings, list of `{"id": ..., "staged": ...}`,
  `{"ids": [...]}`, or `{"S876": {"staged": "S881"}, ...}`;
- `entries`: list of paths, `{"paths": [...]}`, or `{"entries"/"amendments"/
  "canonical": ...}`;
- `rejects`: `refused_staged` / `unreachable_staged`, `refused_files`,
  `families`, `forbidden_ids`;
- `ground`: `fragments`.

The current DRAFT carries none of these, so the defaults apply: rows
S876..S880, entries `conlang-scholarship.md` +
`conlang-scholarship.amend-2026-10-23.md`, forbidden ids S728/S769/S806,
refused staged S869/S894/S910, families naming-systems / calendar / era /
verification, five URL fragments.

## Predicate ambiguities for the attack seats

Each item is a place where the claim text admits more than one reading and the
draft picked one. All are cheap to re-freeze.

1. **CENSUS command shape.** The claim says
   `sources-census.sh validate --root <fleet-root> kotodama` "at the registry
   bytes of `<lands>`". Grading the real fleet root would grade the worktree
   (forbidden by QUALITY 19). The draft synthesizes a temp fleet root
   (`shokunin.conf` + `kotodama-shokunin → materialized tree`) and runs the
   claim's exact command shape against it, plus `--today 2026-10-25` for
   determinism. Attack: is a synthesized root acceptable, or must the claim
   instead spell `validate --file <materialized>/corpus/SOURCES.md`?
2. **ROWS contiguity.** "ids continue from S876 upward" is implemented as a
   contiguous run starting at 876. If wave 1 drops a middle candidate, the
   freeze must renumber the surviving rows contiguously (or add a config that
   says otherwise) — the counter will not accept S876, S877, S879, S880.
3. **ROWS used-by derivation.** "used-by naming exactly the admitted entries
   that cite it" is derived **only from `source:` header lines**. A row cited
   inline but not in a `source:` line will show an empty used-by and fail; a
   row whose used-by names an entry that cites it only inline fails too.
4. **ROWS staged-as-is markers.** Three markers are checked: `\|` anywhere in
   the row, a recheck cell that is not `NNd` / ISO date / symbolic cadence, and
   a used-by set other than the citing entries. Deliberately **not** checked:
   `opened == 2026-10-25` (the claim never states it; a scribe may legitimately
   keep an earlier opened date). If the round wants the staged `2026-10-23`
   opened cell treated as an as-is tell, that must be added at freeze.
5. **REPOINTED URL equality.** Comparison is normalized `(netloc, path)` exact
   match between the cited URL and the row's source-cell URLs. A DOI-form
   citation (`https://doi.org/10.13135/2384-8987/7099`) will **not** match the
   `ojs.unito.it/...` row URL even though it names the same document; the row
   must carry the exact cited URL. The staged rows do carry the direct URLs, so
   this is a scribe constraint, not a blocker.
6. **REPOINTED inline ids.** The draft requires *every* inline S-id in the two
   entries to be an adopted row id. This is stricter than round 72 (source
   lines only). An admitted entry that also cites an older lane row (e.g. a
   pre-existing `conlang-methodology.md` S-id) would fail. The claim does say
   "every source: line **and every inline S-id**", so the draft takes it
   literally; attack if the intent was source lines only.
7. **GATE reject rows.** Each reject row must itself carry an `http(s)` URL
   (QUALITY 21's "every Gate reject records the URL it rejected"); a URL in a
   footnote or a paragraph after the table does not satisfy the row check.
   `reason` and `flip` are checked as tokens in the Gate section, not per row
   (round-72's reject table carries them only in the header).
8. **GATE "located".** "≤25-word located quote" is discharged structurally: the
   admit row must have ≥5 non-empty cells (source+URL, date, quote, locator,
   verdict). There is no semantic check that the locator names a heading or
   page. Word count is whitespace tokens (CJK/Cyrillic per token, per the wave
   brief); straight quotes, curly quotes, guillemets and 「」 all count.
9. **REJECTS conditionality.** The claim makes S894/S910 rejects conditional on
   "their payload stays unreachable by ordinary means". The draft defaults to
   the claim's named set (S869 + S894 + S910 and the three staged files). If
   wave 1 finds S894/S910 reachable, the freeze must add
   `rejects.refused_staged` / `rejects.refused_files` to claims.json, or the
   counter will fail a correct lesson. This is the single most likely
   freeze-time conflict.
10. **REJECTS families.** Each family token must sit on a line that also says
    `not adopted` / `no adoption` / `not admitted`. A lesson that lists the
    families in one paragraph and says "not adopted this round" in another
    fails. (`era` is matched as a whole word, `naming-systems` also accepts
    `naming systems`.)
11. **GROUND receipt shape.** The receipt must contain a `\d+` immediately
    followed by `-row` or ` row` (e.g. "799-row registry") and, for each of the
    five fragments, a standalone `0` on the same line or within the next two
    lines. A receipt that pastes `grep -c` output without repeating the pattern
    on the same line, or writes "rows: 799", fails. The counter also re-derives
    the sweep from the base tree, so the receipt is corroboration, not the only
    evidence.
12. **GROUND count pin.** `799` is required only when `--base` equals the claim
    base; otherwise the receipt's N must equal the base registry's actual row
    count (this is what lets the selftest run on small fixtures without
    weakening the claim-base check).
13. **SCRATCHMIRROR commit identity.** The append commit is the oldest commit
    reachable from `<lands>` that changes the occurrence count of the first
    adopted id in `corpus/SOURCES.md` (`git log <lands> -S <first> -- ...`); the
    receipt's introductory commit is the oldest `--diff-filter=A` commit for the
    receipt path. A later edit of the receipt does not move the introduction
    point, and the check requires `intro != append` plus
    `merge-base --is-ancestor intro append`.
14. **COLLCHECK collisions contents.** The collisions file may list non-adopted
    ids (it currently lists S859..S875 from the staged/lane namespace overlap);
    only adopted ids are forbidden there. `staged-ids` is **not** required to
    contain the adopted lane ids — the two namespaces overlap numerically and
    requiring that would be the arithmetic-join defect the wave is attacking.
    What is required: if claims.json supplies a staged→lane mapping, those
    staged ids must exist in staged-ids.
15. **COLLCHECK map.** Either `id-renumber-map.json` or
    `id-renumber-map-draft.json` is accepted (the draft file currently present
    satisfies the predicate: S881→S876, S882→S877, S892→S878, S893→S879,
    S901→S880, `supersedes` names the round-71 map). `old == new` is rejected
    as the arithmetic-join class. The round-71 map's bytes are required
    unchanged base..lands (`git diff --quiet`).
16. **COLLCHECK guard proof.** Any file under
    `.ufo/waves/round-73/assimilation/guard-proof/` counts if it shows a
    1–3-space-indented row for a **non-adopted** id, the word `collision`, and a
    detection marker (`exit 1`, `fail`, `detected`, `non-empty`, `SURVIVED`,
    `killed`). The planted id must not be an adopted id.
17. **Config fallback reads the worktree.** When `<lands>` has no
    `claims.json`, the draft reads the lane worktree copy as *configuration* and
    discloses it. It is not a graded byte, but an attack seat may prefer that a
    lands run with no committed claims.json fall straight to defaults.
18. **CITEDLINES file count.** The leg requires the tool's own summary to name
    exactly the number of entry files present (`... in 2 file(s)`); a missing
    entry therefore fails two legs (ENTRIES and CITEDLINES), which is
    intentional redundancy, not double-counting in the verdict.

## What a passing lands must contain (checklist for scribes)

- the two entries with the nine-field header, every `source:` line one id
  ≥ S876 whose row URL matches, no S-id below S876 and no S728/S769/S806;
- five (or the frozen set) contiguous rows S876.. mined, recheck a bare cadence,
  no escaped pipes, used-by exactly the citing entries;
- `corpus/lessons/round-73.md` with `## Gate`: one admit row per adopted id
  (URL, 2026-10-25, ≤25-word quote, locator) and a reject table whose every row
  carries its probed URL, with reason and flip columns;
- `reports/round-73/telemetry/gap-sweep.txt` naming the 799-row registry with a
  0 per fragment;
- `.ufo/waves/round-73/assimilation/validate-receipt.txt` (`--file`, `exit 0`,
  the adopted ids) committed **before** the registry append;
- `reg-ids`, `staged-ids`, `collisions`, `guard-proof/*`, and the regenerated
  renumber map under `.ufo/waves/round-73/assimilation/`.

## Tooling and hygiene

- No tool installed or upgraded; nothing downloaded. Used the host `python3`
  3.14.8, `git`, `tar`, and the committed
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (read-only).
- No writes outside `.ufo/waves/round-73/counters/accept-c.py`,
  `.ufo/waves/round-73/w1/ExecCCounter.md`, and `/tmp` scratch
  (`/tmp/ExecCCounter-base.txt`, removed fixtures). `git status --short` shows
  only the pre-existing untracked entries plus the round-73 directories; the
  index and jj/git state are untouched. One `__pycache__` created by an ad-hoc
  debug import was removed; all later runs used `python3 -B`.

## Risks

- The default `rejects` set (ambiguity 9) is the most likely place for the
  counter to disagree with a wave-1 verdict that finds S894/S910 reachable.
- Ambiguities 3, 6 and 7 impose scribe-visible constraints that the claim text
  states only in prose; they are cheap to satisfy but must be read before the
  lesson is written.
- CENSUS is the only leg that passes at base; if the freeze changes the CENSUS
  command shape (ambiguity 1), re-run the do-nothing control before dispatch.
