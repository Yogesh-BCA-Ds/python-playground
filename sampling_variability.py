import numpy as np
from matplotlib import pyplot as plt

# population
p = np.array([1,2,3,4,5,6,7,8,9,10])

# pretend to take these many samples
i_n = 1000

# size2
mean_s1 = []

for i in range(i_n):
    sample = np.random.choice(p,size=2,replace=True)
    sample_means = sample.mean()
    mean_s1.append(sample_means)

# size8
mean_s2 = []
for i in range(i_n):
    sample1 = np.random.choice(p,size=8,replace=True)
    m = sample1.mean()
    mean_s2.append(m)

print("n = 2 so std dev of means:",np.std(mean_s1))
print("n = 8 so std dev of means:",np.std(mean_s2))

plt.figure(figsize=(5,3))
plt.hist(mean_s1,bins=20,alpha=0.6,label="samll n = 2")
plt.hist(mean_s2,bins=20,alpha=0.6,label="large n = 8")
plt.xlabel("sample mean")
plt.ylabel("frequency")
plt.title("sample distribution")
plt.legend()
plt.show()
