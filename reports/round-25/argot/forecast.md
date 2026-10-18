# R25-D01 — the argot-derivation forecast, enumerated

Worker: R25-D01..D04 (D axis, argot analysis). Lane `kotodama-shokunin`, round 25.
Date: 2026-10-18. Baseline revision `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` (claims.json);
worktree at the time of measurement `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`, `git status --porcelain` empty.

Scope: this file records **what round 17 asked for**, with the exact source line for every element,
so the delta file can name what was and was not delivered. It makes no claim about what is on disk
today (that is `current-state.md`).

## 1. Sources

| # | file | sha256 (measured 2026-10-18) | what it fixes |
|---|---|---|---|
| S-1 | `reports/round-17/d4/design-brief.md` | `a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f` | the requirement, the measurable signature, the control, the id |
| S-2 | `reports/round-17/d4/design-language.md` | `cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc` | the two operations' **exact algorithms**, the 11 worked derivations, the quote-slot law |
| S-3 | `reports/round-17/d4/typed-support-1.md` | `16f8bb0441a367970b47090cee00e73c7f69fed677941a9ac5e00b066f11b60c` | names the leg as one the D2 engine never carried (§6.4) |
| S-4 | `reports/round-19/knowledge/analyst-3.md` | — | the first post-hoc read: forecast, not delivered (§3, §6) |

Command for the digests (cwd = lane root):

```
sha256sum reports/round-17/d4/design-brief.md reports/round-17/d4/design-language.md reports/round-17/d4/typed-support-1.md
```

## 2. The requirement, element by element

`reports/round-17/d4/design-brief.md:296-310` — **Δ3 "derivation-checked forms (a third derivation relation)"**:

| element | verbatim requirement | source line |
|---|---|---|
| F-1 third relation | quote forms are **derived** from their plain base by one of two declared, fully specified operations | `design-brief.md:301-302` |
| F-2 the two operations | `head2` (**first two syllables** of the base) for measure words; `reverse` (**string reversal**) for the numeral series | `design-brief.md:302-304` |
| F-3 the fields | the derivation is **checked** through `derived_from` + `derivation` fields | `design-brief.md:303` |
| F-4 relation scope | a relation between **two records of the same packet**, which D2 never graded | `design-brief.md:304` |
| F-5 signature (a) | every derived quote form's check **passes in the delivered packet (zero fails)** | `design-brief.md:305-306` |
| F-6 signature (b) | the **coverage block reports `derived_forms` and `derived_ok` counts that agree** | `design-brief.md:306-307` |
| F-7 control | a fixture whose quote form **≠ `apply(op, base)`** → **FAIL**, id **`D4L-ARGOT-DERIV`** (new id, **control-only**; the delivered packet carries no such row) | `design-brief.md:308-310` |
| F-8 required-controls battery | row **C-02**: "quote form ≠ `apply(op, base)`" → FAIL `D4L-ARGOT-DERIV` | `design-brief.md:456` |

**Answer to "what was D4L-ARGOT-DERIV to mean":** a *new* finding id, emitted **only in the negative
control** — the D4 packet's own debt set was to stay free of it. It is a FAIL-class id (not a hold),
because a non-replaying quote form is a defect, not an open question. It grades the Δ3 relation
specifically: a form that claims to be derived from a base but is not what the declared operation
yields. It is *not* the same id as the naming gate's `DERIV-REPLAY` (which grades a **name's**
`formation` chain) nor `D4L-REGISTER-UNRESOLVED` (which grades a **slot** whose form is owed); Δ3
sits between them — form present, slot filled, but the derivation arithmetic wrong.

## 3. The algorithms, as fixed by `design-language.md` §5 (`:186-217`)

The brief "fixes the operations; this design fixes their **exact algorithms**" (`:188`).

- **`head2`** (`:191-196`) — "the first two syllables of the base". Syllabification is
  **maximal-onset**: a consonant is taken as the onset of the following syllable whenever that yields
  a legal syllable. Worked instance: `saalumi` → `saa.lu.mi` → **`saalu`** — explicitly **not**
  `saalum`, "which a maximal-coda reading would give". The algorithm is stated because the two
  readings disagree, "and a derivation that is not deterministic cannot be checked".
- **`reverse`** (`:198`) — **character-level string reversal** of the base.
- **The checker's standing** (`:200`) — "Eleven worked derivations (**all recomputed by the checker,
  all agreeing**)". So the forecast asserts a checker existed in the design pass; the design receipt
  R-2 (`design-language.md:588`) records "13 fields; **11/11 derivations reproduce**; 0 exact
  collisions … zero unused inventory tokens" from `.scratch/check-d4-language2.py` (a scratch
  artifact, superseded receipt R-6).
- **The spellability law** (`:216-219`) — every numeral was chosen so that its own reversal is a legal
  D4 form; `rak` dropped (its reversal `kar` carries an unlicensed coda `/r/`), `kas` dropped (exact
  D2 fixture form). "A derivation the language cannot spell is not a derivation, it is a defect."

