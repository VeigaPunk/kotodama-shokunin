# ExecDApply59 — claim D application in a sandbox clone (round 59, BUILD wave)

Seat: KotodamaR59.ExecDApply59 (leaf). Assignment: apply the frozen claim-D fixes to a sandbox
clone of the lane at `ff802cc3cb003f128faa88e90658749c9151bd08`, run `reports/round-59/accept-d.py`
there, stage the two patched files, and report hashes and the clone diffstat. **No lane writes**
beyond this report.

**Result: ACCEPT-D-59: PASS (KONGO PASS, SPEECH PASS, CARRY PASS, exit 0).** Both patched files
are staged at `/fast/scratch/hyaku/kotodama-r59/ExecDApply59/out/` with the repo-relative paths, so
landing is a two-file copy. No blockers, no installs, no git/jj write commands.

## 1. Sandbox and instrument identity

```
$ cd /fast/scratch/hyaku/kotodama-r59/ExecDApply59
$ env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone --no-checkout /home/vgpnk/Projects/shokunin/kotodama-shokunin clone
Cloning into 'clone'...
done.
exit=0
$ cd clone && env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git checkout -f ff802cc3cb003f128faa88e90658749c9151bd08
HEAD is now at ff802cc round-59: claim base = freeze d4795abd (claims.json, separability manifest)
exit=0
$ git rev-parse HEAD
ff802cc3cb003f128faa88e90658749c9151bd08
```

Instrument identity, clone vs lane (`sha256sum` of both copies, same value each pair) — the clone at
ff802cc3 carries the frozen instruments byte-identically to the lane's working copies:

| file | sha256 (clone = lane) |
|---|---|
| `reports/round-59/d-fixes.json` | `071232871fb2a8e7fb85cf8a83d15e9cb6e9305d58d63f5a7eab9114018d1c86` |
| `reports/round-59/accept-d.py` | `fc107d8fe49117ca11ba014801a5d135d06542098931909497caeed019b0df48` |
| `reports/round-59/rowcheck.py` | `ffe6fa096b9654c26efffa2948603f973a82038e18c959224648c2be8ac52e7a` |
| `reports/round-59/reopen-quote.py` | `64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8` |
| `reports/round-59/claims.json` | `d6ee39fd18c28b5c02a1bc43864571c751ece250cef2946e6db1bfba8eab7b78` |

Claim base read from that claims.json: `d4795abdcbf4557fb1c2d0f92f65dd14cfa26fa5`. At that base and
in the checked-out tree both targets are byte-identical to the base blobs, CRLF count 0:

```
kongo  corpus/knowledge/civilizations/kongo-kingdom.md                worktree==base: True  30155 bytes
speech corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md worktree==base: True 41389 bytes
```

## 2. Application (`apply-d.py`, Python 3 stdlib, newline='' so bytes are preserved)

Each kongo `old -> new` applied exactly once, in `d-fixes.json` order, with a hard stop unless the old
string occurs exactly once; the speech ids remapped as whole words (`\bS1NN\b`), each countchecked
against the frozen `base_counts`.

```
$ cd /fast/scratch/hyaku/kotodama-r59/ExecDApply59 && timeout 120 python3 -B apply-d.py
applied kongo fix 18: old_occurrences=1 new_len=62
applied kongo fix 65: old_occurrences=1 new_len=163
applied kongo fix 82: old_occurrences=1 new_len=84
applied kongo fix 84a: old_occurrences=1 new_len=151
applied kongo fix 84b: old_occurrences=1 new_len=37
applied kongo fix 85: old_occurrences=1 new_len=244
applied kongo fix 89: old_occurrences=1 new_len=189
applied kongo fix 93: old_occurrences=1 new_len=133
applied kongo fix 97a: old_occurrences=1 new_len=230
applied kongo fix 97b: old_occurrences=1 new_len=28
applied kongo fix 110: old_occurrences=1 new_len=122
applied kongo fix 140: old_occurrences=1 new_len=257
applied kongo fix 141: old_occurrences=1 new_len=401
applied kongo fix 146: old_occurrences=1 new_len=42
remapped speech S135 -> S570: 16 substitutions (declared base count 16)
remapped speech S141 -> S571: 2 substitutions (declared base count 2)
remapped speech S147 -> S572: 3 substitutions (declared base count 3)
remapped speech S151 -> S573: 2 substitutions (declared base count 2)
remapped speech S159 -> S574: 4 substitutions (declared base count 4)
apply-d: done
exit=0
```

