- Seat: A09 | executor | A | date 2026-10-19 | baseline 139e3b6

# A09 — pin-cascade exposure: lessons README and SKILL.md shared-file drafts

**Assignment** (`reports/round-33/targets.json:56`): "Pin-cascade exposure: if the
integrator applies the O/C shared-file drafts (lessons README, SKILL.md lines), which
frozen baselines/pins reference them; re-pin needs listed per X00's matrix."

**Method.** Enumerate every artifact class in this lane that *pins* a file (frozen
`MANIFEST.tsv` rows, `expected.json` baselines under the three battery roots, digest
maps in filed receipts, hard-coded blob/digest constants in filed tools and runners,
live readers, and line-number anchors), then decide for each class whether the declared
O/C edits move it. No file was written outside this fragment; every command below is
read-only.

**Measurement window:** 2026-10-19T03:50Z–04:0xZ, lane HEAD `139e3b6`
(`git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`), env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Files at stake:
`corpus/lessons/README.md` (346 lines, sha256 `ec7469da…`, git blob `a3187055…`) and
`SKILL.md` (715 lines, sha256 `79fe91d3…`) — measured this window, equal to the
digests A10/A13 recorded.

**Verdict:** **GREEN on the frozen surface; three named non-frozen exposures with
owners.** No frozen manifest row or baseline needs a re-pin. The cascade that does
exist is in (E1) a hard-coded blob pin inside round-26's runner, (E2/E3) recorded
digests and the box-1 re-survey obligation, and (E4) line-number anchors — the O/C
edits move those, and each needs a *new* record, never an edited one.

## 1. Pin surface inventory — what actually pins what

| class | artifact | pins | does the O/C edit move it? |
|---|---|---|---|
| frozen manifest rows | 11 `MANIFEST.tsv` under `tools/gates/frozen/**` | gate script digests + culture packet inputs | **no** — zero rows name the README or SKILL.md |
| baselines | 20 `expected.json` under `tools/gates/expected/**`, `tools/gates/frozen/**`, `reports/round-9/baselines/**` | gate script + `packet.yml`/`packet.md`/`examples/culture-d{2,4}/**`/`tools/d2-typed-labels.py` | **no** — no `inputs` map names either file |
| frozen text copies | 4 files under `tools/gates/frozen/**` | — (path strings only) | **no** — and their lessons digests still reproduce (§1.2) |
| runner blob pin | `reports/round-26/run-validation.py:97` | `corpus/lessons/README.md` git blob `a3187055…` | **YES — E1** |
| seat-tool blob pin | `reports/round-26/lessons/c51-revision-audit.py:48` | same blob | **YES — E1** |
| receipt digest maps | `reports/round-25/validation.json:1020`; `reports/round-3{1,2}/validation.json`; 10+ more (§2.2) | README / SKILL.md sha256 | **YES — E2** (stale readings) |
| live readers | `reports/round-30/craft/box1-survey.py:5,10` (SKILL.md); `reports/round-25/audit/c31-lessons-index-audit.py:36` (README) | self-reported digest, no assertion | **YES — E3** (new receipt owed) |
| line anchors | `AGENTS.md:42`; `SKILL.md:149,183` (self-cite `:47`); ~15 filed lesson citations (§2.4) | line numbers in a mutable file | **YES — E4** |
| in-file pins | README §2 rows (26 × `bytes/lines/sha8`), §1 `:97`, §4 `:207` prose arithmetic | live lesson bytes | **satisfy, not break — E5** |

### 1.1 Frozen gate surface — zero exposure (confirms A10's provisional row)

- `grep -rn "lessons/README\|SKILL.md" tools/gates/frozen/*/MANIFEST.tsv tools/gates/frozen/*/*/MANIFEST.tsv` → **0 hits** across all 11 manifests (the two globs cover every `MANIFEST.tsv` in the tree: round-3, round-11, round-18, round-3/attempt-1, round-18/repin-d2, round-20/repin-d2, round-22/d4-repin, round-23/repin-d2, round-25/gate-input, round-26/gate-input, round-26/post-register).
- Enumerating every baseline's `inputs` map (python one-liner over all `expected.json` under the three roots) → **20 baselines**, every `inputs` key a gate script, `packet.yml`/`packet.md`, `examples/culture-d{2,4}/**`, or `tools/d2-typed-labels.py`. None names `corpus/lessons/README.md` or `SKILL.md`. This matches the battery's own reading (`baselines_found 20, pinned 20`, `reports/round-33/op/O07-baseline-receipt.md:38-45`).
- `SKILL.md` appears under `tools/gates/frozen/**` only as *prose inside immutable snapshot copies* — `tools/gates/frozen/round-3/{,attempt-1/}inputs/corpus/knowledge/verification/gate-frozen-run-standard.md:5,15,28,243`, `tools/gates/frozen/handoff-packet-check/r9-pre/freeze.txt:2,110` — never as a pinned path or digest.

