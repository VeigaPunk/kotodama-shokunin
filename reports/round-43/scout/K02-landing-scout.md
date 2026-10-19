# K02 — landing scout: claim C (r42 C01 lithic spare)

- Seat: **K02**, role scout, claim **C** (`reports/round-43/targets.json:14`).
- Round 43, loop 1; baseline `7ceff59` (`reports/round-43/claims.json:7`).
- Observed at `2026-10-19T16:54:58Z`; lane HEAD `7ceff59a0216a8ea21ee43262d9fc72abf770cee`.
- Writes: this file only. No `corpus/**`, `tools/**`, `README`, or filed-round byte touched. No runner executed; no commit/push/install/network.
- Canon: NON-CANON. This seat measures bytes and reports collisions; it lands nothing.

## Verdict at a glance

**COLLISION — claim C cannot land as declared.** The r42 C01 spare is byte-intact, but its
declared target `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` is **already occupied
at HEAD** by the entry r42 landed from C04. The claim's `before` premise ("lithic slot named but
unbuilt", `reports/round-43/claims.json:40`) is contradicted by the live tree: the slot is built,
indexed, and tracked. Landing the spare at its own path would overwrite an existing entry; landing
it under a new slug would create a second owner of the same topic. Both are forbidden by the
claim's own threshold ("no existing entry overwritten", `claims.json:41`) and by the shared rule
("never overwrite an existing entry; report collisions, do not route around them",
`targets.json:9`). This seat reports; it does not choose a workaround.

## 1. Live partition at HEAD — the target is taken

Command: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **26**; `find corpus/knowledge -name '*.md' | wc -l` → **223**.

Full sorted listing observed (26 files):

```
animal-symbolism.md
binding-speech-complex.md
celestial-symbolism-calendars.md
color-symbolism.md
comparative-frameworks.md
cosmology-cosmography.md
creation-myths-taxonomy.md
death-afterlife-eschatology.md
direction-symbolism.md
divination-omen-systems.md
eschatology-world-end-systems.md
flood-traditions.md
hero-journey-variants.md
mineral-stone-symbolism.md
motif-index-usage.md
myth-folktale-genres.md
myth-ritual-theories.md
number-symbolism.md
pantheon-archetypes.md
plant-symbolism.md
purity-pollution-boundary-systems.md
ritual-liminality.md
sacred-kingship-mythic-charter.md
sacred-topography-pilgrimage.md
symbolism-synthesis-method.md
trickster.md
```

The exact target path sorts at position 14, between `hero-journey-variants.md` (13) and
`motif-index-usage.md` (15) — i.e. exactly where the spare was designed to go:

```
$ ls corpus/knowledge/myth-symbol/*.md | xargs -n1 basename | sort | grep -n 'hero-journey\|mineral-stone\|motif-index'
13:hero-journey-variants.md
14:mineral-stone-symbolism.md
15:motif-index-usage.md
```

The occupying file is tracked, clean at HEAD, and not a scratch artifact:

```
$ git ls-files corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
$ git status --porcelain corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
(empty — worktree clean vs index vs HEAD)
$ git rev-parse HEAD:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
f38f87e8750c08419c9e38aa646f9c6a05e79a6f
$ wc -l -c corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
192 61884
$ sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f
```

Its title confirms it is the same register the spare covers, not an adjacent topic:
`# Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and
the quarry-to-regalia chain` (`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1`).

## 2. The spare is byte-intact

File: `reports/round-42/cov/C01-mineral-spare.md`.

| measurement | value |
|---|---|
| whole file | 219 lines, 55,433 bytes, sha256 `2b9326e351de0e324bce3e71d45390c4a03e838138902ffcf23a971704ef6156` |
| git blob id (`git hash-object`) | `97149595a77a5dfd2539247d2b5f26a495285af8` |
| fence lines | `3: ```markdown` … `219: ``` ` — exactly 2 fence lines, no stray fence |
| fenced body (lines 4–218) | 215 lines, 55,101 bytes, sha256 `6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89` |
| body vs r42 pin | **MATCH** — `reports/round-42/cov/C06-delta-receipt.md:426` pins `C01-entry-1.md` block 0 at `6999a9123578bf8f…` |

The body was also diffed against the current `reports/round-42/cov/C01-entry-1.md` block 0
(fences at `:50`/`:267`): `diff` reports only `215a216 >` (one trailing blank line). No text
difference. So the spare is the same entry text that C01 filed, preserved as the named spare.

