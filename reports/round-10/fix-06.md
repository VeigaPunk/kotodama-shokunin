# R10-O06 — findings fixer: tracker idx 4 (r8 S6) and idx 12 (r9 S4)

- shard: **R10-O06** (findings fixer, operability claim O), round 10 (loop 1 of 3, build 3 of 4), 2026-10-17
- baseline revision `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (round-10 declaration) with the round-10 wave in flight (peer fragments under `reports/round-10/`, new corpus entries, `SKILL.md`/`corpus/README.md`/`reports/round-8/run-validation.py`/`reports/round-9/validation.json` modified by peer workers — none of it mine)
- tracker read: `reports/round-10/findings-tracker.json`, sha256 `151217d7fd98965f8f7225de5c91d4b100e89eea3aa2289e8fb0de10b0dcb5ff`, compiled 2026-10-17T21:27Z by R10-O01
- rows fixed here: **idx 4** = `reports/round-8/depth/findings.md` **S6** (medium) and **idx 12** = `reports/round-9/d3/findings.md` **S4** (low; documented design, residual only)
- write discipline: **this file is the only write**. All controls ran on copies under `.scratch/fix06/` (`export TMPDIR=$PWD/.scratch` per dispatch; shared `/tmp` inode-exhausted). No shared file was edited — per `AGENTS.md` ("workers never race to append shared bookkeeping") the tracker rows are patched by the scribe from §3 below.

---

## 1. idx 4 — r8 S6 "a supplied `native_form` on a costume record is still not read" — disposition: **wrong**

Tracker row (verbatim core): *"a supplied native_form on a costume record is still not read at 3548185c: injecting native_form: \"vinter\" into GAR-01 leaves the projection unchanged (the only native-form sources are the lexicon and the unresolved form slots); design-spec.md §1.3 R1/R4 and §1.2 L2 assume a supplied native_form is read. Either implement it or record in the spec that D2 has no supplied-native-form channel."*

**Verdict: the observation reproduces (Control A) but the defect claim and its premise are wrong.** The spec never declares a record-level `native_form` channel; the supplied-native-form capability has a declared input path (the typed-label record of §1.2) and the delivered tool reads it — demonstrated live on the delivered revision **and on the reviewer's own newest-tested revision `e9209f28`**.

Evidence:

1. **The spec bytes are unchanged since the review, and they never declared the field the probe injected.** `sha256sum reports/round-8/depth/design-spec.md` → `84e4b4c1…4cc751` = D16's own pin (`findings.md:7`) = `git show e1694ba:reports/round-8/depth/design-spec.md | sha256sum` = live. In those exact bytes, §1.5 (`design-spec.md:231`) states every GAR record carries "an English `garment` string, a `form_slot` (LEX-GAR-01..10), and **no `native_form`**", and §1.2 (`:107-126`) defines the label record shape where a supplied form lives: `kind: native-form` + `status: supplied`. R1/R4 (§1.3, `:152-171`) are rules over *label records* ("`native-form` + `status: supplied` ⇒ this text is the only checked sound/identity form"), not over component fields. The probe injected an undeclared field.
2. **The declared channel existed at the reviewer's newest-tested revision.** The reviewer's own mirror (`/home/vgpnk/.r8d16/mirror3/tools/d2-typed-labels.py`, sha256 `e9209f280c6d…f4a282`, matching their ledger stamp `e9209f28`) contains the channel: `:594-598` ("Explicit `typed_labels` entries pass through unchanged; they are the channel the malformed controls and hand-authored labels use") and the hold-lift at `:768-777`. Their earlier mirrors (`mirror/` `1756e8c0`, `mirror2/` `623b5b1f`) contain **0** occurrences of `typed_labels` — the channel entered during the final rewrites. Their probe `probes2.py` mutated `mirror2/examples/culture-d2/components/11-costumes.yml` (a component file), i.e. it tested the one path the spec does not define.
3. **Controls (live, this shard):**

| # | what | command | observed |
|---|---|---|---|
| baseline | delivered tool on the real packet | `python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --json` | exit 1; `stats {fail:0, hold:15, labels:58, note:1}`; `D2L-FORM-UNRESOLVED` hold on GAR-01 |
| A | the D16 probe shape: `native_form: "vinter"` injected into the GAR-01 **record** of a packet copy (`packet-A-field.yml`, sha256 `c2754899…2785ba`) | same tool on the copy | **identical finding set to baseline** (exit 1, same counts; GAR-01 still held; the only doc-level diff is the `packet` path field). Correct behavior: an undeclared field is ignored, fail-closed (§1.5) |
| B | the **declared channel**: one explicit typed label `TL-GAR-01` (owner `11-costumes`, `label_id LEX-GAR-01`, `kind native-form`, `status supplied`, `text "vinter"`) appended as a `typed_labels:` block (`packet-B-label.yml`, sha256 `b4c59346…5e02a8`) | same tool on the copy | exit 1; `labels 59`, `fail 2`; **GAR-01 hold gone** (R3 resolved by the supplied form) and `D2L-NATIVE` FAIL ×2 — `supplied form 'vinter' carries symbols outside the declared inventory: ['v']` (R1/R4: native bytes govern and are checked) |
| C | same packet on the **reviewed revision** — the reviewer's own `e9209f28` file, copied to `.scratch/fix06/oldrun/tools/` with a self-contained tree (their `ROOT` is `__file__`-relative) | `python3 .scratch/fix06/oldrun/tools/d2-typed-labels.py --packet …/packet-B-label.yml --json` | exit 1; `labels 59`, `fail 2`; GAR-01 hold gone; identical `D2L-NATIVE` FAIL ×2. **The channel was live at `e9209f28`.** |
| D | §1.2 **L2**: a second supplied native form for the same slot (`packet-D-two.yml`, sha256 `75248eb2…a04ccb`) | same tool on the copy | exit 2; `D2L-DATA` — `two supplied sound forms on one record (11-costumes LEX-GAR-01): identity collision`. L2 is enforced through the same channel |

   Supporting: `python3 tools/d2-typed-labels.py --selftest` → `39/39 checks passed`, exit 0 (includes the L2 probe control at tool `:2739`).

**Limits.** The exact revision the finding measured (`3548185c`, a worktree stamp) is not in git history and not in the reviewer's mirrors (only `1756e8c0`/`623b5b1f`/`e9209f28` exist), so I cannot re-run it; the delivered revision is what a round-10 disposition must address, and it is contradicted by Controls B–D. If the channel was absent at `3548185c`, the subsequent rewrite closed it by construction; the finding's blanket claim ("the only native-form sources are the lexicon and the unresolved form slots") was already false at `e9209f28`. The design question the reviewer themselves left open (`findings.md:133`) is out of this row's scope. A tool-side wart surfaced by Control B is recorded as adjacent A3.

## 2. idx 12 — r9 S4 "the freeze document is unpinned by construction" — disposition: **fixed-with-control**

Tracker row (verbatim core): *"…expected.json excludes itself from its own manifest … so nothing in-tool witnesses an in-place edit of expected_exit/finding_ids/manifest entries — only git and the round receipts do. Recommend the D12 ledger (or admission receipt) carry the freeze's sha256 pre/post re-pin (anchors: 74496aa8.../blob c420ac4c...)."*

**Verdict: the actionable recommendation is implemented and demonstrated; the stated design property remains by design (the finding itself labels it "documented design, residual only").**

Evidence (the pre/post pair now lives in durable round-9 records):

1. **Pre-refresh anchor in the D12 ledger.** `reports/round-9/d3/scribe.md:208-216` carries the pre-refresh freeze token `sha256 74496aa8…` and git blob `c420ac4c…`, and states verbatim: *"This ledger carries the pre-refresh anchor (D09 S4 requests exactly that); the post-refresh `expected.json` sha256 must be recorded at admission."* — the recommendation is tracked by its own ID.
2. **Post-refresh anchor in the admission record.** `reports/round-9/validation.json:24` (`claims.D.measurement.expected_sha256`) and `:991` (`input_sha256["examples/culture-d3/expected.json"]`) both carry `562b76cb…90fc`; the file was committed in the round-9 admit commit `9dc18ec` ("frozen replay 0 findings after legitimate re-pin of 3 round-8 drifted pins").
3. **The pair brackets the actual bytes, asserted by command** (exit 0, prints `all three equal: True`):

```sh
git show 57c3ce6:examples/culture-d3/expected.json | sha256sum     # 74496aa8…90fc  (pre-re-pin bytes)
sha256sum examples/culture-d3/expected.json                        # 562b76cb…90fc  (live)
python3 -c "import json,hashlib;d=json.load(open('reports/round-9/validation.json'));rec=d['claims']['D']['measurement']['expected_sha256'];inp=d['input_sha256']['examples/culture-d3/expected.json'];live=hashlib.sha256(open('examples/culture-d3/expected.json','rb').read()).hexdigest();print(rec,inp,live,rec==inp==live)"
```

4. **The frozen leg is green at the recorded pair**: `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` → `{"counts": {"total": 0}, "exit": 0, "findings": []}`, exit 0; `git log --oneline -1 -- examples/culture-d3/expected.json` → `9dc18ec`.

**Limits.** The in-tool gap (self-exclusion) is not fixable without breaking the freeze's own design; per the row's own severity ("documented design, residual only") the external anchor is the correct control. Residual evidence hygiene issue found while verifying: the D3 docs still print the pre-re-pin token — adjacent A1.

## 3. Tracker row patch (for R10-O14 scribe — the tracker itself was not edited by this shard)

```json
[
  {"idx": 4,  "disposition": "wrong",
   "disposition_evidence": "reports/round-10/fix-06.md §1 — premise false at the reviewer's own newest-tested revision e9209f28 (Control C) and at the delivered revision 0da0015f (Controls B/D); the injected native_form is an undeclared record field (design-spec.md §1.5, bytes unchanged 84e4b4c1); the declared typed-label channel is read and enforces R1/R3/R4 + L2"},
  {"idx": 12, "disposition": "fixed-with-control",
   "disposition_evidence": "reports/round-10/fix-06.md §2 — pre-refresh token in reports/round-9/d3/scribe.md:208-216, post-refresh token in reports/round-9/validation.json:24,991 (admit commit 9dc18ec), live bytes = recorded value, frozen replay exit 0 / 0 findings"}
]
```

## 4. Adjacent observations (outside idx 4/12; for the drift sweep / scribe)

- **A1 — stale freeze tokens in the D3 docs after the re-pin.** `examples/culture-d3/README.md:34,91` and `handoff.md:65,242,278` still print `74496aa8…` as the freeze digest while the live freeze is `562b76cb…` (verified: `grep -n '74496aa8' examples/culture-d3/README.md examples/culture-d3/handoff.md`; `sha256sum examples/culture-d3/expected.json`). Both files were last touched by `57c3ce6` and were not re-dated at the re-pin (`git log --oneline -1 -- examples/culture-d3/README.md examples/culture-d3/handoff.md` → `57c3ce6`), although the round-9 scribe listed exactly that action for the re-pin (`reports/round-9/d3/scribe.md:198`). The docs are freeze-excluded, so the guard never sees this. Not covered by any tracker row.
- **A2 — pre-existing red at HEAD: `python3 tools/d2-typed-labels.py --check` exits 1** — `examples/culture-d2/typed-labels.d2.yml differs from the deterministic projection`; the sole diff line is `packet_sha256` `8da90b07…b81e` (artifact `:9`) vs `e0f21509…b643` (live packet; live == `HEAD:` bytes). The pair was already inconsistent in the admit commit `e1694ba` (packet re-pinned in that commit, artifact not re-emitted; `git show e1694ba:examples/culture-d2/typed-labels.d2.yml | sed -n 9p`). Round-8's runner checks only `--selftest`, so this check has no covering row.
- **A3 — duplicate `D2L-NATIVE` emission.** A supplied sound label paired with a translated label on the same record is checked twice (Control B/D outputs show `TL-GAR-01` twice with identical detail) — cosmetic count inflation, visible only when the channel is used.
- **A4 — Control A reproduces the D16 observation exactly** (record-level `native_form` ignored) — correct per §1.5, recorded here so the observation is not lost.

## 5. Reproduction (all commands from the lane root; scratch in-lane)

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch && mkdir -p .scratch/fix06
# mirrors A/B/D — exact build (python; expected shas A c2754899…, B b4c59346…, D 75248eb2…):
python3 - <<'PY'
import pathlib
text = pathlib.Path('examples/culture-d2/packet.d2.yml').read_text(encoding='utf-8')
anchor = '    form_slot: "LEX-GAR-01, the valley grade of L35 mirken (to-verify with 05-lexicon)"\n'
assert text.count(anchor) == 1
label = ('\ntyped_labels:\n  -\n    id: "TL-GAR-01"\n    owner: "11-costumes"\n'
         '    label_id: "LEX-GAR-01"\n    kind: "native-form"\n    text: "vinter"\n'
         '    script: "Latn"\n    representation: "editorial-romanization"\n'
         '    scheme: "d2-roman"\n    status: "supplied"\n    era_ids: [E0]\n'
         '    register: "everyday"\n    evidence: "design-choice"\n')
two = label + ('  -\n    id: "TL-GAR-01b"\n    owner: "11-costumes"\n'
               '    label_id: "LEX-GAR-01"\n    kind: "native-form"\n    text: "mirken"\n'
               '    script: "Latn"\n    representation: "editorial-romanization"\n'
               '    scheme: "d2-roman"\n    status: "supplied"\n    era_ids: [E0]\n'
               '    register: "everyday"\n    evidence: "design-choice"\n')
p = pathlib.Path('.scratch/fix06'); p.mkdir(parents=True, exist_ok=True)
(p/'packet-A-field.yml').write_text(text.replace(anchor, anchor + '    native_form: "vinter"\n', 1), encoding='utf-8')
(p/'packet-B-label.yml').write_text(text + label, encoding='utf-8')
(p/'packet-D-two.yml').write_text(text + two, encoding='utf-8')
PY
python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --json          # baseline
python3 tools/d2-typed-labels.py --packet .scratch/fix06/packet-A-field.yml --json         # A
python3 tools/d2-typed-labels.py --packet .scratch/fix06/packet-B-label.yml --json         # B
python3 tools/d2-typed-labels.py --packet .scratch/fix06/packet-D-two.yml --json           # D
# C — the reviewed revision, self-contained:
cp /home/vgpnk/.r8d16/mirror3/tools/d2-typed-labels.py .scratch/fix06/tool-e9209f28.py
mkdir -p .scratch/fix06/oldrun/tools/gates .scratch/fix06/oldrun/examples/culture-d2
cp .scratch/fix06/tool-e9209f28.py .scratch/fix06/oldrun/tools/d2-typed-labels.py
cp tools/gates/costume-era-consistency-gate.py .scratch/fix06/oldrun/tools/gates/
cp -r examples/culture-d2/components .scratch/fix06/oldrun/examples/culture-d2/components
cp .scratch/fix06/packet-B-label.yml .scratch/fix06/oldrun/examples/culture-d2/
python3 .scratch/fix06/oldrun/tools/d2-typed-labels.py --packet .scratch/fix06/oldrun/examples/culture-d2/packet-B-label.yml --json
# S4 controls: see §2 block; A1/A2 receipts: see §4
```

