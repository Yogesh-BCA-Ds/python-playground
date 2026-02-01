import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

np.random.seed(42)

sample_size = [2,5,10,30]

fig,axes = plt.subplots(2,2,figsize=(12,8))
axes = axes.ravel()

for idx,n in enumerate(sample_size):
    sample_mean = [np.random.randint(1,7,size=n).mean()
    for _ in range(1000)]
    axes[idx].hist(sample_mean,bins=30,edgecolor="black"
    ,alpha=0.7)
    axes[idx].set_title(f"n={n}")
    axes[idx].set_xlabel("sample mean")

plt.tight_layout()
plt.suptitle("clt at different sample sizes",y=1.02,
fontsize=14,weight="bold")
plt.show()

