import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def total_ind_energy(energy):
    return [sum(day) for day in energy]
    
def total_energy(building_totals):
    return [sum(day) for day in zip(*building_totals)]

def gather_data(filename):
    bldg_energy = []
    for i in range(1,85,1):
        bldg_energy.append(pd.read_excel(file, sheet_name=str(i),skiprows=0))
    return bldg_energy
    
def gather_energy(names,data):
    return [data[i][names[i]].values for i in range(len(names))]

def split_daily(energy, num_array):
    return [np.array_split(daily,num_array) for daily in energy]
    

#list the file name as a variable
file = 'TCNJMeterData.xlsx'

bldg_names = [
    'Centennial Hall (kWh)', 'Education Building (kWh)', '1918 Pennington Rd(kWh)', 
    'Music Building (kWh)', 'June Walker Softball Field (kWh)', 'Ely House (kWh)', 
    'T/W Garage (kWh)', '1940 Pennington Rd (kWh)', 'Travers Tower (kWh)', 
    'Forcina Hall (kWh)', '1898 Pennington Rd (kWh)', 'Parking Lot 15 (kWh)', 
    'NA - North Fountain (kWh)', 'Hausdoerffer Hall (kWh)', '2000 Pennington RD East (kWh)', 
    'Main Blvd. East Parking (kWh)', 'Travers - Wolfe Service Link (kWh)', 
    'Campus Town SW Building (kWh)', 'Brewster House (kWh)', '1894 Pennington Rd (kWh)', 
    'Packer Hall (kWh)', 'Panera Bread (kWh)', 'Green Hall (kWh)', 
    'Recreation Center (kWh)', 'Lions Stadium Building (kWh)', '12 Lake Blvd (kWh)', 
    'Art and Interactive Multimedia Building (kWh)', '1950 Pennington Rd (kWh)', 
    '1909 Pennington Rd (kWh)', 'Townhouses South (kWh)', '6 Lake Blvd (kWh)',
    'Trenton Hall (kWh)', 'Forum (kWh)', 'Parking Lot 3 (kWh)', 'Armstrong Garage (kWh)',
    '100 Metzger Dr (kWh)', 'William Phelps Hall (kWh)', 'Campus Town West Building (kWh)',
    'Roscoe L. West Hall (kWh)', 'STEM Building (kWh)', 'Science Complex (kWh)',
    'Business Building (kWh)', 'Track (kWh)', 'Campus Town NW Building (kWh)',
    'TCNJ Library (kWh)', 'Eickhoff Hall (kWh)', 'Green Farm House (kWh)',
    'Administrative Services Building (kWh)', 'Social Science Building (kWh)',
    'Parking Lot 5 (kWh)', 'Cromwell Hall (kWh)', 'Townhouses West (kWh)',
    'New Residence Hall (kWh)', 'Allen House (kWh)', 'Kendall Hall (kWh)',
    'TCNJ Tennis Complex (kWh)', '14 Lake Blvd (kWh)', 'Bliss Hall (kWh)',
    'Campus Town East Building (kWh)', 'Brower Student Center (kWh)', '2 Lake Blvd (kWh)',
    'Armstrong Hall (kWh)', 'Parking Lot 4 (kWh)', 'Forcina Garage (kWh)',
    '2000 Pennington Rd West (kWh)', 'Metzger Garage (kWh)', 'Trinity United Methodist Church (kWh)',
    '1959 Pennington Rd (kWh)', '1908 Pennington Rd (kWh)', 'Maintenance Building (kWh)',
    'Decker Garage (kWh)', 'TCNJ Fitness Center at Campus Town (kWh)', '200 Metzger Dr (kWh)',
    'Norsworthy House (kWh)', 'Lake Ceva Pavilion (kWh)', 'Visitor Booth (kWh)',
    'Wolfe Tower (kWh)', '1963 Pennington Rd (kWh)', 'TCNJ Tennis Complex (kWh)',
    'Spiritual Center (kWh)', 'Field Hockey and Lacrosse Complex (kWh)',
    'Decker Hall (kWh)', '8 Lake Blvd (kWh)', 'Campus Town SE Building (kWh)'
]

bldg_data = gather_data(file)

bldg_energy = gather_energy(bldg_names,bldg_data)

num_array = 365
daily = split_daily(bldg_energy,num_array)

print(len(daily))

energy = [total_ind_energy(bldg) for bldg in daily]

tot_energy = total_energy(energy)

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

#plot energy vs timestamp
plt.plot(date, tot_energy)
plt.title('Total Energy Consumed on Campus vs Day')
plt.ylabel('Energy (kWh)')
plt.xlabel('Day')
plt.savefig('TestEnergyconsumption.png')
