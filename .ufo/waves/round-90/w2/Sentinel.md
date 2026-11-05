# Sentinel — round 90 w2: conduct and confinement audit

Seat: Sentinel (leaf, no subagent dispatch) · milestone r90-v2 · lane kotodama-shokunin
Snapshot: `date -Iseconds` → `2026-11-05T00:14:48-03:00`; lane `HEAD` = `3f56892f29e46cce90996bd126ca3a2e7c7658e7`;
graded lands = `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761` (ancestor of HEAD); base = `6b0b86e45ae902331aca75863db380f2991458c4`;
commits in base..HEAD = 10.

All commands are absolute-path or run from the lane root; stage receipts holding the verbatim output of every command are in
`.ufo/waves/round-90/w2/stage/Sentinel/`. Writes made by this seat: this report, that stage directory, and
`/fast/scratch/hyaku/kotodama-r90/Sentinel/` only. No production file, no git/jj mutation, no package install
(tooling record: none installed, none needed; `pacman` untouched).

## Verdict table (one line per check)

| # | Check | Verdict |
|---|-------|---------|
| a | No credential material / private URL / `op://` in round-90 new files at LANDS | PASS — 0 credential shapes, 0 `op://` at `7f3a7aa6`; only site-chrome JS inside captured pages and one pre-existing LOG.md prose line |
| b | Every capture cited by a receipt is a lane file, not /tmp, /var/tmp, /fast/scratch | CAPTURES PASS (32/32 w1 refs + 8/8 manifest captures tracked in-lane, hashes match); SCRATCH LEG RED — `check-cited-records.py` rc=1, 11 round-90 + 3 inherited scratch citations, none of them a capture |
| c | No round-90 file writes outside the lane | NOT CLEAN — no seat wrote outside, but round-90 artifacts exist in the fleet repo (dispatch evidence ×7 commits, plus an uncommitted run report) and in `/tmp` (L1 pre-freeze working dirs) |
| d | Every round-90 commit authored `kotodama-shokunin <kotodama@shokunin.local>`, no seat commit | PASS — 10/10 commits, author and committer identical; 0 seat identities; 0 trailers |
| e | Fleet repo has no round-90 kotodama-named leftover | FAIL (literal) — `git status --porcelain` now lists `?? .ufo/reports/round-90/kotodama.md`; the other four entries are not kotodama-named |
| f | No source opened by passing a bot challenge, login wall or paywall | PASS — 8/8 manifest captures HTTP 200, 32 w1 captures 28×200 + 4 honest 404 dead seeds, zero wall phrases; the one CAPTCHA string is a site feedback widget in page chrome |

## (a) Credential material, private URL, `op://` at LANDS

```
$ git diff --name-only 6b0b86e4..HEAD            # 130 paths fed to git grep
$ git grep -n -I -E 'op://|BEGIN [A-Z ]*PRIVATE KEY|BEGIN OPENSSH|api[_-]?key|apikey|secret[_-]?key|password[[:space:]]*[=:]|passwd|bearer [A-Za-z0-9._-]{8,}|Authorization:[[:space:]]|session[_-]?id|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}' \
    7f3a7aa6 -- <130 paths>
```
Observed: 4 hits, all benign — MediaWiki inline JS (`var cookie=document.cookie.match(...)`) inside the captured
Wikipedia pages (`w1/stage/ExecIndepRefetch/caps/wiki-{curse,sacred,votive}.txt`, `reports/round-90/evidence/S949.txt`),
and one LOG.md prose line (`LOG.md:2064 Authorization: the operator requested a 32–64-worker native OpenCode Go …`).
That LOG.md line is **pre-existing**: `git log -S 'Authorization: the operator requested' -- LOG.md` → `c53782ab 2026-10-17`,
and `git diff 6b0b86e4 HEAD -- LOG.md | grep -c 'Authorization: the operator'` → `0`.

```
$ git grep -n -F 'op://' 7f3a7aa6 -- <130 paths>
```
Observed: **no output** (0 references at the graded lands). At HEAD the literal `op://` occurs twice, both inside seat
prompt text in `.ufo/waves/round-90/spec-v2.json` and `.ufo/waves/round-90/w2-dispatch.json` (the Sentinel instruction
"… private URL or op:// reference"), i.e. instruction text, not a reference.

