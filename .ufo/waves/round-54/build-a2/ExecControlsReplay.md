# ExecControlsReplay — round-54 criterion-11 controls replay and instrument attack

Seat: `KotodamaR54a2.ExecControlsReplay` (leaf executor). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated, branch `main`). Date 2026-10-22.

Scope: re-verify the inherited attempt-1 criterion-11 controls receipt, then attack the accept-c.py instrument on two of its legs (SET and RANGE) with near-misses the receipt does not already cover.

No lane file was written, edited or deleted by this seat. All code and fixtures live under `/fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/`. No pacman or other package transaction was run (no tool was needed: Python 3.14.8 and git 2.56.0 were already present).

---

## 1. Verdict: REPLAY MATCH

The committed receipt at `reports/round-54/telemetry/criterion11-controls.txt` (commit `7fa37fbb`, the round-54 declaration) is **byte-identical** to a fresh replay of the criterion-11 control builder run exactly as its own header prescribes.

### 1.1 How the receipt says it was run

The receipt's header block (lines 1–7) is the run instruction:

```
tree 260c68d58c5d3c2b9a6463ca5c667b7e0fff5987
sha256 ceadf2c68313bc82c4299e11f356aeb148a07531e7600f9453e60f9f0f466160  reports/round-54/accept-c.py
sha256 ce217cb7b24ed382ce8ed06ccaf14d593fadfeea454c1b4d755c04e5de2c9f37  reports/round-54/base-knowledge-files.txt
sha256 9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py
sha256 fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5  tools/check-source-access.py
sha256 d4223b4fbc6f98a066806c46b3fd97d6b77be2d81f7481770ec52a5687697a7d  reports/round-54/criterion11-controls.py
argv (run from each copy's root): python3 -B reports/round-54/accept-c.py
```

The builder's own docstring gives the invocation:
`python3 -B reports/round-54/criterion11-controls.py <lane-repo> <tree-ish> > reports/round-54/telemetry/criterion11-controls.txt`

### 1.2 The replay

Sandbox clone (nothing wrote git state in the lane itself):

```
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin \
    /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane
git -C .../lane checkout -q 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c
```

Command:

```
cd /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane
python3 -B reports/round-54/criterion11-controls.py \
    /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane \
    260c68d58c5d3c2b9a6463ca5c667b7e0fff5987 \
    > /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/replay-criterion11-controls.txt
```

Exit code **0**. Stderr empty. Output 126 lines.

Diff against the committed receipt:

```
diff -u committed-receipt.txt replay-criterion11-controls.txt   # exit 0, no output
sha256 committed-receipt.txt        7e006e22f800d8c12f0572bcc724534ebba7ca292f5c34bdcbeaf314bdca5aa8
sha256 replay-criterion11-controls.txt 7e006e22f800d8c12f0572bcc724534ebba7ca292f5c34bdcbeaf314bdca5aa8
```

The replay reproduces the receipt exactly, including the trailer `CONTROLS 13/13 as expected` and all thirteen control blocks (GREEN, RED-COUNT, RED-SET, RED-SET-EXT, RED-SWEEP, RED-FLOOR, RED-RANGE, RED-RANGE-NOROW, RED-RANGE-DUP, RED-RANGE-SPAN, RED-STATUS, RED-USEDBY, RED-ACCESS) with the same exit codes, the same failing-leg lists and the same leg detail lines.

Working copy vs committed: `diff` of the lane's `reports/round-54/telemetry/criterion11-controls.txt` against `git show HEAD:reports/round-54/telemetry/criterion11-controls.txt` at `7fa37fbb` is empty — the untracked working-tree copy is identical to the committed one, so the receipt was not edited after it was committed.

Second replay, at the declaration tree `7fa37fbb` instead of the base tree, is identical apart from the `tree` line on line 1 (`tail -n +2` diff is empty), which confirms the receipt is reproducible from either tree and that the base tree and the declaration tree carry the same five instruments.

### 1.3 Every sha256 the receipt lists, recomputed

Recomputed from the base tree `260c68d` via `git show 260c68d:<path> | sha256sum`, and independently from the checked-out working tree at `7fa37fbb`. Both agree with the receipt:

