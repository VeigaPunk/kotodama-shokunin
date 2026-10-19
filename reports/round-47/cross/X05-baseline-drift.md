# X05 — baseline-drift critic (round 47)

- Seat: X05 | role: critic | claim: cross | date 2026-10-19
- Out path: `reports/round-47/cross/X05-baseline-drift.md` (this file)
- Declared baseline: `6e9a30d` — `reports/round-47/claims.json:7`,
  `reports/round-47/telemetry/dispatch-declared.json:11`
- Measurement window: `2026-10-19T17:47Z`–`2026-10-19T17:57Z` (UTC);
  HEAD and the round's contract digests re-checked at `2026-10-19T17:56:44Z`
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; read-only
  git commands plus read-only runs of the r44 scratch prototype. No commit,
  no in-tree round runner, no corpus write.

**Verdict: PASS on baseline identity and digest pinning. No commit drift, no
digest drift, and none of the three r47 `before` premises is contradicted at
`6e9a30d`. The r43 claims.json drift defect does not recur. One open
provenance observation (`OBS-1`: an untracked r46 review artifact is outside
the baseline commit) has no effect on C, O, or Ca.**

## 0. What this seat checked

1. That the declared `baseline_commit` resolves unambiguously and equals the
   actual HEAD at declaration, with no commits or ref rewinds after it.
2. That the round's contract files match the digests pinned in
   `telemetry/dispatch-declared.json` (the r43 drift-defect class).
3. That each claim's asserted `before` is true **at the baseline tree** — not
   merely in the worktree — using `git ls-tree`/`git show`/`git grep` at
   `6e9a30d`, and where the claim cites earlier evidence, that the cited bytes
   are unchanged between the scout commit and this baseline.
4. That no filed bytes or corpus paths were modified in the worktree after the
   baseline, and that the only untracked paths are the round's own directories.

## 1. Baseline identity — PASS

```console
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git rev-parse 6e9a30d
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git rev-parse --disambiguate=6e9a30d | wc -l
1
$ git rev-list --count 6e9a30d..HEAD
0
$ git show -s --format='%H%n%ci%n%s' 6e9a30d
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
2026-10-19 14:46:42 -0300
round-46: loop-1 retrospective — 9 admitted / 4 honest-stops / 1 skipped (argon); defects + provider amendments carried to loop 2
```

- Commit time is `17:46:42Z`; `claims.json` declares `declared_at_utc
  2026-10-19T17:46:52Z` (`claims.json:6`), ten seconds later. With zero
  commits after `6e9a30d`, an unbroken reflog, and no ref rewinds, HEAD was
  `6e9a30d` at the declared instant.
- `git reflog --date=iso -12` is linear from `6e9a30d` back through
  `acd37c2`, `1dfb87f`, `c9f4eaa`, `7ceff59`, … with no reset, amend, or
  checkout row between the baseline and this audit.
- The baseline commit itself adds **one file only**:
  `reports/round-46/loop-1-retrospective.md | 60 +++++++++` (`git show --stat
  6e9a30d`). It does not touch `corpus/`, `tools/`, `corpus/README.md`, or
  `reports/round-28/readme/sweep.py`.
- No tags point at HEAD (`git tag --points-at HEAD` → empty).
- Six unreachable commits exist in the object store, all stash/WIP entries
  dated **2026-10-18**, i.e. before this round's baseline; none is on the ref
  chain and none carries post-baseline work.

**Worktree state (same measurement window):**

```console
$ git status --porcelain=v1
?? reports/round-46/review/
?? reports/round-47/
$ git diff --stat        # empty
$ git diff --cached --stat   # empty
```

No tracked file is modified or staged. The two untracked paths are the r46
review (see `OBS-1`) and the in-flight round-47 tree, both outside the
baseline commit by construction.

## 2. Digest pin audit — PASS (the r43 defect class does not recur)