### 3.1 The 11 worked derivations (verbatim table, `:200-215`)

| base | op | quote form | slot | note |
|---|---|---|---|---|
| saalumi (X02) | head2 | saalu | quote | the QN-01 form: carries the length mark |
| min (X13) | reverse | nim | quote | numeral one |
| kus (X14) | reverse | suk | quote | numeral two |
| nam (X15) | reverse | man | quote | numeral three |
| nes (X16) | reverse | sen | quote | numeral four |
| sam (X17) | reverse | mas | quote | numeral five |
| mus (X18) | reverse | sum | quote | numeral six |
| kin (X19) | reverse | nik | quote | numeral seven |
| sun (X20) | reverse | nus | quote | numeral eight |
| samun (X21) | reverse | numas | quote | numeral nine |
| makun (X22) | reverse | nukam | quote | numeral ten |

The base ids `D4-X02`, `D4-X13..X22` are **design-language ids**: the D4 design writes the lexicon in
its own `D4-Xnn` numbering (`design-language.md` §6.1 field tables, 74 lexemes; the design file is the
only place these ids occur — `grep -rc "D4-X" examples/ tools/` → 0 files, 2026-10-18). The delivered
packet numbers the same records `L-nn`.

## 4. The rest of the forecast the argot leg is embedded in

Δ3 is the third relation, not the whole of the round-17 language forecast. Two neighbouring
forecasts are named here because the delta file must not silently absorb them:

- **Δ1 class 2, register-scoped slots** (`design-brief.md:254-282`) — a supplied, inventory-clean
  quote form admissible only in a quote slot; a record carries a register pair `<id>#plain` /
  `<id>#quote`; a plain slot whose doublet is owed yields exactly one hold, `D4L-REGISTER-UNRESOLVED`,
  per owed slot (`:269-272`, `:560`). This is the *slot* half of the argot design and is the sibling
  of Δ3's *arithmetic* half. The forecast's six owed slots are `AL-01#plain .. AL-06#plain`
  (`design-language.md:560`).
- **Δ2 slot cardinality** (`design-brief.md:283-295`) — exactly one supplied checked form per
  `(owner, slot_ref)`; the pair relation carried as the packet fact `doublet_of`; two supplied forms
  in one slot → exit 2 `D4L-DATA`.
- **The six argot loans AL-01..AL-06** (`design-language.md:406-424`) — supplied in the quote slot,
  plain doublet owed, every form inventory-clean. AL-02 is the three-field donor row
  (ultimate `khar` / immediate `west-stage-1` / carrier `southern broker network`, all distinct);
  AL-03 carries `ultimate: null` and is **held, not failed** (Δ4's B2 branch).
- **The name-side argot** (`design-language.md:485-511`, §7.1-§7.3) — eight plain bases
  `kani, masu, niru, saka, mika, kura, nusi, musa` whose **quote names** are their `reverse`s
  (`inak, usam, urin, akas, akim, aruk, isun, asum`), used "**only inside the quote register** and
  never written on the rod" (`:509-510`). `tani` dropped (`inat`, unlicensed `/t/` coda); `risu`
  dropped (`usir`, `/r/`).
- **The design's own honesty clause** (`design-language.md:580-581`) — "exit 0 from the D4 gate is a
  structural pass with open holds printed verbatim — **never a clearance**."

## 5. Where the forecast was later read

- `reports/round-17/d4/typed-support-1.md:274-290` (§6.4 "The D4L-* vocabulary and the projector legs
  the engine does not carry") lists "**argot-derivation check (Δ3)** — `derived_from` + `derivation`
  (`head2`, `reverse`) between two records of the same packet → `D4L-ARGOT-DERIV` **in controls
  only**" beside the register leg, the register-era check, the rank kinds and the material route hold.
- `reports/round-19/knowledge/analyst-3.md:87-105` reads it back as "**design forecast — mark
  `(to-verify)`**" and measures the delivered side: "no delivered D4 byte carries a `D4L-ARGOT-DERIV`
  row (`grep -c "ARGOT-DERIV" examples/culture-d4/packet.d4.yml` → 0)". Its §6 puts the argot
  derivations under "**Forecast (mark `(to-verify)`)**" and the CX-01..03 rule table, the naming
  gate's replay leg and the adapter's text-transform under "Delivered".
- `reports/round-19/integration/d4-lessons-entry.md:85-92` states the lesson in one line: "a
  derivation is replayable only if the operation and its input are both machine-readable — a prose
  rule cannot be replayed, and an unreplayable derivation is not a derivation."

## 6. Counting command for this file

```
grep -n "Δ3\|D4L-ARGOT-DERIV\|derived_from\|derived_forms\|derived_ok" reports/round-17/d4/design-brief.md
grep -n "^## 5\.\|head2\|reverse" reports/round-17/d4/design-language.md
```
