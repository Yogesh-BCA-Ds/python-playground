import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

np.random.seed(42)

# population parameter 
pm = 3.5
pstd = np.sqrt((np.random.randint(1,7)-3.5)**2).mean()

n = 30
sm = [np.random.randint(1,7,size=n).mean() for _ in range(5000)]
print("mean of sample:",np.mean(sm))

se = pstd/np.sqrt(n)
sd_of_sm = np.std(sm)
print("se:",se)
print("std:",sd_of_sm)
