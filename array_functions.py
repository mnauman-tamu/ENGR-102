# array_functions.py
#
# Compute the y-values of the function given x-values
#
# Muhammad Nauman
# Engr 102-213
# Oct 15 2018
#
# Week 8 Quiz

import math
import numpy as np

# Pre-processor
x = np.linspace(-3, 3, num=10)
y = []

# Processor
for i in x:
    ans = 3.41*math.exp(-(i**2)/1.45)
    y.append(ans)

# Post-processor
print("x                              y")
for i in range(10):
    print(x[i], end="\t\t\t\t\t\t")
    print(y[i])

