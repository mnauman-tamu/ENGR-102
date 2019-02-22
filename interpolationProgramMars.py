# interpolationProgramMars.py
#
# compute distance around Mars
#
# Muhammad Nauman
# UIN: 927008027
# September 5, 2018
# ENGR 102-213
#
# Lab 2 - C2

import math

# Pre-processor
true_distance = 64000000
true_days = 304
speed = true_distance/true_days
circular_speed = speed * (1/3)
r = 3435
circular_distance = math.pi * r * 2

# Processor
circular_days = 579
new_distance = circular_speed * circular_days

# Post-processor
print(str(new_distance//circular_distance) + " orbits " + str(new_distance % circular_distance) + " km")
