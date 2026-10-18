# R17-D39 — fragment ledger: round-17 wave (D4 build + C/O)

Seat: R17-D39 (scribe), round 17 (operator loop 2 of 3, build round 1 of 4;
64 declared workers, `opencode-go/deepseek-v4.1-flash`). Date: 2026-10-18.
Reference revision: `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17
declare); baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit;
`git merge-base --is-ancestor f30b6f8 HEAD` → exit 0, 2026-10-18T09:18Z).
Writes: this file only; no commit, no push, no filed round 8–16 byte touched.

This ledger ties the round-17 evidence fragments for the parent's LOG/SCORECARD
integration. It is NON-CANON engineering evidence; it admits nothing and
verifies no promotion. Results are attributed to their source fragment unless
marked ⟦IC⟧ = independently checked by this seat. **Close state:** the wave
was still in flight when this seat's 20-minute polling window ended; the D4
example tree never landed inside the window, so every D4/O row below is an
in-flight pin, not a settled-tree record.

## 0. Method and clock

- cwd = lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  `export TMPDIR=$PWD/.scratch` before every scratch-writing command;
  `PYTHONDONTWRITEBYTECODE=1` for python probes.
- Timestamps are UTC (`date -u +%FT%TZ`). Fragment hashes are `sha256sum` at
  the stated read time; a hash is a **read-time** pin, so a mismatch later
  means the fragment changed after this read, never that the earlier read
  was wrong.
- Dependency polling: 60s cadence, maximum 20 minutes (assignment rule);
  window T0 = 09:15Z … last poll 09:34:43Z, close sweep 09:35:34Z. Poll log
  §5.
- Negative claims (a path absent) carry their sweep command and time.

Poll summary: T0 09:15Z 2 files; T1 09:20:42Z first civ fragment + scope;
T4 09:24:29Z runner + typed support + validation receipt; T7 09:28:22Z
design docs + first component; T11 09:33:34Z assembler exists; T12 09:34:43Z
5 components, 12 civ entries, verify-2; D4 tree 0 files at every poll.

## 1. Baseline receipts — pinned before fragments

Declare-commit scope: `git diff --stat f30b6f8..HEAD` →
`reports/round-17/claims.json` (+34) and `reports/round-17/targets.json`
(+18); no other path (2026-10-18T09:18Z). So all round-17 work lands as new
files on top of this commit.

Artifact pins (`sha256sum`, 2026-10-18T09:16:43Z; full output
`.scratch/d38-d39/baseline.txt`):

| path | sha256 |
|---|---|
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5b495a90e05ce42d4d8b6d08f047359c377e458f9190b1d310d6dde3a` |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` |
| `examples/culture-d3/packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| `examples/culture-d3/packet.gates.yml` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` |
| `examples/culture-d3/expected.json` | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/assemble-d2-typed.py` | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `tools/assemble-culture-d3.py` | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` |
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` |

**Untouched re-check ⟦IC⟧ (2026-10-18T09:32:27Z):** all 13 paths above still
equal their baseline pins (per-file loop, `sha256sum` vs the baseline line
for the same path) — the D and O claims' "d2/d3 untouched" leg held through
the wave window so far. This is a mid-wave observation; the runner and the
parent must re-verify on the settled tree.

Standing green legs (this seat, read-only, 2026-10-18T09:17:44Z; raw
`.scratch/d38-d39/legs.txt`; table duplicated in `scribe-1.md` §4):
`assemble-d2 --check` exit 0; `d2-typed-labels --selftest` 39/39 exit 0;
`d2-typed-labels --check` exit 0; `assemble-culture-d3 --check` exit 0;
`check-evidence-coupling` D3 frozen exit 0 / 0 findings;
`typed-pipeline-gate.py` exit 0 16/16 (15 holds + 1 note);
`replay-frozen --selftest` 79/79 exit 0. Plus ⟦IC⟧
`tools/assemble-culture-d4.py --selftest` exit 0, 79/79 at 09:34:32Z, tool
hash `d5f2693ccc3946e7e31ba91ee56f7b34cc44aa871169f4c27c5cbcb266c6d970` (the
tool was edited again after this pin — see §4).

