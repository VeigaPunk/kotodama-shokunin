# A01 — bleed/scope verification (round 43)

- Seat: **A01**, verifier, claim **cross** (`reports/round-43/targets.json:44`).
- Round 43, loop 1; baseline `7ceff59a0216a8ea21ee43262d9fc72abf770cee` (`claims.json:6`).
- Mission (verbatim, `targets.json:44`): *"Bleed/scope verifier: confirm no cross-domain bleed (no canon, no lore decision, no packet surface), PROVINCE.md still accurate, and the only corpus delta is the single C01 landing + README. Report any scope violation."*
- Observation window: **2026-10-19T16:50Z–16:56:31Z** (first cut: only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; final snapshot 16 files). Writes after that timestamp are outside this report.
- Method: read-only. `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no `reports/round-*/run-validation.py` executed; no git mutation, network, or install. Only this out file was written by this seat.

## Verdict

| scope leg | verdict | basis |
|---|---|---|
| Cross-domain bleed (canon / lore / refusals) | **PASS** | every C artifact ends at the lore handoff and carries a NON-CANON fixture; no seat output decides world truth (§2) |
| Packet surface | **PASS** | `git diff HEAD` empty; F-A02-1's packet file untouched; no artifact proposes a packet edit (§3) |
| Frozen gates / `declared-in-r7` / filed bytes | **PASS** | zero tracked modifications; no re-freeze proposed (§1, §3) |
| `PROVINCE.md` accuracy | **PASS — no edit needed** | six owned partitions present and counted; handoff contract exists; refusal list still matches (§4) |
| Corpus delta *envelope* | **PASS** | actual delta is **zero**; the only proposed corpus write is one new `myth-symbol/*.md` + `corpus/README.md` — no other corpus path is proposed (§5.1–5.2) |
| Corpus delta *validity* (claim C as declared) | **FAIL / BLOCKED** | the declared target topic is already owned by `mineral-stone-symbolism.md` (r42 C04); landing C01 duplicates or overwrites it (§5.3–5.5) |
| Round-record integrity | **1 mismatch + 1 pre-existing prose defect** | `claims.json` digest does not match its dispatch declaration; README rev 2.4 vector prose is arithmetically wrong (§7) |

**Scope violations found: none in the sense of cross-domain absorption.** One **blocking collision** exists inside the lane's own coverage claim (C), reported below with evidence; it is not a bleed, but it makes the declared C landing unsafe to apply. Two minor record/document defects are also filed.

## 1. Tree state and write surface

Final snapshot (2026-10-19T16:56:31Z), lane root:

```
$ git status --porcelain -uall | wc -l
15
$ git diff --name-only HEAD | wc -l
0
$ git ls-files --others --exclude-standard corpus/ | wc -l
0
```

All 15 untracked paths are inside `reports/round-43/` (the two contract files, telemetry, and 12 seat artifacts at cutoff). No tracked file is modified or staged.

```
$ git diff --name-only HEAD -- tools/gates/frozen reports/round-34/handoff/declared-in-r7 examples tools/harness
(empty)
```

No file under `corpus/` is staged or untracked:

```
$ git ls-files --others --exclude-standard corpus/
(empty)
$ find corpus -type f -newermt '2026-10-19 16:40:00'
(empty)
```

This is the mechanical baseline for every scope statement below: **no corpus delta existed at observation**. `reports/round-43/run-validation.py` was absent (`ls` → no such file), so no in-tree runner receipt exists; whether any process ran it elsewhere is not observable from the tree and stays `to-verify` (the ABSOLUTE rule bans it in-tree regardless).

## 2. Cross-domain bleed: canon, lore, refusals

### 2.1 The C draft explicitly hands canon off

- Spare `- topic:` ends: "Reference knowledge and method only; canon decisions belong to lore-shokunin" (`reports/round-42/cov/C01-mineral-spare.md:6`).
- Spare `- scope:`: "It records nothing about any world and decides no canon" (`:26`).
- Spare handoff: "Which stone means what in canon … is lore-shokunin's decision" (`:214`).
- Its worked example is fenced as NON-CANON (`:198`).
- The already-landed lithic entry carries the same posture: "This entry decides nothing about any world … Canon recording and consistency verification belong to lore-shokunin" (`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:19`), and "Nothing here decides what is true in any world" (`:190`).

`corpus/QUALITY.md:17-19` states the same bar ("no entry decides what is true in any world … entries end at the handoff"). The spare clears it. No seat artifact read at cutoff makes a canon, promotion, clearance, or closure decision; the C seats explicitly treat the landing as non-canon generation.

### 2.2 Refusal list still respected

`PROVINCE.md:16-20` refuses canon, real-world rights/attribution rulings, game mechanics, general source-research method, web publishing, and prompt/skill craft. No round-43 artifact proposes any of these. The spare's living-practice material is routed to `verification/real-world-inspiration-boundaries.md` rather than adjudicated (`C01-mineral-spare.md:21`, `:26`), which is the in-lane screening route, not a rights ruling.

### 2.3 No lore decision in any seat output

Checked all artifacts present at cutoff (`cov/`, `op/`, `scout/`): C01, C02, C03, C05, C06, C07, K01, K02, O02, O04, O07, O12. No file states what is true in a world; C03/C06/C07 and K02 explicitly label their verdicts as measurement, not canon. **No bleed.**

## 3. Packet surface, frozen gates, `declared-in-r7`

- The packet defect `F-A02-1-register-law-stale-era-prose` names its surface at `examples/culture-d4/components/13-register-law.yml:57` (`reports/round-40/op/defect-queue-v2.json`, row `F-A02-1…`). `git diff HEAD` over `examples/` is empty; the file is unchanged.
- `tools/harness/packet_links.py`, `tools/harness/packet_uncertainty.py`, `examples/handoff-packet.sample.{md,yml}`, and `tools/gates/fixtures/handoff-packet-check.*` are all unchanged (`git diff` empty; `git status` clean).
- No round-43 artifact proposes a packet-surface edit. The only packet mention in the seat outputs is O12's negative-proof note that frozen `run.log` files are pre-existing ignored artifacts (`op/O12-negative-proof.md:55`), not a change proposal.
- `reports/round-34/handoff/declared-in-r7` is unchanged; no artifact proposes a re-freeze. The round's non-goal "no re-freeze of declared-in-r7" is honored at the tree level.

**PASS.** The O claim's new instrument path (`tools/harness/basename-couples-resolver.py`, `op/O07-durability.md:15-18`) is lane tooling, not packet surface; adding it does not touch the packet tools or fixtures.

## 4. `PROVINCE.md` accuracy

`PROVINCE.md` is byte-unchanged (`git diff HEAD` empty; it is tracked and clean).

| PROVINCE statement | live check | verdict |
|---|---|---|
| owns `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}` (`PROVINCE.md:9-14`) | six directories exist; counts `25 / 26 / 25 / 29 / 24 / 94` = **223** | accurate |
| adjacent contract at `corpus/knowledge/synthesis/worldbible-integration-contract.md` (`:22-25`) | file exists | accurate |
| refuses canon, rights rulings, game mechanics, source-research method, web publishing, prompt craft (`:16-20`) | no r43 artifact claims any; C drafts hand canon to lore | accurate |
| writes only this standalone lane repo, its round reports, allowed L0 questions (`:27-29`) | observed writes are `reports/round-43/**` and `.scratch/**` temp only; no sibling/world-bible/source-tree write is visible from the tree | accurate; outside-repo writes not observable — `to-verify` only in the trivial sense |

The O claim's harness instrument does not expand ownership: `tools/harness/` already holds seven lane instruments, including the r42 `couples-reference-extractor.py` landed without a PROVINCE edit. r40's A02 province audit also found PROVINCE byte-accurate (LOG.md, round-40 entry). **No edit needed.**

## 5. Corpus delta and the C collision

### 5.1 Actual delta: zero

```
$ git status --porcelain -uall | grep -v '^?? reports/round-43/'
(empty)
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

### 5.2 Proposed delta envelope: one entry + README, nothing else

The only corpus write proposed by any claim is claim C's landing plus its README revision. O writes a harness tool and a `reports/round-43/calib/` census; Ca writes dispositions under `reports/round-43/calib/`. No claim proposes a `corpus/lessons/**` edit, a change to another partition, or a second corpus file. **The envelope is within scope.** The validity problem is the identity of the one entry, below.

### 5.3 Blocking finding: the declared lithic slot is already owned

My independent measurement, made at the first cut when only the contract files existed, then re-checked:

```
$ ls -1 corpus/knowledge/myth-symbol/ | grep -iE 'mineral|stone|gem|lapid|lithic'
mineral-stone-symbolism.md
$ wc -l -c corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
192 61884 corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
$ sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f
$ git log --oneline --follow -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore
$ git show --stat --oneline 7ceff59 | grep mineral
.../myth-symbol/mineral-stone-symbolism.md | 192 +++++
```

The file is the r42 C04 lithic register: its title is "Stone, gem and metal symbolism — the lithic register" (`:1`), its `- topic:` opens "the lithic register of a fictional culture's symbolic grammar — the mineral slot the register family lacks" (`:5`), and it is indexed in README rev 2.4. The r42 record says C01 (this round's spare) and C04 authored the same topic; C04 landed and C01 was routed as a spare "for a future re-scoped claim" (`reports/round-42/cov/C01-mineral-spare.md:1`; `reports/round-42/validation.json`, claim C ruling; `LOG.md:3804-3816`).

The r43 claim's `before` — "lithic slot named but unbuilt" (`claims.json:40`) — is therefore **false at the declared baseline**. The live 26/223 already includes the lithic entry. This is not a cross-domain bleed; it is a within-partition duplicate-ownership hazard, and it is exactly what the shared rule ("never overwrite an existing entry; report collisions, don't route around them", `targets.json:9`) is meant to catch.

Independent corroboration at the same HEAD (these seats landed after my first measurement; all agree):

- `scout/K02-landing-scout.md:9-19` — "COLLISION — claim C cannot land as declared"; :123-147 re-runs the absence sweep and finds the slot owned.
- `cov/C01-prepare.md:7-11` — "BLOCKED — the spare's topic is already owned on disk."
- `cov/C03-audit.md:12-29` — "Landing readiness: FAIL — blocking findings F1 and F2."
- `cov/C05-delta-receipt.md:25-33` — finding D-C1: a second owner of the same topic; the sweep has no ownership leg.
- `cov/C06-collision.md:8-18` — target filename occupied; claim's threshold unsatisfiable.
- `cov/C07-scribe.md:220-222` — the r36 spare precedent's operative condition is a *topic-free* spare; it argues against this landing.

### 5.4 Routes and why none is scope-clean without the integrator

1. **Land at `mineral-stone-symbolism.md`** — overwrites the tracked 192-line entry; violates the claim's own "no existing entry overwritten" (`claims.json:41`) and repeats r42's overwrite incident. **Rejected.**
2. **Land under an invented slug** — reaches 27/224 arithmetically but creates two owners of one register topic; the spare's own `- gap filled:`/`- verified-at:` would assert false facts at HEAD ("no entry owns stone", 220 files — `C01-mineral-spare.md:7`, `:24`). This is a route around the collision, not a re-scope. The C seats propose **four different slugs** with no author sanction: `stone-symbolism.md` (`cov/C02-readme-draft.md:67`), `stone-gem-metal-lithic-register.md` (`cov/C03-audit.md:237`), `stone-gem-metal-register.md` (`cov/C05-delta-receipt.md:44`), and `lithic-register-symbolism.md` (mentioned and not recommended, `cov/C01-prepare.md:91`). Divergent invented paths are evidence that no sanctioned landing path exists.
3. **Replace/retire the existing entry** — an overwrite/withdrawal of corpus bytes, outside every seat's authority and outside this round's non-goals. **Not proposed as a seat action; integrator decision only.**
4. **No corpus delta this round (recommended by evidence)** — leave README at rev 2.4 / 223, record claim C as blocked by collision, and carry the spare under its r42 routing until a genuinely re-scoped claim exists. This is C02's Variant B (`cov/C02-readme-draft.md:150-157`), K02's option (b) (`scout/K02-landing-scout.md:200-207`), and C05's disposition left to the integrator.

**A01 recommendation:** do not apply any C01 bytes or README rev 2.5 under the present claim. Either file the no-bump outcome, or re-scope coverage to a fresh gap-named entry with its own topic/gap/sources and a new audit. C02's conditional diff is sweep-green on a staged tree (`cov/C02-readme-draft.md:132-148`) but is explicitly conditional on an integrator re-scope (A3) and is substantively duplicate; its mechanical greenness does not cure the ownership collision.

### 5.5 What I can and cannot certify about the corpus delta

- **Can certify:** at observation, the corpus delta is zero; no file under `corpus/` was staged or modified; no claim proposes a corpus write beyond one new `myth-symbol` entry + `corpus/README.md`.
- **Cannot certify:** that "the single C01 landing + README" is a valid scope-clean delta. The target topic is occupied, so applying it would either overwrite (forbidden) or duplicate (the r42 S2 defect). The mission's phrase is satisfied only in its *envelope* sense, not in its *content* sense.

## 6. Adjacent claims-accuracy finding (not a bleed; outside the bleed verdict)

The O claim's `before` has the same staleness shape as C's:

> "no durable instrument implements the r39 basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch" (`claims.json:27`)

This is contradicted at HEAD by `tools/harness/couples-reference-extractor.py` (332 lines, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`), committed in `7ceff59`; its docstring says "Policy implemented: reports/round-39/calib/basename-couples-policy.md … Tier 1 direct / Tier 2 slash-free unique-basename fallback / ambiguous / unresolved … block extraction (D1) and the … disposition leg (D2)" (`:8-13`). Its selftest is 8/8 PASS and its census reads the wrapped field 4/4 (O12 §3, K01 §4; I independently read the source and the file's commit).

Both the O scout and the negative-proof seat agree: K01 calls the before "factually stale" and recommends hardening the existing tool rather than minting `basename-couples-resolver.py` (`scout/K01-resolver-scout.md:18-25`, `:313-317`); O12 files the same as O12-F2 (`op/O12-negative-proof.md:244-253`). O07 nevertheless chooses the new canonical path and argues the r42 bytes must not be edited (`op/O07-durability.md:15-23`, `:63-70`). That is an unresolved **operability design fork**, not a scope bleed: both routes stay inside `tools/harness/` or patch an existing lane instrument, and neither touches packet/frozen/corpus. The integrator should pick one and correct the claim's before-line; I take no position on which route.

Ca was not yet observable at my cutoff: `reports/round-43/calib/` held no files. Its declared shape (successor records under `reports/round-43/calib/`, never editing `reports/round-40/op/defect-queue-v2.json`) is scope-clean on its face; its actual dispositions are outside this seat's window and belong to Ca02.

## 7. Minor findings

### A01-M1 — `claims.json` no longer matches its declared digest (record integrity)

```
declared (telemetry/dispatch-declared.json):
  reports/round-43/claims.json  sha256 beda7644ec91d61d511af1d62a44f8b93b782c8f68a726a9a57f1a7a80d135aa  bytes 6353
live:
  reports/round-43/claims.json  6546 bytes  sha256 9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b
```

`targets.json` matches its declaration exactly (12,285 bytes, `44d1f7ce…`). So the mismatch is confined to `claims.json`: it was amended (+193 bytes) after `dispatch-declared.json` was written, and the declaration was not updated. This is not a filed-byte violation (round-43's own contract file may be amended), but the durable telemetry now cites a stale digest. **Owner: integrator.** Fix by re-declaring the digest or recording an explicit amendment; cause is `to-verify` (I cannot recover the pre-amendment bytes from the repo).

### A01-M2 — README rev 2.4 revision prose has an arithmetically wrong vector (pre-existing)

`corpus/README.md:10-11` says the vector moved `25/23/25/29/24/94 → 25/23/26/25/24/94`, which sums to **217**, not 223. The same file's totals line (`:544`) says 223 and the footer (`:546-548`) and sweep both read `25/26/25/29/24/94` = **223** (`footer_live` output above). So the footer is correct; only the revision prose is wrong (positions 2–4 are shifted: it should read `25/26/25/29/24/94`). C02's Variant A does not repair this line. If any README edit is applied this round, fix the prose in the same single-file edit; it does not change the sweep result. **Owner: C02/integrator.** (No corpus byte was edited by this seat.)

### A01-M3 — scratch artifacts are temp-only, not durable evidence

C02 (`.scratch/c02-stage/`, `.scratch/c02-readme-2.5.md`), C05 (`.scratch/c05/`), C06 (`.scratch/c06/`), K01 (`.scratch/k01/`), O12 (`.scratch/o12-*`) used the designated `TMPDIR`. The shared rules sanction `.scratch` as temp; none of it is a durable deliverable and none is under `corpus/`. O12's gate and manifest live only in `.scratch`, but its out file embeds the gate source (Appendix A) and the digests, so the evidence survives scratch cleanup. No violation; recorded for the integrator's cleanup decision.

## 8. Findings list

| id | severity | finding | owner |
|---|---|---|---|
| **A01-1** | **blocking (C)** | C01 spare's declared lithic topic is already owned by `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (r42 C04); landing duplicates or overwrites. Claim C's `before` is false at `7ceff59`. Do not apply without a re-scope or no-bump ruling. | integrator |
| A01-2 | minor (record) | `reports/round-43/claims.json` digest/bytes differ from `telemetry/dispatch-declared.json` (live `9662e2bd…`/6546 vs declared `beda7644…`/6353). | integrator |
| A01-3 | minor (docs) | `corpus/README.md:10-11` rev 2.4 prose vector sums to 217; footer/sweep say 223. Fix in any README edit. | C02 / integrator |
| A01-4 | info (O) | O claim's `before` is stale: durable policy-conformant extractor exists at `tools/harness/couples-reference-extractor.py` (r42). K01/O12 concur; O07 and K01 propose different routes. Not a bleed. | integrator / O seats |
| A01-5 | info (process) | Ca and several O seats had not filed at my cutoff; their scope status is unobserved, not passed. | integrator (re-scan) |

**No cross-domain scope violation was found.** No canon, no lore decision, no packet-surface change, no filed-byte edit, no corpus staging, no `declared-in-r7` re-freeze.

## 9. Limits / to-verify

- **Observation is a snapshot.** Seat artifacts written after 2026-10-19T16:56:31Z (notably Ca's dispositions and the remaining O drafts) are not covered. The integrator must re-run §10 before applying anything.
- **Outside-repo writes are not observable.** PROVINCE's "sibling repositories, world bible, domain source trees remain read-only" is verified only as "no such path appears in the repo's changed/untracked set"; a filesystem-wide check was not performed.
- **Semantic duplication is not fully audited.** I verified the one lithic collision with file identity, topic lines, README row, git history, and independent seat agreement. I did not sweep every proposed entry against every other partition for subtler overlaps; that is C06/C03's lane.
- **Process-level runner execution is not observable.** No `reports/round-43/run-validation.py` or validation receipt exists; I can state the in-tree execution ban is respected in the tree, not that no process ran elsewhere.
- **Ca dispositions** were not present at cutoff; their "never edits filed bytes" shape is declared in the targets (`targets.json:37`) but not yet evidenced by a filed artifact.

## 10. Re-run commands for the integrator

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                                  # expect 7ceff59… (or the round's applied HEAD)
git status --porcelain -uall                        # expect only reports/round-43/** before apply
git diff --name-only HEAD                           # expect empty before apply
ls corpus/knowledge/myth-symbol/*.md | wc -l        # 26 before any C landing
find corpus/knowledge -name '*.md' | wc -l          # 223 before
python3 -B reports/round-28/readme/sweep.py         # rows==files==223, exit 0
ls corpus/knowledge/myth-symbol/ | grep -iE 'mineral|stone|gem|lapid|lithic'   # owner present: mineral-stone-symbolism.md
git diff --name-only HEAD -- corpus/lessons tools/gates/frozen \
  reports/round-34/handoff/declared-in-r7 examples  # expect empty
sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
  # c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f at 7ceff59
sha256sum reports/round-43/claims.json reports/round-43/targets.json
  # compare against telemetry/dispatch-declared.json; A01-2 will still show if unamended
```

After any integration: re-run the sweep and re-check `git diff` against `corpus/` — the C landing, if it ever occurs under a re-scope, must be `A` (one new file) and never `M` on an existing entry.

## 11. Post-cutoff addendum (2026-10-19T16:57Z)

Five further seat artifacts landed after the body above was filed and were scanned read-only. None changes the verdicts; two independently corroborate the load-bearing findings.

- `calib/Ca01-dispositions.md:4` — "Filed-byte edits: **none**"; classes are assigned from re-measured bytes (`:18-21`), and the corpus counts re-measured (26/223) match §1 above. No corpus staging.
- `calib/Ca03-queue-update.md:9-17` — a **successor delta only**: `reports/round-40/op/defect-queue-v2.json` is left byte-identical and its parent sha256 is pinned into the new record. Scope-clean.
- `cov/C04-contract-audit.md:11-27` — contract audit **FAIL**, with N2 (topic uniqueness / one-owner rule) marked apply-blocking; Q5 canon hygiene **PASS**. Independent confirmation of A01-1.
- `cross/X00-connector.md:153-165` — "there is no non-colliding landing path"; recommends dropping C. Independent confirmation of A01-1.
- `scribe/S02-telemetry-draft.md:40-57` — independently pins the **same** `claims.json` mismatch (declared 6353 B / `beda7644…` vs live 6546 B / `9662e2bd…`) and shows no `indent=1`, `indent=2`, or compact serialization reproduces the declared bytes, so the declaration names different content. Independent confirmation of A01-2.

A second post-cutoff pass at **2026-10-19T16:58:18Z** added three more artifacts, all scope-clean:

- `op/O06-disposition-leg.md:15` — no filed byte edited; the census artifact is `reports/round-43/calib/couples-census-r43.json` (`:90`), under the round directory. No corpus write.
- `op/O10-census-artifact.md:6`, `:591` — read-only; no corpus staging, no filed-byte edit; explicitly leaves the claim-C landing decision to the integrator.
- `scribe/S01-integration-draft.md:330-333`, `:446`, `:471-472` — integration draft states coverage **unchanged** (26/223, no corpus delta), claim C failed/blocked, adjacency "no packet/canon/lore surface touched", and "Do not commit: any `corpus/**` change … any README rev 2.5 (there is no 224)". Independent confirmation of the A01-1 disposition.

Tree re-check at 2026-10-19T16:58:18Z: 26 files under `reports/round-43/`; `git diff --name-only HEAD` → 0 lines; untracked files under `corpus/` → 0; no status entry outside `reports/round-43/`. No new scope violation.

One note on §9's "Ca not observed" limit: Ca01/Ca03 are now observed and are scope-clean on their face; Ca02 (the independent re-measure), O01/O05/O08/O09/O11, R01/R02 and X01/X02 were still absent at this addendum's cutoff, so their scope status remains unobserved.
