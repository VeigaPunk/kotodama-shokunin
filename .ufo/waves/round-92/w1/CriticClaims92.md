# CriticClaims92 — attack on the frozen v3 entry mode (claim O, operability, milestone r92-v1)

Seat: CriticClaims92 (read-only attack, leaf member). Stage: `.ufo/waves/round-92/w1/stage/CriticClaims92/`
(`attacks.md` per-counterfeit record, `corrections.md` smallest correction per survivor, `attack_driver.py` re-runnable).

## Frozen bytes checked
- `tools/check-advance-evidence.py` sha256 = `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422` (matches O.tool_sha256; also the freeze-commit bytes `066b9728:tools/check-advance-evidence.py`).
- `reports/round-92/controls/make-counterfeits.py` sha256 = `86d3b8168635a1c61928a7732676b0c2a0ec9c92b7d7aaeca8bf86fdc547e05d` (imported read-only for its fixture builder; `-B`, no bytecode written).
- Grading: entry mode, set B (`--min-anchor-span 3 --min-gate-overlap 3`) plus the builder's floors. Each counterfeit is a mini-lane in scratch, deleted at seat end.
- No repo file was edited. No git mutation. No tool installed.

## Numbers (run 2026-11-05, `python3 -B attack_driver.py`, wall 3.9 s)
- 26 graded runs = 21 counterfeits + 5 controls.
- **Counterfeit survivors (rc 0): 16 of 21.**
- Counterfeits refused: 5 (4 on a named leg, 1 unnamed).
- Controls: G0 CLEAN rc 0; C1c refused GATE; A4b refused TOPIC; A5a CLEAN rc 0; A5c refused APPENDONLY. All as expected, so fixtures are not the cause of the survivors.
- Frozen selftest with `--work <scratch>/selftest`: rc 0, `SELFTEST PASS 89/89`, 89 lines beginning `  ok ` (re-run 2026-11-05 after the battery). Without `--work` it exits rc 2 (`--selftest needs --work`). The `attacks.md` header quotes the last line of stdout+stderr concatenated, which is an `ok` line, not the PASS line; that header is cosmetic and the counts above are the verified ones.

## Answers to the seven requested attacks

1. **Chrome quote as own sentence + forged manifest quote — SURVIVOR (A1, rc 0).** The entry carries "Freemium for Journals platform carries this note." and the gate quote is that chrome string. The manifest quote field is forged to "Freemium Journals platform prayer address petition", which shares 3 content words and passes the GATE bind. The same without the forge is refused on GATE (C1c). The manifest quote is the enabler.
2. **Fragment + trailing slash + uppercase host — refused on UNIQUENESS (A2a, rc 1).** But the adjacent variants survive: scheme swap `http://` (A2c), `www.` host (A2d), query suffix `?ref=` (A2e), path case `/Base-Prayer-Notes` (A2f). `norm_url` keeps the scheme, host prefix, query and path case. Uppercase scheme `HTTPS://` (A2b) is refused, but on CAPTURE and GATE, not UNIQUENESS: `URL_RE` is case-sensitive, so the shadow leg never sees that url.
3. **Capture byte-copies the ENTRY — exact copy refused on CAPTURE (A3a, rc 1); entry + one newline SURVIVES (A3b, rc 0).** The graded-bytes guard compares sha256 only, so one byte defeats it while the normalized text is identical.
4. **Three minimal headings each carrying one phrase — SURVIVOR (A4a, rc 0).** `## address`, `## petition`, `## efficacy` plus "table" in the table header gives span 4 and 4 phrase hits, with the rest of the entry genuinely topical. The control with all four phrases in one heading is refused on TOPIC (A4b). Headings of one word count as full surfaces.
5. **Prose sentence "S776 located in the archive" — both over-fire and under-fire, depending on the id.**
   - Over-fire: "S001 located in the archive, …" is refused on APPENDONLY (A5b, rc 1) because S001 has no base disposition. Honest prose is refused for an undisposed old id.
   - No over-fire on a base-disposed id: "S776 located …" with base S776 LOCATED is clean (A5a, rc 0). The relaxed anchor sees LOCATED, the base also says LOCATED, so no movement.
   - Under-fire: `**S001** LOCATED` (A5d), `| S001 | LOCATED |` (A5e) and `LOC\u200bATED` (A5f) all SURVIVE, because `DISPO_RE` needs the id at line start after a whitespace-terminated prefix and a plain verdict token. A visible LOCATED move for an old id is invisible to APPENDONLY.