| instrument | receipt sha256 | recomputed (base tree) | recomputed (worktree) | match |
|---|---|---|---|---|
| `reports/round-54/accept-c.py` | `ceadf2c68313bc82c4299e11f356aeb148a07531e7600f9453e60f9f0f466160` | same | same | yes |
| `reports/round-54/base-knowledge-files.txt` | `ce217cb7b24ed382ce8ed06ccaf14d593fadfeea454c1b4d755c04e5de2c9f37` | same | same | yes |
| `reports/round-28/readme/sweep.py` | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` | same | same | yes |
| `tools/check-source-access.py` | `fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5` | same | same | yes |
| `reports/round-54/criterion11-controls.py` | `d4223b4fbc6f98a066806c46b3fd97d6b77be2d81f7481770ec52a5687697a7d` | same | same | yes |

All five match. The instruments are unchanged between the base tree and the declaration (`git diff --name-status 260c68d 7fa37fbb` touches only `reports/round-54/claims.json`, `reports/round-54/separability-manifest.json`, `reports/round-54/telemetry/criterion11-controls.txt`, `reports/round-54/telemetry/declaration-dry-run.txt`).

**Verdict: REPLAY MATCH.** The receipt is faithful, reproducible and its hashes are correct.

---

## 2. Instrument attack on accept-c.py — SET and RANGE

The receipt's own red controls cover SET via RED-COUNT (a second `.md` with an index row), RED-SET (a second `.md` added and a base file removed) and RED-SET-EXT (a second file that is not `.md`); and cover RANGE via RED-RANGE (S238 cited), RED-RANGE-NOROW (S259 cited, no row), RED-RANGE-DUP (a second queued S258 row) and RED-RANGE-SPAN (`(S257–S258)`).

I built the lane's own GREEN stand-in state (the `green()` function of `reports/round-54/criterion11-controls.py`, imported from the extracted tree so the fixtures are the lane's, not mine), applied one further near-miss per case, and ran the declared argv verbatim from each copy's root.

**Result: the receipt's controls are sound for the near-misses they cover, but two further near-misses pass `accept-c.py` where they should fail. Both are holes in the instrument, not in the receipt's own controls.**

### 2.1 RANGE hole — a range written with "through" hides a defective registry row

`accept-c.py:82` reads range notation with

```python
spans = re.findall(r"\bS\d{3}\s*(?:[–—-]|to)\s*S?\d{3}\b", text)
```

The alternation covers a dash or the word "to". Any other connector ("through", "and", "..", "/") is not a range to the leg, and the ids the range spans are then simply not cited — so `STATUS` and `USEDBY`, which only look at cited ids, never see them.

Near-miss (not covered by the receipt): the entry cites `(S252 through S254)` instead of citing S253 on its own; S253's registry row is `queued` and its used-by cell names `corpus/knowledge/culture-material/ritual-garments.md`; a clean S259 row is added so the entry still cites twenty distinct ids and `FLOOR` stays satisfied.

Result — **accept-c.py exits 0, all seven legs PASS, the defective S253 row goes unseen**:

```
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
```

Control that proves the defect is real and that only the range notation lets it through: the identical S253 row, cited outright rather than ranged, **fails**:

```
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=21 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS FAIL bad=['S253:queued']
  USEDBY FAIL bad=['S253']
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['STATUS', 'USEDBY']
```

### 2.2 SET hole — an extra file under corpus/knowledge reachable only through a directory symlink

`accept-c.py`'s SET leg enumerates the tree with `os.walk`, which by default does **not** descend into a directory symlink (`followlinks=False`), and `sweep.py`'s `disk_files` lists only the `.md` names sitting directly inside each of the six known part directories. A file under a symlinked directory is therefore inside `corpus/knowledge` on disk and outside both counts.

Near-miss (not covered by the receipt): `corpus/knowledge/culture-material/notes-link` is a symlink to a directory holding `masks-masquerade-notes.md`.

Result — **accept-c.py exits 0, all seven legs PASS**:

```
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
```

Measured on disk in that copy: `os.walk` counts **230** files, `os.walk(followlinks=True)` counts **231**, and `find corpus/knowledge/ -name masks-masquerade-notes.md` finds the file. The file is present; both counting legs miss it. Note the base tree contains no symlinks at all (`git ls-tree -r 260c68d` shows no mode-120000 entries), so this is a reachable-but-unusual shape; the claim's SET clause reads "every file under corpus/knowledge, of any extension", which the instrument does not deliver for this shape.

### 2.3 Full probe table

Every case below was run against the GREEN stand-in; the receipt covers none of them.

| case | what the near-miss does | accept-c exit | failing legs | caught? |
|---|---|---|---|---|
| GREEN | none (control) | 0 | `[]` | — |
| SET-NESTED | extra `.md` one directory deeper | 1 | `['SET']` | yes |
| SET-SYMLINKDIR | extra `.md` behind a directory symlink | **0** | `[]` | **no** |
| SET-SYMLINKFILE | extra `.md` that is a file symlink | 1 | `['SET', 'SWEEP']` | yes |
| RANGE-SPACEDASH | range written `(S257 – S258)` with spaces | 1 | `['RANGE']` | yes |
| RANGE-TO-WORD | range written `(S257 to S258)` | 1 | `['RANGE']` | yes |
| RANGE-THROUGH-WORD | range written `(S257 through S258)` | **0** | `[]` | **no** |
| RANGE-FOURDIGIT | `(S1000)` in place of `(S258)` | 1 | `['FLOOR']` | yes (via FLOOR) |
| RANGE-FOURDIGIT-HIDDEN | `(S1000)` beside twenty three-digit ids | **0** | `[]` | **no** |
| RANGE-DUP-INDENTED | second S258 row indented, original replaced | 1 | `['RANGE']` | yes |
| RANGE-DUP-INDENTED-KEEP | second S258 row indented, original kept | **0** | `[]` | **no** |
| RANGE-SHORTROW | cited SOURCES.md row with fewer than 13 cells | 1 | `['RANGE', 'ACCESS']` | yes |

Notes on the three additional misses beyond the two headline holes:

- **RANGE-FOURDIGIT-HIDDEN.** The citation scan at `accept-c.py:81` is `re.findall(r"\bS\d{3}\b", text)` — exactly three digits. A four-digit id is invisible to FLOOR's count and to RANGE's per-id checks alike. Cited on its own it fails FLOOR (19 distinct ids, one too few); cited beside twenty good ids it passes everything, and the id is never range-checked for having a registry row.
- **RANGE-DUP-INDENTED-KEEP.** The registry row counter at `accept-c.py:84` is `re.match(r"^\| S\d{3} ", line)` — anchored at the line start. A duplicate row indented by one space is not counted (measured: 2 physical `| S258 |` lines, 1 counted by accept-c.py, 1 parsed by `check-source-access.py`, which has the same anchor). GitHub-flavoured markdown renders a row indented by up to three spaces as a table row, so the page shows two S258 rows while the leg sees one. The receipt's RED-RANGE-DUP covers an unindented duplicate, which is caught; the indented form is not.
- **RANGE-SHORTROW** also trips ACCESS with exit 2 rather than 1: a row with the wrong cell count makes `check-source-access.py` raise (`parse_rows` requires exactly 11 cells), which is an input error rather than a finding. Worth knowing before a short row is read as a bypass finding.

### 2.4 Range-notation coverage, measured

`accept-c.py:82` pattern, applied to the strings a writer might actually type:

| written as | span detected | ids the citation scan sees |
|---|---|---|
| `S257–S258` | yes | S257, S258 |
| `S257—S258` | yes | S257, S258 |
| `S257-S258` | yes | S257, S258 |
| `S257 – S258` | yes | S257, S258 |
| `S257 to S258` | yes | S257, S258 |
| `S257 –S258` | yes | S257, S258 |
| `S257– S258` | yes | S257, S258 |
| `S257 through S258` | **no** | S257, S258 |
| `S257..S258` | **no** | S257, S258 |
| `S257 and S258` | **no** | S257, S258 |
| `S257/S258` | **no** | S257, S258 |
| `S257throughS258` | **no** | none |

Note the last row: written without spaces, `S257throughS258` yields **no** cited ids at all, so it also evades the FLOOR count.

---

## 3. Recommendation for the L1

The receipt itself is trustworthy — it replays byte-identically and its hashes are correct. The instrument has three reachable holes that the receipt's control set does not close. None of them is a reason to distrust the landed entry, because the landed entry's own text and registry were checked separately by the other seats; they are reasons to tighten `accept-c.py` before round 55:

1. `accept-c.py:82` — widen the range-notation pattern (or forbid the connectors outright) so a written range cannot hide ids from `STATUS` and `USEDBY`.
2. `accept-c.py:81` — the citation scan should reject or count a four-digit id rather than ignore it.
3. `accept-c.py` SET leg — walk `corpus/knowledge` with `followlinks=True`, or refuse a symlink anywhere under `corpus/knowledge`, so a file cannot sit inside the tree and outside the count.
4. `accept-c.py:84` — the registry row counter should tolerate a leading-space row (strip before matching), or the registry should forbid indentation so a duplicate row cannot hide from the counter while still rendering on the page.

Adding a red control for each hole would raise the receipt from 13/13 to 17/17.

---

## 4. Code and fixtures (all under the scratch dir)

Nothing was written to the lane, the fleet repo, or any git state.

| path | sha256 | purpose |
|---|---|---|
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane/` | — | sandbox clone of the lane at `7fa37fbb` |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/nearmiss.py` | `c644ce9853c5879780baf800989de574e231adae23ffbbcf114eee8bd42082a0` | the 12-case near-miss battery |
| `/fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/exploit.py` | `ac075eaa5dade6c5b9b3c6149632db34a9404c52a1588fdcf33cb758f7ba9c22` | the two headline holes plus the control |
| `.../committed-receipt.txt` | `7e006e22f800d8c12f0572bcc724534ebba7ca292f5c34bdcbeaf314bdca5aa8` | `git show 7fa37fbb:reports/round-54/telemetry/criterion11-controls.txt` |
| `.../replay-criterion11-controls.txt` | `7e006e22f800d8c12f0572bcc724534ebba7ca292f5c34bdcbeaf314bdca5aa8` | the replay |
| `.../replay-diff.txt` | empty | `diff -u` of the two above |
| `.../replay-at-HEAD.txt` | — | the second replay, at tree `7fa37fbb` |
| `.../final-nearmiss.txt` | — | the 12-case battery log |
| `.../final-exploit.txt` | — | the headline-hole log |
| `.../work/`, `.../work2/` | — | the extracted trees and per-case copies |

### 4.1 `nearmiss.py` (final source)

```python
#!/usr/bin/env python3
"""Round-54 criterion-11 near-miss attack on accept-c.py legs SET and RANGE.

Builds the GREEN stand-in state with the lane's own criterion11-controls.py
(green()), then applies one further near-miss per case that the committed
receipt (reports/round-54/telemetry/criterion11-controls.txt) does not already
cover, and runs the declared argv verbatim from each copy's root:

    python3 -B reports/round-54/accept-c.py

Read-only against the lane: `git archive <tree>` is extracted into a mktemp
directory under this seat's scratch dir; nothing writes git state anywhere.

Python 3 standard library only.
"""
import argparse
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

