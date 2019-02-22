# quadraticEquation.py
#
# Write a program to solve for the roots of a quadratic equation
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 4

import math
import cmath

# Pre-processor
a = int(input("Enter a to solve for x in a*x^2 + b*x + c = 0: "))
b = int(input("Enter b to solve for x in a*x^2 + b*x + c = 0: "))
c = int(input("Enter c to solve for x in a*x^2 + b*x + c = 0: "))

# Processor
d = (b**2) - (4 * a * c)
if d < 0:
    ans1 = (-b + cmath.sqrt(d)) / (2*a)
    ans2 = (-b - cmath.sqrt(d)) / (2*a)
    print("The equation has two imaginary solutions: " + str(ans1) + " and " + str(ans2))
elif d == 0 and not a == 0:
    ans = (-b)/(2*a)
    print("This equation has 1 root: " + str(ans))
elif d > 0 and not a == 0:
    ans1 = (-b + math.sqrt(d)) / (2*a)
    ans2 = (-b - math.sqrt(d)) / (2*a)
    print("The two roots for this equation are: " + str(ans1) + " and " + str(ans2))
elif a == 0 and not b == 0:
    ans = -c/b
    print("This equation has 1 root: " + str(ans))
elif a == 0 and b == 0 and c == 0:
    print("There are infinitely many equations")