## 2. Round-17 shard map (`reports/round-17/targets.json`, read 09:15Z)

| role | workers |
|---|---|
| D-design | 4 |
| D-components | 12 |
| D-typed | 4 |
| O-assembler | 4 |
| D-tests | 8 |
| D-neg | 3 |
| D-review | 5 |
| D-scribe | 2 (this seat pair) |
| C-fixers | 12 |
| C-verifiers | 4 |
| X | 2 |

Calibration note (count with command + date): the role map sums to **60**,
while `reports/round-17/claims.json` declares **64** workers
(`python3 -c "import json; w=json.load(open('reports/round-17/targets.json'))['workers']; print(sum(w.values()))"` → 60, 2026-10-18T09:16:43Z). Independently
corroborated by two other seats with their own counts: X01
(`corpus/lessons/round-17.md`, opening census) and X02
(`reports/round-17/scope.md` F-X02-1) — three derivations, one number. It is
a count observation for the parent, not a defect claim: the map may be
abbreviated or some roles may carry extra seats.

## 3. Fragment ledger (close sweep 2026-10-18T09:35:34Z)

Status key: **landed** = file exists and was read; **absent** = named but not
on disk at the sweep time; **in-flight** = exists but workers were still
editing (hash is a read-time pin).

| artifact / fragment | role | status | sha256 (read-time 09:35:34Z) | evidence |
|---|---|---|---|---|
| `examples/culture-d4/` (tree: 12 components, typed labels, packet, expected set, frozen manifest, README/handoff) | D-design/D-components/D-typed/integrator | absent | — | `find examples/culture-d4 -type f` → 0 at every poll 09:15–09:34:43Z; `ls` → No such file or directory |
| `reports/round-17/d4/components/01-brief.yml` | D05 | landed | `1a51b313c3da43101ea7fdaab9952d7206b70db2bf23c210edd27de8774a792f` | registry + `contract.hold_set_declaration`; integrator copies fragments into the tree |
| `reports/round-17/d4/components/02-phonology.yml` | D06 | landed | `7aa9cac5c030dfb39fbe5a90d04ea5d94f130f7a7e28b5bbb17ff2773ab0a42a` | component 02 of 12 |
| `reports/round-17/d4/components/03-orthography.yml` | D07 | landed | `de1820b0c115271f7f86fbad8f7e6d637a6155cb61ad9a92cd53e32fdc08783e` | component 03 of 12 |
| `reports/round-17/d4/components/04-lexicon.yml` | D08 | landed | `82efbf71ebd3e078db0db2693640cd26c585276ff00aeb02277a05e479c4ba6b` | component 04 of 12 |
| `reports/round-17/d4/components/05-naming.yml` | D09 | landed | `d07503a9d95f24a6dc64c22feedadc104376885fa4e86be1f1c37c4d89ad5544` | component 05 of 12; components 06–12 absent at close |
| `reports/round-17/d4/design-brief.md` | D01 | landed | `a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f` | D4 brief + 12-component registry + candidate hold set named pre-implementation |
| `reports/round-17/d4/design-language.md` | D02 | landed | `947135770af8fb16f3cac43b6d7234261e3a74aaf811232d9ac89af615e0fb3c` | language slice design + slice hold set |
| `reports/round-17/d4/design-myth-era.md` | D03 | landed | `c17f97798f14d09756102546c3702bf6a6f517f1ffed93dfd62312f9da3aca17` | myth/era slice design + slice hold set |
| `reports/round-17/d4/design-costume.md` | D04 | landed | `04577f4cd0b4232e7ccdcce57bacad1ee33da3dcfbdb1b783f64eaa989e36857` | costume/material slice + slice hold set; pre-implementation record |
| `reports/round-17/d4/typed-support-1.md` | D18 | landed | `7127634d1a89cf994ef93a51d78e6a43b404a1f1583c023f4dfa0b0667770cf4` | typed-derivation contract; finds the D2 projector culture-bound in 3 places (LEX-GAR regex, rank/era legs) |
| `reports/round-17/d4/typed-support-2.md` | D19 | landed | `1f776c3463395ade4e68b6aa3142e748b255924821faeee0b731e5c74639fa26` | hold-set naming/documentation contract |
| `reports/round-17/d4/expected-holds.fragment.json` | D19 | landed | `ee0908e108b22feafb014da40851db34c421a5ae91a3e37ff2791d45a266686a` | expected-hold-set fragment; final expected file + typed labels await the tree |
| `tools/assemble-culture-d4.py` | O-assembler | landed (in-flight) | `5c95f289c11df5384905fcd25f219eb5dc2f0376571e65325d8cfe9645d6b5d7` | landed ~09:33Z; ⟦IC⟧ `--selftest` 79/79 exit 0 at 09:34:32Z (then hash `d5f2693c…`); edited again by 09:35:24Z and 09:35:34Z → re-run at admission |
| `reports/round-17/run-validation.py` | X02 | landed (in-flight) | `4ac405ce35b2d36cfb0a58aa7b9d2e074379ec0be6e65403e543fa9ea2031574` | the round's counting command; edited several times during the wave |
| `reports/round-17/validation.json` | X02 runner | landed (mid-wave receipt) | `9b95acaebf3cb828ef2f001fe26cf937b9e10db612a5ff2cb2193be593e2ccf9` | acceptance **False** with named missing deps (D4 packet/typed/projection/expected/brief, components 0/12, frozen manifest, NON-CANON, assembler); C measured True at that run; receipt `runner_sha256` `9272173c…` ≠ current runner `4ac405ce…` → must be re-run on the settled tree |
| `reports/round-17/tests/neg-1.md` | D30 | landed | `1c2789481dec54069b589f8fe806fe80448c55d16d8c4fae7ee6fc3ed0ff62b8` | gloss-smuggle negative caught (L2-channel line + projector `D2L-NATIVE` fail) |
| `reports/round-17/tests/neg-2.md` | D31 | landed | `eacb46fd6fffcbb7e6cdbf08beb7c277c2543fbcc81fabe28df4330f0daf3230` | owed-form-drop negative caught both directions |
| `reports/round-17/tests/neg-3.md` | D32 | landed | `7ffbdbe8e8520af3e78130ff83625f31252c57769dd4d2658bf24a20883cf876` | loan-without-layer negative caught on both channels; fixtures are D2-derived synthetic controls |
| `reports/round-17/civ/inuit.md` | C01 | landed | `7241e6b48f1b3cb55b2f90f4af5918cd7f6e6adf12e4e162050b4c02036a10a5` | Dorais locator stale-fixed (old→new pageplace preview; 404×3 reconfirmed; ISBN match) |
| `reports/round-17/civ/mongol.md` | C03 | landed | `47ba5951db3662fa4a37cb793d9764e464932a45d58e18560ba4b2ac13ebc013` | rubruck.html live re-attempt 8/8 HTTP 200; locator unchanged |
| `reports/round-17/civ/muisca.md` | C02 | landed | `c671d29b041e80faade8f0655bbd36a7936ec373510cdcea4797a8edda76f1e7` | 4 hard-fail `muysca.cubun.org` URLs dispositioned |
| `reports/round-17/civ/mesoamerica.md` | C04 | landed | `e4e546ab461c071e06099620655a78db78dd06deace8e2d42ec6d0d6b0033432` | 3 hard-fail URLs + round-11 pin drift; entry post-edit hash `d04d8913…` |
| `reports/round-17/civ/persia-sasanian.md` | C06 | landed | `1d536dcecbeba3015490a4ae871decd94a21e125b105f4806f4fc1d4ef6912a7` | never-swept #1 live-swept; 2 stale locators fixed |
| `reports/round-17/civ/polynesia-navigation.md` | C05 | landed | `02deda5b91dfc92dc80fb3d6c91b84a24f329fcd106dd20cb9caa49306132242` | never-swept #2 disposition |
| `reports/round-17/civ/rapa-nui.md` | C08 | landed | `f58f8af47f9ceaae0d4e1271116e922043948a0a49ab3eceb6dff92bac90609a` | never-swept #3 = 9-URL set swept live |
| `reports/round-17/civ/sed77.md` | C09 | landed | `4b628f58991d69160f29ac1c169bb71212569e1c4507a005c39167c6a4fcfd63` | never-swept #4 = `rome.md` (sed-77 identity conflict recorded: line 77 prints persia-sasanian, excluded) |
| `reports/round-17/civ/sed78.md` | C10 | landed | `ebf283ffd73f97cf61b485da43f0d95900415110015f06e748c428ab5f85862f` | never-swept #5 = `ryukyu.md` (sed probe) |
| `reports/round-17/civ/sed79.md` | C11 | landed | `d5c3517d126dbe301cb80222666c2de638fdf7a92efa391bab64f74684ad0257` | never-swept #6 disposition |
| `reports/round-17/civ/sed80.md` | C12 | landed | `d4f1bd00045510a84ad5352defebf93b57989ee714b744d25929b7123782e054` | never-swept #7 = `siam-thai.md` (14 URLs + `sed -n '80p'` probe) |
| `reports/round-17/civ/map-patch.json` | C-verifier | landed | `79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e` | machine map patch (12 dispositions); the round-16 map itself is filed and not edited |
| `reports/round-17/civ/verify-1.md` | C-verifier | landed | `ec27158f71630e5843b552f51e2e38235fc7ab641c7a3e10e8e35e1317c86388` | independent verification receipt 1 |
| `reports/round-17/civ/verify-2.md` | C-verifier | landed | `fb15616fe7465ab6a10309b8bb0ebe4973f3ca939ca475238e538c95e33b9452` | independent verification receipt 2 |
| `reports/round-17/civ/v03-v04-never-swept-verify.md` | C-verifier | landed | `97e7286fc35bc62dbe6f97ab46fe481306d9876484f76a198fda94db1e451edf` | never-swept v03/v04 verification |
| `reports/round-17/scope.md` | X02 | landed | `7eb0d7738dab2ee3f20e0ab4ee7d76f23da5bf2128dcee8b207998b6ff429e6b` | in-scope/clean; F-X02-1 (60 vs 64), F-X02-3 (round-3 replay pin historical class) |
| `reports/round-17/report-draft.md` | X02 | landed (in-flight) | `b628b9b1ef26995f9e7a5225fdd034015b0c41c9ee2e819b81bea8311007e836` | integration report draft; parent owns the final report |
| `corpus/lessons/round-17.md` | X01 | landed | `5a226d39c32f7b3efa0c1c453062d4d4458f8eb53a67a7e6377cb75b05b1a39a` | opening census; D2/D3 before-controls; count finding |
| corpus edits — 12 files, all named stale entries | C-fixers | landed | `inuit 52c5a11b…` `maya-classic d9608d84…` `mesoamerica-primary-sources d04d8913…` `mongol e60b3903…` `muisca 417b7086…` `persia-sasanian 20e7513e…` `polynesia-navigation a47639dc…` `rapa-nui c893805a…` `rome 0b29e05c…` `ryukyu 424fcbb5…` `scythian-saka cb3a6428…` `siam-thai 8bef2a5b…` | `git status --porcelain` 09:34:43Z: exactly these 12 modified; no other corpus path dirty (sweep: full `git status --porcelain` list) |
| `reports/round-17/scribe-1.md` | D38 (this pair) | landed | `b77bdf31e400966e84e6c1160b1f4bf90440adcf3ae204b849dab53aea05a8b2` | capability-row drafts (§ conditions + standing legs) |
| `reports/round-17/scribe-2.md` | D39 (this pair) | this file | self (excluded from pins) | this ledger |
| D4 test fragments (D-tests 8 seats), D-review fragments (5), components 06–12, D4 typed labels / packet / expected / frozen manifest | D-tests/D-review/D-components/D-typed | absent | — | `find reports/round-17 -type f` at 09:34:43Z shows none of these; D4 tree 0 files |

