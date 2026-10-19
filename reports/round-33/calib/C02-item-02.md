- Seat: C02 | executor | claim C | date 2026-10-19 | baseline 139e3b6

# C02 — disposition of open item 2 (canonical id OI-02, `head2` empty proper domain)

**Dependency note (read first).** K03's canonical table had not landed at this
seat's first listing (`ls reports/round-33/calib/` → empty; that listing ran
before this seat's first `date -u` stamp, 2026-10-19T03:56:42Z). It landed
while this seat was still measuring: `reports/round-33/calib/K03-open-items.md`
mtime `Oct 19 00:55` local = `03:55Z` (local = UTC−3, established by the
`date -u` stamp against the `ls` clock). Item 2 was therefore
resolved twice and reconciled: (a) independently, from the two authoritative
enumerations — `reports/round-32/dossier-d13-operator-decisions.md:131`
(Decision 4 table, row 2) and `reports/round-33/claims.json:44` (`head2` listed
second in both) — and (b) against K03's landed table, which assigns it the
canonical id **OI-02** (`reports/round-33/calib/K03-open-items.md:63`) with
class `design-debt`. Both resolutions name the same item, so **no remap is
owed**; K03 itself lists OI-01..OI-03 as carry candidates
(`reports/round-33/calib/K03-open-items.md:75-78`).

## 1. Item identity

| field | value |
|---|---|
| id (canonical, K03) | `OI-02` |
| label (this seat) | `C02-HEAD2-EMPTY-DOMAIN` |
| item | `head2` (first two syllables) has an empty proper domain over the delivered tree: nearly every delivered form is ≤2 syllables, so `head2(form) == form` is an identity, not a derivation |
| origin round | r26 (register stratum) |
| class | `design-debt` |
| D13 pointer (re-verified) | `reports/round-26/register/design.md:228` (RL-2 row); `reports/round-26/register/rules.md:89-96` (§3.2) |
| K03 pointer (re-verified) | same two, `K03-open-items.md:63` |
| filed D13 text | "`head2` empty proper domain \| r26 \| `reports/round-26/register/` named gaps" — `reports/round-32/dossier-d13-operator-decisions.md:131` |

## 2. Status quo re-verified at HEAD (all commands 2026-10-19, HEAD `139e3b6`)

`git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`, identical to
the round's declared baseline (`reports/round-33/claims.json:8`).

### 2a. The pointers resolve and still say what the dossier says they say — VERIFIED

```
$ awk 'NR==228 {printf "%d\t%s\n", NR, $0}' reports/round-26/register/design.md
228	| **RL-2** | `head2` has an **empty proper domain**: 59 of 62 delivered forms are ≤2 syllables, so `head2(form) == form` is an identity, not a derivation | `review.md` §4 |
$ awk 'NR>=89 && NR<=96 {printf "%d\t%s\n", NR, $0}' reports/round-26/register/rules.md
89	### 3.2 Why `head2` is not used (RL-2)
90
91	`head2` is retained in the gate as a declared operation (it is the forecast's,
92	and the gate's selftest re-derives the design's 11 worked rows from it), but
93	this design does **not** build any register form with it, because over the
94	delivered tree it is an identity, not a derivation — 59 of 62 delivered forms
95	are ≤2 syllables (`review.md` §4). A stratum built on `head2` would be a
96	stratum of unchanged words.
```

