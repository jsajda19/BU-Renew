import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
#from productiondata import newtotenergy
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def total_ind_power(power):
    total = []
    for i in range(len(power)):
        total.append(sum(power[i]))
    return total
    
def total_power(bldg1, bldg2, bldg3, bldg4, bldg5):
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
#timestamp_park = parking_lots['Timestamp']
park_kW = parking_lots['Power (kW)']
armstrong_power = Armstrong['Power (kW)']
brower_power = Brower['Power (kW)']
decker_power = Decker['Power (kW)']
packer_power = Packer['Power (kW)']


#split power and timestamp lists into daily lists
num_arrays = 365
daily_power = np.array_split(park_kW, num_arrays)
daily_armpower = np.array_split(armstrong_power, num_arrays)
daily_browpower = np.array_split(brower_power, num_arrays) 
daily_deckpower = np.array_split(decker_power, num_arrays)
daily_packpower = np.array_split(packer_power, num_arrays)

#calculate the total power per day per solar array
totparkpower = total_ind_power(daily_power)
totarmpower = total_ind_power(daily_armpower)
totbrowpower = total_ind_power(daily_browpower)
totdeckpower = total_ind_power(daily_deckpower)
totpackpower = total_ind_power(daily_packpower)

#calculate the total power produced per day
newtotpower = total_power(totparkpower,totarmpower,totbrowpower,totdeckpower,totpackpower)

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates


#estimate missing data by using a line
x = np.linspace(1,163,163)
slope = (30133.9675797 - 20178.784551866) / 163
y = slope*(x-15) + 20178.784551866

# #89.32906

for i in range(1,163,1):
    newtotpower[i+14] = y[i-1]

#plot power vs timestamp
plt.figure()
plt.plot(date, newtotpower)
plt.title('Total Power Produced on Campus vs Day')
plt.ylabel('Power (kWh)')
plt.xlabel('Day')
plt.savefig('Powerproduction.png')