Added-line scan `git diff 6b0b86e4 HEAD | grep '^+' | grep -E 'op://|-----BEGIN|sk-…|ghp_|xox[bap]-|AKIA…|AIza…|Bearer …|password=|api_key=|secret='`
produced only the same two prompt lines. URL hosts in added lines (`git diff 6b0b86e4 7f3a7aa6 | grep '^+' | grep -o -E 'https?://[A-Za-z0-9._-]+' | sort | uniq -c`)
are all public: `en.wikipedia.org`, `wals.info`, `drops.dagstuhl.de`, `pmc.ncbi.nlm.nih.gov`, `www.atticinscriptions.com`,
`glossary.sil.org`, `creativecommons.org`, `doi.org`, `web.archive.org`, `example.org` (fixtures). No userinfo URLs
(`https://user:pass@`), no `localhost`/`127.0.0.1`/`.internal`/intranet hosts. `private` matches are prose or public path
segments (`dedication-private`, "private petition", "private prayer practice").

Receipt: `stage/Sentinel/check-a-credentials.txt`.

## (b) Captures cited by receipts live in the lane tree

```
$ python3 -B tools/check-cited-records.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
CITED-RECORDS: 0 empty / 14 scratch
… 14 SCRATCH lines …
rc=1
```

Separation (round-90 vs inherited):

- **Round-90: 11 hits, all in receipts, all `--work` roots / materialized clone trees, none a capture**
  - `reports/round-90/controls/at-freeze-C-base.txt` ×2, `at-freeze-C-freeze.txt` ×2, `at-freeze-O-base.txt` ×3,
    `at-freeze-O-freeze.txt` ×2 — `--work /fast/scratch/hyaku/kotodama-r90/atfreeze/{c,cf,o,of}` and `…/mat[/tools/check-advance-evidence.py]`
  - `reports/round-90/final/lands-C.txt` ×1, `final/lands-O.txt` ×1 — `observed=/fast/scratch/hyaku/kotodama-r90/L1/run2-{C,O}/mat`
- **Inherited: 3 hits** — `corpus/lessons/round-84-verifier-spotcheck.md` (`/tmp/base84`, `/tmp/base84/corpus/knowledge`),
  `corpus/lessons/round-88-verifier-spotcheck.md` (`/tmp/r88v-work`). Nothing here was authored by round 90.

Capture leg (all pass):

```
$ python3 -B tools/check-cited-records.py … (0 empty)
# manifest verification: 8/8 rows → bytes_ok sha_ok reports/round-90/evidence/S94{2..9}.txt
$ git ls-files --error-unmatch reports/round-90/evidence/S94*.txt   # 8/8 TRACKED, 8/8 PRESENT
# w1 receipt: declared refs: 32  missing-or-untracked: none
# fetch.json contains /tmp: False | /fast/scratch: False
$ grep -rn -E '/(tmp|var/tmp|fast/scratch)/[^ ]*(caps/|S94[0-9])' reports/round-90/ .ufo/waves/round-90/
# no output
```

So no capture cited by any receipt lives in `/tmp`, `/var/tmp` or `/fast/scratch`; every one is a tracked file under
`reports/round-90/evidence/` or `.ufo/waves/round-90/w1/stage/ExecIndepRefetch/caps/`. The tool's rc=1 is caused by
transient working-directory citations, not by evidence bytes.

Receipts: `stage/Sentinel/check-b-cited-records.txt`, `stage/Sentinel/check-b-capture-resolution.txt`.

## (c) Round-90 writes outside the lane

Seat-level: no seat-authored path outside the lane was found; lane stage dirs only hold in-lane artifacts. Outside-lane
round-90 artifacts that do exist, classified:

1. **Fleet repo, committed dispatch evidence** — 7 commits `round-90: kotodama dispatch evidence (hyaku inline attempt 1..3)`,
   each touching only `.ufo/prompts/kotodama-round-90.md` (`git -C …/shokunin show --stat b72ce052` → `.ufo/prompts/kotodama-round-90.md`);
   the file is 92 487 B, committed. This is hyaku's dispatch channel, not a seat write, but it is a round-90 write outside
   the lane by the letter of the contract.
2. **Fleet repo, uncommitted run report** — `?? .ufo/reports/round-90/kotodama.md`, 15 227 B, 125 lines, mtime
   `2026-11-05 00:13:54`. First line `# kotodama — round 90 (hyaku run 15, attempt 1)`; it declares
   `lane tip at report: 195aff9ca0d490684a3975d48f19f2cbfe194dac`. This is the campaign's per-lane report slot
   (`kake.md`, `lore.md`, `revenger.md` are already tracked there), so it is the intended hyaku channel — see finding F1
   for the stale tip.
