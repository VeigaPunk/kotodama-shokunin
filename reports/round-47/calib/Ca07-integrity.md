# Ca07 — successor-integrity verification (claim Ca)

- **Seat:** `Ca07` (claim **Ca**, calibration) | role: verifier, non-author of Ca06
- **Out:** `reports/round-47/calib/Ca07-integrity.md` (the only write by this seat)
- **Baseline:** `6e9a30d` (`git rev-parse --short HEAD` → `6e9a30d`)
- **Verification snapshot:** 2026-10-19T18:08–18:09Z; HEAD unchanged at `6e9a30d`
- **Subject:** `reports/round-47/calib/Ca06-queue-successor.md`, sha256
  `15bb86dfff09ff97cbf8e757bbf139e1cb7bc59f42c66475d19a5a1b02db5ec6`, 46,854 bytes,
  560 lines, JSON deliverable at `:88-516`.
- **Method:** every claim below was re-measured from committed bytes, the live worktree,
  `git show`/`ls-tree` at the named commits, or the read-only fleet ledger. No row
  author's output was accepted as a premise. No filed byte was edited.

## 0. Verdict

**PASS with two conditions** on the successor's integrity contract.

The successor references only real filed paths and commit shas; its three defect rows are
field-for-field identical to the filed Ca01/Ca02/Ca03 fenced rows; its two provider
amendments are field-for-field identical to Ca04's final fenced rows; the parent
`defect-queue-v2.json` is pinned at `dfc9265d…` and is byte-unchanged; and **zero**
`fixed-with-evidence` rows exist, so the "a fixed row must carry a pasted re-run output"
rule is not triggered (G5 forbids minting one without it).

| # | check | verdict | evidence |
|---|---|---|---|
| 1 | parent sha pinned and unchanged | **PASS** | §1 |
| 2 | cited paths resolve | **PASS** (1 intentional absence) | §2.1 |
| 3 | cited commit shas resolve | **PASS** | §2.2 |
| 4 | 64-hex digests map to real bytes | **PASS** with one live-snapshot caveat | §2.3, F-Ca07-4 |
| 5 | defect rows copied without drift | **PASS** — zero differing fields | §3.1 |
| 6 | provider amendments copied without drift | **PASS** — zero differing fields | §3.2 |
| 7 | classes / required fields valid | **PASS** | §3.3 |
| 8 | zero fixed rows; fixed discipline | **PASS** (vacuous; gate absent) | §4 |
| 9 | loop-1 carried items complete | **PASS** — 5/5 + 1, no silent drop | §5 |
| 10 | no filed-byte / corpus writes | **PASS** | §6 |
| 11 | Ca05 source pin current | **CONDITION** — post-assembly rewrite | F-Ca07-2 |
| 12 | PA-47-02 verification sentence true | **CONDITION** — inherited F6 overclaim | F-Ca07-3 |

Conditions: the applied successor must (a) re-anchor its one Ca05 line citation to the
current Ca05 bytes or cite the digest plus a section anchor, and (b) correct the inherited
F6 sentence in `PA-47-02`'s `verification`. Neither condition changes a row's class, owner,
or evidence.

## 1. Parent pin — `reports/round-40/op/defect-queue-v2.json` (PASS)

Successor declaration: `Ca06-queue-successor.md:96-97` pins the parent at assembly and
after assembly at the same digest; `:98` declares `parent_bytes_edited: false`;
`:100` records the two-commit history.

Independently measured at the snapshot:

```
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  reports/round-40/op/defect-queue-v2.json

$ git show 6e9a30d:reports/round-40/op/defect-queue-v2.json | sha256sum
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  -

$ git show ac47c78:reports/round-40/op/defect-queue-v2.json | sha256sum
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907  -

$ git show 13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum
fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98  -

$ git log --oneline -- reports/round-40/op/defect-queue-v2.json
ac47c78 round-41: admit O/Ca — round-runner template + conformance checker (streak classified), N3 pin ruling; luna 32/32 in 7 min
13a1657 round-40: admit C/Ca/A — linguistics 25 (220 total), defect-queue-v2 (38 rows), consolidated r37-40 audit; O12 relative-ROOT cure

$ git status --porcelain -- reports/round-40/op/defect-queue-v2.json
(no output)

$ python3 -c "import json,collections; d=json.load(open('reports/round-40/op/defect-queue-v2.json')); print(len(d['rows']), collections.Counter(r['class'] for r in d['rows']))"
38 Counter({'carried-with-owner': 28, 'fixed-with-evidence': 10})
```

