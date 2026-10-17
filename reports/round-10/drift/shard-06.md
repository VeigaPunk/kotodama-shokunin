# Drift shard 06 — SKILL.md lines 101–120

- seat: R10-F06 (freshness drift re-runner, shard 06 of 13). This file is the
  seat's only write; no SKILL.md, SCORECARD, corpus, tool or sibling-repo byte
  was written or edited by it.
- date: 2026-10-17. Measurement clock: `2026-10-17T21:28:50Z` (local
  UTC-03:00). Lane revision at measurement: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  (`git rev-parse HEAD`); the round's declared `baseline_revision` is
  `9dc18ec1339bffd6f81e74f1a5742464ef578749`.
- scope of the shard (verbatim byte range): `sed -n '101,120p' SKILL.md`
  → sha256 `66835e325dcced20e153a5870a6fecaf7321a583a1e1f72d1b9ff2b4a13fb2e0`;
  whole file `SKILL.md` sha256
  `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`.
  Content: `## Boundaries (hard)` (SKILL.md:102–113) and the first two items
  of `## Checklist (executable)` (SKILL.md:115–120).
- shard-boundary notes, stated so nothing is silently dropped:
  - line 120 ends `…— see` and the cited path lands on SKILL.md:121
    (`synthesis/source-discipline-calibration.md`), outside this shard's byte
    range; it is one sentence, so it is evaluated here and flagged as
    boundary-spanning. Checklist items 3–4 (SKILL.md:122–125) belong to the
    shard holding lines 121–140 and are not re-measured here.
  - **Negative claim, with its sweep:** lines 101–120 contain no shell command
    and no URL. `sed -n '101,120p' SKILL.md | grep -o '`[^`]*`'` → no output
    (zero backticked tokens); `sed -n '101,120p' SKILL.md | grep -c
    'python3\|tools/\|git '` → `0`. The assignment's "web-only citations get a
    documented access attempt" clause is therefore vacuous for this shard:
    there is nothing to fetch. What the shard does carry is a path citation, a
    vocabulary claim, and five lane-boundary claims — each measured below.
- measured where: lane root, read-only commands; scratch under
  `$PWD/.scratch` (`export TMPDIR=$PWD/.scratch`; `/tmp` remains
  inode-exhausted per round 9). Kept receipts: `.scratch/pa-corpus.out`
  (sha256 `644c699890aa1b8be0a7cd3b4ca5260161eac1872e941a0b404c48571331c297`),
  `.scratch/pa-corpus.err` (empty; sha256 `e3b0c442…7852b855`),
  `.scratch/pa-sdc.out` (sha256 `57f88a1bb5ff58a24175f0dec3150573747a4f700fa44e17399752f0e7c2e85a`).
  `.scratch/` is untracked, disposable evidence, not a deliverable.

## 1. Drift rows

Verdict vocabulary: `current` (live surface matches the claim),
`stale-fixed` (fixed in this round, with evidence — **none in this shard**: the
seat's write scope is this file only), `stale-documented` (mismatch recorded
with a reason and a proposed patch for the F15–F18 fixers).

| # | locator | claim under test | command re-run (2026-10-17) | observed | exit | output sha256 | verdict |
|---|---|---|---|---|---|---|---|
| 06-A | SKILL.md:104–107 | canon authority is lore-shokunin's; this lane never edits the world bible or a sibling repo | `for d in lore-shokunin game-dev-2d-shokunin game-dev-3d-shokunin kake-shokunin chousa-shokunin; do [ -d "../$d" ] && echo "OK ../$d"; done` | all five printed `OK`; `../lore-shokunin` exists | 0 | (text) | current |
| 06-B | SKILL.md:108–109 | refuses real-world rights/attribution rulings | `ls corpus/knowledge/verification/real-world-inspiration-boundaries.md` | file present (13 files in `verification/`) | 0 | — | current |
| 06-C | SKILL.md:110 | refuses game mechanics (game-dev-2d/3d) and publishing (kake) | same dir sweep as 06-A | `../game-dev-2d-shokunin`, `../game-dev-3d-shokunin`, `../kake-shokunin` all exist | 0 | — | current |
| 06-D | SKILL.md:111–112 | refuses general research method — that is chousa-shokunin | same dir sweep as 06-A | `../chousa-shokunin` exists | 0 | — | current |
| 06-E | SKILL.md:113 | out-of-province evidence → report, never absorb | `cat PROVINCE.md` (read-only) | `PROVINCE.md:31` carries the line verbatim; `PROVINCE.md:16–20` lists the same refusals (canon, rights, game-dev-2d/3d, chousa, kake) plus kotoba (prompt/skill craft), which SKILL.md's frontmatter anti-trigger carries at `SKILL.md:3` | 0 | — | current |
| 06-F | SKILL.md:115 + :119–120 | header claims the checklist is executable; item 2 (myth/symbolic claims name framework + calibration status) | `python3 tools/gates/provenance-audit.py corpus/knowledge` | **exit 0**; `INFO scan: files=179 marks=618 mark-lines=612 findings=0 blocked=0`; one observation line `INFO calibration-prose-only: corpus/knowledge/synthesis/glossary-registry-format.md`; no `missing-calibration` finding anywhere | 0 | stdout `644c6998…31c297`; stderr `e3b0c442…7852b855` (empty) | current — item 2 is executable and green today; gate `tools/gates/provenance-audit.py` sha256 `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a` |
| 06-F′ | SKILL.md:119–121 (boundary-spanning) | the cited file resolves | `python3 tools/gates/provenance-audit.py corpus/knowledge/synthesis/source-discipline-calibration.md`; `sha256sum` the file | file exists, 39,493 bytes, sha256 `3cbc98b4266aea08d2e8b19513ee369b3f0c6727f16f3c40eafe44796f0e4e93`; gate run exit 0, `INFO to-verify-count … 5 mark(s) on 5 line(s)`, `findings=0` | 0 | stdout `57f88a1b…c2e85a` | current (path) |
| 06-G | SKILL.md:117–118 | "Every language system cites its typological basis (which real language family it draws on and why)" — under a header that says **executable** | `grep -rn "anchor.family\|anchor_family\|typological basis\|family named" tools/*.py tools/gates/*.py tools/harness/*.py`; `grep -rln typolog tools/ --include="*.py" \| grep -v frozen`; `grep -n -i "family\|typolog\|anchor" tools/gates/handoff-packet-check.py` | **0 matches** for the first sweep; the second returns only `tools/gates/phonology-sanity-gate.py` (typological *rarity* warnings, not typological-basis coverage); the handoff gate's single hit is a comment about hex-anchored digests (`handoff-packet-check.py:162`), not a field check. No gate or tool in this lane tests that a language system names its typological anchor | 1 (grep no-match) / 0 | (text) | **stale-documented** — the header's executability claim does not hold for item 1; the nearest surfaces are prose checklists: `corpus/knowledge/linguistics/conlang-methodology.md:151` ("anchor family named in the grammar header; typological passport complete…") and `corpus/knowledge/synthesis/worldbible-integration-contract.md:193` ("real typological inspirations separately cited") — both unchecked `[ ]` boxes, no executable |
| 06-H | SKILL.md:119–121 | calibration status vocabulary is "(mainstream / contested / discredited — see synthesis/source-discipline-calibration.md)" | `for w in mainstream contested discredited speculative rejected; do grep -o -i "$w" <file> \| wc -l; done` on the cited file; same on `corpus/knowledge/verification/calibration-registry.md`, `corpus/README.md`, `QUALITY.md`; `grep -rn "mainstream" corpus/knowledge/` | cited file: **mainstream 0**, contested 5, discredited 2, speculative 1, rejected 1. `verification/` partition: **mainstream 0** in every file. `corpus/README.md`: mainstream 0. `QUALITY.md`: mainstream 0. Corpus-wide, "mainstream" occurs only in entry prose (`historical-linguistics.md:215–216`, `language-contact.md:103`, `myth-ritual-theories.md:73`, `color-symbolism.md:28`, …), never as a declared status label. The cited file declares its **own** status set at `source-discipline-calibration.md:67`: "**S** supported within stated scope; **C** actively contested; **H** heuristic/generator; **R** rejected as stated or unsupported overclaim; **U** evidence does not presently decide; **V** = `(to-verify)`", and at `:94–95` it explicitly says "'Contested,' 'hard to test,' 'not established,' and 'discredited' are not synonyms" and warns against inheriting blanket "discredited" verdicts | 0 (counts) | (text) | **stale-documented** — the sentence cites a file whose declared vocabulary is not the three-value set it names, and whose text argues against using that set as one |

No other runnable surface exists inside the byte range: 0 commands, 0 URLs,
0 backticked tokens (sweeps in the header block above).

## 2. Stale items, dispositions, and proposed minimal patches

Neither stale row was fixed by this seat: R10-F06's write scope is this file
("write ONLY the files your assignment names"), and the round's fixers are
R10-F15..F18 (targets.json: take every stale item from the ledger, fix in
place with cited evidence or document why it stays stale). Both rows are
therefore handed forward as `stale-documented` **with** the patch text below
so the ledger and fixers can act without re-deriving the evidence.

### 06-G — "Checklist (executable)" header vs item 1

- Mismatch: the header at `SKILL.md:115` presents the whole list as
  executable; item 1 (`SKILL.md:117–118`, typological basis) has no
  executable in this lane (sweep above), while item 2 (`SKILL.md:119–121`)
  does, via `provenance-audit`'s `missing-calibration` family (`06-F`).
  Items 3–4 are outside this shard and are the 121–140 shard's rows.
- Proposed minimal patch (re-scope the header, one line, no behavior claim):
  `## Checklist (executable where a tool exists)` — with item 2 tagged
  ``(gate: `provenance-audit` `missing-calibration`)`` and item 1 left as an
  unchecked prose item. Alternative disposition: keep the header and treat
  item 1 as a coverage gap for a future operability round (a tool that reads
  a culture packet's grammar header for an anchor family). Either is
  defensible; the registry/ledger should record which was chosen.
- Why not fixed here: write scope (this file only); the fix is a SKILL.md
  edit and belongs to F15–F18 or the integrator.

### 06-H — calibration-status vocabulary mismatch

- Mismatch: `SKILL.md:119–121` names "(mainstream / contested / discredited)"
  and cites `synthesis/source-discipline-calibration.md`; that file (sha256
  `3cbc98b4…0e4e93`) carries "mainstream" **0×**, declares S/C/H/R/U/V at
  `:67`, and at `:94–95` rejects exactly the flat three-value reading the
  SKILL.md line implies. "mainstream" is used as prose in individual entries,
  not as a declared status anywhere in the corpus (`verification/`, README,
  QUALITY all 0×).
- Proposed minimal patch (make the sentence true without changing lane
  method): replace the parenthetical with the cited file's own set, e.g.
  `status (per-claim set S/C/H/R/U/V — see
  synthesis/source-discipline-calibration.md:67)`.
- Alternative patch (keeps two of the three words, re-points the citation):
  cite `corpus/knowledge/verification/internal-consistency-audit.md:165`,
  which instructs marking a framework "`local design convention`, `supported
  within stated scope`, `contested`, `discredited claim`, or `unverified
  (to-verify)` at claim level" — the corpus's operational marking rule, which
  contains "contested" and "discredited" but still not "mainstream".
- Note for the ledger: the citation *target* is the house convention
  (`conlang-methodology.md:158` also status-tags "per
  `source-discipline-calibration.md`"), so this is a vocabulary mismatch in
  the SKILL.md sentence, not a wrong file. The registry's `provenance-audit`
  row is unaffected: the gate accepts any calibration apparatus shape
  (heading / table-column / bold-label / labelled-line,
  `provenance-audit.py:90–96,268–278`) and is green corpus-wide (`06-F`).

## 3. What this shard does not claim

- Not a verdict on items 3–4 of the checklist (SKILL.md:122–125), on the
  Corpus map (SKILL.md:127–145), or on SCORECARD / round-9 registry rows —
  those belong to other shards. The 179-entry / 16-16-16-24-13-94 partition
  count measured incidentally here is context for the boundary rows, not this
  seat's coverage verdict.
- Not a fix: zero `stale-fixed` rows in this shard; both stale rows are
  `stale-documented` with evidence and patch text, and remain open for
  R10-F15..F18 and the ledger scribe (R10-F14).
- Not a content endorsement: `provenance-audit` exit 0 proves declared
  metadata shape, not scholarship; the tri-value vocabulary question is a
  documentation-vs-corpus mismatch, not a claim that any entry's calibration
  is wrong.
- Not a re-run of any command outside the shard's byte range, and not a claim
  about sibling repos beyond their existence and the text of `PROVINCE.md`.
