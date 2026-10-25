# SentinelScope — round 74, wave 1 — scope and safety review of the round's write surface

Seat: SentinelScope (sentinel, leaf — no dispatch, no background jobs, no mutation).
Round: 74 (hyaku run 7), kotodama lane, base `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Date: 2026-10-25. Report path: `.ufo/waves/round-74/w1/SentinelScope.md` (lane-root-relative).

Verdict in one line: **the round's write surface is clean of credential material, tracking
parameters and private-host reachability, and its content sits inside kotodama's province** — with
five findings, of which two need action before landing: a volatile transport that can yield a
*truncated 200* body into an evidence file (F1), and one remaining fleet-rooted read that must be
asserted read-only when the Ca counter is written (F3); a staged recheck cell that carries
shell-pipeline syntax into a registry cell if copied as-is (F2) is already guarded by claim C's ROWS
leg; F4/F5 are recorded so the Gate and the evidence author do not create them.

Everything below is what I executed; nothing is reported as verified that I did not run. The claims
file was read and never edited; no file outside this report was written. Downloads:
`/tmp/SentinelScope/` (`litmemo.html`, `tuduku.html`, `cw2025.html`, `cw2022.html`, `cdx.out`,
`four-staged-rows.txt`, `ctrl.txt`). Tools installed: none.

## 1. What was reviewed

Read (read-only): `reports/round-74/claims.json` (both DRAFT claims C and Ca, all legs, kill rules,
controls); `.ufo/waves/round-74/w1/spec.json` (all 42 seat items); the staged package
`/home/vgpnk/Projects/shokuknow/merge/kotodama/{SOURCES.append.md, MERGE-REPORT.md,
knowledge/corpus/knowledge/culture-material/…}` — specifically the four rows S883/S884/S899/S900 and the two entry files
`worldbuilding-setting-practice.md` and `worldbuilding-setting-practice.amend-2026-10-23.md`; the two
wave-1 drafts that will actually land (`.ufo/waves/round-74/drafts/worldbuilding-setting-practice.md`,
`…amend-2026-10-23.md`); the seat reports `ScribeEntryBase.md`, `ScribeEntryAmend.md`;
`PROVINCE.md` of this lane and of `lore-shokunin`; `corpus/QUALITY.md` criteria 10, 21, 22 and 24 in
full (6–15 located by heading); `tools/reopen-row.py` (fetch and private-host policy) and the
`tools/check-source-access.py` docstring and bypass patterns;
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (write surface).

Fetched live (exact UA on every request, recorded per response):

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
```

plus `curl/8.15.0` as the plain-request control. No browser automation, no captcha, no wall met.

## 2. Item 1 — credential material, private URLs, `op://`, session tokens, tracking parameters

**Result: none found in any object the round will write, and none in the staged package.**

Method: one regex set over (a) the four staged rows, (b) the two staged entry files, (c) the whole
staged package recursively (a superset, run for completeness), (d) the two wave-1 drafts that carry
the landing content.

```
op:// | gh[pousr]_[A-Za-z0-9]{16,} | AKIA[0-9A-Z]{12,} | xox[baprs]- | eyJ[A-Za-z0-9_-]{10,} |
api[_-]?key | passw(or)?d | bearer | session(id|_id|=) | [?&](token|access_token|key|sig|signature|auth)= |
user:pass@host
```

Pre-scan positive control (`ctrl.txt` containing `op://vault/item`, a `ghp_` token, `?utm_source=`,
`&fbclid=`, `https://user:pw@host/x`) — every shape matched, so the empty results below are
answers, not a broken pattern:

```
1:op://
1:ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
1:?utm_source=news
1:&fbclid=abc
1:https://user:pw@host/x
```

Scans:

| object | secret shapes | tracking params | private hosts |
|---|---|---|---|
| 4 staged rows (S883, S884, S899, S900) | none | none | none |
| 2 staged entry files | none | none | none |
| whole staged package (recursive) | none | none | none |
| 2 wave-1 drafts (the landing bytes) | none | none | none |

URL inventory — every URL the round will carry is bare, with **no query string at all**, therefore no
tracking parameter can be attached:

```
staged base entry:  http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
                    https://litmemo.com/ja/blog/novel-worldbuilding-guide
                    https://tuduku.space/column/novel-worldbuilding
staged amendment:   https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html
                    https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html
                    https://www.chinawriter.com.cn/n1/2025/1030/c404027-40592897.html   (staged S895, not carried)
```

