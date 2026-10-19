# A01 — scope and bleed verification (round 47, claim cross)

- Seat: `A01` | role: verifier | claim: **cross** | round 47, loop 2, position 1
- Out path: `reports/round-47/adj/A01-scope.md` (this file; the only path this seat wrote)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` == `reports/round-47/claims.json:7`
- Observation window: 2026-10-19T17:46:52Z (declaration) – 2026-10-19T18:08Z (latest cut; the wave was still in flight)
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Mission (`reports/round-47/targets.json` seat A01): *"Scope/bleed verifier: no cross-domain bleed (no canon/lore/packet surface); PROVINCE accurate; only corpus delta is the single C landing + README. Report violations."*

## 0. Verdict at this cut

| object of verification | verdict | basis |
|---|---|---|
| Cross-domain bleed (canon / lore / packet surface) | **NONE FOUND** | all 44 files under `reports/round-47/` (41 seat artifacts + contract + telemetry) scanned; every write proposal targets a lane-owned path; no canon decision, promotion, clearance or packet edit proposed (§4) |
| `PROVINCE.md` accuracy | **ACCURATE, no edit needed** | its six named partitions equal the live six dirs; its cited handoff contract exists; the round's three claims all fall inside its "Owns" clause and inside none of its "Refuses" clauses (§2) |
| Corpus delta | **EXACTLY ONE addition + README, as claimed — and not yet applied** | target absent at `6e9a30d`; 223/25 live; the only corpus paths any draft proposes are `corpus/knowledge/culture-material/cartography-and-mapmaking.md` and `corpus/README.md` (§3) |
| Filed-byte / write-surface discipline | **HOLDS for r47 seats; one pre-existing r46 anomaly** | no tracked modification; the only path written outside `reports/round-47/` since 14:46:52 local is `reports/round-46/review/R01-review.md`, an r46-declared artifact, not an r47 seat path (§6) |
| **Overall scope verdict** | **PASS (pre-landing)** | no violation to report; the post-apply half is owed and specified in §8 — do not read this as a post-landing clearance |

Two facts bound this verdict. First, this is a **parallel 64-seat build wave**: at this cut 44 files existed under `reports/round-47/` (41 seat artifacts plus the contract and telemetry), the C entry body and README edit were fenced drafts only (C01–C04 and C09 had filed), and the integrator had applied nothing (`git status --porcelain -- corpus/ tools/ examples/ .ufo/` → empty). Second, a scope verdict on *proposed* bytes is not a verdict on *applied* bytes; §8 is the re-runnable gate that converts it.

## 1. Method and measured baseline

All measurements are read-only at `6e9a30d`; no corpus, tool, README, LOG or filed-round byte was written or staged by this seat.

```console
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain=v1
?? reports/round-46/review/
?? reports/round-47/
$ git status --porcelain=v1 -- corpus/ tools/ examples/ .ufo/
(empty)
$ git rev-list --count 6e9a30d..HEAD
0
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

The live index is green and its digest matches every other seat's reading:

