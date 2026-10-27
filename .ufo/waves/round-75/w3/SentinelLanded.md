# SentinelLanded — round-75 W3 (hyaku run 10), falsify: safety and scope of the landed bytes

Seat: `SentinelLanded` (leaf; no delegation, no background jobs, no `task`; read-only against the lane,
fleet, shokuknow and every sibling lane; scratch only under
`/fast/scratch/hyaku/kotodama-r75/SentinelLanded/`, deleted after the receipts below were copied here).

Pins used (all resolved in the lane, never in the fleet repo):

| name | revision |
|---|---|
| base | `f556d1049fe651d3d63975600b13acd9fb686f15` |
| freeze | `5d0167464309d8133991b30f7d7a7011a6a0fd14` |
| claim Ca lands | `012e8d3c8b92f47c734f735d58d118d574fe6a14` |
| claim C lands (graded diff range end) | `4f5e3b2535c2c06c51627dc2736c40183847cae1` |
| lane main at dispatch | `82ced5c` (`82ced5c round-75: measurements at the landings ...`) — telemetry/report-side only |

The graded range is `git diff f556d10 4f5e3b2` (295 files, +63011/−19). `82ced5c` was audited
separately (it changes no `claims.json`, `ledger.json`, `corpus/`, `SHONEN.md`, `SKILL.md` or
`reports/round-75/evidence/` file; `git diff f556d10 4f5e3b2 --name-only` ∩ those paths for the
`4f5e3b2..82ced5c` diff is empty).

Harness: `D=$(mktemp -d -p /fast/scratch/hyaku/kotodama-r75/SentinelLanded)`;
`git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"`;
`git -C "$D/lane" rev-parse --show-toplevel` →
`/fast/scratch/hyaku/kotodama-r75/SentinelLanded/work/lane` (asserted equal before every mutation and
before both counter runs). Every git call named `-C`. No fixture commit was needed.

---

## 1. Verdict per assigned check

| # | check | verdict |
|---|---|---|
| 1 | credential material, `op://`, tokens, private URLs, tracking query strings in entries/rows/evidence/receipts | **PASS** (no credential, `op://`, userinfo, private host or tracking parameter; D1 is session state, not a credential — see check 7) |
| 2 | every source URL a public ordinary-means page; no bot challenge passed | **PASS** |
| 3 | no write outside the lane (landed bytes and landed tooling) | **PASS** for the landing; the Ca counter's default scratch escapes to `/tmp` (D2, graded under check 5) |
| 4 | no file over 1 MiB introduced | **PASS** |
| 5 | the counters write only under scratch roots | **FAIL** — `accept-c.py` PASS (refuses `/tmp`); `accept-ca.py` FAIL (defaults to the system temp dir; a W3 peer run left clones in `/tmp`) → **D2** |
| 6 | no seat-authored line deletes a protected line | **PASS** (`0`) |
| 7 | the evidence files carry no cookies/session headers | **FAIL** for the landed probe receipts (18 `Set-Cookie` lines with live values in 7 committed files); **PASS** for the graded `reports/round-75/evidence/*.txt` → **D1** |

Overall: **PARTIAL** — the substantive landing is clean on credentials, tracking, private hosts,
oversize files and protected-line preservation, and both counters reproduce PASS *when invoked
correctly*; but one committed artifact class leaks server session state while a landed report states
the opposite, one counter's default scratch escapes the operator roots, and claim Ca's own declared
after-state command does not print PASS.

---

## 2. Check 1 — credential material / `op://` / tokens / private URLs / tracking

```
$ git diff f556d10 4f5e3b2 > landed.diff   # 64917 lines
$ grep -nE 'op://|bw://|vault://|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|github_pat_|xox[abpr]-|-----BEGIN [A-Z ]*PRIVATE KEY|Bearer [A-Za-z0-9._-]{16,}' landed.diff
16113:+add("SentinelScope", "sentinel", f"Scope and safety review ... op:// refs, session tokens, tracking query strings ...
28596:+password|passwd|secret|api[_-]?key|apikey|bearer|authorization|op://|AKIA|ghp_|xox[bap]-|
28700:+| S-75-11 | INFO | no secrets, no private hosts, no op:// refs, no userinfo URLs, ...
28714:+grep -Ein 'password|passwd|secret|api[_-]?key|bearer|authorization|op://|AKIA|ghp_|BEGIN [A-Z ]*PRIVATE KEY|session[_-]?id|auth=|cookie|/tmp/|/home/|docAsPDF' \
29430:+        "task": "/skill:godspeed\n\nYou are a Godspeed-enabled subagent. ... credential material, private URLs, op:// refs ...
29655:+   "prompt": ...
30187:+   "output": ...
```