The spare itself carries no target-path field and no self-reference to a filename
(`grep 'mineral-stone-symbolism\|lithic-register\.md\|stone-gem'` → no output). Its header line
says the fenced bytes are "unmodified" (`C01-mineral-spare.md:1`); no front-matter adjustment or
alternate slug is sanctioned by the spare's own bytes.

## 3. Target filename under the myth-symbol naming convention

The partition convention is lowercase, hyphen-separated, topic-descriptive `.md`; all 26 live names
match `^[a-z0-9]+(-[a-z0-9]+)*\.md$` (zero exceptions).

The spare's own declared name is **`mineral-stone-symbolism.md`**:
- `reports/round-42/cov/C01-entry-1.md:3` — "Proposed landing path:
  `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`";
- `reports/round-42/cov/C01-entry-1.md:28` — "**Filename:** `mineral-stone-symbolism.md`";
- `reports/round-42/scout/K02-myth-gaps.md:212` — the R1 slot proposal that both C01 and C04 used.

Full target: **`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` — OCCUPIED.**

There is no convention-conformant alternate name for this same topic that does not duplicate the
owner; any invented slug (e.g. `lithic-register.md`) would be a new path with the same topic, which
is the duplicate-ownership case the r42 wave already ruled on (see §5).

## 4. Absence sweep re-run at the current 223 total — the slot is owned

The spare's `- gap filled:` line (`C01-mineral-spare.md:7`) records a sweep measured at lane HEAD
`ac47c78` (pre-r42-landing) showing 0 filename hits and 0 topic owners. Re-run now at `7ceff59`:

```
$ find corpus/knowledge -name '*.md' | grep -i 'mineral|stone|gem|lithic'
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md          # 1 hit — the owner

$ grep -rli '^- topic:.*mineral|^- topic:.*gem|^- topic:.*lapidary|^- topic:.*lithic|^- topic:.*precious' corpus/knowledge/
linguistics/sound-symbolism.md                     # false positive: "Dingemanse"
myth-symbol/death-afterlife-eschatology.md         # false positive: "judgement"
myth-symbol/mineral-stone-symbolism.md             # TRUE owner

$ grep -rli 'lapidary' corpus/knowledge/ | wc -l
4        # symbolism-synthesis-method.md:29 (the package mention), mineral-stone-symbolism.md,
         # sacred-topography-pilgrimage.md, civilizations/rome.md:33 (epigraphic sense)
$ grep -rli 'gemstone' corpus/knowledge/ | wc -l
3        # mineral-stone-symbolism.md, culture-material/ritual-garments.md, civilizations/siam-thai.md
```

Result: **the lithic slot is unambiguously owned.** The two non-lithic topic-line hits are the same
substring false positives the spare's gap line recorded (the regex matches `gem` inside
"Dingemanse" and "judgement"); they do not change the finding. The absence claim is now true only
of the pre-r42 tree.

## 5. Why the premise is false — the r42 record

The r42 validation is explicit (`reports/round-42/validation.json`, `claims.C.measurement.legs.C1.measurement.ruling`):

> "C01 and C04 authored the same lithic register mid-wave; C04 lands, C01 routes as the named
> spare (r36 timekeeping precedent); two existing entries (animal-symbolism, plant-symbolism) were
> momentarily overwritten by stale path proposals and restored byte-exact from HEAD at integration"

The same receipt records the claim-C failure: "myth-symbol 26 != 27, total 223 != 224 (three
entries landed, the fourth collided and is routed)". The commit that produced HEAD adds the file:

```
$ git show --name-status --format='' 7ceff59 -- corpus/
M  corpus/README.md
A  corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
A  corpus/knowledge/myth-symbol/purity-pollution-boundary-systems.md
A  corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md
```

