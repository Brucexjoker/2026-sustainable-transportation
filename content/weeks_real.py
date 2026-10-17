"""Weeks rebuilt to the REAL lecture structure (lecture titles read from the NPTEL portal screenshots, Jul-Oct 2021 session).
Merges new content with the older notes in weeks_a/weeks_b. Facts marked 'assignment key' come from the official 2021 assignment answer keys."""
from weeks_a import W as WA
from weeks_b import W as WB
OLD = {w["id"]: w for w in WA + WB}

def merge(new, *olds):
    out = dict(new)
    for k in ("objectives", "concepts", "applications", "cases", "misconceptions", "revision", "refs", "definitions", "formulas", "cards", "notes"):
        out[k] = list(new.get(k, []))
        for o in olds: out[k] += o.get(k, [])
    if not out.get("example"): out["example"] = olds[0]["example"]
    out["overview"] = new["overview"]
    return out

N = {}
N[1] = dict(id=1, title="Introduction to Transportation Systems and Sustainability",
 overview="Lectures 1-5: transportation systems, the concept of sustainability, the current transport scenario in India, and climate change indicators and impacts.",
 objectives=["Describe transport modes and their relative efficiency.","State the definition of sustainable development and the 17 SDGs.","Summarise India's transport scenario (vehicle composition, modal shares).","Link transport to climate change."],
 notes=[("Transportation systems and modes",["Modes: road, rail, water, air and pipelines, plus walking and cycling. Walking is the oldest form of human transport. Per tonne-km, waterways are the most fuel-efficient mode (assignment key), then rail, then road, then air."]),
  ("Sustainability and the SDGs",["Sustainable development meets present needs without compromising the ability of future generations to meet their own needs. It needs an energy source that cannot be exhausted completely and can meet growing demand. The UN has 17 Sustainable Development Goals; they are not only about environment (they include poverty, health, education, equality and economy).","India's PURA (Provision of Urban Amenities to Rural Areas) strategy was proposed by Dr A. P. J. Abdul Kalam."]),
  ("Transport scenario in India",["Road transport dominates; two-wheelers form the largest share of registered motor vehicles (roughly 70%+ in recent decades) while the share of buses is small. Vehicle numbers have grown much faster than road length."]),
  ("Climate change",["Transport is a major source of CO2. Climate indicators include rising temperature, sea level and extreme events. The Paris Agreement aims to keep temperature rise well below 2 degC."]),
  ("Forecasting traffic growth",["A simple elasticity method: traffic growth rate = elasticity x economic growth rate. Example (assignment 0): 2.3 x 7.6 = 17.48 %."])],
 definitions=[("Sustainable development","Development that meets present needs without compromising future generations' ability to meet theirs."),("SDG","Sustainable Development Goal; 17 goals adopted by the UN."),("PURA","Provision of Urban Amenities to Rural Areas."),("Elasticity of traffic","Ratio of traffic growth rate to economic growth rate.")],
 formulas=[("Traffic growth (elasticity method)","Traffic growth rate = elasticity x economic growth rate","%")],
 example=dict(q="Economic growth is forecast as 7.6 and the elasticity constant is 2.3. Find the forecast traffic growth rate.",steps=["Growth = 2.3 x 7.6 = 17.48 %."],ans="17.48 % (the portal accepted 17.40-17.50)."),
 applications=["Choosing waterways/rail for bulk freight to save fuel.","Using SDG indicators to track transport policies."],
 cases=["India's vehicle fleet composition over 1951-2016 shows rapid growth of two-wheelers (assignment 1 graph question)."],
 misconceptions=["SDGs are not only about environment.","Fuel-efficient does not mean fast: waterways are efficient but slow."],
 revision=["17 SDGs; Brundtland definition; waterways most fuel-efficient; walking first mode; PURA - Kalam; Paris < 2 degC."],
 cards=[("How many SDGs are there?","17."),("Most fuel-efficient freight mode?","Waterways."),("Who proposed PURA?","Dr A. P. J. Abdul Kalam."),("Traffic growth formula?","Elasticity x economic growth rate.")],
 refs=["NPTEL 105107210 Week 1 lectures and Assignments 0-1 (2021)."])

