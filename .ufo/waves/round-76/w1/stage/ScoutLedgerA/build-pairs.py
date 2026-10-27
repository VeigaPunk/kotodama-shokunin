import json, subprocess, re, sys, shlex
B="98c486bdb4650ba5b8e651d332910e8ee60ad121"
L="/home/vgpnk/Projects/shokunin/kotodama-shokunin"
LS="corpus/lessons/round-75.md"
def grepo(pat, path): return ["git","grep","-o","-E",pat,B,"--",path]
pairs=[
 dict(id="L76-01",stated_at=LS+":4",
  stated_text="`git cat-file -e HEAD:reports/round-75/claims.json` → absent, so the round's",
  stated_parse="→ (absent),",
  observe_cmd=["git","grep","-c","-E","^",B,"--","reports/round-75/claims.json"],
  parse="count-presence", expected_after="present",
  why="Lesson lines 3-5 (claims line) say no freeze commit exists and that `git cat-file -e HEAD:reports/round-75/claims.json` is absent, so the round's files are untracked. At base 98c486b the file is a tracked blob (freeze 5d01674 is an ancestor: `git merge-base --is-ancestor 5d0167464309d8133991b30f7d7a7011a6a0fd14 98c486bd...` exits 0). The observation counts lines of the committed blob via `git grep -c -E '^'` and the counter's `count-presence` parse maps a positive count to `present`, a 0 to `absent`. The lesson's own `## Status at landing` (line 406-) supersedes the sentence in prose but the sentence at line 4 is unchanged and append-only, so the correction is an ANNOTATE row (ExecCountsSweep F1)."),
 dict(id="L76-02",stated_at=LS+":15",
  stated_text="the claims are `DRAFT`.",
  stated_parse="are `(DRAFT)`",
  observe_cmd=grepo('"status": "[A-Z]+',"reports/round-75/claims.json"),
  parse='"status": "([A-Z]+)', expected_after="FINAL",
  why="Lesson line 15 says the round-75 claims are `DRAFT`. The committed claims.json at base carries `\"status\": \"FINAL — wave-1 and wave-2 attacks applied; frozen by the commit that adds this file ...\"`; the first word is the token. ANNOTATE: the lesson is append-only (ExecCountsSweep F2)."),
 dict(id="L76-03",stated_at=LS+":312",
  stated_text="`git cat-file -e HEAD:reports/round-75/claims.json` still fails: nothing of the round is committed",
  stated_parse="still (fails):",
  observe_cmd=["git","cat-file","-t",B+":reports/round-75/claims.json"],
  parse="^(\\w+)$", expected_after="blob",
  why="R75-M1 (Mistakes table, line 312) asserts the `git cat-file -e` probe still fails. `git cat-file -e` exits 0 exactly when `git cat-file -t` prints an object type; at base the path resolves and prints `blob`, so the probe succeeds. Token vocabulary differs (stated outcome `fails`, observed object type `blob`) because an argv with no pipe cannot print an exit status. ANNOTATE (ExecCountsSweep F3)."),
 dict(id="L76-04",stated_at=LS+":332",
  stated_text="(`git cat-file -e HEAD:reports/round-75/accept-c.py` fails); the freeze must install both at the",
  stated_parse="accept-c\\.py` (fails)\\)",
  observe_cmd=["git","cat-file","-t",B+":reports/round-75/accept-c.py"],
  parse="^(\\w+)$", expected_after="blob",
  why="R74-M8 pointer (lines 330-333) says neither counter is committed and that the `git cat-file -e` probe on accept-c.py fails. At base the path is a tracked blob (accept-ca.py likewise: `git cat-file -t <base>:reports/round-75/accept-ca.py` prints blob). Same probe-outcome vocabulary as L76-03. ANNOTATE (ExecCountsSweep F4)."),
 dict(id="L76-05",stated_at=LS+":92",
  stated_text="`myth-symbol/narrative-structure-frameworks.md` (6862 B),",
  stated_parse="\\((\\d+) B\\)",
  observe_cmd=["git","ls-tree","-l",B,"--","corpus/knowledge/myth-symbol/narrative-structure-frameworks.md"],
  parse="blob [0-9a-f]+\\s+(\\d+)\\s", expected_after="30920",
  why="Lesson line 92 binds 6862 B to the adopted lane path `myth-symbol/narrative-structure-frameworks.md`; that is the staged copy's size in shokuknow/merge/kotodama. The committed lane file is 30920 B at base (`git ls-tree -l` size column; `wc -c` on the base worktree prints the same 30920). Lines 93-94 repeat the error for the amend-2026-10-23 (stated 5933 B, landed 24166 B) and amend-2026-10-23b (stated 2514 B, landed 23049 B) paths; one pair per finding. ANNOTATE (ExecCountsSweep F5; the lesson's own wave-3 section item 1 already lists the byte-size defect as routed, not corrected)."),
 dict(id="L76-06",stated_at=LS+":55",
  stated_text="maximum available — the round-74 R74-M6 allowance, used as written. The other six declare `excerpt`",
  stated_parse="declare `(excerpt)`",
  observe_cmd=grepo("^window-scope: [a-z-]+","reports/round-75/evidence/S891.txt"),
  parse="window-scope: ([a-z-]+)", expected_after="whole-document",
  why="Gate note 3 (lines 53-56) says three whole-document windows (S885, S886, S887) and `The other six declare excerpt`; S891 is one of those six. The committed evidence file reports/round-75/evidence/S891.txt declares `window-scope: whole-document` (chars=2169), so the census is four whole-document / five excerpt, and the statement is false of S891. The single-file observation keeps the token a short string with no pipe; the nine-file census (`git grep -h -E '^window-scope:' <base> -- 'reports/round-75/evidence/*.txt'` prints 4 whole-document, 5 excerpt lines) is in the report. The pointer at line 325 (`exercises it three times`) repeats the count. ANNOTATE (ExecCountsSweep F8; wave-3 section item 1 mentions `three whole-document windows (landed: four)` as routed, not corrected)."),
 dict(id="L76-07",stated_at=LS+":246",
  stated_text="S886, S887, S891, S892 → `amend-2026-10-23`; S888, S889, S890, S893 → base.",
  stated_parse="S891, S892 → `(amend-2026-10-23)`;",
  observe_cmd=grepo("^\\| S891 \\|.*","corpus/SOURCES.md"),
  parse="narrative-structure-frameworks\\.(amend-2026-10-23b?)\\.md", expected_after="amend-2026-10-23b",
  why="The `used-by` rewrite sentence (lines 244-246) maps S891 and S892 to `amend-2026-10-23`; the committed registry row for S891 (corpus/SOURCES.md) lists only `amend-2026-10-23b.md`, which is also what that entry's `source:` line (amend-2026-10-23b.md:4) cites. S892 likewise (row names amend-2026-10-23b.md; entry line 5), and S885 lists base + amend-2026-10-23 + amend-2026-10-23b where the sentence says base + amend-2026-10-23. The sentence copied the pre-move mapping of validate-receipt-draft.txt `USEDBY PASS`. The lesson's wave-3 item 1 does NOT list this defect, so it is unannotated at base. ANNOTATE (ExecCountsSweep F7)."),
 dict(id="L76-08",stated_at=LS+":47",
  stated_text="occur in the stored `--- window ---` text. S888's window (`chars=4097 before=10`) and S892's",
  stated_parse="S888's window \\(`chars=\\d+ before=(\\d+)`\\)",
  observe_cmd=grepo("^window: chars=[0-9]+ min=[0-9]+ pad=[0-9]+ before=[0-9]+","reports/round-75/evidence/S888.txt"),
  parse="before=(\\d+)", expected_after="3266",
  why="Gate note 2 (lines 46-52) says S888's stored window is `chars=4097 before=10` (document head, stopping before p. 3) and would fail the EVIDENCE leg. The committed evidence file at base reads `window: chars=4096 min=4096 pad=400 before=3266 after=809`: the window was re-cut around the anchor quote (the Gate quote occurs in it after NFKC+fold). The token is the window start offset (`before`), the number that places the window; the size token also differs (4097 stated, 4096 landed). S892 likewise: stated before=284, landed before=2020 (chars=4097). The lesson's wave-3 section item 1 notes `notes 2 and cells for S888/S892 say the anchor is absent from the stored window (landed windows contain it)` as routed, not corrected. ANNOTATE (ExecCountsSweep F9)."),
]
for p in pairs:
    p["disposition"]="ANNOTATE"
    argv=p["observe_cmd"]
    r=subprocess.run(argv,cwd=L,capture_output=True,text=True)
    out=r.stdout
    if p["parse"]=="count-presence":
        m=re.search(r":([0-9]+)$",out.strip()); tok="present" if m and int(m.group(1)) else "absent"
    else:
        m=re.search(p["parse"],out,re.M|re.S); tok=" ".join(m.group(1).split()) if m else None
    st=re.search(p["stated_parse"],p["stated_text"],re.M); stok=" ".join(st.group(1).split()) if st else None
    p["observed_at_base"]=tok
    p["red_at_base"]=(tok is not None and stok is not None and tok!=stok)
    p["_stated_token"]=stok; p["_rc"]=r.returncode; p["_out"]=out[:300]
    p["rederive"]=shlex.join(argv)
    print(p["id"],"rc=%d"%r.returncode,"stated=%r observed=%r expected=%r red=%s"%(stok,tok,p["expected_after"],p["red_at_base"]), "match_expected=",tok==p["expected_after"])
    print("   ",shlex.join(argv)); print("   out:",out.strip()[:200].replace("\n","\\n"))
json.dump(pairs,open("/fast/scratch/hyaku/kotodama-r76/ScoutLedgerA/pairs.full.json","w"),ensure_ascii=False,indent=1)
keys=["id","disposition","stated_at","stated_text","stated_parse","observe_cmd","parse","expected_after","observed_at_base","red_at_base","rederive","why"]
json.dump([{k:p[k] for k in keys} for p in pairs],open(L+"/.ufo/waves/round-76/w1/stage/ScoutLedgerA/pairs.json","w"),ensure_ascii=False,indent=1)
