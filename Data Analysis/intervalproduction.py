import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def gather_data(filename, bldgnames):
    bldg_energy = []
    for i in range(len(bldgnames)):
        bldg_energy.append(pd.read_excel(filename, sheet_name=str(bldgnames[i]),skiprows=2))
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
    for i in range(5):
        for j in range (365):
            newtotenergy[j] = newtotenergy[j] + newenergy[i][j]
    return newtotenergy


bldgnames = ['Armstrong Hall', 'Brower Hall', 'Decker Hall', 'Packer Hall', 'Parking Lot 4&5']

filename = '10)TCNJ 15-minute Production Data v2.0.xlsx'

data = gather_data(filename, bldgnames)
energy = gather_energy(data)

numdays = 365
dailyenergy = split_daily(numdays,energy)

newenergy = [total_ind_energy(bldg) for bldg in dailyenergy]

energyproduced = total_energy(newenergy)


print(len(energyproduced))