Session/authority material in the served bodies (checked because an evidence window is cut from
them): no presigned or signed URLs (`X-Amz-Signature|X-Amz-Credential|Signature=|token=|access_token=|
api_key=|sig=` → no match), no `/admin|/internal|/intranet|/private|/staging|/dev` paths, no
credentials in URLs. The only contact strings are publisher addresses in page footers
(`litmemo-support@grogtec.com`, `cnwriter@126.com`) — public, and outside every quote-local window.

**F2 (low, data-integrity, not secrecy).** Each of the four staged rows has 11 cells and carries an
**escaped pipe inside its `recheck` cell** — a shell pipeline fragment
(`curl -fsSL 'https://…' \| grep -c '自然環境'`), i.e. executable syntax stored as registry data.
Copying a staged row as-is would put that fragment into `corpus/SOURCES.md`. Nothing in the lane
executes recheck cells: `grep -rnE 'subprocess|os\.system|os\.popen|shlex' tools/*.py` finds
subprocess use only in the assembly scripts, `check-claim-separability.py` and
`check-craft-exercise.py`, all with explicit argv lists, and `grep -rn 'shell=True' tools/` returns
nothing, as do `os.system`, `os.popen`, `eval(` and `exec(`. Claim C's ROWS leg already forbids it ("a cadence-only recheck cell, no pipe
in any cell") and its kill rule names "un-normalized recheck cell, escaped pipe". **Smallest
remediation:** none beyond enforcing that leg; the guard already exists at freeze.

## 3. Item 2 — the four source URLs are public, ordinary-means pages

**Result: all four are public ordinary-means pages. No login wall, no paywall, no consent gate, no
geo block, no bot challenge, no redirect at all — hidden or otherwise.** One of them (tuduku.space)
is intermittently unreachable at the transport layer, which is a durability problem, not an access
control (F1).

| URL | HTTP | redirects | final URL | bytes | sha256 | plain-curl UA |
|---|---|---|---|---|---|---|
| `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 0 | identical to cited | 101,615 | `441fc921…a334ca64` | 200 |
| `https://tuduku.space/column/novel-worldbuilding` | 200 (when it connects) | 0 | identical to cited | 17,068 | `754f504c…662cfc1b7` | transport failure |
| `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | 200 | 0 | identical to cited | 48,536 | `a3b6640c…68bee94d` | 200 |
| `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | 200 | 0 | identical to cited | 62,604 | `344de345…f4ce5710` | 200 |

`num_redirects=0` on all four: there is no redirect chain in which a hop to a private host could
hide. No `<meta http-equiv="refresh">` and no `location.href|replace` in any body. Every form action
and subresource host is the publisher's own or a public CDN (litmemo.com, chinawriter.com.cn,
vip./wyb./api.chinawriter.com.cn, `www.clarity.ms`, `fonts.googleapis.com`,
`www.googletagmanager.com`, `s.yimg.jp`, `forms.gle`); no RFC1918, loopback, `.internal`, `.lan` or
`.local` target appears in any body. No challenge marker (`cf-browser-verification`, `Just a
moment`, `challenge-platform`, `captcha`, `验证码`, geo-block text) in any body.

Walls checked in the *served* bodies, not just status codes:

- **litmemo** — 12,223 visible characters; the article's own h2「世界観の作り方：5つのステップ」and the
  FAQ block are present; `続きを読む` occurs 3× and **all three sit inside `class="blog-related-card"`**
  (related-post cards, one of which is "設定資料集を本文とズレさせない3ステップ" — a *different*
  article; this confirms the wave's finding that the staged S883 anchor names another page's title).
  `ログイン`×2 / `会員登録`×1 are site nav links; the article body is fully served, no `有料`/
  member-only marker.
- **tuduku** — 3,024 visible characters, document ends `</html>`, publisher 「つづく編集室」, dated
  2026年3月12日; no login, no 会員登録, no consent banner, no paywall; the only 無料 is body prose.
- **chinawriter 2025 / 2022** — 8,297 / 12,429 visible characters, article body present (the key
  spans of both rows found: `我先做的是世界观` ×1 and `非凡特性来自最初造物主` ×1 on 2025;
  `20章之内慢慢来` ×1 on 2022); the single `登录`/`会员` occurrences are header nav links, not gates.
  Both reachable with the plain `curl/8.15.0` UA.

