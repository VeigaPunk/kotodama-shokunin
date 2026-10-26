# MutPredicateC — round 74 WAVE 2, falsify seat (hyaku run 7)

Seat: MutPredicateC (leaf). Attacked: claim C's vacuity predicate at the LANDED
frozen claims — for each of the 13 legs, the cheapest junk landing its wording
would pass, graded by `reports/round-74/accept-c.py`.
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; freeze F3
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands
`c4bf61a8d722f9168ce0fd8021a6261c000610c5`. No claim text amended; no live
repo touched; all mutations lived in my clone under
`.ufo/waves/round-74/w2/mutpredicatec-scratch/lane` (now removed; see
Restoration).

Method: clone → `reset --hard <lands>` → apply one junk class per leg →
commit → run the counter with `--lands <junk-commit>` (local `main` pinned to
the junk commit, per protocol) → record → `reset --hard <lands>`. The counter
graded each junk landing from its own fresh mktemp checkout ("worktree
graded: no"); counter bytes never changed (self sha256
`8d30487fa4692261edfee549d2ba07517fc8b3c9fc4f5af5f0562a504ca5433a` on every
run).

Environment / tooling: no tools installed (none needed; pacman pause
respected). NO network fetches were made — this is an offline vacuity attack,
so fetch-hygiene UA rules never triggered; the survivors that only a live
fetch can close are listed as such. Incident: `/tmp` was 100% full (1.1 MiB
free, host-wide) and the first batch-1 run died with `ERROR: materialize
f7104cbc... failed (git rc=0, tar rc=2)` exit=2 — an ENOSPC refusal, not a
verdict; I moved my scratch to the granted `.ufo/waves/round-74/w2/` area and
set `TMPDIR` there (`/tmp` recovered to 3.5 GiB free).

## Detector validation (pristine)

```
python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
  --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
→ ACCEPT-C-74: PASS legs=13/13   exit=0   tree 29c8c147c948b9fe03af8f092ac92028a23fed56
```

Baseline is green, so every verdict below is interpretable.

## Mutant ledger (before = lands `c4bf61a8…`, tree `29c8c147…`; graded bytes from each mutant's own commit)

| run | lands (junk commit) | tree | junk classes | verdict |
|---|---|---|---|---|
| batch-1 | `d4e1819d49b15a2f3d26b7292e7e646fe53904dc` | `01d1df9e96a84e11c285c98978b0a23ca3659153` | ENTRIES filler body; EVIDENCE fabricated window; INDEX ghost row; REJECTS gutted reasons; GROUND fabricated receipt; CITEDLINES stub tool; COLLCHECK fabricated guard proof | **ACCEPT-C-74: PASS legs=13/13** |
| batch-2a | `a9a6b20c65dba23aa5266ec8dc838187ed6ad8f8` | `f5eabd51e4d5065147e59f5936135c92d81cb602` | duplicate S881 registry row (1472-char byte-identical copy) | FAIL legs=11/13 — ROWS, CENSUS red |
| batch-2b | `335e92855970525e0a271287e92013513f7ff585` | `85bf61d968511830cb7941c0b2f23ac6181b56b2` | unrelated old row cell drift (S001 tier A→C) | FAIL legs=12/13 — ROWS red, **CENSUS green** |
| batch-2c | `19b295cf19888564233a7342fca4996b0c62b590` | `4a1409545ab834a7eca6722af8f7ea02d8f67474` | GATE 25-token/130-char span; REPOINTED backticked `S899`; FROZENCFG one-space graded claims.json edit; INDEX duplicated row | FAIL legs=9/13 — REPOINTED, GATE, FROZENCFG, INDEX red |
| batch-10 | `78ee737b8edc7d2a06207356bb102790357bc45f` | `06955bd3a9e75958de17e008de2d929de06f64f1` | SCRATCHMIRROR fabricated receipt committed before the (rebuilt) append commit | **ACCEPT-C-74: PASS legs=13/13** |

