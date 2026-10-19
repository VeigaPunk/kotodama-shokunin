- Seat: A01 | verifier | claim C | date 2026-10-19 | baseline ac47c78

# A01 — adjacency ride-along: couples/bleed scan of the 4 new myth-symbol entries

**Assignment.** `reports/round-42/targets.json` A01: *"Adjacency ride-along: the 4
new entries' couples/bleed scan (mirror A02-r40)."* Out path:
`reports/round-42/adj/A01-entries-bleed.md`.

**Mirror-target correction (filed, not absorbed).** The mission names "A02-r40" as
the method precedent. `reports/round-40/adj/A02-province.md` is the **PROVINCE
accuracy** seat, not an entries scan; the entries/couples/bleed precedent is
`reports/round-37/adj/A02-entries-bleed.md` (couples resolution + the r34
language predicate), and the extraction/resolution rule is the adopted
`reports/round-39/calib/basename-couples-policy.md`. This seat follows the
entries-bleed precedent and the adopted policy; the pointer discrepancy is
recorded here for the integrator rather than silently resolved.

## 1. Target set status — 3 of the 4 new entries are ABSENT at this cut

- `find reports/round-42 -type f | sort` at this seat's first cut (5 files,
  2026-10-19) → `claims.json`, `op/O09-scribe.md`, `op/O10-gap-fill.md`,
  `targets.json`, `telemetry/dispatch-declared.json`. `reports/round-42/cov/`
  **did not exist** at that cut — `cov/C01..C04` entry drafts, `cov/C05-audit.md`,
  `cov/C06-delta-receipt.md` all absent.
