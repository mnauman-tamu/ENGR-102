# vectorOperations.py
#
# Computes angle between two vectors
#
# Muhammad Nauman
# UIN: 927008027
# September 10, 2018
# ENGR 102-213
#
# Lab 3B - 2

import math

x0 = input("Give the x-coordinate of the observer: ")
y0 = input("Give the y-coordinate of the observer: ")
z0 = input("Give the z-coordinate of the observer: ")
print()

x1 = input("Give the x-coordinate of the first point: ")
y1 = input("Give the y-coordinate of the first point: ")
z1 = input("Give the z-coordinate of the first point: ")
print()

x2 = input("Give the x-coordinate of the second point: ")
y2 = input("Give the y-coordinate of the second point: ")
z2 = input("Give the z-coordinate of the second point: ")
print()

dot_product = ((float(x1) * float(x2)) + (float(y1) * float(y2)) + (float(z1) * float(z2)))

v1 = math.sqrt((((float(x1)) - float(x0))**2) + (((float(y1)) - float(y0))**2) + (((float(z1)) - float(z0))**2))
v2 = math.sqrt((((float(x2)) - float(x0))**2) + (((float(y2)) - float(y0))**2) + (((float(z2)) - float(z0))**2))

angle = math.acos(dot_product/(v1*v2))
angle = angle*180/math.pi
print("The angle between the two points is " + str(angle) + "in degrees")
