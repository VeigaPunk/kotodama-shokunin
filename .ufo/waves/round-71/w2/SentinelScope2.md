# SentinelScope2 — round-71 wave-2: credentials, private hosts, misroot

This seat swept three axes: credential material, private-host URLs, and writes outside the lane (misroot).
Surface: the 37 wave-1 seat reports and the lane diff `b94a543..edd7895` (15 commits, including the post-wave commits
`ccadb59`, `c21213a`, `2166e45`, `cb77200`, `edd7895`), plus the fleet root, `/home/vgpnk/Projects/shokuknow`, and the sibling lanes for the misroot axis.
The seat was read-only apart from this report. No tools were installed (`gitleaks` 8.30.1 was already in `~/.local/bin`).

## Verdicts

| Axis | Verdict |
|---|---|
| Credential material | **PASS**: no matches |
| Private-host URLs | **PASS**: no matches |
| Misroot (writes outside the lane) | **FAIL**: one real misroot (now relocated); the lane's own records misstate it |

## Findings

### SS2-1 — MEDIUM — LOG.md round-71 misroot sweep line is false
- **Evidence:** `LOG.md:4275` (round-71 entry; `git blame` → `1d1b432`, 2026-10-25 08:38:53 -0300) states "**Misroot sweep.** Fleet status lists only driver state and orchestrator-owned scratch; no lane file misplaced."
  At that moment seven kotodama wave-1 fetch artifacts sat untracked in the fleet root (`s795.pdf s796.pdf s804.html s814.html s816.html s817.html s820.pdf`), observed by this seat in `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all`. They were relocated only at `ccadb59` (08:41:59, "misroot relocation (fetch artifacts)"). The line is unchanged at HEAD `edd7895`.
- **Exploit path / impact:** this is a fabricated-readiness record. A verifier who trusts LOG.md concludes the round had no misroot, while the fleet report `.ufo/reports/round-71/kotodama.md:81` says the opposite. The two durable records contradict each other.
- **Smallest remediation:** replace line 4275 with the actual result: seven fetch artifacts by wave-1 seat ScoutQuarantineFetch2 were found in the fleet root and relocated byte-exact at `ccadb59` to `.ufo/waves/round-71/assimilation/fetches/`.
- **Incidental, same entry:** `LOG.md:4267` still carries the unfilled placeholder ``records `<RECORDS>` ``.

### SS2-2 — LOW — the "recorded under lesson Mistakes" claim is unsupported, and the Mistakes table is malformed
- **Evidence:** the fleet report `.ufo/reports/round-71/kotodama.md:81` says the misroot was "recorded under lesson Mistakes". However, `rg -n -i -e 'misroot|relocat|fleet|s795|s820|fetch artifact' corpus/lessons/round-71.md` returns nothing at `cb77200`/`edd7895`.
  The `## Mistakes` table (lines 42–55) also has a bare `| attribution |` row (line 49). That row's evidence/fix cells (V70-2 "round-70 receipts stamped…") were displaced to an orphan line after the `declared-counter defect` row. Blank lines at 51 and 53 split the table, so the `guard-gap` and `declared-counter defect` rows render outside it.
- **Impact:** the misroot lesson never landed in the lane corpus, so the next round's lesson-mistake sweep cannot find it.
- **Smallest remediation:** add one `misroot` row (evidence: `ccadb59` plus the seven filenames; captured-by: orchestrator fleet-status sweep; fix: fetch outputs to `/tmp/<seat>/`). Rejoin the `attribution` row's cells, and delete the two blank lines inside the table.

### SS2-3 — LOW — wave-1 seat ScoutQuarantineFetch2 wrote outside the lane without disclosing it
- **Attribution:** all seven relocated files belong to the "round4" quarantine rows assigned to ScoutQuarantineFetch2 (rows 8–14).
  `rg -l "\bS(795|796|804|814|816|817|820)\b" .ufo/waves/round-71/w1/ScoutQuarantineFetch*.md` matches only `ScoutQuarantineFetch2.md`. The contents confirm it:
  - `s820.pdf` is Kałużyńska, *Onomastica* LXIX, the source the seat quotes for round4 S820.
  - `s816.html` and `s817.html` are the two China Writer 爱潜水的乌贼 articles the seat quotes.
  - `s804.html` is the コトバンク 苗字 page.
  - `s814.html` is 魏斌 單名與雙名.
  - `s795.pdf` and `s796.pdf` are Japanese onomastics reports.

  These are not kotodama's own S795–S820 registry rows, which are unrelated sources with the same ids.
