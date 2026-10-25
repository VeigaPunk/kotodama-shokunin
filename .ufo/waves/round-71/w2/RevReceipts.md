# RevReceipts — round-70 telemetry re-stamps: byte preservation and header honesty

Seat: `L1Kotodama71.RevReceipts` (reviewer, leaf; no delegation, lane read-only).
Assigned scope: verify the six round-70 telemetry receipts preserve their original bytes below the
marker, by diffing the below-marker region against
`git show 453676a2:reports/round-70/telemetry/<file>`.
Reviewer scope on the same artefacts: the header block that sits above the marker.

**This report was rewritten after the lane corrected the header mid-review.** The lane moved repeatedly
while I worked (`edd7895…` → `2eb0183f…` → `27db4ce…` → `99e3d63…`), and the six receipts were edited
twice after wave-1 scoring: `f5c845b` ("receipt header semantics corrected per RevReceipts (true
counter-command sha; controls stamped at base 21e6a7f)") and `27db4ce` ("id map regenerated post-landing
(S874+) + R71-M14 anchor-base note" — message silent about the receipts). Section *History* records what
wave 1 landed and what was fixed; every other section is verified at

```
HEAD = 99e3d63a1fded6e47a015708e516570cfedfb638
```

The six receipts are untouched since `27db4ce` (`git log 27db4ce..99e3d63 -- reports/round-70/telemetry/`
is empty); every verdict below was re-run at `99e3d63`.

Base the receipts name: `453676a2363c97e158cb112c9588906564d95a21` (round-70 records, tree
`7153d0d12f457edc5ee358b9e7b59adc0da1d104`). Declared base: `21e6a7f3fb63e717f2021c46a172e396c4759a7c`
(tree `ece8c7cd25b64bb8cbbc590cd750ecc07790c40e`). Re-stamp carrier: `27db4ce`.
Tooling: none installed (git + python3 sufficed; pacman paused per operator directive).

## Verdict summary (current bytes)

| # | check | verdict | evidence |
|---|---|---|---|
| V1 | below-marker bytes == original bytes at `453676a2` (the assigned question) | **PASS 6/6** | byte-identical after both header rewrites; `diff` exit 0; sha256 equal |
| V2 | line-1 digest is re-derivable by a re-opener | **PASS 6/6** (was FAIL) | = `sha256(counting_command)` of the claim in `reports/round-70/claims.json`; re-derived here |
| V3 | stamped/evaluated/measured revision is where the legs actually run | **PASS 6/6** (was FAIL 3/6) | controls re-stamped at base `21e6a7f`, legs reproduce there; measures reproduce at `453676a2` |
| V4 | criterion-19 carrier parentage (`--topo`) | **FAIL 6/6 — open** | carrier `27db4ce`, parent `e1d0d44d`, stamped `21e6a7f`/`453676a2` |
| V5 | criterion-19 `--lands` leg | **FAIL 6/6 — structurally unsatisfiable for a retrospective re-stamp** | `unreadable` (controls) / `missing_headers` (measures) |
| V6 | the landed counter can detect V2–V5 | **FAIL — open** | `accept-ca.py:76-84` is a substring grep; `ACCEPT-CA-71: PASS` through both mutations |
| V7 | marker-set completeness | **PASS** | exactly the six round-70 files carry the marker/header; round-71's own re-stamps use the same marker append-only (see V7 for the contrast) |
| V8 | the six are still the files the round-70 claims describe, and the record of the repair matches the bytes | **FAIL — open** | `corrections-r70.md` V70-1 row still describes the `1d1b432` header form; the `27db4ce` rewrite is undisclosed |
| V9 | same class outside round 70: does a header's counter-sha attest a counter that existed at its stamp? | **FAIL** (`round-71/telemetry/measures-ca.txt`) | records `1ce25fb9`, but `accept-ca.py` at `64da9e14` is `f706aacd`; the SHA leg cannot see it |