Each fix id is also its line number in the patched `kongo-kingdom.md` (fixes 84a/84b share line 84,
97a/97b share line 97), so a reviewer can spot-check by line:

| id | line | change |
|---|---|---|
| 18 | 18 | S359 doc. 142 `p. 469` -> `p. 470` |
| 65 | 65 | 1512 Regimento sentence -> "the old lineage heads of the provinces began styling themselves as counts, marquises and dukes" |
| 82 | 82 | "royal control of church organization" -> "Kongo's control of church organization" |
| 84a/84b | 84 | ca. 1740 watercolor sentence for the *mestres*; "Overview label, object 318318" -> "record 318318" |
| 85 | 85 | execution date sentence split: Batsîkama's own 2 July 1706 (p. 27), Randels quotation Kimbangu (p. 32), Farias Mbanza Kongo |
| 89 | 89 | Met nkisi sentence -> "may relate to a wide spectrum of physical receptacles..." |
| 93 | 93 | "centre of palero practice" -> "centre of the paleros' attention" |
| 97a/97b | 97 | watercolor leader sentence; cap date "late-1800s" -> "late-1800s–early-1900s" |
| 110 | 110 | table row: S359 doc. 147 `p. 489` -> `p. 490` |
| 140 | 140 | vetting line: doc. 142 p. 470 and doc. 147 p. 490 |
| 141 | 141 | Thornton sentence: older opinion quoted, African-form argument stated |
| 146 | 146 | "no writing" line: doc. 142 `p. 469` -> `p. 470` |

Post-application check: every `old` absent and every `new` present exactly once —
`old_present_or_new_count_ne_1: []` (14 fixes).

## 3. Acceptance run in the clone

```
$ cd /fast/scratch/hyaku/kotodama-r59/ExecDApply59/clone && timeout 900 python3 -B reports/round-59/accept-d.py; echo "exit=$?"
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T03:12Z failing=[]
ACCEPT-D-59: PASS
exit=0
```

Wall time 169.27 s. KONGO is a byte-equality test against "base with the 14 frozen substitutions
applied once, in file order", so no stray edit, no appended sentence and no unfixed sentence can
pass; SPEECH is byte-equality against the whole-word remap plus zero old ids left.

## 4. Staged files, hashes, clone diffstat

```
$ cp clone/corpus/knowledge/civilizations/kongo-kingdom.md out/corpus/knowledge/civilizations/kongo-kingdom.md
$ cp clone/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md out/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
$ find out -type f -printf '%s %p\n' | sort
30711 out/corpus/knowledge/civilizations/kongo-kingdom.md
41389 out/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
$ sha256sum out/corpus/knowledge/civilizations/kongo-kingdom.md out/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
0e1b415f653f31b783e1eedd1c27a9ea845ddbc91ad70c1a6278ce446ac115df  out/corpus/knowledge/civilizations/kongo-kingdom.md
e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb  out/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
$ git -C clone diff --stat
 corpus/knowledge/civilizations/kongo-kingdom.md    | 24 ++++++++--------
 .../speech-surrogates-whistled-drummed.md          | 32 +++++++++++-----------
 2 files changed, 28 insertions(+), 28 deletions(-)
```

The `out/` copies hash-identical to the clone worktree files (same two digests recomputed there).
kongo grew 30,155 -> 30,711 bytes; speech is size-neutral at 41,389 because the remap swaps five
same-length ids 16/2/3/2/4 times.

