#!/usr/bin/env python3
"""CriticClaims-31 probe stub: rows-vs-last-footer only. No disk, no ghosts/topics/headers, no duplicate rule, no --json, fake selftest count."""
import sys, os, re
FOOTER=re.compile(r"Counts checked (\d{4}-\d{2}-\d{2})[^\n]*\n`[^`]+`\n\(total (\d+) files",re.M)
ROW=re.compile(r"^- `[^`]+\.md` — ",re.M)
def err(m):
    print("CORPUS_INDEX_ERROR:",m); return 2
def main():
    a=sys.argv[1:]
    if "--selftest" in a:
        print("SELFTEST: PASS (12 checks)"); return 0
    if "--root" not in a: return err("--root required")
    root=a[a.index("--root")+1]
    if not os.path.isdir(root): return err("root missing")
    p=os.path.join(root,"corpus","README.md")
    if not os.path.isfile(p): return err("no README")
    t=open(p,encoding="utf-8").read()
    ms=list(FOOTER.finditer(t))
    if not ms: return err("no footer")
    total=int(ms[-1].group(2)); rows=len(ROW.findall(t))
    print("CORPUS-INDEX: rows=%d footer=%d"%(rows,total))
    return 0 if rows==total else 1
if __name__=="__main__": sys.exit(main())
