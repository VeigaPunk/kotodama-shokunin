interface SeatVerdict {
  /** Seat id, e.g. "S1-counter-o". */
  seat: string;
  /** "agree" when the seat re-derived the committed verdict, "disagree" when it could not. */
  verdict: "agree" | "disagree";
  /** One to three sentences: what command was run and what it printed. */
  evidence: string;
}

const LANE = "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kotodama-shokunin";
const SCRATCH = "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/kotodama-r80/wave";
const COMMON = `You are a read-only verification seat for the kotodama lane round 80. The lane repo is at ${LANE} (branch main, tip 7439b14024673959cb19c8f3314e1fcc18bb7849). Do NOT edit, create or delete any file inside the lane repo; if you need scratch space use ${SCRATCH}/<your-seat-id>. Do not commit or push. Cite the exact command you ran and its output. If your check is impossible to run, say so plainly instead of guessing.`;

phase("Eight seats re-derive the round's verdicts in parallel");
const seats: { id: string; ask: string }[] = [
  { id: "S1-counter-o", ask: `Run: python -B reports/round-80/accept-o.py --selftest --work <your-scratch>/st (from the lane root). Confirm the last line is exactly "SELFTEST-O80: PASS" and the exit code is 0. Report the verdict line and exit code.` },
  { id: "S2-counter-d", ask: `Run: python -B reports/round-80/accept-d.py --selftest --work <your-scratch>/st (from the lane root). Confirm the last line is exactly "SELFTEST-D80: PASS" and the exit code is 0. Report the verdict line and exit code.` },
  { id: "S3-red-before", ask: `In your scratch dir run: git -C ${LANE} show a8aaeceb42fb4e01f37181697f88aaddb9629e01:tools/ledger-token-guard.py > old-guard.py, then run the OLD tool bytes on the oversize junk fixture: python -B old-guard.py --ledger ${LANE}/reports/round-80/fixtures/refusals/junk-oversize.json --repo ${LANE} --base a8aaeceb42fb4e01f37181697f88aaddb9629e01 --work <your-scratch>/w. The committed claim is that the UNHARDENED bytes ACCEPT this ledger (exit 0, "LEDGER-TOKEN-GUARD: PASS pairs=1") - reproduce that. Also confirm the hardened bytes (python -B ${LANE}/tools/ledger-token-guard.py with the same arguments) refuse it (exit 2). Report both exit codes and verdict lines.` },
  { id: "S4-lint", ask: `From the lane root run: python -B tools/check-cited-lines.py corpus/knowledge/culture-material/maritime-seafaring-lexicon.md (expect exit 0 and "0 finding(s)"), and: grep -cE '^\\|[[:space:]]*S[0-9]{3,}[[:space:]]*\\|' corpus/SOURCES.md (expect 824). Report both.` },
  { id: "S5-census", ask: `Run: bash "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/scripts/sources-census.sh" validate --root "C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin" kotodama. Confirm exit 0 (warnings W01/W04 allowed). Report the exit code and whether any E-line (error) appeared.` },
  { id: "S6-corrections", ask: `Read ${LANE}/reports/round-80/corrections/r80-annotations.md and verify its three bindings by running them: (1) git -C ${LANE} ls-tree 44f76d456c1b326a71ffdb381590af825cbf11be tools/ | find /c /v "" or wc -l (expect 27); (2) the word count of the S897 quote per the record's command adapted to your shell (expect 16); (3) git -C ${LANE} show HEAD:corpus/SOURCES.md | grep -c "python3 -B tools/ledger-token-guard.py" (expect 1). Report each observed value against the record.` },
  { id: "S7-sha-pin", ask: `Verify the pin chain: sha256 of ${LANE}/tools/ledger-token-guard.py must equal cca7db1748bc4e49406cd768a3339454b8a59d63086b06d87a10082be3107f9a; that sha must appear in ${LANE}/SKILL.md (the ledger-token-guard registry row) and in ${LANE}/SCORECARD.md (the capabilities row). Report the computed sha and whether both rows carry it.` },
  { id: "S8-entry-quality", ask: `Read ${LANE}/corpus/QUALITY.md (criteria 1-5) and ${LANE}/corpus/knowledge/culture-material/maritime-seafaring-lexicon.md. Judge only: does the entry carry provenance for its cited claims (criterion 1), calibration markers for its period sources (criterion 2), a couples line naming coupled files (criterion 3), decision tables a worldbuilder can act on (criterion 4), and the canon-hygiene markers (criterion 5)? Name any criterion the entry violates; if none, say so with the line you checked.` },
];

const verdicts: SeatVerdict[] = await Promise.all(
  seats.map((s) =>
    agent(`核验席 ${s.id}`, {
      system: "You verify committed evidence by running commands and reading files. You never edit the repository under verification. You report exactly what you observed, including failures.",
    }).ask<SeatVerdict>(`${COMMON}\n\nYour seat id is ${s.id}. Task: ${s.ask}\n\nAnswer as JSON with seat="${s.id}", verdict "agree" if the committed claim reproduces (or "disagree" if it does not or you could not run it), and evidence quoting the command(s) and key output.`),
  ),
);

phase("Collect the wave verdicts");
const disagreements = verdicts.filter((v) => v.verdict === "disagree");
log(`${verdicts.length - disagreements.length}/${verdicts.length} seats agree with the committed verdicts`);
return {
  conclusion: `${verdicts.length - disagreements.length} of 8 read-only verification seats re-derived the committed round-80 verdicts independently; ${disagreements.length} could not.`,
  verdicts,
  verified: verdicts.map((v) => `${v.seat}: ${v.verdict}`),
  notCovered: ["no seat re-ran the full graded acceptance runs end to end; the seats spot-check selftests, red-befores, lint, census, corrections and pins"],
};