import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#function definitions
def total_ind_power(power):
    return [sum(day) for day in power]
    
def total_power(building_totals):
    return [sum(day) for day in zip(*building_totals)]

def gather_data(filename):
    bldg_power = []
    for i in range(1,85,1):
        bldg_power.append(pd.read_excel(file, sheet_name=str(i),skiprows=0))
    return bldg_power
    
def gather_power(names,data):
    return [data[i][names[i]].values for i in range(len(names))]

def split_daily(power, num_array):
    return [np.array_split(daily,num_array) for daily in power]
    

#list the file name as a variable
file = 'TCNJMeterData.xlsx'

bldg_names = [
    'Centennial Hall (kW)', 'Education Building (kW)', '1918 Pennington Rd (kW)', 
    'Music Building (kW)', 'June Walker Softball Field (kW)', 'Ely House (kW)', 
    'T/W Garage (kW)', '1939 Pennington Rd (kW)', 'Travers Tower (kW)', 
    'Forcina Hall (kW)', '1898 Pennington Rd (kW)', 'Parking Lot 15 (kW)', 
    'NA - North Fountain (kW)', 'Hausdoerffer Hall (kW)', '2000 Pennington RD East (kW)', 
    'Main Blvd. East Parking (kW)', 'Travers - Wolfe Service Link (kW)', 
    'Campus Town SW Building (kW)', 'Brewster House (kW)', '1894 Pennington Rd (kW)', 
    'Packer Hall (kW)', 'Panera Bread (kW)', 'Green Hall (kW)', 
    'Recreation Center (kW)', 'Lions Stadium Building (kW)', '12 Lake Blvd (kW)', 
    'Art and Interactive Multimedia Building (kW)', '1950 Pennington Rd (kW)', 
    '1908 Pennington Rd (kW)', 'Townhouses South (kW)', '6 Lake Blvd (kW)',
    'Trenton Hall (kW)', 'Forum (kW)', 'Parking Lot 3 (kW)', 'Armstrong Garage (kW)',
    '101 Metzger Dr (kW)', 'William Phelps Hall (kW)', 'Campus Town West Building (kW)',
    'Roscoe L. West Hall (kW)', 'STEM Building (kW)', 'Science Complex (kW)',
    'Business Building (kW)', 'Track (kW)', 'Campus Town NW Building (kW)',
    'TCNJ Library (kW)', 'Eickhoff Hall (kW)', 'Green Farm House (kW)',
    'Administrative Services Building (kW)', 'Social Science Building (kW)',
    'Parking Lot 5 (kW)', 'Cromwell Hall (kW)', 'Townhouses West (kW)',
    'New Residence Hall (kW)', 'Allen House (kW)', 'Kendall Hall (kW)',
    'TCNJ Tennis Complex (kW)', '14 Lake Blvd (kW)', 'Bliss Hall (kW)',
    'Campus Town East Building (kW)', 'Brower Student Center (kW)', '2 Lake Blvd (kW)',
    'Armstrong Hall (kW)', 'Parking Lot 4 (kW)', 'Forcina Garage (kW)',
    '2000 Pennington Rd West (kW)', 'Metzger Garage (kW)', 'Trinity United Methodist Church (kW)',
    '1959 Pennington Rd (kW)', '1908 Pennington Rd (kW)', 'Maintenance Building (kW)',
    'Decker Garage (kW)', 'TCNJ Fitness Center at Campus Town (kW)', '200 Metzger Dr (kW)',
    'Norsworthy House (kW)', 'Lake Ceva Pavilion (kW)', 'Visitor Booth (kW)',
    'Wolfe Tower (kW)', '1963 Pennington Rd (kW)', 'TCNJ Tennis Complex (kW)',
    'Spiritual Center (kW)', 'Field Hockey and Lacrosse Complex (kW)',
    'Decker Hall (kW)', '8 Lake Blvd (kW)', 'Campus Town SE Building (kW)'
]

bldg_data = gather_data(file)

bldg_power = gather_power(bldg_names,bldg_data)

num_array = 365
daily = split_daily(bldg_power,num_array)

power = [total_ind_power(bldg) for bldg in daily]

tot_power = total_power(power)

dates_2023 = pd.date_range(start="January 1, 2023", end="December 31, 2023")
dates_list = dates_2023.to_list()  # List of dates
date = dates_2023.to_numpy()  # NumPy array of dates

#plot energy vs timestamp
plt.figure()
plt.plot(date, tot_power)
plt.title('Total Power Consumed on Campus vs Day')
plt.ylabel('Power (kW)')
plt.xlabel('Day')
plt.savefig('Powerconsumption.png')