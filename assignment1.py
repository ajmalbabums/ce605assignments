"""
Assignmet 1
Let X and Y be two independent identically distributed exponential random variables with mean and standard deviation 10. Let Z = X + Y; 
Find the pdf of Z, and obtain its parameters by independantly gnerating 1000 values for X and Y
"""

import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

lambda = 10
size = 1000

x = expon.rvs(loc=lambda, scale=1/lambda, size=size)
y = expon.rvs(loc=lambda, scale=1/lambda, size=size)

z = x + y


ax.hist(x, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)

ax.hist(y, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)


ax.hist(z, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)

plt.show()
