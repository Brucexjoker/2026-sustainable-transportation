"""Weeks 7-12 study material."""

W = []

W.append(dict(
 id=7, title="Modelling of Impacts and Scenario-based Analysis",
 overview="Impacts depend on future conditions, so assessments compare scenarios: business-as-usual (BAU) versus policy or project alternatives, using projections of traffic, fleet, fuel and emissions.",
 objectives=["Define scenarios and the BAU baseline.","Build a simple emission inventory under alternative scenarios.","Perform sensitivity analysis.","Interpret uncertainty in predictions."],
 notes=[
  ("Scenario analysis", ["A scenario is a consistent description of a possible future. Typical set: BAU (no new policy), project scenario, and policy-intervention scenarios (e.g. mode shift, cleaner fuel, EV adoption).","Impact of a measure = emissions (BAU) − emissions (measure)."]),
  ("Emission inventory (bottom-up)", ["Total emissions = Σ over vehicle categories of (number of vehicles × annual distance × emission factor). Fuel-based method: emissions = fuel consumed × fuel emission factor (e.g. ~2.3 kg CO2/L petrol and ~2.7 kg CO2/L diesel are commonly used approximate values)."]),
  ("Sensitivity and uncertainty", ["Sensitivity analysis varies one input (e.g. growth rate, emission factor, load factor) to see its effect on outputs. Uncertainty arises from data quality, model structure and future behaviour; results should be presented as ranges where possible."]),
 ],
 definitions=[("BAU","Business-as-usual scenario assuming existing trends and policies continue."),("Scenario","Plausible, internally consistent description of a future situation."),("Emission inventory","Quantified list of emissions by source and period."),("Sensitivity analysis","Study of how output changes with variation in an input."),("Load factor / occupancy","Average passengers per vehicle (or load per capacity).")],
 concepts=["Compare against BAU, not against today.","Per-passenger-km makes modes comparable.","Mode shift reduces emissions only if load factors are adequate.","Rebound effects may offset savings."],
 formulas=[("Fuel-based CO2","CO2 = Fuel (L) × EF (kg/L)","kg"),("Per passenger-km","Emission per pkm = (EF per vehicle-km) / occupancy","g/pkm"),("Mode shift saving","Saving = pkm shifted × (EF_old − EF_new)","g or kg")],
 example=dict(q="20,000 daily car trips of 8 km are shifted to metro. Car emits 150 g CO2/pkm and metro 30 g CO2/pkm. Find daily CO2 saving.",steps=["Shifted pkm = 20,000 × 8 = 160,000 pkm.","Saving = 160,000 × (150 − 30) = 19,200,000 g = 19.2 t."],ans="19.2 tonnes CO2 per day."),
 applications=["Comparing BRT versus metro options by lifecycle emissions per pkm.","Estimating benefits of low-emission zones."],
 cases=["City emission inventories commonly show road transport as a leading contributor; scenario studies test effects of fleet renewal and public-transport expansion."],
 misconceptions=["Impact is not measured against current conditions alone.","A cleaner vehicle with very low occupancy may not be better per passenger-km."],
 revision=["Impact = BAU − intervention.","Emissions = activity × EF.","Use sensitivity analysis to test assumptions."],
 cards=[("What is BAU?","Business-as-usual scenario; the reference for comparing interventions."),("Per-pkm emissions formula?","EF per vehicle-km ÷ occupancy."),("Purpose of sensitivity analysis?","To see which inputs most affect results."),("Why present ranges?","Because predictions have uncertainty.")],
 refs=["NPTEL 105107210 Week 7 lectures."],
))