```console
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []
header_drift {}           totals_line 223 totals_ok True
footer_findings []        footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

Baseline digests this seat pins for the post-apply check (§8):

```text
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b  reports/round-43/claims.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  tools/harness/basename-couples-resolver.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  tools/harness/couples-reference-extractor.py
adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9  examples/handoff-packet.sample.md
751be0449edce03a54c21ed82b77f9d1f5e3faaf14ef2482c8525941e70cb95b  examples/handoff-packet.sample.yml
```

## 2. PROVINCE.md accuracy — clause by clause

`PROVINCE.md` is the lane's owned-boundary statement. Checked against the live tree and against the round's three claims.

### 2.1 Domain and "Owns"

`PROVINCE.md:3-7` names linguistic-cultural worldbuilding: conlang design, myth/symbol systems, era models, costume/material-culture terminology, naming systems. `PROVINCE.md:9-14` owns "the generative/coupling craft and its records in this repo (`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}`), this lane's own gates, source-check records, non-canon examples and reports."

```console
$ python3 - <<'PY'
import os
listed = ["linguistics","myth-symbol","culture-material","synthesis","verification","civilizations"]
live = sorted(d for d in os.listdir("corpus/knowledge") if os.path.isdir(os.path.join("corpus/knowledge",d)))
print("listed:", sorted(listed)); print("live:", live); print("equal:", sorted(listed) == live)
PY
listed: ['civilizations', 'culture-material', 'linguistics', 'myth-symbol', 'synthesis', 'verification']
live:   ['civilizations', 'culture-material', 'linguistics', 'myth-symbol', 'synthesis', 'verification']
equal: True
```

- The C landing is inside `culture-material` — an owned partition — and is drafted as reference method, not canon.
- The O deliverable `tools/harness/claims-freshness.py` is "this lane's own gate": `tools/harness/` is the lane's instrument directory (8 tracked files, `git ls-tree -r --name-only 6e9a30d tools/harness`), and `claims-freshness.py` is **absent** there and nowhere else (`find tools -iname '*freshness*'` → no output). The path is free; no collision.
- The Ca successor is a lane report under `reports/round-47/calib/` — covered by "reports".

### 2.2 "Refuses" — checked against the actual claims

| refusal (`PROVINCE.md:16-20`) | round-47 proposal that could breach it | measured |
|---|---|---|
| claiming or recording canon | C entry, Ca ledger, O tool | no draft asserts a world fact, a canon ruling or a bible write; the C entry's `- scope:` says "It decides nothing about any world … Canon recording and consistency verification belong to lore-shokunin" (`reports/round-47/cov/C04-entry-header.md:163`; same statement `cov/C03-entry-c.md:233`, `plan/P02-c-plan.md:220`) |
| real-world rights/attribution rulings | C entry's living-practice flags | the entry *routes* restricted material to `verification/real-world-inspiration-boundaries.md:6` and `myth-consistency-gate.md:34`; it issues no rights ruling (`cov/C03-entry-c.md:175-180`) |
| game mechanics | none | no draft touches mechanics |
| general source-research method | C source shelf | the shelf is the domain's own cartography literature; the entry states mechanisms and marks every external page `(to-verify)`; no method-for-other-domains claim |
| web publishing | none | no draft |
| prompt/skill craft | none | no draft touches `SKILL.md` or skills |

No "canon decision" verb appears anywhere in the round: a scan for `decides|records|establishes|sets … canon|world-bible` over all r47 `.md` returns no live assertion (§4.1).

### 2.3 Adjacent contract

`PROVINCE.md:22-25` says the handoff format is defined in `corpus/knowledge/synthesis/worldbible-integration-contract.md`. The file exists (28,421 bytes) and its own header names the interface (`:1-3`). The C entry cites it as the handoff target (`cov/C04-entry-header.md:137,159`; `cov/C03-entry-c.md:233-247`) and proposes no packet or bible write. **Accurate; no PROVINCE edit is earned by this round.**

## 3. Corpus delta — the single C landing + README, and nothing else

### 3.1 What the contract declares

`reports/round-47/claims.json:26-34` requires exactly: `corpus/knowledge/culture-material/cartography-and-mapmaking.md` landed (A, not M), total 223→224, culture-material 25→26, README rev 2.5 sweep-green 224==224 **and** the rev-2.4 prose-vector defect repaired. `claims.json:63-69` forbids corpus staging by seats and any packet/canon/closure move.

### 3.2 What the live tree shows

```console
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '.../cartography-and-mapmaking.md': No such file or directory
$ git cat-file -e 6e9a30d:corpus/knowledge/culture-material/cartography-and-mapmaking.md; echo rc=$?
fatal: path '.../cartography-and-mapmaking.md' does not exist in '6e9a30d'
rc=128
$ ls corpus/knowledge/culture-material/ | nl | sed -n '5,6p'
     5  calendar-festival-systems.md
     6  costume-semiotics.md
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|survey map|world map|graticule|theodolite)' corpus/knowledge/ | wc -l
0
```

The path is absent from the worktree, the index and the HEAD tree; the sort slot is free; the landing can only be `A`. **No collision to report.** The wider topic sweep returns 11 metaphor/verb/handoff hits (K01 §3, C05 §4, C07 §4.1 all agree); none is an owner.

### 3.3 Every corpus path any r47 artifact proposes

A path scan over all 44 files under `reports/round-47/` (`corpus|tools|examples|reports|.ufo|.scratch` prefixes, plus absolute paths) yields only these **write-target** classes:

| proposed write | artifact(s) | in scope? |
|---|---|---|
| `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (new, A) | `claims.json:28,41`; `cov/C01..C04`; `cov/W02` if filed; `plan/P01,P02`; `scout/K01,K02`; `cov/C05,C10`; `cov/V01`; `cross/X00,X05` | **yes** — the one authorized entry |
| `corpus/README.md` (M: rev 2.5 + vector repair) | `claims.json:28`; `plan/P01`; `cov/C04`; `cov/C10`; `cross/X00`; `cov/V01` | **yes** — the authorized index edit |
| `tools/harness/claims-freshness.py` (new) | `claims.json:39,41`; `plan/P01,P03`; `op/O10,O13`; `cross/X00,X05` | **yes** — lane gate, absent today |
| `reports/round-47/calib/*` demos / successor (new) | `claims.json:41,54`; `calib/Ca01..Ca05`; `plan/P01`; `cross/X00` | **yes** — round report surface |
| `reports/round-46/review/R01-review.md` | **no r47 artifact proposes it**; it already exists untracked (see §6) | **not this round's declared surface** |