### 1.2 The only frozen artifacts that mention the lessons partition still reproduce

`grep -rl "corpus/lessons" tools/gates/frozen/` → 4 files: `handoff-packet-check/{r9-pre,r18-post}/packet.md` (`:48`, `:69-72`) and `provenance-audit/{r9-pre,r18-post}/inputs/corpus/knowledge/verification/provenance-audit-ledger-format.md:14`. All are path strings inside frozen copies; the four source-ledger digests at `packet.md:69-72` are digests of `corpus/lessons/round-6-sources/{05,03,13,09}.json`, and all four **reproduce exactly** at HEAD (`a00a5dc4…`, `adb22c9a…`, `69504356…`, `0dd2820d…`). No action; the O/C edits do not touch this partition (source ledgers ≠ the index).

## 2. Cascade verdict per shared file

### 2.1 E1 — the README is pinned by *blob* inside round-26's runner (highest severity)

- `reports/round-26/run-validation.py:96-97` — `LESSONS_README = "corpus/lessons/README.md"`; `README_BASELINE_BLOB = "a31870556c733498243b56697896504a2fb3679a"`.
- `:1494-1500` — if the filed blob differs, the claim fails with "the filed lessons index was edited in place (blob … != declared baseline …); the claim requires a new revision file, not an in-place edit".
- `:1503-1510` — the claim also requires a new revision file under `reports/round-26/`.
- The same pin is mirrored in the filed seat tool `reports/round-26/lessons/c51-revision-audit.py:48,199-203` (`C52-7_filed_unchanged`) and stated as convention in `reports/round-26/zzz-lessons-index-revision-4.md:17-19` ("`corpus/lessons/README.md` is a **filed** artifact and no byte of it was touched").
- Measured now: `git hash-object corpus/lessons/README.md` → `a31870556c733498243b56697896504a2fb3679a` (= `git rev-parse HEAD:corpus/lessons/README.md`), so the pin holds at baseline and **only** moves if the integrator edits the README.

**Why this is a real trade, not a formality.** Claim O's `after_required` demands the README itself carry 33/33 rows (`reports/round-33/claims.json:29`) and its counting command is `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`, whose `INDEX` is hard-coded to `corpus/lessons/README.md` (`reports/round-25/audit/c31-lessons-index-audit.py:36`). So a revision-file-only approach (the r25/r26 pattern: revisions 3–4 under `reports/round-26/`) cannot satisfy the declared counting command, while an in-place edit satisfies c31 and supersedes the r26 blob pin. The integrator must pick one and record it.

**Re-pin need (E1):** a new dated supersession record under `reports/round-33/` naming old blob → new blob, the new sha256, the c31 after-state, and the reason an in-place edit was chosen over a revision; plus a standing rule that round-26's runner is **not** re-run at the round-33 revision. Do **not** re-run `reports/round-26/run-validation.py` without `--check`: `:90` sets `OUTPUT = f"{ROUND_DIR}/validation.json"` and `:1909` writes it (default mode), i.e. a re-run rewrites a filed `validation.json` in place — the same class of in-place filed-byte write already observed this round on `reports/round-5/validation.json` and `reports/round-7/validation.json` (`reports/round-33/op/O07-baseline-receipt.md:147-181`).

### 2.2 E2 — recorded digests become stale readings (new records owed, never edits)

| digest | recorded at |
|---|---|
| README `ec7469da…` | `reports/round-25/validation.json:1020`; `reports/round-26/audit/x63-lessons-receipt.json:75`; `reports/round-25/lessons/C35-C36.md:156,229`; `reports/round-26/lessons/C53.md:144,283,351`; `reports/round-26/scribe/fragment-ledger.json:401`; `corpus/lessons/round-28.md:86` |
| SKILL.md `79fe91d3…` | `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`; `reports/round-32/dossier-d11-shonen-boxes.md:50,205`; `reports/round-32/dossier-d12-capability-inventory.md:97`; `reports/round-32/dossier-d13-operator-decisions.md:48`; `reports/round-32/final-dossier.md:46,133`; `reports/round-32/scribe/fragment-ledger.md:178,235` |
| SKILL.md earlier `83b0a78a…` | `reports/round-30/craft/box1-landed-survey.json:4`; `reports/round-30/validation.json:449` |