Every hit is the round's own **grep-pattern text or seat prompt** (`.ufo/waves/round-75/w1/SentinelScope.md`,
`w1/spec.json`, `w1/dispatch.json`, `w2/w2-results.json`, `counters/`). No live `op://` reference, no
private-key block, no bearer token, no `ghp_`/`xox` token exists in the landed bytes.

```
$ grep -nE '^\+.*(localhost|127\.0\.0\.1|192\.168\.|10\.[0-9]+\.[0-9]+\.[0-9]+|\.internal|\.local[:/]|file://|ftp://|ssh://)' landed.diff | wc -l
   -> hits only inside selftest harness code (ThreadingHTTPServer(("127.0.0.1",0)), file:// fixtures)
      and fixture hostnames; zero in any corpus row, evidence window or receipt URL.

$ grep -oE 'https?://[^/ )"`]*@[^/ )"`]*' landed.diff | sort -u | head
   (empty)                                   # no userinfo URLs

$ grep -nE '^\+.*[?&](utm_[a-z]+|fbclid|gclid|gclsrc|dclid|msclkid|mc_cid|mc_eid|ref=|sessionid|sid|token|access_key|sig)=' landed.diff
   (empty)

$ grep -rlE 'utm_(source|medium|campaign)|fbclid|gclid|mc_eid|mc_cid' corpus reports/round-75 .ufo/waves/round-75
.ufo/waves/round-75/w1/SentinelScope.md      # the literal pattern names in its own grep row, no values
```

The only query strings anywhere in the range are (a) `web.archive.org/cdx/search/cdx?...` discovery
calls (`output=`, `filter=`, `fl=`, `limit=`, `collapse=`, `matchType=` — functional, not tracking),
(b) Persée's functional `?pageId=T1_2`, (c) `ndlsearch.ndl.go.jp/api/opensearch?...` in a staged file
listing, and (d) `challenge-detail` / CSP text inside the probe headers. None is a tracking parameter.

Fixture hostnames `example.invalid`, `example.org`, `evil.example`, `x.example`,
`www.example.com:80` are RFC 2606/6761 reserved names in selftest code.

**Verdict: PASS.**

---

## 3. Check 2 — every source URL is a public ordinary-means page

Nine admitted rows; each has a committed evidence file. Fetch records (verbatim fields):

```
$ for f in reports/round-75/evidence/S88?.txt reports/round-75/evidence/S89?.txt; do grep -E '^(url|http|challenge|final-url|fetch-attempts):' "$f"; done
S885  url: https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113                http: 200  challenge: none  fetch-attempts: 1
S886  url: https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120                http: 200  challenge: none  fetch-attempts: 1
S887  url: https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114                http: 200  challenge: none  fetch-attempts: 1
S888  url: https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf                        http: 200  challenge: none  fetch-attempts: 1
S889  url: https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf                http: 200  challenge: none  fetch-attempts: 1
S890  url: https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf           http: 200  challenge: none  fetch-attempts: 1
S891  url: https://web.archive.org/web/20041220223357id_/http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html
                                                                                     http: 200  challenge: none  fetch-attempts: 1
S892  url: https://web.archive.org/web/20251111222249id_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf
                                                                                     http: 200  challenge: none  fetch-attempts: 1
S893  url: https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html           http: 200  challenge: none  fetch-attempts: 1
```

Nine distinct public surfaces: Persée open notices (3), a Chinese university course-syllabus PDF, two
J-STAGE open PDFs, one University of Geneva excerpt served as an Internet Archive capture, one
University of Palermo repository PDF served as a same-page Internet Archive capture (`id_/` + the exact
live URL — QUALITY 18 same-page binding, not a proxy of a different page), one `chinawriter.com.cn`
article. No login form, no consent wall, no geo gate, no `?token=`-style access grant in any of them.

**The one access control met was not passed.** `.ufo/waves/round-75/counters/probe-receipts/head8.txt`
is the live `iris.unipa.it` result and is `HTTP/2 403` + `cf-mitigated: challenge` (a Cloudflare
interstitial). The round did not attempt the challenge; the S892 row was read from the archived capture,
and the landed entry states this explicitly:

```
corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md:126:
  ... The article-level PDF endpoint of the serving archive answers a plain request with an altcha
  challenge: it was met and not passed, no attempt was made to pass it, and no sentence in this file
  rests on a PDF or on the walled surface.