## V1 — byte preservation: PASS 6/6 (assigned question, exact commands)

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
for f in controls-ca controls-d controls-o measures-ca measures-d measures-o; do
  p=reports/round-70/telemetry/$f.txt
  git show 453676a2:$p > /tmp/orig-$f.txt
  tail -n +9 $p > /tmp/below-$f.txt        # marker is line 8 in every file
  diff -q /tmp/orig-$f.txt /tmp/below-$f.txt; echo "diff_exit=$?"
  sha256sum /tmp/orig-$f.txt /tmp/below-$f.txt
done
```

`diff_exit=0` for all six, before and after the header corrections; sha256 pairs agree:

| receipt | original bytes | sha256 (original == below-marker) |
|---|---|---|
| controls-ca | 342 | `ab73517ed465329a98f4c7ba1708e9536fbac13e60c53b484b04d8f10490eaf1` |
| controls-d | 1284 | `be192e81c7a7d1ca6e37e9e6fbed5b803c6f3183136ef9d317cbd8c57567bd14` |
| controls-o | 407 | `60772272fce24e139bf5851fa871beafece8e4bf1ff6afe24c11fc6f73bf32eb` |
| measures-ca | 132 | `6f40598b2ab66794bd2efc554c5a29319bac02e0eb6d55374ed3e3e226b3a57d` |
| measures-d | 1536 | `e19c6158098adbe027abcfbd86b22bccfaaccaf792f8af0eae54bd4acee8af71` |
| measures-o | 207 | `b7790bec03e5585bfdb0746b7b5ae8758d977495de31117ba1cdf7d0c8f03b8a` |

Strict composition, re-run at HEAD: `sha256(header_block_through_marker + original) == sha256(file)` is
`True` for all six; header block is now **497 B** (556 B before `f5c845b`/`27db4ce`); `added == 497`;
originals end with a newline; the marker occurs exactly once per file at line 8.
`census-start.txt` (last touched `6cb51a4`) and `census-end.txt` (`acc2d61`) carry neither header nor
marker — correct, V70-1 names exactly the six `measures-*`/`controls-*` files.

## V2 — line-1 digest: fixed at `f5c845b`, verified here; one caveat

Wave 1 landed `# counter sha256 (self): <64hex>  (digest of the preserved original bytes below the
marker)` with values that matched nothing (see History). `f5c845b` replaced them with the sha256 of the
claim's frozen `counting_command`; `27db4ce` then removed the parenthetical. Current values, re-derived
here with the command a re-opener can run:

```
python3 -c "import json,hashlib; c={x['id']:x for x in json.load(open('reports/round-70/claims.json'))['claims']}; \
print({k: hashlib.sha256(v['counting_command'].encode()).hexdigest() for k,v in c.items()})"
# Ca e391f8869f9af15aa18198c2ab550f86529dde0884d91d06a2fe68bcb40bd945
# D  2d157c19ce458646e52369edeaab88796f983171126e5666a08f958874b167ae
# O  b0555dcb5c236f5f06e814cb354974ed2da08c505c58e6f5c74de045b30cdea0
```

`controls-ca`/`measures-ca` carry the Ca value, `controls-d`/`measures-d` the D value, `controls-o`/
`measures-o` the O value — all six match, both raw and stripped forms of the command string.

Caveat (finding F-A, low): the field's object is now *undocumented inside the file* — `27db4ce` deleted
the only sentence that said what the digest hashes. `f5c845b` had written "(round-70 claim Ca
counting_command sha)"; the current line 1 is a bare 64-hex. Two consequences: (i) the lane's declared
semantics for this field are `sha256(counter)` (`corpus/QUALITY.md:59`, `tools/check-receipt-seq.py:28`,
round-65 precedent, and the round-71 receipts which carry true counter shas), so a reader who applies the
lane's own definition gets a mismatch on 6/6; (ii) round 70 has no counter file at all
(`git ls-tree -r --name-only 453676a2 -- reports/round-70 | grep accept-` is empty), so the honest
alternatives were to omit the line (criterion 19: the counter-sha leg is *skipped, not failed*, when the
line is absent) or to keep the self-description. Recommend restoring the parenthetical rather than
removing it.

## V3 — evaluation site: fixed at `f5c845b`, verified by re-execution

Current headers: `controls-{o,ca,d}` stamp `stamped == evaluated == measured == 21e6a7f` with tree
`ece8c7cd…`; `measures-{o,ca,d}` keep `453676a2` with tree `7153d0d1…` (unchanged by both corrections).
Re-executed in a fresh clone (a `git archive` extraction is **not** usable for the `accept-d --selftest`
leg — outside a git repo it prints a misleading `1/2`):

```
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/klane
cd /tmp/klane && git checkout -q 21e6a7f     # and separately: git checkout -q 453676a2
```

| receipt | recorded body | at its stamped revision | reproduces? |
|---|---|---|---|
| controls-ca | `0` / `exists=1` / `0` | `0` / `exists=1` / `0` @ `21e6a7f` | **YES** (was NO @ `453676a2`: `10`/`exists=0`/`1`) |
| controls-d | `SELFTEST: 7/7` | `SELFTEST: 7/7` @ `21e6a7f` | **YES** (was NO: `10/10` @ `453676a2`) |
| controls-o | `0` / `36` / `SELFTEST: 1/2 exit=1` | same @ `21e6a7f` | **YES** (was NO: `36`/`36`/`2/2 exit=0`) |
| measures-ca | `10` / `0` / `1` | same @ `453676a2` | YES |
| measures-d | `SELFTEST: 10/10` + `ACCEPT-O-69: PASS legs=7/7` | identical (all 7 LEG lines) @ `453676a2` | YES |
| measures-o | `36` / `36` / `SELFTEST: 2/2 exit=0` | same @ `453676a2` | YES |

Leg commands were copied verbatim from the preserved bodies (registry `grep -cE` + `find … | wc -l` +
`accept-d --selftest`; `check-supersession-settlement.py --selftest`; `reports/round-69/accept-o.py
--root .`; the `awk|sort -u|wc -l` trio). Default header mode is green:
`python3 -B tools/check-receipt-seq.py --root . <six>` → `RECEIPT-SEQ: PASS` (exit 0), including the tree
leg (`ece8c7cd` = `rev-parse 21e6a7f^{tree}`, `7153d0d1` = `rev-parse 453676a2^{tree}`).

## V4 — `--topo`: FAIL 6/6 (open)

```
python3 -B tools/check-receipt-seq.py --root . --topo \
  reports/round-70/telemetry/{controls,measures}-{o,ca,d}.txt