Provenance cross-check: the four bodies I fetched are **byte-identical** to the ones two other seats
fetched independently — my hashes equal the L1 probe `/tmp/q74/*` and the scribes' recorded hashes
(`ScribeEntryBase` 441fc92…/754f504…, `ScribeEntryAmend` a3b6640c…/344de345…). No UA-dependent
variant was observed on any page that served.

**Durability of the two pages with no archive copy** (QUALITY 21/24, probed with a positive control
in the same query window, UA as above):

```
control  https://web.archive.org/cdx/search/cdx?url=example.com&output=txt&limit=3
         → HTTP 200, 318 B, three rows (20020120142510 …)
control2 …url=https%3A%2F%2Fwww.chinawriter.com.cn%2Fn1%2F2022%2F1207%2Fc404024-32582252.html
         → HTTP 200, 188 B, one row (20221207080111)
litmemo  …url=https%3A%2F%2Flitmemo.com%2Fja%2Fblog%2Fnovel-worldbuilding-guide&output=txt&limit=5
         → HTTP 200, 0 B, no rows
tuduku   …url=https%3A%2F%2Ftuduku.space%2Fcolumn%2Fnovel-worldbuilding&output=txt&limit=5
         → HTTP 200, 0 B, no rows
tuduku   …url=tuduku.space&output=txt&limit=3   → HTTP 200, 0 B, no rows
litmemo  …url=litmemo.com&matchType=domain&output=txt&limit=3
         → served the Internet Archive "Temporarily Offline" page (HTML, not CDX rows) — uninformative, not absence
```

Because a known-captured slug returned rows in the same window, the two empty answers are answers:
**no archive capture exists for either slug as of 2026-10-25**, matching both scribes' ruling. The
domain-prefix probe hit a service-side outage page and must not be cited as evidence either way.

