# Q01 — final quality gate (round 47, claim cross)

- Seat: `Q01` | role: verifier (non-author) | claim: **cross** | round 47, loop 2, position 1
- Out path: `reports/round-47/cross/Q01-final-gate.md` — the only path this seat wrote
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`) == `reports/round-47/claims.json:7` (`6e9a30d`)
- Gate cut: **2026-10-19T19:18Z** (UTC, `date -u`). The refire wave was still filing; every verdict below binds to the digests in §9 and to no later revision.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Boundary: no filed byte edited; no corpus/tool/README staging; no `reports/round-*/run-validation.py` executed; no git commit/push/install/network. Assemblies and fixtures live only under `.scratch/q01/`.
- Canon: NON-CANON verification. This seat admits nothing, promotes nothing, and decides no world.

## 0. Verdict at this cut

| object | verdict | basis |
|---|---|---|
| **Baseline identity** | **PASS** | HEAD = `6e9a30d` = declared baseline; `claims.json` sha256 `7eb16979…` and `targets.json` sha256 `d60e5572…` equal the pins in `telemetry/dispatch-declared.json`; no commit or digest drift (§1, §6.1) |
| **C — coverage** | **premise GREEN; `after_required` NOT MET; landed state `could-not-evaluate`; not `improved`** | 223 entries / culture-material 25 / target absent / 0 owners. Drafts are real method, but the assembly is **790 lines vs a 221-line partition maximum**, carries **nine blocking defects B1–B9**, and the audit chain is pinned to superseded bytes. C14 is a blocking **FAIL** (§3) |
| **O — operability** | **durable deliverable ABSENT; pre-landing assembly GREEN; `after_required` NOT MET; durable link `could-not-evaluate`; not `improved`** | `tools/harness/claims-freshness.py` does not exist (exit 2). W01's pinned scratch assembly `6cbfdef1…` independently reproduces selftest 43/43+18/18, r43 O/C stale + Ca fresh exit 1, negative control exit 0, anti-theater stale, deterministic output, malformed exit 2, no-checks exit 3. But no durable file and no `calib/` demonstration exist (§4) |
| **Ca — calibration** | **PASS-with-required-correction; `improved` not yet recordable** | Ca06 is complete in substance: 3 defect rows + 2 named deviations, 5/5 retrospective bullets + 1 r46 item, parent `dfc9265d…` pinned and unchanged, zero `fixed` rows. But Ca04:195 / Ca06:371 carry a demonstrably false zai verification sentence, and Ca06:113 pins a superseded Ca05 (§5) |
| **Cross — axis harm** | **NONE observed on disk** | corpus 223 / culture-material 25; target absent; `git diff` and `git diff --cached` empty; parent queue digest unchanged; no corpus/tool/README staging; all r47 writes under `reports/round-47/` except the pre-existing r46 anomaly (§6.2) |
| **Round close** | **NOT CERTIFIABLE** | 59/64 seat outs filed at the cut; `reports/round-47/run-validation.py` and `validation.json` absent; no observed-dispatch or availability-close record; no claim admissible on the claim's own counting commands (§6.3, §7) |
| **Overall** | **no claim's `after_required` is met as filed; Ca is the only one whose substance is complete** | C and O must be recorded `could-not-evaluate`; Ca only after correction. Do not record any axis as `improved` on pre-landing evidence |

Two facts bound this verdict. First, the deliverables are integrator-applied: seats may draft, but only the integrator writes `corpus/` and `tools/`. At this cut **nothing has been applied** — no entry, no README edit, no tool file. Second, the wave filed late: R01, R03, R04, O07, O14, X03, W01 and V02 landed at 19:13–19:18Z, after many sibling cuts. Their evidence is folded in at its filing digests; cuts that predate them are labelled as such, not silently upgraded.

## 1. Method and measured baseline

All commands were run read-only at `6e9a30d`; no corpus, tool, README, LOG or filed-round byte was written or staged.

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain -uall -- corpus/ tools/ examples/ .ufo/ PROVINCE.md LOG.md
(empty)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '…': No such file or directory
$ sha256sum reports/round-47/claims.json reports/round-47/targets.json
7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34  reports/round-47/claims.json
d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d  reports/round-47/targets.json
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223
totals_line 223 totals_ok True
footer {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
rc=0
```

The `claims.json` and `targets.json` digests equal `telemetry/dispatch-declared.json`'s declared artifacts. X05 independently found no drift; this seat re-measured both digests and the HEAD sha. The live README carries revision 2.4 and its prose vector is defective: `corpus/README.md:11` reads `25/23/25/29/24/94 → 25/23/26/25/24/94`, which sums **217**, not the live 223 (`:544`, `:548`). That is the pre-existing defect claim C's rev-2.5 edit is required to repair.

This seat read every file present at the 19:16Z census (60 files, then 63 at the 19:18Z cut), including all 59 filed seat artifacts; the three files that landed during the gate (O07, O14, X03) and the last two (W01, V02) were read at their filed bytes. No fragment was assumed from its title. The census is in §2; the digests are in §9.

## 2. Filed-fragment census and absent seats

At the 19:18Z cut, `reports/round-47/` holds **63 files**: **59 filed seat outs** plus `claims.json`, `targets.json`, and two telemetry records. Five declared outs are absent; after this file lands, **four** remain:

