"""Numerical problems. Each answer is COMPUTED in code (calc lambda) and cross-checked against the stated answer by tests."""
import math
log = math.log10

# (week, topic, difficulty, given, required, formula, steps[], unit, calc(), tolerance, explanation)
N = [
(6,"Noise","easy","Two identical sources, each 70 dB at the receptor","Combined level","L = 10 log10(Σ 10^(Li/10))",["10^7 + 10^7 = 2×10^7","L = 10 log10(2×10^7) = 70 + 3.01"],"dB",lambda:10*log(2e7),0.1,"Doubling acoustic energy adds about 3 dB."),
(6,"Noise","medium","Three equal sources of 60 dB each","Combined level","L = 60 + 10 log10(3)",["10 log10 3 = 4.77","L = 60 + 4.77"],"dB",lambda:60+10*log(3),0.1,"Equal sources: L = Li + 10 log N."),
(6,"Noise","medium","Point source measured 80 dB at 10 m","Level at 40 m","L2 = L1 − 20 log10(r2/r1)",["r2/r1 = 4","20 log 4 = 12.04","L2 = 80 − 12.04"],"dB",lambda:80-20*log(4),0.1,"Inverse-square spreading: 6 dB per distance doubling."),
(6,"Noise","medium","Traffic line source, 75 dB at 15 m","Level at 60 m","L2 = L1 − 10 log10(r2/r1)",["r2/r1 = 4","10 log 4 = 6.02","L2 = 75 − 6.02"],"dB",lambda:75-10*log(4),0.1,"Line source: 3 dB per doubling."),
(6,"Noise","hard","Noise is 60 dB for half the period and 70 dB for the other half","Leq","Leq = 10 log10[Σ (ti/T) 10^(Li/10)]",["0.5×10^6 + 0.5×10^7 = 5.5×10^6","Leq = 10 log10(5.5×10^6)"],"dB",lambda:10*log(0.5*1e6+0.5*1e7),0.1,"The loud period dominates the energy average."),
(6,"Noise","medium","RMS sound pressure 0.2 Pa, reference 20 µPa","Sound pressure level","L = 20 log10(p/p0)",["p/p0 = 0.2 / 20×10^-6 = 10^4","L = 20 × 4"],"dB",lambda:20*log(0.2/20e-6),0.1,"A 10^4 pressure ratio is 80 dB."),
(6,"Air dispersion","hard","Ground-level source Q = 2 g/s, u = 4 m/s, σy = 30 m, σz = 15 m","Centreline ground concentration (µg/m³)","C = Q /(π u σy σz)",["π·4·30·15 = 5654.9","C = 2/5654.9 = 3.537×10^-4 g/m³","×10^6 µg/g"],"µg/m³",lambda:2/(math.pi*4*30*15)*1e6,0.5,"Source and receptor at ground level, so the height term is 1."),
(7,"Emission estimate","easy","5000 vehicles/day, 12 km road, CO EF 1.2 g/km","Daily CO (kg)","E = N × L × EF",["5000 × 12 × 1.2 = 72,000 g","÷ 1000"],"kg/day",lambda:5000*12*1.2/1000,0.01,"Always convert grams to kilograms at the end."),
(7,"Fuel emissions","easy","1000 L diesel, 2.68 kg CO2/L (approx. typical value)","CO2 emitted (kg)","CO2 = fuel × EF",["1000 × 2.68"],"kg",lambda:1000*2.68,0.01,"Fuel-based method; EF is an assumed typical value."),
(7,"Mode shift","medium","20,000 trips × 8 km shifted from car (150 g/pkm) to metro (30 g/pkm)","Daily CO2 saving (t)","Saving = pkm × (EF_car − EF_metro)",["pkm = 160,000","160,000 × 120 g = 19.2×10^6 g"],"t/day",lambda:20000*8*(150-30)/1e6,0.01,"1 t = 10^6 g."),
(7,"Energy efficiency","medium","Bus 40 L/100 km with 40 passengers; car 8 L/100 km with 2 occupants","Fuel per pkm: bus vs car (mL/pkm), ratio car/bus","Fuel per pkm = (L/km)/occupancy",["Bus: 0.40/40 = 0.010 L/pkm = 10 mL","Car: 0.08/2 = 0.040 L/pkm = 40 mL","Ratio = 4"],"×  (car/bus)",lambda:(0.08/2)/(0.40/40),0.01,"The bus is four times more fuel-efficient per passenger-km at this occupancy."),
(7,"Emission per pkm","medium","Diesel bus 40 L/100 km (2.68 kg/L), 50 passengers","g CO2 per pkm","(L/km × EF)/occupancy",["0.40 × 2.68 = 1.072 kg/km","1.072/50 = 0.02144 kg"],"g/pkm",lambda:0.40*2.68/50*1000,0.1,"Full buses are very efficient per passenger."),
(7,"Emission per pkm","medium","Petrol car 8 L/100 km (2.31 kg/L), 1.5 occupants","g CO2 per pkm","(L/km × EF)/occupancy",["0.08 × 2.31 = 0.1848 kg/km","0.1848/1.5 = 0.1232 kg"],"g/pkm",lambda:0.08*2.31/1.5*1000,0.1,"Compare with the bus result."),
(9,"Decision analysis","medium","Weights 0.5,0.3,0.2; Option B scores 6,9,8","Weighted score of B","S = Σ wi si",["0.5×6 = 3.0","0.3×9 = 2.7","0.2×8 = 1.6"],"points",lambda:0.5*6+0.3*9+0.2*8,0.01,"Option A scores 7.2 so B ranks first, narrowly."),
(11,"EV emissions","medium","EV 15 kWh/100 km, grid 0.8 kg CO2/kWh","g CO2/km","EF = kWh/km × grid EF",["0.15 × 0.8 = 0.12 kg/km"],"g/km",lambda:0.15*0.8*1000,0.1,"Only grid emissions counted (no manufacturing)."),
(12,"LCA","medium","Bus lifecycle 600 t CO2e; lifetime 800,000 km; 30 passengers average","g CO2e per pkm","Impact/FU = total / total pkm",["pkm = 800,000 × 30 = 2.4×10^7","600 t = 6×10^8 g","6×10^8 / 2.4×10^7"],"g CO2e/pkm",lambda:600e6/(800000*30),0.1,"Functional unit: 1 passenger-km."),
(12,"MFA","easy","Input 100 t; outputs 70 t product and 20 t waste","Stock change","ΔStock = Input − Outputs",["100 − (70 + 20)"],"t",lambda:100-(70+20),0.01,"Positive: material accumulates."),
(2,"Land use","easy","Plot 1000 m², FAR 2.0, ground coverage 40%","Number of floors","Floors = FAR/(GC/100)",["Built-up = 2000 m²","Footprint = 400 m²","2000/400"],"floors",lambda:2.0/0.40,0.01,"Max built-up area = FAR × plot area."),
(5,"Water load","easy","Runoff 5000 m³, TSS 40 mg/L","TSS load (kg)","Load = C×V (1 mg/L = 1 g/m³)",["40 g/m³ × 5000 m³ = 200,000 g"],"kg",lambda:40*5000/1000,0.01,"Unit consistency is the key step."),
(9,"CBA","easy","PV benefits 450, PV costs 360 (crore)","BCR","BCR = PVB/PVC",["450/360"],"—",lambda:450/360,0.01,"BCR>1 is economically attractive; NPV = 90 crore."),
]