No artifact proposes any second corpus entry, any edit to an existing corpus entry, any `corpus/lessons/` change, any `examples/` or `.ufo/` change, any `tools/gates/frozen/` change, or any sibling-world-bible write. The only external-path references are **reads**: `calib/Ca03-manifest-schemas.md:7,213` reads `/home/vgpnk/Projects/shokunin/MANIFEST.json` and explicitly labels it a "sibling, read-only per PROVINCE.md"; `cov/C10-sweep.md:15` records the lane root as the working directory.

### 3.4 README edit scope — defect confirmed, edit still `could-not-evaluate`

The pre-existing defect is real and exactly as the claim words it:

```console
$ python3 - <<'PY'
print("rev2.4 prose vector sum:", sum([25,23,26,25,24,94]))
print("live footer vector sum: ", sum([25,26,25,29,24,94]))
print("post-landing vector sum:", sum([25,26,26,29,24,94]))
PY
rev2.4 prose vector sum: 217
live footer vector sum:  223
post-landing vector sum: 224
$ sed -n '10,11p' corpus/README.md
`## myth-symbol/` moved 23 → **26**; the totals and footer moved 220 → **223** and
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. Re-measured with
$ grep -n '^## culture-material/ (25)$\|^Total knowledge entries: 223\.\|directory totals 25/26/25/29/24/94' corpus/README.md
234:## culture-material/ (25)
544:Total knowledge entries: 223.
548:(total 223 files; directory totals 25/26/25/29/24/94).
```

**C09's README draft is now filed** (`cov/C09-readme.md`), so the edit is assessable as a draft — still not as applied bytes. It is minimal in the intended places: it repairs the rev-2.4 token to `25/26/25/29/24/94` (223), inserts the rev-2.5 block, the header `(25)→(26)`, the one row, the totals 224 and the footer `25/26/26/29/24/94` (`cov/C09-readme.md:64-71,77-160`), and explicitly leaves the duplicate H1 untouched (`:246`). Its staged sweep is green 224==224 and it reproduces C10's blind-spot control (`:52-60,217-226`). One hunk is beyond the claim's enumerated edit: hunk 4 (`:146-159`) appends revisions 2.1–2.5 to the counts-footer history. That is not required by "row + counts + vector + rev 2.5"; it is non-destructive and factually correct, but it is an unclaimed edit unless the integrator names it. Recommended: drop hunk 4, or record it explicitly as an index-history annotation carried by rev 2.5.

**Scope boundary for the README edit (binding on C09/integrator).** The claim authorizes the rev-2.5 block, the one row, the header/totals/footer, and the rev-2.4 prose-vector correction. It does **not** authorize:

- deleting the rev-2.4 block or its dated record (P01 §4.4 says keep it; C05 §8 flags only the H1);
- repairing two *other* pre-existing defects this seat found: the duplicate H1 at `corpus/README.md:1,3` and the duplicated `revision: 2.0 —` lead at `:42,44`. Both are real (`sed -n '1,4p'` and `sed -n '42,45p'`), both are outside the claim, and both are independently flagged by C05 §8 ("outside this seat's claim") and X05 OBS-3. C09 confirms it leaves them untouched; that is the correct disposition. If any other editor repairs them, that is an **unclaimed edit** and must be named in the round record. The worse outcome is a silent repair presented as part of rev 2.5;
- writing the post-landing vector in the wrong slot. The correct vector is `25/26/26/29/24/94` (culture-material 25→26). C05 states `26/26/25/29/24/94` at `cov/C05-freshness.md:273,275,295` — sum 224, but the +1 is in the linguistics slot. C10 (`:189-193`) and S01 (`§9`, F-01) independently flag the typo. Do not copy it.

## 4. Cross-domain bleed — measured, not assumed

### 4.1 Canon / lore

Scans over every r47 `.md` (27 files at this cut):

```console
$ grep -rniE '\b(promoted|promotion|cleared|clearance|signed off|green-lit)\b' reports/round-47 --include='*.md'
# hits are: r46 history lines quoted verbatim (K01:39, X05:46), descriptions of
# MANIFEST fields (Ca03), and explicit negations ("no promotion or clearance
# verdict", P02:220, C03:272, C07:93,386). No r47 assertion promotes or clears anything.
$ grep -rniE '\b(decides?|records?|establishes?|sets?) (the )?(canon|world[- ]bible)\b|\bcanon (decision|ruling|record)\b' reports/round-47 --include='*.md'
(no output)
```

- The C entry's own scope line is the operative one: "It decides nothing about any world — no border, no charter and no survey is authorized by this file — and issues no verdict about any round, record or artifact. Canon recording and consistency verification belong to lore-shokunin; the entry ends at the handoff" (`cov/C04-entry-header.md:163`; parallel at `cov/C03-entry-c.md:233`, `cov/C01-entry-a.md:106`, `plan/P02-c-plan.md:220`).
- The worked example is declared NON-CANON twice (`cov/C03-entry-c.md:107-109,272`; `cov/C01-entry-a.md:7`), and the calibration bank routes restricted material outward rather than deciding it (`cov/C03-entry-c.md:175-180`).
- **Wording reviewed, not a bleed:** C03's build-order table has a column headed "Write this into the bible" (`cov/C03-entry-c.md:76-79`) and a sentence "A row is answered when the world bible contains the decision" (`:208`). These are instructions to the *worldbuilder* about which decisions lore must later record; they perform no lane write, name no canon fact, and sit under the entry's explicit "decides nothing" scope. I flag them as the closest-to-the-boundary phrasing in the draft, for R03/C07's judgment, not as a violation.
- No artifact proposes opening, editing or appending `corpus/knowledge/synthesis/worldbible-integration-contract.md`; it is cited as the handoff target only.

### 4.2 Packet surface

The packet surface in this repo is `examples/` (culture-d2/d3/d4, supplement), `examples/handoff-packet.sample.{md,yml}`, and the two packet tools `tools/harness/packet_links.py`, `tools/harness/packet_uncertainty.py`. None appears as a write target anywhere in r47:

```console
$ grep -rniE '(write|edit|modify|apply|stage|touch|change).{0,30}(examples/|\.ufo/|tools/gates/frozen|handoff-packet|packet_(links|uncertainty)\.py|corpus/lessons)' reports/round-47 --include='*.md' \
    | grep -viE '(never|no |not |must not|do not|without|outside|read-only|never edit)'