### 3.1 Machine-readable pins (close-time, 2026-10-18T09:35:34Z)

```json ledger
{
  "observed_at": "2026-10-18T09:35:34Z",
  "pins": [
    {"path": "reports/round-17/claims.json", "sha256": "3ac1586a6860f5fee18a234ba799cee555d211a1e810f72ec570b2146d7df854"},
    {"path": "reports/round-17/targets.json", "sha256": "28ee64378b762de86f6fd7d80d816fe8be78103b11e8193660555cd32c7bf904"},
    {"path": "reports/round-17/scope.md", "sha256": "7eb0d7738dab2ee3f20e0ab4ee7d76f23da5bf2128dcee8b207998b6ff429e6b"},
    {"path": "reports/round-17/report-draft.md", "sha256": "b628b9b1ef26995f9e7a5225fdd034015b0c41c9ee2e819b81bea8311007e836"},
    {"path": "reports/round-17/run-validation.py", "sha256": "4ac405ce35b2d36cfb0a58aa7b9d2e074379ec0be6e65403e543fa9ea2031574"},
    {"path": "reports/round-17/validation.json", "sha256": "9b95acaebf3cb828ef2f001fe26cf937b9e10db612a5ff2cb2193be593e2ccf9"},
    {"path": "reports/round-17/tests/neg-1.md", "sha256": "1c2789481dec54069b589f8fe806fe80448c55d16d8c4fae7ee6fc3ed0ff62b8"},
    {"path": "reports/round-17/tests/neg-2.md", "sha256": "eacb46fd6fffcbb7e6cdbf08beb7c277c2543fbcc81fabe28df4330f0daf3230"},
    {"path": "reports/round-17/tests/neg-3.md", "sha256": "7ffbdbe8e8520af3e78130ff83625f31252c57769dd4d2658bf24a20883cf876"},
    {"path": "reports/round-17/d4/design-brief.md", "sha256": "a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f"},
    {"path": "reports/round-17/d4/design-language.md", "sha256": "947135770af8fb16f3cac43b6d7234261e3a74aaf811232d9ac89af615e0fb3c"},
    {"path": "reports/round-17/d4/design-myth-era.md", "sha256": "c17f97798f14d09756102546c3702bf6a6f517f1ffed93dfd62312f9da3aca17"},
    {"path": "reports/round-17/d4/design-costume.md", "sha256": "04577f4cd0b4232e7ccdcce57bacad1ee33da3dcfbdb1b783f64eaa989e36857"},
    {"path": "reports/round-17/d4/typed-support-1.md", "sha256": "7127634d1a89cf994ef93a51d78e6a43b404a1f1583c023f4dfa0b0667770cf4"},
    {"path": "reports/round-17/d4/typed-support-2.md", "sha256": "1f776c3463395ade4e68b6aa3142e748b255924821faeee0b731e5c74639fa26"},
    {"path": "reports/round-17/d4/expected-holds.fragment.json", "sha256": "ee0908e108b22feafb014da40851db34c421a5ae91a3e37ff2791d45a266686a"},
    {"path": "reports/round-17/d4/components/01-brief.yml", "sha256": "1a51b313c3da43101ea7fdaab9952d7206b70db2bf23c210edd27de8774a792f"},
    {"path": "reports/round-17/d4/components/02-phonology.yml", "sha256": "7aa9cac5c030dfb39fbe5a90d04ea5d94f130f7a7e28b5bbb17ff2773ab0a42a"},
    {"path": "reports/round-17/d4/components/03-orthography.yml", "sha256": "de1820b0c115271f7f86fbad8f7e6d637a6155cb61ad9a92cd53e32fdc08783e"},
    {"path": "reports/round-17/d4/components/04-lexicon.yml", "sha256": "82efbf71ebd3e078db0db2693640cd26c585276ff00aeb02277a05e479c4ba6b"},
    {"path": "reports/round-17/d4/components/05-naming.yml", "sha256": "d07503a9d95f24a6dc64c22feedadc104376885fa4e86be1f1c37c4d89ad5544"},
    {"path": "tools/assemble-culture-d4.py", "sha256": "5c95f289c11df5384905fcd25f219eb5dc2f0376571e65325d8cfe9645d6b5d7"},
    {"path": "reports/round-17/civ/inuit.md", "sha256": "7241e6b48f1b3cb55b2f90f4af5918cd7f6e6adf12e4e162050b4c02036a10a5"},
    {"path": "reports/round-17/civ/maya-classic.md", "sha256": "535f47f4e8b3d1b873f4bf38609c13aa7f638e4ad0eea01f4b738970cc8dc9ea"},
    {"path": "reports/round-17/civ/mesoamerica.md", "sha256": "e4e546ab461c071e06099620655a78db78dd06deace8e2d42ec6d0d6b0033432"},
    {"path": "reports/round-17/civ/mongol.md", "sha256": "47ba5951db3662fa4a37cb793d9764e464932a45d58e18560ba4b2ac13ebc013"},
    {"path": "reports/round-17/civ/muisca.md", "sha256": "c671d29b041e80faade8f0655bbd36a7936ec373510cdcea4797a8edda76f1e7"},
    {"path": "reports/round-17/civ/persia-sasanian.md", "sha256": "1d536dcecbeba3015490a4ae871decd94a21e125b105f4806f4fc1d4ef6912a7"},
    {"path": "reports/round-17/civ/polynesia-navigation.md", "sha256": "02deda5b91dfc92dc80fb3d6c91b84a24f329fcd106dd20cb9caa49306132242"},
    {"path": "reports/round-17/civ/rapa-nui.md", "sha256": "f58f8af47f9ceaae0d4e1271116e922043948a0a49ab3eceb6dff92bac90609a"},
    {"path": "reports/round-17/civ/sed77.md", "sha256": "4b628f58991d69160f29ac1c169bb71212569e1c4507a005c39167c6a4fcfd63"},
    {"path": "reports/round-17/civ/sed78.md", "sha256": "ebf283ffd73f97cf61b485da43f0d95900415110015f06e748c428ab5f85862f"},
    {"path": "reports/round-17/civ/sed79.md", "sha256": "d5c3517d126dbe301cb80222666c2de638fdf7a92efa391bab64f74684ad0257"},
    {"path": "reports/round-17/civ/sed80.md", "sha256": "d4f1bd00045510a84ad5352defebf93b57989ee714b744d25929b7123782e054"},
    {"path": "reports/round-17/civ/map-patch.json", "sha256": "79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e"},
    {"path": "reports/round-17/civ/verify-1.md", "sha256": "ec27158f71630e5843b552f51e2e38235fc7ab641c7a3e10e8e35e1317c86388"},
    {"path": "reports/round-17/civ/verify-2.md", "sha256": "fb15616fe7465ab6a10309b8bb0ebe4973f3ca939ca475238e538c95e33b9452"},
    {"path": "reports/round-17/civ/v03-v04-never-swept-verify.md", "sha256": "97e7286fc35bc62dbe6f97ab46fe481306d9876484f76a198fda94db1e451edf"},
    {"path": "reports/round-17/scribe-1.md", "sha256": "b77bdf31e400966e84e6c1160b1f4bf90440adcf3ae204b849dab53aea05a8b2"},
    {"path": "corpus/lessons/round-17.md", "sha256": "5a226d39c32f7b3efa0c1c453062d4d4458f8eb53a67a7e6377cb75b05b1a39a"},
    {"path": "corpus/knowledge/civilizations/inuit.md", "sha256": "52c5a11b7b7db949f8f93da199a34a0062a888a180e021b2a124558480ef0c5d"},
    {"path": "corpus/knowledge/civilizations/maya-classic.md", "sha256": "d9608d842ccb97da3514032d41a323016dc65c0039ff6396d4f96b7678ce67b5"},
    {"path": "corpus/knowledge/civilizations/mesoamerica-primary-sources.md", "sha256": "d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530"},
    {"path": "corpus/knowledge/civilizations/mongol.md", "sha256": "e60b3903402034bcd897617fac589340fb9c70439a028583fbe193fec14c1163"},
    {"path": "corpus/knowledge/civilizations/muisca.md", "sha256": "417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064"},
    {"path": "corpus/knowledge/civilizations/persia-sasanian.md", "sha256": "20e7513e1f3b288e167f2cd56163caba2cbc238c92b0b6524b655a6f40ca7e2e"},
    {"path": "corpus/knowledge/civilizations/polynesia-navigation.md", "sha256": "a47639dc0774bd7c12782d61099ed07c14b3712d3092f76a1102cd7176bb5981"},
    {"path": "corpus/knowledge/civilizations/rapa-nui.md", "sha256": "c893805a82ed953c29a3f8a20472c6e0579119e7c59d6a3db9ee5e86fb2a0f57"},
    {"path": "corpus/knowledge/civilizations/rome.md", "sha256": "0b29e05c44f0a55e49b7f29ca787eea0809df2d80635e5677f0fa9becbcfe68c"},
    {"path": "corpus/knowledge/civilizations/ryukyu.md", "sha256": "424fcbb5de9f4d226039c7472f92372784801a128f62ee6024a71e590819afa5"},
    {"path": "corpus/knowledge/civilizations/scythian-saka.md", "sha256": "cb3a6428c4b174a4917871185e416f3ac7d3ecdf62a016432f87a486b3ab5c51"},
    {"path": "corpus/knowledge/civilizations/siam-thai.md", "sha256": "8bef2a5b3936c2f45d9d0027646e4d107d45b5f58942379cbb4db9fb7cb6c733"}
  ]
}
```