Batch commands (all runs identical shape; TMPDIR moved off the full /tmp):

```
python3 -B reports/round-74/accept-c.py --root . --lands <junk-commit> \
  --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
```

## Findings — predicate survivors (attack SUCCEEDED; junk the wording admits that the counter also accepts)

### F1 — CITEDLINES: the landed tree's own checker is neuterable — HIGH
The leg runs `tools/check-cited-lines.py` **from the materialized lands tree**
(`leg_citedlines`: `tool = os.path.join(mat, "tools/check-cited-lines.py")`)
and nothing pins its bytes (FROZENCFG pins only claims.json and the map). A
landing that replaces the 287-line checker with a stub satisfies the wording
("the tool prints …") and passes.
Junk: `tools/check-cited-lines.py` → `print("CITED-LINES: 0 finding(s) in %d
file(s)" % (len(sys.argv)-1))` (287 → 4 lines).
Raw output (batch-1): `LEG PASS CITEDLINES` inside **PASS legs=13/13**, with
the entry body simultaneously replaced by 735 words of filler the real tool
would also have passed.
Fix (machine-checkable): pin the tool like the map — wording append "…whose
blob at <lands> is byte-identical to `git show <freeze>:tools/check-cited-lines.py`";
counter compares `git show <lands>:<tool>` sha256 to a frozen value.

### F2 — SCRATCHMIRROR: the receipt is verified as prose, never executed — HIGH
The counter checks the receipt for the tokens `--file`, an exit-0 pattern, the
four ids and both entry basenames, plus commit ordering. It never runs
`validate --file` and never looks at any mirrored corpus (none exists in the
tree). I fabricated a receipt that says, quoted for location,
`mirror root: /tmp/nowhere-does-not-exist/validate` and `# … No mirrored
corpus was ever built … every line below is invented prose` (the fabrication
is self-declared in the file), committed it at `5489ee7` strictly before a
rebuilt append commit, and rebuilt lands on top.
Raw output (batch-10): all 13 `LEG PASS` lines, `ACCEPT-C-74: PASS legs=13/13`, exit=0.
Fix (needs re-execution, not a fetch): wording "…and the counter re-runs
`sources-census.sh validate --file` over the registry blob the receipt names
at the receipt commit, requiring exit 0 and no `^E` line; a receipt whose
named blob is absent or differs fails."

### F3 — COLLCHECK: guard "proof" is pattern-matched, the guard is never run — HIGH
`leg_collcheck` scans files under `.ufo/waves/round-74/assimilation/` for a
1–3-space planted row id with a positive marker line and a 4-space plant with
a not-found marker. Appending fabricated proof lines (plants S9994/S9995,
"collision detected, found, exit 1" / "not found, no collision (0 rows)") —
executed by nothing — keeps the leg green.
Raw output (batch-1): `LEG PASS COLLCHECK` inside **PASS legs=13/13**.
Fix (needs re-execution): "…and the counter re-runs the guard
(`run-guard.sh`) over regenerated fixtures at grade time; marker prose alone
does not satisfy the leg" — or pin the proof files' blobs at the freeze.

