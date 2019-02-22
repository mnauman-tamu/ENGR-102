# functions.py
#
# Plot a cubic function
#
# Muhammad Nauman, Alex B, Daniel H, Patrick Z
# UIN: 927008027
# Oct 10 2018
# ENGR 102-213
#
# Lab 3A-3

import numpy as np
# import matplotlib.pyplot as plt

# Pre-processor
A = int(input("Give A in Ax^3 + Bx^2 + Cx + D = 0: "))
while A == 0:
    A = int(input("Give A in Ax^3 + Bx^2 + Cx + D = 0: "))
B = int(input("Give B in Ax^3 + Bx^2 + Cx + D = 0: "))
C = int(input("Give C in Ax^3 + Bx^2 + Cx + D = 0: "))
D = int(input("Give D in Ax^3 + Bx^2 + Cx + D = 0: "))
minimum = int(input("Input the lower bound of the range of x-values: "))
maximum = int(input("Input the upper bound of the range of x-values: "))
arr = np.linspace(minimum, maximum, 1000)
print(arr)
newarr = np.zeros(1000)
print(newarr)
