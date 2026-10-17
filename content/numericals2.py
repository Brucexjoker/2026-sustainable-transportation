"""More numericals. Answers computed in code; tests recompute independently."""
import math
log = math.log10
N2 = [
(6,"Noise","medium","Sources of 65 dB, 65 dB and 68 dB act together","Combined level","L = 10 log10 Σ 10^(Li/10)",["10^6.5 = 3.162×10^6 (twice) = 6.325×10^6","10^6.8 = 6.310×10^6","Sum = 1.2634×10^7","L = 10 log10(1.2634×10^7)"],"dB",lambda:10*log(2*10**6.5+10**6.8),0.1,"Add energies, not decibels."),
(6,"Noise","easy","Point source gives 90 dB at 5 m","Level at 50 m","L2 = L1 − 20 log10(r2/r1)",["r2/r1 = 10","20 log 10 = 20","L2 = 90 − 20"],"dB",lambda:90-20*log(10),0.1,"A tenfold distance drops a point source by 20 dB."),
(6,"Noise","medium","Traffic line source gives 80 dB at 10 m","Level at 40 m","L2 = L1 − 10 log10(r2/r1)",["r2/r1 = 4","10 log 4 = 6.02","L2 = 80 − 6.02"],"dB",lambda:80-10*log(4),0.1,"Line source: 3 dB per doubling."),
(6,"Noise","medium","RMS sound pressure 2 Pa, p0 = 20 µPa","Sound pressure level","L = 20 log10(p/p0)",["p/p0 = 2/(20×10^-6) = 10^5","L = 20 × 5"],"dB",lambda:20*log(2/20e-6),0.1,"A 10^5 pressure ratio gives 100 dB."),
(6,"Noise","hard","70 dB for 25% of the time and 50 dB for 75% of the time","Leq","Leq = 10 log10[Σ (ti/T) 10^(Li/10)]",["0.25×10^7 = 2.5×10^6","0.75×10^5 = 7.5×10^4","Sum = 2.575×10^6","Leq = 10 log10(2.575×10^6)"],"dB",lambda:10*log(0.25*1e7+0.75*1e5),0.1,"Short loud periods dominate Leq."),
(6,"Air dispersion","hard","Ground-level source Q = 5 g/s, u = 5 m/s, σy = 40 m, σz = 20 m","Ground-level centreline concentration","C = Q /(π u σy σz)",["π × 5 × 40 × 20 = 12,566.4","C = 5 / 12,566.4 = 3.979×10^-4 g/m³","× 10^6 µg/g"],"µg/m³",lambda:5/(math.pi*5*40*20)*1e6,0.5,"Higher wind speed and larger dispersion coefficients reduce concentration."),
(7,"Emission estimate","easy","2000 vehicles/day, 15 km road, NOx EF 0.5 g/km","Daily NOx","E = N × L × EF",["2000 × 15 × 0.5 = 15,000 g","÷ 1000"],"kg/day",lambda:2000*15*0.5/1000,0.01,"Convert g to kg."),
(7,"Fuel emissions","easy","250 L petrol at 2.31 kg CO2/L (typical value)","CO2 emitted","CO2 = fuel × EF",["250 × 2.31"],"kg",lambda:250*2.31,0.01,"Fuel-based method."),
(3,"Mode share","easy","90,000 of 240,000 daily trips are by public transport","Public transport share","Share = PT trips / total × 100",["90,000 / 240,000 × 100"],"%",lambda:90000/240000*100,0.01,"Mode share is a basic sustainability indicator."),
(9,"CBA","medium","Benefit of 120 (crore) arrives after 1 year; cost 100 (crore) now; r = 10%","NPV","NPV = B/(1+r) − C",["PV of benefit = 120/1.10 = 109.09","NPV = 109.09 − 100"],"crore",lambda:120/1.10-100,0.01,"Discounting reduces future benefits."),
(12,"LCA","medium","Car lifecycle 40 t CO2e over 200,000 km at 1.5 occupants","g CO2e per pkm","Impact/FU = total / pkm",["pkm = 200,000 × 1.5 = 300,000","40 t = 4×10^7 g","4×10^7 / 3×10^5"],"g CO2e/pkm",lambda:40e6/(200000*1.5),0.1,"Compare with the bus value of 25 g/pkm."),
(12,"MFA","medium","Input 500 t aggregate; outputs: 430 t in road and 25 t waste","Stock change","ΔStock = In − Out",["Out = 430 + 25 = 455","500 − 455"],"t",lambda:500-(430+25),0.01,"Material not leaving the system is stored."),
(9,"Decision analysis","easy","Weights 0.5,0.3,0.2; Option A scores 8,6,7","Weighted score of A","S = Σ wi si",["0.5×8 = 4.0","0.3×6 = 1.8","0.2×7 = 1.4"],"points",lambda:0.5*8+0.3*6+0.2*7,0.01,"Compare with option B (7.3)."),
(5,"Water load","medium","BOD 25 mg/L in 8000 m³ of effluent","BOD load","Load = C × V",["25 g/m³ × 8000 m³ = 200,000 g"],"kg",lambda:25*8000/1000,0.01,"1 mg/L = 1 g/m³."),
(2,"Land use","medium","Plot 1500 m², FAR 1.8, 3 floors","Ground coverage","GC = footprint / plot × 100",["Built-up = 1.8 × 1500 = 2700 m²","Footprint = 2700/3 = 900 m²","900/1500 × 100"],"%",lambda:(1.8*1500/3)/1500*100,0.1,"Footprint equals built-up area divided by floors."),
]