W.append(dict(
 id=8, title="Assessment of Potential Project Impacts, including Indirect, Cumulative and Synergistic Impacts",
 overview="Beyond direct effects, projects cause indirect (induced) effects, cumulative effects (together with other projects) and synergistic effects (combined effect greater than the sum of parts). Methods are needed to identify and evaluate them.",
 objectives=["Define direct, indirect, cumulative and synergistic impacts.","Describe impact identification methods.","Evaluate impact significance (magnitude, extent, duration, reversibility).","Explain why cumulative assessment is needed."],
 notes=[
  ("Types of impact", ["Direct: caused by the project itself at the same place and time (e.g. land taken). Indirect: later or farther consequences (e.g. new development along a highway). Cumulative: incremental effects added to past, present and future actions. Synergistic: interaction where combined effect exceeds the sum (e.g. noise plus air pollution on health)."]),
  ("Identification methods", ["Checklists (simple lists of impacts), matrices (e.g. Leopold matrix scoring magnitude and importance of actions against environmental components), networks (cause–effect chains for secondary impacts), overlays/GIS mapping, expert judgement (ad hoc), and modelling."]),
  ("Significance", ["Significance depends on magnitude, spatial extent, duration, frequency, reversibility, the sensitivity of receptors and compliance with standards or legal limits."]),
 ],
 definitions=[("Direct impact","Impact caused directly by project activities."),("Indirect impact","Secondary effect induced by the project."),("Cumulative impact","Impact resulting from incremental effect combined with other actions."),("Synergistic impact","Combined effect greater than the sum of the separate effects."),("Leopold matrix","Matrix of project actions versus environmental factors, scored for magnitude and importance.")],
 concepts=["Networks are best for indirect impacts.","Checklists are quick but do not show interactions.","GIS overlay supports spatial analysis.","Irreversible impacts get higher significance."],
 formulas=[("Weighted impact score","Score = Σ (wi × si)","dimensionless"),("Leopold cell","Cell = Magnitude (1–10) and Importance (1–10)","—")],
 example=dict(q="Option A scores 8, 6, 7 and Option B scores 6, 9, 8 on three criteria weighted 0.5, 0.3, 0.2. Which is higher?",steps=["A = 0.5×8 + 0.3×6 + 0.2×7 = 4.0 + 1.8 + 1.4 = 7.2.","B = 0.5×6 + 0.3×9 + 0.2×8 = 3.0 + 2.7 + 1.6 = 7.3."],ans="B (7.3 vs 7.2), though the margin is small."),
 applications=["Assessing induced urban sprawl from a new expressway.","Cumulative impacts of multiple projects in one river basin."],
 cases=["Corridor developments in ecologically sensitive regions require cumulative assessments with other infrastructure."],
 misconceptions=["Indirect impacts are not necessarily smaller than direct ones.","Cumulative does not mean only the project's own impacts over time."],
 revision=["Direct/indirect/cumulative/synergistic.","Networks → indirect; matrix → interactions between actions and factors.","Significance = magnitude + extent + duration + reversibility."],
 cards=[("Synergistic impact?","Combined effect greater than the sum of parts."),("Best method for secondary effects?","Network (cause–effect chain)."),("Leopold matrix is a ...?","Matrix scoring project actions vs environmental factors."),("Why cumulative assessment?","Single-project assessments can miss combined effects.")],
 refs=["NPTEL 105107210 Week 8 lectures."],
))

