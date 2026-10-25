# SentinelScope — round-72 plan write-scope audit

Seat: SentinelScope (sentinel, w1). Date: 2026-10-25. Leaf role; no delegation.

## Method

Audited the round-72 plan's write set against the round prompt's write-scope
(`.ufo/prompts/kotodama-round-72.md` §4/§6, esp. lines 280–285 and §10 source-repo
read-only). Sources read:

- `reports/round-72/claims.json` (frozen claims Ca + C, their legs and after-states)
- `.ufo/waves/round-72/w1/dispatch.json` taskCall tasks (32 seat briefs, full text)
- `.ufo/waves/round-72/w1/spec.json` items (identical brief content) + swarm-registry.json
- Lane git state (read-only): `git status --porcelain`, `git log --oneline -5`
- Fleet `.ufo/` listing (reports/, l0-questions.md present; no round-72 report dir yet)
- `.ufo/waves/round-72/assimilation/` scratch contents

## 1. Enumerated planned writes vs round-prompt scope

Round prompt write-scope (line 280): lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(whole repo), fleet report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotodama.md`,
appended lines in `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Never: MANIFEST.json,
fleet `templates/`, fleet `scripts/`, `.ufo/state/`, `.ufo/watchdog.log`, sibling repos,
shokuknow (read-only per §10).

| # | Planned write | Target path | Scope check | Verdict |
|---|---|---|---|---|
| 1 | Entry: heritage-taxonomy-models.md | lane `corpus/knowledge/culture-material/heritage-taxonomy-models.md` | lane repo | IN SCOPE |
| 2 | Entry: heritage-taxonomy-models.amend-2026-10-24-r13.md | lane `corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` | lane repo | IN SCOPE |
| 3 | Two registry rows S874/S875 | lane `corpus/SOURCES.md` Registry table (append) | lane repo | IN SCOPE |
| 4 | Lesson round-72 | lane `corpus/lessons/round-72.md` (Gate, Mistakes, Quarantine) | lane repo | IN SCOPE |
| 5 | LOG.md append (round-72 entry + K71-1..8 dispositions) | lane `LOG.md` | lane repo | IN SCOPE |
| 6 | QUALITY.md appends (criteria 20 landed, 21 added) | lane `corpus/QUALITY.md` | lane repo | IN SCOPE |
| 7 | Round-71 lesson corrections append | lane `corpus/lessons/round-71.md` (## Corrections (round 72)) | lane repo | IN SCOPE |
| 8 | SCORECARD.md append (claim rows) | lane `SCORECARD.md` | lane repo | IN SCOPE |
| 9 | reports/round-72/** (claims.json; accept-c.py/accept-ca.py counters; telemetry/ measures/controls/receipts) | lane `reports/round-72/` | lane repo | IN SCOPE |
| 10 | Re-stamp receipt append (CASTAMP) | lane `reports/round-71/telemetry/` (new appended file; no filed byte rewritten) | lane repo | IN SCOPE |
| 11 | .ufo/waves/round-72/** (spec/dispatch/registry; 32 w1 seat reports; counters/ drafts; assimilation/ reg-ids/staged-ids/collisions/validate//mutations/) | lane `.ufo/waves/round-72/` | lane repo | IN SCOPE |
| 12 | Fleet report | fleet `.ufo/reports/round-72/kotodama.md` | explicitly allowed (§4 line 101) | IN SCOPE |
| 13 | l0-questions append | fleet `.ufo/l0-questions.md` | explicitly allowed (line 281–282, 345–348) | IN SCOPE |

All 13 planned write targets are inside the round prompt's permitted set. No planned write
targets MANIFEST.json, fleet `templates/`, fleet `scripts/`, `.ufo/state/`, `.ufo/watchdog.log`,
`.scratch/`, any sibling repo, or `/home/vgpnk/Projects/shokuknow`. (Census commands
`scripts/sources-census.sh validate …` are executed read-only; the script itself is never
edited. Any later wave-2 writes would land under lane `.ufo/waves/round-72/w2/` — same lane
scope.)

## 2. Seat-brief check: does any brief write outside its assigned path?

All 32 briefs reviewed in full. Every seat's explicit writes are:

- its `Report:` trailer — `.ufo/waves/round-72/w1/<Seat>.md` (lane, assigned), and
- explicitly named scratch/draft paths: ExecCCounter/ExecCaCounter → lane
  `.ufo/waves/round-72/counters/`; ExecScratchMirror → `/tmp/r72-mirror/` + lane
  `.ufo/waves/round-72/assimilation/validate/`; ExecRenumber → `/tmp/r72-entries/`;
  ScribeEntries → `/tmp/r72-entries-scribe/`; ScribeLesson → `/tmp/r72-lesson.md`;
  ScribeCorrections → `/tmp/r72-corrections.md`; RevReceiptHeader → `/tmp/r72-castamp/`;
  MutRegistryCollision → `/tmp/r72-mut/` + lane `.ufo/waves/round-72/assimilation/mutations/`;
  MutCaAppend → `/tmp/r72-mut-append/`; scouts → `/tmp/` captures (ScoutCDXCanonical names
  `/tmp/ScoutCDXCanonical/`; IHChina/Bunka reuse `/tmp/ihchina-*.html`, `/tmp/bunka.html`).

No brief routes a seat to write to the fleet repo, shokuknow, any sibling repo, or any
forbidden path. The five integration files named in the wave context's never-mutate list
(`LOG.md`, `corpus/SOURCES.md`, `corpus/QUALITY.md`, `SCORECARD.md`,
`corpus/lessons/round-71.md`) appear in seat briefs only as read inputs or as the *subject*
of drafts written to `/tmp`; the L1 is the sole writer of those files (and of
`reports/round-71/telemetry/` receipt #10). No seat brief writes outside its assigned path.

## 3. Flags and observations (non-scope)

- OBS-1 (plan vs frozen leg fidelity, not scope): claim-C leg SCRATCHMIRROR checks receipt
  `.ufo/waves/round-72/assimilation/validate-receipt.txt`, but ExecScratchMirror's brief says
  "save everything under `.ufo/waves/round-72/assimilation/validate/`" (files already present:
  `census-validate-mirror.exit/.out/.err`, `rows-shape-mirror.txt`). The L1 must place the
  receipt at the exact frozen path or the leg fails.
- OBS-2 (process, not scope): ExecRenumber writes `/tmp/r72-entries/` while
  ExecScratchMirror reads it, falling back to marker placeholders if absent; ScribeEntries
  drafts to a separate `/tmp/r72-entries-scribe/`. Placeholder fallback means the mirror gate
  can pass on placeholder bodies if it runs before the real entries land. Keep the gate AFTER
  the entry drafts land.
- OBS-3 (trivial): ScoutCDXCanonical names `/tmp/ScoutCDXCanonical/` rather than
  `/tmp/<seatname>/`; still `/tmp`, no repo impact.
- OBS-4 (consistency): the wave context's never-mutate list includes the five files the frozen
  claims require appends to; this is resolved by routing all of them through the L1 (helper
  commits), no seat brief carries them as a write target. No contradiction in practice.

## Verdict

- Planned writes outside round-prompt scope: **NONE** (13/13 enumerated write targets in scope).
- Seat briefs writing outside assigned path: **NONE** (32/32 reviewed).
- Forbidden-path writes (MANIFEST.json, templates/, scripts/, .ufo/state, watchdog.log,
  .scratch/, siblings, shokuknow): **NONE planned**.