- **Mechanism (inferred, not observed):** the files were written with relative output names in a seat whose working directory was the fleet root `/home/vgpnk/Projects/shokunin`. The dispatch context says "ALL repo writes and reads use absolute paths" but does not route fetch downloads to `/tmp`.
- **Disclosure gap:** `ScoutQuarantineFetch2.md` (11 lines) says only "fetched each cited URL live". It declares no file writes. By contrast, ExecDraftEntryShell, ScribeWaveSummary, ExecSOURCESRowTemplate, and MutGateQuotes each list their `/tmp` writes.
- **Wave-1 coverage gap:** wave-1 SentinelWriteScope audited only the dispatch instructions (it flagged reads of shokuknow and sibling lanes). It did not check the filesystem, so it missed this actual write.
- **Smallest remediation:** add one line to the dispatch context: "network fetch outputs go to `/tmp/<seat>/` only; every file written outside the report path MUST be listed in the report". Make the write-scope sentinel diff the fleet-root `git status` before and after the wave.

### SS2-4 — INFO — the relocation itself checks out, except byte-identity
- **Verified:**
  - The seven files exist at `.ufo/waves/round-71/assimilation/fetches/` (sha256 below).
  - The fleet root no longer holds them (`ls s7*.pdf s8*.html s8*.pdf` reports no such file).
  - Fleet git never tracked them: `git log --all -- s795.pdf …` is empty.
  - Fleet jj never tracked them: `jj --ignore-working-copy log -r 'files(glob:"s79*") | …'` is empty.
  - `origin/main` of the fleet repo does not contain them.
  - No copies exist in sibling lanes or shokuknow (`find … -newer <08:19 -0300> -name 's[0-9][0-9][0-9].{pdf,html}'` is empty).
- **Not verified:** the orchestrator's "cmp-verified byte-exact" claim. The fleet originals were deleted before this seat hashed them. [INFERENCE: plausible; unfalsifiable now.]
- sha256 values:
  - `s795.pdf`: `dae5bef1…`
  - `s796.pdf`: `40584e30…`
  - `s804.html`: `9ddde0ee…`
  - `s814.html`: `f14f7a5c…`
  - `s816.html`: `a3b6640c…`
  - `s817.html`: `344de345…`
  - `s820.pdf`: `5d1bfa5a…`

### SS2-5 — INFO — the relocation pushed third-party full texts to a public remote
- `gh repo view VeigaPunk/kotodama-shokunin --json visibility` returns `PUBLIC`. `git ls-remote origin refs/heads/main` returns `edd7895`, equal to HEAD.
- The relocated fetches (three PDFs of about 0.88 MB combined, plus four full HTML pages) are now redistributed publicly.
- No credentials are involved. The only identifier inside is a public Google Tag Manager container id, `GTM-TPNK2MG`, in `s804.html`.
- **Flag only:** a history rewrite is outside this seat's scope. For future rounds, keep fetches in `/tmp` and commit only URL, sha256, and Wayback pointer.

## Clean sweeps (evidence)

**Credential material: 0 true positives.**
- Regex sweep over the 7,320 added lines of `git diff b94a543..HEAD -U0` plus the then-untracked `measures-c.txt`. Patterns covered:
  - `op://`, bearer tokens, JWTs (`eyJ…`)
  - `gh[pousr]_`, `github_pat_`, `xox[abprs]-`, `AKIA`/`ASIA`, `glpat-`, `sk-`/`sk-ant-`, `AIza…`, `hf_`, `npm_`
  - PEM private keys and `ssh-* AAAA` keys
  - `key|secret|password|token|auth = <12+ chars>`, `Set-Cookie`/session ids, and `user:pass@` URLs
- Every hit was a false positive:
  - `sk-` matched inside `mask-dance-of-the-drums…` and `talchum-mask-dance…` URLs.
  - The 4 `op://` and session-cookie hits are the wave-1 sweep's own vocabulary (SentinelCredentialScan report and the wave-1 task prompt).
- `gitleaks git --log-opts="b94a543..HEAD"` reported 15 commits and "no leaks found".
- `gitleaks dir` on `.ufo/waves/round-71`, `reports/round-71/telemetry/measures-c.txt`, and `.ufo/waves/round-71/assimilation/fetches` reported "no leaks found" each time.
- The lane remote URL carries no embedded userinfo (`git remote -v | rg -c '://[^/]+@'` gives 0).