- Per-path `[ -f ]` tests on the four declared names — `corpus/knowledge/myth-symbol/`
  carries exactly the 23 filed entries (`ls | wc -l` → 23); none of the four
  new names is present. (The r40 linguistics expansion's four files —
  `taboo-strata-lifecycle.md`, `dialect-register-consistency.md`,
  `translation-protocol-fidelity.md`, `sacred-registers-liturgical-language.md` —
  *are* present, but in `linguistics/`, from round 40, not this round's C block.)
- **Same-wave landings.** `cov/C02-entry-2.md` (58314 B, mtime `13:00:26 -0300`)
  and `cov/C08-verify.md` landed **7 s after** this seat's fragment
  (`13:00:19 -0300`); C02's verdict is filed in §3b. `cov/C01`, `C03`, `C04`,
  `C05`, `C06` and `scout/K02-myth-gaps.md` are still absent, so **three of the
  four target entries remain unverdictable** at this cut. Same-wave absence is
  recorded, not treated as a defect (r37 A11 precedent).
- This seat does not score absent drafts. What it does instead: (a) files the
  reusable read-only scan instrument with its exact arithmetic, (b) measures the
  baseline control set, (c) files two live findings the new entries must not
  inherit, and (d) verdicts C02's landed draft under both token rules.

## 2. Instrument (durable) — `reports/round-42/adj/A01-scan-instrument.py`

Read-only; `sha256 2345a23d9f24409fb665b72339ecd1b4afdd27e332b205be2fc46995562c0ad7`
(111 lines; locates the lane root by walking up to the `corpus/knowledge` parent,
so it runs from any cwd). It reproduces the adopted policy's arithmetic
**exactly**:

- **Token rule, as adopted** (`basename-couples-policy.md:18-25`):
  `[A-Za-z0-9_./{},\-]+\.md`, brace-expanded one level, deduped per entry.
- **Block extraction, not single-line** — the field plus its continuation lines
  through the next `- ` header field. This is the r39 Ca04 **D1** fix direction.
- **Two-tier resolution, four classes** (policy §2): direct → unique-basename
  `fallback` → `unresolved` / `ambiguous`.
- **Verification of the instrument** (the strongest available control): run over
  the **212-entry** pre-r40 tree (current 220 minus the 8 r39/r40 additions), the
  block mode yields `entries=212 direct=2337 fallback=163 ambiguous=0
  unresolved=8`; the **single-line** mode yields `direct=2335 fallback=163
  ambiguous=0 unresolved=6` — byte-for-byte the filed r39 Part 2 census
  (`reports/round-39/calib/Ca03-basename-policy.md:35-36,268`;
  `reports/round-39/calib/Ca04-verify.md:29`). The instrument is therefore
  calibrated against filed bytes, and the block−line delta is exactly D1's
  two recovered `phonetics-phonology.md` tokens.

## 3. Baseline control — the myth-symbol partition (23 entries, HEAD `ac47c78`)

Block-mode run, `python3 -B reports/round-42/adj/A01-scan-instrument.py`:

`TOTALS MYTH-SYMBOL (control): files=23 direct=203 extless=99 unresolved=0 ambiguous=0`

| metric | value |
|---|---|
| entries with a `couples:` field | 23 / 23 |
| `.md`-token refs resolved `direct` | 203 |
| extension-less refs resolved | 99 |
| unresolved / ambiguous | 0 / 0 |
| wrapped (continuation-line) fields | 0 |
| language-predicate hits (r34 `LANG_TOKENS`/`LANG_ALLOW`/`LANG_FRAME`) | **0** |
| PROVINCE-derived screen hits | 2, both *routing* language (§5) |
| entries whose `couples:` field contains **zero** `.md` tokens | 8 |

The 203 `direct` + 15 `fallback` on the eleven r37 entries reproduces A02's
filed 334/319/15 exactly (`reports/round-37/adj/A02-entries-bleed.md:7,23`).
Per-entry line/ref/digest table is the instrument's stdout; the `sha8` column
lets any later reader detect a moved entry.

## 4. Verdict — `cov/C02-entry-2.md` (landed 13:00:26 -0300, scanned this seat)

C02 proposes `corpus/knowledge/myth-symbol/purity-pollution-systems.md` and fences
its bytes in a ```markdown block; the scan runs on the fenced content (extracted
read-only to `.scratch/a01/C02-draft.md`), since the draft is not a corpus file
and the integrator applies it.

| check | result |
|---|---|
| `couples:` field | 5051 chars, **single-line**, no continuations |
| distinct `.md` tokens | 36; **35 resolve `direct`, 0 unresolved, 0 ambiguous** |
| extension-less refs | **0** — the draft uses the full-extension form throughout, so F-A01-1 does not bite this entry |
| partition spread | myth-symbol 11, civilizations 9, culture-material 6, linguistics 5, synthesis 3 — cross-register, in-lane |
| language predicate | **1 hit, adjudicated benign** (below) |
| PROVINCE-derived screen | **0 hits** |
| target collision | `corpus/knowledge/myth-symbol/purity-pollution-systems.md` does **not** exist at `ac47c78` — no collision |

- **Language hit (benign, not bleed):** `.scratch/a01/C02-draft.md:126` — `| **intensification** | an axis is promoted | a purity movement … |`. `promoted` here describes an *axis* moving within the entry's own model, not a corpus/promotion verdict; the line carries no grant frame. The r34 predicate's `LANG_FRAME` correctly did not fire on the token alone, and this seat adjudicates the match in context exactly as A02-r37 did for `mechanic*`
  (`reports/round-37/adj/A02-entries-bleed.md:33`).
- **Boundary discipline observed in the draft itself:** the entry states its
  partition boundaries explicitly (forbidden *states/contacts* vs
  `politeness-taboo-euphemism`'s forbidden *words*; status vs
  `bathing-and-body-hygiene`'s washing) and repeats the canon handoff
  ("canon belongs to lore-shokunin"). That is the `corpus/QUALITY.md:13-20`
  hygiene clause working as designed.
- **Verdict: GREEN on couples resolution and bleed for the draft as written.**
  This is a pre-landing structural verdict only — it is **not** an admission,
  scholarship, canon, clearance or closure verdict, and it does not audit the
  draft's sources (C05's assignment). The single unresolved token in the raw
  field, `ritual-liminality.md`, resolves `direct` by the entry-directory rule —
  confirming the draft is authored to the Tier-1 path, not relying on the
  basename fallback.

## 5. Finding **F-A01-1** — the extension-less naming blind spot (live, pre-existing, unfiled)

- **Statement.** The adopted token rule extracts only strings ending in `.md`.
  A large part of the corpus writes `couples:` targets **without the extension**
  — either bare (`semantics-pragmatics`) or partition-qualified
  (`linguistics/semantics-pragmatics`). Every such reference is **invisible** to
  the policy's extractor: it is not `direct`, not `fallback`, not `unresolved`.
  It is simply not counted.
- **Scale (my read-only recount, HEAD `ac47c78`).** 103 of 220 entries use the
  form; in the myth-symbol partition alone 14 of 23 do, and **8 entries have a
  `couples:` field with no `.md` token at all** —
  `animal-symbolism.md:16`, `celestial-symbolism-calendars.md:20`,
  `comparative-frameworks.md:20`, `hero-journey-variants.md:20`,
  `number-symbolism.md:5`, `pantheon-archetypes.md:25`,
  `ritual-liminality.md:14`, `trickster.md:5`. Under the policy these eight
  contribute **0 tokens** to a partition-wide census; read whole they contribute
  56 refs (animal 12, celestial 5, comparative 4, hero-journey 7, number 4,
  pantheon 5, ritual-liminality 13, trickster 6).
- **Worst case is an uncounted zero, not a dangling one.** `trickster.md:5`
  alone writes `language files (… sociolinguistics-registers — …; naming-systems
  — epithet strings …)`; under the policy the whole entry is a zero-token field.
  A "0 unresolved / 0 ambiguous" census line is therefore **not** evidence that
  an entry's couples resolve — the policy's §3.1 rule ("zero unresolved must
  state the fallback count") needs a companion: *and the extension-less count,
  and the zero-token entry count*.
- **Why this is not the already-filed D1.** D1 is about a *wrapped* field
  silently zeroed (one instance). This is a *token-form* blind spot affecting
  103 entries and producing zero-token fields in eight of them; D1's fix (block
  extraction) does **not** touch it. My instrument's `extless` class exists
  precisely to expose it. Grep evidence it is unfiled: `extension-less|
  extensionless|bare basename|no \.md|missing extension` over
  `reports/round-3[7-9]`, `reports/round-40`, `reports/round-41`,
  `corpus/QUALITY.md` → **0 hits**.
- **Adjacency consequence for claim C.** Each new myth-symbol entry must be
  scanned under **both** token rules. If a new entry follows the eight-entry
  house style (bare names), a policy-conformant audit will report it as
  couples-clean **vacuously**. That is a false green, and it is the specific
  adjacency risk this ride-along exists to catch.
- **Route (drafted, integrator-applied; no corpus byte touched).** Successor
  policy note: widen §1's token rule to also match bare/partition-qualified
  entry-name tokens (or explicitly classify them `extless`), add the
  `zero-md-token entry count` to §3's mandatory reporting line, and re-run §6.
  Owner: integrator / next calibration round. Nothing here edits the filed
  policy document or any corpus byte.

## 6. Bleed verdicts on the control set (the population the new entries join)

- **Language predicate (r34 `LANG_TOKENS`/`LANG_ALLOW`/`LANG_FRAME`, copied from
  `reports/round-34/run-validation.py:283-308`): 0 hits** across all 23 entries.
  No grant/completion frame. Clean.
- **PROVINCE-derived screen: 2 hits, both adjudicated as conformant routing, not
  bleed** — `eschatology-world-end-systems.md:198` ("…are **systems this lane
  generates**; whether they are canon is lore-shokunin's decision") and
  `number-symbolism.md:138` ("→ lore-shokunin: reference only. Which number
  *means* what in canon is theirs"). Both are the refusal clause working as
  designed (`PROVINCE.md:16-20`; `corpus/QUALITY.md:13-20`), matching A02-r37's
  reading of the same pattern (`reports/round-37/adj/A02-entries-bleed.md:31`).
- **Ownership:** all 23 entries live under the lane-owned `myth-symbol`
  partition (`PROVINCE.md:9-11`); zero paths under `corpus/lessons/`,
  `tools/gates/frozen/`, sibling repos, or the world bible.
- **Group alignment:** every resolved extension-less mapping in the control set
  lands in the partition its field label names (myth→myth-symbol,
  language→linguistics, costume→culture-material, symbol→myth-symbol) — the
  policy §3 alignment leg holds for the block-read population too.
- **Wrapped fields:** 0 in the partition; corpus-wide exactly 1
  (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`), reproducing
  r39 Ca04 D1 and r42 `op/O09-scribe.md` §1 independently.

