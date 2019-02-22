# plottingFunctions.py
#
# this program plots functions
#
# Daniel Huck, Muhammad Nauman, Patrick Zhong, Alexander Bodgan
# 10/8/18
# ENGR 201-213
# Week 7, activity 3

import numpy as np
import matplotlib.pyplot as plt

a = int(input('Enter an integer for the first coefficient of a cubic equation:  '))
b = int(input('Enter an integer for the second coefficient: '))
c = int(input('Enter the third coefficient: '))
d = int(input('Enter the final coefficient: '))
xmin = int(input('Enter a lower bound for the functions domain: '))
xmax = int(input('Enter an upper bound for the domain: '))
xint = (xmax-xmin)/10

xvals = np.linspace(xmin,xmax, 1000)
yvals = []
for x in xvals:
    fx = (a * x ** 3) + (b * x ** 2) + (c * x) + d
    yvals.append(fx)

plt.plot(xvals, yvals, 'b--', linewidth=1.0)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.grid(True)
plt.show()

xvalsnp = np.array(xvals)
yvalsnp = (a * xvalsnp ** 3) + (b * xvalsnp ** 2) + (c * xvalsnp) + d

elements = 1000
for x in range(elements):
    if xvals[x] == xvalsnp[x]:
        print('For element ' + str(x) + ', the f(x) data are the same.')
    elif xvals[x] != xvalsnp[x]:
        print('For element ' + str(x) + ', the f(x) data is not the same.')

print("x:    " + str(xvals[0:1000:111]))
print("f(x): " + str(yvals[0:1000:111]))



