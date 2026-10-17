"""Weeks 1-6 study material. Titles follow the official NPTEL syllabus PDF (105107210)."""

W = []

W.append(dict(
 id=1, title="Introduction to EIA and Transportation Systems",
 overview="Transport moves people and goods but also consumes energy, land and produces emissions, noise and accidents. Environmental Impact Assessment (EIA) is the systematic process used to predict, evaluate and manage these effects before a project is approved.",
 objectives=["Describe the components of a transportation system and its modes.","Define EIA and explain why it is needed for transport projects.","List the main stages of the EIA process.","Distinguish screening, scoping, baseline study, impact prediction, mitigation and monitoring."],
 notes=[
  ("Transportation system", ["A transport system consists of infrastructure (roads, rails, airports, ports), vehicles, operators and the rules that govern their use. Modes include road, rail, air, water and pipelines, plus non-motorised transport (walking, cycling).","Demand for transport is a derived demand: people travel to reach activities, so land use and transport are tightly linked."]),
  ("What is EIA?", ["EIA is a planning and decision-support tool that identifies likely environmental, social and economic consequences of a proposed project and recommends measures to avoid, reduce or compensate them. It is preventive: it is done before construction.","In India, the legal basis is the Environment (Protection) Act 1986 and the EIA Notification 2006 (as amended), which sorts projects into Category A (central appraisal) and Category B (state appraisal)."]),
  ("Stages of the EIA process", ["1. Screening: decide whether a full EIA is required. 2. Scoping: decide which impacts and alternatives to study (Terms of Reference). 3. Baseline data collection. 4. Impact identification and prediction. 5. Impact evaluation and significance. 6. Mitigation / Environmental Management Plan (EMP). 7. Public consultation. 8. Review and appraisal by an expert committee. 9. Decision. 10. Monitoring and follow-up.","Public consultation (public hearing and written responses) is a statutory step for most projects requiring EIA in India."]),
 ],
 definitions=[("EIA","A systematic process to predict and evaluate the environmental consequences of a proposed project and plan measures to manage them."),("Screening","Deciding whether a proposal needs EIA and at what level of detail."),("Scoping","Identifying the key issues, alternatives and boundaries of the study."),("EMP","Environmental Management Plan: the set of mitigation, monitoring and institutional measures to be carried out."),("Derived demand","Demand for a service (travel) that arises from the need to do something else.")],
 concepts=["EIA is preventive, not remedial.","Alternatives (including 'no-project') should be compared.","Impact = change in an environmental parameter caused by the project relative to baseline.","Early integration of EIA with design is cheaper than retrofitting."],
 formulas=[("Impact (conceptual)","Impact = Condition with project − Condition without project","same unit as parameter")],
 example=dict(q="A project area has measured PM10 of 80 µg/m³. Predicted PM10 with the project is 92 µg/m³ and predicted PM10 without the project (future baseline) is 84 µg/m³. What is the impact attributable to the project?",steps=["Impact compares with-project against without-project at the same future time.","Impact = 92 − 84 = 8 µg/m³."],ans="8 µg/m³ (not 12, because natural growth in background is excluded)."),
 applications=["Highway and expressway alignment studies.","Metro and railway corridor clearances.","Airport expansion and port development approvals."],
 cases=["Typical large linear projects (highways, rail) require EIA because they cross forests, water bodies and settlements; alignment alternatives are compared on environmental grounds."],
 misconceptions=["EIA does not 'approve or reject' by itself; it informs the decision-maker.","EIA is not only about pollution; it also covers social, ecological and cultural impacts.","Scoping is not the same as screening."],
 revision=["EIA = predict + evaluate + manage, before construction.","Order: screening → scoping → baseline → prediction → mitigation → consultation → appraisal → monitoring.","India: EIA Notification 2006; Category A (Centre), B (State)."],
 cards=[("What does EIA stand for and when is it done?","Environmental Impact Assessment; before project approval/construction."),("Screening vs scoping?","Screening decides IF EIA is needed; scoping decides WHAT it will cover."),("What is an EMP?","Environmental Management Plan: mitigation, monitoring and institutional arrangements."),("Why is travel a 'derived demand'?","People travel to reach activities, not for travel itself.")],
 refs=["NPTEL 105107210 Week 1 lectures (Prof. B. R. Gurjar, IIT Roorkee).","MoEF&CC, EIA Notification 2006 (public document)."],
))