N[2] = dict(id=2, title="Impacts of Transportation Systems",
 overview="Lectures 6-10: air pollution, accidents, noise, health, flora and fauna, soil and water impacts and their mitigation.",
 objectives=["List impacts of transport on air, noise, health, ecology, soil and water.","Know Indian vehicle emission norms and noise standards.","Explain mitigation measures."],
 notes=[("Emission norms and health",["Bharat Stage norms tighten with each number: BS-VI is the strictest listed (assignment key). Vehicular emissions increase with vehicle age and poor maintenance. Fossil-fuel emissions include benzene, NMVOC, hydrocarbons and CO. Lack of physical activity is a major factor for coronary heart disease. Traffic air pollution affects humans through inhalation, and the polluted area grows with the number of vehicles. Per-km emissions rise when speed is reduced (e.g. by speed bumps)."]),
  ("Noise",["Noise can raise heart rate and dilate the pupil. CPCB limits depend on area type (commercial/residential/industrial/silence) and day/night; the road width and land-use activities influence noise levels. Assignment key: CPCB standards are comparatively lower-emission than FHWA standards."]),
  ("Ecology, soil and water",["Roads divide habitat: a wolf population split by a road is habitat fragmentation. Ballast water from ships and oil spills affect water; soil pH and road drainage matter for soil and groundwater flow. Bhungroo is a groundwater recharge measure (live-session practice assignment)."]),
  ("Pandemic link",["International travel was a major reason for quick spread of COVID-19 (assignment key)."])],
 definitions=[("Bharat Stage","Indian vehicle emission standards modelled on Euro norms."),("Habitat fragmentation","Splitting of habitat by linear infrastructure."),("Ballast water","Water carried by ships for stability; can transport invasive organisms."),("Bioremediation","Microbial breakdown of oil/hydrocarbon pollution.")],
 example=None,
 applications=["Phasing in BS-VI fuel and vehicles.","Wildlife crossings and noise barriers."],
 cases=["Road through forest dividing a wolf population (assignment 2)."],
 misconceptions=["Noise is a direct impact, not indirect (live session key)."],
 revision=["BS-VI strictest; age + poor maintenance raise emissions; inactivity -> heart disease; habitat fragmentation."],
 cards=[("Strictest norm among BS-III to BS-VI?","BS-VI."),("What is habitat fragmentation?","Splitting of habitat into isolated parts by roads/rail."),("Inactivity is a major factor for which disease?","Coronary heart disease."),("Ballast water risk?","Releases microorganisms that can damage ecosystems.")],
 refs=["NPTEL 105107210 Week 2 lectures and Assignment 2 (2021)."])

N[3] = dict(id=3, title="Environmental Impact Assessment (EIA): Introduction, Processes and Methodologies",
 overview="Lectures 11-15: what EIA is, its stages, methodologies and the EIA process in India.",
 objectives=["Explain EIA stages and who does what.","Know EIA Notification 2006 categories and thresholds mentioned in assignments.","Use baseline concepts."],
 notes=[("EIA in India (assignment-key facts)",["Environment (Protection) Act implemented in 1986. High-impact projects are Category A (EIA Notification 2006). Harbours/ports are Category A above 5 million tonnes per annum. Categorisation of the project is done at screening; the Terms of Reference is the outcome of scoping. India's screening checklist is a hybrid of development/activity-centred and environment-impact-centred information. An Impact/Environmental Management Plan is compulsory in an EIA report.","Environmental management system sequence: environmental policy, planning, implementation, monitoring, review."])],
 definitions=[("Category A","Projects needing central appraisal under EIA Notification 2006 (high impact)."),("ToR","Terms of Reference, fixed at scoping.")],
 example=None, applications=["Port, highway and rail clearances."], cases=[], misconceptions=["Screening (categorisation) and scoping (ToR) are different stages."],
 revision=["EPA 1986; Category A; ports > 5 Mtpa; hybrid checklist; ToR from scoping."],
 cards=[("Year of Environment (Protection) Act?","1986."),("Ports are Category A above what capacity?","5 million tonnes per annum."),("Which stage gives ToR?","Scoping."),("Which stage categorises projects?","Screening.")],
 refs=["NPTEL 105107210 Week 3 lectures and Assignment 3 (2021)."])

