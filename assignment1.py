"""
Assignment 1
Let X and Y be two independent identically distributed exponential random variables with mean and standard deviation 10.
Let Z = X + Y
Find the pdf of Z, and obtain its parameters by independently generating 1000 values for X and Y
"""

import numpy as np
from scipy.stats import expon, gamma
import matplotlib.pyplot as plt

# Inputs
exp_lambda = 0.15
size = 1000


# Generating random variables for X and Y and obtaining Z
x = expon.rvs(scale=1/exp_lambda, size=size)
y = expon.rvs(scale=1/exp_lambda, size=size)
z = x + y


# Defining Subplots
fig1, ax1 = plt.subplots(1, 1)
plt.title("Histogram and PDF for X with lambda = {0}".format(exp_lambda))
plt.xlabel("x")
plt.ylabel("PDF")

fig2, ax2 = plt.subplots(1, 1)
plt.title("Histogram and PDF for Y with lambda = {0}".format(exp_lambda))
plt.xlabel("y")
plt.ylabel("PDF")

fig3, ax3 = plt.subplots(1, 1)
plt.title("Histogram and PDF for Z")
plt.xlabel("z")
plt.ylabel("PDF")

# Plotting histograms for X, Y and Z
ax1.hist(x, bins=50, density=True, histtype='stepfilled', alpha=0.5)
ax2.hist(y, bins=50, density=True, histtype='stepfilled', alpha=0.5)
ax3.hist(z, bins=50, density=True, histtype='stepfilled', alpha=0.5)


# Finding parameters for gamma distribution, Z
fit_gamma_a, fit_loc, fit_beta = gamma.fit(z)
g_mean, g_var, g_skew, g_kurt = gamma.stats(fit_gamma_a, moments='mvsk')

# Plotting PDF over histograms for X, Y and Z
var1 = np.linspace(expon.ppf(0.01, scale=1/exp_lambda), expon.ppf(0.99, scale=1/exp_lambda), 100)
var2 = np.linspace(gamma.ppf(0.01, a=fit_gamma_a, loc=fit_loc, scale=fit_beta),
                   gamma.ppf(0.99, a=fit_gamma_a, loc=fit_loc, scale=fit_beta), 100)

rv1 = expon(scale=1/exp_lambda)
rv2 = gamma(a=fit_gamma_a, loc=fit_loc, scale=fit_beta)
ax1.plot(var1, rv1.pdf(var1), 'k-', lw=2, label='pdf')
ax2.plot(var1, rv1.pdf(var1), 'k-', lw=2, label='pdf')
ax3.plot(var2, rv2.pdf(var2), 'k-', lw=2, label='pdf')

fit_gamma_a = round(fit_gamma_a, 4)
gamma_v = round(1/fit_beta, 4)
print("Obtained parameters for Z, a = {0} and v = {1}".format(fit_gamma_a, gamma_v))
plt.title("Histogram and PDF for Z with a = {0} and v = {1}".format(fit_gamma_a, gamma_v))

plt.show()

