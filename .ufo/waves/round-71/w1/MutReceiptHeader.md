# MutReceiptHeader — mutation test of the Ca receipt-header leg (V70-1)

Seat: `L1Kotodama71.MutReceiptHeader` (mutation-tester, leaf; no delegation).
Claim under test: **Ca** (frozen `reports/round-71/claims.json`), defect V70-1 —
six round-70 telemetry receipts gain the full QUALITY 17/19 header block (6 lines:
`# counter sha256`, `# stamped revision`, `# evaluated revision`, `# measured revision`,
`# tree`, `# worktree dirty`) with the original bytes preserved below a marker.

Scratch sandbox: `/tmp/mut-receipt-header-71/` (outside all protected trees; the
lane repo was read-only — no repo/lane/git/script/template bytes touched).

## 1. Fixtures (3 fake receipt variants)

The marker convention is taken from the lane's own re-stamp precedent
(`reports/round-64/telemetry/final-measures-ca.txt:13` → `--- original receipt bytes ---`);
the "original bytes" payload is the real round-70 body
(`reports/round-70/telemetry/measures-o.txt`, verbatim,
`# after-state receipt O — measured at lane 6cb51a4+landed edits …`).

| variant | file | header | marker | preserved original body |
|---|---|---|---|---|
| (a) good | `a-good.txt` | 6/6 lines | `--- original receipt bytes ---` | yes (7 lines) |
| (b) one missing line | `b-missing-line.txt` | 5/6 (`# tree:` dropped) | present | yes (7 lines) |
| (c) header, original deleted | `c-original-deleted.txt` | 6/6 lines | present | **no (0 lines)** |

Fixture sha256 (pristine, never written after creation):
- `a-good.txt` `062a986c009acbcb2a3609a13a3a2ca7a937d420af4bafff1485cd254d50b3a2`
- `b-missing-line.txt` `9b1e8b9f1f8c43aa04d17da99ba7208b03fadc1732a09a6ace0c324be4e97276`
- `c-original-deleted.txt` `144bb28e02a859fa2f7c1bb42bcb1be83298d826581593572a15c1ab47ffb494`

## 2. Leg detection spec (accepts only (a))

Python `leg.py` implements the RECEIPTS leg contract for the Ca counter:

- **L1** header complete: files match the six header prefixes (`^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)`), one per line.
- **L2** distinct: the six matches are six distinct prefixes (a duplicated line padded to six is rejected).
- **L3** marker: the line `--- original receipt bytes ---` is present.
- **L4** preserved: non-empty bytes exist below the marker (original bytes kept).

Accept iff L1∧L2∧L3∧L4. Exit 0 only then.

## 3. Exact outputs

### 3.1 Claim counting command (grep), per file

```
$ for f in a-good.txt b-missing-line.txt c-original-deleted.txt; do grep -cE '^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)' "$f"; done
a-good.txt: 6
b-missing-line.txt: 5
c-original-deleted.txt: 6
```

Aggregate form (file:count):

```
a-good.txt:6
b-missing-line.txt:5
c-original-deleted.txt:6
```

The six lines matched in (a):

```
1:# counter sha256 (self): 091074c5c054e1ed214204efee8ac25d12c7697414f2e8ea16aac9ec483b405e
2:# stamped revision: acc2d6142ef83f1750593af77daddf34a1e337
3:# evaluated revision: acc2d6142ef83f1750593af77daddf34a1e337
4:# measured revision (lane main): acc2d6142ef83f1750593af77daddf34a1e337
5:# tree: b154a91907a240e92bb5824f1232704b7ebd69f3
6:# worktree dirty (tracked): False
```

### 3.2 Leg detector verdicts

```
$ python3 -B leg.py a-good.txt b-missing-line.txt c-original-deleted.txt
a-good.txt
  L1 header_complete(6)=True  header_lines=6
  L2 header_distinct(6)=True
  L3 marker_present=True
  L4 original_preserved(nonempty)=True  preserved_lines=7
  VERDICT: ACCEPT
b-missing-line.txt
  L1 header_complete(6)=False  header_lines=5
  L2 header_distinct(6)=False
  L3 marker_present=True
  L4 original_preserved(nonempty)=True  preserved_lines=7
  VERDICT: REJECT
c-original-deleted.txt
  L1 header_complete(6)=True  header_lines=6
  L2 header_distinct(6)=True
  L3 marker_present=True
  L4 original_preserved(nonempty)=False  preserved_lines=0
  VERDICT: REJECT
leg exit=1
```

## 4. Mutation verdicts

| mutant | grep count | grep-only verdict | full leg verdict | disposition |
|---|---|---|---|---|
| (a) good | 6 | accept | **ACCEPT** | baseline |
| (b) missing `# tree:` | 5 | reject | **REJECT** | **killed** (header clause) |
| (c) original bytes deleted | 6 | accept | **REJECT** | **survives grep-only; killed by L4** |

Finding for the counter design: the claim's `counting_command` grep leg is
**necessary but not sufficient**. It counts 6 on (a) *and* on (c); "fewer on bad
ones" holds only for the missing-line class, not for the deleted-original class.
The RECEIPTS leg in `reports/round-71/accept-ca.py` MUST pair the 6-line grep with
the sub-marker clause (L3/L4) — the claim text itself requires "original bytes
preserved below a marker", so a grep-only leg would let mutant (c) pass and the
claim's kill rule would not fire. `leg.py` is the concrete spec for that paired leg
(exit 1 on any rejection).

## 5. Evidence hygiene

- Sandbox fixtures verified pristine (sha256 above); the detector runs are read-only; no bytes needed restoring.
- No tool installed/updated (python3 + grep preinstalled; no pacman/uv/npx transactions).
- Lane untouched: no repo write, no git/jj/index operation, no sibling lane access.