The finding itself, its measurement, and its in-round disposition are filed:
`reports/round-26/register/review.md:99` ("Finding RD-3 — `head2` has an empty
proper domain over the delivered tree"), the census output block at
`review.md:104-110` (the census command block; three forms ≥3 syllables at
`:106-108`, "count: 3 of 62" at `:109`, "identity, not a derivation: 59 of 62"
at `:110`), and the disposition table row `review.md:223`
("`lengthen` used instead; `head2` declared-but-unused"). The re-scope is
filed at `reports/round-26/register/execution-3.md:70` ("`head2` **dropped** and
replaced by `lengthen`, because `head2` has no proper domain over the delivered
tree").

Digests of the cited bytes (this seat, HEAD):

```
$ sha256sum reports/round-26/register/design.md reports/round-26/register/rules.md \
             examples/culture-d4/components/04-lexicon.yml examples/culture-d4/packet.d4.yml
27d23fa67d0bb920d1841d25c82b09919419ef58ef3b2f75494d950f3b5bb55a  reports/round-26/register/design.md
535cf7a981c5cf7d8c824454cb46319745bf096342a203add998a34842b026ef  reports/round-26/register/rules.md
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
```

### 2b. The debt is still live, and its proper domain is still exactly three forms — VERIFIED by re-execution

The r26 census script survives in scratch (`.scratch/r26-d-reg/final.py`, dated
2026-10-18) and reads the **live** packet (`final.py:4`), so re-running it is a
status-quo check:

```
$ python3 -B .scratch/r26-d-reg/final.py | tail -12
forms with >=3 syllables (head2 has a PROPER domain only here): [('L-48', 'haitun', ['ha', 'i', 'tun']), ('NM-01', 'tumhai', ['tum', 'ha', 'i']), ('NM-05', 'haitik', ['ha', 'i', 'tik'])]
count: 3 of 70

== head2 identity check over the delivered tree ==
head2(form)==form (identity, not a derivation): 67 of 70

== the design's own row ==
head2(saalumi) = saalu   (design says saalu)
```

**The same three forms** the r26 review filed; only the denominator moved
(62 → 70). Provenance of that move, measured:

```
$ git rev-parse --short 4f09c99^        # the r26 declaration revision
1ad491a
$ git show 1ad491a:examples/culture-d4/packet.d4.yml > /tmp/pkt-parent.yml
$ python3 -B -c "…load_yaml(open('/tmp/pkt-parent.yml'))…"   # naming-collision-gate loader
parent packet lexicon records: 54 names: 8
parent has L-55..L-62: []
```

So the r26 filed set was 54 lexicon records (L-01..L-54) + 8 naming records
(NM-01..NM-08) = **62**, and at HEAD the same script's set is 62 lexicon
records (the eight register records L-55..L-62 landed by r26's own admit
commit, `git log`: `4f09c99` on `04-lexicon.yml`) + the same 8 naming records =
**70**. All eight added records are ≤2 syllables, so they add eight identities
and change nothing about the domain.

Independent re-derivation at HEAD with the gate's own syllabifier (not the
scratch script's), over the exact r26 set definition — an exact reproduction of
the filed numbers:

```
$ python3 -B -c "… import tools/gates/argot-derivation-gate.py as adg; recs = 54 lexicon + 8 naming …"
set size: 62 = lexicon 54 + naming 8 [('NM-01','tumhai'),('NM-02','kalker'),('NM-03','samren'),('NM-04','mestum'),('NM-05','haitik'),('NM-06','meslun'),('NM-07','kalnes'),('NM-08','salwer')]
>=3 syllables: 3
   ('L-48', 'haitun', ['ha', 'i', 'tun'])
   ('NM-01', 'tumhai', ['tum', 'ha', 'i'])
   ('NM-05', 'haitik', ['ha', 'i', 'tik'])
head2 identity: 59 of 62
```

`59 of 62` is byte-for-byte the filed r26 number. The two methods agree on the
proper-domain set.

### 2c. No live defect: the gates are green and no delivered record uses `head2` — VERIFIED

```
$ python3 tools/gates/argot-derivation-gate.py --selftest      # exit 0
selftest: 27/27 checks passed
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # exit 0
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
$ python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml      # exit 0
coverage: examples/culture-d4/packet.d4.yml law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0
$ grep -c "op: head2" examples/culture-d4/packet.d4.yml            # 0
$ grep -c "derivation: head2" examples/culture-d4/packet.d4.yml    # 0
```

The gate's own docstring states the same fact it is measured to enforce:
"no delivered `derived_from`/`derivation` record in any family names `head2`
(the D4 register stratum uses `reverse` and `lengthen`)"
(`tools/gates/argot-derivation-gate.py:65-66`).

### 2d. The debt is disclosed in the delivered tree, not hidden — VERIFIED

```
$ grep -n "derivation_ops" examples/culture-d4/components/04-lexicon.yml
269:  derivation_ops: [head2, reverse, lengthen]
270:  derivation_ops_note: "… `head2` is declared but unused: over the delivered tree it is an identity, not a derivation (reports/round-26/register/review.md section 4)."
```

Same bytes in the live packet: `derivation_ops:` at
`examples/culture-d4/packet.d4.yml:277`, `- "head2"` at `:278`, the note at
`:281`.

### 2e. History — nothing has re-opened or changed the item since r26

```
$ git log --oneline -4 -- reports/round-26/register/design.md
4f09c99 round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)
$ git log --oneline -4 -- examples/culture-d4/components/04-lexicon.yml
11df1fd round-30 wave integration: QREG landing, speaker candidate, law baseline, craft synthesis draft, telemetry
4f09c99 round-26: admit D/O/C …
3dd3754 round-17: C/O verified; D rejected …
```

`design.md` is untouched since r26; the component was touched at r30 (QREG
landing) but its record count is 62 at both `4f09c99` and HEAD (`git show
4f09c99:examples/culture-d4/components/04-lexicon.yml | grep -c "{id: L-"` → 62),
and the live disclosure at `:270` is intact.

## 3. Disposition

### 3a. Why this carries rather than fixes — the bounded-fix test fails on both options

The item admits exactly two fix shapes, and both are measured here:

**Option A — give `head2` a proper domain** by authoring ≥3-syllable delivered
forms. That is content generation (a design decision over the delivered lexicon,
not a calibration fix), and it edits `04-lexicon.yml`, which regenerates
`packet.d4.yml`. The packet digest is **pinned live**:

```
$ sha256sum examples/culture-d4/packet.d4.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3
# == the digest recorded in reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv:2 and :4
$ TMPDIR=/tmp python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv
REPLAY OK: 4/4 rows reproduced the recorded verdicts (reproduction only: a reproduced red verdict stays red)   # exit 0
```

Four currently-green frozen rows replay against those bytes; the same packet
bytes are mirrored at
`tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml`
and
`tools/gates/expected/register-law-gate/r30-post/examples/culture-d4/packet.d4.yml`
(`grep -rl head2` hits both). Any edit to the component therefore drifts a live
pin generation — a re-pin cascade, not a bounded fix. (Method note: with the
seat's prescribed `TMPDIR=$PWD/.scratch` the replay tool refuses with
`mirror_unsafe` and exit 2 because its mirror root must sit outside the repo;
`TMPDIR=/tmp` is what produced the 4/4 result above. Recorded, not filed as a
defect claim.)

**Option B — retire `head2` from `derivation_ops`**
(`04-lexicon.yml:269` / `packet.d4.yml:277-278`). Probe on a scratch copy of the
live packet with exactly that one line removed (`diff` → `278d277`, nothing
else):

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/c02/probe-nohead2.yml    # exit 0
coverage: … records=187 … violations=0 rule_holds=0
$ python3 tools/gates/register-law-gate.py .scratch/c02/probe-nohead2.yml       # exit 0
coverage: … law_rows=5 … findings=0
```

So the gates neither require nor protect the declaration — but Option B still
(i) drifts the same pinned packet digest, (ii) contradicts the r26-filed design
intent, which keeps `head2` declared on purpose (`rules.md:91-92`: it is the
forecast's operation and the gate's selftest re-derives the design's 11 worked
rows from it — selftest rows `design-table-rederived-11` and the four
`head2-*` rows are green in the 27/27 above), and (iii) deletes a disclosure
rather than repairing anything.

**Conclusion.** The r26 round already dispositioned this item in-round the only
way that was in scope — route around it (`lengthen` for the fire axis,
`review.md:223`) and disclose it in the delivered tree
(`04-lexicon.yml:270`). No defect is live (gates green, zero records declare
`head2`). Neither fix shape is bounded within a calibration round, and a seat
"fixing" it would be making a design/content decision and breaking a green pin
generation. **Carried.**

### 3b. Disposition record (ledger row for `C15-ledger-draft.json`)

| field | value |
|---|---|
| id | `OI-02` |
| item | `head2` empty proper domain (59/62 identity at r26; 3 of the same 3 forms ≥3 syllables at HEAD) |
| origin | r26 — `reports/round-26/register/design.md:228` (RL-2), `review.md:99` (RD-3) |
| pointer (re-verified) | `reports/round-26/register/design.md:228`; `reports/round-26/register/rules.md:89-96`; secondary: `reports/round-26/register/review.md:99,223`, `reports/round-26/register/execution-3.md:70`, live disclosure `examples/culture-d4/components/04-lexicon.yml:269-270` |
| status_quo_check | re-verified at HEAD `139e3b6`, 2026-10-19 — pointers resolve verbatim (§2a); census re-executed: same 3 proper-domain forms, `3 of 70` / identity `67 of 70` on the live packet, and `3 of 62` / identity `59 of 62` on the exact r26 set definition (§2b); gates green, 0 records declare `head2` (§2c); disclosure intact (§2d) |
| disposition_class | `carried-with-owner+reason+next-touch` |
| evidence | `reports/round-33/calib/C02-item-02.md` §2a-2e and §3a; digests in §2a; `MANIFEST.tsv:2,:4` + `REPLAY OK: 4/4` |
| fix_draft | none — §3a: no bounded fix exists in round-33 scope; do not emit a `fix_draft` key for this row |
| owner | **operator** (D13 Decision 4 preamble: "owner unassigned (operator's call: future regimen, manual pass, or accepted-as-recorded)" — `reports/round-32/dossier-d13-operator-decisions.md:125-126`) |
| reason | design debt by design, already routed around and disclosed: the r26 stratum uses `lengthen` instead and keeps `head2` declared-but-unused (`rules.md:91-96`), the live tree states the condition (`04-lexicon.yml:270`), no gate red and no record declares `head2` (§2c); either fix shape edits `04-lexicon.yml` → the live-pinned packet digest `aac91246…` drifts and the green r31-post replay rows break (§3a), and Option A is content generation outside a calibration disposition |
| next_touch | (a) operator Decision-4 call at regimen-2 close (accept-as-recorded, or fund a proper-domain delivery); or (b) a future regimen's register/design pass, which must land as: author ≥3-syllable delivered forms (or formally retire the op) at `examples/culture-d4/components/04-lexicon.yml:269`, regenerate `packet.d4.yml`, freeze a **successor** pin generation (never an in-place edit) for the r30-post register-law baseline and the r31-post MANIFEST rows, re-run `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` and `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` expecting exit 0, and re-run the standing check in §3c |

### 3c. Optional standing check (draft only — not applied, not required by claim C)

A one-command drift check the integrator may add as a leg of round-33's own
`run-validation.py` (a new file — no pin cascade). It reproduces the filed r26
numbers exactly, so any future movement of the proper domain or the identity
count is caught:

```
python3 -B -c "
import importlib.util, re
s=importlib.util.spec_from_file_location('adg','tools/gates/argot-derivation-gate.py')
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
lex=[(i,t) for i,t in re.findall(r'\{id: (L-[0-9]+), term: ([a-z]+)[,}]', open('examples/culture-d4/components/04-lexicon.yml').read()) if int(i.split('-')[1])<=54]
lines=open('examples/culture-d4/components/05-naming.yml').read().splitlines(); nm=[]
for n,l in enumerate(lines):
    g=re.match(r'\s*- id: (NM-[0-9]+)', l)
    if g:
        for l2 in lines[n:n+12]:
            g2=re.match(r'\s*name: ([a-z]+)', l2)
            if g2: nm.append((g.group(1), g2.group(1))); break
recs=lex+nm
print('>=3 syllables:', len([1 for i,t in recs if len(m.syllabify(t))>=3]), 'of', len(recs))
print('identity:', len([1 for i,t in recs if m.op_head2(t)==t]), 'of', len(recs))
"
# expected at HEAD 139e3b6: ">=3 syllables: 3 of 62" then "identity: 59 of 62"
```

### 3d. Named finding from this seat (record-only)

**C02-F1 (minor, method — no filed byte to edit).** The r26 census script
(`.scratch/r26-d-reg/final.py`) is not a stable replay tool across revisions:
it reads the live packet (`final.py:4`), so its denominator moves with the tree
(62 at `1ad491a` → 70 at HEAD) while the filed numbers stay bound to their own
set. Re-running it must be read as a *set* comparison, never a count comparison.
The filed r26 "59 of 62" remains true for its own set — verified by
reconstruction: 54 lexicon + 8 naming = 62 at `1ad491a` (§2b). Scratch is not
durable evidence, so this fragment records the reconstruction instead of citing
the script as a receipt.

## Owed

- none — K03 landed mid-flight (`reports/round-33/calib/K03-open-items.md`,
  2026-10-19T03:55Z) and item 2 maps to its `OI-02` without remap; no missing
  dependency remains.

## Citations

Files read (all at HEAD `139e3b662900557afe54f632b468619593dc9fcb`, 2026-10-19):

- `reports/round-33/targets.json` (C02 seat object), `reports/round-33/claims.json:8,42-50`
- `reports/round-33/calib/K03-open-items.md:63,75-78` (canonical id OI-02, carry-candidate list)
- `reports/round-32/dossier-d13-operator-decisions.md:123-138` (Decision 4 table; row 2 at `:131`; owner preamble `:125-126`)
- `reports/round-32/dossier-d11-shonen-boxes.md:114-118` (box-2 standing design debts), `:203-208` (summary)
- `reports/round-26/register/design.md:228` (RL-2), `rules.md:89-96` (§3.2), `review.md:99,104-107,121,223` (RD-3 + census output + disposition), `execution-3.md:70` (F-2 re-scope), `forms.md:19,25-32` (register forms use `lengthen`)
- `examples/culture-d4/components/04-lexicon.yml:224-271` (register block; `derivation_ops` `:269`, disclosure `:270`), `05-naming.yml:53,64,75,86,97,108,119,130` (NM-01..NM-08)
- `examples/culture-d4/packet.d4.yml:277-281` (`derivation_ops` block + note)
- `tools/gates/argot-derivation-gate.py:38,55,65-66,153-171,235-243,455-477,787-802` (declared-op discovery, syllabify, selftest rows)
- `tools/gates/register-law-gate.py` (run at HEAD, exit 0)
- `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv:2,:4` (packet digest pins), `tools/replay-frozen.py`
- `tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml`, `tools/gates/expected/register-law-gate/r30-post/examples/culture-d4/packet.d4.yml` (mirrored pinned packet bytes)
- `.scratch/r26-d-reg/final.py:4,26-58,65-75` (r26 census script, scratch; run at HEAD)

Commands run (all 2026-10-19, HEAD `139e3b6`): `git rev-parse HEAD`;
`sha256sum` on `design.md`/`rules.md`/`04-lexicon.yml`/`packet.d4.yml`;
`python3 -B .scratch/r26-d-reg/final.py` (→ `count: 3 of 70`, identity `67 of
70`); `git rev-parse --short 4f09c99^` → `1ad491a`; packet loader counts at
`1ad491a` (54 lexicon + 8 names) and HEAD (62 + 8); gate-syllabifier census over
the r26 set definition (→ `3 of 62`, identity `59 of 62`); `python3
tools/gates/argot-derivation-gate.py --selftest` (27/27, exit 0); argot gate on
`packet.d4.yml` (exit 0, violations=0); `register-law-gate.py` on
`packet.d4.yml` (exit 0, findings=0); `grep -c "op: head2"` / `"derivation:
head2"` on the packet (0/0); `TMPDIR=/tmp python3 -B tools/replay-frozen.py
reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` (REPLAY OK 4/4, exit 0);
probe `.scratch/c02/probe-nohead2.yml` (one line removed, `diff` → `278d277`)
with both gates exit 0; `date -u` → `2026-10-19T03:56:42Z`.