3. **`/tmp` working dirs from L1, pre-freeze** — `du -sh` → `r90base 8.5M`, `r90land 8.6M`, `r90c2base 13M`,
   `r90c2freeze 13M`, `r90c2land 13M`, `r90ctl-id 13M`, `gate_r90.py 32K`, `r90census.txt 4.0K`,
   `r90-revenger-closure-entry.json 8.0K`; mtimes 19:28–19:46 on 2026-11-04, i.e. before the 19:51 freeze. They are copies
   of corpus/base/lands trees, not clones (no `.git`), none is cited by a round-90 receipt, and none was removed.
   Each artifact is under 50 MB, but they are working dirs, which the contract places under `/fast/scratch/hyaku/kotodama-r90/`.
4. **`/tmp/k72-tip-95amlaa2`** (323 MB apparent, mtime 00:10) — a symlink farm whose entries point into the fleet root
   (`AGENTS.md`, `LOG.md`, `MANIFEST.json`, …) and the lane (`git -C …/kotodama-shokunin rev-parse --show-toplevel` →
   `/home/vgpnk/Projects/shokunin/kotodama-shokunin`). Not round-90 evidence and not cited; see F5 for the write hazard.
5. **In-lane drift after the lands** — commit `3f56892f` (00:11:41) rewrites `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`,
   and at audit time the working tree additionally carries uncommitted edits to that entry (mtime 00:12:46) and to
   `reports/round-90/census-end.txt` (mtime 00:12:15). Inside the lane, so not a boundary breach, but see F2: the graded
   C object at the tip is no longer the lands object.

Untouched: `/home/vgpnk/Projects/shokuknow` (`find … -newermt '2026-11-04 00:00'` → only the `.git` directory itself, no
working-tree file); sibling lanes (`-shokunin/*` mtimes) show no round-90 kotodama content.

Receipt: `stage/Sentinel/check-c-outside-lane.txt`.

## (d) Git attribution

```
$ git log --format='%H|%an|%ae|%cn|%ce|%s' 6b0b86e4..HEAD      # 10 lines
$ … | awk -F'|' '$2!="kotodama-shokunin"||$3!="kotodama@shokunin.local"||$4!="kotodama-shokunin"||$5!="kotodama@shokunin.local"'
awk_rc=1  (1 = no nonconforming commits)
```
All 10 commits in the round range are authored **and** committed by `kotodama-shokunin <kotodama@shokunin.local>`:
`7f3a7aa6` (C lands), `ebd81b1b`, `c0c628d8`, `9fb2c58f`, `d0b6f2a7`, `945e6a3e`, `fe59fc35`, `19187112`, `195aff9c`,
`3f56892f`. No commit carries `Co-authored-by:`/`Signed-off-by:` or a seat identity; the only "seat" strings are subject
text ("validated dispatch, ready handoff (11 seats)"). All-refs identity census: `1428 kotodama-shokunin`, `178 protocol-shokunin`,
`5 t <t@e>` (all 2026-10-21, pre-round), `1 João Pedro Veiga` (2026-10-17 merge) — no seat identity exists in the lane.
The 7 fleet-repo round-90 commits are likewise authored `kotodama-shokunin <kotodama@shokunin.local>`.

Receipt: `stage/Sentinel/check-d-attribution.txt`.

## (e) Fleet repo leftovers

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .scratch/run15-state.json
 M .ufo/l0-questions.md
?? .ufo/reports/round-86/kama.md
?? .ufo/reports/round-90/kotodama.md
?? mo.tip
```
Five entries. Four are not kotodama-named: `.scratch/run15-state.json` is hyaku's run state (diff sets `"round": 90`,
`"kotodama": {…}` counters — orchestrator ledger, not a lane deliverable); `.ufo/l0-questions.md` diff adds two `kotoba`
lines and **zero** kotodama lines; `.ufo/reports/round-86/kama.md` and `mo.tip` contain no kotodama text (grep -c → 0).
The fifth, `?? .ufo/reports/round-90/kotodama.md`, **is** a round-90 kotodama-named leftover (F1). Note this file appeared
between two of my own status samples (4 entries at ~00:11, 5 at 00:14:48), so the fleet repo is live under hyaku.

Receipt: `stage/Sentinel/check-e-fleet-status.txt`.

## (f) Challenge / login / paywall inspection of the captures

```
$ grep -rn -i -E 'just a moment|checking your browser|cf-browser-verification|attention required|verify you are human|
   access denied|request blocked|too many requests|sign in to (read|continue|view)|subscribe to continue|
   institutional login|register to read' reports/round-90/evidence/ .ufo/waves/round-90/w1/stage/ExecIndepRefetch/caps/
