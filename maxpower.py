import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from intervalpower import bldg_power, bldg_names
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#take each building and find the max power
max_power = [max(name) for name in bldg_power]

#plot
plt.figure()
plt.plot(bldg_names, max_power, color = 'red')
plt.title('Current Maximum Power per Building')
plt.ylabel('Max Power (kW)')
plt.xlabel('Building')
plt.savefig('Maxpower.png')