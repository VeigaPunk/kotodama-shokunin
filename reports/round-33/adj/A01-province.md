- Seat: A01 | executor | claim A | date 2026-10-19 | baseline 139e3b6

# A01 — PROVINCE accuracy check at HEAD

**Assignment (targets.json A01):** `git log -- PROVINCE.md` (last touch vs the
c53782a claim), re-read `PROVINCE.md` vs the current tree (owns/refuses lists
still accurate), verdict + evidence.

**Snapshot:** `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T03:53:56Z`;
`git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb` (== declared
baseline in `reports/round-33/claims.json:8`). All commands run at the lane
root, read-only.

## Check A01-1 — last-touch claim vs live history — PASS (with one precision correction)

The claim under test, quoted from the round-32 dossier:

> `PROVINCE.md` is unchanged since before the fleet rounds: `git log --
> PROVINCE.md` shows its last commit as `c53782a` (supplement-opencode-1,
> 2026-10-17) — 31 lines, byte-stable across all 32 rounds.
> — `reports/round-32/dossier-d11-shonen-boxes.md:192-194`

Re-measured at HEAD:

| probe | command | result |
|---|---|---|
| last touch | `git log --oneline --pretty='%h %ad %an %s' -- PROVINCE.md` | `c53782a 2026-10-17 kotodama-shokunin supplement-opencode-1: recheck sources and harden reproducible evidence`; only other row `a527120` (mint) |
| exact timestamp | `git log -1 --format='%H%n%ad' -- PROVINCE.md` | `c53782ab875e88d7311c8b9b1db310357b944685`, `Sat Oct 17 13:09:14 2026 -0300` |
| blob identity | `git rev-parse HEAD:PROVINCE.md` / `git rev-parse c53782a:PROVINCE.md` | both `313b182f251564b7997b06996b4f063370778f11` |
| no drift since | `git diff c53782a HEAD -- PROVINCE.md` | empty (exit 0) |
| live bytes | `sha256sum PROVINCE.md`; `wc -c -l PROVINCE.md` | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`; 31 lines, 1636 bytes |

**Verdict: PASS — the c53782a last-touch claim and the 31-line / byte-stable
claims re-verify at HEAD.** 79 commits separate `c53782a` from HEAD
(`git rev-list --count c53782a..HEAD` → 79) and none touches the file.

**Correction to the "pre-round-8" phrasing (`reports/round-33/claims.json:57`).**
The tighter true bound is **pre-round-5**, not pre-round-8: `c53782a`
(13:09:14-03:00) postdates round 4's admit commit `fe34faa` (12:19:35-03:00)
and predates the first round-5 preparation commits (`c52f2c0` 13:16:19,
`2c66f77` 13:22:58) and round-8's declare commit `cf338a7` (17:10:35). So the
declared claim is true but understated; the dossier's own "unchanged since
before the fleet rounds" (d11:192) is the over-stated side of the same fact —
`c53782a` *is* a fleet-era commit (rounds 1-4 were already closed when it
landed). Neither phrasing is wrong for the use it is put to (the file has not
moved across rounds 5-32); the precise form is: **last touched after round 4,
before round 5.** Owner for adopting the tighter wording in future restatements:
integrator (dossier text only; no file change owed).

## Check A01-2 — `Owns` list vs the live tree — PASS

`PROVINCE.md:9-14` claims the generative/coupling craft and its records:
`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`,
the lane's own gates, source-check records, non-canon examples and reports.

| claim | live measurement | verdict |
|---|---|---|
| six named partitions | `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d` → exactly those six, no seventh | PASS |
| partitions populated | md-file counts per partition: linguistics 21, myth-symbol 19, culture-material 18, synthesis 29, verification 20, civilizations 94 (the 19/19/18/29/20/94 census in `corpus/README.md:95` is a *previous revision's* reading; current totals are one/two higher per partition — a stale-prose item for the README owners, not a PROVINCE defect) | PASS |
| own gates | `ls tools/gates/` → 12 gate scripts + `frozen/` + `expected/` + `fixtures/` | PASS |
| source-check records | `corpus/lessons/supplement-opencode-1/sources/` (tracked, 13 JSON files in that tree per `c53782a` stat) | PASS |
| non-canon examples | `examples/` → `culture-d2/`, `culture-d3/`, `culture-d4/`, `supplement-opencode-1/`, `handoff-packet.sample.{md,yml}`; every entry sampled carries an explicit non-canon stamp (`examples/handoff-packet.sample.md:3,15`; `examples/culture-d3/handoff.md:3,20`; `examples/culture-d2/ASSEMBLY.md:3`) | PASS |
| reports | `reports/` present (1857 tracked files; the bulk of the repo) | PASS |
| verification/civilizations caveat | `PROVINCE.md:12-14` limits those two partitions to linguistic-cultural coupling; both partitions' index prose repeats "Reference knowledge and method only; canon decisions belong to lore-shokunin" (`corpus/README.md:131,138,139,144` sampled) | PASS |

## Check A01-3 — `Refuses` list vs live in-lane content — PASS

| refusal (`PROVINCE.md:16-20`) | probe | result |
|---|---|---|
| canon — lore's | `corpus/README.md:121` "Canon lives with lore-shokunin."; `corpus/knowledge/verification/internal-consistency-audit.md:149` "lore owns canon choices and world-bible verification" | routed, not absorbed — PASS |
| real-world rights/attribution rulings | `corpus/knowledge/synthesis/source-discipline-calibration.md:29` "this lane does not issue rights or attribution rulings"; `corpus/knowledge/verification/provenance-audit-ledger-format.md:207` disclaims the same | disclaimed in-lane — PASS |
| game mechanics (game-dev-2d/3d) | `git ls-files \| grep -ciE 'game\|rpg\|mechanic'` → 0 | PASS |
| general source-research method (chousa) | `internal-consistency-audit.md:149` routes "unresolved historical sourcing … to chousa" | routed — PASS |
| web publishing (kake) | `git ls-files \| grep -cE '\.(html\|css\|js)$'` → 0 | PASS |
| prompt/skill craft (kotoba) | the lane's own `SKILL.md` exists, but its frontmatter declares the refusal itself: "Anti-trigger: … NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin), NOT real-world rights/attribution rulings" (`SKILL.md:3`). Lane-operating craft rules ≠ kotoba's cross-lane skill craft | PASS |

No in-lane artifact was found that decides a refused matter; the two sampled
declarations that touch rights explicitly disclaim the ruling.

## Check A01-4 — write-scope statement vs observed surfaces — PASS

`PROVINCE.md:27-29`: "Only writes this standalone lane repository
(`kotodama-shokunin/`), its own fleet round reports, and allowed append-only
L0 questions."

- lane repo: this file and the rest of `reports/round-33/` — in-lane (own write).
- fleet round reports: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-32/kotodama.md` present (7541 bytes, mtime 2026-10-18 22:01); `.ufo/reports/round-33/` does not exist yet — expected, the round-33 fleet report is filed at round close, not by seats (no defect).
- L0 questions: `.ufo/l0-questions.md` (38356 bytes) carries exactly 4 kotodama rows, lines 44-47 (rounds 2, 8, 9, 11) — append-only surface, unchanged this round by me.
- no out-of-lane write by this seat; my only write is this fragment.