W.append(dict(
 id=9, title="Decision Support Systems for EIA of Transport Infrastructure",
 overview="Choosing among alignments or modes involves conflicting objectives. Decision support systems (DSS) combine data, models and multi-criteria methods so decisions are transparent and repeatable.",
 objectives=["Describe components of a DSS.","Apply multi-criteria decision analysis (MCDA).","Explain the role of GIS in alignment selection.","Understand cost–benefit analysis and its limits."],
 notes=[
  ("DSS components", ["A DSS has a database (spatial and non-spatial), a model base (prediction and evaluation models) and a user interface that lets decision-makers test alternatives."]),
  ("Multi-criteria analysis", ["Steps: define alternatives, select criteria, assign weights, score each alternative, normalise, aggregate (weighted sum) and test sensitivity. The Analytic Hierarchy Process (AHP) derives weights from pairwise comparisons."]),
  ("GIS", ["Geographic Information Systems overlay layers (land use, forest, rivers, settlements, soil) to find least-impact corridors and visualise results."]),
  ("Cost–benefit analysis", ["CBA converts impacts into monetary values and compares discounted benefits and costs (NPV, BCR). Some environmental values are hard to monetise, so CBA is often combined with MCDA."]),
 ],
 definitions=[("DSS","Interactive system combining data, models and interface to support decisions."),("MCDA","Multi-criteria decision analysis."),("AHP","Analytic Hierarchy Process using pairwise comparison to derive weights."),("GIS","System for capturing, analysing and mapping spatial data."),("BCR","Benefit–cost ratio.")],
 concepts=["Transparency and stakeholder participation.","Weights express priorities and are subjective; test sensitivity.","Non-monetary impacts can still be scored.","Do-nothing is an alternative."],
 formulas=[("Weighted sum","S = Σ wi si, Σ wi = 1","—"),("BCR","BCR = PV(benefits) / PV(costs)","—"),("NPV","NPV = Σ (Bt − Ct)/(1+r)^t","currency")],
 example=dict(q="PV of benefits is 450 crore and PV of costs is 360 crore. Find BCR and NPV.",steps=["BCR = 450/360 = 1.25.","NPV = 450 − 360 = 90 crore."],ans="BCR 1.25; NPV 90 crore (project economically attractive)."),
 applications=["Selecting among highway alignments using GIS overlays.","Prioritising metro vs BRT using MCDA."],
 cases=["Route selection studies for railways/highways commonly use GIS-based least-cost path analysis through land-use layers."],
 misconceptions=["A BCR > 1 does not guarantee the project is environmentally acceptable.","Weights are not objective facts."],
 revision=["DSS = data + models + interface.","MCDA steps; AHP weights.","BCR>1 ⇒ benefits exceed costs."],
 cards=[("DSS parts?","Database, model base, user interface."),("AHP is used for?","Deriving criteria weights via pairwise comparison."),("BCR>1 means?","Discounted benefits exceed costs."),("Why sensitivity on weights?","Weights are subjective and can change the ranking.")],
 refs=["NPTEL 105107210 Week 9 lectures."],
))

W.append(dict(
 id=10, title="Abatement Measures",
 overview="Abatement (mitigation) measures reduce adverse impacts. They follow the mitigation hierarchy: avoid, minimise, restore and, as a last resort, offset or compensate.",
 objectives=["Apply the mitigation hierarchy.","Select abatement measures for noise, air, water and ecology.","Explain vehicle, fuel and traffic management measures.","Understand monitoring and EMP implementation."],
 notes=[
  ("Mitigation hierarchy", ["Avoid (change alignment/design), Minimise (reduce scale and intensity), Restore/Rehabilitate (after construction), Compensate/Offset (compensatory afforestation, resettlement and rehabilitation)."]),
  ("Noise", ["At source: quieter vehicles, smooth surfaces, speed control. On path: barriers, earth berms, distance, vegetation (limited effect). At receiver: insulation, window glazing, land-use buffer zones."]),
  ("Air", ["Cleaner fuels (CNG, BS-VI), catalytic converters, inspection and maintenance (PUC), traffic management, dust suppression in construction (water sprinkling, covering material), green belts as supplementary measure."]),
  ("Water, soil and ecology", ["Silt traps, sedimentation basins, oil–grease separators, rainwater harvesting, slope stabilisation, bio-engineering, wildlife crossings and careful timing of work."]),
  ("Monitoring", ["The EMP assigns responsibilities, budget and schedule for monitoring parameters during construction and operation, with corrective action if standards are exceeded."]),
 ],
 definitions=[("Mitigation","Actions to reduce adverse impacts."),("Compensatory afforestation","Planting trees to offset forest area diverted."),("PUC","Pollution Under Control certificate for vehicles."),("Noise barrier","Structure that blocks direct sound path between source and receiver."),("R&R","Resettlement and rehabilitation of affected people.")],
 concepts=["Prevent at source first.","Barriers help only when they break the line of sight and are tall/long enough.","Vegetation provides small noise reduction but visual and air benefits.","Monitoring verifies effectiveness."],
 formulas=[("Barrier insertion loss (concept)","Insertion loss = L_before − L_after","dB"),("Percent reduction","Reduction (%) = (E_before − E_after)/E_before × 100","%")],
 example=dict(q="A measure reduces PM emissions from 250 kg/day to 180 kg/day. Find percent reduction.",steps=["Reduction = 70 kg/day.","Percent = 70/250 × 100 = 28%."],ans="28%."),
 applications=["Noise barriers along urban elevated corridors.","Sprinkling to control construction dust.","Green belts and wildlife underpasses."],
 cases=["Delhi's shift of public buses to CNG after Supreme Court directions is a widely cited example of a fuel-based abatement policy."],
 misconceptions=["Trees alone do not solve road-noise problems.","Compensation is the last step of the hierarchy, not the first."],
 revision=["Avoid → minimise → restore → offset.","Source > path > receiver for noise control.","EMP = measures + responsibility + budget + monitoring."],
 cards=[("Mitigation hierarchy?","Avoid, minimise, restore, offset/compensate."),("Noise control priority?","At the source first, then path, then receiver."),("What is a PUC?","Pollution Under Control certificate."),("What is compensatory afforestation?","Planting to offset forest land diverted for a project.")],
 refs=["NPTEL 105107210 Week 10 lectures."],
))