| absent out | seat | what the claim loses | substitute, if any |
|---|---|---|---|
| `op/O08-verify.md` | O08 | independent clean-scratch verification of the assembled tool | none filed. **O06 §7.3 cites an "O08 reference oracle" as a runner**; no O08 artifact exists, only a `.scratch` assembly that X03:378 says "was written at 16:10 local by a parallel refire and may be superseded". This is a missing seat's artifact cited as evidence — flagged, not accepted |
| `op/O11-baseline-eval.md` | O11 | worktree-vs-baseline control | V02 §1 and W01 §9.2 measure baseline-only behavior; neither is the declared O11 artifact |
| `op/O15-malformed.md` | O15 | malformed-input vectors (no baseline, missing `before`, non-JSON) | W01 §9 / V02 §5 run several; O10's suite covers exits; no O15 artifact |
| `cov/W02-landing-spec.md` | W02 | C apply order, byte source, sha pin | C11 §6 supplies an apply contract; C09/C10 supply staged mechanics. The declared seat artifact is absent |
| `cross/Q01-final-gate.md` | Q01 | this gate | this file |

Seat artifacts that landed late and are folded in: **R01** (19:15Z, `35d17bc…` at read), **R03** (19:16Z, `2c4328f…`), **R04** (19:15Z, `193be9e…`), **O07** (19:15Z, `86c3120…`), **O14** (19:16Z, `bcdd243…`), **X03** (19:16Z, `52220e2…`), **W01** (19:17Z, `3fd4e83…`), **V02** (19:17Z, `4f21cc5…`). R01/R03 were revised at 19:16:45Z; the verdict lines quoted below are from those final bytes.

The absence list is not cosmetic. The O claim's acceptance surface names O08/O11/O14/O15/V02 as independent checks; at this cut only O14, V02 and the non-O X03 exist, and O08's oracle is cited from scratch without a filed owner record. The C claim's landing spec (W02) is absent; C11's §6 is a scribe substitute, not the declared verifier. Both are named in §7 as `could-not-evaluate`, not inferred green.

## 3. Claim C — coverage: real gap, not landing-ready

### 3.1 Premise — GREEN

The premise is measured true by K01, C05, X04, R01 and this seat: 223 entries, culture-material 25, the slug absent, 0 filename owners, 0 `- topic:` owners, 0 header/title owners. The only prior-round naming is the r44 K02 seed itself (`reports/round-44/scout/K02-gap-scout.md:8`); no prior claim, draft or landing exists. The literal phrase "0 prior-round proposals" is true only relative to r44 K02 — the correct wording is "0 proposals before r44 K02; r44 K02 is the cited seed" (K01 §6.3, X04, C11 D5). This wording defect is in the head block and is one of the fixes.

### 3.2 Draft and assembly — present, 790 lines

The four fenced fragments are filed and digest-pinned:

| fragment | file sha256 | bytes | fenced content |
|---|---|---|---|
| C04 head | `cb5a7489676d…` | 36,044 | 51 lines, 8 head fields |
| C01 §§1–4 | `cfb429556173…` | 47,829 | 201 lines |
| C02 §§5–9 | `5f5683a72ea0…` | 60,985 | 361 lines |
| C03 §§10–15 | `4b699e065371…` | 41,114 | 177 lines |
| **assembly** | **`e0c8ae56a6a9…`** | **128,670** | **790 lines (51 head + 739 body); 601 non-blank; 1 H1, 15 H2** |

The assembly is a seat-side extraction (`.scratch/q01-assembled.md`), not an applied entry. The topic line is 766 characters / 775 bytes (`- topic:` at `reports/round-47/cov/C04-entry-header.md:112`), the `- couples:` line is 4,096 characters with 21 unique tokens (`:115`), and the head carries all eight contract fields. C09's README row is 801 characters and its topic substring is byte-equal to the head's topic; the staged tree is 224/26 with a green sweep (`reports/round-47/cov/C09-readme.md:205-215`). Mechanically, the C landing is ready; editorially, it is not.

### 3.3 Blocking defects — nine content/assembly defects plus volume

R03 files **B1–B9 blocking** and a volume problem; R01 confirms the load-bearing ones; this seat re-measured the cited lines.

| # | defect | measured evidence | status in final bytes |
|---|---|---|---|
| **B1** | false-precision arithmetic: 0.2 mm at 1:50,000 = 10 m; a 200 m closure is **20×** coarser, not "ten times" | `reports/round-47/cov/C02-entry-b.md:98` | unfixed |
| **B2** | gap statement's count is unreproducible: says `grep -rli 'cartograph'` → "2 files / 3 lines"; the command lists files, and the measured count is **2 files / 2 lines** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`); `:71` has no `cartograph` token | `reports/round-47/cov/C04-entry-header.md:115`; `grep -rn 'cartograph' corpus/knowledge \| wc -l` → 2 | unfixed |
| **B3** | **false accusation**: C02 says C01's quote "a map is an archive of coups" is "not in the file" and proposes "renamings"; the live line contains the quote verbatim | `reports/round-47/cov/C02-entry-b.md:36,501` vs `corpus/knowledge/linguistics/naming-systems.md:70` | unfixed; applying C02's fix would corrupt a correct quote |
| **B4** | wrong workshop-ladder anchor: `craft-artisan-lexicon.md:44` is the steel-grading row; the ladder is `:54-65` | `reports/round-47/cov/C02-entry-b.md:248`; `sed -n '44p'` → tamahagane row; `:56-63` → systems | unfixed |
| **B5** | cross-reference drift: C03:79 says "typology in §1–3", C03:184 says "§2"; the typology is C01 §4.1 | `reports/round-47/cov/C03-entry-c.md:79,184`; `reports/round-47/cov/C01-entry-a.md:238` | unfixed |
| **B6** | cross-reference drift: C01's handoff says "Provenance/charter (§9)"; the binding map puts it at §8 | `reports/round-47/cov/C01-entry-a.md:298`; `reports/round-47/cov/C02-entry-b.md:278` | unfixed |
| **B7** | **worked example internally inconsistent**: the update rule is stated three incompatible ways | `reports/round-47/cov/C03-entry-c.md:123` ("after any storm that breaches a dike"), `:137` ("not due until the levy year turns"; joint rule "after every breach"), `:150` ("after a dike breach, per levy year") | unfixed; C14 F-1 blocking |
| **B8** | competing-ownership sentence missing: `cosmology-cosmography.md:27` defines cosmography as "how the world is drawn (maps)…"; the draft cites only the disclaimers `:71`/`:102` | `reports/round-47/cov/C01-entry-a.md:90,96`; `reports/round-47/cov/C04-entry-header.md:115`; `grep -n ':27' .scratch/q01-assembled.md` → 0 | unfixed |
| **B9** | "minimum credible build per form" covers 5 of the 8 forms in C01 §4.1; celestial, thematic and cartographic-history/ lienzo are missing | `reports/round-47/cov/C03-entry-c.md:95-103` vs `reports/round-47/cov/C01-entry-a.md:238-249` | unfixed |
| **volume** | 790 lines / 739 body vs live 103–221 (min 103, median 149, max 221); 3.6× the longest existing entry, 5.3× the median | §3.2; R02, C11 D1 (854 pre-trim), X04, R03 P2-3 | unfixed; C07's own checker FAILs `854 > 260` (C11 §2.1) |