## Check A01-5 — cross-seat observation, routed (not my verdict)

Filed-round bytes were modified **in the working tree during this wave**:

```
$ git status --porcelain          # at ~03:50Z → 3 entries
 M LOG.md
?? REGIMEN.md
?? reports/round-33/
$ git status --porcelain          # at 03:53:56Z → 5 entries
 M LOG.md
 M reports/round-5/validation.json
 M reports/round-7/validation.json
?? REGIMEN.md
?? reports/round-33/
$ stat -c '%y %n' reports/round-5/validation.json reports/round-7/validation.json
2026-10-19 00:54:15.802084688 -0300 reports/round-5/validation.json
2026-10-19 00:54:18.608932265 -0300 reports/round-7/validation.json
$ git diff --stat -- reports/round-5/validation.json reports/round-7/validation.json
 reports/round-5/validation.json | 4 ++--
 reports/round-7/validation.json | 2 +-
```

Diff content (read-only inspection): the claim-O `error` text in round-5 is
replaced by a `tools/replay-frozen.py … gate_digest_mismatch` could-not-evaluate
dump, and `tested_file_sha256."tools/check-gate-battery.py"` changes
`0a126b70…` → `455b595a…` in both files. `tools/check-gate-battery.py` itself is
**not** modified in the working tree (`git status` shows no entry for it), so
this is a re-run of round-5/round-7 validation against a *different* battery
revision than the one those receipts were filed with.

This is routed, not absorbed: owner **A03** (scope watch) and **X02**
(conformance) to judge whether a seat wrote filed-round bytes in violation of
`targets.json shared_rules[1]`, or whether an authorized integrator action
(round-23 precedent: `c64b2b3 "refreshed validation receipt (close-time,
receipt-guard REFRESH_RECEIPTS=1)"`) explains it. I did not touch those files
and did not revert them. It has no bearing on this fragment's verdicts:
`PROVINCE.md` is untouched by it.

**Follow-up, same session (~00:55 -0300 / 03:55Z):** the two entries are gone —
`git status --porcelain` is back to 3 entries (` M LOG.md`, `?? REGIMEN.md`,
`?? reports/round-33/`), so the filed bytes were restored to their committed
state within roughly two minutes. The finding is therefore *transient
filed-byte mutation during the wave, reverted*, not residual drift; the fact
that a write occurred at all still belongs to A03/X02's judgment, and no seat
should repeat it.