W.append(dict(
 id=2, title="Land-use Plans, Zoning Schemes and Provisions",
 overview="Land use determines where trips begin and end. Zoning and development controls shape travel distance, mode choice and, therefore, transport impacts. Integrating land use and transport is the foundation of sustainable planning.",
 objectives=["Explain how land use drives travel demand.","Describe common zoning categories and development controls.","Define FAR/FSI, ground coverage and density.","Understand the role of master plans and mixed land use."],
 notes=[
  ("Land use and transport interaction", ["Land use generates trips (homes produce, offices attract). Transport accessibility in turn raises land value and attracts development, forming a feedback loop.","Compact, mixed-use development shortens trips and makes walking, cycling and public transport viable; dispersed, single-use development increases car dependence."]),
  ("Zoning", ["Zoning divides an area into zones (residential, commercial, industrial, recreational, public/semi-public, transport, agricultural) and regulates what can be built where.","Typical regulations: permitted uses, plot size, setbacks, height limits, Floor Area Ratio (FAR) or Floor Space Index (FSI), ground coverage, parking norms.","Master plans (e.g. city development plans) set land use for 20-year horizons and are reviewed periodically; zonal and local-area plans add detail."]),
  ("Mixed use and density", ["Mixed land use places homes, jobs and services close together, reducing average trip length.","Higher densities near transit stations support high-frequency service. Transit-oriented policies often grant higher FAR near stations."]),
 ],
 definitions=[("Zoning","Regulation dividing land into zones with controlled uses and development standards."),("FAR / FSI","Ratio of total built-up floor area to plot area."),("Ground coverage","Percentage of plot area covered by the building footprint."),("Master plan","Long-term statutory plan indicating land-use allocation and infrastructure."),("Mixed land use","Combination of compatible activities (residential, commercial, services) in one area.")],
 concepts=["Land use ↔ transport feedback.","Density + diversity + design support sustainable travel.","Parking norms influence car use.","Buffer/green zones separate incompatible uses (e.g. industry from housing)."],
 formulas=[("Floor Area Ratio","FAR = Total built-up floor area / Plot area","dimensionless"),("Ground coverage","GC (%) = Building footprint / Plot area × 100","%"),("Number of floors (approx.)","Floors = FAR / (GC/100)","count")],
 example=dict(q="A plot of 1000 m² has FAR 2.0 and permitted ground coverage 40%. Find the maximum built-up area and the number of floors.",steps=["Built-up area = FAR × plot area = 2.0 × 1000 = 2000 m².","Footprint = 0.40 × 1000 = 400 m².","Floors = 2000 / 400 = 5."],ans="2000 m² and 5 floors."),
 applications=["Station-area upzoning near metro stations.","Industrial zone buffers to protect residential areas from noise and air pollution.","Parking maximums in city centres."],
 cases=["Delhi Master Plan documents promote mixed land use and higher-density development along transit corridors (general policy direction)."],
 misconceptions=["FAR is not the same as ground coverage.","Higher FAR does not automatically mean more traffic if the area is well served by transit.","Zoning is not purely restrictive; it can also incentivise desired development."],
 revision=["FAR = floor area / plot area.","Mixed use → shorter trips.","Master plan: ~20-year, zoning: use + intensity rules."],
 cards=[("Formula for FAR?","Total built-up floor area ÷ plot area."),("Why does mixed land use help sustainability?","Shorter trips, more walking/cycling/transit viability."),("Name typical zones.","Residential, commercial, industrial, recreational, public/semi-public, transport, agricultural."),("What is a buffer zone?","Space (often green) separating incompatible land uses.")],
 refs=["NPTEL 105107210 Week 2 lectures.","State/city master plan documents (public)."],
))

