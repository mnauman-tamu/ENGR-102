# car.py
#
# Write a program that tells whether a feature is available
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 3c

# Pre-processor (car)
feature = input("Enter one of these features: Power Windows, V-6 Engine, Traction Control, Sport Package, Multi-tone "
                "Paint, or Parking Assist: ")
trim = input("Enter trim level: Base, Premium, or Luxury: ")

# Processor and Post-processor (car)
if (trim == "Base") and (feature == "V-6 Engine" or "Sport Package" or "Multi-tone Paint" or "Parking Assist") or (trim == "Premium" and feature == "Sport Package"):
    print("The feature is unavailable.")
elif ((trim == "Base") and (feature == "Traction Control")) or ((trim == "Premium") and (feature == "V-6 Engine" or "Multi-tone Paint" or "Parking Assist")) or (trim == "Luxury") and (feature == "Sport Package" or "Multi-tone Paint"):
    print("The feature is available for extra charge.")
else:
    print("The feature is standard.")
print()
