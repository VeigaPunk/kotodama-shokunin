# Review — component 09-eras-calendar (culture D2)

- reviewer: round-4 REVIEW worker (missing round-3 review)
- target: `examples/culture-d2/components/09-eras-calendar.yml`
- target revision: 1.1 (reviewed worktree)
- target sha256: `540a9339627fdcb802a7f59915a3c72e8234fff37c4a771783382af9c863b030`
- basis: `corpus/knowledge/culture-material/calendar-festival-systems.md`
- basis sha256: `8ae5bf3216a88f575af0b110164a0d396eaf27493e5abc7fe2d32f8feac90a39`
- repository base HEAD: `c610e0abd8edf90d6c6d86ebebdc7a7cba8d4a0b`
- status: **FINDINGS**, not a calendar-consistency pass
- counts: 5 findings; 5 design-gap flags; 10 issue entries; 0 triage-ledger rows
- canon: **NON-CANON** design review; lore-shokunin owns canon

Component pointers below refer to the target; corpus section references refer
only to the basis named above. Findings identify a conflicting assertion or an
unsupported inference. Flags identify missing rules, not demonstrated impossibilities.

A concurrent worker added revision 1.1's E0–E3/named-era mapping during final
verification. The digest check caught the change. The full 687-line revision was
re-read in bounded windows; its chronology, day rules, and seam rules are
unchanged. Citations below refer to that revision, not the earlier line offsets.

## Calendar classification and intercalation verdict

The three clocks at component lines 315–334 are deliberately different:
criterion-bound pastoral turns, observational solar stations, and borrowed lunar
trade months. This is a hybrid/mismatched-calendar design, not a locally specified
lunisolar calendar. The corpus explicitly permits procedural calendars and dual
mismatch (§1), and observational rather than fixed-cycle correction (§2).

Consequently, **absence of a 19-year cycle, twelve/thirteen local months, or a leap
month is not a violation**. Do not add a Metonic scheme just to satisfy this review.
The Wind-Speaker owns 3–12-day waits at the two seasonal gates (lines 361–369);
these reconcile herd readiness and sky readings. They are not demonstrated lunar
intercalation. Held turns instead suppress the doctrinal climb count (lines
112–119, 250, 394–399); they neither delete physical years nor repair lunar drift.

Using the corpus's mean constants, twelve lunations are 354.36708 days and fall
10.87512 days short of its tropical year (§1). That comparison explains why a
borrowed pure-lunar month may migrate against a seasonal salt opening. It is not
a claim that D2 must insert that many days. The lowland partner's correction
policy remains unprovided (G04); no lunar/solar synchronization can be certified.

## Findings

### F01 — HIGH: the half-open era table excludes its own sample present

- Evidence: component lines 100–110, 212–223, 559, 639, 686.
- `Two Counts: [D99, D103)` has four turn-coordinate units and excludes D103.
  ER-08 nevertheless calls that interval five turns, and DC-01/the index date the
  sample as `Two Counts 5, the 103rd descent`. The replay below returns `false`
  for membership; finite era spans total 102, not the validation's inclusive 103.
- The relative ordinal `103 - 99 + 1 = 5` is internally sensible. Its use with an
  exclusive D103 upper bound is the defect. A snapshot cutoff must not silently
  double as an ended era's boundary.
- Resolve by choosing one coordinate convention: retain half-open bounds and
  separate the ongoing era's open end from the sample timestamp, or explicitly
  distinguish completed durations from the running fifth turn. Reconcile the
  table, ER-08, fixture, and VAL-02; do not merely relabel the replay PASS.
- Corpus criterion: §8 (era/epoch as statute), §11.6 and §11.9 (dating mechanics
  and a replayable calendar).

### F02 — MEDIUM: the half-turn artifact does not follow from the seam rule

- Evidence: component lines 155–163, 245, 347, 360, 500–505, 547–548, 572.
- ER-03 says Salt Turn ends **mid-turn**, leaving `Salt Turn 42` only half a
  turn. EL-02/SEAM-HALF instead make a summer announcement effective at the
  closing descent; CAL-GATE-9/FES-03 close the turn at penning. The elapsed
  half-turn from announcement to effect is not itself a half-length old-era turn.
  The D31/D73 endpoints provide no separate sub-turn effective timestamp.
- Resolve whether “descent” means its opening gate, its penning close, or an
  ordinal label. Record the announcement and legal effective event separately,
  then derive ART-01's duration. If the rule really changes eras only at the
  annual close, preserve the announcement tail without calling it a mid-turn end.
