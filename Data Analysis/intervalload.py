import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def gather_data(filename, bldgnames):
    bldg_energy = []
    for i in range(len(bldgnames)):
        bldg_energy.append(pd.read_excel(filename, sheet_name=str(bldgnames[i]),skiprows=0))
    return bldg_energy


def gather_energy(data):
    energy = []
    for i in range(len(data)):
        ef = pd.DataFrame(data[i])
        energy.append(ef["Energy (kWh)"])
    return energy

def split_daily(numarray,energy):
    daily = []
    for i in range(len(energy)):
        daily.append(np.array_split(energy[i],numarray))
    return daily

def total_ind_energy(energy):
    return [sum(day) for day in energy]

def total_energy(newenergy):
    newtotenergy = np.zeros((365,1))
    for i in range(34):
        for j in range (365):
            newtotenergy[j] = newtotenergy[j] + newenergy[i][j]
    return newtotenergy


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
energy = gather_energy(data)

numdays = 365
dailyenergy = split_daily(numdays,energy)

newenergy = [total_ind_energy(bldg) for bldg in dailyenergy]

newtotenergy = total_energy(newenergy)


print(len(newtotenergy))

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

#plot energy vs timestamp
plt.figure()
plt.plot(date, newtotenergy)
plt.title('Total Energy Consumed on Campus vs Day')
plt.ylabel('Energy (kWh)')
plt.xlabel('Day')
plt.savefig('Energyconsumption.png')
