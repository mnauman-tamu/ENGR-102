# widgets.py
#
# Write a program that tells how many widgets have been produced
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 3d

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