## 7. Process boundaries

Read-only throughout: `ls`/`find`/`grep`/`git`/`sha256sum` plus `python3 -B` over
corpus bytes. No `reports/round-*/run-validation.py` executed; no replay; no
re-freeze; no git mutation; no corpus staging; no packet-surface change. Writes
landed only under `reports/round-42/adj/` (this fragment + the instrument).

## Owed

- **`cov/C01`, `C03`, `C04` — three of the four target entries** — re-run this
  instrument against their output paths once they exist, under both token rules;
  verdict per entry. `cov/C02-entry-2.md` is verdicted in §4; the other three were
  absent at this cut, so this part of the mission's deliverable is unfulfilled.
  Owner: the seat (or integrator) that next holds the drafts. `to-verify`.
- **F-A01-1** → integrator / next calibration round: successor policy note
  widening §1's token rule + adding the zero-token-entry count to §3. Drafted in
  §5; no filed byte edited.
- **O09-scribe.md §1** independently corroborates the single wrapped field and
  the line-break mangling; this seat's recount agrees — no reconciliation owed.
- The mission's "mirror A02-r40" pointer resolves to the r37 entries-bleed
  fragment, not r40's PROVINCE seat; recorded, not absorbed.
- C02's draft verdict (§4) is **structural only**; its source audit is C05's and
  C08's assignment, not this seat's.

