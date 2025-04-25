import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from intervalproduction import energyproduced
warnings.filterwarnings("ignore", category=FutureWarning)

jan = 0
feb = 0
march = 0
april = 0
may = 0
june = 0
july = 0
aug = 0
sep = 0
octob = 0
nov = 0
dec = 0

for i in range(31):
    jan = jan + energyproduced[i]
    march = march + energyproduced[i+31+28]
    may = may + energyproduced[i+31+28+31+30]
    july = july + energyproduced[i+31+28+31+30+31+30]
    aug = aug + energyproduced[i+31+28+31+30+31+30+31]
    octob = octob + energyproduced[i+31+28+31+30+31+30+31+31+30]
    dec = dec + energyproduced[i+31+28+31+30+31+30+31+31+30+31+30]

for i in range(28):
    feb = feb + energyproduced[i+31]
    
for i in range(30):
    april = april + energyproduced[i+31+28+31]
    june = june + energyproduced[i+31+28+31+30+31]
    sep = sep + energyproduced[i+31+28+31+30+31+30+31+31]
    nov = nov + energyproduced[i+31+28+31+30+31+30+31+31+30+31]
    
print(jan)
print(feb)
print(march)
print(april)
print(may)
print(june)
print(july)
print(aug)
print(sep)
print(octob)
print(nov)
print(dec)

print("total")
print(jan+feb+march+april+may+june+july+aug+sep+octob+nov+dec)