`corpus/README.md:5-12` (revision 2.4) already documents the landing and the spare routing, and
its index row for `mineral-stone-symbolism.md` is at `corpus/README.md:219`. The r42 collision
verifier names the hazard directly: C01 and C04 "declare `corpus/knowledge/myth-symbol/
mineral-stone-symbolism.md` — the **lithic register** … the **same path**, so at most one file can
exist" (`reports/round-42/cov/C08-verify.md:426-454`, finding D3).

So the current 26/223 state is not "lithic slot unbuilt"; it is "lithic slot built by C04, spare
carried". The r43 claim's `before` sentence (`claims.json:40`) is a stale reading of the r42
outcome.

**Concurrent corroboration (read at handoff, not used as this seat's evidence).** Two other r43
seats independently reached the same verdict on their own measurements: C01-prepare reports
"BLOCKED — the spare's topic is already owned on disk" (`reports/round-43/cov/C01-prepare.md`),
and C06-collision reports "FAIL — the claim-C target filename is already occupied at HEAD, and the
claim's 'before' premise is stale" (`reports/round-43/cov/C06-collision.md`).

## 6. Consequences for claim C as declared

Claim C requires myth-symbol 26 → 27 and total 223 → 224 (`claims.json:39-41`). Three routes:

1. **Land at the declared path** — overwrites the tracked entry `mineral-stone-symbolism.md`.
   Forbidden: the claim's own threshold says "no existing entry overwritten" (`claims.json:41`);
   the shared rule says never overwrite (`targets.json:9`); r42 already had an overwrite incident
   with two restored entries and a collision ruling.
2. **Land under an invented slug** — reaches 27/224 arithmetically but creates two entries owning
   the one lapidary slot that `symbolism-synthesis-method.md:23,:29` names once. It also makes the
   spare's own `- gap filled:` line false in the landed copy ("the lithic register is absent from
   the partition"), and would require the README to list two lithic register rows. This is the
   duplicate-topic collision the r42 ruling routed the spare *away* from, not a re-scope.
3. **Replace the tracked entry with the spare** — an overwrite/withdrawal of existing corpus bytes,
   outside this seat's authority, contrary to the claim's no-overwrite threshold, and requiring its
   own provenance and rollback record. Reported only; this seat does not do it.

None of these is a silent adjustment this seat may make. The mechanically free facts are: the path
is taken, the topic is owned, and the only sanctioned name for the spare is the taken one.

## 7. Decision fork for the parent (no routing around)

- **(a) Re-scope claim C** to a genuinely unowned gap. This requires a new scoped claim and a new
  entry; none of the C-seat bytes prepared for the lithic spare (README row, audits, delta receipt)
  transfer without retargeting.
- **(b) Withdraw C this round** and record the spare as still-routed under its r42 disposition,
  with this file as the collision evidence. No corpus delta; claim C stays unfulfilled.
- **(c) An explicit integrator ruling** to supersede the tracked lithic entry, with a named owner,
  a byte-level before/after record, and a restore path. This seat flags it as an overwrite and does
  not recommend it; the claim's own threshold forbids it.

Whichever route is chosen, the spare should not be staged under `corpus/` by a seat; the shared
rules reserve corpus application to the integrator.

## 8. Command log (all run this seat, with `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`)

| command | output |
|---|---|
| `git rev-parse HEAD` | `7ceff59a0216a8ea21ee43262d9fc72abf770cee` |
| `git status --porcelain` | `?? reports/round-43/` only |
| `ls corpus/knowledge/myth-symbol/*.md \| wc -l` | `26` |
| `find corpus/knowledge -name '*.md' \| wc -l` | `223` |
| `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, `totals_ok True`, `footer_ok True`, exit 0 |
| `sha256sum reports/round-42/cov/C01-mineral-spare.md` | `2b9326e3…ef6156` |
| `sed -n '4,218p' …C01-mineral-spare.md \| sha256sum` | `6999a912…4dbd89` (matches r42 C06 pin) |
| `wc -l -c corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` | `192 61884` |
| `grep -n '^```' reports/round-42/cov/C01-mineral-spare.md` | `3:```markdown`, `219:``` ` |
| `git show --name-status --format='' 7ceff59 -- corpus/` | `A mineral-stone-symbolism.md` (+ two other r42 entries, README M) |

The filed sweep was executed read-only (`reports/round-28/readme/sweep.py`); no
`reports/round-*/run-validation.py` was executed anywhere.

## 9. Limits / to-verify

- This seat did **not** re-audit the spare's content against `corpus/QUALITY.md` or the entry
  contract; that is C01/C03/C04's pre-landing work, and it is moot while the path is occupied.
- This seat did **not** judge whether the r43 parent intended "replace C04's entry" rather than
  "add a second entry"; the claim text and the r42 ruling both say the spare is routed *away* from
  the landed path, so the overwrite reading is unsupported by the filed record. That intent
  question is the parent's to resolve.
- The claim's `before` statement is contradicted by HEAD; whether the r43 claim was authored
  against a pre-`7ceff59` snapshot cannot be recovered from the repo (the claims file itself
  declares baseline `7ceff59`), so it stays `to-verify` as a process question, not a bytes question.
- No corpus staging was performed and no filed byte was edited.