- Corpus criterion: §8 (the count is a statute) and §11.6 (era mechanics must
  support the double-dated artifact). This is a timing-model inconsistency, not
  a ban on invented short years.

### F03 — MEDIUM: T5 ratification and emergency effectiveness are unreconciled

- Evidence: component lines 188–199, 245, 248, 505, 548.
- EL-05 says the Keeper's storm-season death is ratified **at the next moot**.
  ER-06 says the D78 T5 seam is announced at the descent assembly and effective
  **at that close**; SEAM-DAYS calls that the emergency T2/T5 form. No rule says
  whether this is a provisional era before later ratification, an exception to
  EL-05, or a seam whose effect must wait for the moot.
- This matters for contracts made between the descent assembly and that moot:
  their legally usable era cannot be derived from the trigger law alone.
- Resolve the emergency authority and give the event an ordered record:
  death → announcement → carried formula → effective event → ratification.
  If ratification is retrospective, specify its effect on interim documents.
- Corpus criterion: §8 (era as statute), §11.6; the missing legal distinction
  should not be resolved by assuming that the two dates mean the same thing.

### F04 — MEDIUM: DC-T2 conflates annual count gaps with held-day evidence

- Evidence: component lines 112–119, 250, 361–369, 563, 569, 573.
- The board's D95 gap establishes a **held turn**, an omission from the climb
  count. CAL-HELD-D is a different object: a 3–12-day prohibition at a gate.
  DC-T2 uses the board gap while testing a sale purportedly inside those days,
  but no day-level declaration or interval is supplied. An annual gap cannot
  establish which days of that year prohibited sales.
- DC-05 still legitimately voids a document that explicitly dates its own sale
  “inside the still”; retain that facial test. Do not present the annual gap as
  independent corroboration. Add or reference a dated Wind-Speaker declaration,
  gate record, or witnessed held-day interval if corroboration is intended.
- Corpus criterion: §1 (distinct clocks), §2 (the authority owns the inserted
  unit), §6 and §11.9 (day-level rules must be executable).

### F05 — MEDIUM: D95 is both already ratified and awaiting an unnamed ruling

- Evidence: component lines 211, 386, 391, 682.
- ER-07 states that D95 **is ratified retroactively at D99**. The handoff asks
  for “the D108 muster ruling on the held turn D95” as a still-open story
  decision. With no appeal/reopening distinction, the same legal status is
  simultaneously settled before D103 and left for a future muster.
- Resolve whether D108 hears an appeal or revisits a D99 decision, or whether
  D99 did not ratify it. Keep the historic status separate from any future
  factional challenge; this review does not choose which faction is right.
- Corpus criterion: §2 (ownership of inserted/withheld time), §8 and §11.6
  (office terms and dating depend on enacted decisions).

## Design-gap flags — not additional confirmed contradictions

### G01 — Held-day numbering and five-day continuity are unspecified

Component lines 335–348, 361–381, 500–525, 559–563 call held days “not counted”
but do not say whether the five-day hand pauses, continues underneath, or restarts
when the gate opens. The generic date has a stage and held state, not a unique
held-day index. A wait of five versus six days can therefore produce different
post-wait contract days depending on an unstated convention. Also specify whether
festival permissions override or intersect CAL-H1..H5; FES-03's smoke-only oath
condition does not state the weekday precedence. Supply a worked entry/exit
example, without assuming that every observed festival must use a fixed date.
Corpus: §6, §11.3, §11.5 and §11.9.

### G02 — The 3–12-day reconciliation has no out-of-range outcome

Component lines 318, 356–369, 396 assign authority and a finite wait, which is a
good start. They do not say what happens if the sky event occurs but the herd is
still unready on day 13, if observation is unavailable, or if disagreement clears
before day 3. Declare an exceptional extension, cancellation, substitute witness,
or a criterion that actually bounds the mismatch. This is a missing edge rule,
not evidence that an observational calendar needs fixed-cycle intercalation.
Corpus: §2 and §11.2/§11.9.

### G03 — Winter and the annual count boundary need an explicit state

Component lines 317–324, 342–360, 456, 469, 489–505, 559–566 place return/turn
closure in autumn, solar inner-account closure at the winter solstice, and the
next departure in spring. DC-01 allows only an ascent/descent stage. It is not
stated whether a winter-shelter event belongs to the preceding turn, a new turn,
or an inter-turn period, nor when descent/climb/era-year ordinals advance.
Separate sacred, herd, and accounting new years if intended; give a date just
after penning, at the solstice, and before the next sky-gate. Multiple new years
are allowed, not a defect in themselves. Corpus: §8 and §11.4/§11.9.