The length is not a style preference: `corpus/knowledge/culture-material/` has a 221-line maximum, and C11 measured the same assembly at 854 lines before C02's 424→361 trim; it is now 790, still outside the band. The count would move to 224 while the partition's usability contract regresses. R01's summary is the correct framing: "a 790-line entry against a 221-line maximum … are not a landing. Do not record coverage as improved."

C14 adds two independent example defects: **F-1** (the three-way update rule) and **F-2** (`grep -c 'DR-CT-'` on §11 is 0; no rule id is named and no consequence↔rule map exists), both blocking under `corpus/knowledge/verification/worked-example-verification.md:52`. C03's file digest is unchanged (`4b699e06…`), so the FAIL stands against the final bytes.

### 3.4 The audit chain is pinned to superseded bytes

`claims.json:31` requires "audits PASS". At the final C02 digest (`5f5683a7…`, 60,985 bytes) the audit chain does not hold:

| audit | pinned/read bytes | current bytes | verdict on final bytes |
|---|---|---|---|
| C06 source | assembly sha `2422ca96…`, **855 lines**, C02 before the 424→361 trim (`reports/round-47/cov/C06-source-audit.md:7,97,627`) | assembly `e0c8ae56…`, 790 lines | **superseded** — must re-run |
| C07 contract | pre-bytes `could-not-evaluate` (no draft at its 17:55Z cut); its checker FAILs length `854 > 260` | drafts exist | **not a pass**; re-run required |
| C08 boundary | pins C01 `a02031a4…`, C02 `85085d24…` (`reports/round-47/cov/C08-boundary.md:6-7,332-333`) | C01 `cfb42955…`, C02 `5f5683a7…` | **stale pins**; its PASS-with-P1 findings were re-read, not re-run |
| C12 shelf | pins C02 `bfce3aca…`, 61,511 bytes (`reports/round-47/cov/C12-shelf.md:33`) | `5f5683a7…`, 60,985 bytes | **stale C02**; advisories stand, audit does not |
| C13 couples | line pin `cf59ba1f…`, stable across C04 revisions | still matches | **passes at the field level**; re-run after assembly |
| C14 example | C03 `4b699e06…` | unchanged | **FAIL** (F-1/F-2) |
| C05 freshness | PASS ownership; post-landing vector `26/26/25/29/24/94` (`reports/round-47/cov/C05-freshness.md:273,295`) | correct post is `25/26/26/29/24/94` | **minor filed-verifier defect**: slot-swapped post-landing vector (X02) |

This is the same class as the defect the O claim exists to prevent — a verification sentence not re-measured against the bytes it cites — one level down. R01 §2.4 reaches the same conclusion: the integrator "cannot record 'audits PASS' without re-running C06/C07/C08/C12/C13/C14 on the final assembly."

### 3.5 The mechanically ready half

C09's README patch is a four-hunk diff: it adds rev 2.5 before rev 2.4, repairs rev 2.4's prose vector `25/23/26/25/24/94 → 25/26/25/29/24/94` (sum 217 → 223), moves `## culture-material/` 25 → 26, inserts the cartography row after `calendar-festival-systems.md`, and moves the totals/footer 223 → 224 with vector `25/26/26/29/24/94` (sum 224). The staged sweep is `rows 224 files 224`, 0 missing/ghosts/topic mismatches, `ok: true`, exit 0 (`reports/round-47/cov/C09-readme.md:205-215`). C10 independently reproduces the staged mechanics and records the sweep's blind spot: control D leaves the rev-2.4 prose vector unrepaired and the sweep still says `ok True`, so a green sweep alone does not prove the vector repair (`reports/round-47/cov/C10-sweep.md:123-129`). C13's 21/21 couples resolution and +1 entry/+21 refs delta are stable. These are apply mechanics, not a landing approval.

### 3.6 C verdict

**Premise green; `after_required` NOT MET; landed state `could-not-evaluate`; not `improved`.** Do not land the 790-line assembly. Close B1–B9, D1–D5 (C11) and the volume; re-assemble; re-run C06/C07/C08/C12/C13/C14 on the final bytes; then apply entry + README atomically and run V01 live. Until then the coverage axis is unchanged at 223, and no axis move is recordable.

## 4. Claim O — operability: the method is proven, the instrument is absent

### 4.1 The durable path does not exist

