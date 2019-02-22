# wellLocation.py
#
# Compute if point Q is in polygon ABCD
#
# Muhammad Nauman
# UIN: 927008027
# Engr 102-213
# September 24 2018
#
# Lab 5 Sample

# Pre-processor

# Enter the coordinates of the well
Wx = 1083606.857
Wy = 3130187.096

# Enter the coordinates of vertices of Block 16
Ax = 1083666.037
Ay = 3127482.653
Bx = 1081094.743
By = 3129730.776
Cx = 1084602.605
Cy = 3133639.561

# Processor

# Set a boolean to hold the T/F value of inside Block 16
in_B16 = True

# Get the equation of Line AB and find point Q
m = (By - Ay) / (Bx - Ax)
Qy = m * (Wx - Bx) + By
# print('Qy (m) = ' + str(Qy))

# Check if well is South of Line AB
if Wy < Qy:
    in_B16 = False

# Get the equation of Line BC and find point Q
m = (By - Cy) / (Bx - Cx)
Qy = m * (Wx - Bx) + By
# print('Qy (m) = ' + str(Qy))

# Check if well is South of Line BC
if Wy > Qy:
    in_B16 = False

# Post-processor
if in_B16:
    print("Well is located in Block 16")
else:
    print("Well is located outside Block 16")