(no output)
$ git status --porcelain=v1 -- examples/ .ufo/ tools/gates/frozen/
(empty)
```

P01 §7.5 explicitly classes `.ufo/reports/round-47/kotodama.md` and the `MANIFEST.json` row as integrator/operator surfaces "outside this seat's write scope" (`plan/P01-plan.md:525`) — the correct disposition. No r47 artifact proposes a re-freeze of `declared-in-r7`; the token appears only in the contract's non-goal list (`claims.json:66`, `targets.json:8`).

### 4.3 Sibling repositories / world bible

Only two references leave the lane root, both reads: the fleet `MANIFEST.json` read by Ca03/Ca05 (declared read-only) and the lane root path recorded by C10. No write to a sibling, the world bible or a domain source tree is proposed. The fleet `MANIFEST.json` had no kotodama round-47 row at this cut (`python3` over 282 rows → 0 hits), consistent with the integrator not yet having closed the round.

### 4.4 One-owner / adjacency (scope half only)

The C draft does not absorb a neighbour's register: each of the seven/eight boundary rows states "owns X; this entry takes Y; does not restate X" (`cov/C01-entry-a.md:92-105`; `cov/C04-entry-header.md:114,159`). Whether the boundary claims are *correct* is C08/A02's seat; from the scope side, the proposed `- couples:` tokens are all in-repo corpus entries and none is a packet, lore or sibling path. No second corpus owner is created at the live tree.

## 5. Seat-surface integrity

`reports/round-47/targets.json` declares 64 seats with 64 unique, relative out paths, all under `reports/round-47/{scout,plan,cross,cov,op,calib,review,scribe,adj}/`; no absolute path and no `..`:

```console
seats: 64 unique outs: 64
bad outs: []
duplicate outs: []
```

At this cut 27 files existed under `reports/round-47/`; every one maps to a declared out path, with one expected exception:

```text
UNDECLARED reports/round-47/telemetry/dispatch-declared.json
```

`telemetry/dispatch-declared.json` is the declared dispatch record (round contract + telemetry per `AGENTS.md`/`REGIMEN.md`), not a seat write; it is correctly additional to the seat out map. No file appeared under another seat's declared path with a mismatched name, and no seat wrote a second file.

Two verifier artifacts deserve explicit credit for honesty rather than theater:

- `cov/V01-post-landing.md` is named "post-landing" but states **"PRE-LANDING / could-not-evaluate on live bytes"** (`:9-17`), measures the live 223 baseline, and confines its 224 proof to a `.scratch` stage. It does not claim a landing happened. This is the correct status at this cut.
- `op/O10-exit-codes.md` states the durable target is **absent** and the exit contract is `could-not-evaluate` (`:10-21`), rather than validating the scratch prototype as if it were the deliverable.

## 6. Write-surface census — what changed during the round

```console
$ find . -newermt '2026-10-19 14:46:52' -type f \
    -not -path './.git/*' -not -path './reports/round-47/*' -not -path './.scratch/*' \
    -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort
2026-10-19 14:48:54.9918670300 ./reports/round-46/review/R01-review.md
$ git status --porcelain=v1 --untracked-files=no | wc -l
0
```

That is the entire out-of-round write surface: **one untracked file in a filed round's directory**, plus the in-flight `reports/round-47/` tree. No tracked byte changed; HEAD did not move.

### OBS-A — `reports/round-46/review/R01-review.md` appeared after the round-47 declaration

| fact | measurement |
|---|---|
| path | `reports/round-46/review/R01-review.md` |
| size / mtime | 6,657 B / `2026-10-19 14:48:54.991 -0300` = **17:48:54.99Z** |
| round-47 declaration | `2026-10-19T17:46:52Z` — the file is **132 s after the baseline commit** (`6e9a30d` commit time 17:46:42Z) |
| tracked? | no — `git ls-files reports/round-46/review/` → 0; absent from `6e9a30d` |
| declared by r46? | yes — `reports/round-46/validation.json:148` says the reviewer's output "lands at review/R01-review.md" (prospective wording), and `reports/round-46/targets.json:17` declares the r46 R01 out path |
| cited by any r47 claim? | no — no `claims.json` field and no r47 artifact cites it; the only r46-review citations in r47 are against **r44** reviews (`ca02`, `O10`) |

Reading: this is the **late landing of an r46-declared artifact**, not a round-47 seat writing outside its out path. It is nonetheless a write-surface anomaly because the r46 round was already validated/closed without it and the round-47 baseline commit does not contain it. Independent corroboration: `cross/X05-baseline-drift.md` OBS-1 ("post-baseline untracked artifact under a filed round … owner integrator … do not treat it as part of `6e9a30d`, and do not edit it") and `calib/Ca05-verify.md` F5 ("a write-surface anomaly for A03 to classify").

**Disposition (not an r47 violation):** do not edit or delete it; do not cite it as baseline evidence; in the round-47 close record, either pin its sha256 as an unpinned worktree input labelled `could-not-evaluate` or carry it as an r46 hygiene item. Owner: integrator.

### OBS-B — fleet `MANIFEST.json` mtime during the window

`/home/vgpnk/Projects/shokunin/MANIFEST.json` mtime `2026-10-19 15:01:00 -0300` (18:01Z), size 310,769 B. It contains **no** kotodama round-47 row (282 rows scanned). The fleet file is shared across lanes, so the mtime is consistent with another lane's close and is not attributable to this lane from in-repo evidence. **`to-verify` by the integrator; no action for this seat.**

## 7. Findings register

| id | severity | finding | evidence | owner / action |
|---|---|---|---|---|
| S-1 | info (pass) | No canon/lore/packet bleed; every draft write target is lane-owned | §4.1–4.3 scans; `git status --porcelain -- examples/ .ufo/ tools/gates/frozen/` empty | none |
| S-2 | info (pass) | `PROVINCE.md` accurate at `6e9a30d`; no edit earned | §2; six-dir equality command | none |
| S-3 | low / open | r46 review artifact landed after the r47 baseline, untracked, in a filed round dir | §6 OBS-A; X05 OBS-1; Ca05 F5 | integrator: classify at close, do not edit |
| S-4 | info | Two pre-existing README defects outside the C claim: duplicate H1 `:1,:3`; duplicate `revision: 2.0` lead `:42,:44` | `sed -n '1,4p'`, `sed -n '42,45p'`; C05 §8; X05 OBS-3 | C09/integrator: do not repair silently; if repaired, name it as unclaimed |
| S-5 | info / `to-verify` | The C claim's literal "0 prior-round proposals" is imprecise: r44 K02 is a prior-round scout naming the gap; the operative facts are 0 prior claims, 0 drafts, 0 landings | `scout/K01-gap-recheck.md` §6.3; `cross/X00-connector.md` §7.1 | integrator/reviewers: use the registry-scoped wording in the round record |
| S-6 | info / `to-verify` | The O claim's historical parenthesis ("r43 and r44 both declared claims on stale premises") overstates r44: r44 O was true and improved; r44 C failed as a *carried candidate*, a distinct criterion | `cross/X00-connector.md` §7.2; `calib/Ca05-verify.md` F3 | integrator: do not repeat the overstatement in `LOG.md`; O's actionable clause ("no durable gate") is true |
| S-7 | info / `to-verify` | Fleet `MANIFEST.json` mtime changed during the round; no kotodama r47 row present | §6 OBS-B | integrator |
| S-8 | info (pass) | The two verifiers whose titles imply post-delivery results (`V01-post-landing`, `O10-exit-codes`) correctly report pre-landing/`could-not-evaluate`, not green | V01 `:9-17`; O10 `:10-21` | none |

No finding alleges a fabricated source, an out-of-path write by an r47 seat, a corpus overwrite, or a forbidden surface change.

## 8. Owed — post-apply scope gate (integrator, binding)

This verdict covers proposed bytes at `6e9a30d`. After the integrator applies O, C and Ca, run the following; any non-empty unexpected line is a scope failure, not a warning.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. HEAD/baseline discipline: no commits unless the round contract says so
git rev-parse --short HEAD                      # record; if advanced, record the close commit

# 2. the corpus delta must be exactly one A + one M
git status --porcelain -- corpus/
#   expect exactly:
#     M corpus/README.md
#    ?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
git diff --name-only 6e9a30d -- corpus/     # expect exactly those two paths
test "$(find corpus/knowledge -name '*.md' | wc -l)" -eq 224
test "$(ls corpus/knowledge/culture-material/*.md | wc -l)" -eq 26
git cat-file -e 6e9a30d:corpus/knowledge/culture-material/cartography-and-mapmaking.md; test $? -eq 128  # A, not M

# 3. no forbidden surface moved
git status --porcelain -- examples/ .ufo/ tools/gates/frozen/ corpus/lessons/
#   expect empty
git diff --stat 6e9a30d -- examples/ tools/harness/packet_links.py tools/harness/packet_uncertainty.py
#   expect empty (the O tool is a new file, not a packet-tool edit)
test -z "$(git diff --name-only 6e9a30d -- reports/round-1..46)"   # filed rounds untouched

# 4. the only new tool is the declared one
test -f tools/harness/claims-freshness.py
test -z "$(git status --porcelain -- tools/harness | grep -v 'claims-freshness.py')"
sha256sum tools/harness/basename-couples-resolver.py | grep 43ce341f   # witness unchanged
sha256sum reports/round-40/op/defect-queue-v2.json | grep dfc9265d      # parent queue unchanged
sha256sum reports/round-43/claims.json | grep 9662e2bd                  # r43 filed bytes unchanged

# 5. README edit is confined to the declared anchors
git diff 6e9a30d -- corpus/README.md
#   review: hunks at :5 (rev 2.5 block), :11 (rev-2.4 vector repair), :234 (header),
#   :240/241 (one new row), :544 (totals), :548 (footer). Any hunk outside these
#   anchors is an unclaimed edit (see S-4).
python3 -B reports/round-28/readme/sweep.py     # rows 224 files 224, exit 0
```