`telemetry/dispatch-declared.json` is the digest anchor for the contract
because `reports/round-47/` is not in the baseline commit (`git ls-tree
6e9a30d reports/round-47` → 0 files). The r43 round is the defect precedent:
its declared pin named different content than the live file after provider
redirects edited the claim text.

| round | claims declared → live | match | targets declared → live | match |
|---|---|---|---|---|
| 43 | `beda7644…` / 6353 B → `9662e2bd…` / 6546 B | **NO** | `44d1f7ce…` → `44d1f7ce…` | yes |
| 44 | `5bd54b71…` → `5bd54b71…` | yes | `1f73f172…` → `1f73f172…` | yes |
| 46 | `7aacf5b1…` → `7aacf5b1…` | yes | `dc6293c1…` → `dc6293c1…` | yes |
| **47** | **`7eb16979…` / 6113 B → `7eb16979…` / 6113 B** | **yes** | **`d60e5572…` / 18755 B → `d60e5572…`** | **yes** |

r43's defect, reproduced from its filed bytes:

```console
$ # r43 dispatch-declared.json:14
"reports/round-43/claims.json": {"sha256": "beda7644…", "bytes": 6353}
$ sha256sum reports/round-43/claims.json; wc -c < reports/round-43/claims.json
9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b  reports/round-43/claims.json
6546
```