```

`head4..8.txt` also record the `Content-Security-Policy: ... challenges.cloudflare.com` and CSP nonce
of that 403, i.e. the wall is documented rather than bypassed. The Persée PDF endpoint
(`docAsPDF`) is recorded as a met-but-not-passed altcha too; the entries cite only the public per-page
transcription, and no landed sentence calls that transcription access-controlled (C's `kill_rule`
branch). Fetch records bind one UA to one response: every evidence file carries exactly one
`ua:`/`user-agent:` pair and exactly one `http:`/`http-status:` line for the same `fetch:` URL — none
mixes two agents.

**Verdict: PASS.**

---

## 4. Check 3 — no write outside the lane

```
$ git diff --name-only f556d10 4f5e3b2 | grep -vc '^\(corpus\|reports\|\.ufo\|tools\|SHONEN.md\|SKILL.md\|LOG.md\|SCORECARD.md\|MANIFEST.json\)'
0
```

Every changed path is inside the lane. The landed tooling writes only to the root it is handed:

* `.ufo/waves/round-75/apply-landing.py` — `wr()`/`cp()` write under `argv[1]` (`<root>`), source
  `.ufo/waves/round-75/w2/stage` read-only;
* `.ufo/waves/round-75/assimilation/build-map.py` — writes under `A` (the lane's own
  `assimilation/` dir) and copies into `A/guard-proof/out`;
* `.ufo/waves/round-75/build-w{1,2,3}.py`, `build-claims-final*.py`, `build-rows.py` — write under
  `LANE` or `W` (lane paths);
* the counters' own write helpers (`accept-c.py:_sfx_write`, `accept-ca.py:_write`) take `root` from
  the caller, and every caller passes a clone/fixture directory under the scratch root.

```
$ grep -rnE 'git -C /home/vgpnk/Projects/shokunin +(add|commit|checkout|reset|rm|clean|merge)' --include='*.py' --include='*.sh' .ufo/waves/round-75 reports/round-75
   (empty)
$ grep -rn '\.local/bin\|/usr/local' --include='*.py' --include='*.sh' .ufo/waves/round-75 reports/round-75
.ufo/waves/round-75/counters/accept-ca.py:1164/2180/2219: "PATH": os.environ.get("PATH", "/usr/local/bin:/usr/bin:/bin")   # env passthrough only
.ufo/waves/round-75/counters/accept-ca.py:1165: "HOME": os.environ.get("HOME", "/tmp")                                        # subprocess env only
.ufo/waves/round-75/build-*.py:16/28/21: the fleet-root sentence inside the seat context string        # text, not a write
```

The fleet `scripts/sources-census.sh` is invoked three ways in the receipt text
(`validate --file <registry>`), i.e. read-only; no landed script mutates the fleet repo, a sibling
lane, `MANIFEST.json`, `templates/`, `.ufo/state`, `.ufo/watchdog.log` or shokuknow. `82ced5c`
carries the same profile.

**Verdict: PASS for the landing.** (The counter's *default* scratch directory is a separate defect —
check 5 / D2.)

---

## 5. Check 4 — no file over 1 MiB

```
$ git diff --diff-filter=A --name-only f556d10 4f5e3b2 | while read f; do printf '%s %s\n' "$(git cat-file -s 4f5e3b2:$f)" "$f"; done | sort -rn | head -8
282910 reports/round-75/accept-c.py
166430 reports/round-75/accept-ca.py
166430 .ufo/waves/round-75/counters/accept-ca.py
166264 .ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py
146483 .ufo/waves/round-75/w2/w2-results.json
140464 .ufo/waves/round-75/w1/w1-results.json
126734 .ufo/waves/round-75/w2/dispatch.json
115182 .ufo/waves/round-75/w2/spec.json

$ git ls-tree -r -l 4f5e3b2 | awk '$4>1048576 {print $4, $5}'
1597667 reports/round-60/captures/pages/S637.txt
$ git ls-tree -l f556d10 reports/round-60/captures/pages/S637.txt
100644 blob 8e4bac1c94afa17c6adab7dd9e8655f037e48697 1597667 reports/round-60/captures/pages/S637.txt
```

The only file above 1 MiB at the lands revision is byte-identical at base (same blob, same size) —
not introduced by this round. Largest **added** file is 282 910 B; largest **modified** is
`corpus/SOURCES.md` at 977 373 B (977 373 < 1 048 576).

**Verdict: PASS.**

---

## 6. Check 5 — the counters write only under scratch roots

### `accept-c.py` — PASS

```
$ sed -n '6007,6029p' reports/round-75/accept-c.py
def _scratch_root(args):
    """M4: the scratch root for every clone, materialization and temp dir.
    `--work` wins; then `$HYAKU_SCRATCH/kotodama-r75/counter`; then the
    operator's scratch tree.  Never the system temporary directory."""
    ...
    return "/fast/scratch/hyaku/kotodama-r75/counter"

