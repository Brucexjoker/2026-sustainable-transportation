"""Builds app/data/data.js from the content modules. Run: python3 content/build.py"""
import json, os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
from weeks_a import W as WA
from weeks_b import W as WB
from questions import Q, AR
from questions2 import Q2
from numericals import N
from numericals2 import N2
from questions3 import Q3
Q = Q + Q2 + [(t[0] + 100,) + t[1:] for t in Q3]
N = N + N2

OUT = os.path.join(os.path.dirname(__file__), "..", "app", "data", "data.js")
from weeks_real import WEEKS
weeks = WEEKS
TOPIC_ABBR = [("EIA","Environmental Impact Assessment"),("EMP","Environmental Management Plan"),("FAR/FSI","Floor Area Ratio / Floor Space Index"),("NUTP","National Urban Transport Policy"),("TDM","Transport Demand Management"),("BRT","Bus Rapid Transit"),("BRTS","Bus Rapid Transit System"),("NMT","Non-Motorised Transport"),("NAAQS","National Ambient Air Quality Standards"),("PM","Particulate Matter"),("BOD","Biochemical Oxygen Demand"),("COD","Chemical Oxygen Demand"),("DO","Dissolved Oxygen"),("Leq","Equivalent continuous sound level"),("BAU","Business-As-Usual"),("DSS","Decision Support System"),("MCDA","Multi-Criteria Decision Analysis"),("AHP","Analytic Hierarchy Process"),("GIS","Geographic Information System"),("BCR","Benefit-Cost Ratio"),("NPV","Net Present Value"),("PUC","Pollution Under Control"),("R&R","Resettlement & Rehabilitation"),("LCA","Life Cycle Assessment"),("LCI","Life Cycle Inventory"),("LCIA","Life Cycle Impact Assessment"),("GWP","Global Warming Potential"),("MFA","Material Flow Analysis"),("STAN","subSTance flow ANalysis (software)"),("CNG","Compressed Natural Gas"),("EV","Electric Vehicle"),("pkm","passenger-kilometre")]

SRC = dict(type="generated", label="Self-made practice (reviewed)", year=None, url=None, verification="self-made-reviewed: written for this app from lecture topics; answers and explanations re-checked in a second full review pass; NOT an official NPTEL question")


WEEK_FIX = {"Travel demand is called a derived demand": 1, "Which are modes of transport?": 1, "Which is an external cost of road transport?": 2, "Select Avoid": 10}
def remap(wk, topic):
    """Old (syllabus-PDF) week -> real lecture week."""
    if wk >= 100: return wk - 100
    base = {1:3, 2:5, 3:6, 4:2, 5:3, 6:9, 7:8, 8:3, 9:7, 10:2}
    if wk in base:
        if wk == 3 and topic in ("Demand",): return 7
        return base[wk]
    if wk == 11:
        return {"Concept":1,"Modes":11,"NMT":11,"EV":10,"Fuels":10,"Indicators":12,"Last mile":11,"Emerging":10}.get(topic, 11)
    if wk == 12:
        return {"LCA":7,"MFA":8,"Tools":12,"Projects":11}.get(topic, 12)
    return wk
def remap_num(wk, topic):
    if wk == 3: return 6
    if wk == 7: return 8
    if wk == 11: return 10
    if wk == 12: return 7 if topic == "LCA" else 8
    return remap(wk, topic)

questions = []
cnt = {}
for (wk, topic, typ, diff, text, opts, ans, expl) in Q:
    wk = remap(wk, topic)
    for _k, _v in WEEK_FIX.items():
        if text.startswith(_k): wk = _v
    cnt[wk] = cnt.get(wk, 0) + 1
    qid = "Q-W%02d-%03d" % (wk, cnt[wk])
    o = dict(id=qid, week=wk, topic=topic, format=typ, difficulty=diff, text=text, explanation=expl, source=SRC, related=[topic])
    if typ == "tf":
        o["options"] = ["True", "False"]; o["answer"] = [0 if ans else 1]; o["format"] = "tf"
    elif typ == "ar":
        o["options"] = AR; o["answer"] = [ans]
    elif typ == "multi":
        o["options"] = opts; o["answer"] = sorted(ans)
    else:
        o["options"] = opts; o["answer"] = [ans]
    questions.append(o)

