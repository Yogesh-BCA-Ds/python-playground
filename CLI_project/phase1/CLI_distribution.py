import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats

np.random.seed(42) # gives same random output each time

sample_mean = [np.random.randint(1,7,size=5).mean() for _ in
range(1000)]
l = [1,2,3,4,5,6]
# sampled mean plot 
plt.figure(figsize=(4,4))
plt.hist(sample_mean,bins=30,
edgecolor="black",alpha=0.7)
plt.title("1000 single die rolls - sample mean")
plt.xlabel("average die value")
plt.ylabel("frequency")
plt.xticks(l)
plt.show()