N[4] = dict(id=4, title="Global EIA Practices and EIA Case Studies (Mumbai-Ahmedabad High Speed Rail)",
 overview="Lectures 16-20: global EIA practice and case studies, mainly the Mumbai-Ahmedabad High Speed Rail (MAHSR) project.",
 objectives=["Know India's hybrid screening approach and exemptions.","Describe the MAHSR project actors.","Identify mitigation examples."],
 notes=[("Practices and rules (assignment-key facts)",["India follows a hybrid approach for screening parameters. EIA reports are prepared by agencies registered with the Quality Council of India or as notified by the Ministry of Environment, Forest and Climate Change. Project splitting (dividing a project into pieces) is used to bypass the EIA process - it is not a legitimate stage. Border infrastructure projects are exempted. In the EIA draft notification 2020, border area is 100 km aerial distance. Compensatory afforestation offsets deforestation by planting new trees. Bamboo net plantation stabilises slopes against landslides."]),
  ("MAHSR case",["The Mumbai-Ahmedabad High Speed Rail (bullet train, Shinkansen technology) is India's first high-speed corridor. The project proponent is the National High Speed Rail Corporation (NHSRCL); the funding agency is the Japan International Cooperation Agency (JICA); a Special Purpose Vehicle is a legal entity for a project. The EIA's business-as-usual scenario was 'no high speed rail'."])],
 formulas=[("Project impact","Impact = condition with project - condition without project (BAU)","same unit as parameter")],
 definitions=[("Project splitting","Breaking a project into parts to avoid EIA thresholds."),("SPV","Special Purpose Vehicle: legal entity formed for a project."),("NHSRCL","National High Speed Rail Corporation Limited, the proponent of MAHSR."),("JICA","Japan International Cooperation Agency, funder of MAHSR.")],
 example=None, applications=["Slope stabilisation with bio-engineering."], cases=["MAHSR (Mumbai-Ahmedabad) EIA."],
 misconceptions=["BAU in the MAHSR EIA is the no-project scenario, not a different rail design."],
 revision=["Hybrid approach; QCI-registered consultants; splitting = bypass; border area 100 km (draft 2020); MAHSR: NHSRCL, JICA."],
 cards=[("MAHSR connects which cities?","Mumbai and Ahmedabad."),("Who funds MAHSR?","JICA."),("Project proponent of MAHSR?","NHSRCL."),("Project splitting is used to ...?","Bypass the EIA process.")],
 refs=["NPTEL 105107210 Week 4 lectures and Assignment 4 (2021)."])

N[5] = dict(id=5, title="Land Use, Zoning and Transit-Oriented Development (TOD)",
 overview="Lectures 21-25: EIA case study V, introduction to land use, land-use planning and zoning, TOD and its implementation.",
 objectives=["Explain land use planning and zoning.","State National TOD Policy (2017) parameters.","Distinguish greenfield and brownfield TOD."],
 notes=[("TOD (assignment-key facts)",["India's National TOD Policy was released in 2017. Walkshed radius: 500-800 m. For high-density TOD the minimum FAR is 300-500%. Inclusive TOD features people-centric public spaces, walking/cycling-friendly infrastructure and accessible public transit. Delhi Metro is an example of brownfield TOD. The World Bank gave the '3 values' framework for TOD assessment. The Vizhinjam seaport was listed with IFC as funder in the key.","The 74th constitutional amendment relates to urban land use/planning. Primary zones: commercial, residential, agricultural, etc. Chandigarh follows a grid/block pattern."])],
 definitions=[("TOD","Transit-Oriented Development: compact mixed-use development around transit stations."),("Walkshed","Area reachable on foot from a station."),("Brownfield TOD","TOD in an already built-up area."),("Greenfield TOD","TOD on undeveloped land.")],
 example=None, applications=["Station-area planning with higher FAR."], cases=["Delhi Metro (brownfield), Chandigarh grid."],
 misconceptions=["Walkshed of 500-800 m is not the same as 1-2 km catchment."],
 revision=["TOD policy 2017; walkshed 500-800 m; FAR 300-500%; Delhi Metro = brownfield; 74th Amendment."],
 cards=[("National TOD Policy year?","2017."),("Walkshed radius?","500-800 m."),("High-density TOD minimum FAR?","300-500%."),("Delhi Metro is which TOD type?","Brownfield.")],
 refs=["NPTEL 105107210 Week 5 lectures and Assignment 5 (2021)."])