These are close-time pins on an in-flight tree. The ledger control (§5)
asserts every path exists and reports any hash mismatch as **DRIFT** (the file
changed after the pin — re-read it, do not trust the stale pin). At
integration the parent should re-pin the settled tree; this block is a
freshness map, not an acceptance record.

## 4. Cross-fragment ties (close-time observations)

1. **Hold set named pre-implementation (claim D condition).** Four independent
   design seats name hold sets before any D4 tree byte exists: D01
   `design-brief.md` (candidate hold set + 12-component registry), D04
   `design-costume.md` (costume slice holds), D02/D03
   `design-language.md`/`design-myth-era.md` (slice holds),
   `components/01-brief.yml` `contract.hold_set_declaration`, and D19
   `expected-holds.fragment.json`. The **equality leg** (gate findings ==
   expected set) still awaits the tree: `examples/culture-d4/` was absent at
   every poll.
2. **Typed pipeline is culture-bound (D18 finding).** `typed-support-1.md`
   reports the D2 projector hard-codes `LEX-GAR-[0-9]{2}` costume-slot regex
   and reads D2 rank/era legs at module level, so the D4 typed derivation
   needs adaptation, not a straight reuse. The D-typed seats own the fix; the
   D4 typed labels/projection were not on disk at close.
3. **C claim on disk looks complete; acceptance still parent-owned.** All 12
   round-16 stale entries have disposition fragments (12 files under
   `reports/round-17/civ/` + `map-patch.json` + 3 verifier receipts) and
   exactly the 12 named corpus entries are edited (`git status` 09:34:43Z —
   no other corpus path dirty). The mid-wave runner receipt measured C True
   at that time, but the runner and receipt were both later edited; the
   parent must re-run on the settled tree. `sed77.md` records an identity
   conflict (sed-77 prints persia-sasanian, which was excluded) resolved to
   `rome.md`; the C-verifier receipts should be checked against that choice.
