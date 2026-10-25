# RevQuality22 — wave 2 (FALSIFY) attack on QUALITY criteria 22 & 23

Seat: RevQuality22 (critic/reviewer, leaf). Round 73, wave 2. Date 2026-10-25.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at lands `0316b8883b4f8d44b8efd720140e7f52f734a102`
(base `8841ad3b896a0227674fa0725b818c999118046f`, freeze `af65165cf269db346ef872e16a656eccd7264d01`).
Read-only on lane/fleet except this report; experiments ran in `/tmp/RevQuality22/` (throwaway clone of the lane
at lands) and live fetches downloaded to `/tmp/RevQuality22/`. No tools installed (curl 8.23.0, git, GNU grep,
python3 already present; no pacman, no `task`/subagents, no peer messaging).

## Verdicts

- **Criterion 22: STANDS.** The rule, the check, the controls and the first applications all work; the
  only drift is that two illustrative byte figures from the round-72 grounding (43,419 / 154,144 B) do not
  re-measure exactly today (see Finding Q22-M1, MINOR).
- **Criterion 23: STANDS.** Every cited leg is verifiable and reproduced: `SELFTEST: 10/11` exit 1 for
  the round-72 counter at lands; selftest receipt committed at freeze with pinned hashes; freeze tree has
  receipts and no landing; the r3 red-before reproduces verbatim when only the `load_ledger` guard is
  removed; the intact r3 counter passes `SELFTEST OK: 10 scenarios` exit 0.

## Findings by severity

### Q22-M1 (MINOR) — the criterion's UNESCO byte figures are stale; Springer and Cambridge figures reproduce exactly

Grounding sentence (QUALITY.md:69): "...round-72 UNESCO 43,419 B wall vs 154,144 B narrative; round-73
Springer 200/3,038 B `<title>Client Challenge</title>`...". Re-measured 2026-10-25 (downloads to
`/tmp/RevQuality22/`; `curl -sSL -A <UA> -o <file> -w 'http=%{http_code} size=%{size_download}'`):

| source | UA (verbatim) | http | bytes | wall |
|---|---|---|---|---|
| Springer chapter `10.1007/978-3-032-03277-5_15` | `curl/8.7.1` | 200 | 325,225 | absent (`<title>Conlangs in Theoretical Linguistics | Springer Nature Link</title>`, 21,768 words) |
| Springer chapter | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` | 200 | 3,038 | present (`<title>Client Challenge</title>`) |
| Cambridge DOI `10.1017/cnj.2024.21` (→ `cambridge.org/core/product/identifier/S0008413124000215/type/journal_article`) | `curl/8.7.1` | 429 | 1,302 | present ("Too many automated requests") |
| Cambridge DOI | browser UA (same string) | 429 | 1,302 | present ("Too many automated requests") |
| UNESCO `https://ich.unesco.org/en/RL/tango-00258` | `Mozilla/5.0` (round-72 plain) | 200 | 46,392 | present (captcha/TSPD/"Please enable JavaScript") |
| UNESCO | `curl/8.7.1` | 200 | 40,956 | present (same markers) |
| UNESCO | `Mozilla/5.0 (X11; Linux x86_64)` (round-72 browser) | 200 | 154,141 | absent (title "Tango - UNESCO Intangible Cultural Heritage") |
| UNESCO | full Chrome string (the criterion's prescribed second UA) | 200 | 154,319 | absent |
| UNESCO | empty UA `""` | 200 | 154,141 | absent |

Springer 200/325,225 B (curl) vs 200/3,038 B Client Challenge (browser) — **reproduces exactly**. Cambridge
429/1,302 B under both UAs — **reproduces exactly**. UNESCO's *class* behavior reproduces (plain UAs incl.
`curl` get the wall; browser-shaped and empty UAs get the full narrative), but the exact numbers do not: the
wall is now 46,392 B (`Mozilla/5.0`) or 40,956 B (`curl/8.7.1`), not 43,419 B, and the narrative is
154,141–154,319 B, not 154,144 B. The figures in the criterion are point measurements from round 72 and
drift with UA string and time; they are illustrative, not load-bearing (the rule — bytes + marker per
request, status decides nothing — stands on the reproduced class behavior). Suggested optional patch: phrase
as "round-72 measured …" or drop the byte figures.

### Q22-M2 (MINOR, information only) — no earlier Gate line is in scope; nothing retro-fitted (as the criterion states)

Declared greps (from the criterion and `reports/round-73/telemetry/quality22-controls.txt`):

```
GROUND='^[|*-].*\| *(wall|captcha|status):'
SHAPE='UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent).*UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'
```