N[6] = dict(id=6, title="TOD Case Studies and Sustainable Transport Planning (Traditional 4-step Process)",
 overview="Lectures 26-30: TOD case studies (Delhi Metro, Belgrade, Naya Raipur), introduction to sustainable transport planning and the traditional transport planning process.",
 objectives=["Explain the 4-step process in order.","Compute trip rate and floors from FAR.","Know TOD zone characteristics and value-capture tools."],
 notes=[("Assignment-key facts",["Order: trip generation, trip distribution, modal split, trip assignment. Ideal trip distribution balances trips generated and attracted (equal). The gravity model resembles Newton's law of gravitation. Hard land is land whose use cannot be changed. The external cordon is the imaginary boundary of the study area. In TOD, the transition zone has the highest residential share and the station area the highest FAR. Development-based land value capture includes air rights sale, joint development and land readjustment.","Trip rate = trips / population (e.g. 12000/4000 = 3). Floors = FAR x plot area / (coverage x plot area): with FAR 5 and 50% coverage -> 10 floors."]),
  ("Case studies",["Delhi Metro (Section of Delhi Metro), Belgrade (Serbia) and Naya Raipur are the TOD case studies in the lectures; refer to the lecture videos for details, which are not reproduced here."])],
 definitions=[("External cordon","Boundary around the study area in transport planning."),("Hard land","Land use that cannot be changed."),("Land value capture","Recovering part of the value created by public investment."),("Trip rate","Trips per person (or household) per day.")],
 formulas=[("Trip rate","Trips / Population","trips per person")],
 example=dict(q="A residential zone has population 4000 and 12000 trips. Find the trip rate.",steps=["12000 / 4000 = 3."],ans="3 trips per person."),
 applications=["Planning TOD around metro stations."], cases=["Delhi Metro, Belgrade, Naya Raipur (lectures 26-28)."],
 misconceptions=["Modal split is step 3, not step 4."],
 revision=["4 steps in order; gravity model; external cordon; station area highest FAR; transition zone highest residential."],
 cards=[("Four steps in order?","Generation, distribution, modal split, assignment."),("Gravity model analogy?","Newton's law of gravitation."),("Hard land?","Land use that cannot be changed."),("Highest FAR zone in TOD?","Station area.")],
 refs=["NPTEL 105107210 Week 6 lectures and Assignment 6 (2021)."])

