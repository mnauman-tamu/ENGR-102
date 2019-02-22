# shortPrograms.py
#
# Write 4 short programs
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 3

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

# Pre-processor (machine)
day = int(input("Enter a day: "))

# Processor and Post-processor (machine)
if day < 11:
    widgets = day * 10
elif 10 < day < 61:
    widgets = ((day - 10) * 40) + 100
elif 60 < day < 100:
    less = day - 60
    widgets = 2100 + (40 * less) - ((less**2 + less)/2)
else:
    day = 100
    less = day - 60
    widgets = 2100 + (40 * less) - ((less ** 2 + less) / 2)
print(str(widgets) + " widgets produced by day " + str(day))
print()