ACCEPT_ARGV = ["python3", "-B", "reports/round-54/accept-c.py"]
ENTRY = "corpus/knowledge/culture-material/masks-masquerade.md"
PART = "corpus/knowledge/culture-material"


def load_builder(base):
    """Import the lane's own control builder so the fixtures are the lane's."""
    path = os.path.join(base, "reports", "round-54", "criterion11-controls.py")
    spec = importlib.util.spec_from_file_location("c11controls", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tree_digest(root):
    """sha256 of every file under root, path-sorted, for a before/after diff."""
    out = {}
    for d, ds, fs in os.walk(root):
        for name in sorted(ds):
            p = os.path.join(d, name)
            if os.path.islink(p):
                out[os.path.relpath(p, root)] = "symlink-dir -> " + os.readlink(p)
        for f in sorted(fs):
            p = os.path.join(d, f)
            rel = os.path.relpath(p, root)
            if os.path.islink(p):
                out[rel] = "symlink -> " + os.readlink(p)
            else:
                with open(p, "rb") as fh:
                    out[rel] = hashlib.sha256(fh.read()).hexdigest()
    return out


def change_log(before, after):
    lines = []
    for k in sorted(set(before) | set(after)):
        if before.get(k) != after.get(k):
            b = before.get(k, "<absent>")
            a = after.get(k, "<absent>")
            if len(b) > 60:
                b = b[:57] + "..."
            if len(a) > 60:
                a = a[:57] + "..."
            lines.append(f"    {k}: {b} -> {a}")
    return lines


# ------------------------------------------------------------------ mutations

def set_nested(root):
    """SET near-miss #1: an extra .md one directory deeper under corpus/knowledge.

    The receipt's RED-SET-EXT puts a non-.md file at the same directory level.
    This one is a .md file nested one level deeper (a subdirectory the base tree
    does not have), which SET's os.walk sees and sweep.py's flat os.listdir
    does not.
    """
    d = os.path.join(root, PART, "masks-masquerade")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "notes.md"), "w", encoding="utf-8") as fh:
        fh.write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")


