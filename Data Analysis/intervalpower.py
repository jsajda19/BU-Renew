import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def gather_data(filename, bldgnames):
    bldg_power = []
    for i in range(len(bldgnames)):
        bldg_power.append(pd.read_excel(filename, sheet_name=str(bldgnames[i]),skiprows=0))
    return bldg_power


def gather_power(data):
    power = []
    for i in range(len(data)):
        pf = pd.DataFrame(data[i])
        power.append(pf["Electric Load (kW)"])
    return power

def split_daily(numarray,power):
    daily = []
    for i in range(len(power)):
        daily.append(np.array_split(power[i],numarray))
    return daily

def total_ind_power(power):
    return [sum(day) for day in power]

def total_power(newpower):
    newtotpower = np.zeros((365,1))
    for i in range(34):
        for j in range (365):
            newtotpower[j] = newtotpower[j] + newpower[i][j]
    return newtotpower


bldgnames = ['Athletic Recreation Center', 'Administrative Services Bldg', 'Armstrong Hall', 'Art & IMM Building',
             'Biology Building', 'Bliss Hall and Bliss Annex', 'Brower Student Center', 'Centennial Hall', 
             'Chemistry, Physics, Mathematics', 'Cromwell Hall', 'Decker Hall', 'Education Building', 'Eickoff Hall',
             'Ely Allen Brewster House', 'Forcina Hall', 'Green Hall', 'Hausdoerffer & Phelps Halls', 'Kendall Hall',
             'Maintenance Building', 'Music Building', 'New Residence Hall', 'Norsworthy Hall', 'Packer Hall',
             'Power House- Congretation Plant', 'R. Barbara Gitenstein Library', 'Roscoe L. West 68 Building',
             'School of Business', 'Social Science Building', 'Spiritual Center', 'STEM Building-Forum',
             'Townhouse West and East', 'Townhouses South', 'Travers Wolfe Hall', 'Trenton Hall']

filename = '8) TNCJ 15-Minute Meter Data v2.0.xlsx'

data = gather_data(filename, bldgnames)
power = gather_power(data)

numdays = 365
dailypower = split_daily(numdays,power)

newpower = [total_ind_power(bldg) for bldg in dailypower]

newtotpower = total_power(newpower)


print(len(newtotpower[0]))

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

#plot energy vs timestamp
plt.figure()
plt.plot(date, newtotpower)
plt.title('Total Power Consumed on Campus vs Day')
plt.ylabel('Power (kW)')
plt.xlabel('Day')
plt.savefig('Powerconsumption.png')