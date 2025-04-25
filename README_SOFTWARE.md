# Data Analysis
The software used was all python 3.10.12. The only required libraries are matplotlib, pandas, and numpy.

intervalload.py

This file takes in the 15 minute interval load data provided by the competition and gets the daily energy consumption totals. This is done by taking the building names and going into the xlsx file under the tab with each building name. A pandas dataframe is created for each "Energy (kWh)" column. From here, the entries in each column are then added together so that each entry of the dataframe is now a vector with the daily energy consumed for each building. From there, the vectors are addaed across so that the final data frame is the daily energy consumption for the entire campus. This is then plotted on the y-axis with the x-axis being the date. This is plotted and stored using matplotlib.

intervalpower.py, intervalproduction.py, and powerproduction.py

intervalpower.py, intervalproduction.py, and powerproduction.py are the daily power consumption, daily energy production, and daily power production calculated in the same manner as intervalload.py except that instead of the energy column for each building it is either the power column of the 15 minute interval load data or the power column or the energy column in the energy production xlsx file.

monthlyenergy.py and monthlyproduction.py

monthlyenergy.py and monthlyproduction.py take in the daily energy production or consumption and add it together to create a monthly production and monthly consumption total. It also calculates the annual totals. The way these monthly totals were calculated by going through and adding up all of the days in each month and outputting it. The annual production or consumption was calculated by adding up the monthly data. The purpose of this is because one of the modeling softwares, Helioscope required the monthly and annual consumption data to correctly model the designed PV arrays.

poweranalysis.py and energyanalysis.py

The purpose of these files is to visualize the energy and power offset of the consumption by the existing PV arrays. The way this offset was calculated was simply taking the daily consumption data and subtracting the daily production data and then graphing it using matplotlib.


# Helioscope

Helioscope is an industry standard PV modeling software that was used to model the desired PV arrays. It has built in shading analysis, lidar data, roof setbacks, and different PV panels to test out. 