### F4 — EVIDENCE: fabricated window + recomputed `window-sha256` passes; "around the quote" is unenforced — HIGH (authenticity half is a DECLARED residual)
The tasking's named example. I replaced S881's stored window with
`<Gate quote> + " filler"×700` (4943 chars, 5029 bytes), recomputed
`window-sha256: 6e4bb543c61e331a43810ac10964a7ae37df56982ca1a5dd6da298acc7003b13`
and `window-bytes:` — the counter recomputes the digest over the stored bytes,
so a fabricated window self-certifies. I also put the quote at offset 0,
which violates the wording's "window >= 4096 characters **around** the quote"
(the counter checks only `len(window) >= 4096` and quote-in-window).
Raw output (batch-1): `LEG PASS EVIDENCE` inside **PASS legs=13/13**.
The claim wording already carries the residual ("an offline counter cannot
prove a fetch happened, the non-author re-open does"), so the authenticity
half is known-open; the scope limb and the stale body `sha256:` (only
format-checked, never compared to anything) are tightenable now.
Fix (machine parts): "…the quote cell's span must begin between 25% and 75%
of the window; the recorded body `sha256:` must equal the digest recorded at
the Gate row" — plus the declared live re-open for authenticity (below).

### F5 — GATE: a quote that is in the window but not on the live page — DECLARED residual, needs live fetch
Offline-indistinguishable by construction: the landing controls both the
lesson's quote cell and the window. Batch-1's window mutant already
demonstrates the coupling is internal to the landing's own artifacts; the
"not on the live page" half is exactly what the wording routes to the
non-author re-open. Attack on the machine predicate FAILED beyond the
declared residual (see also F12: the counter recomputes quote caps).
Fix: none offline — keep the residual clause; the re-open must re-fetch with
the recorded browser UA and a canonical-slug CDX probe per QUALITY 21/22/24.

### F6 — REJECTS: family "reason and flip" is checked as two words, not per row — MEDIUM
The wording requires "each refused family and file in rejects, each with
reason and flip". The counter only checks (a) each family name appears
anywhere in the lesson, (b) the words "reason"/"flip" appear anywhere, (c) the
2/4/34/40 sentence. I gutted all six "why not adopted" cells to `—` (the
tasking's "listing the family names without reasons").
Raw output (batch-1): `LEG PASS REJECTS` inside **PASS legs=13/13**.
Both boxes apply: junk with fabricated one-word reasons also passes (content
unchecked), and junk without reasons passes (this run).
Fix (machine-checkable): "…the counter parses the family table's reason and
flip columns and requires every row's cells to be non-dash" (the table already
has the columns).

### F7 — ENTRIES: 735-word filler body passes the length-and-shape gate — MEDIUM (declared residual)
Entry 1's body after the first `## ` was replaced with one repeated 14-word
sentence (header block byte-preserved). Wording declares "ENTRIES is a
length-and-shape gate only — content fidelity is carried by GATE, EVIDENCE
and the non-author re-open" — but GATE/EVIDENCE couple only the quotes, so
entry prose is uncoupled from anything.
Raw output (batch-1): `LEG PASS ENTRIES` inside **PASS legs=13/13**.
Fix (machine-checkable, closes most of it): "the body must contain, for each
adopted row, that row's Gate quote or a ≥20-character NFKC overlap with it".

### F8 — GROUND: receipt counts are parsed decoratively — LOW
I replaced the gap-sweep receipt with one claiming **3/2/1 fragment hits and
4/5/6 CJK files** (the opposite of the truth), keeping `804-row` and putting a
decorative `0` ("appendix 0") within three lines of each term.
Raw output (batch-1): `LEG PASS GROUND` inside **PASS legs=13/13**.
Severity LOW because the counter *independently* re-derives the absence at
base (fragment-not-in-base-registry, term-not-in-base-bodies), so the junk
receipt cannot hide real coverage — but the leg as worded ("names … 0
matches") is not what the machine enforces. Receipt authenticity (was a sweep
ever run) is the usual offline residual.
Fix (machine-checkable): "each term line must match `<term>: 0$`" (count
immediately after the colon).

### F9 — INDEX: rows for files that do not exist are unchecked — LOW
Wording: "exactly one row per adopted entry …". I added
`- `zzz-fabricated-junk-entry.md` — fabricated topic line for a file that
does not exist` inside `## culture-material/ (36)` (corpus/README.md, after
the worldbuilding-setting-practice.md row).
Raw output (batch-1): `LEG PASS INDEX` inside **PASS legs=13/13**.
Fix (machine-checkable): "every `- `name.md` — …` row in corpus/README.md
names a file that exists under corpus/knowledge at <lands>".

### F10 — CENSUS is blind to cell-value drift — LOW (informational)
Flipping an unrelated old row's tier (S001 A→C) left CENSUS green
(`census exit=0`, no E-code) — only ROWS's byte-identity caught it
(`LEG FAIL ROWS / S001 removed (only a reused row's used-by cell may change)`).
CENSUS's own wording promises only "exits 0 … no ^E[0-9][0-9]", so this is not
a wording violation — but the tier guard lives solely in ROWS. The census
tool itself reads from the fleet repo (outside any lane landing's reach), so
no CITEDLINES-style tool swap exists here. Attack on CENSUS FAILED (claim
survived, via ROWS).

### F11 — EVIDENCE couples any ok span in the admit ROW, not the quote column — LOW/MEDIUM
Observed in batch-2c: with the quote cell's span made invalid (25 tokens /
130 chars → `LEG FAIL GATE / …(recomputed: tokens=[25] chars=[130])`),
EVIDENCE still passed because `quoted_spans` runs over the whole row and the
locator cell's `「3. 外側の層へ因果をつなぐ」` (2 tokens) is a valid span that
occurs in the window. So "the Gate quote occurs in the stored window" is
satisfied by *any* quoted span of the row.
Fix (machine-checkable): restrict the EVIDENCE coupling to the quote column's
spans.

## Findings — counter caught the junk (attack FAILED; the claim survived)

### F12 — ROWS duplicate row — CAUGHT
Junk: byte-identical copy of the 1472-char S881 row appended to
corpus/SOURCES.md (wording: "adds exactly S881..S884" — violated).
Raw output (batch-2a):
```
LEG FAIL ROWS
     added rows ['S881', 'S881', 'S882', 'S883', 'S884'] (want ['S881', 'S882', 'S883', 'S884']); a row line is added twice: ['S881', 'S881', 'S882', 'S883', 'S884']
LEG FAIL CENSUS
     census exit=1 (exit=1 last-line=kotodama	E12	S881 row outside Registry section)
```
Two independent legs red. Attack FAILED.

### F13 — REPOINTED backticked staged-id mention — CAUGHT
Junk: a prose line in entry 1 mentioning `` `S899` `` in backticks (arguably a
mention, not "cited as a lane row"). Raw output (batch-2c):
```
LEG FAIL REPOINTED
     corpus/knowledge/culture-material/worldbuilding-setting-practice.md:18 inline id S899 resolves to no adopted/reused row; corpus/knowledge/culture-material/worldbuilding-setting-practice.md cites staged-namespace id S899 as if it were a lane row
```
Note: the counter is STRICTER than a loose reading of the wording (it bans
every occurrence). Attack FAILED; suggest the wording clarify "no occurrence,
mentions included".

### F14 — GATE oversized quote — CAUGHT (machine recompute, H3)
25-token, 130-char span replaces S881's 1-token/43-char quote. Raw output
(batch-2c): `LEG FAIL GATE / S881 admit row quote exceeds 25 tokens or 80
characters (recomputed: tokens=[25] chars=[130])` — caught on the character
limb. Attack FAILED.

### F15 — FROZENCFG graded-tree claims.json edit — CAUGHT
One appended space inside the graded `reports/round-74/claims.json`. Raw
output (batch-2c): `LEG FAIL FROZENCFG / reports/round-74/claims.json at
lands differs from the frozen bytes (counter config edited in the graded
tree)`. Attack FAILED. (This is also the round's own control; mine
re-confirmed it at the lands commit.)

### F16 — INDEX duplicated row — CAUGHT
Byte-duplicate of the adopted entry's README row. Raw output (batch-2c):
`LEG FAIL INDEX / worldbuilding-setting-practice.md has 2 index rows (want
exactly one)`. Attack FAILED.

### ROWS/GATE/EVIDENCE content truth — the shared residual
The only "junk" that survives on those legs is the self-consistent
fabrication (fabricated rows + entries + quotes + windows, F4/F5/F7), which
is offline-indistinguishable from an honest landing and is what the claim's
residual clause and kill_rule route to the non-author re-open. That is a
coverage finding, not a wording defect: the claim already says so.

## Answer to the seat question

Legs whose wording is satisfiable by junk the counter also accepts
(predicate survivors): **ENTRIES (F7), EVIDENCE (F4, F11), GATE (F5,
within the declared residual), REJECTS (F6), GROUND (F8), CITEDLINES (F1),
SCRATCHMIRROR (F2), COLLCHECK (F3), INDEX (F9, ghost rows), and ROWS only in
the shared self-consistent-fabrication class** (its discrete machine checks
all held: F12).
Legs where junk the wording permits is caught: **REPOINTED (F13), GATE
caps (F14), FROZENCFG (F15), INDEX duplicates (F16), ROWS line-level diff
(F12), CENSUS via ROWS (F10)**.

The round's own junk controls (junk-c.txt) cover five classes (400-word
stubs; staged used-by rows; quote-not-in-window; graded-tree config edit;
typed flag over a fabricated window). This seat adds eight junk classes the
landed predicate accepts: F1–F4, F6–F9.