The pinned history is exact: the parent was `fe596a9d…` at `13a1657`, the recorded r41
in-place amendment at `ac47c78` produced `dfc9265d…`, and the file is unchanged at
`6e9a30d`. The r43 predecessor's pin
(`reports/round-43/calib/defect-queue-v2-successor-r43.json:7`) carries the same digest,
and the predecessor has 4 rows and sha256
`77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38`, matching
`Ca06:101-106`.

**Verdict: PASS.** The parent is pinned, unchanged, and not routed around.

## 2. Provenance — paths, commits, digests

### 2.1 Path citations (PASS; one intentional absence)

Extracted 77 unique path citations from the fenced JSON at `Ca06:88-516` and checked each
against the worktree (fleet-root files resolved read-only against
`/home/vgpnk/Projects/shokunin/`). 76 resolve; the one miss is intentional:

- `tools/harness/claims-freshness.py` — cited as **absent** (`Ca06:36,40,100,505`);
  `ls` returns exit 2 at the snapshot. This is an absence assertion, not a dangling
  reference, and it is the premise that keeps `r43-stale-premises` at
  `routed-with-owner`.
- `MANIFEST.json`, `PROTOCOL.md`, `PROTOCOL-APPENDIX.md` resolve at the fleet root as
  read-only siblings; line ranges checked at the snapshot (`MANIFEST.json:4241,4337,4505,4806,4860,4979,5030`;
  `PROTOCOL.md:194-196,237-243,283-290`; `PROTOCOL-APPENDIX.md:37`).
- Every in-repo citation the successor inherited from Ca01/Ca02/Ca03 resolves at the
  stated line, including `reports/round-43/review/R01-review.md:400` (R01-43-12),
  `reports/round-44/review/R01-review.md:290` (R01-44-05),
  `reports/round-44/review/R02-review.md:468` (R02-44-11), and the Ca04 telemetry table.

### 2.2 Commit shas (PASS)

Five distinct short shas appear in the deliverable; all resolve as commits:

```
6e9a30d  commit  round-46: loop-1 retrospective
ac47c78  commit  round-41: admit O/Ca
13a1657  commit  round-40: admit C/Ca/A
7ceff59  commit  round-42: NOT ADMITTED on C
c9f4eaa  commit  round-43: NOT ADMITTED on O+C
```

No sha is fabricated, and no cited sha is a tag or a missing object.

### 2.3 sha256 literals (PASS with one caveat)

Every 64-hex literal in the deliverable was matched to a measured file or to a recorded
predecessor digest:

| digest prefix | claimed source | measured |
|---|---|---|
| `dfc9265d…` | parent queue | matches at HEAD/`ac47c78` |
| `fe596a9d…` | parent at `13a1657` | matches |
| `77f9d63e…` | r43 successor | matches |
| `43ce341f…` | `basename-couples-resolver.py` | matches |
| `d8d23a26…` | r42 extractor | matches at `7ceff59` and HEAD |
| `c99f44ca…` | `mineral-stone-symbolism.md` at `7ceff59` | matches |
| `a8e3fabb…` | loop-1 retrospective | matches |
| `e0e51e56…` | Ca01 | matches at snapshot |
| `91cd4484…` | Ca02 | matches at snapshot |
| `a2e61cdb…` | Ca03 | matches at snapshot |
| `94b99878…` | Ca04 | matches at snapshot |
| `747c0fdb…` | Ca05 (pinned) | **does not match current Ca05** — see F-Ca07-2 |
| `565e4fbd…`,`445daadf…`,`8a9146e1…` | r44 telemetry | match |
| `76632d73…`,`10181657…`,`eddfb5f3…` | r43 telemetry | match |
| `3d826369…` | r47 dispatch-declared | matches |
| `dd88d9e1…` | `.scratch` prototype (non-durable) | matches, labelled method-only |
| `509305c8…` | Ca03's live MANIFEST snapshot | **not recoverable from git** — see F-Ca07-4 |

Ca06's own `source_fragments` (`:108-115`) lists six entries. Five match current bytes:

```
MATCH  Ca01  e0e51e56…   current e0e51e56…
MATCH  Ca02  91cd4484…   current 91cd4484…
MATCH  Ca03  a2e61cdb…   current a2e61cdb…
MATCH  Ca04  94b99878…   current 94b99878…
MISMATCH Ca05 747c0fdb…  current 8ec61c7e… (as of 18:08:38Z; Ca05 is still being revised)
MATCH  retrospective a8e3fabb…
```

## 3. Row integrity

### 3.1 Defect rows — zero drift from the filed fragments (PASS)

The three row objects at `Ca06:124-221` were compared key-for-key against the fenced rows
in the source fragments. Differing fields: **none**.

