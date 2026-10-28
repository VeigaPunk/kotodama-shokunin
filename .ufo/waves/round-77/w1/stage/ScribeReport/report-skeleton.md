# Kotodama — round 77 (attempt 1)

<!--
DRAFT SKELETON ONLY — written by WAVE-1 seat ScribeReport.
The filed report is written by the L1 AFTER WAVE-DONE at
/home/vgpnk/Projects/shokunin/.ufo/reports/round-77/kotodama.md (fleet repo; no seat writes it).
Every <L1-FILL> below is a cell the L1 replaces with a measured value AND the command that produced it.
Do not file this file as-is: a report carrying unreplaced <L1-FILL> text or no evidence pointers is
contentless and counts as a failed round (round-prompt §4 marker rule).
Contract sections below are in the §4 order: Work performed; Landed changes; Before → after
measurements; Sources & frontier; Trend verdicts; SHONEN — then the addendum lines.
-->

Lane final pushed tip: <L1-FILL — full 40-hex hash> (`main`; `jj-lane.sh state` local=remote, ahead=0/behind=0; `git ls-remote origin refs/heads/main` returned the same hash). The report is filed only after WAVE-DONE for both waves.

## Work performed

Declared claims: **C — coverage** (one assimilation-sourced `linguistics/naming-systems` amendment: D1/S897 魏斌〈單名與雙名〉 and D2/S898 Kałużyńska 2025, Onomastica LXIX) and **Ca — calibration** (≥10-pair frozen ledger of stated-token/artifact mismatches in the round-75/76 and base records). Admission verdict: <L1-FILL — "C admitted / Ca admitted" or "neither claim is admitted", naming the frozen counter result>.

- Froze claims/ledger/counters at <L1-FILL — freeze commit>, ran the pre-data selftests and no-data controls, and verified the frozen leg set before data (LEGCOUNT). Evidence: <L1-FILL — command output path:line / commit / receipt path>.
- C: re-opened D1 and D2 this round under CORPUS.md rule 1 (own access date + ≤25-word located quote per row), added rows S897 (→D1) and S898 (→D2), landed exactly one entry `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`, and recorded the rejects with reasons + flips: `naming-systems.amend-2026-10-24.md` (S933 live text gone; S934 document-level duplicate of D2; S936 bibliography-bridge), `naming-systems.amend-2026-10-24-r10.md` (S939–S944, tier-C upload record pending S899/S900 resolution), `naming-systems.amend-2026-10-23b.md` (S906/S907/S911, different ground). Evidence: <L1-FILL — `corpus/lessons/round-77.md` `## Gate` line numbers; `reports/round-77/evidence/S897.txt`, `S898.txt`>.
- Ca: recorded the frozen ≥10 pairs' dispositions — ANNOTATE rows (id + old token + observed token + the pair's own re-derivation command) under `SCORECARD.md` `## Corrections — round 77`, REPAIR pairs on the frozen mutable set {corpus/README.md, SKILL.md, SHONEN.md} only; APPENDONLY and the rule-2 SOURCES exception left green. Evidence: <L1-FILL — `LOG.md:<n>`; `reports/round-77/ledger.json`; `reports/round-77/telemetry/measures-ca.txt`>.
- W2 review: <L1-FILL — one line per review finding with its fix and artifact path, or "no W2 finding required a change" with the reviewer artifact that says so>.
- Mistakes recorded: <L1-FILL — R77-M1..R77-Mn, one pointer each; candidates from the draft: R76-M3 successor (leg-list hygiene), L76-19 stated_text-absence class (now LEDGER-leg guarded), report-correction discipline (append-only errata), wave-design circularity (no seat reviews a pre-WAVE-DONE report)>.
- Controlled the claims: <L1-FILL — lands==freeze fails on the named data legs; lands==base refused exit 2; each J-series junk fixture fails its named leg; receipt paths>.
- Pre-report fleet-root misroot sweep: <L1-FILL — `git status --porcelain` at /home/vgpnk/Projects/shokunin and the disposition of any lane-seat note found outside the lane>.
- `considerthese/` is absent for this lane (verified `ls` at base: `ls: cannot access 'considerthese': No such file or directory`); no proposal available. Report line only.
- Tooling: `/home/vgpnk/.omp/agent/RULES.md` was read before work; <L1-FILL — tools installed/upgraded (tool, version, channel, reason) or "none">; pacman was not run.

## Landed changes

Every item is logged in `LOG.md:<L1-FILL — line range>`; all lane changes used the lane helper and the lane ends clean/pushed.

