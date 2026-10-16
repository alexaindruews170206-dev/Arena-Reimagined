#!/usr/bin/env python3
"""Pre-lint del pack: caza los 5 pecados ANTES de hornear."""
import sys, re
p=sys.argv[1]
s=open(p,encoding='utf-8').read()
errs=[]
if "=====GLOS=====" not in s: errs.append("FALTA =====GLOS=====")
nodice=[l for l in s.split("\n") if l.strip().startswith("No dice")]
y_nodice=[l for l in s.split("\n") if l.strip().startswith("Y no dice")]
if len(nodice)<5: errs.append(f"No dice x{len(nodice)} <5")
if y_nodice: errs.append(f"Y no dice x{len(y_nodice)} → convertir a 'No dice'")
stars=[l for l in s.split("\n") if "★" in l and re.search(r"★\s*[\d.]",l) and not any(y in l for y in ("2023","2024","2025","2026"))]
for l in stars: errs.append("★sinFecha: "+l[:80])
from collections import Counter
c=Counter()
for l in s.split("\n"):
    w=l.strip().strip("*").split()
    if len(w)>=2: c[(w[0],w[1])]+=1
for k,v in c.items():
    if v>=5 and k!=("No","dice"): errs.append(f"arranque x{v}: {k}")
longs=[(len(b),b[:60]) for b in re.split(r"\n\n+",s) if len(b)>430]
for n,b in longs: errs.append(f"bloque {n}c >430: {b}...")
print("\n".join(errs) if errs else "PACK LIMPIO ✓")
