#!/usr/bin/env python3
r"""A01 scan v2 — extension-less-aware couples resolver (read-only).
Adds the `extless` class the r39 policy's token rule ([...]+\.md) cannot see.
"""
import os, re, sys, glob, hashlib
def _find_root(start):
    d = os.path.abspath(start)
    while d != "/":
        if os.path.isdir(os.path.join(d, "corpus", "knowledge")):
            return d
        d = os.path.dirname(d)
    raise SystemExit("lane root not found")

ROOT = _find_root(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
TOKEN = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
EXT = re.compile(r"(?<![\w/\-.])((?:[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\-]*)(?![\w/\-.])")
BRACE = re.compile(r"\{([^{}]*)\}")
LANG_TOKENS = re.compile(r"(?i)\b(promot\w*|canon\w*|clearance|closure|verified)\b")
LANG_ALLOW = re.compile(r"(?i)(no |none |not |never |remains? the operator|operator-owned|routed|owed|absorbed|without |non-|negation|not a)")
LANG_FRAME = re.compile(r"(?i)(is|are|was|were|being) (promoted|canonized|cleared|granted)\w*|promotion (is )?(granted|complete|approved)|boxes? (all )?(pass|satisf)|checklist (all )?pass|canon standing (is )?(granted|given|conferred)|closure (is )?(granted|complete|decided)|verdict:\s*(pass|admitted|promoted|granted)|\[(x|v)\]\s|verified by (the )?(lane|seat|self)\b|unconditional")
PROVINCE_SCREEN = {
 "game-dev": re.compile(r"(?i)\b(game ?dev|game-?mechanics|playtest|level design)\b"),
 "chousa": re.compile(r"(?i)\b(chousa|source-research-method|citation-management protocol)\b"),
 "kake": re.compile(r"(?i)\b(kake|web ?publish\w*|prompt engineer\w*|prompt-skill)\b"),
 "sibling-repo": re.compile(r"(?i)(\.\./(lore|chousa|kake|kotoba|game-dev)[-a-z0-9]*)"),
 "canon-ownership": re.compile(r"(?i)\b(canon (is|becomes|belongs to us)|we (own|decide) (the )?(canon|world truth))\b"),
}
def sha(p):
    return hashlib.sha256(open(p,"rb").read()).hexdigest()
def field_block(lines, field):
    for i,l in enumerate(lines):
        if l.startswith(f"- {field}:"):
            b=[l]; j=i+1
            while j<len(lines) and lines[j].strip() and not lines[j].startswith("- "):
                b.append(lines[j]); j+=1
            return i+1, "\n".join(b), len(b)>1
    return None,"",False
def expand(s):
    m=BRACE.search(s)
    if not m: return [s]
    out=[]
    for o in m.group(1).split(","):
        for t in expand(s[m.end():]): out.append(s[:m.start()]+o+t)
    return out
INDEX={}
for p in glob.glob("corpus/knowledge/*/*.md"):
    INDEX.setdefault(os.path.basename(p)[:-3],[]).append(p)
    INDEX.setdefault(os.path.basename(p),[]).append(p)
PART={}
for p in glob.glob("corpus/knowledge/*/*.md"):
    PART.setdefault(os.path.basename(p)[:-3],set()).add(p.split("/")[2])
def cls(entry,tok):
    d=os.path.dirname(entry)
    for c in (os.path.join(d,tok),tok,os.path.join("corpus/knowledge",tok)):
        if os.path.isfile(c): return "direct",c
    if "/" in tok:
        part,tail=tok.split("/",1)
        if part in ("linguistics","myth-symbol","culture-material","synthesis","verification","civilizations"):
            c=f"corpus/knowledge/{part}/{tail}.md"
            if os.path.isfile(c): return "extless-direct",c
        return "unresolved",None
    h=INDEX.get(tok,[])
    if len(h)==1: return "extless-basename",h[0]
    if len(h)>1:
        return ("extless-basename",";".join(sorted(h)))
    return "unresolved",None
def scan(paths,label):
    print(f"## {label}")
    tot={k:0 for k in ("direct","extless-direct","extless-basename","unresolved","ambiguous")}
    dang=[];ext=[];amb=[];lang=[];prov=[];wrap=[];zero=[]
    for p in sorted(paths):
        lines=open(p,encoding="utf-8").read().splitlines()
        ln,val,w=field_block(lines,"couples")
        if ln is None: print("NO-COUPLES",p); continue
        if w: wrap.append((p,ln,len(val.splitlines())))
        toks=[]
        for t in TOKEN.findall(val):
            for e in expand(t):
                if e.strip(): toks.append(e.strip())
        for m in EXT.finditer(val):
            t=m.group(1)
            if t in INDEX or t.split("/")[-1] in INDEX: toks.append(t)
        seen=set(); toks=[t for t in toks if not (t in seen or seen.add(t))]
        # a `P/name` token and a bare `name` token can name the same file;
        # keep the first occurrence per resolved target so the class counts are honest
        dedup=[]; seen_t=set()
        for t in toks:
            k,target=cls(p,t)
            key=target if target else t
            if key in seen_t: continue
            seen_t.add(key); dedup.append(t)
        toks=dedup
        md_toks=[t for t in toks if t.endswith(".md")]
        if not md_toks: zero.append((p,ln))
        c={k:0 for k in tot}
        for t in toks:
            if "*" in t or "{" in t or t.startswith("-"): continue
            k,target=cls(p,t)
            if k=="extless-basename" and target and ";" in target: k="ambiguous"
            c[k]+=1; tot[k]+=1
            if k=="unresolved": dang.append((p,ln,t))
            if k.startswith("extless"): ext.append((p,t,target))
            if k=="ambiguous": amb.append((p,t,target))
        for i,l in enumerate(lines,1):
            for m in LANG_TOKENS.finditer(l):
                if not LANG_ALLOW.search(l) and LANG_FRAME.search(l): lang.append((p,i,m.group(0)))
            for n,rx in PROVINCE_SCREEN.items():
                if rx.search(l): prov.append((p,i,n,l.strip()[:110]))
        print(f"{p}\tline={ln}\trefs={len(toks)}\tmd={c['direct']}\textless={c['extless-direct']+c['extless-basename']}\tunresolved={c['unresolved']}\tambig={c['ambiguous']}\twrapped={w}\tsha8={sha(p)[:8]}")
    print(f"TOTALS {label}: files={len(paths)} direct={tot['direct']} extless={tot['extless-direct']+tot['extless-basename']} unresolved={tot['unresolved']} ambiguous={tot['ambiguous']}")
    print(f"ZERO-MD-TOKEN entries ({len(zero)}): {zero}")
    print(f"WRAPPED: {wrap}")
    print(f"DANGLING: {dang}")
    print(f"EXTENSION-LESS mappings ({len(ext)}): {ext}")
    print(f"AMBIGUOUS: {amb}")
    print(f"LANGUAGE-PREDICATE hits: {lang}")
    print(f"PROVINCE-SCREEN hits ({len(prov)}): {prov}")
    print()
if __name__=="__main__":
    a=sys.argv[1:]
    scan(a,"TARGET (argv)") if a else scan(glob.glob("corpus/knowledge/myth-symbol/*.md"),"MYTH-SYMBOL (control)")