| Commit | Change |
|---|---|
| <L1-FILL — 40-hex> | F-series freeze: claims/ledger/counters, selftests, no-data controls, LEGCOUNT (`LOG.md:<n>`). |
| <L1-FILL — 40-hex> | Ca landing: ANNOTATE rows + REPAIR pairs; measured receipt (`LOG.md:<n>`). |
| <L1-FILL — 40-hex> | C landing: S897/S898 registry append, entry, README index row + footer, evidence captures, lesson Gate (`LOG.md:<n>`). |
| <L1-FILL — 40-hex> | W2 artifacts and review fixes (`LOG.md:<n>`). |
| <L1-FILL — 40-hex> | Close records, final counter restamp, census receipts (`LOG.md:<n>`). |

## Before → after measurements

- **C — coverage.** Counting commands (the commands the L1 runs; W1 re-derived the base cells with them at 253/820 — the values stay `<L1-FILL>` because the L1 re-measures and files them):
  ```sh
  for rev in 211f9526800906e0c585d878d265c37e5e090c15 <L1-FILL — C-lands>; do
    printf '%s knowledge=' "$rev"; git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only "$rev" corpus/knowledge | grep -c '\.md$'
    printf '%s rows=' "$rev"; git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show "$rev:corpus/SOURCES.md" | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  done
  ```
  Output: base `knowledge=<L1-FILL>, rows=<L1-FILL>`; C-lands `knowledge=<L1-FILL>, rows=<L1-FILL>` (DRAFT target 254 / 822). W1 re-derivation of the base cells with this exact command: 253 / 820 at `211f952` (`.ufo/waves/round-77/w1/ScribeReport.md` §1); the L1 re-derives and writes the values.
  Ground sweep, verbatim from CLAIMS-DRAFT (the draft's `211f952…` is expanded to the full base revision; this is a BASE-scope negative claim, so it is measured at the base, not at C-lands — at C-lands the adopted entry legitimately contains both URLs and the sweep is expected to print it):
  ```sh
  git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge
  ```
  Output: <L1-FILL — the command's output and exit code, stated with its scope>. W1 re-derivation at the base revision: empty output, exit 1 (no match); at C-lands the adopted entry is expected to print, which is not a leg failure (`.ufo/waves/round-77/w1/ScribeReport.md` §2).
  Frozen acceptance command (`accept-c.py` argv is not spelled out in the draft; this mirrors the round-76 invocation and the draft's argument set):
  ```sh
  python3 -B reports/round-77/accept-c.py --root . --lands <L1-FILL — C-lands> --freeze <L1-FILL — freeze> --fleet-root /home/vgpnk/Projects/shokunin --work /fast/scratch/hyaku/kotodama-r77/<L1-FILL — seat>
  ```
  Output: <L1-FILL — the exact `ACCEPT-C-77: PASS|FAIL legs=n/n` line and the receipt path in `reports/round-77/telemetry/>`. Leg set (draft verbatim, exact set frozen with the counter): FROZENCFG, STAMP, LEDGELIST?, COUNTS, ENTRIES, ROWS, APPENDONLY, COLLCHECK, INDEX, EVIDENCE, GATE, REJECTS, CENSUS, GROUND, RECEIPTS — the `LEDGELIST?` marker must be resolved to present/absent at freeze and reported as such.
  Routed-defect scope statements the report must carry: ROWS counts only `| S### |` row lines added inside the frozen row_set, with required non-row edits (Paths, Search log lines) enumerated in `required_sections[]` and checked by INDEX (r76 #1); COLLCHECK compares normalized document identity per the staged→lane map, not raw URL strings (r76 #2).
  End census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit <L1-FILL>; receipt `reports/round-77/telemetry/<L1-FILL>`.
- **Ca — calibration.** Frozen ledger: <L1-FILL — pair count and ANNOTATE/REPAIR split>. Command, verbatim from CLAIMS-DRAFT with the placeholder cells filled:
  ```sh
  python3 -B reports/round-77/accept-ca.py --root . --lands <L1-FILL — Ca-lands> --freeze <L1-FILL — freeze> --fleet-root /home/vgpnk/Projects/shokunin --combined <L1-FILL — C-lands> --main <L1-FILL — Ca-lands> --work /fast/scratch/hyaku/kotodama-r77/<L1-FILL — seat>
  ```
  Output: <L1-FILL — exact `ACCEPT-CA-77: PASS|FAIL legs=n/n` line, red legs, receipt path>. Leg set from the draft (final list frozen with the counter): LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, SEPARABLE, COMBINED, RECEIPTS, FROZENCFG, STAMP, LEDGELIST.
  Disposition bounds the report must state: ANNOTATE `stated_at` inside the frozen allowlist {LOG.md, SCORECARD.md, corpus/lessons/round-75.md, corpus/lessons/round-76.md}, `corpus/README.md` REPAIR-only; `stated_text` verified present in the BASE tree at ledger build; every `rederive`/observe_cmd is argv-executable with its executable in {git, grep, wc, sha256sum, ls, cat, head, tail, cut}; every cited telemetry receipt exists at the freeze; the COMBINED README exemption carries its required line number.
  Controls: lands==freeze red on REPAIR/ANNOTATE; lands==base refused exit 2; missing `--combined`/`--work` refused exit 2 printing no leg line; <L1-FILL — junk-fixture outcomes (constant printer, interpreter, shell string, dead pin, out-of-clone operand)>.

## Sources & frontier

`corpus/SOURCES.md`: <L1-FILL>→<L1-FILL> rows, counted at base `<L1-FILL>` and lands/close tree `<L1-FILL>` using `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`. Required census validation command, run at start and end: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit <L1-FILL> both; start receipt `reports/round-77/telemetry/census-start.txt`. <L1-FILL — declare what the start receipt itself records; it carries validate stdout only, so pair it with a counts receipt that shows the command, its output and the exit code.> Start histogram <L1-FILL — A/B/C and mined/queued/rejected>; end <L1-FILL — rows, A/B/C, mined/queued/rejected> (`reports/round-77/telemetry/<L1-FILL>`).

Rows added by tier: <L1-FILL — S897 tier X, S898 tier Y>. Rows touched old→new: <L1-FILL — "none" or the row ids and the cells changed>. Frontier advanced: <L1-FILL — the staged document ids S897→D1, S898→D2 and the theme `linguistics/naming-systems`>.

Assimilation: <L1-FILL — one naming-systems theme, one adopted entry, ≥1 admit + ≥1 reject with reason/flip; the by-document map lives in `reports/round-77/claims.json` `row_set`>. No `considerthese/` directory exists for this lane.

## Trend verdicts

- **expansion: <L1-FILL — improved | harmed | unchanged | unprovable-but-better>** — <L1-FILL — evidence pointer for the row/entry delta; state separately whether claim C is admitted (a failed frozen counter is not a score advance)>.
- **quality: <L1-FILL>** — <L1-FILL — evidence pointer: QUALITY criterion added/corrected, evidence recapture, routed-defect fixes>.
- **discernment: <L1-FILL>** — <L1-FILL — evidence pointer: the refusals with reasons/flips, the duplicate checks by document, any reviewer disagreement preserved>.
No scalar is claimed.

## SHONEN

One line per box of `SHONEN.md`, `[x]` only with a named non-author verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched.

- [<L1-FILL — x|~|space>] SKILL decision tables/error patterns/checklists and cited source base — <L1-FILL — pointer, e.g. `SKILL.md:<n>`, `corpus/SOURCES.md`, census receipt>.
- [<L1-FILL>] End-to-end domain task executed and logged — <L1-FILL — pointer, e.g. the amendment path + `LOG.md:<n>` + the C measurement receipt>.
- [<L1-FILL>] Instructions executable without oral context — <L1-FILL — pointer to frozen counter commands/selftests/census receipts; state whether any fresh-clone verifier is claimed>.
- [<L1-FILL>] No cross-domain bleed; PROVINCE remains accurate — <L1-FILL — pointer to `PROVINCE.md` and the entry; state whether a non-author promotion verdict is claimed>.

Stale-lane: <L1-FILL — "none" or the stale surface and its disposition>. Tools installed or upgraded: <L1-FILL — "none" or tool/version/channel/reason>. `/home/vgpnk/.omp/agent/RULES.md` was read; pacman remained paused host-wide and no pacman transaction was run. Wave shape: W1 = 36 seats as declared in `.ufo/waves/round-77/w1/spec.json` (12 scout / 8 executor / 6 scribe / 4 critic / 2 reviewer / 1 connector / 1 mutation-tester / 1 revenger / 1 sentinel), attack roles 8/36, connectors 1; actual completed seats <L1-FILL — n>. W2 = <L1-FILL — seat count and role split>. Round total <L1-FILL — n>; attack roles <L1-FILL — n/total>; connectors <L1-FILL — n>. Dead seats: <L1-FILL — "none" or the ids with how each was recovered>. L1 held the planner/data-walk role under the addendum (<L1-FILL — confirm; record the validator exception if a planner role was requested>). Assimilation: <L1-FILL — one line>. considerthese: absent for this lane — report line only. L0: freshness axis-moves remain paused under the open kotodama round-11 L0 row (CLAIMS-DRAFT axes note); Open L0 questions: <L1-FILL — "none" or the appended `<lane> | round-77 | <question>` line>.
