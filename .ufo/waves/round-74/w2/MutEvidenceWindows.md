# MutEvidenceWindows — round 74 WAVE 2 (kotodama, hyaku run 7) — evidence-window mutation probes

Seat: LEAF, no delegation. Attack targets: `reports/round-74/evidence/{S877,S881,S882,S883,S884}.txt` and
`.ufo/waves/round-74/counters/capture-evidence.py`, via the frozen claim-C EVIDENCE leg
(`git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/claims.json`, leg `EVIDENCE`)
implemented by `reports/round-74/accept-c.py` (counter sha256 8d30487fa4692261…, byte-identical at freeze,
5e4796c0, c4bf61a8 and dispatch main).

## Environment and baselines (pristine detector runs)

Clone hygiene per dispatch: `D=$(mktemp -d) && git -C "$D" init -q && git -C "$D" rev-parse --show-toplevel`
printed `$D` (`/tmp/MutEvidenceWindows`); probes ran in `/tmp/MutEvidenceWindows/laneC`, a fresh clone of the
lane, with `git branch -f main c4bf61a8d722f9168ce0fd8021a6261c000610c5` (claim C lands) and a `mut` branch for
probe commits. The fleet repo was never written; all mutation commits live only in the /tmp clone.

- Baseline, pristine bytes at lands c4bf61a8:
  `python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin`
  → `ACCEPT-C-74: PASS legs=13/13` (exit 0).
- Baseline at Ca's own landing 5e4796c0 (its `main` pinned there first):
  `python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin`
  → `ACCEPT-CA-74: PASS legs=11/11` (exit 0), all 11 legs PASS.

N1 (environment note, not a defect): the same accept-ca run pointed at the **C** landing c4bf61a8 fails
`ACCEPT-CA-74: FAIL legs=9/11` — `LEG FAIL APPENDONLY … problems=['corpus/SOURCES.md: changed lines outside
REPAIR stated_at lines [832]']` (claim C's landing legitimately rewrites the S877 row in place, which is not a
Ca REPAIR stated_at line) and `LEG FAIL RECEIPTS … accept-ca-73 re-run exit=1 (want 0) …`. The two counters
grade different lands by design (Ca lands before the registry append; 5e4796c0 is an ancestor of c4bf61a8);
each passes at its own landing.

## Detector summary

| probe | mutation (file / field) | accept-c verdict | capture-evidence --verify |
|---|---|---|---|
| baseline | none (lands c4bf61a8) | PASS 13/13 | — |
| a | S881 window char 触→觸, nothing recomputed | **KILLED** (EVIDENCE) | VERIFY FAIL |
| b | same mutation + `window-sha256` recomputed | survives offline (disclosed residual) | VERIFY OK |
| b-reopen | (b) against today's live body | — | **EXPOSED by live re-open** |
| c1 | S881 `window-scope: excerpt`→`whole-document` | **KILLED** (EVIDENCE) | — |
| c2 | S882 `visible-chars: 2953`→`2952` (whole-document) | **KILLED** (EVIDENCE) | — |
| c2b | S881 `visible-chars: 9855`→`4000` (excerpt) | **SURVIVES** (finding F1) | VERIFY FAIL |
| c3 | S881 `user-agent:`→`curl/8.23.0` | **KILLED** (EVIDENCE) | — |
| c3b | S881 `ua:`→`curl/8.23.0` only (duplicate line) | **SURVIVES** (finding F2) | VERIFY OK |
| c4 | S881 `http-status:` 200→404 | **KILLED** (EVIDENCE) | — |
| c4b | S881 `http:` 200→404 only (duplicate line) | **SURVIVES** (finding F3) | VERIFY OK |
| restored | all five files re-hashed == lands blobs | PASS 13/13 | — |

Probe commits in /tmp/MutEvidenceWindows/laneC (branch `mut`, each a child chain off lands):
a=c1f7ab48c40f3405c54470807926de3b31638b4c, b=b8fd6ea7a1d9e6d398989c331330dbe32d81e6a7,
c1=39e6785cee774aa3c17c2376edc22e1d420d611c, c2=ea1f478f442f03e4c845bae82f63ec1469e93473,
c2b(weak, 9854)=f59e7a50288b0593beb209a70396330964059c97, c2b(redo, 4000)=396f28eea00e30cf176a539d15704c632b033029,
c3=30d9b6ad36f5a3b5e5d7a63373fbd7cc39f1b225, c3b=2392f1ef55c7bb0698d6f14bcc8fb1a3fc91d4e1,
c4=61cb5177af1037027022ca58bc0693570355835a, c4b=c87235cc959724f645cb1e0f69b376201bb4a419.