6. **Invented classes:**
   - A6a: base row S776 teaches cell rewritten in the lands registry — SURVIVOR for the tool (rc 0). Entry mode does not compare lands base rows. The frozen counter does (`reports/round-92/measure92.py` lines 303–310: `removed` / `cells changed` over the base registry for claim C). I read those lines; I did not run the counter, so the claim-level refusal is by code reading.
   - A6b: base row S001 dropped from the lands registry — SURVIVOR for the tool (rc 0); the same counter lines cover it by reading.
   - A6c: S955 capture is an in-root symlink to `base-lesson.md`, a non-graded blob — SURVIVOR (rc 0). Residual of routed finding 6. Confinement is lexical; `open()` follows the link.
   - A6d: S955 capture is a symlink escaping the repository root — SURVIVOR (rc 0).
   - A6e: quote only inside `<meta content>` of raw HTML — SURVIVOR (rc 0). CAPTURE matches raw bytes, so markup counts as located prose.
   - A6f: gate line with a valid first quote and a chrome "body:" quote second — SURVIVOR (rc 0). Only the first quote span is ever checked.
   - A6g: manifest with `rows` as a list — refused with rc 1 and an unnamed traceback (AttributeError at grade_entry line 586). Only `Refused` is caught (line 1251); no named leg.

## Survivors (16), with the smallest correction
Full recipe, command, rc and verdict line per item: `stage/CriticClaims92/attacks.md`. Smallest correction, tradeoff and mutant target per item: `stage/CriticClaims92/corrections.md`.

| id | class | smallest correction (summary) |
|---|---|---|
| A1 | chrome quote, forged manifest quote | refuse gate quote verbatim in entry prose; require manifest quote to occur in capture and bind to teaching |
| A2c–f | scheme / www / query / path-case shadow | `norm_url`: map http→https, drop www., drop query, casefold path |
| A3b | capture = graded entry + 1 byte | compare `norm()` text of capture with graded files, not sha |
| A4a | span gaming, one-word headings | count a heading only if ≥3 words with a content word beyond the phrase |
| A5d–f | markdown / table / ZWSP disposition | strip emphasis, pipes, Cf characters before `DISPO_RE` |
| A6a–b | base row rewritten or dropped in lands | in `grade_entry`, compare every base row with lands cells (OTHERCELLS) |
| A6c–d | in-root / out-of-root symlink capture | refuse islink; realpath confined to capture dir; regular file only |
| A6e | quote only in HTML markup | strip script/style/head/tags before the quote-in-capture test |
| A6f | decoy first quote | check every quoted span on the gate line |

## Operability observations (not survivors)
- Uncaught exceptions exit rc 1 with a traceback and no named FAIL leg (A6g). Only `Refused` is caught.
- The UNIQUENESS shadow leg is blind to uppercase schemes (`URL_RE` is `https?`, case-sensitive); the refusal happens to come from other legs.
- The over-fire in A5b is conservative and by design (V10a class); under-fire in A5d–A5f is not.

## Scope and bounds of this measurement
- Measured: the 21 counterfeit runs and 5 controls above, with the frozen tool at its committed sha.
- Not measured: the frozen counter `measure92.py` was not run; its base-row coverage is stated from reading lines 303–310 only. The v3 mutation pass and the stub control were not re-run here. The seven routed round-91 fixtures were not re-run by this seat (the builder's after-receipt is the lead's).
- No claim of scholarly content; these are operability attacks on the grader.
- Tool installs: none. Writes: stage dir and this report only; scratch deleted at end.

## Verdict for O
The seven routed round-91 fixtures were not re-run by this seat, so this report makes no claim that they still refuse. Of the 21 new counterfeits, 16 pass rc 0 under set B, including the requested recipes A1 and A4a and the requested near-copy A3b. The grader therefore does not close the classes above. For a claim whose kill rule is "any FAIL leg kills O", these are attacks on the grader itself, not on claim C. Each survivor has a correction in `corrections.md`; none is applied here.
