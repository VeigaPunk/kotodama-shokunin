# SentinelScope — round 73 (hyaku run 7), wave 1: scope and safety review of the write surface

Seat: SentinelScope (sentinel, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` @ `8841ad3` (matches `claims.json` base `8841ad3b896a0227674fa0725b818c999118046f`).
Read-only seat: every command below is a read, a probe, or an offline selftest. Nothing under the fleet root, the lane index, `corpus/**`, or `/home/vgpnk/Projects/shokuknow` was written. Downloads: none (headers-only probes; no body saved). Tools installed: none.

Verdict: **no credential leak, no private-host URL, no login-walled source, no SSRF vector in any seat-instructed fetch.** Three scope defects stand between the draft claims and a lawful landing (S-1 HIGH, S-2/S-3 MEDIUM).

---

## 1. Credential / private-URL sweep of the staged entries and rows — CLEAN

Reviewed bytes (sha256):

```
ce666a2bf15d97531545acafb88b559f239819ab11aad1883dd2f9d2d6854891  conlang-scholarship.md
8f889666b32c81a9ea4eb8905e79c6e3c992e70e6f0e49debd22cda86b86a8d6  conlang-scholarship.amend-2026-10-23.md
9ff3de578c7c25131f003c6e75585f81f8be13be9f5c55af238caa8763c7f0b9  conlang-scholarship.amend-2026-10-23b.md
042252ed2201405dcfec4100039329bf67d4e4205f80c7c8b2e6856e5184d08e  conlang-scholarship.amend-2026-10-23c.md
073f8de65d52379851100d927eebeb6f2ecd674e5287f8a22dfe55ceb7cdaa86  conlang-scholarship.amend-2026-10-24.md
7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754  SOURCES.append.md
```

Patterns swept (five entries; five rows S881/S882/S892/S893/S901; then the whole staged package `SOURCES.append.md` + `MERGE-REPORT.md` + `MERGE-REPORT.json`):

```
password|passwd|secret|api[_-]?key|apikey|bearer|authorization|op://|AKIA|ghp_|xox[bap]-|
BEGIN [A-Z ]*PRIVATE KEY|ssh-rsa|session[_-]?id|sessionid|auth=|sid=|cookie|localhost|127.0.0.1|
0.0.0.0|192.168.|10.x|172.16-31.|.internal|.local|ssh://|file://|ftp://|<email>
```

- Five entries: **0 hits** (exit 1).
- Five rows: **0 hits**; also **0 email addresses** and **0 `user:pass@` URL authorities**.
- Whole staged package (214 KB `SOURCES.append.md` + both merge reports): **0 hits**, 0 userinfo URLs.
- No absolute operator paths (`/home/...`, `/Users/...`, `C:\`) in the five entries. The only `/tmp/` references in the five rows are inside their recheck cells (`-o /tmp/s.pdf`, `/tmp/r.pdf`, `/tmp/c.pdf`) — fetch scratch, not secrets.
- No `op://` refs, no session tokens, no cookies, no bearer headers anywhere in the staged text.
- Sibling wave-1 reports (`w1/*.md`, `assimilation/*`) re-swept for leaked tokens: only false positives, the substring `bearer p`/`bearer s` inside prose ("the bearer's …") in a mirrored registry copy. No `Set-Cookie`/`OJSSID`/`__ddg`/`api_key` text leaked into any seat report.

Related, already-known defect confirmed (not a safety issue, an id-integrity one): staged base entry line 11 cites `S728`; lane registry `corpus/SOURCES.md:683` names S728 = "Henrike Frye, 2022 'Corrective input', Child-directed Speech in Qaqet…" — unrelated document, exactly the campaign-id class claim C's REPOINTED leg forbids.

## 2. The five source URLs are public ordinary-means pages — PASS, with two hygiene notes

URLs as they appear in the staged rows (0 `?` characters in any of the five rows — **no tracking query strings**):

| row | URL | browser-UA | plain-curl 8.23.0 | content-type | redirect | wall |
|---|---|---|---|---|---|---|
| S881 | `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` | 200 | 200 | text/html | none | none |
| S882 | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 200 | application/pdf | none | none |
| S892 | `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` | 200 | 200 | application/pdf | none | none |
| S893 | `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` | 200 | 200 | text/html | none | none |
| S901 | `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` | 200 | 200 | application/pdf | none | none |

UAs used (recorded per QUALITY 21/22 draft):
- browser-shaped: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
- plain: `curl 8.23.0` (default UA)

No `WWW-Authenticate`, no `Location:` to a login/consent page, no 403/429/503, no CAPTCHA interstitial under either UA. **The plain-curl UA is not walled on these five** — unlike the round-72 UNESCO case, so the staged rows' own `curl -fsSL` recheck cells are sound today.

DNS resolution (SSRF sanity, see §4): `ojs.unito.it 130.192.100.111`, `www.philol.msu.ru 93.180.13.6`, `journals.rudn.ru 185.178.208.57`, `cyberleninka.ru 104.26.10.2 / 104.26.11.2 / 172.67.70.180 (+2 v6)` (Cloudflare edge), `sanders.phonologist.org 67.205.6.174`. All globally routable; no loopback/RFC1918/link-local.

Hygiene notes (LOW/INFO, for the row normaliser, not blockers):
- **S-4 (LOW):** S882's row URL is cleartext `http://` while the HTTPS variant serves the identical object — `https://www.philol.msu.ru/~sidorova/files/conlangs.pdf` → 200 `application/pdf` (probed, browser UA). A quote taken over cleartext is MITM-exposed; the normalized row should carry the `https` URL and the Gate should record the PDF's sha256 alongside the quote.
- **S-8 (INFO):** probes returned server-set cookies — `OJSSID` (ojs.unito.it), `__ddg1_/__ddg8_/__ddg9_/__ddg10_` (DDoS-Guard on rudn.ru, `__ddg9_` encodes the client IP), `RUDNJOURNALS_OJSSID`, `currentLocale`. These are server-issued anti-bot session state, not credentials; my probe persisted none and no cookie value reached any lane file. Worth knowing that a recheck cell which saves headers would capture a client IP.

## 3. Draft claims' write paths — inside the granted surface, but the landing authority is missing

Enumerated every path token in `reports/round-73/claims.json` and classified:

| path | claim | class |
|---|---|---|
| `reports/round-73/accept-c.py`, `accept-ca.py`, `ledger.json`, `telemetry/{census-start,gap-sweep}.txt` | C, Ca | lane, in-surface |
| `corpus/knowledge/linguistics/conlang-scholarship{,.amend-2026-10-23}.md` | C | lane, in-surface |
| `corpus/SOURCES.md`, `corpus/lessons/round-73.md` | C | lane, in-surface |
| `.ufo/waves/round-73/assimilation/validate-receipt.txt` | C | lane scratch, in-surface |
| `SKILL.md`, `README.md`, `SCORECARD.md`, `LOG.md` | Ca | lane, in-surface (see S-1) |
| `tools/check-cited-lines.py` | C | lane read-only invocation |
| `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` | C | fleet **read-only invocation** |
| `/home/vgpnk/Projects/shokunin` (`--fleet-root`, fleet git) | Ca | fleet **read-only** |
| `MANIFEST.json`, `templates/`, `.ufo/state`, `shokuknow/**` | — | **absent from both claims** |

No claim writes `MANIFEST.json` (it does not exist in the lane: `ls kotodama-shokunin/MANIFEST.json` → ENOENT), nothing writes `templates/`, `.ufo/state`, `watchdog.log`, `QUALITY.md`, `corpus/README.md`, `claims.json`, or the shokuknow tree. The fleet path appears only as a read root and as the canonical census command.

`scripts/sources-census.sh` verified to be write-free for `validate`/`census`: header line 7 states "writes only stdout or --out"; `out_sink()` appends only when `OUT` is non-empty (set solely by `--out`); every `mkdir`/`>` in the script is inside the `--selftest` temp tree. So claim C's CENSUS leg (`validate --root <fleet-root> kotodama`) mutates nothing under the fleet root.

**S-1 (HIGH) — the claims require writes that no seat in this round is permitted to make.** The wave-1 shared CONTEXT (`build-w1.py:10`, identical in `w1/spec.json:3` and `w1/dispatch.json:259`) binds *every* seat: "You NEVER mutate: … LOG.md, SCORECARD.md, SKILL.md, corpus/SOURCES.md, corpus/QUALITY.md, corpus/README.md, corpus/knowledge/**, corpus/lessons/** …", and "Your assigned write path is the `Report:` file named in your item (plus any scratch/draft path…)". Claim C needs entries + registry rows + `corpus/lessons/round-73.md`; claim Ca needs SKILL.md registry rows, a README footer line and a `## Corrections — round 73` block in SCORECARD.md. `.ufo/waves/round-73/w2/` is **empty** (no wave-2 items built), so the landing authority is currently undefined: as written, the round cannot land either claim. Before freeze, wave 2 must be built with an explicit per-seat carve-out naming these paths (and the fleet report `.ufo/reports/round-73/kotodama.md`), or the claims' `after` states are unachievable. This is a scope defect, not a safety one — but it is the one that would waste the round.

**S-2 (MEDIUM) — Ca's APPENDONLY leg mixes two repositories and lands on a dirty tree.** The leg reads "`git diff --numstat base..<lands>` shows zero removed lines in LOG.md, SCORECARD.md, corpus/lessons/round-72.md, corpus/lessons/round-71.md **and the round-72 fleet report (fleet git)**". `base`/`<lands>` are lane commits; a path in the fleet repo cannot be diffed by that invocation (path outside repository), so the leg needs a second, separately pinned fleet-git diff. The fleet tree has no pinned revision for this round and is dirty right now (§6: 16 modified `.ufo/state/*.report-baseline` + `.ufo/watchdog.log` + untracked dirs), so a fleet-git append-only check would either see unrelated state churn or need its own base pin. Also, the only fleet write surface granted this round is `.ufo/reports/round-73/kotodama.md`; the leg names the *round-72* report, so any corrective append there is outside the granted surface. Remediation: split the leg (`LANE-APPENDONLY` over lane commits, `FLEET-APPENDONLY` over a named fleet base..tip pair) and name the exact fleet file.

**S-3 (MEDIUM) — one wave-1 fixture item deviates from the fixture-repo rule.** The rule: fixtures are `D=$(mktemp -d) && git -C "$D" init -q`, every git call names `-C "$D"`, and never commit with a throwaway identity anywhere else. `MutRegistryCollision` complies (`init -q` in `$D`, `-C "$D"` mandatory, "or avoid git entirely"). `ExecReceiptRerun` instead instructs `git clone -q <LANE> "$D/lane"` — a clone, not an init'ed fixture — with subsequent calls implicitly at `-C "$D/lane"`, and no instruction against committing inside it. A clone does **not** carry the lane's local `user.email` (`kotodama@shokunin.local`); it inherits the **global** identity, which on this host is `probe@example.invalid` — precisely a throwaway identity. Remediation before dispatch: state "the clone is read-only; make no commits in `$D/lane`", or have the seat pass the lane identity explicitly.

**S-5 (LOW) — the staged recheck cells are shell commands, not cadences.** Each of the five staged rows carries `180d — \`curl -fsSL '<url>' … && pdftotext … \| grep -c '<span>'\` -> N (ran 2026-10-23)` — an executable pipeline with an escaped pipe, and `opened` = 2026-10-23. Claim C already forbids appending the staged text as-is (ROWS leg) and requires the normalised recheck; the normaliser must replace the pipeline with an ISO date/cadence (and may keep the command as a Gate note, re-escaping the pipe). Sanity: the pipe count is correct (12 unescaped + 1 escaped `\|` = 11 cells), so the staged rows are schema-shaped; the hazard is the content, not the delimiters.

**S-6 (LOW) — one staged entry cites a discovery-query URL.** `conlang-scholarship.amend-2026-10-23c.md` cites `https://api.crossref.org/works?query.container-title=The+Palgrave+Handbook+of+Constructed+Languistics&rows=40&select=…`. Those are functional API parameters, not tracking, and the host is public — but a query endpoint is not a page: if any adopted row's *source cell* carried it, QUALITY 18's same-page anchor leg (live URL + matching Wayback capture whose original normalises to it) could not be satisfied. Keep the query URL as a Gate provenance note only; rows must cite the document URL.

**S-7 (INFO) — "QUALITY 22" is not on disk.** The seat context cites "Fetch hygiene (QUALITY 21/22 draft)" and the claims list QUALITY 22 as the round's quality candidate, but `corpus/QUALITY.md` ends at criterion 21 (63 lines, read to EOF). Nothing in this wave may write QUALITY.md, so the UA-record clause is a draft obligation carried by the prompts, not a landed criterion — seats should not cite "QUALITY 22" as if it were on disk.

## 4. SSRF / private-host pivot audit — PASS; `reopen-row.py` hold is lifted and its guard holds

URLs any seat is actually told to fetch (extracted from `build-w1.py`, `w1/spec.json`, `w1/dispatch.json`): exactly six with a scheme —

```
https://ojs.unito.it/index.php/ricognizioni/article/view/7099
http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955
https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike
https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf
https://api.crossref.org/works/10.1146/annurev-anthro-101819-110152
```

plus bare hosts named without a scheme in prompts (`conlang.org/26c3.pdf`, `doi.org/10.1017/cnj.2024.21`, the Cambridge DOI, `web.archive.org` CDX). Grep for `localhost|127.|0.0.0.0|192.168.|10.x|172.16-31|.internal|.local|[::1]|user:|pass:|token|key=|secret` over that URL set: **0 hits**. No `file://`, `ssh://`, `gopher://`, `dict://`, no userinfo, no metadata-service address. All hosts are public academic/API hosts (§2 DNS). No seat prompt tells anyone to fetch a URL taken from untrusted record bytes except through `tools/reopen-row.py`, which is not invoked by any wave-1 item (only my own item names it).

Hold status: `corpus/QUALITY.md:51` is the hold; `:53` records the **lift** at `dd81fd29` for the named behaviours. Verified against current bytes: `git cat-file -t dd81fd29` → commit, `git log -1 dd81fd29` → "round-63: claim O land — tools/reopen-row.py repaired …". Tool sha256 `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0`. Guard read: `private_host()` (`ipaddress` check over `getaddrinfo`, loopback/private/link-local/reserved, unresolvable = refused) at lines 452–486; every redirect hop re-checks `private_host` (lines 611–615) and a hop to another authority is refused **even under `--allow-private`**. Offline selftest exercised:

```
python3 -B tools/reopen-row.py --selftest   →  -- selftest: 49 checks, 0 failures --  (exit 0)
  ok redirect verdict / redirect hits / redirect url 'http://127.0.0.1:<port>/redirtarget'
  ok cross-authority redirect refused: hop refused ('REFUSED','attempts=1'); source hit 1; target untouched 0
  ok malformed port/ipv6/empty host ('MALFORMED','attempts=0'); ok gzip; ok truncation; ok request budget stall ('UNREACHABLE','attempts=3')
```

Residual class stays as documented in `corpus/lessons/round-63.md`: **DNS-rebind TOCTOU** (the name is resolved, then the socket connects; a rebinding resolver can still land on a private address) and fixed-socket-timeout tools indistinguishable from a wall budget — LOW, accepted, not introduced by this round. If a wave-2 seat does use the tool on live rows, prefer the base locator `reports/round-61/reopen-quote.py` where its budget suffices; the hold no longer forbids `reopen-row.py`.

## 5. Fixture-repo rule compliance in the wave context

- Fixture-bearing seats: `ExecReceiptRerun` (`mktemp -d` + **clone** — see S-3), `MutRegistryCollision` (`mktemp -d` + `init -q`, `-C "$D"` mandated — compliant). No other wave-1 item creates a repo.
- No prompt contains `git add`, `git commit`, `git checkout/reset/apply`, `git -c user.*`, or `user.email`/`user.name` setup (grep: 0 hits in `build-w1.py`). So no seat is instructed to touch the lane index or commit — consistent with the "read-only git" rule; the only exposure is the implicit commit-in-clone in S-3.
- Downloads land in `/tmp/<SeatName>/` in every fetch item (`/tmp/ScoutS882/`, `/tmp/ScoutS892/`, `/tmp/ScoutS901/`, `/tmp/ScoutQuarantineConlang/`…), never the fleet or lane root — compliant.
- Lane identity for reference: `user.email kotodama@shokunin.local`, `user.name kotodama-shokunin` (lane-local); global identity is `probe@example.invalid` (throwaway — the reason S-3 matters).

## 6. Misroot sweep baseline (nothing moved)

`git -C /home/vgpnk/Projects/shokunin status --porcelain | head -50`:

```
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kasegi.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kotoba.report-baseline
 M .ufo/state/kotodama.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/revenger.report-baseline
 M .ufo/state/souji.report-baseline
 M .ufo/state/tabi.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
?? .ufo/waves/round-30/
```

- 16 `.ufo/state/*.report-baseline` + `.ufo/watchdog.log`: orchestrator runtime churn (state files are on the never-write list; not touched by me).
- `?? .ufo/waves/round-30/` → `wave1/ScribeLesson.md` (1521 B, 2026-10-25 15:58): **not kotodama** (`grep -c -i kotodama` = 0); a foreign round-30 artifact sitting untracked in the fleet tree. Left in place.
- Lane (`git -C <lane> status --porcelain`, 4 entries): `?? .ufo/waves/round-72/w1/ScoutMergeScan.md`, `?? .ufo/waves/round-72/w1/ScribeLesson.md` (the known R1 pair), `?? .ufo/waves/round-73/`, `?? reports/round-73/`. Expected wave scratch.
- Round-73 paths naming kotodama **outside** the lane: none. `find <fleet> -maxdepth 4 -name '*round-73*'` outside the lane returns `.ufo/reports/round-73` (holds only `audio.md`, `game-dev-3d.md` — other lanes), `.ufo/prompts/kotodama-round-73.md` (the L1 prompt, expected), and the sibling lanes' own `reports/round-73/` (audio, game-dev-2d, game-dev-3d — their own rounds, not misrooted kotodama files). No kotodama round-73 report has leaked into the fleet report dir yet (`kotodama.md` absent — expected pre-wave-1).
- All 37 wave-1 seat `Report:` trailers resolve to `.ufo/waves/round-73/w1/<Seat>.md` (verified from `w1/spec.json`); one grep false positive ("Report: keep/cut per row…" is prompt prose, not a trailer).

## 7. Findings summary

| id | sev | finding | smallest remediation |
|---|---|---|---|
| S-1 | **HIGH** | Claims C and Ca must write `corpus/knowledge/**`, `corpus/SOURCES.md`, `corpus/lessons/round-73.md`, `SKILL.md`, `SCORECARD.md`, `README.md` — paths the shared CONTEXT forbids every seat, and `w2/` is empty, so no landing authority exists | build wave 2 with explicit per-seat path carve-outs (lane files + `.ufo/reports/round-73/kotodama.md`) before freeze |
| S-2 | MEDIUM | Ca APPENDONLY diffs a fleet path with lane revisions; fleet tree dirty/unpinned; round-72 fleet report outside the granted surface | split into LANE/FLEET legs with named base..tip pairs; name the fleet file |
| S-3 | MEDIUM | `ExecReceiptRerun` clones instead of init'ing a fixture and does not forbid commits; clone inherits global throwaway identity `probe@example.invalid` | mark the clone read-only (no commits), or pass the lane identity explicitly |
| S-4 | LOW | S882 row URL is cleartext `http://` though HTTPS serves the same object | normalise to `https://…`; record PDF sha256 in the Gate |
| S-5 | LOW | Staged recheck cells embed executable `curl … && pdftotext … \| grep -c` pipelines | normalise to ISO date/cadence; keep command as Gate note with re-escaped pipe |
| S-6 | LOW | A staged entry cites a crossref **query** URL as a source | keep as Gate provenance; rows cite document URLs only (QUALITY 18) |
| S-7 | INFO | "QUALITY 22" is cited but absent from `corpus/QUALITY.md` (ends at 21) | treat as prompt-level draft until landed; don't cite it as on-disk |
| S-8 | INFO | probes returned server-set cookies (`OJSSID`, `__ddg*` incl. client IP) | don't persist response headers into lane files |
| — | INFO | staged base entry line 11 cites `S728` = Qaqet row (`SOURCES.md:683`) | already guarded by claim C REPOINTED; as-is append would fail |

Checks I did **not** run (unrun ≠ passed): the round counters (`accept-c.py`, `accept-ca.py`) do not exist yet; the census was not re-run; no claim leg was graded. My probes are header-only GETs at 2026-10-25 with the UAs recorded in §2.
