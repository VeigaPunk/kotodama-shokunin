- Seat: C06 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C06 — disposition of open item 6 (OI-06, box-1 condition 4: dangling tool anchors)

**Dependency reconciliation.** At this seat's first evidence cut
(`2026-10-19T03:55Z`) `reports/round-33/calib/` was empty, so item 6 was
derived from the two authoritative enumerations K03 is chartered to
canonicalize (`reports/round-32/dossier-d13-operator-decisions.md:128-138`;
`reports/round-33/claims.json:44`) under two candidate expansion conventions,
both of which the derivation recorded as `to-verify` (reading A: cold-run
N1/N4/N5/N7 split, item 6 = N4; reading B: D11 box-4 readings added, item 6 =
lore-owned bilateral read). **Both readings were wrong and are discarded, not
carried.** K03 landed at `00:56` local and was read in full before this
fragment closed: its seat mapping is explicit — "C01↔OI-01 … C12↔OI-12 in this
order" (`calib/K03-open-items.md:75`) — so item 6 is **OI-06**:

| field | value |
|---|---|
| id | `OI-06` (K03 canonical, `calib/K03-open-items.md:67`) |
| item | box-1 condition 4 — dangling tool anchors `TL-01` / `TL-02` / `FIELD_DEFAULTS` / `fictional-coordinate` / `descriptive-gloss` |
| origin | r24 (re-confirmed r32) |
| class (K03 domain vocabulary) | `citation-condition` (`calib/K03-open-items.md:58,67`) |
| D13 pointer | `reports/round-32/dossier-d13-operator-decisions.md:133`; `reports/round-24/promotion-review.md:81-84`; `reports/round-32/dossier-d11-shonen-boxes.md:64-68` |
| K03's own routing | **not** in K03's carry list (`:76-78` names OI-01..03, OI-08..12) and **not** in C14's named draft set (`:76-77` names OI-04/05/06 — OI-06 **is** named there); this fragment therefore files the bounded draft itself |

## 1. Status quo re-verified at HEAD (all commands 2026-10-19, HEAD `139e3b6`)

**1a. The anchors resolve to nothing in the toolchain — RE-CONFIRMED.**
`grep -rn "TL-01\|TL-02\|FIELD_DEFAULTS" tools/ SKILL.md` → four hits, all in
`SKILL.md` (`:479`, `:481`, `:483`, `:491`), **zero** in `tools/`.
`grep -rn "fictional-coordinate\|descriptive-gloss" tools/ SKILL.md examples/`
→ one hit, `SKILL.md:491`, zero in `tools/` and `examples/`. Per-token counts
(`2026-10-19T03:57:35Z`), live tool vs whole repo excluding `.scratch` and
rounds 20-32: `TL-01` 0/68, `TL-02` 0/46, `FIELD_DEFAULTS` 0/23,
`fictional-coordinate` 0/43, `descriptive-gloss` 0/49 — every repo hit is filed
prose (r8 drafts, r10 drift, r24 review, `SKILL.md` itself), none is a
resolvable tool token. The tool that the rows cite ships three kinds, not five:
`tools/d2-typed-labels.py:410` `KINDS = ("translated-label", "native-form",
"borrowed-strata")`, docstring `:7-12`.

**1b. `FIELD_DEFAULTS` is absent; the only `*DEFAULTS` token is a different
object.** `D2_DEFAULTS` exists at `tools/gates/typed-pipeline-gate.py:132` —
the D2 pipeline identity resolver's default path set, consumed at `:374-404`
(`resolved = dict(D2_DEFAULTS)` … `generalized = … resolved[key] !=
D2_DEFAULTS[key]`). It is a path-identity table, **not** a label-field typing
table; the SKILL row's `(tool FIELD_DEFAULTS)` therefore points at no object at
all, and re-pointing it at `D2_DEFAULTS` would be a new mis-cite.

