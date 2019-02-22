# StressStrain.py
#
# Report the stress for a given strain for steel
#
# Muhammad Nauman
# UIN: 927008027
# Engr 102-213
# September 24 2018
#
# Lab 5A

# Pre-processor
strain = float(input("Enter a strain percent between 0 and 25: "))
within_elastic = False
stress = 0

# Processor
if 0 <= strain < 1.5:
    stress = 167*strain
    within_elastic = True
elif 1.5 <= strain < 2.58:
    stress = 213.33*strain**3 - 1280*strain**2 + 2526.67*strain - 1380
elif 2.58 <= strain <= 25:
    stress = -0.98*strain**2 + 28.9*strain + 213.63
else:
    print("You must use a variable in the stated range")

# Post-processor
print("Your stress in MPa is " + str(stress))
if within_elastic:
    print("The strain is within elastic limit")
else:
    print("The strain is within the plastic deformation stage")

print("Stress in MPa for strain 5% is " + str(213.33*5**3 - 1280*5**2 + 2526.67*5 - 1380))
print("The strain 5% is within plastic deformation range.")