## Ranked wording tightenings (exact text)

1. CITEDLINES (F1, machine): append to the leg: "whose blob at <lands> is
   byte-identical to `git show <freeze>:tools/check-cited-lines.py`".
2. SCRATCHMIRROR (F2, execution): replace "validate-receipt.txt shows …" with
   "validate-receipt.txt shows …, and the counter re-runs
   `sources-census.sh validate --file` over the registry blob the receipt
   names at the receipt commit, requiring exit 0 and no `^E` line; a receipt
   whose named blob is absent or differs fails".
3. COLLCHECK (F3, execution): append "and the counter re-runs the guard over
   the regenerated fixtures at grade time; marker prose alone does not
   satisfy the leg".
4. EVIDENCE (F4/F11, machine + declared live): append "the quote must lie
   between 25% and 75% of the stored window; the coupling span is the quote
   column's span, not any span of the row; authenticity remains with the
   non-author re-open".
5. REJECTS (F6, machine): replace "each with reason and flip" with "with the
   family table's reason and flip cells non-dash on every row (the counter
   parses the columns per row)".
6. ENTRIES (F7, machine): append "and the body contains, for each adopted
   row, that row's Gate quote or a ≥20-character NFKC overlap with it".
7. GROUND (F8, machine): append "each count line must read `<term>: 0`
   (count immediately after the colon)".
