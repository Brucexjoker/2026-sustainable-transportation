"""Data consistency tests. Run: python3 tests/check_data.py"""
import json, os, re, sys, math
p = os.path.join(os.path.dirname(__file__), "..", "app", "data", "data.js")
raw = open(p, encoding="utf-8").read()
D = json.loads(raw[len("window.DATA = "):].rstrip().rstrip(";"))
fails = []
def check(c, m):
    if not c: fails.append(m)

check(len(D["weeks"]) == 12, "need 12 weeks")
for w in D["weeks"]:
    for k in ("overview","objectives","notes","definitions","concepts","formulas","example","applications","cases","misconceptions","revision","refs"):
        check(w.get(k), "week %s missing %s" % (w["id"], k))
allq = D["questions"] + D["numericals"]
ids = [q["id"] for q in allq]
check(len(ids) == len(set(ids)), "duplicate IDs")
texts = [(q["text"].strip().lower(), tuple(q.get("options") or [])) for q in allq]
check(len(texts) == len(set(texts)), "duplicate question text")
for q in D["questions"]:
    n = len(q["options"])
    check(n >= 2, q["id"] + " few options")
    check(q["answer"] and all(0 <= a < n for a in q["answer"]), q["id"] + " bad answer index")
    check(len(set(q["options"])) == n, q["id"] + " duplicate options")
    check(q["format"] != "multi" or len(q["answer"]) >= 2, q["id"] + " multi needs >=2 answers")
    check(q["format"] in ("mcq", "multi", "tf", "ar"), q["id"] + " format")
    check(1 <= q["week"] <= 12, q["id"] + " week")
    check(len(q["explanation"]) > 15, q["id"] + " explanation")
# source labelling honesty
for q in allq:
    st = q["source"]["type"]
    if st == "generated": check(q["source"]["year"] is None and q["source"]["url"] is None and not q["id"].startswith("O21"), q["id"] + " generated must not carry official metadata")
    elif st == "assignment": check(q["id"].startswith("O%02d-" % (q["source"]["year"] % 100)) and "transcribed" in q["source"]["verification"] and q.get("years"), q["id"] + " bad official metadata")
    else: fails.append(q["id"] + " unknown source type")
# numerical recomputation (independent of the build lambdas)
exp = {"N-W06-001": 10*math.log10(2e7), "N-W06-003": 80-20*math.log10(4), "N-W06-007": 2/(math.pi*4*30*15)*1e6 if False else None}
for q in D["numericals"]:
    check(len(q["steps"]) >= 1 and q["unit"] and q["formula"], q["id"] + " incomplete")
import math as m
L=m.log10
# independent expected values keyed by a unique substring of the "given" text
manual = [("5000 vehicles/day",72.0),("20,000 trips",19.2),("Bus lifecycle 600 t",25.0),("Input 100 t",10.0),("Plot 1000",5.0),("Runoff 5000",200.0),
 ("Point source measured 80 dB",80-20*L(4)),("Sources of 65 dB",10*L(2*10**6.5+10**6.8)),("Point source gives 90 dB",70.0),("Traffic line source gives 80 dB",80-10*L(4)),
 ("RMS sound pressure 2 Pa",100.0),("70 dB for 25%",10*L(.25e7+.75e5)),("Q = 5 g/s",5/(m.pi*5*40*20)*1e6),("Q = 2 g/s",2/(m.pi*4*30*15)*1e6),("2000 vehicles/day",15.0),
 ("250 L petrol",577.5),("90,000 of 240,000",37.5),("Benefit of 120",120/1.1-100),("Car lifecycle 40 t",40e6/300000),("Input 500 t",45.0),("Option A scores 8,6,7",7.2),
 ("BOD 25 mg/L",200.0),("Plot 1500",60.0),("Option B scores 6,9,8",7.3),("40 L/100 km (2.68 kg/L), 50",21.44),("8 L/100 km (2.31 kg/L), 1.5",123.2),("EV 15 kWh/100 km",120.0),("PV benefits 450",450/360)]
for sub,v in manual:
    hits=[q for q in D["numericals"] if sub in q["given"]]
    check(len(hits)==1, "manual key %r matched %d" % (sub,len(hits)))
    if hits: check(abs(hits[0]["answer"]-v)<=hits[0]["tolerance"]+1e-9, "%s expected %s got %s" % (sub,v,hits[0]["answer"]))
# mocks reference valid questions
idset = set(ids)
for m in D["mocks"]:
    check(len(m["ids"]) == len(set(m["ids"])), m["id"] + " duplicate in mock")
    check(all(i in idset for i in m["ids"]), m["id"] + " invalid id")
# coverage: every week has questions and cards
for w in range(1, 13):
    check(sum(1 for q in D["questions"] if q["week"] == w) >= 7, "week %d too few questions" % w)
    check(sum(1 for c in D["cards"] if c["week"] == w) >= 8, "week %d too few cards" % w)
off=[q for q in allq if q["source"]["type"]=="assignment"]
check(sum(1 for q in off if q["id"].startswith("O21-"))==125, "expected 125 official 2021")
check(sum(1 for q in off if q["format"]=="num")==2, "official numerics")
print("official", len(off))
print("questions", len(D["questions"]), "numericals", len(D["numericals"]), "cards", len(D["cards"]))
print("FAIL" if fails else "PASS")
for f in fails: print(" -", f)
sys.exit(1 if fails else 0)