The r43 closing snapshot records the same finding and re-pins the live digest
append-only: `reports/round-43/telemetry/availability-close-43.json:18`
("digest drift vs dispatch-declared.json's beda7644…/6353B … the closing
snapshot re-pins the live digest 9662e2bd… as the executed contract").

At r47 the declared pin and the live bytes agree at declaration, at first
audit, and at the final re-check (`17:56:44Z`):

```console
$ sha256sum reports/round-47/claims.json reports/round-47/targets.json
7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34  reports/round-47/claims.json
d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d  reports/round-47/targets.json
```

**Timing note (`OBS-2`, informational).** The file mtimes are later than the
`recorded_at_utc` that names the declaration:

```text
2026-10-19 17:47:07.820Z  reports/round-47/claims.json       (+15.8 s vs 17:46:52Z)
2026-10-19 17:48:10.806Z  reports/round-47/targets.json
2026-10-19 17:48:20.024Z  reports/round-47/telemetry/dispatch-declared.json
```

`recorded_at_utc` therefore records the declaration *intent*, not the instant
the digest was computed; the digest pin, not the timestamp, is what binds the
bytes. At r43 the same shape of lag concealed a real content mismatch; here
the pin matches the post-write bytes, so the class is closed by evidence, not
by timestamp. The round's closing snapshot should re-pin the final digests per
`AGENTS.md` ("Close what you open") — this is a normal close obligation, not a
defect found now.

## 3. Premise audit at `6e9a30d` (git tree, not worktree)

### 3.1 Claim C — coverage / cartography

Every numeric and ownership premise in `claims.json:27` is true at the
baseline tree:

```console
$ git ls-tree -r --name-only 6e9a30d corpus/knowledge | grep -c '\.md$'
223
$ git ls-tree -r --name-only 6e9a30d corpus/knowledge/culture-material | grep -c '\.md$'
25
$ git ls-tree -r --name-only 6e9a30d corpus/knowledge | grep -iE 'cartograph|mapmaking' || echo NONE
NONE
$ git grep -n -iE 'cartograph|mapmaking' 6e9a30d -- corpus/knowledge
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58:…cartographic histories…
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102:…not cartographic claims…
$ git cat-file -e 6e9a30d:corpus/knowledge/culture-material/cartography-and-mapmaking.md
fatal: path '…/cartography-and-mapmaking.md' does not exist in '6e9a30d'
```

- **0 filename owners, 0 `- topic:` owners.** The two body hits are the
  by-product mentions the r44 scout dispositioned (a lienzo source row and the
  T-O "not cartographic" calibration).
- The one filename containing "map" is not an owner:
  `corpus/knowledge/synthesis/dialect-faction-map-workflow.md:2` reads
  "Map dialect features and situational registers onto travel networks…" — a
  verb, not the cartographic register.
- **Not carried:** no prior round's `claims.json` or `targets.json` contains
  "cartograph" or "mapmaking" (`grep -l … reports/round-{1..46}/{claims,targets}.json`
  → none). The only substantive prior-round scout hit is the r44 seed itself
  (`reports/round-44/scout/K02-gap-scout.md:8,85,203`).
- **Evidence still valid at this baseline:** the corpus is byte-identical
  between the r44 scout's baseline and this round's:
  `git diff --name-only c9f4eaa 6e9a30d -- corpus/knowledge/ | wc -l` → `0`.
  The r44 K02 file itself is unchanged between its commit and `6e9a30d`
  (sha256 `a72fff27…`, baseline and worktree).
- **Proposed landing path is free** at baseline and in the worktree; no
  collision to report.
- **README prose-vector defect confirmed at baseline.** The rev-2.4 note
  (`corpus/README.md:10-11`) records the vector `25/23/25/29/24/94 →
  25/23/26/25/24/94`; the written vector sums to **217**
  (25+23+26+25+24+94), while the live counts footer
  (`corpus/README.md:544,548`) reads `Total knowledge entries: 223` /
  `(total 223 files; directory totals 25/26/25/29/24/94)` — sum **223**.
  The three rotated slots are exactly myth-symbol 23→26, culture-material
  26→25, synthesis 25→29. After the cartography landing, culture-material
  becomes 26, so the sweep-consistent rev-2.5 vector is
  `25/26/26/29/24/94` = 224. This is the arithmetic the C claim's
  `after_required` (`claims.json:28`) demands; it is verified here, not taken
  from the claim.
- Worktree == baseline for the measured paths: `find corpus/knowledge -name
  '*.md' | wc -l` → 223; `ls corpus/knowledge/culture-material/*.md | wc -l`
  → 25; `git diff --stat` empty. The read-only sweep confirms parity:
  `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`,
  `orphan_rows 0`, `footer [25,26,25,29,24,94]`, exit 0;
  `readme_sha256 7c788a1d…` matches the baseline README.

Adjacent observation (`OBS-3`, not part of claim C, no action required):
`corpus/README.md:1` and `:3` duplicate the H1. It does not affect the
rev-2.5 counts arithmetic; flagged only so the integrator is not surprised
while editing that header.

### 3.2 Claim O — operability / freshness gate

The baseline tree has **no** claims-freshness tool:

```console
$ git ls-tree -r --name-only 6e9a30d tools/harness | sort
tools/harness/basename-couples-resolver.py
tools/harness/couples-reference-extractor.py
tools/harness/packet_links.py
tools/harness/packet_uncertainty.py
tools/harness/r8_checks.py
tools/harness/receipt_guard.py
tools/harness/receipt_guard_adoption.py
tools/harness/round_runner_conformance.py
```

The r44 prototype that the claim calls "red-selftest and non-durable"
(`claims.json:40`) is present only in the ignored scratch tree, not in any
commit:

```console
$ git check-ignore -v .scratch/ca01/claims-freshness.py
.gitignore:6:.scratch/    .scratch/ca01/claims-freshness.py
$ sha256sum .scratch/ca01/claims-freshness.py
dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434
$ python3 -B .scratch/ca01/claims-freshness.py --selftest; echo exit=$?
… FAIL  grep_absent hit fails
… FAIL  seventeen checks collected (18)
selftest 17/19 FAIL
exit=1
```

Its r43 behaviour also reproduces exactly, read-only:

```console
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
[O] operability -- STALE (0/2 premises hold)
[C] coverage -- STALE (2/3 premises hold)
[Ca] calibration -- FRESH (1/1 premises hold)
REFUSE: claims O, C have a `before` already false at 7ceff59…; do not dispatch.
exit=2
```

That checks the r47 O premise as stated (red selftest, non-durable, method
proven). The evidence has a durability caveat (`OBS-5`): it lives only in
`.scratch` and is not pinned by `6e9a30d`; its sha256 is recorded above so
the check is reproducible while the scratch tree survives.

**The r43 stale premises are real at r43's own baseline `7ceff59`:**

- C's `before` (`reports/round-43/claims.json:40`) says the lithic slot is
  "named but unbuilt"; the entry exists at that baseline:
  ```console
  $ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sed -n '1,5p'
  # Stone, gem and metal symbolism — the lithic register: …
  - gap filled: the lithic/mineral register is absent from the partition and this entry fills it…
  - topic: the lithic register of a fictional culture's symbolic grammar — …
  $ git ls-tree -r --name-only 7ceff59 corpus/knowledge/myth-symbol | wc -l
  26
  $ git ls-tree -r --name-only 7ceff59 corpus/knowledge | wc -l
  223
  ```
  The count half of the premise (26/223) is true; the ownership half is false
  at the same commit. The r43 prototype's `topic_unowned` probe reports three
  owner hits, all on `mineral-stone-symbolism.md`.
- O's `before` (`reports/round-43/claims.json:27`) says "no durable instrument
  implements the r39 basename-couples policy"; a durable parser with a
  `--selftest` flag is present at `7ceff59`
  (`tools/harness/couples-reference-extractor.py:299-301`). The round's own
  record adjudicated the premise stale: `reports/round-43/op/O12-negative-proof.md:462`
  ("`claims.json:27` 'before' is stale; the r42 extractor is durable at
  HEAD") and `LOG.md:3842-3843` ("claims O and C were declared on premises
  false at baseline `7ceff59` (not re-measured before dispatch) — R01-43-12").
  `LOG.md:3828-3831` records the adjudication that minting the claim-named
  resolver "would fork the parser". The interpretive clause — whether the r42
  extractor *implements the r39 policy* — is the point the durable gate must
  encode as typed probes; for baseline-drift purposes it is enough that the
  premise "no durable instrument" is contradicted by the tree and was ruled
  stale by the round.
- Ca's `before` was true at `7ceff59`: the dispositions artifact is absent
  from that tree (`git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json`
  → exists on disk, not in commit), matching the prototype's `FRESH` verdict.

For the O negative control, the r44 premise is true at r44's baseline: the
four-class resolver is absent at `c9f4eaa` (`grep -c` → 0) and first appears
at `1dfb87f` (`git ls-tree 1dfb87f tools/harness` →
`basename-couples-resolver.py`). At r47's baseline it exists with sha256
`43ce341f…`, so the future gate must not evaluate `tools/harness` as if it
were the r44 tree; baseline evaluation via `git show` is mandatory
(`reports/round-44/review/R01-review.md:243-251`, contract clauses 1-2).

### 3.3 Claim Ca — calibration / loop-1 reconciliation

The baseline commit contains the retrospective and no loop-2 successor:

```console
$ git ls-tree -r --name-only 6e9a30d reports/round-46 | grep -iE 'queue|successor' || echo NONE
NONE
$ git ls-tree -r --name-only 6e9a30d reports | grep -i 'defect-queue'
reports/round-37/op/defect-queue.json
reports/round-40/op/defect-queue-v2.json
reports/round-43/calib/defect-queue-v2-successor-r43.json
```

The retrospective names exactly **five** carried items
(`reports/round-46/loop-1-retrospective.md:43-53`): the R01-43-12 freshness
gate (:45-46), the stale-premises pattern (:47-48), the resolver latent edge
(:49-50), the antigravity outage (:51-52), and zai exhaustion (:53). No
successor dispositioning them exists in the baseline tree, so the Ca `before`
("not yet dispositioned into the queue successor", `claims.json:53`) is true.

The parent ledger is pinned and byte-stable:
`reports/round-40/op/defect-queue-v2.json` sha256
`dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`
at `6e9a30d` and in the worktree; 38 rows, schema
`kotodama-defect-queue-v2`. The new successor must reference (not edit) this
digest, per the Ca claim's own threshold.

## 4. Drift register

| id | class | evidence | severity | effect on the three claims |
|---|---|---|---|---|
| D-1 | commit drift after declaration | `git rev-list --count 6e9a30d..HEAD` → 0; reflog linear; no tags | none | none |
| D-2 | contract digest drift | r47 declared pin == live sha for claims and targets (§2) | none | none |
| D-3 | worktree tracked-file drift | `git diff --stat` / `--cached` empty; only two untracked dirs | none | none |
| D-4 | premise drift at baseline | all `before` clauses checked in §3 | none | none |
| OBS-1 | post-baseline untracked artifact under a filed round | `reports/round-46/review/R01-review.md`: 6657 B, mtime `17:48:54.99Z` (132 s after the baseline commit), declared at `reports/round-46/targets.json:17`, **absent from `6e9a30d`**, not cited by any r47 claim | open / low | none; must not be cited as baseline evidence |
| OBS-2 | `recorded_at_utc` precedes contract file mtimes by 15.8 s | §2 timing block | info | none; digest pin binds the bytes |
| OBS-3 | duplicate H1 in `corpus/README.md:1,3` | `grep -n '^# kotodama-shokunin corpus index'` → 1, 3 | info | none; not claimed by C |
| OBS-4 | contract files are outside the baseline commit | `git ls-tree 6e9a30d reports/round-47` → 0 files | info / by design | none; dispatch-declared pin is the anchor and matches |
| OBS-5 | r44 prototype is gitignored / unpinned | `.gitignore:6`; sha `dd88d9e1…` recorded §3.2 | info | none now; premise evidence is not durable, which is the O claim's subject |

**OBS-1 detail and recommendation.** The only worktree path that appeared
after the baseline commit is the r46 reviewer's declared output. Because
round-46's commit (`6e9a30d`) contains the retrospective but not the review,
the baseline pins the round record and not this artifact. No r47 claim cites
it (the only r44-review citations in the round are `targets.json:15` K03 and
`calib/Ca02-resolver-edge.md` against `reports/round-44/review/`). Owner:
integrator. Recommendation: in the round-47 closing snapshot either pin its
sha256 as an unpinned worktree input with a `to-verify`/`could-not-evaluate`
label, or record it as an r46 hygiene carry — do **not** treat it as part of
`6e9a30d`, and do not edit it.

## 5. Verdict

- **Baseline identity:** PASS. `6e9a30d` is the unique, un-rewound HEAD at the
  declared instant and for the whole audit window.
- **Digest drift (r43 defect class):** PASS / does not recur. r47's claims and
  targets match their declared pins byte-for-byte; r43's mismatch is
  reproduced only as historical evidence for the O regression.
- **Premise drift:** PASS for C, O, Ca. C's gap remains unowned at the
  baseline; O's gate is absent and the prototype is red/non-durable; Ca's five
  loop-1 items have no successor yet. No claim rests on a worktree-only
  measurement.
- **Open:** `OBS-1` only, with no effect on the three claims. `OBS-2`–`OBS-5`
  are informational.
- **Cannot evaluate (stated, not guessed):** r47's own outputs — at this cut
  only `reports/round-47/calib/Ca02-resolver-edge.md` existed; no verdict on
  any seat's deliverable. The r46 review's provenance beyond its declared out
  path. The contents of `.scratch` after any later cleanup.

## Appendix A — digest registry (baseline `6e9a30d` unless noted)

| artifact | sha256 | note |
|---|---|---|
| `reports/round-47/claims.json` | `7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34` | == dispatch pin |
| `reports/round-47/targets.json` | `d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d` | == dispatch pin |
| `reports/round-47/telemetry/dispatch-declared.json` | `3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8` | records the pins |
| `reports/round-43/claims.json` | `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b` | r43 live; declared pin differs |
| `reports/round-44/scout/K02-gap-scout.md` | `a72fff27ee193cc12e689b5a3b485d3c0389bd4317b7810abf745ee441f335f6` | baseline == worktree |
| `reports/round-44/review/R01-review.md` | `b98e3849b281ec60b6e3ba5f6ffba3b295a3f50bfb1f3bc3deadd36c9498e067` | baseline == worktree |
| `reports/round-46/loop-1-retrospective.md` | `a8e3fabb0d6502a03371be32632003fa3772f0ad39d15280847bcefc8b2d895d` | baseline == worktree |
| `reports/round-40/op/defect-queue-v2.json` | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` | 38 rows |
| `tools/harness/basename-couples-resolver.py` | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` | baseline == worktree |
| `corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | rev 2.4 |
| `.scratch/ca01/claims-freshness.py` | `dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434` | **unpinned** (gitignored) |

## Appendix B — key commands run

```bash
git rev-parse HEAD; git rev-parse 6e9a30d; git rev-parse --disambiguate=6e9a30d | wc -l
git rev-list --count 6e9a30d..HEAD; git show -s --format='%H%n%ci%n%s' 6e9a30d
git reflog --date=iso -12; git status --porcelain=v1; git diff --stat; git diff --cached --stat
git ls-tree -r --name-only 6e9a30d corpus/knowledge | grep -c '\.md$'
git ls-tree -r --name-only 6e9a30d corpus/knowledge/culture-material | grep -c '\.md$'
git ls-tree -r --name-only 6e9a30d tools/harness | sort
git grep -n -iE 'cartograph|mapmaking' 6e9a30d -- corpus/knowledge
git diff --name-only c9f4eaa 6e9a30d -- corpus/knowledge/ | wc -l
git diff --name-status c9f4eaa 6e9a30d -- tools/
git ls-tree -r --name-only 7ceff59 corpus/knowledge/myth-symbol | wc -l
git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sed -n '1,5p'
git ls-tree -r --name-only c9f4eaa tools/harness | grep -c basename-couples-resolver
git show 6e9a30d:corpus/README.md | sha256sum; sha256sum corpus/README.md
grep -l -iE 'cartograph|mapmaking' reports/round-{1..46}/claims.json reports/round-{1..46}/targets.json
python3 -B reports/round-28/readme/sweep.py
python3 -B .scratch/ca01/claims-freshness.py --selftest
python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
# digest comparison r43/r44/r46/r47: sha256sum + declared_artifacts read via python3 -B
```

## Appendix C — citation index

- `reports/round-47/claims.json:6-7` — declared time and baseline.
- `reports/round-47/claims.json:27` — C `before` (223; cartography fresh).
- `reports/round-47/claims.json:40` — O `before` (stale premises; red prototype).
- `reports/round-47/claims.json:53` — Ca `before` (five carried items).
- `reports/round-47/telemetry/dispatch-declared.json:11,15-16` — baseline and pins.
- `reports/round-43/claims.json:6-7,27,40` — r43 baseline and the two false premises.
- `reports/round-43/telemetry/availability-close-43.json:18` — r43 re-pin.
- `reports/round-43/op/O12-negative-proof.md:462` — "stale; the r42 extractor is durable".
- `LOG.md:3828-3831,3842-3843` — fork-risk ruling and the R01-43-12 process defect.
- `reports/round-44/review/R01-review.md:212,243-251` — gate contract (baseline evaluation).
- `reports/round-44/claims.json:27,40,52` — r44 premises / negative control.
- `reports/round-44/scout/K02-gap-scout.md:8,85,112,203` — cartography seed and non-carriage.
- `reports/round-46/loop-1-retrospective.md:43-53` — five carried items.
- `reports/round-46/targets.json:17` — declared r46 review out path.
- `corpus/README.md:10-11,544,548` — prose vector vs live footer.
- `corpus/knowledge/synthesis/dialect-faction-map-workflow.md:2` — "map" as verb.
- `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1,3,5` (at `7ceff59`) — lithic owner.
- `tools/harness/couples-reference-extractor.py:299-301` (at `7ceff59`) — durable parser + selftest.
- `.gitignore:6` — `.scratch/` ignored.