W.append(dict(
 id=11, title="Sustainable Transportation Systems",
 overview="Sustainable transport meets present mobility needs without compromising the environment, economy and social equity of future generations. It uses public transport, non-motorised transport (NMT), cleaner vehicles and compact land use.",
 objectives=["Define sustainable transportation and its three pillars.","Explain mass rapid transit (metro, BRT) and NMT roles.","Discuss alternative fuels and EVs.","Use indicators to measure sustainability."],
 notes=[
  ("Concept", ["Sustainability has environmental, economic and social pillars. Sustainable transport minimises emissions, energy use, land take, noise and accidents while providing affordable and equitable access."]),
  ("Mass rapid transit", ["Metro rail has high capacity, electric traction (no tailpipe emissions, though upstream power emissions apply) and low land use per passenger. Bus Rapid Transit (BRT) provides dedicated lanes, level boarding and off-board fare collection at lower cost and faster implementation."]),
  ("NMT and last mile", ["Walking and cycling are zero-emission and healthy; they require safe footpaths, cycle tracks, crossings and traffic calming. Public bike sharing and feeder services solve the first/last-mile problem."]),
  ("Alternative fuels and EVs", ["CNG, LPG, biofuels (ethanol, biodiesel), electricity and hydrogen. EV well-to-wheel emissions depend on the electricity mix; with a cleaner grid, EVs offer larger benefits. Other emerging technology, e.g. Hyperloop, remains largely experimental."]),
  ("Indicators", ["Examples: public transport mode share, NMT share, emissions per capita, fatalities per 100,000 population, modal accessibility, average trip length, share of clean vehicles."]),
 ],
 definitions=[("Sustainable transport","Mobility that is environmentally sound, economically viable and socially equitable."),("BRT","Bus Rapid Transit: high-quality bus-based system with dedicated lanes."),("NMT","Non-motorised transport: walking and cycling."),("Well-to-wheel","Emissions from fuel production through vehicle use."),("First/last mile","Short trip between origin/destination and a transit station.")],
 concepts=["Three pillars.","Modal hierarchy.","Tailpipe vs lifecycle emissions.","Equity: affordability and access for all."],
 formulas=[("Emission per km (EV)","EF = Energy use (kWh/km) × Grid EF (kg/kWh)","kg/km"),("Emission per km (fuel vehicle)","EF = Fuel use (L/km) × fuel EF (kg/L)","kg/km")],
 example=dict(q="An EV uses 0.15 kWh/km and grid factor is 0.8 kg CO2/kWh. A petrol car uses 0.06 L/km at 2.31 kg CO2/L. Compare.",steps=["EV = 0.15 × 0.8 = 0.12 kg/km = 120 g/km.","Petrol = 0.06 × 2.31 = 0.1386 kg/km ≈ 138.6 g/km."],ans="EV 120 g/km vs petrol ≈ 138.6 g/km: EV is about 13% lower on this grid."),
 applications=["Metro and BRT corridors with feeder buses.","City cycle-lane networks.","Electric bus fleets."],
 cases=["Bogotá's TransMilenio and Ahmedabad's Janmarg are often cited BRT examples; Delhi Metro is a major Indian metro example (general references)."],
 misconceptions=["EVs are not zero-emission over their life cycle.","BRT is not just 'a bus lane': it needs stations, fare system and priority."],
 revision=["Three pillars; modal hierarchy.","EV benefit depends on grid mix.","BRT vs metro: cost, capacity, speed of delivery."],
 cards=[("Three pillars of sustainability?","Environmental, economic, social."),("BRT?","Bus Rapid Transit: dedicated lanes, high-quality stations."),("Why is EV benefit variable?","Depends on electricity generation mix."),("NMT?","Walking and cycling.")],
 refs=["NPTEL 105107210 Week 11 lectures."],
))