4. **O claim partially verified.** The assembler landed mid-wave and this
   seat's ⟦IC⟧ selftest run passed 79/79 (09:34:32Z) — but the tool hash
   changed twice afterwards (still in-flight), and `--check` needs the D4
   tree. The d2/d3 assemblers remained byte-identical to baseline (13/13
   re-check at 09:32:27Z).
5. **Mid-wave receipt semantics.** `validation.json` acceptance False is a
   named-missing-dependency receipt (D4 tree + assembler absent at run time),
   not a claim failure verdict; its `runner_sha256` `9272173c…` no longer
   matches the current runner `4ac405ce…`. No acceptance inference may be
   drawn from it in either direction.
6. **Count calibration (60 vs 64).** Three independent seats derive 60 from
   `targets.json` against the declared 64 (X01 lessons, X02 scope F-X02-1,
   this ledger §2). Parent reconciles; none of us rewrites the declaration.
7. **Negatives are D2-derived fixtures.** `neg-1..3` state their fixtures are
   synthetic controls derived from filed D2 bytes. They demonstrate the
   pipeline's catch mechanics, not a D4-instance catch; the runner's D-claim
   legs are what grade the D4 instance.

## 5. Poll log and verification

Poll stamps (60s cadence; window T0 09:15Z → last 09:34:43Z; close sweep
09:35:34Z): T0 09:15Z (claims+targets only); T1 09:20:42Z (civ/inuit, civ/mongol,
scope); T2 09:21:46Z (muisca, neg-1, neg-2); T3 09:23:07Z (rapa-nui, sed80,
neg-3); T4 09:24:29Z (runner, typed-support 1–2, validation.json, maya-classic,
sed77); T5 09:25:52Z (mesoamerica, validation.json); T6 09:26:58Z (persia-sasanian,
design-brief); T7 09:28:22Z (design-costume, components/01-brief, report-draft,
sed78); T8 09:29:40Z (corpus 12/12 modified; sed79); T9 09:31:09Z
(polynesia-navigation, verify-1, components 02, design-language, design-myth-era);
T10 09:32:17Z (components 03; d2/d3 re-check 13/13 OK); T11 09:33:34Z
(assembler exists, components 04, expected-holds.fragment.json, verify-2,
v03-v04); T12 09:34:43Z (components 05, close sweep). All polls also swept
`examples/culture-d4` (0 files every time) and `tools/assemble-culture-d4.py`
(absent until T11).