```
r43-stale-premises                  source=Ca01  diffs=[]
r44-resolver-hyphen-after-blank     source=Ca02  diffs=[]
manifest-ledger-two-schema-evolution source=Ca03 diffs=[]
```

The same was true of the predecessor's row fields (`id`, `origin`, `class`,
`v2_class_equivalent`, `owner`, `reason`, `next_touch`, `evidence`, `verification`), so the
successor does not silently rewrite a filed fragment's semantics.

### 3.2 Provider amendments — zero drift from Ca04's final rows (PASS)

`Ca06:222-380` carries a top-level `provider_amendments[]` with Ca04's final ids. Compared
key-for-key against `reports/round-47/calib/Ca04-provider-amendments.md` (sha `94b99878…`):
**zero differing fields** for both rows.

```
PA-47-01-antigravity-lane-outage  diffs vs Ca04: []
PA-47-02-zai-exhaustion-luna-max  diffs vs Ca04: []
```

Both carry `defect_row: false`, `class: named-deviation`, `v2_class_equivalent: null`; the
defect census stays 38 parent rows + 3 disposition rows, with the two amendments counted
separately. Ca04's own wording correction ("pos 12 re-routed and executed, pos 13
skipped") survives verbatim into the successor (`Ca06:224-310`).

### 3.3 Schema and required fields (PASS)

- Successor parses as JSON; `schema: kotodama-defect-queue-successor-v1`, `round: 47`,
  `baseline_commit: 6e9a30d`.
- `rows`: 3 — `routed-with-owner` 1, `recorded` 2; all four classes are from the declared
  vocabulary.
- `provider_amendments`: 2 — both `named-deviation`, neither duplicated in `rows[]`.
- Every row and amendment has non-empty `id`, `origin`, `class`, `owner`, `reason`,
  `next_touch`, `evidence`, `verification`.
- `loop1_coverage`: `retro_carried_bullets: 5`, `retro_bullets_mapped: 5`,
  `additional_loop1_close_items: 1`.
- `application_gates`: G1–G8 present (`Ca06:438-478`).

## 4. Fixed-row discipline (PASS — vacuous, and correctly so)

There are **zero** `fixed-with-evidence` rows in the successor. The requirement that every
"fixed" row carry a re-run command output is therefore not triggered; there is no fixed
claim to verify.

The only theoretical flip is `r43-stale-premises`, and it is explicitly gated
(`Ca06:158-166`, `:460-463`): it requires the durable tool, a green selftest whose asserted
count equals the controls actually run, the r43 positive regression (O and C STALE, Ca
FRESH), a fresh negative control, the anti-theater mutation, baseline evaluation via
`git show`, and `could-not-evaluate != green` — each with pasted output. At this snapshot
`tools/harness/claims-freshness.py` does not exist (`ls` exit 2), so no flip is
permissible. **The fixed-row contract is satisfied: nothing is claimed fixed.**

## 5. Loop-1 carried-item completeness (PASS — 5/5, no silent drop)

`reports/round-46/loop-1-retrospective.md:43-53` has exactly five carried bullets. The
successor's `loop1_coverage.mapping` (`Ca06:382-437`) maps each one, citing the exact
retrospective line:

| retrospective lines | item | disposition |
|---|---|---|
| `:45-46` | freshness gate absent | `r43-stale-premises` (routed-with-owner) |
| `:47-48` | stale-premises pattern | same row; `class_boundary` records narrow r43 O+C and excludes r44 C |
| `:49-50` | resolver soft-wrap latent edge | `r44-resolver-hyphen-after-blank` (recorded) |
| `:51-52` | antigravity outage | `PA-47-01` (named deviation; 12 re-routed, 13 skipped) |
| `:53` | zai exhaustion | `PA-47-02` (named deviation) |

Plus one additional loop-1 close item named by the Ca claim but not by the retrospective —
the two MANIFEST ledger schemas — recorded at `Ca06:187-221` with a provenance correction
stating it originates in the r46 audit, not the retrospective. Every `not_requeued` entry
(`Ca06:426-436`) carries a reason. Zero items are silently dropped.

## 6. Filed-byte and write-surface integrity (PASS)

