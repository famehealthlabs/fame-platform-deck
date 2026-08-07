#!/usr/bin/env python3
"""Aggregate the F.A.M.E. stock-catalog CSV into the compact JSON embedded in index.html.

Usage: python3 tools/aggregate_catalog.py path/to/fame-stock-catalog.csv
Prints JSON to stdout. Paste between the CATALOG markers in index.html
(or rerun the injection step) whenever the Webflow export is refreshed.
"""
import csv, re, json, sys
from collections import Counter, defaultdict

FORMATS=[("Gummies",r"gumm"),("Capsules",r"capsule|caps\b|\bvcap"),("Tablets",r"tablet|chewable|lozenge"),
         ("Powders",r"powder|drink mix|stick pack|sachet|scoop"),("Liquids",r"liquid|drops\b|syrup|tincture|spray|shot"),
         ("Softgels",r"softgel|soft gel")]

def fmt(name):
    n=name.lower()
    for f,pat in FORMATS:
        if re.search(pat,n): return f
    return "Other"

def clean(name):
    for sep in ("–"," W/ "," w/ "," - "):
        name=name.split(sep)[0]
    return name.strip().rstrip("!,.")[:56]

def main(path):
    rows=list(csv.DictReader(open(path)))
    cats=Counter(); fmts=defaultdict(Counter); samples=defaultdict(list); diets=Counter()
    for r in rows:
        raw=(r.get("New Category") or "").strip()
        cs=[c.strip() for c in raw.split("|") if c.strip()] or ["General"]
        for c in cs:
            cats[c]+=1; fmts[c][fmt(r["Name"])]+=1
            if len(samples[c])<5: samples[c].append(clean(r["Name"]))
        for d in (r.get("Dietery Preferences") or "").split(","):
            d=d.strip()
            if d: diets[d]+=1
    ordered=[(c,n) for c,n in cats.most_common() if n>=4 and c!="General"]
    if cats.get("General"): ordered.append(("General",cats["General"]))
    out={"asOf":"August 2026","total":len(rows),
         "diets":[[k,v] for k,v in diets.most_common(5)],
         "cats":[{"n":c,"c":n,"f":dict(fmts[c]),"s":samples[c]} for c,n in ordered]}
    json.dump(out,sys.stdout,separators=(",",":"))

if __name__=="__main__": main(sys.argv[1])