```
$ ls tools/harness/claims-freshness.py
ls: cannot access '…': No such file or directory
$ python3 tools/harness/claims-freshness.py --selftest
python3: can't open file '…/tools/harness/claims-freshness.py': [Errno 2] No such file or directory
rc=2
$ python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json
(same; rc=2)
$ git cat-file -e 6e9a30d:tools/harness/claims-freshness.py; echo rc=$?
fatal: path '…' does not exist in '6e9a30d'
rc=128
```

The claim's first two counting commands fail. No `calib/` demonstration exists: `reports/round-47/calib/` contains only Ca01–Ca07. The claim's `after_required` — durable tool, green selftest, r43 O/C stale + Ca fresh, negative control not flagged, anti-theater still flags, filed demonstration, non-zero on stale — is unmet on the durable link, regardless of how strong the scratch evidence is.

### 4.2 The pre-landing assembly is green — independently reproduced

W01 landed at 19:17Z with an apply-ready assembly: four durable fences plus a 673-line seam, pinned at **sha256 `6cbfdef1f27dbea80450ebd905700dbc13f1a8f233c72d69c512b74d196461d4`**, 104,538 bytes / 2,695 lines (`reports/round-47/op/W01-landing-spec.md:15-23`). The pinned scratch file exists at `.scratch/w01/claims-freshness.py` and matches that digest. This seat re-ran it independently:

| check | command | measured |
|---|---|---|
| selftest | `python3 -B .scratch/w01/claims-freshness.py --selftest` | `SELFTEST OK: registry 43/43 + seam 18/18 controls`, **rc 0** |
| r43 regression | `--claims reports/round-43/claims.json --checks .scratch/w01/r43-checks.json` | **O STALE 2/2**, **C STALE 1/3** (ownership only), **Ca FRESH 1/1**, summary 1 fresh/2 stale, `REFUSE: claim(s) O, C …`, **rc 1** |
| negative control | `--claims .scratch/w01/negative-control.claims.json` at `c9f4eaa` | **3 fresh, 9/9 clauses, rc 0** |
| discriminator at HEAD | same fixture `--at 6e9a30d` | **O STALE 2/5, C+Ca fresh, rc 1** — a worktree reader would falsely flag the control |
| anti-theater | mutated r43 (resolver/witness renames) `--checks r43-mutated-checks.json` | **O STALE 2/2, C STALE 1/3, Ca FRESH, rc 1** — the flag survives the rename |
| determinism | two `--json` runs | identical sha256 `705d8de4…`, both rc 1 |
| malformed | no `baseline_commit` | `no baseline_commit; worktree evaluation is forbidden`, **rc 2** |
| could-not-evaluate | claim with no checks | summary `0 fresh, 0 stale, 1 could-not-evaluate`, `absence of a verdict is not freshness`, **rc 3** |

This is a genuine measurement layer: baseline-only git plumbing, typed probes, declared polarity, STALE on contradiction, non-zero for malformed and could-not-evaluate. It is the strongest operability asset the round produced. It is also **scratch**, and the claim says "durable not `.scratch`" (`claims.json:47`).

### 4.3 Why the parts did not compose without W01

The three O author fragments are individually sound but not drop-in. This seat reproduced the failures:

- **Plain concatenation is a `SyntaxError`.** `cat` O01+O02+O03 fails at assembled line 694: `from __future__ import annotations` mid-file. `ast.parse` alone does not catch it; `python3` compilation does (`rc=1`).
- **After stripping the later future imports, the concatenation is a false green.** It prints `PROBE-REGISTRY SELFTEST: 43/43` and exits **0** without reading claims, because O02's `if __name__ == "__main__": sys.exit(selftest_registry())` sits mid-file (`reports/round-47/op/O02-probe-registry.md:1220-1221`). Running O02 alone with `--claims reports/round-43/claims.json` has the same result: rc 0, 43/43, no verdict. W01 S2 documents this, R01 and V02 reproduce it.
- **The status vocabulary breaks at the O02→O03 seam.** O02 emits `holds | mismatch | could-not-evaluate` (`O02:687`); O03 accepts `HOLDS | CONTRADICTED | NOT_EVALUATED` and downgrades anything else to `NOT_EVALUATED` (`O03:138,172-184`). Unmapped, a contradiction becomes exit 3, not exit 1 (R04 §3.3, V02 B4, O14 F-O14-2).
- **The probe vocabulary is split 7 vs 8.** O01:96 and O02:61 close at seven kinds and reject `grep_present`; O04:189 and its K4b/K4c controls require an 8-kind registry, `FixtureBaseline` and `evaluate_claim`. O04's 285-line block is a function only, with no `__main__`; running it directly exits 0 silently. W01 resolves this explicitly as a named divergence: seven kinds, O04's 8th kind and its `FixtureBaseline` API are not applicable (`reports/round-47/op/W01-landing-spec.md:1104-1112`).
- **O03's integration sketch is not the parts' API.** `O03:686-701` calls `load_claims(path) -> (header, claims)`, `resolve_baseline(ref)`, and `validate_check(check, claim_id, index)`; O01:508 returns a `ClaimsDoc`, O01:743 defines `open_baseline(root, commit)`, and O02:566 defines `validate_check(check, before_text, seen_ids=None)`. No part defines `main()` or `argparse`; O01 concedes "No CLI yet" (`O01:798`). W01's seam supplies the loader, target compatibility, result bridge and CLI — 673 lines, not a cosmetic patch.

The authors' claims that "plain concatenation" works are false. W01's S1–S7 table is the correct accounting, and its pinned assembly is the only executable path that has been shown to satisfy the contract.

### 4.4 What the O chain still lacks

Even with W01's green pre-landing assembly:

