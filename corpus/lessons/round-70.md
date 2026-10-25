# Round 70 (2026-10-25, hyaku run 6, L1 kotodama-r70) — repair-first after round 69 closure rejection

The round-69 closure rejected the round (honest stop: operability and depth improved, but the
Ca2 kill rule fired; verdicts known). Its verifier spot-check routed defects D1..D10 to this
round; the lane also stood self-routed items (R69-M8..M12). This round repairs all of them and
claims operability (gate-registry + selftest repair), calibration (records/dispositions) and
depth (settlement-checker hardening, sourced).

## Gate

| source | access date | quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|
| S860 — `tools/check-supersession-settlement.py` (lane own-work) | 2026-10-25 | "A row whose `used-by` names a path that does not contain the row's own id is `STALE-USED-BY` (reported; gated only for the frozen ruling set, not globally...)" | the hardened checker now reports malformed rows (`MALFORMED-ROW`) and counts missing used-by files uniquely; `--selftest` proves it (SELFTEST 10/10, incl. cases `missing-unique-file`, `malformed-rows-report`, `malformed-target-no-crash`); ran `python3 -B tools/check-supersession-settlement.py --selftest` at `6cb51a4` | admitted |

## Mistakes

| class | evidence | captured-by | fix | payoff | state |
|---|---|---|---|---|---|
| record accuracy | SCORECARD.md:1331 filed round-69 calibration `improved` while the attempt-2 residual block (:1360) files `FAILED AS DECLARED` — the Ca2 kill rule fires on the 4 live pairs, and the declared after-state required rewriting frozen round-68 bytes (R69-M7) | round-69 verifier spot-check (D4) | appended correction row in the round-70 SCORECARD corrections (D4): round-69 calibration is unprovable / the claim failed as declared; the `improved` row is superseded | the scorecard's calibration row no longer contradicts its own residual verdict | new |
| record wording | the round-69 report said "claims.json is unchanged since 6a98d7d"; the frozen predicate/kill-rule/target/counting-command fields are byte-identical at 6a98d7d, 52b92a6, ef75509, but wave metadata and `counter_revisions` were appended at `52b92a6` | round-69 verifier spot-check (D3) | the round-70 report and the dispositions table use the corrected wording ("frozen fields unchanged; wave metadata and counter_revisions appended at 52b92a6") | claim-state sentences now mean exactly what the bytes show | new |
| pointer accuracy | `.ufo/waves/round-69/assimilation/guard-proof/note.txt` cited R69-M10 for the S859 lane-package collision; the lane lesson assigns that mistake R69-M13 | round-69 verifier spot-check (D9) | pointer fixed in place (note.txt line 4) and the collision re-proven at round 70 (`.ufo/waves/round-70/assimilation/collisions` = S859) | readers of the guard proof land on the right mistake | new |
| drafting | the first generated gate-registry block named rows `accept-accept-X-N` (double prefix) | L1 self-review before landing | regenerated naming `{cmd}-{round}` (e.g. `accept-c-53`); the landed table has exactly 36 rows matching the 36 enumerated counter files | no malformed registry names entered the table | kept |

## Corrections (round 69)

Per-defect dispositions with landings: `reports/round-70/corrections-r69.md` (D1..D10).
The SCORECARD round-70 corrections section appends the D2/D3/D4/D9/D10 rows; the D5 sentence is
reworded in place and disclosed there.

## Quarantine

Item 10 stays CLOSED: adoption is CLOSED, no shokuknow bytes are adopted, appended or renumbered.
The id-collision guard is re-proven at the 783-row registry: the lane's S859 row still collides
with the package's first staged id (collisions = S859), so the quarantine slice verdicts from
rounds 68/69 stand unchanged.

## Frontier-step

Round-70 claims: O (operability, counter-registry + accept-d selftest repair), Ca (calibration,
records/dispositions), D (depth, settlement-checker hardening — sourced via S860). All three
verify with committed receipts; no frozen round-69 byte was rewritten to reach any after-state.
