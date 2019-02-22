# RN.py
#
# Write a program to find the reynold's number
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 3b

# Pre-processor (RN)
length = input("Length in ft: ")
velocity = input("Velocity in ft/s: ")
k_viscosity = input("Kinematic viscosity in ft^2/s: ")

# Processor (RN)
R_number = float(velocity) * float(length) / float(k_viscosity)

# Post_processor (RN)
print("The Reynolds number is: " + str(R_number))
if R_number < 2300:
    print("The flow is laminar.")
elif R_number > 4000:
    print("The flow is turbulent.")
else:
    print("The flow is transitional.")
print("Source: https://www.engineeringtoolbox.com/laminar-transitional-turbulent-flow-d_577.html")
print()