W.append(dict(
 id=3, title="Urban and Regional Transport Planning",
 overview="Transport planning forecasts travel demand and chooses networks and policies to meet it. The classic framework is the four-step model, complemented by sustainability-oriented policies such as public transport priority and demand management.",
 objectives=["Explain the four-step travel demand model.","Describe urban versus regional planning scales.","Know India's urban transport policy directions.","Identify tools for demand management."],
 notes=[
  ("Four-step model", ["1. Trip generation: how many trips are produced/attracted by each zone. 2. Trip distribution: where trips go (origin-destination matrix; gravity model). 3. Modal split: which mode is used. 4. Traffic assignment: which routes are used.","Inputs: socio-economic data, land use, network characteristics, costs and travel times from household surveys and traffic counts."]),
  ("Urban vs regional planning", ["Urban planning deals with intra-city movement, congestion, public transport and last-mile access. Regional planning covers inter-city freight and passenger links (highways, railways, air, waterways) and economic corridors."]),
  ("Policy directions", ["India's National Urban Transport Policy (2006) emphasises people over vehicles: priority to public transport and non-motorised transport, integrated land use–transport planning, and use of cleaner technologies.","Common tools: Comprehensive Mobility Plans, parking pricing, congestion charging, low-emission zones, bus priority, integrated ticketing."]),
  ("Avoid–Shift–Improve", ["Avoid unnecessary travel (land-use planning), Shift to efficient modes (walking, cycling, public transport), Improve vehicle and fuel technology."]),
 ],
 definitions=[("Trip generation","Estimating number of trips produced by and attracted to zones."),("Modal split","Allocation of trips among available modes."),("Traffic assignment","Loading trips onto network routes."),("Gravity model","Distribution model where trips are proportional to attractions and inversely related to a function of travel cost/distance."),("TDM","Transport Demand Management: policies that reduce or reshape demand, e.g. pricing and parking control.")],
 concepts=["Four steps are sequential and iterative.","Mode hierarchy for sustainability: walk > cycle > public transport > shared > private car.","Supply expansion alone induces demand (induced traffic).","Planning must consider equity and safety."],
 formulas=[("Gravity model (conceptual)","Tij = Pi · Aj · f(cij) / Σj Aj f(cij)","trips"),("Mode share","Mode share (%) = Trips by mode / Total trips × 100","%")],
 example=dict(q="In a city, 45,000 of 150,000 daily trips are made by public transport. Find the public transport mode share.",steps=["Share = 45,000 / 150,000 × 100 = 30%."],ans="30%."),
 applications=["Metro corridor selection using projected demand.","Bus network redesign.","Parking policy to restrain car use."],
 cases=["Cities with Comprehensive Mobility Plans use the four-step model to compare BRT, metro and bus options."],
 misconceptions=["Building more road capacity does not permanently solve congestion (induced demand).","Modal split is not the same as traffic assignment."],
 revision=["4 steps: generation → distribution → modal split → assignment.","Avoid–Shift–Improve.","NUTP 2006: move people, not vehicles."],
 cards=[("List the four steps of travel demand modelling.","Trip generation, trip distribution, modal split, traffic assignment."),("What is induced demand?","Extra traffic generated by added road capacity."),("Avoid–Shift–Improve?","Reduce trips, shift to efficient modes, improve technology."),("What is TDM?","Transport Demand Management policies to reduce/reshape travel demand.")],
 refs=["NPTEL 105107210 Week 3 lectures.","National Urban Transport Policy 2006 (MoUD, public)."],
))

W.append(dict(
 id=4, title="Impacts on Humans, Flora and Fauna, Soil, Water, Air, Climate and Landscape",
 overview="Transport infrastructure and operations affect almost every environmental component. This week catalogues those impacts in construction and operation phases and links them to indicators.",
 objectives=["List major transport impacts on each environmental component.","Differentiate construction-phase and operation-phase impacts.","Explain habitat fragmentation and the barrier effect.","Relate pollutants to health outcomes."],
 notes=[
  ("Human impacts", ["Air pollutants (PM2.5, PM10, NOx, CO, HC) cause respiratory and cardiovascular disease; noise causes annoyance, sleep disturbance and stress; accidents cause injury and death; severance and displacement affect communities and livelihoods."]),
  ("Flora and fauna", ["Land clearing destroys habitat; roads and railways fragment habitat, causing animal–vehicle collisions and isolating populations. Mitigation: wildlife underpasses/overpasses, fencing, alignment away from sensitive areas."]),
  ("Soil and water", ["Construction causes erosion, compaction, contamination by fuels and oils, and sedimentation. Road runoff carries suspended solids, heavy metals, oil and de-icing salts. Drainage changes can alter flooding and groundwater recharge."]),
  ("Air and climate", ["Vehicles emit CO2 (greenhouse gas), CO, NOx, hydrocarbons, PM, SO2. Transport is a significant and growing source of CO2. Secondary pollutants such as ozone form from NOx and VOC in sunlight."]),
  ("Landscape", ["Visual intrusion, loss of agricultural land and heritage impacts. Good design and screening can reduce visual impacts."]),
 ],
 definitions=[("Habitat fragmentation","Breaking of continuous habitat into smaller isolated patches."),("Barrier effect (severance)","Reduced movement across a corridor because of a road or rail line."),("Secondary pollutant","Pollutant formed in the atmosphere from precursors, e.g. ozone."),("Sedimentation","Deposition of eroded soil particles in water bodies."),("Greenhouse gas","Gas that traps heat in the atmosphere, e.g. CO2, CH4, N2O.")],
 concepts=["Impacts occur in construction, operation and decommissioning phases.","Direct vs indirect impacts.","Vulnerable groups (children, elderly, roadside residents) face higher exposure.","Sensitive receptors: schools, hospitals, protected areas."],
 formulas=[("Linear emission estimate","E = N × L × EF","g (N vehicles, L km, EF g/km)")],
 example=dict(q="5000 vehicles per day travel a 12 km road. If the average CO emission factor is 1.2 g/km, estimate daily CO emission.",steps=["E = 5000 × 12 × 1.2 g = 72,000 g.","72,000 g = 72 kg."],ans="72 kg CO per day."),
 applications=["Siting schools and hospitals away from major roads.","Wildlife crossings on highways through forests.","Stormwater treatment of road runoff."],
 cases=["Highways through protected forests commonly require wildlife passages and compensatory afforestation as conditions of clearance."],
 misconceptions=["Only tailpipe emissions matter: construction, materials and fuel production also contribute.","Noise is not a 'minor' impact; it has documented health effects."],
 revision=["Air → health; habitat → fragmentation; runoff → water quality.","Both construction and operation phases matter.","Sensitive receptors need extra protection."],
 cards=[("What is habitat fragmentation?","Splitting of habitat into small isolated patches, often by linear infrastructure."),("Name a secondary pollutant from vehicles.","Ground-level ozone (from NOx + VOC)."),("Main road-runoff pollutants?","Suspended solids, heavy metals, oils."),("Wildlife mitigation measures?","Underpasses/overpasses, fencing, careful alignment.")],
 refs=["NPTEL 105107210 Week 4 lectures."],
))

