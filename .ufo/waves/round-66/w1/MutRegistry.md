# MutRegistry — claim-C registry-diff mutation probes (round 66)

Seat: `L1-kotodama-r66.MutRegistry` (UFO-FSD mutation tester, leaf).
Target: the three registry-diff legs `ROWS`, `LINK`, `RESTATE` of
`reports/round-66/accept-c.py` (counter sha256 self `0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86`).
Lane base `94209e8f80969dbac48d56c5d0e2e623635b8616`; lane `main` == base at probe time.

## Harness (all bytes under `.ufo/waves/round-66/stage/mut-reg/`)

The integrated draft rows do not exist yet at the lane tip (`corpus/SOURCES.md` ends
at S775; `.ufo/waves/round-66/rows/` is empty), so the counter was exercised on a
**conformance fixture** built on base bytes: a `git clone --shared` of the lane at
the base revision, plus 24 synthetic rows `S777`-`S800` on hosts
`fixtureNN.example.org`, a synthetic entry, and one README index row with the
counts/footer deltas (`239->240`, `30/29/32/29/24/95 -> 30/29/33/29/24/95`).
All fixture hosts are `.example.org`, `FIXTURE.md` labels the tree "not corpus
data".

Baseline on pristine fixture bytes — **all 11 legs PASS**, `ACCEPT-C-66: PASS`, exit 0
(`restored-baseline.txt`): FILE/SET/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/CAPTURE/TOPIC.
Hence any leg flip below is attributable to the single mutated line. Known harness
limits: `NOHARM` is vacuous in the clone (`BASE..main` diff empty); `SWEEP` is green
only because the fixture README counts were updated consistently.

Reproduce: `sh .ufo/waves/round-66/stage/mut-reg/run.sh` -> full replay in 1.0 s,
transcript `run-all.txt` (identical to the per-probe transcripts `mut*.txt`).

Byte hashes of the fixture (before each probe, re-checked after each):

| file | sha256 |
|---|---|
| `corpus/SOURCES.md` (pristine) | `85dd649926186e495f910d77c6abb6171d72716699cfc3ca54ec6d1aa67e0100` |
| entry `.../scent-perfume-aromatics-codes.md` | `4f7b5cd7ebed55d4cbb55b6bc4d2838cd7d90f9635da10d0a467b04261813006` |
| `corpus/README.md` | `4ef0aa75f926e803464919b37b1eb659f9c08e881b422830566c3916fd9c69b5` |

## Probes

| # | mutation (one line changed) | expected leg | actual leg | verdict |
|---|---|---|---|---|
| mut1 | `S790` status `mined` -> `queued` (`mut1-status-queued.SOURCES.md`) | ROWS FAIL | **ROWS FAIL** `bad=["S790:status='queued'"] n=1`, exit 1 | **killed** |
| mut2 | `S791` live URL := `S790`'s page + `?mirror=1` (`mut2-dup-url-query.SOURCES.md`) | LINK FAIL | **LINK PASS**, whole counter PASS, exit 0 (HOSTS 24->23, still >=10) | **survived** |
| mut2b | `S791` live URL := `S790`'s page, byte-identical | LINK FAIL | LINK FAIL `bad=['S791:dup-S790']`, exit 1 | killed (control) |
| mut2c | `S791` live URL := `S790`'s page + `#anchor` | LINK FAIL | LINK FAIL `['S791:dup-S790']`, exit 1 | killed (control) |
| mut3 | `S792` teaches cell := verbatim copy of its anchor quote (`mut3-teaches-nearcopy.SOURCES.md`) | RESTATE FAIL | **RESTATE PASS** (bullet-side cov 0.60), exit 0 | **survived** |
| mut3b | `S792` teaches := quote copy + 2 extra content words (`mut3b-teaches-padded.SOURCES.md`) | RESTATE FAIL | **RESTATE PASS**, exit 0 | **survived** |
| mut3c | mut3 registry + `S792` entry bullet := quote copy (`mut3c-purecopy-both.*`) | RESTATE FAIL | RESTATE FAIL `bad=['S792:quote_words=5 teaches_cov=1.00 novel=7']` | killed (control) |
| mut3d | mut3b registry + quote-copy bullet (`mut3d-padded-both.*`) | RESTATE FAIL | **RESTATE PASS** (cov 0.7143), exit 0 | **survived** |

## Findings

### F1 [MED] `LINK` treats the query string as source identity — duplicate page, different query, passes
`norm_url()` appends `?<query>` (`return f"{scheme}://{host}{path}?{parsed.query}"`),
so two new rows citing the *same live page* with any distinct query
(`?mirror=1`, `?utm_source=...`, `?lang=en`) are distinct identities. LINK checks
only `norm_url` equality; ROWS has no duplicate-URL check; HOSTS counts netloc and
stayed at 23 (>=10) in the mutant, so **no leg fires** (mut2: whole counter PASS).
Fragments are normalized away, so `#anchor` duplicates *are* caught (mut2c) — the
hole is query-only. Attack shape against claim C: submit the same page twice under
one id with `?mirror=`/`?print=1` and lose one genuine source from S777-S800 while
every predicate stays green. Suggested repair direction (contract unchanged): strip
the query (or identity-neutral params) before comparison, or add a separate
`(host, path)` collision leg.

### F2 [MED] `RESTATE` cannot see a teaches cell that copies the quote unless the *bullet* covers >=80% of it
`cov = in_order_coverage(teaches_words, bullet_words)` is measured on the entry
bullet, not on the quote. Therefore:
- mut3 (teaches := quote verbatim, bullet abbreviated, cov 0.60) -> PASS.
- mut3d: teaches := quote (5 content words) + `chapel harbor` (7 words), bullet
  copies the quote verbatim -> hits 5, cov 5/7 = 0.7143 < 0.8 -> PASS, though
  `novel` is satisfied by the bullet's own words.
- Only the symmetric pure copy (mut3c, cov 1.00) is killed.

General evasion rule for a quote of `q` content words copied verbatim into the
teaches cell with `k` extra content words appended: coverage is `q/(q+k)`, so the
leg passes whenever `k > q/4` (q=5 -> k>=2, q=6 -> k>=2, q=8 -> k>=3). Padding a
quote-copy with two content words defeats the near-copy check even when the entry
bullet is a verbatim quote restatement. This is a coverage finding on the frozen
predicate, not a request to change the contract: when the 24 real rows land, a
teaches cell of the form "quote + two extra content words" plus a bullet that
restates the quote will be stamped PASS by RESTATE.

### Confirmed working (non-findings)
- ROWS is exact on status/opened/tier/used-by/cell-count (mut1 killed).
- LINK is exact on identical and fragment-only duplicates (mut2b/mut2c killed).
- RESTATE kills a pure quote copy when the bullet restates it (mut3c killed).

## Restoration evidence
Every probe wrote only into the scratch clone; after each run the three pristine
files were restored byte-exact and hash-compared (`restored=True` in every probe),
and a final restored-bytes run printed `ACCEPT-C-66: PASS`, exit 0
(`restored-baseline.txt`, SOURCES sha `85dd64...`). The 140 MB scratch clone was
pruned after the replay; `run.sh` rebuilds it from the lane in ~0.4 s. No writes
touched the lane tree, lane git index, or jj state; only read-only `git` was used in
the lane. No tools installed or upgraded.

Report: .ufo/waves/round-66/w1/MutRegistry.md