`git status --porcelain` in the clone shows exactly the two modified files and nothing else.

## 5. CARRY route detail (which listed URL actually carried each quote)

Read-only probe (`probe-routes-seq.py`): loads the frozen `rowcheck.py` as `accept-d.py` does, wraps
`rowcheck.locator.fetch` to log every attempt, and calls `rowcheck.locator.locate` per fix in file
order. It claims no verdict; it records the route. **Every fix located on the FIRST listed URL, with
no fetch error and no fallback capture used.** (An earlier parallel probe produced the same verdicts
but interleaved its attempt log across threads; its per-URL attribution is discarded, the sequential
run below is the retained evidence.)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ExecDApply59 && timeout 600 python3 -B probe-routes-seq.py; echo "exit=$?"
fix 18:  located=True resolved=https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt   [ok 896693]
fix 65:  located=True resolved=https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf                              [ok 67503]
fix 82:  located=True resolved=https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 [ok 1158758]
fix 84a: located=True resolved=https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf                                       [ok 1291427]
fix 84b: located=True resolved=https://www.metmuseum.org/art/collection/search/318318                                               [ok 235512]
fix 85:  located=True resolved=https://revistas.usp.br/sankofa/article/download/187402/173183/497395                                  [ok 985805]
fix 89:  located=True resolved=https://www.metmuseum.org/art/collection/search/312342                                               [ok 235627]
fix 93:  located=True resolved=https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480            [ok 303987]
fix 97a: located=True resolved=https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf                                       [ok 1291427]
fix 97b: located=True resolved=https://openaccess-api.clevelandart.org/api/artworks/159880                                          [ok 8764]
fix 110: located=True resolved=https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt [ok 896693]
fix 140: located=True resolved=https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt [ok 896693]
fix 141: located=True resolved=https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 [ok 1158758]
fix 146: located=True resolved=https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt [ok 896693]
exit=0
```

(The brackets are the served body size in bytes recorded by the wrapper; the tool's own lines print
`located=<bool> resolved=<url>` plus one `tried ok <bytes> <url>` line per attempt.) Fixes 82 and 141
list only Wayback captures, and fix 93 lists only four captures (no live URL) — each answered on its
first capture today, so CARRY does not depend on a live Cambridge or openedition fetch.

## 6. Landing instructions for the L1 (lane untouched by this seat)

Checked read-only just now: lane HEAD `5ed5b8e0aaacb146ac8cee027ac9bf50bc691b17`, and both target
files are still byte-identical to claim base `d4795abd` (`LANE_UNCHANGED` for both). So the staged
files are an exact, unambiguous land — whole-file copy, no patch application:

```
cp /fast/scratch/hyaku/kotodama-r59/ExecDApply59/out/corpus/knowledge/civilizations/kongo-kingdom.md \
   /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/civilizations/kongo-kingdom.md
cp /fast/scratch/hyaku/kotodama-r59/ExecDApply59/out/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md \
   /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-59/accept-d.py
```

Expected after the copy: `sha256sum` of both lane files equals the two digests in §4, and the lane
run prints the same three PASS lines. If the lane files moved since `5ed5b8e0`, re-check with
`cmp` before copying; a divergence means a sibling touched them and the land must be reconciled, not
overwritten.

## 7. Follow-up that rides claim C's land path (SOURCES rows, not D's counter)

Observed at base, not touched by this seat: after the remap no knowledge file cites `S135`, `S141`,
`S147`, `S151` or `S159` (only `corpus/SOURCES.md` still mentions them), while the speech entry now
cites `S570`–`S574`, whose registry rows are still `queued` with `used-by —`:

| id | status | used-by | teaches opens |
|---|---|---|---|
| S570 | queued | — | `supersedes S135 —` |
| S571 | queued | — | `supersedes S141 —` |
| S572 | queued | — | `supersedes S147 —` |
| S573 | queued | — | `supersedes S151 —` |
| S574 | queued | — | `supersedes S159 —` |
| S135/S141/S147/S151/S159 | mined | `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | (unchanged) |