- **No durable file.** `tools/harness/claims-freshness.py` is absent; W01's §3 step 5 is an instruction, not an applied byte.
- **No `calib/` demonstration.** W01 §10 names `reports/round-47/calib/claims-freshness-demo.json`, `r43-checks.json`, `negative-control.claims.json`; none is filed. The claim's "filed demonstration at `reports/round-47/calib/`" is unmet.
- **No durable-path independent run.** V02's mission is to run from the durable path after apply; at its 19:17Z cut the path was absent, so its verdict is `could-not-evaluate`. Its reconstruction is verifier-local and not a landing (`reports/round-47/op/V02-gate-verify.md:116`).
- **O08/O11/O15 absent.** O08's oracle is cited by O06 §7.3 as "the only green gate implementation on disk" but has no filed artifact; O11's baseline-eval and O15's malformed vectors are missing. O07, O14 and X03 are filed and all three say the same thing: method PASS, deliverable absent/false-green.
- **One dangerous latent edge is unflagged by the assembly's own suite.** R04 measured that a capability candidate which executes and exits non-zero is treated as "no capability"; for an absence claim (`expect:false`), an incomplete fixture can launder a present capability as absent (R04 §3.1). The r43 O claims are absence claims. W01 §13.1 declares the execution not sandboxed; V02 §5 repeats the edge. The landed tool should treat a non-zero candidate as `could-not-evaluate` for absence claims, or state the limitation at the point of use.

### 4.5 O verdict

**`could-not-evaluate` on the durable deliverable; `after_required` NOT MET; not `improved`.** The method is proven and the assembly is apply-ready at a pinned digest, but the claim is about a durable file, a green selftest from that file, a filed demonstration and independent verification. None of those exists. The correct integrator action is to apply W01's pinned bytes — not the naive concatenation — run the six acceptance commands from the durable path, file the `calib/` demo and fixtures, and let V02 re-run. Until then the operability axis is unchanged; the latent harm is that applying the concatenation would exit 0 on stale claims, which is worse than no tool.

## 5. Claim Ca — calibration: substance complete, one false sentence

### 5.1 What is filed and measured

| artifact | digest (sha256) | status |
|---|---|---|
| Ca01 stale-premises, `routed-with-owner` | `e0e51e56…` | PASS; route to the O gate; refuses `fixed` while the gate is absent |
| Ca02 resolver edge, `recorded` | `91cd4484…` | PASS; 0/223 live incidence; body pinned; no fix claimed |
| Ca03 MANIFEST schemas, `recorded` | `a2e61cdb…` | PASS; S1 33–42 and S2 43/44/46 documented |
| Ca04 two provider amendments | `94b99878…` | PASS with F6; `defect_row:false` |
| Ca05 verifier | `5dfe7b12…` | PASS; digest block internally inconsistent (R05 F-R05-4) |
| Ca06 successor | `15bb86d…` (46,854 bytes) | 3 rows + 2 amendments; JSON fence parses; parent `dfc9265d…` pinned and unchanged; 5/5 retro bullets + 1 r46 item; zero `fixed` rows; 8 application gates |
| Ca07 integrity | `895d76f7…` | PASS with two conditions |
| R05 reconciliation | `52a1f54f…` | PASS with F-R05-1..5 |
| R01 review | `35d17bc…` (19:15Z) | PASS-with-required-correction |

This seat re-parsed Ca06's JSON fence: top-level keys include `parent`, `parent_sha256_at_assembly` = `parent_sha256_recheck_after_assembly` = `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`, `rows` = 3, `provider_amendments` = 2, `loop1_coverage` = 5/5 + 1. Ca06's file digest equals Ca07's pin. The parent queue is byte-unchanged, and no filed byte was edited. Ca01's routing is correct: the stale-premises row is not marked fixed; it is routed to the O tool, which does not exist.

### 5.2 The required correction

**Ca-R01-1 / F-R05-1 / F-Ca07-3.** `reports/round-47/calib/Ca04-provider-amendments.md:195` and its copy at `reports/round-47/calib/Ca06-queue-successor.md:371` say:

> "no dispatch-declared.json at r44, r46 or r47 names zai (lanes: opencode-go, devin, opencode-go)"

The literal sentence is false. `reports/round-46/telemetry/dispatch-declared.json:16` says "zai usage exhausted", and `reports/round-47/telemetry/dispatch-declared.json:18` says "Standing amendments: zai->luna-max all session". The intended true statement is "none of those rounds dispatched **on** zai; the amendment appears only in the notes." This is the same class the queue exists to prevent — a verification sentence not re-measured against the bytes it cites. It is not a class error; the row remains `named-deviation`, `defect_row:false`, and the parent's practice keeps telemetry deviations out of the defect count.

**Ca-R01-2 / F-Ca07-2.** Ca06:113 pins Ca05 at `747c0fdb1a1c…`; Ca05 was rewritten after assembly. At this cut Ca05's digest is `5dfe7b12c0f4…` (23,xxx bytes). Ca07 read an intermediate `8ec61c7e…`; R05 reviewed `26430501…`. The successor's one line citation to Ca05 (`Ca06:100` → `Ca05:170-187`) lands on the Ca01 verdict section in the current bytes; the parent section is at `Ca05:147` ff. Re-anchor the citation and re-pin the digest after correction.

**Ca-R01-3 / F-R05-3.** Ca03 and Ca06 cite `MANIFEST.json`, `PROTOCOL.md` and `PROTOCOL-APPENDIX.md` as bare paths; they are fleet-root files, not lane files (`ls PROTOCOL.md` → ENOENT). Prefix the fleet root or add one root note.

**F-R05-2 (minor).** Ca06:430 says "r43 Ca admitted"; r43's round verdict is `rejected-honest-stop`; the Ca **claim** was `improved`. Use the Ca01 phrasing ("passed (improved) even though the round was rejected"), not the round-level term "admitted".

**F-R05-4 (minor).** Ca05's own digest block is internally inconsistent (reviewed digest vs current). Recompute at filing.