**1c. Provenance of the stale ids (so the draft re-points rather than guesses).**
`reports/round-8/depth/skill-table-draft.md:240` cites "tool `FIELD_DEFAULTS`
(`tools/d2-typed-labels.py:126-135`)"; `:252`/`:259-260` define the two extra
kinds citing `tools/d2-typed-labels.py:84-103`. `reports/round-8/depth/
design-spec.md:580` records the r8 tool at `:85` shipping **five** kinds, and
`reports/round-8/depth/findings.md:112` records the narrowing to three at
`3548185c`. At HEAD those line regions are loader internals (`:126-135` ends in
`_scan_flow_balance` at `:132`) — the anchors are stale *region labels plus a
five-kind vocabulary the tool no longer ships*. The staleness is already filed:
`reports/round-10/drift/shard-05.md:46` — "`grep -c "FIELD_DEFAULTS"` = 0;
kinds `fictional-coordinate`/`descriptive-gloss` also absent from the live tool
… **stale — id + kind names**".

**1d. The behaviours the rows describe are real and selftest-enforced at HEAD —
VERIFIED.** This is what r24 asked to preserve ("the rule itself is
executable-verified; needs re-point or dated erratum",
`reports/round-24/promotion-review.md:81-84`):

- label-only off the sound channel: `tools/d2-typed-labels.py:690` —
  `check_sound_form` (`:686`) returns before any test unless
  `kind ∈ SOUND_KINDS` (`:411`) and `status == "supplied"`.
