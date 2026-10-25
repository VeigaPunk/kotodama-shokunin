# MutCa — mutation test of the Ca counter (round 71, wave 2)

Seat: `L1Kotodama71.MutCa` (mutation-tester, leaf). Lane HEAD `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6`.
Detector: `python3 -B reports/round-71/accept-ca.py --root <scratch>`; the counter's sha256 is
`3f3f63fc628aeac1fb9d076a77c6840161bbeacdde065294f01b13ea5139eb46`, the same digest stamped in
`reports/round-71/telemetry/measures-ca.txt`. The lane was not written: each probe ran in a
`.git`-less tar copy of the lane at `/tmp/mutca/scratch`. The harness is `/tmp/mutca/harness.py`
and its full output is in `/tmp/mutca/run.log`.

## Verdict

**PASS. All 3 assigned mutations are KILLED.** Each injected defect flips `ACCEPT-CA-71` from
PASS to FAIL (exit 0 → 1), and the counter names the expected leg. For each one, a counter
mutant that drops the corresponding clause turns the same defective bytes back to PASS. That
shows the clause is what kills the defect, not some other leg. Two neighbouring probes
**SURVIVE** (coverage findings, listed below). A separate defect in the claim's declared shell
`counting_command` is also recorded below.

## Baseline (must be green, or every probe is inconclusive)

| run | exit | output |
|---|---|---|
| lane, pristine counter | 0 | `ACCEPT-CA-71: PASS` (6/6 legs; V70-3 `words=25`; QUARANTINE `rows=21 unique-ids=21`) |
| scratch, pristine counter | 0 | `ACCEPT-CA-71: PASS` |
| scratch, counter mutants M1/M2/M3 | 0/0/0 | `ACCEPT-CA-71: PASS` (all mutants are equivalent on good bytes) |

## Counter mutants (built in /tmp only)

| id | clause removed | edit | sha256 |
|---|---|---|---|
| M1 | marker preservation | `has_all and marker_ok and original_ok,` → `has_all,` | `928806bc…ad32` |
| M2 | ≤25-word bound | `words <= 25` → `words <= 26` | `4a9d9010…b43a` |
| M3 | duplicate-id rejection | `len(rows) == 21 and len({ids}) == 21` → `len(rows) == 21` | `73aef5cd…b1014` |

## Probes

| probe | defect injected into the scratch bytes | pristine counter | clause mutant | verdict |
|---|---|---|---|---|
| D1 | `measures-ca.txt`: delete the `# original bytes preserved below` marker line (original bytes kept) | exit 1, `LEG FAIL V70-1`, `measures-ca.txt False` → **FAIL** | M1: exit 0 PASS | **KILLED** |
| D2 | `round-70.md` line 13, column 4: Gate quote padded from 25 to 26 words (`…ruling set, extra"`) | exit 1, `LEG FAIL V70-3`, `words=26 (want <=25)` → **FAIL** | M2: exit 0 PASS | **KILLED** |
| D3 | `quarantine-verdicts.md`: `\| S835 \|` rewritten to `\| S776 \|` (duplicate id; still 21 rows) | exit 1, `LEG FAIL QUARANTINE`, `rows=21 unique-ids=20` → **FAIL** | M3: exit 0 PASS | **KILLED** |
| D1b | `measures-ca.txt`: marker kept, original first line `# after-state receipt Ca …` replaced by `# forged line Ca` | exit 0, **PASS** | M1: PASS | **SURVIVED** |
| D3b | `quarantine-verdicts.md`: `\| S835 \|` rewritten to `\| S999 \|` (21 unique ids, but the wrong set) | exit 0, **PASS** | M3: PASS | **SURVIVED** |

D3 keeps the row count at 21 on purpose. If a duplicate row were appended instead (22 rows), the
row-count clause would kill it, and the uniqueness clause would never be tested on its own.

### Restoration evidence (sha256: pristine → mutated → restored; the restored bytes rerun PASS)

| file | pristine = restored = lane | mutated |
|---|---|---|
| `reports/round-70/telemetry/measures-ca.txt` | `28e43062ec1eab9720e1332db9968392b780a3fe2a6a82d4b08dfbd6ebbe665d` | D1 `0b59fd71…2fd9`, D1b `66e455b8…0d8` |
| `corpus/lessons/round-70.md` | `a2bd382f254b57be857d15ea1ac9cb425331e56828ef62fd1ead8302d2579607` | D2 `02446576…04d9` |
| `reports/round-71/telemetry/quarantine-verdicts.md` | `ad3f05f63104f4907d2938853050fdb43cf613923a1cc577f3970c83d5ffbf4e` | D3 `21484b1e…1713`, D3b `9e9d1dd3…c083` |

After each probe the pristine bytes were written back. Every restored hash matched, the pristine
counter returned to exit 0 PASS on the restored bytes, and the lane copy of every file kept its
pristine hash.

## Coverage findings (survivors; the frozen contract stays unchanged)

1. **The original-bytes check does not verify the original (D1b).** `accept-ca.py` defines
   `ORIGINAL_FIRST = "# after-state receipt"` (line 39) but never uses it. `original_ok` only
   asks whether the first line below the marker starts with `#` and is longer than 3 characters.
   So any comment line placed under the marker satisfies "original bytes preserved". The
   controls receipts start with `# pre-data control …`, not `# after-state receipt`, so simply
   switching to `ORIGINAL_FIRST` would wrongly fail three files. A real check would need the
   original first line per file, or the digest that the header already records ("digest of the
   preserved original bytes below the marker").
2. **The quarantine leg checks the number of ids, not the id set (D3b).** The docstring says
   "exactly the 21 slice ids", but the counter only checks 21 rows and 21 unique ids. Swapping
   in a foreign id (`S999`) passes. The expected id set (18 payload-absent + 3 unreachable,
   re-derived in `.ufo/waves/round-71/w1/RevQuarantineCrossCheck.md`) is not encoded in the
   counter.

## Declared shell `counting_command` defect (adjacent; not one of the assigned mutations)

The verdict-table leg of claim Ca's frozen `counting_command` in `reports/round-71/claims.json`
cannot reach its target:

```
awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}' reports/round-71/telemetry/quarantine-verdicts.md
→ 0   (target: 21)
```

With `-F'|'`, `$1` is the empty text before the leading pipe, and `$2`/`$3` keep their padding
spaces. The corrected field form (`$2 ~ /S[0-9]+/`, `$3` with spaces stripped) prints `21`. The
other shell legs print `6 6` (six files × 6 header lines), `1`, `25`, `1`, `1`. The landed
receipt `reports/round-71/telemetry/measures-ca.txt` records only the Python counter's output,
not the declared shell command's output. So the declared command was never run as written, or
its `0` went unreported. The shell per-file header grep also has no marker leg: D1 would pass
that shell leg (6 header lines still present). Only the Python counter catches D1.

## Exact commands

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-71/accept-ca.py --root .; echo EXIT=$?
python3 -B /tmp/mutca/harness.py        # copies the lane with tar --exclude=.git, builds M1-M3, runs D1/D1b/D2/D3/D3b, restores, checks hashes
```

Tooling: nothing installed or updated.