numericals = []
ncnt = {}
for (wk, topic, diff, given, req, formula, steps, unit, calc, tol, expl) in N:
    wk = remap_num(wk, topic)
    ncnt[wk] = ncnt.get(wk, 0) + 1
    nid = "N-W%02d-%03d" % (wk, ncnt[wk])
    val = round(calc(), 4)
    numericals.append(dict(id=nid, week=wk, topic=topic, format="num", difficulty=diff, given=given, required=req, formula=formula, steps=steps, unit=unit, answer=val, tolerance=tol,
        text="Given: %s. Find: %s (%s)." % (given, req, unit), explanation=expl, source=SRC, related=[topic]))

# ---- Official assignments (Jul-Oct 2021 session), transcribed from user-supplied portal screenshots
from official2021 import O
OSRC = dict(type="assignment", label="Official NPTEL assignment (Jul-Oct 2021)", year=2021, url="https://nptel.ac.in/courses/105107210",
  document="NPTEL Sustainable Transportation Systems - Assignments 0-12, Jul-Oct 2021 session (portal screenshots supplied by the user)",
  verification="transcribed-from-official-portal-screenshots: question text and accepted answer copied by hand from the NPTEL portal; not independently re-verified")
NUMU = {(0,2): "%", (8,3): "g"}
for (an, qn, typ, text, opts, ans, expl) in O:
    wk = 1 if an == 0 else an
    oid = "O21-A%02d-%02d" % (an, qn)
    base = dict(id=oid, week=wk, topic="Official Assignment %d (2021)" % an, difficulty="official", text=text, explanation=expl, source=OSRC, related=["Assignment %d" % an], assignment=an)
    if typ == "num":
        base.update(format="num", given=text, required="value", formula="See explanation", steps=[expl], unit=NUMU[(an, qn)], answer=ans[0], tolerance=ans[1])
        numericals.append(base)
    else:
        base.update(format="tf" if typ == "tf" else "mcq", options=opts, answer=[ans])
        questions.append(base)


# ---- Official weekly assignments for later years (tuple format: see content/official2026.py).
# 2026 is built in; to add 2022-2025 create content/official2022.py ... official2025.py defining P in the same format.
import difflib, importlib
def _norm(t): return "".join(ch for ch in t.lower() if ch.isalnum())
def add_year(year, P, how):
    OS = dict(type="assignment", label="Official NPTEL assignment (%d)" % year, year=year, url="https://nptel.ac.in/courses/105107210",
      document="NPTEL Sustainable Transportation Systems - weekly assignments %d (%s)" % (year, how),
      verification="transcribed-from-official-%d-assignment-source: %s; explanation written by the assistant" % (year, how))
    pool = [q for q in questions if q["source"]["type"] == "assignment" and q["source"]["year"] != year]
    merged = added = 0
    for (w, n, text, opts, ans, basis, expl) in P:
        idx = "abcde".index(ans); corr = _norm(opts[idx]); hit = None
        for q in pool:
            if difflib.SequenceMatcher(None, _norm(q["text"]), _norm(text)).ratio() >= 0.98 and set(map(_norm, q["options"])) == set(map(_norm, opts)):
                hit = q; break
        if hit:
            if _norm(hit["options"][hit["answer"][0]]) != corr:
                print("WARNING: keys differ for", hit["id"], "/ %d W%d Q%d" % (year, w, n)); hit = None
            else:
                prev = hit["source"].get("also_years", [])
                hit["source"] = dict(hit["source"], also_years=prev + [year], also_year=year)
                hit["source"]["label"] = "Official NPTEL assignment (" + " & ".join(str(y) for y in sorted([hit["source"]["year"]] + hit["source"]["also_years"])) + ")"
                merged += 1; continue
        questions.append(dict(id="O%02d-W%02d-%02d" % (year % 100, w, n), week=w, topic="Official Assignment Week %d (%d)" % (w, year), difficulty="official", text=text, explanation=expl,
            source=OS, related=["Assignment %d (%d)" % (w, year)], assignment=w, format="tf" if opts == ["True", "False"] else "mcq", options=opts, answer=[idx]))
        added += 1
    print("official %d: merged into earlier years = %d, added new = %d" % (year, merged, added))
from official2026 import P as P26
add_year(2026, P26, "PDFs supplied by the user; correct option highlighted yellow")
for _y in (2022, 2023, 2024, 2025):
    try: _m = importlib.import_module("official%d" % _y)
    except ModuleNotFoundError: continue
    add_year(_y, _m.P, getattr(_m, "HOW", "supplied by the user"))