## Citations

- Assignment: `reports/round-42/targets.json` A01 (out `adj/A01-entries-bleed.md`);
  `reports/round-42/claims.json` claim C (myth-symbol 23→27, total 220→224) and
  `non_goals`.
- Adopted rule: `reports/round-39/calib/basename-couples-policy.md:14-25` (§1
  token rule + single-line extraction), `:35-36,268` (the 212/2504/2335/163/0/6
  census), `:38-48` (§2 two-tier four-class), `:101` (§5.6 glob fragments),
  `:22-25` (§3.1 reporting).
- D1: `reports/round-39/calib/Ca04-verify.md:78-88` (single-line extractor zeroes
  the wrapped field; 4 named, 2 existing, 2 phantom; line-break mangling of
  `tone-`+`prosody.md`); `reports/round-39/calib/Ca03-basename-policy.md:35-38`.
- Host instruments: `reports/round-19/audit/entry-audit.py:31` (MDREF_RE),
  `:75` (`re.search(r"^- couples:\s*(.*)$", text, re.M)`), `:87-95` (Tier 1);
  `sha256 e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`.
- Precedent: `reports/round-37/adj/A02-entries-bleed.md:7,23,31,33` (334 refs, 0
  unresolved, canon-routing language, `mechanic*` contextual adjudication);
  `reports/round-37/adj/A06-verify.md:29` (319 direct + 15 unresolved);
  `reports/round-37/adj/A12-gap-fill.md:9`.
- Same-wave target: `reports/round-42/cov/C02-entry-2.md` (fenced draft, proposed
  target `corpus/knowledge/myth-symbol/purity-pollution-systems.md`, which does
  not exist at `ac47c78`); `reports/round-42/cov/C08-verify.md` present;
  `reports/round-42/cov/C01|C03|C04|C05|C06` and `reports/round-42/scout/K02-myth-gaps.md`
  absent at this cut.
- Language predicate source: `reports/round-34/run-validation.py:283-308`.
- Boundaries: `PROVINCE.md:9-11,16-20`; `corpus/QUALITY.md:13-16` (coupling clause).
- Command outputs (2026-10-19, lane root, `TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD` →
  `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`; `find reports/round-42 -type f`
  → 5 files at first cut (13:00:19 -0300), no `cov/`; `ls corpus/knowledge/myth-symbol
  | wc -l` → 23; `python3 -B reports/round-42/adj/A01-scan-instrument.py` →
  myth-symbol control `203 direct / 99 extless / 0 unresolved / 0 ambiguous / 0
  language hits`, 8 zero-`.md`-token entries, 1 wrapped field corpus-wide;
  instrument block mode on the 212-entry set → `direct=2337 fallback=163
  unresolved=8`, single-line mode → `direct=2335 fallback=163 unresolved=6`
  (reproduces filed r39 Part 2 byte-for-byte); extension-less recount → 103/220
  entries, 57 distinct targets; scan of `.scratch/a01/C02-draft.md` (extracted
  from `cov/C02-entry-2.md`, 13:00:26 -0300) → `direct=35 extless=0 unresolved=0
  ambiguous=0`, 1 benign language hit at `:126`, 0 PROVINCE-screen hits;
  `python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`,
  `totals_ok True`, `footer_ok True`, exit 0,
  `readme_sha256 d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f`;
  `sha256sum corpus/README.md` → same digest (README byte-stable, rev 2.3,
  footer `25/23/25/29/24/94`, totals 220);
  `sha256sum reports/round-42/adj/A01-scan-instrument.py` →
  `2345a23d9f24409fb665b72339ecd1b4afdd27e332b205be2fc46995562c0ad7`.
