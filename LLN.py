# demonstrating law of large numbers

import numpy as np

'''
assume each customer will convert to new web site or not
if yes 1 else 0 this is the data and true population mean is 0.3 just
assumption
'''

np.random.seed(42) # it reproduce same sequence every time we run code

mu = 0.3 

n = 10000

data = np.random.binomial(n=1,p=mu,size=n)

cm = np.cumsum(data)

rm = cm/np.arange(1,n+1)

print(rm)