rc=1  (no wall phrases)
```
Statuses from the receipts: manifest 8×200; `fetch.json` captures 28×200 + 4×404. The four 404s are recorded as tier
`dead` seeds (`sil-vocative`, `sil-prayer`, `etcsl-cat`, `aio-browse`) — honest absences, not walls. Fetch method recorded in
the receipt itself: `curl -sS -L -D headers, body saved verbatim, sha256 of the bytes on disk`, note verbatim
"No headless browser, no CAPTCHA handling, no paywall workaround. Every status is the status curl saw."

The single `captcha` string cluster is `reports/round-90/evidence/S948.txt:1457–1908`, inside the Dagstuhl page's own
`_feedback-form`/`_captcha-check` widget ("Feedback on the Current Page", "Thanks for your feedback! … Dagstuhl Publishing") —
page chrome of a page that served HTTP 200 with its real metadata and abstract ("Dei Genitrix: A Generative Grammar for
Traditional Litanies", `citation_doi 10.4230/OASIcs.CMN.2016.12`, abstract present at line 93). No source was opened through a
challenge, login or paywall; no capture contains a challenge interstitial. (Inherited context, not round 90: SOURCES row S240
documents a prior Springer "Client Challenge" that was *met, not passed*, with the text read from a Wayback capture.)

Receipt: `stage/Sentinel/check-f-wall-markers.txt`.

## Findings

| # | Sev | Finding | Smallest remediation |
|---|-----|---------|----------------------|
| F1 | MEDIUM | Fleet repo carries the round-90 run report as an **untracked** file `?? .ufo/reports/round-90/kotodama.md` (15 227 B, mtime 00:13:54), and its provenance field is already wrong: it says `lane tip at report: 195aff9c` while the lane HEAD was `3f56892f` from 00:11:41 onward. A closure that trusts that field reads a stale tip. | hyaku commits the report and states the tip as `git rev-parse HEAD` at write time, or pins the graded revision `7f3a7aa6` explicitly. |
| F2 | MEDIUM | Lands-vs-tip drift on the graded object. Commit `3f56892f` rewrites `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md` *after* the lands `7f3a7aa6`, and at audit time that entry (00:12:46) and `reports/round-90/census-end.txt` (00:12:15) carry further **uncommitted** edits. The frozen C receipts are evidence about `7f3a7aa6` only; measured-at-tip means something else now. If a seat rather than L1 made the uncommitted edits, it also breaches the seat read-only-production grant. | State C's graded revision in every receipt (already true at lands), and have the closure re-run the frozen counter at the tip before committing any post-lands entry edit, or revert the uncommitted edits and land them as a new round. |
| F3 | LOW | `tools/check-cited-records.py` exits 1 on round 90: 11 SCRATCH citations (`reports/round-90/controls/at-freeze-*`, `final/lands-*`) point at `/fast/scratch/.../{atfreeze,L1/run2-*}` `--work` roots and materialized trees. None is a capture and no evidence byte depends on scratch, but the QUALITY-31 leg is red at lands and at tip. | Accept as a recorded red in the closure (the receipts are frozen and cannot be edited), or have the tool treat an explicit `--work` root as non-citable; do not cite scratch roots from future receipts. |
| F4 | LOW | L1 left six `/tmp` working trees (base, lands, three c2 variants, ctl-id; 8.5–13 MB each) plus `gate_r90.py`, `r90census.txt`, `r90-revenger-closure-entry.json` in `/tmp` instead of `/fast/scratch/hyaku/kotodama-r90/`, and did not remove them. None is cited by a round-90 receipt. | Remove them once the round closes; future pre-freeze work goes under the seat's `/fast/scratch` root with `TMPDIR` set. |
| F5 | LOW | `/tmp/k72-tip-95amlaa2` (323 MB, mtime 00:10) is a symlink farm whose members resolve into the fleet root (`LOG.md`, `MANIFEST.json`, …) and the lane; any write through it mutates production and would not be visible as a lane write. Not round-90 evidence; owner unattributed. | Whoever owns the run should delete it; never write through a symlinked `MANIFEST.json`/`LOG.md`, and no seat may follow it into production. |
| F6 | INFO | S948's capture legitimately contains a CAPTCHA input block (site feedback widget). A reader grepping captures for `captcha` will hit it; it is not challenge passage. | Recorded here so the reviewer/critic do not read it as a wall breach. |
| F7 | INFO | Pre-existing empty nested dir `kotodama-shokunin/kotodama-shokunin/reports` (mtime 2026-10-18) inside the lane. Not a round-90 write, not cited. | None this round. |

## Boundaries observed

Not run, by design: the frozen counters (`measure90.py`, `separability90.py`) — their verdicts belong to ExecCounterAtLands and
the closure, and re-running them here would duplicate another seat's surface. No freshness row was read-for-repair or
re-dated; no registry row was touched. No production file was edited by this seat; `git status` samples above are read-only
observations of concurrent activity by other seats/L1, not of my own writes.
