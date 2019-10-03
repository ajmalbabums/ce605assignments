"""
Assignmet 1
Let X and Y be two independent identically distributed exponential random variables with mean and standard deviation 10. Let Z = X + Y; 
Find the pdf of Z, and obtain its parameters by independantly gnerating 1000 values for X and Y
"""

import numpy as np
from scipy.stats import expon, gamma
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

exp_lambda = 10
size = 1000

x = expon.rvs(loc=exp_lambda, scale=1/exp_lambda, size=size)
y = expon.rvs(loc=exp_lambda, scale=1/exp_lambda, size=size)

z = x + y

#
ax.hist(x, bins=50) #density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)

ax.hist(y, bins=50) #density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)


ax.hist(z, bins=50) #density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)


fit_alpha, fit_loc, fit_beta=gamma.fit(z)
print(fit_alpha, fit_loc, fit_beta)

plt.show()