- label-only held, never a silent pass: `:810-814`, two
  `_fail(..., D2L_FORM, ..., hold=True)` sites with stable reasons ("label_id …
  has no supplied native/borrowed form"; "translated label with no supplied
  sound form and no label_id"); code `D2L_FORM = "D2L-FORM-UNRESOLVED"`
  (`:422`); selftest asserts 12/12 of them are `hold` (`:2997-2998`).
- no declared kind: `:769` — `_fail(D2L_DATA, where, f"kind {…!r} is not one of
  {KINDS}")`, a stable-reason **failure**, never a guess; no text-language
  inference path exists (the only text-sensitive check is gated on the declared
  kind at `:690`).
- era tags / slot glosses off the name channel: the off-channel routing is live
  in `tools/assemble-d2-typed.py:203-229` (`source_field` →
  `off_channel_field` `"%s_gloss"`, with `channel`, `hold`, `owed_slot`), rule
  text at `:229`, asserted at `:407`; projection exclusion
  `NON_PROJECTABLE_KINDS` at `tools/d2-typed-labels.py:974`.
- dated green: `python3 tools/d2-typed-labels.py --selftest` →
  `selftest: 163/163 checks passed`, exit 0, **2026-10-19T03:59:29Z**.

**1e. Note on the row's own code words (a second-order defect inside OI-06).**
Row `SKILL.md:483` says "**hold** with a stable reason"; at HEAD a record with
no declared kind is a **fail** (`:769`), and row `:481`'s "HOLD, not clean" maps
to the prototype's rule 4 (`22-label-representation.md:131-132`) — live, a
`supplied` sound kind with no bytes is a hard fail (`:775`, "status supplied
requires text") while the not-supplied case stays in the owed-form hold census
(selftest `:3193-3194`). A bare id swap would leave both codes wrong; the draft
in §3 restates them.

## 2. Disposition

**Class: fixable-now (bounded, citation-level) — bounded fix draft F-OI06 filed
in §3 for integrator application.** Grounds: the condition is pointer-level
(`promotion-review.md:81-84`: "needs re-point or dated erratum"), the target
file is `SKILL.md`, and seats never edit shared files
(`reports/round-33/targets.json` shared_rules[1]; `claims.json:46` "no source
edits by seats; integrator applies").

**Ledger value for C15 (`disposition_class`), stated two ways so C13/R04 do not
have to infer:**

- `fixed-with-evidence` **only once the integrator applies F-OI06** and the
  §3 verification commands re-run green — until then it must not be written as
  fixed.
- `carried-with-owner+reason+next-touch` is the honest value at this fragment's
  cut: **owner** = round-33 integrator; **reason** = the fix is a shared-file
  edit reserved to the integrator, and no lane seat may edit `SKILL.md`;
  **next-touch** = round-33 integration, then re-run the §3 commands and
  re-digest the box-1 survey.
- Domain class stays `citation-condition` (K03's vocabulary) — a different
  field from the ledger's status class, not a contradiction (same shape as
  C01's note, `calib/C01-item-01.md:24-28`).

## 3. Bounded fix draft F-OI06 (before → after, exact bytes; integrator applies)

Rationale: re-pointing is strictly stronger than a dated erratum here, because
the enforcement exists at HEAD — after the edit no row claims a token that
resolves to nothing, and no behaviour claim is dropped. Line numbers are the
current ones; the integrator must re-anchor if earlier edits shift them.

**F1 — `SKILL.md:479`**

before:

```
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red (`22-label-representation.md:126-128`; executable `TL-01`) |
```

after:

```
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red (`22-label-representation.md:126-128`; live: `tools/d2-typed-labels.py:690` keeps any non-sound kind out of the check and `:810-814` emits the hold `D2L-FORM-UNRESOLVED` (`:422`); selftest "no GAR label is graded on the sound channel" `:3195-3197`) |
```

**F2 — `SKILL.md:481`**

before:

```
| A sound kind declared with no bytes supplied | HOLD, not clean (`22-label-representation.md:131-132`; executable `TL-01`) |
```

after:

```
| A sound kind declared with no bytes supplied | not clean (`22-label-representation.md:131-132` prototype rule 4; live at `tools/d2-typed-labels.py`: a `supplied` sound kind with no text is a hard fail `:775`, and a not-supplied one stays in the owed-form hold census — selftest `:3193-3194`, 12/12 holds asserted `:2997-2998`) |
```

**F3 — `SKILL.md:483`**

before:

```
| A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py` `TL-02`) |
```

after:

```
| A record with no declared kind at all | fails with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py:769`: a kind outside `KINDS` (`:410`) fails as `D2L-DATA` naming the value and the legal set; the only text-sensitive check is gated on the declared kind at `:690`) |
```

**F4 — `SKILL.md:491`**

before:

```
| Era tags or slot glosses graded on the name/sound channel | type them `fictional-coordinate` / `descriptive-gloss`; neither enters the sound channel (tool `FIELD_DEFAULTS`) |
```

after:

```
| Era tags or slot glosses graded on the name/sound channel | move them off the channel, not re-type them: the live tool ships three kinds (`tools/d2-typed-labels.py:410`) and routes a gloss field to `garment_gloss` with `channel`/`hold`/`owed_slot` recorded (`tools/assemble-d2-typed.py:203-229`, asserted `:407`); non-projectable kinds `tools/d2-typed-labels.py:974`. (`fictional-coordinate`/`descriptive-gloss` were r8 draft vocabulary, `reports/round-8/depth/design-spec.md:580`, dropped at `3548185c` — `reports/round-8/depth/findings.md:112`; already filed stale `reports/round-10/drift/shard-05.md:46`.) |
```

**Cascade note (for A09/X01).** Applying F1-F4 changes `SKILL.md`'s sha256
from the live `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`
(= D11's r32 re-run digest, `reports/round-32/dossier-d11-shonen-boxes.md:50`)
to a new value; the box-1 survey receipt `reports/round-30/craft/
box1-landed-survey.json` already pins an older `skill_sha256` `83b0a78a…`, so
the integrator must re-run `python3 -B reports/round-30/craft/box1-survey.py`
and state the new digest rather than leave the r30 receipt reading as current.
No frozen gate fixture pins `SKILL.md` bytes — `grep -rn "SKILL.md"
tools/gates/frozen/` returns only prose references to "`SKILL.md` §Gates" as a
registry home, so no frozen-bytes invalidation is triggered.

**Verification commands for the applied draft** (run by the integrator after
applying; all expected green):

```sh
grep -c "TL-01\|TL-02\|FIELD_DEFAULTS" SKILL.md                      # expect 0
grep -c "fictional-coordinate\|descriptive-gloss" SKILL.md           # expect 0
python3 -B reports/round-30/craft/box1-survey.py                     # expect 28/28, exit 0, new digest
python3 tools/d2-typed-labels.py --selftest                          # expect 163/163, exit 0 (tool untouched)
```

## 4. Adjacent observations (routed, not absorbed — no disposition claimed)

- **Filed-round bytes transiently dirty in the working tree.** At
  `2026-10-19T03:55Z` `git status --porcelain` listed
  ` M reports/round-5/validation.json` and ` M reports/round-7/validation.json`
  alongside ` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`; at
  `04:00Z` the same command lists neither (only ` M LOG.md`, `?? REGIMEN.md`,
  `?? reports/round-33/`), and `git diff --stat` over both files is empty. This
  is the N2 class already on record — "the three acceptance scripts rewrite
  filed tracked receipts in place" (`reports/round-24/promotion-review.md:183-185`)
  — i.e. a seat run can leave a filed round-1..32 byte modified with no
  round-33 author. The actor is `to-verify` (this seat ran only read-only
  commands plus the tool selftests, and did not touch either path). Routed to
  X02 (append-only discipline) and the integrator for a close-time
  `git status` check before the round commit.
- **Item 6 is not the lore-owned pair.** The two lore/operator-owned rows are
  `OI-08`/`OI-09` (`calib/K03-open-items.md:69-70`), mapped to C08/C09. This
  fragment dispositions neither; the contract-digest and bilateral-read
  measurements this seat took (live contract sha256
  `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`, unchanged
  vs HEAD; handoff gate on the sample pair exit 0, 16/16 fields, findings=0 at
  `2026-10-19T03:56:27Z`) are left for those seats and A06 rather than claimed
  here.

## Owed

- none (K03 landed and was read; F-OI06 is drafted in full above; no shared-file
  byte was edited by this seat)

## Citations

- `reports/round-33/targets.json` — C06 seat object (mission, `out`
  `calib/C06-item-06.md`), shared_rules[1] (no seat edits to shared files)
- `reports/round-33/claims.json:8,44,46` — baseline, claim-C enumeration,
  "no source edits by seats; integrator applies"
- `reports/round-33/calib/K03-open-items.md:58,67,75-78` — OI-06 row, class
  vocabulary, seat mapping, K03's carry/fix-draft routing
- `reports/round-33/calib/C01-item-01.md:24-28` — the domain-class vs
  ledger-status-class note this fragment follows
- `reports/round-32/dossier-d13-operator-decisions.md:128-138` — Decision 4 table
- `reports/round-32/dossier-d11-shonen-boxes.md:50,64-68` — box-1 condition 4
  re-confirmation; SKILL digest 79fe91d3
- `reports/round-24/promotion-review.md:81-84,183-185` — the r24 condition text
  ("re-point or dated erratum") and the N2 acceptance-script class
- `reports/round-8/depth/skill-table-draft.md:240,252,259-260`,
  `reports/round-8/depth/design-spec.md:580`,
  `reports/round-8/depth/findings.md:112` — anchor provenance and the
  five→three kind narrowing at `3548185c`
- `reports/round-10/drift/shard-05.md:46` — the staleness already filed
- `SKILL.md:479,481,483,491` — the four rows carrying the five anchors
- `tools/d2-typed-labels.py:7-12,410,411,422,686,690,769,775,810-814,974,2997-2998,3193-3194,3195-3197`
- `tools/assemble-d2-typed.py:203-229,407` — live off-channel routing
- `tools/gates/typed-pipeline-gate.py:132,374-404` — `D2_DEFAULTS`, the
  different object
- `reports/round-30/craft/box1-landed-survey.json` — pinned `skill_sha256`
  `83b0a78a…`
- `reports/supplement-opencode-1/22-label-representation.md:126-134` — prototype
  rules 2-5 that the rows summarise
- Commands (2026-10-19, HEAD `139e3b662900557afe54f632b468619593dc9fcb`):
  `grep -rn "TL-01\|TL-02\|FIELD_DEFAULTS" tools/ SKILL.md` → 4 SKILL rows, 0
  tool hits; `grep -rn "fictional-coordinate\|descriptive-gloss" tools/ SKILL.md
  examples/` → 1 hit (`SKILL.md:491`); `grep -rn "DEFAULTS" tools/` →
  `typed-pipeline-gate.py:132` + frozen copies; `sha256sum SKILL.md` →
  `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`;
  `python3 tools/d2-typed-labels.py --selftest` → `163/163 checks passed`,
  exit 0, `2026-10-19T03:59:29Z`; `git status --porcelain` at `03:55Z` and
  `04:00Z` (filed-round dirt transient, §4); `python3
  tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` →
  `fields=16/16 glossary-entries=20 findings=0`, exit 0, `2026-10-19T03:56:27Z`;
  `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` →
  `5f4c02bf…`