def _forbidden_scratch(path):
    p = os.path.abspath(path)
    banned = {os.path.abspath("/tmp"), os.path.abspath(tempfile.gettempdir())}
    for b in banned:
        if p == b or p.startswith(b + os.sep):
            return True
    return False
```

Resolution order is `--work` → `$HYAKU_SCRATCH/kotodama-r75/counter` → `/fast/scratch/hyaku/kotodama-r75/counter`,
and `main()` refuses to grade when the resolved root is `/tmp` (`REFUSED: scratch root … is the system
temporary directory`). Verified by the run below (clone path printed under the seat's own `--work`).

### `accept-ca.py` — FAIL (D2)

```
$ sed -n '266,280p' reports/round-75/accept-ca.py
def scratch_dir(explicit=None):
    """The one scratch root: --work, else $HYAKU_SCRATCH/kotodama-r75, else the
    system tempdir.  Never a hardcoded /tmp."""
    root = explicit
    if not root:
        base = os.environ.get("HYAKU_SCRATCH")
        root = os.path.join(base, "kotodama-r75") if base else None
    if not root:
        root = tempfile.gettempdir()
    root = os.path.abspath(root)
    os.makedirs(root, exist_ok=True)
    return root
```

There is no `/fast/scratch` fallback and no `/tmp` refusal:

```
$ env -u HYAKU_SCRATCH -u TMPDIR python3 -c "<load accept-ca.py, call scratch_dir()>"
scratch_dir(None) = /tmp
```

The claims' own Ca invocation carries neither `--work` nor `HYAKU_SCRATCH`
(`claims.json`, claim Ca `counter`/`after`: `... --root . --lands <Ca-lands> --freeze <freeze> --fleet-root
/home/vgpnk/Projects/shokunin`), so the documented command materializes `lands/`, `base/`, `r1-green/`,
`r1-red/`, `r1-mixed/`, `r74lands/`, `sweep-base/` clones under `/tmp`. That is not a theory — a peer
W3 run of exactly that command left the tree behind:

```
$ ls -la /tmp/r75-ca-lgjau102
drwx------ 10 vgpnk vgpnk 130 Oct 27 17:53 .
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 base
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 lands
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 r1-green
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 r1-mixed
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 r1-red
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 r74lands
drwxr-xr-x 9 vgpnk vgpnk 4096 Oct 27 17:53 sweep-base
```

I did not create this directory (my two runs passed `--work`), and I did not touch it: it belongs to
another seat. It is also uncitable evidence by the operator rule ("a `/tmp` path is never citable
evidence") — which is exactly the property the operator scratch rule exists to guarantee, and which the
committed `measures-ca.txt` only avoids because its executor set the environment
(`# clone: /fast/scratch/hyaku/kotodama-r75/r75-ca-y1jf_l7c/lands`).

Impact: disk growth outside the sanctioned root, per-run clones of the whole lane in a world-traversable
directory (mode 0700 as created, so not cross-user readable), and receivers following the documented
command leaving `/tmp` residue; no data exposure beyond the (already public) lane history, and no
security boundary crossed.

**Verdict: accept-c PASS; accept-ca FAIL.**

---

## 7. Check 6 — no seat-authored line deletes a protected line

```
$ git diff f556d1049fe651d3d63975600b13acd9fb686f15 4f5e3b2535c2c06c51627dc2736c40183847cae1 -- LOG.md SCORECARD.md corpus/lessons | grep '^-[^-]' | wc -l
0

$ git diff --numstat f556d10 4f5e3b2 -- LOG.md SCORECARD.md corpus/lessons
33      0       SCORECARD.md
403     0       corpus/lessons/round-75.md
```

`LOG.md` is untouched in the range; `SCORECARD.md` only gains 33 lines (`## Corrections — round 75`);
`corpus/lessons` only gains the new `round-75.md`. The same check against the later report-side commit:

```
$ git diff f556d10 82ced5c -- LOG.md SCORECARD.md corpus/lessons SHONEN.md SKILL.md corpus/QUALITY.md corpus/README.md | grep '^-[^-]'
   (empty)
```

The two non-append-only protected files are the Ca-declared repairs, and their removed lines are exactly
the stated_at lines the frozen ledger names:

```
$ git diff f556d10 4f5e3b2 -- SHONEN.md SKILL.md | grep -E '^[-+][^-+]' | cut -c1-200
-  asserted: ... sources registered in `corpus/SOURCES.md` (412 rows after round 56 — 367 mined, 35 queued, 10 rejected — ...
+  asserted: ... sources registered in `corpus/SOURCES.md` (Registry counts at round 75 Ca landing — rows: 808, mined: 713, q...
-| accept-c-72 | gate | ... the denominator is a lit...
+| accept-c-72 | gate | ... the denominator is a lit...
+| accept-c-75 | gate | ...
+| accept-ca-75 | gate | ...
```

`SHONEN.md:6` is ledger pair L75-01 (`412` → `808`), `SKILL.md:701` is in the Ca `fixed_surfaces`
list, and the `accept-c-72` line is re-emitted because a row is appended after it (no protected token
changes). The APPENDONLY leg (run below) independently reports `protected=[...] problems=[]` and
`rule2-edits=0` at the graded tree.

**Verdict: PASS.**

---

## 8. Check 7 — the evidence files carry no cookies/session headers

The **graded** evidence set is clean:

```
$ grep -cEi 'set-cookie|cookie:|jsessionid|__cf_bm|authorization|bearer' reports/round-75/evidence/*.txt
S885.txt:0  S886.txt:0  S887.txt:0  S888.txt:0  S889.txt:0  S890.txt:0  S891.txt:0  S892.txt:0  S893.txt:0
```

Their `fetch-command` is a stateless `curl -sS -L --compressed ... -A "<UA>" -o BODY -D HEADERS` with no
cookie jar and no `Cookie:` request header, so no request-side session state is recorded either.

The **landed probe receipts**, however, are not clean. `.ufo/waves/round-75/counters/probe-receipts/`
`MANIFEST.txt` says *"head\*.txt are the raw curl response headers of the same requests"*, and those raw
headers were committed verbatim in the C landing (`4f5e3b2`, 18 added `Set-Cookie` lines):

```
$ grep -ciE '^set-cookie' .ufo/waves/round-75/counters/probe-receipts/head*.txt
head1.txt:3   head2.txt:3   head3.txt:3   head4.txt:0
head5.txt:3   head6.txt:3   head7.txt:2   head8.txt:1        # 18 lines, 7 files

$ grep -nEi '^set-cookie' .ufo/waves/round-75/counters/probe-receipts/head*.txt
head1.txt:9:Set-Cookie: JSESSIONID=D7FF…<value redacted in this report>; Path=/; Secure; HttpOnly
head1.txt:10:Set-Cookie: COOKIE_SUPPORT=true; Max-Age=1471228928; ...; HttpOnly
head1.txt:11:Set-Cookie: GUEST_LANGUAGE_ID=fr_FR; Max-Age=1471228928; ...; HttpOnly
head2.txt:9:Set-Cookie: JSESSIONID=31EB…<value redacted in this report>; ...
head3.txt:9:Set-Cookie: JSESSIONID=451D…<value redacted in this report>; ...
head5.txt:8:Set-Cookie: jsessionid_if=B5AD…<value redacted in this report>; Path=/; Secure; HttpOnly
head5.txt:9:Set-Cookie: BIGipServerPOOL_TSC119_006=2380…<value redacted in this report>; expires=Tue, 27-Oct-2026 19:02:47 GMT
head5.txt:16:Set-Cookie: TS01e91e28=0192…<value redacted in this report>
head6.txt:8:Set-Cookie: jsessionid_if=A549…<value redacted in this report>; ...
head6.txt:16:Set-Cookie: TS01e91e28=0192d1…<value redacted in this report>...
head7.txt:2:Set-Cookie: TSc4f20db1029=0881…<value redacted in this report>...
head7.txt:9:Set-Cookie: TS98a5990b027=0881…<value redacted in this report>
head8.txt:18:set-cookie: __cf_bm=BDFp…<value redacted in this report>; ... Domain=iris.unipa.it
```

Nine distinct cookie names, each with a live value in the committed bytes (`JSESSIONID` ×3,
`COOKIE_SUPPORT` ×3, `GUEST_LANGUAGE_ID` ×3, `jsessionid_if` ×2, `BIGipServerPOOL_TSC119_006` ×2,
F5 ASM `TS01e91e28` ×2, `TSc4f20db1029`, `TS98a5990b027`, Cloudflare `__cf_bm`). Only the first four
characters of each value are quoted above: this report redacts the rest rather than re-publishing the
leak it reports. `head8.txt` also carries `cf-ray` and a CSP `nonce-…` for the challenge page.

This is the exact hygiene class a landed seat report says did not happen:

```
.ufo/waves/round-75/w1/SentinelScope.md:37:
  - Probes did receive server-set cookies from `persee.fr` (`JSESSIONID`, `COOKIE_SUPPORT`,
    `GUEST_LANGUAGE_ID`) and one Cloudflare cookie from `iris.unipa.it`. They are server-issued session
    state, not credentials; **I persisted no cookie value into any lane file**, and no seat report
    carries one. ... do not paste response headers into a committed evidence file.
```