Minor, no owner required: an empty untracked directory tree
`kotodama-shokunin/reports/round-29/defects/` exists inside the lane
(`find kotodama-shokunin -type f` → no files; `git ls-files kotodama-shokunin/`
→ 0). In-lane, carries no content, invisible to git; optional cleanup by the
integrator, no PROVINCE impact.

## Verdict table

| check | verdict | basis |
|---|---|---|
| A01-1 last-touch = `c53782a`, 31 lines, byte-stable | **PASS** (precision correction: pre-round-5, not merely pre-round-8) | blob `313b182f…` equal at `c53782a` and HEAD; empty diff over 79 commits |
| A01-2 `Owns` list accurate | **PASS** | six partitions + gates + sources + non-canon examples + reports all live |
| A01-3 `Refuses` list accurate | **PASS** | 0 game-mechanics and 0 web artifacts; canon/rights/chousa disclaimed or routed in-lane |
| A01-4 write-scope statement accurate | **PASS** | fleet round-32 report present; 4 L0 rows; no out-of-lane write by this seat |
| A01-5 wave-time filed-byte mutation | **named finding, routed** to A03 + X02 (transient: reverted within ~2 min) | working-tree diff above; not my verdict |

**Net: `PROVINCE.md` needs no edit at HEAD.** No scope drift, no absorbed
out-of-province matter found in the sampled surfaces.

## Limits / to-verify

- Exhaustive per-file refuse-list audit of all 382 corpus files was **not**
  run by this seat (spot greps + partition index prose only); A04/A05/A08 own
  the bleed and corpus-partition legs, R07 reviews them.
- Handoff gate re-run is A02's leg; not re-run here.
- `corpus/README.md:95` partition census (19/19/18/29/20/94) vs live counts
  (21/19/18/29/20/94) is a stale-prose observation only — I did not measure
  which revision the README row intends; `to-verify` for the README owners.
- K04's method-scout fragment (`reports/round-33/adj/K04-method-scout.md`) did
  not exist at write time (`ls reports/round-33/adj/` → empty); this leg did
  not depend on it.

## Owed: none

## Citations

- `reports/round-33/claims.json:8` (baseline commit), `:20-38` (claim O),
  `:53-65` (claim A), `:57` (c53782a phrasing under correction)
- `reports/round-33/targets.json:48` (A01 mission), `:5-11` (shared_rules)
- `REGIMEN.md:25-50` (per-round contract)
- `reports/round-32/dossier-d11-shonen-boxes.md:192-194` (quoted last-touch claim), `:169`, `:208`
- `PROVINCE.md:1-31` (read in full; owns :9-14, refuses :16-20, adjacent :22-25, write scope :27-29)
- `corpus/README.md:95`, `:121`, `:131`, `:138-139`, `:144`
- `corpus/knowledge/synthesis/source-discipline-calibration.md:29`
- `corpus/knowledge/verification/provenance-audit-ledger-format.md:207`
- `corpus/knowledge/verification/internal-consistency-audit.md:149`
- `examples/handoff-packet.sample.md:3,15`; `examples/culture-d3/handoff.md:3,20`; `examples/culture-d2/ASSEMBLY.md:3`
- `SKILL.md:1-3` (frontmatter anti-triggers)
- Commands (lane root, 2026-10-19T03:53:56Z snapshot):
  - `git rev-parse HEAD`; `git rev-list --count c53782a..HEAD` (79); `git merge-base --is-ancestor c53782a HEAD` (yes)
  - `git log --oneline --pretty='%h %ad %an %s' -- PROVINCE.md`; `git log -1 --format='%H%n%ad%n%an%n%s' -- PROVINCE.md`
  - `git rev-parse HEAD:PROVINCE.md`; `git rev-parse c53782a:PROVINCE.md`; `git diff c53782a HEAD -- PROVINCE.md` (empty)
  - `sha256sum PROVINCE.md`; `wc -c -l PROVINCE.md` (1636 bytes / 31 lines)
  - `git log --format='%h %ad %s' --date=iso-strict` filtered for rounds 4-8 declare/prep commits
  - `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d`; per-partition `find … -name '*.md' | wc -l`
  - `ls tools/gates/`; `ls examples/`; `git ls-files | awk -F/ '{print $1}' | sort | uniq -c`
  - `git status --porcelain` (twice, ~03:50Z and 03:53:56Z); `stat -c '%y %n' reports/round-5/validation.json reports/round-7/validation.json`; `git diff --stat` + `git diff -- reports/round-5/validation.json`
  - `git ls-files | grep -cE '\.(html|css|js)$'` (0); `git ls-files | grep -ciE 'game|rpg|mechanic'` (0)
  - `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-32/`; `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-33/` (absent); `grep -n -i 'kotodama' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` (lines 44-47)
  - `find kotodama-shokunin -type f` (none); `git ls-files kotodama-shokunin/` (0)
  - `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-19T03:53:56Z`