Lane precedent for superseded rows, measured across all 43 `supersedes` pairs in SOURCES.md: the old
row is never edited (e.g. `S126` mined/used-by sign-languages while `S105` still mined/used-by the
same file, and that file still cites `S105` once and `S126` three times). So the records item in
claims.json is the whole job: flip `S570`–`S574` to `mined` with `used-by
corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` and log each old→new in the
round-59 lesson; leave the five old rows as the 43-pair precedent leaves them.

## 8. Risks

- **CARRY is non-discriminating by design** (accept-d.py docstring): the base tree passes CARRY too.
  The discriminating legs are KONGO (byte equality to the frozen transform) and SPEECH (whole-word
  remap equality plus zero remaining old ids), both PASS here.
- **Wayback dependence at re-run time.** Fixes 82, 141 (captures only) and 93 (four captures, no live
  URL) rely on `web.archive.org`. Today the first capture of each answered in one GET; a future
  `accept-d.py` run on a throttled archive skips a failing URL and can fail CARRY without any text
  change. That is the declared FETCH-59 behaviour, not a defect of this land.
- **Wording is the frozen round-58 verdict, not re-judged here.** Fix 82's new sentence attributes
  the control to "Kongo" while the served quote's subject is "it"; fix 93 changes "palero practice"
  to "the paleros' attention". Both are exactly the frozen `new` strings, so the reviewer question
  ("is each new sentence the best reading of its page") stays the round-59 falsify seats' sample,
  per accept-d.py's review-only note.
- **SOURCES gap until C lands** (§7): `S570`–`S574` stay `queued`, so any later checker that requires
  cited ids to be `mined` would surface the gap there. D's counter does not read SOURCES.
- **Whole-file land is safe only against base-identical targets**; the `cmp` re-check in §6 covers a
  concurrent edit by a sibling between this report and the copy.

## 9. Rejected / not done

- Nothing was rejected and nothing is blocked.
- No tool installed or updated (none needed; python3 stdlib only).
- No lane, fleet-repo or sibling-lane file created, edited or deleted; this report is the only lane
  write. No `git`/`jj` write command ran anywhere; read-only `git show`, `rev-parse`, `status`,
  `diff`, `clone`/`checkout` inside the scratch clone only.
- No subagent, background service or swarm was started; both long runs were foreground `timeout`-capped
  commands that completed (169 s and 178 s), and no process of mine survives.

## 10. Scratch artifacts (all under `/fast/scratch/hyaku/kotodama-r59/ExecDApply59/`)

| file | sha256 | note |
|---|---|---|
| `apply-d.py` | `44a54d086b69be0960dd66dba48e2100771a8259bdef9b9cb9b681a6b017e587` | the applier (read/write newline='') |
| `probe-routes-seq.py` | `9be6a2c1cdc4d9b91a2d27311a1f262353bbabe65fd64d6ab0e669b9a1db4ff4` | sequential route probe |
| `probe-routes.py` | `3138ca8f7a78965a09cb89993a3f6bbaf96f7176bccc908ac046cf8f07bf8a48` | parallel probe (verdicts agree; log interleaved, not used) |
| `probe-routes-seq.out` | `a881222362c05b55c6465b7f697750c28eacea214dc3db9086ff222259169f56` | §5 output, 3,543 bytes |
| `probe-routes.out` | `9c72ac077bee2213dc15066cac425ef68289d6cbb63e9f44d2d59f250423a3bd` | first probe output, 10,370 bytes |
| `d-diff.patch` | `baae6f8866a3f1a04db1729acc65d7086f6d137af733d610ad4e5cd97fd2a061` | full `git diff -- corpus` of the clone, 39,786 bytes |
| `out/corpus/knowledge/civilizations/kongo-kingdom.md` | `0e1b415f653f31b783e1eedd1c27a9ea845ddbc91ad70c1a6278ce446ac115df` | land candidate |
| `out/corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` | land candidate |
