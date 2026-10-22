import base64, os, re, subprocess, sys
WORDS = base64.b64decode("S29ybwpSb2JpbgpTaGlrYW1hcnUKTC1ib3QKTmFydXRvCk5hbWkKZHIgZWdnYm90ClZpb2xldApTYWdlClVzb3BwClNhaQpMdWZmeQpHcm9rIEJvdApFcndpbgpCdWxtYQpFcGluaW8K").decode().split("\n")
WORDS = [w for w in WORDS if w.strip()]
SECRETS = [r"gh[pousr]_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{20,}", r"AKIA[0-9A-Z]{16}",
  r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"xox[abposr]-[A-Za-z0-9-]{10,}", r"sk-[A-Za-z0-9]{32,}",
  r"AIza[0-9A-Za-z_-]{35}", r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"\s]{12,}['\"]"]
wre = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(w).replace(r"\ ", r"[\s_-]+") for w in WORDS) + r")(?![A-Za-z0-9])", re.I)
sres = [re.compile(p) for p in SECRETS]
files = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
bad = 0
for f in files:
    try: text = open(f, encoding="utf-8").read()
    except Exception: continue
    for i, line in enumerate(text.splitlines(), 1):
        if any(r.search(line) for r in sres): print(f"{f}:{i}: possible secret"); bad += 1
        m = wre.search(line)
        if m: print(f"{f}:{i}: disallowed name '{m.group(0)}'"); bad += 1
print(f"{bad} finding(s) in {len(files)} files"); sys.exit(1 if bad else 0)