W.append(dict(
 id=5, title="Establishing Baseline Conditions: Soil, Water and Air Quality",
 overview="A baseline is the description of existing environmental conditions before the project. Without a reliable baseline, impacts cannot be measured. Data come from monitoring, secondary sources and surveys.",
 objectives=["Explain the purpose of baseline studies.","Select parameters for air, water and soil baselines.","Design a monitoring network (location, frequency, duration).","Compare results with standards."],
 notes=[
  ("Baseline purpose", ["Baseline data (a) describe the existing state, (b) give a reference for predicting change, (c) identify sensitive receptors, (d) support later monitoring. Both primary data (field measurement) and secondary data (government records, literature) are used."]),
  ("Air quality baseline", ["Typical parameters: PM10, PM2.5, SO2, NOx, CO, ozone. Sampling stations are chosen using wind direction, land use, sensitive receptors and a core zone / buffer zone approach. Results are compared with the National Ambient Air Quality Standards (NAAQS)."]),
  ("Water quality baseline", ["Parameters include pH, turbidity, total suspended solids, dissolved oxygen (DO), BOD, COD, nutrients, oil and grease, coliforms and heavy metals. Sampling covers surface water and groundwater, upstream and downstream of the project."]),
  ("Soil baseline", ["Parameters: texture, pH, organic matter, nutrients, contamination (heavy metals, hydrocarbons), erosion potential and land capability. Samples are collected at representative depths and locations."]),
  ("Seasonality", ["Environmental data vary seasonally, so baseline monitoring should capture representative seasons; short periods may under- or over-estimate typical conditions."]),
 ],
 definitions=[("Baseline","Existing environmental condition before project implementation."),("Primary data","Data collected by direct measurement for the study."),("Secondary data","Data obtained from existing records or literature."),("BOD","Biochemical Oxygen Demand: oxygen consumed by microbes to decompose organic matter."),("NAAQS","National Ambient Air Quality Standards.")],
 concepts=["Study area: core zone and buffer zone.","Sampling design must reflect wind direction and receptors.","Quality assurance/quality control (QA/QC) is essential.","Compare each parameter with a legal standard."],
 formulas=[("Concentration conversion","1 mg/L = 1 g/m³","—"),("Pollutant load","Load = Concentration × Volume","e.g. g or kg")],
 example=dict(q="Runoff of 5000 m³ contains 40 mg/L total suspended solids. Find the TSS load.",steps=["40 mg/L = 40 g/m³.","Load = 40 × 5000 = 200,000 g = 200 kg."],ans="200 kg of TSS."),
 applications=["Pre-construction air monitoring along a proposed corridor.","River water sampling upstream and downstream of a bridge site."],
 cases=["Baseline surveys at proposed airports typically combine air, noise, water and ecology measurements within a defined radius of the site."],
 misconceptions=["One day of measurements is not a baseline.","Secondary data alone are rarely sufficient for site-specific assessment."],
 revision=["Baseline = reference for prediction.","DO low + BOD high = organic pollution.","Select stations by wind, receptors, land use."],
 cards=[("Why baseline?","To describe existing conditions and give a reference to measure project impacts."),("What does BOD indicate?","Amount of biodegradable organic pollution."),("1 mg/L equals?","1 g/m³."),("Core vs buffer zone?","Core: project footprint; buffer: surrounding area of influence.")],
 refs=["NPTEL 105107210 Week 5 lectures.","CPCB National Ambient Air Quality Standards (public)."],
))