**Private-host URLs: 0.**
- Patterns covered: localhost/loopback, `0.0.0.0`, RFC1918 ranges, link-local, `::1`, CGNAT/Tailscale `100.64/10`, `.internal|.local|.lan|.corp|.home|.intranet|.priv|.localdomain|.test|.localhost|.ts.net`, and ngrok.
- The only hits were the wave-1 sweep's own vocabulary lines.
- The URL-host inventory of the diff found 35 distinct hosts, all public research or archive sites (top: `ich.unesco.org` 24, `doi.org` 12, `www.chinawriter.com.cn` 9, `web.archive.org` 8).
- Schemes: `https` 132, `http` 12, `op` 4 (vocabulary only). Every `http://` hit inspected (`rg -n 'op://|http://'`) is the public `ickl.org` homepage (S870 row, entry source line, and seat report).
- The fetch HTML contains no private-host URLs.

**Misroot, other surfaces: clean.**
- The lane diff touches only the lane's own paths: `.ufo/waves/round-71/**`, `LOG.md`, `SCORECARD.md`, `corpus/**`, `reports/round-70/telemetry/*`, and `reports/round-71/**`. It does not touch `.ufo/state`, `MANIFEST.json`, `.scratch`, or jj/git state.
- Fleet root files modified since 08:19 -0300 are other lanes' hyaku prompts/state/reports, or orchestrator-owned items:
  - `.ufo/reports/round-71/kotodama.md`, committed by the lane identity via fleet jj (`jj op log`: "round-71: kotodama report").
  - `MANIFEST.json`/`.jj` at 08:38:41, which has no `git diff`.

  No other kotodama file is in the fleet root (`git status --porcelain --untracked-files=all`).
- `.ufo/state/kotodama.report-baseline` (08:14:52) predates the declaration (08:19:00) and is driver state.
- In shokuknow, the only file modified in the window is `lanes/tabi/round8/.work/ratelimit-series.tsv`, which belongs to the tabi lane.
- Fleet `scripts/` and `templates/` have no modifications in the window. The `hyaku.env`/`lane-addendum.md` modifications predate the round.
- Sibling lanes: four files in the window mention kotodama (kake round-53 lesson and gate-draft, kotoba `considerthese`, mori `LOG.md`). Each is that lane's own prose about kotodama ids or the census, not a kotodama write.
- Wave-1 `/tmp` writes are within the sanctioned scratch root:
  - `/tmp/round71-claimC-entry-shell.md`, `/tmp/row-template-builder.py`
  - `/tmp/kotodama-round71-lesson-skeleton.md`, `/tmp/kotodama-package-id-map.json`
  - `/tmp/mut-gate-quotes/`, `/tmp/mut-settlement/`, `/tmp/mut-receipt-header-71/`
  - `/tmp/revcounter`, `/tmp/critbase71`, `/tmp/r71-base`
  - `/tmp/gate-battery-3jnzyq1q`, `/tmp/d71-nogit-XXXXXX`

## Commands (re-runnable from the lane root)
```
git diff --name-status b94a543..HEAD
git diff b94a543..HEAD -U0 | rg '^\+' | rg -v '^\+\+\+' > /tmp/ss2-added.txt
rg -n -i -e 'op://' -e 'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}' -e 'gh[pousr]_[A-Za-z0-9]{20,}' -e 'AKIA[0-9A-Z]{16}' -e 'sk-[A-Za-z0-9_-]{20,}' -e 'BEGIN [A-Z ]*PRIVATE KEY' -e '://[^/\s:@]+:[^/\s@]+@' /tmp/ss2-added.txt
rg -n -i -e 'localhost' -e '127\.0\.0\.' -e '\b10\.\d+\.\d+\.\d+' -e '\b192\.168\.' -e '\b172\.(1[6-9]|2\d|3[01])\.' -e '\.(internal|local|lan|corp|home|intranet|test|ts\.net)\b' /tmp/ss2-added.txt
rg -o -i '[a-z][a-z0-9+.-]*://[^\s)<>"`\x27\]]+' /tmp/ss2-added.txt | sed -E 's#^[^:]+://##; s#[/?:\#].*##' | sort | uniq -c | sort -rn
gitleaks git --log-opts="b94a543..HEAD" --redact --no-banner .
gitleaks dir --redact --no-banner .ufo/waves/round-71
git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all
touch -d '2026-10-25T11:19:00Z' /tmp/ss2-ref; /usr/bin/find /home/vgpnk/Projects/shokunin -maxdepth 4 -newer /tmp/ss2-ref -type f -not -path './*-shokunin/*' -not -path './.git/*'
git log --all --oneline -- s795.pdf s796.pdf s804.html s814.html s816.html s817.html s820.pdf   # in fleet root
git show --stat ccadb59
git blame -L 4275,4275 LOG.md
rg -n -A12 '^#+ *Mistakes' corpus/lessons/round-71.md
rg -l '\bS(795|796|804|814|816|817|820)\b' .ufo/waves/round-71/w1/ScoutQuarantineFetch*.md
gh repo view VeigaPunk/kotodama-shokunin --json visibility
```
