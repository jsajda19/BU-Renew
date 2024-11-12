import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from intervalpower import tot_power
from powerproduction import newtotpower
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#calculate power offset by subtracting production from consumption
power_offset = []

for i in range(len(newtotpower)):
    power_offset.append(tot_power[i]-newtotpower[i])

#create dates array
dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

#create a zeros line to show when power consumption is less than production
zeros = np.linspace(1,365,365)
for j in range(len(zeros)):
    zeros[j] = 0

#plot the results
plt.figure()
plt.plot(date, power_offset, color = 'green')
#plt.plot(date, zeros, color = 'black')
plt.title('Current Campus Power Offset vs Day')
plt.ylabel('Power (kW)')
plt.xlabel('Day')
plt.savefig('Poweroffset.png')