## (a) One window character mutated, NOTHING recomputed — counter killed the mutant (attack found no defect; claim survived)

Mutation: `S881.txt` window line, one character, `触` (U+89E6) → `觸` (U+89F8), length- and byte-preserving
(both 3-byte UTF-8), ~1300 chars away from the Gate quote; no header field touched.

```
git -c user.name=mut … commit -q -m "probe-a: one window char mutated, nothing recomputed"  # M1=c1f7ab4…
python3 -B reports/round-74/accept-c.py --root . --lands c1f7ab48c40f3405c54470807926de3b31638b4c --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-74: FAIL legs=12/13
LEG FAIL EVIDENCE
     S881 window-sha256 '83e313a946d1cbec' != the recomputed digest of the stored window (b70c26d19f18e532)
```
Tool-level detector agrees: `capture-evidence.py --verify reports/round-74/evidence/S881.txt` →
`VERIFY FAIL … (1 problem(s))` with the same `window-sha256 mismatch` line. The `window-sha256:`-recomputation
limb of the EVIDENCE leg is real and bites.

## (b) Same mutation with `window-sha256` recomputed — offline survivor, exposed by live re-open

With the window mutated and `window-sha256:` updated to the recomputed digest (`b70c26d19f18e532fb072d571e86ef9120c85b37f4f9c67344b4b51d1af323e2`;
`window-bytes` unchanged at 11709), the counter passes everything:

```
python3 -B reports/round-74/accept-c.py --root . --lands b8fd6ea7a1d9e6d398989c331330dbe32d81e6a7 --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-C-74: PASS legs=13/13
```

