import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

np.random.seed(42)

p = np.random.exponential(scale=1.0,size=100000)

def get_sample_mean(n,repeats=1000):
    means = []
    for _ in range(repeats):
        sample = np.random.choice(p,size=n)
        means.append(sample.mean())
    return means

sample_sizes = [5,30,100]
plt.figure(figsize=(12,4))
for i,n in enumerate(sample_sizes):
    means = get_sample_mean(n)
    plt.subplot(1,3,i+1)
    plt.hist(means,bins=30)
    plt.title(f"sample size {n}")
    plt.xlabel("mean")

plt.tight_layout()
plt.show()
