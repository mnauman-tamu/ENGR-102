# BMI.py
#
# Write a program to find the BMI of a person
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 3a

# Pre-processor (BMI)
weight = float(input("Give your weight in kg: "))
height = float(input("Give your height in meters: "))

# Processor (BMI)
BMI = weight/(height**2)
print("Your BMI is " + str(BMI))

# Post-processor (BMI)
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("Your BMI is normal.")
elif 25.0 <= BMI <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
print()
