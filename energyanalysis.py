import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from productiondata import newtotenergy
from intervaldata import tot_energy
warnings.filterwarnings("ignore", category=FutureWarning)

#calculate energy offset by subtracting production from consumption
energy_offset = []

for i in range(len(newtotenergy)):
    energy_offset.append(tot_energy[i]-newtotenergy[i])

#plot the results
dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

zeros = np.linspace(1,365,365)
for j in range(len(zeros)):
    zeros[j] = 0

plt.figure()
plt.plot(date, energy_offset, color = 'green')
plt.plot(date, zeros, color = 'black')
plt.title('Current Campus Energy Offset vs Day')
plt.ylabel('Energy (kWh)')
plt.xlabel('Day')
plt.savefig('Energyoffset.png')
