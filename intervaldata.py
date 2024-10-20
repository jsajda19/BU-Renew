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
    
def total_energy(bldg1, bldg2, bldg3, bldg4, bldg5, b6, b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
    total = []
    for i in range(len(bldg1)):
        total.append(bldg1[i] + bldg2[i] + bldg3[i] + bldg4[i] + bldg5[i] + b6[i] + b7[i] + b8[i] + b9[i] + b10[i] + b11[i] + b12[i] + b13[i] + b14[i] + b15[i] + b16[i] + b17[i] + b18[i] + b19[i] + b20[i] + b21[i] + b22[i] + b23[i] + b24[i] + b25[i] + b26[i] + b27[i] + b28[i] + b29[i] + b30[i])
    return total

#list the file name as a variable
file = 'TCNJMeterData.xlsx'

#read the excel file and clean it by cutting out the first 2 rows
b1 = pd.read_excel(file, sheet_name='1',skiprows=0)
b2 = pd.read_excel(file, sheet_name='2',skiprows=0)
b3 = pd.read_excel(file, sheet_name='3',skiprows=0)
b4 = pd.read_excel(file, sheet_name='4',skiprows=0)
b5 = pd.read_excel(file, sheet_name='5',skiprows=0)
b6 = pd.read_excel(file, sheet_name='6',skiprows=0)
b7 = pd.read_excel(file, sheet_name='7',skiprows=0)
b8 = pd.read_excel(file, sheet_name='8',skiprows=0)
b9 = pd.read_excel(file, sheet_name='9',skiprows=0)
b10 = pd.read_excel(file, sheet_name='10',skiprows=0)
b11 = pd.read_excel(file, sheet_name='11',skiprows=0)
b12 = pd.read_excel(file, sheet_name='12',skiprows=0)
b13 = pd.read_excel(file, sheet_name='13',skiprows=0)
b14 = pd.read_excel(file, sheet_name='14',skiprows=0)
b15 = pd.read_excel(file, sheet_name='15',skiprows=0)
b16 = pd.read_excel(file, sheet_name='16',skiprows=0)
b17 = pd.read_excel(file, sheet_name='17',skiprows=0)
b18 = pd.read_excel(file, sheet_name='18',skiprows=0)
b19 = pd.read_excel(file, sheet_name='19',skiprows=0)
b20 = pd.read_excel(file, sheet_name='20',skiprows=0)
b21 = pd.read_excel(file, sheet_name='21',skiprows=0)
b22 = pd.read_excel(file, sheet_name='22',skiprows=0)
b23 = pd.read_excel(file, sheet_name='23',skiprows=0)
b24 = pd.read_excel(file, sheet_name='24',skiprows=0)
b25 = pd.read_excel(file, sheet_name='25',skiprows=0)
b26 = pd.read_excel(file, sheet_name='26',skiprows=0)
b27 = pd.read_excel(file, sheet_name='27',skiprows=0)
b28 = pd.read_excel(file, sheet_name='28',skiprows=0)
b29 = pd.read_excel(file, sheet_name='29',skiprows=0)
b30 = pd.read_excel(file, sheet_name='30',skiprows=0)

#parse out each set of energy data
b1en = b1['Centennial Hall (kWh)']
b2en = b2['Education Building (kWh)']
b3en = b3['1918 Pennington Rd(kWh)']
b4en = b4['Music Building (kWh)']
b5en = b5['June Walker Softball Field (kWh)']
b6en = b6['Ely House (kWh)']
b7en = b7['T/W Garage (kWh)']
b8en = b8['1940 Pennington Rd (kWh)']
b9en = b9['Travers Tower (kWh)']
b10en = b10['Forcina Hall (kWh)']
b11en = b11['1898 Pennington Rd (kWh)']
b12en = b12['Parking Lot 15 (kWh)']
b13en = b13['NA - North Fountain (kWh)']
b14en = b14['Hausdoerffer Hall (kW)']
b15en = b15['2000 Pennington RD East (kWh)']
b16en = b16['Main Blvd. East Parking (kWh)']
b17en = b17['Travers - Wolfe Service Link (kWh)']
b18en = b18['Campus Town SW Building (kWh)']
b19en = b19['Brewster House (kWh)']
b20en = b20['1894 Pennington Rd (kWh)']
b21en = b21['Packer Hall (kWh)']
b22en = b22['Panera Bread (kWh)']
b23en = b23['Green Hall (kWh)']
b24en = b24['Recreation Center (kWh)']
b25en = b25['Lions Stadium Building (kWh)']
b26en = b26['12 Lake Blvd (kWh)']
b27en = b27['Art and Interactive Multimedia Building (kWh)']
b28en = b28['1950 Pennington Rd (kWh)']
b29en = b29['1909 Pennington Rd (kWh)']
b30en = b30['Townhouses South (kWh)']

#split energy into daily lists
num_arrays = 365
daily1 = np.array_split(b1en,num_arrays)
daily2 = np.array_split(b2en,num_arrays)
daily3 = np.array_split(b3en,num_arrays)
daily4 = np.array_split(b4en,num_arrays)
daily5 = np.array_split(b5en,num_arrays)
daily6 = np.array_split(b6en,num_arrays)
daily7 = np.array_split(b7en,num_arrays)
daily8 = np.array_split(b8en,num_arrays)
daily9 = np.array_split(b9en,num_arrays)
daily10 = np.array_split(b10en,num_arrays)
daily11 = np.array_split(b11en,num_arrays)
daily12 = np.array_split(b12en,num_arrays)
daily13 = np.array_split(b13en,num_arrays)
daily14 = np.array_split(b14en,num_arrays)
daily15 = np.array_split(b15en,num_arrays)
daily16 = np.array_split(b16en,num_arrays)
daily17 = np.array_split(b17en,num_arrays)
daily18 = np.array_split(b18en,num_arrays)
daily19 = np.array_split(b19en,num_arrays)
daily20 = np.array_split(b20en,num_arrays)
daily21 = np.array_split(b21en,num_arrays)
daily22 = np.array_split(b22en,num_arrays)
daily23 = np.array_split(b23en,num_arrays)
daily24 = np.array_split(b24en,num_arrays)
daily25 = np.array_split(b25en,num_arrays)
daily26 = np.array_split(b26en,num_arrays)
daily27 = np.array_split(b27en,num_arrays)
daily28 = np.array_split(b28en,num_arrays)
daily29 = np.array_split(b29en,num_arrays)
daily30 = np.array_split(b30en,num_arrays)

#calculate the total energy per day per solar array
total1 = total_ind_energy(daily1)
total2 = total_ind_energy(daily2)
total3 = total_ind_energy(daily3)
total4 = total_ind_energy(daily4)
total5 = total_ind_energy(daily5)
total6 = total_ind_energy(daily6)
total7 = total_ind_energy(daily7)
total8 = total_ind_energy(daily8)
total9 = total_ind_energy(daily9)
total10 = total_ind_energy(daily10)
total11 = total_ind_energy(daily11)
total12 = total_ind_energy(daily12)
total13 = total_ind_energy(daily13)
total14 = total_ind_energy(daily14)
total15 = total_ind_energy(daily15)
total16 = total_ind_energy(daily16)
total17 = total_ind_energy(daily17)
total18 = total_ind_energy(daily18)
total19 = total_ind_energy(daily19)
total20 = total_ind_energy(daily20)
total21 = total_ind_energy(daily21)
total22 = total_ind_energy(daily22)
total23 = total_ind_energy(daily23)
total24 = total_ind_energy(daily24)
total25 = total_ind_energy(daily25)
total26 = total_ind_energy(daily26)
total27 = total_ind_energy(daily27)
total28 = total_ind_energy(daily28)
total29 = total_ind_energy(daily29)
total30 = total_ind_energy(daily30)

#calculate the total energy produced per day
newtotenergy = total_energy(total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12,total13,total14,total15,total16,total17,total18,total19,total20,total21,total22,total23,total24,total25,total26,total27,total28,total29,total30)

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

#plot energy vs timestamp
plt.plot(date, newtotenergy)
plt.title('Total Energy Consumed on Campus vs Day')
plt.ylabel('Energy (kWh)')
plt.xlabel('Day')
plt.savefig('Energyconsumption.png')