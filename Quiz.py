# Quiz.py
#
# computes: area and perimeter of circle; length of a side of square given area and perimeter
#
# Muhammad Nauman
# UIN: 927008027
# September 10, 2018
# ENGR 102-213
#
# Quiz

import math

# Pre-processor (1)
radius = 3.21

# Processor (1)
area = math.pi * (radius**2)
perimeter = 2 * math.pi * radius
side_area = math.sqrt(area)
side_perimeter = perimeter / 4

# Post-processor (1)
print("The area of the circle with radius " + str(radius) + " km is " + str(area) + " km^2.")
print("The perimeter of the circle with radius " + str(radius) + " km is " + str(perimeter) + " km.")
print()
print("The length of the side of a square with area " + str(area) + " km^2 is " + str(side_area) + " km.")
print()
print("The length of the side of a square with perimeter " + str(perimeter) + " km is " + str(side_perimeter) + " km.")
print()
