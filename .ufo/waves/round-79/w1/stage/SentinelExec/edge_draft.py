import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("og", "/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-79/w1/stage/SentinelExec/observe_grammar.py")
og = importlib.util.module_from_spec(spec); spec.loader.exec_module(og)
R = "7d8755dabe82d184c5de2f6835ee5f2db50a8d18"
EDGE = [
 ("E1 upper-case hex rev", ["git","cat-file","-p",R.upper()+":a.txt"]),
 ("E2 extra trailing arg on cat-file", ["git","cat-file","-p",R+":a.txt","extra"]),
 ("E3 grep with trailing --", ["git","grep","-n","needle",R,"--","a.txt","--"]),
 ("E4 grep without -- separator", ["git","grep","-n","needle",R,"a.txt"]),
 ("E5 empty path after colon", ["git","cat-file","-p",R+":"]),
 ("E6 newline in path", ["git","cat-file","-p",R+":a.txt\n"]),
 ("E7 rev with ^{tree} as cat-file object", ["git","cat-file","-p",R+"^{tree}:a.txt"]),
 ("E8 ls-tree path starting dash", ["git","ls-tree","-r","--name-only",R,"--","-rf"]),
 ("E9 rev-parse wrong flag set", ["git","rev-parse","--quiet","--verify","-q",R+"^{tree}"]),
 ("E10 grep repeated flag", ["git","grep","-n","-n","needle",R,"--","a.txt"]),
 ("E11 argv not a list", "git cat-file -p x"),
 ("E12 non-string element", ["git","cat-file",None]),
 ("E13 single element argv", ["git"]),
 ("E14 grep -- placed before flags", ["git","grep","--","-n","needle",R,"--","a.txt"]),
 ("E15 ls-tree rev is branch", ["git","ls-tree","-r","--name-only","refs/heads/main","--","a.txt"]),
]
for name, argv in EDGE:
    try:
        print(name, "->", og.check_argv(argv))
    except Exception as e:
        print(name, "-> EXCEPTION", type(e).__name__, e)