Run over **every** `corpus/lessons/*.md` at the lands commit (fresh clone): **only `round-73.md` has
in-scope records — GROUND=2, SHAPE=2, automation-none=2 (rows S894 and S910 in `## Gate`). Every other
lessons file scores 0/0/0**, so no earlier Gate line fails the declared check (they are out of scope by the
criterion's own design: "Binds from round 73; no earlier Gate line is retro-fitted"). As information: earlier
Gate lines carry refusal reasons in other vocabularies that would fail SHAPE if they were in scope — e.g.
`round-49.md:64` ("publisher page 403"), `round-51-verifier-spotcheck.md:108` (S094 "HTTP 403, Cloudflare
challenge"), `round-52-verifier-spotcheck.md:106` (S132 "HTTP 403 … cf-mitigated: challenge"),
`round-62.md:43` (`-A 'Mozilla/5.0 …Firefox/131.0'`, elided UA). None match GROUND, i.e. none are flagged,
consistent with "no retro-fit".

## (b) The three controls re-derived (exact printed lines)

The controls file gives only expected counts; fixture lines were reconstructed from the wave-1 review's
shapes. My runs:

```
missing.txt:    GROUND=1 SHAPE=0 automation-none=0     # status: + HTTP 403, no UA record, no automation token
compliant.txt:  GROUND=1 SHAPE=1 automation-none=1     # two UA->response records + automation: none
automation.txt: GROUND=1 SHAPE=1 automation-none=0     # shape-compliant, automation token absent
round-73.md:    GROUND=2 SHAPE=2 automation-none=2
```

This re-derives `quality22-controls.txt` lines 4–7 verbatim: `missing: GROUND=1 SHAPE=0 automation-none=0 -> FAIL`,
`compliant: GROUND=1 SHAPE=1 automation-none=1 -> PASS`, `automation: GROUND=1 SHAPE=1 automation-none=0 -> FAIL`,
`real lesson corpus/lessons/round-73.md: GROUND=2 SHAPE=2 automation-none=2 -> PASS`.

## (c) Fake record passes the whole check — and the criterion states exactly this limit

A fabricated record with two pasted UA→response lines and `automation: none`, never actually sent, scores
GROUND=1 SHAPE=1 automation-none=1 (PASS):

```
| staged S999 | S999 | status: UA "curl/8.7.1" -> HTTP 200, 123456 B, wall absent; UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 654321 B, wall absent; automation: none | fabricated, no request sent | rejected |
```

So grep cannot distinguish a pasted UA record from a sent one. **The limit is stated in the criterion
(QUALITY.md:73): "grep cannot tell a pasted UA from a sent one, cannot resolve an alias and cannot read a
wrapped record; the verbatim output block and the re-open command in the record are what a re-opener
repeats."** Not a defect. (Also verified: an alias record `UA-B -> …` and an elided `…` UA cannot match the
SHAPE regex, so the alias/elision prohibitions are machine-enforced.)

## (e) Criterion 23 checks

1. **`python3 -B reports/round-72/accept-c.py --selftest` at lands (fresh clone of 0316b888):**
```
SELFTEST: 10/11
--- clean fixture: expected PASS 10/10, got exit=1
LEG PASS ENTRIES
...
ACCEPT-C-72: FAIL legs=10/10
exit=1
```
Reproduces the R73-M4 grounding verbatim (verdict line, exit 1, and the clean-fixture line quoted in the lesson).

2. **Red-before-r3 reproduction.** `sha256sum` of landed `reports/round-73/accept-ca.py` =
`222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89` (r3, matches counter-revisions.md). Copied
to `/tmp/RevQuality22/accept-ca-noguard.py` and deleted **only** the `load_ledger` default-path guard
(`if rel == LEDGER_REL: return None, "absent", … "the default ledger is never read from the worktree"`).
`python3 -B accept-ca-noguard.py --selftest`:
```
ERROR: --lands must be 40 hex
ERROR: base 8841ad3b896a0227674fa0725b818c999118046f is not a commit in /tmp/r73-ca-selftest-4r3kqsvf/lane
SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'
```
exit=1. Identical to `reports/round-73/telemetry/red-before-r3.txt` modulo the random temp-dir suffix, and the
three ERROR lines are also printed by the passing run (they belong to the CLI-error scenarios), so the
discriminating line is the SELFTEST FAIL line. Control: the **intact** r3 counter in the same clone prints
`SELFTEST OK: 10 scenarios — …` exit 0 (matches `selftest-r3.txt`), proving the red-before is caused by
removing the guard and nothing else.

3. **Freeze-commit receipt.** `git ls-tree -r --name-only af65165… -- reports/round-73/` contains
`telemetry/selftest.txt` (plus `controls-c.txt`, `controls-ca.txt`, `census-start.txt`, `gap-sweep.txt`) and
the freeze tree has no conlang-scholarship entries, an unchanged `corpus/SOURCES.md` (identical blob to base),
and no `round-73.md` lesson — receipts present, landing absent. The receipt's pinned hashes
(`f8ebb5d…` accept-ca.py r1, `95aee881…` accept-c.py) equal the freeze-committed bytes (re-derived via
`git show af65165…:<path> | sha256sum`). The revision ledger (`counter-revisions.md`) records r1/r2/r3 with
old/new sha, what moved, and predicate-moved statements; the r3 selftest re-run and red-before are committed.
No defect found.

## What I could NOT check

- The round-72 "5/5" runs (ScoutCapoeiraReopen.md F4) are repeated-run claims; I made single runs per UA
  today (classes reproduced: wall under plain/curl UAs, narrative under browser-shaped and empty UAs).
- The exact round-72 byte readings (43,419 / 154,144) cannot be re-established historically; only today's
  re-measurement (46,392 / 40,956 wall; 154,141–154,319 narrative) is reported.
- The Wayback CDX "no capture" rulings for Cambridge S894 (criterion 21's subject) were not re-probed; I
  only re-measured the live responses.
- The criterion-23 sentence about "round 73: GROUND, SCRATCHMIRROR and COLLCHECK read the committed receipts in
  shapes the receipts did not have" rests on lesson R73-M6 text and the freeze-era control receipts; I did
  not re-run the frozen counters at the freeze commit (only verified the committed receipt + pinned hashes).
- No attempt was made to bypass any challenge (no browser automation, no captcha solving); the Client
  Challenge and UNESCO captcha/TSPD shells were recorded as walls, not solved.

## Tooling record

No installs or upgrades (the operator rule does not force one where the stock toolchain suffices); used
system curl 8.23.0, GNU grep, git (read-only against the lane), python3. Live fetches: exact UA, bytes and
status recorded per request above; both a browser-shaped UA and `curl/8.7.1` were tried for every source
before any reachability statement; downloads kept under `/tmp/RevQuality22/` (springer-curl.html,
springer-browser.html, camb-curl.html, camb-browser.html, unesco-a…e.html, selftest/control outputs).