```
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/

$ git diff --name-only; git diff --cached --name-only
(empty; empty)

$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

No tracked filed byte is modified, staged, or deleted. The only corpus delta in the round
is C's landing, which the integrator applies separately. The Ca seats write only under
`reports/round-47/` plus ephemeral `.scratch/` fixtures; no `corpus/` or `tools/` write is
made by the successor.

## 7. Findings

### F-Ca07-1 — parent pin (PASS, no action)

Verified in §1. The pin is honest and the parent is unchanged at
`dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`.

### F-Ca07-2 — Ca05 source pin and line citation drifted after assembly (should-fix; owner integrator)

`Ca06:113` pins `Ca05-verify.md` at `747c0fdb…`. Ca05 was rewritten at least twice after
Ca06 assembled (15:06 and 15:08 local), and at this snapshot its sha256 is
`8ec61c7e7ff2e3ff75472b80d9d73309513f7699436772ce421fe53438510bcd` (23,497 bytes, 391
lines). Consequence: the one line-range citation to Ca05 in the successor —
`Ca06:100` → `Ca05-verify.md:170-187` for the parent-queue re-measurement — now lands on
the Ca01 verdict section. In the current Ca05 bytes the parent section is at `:147` ff.

Ca06's own G8 anticipates exactly this: "a mismatch means a fragment was revised after
this assembly — reconcile by evidence and record an id alias, never duplicate the rows or
edit this artifact" (`Ca06:475-477`). The substance is not contradicted: current Ca05
re-measures the parent pin at `:147-159`, the antigravity facts at `:116-145`, and the zai
facts at `:135-145`. **Action:** the integrator should cite Ca05 by digest plus a section
anchor, or re-anchor to the current lines, and record the post-assembly revision as a
successor note; do not treat `747c0fdb` as the current bytes.

### F-Ca07-3 — inherited F6 overclaim in `PA-47-02`'s verification (should-fix; owner Ca04/Ca06 integrator)

`Ca06:371` (copied verbatim from `Ca04-provider-amendments.md:195`) states:

> "no dispatch-declared.json at r44, r46 or r47 names zai (lanes: opencode-go, devin,
> opencode-go)"

The parenthetical is true of the `provider_lane`/`model` fields, but the sentence's literal
claim is false: the r46 dispatch notes say "zai lanes route to openai-codex/gpt-6-luna-max
for the session (zai usage exhausted)"
(`reports/round-46/telemetry/dispatch-declared.json:16`), and the r47 notes say
"Standing amendments: zai->luna-max all session"
(`reports/round-47/telemetry/dispatch-declared.json:18`). Ca05's F6 already flags this
(`Ca05-verify.md:258`: "false for r46/r47 notes; the true point is the dispatch lane, not
the notes").

**Action:** in the applied successor, scope the sentence to the dispatch lane, e.g. "no
dispatch-declared.json at r44/r46/r47 declares zai as `provider_lane`/`model`; the r46 and
r47 notes record the standing zai→luna-max amendment". The row's class, owner, evidence and
reclass gates are unaffected; this is a wording correction, not a new defect row.

### F-Ca07-4 — Ca03's live MANIFEST digest is not recoverable from git (`could-not-recover`; owner integrator)

Ca03 pins the fleet `MANIFEST.json` at `509305c8…`, 293,641 bytes, 281 rows, read live at
17:53:10Z (`Ca03-manifest-schemas.md` §1, §7). The ledger is live and append-ordered; the
committed blobs I can recover are:

```
$ git -C /home/vgpnk/Projects/shokunin show 2c425ef:MANIFEST.json | sha256sum
19ddec8b8c667f403a0006eb463c1604dd4f61bb7b08a29e366286832d2a705b   (280 rows; matches Ca03's "earlier read")
$ git -C /home/vgpnk/Projects/shokunin show f775cae:MANIFEST.json | sha256sum
6a40b0a588002bd8c45974e60260dc485f6c3996406c5938262a94c1f0a5b434   (282 rows; current committed ledger)
```

The 281-row intermediate (509305c8) is not in git history and cannot be reconstructed. This
is not a fabrication: Ca03 itself says the ledger is live and pins a digest "not a path".
Its structural claims still reproduce against the 282-row ledger: S1 rounds 33–42 with 11
keys, S2 rounds 43/44/46 with 15 keys, `lane_rounds == round` 10/10, and the claims key-set
variation `{C,Ca,O}` vs `{A,Ca,O}`. **Action:** record the pinned 509305c8 as a seat-time
live read (`could-not-recover` from durable sources), and do not present it as a
re-derivable digest.

### F-Ca07-5 — Ca05's own digest pins are internally split (observation; owner Ca05/integrator)

At this snapshot Ca05's summary table pins Ca04 at `94b99878…`
(`Ca05-verify.md:26`) while its Ca04 section heading and machine-readable block still pin
`5f370306…` (`:214`, `:338`). Ca06 pins the final `94b99878…`, so the successor is correct;
the split is in the verifier fragment. Treat Ca05 as volatile (three writes observed during
this wave) and rely on the successor's source pin. No edit to Ca05 by this seat.

### F-Ca07-6 — Ca05's earlier Ca02 digest was stale; corrected (resolved, no action)

Ca05's first landing recorded `row_sha256: 7ceb8445…` for Ca02
(`Ca05-verify.md` first edition). The filed Ca02 bytes are `91cd4484…`; the current Ca05
records `91cd4484…` (`:24`, `:314`) and Ca06 pins the same digest (`:110`). Ca06's
observation 3 (`:483`) explains the mismatch as a pre-final read; the explanation is
consistent with the mtimes (Ca02 final write 14:56:50, Ca05 first write 14:58:04). No
action.

### F-Ca07-7 — verification binds to Ca06's final revision (observation)

Ca06 was itself rewritten during the wave: an earlier read at 18:04Z had sha `c9b7d7af…`
and no Ca04 rows; the final artifact is `15bb86df…` (15:05 local) and includes Ca04's
fenced rows verbatim. This report binds to `15bb86df…`. A later rewrite must be re-checked
against G8, not assumed covered by this verdict.

## 8. Application conditions (binding on the integrator)

1. **Parent:** re-run `sha256sum reports/round-40/op/defect-queue-v2.json`; expect
   `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`. A mismatch means
   stop and report; never route around it.
2. **Apply as a new artifact:** extract the fenced JSON at `Ca06:88-516` to
   `reports/round-47/calib/queue-successor-r47.json` (or apply the successor update). Do
   not edit the parent or any filed round.
3. **Correct F-Ca07-3** in the applied `PA-47-02` verification sentence, and record the
   correction with the `Ca05-verify.md:258` (F6) citation.
4. **Re-anchor F-Ca07-2:** cite Ca05 by its final digest plus section anchor, or update the
   line reference; record that Ca05 was revised after Ca06's assembly.
5. **Fixed discipline:** do not mint a `fixed-with-evidence` row unless O lands and its
   demonstration pastes the r43 regression output. At this snapshot the tool is absent.
6. **Record F-Ca07-4:** the 509305c8 MANIFEST snapshot is a seat-time live read, not
   recoverable from git.

## 9. Reproduction

```bash
# parent pin and history
sha256sum reports/round-40/op/defect-queue-v2.json
git show 6e9a30d:reports/round-40/op/defect-queue-v2.json | sha256sum
git show ac47c78:reports/round-40/op/defect-queue-v2.json | sha256sum
git show 13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum
git log --oneline -- reports/round-40/op/defect-queue-v2.json
git status --porcelain -- reports/round-40/op/defect-queue-v2.json

# successor parse + row provenance
python3 - <<'PY'
import re, json, hashlib
t = open('reports/round-47/calib/Ca06-queue-successor.md').read()
o = json.loads(re.findall(r"```json\n(.*?)\n```", t, re.S)[0])
print(len(o['rows']), len(o['provider_amendments']), [r['class'] for r in o['rows']])
for p, h in o['source_fragments'].items():
    print(p, hashlib.sha256(open(p, 'rb').read()).hexdigest() == h)
PY

# commit shas
for c in 6e9a30d ac47c78 13a1657 7ceff59 c9f4eaa; do git cat-file -t "$c"; done

# fixed rows
python3 -c "import re,json;o=json.loads(re.findall(r'\`\`\`json\n(.*?)\n\`\`\`',open('reports/round-47/calib/Ca06-queue-successor.md').read(),re.S)[0]);print([r['id'] for r in o['rows'] if r['class']=='fixed-with-evidence'])"

# write surface
git status --porcelain
git diff --name-only; git diff --cached --name-only
find corpus/knowledge -name '*.md' | wc -l
ls corpus/knowledge/culture-material/*.md | wc -l
```

## 10. Boundary and provenance

Only `reports/round-47/calib/Ca07-integrity.md` was written by this seat. No filed byte
(`reports/round-1..46/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`)
was edited or staged. No round runner was executed; no corpus staging; no git
mutation/network/install. The fleet `MANIFEST.json`, `PROTOCOL.md` and
`PROTOCOL-APPENDIX.md` were read only (siblings, read-only per `AGENTS.md`).

`to-verify` (named, not guessed):

- The final Ca05 bytes at integration (it was still being revised at the snapshot;
  digest `8ec61c7e…` was current at 18:08:38Z).
- Whether the integrator applies the successor JSON as a separate file or folds it into the
  ledger; either is acceptable if the parent stays byte-identical.
- The r43-stale-premises reclass, which is outside this artifact and depends on O's landing
  plus a pasted demonstration.