N[7] = dict(id=7, title="Contemporary Transport Planning, Management Strategies and Life Cycle Assessment (LCA)",
 overview="Lectures 31-35: contemporary planning process, transportation system management, and LCA (introduction, theory and case study).",
 objectives=["Contrast accessibility and mobility based planning.","Name TSM strategies and traffic calming types.","State LCA stages, ISO series and system boundaries."],
 notes=[("Planning and management (assignment-key facts)",["Contemporary planning emphasises accessibility over mobility. Spatial imprint varies with socio-economic and geographical characteristics of a city. TSM/management strategies include exclusive bus lanes, cordon pricing and internal shuttles. A contra-flow lane is used exclusively for peak-direction traffic. Speed bumps are vertical deflection in traffic calming."]),
  ("LCA",["ISO 14040 series covers LCA. Stages: goal and scope, inventory, impact assessment, interpretation (risk management is not a stage). Cradle-to-gate = raw material extraction to manufactured product. Applications include product improvement and environmental planning."])],
 definitions=[("Accessibility","Ease of reaching destinations; the goal of contemporary planning."),("Contra-flow lane","Lane reversed to serve peak-direction traffic."),("Traffic calming","Measures (e.g. humps) reducing vehicle speeds.")],
 example=None, applications=["Exclusive bus lanes, cordon pricing."], cases=["LCA case study (lecture 35)."],
 misconceptions=["Risk management is not an LCA stage."],
 revision=["Accessibility > mobility; ISO 14040; cradle-to-gate; speed bump = vertical deflection."],
 cards=[("LCA standard series?","ISO 14040."),("Cradle-to-gate ends at?","The factory gate."),("Is a speed bump vertical or horizontal deflection?","Vertical."),("Not an LCA stage?","Risk management.")],
 refs=["NPTEL 105107210 Week 7 lectures and Assignment 7 (2021)."])

N[8] = dict(id=8, title="Material Flow Analysis, Circular Economy and Modelling of Transport Emissions",
 overview="Lectures 36-40: MFA and case study, circular economy (including in transport) and modelling of transport emissions I.",
 objectives=["Apply the MFA mass balance.","Contrast linear and circular economies.","Recognise emission models and their developers."],
 notes=[("MFA and CE (assignment-key facts)",["MFA is based on mass conservation: Input = Output + Stock. Example: 100 L fuel with 2 g lead/L gives 200 g input; if 180 g is found after combustion, stock = 20 g. The linear economy is take-make-consume-throw away; the circular economy rests on regenerating natural systems, durable products and minimising waste, and is shown in the butterfly diagram.","MOBILE was superseded by MOVES (US EPA). EMFAC is developed by the California Air Resources Board. COPERT is the European model. Emission models use vehicle type, fuel category and vehicle-km travelled."])],
 definitions=[("MFA","Material Flow Analysis: tracking material flows and stocks via mass balance."),("Circular economy","Economy designed to keep materials in use and regenerate natural systems."),("MOVES","US EPA Motor Vehicle Emission Simulator."),("EMFAC","California Air Resources Board emission factor model.")],
 example=dict(q="100 L fuel with 2 g lead per litre; 180 g lead found after combustion. Find the stock.",steps=["Input = 200 g; Output = 180 g; Stock = 20 g."],ans="20 g."),
 applications=["Tracking lead or CO2 flows in transport systems."], cases=["MFA case study (lecture 37)."],
 misconceptions=["Butterfly diagram = circular economy, not linear."],
 revision=["Input = Output + Stock; linear = throw away; MOBILE -> MOVES; EMFAC = CARB."],
 cards=[("MFA equation?","Input = Output + Stock."),("Butterfly diagram shows?","Circular economy."),("EMFAC developed by?","California Air Resources Board."),("MOVES replaced?","MOBILE.")],
 refs=["NPTEL 105107210 Week 8 lectures and Assignment 8 (2021)."])

