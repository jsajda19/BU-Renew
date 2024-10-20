import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def total_ind_energy(energy):
    total = []
    for i in range(len(energy)):
        total.append(sum(energy[i]))
    return total
    
def total_energy(bldg1, bldg2, bldg3, bldg4, bldg5):
    total = []
    for i in range(len(bldg1)):
        total.append(bldg1[i] + bldg2[i] + bldg3[i] + bldg4[i] + bldg5[i])
    return total

#list the file name as a variable
file = 'TCNJSolarProductionData.xlsx'

#read the excel file and clean it by cutting out the first 2 rows
parking_lots = pd.read_excel(file, sheet_name='Parking Lot 4&5',skiprows=2)
Armstrong = pd.read_excel(file, sheet_name='Armstrong Hall',skiprows=2)
Brower = pd.read_excel(file, sheet_name='Brower Hall',skiprows=2)
Decker = pd.read_excel(file, sheet_name='Decker Hall',skiprows=2)
Packer = pd.read_excel(file, sheet_name='Packer Hall',skiprows=2)

#create separate arrays for each column in the parking lots tab
timestamp_park = parking_lots['Timestamp']
park_kW = parking_lots['Power (kW)']
park_energy = parking_lots['Energy (kWh)']
armstrong_energy = Armstrong['Energy (kWh)']
brower_energy = Brower['Energy (kWh)']
decker_energy = Decker['Energy (kWh)']
packer_energy = Packer['Energy (kWh)']


#split power, energy, and timestamp lists into daily lists
num_arrays = 365
daily_time = np.array_split(timestamp_park, num_arrays)
daily_power = np.array_split(park_kW, num_arrays)
daily_parkenergy = np.array_split(park_energy, num_arrays)
daily_armenerg = np.array_split(armstrong_energy, num_arrays)
daily_browenerg = np.array_split(brower_energy, num_arrays) 
daily_deckenerg = np.array_split(decker_energy, num_arrays)
daily_packenerg = np.array_split(packer_energy, num_arrays)

#calculate the total energy per day per solar array
totparkenerg = total_ind_energy(daily_parkenergy)
totarmenerg = total_ind_energy(daily_armenerg)
totbrowenerg = total_ind_energy(daily_browenerg)
totdeckenerg = total_ind_energy(daily_deckenerg)
totpackenerg = total_ind_energy(daily_packenerg)

#calculate the total energy produced per day
newtotenergy = total_energy(totparkenerg,totarmenerg,totbrowenerg,totdeckenerg,totpackenerg)

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates


#estimate missing data by using a line
x = np.linspace(1,152,152)
slope = (8533.321527807499 - 5044.6961379665) / 152
y = slope*(x-22) + 5044.6961379665

#89.32906

for i in range(1,152,1):
    newtotenergy[i+21] = y[i-1]

#plot energy vs timestamp
plt.plot(date, newtotenergy)
plt.title('Total Energy Produced on Campus vs Day')
plt.ylabel('Energy (kWh)')
plt.xlabel('Day')
plt.savefig('Energyproduction.png')

print(newtotenergy)
print(len(newtotenergy))
print(slope)