This is exactly the residual the frozen claim declares ("an offline counter cannot prove a fetch happened, the
non-author re-open does"). The non-author re-open exposes it: re-fetching
`https://litmemo.com/ja/blog/novel-worldbuilding-guide` today (body sha256 441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64
= the stored value) and re-extracting with the tool's own code gives:

```
pristine window == live excerpt: True
mutated   window == live excerpt: False
make_window(live) == pristine window: True   (byte-for-byte regeneration of the stored window)
EXPOSURE: MUTATION EXPOSED by live re-open
```

So the residual is real but has a working backstop: any window tampering that updates the hash is caught by
re-extraction, because the stored window must be an exact collapse of the live page text. Recorded as residual
R1, not a new defect.

## (c) Scope / UA / status mutations

KILLED (raw `LEG FAIL EVIDENCE` lines):

- c1 — S881 `window-scope: excerpt`→`whole-document` (4098-char window):
  `S881 whole-document window is 4098 characters (>= 4096: declare excerpt); S881 whole-document window is 4098 characters but visible-chars is 9855` → `ACCEPT-C-74: FAIL legs=12/13`.
- c2 — S882 `visible-chars: 2953`→`2952` (whole-document equality limb):
  `S882 whole-document window is 2953 characters but visible-chars is 2952` → `ACCEPT-C-74: FAIL legs=12/13`.
- c3 — S881 `user-agent:`→`curl/8.23.0`:
  `S881 user-agent not recorded as a browser-shaped UA: 'curl/8.23.0'` → `ACCEPT-C-74: FAIL legs=12/13`.
- c4 — S881 `http-status:` 200→404:
  `S881 http-status '404' (want 200)` → `ACCEPT-C-74: FAIL legs=12/13`.

Three survivors (findings F1–F3 below). A first c2b attempt truncating 9855→9854 passes everywhere
trivially (9854 still exceeds the 4098-char window); the meaningful truncation is below the window length.

## (d) Live re-fetch today vs stored `sha256:` / `bytes:` — attack FAILED, claim survived

Every fetch: `curl -sS -L --compressed --connect-timeout 20 --max-time 90 -A "<UA>" -o <file> -w "%{http_code} %{size_download}" <url>`,
UA = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
(browser-shaped, identical to the recorded captures), run 2026-10-26T02:08Z (2026-10-25 23:08 host time -03,
same access-date day as the captures). All five URLs answered HTTP 200 on the first attempt — no wall, no
retry needed, hence no CDX probes required.

```
S877 http=200 live_bytes=1055723 (bytes MATCH vs stored 1055723) live_sha=e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9 (sha256 MATCH)
S881 http=200 live_bytes=101615  (bytes MATCH vs stored 101615)  live_sha=441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64 (sha256 MATCH)
S882 http=200 live_bytes=17068   (bytes MATCH vs stored 17068)   live_sha=754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7 (sha256 MATCH)
S883 http=200 live_bytes=48536   (bytes MATCH vs stored 48536)   live_sha=a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d (sha256 MATCH)
S884 http=200 live_bytes=62604   (bytes MATCH vs stored 62604)   live_sha=344de345cef7f5f98c64321f4ce5710faaec7563577e9b2ae306aa00bdd3d659 (sha256 MATCH)
```

Beyond the digest match, re-extraction with the tool's own code reproduces the recorded geometry exactly:
S882 live collapsed text = 2953 chars = stored whole-document window = `visible-chars:`; S877 pdftotext
re-extraction = 494887 chars (as recorded), collapsed 492810 = `visible-chars:`, and the stored window is a
substring of today's live collapsed text. The five evidence files are byte-faithful captures of the live
pages as of today; no fabrication, no drift. (S877's row URL is http:// — plaintext — but that is the
author-hosted MSU URL the round registered; the leg does not require https. Noted, not a defect.)

## (e) Independent fold + containment check — attack FAILED, claim survived

Independent implementation (not the counter's): own table parser for the Gate quotes, three independently
written folds — (A) whole-string NFKC + `str.split()` folding, (B) per-character NFKC + `isspace()`-driven run
collapse, (C) NFKD + `split()` — plus independent marker parsing, digest recomputation and cap checks.

```
S877 | win-sha OK | win-bytes OK | single-line OK | tokens 7<=25:OK  | chars 54<=80:OK | in-window A/B/C = 1/1/1 | qblock==gate:True hdr==gate:True | gate-row-sha:OK gate-row-size:OK | scope=excerpt visible=492810
S881 | … tokens 1<=25:OK  | chars 43<=80:OK | in-window A/B/C = 1/1/1 | … scope=excerpt visible=9855
S882 | … tokens 1<=25:OK  | chars 33<=80:OK | in-window A/B/C = 1/1/1 | … scope=whole-document visible=2953
S883 | … tokens 1<=25:OK  | chars 32<=80:OK | in-window A/B/C = 1/1/1 | … scope=excerpt visible=8162
S884 | … tokens 1<=25:OK  | chars 27<=80:OK | in-window A/B/C = 1/1/1 | … scope=excerpt visible=12270
INDEPENDENT CHECK: ALL GREEN (0 hard failure(s))
```

Every Gate quote occurs in its stored window after NFKC + whitespace folding under all three folds; every
stored `window-sha256:`/`window-bytes:` recomputes correctly; each Gate row's quoted sha256 and size match its
evidence file; all quotes respect the ≤25-token / ≤80-char caps.

## FINDINGS

**F1 [LOW] — excerpt-scope evidence may record `visible-chars` smaller than its own window; the claim's counter passes.**
Mutant: S881 `visible-chars: 9855`→`4000` (excerpt scope, window 4098 chars — a self-contradictory record,
since the window cannot exceed the whole text it was excerpted from).
Command: `python3 -B reports/round-74/accept-c.py --root . --lands 396f28eea00e30cf176a539d15704c632b033029 --freeze 00c408a0… --fleet-root /home/vgpnk/Projects/shokunin`
Raw output: `ACCEPT-C-74: PASS legs=13/13` / `LEG PASS EVIDENCE`, while the round's own tool on the same file
prints `VERIFY reports/round-74/evidence/S881.txt: window is longer than the whole text (4098 > 4000)` /
`VERIFY FAIL`. Root cause: `accept-c.py::_evidence_core` checks the excerpt limb only as
`len(window) < MIN_WINDOW_CHARS`; `capture-evidence.py::verify_file` additionally checks `len(win) > visible`
but the claim's counter never calls it. The frozen leg text cross-checks `visible-chars` only for
whole-document, so the counter is faithful to the letter and the gap is a coverage finding, not a broken
contract. Proposed fix (one line, offline): port the excerpt limb `if int(visible) < len(window): bad.append(...)`
into `_evidence_core`'s excerpt branch, mirroring `verify_file`.

**F2 [LOW] — the duplicate `ua:` line can contradict `user-agent:` undetected by both detectors.**
Mutant: S881 `ua:` (line 7) → `curl/8.23.0`, `user-agent:` (line 22) left browser-shaped. Output:
`ACCEPT-C-74: PASS legs=13/13` and `VERIFY OK …`. Root cause: the render grammar writes the UA twice;
`accept-c.py` reads `ev.get("user-agent") or ev.get("ua")` (never cross-checks), and `verify_file` checks no
UA shape at all (the Mozilla/5.0 check lives only in accept-c). An evidence file whose two UA records disagree
passes the round's gate. Proposed fix: cross-check `ua == user-agent` wherever either is read, or stop writing
the duplicate.

**F3 [LOW] — the duplicate `http:` line can contradict `http-status:` undetected by both detectors.**
Mutant: S881 `http: 200`→`http: 404` (line 3), `http-status: 200` untouched. Output:
`ACCEPT-C-74: PASS legs=13/13` and `VERIFY OK … http-status=200`. Root cause: same duplicate-record pattern;
both detectors prefer `http-status` and never compare the two status fields. Proposed fix: same as F2 —
cross-check or single field.

**R1 [RESIDUAL, disclosed by the claim, re-confirmed] — a hash-consistent window forgery passes offline.**
Probe (b): `ACCEPT-C-74: PASS legs=13/13` with a mutated window whose `window-sha256` was recomputed. This is
exactly the residual the frozen leg declares ("an offline counter cannot prove a fetch happened, the non-author
re-open does"). Working backstop demonstrated: re-fetch + re-extract today regenerates the stored window
byte-for-byte (`make_window(live) == pristine window: True`) and rejects the forged one
(`mutated window == live excerpt: False`). No new defect; the residual's compensation is real.

No BLOCKER/HIGH/MEDIUM findings. All killed mutants are exactly the limbs the EVIDENCE leg names
(window-sha256 recomputation, scope rule, browser-shaped UA, HTTP 200); the three survivors are
duplicate-field/conservation gaps in the recorded facts, each with a one-line offline fix.

## Restoration evidence

Probe commits live only in /tmp/MutEvidenceWindows/laneC (branch `mut`; `main` pinned at lands c4bf61a8,
worktree checked out at `main`, `git status --porcelain` = 0 entries). Final per-file verification against the
lane repo's committed blobs at lands:

```
S877 1659516145484016… IDENTICAL
S881 f22e223e39ed7a5f… IDENTICAL
S882 e6030849c25eabb7… IDENTICAL
S883 6013c8258e52c34c… IDENTICAL
S884 68bede11dc8d1be3… IDENTICAL
```

(sha256, full values in the run log: S877 165951614548401672378ff8b4696f83b7581b17ecf30922e8edfa3c93acdf26,
S881 f22e223e39ed7a5fb8049e8e467cbe4d1f57dd330db5a24881c125ffce78c145,
S882 e6030849c25eabb7ee742ba4f100977d8b02599191d21cf4c440d4b58e9f7da7,
S883 6013c8258e52c34cd622de5021cfbf76302bc9d607c01d459ad841385533aa9c,
S884 68bede11dc8d1be3856deb4b61a34fd0886fb6f139eb1128dba41dc812948029.)
Restored-bytes detector run: `ACCEPT-C-74: PASS legs=13/13` at lands. The first clone
(/tmp/MutEvidenceWindows/lane, used for the accept-ca baseline with its `main` at 5e4796c0) is clean. The lane
repo at /home/vgpnk/Projects/shokunin/kotodama-shokunin was never written except this report file.

## Notes

- Fetch hygiene (QUALITY 21/22/24): exact UA per fetch recorded above; browser-shaped on every fetch; no wall
  encountered (no plain-curl fallback needed), so no 'no capture' ruling and no CDX probe was required.
- One transient infrastructure failure during probe c2's first counter run: `ERROR: materialize f7104cbce186
  failed (git rc=0, tar rc=2)` with the root filesystem at 100% (1.1 GiB free); the rerun on the same commit
  succeeded. Inconclusive runs are not counted as kills; the kill rests on the rerun output above.
- Tooling: nothing installed or upgraded (curl 8.23.0, python3 stdlib, pdftotext already present). Pacman not
  used, per the 2026-10-20 host-wide pause.