W.append(dict(
 id=6, title="Noise, Air and Water Pollution Modelling",
 overview="Prediction uses mathematical models. For noise, logarithmic decibel arithmetic and distance attenuation; for air, emission factors and dispersion models; for water, load and runoff estimation.",
 objectives=["Add and average decibel levels correctly.","Compute noise attenuation with distance.","Estimate vehicle emissions using emission factors.","Apply a simple Gaussian plume expression."],
 notes=[
  ("Noise basics", ["Sound level in decibels: L = 10 log10(I/I0) = 20 log10(p/p0) with p0 = 20 µPa. Decibels are logarithmic, so they cannot be added arithmetically.","Adding sources: L = 10 log10(Σ 10^(Li/10)). Two equal sources add 3 dB. A ten-fold increase in intensity adds 10 dB.","Equivalent continuous level Leq represents a fluctuating noise as a steady level with the same energy over time T: Leq = 10 log10[(1/T) Σ ti·10^(Li/10)]."]),
  ("Noise propagation", ["Point source: level drops 6 dB per doubling of distance (20 log r). Line source (steady traffic): 3 dB per doubling (10 log r). Barriers, ground absorption and air absorption give further reduction."]),
  ("Air pollution modelling", ["Emissions are estimated as activity × emission factor (e.g. vehicle-km × g/km). Dispersion models (Gaussian plume; line-source models such as CALINE and others) convert emissions to ambient concentrations using wind speed, stability class and geometry.","Gaussian plume (ground-level source, centreline): C = Q / (π u σy σz)."]),
  ("Water pollution modelling", ["Runoff pollutant load = concentration × runoff volume; receiving-water models use mixing and dissolved-oxygen balance (e.g. Streeter–Phelps concept) to predict downstream quality."]),
 ],
 definitions=[("Decibel (dB)","Logarithmic unit for sound level relative to a reference."),("Leq","Equivalent continuous sound level over a period."),("Emission factor","Mass of pollutant emitted per unit activity (e.g. g/km)."),("Gaussian plume","Dispersion model assuming normal distribution of concentration in the crosswind and vertical directions."),("Stability class","Classification of atmospheric turbulence affecting dispersion.")],
 concepts=["dB are logarithmic.","Distance attenuation differs for point and line sources.","Dispersion depends on wind, stability and source geometry.","Model validation against measurements is needed."],
 formulas=[("Sound level (pressure)","L = 20 log10(p / p0), p0 = 20 µPa","dB"),("Adding levels","L = 10 log10 Σ 10^(Li/10)","dB"),("Point source","L2 = L1 − 20 log10(r2/r1)","dB"),("Line source","L2 = L1 − 10 log10(r2/r1)","dB"),("Leq","10 log10[Σ (ti/T) 10^(Li/10)]","dB"),("Gaussian plume (ground-level source)","C = Q / (π u σy σz)","g/m³ (Q g/s, u m/s, σ m)")],
 example=dict(q="Two identical machines each produce 70 dB at a receptor. What is the combined level?",steps=["L = 10 log10(10^7 + 10^7) = 10 log10(2×10^7) = 70 + 3.01 = 73.0 dB."],ans="≈ 73 dB (not 140 dB)."),
 applications=["Predicting noise at homes next to a new highway.","Siting noise barriers.","Estimating roadside NO2 or PM from traffic."],
 cases=["Airport EIAs use noise contours (e.g. Leq or day–night metrics) to show the affected area around runways."],
 misconceptions=["Doubling noise sources does not double the dB value (adds 3 dB).","A line source attenuates more slowly with distance than a point source."],
 revision=["Equal sources: +3 dB per doubling of count.","Point: −6 dB/doubling distance; line: −3 dB.","C = Q/(π u σy σz) for ground-level source."],
 cards=[("Two equal 60 dB sources combined?","63 dB (+3 dB)."),("Point-source attenuation per distance doubling?","6 dB."),("Line-source attenuation per distance doubling?","3 dB."),("What is Leq?","Steady level with the same acoustic energy as the fluctuating noise over the period.")],
 refs=["NPTEL 105107210 Week 6 lectures."],
))
