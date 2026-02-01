import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats

np.random.seed(42) # gives same random output each time

single_roll = np.random.randint(1,7,size=1000)

# raw population data of die roll 
plt.figure(figsize=(4,4))
plt.hist(single_roll,bins=np.arange(0.5,7.5,1),
edgecolor="black",alpha=0.7)
plt.title("1000 single die rolls - raw data")
plt.xlabel("die face")
plt.ylabel("frequency")
#plt.xticks(range(1,7))
plt.show()