for _q in questions + numericals:
    if _q["source"]["type"] == "assignment":
        _q["years"] = sorted({_q["source"]["year"]} | set(_q["source"].get("also_years", [])))
    else:
        _q["years"] = []

# Mocks (deterministic, round-robin over weeks)
rnd = random.Random(105107210)
def pick(pool, n):
    by = {}
    for q in pool: by.setdefault(q["week"], []).append(q)
    for v in by.values(): rnd.shuffle(v)
    out = []
    while len(out) < n and any(by.values()):
        for w in sorted(by):
            if by[w] and len(out) < n: out.append(by[w].pop())
    return [q["id"] for q in out]
conc = [q for q in questions]
mock1 = pick([q for q in conc if q["difficulty"] in ("easy", "medium")], 40)
m2c = pick([q for q in conc if q["difficulty"] in ("medium",)], 32)
m2n = pick([q for q in numericals if q["difficulty"] in ("easy", "medium")], 8)
mock2 = m2c + m2n
m3c = pick([q for q in conc if q["difficulty"] in ("medium", "hard")], 30)
m3n = pick([q for q in numericals if q["difficulty"] in ("medium", "hard")], 10)
mock3 = m3c + m3n
mocks = [
 dict(id="M1", title="Mock Test 1: Fundamentals and conceptual understanding", ids=mock1, minutes=45),
 dict(id="M2", title="Mock Test 2: Mixed conceptual and numerical", ids=mock2, minutes=60),
 dict(id="M3", title="Mock Test 3: Advanced revision and application", ids=mock3, minutes=60),
]

cards = []
for w in weeks:
    for i, (a, b) in enumerate(w["cards"]):
        cards.append(dict(id="C-W%02d-%02d" % (w["id"], i + 1), week=w["id"], kind="qa", front=a, back=b))
    for i, (t, d) in enumerate(w["definitions"]):
        cards.append(dict(id="D-W%02d-%02d" % (w["id"], i + 1), week=w["id"], kind="definition", front="Define: " + t, back=d))
    for i, (n, f, u) in enumerate(w["formulas"]):
        cards.append(dict(id="F-W%02d-%02d" % (w["id"], i + 1), week=w["id"], kind="formula", front="Formula: " + n, back="%s   [unit: %s]" % (f, u)))
    for i, c in enumerate(w["cases"]):
        cards.append(dict(id="K-W%02d-%02d" % (w["id"], i + 1), week=w["id"], kind="case", front="Case/application, Week %d" % w["id"], back=c))
    for i, m in enumerate(w["misconceptions"]):
        cards.append(dict(id="X-W%02d-%02d" % (w["id"], i + 1), week=w["id"], kind="misconception", front="Common misconception (Week %d) - what is wrong?" % w["id"], back=m))
for i, (a, b) in enumerate(TOPIC_ABBR):
    cards.append(dict(id="A-%03d" % (i + 1), week=0, kind="abbreviation", front="Full form: " + a, back=b))

wk_out = []
for w in weeks:
    wk_out.append(dict(id=w["id"], title=w["title"], overview=w["overview"], objectives=w["objectives"],
        notes=[dict(h=h, p=p) for h, p in w["notes"]], definitions=[dict(term=t, def_=d) for t, d in w["definitions"]],
        concepts=w["concepts"], formulas=[dict(name=n, formula=f, unit=u) for n, f, u in w["formulas"]],
        example=w["example"], applications=w["applications"], cases=w["cases"], misconceptions=w["misconceptions"],
        revision=w["revision"], refs=w["refs"]))

data = dict(
  course=dict(name="Sustainable Transportation Systems", code="105107210", institute="IIT Roorkee", instructor="Prof. Bhola Ram Gurjar", url="https://nptel.ac.in/courses/105107210", syllabus_pdf="https://archive.nptel.ac.in/content/syllabus_pdf/105107210.pdf", weeks_total=12),
  weeks=wk_out, questions=questions, numericals=numericals, mocks=mocks, cards=cards,
  sources=dict(official_assignments=0, official_pyq=0, note="No official assignments or final-exam papers could be accessed from public pages; every question is newly generated. See VERIFICATION_REPORT.md."),
)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("window.DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
print("weeks", len(wk_out), "questions", len(questions), "numericals", len(numericals), "cards", len(cards), "mocks", [len(m["ids"]) for m in mocks])
