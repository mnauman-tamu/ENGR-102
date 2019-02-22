# program2a.py
#
# compute 3D interpolation at one point
#
# Muhammad Nauman
# UIN: 927008027
# September 5, 2018
# ENGR 102-213
#
# Lab 2b - B

import math

# Pre-processor
time1 = 13
x1 = 1
y1 = 3
z1 = 7

time2 = 84
x2 = 23
y2 = -5
z2 = 10

distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
time = time2 - time1
speed = distance/time
change_in_x = (x2-x1)/time
change_in_y = (y2-y1)/time
change_in_z = (z2-z1)/time

# Processor
currentTime = 50
realTime = currentTime - time1
currentX = x1 + (realTime * change_in_x)
currentY = y1 + (realTime * change_in_y)
currentZ = z1 + (realTime * change_in_z)


# Post-processor
print(currentX)
print(currentY)
print(currentZ)