N[9] = dict(id=9, title="Emission Modelling, Dispersion Models, Traffic Noise Models and Policies",
 overview="Lectures 41-45: modelling transport emissions II, dispersion models, traffic noise models, initiatives and policies, and NCAP.",
 objectives=["Name Gaussian and other dispersion models.","Know inputs to dispersion models.","Recall key policies and numbers (Paris, NAPCC, NCAP)."],
 notes=[("Assignment-key facts",["VAPI (Vehicular Air Pollution Inventory) model does not include a speed correction factor (per key). Dispersion = spread of pollutants horizontally and vertically. Gaussian models include AERMOD, CALPUFF and CALINE4; GRAL is the one that is not Gaussian per the key. Dispersion model inputs: topography, meteorology, emissions. Vehicular emissions are treated as a line source. The FHWA traffic noise model does not consider an area adjustment (shielding, flow and segment adjustments are considered).","Paris Agreement: well below 2 degC. NAPCC adopted in 2008. NCAP: 122 targeted cities (2021 key); it aims to reduce particulate matter."])],
 definitions=[("Dispersion","Spreading of pollutants by wind and turbulence."),("NCAP","National Clean Air Programme."),("NAPCC","National Action Plan on Climate Change (2008)."),("Line source","Emission source along a line, e.g. a road.")],
 example=None, applications=["Predicting roadside concentrations with CALINE4."], cases=[],
 misconceptions=["Roads are line sources, not point sources."],
 revision=["Gaussian: AERMOD, CALPUFF, CALINE4; NAPCC 2008; NCAP 122 cities, PM; Paris < 2 degC."],
 cards=[("NAPCC adopted in?","2008."),("NCAP targets which pollutant?","Particulate matter."),("Inputs to a dispersion model?","Topography, meteorology and emissions."),("Vehicle emissions are what type of source?","Line source.")],
 refs=["NPTEL 105107210 Week 9 lectures and Assignment 9 (2021)."])

N[10] = dict(id=10, title="Decarbonization, Alternative Fuels, EVs, Hyperloop and BRTS",
 overview="Lectures 46-50: decarbonizing transport, alternate fuels, electric vehicles, Hyperloop and Bus Rapid Transit System (BRTS).",
 objectives=["Know the ASI framework.","Compare fuels and EVs.","State Hyperloop limits and BRTS features."],
 notes=[("Assignment-key facts",["Decarbonisation options: NMT, congestion pricing, user-friendly public transport (promoting air transport is not an option). ASI = Avoid-Shift-Improve. Fuel vs food debate: food crops should first feed people. Linkoping (Sweden) uses 100% biogas for urban transport. Efficient EV batteries need high charge retention. EVs have zero tail-pipe emissions (not zero overall). Cleaner electricity helps decarbonise transport. Hyperloop limitations include turnings, passenger comfort/space and dizziness from acceleration, but it is not weather-sensitive (sealed tube); the first Indian proposal listed is Mumbai-Pune. Efficient BRTS has dedicated lanes, real-time information, integrated ticketing and elevated/level platforms, not mixed lanes."])],
 formulas=[("EV emission per km","EF = kWh/km x grid EF (kg CO2/kWh)","kg CO2/km"),("Fuel CO2","CO2 = litres x fuel EF","kg")],
 definitions=[("ASI","Avoid-Shift-Improve framework."),("Hyperloop","Proposed high-speed transport in low-pressure tubes."),("BRTS","Bus Rapid Transit System with dedicated lanes and quality stations."),("Tail-pipe emission","Exhaust emission from the vehicle.")],
 example=None, applications=["Electric buses on BRTS corridors."], cases=["Linkoping biogas buses."],
 misconceptions=["EV does not mean zero emissions overall."],
 revision=["ASI; EV zero tail-pipe; BRTS = dedicated lane; Linkoping biogas; Hyperloop Mumbai-Pune."],
 cards=[("ASI stands for?","Avoid-Shift-Improve."),("EV emissions at the vehicle?","Zero tail-pipe emissions."),("Which Swedish city uses 100% biogas buses?","Linkoping."),("Not a BRTS feature?","Mixed lanes.")],
 refs=["NPTEL 105107210 Week 10 lectures and Assignment 10 (2021)."])