W.append(dict(
 id=12, title="Case Studies of Highway, Railway and Airport Projects; OpenLCA and STAN",
 overview="The final week applies EIA to highway, railway and airport projects and introduces tools: openLCA for life cycle assessment and STAN for material (substance) flow analysis.",
 objectives=["Summarise typical EIA concerns of highway, railway and airport projects.","Explain the four phases of LCA (ISO 14040).","Define goal, scope, functional unit and system boundary.","Explain mass-balance principle used in MFA/STAN."],
 notes=[
  ("Highways, railways, airports", ["Highways: land acquisition, forest diversion, severance, air and noise along the corridor, runoff and accidents. Railways: land, noise and vibration, electrification benefits, level crossings. Airports: noise contours, air quality, bird hazard, land take, induced development, water use."]),
  ("Life Cycle Assessment", ["LCA (ISO 14040/14044) evaluates environmental impacts across the whole life cycle. Phases: (1) Goal and scope definition including functional unit and system boundary, (2) Life Cycle Inventory (LCI), (3) Life Cycle Impact Assessment (LCIA) such as global warming potential, (4) Interpretation.","openLCA is a free, open-source software for modelling product systems and calculating LCI and LCIA using databases."]),
  ("Material / substance flow analysis", ["MFA tracks flows and stocks of materials through a system with the mass-balance principle: Inputs = Outputs + Stock change.","STAN (subSTance flow ANalysis) is free software from TU Wien for MFA that supports data reconciliation with uncertainty."]),
 ],
 definitions=[("LCA","Life Cycle Assessment: compilation and evaluation of inputs, outputs and impacts across a product's life cycle."),("Functional unit","Quantified performance of a system used as a reference unit, e.g. 1 passenger-km."),("System boundary","Defines which processes are included in the LCA."),("LCI","Life Cycle Inventory: inputs and outputs of all processes."),("MFA","Material Flow Analysis."),("GWP","Global Warming Potential, expressed in CO2-equivalents.")],
 concepts=["Cradle-to-grave vs cradle-to-gate.","Functional unit must be comparable between alternatives.","Mass balance in MFA.","Interpretation includes sensitivity and completeness checks."],
 formulas=[("LCA result per functional unit","Impact per FU = Total life-cycle impact / Total functional units","e.g. g CO2e/pkm"),("Mass balance","Input = Output + ΔStock","t or kg")],
 example=dict(q="A bus has life-cycle emissions of 600 t CO2e over 800,000 km with average 30 passengers. Find g CO2e per passenger-km.",steps=["Total pkm = 800,000 × 30 = 24,000,000.","600 t = 6.0×10^8 g.","Per pkm = 6.0×10^8 / 2.4×10^7 = 25 g."],ans="25 g CO2e per passenger-km."),
 applications=["Comparing bus, metro and car alternatives per pkm.","Tracking steel, cement and aggregates in infrastructure construction."],
 cases=["EIA reports for highway/rail/airport projects are public documents often available on regulator websites and show how baseline, prediction and EMP are presented."],
 misconceptions=["LCA is not just carbon accounting: other impact categories exist.","MFA input and output need not balance if material accumulates as stock."],
 revision=["LCA: goal/scope → LCI → LCIA → interpretation.","Functional unit enables fair comparison.","Mass balance: In = Out + ΔStock."],
 cards=[("Four phases of LCA?","Goal & scope, inventory (LCI), impact assessment (LCIA), interpretation."),("openLCA is used for?","LCA modelling and calculation (free, open-source)."),("STAN is used for?","Material/substance flow analysis with data reconciliation."),("Functional unit example?","1 passenger-km.")],
 refs=["NPTEL 105107210 Week 12 lectures.","ISO 14040:2006 and 14044:2006 (standards).","openLCA (GreenDelta) and STAN (TU Wien) software documentation."],
))
