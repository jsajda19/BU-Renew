import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from intervaldata import tot_energy
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
    jan = jan + tot_energy[i]
    march = march + tot_energy[i+31+28]
    may = may + tot_energy[i+31+28+31+30]
    july = july + tot_energy[i+31+28+31+30+31+30]
    aug = aug + tot_energy[i+31+28+31+30+31+30+31]
    octob = octob + tot_energy[i+31+28+31+30+31+30+31+31+30]
    dec = dec + tot_energy[i+31+28+31+30+31+30+31+31+30+31+30]

for i in range(28):
    feb = feb + tot_energy[i+31]
    
for i in range(30):
    april = april + tot_energy[i+31+28+31]
    june = june + tot_energy[i+31+28+31+30+31]
    sep = sep + tot_energy[i+31+28+31+30+31+30+31+31]
    nov = nov + tot_energy[i+31+28+31+30+31+30+31+31+30+31]
    
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