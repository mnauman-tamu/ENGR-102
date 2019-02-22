# roundoffError.py
#
# Compute boolean operations
#
# Muhammad Nauman
# UIN: 927008027
# September 17, 2018
# ENGR 102-213
#
# In collaboration with: Patrick Zhong, Daniel Huck, and Alexander Bogdan
#
# Lab 4A

import math

a = 1/7
print(a)
b = a*7
print(b)
print()

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
print()

from math import *
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
print()

TOL = 0.0001

# 1
a = 1/14
print(a)
b = 4*a
print(b)
c = 10*a
print(c)
d = b + c
print(d)
print("Is 1 the same as ((4/14)+(10/14))?")
print(1 == d)
print("Are 1 and " + str(d) + " within the tolerance of " + str(TOL) + "?")
e = (math.fabs(1-d)) < TOL
print(e)
print()

# 2
a = log(102)
print(a)
b = math.exp(a)
print(b)
print("Is e^ln(102) equal to 102?")
print(102 == b)
print("Are 102 and " + str(b) + " within the tolerance of " + str(TOL) + "?")
e = (math.fabs(1-b)) < TOL
print(e)
print()

# 3
print("\nIs (1/5+2/5)E100 the same as 0.6E100? " + str((1/5+2/5) * 10**100 == 0.6 * 10**100))
print((1/5+2/5) * 10**100)
print("Are (1/5+2/5)E100 and 0.6E100 within the tolerance of " + str(TOL) + "? " + str((1/5+2/5) * 10**100 - 0.6 * 10**100 <= TOL))
print()

# 4
print("\nIs sqrt(2) squared the same as 4-2? " + str(sqrt(2) ** 2 == (4-2)))
print(sqrt(2) ** 2)
print("Are sqrt(2) and 4-2 within the tolerance of " + str(TOL) + "? " + str(abs(sqrt(2) ** 2 - (4-2)) <= TOL))
print()

# 5
x = 51**(1/3)
print(x)
y = x * x * x
print(y)
z = sqrt(x) ** 6
print(z)
print("Is sqrt(x)^6 the same as x*x*x?")
print(y == z)
print("Are " + str(z) + " and " + str(y) + " within the tolerance of " + str(TOL) + "?")
e = (math.fabs(y - z)) < TOL
print(e)
print()

# 6
a = .3
b = .1
c = .2
e = b + c
print("is " + str(a) + " the same as " + str(b) + " plus " + str(c))
print("NO! it's " + str(e))
print("Are " + str(b+c) + " and " + str(a) + " within the tolerance of " + str(TOL) + "?")
e = (math.fabs((b+c) - a)) < TOL
print(e)
print()

# 7
x = 124 * 81.2 * 2 / 250
y = 124 * 8.12 * 2 / 25
print("is 124 * 81.2 * 2 / 250 the same as 124 * 8.12 * 2 / 25")
print("NO! it's " + str(x) + " and " + str(y))
print("Are " + str(x) + " and " + str(y) + " within the tolerance of " + str(TOL) + "?")
e = (math.fabs(y - x)) < TOL
print(e)
print()

# 8
x = 10**log10(54)
print(x)
print("Is 54 the same as as 10^log(54)?")
print(54 == x)
print("Are " + str(x) + " and 54 within the tolerance of " + str(TOL) + "?")
e = (math.fabs(x - 54)) < TOL
print(e)
print()
print()

# 1.3
p1 = [(1/5+2/5) * 10**100, 0.6 * 10**100]
p2 = [1.1 + 1, 1.1 + 1.00001]

print("\nTOLERANCE: ", TOL)

print("\n(a, b) -> ((1/5+2/5)E100, 0.6E100):", p1)
print("  should be the same.")
print("  within tolerance:", abs(p1[0] - p1[1]) <= TOL)

print("\n(x, y) -> (1.1 + 1, 1.1 + 1.00001):", p2)
print("  shouldn't be the same.")
print("  within tolerance:", abs(p2[0] - p2[1]) <= TOL)