### G04 — The borrowed-moon document is too coarse to certify conversion

Component lines 328–334, 562, 574, 604–605 provide a borrowed **month**, not a
worked cross-calendar day. No lowland year/epoch, month-start convention,
month-day, correlation event, or possible duplicate/leap-month discriminator is
given. If the partner is pure lunar, record that seasonal month drift is accepted;
if it is lunisolar, reference its intercalation authority and distinguish any
repeated month. Do not silently invent the partner's system. Either label ART-03
a month-resolution correlation only, or supply one fully disambiguated example
using a named observed correlation. Exact conversion is currently unverified.
Corpus: §1–§2, §9 (double dating), §11.6 and §11.8/§11.9.

### G05 — The death-seam ceremony lacks a complete officiant/pause trace

Component lines 536–549 require a Keeper's recital even when T5 means the Keeper
has died. No acting Keeper or succession reference is supplied. The sequence
also places a “no formulas, no marks until the stage gate” mourning pause after
the carried formula and mark; a descent-close seam has no identified next stage
gate within that completed turn. State who performs SEAM-07, when the pause
starts, which gate ends it, and which steps defer. This is a missing ritual
execution path; mourning after a preliminary mark is not inherently impossible.
Corpus: §8 and §11.6/§11.9 (a calendrical statute needs an executable occasion).

## Checked and coherent on the reviewed bytes

- Ruby/Psych parses the complete YAML. Parsing is not a semantic pass.
- D103 minus held turns `[74, 78, 84, 95]` yields official C99; restoring them
  yields C103. These occupy the declared C76–100 and C101–125 rungs respectively.
- The Top at C126 is 27 official climbs or 23 restored climbs away.
- D90, D99 and D108 are multiples of nine. Counting muster cadence by descents,
  not disputed climbs, avoids a four-year factional offset; “summer moot of a
  designated descent-year” is a coherent reading, not a seasonal contradiction.
- The ordinary seam has an authority, place, reveal object, broken banner,
  audibility/smoke condition, retransmission, and herald-lag convention. A failed
  formula has a waiting label and cannot license the new name on documents.
- Eclipse re-ratification is explicitly not a new seam (SKY-05/SEAM-REPEAT), so
  repeating that formula does not itself breach the one-seam-per-turn Quiet Rule.
- Non-canon status, the invented nature of rung arithmetic, retrospective early
  labels, and the unresolved cosmological outcome are disclosed. No real-world
  ritual or historical intercalation example has been independently verified here.

## Verification and limits

Read the complete component in six windows of at most 120 lines and the calendar
basis in two such windows. Manual traces covered a summer announcement, a T5
descent seam, a failed formula, a held-day sale, and the D103 fixture. F01, F03,
F04 and the gaps prevent a full clean replay; they are not hidden by parse success.

This read-only arithmetic probe was run against the pinned target:

```bash
ruby -ryaml <<'RUBY'
d = YAML.load_file('examples/culture-d2/components/09-eras-calendar.yml')
spans = d.fetch('era_dates').values.select { |a,b| a && b }.map { |a,b| [a.delete_prefix('D').to_i,b.delete_prefix('D').to_i] }
a,b = d.fetch('era_dates').fetch('Two Counts').map { |v| v.delete_prefix('D').to_i }
held = d.fetch('held_turns').fetch('list')
official = 103 - held.count { |v| v <= 103 }
puts 'YAML: PASS'
puts "half-open named turns: #{spans.sum { |x,y| y-x }}"
puts "Two Counts length: #{b-a}; inclusive ordinal at D103: #{103-a+1}"
puts "D103 inside [D99,D103): #{a <= 103 && 103 < b}"
puts "counts at D103: official C#{official}; restored C103"
puts "Top distances: official #{126-official}; restored #{126-103}"
puts "D90/D99/D108 multiples of nine: #{[90,99,108].all? { |v| v%9 == 0 }}"
RUBY
```

Observed output (exit 0; this is a probe, not an executable culture gate):

```text
YAML: PASS
half-open named turns: 102
Two Counts length: 4; inclusive ordinal at D103: 5
D103 inside [D99,D103): false
counts at D103: official C99; restored C103
Top distances: official 27; restored 23
D90/D99/D108 multiples of nine: true
```

Only this review was created. The component, corpus, gates, LOG.md, and other
workers' files were not edited; no commit was made. No gate battery was run or
weakened by this worker. The round closer must re-run the unchanged gates, and
manual findings above remain open regardless of a machine gate's result. Any
change to either pinned input requires re-review. These recommendations do not
canonize D2 or select the correct in-world count.