The bytes falsify that sentence: the values are in `counters/probe-receipts/head{1,2,3,5,6,7,8}.txt`, in
the same wave's tree. Cookie *values* appear nowhere else:

```
$ grep -rlE 'JSESSIONID=[A-F0-9]{20}|TS01e91e28=[0-9a-f]{40}|__cf_bm=[A-Za-z0-9_.-]{20}|BIGipServerPOOL_TSC119_006=[0-9]{6}|TSc4f20db1029=[0-9a-f]{20}|TS98a5990b027=[0-9a-f]{20}|jsessionid_if=[A-F0-9]{20}' .
./.ufo/waves/round-75/counters/probe-receipts/head1.txt
./.ufo/waves/round-75/counters/probe-receipts/head2.txt
./.ufo/waves/round-75/counters/probe-receipts/head3.txt
./.ufo/waves/round-75/counters/probe-receipts/head5.txt
./.ufo/waves/round-75/counters/probe-receipts/head6.txt
./.ufo/waves/round-75/counters/probe-receipts/head7.txt
./.ufo/waves/round-75/counters/probe-receipts/head8.txt
```

(head4.txt is a `Set-Cookie`-free response; these seven are the whole set, and this report's own
redacted prefixes do not match the pattern.)

Earlier rounds' Sentinel reports name the cookie headers but paste no values
(`grep -rlE 'JSESSIONID=[A-F0-9]{20}|__cf_bm=[A-Za-z0-9]' .ufo/waves/round-64 .ufo/waves/round-71
.ufo/waves/round-73` → empty), so this is a round-75 regression of a rule those reports state.

**Verdict: FAIL** for the landed receipt set (graded evidence files: PASS).

---

## 9. Counter reproduction (both counters, run inside the seat's scratch clone only)

Pinned clone:

```
$ git -C "$D/lane" rev-parse --show-toplevel
/fast/scratch/hyaku/kotodama-r75/SentinelLanded/work/lane
$ git -C "$D/lane" checkout -q -B main 4f5e3b2535c2c06c51627dc2736c40183847cae1
```

**Claim C — PASS unaffected.** `--work "$S/scratch-c"`, 2.2 s:

```
LEG PASS ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / GROUND
LEG PASS CITEDLINES   files=3 last-line=CITED-LINES: 0 finding(s) in 3 file(s)
LEG PASS CENSUS       exit=0 file ok .../scratch-c/r75-lands-lqp1olze/clone/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR receipt@0 append@2 rows=9 entries=3
LEG PASS COLLCHECK    ids=808 staged=132 collisions=26 guard=ok/ok map=12
LEG PASS FROZENCFG    freeze 5d0167464309 ... claims@lands=frozen-bytes map=...(sha256-match)
LEG PASS INDEX        myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s)
ACCEPT-C-75: PASS legs=13/13
```

**Claim Ca — PASS only with an undocumented flag; the declared command FAILS (D3).**

```
$ git -C "$D/lane" checkout -q -B main 012e8d3c8b92f47c734f735d58d118d574fe6a14
$ python3 -B reports/round-75/accept-ca.py --root . --lands 012e8d3c8b92f47c734f735d58d118d574fe6a14 \
      --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 \
      --fleet-root /home/vgpnk/Projects/shokunin --work "$S/scratch-ca"      # the claims' documented command
...
LEG PASS LEDGER (pairs=10) / BASEMISMATCH (red=10) / REPAIR (green 6, red []) / ANNOTATE (rows=25)
LEG PASS NOSTUB / APPENDONLY (rule2-edits=0 problems=[]) / R1EXEMPT (green=True red=False mixed=False)
LEG PASS SEPARABLE (problems=[]) / RECEIPTS (rev=5e4796c0cb6a) / FROZENCFG / STAMP (012e8d3c)
LEG FAIL COMBINED
     the explicit --combined revision is required
ACCEPT-CA-75: FAIL legs=11/12
exit=1
```

Adding the flag the frozen COMBINED leg text names:

```
$ python3 -B reports/round-75/accept-ca.py ... --combined 4f5e3b2535c2c06c51627dc2736c40183847cae1 --work "$S/scratch-ca"
LEG PASS COMBINED   ca-lands=012e8d3c8b92 combined=4f5e3b2535c2 tree=43a96e737f25 problems=[]
LEG PASS STAMP      stamped=evaluated=measured=012e8d3c8b92 tree=c943f86b4cb2 counter=98d8e7974c82
ACCEPT-CA-75: PASS legs=12/12
exit=0
```

