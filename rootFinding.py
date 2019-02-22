# rootFinding.py
#
# Estimate the root of a cubic polynomial given coefficients and a span interval
#
# Muhammad Nauman, Daniel Huck, Alexander Bodgan, Patrick Zhong
# UIN: 927008027
# 10-01-2018
# Engr 102-213
#
# Lab 6-1.a

import math

# Pre-processor
A = int(input("Give A in Ax^3 + Bx^2 + Cx + D = 0: "))
while A == 0:
    A = int(input("Give A in Ax^3 + Bx^2 + Cx + D = 0: "))
B = int(input("Give B in Ax^3 + Bx^2 + Cx + D = 0: "))
C = int(input("Give C in Ax^3 + Bx^2 + Cx + D = 0: "))
D = int(input("Give D in Ax^3 + Bx^2 + Cx + D = 0: "))
change = "Y"
TOL = 10**-6
a = 0
b = 0

# Processor
while change == "Y":
    a = int(input("Give the lower x-value that brackets the root: (a)"))
    b = int(input("Give the upper x-value that brackets the root: (b)"))
    c = (b - a) / 9
    x = a
    for i in range(10):
        print("f(" + str(x) + ") is " + str(A*x**3 + B*x**2 + C*x + D))
        x += c
    change = input("Do you wanna change the values of a and b? (Y/N) ")

fa = A*a**3 + B*a**2 + C*a + D
fb = A*b**3 + B*b**2 + C*b + D

if fa*fb > 0:
    print("Error: no root found in the interval (a,b)")
    exit()

count = 0
fnew = fa
new = a
while not math.fabs(fnew) <= TOL:
    new = (a+b)/2
    fnew = A*new**3 + B*new**2 + C*new + D
    if fa*fnew > 0:
        a = new
    elif fb*fnew > 0:
        b = new
    count += 1

# Post-processor
print("The x-value of a root is approximately " + str(new))
print("It took " + str(count) + " iterations")