All are filed, read-only bytes. **Re-pin need (E2):** after the edits land, the integrator files a new receipt naming the new digests; every listed row above is then a *superseded reading* (the x61 classifier's `supersession`, `reports/round-27/audit/x61-pin-sweep.py:186-197`), not a tamper finding and not something to repair in place.

### 2.3 E3 — SKILL.md's live re-survey obligation (box-1)

- `reports/round-30/craft/box1-survey.py:5,10` reads `SKILL.md` at run time and emits `skill_sha256`; exit 0 iff every `tools/*.py` path named in SKILL.md resolves. Last filed receipt: `reports/round-30/craft/box1-landed-survey.json:4-6` → `83b0a78a…`, `named_in_skill 28 / resolvable 28`.
- `reports/round-30/run-validation.py:697-700` makes "a dated receipt pinned to the post-landing SKILL.md bytes" a claim requirement and records `skill_sha256` in the measurement.
- The round-32 dossier closes box-1 condition 1 at `79fe91d3…` (`reports/round-32/final-dossier.md:46`).

**Re-pin need (E3):** a **new** box-1 re-survey receipt after the SKILL.md edit, pinned to the new bytes (re-run `python3 -B reports/round-30/craft/box1-survey.py`, file the output as a new file — `box1-landed-survey.json` is filed and is not edited). If the C14 drafts change the *set* of `tools/*.py` paths named in SKILL.md, `named_in_skill` moves off 28 and the new receipt must carry the new count; the r32 condition-1 closure at `79fe91d3…` reads as superseded, not falsified.

### 2.4 E4 — line anchors: the cascade proper

Measured SKILL.md addresses at HEAD: 715 lines total; `## Checklist (executable where a tool exists)` heading `:522`, last content line `:534`, `:535` blank, `:536` `## Corpus map`; `## Source-bounded culture drill — D3 (round 7)` `:660`; the r31-landed checklist item `:713-715` (end of file).

- **Live anchor:** `AGENTS.md:42` — "### 2.2 `SKILL.md` — append one item to "## Checklist (executable where a tool exists)" (after :534)". Committed at HEAD (blob `959acccc…`, working tree identical: `git diff --stat -- AGENTS.md` empty, sha256 `1afaf106…`), so this is a *live* line-number instruction on a mutable file. Its own target is already 179 lines off (`corpus/lessons/round-32.md:33`: the item landed at `:713-715` while the section is `:522-534`).
- **In-file self-citation:** `SKILL.md:149` and `SKILL.md:183` cite `SKILL.md:47`. The C14 fix targets (`:486`, `:488`, `:501`, `:128` — `reports/round-32/final-dossier.md:46`) sit between `:47` and `:534`, so a line-count-changing edit at those lines shifts the `:534` anchor and the `:713-715` item's address, while an insertion above `:47` would additionally shift the two self-citations.
- **Filed citations that shift with any line-count delta below them:** `corpus/lessons/round-31.md:46` (`:294`, `:456-458`, `:522`, `:534`, `:535`, `:536`); `corpus/lessons/round-32.md:7,33,41,55,57,58` (`:710`, `:713-715`, `:660`, `:522-534`, `:294`); `corpus/lessons/round-25.md:44` (`:189-214`); `corpus/lessons/round-19.md:88,100,101,179` (`:278`, `:323-375`, `:262-278`); `corpus/lessons/round-15.md:25` (`:157`, `:205`); `corpus/lessons/round-14.md:141` (`:208`).
- **corpus/knowledge entries with a SKILL.md dependency and an explicit recheck trigger** (section-name, not line — safe under a same-section edit, but the trigger fires): `corpus/knowledge/synthesis/typed-label-routing-workflow.md:6,19`; `corpus/knowledge/verification/label-channel-routing-verification.md:6,17`; `corpus/knowledge/verification/verification-method-overview.md:9`; `corpus/knowledge/verification/gate-frozen-run-standard.md:5`.

**Re-pin need (E4):** apply every SKILL.md draft as a **line-count-neutral in-place replacement** (same line replaced, no insertion/deletion). Control after the edit: `git diff --numstat -- SKILL.md` shows equal added/removed counts and `wc -l SKILL.md` still reads 715. If the integrator accepts a line-count delta instead, the record must state the shift and every citation above the change point becomes a stale reading requiring a new dated record (filed bytes are never edited).

### 2.5 E5 — README-side pins the drafts must satisfy (not break)

- The README is itself a pin carrier: §2 carries 26 rows with `bytes/lines/sha8` cells; c31's C34/C34c re-derive them (`reports/round-25/audit/c31-lessons-index-audit.py:51,53`) and both PASS at HEAD (measured). New rows must carry cells re-measured from live bytes (K02/O01 own the measurements).
- C34b FAILs at HEAD, measured: `{'stated': [26, 26], 'measured': [26, 33]}`. The two prose sites are `corpus/lessons/README.md:97` ("**Rows: 26. Files: 26.**") and `:207` ("Rows: **49**. Of the 26 index rows, **23 carry at least one question**"). Note the `49` is the **queue** count, a different declared value that round-25's runner regex reads globally (`reports/round-29/recount/r25-1.md:22`) — the edit must re-derive the row/file counts without disturbing the queue arithmetic's meaning.
- Peer instruments: `x45` (`reports/round-25/audit/x45-lessons-pointer-audit.py:178-179`) is **red at HEAD** (exit 1, `X45-P1 unresolved-pointer`: the round-4 row's `reports/round-4*` glob) — a baseline state, so not a round-33 regression, but if the O02 delta does not repoint that row the round carries the red as a named finding. `x57` (r27/r28) `--selftest` is **34/37 at HEAD**: three historical partition controls baked at the round-27/28 tree fail now (`partition is 27 md files` observed 33; `filed orphan is exactly round-26.md` observed the 7 orphans; `revision has no orphan` observed 6). No round-26..32 runner re-runs x57 (`grep … reports/round-2[6-9]/run-validation.py reports/round-3[0-2]/run-validation.py` → 0 hits), so it is not on a live surface — but nobody may quote `x57 --selftest` as a green instrument at HEAD.
- **Stamp hazard:** the partition is 33 `*.md` at HEAD (`ls corpus/lessons/*.md | wc -l` → 33). If `corpus/lessons/round-33.md` lands *after* the reconciliation stamp, C31-1 re-opens with exactly one orphan; land the round-33 lesson and its README row in the same edit, or file a dated follow-up row.

## 3. Re-pin needs — the deliverable list

| # | artifact to re-pin / re-issue | action | owner |
|---|---|---|---|
| R1 | `corpus/lessons/README.md` blob pin (`reports/round-26/run-validation.py:97`) | new dated supersession record (old blob `a3187055…` → new), stating in-place vs revision choice; never re-run the r26 runner without `--check` | integrator |
| R2 | README sha256 receipts (6 sites, §2.2) | new receipt naming the new digest; listed rows read as superseded | integrator |
| R3 | SKILL.md sha256 receipts (8 sites, §2.2) | same | integrator |
| R4 | box-1 re-survey (`reports/round-30/craft/box1-survey.py`) | re-run at the new SKILL.md bytes, file a **new** receipt (`named_in_skill` may move off 28) | integrator |
| R5 | SKILL.md line anchors (`AGENTS.md:42`; self-cites `:149,:183`; filed lesson citations §2.4) | keep the edit line-count-neutral (`git diff --numstat -- SKILL.md` equal; `wc -l` = 715), or record the shift and re-issue the anchor | integrator (C14 draft owners supply the before/after text) |
| R6 | README prose arithmetic (`:97`, `:207`) and new rows' `bytes/lines/sha8` cells | re-derive at the edit stamp; c31 full run must read exit 0, 33 == 33, `findings: 0` | integrator (O01/O02/K02 measurements) |
| R7 | x45 `X45-P1` and x57 historical controls | carry as named findings if not fixed by the O02 delta; do not cite as green | integrator + A10/A15 |
| R8 | README rows vs `round-33.md` landing order | land lesson + row in one edit, or file the follow-up orphan row | integrator + round-33 scribe |

None of R1–R8 is a frozen-baseline re-pin: the frozen gate surface (§1.1) is untouched, so no `MANIFEST.tsv` row, `expected.json`, or `freeze-receipt.json` needs a new generation this round.

## 4. Named findings with owners

| id | finding | class | owner | evidence |
|---|---|---|---|---|
| **A09-F1** | The README is pinned by git blob inside round-26's runner; claim O's after-state (README carries 33/33, c31's `INDEX` hard-coded to the README) necessarily supersedes that pin. Silent handling would leave an admitted round's runner red at HEAD with no record. | real finding — pin cascade | integrator | §2.1 commands; `reports/round-26/run-validation.py:97,1494-1500`; `reports/round-25/audit/c31-lessons-index-audit.py:36` |
| **A09-F2** | Re-running `reports/round-26/run-validation.py` (default mode) rewrites the filed `reports/round-26/validation.json` in place; the same failure mode already fired this round on rounds 5 and 7. | real finding — filed-byte hazard | integrator + A03/X02 | `reports/round-26/run-validation.py:90,1871,1909`; `reports/round-33/op/O07-baseline-receipt.md:147-181` |
| **A09-F3** | `AGENTS.md:42` carries a live SKILL.md line anchor (`after :534`) that is (a) already 179 lines off and (b) shifted by any line-count-changing SKILL.md edit. | real finding — line anchor | integrator | §2.4; `corpus/lessons/round-32.md:33`; `git diff --stat -- AGENTS.md` empty |
| **A09-F4** | `x57 --selftest` reads 34/37 at HEAD (three partition controls baked at r27/r28); `x45` reads exit 1. Neither is on a live round-33 surface, but both are quotable-as-green instruments unless named. | drift, no action | A15/A10 + integrator | §2.5; command outputs |
| **A09-F5** | The declared SKILL.md fix targets (`:486/:488/:501/:128`) sit between the `:47` self-citations and the `:534` checklist anchor, so the drafts' line behaviour decides whether R5 is a no-op or a re-issue. C14's drafts were not on disk at this seat's reads. | procedural / owed | C14 draft owner + integrator | `reports/round-32/final-dossier.md:46`; `ls reports/round-33/calib/` |

## 5. Reconciliation with A10's provisional row and with X00

- A10's row (written before any A-fragment existed) reads "A09 … **GREEN** — zero digest-pin exposure; no re-pin owed" (`reports/round-33/adj/A10-receipt.md`, §1) and explicitly conditions it on "to be re-confirmed against X00's collision matrix once it lands". Per A10's own A10-F5 rule, a landed fragment wins over that row: the **frozen-surface** half is confirmed exactly (§1.1–1.2), and the **full** verdict adds E1–E5 with findings A09-F1..F5 and the R1–R8 re-pin list. The integrator should carry A10's A09 row as errata, not as a second vote.
- X00's collision matrix (`reports/round-33/cross/X00-connector.md`) was **not on disk** at every read this seat made (`ls reports/round-33/cross/` → empty, 03:50Z–04:0xZ). R1–R8 are therefore keyed to the artifact classes measured here; when X00 lands, each R-row must be matched to X00's row for the same artifact and any X00 row with no counterpart here must be answered explicitly.

## Owed

- `reports/round-33/cross/X00-connector.md` — X00's collision matrix / pin-cascade exposure list is the mission's named cross-reference ("re-pin needs listed per X00's matrix") and had not landed at this seat's reads (`ls reports/round-33/cross/` → empty). The integrator completes the R1–R8 ↔ X00-row match (and answers any X00 row this fragment does not cover).
- `reports/round-33/calib/C14-fix-drafts.md` and `reports/round-33/op/O02-readme-delta.md` — the exact before/after text of the SKILL.md and README edits. R5/R6 are keyed to the declared targets (`:486/:488/:501/:128`; README `:97`,`:207`); when the drafts land, confirm each is line-count-neutral (SKILL.md) and that every new row's cells come from live bytes (README).

## Citations

- `reports/round-33/targets.json:56` (A09 mission + out path), `:5-11` (shared rules), `:10` (missing-dependency rule); `reports/round-33/claims.json:29,33` (claim-O after-state + counting command), `:59` (claim-A after-state)
- `reports/round-33/adj/A10-receipt.md` §1 A09 row, §2 A10-F3/F5 (provisional row + errata rule); `reports/round-33/adj/A13-verify-a07-a09.md` (A09 class re-run, same window)
- `reports/round-33/op/O07-baseline-receipt.md:38-45` (battery 20/20 pinned), `:52-63` (c31 before-state), `:76` (README digest), `:147-181` (in-place filed-byte incident on rounds 5/7)
- commands (2026-10-19T03:50Z–04:0xZ, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `git status --porcelain`; `git ls-files | wc -l`; `sha256sum SKILL.md corpus/lessons/README.md AGENTS.md`; `git hash-object corpus/lessons/README.md`; `git rev-parse HEAD:corpus/lessons/README.md`; `git diff --stat -- AGENTS.md`; `wc -l SKILL.md corpus/lessons/README.md`; `ls corpus/lessons/*.md | wc -l`; `sed -n '47p;128p;149p;183p;294p;456,458p;486p;488p;501p;522p;534,536p;660p;710p;713,715p' SKILL.md`; `sed -n '97p;207p' corpus/lessons/README.md`; `grep -rn "lessons/README\|SKILL.md" tools/gates/frozen/*/MANIFEST.tsv tools/gates/frozen/*/*/MANIFEST.tsv`; `grep -rn "SKILL" tools/gates/frozen/ tools/gates/expected/ reports/round-9/baselines/`; `grep -rl "corpus/lessons" tools/gates/frozen/ | wc -l`; `sha256sum corpus/lessons/round-6-sources/{05,03,13,09}.json`; python one-liner enumerating every `expected.json` `inputs` map under the three battery roots; `grep -rn "README_BASELINE_BLOB\|a3187055" reports/ tools/`; `grep -rn "find_readme_revisions\|README_BASELINE_BLOB" reports/round-2[6-9]/run-validation.py reports/round-3[0-2]/run-validation.py`; `sed -n '90p;96,97p;1494,1510p;1871p;1909p' reports/round-26/run-validation.py`; `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 1, 2 findings); `python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py` (exit 1, X45-P1); `python3 -B reports/round-27/audit/x57-lessons-audit.py --selftest` (34/37); `grep -rn "SKILL\.md:[0-9]" corpus/ tools/ AGENTS.md`
- `reports/round-25/audit/c31-lessons-index-audit.py:36,51,53,328,337-432`; `reports/round-25/audit/x45-lessons-pointer-audit.py:178-179`; `reports/round-27/audit/x57-lessons-audit.py:563-565`; `reports/round-27/audit/x61-pin-sweep.py:186-197`
- `reports/round-26/run-validation.py:90,96-97,1494-1510,1871,1909`; `reports/round-26/lessons/c51-revision-audit.py:19,48,199-203`; `reports/round-26/zzz-lessons-index-revision-4.md:5-7,17-19`; `reports/round-26/zzz-lessons-index-revision-3.md:183`
- `reports/round-30/craft/box1-survey.py:5,10`; `reports/round-30/craft/box1-landed-survey.json:4-6`; `reports/round-30/run-validation.py:697-700`
- `reports/round-25/validation.json:1020`; `reports/round-26/audit/x63-lessons-receipt.json:75`; `reports/round-26/scribe/fragment-ledger.json:401`; `reports/round-31/validation.json:1026`; `reports/round-32/validation.json:1000`; `reports/round-32/dossier-d11-shonen-boxes.md:50,205`; `reports/round-32/dossier-d12-capability-inventory.md:97`; `reports/round-32/dossier-d13-operator-decisions.md:48`; `reports/round-32/final-dossier.md:46,133`; `reports/round-32/scribe/fragment-ledger.md:178,235`; `reports/round-30/validation.json:449`
- `corpus/lessons/README.md:1,6-8,17-21,22-29,36-40,69,97,207`; `corpus/lessons/round-14.md:141`; `corpus/lessons/round-15.md:25`; `corpus/lessons/round-19.md:88,100,101,179`; `corpus/lessons/round-25.md:44`; `corpus/lessons/round-28.md:86`; `corpus/lessons/round-31.md:46`; `corpus/lessons/round-32.md:7,33,41,55,57,58`
- `SKILL.md:47,128,149,183,486,488,501,522,534-536,660,713-715`; `AGENTS.md:42`
- `corpus/knowledge/synthesis/typed-label-routing-workflow.md:6,19`; `corpus/knowledge/verification/label-channel-routing-verification.md:6,17`; `corpus/knowledge/verification/verification-method-overview.md:9`; `corpus/knowledge/verification/gate-frozen-run-standard.md:5`
- `tools/gates/frozen/handoff-packet-check/{r9-pre,r18-post}/packet.md:48,69-72`; `tools/gates/frozen/handoff-packet-check/r9-pre/freeze.txt:2,110`; `tools/gates/frozen/provenance-audit/{r9-pre,r18-post}/inputs/corpus/knowledge/verification/provenance-audit-ledger-format.md:14`; `tools/gates/frozen/round-3/{,attempt-1/}inputs/corpus/knowledge/verification/gate-frozen-run-standard.md:5,15,28,243`
- `reports/round-29/recount/r25-1.md:22` (the `Rows: 49` queue-count scope note)