→ TOPO-… FAIL carrier=27db4ce8 parent=e1d0d44d stamped=21e6a7f3   (controls ×3)
→ TOPO-… FAIL carrier=27db4ce8 parent=e1d0d44d stamped=453676a2   (measures ×3)
→ RECEIPT-SEQ: FAIL
```

The leg is satisfiable in general — the lane's own round-71 `measures-d` PASSes right now (carrier
`3764c2d`, parent `1d1b432` = stamped), and the current lane-wide census is 18 PASS / 10 FAIL over the 28
header-carrying receipts. It is also *unstable*: `round-71/telemetry/measures-ca.txt` PASSed at `27db4ce`
(carrier `7179d6d`, parent `64da9e1` = stamped) and FAILs again at `99e3d63`, because a later commit
touched the file and the carrier moved off the stamped revision. Any subsequent edit re-breaks the leg.
But it is **unsatisfiable for these six as configured**: the carrier rule is
"the commit that carries a receipt has the stamped revision as its parent", and (i) the two truthful stamps
are different revisions (`21e6a7f` for the controls, `453676a2` for the measures), so no single carrier
commit can be a direct child of both; (ii) both revisions are far in the past on a linear `main`
(`453676a2` is 7 commits behind `1d1b432`, `21e6a7f` is round-70's
declaration), so a child commit carrying the re-stamp cannot exist without rewriting history. This is a
criterion-design consequence of V70-1's "re-stamp in place", not a fresh seat error: `QUALITY.md:59`
itself says "no header is ever written onto its original bytes" for pre-protocol receipts while
criterion 17 (`QUALITY.md:55`) prescribes exactly that marker-preserved re-stamp. The two clauses
contradict, and `--topo`/`--lands` grade the branch that the repair was ordered not to take.
**Remedy (either):** (a) record these six as retrospective re-stamps and grade them by byte preservation +
truthful stamp (V1–V3) instead of carrier parentage, amending criterion 19's exemption text; or (b) drop
the header and revert to criterion 19's `no_stamp_header` route for pre-protocol receipts.

## V5 — `--lands`: FAIL 6/6, same structural cause

```
python3 -B tools/check-receipt-seq.py --root . --lands 21e6a7f… reports/round-70/telemetry/controls-ca.txt
→ SEQ-… FAIL unreadable
python3 -B tools/check-receipt-seq.py --root . --lands 453676a2… reports/round-70/telemetry/measures-o.txt
→ SEQ-… FAIL missing_headers=['stamped','evaluated','measured','tree']
```

A receipt's header exists only in the commit that writes it, so at its (historical, truthful) stamped
revision the file cannot carry the *current* header. Census at HEAD: 28 receipts carry a `# stamped
revision:` line and **0** have their current bytes at their stamped revision
(`git show <stamped>:<file> | cmp -s - <file>` → no match, 28/28). Two round-71 receipts have *some*
header there (`measures-c.txt`, `measures-ca.txt` at `64da9e14`), but it is an earlier re-stamp: reading
`measures-ca.txt` in `--lands 64da9e14` mode grades text whose own stamp is `1d1b432`
(`SEQ-… PASS stamped=1d1b4325`), i.e. a different receipt than the one on disk. The tool's selftest
asserts the intended model (`lands-absent-is-fail`: "receipt not in lands tree must FAIL not skip").
Criterion 19 nevertheless states the check as "`--lands <40hex> <receipt> [<counter>]` exits 0" —
unsatisfiable for any receipt that was edited after its stamp. Route: criterion text / instrument (grade
the *counter* at lands, the *receipt* by V1–V4), not the six files.

*Census note (resolves a peer discrepancy):* the peer seat counted 27 header-carrying receipts; I count
**28** at HEAD by both `rg -l '^# stamped revision: [0-9a-f]{40}' reports/` and a shell loop
(`loose=28 strict=28`, no malformed stamp line). The peer's 27 is a snapshot taken before the round-71
`measures-c` re-stamp/commit landed during wave 2; the difference does not change either conclusion.

## V6 — the landed Ca counter is blind to all of this (open)

`reports/round-71/accept-ca.py:76-84`:

```
has_all     = all(line in data for line in HDR_LINES)     # substring presence only
marker_ok   = MARKER in data
below       = data.split(MARKER, 1)[1]
first       = below.strip().splitlines()[0].strip()
original_ok = first.startswith("#") and len(first) > 3     # ANY comment counts as "original bytes"
```

`python3 -B reports/round-71/accept-ca.py --root .` prints `ACCEPT-CA-71: PASS` (exit 0) with
`V70-1 … True` for all six **after both header rewrites**, including the wave-1 form whose digest matched
nothing. The leg never hashes the preserved bytes, never compares a digest, never checks
`evaluated == measured == stamped` against the body, and never calls `--topo`. This is exactly the hole
wave 1's critic predicted (`.ufo/waves/round-71/w1/CritClaimSizing.md` §2.4) and the mutation seat's
stronger L1–L4 design (`MutReceiptHeader.md` §2) did not survive into the landed counter.

Provenance makes the green weaker still: `reports/round-71/accept-ca.py` does not exist at `8c203bd` and
first appears in `1d1b432` — the same commit that lands every Ca artefact (the six re-stamps, the S860
cell, the round-70 quote trim, the SCORECARD row, `corpus/lessons/round-71.md`,
`reports/round-71/telemetry/quarantine-verdicts.md`, `reports/round-71/corrections-r70.md`). So the counter
arrived *with* its data, and no pre-data freeze of it exists to compare against. (Claim C's data commits are
separate and touch no Ca artefact: `498db73` edits `corpus/README.md`, `corpus/SOURCES.md`, the dance entry
and `accept-c.py`; `8c203bd` edits `corpus/SOURCES.md` only.)
The peer seat measured 8 of 12 deliberately broken inputs still passing it (`RevCounterCa.md`; not re-run by
this seat).
Recommended minimum: per file, `sha256(below_marker) == sha256(git show <stamped>:<path>)`, the declared
digest re-derived from its stated object, `evaluated == measured == stamped`, and one `--topo` call.

## V7 — marker-set completeness: PASS (with a contrast worth recording)

`grep -c '^# original bytes preserved below$' reports/round-70/telemetry/*.txt` → 1 for the six, 0 for
`census-start.txt`/`census-end.txt`; `grep -l '^# stamped revision' reports/round-70/telemetry/*.txt` →
exactly the same six. No seventh round-70 receipt was re-stamped.

Two files **outside** round 70 carry the marker: `reports/round-71/telemetry/measures-c.txt` and
`measures-ca.txt`. They are the lane's own append-only re-stamps — each keeps the *previous header* below
the marker (e.g. `measures-ca.txt` line 9 onward is the earlier header with counter sha `f706aacd…`), which
is the pattern that makes a re-stamp auditable inside the file. The round-70 corrections did not follow it:
`f5c845b` and `27db4ce` rewrote lines 1–6 in place, so wave-1's header form — the bytes wave-2 seats
scored — is no longer recoverable from the file, only from `git show 1d1b432:<path>`. That is finding F-B
below.

## V8 — the repair's own record no longer matches the bytes (open)

`reports/round-71/corrections-r70.md:9` (V70-1 row) still describes the header as landed at `1d1b432`
("each file now opens with the six-line 17/19 header … original bytes preserved below
`# original bytes preserved below`") and says "re-stamped in place, round 71". It records neither
`f5c845b` (semantics corrected, stamps changed for the three controls) nor `27db4ce` (self-description
removed). `grep -rnE 'f5c845b|counting_command sha|RevReceipts' reports/round-71/corrections-r70.md
corpus/lessons/round-71.md reports/round-71/claims.json` returns nothing. Two defects:

* **F-B (medium) — undisclosed, non-append-only evidence mutation.** `27db4ce`'s message is "id map
  regenerated post-landing (S874+) + R71-M14 anchor-base note", yet it edits all six receipts (2 lines
  each: the line-1 parenthetical removed); `f5c845b` rewrote lines 1–6 of all six. Both rewrote the header
  **in place** instead of appending it below the marker, which is how the lane re-stamps elsewhere in the
  same round (`round-71/telemetry/measures-c.txt`/`measures-ca.txt` keep the previous header below
  `# original bytes preserved below`). Consequence: the header form wave-2 seats scored at `1d1b432` is no
  longer in the file. Receipt bytes are the artefact whose whole point is being citable; a commit that
  changes them without saying so is the same class as round-71's F7 (`accept-c.py` edited after scoring,
  flagged by `CritGaming1.md`).
* **F-C (medium) — stale record.** The V70-1 row must name the current header form (true stamp for
  controls at `21e6a7f`; digest = claim `counting_command` sha) and the two correction commits, or the
  next re-opener grades the wrong bytes. Note the frozen `reports/round-71/claims.json` Ca `after` text
  ("all six round-70 receipts carry the six-line 17/19 header … with original bytes preserved below a
  marker") is still satisfied — the corrections changed *values*, not the shape — so this is a record
  defect, not a claim failure.

## V9 — `round-71/telemetry/measures-ca.txt` attests a counter that did not exist at its stamp (open)

Cross-check requested by the peer seat; verified independently here. The file's current header pairs a
counter sha with a stamp that cannot both be true:

```
# counter sha256 (self): 1ce25fb9ade45c263ba8ddec32f4fb73492ee5f0e82ef2e501bfa975fdcd2517
# stamped revision: 64da9e14e5fa512c7f9c1d7695f48b6d34009b47
...
# original bytes preserved below
# counter sha256 (self): f706aacd001ee5448ef9f32f8dc2d5bdd90839e8f3811311819fe3791fee9a3e   ← same stamp
# stamped revision: 64da9e14e5fa512c7f9c1d7695f48b6d34009b47
```

`accept-ca.py` hashes to `f706aacd…` **at** `64da9e14`; `1ce25fb9…` first exists at `57e0a72`, a
descendant of `64da9e14`:

```
for rev in $(git log --format='%h' -- reports/round-71/accept-ca.py); do
  echo "$rev $(git show $rev:reports/round-71/accept-ca.py | sha256sum | cut -c1-12)"; done
# 57e0a72 1ce25fb9ade4   ← "quarantine table re-derivation … append-only receipt re-stamps"
# 75d1675 f706aacd001e   ← "post-filing hardening — accept-ca.py slice/id …"
# 1d1b432 3f3f63fc628a   ← "records — Ca repairs V70-1..5 …"
```

The file's own preserved previous header (line 9) records `f706aacd…` at the same stamp, so the
inconsistency is visible inside the artefact: the append-only re-stamp at `57e0a72` updated the counter sha
to the current counter without moving the stamp.

Why no leg catches it (this is the instrument defect, not a seat slip):

```
python3 -B tools/check-receipt-seq.py --root . reports/round-71/telemetry/measures-ca.txt reports/round-71/accept-ca.py
→ SHA-… PASS recorded=1ce25fb9 actual=1ce25fb9        (both sides read "now")
python3 -B tools/check-receipt-seq.py --root . --lands 64da9e14… reports/round-71/telemetry/measures-ca.txt reports/round-71/accept-ca.py
→ SHA-… FAIL recorded=3f3f63fc actual=1ce25fb9        (lands-receipt vs worktree counter)
```

Neither mode reads the counter at the stamped revision (`check_counter_sha`,
`tools/check-receipt-seq.py:160`, hashes `read_worktree(counter)` and falls back to `read_rev("main",
counter)` — never the stamped or lands revision), so a header written from a *later* counter revision
passes, and a correctly-stamped receipt whose counter was later edited fails. Same class as the wave-1
round-70 digests (V2 history): a field true of "now" while false of "then". Sibling receipts are
consistent — `measures-c` (counter `80b4ca09…` = `accept-c.py` at `64da9e14`) and `measures-d`
(`459cfa9d…` = `accept-d.py` at `1d1b432`) both check out.

**Remedy (corrected).** My first proposal — read the counter at the stamp and *fall back* to the worktree
when it is absent — is wrong, and the peer seat caught it: the fallback reopens the same hole whenever the
counter does not exist at the stamped revision. Reproduced in a scratch clone at `99e3d63` with
`telemetry/fx-absent.txt` (stamped `8c203bd`, where `reports/round-71/accept-ca.py` does not exist, tree
`ffb5c549…` correct, counter sha = today's `1ce25fb9…`):

```
current tool      → SHA-… PASS recorded=1ce25fb9 actual=1ce25fb9
stamp+fallback    → SHA-… PASS recorded=1ce25fb9 actual=1ce25fb9     (my earlier variant: still blind)
stamp-only strict → SHA-… FAIL counter_absent_at_stamp:reports/round-71/accept-ca.py
```

The correct route is **stamp-only**: resolve the counter at `h["stamped"]` (in `--lands` mode at `<lands>`)
and FAIL with `counter_absent_at_stamp` when it is not there — no worktree or `main` fallback. Verified in a
scratch copy (`/tmp/crs-strict.py`, `blob = read_rev(root, h["stamped"], cpath)` then
`seq.leg(…, False, f"counter_absent_at_stamp:{cpath}")`):

```
measures-ca → SHA-… FAIL recorded=1ce25fb9 actual=f706aacd     ← V9 defect visible
measures-c  → SHA-… PASS recorded=80b4ca09 actual=80b4ca09     ← true positive kept
measures-d  → SHA-… PASS recorded=459cfa9d actual=459cfa9d
the six round-70 receipts, unpaired → RECEIPT-SEQ: PASS        ← sha leg still skipped, per criterion 19
--selftest → SELFTEST: 14/14                                    (unchanged)
```

The unchanged 14/14 is the gap: **no fixture covers either failure mode**, so the fix can regress
silently. Route it with two fixtures: (a) counter written at lands, receipt stamped at lands, counter edited
in a later commit → must print `SHA-… FAIL` against the stamped blob; (b) counter absent at the stamp while
the recorded sha equals the current counter → must print `SHA-… FAIL counter_absent_at_stamp`. The lane was
not modified: both patched tools are `/tmp` copies run with `--root .`.

## History — what wave 1 landed, and what was fixed (for the record)

At `1d1b432` (the form wave-2 review began on, and the form `f5c845b`'s message responds to):

* line 1 read `# counter sha256 (self): <64hex>  (digest of the preserved original bytes below the
  marker)`; the six values (`a368cc05…`, `8fefc70f…`, `fb1fa64f…`, `3722a4a6…`, `03cda056…`,
  `eff10b1b…`) matched neither the preserved bytes nor any of 29 tested constructions, nor any committed
  file body (scanned 6917 blobs at HEAD, 6828 at `453676a2` and `acc2d614`), nor any counter.
* all six stamped `453676a2`; the three controls' legs reproduce at base `21e6a7f`, not there.
* `--topo` FAILed 6/6 with carrier `1d1b432`, parent `8c203bd` (chain `453676a2 → b94a543 → 825b78a →
  b694afd → 65ff151 → 498db73 → 8c203bd → 1d1b432`).
* `accept-ca.py` was absent at `8c203bd` and first present at `1d1b432`; its `--lands` flag is parsed and
  never read (`reports/round-71/accept-ca.py:64`, help text "printed, not graded"); it never invokes
  `tools/check-gate-quotes.py` (0 occurrences) although the claim's predicate names that command.

`f5c845b` fixed the first two; V4/V5/V6/V8 remain as above.

## Cross-checks requested by the peer seat

* (a) **Quarantine counting command is vacuous — confirmed.** `reports/round-71/claims.json` Ca
  `counting_command` ends with
  `awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}'
  reports/round-71/telemetry/quarantine-verdicts.md`; against the landed 21-row table it prints `0`
  (rows begin with `|`, so `$1` is empty and `$2` is untrimmed). A trimmed variant
  (`$2 ~ /^S[0-9]+$/` on `$2`, verdict on `$3`) prints `21`. Declared target 21 → the declared command
  cannot reach it.
* (b) **`accept-ca.py` provenance — confirmed** as in History above (absent at `8c203bd`, present at
  `1d1b432`; `--lands` never read; `check-gate-quotes` never invoked). Its `ACCEPT-CA-71: PASS` is real on
  the current bytes but rests on substring greps.

## Residual risk and verification gaps

* The lane is live: this review saw five HEADs (`baf3b6a6`, `edd7895`, `2eb0183f`, `27db4ce`, `99e3d63`)
  and two receipt rewrites. All numbers above are pinned to `99e3d63`; re-check
  `git log 1d1b432..HEAD -- reports/round-70/telemetry/` before citing.
* Provenance of the original (wave-1) digests is unknowable now that they are overwritten; the only
  construction consistent with the evidence is a worktree state never committed (round 70 measured "at
  lane `6cb51a4`+landed edits"). That is what made them unfalsifiable.
* `# worktree dirty (tracked): False` is unverifiable as a historical fact for either run (no recorded
  dirty-file list); it is consistent with the clean clones I used.
* V3 rests on leg re-execution in a clean clone; `accept-d --selftest` is git-sensitive (see above).
* No lane source was modified by this seat; only this report was written.