Captured outputs (sha256; regenerated 2026-10-17 from the exact commands above, repo root): `out-current-baseline.json` `880d0e45…`, `out-current-A-field.json` `3967a1f6…`, `out-current-B-label.json` `4435b10f…`, `out-current-D-two.json` `fe615e80…`, `out-old-B-label.json` `b0705d1c…`, `regen.yml` `a3aa452c…` (all under `.scratch/fix06/`). Content spot-check after regeneration: baseline/A = 10 holds incl. GAR-01; B/old-B = 9 holds, GAR-01 absent, 2 × `vinter` D2L-NATIVE; D = 1 × `D2L-DATA` collision, exit 2.

## 6. Limits and self-disclosure

- The `3548185c` revision is unavailable (worktree stamp; no mirror, no git object) — Control C substitutes the reviewer's own newest-tested `e9209f28`.
- Running the old tool required a self-contained tree under `.scratch/fix06/oldrun/` because its `ROOT` is `__file__`-relative (`tool-e9209f28.py:2197`); nothing outside the repo was written.
- All my writes are under `.scratch/fix06/` and this file; the worktree dirt listed in the header belongs to peer round-10 workers.

FILES: reports/round-10/fix-06.md | SUMMARY: Dispositioned tracker idx 4 (r8 S6) as **wrong** — the injected record-level `native_form` is an undeclared field (spec §1.5 unchanged since review) while the declared typed-label channel is read and enforces R1/R3/R4 + L2, demonstrated on the delivered revision and on the reviewer's own newest-tested `e9209f28` (Controls A/B/C/D) — and tracker idx 12 (r9 S4) as **fixed-with-control**: the pre-re-pin token `74496aa8` sits in the round-9 D12 ledger and the post token `562b76cb` in the admit record `validation.json` (commit `9dc18ec`), asserted equal to live bytes with the frozen replay green; adjacent observations filed for the scribe/drift sweep (stale `74496aa8` tokens in `examples/culture-d3/README.md`/`handoff.md`; pre-existing `d2-typed-labels --check` red at HEAD; duplicate `D2L-NATIVE` emission), with a ready tracker-row patch in §3.