8. INDEX (F9, machine): append "and every `- `name.md` — …` row in
   corpus/README.md names a file that exists under corpus/knowledge at
   <lands>".
9. REPOINTED (F13, clarity): replace "no campaign-namespace id is cited as a
   lane row" with "no campaign-namespace id occurs anywhere in either entry,
   mentions included".

Survivors needing a LIVE FETCH (not machine-checkable): F4 authenticity
(window really came from the row URL), F5 (Gate quote really on the live
page), and the ROWS/GATE/EVIDENCE shared content class — close via the
declared non-author re-open with the recorded browser UA
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/130.0 Safari/537.36` plus a canonical-slug CDX probe with a positive
control. Survivors needing re-EXECUTION (no fetch): F2, F3. All other
tightenings above are machine-checkable offline.

## Restoration

After the last mutant: `git checkout --detach c4bf61a8…`,
`git branch -f main c4bf61a8…`, `git clean -qfd`:
HEAD `c4bf61a8d722f9168ce0fd8021a6261c000610c5`, tree
`29c8c147c948b9fe03af8f092ac92028a23fed56` (== the pristine baseline receipt
tree), `git status --porcelain` = 0 entries. Restoration baseline re-run:
`ACCEPT-C-74: PASS legs=13/13`, exit=0, counter sha256 unchanged
(`8d30487f…`). The scratch clone, TMPDIR and mutate.py helper were then
deleted; this report is the only file this seat leaves under
`.ufo/waves/round-74/w2/`. The real lane repo, its git/jj state, and the
fleet repo were never written.