Expected post-apply scope result: **PASS** only if steps 1-5 are clean. If `corpus/` shows a third path, an existing entry is `M`, or any packet/example/frozen path moved, the scope verdict is **FAIL** regardless of the coverage or operability numbers.

## 9. Provenance

Files read (no edits): `reports/round-47/claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; `scout/K01,K02`; `plan/P01,P02,P03`; `cov/C01,C02,C03,C04,C05,C07,C10,V01`; `op/O10,O13`; `calib/Ca01,Ca02,Ca03,Ca04,Ca05`; `cross/X00,X05`; `PROVINCE.md`, `REGIMEN.md`, `corpus/QUALITY.md`, `corpus/README.md`, `reports/round-44/scout/K02-gap-scout.md`, `reports/round-43/claims.json`, `reports/round-44/claims.json`, `reports/round-46/validation.json`, `reports/round-46/targets.json`, `reports/round-46/loop-1-retrospective.md`, `reports/round-40/op/defect-queue-v2.json`, `reports/round-43/calib/defect-queue-v2-successor-r43.json`, `/home/vgpnk/Projects/shokunin/MANIFEST.json` (read-only sibling).

Commands run (selection): `git rev-parse HEAD`; `git status --porcelain`; `git status --porcelain -- corpus/ tools/ examples/ .ufo/`; `git rev-list --count 6e9a30d..HEAD`; `git cat-file -e 6e9a30d:...`; `find corpus/knowledge -name '*.md' | wc -l`; `ls corpus/knowledge/culture-material/*.md | wc -l`; `python3 -B reports/round-28/readme/sweep.py`; `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`; `sha256sum` over the digest registry; `sed -n` over README anchors; `find . -newermt` / `stat` for the write surface; the path and bleed scans in §3.3/§4; `python3` census of `targets.json`.
No `reports/round-*/run-validation.py` was executed; no git commit, push, install or network; no corpus staging; no filed byte edited.