N[11] = dict(id=11, title="Mass Rapid Transit, Airports, Water Transport, NMT and openLCA",
 overview="Lectures 51-55: case studies on MRT, sustainability in airports, sustainable water transport, NMT, and an introduction to openLCA.",
 objectives=["Know airport impacts and rating systems.","Know water-transport issues (ballast water, national waterways).","State NMT benefits."],
 notes=[("Assignment-key facts",["Airport impacts: noise, land-use change, de-icing emissions. Airport rating systems: BREEAM, LEED, ENVISION (PANACHE is the odd one out per key). Delhi's IGI Airport was the first carbon-neutral tagged airport in Asia-Pacific. Ballast water can release microorganisms causing ecosystem damage. National Waterway-2 is on the Brahmaputra. NMT gives safety/health, recreation, near-zero emissions; fatalities tend to fall as NMT share rises. Copenhagen is the 'City of Cyclists'. LCA tools: GaBi, SimaPro, Umberto (CALINE is not). Metro success needs dense population, positive attitude to public transport and last-mile connectivity, not scattered settlements."])],
 definitions=[("NW-2","National Waterway 2 on the Brahmaputra."),("ENVISION","Sustainability rating system for infrastructure."),("Last-mile connectivity","Access between a station and the final destination.")],
 example=None, applications=["Carbon-neutral airports, cycling cities."], cases=["IGI Airport; Copenhagen."],
 misconceptions=["NMT is not 'very fast connectivity'."],
 revision=["IGI carbon neutral; NW-2 Brahmaputra; Copenhagen cyclists; GaBi/SimaPro/Umberto are LCA tools."],
 cards=[("NW-2 is on which river?","Brahmaputra."),("City of Cyclists?","Copenhagen."),("First carbon-neutral airport in Asia-Pacific (per key)?","Indira Gandhi International Airport."),("Name three LCA tools.","GaBi, SimaPro, Umberto.")],
 refs=["NPTEL 105107210 Week 11 lectures and Assignment 11 (2021)."])

N[12] = dict(id=12, title="openLCA, STAN, Sustainability Indicators, STAR and Measuring Sustainability",
 overview="Lectures 56-60: openLCA case study, STAN material flow analysis tool, sustainability indicators, STAR rating and measuring sustainability.",
 objectives=["Know tools: openLCA, STAN.","Know STAR rating system basics.","Know SDG India Index and EPI facts."],
 notes=[("Assignment-key facts",["STAN is used for material flow analysis. STAR = Sustainable Transportation Appraisal Rating, developed by the Asian Development Bank (the system does NOT have 4 criteria and 15 sub-criteria). SDG India Index is developed by NITI Aayog; its method: raw data, target setting, normalisation, goal score, composite score; SDG-17 was omitted from the index. In the Environmental Performance Index, environmental vitality has a weightage of 60%; the Global West ranks highly."])],
 formulas=[("LCA per functional unit","Impact / FU = total life-cycle impact / total functional units","e.g. g CO2e/pkm"),("MFA balance","Input = Output + Stock change","t")],
 definitions=[("STAR","Sustainable Transportation Appraisal Rating (ADB)."),("SDG India Index","NITI Aayog's index tracking SDG progress."),("EPI","Environmental Performance Index.")],
 example=None, applications=["Rating transport projects with STAR."], cases=["openLCA application case study (lecture 56)."],
 misconceptions=["STAR was not developed by the World Bank."],
 revision=["STAN = MFA; STAR by ADB; SDG India Index by NITI Aayog; EPI vitality 60%."],
 cards=[("STAR developed by?","Asian Development Bank."),("SDG India Index developed by?","NITI Aayog."),("EPI vitality weight?","60%."),("Software for MFA?","STAN.")],
 refs=["NPTEL 105107210 Week 12 lectures and Assignment 12 (2021)."])

for _i, _w in N.items():
    _w.setdefault('concepts', _w['revision'][:])
MERGE = {1: [], 2: [4, 10], 3: [1, 5, 8], 4: [], 5: [2], 6: [3], 7: [12, 9], 8: [7], 9: [6], 10: [], 11: [11], 12: []}
WEEKS = []
for i in range(1, 13):
    olds = [OLD[j] for j in MERGE[i]]
    n = dict(N[i])
    for k in ("objectives","concepts","applications","cases","misconceptions","revision","refs","definitions","formulas","cards","notes"): n.setdefault(k, [])
    n.setdefault("example", None)
    if olds: m = merge(n, *olds)
    else:
        m = dict(n)
        m["example"] = n["example"] or dict(q="See the formulas and assignment-key facts above.", steps=["Revise the key numbers and definitions."], ans="n/a")
    # drop old-note items that duplicate nothing (old notes keep their own headings)
    WEEKS.append(m)