def set_symlink_dir(root):
    """SET near-miss #2: an extra .md reached only through a symlinked directory.

    os.walk does not descend into a symlinked directory (followlinks defaults
    to False), and sweep.py lists only the .md names directly inside each part
    directory, so neither instrument sees the file.
    """
    outside = os.path.join(root, "..", "linked-dir-" + os.path.basename(root))
    os.makedirs(outside, exist_ok=True)
    with open(os.path.join(outside, "masks-masquerade-notes.md"), "w", encoding="utf-8") as fh:
        fh.write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")
    link = os.path.join(root, PART, "notes-link")
    os.symlink(os.path.abspath(outside), link)


def range_spaced_dash(root):
    """RANGE near-miss #1: the range written with spaces around the dash.

    The receipt's RED-RANGE-SPAN writes (S257–S258) with no spaces. The same
    range written the way a typesetter would space it, (S257 – S258), is the
    nearest miss the instrument's range-notation pattern does not match.
    """
    p = os.path.join(root, ENTRY)
    text = open(p, encoding="utf-8").read()
    new = text.replace("(S258)", "(S257 – S258)", 1)
    assert new != text
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


def range_to_word(root):
    """RANGE near-miss #2: the range written with the word 'to'."""
    p = os.path.join(root, ENTRY)
    text = open(p, encoding="utf-8").read()
    new = text.replace("(S258)", "(S257 to S258)", 1)
    assert new != text
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


def range_through_word(root):
    """RANGE near-miss #4: the range written with the word 'through'.

    The leg's range-notation pattern alternates on a dash or the word 'to';
    'through' is neither, so a written range passes the leg.
    """
    p = os.path.join(root, ENTRY)
    text = open(p, encoding="utf-8").read()
    new = text.replace("(S258)", "(S257 through S258)", 1)
    assert new != text
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


def range_four_digit(root):
    """RANGE near-miss #5: a cited id of four digits, which no leg reads.

    The entry's citation scan matches exactly three digits, so a four-digit
    id is invisible to FLOOR and RANGE alike.
    """
    p = os.path.join(root, ENTRY)
    text = open(p, encoding="utf-8").read()
    new = text.replace("(S258)", "(S1000)", 1)
    assert new != text
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


def range_dup_indented(root):
    """RANGE near-miss #6: a second S258 row indented by one space.

    accept-c.py counts registry rows with a pattern anchored at the line
    start, so an indented duplicate row is a row the leg cannot see.
    """
    p = os.path.join(root, "corpus", "SOURCES.md")
    text = open(p, encoding="utf-8").read()
    m = re.search(r"^\| S258 .*$", text, re.M)
    assert m
    line = m.group(0)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text.replace(line, " " + line, 1))


def range_dup_indented_kept(root):
    """RANGE near-miss #7: a second S258 row indented by one space, the
    original left in place.

    The registry row-count is read with a pattern anchored at the line start,
    so an indented row is invisible to the duplicate-row check. GitHub-flavoured
    markdown renders a row indented by up to three spaces as a table row, so
    the registry on the page shows two S258 rows while the leg counts one.
    """
    p = os.path.join(root, "corpus", "SOURCES.md")
    text = open(p, encoding="utf-8").read()
    m = re.search(r"^\| S258 .*$", text, re.M)
    assert m
    line = m.group(0)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text.replace(line, line + "\n " + line, 1))


def range_four_digit_hidden(root):
    """RANGE near-miss #8: a four-digit id cited in addition to twenty
    three-digit ones.

    The citation scan matches exactly three digits, so the four-digit id is
    outside both FLOOR's count and RANGE's per-id checks.
    """
    p = os.path.join(root, ENTRY)
    text = open(p, encoding="utf-8").read()
    new = text.replace("(S239)", "(S239) (S1000)", 1)
    assert new != text
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


def set_symlink_file(root):
    """SET near-miss #9: an extra .md that is a symlink to a file elsewhere."""
    outside = os.path.join(root, "..", "linked-file-" + os.path.basename(root))
    with open(outside, "w", encoding="utf-8") as fh:
        fh.write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")
    os.symlink(os.path.abspath(outside),
               os.path.join(root, PART, "masks-masquerade-notes.md"))


def range_short_row(root):
    """RANGE near-miss #3: a cited row whose cell count is short of 13."""
    p = os.path.join(root, "corpus", "SOURCES.md")
    text = open(p, encoding="utf-8").read()
    m = re.search(r"^\| S258 .*$", text, re.M)
    assert m
    line = m.group(0)
    cells = line.split("|")
    assert len(cells) == 13, len(cells)
    short = "|".join(cells[:-2]) + "|"  # drop the recheck and used-by cells
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text.replace(line, short, 1))