**F1 (medium — evidence integrity; it is the round's only live-fetch risk).** `tuduku.space` drops
connections for minutes at a time, and it can return **HTTP 200 with a truncated body**:

```
burst 1, 6 attempts each, 2 s apart:   browser-shaped UA → 200 on 2/6 (fails: rc=56, rc=55, rc=56, rc=28)
                                       plain curl UA    → 200 on 1/6 (fails: rc=28, rc=56, rc=28, rc=55)
burst 2, 3 attempts each:              --http1.1 → 0/3 ;  --http2 → 0/3
one failure carried %{http_code}=200 with the transfer then timing out (curl rc=28)
```

So the failure is transport-level and UA-independent (a UA-gated source would fail consistently for
one UA and succeed for the other; here both classes fail and both succeed). The specific hazard: a
`200`-with-partial-body fetch would let `reports/round-74/evidence/S882.txt` store a **truncated**
body, compute a sha256 over it, and still contain the quoted window — the EVIDENCE leg ("a 64-hex
sha256 of the fetched body") and the counter's "Gate quote occurs inside that stored window" both
pass on a page that no re-opener can reproduce.

*Exploit path:* fetch at an unlucky moment → 200 + partial body → sha256 of the fragment recorded as
the page's hash → counter green → the row's provenance cannot be reproduced, and the defect surfaces
only at the next round's recheck as an unexplained hash mismatch.
*Impact:* a provenance claim that is not reproducible (the class QUALITY 17/19 receipts exist to
prevent), plus a registry long-lived row whose re-opener sees "unreachable" and may read it as a dead
source.
*Smallest remediation:* in the evidence record for **every** row, and specifically S882, store
(i) `wc -c` of the stored body, (ii) the last 32 bytes asserted to close the document (`</html>`), and
(iii) `curl -f` semantics (fail on any non-2xx **and** on an incomplete transfer — `curl -f` already
exits 18 on a short body only when a Content-Length mismatch is detectable, so the explicit tail +
byte-count assertions are the real guard); the counter then checks stored size == declared size and
the tail marker for html rows, and a truncation fails the leg instead of passing it. Also worth one
sentence in the S882 row's recheck cell: *this host intermittently resets the connection; a transport
error is not an absence reading.*

## 4. Item 3 — the draft claims' write paths stay inside the lane

**Result: every path either claim writes is lane-relative and inside
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/`; the forbidden surfaces are named nowhere as write
targets.**

Extraction: every path-shaped token in `claims.json` (`python3 -c 'json.load(…)'` + regex), and every
`Report:` trailer in `spec.json`:

```
.ufo/waves/round-74/assimilation/id-renumber-map.json      .ufo/waves/round-74/assimilation/validate-receipt.txt
corpus/SOURCES.md                                          corpus/knowledge/culture-material/worldbuilding-setting-practice{,.amend-2026-10-23}.md
corpus/lessons/round-72.md  corpus/lessons/round-73.md  corpus/lessons/round-74.md
reports/round-74/accept-c.py  reports/round-74/accept-ca.py  reports/round-74/ledger.json
reports/round-74/evidence/<id>.txt  reports/round-74/telemetry/{census-start,controls-c,controls-ca,gap-sweep}.txt
tools/check-cited-lines.py  tools/check-receipt-seq.py            (executed, never written)
scripts/sources-census.sh                                          (executed, never written)
.ufo/l0-questions.md                                               (read: the paused freshness rows)
```

- `MANIFEST.json`, `/home/vgpnk/Projects/shokunin/scripts`, `/home/vgpnk/Projects/shokunin/templates`,
  `.ufo/state`, `.ufo/watchdog.log`: **absent as write targets** in claims.json and in all 42 seat
  prompts — a token search over `spec.json` finds `MANIFEST` exactly once, in this sentinel seat's own
  ban list, and `templates` / `.ufo/state` likewise only in that ban list; `scripts` occurs only inside
  the executed, write-free census command.
- All 42 seat `Report:` paths resolve under `.ufo/waves/round-74/w1/`. Every fleet-root, shokuknow or
  sibling-lane path in the 42 prompts is an **input**: the staged package and the register
  (`scout`, `scribe`, `connector`, `reviewer`, `critic`, `renumber`, `mirror` seats), the fleet prompt
  snapshot `/.ufo/prompts/kotodama-round-74.md`, `AXES.md`/`CORPUS.md`/`LEARNING.md`,
  `*-shokunin/PROVINCE.md`, the round-73 fleet report as the ledger's read pin
  (`ExecReceiptRerun73`, `ScoutLedgerSweepB`), `.ufo/state` "ONLY by reading" (`ExecLeftovers`), and
  `git -C /home/vgpnk/Projects/shokunin show` (`ExecLedger`). The only executions of a fleet script are
  the two read-only census invocations (`ExecScratchMirror`, `MutRegistryCollision`).
- The fleet round report the item names — `/home/vgpnk/Projects/shokunin/.ufo/reports/round-74/kotodama.md`
  — does not exist yet; the directory exists and holds other lanes' files
  (`game-dev-2d.md`, `game-dev-3d.md`). Nothing in claims.json or in any seat prompt writes it, so it
  is the integrator's write, not a seat's.
- The declared census command carries **no `--out`**, and `scripts/sources-census.sh` only writes
  when `--out` is given (`emit()` appends to `$OUT`; the only other writes are inside `--selftest`,
  into `mktemp -d` with `trap 'rm -rf' EXIT`). So the declared invocation is read-only against the
  fleet root; if a later seat adds `--out` pointing anywhere under `/home/vgpnk/Projects/shokunin`,
  it becomes a fleet write.

**F3 (medium — trust boundary; pre-landing requirement for a file that does not exist yet).**
`accept-ca.py` is declared as
`python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin`.
The Ca legs read exactly one fleet artefact (the round-73 fleet report at the ledger's `fleet_pin`),
and the counter runs in the graded tree with a fleet-root argument. As written, nothing stops a later
edit from writing through that argument; today the risk is latent because the counter is unwritten.
*Smallest remediation:* the Ca counter must open every fleet-rooted path read-only (`rb`), assert the
resolved realpath is under `<fleet-root>/.ufo/reports/` and refuse otherwise, and its `--selftest`
must carry a control proving a write attempt through `--fleet-root` fails — the existing
junk-landing control family (`config-edited-in-graded-tree`) is the natural place to add it.

Note on the inherited round-73 wave-2 state: claim Ca's TRACKED leg requires those six files to be
byte-equal (sha256 recorded in the ledger) and non-empty at lands. That is the right mitigation for
the R73 "late seat writes" defect: the ledger pins the bytes, so a seat that "tidies" one of them
fails a leg instead of silently changing inherited state. No seat prompt grants a write there.

## 5. Item 4 — canon decision, or a rights/attribution ruling?

**Result: neither. The entries record how real practitioners specify a setting; they decide no
world's canon and make no rights or attribution ruling.** This is the province line the lane draws
for itself at `PROVINCE.md:16-20`.

Evidence in the bytes that will land, not in the staged text:

- Base draft `- scope:` — "it decides no world's canon and rules on no real-world culture or reader".
- Base draft `- refuses:` — "canon for any world; any claim that either practitioner page is measured,
  tested or authoritative; a universal build order; …".
- Base draft §10 closing — "Nothing here rules on any world. No layer assignment, no element count, no
  depth target and no document layout is fixed for a setting by this entry; the practitioner pages
  are reported as conventions, and a builder's own choice is the design decision."
- Amendment `- refuses:` — "any claim that this order is the order other authors use; … roughly
  twenty chapters is a boundary, a threshold or a measured optimum; canon for any world, invented or
  real".
- Amendment §5's worked example is marked "hypothetical and canon-free"; §6 closes "this entry ends at
  that handoff and records no canon."
- Tier framing keeps a commercial page from carrying a claim alone: the two Japanese pages are tier C
  in the drafts, the Russian monograph tier B, and the drafts say so on the `sources:` line.

Attribution is present but is **naming, not ruling**: the amendment binds every span to a speaker
(§1 "Whose words these are", interviewer statements marked as interviewer statements, the author's
own hedge 大概 preserved). No sentence in either draft claims permission, licence, fair use,
public-domain status or AI-training rights for any source. That is the tripwire to watch:
`PROVINCE.md:17-18` refuses "real-world rights/attribution rulings on reference works", so if a
later seat adds a sentence about *whether* quoting these pages is permitted, it is out of province
and must be reported, not absorbed. Nothing of the kind exists today.

## 6. Item 5 — PROVINCE fit: setting specification vs world-bible craft

**Verdict: IN PROVINCE for kotodama, as method evidence with a named handoff — provided the entries
never prescribe the world bible's own structure or canon discipline.** The boundary runs inside §9/§10
and the drafts sit on the correct side of it.

Path:line from this lane's `PROVINCE.md`:

- `PROVINCE.md:3-7` — the domain is "linguistic-cultural worldbuilding … costume & material-culture
  terminology; naming systems — for fictional worlds, **feeding** the world bible". Feeding is the
  relationship, not owning the artefact.
- `PROVINCE.md:9-11` — owns "the generative/coupling craft and its records in this repo
  (`corpus/knowledge/{…culture-material…}`)". Specifying a setting is the generative craft, and
  `culture-material/` is the partition the two entries land in.
- `PROVINCE.md:16-18` — refuses "claiming or recording canon — that is lore-shokunin (kotodama *hands
  off* systems; lore records and verifies them)".
- `PROVINCE.md:22-25` — "lore-shokunin owns the world bible and its consistency verification. The
  handoff format is defined in `corpus/knowledge/synthesis/worldbible-integration-contract.md`.
  Contested scope → report to the integrator, never absorb."

Path:line from `lore-shokunin/PROVINCE.md`:

- `:3` — "Owns: fictional-world records — entities …, relations, timeline events — with consistency
  verification and sourced inspiration." The world bible as a record and its consistency checking:
  lore.
- `:28` — the decisive analogy, because it already settles a neighbouring case: kotodama "owns name
  generation … and calendar/era design …; **lore owns the names and dates recorded on landed
  entities and events**." Design method → kotodama; recorded instance + verification → lore. Applying
  it here: *how a setting is specified* → kotodama; *the world bible that records it, and whether it
  is consistent* → lore.
- `:9` and `:19`/`:23` — lore refuses "claiming canon without an in-world citation" and records CM-g
  "kotodama packet intake" as `uncovered`, i.e. the handoff contract is the lane crossing, and the
  intake side is lore's debt, not kotodama's to absorb.

How the drafts satisfy this: base draft §10 hands off explicitly ("this entry supplies the order, the
layers, the element and note schemas and the single-source discipline; lore decides which of them a
given world adopts, records the canon, and verifies consistency"), couples inward to the lane's own
`verification/` partition rather than restating lore's contradiction ledger, and fixes no layout for a
setting. The amendment's §6 does the same for the derived ladder and the release schedule. Both
entries are in `culture-material/`, the partition `PROVINCE.md:9-11` names.

Residual drift risk (reported, not blocked): §9's "one authoritative document / write the change back
the same day" is the practitioner page's operating rule, and it is *adjacent* to lore's world-bible
bookkeeping. The draft keeps it as the page's rule with the per-series reading marked `(to-verify)` and
ends §9 by handing the verification verdicts to lore — correct. It becomes a province violation only
if a later edit turns those rules into requirements on the world bible (e.g. "the world bible must
carry these five tables", "supersession is recorded thus"). The current sentence — "no document layout
is fixed for a setting by this entry" — is the guard; keep it verbatim through landing.

## 7. Findings, ranked

| id | severity | surface | exploit / failure path | impact | smallest remediation |
|---|---|---|---|---|---|
| F1 | medium | evidence leg, tuduku.space (S882 lane row) | host intermittently returns 200 with a partial body (observed `rc=28` after `200`); sha256 of the fragment lands as "the fetched body's hash" and the Gate quote is inside it | provenance claim not reproducible; counter and EVIDENCE leg both pass on a truncated page | evidence record stores `wc -c` + `</html>` tail assertion; counter compares stored size to declared size; S882 recheck cell notes that a transport error ≠ absence |
| F3 | medium | `accept-ca.py --fleet-root` (unwritten) | a later edit could write through the fleet-root argument into `/home/vgpnk/Projects/shokunin/**` | a lane counter mutating the fleet repo (the R73 late-write class) | open fleet paths `rb`, realpath-contain under `<fleet-root>/.ufo/reports/`, plus a selftest control proving a write through `--fleet-root` fails |
| F2 | low | staged rows S883/S884/S899/S900 `recheck` cells | escaped pipe carries `curl … \| grep -c …` into a registry cell; copying a row as-is imports executable syntax as data | registry cell corruption at minimum; command-execution syntax if any future tool ever runs recheck cells (none does today: no `shell=True` in `tools/`) | none beyond enforcing claim C's existing ROWS leg/kill rule ("cadence-only recheck cell, no pipe in any cell") |
| F4 | low | base draft `source: S877` | the monograph is fetched over **http** (`http://www.philol.msu.ru/…`), so the bytes are not transport-authenticated | a network attacker could substitute the PDF and the entry's four Russian quotes would still read | already mitigated in the draft: the source line records 1,055,723 bytes + sha256 `e512a20d…7ca595a9`, the same hash `ScribeEntryBase` recorded from its own fetch (this seat did not re-fetch the 1 MB PDF); the S877 evidence file must carry the same triple (bytes, sha256, complete-document marker) |
| F5 | info | litmemo evidence / whole-body dumps | the served bodies embed third-party trackers (`G-KE7TTKMWSP`, `G-1K1KGKQS40`, `clarity.ms`, `yimg.jp`) and publisher contact addresses | committing whole bodies would vendor third-party script bytes and contact strings into the lane repo | store quote-local windows, not whole bodies (the claim already says "the body window around the quote"); if a whole body is ever stored, say why in the evidence header |

No critical finding. No credential, token, private URL or tracking parameter exists anywhere in the
round's write surface, and no source is behind a login, paywall, consent, geo or bot wall.

## 8. Not run (and therefore not claimed)

- No acceptance counter was run: `reports/round-74/accept-c.py` and `accept-ca.py` do not exist yet
  (`ls reports/round-74/` → `claims.json`, `telemetry/`). Their behaviour is reviewed from the
  declaration only, which is why F3 is a requirement on the file to be written, not a measured defect.
- No census run, no Gate record, no evidence-file check, no landing, no commit. I issued no `git` or
  `jj` command in this seat at all (not even read-only): the base-revision facts quoted here are the
  claims' own text and my own fetches, which is why every base number in this report is attributed to
  the claim rather than re-derived.
- No `desktop`/dashboard review; no review of the second staged amendment block (staged S895), which
  both the claim rejects map and the amendment draft drop — outside this seat's five items.
- Downloads live in `/tmp/SentinelScope/` only; nothing was fetched into the fleet or lane root.
