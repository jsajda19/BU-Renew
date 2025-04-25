import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def gather_data(filename, bldgnames):
    bldg_power = []
    for i in range(len(bldgnames)):
        bldg_power.append(pd.read_excel(filename, sheet_name=str(bldgnames[i]),skiprows=2))
    return bldg_power


def gather_power(data):
    power = []
    for i in range(len(data)):
        ef = pd.DataFrame(data[i])
        power.append(ef["Energy (kWh)"])
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
    for i in range(5):
        for j in range (365):
            newtotpower[j] = newtotpower[j] + newpower[i][j]
    return newtotpower


bldgnames = ['Armstrong Hall', 'Brower Hall', 'Decker Hall', 'Packer Hall', 'Parking Lot 4&5']

filename = '10)TCNJ 15-minute Production Data v2.0.xlsx'

data = gather_data(filename, bldgnames)
power = gather_power(data)

numdays = 365
dailypower = split_daily(numdays,power)

newpower = [total_ind_power(bldg) for bldg in dailypower]

powerproduced = total_power(newpower)


print(len(powerproduced))


