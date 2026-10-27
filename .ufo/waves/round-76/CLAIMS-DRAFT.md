# Kotodama round 76 — claims DRAFT (L1 KotodamaR76). Not frozen. The freeze commit supersedes this file.

Base revision (lane main at round start): `98c486bdb4650ba5b8e651d332910e8ee60ad121`.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Fleet: `/home/vgpnk/Projects/shokunin`.
Scratch root: `/fast/scratch/hyaku/kotodama-r76/<seat-name>/` (delete on exit; never /tmp).

## Axes note

SCORECARD holds no numeric scores; freshness axis-move claims stay paused by the open L0 row
`kotodama | round-11` (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47`). No stagnation-nudge
waiver is claimed. The round works coverage (C) and calibration (Ca). Two claims, no exploratory claim.

## Claim C — coverage (assimilation-sourced), theme "calendar and era instruments"

Surface the claim moves: frontier -> core for **standards-level calendar compilation and archival era-name
tables**, ground the lane does not hold. Package: `/home/vgpnk/Projects/shokuknow/merge/kotodama/` (read-only).

Candidate entries (staged paths under `merge/kotodama/knowledge/corpus/knowledge/culture-material/`):

| key | staged file | cites (campaign ids) | proposed lane path |
|---|---|---|---|
| a | `calendar-festival-systems.amend-2026-10-24.md` | S937, S935, S932, S919, S921 | `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` |
| b | `calendar-festival-systems.amend-2026-10-24-r10.md` | S938 | `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24-r10.md` |
| c | `era-periodization-models.amend-2026-10-23b.md` | S908 (+S757 coupling only) | `corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23b.md` |
| d | `calendar-festival-systems.amend-2026-10-23c.md` | S916 (tier C reproduction page; S718/S719 coupling only) | `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-23c.md` |

Campaign-namespace ids collide with lane ids (35 collisions S859-S893, `assimilation/collisions`): every
adopted entry's citation is re-pointed BY DOCUMENT to a lane id. Planned lane ids (continuing the registry,
last id S893): S894 = National Archives of Japan era-name table (campaign S908 live form + S935 Wayback
capture of the SAME page, one row); S895 = xingzuobaike GB/T 33661 reproduction (S916); S896 = openstd
newGbInfo Wayback capture (S932); S897 = openstd showGb page (S938); S898 = gmw.cn 2017 report (S937).
Already-held documents: campaign S919 -> lane S892 (Marrone), campaign S921 -> lane S885 (Barthes, Persee).
Scouts may change this plan where a document is unreachable or two URLs are one document.

Declared after-state (concrete): knowledge `.md` files 252 -> 252+n with n>=2 (n counts admitted files among
the four candidate paths ONLY); registry rows 817 -> 817+k, k = number of distinct documents cited by the
admitted entries that the registry did not hold, one row per document, each `mined`, `opened 2026-10-27`,
used-by exactly the citing admitted entries; no tier-C row is the sole support of an admitted entry; every
Gate quote located inside a committed evidence window; Gate carries >=1 admit and >=1 reject from the
assimilation set; census exit 0. Before: `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and
`git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus` each print nothing (exit 1).
Do-nothing control: counter at `lands == freeze` must FAIL the data legs.
Sourced claim: C cites the opened rows S894+ (frontier-step item 4).
Kill rule (frozen with the claim): fewer than two candidate files landing, a row appended as staged,
a quote not in its window, an access-control bypass, or a cited campaign-namespace id -> fails as declared (honest stop).

## Claim Ca — calibration (round-75 landed statements vs observed repo state)

A committed-bytes ledger `reports/round-76/ledger.json` (>= 10 pairs, fixed before data), each pair a
statement filed by round 75 (lesson `corpus/lessons/round-75.md`, SKILL.md, SCORECARD, QUALITY 27, report) whose stated token
differs from the observed token at base `98c486b` (sources: `.ufo/waves/round-75/w3/ExecCountsSweep.md`
F1-F13, `corpus/lessons/round-75-verifier-spotcheck.md` section 7, `corpus/lessons/round-75.md` `## Routed to round 76`).
Disposition per pair: REPAIR (mutable file: SHONEN.md, SKILL.md, README) or ANNOTATE (append-only file: the
round-75 lesson, LOG, SCORECARD, QUALITY: a row under `## Corrections — round 76` in SCORECARD.md carrying id,
old token, new token, the pair's re-derivation command). Counter: `reports/round-76/accept-ca.py` adapted from
`reports/round-75/accept-ca.py`. Also in Ca: the claim text prints the FULL measuring command (with
`--combined` and the pinned-main requirement where the counter needs them); the round-76 counters honour
`TMPDIR`/`--work`/`$HYAKU_SCRATCH` and write nothing under a literal `/tmp` (routed defect).

## Frontier step (inside the cap)

SOURCES.md rows for C; census before -> after (`reports/round-76/telemetry/census-start.txt` exit 0 at start);
`corpus/lessons/round-76.md` with `## Gate`, `## Quarantine`, `## Collision guard`, `## Normalization`, `## Census`,
`## Mistakes` (>=1 mined mistake; a fix counts only once shown able to fail), `## Routed to round 77`;
a QUALITY criterion for the mined mistake when no criterion caught it.
`considerthese/`: no such directory for this lane (`ls /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese` fails).