### 5.3 Ca verdict

**PASS-with-required-correction.** The claim's substance is met: every loop-1 carried item reaches a class with an owner and cited evidence; zero are silently dropped; the freshness row is routed, not prematurely fixed; the provider amendments are named deviations; the parent is pinned and unchanged. But as filed the successor carries a demonstrably false verification sentence and a stale source pin. Record `improved` **only** after Ca04 and Ca06 are corrected, Ca05 is re-pinned, and Ca05/Ca07/R05 re-verify the corrected bytes. A corrected Ca06 is a new digest; Ca07's current PASS does not carry over.

## 6. Cross-cutting close state

### 6.1 Baseline identity — PASS

HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`; commit time `2026-10-19 14:46:42 -0300` = `17:46:42Z`; `claims.json` and `targets.json` digests equal the dispatch pins; no commits after the baseline (`git rev-list --count 6e9a30d..HEAD` → 0). X05 independently found no drift, no digest drift, no ref rewind.

### 6.2 Write surface — no corpus/tool harm

`git status --porcelain -uall -- corpus/ tools/ examples/ .ufo/ PROVINCE.md LOG.md` is empty; `git diff` and `git diff --cached` are empty. The only path outside `reports/round-47/` is the pre-existing untracked `reports/round-46/review/R01-review.md`, an r46 artifact, not an r47 seat path. A gitignored `.pyc` under `tools/harness/__pycache__/` is a runtime side-effect, not a tracked write. A03's census reaches the same conclusion; A01 found no cross-domain bleed and PROVINCE accurate.

### 6.3 Close artifacts — absent

`reports/round-47/run-validation.py` and `reports/round-47/validation.json` do not exist. The claims' counting command for O and Ca names `run-validation.py`; it cannot run. `reports/round-47/telemetry/` has only `dispatch-declared.json` and `refire-key6.json`; there is no observed-dispatch record and no availability-close snapshot. S02 drafted the skeletons; they are not filed. Per `AGENTS.md`, the closing snapshot is owed when `validation.json` lands; it has not landed, so the round cannot be admitted to `LOG.md`.

The `refire-key6.json` note records 14 seats missing after the first batch and a refire on key 6. At this cut 5 outs are missing (4 after this file). Requested workers = 64; observed launches/completions/failures are **not recorded** — they stay `null`/`could-not-evaluate`, not inferred from the seat counts. The seat count is a file census, not a dispatch telemetry measurement.

### 6.4 Claim counting commands — evaluated

| claim | command | result |
|---|---|---|
| C | `find corpus/knowledge -name '*.md' \| wc -l` | 223 (pre-landing) |
| C | `ls corpus/knowledge/culture-material/*.md \| wc -l` | 25 |
| C | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, exit 0 |
| C | target path | absent |
| O | `python3 tools/harness/claims-freshness.py --selftest` | exit 2 (file absent) |
| O | `python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json` | exit 2 (file absent) |
| Ca | `python3 reports/round-47/run-validation.py` | exit 2 (file absent) |

The O claim's `after_required` and the Ca claim's counting command both fail for the same reason: the artifacts the round is meant to produce have not been applied. That is a delivery fact, not a measurement defect.

## 7. Could-not-evaluate register

Everything below is explicitly `could-not-evaluate`; none is inferred green. Each has an owner and a re-run.

| # | item | owner | re-run |
|---|---|---|---|
| 1 | C landed state: 224 total, culture-material 26, no second owner | integrator (W02 apply) | V01 §7 after apply |
| 2 | C content audits on final bytes | C06/C07/C08/C12/C13/C14 authors or integrator | re-run each on the corrected assembly; C07's checker must be 0 FAIL |
| 3 | C QUALITY Q1–Q5 "as delivered" | C07/R03 | C07 §7 after apply; R03 re-read |
| 4 | O durable tool, its selftest and r43/negative/anti-theater runs | integrator (W01 apply) | `--selftest`, then the five commands in W01 §3 step 6 |
| 5 | O filed `calib/` demonstration and fixtures | integrator / O12 | file `claims-freshness-demo.json`, `r43-checks.json`, `negative-control.claims.json`; re-run |
| 6 | O08 independent verification, O11 baseline-eval, O15 malformed vectors | O08/O11/O15 | file the declared outs; V02 re-run |
| 7 | O08 oracle provenance (O06 §7.3 cites an unfiled `O08` runner) | O06/O08 | file the oracle or re-label it `to-verify`; do not cite a scratch file as O08 |
| 8 | Ca corrected successor and re-verification | Ca04/Ca06 author + Ca05/Ca07 | correct the zai sentence, re-pin Ca05, re-run Ca05/Ca07/R05 |
| 9 | Ca "improved" verdict | integrator/validation | only after #8 |
| 10 | Round validation `validation.json` / `run-validation.py` | integrator | file the runner, run it from a copy, file the receipt |
| 11 | Observed dispatch and availability close | integrator/telemetry owner | file redacted samples with owner, window, counting command, digests; unknowns stay `null` |
| 12 | Missing seats O08/O11/O15/W02 | parent/dispatch | file or record `could-not-evaluate` with an owner; do not backfill |
| 13 | C05's post-landing vector | C05 | correct `26/26/25/29/24/94` → `25/26/26/29/24/94` before it is cited |
| 14 | O capability absence edge (non-zero candidate treated as absent) | O author/R04 | add the `could-not-evaluate` rule or state the limitation at the point of use |

## 8. Close checklist — what the integrator must do, in order

1. **C: do not land the 790-line assembly.** Fix B1–B9 and C11 D1–D5 (volume, false `cartograph` count, cosmology:27 disposition, craft ladder, cross-refs, per-form table, C02's false accusation). Re-assemble; re-run C06/C07/C08/C12/C13/C14 on the corrected bytes. Only then apply the entry + README atomically (C09's four hunks, C10's staged sweep) and run V01 live. Record 224/26 and the corrected vector `25/26/26/29/24/94`.
2. **O: apply W01's pinned bytes, not the concatenation.** Verify the four fence digests and the assembled sha `6cbfdef1…`; apply `tools/harness/claims-freshness.py`; run `--selftest` and the five acceptance commands from the durable path; file the `calib/` demonstration and fixtures; run V02. Treat the naive concat as a known false green.
3. **Ca: correct before filing.** Fix the zai sentence in Ca04 and Ca06, re-pin and re-anchor Ca05, add the fleet-root prefix, fix the "admitted" wording. Re-run Ca05/Ca07/R05. Only then record Ca `improved`.
4. **File the round's own close artifacts.** `run-validation.py` and `validation.json`; observed-dispatch and availability-close snapshots with durable samples and digests, or `null` with an owner and reason. Do not reconstruct historical samples.
5. **Admit nothing on pre-landing evidence.** C and O stay `could-not-evaluate`; Ca stays conditional; the coverage axis is unchanged at 223; the operability axis is unchanged. No axis move is recordable from this cut.

## 9. Evidence appendix

### 9.1 Digests of the bytes reviewed (selected; full set measured at 19:18Z)

```
cfb42955617373479a41d881fb6fd83f7df907aa7f563f51de95493d9ec8c44d  cov/C01-entry-a.md
5f5683a72ea06d4e929d694a7eb03a067ebc7adc00cdb5ea6d72f489797779af  cov/C02-entry-b.md
4b699e06537115274807b64fbc5947cefc889348e5b4434b14a8ddb661eee3e5  cov/C03-entry-c.md
cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0  cov/C04-entry-header.md
e0c8ae56a6a9a67b142af54317363013ac08e03cb7611058c65ca5189e9913aa  .scratch/q01-assembled.md (790 lines)
2422ca96c2fab0385b1e6f89a8faa4f72134c59cde5522d9d498720b149b0942  C06's assembly (855 lines; superseded)
6cbfdef1f27dbea80450ebd905700dbc13f1a8f233c72d69c512b74d196461d4  .scratch/w01/claims-freshness.py (2,695 lines; W01 pin)
3fd4e831eba0b1ca351fd563a194213cd43d7b240e2a77844fc66943c0772e3d  op/W01-landing-spec.md
4f21cc565cfb8c553af545637a713582f7c644f1c4ccdb21948bab6e5cd8cdd3  op/V02-gate-verify.md
86c31202799635ca92dbafc68dc8a56bd78b161b174eb5986b7695ba6e58bdce  op/O07-anti-theater.md
bcdd243d4a324014ed6e84d6c5d03b535c3a2cfba30e041bb94142dfe82201b1  op/O14-determinism.md
52220e2622684b08f913c8add6094cfab2139e449e839fd74b4eec2c280ef239  cross/X03-gate-theater.md
94b99878a31ae6aa8c376fa35af786e36d07f3210c9f368f9a014f4a4ac2136e  calib/Ca04-provider-amendments.md
5dfe7b12c0f4adbdac16e26942dfbe54fb37582ce17cbbefe44039d279e9207f  calib/Ca05-verify.md
15bb86dfff09ff97cbf8e757bbf139e1cb7bc59f42c66475d19a5a1b02db5ec6  calib/Ca06-queue-successor.md
895d76f7cc2c80b1ab14b05d21b869630a002f293f8ae6e7412fbe77b114eb3b  calib/Ca07-integrity.md
```

`claims.json` = `7eb16979…f9e1fa34`; `targets.json` = `d60e5572…09ca3d`; both equal the dispatch pins. Ca05's digest changed after Ca06's assembly: Ca06:113 pins `747c0fdb…`; the current file is `5dfe7b12…`; Ca07 read an intermediate `8ec61c7e…`.

### 9.2 Commands (representative)

```
git rev-parse HEAD; git status --porcelain -uall; git diff; git diff --cached
find corpus/knowledge -name '*.md' | wc -l; ls corpus/knowledge/culture-material/*.md | wc -l
python3 -B reports/round-28/readme/sweep.py
grep -rn 'cartograph' corpus/knowledge | wc -l
sed -n '27p;71p;102p' corpus/knowledge/myth-symbol/cosmology-cosmography.md
sed -n '44p;54,65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
sed -n '70p' corpus/knowledge/linguistics/naming-systems.md
python3 -B -c 'import ast; ast.parse(open(".scratch/q01/assembled-naive.py").read())'
python3 -B .scratch/q01/assembled-naive.py --claims reports/round-43/claims.json   # SyntaxError line 694, rc 1
python3 -B .scratch/w01/claims-freshness.py --selftest                             # rc 0, 43/43 + 18/18
python3 -B .scratch/w01/claims-freshness.py --claims reports/round-43/claims.json --checks .scratch/w01/r43-checks.json  # rc 1
python3 -B .scratch/w01/claims-freshness.py --claims .scratch/w01/negative-control.claims.json                            # rc 0
python3 -B .scratch/w01/claims-freshness.py --claims .scratch/w01/r43-mutated.json --checks .scratch/w01/r43-mutated-checks.json  # rc 1
python3 -B .scratch/w01/claims-freshness.py --claims .scratch/w01/negative-control.claims.json --at 6e9a30d               # rc 1
python3 -B .scratch/w01/claims-freshness.py --claims ... (no baseline)                                                    # rc 2
python3 -B .scratch/w01/claims-freshness.py --claims ... (no checks)                                                      # rc 3
sha256sum reports/round-47/calib/Ca04-provider-amendments.md … Ca06-queue-successor.md
```

### 9.3 Limits of this gate

This is a **cut**, not a close. The wave was still filing at 19:18Z: O08, O11, O15 and W02 remained absent, and any of them could land after this file. The verdicts are bound to the digests in §9.1. This seat did not author any fragment, did not apply any byte, did not run `run-validation.py`, and did not infer a completion count from the seat census. Where a run depended on scratch bytes (W01's assembly, O05/O06 reference evaluators), it is labelled scratch and is not a durable-path proof.

Signed: **Q01** — non-author final gate for round 47, claim cross. No filed byte edited; nothing staged under `corpus/`; no commit, push, install or network; no `reports/round-*/run-validation.py` executed in-tree.

---

## 10. Post-cut re-census (2026-10-19T19:20Z) — O08, O15, W02 and final R01/R03

The wave completed its remaining verifier and landing seats after the 19:18Z cut. This section is a dated re-census; it supersedes the absence rows in §2 for O08/O15/W02 and the R01/R03 digests in §5.1. **No claim verdict in §0–§8 changes.**

**Census at 19:20:43Z:** `reports/round-47/` holds **67 files** — **63 filed seat outs** plus the four non-seat records. **`op/O11-baseline-eval.md` is the only absent declared out.** The earlier `five absent` count is superseded.

| late filing | digest (sha256) | bytes | effect on this gate |
|---|---|---|---|
| `op/O08-verify.md` | `12b14cacacf8fba5d29ca2be05e922e4276dafdcda7612e3672a3fcc4b4dcdd8` | 19,174 | **BLOCKED, conditional PASS on behavior / FAIL on artifact.** Four required behaviors reproduce through a ~100-line verifier adapter (registry 43/43; r43 O/C stale + Ca fresh exit 1; negative control 8/8 exit 0; anti-theater 4/4); plain concatenation fails; the filed O05 overlay is rejected 5/6 and the O06 fixture is rejected. Files D1–D9. Its cut predates W01's corrective assembly, so it does not test the pinned 2,695-line body |
| `op/O15-malformed.md` | `519e0854f8e5bb35dd1734dd30c536ea6c15c1f948de298aba92c2d6cdd7a81c` | 29,922 | Three named malformed inputs (no baseline, missing `before`, non-JSON) each exit 2 with no traceback and no green on the assembled draft; focused battery 13/13, broad 16/17. **New defect O15-D1:** a non-UTF-8 claims file raises `UnicodeDecodeError` out of part 1 as a traceback/exit 1 instead of exit 2. Durable link `could-not-evaluate` |
| `cov/W02-landing-spec.md` | `4f0df48c080106fcd63d8ce57b4bbc4dc39a0334e8fe4075b665c85cc07eccf6` | 31,901 | **Apply sheet, not an applied landing.** Its assembler applies the C08 P1 boundary rows and R02 C-D2/C-D3 corrections and pins **797 lines / 130,776 bytes / sha256 `8fdb8bd7c0445ac3c3b57e44b6debf3dac20e4c9b4fdc0848bf1e7eb1687b25b`**; the staged 224 tree is sweep-green. **The length gate is explicitly left open:** W02 reports C07's checker as 0 FAIL / 2 WARN at 797 lines, while C11 D1, R02, X04, R01 and R03 call the length blocking. W02 offers three options — trim to ≤340 (or C07's ≤260), file a C07/R03 waiver, or land and record C `unchanged` — and says "do not land silently at 797 and claim improved" |
| `review/R01-review.md` (final) | `196328de7de3ea19cce8f689bef140bbaa13f8b77b0be987253a702c23fe235c` | 41,860 | Verdicts unchanged; now folds in W01/V02: O stays `could-not-evaluate` (durable path absent, no `calib/` demo), C stays not landing-ready, Ca stays PASS-with-required-correction |
| `review/R03-c-content.md` (final) | `7e3e0880cfc7610b5d066bdf09c713a22038121b84cabb12c4fb8f968e8f238e` | 32,845 | B1–B9 and the volume finding unchanged |

**Consequences for the record.**

1. **§2 absence table.** The O08, O15 and W02 rows are superseded: all three are filed. Only `op/O11-baseline-eval.md` remains absent; V02's baseline-only measurements and W01 §9.2 are the substitute evidence, not the declared artifact.
2. **§4.4.** Replace "O08/O11/O15 absent" with: O08 filed and independently confirms the artifact failure (conditional PASS behavior / FAIL artifact, D1–D9); O15 filed and confirms the malformed leg while adding O15-D1; O11 remains absent. W01's pinned assembly `6cbfdef1…` is still the only executable path shown to satisfy the contract; O08's adapter predates it.
3. **§3.2/§3.3.** W02's corrected assembly is **797 lines**, not 790: the corrections add bytes and do not cure B1–B9 or the volume. The length conflict (C07 WARN vs C11/R02/X04/R01/R03 blocking) is now explicit and must be resolved by the integrator before apply. The stricter reading governs this gate: **C is not landing-ready.**
4. **§5.1.** R01's final digest is `196328de…` (41,860 bytes, 19:18Z), not `35d17bc…`. Its Ca correction (Ca-R01-1/2/3) is unchanged.
5. **§7.** Item 6 narrows to O08-already-filed / O11-absent; add **O15-D1** (non-UTF-8 input must exit 2, not traceback/exit 1) as a required fix before apply.

**Gate verdict at the 19:20Z re-census: unchanged.** C and O remain `could-not-evaluate` on their `after_required`; Ca remains PASS-with-required-correction; no axis is recordable as `improved`; the round close is not certifiable until `run-validation.py`, `validation.json`, the observed-dispatch/availability-close record and O11 are filed, and until W01's bytes are applied and verified from the durable path.