So the claim's substance verifies; its **declared invocation** does not. Both runs left
`git -C "$D/lane" status --porcelain` empty and wrote nothing outside `$S/scratch-c{,a}` (the counters
remove their `tmp_root` on exit; `du -sh` on both scratch dirs afterwards = 0).

---

## 10. Defect list (severity, exploit path, evidence, impact, smallest remediation)

### D1 — Server session cookies committed with receipt bytes; a landed report states the opposite
**Severity: MEDIUM** (policy/hygiene; exploit value ~0 today; permanent until history is filtered).

* **Exploit path.** `.ufo/waves/round-75/counters/probe-receipts/head1..3,5..8.txt` (18 lines) publish
  anonymous Persée `JSESSIONID` values, F5 ASM tokens (`TS01e91e28`, `TSc4f20db1029`,
  `TS98a5990b027`), an `jsessionid_if` value and a Cloudflare `__cf_bm` value. Anyone with repo read
  access can replay them; all are expired or IP/UA-bound, so the practical replay surface is nil. The
  durable harm is that a repo whose receipts are treated as public evidence now carries server-issued
  session state in its history, in the same tree whose own sentinel report (`w1/SentinelScope.md:37`)
  asserts no cookie value was persisted — the report's readiness statement is false as compiled.
* **Evidence.** §8 above; `MANIFEST.txt` ("head\*.txt are the raw curl response headers"), C landing
  commit `4f5e3b2`, `git diff f556d10 4f5e3b2 | grep -c '^+[Ss]et-[Cc]ookie'` → `18`.
* **Impact.** No credential or personal datum leaks; receipt integrity and report truthfulness do.
* **Smallest remediation.** `git rm` the eight `head*.txt` files — nothing in either counter reads them
  (the graded window comes from `reports/round-75/evidence/`), they are cited only by `MANIFEST.txt`'s
  own description — and correct the two sentences that claim otherwise (`MANIFEST.txt` last comment,
  `SentinelScope.md:37`). If a header record must be kept, keep header **names**/status only and redact
  every `Set-Cookie` value; the S885–S893 status/bytes/UA facts that matter are already in the `.txt`
  probe receipts and the evidence files.

### D2 — `accept-ca.py` defaults its scratch root to the system temp dir
**Severity: MEDIUM** (scope rule; disk growth; uncitable receipts).

* **Exploit path.** `python3 -B reports/round-75/accept-ca.py --root . --lands <Ca> --freeze <freeze>
  --fleet-root <fleet>` — the exact string in claim Ca's `counter`/`after` — resolves `scratch_dir(None)`
  to `tempfile.gettempdir()` and materializes seven full clone trees there. A peer run already left
  `/tmp/r75-ca-lgjau102` behind (`lands base r1-green r1-mixed r1-red r74lands sweep-base`).
  `accept-c.py` in the same round refuses exactly this (`_forbidden_scratch` → `REFUSED: scratch root …
  is the system temporary directory`), so the two counters disagree on the operator rule.
* **Impact.** Writes outside the sanctioned scratch roots; a path that may never be cited as evidence
  becomes the default receipt location; clones accumulate across runs and can collide across seats.
* **Smallest remediation.** Give `accept-ca.py` the same three-step resolution as `accept-c.py`
  (`--work` → `$HYAKU_SCRATCH/kotodama-r75` → `/fast/scratch/hyaku/kotodama-r75`) plus the
  `_forbidden_scratch` refusal, and add `--work`/`HYAKU_SCRATCH` to the documented invocation in
  `claims.json`'s Ca `counter`/`after` and `SKILL.md:708`. Fourteen lines in one function.

### D3 — Claim Ca's declared after-state command prints FAIL at the landed tree
**Severity: MEDIUM** (reproducibility).

* **Exploit path.** A W3/W4 reviewer (or the next round) runs the command the claim declares — without
  `--combined` — and gets `ACCEPT-CA-75: FAIL legs=11/12`, `exit=1`, because the COMBINED leg *requires*
  `--combined`. Reproduced in the scratch clone (§9). The claim's `after` states this command "prints
  ACCEPT-CA-75: PASS legs=12/12 (exit 0)". The claim's own COMBINED leg text and `SKILL.md:708` both
  name `--combined`, so the `after`/`counter` fields are the wrong artifact.
* **Impact.** A landed claim that a grader follows yields a false red, and the counter's exit contract
  (`0` PASS / `1` FAIL / `2` refused) is violated by the claim's own documentation. The underlying legs
  are green: `PASS legs=12/12` with `--combined 4f5e3b2`.