CASES = [
    ("GREEN", None, "no near-miss: the receipt's own stand-in state"),
    ("SET-NESTED", set_nested,
     "extra .md one directory deeper under corpus/knowledge"),
    ("SET-SYMLINKDIR", set_symlink_dir,
     "extra .md reachable only through a symlinked directory"),
    ("RANGE-SPACEDASH", range_spaced_dash,
     "the S-range written with spaces around the dash"),
    ("RANGE-TO-WORD", range_to_word,
     "the S-range written with the word 'to'"),
    ("RANGE-THROUGH-WORD", range_through_word,
     "the S-range written with the word 'through'"),
    ("RANGE-FOURDIGIT", range_four_digit,
     "a four-digit id cited in place of S258"),
    ("RANGE-DUP-INDENTED", range_dup_indented,
     "a second S258 row indented by one space"),
    ("RANGE-SHORTROW", range_short_row,
     "a cited SOURCES.md row with fewer than 13 cells"),
    ("RANGE-DUP-INDENTED-KEEP", range_dup_indented_kept,
     "a second S258 row indented one space, the original left in place"),
    ("RANGE-FOURDIGIT-HIDDEN", range_four_digit_hidden,
     "a four-digit id cited beside twenty three-digit ones"),
    ("SET-SYMLINKFILE", set_symlink_file,
     "an extra .md that is a symlink to a file outside corpus/knowledge"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", required=True)
    ap.add_argument("--tree", required=True)
    ap.add_argument("--workdir", required=True)
    args = ap.parse_args()

    os.makedirs(args.workdir, exist_ok=True)
    rev = subprocess.run(["git", "-C", args.lane, "rev-parse", args.tree],
                         capture_output=True, text=True, check=True).stdout.strip()
    print(f"lane {args.lane}")
    print(f"tree {rev}")
    base = os.path.join(args.workdir, "base")
    os.makedirs(base, exist_ok=True)
    archive = subprocess.run(["git", "-C", args.lane, "archive", rev],
                              capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", base], input=archive, check=True)
    builder = load_builder(base)

    for name, fn, what in CASES:
        copy = os.path.join(args.workdir, name)
        shutil.rmtree(copy, ignore_errors=True)
        shutil.copytree(base, copy, symlinks=True)
        builder.green(copy)
        before = tree_digest(copy)
        if fn:
            fn(copy)
        after = tree_digest(copy)
        r = subprocess.run(ACCEPT_ARGV, cwd=copy, capture_output=True, text=True)
        legs = re.findall(r"^(\w+) (PASS|FAIL)", r.stdout, re.M)
        failing = [l for l, v in legs if v == "FAIL"]
        print(f"\n===== {name}: {what}")
        print(f"command: {ACCEPT_ARGV[0]} {ACCEPT_ARGV[1]} {ACCEPT_ARGV[2]}   (cwd = copy root)")
        print("tree change:")
        for line in change_log(before, after):
            print(line)
        print(f"exit {r.returncode}")
        for line in r.stdout.splitlines():
            print("  " + line)
        if r.stderr.strip():
            print("  stderr: " + r.stderr.strip())
        print(f"failing legs: {failing}   legs seen: {[l for l, _ in legs]}")
        if name == "GREEN":
            print("  (control: this copy must exit 0 with no failing leg)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### 4.2 `exploit.py` (final source)

```python
#!/usr/bin/env python3
"""Round-54 criterion-11 headline near-miss probes: one further near-miss per
leg of accept-c.py (SET and RANGE), each a miss the committed receipt
(reports/round-54/telemetry/criterion11-controls.txt) does not already cover.

Each case is built on the lane's own GREEN stand-in state (the green() function
of reports/round-54/criterion11-controls.py), then the near-miss is applied and
the declared argv is run verbatim from the copy's root:

    python3 -B reports/round-54/accept-c.py

Read-only against the lane: `git archive <tree>` is extracted into a mktemp
directory under this seat's scratch dir. Nothing writes git state anywhere.

Python 3 standard library only.
"""
import argparse
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

ACCEPT_ARGV = ["python3", "-B", "reports/round-54/accept-c.py"]
ENTRY = "corpus/knowledge/culture-material/masks-masquerade.md"
PART = "corpus/knowledge/culture-material"


def load_builder(base):
    path = os.path.join(base, "reports", "round-54", "criterion11-controls.py")
    spec = importlib.util.spec_from_file_location("c11controls", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tree_digest(root):
    out = {}
    for d, ds, fs in os.walk(root):
        for name in sorted(ds):
            p = os.path.join(d, name)
            if os.path.islink(p):
                out[os.path.relpath(p, root)] = "symlink-dir -> " + os.readlink(p)
        for f in sorted(fs):
            p = os.path.join(d, f)
            rel = os.path.relpath(p, root)
            if os.path.islink(p):
                out[rel] = "symlink -> " + os.readlink(p)
            else:
                with open(p, "rb") as fh:
                    out[rel] = hashlib.sha256(fh.read()).hexdigest()
    return out


def change_log(before, after):
    lines = []
    for k in sorted(set(before) | set(after)):
        if before.get(k) != after.get(k):
            b, a = before.get(k, "<absent>"), after.get(k, "<absent>")
            lines.append(f"    {k}: {b[:57]}{'...' if len(b) > 57 else ''} -> "
                         f"{a[:57]}{'...' if len(a) > 57 else ''}")
    return lines


# ------------------------------------------------------------------ mutations

def set_symlink_dir(root):
    """SET near-miss: an extra .md under corpus/knowledge, reachable only
    through a directory symlink.

    accept-c.py's SET leg enumerates corpus/knowledge with os.walk, which does
    not descend into a directory symlink, and sweep.py lists only the .md names
    sitting directly in each of the six known part directories. A file under a
    symlinked directory is therefore under corpus/knowledge on disk and outside
    both counts.
    """
    outside = os.path.join(root, "..", "linked-dir-" + os.path.basename(root))
    os.makedirs(outside, exist_ok=True)
    with open(os.path.join(outside, "masks-masquerade-notes.md"), "w", encoding="utf-8") as fh:
        fh.write("# notes\n\n- topic: stand-in notes\n- couples: stand-in\n")
    os.symlink(os.path.abspath(outside), os.path.join(root, PART, "notes-link"))


def range_through_hides_defect(root):
    """RANGE near-miss: the range written with the word 'through', hiding a
    defective registry row inside it.

    The leg's range-notation pattern alternates on a dash or the word 'to', so
    'through' is not a range it can see. The interior id of the range is then
    never among the entry's cited ids, and the STATUS and USEDBY legs only
    look at cited ids: a row that is queued and names another entry in its
    used-by cell stays invisible. A twenty-first row (S259) is added so the
    entry keeps twenty distinct cited ids and the FLOOR leg stays satisfied.
    """
    sources = os.path.join(root, "corpus", "SOURCES.md")
    text = open(sources, encoding="utf-8").read()

    # S253's row: queued, and its used-by names another entry.
    m = re.search(r"^\| S253 .*$", text, re.M)
    assert m
    line = m.group(0)
    cells = line.split("|")
    cells[8] = " queued "
    cells[11] = " corpus/knowledge/culture-material/ritual-garments.md "
    bad_row = "|".join(cells)
    text = text.replace(line, bad_row, 1)

    # a twentieth-plus-one clean row, so the entry can cite twenty ids
    extra = (f"| S259 | stand-in source S259 — https://example.invalid/S259 | paper | A | "
             f"stand-in scope | stand-in anchor | stand-in teaches | mined | 2026-10-22 | "
             f"2027-10-22 | {ENTRY} |\n")
    m238 = re.search(r"^\| S258 .*\n", text, re.M)
    assert m238
    text = text.replace(m238.group(0), m238.group(0) + extra, 1)
    with open(sources, "w", encoding="utf-8") as fh:
        fh.write(text)

    # the entry: S253's own citation is replaced by a range that hides it
    p = os.path.join(root, ENTRY)
    entry = open(p, encoding="utf-8").read()
    new = entry.replace("- stand-in sentence (S253).",
                        "- stand-in sentence (S252 through S254).", 1)
    assert new != entry
    new = new.replace("- stand-in sentence (S258).",
                       "- stand-in sentence (S258).\n- stand-in sentence (S259).", 1)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


def range_same_defect_cited(root):
    """Control for the RANGE near-miss: the same defective S253 row, but the
    entry cites S253 outright instead of hiding it inside a range.

    This must fail STATUS and USEDBY, which proves the defect is real and
    that only the range notation is what lets it through.
    """
    range_through_hides_defect(root)
    p = os.path.join(root, ENTRY)
    entry = open(p, encoding="utf-8").read()
    new = entry.replace("- stand-in sentence (S252 through S254).",
                        "- stand-in sentence (S253).", 1)
    assert new != entry
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(new)


CASES = [
    ("GREEN", None, "the receipt's own stand-in state, no near-miss"),
    ("SET-SYMLINKDIR-HOLE", set_symlink_dir,
     "an extra .md under corpus/knowledge reachable only through a directory symlink"),
    ("RANGE-THROUGH-HIDES-DEFECT", range_through_hides_defect,
     "a range written with 'through' hiding a queued row from the cited-id legs"),
    ("RANGE-CONTROL-DEFECT-CITED", range_same_defect_cited,
     "control: the same defective S253 row, cited outright instead of ranged"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", required=True)
    ap.add_argument("--tree", required=True)
    ap.add_argument("--workdir", required=True)
    args = ap.parse_args()

    os.makedirs(args.workdir, exist_ok=True)
    rev = subprocess.run(["git", "-C", args.lane, "rev-parse", args.tree],
                         capture_output=True, text=True, check=True).stdout.strip()
    print(f"lane {args.lane}")
    print(f"tree {rev}")
    base = os.path.join(args.workdir, "base")
    os.makedirs(base, exist_ok=True)
    archive = subprocess.run(["git", "-C", args.lane, "archive", rev],
                              capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", base], input=archive, check=True)
    builder = load_builder(base)

    for name, fn, what in CASES:
        copy = os.path.join(args.workdir, name)
        shutil.rmtree(copy, ignore_errors=True)
        shutil.copytree(base, copy, symlinks=True)
        builder.green(copy)
        before = tree_digest(copy)
        if fn:
            fn(copy)
        after = tree_digest(copy)
        r = subprocess.run(ACCEPT_ARGV, cwd=copy, capture_output=True, text=True)
        legs = re.findall(r"^(\w+) (PASS|FAIL)", r.stdout, re.M)
        failing = [l for l, v in legs if v == "FAIL"]
        print(f"\n===== {name}: {what}")
        print(f"command: {ACCEPT_ARGV[0]} {ACCEPT_ARGV[1]} {ACCEPT_ARGV[2]}   (cwd = copy root)")
        print("tree change:")
        for line in change_log(before, after):
            print(line)
        # show the resulting entry and the defective row
        ep = os.path.join(copy, ENTRY)
        if os.path.isfile(ep):
            print("entry citation lines:")
            for ln in open(ep, encoding="utf-8").read().splitlines():
                if "stand-in sentence" in ln:
                    print("  " + ln)
        sp = os.path.join(copy, "corpus", "SOURCES.md")
        if os.path.isfile(sp):
            for ln in open(sp, encoding="utf-8").read().splitlines():
                if re.match(r"^\| S25[239] ", ln):
                    print("registry: " + ln)
        print(f"exit {r.returncode}")
        for line in r.stdout.splitlines():
            print("  " + line)
        if r.stderr.strip():
            print("  stderr: " + r.stderr.strip())
        print(f"failing legs: {failing}   legs seen: {[l for l, _ in legs]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

---

## 5. Every run

All commands run from `/fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/` unless stated. Environment: Python 3.14.8, git 2.56.0.

### 5.1 Clone and checkout

```
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane
$ git -C .../lane checkout -q 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c
$ git -C .../lane log --oneline -5
7fa37fb round-54: declaration revised before dispatch — claim C statement, clause list and controls receipt (13/13), dry run
260c68d round-54: claim C instruments revised before dispatch (SET walks every file; RANGE fails duplicate rows and range notation; five more red controls) after the pre-dispatch critic findings
1ec84db round-54: declaration — claim C (masks and masquerade entry), clause list, criterion-11 controls receipt, dry run
4b2299b round-54: claim C instruments (accept-c.py, base knowledge list, criterion-11 control builder, start census)
d761ee8 round-54: prerequisite — round-53 closure routed fixes (gesture lines 68/133/150/199, speech-surrogates line 75 to S185, S145 retired, S225 access note, spot-check index row)
```
Exit 0. `git rev-parse HEAD` = `7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c`; `git rev-parse 260c68d58c5d3c2b9a6463ca5c667b7e0fff5987` resolves; `git cat-file -t` = commit.

### 5.2 Receipt identity

```
$ git -C .../lane show HEAD:reports/round-54/telemetry/criterion11-controls.txt > committed-receipt.txt
$ diff -u committed-receipt.txt /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-54/telemetry/criterion11-controls.txt
WORKINGCOPY==COMMITTED
```
Exit 0, no diff output. The lane working copy of the receipt equals the committed one.

### 5.3 Control-builder replay at the base tree

```
$ cd /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane
$ python3 -B reports/round-54/criterion11-controls.py \
    /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay/lane \
    260c68d58c5d3c2b9a6463ca5c667b7e0fff5987 \
    > ../replay-criterion11-controls.txt 2> ../replay-stderr.txt
BUILDER_EXIT=0
--- stderr ---
(empty)
```
126 lines out. Replay head:

```
tree 260c68d58c5d3c2b9a6463ca5c667b7e0fff5987
sha256 ceadf2c68313bc82c4299e11f356aeb148a07531e7600f9453e60f9f0f466160  reports/round-54/accept-c.py
sha256 ce217cb7b24ed382ce8ed06ccaf14d593fadfeea454c1b4d755c04e5de2c9f37  reports/round-54/base-knowledge-files.txt
sha256 9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py
sha256 fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5  tools/check-source-access.py
sha256 d4223b4fbc6f98a066806c46b3fd97d6b77be2d81f7481770ec52a5687697a7d  reports/round-54/criterion11-controls.py
argv (run from each copy's root): python3 -B reports/round-54/accept-c.py
```

```
$ diff -u committed-receipt.txt replay-criterion11-controls.txt > replay-diff.txt
DIFF_EXIT=0
--- diff (empty means identical) ---
(nothing)
$ sha256sum committed-receipt.txt replay-criterion11-controls.txt
7e006e22f800d8c12f0572bcc724534ebba7ca292f5c34bdcbeaf314bdca5aa8  committed-receipt.txt
7e006e22f800d8c12f0572bcc724534ebba7ca292f5c34bdcbeaf314bdca5aa8  replay-criterion11-controls.txt
```

**REPLAY MATCH.**

### 5.4 sha256 recomputation

```
$ cd .../lane && for f in reports/round-54/accept-c.py reports/round-54/base-knowledge-files.txt reports/round-28/readme/sweep.py tools/check-source-access.py reports/round-54/criterion11-controls.py; do git show 260c68d58c5d3c2b9a6463ca5c667b7e0fff5987:$f | sha256sum; done
sha256 ceadf2c68313bc82c4299e11f356aeb148a07531e7600f9453e60f9f0f466160  reports/round-54/accept-c.py
sha256 ce217cb7b24ed382ce8ed06ccaf14d593fadfeea454c1b4d755c04e5de2c9f37  reports/round-54/base-knowledge-files.txt
sha256 9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py
sha256 fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5  tools/check-source-access.py
sha256 d4223b4fbc6f98a066806c46b3fd97d6b77be2d81f7481770ec52a5687697a7d  reports/round-54/criterion11-controls.py
```
Exit 0. All five equal the receipt's lines.

### 5.5 Second replay at the declaration tree

```
$ cd .../lane && python3 -B reports/round-54/criterion11-controls.py .../lane 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c > ../replay-at-HEAD.txt 2>&1
EXIT=0
--- diff vs receipt, ignoring only the tree line ---
IDENTICAL_APART_FROM_TREE_LINE
```
Exit 0. Only line 1 (`tree …`) differs.

### 5.6 The 12-case near-miss battery

```
$ cd /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay
$ python3 -B nearmiss.py --lane .../lane --tree 260c68d58c5d3c2b9a6463ca5c667b7e0fff5987 --workdir .../work
NEARMISS_EXIT=0
```
Exit 0. Per-case output (each case runs `python3 -B reports/round-54/accept-c.py` from its own copy root):

```
===== GREEN: no near-miss: the receipt's own stand-in state
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== SET-NESTED: extra .md one directory deeper under corpus/knowledge
exit 1
  SET FAIL count=231 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md', 'corpus/knowledge/culture-material/masks-masquerade/notes.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['SET']

===== SET-SYMLINKDIR: extra .md reachable only through a symlinked directory
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== RANGE-SPACEDASH: the S-range written with spaces around the dash
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE FAIL bad=[] range_notation=['S257 – S258']
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['RANGE']

===== RANGE-TO-WORD: the S-range written with the word 'to'
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE FAIL bad=[] range_notation=['S257 to S258']
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['RANGE']

===== RANGE-THROUGH-WORD: the S-range written with the word 'through'
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== RANGE-FOURDIGIT: a four-digit id cited in place of S258
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR FAIL cited=19 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['FLOOR']

===== RANGE-DUP-INDENTED: a second S258 row indented by one space
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE FAIL bad=['S258'] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['RANGE']

===== RANGE-SHORTROW: a cited SOURCES.md row with fewer than 13 cells
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE FAIL bad=['S258'] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS FAIL exit=2 ?
failing legs: ['RANGE', 'ACCESS']

===== RANGE-DUP-INDENTED-KEEP: a second S258 row indented one space, the original left in place
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== RANGE-FOURDIGIT-HIDDEN: a four-digit id cited beside twenty three-digit ones
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== SET-SYMLINKFILE: an extra .md that is a symlink to a file outside corpus/knowledge
exit 1
  SET FAIL count=231 required=230 added=['corpus/knowledge/culture-material/masks-masquerade-notes.md', 'corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP FAIL exit=1 rows 230 files 231 missing_from_index 1 ['culture-material/masks-masquerade-notes.md']
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['SET', 'SWEEP']
```

### 5.7 The two headline holes plus the control

```
$ cd /fast/scratch/hyaku/kotodama-r54-a2/ExecControlsReplay
$ python3 -B exploit.py --lane .../lane --tree 260c68d58c5d3c2b9a6463ca5c667b7e0fff5987 --workdir .../work2
EXPLOIT_EXIT=0
```

```
===== GREEN: the receipt's own stand-in state, no near-miss
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== SET-SYMLINKDIR-HOLE: an extra .md under corpus/knowledge reachable only through a directory symlink
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== RANGE-THROUGH-HIDES-DEFECT: a range written with 'through' hiding a queued row from the cited-id legs
entry citation lines:
  - stand-in sentence (S252).
  - stand-in sentence (S252 through S254).
  - stand-in sentence (S255).
  - stand-in sentence (S259).
registry: | S253 | stand-in source S253 — https://example.invalid/S253 | paper | A | stand-in scope | stand-in anchor | stand-in teaches | queued | 2026-10-22 | 2027-10-22 | corpus/knowledge/culture-material/ritual-garments.md |
registry: | S259 | stand-in source S259 — https://example.invalid/S259 | paper | A | stand-in scope | stand-in anchor | stand-in teaches | mined | 2026-10-22 | 2027-10-22 | corpus/knowledge/culture-material/masks-masquerade.md |
exit 0
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=20 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS PASS bad=[]
  USEDBY PASS bad=[]
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: []

===== RANGE-CONTROL-DEFECT-CITED: control: the same defective S253 row, cited outright instead of ranged
registry: | S253 | stand-in source S253 — https://example.invalid/S253 | paper | A | stand-in scope | stand-in anchor | stand-in teaches | queued | 2026-10-22 | 2027-10-22 | corpus/knowledge/culture-material/ritual-garments.md |
exit 1
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
  FLOOR PASS cited=21 floor=20
  RANGE PASS bad=[] range_notation=[]
  STATUS FAIL bad=['S253:queued']
  USEDBY FAIL bad=['S253']
  ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
failing legs: ['STATUS', 'USEDBY']
```

### 5.8 On-disk confirmation of the two holes

```
$ cd .../work2/SET-SYMLINKDIR-HOLE
$ ls -la corpus/knowledge/culture-material/notes-link/
total 4
drwxr-xr-x 2 vgpnk vgpnk  39 Oct 22 15:46 .
drwxr-xr-x 8 vgpnk vgpnk 126 Oct 22 15:46 ..
-rw-r--r-- 1 vgpnk vgpnk  53 Oct 22 15:46 masks-masquerade-notes.md
$ python3 -c "..."
files os.walk counts: 230
files on disk under corpus/knowledge (following symlinks): 231
```

```
$ cd .../work/RANGE-DUP-INDENTED-KEEP
$ grep -n "S258 |" corpus/SOURCES.md
287:| S258 | stand-in source S258 — https://example.invalid/S258 | p
288: | S258 | stand-in source S258 — https://example.invalid/S258 |
$ python3 -c "..."
physical lines mentioning | S258 |: 2
rows accept-c counts for S258: 1
```

### 5.9 Range-notation pattern coverage

```
$ python3 -c "<the table in section 2.4>"
'S257–S258'                  span_detected=True  ids_cited=['S257', 'S258']
'S257—S258'                  span_detected=True  ids_cited=['S257', 'S258']
'S257-S258'                  span_detected=True  ids_cited=['S257', 'S258']
'S257 – S258'                span_detected=True  ids_cited=['S257', 'S258']
'S257 to S258'               span_detected=True  ids_cited=['S257', 'S258']
'S257 toS258'                span_detected=True  ids_cited=['S257']
'S257throughS258'            span_detected=False  ids_cited=[]
'S257 through S258'          span_detected=False  ids_cited=['S257', 'S258']
'S257..S258'                 span_detected=False  ids_cited=['S257', 'S258']
'S257 and S258'              span_detected=False  ids_cited=['S257', 'S258']
'S257/S258'                  span_detected=False  ids_cited=['S257', 'S258']
'S257 –S258'                 span_detected=True  ids_cited=['S257', 'S258']
'S257– S258'                 span_detected=True  ids_cited=['S257', 'S258']
'S239-S258'                  span_detected=True  ids_cited=['S239', 'S258']
'S257 to 258'                span_detected=True  ids_cited=['S257']
'(S257–S258)'                span_detected=True  ids_cited=['S257', 'S258']
```

### 5.10 The live lane at the time of writing

Read-only, run after the replay work:

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-54/accept-c.py
SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 []
FLOOR PASS cited=46 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LANE_ACCEPT_C_EXIT=0
```

The claim has landed in the lane in the meantime (jj change `qntnxuoztstr`, commit `6a658ca4fe92`, "round-54: claim C lands …"), and the gate passes on the landed tree with 46 distinct cited ids. The three instrument holes above are in the gate, not in the landed entry: the landed entry cites each id outright, so none of the hiding shapes applies to it.

---

## 6. Checks not run

- No build, lint, formatter or test suite was run: this seat's assignment is a replay and an instrument attack, and the parent owns the post-integration gate.
- `accept-c.py` was not modified; the holes are reported, not fixed, because the instrument belongs to the declaration commit and the L1 owns it.
- No external web source was opened; this seat had no source-reading assignment, so the report carries no citations.
- No pacman or package install was run; no tool was needed.

## 7. Risks and blockers

- **Blockers: none.** Every step of the assignment completed and every result is backed by a command, an output and an exit code in section 5.
- **Risk to the L1: the gate has three reachable holes.** They do not affect the landed entry (it cites ids outright and the landed tree passes all seven legs), but a future entry that writes a range with a word other than "to" or a dash could hide a defective registry row from the STATUS and USEDBY legs, and a symlinked directory under `corpus/knowledge` could hide a whole extra file. Four red controls would close them (see section 3).
- **Calibration note.** The receipt's own thirteen controls all still behave exactly as claimed, so the receipt is not overstated. Its coverage claim is only that it closes the thirteen shapes it names; it does not claim to close the shapes in section 2.3.