Ledger verification control (stdout-only; existence asserted, drift reported):

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import hashlib, json, time
from pathlib import Path
text = Path('reports/round-17/scribe-2.md').read_text()
block = text.split('```json ledger', 1)[1].split('```', 1)[0]
rows = json.loads(block)['pins']
missing, drifted = [], []
for row in rows:
    p = Path(row['path'])
    if not p.is_file():
        missing.append(row['path'])
        continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if row.get('sha256') and h != row['sha256']:
        drifted.append((row['path'], row['sha256'][:16], h[:16]))
print('observed_at=' + time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
print('pins=' + str(len(rows)) + ' missing=' + repr(missing))
print('drifted=' + repr(drifted))
assert not missing, 'ledger pins missing paths'
if drifted:
    print('DRIFT: files changed after the close-time pin; re-read them (mid-wave edit, not a pin error)')
print('LEDGER_CONTROL=EXISTENCE_PASS')
PY
```

**Control executed (this seat):** at 2026-10-18T09:37:16Z the exact block
above ran (extracted from this file, `bash`, cwd = lane root), exit **0**:
`pins=52 missing=[]`; `drifted` named 6 in-flight files — `run-validation.py`,
`d4/design-myth-era.md`, `d4/design-costume.md`, `d4/typed-support-1.md`,
`d4/typed-support-2.md`, `tools/assemble-culture-d4.py` — all mid-wave edits
after the 09:35:34Z pin, reported not hidden. Re-run at integration on the
settled tree.

## 6. Status and handoff

Close status (2026-10-18T09:35:34Z): C-claim evidence is substantially on
disk (12/12 dispositions + verifier receipts + 12 corpus edits); D4 design
and 5/12 components plus typed-support contracts and the assembler are on
disk; **the D4 example tree itself, the D4 typed artifacts, components 06–12,
D-tests/D-review fragments, the frozen manifest, and a settled-tree
`validation.json` are not** — they remain for the still-running wave seats
and the parent. This ledger is an in-flight record, not the round-17
acceptance receipt; the parent must re-run
`python3 reports/round-17/run-validation.py` on the settled tree and re-pin
this block before LOG/SCORECARD integration. The polling cap (60s × 20 min)
ended this seat's dependency window at 09:35Z; it did not end the round.
