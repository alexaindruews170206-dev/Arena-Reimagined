#!/usr/bin/env python3
"""Pre-lint del pack v2: solo los pecados que el montador NO auto-corrigé."""
import sys, re
from collections import Counter
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
errs=[]
if "=====GLOS=====" not in s: errs.append("FALTA =====GLOS=====")
nodice=[l for l in s.split("\n") if l.strip().startswith("No dice")]
yn=[l for l in s.split("\n") if l.strip().startswith("Y no dice")]
if len(nodice)<5: errs.append(f"'No dice' x{len(nodice)} <5")
for l in yn: errs.append("Y-no-dice: "+l[:60])
in_fence=False
for l in s.split("\n"):
    if l.strip().startswith("```"): in_fence=not in_fence; continue
    if in_fence or l.startswith(">>>REV>>>"): continue
    if "★" in l and re.search(r"★\s*[\d.]",l) and not any(y in l for y in ("2023","2024","2025","2026")):
        errs.append("★sinFecha: "+l[:80])
c=Counter()
in_fence=False
for l in s.split("\n"):
    if l.strip().startswith("```"): in_fence=not in_fence; continue
    if in_fence or l.startswith(">>>REV>>>"): continue
    w=l.strip().strip("*").split()
    if len(w)>=2: c[(w[0],w[1])]+=1
for k,v in c.items():
    if v>=5 and k!=("No","dice"): errs.append(f"arranque x{v}: {k}")
print("\n".join(errs) if errs else "PACK LIMPIO ✓")