* **Smallest remediation.** Amend claim Ca's `after` and `counter` to
  `... --combined <the tree carrying both landings>` (the string already in `measures-ca.txt`), or make
  the COMBINED leg resolve `--combined` from the frozen claims when the argument is omitted. The
  documented string and the committed receipt must be the same command.

### D4 — The COMBINED leg names a receipt that does not exist
**Severity: LOW–MEDIUM** (evidence-pointer).

* **Exploit path.** The frozen COMBINED leg says *"Receipt `measures-ca-combined.txt` carries the
  Ca-lands stamp and exact combined revision/tree"*. No such path exists:
  `git ls-tree -r --name-only 4f5e3b2 | grep -c measures-ca-combined` → `0`; the committed receipt is
  `reports/round-75/telemetry/measures-ca.txt` (which does carry `combined=4f5e3b25…` and the stamp).
* **Impact.** The leg's own named artifact cannot be opened by a reviewer; a missing named receipt is
  indistinguishable from a suppressed one until the rename is noticed. No leg is actually unbacked.
* **Smallest remediation.** Rename `measures-ca.txt` → `measures-ca-combined.txt` (it is that run), or
  correct the leg text to the path that exists. One-line commit either way.

### D5 — INFO: the observed-observation set for S885 is one short
**Severity: INFO** (already disclosed; no claim impact).

* `corpus/lessons/round-75.md:57-63` records "three stored observations" of S885 (111487 / 111486 /
  109589 bytes) and states the drift is "recorded, not repaired"; the graded evidence
  `reports/round-75/evidence/S885.txt` is a **fourth** observation (109588 B, `20b571d7…`, fetched
  `19:48:02Z`) and the entry's `verified-at` (line 8) quotes the w1 figure 111487 as its own observed
  byte count. All four are self-bound (`window-sha256:` per file), and the lesson names no byte count as
  canonical, so nothing is fabricated — but the note's count is stale and the entry's number is not the
  graded window's number.
* **Smallest remediation.** Extend the note to four observations (or cite the graded file), and make the
  entry's `verified-at` say which observation it quotes or drop the exact byte count for the
  non-byte-stable Persée notice.

---

## 11. Not defects, checked and cleared

* `staged S870` quote refused, source re-opened as S893 (REJECTS leg PASS; lesson §Quarantine present).
* Appended rows carry no pipe in any cell, one row per document, contiguous S885–S893, status `mined`,
  opened `2026-10-27` — ROWS/REPOINTED/COLLCHECK green.
* All nine evidence windows recompute their own `window-sha256:`; `window-scope: whole-document` only
  where `visible-chars` < 4096 (S885 3720, S886 3526, S887 3073, S891 2169) — EVIDENCE leg green.
* No credential, `op://` reference, private host, userinfo URL, tracking parameter, request-side
  `Cookie:` header, or `Authorization` header exists in any corpus file, evidence window or receipt.
* No landed script mutates the fleet repo, a sibling lane, `MANIFEST.json`, `templates/`,
  `.ufo/state`/`.ufo/watchdog.log`, or shokuknow.
* `82ced5c` (lane main past the C landing) touches only `.ufo/waves/round-75/**` and
  `reports/round-75/telemetry/**`: no `claims.json`, `ledger.json`, `corpus/`, `SHONEN.md`, `SKILL.md`
  or evidence file changes, and zero protected-line deletions.

## 12. Seat hygiene

* Read-only against the lane (only this report written), the fleet, shokuknow and every sibling lane;
  no `jj`, no git index/state mutation, no sibling-lane contact (no messages sent).
* The lane working tree carried two **foreign** uncommitted edits at the time of this report —
  `LOG.md` (+10 lines) and `corpus/lessons/round-75.md` (+32 lines), mtimes `17:50:44`/`17:50:26` — both
  pure insertions, both older than this report (`17:56:40`). They are a sibling W3 seat's work, they are
  present in no revision I graded (every check above reads commits, never the worktree), and I did not
  touch them.
* Both counter runs used `--work /fast/scratch/hyaku/kotodama-r75/SentinelLanded/scratch-{c,ca}`; after
  them the clone's `git status --porcelain` was empty and nothing existed under `/tmp` from this seat.
* No tool installed, upgraded or removed (no `pacman`, no `uv`, no `npm`); nothing added to `PATH`.
* Scratch `/fast/scratch/hyaku/kotodama-r75/SentinelLanded/` (the `work/lane` clone, `landed.diff`, both
  counter dirs) deleted after these receipts were copied here. The foreign `/tmp/r75-ca-lgjau102` was
  read only and left untouched (D2 evidence).
